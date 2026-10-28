"""Lippen-Kontaktbilder aus dem finalen Hauptfilm-MP4 (Folge 042): je Sprechfenster Einzelbilder in 0,1-s-Schritten,
Ausschnitt um den Kopf der sprechenden Figur und ihres Gegenübers (Gegenprobe: Mund zu). Die Kopfausschnitte werden aus
denselben Positionen wie im Folienskript berechnet. Ausgabe ../out/lip_<name>.png."""
import json, os, subprocess, sys
import numpy as np
import imageio_ffmpeg
from PIL import Image, ImageDraw
sys.path.insert(0, "../../etb2/src")
import bausteine
bausteine.FIGORDNER = "op_042/"
FF = imageio_ffmpeg.get_ffmpeg_exe()
MP4 = "../out/042-Gefaehrliche-Koerperverletzung-Hauptfilm.mp4"
cj = json.load(open("../cues.json"))
seg = {s["i"]: (s["start"], s["ende"]) for s in cj["segmente"]}


def kopf(name, cx, unten, hoehe):
    e = bausteine.peep_voll(name, cx, unten, hoehe, "_")
    a = np.asarray(e.sprite)[:, :, 3] > 20
    ys, xs = np.nonzero(a); top = ys.min()
    band = a[top:top + int(hoehe * 0.2)]
    yy, xx = np.nonzero(band)
    x0, x1 = e.x + xx.min() - 10, e.x + xx.max() + 10
    return (int(x0), int(e.y + top - 10), int(x1), int(e.y + top + hoehe * 0.2 + 10))


SH, FR = 560, 440
TOS_H = int(SH * 0.68)
F = {   # name: (Segment-Nr., Kopf-Box)
    "reinhard_r1": (1, kopf("RE_redet", 1640, 900, SH)),
    "tobias_bei_reinhard": (1, kopf("TO_froh_r", 840, 900, SH)),
    "tobias_t1": (3, kopf("TOS_redet_r", 720, 900, TOS_H)),
    "reinhard_bei_tobias": (3, kopf("RE_veraechtlich", 990, 900, SH)),
    "reinhard_r2": (12, kopf("RE_laechelt_r", 1430, 930, FR)),
    "tobias_bei_r2": (12, kopf("TO_froh", 1760, 930, FR)),
    "anja_a1": (15, kopf("AN_redet", 1810, 930, FR)),
    "tobias_bei_anja": (15, kopf("TO_skeptisch", 1600, 930, FR)),
    "lexi_tipp": (21, kopf("LX_warnt", 1560, 930, FR + 60)),
    "lexi_merke": (23, kopf("LX_erklaert", 1680, 990, 700)),
}
os.makedirs("../out/lip", exist_ok=True)
for name, (si, box) in F.items():
    a, b = seg[si]
    a, b = a - 0.2, min(b + 0.3, a + 4.6)
    n = int(round((b - a) * 10))
    subprocess.run([FF, "-v", "error", "-y", "-ss", f"{a:.2f}", "-i", MP4, "-frames:v", str(n), "-vf",
                    f"fps=10,crop={box[2]-box[0]}:{box[3]-box[1]}:{box[0]}:{box[1]}", f"../out/lip/{name}_%03d.png"], check=True)
    bilder = [Image.open(f"../out/lip/{name}_{i:03d}.png") for i in range(1, n + 1) if os.path.exists(f"../out/lip/{name}_{i:03d}.png")]
    w, h = bilder[0].size; sc = min(1.0, 200 / w); w2, h2 = int(w * sc), int(h * sc); cols = 12
    s = Image.new("RGB", (cols * w2, ((len(bilder) + cols - 1) // cols) * (h2 + 18)), "white"); d = ImageDraw.Draw(s)
    for i, im in enumerate(bilder):
        x, y = (i % cols) * w2, (i // cols) * (h2 + 18)
        s.paste(im.resize((w2, h2)), (x, y)); d.text((x + 3, y + h2 + 2), f"{a + i * 0.1:.1f}s", fill=(0, 0, 0))
    s.save(f"../out/lip_{name}.png"); print(name, len(bilder), box)
