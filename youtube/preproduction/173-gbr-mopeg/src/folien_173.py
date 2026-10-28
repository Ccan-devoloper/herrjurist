"""Folge 173 · GbR nach MoPeG: Rechtsfähig, eingetragen, haftend (§§ 705 ff. BGB) – Serienstandard Open Peeps (Katzenkönig).
Beispielfall: Bente, Gerrit und Ingo gründen per Handschlag eine Band (50 € im Monat in die Bandkasse) und kaufen zu dritt im
Musikgeschäft von Frau Bornemann für die Band eine Anlage für 3.600 € auf Rechnung; die Bandkasse reicht nicht, Frau Bornemann
verlangt alles von Ingo.
Szenen laut ../SZENENPLAN.md: A1 Proberaum, A2 Musikgeschäft, A3 Die Rechnung, B Sachverhalt, C Aufbau, D Wortlautkarte
§ 705 Abs. 1, E1 Wortlautkarte § 705 Abs. 2, E2 Wortlautkarten § 705 Abs. 3 und § 719 Abs. 1, F Wortlautkarten § 707 Abs. 1
und § 47 Abs. 2 GBO, G Wortlautkarte § 713 mit ARGE Weißes Roß, H Wortlautkarte § 720 Abs. 1, I Wortlautkarte § 721,
J Lösung, K Klausurtipp (Lexi), L Prüfschema, M Merksatz (Lexi).
Zwei Handlungsgeräusche (Ladenglocke, als die drei ins Musikgeschäft kommen; Stift, als alle unterschreiben;
../geraeusche_herkunft.json). Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/
wortlaut/redet/fig/ns/okz/neinz als eigene Kopie aus Folge 152 (gemeinsame Dateien unverändert); neu: raum(), regal(),
theke(), laden().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_173/"

# Sprechblasen müssen im Stil C entstehen (kein stiller Rückfall auf Stil e)
_run0 = bausteine._sp.run


def _run_c(args, **k):
    r = _run0(args, **k)
    if len(args) > 1 and str(args[1]).endswith("blase_c.js"):
        assert r.returncode == 0, f"Blase Stil C fehlgeschlagen: {args[2]}"
    return r


bausteine._sp.run = _run_c

FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
ZITAT = (246, 246, 250, 255)
HELLROT = (253, 232, 228, 255)
HELLGRUEN = (232, 247, 233, 255)
HELLGRAU = (226, 226, 222, 255)
HOLZ = (214, 160, 110, 255)
DAUER = bausteine._cj()["dauer"]
T_ = bausteine._t

_CMAP = set(TTFont(SP + "humaaans/fonts/Nunito[wght].ttf").getBestCmap())


def glyphen(text):
    """Nunito muss jedes Zeichen haben (sonst Kästchen)."""
    fehl = {c for c in text if ord(c) not in _CMAP and not c.isspace()}
    assert not fehl, f"Zeichen fehlt in Nunito: {fehl} in {text!r}"
    return text


def z(text, x, y, cue, stil="Regular", size=34, farbe=INK, d=0.0, rechts=1170, **k):
    """Tafelzeile, die rechts nicht über die Karte hinausragen darf (Mindestgröße 26 px, mobile Lesbarkeit)."""
    assert size >= 26, f"Schrift zu klein: {text}"
    e = zeile(glyphen(text), x, y, cue, stil, size, farbe=farbe, d=d, **k)
    assert e.x + e.sprite.width <= rechts, f"Zeile zu breit: {text} ({e.x + e.sprite.width:.0f} > {rechts})"
    return e


def pl(text, *a, **k):
    assert k.get("size", 40) >= 26
    return pille(glyphen(text), *a, **k)


def tafel(cue, titel_, h=840, fill=WEISS, size=46, frei=1170):
    """Rechtstafel links, rechts bleibt Platz für die Figuren."""
    assert 110 + F("ExtraBold", size).getlength(glyphen(titel_)) <= frei, f"Titel zu breit: {titel_}"
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(titel_, 110, 100, cue, size)]


def blk(x, y, w, h, fill, cue, zeilen, **k):
    for t, s, g, f in zeilen:
        assert g >= 26 and F(s, g).getlength(glyphen(t)) <= w - 30, f"Blockzeile zu breit: {t}"
    from engine import block as _block
    return _block(x, y, w, h, fill, None, cue, textsize=max(g for _, _, g, _ in zeilen), rund=k.pop("rund", 18), rand=INK,
                  randbreite=k.pop("rand", 5), anim=k.pop("anim", "rise"), zeilen=zeilen, **k)


def bis_(el, bis):
    el.bis = bis
    return el


def hart(e):
    """Harter Schnitt statt Einblendung."""
    e.anim = "cut"
    return e


def lexi_bis_ende(cue):
    return (cue, round(DAUER - T_(cue) + 0.5, 3))       # Lexi bleibt bis zum letzten Frame


def zit(text, x, y, cue, size=26, **k):
    """Fundstellenzeile (grau, 26 px)."""
    return z(text, x, y, cue, size=size, farbe=TEXT, **k)


def rechts_frei(els, x0=1250):
    """Figuren und Requisiten der Tafelfolien stehen rechts der Tafel."""
    for e in els:
        n = e.name or ""
        if n.startswith(("bild:", "ficon:")) or "/op_173/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def wortlaut(x, y, w, zeilen, quelle, cue, marken=(), size=32, bis=None):
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 04.10.2026, Stand BGB: zuletzt geändert durch Art. 6 G v. 23.7.2026), als Zitat mit Normangabe;
    marken = [(zeile, wort, cue)] legt synchron zum gesprochenen Wort einen Textmarker hinter das Wort."""
    lh = int(size * 1.42)
    hgt = 40 + lh * len(zeilen) + 46
    els = [bis_(karte(x, y, w, hgt, cue, fill=ZITAT, rund=18, schatten=6, rand=4), bis)]
    f = F("Regular", size)
    tx, ty = x + 28, y + 26
    for zi, wort, mc in marken:
        t = zeilen[zi]
        a = t.index(wort)
        x0 = tx + f.getlength(t[:a]) - 4
        x1 = tx + f.getlength(t[:a + len(wort)]) + 4
        y0 = ty + zi * lh + size * 0.30
        im = Image.new("RGBA", (int(x1 - x0) + 2, int(size * 0.85)))
        ImageDraw.Draw(im).rounded_rectangle((0, 0, im.width - 1, im.height - 1), 7, fill=MARKER)
        els.append(El(im, x0, y0, mc, "fade", 0.0, bis, name="marker:" + wort))
    for i, t in enumerate(zeilen):
        els.append(z(t, tx, ty + i * lh, cue, size=size, rechts=x + w - 16, bis=bis))
    els.append(z(quelle, tx, ty + len(zeilen) * lh + 4, cue, "Bold", size - 4, farbe=TEXT, rechts=x + w - 16, bis=bis))
    return els, y + hgt


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 103/109/112/124) -----------------------------
_W = _wave.open("../stimme.wav"); _SR = _W.getframerate()
_X = np.frombuffer(_W.readframes(_W.getnframes()), np.int16).astype(np.float32) / 32768
_W.close()


def _hoerbares_ende(a, b, schwelle=-38.0):
    h = int(0.01 * _SR); seg = _X[int(a * _SR):int(b * _SR)]; n = len(seg) // h
    if n == 0:
        return b
    db = 20 * np.log10(np.sqrt((seg[: n * h].reshape(n, h) ** 2).mean(1)) + 1e-9)
    laut = np.nonzero(db > schwelle)[0]
    return min(b, a + (laut[-1] + 1) * 0.01) if len(laut) else min(b, a + 0.1)


def redet(basis, cx, unten, hoehe, cue, bis, **k):
    """Wie bausteine.redet(), aber Wortende = hörbares Ende; Viseme aus der Schreibung geschätzt."""
    cj = bausteine._cj(); ta, tb = T_(cue), T_(bis)
    els = [peep_voll(basis, cx, unten, hoehe, cue, anim="cut", bis=bis, **k)]
    for s_ in cj["segmente"]:
        for w, (a, b) in zip(s_["text"].split(), s_["woerter"]):
            if a < ta - 0.01 or b > tb + 0.01:
                continue
            b = _hoerbares_ende(a, b)
            folge = bausteine.mundfolge(w)
            dauer = (b - a) * 0.88
            n = max(1, min(len(folge), int(dauer / 0.1)))
            folge = folge[:: max(1, len(folge) // n)][:n]
            for j, v in enumerate(folge):
                s0, s1 = a + dauer * j / n, a + dauer * (j + 1) / n
                els.append(peep_voll(f"{basis}_{v}", cx, unten, hoehe, (cue, round(s0 - ta, 3)), anim="cut",
                                     bis=(cue, round(s1 - ta, 3)), **k))
    return els


def fig(name, cx, unten, hoehe, folge, bis=None, erst="pop", d=0.0):
    """Mimikfolge einer Figur am selben Platz: folge = [(cue, suffix)] → harte Schnitte."""
    els = []
    for i, (c, s) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else bis
        els.append(peep_voll(f"{name}_{s}", cx, unten, hoehe, c, anim=erst if i == 0 else "cut", d=d if i == 0 else 0.0, bis=b))
    return els


def ns(text, cx, unten, cue, fill, **k):
    """Namensschild unter der Figur (ab ihrem ersten Auftritt, solange sie im Bild ist)."""
    return pl(text, cx, unten + 22, cue, fill=fill, size=30, anker="m", **k)


def okz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Haken davor (zur gesprochenen Bejahung)."""
    return [ok(x - 45, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]


def neinz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Kreuz davor (zur gesprochenen Verneinung)."""
    return [nein(x - 45, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]





# --- eigene Szenenbausteine (programmatisch, Palettenflächen, Tuschekontur) ---------------------------------------------------
WAND_PROBE = (236, 230, 246, 255)
WAND_LADEN = (250, 238, 214, 255)
BODEN_F = (168, 120, 80, 255)
BODEN_Y = 905                                # Boden = Unterkante der Figuren
FHA = 480                                    # Figurenhöhe in den Fallszenen
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
HELLROT = (253, 232, 228, 255)


def raum(c, fill):
    """Raum (Grundform): Wandfläche mit Tuschekontur und Bodenstreifen; harter Schnitt."""
    s = 2
    x0, y0, w, h = 80, 380, 1760, BODEN_Y - 380
    im = Image.new("RGBA", (w * s, (h + 40) * s))
    dr = ImageDraw.Draw(im)
    dr.rounded_rectangle((3 * s, 3 * s, (w - 3) * s, h * s), 22 * s, fill=fill, outline=INK, width=6 * s)
    dr.rectangle((0, h * s, w * s, (h + 36) * s), fill=BODEN_F)
    dr.line((0, h * s, w * s, h * s), fill=INK, width=5 * s)
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    return hart(El(im, x0, y0, c, "cut", 0.0, None, name="raum"))


def teppich(c, x, w):
    s = 2
    im = Image.new("RGBA", (w * s, 34 * s))
    ImageDraw.Draw(im).ellipse((2 * s, 2 * s, (w - 2) * s, 32 * s), fill=ROT, outline=INK, width=4 * s)
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    return hart(El(im, x, BODEN_Y - 18, c, "cut", 0.0, None, name="teppich"))


def regal(c):
    """Wandregal im Musikgeschäft (Grundform) mit Instrumenten aus Phosphor/Fluent (Palettenfüllung)."""
    s = 2
    im = Image.new("RGBA", (860 * s, 20 * s))
    ImageDraw.Draw(im).rounded_rectangle((2 * s, 2 * s, 858 * s, 18 * s), 5 * s, fill=HOLZ, outline=INK, width=4 * s)
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    els = [hart(El(im, 110, 560, c, "cut", 0.0, None, name="regal"))]
    for cx, st, ic, fu, br in ((170, "ph", "guitar", ROT, 100), (290, "ph", "headphones", BLAU, 90),
                               (400, "ph", "piano-keys", GELB, 90),
                               (770, "ph", "microphone-stage", LILA, 80), (890, "ph", "guitar", GRUEN, 100)):
        els.append(hart(ficon(st, ic, cx, 562, br, c, fuell=fu, anim="cut")))
    return els


THEKE = (250, 700, 610)                      # Ladentheke: links, oben, Breite


def theke(c):
    s = 2
    x, y, w = THEKE
    im = Image.new("RGBA", (w * s, (BODEN_Y - y + 4) * s))
    dr = ImageDraw.Draw(im)
    dr.rounded_rectangle((3 * s, 3 * s, (w - 3) * s, (BODEN_Y - y) * s), 10 * s, fill=HOLZ, outline=INK, width=5 * s)
    dr.line((3 * s, 34 * s, (w - 3) * s, 34 * s), fill=INK, width=4 * s)
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    return hart(El(im, x, y, c, "cut", 0.0, None, name="theke"))


NAME = {"BT": "Bente", "GE": "Gerrit", "IN": "Ingo", "BO": "Frau Bornemann"}
NFARBE = {"BT": LILA, "GE": GRUEN, "IN": BLAU, "BO": GELB}


def stehend(k, x, folge, unten=930, hoehe=480):
    return [*fig(k, x, unten, hoehe, folge), ns(NAME[k], x, unten, folge[0][0], NFARBE[k], d=0.1)]


X1, X2 = 1430, 1730                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante


def requisit(folge, px=PX):
    """Wechselndes Requisit über den Figuren: folge = [(cue, (set, icon, breite, fuell), pillentext, pillenfarbe)]."""
    els = []
    for i, (c, ic, txt, pf) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else None
        if ic:
            s_, n_, br, fu = ic
            els.append(ficon(s_, n_, px, PU, br, c, fuell=fu, bis=b))
        if txt:
            els.append(pl(txt, px, PY, c, fill=pf, size=28, anker="m", bis=b))
    return els


def zwei(k1, f1, k2, f2):
    """Zwei Figuren rechts neben der Tafel (blicken nach links zur Tafel)."""
    return [*stehend(k1, X1, f1), *stehend(k2, X2, f2)]


def allein(k, folge):
    return stehend(k, FX, folge)


# ===========================================================================================================================
# A1 Fall: im Proberaum
# ===========================================================================================================================
BX, GX, IX = 760, 1130, 1500                 # Bente (blickt nach rechts), Gerrit und Ingo (blicken nach links)
folie([(NULL, "Fall · Die Band"), ("b1", "Fall · Abgemacht?")], [
    raum(NULL, WAND_PROBE),
    teppich(NULL, 1180, 280),
    hart(pl("Seit der Schulzeit zusammen Musik", 70, 30, NULL, fill=GELB, size=38)),
    *fig("BT", BX, BODEN_Y, FHA, [(NULL, "froh_r")], bis="b1"),
    *fig("GE", GX, BODEN_Y, FHA, [(NULL, "ruhig")], bis="g1"),
    *fig("IN", IX, BODEN_Y, FHA, [(NULL, "ruhig"), (beim("g1", "Abgemacht"), "froh")]),
    hart(ns("Bente", BX, BODEN_Y, NULL, LILA)), hart(ns("Gerrit", GX, BODEN_Y, NULL, GRUEN)),
    hart(ns("Ingo", IX, BODEN_Y, NULL, BLAU)),
    pl("Gitarre · Schlagzeug · Bass", 70, 110, "proben", fill=WEISS, size=34),
    ficon("ph", "guitar", 560, BODEN_Y, 120, beim("proben", "Gitarre"), fuell=ROT),
    ficon("fluent-emoji-high-contrast", "long-drum", 1315, BODEN_Y - 4, 110, beim("proben", "Schlagzeug"), fuell=GELB),
    ficon("ph", "guitar", 1700, BODEN_Y, 120, beim("proben", "Bass"), fuell=BLAU, spiegeln=True),
    # Figurenrede
    *redet("BT_redet_r", BX, BODEN_Y, FHA, "b1", "g1"),
    blase("sprech", 600, 210, "b1", 1010, 250, inhalt=["Ab heute sind wir", "eine echte Band. Abgemacht?"], textsize=36,
          figur=("BT_redet_r", BX, BODEN_Y, FHA), bis="g1"),
    *fig("BT", BX, BODEN_Y, FHA, [("g1", "froh_r")], erst="cut"),
    *redet("GE_redet", GX, BODEN_Y, FHA, "g1", "laden"),
    blase("sprech", 660, 230, "g1", 1290, 250, inhalt=["Abgemacht! Jeder zahlt 50 €", "im Monat in die Bandkasse."],
          textsize=36, figur=("GE_redet", GX, BODEN_Y, FHA)),
    ficon("ph", "handshake", 945, 660, 110, beim("g1", "Abgemacht"), fuell=GELB),
    ficon("ph", "piggy-bank", 1315, 770, 100, beim("g1", "Bandkasse"), fuell=PINK),
])

# ===========================================================================================================================
# A2 Fall: im Musikgeschäft
# ===========================================================================================================================
KO, KG, KI, KB = 1080, 1380, 1680, 560       # Bente, Gerrit, Ingo (blicken nach links), Frau Bornemann (blickt nach rechts)
G_LOS, G_DA = "laden", beim("laden", "Musikgeschäft", ende=True)


def laden(c):
    return [raum(c, WAND_LADEN), *regal(c)]


def kommt(k, x, c0, bis, glocke=False):
    """Figur kommt mit den anderen 120 px von rechts ins Geschäft (Grundbild bis 'bis')."""
    e = bewegt(peep_voll(k, x, BODEN_Y, FHA, "laden", anim="pop", bis=bis), G_LOS, G_DA, 120, 0)
    n = bewegt(ns(NAME[k[:2]], x, BODEN_Y, "laden", NFARBE[k[:2]], d=0.1), G_LOS, G_DA, 120, 0)
    return [szene(e, "173glocke*", 1.0, 0.0) if glocke else e, n]


BO_hinten = [   # Frau Bornemann hinter der Theke (alle ihre Bilder vor der Theke in die Liste, damit die Theke sie verdeckt)
    *fig("BO", KB, BODEN_Y, FHA, [(beim("bor", "Inhaberin"), "froh_r")], bis="fb1"),
    *redet("BO_redet_r", KB, BODEN_Y, FHA, "fb1", "b2"),
    *fig("BO", KB, BODEN_Y, FHA, [("b2", "froh_r"), ("liefer", "ruhig_r")], erst="cut"),
]
folie([("laden", "Fall · Im Musikgeschäft"), ("fb1", "Fall · Auf wen die Rechnung?"), ("unter", "Fall · Der Kaufvertrag")], [
    *laden("laden"),
    *BO_hinten,
    theke("laden"),
    ns("Frau Bornemann", KB, BODEN_Y, beim("bor", "Inhaberin"), GELB, d=0.1),
    pl("Im Musikgeschäft", 70, 30, "laden", fill=GELB, size=38),
    pl("Inhaberin: Frau Bornemann", 70, 110, beim("bor", "Inhaberin"), fill=WEISS, size=34, bis="unter"),
    ficon("ph", "speaker-hifi", 330, 702, 120, beim("bor", "Anlage"), fuell=LILA),
    ficon("ph", "speaker-hifi", 790, 702, 120, beim("bor", "Anlage"), fuell=LILA),
    pl("Anlage: 3.600 €", 70, 190, beim("bor", "dreitausendsechshundert"), fill=GELB, size=34, bis="unter"),
    # die drei kommen ins Geschäft (Ladenglocke)
    *kommt("BT_froh", KO, "laden", "b2", glocke=True),
    *redet("BT_redet", KO, BODEN_Y, FHA, "b2", "unter"),
    *fig("BT", KO, BODEN_Y, FHA, [("unter", "ruhig"), ("liefer", "froh")], erst="cut"),
    *kommt("GE_staunt", KG, "laden", "fb1"),
    *fig("GE", KG, BODEN_Y, FHA, [("fb1", "ruhig"), ("unter", "froh")], erst="cut"),
    *kommt("IN_ruhig", KI, "laden", "unter"),
    *fig("IN", KI, BODEN_Y, FHA, [("unter", "froh")], erst="cut"),
    # Figurenrede
    blase("sprech", 560, 200, "fb1", 900, 280, inhalt=["Auf wen schreibe ich", "die Rechnung?"], textsize=38,
          figur=("BO_redet_r", KB, BODEN_Y, FHA), bis="b2"),
    blase("sprech", 600, 210, "b2", 1230, 270, inhalt=["Auf unsere Band.", "Wir kaufen sie zusammen."], textsize=38,
          figur=("BT_redet", KO, BODEN_Y, FHA), bis="unter"),
    # Kaufvertrag: alle drei unterschreiben für die Band (Stift)
    szene(ficon("tabler", "contract", 700, 700, 90, "unter", fuell=WEISS), "173stift*", 1.0, 0.25),
    ficon("tabler", "writing-sign", 860, 640, 70, beim("unter", "unterschreiben"), fuell=WEISS),
    pl("Alle 3 unterschreiben für die Band", 70, 110, beim("unter", "unterschreiben"), fill=GRUEN, size=34),
    pl("Rechnung: 3.600 €, fällig in 14 Tagen", 70, 190, beim("liefer", "Rechnung"), fill=WEISS, size=34),
    ficon("tabler", "receipt-euro", 800, 266, 70, beim("liefer", "Rechnung"), fuell=WEISS),
    ficon("tabler", "truck-delivery", 910, 268, 90, beim("liefer", "geliefert"), fuell=GELB),
])

# ===========================================================================================================================
# A3 Fall: die Rechnung
# ===========================================================================================================================
KI3 = 1120                                    # Ingo vor der Theke (blickt nach links zu Frau Bornemann)
folie([("spaet", "Fall · Die Rechnung"), ("fb2", "Fall · Ingo soll zahlen"), ("frage", "Fall · Die Frage")], [
    *laden("spaet"),
    *fig("BO", KB, BODEN_Y, FHA, [("spaet", "skeptisch_r")], bis="fb2"),
    *redet("BO_streng_r", KB, BODEN_Y, FHA, "fb2", "i1"),
    *fig("BO", KB, BODEN_Y, FHA, [("i1", "skeptisch_r"), ("frage", "ruhig_r")], erst="cut"),
    theke("spaet"),
    hart(ns("Frau Bornemann", KB, BODEN_Y, "spaet", GELB)),
    ficon("tabler", "receipt-euro", 700, 700, 80, "spaet", fuell=WEISS),
    pl("Rechnung: 3.600 €", 70, 30, "spaet", fill=WEISS, size=38),
    pl("Die Bandkasse reicht nicht", 70, 110, beim("spaet", "Bandkasse"), fill=HELLROT, size=34, bis="frage"),
    ficon("ph", "piggy-bank", 1500, 900, 110, beim("spaet", "Bandkasse"), fuell=HELLROT),
    *fig("IN", KI3, BODEN_Y, FHA, [("ingo", "ruhig")], bis="fb2"),
    ns("Ingo", KI3, BODEN_Y, "ingo", BLAU, d=0.1),
    *fig("IN", KI3, BODEN_Y, FHA, [("fb2", "schreck")], erst="cut", bis="i1"),
    *redet("IN_redet", KI3, BODEN_Y, FHA, "i1", "frage"),
    *fig("IN", KI3, BODEN_Y, FHA, [("frage", "sorge")], erst="cut"),
    blase("sprech", 560, 200, "fb2", 880, 270, inhalt=["Bitte zahlen Sie", "die 3.600 €."], textsize=40,
          figur=("BO_streng_r", KB, BODEN_Y, FHA), bis="i1"),
    blase("sprech", 640, 220, "i1", 1290, 270, inhalt=["Ich allein? Die Anlage hat", "doch die Band gekauft!"], textsize=36,
          figur=("IN_redet", KI3, BODEN_Y, FHA), bis="frage"),
    pl("Wer ist hier Vertragspartner?", 70, 190, "frage", fill=PINK, size=36),
    pl("Muss Ingo wirklich die ganze Summe zahlen?", 70, 270, "frage2", fill=PINK, size=36),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_173(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=33, zeilenabstand=1.28)
        els += e; y += 16
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_173("sv", [
    "Bente, Gerrit und Ingo machen seit der Schulzeit in ihrer Freizeit zusammen Musik. Per Handschlag vereinbaren sie, "
    "von nun an eine Band zu sein, gemeinsam zu proben und aufzutreten; jeder zahlt 50 € im Monat in die Bandkasse. "
    "Ins Gesellschaftsregister lassen sie sich nicht eintragen.",
    "Zu dritt kaufen sie im Musikgeschäft von Frau Bornemann eine Musikanlage für 3.600 €. Auf die Frage, auf wen die "
    "Rechnung lauten soll, antwortet Bente: „Auf unsere Band. Wir kaufen sie zusammen.“ Alle drei unterschreiben den "
    "Kaufvertrag für die Band. Frau Bornemann liefert und übereignet die Anlage; die Rechnung ist in 14 Tagen fällig.",
    "Die Bandkasse reicht nicht. Frau Bornemann verlangt die 3.600 € von Ingo, der als Einziger ein festes Gehalt hat. "
    "Ingo meint, die Anlage habe doch die Band gekauft.",
], "Wer ist Vertragspartner, und muss Ingo die ganze Summe zahlen?")

# ===========================================================================================================================
# C Aufbau
# ===========================================================================================================================
folie([("aufbau", "Aufbau · MoPeG seit 1.1.2024"), ("a1", "Aufbau · drei Schritte"),
       ("a2", "Aufbau › 1. Rechtsfähige GbR?"), ("a3", "Aufbau › 2. Wirksam vertreten?"),
       ("a4", "Aufbau › 3. Persönliche Haftung?")], rechts_frei([
    *tafel("aufbau", "Der Aufbau"),
    z("MoPeG: neues Recht der GbR seit 1.1.2024", 110, 180, "aufbau", "Bold", 36),
    zit("§§ 705 ff. BGB n. F.; BGBl. 2021 I S. 3436", 110, 232, beim("aufbau", "Mopeg")),
    z("GbR = Gesellschaft bürgerlichen Rechts", 110, 280, beim("aufbau", "kurz"), size=32),
    z("Wir prüfen in drei Schritten:", 110, 350, "a1", "Bold", 36),
    blk(110, 420, 1040, 80, GELB, "a2", [("1. Ist die Band eine rechtsfähige GbR?", "ExtraBold", 36, INK)]),
    blk(110, 530, 1040, 80, BLAU, "a3", [("2. Wurde sie wirksam vertreten?", "ExtraBold", 36, INK)]),
    blk(110, 640, 1040, 80, HELLROT, "a4", [("3. Haften die Bandmitglieder persönlich?", "ExtraBold", 36, INK)]),
    *requisit([("aufbau", ("tabler", "book", 100, WEISS), "§§ 705 ff. BGB", GELB),
               ("a2", ("ph", "users-three", 110, LILA), "rechtsfähig?", GELB),
               ("a3", ("tabler", "contract", 100, WEISS), "vertreten?", BLAU),
               ("a4", ("ph", "wallet", 100, HELLROT), "persönlich?", HELLROT)]),
    *zwei("BT", [("aufbau", "ruhig"), ("a4", "skeptisch")], "GE", [("aufbau", "ruhig"), ("a3", "skeptisch")]),
]))

# ===========================================================================================================================
# D Wortlautkarte § 705 Abs. 1: Entstehung
# ===========================================================================================================================
PA = "Rechtsfähige GbR"
W1 = ["„Die Gesellschaft wird durch den Abschluss des",
      "Gesellschaftsvertrags errichtet, in dem sich die",
      "Gesellschafter verpflichten, die Erreichung eines",
      "gemeinsamen Zwecks in der durch den Vertrag",
      "bestimmten Weise zu fördern.“"]
w1, w1_y = wortlaut(80, 170, 1100, W1, "§ 705 Abs. 1 BGB", "p1", marken=[
    (1, "Gesellschaftsvertrags", beim("p1", "Gesellschaftsvertrag")), (2, "verpflichten", beim("p1", "verpflichten")),
    (3, "gemeinsamen Zwecks", beim("p1", "gemeinsamen")), (4, "zu fördern", beim("p1", "fördern"))], size=32)
folie([("p1", f"{PA} › Entstehung, § 705 Abs. 1 BGB"), ("form", f"{PA} › Gesellschaftsvertrag: formfrei"),
       ("zweck", f"{PA} › gemeinsamer Zweck"), ("foerd", f"{PA} › Förderung"), ("p1fall", f"{PA} › GbR gegründet (+)")],
      rechts_frei([
    *tafel("p1", "Entstehung: § 705 Abs. 1 BGB"),
    *w1,
    *okz("Vertrag: keine besondere Form, Handschlag genügt", w1_y + 25, "form", "Bold", 32, x=160),
    zit("grundsätzlich formfrei: BT-Drs. 19/27635, S. 104 f.", 160, w1_y + 72, "form"),
    *okz("Zweck: zusammen Musik machen", w1_y + 125, "zweck", "Bold", 32, x=160),
    *okz("Förderung: Proben und 50 € im Monat", w1_y + 185, "foerd", "Bold", 32, x=160),
    blk(110, w1_y + 255, 1040, 80, GRUEN, "p1fall", [("Die drei haben eine GbR gegründet (+)", "ExtraBold", 36, INK)]),
    *requisit([("p1", ("tabler", "book", 100, WEISS), "§ 705 Abs. 1 BGB", GELB),
               ("form", ("ph", "handshake", 110, GELB), "per Handschlag", GELB),
               ("zweck", ("ph", "music-notes", 100, LILA), "zusammen Musik", LILA),
               ("foerd", ("ph", "piggy-bank", 100, PINK), "50 € im Monat", PINK),
               ("p1fall", ("ph", "users-three", 110, GRUEN), "GbR", GRUEN)]),
    *zwei("IN", [("p1", "ruhig"), ("p1fall", "froh")], "BT", [("p1", "ruhig"), ("form", "froh")]),
]))

# ===========================================================================================================================
# E1 Wortlautkarte § 705 Abs. 2: rechtsfähig oder nicht rechtsfähig
# ===========================================================================================================================
W2 = ["„Die Gesellschaft kann entweder selbst Rechte erwerben",
      "und Verbindlichkeiten eingehen, wenn sie nach dem",
      "gemeinsamen Willen der Gesellschafter am Rechtsverkehr",
      "teilnehmen soll (rechtsfähige Gesellschaft), oder sie",
      "kann den Gesellschaftern zur Ausgestaltung ihres",
      "Rechtsverhältnisses untereinander dienen (nicht",
      "rechtsfähige Gesellschaft).“"]
w2, w2_y = wortlaut(80, 165, 1100, W2, "§ 705 Abs. 2 BGB", "p2", marken=[
    (0, "selbst Rechte erwerben", beim("p2a", "selbst")), (1, "Verbindlichkeiten eingehen", beim("p2a", "Verbindlichkeiten")),
    (2, "gemeinsamen Willen", beim("p2a", "gemeinsamen")), (2, "am Rechtsverkehr", beim("p2a", "Rechtsverkehr")),
    (3, "teilnehmen soll", beim("p2a", "teilnehmen")), (5, "untereinander dienen", beim("innen", "untereinander"))], size=31)
folie([("p2", f"{PA} › rechtsfähig? § 705 Abs. 2 BGB"), ("p2a", f"{PA} › Wille: Teilnahme am Rechtsverkehr"),
       ("innen", f"{PA} › sonst: nicht rechtsfähig")], rechts_frei([
    *tafel("p2", "Rechtsfähig? § 705 Abs. 2 BGB"),
    *w2,
    blk(110, w2_y + 30, 505, 120, GRUEN, beim("p2a", "teilnehmen"), [("rechtsfähig:", "ExtraBold", 32, INK),
                                                                      ("tritt nach außen auf", "Regular", 30, INK)]),
    blk(645, w2_y + 30, 505, 120, HELLGRAU, "innen", [("nicht rechtsfähig:", "ExtraBold", 32, INK),
                                                       ("nur untereinander", "Regular", 30, INK)]),
    *requisit([("p2", ("ph", "users-three", 110, GRUEN), "rechtsfähig?", WEISS),
               (beim("p2a", "Rechtsverkehr"), ("tabler", "building-store", 110, GELB), "am Rechtsverkehr", GRUEN),
               ("innen", ("ph", "lock", 90, HELLGRAU), "nur intern", HELLGRAU)]),
    *zwei("GE", [("p2", "skeptisch"), (beim("p2a", "teilnehmen"), "froh")], "IN", [("p2", "ruhig"), ("innen", "skeptisch")]),
]))
assert w2_y + 150 <= 900, w2_y

# ===========================================================================================================================
# E2 Wortlautkarten § 705 Abs. 3 und § 719 Abs. 1
# ===========================================================================================================================
W3 = ["„Ist der Gegenstand der Gesellschaft der Betrieb eines",
      "Unternehmens unter gemeinschaftlichem Namen, so wird",
      "vermutet, dass die Gesellschaft nach dem gemeinsamen",
      "Willen der Gesellschafter am Rechtsverkehr teilnimmt.“"]
w3, w3_y = wortlaut(80, 165, 1100, W3, "§ 705 Abs. 3 BGB", "p3", marken=[
    (1, "Unternehmens", beim("p3", "Unternehmen")), (1, "gemeinschaftlichem Namen", beim("p3", "gemeinsamem")),
    (2, "vermutet", beim("p3", "vermutet"))], size=30)
W719 = ["„Im Verhältnis zu Dritten entsteht die Gesellschaft,",
        "sobald sie mit Zustimmung sämtlicher Gesellschafter am",
        "Rechtsverkehr teilnimmt, spätestens aber mit ihrer",
        "Eintragung im Gesellschaftsregister.“"]
w719, w719_y = wortlaut(80, w3_y + 92, 1100, W719, "§ 719 Abs. 1 BGB", "p719", marken=[
    (0, "Dritten", beim("p719", "Dritten")), (1, "Zustimmung sämtlicher", beim("p719", "Zustimmung")),
    (2, "Rechtsverkehr teilnimmt", beim("p719", "Rechtsverkehr"))], size=30)
folie([("p3", f"{PA} › Vermutung, § 705 Abs. 3 BGB"), ("p2fall", f"{PA} › Band will einkaufen (+)"),
       ("p719", f"{PA} › entstanden mit dem Kauf, § 719 Abs. 1 BGB")], rechts_frei([
    *tafel("p3", "Vermutung und Entstehung"),
    *w3,
    *okz("Hier unnötig: alle wollen als Band einkaufen", w3_y + 18, "p2fall", "Bold", 32, x=160),
    *w719,
    *okz("Hier: entstanden mit dem gemeinsamen Kauf", w719_y + 18, beim("p719", "Kauf"), "Bold", 32, x=160),
    *requisit([("p3", ("tabler", "building-store", 110, WEISS), "Unternehmen?", WEISS),
               ("p2fall", ("ph", "speaker-hifi", 110, LILA), "Kauf als Band", GRUEN),
               ("p719", ("tabler", "contract", 100, WEISS), "gegenüber Dritten", WEISS)]),
    *zwei("BT", [("p3", "skeptisch"), ("p2fall", "froh")], "GE", [("p3", "ruhig"), ("p719", "froh")]),
]))
assert w719_y + 75 <= 900, w719_y

# ===========================================================================================================================
# F Wortlautkarten § 707 Abs. 1 und § 47 Abs. 2 GBO: Eintragung
# ===========================================================================================================================
W707 = ["„Die Gesellschafter können die Gesellschaft bei dem",
        "Gericht, in dessen Bezirk sie ihren Sitz hat, zur",
        "Eintragung in das Gesellschaftsregister anmelden.“"]
w707, w707_y = wortlaut(80, 165, 1100, W707, "§ 707 Abs. 1 BGB", "eintr", marken=[
    (0, "können", beim("p707", "können")), (2, "Gesellschaftsregister", beim("p707", "Gesellschaftsregister"))], size=31)
W47 = ["„Für eine Gesellschaft bürgerlichen Rechts soll ein Recht",
       "nur eingetragen werden, wenn sie im Gesellschaftsregister",
       "eingetragen ist.“"]
w47, w47_y = wortlaut(80, w707_y + 175, 1100, W47, "§ 47 Abs. 2 GBO", "gbo", marken=[
    (0, "soll ein Recht", beim("gbo", "soll")), (1, "im Gesellschaftsregister", beim("gbo", "Gesellschaftsregister", nr=1))],
    size=30)
folie([("eintr", f"{PA} › Eintragung? § 707 Abs. 1 BGB"), ("kann", f"{PA} › Eintragung freiwillig"),
       ("egbr", f"{PA} › Namenszusatz „eGbR“, § 707a Abs. 2 BGB"), ("gbo", f"{PA} › Grundbuch, § 47 Abs. 2 GBO")],
      rechts_frei([
    *tafel("eintr", "Eintragung: § 707 Abs. 1 BGB"),
    *w707,
    *okz("Kann, muss nicht: rechtsfähig auch ohne Eintragung", w707_y + 18, beim("kann", "Rechtsfähigkeit"), "Bold", 32, x=160),
    zit("BT-Drs. 19/27635, S. 128", 160, w707_y + 64, beim("kann", "Rechtsfähigkeit")),
    z("Eingetragen: Zusatz „eGbR“ (§ 707a Abs. 2 S. 1 BGB)", 110, w707_y + 120, "egbr", "Bold", 32),
    *w47,
    blk(110, w47_y + 22, 1040, 76, GELB, "haus", [("Grundstück kaufen? Erst eintragen lassen", "ExtraBold", 34, INK)]),
    *requisit([("eintr", ("tabler", "license", 100, WEISS), "Gesellschaftsregister?", WEISS),
               ("kann", ("ph", "users-three", 110, GRUEN), "freiwillig", GRUEN),
               ("egbr", ("tabler", "id-badge-2", 100, WEISS), "eGbR", GELB),
               ("gbo", ("tabler", "book-2", 100, BLAU), "Grundbuch", BLAU),
               ("haus", ("ph", "house", 110, GELB), "erst eintragen", GELB)]),
    *zwei("IN", [("eintr", "skeptisch"), ("kann", "froh"), ("gbo", "ernst")], "GE", [("eintr", "ruhig"), ("haus", "staunt")]),
]))
assert w47_y + 100 <= 900, w47_y

# ===========================================================================================================================
# G Wortlautkarte § 713: Vermögen der Gesellschaft; ARGE Weißes Roß
# ===========================================================================================================================
W713 = ["„Die Beiträge der Gesellschafter sowie die für oder durch",
        "die Gesellschaft erworbenen Rechte und die gegen sie",
        "begründeten Verbindlichkeiten sind Vermögen der",
        "Gesellschaft.“"]
w713, w713_y = wortlaut(80, 165, 1100, W713, "§ 713 BGB", "verm", marken=[
    (0, "Die Beiträge", beim("p713", "Beiträge")), (1, "erworbenen Rechte", beim("p713", "erworbenen")),
    (2, "begründeten Verbindlichkeiten", beim("p713", "Verbindlichkeiten")), (2, "Vermögen der", beim("p713", "Vermögen")),
    (3, "Gesellschaft", beim("p713", "Vermögen"))], size=31)
GY0 = w713_y + 150
folie([("verm", "Vermögen, § 713 BGB"), ("anl2", "Vermögen › gehört der GbR"), ("schuld", "Vermögen › auch die Schuld"),
       ("arge", "Vermögen › BGH 2001: ARGE Weißes Roß"), ("mopeg", "Vermögen › Gesamthand aufgegeben")], rechts_frei([
    *tafel("verm", "Wem gehört die Anlage? § 713 BGB"),
    *w713,
    *okz("Anlage und Bandkasse: Vermögen der GbR", w713_y + 18, "anl2", "Bold", 32, x=160),
    *okz("Kaufpreisschuld: Verbindlichkeit der GbR", w713_y + 76, "schuld", "Bold", 32, x=160),
    karte(100, GY0, 1060, 230, "arge", fill=HELL, rund=18, schatten=6, rand=4),
    z("BGH, Urt. v. 29.1.2001 – II ZR 331/00, BGHZ 146, 341", 130, GY0 + 20, "arge", "Bold", 30),
    z("„ARGE Weißes Roß“: rechtsfähig, soweit sie", 130, GY0 + 66, beim("arge", "Außengesellschaft"), size=30),
    z("am Rechtsverkehr teilnimmt (Leitsatz a)", 130, GY0 + 106, beim("arge", "Außengesellschaft"), size=30),
    z("MoPeG: Gesamthand aufgegeben", 130, GY0 + 158, "mopeg", "ExtraBold", 32),
    zit("BT-Drs. 19/27635, S. 148", 700, GY0 + 164, "mopeg", rechts=1150),
    *requisit([("verm", ("ph", "speaker-hifi", 110, LILA), "Wem gehört die Anlage?", WEISS),
               ("anl2", ("ph", "speaker-hifi", 110, LILA), "gehört der GbR", GRUEN),
               ("schuld", ("tabler", "receipt-euro", 90, WEISS), "Schuld der GbR", HELLROT),
               ("arge", ("tabler", "building-bank", 110, BLAU), "BGH 2001", BLAU),
               ("mopeg", ("tabler", "book", 100, WEISS), "MoPeG 2024", GELB)]),
    *zwei("GE", [("verm", "skeptisch"), ("anl2", "froh")], "IN", [("verm", "ruhig"), ("schuld", "ernst")]),
]))
assert GY0 + 240 <= 900, GY0

# ===========================================================================================================================
# H Wortlautkarte § 720 Abs. 1: Vertretung; § 715 Geschäftsführung
# ===========================================================================================================================
PV = "Vertretung"
W720 = ["„Zur Vertretung der Gesellschaft sind alle Gesellschafter",
        "gemeinsam befugt, es sei denn, der Gesellschaftsvertrag",
        "bestimmt etwas anderes.“"]
w720, w720_y = wortlaut(80, 165, 1100, W720, "§ 720 Abs. 1 BGB", "p720", marken=[
    (0, "alle Gesellschafter", beim("p720", "alle")), (1, "gemeinsam befugt", beim("p720", "gemeinsam")),
    (1, "es sei denn", beim("p720", "sei"))], size=31)
folie([("vertr", f"2. {PV}: Wer handelt für die Band?"), ("p720", f"{PV} › Gesamtvertretung, § 720 Abs. 1 BGB"),
       ("vfall", f"{PV} › gemeinsam unterschrieben (+)"), ("allein", f"{PV} › allein? Vollmacht"),
       ("gf", f"{PV} › Geschäftsführung, § 715 BGB")], rechts_frei([
    *tafel("vertr", "Vertretung: § 720 Abs. 1 BGB"),
    *w720,
    *okz("Alle 3 haben für die Band unterschrieben", w720_y + 22, "vfall", "Bold", 32, x=160),
    *okz("Die GbR ist wirksam vertreten", w720_y + 80, beim("vfall", "wirksam"), "Bold", 32, x=160),
    z("Bente allein? Einzelvertretungsmacht oder Vollmacht", 110, w720_y + 150, "allein", "Bold", 32),
    zit("Abweichung im Vertrag: § 720 Abs. 1 a. E.; Vollmacht der GbR: BT-Drs. 19/27635, S. 162", 110, w720_y + 196,
        beim("allein", "Vollmacht")),
    blk(110, w720_y + 260, 1040, 120, BLAU, "gf", [("§ 715 BGB: Geschäftsführung", "ExtraBold", 34, INK),
                                                   ("= wer intern entscheiden darf", "Regular", 32, INK)]),
    *requisit([("vertr", ("tabler", "contract", 100, WEISS), "Wer handelt?", WEISS),
               ("vfall", ("tabler", "writing-sign", 100, WEISS), "alle 3 zusammen", GRUEN),
               ("allein", ("tabler", "file-certificate", 100, WEISS), "Vollmacht?", GELB),
               ("gf", ("ph", "users-three", 110, BLAU), "Innenverhältnis", BLAU)]),
    *zwei("BT", [("vertr", "ruhig"), ("vfall", "froh"), ("allein", "skeptisch")], "IN", [("vertr", "ruhig"), ("vfall", "froh")]),
]))
assert w720_y + 390 <= 900, w720_y

# ===========================================================================================================================
# I Wortlautkarte § 721: Haftung; § 721a, § 721b
# ===========================================================================================================================
PH = "Haftung"
W721 = ["„Die Gesellschafter haften für die Verbindlichkeiten der",
        "Gesellschaft den Gläubigern als Gesamtschuldner",
        "persönlich. Eine entgegenstehende Vereinbarung ist",
        "Dritten gegenüber unwirksam.“"]
w721, w721_y = wortlaut(80, 165, 1100, W721, "§ 721 BGB", "p721", marken=[
    (0, "haften", beim("p721", "haften")), (1, "als Gesamtschuldner", beim("p721", "Gesamtschuldner")),
    (2, "persönlich.", beim("p721", "persönlich")), (3, "unwirksam", beim("p721", "unwirksam"))], size=31)
folie([("haft", f"3. {PH}: Und Ingo?"), ("p721", f"{PH} › § 721 BGB"), ("pers", f"{PH} › persönlich: Privatvermögen"),
       ("gesamt", f"{PH} › Gesamtschuldner, § 421 BGB"), ("p721a", f"{PH} › Eintritt, § 721a BGB"),
       ("p721b", f"{PH} › Einwendungen, § 721b BGB")], rechts_frei([
    *tafel("haft", "Haftung: § 721 BGB"),
    *w721,
    blk(110, w721_y + 22, 1040, 76, HELLROT, "pers", [("persönlich = auch mit dem Privatvermögen", "ExtraBold", 34, INK)]),
    z("Gesamtschuldner: jeder die ganze Summe, aber nur einmal", 110, w721_y + 122, "gesamt", "Bold", 32),
    zit("§ 421 BGB · Video „Gesamtschuld“", 110, w721_y + 166, "v120"),
    z("§ 721a: Wer später eintritt, haftet auch für Altschulden", 110, w721_y + 218, "p721a", size=32),
    z("§ 721b: Einwendungen der GbR, z. B. schon bezahlt", 110, w721_y + 272, "p721b", size=32),
    *requisit([("haft", ("ph", "wallet", 100, WEISS), "Ingo zahlen?", WEISS),
               ("pers", ("ph", "wallet", 100, HELLROT), "Privatvermögen", HELLROT),
               ("gesamt", ("tabler", "receipt-euro", 90, WEISS), "3.600 € – nur einmal", GELB),
               ("p721a", ("ph", "user-plus", 100, WEISS), "neu in der Band", WEISS),
               ("p721b", ("tabler", "receipt-euro", 90, GRUEN), "schon bezahlt?", GRUEN)]),
    *allein("IN", [("haft", "sorge"), (beim("p721", "persönlich"), "schreck"), ("gesamt", "muede"), ("p721b", "skeptisch")]),
]))
assert w721_y + 320 <= 900, w721_y

# ===========================================================================================================================
# J Lösung
# ===========================================================================================================================
folie([("loes", "Lösung"), ("l2", "Lösung › Käuferin: die GbR"), ("l4", "Lösung › alle drei haften"),
       ("l6", "Lösung › Rückgriff bei der GbR")], rechts_frei([
    *tafel("loes", "Lösung"),
    *okz("Die Band ist eine rechtsfähige GbR", 180, "l1", "Bold", 34, x=160),
    *okz("Käuferin ist die GbR selbst (gemeinsam vertreten)", 240, "l2", "Bold", 32, x=160),
    z("Anspruch gegen die GbR: 3.600 €, § 433 Abs. 2 BGB", 110, 305, "l3", "Bold", 32),
    *okz("Alle drei haften persönlich, auch Ingo (§ 721)", 370, "l4", "Bold", 32, x=160),
    blk(110, 440, 1040, 120, GELB, "l5", [("Von der GbR und von jedem der drei:", "ExtraBold", 34, INK),
                                          ("alles verlangen – insgesamt nur einmal", "ExtraBold", 34, INK)]),
    z("Ingo zahlt? Rückgriff bei der Gesellschaft", 110, 590, "l6", "Bold", 32),
    zit("BT-Drs. 19/27635, S. 166", 110, 636, "l6"),
    *requisit([("loes", ("tabler", "gavel", 100, HOLZ), "Lösung", WEISS),
               ("l2", ("ph", "users-three", 110, GRUEN), "Käuferin: GbR", GRUEN),
               ("l4", ("ph", "wallet", 100, HELLROT), "persönlich", HELLROT),
               ("l6", ("ph", "piggy-bank", 100, PINK), "Rückgriff", PINK)]),
    *zwei("BT", [("loes", "ruhig"), ("l4", "ernst")], "IN", [("loes", "ruhig"), ("l4", "sorge"), ("l6", "froh")]),
]))

# ===========================================================================================================================
# K Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Anspruch gegen einen Gesellschafter"), ("t4", "Klausurtipp · Anspruchsgrundlage")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Anspruch gegen einen Gesellschafter:", 200, 200, beim("tipp", "Prüfe"), "Bold", 36),
    z("1. Gibt es eine rechtsfähige GbR?", 200, 270, "t1", size=34),
    z("2. Hat sie, wirksam vertreten, eine", 200, 330, "t2", size=34),
    z("Verbindlichkeit begründet?", 236, 378, "t2", size=34),
    z("3. Haftet der Gesellschafter nach § 721?", 200, 438, "t3", size=34),
    linienzug([(130, 515), (1130, 515)], "t4", breite=3),
    z("Anspruchsgrundlage:", 200, 545, "t4", "Bold", 36),
    z("§ 433 Abs. 2 i. V. m. § 721 S. 1 BGB", 200, 605, beim("t4", "Paragraf"), "ExtraBold", 36),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# L Prüfschema
# ===========================================================================================================================
REIHEN = [("s1", 0, "I. Schuld der Gesellschaft", True),
          ("s1a", 1, "1. rechtsfähige GbR: Vertrag und gewollte Teilnahme am Rechtsverkehr, § 705 Abs. 1, 2 BGB", False),
          ("s1b", 1, "2. Vertrag, wirksam vertreten, § 720 BGB", False),
          ("s2", 0, "II. Haftung des Gesellschafters, § 721 BGB", True),
          ("s2a", 1, "1. Gesellschafterstellung", False),
          ("s2b", 1, "2. keine Einwendungen, § 721b BGB", False)]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfschema: Haftung in der GbR"), 110, 90, "sch", 46),
           z("§ 433 Abs. 2 i. V. m. § 721 S. 1 BGB", 110, 160, "sch", "Bold", 32, farbe=TEXT, rechts=1800)]
y = 250
for c, ebene, text, fett in REIHEN:
    x = (130, 200)[ebene]
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 40 if ebene == 0 else 34, rechts=1800))
    y += {0: 84, 1: 72}[ebene]
assert y <= 970, y
folie([("sch", "Prüfschema"), ("s1", "Prüfschema › I. Schuld der Gesellschaft"),
       ("s2", "Prüfschema › II. Haftung des Gesellschafters")], els_sch)

# ===========================================================================================================================
# M Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Die rechtsfähige GbR", 0)], [("kauft und schuldet ", 0), ("selbst", "a"), (".", 0)]], 750, 300, 46,
                "merke", {"a": beim("merke", "selbst")}),
    *markertext([[("Für ihre Schulden haftet", 0)], [("jeder Gesellschafter", 0)],
                 [("persönlich", "b"), (" auf das Ganze.", 0)]], 750, 540, 46, "m2", {"b": beim("m2", "persönlich")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
