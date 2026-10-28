"""Folge 089 · Abtretung § 398 BGB: Voraussetzungen und Schuldnerschutz – Serienstandard Open Peeps (Katzenkönig).
Beispielfall: Malermeister Ewald hat das Wohnzimmer von Tanja gestrichen (Werklohn 2.400 €, abgenommen), verkauft die
Forderung an ein Inkassobüro (Sachbearbeiter Sven) und tritt sie ab; Tanja weiß nichts und überweist an Ewald.
Szenen laut ../SZENENPLAN.md: A1 Auftrag (Wohnzimmer), A2 Verkauf der Rechnung (Inkassobüro), A3 Zahlung (Wohnzimmer,
Smartphone), A4 Anruf des Inkassobüros und Frage, B Sachverhalt, C § 398 (Wortlaut), D1–D4 Voraussetzungen, D5 Abstraktion,
E Rechtsfolge, F Schuldnerschutz §§ 404, 406, G1 § 407 Abs. 1 (Wortlaut), G2 Subsumtion, H §§ 409, 410, I Ergebnis (Bühne,
§ 816 Abs. 2), J Klausurtipp (Lexi), K Klausurschema, L Merksatz (Lexi).
Zwei Handlungsgeräusche (Tippen beim Überweisen, Vibration beim Anruf; ../geraeusche_herkunft.json).
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/hand als
eigene Kopie aus Folge 086 (gemeinsame Dateien unverändert). Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_089/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_089/" in n:
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 027/073/083) ------------------------------------
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


def hand(name, cx, unten, hoehe, seite):
    """Äußerster Punkt der Figur (Hand) im Band 40–62 % der Höhe; seite = -1 links, +1 rechts."""
    e = peep_voll(name, cx, unten, hoehe, "_")
    a = np.asarray(e.sprite)[:, :, 3] > 40
    h = a.shape[0]
    band = a[int(h * 0.40):int(h * 0.62)]
    ys, xs = np.nonzero(band)
    i = xs.argmin() if seite < 0 else xs.argmax()
    return int(e.x + xs[i]), int(e.y + int(h * 0.40) + ys[i])


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
NAME = {"EW": "Ewald", "TA": "Tanja", "SV": "Sven"}
NFARBE = {"EW": BLAU, "TA": GRUEN, "SV": LILA}
WAND = (214, 238, 214, 255)


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
    """Tafelszene: zwei Figuren rechts der Tafel, beide blicken zur Tafel (nach links); l, r = Kürzel EW/TA/SV."""
    return [*fig(l, X1, FB, FR, lf), ns(NAME[l], X1, FB, c0, NFARBE[l], d=0.1),
            *fig(r, X2, FB, FR, rf, d=0.2), ns(NAME[r], X2, FB, c0, NFARBE[r], d=0.3)]



def fl(name, cx, folge, bis=None, erst="cut", unten=BODEN, hoehe=FH, d=0.0):
    """Figur auf der Bühne: folge = [(cue, ansicht)] mit Ansichtsnamen ohne Präfix (z. B. 'ruhig_r')."""
    return fig(name, cx, unten, hoehe, folge, bis=bis, erst=erst, d=d)


def plus(cue, sek):
    c, o = cue if isinstance(cue, tuple) else (cue, 0.0)
    return (c, round(o + sek, 3))


# A1 Fall: der Auftrag (Wohnzimmer von Tanja) --------------------------------------------------------------------------------
EX, TX = 1180, 1620
ABG = beim("rech", "abgenommen")
folie([(NULL, "Fall · Der Auftrag")], [
    hart(pl("Ewald hat das Wohnzimmer gestrichen", 70, 30, NULL, fill=GELB, size=44)),
    hart(boden(NULL)),
    hart(karte(100, 140, 900, 560, NULL, fill=WAND, rund=10, schatten=0, rand=4)),
    pl("frisch gestrichen", 550, 380, beim("fall", "gestrichen"), fill=WEISS, size=34, anker="m"),
    hart(ficon("ph", "ladder", 250, BODEN, 210, NULL, fuell=WEISS)),
    hart(ficon("tabler", "sofa", 620, BODEN, 330, NULL, fuell=LILA)),
    hart(ficon("ph", "paint-bucket", 905, BODEN, 120, NULL, fuell=GRUEN)),
    hart(ficon("ph", "paint-roller", 900, 720, 130, NULL, fuell=GRUEN)),
    *fl("EW", EX, [(NULL, "ruhig_r"), (ABG, "froh_r")]),
    hart(ns("Ewald", EX, BODEN, NULL, NFARBE["EW"])),
    *fl("TA", TX, [(NULL, "ruhig"), (ABG, "froh")]),
    hart(ns("Tanja", TX, BODEN, NULL, NFARBE["TA"])),
    pl("Arbeit abgenommen", 1400, 100, ABG, fill=GRUEN, size=32, anker="m"),
    pl("Rechnung: 2.400 €", 1400, 175, beim("rech", "Rechnung"), fill=WEISS, size=32, anker="m"),
    ficon("tabler", "receipt-euro", 1400, 345, 90, beim("rech", "zweitausendvierhundert"), fuell=GELB),
])

# A2 Fall: Ewald verkauft die Rechnung (Inkassobüro) ---------------------------------------------------------------------------
EX2, SX2 = 600, 1330
TISCH = ficon("tabler", "desk", 965, BODEN, 300, "_", fuell=GELB)
TY = int(TISCH.y + 0.12 * TISCH.sprite.height)
AB = beim("hu1", "ab", nr=1)
folie([("verk", "Fall · Ewald verkauft die Rechnung")], [
    pl("Ewald verkauft die Rechnung", 70, 30, "verk", fill=GELB, size=44),
    boden("verk"),
    ficon("tabler", "desk", 965, BODEN, 300, "verk", fuell=GELB),
    ficon("ph", "building-office", 1740, 300, 150, beim("verk", "Inkassobüro"), fuell=BLAU),
    pl("Inkassobüro", 1740, 315, beim("verk", "Inkassobüro"), fill=BLAU, size=30, anker="m"),
    *fl("EW", EX2, [("verk", "ruhig_r")], bis="hu1", erst="pop"),
    ns("Ewald", EX2, BODEN, "verk", NFARBE["EW"], d=0.1),
    *redet("EW_redet_r", EX2, BODEN, FH, "hu1", "sn1"),
    *fl("EW", EX2, [("sn1", "froh_r")]),
    ficon("tabler", "receipt-euro", 800, 470, 80, beim("verk", "offene"), fuell=GELB, bis=AB),
    bewegt(ficon("tabler", "receipt-euro", 1140, 470, 80, AB, fuell=GELB, anim="cut"), AB, plus(AB, 0.9), 800 - 1140, 0),
    *fl("SV", SX2, [("sven", "ruhig")], bis="sn1", erst="pop"),
    ns("Sven", SX2, BODEN, "sven", NFARBE["SV"], d=0.1),
    *redet("SV_redet", SX2, BODEN, FH, "sn1", "nichts"),
    blase("sprech", 720, 200, "hu1", 640, 210, inhalt=["Die Forderung gegen Tanja", "über 2.400 € trete ich Ihnen ab."],
          textsize=34, figur=("EW_redet_r", EX2, BODEN, FH), bis="sn1"),
    blase("sprech", 640, 190, "sn1", 1260, 210, inhalt=["Einverstanden. Ab jetzt", "zahlt sie an uns."], textsize=34,
          figur=("SV_redet", SX2, BODEN, FH), bis="nichts"),
    pl("Abtretungsvertrag", 965, 525, beim("sn1", "Einverstanden"), fill=WEISS, size=30, anker="m"),
    ficon("ph", "handshake", 965, TY + 2, 120, beim("sn1", "Einverstanden"), fuell=GELB),
])

# A3 Fall: Tanja zahlt an Ewald -------------------------------------------------------------------------------------------------
TX3 = 560
HX, HY = hand("TA_ruhig_r", TX3, BODEN, FH, +1)
UEB = beim("zahlt", "überweist")
ANE = beim("zahlt", "Ewald")
BETRAG = beim("zahlt", "zweitausendvierhundert")
folie([("nichts", "Fall · Tanja zahlt an Ewald")], [
    pl("Tanja weiß nichts von der Abtretung", 70, 30, "nichts", fill=GELB, size=44),
    boden("nichts"),
    ficon("tabler", "sofa", 1000, BODEN, 330, "nichts", fuell=LILA),
    ficon("tabler", "lamp", 1780, BODEN, 150, "nichts", fuell=GELB),
    ficon("ph", "potted-plant", 200, BODEN, 130, "nichts", fuell=GRUEN),
    *fl("TA", TX3, [("nichts", "denkt_r"), (UEB, "ruhig_r"), (ANE, "froh_r")], erst="pop"),
    ns("Tanja", TX3, BODEN, "nichts", NFARBE["TA"], d=0.1),
    pl("1 Woche später", 70, 115, "zahlt", fill=WEISS, size=34),
    ficon("tabler", "device-mobile", HX + 20, HY + 40, 60, UEB, fuell=WEISS),
    szene(karte(800, 260, 460, 190, UEB, fill=WEISS, rund=18, schatten=6, rand=4), "089tippen*", 0.8, 0.0),
    z("Überweisung", 830, 280, UEB, "Bold", 36, rechts=1240),
    z("2.400 € an Ewald", 830, 345, beim("zahlt", "zweitausendvierhundert"), size=36, rechts=1240),
    ficon("tabler", "building-bank", 1520, 560, 170, UEB, fuell=BLAU),
    pl("Konto von Ewald", 1520, 585, ANE, fill=BLAU, size=30, anker="m"),
    bewegt(ficon("tabler", "cash-banknote", 1520, 400, 110, BETRAG, fuell=GRUEN, anim="cut"), BETRAG, ANE,
           1030 - 1520, 120),
])

# A4 Fall: das Inkassobüro meldet sich, die Frage --------------------------------------------------------------------------------
TX4, SX4 = 470, 1450
HX4, HY4 = hand("TA_denkt_r", TX4, BODEN, FH, +1)
trenner = linienzug([(960, 140), (960, 840)], "meldet", breite=4, farbe=(21, 21, 21, 90))
folie([("meldet", "Fall · Das Inkassobüro meldet sich"), ("frage", "Fall · Die Frage")], [
    pl("Das Inkassobüro meldet sich", 70, 30, "meldet", fill=GELB, size=44, bis="frage"),
    boden("meldet"), trenner,
    ficon("ph", "building-office", 1760, 560, 140, "meldet", fuell=BLAU),
    pl("Inkassobüro", 1760, 575, "meldet", fill=BLAU, size=28, anker="m"),
    ficon("tabler", "device-mobile", HX4 + 20, HY4 + 40, 60, "meldet", fuell=WEISS),
    szene(ficon("tabler", "phone-call", 700, 600, 90, beim("meldet", "meldet"), fuell=GRUEN), "089vibration*", 0.9, 0.0),
    ficon("tabler", "phone-call", 1220, 600, 90, beim("meldet", "meldet"), fuell=LILA, spiegeln=True),
    *fl("TA", TX4, [("meldet", "denkt_r")], bis="ta1", erst="pop"),
    *redet("TA_redet_r", TX4, BODEN, FH, "ta1", "frage"),
    *fl("TA", TX4, [("frage", "sorge_r")]),
    ns("Tanja", TX4, BODEN, "meldet", NFARBE["TA"], d=0.1),
    *fl("SV", SX4, [("meldet", "ruhig")], bis="sn2", erst="pop"),
    *redet("SV_redet", SX4, BODEN, FH, "sn2", "ta1"),
    *fl("SV", SX4, [("ta1", "denkt"), ("frage", "ruhig")]),
    ns("Sven", SX4, BODEN, "meldet", NFARBE["SV"], d=0.1),
    blase("sprech", 640, 190, "sn2", 1380, 220, inhalt=["Bitte zahlen Sie die", "2.400 € jetzt an uns."], textsize=34,
          figur=("SV_redet", SX4, BODEN, FH), bis="ta1"),
    blase("sprech", 700, 190, "ta1", 560, 220, inhalt=["Aber ich habe doch schon", "an den Maler gezahlt!"], textsize=34,
          figur=("TA_redet_r", TX4, BODEN, FH), bis="frage"),
    pl("Muss Tanja noch einmal zahlen?", 960, 40, "frage", fill=PINK, size=42, anker="m"),
    pl("1. Ist die Forderung übergegangen?", 960, 135, beim("frage2", "Ist"), fill=WEISS, size=34, anker="m"),
    pl("2. Wie schützt das Gesetz Tanja?", 960, 215, beim("frage2", "Und"), fill=WEISS, size=34, anker="m"),
])


# B Sachverhalt -------------------------------------------------------------------------------------------------------------------
def sachverhalt_089(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=36, zeilenabstand=1.32)
        els += e; y += 22
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=38))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_089("sv", [
    "Malermeister Ewald hat das Wohnzimmer von Tanja gestrichen. Tanja hat die Arbeit abgenommen. Die Rechnung lautet auf "
    "2.400 Euro.",
    "Ewald verkauft die offene Forderung an ein Inkassobüro und tritt sie ab; Sven schließt den Vertrag für das Büro. Ein "
    "Abtretungsverbot haben Ewald und Tanja nicht vereinbart.",
    "Tanja erfährt davon nichts. Eine Woche später überweist sie die 2.400 Euro an Ewald. Danach verlangt das Inkassobüro "
    "von ihr Zahlung der 2.400 Euro.",
], "Muss Tanja noch einmal zahlen?")

# C § 398 BGB (Wortlaut) ------------------------------------------------------------------------------------------------------------
W398 = ["„Eine Forderung kann von dem Gläubiger durch Vertrag mit einem",
        "anderen auf diesen übertragen werden (Abtretung). Mit dem Abschluss",
        "des Vertrags tritt der neue Gläubiger an die Stelle des bisherigen",
        "Gläubigers.“"]
w398, w398_y = wortlaut(80, 175, 1100, W398, "§ 398 BGB", "w398", marken=[
    (0, "durch Vertrag", beim("w398", "Vertrag")), (1, "übertragen", beim("w398", "übertragen")),
    (2, "tritt der neue Gläubiger an die Stelle", beim("w398b", "tritt"))], size=32)
folie([("w398", "Abtretung › § 398 BGB"), ("rollen", "§ 398 BGB › Zedent und Zessionar")], rechts_frei([
    *tafel("w398", "§ 398 BGB: Abtretung"),
    *w398,
    z("Altgläubiger (Zedent): Ewald", 110, w398_y + 40, beim("rollen", "Altgläubiger"), "Bold", 36),
    z("Neugläubiger (Zessionar): Inkassobüro", 110, w398_y + 100, beim("rollen", "Neugläubiger"), "Bold", 36),
    z("Schuldnerin: Tanja", 110, w398_y + 160, beim("rollen", "Schuldnerin"), "Bold", 36),
    *requisit([("w398", ("tabler", "file-text", 100, WEISS), "Vertrag", WEISS),
               (beim("w398b", "neue"), ("tabler", "arrows-exchange", 110, WEISS), "neuer Gläubiger", GRUEN)]),
    *paar("w398", "EW", [("w398", "ruhig"), ("rollen", "denkt")], "SV", [("w398", "ruhig"), (beim("w398b", "neue"), "froh")]),
]))

# D1 I. Voraussetzungen: 1. Abtretungsvertrag -------------------------------------------------------------------------------------
folie([("vor", "Abtretung › I. Voraussetzungen"), ("v1", "I. Voraussetzungen › 1. Abtretungsvertrag")], rechts_frei([
    *tafel("vor", "I. Voraussetzungen der Abtretung"),
    z("1. Abtretungsvertrag", 110, 190, "v1", "Bold", 40),
    z("Einigung zwischen Alt- und Neugläubiger", 160, 255, beim("v1", "Einigung"), size=36),
    z("grundsätzlich formfrei", 160, 335, "v1b", "Bold", 36),
    z("Schuldner muss nicht mitwirken", 160, 395, beim("v1b", "Schuldner"), "Bold", 36),
    *okz("Ewald und Inkassobüro: geeinigt", 500, "v1c", "Bold", 36, x=160),
    *okz("Tanja weiß nichts: schadet nicht", 565, beim("v1c", "Dass"), "Bold", 36, x=160),
    *requisit([("vor", ("tabler", "list-numbers", 100, WEISS), "4 Voraussetzungen", WEISS),
               ("v1", ("ph", "handshake", 130, GELB), "Einigung", WEISS),
               ("v1c", ("ph", "handshake", 130, GRUEN), "geeinigt", GRUEN)]),
    *paar("vor", "EW", [("vor", "ruhig"), ("v1c", "froh")], "SV", [("vor", "ruhig"), ("v1c", "froh")]),
]))

# D2 2. Bestehen der Forderung, § 405 -----------------------------------------------------------------------------------------------
folie([("v2", "I. Voraussetzungen › 2. Bestehen der Forderung")], rechts_frei([
    *tafel("v2", "2. Bestehen der Forderung"),
    *neinz("grundsätzlich kein gutgläubiger Erwerb", 200, "v2b", "Bold", 36, x=160),
    z("von Forderungen", 160, 252, beim("v2b", "Forderungen"), "Bold", 36),
    z("Ausnahme § 405 BGB: Abtretung unter", 110, 345, "v405", "Bold", 36),
    z("Vorlage einer Schuldurkunde", 160, 397, beim("v405", "Vorlage"), size=36),
    *okz("Werklohn, § 631 Abs. 1 BGB: besteht", 500, "v2c", "Bold", 36, x=160),
    *requisit([("v2", ("tabler", "receipt-euro", 90, GELB), "Forderung", WEISS),
               ("v405", ("tabler", "file-certificate", 100, WEISS), "Schuldurkunde", WEISS),
               ("v2c", ("ph", "paint-roller", 120, GRUEN), "Werklohn", GRUEN)]),
    *paar("v2", "EW", [("v2", "ruhig"), ("v2c", "froh")], "TA", [("v2", "ruhig"), ("v2c", "denkt")]),
]))

# D3 3. Bestimmtheit -----------------------------------------------------------------------------------------------------------------
folie([("v3", "I. Voraussetzungen › 3. Bestimmbarkeit")], rechts_frei([
    *tafel("v3", "3. Bestimmt oder bestimmbar"),
    z("Forderung bestimmt oder wenigstens bestimmbar", 110, 190, beim("v3", "bestimmt"), "Bold", 36),
    z("künftige Forderung: spätestens bei", 110, 280, "v3k", "Bold", 36),
    z("ihrer Entstehung bestimmbar", 160, 332, beim("v3k", "Entstehung"), size=36),
    zit("BGH, Urt. v. 8.4.2020 – VIII ZR 130/19, Rn. 81", 160, 390, beim("v3k", "Entstehung")),
    *okz("Rechnung über 2.400 € gegen Tanja: eindeutig", 480, "v3b", "Bold", 36, x=160),
    *requisit([("v3", ("tabler", "search", 100, WEISS), "bestimmbar?", WEISS),
               ("v3b", ("tabler", "receipt-euro", 90, GRUEN), "eindeutig", GRUEN)]),
    *paar("v3", "TA", [("v3", "ruhig"), ("v3b", "denkt")], "SV", [("v3", "ruhig"), ("v3b", "froh")]),
]))

# D4 4. kein Ausschluss: § 399, § 354a HGB, § 400 ----------------------------------------------------------------------------------
folie([("v4", "I. Voraussetzungen › 4. kein Ausschluss")], rechts_frei([
    *tafel("v4", "4. kein Ausschluss"),
    z("§ 399 BGB: etwa vertragliches Abtretungsverbot", 110, 190, "v399", "Bold", 36),
    z("§ 354a HGB: beiderseitiges Handelsgeschäft,", 110, 280, "v354", "Bold", 36),
    z("Geldforderung: trotzdem wirksam", 160, 332, beim("v354", "Geldforderung"), size=36),
    z("§ 400 BGB: unpfändbare Forderung", 110, 420, "v400", "Bold", 36),
    z("nicht abtretbar", 160, 472, beim("v400", "abtretbar"), size=36),
    *okz("Ewald und Tanja: nichts ausgeschlossen", 570, "v4b", "Bold", 36, x=160),
    *requisit([("v399", ("tabler", "ban", 100, ROT), "Abtretungsverbot?", WEISS),
               ("v354", ("tabler", "building", 100, BLAU), "Handelsgeschäft", WEISS),
               ("v400", ("tabler", "lock", 90, WEISS), "unpfändbar", WEISS),
               ("v4b", ("tabler", "shield-check", 100, GRUEN), "nichts ausgeschlossen", GRUEN)]),
    *paar("v4", "EW", [("v4", "ruhig"), ("v4b", "froh")], "TA", [("v4", "ruhig"), ("v399", "denkt"), ("v4b", "ruhig")]),
]))

# D5 Abstraktionsprinzip -------------------------------------------------------------------------------------------------------------
folie([("abstr", "I. Voraussetzungen › Abstraktionsprinzip")], rechts_frei([
    *tafel("abstr", "Abstraktionsprinzip"),
    blk(110, 190, 1040, 140, GELB, beim("abstr", "Grund"), [("Grund: Forderungskauf", "ExtraBold", 40, INK),
                                                           ("§ 453 Abs. 1 BGB", "Bold", 34, INK)]),
    blk(110, 380, 1040, 140, GRUEN, "abstr2", [("Abtretung: die Verfügung", "ExtraBold", 40, INK),
                                               ("§ 398 BGB", "Bold", 34, INK)]),
    z("Wirksamkeit grundsätzlich unabhängig", 110, 580, beim("abstr2", "Ihre"), "Bold", 38),
    z("davon, ob der Kauf wirksam ist", 160, 636, beim("abstr2", "ob"), size=38),
    *requisit([("abstr", ("tabler", "receipt-euro", 90, GELB), "Forderungskauf", GELB),
               ("abstr2", ("tabler", "arrows-exchange", 110, GRUEN), "Verfügung", GRUEN)]),
    *paar("abstr", "EW", [("abstr", "ruhig")], "SV", [("abstr", "ruhig"), ("abstr2", "denkt")]),
]))

# E II. Rechtsfolge -------------------------------------------------------------------------------------------------------------------
folie([("rf", "Abtretung › II. Rechtsfolge, § 398 Satz 2 BGB")], rechts_frei([
    *tafel("rf", "II. Rechtsfolge"),
    z("§ 398 Satz 2 BGB: Mit dem Vertrag ist", 110, 190, beim("rf", "Mit"), "Bold", 38),
    z("das Inkassobüro Gläubiger", 160, 245, beim("rf", "Gläubiger"), size=38),
    z("§ 401 BGB: akzessorische Sicherheiten", 110, 340, "p401", "Bold", 36),
    z("(Bürgschaft, Pfandrecht, Hypothek)", 160, 392, beim("p401", "Bürgschaft"), size=36),
    z("gehen automatisch mit", 160, 444, beim("p401", "automatisch"), size=36),
    blk(110, 540, 1040, 110, BLAU, "rf2", [("Tanja schuldet 2.400 € dem Inkassobüro", "ExtraBold", 38, INK)]),
    *requisit([("rf", ("tabler", "arrows-exchange", 110, WEISS), "neuer Gläubiger", GRUEN),
               ("p401", ("tabler", "shield-check", 100, WEISS), "Sicherheiten", WEISS),
               ("rf2", ("tabler", "receipt-euro", 90, BLAU), "2.400 €", BLAU)]),
    *paar("rf", "TA", [("rf", "ruhig"), ("rf2", "sorge")], "SV", [("rf", "ruhig"), ("rf2", "froh")]),
]))

# F III. Schuldnerschutz: §§ 404, 406 ---------------------------------------------------------------------------------------------
folie([("schutz", "Abtretung › III. Schuldnerschutz"), ("p404", "III. Schuldnerschutz › §§ 404, 406 BGB")], rechts_frei([
    *tafel("schutz", "III. Schuldnerschutz"),
    z("Tanja soll nicht schlechter stehen", 110, 190, beim("schutz", "soll"), "Bold", 38),
    z("§ 404 BGB: Einwendungen, die bei der Abtretung", 110, 290, "p404", "Bold", 36),
    z("gegen Ewald begründet waren, bleiben", 160, 342, beim("p404", "gegen"), size=36),
    z("Beispiel: Mangel, fleckige Wand", 160, 400, "p404b", size=36),
    z("§ 406 BGB: Aufrechnung mit Forderung gegen", 110, 500, "p406", "Bold", 36),
    z("Ewald grundsätzlich auch gegenüber dem", 160, 552, beim("p406", "grundsätzlich"), size=36),
    z("Inkassobüro", 160, 604, beim("p406", "Inkassobüro"), size=36),
    *requisit([("schutz", ("tabler", "shield-check", 100, WEISS), "Schuldnerschutz", GRUEN),
               ("p404b", ("ph", "paint-roller", 120, WEISS), "fleckige Wand?", WEISS),
               ("p406", ("tabler", "arrows-exchange", 110, WEISS), "Aufrechnung", WEISS)]),
    *paar("schutz", "TA", [("schutz", "ruhig"), ("p404", "denkt"), ("p406", "froh")], "SV", [("schutz", "ruhig"), ("p404b", "sorge")]),
]))

# G1 § 407 Abs. 1 BGB (Wortlaut) ----------------------------------------------------------------------------------------------------
W407 = ["„(1) Der neue Gläubiger muss eine Leistung, die der Schuldner nach",
        "der Abtretung an den bisherigen Gläubiger bewirkt, … gegen sich",
        "gelten lassen, es sei denn, dass der Schuldner die Abtretung bei der",
        "Leistung … kennt.“"]
w407, w407_y = wortlaut(80, 175, 1100, W407, "§ 407 Abs. 1 BGB", "w407", marken=[
    (0, "nach", beim("w407", "nach")), (1, "an den bisherigen Gläubiger", beim("w407", "bisherigen")),
    (3, "kennt", beim("w407b", "kennt"))], size=32)
folie([("w407", "III. Schuldnerschutz › § 407 Abs. 1 BGB")], rechts_frei([
    *tafel("w407", "§ 407 Abs. 1 BGB"),
    *w407,
    z("maßgeblich: Kenntnis bei der Zahlung", 110, w407_y + 40, "kenn", "Bold", 38),
    *neinz("Kennenmüssen reicht nicht", w407_y + 120, beim("kenn", "Kennenmüssen"), "Bold", 36, x=160),
    *requisit([("w407", ("tabler", "cash-banknote", 110, GRUEN), "Leistung", WEISS),
               ("kenn", ("tabler", "eye-off", 100, WEISS), "Kenntnis?", WEISS)]),
    *paar("w407", "TA", [("w407", "ruhig"), ("kenn", "denkt")], "EW", [("w407", "ruhig")]),
]))

# G2 § 407 Abs. 1: Subsumtion ---------------------------------------------------------------------------------------------------------
folie([("sub407", "§ 407 Abs. 1 BGB › Tanja zahlt an Ewald")], rechts_frei([
    *tafel("sub407", "§ 407 Abs. 1 BGB im Fall"),
    *okz("Tanja wusste nichts", 200, beim("sub407", "wusste"), "Bold", 38, x=160),
    *okz("Zahlung nach der Abtretung an Ewald", 270, beim("sub407", "nach"), "Bold", 38, x=160),
    blk(110, 370, 1040, 150, GRUEN, "frei", [("Inkassobüro muss Zahlung gelten lassen:", "ExtraBold", 36, INK),
                                             ("Tanja wird frei", "ExtraBold", 40, INK)]),
    zit("BGH, Urt. v. 24.2.2022 – VII ZR 13/20, Rn. 35", 160, 545, beim("frei", "Bundesgerichtshof")),
    *requisit([("sub407", ("tabler", "cash-banknote", 110, GRUEN), "2.400 € an Ewald", WEISS),
               ("frei", ("tabler", "shield-check", 100, GRUEN), "frei", GRUEN)]),
    *paar("sub407", "TA", [("sub407", "ruhig"), ("frei", "froh")], "SV", [("sub407", "ruhig"), ("frei", "sorge")]),
]))

# H Ergänzungen §§ 409, 410 ---------------------------------------------------------------------------------------------------------
folie([("p409", "III. Schuldnerschutz › §§ 409, 410 BGB")], rechts_frei([
    *tafel("p409", "Ergänzungen: §§ 409, 410 BGB"),
    z("§ 409 BGB: Altgläubiger zeigt Abtretung an:", 110, 190, beim("p409", "Zeigt"), "Bold", 36),
    z("gilt dem Schuldner gegenüber,", 160, 242, beim("p409", "gegen"), size=36),
    z("auch wenn sie unwirksam ist", 160, 294, beim("p409", "unwirksam"), size=36),
    linienzug([(110, 380), (1150, 380)], "p410", breite=3),
    z("§ 410 BGB: Zahlung an den Neugläubiger", 110, 410, "p410", "Bold", 36),
    z("nur gegen Abtretungsurkunde,", 160, 462, beim("p410", "Abtretungsurkunde"), size=36),
    z("außer schriftlich angezeigt", 160, 514, beim("p410", "außer"), size=36),
    *requisit([("p409", ("tabler", "mail", 100, WEISS), "Anzeige", WEISS),
               ("p410", ("tabler", "certificate", 110, WEISS), "Abtretungsurkunde", WEISS)]),
    *paar("p409", "TA", [("p409", "ruhig"), ("p410", "denkt")], "SV", [("p409", "ruhig")]),
]))

# I Ergebnis (Bühne): Tanja frei, Inkassobüro gegen Ewald aus § 816 Abs. 2 --------------------------------------------------------
TX9, EX9, SX9 = 330, 1000, 1600
folie([("erg", "Ergebnis · Tanja muss nicht noch einmal zahlen"), ("p816", "Ergebnis › Inkassobüro gegen Ewald, § 816 Abs. 2 BGB")], [
    blk(80, 40, 1760, 100, GRUEN, "erg", [("Ergebnis: Tanja muss nicht noch einmal zahlen", "ExtraBold", 42, INK)]),
    z("Zahlung an Ewald wirkt nach § 407 Abs. 1 BGB auch gegenüber dem Inkassobüro", 110, 165, beim("erg", "Ihre"), "Bold", 34,
      rechts=1820),
    boden("erg"),
    *fl("TA", TX9, [("erg", "froh_r")], erst="pop"),
    ns("Tanja", TX9, BODEN, "erg", NFARBE["TA"], d=0.1),
    pl("frei", TX9, 300, beim("erg", "Ihre"), fill=GRUEN, size=32, anker="m"),
    *fl("EW", EX9, [("erg", "ruhig_r"), ("p816", "sorge_r")], erst="pop", d=0.1),
    ns("Ewald", EX9, BODEN, "erg", NFARBE["EW"], d=0.2),
    *fl("SV", SX9, [("erg", "sorge"), ("p816", "denkt")], erst="pop", d=0.2),
    ns("Sven", SX9, BODEN, "erg", NFARBE["SV"], d=0.3),
    ficon("ph", "building-office", 1790, 560, 120, "erg", fuell=BLAU),
    pfeil(1470, 560, 1140, 560, "p816", breite=10, kopf=30),
    pl("§ 816 Abs. 2 BGB", 1305, 470, "p816", fill=WEISS, size=30, anker="m"),
    pl("Nichtberechtigter", EX9, 300, beim("p816b", "Nichtberechtigter"), fill=WEISS, size=30, anker="m"),
    pl("2.400 € herausgeben", 1305, 600, beim("p816b", "herausgeben"), fill=GELB, size=30, anker="m"),
])

# J Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · Abtretung im Anspruchsaufbau")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Neugläubiger: ursprünglicher Anspruch", 200, 200, beim("tipp", "Neugläubiger"), "Bold", 38),
    z("i. V. m. § 398 BGB", 200, 258, beim("tipp", "Verbindung"), size=36),
    z("1. Anspruch entstanden und übergegangen?", 200, 360, "tipp2", "Bold", 36),
    z("2. § 407 BGB beim Erlöschen,", 200, 450, "tipp3", "Bold", 36),
    z("zusammen mit § 362 Abs. 1 BGB", 250, 505, beim("tipp3", "zusammen"), size=36),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# K Klausurschema ---------------------------------------------------------------------------------------------------------------------
K1, K2 = 150, 230
folie([("sch", "Klausurschema"), ("k2", "Klausurschema › II. Übergang durch Abtretung"),
       ("k3", "Klausurschema › III. nicht erloschen, durchsetzbar"), ("k4", "Klausurschema › IV. Ergebnis")], [
    karte(60, 50, 1800, 900, "sch"),
    titel(glyphen("Klausurschema: Anspruch des Neugläubigers"), 110, 90, "sch", 46),
    z("I. Anspruch entstanden", K1, 200, "k1", "Bold", 40, rechts=1820),
    z("II. Übergang durch Abtretung, § 398 BGB", K1, 280, "k2", "Bold", 40, rechts=1820),
    z("1. Abtretungsvertrag  2. Bestehen der Forderung", K2, 340, beim("k2a", "Vertrag"), size=36, rechts=1820),
    z("3. Bestimmbarkeit  4. kein Ausschluss", K2, 395, beim("k2a", "Bestimmbarkeit"), size=36, rechts=1820),
    z("III. Anspruch nicht erloschen und durchsetzbar", K1, 480, "k3", "Bold", 40, rechts=1820),
    z("Schuldnerschutz: §§ 404, 406, 407 BGB", K2, 540, "k3a", size=36, rechts=1820),
    z("IV. Ergebnis", K1, 625, "k4", "Bold", 40, rechts=1820),
    z("Schuldner frei: Ausgleich über § 816 Abs. 2 BGB", K2, 685, "k5", size=36, rechts=1820),
])

# L Merksatz (Lexi) ---------------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Die Abtretung ", 0), ("wechselt den Gläubiger,", "a")], [("ohne den Schuldner zu fragen.", 0)]],
                750, 310, 42, "merke", {"a": beim("merke", "wechselt")}),
    *markertext([[("Deshalb darf sie ihn nicht ", 0), ("schlechter", "b")], [("stellen", "b"), (": Wer nichts von ihr weiß,", 0)],
                 [("zahlt beim Altgläubiger", 0)], [("mit befreiender Wirkung.", "c")]],
                750, 500, 42, "m2", {"b": beim("m2", "schlechter"), "c": beim("m2", "befreiender")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
