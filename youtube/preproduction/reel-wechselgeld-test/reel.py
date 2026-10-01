"""Instagram-Reel „Zu viel Wechselgeld“ (1080 × 1920, 30 fps): Open-Peeps-Szene an der Kasse, große Schlagzeilen,
Wort-für-Wort-Untertitel (eingebrannt, weil Reels meist ohne Ton laufen), Stimme Carla, nur Handlungsgeräusche.

    python3 reel.py [--bild SEKUNDE]      # --bild: nur ein Standbild zur Kontrolle"""
import json, math, os, subprocess, sys, wave
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
import imageio_ffmpeg

sys.path.insert(0, "/home/user/herrjurist/youtube/thumbnails")
import thumbnail as T

W, H, FPS = 1080, 1920, 30
cj = json.load(open("../cues.json"))
C = {k: v["t"] for k, v in cj["cues"].items()}
DAUER = cj["dauer"]
INK, GELB, WEISS = (20, 20, 20, 255), (255, 210, 63, 255), (255, 255, 255, 255)
ROT = (215, 38, 61)
SAFE_OBEN, SAFE_UNTEN = 230, 1500          # Instagram blendet oben Kopfzeile, unten Text und Buttons ein


# --- Bausteine ---------------------------------------------------------------------------------------------------------
def hintergrund():
    r, g, b = ROT
    grund = Image.new("RGBA", (W, H), (r, g, b, 255))
    v = Image.new("L", (W, H), 0); ImageDraw.Draw(v).ellipse((-W * .4, -H * .1, W * 1.4, H * 1.0), fill=255)
    dunkel = Image.new("RGBA", (W, H), (int(r * .62), int(g * .62), int(b * .62), 255))
    return Image.composite(grund, dunkel, v.filter(ImageFilter.GaussianBlur(220)))


def text(zeilen, groesse, max_b=980, farbe=WEISS, kontur=14):
    """Großer Text, '*wort' gelb. Gibt ein freigestelltes Bild zurück (Breite höchstens max_b)."""
    while True:
        f = T.font(groesse)
        breite = max(f.getlength(z.replace("*", "")) for z in zeilen)
        if breite <= max_b or groesse < 50: break
        groesse -= 4
    zh = int(groesse * 1.02)
    im = Image.new("RGBA", (int(breite) + 2 * kontur + 20, zh * len(zeilen) + 2 * kontur + 24))
    d = ImageDraw.Draw(im)
    for i, z in enumerate(zeilen):
        x = (im.width - f.getlength(z.replace("*", ""))) / 2; y = kontur + i * zh
        for wort in z.split(" "):
            gelb = wort.startswith("*"); wort = wort.lstrip("*") + " "
            d.text((x + 6, y + 9), wort, font=f, fill=(0, 0, 0, 110), stroke_width=kontur, stroke_fill=(0, 0, 0, 110))
            d.text((x, y), wort, font=f, fill=GELB if gelb else farbe, stroke_width=kontur, stroke_fill=INK)
            x += f.getlength(wort)
    return im.crop(im.getbbox())


def emoji(name, g, dreh=0):
    return T.sticker(T.emoji(name, g, drehen=dreh), 9)


def figur(spec, hoehe):
    im = T.person(spec)
    im = im.resize((int(im.width * hoehe / im.height), hoehe), Image.LANCZOS)
    return T.sticker(T.linien_verstaerken(im, 2), 10)


def geldschein(wert, breite=300):
    h = int(breite * 0.52)
    im = Image.new("RGBA", (breite + 20, h + 20)); d = ImageDraw.Draw(im)
    farbe = {"50": (246, 145, 60), "5": (170, 170, 170)}[wert]
    d.rounded_rectangle((10, 10, breite + 10, h + 10), radius=18, fill=farbe + (255,), outline=INK, width=6)
    d.rounded_rectangle((28, 28, breite - 8, h - 8), radius=12, outline=(255, 255, 255, 170), width=4)
    f = T.font(int(h * 0.55))
    t = f"{wert} €"; tw = f.getlength(t)
    d.text(((breite + 20 - tw) / 2, h * 0.18), t, font=f, fill=WEISS, stroke_width=6, stroke_fill=INK)
    return T.sticker(im.rotate(-8, expand=True, resample=Image.BICUBIC), 8)


def strich(breite):
    """Roter Durchstreich-Balken über einer Schlagzeile (Wort bleibt lesbar)."""
    im = Image.new("RGBA", (breite + 40, 90)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((20, 33, breite + 20, 57), radius=12, fill=(235, 30, 50, 230), outline=INK, width=4)
    return im.rotate(-7, expand=True, resample=Image.BICUBIC)


def tafel(text_zeile, breite=520, farbe=(255, 255, 255, 255)):
    f = T.font(64)
    tw = f.getlength(text_zeile)
    im = Image.new("RGBA", (int(max(breite, tw + 70)), 110)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, im.width - 1, 109), radius=26, fill=INK)
    d.text(((im.width - tw) / 2, 14), text_zeile, font=f, fill=farbe)
    return T.sticker(im, 8)


# --- Zeitachse ---------------------------------------------------------------------------------------------------------
def ease_back(x):
    c1 = 1.70158; c3 = c1 + 1
    return 1 + c3 * (x - 1) ** 3 + c1 * (x - 1) ** 2


def ease(x):
    return 1 - (1 - x) ** 3


class E:
    """Element: Bild, Mittelpunkt (x, y), sichtbar von t0 bis t1, Einblendung 'pop'/'fade'/'slide'/'stempel'/'hart'."""
    def __init__(self, img, x, y, t0, t1=None, ein="pop", dauer=0.28, z=5, wege=(), wackeln=0.0):
        self.img, self.x, self.y, self.t0, self.t1, self.ein, self.dauer, self.z = img, x, y, t0, t1, ein, dauer, z
        self.wege, self.wackeln = list(wege), wackeln          # wege: (ta, tb, x2, y2, alpha2)

    def zustand(self, t):
        if t < self.t0 or (self.t1 is not None and t >= self.t1): return None
        x, y, a, s, rot = self.x, self.y, 1.0, 1.0, 0.0
        for ta, tb, x2, y2, a2 in self.wege:
            if t >= tb: x, y, a = x2, y2, a2
            elif t > ta:
                k = ease((t - ta) / (tb - ta)); x, y, a = x + (x2 - x) * k, y + (y2 - y) * k, a + (a2 - a) * k
        p = min(1.0, (t - self.t0) / self.dauer) if self.dauer else 1.0
        if self.ein == "pop": s = 0.4 + 0.6 * ease_back(p); a *= min(1, p * 3)
        elif self.ein == "stempel": s = 2.2 - 1.2 * ease(p); a *= min(1, p * 2); rot = -12 * (1 - p)
        elif self.ein == "fade": a *= p
        elif self.ein == "slide": y += (1 - ease(p)) * 160; a *= p
        if self.wackeln and t - self.t0 < 0.5:
            rot += math.sin((t - self.t0) * 40) * self.wackeln * (1 - (t - self.t0) / 0.5)
        if self.t1 is not None and self.t1 - t < 0.12: a *= (self.t1 - t) / 0.12
        return x, y, a, s, rot

    def zeichnen(self, bild, t):
        z = self.zustand(t)
        if not z: return
        x, y, a, s, rot = z
        im = self.img
        if abs(s - 1) > 0.01: im = im.resize((max(1, int(im.width * s)), max(1, int(im.height * s))), Image.BILINEAR)
        if abs(rot) > 0.2: im = im.rotate(rot, expand=True, resample=Image.BILINEAR)
        if a < 0.99:
            im = im.copy(); im.putalpha(im.getchannel("A").point(lambda v: int(v * max(0, a))))
        bild.alpha_composite(im, (int(x - im.width / 2), int(y - im.height / 2))) if x - im.width / 2 >= 0 and y - im.height / 2 >= 0 \
            else bild.paste(im, (int(x - im.width / 2), int(y - im.height / 2)), im)


# --- Szene -------------------------------------------------------------------------------------------------------------
EL = []
THEKE_OBEN, THEKE_UNTEN = 1170, 1370
KOPF_Y = 430                                 # Mitte der Schlagzeilen

kass = dict(pose="standing/robot_dance-1", kopf="Long Curly", farben={"Skin": "#D9A07A", "Top": "#7FB2F0"}, spiegeln=False)
kund = dict(pose="standing/robot_dance-1", kopf="Short 2", farben={"Skin": "#F1C6A5", "Top": "#9BD88A"}, spiegeln=True)
FIG_H = 1060
FIG_OBEN = 640


def figur_zustaende(spec, gesichter, cx):
    """Gesicht wechselt zu den genannten Zeiten; Figur unten an der Theke abgeschnitten."""
    bilder = []
    for i, (t0, gesicht) in enumerate(gesichter):
        im = figur(dict(spec, gesicht=gesicht), FIG_H)
        im = im.crop((0, 0, im.width, min(im.height, THEKE_UNTEN - FIG_OBEN)))
        t1 = gesichter[i + 1][0] if i + 1 < len(gesichter) else C["cta"]
        bilder.append((im, t0, t1))
    return [E(im, cx, FIG_OBEN + im.height / 2, t0, t1, ein="hart", dauer=0.0, z=2)
            for i, (im, t0, t1) in enumerate(bilder)]


EL += figur_zustaende(kass, [(0.0, "Smile"), (C["behalten"], "Rage")], 280)
EL += figur_zustaende(kund, [(0.0, "Calm"), (C["merkt"], "Awe"), (C["steckt"], "Cheeky"), (C["aber"], "Concerned Fear")], 800)

theke = Image.new("RGBA", (W - 60, THEKE_UNTEN - THEKE_OBEN + 20)); d = ImageDraw.Draw(theke)
d.rounded_rectangle((10, 10, theke.width - 10, theke.height - 10), radius=22, fill=(139, 90, 60, 255), outline=INK, width=7)
d.line((10, 60, theke.width - 10, 60), fill=INK, width=6)
theke = T.sticker(theke, 8)
EL.append(E(theke, W / 2, (THEKE_OBEN + THEKE_UNTEN) / 2, 0.0, C["cta"], ein="hart", dauer=0, z=4))
EL.append(E(emoji("receipt", 150, 8), 140, THEKE_OBEN - 30, 0.0, C["cta"], ein="hart", dauer=0, z=4))

# Geldschein: Kassiererin -> Kunde -> Tasche -> Hand -> zurück zur Kassiererin
hand_k, hand_c = (520, 905), (585, 905)
schein = geldschein("50", 300)
EL.append(E(schein, 470, 1010, 0.0, C["steckt"] + 0.6, ein="hart", dauer=0, z=6, wege=[
    (0.55, 1.15, 650, 1010, 1.0),
    (C["steckt"], C["steckt"] + 0.55, 830, 1330, 0.0)]))
EL.append(E(schein, 650, 1010, C["eigen"], None, ein="pop", z=6, wege=[
    (C["bgb"] + 0.3, C["bgb"] + 1.1, 460, 1010, 1.0)]))
EL[-1].t1 = C["cta"]
EL.append(E(emoji("eyes", 140), 900, 640, C["merkt"], C["steckt"], z=7))
EL.append(E(emoji("zipper-mouth-face", 170), 950, 700, C["schweigen"], C["pflicht"], z=7))
EL.append(E(emoji("bell-with-slash", 190), 540, 820, C["pflicht"], C["unt"], z=7))
EL.append(E(emoji("check-mark-button", 130), 800, 880, C["eigen"] + 0.3, C["aber"], z=7))
EL.append(E(emoji("red-exclamation-mark", 170), 120, 700, C["behalten"], C["bgb"], z=7, wackeln=10))

# Schlagzeilen (wechseln mit dem Satz)
def kopf(zeilen, t0, t1, groesse=150, ein="pop", wackeln=0.0, y=KOPF_Y):
    EL.append(E(text(zeilen, groesse), W / 2, y, t0, t1, ein=ein, dauer=0.25, z=8, wackeln=wackeln))

kopf(["*50 €", "STATT 5 €"], 0.0, C["frage"], 140, ein="hart", y=KOPF_Y + 20)
kopf(["*BETRUG?"], C["frage"], C["unt"], 190)
EL.append(E(tafel("§ 263 StGB"), W / 2, KOPF_Y + 165, C["nein"], C["unt"], ein="slide", z=8))
EL.append(E(strich(760), W / 2, KOPF_Y, C["nein"], C["unt"], ein="stempel", dauer=0.3, z=9))
EL.append(E(emoji("cross-mark", 120), W / 2 + 270, KOPF_Y + 165, C["nein"] + 0.2, C["unt"], z=9))
kopf(["*UNTERSCHLAGUNG?"], C["unt"], C["aber"], 130)
EL.append(E(tafel("§ 246 StGB"), W / 2, KOPF_Y + 140, C["unt"] + 0.3, C["aber"], ein="slide", z=8))
EL.append(E(strich(1000), W / 2, KOPF_Y, C["unt2"], C["aber"], ein="stempel", dauer=0.3, z=9))
EL.append(E(emoji("cross-mark", 120), W / 2 + 260, KOPF_Y + 140, C["unt2"] + 0.2, C["aber"], z=9))
kopf(["*ABER!"], C["aber"], C["bgb"], 230, wackeln=6)
kopf(["*§ 812 BGB"], C["bgb"], C["cta"], 170)
EL.append(E(tafel("45 € ZURÜCK"), W / 2, KOPF_Y + 165, C["bgb"] + 0.4, C["cta"], ein="slide", z=8))

# Schluss: Lexi mit Mundbewegung + Aufforderung
lexi_zu = figur({"lexi": "erklaert_zu", "spiegeln": False}, 1500)
lexi_auf = figur({"lexi": "erklaert_auf", "spiegeln": False}, 1500)
lexi_zu, lexi_auf = [im.crop((0, 0, im.width, 1500 - 640)) for im in (lexi_zu, lexi_auf)]
cta_seg = [s for s in cj["segmente"] if s["start"] >= C["cta"] - 0.05][0]


class Lexi(E):
    def zeichnen(self, bild, t):
        offen = any(a <= t <= b and int((t - a) / 0.11) % 2 == 0 for a, b in cta_seg["woerter"])
        self.img = lexi_auf if offen else lexi_zu
        super().zeichnen(bild, t)

EL.append(Lexi(lexi_zu, 600, 1500 - lexi_zu.height / 2, C["cta"], None, ein="slide", dauer=0.35, z=3))
kopf(["FOLG", "*@LEXVERSE"], C["cta"], None, 150, y=440)

# --- Untertitel (Wort für Wort, Schriftform) ---------------------------------------------------------------------------
ERSATZ = [(["Fünfzig"], "50"), (["fünf"], "5"), (["fünfundvierzig"], "45"), (["dreißig"], "30"),
          (["Paragraf", "achthundertzwölf"], "§ 812"), (["B.G.B"], "BGB")]
woerter = []
for s in cj["segmente"]:
    for w, (a, b) in zip(s["text"].split(" "), s["woerter"]):
        woerter.append([w, a, b])
i, untertitel = 0, []
while i < len(woerter):
    for quelle, ziel in ERSATZ:
        n = len(quelle)
        teil = [x[0].rstrip(".,!?:") for x in woerter[i:i + n]]
        if teil == quelle:
            satzzeichen = woerter[i + n - 1][0][len(woerter[i + n - 1][0].rstrip(".,!?:")):]
            if ziel == "BGB": satzzeichen = ""                        # Punkte der Abkürzung, kein Satzende
            untertitel.append([ziel + satzzeichen, woerter[i][1], woerter[i + n - 1][2]]); i += n; break
    else:
        if woerter[i][0] == "–" and untertitel: untertitel[-1][0] += " –"
        else: untertitel.append(list(woerter[i]))
        i += 1
gruppen, akt = [], []
for w in untertitel:
    akt.append(w)
    if len(akt) == 3 or len(" ".join(x[0] for x in akt)) > 14 or w[0][-1] in ".!?:–,":
        gruppen.append(akt); akt = []
if akt: gruppen.append(akt)
UT_Y = 1460
FU = T.font(104)


def untertitel_bild(t):
    for k, g in enumerate(gruppen):
        ende = gruppen[k + 1][0][1] if k + 1 < len(gruppen) else g[-1][2] + 0.6
        ende = min(ende, g[-1][2] + 0.7)
        if g[0][1] - 0.05 <= t < ende:
            break
    else:
        return None
    zeile = " ".join(w[0] for w in g)
    f = FU
    while f.getlength(zeile) > 980: f = T.font(f.size - 4)
    im = Image.new("RGBA", (W, 190)); d = ImageDraw.Draw(im)
    x = (W - f.getlength(zeile)) / 2
    for j, w in enumerate(g):
        aktiv = w[1] - 0.03 <= t < (g[j + 1][1] if j + 1 < len(g) else ende)
        wort = w[0] + (" " if j < len(g) - 1 else "")
        d.text((x + 5, 37), wort, font=f, fill=(0, 0, 0, 110), stroke_width=13, stroke_fill=(0, 0, 0, 110))
        d.text((x, 30), wort, font=f, fill=GELB if aktiv else WEISS, stroke_width=13, stroke_fill=INK)
        x += f.getlength(wort)
    return im


# --- Rendern -----------------------------------------------------------------------------------------------------------
BG = hintergrund()
EL.sort(key=lambda e: e.z)


def frame(t):
    bild = BG.copy()
    for e in EL:
        e.zeichnen(bild, t)
    ut = untertitel_bild(t)
    if ut: bild.alpha_composite(ut, (0, UT_Y - 70))
    return bild


if "--bild" in sys.argv:
    for s in sys.argv[sys.argv.index("--bild") + 1].split(","):
        frame(float(s)).convert("RGB").save(f"../bild_{s}.png")
    sys.exit()

# Ton: Stimme + Handlungsgeräusche
SR = 48000
wv = wave.open("../stimme.wav")
stimme = np.frombuffer(wv.readframes(wv.getnframes()), np.int16).astype(np.float32) / 32768
def lade(n):
    w = wave.open(f"../sfx/{n}.wav"); return np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768
mix = stimme.copy()
for t0, n, pegel in ((0.35, "szene_kasse", 0.16), (C["steckt"] + 0.15, "szene_muenzen", 0.14), (C["eigen"] - 0.05, "szene_muenzen", 0.10),
                     (C["bgb"] + 0.3, "szene_kasse", 0.10)):
    x = lade(n); x = x / (np.abs(x).max() + 1e-9) * pegel
    a = int(t0 * SR); e = min(len(mix), a + len(x)); mix[a:e] += x[:e - a]
mix *= min(1.0, 0.95 / np.abs(mix).max())
with wave.open("../ton_mix.wav", "wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((np.repeat(np.clip(mix, -1, 1)[:, None], 2, axis=1) * 32767).astype(np.int16).tobytes())

ff = imageio_ffmpeg.get_ffmpeg_exe()
os.makedirs("../out", exist_ok=True)
cmd = [ff, "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
       "-i", "../ton_mix.wav", "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-preset", "medium", "-crf", "19",
       "-pix_fmt", "yuv420p", "-profile:v", "high", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
       "-movflags", "+faststart", "-shortest", "../out/Reel-Wechselgeld.mp4"]
p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
for fr in range(int(round(DAUER * FPS))):
    p.stdin.write(frame(fr / FPS).convert("RGB").tobytes())
p.stdin.close(); p.wait()
print("fertig", round(DAUER, 2), "s")
