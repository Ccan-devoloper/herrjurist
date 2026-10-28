"""Folge 067 · § 823 I BGB Schema: Radfahrer rammt dich – was musst du beweisen? – Serienstandard Open Peeps (Katzenkönig).
Beispielfall (Plan-Hook „Ein Radfahrer rammt dich auf dem Gehweg“): Martina geht auf dem Gehweg an der Bäckerei von Erwin
vorbei; Stefan fährt zügig mit dem Rad über den Gehweg, streift sie, Martina stürzt (Handgelenk verstaucht, Brille
zerbrochen – keine Wunden). Stefan: „Sie sind mir doch vor das Rad gelaufen!“; Erwin (Zeuge): „Sie waren viel zu schnell!“
Szenen laut ../SZENENPLAN.md: A1 Gehweg vor der Bäckerei, A2 Forderung und Frage, B Sachverhalt, C § 823 I (Wortlaut) und
Beweislast, D1 I. Rechtsgutsverletzung/Handlung, D2 haftungsbegründende Kausalität und § 286 ZPO, E II. Rechtswidrigkeit,
F1 III. Deliktsfähigkeit, F2 Fahrlässigkeit und Beweislast, G1 Abwandlung (Wortlaut § 828 II 1, III), G2 Abwandlung
(Beweislast, Altersgruppe, § 829), H IV. Schaden und § 287 ZPO, I V. Rechtsfolge, Mitverschulden, Ergebnis, J Klausurtipp
(Lexi), K Klausurschema, L Merksatz (Lexi).
Ein Handlungsgeräusch (Sturz, siehe ../geraeusche_herkunft.json). Namensschild jeder Figur, solange sie im Bild ist.
Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns als eigene Kopie aus Folge 063 (gemeinsame Dateien
unverändert). Zahlen auf Tafeln, Pillen und Blasen als Ziffern, im Sprechtext als Wörter."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_067/"

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
    return (cue, round(DAUER - T_(cue) + 0.5, 3))       # Lexi bleibt bis zum letzten Frame (Befund Folge 063)


def zit(text, x, y, cue, size=26):
    """Fundstellenzeile (grau, klein)."""
    return z(text, x, y, cue, size=size, farbe=TEXT)


def rechts_frei(els, x0=1250):
    """Figuren und Requisiten der Tafelfolien stehen rechts der Tafel."""
    for e in els:
        n = e.name or ""
        if n.startswith(("bild:", "ficon:")) or "/op_067/" in n:
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



BODEN, FH = 860, 480
X1, X2 = 1420, 1720                         # zwei Figuren neben der Tafel: Martina links, Stefan rechts
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
MT_F, ST_F, EW_F = LILA, ORANGE, GELB       # Farben der Namensschilder
PX, PY, PU = 1570, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
RAD_H, BODEN_H = 360, 300                   # Höhe Radfahrer-Pose, Höhe Martina am Boden


def boden(cue, hart_=False):
    e = linienzug([(40, BODEN), (1880, BODEN)], cue, breite=7, farbe=INK)
    return hart(e) if hart_ else e


def martina(cx, unten, hoehe, folge, **k):
    return fig("MT", cx, unten, hoehe, folge, **k)


def stefan(cx, unten, hoehe, folge, **k):
    return fig("ST", cx, unten, hoehe, folge, **k)


def erwin(cx, unten, hoehe, folge, **k):
    return fig("EW", cx, unten, hoehe, folge, **k)


def paar(c0, mt_folge, st_folge):
    """Tafelszene: Martina links (X1), Stefan rechts (X2), beide blicken zur Tafel."""
    return [*martina(X1, FB, FR, mt_folge), ns("Martina", X1, FB, c0, MT_F),
            *stefan(X2, FB, FR, st_folge, d=0.2), ns("Stefan", X2, FB, c0, ST_F, d=0.2)]


def nur_martina(c0, folge):
    return [*martina(FX, FB, FR, folge), ns("Martina", FX, FB, c0, MT_F)]


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


SCALE = ("tabler", "scale", 130, WEISS)
BRILLE = ("tabler", "eyeglass-off", 130, WEISS)
RAD = ("tabler", "bike", 150, WEISS)

# A1 Fall: Gehweg vor der Bäckerei ----------------------------------------------------------------------------------------
EX, MX, SX0, SX1 = 440, 930, 1660, 1340     # Erwin, Martina, Stefan (Start/Ende der Fahrt)
SST = 1470                                   # Stefan steht (nach dem Absteigen)
folie([(NULL, "Fall · Auf dem Gehweg"), ("stoss", "Fall · Der Zusammenstoß"), ("mt1", "Fall · Wer sagt was?")], [
    hart(pl("Auf dem Gehweg vor der Bäckerei", 70, 40, NULL, fill=GELB, size=44)),
    hart(boden(NULL)),
    hart(ficon("tabler", "building-store", 210, BODEN, 260, NULL, fuell=GELB)),
    hart(ficon("tabler", "baguette", 210, BODEN - 300, 110, NULL, fuell=GELB)),
    *erwin(EX, BODEN, FH, [(NULL, "ruhig_r"), ("stoss", "schaut_r")], bis="er1", erst="cut"),
    *redet("EW_redet_r", EX, BODEN, FH, "er1", "ford"),
    hart(ns("Erwin, Bäcker", EX, BODEN, NULL, EW_F)),
    *martina(MX, BODEN, FH, [(NULL, "geht_r")], bis="stoss", erst="cut"),
    szene(peep_voll("MT_boden_r", MX, BODEN, BODEN_H, "stoss", anim="cut", bis="mt1"), "067sturz*", 0.7, -0.03),
    *redet("MT_boden_redet_r", MX, BODEN, BODEN_H, "mt1", "st1"),
    peep_voll("MT_boden_r", MX, BODEN, BODEN_H, "st1", anim="cut"),
    hart(ns("Martina, Fußgängerin", MX, BODEN, NULL, MT_F)),
    bewegt(peep_voll("ST_faehrt", SX1, BODEN, RAD_H, "rad", anim="cut", bis="stoss"), "rad", ("stoss", -0.05), SX0 - SX1),
    peep_voll("ST_rad_schreck", SX1, BODEN, RAD_H, "stoss", anim="cut", bis="st1"),
    bewegt(bis_(ns("Stefan, Radfahrer", SX1, BODEN, "rad", ST_F), "st1"), "rad", ("stoss", -0.05), SX0 - SX1),
    ficon("tabler", "bike", 1740, BODEN, 260, "st1", anim="cut"),
    *redet("ST_redet", SST, BODEN, FH, "st1", "er1"),
    *stefan(SST, BODEN, FH, [("er1", "ertappt")], erst="cut"),
    ns("Stefan, Radfahrer", SST, BODEN, "st1", ST_F),
    pl("zügig auf dem Gehweg", 1500, 420, beim("rad", "zügig"), fill=WEISS, size=30, anker="m", bis="stoss"),
    ficon("fluent-emoji-high-contrast", "collision", 1110, 640, 110, "stoss", bis="mt1"),
    pl("Handgelenk verstaucht", MX, 470, beim("folge", "Handgelenk"), fill=ORANGE, size=30, anker="m", bis="mt1"),
    ficon("tabler", "eyeglass-off", 680, BODEN, 90, beim("folge", "Brille"), fuell=WEISS),
    pl("Brille zerbrochen", 690, 700, beim("folge", "Brille"), fill=ORANGE, size=28, anker="m", bis="mt1"),
    blase("sprech", 640, 220, "mt1", 960, 300, inhalt=["Mein Handgelenk! Und", "meine Brille ist kaputt!"], textsize=36,
          figur=("MT_boden_redet_r", MX, BODEN, BODEN_H), bis="st1"),
    blase("sprech", 600, 220, "st1", 1420, 230, inhalt=["Sie sind mir doch vor", "das Rad gelaufen!"], textsize=36,
          figur=("ST_redet", SST, BODEN, FH), bis="er1"),
    blase("sprech", 660, 220, "er1", 700, 230, inhalt=["Nein, ich habe alles gesehen.", "Sie waren viel zu schnell!"],
          textsize=36, figur=("EW_redet_r", EX, BODEN, FH), bis="ford"),
])

# A2 Fall: Forderung und Frage ---------------------------------------------------------------------------------------------
AMX, ASX = 330, 1590
folie([("ford", "Fall · Die Forderung"), ("frage", "Fall · Die Frage")], [
    pl("Was Martina verlangt", 70, 40, "ford", fill=GELB, size=44),
    boden("ford"),
    *martina(AMX, BODEN, FH, [("ford", "sorge_r"), ("frage", "denkt_r")]),
    ns("Martina", AMX, BODEN, "ford", MT_F),
    *stefan(ASX, BODEN, FH, [("ford", "denkt"), ("frage2", "sorge")], d=0.2),
    ns("Stefan", ASX, BODEN, "ford", ST_F, d=0.2),
    ficon("tabler", "eyeglass", 700, 250, 110, beim("ford", "dreihundert"), fuell=WEISS),
    pl("300 € für eine neue Brille", 780, 190, beim("ford", "dreihundert"), fill=WEISS, size=34),
    ficon("tabler", "first-aid-kit", 700, 370, 100, beim("ford", "Behandlungskosten"), fuell=WEISS),
    pl("Behandlungskosten", 780, 310, beim("ford", "Behandlungskosten"), fill=WEISS, size=34),
    ficon("tabler", "coins", 700, 490, 100, beim("ford", "Schmerzensgeld"), fuell=GELB),
    pl("Schmerzensgeld", 780, 430, beim("ford", "Schmerzensgeld"), fill=WEISS, size=34),
    pl("Woraus kann Martina das verlangen?", 960, 590, "frage", fill=PINK, size=36, anker="m"),
    pl("Und was muss sie beweisen?", 960, 690, "frage2", fill=PINK, size=36, anker="m"),
])

# B Sachverhalt ------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Martina geht auf dem Gehweg an der Bäckerei von Erwin vorbei. Stefan fährt mit dem Fahrrad zügig mitten auf dem "
    "Gehweg, streift sie am Arm, und Martina stürzt. Ihr Handgelenk ist verstaucht, ihre Brille zerbrochen.",
    "Stefan sagt: „Sie sind mir doch vor das Rad gelaufen!“ Erwin hat alles gesehen: „Sie waren viel zu schnell!“ "
    "Martina verlangt 300 Euro für eine neue Brille, die Behandlungskosten und ein Schmerzensgeld.",
], "Woraus kann Martina das verlangen, und was muss sie beweisen?")

# C § 823 Abs. 1 BGB (Wortlaut) und Beweislast ----------------------------------------------------------------------------
W823 = ["„Wer vorsätzlich oder fahrlässig das Leben, den Körper, die",
        "Gesundheit, die Freiheit, das Eigentum oder ein sonstiges Recht",
        "eines anderen widerrechtlich verletzt, ist dem anderen zum Ersatz",
        "des daraus entstehenden Schadens verpflichtet.“"]
w823, w823_y = wortlaut(80, 170, 1100, W823, "§ 823 Abs. 1 BGB", "norm", marken=[
    (0, "vorsätzlich oder fahrlässig", beim("w823", "vorsätzlich")),
    (0, "den Körper", beim("w823", "Körper")), (1, "Gesundheit", beim("w823", "Gesundheit")),
    (1, "das Eigentum", beim("w823", "Eigentum")),
    (2, "widerrechtlich verletzt", beim("w823", "widerrechtlich")),
    (2, "zum Ersatz", beim("w823", "Ersatz")), (3, "des daraus entstehenden Schadens", beim("w823", "Ersatz"))], size=32)
folie([("norm", "Anspruchsgrundlage · § 823 Abs. 1 BGB › Wortlaut"), ("bew", "Beweislast · der rote Faden")], rechts_frei([
    *tafel("norm", "Anspruchsgrundlage: § 823 Abs. 1 BGB"),
    *w823,
    z("Der rote Faden: Wer muss was beweisen?", 110, w823_y + 40, "bew", "Bold", 36),
    blk(110, w823_y + 110, 1040, 100, BLAU, beim("bew", "Anspruchsteller"),
        [("Anspruchsteller: Tatsachen, die den Anspruch begründen", "ExtraBold", 32, INK)]),
    blk(110, w823_y + 240, 1040, 100, GELB, "bew2", [("Schädiger: Einwendungen", "ExtraBold", 34, INK)]),
    *requisit([("norm", SCALE, "§ 823 Abs. 1 BGB", GELB), ("bew", None, None, None)]),
    pl("Anspruchsteller", X1, 330, beim("bew", "Anspruchsteller"), fill=BLAU, size=28, anker="m"),
    pl("Schädiger", X2, 400, "bew2", fill=GELB, size=28, anker="m"),
    *paar("norm", [("norm", "ruhig"), ("bew", "denkt")], [("norm", "ruhig"), ("bew2", "denkt")]),
]))

# D1 I. Tatbestand: Rechtsgutsverletzung, Verletzungshandlung --------------------------------------------------------------
folie([("tb", "I. Tatbestand"), ("rg", "I. Tatbestand › 1. Rechtsgutsverletzung"),
       ("hd", "I. Tatbestand › 2. Verletzungshandlung")], rechts_frei([
    *tafel("tb", "I. Tatbestand"),
    z("1. Rechtsgutsverletzung", 110, 190, "rg", "Bold", 36),
    z("Handgelenk verstaucht: Körper und Gesundheit", 160, 250, beim("rg", "verstauchte"), size=34),
    ok(130, 270, beim("rg", "Gesundheit"), gr=20),
    z("Brille zerbrochen: Eigentum", 160, 310, "rg2", size=34),
    ok(130, 330, beim("rg2", "Eigentum"), gr=20),
    z("2. Verletzungshandlung", 110, 420, "hd", "Bold", 36),
    z("Stefan fährt Martina an: ein aktives Tun", 160, 480, beim("hd", "Stefan"), size=34),
    ok(130, 500, beim("hd", "aktives"), gr=20),
    *requisit([("tb", None, "Tatbestand", WEISS), ("rg", ("tabler", "bandage", 120, WEISS), "Körper, Gesundheit", ORANGE),
               ("rg2", BRILLE, "Eigentum", GELB), ("hd", RAD, "aktives Tun", WEISS)]),
    *paar("tb", [("tb", "ruhig"), ("rg", "sorge"), ("hd", "denkt")], [("tb", "ruhig"), ("hd", "sorge")]),
]))

# D2 I.3 Haftungsbegründende Kausalität und Beweismaß ----------------------------------------------------------------------
folie([("ks", "I. Tatbestand › 3. haftungsbegründende Kausalität"),
       ("kbew", "I. Tatbestand › Beweis: volle Überzeugung, § 286 ZPO")], rechts_frei([
    *tafel("ks", "3. Haftungsbegründende Kausalität"),
    z("zwischen Handlung und Rechtsgutsverletzung", 110, 175, beim("ks", "zwischen"), size=34),
    z("Äquivalenz: nicht hinwegzudenken", 110, 245, "aeq", "Bold", 34),
    z("Adäquanz: nicht nur ganz unwahrscheinlich", 110, 305, "adq", "Bold", 34),
    zit("BGH, Urt. v. 8.12.2020 – VI ZR 19/20, Rn. 23", 150, 355, "adq"),
    z("Schutzzweck: Gefahr, vor der die Norm schützt", 110, 405, "szw", "Bold", 34),
    zit("BGH, Urt. v. 8.12.2020 – VI ZR 19/20, Rn. 11", 150, 455, "szw"),
    ok(140, 530, "ksub", gr=22),
    z("Ohne Zusammenstoß kein Sturz: typische Folge", 185, 510, "ksub", size=34),
    blk(110, 590, 1040, 100, BLAU, "kbew", [("Martina beweist voll: § 286 ZPO", "ExtraBold", 36, INK)]),
    zit("BGH, Urt. v. 23.6.2020 – VI ZR 435/19, Rn. 13", 110, 705, "kbew"),
    z("Zeuge des Zusammenstoßes: Erwin", 110, 770, "kzeu", "Bold", 34),
    *requisit([("ks", RAD, "Handlung", WEISS), (beim("ks", "Verletzung"), ("tabler", "bandage", 120, WEISS), "Verletzung", ORANGE),
               ("aeq", ("tabler", "link", 120, WEISS), "Äquivalenz", WEISS),
               ("adq", ("tabler", "zoom-question", 120, WEISS), "Adäquanz", WEISS),
               ("szw", ("tabler", "shield-check", 120, GRUEN), "Schutzzweck", GRUEN),
               ("kbew", SCALE, "volle Überzeugung", BLAU), ("kzeu", ("tabler", "eye", 120, WEISS), "Zeuge Erwin", GELB)]),
    *paar("ks", [("ks", "ruhig"), ("kbew", "denkt"), ("kzeu", "froh")], [("ks", "denkt"), ("kzeu", "sorge")]),
]))

# E II. Rechtswidrigkeit ---------------------------------------------------------------------------------------------------
folie([("rw", "II. Rechtswidrigkeit › indiziert")], rechts_frei([
    *tafel("rw", "II. Rechtswidrigkeit"),
    z("Unmittelbare Verletzung:", 110, 190, beim("rw", "Bei"), "Bold", 36),
    z("Rechtswidrigkeit indiziert (h. M.)", 160, 250, beim("rw", "indiziert"), size=36),
    z("Rechtfertigungsgrund, etwa Notwehr?", 110, 360, "rw2", "Bold", 36),
    nein(140, 440, beim("rw2", "hat"), gr=20),
    z("Stefan hat keinen", 185, 420, beim("rw2", "hat"), size=36),
    *requisit([("rw", ("tabler", "scale", 130, WEISS), "indiziert", GELB), ("rw2", ("tabler", "shield-x", 120, ROT), "keine Notwehr", ROT)]),
    *paar("rw", [("rw", "ruhig")], [("rw", "denkt"), ("rw2", "sorge")]),
]))

# F1 III. Verschulden: Deliktsfähigkeit ------------------------------------------------------------------------------------
folie([("vs", "III. Verschulden"), ("df", "III. Verschulden › 1. Deliktsfähigkeit, §§ 827, 828 BGB"),
       ("dfbew", "III. Verschulden › Ausschlussgründe: Beweislast beim Schädiger")], rechts_frei([
    *tafel("vs", "III. Verschulden"),
    z("1. Deliktsfähigkeit, §§ 827, 828 BGB", 110, 190, "df", "Bold", 36),
    z("Stefan: erwachsen, bei klarem Verstand", 160, 255, beim("df", "Stefan"), size=34),
    ok(130, 275, beim("df", "klarem"), gr=20),
    blk(110, 360, 1040, 100, GELB, "dfbew", [("Ausschlussgründe = Einwendungen", "ExtraBold", 36, INK)]),
    z("Ihre Voraussetzungen beweist der Schädiger", 110, 490, beim("dfbew", "Ihre"), "Bold", 34),
    zit("BGH, Urt. v. 9.7.2015 – III ZR 329/14, Rn. 15", 110, 545, beim("dfbew", "Ihre")),
    zit("BGH, Urt. v. 30.6.2009 – VI ZR 310/08, Rn. 10 (zu § 828 Abs. 2 BGB)", 110, 585, beim("dfbew", "Ihre")),
    *requisit([("vs", ("tabler", "brain", 120, WEISS), "Verschulden", WEISS), ("df", ("tabler", "user-check", 120, WEISS), "erwachsen", GRUEN),
               ("dfbew", SCALE, "Schädiger beweist", GELB)]),
    *paar("vs", [("vs", "ruhig"), ("dfbew", "denkt")], [("vs", "denkt"), ("df", "ruhig"), ("dfbew", "denkt")]),
]))

# F2 III. Verschulden: Fahrlässigkeit, Beweislast --------------------------------------------------------------------------
folie([("fl", "III. Verschulden › 2. Fahrlässigkeit, § 276 Abs. 2 BGB"), ("stvo", "III. Verschulden › Gehweg, § 2 Abs. 1, 5 StVO"),
       ("vbew", "III. Verschulden › keine Vermutung: Martina beweist")], rechts_frei([
    *tafel("fl", "III. Verschulden: Fahrlässigkeit"),
    z("2. Vorsatz oder Fahrlässigkeit", 110, 180, "fl", "Bold", 36),
    z("§ 276 Abs. 2 BGB: die im Verkehr erforderliche", 150, 240, beim("fl", "handelt"), size=32),
    z("Sorgfalt außer Acht gelassen", 150, 285, beim("fl", "Sorgfalt"), size=32),
    z("§ 2 Abs. 1 StVO: Fahrzeuge auf die Fahrbahn", 150, 350, "stvo", size=32),
    z("§ 2 Abs. 5 StVO: Gehweg grundsätzlich nur für Kinder", 150, 395, beim("stvo", "Gehweg"), size=32),
    ok(140, 480, beim("fsub", "fahrlässig"), gr=22),
    z("Stefan: auf dem Gehweg, viel zu schnell", 185, 460, "fsub", "Bold", 34),
    blk(110, 540, 1040, 100, LILA, "vbew", [("Nicht vermutet wie in § 280 Abs. 1 Satz 2 BGB", "ExtraBold", 34, INK)]),
    zit("vgl. BGH, Urt. v. 25.10.2013 – V ZR 230/12, Rn. 18", 110, 655, "vbew"),
    z("Martina beweist das Verschulden", 110, 710, beim("vbew", "Martina"), "Bold", 34),
    z("Zeuge: Erwin", 110, 765, "zeuge", "Bold", 34),
    *requisit([("fl", ("tabler", "brain", 120, WEISS), "Sorgfalt", WEISS), ("stvo", ("tabler", "road", 120, WEISS), "Fahrbahn", WEISS),
               (beim("stvo", "Gehweg"), RAD, "Gehweg nur Kinder", GELB), ("fsub", RAD, "zu schnell", ROT),
               ("vbew", SCALE, "Martina beweist", LILA), ("zeuge", ("tabler", "eye", 120, WEISS), "Zeuge Erwin", GELB)]),
    *paar("fl", [("fl", "ruhig"), ("vbew", "denkt"), ("zeuge", "froh")], [("fl", "denkt"), ("fsub", "ertappt")]),
]))

# G1 Abwandlung: neunjähriger Radfahrer, Wortlaut § 828 Abs. 2, 3 ----------------------------------------------------------
W828 = ["„(2) Wer das siebente, aber nicht das zehnte Lebensjahr vollendet hat,",
        "ist für den Schaden, den er bei einem Unfall mit einem Kraftfahrzeug,",
        "einer Schienenbahn oder einer Schwebebahn einem anderen zufügt,",
        "nicht verantwortlich. …",
        "(3) Wer das 18. Lebensjahr noch nicht vollendet hat, ist, sofern seine",
        "Verantwortlichkeit nicht nach Absatz 1 oder 2 ausgeschlossen ist, für den",
        "Schaden, den er einem anderen zufügt, nicht verantwortlich, wenn er bei",
        "der Begehung der schädigenden Handlung nicht die zur Erkenntnis der",
        "Verantwortlichkeit erforderliche Einsicht hat.“"]
w828, w828_y = wortlaut(80, 165, 1100, W828, "§ 828 Abs. 2 Satz 1, Abs. 3 BGB (Auszug)", "w828", marken=[
    (0, "das siebente, aber nicht das zehnte Lebensjahr", beim("w828", "sieben")),
    (1, "Unfall mit einem Kraftfahrzeug", beim("w828", "Unfall")),
    (2, "einer Schienenbahn oder einer Schwebebahn", beim("w828", "Schienenbahn")),
    (6, "nicht verantwortlich", beim("abs3", "verantwortlich")),
    (7, "nicht die zur Erkenntnis der", beim("abs3", "Erkenntnis")),
    (8, "Verantwortlichkeit erforderliche Einsicht", beim("abs3", "Einsicht"))], size=28)
folie([("abw", "Abwandlung · Radfahrer 9 Jahre"), ("w828", "Abwandlung › § 828 Abs. 2 BGB: nur Kraftfahrzeug, Schienen- oder Schwebebahn"),
       ("abs3", "Abwandlung › § 828 Abs. 3 BGB: Einsicht")], rechts_frei([
    *tafel("abw", "Abwandlung: Der Radfahrer ist 9 Jahre alt"),
    *w828,
    blk(110, w828_y + 25, 1040, 90, ROT, "kfz", [("Fahrrad ist kein Kraftfahrzeug: Abs. 2 greift nicht", "ExtraBold", 32, INK)]),
    ficon("fluent-emoji-high-contrast", "child", 1330, 560, 110, "abw"),
    ficon("tabler", "bike", 1330, 720, 150, "abw", fuell=WEISS),
    pl("9 Jahre", 1330, 745, "abw", fill=GELB, size=28, anker="m"),
    pl("Gehweg erlaubt, § 2 Abs. 5 StVO", 1570, 100, "abw2", fill=GRUEN, size=28, anker="m"),
    pl("besondere Rücksicht", 1570, 180, beim("abw2", "besondere"), fill=GELB, size=28, anker="m"),
    pl("Fahrrad: kein Kfz", 1570, 260, "kfz", fill=ROT, size=28, anker="m"),
    *nur_martina("abw", [("abw", "ruhig"), ("w828", "denkt"), ("kfz", "ernst")]),
]))

# G2 Abwandlung: Beweislast § 828 Abs. 3, Altersgruppe, § 829 --------------------------------------------------------------
folie([("abs3b", "Abwandlung › Einsicht vermutet: Beweislast beim Kind"), ("alt", "Abwandlung › Fahrlässigkeit nach Altersgruppe"),
       ("p829", "Abwandlung › Billigkeitshaftung, § 829 BGB")], rechts_frei([
    *tafel("abs3b", "Abwandlung: § 828 Abs. 3 BGB"),
    z("Die Einsicht wird vermutet", 110, 190, beim("abs3b", "Diese"), "Bold", 36),
    z("Ihr Fehlen muss das Kind beweisen", 110, 250, beim("abs3b", "Fehlen"), "Bold", 36),
    zit("BGH, Urt. v. 9.7.2015 – III ZR 329/14, Rn. 15", 110, 305, beim("abs3b", "Fehlen")),
    zit("BGH, Urt. v. 30.11.2004 – VI ZR 335/03, BGHZ 161, 180 (Gründe II. 2.)", 110, 345, beim("abs3b", "Fehlen")),
    z("Fahrlässigkeit: Maßstab sind Kinder seines Alters", 110, 430, "alt", "Bold", 34),
    zit("BGH, Urt. v. 30.11.2004 – VI ZR 335/03 (Gründe II. 3. a)", 110, 480, "alt"),
    blk(110, 560, 1040, 100, GELB, "p829", [("Ohne Verantwortlichkeit: ausnahmsweise § 829 BGB", "ExtraBold", 34, INK)]),
    z("Haftung aus Billigkeit", 110, 690, beim("p829", "Billigkeit"), size=34),
    ficon("fluent-emoji-high-contrast", "child", 1330, 560, 110, "abs3b"),
    ficon("tabler", "bike", 1330, 720, 150, "abs3b", fuell=WEISS),
    pl("9 Jahre", 1330, 745, "abs3b", fill=GELB, size=28, anker="m"),
    *requisit([("abs3b", ("tabler", "brain", 120, WEISS), "Einsicht vermutet", GELB),
               (beim("abs3b", "Fehlen"), SCALE, "Kind beweist", GELB),
               ("alt", ("tabler", "users", 120, WEISS), "gleiches Alter", WEISS),
               ("p829", SCALE, "Billigkeit", GELB)]),
    *nur_martina("abs3b", [("abs3b", "denkt"), ("alt", "ruhig"), ("p829", "denkt")]),
]))

# H IV. Schaden und haftungsausfüllende Kausalität ----------------------------------------------------------------------------
folie([("sd", "IV. Schaden und haftungsausfüllende Kausalität"), ("sdbew", "IV. Schaden › Beweis: § 287 ZPO")], rechts_frei([
    *tafel("sd", "IV. Schaden, haftungsausfüllende Kausalität", size=40),
    z("Schaden beruht auf der Verletzung:", 110, 190, "sd2", "Bold", 36),
    z("Behandlungskosten", 160, 255, beim("sd2", "Behandlungskosten"), size=36),
    ok(130, 275, beim("sd2", "Behandlungskosten"), gr=20),
    z("neue Brille", 160, 315, beim("sd2", "Brille"), size=36),
    ok(130, 335, beim("sd2", "Brille"), gr=20),
    blk(110, 410, 1040, 100, GRUEN, "sdbew", [("§ 287 ZPO: Beweiserleichterung", "ExtraBold", 36, INK)]),
    z("überwiegende Wahrscheinlichkeit kann genügen", 110, 540, beim("sdbew", "überwiegende"), "Bold", 34),
    zit("BGH, Urt. v. 23.6.2020 – VI ZR 435/19, Rn. 13", 110, 595, beim("sdbew", "überwiegende")),
    *requisit([("sd", ("tabler", "receipt", 110, WEISS), "Schaden", WEISS),
               (beim("sd2", "Behandlungskosten"), ("tabler", "first-aid-kit", 110, WEISS), "Behandlungskosten", WEISS),
               (beim("sd2", "Brille"), ("tabler", "eyeglass", 120, WEISS), "neue Brille", WEISS),
               ("sdbew", SCALE, "§ 287 ZPO", GRUEN)]),
    *paar("sd", [("sd", "ruhig"), ("sdbew", "froh")], [("sd", "denkt")]),
]))

# I V. Rechtsfolge, Mitverschulden, Ergebnis ---------------------------------------------------------------------------------
folie([("rf", "V. Rechtsfolge › §§ 249 ff. BGB"), ("rf2", "V. Rechtsfolge › Schmerzensgeld, § 253 Abs. 2 BGB"),
       ("mv", "V. Rechtsfolge › Mitverschulden, § 254 BGB"), ("erg", "Ergebnis")], rechts_frei([
    *tafel("rf", "V. Rechtsfolge, §§ 249 ff. BGB"),
    z("§ 249 Abs. 2 Satz 1 BGB: Geldbetrag statt Herstellung", 110, 180, "rf1", "Bold", 32),
    z("Heilbehandlungskosten", 160, 235, beim("rf1b", "Heilbehandlungskosten"), size=34),
    z("300 € für die Brille", 160, 285, beim("rf1b", "dreihundert"), size=34),
    z("§ 253 Abs. 2 BGB: Schmerzensgeld", 110, 360, "rf2", "Bold", 32),
    z("billige Entschädigung in Geld", 160, 410, beim("rf2", "billige"), size=34),
    z("§ 254 BGB: Mitverschulden kann kürzen", 110, 485, "mv", "Bold", 32),
    z("beweisen müsste es Stefan", 160, 535, beim("mv", "beweisen"), size=34),
    zit("BGH, Beschl. v. 1.7.2025 – VI ZR 357/24, Rn. 20", 160, 585, beim("mv", "beweisen")),
    blk(110, 650, 1040, 110, GRUEN, "erg", [("Stefan zahlt: Brille, Behandlungskosten,", "ExtraBold", 34, INK),
                                             ("Schmerzensgeld", "ExtraBold", 34, INK)]),
    *requisit([("rf", ("tabler", "receipt", 110, WEISS), "Rechtsfolge", WEISS),
               ("rf1", ("tabler", "cash-banknote", 150, GRUEN), "Geldbetrag", GRUEN),
               ("rf2", ("tabler", "coins", 120, GELB), "Schmerzensgeld", GELB),
               ("mv", ("tabler", "scale", 130, WEISS), "Mitverschulden?", WEISS),
               ("erg", ("tabler", "cash-banknote", 150, GRUEN), "Stefan zahlt", GRUEN)]),
    *paar("rf", [("rf", "ruhig"), ("mv", "denkt"), ("erg", "froh")], [("rf", "denkt"), ("mv", "ruhig"), ("erg", "sorge")]),
]))

# J Klausurtipp (Lexi) -------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · zwei Kausalitäten")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Trenne die beiden Kausalitäten:", 200, 200, beim("tipp", "Trenne"), "Bold", 36),
    z("1. haftungsbegründende Kausalität:", 150, 300, "tipp1", "Bold", 34),
    z("Handlung – Rechtsgutsverletzung", 185, 350, beim("tipp1", "verbindet"), size=34),
    z("Verschulden muss sich darauf beziehen", 185, 400, beim("tipp1", "Verschulden"), size=34),
    zit("BGH, Urt. v. 8.12.2020 – VI ZR 19/20, Rn. 25", 185, 450, beim("tipp1", "Verschulden")),
    z("2. haftungsausfüllende Kausalität:", 150, 520, "tipp2", "Bold", 34),
    z("Rechtsgutsverletzung – Schaden", 185, 570, beim("tipp2", "verbindet"), size=34),
    z("kein Verschulden nötig", 185, 620, beim("tipp2", "kein"), size=34),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# K Klausurschema ------------------------------------------------------------------------------------------------------------
K1, K2 = 150, 210
folie([("sch", "Klausurschema"), ("k4", "Klausurschema › Schaden und Rechtsfolge")], [
    karte(60, 50, 1800, 900, "sch"),
    titel(glyphen("Klausurschema: § 823 Abs. 1 BGB"), 110, 90, "sch", 44),
    z("I. Tatbestand", K1, 200, "k1", "Bold", 38, rechts=1820),
    z("Rechtsgutsverletzung, Verletzungshandlung, haftungsbegründende Kausalität", K2, 255,
      beim("k1", "Rechtsgutsverletzung"), size=32, rechts=1820),
    z("II. Rechtswidrigkeit", K1, 340, "k2", "Bold", 38, rechts=1820),
    z("III. Verschulden", K1, 425, "k3", "Bold", 38, rechts=1820),
    z("mit Deliktsfähigkeit, §§ 827, 828 BGB", K2, 480,
      beim("k3", "Deliktsfähigkeit"), size=32, rechts=1820),
    z("IV. Schaden und haftungsausfüllende Kausalität", K1, 565, "k4", "Bold", 38, rechts=1820),
    z("V. Rechtsfolge, §§ 249 ff. BGB", K1, 650, "k5", "Bold", 38, rechts=1820),
])

# L Merksatz (Lexi) ----------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Wer aus § 823 Abs. 1 BGB Schadensersatz will,", 0)],
                 [("beweist grundsätzlich alle anspruchsbegründenden", 0)],
                 [("Tatsachen, ", 0), ("auch das Verschulden", "a"), (".", 0)]],
                750, 300, 38, "merke", {"a": beim("merke", "Verschulden")}),
    *markertext([[("Die Ausschlussgründe der §§ 827, 828 BGB", 0)],
                 [("muss der Schädiger beweisen", "b"), (".", 0)]],
                750, 560, 40, "m2", {"b": beim("m2", "Schädiger")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
