"""Rendert die Testfolge 081 ohne Illustrationen: blaue Bühne, Prüfpfad und Rechtskarte nach Master 09.

Layoutwerte aus youtube/MASTERSTANDARD-09.md, Abschnitt 3 (1920x1080). Rechts steht statt der
Fallillustration ein ruhiges Stichwort. Jede Textzeile wird gegen ihre Box geprüft (Abbruch bei Überlauf).
"""
import json, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import imageio_ffmpeg
sys.path.insert(0, ".")
from skript import S

W, H, FPS = 1920, 1080, 30
FONTS = "/home/user/herrjurist/fonts/"
NAVY = (5, 20, 56, 242)
ORANGE = (0xFF, 0x84, 0x47, 255)
WEISS = (0xFC, 0xFD, 0xFF, 255)
BLAUWEISS = (0xC9, 0xD8, 0xFF, 255)
FADE = 6  # Frames Einblendung neuer Kartenteile

def font(name, size, weight):
    f = ImageFont.truetype(FONTS + name, size)
    axes = f.get_variation_axes()
    f.set_variation_by_axes([min(max(size, 14), 32) if a["name"] == b"Optical size" else weight for a in axes])
    return f

F_PFAD = font("SpaceGrotesk.ttf", 28, 700)
F_TITEL = font("Inter.ttf", 44, 700)
F_ZEILE = font("Inter.ttf", 34, 500)
F_UNTER = font("Inter.ttf", 31, 450)
F_KICKER = font("SpaceGrotesk.ttf", 34, 500)
F_WORT = font("SpaceGrotesk.ttf", 84, 700)

bounds_log = []

def check(draw, text, f, x, maxright, what):
    b = draw.textbbox((x, 0), text, font=f)
    ok = b[2] <= maxright
    bounds_log.append(dict(was=what, text=text, rechts=b[2], grenze=maxright, ok=ok))
    if not ok:
        raise SystemExit(f"Textüberlauf: {what} '{text}' rechts={b[2]} > {maxright}")

def buehne():
    y = np.linspace(0, 1, H)[:, None]
    x = np.linspace(0, 1, W)[None, :]
    top, bot = np.array([34, 86, 214]), np.array([18, 58, 170])
    img = top * (1 - y[..., None]) + bot * y[..., None]
    img = np.broadcast_to(img, (H, W, 3)).copy()
    # ruhiger heller Lichtfleck rechts, Kartenraum links bleibt gleichmäßig
    d = np.sqrt(((x - 0.74) * 1.6) ** 2 + (y - 0.52) ** 2)
    img += (np.clip(1 - d / 0.55, 0, 1) ** 2 * 26)[..., None]
    base = Image.fromarray(np.clip(img, 0, 255).astype(np.uint8)).convert("RGBA")
    # dezente Bodenlinie als Bühnenkante rechts
    ov = Image.new("RGBA", (W, H))
    dr = ImageDraw.Draw(ov)
    dr.rounded_rectangle((900, 840, 1840, 846), 3, fill=(255, 255, 255, 38))
    return Image.alpha_composite(base, ov)

BG = buehne()

def box(dr, xy, rad, border):
    dr.rounded_rectangle(xy, rad, fill=NAVY, outline=ORANGE, width=border)

def pfad_layer(text):
    ov = Image.new("RGBA", (W, H)); dr = ImageDraw.Draw(ov)
    x, y, w, h = 58, 32, 740, 67
    box(dr, (x, y, x + w, y + h), 16, 2)
    dr.rectangle((x + 16, y + 14, x + 16 + 6, y + h - 14), fill=ORANGE)
    check(dr, text, F_PFAD, x + 40, x + w - 20, "Prüfpfad")
    tb = dr.textbbox((0, 0), text, font=F_PFAD)
    dr.text((x + 40, y + (h - (tb[3] - tb[1])) / 2 - tb[1]), text, font=F_PFAD, fill=WEISS)
    return ov

def karte_layer(titel, zeilen, sichtbar=None):
    ov = Image.new("RGBA", (W, H)); dr = ImageDraw.Draw(ov)
    x, y, w = 58, 124, 740
    tx, right = 111, x + w - 24
    lh, lh_u, gap_t = 50, 46, 22
    hoehe = 34 + 56 + gap_t + sum(lh_u if z.startswith("  ") else lh for z in zeilen) + 26
    assert hoehe <= 720, hoehe
    box(dr, (x, y, x + w, y + hoehe), 22, 3)
    dr.rectangle((x + 24, y + 30, x + 30, y + hoehe - 30), fill=ORANGE)
    check(dr, titel, F_TITEL, tx, right, "Kartentitel")
    dr.text((tx, y + 30), titel, font=F_TITEL, fill=WEISS)
    cy = y + 34 + 56 + gap_t
    for i, z in enumerate(zeilen):
        if sichtbar is not None and i >= sichtbar:
            continue
        if z.startswith("  "):
            t = z.strip(); check(dr, t, F_UNTER, tx + 34, right, "Unterpunkt")
            dr.text((tx + 34, cy), t, font=F_UNTER, fill=BLAUWEISS); cy += lh_u
        else:
            check(dr, z, F_ZEILE, tx, right, "Zeile")
            dr.text((tx, cy), z, font=F_ZEILE, fill=WEISS); cy += lh
    assert cy + 10 <= y + hoehe
    return ov

def rechts_layer(kicker, wort):
    ov = Image.new("RGBA", (W, H)); dr = ImageDraw.Draw(ov)
    cx, left, right = 1370, 880, 1860
    for t, f in ((kicker, F_KICKER), (wort, F_WORT)):
        b = dr.textbbox((0, 0), t, font=f)
        check(dr, t, f, cx - (b[2] - b[0]) / 2, right, "Stichwort")
        assert cx - (b[2] - b[0]) / 2 >= left, t
    kb = dr.textbbox((0, 0), kicker.upper(), font=F_KICKER)
    dr.text((cx - (kb[2] - kb[0]) / 2, 440), kicker.upper(), font=F_KICKER, fill=ORANGE)
    wb = dr.textbbox((0, 0), wort, font=F_WORT)
    dr.text((cx - (wb[2] - wb[0]) / 2, 500), wort, font=F_WORT, fill=WEISS)
    # weicher Schatten für Lesbarkeit
    sh = ov.split()[3].filter(ImageFilter.GaussianBlur(10)).point(lambda a: a * 0.35)
    shadow = Image.new("RGBA", (W, H), (5, 20, 56, 0)); shadow.putalpha(sh)
    return Image.alpha_composite(shadow, ov)

# --- Zustände aus Skript ableiten --------------------------------------------------------
cues = json.load(open("../cues.json"))
dauer = cues["dauer"]
states, pfad, titel, zeilen, rechts = [], None, None, [], None
for s, c in zip(S, cues["cues"]):
    neu = s["neu"]
    if s["pfad"]: pfad = s["pfad"]
    if neu: titel, zeilen, rechts = s["titel"], list(s["zeilen"]), s["rechts"]
    else: zeilen = zeilen + list(s["zeilen"])
    states.append(dict(t=c["start"], pfad=pfad, titel=titel, zeilen=zeilen, rechts=rechts, neu=neu,
                       alt=len(zeilen) - (0 if neu else len(s["zeilen"]))))
states[0]["t"] = 0.0  # Prüfpfad und erste Karte ab dem ersten Hauptfilmbild

frames = []
for st in states:
    grund = Image.alpha_composite(BG, pfad_layer(st["pfad"]))
    voll = Image.alpha_composite(Image.alpha_composite(grund, rechts_layer(*st["rechts"])), karte_layer(st["titel"], st["zeilen"]))
    st["grund"] = np.asarray(grund.convert("RGB"), np.float32)
    if not st["neu"]:
        # Karte sofort in neuer Größe mit den bisherigen Zeilen; nur die neuen Zeilen blenden ein
        vor = Image.alpha_composite(Image.alpha_composite(grund, rechts_layer(*st["rechts"])), karte_layer(st["titel"], st["zeilen"], st["alt"]))
        st["grund"] = np.asarray(vor.convert("RGB"), np.float32)
    st["voll"] = np.asarray(voll.convert("RGB"), np.uint8)

n = int(round(dauer * FPS))
ff = imageio_ffmpeg.get_ffmpeg_exe()
cmd = [ff, "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
       "-i", "../stimme_48k.wav", "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-preset", "medium", "-crf", "17",
       "-pix_fmt", "yuv420p", "-profile:v", "high", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
       "-movflags", "+faststart", "-shortest", "../ETBI-Test-081.mp4"]
p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
si = 0
for f in range(n):
    t = f / FPS
    while si + 1 < len(states) and t >= states[si + 1]["t"]:
        si += 1
    st = states[si]
    k = int((t - st["t"]) * FPS)
    if si > 0 and k < FADE:
        # neue Karte: nur Hintergrund+Pfad -> neue Karte (keine Geisterschrift der alten);
        # angehängte Zeile: vergrößerte Karte mit alten Zeilen -> neue Zeilen blenden ein
        a = (k + 1) / (FADE + 1)
        src = st["grund"]
        img = (src * (1 - a) + st["voll"] * a).astype(np.uint8)
    else:
        img = st["voll"]
    p.stdin.write(img.tobytes())
p.stdin.close(); p.wait()
json.dump(dict(bounds=bounds_log, zustaende=[dict(t=s["t"], pfad=s["pfad"], titel=s["titel"], zeilen=s["zeilen"], rechts=s["rechts"]) for s in states]),
          open("../render-protokoll.json", "w"), ensure_ascii=False, indent=1)
for i, st in enumerate(states):
    Image.fromarray(st["voll"]).save(f"../frames/zustand_{i:02d}.png")
print("fertig", n, "Frames", len(states), "Zustände", sum(not b["ok"] for b in bounds_log), "Überläufe")
