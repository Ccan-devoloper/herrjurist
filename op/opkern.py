"""Kern der Open-Peeps-Vorproduktion (Variante C) für Examenscampus und Herrjurist.

Gemeinsame Bausteine für Karussell (1080×1350), Story (1080×1920) und Reel (1080×1920):
Rahmen in der Klausurfarbe, Schlagzeilen, Normzeilen, Karten, Kalenderblatt, Gesetzesseite,
Brustbilder mit Sprechblasen. Die Regeln dazu stehen in REDAKTION.md.
"""
import json, os, re, sys

HIER = os.path.dirname(os.path.abspath(__file__))
os.environ.setdefault("OP_RES", os.path.join(HIER, ".res"))
sys.path.insert(0, os.path.join(HIER, "lib"))
sys.path.insert(0, os.path.join(HIER, "ressourcen", "peeps-bibliothek"))

import numpy as np
from PIL import Image, ImageDraw, ImageFont
import engine, bausteine
from bausteine import *            # noqa: F401,F403  (Palette, titel, pille, absatz, fl_block, karte, icon, ficon, blase …)

RES = os.environ["OP_RES"]
# Kanal: Standard Examenscampus; ein anderer Kanal (Herrjurist) legt marke.json neben diese Datei.
MARKE = {"kanal": "examenscampus", "fachLabel": "Steuerberaterexamen", "klausurLabel": None, "reelZielS": 44.4, "reelMaxS": 45.5}
if os.path.exists(os.path.join(HIER, "marke.json")):
    MARKE.update(json.load(open(os.path.join(HIER, "marke.json"), encoding="utf-8")))
bausteine.FIGORDNER = "op_ec/"
C = "_"

# ---------------------------------------------------------------- Farben
PASTELL = {0: LILA, 1: BLAU, 2: ORANGE, 3: GRUEN, 4: LILA}         # 4 = Wochenrückblick (Herrjurist): lila wie „Sonstiges“
FEED = {0: (124, 92, 255, 255), 1: (45, 91, 227, 255), 2: (255, 122, 69, 255), 3: (35, 217, 139, 255), 4: (124, 92, 255, 255)}
HELL = (255, 251, 230, 255)
FALLE_FILL = (255, 240, 234, 255)
GRAUTEXT = (92, 92, 104, 255)          # Normen auf Folgefolien (F3a)
NORMFARBE = (88, 62, 190, 255)         # Normen im Reel (eine ruhige lila Zeile je Szene)
FARBEN = {"WEISS": WEISS, "GELB": GELB, "GRUEN": GRUEN, "ROT": ROT, "BLAU": BLAU, "LILA": LILA, "TUERKIS": TUERKIS,
          "ORANGE": ORANGE, "PINK": PINK, "HELL": HELL, None: WEISS}
MARK = {"g": (255, 222, 89, 150), "r": (255, 140, 140, 140), "b": (140, 190, 255, 150), "gr": (120, 220, 150, 150)}

TITEL, TEXT, KLEIN = 62, 40, 32         # Mindestgrößen Karussell
SERIF = lambda s: ImageFont.truetype(os.path.join(RES, "fonts", "LiberationSerif-Regular.ttf"), s)
SERIFB = lambda s: ImageFont.truetype(os.path.join(RES, "fonts", "LiberationSerif-Bold.ttf"), s)
HAND = lambda s: ImageFont.truetype(os.path.join(RES, "fonts", "Caveat.ttf"), s)


class Format:
    """Bildformat samt Grenzen; wird je Ausgabe gesetzt (engine.W/H steuern die Bausteine)."""
    def __init__(self, w, h, rahmen_innen=24):
        self.W, self.H = w, h
        self.innen_unten = h - rahmen_innen

    def aktiv(self):
        engine.W, engine.H = self.W, self.H
        global AKTIV
        AKTIV = self


KARUSSELL = Format(1080, 1350)
STORY = Format(1080, 1920)
AKTIV = KARUSSELL
X0, X1 = 64, 1016                       # im Profilraster (3:4) sichtbarer Bereich


def worte(*texte):
    return sum(len(str(t).replace("§", " ").split()) for t in texte if t)


def zusammensetzen(els, klausur, fmt=None, rund=30):
    """Ebenen auf Creme legen, Rahmen in der Klausurfarbe zuletzt (schneidet Brustbilder sauber ab)."""
    fmt = fmt or AKTIV
    W_, H_ = fmt.W, fmt.H
    bg = Image.new("RGBA", (W_, H_), CREME)
    for e in els:
        sp, x, y = e.sprite, int(e.x), int(e.y)
        if x >= W_ or y >= H_ or x + sp.width <= 0 or y + sp.height <= 0:
            continue
        cx0, cy0 = max(0, -x), max(0, -y)
        sp = sp.crop((cx0, cy0, min(sp.width, W_ - x), min(sp.height, H_ - y)))
        if sp.width > 0 and sp.height > 0:
            bg.alpha_composite(sp, (x + cx0, y + cy0))
    ov = Image.new("RGBA", (W_, H_), FEED[klausur])
    m = Image.new("L", (W_, H_), 255)
    ImageDraw.Draw(m).rounded_rectangle((24, 24, W_ - 24, H_ - 24), rund, fill=0)
    ov.putalpha(m)
    ImageDraw.Draw(ov).rounded_rectangle((18, 18, W_ - 18, H_ - 18), rund + 4, outline=INK, width=6)
    bg.alpha_composite(ov)
    return bg.convert("RGB")


# ---------------------------------------------------------------- Figuren-Hilfen
def peep(name, cx, unten, hoehe, **k):
    return peep_voll(name, cx, unten, int(hoehe), C, **k)


def nah(name, cx, oben, max_h=600):
    """Brustbild am unteren Rand (unten angeschnitten), so groß wie Platz ist."""
    hoehe = int(min(max_h, AKTIV.innen_unten + 70 - oben))
    for _ in range(6):                 # breite Büsten (z. B. Macbook) erst kleiner, dann zur Mitte rücken
        try:
            return peep_voll(name, cx, AKTIV.innen_unten + 70, hoehe, C, unten_offen=True)
        except AssertionError:
            hoehe = int(hoehe * 0.9); cx = int(cx + (540 - cx) * 0.25)
    return peep_voll(name, cx, AKTIV.innen_unten + 70, hoehe, C, unten_offen=True)


def kopfpunkt(e, seite):
    a = np.asarray(e.sprite)[..., 3] > 40
    ys, xs = np.nonzero(a[: int(a.shape[0] * 0.3)])
    return int(e.x + (xs.max() if seite > 0 else xs.min())), int(e.y + int(a.shape[0] * 0.18))


def bl(art, w, h, cx, cy, text, ziel, size=36):
    """Sprech-/Denkblase; die Blasen-Engine arbeitet in 1920×1080, darum wird bei Bedarf verschoben."""
    zx, zy = kopfziel(ziel, art, cx) if len(ziel) == 4 else ziel
    dy = max(0, max(cy, zy) + h - 1040)
    W_, H_ = engine.W, engine.H
    engine.W, engine.H = 1920, 1080
    try:
        e = blase(art, w, h, C, cx, cy - dy, text, textsize=size, ziel=(zx, zy - dy))
    finally:
        engine.W, engine.H = W_, H_
    e.y += dy
    return e


def blase_zu(els, bueste, unten, blase_, max_h=520):
    """Brustbild unter der Karte; Sprechblase auf der freien Seite, mit adaptiver Breite."""
    if not bueste:
        return
    if unten + 150 > AKTIV.innen_unten - 220:          # kein Platz für ein Brustbild: lieber ohne Figur
        return
    name, cx = bueste
    b = nah(name, cx, unten + 150, max_h)
    els.append(b)
    if blase_:
        sb = 1 if cx < 540 else -1
        bw = max(320, int(F("Bold", 38).getlength(blase_) / 0.74) + 40)
        bx = min(max(cx + sb * (150 + bw / 2), 48 + bw / 2), 1032 - bw / 2)
        els.append(bl("sprech", bw, 150, bx, unten + 100, blase_, kopfpunkt(b, sb), 38))


# ---------------------------------------------------------------- Text- und Kartenbausteine
def unterkante(els):
    return max(e.y + e.sprite.height for e in els)


def karte_um(inhalt, y=128, pad=44, fill=WEISS):
    h = unterkante(inhalt) - y + pad
    return [karte(48, y, 984, h, C, fill=fill)] + inhalt, y + h


def passt(text, stil, size, breite, minimum=28):
    """Schriftgröße, bei der text in breite passt (für einzeilige Blöcke)."""
    while F(stil, size).getlength(text) > breite and size > minimum: size -= 2
    return size


def zeichen(z, x, y):
    if z == "ok": return haken_i(x, y, C, gr=22)
    if z == "nein": return kreuz_i(x, y, C, gr=22)
    if z == "warn": return warnung_i(x, y, C, gr=19)
    return None


def schlagzeile(zeilen, y, groesse=170, abstand=1.1, klausur=1, x0=X0, x1=X1, marker=None):
    s = groesse
    while max(F("ExtraBold", s).getlength(z) for z in zeilen) + 40 > x1 - x0: s -= 2
    els = [titel(z, x0 - 16, y + i * int(s * abstand), C, s, marker=marker or PASTELL[klausur]) for i, z in enumerate(zeilen)]
    return els, y + len(zeilen) * int(s * abstand)


def titel_passend(text, x, y, size, rechts=1000, **kw):
    """Folientitel in der vorgesehenen Größe, aber nie über den rechten Kartenrand (x 1000) hinaus."""
    s = size
    while F("ExtraBold", s).getlength(text) + 40 > rechts - x and s > 40: s -= 2
    return titel(text, x, y, C, s, **kw)


def norm_titel(text, y, groesse=76):
    """Cover N3: Norm als dritte Schlagzeilenzeile mit lila Marker."""
    s = groesse
    while F("ExtraBold", s).getlength(text) + 40 > X1 - X0: s -= 2
    return titel(text, X0 - 16, y + 10, C, s, marker=LILA), y + 30 + int(s * 1.25)


def kalenderblatt(cx, oben, w, monat, tag, unter):
    """Abreißkalender: roter Kopf mit Monat, große Zahl, Zeile darunter."""
    k = 2; h = int(w * 1.08)
    im = Image.new("RGBA", ((w + 30) * k, (h + 30) * k)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((14 * k, 14 * k, (w + 14) * k, (h + 14) * k), 30 * k, fill=INK)
    d.rounded_rectangle((0, 0, w * k, h * k), 30 * k, fill=INK)
    d.rounded_rectangle((6 * k, 6 * k, (w - 6) * k, (h - 6) * k), 25 * k, fill=WEISS)
    kh = int(h * 0.24)
    d.rounded_rectangle((6 * k, 6 * k, (w - 6) * k, kh * k), 25 * k, fill=ROT)
    d.rectangle((6 * k, (kh - 30) * k, (w - 6) * k, kh * k), fill=ROT)
    d.line((6 * k, kh * k, (w - 6) * k, kh * k), fill=INK, width=6 * k)
    d.text((w / 2 * k, (kh / 2 + 6) * k), monat, font=F("ExtraBold", int(w * 0.15) * k), fill=INK, anchor="mm")
    d.text((w / 2 * k, (kh + (h - kh) * 0.44) * k), tag, font=F("ExtraBold", int(w * 0.5) * k), fill=INK, anchor="mm")
    su = int(w * 0.11)
    while F("Bold", su).getlength(unter) > w - 30 and su > 12: su -= 1
    d.text((w / 2 * k, (h - (h - kh) * 0.13) * k), unter, font=F("Bold", su * k), fill=INK, anchor="mm")
    im = im.resize((im.width // k, im.height // k), Image.LANCZOS)
    return engine.El(im, cx - w / 2, oben, C, "pop", 0.0, name="kalender")


def zahlblock(x, y, w, h, fill, label, zahl, zs=120, ls=48):
    """Block mit Beschriftung oben und großer Zahl darunter – ein Sprite, nichts überlappt."""
    e = fl_block(x, y, w, h, fill, C, [(" ", "Bold", 10, INK)])
    sp = e.sprite.copy()
    while F("ExtraBold", zs).getlength(zahl) > w - 60 and zs > 30: zs -= 2
    for t, stil, size, yy in ((label, "Bold", ls, y + 26), (zahl, "ExtraBold", zs, y + 26 + int(ls * 1.25))):
        o = OT(t, x + w / 2, yy, C, stil, size, anker="m")
        sp.alpha_composite(o.sprite, (int(o.x - e.x), int(o.y - e.y)))
    e.sprite = sp
    return e


MONATE = {"Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"}


def norm_label(t):
    """Absatzlabel kompakt und eindeutig: „§ 6 (1) 3.“ → „§ 6 (1) Nr. 3“, „§ 7 (1) 5“ → „§ 7 (1) S. 5“, „3.“ → „Nr. 3“."""
    t = re.sub(r"Abs\. (\d+[a-z]?)", r"(\1)", t.strip())
    t = re.sub(r"(\(\d+[a-z]?\)) (\d+[a-z]?)\.$", r"\1 Nr. \2", t)
    t = re.sub(r"(\(\d+[a-z]?\)) (\d+)(?=( |$))", r"\1 S. \2", t)
    t = re.sub(r"^(\d+[a-z]?)\.$", r"Nr. \1", t)
    return t


def _nummern(woerter):
    """Aufzählungsnummern im Gesetzestext („1. bei …“) als „Nr. 1“ (fett) darstellen, Datumsangaben bleiben."""
    aus = []
    for i, (w_, mk) in enumerate(woerter):
        vor = woerter[i - 1][0] if i else ""
        nach = woerter[i + 1][0] if i + 1 < len(woerter) else ""
        if (mk != "__nr" and re.fullmatch(r"\d+[a-z]?\.", w_) and nach and nach.rstrip(",.") not in MONATE
                and not re.fullmatch(r"\d.*", nach) and not nach.startswith(("Halbsatz", "Alternative", "Fall", "Var", "Hs")) and vor not in ("Satz", "Absatz", "Nummer", "Nr.", "Abs.", "S.", "am", "vom", "zum", "bis", "ab")):
            aus.append(("Nr.", "__nr")); aus.append((w_[:-1], "__nr"))
        else:
            aus.append((w_, mk))
    return aus


def gesetzesseite(x, y, w, kopf, absaetze_, size=34, kompakt=False):
    """Aufgeschlagene Gesetzesseite mit Markierungen. absaetze_: [[nummer|null, [[text, mark|null], …]], …];
    mark: g/b/r/gr + Index (g1, b1 …). Gibt (El, Markierungspositionen, Höhe) zurück."""
    pad, lh = 54, 1.38
    f, fb = SERIF(size), SERIFB(size)
    zeilen, yy = [], (82 if kompakt else 110)
    for nr, teile in absaetze_:
        woerter = []
        for txt, mk in teile:
            for w_ in txt.split(" "):
                if w_: woerter.append((w_, mk))
        verbunden = []
        for w_, mk in woerter:                      # Satzzeichen am Segmentanfang ohne Leerzeichen anhängen
            if verbunden and w_[:1] in ",;.:)" :
                verbunden[-1] = (verbunden[-1][0] + w_, verbunden[-1][1])
            else:
                verbunden.append((w_, mk))
        woerter = verbunden
        if nr: woerter.insert(0, ((f"({nr})" if isinstance(nr, int) else norm_label(str(nr))), "__nr"))
        woerter = _nummern(woerter)
        cur, cw = [], 0
        for w_, mk in woerter:
            ww = (fb if mk == "__nr" else f).getlength(w_ + " ")
            if cw + ww > w - 2 * pad and cur:
                zeilen.append((yy, cur)); yy += int(size * lh); cur, cw = [], 0
            cur.append((cw, w_, mk)); cw += ww
        zeilen.append((yy, cur)); yy += int(size * lh) + 14
    h = yy + (18 if kompakt else 40)
    im = Image.new("RGBA", (w + 40, h + 40))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((14, 14, w + 14, h + 14), 18, fill=(0, 0, 0, 60))
    d.rounded_rectangle((0, 0, w, h), 18, fill=(253, 251, 244, 255), outline=INK, width=4)
    for i in range(26):
        d.line((4 + i, 6, 4 + i, h - 6), fill=(0, 0, 0, int(55 * (1 - i / 26))))
    if kompakt:
        d.text((pad, 26), kopf, font=SERIFB(27), fill=(60, 60, 60, 255))
        d.line((pad, 64, w - pad, 64), fill=(180, 180, 180, 255), width=2)
    else:
        d.text((pad, 40), kopf, font=SERIFB(31), fill=(60, 60, 60, 255))
        d.line((pad, 86, w - pad, 86), fill=(180, 180, 180, 255), width=2)
    ml = Image.new("RGBA", im.size); md = ImageDraw.Draw(ml)
    pos = {}
    for yy, cur in zeilen:
        for cx, w_, mk in cur:
            if mk and mk != "__nr":
                ww = f.getlength(w_)
                md.rectangle((pad + cx - 4, yy + size * 0.12, pad + cx + ww + 6, yy + size * 1.08), fill=MARK[mk.rstrip("0123456789")])
                pos.setdefault(mk, []).append((pad + cx, yy, pad + cx + ww, yy + size))
    im.alpha_composite(ml)
    for yy, cur in zeilen:
        for cx, w_, mk in cur:
            d.text((pad + cx, yy), w_, font=fb if mk == "__nr" else f, fill=INK)
    return engine.El(im, x, y, C, "fade", 0.0, name="gesetz"), pos, h
