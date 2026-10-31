# Sous-titres auto YouTube (.srt) -> texte lisible : garde la dernière ligne de chaque bloc (les autres sont des répétitions), repère toutes les minutes.
import re, sys
blocks = open(sys.argv[1], encoding='utf-8').read().strip().split('\n\n')
out, last, lastmin = [], None, -1
for b in blocks:
    L = b.split('\n')
    if len(L) < 3: continue
    m = re.match(r'(\d+):(\d+):(\d+)', L[1]); t = int(m[1])*3600 + int(m[2])*60 + int(m[3])
    line = L[-1].strip()
    if not line or line == last: continue
    last = line
    if t // 60 != lastmin: out.append(f'\n[{t//60:02d}:00] '); lastmin = t // 60
    out.append(line + ' ')
open(sys.argv[2], 'w').write(re.sub(r'[ \t]+', ' ', ''.join(out)))
