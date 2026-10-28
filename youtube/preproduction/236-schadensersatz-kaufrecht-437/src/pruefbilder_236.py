"""Prüfbilder aus dem finalen MP4 (Folge 236): Bildhalt-Kontaktbögen, Lippenstreifen und Schnittstellen.
    python3 pruefbilder_236.py halte  ../out/236-Schadensersatz-Kaufrecht-437-Hauptfilm.mp4      → ../out/bildhalte_mp4_N.png
    python3 pruefbilder_236.py lippen ../out/236-Schadensersatz-Kaufrecht-437-Hauptfilm.mp4      → ../out/lip_*.png (0,1-s-Schritte)
    python3 pruefbilder_236.py schnitt ../out/236-Schadensersatz-Kaufrecht-437.mp4               → ../out/schnittstellen.png
Keyframe-Zeiten aus ../bildhalt_manifest.json (Ende − 0,04 s bzw. vor der Schiebeblende wie im Renderer)."""
import os
OUT = os.environ.get("OUT", "../out")   # Ausgabeordner (Prüfbilder nicht im Repository)
import json, subprocess, sys, io
from PIL import Image, ImageDraw
import imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe()


def bild(mp4, t, w=480, h=270):
    r = subprocess.run([FF, "-v", "error", "-ss", f"{t:.3f}", "-i", mp4, "-frames:v", "1", "-f", "image2pipe", "-vcodec",
                        "png", "-"], capture_output=True)
    return Image.open(io.BytesIO(r.stdout)).convert("RGB").resize((w, h))


def bogen(bilder, cols, w, h, name):
    rows = (len(bilder) + cols - 1) // cols
    sh = Image.new("RGB", (cols * w, rows * (h + 22)), (255, 255, 255)); d = ImageDraw.Draw(sh)
    for i, (txt, im) in enumerate(bilder):
        x, y = (i % cols) * w, (i // cols) * (h + 22)
        sh.paste(im, (x, y + 22)); d.text((x + 4, y + 4), txt, fill=(200, 0, 0))
    sh.save(name)


art, mp4 = sys.argv[1], sys.argv[2]
if art == "halte":
    man = json.load(open("../bildhalt_manifest.json")); H = man["halte"]
    bilder = []
    for i, h in enumerate(H):
        t = h["ende"] - 0.04
        if i + 1 < len(H) and H[i + 1]["folie"] != h["folie"]:
            t = h["ende"] - 16 / 30                 # vor der Schiebeblende, wie im Renderer
        bilder.append((f'{h["nr"]:03d}  {h["start"]:.1f}s', bild(mp4, min(man["dauer"] - 0.1, max(h["start"] + 0.02, t)))))
    for k in range(0, len(bilder), 30):
        bogen(bilder[k:k + 30], 5, 480, 270, f"{OUT}/bildhalte_mp4_{k // 30 + 1}.png")
    print(len(bilder), "Bildhalte aus dem MP4")
elif art == "lippen":
    cj = json.load(open("../cues.json"))
    fenster = json.loads(sys.argv[3])          # [[name, start, ende, x, y, w, h], ...] Ausschnitt um den Kopf
    for name, a, b, x, y, w, h in fenster:
        bilder = []
        t = a
        while t <= b:
            r = subprocess.run([FF, "-v", "error", "-ss", f"{t:.3f}", "-i", mp4, "-frames:v", "1", "-f", "image2pipe",
                                "-vcodec", "png", "-"], capture_output=True)
            im = Image.open(io.BytesIO(r.stdout)).convert("RGB").crop((x, y, x + w, y + h)).resize((160, 160))
            bilder.append((f"{t:.1f}", im)); t = round(t + 0.1, 3)
        bogen(bilder, 15, 160, 160, f"{OUT}/lip_{name}.png")
        print(name, len(bilder))
elif art == "schnitt":
    ts = [float(v) for v in sys.argv[3].split(",")]
    bogen([(f"{t:.2f}s", bild(mp4, t)) for t in ts], 3, 640, 360, f"{OUT}/schnittstellen.png")
