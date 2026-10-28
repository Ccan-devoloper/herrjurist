"""Rendert Folge 081 v2: Folien aus folien.py, Zeiten aus cues.json, Ton aus stimme_48k.wav."""
import json, subprocess, sys
import numpy as np
from PIL import Image
import imageio_ffmpeg
sys.path.insert(0, ".")
from folien_h import FOLIEN
from engine import W, H, T, papier, PFADGRAU
from PIL import Image as _I

FPS = 30
DUR = {"rise": 10, "pop": 12, "fade": 10, "cut": 1}
OUT = 8  # Frames Ausblenden vor Folienwechsel
nur_vorschau = "--vorschau" in sys.argv

cj = json.load(open("../cues.json"))
cues, dauer = cj["cues"], cj["dauer"]
BG = {"cyan": _I.new("RGBA", (W, H), (213, 241, 244, 255)), "blau": _I.new("RGBA", (W, H), (35, 39, 168, 255))}

def zeit(c):
    if isinstance(c, tuple):
        return cues[c[0]]["t"] + c[1]
    return cues[c]["t"]

# Pfad-Elemente ergänzen, Zeiten auflösen
genutzt = set()
for f in FOLIEN:
    pf = []
    for k, (cue, text) in enumerate(f["pfade"]):
        nxt = f["pfade"][k + 1][0] if k + 1 < len(f["pfade"]) else None
        farbe = (31, 29, 91, 150) if f["bg"] == "cyan" else (200, 205, 255, 200)
        pf.append(T(text, 40, 1034, cue, "Medium", 30, farbe=farbe, anim="fade", bis=nxt))
    f["els"] = pf + f["els"]
    for e in f["els"]:
        e.t0 = zeit(e.cue) + e.d
        e.t1 = zeit(e.bis) if e.bis is not None else None
        genutzt.add(e.cue if isinstance(e.cue, str) else e.cue[0])
    f["start"] = min(e.t0 for e in f["els"])
fehl = set(cues) - genutzt
assert not fehl, f"Marken ohne Bildelement: {fehl}"
for a, b in zip(FOLIEN, FOLIEN[1:]):
    assert b["start"] > a["start"]
    for e in a["els"]:
        assert e.t0 < b["start"] - OUT / FPS, f"Element erscheint erst nach Folienende: {e.name}"

def ease(x):
    return 1 - (1 - x) ** 3

def back(x):
    c = 1.7
    return 1 + (c + 1) * (x - 1) ** 3 + c * (x - 1) ** 2

def mit_alpha(im, a):
    if a >= 0.999:
        return im
    im = im.copy()
    im.putalpha(im.getchannel("A").point(lambda v: int(v * a)))
    return im

def setze(base, sp, x, y):
    """alpha_composite, das auch links/oben über den Bildrand ragende Sprites korrekt beschneidet."""
    x, y = int(x), int(y)
    if x < 0 or y < 0:
        sp = sp.crop((max(0, -x), max(0, -y), sp.width, sp.height)); x, y = max(0, x), max(0, y)
    base.alpha_composite(sp, (x, y))

def zeichne(base, e, t):
    k = (t - e.t0) * FPS
    n = DUR[e.anim]
    if k >= n:
        setze(base, e.sprite, e.x, e.y)
        return
    x = k / n
    if e.anim == "rise":
        dy = int((1 - ease(x)) * 26)
        setze(base, mit_alpha(e.sprite, ease(x)), e.x, e.y + dy)
    elif e.anim in ("fade", "cut"):
        setze(base, mit_alpha(e.sprite, ease(x)), e.x, e.y)
    else:  # pop
        s = max(0.05, 0.55 + 0.45 * back(x))
        w, h = max(1, int(e.sprite.width * s)), max(1, int(e.sprite.height * s))
        sp = mit_alpha(e.sprite.resize((w, h), Image.BILINEAR), min(1, x * 2.2))
        cx, cy = e.x + e.sprite.width / 2, e.y + e.sprite.height / 2
        px, py = int(cx - w / 2), int(cy - h / 2)
        setze(base, sp, px, py)

cache = {}
def folienbild(fi, t):
    f = FOLIEN[fi]
    sichtbar = [e for e in f["els"] if e.t0 <= t and (e.t1 is None or t < e.t1)]
    statisch = tuple(id(e) for e in sichtbar if (t - e.t0) * FPS >= DUR[e.anim])
    key = (fi, statisch)
    if key not in cache:
        cache.clear()
        b = BG[f["bg"]].copy()
        for e in sichtbar:
            if id(e) in statisch:
                zeichne(b, e, t)
        cache[key] = b
    anim = [e for e in sichtbar if id(e) not in statisch]
    if not anim:
        return cache[key], True
    b = cache[key].copy()
    for e in anim:
        zeichne(b, e, t)
    return b, False

def frame(t):
    fi = 0
    while fi + 1 < len(FOLIEN) and t >= FOLIEN[fi + 1]["start"]:
        fi += 1
    img, stat = folienbild(fi, t)
    if fi + 1 < len(FOLIEN):
        rest = (FOLIEN[fi + 1]["start"] - t) * FPS
        if rest < OUT:
            a = 1 - rest / OUT
            nb = np.asarray(BG[FOLIEN[fi + 1]["bg"]].convert("RGB"), np.float32)
            cur = np.asarray(img.convert("RGB"), np.float32)
            return Image.fromarray((cur * (1 - a) + nb * a).astype(np.uint8)), False
    return img, stat

if nur_vorschau:
    # Endzustand jeder Folie (kurz vor dem Wechsel) als PNG + Kontaktbogen
    bilder = []
    for fi, f in enumerate(FOLIEN):
        tend = (FOLIEN[fi + 1]["start"] - (OUT + 2) / FPS) if fi + 1 < len(FOLIEN) else dauer - 0.1
        im, _ = frame(tend)
        im.convert("RGB").save(f"../h/frames/folie_{fi+1:02d}.png"); bilder.append(im.convert("RGB"))
    tw, th, cols = 640, 360, 3
    rows = (len(bilder) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * tw, rows * th), (255, 255, 255))
    for i, b in enumerate(bilder):
        sheet.paste(b.resize((tw, th)), ((i % cols) * tw, (i // cols) * th))
    sheet.save("../h/kontaktbogen.png")
    print("Vorschau:", len(bilder), "Folien", [round(f["start"], 2) for f in FOLIEN])
    sys.exit()

ff = imageio_ffmpeg.get_ffmpeg_exe()
cmd = [ff, "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
       "-i", "../stimme_48k.wav", "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-preset", "medium", "-crf", "18",
       "-pix_fmt", "yuv420p", "-profile:v", "high", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
       "-movflags", "+faststart", "-shortest", "../h/ETBI-Humaaans.mp4"]
p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
n = int(round(dauer * FPS))
letzt = None
for fr in range(n):
    im, stat = frame(fr / FPS)
    if stat and letzt is not None and letzt[0] is im:
        p.stdin.write(letzt[1]); continue
    by = im.convert("RGB").tobytes()
    letzt = (im, by) if stat else None
    p.stdin.write(by)
p.stdin.close(); p.wait()
print("fertig", n, "Frames,", len(FOLIEN), "Folien")
