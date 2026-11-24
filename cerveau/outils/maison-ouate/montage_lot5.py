# Lot 5 (23/11) : vidéos d'essayage au montage de la gagnante V1 (« New Sales ad »), nouvelles accroches
# reformulées d'après la veille Domelyah du 23/11. Recréé après la perte du dossier de travail.
# Format calqué sur la pub n°1 du concurrent (relevé du 06/11) : 720x1280, 30 i/s, 8 plans (gros plan / miroir),
# accroche en bulle au centre toute la vidéo, appel à l'action empilé dessous à partir de 7,5 s.
import os, sys, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from captions import caption, overlay_png
ROOT = os.path.join(HERE, '..'); RAW = os.path.join(ROOT, 'pubs', 'raw'); OUT = os.path.join(ROOT, 'pubs', 'out', 'lot5'); TMP = os.path.join(OUT, '_tmp')
os.makedirs(TMP, exist_ok=True)
W, H = 720, 1280
MUSIC = os.path.join(RAW, 'musique.mp3')
HOOK_Y, CTA_Y, CTA_T = 0.545, 0.657, 7.5


def src(clip):
    return os.path.join(RAW, 'gp', f'c-{clip}.mp4') if clip.startswith('gp-') else os.path.join(RAW, f'c-{clip}.mp4')


V1 = [('gp-creme', 0.0, 1.5), ('creme', 0.3, 1.7), ('gp-noir', 0.5, 1.9), ('noir', 0.8, 2.2), ('gp-bleu', 0.3, 1.8), ('bleu', 0.6, 2.0), ('gp-lilas', 0.0, 1.5), ('lilas', 0.8, 2.3)]
V2 = [('gp-rose', 0.0, 1.6), ('rose', 1.2, 2.6), ('gp-bleu', 2.0, 3.4), ('noir', 0.8, 2.2), ('gp-lilas', 3.0, 4.4), ('lilas', 1.0, 2.4), ('gp-creme', 3.2, 4.6), ('creme', 2.5, 3.9)]
V3 = [('gp-noel', 0.0, 1.6), ('noel', 0.0, 1.5), ('gp-rose', 1.6, 3.0), ('noel', 3.2, 4.6), ('gp-bleu', 0.3, 1.7), ('lilas', 0.5, 1.9), ('gp-noel', 3.0, 4.5), ('noel', 1.6, 3.0)]
VIDEOS = {
    'V15-il-a-compris': {'segments': V1, 'hook': ['POV : il a enfin compris', 'ce qu’elle voulait vraiment 🎄']},
    'V16-elle-ne-le-quitte-plus': {'segments': V3, 'hook': ['POV : elle l’ouvre…', '…et ne le quitte plus 🎁']},
    'V17-la-3e-offerte': {'segments': V2, 'hook': ['Ta chérie, ta mère, ta sœur :', 'la 3e est offerte 🎁']},
    'V18-messieurs': {'segments': V1, 'hook': ['Messieurs, son cadeau de Noël', 'est réglé en 2 minutes 🎁']},
}
CTA = ['Offrez un peu de douceur', 'avec Maison Ouate 👇']


def run(cmd):
    subprocess.run(cmd, check=True)


for name, cfg in VIDEOS.items():
    segs = cfg['segments']; total = round(sum(b - a for _, a, b in segs), 2)
    hook = os.path.join(TMP, f'{name}-hook.png'); cta = os.path.join(TMP, f'{name}-cta.png')
    overlay_png(hook, (W, H), [(caption(cfg['hook'], size=34), HOOK_Y)])
    overlay_png(cta, (W, H), [(caption(CTA, size=34), CTA_Y)])
    inputs, chains = [], []
    for i, (clip, a, b) in enumerate(segs):
        inputs += ['-i', src(clip)]
        chains.append(f'[{i}:v]trim={a}:{b},setpts=PTS-STARTPTS,scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps=30,format=yuv420p[s{i}]')
    n = len(segs)
    inputs += ['-i', hook, '-i', cta, '-i', MUSIC]
    fc = ';'.join(chains) + ';' + ''.join(f'[s{i}]' for i in range(n)) + f'concat=n={n}:v=1:a=0[base];' \
         f'[base][{n}:v]overlay=0:0[v1];' \
         f"[v1][{n+1}:v]overlay=0:0:enable='gte(t,{CTA_T})'[v];" \
         f'[{n+2}:a]atrim=0:{total},asetpts=PTS-STARTPTS,afade=t=in:st=0:d=0.2,afade=t=out:st={total-0.7}:d=0.7,volume=0.9[a]'
    out = os.path.join(OUT, f'{name}.mp4')
    run(['ffmpeg', '-v', 'error', '-y', *inputs, '-filter_complex', fc, '-map', '[v]', '-map', '[a]', '-c:v', 'libx264', '-crf', '18', '-preset', 'medium',
         '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '160k', '-movflags', '+faststart', '-t', str(total), out])
    print('ok', name, total, 's')
