# Horodatage mot par mot d'une voix off (faster-whisper), sortie JSON.
import sys, json, subprocess, numpy as np
from faster_whisper import WhisperModel
m = WhisperModel("small", device="cpu", compute_type="int8")
for p in sys.argv[1:]:
    x = np.frombuffer(subprocess.run(["ffmpeg","-v","error","-i",p,"-f","f32le","-ac","1","-ar","16000","-"],capture_output=True).stdout, np.float32)
    segs,_ = m.transcribe(x, beam_size=5, word_timestamps=True, vad_filter=False)
    words = [{"w": w.word.strip(), "s": round(w.start,2), "e": round(w.end,2)} for s in segs for w in s.words]
    json.dump(words, open(p.rsplit('.',1)[0]+'.words.json','w'), indent=0)
    print(p, len(words), " ".join(w["w"] for w in words))
