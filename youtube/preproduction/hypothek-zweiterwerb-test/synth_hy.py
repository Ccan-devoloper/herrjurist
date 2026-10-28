"""Vertont skript2.py mit Piper (de-thorsten-low) und legt jede [marke] auf den Wortbeginn.

Die Wortzeiten stammen aus den Dauer-Ausgaben des Sprachmodells selbst (Phonem-Alignments),
nicht aus einer nachträglichen Schätzung. Ausgabe: stimme.wav (16 kHz mono), cues.json.
"""
import json, re, sys, wave, hashlib
import numpy as np
from piper import PiperVoice
from piper import phonemize_espeak as pe
from piper.config import SynthesisConfig
sys.path.insert(0, ".")
from skript_hy import SEGMENTE

# piper-tts 1.8 zerlegt 'ç' (ich-Laut) per NFD in 'c' + Cedille, die das Modell nicht kennt.
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

V = PiperVoice.load("../../etb/voice/de-thorsten-low.onnx", include_alignments=True)
SR = V.config.sample_rate
CFG = SynthesisConfig(length_scale=0.97, noise_scale=0.6, noise_w_scale=0.7)
PUNKT = set(".,:;!?-–\"'()^$_ ")

def woerter(phon_saetze):
    n = 0
    for satz in phon_saetze:
        for tok in "".join(satz).split(" "):
            if any(ch not in PUNKT for ch in tok):
                n += 1
    return n

def wortstarts(chunks):
    """Startsample jedes Wortes über alle Satz-Chunks."""
    starts, pos = [], 0
    for ch in chunks:
        neu = True
        for al in ch.phoneme_alignments:
            p = al.phoneme
            if p == " ":
                neu = True
            elif p not in PUNKT and neu:
                starts.append(pos); neu = False
            pos += int(al.num_samples)
    return starts, pos

lead = 0.5
parts, cues, segs, t = [np.zeros(int(lead * SR), np.int16)], {}, [], lead
for i, (roh, pause) in enumerate(SEGMENTE):
    text = re.sub(r"\[\w+\]", "", roh)
    chunks = list(V.synthesize(text, syn_config=CFG, include_alignments=True))
    audio = np.concatenate([c.audio_int16_array for c in chunks])
    starts, total = wortstarts(chunks)
    assert total == len(audio), (total, len(audio))
    wlist = text.split()
    for m in re.finditer(r"\[(\w+)\]", roh):
        name = m.group(1)
        assert name not in cues, f"Marke doppelt: {name}"
        prefix = re.sub(r"\[\w+\]", "", roh[:m.start()]).strip()
        k = woerter(V.phonemize(prefix)) if prefix else 0
        folgewort = re.sub(r"\[\w+\]", "", roh[m.end():]).split()[0]
        cues[name] = dict(t=round(t + max(0, starts[k] - int(0.04 * SR)) / SR, 3), seg=i, wort=folgewort, index=k)
    d = len(audio) / SR
    segs.append(dict(i=i, start=round(t, 3), ende=round(t + d, 3), text=text))
    parts += [audio, np.zeros(int(pause * SR), np.int16)]
    t += d + pause
pcm = np.concatenate(parts)
with wave.open("../stimme.wav", "wb") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
json.dump(dict(dauer=round(len(pcm) / SR, 3), sr=SR, cues=cues, segmente=segs), open("../cues.json", "w"), ensure_ascii=False, indent=1)
print(f"Dauer {len(pcm)/SR:.2f}s, {sum(len(s['text'].split()) for s in segs)} Wörter, {len(cues)} Marken, "
      f"sha256 {hashlib.sha256(pcm.tobytes()).hexdigest()[:16]}")
