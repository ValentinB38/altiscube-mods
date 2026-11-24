# Compare des voix candidates : durée parlée, F0 médiane (voix grave = plus mature), variabilité de F0 (expressivité), transcription.
import sys, subprocess, numpy as np
from faster_whisper import WhisperModel
m = WhisperModel('small', device='cpu', compute_type='int8')
def pcm(p, sr=16000):
    return np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',p,'-f','f32le','-ac','1','-ar',str(sr),'-'],capture_output=True).stdout, np.float32)
def f0s(x, sr=16000, fl=640, hop=160):
    out=[]
    for i in range(0, len(x)-fl, hop):
        f = x[i:i+fl]; f = f - f.mean()
        if np.sqrt((f**2).mean()) < 0.02: continue
        ac = np.correlate(f, f, 'full')[fl-1:]; ac /= ac[0] + 1e-9
        lo, hi = sr//400, sr//70
        k = lo + np.argmax(ac[lo:hi])
        if ac[k] > 0.5: out.append(sr/k)
    return np.array(out)
for p in sys.argv[1:]:
    x = pcm(p); f = f0s(x)
    segs,_ = m.transcribe(x, beam_size=5, word_timestamps=True)
    ws = [w for s in segs for w in s.words]
    st, en = ws[0].start, ws[-1].end
    print(f"{p.split('/')[-1]:12s} parole {st:.2f}-{en:.2f} ({en-st:.1f}s) F0 méd {np.median(f):.0f} Hz, écart {np.std(12*np.log2(f/np.median(f))):.1f} demi-tons")
    print('   ', ' '.join(w.word.strip() for w in ws))
