"""Lippen-Kontaktbilder aus dem finalen Hauptfilm-MP4 (Folge 038): je Sprechfenster Einzelbilder in 0,1-s-Schritten,
Ausschnitt um die Köpfe (sprechende Figur und ggf. Gegenüber). Ausgabe ../out/lip_<name>.png."""
import os, subprocess, sys
import imageio_ffmpeg
from PIL import Image, ImageDraw
FF = imageio_ffmpeg.get_ffmpeg_exe()
MP4 = "../out/038-Koerperverletzung-Hauptfilm.mp4"
# name: (start, ende, (x0, y0, x1, y1))
F = {
    "katrin_k1": (18.9, 22.4, (570, 440, 750, 560)),            # Katrin redet (Sofa)
    "sigrid_bei_katrin": (18.9, 22.4, (1030, 335, 1190, 445)),  # Sigrid hört zu: Mund zu
    "sigrid_s1": (22.6, 25.1, (1030, 335, 1190, 445)),          # Sigrid redet
    "katrin_bei_sigrid": (22.6, 25.1, (570, 440, 750, 560)),    # Katrin hört zu: Mund zu
    "lindner_l1": (218.9, 221.9, (1680, 485, 1810, 575)),       # Doktor Lindner redet
    "katrin_bei_lindner": (218.9, 221.9, (1375, 550, 1515, 640)),
    "katrin_k2": (222.0, 224.5, (1375, 550, 1515, 640)),        # Katrin redet (Liege)
    "lindner_bei_katrin": (222.0, 224.5, (1680, 485, 1810, 575)),
    "lexi_tipp": (301.2, 305.0, (1480, 420, 1660, 545)),
    "lexi_merke": (349.8, 353.6, (1580, 280, 1800, 440)),
}
os.makedirs("../out/lip", exist_ok=True)
for name, (a, b, box) in F.items():
    n = int(round((b - a) * 10))
    subprocess.run([FF, "-v", "error", "-y", "-ss", f"{a:.2f}", "-i", MP4, "-frames:v", str(n), "-vf",
                    f"fps=10,crop={box[2]-box[0]}:{box[3]-box[1]}:{box[0]}:{box[1]}", f"../out/lip/{name}_%03d.png"], check=True)
    bilder = [Image.open(f"../out/lip/{name}_{i:03d}.png") for i in range(1, n + 1) if os.path.exists(f"../out/lip/{name}_{i:03d}.png")]
    w, h = bilder[0].size; sc = min(1.0, 360 / w); w2, h2 = int(w * sc), int(h * sc); cols = 9
    s = Image.new("RGB", (cols * w2, ((len(bilder) + cols - 1) // cols) * (h2 + 18)), "white"); d = ImageDraw.Draw(s)
    for i, im in enumerate(bilder):
        x, y = (i % cols) * w2, (i // cols) * (h2 + 18)
        s.paste(im.resize((w2, h2)), (x, y)); d.text((x + 3, y + h2 + 2), f"{a + i * 0.1:.1f}s", fill=(0, 0, 0))
    s.save(f"../out/lip_{name}.png"); print(name, len(bilder))
