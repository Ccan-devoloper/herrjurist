"""Folge 056 · Werkvertrag oder Dienstvertrag? Abgrenzung nach §§ 611, 631, 650 BGB – Serienstandard Open Peeps (Katzenkönig).
Beispielfall (Plan-Hook „Der Nachhilfelehrer garantiert keine Note – der Maler aber eine gestrichene Wand“): Mareike bucht
bei Henrik zehn Stunden Nachhilfe zu je 30 € und lässt ihr Zimmer von der Malerin Frau Ostertag für 400 € streichen. Die
Wand ist am Freitag fleckig, Mareike verweigert die Abnahme; die Klausur besteht sie trotz Nachhilfe nicht.
Szenen laut ../SZENENPLAN.md: A1 Lernplatz (Nachhilfe), A2 Zimmerwand (Malerin), A3 Lernplatz (Klausur, Frage), B Sachverhalt,
C1 Wortlaut § 611 I, C2 Wortlaut § 631 I, II, D Kriterium Erfolg/Tätigkeit, E Subsumtion, F1 Grenzfall Arzt, F2 Website,
Software, Wartung, G1 Werklieferung (Wortlaut § 650 I 1), G2 Vorgaben/Einbau, H1 Folgen Werkvertrag, H2 die fleckige Wand,
I Folgen Dienstvertrag, J Vergütung/Arbeitsvertrag, K Klausurtipp (Lexi), L Entscheidungsbaum, M Merksatz (Lexi).
Geräusch nur bei sichtbarer Handlung (Farbroller an der Wand; Freesound CC0, Herkunft in ../geraeusche_herkunft.json).
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns als eigene
Kopie aus Folge 053 (gemeinsame Dateien unverändert)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_056/"

FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
ZITAT = (246, 246, 250, 255)
GRAU = (176, 178, 190, 255)
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


def lexi_bis_ende(cue):
    return (cue, round(DAUER - T_(cue) - 0.05, 3))


def zit(text, x, y, cue, size=26):
    """Fundstellenzeile (grau, klein)."""
    return z(text, x, y, cue, size=size, farbe=TEXT)


def rechts_frei(els, x0=1250):
    """Figuren und Requisiten der Tafelfolien stehen rechts der Tafel."""
    for e in els:
        n = e.name or ""
        if n.startswith(("bild:", "ficon:")) or "/op_056/" in n:
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




BODEN, FH = 880, 480
X1, X2 = 1420, 1720                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
MA_F, HE_F, OS_F = LILA, GRUEN, GELB        # Farben der Namensschilder


def boden(cue, hart_=False):
    e = linienzug([(40, BODEN), (1880, BODEN)], cue, breite=7, farbe=INK)
    return hart(e) if hart_ else e


def mareike(cx, unten, hoehe, folge, **k):
    return fig("MA", cx, unten, hoehe, folge, **k)


def henrik(cx, unten, hoehe, folge, **k):
    return fig("HE", cx, unten, hoehe, folge, **k)


def ostertag(cx, unten, hoehe, folge, **k):
    return fig("OS", cx, unten, hoehe, folge, **k)


def paar(c0, links, rechts, a="HE", b="MA"):
    """Tafelszene: Figur a links (X1), Figur b rechts (X2), beide blicken zur Tafel."""
    name = {"HE": ("Henrik", HE_F), "MA": ("Mareike", MA_F), "OS": ("Frau Ostertag", OS_F)}
    return [*fig(a, X1, FB, FR, links), ns(name[a][0], X1, FB, c0, name[a][1]),
            *fig(b, X2, FB, FR, rechts, d=0.2), ns(name[b][0], X2, FB, c0, name[b][1], d=0.2)]


def tisch(cue, hart_=False, **k):
    """Mareikes Lernplatz: Schreibtisch (Phosphor desk) mit Büchern und Taschenrechner."""
    t = ficon("ph", "desk", 1060, BODEN - 2, 340, cue, fuell=GELB, nebenfarbe=WEISS, **k)
    oben = t.y + 6
    els = [t, ficon("ph", "books", 960, oben, 110, cue, fuell=BLAU, nebenfarbe=WEISS, **k),
           ficon("tabler", "calculator", 1140, oben, 80, cue, fuell=WEISS, **k)]
    return [hart(e) for e in els] if hart_ else els


# A1 Fall: die Nachhilfe ------------------------------------------------------------------------------------------------
MAX, HEX = 620, 1500
folie([(NULL, "Fall · Die Statistikklausur"), ("nh", "Fall · Die Nachhilfe")], [
    hart(pl("In sechs Wochen: Statistikklausur", 70, 40, NULL, fill=GELB, size=44)),
    boden(NULL, True),
    *tisch(NULL, hart_=True),
    *mareike(MAX, BODEN, FH, [(NULL, "ueberlegt_r"), ("nh", "ruhig_r"), ("h1", "froh_r")], erst="cut"),
    hart(ns("Mareike", MAX, BODEN, NULL, MA_F)),
    hart(ficon("tabler", "calendar-event", 1060, 360, 110, NULL, fuell=WEISS, bis=beim("nh", "zehn"))),
    hart(pl("6 Wochen", 1060, 380, NULL, fill=WEISS, size=30, anker="m", bis=beim("nh", "zehn"))),
    *henrik(HEX, BODEN, FH, [(beim("nh", "Henrik"), "ruhig")], bis="h1"),
    *redet("HE_redet", HEX, BODEN, FH, "h1", "maler"),
    ns("Henrik, Nachhilfelehrer", HEX, BODEN, beim("nh", "Henrik"), HE_F),
    pl("10 Stunden Nachhilfe", 1060, 330, beim("nh", "zehn"), fill=WEISS, size=32, anker="m"),
    pl("je 30 €", 1060, 410, beim("nh", "dreißig"), fill=GELB, size=32, anker="m"),
    blase("sprech", 660, 230, "h1", 1100, 170, inhalt=["Ich erkläre dir den Stoff.", "Bestehen musst du selbst."],
          textsize=38, figur=("HE_redet", HEX, BODEN, FH)),
])

# A2 Fall: die Malerin an der Wand -------------------------------------------------------------------------------------
WAND = (110, 250, 560, BODEN - 250)                 # x, y, w, h der Zimmerwand
OSX, MA2X = 900, 1520
ROLLE = (560, 820)                                  # Farbroller an der Wand (Mitte unten), fährt bei „streichen“ hoch
STREIF = "streif"


def streifen(cue):
    """Flecken und Streifen auf der frisch gestrichenen Wand (einfache Linienzüge in Palettengrau)."""
    els = []
    x0, y0, w, h = WAND
    for i, (dx, s) in enumerate([(70, 0), (160, 30), (250, -20), (340, 25), (430, -10)]):
        xa = x0 + dx
        pts = [(xa + s * 0.0, y0 + 40), (xa + 18, y0 + h * 0.35), (xa - 6, y0 + h * 0.65), (xa + 12, y0 + h - 40)]
        els.append(linienzug(pts, cue, breite=26 if i % 2 else 18, farbe=(214, 205, 190, 255)))
    for cx, cy, r in [(190, 420, 34), (420, 330, 28), (330, 560, 40), (520, 470, 30), (240, 700, 26)]:
        im = Image.new("RGBA", (2 * r + 4, 2 * r + 4))
        ImageDraw.Draw(im).ellipse((2, 2, 2 * r + 2, 2 * r + 2), fill=(203, 193, 176, 255))
        els.append(El(im, cx - r - 2, cy - r - 2, cue, "fade", 0.0, None, name="fleck"))
    return els


folie([("maler", "Fall · Die Malerin"), (STREIF, "Fall · Freitag: die Wand")], [
    pl("Außerdem: das Zimmer streichen", 70, 40, "maler", fill=GELB, size=44, bis=STREIF),
    pl("Am Freitag", 70, 40, STREIF, fill=GELB, size=44),
    boden("maler"),
    karte(*WAND, "maler", fill=(226, 214, 192, 255), rund=6, schatten=0, rand=5),
    pl("alte Wand", WAND[0] + WAND[2] / 2, 290, "maler", fill=WEISS, size=28, anker="m", bis=beim("maler", "streichen")),
    karte(*WAND, beim("maler", "streichen"), fill=WEISS, rund=6, schatten=0, rand=5),
    *streifen(STREIF),
    pl("fleckig, voller Streifen", WAND[0] + WAND[2] / 2, 290, beim(STREIF, "fleckig"), fill=ROT, size=30, anker="m"),
    szene(bis_(bewegt(ficon("ph", "paint-roller", ROLLE[0], ROLLE[1] - 260, 150, "maler", fuell=WEISS),
                      beim("maler", "streichen"), beim("maler", "streichen", ende=True), 0, 260), None), "056rolle*", 0.8),
    ficon("tabler", "bucket", OSX + 190, BODEN - 2, 110, "maler", fuell=WEISS),
    *ostertag(OSX, BODEN, FH, [("maler", "ruhig")], bis="o1"),
    *redet("OS_redet_r", OSX, BODEN, FH, "o1", STREIF),
    *ostertag(OSX, BODEN, FH, [(STREIF, "ertappt_r")], erst="cut"),
    ns("Frau Ostertag, Malerin", OSX, BODEN, "maler", OS_F),
    *mareike(MA2X, BODEN, FH, [("maler", "ruhig"), ("o1", "froh"), (STREIF, "sorge")], bis="m1"),
    *redet("MA_redet", MA2X, BODEN, FH, "m1", "stunden"),
    ns("Mareike", MA2X, BODEN, "maler", MA_F),
    pl("400 €", 1250, 420, beim("o1", "vierhundert"), fill=GELB, size=34, anker="m"),
    blase("sprech", 640, 230, "o1", 1180, 170, inhalt=["Bis Freitag ist die Wand weiß.", "Das macht vierhundert Euro."],
          textsize=36, figur=("OS_redet_r", OSX, BODEN, FH), bis=STREIF),
    blase("sprech", 640, 230, "m1", 1150, 170, inhalt=["So nehme ich die Wand nicht ab.", "Bitte streichen Sie noch einmal!"],
          textsize=34, figur=("MA_redet", MA2X, BODEN, FH)),
])

# A3 Fall: die Klausur, die Frage --------------------------------------------------------------------------------------
folie([("stunden", "Fall · Die Klausur"), ("frage", "Fall · Die Frage")], [
    pl("Henrik gibt alle 10 Stunden", 70, 40, "stunden", fill=GELB, size=44),
    boden("stunden"),
    *tisch("stunden"),
    pl("wie vereinbart", 1060, 420, beim("stunden", "wie"), fill=WEISS, size=30, anker="m", bis="durch"),
    ficon("tabler", "file-x", 1060, 460, 100, "durch", fuell=ROT, bis="frage"),
    pl("durchgefallen", 1060, 480, beim("durch", "durch"), fill=ROT, size=30, anker="m", bis="frage"),
    *mareike(MAX, BODEN, FH, [("stunden", "ruhig_r"), ("durch", "muede_r")], bis="m2"),
    *redet("MA_redet_r", MAX, BODEN, FH, "m2", "frage"),
    *mareike(MAX, BODEN, FH, [("frage", "ueberlegt_r")], erst="cut"),
    ns("Mareike", MAX, BODEN, "stunden", MA_F),
    *henrik(HEX, BODEN, FH, [("stunden", "froh"), ("durch", "ruhig"), ("m2", "denkt"), ("frage", "ernst")]),
    ns("Henrik", HEX, BODEN, "stunden", HE_F),
    blase("sprech", 600, 230, "m2", 1060, 170, inhalt=["Ich bin durchgefallen.", "Dafür zahle ich nichts!"], textsize=40,
          figur=("MA_redet_r", MAX, BODEN, FH), bis="frage"),
    pl("Muss Mareike für die Nachhilfe zahlen?", 1060, 120, "frage", fill=PINK, size=34, anker="m"),
    pl("Was kann sie von Frau Ostertag verlangen?", 1060, 200, "frage2", fill=PINK, size=34, anker="m"),
    pl("Nachhilfelehrer: keine Note garantiert", 1060, 280, "hook", fill=WEISS, size=32, anker="m"),
    pl("Malerin: eine gestrichene Wand", 1060, 350, beim("hook", "Malerin"), fill=WEISS, size=32, anker="m"),
])

# B Sachverhalt ----------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Mareike bucht für ihre Statistikklausur bei Henrik zehn Stunden Nachhilfe zu je 30 Euro. Henrik sagt: „Ich erkläre "
    "dir den Stoff. Bestehen musst du selbst.“ Er gibt alle zehn Stunden wie vereinbart. Mareike fällt trotzdem durch und "
    "will die 300 Euro nicht zahlen.",
    "Außerdem lässt Mareike ihr Zimmer von der Malerin Frau Ostertag streichen. Frau Ostertag sagt: „Bis Freitag ist die "
    "Wand weiß. Das macht 400 Euro.“ Am Freitag ist die Wand fleckig und voller Streifen. Mareike nimmt die Wand nicht ab "
    "und verlangt, dass Frau Ostertag noch einmal streicht.",
], "Muss Mareike für die Nachhilfe zahlen, was kann sie von Frau Ostertag verlangen?")

# C1 Wortlaut § 611 Abs. 1 BGB ------------------------------------------------------------------------------------------
W611 = ["„Durch den Dienstvertrag wird derjenige, welcher Dienste zusagt,",
        "zur Leistung der versprochenen Dienste, der andere Teil zur",
        "Gewährung der vereinbarten Vergütung verpflichtet.“"]
w611, w611_y = wortlaut(80, 230, 1100, W611, "§ 611 Abs. 1 BGB", "p611", marken=[
    (1, "zur Leistung der versprochenen Dienste", beim("p611", "Leistung")),
    (2, "Gewährung der vereinbarten Vergütung", beim("p611", "Gewährung"))], size=32)
folie([("p611", "Die Vertragstypen · Dienstvertrag, § 611 Abs. 1 BGB")], rechts_frei([
    *tafel("p611", "Der Dienstvertrag"),
    pl("Erst die beiden Vertragstypen", 110, 160, "p611", fill=WEISS, size=30),
    *w611,
    z("Dienste: Henrik unterrichtet", 110, w611_y + 50, beim("p611", "Leistung"), "Bold", 36),
    z("Vergütung: 30 € je Stunde", 110, w611_y + 110, beim("p611", "Gewährung"), "Bold", 36),
    ficon("tabler", "chalkboard", X1 + 150, 380, 140, beim("p611", "Dienste"), fuell=GRUEN),
    pl("Dienste", X1 + 150, 160, beim("p611", "Dienste"), fill=GRUEN, size=28, anker="m"),
    *paar("p611", [("p611", "ruhig"), (beim("p611", "Leistung"), "froh")], [("p611", "denkt")]),
]))

# C2 Wortlaut § 631 Abs. 1 und 2 BGB -----------------------------------------------------------------------------------
W631_1 = ["„Durch den Werkvertrag wird der Unternehmer zur Herstellung des",
          "versprochenen Werkes, der Besteller zur Entrichtung der",
          "vereinbarten Vergütung verpflichtet.“"]
W631_2 = ["„Gegenstand des Werkvertrags kann sowohl die Herstellung oder",
          "Veränderung einer Sache als auch ein anderer durch Arbeit oder",
          "Dienstleistung herbeizuführender Erfolg sein.“"]
w631, w631_y = wortlaut(80, 180, 1100, W631_1, "§ 631 Abs. 1 BGB", "p631", marken=[
    (0, "zur Herstellung des", beim("p631", "Herstellung")), (1, "versprochenen Werkes", beim("p631", "Herstellung"))], size=31)
w631b, w631b_y = wortlaut(80, w631_y + 30, 1100, W631_2, "§ 631 Abs. 2 BGB", "p631", marken=[
    (1, "Veränderung einer Sache", beim("p631b", "Veränderung")),
    (2, "herbeizuführender Erfolg", beim("p631c", "Erfolg"))], size=31)
folie([("p631", "Die Vertragstypen · Werkvertrag, § 631 Abs. 1 BGB"), ("p631b", "Die Vertragstypen · Werkvertrag, § 631 Abs. 2 BGB")],
      rechts_frei([
    *tafel("p631", "Der Werkvertrag"),
    *w631, *w631b,
    z("Wand streichen: Veränderung einer Sache", 110, w631b_y + 30, beim("p631b", "Veränderung"), "Bold", 34),
    ficon("ph", "paint-roller", X1 + 150, 380, 150, beim("p631b", "Veränderung"), fuell=WEISS, bis="p631c"),
    pl("Veränderung", X1 + 150, 160, beim("p631b", "Veränderung"), fill=WEISS, size=28, anker="m", bis="p631c"),
    ficon("tabler", "checks", X1 + 150, 380, 130, "p631c", fuell=GRUEN),
    pl("Erfolg", X1 + 150, 160, beim("p631c", "Erfolg"), fill=GRUEN, size=28, anker="m"),
    *paar("p631", [("p631", "ruhig"), ("p631b", "froh")], [("p631", "denkt"), ("p631c", "ruhig")], a="OS", b="MA"),
]))

# D Das Kriterium: Erfolg oder Tätigkeit ------------------------------------------------------------------------------
folie([("krit", "Abgrenzung · Tätigkeit oder Erfolg?"), ("ausl", "Abgrenzung · Auslegung, §§ 133, 157 BGB")], rechts_frei([
    *tafel("krit", "Der Unterschied: Erfolg"),
    blk(110, 190, 500, 200, BLAU, "kd", [("Dienstvertrag", "ExtraBold", 40, INK), ("geschuldet:", "Regular", 32, INK),
                                         ("die Tätigkeit", "Bold", 36, INK)]),
    blk(650, 190, 500, 200, GRUEN, "kw", [("Werkvertrag", "ExtraBold", 40, INK), ("geschuldet:", "Regular", 32, INK),
                                          ("das Ergebnis", "Bold", 36, INK)]),
    z("Was geschuldet ist: Auslegung", 110, 440, "ausl", "Bold", 36),
    pl("Wille der Parteien", 110, 510, beim("ausl2", "Willen"), fill=WEISS, size=30),
    pl("Vertragszweck", 460, 510, beim("ausl2", "Vertragszweck"), fill=WEISS, size=30),
    pl("Umstände", 750, 510, beim("ausl2", "Umständen"), fill=WEISS, size=30),
    zit("Vertragszweck und Parteiwille: BGH, Urt. v. 4.3.2010 – III ZR 79/09, Rn. 16", 110, 600, beim("ausl2", "Vertragszweck")),
    pl("Hilfsfrage: Hat er den Erfolg allein in der Hand?", 110, 680, "hilf", fill=PINK, size=32),
    *paar("krit", [("krit", "ruhig"), ("kd", "froh"), ("kw", "ruhig"), ("hilf", "denkt")],
          [("krit", "ruhig"), ("kw", "froh"), ("hilf", "denkt")], a="HE", b="OS"),
]))

# E Subsumtion ---------------------------------------------------------------------------------------------------------
folie([("nhs", "Subsumtion · die Nachhilfe"), ("mal", "Subsumtion · die Malerin")], rechts_frei([
    *tafel("nhs", "Nachhilfe und Malerin"),
    z("Henrik verspricht Unterricht.", 110, 190, "nhs", "Bold", 36),
    z("Bestehen hängt auch von Mareike ab,", 150, 245, "nhs2", size=34),
    z("eine Note sagt er nicht zu.", 150, 295, beim("nhs2", "eine"), size=34),
    blk(110, 350, 1040, 90, BLAU, "dv", [("Dienstvertrag, § 611 BGB", "ExtraBold", 38, INK)]),
    z("Frau Ostertag verspricht eine weiße Wand:", 110, 490, "mal", "Bold", 36),
    z("Veränderung einer Sache, § 631 Abs. 2 BGB", 150, 545, beim("mal", "Veränderung"), size=34),
    blk(110, 610, 1040, 90, GRUEN, "wv", [("Werkvertrag, § 631 BGB", "ExtraBold", 38, INK)]),
    *paar("nhs", [("nhs", "froh"), ("mal", "ruhig")], [("nhs", "ruhig"), ("mal", "froh")], a="HE", b="OS"),
]))

# F1 Grenzfall Arzt ----------------------------------------------------------------------------------------------------
folie([("grenz", "Grenzfälle · 1. der Arzt, § 630a BGB")], rechts_frei([
    *tafel("grenz", "Drei Grenzfälle: 1. der Arzt"),
    z("Behandlung nach dem fachlichen Standard,", 110, 200, "arzt", "Bold", 36),
    z("§ 630a Abs. 2 BGB", 150, 255, beim("arzt", "Standard"), size=34),
    nein(140, 345, beim("arzt", "keine"), gr=22), z("aber keine Heilung geschuldet", 185, 325, beim("arzt", "keine"), "Bold", 36),
    z("Behandlungsvertrag, § 630a BGB:", 110, 430, "arzt2", "Bold", 36),
    blk(110, 500, 1040, 90, BLAU, beim("arzt2", "Dienstvertragsrecht"),
        [("§ 630b BGB: Dienstvertragsrecht", "ExtraBold", 38, INK)]),
    zit("Zahnarzt schuldet kein Gelingen: BGH, Urt. v. 13.9.2018 – III ZR 294/16, Rn. 15", 110, 630,
        beim("arzt2", "Dienstvertragsrecht")),
    ficon("tabler", "stethoscope", X1 + 30, 470, 200, "arzt", fuell=WEISS),
    ficon("tabler", "heartbeat", X2 - 20, 470, 160, beim("arzt", "keine"), fuell=ROT),
    pl("Behandlung", X1 + 30, 200, "arzt", fill=WEISS, size=28, anker="m"),
    pl("keine Heilung", X2 - 20, 200, beim("arzt", "keine"), fill=ROT, size=28, anker="m"),
    pl("Dienstvertragsrecht", FX, 560, beim("arzt2", "Dienstvertragsrecht"), fill=BLAU, size=30, anker="m"),
]))

# F2 Website, Software, Wartung ----------------------------------------------------------------------------------------
folie([("web", "Grenzfälle · 2. Website und Software"), ("wart", "Grenzfälle · 3. Wartung")], rechts_frei([
    *tafel("web", "2. Website und Software, 3. Wartung"),
    z("Individuelle Website oder Software:", 110, 200, "web", "Bold", 36),
    ok(140, 275, beim("web", "regelmäßig"), gr=22), z("regelmäßig ein Werk: Werkvertrag", 185, 255, beim("web", "regelmäßig"), size=36),
    zit("BGH, Urt. v. 4.3.2010 – III ZR 79/09, Rn. 21, 26", 185, 315, beim("web", "regelmäßig")),
    z("Wartung: Es kommt darauf an.", 110, 400, "wart", "Bold", 36),
    z("Störungen beseitigen, Funktion erhalten:", 150, 460, beim("wart", "Störungen"), size=34),
    z("Werkvertrag", 150, 510, beim("wart", "Werkvertrag"), "Bold", 34),
    z("nur laufender Service als Tätigkeit:", 150, 580, "wart2", size=34),
    z("Dienstvertrag liegt nahe", 150, 630, beim("wart2", "Dienstvertrag"), "Bold", 34),
    zit("BGH, Urt. v. 4.3.2010 – III ZR 79/09, Rn. 23", 150, 695, beim("wart2", "Dienstvertrag")),
    ficon("tabler", "world-www", X1, 330, 140, "web", fuell=BLAU, bis="wart"),
    ficon("tabler", "code", X2 - 40, 330, 140, beim("web", "Software"), fuell=WEISS, bis="wart"),
    pl("Werk", FX, 400, beim("web", "regelmäßig"), fill=GRUEN, size=30, anker="m", bis="wart"),
    ficon("tabler", "tool", X1, 330, 130, "wart", fuell=GELB),
    ficon("tabler", "settings", X2 - 40, 330, 130, "wart2", fuell=WEISS),
    pl("Werkvertrag", X1, 400, beim("wart", "Werkvertrag"), fill=GRUEN, size=28, anker="m"),
    pl("Dienstvertrag?", X2 - 40, 400, beim("wart2", "Dienstvertrag"), fill=BLAU, size=28, anker="m"),
]))

# G1 Werklieferungsvertrag, Wortlaut § 650 Abs. 1 Satz 1 BGB ---------------------------------------------------------
W650 = ["„Auf einen Vertrag, der die Lieferung herzustellender oder zu",
        "erzeugender beweglicher Sachen zum Gegenstand hat, finden die",
        "Vorschriften über den Kauf Anwendung.“"]
w650, w650_y = wortlaut(80, 360, 1100, W650, "§ 650 Abs. 1 Satz 1 BGB", "p650", marken=[
    (0, "Lieferung herzustellender", beim("p650", "Lieferung")), (1, "beweglicher Sachen", beim("p650", "beweglicher")),
    (2, "Vorschriften über den Kauf", beim("p650", "Vorschriften"))], size=31)
folie([("wl", "Werklieferungsvertrag · erst hergestellt, dann geliefert"), ("p650", "Werklieferungsvertrag · § 650 Abs. 1 BGB")],
      rechts_frei([
    *tafel("wl", "Der Werklieferungsvertrag"),
    pl("Erst hergestellt, dann geliefert?", 110, 170, "wl", fill=PINK, size=32),
    z("Schreiner baut ein Regal nach Maß und liefert es", 110, 270, "schr", "Bold", 34),
    *w650,
    blk(110, w650_y + 30, 1040, 90, GELB, beim("p650", "Vorschriften"), [("Es gilt Kaufrecht.", "ExtraBold", 38, INK)]),
    ficon("ph", "ruler", X1 + 30, 400, 150, beim("schr", "Schreiner"), fuell=GELB),
    ficon("tabler", "hammer", X1 + 30, 620, 110, beim("schr", "Werkstatt"), fuell=GELB),
    ficon("ph", "books", X2 - 30, 400, 150, beim("schr", "Regal"), fuell=BLAU, nebenfarbe=WEISS),
    pl("Regal nach Maß", X2 - 30, 160, beim("schr", "Regal"), fill=WEISS, size=28, anker="m"),
    ficon("tabler", "truck-delivery", X2 - 30, 620, 170, beim("schr", "liefert"), fuell=WEISS),
    pl("bewegliche Sache", FX, 700, beim("p650", "beweglicher"), fill=GELB, size=30, anker="m"),
]))

# G2 Vorgaben des Kunden, Einbau vor Ort -------------------------------------------------------------------------------
folie([("x82", "Werklieferungsvertrag · nach Vorgaben des Kunden"), ("einb", "Abgrenzung · Schwerpunkt Einbau vor Ort")],
      rechts_frei([
    *tafel("x82", "Kaufrecht oder Werkvertrag?"),
    ok(140, 220, "x82", gr=22), z("auch nach Vorgaben des Kunden: Kaufrecht", 185, 200, "x82", "Bold", 36),
    zit("BGH, Urt. v. 9.2.2010 – X ZR 82/07, Rn. 8 (zu § 651 a. F., heute § 650 BGB)", 185, 260, beim("x82", "Vorgaben")),
    z("Schwerpunkt: Einbau und Anpassung vor Ort,", 110, 360, "einb", "Bold", 36),
    z("etwa Lift an der Hausfassade", 150, 415, beim("einb", "Lift"), size=34),
    blk(110, 490, 1040, 90, GRUEN, "einb2", [("Dann: Werkvertrag, § 631 BGB", "ExtraBold", 38, INK)]),
    zit("BGH, Urt. v. 30.8.2018 – VII ZR 243/17, Rn. 25, 29", 110, 610, beim("einb", "Lift")),
    ficon("ph", "books", X1 + 150, 380, 150, "x82", fuell=BLAU, nebenfarbe=WEISS, bis="einb"),
    pl("Kaufrecht", X1 + 150, 160, "x82", fill=GELB, size=28, anker="m", bis="einb"),
    ficon("tabler", "elevator", X1 + 150, 380, 130, beim("einb", "Lift"), fuell=WEISS),
    ficon("tabler", "home", X1 + 150, 230, 90, beim("einb", "Hausfassade"), fuell=GELB),
    pl("Werkvertrag", X1 + 150, 410, "einb2", fill=GRUEN, size=28, anker="m"),
    *fig("MA", X2 + 20, FB, FR, [("x82", "ruhig"), ("einb", "denkt"), ("einb2", "froh")], d=0.2),
    ns("Mareike", X2 + 20, FB, "x82", MA_F, d=0.2),
]))

# H1 Folgen beim Werkvertrag ---------------------------------------------------------------------------------------------
folie([("folg", "Folgen · Werkvertrag: Abnahme, § 640 Abs. 1 BGB"), ("faell", "Folgen · Werkvertrag: Fälligkeit, § 641 Abs. 1 BGB")],
      rechts_frei([
    *tafel("folg", "Folgen beim Werkvertrag"),
    pl("Warum ist die Einordnung so wichtig?", 110, 170, "folg", fill=PINK, size=32),
    z("Abnahme: Der Besteller muss das vertragsmäßig", 110, 280, "abn", "Bold", 34),
    z("hergestellte Werk abnehmen, § 640 Abs. 1 BGB", 150, 335, beim("abn", "hergestellte"), size=34),
    z("Vergütung erst bei der Abnahme,", 110, 430, "faell", "Bold", 34),
    z("§ 641 Abs. 1 BGB", 150, 485, beim("faell", "Paragraf"), size=34),
    ficon("tabler", "checks", X1 + 150, 380, 130, "abn", fuell=GRUEN, bis="faell"),
    pl("Abnahme", X1 + 150, 160, "abn", fill=GRUEN, size=28, anker="m", bis="faell"),
    ficon("tabler", "cash-banknote", X1 + 150, 380, 140, "faell", fuell=GRUEN),
    pl("400 € erst dann", X1 + 150, 160, "faell", fill=GELB, size=28, anker="m"),
    *paar("folg", [("folg", "ruhig")], [("folg", "denkt"), ("faell", "ruhig")], a="OS", b="MA"),
]))

# H2 Die fleckige Wand ------------------------------------------------------------------------------------------------
folie([("fleck", "Werkvertrag · die fleckige Wand, § 640 Abs. 1 Satz 2 BGB"), ("herst", "Werkvertrag · Herstellung, § 631 Abs. 1 BGB"),
       ("m634", "Werkvertrag · Mängelrechte, § 634 BGB")], rechts_frei([
    *tafel("fleck", "Die fleckige Wand"),
    nein(140, 220, "fleck", gr=22), z("Flecken und Streifen: kein unwesentlicher Mangel", 185, 200, "fleck", "Bold", 33),
    ok(140, 295, "verw", gr=22), z("Abnahme verweigert, noch nicht zahlen", 185, 275, "verw", "Bold", 34),
    ok(140, 370, "herst", gr=22), z("weiter: mangelfrei streichen, § 631 Abs. 1 BGB", 185, 350, "herst", "Bold", 34),
    zit("BGH, Urt. v. 19.1.2017 – VII ZR 301/13, Rn. 31 f.", 185, 405, beim("herst", "mangelfrei")),
    z("Nach der Abnahme: Mängelrechte, § 634 BGB", 110, 490, "m634", "Bold", 36),
    pl("Nacherfüllung", 150, 560, beim("m634", "Nacherfüllung"), fill=WEISS, size=30),
    pl("Selbstvornahme", 470, 560, beim("m634", "Selbstvornahme"), fill=WEISS, size=30),
    pl("Rücktritt oder Minderung", 150, 640, beim("m634", "Rücktritt"), fill=WEISS, size=30),
    pl("Schadensersatz", 620, 640, beim("m634", "Schadensersatz"), fill=WEISS, size=30),
    ficon("tabler", "wall", X1 + 150, 380, 130, "fleck", fuell=WEISS),
    pl("fleckig", X1 + 150, 160, "fleck", fill=ROT, size=28, anker="m"),
    *paar("fleck", [("fleck", "ertappt"), ("herst", "ruhig")], [("fleck", "sorge"), ("verw", "denkt"), ("herst", "ruhig")],
          a="OS", b="MA"),
]))

# I Folgen beim Dienstvertrag ----------------------------------------------------------------------------------------------
folie([("dfolg", "Folgen · Dienstvertrag: keine Gewährleistung"), ("p280", "Folgen · Dienstvertrag: § 280 Abs. 1 BGB"),
       ("hen", "Folgen · Dienstvertrag: Henrik")], rechts_frei([
    *tafel("dfolg", "Folgen beim Dienstvertrag"),
    nein(140, 220, "dfolg", gr=22), z("keine Abnahme, keine Mängelrechte", 185, 200, "dfolg", "Bold", 36),
    z("keine Gewährleistung:", 110, 280, beim("bgh", "Gewährleistung"), size=34),
    z("Vergütung bei schlechter Leistung", 150, 330, beim("bgh", "Vergütung"), size=34),
    z("grundsätzlich nicht gekürzt", 150, 380, beim("bgh", "Vergütung"), size=34),
    zit("BGH, Urt. v. 13.9.2018 – III ZR 294/16, Rn. 16", 150, 432, beim("bgh", "Vergütung")),
    z("schuldhafte Pflichtverletzung: § 280 Abs. 1 BGB", 110, 482, "p280", "Bold", 34),
    ok(140, 565, "hen", gr=22), z("Henrik hat wie vereinbart unterrichtet.", 185, 545, "hen", "Bold", 34),
    nein(140, 635, beim("hen", "Dass"), gr=22), z("Durchfallen: keine Pflichtverletzung", 185, 615, beim("hen", "Dass"), "Bold", 34),
    blk(110, 700, 1040, 90, BLAU, "zahl", [("Mareike zahlt 300 €.", "ExtraBold", 38, INK)]),
    ficon("tabler", "chalkboard", X1 + 150, 380, 140, "dfolg", fuell=GRUEN, bis="zahl"),
    pl("keine Mängelrechte", X1 + 150, 160, "dfolg", fill=WEISS, size=28, anker="m", bis="zahl"),
    ficon("tabler", "cash-banknote", X1 + 150, 380, 140, "zahl", fuell=GRUEN),
    pl("300 €", X1 + 150, 160, "zahl", fill=GELB, size=28, anker="m"),
    *paar("dfolg", [("dfolg", "ruhig"), ("hen", "froh")], [("dfolg", "ueberlegt"), ("hen", "denkt"), ("zahl", "muede")]),
]))

# J Vergütung und Arbeitsvertrag -------------------------------------------------------------------------------------------
folie([("verg", "Vergütung · stillschweigend vereinbart, §§ 612, 632 BGB"), ("p611a", "Arbeitsvertrag · § 611a BGB")], rechts_frei([
    *tafel("verg", "Vergütung und Arbeitsvertrag"),
    z("Über Geld nicht gesprochen?", 110, 190, "verg", "Bold", 36),
    z("nur gegen Vergütung zu erwarten:", 150, 250, beim("verg", "nur"), size=34),
    z("stillschweigend vereinbart", 150, 300, beim("verg", "stillschweigend"), "Bold", 34),
    z("Dienstvertrag: § 612 Abs. 1 BGB", 150, 370, "verg2", size=34),
    z("Werkvertrag: § 632 Abs. 1 BGB", 150, 420, beim("verg2", "beim", nr=2), size=34),
    blk(110, 510, 1040, 90, LILA, "p611a", [("Arbeitsvertrag, § 611a BGB", "ExtraBold", 38, INK)]),
    z("weisungsgebunden, fremdbestimmt,", 150, 630, beim("p611a", "weisungsgebundene"), size=34),
    z("in persönlicher Abhängigkeit", 150, 680, beim("p611a", "persönlicher"), size=34),
    ficon("tabler", "cash-banknote", FX, 380, 160, "verg", fuell=GRUEN, bis="p611a"),
    pl("Vergütung", FX, 160, "verg", fill=GELB, size=28, anker="m", bis="p611a"),
    ficon("tabler", "briefcase", FX, 380, 150, "p611a", fuell=LILA),
    pl("Arbeitsvertrag", FX, 160, "p611a", fill=LILA, size=28, anker="m"),
    ficon("tabler", "chalkboard", X1, 640, 100, beim("verg2", "Dienstvertrag"), fuell=GRUEN, bis="p611a"),
    ficon("ph", "paint-roller", X2, 640, 110, beim("verg2", "beim", nr=2), fuell=WEISS, bis="p611a"),
]))

# K Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · erst einordnen")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Vertrag gleich am Anfang einordnen,", 200, 200, beim("tipp", "Ordne"), "Bold", 36),
    z("bei der Anspruchsgrundlage", 200, 255, beim("tipp", "Anspruchsgrundlage"), "Bold", 36),
    z("nicht das Etikett, sondern der Inhalt:", 150, 350, "tipp2", size=36),
    z("Tätigkeit oder Erfolg?", 150, 405, beim("tipp2", "Tätigkeit"), "Bold", 36),
    nein(140, 520, "tipp3", gr=22), z("beim Dienstvertrag: nie § 634 BGB prüfen", 185, 500, "tipp3", "Bold", 34),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# L Entscheidungsbaum -------------------------------------------------------------------------------------------------------
folie([("sch", "Entscheidungsbaum"), ("s1n", "Entscheidungsbaum › nur Tätigkeit: Dienstvertrag"),
       ("s2", "Entscheidungsbaum › Erfolg: bewegliche Sache geliefert?")], [
    karte(60, 50, 1800, 900, "sch"),
    titel(glyphen("Dein Entscheidungsbaum"), 110, 90, "sch", 46),
    blk(560, 180, 800, 120, GELB, "s1", [("1. Ist ein Erfolg geschuldet?", "ExtraBold", 38, INK),
                                         ("Auslegung", "Regular", 30, INK)]),
    pfeil(760, 300, 430, 400, beim("s1n", "Nein"), breite=8, kopf=26),
    pl("Nein", 470, 315, beim("s1n", "Nein"), fill=WEISS, size=30),
    blk(110, 410, 640, 210, BLAU, beim("s1n", "Dienstvertrag"), [("Dienstvertrag, § 611 BGB", "ExtraBold", 36, INK),
                                                                  ("ohne Mängelrechte,", "Regular", 30, INK),
                                                                  ("bei Pflichtverletzung § 280", "Regular", 30, INK)]),
    pfeil(1160, 300, 1320, 400, "s2", breite=8, kopf=26),
    pl("Ja", 1290, 315, "s2", fill=WEISS, size=30),
    blk(860, 410, 940, 120, LILA, beim("s2", "zweite"), [("2. Bewegliche Sache hergestellt", "ExtraBold", 34, INK),
                                                         ("und geliefert?", "ExtraBold", 34, INK)]),
    pfeil(1150, 530, 1050, 640, "s2j", breite=8, kopf=26),
    pl("Ja", 960, 560, "s2j", fill=WEISS, size=30),
    blk(860, 650, 440, 200, GELB, beim("s2j", "Paragraf"), [("§ 650 BGB:", "ExtraBold", 36, INK),
                                                             ("Kaufrecht", "Bold", 34, INK)]),
    pfeil(1510, 530, 1600, 640, "s2n", breite=8, kopf=26),
    pl("Nein", 1600, 560, "s2n", fill=WEISS, size=30),
    blk(1340, 650, 460, 200, GRUEN, beim("s2n", "Werkvertrag"), [("Werkvertrag,", "ExtraBold", 36, INK),
                                                                  ("§ 631 BGB:", "ExtraBold", 34, INK),
                                                                  ("Abnahme, Mängelrechte", "Regular", 28, INK)]),
])

# M Merksatz (Lexi) ---------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Wer nur sein ", 0), ("Bemühen", "a"), (" schuldet,", 0)], [("schließt einen Dienstvertrag.", 0)]],
                750, 320, 44, "merke", {"a": beim("merke", "Bemühen")}),
    *markertext([[("Wer einen ", 0), ("Erfolg", "b"), (" verspricht,", 0)], [("einen Werkvertrag.", 0)]],
                750, 470, 44, "mk2", {"b": beim("mk2", "Erfolg")}),
    *markertext([[("Bewegliche Sache hergestellt", 0)], [("und geliefert: ", 0), ("Kaufrecht.", "c")]],
                750, 620, 42, "mk3", {"c": beim("mk3", "Kaufrecht")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
