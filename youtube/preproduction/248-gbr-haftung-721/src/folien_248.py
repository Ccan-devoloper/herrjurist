"""Folge 248 · Gesellschafterhaftung GbR § 721 BGB: Haften die Mitglieder privat? · Serienstandard Open Peeps (Katzenkönig).
Beispielfall: Philipp und Mathilde betreiben ein Architekturbüro als GbR. Im Februar kauft das Büro beim Tischler Herrn
Altmann Arbeitstische und Regale für 18.000 €, zahlbar Ende Juni. Im März tritt Alma ein (interne Abrede: keine Haftung für
Altschulden), Ende April scheidet Mathilde aus (Rundschreiben an Herrn Altmann). Im Juli ist das Konto des Büros leer;
Herr Altmann verlangt die 18.000 € von Philipp privat. Das Büro hat gegen ihn ein fälliges Honorar von 3.000 €.
Danach: I. Schuld der GbR (§ 705 Abs. 2, § 433 Abs. 2; Verweis 173), II. § 721 (Wortlautkarte) und Merkmale,
III. § 721a (Wortlautkarte), IV. § 721b Abs. 1 und 2 (Wortlautkarten), V. § 728b (Wortlautkarte, Zeitleiste),
VI. § 722 Abs. 2 (Wortlautkarte), VII. Innenausgleich, Ergebnis, Klausurtipp (Zeitleiste), Schema, Merksatz.
Szenen laut ../SZENENPLAN.md. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/feld als eigene Kopie
aus Folge 245 (gemeinsame Dateien unverändert); neu: regal(), buero(), zeitleiste().
Keine echten Firmen; Möbel aus Tabler-Icons bzw. Grundformen ohne Schriftzug.
Handlungsgeräusche: Karton (Mathilde scheidet aus) und Klopfen (Herr Altmann an der Bürotür); ../geraeusche_herkunft.json.
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut nach gesetze-im-internet.de (BGB), Abruf 08.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_248/"

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
HELLROT = (253, 232, 228, 255)
HELLGRUEN = (232, 247, 233, 255)
BLAUHELL = (228, 238, 253, 255)
LILAHELL = (240, 236, 255, 255)
HELLGRAU = (226, 226, 222, 255)
HOLZ = (214, 160, 110, 255)
DUNKELHOLZ = (150, 98, 66, 255)
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
    """Rechtstafel links, rechts bleibt Platz für die Figuren."""
    assert 110 + F("ExtraBold", size).getlength(glyphen(titel_)) <= frei, f"Titel zu breit: {titel_}"
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(titel_, 110, 100, cue, size)]


def blk(x, y, w, h, fill, cue, zeilen, **k):
    for t, s, g, f in zeilen:
        assert g >= 26 and F(s, g).getlength(glyphen(t)) <= w - 30, f"Blockzeile zu breit: {t}"
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
        if n.startswith(("bild:", "ficon:")) or "/op_248/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def umbruch(text, size, breite, stil="Regular"):
    f = F(stil, size); zeilen, akt = [], ""
    for w in text.split(" "):
        t = (akt + " " + w).strip()
        if f.getlength(t) <= breite:
            akt = t
        else:
            zeilen.append(akt); akt = w
    return zeilen + [akt]


def wortlaut(x, y, w, text, quelle, cue, marken=(), size=32, bis=None):
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 08.10.2026), als Zitat mit Normangabe; der
    Zeilenumbruch wird berechnet. marken = [(wort, cue)] legt synchron zum gesprochenen Wort einen Textmarker hinter die
    erste noch nicht markierte Fundstelle von 'wort' (muss in einer Zeile stehen)."""
    zeilen = umbruch(glyphen(text), size, w - 60)
    lh = int(size * 1.42)
    hgt = 40 + lh * len(zeilen) + 46
    els = [bis_(karte(x, y, w, hgt, cue, fill=ZITAT, rund=18, schatten=6, rand=4), bis)]
    f = F("Regular", size)
    tx, ty = x + 28, y + 26
    belegt = []
    for wort, mc in marken:
        treffer = None
        for zi, t in enumerate(zeilen):
            a = t.find(wort)
            while a >= 0 and (zi, a) in belegt:
                a = t.find(wort, a + 1)
            if a >= 0:
                treffer = (zi, a); break
        assert treffer, f"Marker {wort!r} nicht in einer Zeile: {zeilen}"
        belegt.append(treffer)
        zi, a = treffer; t = zeilen[zi]
        x0 = tx + f.getlength(t[:a]) - 4
        x1 = tx + f.getlength(t[:a + len(wort)]) + 4
        y0 = ty + zi * lh + size * 0.30
        im = Image.new("RGBA", (int(x1 - x0) + 2, int(size * 0.85)))
        ImageDraw.Draw(im).rounded_rectangle((0, 0, im.width - 1, im.height - 1), 7, fill=MARKER)
        els.append(El(im, x0, y0, mc, "fade", 0.0, bis, name="marker:" + wort))
    for i, t in enumerate(zeilen):
        els.append(z(t, tx, ty + i * lh, cue, size=size, rechts=x + w - 16, bis=bis))
    els.append(z(quelle, tx, ty + len(zeilen) * lh + 4, cue, "Bold", max(26, size - 4), farbe=TEXT, rechts=x + w - 16, bis=bis))
    return els, y + hgt


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 160/203/205/229) ---------------------------------
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
    return pl(text, cx, unten + 22, cue, fill=fill, size=26 if len(text) > 14 else 30, anker="m", **k)


def okz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Haken davor (zur gesprochenen Bejahung)."""
    return [bis_(ok(x - 45, y + 20, cue, gr=gr), k.get("bis")), z(text, x, y, cue, stil, size, **k)]


def neinz(text, y, cue, stil="Regular", size=34, x=185, gr=20, kreuz=None, **k):
    """Tafelzeile mit Bleistift-Kreuz davor; kreuz = Cue der gesprochenen Verneinung (sonst mit der Zeile)."""
    return [bis_(nein(x - 45, y + 20, kreuz or cue, gr=gr), k.get("bis")), z(text, x, y, cue, stil, size, **k)]



# --- eigene Szenenbausteine (programmatisch, Palettenflächen, Tuschekontur) ---------------------------------------------------
BODEN = 860
FH = 440                                    # stehende Figur in der Fallszene
X1, X2 = 1400, 1720                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"PH": "Philipp", "AL": "Alma", "MA": "Mathilde", "AT": "Herr Altmann"}
NFARBE = {"PH": BLAU, "AL": GRUEN, "MA": LILA, "AT": GELB}
HOLZ = (214, 160, 110, 255)
DUNKELHOLZ = (150, 98, 66, 255)
HELL = (255, 251, 230, 255)
ZITAT = (246, 246, 250, 255)
HELLROT = (253, 232, 228, 255)
HELLGRUEN = (232, 247, 233, 255)
BLAUHELL = (228, 238, 253, 255)
LILAHELL = (240, 236, 255, 255)
WAND = (236, 230, 216, 255)


def _flaeche(w, h):
    s = 2
    im = Image.new("RGBA", ((w + 12) * s, (h + 12) * s))
    return im, ImageDraw.Draw(im), s


def boden(cue):
    return hart(linienzug([(40, BODEN), (1880, BODEN)], cue, breite=7, farbe=INK))


def _feld(w, h, fill=WEISS, rand=4, rund=14):
    im, dr, s = _flaeche(w, h)
    o = 6 * s
    dr.rounded_rectangle((o, o, o + w * s, o + h * s), rund * s, fill=fill, outline=INK, width=rand * s)
    return im.resize((w + 12, h + 12), Image.LANCZOS)


def feld(x, y, w, h, cue, fill=WEISS, rand=4, rund=14, bis=None, anim="cut", name="feld"):
    return El(_feld(w, h, fill, rand, rund), x, y, cue, anim, 0.0, bis, name=name)


def fenster(x, y, w, h, cue):
    """Fenster mit Sprossen (Tageslicht)."""
    return [hart(feld(x, y, w, h, cue, fill=BLAUHELL, rand=5, rund=8, name="fenster")),
            hart(feld(x + w // 2 - 4, y + 6, 8, h - 12, cue, fill=INK, rand=1, rund=2, name="sprosse1")),
            hart(feld(x + 6, y + h // 2 - 4, w - 12, 8, cue, fill=INK, rand=1, rund=2, name="sprosse2"))]


def regal(x, cue, w=230, h=380, anim="pop", bis=None):
    """Bücherregal aus Grundformen (Rahmen, drei Böden) mit Ordnern/Büchern (Tabler books, archive)."""
    els = [bis_(feld(x, BODEN - h - 6, w, h, cue, fill=HOLZ, rand=5, rund=6, anim=anim, name="regal"), bis)]
    for i in range(1, 3):
        els.append(bis_(feld(x + 6, BODEN - 6 - h + i * h // 3 - 4, w - 12, 8, cue, fill=DUNKELHOLZ, rand=2, rund=2,
                             anim=anim, name=f"regalboden{i}"), bis))
    for i, (ic, fu) in enumerate([("books", BLAU), ("archive", GELB), ("books", ROT)]):
        unten = BODEN - 6 - h + (i + 1) * h // 3 - 6
        els.append(ficon("tabler", ic, x + w // 2, unten, 96, cue, fuell=fu, anim=anim, bis=bis))
    return els


# Architekturbüro (A1, A2, Ergebnis): Wand, Fenster, Pflanze, Lampe; ab „Möbel“ neue Tische und Regale
def buero(cue, moebel=None):
    m = moebel or cue
    an = "cut" if moebel is None else "pop"
    return [boden(cue), *fenster(400, 230, 300, 230, cue),
            ficon("tabler", "plant-2", 760, BODEN, 120, cue, fuell=GRUEN, anim="cut"),
            *regal(110, m, anim=an),
            ficon("tabler", "desk", 540, BODEN, 300, m, fuell=HOLZ, anim=an),
            ficon("tabler", "lamp-2", 470, BODEN - 192, 80, m, fuell=GELB, anim=an)]


def _tischkante():
    """Oberkante der Tischplatte (Tabler desk, 300 px breit, unten auf BODEN) aus dem Icon selbst bestimmt."""
    e = ficon("tabler", "desk", 540, BODEN, 300, "fall", fuell=HOLZ)
    a = np.asarray(e.sprite)[:, :, 3] > 60
    return int(e.y + np.nonzero(a.any(1))[0][0]) + 2


TISCH = _tischkante()


def ort(text, cue, bis=None):
    return hart(pl(text, 70, 30, cue, fill=GELB, size=32, bis=bis))


# ===========================================================================================================================
# A1 Fall: das Architekturbüro – Kauf bei Herrn Altmann, Alma tritt ein, Mathilde scheidet aus
# ===========================================================================================================================
PHX, MAX, ALX, ATX = 1000, 1260, 1520, 1740
folie([(NULL, "Fall · Das Architekturbüro"), ("moebel", "Fall · Februar: Möbel für 18.000 €"),
       ("alma", "Fall · März: Alma tritt ein"), ("mathilde", "Fall · Ende April: Mathilde scheidet aus")], [
    *buero(NULL, moebel="moebel"),
    ort("Im Architekturbüro", NULL, bis="moebel"),
    pl("Gesellschaft bürgerlichen Rechts", 70, 104, beim("fall", "Gesellschaft"), fill=WEISS, size=28, bis="moebel"),
    ort("Im Architekturbüro · Februar", "moebel", bis="alma"),
    ort("Im Architekturbüro · März", "alma", bis="mathilde"),
    ort("Im Architekturbüro · Ende April", "mathilde"),
    *fig("PH", PHX, BODEN, FH, [(NULL, "froh_r"), ("moebel", "ruhig_r"), ("alma", "froh_r"), ("mathilde", "ruhig_r")],
         erst="cut"),
    hart(ns(NAME["PH"], PHX, BODEN, NULL, BLAU)),
    *fig("MA", MAX, BODEN, FH, [(NULL, "froh_r"), ("alma", "froh_r"), ("mathilde", "froh_r")], erst="cut"),
    hart(ns(NAME["MA"], MAX, BODEN, NULL, LILA)),
    *fig("AT", ATX, BODEN, FH, [("moebel", "froh")], bis="alma"),
    bis_(ns(NAME["AT"], ATX, BODEN, "moebel", GELB, d=0.1), "alma"),
    pl("Arbeitstische und Regale", 420, 110, beim("moebel", "Arbeitstische"), fill=WEISS, size=30, bis="alma"),
    pl("18.000 € · zahlbar Ende Juni", 420, 174, beim("moebel", "achtzehntausend"), fill=GELB, size=32, bis="alma"),
    *fig("AL", ALX, BODEN, FH, [("alma", "strahlt")], bis="a1"),
    *redet("AL_redet", ALX, BODEN, FH, "a1", "mathilde"),
    *fig("AL", ALX, BODEN, FH, [("mathilde", "froh")], erst="cut"),
    ns(NAME["AL"], ALX, BODEN, "alma", GRUEN, d=0.1),
    pl("tritt als Gesellschafterin ein", ALX, 330, beim("alma", "Gesellschafterin"), fill=GRUEN, size=28, anker="m", bis="a1"),
    blase("sprech", 860, 250, "a1", 1010, 250, inhalt=["Ab heute bin ich dabei! Für alte", "Rechnungen hafte ich aber nicht,",
                                                     "das haben wir so vereinbart."], textsize=32,
          figur=("AL_redet", ALX, BODEN, FH), bis="mathilde"),
    szene(ficon("tabler", "box", MAX + 150, BODEN, 120, "mathilde", fuell=HOLZ), "248karton*", 0.8, 0.05),
    pl("scheidet aus · Ruhestand", MAX, 330, beim("mathilde", "scheidet"), fill=LILA, size=28, anker="m"),
    ficon("tabler", "mail", 470, 172, 76, "rund", fuell=WEISS),
    pl("Rundschreiben an Herrn Altmann", 530, 110, "rund", fill=WEISS, size=30),
])


# ===========================================================================================================================
# A2 Juli: Konto leer, Herr Altmann an der Tür – „Dann zahlen Sie eben von Ihrem Privatkonto!“ – die Frage
# ===========================================================================================================================
def tuer(x, cue, farbe=HOLZ, w=190, h=380):
    """Bürotür aus Grundformen (Rahmen, Blatt, Klinke) auf dem Boden."""
    im, dr, s = _flaeche(w, h)
    o = 6 * s
    dr.rounded_rectangle((o, o, o + w * s, o + h * s), 8 * s, fill=farbe, outline=INK, width=5 * s)
    dr.rounded_rectangle((o + 22 * s, o + 26 * s, o + (w - 22) * s, o + 160 * s), 6 * s, outline=INK, width=4 * s)
    dr.rounded_rectangle((o + 22 * s, o + 190 * s, o + (w - 22) * s, o + (h - 26) * s), 6 * s, outline=INK, width=4 * s)
    dr.rounded_rectangle((o + 18 * s, o + 176 * s, o + 52 * s, o + 188 * s), 4 * s, fill=INK)
    im = im.resize((w + 12, h + 12), Image.LANCZOS)
    return hart(El(im, x, BODEN - h - 6, cue, "cut", 0.0, None, name="tuer"))


PHX2, ALX2, ATX2 = 1180, 910, 1640
folie([("juli", "Fall · Juli: Rechnung offen, Konto leer"), ("h1", "Fall · „Dann zahlen Sie eben privat!“"),
       ("p1", "Fall · Philipp: „Das Büro hat gekauft“"), ("frage", "Die Frage · Privatvermögen?"),
       ("frage2", "Die Frage · Und Alma und Mathilde?")], [
    *buero("juli"), tuer(1700, "juli"),
    ort("Im Architekturbüro · Juli", "juli", bis="frage"),
    ficon("tabler", "receipt-euro", 580, TISCH, 70, beim("juli", "Rechnung"), fuell=WEISS),
    pl("Rechnung: 18.000 € offen", 420, 110, beim("juli", "Rechnung"), fill=WEISS, size=30, bis="h1"),
    pl("Konto des Büros: leer", 420, 174, beim("juli", "Konto"), fill=ROT, size=30, bis="h1"),
    ficon("tabler", "pig-money", 650, TISCH, 70, beim("juli", "Konto"), fuell=HELLROT, bis="h1"),
    *fig("AL", ALX2, BODEN, FH, [("juli", "ruhig_r"), ("h1", "sorge_r"), ("frage", "denkt_r")], erst="cut"),
    hart(ns(NAME["AL"], ALX2, BODEN, "juli", GRUEN)),
    *fig("PH", PHX2, BODEN, FH, [("juli", "ruhig_r"), ("h1", "staunt_r")], bis="p1", erst="cut"),
    *redet("PH_redet_r", PHX2, BODEN, FH, "p1", "frage"),
    *fig("PH", PHX2, BODEN, FH, [("frage", "denkt_r")], erst="cut"),
    hart(ns(NAME["PH"], PHX2, BODEN, "juli", BLAU)),
    szene(fig("AT", ATX2, BODEN, FH, [(beim("juli", "leer", ende=True), "ernst")], bis="h1")[0], "248klopfen*", 0.8, 0.0),
    *redet("AT_redet", ATX2, BODEN, FH, "h1", "p1"),
    *fig("AT", ATX2, BODEN, FH, [("p1", "denkt"), ("frage", "ernst")], erst="cut"),
    ns(NAME["AT"], ATX2, BODEN, beim("juli", "leer", ende=True), GELB, d=0.1),
    blase("sprech", 760, 250, "h1", 1290, 250, inhalt=["Die 18.000 € sind seit Wochen", "fällig. Dann zahlen Sie eben",
                                                     "von Ihrem Privatkonto!"], textsize=32,
          figur=("AT_redet", ATX2, BODEN, FH), bis="p1"),
    blase("sprech", 900, 260, "p1", 1290, 250, inhalt=["Die Möbel hat doch das Büro gekauft,", "nicht ich! Und Sie schulden uns noch",
                                                     "3.000 € für die Pläne Ihrer Werkstatt."], textsize=31,
          figur=("PH_redet_r", PHX2, BODEN, FH), bis="frage"),
    pl("Muss Philipp mit seinem Privatvermögen zahlen?", 70, 30, "frage", fill=PINK, size=34),
    pl("Und haften auch Alma und Mathilde?", 70, 110, "frage2", fill=PINK, size=34),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_248(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 200
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=34, zeilenabstand=1.28)
        els += e; y += 12
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 4, cue, fill=PINK, size=30))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_248("sv", [
    "Philipp und Mathilde betreiben gemeinsam ein Architekturbüro als Gesellschaft bürgerlichen Rechts; im "
    "Gesellschaftsregister ist es nicht eingetragen. Im Februar kaufen sie für das Büro beim Tischler Herrn Altmann "
    "Arbeitstische und Regale für 18.000 €, zahlbar Ende Juni. Beide unterschreiben den Kaufvertrag für das Büro.",
    "Im März tritt Alma als dritte Gesellschafterin ein. Intern vereinbart sie mit den anderen, für alte Schulden nicht "
    "einzustehen. Ende April scheidet Mathilde aus; Herr Altmann erfährt davon durch ein Rundschreiben.",
    "Im Juli ist die Rechnung offen und das Konto des Büros leer. Herr Altmann verlangt die 18.000 € von Philipp aus "
    "dessen Privatvermögen. Das Büro hat gegen Herrn Altmann ein fälliges, noch offenes Honorar von 3.000 € für die "
    "Pläne seiner Werkstatt.",
], "Muss Philipp zahlen, und haften auch Alma und Mathilde?")


# ===========================================================================================================================
# Tafel-Helfer
# ===========================================================================================================================
def requisit(folge, px=PX, bis=None, pu=PU, py=PY):
    """Wechselndes Requisit rechts der Tafel: folge = [(cue, (set, icon, breite, fuell), pillentext, pillenfarbe)]."""
    els = []
    for i, (c, ic, txt, pf) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else bis
        if ic:
            s_, n_, br, fu = ic
            els.append(ficon(s_, n_, px, pu, br, c, fuell=fu, bis=b))
        if txt:
            els.append(pl(txt, px, py, c, fill=pf, size=28, anker="m", bis=b))
    return rechts_frei(els)


def stehend(k, x, folge, bis=None):
    els = [*fig(k, x, FB, FR, folge, bis=bis), bis_(ns(NAME[k], x, FB, folge[0][0], NFARBE[k], d=0.1), bis)]
    return rechts_frei(els, 1200)


def paar(a, af, b, bf):
    """Tafelszene: zwei Figuren rechts der Tafel (beide blicken nach links zur Tafel)."""
    return [*stehend(a, X1, af), *stehend(b, X2, bf)]


def zeitleiste(x0, x1, y, cue, punkte, farbe=INK):
    """Waagerechte Zeitleiste: punkte = [(x, oben, unten, cue, fill)] – Punkt mit Beschriftung oben/unten (26–28 px)."""
    els = [linienzug([(x0, y), (x1 - 30, y)], cue, breite=6, farbe=farbe), pfeil(x1 - 60, y, x1, y, cue, breite=6, kopf=24)]
    for x, oben, unten, c, fu in punkte:
        els.append(feld(x - 14, y - 14, 28, 28, c, fill=fu, rand=4, rund=14, anim="pop", name="zeitpunkt"))
        if oben:
            els.append(pl(oben, x, y - 92, c, fill=fu, size=28, anker="m"))
        if unten:
            els.append(z(unten, x - F("Bold", 28).getlength(glyphen(unten)) / 2, y + 26, c, "Bold", 28, rechts=1175))
    return els


# ===========================================================================================================================
# C I. Schuldnerin ist die GbR (§ 705 Abs. 2, § 433 Abs. 2 BGB; Verweis Folge 173)
# ===========================================================================================================================
PI = "I. Schuld der Gesellschaft"
folie([("gbr", f"{PI} · Wer schuldet?"), ("rf", f"{PI} › rechtsfähige GbR, § 705 Abs. 2 BGB"),
       ("v173", f"{PI} › Verweis: Video zur GbR"), ("schuld", f"{PI} › Käuferin: die GbR, § 433 Abs. 2 BGB")], [
    *tafel("gbr", "I. Wer schuldet?"),
    z("Das Büro soll am Rechtsverkehr teilnehmen:", 110, 190, "rf", "Bold", 36),
    *okz("rechtsfähige Gesellschaft, § 705 Abs. 2 BGB", 260, beim("rf", "rechtsfähige"), "Bold", 36),
    blk(110, 340, 1040, 90, LILAHELL, "v173", [("Wie sie entsteht: Video „GbR nach MoPeG“", "ExtraBold", 33, INK)]),
    blk(110, 480, 1040, 140, GELB, "schuld", [("Käuferin ist die Gesellschaft selbst:", "ExtraBold", 34, INK),
                                            ("18.000 € aus § 433 Abs. 2 BGB", "ExtraBold", 34, INK)]),
    *requisit([("gbr", ("tabler", "help-circle", 110, WEISS), "Wer schuldet?", WEISS),
               ("rf", ("tabler", "users-group", 140, LILA), "rechtsfähige GbR", LILA),
               ("schuld", ("tabler", "receipt-euro", 120, GELB), "18.000 €", GELB)], px=1560, pu=330, py=90),
    *paar("PH", [("gbr", "ruhig"), ("schuld", "ernst")], "AL", [("gbr", "ruhig"), ("rf", "denkt")]),
])

# ===========================================================================================================================
# D II. § 721 BGB (Wortlautkarte), Rechtsstand MoPeG (BGH II ZR 331/00, Leitsatz c; BT-Drs. 19/27635, S. 165)
# ===========================================================================================================================
PII = "II. Haftung, § 721 BGB"
w721, w721_y = wortlaut(80, 180, 1100, "„Die Gesellschafter haften für die Verbindlichkeiten der Gesellschaft den Gläubigern "
                                       "als Gesamtschuldner persönlich. Eine entgegenstehende Vereinbarung ist Dritten "
                                       "gegenüber unwirksam.“", "§ 721 BGB", "w721",
                        marken=[("Verbindlichkeiten der Gesellschaft", beim("w721", "Verbindlichkeiten")),
                                ("als Gesamtschuldner", beim("w721", "Gesamtschuldner")), ("persönlich", beim("w721", "persönlich")),
                                ("unwirksam", beim("satz2", "unwirksam"))])
folie([("p721", f"{PII} · Und die Gesellschafter?"), ("w721", f"{PII} › Satz 1: persönlich, als Gesamtschuldner"),
       ("satz2", f"{PII} › Satz 2: Abreden Dritten gegenüber unwirksam"), ("frueher", f"{PII} › seit 1.1.2024 im Gesetz")], [
    *tafel("p721", "II. Haftung der Gesellschafter"),
    *w721,
    blk(110, w721_y + 30, 1040, 140, BLAUHELL, "frueher", [("früher: entsprechend dem OHG-Recht", "ExtraBold", 33, INK),
                                                         ("(§§ 128–130 HGB a. F.)", "Bold", 30, INK)]),
    zit("BGH, Urt. v. 29.1.2001 – II ZR 331/00, Leitsatz c", 110, w721_y + 186, "frueher"),
    blk(110, w721_y + 240, 1040, 90, HELLGRUEN, beim("frueher", "seit"), [("seit 1.1.2024 ausdrücklich im Gesetz (MoPeG)", "ExtraBold", 33, INK)]),
    *requisit([("p721", ("tabler", "users", 130, WEISS), "Gesellschafter?", WEISS),
               ("w721", ("tabler", "scale", 120, GELB), "§ 721 BGB", GELB),
               ("frueher", ("tabler", "calendar-event", 120, BLAUHELL), "1.1.2024", BLAUHELL)]),
    *stehend("PH", FX, [("p721", "ruhig"), ("w721", "sorge"), ("frueher", "denkt")]),
])
assert w721_y + 340 <= 900, w721_y

# ===========================================================================================================================
# E II. Merkmale der Haftung (BT-Drs. 19/27635, S. 165 f.; BGH II ZR 331/00, S. 23 f.; § 421 BGB; Verweis Folge 120)
# ===========================================================================================================================
folie([("merk", f"{PII} › Was heißt das?"), ("pers", f"{PII} › persönlich: Privatvermögen"),
       ("unbe", f"{PII} › unbeschränkt"), ("prim", f"{PII} › unmittelbar und primär"),
       ("gesamt", f"{PII} › als Gesamtschuldner, § 421 BGB"), ("akz", f"{PII} › akzessorisch")], [
    *tafel("merk", "II. Wie haftet Philipp?"),
    *okz("persönlich: mit seinem Privatvermögen", 180, "pers", "Bold", 35),
    *okz("unbeschränkt: ohne Höchstbetrag", 260, "unbe", "Bold", 35),
    *okz("unmittelbar und primär: direkt an Philipp,", 340, "prim", "Bold", 35),
    z("nicht zuerst die Gesellschaft verklagen", 185, 388, beim("prim", "nicht"), "Bold", 35),
    *okz("als Gesamtschuldner: jeder die ganze Summe,", 468, "gesamt", "Bold", 35),
    z("Herr Altmann bekommt sie nur einmal, § 421 BGB", 185, 516, beim("gesamt", "Herr"), "Bold", 35),
    pl("Video „Gesamtschuld“", 185, 580, "v120", fill=LILAHELL, size=28),
    *okz("akzessorisch: folgt Bestand und Inhalt", 660, "akz", "Bold", 35),
    z("der Schuld der Gesellschaft", 185, 708, beim("akz", "Bestand"), "Bold", 35),
    zit("BT-Drs. 19/27635, S. 165 f.; BGH, Urt. v. 29.1.2001 – II ZR 331/00", 110, 790, "akz"),
    *requisit([("merk", ("tabler", "help-circle", 110, WEISS), "Wie?", WEISS),
               ("pers", ("tabler", "wallet", 130, BLAU), "Privatvermögen", BLAU),
               ("unbe", ("tabler", "infinity", 140, GELB), "ohne Höchstbetrag", GELB),
               ("prim", ("tabler", "arrow-right", 120, WEISS), "direkt", WEISS),
               ("gesamt", ("tabler", "users", 130, GRUEN), "jeder das Ganze", GRUEN),
               ("akz", ("tabler", "link", 120, LILA), "akzessorisch", LILA)], px=1560, pu=330, py=90),
    *paar("PH", [("merk", "ruhig"), ("pers", "sorge"), ("gesamt", "ernst")], "AT", [("merk", "ruhig"), ("prim", "froh"), ("akz", "denkt")]),
])

# ===========================================================================================================================
# F III. Eintritt: Alma, § 721a BGB (Wortlautkarte)
# ===========================================================================================================================
PIII = "III. Eintritt: Alma, § 721a BGB"
w721a, w721a_y = wortlaut(80, 180, 1100, "„Wer in eine bestehende Gesellschaft eintritt, haftet gleich den anderen "
                                         "Gesellschaftern nach Maßgabe der §§ 721 und 721b für die vor seinem Eintritt "
                                         "begründeten Verbindlichkeiten der Gesellschaft. Eine entgegenstehende Vereinbarung "
                                         "ist Dritten gegenüber unwirksam.“", "§ 721a BGB", "w721a",
                          marken=[("eintritt", beim("w721a", "eintritt")), ("Eintritt begründeten", beim("w721a", "begründeten")),
                                  ("unwirksam", beim("abr", "unwirksam"))])
folie([("eintr", f"{PIII} · Nun zu Alma"), ("w721a", f"{PIII} › Altschulden"), ("alt", f"{PIII} › Kauf im Februar, Eintritt im März"),
       ("abr", f"{PIII} › interne Abrede: Dritten gegenüber unwirksam"), ("afall", f"{PIII} › Alma haftet mit (+)")], [
    *tafel("eintr", "III. Eintritt: Alma"),
    *w721a,
    *zeitleiste(150, 1130, w721a_y + 120, "alt", [(330, "Februar", "Kauf: 18.000 €", "alt", GELB),
                                                 (760, "März", "Alma tritt ein", beim("alt", "Alma"), GRUEN)]),
    *okz("Altschuld", w721a_y + 200, beim("alt", "Altschuld"), "ExtraBold", 35, x=930, rechts=1170),
    *neinz("interne Abrede: Dritten gegenüber unwirksam, Satz 2", w721a_y + 270, "abr", "Bold", 33, kreuz=beim("abr", "unwirksam")),
    blk(110, w721a_y + 340, 1040, 80, HELLGRUEN, "afall", [("Alma haftet mit: 18.000 €", "ExtraBold", 34, INK)]),
    *requisit([("eintr", ("tabler", "user-plus", 130, GRUEN), "Eintritt", GRUEN),
               ("alt", ("tabler", "receipt-euro", 120, GELB), "Altschuld", GELB),
               ("abr", ("tabler", "file-x", 120, HELLROT), "Abrede unwirksam", HELLROT)]),
    *stehend("AL", FX, [("eintr", "froh"), ("w721a", "staunt"), ("abr", "sorge"), ("afall", "ernst")]),
])
assert w721a_y + 430 <= 900, w721a_y

# ===========================================================================================================================
# G1 IV. Einwendungen: § 721b Abs. 1 BGB (Wortlautkarte)
# ===========================================================================================================================
PIV = "IV. Einwendungen, § 721b BGB"
w721b1, w721b1_y = wortlaut(80, 180, 1100, "„(1) Wird ein Gesellschafter wegen einer Verbindlichkeit der Gesellschaft in "
                                           "Anspruch genommen, kann er Einwendungen und Einreden, die nicht in seiner Person "
                                           "begründet sind, insoweit geltend machen, als sie von der Gesellschaft erhoben "
                                           "werden können.“", "§ 721b Abs. 1 BGB", "w721b",
                            marken=[("Einwendungen", beim("w721b", "Einwendungen")), ("Einreden", beim("w721b", "Einreden")),
                                    ("von der Gesellschaft erhoben", beim("w721b", "Gesellschaft"))])
folie([("einw", f"{PIV} · Kann Philipp sich wehren?"), ("w721b", f"{PIV} › Abs. 1: Einwendungen der Gesellschaft")], [
    *tafel("einw", "IV. Kann Philipp sich wehren?"),
    *w721b1,
    z("etwa:", 110, w721b1_y + 40, beim("w721b", "etwa"), "Bold", 35),
    pl("Erfüllung", 230, w721b1_y + 32, beim("w721b", "Erfüllung"), fill=GRUEN, size=32),
    pl("Verjährung", 450, w721b1_y + 32, beim("w721b", "Verjährung"), fill=BLAUHELL, size=32),
    *requisit([("einw", ("tabler", "shield", 120, WEISS), "Verteidigung?", WEISS),
               ("w721b", ("tabler", "shield", 120, GRUEN), "wie die GbR", GRUEN)]),
    *stehend("PH", FX, [("einw", "denkt"), ("w721b", "ruhig")]),
])

# ===========================================================================================================================
# G2 IV. § 721b Abs. 2 BGB (Wortlautkarte): Aufrechnungsrecht der Gesellschaft (§§ 387, 389 BGB)
# ===========================================================================================================================
w721b2, w721b2_y = wortlaut(80, 180, 1100, "„(2) Der Gesellschafter kann die Befriedigung des Gläubigers verweigern, solange "
                                           "der Gesellschaft in Ansehung der Verbindlichkeit das Recht zur Anfechtung oder "
                                           "Aufrechnung oder ein anderes Gestaltungsrecht, dessen Ausübung die Gesellschaft "
                                           "ihrerseits zur Leistungsverweigerung berechtigen würde, zusteht.“",
                            "§ 721b Abs. 2 BGB", "abs2", size=31,
                            marken=[("Befriedigung des Gläubigers verweigern", beim("abs2", "Befriedigung")),
                                    ("Anfechtung oder", beim("abs2", "Anfechtung")), ("Aufrechnung", beim("abs2", "Aufrechnung"))])
folie([("abs2", f"{PIV} › Abs. 2: Leistungsverweigerung"), ("aufr", f"{PIV} › Aufrechnung mit 3.000 € Honorar"),
       ("verw", f"{PIV} › 3.000 € verweigern"), ("rest", f"{PIV} › offen: 15.000 €")], [
    *tafel("abs2", "IV. Kann Philipp sich wehren?"),
    *w721b2,
    *okz("hier: Aufrechnung mit fälligem Honorar, 3.000 €", w721b2_y + 34, "aufr", "Bold", 34),
    *okz("in dieser Höhe: Zahlung verweigern", w721b2_y + 104, "verw", "Bold", 34),
    blk(110, w721b2_y + 180, 1040, 90, GELB, "rest", [("18.000 € − 3.000 € = 15.000 € offen", "ExtraBold", 35, INK)]),
    *requisit([("abs2", ("tabler", "hand-stop", 120, WEISS), "verweigern", WEISS),
               ("aufr", ("tabler", "arrows-exchange", 130, GELB), "Honorar 3.000 €", GELB),
               ("rest", ("tabler", "receipt-euro", 120, GELB), "15.000 €", GELB)], px=1560, pu=330, py=90),
    *paar("PH", [("abs2", "ruhig"), ("verw", "froh")], "AT", [("abs2", "ruhig"), ("aufr", "denkt"), ("rest", "ernst")]),
])
assert w721b2_y + 280 <= 900, w721b2_y

# ===========================================================================================================================
# H1 V. Ausgeschieden: Mathilde, § 728b BGB (Wortlautkarte)
# ===========================================================================================================================
PV = "V. Ausgeschieden: Mathilde, § 728b BGB"
w728b, w728b_y = wortlaut(80, 180, 1100, "„(1) Scheidet ein Gesellschafter aus der Gesellschaft aus, so haftet er für deren "
                                         "bis dahin begründete Verbindlichkeiten, wenn sie vor Ablauf von fünf Jahren nach "
                                         "seinem Ausscheiden fällig sind und 1. daraus Ansprüche gegen ihn in einer in § 197 "
                                         "Absatz 1 Nummer 3 bis 5 bezeichneten Art festgestellt sind oder 2. eine gerichtliche "
                                         "oder behördliche Vollstreckungshandlung vorgenommen oder beantragt wird; …“",
                          "§ 728b Abs. 1 Satz 1 BGB", "w728b", size=31,
                          marken=[("bis dahin begründete", beim("w728b", "bis")), ("fünf Jahren", beim("w728b", "fünf")),
                                  ("festgestellt", beim("fest", "festgestellt")), ("Vollstreckungshandlung", beim("fest", "Vollstreckungshandlung"))])
folie([("aus", f"{PV} · Mathilde ist ausgeschieden"), ("w728b", f"{PV} › fällig binnen 5 Jahren"),
       ("fest", f"{PV} › festgestellt, etwa durch Urteil")], [
    *tafel("aus", "V. Und Mathilde?"),
    *w728b,
    *okz("festgestellt: etwa durch Urteil, § 197 Abs. 1 Nr. 3 BGB", w728b_y + 34, beim("fest", "Urteil"), "Bold", 33),
    *requisit([("aus", ("tabler", "user-minus", 130, LILA), "ausgeschieden", LILA),
               ("w728b", ("tabler", "hourglass", 110, GELB), "5 Jahre", GELB),
               ("fest", ("tabler", "file-certificate", 120, WEISS), "Urteil", WEISS)]),
    *stehend("MA", FX, [("aus", "ruhig"), ("w728b", "denkt"), ("fest", "ernst")]),
])
assert w728b_y + 90 <= 900, w728b_y

# ===========================================================================================================================
# H2 V. Zeitleiste Mathilde: Frist ab Kenntnis (§ 728b Abs. 1 Satz 3), Altverbindlichkeit (BGH II ZR 197/10 Rn. 14)
# ===========================================================================================================================
folie([("frist", f"{PV} › Frist ab Kenntnis: Rundschreiben"), ("mfall", f"{PV} › begründet vor dem Ausscheiden, fällig Ende Juni"),
       ("mfall2", f"{PV} › rechtzeitige Klage: Mathilde haftet (+)")], [
    *tafel("frist", "V. Mathilde: die Zeitleiste"),
    z("nicht eingetragene GbR: Frist ab Kenntnis", 110, 180, "frist", "Bold", 35),
    z("des Gläubigers, § 728b Abs. 1 Satz 3 BGB", 110, 228, beim("frist", "Gläubiger"), "Bold", 35),
    *zeitleiste(130, 1140, 420, "frist", [(260, "Februar", "Kauf", beim("mfall", "Kauf"), GELB),
                                         (500, "Ende April", "Ausscheiden", beim("mfall", "Ausscheiden"), LILA),
                                         (740, "Rundschreiben", "Fristbeginn", beim("frist", "Rundschreiben"), WEISS),
                                         (980, "Ende Juni", "fällig", beim("mfall", "fällig"), ROT)]),
    *okz("begründet vor dem Ausscheiden", 560, beim("mfall", "begründet"), "Bold", 34),
    *okz("fällig Ende Juni: innerhalb der 5 Jahre", 620, beim("mfall", "fällig"), "Bold", 34),
    zit("BGH, Urt. v. 17.1.2012 – II ZR 197/10, Rn. 14 (Altverbindlichkeit)", 185, 672, beim("mfall", "begründet")),
    blk(110, 730, 1040, 90, HELLGRUEN, "mfall2", [("rechtzeitige Klage: auch Mathilde haftet", "ExtraBold", 34, INK)]),
    *requisit([("frist", ("tabler", "mail", 120, WEISS), "Rundschreiben", WEISS),
               ("mfall", ("tabler", "calendar-event", 120, ROT), "fällig Ende Juni", ROT),
               ("mfall2", ("tabler", "file-certificate", 120, HELLGRUEN), "Klage", HELLGRUEN)]),
    *stehend("MA", FX, [("frist", "ruhig"), ("mfall", "denkt"), ("mfall2", "staunt")]),
])

# ===========================================================================================================================
# I VI. Vollstreckung: § 722 Abs. 2 BGB (Wortlautkarte; BT-Drs. 19/27635, S. 169; BGH II ZR 331/00, S. 23)
# ===========================================================================================================================
PVI = "VI. Vollstreckung, § 722 Abs. 2 BGB"
w722, w722_y = wortlaut(80, 180, 1100, "„(2) Aus einem gegen die Gesellschaft gerichteten Vollstreckungstitel findet die "
                                       "Zwangsvollstreckung gegen die Gesellschafter nicht statt.“", "§ 722 Abs. 2 BGB", "w722",
                        marken=[("gegen die Gesellschaft gerichteten", beim("w722", "Gesellschaft")),
                                ("gegen die Gesellschafter nicht statt", beim("w722", "Gesellschafter"))])
folie([("vollstr", f"{PVI} · Wie kommt Herr Altmann ans Geld?"), ("w722", f"{PVI} › Titel gegen die GbR reicht nicht"),
       ("titel", f"{PVI} › Titel gegen Philipp selbst"), ("beide", f"{PVI} › GbR und Gesellschafter zusammen verklagen")], [
    *tafel("vollstr", "VI. Vollstreckung"),
    *w722,
    *neinz("Titel nur gegen die GbR: nicht ins Privatkonto", w722_y + 34, beim("w722", "nicht"), "Bold", 34),
    *okz("Privatkonto: Titel gegen Philipp selbst", w722_y + 104, "titel", "Bold", 34),
    blk(110, w722_y + 190, 1040, 140, GELB, "beide", [("am besten: die Gesellschaft und die", "ExtraBold", 34, INK),
                                                    ("Gesellschafter zusammen verklagen", "ExtraBold", 34, INK)]),
    zit("BT-Drs. 19/27635, S. 169; BGH, Urt. v. 29.1.2001 – II ZR 331/00 (S. 23)", 110, w722_y + 346, "beide"),
    *requisit([("vollstr", ("tabler", "building-bank", 130, BLAUHELL), "Privatkonto?", BLAUHELL),
               ("titel", ("tabler", "file-certificate", 120, WEISS), "Titel gegen Philipp", WEISS),
               ("beide", ("tabler", "users-group", 140, GELB), "alle verklagen", GELB)], px=1560, pu=330, py=90),
    *paar("PH", [("vollstr", "ruhig"), ("titel", "sorge")], "AT", [("vollstr", "ernst"), ("beide", "denkt")]),
])
assert w722_y + 380 <= 900, w722_y

# ===========================================================================================================================
# J VII. Innenausgleich (§ 716 Abs. 1, § 426 BGB; BGH II ZR 310/12 Rn. 34 f.; BT-Drs. 19/27635, S. 157, 166)
# ===========================================================================================================================
PVII = "VII. Innenausgleich"
folie([("innen", f"{PVII} · Und wenn Philipp zahlt?"), ("p716", f"{PVII} › Ersatz von der GbR, § 716 Abs. 1 BGB"),
       ("p426", f"{PVII} › Mitgesellschafter nur nachrangig, § 426 BGB"), ("abr2", f"{PVII} › hier zählt die Abrede mit Alma")], [
    *tafel("innen", "VII. Und wenn Philipp zahlt?"),
    *okz("Ersatz von der Gesellschaft, § 716 Abs. 1 BGB", 190, "p716", "Bold", 35),
    zit("BT-Drs. 19/27635, S. 157, 166", 185, 240, "p716"),
    *okz("von den Mitgesellschaftern: nur, wenn von der", 320, "p426", "Bold", 35),
    z("Gesellschaft nichts zu bekommen ist, § 426 BGB", 185, 368, beim("p426", "Gesellschaft"), "Bold", 35),
    zit("BGH, Urt. v. 8.10.2013 – II ZR 310/12, Rn. 34 f.", 185, 418, beim("p426", "Gesellschaft")),
    blk(110, 500, 1040, 140, LILAHELL, "abr2", [("erst im Innenverhältnis zählt", "ExtraBold", 34, INK),
                                              ("die Abrede mit Alma", "ExtraBold", 34, INK)]),
    *requisit([("innen", ("tabler", "cash-banknote", 140, GRUEN), "Philipp zahlt", GRUEN),
               ("p716", ("tabler", "arrow-back-up", 120, WEISS), "Ersatz von der GbR", WEISS),
               ("abr2", ("tabler", "file-text", 120, LILAHELL), "Abrede intern", LILAHELL)], px=1560, pu=330, py=90),
    *paar("PH", [("innen", "ruhig"), ("p716", "froh")], "AL", [("innen", "ruhig"), ("abr2", "froh")]),
])

# ===========================================================================================================================
# K Ergebnis: zurück im Büro
# ===========================================================================================================================
PHX3, ALX3, ATX3 = 1180, 910, 1640
folie([("erg", "Ergebnis · 15.000 € von Philipp persönlich"), ("erg2", "Ergebnis › 3.000 € verweigern, solange aufgerechnet werden kann"),
       ("erg3", "Ergebnis › ebenso Alma und Mathilde")], [
    *buero("erg"), tuer(1700, "erg"),
    *okz("Philipp: 15.000 € persönlich, § 433 Abs. 2, § 721 Satz 1 BGB", 40, beim("erg", "fünfzehntausend"), "Bold", 31,
         x=130, rechts=1880),
    *okz("3.000 € verweigern, solange die GbR aufrechnen kann", 100, "erg2", "Bold", 31, x=130, rechts=1880),
    *okz("ebenso: Alma (§ 721a) und, bei rechtzeitiger Klage, Mathilde (§ 728b)", 160, "erg3", "Bold", 31, x=130, rechts=1880),
    *fig("AL", ALX3, BODEN, FH, [("erg", "ruhig_r"), ("erg3", "ernst_r")], erst="cut"),
    hart(ns(NAME["AL"], ALX3, BODEN, "erg", GRUEN)),
    *fig("PH", PHX3, BODEN, FH, [("erg", "ernst_r"), ("erg2", "froh_r")], erst="cut"),
    hart(ns(NAME["PH"], PHX3, BODEN, "erg", BLAU)),
    *fig("AT", ATX3, BODEN, FH, [("erg", "froh"), ("erg2", "denkt")], erst="cut"),
    hart(ns(NAME["AT"], ATX3, BODEN, "erg", GELB)),
    ficon("tabler", "cash-banknote", 1410, 420, 120, beim("erg", "fünfzehntausend"), fuell=GRUEN),
])

# ===========================================================================================================================
# L Klausurtipp (Lexi; BGH II ZR 197/10 Rn. 14)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Zeitleiste je Gesellschafter"), ("tipp2", "Klausurtipp · Wann wurde die Schuld begründet?"),
       ("tipp3", "Klausurtipp · vor Eintritt § 721a, vor Ausscheiden § 728b")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Zeichne für jeden Gesellschafter", 200, 200, "tipp", "Bold", 35),
    z("eine Zeitleiste.", 200, 250, beim("tipp", "Zeitleiste"), "Bold", 35),
    z("Entscheidend: Wann wurde die Verbindlichkeit", 200, 330, "tipp2", "Bold", 34),
    z("begründet, also ihre Rechtsgrundlage gelegt?", 200, 378, beim("tipp2", "Rechtsgrundlage"), "Bold", 34),
    z("auch wenn sie erst später fällig wird", 200, 426, beim("tipp2", "auch"), "Regular", 32),
    zit("BGH, Urt. v. 17.1.2012 – II ZR 197/10, Rn. 14", 200, 474, beim("tipp2", "auch")),
    blk(130, 560, 1000, 80, GRUEN, "tipp3", [("vor dem Eintritt begründet: § 721a BGB", "ExtraBold", 32, INK)]),
    blk(130, 670, 1000, 80, LILA, beim("tipp3", "liegt", 2), [("vor dem Ausscheiden begründet: § 728b BGB", "ExtraBold", 32, INK)]),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# M Prüfungsschema
# ===========================================================================================================================
REIHEN = [("s1", 0, "1. Verbindlichkeit der rechtsfähigen Gesellschaft", True),
          (beim("s1", "hier"), 1, "hier: Kaufpreis, § 433 Abs. 2 BGB", False),
          ("s2", 0, "2. Gesellschafterstellung", True),
          (beim("s2", "beim"), 1, "Eintritt: § 721a BGB", False),
          (beim("s2", "nach"), 1, "nach dem Ausscheiden: Grenzen des § 728b BGB", False),
          ("s3", 0, "3. Rechtsfolge, § 721 BGB", True),
          (beim("s3", "persönliche"), 1, "persönlich, unbeschränkt, als Gesamtschuldner", False),
          ("s4", 0, "4. Einwendungen und Einreden, § 721b BGB", True),
          ("s5", 0, "Vollstreckung: Titel gegen den Gesellschafter selbst, § 722 Abs. 2 BGB", True)]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfungsschema: Haftung des Gesellschafters, § 721 BGB"), 110, 90, "sch", 44)]
y = 195
for c, ebene, text, fett in REIHEN:
    x = (130, 200)[ebene]
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 40 if ebene == 0 else 36, rechts=1800))
    y += {0: 84, 1: 74}[ebene]
assert y <= 975, y
folie([("sch", "Prüfungsschema"), ("s1", "Prüfungsschema › 1. Verbindlichkeit der GbR"),
       ("s2", "Prüfungsschema › 2. Gesellschafterstellung"), ("s3", "Prüfungsschema › 3. Rechtsfolge"),
       ("s4", "Prüfungsschema › 4. Einwendungen und Einreden"), ("s5", "Prüfungsschema › Vollstreckung")], els_sch)

# ===========================================================================================================================
# N Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Für die Schulden der Gesellschaft", 0)], [("haftet jeder Gesellschafter", 0)],
                 [("persönlich", "a"), (" und ", 0), ("unbeschränkt", "b"), (".", 0)]],
                750, 270, 44, "merke", {"a": beim("merke", "persönlich"), "b": beim("merke", "unbeschränkt")}),
    *markertext([[("Wer eintritt, haftet auch für ", 0), ("Altschulden", "c"), (";", 0)],
                 [("wer ausscheidet, nur noch in den", 0)], [("Grenzen der ", 0), ("Fünfjahresfrist", "d"), (".", 0)]],
                750, 560, 42, "merk2", {"c": beim("merk2", "Altschulden"), "d": beim("merk2", "Fünfjahresfrist")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
