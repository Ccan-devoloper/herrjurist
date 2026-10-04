"""Folge 145 · Hauskauf in drei Schritten: Kaufvertrag, Auflassung, Grundbuch – Serienstandard Open Peeps (Katzenkönig).
Beispielfall: Ute und Joachim kaufen von Herrn Ackermann ein Haus; bei der Notarin Kaufvertrag und Auflassung im selben
Termin (die zunächst gewünschte Bedingung lässt Herr Ackermann fallen); Wochen später Fälligkeitsmitteilung, Zahlung,
Antrag, Eintragung.
Szenen laut ../SZENENPLAN.md: A1 Bei der Notarin, A2 Wochen später / Frage, B Sachverhalt, C Aufbau, D 1. Kaufvertrag
§ 311b Abs. 1 S. 1 (Wortlaut), § 125, E Heilung § 311b Abs. 1 S. 2 (Wortlaut), Trennungsprinzip, F 2. Auflassung § 925 Abs. 1
S. 1 (Wortlaut), Vertretung, G § 925 Abs. 2 (Wortlaut), Rechtsklarheit, H Sofa ja – Haus nein, Vorlagesperre, I 3. Eintragung
§ 873 Abs. 1 (Wortlaut) mit Zeitstrahl, J Zwischenzeit: Vormerkung § 883, Fälligkeitsmitteilung, K Ergebnis (vor dem Haus),
L Klausurtipp (Lexi), M Klausurschema, N Merksatz (Lexi).
Handlungsgeräusch: Unterschrift bei der Notarin (../geraeusche_herkunft.json).
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/hand/okz/
neinz/tisch/punkt als eigene Kopie aus Folge 139 (gemeinsame Dateien unverändert); neu: paar(), requisit(), zeitstrahl().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_145/"

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
HELLROT = (250, 205, 198, 255)
HELLGRUEN = (214, 240, 214, 255)
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
    """Rechtstafel links, rechts bleibt Platz für die Figuren; frei = rechte Grenze des Titels (Rechenleiste)."""
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
    """Figuren und Requisiten der Tafelfolien stehen rechts der Tafel (Diagramm-Icons des Zeitstrahls ausgenommen)."""
    for e in els:
        n = e.name or ""
        if n.startswith(("bild:", "ficon:")) or "/op_145/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def dicon(*a, **k):
    """Icon als Teil eines Diagramms innerhalb der Tafel (Zeitstrahl), nicht als Requisit."""
    e = ficon(*a, **k)
    e.name = "diagramm:" + (e.name or "")
    return e


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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 027/073/083/103) --------------------------------
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



def tisch(cx, unten, cue, w=420, h=250, fill=GELB):
    """Schreibtisch/Ladentheke in Seitenansicht (programmatisch: Platte, zwei Beine; Palettenfläche, Tuschekontur)."""
    s = 2
    im = Image.new("RGBA", ((w + 12) * s, (h + 12) * s))
    dr = ImageDraw.Draw(im)
    o = 6 * s
    dr.rounded_rectangle((o, o, o + w * s, o + 30 * s), 10 * s, fill=fill, outline=INK, width=5 * s)
    for lx in (24, w - 46):
        dr.rectangle((o + lx * s, o + 28 * s, o + (lx + 22) * s, o + h * s), fill=WEISS, outline=INK, width=5 * s)
    im = im.resize((w + 12, h + 12), Image.LANCZOS)
    return El(im, cx - w / 2 - 6, unten - h - 6, cue, "cut", 0.0, None, name="tisch")


def punkt(cx, cy, cue, farbe=ROT, r=11):
    im = Image.new("RGBA", (2 * r + 8, 2 * r + 8))
    ImageDraw.Draw(im).ellipse((4, 4, 2 * r + 4, 2 * r + 4), fill=farbe, outline=INK, width=4)
    return El(im, cx - r - 4, cy - r - 4, cue, "pop", 0.0, None, name="punkt")






BODEN, FH = 860, 480
X1, X2 = 1420, 1720                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
PX, PY, PU = 1570, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"UT": "Ute", "JO": "Joachim", "AK": "Herr Ackermann", "NO": "Notarin"}
NFARBE = {"UT": BLAU, "JO": ROT, "AK": GRUEN, "NO": LILA}
HAUS = GELB                                 # das Haus durchgehend gelb (Phosphor house)
GB = BLAU                                   # Grundbuch durchgehend blau (Tabler book-2)


def boden(cue, hart_=False, x0=40, x1=1880):
    e = linienzug([(x0, BODEN), (x1, BODEN)], cue, breite=7, farbe=INK)
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


# ===========================================================================================================================
# A1 Fall: bei der Notarin (Ackermann links, Notarin hinter dem Tisch, Ute und Joachim rechts)
# ===========================================================================================================================
AKX, NOX, UTX, JOX = 300, 820, 1330, 1640
UNT = beim("unter", "unterschreiben")
folie([(NULL, "Fall · Der Hauskauf"), ("notar", "Fall · Bei der Notarin"), ("n1", "Fall · Die Einigung"),
       ("unter", "Fall · Die Unterschrift")], [
    boden(NULL, hart_=True),
    pl("Ute und Joachim kaufen ein Haus", 70, 30, NULL, fill=GELB, size=40, anim="cut", bis="n1"),
    hart(ficon("ph", "house", 520, 400, 200, NULL, fuell=HAUS, bis="n1")),
    pl("Herr Ackermann: Eigentümer im Grundbuch", 70, 120, beim("verk", "Eigentümer"), fill=WEISS, size=34, bis="n1"),
    ficon("tabler", "book-2", 700, 400, 110, beim("verk", "Grundbuch"), fuell=GB, bis="n1"),
    *fig("UT", UTX, BODEN, FH, [(NULL, "laechelt"), ("notar", "ruhig"), ("n1", "denkt"), ("ak1", "staunt"), ("n2", "ruhig")],
         erst="cut", bis="ut1"),
    hart(ns("Ute", UTX, BODEN, NULL, NFARBE["UT"])),
    *redet("UT_redet", UTX, BODEN, FH, "ut1", "unter"),
    *fig("UT", UTX, BODEN, FH, [("unter", "froh"), ("jo1", "laechelt")], erst="cut"),
    *fig("JO", JOX, BODEN, FH, [(NULL, "froh"), ("notar", "ruhig"), ("n1", "laechelt"), ("ak1", "sorge"), ("ak2", "froh"),
                                ("unter", "laechelt")], erst="cut", bis="jo1"),
    hart(ns("Joachim", JOX, BODEN, NULL, NFARBE["JO"])),
    *redet("JO_redet", JOX, BODEN, FH, "jo1", "spaet"),
    *fig("AK", AKX, BODEN, FH, [(beim("verk", "gehört"), "ruhig_r"), ("n1", "denkt_r")], bis="ak1"),
    ns("Herr Ackermann", AKX, BODEN, beim("verk", "gehört"), NFARBE["AK"], d=0.1),
    *redet("AK_streng_r", AKX, BODEN, FH, "ak1", "n2"),
    *fig("AK", AKX, BODEN, FH, [("n2", "ernst_r")], erst="cut", bis="ak2"),
    *redet("AK_redet_r", AKX, BODEN, FH, "ak2", "ut1"),
    *fig("AK", AKX, BODEN, FH, [("ut1", "froh_r")], erst="cut"),
    # Notarin hinter dem Tisch (Tisch nach der Figur gezeichnet, verdeckt die Beine)
    *fig("NO", NOX, BODEN, FH, [("notar", "laechelt_r"), ("vorl", "ruhig_r")], bis="n1"),
    *redet("NO_redet_r", NOX, BODEN, FH, "n1", "ak1"),
    *fig("NO", NOX, BODEN, FH, [("ak1", "denkt")], erst="cut", bis="n2"),
    *redet("NO_streng", NOX, BODEN, FH, "n2", "ak2"),
    *fig("NO", NOX, BODEN, FH, [("ak2", "laechelt"), ("ut1", "laechelt_r"), ("jo1", "ruhig_r")], erst="cut"),
    tisch(NOX, BODEN, "notar", w=460, h=230, fill=GELB),
    ns("Notarin", NOX, BODEN, "notar", NFARBE["NO"], d=0.1),
    ficon("tabler", "contract", NOX - 170, BODEN - 236, 90, "vorl", fuell=WEISS),
    pl("Kaufvertrag", NOX - 170, 520, "vorl", fill=WEISS, size=30, anker="m", bis="n1"),
    szene(ficon("tabler", "writing-sign", NOX + 170, BODEN - 236, 90, UNT, fuell=WEISS), "145unterschrift*", 0.7, 0.0),
    pl("Alle unterschreiben", 70, 30, UNT, fill=GRUEN, size=40, bis="jo1"),
    # Sprechblasen
    blase("sprech", 900, 210, "n1", 900, 200, inhalt=["Sind Sie sich einig, dass das Eigentum", "am Grundstück auf die Käufer übergeht?"],
          textsize=34, figur=("NO_redet_r", NOX, BODEN, FH), bis="ak1"),
    blase("sprech", 700, 200, "ak1", 560, 200, inhalt=["Ja. Aber erst, wenn", "der Kaufpreis bezahlt ist."], textsize=36,
          figur=("AK_streng_r", AKX, BODEN, FH), bis="n2"),
    blase("sprech", 900, 250, "n2", 860, 190, inhalt=["Unter einer Bedingung geht das nicht.", "Ich beantrage die Eintragung erst,",
                                                       "wenn Ihr Geld da ist."], textsize=34,
          figur=("NO_streng", NOX, BODEN, FH), bis="ak2"),
    blase("sprech", 700, 170, "ak2", 560, 210, inhalt=["Gut, dann ohne Bedingung: Ja."], textsize=36,
          figur=("AK_redet_r", AKX, BODEN, FH), bis="ut1"),
    blase("sprech", 600, 170, "ut1", 1180, 210, inhalt=["Ja, wir sind uns einig."], textsize=38,
          figur=("UT_redet", UTX, BODEN, FH), bis="unter"),
    blase("sprech", 760, 170, "jo1", 1300, 230, inhalt=["Ab heute gehört uns das Haus!"], textsize=38,
          figur=("JO_redet", JOX, BODEN, FH), bis="spaet"),
])

# ===========================================================================================================================
# A2 Fall: Wochen später vor dem Haus, Frage
# ===========================================================================================================================
HX = 470                                     # Haus links
U2, J2 = 1300, 1600                          # Ute und Joachim rechts, blicken nach links zum Haus
folie([("spaet", "Fall · Wochen später"), ("frage", "Fall · Die Frage")], [
    boden("spaet"),
    hart(ficon("ph", "house", HX, BODEN, 440, "spaet", fuell=HAUS)),
    ficon("ph", "tree", HX + 330, BODEN, 170, "spaet", fuell=GRUEN),
    pl("Wochen später", 70, 30, "spaet", fill=WEISS, size=40, bis="frage"),
    ficon("tabler", "mail-opened", 1000, 300, 110, beim("spaet", "teilt"), fuell=WEISS, bis="zahl"),
    pl("Kaufpreis fällig", 70, 120, beim("spaet", "Kaufpreis"), fill=GELB, size=36, bis="frage"),
    ficon("tabler", "coins", 1000, 300, 120, "zahl", fuell=GELB, bis="gb"),
    pl("Ute und Joachim zahlen", 70, 200, beim("zahl", "zahlen"), fill=GRUEN, size=36, bis="frage"),
    ficon("tabler", "book-2", 1000, 300, 120, beim("gb", "Grundbuchamt"), fuell=GB, bis="frage"),
    pl("Grundbuch: Ute und Joachim", 70, 280, beim("gb", "Eigentümer"), fill=BLAU, size=36, bis="frage"),
    *fig("UT", U2, BODEN, FH, [("spaet", "ruhig"), ("zahl", "laechelt"), ("gb", "froh"), ("frage", "denkt")]),
    ns("Ute", U2, BODEN, "spaet", NFARBE["UT"], d=0.1),
    *fig("JO", J2, BODEN, FH, [("spaet", "ruhig"), ("zahl", "laechelt"), ("gb", "froh"), ("frage", "denkt")], d=0.2),
    ns("Joachim", J2, BODEN, "spaet", NFARBE["JO"], d=0.3),
    pl("Ab wann gehört ihnen das Haus?", 70, 30, "frage", fill=PINK, size=40),
    ficon("tabler", "writing-sign", 190, 290, 90, "o1", fuell=WEISS),
    pl("Unterschrift?", 190, 320, "o1", fill=WEISS, size=30, anker="m"),
    ficon("tabler", "coins", 470, 290, 90, "o2", fuell=GELB),
    pl("Zahlung?", 470, 320, "o2", fill=WEISS, size=30, anker="m"),
    ficon("tabler", "book-2", 750, 290, 90, "o3", fuell=GB),
    pl("Eintragung?", 750, 320, "o3", fill=WEISS, size=30, anker="m"),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_145(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=36, zeilenabstand=1.30)
        els += e; y += 16
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=34))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_145("sv", [
    "Ute und Joachim kaufen von Herrn Ackermann ein Haus. Herr Ackermann ist als Eigentümer im Grundbuch eingetragen. "
    "Bei einer Notarin wird der Kaufvertrag beurkundet.",
    "Im selben Termin erklären alle die Auflassung. Herr Ackermann will zunächst, dass das Eigentum erst nach Zahlung des "
    "Kaufpreises übergeht. Die Notarin sagt, eine Bedingung gehe nicht; sie werde die Eintragung erst nach Zahlung "
    "beantragen. Daraufhin erklären alle die Auflassung ohne Bedingung und unterschreiben.",
    "Wochen später teilt die Notarin mit, dass der Kaufpreis fällig ist. Ute und Joachim zahlen. Danach beantragt die "
    "Notarin die Eintragung, und das Grundbuchamt trägt die beiden als Eigentümer ein.",
], "Ab wann gehört Ute und Joachim das Haus?")

# ===========================================================================================================================
# C Aufbau: drei Schritte
# ===========================================================================================================================
SCHRITTE = [("s1", "1.", "Kaufvertrag", GELB), ("s2", "2.", "Auflassung", GRUEN), ("s3", "3.", "Eintragung ins Grundbuch", BLAU)]
folie([("plan", "Hauskauf › Aufbau")], rechts_frei([
    *tafel("plan", "Hauskauf in drei Schritten"),
    *[e for k, (c, r, t, fa) in enumerate(SCHRITTE) for e in (
        karte(130, 220 + k * 150, 110, 90, c, fill=fa, rund=14, schatten=5, rand=4),
        z(r, 185 - F("ExtraBold", 40).getlength(r) / 2, 240 + k * 150, c, "ExtraBold", 40),
        z(t, 280, 240 + k * 150, c, "Bold", 40))],
    *requisit([("plan", ("ph", "house", 150, HAUS), "3 Schritte", WEISS),
               ("s1", ("tabler", "contract", 100, WEISS), "Kaufvertrag", GELB),
               ("s2", ("ph", "handshake", 120, GRUEN), "Auflassung", GRUEN),
               ("s3", ("tabler", "book-2", 110, GB), "Grundbuch", BLAU)]),
    *paar("plan", "UT", [("plan", "ruhig"), ("s2", "denkt"), ("s3", "laechelt")], "JO", [("plan", "laechelt"), ("s3", "froh")]),
]))

# ===========================================================================================================================
# D 1. Kaufvertrag: § 311b Abs. 1 S. 1 (Wortlaut), Zweck, § 125 S. 1
# ===========================================================================================================================
W311 = ["„(1) Ein Vertrag, durch den sich der eine Teil verpflichtet,",
        "das Eigentum an einem Grundstück zu übertragen oder zu",
        "erwerben, bedarf der notariellen Beurkundung. …“"]
w311, w311_y = wortlaut(80, 180, 1100, W311, "§ 311b Abs. 1 S. 1 BGB", beim("k1", "Paragraf"), marken=[
    (1, "Eigentum an einem Grundstück", beim("w311", "Eigentum")),
    (2, "notariellen Beurkundung", beim("w311", "notariellen"))], size=33)
folie([("k1", "1. Kaufvertrag › § 311b Abs. 1 S. 1 BGB"), ("nichtig", "1. Kaufvertrag › Formmangel, § 125 S. 1 BGB")],
      rechts_frei([
    *tafel("k1", "1. Kaufvertrag: beim Notar"),
    *w311,
    z("Zweck: Schutz vor unüberlegten Verträgen,", 110, w311_y + 40, "zweck", "Bold", 36),
    z("Belehrung durch den Notar", 110, w311_y + 95, beim("zweck", "Notar"), "Bold", 36),
    zit("vgl. BGH, Urt. v. 14.9.2018 – V ZR 213/17, Rn. 12", 110, w311_y + 150, beim("zweck", "Notar")),
    *neinz("ohne Beurkundung: nichtig, § 125 S. 1 BGB", w311_y + 230, beim("nichtig", "nichtig"), "Bold", 36, x=160),
    *requisit([("k1", ("tabler", "contract", 100, WEISS), "Kaufvertrag", GELB),
               (beim("w311", "notariellen"), ("tabler", "writing-sign", 100, WEISS), "notarielle Beurkundung", WEISS),
               ("zweck", ("tabler", "shield-check", 100, GRUEN), "Schutz", GRUEN),
               (beim("nichtig", "nichtig"), ("tabler", "ban", 100, ROT), "nichtig", ROT)]),
    *paar("k1", "UT", [("k1", "ruhig"), ("zweck", "laechelt"), ("nichtig", "denkt")], "AK",
          [("k1", "ruhig"), ("zweck", "froh"), ("nichtig", "ernst")]),
]))

# ===========================================================================================================================
# E Heilung § 311b Abs. 1 S. 2 (Wortlaut), Trennungsprinzip (Verweis 005)
# ===========================================================================================================================
W311B = ["„Ein ohne Beachtung dieser Form geschlossener Vertrag wird",
         "seinem ganzen Inhalt nach gültig, wenn die Auflassung und",
         "die Eintragung in das Grundbuch erfolgen.“"]
w311b, w311b_y = wortlaut(80, 180, 1100, W311B, "§ 311b Abs. 1 S. 2 BGB", "heil", marken=[
    (1, "gültig", beim("w311b", "gültig")), (1, "Auflassung", beim("w311b", "Auflassung")),
    (2, "die Eintragung in das Grundbuch", beim("w311b", "Eintragung"))], size=33)
folie([("heil", "1. Kaufvertrag › Heilung, § 311b Abs. 1 S. 2 BGB"), ("trenn", "1. Kaufvertrag › noch kein Eigentum")],
      rechts_frei([
    *tafel("heil", "1. Kaufvertrag: Heilung"),
    *w311b,
    linienzug([(110, w311b_y + 40), (1150, w311b_y + 40)], "trenn", breite=3),
    *okz("Pflicht: das Eigentum zu verschaffen", w311b_y + 70, beim("trenn", "verpflichtet"), "Bold", 36, x=160),
    zit("§ 433 Abs. 1 S. 1 BGB", 160, w311b_y + 125, beim("trenn", "verpflichtet")),
    *neinz("übertragen: noch nichts", w311b_y + 180, "nochn", "Bold", 36, x=160),
    blk(110, w311b_y + 260, 1040, 80, LILA, "verw", [("Trennungsprinzip: Video „Abstraktionsprinzip“", "ExtraBold", 32, INK)]),
    *requisit([("heil", ("tabler", "file-check", 100, GRUEN), "Heilung", GRUEN),
               ("trenn", ("tabler", "contract", 100, WEISS), "nur Pflicht", WEISS),
               ("nochn", ("ph", "house", 140, HAUS), "noch kein Eigentum", ROT),
               ("verw", ("tabler", "arrows-split-2", 100, WEISS), "Trennungsprinzip", LILA)]),
    *paar("heil", "JO", [("heil", "ruhig"), ("trenn", "denkt"), ("nochn", "sorge")], "AK",
          [("heil", "ruhig"), ("trenn", "ernst"), ("verw", "ruhig")]),
]))

# ===========================================================================================================================
# F 2. Auflassung: § 925 Abs. 1 S. 1 (Wortlaut), S. 2, Vertretung, Regelfall
# ===========================================================================================================================
W925 = ["„(1) Die zur Übertragung des Eigentums an einem Grundstück",
        "nach § 873 erforderliche Einigung des Veräußerers und",
        "des Erwerbers (Auflassung) muss bei gleichzeitiger",
        "Anwesenheit beider Teile vor einer zuständigen Stelle",
        "erklärt werden. …“"]
w925, w925_y = wortlaut(80, 180, 1100, W925, "§ 925 Abs. 1 S. 1 BGB", beim("a1", "Einigung"), marken=[
    (1, "Einigung des Veräußerers und", beim("w925", "Einigung")),
    (2, "gleichzeitiger", beim("w925", "gleichzeitiger")), (3, "Anwesenheit beider Teile", beim("w925", "Anwesenheit")),
    (3, "zuständigen Stelle", beim("w925", "zuständigen"))], size=32)
folie([("a1", "2. Auflassung › § 925 Abs. 1 S. 1 BGB"), ("vertr", "2. Auflassung › Vertretung"),
       ("regel", "2. Auflassung › im Fall")], rechts_frei([
    *tafel("a1", "2. Auflassung"),
    *w925,
    z("zuständig: jeder Notar, § 925 Abs. 1 S. 2 BGB", 110, w925_y + 30, "zust", "Bold", 34),
    *okz("nicht persönlich: Vertretung möglich,", w925_y + 100, "vertr", "Bold", 34, x=160),
    z("etwa mit Auflassungsvollmacht", 160, w925_y + 150, beim("vertr", "Auflassungsvollmacht"), size=34),
    zit("vgl. BGH, Urt. v. 27.5.2020 – XII ZR 107/17, Rn. 19", 160, w925_y + 200, beim("vertr", "Auflassungsvollmacht")),
    *okz("im Fall: im selben Termin wie der Kaufvertrag", w925_y + 255, beim("regel", "selben"), "Bold", 34, x=160),
    zit("vgl. BGH, Urt. v. 14.9.2018 – V ZR 213/17, Rn. 13", 160, w925_y + 305, beim("regel", "regelmäßig")),
    *requisit([("a1", ("ph", "handshake", 120, GRUEN), "Einigung", GRUEN),
               (beim("w925", "gleichzeitiger"), ("tabler", "users", 110, WEISS), "beide gleichzeitig", WEISS),
               ("zust", ("ph", "seal-check", 110, LILA), "jeder Notar", LILA),
               ("vertr", ("tabler", "file-certificate", 100, WEISS), "Vollmacht", WEISS),
               ("regel", ("tabler", "calendar-event", 100, WEISS), "ein Termin", GELB)]),
    *paar("a1", "NO", [("a1", "ruhig"), ("zust", "laechelt"), ("regel", "ruhig")], "JO",
          [("a1", "ruhig"), ("vertr", "denkt"), ("regel", "laechelt")]),
]))

# ===========================================================================================================================
# G § 925 Abs. 2 (Wortlaut), Bedingung von Herrn Ackermann, Rechtsklarheit
# ===========================================================================================================================
W9252 = ["„(2) Eine Auflassung, die unter einer Bedingung oder einer",
         "Zeitbestimmung erfolgt, ist unwirksam.“"]
w9252, w9252_y = wortlaut(80, 180, 1100, W9252, "§ 925 Abs. 2 BGB", "w9252", marken=[
    (0, "Bedingung", beim("w9252", "Bedingung")), (1, "Zeitbestimmung", beim("w9252", "Zeitbestimmung")),
    (1, "unwirksam", beim("w9252", "unwirksam"))], size=34)
folie([("w9252", "2. Auflassung › § 925 Abs. 2 BGB"), ("klar", "2. Auflassung › Warum so streng?")], rechts_frei([
    *tafel("w9252", "2. Auflassung: ohne Bedingung"),
    *w9252,
    *neinz("„erst, wenn der Kaufpreis bezahlt ist“:", w9252_y + 40, "akb", "Bold", 34, x=160),
    z("Auflassung wäre unwirksam gewesen", 160, w9252_y + 95, beim("akb", "unwirksam"), "Bold", 34),
    linienzug([(110, w9252_y + 170), (1150, w9252_y + 170)], "klar", breite=3),
    z("Warum so streng?", 110, w9252_y + 190, "klar", "ExtraBold", 36),
    z("Das Grundbuch soll zeigen, wem ein Grundstück gehört.", 110, w9252_y + 250, beim("klar", "Grundbuch"), size=34),
    z("Sachenrechtliche Zuordnung: in erhöhtem Maße", 110, w9252_y + 305, beim("klar", "sachenrechtliche"), size=34),
    z("Rechtssicherheit und Rechtsklarheit", 110, w9252_y + 355, beim("klar", "Rechtssicherheit"), "Bold", 34),
    zit("vgl. BGH, Beschl. v. 22.10.2015 – V ZB 126/14, Rn. 10", 110, w9252_y + 410, beim("klar", "Rechtssicherheit")),
    *requisit([("w9252", ("tabler", "hourglass", 100, WEISS), "Bedingung? Frist?", WEISS),
               (beim("w9252", "unwirksam"), ("tabler", "ban", 100, ROT), "unwirksam", ROT),
               ("klar", ("tabler", "book-2", 110, GB), "Rechtsklarheit", BLAU)]),
    *paar("w9252", "NO", [("w9252", "ernst"), ("klar", "ruhig")], "AK",
          [("w9252", "ruhig"), ("akb", "denkt"), ("klar", "ernst")]),
]))

# ===========================================================================================================================
# H Kontrast: Sofa ja – Haus nein; Schutz des Verkäufers durch die Vorlagesperre
# ===========================================================================================================================
folie([("sofa", "2. Auflassung › Kontrast: bewegliche Sachen"), ("sperre", "2. Auflassung › Schutz des Verkäufers")],
      rechts_frei([
    *tafel("sofa", "Bedingung: Sofa ja, Haus nein"),
    karte(110, 190, 1040, 250, "sofa", fill=HELLGRUEN, rund=18, schatten=5, rand=4),
    z("bewegliche Sache: Eigentumsvorbehalt", 140, 210, "sofa", "ExtraBold", 34),
    *okz("aufschiebend bedingt übereignet, § 449 Abs. 1 BGB", 270, beim("sofa", "aufschiebend"), size=34, x=190),
    z("Mehr dazu: Video „Eigentumsvorbehalt“", 190, 350, beim("sofa", "Mehr"), "Bold", 32),
    karte(110, 480, 1040, 330, "sperre", fill=HELL, rund=18, schatten=5, rand=4),
    z("Grundstück: anderer Schutz des Verkäufers", 140, 500, "sperre", "ExtraBold", 34),
    z("Meist wird vereinbart:", 140, 565, beim("sperre", "Meist"), size=34),
    z("der Notar beantragt die Eintragung erst,", 140, 615, beim("sperre", "Notar"), size=34),
    *okz("wenn die Zahlung nachgewiesen ist", 670, beim("sperre", "Zahlung"), "Bold", 34, x=190),
    zit("vgl. BGH, Urt. v. 14.9.2018 – V ZR 213/17, Rn. 20 f.", 190, 735, beim("sperre", "Zahlung")),
    *requisit([("sofa", ("tabler", "sofa", 150, BLAU), "Sofa: bedingt möglich", GRUEN),
               ("sperre", ("ph", "house", 150, HAUS), "Grundstück: anderer Schutz", WEISS),
               (beim("sperre", "Notar"), ("ph", "seal-check", 110, LILA), "Antrag erst nach Zahlung", GELB)]),
    *paar("sofa", "AK", [("sofa", "ruhig"), ("sperre", "denkt"), (beim("sperre", "Zahlung"), "froh")], "NO",
          [("sofa", "ruhig"), ("sperre", "laechelt")]),
]))


# ===========================================================================================================================
# I 3. Eintragung: § 873 Abs. 1 (Wortlaut mit Auslassung), Zeitstrahl
# ===========================================================================================================================
W873 = ["„(1) Zur Übertragung des Eigentums an einem Grundstück …",
        "ist die Einigung des Berechtigten und des anderen Teils",
        "über den Eintritt der Rechtsänderung und die Eintragung",
        "der Rechtsänderung in das Grundbuch erforderlich, …“"]
w873, w873_y = wortlaut(80, 180, 1100, W873, "§ 873 Abs. 1 BGB", beim("e1", "Paragraf"), marken=[
    (1, "Einigung des Berechtigten", beim("w873", "Einigung")),
    (2, "die Eintragung", beim("w873", "Eintragung")), (3, "in das Grundbuch", beim("w873", "Grundbuch"))], size=33)
ZY = w873_y + 210                                    # Zeitstrahl


def zeitstrahl(cue):
    els = [linienzug([(180, ZY), (1080, ZY)], cue, breite=6),
           punkt(180, ZY, cue, farbe=GELB, r=14), punkt(1080, ZY, cue, farbe=BLAU, r=14),
           z("Unterschrift", 120, ZY + 30, cue, "Bold", 32),
           z("Eintragung", 990, ZY + 30, cue, "Bold", 32),
           pl("Wochen oder Monate", 630, ZY - 70, beim("dauer", "Wochen"), fill=WEISS, size=30, anker="m")]
    return els


folie([("e1", "3. Eintragung › § 873 Abs. 1 BGB"), ("dauer", "3. Eintragung › bis dahin")], rechts_frei([
    *tafel("e1", "3. Eintragung ins Grundbuch"),
    *w873,
    blk(110, w873_y + 40, 1040, 80, HELLGRUEN, "erst", [("Eigentum erst mit der Eintragung", "ExtraBold", 36, INK)]),
    *zeitstrahl("dauer"),
    *requisit([("e1", ("tabler", "book-2", 110, GB), "Grundbuch", BLAU),
               ("erst", ("ph", "house", 150, HAUS), "Eigentum: erst jetzt", GRUEN),
               ("dauer", ("tabler", "hourglass", 100, WEISS), "Wochen oder Monate", WEISS)]),
    *paar("e1", "UT", [("e1", "ruhig"), ("erst", "staunt"), ("dauer", "denkt")], "JO",
          [("e1", "ruhig"), ("erst", "sorge"), ("dauer", "denkt")]),
]))

# ===========================================================================================================================
# J Zwischenzeit: Auflassungsvormerkung § 883 (Verweis), Fälligkeitsmitteilung
# ===========================================================================================================================
folie([("vorm", "3. Eintragung › Zwischenzeit: Vormerkung, § 883 BGB"), ("faellig", "3. Eintragung › Praxis: Fälligkeit")],
      rechts_frei([
    *tafel("vorm", "Bis zur Eintragung"),
    z("Auflassungsvormerkung, § 883 BGB", 110, 180, "vorm", "Bold", 36),
    z("Verfügungen nach ihrer Eintragung: unwirksam,", 150, 240, beim("vorm", "Verfügungen"), size=34),
    z("soweit sie den Anspruch der Käufer", 150, 290, beim("vorm", "soweit"), size=34),
    z("vereiteln oder beeinträchtigen würden", 150, 340, beim("vorm", "vereiteln"), size=34),
    zit("§ 883 Abs. 2 S. 1 BGB", 150, 395, beim("vorm", "vereiteln")),
    blk(110, 445, 1040, 70, LILA, beim("vorm", "Dazu"), [("Mehr dazu: eigene Folge", "ExtraBold", 32, INK)]),
    linienzug([(110, 550), (1150, 550)], "faellig", breite=3),
    z("Praxis: Kaufpreis häufig erst fällig nach einer", 110, 575, beim("faellig", "Praxis"), "Bold", 34),
    z("Mitteilung des Notars", 110, 625, beim("faellig", "Mitteilung"), "Bold", 34),
    zit("Vertragsbeispiele: BGH V ZB 174/10, Rn. 1; V ZR 307/13, Rn. 2", 110, 685, beim("faellig", "Mitteilung")),
    *requisit([("vorm", ("tabler", "bookmark", 100, GELB), "Vormerkung", GELB),
               (beim("vorm", "Verfügungen"), ("tabler", "shield-lock", 100, GRUEN), "Anspruch gesichert", GRUEN),
               ("faellig", ("tabler", "mail-opened", 110, WEISS), "Kaufpreis fällig", GELB)]),
    *paar("vorm", "UT", [("vorm", "denkt"), (beim("vorm", "Verfügungen"), "laechelt"), ("faellig", "ruhig")], "JO",
          [("vorm", "ruhig"), (beim("vorm", "Verfügungen"), "froh"), ("faellig", "denkt")]),
]))

# ===========================================================================================================================
# K Ergebnis (vor dem Haus)
# ===========================================================================================================================
folie([("erg", "Ergebnis"), ("r4", "Ergebnis › mit der Eintragung")], rechts_frei([
    *tafel("erg", "Ergebnis"),
    z("Nach der Unterschrift:", 110, 180, "r1", "Bold", 36),
    *okz("wirksamer Kaufvertrag", 245, beim("r1", "Kaufvertrag"), size=36, x=160),
    *okz("wirksame Auflassung", 305, beim("r1", "Auflassung"), size=36, x=160),
    *neinz("aber noch kein Eigentum", 365, beim("r1", "Eigentum"), "Bold", 36, x=160),
    *neinz("Zahlung allein: kein Eigentum", 445, "r2", "Bold", 36, x=160),
    *okz("Herr Ackermann: Berechtigter", 525, "r3", "Bold", 36, x=160),
    blk(110, 615, 1040, 90, HELLGRUEN, beim("r4", "Eintragung"), [("Eintragung: Das Haus gehört den beiden.", "ExtraBold", 36, INK)]),
    boden("erg", x0=1240, x1=1880),
    hart(ficon("ph", "house", 1560, 380, 230, "erg", fuell=HAUS)),
    ficon("tabler", "book-2", 1760, 380, 100, beim("r4", "Eintragung"), fuell=GB),
    *fig("UT", 1400, BODEN, 440, [("erg", "ruhig"), ("r1", "denkt"), ("r4", "froh")]),
    ns("Ute", 1400, BODEN, "erg", NFARBE["UT"], d=0.1),
    *fig("JO", 1700, BODEN, 440, [("erg", "ruhig"), ("r2", "denkt"), ("r4", "froh")], d=0.2),
    ns("Joachim", 1700, BODEN, "erg", NFARBE["JO"], d=0.3),
    pl("Eigentümer: Ute und Joachim", 1560, 80, beim("r4", "gehört"), fill=GRUEN, size=28, anker="m"),
], x0=1250))

# ===========================================================================================================================
# L Klausurtipp (Lexi)
# ===========================================================================================================================
TIPP = [("t1", "1. Einigung (Auflassung)"), ("t2", "2. Eintragung"), ("t3", "3. Einigsein bei der Eintragung"), ("t4", "4. Berechtigung")]
folie([("tipp", "Klausurtipp · Reihenfolge"), ("t5", "Klausurtipp · Einigsein")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Prüfe in dieser Reihenfolge:", 200, 200, beim("tipp", "Reihenfolge"), "Bold", 36),
    *[z(t, 240, 270 + i * 55, c if c != "t4" else beim("t4", "Berechtigung"), size=34) for i, (c, t) in enumerate(TIPP)],
    linienzug([(130, 510), (1130, 510)], "t5", breite=3),
    z("Einigsein: Die Einigung muss bei der", 200, 535, beim("t5", "Einigung"), "Bold", 34),
    z("Eintragung noch bestehen.", 200, 585, beim("t5", "bestehen"), "Bold", 34),
    z("Bindend vorher nur nach § 873 Abs. 2 BGB,", 200, 655, beim("t5", "Bindend"), size=34),
    z("etwa bei notarieller Beurkundung", 200, 705, beim("t5", "etwa"), size=34),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# M Klausurschema
# ===========================================================================================================================
REIHEN = [("kI", "I.", "Einigung (Auflassung)", "§ 925 Abs. 1 BGB", GRUEN, 0),
          ("kI1", "1.", "gleichzeitige Anwesenheit vor zuständiger Stelle", "", None, 1),
          ("kI2", "2.", "ohne Bedingung und Zeitbestimmung", "§ 925 Abs. 2 BGB", None, 1),
          ("kII", "II.", "Eintragung im Grundbuch", "§ 873 Abs. 1 BGB", BLAU, 0),
          ("kIII", "III.", "Einigsein bei der Eintragung", "§ 873 Abs. 2 BGB", GELB, 0),
          ("kIV", "IV.", "Berechtigung des Veräußerers", "", LILA, 0),
          ("kV", "", "daneben: Kaufvertrag als Rechtsgrund, notarielle Form", "§ 311b Abs. 1 S. 1 BGB", None, 2)]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Klausurschema: Eigentumserwerb am Grundstück"), 110, 90, "sch", 46),
           zit("§§ 873, 925 BGB", 110, 150, "sch", size=30)]
y = 215
for c, r, kopf, norm, farbe, ebene in REIHEN:
    if ebene == 0:
        els_sch += [karte(110, y, 110, 70, c, fill=farbe, rund=14, schatten=5, rand=4),
                    z(r, 165 - F("ExtraBold", 38).getlength(r) / 2, y + 10, c, "ExtraBold", 38, rechts=1820),
                    z(kopf, 255, y + 10, c, "ExtraBold", 40, rechts=1820)]
        hh = 100
    elif ebene == 1:
        els_sch += [z(r, 270, y + 4, c, "Bold", 36, rechts=1820), z(kopf, 330, y + 4, c, "Bold", 36, rechts=1820)]
        hh = 80
    else:
        y += 14
        els_sch += [linienzug([(110, y - 8), (1810, y - 8)], c, breite=3), z(kopf, 130, y + 10, c, "ExtraBold", 36, rechts=1240)]
        hh = 92
    if norm:
        els_sch.append(zit(norm, 1300, y + (18 if ebene != 1 else 12), c, size=30, rechts=1820))
    y += hh
assert y <= 970, y
folie([("sch", "Klausurschema"), ("kI", "Klausurschema › I. Einigung (Auflassung)"), ("kII", "Klausurschema › II. Eintragung"),
       ("kIII", "Klausurschema › III. Einigsein"), ("kIV", "Klausurschema › IV. Berechtigung"),
       ("kV", "Klausurschema › Kaufvertrag als Rechtsgrund")], els_sch)

# ===========================================================================================================================
# N Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Der Kaufvertrag", 0)], [("verpflichtet nur.", "a")]],
                750, 290, 42, "merke", {"a": beim("merke", "verpflichtet")}),
    *markertext([[("Eigentum am Haus bringen erst", 0)], [("Auflassung und Eintragung.", "b")]],
                750, 480, 42, "mk2", {"b": beim("mk2", "Auflassung")}),
    *markertext([[("Die Auflassung verträgt", 0)], [("keine Bedingung.", "c")]],
                750, 670, 42, "mk3", {"c": beim("mk3", "Bedingung")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
