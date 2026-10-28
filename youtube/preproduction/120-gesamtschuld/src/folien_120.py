"""Folge 120 · Gesamtschuld §§ 421, 426 BGB: Einer zahlt für alle – und dann? – Serienstandard Open Peeps (Katzenkönig).
Fall: Insa, Lars und Rieke wohnen in einer WG, alle drei haben den Stromvertrag unterschrieben; Rieke ist ausgezogen und
zahlungsunfähig; Jahresabrechnung 900 € Nachzahlung; der Versorger verlangt alles von Insa, sie zahlt; Lars will nur 300 €
erstatten.
Szenen laut ../SZENENPLAN.md: A1 WG-Küche (Vertrag, Auszug, Abrechnung, Anruf), A2 Telefonat mit dem Versorger, Zahlung,
A3 Insa und Lars, Frage, B Sachverhalt, C zwei Ebenen, D1 § 421 S. 1 (Wortlaut), D2 Entstehungsgründe, D3 im Fall,
E § 422 Abs. 1, § 425, F § 426 Abs. 1 S. 1 (Wortlaut), G § 426 Abs. 1 S. 2 (Wortlaut), H § 426 Abs. 2 S. 1 (Wortlaut),
§§ 412, 401, I Verhältnis Abs. 1/Abs. 2, J Rechnung, K Ergebnis (Bühne), L Klausurtipp (Lexi), M Klausurschema,
N Merksatz (Lexi).
Zwei Handlungsgeräusche (Tür beim Auszug, Telefon beim Anruf; ../geraeusche_herkunft.json). Namensschild jeder Figur,
solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns als eigene Kopie aus Folge 099
(gemeinsame Dateien unverändert). Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_120/"

FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
ZITAT = (246, 246, 250, 255)
HELLROT = (250, 205, 198, 255)
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


def tafel(cue, titel_, h=840, fill=WEISS, size=46):
    """Rechtstafel links, rechts bleibt Platz für die Figuren."""
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(glyphen(titel_), 110, 100, cue, size)]


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
        if n.startswith(("bild:", "ficon:")) or "/op_120/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def wortlaut(x, y, w, zeilen, quelle, cue, marken=(), size=32, bis=None):
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 089/099) -------------------------------------
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


BODEN, FH = 860, 480
X1, X2 = 1420, 1720                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
PX, PY, PU = 1570, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"IN": "Insa", "LA": "Lars", "RI": "Rieke", "SB": "Stromversorger"}
NFARBE = {"IN": ROT, "LA": BLAU, "RI": LILA, "SB": GRUEN}


def boden(cue, hart_=False):
    e = linienzug([(40, BODEN), (1880, BODEN)], cue, breite=7, farbe=INK)
    return hart(e) if hart_ else e


def requisit(folge):
    """Wechselndes Requisit über den Figuren: folge = [(cue, (set, icon, breite, fuell), pillentext, pillenfarbe)]."""
    els = []
    for i, (c, ic, txt, pf) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else None
        if ic:
            s_, n_, br, fu = ic
            els.append(ficon(s_, n_, PX, PU, br, c, fuell=fu, bis=b))
        if txt:
            els.append(pl(txt, PX, PY, c, fill=pf, size=28, anker="m", bis=b))
    return els


def paar(c0, l, lf, r, rf):
    """Tafelszene: zwei Figuren rechts der Tafel, beide blicken zur Tafel (nach links)."""
    return [*fig(l, X1, FB, FR, lf), ns(NAME[l], X1, FB, c0, NFARBE[l], d=0.1),
            *fig(r, X2, FB, FR, rf, d=0.2), ns(NAME[r], X2, FB, c0, NFARBE[r], d=0.3)]


def fl(name, cx, folge, bis=None, erst="cut", unten=BODEN, hoehe=FH, d=0.0):
    """Figur auf der Bühne: folge = [(cue, ansicht)] mit Ansichtsnamen ohne Präfix (z. B. 'ruhig_r')."""
    return fig(name, cx, unten, hoehe, folge, bis=bis, erst=erst, d=d)


# A1 Fall: die WG-Küche --------------------------------------------------------------------------------------------------------
IX1, LX1, RX1, RX1b = 860, 1190, 1520, 1690
folie([(NULL, "Fall · Die Wohngemeinschaft"), ("auszug", "Fall · Rieke zieht aus"),
       ("abr", "Fall · Die Jahresabrechnung")], [
    hart(pl("Insa, Lars und Rieke wohnen in einer WG", 70, 30, NULL, fill=GELB, size=44)),
    hart(boden(NULL)),
    hart(ficon("tabler", "fridge", 470, BODEN, 190, NULL, fuell=WEISS)),
    hart(ficon("fluent-emoji-flat", "light-bulb", 470, 470, 70, NULL)),
    *fl("IN", IX1, [(NULL, "ruhig"), ("abr", "staunt"), ("anruf", "ruhig")]),
    hart(ns("Insa", IX1, BODEN, NULL, NFARBE["IN"])),
    *fl("LA", LX1, [(NULL, "ruhig"), ("abr", "sorge")]),
    hart(ns("Lars", LX1, BODEN, NULL, NFARBE["LA"])),
    *fl("RI", RX1, [(NULL, "ruhig_r")], bis="auszug"),
    bis_(hart(ns("Rieke", RX1, BODEN, NULL, NFARBE["RI"])), "auszug"),
    # Stromvertrag mit drei Unterschriften
    bis_(karte(90, 120, 560, 250, "vertrag", fill=WEISS, rund=10, schatten=6, rand=4), "abr"),
    ficon("fluent-emoji-flat", "high-voltage", 140, 210, 60, "vertrag", bis="abr"),
    z("Stromvertrag", 185, 140, "vertrag", "Bold", 38, rechts=630, bis="abr"),
    z("Unterschriften:", 120, 215, beim("vertrag", "alle"), size=30, rechts=630, bis="abr"),
    z("Insa", 120, 270, beim("vertrag", "alle"), "ExtraBold", 36, rechts=630, bis="abr"),
    z("Lars", 280, 270, beim("vertrag", "drei"), "ExtraBold", 36, rechts=630, bis="abr"),
    z("Rieke", 440, 270, beim("vertrag", "unterschrieben"), "ExtraBold", 36, rechts=630, bis="abr"),
    # Auszug: Rieke an der Tür, mit Umzugskarton
    szene(ficon("tabler", "door-exit", 1830, BODEN, 110, "auszug", fuell=WEISS), "120tuer*", 0.9, 0.2),
    *fl("RI", RX1b, [("auszug", "sorge"), ("pleite", "traurig")]),
    ns("Rieke", RX1b, BODEN, "auszug", NFARBE["RI"]),
    ficon("fluent-emoji-flat", "package", RX1b - 150, BODEN, 110, "auszug"),
    pl("zieht aus", RX1b, 300, beim("auszug", "zieht"), fill=WEISS, size=30, anker="m"),
    pl("zahlungsunfähig", RX1b, 230, "pleite", fill=ROT, size=32, anker="m"),
    # Jahresabrechnung
    karte(90, 120, 560, 250, "abr", fill=WEISS, rund=10, schatten=6, rand=4),
    ficon("fluent-emoji-flat", "receipt", 150, 230, 70, "abr"),
    z("Jahresabrechnung", 200, 140, "abr", "Bold", 38, rechts=630),
    z("Nachzahlung:", 200, 215, beim("abr", "Nachzahlung"), size=34, rechts=630),
    z("900 €", 200, 270, beim("abr", "Nachzahlung"), "ExtraBold", 48, farbe=DROT, rechts=630),
    szene(ficon("fluent-emoji-flat", "telephone-receiver", IX1 - 190, 470, 80, "anruf"), "120telefon*", 0.8, 0.0),
    pl("Der Versorger meldet sich", IX1, 230, beim("anruf", "meldet"), fill=GRUEN, size=30, anker="m"),
])

# A2 Fall: Telefonat mit dem Versorger, Insa zahlt ------------------------------------------------------------------------------
SX2, IX2 = 470, 1450
folie([("sb1", "Fall · Der Versorger verlangt alles"), ("zahlt", "Fall · Insa zahlt")], [
    pl("Der Versorger ruft Insa an", 70, 30, "sb1", fill=GELB, size=44),
    boden("sb1"),
    ficon("fluent-emoji-flat", "high-voltage", 170, 470, 100, "sb1"),
    ficon("tabler", "desk", SX2 + 300, BODEN, 260, "sb1", fuell=GELB),
    ficon("fluent-emoji-flat", "telephone-receiver", SX2 + 300, BODEN - 150, 80, "sb1"),
    *redet("SB_redet_r", SX2, BODEN, FH, "sb1", "in1"),
    *fl("SB", SX2, [("in1", "ruhig_r"), ("zahlt", "froh_r")]),
    ns("Stromversorger", SX2, BODEN, "sb1", NFARBE["SB"]),
    *redet("IN_redet", IX2, BODEN, FH, "in1", "zahlt"),
    *fl("IN", IX2, [("sb1", "sorge")], bis="in1"),
    *fl("IN", IX2, [("zahlt", "ruhig")]),
    ns("Insa", IX2, BODEN, "sb1", NFARBE["IN"]),
    ficon("tabler", "phone", IX2 - 190, 520, 80, "sb1", fuell=WEISS),
    blase("sprech", 700, 220, "sb1", 900, 230, inhalt=["Die 900 € verlangen wir", "vollständig von Ihnen."], textsize=36,
          figur=("SB_redet_r", SX2, BODEN, FH), bis="in1"),
    blase("sprech", 640, 220, "in1", 1100, 230, inhalt=["Von mir allein?", "Wir waren doch zu dritt!"], textsize=36,
          figur=("IN_redet", IX2, BODEN, FH), bis="zahlt"),
    ficon("fluent-emoji-flat", "euro-banknote", 1000, 560, 130, "zahlt"),
    pl("Insa zahlt 900 €", 1000, 330, beim("zahlt", "zahlt"), fill=GRUEN, size=34, anker="m"),
    pfeil(1250, 520, 760, 520, beim("zahlt", "neunhundert"), breite=10, kopf=30),
])

# A3 Fall: Insa und Lars, die Frage ----------------------------------------------------------------------------------------------
IX3, LX3 = 700, 1300
folie([("lars", "Fall · Insa verlangt Ausgleich"), ("frage", "Fall · Die Frage")], [
    pl("Insa wendet sich an Lars", 70, 30, "lars", fill=GELB, size=44, bis="frage"),
    boden("lars"),
    ficon("tabler", "fridge", 200, BODEN, 190, "lars", fuell=WEISS),
    *fl("IN", IX3, [("lars", "ruhig_r")], bis="in2", erst="pop"),
    *redet("IN_redet_r", IX3, BODEN, FH, "in2", "la1"),
    *fl("IN", IX3, [("la1", "sorge_r"), ("frage", "denkt_r")]),
    ns("Insa", IX3, BODEN, "lars", NFARBE["IN"]),
    *fl("LA", LX3, [("lars", "ruhig")], bis="la1", erst="pop", d=0.1),
    *redet("LA_redet", LX3, BODEN, FH, "la1", "frage"),
    *fl("LA", LX3, [("frage", "denkt")]),
    ns("Lars", LX3, BODEN, "lars", NFARBE["LA"], d=0.1),
    blase("sprech", 700, 220, "in2", 1000, 250, inhalt=["Du schuldest mir die Hälfte,", "450 Euro."], textsize=36,
          figur=("IN_redet_r", IX3, BODEN, FH), bis="la1"),
    blase("sprech", 700, 220, "la1", 1150, 250, inhalt=["Wir waren drei. Ich zahle", "dir 300, mehr nicht."], textsize=36,
          figur=("LA_redet", LX3, BODEN, FH), bis="frage"),
    ficon("fluent-emoji-flat", "euro-banknote", 1680, BODEN, 130, "la1"),
    pl("Durfte der Versorger alles von Insa verlangen?", 960, 40, "frage", fill=PINK, size=42, anker="m"),
    pl("Und wie viel muss Lars ihr erstatten?", 960, 130, "frage2", fill=PINK, size=38, anker="m"),
])


# B Sachverhalt -------------------------------------------------------------------------------------------------------------------
def sachverhalt_120(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=36, zeilenabstand=1.32)
        els += e; y += 22
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=38))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_120("sv", [
    "Insa, Lars und Rieke wohnen zusammen in einer Wohngemeinschaft. Den Stromliefervertrag mit dem Versorger haben alle "
    "drei unterschrieben. Im Frühjahr zieht Rieke aus; sie ist inzwischen zahlungsunfähig.",
    "Die Jahresabrechnung ergibt eine Nachzahlung von 900 Euro. Der Versorger verlangt den ganzen Betrag von Insa, und "
    "Insa zahlt die 900 Euro.",
    "Danach verlangt Insa von Lars 450 Euro. Lars meint: „Wir waren drei. Ich zahle dir 300, mehr nicht.“",
], "Durfte der Versorger alles von Insa verlangen, und wie viel muss Lars erstatten?")

# C Zwei Ebenen ---------------------------------------------------------------------------------------------------------------------
folie([("eben", "Gesamtschuld · Zwei Ebenen"), ("aussen", "Gesamtschuld › I. Außenverhältnis"),
       ("innen", "Gesamtschuld › II. Innenverhältnis")], rechts_frei([
    *tafel("eben", "Gesamtschuld: zwei Ebenen"),
    blk(400, 185, 460, 95, GRUEN, "eben", [("Versorger (Gläubiger)", "ExtraBold", 34, INK)]),
    blk(130, 480, 280, 90, ROT, "eben", [("Insa", "ExtraBold", 36, INK)], anim="pop"),
    blk(490, 480, 280, 90, BLAU, "eben", [("Lars", "ExtraBold", 36, INK)], anim="pop"),
    blk(850, 480, 280, 90, LILA, "eben", [("Rieke", "ExtraBold", 36, INK)], anim="pop"),
    pfeil(560, 290, 280, 470, beim("aussen", "Gläubiger"), breite=8, kopf=26),
    pfeil(630, 290, 630, 470, beim("aussen", "Gläubiger"), breite=8, kopf=26),
    pfeil(700, 290, 980, 470, beim("aussen", "Gläubiger"), breite=8, kopf=26),
    z("I. Außenverhältnis: Gläubiger – Schuldner", 110, 700, "aussen", "Bold", 36),
    pfeil(630, 630, 290, 630, "innen", breite=8, kopf=26, farbe=DROT),
    pfeil(630, 630, 970, 630, "innen", breite=8, kopf=26, farbe=DROT),
    z("II. Innenverhältnis: Ausgleich untereinander", 110, 770, beim("innen", "Ausgleich"), "Bold", 36, farbe=DROT),
    *requisit([("eben", ("tabler", "hierarchy-2", 110, WEISS), "2 Ebenen", WEISS),
               ("aussen", ("fluent-emoji-flat", "high-voltage", 100, None), "Außenverhältnis", GRUEN),
               ("innen", ("tabler", "arrows-right-left", 110, WEISS), "Innenverhältnis", ROT)]),
    *paar("eben", "IN", [("eben", "ruhig"), ("innen", "denkt")], "LA", [("eben", "ruhig"), ("aussen", "denkt")]),
]))

# D1 I. 1. Entstehen der Gesamtschuld: § 421 S. 1 (Wortlaut) --------------------------------------------------------------------
W421 = ["„Schulden mehrere eine Leistung in der Weise, dass jeder die",
        "ganze Leistung zu bewirken verpflichtet, der Gläubiger aber die",
        "Leistung nur einmal zu fordern berechtigt ist (Gesamtschuldner),",
        "so kann der Gläubiger die Leistung nach seinem Belieben von jedem",
        "der Schuldner ganz oder zu einem Teil fordern. …“"]
w421, w421_y = wortlaut(80, 175, 1100, W421, "§ 421 Satz 1 BGB", "w421", marken=[
    (0, "Schulden mehrere eine Leistung", "m1"),
    (1, "ganze Leistung zu bewirken verpflichtet", "m2"),
    (2, "nur einmal zu fordern berechtigt", "m3"),
    (3, "nach seinem Belieben", "m4")], size=32)
folie([("w421", "I. Außenverhältnis › 1. Entstehen, § 421 BGB")], rechts_frei([
    *tafel("w421", "I. 1. Entstehen der Gesamtschuld"),
    *w421,
    z("mehrere schulden eine Leistung", 110, w421_y + 35, beim("m1", "Leistung"), "Bold", 36),
    z("jeder muss ganz leisten – Gläubiger fordert nur einmal", 110, w421_y + 95, beim("m3", "einmal"), "Bold", 34),
    z("Gläubiger wählt: von jedem ganz oder zum Teil", 110, w421_y + 155, beim("m4", "wählen"), "Bold", 34),
    *requisit([("w421", ("tabler", "users", 110, WEISS), "mehrere Schuldner", WEISS),
               ("m2", ("fluent-emoji-flat", "euro-banknote", 110, None), "jeder ganz", GELB),
               ("m3", ("tabler", "circle-check", 100, GRUEN), "nur einmal", GRUEN),
               ("m4", ("tabler", "hand-finger", 100, WEISS), "Gläubiger wählt", WEISS)]),
    *paar("w421", "IN", [("w421", "ruhig"), ("m4", "sorge")], "LA", [("w421", "ruhig"), ("m3", "denkt")]),
]))

# D2 Entstehungsgründe, Gleichstufigkeit ------------------------------------------------------------------------------------------
folie([("p427", "I. 1. Entstehen › gemeinsamer Vertrag, § 427 BGB"), ("p840", "I. 1. Entstehen › Gesetz, § 840 Abs. 1 BGB"),
       ("gleich", "I. 1. Entstehen › Gleichstufigkeit")], rechts_frei([
    *tafel("p427", "I. 1. Wie entsteht eine Gesamtschuld?"),
    z("Vertrag: gemeinschaftlich zu teilbarer Leistung,", 110, 190, beim("p427", "Verpflichten"), "Bold", 36),
    z("§ 427 BGB: im Zweifel Gesamtschuldner", 160, 245, beim("p427", "Zweifel"), size=36),
    z("Gesetz: z. B. § 840 Abs. 1 BGB,", 110, 345, beim("p840", "Gesetz"), "Bold", 36),
    z("mehrere verantwortlich für einen Schaden", 160, 400, beim("p840", "mehrere"), size=36),
    z("aus unerlaubter Handlung", 160, 455, beim("p840", "unerlaubter"), size=36),
    z("Gleichstufigkeit der Pflichten:", 110, 555, "gleich", "Bold", 36),
    z("keiner haftet nur nachrangig oder vorläufig", 160, 610, beim("gleich", "Keiner"), size=36),
    zit("BGH, Urt. v. 22.12.2011 – VII ZR 7/11, Rn. 18", 160, 668, beim("gleich", "Keiner")),
    *requisit([("p427", ("tabler", "file-text", 100, WEISS), "Vertrag", WEISS),
               ("p840", ("tabler", "scale", 110, WEISS), "Gesetz", WEISS),
               ("gleich", ("tabler", "equal", 100, GELB), "gleichstufig", GELB)]),
    *paar("p427", "IN", [("p427", "ruhig"), ("gleich", "denkt")], "LA", [("p427", "ruhig"), ("p840", "denkt")]),
]))

# D3 Im Fall: Gesamtschuld (+) ---------------------------------------------------------------------------------------------------
folie([("sub1", "I. 1. Entstehen › im Fall"), ("sub2", "I. 1. Entstehen › Gesamtschuld (+)")], rechts_frei([
    *tafel("sub1", "Im Fall: Gesamtschuld?"),
    karte(110, 185, 560, 220, "sub1", fill=WEISS, rund=10, schatten=6, rand=4),
    z("Stromvertrag", 140, 200, "sub1", "Bold", 36, rechts=650),
    z("Insa   Lars   Rieke", 140, 265, "sub1", "ExtraBold", 36, rechts=650),
    z("Nachzahlung: 900 €", 140, 330, "sub1", size=34, rechts=650),
    *okz("alle 3 haben unterschrieben: Vertrag", 470, beim("sub1", "unterschrieben"), "Bold", 36, x=160),
    *okz("Geldzahlung ist teilbar, § 427 BGB", 540, beim("sub1", "teilbar"), "Bold", 36, x=160),
    blk(110, 630, 1040, 160, GRUEN, "sub2", [("Gesamtschuldner: Der Versorger durfte", "ExtraBold", 38, INK),
                                            ("die ganzen 900 € von Insa verlangen", "ExtraBold", 38, INK)]),
    *requisit([("sub1", ("tabler", "signature", 110, WEISS), "3 Unterschriften", WEISS),
               ("sub2", ("fluent-emoji-flat", "high-voltage", 100, None), "900 € von Insa", GRUEN)]),
    *paar("sub1", "IN", [("sub1", "ruhig"), ("sub2", "sorge")], "LA", [("sub1", "ruhig"), ("sub2", "froh")]),
]))

# E I. 2. Wirkung der Erfüllung, § 422 Abs. 1, § 425 ---------------------------------------------------------------------------------
folie([("p422", "I. Außenverhältnis › 2. Erfüllung, § 422 Abs. 1 BGB"),
       ("p425", "I. 2. Erfüllung › andere Tatsachen, § 425 BGB")], rechts_frei([
    *tafel("p422", "I. 2. Wirkung der Erfüllung"),
    z("§ 422 Abs. 1 BGB: Erfüllung durch einen", 110, 190, beim("p422", "Nach"), "Bold", 36),
    z("Gesamtschuldner wirkt auch für die übrigen", 160, 245, beim("p422", "wirkt"), size=36),
    blk(110, 330, 1040, 110, GRUEN, "frei", [("Lars und Rieke sind frei", "ExtraBold", 38, INK)]),
    z("gegenüber dem Versorger", 160, 455, beim("frei", "gegenüber"), size=36),
    z("§ 425 BGB: andere Tatsachen, z. B. Verzug,", 110, 560, "p425", "Bold", 36),
    z("Verjährung: wirken grundsätzlich nur für den,", 160, 615, beim("p425", "grundsätzlich"), size=36),
    z("bei dem sie eintreten", 160, 670, beim("p425", "eintreten"), size=36),
    *requisit([("p422", ("fluent-emoji-flat", "euro-banknote", 110, None), "Erfüllung", GRUEN),
               ("frei", ("tabler", "user-check", 100, GRUEN), "alle frei", GRUEN),
               (beim("p425", "nur"), ("tabler", "user", 100, WEISS), "nur für den einen", WEISS)]),
    *paar("p422", "IN", [("p422", "ruhig"), ("p425", "denkt")], "LA", [("p422", "ruhig"), ("frei", "froh"), ("p425", "ruhig")]),
]))

# F II. 1. Ausgleich, § 426 Abs. 1 S. 1 (Wortlaut) -----------------------------------------------------------------------------------
W4261 = ["„Die Gesamtschuldner sind im Verhältnis zueinander zu gleichen",
         "Anteilen verpflichtet, soweit nicht ein anderes bestimmt ist. …“"]
w4261, w4261_y = wortlaut(80, 175, 1100, W4261, "§ 426 Abs. 1 Satz 1 BGB", "w426", marken=[
    (0, "zu gleichen", beim("w426", "gleichen")),
    (1, "Anteilen", beim("w426", "Anteilen")),
    (1, "soweit nicht ein anderes bestimmt ist", beim("w426", "soweit"))], size=32)
folie([("w426", "II. Innenverhältnis › 1. Ausgleich, § 426 Abs. 1 S. 1 BGB"),
       ("abrede", "II. 1. Ausgleich › anderweitige Bestimmung")], rechts_frei([
    *tafel("w426", "II. 1. Ausgleichsanspruch"),
    *w4261,
    z("900 € : 3 Mitbewohner", 110, w4261_y + 40, "anteil", "Bold", 38),
    blk(110, w4261_y + 110, 320, 90, ROT, beim("anteil", "dreihundert"), [("Insa: 300 €", "ExtraBold", 36, INK)], anim="pop"),
    blk(470, w4261_y + 110, 320, 90, BLAU, beim("anteil", "dreihundert"), [("Lars: 300 €", "ExtraBold", 36, INK)], anim="pop", d=0.15),
    blk(830, w4261_y + 110, 320, 90, LILA, beim("anteil", "dreihundert"), [("Rieke: 300 €", "ExtraBold", 36, INK)], anim="pop", d=0.3),
    z("Variante: andere Vereinbarung in der WG,", 110, w4261_y + 250, "abrede", "Bold", 36),
    z("z. B. Verteilung nach Zimmergröße", 160, w4261_y + 305, beim("abrede", "Verteilung"), size=36),
    zit("BGH, Urt. v. 3.2.2010 – XII ZR 53/08, Rn. 9", 160, w4261_y + 362, beim("abrede", "Verteilung")),
    *requisit([("w426", ("tabler", "arrows-right-left", 110, WEISS), "Innenverhältnis", WEISS),
               (beim("w426", "Ausgleichsanspruch"), ("tabler", "coins", 100, GELB), "Ausgleichsanspruch", GELB),
               (beim("w426", "zueinander"), ("tabler", "users", 110, WEISS), "zueinander", WEISS),
               ("anteil", ("tabler", "chart-pie", 100, GELB), "je 300 €", GELB),
               ("abrede", ("tabler", "home", 100, WEISS), "andere Vereinbarung?", WEISS)]),
    *paar("w426", "IN", [("w426", "ruhig"), ("anteil", "denkt"), ("abrede", "ruhig")], "LA", [("w426", "ruhig"), ("anteil", "froh")]),
]))

# G II. 2. Ausfall, § 426 Abs. 1 S. 2 (Wortlaut) -----------------------------------------------------------------------------------
W4262 = ["„Kann von einem Gesamtschuldner der auf ihn entfallende Beitrag",
         "nicht erlangt werden, so ist der Ausfall von den übrigen zur",
         "Ausgleichung verpflichteten Schuldnern zu tragen.“"]
w4262, w4262_y = wortlaut(80, 175, 1100, W4262, "§ 426 Abs. 1 Satz 2 BGB", "w426s2", marken=[
    (1, "nicht erlangt werden", beim("w426s2", "erlangt")),
    (1, "Ausfall von den übrigen", beim("w426s2", "Ausfall"))], size=32)
folie([("w426s2", "II. Innenverhältnis › 2. Ausfall, § 426 Abs. 1 S. 2 BGB")], rechts_frei([
    *tafel("w426s2", "II. 2. Ausfallhaftung"),
    *w4262,
    *neinz("Rieke zahlungsunfähig: 300 € nicht zu erlangen", w4262_y + 45, "ausfall", "Bold", 34, x=160),
    z("ihre 300 € tragen Insa und Lars je zur Hälfte:", 110, w4262_y + 130, "halb", "Bold", 36),
    blk(110, w4262_y + 200, 500, 90, ROT, beim("halb", "hundertfünfzig"), [("Insa: + 150 €", "ExtraBold", 36, INK)], anim="pop"),
    blk(650, w4262_y + 200, 500, 90, BLAU, beim("halb", "hundertfünfzig"), [("Lars: + 150 €", "ExtraBold", 36, INK)], anim="pop", d=0.15),
    *requisit([("w426s2", ("tabler", "user-x", 100, WEISS), "Ausfall", WEISS),
               ("ausfall", ("fluent-emoji-flat", "package", 110, None), "Rieke: zahlungsunfähig", ROT),
               ("halb", ("tabler", "chart-pie", 100, GELB), "je 150 €", GELB)]),
    *paar("w426s2", "IN", [("w426s2", "ruhig"), ("halb", "sorge")], "LA", [("w426s2", "ruhig"), ("ausfall", "sorge"), ("halb", "denkt")]),
]))

# H II. 3. Legalzession, § 426 Abs. 2 S. 1 (Wortlaut), §§ 412, 401 -------------------------------------------------------------------
W4262b = ["„Soweit ein Gesamtschuldner den Gläubiger befriedigt und von den",
          "übrigen Schuldnern Ausgleichung verlangen kann, geht die Forderung",
          "des Gläubigers gegen die übrigen Schuldner auf ihn über. …“"]
w426b, w426b_y = wortlaut(80, 175, 1100, W4262b, "§ 426 Abs. 2 Satz 1 BGB", "w426b", marken=[
    (0, "den Gläubiger befriedigt", beim("w426b", "befriedigt")),
    (1, "geht die Forderung", beim("w426b", "geht")),
    (2, "auf ihn über", beim("w426b", "über"))], size=32)
folie([("w426b", "II. Innenverhältnis › 3. Legalzession, § 426 Abs. 2 BGB"),
       ("sich", "II. 3. Legalzession › Sicherheiten, §§ 412, 401 BGB")], rechts_frei([
    *tafel("w426b", "II. 3. Legalzession"),
    *w426b,
    blk(110, w426b_y + 40, 400, 90, GRUEN, "ueber", [("Versorger gegen Lars", "ExtraBold", 32, INK)], anim="pop"),
    pfeil(530, w426b_y + 85, 760, w426b_y + 85, beim("ueber", "Insa"), breite=10, kopf=30),
    blk(780, w426b_y + 40, 370, 90, ROT, beim("ueber", "Insa"), [("Insa gegen Lars", "ExtraBold", 32, INK)], anim="pop"),
    z("kraft Gesetzes, soweit Insa Ausgleich verlangen kann", 110, w426b_y + 155, beim("ueber", "soweit"), size=32),
    z("§§ 412, 401 BGB: Sicherheiten wie eine", 110, w426b_y + 240, "sich", "Bold", 36),
    z("Bürgschaft gehen mit – wie bei der Abtretung", 160, w426b_y + 295, beim("sich", "Bürgschaft"), size=36),
    *requisit([("w426b", ("tabler", "transfer", 110, WEISS), "Forderung geht über", WEISS),
               ("ueber", ("tabler", "file-text", 100, WEISS), "kraft Gesetzes", GELB),
               ("sich", ("tabler", "shield", 100, GRUEN), "Sicherheiten", GRUEN)]),
    *paar("w426b", "IN", [("w426b", "ruhig"), ("ueber", "froh"), ("sich", "ruhig")], "LA", [("w426b", "ruhig"), ("ueber", "sorge")]),
]))

# I Verhältnis von Abs. 1 und Abs. 2 ---------------------------------------------------------------------------------------------
folie([("neben", "II. Innenverhältnis › Verhältnis von Abs. 1 und Abs. 2")], rechts_frei([
    *tafel("neben", "2 Anspruchsgrundlagen"),
    blk(110, 200, 500, 200, ROT, beim("neben", "Absatz", nr=1), [("§ 426 Abs. 1:", "ExtraBold", 36, INK),
                                                              ("eigener", "Bold", 34, INK), ("Ausgleichsanspruch", "Bold", 34, INK)]),
    blk(650, 200, 500, 200, GRUEN, beim("neben", "Absatz", nr=2), [("§ 426 Abs. 2:", "ExtraBold", 36, INK),
                                                                ("übergegangene", "Bold", 34, INK), ("Forderung", "Bold", 34, INK)]),
    z("selbständig nebeneinander", 110, 470, beim("neben2", "selbständig"), "ExtraBold", 42),
    zit("BGH, Urt. v. 17.3.2022 – IX ZR 216/20, Rn. 19", 110, 545, beim("neben2", "selbständig")),
    zit("BGH, Versäumnisurt. v. 20.3.2012 – XI ZR 234/11, Rn. 20", 110, 590, beim("neben2", "selbständig")),
    *requisit([("neben", ("tabler", "arrows-split-2", 110, WEISS), "2 Anspruchsgrundlagen", WEISS),
               ("neben2", ("tabler", "equal", 100, GELB), "nebeneinander", GELB)]),
    *paar("neben", "IN", [("neben", "denkt"), ("neben2", "froh")], "LA", [("neben", "ruhig")]),
]))

# J Rechnung ----------------------------------------------------------------------------------------------------------------------
folie([("rech", "Rechnung · Wer zahlt wem wie viel?"), ("r4", "Rechnung · Lars schuldet 450 €")], rechts_frei([
    *tafel("rech", "Die Rechnung"),
    z("Insa hat gezahlt:", 110, 200, beim("r1", "Insa"), "Bold", 38),
    z("900 €", 800, 200, beim("r1", "neunhundert"), "ExtraBold", 38, farbe=DROT),
    z("eigener Anteil von Insa:", 110, 265, beim("r1", "Anteil"), size=38),
    z("300 €", 800, 265, beim("r1", "dreihundert"), "ExtraBold", 38),
    z("Lars: eigener Anteil", 110, 365, beim("r2", "Anteil"), "Bold", 38),
    z("300 €", 800, 365, beim("r2", "dreihundert"), "ExtraBold", 38),
    z("+ Hälfte des Ausfalls von Rieke", 110, 430, "r3", size=38),
    z("150 €", 800, 430, beim("r3", "hundertfünfzig"), "ExtraBold", 38),
    linienzug([(110, 505), (1000, 505)], "r4", breite=5),
    blk(110, 530, 1040, 100, GRUEN, "r4", [("Lars an Insa: 450 €", "ExtraBold", 42, INK)]),
    z("Insa trägt am Ende selbst: 450 €", 110, 680, "r5", "Bold", 38),
    *requisit([("rech", ("tabler", "calculator", 100, WEISS), "Rechnung", WEISS),
               ("r2", ("fluent-emoji-flat", "euro-banknote", 110, None), "Anteil Lars", BLAU),
               ("r4", ("fluent-emoji-flat", "money-bag", 100, None), "450 € an Insa", GRUEN)]),
    *paar("rech", "IN", [("rech", "ruhig"), ("r4", "froh")], "LA", [("rech", "ruhig"), ("r3", "sorge"), ("r5", "denkt")]),
]))

# K Ergebnis (Bühne) --------------------------------------------------------------------------------------------------------------------
IX9, LX9 = 760, 1300
folie([("erg", "Ergebnis · Lars schuldet Insa 450 €")], [
    blk(80, 40, 1760, 95, GRUEN, "erg", [("Ergebnis: Der Versorger durfte die vollen 900 € von Insa verlangen", "ExtraBold", 38, INK)]),
    z("Lars muss Insa 450 € erstatten: § 426 Abs. 1 und Abs. 2 BGB", 110, 160, beim("erg2", "Lars"), "Bold", 36, rechts=1820),
    boden("erg"),
    ficon("tabler", "fridge", 200, BODEN, 190, "erg", fuell=WEISS),
    *fl("IN", IX9, [("erg", "ruhig_r"), ("erg2", "froh_r")], erst="pop"),
    ns("Insa", IX9, BODEN, "erg", NFARBE["IN"]),
    *fl("LA", LX9, [("erg", "denkt"), ("erg3", "sorge")], bis="la2", erst="pop", d=0.1),
    *redet("LA_redet", LX9, BODEN, FH, "la2", "tipp"),
    ns("Lars", LX9, BODEN, "erg", NFARBE["LA"], d=0.1),
    pl("§ 426 Abs. 1: Ausgleichsanspruch", 110, 225, beim("erg2", "Paragraf"), fill=ROT, size=28),
    pl("§ 426 Abs. 2: übergegangene Forderung", 110, 295, beim("erg2", "übergegangenen"), fill=GRUEN, size=28),
    *neinz("mit 300 € nicht getan", 260, "erg3", "Bold", 36, x=1450, rechts=1880),
    blase("sprech", 560, 170, "la2", 990, 300, inhalt=["Na gut, dann 450."], textsize=36,
          figur=("LA_redet", LX9, BODEN, FH), bis="tipp"),
    ficon("fluent-emoji-flat", "euro-banknote", 1030, 640, 130, beim("la2", "vierhundertfünfzig")),
])

# L Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · Regress auf beiden Wegen")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("1. Regress immer auf beiden Wegen prüfen", 200, 200, beim("tipp", "Prüfe"), "Bold", 36),
    z("2. Abs. 2: Sicherheiten gehen mit, aber auch", 200, 290, "tipp2", "Bold", 36),
    z("Einwendungen, §§ 412, 404 BGB", 250, 345, beim("tipp2", "Einwendungen"), size=36),
    z("3. Verjährung und Einreden getrennt", 200, 430, "tipp3", "Bold", 36),
    zit("BGH, Urt. v. 17.3.2022 – IX ZR 216/20, Rn. 19", 250, 485, beim("tipp3", "getrennt")),
    z("4. Ausgleichsanspruch entsteht mit der", 200, 560, "tipp4", "Bold", 36),
    z("Gesamtschuld: vor der Zahlung Mitwirkung, Befreiung,", 250, 615, beim("tipp4", "Mitwirkung"), size=36),
    z("danach: auf Zahlung gerichtet", 250, 670, beim("tipp4", "danach"), size=36),
    zit("BGH, Urt. v. 8.11.2016 – VI ZR 200/15, Rn. 11", 250, 725, beim("tipp4", "danach")),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# M Klausurschema ---------------------------------------------------------------------------------------------------------------------
K1, K2 = 150, 230
folie([("sch", "Klausurschema"), ("k1", "Klausurschema › I. Außenverhältnis"), ("k2", "Klausurschema › II. Innenverhältnis")], [
    karte(60, 50, 1800, 900, "sch"),
    titel(glyphen("Klausurschema: Gesamtschuld, §§ 421 ff. BGB"), 110, 90, "sch", 46),
    z("I. Außenverhältnis", K1, 200, "k1", "Bold", 40, rechts=1820),
    z("1. Entstehen der Gesamtschuld, § 421 BGB: Vertrag (§ 427) oder Gesetz (z. B. § 840 Abs. 1)", K2, 262, "k1a",
      size=34, rechts=1820),
    z("2. Wirkung der Erfüllung, § 422 Abs. 1 BGB", K2, 320, "k1b", size=34, rechts=1820),
    z("II. Innenverhältnis", K1, 410, "k2", "Bold", 40, rechts=1820),
    z("1. Ausgleich nach § 426 Abs. 1 S. 1 BGB: gleiche Anteile, soweit nichts anderes bestimmt", K2, 472, "k2a",
      size=34, rechts=1820),
    z("2. Ausfall nach § 426 Abs. 1 S. 2 BGB", K2, 530, "k2b", size=34, rechts=1820),
    z("3. Legalzession nach § 426 Abs. 2 BGB (mit §§ 412, 401 BGB)", K2, 588, "k2c", size=34, rechts=1820),
])

# N Merksatz (Lexi) ---------------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Außen haftet jeder auf das ", 0), ("Ganze", "a"), (",", 0)], [("innen nur auf seinen ", 0), ("Anteil", "b"), (".", 0)]],
                750, 300, 42, "merke", {"a": beim("merke", "Ganze"), "b": beim("merke", "Anteil")}),
    *markertext([[("Fällt einer aus, teilen die übrigen", 0)], [("seinen Anteil.", 0)]], 750, 450, 42, "mk2",
                {}),
    *markertext([[("Und wer zahlt, hat ", 0), ("zwei Wege", "c"), (" zum Regress:", 0)],
                 [("Absatz 1 und die übergegangene", 0)], [("Forderung aus Absatz 2.", 0)]],
                750, 600, 42, "mk3", {"c": beim("mk3", "zwei")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
