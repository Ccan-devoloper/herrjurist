"""Spracherkennung der finalen Sprachspur (faster-whisper, Modell als Argument: small|medium) mit Wortzeiten.
Ausgabe: JSON-Liste [Start, Ende, Wort] und je Segment der erkannte Text (Gegenprobe zu pruefe_folge.py).
Aufruf: python3 asr_119.py medium <ausgabe.json>"""
import json, sys, wave
import numpy as np
from scipy.signal import resample_poly
from faster_whisper import WhisperModel

modell = sys.argv[1]
m = WhisperModel(modell, device="cpu", compute_type="int8", cpu_threads=2)
segs, _ = m.transcribe("../stimme.wav", language="de", beam_size=5, word_timestamps=True)
woerter = [[round(w.start, 2), round(w.end, 2), w.word.strip()] for s in segs for w in s.words]
cj = json.load(open("../cues.json"))
w = wave.open("../stimme.wav"); sr = w.getframerate()
x = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768
je = []
for s in cj["segmente"]:
    y = resample_poly(x[int(s["start"] * sr):int(s["ende"] * sr)], 1, 3).astype(np.float32)
    t, _ = m.transcribe(y, language="de", beam_size=5, condition_on_previous_text=False)
    je.append(dict(nr=s["i"] + 1, rolle=s["rolle"], skript=s["text"], erkannt=" ".join(z.text.strip() for z in t)))
json.dump(dict(modell=modell, woerter=woerter, segmente=je), open(sys.argv[2], "w"), ensure_ascii=False, indent=1)
print(len(woerter), "Wörter")
