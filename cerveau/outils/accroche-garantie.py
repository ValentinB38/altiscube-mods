# Variante d'accroche « garantie » : un bandeau en haut pendant les 3,6 premières secondes, sur la vidéo sous-titrée.
# Usage : python3 accroche-garantie.py source_sous_titree.mp4 sortie.mp4
import os, subprocess, sys, tempfile
from PIL import Image, ImageDraw, ImageFont

src, out = sys.argv[1:3]
HERE = os.path.dirname(os.path.abspath(__file__)); FONTS = os.path.join(HERE, 'polices')
F = lambda n, s: ImageFont.truetype(os.path.join(FONTS, n), s)
W, H = 1080, 1920
RED, INK, CREAM = (196, 18, 47), (42, 20, 24), (255, 248, 245)

def center(d, y, text, f, fill):
    b = f.getbbox(text); d.text(((W - (b[2] - b[0])) // 2 - b[0], y), text, font=f, fill=fill)

im = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
d.rounded_rectangle((90, 100, W - 90, 470), 40, fill=CREAM + (244,))
center(d, 128, 'Smoother-looking lip lines', F('BodoniModa-Black.ttf', 64), INK)
center(d, 212, 'in about 60 seconds.', F('BodoniModa-Black.ttf', 64), INK)
f = F('DMSans-Bold.ttf', 48); t = 'Or your money back'; b = f.getbbox(t); pw = b[2] - b[0] + 80
d.rounded_rectangle(((W - pw) // 2, 318, (W + pw) // 2, 418), 50, fill=RED)
d.text(((W - (b[2] - b[0])) // 2 - b[0], 368 - (b[3] - b[1]) // 2 - b[1]), t, font=f, fill=(255, 255, 255))
png = os.path.join(tempfile.mkdtemp(), 'banner.png'); im.save(png)

fc = "[1:v]format=rgba,fade=t=out:st=3.3:d=0.3:alpha=1[b];[0:v][b]overlay=0:0:enable='lte(t,3.6)'[v]"
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', src, '-loop', '1', '-t', '3.7', '-i', png, '-filter_complex', fc,
                '-map', '[v]', '-map', '0:a', '-c:v', 'libx264', '-crf', '19', '-pix_fmt', 'yuv420p', '-c:a', 'copy',
                '-movflags', '+faststart', out], check=True)
subprocess.run(['rm', '-rf', os.path.dirname(png)])
print('ok', out)
