"""Folge 037 · Firmenwagen geschrottet: Arbeitnehmerhaftung – wer zahlt den Schaden? – Serienstandard Open Peeps (Katzenkönig).
Übungsfall (fiktiv): Außendienstmitarbeiterin Imke fährt auf einer Dienstfahrt mit dem Firmenwagen im Stau auf einen
Lastwagen auf (Blechschaden, niemand verletzt). Ihr Chef, Herr Schäfer, verlangt 12.000 Euro Reparaturkosten.
Szenen laut ../SZENENPLAN.md: A Die Dienstfahrt, B Im Büro, C Sachverhalt, D Wortlaut § 280 I, E Prüfung I./II./Schaden,
F § 619a (Wortlaut, Beweislast), G Innerbetrieblicher Schadensausgleich (BAG GS), H Betrieblich veranlasst,
I Grad des Verschuldens, J Abwägung, K Vollkasko und Ergebnis, L Gegenfall grobe Fahrlässigkeit/Vorsatz,
M Abgrenzung § 105 SGB VII, N Klausurtipp (Lexi), O Klausurschema, P Merksatz (Lexi).
Geräusche nur bei sichtbarer Handlung (Einsteigen, Anfahren, Aufprall; CC0 aus sfx3, Herkunft in ../geraeusche_herkunft.json).
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns wie in
Folge 031 (eigene Kopie, gemeinsame Dateien unverändert)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_037/"

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
    return fl_block(x, y, w, h, fill, cue, [(glyphen(t), s, g, f) for t, s, g, f in zeilen], **k)


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
        if n.startswith(("bild:", "ficon:")) or "/op_037/" in n:
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


# --- Eigene Hilfsfunktion (wie Folge 031): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt -----------------
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


def im(cx, unten, hoehe, folge, **k):
    return fig("IM", cx, unten, hoehe, folge, **k)


def sc(cx, unten, hoehe, folge, **k):
    return fig("SC", cx, unten, hoehe, folge, **k)


BODEN, FH = 880, 480
X1, X2 = 1420, 1720                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
K1, K2, K3 = 150, 210, 270
IM_F, SC_F = BLAU, LILA                     # Farben der Namensschilder
FIRMA = (127, 178, 240, 255)                # Firmenwagen (Blau, wie Imkes Jacke)
LASTER = (249, 213, 110, 255)               # Lastwagen (Gelb)
HOLZ = (232, 205, 160, 255)

# A Fall: die Dienstfahrt -----------------------------------------------------------------------------------------------
CW, CX0, CX1, CX2 = 330, 330, 880, 1185     # Firmenwagen: Breite, parkt, steht im Stau, nach dem Auffahren
TX, TW = 1540, 440                          # Lastwagen am Stauende
IMA, IMA2 = 640, 830                        # Imke neben dem Wagen (vor der Fahrt, nach dem Aussteigen)
LOS = ("fahrt", 0.6)                        # Wagen fährt los (nach dem Einsteigen)
HALT = beim("stau", "Verkehr", ende=True)
AUF0 = beim("auffahr", "fährt")
KNALL = beim("auffahr", "Lastwagen", ende=True)
IM_RED = ("IM_schreck_r", IMA2, BODEN, FH)
folie([(NULL, "Fall · Die Dienstfahrt")], [
    hart(pl("Außendienst · Werkzeughandel", 70, 40, NULL, fill=GELB, size=44)),
    hart(linienzug([(40, BODEN), (1880, BODEN)], NULL, breite=7, farbe=INK)),
    hart(linienzug([(140, BODEN + 60), (300, BODEN + 60)], NULL, breite=6, farbe=GRAU)),
    hart(linienzug([(560, BODEN + 60), (720, BODEN + 60)], NULL, breite=6, farbe=GRAU)),
    hart(linienzug([(980, BODEN + 60), (1140, BODEN + 60)], NULL, breite=6, farbe=GRAU)),
    hart(linienzug([(1400, BODEN + 60), (1560, BODEN + 60)], NULL, breite=6, farbe=GRAU)),
    # Imke mit Musterkoffer neben dem Firmenwagen, steigt ein
    peep_voll("IM_froh_r", IMA, BODEN, FH, NULL, anim="cut", bis="fahrt"),
    ns("Imke", IMA, BODEN, NULL, IM_F, anim="cut", bis="fahrt"),
    ficon("tabler", "tools", IMA + 170, BODEN - 4, 90, NULL, fuell=GELB, anim="cut", bis="fahrt"),
    hart(ficon("tabler", "car", CX0, BODEN - 2, CW, NULL, fuell=FIRMA, bis="fahrt")),
    # Fahrt: Wagen fährt zum Stau, Namensschild fährt mit (Imke sitzt am Steuer)
    szene(bewegt(ficon("tabler", "car", CX1, BODEN - 2, CW, "fahrt", fuell=FIRMA, anim="cut", bis=AUF0), LOS, HALT,
                 CX0 - CX1), "037anfahren*", 0.7, 0.2),
    szene(bewegt(pl("Imke am Steuer", CX1, BODEN + 22, "fahrt", fill=IM_F, size=30, anker="m", anim="cut", bis=AUF0), LOS,
                 HALT, CX0 - CX1), "037tuer*", 0.8, 0.0),
    bewegt(pl("Firmenwagen", CX1, 560, beim("fahrt", "Firmenwagen"), fill=WEISS, size=28, anker="m", bis="stau"), LOS, HALT,
           CX0 - CX1),
    ficon("tabler", "map-pin", 1800, BODEN - 4, 70, beim("fahrt", "Kunden"), fuell=ROT, bis="stau"),
    # Stau: Lastwagen steht am Stauende
    ficon("tabler", "truck", TX, BODEN - 2, TW, "stau", fuell=LASTER),
    pl("Stau", TX, 450, beim("stau", "staut"), fill=ROT, size=32, anker="m", bis="blech"),
    # Auffahren: Wagen rollt zu nah heran, Aufprall
    bewegt(ficon("tabler", "car", CX2 - 30, BODEN - 2, CW, AUF0, fuell=FIRMA, anim="cut", bis=KNALL), AUF0, KNALL, CX1 - CX2 + 30),
    bewegt(pl("Imke am Steuer", CX2 - 30, BODEN + 22, AUF0, fill=IM_F, size=30, anker="m", anim="cut", bis=KNALL), AUF0, KNALL,
           CX1 - CX2 + 30),
    pl("zu wenig Abstand", 700, 330, beim("auffahr", "Abstand"), fill=GELB, size=32, anker="m", bis="i1"),
    szene(ficon("tabler", "car-crash", CX2, BODEN - 2, CW + 10, KNALL, fuell=FIRMA, anim="cut"), "037aufprall*", 0.8, -0.05),
    # Imke steigt aus (unverletzt) und spricht
    *redet("IM_schreck_r", IMA2, BODEN, FH, "i1", "blech"),
    *im(IMA2, BODEN, FH, [("blech", "sorge_r"), ("kosten", "ernst_r")], erst="cut"),
    ns("Imke", IMA2, BODEN, "i1", IM_F, anim="cut"),
    blase("sprech", 520, 190, "i1", 560, 250, inhalt=["Oh nein, der", "Firmenwagen!"], textsize=40, figur=IM_RED, bis="blech"),
    pl("niemand verletzt", 420, 160, "blech", fill=GRUEN, size=32, anker="m"),
    ficon("tabler", "shield-check", TX, 560, 110, "lkw", fuell=GRUEN),
    pl("Haftpflicht zahlt den Lastwagen-Schaden", 1300, 160, "lkw", fill=GRUEN, size=30, anker="m"),
    pl("Fahrerin mitversichert", 1300, 240, beim("lkw", "mitversichert"), fill=WEISS, size=28, anker="m"),
    ficon("tabler", "receipt", CX2, 610, 90, "kosten", fuell=WEISS),
    pl("Reparatur Firmenwagen: 12.000 €", CX2, 330, beim("kosten", "zwölftausend"), fill=ROT, size=32, anker="m"),
    ficon("tabler", "shield-off", CX2 - 170, 472, 76, beim("kasko0", "Vollkaskoversicherung"), fuell=WEISS),
    pl("keine Vollkasko", CX2 + 20, 410, beim("kasko0", "Vollkaskoversicherung"), fill=WEISS, size=28, anker="m"),
])

# B Im Büro ---------------------------------------------------------------------------------------------------------------
IMB, SCB = 480, 1440
SC_RED = ("SC_redet", SCB, BODEN, FH)
IM_RED2 = ("IM_redet_r", IMB, BODEN, FH)
folie([("buero", "Fall · Im Büro"), ("frage", "Fall · Die Frage")], [
    pl("Im Büro von Herrn Schäfer", 70, 40, "buero", fill=LILA, size=44),
    linienzug([(40, BODEN), (1880, BODEN)], "buero", breite=7, farbe=INK),
    karte(830, 690, 420, BODEN - 690, "buero", fill=HOLZ, rund=8, schatten=6, rand=5),
    ficon("tabler", "receipt", 960, 690, 110, beim("buero", "Geld"), fuell=WEISS),
    pl("12.000 €", 1110, 640, beim("buero", "Geld"), fill=ROT, size=30, anker="m"),
    *im(IMB, BODEN, FH, [("buero", "sorge_r")], bis="i2"),
    *redet("IM_redet_r", IMB, BODEN, FH, "i2", "frage"),
    *im(IMB, BODEN, FH, [("frage", "denkt_r")], erst="cut"),
    ns("Imke", IMB, BODEN, "buero", IM_F),
    *sc(SCB, BODEN, FH, [(beim("buero", "Herr"), "streng")], bis="s1"),
    *redet("SC_redet", SCB, BODEN, FH, "s1", "i2"),
    *sc(SCB, BODEN, FH, [("i2", "denkt")], erst="cut"),
    ns("Herr Schäfer, Chef", SCB, BODEN, beim("buero", "Herr"), SC_F),
    blase("sprech", 720, 210, "s1", 1150, 230, inhalt=["Sie haben den Wagen beschädigt.", "Sie zahlen die Reparatur!"],
          textsize=34, figur=SC_RED, bis="i2"),
    blase("sprech", 560, 190, "i2", 760, 250, inhalt=["Aber ich war doch", "dienstlich unterwegs!"], textsize=36,
          figur=IM_RED2, bis="frage"),
    pl("Muss Imke 12.000 € ersetzen?", 960, 170, "frage", fill=PINK, size=40, anker="m"),
    pl("Was ändert der Grad ihres Verschuldens?", 960, 270, "frage2", fill=WEISS, size=32, anker="m"),
    ficon("tabler", "scale", 960, 470, 120, "frage2", fuell=WEISS),
])

# C Sachverhalt --------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Imke arbeitet im Außendienst eines Werkzeughandels und verdient 3.000 Euro brutto im Monat. Auf einer Dienstfahrt "
    "zu einem Kunden ist sie im Stau einen Moment unaufmerksam, hält zu wenig Abstand und fährt auf einen Lastwagen auf. "
    "Ein grober Verstoß liegt nicht vor. Niemand wird verletzt.",
    "Den Schaden am Lastwagen zahlt die Haftpflichtversicherung des Firmenwagens. Die Reparatur des Firmenwagens "
    "kostet 12.000 Euro; eine Vollkaskoversicherung besteht nicht. Ihr Chef, der Inhaber Herr Schäfer, verlangt den "
    "vollen Betrag von ihr.",
], "Muss Imke die 12.000 Euro ersetzen?")

# D Anspruchsgrundlage: Wortlaut § 280 Abs. 1 BGB ---------------------------------------------------------------------------------
W280 = ["„Verletzt der Schuldner eine Pflicht aus dem Schuldverhältnis, so",
        "kann der Gläubiger Ersatz des hierdurch entstehenden Schadens",
        "verlangen. Dies gilt nicht, wenn der Schuldner die Pflichtverletzung",
        "nicht zu vertreten hat.“"]
w280, w280_y = wortlaut(80, 190, 1100, W280, "§ 280 Abs. 1 BGB", beim("agl", "Paragraf"), marken=[
    (0, "Pflicht aus dem Schuldverhältnis", beim("w280", "Pflicht")),
    (1, "Ersatz des hierdurch entstehenden Schadens", beim("w280", "Ersatz")),
    (2, "Dies gilt nicht", "w280b"), (3, "nicht zu vertreten hat", beim("w280b", "nicht", nr=2))], size=31)
folie([("agl", "Anspruch · § 280 Abs. 1 BGB")], rechts_frei([
    *tafel("agl", "Anspruch aus § 280 Abs. 1 BGB?"),
    *w280,
    ficon("tabler", "car-crash", FX, 330, 170, "agl", fuell=FIRMA),
    pl("12.000 €", FX, 350, "agl", fill=ROT, size=28, anker="m"),
    *sc(X2, FB, FR, [("agl", "streng")]),
    ns("Herr Schäfer", X2, FB, "agl", SC_F),
    *im(X1, FB, FR, [("agl", "sorge"), ("w280b", "denkt")], d=0.2),
    ns("Imke", X1, FB, "agl", IM_F, d=0.2),
]))

# E Prüfung: I. Schuldverhältnis, II. Pflichtverletzung, Schaden ------------------------------------------------------------------
folie([("sv1", "A. Schäfer gegen Imke, § 280 Abs. 1 BGB › I. Schuldverhältnis"),
       ("pv", "A. Schäfer gegen Imke, § 280 Abs. 1 BGB › II. Pflichtverletzung"),
       ("schad", "A. Schäfer gegen Imke, § 280 Abs. 1 BGB › Schaden")], rechts_frei([
    *tafel("sv1", "A. Schäfer gegen Imke"),
    ok(140, 220, "sv1", gr=20), z("I. Schuldverhältnis: Arbeitsvertrag, § 611a BGB", 185, 200, "sv1", "Bold", 34),
    z("II. Pflichtverletzung: Rücksicht auf das Eigentum", 185, 300, "pv", "Bold", 34),
    z("des Arbeitgebers, § 241 Abs. 2 BGB", 225, 355, beim("pv", "Arbeitgebers"), size=32),
    ok(140, 450, "pv2", gr=20), z("Auffahrunfall: Pflicht verletzt", 185, 430, "pv2", size=32),
    ok(140, 550, "schad", gr=20), z("Schaden: 12.000 € Reparatur", 185, 530, "schad", "Bold", 34),
    ficon("tabler", "file-text", FX, 330, 110, "sv1", fuell=WEISS, bis="pv"),
    pl("Arbeitsvertrag", FX, 350, "sv1", fill=WEISS, size=28, anker="m", bis="pv"),
    ficon("tabler", "car", FX, 330, 190, "pv", fuell=FIRMA, bis="schad"),
    pl("Eigentum des Arbeitgebers", FX, 350, "pv", fill=WEISS, size=28, anker="m", bis="schad"),
    ficon("tabler", "receipt", FX, 330, 100, "schad", fuell=WEISS),
    pl("12.000 €", FX, 350, "schad", fill=ROT, size=28, anker="m"),
    *sc(X2, FB, FR, [("sv1", "ruhig"), ("schad", "streng")]),
    ns("Herr Schäfer", X2, FB, "sv1", SC_F),
    *im(X1, FB, FR, [("sv1", "ernst"), ("pv2", "sorge")], d=0.2),
    ns("Imke", X1, FB, "sv1", IM_F, d=0.2),
]))

# F § 619a BGB: Wortlaut und Beweislast --------------------------------------------------------------------------------------------
W619 = ["„Abweichend von § 280 Abs. 1 hat der Arbeitnehmer dem Arbeitgeber",
        "Ersatz für den aus der Verletzung einer Pflicht aus dem",
        "Arbeitsverhältnis entstehenden Schaden nur zu leisten, wenn er",
        "die Pflichtverletzung zu vertreten hat.“"]
w619, w619_y = wortlaut(80, 190, 1100, W619, "§ 619a BGB", "w619", marken=[
    (0, "Abweichend von § 280 Abs. 1", beim("w619b", "Abweichend")),
    (2, "nur zu leisten, wenn er", beim("w619b", "nur")),
    (3, "die Pflichtverletzung zu vertreten hat", beim("w619b", "Pflichtverletzung"))], size=31)
folie([("w619", "A. Schäfer gegen Imke › III. Vertretenmüssen, § 619a BGB"),
       ("bew", "A. Schäfer gegen Imke › III. Vertretenmüssen · Beweislast")], rechts_frei([
    *tafel("w619", "III. Vertretenmüssen: § 619a BGB"),
    *w619,
    nein(140, w619_y + 70, "bew", gr=20), z("Imke muss sich nicht entlasten", 185, w619_y + 50, "bew", size=32),
    ok(140, w619_y + 140, "bew2", gr=20), z("Beweislast: Herr Schäfer", 185, w619_y + 120, "bew2", "Bold", 34),
    zit("BAG, Urt. v. 21.5.2015 – 8 AZR 116/14 u. a., Rn. 25", 225, w619_y + 175, beim("bew2", "beweisen")),
    ok(140, w619_y + 260, "bew3", gr=20),
    z("unaufmerksam: fahrlässig, § 276 Abs. 2 BGB", 185, w619_y + 240, "bew3", size=32),
    ficon("tabler", "scale", FX, 330, 130, "bew2", fuell=WEISS),
    pl("Beweislast", FX, 350, "bew2", fill=WEISS, size=28, anker="m"),
    *sc(X2, FB, FR, [("w619", "ruhig"), ("bew2", "denkt")]),
    ns("Herr Schäfer", X2, FB, "w619", SC_F),
    *im(X1, FB, FR, [("w619", "ernst"), ("bew", "froh"), ("bew3", "sorge")], d=0.2),
    ns("Imke", X1, FB, "w619", IM_F, d=0.2),
]))

# G Innerbetrieblicher Schadensausgleich (BAG GS) -------------------------------------------------------------------------------------
folie([("ibs", "A. Schäfer gegen Imke › Haftung beschränkt?"),
       ("gs", "Innerbetrieblicher Schadensausgleich · BAG GS 1994")], rechts_frei([
    *tafel("ibs", "Innerbetrieblicher Schadensausgleich", size=44),
    z("alles zahlen?", 185, 190, "ibs", "Bold", 34),
    nein(140, 210, beim("ibs", "Nein"), gr=20),
    z("Nein.", 185 + F("Bold", 34).getlength("alles zahlen? "), 190, beim("ibs", "Nein"), "Bold", 34),
    z("BAG GS, Beschl. v. 27.9.1994 – GS 1/89 (A)", 110, 280, "gs", "Bold", 34),
    zit("BAGE 78, 56; Gründe I.–IV. (Volltext nicht amtlich online)", 150, 330, "gs"),
    ok(140, 420, "gs2", gr=20), z("betrieblich veranlasste Tätigkeit:", 185, 400, "gs2", "Bold", 34),
    z("Haftung des Arbeitnehmers beschränkt", 185, 450, beim("gs2", "Haftung"), size=32),
    z("Grundlage: § 254 BGB entsprechend", 185, 540, "p254", "Bold", 34),
    z("Betriebsrisiko des Arbeitgebers:", 185, 630, "risk", "Bold", 34),
    z("Organisation des Betriebs,", 225, 685, beim("risk", "organisiert"), size=32),
    z("Gestaltung der Arbeitsbedingungen", 225, 735, beim("risk", "gestaltet"), size=32),
    ficon("tabler", "building-store", FX, 330, 170, "risk", fuell=GELB),
    pl("Betriebsrisiko", FX, 350, "risk", fill=GELB, size=28, anker="m"),
    *sc(X2, FB, FR, [("ibs", "streng"), ("risk", "denkt")]),
    ns("Herr Schäfer", X2, FB, "ibs", SC_F),
    *im(X1, FB, FR, [("ibs", "sorge"), ("gs2", "froh")], d=0.2),
    ns("Imke", X1, FB, "ibs", IM_F, d=0.2),
]))

# H 1. Betrieblich veranlasste Tätigkeit -------------------------------------------------------------------------------------------------
folie([("bv", "Haftungsbeschränkung › 1. betrieblich veranlasste Tätigkeit")], rechts_frei([
    *tafel("bv", "1. Betrieblich veranlasste Tätigkeit", size=44),
    z("dem Arbeitnehmer übertragen oder", 110, 200, "bv2", "Bold", 34),
    z("im Interesse des Betriebs", 110, 255, beim("bv2", "Interesse"), "Bold", 34),
    zit("BAG GS, Gründe IV. 2; BAG 8 AZR 418/09, Rn. 14", 150, 310, beim("bv2", "Interesse")),
    ok(140, 420, "bv3", gr=20), z("Fahrt zum Kunden: gehört zur Arbeit", 185, 400, "bv3", size=34),
    nein(140, 520, "bv4", gr=20), z("anders: Privatfahrt am Wochenende", 185, 500, "bv4", size=34),
    z("allgemeines Lebensrisiko, keine Beschränkung", 225, 555, beim("bv4", "allgemeines"), size=31, farbe=TEXT),
    ficon("tabler", "briefcase", FX, 330, 130, "bv", fuell=GELB, bis="bv3"),
    pl("betrieblich veranlasst?", FX, 350, beim("bv", "betrieblich"), fill=WEISS, size=28, anker="m", bis="bv3"),
    ficon("tabler", "map-pin", X1, 330, 80, "bv3", fuell=ROT, bis="bv4"),
    ficon("tabler", "car", X2, 330, 200, "bv3", fuell=FIRMA, bis="bv4"),
    pl("Dienstfahrt", (X1 + X2) // 2, 350, "bv3", fill=GRUEN, size=28, anker="m", bis="bv4"),
    ficon("tabler", "beach", (X1 + X2) // 2, 330, 140, "bv4", fuell=GELB),
    pl("Wochenende", (X1 + X2) // 2, 350, beim("bv4", "Wochenende"), fill=WEISS, size=28, anker="m"),
    *im(FX, FB, FR, [("bv", "ruhig"), ("bv3", "froh"), ("bv4", "denkt")]),
    ns("Imke", FX, FB, "bv", IM_F),
]))

# I 2. Grad des Verschuldens -----------------------------------------------------------------------------------------------------------
SY = [200, 330, 460, 590]
folie([("stufen", "Haftungsbeschränkung › 2. Grad des Verschuldens")], rechts_frei([
    *tafel("stufen", "2. Grad des Verschuldens"),
    blk(110, SY[0], 1040, 100, GRUEN, "st1", [("leichteste Fahrlässigkeit: keine Haftung", "ExtraBold", 36, INK)]),
    blk(110, SY[1], 1040, 100, GELB, "st2", [("normale (mittlere) Fahrlässigkeit: Teilung", "ExtraBold", 36, INK)]),
    blk(110, SY[2], 1040, 100, ORANGE, "st3", [("grobe Fahrlässigkeit: in aller Regel voll", "ExtraBold", 36, INK)]),
    blk(110, SY[3], 1040, 100, ROT, "st4", [("Vorsatz: volle Haftung", "ExtraBold", 36, INK)]),
    zit("BAG GS, Gründe I. 1; BAG 8 AZR 418/09, Rn. 17", 110, 730, "st1"),
    ficon("tabler", "circle-half", FX, 330, 120, "st2", fuell=GELB, bis="st3"),
    pl("Teilung", FX, 350, "st2", fill=GELB, size=28, anker="m", bis="st3"),
    ficon("tabler", "alert-triangle", FX, 330, 120, "st3", fuell=ROT),
    pl("in aller Regel voll", FX, 350, "st3", fill=ORANGE, size=28, anker="m"),
    *im(X1, FB, FR, [("stufen", "ernst"), ("st1", "froh"), ("st3", "sorge")]),
    ns("Imke", X1, FB, "stufen", IM_F),
    *sc(X2, FB, FR, [("stufen", "ruhig"), ("st4", "streng")], d=0.2),
    ns("Herr Schäfer", X2, FB, "stufen", SC_F, d=0.2),
]))

# J 3. Abwägung im Fall --------------------------------------------------------------------------------------------------------------------
folie([("mittel", "Haftungsbeschränkung › 2. Grad des Verschuldens: Imke"),
       ("abw", "Haftungsbeschränkung › 3. Abwägung aller Umstände")], rechts_frei([
    *tafel("mittel", "Imkes Verschulden und die Abwägung", size=44),
    z("unaufmerksam, zu wenig Abstand", 110, 190, "mittel", "Bold", 34),
    nein(140, 270, beim("mittel", "grober"), gr=20), z("kein grober Verstoß", 185, 250, beim("mittel", "grober"), size=32),
    ok(140, 340, "mittel2", gr=20), z("normale Fahrlässigkeit", 185, 320, "mittel2", "Bold", 34),
    z("Teilung nach Abwägung aller Umstände:", 110, 420, "abw", "Bold", 34),
    z("· Grad des Verschuldens", 150, 480, "abw1", size=32),
    z("· Gefahr der Tätigkeit", 150, 530, beim("abw1", "Gefahr"), size=32),
    z("· Schaden zum Verdienst: 12.000 € = 4 Monatsgehälter", 150, 580, "abw2", size=32),
    z("· Risiko, das der Arbeitgeber versichern konnte", 150, 630, "abw3", size=32),
    zit("BAG GS, Gründe IV. 1; BAG 8 AZR 418/09, Rn. 18", 150, 700, "abw1"),
    ficon("tabler", "scale", FX, 330, 150, "abw", fuell=WEISS),
    pl("Abwägung", FX, 350, "abw", fill=WEISS, size=28, anker="m"),
    *im(X1, FB, FR, [("mittel", "sorge"), ("mittel2", "ernst"), ("abw2", "denkt")]),
    ns("Imke", X1, FB, "mittel", IM_F),
    *sc(X2, FB, FR, [("mittel", "ruhig"), ("abw3", "denkt")], d=0.2),
    ns("Herr Schäfer", X2, FB, "mittel", SC_F, d=0.2),
]))

# K Vollkasko und Ergebnis -------------------------------------------------------------------------------------------------------------------
folie([("kasko", "Haftungsbeschränkung › 3. Abwägung · Vollkasko"),
       ("erg", "A. Schäfer gegen Imke › Ergebnis")], rechts_frei([
    *tafel("kasko", "Und die Vollkasko?"),
    nein(140, 210, "kasko1", gr=20), z("keine Pflicht, sie abzuschließen", 185, 190, "kasko1", "Bold", 34),
    zit("BAG, Urt. v. 15.11.2012 – 8 AZR 705/11, Rn. 45", 225, 245, beim("kasko1", "abzuschließen")),
    ok(140, 340, "kasko2", gr=20), z("aber: versicherbares Risiko spricht für Imke", 185, 320, "kasko2", "Bold", 34),
    zit("BAG GS, Gründe IV. 1; BAG 8 AZR 418/09, Rn. 25", 225, 375, beim("kasko2", "Abwägung")),
    blk(110, 470, 1040, 140, GRUEN, "erg", [("Ergebnis: Imke trägt nur", "ExtraBold", 38, INK),
                                          ("einen Teil des Schadens", "ExtraBold", 38, INK)]),
    z("Quote: das Gericht im Einzelfall", 110, 650, "erg2", size=34),
    ficon("tabler", "shield-off", FX, 330, 110, "kasko", fuell=WEISS, bis="erg"),
    pl("keine Vollkasko", FX, 350, "kasko", fill=WEISS, size=28, anker="m", bis="erg"),
    ficon("tabler", "chart-pie", FX, 330, 120, "erg", fuell=GELB),
    pl("nur ein Teil", FX, 350, "erg", fill=GRUEN, size=28, anker="m"),
    *im(X1, FB, FR, [("kasko", "denkt"), ("kasko2", "froh"), ("erg", "zufrieden")]),
    ns("Imke", X1, FB, "kasko", IM_F),
    *sc(X2, FB, FR, [("kasko", "ruhig"), ("kasko2", "sorge"), ("erg", "ruhig")], d=0.2),
    ns("Herr Schäfer", X2, FB, "kasko", SC_F, d=0.2),
]))

# L Gegenfall: grobe Fahrlässigkeit, Vorsatz ---------------------------------------------------------------------------------------------------
folie([("grob", "Gegenfall · grobe Fahrlässigkeit"), ("vors", "Gegenfall · Vorsatz")], rechts_frei([
    *tafel("grob", "Gegenfall: Handy am Steuer"),
    z("Nachricht ins Handy getippt", 110, 185, beim("grob", "Nachricht"), "Bold", 34),
    z("angenommen: grob fahrlässig", 110, 235, "grob1", "Bold", 34),
    z("Sorgfalt in ungewöhnlich hohem Maß verletzt", 150, 285, beim("grob1", "Sorgfalt"), size=31),
    zit("BAG, Urt. v. 15.11.2012 – 8 AZR 705/11, Rn. 22", 150, 330, beim("grob1", "Sorgfalt")),
    z("in aller Regel: ganzer Schaden", 110, 385, "grob2", "Bold", 34),
    ok(140, 460, "grob3", gr=20), z("aber Erleichterung möglich:", 185, 440, "grob3", size=32),
    z("deutliches Missverhältnis Verdienst – Schadensrisiko", 185, 490, "grob4", size=31),
    zit("8 AZR 705/11, Rn. 26; 8 AZR 418/09, Rn. 25", 185, 540, "grob4"),
    nein(140, 620, "grob5", gr=20), z("keine feste Obergrenze, etwa 3 Monatsgehälter", 185, 600, "grob5", size=32),
    zit("8 AZR 705/11, Rn. 27 ff.", 185, 650, "grob5"),
    blk(110, 720, 1040, 100, ROT, "vors", [("Vorsatz: volle Haftung", "ExtraBold", 38, INK)]),
    ficon("tabler", "device-mobile-message", FX, 330, 110, beim("grob", "Nachricht"), fuell=WEISS),
    pl("Handy am Steuer", FX, 350, beim("grob", "Handy"), fill=ORANGE, size=28, anker="m"),
    *im(FX, FB, FR, [("grob", "ernst"), ("grob2", "sorge"), ("grob3", "denkt"), ("vors", "ernst")]),
    ns("Imke", FX, FB, "grob", IM_F),
]))

# M Abgrenzung: Personenschaden, § 105 SGB VII ------------------------------------------------------------------------------------------------
folie([("pers", "Abgrenzung · Personenschaden, § 105 SGB VII")], rechts_frei([
    *tafel("pers", "Abgrenzung: Personenschaden"),
    z("Kollege fährt mit und wird verletzt?", 110, 190, beim("pers", "Kollegen"), "Bold", 34),
    z("Personenschaden: § 105 Abs. 1 SGB VII", 110, 290, beim("pers", "Paragraf"), "Bold", 34),
    ok(140, 390, "pers2", gr=20), z("Haftung grundsätzlich nur bei Vorsatz", 185, 370, "pers2", size=34),
    zit("§ 105 Abs. 1 Satz 1 SGB VII (Stand 2.10.2026)", 185, 425, "pers2"),
    ficon("tabler", "users", FX, 330, 150, beim("pers", "Kollegen"), fuell=GELB),
    pl("Kollege", FX, 350, beim("pers", "Kollegen"), fill=GELB, size=28, anker="m"),
    *im(FX, FB, FR, [("pers", "denkt"), ("pers2", "ernst")]),
    ns("Imke", FX, FB, "pers", IM_F),
]))

# N Klausurtipp (Lexi) -----------------------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · Haftungsbeschränkung erst beim Umfang"), ("tipp2", "Klausurtipp · § 619a BGB nicht vergessen")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Haftungsbeschränkung erst prüfen, wenn", 200, 200, beim("tipp", "Prüfe"), "Bold", 34),
    z("der Anspruch aus § 280 BGB steht", 200, 255, beim("tipp", "Anspruch"), "Bold", 34),
    z("etwa beim Umfang des Ersatzes", 200, 330, "tipp1", size=34),
    ok(140, 450, "tipp2", gr=20), z("§ 619a BGB: Vertretenmüssen nicht vermutet", 185, 430, "tipp2", size=34),
    ok(140, 540, "tipp3", gr=20), z("gilt auch für den Anspruch aus § 823 BGB", 185, 520, "tipp3", size=34),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# O Klausurschema ----------------------------------------------------------------------------------------------------------------------------
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel(glyphen("Klausurschema: Arbeitnehmerhaftung"), 110, 90, "sch", 46),
    z("Anspruch des Arbeitgebers aus § 280 Abs. 1 BGB", K1, 190, "sc1", "Bold", 36, rechts=1820),
    z("I. Schuldverhältnis: Arbeitsvertrag", K1, 260, "sc2", "Bold", 36, rechts=1820),
    z("II. Pflichtverletzung", K1, 325, "sc3", "Bold", 36, rechts=1820),
    z("III. Vertretenmüssen (Beweislast § 619a BGB)", K1, 390, "sc4", "Bold", 36, rechts=1820),
    z("IV. Schaden", K1, 455, "sc5", "Bold", 36, rechts=1820),
    z("V. Haftungsbeschränkung", K1, 520, "sc6", "Bold", 36, rechts=1820),
    z("1. betrieblich veranlasste Tätigkeit", K3, 580, beim("sc6", "Erstens"), size=34, rechts=1820),
    z("2. Grad des Verschuldens", K3, 635, "sc7", size=34, rechts=1820),
    z("3. Abwägung aller Umstände (§ 254 BGB analog)", K3, 690, "sc8", size=34, rechts=1820),
])

# P Merksatz (Lexi) -----------------------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Wer bei der Arbeit einen Schaden anrichtet,", 0)], [("haftet nach dem ", 0), ("Grad seines Verschuldens.", "a")]],
                750, 320, 44, "merke", {"a": beim("merke", "Grad")}),
    *markertext([[("Bei leichtester Fahrlässigkeit ", 0), ("gar nicht,", "b")], [("bei normaler ", 0), ("anteilig,", "c")],
                 [("bei grober ", 0), ("in aller Regel voll.", "d")]],
                750, 540, 42, "m2", {"b": beim("m2", "gar"), "c": beim("m2", "anteilig"), "d": beim("m2", "in")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
