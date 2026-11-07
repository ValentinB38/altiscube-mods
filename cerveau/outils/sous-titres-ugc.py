# Sous-titres façon UGC (style éline) sur une vidéo : transcription mot à mot puis incrustation.
# Usage : python sous-titres-ugc.py entree.mp4 sortie.mp4 (faster-whisper et ffmpeg avec libass requis)
import sys, subprocess, numpy as np, os
from faster_whisper import WhisperModel
src, dst = sys.argv[1], sys.argv[2]
FONTS = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'polices')
pcm = subprocess.run(['ffmpeg', '-v', 'error', '-i', src, '-f', 'f32le', '-ac', '1', '-ar', '16000', '-'], capture_output=True, check=True).stdout
segs, _ = WhisperModel('small', device='cpu', compute_type='int8').transcribe(np.frombuffer(pcm, np.float32), beam_size=5, word_timestamps=True)
raw = [w for s in segs for w in s.words]
words = []
for w in raw:
    if words and w.word.strip().startswith('-'):
        words[-1].word = words[-1].word + w.word.strip(); words[-1].end = w.end
    else:
        words.append(w)
groups, cur = [], []
for k, w in enumerate(words):
    cur.append(w)
    nxt = words[k + 1].word.strip() if k + 1 < len(words) else ''
    end_sentence = w.word.strip()[-1:] in '.?!'
    if end_sentence or (len(cur) >= 4 and not nxt[-1:] in '.?!') or (w.word.strip()[-1:] == ',' and len(cur) >= 2):
        groups.append(cur); cur = []
if cur: groups.append(cur)
ts = lambda t: f'{int(t // 3600)}:{int(t % 3600 // 60):02d}:{t % 60:05.2f}'
w_, h_ = map(int, subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=width,height', '-of', 'csv=p=0', src], capture_output=True, text=True).stdout.strip().split(','))
ev = []
for j, g in enumerate(groups):
    st = g[0].start; en = groups[j + 1][0].start if j + 1 < len(groups) else g[-1].end + 0.5
    txt = ' '.join(x.word.strip() for x in g).replace('Unlined', 'unlined')
    ev.append(f'Dialogue: 0,{ts(st)},{ts(en)},Cap,,0,0,0,,{txt}')
    print(f'{st:5.2f}-{en:5.2f} {txt}')
ass = dst.rsplit('.', 1)[0] + '.ass'
open(ass, 'w').write(f"""[Script Info]
ScriptType: v4.00+
PlayResX: {w_}
PlayResY: {h_}

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,DM Sans 9pt,{round(h_ * 0.03)},&H00FFFFFF,&H00FFFFFF,&H00000000,&H80000000,1,0,0,0,100,100,0,0,1,{max(2, round(h_ * 0.0025))},1,2,40,40,{round(h_ * 0.30)},1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
""" + '\n'.join(ev) + '\n')
subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', src, '-vf', f"ass='{ass}':fontsdir='{FONTS}'", '-c:v', 'libx264', '-crf', '18', '-preset', 'medium', '-pix_fmt', 'yuv420p', '-c:a', 'copy', '-movflags', '+faststart', dst], check=True)
print('ok', dst)
