"""Folge 133 · Für Freunde bürgen? Bürgschaft Schema §§ 765 ff. BGB – Serienstandard Open Peeps (Katzenkönig).
Fall: Hilke nimmt für eine neue Küche einen Bankkredit über 15.000 € auf (Zinsen 75 € im Monat); ihre Schwester Marlies
(netto 3.400 €) unterschreibt in der Bank „Ich bürge selbstschuldnerisch für den Kredit von Hilke über 15.000 Euro.“
Zwei Jahre später sind 9.000 € offen, Herr Seibold von der Bank verlangt sie von Marlies.
Szenen laut ../SZENENPLAN.md: A1 Küche, A2 Bank (Bürgschaft verlangt, Bitte, Urkunde), A3 zwei Jahre später (Frage),
B Sachverhalt, C Anspruch § 765 Abs. 1 (Wortlaut) und Aufbau, D1 I. 1. Bürgschaftsvertrag, § 766 (Wortlaut), § 126, § 350 HGB,
D2 I. 2. Sittenwidrigkeit (BGH XI ZR 82/11), D3 I. 3. Hauptschuld § 767 (Wortlaut) und II. Erlöschen, D4 III. §§ 768, 770,
D5 § 771 und § 773 Abs. 1 Nr. 1 (Wortlaut), E Ergebnis (Bühne), F IV. Rückgriff § 774 (Wortlaut), § 670, G Klausurtipp (Lexi),
H Klausurschema, I Merksatz (Lexi).
Zwei Handlungsgeräusche (Unterschrift, Brief; ../geraeusche_herkunft.json). Namensschild jeder Figur, solange sie im Bild
ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/hand als eigene Kopie aus Folge 099 (gemeinsame Dateien
unverändert). Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_133/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_133/" in n:
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
NAME = {"MA": "Marlies", "HI": "Hilke", "SE": "Herr Seibold"}
NFARBE = {"MA": LILA, "HI": ROT, "SE": BLAU}


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



# A1 Fall: der Kredit für die Küche -------------------------------------------------------------------------------------------
HX1 = 1180
folie([(NULL, "Fall · Der Kredit für die Küche")], [
    hart(pl("Hilke will eine neue Küche", 70, 30, NULL, fill=GELB, size=44)),
    hart(boden(NULL)),
    hart(ficon("tabler", "fridge", 260, BODEN, 300, NULL, fuell=WEISS)),
    hart(ficon("tabler", "cooker", 560, BODEN, 260, NULL, fuell=GELB)),
    hart(ficon("tabler", "microwave", 560, BODEN - ficon("tabler", "cooker", 560, BODEN, 260, "_").sprite.height + 4, 170, NULL, fuell=WEISS)),
    *fl("HI", HX1, [(NULL, "froh"), ("kredit", "ruhig"), ("zins", "sorge")]),
    hart(ns("Hilke", HX1, BODEN, NULL, NFARBE["HI"])),
    ficon("tabler", "building-bank", 1620, 300, 150, "kredit", fuell=BLAU),
    pl("Kredit: 15.000 €", 1620, 330, beim("kredit", "Kredit"), fill=GELB, size=32, anker="m"),
    pl("Zinsen: 75 € im Monat", 1620, 410, beim("zins", "Zinsen"), fill=WEISS, size=32, anker="m"),
])

# A2 Fall: die Bank will eine Bürgschaft, Hilke fragt Marlies, Marlies unterschreibt -------------------------------------------
SX2, HX2, MX2 = 430, 1110, 1610
MHX, MHY = hand("MA_ruhig", MX2, BODEN, FH, -1)
UNT = beim("urk", "Euro")
folie([("bank", "Fall · Die Bank will eine Bürgschaft"), ("netto", "Fall · Marlies unterschreibt")], [
    pl("Bei der Bank", 70, 30, "bank", fill=GELB, size=44),
    boden("bank"),
    ficon("tabler", "building-bank", 120 + 60, 420, 120, "bank", fuell=BLAU),
    *fl("SE", SX2, [("bank", "ruhig_r")], bis="se1", erst="pop"),
    *redet("SE_redet_r", SX2, BODEN, FH, "se1", "frag"),
    *fl("SE", SX2, [("frag", "ruhig_r"), (beim("an", "nimmt"), "froh_r")]),
    karte(200, 660, 470, 200, "bank", fill=BLAU, rund=12, schatten=6, rand=5),
    ns("Herr Seibold", SX2, BODEN, "bank", NFARBE["SE"], d=0.1),
    *fl("HI", HX2, [("bank", "ruhig")], bis="hi1", erst="pop", d=0.1),
    *redet("HI_redet_r", HX2, BODEN, FH, "hi1", "ma1"),
    *fl("HI", HX2, [("ma1", "froh_r"), ("netto", "ruhig")]),
    ns("Hilke", HX2, BODEN, "bank", NFARBE["HI"], d=0.2),
    *fl("MA", MX2, [("frag", "ruhig")], bis="ma1", erst="pop"),
    *redet("MA_redetfroh", MX2, BODEN, FH, "ma1", "netto"),
    *fl("MA", MX2, [("netto", "ruhig"), (beim("an", "nimmt"), "sorge")]),
    ns("Marlies", MX2, BODEN, "frag", NFARBE["MA"], d=0.1),
    blase("sprech", 660, 210, "se1", 760, 230, inhalt=["Den Kredit bekommen Sie,", "wenn jemand für Sie bürgt."], textsize=34,
          figur=("SE_redet_r", SX2, BODEN, FH), bis="frag"),
    blase("sprech", 560, 170, "hi1", 1340, 200, inhalt=["Marlies, bürgst du für mich?"], textsize=34,
          figur=("HI_redet_r", HX2, BODEN, FH), bis="ma1"),
    blase("sprech", 560, 170, "ma1", 1400, 200, inhalt=["Klar, für dich mache ich das."], textsize=34,
          figur=("MA_redetfroh", MX2, BODEN, FH), bis="netto"),
    pl("verdient netto 3.400 € im Monat", MX2, 300, beim("netto", "verdient"), fill=GRUEN, size=30, anker="m"),
    karte(470, 70, 820, 290, beim("urk", "Urkunde"), fill=WEISS, rund=10, schatten=6, rand=4),
    z("Bürgschaft", 505, 88, beim("urk", "Urkunde"), "ExtraBold", 36, rechts=1270),
    z("Ich bürge selbstschuldnerisch für den", 505, 145, beim("urk", "Ich"), size=34, rechts=1270),
    z("Kredit von Hilke über 15.000 Euro.", 505, 195, beim("urk", "Kredit"), size=34, rechts=1270),
    linienzug([(840, 335), (1240, 335)], UNT, breite=3),
    szene(z("Marlies", 900, 276, UNT, "ExtraBold", 40, rechts=1270), "133unterschrift*", 0.9, 0.0),
    ficon("tabler", "ballpen", MHX - 30, MHY + 30, 70, beim("urk", "eigenhändig"), fuell=GELB),
    pl("Bank nimmt an", SX2, 735, beim("an", "nimmt"), fill=GRUEN, size=30, anker="m"),
])

# A3 Fall: zwei Jahre später – die Bank verlangt Zahlung, die Frage ---------------------------------------------------------------
SX3, MX3, HX3 = 430, 1080, 1660
folie([("spaet", "Fall · Zwei Jahre später"), ("frage", "Fall · Die Frage")], [
    pl("Zwei Jahre später: Hilke zahlt nicht mehr", 70, 30, "spaet", fill=GELB, size=44, bis="frage"),
    boden("spaet"),
    *fl("HI", HX3, [("spaet", "sorge"), ("frage", "muede")], erst="pop"),
    ns("Hilke", HX3, BODEN, "spaet", NFARBE["HI"], d=0.1),
    ficon("tabler", "calendar", HX3, 360, 100, "spaet", fuell=WEISS),
    pl("Bank kündigt", HX3, 105, beim("kuend", "kündigt"), fill=WEISS, size=30, anker="m"),
    pl("offen: 9.000 €", HX3, 170, beim("kuend", "neuntausend"), fill=ROT, size=32, anker="m"),
    ficon("tabler", "building-bank", 150, 420, 120, "brief", fuell=BLAU),
    *fl("SE", SX3, [("brief", "ruhig_r")], bis="se2", erst="pop"),
    *redet("SE_redet_r", SX3, BODEN, FH, "se2", "ma2"),
    *fl("SE", SX3, [("ma2", "denkt_r"), ("frage", "ruhig_r")]),
    ns("Herr Seibold", SX3, BODEN, "brief", NFARBE["SE"], d=0.1),
    szene(ficon("tabler", "mail", 760, 600, 110, beim("brief", "wendet"), fuell=WEISS), "133brief*", 0.8, 0.0),
    *fl("MA", MX3, [("brief", "ruhig")], bis="ma2", erst="pop", d=0.1),
    *redet("MA_redet", MX3, BODEN, FH, "ma2", "frage"),
    *fl("MA", MX3, [("frage", "denkt")]),
    ns("Marlies", MX3, BODEN, "brief", NFARBE["MA"], d=0.2),
    blase("sprech", 700, 210, "se2", 660, 220, inhalt=["Bitte zahlen Sie die 9.000 €", "für Ihre Schwester."],
          textsize=34, figur=("SE_redet_r", SX3, BODEN, FH), bis="ma2"),
    blase("sprech", 640, 210, "ma2", 860, 215, inhalt=["Dann holen Sie sich das Geld", "doch erst bei Hilke!"],
          textsize=34, figur=("MA_redet", MX3, BODEN, FH), bis="frage"),
    pl("Muss Marlies zahlen?", 960, 40, "frage", fill=PINK, size=42, anker="m"),
    pl("Bekommt sie ihr Geld von Hilke zurück?", 900, 125, beim("frage2", "Und"), fill=WEISS, size=34, anker="m"),
])


# B Sachverhalt -------------------------------------------------------------------------------------------------------------------
def sachverhalt_133(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 205
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=35, zeilenabstand=1.30)
        els += e; y += 20
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=36))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_133("sv", [
    "Hilke will sich eine neue Küche kaufen und nimmt dafür bei einer Bank einen Kredit über 15.000 Euro auf; die Zinsen "
    "betragen 75 Euro im Monat. Herr Seibold von der Bank verlangt eine Bürgschaft.",
    "Hilke bittet ihre Schwester Marlies, für sie zu bürgen, und Marlies sagt zu. Marlies verdient netto 3.400 Euro im "
    "Monat. In der Bank unterschreibt sie eigenhändig eine Urkunde: „Ich bürge selbstschuldnerisch für den Kredit von "
    "Hilke über 15.000 Euro.“ Herr Seibold nimmt die Erklärung an.",
    "Zwei Jahre später zahlt Hilke die Raten nicht mehr. Die Bank kündigt den Kredit wirksam, 9.000 Euro sind offen. Sie "
    "verlangt das Geld von Marlies. Marlies meint, die Bank müsse es zuerst bei Hilke holen.",
], "Muss Marlies zahlen, und kann sie das Geld von Hilke zurückverlangen?")

# C Anspruch aus § 765 Abs. 1 (Wortlaut) und Aufbau ----------------------------------------------------------------------------------
W765 = ["„(1) Durch den Bürgschaftsvertrag verpflichtet sich der Bürge gegenüber",
        "dem Gläubiger eines Dritten, für die Erfüllung der Verbindlichkeit des",
        "Dritten einzustehen.“"]
w765, w765_y = wortlaut(80, 250, 1100, W765, "§ 765 Abs. 1 BGB", "w765", marken=[
    (1, "Gläubiger eines Dritten", beim("w765", "Gläubiger")),
    (2, "einzustehen", beim("w765", "einzustehen"))], size=32)
folie([("agl", "Anspruch · Bank gegen Marlies, § 765 Abs. 1 BGB"), ("aufbau", "Anspruch › Prüfungsaufbau")], rechts_frei([
    *tafel("agl", "Bank gegen Marlies: 9.000 €"),
    z("Anspruch aus § 765 Abs. 1 BGB", 110, 180, beim("agl", "Anspruch"), "Bold", 38),
    *w765,
    z("I. Anspruch entstanden?", 110, w765_y + 40, beim("aufbau", "entstanden"), "Bold", 38),
    z("II. nicht erloschen?", 110, w765_y + 100, beim("aufbau", "erloschen"), "Bold", 38),
    z("III. durchsetzbar?", 110, w765_y + 160, beim("aufbau", "durchsetzbar"), "Bold", 38),
    *requisit([("agl", ("tabler", "building-bank", 110, BLAU), "Anspruch", WEISS),
               ("w765", ("tabler", "file-certificate", 100, WEISS), "einstehen", WEISS),
               ("aufbau", ("tabler", "list-numbers", 100, GELB), None, None)]),
    *paar("agl", "SE", [("agl", "ruhig")], "MA", [("agl", "sorge"), ("aufbau", "denkt")]),
]))

# D1 I. 1. Bürgschaftsvertrag, § 766 (Wortlaut), § 126 Abs. 1, § 350 HGB ----------------------------------------------------------------
W766 = ["„Zur Gültigkeit des Bürgschaftsvertrags ist schriftliche Erteilung der",
        "Bürgschaftserklärung erforderlich. Die Erteilung der Bürgschafts-",
        "erklärung in elektronischer Form ist ausgeschlossen. …“"]
w766, w766_y = wortlaut(80, 300, 1100, W766, "§ 766 Satz 1 und 2 BGB", "w766", marken=[
    (0, "schriftliche Erteilung", beim("w766", "schriftliche")),
    (2, "in elektronischer Form ist ausgeschlossen", beim("nur", "elektronisch"))], size=32)
folie([("i1", "I. Entstanden › 1. Bürgschaftsvertrag"), ("w766", "1. Bürgschaftsvertrag › Schriftform, § 766 BGB"),
       ("hgb", "1. Bürgschaftsvertrag › Ausnahme, § 350 HGB")], rechts_frei([
    *tafel("i1", "I. Anspruch entstanden?"),
    z("1. wirksamer Bürgschaftsvertrag", 110, 180, beim("i1", "wirksamer"), "Bold", 38),
    *okz("Einigung: Marlies und die Bank", 235, "einig", size=36, x=160),
    *w766,
    z("nur die Erklärung von Marlies, nicht elektronisch", 110, w766_y + 28, "nur", "Bold", 36),
    *okz("eigenhändig unterschrieben, § 126 Abs. 1 BGB", w766_y + 92, beim("eigen", "eigenhändig"), size=36, x=160),
    *okz("Form gewahrt", w766_y + 152, beim("eigen", "gewahrt"), "Bold", 36, x=160),
    z("Ausnahme: Kaufmann, Handelsgeschäft, § 350 HGB", 110, w766_y + 235, "hgb", size=34),
    *requisit([("i1", ("tabler", "file-certificate", 100, WEISS), "Bürgschaftsvertrag", WEISS),
               ("w766", ("tabler", "signature", 110, WEISS), "schriftlich", GELB),
               ("hgb", ("tabler", "briefcase", 100, WEISS), "Kaufmann", WEISS)]),
    *paar("i1", "SE", [("i1", "ruhig"), ("hgb", "denkt")], "MA", [("i1", "ruhig"), ("eigen", "sorge")]),
]))

# D2 I. 2. keine Sittenwidrigkeit, § 138 Abs. 1 (BGH XI ZR 82/11 Rn. 9) ----------------------------------------------------------------
folie([("i2", "I. Entstanden › 2. keine Sittenwidrigkeit, § 138 Abs. 1 BGB"), ("s138", "2. Sittenwidrigkeit › im Fall")], rechts_frei([
    *tafel("i2", "2. Keine Sittenwidrigkeit, § 138 Abs. 1 BGB", size=44),
    z("krass überfordert, wenn nicht einmal die", 110, 185, "krass", "Bold", 36),
    z("laufenden Zinsen aus dem pfändbaren Teil", 160, 240, beim("krass", "laufenden"), size=36),
    z("von Einkommen und Vermögen tragbar", 160, 295, beim("krass", "Einkommens"), size=36),
    zit("BGH, Urt. v. 19.2.2013 – XI ZR 82/11, Rn. 9", 160, 352, beim("krass", "tragen")),
    z("+ persönlich besonders nahe: widerlegliche", 110, 425, "verm", "Bold", 36),
    z("Vermutung, emotionale Verbundenheit,", 160, 480, beim("verm", "widerleglich"), size=36),
    z("Bank hat sittlich anstößig ausgenutzt", 160, 535, beim("verm", "sittlich"), size=36),
    z("Marlies: 3.400 € netto, Zinsen 75 € im Monat", 110, 625, "s138", "Bold", 36),
    *neinz("keine krasse Überforderung", 690, beim("s138b", "Krass"), size=36, x=160),
    *okz("Bürgschaft wirksam", 750, beim("s138b", "wirksam"), "Bold", 36, x=160),
    *requisit([("i2", ("tabler", "scale", 110, WEISS), "Sittenwidrigkeit?", WEISS),
               ("s138", ("tabler", "wallet", 100, GRUEN), "3.400 € netto", GRUEN),
               (beim("s138", "Zinsen"), ("tabler", "coin-euro", 100, GELB), "75 € Zinsen", WEISS)]),
    *paar("i2", "MA", [("i2", "denkt"), ("s138b", "ruhig")], "HI", [("i2", "ruhig"), ("verm", "sorge")]),
]))

# D3 I. 3. Hauptschuld, § 767 Abs. 1 S. 1 (Wortlaut), II. nicht erloschen (BGH IX ZR 36/22 Rn. 20) ---------------------------------------
W767 = ["„Für die Verpflichtung des Bürgen ist der jeweilige Bestand der",
        "Hauptverbindlichkeit maßgebend. …“"]
w767, w767_y = wortlaut(80, 240, 1100, W767, "§ 767 Abs. 1 Satz 1 BGB", "akz", marken=[
    (0, "jeweilige Bestand", beim("akz", "jeweiligen"))], size=32)
folie([("i3", "I. Entstanden › 3. Hauptschuld, § 767 BGB"), ("ii", "II. Anspruch nicht erloschen")], rechts_frei([
    *tafel("i3", "Hauptschuld und Erlöschen"),
    z("3. Bestehen der Hauptschuld", 110, 180, "i3", "Bold", 38),
    *w767,
    z("Darlehen, § 488 Abs. 1 BGB: 9.000 € offen,", 110, w767_y + 28, "haupt", "Bold", 36),
    z("fällig nach der Kündigung", 160, w767_y + 83, beim("haupt", "fällig"), size=36),
    *okz("I. Anspruch entstanden", w767_y + 148, beim("haupt", "entstanden"), "Bold", 36, x=160),
    z("II. Anspruch nicht erloschen", 110, w767_y + 235, "ii", "Bold", 38),
    *okz("niemand hat gezahlt", w767_y + 295, beim("erl", "Niemand"), size=36, x=160),
    z("hätte Hilke gezahlt: Marlies frei", 160, w767_y + 355, beim("erl", "Hätte"), size=36),
    zit("BGH, Urt. v. 7.12.2023 – IX ZR 36/22, Rn. 20", 160, w767_y + 410, beim("erl", "Akzessorietät")),
    *requisit([("i3", ("tabler", "file-text", 100, WEISS), "Hauptschuld", WEISS),
               ("akz", ("tabler", "link", 100, GELB), "akzessorisch", GELB),
               ("haupt", ("tabler", "cash-banknote", 120, ROT), "9.000 € offen", ROT),
               ("ii", ("tabler", "receipt-euro", 100, WEISS), "nicht erloschen", WEISS)]),
    *paar("i3", "HI", [("i3", "sorge")], "MA", [("i3", "ruhig"), ("erl", "denkt")]),
]))

# D4 III. durchsetzbar: §§ 768, 770 ----------------------------------------------------------------------------------------------------
folie([("iii", "III. Durchsetzbar › §§ 768, 770 BGB")], rechts_frei([
    *tafel("iii", "III. Anspruch durchsetzbar?"),
    z("§ 768 BGB: Einreden der Hauptschuldnerin,", 110, 190, "p768", "Bold", 36),
    z("etwa die Verjährung", 160, 245, beim("p768", "Verjährung"), size=36),
    z("§ 770 BGB: Verweigerung, solange Hilke", 110, 330, "p770", "Bold", 36),
    z("anfechten oder die Bank aufrechnen kann", 160, 385, beim("p770", "anfechten"), size=36),
    *neinz("hier keine Anhaltspunkte", 470, beim("keine", "keine"), "Bold", 36, x=160),
    *requisit([("p768", ("tabler", "shield", 100, GRUEN), "Einreden", GRUEN),
               ("p770", ("tabler", "arrows-exchange", 110, WEISS), "anfechten, aufrechnen", WEISS),
               ("keine", ("tabler", "circle-x", 100, WEISS), "keine Anhaltspunkte", WEISS)]),
    *paar("iii", "MA", [("iii", "denkt"), ("keine", "sorge")], "HI", [("iii", "ruhig")]),
]))

# D5 § 771 S. 1 (Wortlaut), § 773 Abs. 1 Nr. 1 (Wortlaut) -------------------------------------------------------------------------------
W771 = ["„Der Bürge kann die Befriedigung des Gläubigers verweigern, solange nicht",
        "der Gläubiger eine Zwangsvollstreckung gegen den Hauptschuldner ohne",
        "Erfolg versucht hat (Einrede der Vorausklage). …“"]
w771, w771_y = wortlaut(80, 165, 1100, W771, "§ 771 Satz 1 BGB", "w771", marken=[
    (0, "verweigern", beim("w771", "verweigern")),
    (1, "Zwangsvollstreckung gegen den Hauptschuldner", beim("w771", "vollstrecken"))], size=30)
W773 = ["„(1) Die Einrede der Vorausklage ist ausgeschlossen:",
        "1. wenn der Bürge auf die Einrede verzichtet, insbesondere wenn er sich",
        "als Selbstschuldner verbürgt hat, …“"]
w773, w773_y = wortlaut(80, w771_y + 22, 1100, W773, "§ 773 Abs. 1 Nr. 1 BGB", "w773", marken=[
    (1, "verzichtet", beim("w773", "Verzicht")),
    (2, "als Selbstschuldner verbürgt", beim("w773", "Selbstschuldner"))], size=30)
folie([("w771", "III. Durchsetzbar › Einrede der Vorausklage, § 771 BGB"),
       ("w773", "III. Durchsetzbar › Ausschluss, § 773 Abs. 1 Nr. 1 BGB")], rechts_frei([
    *tafel("w771", "Einrede der Vorausklage"),
    *w771, *w773,
    *okz("Marlies hat „selbstschuldnerisch“ unterschrieben", w773_y + 30, "s773", "Bold", 34, x=160),
    *neinz("Bank muss nicht erst bei Hilke vollstrecken", w773_y + 92, beim("s773", "Bank"), size=34, x=160),
    *requisit([("w771", ("tabler", "gavel", 100, WEISS), "Vorausklage?", WEISS),
               ("w773", ("tabler", "ballpen", 100, GELB), "Selbstschuldner", GELB),
               ("s773", ("tabler", "file-certificate", 100, WEISS), "unterschrieben", GRUEN)]),
    *paar("w771", "MA", [("w771", "denkt"), ("s773", "sorge")], "SE", [("w771", "ruhig")]),
]))

# E Ergebnis (Bühne) --------------------------------------------------------------------------------------------------------------------
SX9, MX9, HX9 = 470, 1120, 1660
folie([("erg", "Ergebnis · Marlies muss 9.000 € zahlen")], [
    blk(80, 40, 1760, 100, GRUEN, "erg", [("Ergebnis: Marlies muss der Bank 9.000 € zahlen", "ExtraBold", 42, INK)]),
    boden("erg"),
    ficon("tabler", "building-bank", 170, 420, 130, "erg", fuell=BLAU),
    *fl("SE", SX9, [("erg", "ruhig_r")], erst="pop"),
    ns("Herr Seibold", SX9, BODEN, "erg", NFARBE["SE"], d=0.1),
    *fl("MA", MX9, [("erg", "sorge")], erst="pop", d=0.1),
    ns("Marlies", MX9, BODEN, "erg", NFARBE["MA"], d=0.2),
    *fl("HI", HX9, [("erg", "muede")], erst="pop", d=0.2),
    ns("Hilke", HX9, BODEN, "erg", NFARBE["HI"], d=0.3),
    ficon("tabler", "cash-banknote", 800, 520, 150, beim("erg", "neuntausend"), fuell=GRUEN),
    pfeil(930, 600, 680, 600, beim("erg", "neuntausend"), breite=10, kopf=30),
    pl("9.000 €", 800, 330, beim("erg", "neuntausend"), fill=GELB, size=34, anker="m"),
])

# F IV. Rückgriff: § 774 Abs. 1 S. 1 (Wortlaut), Auftrag § 670 (BGH XI ZR 362/15 Rn. 20, 21) -------------------------------------------
W774 = ["„Soweit der Bürge den Gläubiger befriedigt, geht die Forderung des",
        "Gläubigers gegen den Hauptschuldner auf ihn über. …“"]
w774, w774_y = wortlaut(80, 175, 1100, W774, "§ 774 Abs. 1 Satz 1 BGB", "w774", marken=[
    (0, "geht die Forderung des", beim("w774", "Forderung")),
    (1, "auf ihn über", beim("w774", "über"))], size=32)
folie([("iv", "IV. Rückgriff › § 774 Abs. 1 Satz 1 BGB"), ("p670", "IV. Rückgriff › Auftrag, § 670 BGB"),
       ("risiko", "IV. Rückgriff › Risiko")], rechts_frei([
    *tafel("iv", "IV. Rückgriff nach der Zahlung"),
    *w774,
    z("gesetzlicher Forderungsübergang, wie § 426 Abs. 2 BGB", 110, w774_y + 30, "legal", "Bold", 34),
    z("Auftrag: Hilke bat Marlies um die Bürgschaft", 110, w774_y + 110, beim("p670", "Auftrag"), "Bold", 36),
    z("Ersatz nach § 670 BGB", 160, w774_y + 165, beim("p670", "sechshundertsiebzig"), size=36),
    z("beide Wege, das Geld aber nur einmal", 110, w774_y + 245, "wahl", "Bold", 36),
    zit("BGH, Urt. v. 24.10.2017 – XI ZR 362/15, Rn. 20", 160, w774_y + 300, beim("wahl", "Bundesgerichtshof")),
    z("bürgende Person trägt das Insolvenzrisiko", 110, w774_y + 380, beim("risiko", "bürgende"), "Bold", 36),
    zit("BGH, Urt. v. 24.10.2017 – XI ZR 362/15, Rn. 21", 160, w774_y + 435, beim("risiko", "Insolvenzrisiko")),
    *requisit([("iv", ("tabler", "arrow-back-up", 110, WEISS), "Forderung geht über", WEISS),
               ("p670", ("tabler", "file-text", 100, WEISS), "Auftrag", GELB),
               ("risiko", ("tabler", "alert-triangle", 100, GELB), "Kann Hilke zahlen?", WEISS)]),
    *paar("iv", "MA", [("iv", "denkt"), ("p670", "ruhig"), ("risiko", "sorge")], "HI", [("iv", "sorge"), ("risiko", "muede")]),
]))

# G Klausurtipp (Lexi) ---------------------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · selbstschuldnerisch ist keine Gesamtschuld")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("1. selbstschuldnerisch heißt nur:", 200, 200, beim("tipp", "Selbstschuldnerisch"), "Bold", 36),
    z("Einrede der Vorausklage fehlt", 250, 255, beim("tipp", "Einrede"), size=36),
    z("2. trotzdem keine Gesamtschuld", 200, 340, "tipp2", "Bold", 36),
    zit("BGH, Urt. v. 7.12.2023 – IX ZR 36/22, Rn. 17", 250, 395, beim("tipp2", "Gesamtschuldner")),
    z("3. Hauptschuld und § 768 BGB prüfen", 200, 475, "tipp3", "Bold", 36),
    z("4. Rückgriff: § 774 BGB und Auftrag", 200, 560, "tipp4", "Bold", 36),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# H Klausurschema ---------------------------------------------------------------------------------------------------------------------
K1, K2 = 150, 230
folie([("sch", "Klausurschema"), ("k2", "Klausurschema › II. nicht erloschen"), ("k3", "Klausurschema › III. durchsetzbar"),
       ("k4", "Klausurschema › IV. Rückgriff")], [
    karte(60, 50, 1800, 900, "sch"),
    titel(glyphen("Klausurschema: Anspruch aus § 765 Abs. 1 BGB"), 110, 90, "sch", 46),
    z("I. Anspruch entstanden", K1, 190, "k1", "Bold", 40, rechts=1820),
    z("1. wirksamer Bürgschaftsvertrag, Schriftform (§ 766 S. 1 BGB; § 350 HGB)", K2, 250, "k1a", size=34, rechts=1820),
    z("2. keine Sittenwidrigkeit (§ 138 Abs. 1 BGB)", K2, 302, "k1b", size=34, rechts=1820),
    z("3. Bestehen der Hauptschuld (§ 767 Abs. 1 S. 1 BGB)", K2, 354, "k1c", size=34, rechts=1820),
    z("II. Anspruch nicht erloschen", K1, 430, "k2", "Bold", 40, rechts=1820),
    z("III. Anspruch durchsetzbar", K1, 510, "k3", "Bold", 40, rechts=1820),
    z("keine Einreden, §§ 768, 770, 771 BGB", K2, 570, "k3a", size=34, rechts=1820),
    z("Ausschluss der Vorausklage, § 773 Abs. 1 BGB", K2, 622, "k3b", size=34, rechts=1820),
    z("IV. Rückgriff nach der Zahlung: § 774 Abs. 1 S. 1 BGB, § 670 BGB", K1, 700, "k4", "Bold", 40, rechts=1820),
])

# I Merksatz (Lexi) ---------------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 175, "merke", 84, anker="m"),
    *markertext([[("Wer bürgt, steht für eine ", 0), ("fremde Schuld", "a"), (" ein,", 0)]],
                750, 300, 42, "merke", {"a": beim("merke", "fremde")}),
    *markertext([[("schriftlich", "b"), (" und ", 0), ("akzessorisch", "c"), (".", 0)]],
                750, 360, 42, "m2", {"b": beim("m2", "schriftlich"), "c": beim("m2", "akzessorisch")}),
    *markertext([[("Wer ", 0), ("selbstschuldnerisch", "d"), (" bürgt, kann die Bank", 0)],
                 [("nicht erst zur Schuldnerin schicken.", 0)]],
                750, 460, 42, "m3", {"d": beim("m3", "selbstschuldnerisch")}),
    *markertext([[("Nach der Zahlung holt man sich das Geld", 0)], [("über ", 0), ("§ 774 BGB", "e"), (" zurück, wenn die", 0)],
                 [("Schuldnerin zahlen kann.", 0)]],
                750, 600, 42, "m4", {"e": beim("m4", "siebenhundertvierundsiebzig")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
