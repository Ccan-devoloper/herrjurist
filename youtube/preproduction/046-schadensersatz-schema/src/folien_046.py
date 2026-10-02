"""Folge 046 · Schadensersatz Schema: Das System der §§ 280 ff. BGB – Serienstandard Open Peeps (Katzenkönig).
Beispielfall (Plan-Hook): Gisela kauft beim Elektrohändler Kranz eine Waschmaschine; Kranz liefert eine Woche zu spät
(Waschsalon 30 €), stößt die Maschine beim Ausladen an (Schlauch gerissen), beim ersten Waschgang flutet Wasser das Bad
und den Parkettboden im Flur (1.500 €); nach erfolgloser Frist Reparatur in einer Werkstatt (200 €).
Szenen laut ../SZENENPLAN.md: A1 Der Kauf, A2 Die Verspätung, A3 Die Lieferung, A4 Das Bad, A5 Frist und Werkstatt,
A6 Die Frage, B Sachverhalt, C Wortlaut § 280 I, D Wortlaut § 280 II, III, E1 Drei Arten, E2 Kontrollfrage,
F1/F2 A. Wasserschaden (neben der Leistung), G1/G2 B. Waschsalon (Verzögerungsschaden, Verzug), H1/H2 C. Reparatur
(statt der Leistung, Wortlaut § 281 I 1), I1 § 282, I2 §§ 283, 311a II, J Klausurtipp (Lexi), K Klausurschema als
Entscheidungsbaum, L Merksatz (Lexi).
Geräusche nur bei sichtbarer Handlung (Stoß der Maschine gegen die Treppe, auslaufendes Wasser; Freesound CC0, Herkunft in
../geraeusche_herkunft.json). Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/
wortlaut/redet/fig/ns wie in Folge 037 (eigene Kopie, gemeinsame Dateien unverändert)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_046/"

FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
ZITAT = (246, 246, 250, 255)
GRAU = (176, 178, 190, 255)
WASSER = (141, 179, 242, 255)
DAUER = bausteine._cj()["dauer"]
T_ = bausteine._t

_CMAP = set(TTFont(SP + "humaaans/fonts/Nunito[wght].ttf").getBestCmap())


def glyphen(text):
    """Nunito muss jedes Zeichen haben (sonst Kästchen)."""
    fehl = {c for c in text if ord(c) not in _CMAP and not c.isspace()}
    assert not fehl, f"Zeichen fehlt in Nunito: {fehl} in {text!r}"
    return text


def z(text, x, y, cue, stil="Regular", size=36, farbe=INK, d=0.0, rechts=1170, **k):
    """Tafelzeile, die rechts nicht über die Karte hinausragen darf."""
    e = zeile(glyphen(text), x, y, cue, stil, size, farbe=farbe, d=d, **k)
    assert e.x + e.sprite.width <= rechts, f"Zeile zu breit: {text} ({e.x + e.sprite.width:.0f} > {rechts})"
    return e


def pl(text, *a, **k):
    return pille(glyphen(text), *a, **k)


def tafel(cue, titel_, h=840, fill=WEISS, size=46):
    """Rechtstafel links, rechts bleibt Platz für die Figuren."""
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(glyphen(titel_), 110, 100, cue, size)]


def blk(x, y, w, h, fill, cue, zeilen, **k):
    for t, s, g, f in zeilen:
        assert F(s, g).getlength(glyphen(t)) <= w - 30, f"Blockzeile zu breit: {t}"
    # wie fl_block(), aber Zeilenabstand nach der tatsächlichen Schriftgröße (fl_block nimmt 64 px an)
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


def gedreht(e, winkel):
    """Requisit leicht gekippt (Stoß), Unterkante und Mitte bleiben."""
    cx, unten = e.x + e.sprite.width / 2, e.y + e.sprite.height
    e.sprite = e.sprite.rotate(winkel, resample=Image.BICUBIC, expand=True)
    e.sprite = e.sprite.crop(e.sprite.getbbox())
    e.x, e.y = int(cx - e.sprite.width / 2), int(unten - e.sprite.height)
    return e


def lexi_bis_ende(cue):
    return (cue, round(DAUER - T_(cue) - 0.05, 3))


def zit(text, x, y, cue, size=26):
    """Fundstellenzeile (grau, klein)."""
    return z(text, x, y, cue, size=size, farbe=TEXT)


def rechts_frei(els, x0=1250):
    """Figuren und Requisiten der Tafelfolien stehen rechts der Tafel."""
    for e in els:
        n = e.name or ""
        if n.startswith(("bild:", "ficon:")) or "/op_046/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def wortlaut(x, y, w, zeilen, quelle, cue, marken=(), size=34, bis=None):
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de, als Zitat mit Normangabe;
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


# --- Eigene Hilfsfunktion (wie Folge 031/037): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt -------------
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


def gi(cx, unten, hoehe, folge, **k):
    return fig("GI", cx, unten, hoehe, folge, **k)


def kr(cx, unten, hoehe, folge, **k):
    return fig("KR", cx, unten, hoehe, folge, **k)


BODEN, FH = 880, 480
X1, X2 = 1420, 1720                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
GI_F, KR_F = LILA, BLAU                     # Farben der Namensschilder
HOLZ = (232, 205, 160, 255)
MASCH = WEISS                               # Waschmaschine (weiß)


def boden(cue, hart_=False):
    e = linienzug([(40, BODEN), (1880, BODEN)], cue, breite=7, farbe=INK)
    return hart(e) if hart_ else e


# A1 Fall: Der Kauf -------------------------------------------------------------------------------------------------------
GIA, KRA = 480, 1440
folie([(NULL, "Fall · Der Kauf")], [
    hart(pl("Elektrohandel Kranz", 70, 40, NULL, fill=BLAU, size=44)),
    boden(NULL, True),
    hart(ficon("tabler", "building-store", 1720, 300, 150, NULL, fuell=BLAU)),
    hart(peep_voll("GI_froh_r", GIA, BODEN, FH, NULL)), hart(ns("Gisela", GIA, BODEN, NULL, GI_F)),
    hart(peep_voll("KR_froh", KRA, BODEN, FH, NULL)), hart(ns("Herr Kranz, Elektrohändler", KRA, BODEN, NULL, KR_F)),
    ficon("tabler", "wash-machine", 880, BODEN - 2, 220, beim("fall", "Waschmaschine"), fuell=MASCH),
    pl("Waschmaschine", 880, 560, beim("fall", "Waschmaschine"), fill=WEISS, size=30, anker="m"),
    ficon("tabler", "calendar-event", 880, 300, 120, beim("termin", "Lieferung"), fuell=GELB),
    pl("Lieferung und Anschluss: 2. März", 880, 330, beim("termin", "zweiten"), fill=GELB, size=32, anker="m"),
])

# A2 Fall: Die Verspätung ------------------------------------------------------------------------------------------------------
GIB = 560
WSCH = beim("salon", "wäscht")
folie([("warten", "Fall · Die Verspätung")], [
    pl("Gisela wartet", 70, 40, "warten", fill=LILA, size=44),
    boden("warten"),
    ficon("tabler", "calendar-x", 1100, 330, 130, "warten", fuell=GELB, bis=WSCH),
    pl("2. März", 1100, 360, "warten", fill=GELB, size=30, anker="m", bis=WSCH),
    pl("Termin vergessen", 1100, 450, beim("warten", "vergisst"), fill=ROT, size=32, anker="m", bis=WSCH),
    pl("erst eine Woche später", 1100, 540, beim("warten", "Woche"), fill=WEISS, size=32, anker="m", bis=WSCH),
    *gi(GIB, BODEN, FH, [("warten", "sorge_r"), (WSCH, "ernst_r")]),
    ns("Gisela", GIB, BODEN, "warten", GI_F),
    ficon("tabler", "basket", GIB + 230, BODEN - 4, 110, WSCH, fuell=GELB),
    ficon("tabler", "wash-machine", 1150, BODEN - 2, 200, beim("salon", "Waschsalon"), fuell=MASCH),
    ficon("tabler", "wash-machine", 1400, BODEN - 2, 200, beim("salon", "Waschsalon"), fuell=MASCH),
    pl("Waschsalon", 1275, 560, beim("salon", "Waschsalon"), fill=BLAU, size=34, anker="m"),
    pl("30 €", 1275, 440, beim("salon", "dreißig"), fill=GELB, size=34, anker="m"),
])

# A3 Fall: Die Lieferung ---------------------------------------------------------------------------------------------------------
KRC, GIC = 760, 1620
STOSS = beim("stoss", "stößt")
KR_RED = ("KR_redet_r", KRC, BODEN, FH)
folie([("k1", "Fall · Die Lieferung")], [
    pl("Eine Woche später", 70, 40, "k1", fill=LILA, size=44),
    boden("k1"),
    ficon("tabler", "truck-delivery", 300, BODEN - 2, 330, "k1", fuell=BLAU),
    ficon("tabler", "stairs", 1330, BODEN - 2, 230, "k1", fuell=HOLZ),
    *redet("KR_redet_r", KRC, BODEN, FH, "k1", "stoss"),
    *kr(KRC, BODEN, FH, [("stoss", "ernst_r"), (STOSS, "schreck_r")], erst="cut"),
    ns("Herr Kranz", KRC, BODEN, "k1", KR_F),
    blase("sprech", 640, 210, "k1", 1100, 250, inhalt=["Entschuldigung, ich hatte", "den Termin vergessen!"],
          textsize=36, figur=KR_RED, bis="stoss"),
    *gi(GIC, BODEN, FH, [("k1", "ernst"), (STOSS, "schreck")]),
    ns("Gisela", GIC, BODEN, "k1", GI_F),
    ficon("tabler", "wash-machine", 1040, BODEN - 2, 200, "stoss", fuell=MASCH, bis=STOSS),
    szene(gedreht(ficon("tabler", "wash-machine", 1130, BODEN - 2, 200, STOSS, fuell=MASCH, anim="cut"), -9),
          "046stoss*", 0.7, -0.03),
    pl("unachtsam", 1130, 470, beim("stoss", "unachtsam"), fill=ROT, size=32, anker="m"),
    pl("innen reißt ein Schlauch", 1130, 380, beim("stoss", "reißt"), fill=WEISS, size=30, anker="m"),
])

# A4 Fall: Das Bad ----------------------------------------------------------------------------------------------------------------
GID = 1620
GI_RED = ("GI_redet", GID, BODEN, FH)
folie([("flut", "Fall · Das Bad")], [
    pl("Im Bad", 70, 40, "flut", fill=BLAU, size=44),
    boden("flut"),
    ficon("tabler", "bath", 420, BODEN - 2, 320, "flut", fuell=WEISS),
    ficon("tabler", "wash-machine", 820, BODEN - 2, 220, "flut", fuell=MASCH),
    ficon("tabler", "droplets", 980, 760, 90, beim("flut", "Wasser"), fuell=WASSER),
    szene(linienzug([(620, BODEN - 10), (1180, BODEN - 10)], beim("flut", "Wasser"), breite=14, farbe=WASSER),
          "046wasser*", 0.6, 0.0),
    pl("flutet das Bad", 620, 420, beim("flut", "flutet"), fill=BLAU, size=34, anker="m"),
    linienzug([(1180, BODEN - 10), (1420, BODEN - 10)], "parkett", breite=14, farbe=WASSER),
    ficon("tabler", "ripple", 1300, BODEN - 24, 120, "parkett", fuell=None),
    pl("Parkettboden im Flur", 1060, 560, "parkett", fill=HOLZ, size=30, anker="m"),
    pl("Schaden: 1.500 €", 1060, 640, beim("parkett", "tausendfünfhundert"), fill=ROT, size=32, anker="m"),
    *gi(GID, BODEN, FH, [("flut", "schreck")], bis="g1"),
    *redet("GI_redet", GID, BODEN, FH, "g1", "frist"),
    ns("Gisela", GID, BODEN, "flut", GI_F),
    blase("sprech", 560, 210, "g1", 1250, 250, inhalt=["Mein Bad steht", "unter Wasser!"], textsize=40, figur=GI_RED,
          bis="frist"),
])

# A5 Fall: Frist und Werkstatt ----------------------------------------------------------------------------------------------------
GIE = 520
folie([("frist", "Fall · Frist zur Reparatur")], [
    pl("Gisela verlangt die Reparatur", 70, 40, "frist", fill=LILA, size=44),
    boden("frist"),
    *gi(GIE, BODEN, FH, [("frist", "ernst_r"), ("still", "denkt_r"), ("werk", "froh_r")]),
    ns("Gisela", GIE, BODEN, "frist", GI_F),
    ficon("tabler", "calendar-event", 1050, 330, 120, beim("frist", "Frist"), fuell=GELB),
    pl("Frist: zwei Wochen", 1050, 360, beim("frist", "Frist"), fill=GELB, size=32, anker="m"),
    ficon("tabler", "phone-off", 1450, 330, 110, "still", fuell=WEISS),
    pl("Er meldet sich nicht.", 1450, 360, "still", fill=WEISS, size=30, anker="m"),
    ficon("tabler", "tool", 1250, BODEN - 4, 140, beim("werk", "Werkstatt"), fuell=GELB),
    ficon("tabler", "wash-machine", 1450, BODEN - 2, 200, "frist", fuell=MASCH),
    pl("Reparatur", 1450, 650, beim("frist", "Reparatur"), fill=WEISS, size=30, anker="m"),
    pl("Werkstatt", 1350, 560, beim("werk", "Werkstatt"), fill=GELB, size=32, anker="m"),
    pl("200 €", 1350, 470, beim("werk", "zweihundert"), fill=ROT, size=34, anker="m"),
])

# A6 Fall: Die Frage --------------------------------------------------------------------------------------------------------------
GIF, KRF = 380, 1560
folie([("frage", "Fall · Die Frage")], [
    boden("frage"),
    *gi(GIF, BODEN, FH, [("frage", "denkt_r")]), ns("Gisela", GIF, BODEN, "frage", GI_F),
    *kr(KRF, BODEN, FH, [("frage", "sorge")]), ns("Herr Kranz", KRF, BODEN, "frage", KR_F),
    pl("Drei Schäden", 960, 90, beim("frage", "Drei"), fill=WEISS, size=40, anker="m"),
    blk(660, 190, 600, 80, GELB, beim("frage", "Schäden"), [("Waschsalon: 30 €", "ExtraBold", 34, INK)]),
    blk(660, 290, 600, 80, BLAU, beim("frage", "Schäden"), [("Wasserschaden: 1.500 €", "ExtraBold", 34, INK)]),
    blk(660, 390, 600, 80, ROT, beim("frage", "Schäden"), [("Reparatur: 200 €", "ExtraBold", 34, INK)]),
    pl("ein Händler", 960, 500, beim("frage", "Händler"), fill=BLAU, size=32, anker="m"),
    pl("Welcher Schaden gehört zu welcher Anspruchsgrundlage?", 960, 610, "frage2", fill=PINK, size=32, anker="m"),
    ficon("tabler", "scale", 960, 850, 120, beim("frage2", "Anspruchsgrundlage"), fuell=WEISS),
])

# B Sachverhalt --------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Gisela kauft für ihre Wohnung beim Elektrohändler Kranz eine Waschmaschine. Vereinbart sind Lieferung und Anschluss "
    "am 2. März. Herr Kranz vergisst den Termin und kommt erst eine Woche später; bis dahin zahlt Gisela 30 Euro im "
    "Waschsalon.",
    "Beim Ausladen stößt Herr Kranz die Maschine unachtsam gegen die Treppe; innen reißt ein Schlauch. Beim ersten "
    "Waschgang flutet auslaufendes Wasser das Bad, der Parkettboden im Flur quillt auf (Schaden 1.500 Euro).",
    "Gisela verlangt die Reparatur und setzt eine Frist von zwei Wochen. Herr Kranz meldet sich nicht. Eine Werkstatt "
    "repariert die Maschine für 200 Euro.",
], "Welche Ansprüche hat Gisela gegen Herrn Kranz?")

# C Wortlaut § 280 Abs. 1 BGB ---------------------------------------------------------------------------------------------------
W280 = ["„Verletzt der Schuldner eine Pflicht aus dem Schuldverhältnis, so",
        "kann der Gläubiger Ersatz des hierdurch entstehenden Schadens",
        "verlangen. Dies gilt nicht, wenn der Schuldner die Pflichtverletzung",
        "nicht zu vertreten hat.“"]
w280, w280_y = wortlaut(80, 180, 1100, W280, "§ 280 Abs. 1 BGB", "agl", marken=[
    (0, "Pflicht aus dem Schuldverhältnis", beim("w1", "Pflicht")),
    (1, "Ersatz des hierdurch entstehenden Schadens", beim("w1", "Ersatz")),
    (2, "Dies gilt nicht", "w1b"), (3, "nicht zu vertreten hat", beim("w1b", "nicht", nr=2))], size=31)
MY = w280_y + 40
folie([("agl", "Anspruchsgrundlage · § 280 Abs. 1 BGB"), ("grund", "§ 280 Abs. 1 BGB › Grundtatbestand"),
       ("verm", "§ 280 Abs. 1 Satz 2 BGB › Vertretenmüssen vermutet")], rechts_frei([
    *tafel("agl", "Zentrale Norm: § 280 BGB"),
    *w280,
    z("Grundtatbestand, vier Merkmale:", 110, MY, "grund", "Bold", 34),
    z("1. Schuldverhältnis", 150, MY + 55, "m1", size=33),
    z("2. Pflichtverletzung", 600, MY + 55, "m2", size=33),
    z("3. Vertretenmüssen", 150, MY + 105, "m3", size=33),
    z("4. Schaden", 600, MY + 105, beim("m4", "Schaden"), size=33),
    blk(110, MY + 170, 1040, 90, GELB, "verm", [("Vertretenmüssen vermutet: Schuldner muss sich entlasten", "ExtraBold", 32, INK)]),
    zit("§ 280 Abs. 1 Satz 2 BGB; BGH, Urt. v. 4.12.2014 – VII ZR 4/13, Rn. 59", 110, MY + 275, beim("verm", "Schuldner")),
    ficon("tabler", "scale", FX, 330, 140, "agl", fuell=WEISS),
    pl("§ 280 BGB", FX, 350, "agl", fill=WEISS, size=28, anker="m"),
    *gi(X1, FB, FR, [("agl", "ernst"), ("grund", "denkt")]), ns("Gisela", X1, FB, "agl", GI_F),
    *kr(X2, FB, FR, [("agl", "ruhig"), ("verm", "sorge")], d=0.2), ns("Herr Kranz", X2, FB, "agl", KR_F, d=0.2),
]))

# D Wortlaut § 280 Abs. 2 und 3 BGB -----------------------------------------------------------------------------------------------
W2 = ["„Schadensersatz wegen Verzögerung der Leistung kann der Gläubiger",
      "nur unter der zusätzlichen Voraussetzung des § 286 verlangen.“"]
W3 = ["„Schadensersatz statt der Leistung kann der Gläubiger nur unter den",
      "zusätzlichen Voraussetzungen des § 281, des § 282 oder des § 283",
      "verlangen.“"]
w2, w2_y = wortlaut(80, 180, 1100, W2, "§ 280 Abs. 2 BGB", "w2", marken=[
    (0, "Verzögerung der Leistung", beim("w2", "Verzögerung")),
    (1, "zusätzlichen Voraussetzung des § 286", beim("w2", "zusätzlichen"))], size=31)
w3, w3_y = wortlaut(80, w2_y + 40, 1100, W3, "§ 280 Abs. 3 BGB", "w3", marken=[
    (0, "statt der Leistung", beim("w3", "statt")),
    (1, "des § 281, des § 282 oder des § 283", beim("w3", "zweihunderteinundachtzig"))], size=31)
folie([("w2", "§ 280 Abs. 2 BGB › Verzögerung der Leistung"), ("w3", "§ 280 Abs. 3 BGB › Schadensersatz statt der Leistung")],
      rechts_frei([
    *tafel("w2", "§ 280 Abs. 2 und 3 BGB"),
    *w2, *w3,
    ficon("tabler", "hourglass", FX, 330, 110, "w2", fuell=GELB, bis="w3"),
    pl("Verzögerung", FX, 350, "w2", fill=GELB, size=28, anker="m", bis="w3"),
    ficon("tabler", "refresh", FX, 330, 120, "w3", fuell=WEISS),
    pl("statt der Leistung", FX, 350, "w3", fill=ORANGE, size=28, anker="m"),
    *gi(X1, FB, FR, [("w2", "ruhig"), ("w3", "denkt")]), ns("Gisela", X1, FB, "w2", GI_F),
    *kr(X2, FB, FR, [("w2", "ernst")], d=0.2), ns("Herr Kranz", X2, FB, "w2", KR_F, d=0.2),
]))

# E1 Drei Arten ------------------------------------------------------------------------------------------------------------------
folie([("drei", "System · drei Arten des Schadensersatzes")], rechts_frei([
    *tafel("drei", "Drei Arten des Schadensersatzes"),
    blk(110, 200, 1040, 150, GRUEN, "a1", [("Schadensersatz neben der Leistung", "ExtraBold", 38, INK),
                                          ("§ 280 Abs. 1 BGB", "Bold", 32, INK)]),
    blk(110, 390, 1040, 150, GELB, "a2", [("Verzögerungsschaden", "ExtraBold", 38, INK),
                                         ("§ 280 Abs. 1, 2, § 286 BGB", "Bold", 32, INK)]),
    blk(110, 580, 1040, 150, ORANGE, "a3", [("Schadensersatz statt der Leistung", "ExtraBold", 38, INK),
                                           ("§ 280 Abs. 1, 3, §§ 281, 282, 283 BGB", "Bold", 32, INK)]),
    *gi(X1, FB, FR, [("drei", "denkt"), ("a3", "ernst")]), ns("Gisela", X1, FB, "drei", GI_F),
    *kr(X2, FB, FR, [("drei", "ruhig")], d=0.2), ns("Herr Kranz", X2, FB, "drei", KR_F, d=0.2),
]))

# E2 Kontrollfrage -----------------------------------------------------------------------------------------------------------------
folie([("test", "System · Kontrollfrage")], rechts_frei([
    *tafel("test", "Die Kontrollfrage"),
    blk(110, 190, 1040, 140, GELB, beim("test", "ob"), [("Würde eine Nacherfüllung", "ExtraBold", 40, INK),
                                                       ("den Schaden beseitigen?", "ExtraBold", 40, INK)]),
    zit("BGH, Urt. v. 3.7.2013 – VIII ZR 169/12, Rn. 26 f.;", 110, 350, beim("test", "Bundesgerichtshof")),
    zit("BGH, Urt. v. 7.2.2019 – VII ZR 63/18, Rn. 17–19", 110, 385, beim("test", "Bundesgerichtshof")),
    ok(140, 480, "test2", gr=20), z("Wenn ja: Schadensersatz statt der Leistung", 185, 460, "test2", "Bold", 34),
    z("Schuldner bekommt zuerst eine letzte Gelegenheit", 225, 515, beim("test2", "letzte"), size=31),
    ok(140, 620, "test3", gr=20), z("Bleibt der Schaden: neben der Leistung", 185, 600, "test3", "Bold", 34),
    ficon("tabler", "tool", FX, 330, 130, beim("test", "Nacherfüllung"), fuell=GELB),
    pl("Nacherfüllung", FX, 350, beim("test", "Nacherfüllung"), fill=GELB, size=28, anker="m"),
    *gi(X1, FB, FR, [("test", "denkt"), ("test3", "froh")]), ns("Gisela", X1, FB, "test", GI_F),
    *kr(X2, FB, FR, [("test", "ruhig"), ("test2", "denkt")], d=0.2), ns("Herr Kranz", X2, FB, "test", KR_F, d=0.2),
]))

# F1 A. Wasserschaden: Zuordnung --------------------------------------------------------------------------------------------------
folie([("wass", "A. Wasserschaden (1.500 €) › Zuordnung"),
       ("wass2", "A. Wasserschaden › neben der Leistung, §§ 437 Nr. 3, 280 Abs. 1 BGB")], rechts_frei([
    *tafel("wass", "A. Der Wasserschaden: 1.500 €"),
    z("Würde eine Reparatur der Maschine", 110, 190, "wass1", "Bold", 34),
    z("den Parkettboden retten?", 110, 245, beim("wass1", "Parkettboden"), "Bold", 34),
    nein(140, 340, beim("wass1", "Nein"), gr=20), z("Nein.", 185, 320, beim("wass1", "Nein"), "Bold", 34),
    blk(110, 420, 1040, 100, GRUEN, "wass2", [("Schadensersatz neben der Leistung", "ExtraBold", 38, INK)]),
    z("Mangel: § 437 Nr. 3 BGB führt zu § 280 Abs. 1 BGB", 110, 570, "brueck", "Bold", 33),
    zit("BGH, Urt. v. 7.2.2019 – VII ZR 63/18, Leitsatz 1, Rn. 17 (Folgeschäden)", 110, 625, "brueck"),
    ficon("tabler", "droplets", FX, 330, 120, "wass", fuell=WASSER),
    pl("Parkett: 1.500 €", FX, 350, "wass", fill=BLAU, size=28, anker="m"),
    *gi(X1, FB, FR, [("wass", "sorge"), ("wass2", "ernst")]), ns("Gisela", X1, FB, "wass", GI_F),
    *kr(X2, FB, FR, [("wass", "sorge"), ("brueck", "ernst")], d=0.2), ns("Herr Kranz", X2, FB, "wass", KR_F, d=0.2),
]))

# F2 A. Wasserschaden: Prüfung § 280 Abs. 1 -----------------------------------------------------------------------------------------
PA = "A. Wasserschaden, §§ 437 Nr. 3, 280 Abs. 1 BGB › "
folie([("wp1", PA + "I. Schuldverhältnis"), ("wp2", PA + "II. Pflichtverletzung"), ("wp3", PA + "III. Vertretenmüssen"),
       ("wp4", PA + "IV. Schaden")], rechts_frei([
    *tafel("wp1", "A. Gisela gegen Kranz: 1.500 €", size=44),
    ok(140, 220, "wp1", gr=20), z("I. Schuldverhältnis: Kaufvertrag", 185, 200, "wp1", "Bold", 34),
    z("II. Pflichtverletzung: mangelhafte Maschine", 185, 290, "wp2", "Bold", 34),
    ok(140, 310, beim("wp2", "geliefert", ende=True), gr=20),
    zit("§ 433 Abs. 1 Satz 2 BGB", 225, 345, beim("wp2", "Paragraf")),
    ok(140, 420, "wp3", gr=20), z("III. Vertretenmüssen: vermutet", 185, 400, "wp3", "Bold", 34),
    z("und unachtsam gestoßen", 225, 455, beim("wp3", "unachtsam"), size=32),
    ok(140, 560, "wp4", gr=20), z("IV. Schaden: 1.500 €", 185, 540, "wp4", "Bold", 34),
    blk(110, 640, 1040, 90, GRUEN, "wp5", [("Eine Frist braucht Gisela nicht.", "ExtraBold", 36, INK)]),
    ficon("tabler", "file-text", FX, 330, 110, "wp1", fuell=WEISS, bis="wp2"),
    pl("Kaufvertrag", FX, 350, "wp1", fill=WEISS, size=28, anker="m", bis="wp2"),
    ficon("tabler", "wash-machine", FX, 330, 150, "wp2", fuell=MASCH, bis="wp4"),
    pl("mangelhaft", FX, 350, "wp2", fill=ROT, size=28, anker="m", bis="wp4"),
    ficon("tabler", "droplets", FX, 330, 110, "wp4", fuell=WASSER),
    pl("1.500 €", FX, 350, "wp4", fill=BLAU, size=28, anker="m"),
    *gi(X1, FB, FR, [("wp1", "ernst"), ("wp4", "froh")]), ns("Gisela", X1, FB, "wp1", GI_F),
    *kr(X2, FB, FR, [("wp1", "ruhig"), ("wp3", "sorge")], d=0.2), ns("Herr Kranz", X2, FB, "wp1", KR_F, d=0.2),
]))

# G1 B. Waschsalon: Zuordnung -----------------------------------------------------------------------------------------------------
folie([("verz", "B. Waschsalon (30 €) › Zuordnung"),
       ("verz2", "B. Waschsalon › Verzögerungsschaden, §§ 280 Abs. 1, 2, 286 BGB")], rechts_frei([
    *tafel("verz", "B. Der Waschsalon: 30 €"),
    z("Würde eine spätere Leistung sie beseitigen?", 110, 190, "verz1", "Bold", 34),
    nein(140, 280, beim("verz1", "nicht"), gr=20), z("Nein.", 185, 260, beim("verz1", "nicht"), "Bold", 33),
    z("Sie beruhen auf der Verspätung.", 185 + F("Bold", 33).getlength("Nein. "), 260, beim("verz1", "denn"), size=33),
    blk(110, 360, 1040, 140, GELB, "verz2", [("Verzögerungsschaden", "ExtraBold", 38, INK),
                                            ("§ 280 Abs. 1, 2, § 286 BGB", "Bold", 32, INK)]),
    z("Voraussetzung: Verzug", 110, 560, "verz3", "Bold", 36),
    ficon("tabler", "wash-machine", FX, 330, 140, "verz", fuell=MASCH),
    pl("Waschsalon: 30 €", FX, 350, "verz", fill=GELB, size=28, anker="m"),
    *gi(X1, FB, FR, [("verz", "ruhig"), ("verz2", "denkt")]), ns("Gisela", X1, FB, "verz", GI_F),
    *kr(X2, FB, FR, [("verz", "muede")], d=0.2), ns("Herr Kranz", X2, FB, "verz", KR_F, d=0.2),
]))

# G2 B. Waschsalon: Verzug, § 286 -------------------------------------------------------------------------------------------------
PB = "B. Waschsalon › Verzug, § 286 BGB › "
folie([("v1", PB + "Fälligkeit"), ("v2", PB + "Mahnung"), ("v4", PB + "Vertretenmüssen"),
       ("v5", "B. Waschsalon › Ergebnis")], rechts_frei([
    *tafel("v1", "Verzug, § 286 BGB"),
    ok(140, 220, "v1", gr=20), z("1. Fälligkeit: Lieferung am 2. März", 185, 200, "v1", "Bold", 34),
    nein(140, 310, "v2", gr=20), z("2. Mahnung: nicht erfolgt", 185, 290, "v2", "Bold", 34),
    ok(140, 390, beim("v3", "entbehrlich"), gr=20), z("aber entbehrlich: Zeit nach dem Kalender", 185, 370, beim("v3", "entbehrlich"), size=33),
    z("bestimmt, § 286 Abs. 2 Nr. 1 BGB", 225, 420, beim("v3", "Kalender"), size=33),
    ok(140, 520, "v4", gr=20), z("3. Vertretenmüssen: Termin vergessen", 185, 500, "v4", "Bold", 34),
    zit("§ 286 Abs. 4 BGB", 225, 555, "v4"),
    blk(110, 630, 1040, 90, GRUEN, "v5", [("Kranz schuldet die 30 €.", "ExtraBold", 38, INK)]),
    ficon("tabler", "calendar-event", FX, 330, 120, "v1", fuell=GELB),
    pl("2. März", FX, 350, "v1", fill=GELB, size=28, anker="m"),
    *gi(X1, FB, FR, [("v1", "ernst"), ("v5", "froh")]), ns("Gisela", X1, FB, "v1", GI_F),
    *kr(X2, FB, FR, [("v1", "ruhig"), ("v4", "sorge")], d=0.2), ns("Herr Kranz", X2, FB, "v1", KR_F, d=0.2),
]))

# H1 C. Reparatur: Zuordnung --------------------------------------------------------------------------------------------------------
folie([("statt", "C. Reparatur (200 €) › Zuordnung"),
       ("statt2", "C. Reparatur › statt der Leistung, §§ 437 Nr. 3, 280 Abs. 1, 3, 281 BGB")], rechts_frei([
    *tafel("statt", "C. Die Reparatur: 200 €"),
    z("Hätte Kranz nachgebessert?", 110, 190, "statt1", "Bold", 34),
    ok(140, 280, beim("statt1", "nie"), gr=20), z("Dann wären sie nie angefallen.", 185, 260, beim("statt1", "nie"), size=33),
    blk(110, 360, 1040, 100, ORANGE, "statt2", [("Schadensersatz statt der Leistung", "ExtraBold", 38, INK)]),
    z("§ 437 Nr. 3 BGB: §§ 280 Abs. 1, 3, 281 BGB", 110, 500, beim("statt2", "vierhundertsiebenunddreißig"), "Bold", 33),
    zit("BGH, Urt. v. 12.3.2021 – V ZR 33/19, Rn. 8 (Mängelbeseitigungskosten)", 110, 555, beim("statt2", "vierhundertsiebenunddreißig")),
    ficon("tabler", "tool", FX, 330, 130, "statt", fuell=GELB),
    pl("Werkstatt: 200 €", FX, 350, "statt", fill=ROT, size=28, anker="m"),
    *gi(X1, FB, FR, [("statt", "ruhig"), ("statt2", "denkt")]), ns("Gisela", X1, FB, "statt", GI_F),
    *kr(X2, FB, FR, [("statt", "ernst"), ("statt1", "sorge")], d=0.2), ns("Herr Kranz", X2, FB, "statt", KR_F, d=0.2),
]))

# H2 C. Reparatur: Wortlaut § 281 Abs. 1 Satz 1 und Prüfung -------------------------------------------------------------------------
W281 = ["„Soweit der Schuldner die fällige Leistung nicht oder nicht wie",
        "geschuldet erbringt, kann der Gläubiger unter den Voraussetzungen",
        "des § 280 Abs. 1 Schadensersatz statt der Leistung verlangen, wenn",
        "er dem Schuldner erfolglos eine angemessene Frist zur Leistung",
        "oder Nacherfüllung bestimmt hat.“"]
w281, w281_y = wortlaut(80, 180, 1100, W281, "§ 281 Abs. 1 Satz 1 BGB", "w281", marken=[
    (0, "nicht oder nicht wie", beim("w281a", "nicht")), (1, "geschuldet", beim("w281a", "geschuldet")),
    (3, "erfolglos eine angemessene Frist", beim("w281b", "erfolglos")),
    (4, "oder Nacherfüllung bestimmt hat", beim("w281b", "Nacherfüllung"))], size=30)
PC = "C. Reparatur, §§ 280 Abs. 1, 3, 281 BGB › "
folie([("w281", PC + "Wortlaut § 281 Abs. 1 Satz 1"), ("f1", PC + "nicht wie geschuldet"), ("f2", PC + "Frist"),
       ("f3", PC + "Vertretenmüssen"), ("f4", "C. Reparatur › Ergebnis")], rechts_frei([
    *tafel("w281", "Voraussetzungen des § 281 BGB", size=44),
    *w281,
    ok(140, w281_y + 50, "f1", gr=20), z("mangelhaft: nicht wie geschuldet", 185, w281_y + 30, "f1", "Bold", 33),
    ok(140, w281_y + 110, "f2", gr=20), z("Frist von zwei Wochen ungenutzt abgelaufen", 185, w281_y + 90, "f2", "Bold", 33),
    ok(140, w281_y + 170, "f3", gr=20), z("Vertretenmüssen: wieder vermutet", 185, w281_y + 150, "f3", "Bold", 33),
    blk(110, w281_y + 220, 1040, 80, GRUEN, "f4", [("Ergebnis: 200 €", "ExtraBold", 36, INK)]),
    ficon("tabler", "wash-machine", FX, 330, 140, "w281", fuell=MASCH, bis="f2"),
    pl("nicht wie geschuldet", FX, 350, beim("w281a", "geschuldet"), fill=ROT, size=28, anker="m", bis="f2"),
    ficon("tabler", "calendar-event", FX, 330, 110, "f2", fuell=GELB),
    pl("Frist: zwei Wochen", FX, 350, "f2", fill=GELB, size=28, anker="m"),
    *gi(X1, FB, FR, [("w281", "ruhig"), ("f4", "froh")]), ns("Gisela", X1, FB, "w281", GI_F),
    *kr(X2, FB, FR, [("w281", "ernst"), ("f2", "muede")], d=0.2), ns("Herr Kranz", X2, FB, "w281", KR_F, d=0.2),
]))

# I1 § 282 BGB ------------------------------------------------------------------------------------------------------------------------
folie([("weg", "Statt der Leistung › weitere Wege"), ("p282", "Statt der Leistung › Rücksichtspflicht, § 282 BGB")],
      rechts_frei([
    *tafel("weg", "Statt der Leistung: drei weitere Wege"),
    z("§ 282 BGB: Rücksichtspflicht verletzt", 110, 280, "p282", "Bold", 34),
    z("(§ 241 Abs. 2 BGB) und die Leistung durch ihn", 150, 335, beim("p282", "und"), size=32),
    z("ist dem Gläubiger nicht mehr zuzumuten", 150, 385, beim("p282", "zuzumuten"), size=32),
    z("Beispiel der Gesetzesbegründung:", 110, 490, "p282b", "Bold", 34),
    z("Ein Maler beschädigt bei der Arbeit", 150, 545, beim("p282b", "Maler"), size=32),
    z("immer wieder Möbel.", 150, 595, beim("p282b", "immer"), size=32),
    zit("BT-Drucks. 14/6040, S. 141 f.", 150, 650, beim("p282b", "immer")),
    ficon("tabler", "route", FX, 330, 120, "weg", fuell=None, bis=beim("p282b", "Maler")),
    pl("drei weitere Wege", FX, 350, beim("weg", "drei"), fill=WEISS, size=28, anker="m", bis=beim("p282b", "Maler")),
    ficon("tabler", "brush", X1, 330, 110, beim("p282b", "Maler"), fuell=GELB),
    ficon("tabler", "armchair", X2, 330, 150, beim("p282b", "Möbel"), fuell=ROT),
    pl("Maler", X1, 350, beim("p282b", "Maler"), fill=GELB, size=28, anker="m"),
    pl("Möbel", X2, 350, beim("p282b", "Möbel"), fill=WEISS, size=28, anker="m"),
    *gi(FX, FB, FR, [("weg", "denkt"), ("p282b", "aerger")]), ns("Gisela", FX, FB, "weg", GI_F),
]))

# I2 §§ 283, 311a Abs. 2 BGB -----------------------------------------------------------------------------------------------------------
folie([("p283", "Statt der Leistung › nachträglich, § 283 BGB"), ("p311", "Statt der Leistung › anfänglich, § 311a Abs. 2 BGB")],
      rechts_frei([
    *tafel("p283", "Wenn die Leistungspflicht entfällt"),
    z("§ 283 BGB: Leistungspflicht entfällt nach § 275", 110, 190, "p283", "Bold", 34),
    z("nach Vertragsschluss, z. B. Einzelstück verbrennt", 150, 245, beim("p283", "verkauftes"), size=32),
    nein(140, 320, beim("p283", "Frist"), gr=20), z("keine Frist nötig", 185, 300, beim("p283", "Frist"), size=33),
    zit("§ 283 Satz 1 BGB; BT-Drucks. 14/6040, S. 142", 185, 350, beim("p283", "Frist")),
    z("§ 311a Abs. 2 BGB: Hindernis schon", 110, 450, "p311", "Bold", 34),
    z("bei Vertragsschluss", 150, 505, beim("p311", "Vertragsschluss"), "Bold", 34),
    ok(140, 600, "p311b", gr=20), z("Haftung, wenn der Schuldner es kannte", 185, 580, "p311b", size=32),
    z("oder seine Unkenntnis zu vertreten hat", 185, 630, beim("p311b", "Unkenntnis"), size=32),
    zit("§ 311a Abs. 2 Satz 2 BGB", 185, 680, beim("p311b", "Unkenntnis")),
    ficon("tabler", "flame", FX, 330, 110, beim("p283", "verbrennt"), fuell=ORANGE, bis="p311"),
    pl("Einzelstück verbrennt", FX, 350, beim("p283", "verbrennt"), fill=ORANGE, size=28, anker="m", bis="p311"),
    ficon("tabler", "file-text", FX, 330, 110, "p311", fuell=WEISS),
    pl("schon bei Vertragsschluss", FX, 350, beim("p311", "Vertragsschluss"), fill=WEISS, size=28, anker="m"),
    *kr(FX, FB, FR, [("p283", "denkt"), ("p311b", "ernst")]), ns("Herr Kranz", FX, FB, "p283", KR_F),
]))

# J Klausurtipp (Lexi) --------------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · jeden Schaden einzeln zuordnen"), ("tipp1", "Klausurtipp · keine Frist für Folgeschäden")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Jeden Schaden einzeln mit der", 200, 200, beim("tipp", "Ordne"), "Bold", 34),
    z("Kontrollfrage zuordnen", 200, 255, beim("tipp", "Kontrollfrage"), "Bold", 34),
    nein(140, 380, "tipp1", gr=20), z("Fehler: den Wasserschaden über § 281 BGB", 185, 360, "tipp1", size=34),
    z("prüfen und eine Frist verlangen", 185, 415, "tipp2", size=34),
    ok(140, 520, beim("tipp2", "Folgeschäden"), gr=20),
    z("Für Folgeschäden braucht es keine Frist.", 185, 500, beim("tipp2", "Folgeschäden"), "Bold", 34),
    zit("BGH, Urt. v. 7.2.2019 – VII ZR 63/18, Rn. 19", 185, 555, beim("tipp2", "Folgeschäden")),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# K Klausurschema als Entscheidungsbaum -----------------------------------------------------------------------------------------------
L0, L1_, R0, R1_ = 110, 900, 1020, 1810
folie([("sch", "Klausurschema"), ("sb3", "Klausurschema › neben der Leistung"), ("sb6", "Klausurschema › statt der Leistung"),
       ("sb10", "Klausurschema › jeweils § 280 Abs. 1 BGB")], [
    karte(60, 50, 1800, 900, "sch"),
    titel(glyphen("Klausurschema: Schadensersatz, §§ 280 ff. BGB"), 110, 90, "sch", 44),
    blk(610, 170, 700, 70, GELB, "sb1", [("1. Welcher Schaden?", "ExtraBold", 34, INK)]),
    linienzug([(960, 240), (960, 270)], "sb2", breite=6),
    blk(410, 270, 1100, 70, GELB, "sb2", [("2. Würde eine Nacherfüllung ihn beseitigen?", "ExtraBold", 34, INK)]),
    linienzug([(700, 340), (500, 390)], "sb3", breite=6),
    blk(L0, 390, L1_ - L0, 70, GRUEN, "sb3", [("Wenn nein: neben der Leistung", "ExtraBold", 33, INK)]),
    blk(L0 + 40, 490, L1_ - L0 - 40, 110, WEISS, "sb4", [("Verspätung: zusätzlich Verzug", "Bold", 31, INK),
                                                       ("§§ 280 Abs. 1, 2, 286 BGB", "Regular", 30, INK)]),
    blk(L0 + 40, 630, L1_ - L0 - 40, 70, WEISS, "sb5", [("sonst: § 280 Abs. 1 BGB", "Bold", 31, INK)]),
    linienzug([(1220, 340), (1420, 390)], "sb6", breite=6),
    blk(R0, 390, R1_ - R0, 70, ORANGE, "sb6", [("Wenn ja: statt der Leistung", "ExtraBold", 33, INK)]),
    blk(R0 + 40, 490, R1_ - R0 - 40, 110, WEISS, "sb7", [("Leistungspflicht besteht: § 281 (Frist),", "Bold", 31, INK),
                                                       ("Rücksichtspflicht: § 282 BGB", "Regular", 30, INK)]),
    blk(R0 + 40, 630, R1_ - R0 - 40, 70, WEISS, "sb8", [("entfällt nach Vertragsschluss: § 283", "Bold", 31, INK)]),
    blk(R0 + 40, 730, R1_ - R0 - 40, 70, WEISS, "sb9", [("Hindernis bei Vertragsschluss: § 311a II", "Bold", 31, INK)]),
    blk(L0, 835, R1_ - L0, 75, LILA, "sb10", [("Dann jeweils: Schuldverhältnis · Pflichtverletzung · Vertretenmüssen · Schaden",
                                               "ExtraBold", 31, INK)]),
])

# L Merksatz (Lexi) ------------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Erst den ", 0), ("Schaden zuordnen,", "a")], [("dann die Norm wählen.", 0)]],
                750, 320, 46, "merke", {"a": beim("merke", "Schaden")}),
    *markertext([[("Was eine Nacherfüllung beseitigen würde,", 0)], [("gibt es nur ", 0), ("statt der Leistung", "b")],
                 [("und grundsätzlich ", 0), ("erst nach einer Frist.", "c")]],
                750, 520, 42, "merke2", {"b": beim("merke2", "statt"), "c": beim("merke2", "erst")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
