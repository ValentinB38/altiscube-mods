# Accroche « médaillon » : gros plan macro des rides + feutre rouge qui entoure la zone + l'actrice en médaillon,
# pendant les N premières images, puis la vidéo d'origine en plein écran. Son et sous-titres d'origine conservés.
# Usage : python3 accroche-medaillon.py source.mp4 macro.png captions.ass sortie.mp4 nb_images cx cy rx ry crop_x crop_y crop_size "ligne 1" "ligne 2"
import math, os, random, subprocess, sys, tempfile
from PIL import Image, ImageDraw, ImageFilter, ImageFont

src, macro, ass, out = sys.argv[1:5]
N = int(sys.argv[5]); cx, cy, rx, ry = map(int, sys.argv[6:10]); kx, ky, ks = map(int, sys.argv[10:13]); l1, l2 = sys.argv[13:15]
HERE = os.path.dirname(os.path.abspath(__file__)); FONTS = os.path.join(HERE, 'polices')
F = lambda n, s: ImageFont.truetype(os.path.join(FONTS, n), s)
W, H, FPS = 1080, 1920, 30
RED, INK, CREAM = (196, 18, 47), (42, 20, 24), (255, 248, 245)
tmp = tempfile.mkdtemp()

# Images de la source pour le médaillon
subprocess.run(['ffmpeg', '-v', 'error', '-i', src, '-frames:v', str(N), os.path.join(tmp, 's%04d.png')], check=True)

base = Image.open(macro).convert('RGB')
s = W / base.width; base = base.resize((W, round(base.height * s)), Image.LANCZOS).crop((0, 0, W, H))

# Trait de feutre : ellipse irrégulière, qui dépasse un peu son point de départ
random.seed(7)
pts = []
for i in range(181):
    a = -math.pi * 0.6 + 2.15 * math.pi * i / 180
    w = 1 + 0.035 * math.sin(3 * a + 0.8) + random.uniform(-0.006, 0.006)
    pts.append((cx + rx * w * math.cos(a), cy + ry * w * math.sin(a)))

D = 460; ring = 10
mask = Image.new('L', (D, D), 0); ImageDraw.Draw(mask).ellipse((0, 0, D - 1, D - 1), fill=255)
shadow = Image.new('L', (D + 60, D + 60), 0); ImageDraw.Draw(shadow).ellipse((30, 36, D + 30, D + 36), fill=110)
shadow = shadow.filter(ImageFilter.GaussianBlur(14))
MX, MY = 36, H - D - 50

banner = Image.new('RGBA', (W, H), (0, 0, 0, 0)); bd = ImageDraw.Draw(banner)
f1, f2 = F('BodoniModa-Black.ttf', 70), F('BodoniModa-Black.ttf', 70)
w1 = f1.getbbox(l1)[2] - f1.getbbox(l1)[0]; w2 = f2.getbbox(l2)[2] - f2.getbbox(l2)[0]
bw = max(w1, w2) + 90
bd.rounded_rectangle(((W - bw) // 2, 110, (W + bw) // 2, 330), 36, fill=CREAM + (240,))
bd.text(((W - w1) // 2 - f1.getbbox(l1)[0], 130), l1, font=f1, fill=INK)
bd.text(((W - w2) // 2 - f2.getbbox(l2)[0], 222), l2, font=f2, fill=RED)

for i in range(N):
    t = i / FPS
    fr = base.copy(); d = ImageDraw.Draw(fr)
    p = min(1, max(0, (t - 0.5) / 1.3))
    k = int(p * (len(pts) - 1))
    if k > 1:
        d.line(pts[:k + 1], fill=(222, 24, 38), width=16, joint='curve')
        for q in (pts[0], pts[k]): d.ellipse((q[0] - 8, q[1] - 8, q[0] + 8, q[1] + 8), fill=(222, 24, 38))
    z = 1 + 0.07 * t / (N / FPS)
    bw2, bh2 = W / z, H / z; x0 = min(max(cx - bw2 / 2, 0), W - bw2); y0 = min(max(cy - bh2 / 2, 0), H - bh2)
    fr = fr.crop((round(x0), round(y0), round(x0 + bw2), round(y0 + bh2))).resize((W, H), Image.LANCZOS)
    sfr = Image.open(os.path.join(tmp, f's{i + 1:04d}.png')).convert('RGB').crop((kx, ky, kx + ks, ky + ks)).resize((D, D), Image.LANCZOS)
    fr.paste((20, 10, 12), (MX - 30, MY - 30), shadow.point(lambda v: v // 2))
    ImageDraw.Draw(fr).ellipse((MX - ring, MY - ring, MX + D + ring, MY + D + ring), fill=(255, 255, 255))
    fr.paste(sfr, (MX, MY), mask)
    fr = Image.alpha_composite(fr.convert('RGBA'), banner).convert('RGB')
    fr.save(os.path.join(tmp, f'h{i:04d}.png'))

hook = os.path.join(tmp, 'hook.mp4')
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-framerate', str(FPS), '-i', os.path.join(tmp, 'h%04d.png'),
                '-vf', 'gblur=sigma=0.5,noise=c0s=9:c0f=t,format=yuv420p', '-c:v', 'libx264', '-crf', '17', hook], check=True)
fc = (f'[0:v]setpts=PTS-STARTPTS[h];[1:v]trim=start_frame={N},setpts=PTS-STARTPTS,format=yuv420p[t];'
      f"[h][t]concat=n=2:v=1:a=0[v];[v]subtitles='{ass}':fontsdir='{FONTS}'[vs]")
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', hook, '-i', src, '-filter_complex', fc, '-map', '[vs]', '-map', '1:a',
                '-c:v', 'libx264', '-crf', '19', '-preset', 'medium', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '160k',
                '-movflags', '+faststart', '-shortest', out], check=True)
subprocess.run(['rm', '-rf', tmp])
print('ok', out)
