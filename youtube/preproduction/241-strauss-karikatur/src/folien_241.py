"""Folge 241 · Strauß-Karikatur: Darf man Politiker als Tiere zeichnen? – Serienstandard Open Peeps (Katzenkönig).
Fiktiver Rahmen: Redaktion eines Satiremagazins (Karikaturist Meinrad, Redakteurin Henriette), Büro der
Ministerpräsidentin Achenbach, Amtsgericht; danach der echte Fall sachlich: BVerfGE 75, 369 (Seitenzitat nach DFR).
DARSTELLUNG: Die Original-Karikaturen werden nicht nachgezeichnet, keine sexuelle Darstellung; Tiere nur als neutrales
Icon (Tabler „pig“, Fluent Emoji High Contrast „fox“) auf einem leeren Zeichenblatt, ohne Figur und ohne Pose. Die reale
Person ist keine Figur; ihr Name steht nur in der Fallbezeichnung „Strauß-Karikatur“. Szenen laut ../SZENENPLAN.md.
Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/neinz2/tisch als eigene Kopie aus Folge 160
(gemeinsame Dateien unverändert); neu: zeichentisch, pinnwand, fenster, richterbank; ns() hält lange Namensschilder im
Bild. Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from ostil import titel, karte, pille
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_241/"

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
        if n.startswith(("bild:", "ficon:", "bank")) or "/op_241/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def wortlaut(x, y, w, zeilen, quelle, cue, marken=(), size=32, bis=None):
    """Wortlaut-/Zitatkarte: Normtext wörtlich nach gesetze-im-internet.de bzw. Beschlusstext nach DFR (Abruf 07.10.2026),
    als Zitat mit Fundstelle; marken = [(zeile, wort, cue)] legt synchron zum gesprochenen Wort einen Textmarker."""
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 103/109/112/160) ----------------------------
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
    """Namensschild unter der Figur (ab ihrem ersten Auftritt, solange sie im Bild ist); lange Schilder werden so
    verschoben, dass sie vollständig im Bild bleiben."""
    w = F("Bold", 30).getlength(glyphen(text)) + 60 + 8
    cx = min(max(cx, 30 + w / 2), 1880 - w / 2)
    return pl(text, cx, unten + 22, cue, fill=fill, size=30, anker="m", **k)


def okz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Haken davor (zur gesprochenen Bejahung)."""
    return [ok(x - 45, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]


def neinz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Kreuz davor (zur gesprochenen Verneinung)."""
    return [nein(x - 45, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]


def neinz2(text, y, cue, kreuz, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile zum Satzbeginn, Kreuz erst zur gesprochenen Verneinung."""
    return [nein(x - 45, y + 20, kreuz, gr=gr), z(text, x, y, cue, stil, size, **k)]


def okz2(text, y, cue, haken, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile zum Satzbeginn, Haken erst zur gesprochenen Bejahung."""
    return [ok(x - 45, y + 20, haken, gr=gr), z(text, x, y, cue, stil, size, **k)]


# --- eigene Szenenbausteine (programmatisch, Palettenflächen, Tuschekontur) ----------------------------------------------
def _flaeche(w, h):
    s = 2
    im = Image.new("RGBA", ((w + 12) * s, (h + 12) * s))
    return im, ImageDraw.Draw(im), s


BODEN = 860
FH = 440                                    # stehende Figur in der Fallszene
X1, X2 = 1400, 1720                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"ME": "Meinrad", "HE": "Henriette", "AC": "Ministerpräsidentin Achenbach"}
NFARBE = {"ME": LILA, "HE": GRUEN, "AC": BLAU}


def boden(cue):
    return hart(linienzug([(40, BODEN), (1880, BODEN)], cue, breite=7, farbe=INK))


def tisch(x, breite, cue):
    """Schreibtisch aus Grundformen (Holzplatte, zwei Beine) auf dem Boden."""
    im, dr, s = _flaeche(breite, 210)
    o = 6 * s
    dr.rounded_rectangle((o, o, o + breite * s, o + 34 * s), 8 * s, fill=HOLZ, outline=INK, width=5 * s)
    for xx in (o + 30 * s, o + (breite - 52) * s):
        dr.rectangle((xx, o + 34 * s, xx + 22 * s, o + 210 * s), fill=HOLZ, outline=INK, width=5 * s)
    im = im.resize((breite + 12, 222), Image.LANCZOS)
    return hart(El(im, x, BODEN - 216, cue, "cut", 0.0, None, name="tisch"))


ZT_X, ZT_Y = 560, BODEN - 420               # Zeichentisch: linke obere Ecke


def zeichentisch(cue, bis=None):
    """Schräges Zeichenbrett mit leerem Blatt auf zwei Beinen (Grundformen)."""
    w, h = 340, 420
    im, dr, s = _flaeche(w, h)
    o = 6 * s
    P_ = lambda pts: [(o + x * s, o + y * s) for x, y in pts]
    dr.line(P_([(70, 240), (45, 418)]), fill=INK, width=12 * s)
    dr.line(P_([(280, 225), (305, 418)]), fill=INK, width=12 * s)
    dr.line(P_([(58, 340), (292, 330)]), fill=INK, width=8 * s)
    dr.polygon(P_([(8, 46), (332, 8), (332, 228), (8, 262)]), fill=HOLZ, outline=INK, width=6 * s)
    dr.polygon(P_([(34, 58), (306, 28), (306, 210), (34, 238)]), fill=WEISS, outline=INK, width=4 * s)
    im = im.resize((w + 12, h + 12), Image.LANCZOS)
    return hart(El(im, ZT_X, ZT_Y, cue, "cut", 0.0, bis, name="zeichentisch"))


def blattbild(setname, name, cue, fuell, bis=None, breite=150):
    """Neutrales Tier-Icon allein auf dem Zeichenblatt (keine Figur, keine Pose)."""
    return ficon(setname, name, ZT_X + 176, ZT_Y + 226, breite, cue, fuell=fuell, bis=bis)


def pinnwand(cue):
    """Pinnwand der Redaktion mit leeren Notizzetteln (Grundformen)."""
    x0, y0, w, h = 1460, 420, 400, 300
    im, dr, s = _flaeche(w, h)
    o = 6 * s
    dr.rounded_rectangle((o, o, o + w * s, o + h * s), 10 * s, fill=HOLZ, outline=INK, width=5 * s)
    for (a, b, c) in ((40, 40, GELB), (170, 60, BLAU), (290, 36, PINK), (70, 170, GRUEN), (220, 165, WEISS)):
        dr.rectangle((o + a * s, o + b * s, o + (a + 90) * s, o + (b + 90) * s), fill=c, outline=INK, width=4 * s)
        dr.ellipse((o + (a + 38) * s, o + (b - 6) * s, o + (a + 52) * s, o + (b + 8) * s), fill=ROT, outline=INK, width=2 * s)
    im = im.resize((w + 12, h + 12), Image.LANCZOS)
    return hart(El(im, x0, y0, cue, "cut", 0.0, None, name="pinnwand"))


def fenster(cue):
    """Fenster im Büro der Ministerpräsidentin."""
    x0, y0, w, h = 180, 190, 380, 300
    im, dr, s = _flaeche(w, h)
    o = 6 * s
    dr.rectangle((o, o, o + w * s, o + h * s), fill=BLAUHELL, outline=INK, width=6 * s)
    dr.line((o + w * s // 2, o, o + w * s // 2, o + h * s), fill=INK, width=5 * s)
    dr.line((o, o + h * s // 2, o + w * s, o + h * s // 2), fill=INK, width=5 * s)
    im = im.resize((w + 12, h + 12), Image.LANCZOS)
    return hart(El(im, x0, y0, cue, "cut", 0.0, None, name="fenster"))


RB_X, RB_W, RB_H = 140, 640, 300            # Richterbank


def richterbank(cue):
    """Richterbank des Amtsgerichts (Holzblock mit Frontblende)."""
    im, dr, s = _flaeche(RB_W, RB_H)
    o = 6 * s
    dr.rectangle((o, o, o + RB_W * s, o + 40 * s), fill=HOLZ, outline=INK, width=5 * s)
    dr.rectangle((o + 20 * s, o + 40 * s, o + (RB_W - 20) * s, o + RB_H * s), fill=HOLZ, outline=INK, width=5 * s)
    for k in range(3):
        xa = o + (50 + k * 195) * s
        dr.rectangle((xa, o + 80 * s, xa + 150 * s, o + (RB_H - 30) * s), outline=INK, width=4 * s)
    im = im.resize((RB_W + 12, RB_H + 12), Image.LANCZOS)
    return hart(El(im, RB_X, BODEN - RB_H, cue, "cut", 0.0, None, name="richterbank"))


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
    els = [*fig(k, x, FB, FR, folge, bis=bis), bis_(ns(NAME[k], x, FB, folge[0][0], NFARBE[k], d=0.1), bis)]
    return rechts_frei(els, 1200)


def paar(a, af, b, bf):
    """Tafelszene: zwei Figuren rechts der Tafel (beide blicken nach links zur Tafel)."""
    return [*stehend(a, X1, af), *stehend(b, X2, bf)]


# ===========================================================================================================================
# A1 Fall: Redaktion des Satiremagazins. Meinrad links am Zeichentisch (blickt nach rechts aufs Blatt), Henriette rechts
# (blickt nach links zu ihm). Das Blatt zeigt nur ein neutrales Schwein-Icon – keine Figur, keine Pose.
# ===========================================================================================================================
MEX, HEX = 400, 1250
folie([(NULL, "Fall · In der Redaktion eines Satiremagazins"), ("zeich", "Fall · Die Karikatur"),
       ("botsch", "Fall · Die Botschaft"), ("he1", "Fall · Satire darf alles?")], [
    boden(NULL), pinnwand(NULL), zeichentisch(NULL),
    szene(blattbild("tabler", "pig", beim("zeich", "Schwein"), PINK), "241stift*", 0.8, -0.1),
    pl("Satiremagazin · Redaktion", 1660, 740, NULL, fill=WEISS, size=28, anker="m", anim="cut"),
    pl("Karikatur: die Ministerpräsidentin als Schwein", 60, 40, beim("zeich", "Schwein"), fill=WEISS, size=30),
    pl("in einer sexuell herabwürdigenden Pose", 60, 104, "pose", fill=HELLROT, size=30),
    pl("Botschaft: Politik für Bauinvestoren", 60, 168, "botsch", fill=GELB, size=30),
    # Meinrad zeichnet (blickt nach rechts zum Blatt)
    *fig("ME", MEX, BODEN, FH, [(NULL, "ruhig_r"), ("zeich", "zeichnet_r"), ("botsch", "froh_r")], erst="cut"),
    hart(ns("Meinrad", MEX, BODEN, NULL, LILA)),
    pl("Karikaturist", MEX, BODEN + 84, NULL, fill=WEISS, size=28, anker="m", anim="cut"),
    # Henriette (blickt nach links zu Meinrad)
    *fig("HE", HEX, BODEN, FH, [(NULL, "ruhig"), ("botsch", "denkt")], bis="he1", erst="cut"),
    *redet("HE_redet", HEX, BODEN, FH, "he1", "heft"),
    hart(ns("Henriette", HEX, BODEN, NULL, GRUEN)),
    pl("Redakteurin", HEX, BODEN + 84, NULL, fill=WEISS, size=28, anker="m", anim="cut"),
    blase("sprech", 520, 190, "he1", 1560, 270, inhalt=["Satire darf alles.", "Das drucken wir."], textsize=32,
          figur=("HE_redet", HEX, BODEN, FH), bis="heft"),
])

# ===========================================================================================================================
# A2 Büro der Ministerpräsidentin: Heft auf dem Schreibtisch, sie blickt nach links darauf
# ===========================================================================================================================
ACX = 1250
TI_X, TI_B = 640, 420
folie([("heft", "Fall · Das Heft erscheint"), ("ac1", "Fall · Der Strafantrag")], [
    boden("heft"), fenster("heft"), tisch(TI_X, TI_B, "heft"),
    hart(ficon("ph", "newspaper", TI_X + 210, BODEN - 208, 170, "heft", fuell=WEISS, anim="cut")),
    hart(ficon("tabler", "pig", TI_X + 210, BODEN - 252, 60, "heft", fuell=PINK, anim="cut")),
    pl("Das Heft erscheint", 60, 40, "heft", fill=WEISS, size=30),
    *fig("AC", ACX, BODEN, FH, [("heft", "ruhig"), (beim("heft", "sieht"), "denkt"), (beim("heft", "Zeichnung"), "aerger")],
         bis="ac1", erst="cut"),
    *redet("AC_redet", ACX, BODEN, FH, "ac1", "urteil"),
    hart(ns("Ministerpräsidentin Achenbach", ACX, BODEN, "heft", BLAU)),
    blase("sprech", 600, 250, "ac1", 1560, 260, inhalt=["Das ist keine Kritik mehr,", "das ist entwürdigend.",
                                                          "Ich stelle Strafantrag."], textsize=30,
          figur=("AC_redet", ACX, BODEN, FH), bis="urteil"),
    pl("Strafantrag wegen Beleidigung", 60, 104, beim("ac1", "Strafantrag"), fill=HELLROT, size=30),
])

# ===========================================================================================================================
# A3 Amtsgericht: Richterbank links; Meinrad und die Ministerpräsidentin blicken nach links zur Bank
# ===========================================================================================================================
GMX, GAX = 1120, 1600


def gericht(cue):
    return [boden(cue), richterbank(cue),
            hart(pl("Amtsgericht", RB_X + RB_W / 2, BODEN - RB_H + 110, cue, fill=WEISS, size=30, anker="m", anim="cut"))]


folie([("urteil", "Fall · Das Amtsgericht verurteilt"), ("me1", "Fall · Meinrad: Das ist Kunst"),
       ("frage", "Die Frage · Darf man Politiker als Tiere zeichnen?"),
       ("klassiker", "Die Frage · Beschluss zur Strauß-Karikatur")], [
    *gericht("urteil"),
    szene(ficon("tabler", "gavel", RB_X + RB_W / 2, BODEN - RB_H + 6, 130, beim("urteil", "verurteilt"), fuell=HOLZ),
          "241hammer*", 0.9, 0.0),
    pl("Urteil: Beleidigung", 60, 40, beim("urteil", "Beleidigung"), fill=HELLROT, size=30, bis="frage"),
    *fig("ME", GMX, BODEN, FH, [("urteil", "ernst"), (beim("urteil", "verurteilt"), "sorge")], bis="me1", erst="cut"),
    *redet("ME_redet", GMX, BODEN, FH, "me1", "frage"),
    *fig("ME", GMX, BODEN, FH, [("frage", "denkt")], erst="cut"),
    hart(ns("Meinrad", GMX, BODEN, "urteil", LILA)),
    *fig("AC", GAX, BODEN, FH, [("urteil", "ernst"), ("me1", "aerger"), ("frage", "denkt")], erst="cut"),
    hart(ns("Ministerpräsidentin Achenbach", GAX, BODEN, "urteil", BLAU)),
    blase("sprech", 540, 200, "me1", 900, 300, inhalt=["Das ist Kunst. Ich", "kritisiere ihre Politik."], textsize=32,
          figur=("ME_redet", GMX, BODEN, FH), bis="frage"),
    pl("Darf man Politiker als Tiere zeichnen?", 60, 40, "frage", fill=PINK, size=34),
    pl("Verletzt die Verurteilung die Kunstfreiheit von Meinrad?", 60, 116, beim("frage", "verletzt"), fill=WEISS, size=30),
    pl("Strauß-Karikatur · BVerfGE 75, 369", 60, 186, beim("klassiker", "Strauß"), fill=GELB, size=30),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_241(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=33, zeilenabstand=1.28)
        els += e; y += 16
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_241("sv", [
    "Der Karikaturist Meinrad zeichnet für ein Satiremagazin die Ministerpräsidentin Achenbach als Schwein, in einer "
    "sexuell herabwürdigenden Pose. Seine Botschaft: Sie mache Politik für Bauinvestoren. Die Redakteurin Henriette "
    "druckt die Karikatur: „Satire darf alles.“",
    "Die Ministerpräsidentin stellt Strafantrag. Das Amtsgericht verurteilt Meinrad wegen Beleidigung (§ 185 StGB).",
    "Meinrad beruft sich auf die Kunstfreiheit: Seine Zeichnung sei Kunst und kritisiere ihre Politik.",
], "Verletzt die Verurteilung Meinrad in seinem Grundrecht aus Art. 5 Abs. 3 Satz 1 GG?")

# ===========================================================================================================================
# C1 I. Schutzbereich: Wortlautkarte Art. 5 Abs. 3 Satz 1 GG; Karikatur ist Kunst (BVerfGE 75, 369 <377>)
# ===========================================================================================================================
PI = "I. Schutzbereich"
W53 = ["„(3) Kunst und Wissenschaft, Forschung und Lehre sind frei. …“"]
w53, w53_y = wortlaut(80, 175, 1100, W53, "Art. 5 Abs. 3 Satz 1 GG", "a53", marken=[
    (0, "Kunst", beim("a53", "Kunst")), (0, "frei", beim("a53", "frei"))], size=32)
folie([("a53", f"{PI} · Art. 5 Abs. 3 Satz 1 GG"), ("kunst", f"{PI} › Ist eine Karikatur Kunst?"),
       ("beleg", f"{PI} › Karikatur ist Kunst (+)"), ("v160", f"{PI} › Kunstbegriffe: Folge zum Mephisto-Beschluss")], [
    *tafel("a53", "I. Schutzbereich: die Kunstfreiheit"),
    *w53,
    z("Ist eine Karikatur Kunst?", 110, w53_y + 36, "kunst", "Bold", 36),
    blk(110, w53_y + 100, 1040, 210, BLAUHELL, beim("beleg", "Gericht"),
        [("„das geformte Ergebnis einer freien schöpferischen", "Regular", 31, INK),
         ("Gestaltung, in welcher [der Zeichner] seine Eindrücke,", "Regular", 31, INK),
         ("Erfahrungen und Erlebnisse zu unmittelbarer", "Regular", 31, INK),
         ("Anschauung bringt“", "Regular", 31, INK)]),
    *plusminus("Die Karikatur ist Kunst", 110, w53_y + 330, beim("beleg", "Gericht"), True, size=36, stil="ExtraBold"),
    zit("BVerfGE 75, 369 <377>", 640, w53_y + 340, beim("beleg", "Gericht")),
    zit("Formaler, materieller, offener Kunstbegriff: Folge zum Mephisto-Beschluss", 110, w53_y + 410, "v160"),
    *requisit([("a53", ("tabler", "palette", 110, GELB), "Kunstfreiheit", GELB),
               ("kunst", ("tabler", "pencil", 110, GELB), "Karikatur?", PINK),
               (beim("beleg", "Gericht"), ("tabler", "brush", 110, BLAUHELL), "Kunst (+)", HELLGRUEN),
               ("v160", ("tabler", "book", 120, WEISS), "Folge Mephisto", WEISS)]),
    *stehend("ME", FX, [("a53", "ruhig"), ("kunst", "denkt"), (beim("beleg", "Gericht"), "froh")]),
])

# ===========================================================================================================================
# C2 Niveaukontrolle, Kunst und Meinung (Art. 5 Abs. 1 nur Abgrenzung), II. Eingriff (<377>)
# ===========================================================================================================================
PII = "II. Eingriff"
folie([("niveau", f"{PI} › keine Niveaukontrolle"), ("meinung", f"{PI} › zugleich eine Meinung"),
       ("spez", f"{PI} › Art. 5 Abs. 3 GG als spezielle Norm"), ("v238", f"{PI} › Abgrenzung zu Art. 5 Abs. 1 GG"),
       ("eingriff", f"{PII} · Verurteilung wegen Beleidigung (+)")], [
    *tafel("niveau", "Kunst, Meinung und Eingriff"),
    z("gut oder geschmacklos: spielt keine Rolle", 110, 175, "niveau", "Bold", 34),
    *neinz2("Niveaukontrolle = unzulässige Inhaltskontrolle", 225, beim("niveau", "Niveaukontrolle"),
            beim("niveau", "unzulässige"), size=34, x=160),
    zit("BVerfGE 75, 369 <377>", 160, 273, beim("niveau", "unzulässige")),
    z("Meinrad äußert zugleich eine Meinung.", 110, 335, "meinung", "Bold", 34),
    *okz("Kunst und Meinungsäußerung schließen sich nicht aus", 383, "nausschl", size=33, x=160),
    blk(110, 445, 1040, 80, GELB, "spez", [("maßgeblich: Art. 5 Abs. 3 GG als spezielle Norm", "ExtraBold", 34, INK)]),
    zit("BVerfGE 75, 369 <377>; BVerfGE 30, 173 <200>", 110, 537, "spez"),
    zit("Meinungsfreiheit, Schranken aus Art. 5 Abs. 2 GG: Folge zu „Soldaten sind Mörder“", 110, 577, "v238"),
    linienzug([(110, 640), (1150, 640)], "eingriff", breite=3),
    *plusminus("II. Eingriff: Verurteilung wegen Beleidigung", 110, 665, "eingriff", True, size=36, stil="ExtraBold"),
    *requisit([("niveau", ("tabler", "brush", 110, WEISS), "keine Niveaukontrolle", WEISS),
               ("meinung", ("tabler", "message-circle", 110, WEISS), "Meinung", BLAUHELL),
               ("spez", ("tabler", "palette", 110, GELB), "Art. 5 Abs. 3 GG", GELB),
               ("eingriff", ("tabler", "gavel", 120, HOLZ), "Eingriff (+)", HELLROT)], px=1560),
    *paar("ME", [("niveau", "ruhig"), ("meinung", "froh"), ("eingriff", "sorge")],
          "HE", [("niveau", "froh"), ("spez", "ruhig"), ("eingriff", "denkt")]),
])

# ===========================================================================================================================
# D III. Rechtfertigung: vorbehaltlos, kollidierendes Verfassungsrecht, APR, Wortlautkarte Art. 1 Abs. 1 GG, § 185 StGB
# (BVerfGE 30, 173 <191, 193>; BVerfGE 75, 369 <378–380>)
# ===========================================================================================================================
PIII = "III. Rechtfertigung"
W11 = ["„(1) Die Würde des Menschen ist unantastbar. …“"]
w11, w11_y = wortlaut(80, 440, 1100, W11, "Art. 1 Abs. 1 Satz 1 GG", "a11",
                      marken=[(0, "Würde des Menschen", beim("a11", "Würde")), (0, "unantastbar", beim("a11", "unantastbar"))], size=32)
folie([("vorb", f"{PIII} · kein Gesetzesvorbehalt"), ("kolli", f"{PIII} › kollidierendes Verfassungsrecht"),
       ("apr", f"{PIII} › allgemeines Persönlichkeitsrecht"), ("a11", f"{PIII} › Kern: Art. 1 Abs. 1 GG"),
       ("p185", f"{PIII} › § 185 StGB schützt die Ehre"), ("licht", f"{PIII} › Auslegung im Licht der Kunstfreiheit")], [
    *tafel("vorb", "III. Rechtfertigung: Schranken"),
    *neinz2("Gesetzesvorbehalt: keiner", 172, "vorb", beim("vorb", "nicht"), "Bold", 34),
    zit("BVerfGE 30, 173 <191, 193>", 185, 220, beim("vorb", "nicht")),
    *okz("Grenzen: nur kollidierendes Verfassungsrecht", 268, "kolli", "Bold", 34),
    blk(110, 330, 1040, 90, PINK, "apr", [("allgemeines Persönlichkeitsrecht,", "ExtraBold", 33, INK),
                                       ("Art. 2 Abs. 1 i. V. m. Art. 1 Abs. 1 GG", "ExtraBold", 31, INK)]),
    *w11,
    *okz("§ 185 StGB schützt die Ehre, gilt auch gegenüber der Kunst", w11_y + 28, "p185", size=32, x=160),
    z("ausgelegt im Licht der Kunstfreiheit", 160, w11_y + 74, "licht", "Bold", 34),
    zit("BVerfGE 75, 369 <378 f.>", 160, w11_y + 122, "licht"),
    *requisit([("vorb", ("tabler", "shield-check", 110, GELB), "vorbehaltlos", GELB),
               ("apr", ("tabler", "fingerprint", 110, PINK), "Persönlichkeitsrecht", PINK),
               ("a11", ("tabler", "shield-check", 110, WEISS), "Menschenwürde", WEISS),
               ("p185", ("tabler", "gavel", 120, HOLZ), "§ 185 StGB", HELLROT)], px=1560),
    *stehend("AC", FX, [("vorb", "ruhig"), ("apr", "ernst"), ("licht", "denkt")]),
])

# ===========================================================================================================================
# E Der echte Fall (BVerfGE 75, 369 <369–371, 376>) – ohne Figuren, keine Karikatur, nur neutrale Icons
# ===========================================================================================================================
PS_ = "Strauß-Karikatur"
folie([("echt", f"{PS_} · der echte Fall"), ("echt1", f"{PS_} › die Karikaturen"), ("olg", f"{PS_} › Schuldspruch"),
       ("vb", f"{PS_} › Verfassungsbeschwerde")], [
    boden("echt"),
    pl("Strauß-Karikatur · BVerfG, 3.6.1987 · 1 BvR 313/85 · BVerfGE 75, 369", 70, 40, "echt", fill=GELB, size=30),
    pl("Zeitschrift: der damalige bayerische Ministerpräsident, mehrfach als Schwein", 70, 118,
       beim("echt1", "Zeitschrift"), fill=WEISS, size=30),
    pl("in ähnlichen Posen, dazu Schweine in Richterrobe", 70, 188, "robe", fill=WEISS, size=30),
    pl("OLG: schuldig der Beleidigung in 3 Fällen (§ 185 StGB)", 70, 258, "olg", fill=HELLROT, size=30),
    pl("Verfassungsbeschwerde: Art. 5 Abs. 3 Satz 1 GG", 70, 328, "vb", fill=HELL, size=30),
    zit("BVerfGE 75, 369 <369–371, 376>", 80, 400, "vb"),
    ficon("tabler", "calendar-event", 260, BODEN, 150, "echt", fuell=WEISS),
    ficon("ph", "newspaper", 640, BODEN, 190, beim("echt1", "Zeitschrift"), fuell=WEISS),
    ficon("tabler", "pencil", 1010, BODEN, 160, beim("echt1", "Schwein"), fuell=GELB),
    ficon("tabler", "gavel", 1380, BODEN, 170, "olg", fuell=HOLZ),
    ficon("tabler", "scale", 1700, BODEN, 160, "vb", fuell=WEISS),
])

# ===========================================================================================================================
# F Deutung: Aussagekern und Einkleidung (BVerfGE 75, 369 <377 f.>)
# ===========================================================================================================================
PD = "Deutung"
WAK = ["„Dieser Aussagekern und seine Einkleidung sind sodann",
       "gesondert daraufhin zu überprüfen, ob sie eine Kundgabe",
       "der Mißachtung gegenüber der karikierten Person enthalten.“"]
wak, wak_y = wortlaut(80, 420, 1100, WAK, "BVerfGE 75, 369 <378>", "gesond", marken=[
    (1, "gesondert", beim("gesond", "gesondert")), (2, "Mißachtung", beim("gesond", "Missachtung"))], size=31)
folie([("deut", f"{PD} · Wie prüft man Satire?"), ("verfr", f"{PD} › Übertreibung und Verfremdung"),
       ("kern", f"{PD} › Aussagekern"), ("einkl", f"{PD} › Einkleidung"), ("gesond", f"{PD} › gesondert prüfen"),
       ("milde", f"{PD} › Einkleidung: weniger strenger Maßstab")], [
    *tafel("deut", "Satire deuten: Kern und Einkleidung"),
    z("Übertreibungen, Verzerrungen, Verfremdungen", 110, 172, "verfr", "Bold", 34),
    z("zuerst das satirische Gewand ausziehen:", 110, 222, "entkl", size=34),
    blk(110, 285, 505, 110, BLAUHELL, "kern", [("Aussagekern", "ExtraBold", 34, INK),
                                            ("der eigentliche Inhalt", "Regular", 31, INK)]),
    blk(645, 285, 505, 110, LILAHELL, "einkl", [("Einkleidung", "ExtraBold", 34, INK),
                                             ("das satirische Gewand", "Regular", 31, INK)]),
    *wak,
    blk(110, wak_y + 25, 1040, 80, GELB, "milde", [("Einkleidung: weniger strenger Maßstab", "ExtraBold", 34, INK)]),
    zit("BVerfGE 75, 369 <377 f.>", 110, wak_y + 117, "milde"),
    *requisit([("deut", ("tabler", "zoom-question", 110, WEISS), "Satire deuten", WEISS),
               ("kern", ("tabler", "search", 110, BLAUHELL), "Aussagekern", BLAUHELL),
               ("einkl", ("tabler", "masks-theater", 120, LILAHELL), "Einkleidung", LILAHELL),
               ("milde", ("tabler", "scale", 120, GELB), "milderer Maßstab", GELB)], px=1560),
    *paar("ME", [("deut", "ruhig"), ("kern", "denkt"), ("milde", "froh")],
          "HE", [("deut", "denkt"), ("einkl", "ruhig"), ("milde", "froh")]),
])

# ===========================================================================================================================
# G1 Echter Fall: Kern und Einkleidung, Entwertung als Person (BVerfGE 75, 369 <379–381>)
# ===========================================================================================================================
WEN = ["„Gerade die Darstellung sexuellen Verhaltens, … sollte",
       "den Betroffenen als Person entwerten, ihn seiner Würde",
       "als Mensch entkleiden.“"]
wen, wen_y = wortlaut(80, 450, 1100, WEN, "BVerfGE 75, 369 <380>", "entw", marken=[
    (1, "als Person entwerten", beim("entw", "Person")), (1, "seiner Würde", beim("entw", "Würde"))], size=31)
folie([("kern1", f"{PS_} › Aussagekern"), ("einkl1", f"{PS_} › Einkleidung"),
       ("entw", f"{PS_} › Entwertung als Person"), ("oeff", f"{PS_} › Politiker: personale Würde bleibt")], [
    *tafel("kern1", "Strauß-Karikatur: Kern und Einkleidung"),
    blk(110, 172, 1040, 110, BLAUHELL, "kern1", [("Aussagekern: Er mache sich die Justiz", "ExtraBold", 33, INK),
                                              ("in anstößiger Weise zunutze.", "Regular", 31, INK)]),
    blk(110, 300, 1040, 80, LILAHELL, "einkl1", [("Einkleidung: als Schwein bei sexuellem Verhalten", "ExtraBold", 32, INK)]),
    zit("BVerfGE 75, 369 <379>", 110, 392, "einkl1"),
    *wen,
    *okz("Politiker: mehr Kritik, aber personale Würde bleibt", wen_y + 28, "oeff", "Bold", 32, x=160),
    zit("BVerfGE 75, 369 <379–381>", 160, wen_y + 76, "oeff"),
    *requisit([("kern1", ("tabler", "search", 110, BLAUHELL), "Aussagekern", BLAUHELL),
               ("einkl1", ("tabler", "masks-theater", 120, LILAHELL), "Einkleidung", LILAHELL),
               ("entw", ("tabler", "shield-check", 110, PINK), "Würde als Mensch", PINK),
               ("oeff", ("tabler", "podium", 120, WEISS), "Politiker", WEISS)], px=1560),
    *stehend("AC", FX, [("kern1", "ruhig"), ("einkl1", "ernst"), ("oeff", "denkt")]),
])

# ===========================================================================================================================
# G2 Menschenwürde: keine Abwägung; Ergebnis (BVerfGE 75, 369 <369 Leitsatz, 376, 380>)
# ===========================================================================================================================
WAB = ["„Soweit das allgemeine Persönlichkeitsrecht allerdings",
       "unmittelbarer Ausfluß der Menschenwürde ist, wirkt diese",
       "Schranke absolut ohne die Möglichkeit eines Güterausgleichs.“"]
wab, wab_y = wortlaut(80, 300, 1100, WAB, "BVerfGE 75, 369 <380>", "absolut", marken=[
    (1, "Menschenwürde", beim("absolut", "Menschenwürde")), (2, "absolut", beim("absolut", "absolut")),
    (2, "Güterausgleichs", beim("absolut", "Güterausgleichs"))], size=31)
folie([("abw", f"{PS_} › sonst: Abwägung"), ("absolut", f"{PS_} › Menschenwürde: absolute Schranke"),
       ("erg", f"{PS_} · Ergebnis: Verurteilung verfassungsgemäß")], [
    *tafel("abw", "Menschenwürde: keine Abwägung"),
    z("sonst: Abwägung, kein genereller Vorrang", 110, 172, "abw", "Bold", 34),
    z("des Persönlichkeitsrechts vor der Kunst", 110, 218, beim("abw", "generellen"), "Bold", 34),
    *wab,
    blk(110, wab_y + 30, 1040, 80, GRUEN, "erg", [("Verurteilung wegen Beleidigung: verfassungsgemäß", "ExtraBold", 32, INK)]),
    blk(110, wab_y + 128, 1040, 80, WEISS, "zurueck", [("Verfassungsbeschwerde zurückgewiesen", "ExtraBold", 32, INK)]),
    zit("BVerfGE 75, 369, Leitsatz; Entscheidungsformel; <376, 380>", 110, wab_y + 222, "zurueck"),
    *requisit([("abw", ("tabler", "scale", 120, WEISS), "Abwägung", WEISS),
               ("absolut", ("tabler", "shield-check", 110, PINK), "absolute Schranke", PINK),
               ("erg", ("tabler", "gavel", 120, HOLZ), "Verurteilung hält", GRUEN)], px=1560),
    *stehend("ME", FX, [("abw", "ruhig"), ("absolut", "sorge"), ("erg", "ernst")]),
])

# ===========================================================================================================================
# H Zurück zum Fall (Schauplatz Amtsgericht wie A3: die Geschichte kehrt zum Ausgangsfall zurück)
# ===========================================================================================================================
folie([("zur", "Zurück zu Meinrad · die Lösung"), ("zk", "Zurück zu Meinrad › Aussagekern: zulässige Kritik"),
       ("ze", "Zurück zu Meinrad › Einkleidung: Entwertung als Person"), ("zm", "Zurück zu Meinrad › Menschenwürde"),
       ("zv", "Zurück zu Meinrad › Verurteilung hält")], [
    *gericht("zur"),
    hart(ficon("tabler", "gavel", RB_X + RB_W / 2, BODEN - RB_H + 6, 130, "zur", fuell=HOLZ, anim="cut")),
    *fig("ME", GMX, BODEN, FH, [("zur", "ruhig"), ("zk", "froh"), ("ze", "sorge"), ("zv", "ernst")], erst="cut"),
    hart(ns("Meinrad", GMX, BODEN, "zur", LILA)),
    *fig("AC", GAX, BODEN, FH, [("zur", "ernst"), ("zk", "denkt"), ("zv", "ruhig")], erst="cut"),
    hart(ns("Ministerpräsidentin Achenbach", GAX, BODEN, "zur", BLAU)),
    *okz2("Aussagekern: Politik für Bauinvestoren", 50, "zk", beim("zk", "scharfe"), "Bold", 32, x=110, rechts=1880),
    z("scharfe politische Kritik: muss sie aushalten", 110, 96, beim("zk", "scharfe"), size=32, rechts=1880),
    *neinz2("Einkleidung: soll sie als Person entwerten", 160, "ze", beim("ze", "entwerten"), "Bold", 32, x=110, rechts=1880),
    pl("trifft den Kern ihrer Menschenwürde", 60, 226, "zm", fill=PINK, size=32),
    pl("Verurteilung nach § 185 StGB verletzt die Kunstfreiheit nicht", 60, 306, "zv", fill=GELB, size=32),
])

# ===========================================================================================================================
# I Gegenfall: der Fuchs (BVerfGE 75, 369 <378, 379>) – zurück in der Redaktion
# ===========================================================================================================================
folie([("gegen", "Gegenfall · Nie als Tiere zeichnen?"), ("me2", "Gegenfall · Meinrad zeichnet einen Fuchs"),
       ("ueblich", "Gegenfall › übliche Karikatur"), ("abw2", "Gegenfall › Abwägung, milderer Maßstab")], [
    boden("gegen"), pinnwand("gegen"), zeichentisch("gegen"),
    szene(blattbild("fluent-emoji-high-contrast", "fox", beim("fuchs", "Fuchs"), ORANGE), "241stift*", 0.8, -0.1),
    hart(pl("Satiremagazin · Redaktion", 1660, 740, "gegen", fill=WEISS, size=28, anker="m", anim="cut")),
    pl("Nie als Tiere zeichnen? Das folgt daraus nicht.", 60, 40, "gegen", fill=PINK, size=30),
    pl("Fuchs: überspitzt einen Charakterzug", 60, 104, beim("fuchs", "überspitzt"), fill=WEISS, size=30),
    pl("übliche Karikatur: Tiergestalt allein greift die Würde nicht an", 60, 168, "ueblich", fill=HELLGRUEN, size=30),
    pl("Abwägung, milderer Maßstab für die Einkleidung", 60, 232, "abw2", fill=GELB, size=30),
    *fig("ME", MEX, BODEN, FH, [("gegen", "denkt_r")], bis="me2", erst="cut"),
    *redet("ME_redet_r", MEX, BODEN, FH, "me2", "fuchs"),
    *fig("ME", MEX, BODEN, FH, [("fuchs", "zeichnet_r"), ("ueblich", "froh_r")], erst="cut"),
    hart(ns("Meinrad", MEX, BODEN, "gegen", LILA)),
    *fig("HE", HEX, BODEN, FH, [("gegen", "ruhig"), ("fuchs", "froh")], erst="cut"),
    hart(ns("Henriette", HEX, BODEN, "gegen", GRUEN)),
    blase("sprech", 560, 190, "me2", 820, 330, inhalt=["Dann zeichne ich sie", "eben als Fuchs."], textsize=32,
          figur=("ME_redet_r", MEX, BODEN, FH), bis="fuchs"),
    zit("BVerfGE 75, 369 <378, 379>", 70, 300, "ueblich"),
])

# ===========================================================================================================================
# J Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Art. 5 Abs. 3 statt Abs. 1 GG"), ("t2", "Klausurtipp · Kern und Einkleidung trennen"),
       ("t3", "Klausurtipp · Menschenwürde nicht vorschnell")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Meinung im Kunstwerk:", 200, 200, "tipp", "Bold", 36),
    *okz2("Art. 5 Abs. 3 GG prüfen, nicht Abs. 1", 255, "tipp", beim("tipp", "Artikel"), size=34, x=200),
    *neinz("keine Schranken aus Art. 5 Abs. 2 GG", 305, "t1", size=34, x=200),
    linienzug([(130, 380), (1130, 380)], "t2", breite=3),
    *okz("Aussagekern und Einkleidung trennen,", 405, "t2", "Bold", 34, x=200),
    z("beide gesondert prüfen", 200, 451, beim("t2", "prüfe"), "Bold", 34),
    blk(130, 525, 1000, 120, GELB, "t3", [("Menschenwürde nicht vorschnell:", "ExtraBold", 34, INK),
                                       ("nur dann entfällt die Abwägung", "ExtraBold", 34, INK)]),
    zit("BVerfGE 75, 369 <377 f., 380>; BVerfGE 30, 173 <191>", 200, 660, beim("t3", "Nur")),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# K Prüfschema
# ===========================================================================================================================
REIHEN = [("k1", 0, "I. Schutzbereich: die Karikatur als Kunst", True),
          ("k2", 0, "II. Eingriff durch die Verurteilung", True),
          ("k3", 0, "III. Rechtfertigung", True),
          ("k3a", 1, "1. kollidierendes Verfassungsrecht: § 185 StGB zum Schutz des Persönlichkeitsrechts", False),
          ("k3b", 1, "2. Deutung: Aussagekern und Einkleidung", False),
          ("k3c", 1, "3. Abwägung, außer bei einem Angriff auf die Menschenwürde", False)]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfschema: Kunstfreiheit bei Satire, Art. 5 Abs. 3 Satz 1 GG"), 110, 90, "sch", 46)]
y = 230
for c, ebene, text, fett in REIHEN:
    x = (130, 200)[ebene]
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 42 if ebene == 0 else 36, rechts=1820))
    y += {0: 100, 1: 92}[ebene]
assert y <= 970, y
folie([("sch", "Prüfschema"), ("k1", "Prüfschema › I. Schutzbereich"), ("k2", "Prüfschema › II. Eingriff"),
       ("k3", "Prüfschema › III. Rechtfertigung"), ("k3a", "Prüfschema › III. 1. kollidierendes Verfassungsrecht"),
       ("k3b", "Prüfschema › III. 2. Deutung"), ("k3c", "Prüfschema › III. 3. Abwägung")], els_sch)

# ===========================================================================================================================
# L Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Satire darf ", 0), ("übertreiben", "a"), (" und", 0)],
                 [("verfremden, auch in Tiergestalt.", 0)]], 750, 300, 44, "merke",
                {"a": beim("merke", "übertreiben")}),
    *markertext([[("Wer aber einen Menschen als Person", 0)], [("entwertet, trifft seine ", 0), ("Würde", "b"), (",", 0)],
                 [("und dort endet die Kunstfreiheit.", 0)]], 750, 500, 44, "m2",
                {"b": beim("m2", "Würde")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
