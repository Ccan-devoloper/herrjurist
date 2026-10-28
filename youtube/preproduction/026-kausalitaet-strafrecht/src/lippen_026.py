"""Lippen-Kontaktbilder aus dem finalen Hauptfilm-MP4 (Folge 026): je Sprechfenster Einzelbilder in 0,1-s-Schritten,
Ausschnitt um die Köpfe (sprechende Figur und ggf. Gegenüber). Ausgabe ../out/lip_<name>.png."""
import os, subprocess, sys
import imageio_ffmpeg
from PIL import Image, ImageDraw
FF = imageio_ffmpeg.get_ffmpeg_exe()
MP4 = "../out/026-Kausalitaet-Strafrecht-Hauptfilm.mp4"
# name: (start, ende, (x0, y0, x1, y1))
F = {
    "bodo_egon_kiosk": (7.9, 11.6, (480, 430, 1400, 640)),       # Bodo redet, dann Egon; der jeweils andere hat den Mund zu
    "maren": (23.9, 25.9, (1420, 420, 1700, 600)),
    "bodo_einwand": (116.2, 119.5, (1440, 420, 1680, 600)),
    "lexi_tipp": (295.3, 299.0, (1440, 300, 1700, 520)),
    "lexi_merke": (346.0, 349.6, (1560, 250, 1820, 470)),
}
os.makedirs("../out/lip", exist_ok=True)
for name, (a, b, box) in F.items():
    n = int(round((b - a) * 10))
    subprocess.run([FF, "-v", "error", "-y", "-ss", f"{a:.2f}", "-i", MP4, "-frames:v", str(n), "-vf",
                    f"fps=10,crop={box[2]-box[0]}:{box[3]-box[1]}:{box[0]}:{box[1]}", f"../out/lip/{name}_%03d.png"], check=True)
    bilder = [Image.open(f"../out/lip/{name}_{i:03d}.png") for i in range(1, n + 1) if os.path.exists(f"../out/lip/{name}_{i:03d}.png")]
    w, h = bilder[0].size; sc = min(1.0, 360 / w); w2, h2 = int(w * sc), int(h * sc); cols = 6
    s = Image.new("RGB", (cols * w2, ((len(bilder) + cols - 1) // cols) * (h2 + 18)), "white"); d = ImageDraw.Draw(s)
    for i, im in enumerate(bilder):
        x, y = (i % cols) * w2, (i // cols) * (h2 + 18)
        s.paste(im.resize((w2, h2)), (x, y)); d.text((x + 3, y + h2 + 2), f"{a + i * 0.1:.1f}s", fill=(0, 0, 0))
    s.save(f"../out/lip_{name}.png"); print(name, len(bilder))
