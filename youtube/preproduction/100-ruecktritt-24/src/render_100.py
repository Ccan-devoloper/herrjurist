"""Rendert Folge 100 Rücktritt § 24 StGB (Open Peeps, Serienstandard Katzenkönig): Bewegung, stumme Schiebe-Übergänge,
Stimme + Handlungsgeräusche (Freesound CC0). Intro/Outro hängt tools/schnitt.py an. Kopie von render_raser.py (nur Import und Videoname)."""
import json, os, subprocess, sys, wave
import numpy as np
from PIL import Image
import imageio_ffmpeg
sys.path.insert(0, ".")
sys.path.insert(0, "../../etb2/src")
from folien_100 import FOLIEN, BG_FARBE, PFAD_FARBE
from engine import W, H, T
import ostil

FPS = 30
DUR = {"rise": 10, "pop": 12, "fade": 10, "cut": 0, "grow": 5}   # cut = harter Schnitt (kein halbtransparenter Mund-Frame)
WISCH = 14  # Frames der Schiebe-Blende zwischen Folien (endet genau am Folienstart)
nur_vorschau = "--vorschau" in sys.argv
OUT = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else "../out"

cj = json.load(open("../cues.json"))
cues, dauer = cj["cues"], cj["dauer"]


def hintergrund(art):
    if art == "nacht":
        y = np.linspace(0, 1, H)[:, None, None]
        oben, unten = np.array([44, 52, 98]), np.array([84, 98, 150])   # aufgehellt: Tuschekonturen bleiben lesbar
        img = np.broadcast_to(oben * (1 - y) + unten * y, (H, W, 3)).astype(np.uint8)
        return Image.fromarray(img).convert("RGBA")
    return Image.new("RGBA", (W, H), BG_FARBE[art])


BG = {k: hintergrund(k) for k in BG_FARBE}


def zeit(c):
    if isinstance(c, tuple):
        return cues[c[0]]["t"] + c[1]
    return cues[c]["t"]


genutzt = set()
sfx_liste = []
for f in FOLIEN:
    pf = []
    for k, (cue, text) in enumerate(f["pfade"]):
        nxt = f["pfade"][k + 1][0] if k + 1 < len(f["pfade"]) else None
        pf.append(T(text, 40, 1034, cue, "Medium", 30, farbe=PFAD_FARBE[f["bg"]], anim="fade", bis=nxt))
    f["els"] = pf + f["els"]
    for e in f["els"]:
        e.t0 = zeit(e.cue) + e.d
        e.t1 = zeit(e.bis) if e.bis is not None else None
        genutzt.add(e.cue if isinstance(e.cue, str) else e.cue[0])
        if hasattr(e, "weg"):
            s0, s1, dx, dy = e.weg
            e.w0, e.w1, e.wdx, e.wdy = zeit(s0), zeit(s1), dx, dy
        if hasattr(e, "ton"):
            klang, gain, vers = e.ton
            sfx_liste.append((e.t0 + vers, klang, gain))
    f["start"] = min(e.t0 for e in f["els"])
# Stand 30.09.2026: nur Handlungsgeräusche (szene_*), keine UI-, Wisch- oder Blättergeräusche
assert all(k.startswith("szene_") for _, k, _ in sfx_liste), "Nur Handlungsgeräusche erlaubt"
# Prüfpfad-Wechsel als Kapitelquelle für YouTube (tools/youtube_metadaten.py)
json.dump([{"t": round(zeit(c), 3), "pfad": txt} for f_ in FOLIEN for c, txt in f_["pfade"]],
          open("../kapitel.json", "w"), ensure_ascii=False, indent=1)
fehl = set(cues) - genutzt
assert not fehl, f"Marken ohne Bildelement: {fehl}"
# Folge 100 (wie 097, 095, 076, 073, 027): Prüfpfad und Grundbild der ersten Szene stehen ab 0,0 s (direkt nach dem Intro), ohne Einblendung
for e in FOLIEN[0]["els"]:
    if e.t0 <= cues["fall"]["t"] + 1e-6:
        e.t0, e.anim = 0.0, "cut"
FOLIEN[0]["start"] = 0.0
for a, b in zip(FOLIEN, FOLIEN[1:]):
    assert b["start"] > a["start"]
    for e in a["els"]:
        assert e.t0 < b["start"] - WISCH / FPS, f"Element erscheint erst im Übergang: {e.name}"


def ease(x):
    return 1 - (1 - x) ** 3


def ease_io(x):
    return 3 * x * x - 2 * x * x * x


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
    x, y = int(x), int(y)
    if x + sp.width <= 0 or y + sp.height <= 0 or x >= W or y >= H:     # vollständig außerhalb (einfahrende Autos)
        return
    if x < 0 or y < 0:
        sp = sp.crop((max(0, -x), max(0, -y), sp.width, sp.height)); x, y = max(0, x), max(0, y)
    base.alpha_composite(sp, (x, y))


def versatz(e, t):
    if not hasattr(e, "weg"):
        return 0, 0
    fr = min(1.0, max(0.0, (t - e.w0) / max(1e-6, e.w1 - e.w0)))
    k = 1 - ease_io(fr)
    return e.wdx * k, e.wdy * k


def fertig(e, t):
    if (t - e.t0) * FPS < DUR[e.anim]:
        return False
    return not hasattr(e, "weg") or t >= e.w1


def zeichne(base, e, t):
    ox, oy = versatz(e, t)
    k = (t - e.t0) * FPS
    n = DUR[e.anim]
    if k >= n:
        setze(base, e.sprite, e.x + ox, e.y + oy)
        return
    x = k / n
    if e.anim == "rise":
        dy = int((1 - ease(x)) * 26)
        setze(base, mit_alpha(e.sprite, ease(x)), e.x + ox, e.y + dy + oy)
    elif e.anim in ("fade", "cut"):
        setze(base, mit_alpha(e.sprite, ease(x)), e.x + ox, e.y + oy)
    elif e.anim == "grow":
        h = int(e.h0 + (e.h1 - e.h0) * ease(x))
        setze(base, e.macher(h), e.x, e.y)
    else:  # pop
        s = max(0.05, 0.55 + 0.45 * back(x))
        w, h = max(1, int(e.sprite.width * s)), max(1, int(e.sprite.height * s))
        sp = mit_alpha(e.sprite.resize((w, h), Image.BILINEAR), min(1, x * 2.2))
        cx, cy = e.x + ox + e.sprite.width / 2, e.y + oy + e.sprite.height / 2
        setze(base, sp, cx - w / 2, cy - h / 2)


import re as _re
OHNE_MUND = False
def ist_mund(e):
    """Zusätzliche Mundzustände (…_a/_o/_e.png) zählen nicht als Bildhalt."""
    return bool(_re.search(r"_[aoe]\.png$", e.name or ""))


cache = {}
def folienbild(fi, t):
    f = FOLIEN[fi]
    sichtbar = [e for e in f["els"] if e.t0 <= t and (e.t1 is None or t < e.t1) and not (OHNE_MUND and ist_mund(e))]
    statisch = tuple(id(e) for e in sichtbar if fertig(e, t))
    # Reihenfolge der Ebenen erhalten: Nur ein statisches Präfix wird gecacht
    praefix = []
    for e in sichtbar:
        if id(e) in statisch:
            praefix.append(e)
        else:
            break
    key = (fi, tuple(id(e) for e in praefix))
    if key not in cache:
        cache.clear()
        b = BG[f["bg"]].copy()
        for e in praefix:
            zeichne(b, e, t)
        cache[key] = b
    rest = sichtbar[len(praefix):]
    if not rest:
        return cache[key], True
    b = cache[key].copy()
    for e in rest:
        zeichne(b, e, t)
    return b, False


def frame(t):
    fi = 0
    while fi + 1 < len(FOLIEN) and t >= FOLIEN[fi + 1]["start"]:
        fi += 1
    img, stat = folienbild(fi, t)
    if fi + 1 < len(FOLIEN):
        rest = (FOLIEN[fi + 1]["start"] - t) * FPS
        if rest < WISCH:
            # Schiebe-Wisch: alte Folie nach links hinaus, leerer Hintergrund der neuen Folie von rechts
            p = ease_io(1 - rest / WISCH)
            dx = int(p * W)
            out = Image.new("RGBA", (W, H))
            out.paste(img.crop((dx, 0, W, H)), (0, 0))
            out.paste(BG[FOLIEN[fi + 1]["bg"]].crop((0, 0, dx, H)), (W - dx, 0))
            return out, False
    return img, stat


if "--manifest" in sys.argv:                    # Bildhalt-Manifest: Zustandswechsel ohne Mundzustände, SHA-256 je Keyframe
    import hashlib, os
    OHNE_MUND = True
    os.makedirs(f"{OUT}/bildhalte", exist_ok=True)
    zeiten = set()
    for fi, f_ in enumerate(FOLIEN):
        zeiten.add(round(f_["start"], 3))
        for e in f_["els"]:
            if ist_mund(e):
                continue
            zeiten.add(round(e.t0, 3))
            if e.t1 is not None:
                zeiten.add(round(e.t1, 3))
    zeiten = sorted(t for t in zeiten if 0 <= t < dauer) + [dauer]
    halte, gesehen = [], {}
    for a_, b_ in zip(zeiten, zeiten[1:]):
        if b_ - a_ < 0.35:                      # Animationsschritte unter 0,35 s sind kein eigener Halt
            continue
        tk = b_ - 0.04
        if any(abs(b_ - f_["start"]) < 1e-3 for f_ in FOLIEN[1:]):
            tk = b_ - (WISCH + 2) / FPS              # Keyframe vor der Schiebeblende, nicht mitten im Wisch
            if tk <= a_:
                continue
        im, _ = frame(tk)
        h = hashlib.sha256(im.convert("RGB").tobytes()).hexdigest()
        fi = max(i for i, f_ in enumerate(FOLIEN) if f_["start"] <= tk)
        pfad = next((txt for c, txt in reversed(FOLIEN[fi]["pfade"]) if zeit(c) <= tk), FOLIEN[fi]["pfade"][0][1])
        neu = h not in gesehen
        if neu:
            gesehen[h] = len(halte) + 1
            im.convert("RGB").resize((480, 270)).save(f"{OUT}/bildhalte/{len(gesehen):03d}.jpg", quality=85)
        halte.append(dict(nr=len(halte) + 1, start=round(a_, 3), ende=round(b_, 3), folie=fi + 1, pruefpfad=pfad,
                          sha256=h, eigenstaendig=neu, gleich_wie=None if neu else gesehen[h]))
    json.dump(dict(dauer=dauer, bildhalte=len(halte), eigenstaendig=len(gesehen), halte=halte),
              open("../bildhalt_manifest.json", "w"), ensure_ascii=False, indent=1)
    print("Bildhalte:", len(halte), "eigenständig:", len(gesehen))
    sys.exit()

if "--frames" in sys.argv:                      # Einzelbilder zu Zeitpunkten (Sekunden, kommagetrennt) zur Sichtprüfung
    import os
    os.makedirs(f"{OUT}/einzel", exist_ok=True)
    for ts in sys.argv[sys.argv.index("--frames") + 1].split(","):
        im, _ = frame(float(ts))
        im.convert("RGB").save(f"{OUT}/einzel/t{float(ts):07.2f}.png")
    sys.exit()

if nur_vorschau:
    import os
    os.makedirs(f"{OUT}/frames", exist_ok=True)
    bilder = []
    for fi, f in enumerate(FOLIEN):
        tend = (FOLIEN[fi + 1]["start"] - (WISCH + 2) / FPS) if fi + 1 < len(FOLIEN) else dauer - 0.1
        im, _ = frame(tend)
        im.convert("RGB").save(f"{OUT}/frames/folie_{fi+1:02d}.png"); bilder.append(im.convert("RGB"))
    tw, th, cols = 640, 360, 3
    rows = (len(bilder) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * tw, rows * th), (255, 255, 255))
    for i, b in enumerate(bilder):
        sheet.paste(b.resize((tw, th)), ((i % cols) * tw, (i // cols) * th))
    sheet.save(f"{OUT}/kontaktbogen.png")
    print("Vorschau:", len(bilder), "Folien", [round(f["start"], 2) for f in FOLIEN])
    sys.exit()

# --- Tonspur: Stimme + Geräusche -----------------------------------------------------------------------
SR = 48000
SFXD = "../../sfx/wav/"
SFX3 = "../../sfx3/"          # Standardbibliothek (Freesound CC0 + ElevenLabs), Herkunft in sfx3/herkunft.json
import glob
_zaehler = {}
def waehle(klang):
    """'haken*' -> reihum haken_1, haken_2, … (Varianten abwechseln)."""
    if not klang.endswith("*"):
        return klang
    basis = klang[:-1]
    var = sorted(os.path.basename(p)[:-4] for p in glob.glob(SFX3 + basis + "_*.wav"))
    i = _zaehler.get(basis, 0); _zaehler[basis] = i + 1
    return var[i % len(var)]
def lade(name):
    w = wave.open((SFX3 if os.path.exists(SFX3 + name + ".wav") else SFXD) + name + ".wav")
    assert w.getframerate() == SR
    return np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768

wv = wave.open("../stimme_48k.wav")
stimme = np.frombuffer(wv.readframes(wv.getnframes()), np.int16).astype(np.float32).reshape(-1, 2) / 32768
sfx = np.zeros(len(stimme), np.float32)
# Pegel je Klangart (Spitzenwert relativ zur Stimme); Sprache bleibt deutlich vorn
PEGEL = {"haken": 0.13, "kreuz": 0.13, "blatt": 0.07, "papier": 0.10, "unterstreichen": 0.11, "textmarker": 0.09,
         "swoosh": 0.08, "klick": 0.09, "szene": 0.12, "default": 0.11}
protokoll = []
for t0, klang, gain in sorted(sfx_liste, key=lambda s: s[0]):
    klang = waehle(klang)
    x = lade(klang)
    art = klang.rsplit("_", 1)[0] if klang.rsplit("_", 1)[0] in PEGEL else "default"
    x = x / (np.abs(x).max() + 1e-9) * PEGEL[art] * gain
    n = int(t0 * SR)
    if n < 0:
        x = x[-n:]; n = 0
    e = min(len(sfx), n + len(x))
    sfx[n:e] += x[: e - n]
    protokoll.append(dict(t=round(t0, 3), klang=klang, pegel=round(float(np.abs(x).max()), 3)))
mix = stimme + sfx[:, None]
spitze = float(np.abs(mix).max())
if spitze > 0.97:
    mix *= 0.97 / spitze
with wave.open(f"{OUT}/ton_mix.wav", "wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((np.clip(mix, -1, 1) * 32767).astype(np.int16).tobytes())
json.dump(protokoll, open(f"{OUT}/sfx_cues.json", "w"), indent=1)
print("SFX:", len(protokoll), "Einsätze, Spitze", round(spitze, 3))

ff = imageio_ffmpeg.get_ffmpeg_exe()
cmd = [ff, "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
       "-i", f"{OUT}/ton_mix.wav", "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-preset", "medium", "-crf", "18",
       "-pix_fmt", "yuv420p", "-profile:v", "high", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
       "-movflags", "+faststart", "-shortest", f"{OUT}/" + os.environ.get("VIDEONAME", "100-Ruecktritt-24-StGB-Hauptfilm") + ".mp4"]
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
