"""Lippen-Kontaktbilder aus dem finalen Hauptfilm-MP4 (Folge 051): je Sprechfenster Einzelbilder in 0,1-s-Schritten,
Ausschnitt um die Köpfe (sprechende Figur und ggf. Gegenüber). Ausgabe ../out/lip_<name>.png."""
import os, subprocess, sys
import imageio_ffmpeg
from PIL import Image, ImageDraw
FF = imageio_ffmpeg.get_ffmpeg_exe()
MP4 = "../out/051-Diebstahl-Schema-Hauptfilm.mp4"
# name: (start, ende, (x0, y0, x1, y1))
F = {
    "matthias_m1": (25.8, 28.0, (1420, 320, 1640, 480)),        # Matthias redet (Fall, Nachbartisch)
    "antje_a1": (37.4, 39.6, (420, 320, 640, 480)),              # Antje redet (Fall)
    "matthias_m2": (239.4, 241.7, (1630, 480, 1850, 620)),       # Matthias redet (Variante 2)
    "antje_bei_m2": (239.4, 241.7, (1310, 480, 1530, 620)),      # Antje hört zu: Mund zu
    "lexi_tipp": (337.8, 341.5, (1450, 420, 1680, 580)),
    "lexi_merke": (396.4, 400.1, (1560, 280, 1800, 450)),
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
