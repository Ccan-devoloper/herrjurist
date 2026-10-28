"""Folge 002 · Pegelnachführung für Figurensegmente, die angleichen() (synth_el.py) wegen der Spitzenbegrenzung nicht auf
−19 LUFS bringen kann (Emma, „Abgemacht! …“: Rohaufnahme −21,1 LUFS bei −1,3 dBFS Spitze, Verstärkung nur +0,3 dB).
Läuft nach synth_el.py und vor der 48-kHz-Wandlung; ändert keine Länge und keine Zeiten (Cues bleiben gültig), ist idempotent.
Verfahren: Verstärkung bis −19,0 LUFS, Spitzen über −1 dBFS mit Vorschau-Limiter (Hüllkurve: Minimum über ±3 ms, Glättung 6 ms).

    python3 pegel_002.py        (im src-Ordner; danach ffmpeg -i ../stimme.wav -ac 2 -ar 48000 ../stimme_48k.wav)
"""
import json, wave
import numpy as np
import pyloudnorm as pyln
from scipy.ndimage import minimum_filter1d, uniform_filter1d

SR, ZIEL, SPITZE, TOL = 48000, -19.0, 0.89, 0.3
cj = json.load(open("../cues.json"))
w = wave.open("../stimme.wav"); x = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float64) / 32768; w.close()
m = pyln.Meter(SR)


def begrenzt(seg, g):
    y = seg * 10 ** (g / 20)
    r = np.minimum(1.0, SPITZE / np.maximum(np.abs(y), 1e-9))
    r = minimum_filter1d(r, int(0.006 * SR))
    r = uniform_filter1d(r, int(0.006 * SR))
    r = minimum_filter1d(r, int(0.002 * SR))
    return np.clip(y * r, -0.97, 0.97)


protokoll = []
for s in cj["segmente"]:
    a, b = int(round(s["start"] * SR)), int(round(s["ende"] * SR))
    seg = x[a:b]
    l = m.integrated_loudness(seg if len(seg) >= SR // 2 else np.tile(seg, 2))
    if l >= ZIEL - TOL:
        continue
    g = ZIEL - l
    for _ in range(8):                            # Verstärkung nachführen, bis die begrenzte Fassung −19 LUFS erreicht
        neu = begrenzt(seg, g)
        ln = m.integrated_loudness(neu)
        if abs(ln - ZIEL) < 0.05:
            break
        g += ZIEL - ln
    x[a:b] = neu
    protokoll.append(dict(segment=s["i"] + 1, rolle=s["rolle"] or "Erzählerin", vorher=round(l, 1), nachher=round(ln, 1),
                          verstaerkung_db=round(g, 1), spitze_dbfs=round(20 * np.log10(np.abs(neu).max()), 1)))
with wave.open("../stimme.wav", "wb") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((np.clip(x, -1, 1) * 32767).astype(np.int16).tobytes())
print(json.dumps(protokoll, ensure_ascii=False) if protokoll else "keine Segmente unter −19,3 LUFS – nichts geändert")
