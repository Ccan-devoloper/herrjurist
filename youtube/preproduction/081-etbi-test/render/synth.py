"""Spricht jede Einheit aus skript.py mit Piper (de-thorsten-low) und baut die Sprachspur.

Behebt den NFD-Zerfall von 'ç' (ich-Laut) in piper-tts 1.8, der sonst 'c' + Cedille liefert.
Ergebnis: stimme.wav (16 kHz mono) und cues.json (exakte Start/Ende je Einheit).
"""
import json, sys, wave, hashlib
import numpy as np
from piper import PiperVoice
from piper import phonemize_espeak as pe
sys.path.insert(0, ".")
from skript import S

_orig = pe.EspeakPhonemizer.phonemize
def _fix(self, *a, **k):
    out = []
    for sent in _orig(self, *a, **k):
        fixed = []
        for p in sent:
            if p == "̧" and fixed and fixed[-1] == "c":
                fixed[-1] = "ç"
            else:
                fixed.append(p)
        out.append(fixed)
    return out
pe.EspeakPhonemizer.phonemize = _fix

V = PiperVoice.load("../voice/de-thorsten-low.onnx")
SR = V.config.sample_rate
from piper.config import SynthesisConfig
cfg = SynthesisConfig(length_scale=0.96, noise_scale=0.6, noise_w_scale=0.7)

lead = 0.45
parts, cues, t = [np.zeros(int(lead * SR), np.int16)], [], lead
for i, s in enumerate(S):
    audio = np.concatenate([c.audio_int16_array for c in V.synthesize(s["text"], syn_config=cfg)])
    # Stille am Rand kappen, damit der Cue auf dem hörbaren Einsatz liegt
    thr = 400
    nz = np.nonzero(np.abs(audio) > thr)[0]
    a0, a1 = max(0, nz[0] - int(0.02 * SR)), min(len(audio), nz[-1] + int(0.06 * SR))
    audio = audio[a0:a1]
    d = len(audio) / SR
    cues.append(dict(i=i, start=round(t, 3), ende=round(t + d, 3), text=s["text"]))
    parts += [audio, np.zeros(int(s["pause"] * SR), np.int16)]
    t += d + s["pause"]
pcm = np.concatenate(parts)
with wave.open("../stimme.wav", "wb") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
json.dump(dict(dauer=round(len(pcm) / SR, 3), sr=SR, cues=cues), open("../cues.json", "w"), ensure_ascii=False, indent=1)
words = sum(len(s["text"].split()) for s in S)
print(f"Dauer {len(pcm)/SR:.2f}s, {words} Wörter, {len(S)} Einheiten, sha256 {hashlib.sha256(pcm.tobytes()).hexdigest()[:16]}")
