"""Prüfbilder Folge 082 aus dem finalen Hauptfilm-MP4 (Sichtprüfung, nicht aus dem Renderer):
- bildhalte_mp4_N.png: Keyframe jedes Bildhalts (Zeit aus ../bildhalt_manifest.json, 0,04 s vor Ende bzw. vor der Blende),
  je Bogen 30 Bilder mit Nummer, Zeit und Prüfpfad
- lip_<name>.png: Sprechfenster in 0,1-s-Schritten, Ausschnitt um den Kopf der Figur
- schnittstellen.png: Einzelbilder an den Übergängen Intro/Hauptfilm/Outro (aus dem Endschnitt)
Aufruf: python3 pruefbilder_082.py ../out/082-Anfechtungsklage-Schema-Hauptfilm.mp4 [../out/082-Anfechtungsklage-Schema.mp4]"""
import json, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import imageio_ffmpeg

FF = imageio_ffmpeg.get_ffmpeg_exe()
MP4 = sys.argv[1]
FONT = ImageFont.truetype("../../humaaans/fonts/Nunito[wght].ttf", 18)


def bild(t, quelle=MP4):
    raw = subprocess.run([FF, "-v", "error", "-ss", f"{t:.3f}", "-i", quelle, "-frames:v", "1", "-f", "rawvideo",
                          "-pix_fmt", "rgb24", "-"], capture_output=True).stdout
    return Image.frombytes("RGB", (1920, 1080), raw)


def bogen(bilder, cols, tw, th, name):
    rows = (len(bilder) + cols - 1) // cols
    s = Image.new("RGB", (cols * tw, rows * (th + 26)), "white"); d = ImageDraw.Draw(s)
    for i, (im, txt) in enumerate(bilder):
        x, y = (i % cols) * tw, (i // cols) * (th + 26)
        s.paste(im.resize((tw, th)), (x, y)); d.text((x + 4, y + th + 2), txt[:70], fill=(0, 0, 0), font=FONT)
    s.save(name)


NUR_LIPPEN = "--nur-lippen" in sys.argv
if NUR_LIPPEN:
    sys.argv.remove("--nur-lippen")
man = json.load(open("../bildhalt_manifest.json"))
WISCH = 14 / 30
starts = sorted({h["start"] for h in man["halte"]})
bilder = []
HL = man["halte"]
for i, h in enumerate([] if NUR_LIPPEN else HL):
    tk = h["ende"] - 0.04
    if i + 1 < len(HL) and HL[i + 1]["folie"] != h["folie"]:   # Halt endet an einer Schiebeblende: Keyframe vor dem Wisch
        tk = h["ende"] - 16 / 30
    im = bild(tk)
    bilder.append((im, f"{h['nr']} {tk:.1f}s {h['pruefpfad'][-48:]}"))
for k in range(0, len(bilder), 30):  # noqa
    bogen(bilder[k:k + 30], 5, 384, 216, f"../out/bildhalte_mp4_{k // 30 + 1}.png")
print(len(bilder), "Bildhalte aus dem MP4")

cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"]
# (Name, von, bis, Kopfausschnitt x0, y0, x1, y1)
LIPPEN = [("steinke_st1", T("st1"), T("bescheid"), 1440, 380, 1680, 580),
          ("hinrichs_waehrend_steinke", T("st1"), T("bescheid"), 820, 380, 1060, 580),
          ("hinrichs_hi1", T("hi1"), T("klage"), 820, 380, 1060, 580),
          ("steinke_waehrend_hinrichs", T("hi1"), T("klage"), 1440, 380, 1680, 580),
          ("richterin_vor_ri1", T("urteil"), T("ri1"), 1200, 380, 1440, 580),
          ("richterin_ri1", T("ri1"), T("ende"), 1200, 380, 1440, 580),
          ("hinrichs_waehrend_richterin", T("ri1"), T("ende"), 500, 380, 740, 580),
          ("lexi_tipp", T("tipp"), T("tipp") + 6.0, 1440, 400, 1720, 640),
          ("lexi_merke", T("merke"), T("merke") + 6.0, 1500, 230, 1860, 530)]
for name, a, b, x0, y0, x1, y1 in LIPPEN:
    ts = np.arange(a, b, 0.1)
    bs = [(bild(t).crop((x0, y0, x1, y1)), f"{t + 8:.1f}") for t in ts]
    bogen(bs, 10, (x1 - x0) // 2, (y1 - y0) // 2, f"../out/lip_{name}.png")
print("Lippenbilder:", [l[0] for l in LIPPEN])

if len(sys.argv) > 2:
    END = sys.argv[2]
    haupt_ende = 8.0 + cj["dauer"]
    ts = [7.9, 8.05, 8.5, haupt_ende - 1.6, haupt_ende - 0.1, haupt_ende + 0.2]
    bogen([(bild(t, END), f"{t:.2f}s") for t in ts], 3, 640, 360, "../out/schnittstellen.png")
    print("Schnittstellen", ts)
