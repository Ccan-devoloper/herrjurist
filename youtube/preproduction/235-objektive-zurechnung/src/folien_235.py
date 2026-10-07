"""Folge 235 · Objektive Zurechnung: Der Neffe, das Gewitter und der Blitz – Serienstandard Open Peeps (Katzenkönig).
Fiktiver Fall (Gewitterfall, Lehrbuchklassiker): Hildegard (Mitte 70, wohlhabend) auf ihrer Terrasse am Waldrand, Neffe Rupert
(einziger Erbe) sieht eine Unwetterwarnung, rät ihr zum Spaziergang im Wald und hofft auf einen Blitz. Im Wald bricht das
Gewitter los, ein Blitz trifft sie tödlich (nur als Symbol; harter Schnitt, keine Leiche, keine Verletzung). Danach § 212 Abs. 1
(Wortlautkarte), Mord kurz; Erfolg, Kausalität (BGH 3 StR 394/20 Rn. 5); objektive Zurechnung (Lehre); Gewitterfall:
allgemeines Lebensrisiko, nicht beherrschbar; Weg der Rechtsprechung über den Vorsatz (3 StR 394/20 Rn. 8); Abwandlung;
§ 222 (Wortlautkarte, 4 StR 19/20 Rn. 21); Fallgruppen; Klausurtipp, Schema, Merksatz mit Lexi.
Szenen laut ../SZENENPLAN.md. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/feld/requisit als eigene
Kopie aus Folge 231 (gemeinsame Dateien unverändert); neu: gewitterfolie(), weg(), tisch().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut StGB nach gesetze-im-internet.de, Abruf 07.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_235/"

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
LILAHELL = (246, 243, 255, 255)
BLAUHELL = (228, 238, 253, 255)
HELLGRAU = (226, 226, 222, 255)
TUERKIS_ = (127, 214, 208, 255)
HOLZ = (214, 160, 110, 255)
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
        if n.startswith(("bild:", "ficon:")) or "/op_235/" in n:
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
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 07.10.2026), als Zitat mit Normangabe; der
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 160/203) -------------------------------------
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
NAME = {"HI": "Hildegard", "RU": "Rupert"}
NFARBE = {"HI": LILA, "RU": TUERKIS_}
WAND = (246, 236, 220, 255)


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


# --- Folge 235: Größen, Gewitterhimmel, Terrassen- und Waldbausteine --------------------------------------------------------
GROESSE = {"HI": 0.93, "RU": 1.0}         # Hildegard etwas kleiner als Rupert


def hh(k, h):
    return round(h * GROESSE[k])


def stehend(k, x, folge, bis=None):
    els = [*fig(k, x, FB, hh(k, FR), folge, bis=bis), bis_(ns(NAME[k], x, FB, folge[0][0], NFARBE[k], d=0.1), bis)]
    return rechts_frei(els, 1200)


BG_FARBE["gewitter"] = None                  # Gewitterhimmel = grauer Verlauf, erzeugt im Renderer
PFAD_FARBE["gewitter"] = (255, 255, 255, 190)


def gewitterfolie(pfade, els):
    """Waldszene im Gewitter: grauer Himmel, weil das Unwetter den Fall trägt (Begründung im Szenenplan)."""
    pruefe_im_bild(els)
    FOLIEN.append(dict(bg="gewitter", pfade=pfade, els=els))


WALDWEG = (196, 170, 128, 255)


def weg(cue, farbe=WALDWEG):
    im = Image.new("RGBA", (1840, 60))
    ImageDraw.Draw(im).rectangle((0, 0, 1840, 60), fill=farbe)
    return El(im, 40, BODEN, cue, "cut", 0.0, None, name="weg")


def tisch(x, cue, breite=200, hoehe=150):
    """Terrassentisch: Platte und zwei Beine (Tuschekontur)."""
    return [hart(feld(x, BODEN - hoehe, breite, 22, cue, fill=HOLZ, rand=4, rund=6, name="tischplatte")),
            hart(linienzug([(x + 30, BODEN - hoehe + 22), (x + 30, BODEN)], cue, breite=6, farbe=INK)),
            hart(linienzug([(x + breite - 30, BODEN - hoehe + 22), (x + breite - 30, BODEN)], cue, breite=6, farbe=INK))]


# ===========================================================================================================================
# A1 Fall: Terrasse am Waldrand – Hildegard, Rupert, Unwetterwarnung, Rat zum Spaziergang
# ===========================================================================================================================
RUX, HIX0, HIX1 = 760, 1080, 1330
FH_ = {k: hh(k, FH) for k in GROESSE}
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
GEH = beim("wald", "spaziert"), beim("wald", "Wald", ende=True)
folie([(NULL, "Fall · Ein Sommernachmittag am Waldrand"), ("hildegard", "Fall · Hildegard auf ihrer Terrasse"),
       ("rupert", "Fall · Neffe Rupert, der einzige Erbe"), ("warn", "Fall · Unwetterwarnung"),
       ("ru1", "Fall · Der Rat zum Spaziergang"), ("hofft", "Fall · Rupert hofft insgeheim"),
       ("wald", "Fall · Hildegard geht in den Wald")], [
    boden(NULL),
    hart(ficon("tabler", "home", 220, BODEN + 4, 360, NULL, fuell=GELB, anim="cut")),
    *tisch(430, NULL),
    hart(ficon("tabler", "mug", 520, BODEN - 172, 54, NULL, fuell=WEISS, anim="cut")),
    hart(ficon("tabler", "trees", 1560, BODEN + 4, 280, NULL, fuell=GRUEN, anim="cut")),
    hart(ficon("tabler", "tree", 1790, BODEN + 4, 170, NULL, fuell=GRUEN, anim="cut")),
    hart(ficon("tabler", "sun", 1800, 170, 100, NULL, fuell=GELB, anim="cut")),
    bis_(hart(pl("Ein schwüler Sommernachmittag am Waldrand", 70, 30, NULL, fill=GELB, size=32)), "hildegard"),
    # Hildegard: zuerst auf der Terrasse (Blick zu Rupert), redet, dreht sich zum Wald und spaziert los
    *fig("HI", HIX0, BODEN, FH_["HI"], [(NULL, "geniesst"), ("rupert", "froh"), ("warn", "ruhig"),
                                        ("ru1", "froh")], bis="hi1"),
    *redet("HI_redet", HIX0, BODEN, FH_["HI"], "hi1", "hofft"),
    *fig("HI", HIX0, BODEN, FH_["HI"], [("hofft", "froh")], bis=GEH[0], erst="cut"),
    bewegt(peep_voll("HI_froh_r", HIX1, BODEN, FH_["HI"], GEH[0], anim="cut"), GEH[0], GEH[1], -(HIX1 - HIX0)),
    bis_(ns(NAME["HI"], HIX0, BODEN, NULL, NFARBE["HI"], anim="cut"), GEH[0]),
    bewegt(ns(NAME["HI"], HIX1, BODEN, GEH[0], NFARBE["HI"], anim="cut"), GEH[0], GEH[1], -(HIX1 - HIX0)),
    bis_(pl("Hildegard, eine wohlhabende Witwe, Mitte 70", 70, 30, "hildegard", fill=LILA, size=32), "rupert"),
    bis_(pl("trinkt Kaffee auf ihrer Terrasse", 70, 94, beim("hildegard", "Kaffee"), fill=WEISS, size=30), "rupert"),
    # Rupert: kommt zu Besuch, Handy mit Unwetterwarnung, redet, denkt
    *fig("RU", RUX, BODEN, FH_["RU"], [("rupert", "ruhig_r"), ("warn", "ernst_r")], bis="ru1"),
    *redet("RU_redet_r", RUX, BODEN, FH_["RU"], "ru1", "hi1"),
    *fig("RU", RUX, BODEN, FH_["RU"], [("hi1", "froh_r"), ("hofft", "denkt_r"), ("wald", "ruhig_r")], erst="cut"),
    ns(NAME["RU"], RUX, BODEN, "rupert", NFARBE["RU"], d=0.1),
    bis_(pl("Ihr Neffe Rupert ist zu Besuch.", 70, 30, "rupert", fill=TUERKIS_, size=32), "warn"),
    bis_(pl("Er ist ihr einziger Erbe.", 70, 94, beim("rupert", "Er"), fill=WEISS, size=30), "warn"),
    bis_(ficon("tabler", "moneybag", 920, 330, 70, beim("rupert", "Erbe"), fuell=GELB), "warn"),
    bis_(ficon("tabler", "device-mobile", 930, 360, 70, "warn", fuell=BLAU), "ru1"),
    bis_(ficon("tabler", "alert-triangle", 930, 280, 54, beim("warn", "Unwetterwarnung"), fuell=ROT), "ru1"),
    bis_(pl("Unwetterwarnung: Ein Gewitter zieht auf.", 70, 30, beim("warn", "Unwetterwarnung"), fill=ROT, size=32), "ru1"),
    ficon("tabler", "cloud-storm", 1690, 250, 110, beim("warn", "Gewitter"), fuell=HELLGRAU),
    blase("sprech", 700, 250, "ru1", 1080, 220, inhalt=["Tante Hildegard, geh doch noch", "ein Stück in den Wald.",
                                                       "Die Luft ist so schön!"], textsize=32,
          figur=("RU_redet_r", RUX, BODEN, FH_["RU"]), bis="hi1"),
    blase("sprech", 500, 170, "hi1", 1340, 230, inhalt=["Gute Idee.", "Bis später, Rupert!"], textsize=34,
          figur=("HI_redet", HIX0, BODEN, FH_["HI"]), bis="hofft"),
    blase("denk", 400, 170, "hofft", 640, 250, inhalt=["Ein Blitz …?"], textsize=36,
          figur=("RU_denkt_r", RUX, BODEN, FH_["RU"]), bis="wald"),
    bis_(pl("Rupert hofft insgeheim auf einen Blitz.", 70, 30, beim("hofft", "hofft"), fill=GELB, size=32), "wald"),
    pl("Hildegard spaziert in den Wald.", 70, 30, beim("wald", "spaziert"), fill=GRUEN, size=32),
])

# ===========================================================================================================================
# A2 Fall: Im Wald bricht das Gewitter los – Blitz (nur als Symbol, Tod nur angedeutet)
# ===========================================================================================================================
HIW = 900
LOS = beim("gewitter", "Gewitter")
SCHLAG = beim("blitz", "schlägt")
TRIFFT = beim("blitz", "trifft")
wolke1 = ficon("tabler", "cloud-storm", 1000, 260, 200, LOS, fuell=HELLGRAU)
blitz_ = ficon("tabler", "bolt", 1240, 520, 150, SCHLAG, fuell=GELB)
szene(wolke1, "235grollen*", 0.6, 0.0)             # Donnergrollen, wenn die Gewitterwolken erscheinen
szene(blitz_, "235donner*", 0.75, 0.0)             # Einschlag beim sichtbaren Blitz
gewitterfolie([("gewitter", "Fall · Das Gewitter bricht los"), ("blitz", "Fall · Der Blitz")], [
    hart(weg("gewitter")), boden("gewitter"),
    hart(ficon("tabler", "trees", 230, BODEN + 4, 320, "gewitter", fuell=GRUEN, anim="cut")),
    hart(ficon("tabler", "tree", 520, BODEN + 4, 200, "gewitter", fuell=GRUEN, anim="cut")),
    hart(ficon("tabler", "tree", 1240, BODEN + 4, 240, "gewitter", fuell=GRUEN, anim="cut")),
    hart(ficon("tabler", "trees", 1640, BODEN + 4, 340, "gewitter", fuell=GRUEN, anim="cut")),
    pl("Dann bricht das Gewitter los.", 70, 30, LOS, fill=HELLGRAU, size=32),
    wolke1,
    ficon("tabler", "cloud-rain", 1280, 230, 170, beim("gewitter", "los"), fuell=HELLGRAU),
    ficon("tabler", "cloud-storm", 1560, 250, 180, beim("gewitter", "los"), fuell=HELLGRAU),
    *fig("HI", HIW, BODEN, FH_["HI"], [("gewitter", "froh_r"), (LOS, "sorge_r"), (SCHLAG, "schreck_r")], bis=TRIFFT,
         erst="cut"),
    bis_(ns(NAME["HI"], HIW, BODEN, "gewitter", NFARBE["HI"], anim="cut"), TRIFFT),
    blitz_,
    pl("Ein Blitz schlägt ein und trifft Hildegard tödlich.", 70, 94, TRIFFT, fill=GELB, size=32),
])

# ===========================================================================================================================
# A3 Die Frage
# ===========================================================================================================================
folie([("frage", "Die Frage · Tod gewünscht und verursacht"), ("frage2", "Die Frage · Reicht die Verursachung?")], [
    *tafel("frage", "Die Frage"),
    z("Rupert hat sich ihren Tod gewünscht, und ohne", 110, 190, "frage", "Bold", 36),
    z("seinen Rat wäre sie nicht im Wald gewesen.", 110, 242, beim("frage", "ohne"), "Bold", 36),
    blk(110, 330, 1040, 90, GELB, beim("frage", "Hat"), [("Hat er sie getötet?", "ExtraBold", 38, INK)]),
    blk(110, 460, 1040, 130, LILAHELL, "frage2", [("Oder reicht es nicht,", "ExtraBold", 36, INK),
                                               ("den Tod verursacht zu haben?", "ExtraBold", 36, INK)]),
    *requisit([("frage", ("tabler", "cloud-bolt", 120, HELLGRAU), "Tod gewünscht", WEISS),
               ("frage2", ("tabler", "link", 110, LILAHELL), "verursacht = getötet?", LILAHELL)]),
    *stehend("RU", FX, [("frage", "ernst"), ("frage2", "denkt")]),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_235(cue, absaetze, frage):
    els = [karte(140, 50, 1640, 930, cue, fill=HELL), titel("Sachverhalt", 210, 84, cue, 56)]
    y = 180
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=36, zeilenabstand=1.3)
        els += e; y += 12
    assert y + 66 <= 975, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=34))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_235("sv", [
    "Ein schwüler Sommernachmittag am Waldrand. Hildegard, eine wohlhabende Witwe Mitte 70, trinkt Kaffee auf ihrer "
    "Terrasse. Ihr Neffe Rupert ist zu Besuch; er ist ihr einziger Erbe. Auf seinem Handy erscheint eine "
    "Unwetterwarnung: Ein Gewitter zieht auf.",
    "Rupert rät ihr: „Tante Hildegard, geh doch noch ein Stück in den Wald. Die Luft ist so schön!“ Er hofft "
    "insgeheim, dass ein Blitz sie trifft. Ohne seinen Rat wäre Hildegard nicht in den Wald gegangen.",
    "Im Wald bricht das Gewitter los. Ein Blitz schlägt ein und trifft Hildegard tödlich.",
], "Hat sich Rupert strafbar gemacht?")

# ===========================================================================================================================
# C § 212 Abs. 1 StGB (Wortlautkarte), Mord aus Habgier (ein Satz)
# ===========================================================================================================================
PA = "A. Rupert, § 212 Abs. 1 StGB"
w212, w212_y = wortlaut(80, 180, 1100,
                        "„(1) Wer einen Menschen tötet, ohne Mörder zu sein, wird als Totschläger mit Freiheitsstrafe "
                        "nicht unter fünf Jahren bestraft.“", "§ 212 Abs. 1 StGB", "p212",
                        marken=[("Menschen tötet", beim("p212", "Menschen")), ("Totschläger", beim("p212", "Totschläger"))],
                        size=34)
folie([("p212", f"{PA} · Wortlaut"), ("mord", "A. Rupert › Mord aus Habgier, § 211?"),
       ("mord2", "A. Rupert › auch Mord: einen Menschen töten")], [
    *tafel("p212", "Totschlag, § 212 StGB"),
    *w212,
    blk(110, w212_y + 40, 1040, 90, GELB, "mord", [("Rupert will erben: Mord aus Habgier?", "ExtraBold", 34, INK)]),
    z("§ 211 Abs. 2: „Mörder ist, wer … aus Habgier …", 110, w212_y + 170, "mord2", "Bold", 33),
    z("einen Menschen tötet.“", 110, w212_y + 218, "mord2", "Bold", 33),
    blk(110, w212_y + 290, 1040, 90, BLAUHELL, beim("mord2", "einen"),
        [("Beide setzen voraus: einen Menschen töten", "ExtraBold", 34, INK)]),
    *requisit([("p212", ("tabler", "book", 110, WEISS), "§ 212 StGB", WEISS),
               ("mord", ("tabler", "moneybag", 110, GELB), "Habgier?", GELB),
               ("mord2", ("tabler", "book", 110, BLAUHELL), "§ 211 StGB", BLAUHELL)]),
    *stehend("RU", FX, [("p212", "ruhig"), ("mord", "sorge"), ("mord2", "ernst")]),
])
assert w212_y + 380 <= 900, w212_y

# ===========================================================================================================================
# D I. Objektiver Tatbestand: Erfolg und Kausalität
# ===========================================================================================================================
PT = f"{PA} › I. Objektiver Tatbestand"
folie([("erfolg", f"{PT} › 1. Erfolg"), ("kaus", f"{PT} › 2. Kausalität"),
       ("opfer", f"{PT} › 2. Kausalität › Opfer und Natur wirken mit")], [
    *tafel("erfolg", "I. Objektiver Tatbestand"),
    *okz("1. Erfolg: Hildegard ist tot.", 180, beim("erfolg", "Hildegard"), "Bold", 35),
    z("2. Kausalität (Formel: siehe Folge 026)", 185, 270, "kaus", "Bold", 35),
    z("Denk den Rat weg: kein Spaziergang,", 230, 330, beim("kaus", "Denk"), size=34),
    z("kein Blitz, der sie trifft", 230, 378, beim("kaus", "Denk"), size=34),
    *okz("kausal", 438, beim("kaus", "Kausal"), "ExtraBold", 35, x=275),
    blk(110, 530, 1040, 130, LILAHELL, "opfer", [("Sie geht selbst, die Natur tut den Rest:", "ExtraBold", 33, INK),
                                              ("Bedingung bleibt ursächlich", "Regular", 33, INK)]),
    zit("BGH, Beschl. v. 10.8.2021 – 3 StR 394/20, Rn. 5", 110, 676, beim("opfer", "Bundesgerichtshof")),
    *requisit([("erfolg", ("tabler", "cloud-bolt", 120, HELLGRAU), "Erfolg: Tod", WEISS),
               ("kaus", ("tabler", "link", 110, GELB), "kausal", GELB),
               ("opfer", ("tabler", "walk", 110, LILAHELL), "Opfer wirkt mit", LILAHELL)]),
    *stehend("RU", FX, [("erfolg", "feierlich"), ("kaus", "ruhig"), ("opfer", "denkt")]),
])

# ===========================================================================================================================
# E Problem: Reicht Kausalität? Objektive Zurechnung (Lehre)
# ===========================================================================================================================
PZ = f"{PT} › 3. Objektive Zurechnung"
folie([("reicht", f"{PT} › Reicht Kausalität?"), ("lehre", f"{PZ} (Lehre)"),
       ("def", f"{PZ} › rechtlich missbilligte Gefahr"), ("real", f"{PZ} › Gefahr im Erfolg verwirklicht"),
       ("werk", f"{PZ} › Werk oder Zufall?")], [
    *tafel("reicht", "Reicht Kausalität?"),
    z("Nach der Formel wäre schon der bloße Rat", 110, 180, beim("reicht", "Nach"), "Bold", 35),
    z("zum Spaziergang eine Tötung.", 110, 230, beim("reicht", "Nach"), "Bold", 35),
    z("Lehre: Die objektive Zurechnung begrenzt die Formel.", 110, 310, "lehre", size=33),
    blk(110, 380, 1040, 70, BLAUHELL, "def", [("Zurechenbar ist der Erfolg nur, wenn der Täter", "ExtraBold", 32, INK)],
        rund=14),
    z("(1) eine rechtlich missbilligte Gefahr geschaffen hat", 140, 470, beim("def", "rechtlich"), "Bold", 33),
    z("(2) und sich gerade diese Gefahr im Erfolg", 140, 530, "real", "Bold", 33),
    z("verwirklicht hat.", 196, 578, beim("real", "verwirklicht"), "Bold", 33),
    zit("Lehre: LMU München, Strukturkarte Objektive Zurechnung;", 110, 636, beim("def", "rechtlich")),
    zit("Uni Freiburg, AG Strafrecht AT, Übersicht Objektive Zurechnung", 110, 672, beim("def", "rechtlich")),
    blk(110, 740, 1040, 90, GELB, "werk", [("Ist der Tod sein Werk oder ein Zufall?", "ExtraBold", 34, INK)]),
    *requisit([("reicht", ("tabler", "link", 110, WEISS), "Reicht das?", WEISS),
               ("lehre", ("tabler", "scale", 120, BLAUHELL), "Lehre", BLAUHELL),
               ("def", ("tabler", "alert-triangle", 110, HELLROT), "missbilligte Gefahr", HELLROT),
               ("real", ("tabler", "target", 110, GELB), "verwirklicht", GELB),
               ("werk", ("tabler", "dice-5", 110, WEISS), "Werk oder Zufall?", WEISS)]),
    *stehend("RU", FX, [("reicht", "ruhig"), ("lehre", "denkt"), ("def", "ernst"), ("werk", "sorge")]),
])

# ===========================================================================================================================
# F Gewitterfall: allgemeines Lebensrisiko, nicht beherrschbar → keine Zurechnung
# ===========================================================================================================================
folie([("gef", f"{PZ} › (1) Gefahr geschaffen?"), ("leben", f"{PZ} › allgemeines Lebensrisiko"),
       ("herr", f"{PZ} › Blitz nicht beherrschbar"), ("zuneg", f"{PZ} (−)"),
       ("tsneg", "A. Rupert › Ergebnis: § 212 (−), § 211 (−)")], [
    *tafel("gef", "Rechtlich missbilligte Gefahr?"),
    z("Spaziergang im Wald, auch bei Gewitter:", 110, 180, "leben", "Bold", 35),
    z("allgemeines Lebensrisiko", 110, 230, beim("leben", "allgemeinen"), "ExtraBold", 35),
    z("Blitz so unwahrscheinlich: Der Rat ist nicht verboten.", 110, 300, beim("leben", "Vom"), size=33),
    z("Blitz nicht lenkbar: außerhalb jeder", 110, 370, "herr", size=33),
    z("menschlichen Beherrschung", 110, 418, beim("herr", "außerhalb"), size=33),
    zit("Lehre: LMU München (Bsp. Tod durch Gewitter); juraindividuell", 110, 470, beim("leben", "allgemeinen")),
    *neinz("keine rechtlich missbilligte Gefahr", 540, "zuneg", "ExtraBold", 35),
    blk(110, 610, 1040, 90, HELLROT, beim("zuneg", "Tod"), [("Der Tod ist nicht objektiv zuzurechnen.", "ExtraBold", 34, INK)]),
    *plusminus("Totschlag", 110, 740, "tsneg", False, size=36, stil="ExtraBold"),
    *plusminus("Mord", 420, 740, beim("tsneg", "Mord"), False, size=36, stil="ExtraBold"),
    *requisit([("gef", ("tabler", "alert-triangle", 110, WEISS), "Gefahr?", WEISS),
               ("leben", ("tabler", "cloud-storm", 130, HELLGRAU), "allgemeines Lebensrisiko", WEISS),
               ("herr", ("tabler", "bolt", 100, GELB), "nicht lenkbar", GELB),
               ("zuneg", ("tabler", "shield-x", 110, HELLROT), "nicht zurechenbar", HELLROT)]),
    *stehend("RU", FX, [("gef", "denkt"), ("leben", "ruhig"), ("herr", "staunt"), ("zuneg", "ernst"), ("tsneg", "muede")]),
])

# ===========================================================================================================================
# G Weg der Rechtsprechung: Lösung beim Vorsatz
# ===========================================================================================================================
PV = "A. Rupert › Rechtsprechung: Vorsatz"
folie([("rspr", PV), ("vors", f"{PV} › Geschehensablauf"), ("wunsch", f"{PV} › Wunsch ist kein Vorsatz"),
       ("gleich", f"{PV} › gleiches Ergebnis")], [
    *tafel("rspr", "Weg der Rechtsprechung"),
    z("Bei Vorsatztaten keine eigene Stufe", 110, 180, "rspr", "Bold", 35),
    z("„objektive Zurechnung“: Lösung beim Vorsatz", 110, 230, beim("rspr", "Sie"), "Bold", 35),
    zit("Lehrmaterial: Uni Freiburg, Vorlesung Strafrecht AT, § 9 KK 201", 110, 282, beim("rspr", "Sie")),
    blk(110, 340, 1040, 170, BLAUHELL, "vors", [("Vorsatz muss den Geschehensablauf umfassen;", "ExtraBold", 32, INK),
                                             ("unwesentlich: Abweichungen in den Grenzen", "Regular", 32, INK),
                                             ("allgemeiner Lebenserfahrung", "Regular", 32, INK)]),
    zit("BGH, Beschl. v. 10.8.2021 – 3 StR 394/20, Rn. 8", 110, 522, beim("vors", "Unwesentlich")),
    blk(110, 580, 1040, 130, HELLROT, "wunsch", [("Tod durch Blitz: nur erhofft, nicht herbeigeführt.", "ExtraBold", 32, INK),
                                              ("Ein bloßer Wunsch ist kein Vorsatz.", "Regular", 32, INK)]),
    blk(110, 740, 1040, 90, HELLGRUEN, "gleich", [("Beide Wege: dasselbe Ergebnis", "ExtraBold", 34, INK)]),
    *requisit([("rspr", ("tabler", "gavel", 110, WEISS), "Rechtsprechung", WEISS),
               ("vors", ("tabler", "target", 110, BLAUHELL), "Vorsatz", BLAUHELL),
               ("wunsch", ("tabler", "bulb", 110, HELLROT), "nur ein Wunsch", HELLROT),
               ("gleich", ("tabler", "scale", 120, HELLGRUEN), "gleiches Ergebnis", HELLGRUEN)]),
    *stehend("RU", FX, [("rspr", "ruhig"), ("vors", "denkt"), ("wunsch", "muede"), ("gleich", "ernst")]),
])

# ===========================================================================================================================
# H Abwandlung: Täter wartet im Wald (Sonderwissen)
# ===========================================================================================================================
folie([("abw", "Abwandlung · Rupert weiß von einem Täter im Wald")], [
    *tafel("abw", "Abwandlung"),
    z("Rupert weiß: Im Wald wartet", 110, 190, beim("abw", "Weiß"), "Bold", 36),
    z("ein Täter auf Hildegard.", 110, 242, beim("abw", "Weiß"), "Bold", 36),
    *okz("Sonderwissen: rechtlich missbilligte Gefahr", 340, beim("abw", "Sonderwissen"), "ExtraBold", 34),
    zit("Lehre: LMU München, Strukturkarte (Beurteilung ex ante inkl. Sonderwissen)", 140, 400, beim("abw", "Sonderwissen")),
    *requisit([("abw", ("tabler", "alert-triangle", 110, HELLROT), "Täter im Wald", HELLROT),
               (beim("abw", "Sonderwissen"), ("tabler", "eye", 110, GELB), "Sonderwissen", GELB)]),
    *stehend("RU", FX, [("abw", "ernst"), (beim("abw", "Sonderwissen"), "sorge")]),
])

# ===========================================================================================================================
# I B. § 222 StGB (Wortlautkarte) – entfällt ebenso
# ===========================================================================================================================
PB = "B. Rupert, § 222 StGB"
w222, w222_y = wortlaut(80, 170, 1100,
                        "„Wer durch Fahrlässigkeit den Tod eines Menschen verursacht, wird mit Freiheitsstrafe bis zu "
                        "fünf Jahren oder mit Geldstrafe bestraft.“", "§ 222 StGB", "p222",
                        marken=[("Fahrlässigkeit", beim("p222", "Fahrlässigkeit")), ("verursacht", beim("p222", "verursacht"))],
                        size=34)
folie([("p222", f"{PB} · Wortlaut"), ("p222b", f"{PB} › Zurechnung"), ("p222c", f"{PB} › keine Sorgfaltspflichtverletzung"),
       ("straflos", "Ergebnis: Rupert ist nicht strafbar")], [
    *tafel("p222", "B. Fahrlässige Tötung"),
    *w222,
    z("BGH: zugerechnet nur, wenn sich gerade die", 110, w222_y + 36, "p222b", "Bold", 33),
    z("vom Täter gesetzte Gefahr im Erfolg verwirklicht", 110, w222_y + 84, beim("p222b", "Täter"), "Bold", 33),
    zit("BGH, Beschl. v. 5.5.2021 – 4 StR 19/20, Rn. 21", 110, w222_y + 132, beim("p222b", "Täter")),
    *neinz("Rat zum Spaziergang: keine Sorgfaltspflicht", w222_y + 190, "p222c", "Bold", 33),
    z("verletzt, keine solche Gefahr geschaffen", 185, w222_y + 238, beim("p222c", "schafft"), size=33),
    blk(110, w222_y + 310, 1040, 90, HELLGRUEN, "straflos", [("Rupert: weder § 212 noch § 222 strafbar", "ExtraBold", 34, INK)]),
    *requisit([("p222", ("tabler", "book", 110, WEISS), "§ 222 StGB", WEISS),
               ("p222b", ("tabler", "gavel", 110, WEISS), "Bundesgerichtshof", WEISS),
               ("p222c", ("tabler", "shield-x", 110, HELLROT), "keine Pflichtverletzung", HELLROT),
               ("straflos", ("tabler", "scale", 120, HELLGRUEN), "straflos", HELLGRUEN)]),
    *stehend("RU", FX, [("p222", "ruhig"), ("p222b", "denkt"), ("straflos", "muede")]),
])
assert w222_y + 400 <= 900, w222_y

# ===========================================================================================================================
# J Weitere Fallgruppen (Lehre)
# ===========================================================================================================================
PG = "Fallgruppen der objektiven Zurechnung"
folie([("gruppen", PG), ("g1", f"{PG} › 1. Schutzzweck der Norm"), ("g2", f"{PG} › 2. Selbstgefährdung"),
       ("g3", f"{PG} › 3. atypischer Kausalverlauf"), ("g4", f"{PG} › 4. rechtmäßiges Alternativverhalten")], [
    *tafel("gruppen", "Weitere Fallgruppen (Lehre)"),
    z("Neben dem allgemeinen Lebensrisiko:", 110, 170, "gruppen", size=33),
    z("1. Schutzzweck der Norm: Erfolg im Bereich,", 110, 236, "g1", "Bold", 33),
    z("den die verletzte Pflicht schützen soll", 150, 282, beim("g1", "Der"), size=32),
    z("2. Eigenverantwortliche Selbstgefährdung", 110, 352, "g2", "Bold", 33),
    z("des Opfers (Folgen 058 und 203)", 150, 398, beim("g2", "des"), size=32),
    zit("BGH, Urt. v. 28.1.2014 – 1 StR 494/13, BGHSt 59, 150, Rn. 71", 150, 440, beim("g2", "des")),
    z("3. Atypischer Kausalverlauf: völlig außerhalb", 110, 498, "g3", "Bold", 33),
    z("der Lebenserfahrung", 150, 544, beim("g3", "außerhalb"), size=32),
    z("4. Rechtmäßiges Alternativverhalten: zugerechnet", 110, 614, "g4", "Bold", 33),
    z("nur, wenn bei pflichtgemäßem Verhalten ausgeblieben", 150, 660, beim("g4", "Zugerechnet"), size=32),
    zit("BGH, Beschl. v. 5.5.2021 – 4 StR 19/20, Rn. 21 (zu 1. und 4.)", 150, 704, beim("g4", "Zugerechnet")),
    zit("Lehre: LMU München; Uni Freiburg, AG Strafrecht AT", 110, 760, "gruppen"),
    *requisit([("gruppen", ("tabler", "list-check", 110, WEISS), "Fallgruppen", WEISS),
               ("g1", ("tabler", "shield-check", 110, BLAUHELL), "Schutzzweck", BLAUHELL),
               ("g2", ("tabler", "walk", 110, LILAHELL), "Selbstgefährdung", LILAHELL),
               ("g3", ("tabler", "route", 110, GELB), "atypisch", GELB),
               ("g4", ("tabler", "arrows-split", 110, HELLGRUEN), "Alternativverhalten", HELLGRUEN)]),
    *stehend("RU", FX, [("gruppen", "ruhig"), ("g2", "denkt"), ("g4", "ernst")]),
])

# ===========================================================================================================================
# K Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Standort: objektiver Tatbestand"), ("k1", "Klausurtipp › ausführlich nur bei Anlass"),
       ("k2", "Klausurtipp › Weg der Rechtsprechung kurz")], [
    *tafel("tipp", "Klausurtipp: Wo und wie?", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Im objektiven Tatbestand prüfen,", 200, 200, beim("tipp", "objektiven"), "ExtraBold", 35),
    z("direkt nach der Kausalität", 240, 252, beim("tipp", "direkt"), size=34),
    linienzug([(130, 320), (1130, 320)], "k1", breite=3),
    z("Ausführlich nur, wenn der Fall Anlass gibt:", 200, 344, "k1", "ExtraBold", 34),
    z("Zufall und Natur, Opfer selbst, Dritte", 240, 396, beim("k1", "bei"), size=34),
    z("sonst genügt ein Satz", 240, 448, beim("k1", "Sonst"), size=34),
    linienzug([(130, 516), (1130, 516)], "k2", breite=3),
    z("Weg der Rechtsprechung kurz erwähnen;", 200, 540, "k2", "ExtraBold", 34),
    z("gleiches Ergebnis: Streit nicht entscheiden", 240, 592, beim("k2", "Führt"), size=34),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# L Klausurschema (Lexi), Punkt für Punkt
# ===========================================================================================================================
folie([("sch", "Klausurschema · Rupert"), ("s1", "Klausurschema › A. § 212 › I. Obj. Tatbestand › 1. Erfolg"),
       ("s2", "Klausurschema › 2. Kausalität"), ("s3", "Klausurschema › 3. Objektive Zurechnung"),
       ("s4", "Klausurschema › Tatbestand entfällt"), ("s5", "Klausurschema › B. § 222 StGB")], [
    *tafel("sch", "Klausurschema: Rupert"),
    z("A. § 212 StGB, I. Objektiver Tatbestand", 110, 170, "s1", "ExtraBold", 34),
    *plusminus("1. Erfolg: Hildegard ist tot", 150, 236, beim("s1", "Erstens"), True, size=34, stil="Bold"),
    *plusminus("2. Kausalität", 150, 296, "s2", True, size=34, stil="Bold"),
    z("3. Objektive Zurechnung: keine rechtlich", 150, 356, "s3", "Bold", 34),
    *plusminus("missbilligte Gefahr", 196, 408, beim("s3", "keine"), False, size=34),
    blk(110, 480, 1040, 90, HELLROT, "s4", [("Tatbestand entfällt: kein Totschlag", "ExtraBold", 34, INK)]),
    *plusminus("B. § 222 StGB: aus demselben Grund", 110, 610, "s5", False, size=34, stil="ExtraBold"),
    *redet("LX_erklaert", FX, FB, FR + 40, "sch", "merke"),
    ns("Lexi", FX, FB, "sch", GELB, d=0.2),
])

# ===========================================================================================================================
# M Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Kausalität", "a"), (" allein macht noch keinen Täter.", 0)]], 750, 300, 42, "merke",
                {"a": beim("merke", "Kausalität")}),
    *markertext([[("Zurechenbar ist der Erfolg nur, wenn der", 0)],
                 [("Täter eine ", 0), ("rechtlich missbilligte Gefahr", "b")],
                 [("geschaffen hat, die sich im Erfolg ", 0), ("verwirklicht", "c"), (".", 0)]],
                750, 440, 42, "m2", {"b": beim("m2", "rechtlich"), "c": beim("m2", "verwirklicht")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
