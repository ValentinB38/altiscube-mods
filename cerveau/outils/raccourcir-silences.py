# Raccourcit des silences précis d'une voix off (après certains mots) avec un léger fondu, sans toucher au reste.
# Usage : python raccourcir-silences.py voix.mp3 voix.words.json sortie.wav "why.=0.5" "underneath,=0.4" ...
import sys, json, subprocess, numpy as np
src, wj, dst, rules = sys.argv[1], sys.argv[2], sys.argv[3], dict(r.split('=') for r in sys.argv[4:])
SR = 44100
x = np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',src,'-f','f32le','-ac','1','-ar',str(SR),'-'],capture_output=True,check=True).stdout, np.float32).copy()
w = json.load(open(wj)); cuts = []
for i in range(len(w)-1):
    keep = rules.get(w[i]['w'])
    gap = w[i+1]['s'] - w[i]['e']
    if keep and gap > float(keep):
        mid = (w[i]['e'] + w[i+1]['s']) / 2; rm = gap - float(keep)
        cuts.append((int((mid - rm/2)*SR), int((mid + rm/2)*SR)))
out, pos, fade = [], 0, int(0.01*SR)
for a, b in cuts:
    seg = x[pos:a].copy(); seg[-fade:] *= np.linspace(1, 0, fade)
    out.append(seg); pos = b
    x[pos:pos+fade] *= np.linspace(0, 1, fade)
out.append(x[pos:]); y = np.concatenate(out)
subprocess.run(['ffmpeg','-v','error','-y','-f','f32le','-ar',str(SR),'-ac','1','-i','-',dst], input=y.tobytes(), check=True)
print(f'{len(cuts)} silences raccourcis, {len(x)/SR:.2f}s -> {len(y)/SR:.2f}s')
