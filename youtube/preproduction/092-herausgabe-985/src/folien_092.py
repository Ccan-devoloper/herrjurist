"""Folge 092 · § 985 BGB: Der Herausgabeanspruch – Prüfungsschema Vindikation – Serienstandard Open Peeps (Katzenkönig).
Beispielfall: Theresa kauft sich lange vor dem Zusammenziehen einen Plattenspieler; in der gemeinsamen Wohnung darf Clemens ihn
mitbenutzen; nach der Trennung bleibt er bei Clemens, Theresa fordert ihn zurück.
Szenen laut ../SZENENPLAN.md: A1 Kauf (Laden), A2 gemeinsame Wohnung, A3 Trennung/Frage, B Sachverhalt, C Wortlaut § 985 und
drei Prüfungspunkte, D1 I. Eigentum historisch, D2 § 1006, E II. Besitz, F Wortlaut § 986 I 1, G eigenes/abgeleitetes
Besitzrecht, H Einwendung und Beweislast, I Ergebnis/Rechtsfolge (Abholung, Holschuld), J § 604 und Ausblick §§ 987 ff.,
K Klausurtipp (Lexi), L Klausurschema, M Merksatz (Lexi).
Zwei Handlungsgeräusche (Karton beim Auszug, Klopfen an der Tür beim Abholen; ../geraeusche_herkunft.json).
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/hand als
eigene Kopie aus Folge 083 (gemeinsame Dateien unverändert). Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_092/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_092/" in n:
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 027/073) ------------------------------------
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
TH_N, CL_N = ROT, LILA                         # Farben der Namensschilder
PX, PY, PU = 1570, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"TH": "Theresa", "CL": "Clemens"}
NFARBE = {"TH": TH_N, "CL": CL_N}


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
    """Tafelszene: zwei Figuren rechts der Tafel, beide blicken zur Tafel (nach links); l, r = Kürzel TH/CL."""
    return [*fig(l, X1, FB, FR, lf), ns(NAME[l], X1, FB, c0, NFARBE[l], d=0.1),
            *fig(r, X2, FB, FR, rf, d=0.2), ns(NAME[r], X2, FB, c0, NFARBE[r], d=0.3)]




PLATTE = ("tabler", "vinyl", 110, BLAU)


def platte(cx, cue, breite=190, unten=BODEN, bis=None, anim="pop", d=0.0):
    """Der Plattenspieler von Theresa (Tabler vinyl mit Tonarm, Teller blau gefüllt), ohne Marke."""
    return ficon("tabler", "vinyl", cx, unten, breite, cue, fuell=BLAU, bis=bis, anim=anim, d=d)


# A1 Fall: der Kauf im Laden ------------------------------------------------------------------------------------------------
TX1, LX1 = 620, 1500
PL0, PL1 = 1200, 900                                   # Plattenspieler im Laden → bei Theresa
KAUF = (beim("fall", "Plattenspieler"), beim("fall", "Plattenspieler", ende=True))
folie([(NULL, "Fall · Der Kauf")], [
    hart(pl("Theresa kauft sich einen Plattenspieler", 70, 40, NULL, fill=GELB, size=44)),
    hart(boden(NULL)),
    hart(ficon("tabler", "building-store", LX1, BODEN, 340, NULL, fuell=GELB)),
    hart(platte(PL0, NULL, bis=KAUF[0])),
    bewegt(platte(PL1, KAUF[0], anim="cut"), *KAUF, PL0 - PL1, 0),
    ficon("ph", "receipt", PL1, 560, 80, KAUF[1], fuell=WEISS),
    pl("gekauft", PL1, 590, KAUF[1], fill=GRUEN, size=30, anker="m"),
    ficon("tabler", "calendar-event", 1200, 420, 80, "lange", fuell=WEISS),
    pl("lange vor dem Zusammenziehen", 1200, 440, "lange", fill=WEISS, size=30, anker="m"),
    *fig("TH", TX1, BODEN, FH, [(NULL, "ruhig_r")], bis="th1", erst="cut"),
    *redet("TH_redet_r", TX1, BODEN, FH, "th1", "zusammen"),
    hart(ns("Theresa", TX1, BODEN, NULL, TH_N)),
    blase("sprech", 720, 220, "th1", 900, 240, inhalt=["Endlich mein eigener", "Plattenspieler!"], textsize=36,
          figur=("TH_redet_r", TX1, BODEN, FH), bis="zusammen"),
])

# A2 Fall: das gemeinsame Wohnzimmer ----------------------------------------------------------------------------------------
TX2, CX2, PL2, SO2 = 520, 1480, 820, 1120
folie([("zusammen", "Fall · Die gemeinsame Wohnung")], [
    pl("Die gemeinsame Wohnung", 70, 40, "zusammen", fill=GELB, size=44),
    boden("zusammen"),
    ficon("ph", "couch", SO2, BODEN, 300, "zusammen", fuell=GRUEN),
    platte(PL2, beim("zusammen", "Plattenspieler"), breite=170),
    pl("gemeinsames Wohnzimmer", 960, 470, beim("zusammen", "Wohnzimmer"), fill=WEISS, size=30, anker="m"),
    ficon("ph", "music-notes", PL2, 650, 80, beim("th2", "nutz"), fuell=WEISS),
    *fig("TH", TX2, BODEN, FH, [("zusammen", "froh_r")], bis="cl1", erst="pop"),
    *fig("TH", TX2, BODEN, FH, [("cl1", "ruhig_r")], bis="th2", erst="cut"),
    *redet("TH_redet_r", TX2, BODEN, FH, "th2", "trennung"),
    ns("Theresa", TX2, BODEN, "zusammen", TH_N),
    *fig("CL", CX2, BODEN, FH, [("zusammen", "ruhig")], bis="cl1", erst="pop", d=0.2),
    *redet("CL_redet", CX2, BODEN, FH, "cl1", "th2"),
    *fig("CL", CX2, BODEN, FH, [("th2", "froh")], erst="cut"),
    ns("Clemens", CX2, BODEN, "zusammen", CL_N, d=0.3),
    blase("sprech", 700, 220, "cl1", 1100, 240, inhalt=["Darf ich auch mal", "Platten auflegen?"], textsize=36,
          figur=("CL_redet", CX2, BODEN, FH), bis="th2"),
    blase("sprech", 640, 200, "th2", 840, 240, inhalt=["Klar, nutz ihn", "ruhig mit."], textsize=36,
          figur=("TH_redet_r", TX2, BODEN, FH), bis="trennung"),
])

# A3 Fall: die Trennung -----------------------------------------------------------------------------------------------------
TX3, CX3, PL3, HX3 = 520, 1480, 1210, 1790
TH3H = hand("TH_ruhig_r", TX3, BODEN, FH, +1)
folie([("trennung", "Fall · Nach der Trennung"), ("frage", "Fall · Die Frage")], [
    pl("Nach der Trennung", 70, 40, "trennung", fill=GELB, size=44, bis="frage"),
    boden("trennung"),
    ficon("tabler", "door", 170, BODEN, 200, "trennung", fuell=GELB),
    ficon("ph", "house", HX3, BODEN, 170, "trennung", fuell=WEISS),
    szene(ficon("tabler", "package", TH3H[0] + 120, BODEN, 150, beim("trennung", "aus"), fuell=GELB), "092karton*", 0.8, 0.0),
    pl("Theresa zieht aus", TX3, 300, beim("trennung", "aus"), fill=WEISS, size=30, anker="m", bis="th3"),
    platte(PL3, "trennung", breite=170),
    pl("bleibt bei Clemens", PL3, 580, beim("bleibt", "bei"), fill=WEISS, size=30, anker="m", bis="th3"),
    *fig("TH", TX3, BODEN, FH, [("trennung", "ruhig_r")], bis="th3"),
    *redet("TH_bittet_r", TX3, BODEN, FH, "th3", "cl2"),
    *fig("TH", TX3, BODEN, FH, [("cl2", "ruhig_r"), ("frage", "denkt_r")], erst="cut"),
    ns("Theresa", TX3, BODEN, "trennung", TH_N),
    *fig("CL", CX3, BODEN, FH, [("trennung", "ruhig")], bis="cl2", d=0.2),
    *redet("CL_meint", CX3, BODEN, FH, "cl2", "frage"),
    *fig("CL", CX3, BODEN, FH, [("frage", "denkt")], erst="cut"),
    ns("Clemens", CX3, BODEN, "trennung", CL_N, d=0.3),
    blase("sprech", 760, 220, "th3", 860, 240, inhalt=["Clemens, ich möchte", "meinen Plattenspieler zurück."],
          textsize=34, figur=("TH_bittet_r", TX3, BODEN, FH), bis="cl2"),
    blase("sprech", 800, 220, "cl2", 1080, 240, inhalt=["Wir haben ihn doch zusammen", "genutzt. Er kann hierbleiben."],
          textsize=34, figur=("CL_meint", CX3, BODEN, FH), bis="frage"),
    pl("Kann Theresa den Plattenspieler herausverlangen?", 960, 40, "frage", fill=PINK, size=40, anker="m"),
    pl("Und wie prüfst du das in der Klausur?", 960, 130, "frage2", fill=WEISS, size=36, anker="m"),
])


# B Sachverhalt ---------------------------------------------------------------------------------------------------------------
def sachverhalt_092(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=38, zeilenabstand=1.34)
        els += e; y += 26
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=38))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_092("sv", [
    "Theresa kauft sich einen Plattenspieler, lange bevor sie mit Clemens zusammenzieht. Der Händler übereignet ihn ihr.",
    "In der gemeinsamen Wohnung stellt sie ihn ins Wohnzimmer und erlaubt Clemens, ihn mitzubenutzen. Für wie lange, "
    "vereinbaren die beiden nicht.",
    "Nach der Trennung zieht Theresa aus. Der Plattenspieler bleibt in der Wohnung von Clemens. Theresa fordert ihn "
    "zurück; Clemens möchte ihn behalten, weil beide ihn zusammen genutzt haben.",
], "Kann Theresa den Plattenspieler herausverlangen?")

# C § 985 (Wortlaut) und drei Prüfungspunkte ------------------------------------------------------------------------------------
W985 = ["„Der Eigentümer kann von dem Besitzer die Herausgabe der",
        "Sache verlangen.“"]
w985, w985_y = wortlaut(80, 190, 1100, W985, "§ 985 BGB", "w985", marken=[
    (0, "Eigentümer", beim("w985", "Eigentümer")), (0, "Besitzer", beim("w985", "Besitzer")),
    (0, "Herausgabe", beim("w985", "Herausgabe"))], size=36)
PUNKTE = [("v1", "I. Theresa ist Eigentümerin"), ("v2", "II. Clemens ist Besitzer"), ("v3", "III. kein Recht zum Besitz")]
folie([("p985", "Anspruchsgrundlage · § 985 BGB"), ("drei", "§ 985 BGB › 3 Prüfungspunkte")], rechts_frei([
    *tafel("p985", "Herausgabeanspruch"),
    *w985,
    z("3 Prüfungspunkte", 110, w985_y + 40, "drei", "Bold", 40),
    *[z(t, 160, w985_y + 120 + 80 * i, c, "Bold", 40) for i, (c, t) in enumerate(PUNKTE)],
    *requisit([("p985", PLATTE, "Herausgabe?", WEISS), ("drei", ("tabler", "list-check", 110, WEISS), "3 Prüfungspunkte", WEISS)]),
    *paar("p985", "TH", [("p985", "ruhig"), ("v1", "froh")], "CL", [("p985", "ruhig"), ("v3", "denkt")]),
]))

# D1 I. Eigentum, historisch -------------------------------------------------------------------------------------------------
folie([("eig", "I. Eigentum › historisch prüfen"), ("verlust", "I. Eigentum › später verloren?")], rechts_frei([
    *tafel("eig", "I. Eigentum: historisch prüfen"),
    z("1. Am Anfang: der Kauf", 110, 195, "urspr", "Bold", 38),
    *okz("Händler übereignet an Theresa (§ 929 S. 1 BGB)", 255, beim("urspr", "übereignet"), size=34, x=160),
    z("2. Später verloren?", 110, 345, "verlust", "Bold", 38),
    *neinz("Zusammenziehen: weder geschenkt noch übereignet", 405, "zus2", size=34, x=160),
    z("es fehlt schon an der Einigung", 160, 457, beim("zus2", "Einigung"), size=34),
    *neinz("kein Dritter hat ihn erworben, auch nicht gutgläubig", 530, "dritte", size=34, x=160),
    zit("Mehr dazu in den Videos zur Übereignung und zum gutgläubigen Erwerb", 160, 590, beim("dritte", "Videos"), size=28),
    *requisit([("eig", ("tabler", "list-numbers", 100, WEISS), "Schritt für Schritt", WEISS),
               ("urspr", ("ph", "receipt", 90, WEISS), "gekauft", GRUEN),
               ("zus2", ("ph", "couch", 140, GRUEN), "Zusammenziehen", WEISS),
               ("dritte", ("ph", "handshake", 120, WEISS), "kein Erwerb Dritter", WEISS)]),
    *paar("eig", "TH", [("eig", "ruhig"), ("zus2", "froh")], "CL", [("eig", "ruhig"), ("verlust", "denkt"), ("zus2", "ruhig")]),
]))

# D2 § 1006 BGB, Ergebnis Eigentum ---------------------------------------------------------------------------------------------
folie([("p1006", "I. Eigentum › Vermutung, § 1006 BGB"), ("eig2", "I. Eigentum › Theresa ist Eigentümerin")], rechts_frei([
    *tafel("p1006", "Eigentumsvermutung"),
    z("§ 1006 Abs. 1 S. 1 BGB: Vermutung für den Besitzer", 110, 200, "p1006", "Bold", 36),
    *neinz("hilft Clemens nicht", 280, beim("p1006", "hilft"), "Bold", 36, x=160),
    z("fest steht: nur mitbenutzt,", 160, 350, beim("p1006", "fest"), size=34),
    z("nie Eigentum erworben", 160, 402, beim("p1006", "nie"), size=34),
    zit("vgl. BGH, Versäumnisurt. v. 3.3.2017 – V ZR 268/15, Rn. 18, 27", 160, 462, beim("p1006", "erworben")),
    blk(110, 550, 1040, 100, GRUEN, "eig2", [("Theresa ist Eigentümerin geblieben", "ExtraBold", 40, INK)]),
    *requisit([("p1006", ("ph", "scales", 120, WEISS), "Vermutung?", WEISS),
               ("eig2", PLATTE, "gehört Theresa", GRUEN)]),
    *paar("p1006", "TH", [("p1006", "ruhig"), ("eig2", "froh")], "CL", [("p1006", "ruhig"), (beim("p1006", "hilft"), "sorge")]),
]))

# E II. Besitz -------------------------------------------------------------------------------------------------------------------
folie([("bes", "II. Besitz › § 854 Abs. 1 BGB"), ("mittel", "II. Besitz › mittelbarer Besitz, § 868 BGB")], rechts_frei([
    *tafel("bes", "II. Besitz von Clemens"),
    z("Besitz: tatsächliche Gewalt über die Sache", 110, 200, beim("bes", "tatsächliche"), "Bold", 36),
    zit("§ 854 Abs. 1 BGB", 160, 255, beim("bes", "Paragraf")),
    *okz("Plattenspieler steht in seiner Wohnung:", 330, "bes2", size=34, x=160),
    z("unmittelbarer Besitzer", 160, 382, beim("bes2", "unmittelbarer"), "Bold", 36),
    linienzug([(110, 465), (1150, 465)], "mittel", breite=3),
    z("Auch der mittelbare Besitzer (§ 868 BGB),", 110, 495, "mittel", "Bold", 36),
    z("etwa wer die Sache verliehen hat,", 160, 550, beim("mittel", "etwa"), size=34),
    z("kann Anspruchsgegner sein", 160, 602, beim("mittel", "Anspruchsgegner"), size=34),
    *requisit([("bes", ("tabler", "hand-grab", 110, WEISS), "tatsächliche Gewalt", BLAU),
               ("bes2", ("ph", "house", 120, WEISS), "in seiner Wohnung", GRUEN),
               ("mittel", ("ph", "handshake", 120, WEISS), "mittelbarer Besitz", WEISS)]),
    *paar("bes", "TH", [("bes", "ruhig")], "CL", [("bes", "ruhig"), ("bes2", "denkt")]),
]))

# F III. kein Recht zum Besitz, Wortlaut § 986 Abs. 1 S. 1 ----------------------------------------------------------------------------
W986 = ["„Der Besitzer kann die Herausgabe der Sache verweigern, wenn er",
        "oder der mittelbare Besitzer, von dem er sein Recht zum Besitz",
        "ableitet, dem Eigentümer gegenüber zum Besitz berechtigt ist.“"]
w986, w986_y = wortlaut(80, 190, 1100, W986, "§ 986 Abs. 1 Satz 1 BGB", "w986", marken=[
    (0, "verweigern", beim("w986", "verweigern")), (0, "wenn er", beim("w986", "wenn")),
    (1, "der mittelbare Besitzer", beim("w986", "mittelbare")), (2, "zum Besitz berechtigt", beim("w986", "berechtigt"))],
    size=32)
folie([("rzb", "III. kein Recht zum Besitz › § 986 Abs. 1 S. 1 BGB")], rechts_frei([
    *tafel("rzb", "III. Kein Recht zum Besitz"),
    *w986,
    *requisit([("rzb", PLATTE, "Recht zum Besitz?", WEISS),
               (beim("w986", "berechtigt"), ("tabler", "shield-check", 110, GRUEN), "zum Besitz berechtigt?", WEISS)]),
    *paar("rzb", "TH", [("rzb", "ruhig")], "CL", [("rzb", "ruhig"), (beim("w986", "berechtigt"), "denkt")]),
]))

# G eigenes und abgeleitetes Besitzrecht --------------------------------------------------------------------------------------
folie([("eigen", "III. › eigenes Besitzrecht: Leihe"), ("ende", "III. › Ende des Besitzrechts"),
       ("abgel", "III. › abgeleitetes Besitzrecht")], rechts_frei([
    *tafel("eigen", "Recht zum Besitz?"),
    z("1. Eigenes Besitzrecht aus Vertrag", 110, 190, "eigen", "Bold", 38),
    z("unentgeltliche Mitbenutzung: etwa Leihe (§ 598 BGB)", 160, 248, beim("leihe", "Leihe"), size=34),
    zit("vgl. BGH, Beschl. v. 10.3.2021 – XII ZB 243/20, Rn. 41", 160, 302, beim("leihe", "Leihe")),
    z("solange durfte Clemens besitzen", 160, 350, beim("leihe", "Solange"), size=34),
    z("keine feste Zeit vereinbart", 160, 410, "ende", size=34),
    *neinz("endet mit der Rückforderung (§ 604 Abs. 3 BGB)", 465, beim("ende", "endet"), "Bold", 34, x=160),
    linienzug([(110, 545), (1150, 545)], "abgel", breite=3),
    z("2. Abgeleitetes Besitzrecht", 110, 570, "abgel", "Bold", 38),
    zit("§ 986 Abs. 1 S. 1 Alt. 2 BGB", 160, 624, "abgel"),
    z("etwa ein Freund, dem Clemens ihn weiterleiht:", 160, 672, beim("abgel", "Freund"), size=34),
    z("nur, wenn Clemens berechtigt ist und", 160, 724, beim("abgel", "nur"), size=34),
    z("ihn weitergeben darf", 160, 776, beim("abgel", "weitergeben"), size=34),
    *requisit([("eigen", ("tabler", "file-certificate", 100, WEISS), "Vertrag", WEISS),
               ("leihe", ("ph", "handshake", 120, WEISS), "Leihe", GELB),
               ("ende", ("tabler", "calendar-event", 90, WEISS), "keine feste Zeit", WEISS),
               (beim("ende", "zurückfordert"), ("tabler", "arrow-back-up", 100, WEISS), "zurückgefordert", HELLROT),
               ("abgel", PLATTE, "weitergeliehen?", WEISS)]),
    *paar("eigen", "TH", [("eigen", "ruhig"), (beim("ende", "zurückfordert"), "froh"), ("abgel", "ruhig")],
          "CL", [("eigen", "ruhig"), ("leihe", "froh"), (beim("ende", "endet"), "sorge"), ("abgel", "denkt")]),
]))

# H Einwendung und Beweislast -----------------------------------------------------------------------------------------------------
folie([("einw", "III. › Einwendung, keine Einrede"), ("beweis", "III. › Beweislast")], rechts_frei([
    *tafel("einw", "Einwendung, keine Einrede"),
    z("Das Gericht beachtet es von Amts wegen,", 110, 200, beim("einw", "Gericht"), "Bold", 36),
    z("wenn die Tatsachen vorgetragen sind", 160, 255, beim("einw", "Tatsachen"), size=34),
    z("Darlegen und beweisen muss es Clemens", 110, 345, "beweis", "Bold", 36),
    zit("vgl. BGH, Beschl. v. 10.3.2021 – XII ZB 243/20, Rn. 42", 160, 400, beim("beweis", "Clemens")),
    blk(110, 480, 1040, 100, GELB, "kein", [("Hier: kein Recht zum Besitz mehr", "ExtraBold", 40, INK)]),
    *requisit([("einw", ("tabler", "gavel", 100, WEISS), "von Amts wegen", WEISS),
               ("beweis", ("ph", "scales", 120, WEISS), "Beweislast: Clemens", WEISS),
               ("kein", ("tabler", "shield-x", 110, HELLROT), "kein Recht zum Besitz", HELLROT)]),
    *paar("einw", "TH", [("einw", "ruhig"), ("kein", "froh")], "CL", [("einw", "ruhig"), ("beweis", "denkt"), ("kein", "sorge")]),
]))

# I Ergebnis und Rechtsfolge: Theresa holt den Plattenspieler ab ---------------------------------------------------------------
TX4, TU4, CX4, PL4 = 680, 1060, 1480, 1270
HOLT = (beim("ort", "holt"), beim("ort", "ab", ende=True))
folie([("erg", "Ergebnis · § 985 BGB"), ("ort", "Rechtsfolge › Herausgabe am Ort der Sache")], [
    pl("Ergebnis", 70, 40, "erg", fill=GELB, size=44),
    boden("erg"),
    szene(ficon("tabler", "door", TU4, BODEN, 190, "erg", fuell=GELB), "092klopfen*", 0.7, 0.4),
    ficon("ph", "house", 1790, BODEN, 170, "erg", fuell=WEISS),
    platte(PL4, "erg", breite=140, bis=HOLT[0]),
    bewegt(platte(TX4 + 170, HOLT[0], breite=140, anim="cut"), *HOLT, PL4 - (TX4 + 170), 0),
    pl("Herausgabe nach § 985 BGB", 960, 140, beim("erg", "Theresa"), fill=GRUEN, size=36, anker="m"),
    pl("dort, wo er steht: in seiner Wohnung", 960, 230, "ort", fill=WEISS, size=32, anker="m"),
    pl("Theresa holt ihn ab: Holschuld", 960, 310, beim("ort", "Holschuld"), fill=GELB, size=32, anker="m"),
    *fig("TH", TX4, BODEN, FH, [("erg", "ruhig_r"), (HOLT[0], "froh_r")]),
    ns("Theresa", TX4, BODEN, "erg", TH_N),
    *fig("CL", CX4, BODEN, FH, [("erg", "ruhig")], d=0.2),
    ns("Clemens", CX4, BODEN, "erg", CL_N, d=0.3),
])

# J Daneben: § 604 BGB; Ausblick §§ 987 ff. BGB -------------------------------------------------------------------------------
folie([("p604", "Daneben · § 604 BGB"), ("ebv", "Ausblick · §§ 987 ff. BGB")], rechts_frei([
    *tafel("p604", "Daneben und danach"),
    z("§ 604 BGB: vertraglicher Rückgabeanspruch", 110, 200, beim("p604", "vertraglichen"), "Bold", 36),
    z("aus der Leihe", 160, 255, beim("p604", "Leihe"), size=34),
    *okz("Beide Ansprüche stehen nebeneinander", 330, beim("p604", "Beide"), "Bold", 34, x=160),
    linienzug([(110, 420), (1150, 420)], "ebv", breite=3),
    z("Nutzungen herausgeben? Schadensersatz?", 110, 450, beim("ebv", "Nutzungen"), "Bold", 36),
    z("§§ 987 ff. BGB: Eigentümer-Besitzer-Verhältnis", 160, 510, beim("ebv", "Paragrafen"), size=34),
    *requisit([("p604", ("ph", "handshake", 120, WEISS), "Leihe, § 604 BGB", GELB),
               (beim("p604", "Beide"), ("tabler", "arrows-exchange", 110, WEISS), "nebeneinander", GRUEN),
               ("ebv", ("ph", "scales", 120, WEISS), "§§ 987 ff. BGB", WEISS)]),
    *paar("p604", "TH", [("p604", "ruhig")], "CL", [("p604", "ruhig"), ("ebv", "denkt")]),
]))

# K Klausurtipp (Lexi) ---------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · Eigentum historisch prüfen")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Eigentum immer historisch prüfen", 200, 200, beim("tipp", "Prüfe"), "Bold", 38),
    z("Beginne bei der Person, die unstreitig", 200, 300, "tipp2", size=34),
    z("Eigentümerin war,", 200, 352, beim("tipp2", "Eigentümerin"), size=34),
    z("und prüfe jeden späteren Erwerb der Reihe nach", 200, 404, beim("tipp2", "prüfe"), size=34),
    *neinz("Heutiger Besitzer = Eigentümer?", 500, "tipp3", "Bold", 36, x=200),
    z("Damit verschenkst du Punkte", 200, 556, beim("tipp3", "verschenkt"), size=34),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# L Klausurschema --------------------------------------------------------------------------------------------------------------
K1, K2 = 150, 230
folie([("sch", "Klausurschema"), ("k2", "Klausurschema › II. Besitz"), ("k3", "Klausurschema › III. kein Recht zum Besitz"),
       ("k4", "Klausurschema › IV. Rechtsfolge")], [
    karte(60, 50, 1800, 900, "sch"),
    titel(glyphen("Klausurschema: Herausgabeanspruch, § 985 BGB"), 110, 90, "sch", 46),
    z("I. Eigentum des Anspruchstellers", K1, 210, "k1", "Bold", 40, rechts=1820),
    z("historisch geprüft", K2, 264, "k1b", size=36, rechts=1820),
    z("II. Besitz des Anspruchsgegners", K1, 350, "k2", "Bold", 40, rechts=1820),
    z("unmittelbar oder mittelbar", K2, 404, "k2b", size=36, rechts=1820),
    z("III. kein Recht zum Besitz, § 986 BGB", K1, 490, "k3", "Bold", 40, rechts=1820),
    z("eigenes oder abgeleitetes", K2, 544, "k3b", size=36, rechts=1820),
    z("IV. Rechtsfolge: Herausgabe der Sache", K1, 630, "k4", "Bold", 40, rechts=1820),
])

# M Merksatz (Lexi) ------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Der Eigentümer bekommt seine", 0)], [("Sache vom Besitzer ", 0), ("zurück.", "a")]],
                750, 320, 46, "merke", {"a": beim("merke", "zurück")}),
    *markertext([[("Es sei denn, der Besitzer hat ihm", 0)], [("gegenüber ein ", 0), ("Recht zum Besitz.", "b")]],
                750, 560, 46, "m2", {"b": beim("m2", "Recht")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
