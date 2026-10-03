"""Folge 103 · Einwendung und Einrede: Warum Verjährung den Anspruch nicht tötet – Serienstandard Open Peeps (Katzenkönig).
Beispielfall: Der Tischler Herr Grünwald restauriert im Herbst 2022 den alten Esstisch von Tilda; im Oktober 2022 holt sie
ihn zufrieden ab und erhält die Rechnung über 1.400 €, die in einer Schublade landet. Im September 2026 verlangt Herr
Grünwald das Geld.
Szenen laut ../SZENENPLAN.md: A1 Werkstatt, A2 Bei Tilda (Schublade, September 2026, Frage), B Sachverhalt, C Drei Stufen
(Treppe), D I. entstanden, E II. untergegangen, F1 III. durchsetzbar (§ 214 Abs. 1, Wortlaut), F2 Frist (Zeitstrahl),
F3 aufschiebende Einreden, G Wirkung im Prozess, H § 214 Abs. 2 (Wortlaut), I Ergebnis, J Klausurtipp (Lexi, § 215
Wortlaut), K Klausurschema (Treppe), L Merksatz (Lexi). Zwei Handlungsgeräusche (Rechnung wird übergeben, Schublade;
../geraeusche_herkunft.json).
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/hand als
eigene Kopie aus Folge 095 (gemeinsame Dateien unverändert). Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_103/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_103/" in n:
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
TI_N, GR_N = LILA, BLAU                     # Farben der Namensschilder
PX, PY, PU = 1570, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"TI": "Tilda", "GR": "Herr Grünwald"}
NFARBE = {"TI": TI_N, "GR": GR_N}


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
    """Tafelszene: zwei Figuren rechts der Tafel, beide blicken zur Tafel (nach links); l, r = Kürzel TI/GR."""
    return [*fig(l, X1, FB, FR, lf), ns(NAME[l], X1, FB, c0, NFARBE[l], d=0.1),
            *fig(r, X2, FB, FR, rf, d=0.2), ns(NAME[r], X2, FB, c0, NFARBE[r], d=0.3)]




HOLZ_ALT = (196, 178, 150, 255)             # stumpfes, verkratztes Holz vor der Restaurierung
HOLZ_NEU = (233, 170, 92, 255)              # frisch geöltes Holz
STUFE_F = {1: BLAU, 2: LILA, 3: GELB}       # Farben der drei Stufen (Treppe, Mini-Treppe, Schema)


def tisch(cx, unten, cue, w=520, h=230, alt=False, bis=None):
    """Esstisch in Seitenansicht (programmatisch: Platte, Zarge, zwei Beine; Palettenflächen, Tuschekontur).
    alt = stumpfes Holz mit Kratzern (vor der Restaurierung)."""
    s = 2
    im = Image.new("RGBA", ((w + 12) * s, (h + 12) * s))
    dr = ImageDraw.Draw(im)
    f = HOLZ_ALT if alt else HOLZ_NEU
    o = 6 * s
    dr.rounded_rectangle((o, o, o + w * s, o + 34 * s), 8 * s, fill=f, outline=INK, width=5 * s)            # Platte
    dr.rectangle((o + 40 * s, o + 30 * s, o + (w - 40) * s, o + 70 * s), fill=f, outline=INK, width=5 * s)  # Zarge
    for bx in (40, w - 80):                                                                                    # Beine
        dr.rectangle((o + bx * s, o + 66 * s, o + (bx + 40) * s, o + h * s), fill=f, outline=INK, width=5 * s)
    if alt:
        for x0, y0, x1, y1 in ((90, 14, 160, 22), (250, 10, 300, 24), (380, 16, 450, 12)):
            dr.line((o + x0 * s, o + y0 * s, o + x1 * s, o + y1 * s), fill=INK, width=3 * s)
        dr.line((o + 52 * s, o + 110 * s, o + 70 * s, o + 170 * s), fill=INK, width=3 * s)
    else:
        dr.line((o + 30 * s, o + 12 * s, o + (w - 30) * s, o + 12 * s), fill=(250, 214, 160, 255), width=4 * s)  # Glanz
    im = im.resize((w + 12, h + 12), Image.LANCZOS)
    return El(im, cx - w / 2 - 6, unten - h - 6, cue, "cut", 0.0, bis, name="tisch:" + ("alt" if alt else "neu"))


def kommode(x0, unten, cue, w=300, h=290):
    """Kommode mit drei Schubladen (programmatisch, Palettengelb, Tuschekontur, Griffe)."""
    s = 2
    im = Image.new("RGBA", ((w + 12) * s, (h + 12) * s))
    dr = ImageDraw.Draw(im)
    o = 6 * s
    dr.rounded_rectangle((o, o, o + w * s, o + (h - 24) * s), 10 * s, fill=GELB, outline=INK, width=5 * s)
    for k in range(3):
        y0 = 18 + k * ((h - 60) // 3)
        y1 = y0 + (h - 60) // 3 - 12
        dr.rounded_rectangle((o + 18 * s, o + y0 * s, o + (w - 18) * s, o + y1 * s), 6 * s, outline=INK, width=4 * s)
        gy = (y0 + y1) / 2
        dr.rounded_rectangle((o + (w / 2 - 30) * s, o + (gy - 5) * s, o + (w / 2 + 30) * s, o + (gy + 5) * s), 4 * s, fill=INK)
    for bx in (20, w - 44):
        dr.rectangle((o + bx * s, o + (h - 26) * s, o + (bx + 24) * s, o + h * s), fill=INK)
    im = im.resize((w + 12, h + 12), Image.LANCZOS)
    return El(im, x0 - 6, unten - h - 6, cue, "cut", 0.0, None, name="kommode")


def stufe(x, oben, w, unten, nr, cue, rund=16, schatten=6, aktiv=True):
    """Eine Stufe der Treppe (Karte in der Stufenfarbe, Tuschekontur)."""
    return karte(x, oben, w, unten - oben, cue, fill=STUFE_F[nr] if aktiv else WEISS, rund=rund, schatten=schatten,
                 rand=4 if schatten < 6 else 5)


def mini(aktiv, cue):
    """Mini-Treppe oben rechts auf der Tafel: zeigt, auf welcher der drei Stufen die Prüfung gerade steht."""
    els = []
    for k, hh in ((1, 34), (2, 62), (3, 90)):
        x = 975 + (k - 1) * 62
        els.append(stufe(x, 175 - hh, 56, 175, k, cue, rund=8, schatten=4, aktiv=(k == aktiv)))
    return els


# A1 Fall: in der Werkstatt, Herbst 2022 -------------------------------------------------------------------------------
TX = 430                                              # Tisch: Mitte
GRX, TIX = 1150, 1650                                 # Grünwald (blickt nach rechts zu Tilda), Tilda (blickt nach links)
REST = "rest"
GR_HAND = hand("GR_redet_r", GRX, BODEN, FH, +1)
TI_HAND = hand("TI_ruhig", TIX, BODEN, FH, -1)
RECH = beim("gr1", "Rechnung")
folie([(NULL, "Fall · In der Werkstatt")], [
    hart(pl("Herbst 2022", 70, 30, NULL, fill=GELB, size=44, bis="abh")),
    pl("Oktober 2022: Tilda holt den Tisch ab", 70, 30, "abh", fill=GELB, size=44),
    hart(boden(NULL)),
    # Werkzeugwand des Tischlers
    hart(karte(80, 340, 600, 170, NULL, fill=(226, 238, 250, 255), rund=14, schatten=6)),
    hart(ficon("tabler", "hammer", 180, 480, 100, NULL, fuell=WEISS)),
    hart(ficon("tabler", "ruler", 330, 485, 110, NULL, fuell=WEISS)),
    hart(ficon("tabler", "brush", 470, 485, 100, NULL, fuell=WEISS)),
    hart(ficon("tabler", "tool", 600, 480, 90, NULL, fuell=WEISS)),
    hart(tisch(TX, BODEN, NULL, alt=True, bis=REST)),
    tisch(TX, BODEN, REST),
    pl("Omas alter Esstisch", TX, 545, NULL, fill=WEISS, size=30, anker="m", bis=REST),
    pl("abschleifen", 70, 120, REST, fill=WEISS, size=30),
    pl("Beine neu leimen", 70, 190, beim("rest", "leimt"), fill=WEISS, size=30),
    pl("Holz ölen", 70, 260, beim("rest", "ölt"), fill=WEISS, size=30),
    # Herr Grünwald (links, blickt zu Tilda)
    *fig("GR", GRX, BODEN, FH, [(NULL, "ruhig_r"), (REST, "denkt_r"), ("abh", "froh_r")], bis="gr1", erst="cut"),
    hart(ns("Herr Grünwald", GRX, BODEN, NULL, GR_N)),
    *redet("GR_redet_r", GRX, BODEN, FH, "gr1", "schub"),
    blase("sprech", 700, 230, "gr1", 820, 230, inhalt=["Schön geworden, oder? Hier ist", "die Rechnung: 1.400 €."],
          textsize=36, figur=("GR_redet_r", GRX, BODEN, FH), bis="schub"),
    # die Rechnung wandert von Grünwald zu Tilda
    szene(bewegt(ficon("tabler", "receipt-euro", TI_HAND[0] - 10, TI_HAND[1] + 45, 80, RECH, fuell=WEISS),
                 RECH, (RECH[0], RECH[1] + 0.8), GR_HAND[0] - TI_HAND[0] + 20, GR_HAND[1] - TI_HAND[1]), "103rechnung*", 0.7, 0.0),
    pl("1.400 €", TIX, 290, beim("gr1", "tausendvierhundert"), fill=GELB, size=40, anker="m"),
    # Tilda (rechts, blickt zu Grünwald und zum Tisch)
    *fig("TI", TIX, BODEN, FH, [(NULL, "ruhig"), (REST, "staunt"), ("abh", "froh")], erst="cut"),
    hart(ns("Tilda", TIX, BODEN, NULL, TI_N)),
])

# A2 Fall: bei Tilda – Schublade, September 2026, die Frage ---------------------------------------------------------------
KX, KW = 90, 300                                      # Kommode links
SCHUB = (KX + KW // 2, BODEN - 290 + 18 + 40)         # Mitte der oberen Schublade
TI2_HAND = hand("TI_ruhig", TIX, BODEN, FH, -1)
UND = beim("schub", "Und")
SEPT = "sept"
folie([("schub", "Fall · Die Rechnung in der Schublade"), (SEPT, "Fall · September 2026"), ("frage", "Fall · Die Frage")], [
    pl("Bei Tilda zu Hause", 70, 30, "schub", fill=GELB, size=44, bis=SEPT),
    pl("Fast 4 Jahre später: September 2026", 70, 30, SEPT, fill=GELB, size=44),
    boden("schub"),
    kommode(KX, BODEN, "schub", w=KW),
    tisch(720, BODEN, "schub", w=440, h=210),
    # Tilda legt die Rechnung in die obere Schublade
    szene(bis_(bewegt(ficon("tabler", "receipt-euro", SCHUB[0], SCHUB[1] + 30, 70, "schub", fuell=WEISS),
                      ("schub", 0.3), ("schub", 1.4), TI2_HAND[0] - SCHUB[0], TI2_HAND[1] - SCHUB[1]), UND),
          "103schublade*", 0.8, 1.45),
    pl("vergessen", SCHUB[0], 470, beim("schub", "vergisst"), fill=WEISS, size=30, anker="m", bis=SEPT),
    ficon("tabler", "calendar-event", 960, 104, 72, SEPT, fuell=WEISS),
    pl("1.400 € offen", SCHUB[0], 470, beim("sept", "offene"), fill=ROT, size=32, anker="m"),
    # Tilda
    *fig("TI", TIX, BODEN, FH, [("schub", "ruhig"), (beim("sept", "kommt"), "staunt")], bis="ti1"),
    ns("Tilda", TIX, BODEN, "schub", TI_N, d=0.1),
    *redet("TI_redet", TIX, BODEN, FH, "ti1", "frage"),
    *fig("TI", TIX, BODEN, FH, [("frage", "sorge"), ("frage2", "denkt")], erst="cut"),
    # Herr Grünwald kommt vorbei
    *fig("GR", GRX, BODEN, FH, [(beim("sept", "kommt"), "ruhig_r")], bis="gr2"),
    ns("Herr Grünwald", GRX, BODEN, beim("sept", "kommt"), GR_N, d=0.1),
    *redet("GR_fordert_r", GRX, BODEN, FH, "gr2", "ti1"),
    *fig("GR", GRX, BODEN, FH, [("ti1", "denkt_r")], erst="cut"),
    blase("sprech", 640, 210, "gr2", 830, 230, inhalt=["Sie schulden mir noch", "1.400 € für den Tisch!"], textsize=36,
          figur=("GR_fordert_r", GRX, BODEN, FH), bis="ti1"),
    blase("sprech", 700, 260, "ti1", 1240, 215, inhalt=["Die Rechnung ist fast 4 Jahre", "alt. Muss ich die wirklich",
                                                    "noch zahlen?"], textsize=34,
          figur=("TI_redet", TIX, BODEN, FH), bis="frage"),
    pl("Muss Tilda zahlen?", 70, 130, "frage", fill=PINK, size=40),
    pl("Zahlt sie erst: Geld zurück?", 70, 225, "frage2", fill=WEISS, size=36),
])


# B Sachverhalt -------------------------------------------------------------------------------------------------------
def sachverhalt_103(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=35, zeilenabstand=1.32)
        els += e; y += 20
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=36))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_103("sv", [
    "Im Herbst 2022 lässt die 31-jährige Tilda den alten Esstisch ihrer Oma vom Tischler Herrn Grünwald restaurieren. "
    "Im Oktober 2022 holt sie den Tisch ab, ist zufrieden und erhält die Rechnung über 1.400 Euro. Sie legt die "
    "Rechnung in eine Schublade und vergisst sie.",
    "Im September 2026 findet Herr Grünwald die offene Rechnung und verlangt die 1.400 Euro. Tilda hat bisher nichts "
    "gezahlt. Die beiden haben nie über die Rechnung verhandelt, und Herr Grünwald hat weder geklagt noch einen "
    "Mahnbescheid beantragt.",
], "Muss Tilda zahlen – und bekommt sie gezahltes Geld zurück?")

# C Drei Stufen (Treppe) ------------------------------------------------------------------------------------------------
T_X, T_W, T_U = (110, 455, 800), 345, 880             # Treppe: linke Kanten, Breite, Unterkante
T_O = (640, 500, 360)                                 # Oberkanten der drei Stufen
folie([("drei", "Gegenrechte › Drei Stufen"), ("stufe", "Gegenrechte › Einwendungen und Einreden")], rechts_frei([
    *tafel("drei", "Drei Stufen der Prüfung"),
    z("Wogegen wehrt sich der Schuldner?", 110, 190, "drei", "Bold", 38),
    *[e for k, c in ((1, "st1"), (2, "st2"), (3, "st3")) for e in (
        stufe(T_X[k - 1], T_O[k - 1], T_W, T_U, k, c),
        z(("1. entstanden?", "2. untergegangen?", "3. durchsetzbar?")[k - 1], T_X[k - 1] + 20, T_O[k - 1] + 18, c, "ExtraBold",
          32, rechts=T_X[k - 1] + T_W - 10))],
    z("Zu jeder Stufe eigene Gegenrechte:", 110, 250, "stufe", size=34),
    *[e for k, c, a, b in ((1, "e1", "rechtshindernde", "Einwendungen"), (2, "e2", "rechtsvernichtende", "Einwendungen"),
                           (3, "e3", "rechtshemmende", "Einreden")) for e in (
        z(a, T_X[k - 1] + 20, T_O[k - 1] + 78, c, "Bold", 30, rechts=T_X[k - 1] + T_W - 10),
        z(b, T_X[k - 1] + 20, T_O[k - 1] + 120, c, "Bold", 30, rechts=T_X[k - 1] + T_W - 10))],
    *requisit([("drei", ("tabler", "stairs", 110, WEISS), "3 Stufen", WEISS),
               ("e1", ("tabler", "ban", 100, BLAU), "hindert", BLAU),
               ("e2", ("tabler", "trash", 100, LILA), "vernichtet", LILA),
               ("e3", ("tabler", "hand-stop", 100, GELB), "hemmt", GELB)]),
    *paar("drei", "TI", [("drei", "ruhig"), ("stufe", "denkt")], "GR", [("drei", "ruhig"), ("e3", "denkt")]),
]))

# D I. entstanden: rechtshindernde Einwendungen ---------------------------------------------------------------------------
folie([("i", "I. entstanden › rechtshindernde Einwendungen"), ("isub", "I. entstanden › der Fall")], rechts_frei([
    *tafel("i", "I. Anspruch entstanden?"), *mini(1, "i"),
    z("Rechtshindernde Einwendungen:", 110, 200, "i", "Bold", 38),
    z("Der Anspruch entsteht gar nicht erst.", 110, 255, beim("i", "gar"), size=34),
    z("§ 105 Abs. 1: Erklärung eines Geschäftsunfähigen", 150, 330, "h105", "Bold", 34),
    z("§ 125 Satz 1: Grundstückskauf ohne Notar", 150, 390, "h125", "Bold", 34),
    zit("i. V. m. § 311b Abs. 1 Satz 1 BGB", 200, 438, beim("h125", "Notar")),
    z("§ 134: Werkvertrag über Schwarzarbeit", 150, 488, "h134", "Bold", 34),
    zit("BGH, Urt. v. 1.8.2013 – VII ZR 6/13, Rn. 13", 200, 536, beim("h134", "Schwarzarbeit")),
    z("§ 138: Wuchergeschäft", 150, 586, "h138", "Bold", 34),
    linienzug([(110, 660), (1150, 660)], "isub", breite=3),
    *okz("volljährig, keine Form nötig, mit Rechnung", 685, "isub", "Bold", 34, x=160),
    blk(110, 765, 1040, 90, BLAU, "iok", [("Werklohn, § 631 Abs. 1 BGB: entstanden", "ExtraBold", 36, INK)]),
    *requisit([("i", ("tabler", "ban", 100, BLAU), "entsteht nicht", BLAU),
               ("h105", ("tabler", "user-x", 100, WEISS), "geschäftsunfähig", WEISS),
               ("h125", ("tabler", "signature", 110, WEISS), "Form fehlt", WEISS),
               ("h134", ("tabler", "receipt-off", 100, WEISS), "Schwarzarbeit", WEISS),
               ("h138", ("tabler", "coins", 100, ROT), "Wucher", ROT),
               ("isub", ("tabler", "user-check", 100, WEISS), "volljährig", WEISS),
               ("iok", ("tabler", "check", 100, GRUEN), "entstanden", GRUEN)]),
    *paar("i", "TI", [("i", "ruhig"), ("isub", "denkt")], "GR", [("i", "ruhig"), ("iok", "froh")]),
]))

# E II. untergegangen: rechtsvernichtende Einwendungen --------------------------------------------------------------------
folie([("ii", "II. untergegangen › rechtsvernichtende Einwendungen"), ("iisub", "II. untergegangen › der Fall")], rechts_frei([
    *tafel("ii", "II. Anspruch untergegangen?"), *mini(2, "ii"),
    z("Rechtsvernichtende Einwendungen:", 110, 200, "ii", "Bold", 38),
    z("Der entstandene Anspruch erlischt.", 110, 255, beim("ii", "lassen"), size=34),
    z("§ 362 Abs. 1: Erfüllung", 150, 335, "v362", "Bold", 34),
    z("§ 389: Aufrechnung", 150, 395, "v389", "Bold", 34),
    z("§ 142 Abs. 1: Anfechtung, rückwirkend nichtig", 150, 455, "v142", "Bold", 34),
    linienzug([(110, 535), (1150, 535)], "iisub", breite=3),
    *neinz("nichts gezahlt", 560, "iisub", "Bold", 34, x=160),
    *neinz("nicht aufgerechnet", 615, beim("iisub", "aufgerechnet"), "Bold", 34, x=160),
    *neinz("nicht angefochten", 670, beim("iisub", "angefochten"), "Bold", 34, x=160),
    blk(110, 755, 1040, 90, LILA, "iiok", [("Der Anspruch besteht noch", "ExtraBold", 38, INK)]),
    *requisit([("ii", ("tabler", "trash", 100, LILA), "erlischt", LILA),
               ("v362", ("tabler", "cash-banknote", 110, GRUEN), "Erfüllung", WEISS),
               ("v389", ("tabler", "arrows-exchange", 100, WEISS), "Aufrechnung", WEISS),
               ("v142", ("tabler", "arrow-back-up", 100, WEISS), "rückwirkend", WEISS),
               ("iisub", ("tabler", "receipt-euro", 90, WEISS), "1.400 € offen", ROT),
               ("iiok", ("tabler", "check", 100, GRUEN), "besteht", GRUEN)]),
    *paar("ii", "TI", [("ii", "ruhig"), ("iisub", "sorge")], "GR", [("ii", "ruhig"), ("iiok", "froh")]),
]))

# F1 III. durchsetzbar: Verjährung, § 214 Abs. 1 (Wortlaut) ---------------------------------------------------------------
W214A = ["„(1) Nach Eintritt der Verjährung ist der Schuldner berechtigt,",
         "die Leistung zu verweigern.“"]
w214a, w214a_y = wortlaut(80, 470, 1100, W214A, "§ 214 Abs. 1 BGB", "p214", marken=[
    (0, "berechtigt", beim("p214", "berechtigt")), (1, "die Leistung zu verweigern", beim("p214", "Leistung"))], size=34)
folie([("iii", "III. durchsetzbar › rechtshemmende Einreden"), ("p214", "III. durchsetzbar › Verjährung, § 214 Abs. 1 BGB")],
      rechts_frei([
    *tafel("iii", "III. Anspruch durchsetzbar?"), *mini(3, "iii"),
    z("Rechtshemmende Einreden:", 110, 200, "iii", "Bold", 38),
    z("Der Anspruch bleibt bestehen; der Schuldner", 110, 255, beim("iii", "lassen"), size=34),
    z("darf nur die Leistung verweigern.", 160, 305, beim("iii", "Sie"), size=34),
    blk(110, 375, 1040, 76, GELB, "dauer", [("Dauernde Einrede: Verjährung", "ExtraBold", 36, INK)]),
    *w214a,
    *requisit([("iii", ("tabler", "hand-stop", 100, GELB), "verweigern", GELB),
               ("dauer", ("tabler", "hourglass", 90, WEISS), "Verjährung", WEISS),
               ("p214", ("tabler", "lock", 90, WEISS), "dauernd", WEISS)]),
    *paar("iii", "TI", [("iii", "ruhig"), ("dauer", "staunt"), (beim("p214", "verweigern"), "froh")],
          "GR", [("iii", "ruhig"), ("dauer", "sorge")]),
]))

# F2 Die Frist (Zeitstrahl) -------------------------------------------------------------------------------------------------
ZX0, ZX1, ZY = 150, 1130, 560                         # Zeitstrahl: 1.1.2022 bis 31.12.2026
def zx(jahr):                                         # x-Position eines Zeitpunkts (Jahr als Dezimalzahl)
    return ZX0 + (jahr - 2022) / 5 * (ZX1 - ZX0)


ABL = beim("rech", "Ablauf")
folie([("frist", "Verjährung › Frist, §§ 195, 199 Abs. 1 BGB"), ("hemm", "Verjährung › keine Hemmung")], rechts_frei([
    *tafel("frist", "Verjährung: die Frist"), *mini(3, "frist"),
    z("§ 195: 3 Jahre", 110, 200, "frist", "Bold", 38),
    z("§ 199 Abs. 1: ab Schluss des Jahres der Entstehung", 110, 258, beim("frist", "Sie"), size=34),
    z("und Kenntnis (oder grob fahrlässiger Unkenntnis)", 160, 308, beim("frist", "Gläubiger"), size=34),
    # Zeitstrahl
    linienzug([(ZX0, ZY), (ZX1, ZY)], "rech", breite=5),
    *[e for j in range(2022, 2027) for e in (linienzug([(zx(j), ZY - 14), (zx(j), ZY + 14)], "rech", breite=4),
                                              z(str(j), zx(j) + 8, ZY + 22, "rech", "Bold", 28, rechts=1170))],
    ring(int(zx(2022.8)), ZY, 26, 26, "rech", farbe=ROT, breite=6),
    z("10/2022: fällig mit Abnahme", 150, 380, "rech", "Bold", 32),
    zit("§ 641 Abs. 1 BGB; Entstehung = grundsätzlich Fälligkeit:", 200, 420, beim("rech", "Abnahme")),
    zit("BGH, Beschl. v. 1.2.2023 – XII ZB 104/22, Rn. 16", 200, 452, beim("rech", "Abnahme")),
    blk(int(zx(2023)), ZY - 78, int(zx(2026) - zx(2023)), 54, GELB, beim("rech", "Frist"),
        [("3 Jahre", "ExtraBold", 32, INK)], anim="fade"),
    z("Beginn: 31.12.2022", 150, ZY + 70, beim("rech", "Frist"), "Bold", 32),
    z("verjährt mit Ablauf des 31.12.2025", 150, ZY + 120, ABL, "Bold", 32),
    *neinz("keine Hemmung: keine Verhandlungen,", 745, "hemm", "Bold", 32, x=160),
    z("keine Klage, kein Mahnbescheid (§§ 203, 204 BGB)", 160, 795, beim("hemm", "Herr"), size=32),
    *requisit([("frist", ("tabler", "calendar-event", 100, WEISS), "3 Jahre", WEISS),
               ("rech", ("tabler", "receipt-euro", 90, WEISS), "fällig: 10/2022", WEISS),
               (ABL, ("tabler", "hourglass-empty", 90, GELB), "Ablauf: 31.12.2025", GELB),
               ("hemm", ("tabler", "gavel", 100, WEISS), "keine Klage", WEISS)]),
    *paar("frist", "TI", [("frist", "ruhig"), (ABL, "froh")], "GR", [("frist", "ruhig"), (ABL, "sorge")]),
]))

# F3 aufschiebende Einreden ----------------------------------------------------------------------------------------------------
folie([("aufsch", "III. durchsetzbar › aufschiebende Einreden"), ("zug", "aufschiebende Einreden › Zug um Zug"),
       ("nicht", "aufschiebende Einreden › der Fall")], rechts_frei([
    *tafel("aufsch", "Aufschiebende Einreden"), *mini(3, "aufsch"),
    z("§ 320: gegenseitiger Vertrag", 110, 200, "p320", "Bold", 36),
    z("verweigern bis zur Gegenleistung,", 160, 252, beim("p320", "verweigern"), size=34),
    z("außer bei Vorleistungspflicht", 160, 302, beim("p320", "außer"), size=34),
    z("§ 273: Zurückbehaltungsrecht", 110, 380, "p273", "Bold", 36),
    z("fälliger Gegenanspruch aus demselben", 160, 432, beim("p273", "demselben"), size=34),
    z("rechtlichen Verhältnis", 160, 482, beim("p273", "rechtlichen"), size=34),
    blk(110, 560, 1040, 80, GELB, "zug", [("Im Prozess: Verurteilung Zug um Zug", "ExtraBold", 36, INK)]),
    zit("§ 274 Abs. 1, § 322 Abs. 1 BGB", 160, 652, beim("zug", "Zug")),
    *neinz("§ 320: Tisch ist fertig", 715, beim("nicht", "Tisch"), "Bold", 34, x=160),
    *neinz("§ 273: kein Gegenanspruch", 775, beim("nicht", "einen"), "Bold", 34, x=160),
    *requisit([("aufsch", ("tabler", "clock", 100, WEISS), "aufschiebend", WEISS),
               ("p320", ("tabler", "arrows-exchange", 100, WEISS), "Leistung gegen Leistung", WEISS),
               ("p273", ("tabler", "hand-stop", 100, WEISS), "zurückbehalten", WEISS),
               ("zug", ("tabler", "arrows-left-right", 100, GELB), "Zug um Zug", GELB),
               ("nicht", ("tabler", "x", 100, WEISS), "passt nicht", WEISS)]),
    *paar("aufsch", "TI", [("aufsch", "ruhig"), ("nicht", "denkt")], "GR", [("aufsch", "ruhig"), ("nicht", "froh")]),
]))

# G Wirkung im Prozess ------------------------------------------------------------------------------------------------------------
folie([("amt", "Einwendung oder Einrede › Wirkung im Prozess")], rechts_frei([
    *tafel("amt", "Wirkung im Prozess"),
    blk(110, 190, 505, 80, BLAU, beim("amt", "Einwendungen"), [("Einwendung", "ExtraBold", 38, INK)]),
    z("Gericht beachtet sie", 130, 300, beim("amt", "beachtet"), "Bold", 34, rechts=610),
    z("von Amts wegen,", 130, 350, beim("amt", "Amts"), "Bold", 34, rechts=610),
    z("sobald die Tatsachen", 130, 400, beim("amt", "sobald"), size=34, rechts=610),
    z("vorgetragen sind", 130, 450, beim("amt", "vorgetragen"), size=34, rechts=610),
    blk(645, 190, 505, 80, GELB, "einr", [("Einrede", "ExtraBold", 38, INK)]),
    z("wirkt nur, wenn sich", 665, 300, beim("einr", "wirken"), "Bold", 34),
    z("der Schuldner darauf", 665, 350, beim("einr", "Schuldner"), "Bold", 34),
    z("beruft", 665, 400, beim("einr", "beruft"), "Bold", 34),
    zit("BGH, Beschl. v. 1.2.2023 – XII ZB 104/22, Rn. 16;", 130, 530, beim("einr", "beruft")),
    zit("BGH, Urt. v. 19.1.2018 – V ZR 273/16, Rn. 27;", 130, 566, beim("einr", "beruft")),
    zit("BGH, Urt. v. 5.7.2016 – XI ZR 254/15, Rn. 27 (§§ 320, 322)", 130, 602, beim("einr", "beruft")),
    blk(110, 680, 1040, 90, ROT, "beruf", [("Einrede nicht erhoben: Tilda muss zahlen", "ExtraBold", 36, INK)]),
    *requisit([("amt", ("tabler", "gavel", 100, WEISS), "von Amts wegen", BLAU),
               ("einr", ("tabler", "hand-stop", 100, GELB), "nur auf Einrede", GELB),
               ("beruf", ("tabler", "cash-banknote", 110, ROT), "muss zahlen", ROT)]),
    *paar("amt", "TI", [("amt", "ruhig"), ("einr", "denkt"), ("beruf", "sorge")], "GR", [("amt", "ruhig"), ("beruf", "froh")]),
]))

# H § 214 Abs. 2 (Wortlaut), § 813 Abs. 1 Satz 2 -----------------------------------------------------------------------------------
W214B = ["„(2) Das zur Befriedigung eines verjährten Anspruchs Geleistete",
         "kann nicht zurückgefordert werden, auch wenn in Unkenntnis der",
         "Verjährung geleistet worden ist. …“"]
w214b, w214b_y = wortlaut(80, 190, 1100, W214B, "§ 214 Abs. 2 BGB", "p214b", marken=[
    (1, "nicht zurückgefordert", beim("p214b", "nicht")), (1, "in Unkenntnis", beim("p214b", "Unkenntnis"))], size=32)
folie([("tot", "Verjährung › § 214 Abs. 2 BGB"), ("p813", "Verjährung › § 813 Abs. 1 Satz 2 BGB")], rechts_frei([
    *tafel("tot", "Verjährung tötet den Anspruch nicht"),
    *w214b,
    z("§ 813 Abs. 1 Satz 1: Rückforderung bei dauernder", 110, w214b_y + 40, "p813", "Bold", 34),
    z("Einrede grundsätzlich möglich – aber Satz 2:", 160, w214b_y + 92, beim("p813", "nimmt"), size=34),
    z("„Die Vorschrift des § 214 Abs. 2 bleibt unberührt.“", 160, w214b_y + 144, beim("p813", "genau"), "Bold", 34),
    blk(110, w214b_y + 230, 1040, 90, GRUEN, beim("p813", "Fall"), [("Gezahlt ist gezahlt", "ExtraBold", 38, INK)]),
    *requisit([("tot", ("tabler", "heart", 100, PINK), "Anspruch lebt", PINK),
               ("p214b", ("tabler", "cash-banknote", 110, WEISS), "kein Geld zurück", WEISS),
               ("p813", ("tabler", "arrow-back-up", 100, WEISS), "§ 813: Ausnahme", WEISS)]),
    *paar("tot", "TI", [("tot", "staunt"), ("p214b", "sorge")], "GR", [("tot", "ruhig"), ("p214b", "froh")]),
]))

# I Ergebnis ---------------------------------------------------------------------------------------------------------------
folie([("erg", "Ergebnis")], rechts_frei([
    *tafel("erg", "Ergebnis"),
    *okz("Werklohn, § 631 Abs. 1 BGB: 1.400 €", 200, "erg", "Bold", 36, x=160),
    *okz("I. entstanden", 270, beim("erg", "entstanden"), "Bold", 36, x=160),
    *okz("II. nicht untergegangen", 335, beim("erg", "untergegangen"), "Bold", 36, x=160),
    *neinz("III. durchsetzbar: verjährt, § 214 Abs. 1 BGB", 400, "erg2", "Bold", 36, x=160),
    blk(110, 490, 1040, 90, GELB, beim("erg2", "Beruft"), [("Einrede erhoben: Tilda muss nicht zahlen", "ExtraBold", 36, INK)]),
    blk(110, 620, 1040, 90, HELLROT, "erg3", [("Zahlt sie trotzdem: Geld weg, § 214 Abs. 2 BGB", "ExtraBold", 34, INK)]),
    *requisit([("erg", ("tabler", "receipt-euro", 90, WEISS), "1.400 €", WEISS),
               (beim("erg2", "Beruft"), ("tabler", "hand-stop", 100, GELB), "Einrede", GELB),
               ("erg3", ("tabler", "cash-banknote", 110, ROT), "Geld weg", ROT)]),
    *paar("erg", "TI", [("erg", "ruhig"), (beim("erg2", "Beruft"), "frech"), ("erg3", "sorge")],
          "GR", [("erg", "ruhig"), (beim("erg2", "Beruft"), "sorge"), ("erg3", "froh")]),
]))

# J Klausurtipp (Lexi), § 215 (Wortlaut) ---------------------------------------------------------------------------------------
W215 = ["„Die Verjährung schließt die Aufrechnung … nicht aus,",
        "wenn der Anspruch in dem Zeitpunkt noch nicht verjährt war,",
        "in dem erstmals aufgerechnet … werden konnte.“"]
w215, w215_y = wortlaut(100, 420, 1070, W215, "§ 215 BGB", beim("tipp2", "Nach"), marken=[
    (0, "Aufrechnung", beim("tipp2", "Aufrechnung", 2)), (1, "noch nicht verjährt", beim("tipp2", "noch")),
    (2, "erstmals aufgerechnet", beim("tipp2", "erstmals"))], size=32)
folie([("tipp", "Klausurtipp · Verjährung richtig einordnen"), ("tipp2", "Klausurtipp · Aufrechnung, § 215 BGB")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Verjährung nie beim Untergang prüfen,", 200, 200, beim("tipp", "Die"), "Bold", 36),
    z("sondern bei der Durchsetzbarkeit", 200, 255, beim("tipp", "sondern"), "Bold", 36),
    z("Vorsicht bei der Aufrechnung:", 200, 345, "tipp2", "Bold", 36),
    *w215,
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# K Klausurschema (Treppe) --------------------------------------------------------------------------------------------------
S_X, S_W, S_U = (110, 690, 1270), 560, 905
S_O = (610, 455, 300)
SCH = [("k1", "I. Anspruch entstanden", [("rechtshindernde Einwendungen", "k1", "rechtshindernden"),
                                          ("z. B. Nichtigkeit:", "k1", "Nichtigkeit"),
                                          ("§§ 105, 125, 134, 138 BGB", "k1", "Nichtigkeit")]),
       ("k2", "II. Anspruch untergegangen", [("rechtsvernichtende Einwendungen", "k2", "rechtsvernichtende"),
                                             ("Erfüllung, Aufrechnung,", "k2", "Erfüllung"),
                                             ("Anfechtung", "k2", "Anfechtung"),
                                             ("§§ 362, 389, 142 Abs. 1 BGB", "k2", "Anfechtung")]),
       ("k3", "III. Anspruch durchsetzbar", [("rechtshemmende Einreden", "k3", "Einreden"),
                                            ("dauernd: Verjährung, § 214", "k3a", None),
                                            ("aufschiebend: §§ 320, 273", "k3b", None)])]
els_sch = [karte(60, 50, 1800, 900, "sch"), titel(glyphen("Klausurschema: Anspruch aus § 631 Abs. 1 BGB"), 110, 90, "sch", 46)]
for k, (c, kopf, zeilen) in enumerate(SCH):
    els_sch += [stufe(S_X[k], S_O[k], S_W, S_U, k + 1, c),
                z(kopf, S_X[k] + 22, S_O[k] + 18, c, "ExtraBold", 34, rechts=S_X[k] + S_W - 12)]
    for j, (t, cc, w) in enumerate(zeilen):
        els_sch.append(z(t, S_X[k] + 22, S_O[k] + 76 + j * 44, beim(cc, w) if w else cc, "Bold" if j == 0 else "Regular",
                         30, rechts=S_X[k] + S_W - 12))
els_sch.append(z("IV. Ergebnis", S_X[2] + 22, 215, "k4", "ExtraBold", 40, rechts=1820))
folie([("sch", "Klausurschema"), ("k1", "Klausurschema › I. entstanden"), ("k2", "Klausurschema › II. untergegangen"),
       ("k3", "Klausurschema › III. durchsetzbar"), ("k4", "Klausurschema › IV. Ergebnis")], els_sch)

# L Merksatz (Lexi) -----------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Einwendungen ", 0), ("hindern oder vernichten", "a")], [("den Anspruch, das Gericht beachtet sie von selbst.", 0)]],
                750, 290, 40, "merke", {"a": beim("merke", "hindern")}),
    *markertext([[("Einreden ", 0), ("lassen ihn bestehen", "b")], [("und wirken nur, wenn der Schuldner sie erhebt.", 0)]],
                750, 480, 40, "mk2", {"b": beim("mk2", "lassen")}),
    *markertext([[("Verjährung ", 0), ("tötet den Anspruch nicht:", "c")], [("Wer zahlt, bekommt nichts zurück.", 0)]],
                750, 670, 40, "mk3", {"c": beim("mk3", "tötet")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
