"""Folge 160 · Mephisto-Beschluss: Wie viel Wahrheit darf ein Roman enthalten? – Serienstandard Open Peeps (Katzenkönig).
Fiktiver Rahmen: Leseabend in einer Buchhandlung mit Liesel (Autorin), Winfried (ihr früherer Partner, sitzt) und
Frau Hollerbach (Buchhändlerin); danach die echten Fälle sachlich: BVerfGE 30, 173 (Mephisto, Seitenzitat) und
BVerfGE 119, 1 (Esra, Rn.). DARSTELLUNG: keine intimen oder sexuellen Darstellungen, keine Romanzitate, „intime Szenen“
nur als Text-Pille; reale Personen (Klaus Mann, Gustaf Gründgens, Autor und Klägerinnen im Esra-Fall) keine Figuren,
im Esra-Fall keine Namen; keine Buchcover, nur neutrale Icons. Szenen laut ../SZENENPLAN.md.
Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/neinz2/tisch als eigene Kopie aus Folge 154
(gemeinsame Dateien unverändert); neu: regal, kissen, hoehe (sitzende Figur). Zahlen auf Tafeln, Pillen und Blasen als
Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from ostil import titel, karte, pille
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_160/"

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
LILAHELL = (246, 243, 255, 255)
BLAUHELL = (228, 238, 253, 255)
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
        assert F(s, g).getlength(glyphen(t)) <= w - 30, f"Blockzeile zu breit: {t}"
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
        if n.startswith(("bild:", "ficon:", "bank")) or "/op_160/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def wortlaut(x, y, w, zeilen, quelle, cue, marken=(), size=32, bis=None):
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 04.10.2026), als Zitat mit Normangabe;
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 103/109/112) --------------------------------
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


def neinz2(text, y, cue, kreuz, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile zum Satzbeginn, Kreuz erst zur gesprochenen Verneinung (kreuz = Cue des Wortes „nicht“)."""
    return [nein(x - 45, y + 20, kreuz, gr=gr), z(text, x, y, cue, stil, size, **k)]


# --- eigene Szenenbausteine (programmatisch, Palettenflächen, Tuschekontur) ---------------------------------------------------
def _flaeche(w, h):
    s = 2
    im = Image.new("RGBA", ((w + 12) * s, (h + 12) * s))
    return im, ImageDraw.Draw(im), s






def tisch(x, breite, cue):
    """Schreibtisch aus Grundformen (Holzplatte, zwei Beine) auf dem Boden."""
    im, dr, s = _flaeche(breite, 210)
    o = 6 * s
    dr.rounded_rectangle((o, o, o + breite * s, o + 34 * s), 8 * s, fill=HOLZ, outline=INK, width=5 * s)
    for xx in (o + 30 * s, o + (breite - 52) * s):
        dr.rectangle((xx, o + 34 * s, xx + 22 * s, o + 210 * s), fill=HOLZ, outline=INK, width=5 * s)
    im = im.resize((breite + 12, 222), Image.LANCZOS)
    return hart(El(im, x, BODEN - 216, cue, "cut", 0.0, None, name="tisch"))




BODEN = 860
FH = 440                                    # stehende Figur in der Fallszene
X1, X2 = 1400, 1720                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
SITZ = 0.77                                 # Winfried sitzt: Höhe relativ zur stehenden Figur (gleiche Kopfgröße)
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"LI": "Liesel", "WI": "Winfried", "HO": "Frau Hollerbach"}
NFARBE = {"LI": PINK, "WI": BLAU, "HO": GRUEN}


def hoehe(k, h):
    return round(h * SITZ) if k == "WI" else h


def boden(cue):
    return hart(linienzug([(40, BODEN), (1880, BODEN)], cue, breite=7, farbe=INK))


def kissen(cx, unten, h, cue, bis=None):
    """Sitzkissen unter Winfried (Grundform, Palettenfarbe); liegt hinter der Figur."""
    w = int(h * 0.62)
    im, dr, s = _flaeche(w, 34)
    o = 6 * s
    dr.rounded_rectangle((o, o, o + w * s, o + 34 * s), 16 * s, fill=GELB, outline=INK, width=5 * s)
    im = im.resize((w + 12, 46), Image.LANCZOS)
    return El(im, cx - w / 2 + h * 0.08, unten - 40, cue, "cut", 0.0, bis, name="kissen")


def regal(cue):
    """Bücherregal an der Wand links (Grundformen, Buchrücken in Palettenfarben)."""
    x0, y0, w, h = 60, 150, 440, BODEN - 150
    im, dr, s = _flaeche(w, h)
    o = 6 * s
    dr.rectangle((o, o, o + w * s, o + h * s), fill=HOLZ, outline=INK, width=5 * s)
    farben = [ROT, BLAU, GELB, GRUEN, LILA, PINK, TUERKIS, WEISS]
    import random
    rnd = random.Random(160)
    fach = (h - 30) // 4
    for f in range(4):
        yb = o + (25 + (f + 1) * fach) * s                # Fachboden
        dr.rectangle((o, yb, o + w * s, yb + 12 * s), fill=HOLZ, outline=INK, width=4 * s)
        xx = o + 22 * s
        while xx < o + (w - 40) * s:
            bw = rnd.randint(22, 34) * s; bh = rnd.randint(int(fach * 0.62), int(fach * 0.85)) * s
            dr.rectangle((xx, yb - bh, xx + bw, yb), fill=rnd.choice(farben), outline=INK, width=4 * s)
            xx += bw + rnd.randint(0, 4) * s
    im = im.resize((w + 12, h + 12), Image.LANCZOS)
    return hart(El(im, x0, y0, cue, "cut", 0.0, None, name="regal"))


def requisit(folge, px=PX, bis=None, pu=PU, py=PY):
    """Wechselndes Requisit rechts der Tafel: folge = [(cue, (set, icon, breite, fuell), pillentext, pillenfarbe)]."""
    els = []
    for i, (c, ic, txt, pf) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else bis
        if ic:
            s_, n_, br, fu = ic
            els.append(ficon(s_, n_, px, pu, br, c, fuell=fu, bis=b))
        if txt:
            els.append(pl(txt, px, py, c, fill=pf, size=28, anker="m", bis=b))
    return rechts_frei(els)


def stehend(k, x, folge, bis=None):
    h = hoehe(k, FR)
    els = [kissen(x, FB, h, folge[0][0], bis)] if k == "WI" else []
    els += [*fig(k, x, FB, h, folge, bis=bis), bis_(ns(NAME[k], x, FB, folge[0][0], NFARBE[k], d=0.1), bis)]
    return rechts_frei(els, 1200)


def paar(a, af, b, bf):
    """Tafelszene: zwei Figuren rechts der Tafel (beide blicken nach links zur Tafel)."""
    return [*stehend(a, X1, af), *stehend(b, X2, bf)]


# ===========================================================================================================================
# A Fall: Leseabend in der Buchhandlung (fiktiv). Frau Hollerbach links am Regal (blickt nach rechts), Liesel am Lesetisch
# (blickt nach rechts zum Publikum), Winfried sitzt rechts auf einem Kissen in der ersten Reihe (blickt nach links).
# ===========================================================================================================================
HOX, LIX, WIX = 640, 1110, 1600
TISCH_X, TISCH_B = 760, 260
TISCH_O = BODEN - 216 + 8
WH = round(FH * SITZ)


def buchhandlung(cue, mit_buch=True):
    els = [boden(cue), regal(cue), tisch(TISCH_X, TISCH_B, cue)]
    return els


def winfried_kissen(cue):
    return hart(kissen(WIX, BODEN, WH, cue))


folie([(NULL, "Fall · Leseabend in der Buchhandlung"), ("erkennt", "Fall · Winfried erkennt sich im Roman"),
       ("frage", "Die Frage · Wie viel Wahrheit darf ein Roman enthalten?"),
       ("klassiker", "Die Frage · Mephisto- und Esra-Beschluss")], [
    *buchhandlung(NULL),
    # Liesel liest aus dem aufgeschlagenen Buch; bei Winfrieds Einwurf klappt sie es zu (Handlungsgeräusch)
    hart(ficon("tabler", "book", TISCH_X + 130, TISCH_O, 130, NULL, fuell=WEISS, bis="wi1", anim="cut")),
    szene(hart(ficon("tabler", "book-2", TISCH_X + 130, TISCH_O, 100, "wi1", fuell=ROT, anim="cut")), "160buch*", 0.9, -0.15),
    # Frau Hollerbach begrüßt das Publikum (blickt nach rechts)
    *fig("HO", HOX, BODEN, FH, [(NULL, "ruhig_r")], bis="hgruss", erst="cut"),
    *redet("HO_redet_r", HOX, BODEN, FH, "hgruss", "ex"),
    *fig("HO", HOX, BODEN, FH, [("ex", "ruhig_r"), ("wi1", "froh_r"), (beim("wi1", "So"), "ruhig_r")], erst="cut"),
    hart(ns("Frau Hollerbach", HOX, BODEN, NULL, GRUEN)),
    # Liesel (blickt nach rechts zu Winfried)
    *fig("LI", LIX, BODEN, FH, [(NULL, "ruhig_r"), ("wi1", "sorge_r")], bis="li1", erst="cut"),
    *redet("LI_redet_r", LIX, BODEN, FH, "li1", "frage"),
    *fig("LI", LIX, BODEN, FH, [("frage", "denkt_r")], erst="cut"),
    hart(ns("Liesel", LIX, BODEN, NULL, PINK)),
    # Winfried (sitzt, blickt nach links zu Liesel)
    winfried_kissen(NULL),
    *fig("WI", WIX, BODEN, WH, [(NULL, "ruhig"), (beim("erkennt", "erkennt"), "denkt"), (beim("erkennt", "intime"), "aerger")],
         bis="wi1", erst="cut"),
    *redet("WI_redet", WIX, BODEN, WH, "wi1", "li1"),
    *fig("WI", WIX, BODEN, WH, [("li1", "aerger"), ("frage", "ernst")], erst="cut"),
    hart(ns("Winfried", WIX, BODEN, NULL, BLAU)),
    pl("ihr früherer Partner", WIX, BODEN + 84, "ex", fill=WEISS, size=28, anker="m"),
    # was Winfried hört (nur als Text-Pille, keine Darstellung)
    pl("erkennt sich in der Hauptfigur wieder", 600, 40, beim("erkennt", "erkennt"), fill=WEISS, size=30, bis="wi1"),
    pl("bis in intime Szenen", 600, 104, beim("erkennt", "intime"), fill=HELLROT, size=30, bis="wi1"),
    blase("sprech", 560, 190, "hgruss", 980, 250, inhalt=["Willkommen! Heute liest Liesel", "aus ihrem neuen Roman."],
          textsize=30, figur=("HO_redet_r", HOX, BODEN, FH), bis="ex"),
    blase("sprech", 560, 190, "wi1", 1440, 250, inhalt=["Das bin ja ich! So darf das", "Buch nicht verbreitet werden."],
          textsize=30, figur=("WI_redet", WIX, BODEN, WH), bis="li1"),
    blase("sprech", 520, 190, "li1", 1290, 250, inhalt=["Das ist ein Roman.", "Die Figur ist erfunden."],
          textsize=32, figur=("LI_redet_r", LIX, BODEN, FH), bis="frage"),
    pl("Wie viel Wahrheit darf ein Roman enthalten?", 560, 40, "frage", fill=PINK, size=34),
    pl("Mephisto-Beschluss · BVerfGE 30, 173", 560, 112, beim("klassiker", "Mephisto"), fill=GELB, size=30),
    pl("Esra-Beschluss · BVerfGE 119, 1", 560, 178, beim("klassiker", "Esra"), fill=GELB, size=30),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_160(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=33, zeilenabstand=1.28)
        els += e; y += 16
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_160("sv", [
    "Bei einem Leseabend in einer Buchhandlung liest die Autorin Liesel aus ihrem neuen Roman. In der ersten Reihe sitzt "
    "ihr früherer Partner Winfried.",
    "Er erkennt sich in der männlichen Hauptfigur wieder. Beruf, Wohnort und viele gemeinsame Erlebnisse stimmen "
    "überein, sodass auch Freunde und Kollegen ihn erkennen. Der Roman schildert auch intime Szenen der Beziehung.",
    "Winfried verlangt, dass der Roman nicht weiter verbreitet wird. Liesel beruft sich auf die Kunstfreiheit: Es "
    "handle sich um einen Roman, die Figur sei erfunden.",
], "Wäre ein gerichtliches Verbot des Romans mit Art. 5 Abs. 3 Satz 1 GG vereinbar?")

# ===========================================================================================================================
# C1 I. Schutzbereich: Wortlautkarte Art. 5 Abs. 3 Satz 1 GG, vorbehaltlos (BVerfGE 30, 173 <191>)
# ===========================================================================================================================
PI = "I. Schutzbereich"
W53 = ["„(3) Kunst und Wissenschaft, Forschung und Lehre sind frei. …“"]
w53, w53_y = wortlaut(80, 175, 1100, W53, "Art. 5 Abs. 3 Satz 1 GG", "a53", marken=[
    (0, "Kunst", beim("a53", "Kunst")), (0, "frei", beim("a53", "frei"))], size=32)
folie([("a53", f"{PI} · Art. 5 Abs. 3 Satz 1 GG"), ("vorb", f"{PI} › vorbehaltlos gewährleistet")], [
    *tafel("a53", "I. Schutzbereich: die Kunstfreiheit"),
    *w53,
    *neinz("kein Gesetzesvorbehalt im Wortlaut", w53_y + 40, "vorb", "Bold", 34, x=160),
    blk(110, w53_y + 110, 1040, 80, GELB, beim("vorb", "vorbehaltlos"), [("vorbehaltlos gewährleistet", "ExtraBold", 36, INK)]),
    zit("BVerfGE 30, 173 <191>; BVerfGE 119, 1, Rn. 68", 110, w53_y + 205, beim("vorb", "vorbehaltlos")),
    *requisit([("a53", ("tabler", "palette", 110, GELB), "Kunstfreiheit", GELB),
               ("vorb", ("tabler", "shield-check", 110, HELLGRUEN), "vorbehaltlos", HELLGRUEN)]),
    *stehend("LI", FX, [("a53", "ruhig"), (beim("vorb", "vorbehaltlos"), "froh")]),
])

# ===========================================================================================================================
# C2 Kunstbegriffe (materiell: BVerfGE 30, 173 <188 f.>; formal, offen: BVerfGE 67, 213 <226 f.>)
# ===========================================================================================================================
folie([("kunst", f"{PI} › Was ist Kunst?"), ("mat", f"{PI} › materieller Kunstbegriff"),
       ("formal", f"{PI} › formaler Kunstbegriff"), ("offen", f"{PI} › offener Kunstbegriff"),
       ("roman", f"{PI} › Roman ist Kunst (+)")], [
    *tafel("kunst", "Was ist Kunst? Drei Kunstbegriffe"),
    blk(110, 172, 1040, 250, BLAUHELL, "mat", [("materiell (Mephisto-Beschluss):", "ExtraBold", 32, INK),
                                            ("„freie schöpferische Gestaltung, in der Eindrücke,", "Regular", 31, INK),
                                            ("Erfahrungen, Erlebnisse des Künstlers durch das", "Regular", 31, INK),
                                            ("Medium einer bestimmten Formensprache zu", "Regular", 31, INK),
                                            ("unmittelbarer Anschauung gebracht werden“", "Regular", 31, INK)]),
    zit("BVerfGE 30, 173 <188 f.>", 110, 432, "mat"),
    blk(110, 478, 1040, 110, LILAHELL, "formal", [("formal: Gattungsanforderungen eines Werktyps,", "ExtraBold", 32, INK),
                                                ("etwa Malen, Bildhauen, Dichten", "Regular", 31, INK)]),
    blk(110, 608, 1040, 110, HELLGRUEN, "offen", [("offen: durch fortgesetzte Interpretation immer", "ExtraBold", 32, INK),
                                               ("weiterreichende Bedeutungen", "Regular", 31, INK)]),
    zit("BVerfGE 67, 213 <226 f.> (Anachronistischer Zug)", 110, 728, "formal"),
    *plusminus("Ein Roman ist Kunst", 110, 790, "roman", True, size=36, stil="ExtraBold"),
    zit("BVerfGE 30, 173 <189 f.>; BVerfGE 119, 1, Rn. 59", 560, 800, "roman"),
    *requisit([("kunst", ("tabler", "palette", 110, GELB), "Was ist Kunst?", PINK),
               ("mat", ("tabler", "brush", 110, BLAUHELL), "materiell", BLAUHELL),
               ("formal", ("tabler", "typography", 110, LILAHELL), "formal", LILAHELL),
               ("offen", ("tabler", "search", 110, HELLGRUEN), "offen", HELLGRUEN),
               ("roman", ("tabler", "book", 120, WEISS), "Roman: Kunst (+)", GELB)]),
    *stehend("LI", FX, [("kunst", "ruhig"), ("mat", "denkt"), ("roman", "froh")]),
])

# ===========================================================================================================================
# C3 Werkbereich und Wirkbereich, Verlag (BVerfGE 30, 173 <189, 191>; BVerfGE 119, 1, Rn. 63–65)
# ===========================================================================================================================
folie([("werk", f"{PI} › Werkbereich"), ("wirk", f"{PI} › Wirkbereich"), ("verlag", f"{PI} › auch der Verlag")], [
    *tafel("werk", "Werkbereich und Wirkbereich"),
    blk(110, 180, 505, 170, BLAUHELL, "werk", [("Werkbereich", "ExtraBold", 34, INK),
                                            ("künstlerische Betätigung:", "Regular", 31, INK),
                                            ("das Schreiben", "Regular", 31, INK)]),
    blk(645, 180, 505, 170, LILAHELL, "wirk", [("Wirkbereich", "ExtraBold", 34, INK),
                                            ("Darbietung und", "Regular", 31, INK),
                                            ("Verbreitung", "Regular", 31, INK)]),
    zit("BVerfGE 30, 173 <189>", 110, 362, "wirk"),
    *okz("Deshalb kann sich auch der Verlag", 430, "verlag", "Bold", 34, x=160),
    z("auf die Kunstfreiheit berufen.", 160, 476, beim("verlag", "Kunstfreiheit"), "Bold", 34),
    zit("BVerfGE 30, 173 <191>; BVerfGE 119, 1, Rn. 64 f.", 160, 526, beim("verlag", "Kunstfreiheit")),
    *requisit([("werk", ("tabler", "writing", 110, BLAUHELL), "schreiben", BLAUHELL),
               ("wirk", ("tabler", "books", 120, LILAHELL), "verbreiten", LILAHELL),
               ("verlag", ("tabler", "building-store", 120, WEISS), "Verlag", WEISS)], px=1560),
    *paar("LI", [("werk", "ruhig"), ("verlag", "froh")], "WI", [("werk", "ernst"), ("verlag", "denkt")]),
])

# ===========================================================================================================================
# D II. Eingriff (BVerfGE 119, 1, Rn. 58, 66, 69)
# ===========================================================================================================================
PII = "II. Eingriff"
folie([("eingriff", f"{PII} · gerichtliches Verbot (+)"), ("dritt", f"{PII} › Klage eines Privaten")], [
    *tafel("eingriff", "II. Eingriff: das gerichtliche Verbot"),
    *okz("Ein Gericht verbietet den Roman:", 185, "eingriff", "Bold", 34, x=160),
    *plusminus("Eingriff in die Kunstfreiheit", 160, 233, beim("eingriff", "greift"), True, size=34, stil="Bold"),
    blk(110, 300, 1040, 76, HELLROT, beim("eingriff", "besonders"), [("besonders starker Eingriff", "ExtraBold", 34, INK)]),
    zit("BVerfGE 119, 1, Rn. 58, 66", 110, 388, beim("eingriff", "besonders")),
    z("Ein Privater klagt? Das ändert nichts:", 110, 460, "dritt", "Bold", 34),
    *okz("Das Gericht ist den Grundrechten", 515, beim("dritt", "Gericht"), size=34),
    z("beider Seiten verpflichtet.", 185, 561, beim("dritt", "beider"), size=34),
    zit("BVerfGE 119, 1, Rn. 69; Ausstrahlung: Folge zum Lüth-Urteil", 185, 611, beim("dritt", "Lüth")),
    *requisit([("eingriff", ("tabler", "gavel", 120, HOLZ), "Verbot", HELLROT),
               ("dritt", ("tabler", "scale", 120, WEISS), "beide Seiten", WEISS)], px=1560),
    *paar("LI", [("eingriff", "sorge"), ("dritt", "denkt")], "WI", [("eingriff", "ernst"), ("dritt", "ruhig")]),
])

# ===========================================================================================================================
# E1 III. Rechtfertigung: verfassungsimmanente Schranken (BVerfGE 30, 173 <191–193>; BVerfGE 119, 1, Rn. 68)
# ===========================================================================================================================
PIII = "III. Rechtfertigung"
folie([("schranke", f"{PIII} · vorbehaltlos, nicht schrankenlos"), ("verf", f"{PIII} › kollidierendes Verfassungsrecht"),
       ("nicht52", f"{PIII} › nicht Art. 5 Abs. 2 GG")], [
    *tafel("schranke", "III. Rechtfertigung: Schranken"),
    blk(110, 175, 1040, 80, GELB, "schranke", [("vorbehaltlos, aber nicht schrankenlos", "ExtraBold", 36, INK)]),
    zit("BVerfGE 30, 173 <193>", 110, 266, "schranke"),
    *okz("Grenzen zieht nur die Verfassung selbst:", 330, "verf", "Bold", 34),
    z("kollidierendes Verfassungsrecht", 185, 376, beim("verf", "kollidierendes"), "Bold", 34),
    zit("BVerfGE 30, 173 <193>; BVerfGE 119, 1, Rn. 68", 185, 424, beim("verf", "kollidierendes")),
    *neinz2("Schranken des Art. 5 Abs. 2 GG: gelten nicht", 500, "nicht52", beim("nicht52", "nicht"), "Bold", 34),
    zit("BVerfGE 30, 173 <191>, Leitsatz 4", 185, 548, beim("nicht52", "nicht")),
    *requisit([("schranke", ("tabler", "shield-check", 110, GELB), "nicht schrankenlos", GELB),
               ("verf", ("tabler", "book-2", 110, ROT), "Verfassung", WEISS),
               ("nicht52", ("tabler", "ban", 100, HELLROT), "nicht Art. 5 Abs. 2", HELLROT)], px=1560),
    *paar("LI", [("schranke", "denkt"), ("nicht52", "ruhig")], "WI", [("schranke", "ruhig"), ("verf", "froh")]),
])

# ===========================================================================================================================
# E2 Kollidierend: allgemeines Persönlichkeitsrecht (Wortlautkarten Art. 2 Abs. 1, Art. 1 Abs. 1 GG; BVerfGE 119, 1, Rn. 70 f.)
# ===========================================================================================================================
W21 = ["„(1) Jeder hat das Recht auf die freie Entfaltung seiner", "Persönlichkeit, …“"]
W11 = ["„(1) Die Würde des Menschen ist unantastbar. …“"]
w21, w21_y = wortlaut(80, 290, 1100, W21, "Art. 2 Abs. 1 GG (Auszug)", "a21",
                      marken=[(0, "freie Entfaltung", beim("a21", "freie")), (1, "Persönlichkeit", beim("a21", "Persönlichkeit", 1))], size=32)
w11, w11_y = wortlaut(80, w21_y + 25, 1100, W11, "Art. 1 Abs. 1 Satz 1 GG", "a11",
                      marken=[(0, "Würde des Menschen", beim("a11", "Würde")), (0, "unantastbar", beim("a11", "unantastbar"))], size=32)
folie([("apr", f"{PIII} › allgemeines Persönlichkeitsrecht"), ("a21", f"{PIII} › Art. 2 Abs. 1 GG"),
       ("a11", f"{PIII} › i. V. m. Art. 1 Abs. 1 GG"), ("entst", f"{PIII} › Schutz vor Entstellung")], [
    *tafel("apr", "Kollision: das Persönlichkeitsrecht"),
    blk(110, 172, 1040, 90, PINK, "apr", [("allgemeines Persönlichkeitsrecht,", "ExtraBold", 33, INK),
                                       ("Art. 2 Abs. 1 i. V. m. Art. 1 Abs. 1 GG", "ExtraBold", 31, INK)]),
    *w21, *w11,
    *okz("schützt vor verfälschenden oder", w11_y + 30, "entst", "Bold", 34, x=160),
    z("entstellenden Darstellungen", 160, w11_y + 76, beim("entst", "entstellenden"), "Bold", 34),
    zit("BVerfGE 119, 1, Rn. 70 f.", 160, w11_y + 124, beim("entst", "entstellenden")),
    *requisit([("apr", ("tabler", "fingerprint", 110, PINK), "Persönlichkeitsrecht", PINK),
               ("a11", ("tabler", "shield-check", 110, WEISS), "Menschenwürde", WEISS),
               ("entst", ("tabler", "mask", 110, HELLROT), "Entstellung", HELLROT)], px=1560),
    *stehend("WI", FX, [("apr", "ruhig"), ("a21", "denkt"), ("entst", "ernst")]),
])

# ===========================================================================================================================
# F1 Der echte Fall Mephisto (BVerfGE 30, 173 <173–181>) – ohne Figuren, nur neutrale Icons, kein Buchcover
# ===========================================================================================================================
PM = "Mephisto"
folie([("meph", f"{PM} · der Fall"), ("mann", f"{PM} › der Roman"), ("vorbild", f"{PM} › das Vorbild"),
       ("klage1", f"{PM} › Klage und Verbot")], [
    boden("meph"),
    pl("Mephisto-Beschluss · BVerfG, 24.2.1971 · 1 BvR 435/68 · BVerfGE 30, 173", 70, 40, "meph", fill=GELB, size=30),
    pl("Klaus Mann: Roman „Mephisto“", 70, 118, "mann", fill=WEISS, size=30),
    pl("Aufstieg des Schauspielers Hendrik Höfgen im nationalsozialistischen Deutschland", 70, 188,
       beim("mann", "Aufstieg"), fill=WEISS, size=30),
    pl("Vorbild: der Schauspieler Gustaf Gründgens", 70, 258, "vorbild", fill=HELL, size=30),
    pl("nach seinem Tod: Klage des Adoptivsohns", 70, 328, "klage1", fill=WEISS, size=30),
    pl("OLG und BGH: Veröffentlichung untersagt", 70, 398, beim("klage1", "Oberlandesgericht"), fill=HELLROT, size=30),
    zit("BVerfGE 30, 173 <174 f., 176–181>", 80, 470, beim("klage1", "Oberlandesgericht")),
    ficon("tabler", "calendar-event", 260, BODEN, 150, "meph", fuell=WEISS),
    ficon("tabler", "book", 640, BODEN, 190, "mann", fuell=WEISS),
    ficon("tabler", "masks-theater", 1010, BODEN, 180, "vorbild", fuell=HELL),
    ficon("tabler", "gavel", 1380, BODEN, 170, beim("klage1", "Oberlandesgericht"), fuell=HOLZ),
    ficon("tabler", "ban", 1680, BODEN, 150, beim("klage1", "untersagten"), fuell=HELLROT),
])

# ===========================================================================================================================
# F2 Mephisto: Abwägung und Ergebnis (BVerfGE 30, 173 <194–200>)
# ===========================================================================================================================
UB = ["„… ob und inwieweit das ‚Abbild‘ gegenüber dem ‚Urbild‘ …",
      "so verselbständigt erscheint, daß das Individuelle,",
      "Persönlich-Intime zugunsten des Allgemeinen,",
      "Zeichenhaften der ‚Figur‘ objektiviert ist.“"]
ub, ub_y = wortlaut(80, 330, 1100, UB, "BVerfGE 30, 173 <195>", "urbild", marken=[
    (0, "Abbild", beim("urbild", "Abbild")), (0, "Urbild", beim("urbild", "Urbild")),
    (3, "objektiviert", beim("urbild", "objektiviert"))], size=31)
folie([("tot", f"{PM} › nach dem Tod: Art. 1 Abs. 1 GG"), ("urbild", f"{PM} › Abbild und Urbild"),
       ("schmaeh", f"{PM} › Schmähschrift in Romanform"), ("patt", f"{PM} › Stimmengleichheit 3:3"),
       ("erg1", f"{PM} · Ergebnis: Verbot bleibt")], [
    *tafel("tot", "Mephisto: die Abwägung"),
    *neinz2("Art. 2 Abs. 1 GG: endet mit dem Tod", 172, "tot", beim("tot", "nicht"), "Bold", 33),
    *okz("Art. 1 Abs. 1 GG: Achtungsanspruch bleibt", 220, beim("tot", "geschützt"), "Bold", 33),
    zit("BVerfGE 30, 173 <194>", 185, 268, beim("tot", "geschützt")),
    *ub,
    z("Gerichte: negativ-verfälschendes Porträt,", 110, ub_y + 18, "schmaeh", "Bold", 33),
    z("„Schmähschrift in Romanform“", 110, ub_y + 62, beim("schmaeh", "Schmähschrift"), "Bold", 33),
    zit("BVerfGE 30, 173 <198 f.>", 640, ub_y + 70, beim("schmaeh", "Schmähschrift")),
    blk(110, ub_y + 115, 440, 76, GELB, "patt", [("Stimmengleichheit 3:3", "ExtraBold", 31, INK)]),
    blk(580, ub_y + 115, 570, 76, GRUEN, "erg1", [("Verbot bleibt bestehen", "ExtraBold", 31, INK)]),
    zit("BVerfGE 30, 173 <195 f., 200>; Entscheidungsformel", 110, ub_y + 200, "erg1"),
    *requisit([("tot", ("tabler", "shield-check", 110, WEISS), "Menschenwürde", WEISS),
               ("urbild", ("tabler", "search", 110, WEISS), "Abbild/Urbild", WEISS),
               ("schmaeh", ("tabler", "mask", 110, HELLROT), "Schmähschrift", HELLROT),
               ("patt", ("tabler", "scale", 120, GELB), "3:3", GELB),
               ("erg1", ("tabler", "ban", 100, GRUEN), "Verbot bleibt", GRUEN)], px=1560),
    *stehend("LI", FX, [("tot", "ruhig"), ("urbild", "denkt"), ("erg1", "sorge")]),
])

# ===========================================================================================================================
# G1 Der echte Fall Esra (BVerfGE 119, 1, Rn. 1–3, 7, 10 f.) – ohne Figuren, ohne Namen, kein Buchcover
# ===========================================================================================================================
PE = "Esra"
folie([("esra", f"{PE} · der Fall"), ("esra1", f"{PE} › der Roman"), ("klaeg", f"{PE} › die Klägerinnen")], [
    boden("esra"),
    pl("Esra-Beschluss · BVerfG, 13.6.2007 · 1 BvR 1783/05 · BVerfGE 119, 1", 70, 40, "esra", fill=GELB, size=30),
    pl("Roman „Esra“", 70, 118, "esra1", fill=WEISS, size=30),
    pl("Liebesgeschichte eines Schriftstellers und einer Schauspielerin", 70, 188, beim("esra1", "Liebesgeschichte"),
       fill=WEISS, size=30),
    pl("Klägerinnen: die frühere Partnerin des Autors und deren Mutter", 70, 258, "klaeg", fill=HELL, size=30),
    pl("erkannten sich in den Figuren wieder und klagten", 70, 328, beim("klaeg", "erkannten"), fill=WEISS, size=30),
    zit("BVerfGE 119, 1, Rn. 2 f., 7, 10 f.", 80, 400, beim("klaeg", "erkannten")),
    ficon("tabler", "calendar-event", 300, BODEN, 150, "esra", fuell=WEISS),
    ficon("tabler", "book", 720, BODEN, 190, "esra1", fuell=WEISS),
    ficon("tabler", "heart", 1100, BODEN, 160, beim("esra1", "Liebesgeschichte"), fuell=PINK),
    ficon("tabler", "search", 1450, BODEN, 150, beim("klaeg", "erkannten"), fuell=WEISS),
    ficon("tabler", "gavel", 1720, BODEN, 150, beim("klaeg", "klagten"), fuell=HOLZ),
])

# ===========================================================================================================================
# G2 Esra: kunstspezifische Betrachtung (LS 2; Rn. 74, 84)
# ===========================================================================================================================
folie([("kspez", f"{PE} › kunstspezifische Betrachtung"), ("vermut", f"{PE} › Vermutung der Fiktionalität"),
       ("erkenn", f"{PE} › Erkennbarkeit allein genügt nicht")], [
    *tafel("kspez", "Esra: kunstspezifische Betrachtung"),
    *okz("kunstspezifische Betrachtung", 185, "kspez", "Bold", 34),
    zit("BVerfGE 119, 1, Leitsatz 2", 185, 233, "kspez"),
    *okz("Ein Roman ist zunächst als Fiktion anzusehen,", 305, "vermut", "Bold", 34),
    z("auch wenn reale Vorbilder erkennbar sind", 185, 351, beim("vermut", "reale"), size=34),
    zit("Rn. 84 (Vermutung für die Fiktionalität)", 185, 399, beim("vermut", "reale")),
    *neinz2("Erkennbarkeit allein: noch keine Verletzung", 475, "erkenn", beim("erkenn", "keine"), "Bold", 34),
    zit("Rn. 74", 185, 523, beim("erkenn", "keine")),
    *requisit([("kspez", ("tabler", "book", 120, WEISS), "Kunst", GELB),
               ("vermut", ("tabler", "sparkles", 110, GELB), "Fiktion", GELB),
               ("erkenn", ("tabler", "search", 110, WEISS), "erkennbar", WEISS)], px=1560),
    *paar("LI", [("kspez", "ruhig"), ("vermut", "froh")], "WI", [("kspez", "ernst"), ("erkenn", "denkt")]),
])

# ===========================================================================================================================
# G3 Je-desto-Formel (LS 4, Rn. 90) und Intimsphäre (Rn. 88, 102)
# ===========================================================================================================================
JD = ["„Je stärker Abbild und Urbild übereinstimmen, desto",
      "schwerer wiegt die Beeinträchtigung des Persönlichkeitsrechts.",
      "Je mehr die künstlerische Darstellung besonders geschützte",
      "Dimensionen des Persönlichkeitsrechts berührt, desto stärker",
      "muss die Fiktionalisierung sein, um eine",
      "Persönlichkeitsrechtsverletzung auszuschließen.“"]
jd, jd_y = wortlaut(80, 175, 1100, JD, "BVerfGE 119, 1, Leitsatz 4 (Rn. 90)", "jed", marken=[
    (0, "Je stärker", beim("je1", "Je")), (1, "schwerer wiegt", beim("je1", "schwerer")),
    (2, "besonders geschützte", beim("je2", "besonders")), (4, "Fiktionalisierung", beim("je2", "Fiktionalisierung"))], size=31)
folie([("jed", f"{PE} › Je-desto-Formel"), ("je1", f"{PE} › je mehr Übereinstimmung, desto schwerer"),
       ("je2", f"{PE} › je geschützter, desto mehr Fiktionalisierung"), ("intim", f"{PE} › Intimsphäre: Menschenwürdekern")], [
    *tafel("jed", "Die Je-desto-Formel"),
    *jd,
    blk(110, jd_y + 30, 1040, 80, PINK, "intim", [("Intimsphäre: gehört zum Menschenwürdekern", "ExtraBold", 33, INK)]),
    zit("BVerfGE 119, 1, Rn. 88, 102", 110, jd_y + 122, "intim"),
    *requisit([("jed", ("tabler", "scale", 120, WEISS), "Je-desto-Formel", GELB),
               ("je2", ("tabler", "sparkles", 110, GELB), "Fiktionalisierung", GELB),
               ("intim", ("tabler", "lock-heart", 110, PINK), "Intimsphäre", PINK)], px=1560),
    *paar("LI", [("jed", "denkt"), ("intim", "sorge")], "WI", [("jed", "ruhig"), ("intim", "ernst")]),
])

# ===========================================================================================================================
# G4 Esra: Ergebnis (Entscheidungsformel; Rn. 57, 92–103)
# ===========================================================================================================================
folie([("erg2", f"{PE} · Ergebnis: teilweise Erfolg"), ("mutter", f"{PE} › Mutter: Verbot verletzt die Kunstfreiheit"),
       ("partn", f"{PE} › frühere Partnerin: Verbot hält")], [
    *tafel("erg2", "Esra: das Ergebnis"),
    blk(110, 175, 1040, 80, GELB, "erg2", [("Verfassungsbeschwerde: teilweise Erfolg", "ExtraBold", 34, INK)]),
    zit("BVerfGE 119, 1, Entscheidungsformel; Rn. 57", 110, 266, "erg2"),
    *neinz2("Verbot zugunsten der Mutter: verletzt", 335, "mutter", beim("mutter", "verletzte"), "Bold", 34),
    z("die Kunstfreiheit, Vermutung der Fiktion", 185, 381, beim("mutter", "Kunstfreiheit"), size=34),
    z("nicht hinreichend beachtet", 185, 427, beim("mutter", "Vermutung"), size=34),
    zit("Rn. 92–99", 185, 475, beim("mutter", "Vermutung")),
    *okz("Verbot zugunsten der früheren Partnerin: hält", 545, "partn", "Bold", 34),
    z("erkennbar, intimste Details,", 185, 591, beim("partn", "erkennbar"), size=34),
    z("dazu die Krankheit ihrer Tochter", 185, 637, beim("partn", "Krankheit"), size=34),
    zit("Rn. 100–103", 185, 685, beim("partn", "Krankheit")),
    *requisit([("erg2", ("tabler", "gavel", 120, HOLZ), "teilweise Erfolg", GELB),
               ("mutter", ("tabler", "circle-check", 110, HELLGRUEN), "Mutter: Kunstfreiheit verletzt", HELLGRUEN),
               ("partn", ("tabler", "lock-heart", 110, PINK), "Partnerin: Verbot hält", PINK)], px=1560),
    *paar("LI", [("erg2", "ruhig"), ("partn", "sorge")], "WI", [("erg2", "denkt"), ("partn", "ernst")]),
])

# ===========================================================================================================================
# H Zurück zur Lesung (gleicher Schauplatz wie A: die Geschichte kehrt zum Ausgangsfall zurück)
# ===========================================================================================================================
folie([("zur", "Zurück zur Lesung · die Lösung"), ("loes1", "Zurück zur Lesung › erkennbar und intim"),
       ("loes2", "Zurück zur Lesung › Verbot möglich, Abwägung")], [
    *buchhandlung("zur"),
    hart(ficon("tabler", "book-2", TISCH_X + 130, TISCH_O, 100, "zur", fuell=ROT, anim="cut")),
    *fig("HO", HOX, BODEN, FH, [("zur", "ruhig_r")], erst="cut"),
    hart(ns("Frau Hollerbach", HOX, BODEN, "zur", GRUEN)),
    *fig("LI", LIX, BODEN, FH, [("zur", "denkt_r"), (beim("loes2", "Verbot"), "sorge_r")], erst="cut"),
    hart(ns("Liesel", LIX, BODEN, "zur", PINK)),
    winfried_kissen("zur"),
    *fig("WI", WIX, BODEN, WH, [("zur", "ernst"), (beim("loes1", "wiegt"), "froh")], erst="cut"),
    hart(ns("Winfried", WIX, BODEN, "zur", BLAU)),
    *okz("für Bekannte erkennbar", 70, beim("loes1", "Bekannte"), "Bold", 32, x=640, rechts=1880),
    *okz("intime Szenen der Beziehung", 125, beim("loes1", "intime"), "Bold", 32, x=640, rechts=1880),
    pl("Persönlichkeitsrecht wiegt schwer", 595, 185, beim("loes1", "wiegt"), fill=PINK, size=32),
    pl("Verbot möglich, je nach Abwägung im Einzelfall", 595, 260, beim("loes2", "Verbot"), fill=GELB, size=32),
])

# ===========================================================================================================================
# I Klausurtipp (Lexi) – vorbehaltloses Grundrecht (BVerfGE 30, 173 <191, 193>; BVerfGE 93, 1 <21>)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · kein Art. 5 Abs. 2 GG"), ("tipp2", "Klausurtipp · Verfassungsgut mit Norm"),
       ("tipp3", "Klausurtipp · praktische Konkordanz")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("vorbehaltloses Grundrecht:", 200, 200, beim("tipp", "vorbehaltlosen"), "Bold", 36),
    *neinz2("kein Gesetzesvorbehalt, nicht Art. 5 Abs. 2 GG", 260, beim("tipp", "vorbehaltlosen"), beim("tipp", "keinen"),
            size=34, x=200),
    linienzug([(130, 335), (1130, 335)], "tipp2", breite=3),
    *okz("kollidierendes Verfassungsgut benennen,", 365, "tipp2", "Bold", 34, x=200),
    z("mit seiner Norm", 200, 411, beim("tipp2", "Norm"), "Bold", 34),
    blk(130, 485, 1000, 120, GELB, "tipp3", [("praktische Konkordanz:", "ExtraBold", 34, INK),
                                          ("möglichst schonender Ausgleich", "ExtraBold", 34, INK)]),
    zit("BVerfGE 30, 173 <191, 193>; BVerfGE 93, 1 <21>", 200, 620, beim("tipp3", "schonenden")),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# J Prüfschema
# ===========================================================================================================================
REIHEN = [("k1", 0, "I. Schutzbereich: Kunst, Werk- und Wirkbereich", True),
          ("k2", 0, "II. Eingriff, etwa das gerichtliche Verbot", True),
          ("k3", 0, "III. Rechtfertigung", True),
          ("k3a", 1, "1. verfassungsimmanente Schranke: kollidierendes Verfassungsrecht", False),
          ("k3b", 1, "2. praktische Konkordanz: kunstspezifische Betrachtung, Je-desto-Formel", False)]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfschema: Kunstfreiheit, Art. 5 Abs. 3 Satz 1 GG"), 110, 90, "sch", 46),
           zit("Grundschema: Folge zur Grundrechtsprüfung", 115, 165, beim("sch", "Grundschema"), rechts=1800)]
y = 250
for c, ebene, text, fett in REIHEN:
    x = (130, 200)[ebene]
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 42 if ebene == 0 else 38, rechts=1800))
    y += {0: 100, 1: 92}[ebene]
assert y <= 970, y
folie([("sch", "Prüfschema"), ("k1", "Prüfschema › I. Schutzbereich"), ("k2", "Prüfschema › II. Eingriff"),
       ("k3", "Prüfschema › III. Rechtfertigung"), ("k3a", "Prüfschema › III. 1. verfassungsimmanente Schranke"),
       ("k3b", "Prüfschema › III. 2. praktische Konkordanz")], els_sch)

# ===========================================================================================================================
# K Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Die Kunstfreiheit ist ", 0), ("vorbehaltlos", "a"), (",", 0)],
                 [("aber nicht schrankenlos.", "b")]], 750, 300, 44, "merke",
                {"a": beim("merke", "vorbehaltlos"), "b": beim("merke", "schrankenlos")}),
    *markertext([[("Je erkennbarer das Urbild und", 0)], [("je intimer das Geschilderte,", 0)],
                 [("desto stärker muss der Roman", 0)], [("fiktionalisieren", "c"), (".", 0)]], 750, 500, 44, "m2",
                {"c": beim("m2", "fiktionalisieren")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
