"""Folge 231 · Erlaubnistatbestandsirrtum (ETBI): Alle Schuldtheorien erklärt – Serienstandard Open Peeps (Katzenkönig).
Fiktiver Fall: Herbstabend im Stadtpark (Nacht, weil die Dunkelheit den Irrtum trägt). Bärbel verliert beim Joggen ihr Handy,
Helge hebt es auf, läuft ihr hinterher und ruft. Unter der Laterne glänzt das Handy in seiner Hand; Bärbel hält es für ein
Messer und sprüht Pfefferspray (nur als Icon, keine Verletzung im Bild). Danach § 223 (§ 224) kurz, § 32 Abs. 2 StGB
(Wortlautkarte): kein Angriff → rechtswidrig; Erlaubnistatbestandsirrtum, Abgrenzung Erlaubnisirrtum; § 16 Abs. 1 Satz 1 und
§ 17 Satz 1 (Wortlautkarten); fünf Theorien mit Ergebnis im Fall und Kritik, Teilnahme-Argument (§§ 26, 27); BGH;
Ergebnis § 229 (vermeidbarer Irrtum), Gegenfall; Klausurtipp, Schema, Merksatz mit Lexi.
Szenen laut ../SZENENPLAN.md. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/feld/requisit/paar als
eigene Kopie aus Folge 227 (gemeinsame Dateien unverändert); neu: nachtfolie(), hand(), park-Bausteine.
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut StGB nach gesetze-im-internet.de, Abruf 07.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_231/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_231/" in n:
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
NAME = {"BA": "Bärbel", "HE": "Helge"}
NFARBE = {"BA": PINK, "HE": ORANGE}
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







# --- Folge 231: Größen, Nacht, Park-Bausteine -----------------------------------------------------------------------------
GROESSE = {"BA": 0.95, "HE": 1.0}         # Bärbel etwas kleiner als Helge


def hh(k, h):
    return round(h * GROESSE[k])


def stehend(k, x, folge, bis=None):
    els = [*fig(k, x, FB, hh(k, FR), folge, bis=bis), bis_(ns(NAME[k], x, FB, folge[0][0], NFARBE[k], d=0.1), bis)]
    return rechts_frei(els, 1200)


BG_FARBE["nacht"] = None                     # Nacht = Verlauf, erzeugt im Renderer (wie Folgen 001, 148)
PFAD_FARBE["nacht"] = (255, 255, 255, 170)


def nachtfolie(pfade, els):
    """Fallszene bei Nacht: Der Fall spielt im dunklen Park, die Dunkelheit trägt Bärbels Irrtum."""
    pruefe_im_bild(els)
    FOLIEN.append(dict(bg="nacht", pfade=pfade, els=els))


def hand(name, cx, unten, hoehe):
    """Position der ausgestreckten Hand (äußerster deckender Punkt im Band 35–60 % der Höhe) einer Figur."""
    e = peep_voll(name, cx, unten, hoehe, "_")
    a = np.asarray(e.sprite)[:, :, 3] > 40
    h_ = a.shape[0]
    band = a[int(h_ * 0.35):int(h_ * 0.60)]
    ys, xs = np.nonzero(band)
    links = name.endswith("_r") is False
    i = xs.argmin() if links else xs.argmax()
    return e.x + xs[i], e.y + int(h_ * 0.35) + ys[i]


WEG = (96, 104, 128, 255)                    # Parkweg bei Nacht


def parkweg(cue):
    """Parkweg in Seitenansicht: Fläche unter der Bodenlinie."""
    im = Image.new("RGBA", (1840, 70))
    ImageDraw.Draw(im).rectangle((0, 0, 1840, 70), fill=WEG)
    return El(im, 40, BODEN, cue, "cut", 0.0, None, name="parkweg")


# ===========================================================================================================================
# A1 Fall: Herbstabend im Stadtpark (Nacht) – Handy verloren, Helge läuft hinterher, Laterne, Pfefferspray
# ===========================================================================================================================
BAX, HEX0, HEXM, HEX1, LATX = 600, 1660, 1570, 1230, 1420
FH_ = {k: hh(k, FH) for k in GROESSE}
lat, (lkx, lky) = laterne(LATX, BODEN, 640, NULL)
JOG = NULL, beim("baerbel", "Ohr", ende=True)                               # Bärbel joggt ab 0,0 s nach links ins Bild
GEH = beim("helge", "läuft"), beim("helge", "hinterher", ende=True)          # Helge läuft ihr hinterher (erstes Stück)
RENN = beim("dreht", "rennt"), beim("dreht", "zu", ende=True)                # … und rennt im Dunkeln auf sie zu
DXJ, DXH, DXR = 300, HEX0 - HEXM, HEXM - HEX1
HANDY0 = beim("handy", "rutscht")
AUF = beim("helge", "hebt")
hxm, hym = hand("HE_ruhig", HEXM, BODEN, FH_["HE"])
hx1, hy1 = hand("HE_ruhig", HEX1, BODEN, FH_["HE"])
ba_jog = bewegt(peep_voll("BA_ruhig", BAX, BODEN, FH_["BA"], NULL, anim="cut", bis="dreht"), JOG[0], JOG[1], DXJ)
he_geh = bewegt(peep_voll("HE_froh", HEXM, BODEN, FH_["HE"], AUF, anim="cut", bis="he1"), GEH[0], GEH[1], DXH)
he_renn = bewegt(peep_voll("HE_froh", HEX1, BODEN, FH_["HE"], "dreht", anim="cut", bis="glanz"), RENN[0], RENN[1], DXR)
spray = ficon("tabler", "spray", BAX + 160, BODEN - 200, 96, beim("spray", "sprüht"), fuell=ROT, bis="he2")
szene(spray, "231spray*", 0.5, 0.0)                     # Sprühen: kurzer Sprühstoß beim sichtbaren Spray
szene(he_renn, "231schritte*", 0.55, round(T_(RENN[0]) - T_("dreht"), 3))   # Laufschritte ab „rennt“, solange Helge sichtbar läuft
handy_geh = bewegt(ficon("tabler", "device-mobile", hxm - 8, hym + 6, 46, AUF, fuell=BLAU, anim="cut", bis="dreht"),
                   GEH[0], GEH[1], DXH)
handy_renn = bewegt(ficon("tabler", "device-mobile", hx1 - 8, hy1 + 6, 46, "dreht", fuell=BLAU, anim="cut"),
                    RENN[0], RENN[1], DXR)
nachtfolie([(NULL, "Fall · Herbstabend im Stadtpark"), ("baerbel", "Fall · Bärbel beim Joggen"),
            ("handy", "Fall · Das verlorene Handy"), ("helge", "Fall · Helge läuft hinterher"),
            ("dreht", "Fall · Ein Mann rennt auf sie zu"), ("glanz", "Fall · Unter der Laterne"),
            ("messer", "Fall · Bärbel glaubt: ein Messer"), ("spray", "Fall · Das Pfefferspray"),
            ("he2", "Fall · Nur das Handy")], [
    hart(lichtkegel(lkx, lky, 230, BODEN, NULL)),
    hart(parkweg(NULL)), boden(NULL),
    hart(lat),
    hart(mond(1110, 110, 44, NULL)),
    hart(ficon("tabler", "trees", 160, BODEN + 4, 220, NULL, fuell=GRUEN, anim="cut")),
    hart(ficon("tabler", "trees", 400, BODEN + 4, 170, NULL, fuell=GRUEN, anim="cut")),
    hart(pl("Herbstabend im Stadtpark, es ist schon dunkel", 70, 30, NULL, fill=GELB, size=32)),
    # Bärbel joggt (Musik im Ohr), dreht sich um, erschrickt, ruft, sprüht
    ba_jog,
    bewegt(ficon("tabler", "headphones", BAX + 10, 430, 62, beim("baerbel", "Musik"), fuell=PINK, anim="cut", bis="dreht"),
           JOG[0], JOG[1], DXJ),
    pl("Musik im Ohr", 70, 94, beim("baerbel", "Musik"), fill=WEISS, size=30, bis=HANDY0),
    *fig("BA", BAX, BODEN, FH_["BA"], [("dreht", "schreck_r"), ("messer", "angst_r")], bis="ba1", erst="cut"),
    *redet("BA_ruft_r", BAX, BODEN, FH_["BA"], "ba1", "spray"),
    *fig("BA", BAX, BODEN, FH_["BA"], [("spray", "angst_r"), ("he2", "sorge_r")], erst="cut"),
    bis_(bewegt(ns(NAME["BA"], BAX, BODEN, NULL, NFARBE["BA"], anim="cut"), JOG[0], JOG[1], DXJ), "dreht"),
    ns(NAME["BA"], BAX, BODEN, "dreht", NFARBE["BA"], anim="cut"),
    # Handy rutscht aus der Tasche und liegt auf dem Weg, bis Helge es aufhebt
    ficon("tabler", "device-mobile", 930, BODEN - 2, 46, HANDY0, fuell=BLAU, bis=AUF),
    pl("Handy verloren, ohne dass sie es merkt", 70, 94, HANDY0, fill=BLAU, size=30, bis="dreht"),
    # Helge: hebt es auf (rechts), läuft hinterher, ruft, rennt bis unter die Laterne, Augen brennen, redet
    *fig("HE", HEX0, BODEN, FH_["HE"], [("helge", "ruhig")], bis=AUF),
    he_geh, handy_geh,
    *redet("HE_ruft", HEXM, BODEN, FH_["HE"], "he1", "dreht"),
    he_renn, handy_renn,
    *fig("HE", HEX1, BODEN, FH_["HE"], [("glanz", "froh"), ("augen", "augen")], bis="he2", erst="cut"),
    *redet("HE_klagt", HEX1, BODEN, FH_["HE"], "he2", "frage"),
    bis_(ns(NAME["HE"], HEX0, BODEN, "helge", NFARBE["HE"], d=0.1), GEH[0]),
    bis_(bewegt(ns(NAME["HE"], HEXM, BODEN, GEH[0], NFARBE["HE"], anim="cut"), GEH[0], GEH[1], DXH), "dreht"),
    bewegt(ns(NAME["HE"], HEX1, BODEN, "dreht", NFARBE["HE"], anim="cut"), RENN[0], RENN[1], DXR),
    pl("Helge, ein älterer Spaziergänger", 70, 158, beim("helge", "Helge"), fill=WEISS, size=30, bis="dreht"),
    blase("sprech", 440, 170, "he1", 1660, 220, inhalt=["Hallo! Warten Sie!"], textsize=34,
          figur=("HE_ruft", HEXM, BODEN, FH_["HE"]), bis="dreht"),
    pl("Ein Mann rennt im Dunkeln auf sie zu.", 70, 94, beim("dreht", "Ein"), fill=WEISS, size=30, bis="spray"),
    # Unter der Laterne: das Handy glänzt
    ficon("tabler", "sparkles", hx1 - 40, hy1 - 22, 54, beim("glanz", "glänzt"), fuell=GELB, bis="spray"),
    pl("Unter der Laterne glänzt etwas in seiner Hand.", 70, 158, "glanz", fill=GELB, size=30, bis="spray"),
    blase("denk", 380, 200, "messer", 330, 340, inhalt=["Ein Messer!"], textsize=34,
          figur=("BA_angst_r", BAX, BODEN, FH_["BA"]), bis="ba1"),
    blase("sprech", 440, 180, "ba1", 330, 340, inhalt=["Bleiben Sie weg!"], textsize=34,
          figur=("BA_ruft_r", BAX, BODEN, FH_["BA"]), bis="spray"),
    # Pfefferspray nur als Symbol, keine Verletzung im Bild
    spray,
    pl("Pfefferspray", 70, 94, beim("spray", "Pfefferspray"), fill=ROT, size=30),
    pl("Helges Augen brennen.", 70, 158, "augen", fill=HELLROT, size=30),
    blase("sprech", 440, 200, "he2", 930, 330, inhalt=["Ich wollte Ihnen doch", "nur Ihr Handy bringen!"], textsize=30,
          figur=("HE_klagt", HEX1, BODEN, FH_["HE"])),
])

# ===========================================================================================================================
# A2 Die Frage
# ===========================================================================================================================
folie([("frage", "Die Frage · Angriff, den es nie gab"), ("frage2", "Die Frage · Fünf Theorien")], [
    *tafel("frage", "Die Frage"),
    z("Bärbel hat sich gegen einen Angriff gewehrt,", 110, 190, "frage", "Bold", 38),
    z("den es nie gab.", 110, 244, "frage", "Bold", 38),
    blk(110, 330, 1040, 90, GELB, beim("frage", "Ist"), [("Ist sie wegen Körperverletzung strafbar?", "ExtraBold", 37, INK)]),
    blk(110, 470, 1040, 90, LILAHELL, "frage2", [("Darüber streiten 5 Theorien.", "ExtraBold", 37, INK)]),
    *requisit([("frage", ("tabler", "device-mobile", 90, BLAU), "Angriff, den es nie gab", WEISS),
               ("frage2", ("tabler", "scale", 120, LILAHELL), "Streitstand", LILAHELL)]),
    *paar("BA", [("frage", "sorge"), ("frage2", "denkt")], "HE", [("frage", "muede")]),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_231(cue, absaetze, frage):
    els = [karte(140, 50, 1640, 930, cue, fill=HELL), titel("Sachverhalt", 210, 84, cue, 56)]
    y = 180
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=36, zeilenabstand=1.3)
        els += e; y += 12
    assert y + 66 <= 975, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=34))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_231("sv", [
    "Ein Herbstabend im Stadtpark, es ist schon dunkel. Bärbel joggt mit Musik im Ohr. Dabei rutscht ihr das Handy aus der "
    "Tasche, ohne dass sie es merkt. Helge, ein älterer Spaziergänger, hebt es auf, läuft ihr hinterher und ruft: "
    "„Hallo! Warten Sie!“",
    "Bärbel dreht sich um und sieht einen Mann im Dunkeln auf sich zurennen. Unter einer Laterne hebt er die Hand, darin "
    "glänzt etwas. Bärbel hält es für ein Messer, ruft „Bleiben Sie weg!“ und sprüht ihm Pfefferspray ins Gesicht. "
    "Helges Augen brennen; ein Arzt muss sie ausspülen.",
    "Helge wollte ihr nur das Handy bringen. Unter der Laterne war das Handy in seiner Hand zu erkennen; ein kurzer Blick "
    "hätte Bärbel den Irrtum gezeigt.",
], "Wie hat sich Bärbel strafbar gemacht?")

# ===========================================================================================================================
# C I. Tatbestand: § 223, § 224 Abs. 1 Nr. 2 StGB (kurz)
# ===========================================================================================================================
PA_ = "A. Bärbel, §§ 223, 224 StGB"
folie([("tb", f"{PA_} › I. Tatbestand › § 223 Abs. 1"), ("tb2", f"{PA_} › I. Tatbestand › § 224 Abs. 1 Nr. 2: Pfefferspray"),
       ("vors", f"{PA_} › I. Tatbestand › Vorsatz")], [
    *tafel("tb", "I. Tatbestand: §§ 223, 224 StGB"),
    *okz("§ 223 Abs. 1: Spray in den Augen", 190, beim("tb", "Körperverletzung"), "Bold", 34),
    z("ist eine Körperverletzung.", 185, 238, beim("tb", "Körperverletzung"), size=33),
    *okz("§ 224 Abs. 1 Nr. 2: Pfefferspray als", 320, beim("tb2", "gefährliches"), "Bold", 34),
    z("gefährliches Werkzeug kommt in Betracht", 185, 368, beim("tb2", "kommt"), size=33),
    zit("vgl. BGH, Urt. v. 20.9.2017 – 1 StR 112/17, Rn. 16", 185, 414, beim("tb2", "gefährliches")),
    *okz("Vorsatz: Bärbel wollte ihn treffen.", 490, "vors", "Bold", 34),
    *requisit([("tb", ("tabler", "book", 110, WEISS), "§§ 223, 224 StGB", WEISS),
               ("tb2", ("tabler", "spray", 90, ROT), "Pfefferspray", WEISS),
               ("vors", ("tabler", "target", 110, GELB), "vorsätzlich", GELB)]),
    *paar("BA", [("tb", "ernst"), ("vors", "muede")], "HE", [("tb", "augen"), ("vors", "ruhig")]),
])

# ===========================================================================================================================
# D II. Rechtswidrigkeit: § 32 Abs. 2 StGB (Wortlautkarte) – kein Angriff, keine Notwehrlage
# ===========================================================================================================================
PR = "A. Bärbel › II. Rechtswidrigkeit: Notwehr, § 32 StGB"
w32, w32_y = wortlaut(80, 180, 1100,
                      "„(2) Notwehr ist die Verteidigung, die erforderlich ist, um einen gegenwärtigen rechtswidrigen "
                      "Angriff von sich oder einem anderen abzuwenden.“", "§ 32 Abs. 2 StGB", "p32",
                      marken=[("Verteidigung", beim("p32", "Verteidigung")), ("erforderlich", beim("p32", "erforderlich")),
                              ("gegenwärtigen", beim("p32", "gegenwärtigen")),
                              ("rechtswidrigen", beim("p32", "rechtswidrigen")), ("Angriff", beim("p32", "Angriff"))],
                      size=33)
folie([("rw", f"{PR}?"), ("p32", f"{PR} · Wortlaut Abs. 2"), ("kein", f"{PR} › Angriff? (−)"),
       ("rw_neg", f"{PR} › keine Notwehrlage: rechtswidrig")], [
    *tafel("rw", "II. Rechtswidrigkeit: Notwehr?"),
    *w32,
    *neinz("Angriff: Helge wollte nur das Handy zurückgeben.", w32_y + 40, "kein", "Bold", 33,
           kreuz=beim("kein", "Angriff")),
    zit("vgl. BGH, Urt. v. 25.5.2022 – 4 StR 36/22, Rn. 10", 185, w32_y + 88, beim("kein", "Angriff")),
    blk(110, w32_y + 150, 1040, 90, HELLROT, "rw_neg", [("Keine Notwehrlage: Das Sprühen war rechtswidrig.", "ExtraBold", 33, INK)]),
    *requisit([("rw", ("tabler", "shield-check", 110, GELB), "Notwehr?", GELB),
               ("kein", ("tabler", "device-mobile", 90, BLAU), "nur das Handy", WEISS),
               ("rw_neg", ("tabler", "shield-x", 110, HELLROT), "rechtswidrig", HELLROT)]),
    *paar("BA", [("rw", "denkt"), ("rw_neg", "sorge")], "HE", [("rw", "ruhig"), ("kein", "froh")]),
])
assert w32_y + 240 <= 900, w32_y

# ===========================================================================================================================
# E III. Schuld: Erlaubnistatbestandsirrtum; Abgrenzung Erlaubnisirrtum (§ 17)
# ===========================================================================================================================
folie([("irrtum", "A. Bärbel › Irrtum?"), ("vorst", "A. Bärbel › Irrtum › vorgestellt: Messerangriff"),
       ("hypo", "A. Bärbel › Irrtum › wäre gerechtfertigt"), ("etbi", "A. Bärbel › Erlaubnistatbestandsirrtum"),
       ("eti", "A. Bärbel › Abgrenzung: Erlaubnisirrtum, § 17")], [
    *tafel("irrtum", "Bärbel hat sich geirrt"),
    z("Vorgestellt: ein Mann greift sie", 110, 180, "vorst", "Bold", 35),
    z("mit einem Messer an", 110, 228, beim("vorst", "einen"), "Bold", 35),
    *okz("Wäre das wahr: Spray erforderlich und geboten", 300, "hypo", size=33),
    *okz("Bärbel wäre gerechtfertigt.", 346, beim("hypo", "sie"), "Bold", 33),
    blk(110, 420, 1040, 120, GELB, "etbi", [("Erlaubnistatbestandsirrtum", "ExtraBold", 36, INK),
                                         ("auch: Putativnotwehr", "Regular", 33, INK)]),
    zit("BGH, Beschl. v. 25.5.2022 – 4 StR 36/22, Rn. 11; BGH 3 StR 450/10, Rn. 12", 110, 552, "etbi"),
    blk(110, 620, 1040, 210, LILAHELL, "eti", [("Anders: Erlaubnisirrtum, § 17", "ExtraBold", 33, INK),
                                            ("wüsste sie: nur das Handy, und glaubte sie,", "Regular", 32, INK),
                                            ("man dürfe jeden besprühen, der nachts", "Regular", 32, INK),
                                            ("auf einen zuläuft: Irrtum über das Recht", "Regular", 32, INK)]),
    *requisit([("irrtum", ("tabler", "zoom-question", 110, WEISS), "Irrtum", WEISS),
               ("vorst", ("tabler", "alert-triangle", 110, HELLROT), "Messer?", HELLROT),
               ("etbi", ("tabler", "eye", 110, GELB), "Putativnotwehr", GELB),
               ("eti", ("tabler", "book", 110, LILAHELL), "Irrtum über das Recht", LILAHELL)]),
    *paar("BA", [("irrtum", "denkt"), ("vorst", "angst"), ("etbi", "sorge"), ("eti", "ernst")], "HE",
          [("irrtum", "ruhig"), ("vorst", "froh"), ("etbi", "denkt")]),
])

# ===========================================================================================================================
# F Zwischen § 16 und § 17: Wortlautkarten (vorgelesen)
# ===========================================================================================================================
PE_ = "A. Bärbel › Erlaubnistatbestandsirrtum"
w16, w16_y = wortlaut(80, 170, 1100,
                      "„(1) Wer bei Begehung der Tat einen Umstand nicht kennt, der zum gesetzlichen Tatbestand gehört, "
                      "handelt nicht vorsätzlich. …“", "§ 16 Abs. 1 Satz 1 StGB", "p16",
                      marken=[("Umstand", beim("p16", "Umstand")), ("vorsätzlich", beim("p16", "vorsätzlich"))], size=32)
w17, w17_y = wortlaut(80, w16_y + 24, 1100,
                      "„Fehlt dem Täter bei Begehung der Tat die Einsicht, Unrecht zu tun, so handelt er ohne Schuld, "
                      "wenn er diesen Irrtum nicht vermeiden konnte. …“", "§ 17 Satz 1 StGB", "p17",
                      marken=[("Einsicht", beim("p17", "Einsicht")), ("Schuld", beim("p17", "Schuld"))], size=32)
folie([("gesetz", f"{PE_} › gesetzlich nicht geregelt"), ("p16", f"{PE_} › § 16 Abs. 1 Satz 1"),
       ("p17", f"{PE_} › § 17 Satz 1"), ("dazw", f"{PE_} › zwischen § 16 und § 17")], [
    *tafel("gesetz", "Nicht ausdrücklich geregelt"),
    *w16, *w17,
    blk(110, w17_y + 26, 1040, 130, GELB, "dazw", [("Irrtum über Tatsachen: wie § 16", "ExtraBold", 33, INK),
                                               ("kein Unrechtsbewusstsein: wie § 17", "ExtraBold", 33, INK)]),
    *requisit([("gesetz", ("tabler", "book", 110, WEISS), "nicht geregelt", WEISS),
               ("dazw", ("tabler", "arrows-exchange", 110, GELB), "Streit", GELB)]),
    *stehend("BA", FX, [("gesetz", "denkt"), ("dazw", "sorge")]),
])
assert w17_y + 170 <= 900, w17_y


# ===========================================================================================================================
# G Die fünf Theorien: je Kern, Ergebnis im Fall, Kritik
# ===========================================================================================================================
def theorie(nr, name, cue, kern, ergebnis, erg_cue, kritik, krit_cue, beleg, req, ba, extra=(), titelsize=44, pfad_extra=()):
    """Theorietafel: Kern (blau), Ergebnis im Fall (grün/rot), Kritik (Kreuz, hellrot)."""
    pf = f"{PE_} › Rechtsfolge: {nr}. {name}"
    y = 180
    els = [*tafel(cue, f"{nr}. {name}", size=titelsize)]
    els.append(blk(110, y, 1040, 50 + 44 * len(kern), BLAUHELL, cue, [(t, s_, 32, INK) for t, s_ in kern]))
    y += 50 + 44 * len(kern) + 28
    ef, et = ergebnis
    els.append(blk(110, y, 1040, 50 + 44 * len(et), ef, erg_cue, [(t, s_, 32, INK) for t, s_ in et]))
    y += 50 + 44 * len(et) + 28
    els.append(bis_(nein(140, y + 24, krit_cue, gr=20), None))
    for i, (t, s_) in enumerate(kritik):
        els.append(z(t, 185, y + i * 44, krit_cue, s_, 32))
    y += 44 * len(kritik) + 8
    els.append(zit(beleg, 185, y, krit_cue))
    y += 44
    els += list(extra)
    assert y <= 880, (name, y)
    els += requisit(req)
    els += stehend("BA", FX, ba)
    return pf, els


P1, E1 = theorie(1, "Vorsatztheorie", "t1",
                 [("Zum Vorsatz gehört auch das Bewusstsein,", "ExtraBold"), ("Unrecht zu tun.", "ExtraBold")],
                 (HELLGRUEN, [("Bärbel fehlte es: kein Vorsatz", "ExtraBold")]), "t1e",
                 [("Kritik: § 17 macht das fehlende Unrechts-", "Bold"), ("bewusstsein zur Frage der Schuld;", "Regular"),
                  ("mit dem Gesetz nicht vereinbar", "Regular")], "t1k",
                 "vgl. BGH, Beschl. v. 18.3.1952 – GSSt 2/51, BGHSt 2, 194 (Schuldtheorie)",
                 [("t1", ("tabler", "bulb", 110, GELB), "Unrechtsbewusstsein", GELB),
                  ("t1k", ("tabler", "book", 110, WEISS), "§ 17", WEISS)],
                 [("t1", "denkt"), ("t1e", "froh"), ("t1k", "ernst")])
folie([("t1", P1), ("t1e", f"{P1} › Bärbel: kein Vorsatz"), ("t1k", f"{P1} › Kritik: § 17")], E1)

P2, E2 = theorie(2, "Strenge Schuldtheorie", "t2",
                 [("Jeder Irrtum über die Rechtswidrigkeit", "ExtraBold"), ("ist ein Verbotsirrtum, § 17.", "ExtraBold")],
                 (HELLROT, [("Bärbel handelte vorsätzlich; ohne Schuld nur,", "ExtraBold"),
                            ("wenn der Irrtum unvermeidbar war,", "Regular"),
                            ("sonst nur Strafmilderung (§ 17 Satz 2)", "Regular")]), "t2e",
                 [("Kritik: Wer sich nur über Tatsachen irrt,", "Bold"),
                  ("wird behandelt wie jemand, der sich", "Regular"), ("über das Recht hinwegsetzt", "Regular")], "t2k",
                 "Lehrmaterial: TU Dresden, Übersicht Schuld (Strafrecht IV)",
                 [("t2", ("tabler", "book", 110, WEISS), "§ 17", WEISS),
                  ("t2e", ("tabler", "gavel", 110, HELLROT), "vorsätzlich", HELLROT),
                  ("t2k", ("tabler", "scale", 120, WEISS), "Tatsachen statt Recht", WEISS)],
                 [("t2", "ernst"), ("t2e", "angst"), ("t2k", "denkt")], titelsize=44)
folie([("t2", P2), ("t2e", f"{P2} › Bärbel: Vorsatz bleibt"), ("t2k", f"{P2} › Kritik")], E2)

P3, E3 = theorie(3, "Negative Tatbestandsmerkmale", "t3",
                 [("Rechtfertigungsgründe gehören schon zum", "ExtraBold"),
                  ("Tatbestand, als Merkmale, die fehlen müssen.", "ExtraBold")],
                 (HELLGRUEN, [("§ 16 direkt: Bärbels Vorsatz entfällt", "ExtraBold")]), "t3e",
                 [("Kritik: verwischt den Unterschied zwischen", "Bold"),
                  ("Tatbestand und Rechtswidrigkeit,", "Regular"), ("den das Gesetz macht", "Regular")], "t3k",
                 "Lehrmaterial: Uni Freiburg, AG Strafrecht AT, Übersicht ETBI",
                 [("t3", ("tabler", "puzzle", 110, BLAUHELL), "schon im Tatbestand", BLAUHELL),
                  ("t3e", ("tabler", "book", 110, HELLGRUEN), "§ 16 direkt", HELLGRUEN),
                  ("t3k", ("tabler", "git-branch", 110, WEISS), "Unterschied verwischt", WEISS)],
                 [("t3", "ruhig"), ("t3e", "froh"), ("t3k", "denkt")], titelsize=42)
folie([("t3", P3), ("t3e", f"{P3} › § 16 direkt"), ("t3k", f"{P3} › Kritik")], E3)

P4, E4 = theorie(4, "Eingeschränkte Schuldtheorie", "t4",
                 [("Der Irrtum gleicht einem Tatbestands-", "ExtraBold"), ("irrtum: § 16 entsprechend.", "ExtraBold")],
                 (HELLGRUEN, [("Bärbels Vorsatz entfällt", "ExtraBold")]), "t4e",
                 [("Kritik: keine vorsätzliche rechtswidrige", "Bold"), ("Haupttat", "Regular")], "t4k",
                 "Lehrmaterial: Uni Freiburg, AG Strafrecht AT, Übersicht ETBI",
                 [("t4", ("tabler", "book", 110, WEISS), "§ 16 entsprechend", WEISS),
                  ("teiln", ("tabler", "users", 110, HELLROT), "Helfer straflos", HELLROT)],
                 [("t4", "ruhig"), ("t4e", "froh"), ("t4k", "denkt")], titelsize=42,
                 extra=[blk(110, 640, 1040, 170, ZITAT, "teiln", [("§§ 26, 27: „… vorsätzlich begangener", "Bold", 32, INK),
                                                                ("rechtswidriger Tat …“", "Bold", 32, INK),
                                                                ("eingeweihter Helfer: als Teilnehmer straflos", "Regular", 32, INK)])])
folie([("t4", P4), ("t4e", f"{P4} › Vorsatz entfällt"), ("t4k", f"{P4} › Kritik: keine Haupttat"),
       ("teiln", f"{P4} › Teilnahme, §§ 26, 27")], E4)

P5 = f"{PE_} › Rechtsfolge: 5. rechtsfolgenverweisende eingeschränkte Schuldtheorie"
folie([("t5", P5), ("t5e", f"{P5} › Vorsatzschuld entfällt"), ("t5p", f"{P5} › Teilnahme möglich"),
       ("t5k", f"{P5} › Kritik"), ("hm", f"{P5} › h. M.")], [
    *tafel("t5", "5. Rechtsfolgenverweisende", size=44),
    z("eingeschränkte Schuldtheorie", 110, 160, "t5", "ExtraBold", 40),
    blk(110, 230, 1040, 140, BLAUHELL, "t5e", [("Vorsatz bleibt, nur die Vorsatzschuld entfällt:", "ExtraBold", 32, INK),
                                            ("Rechtsfolge wie § 16, höchstens", "Regular", 32, INK),
                                            ("Strafe wegen Fahrlässigkeit", "Regular", 32, INK)]),
    *okz("Tat bleibt vorsätzlich und rechtswidrig:", 400, "t5p", "Bold", 32),
    z("Helfer als Teilnehmer strafbar, §§ 26, 27", 185, 444, beim("t5p", "Helfer"), size=32),
    *neinz("Kritik: doppelter Vorsatz (Tatbestand", 520, "t5k", "Bold", 32),
    z("und Schuld) wirkt konstruiert", 185, 564, "t5k", size=32),
    blk(110, 640, 1040, 90, HELLGRUEN, "hm", [("im Schrifttum herrschende Meinung", "ExtraBold", 34, INK)]),
    zit("Lehrmaterial: TU Dresden, Übersicht Schuld; Uni Freiburg, AG Strafrecht AT", 110, 742, "hm"),
    *requisit([("t5", ("tabler", "scale", 120, BLAUHELL), "Vorsatzschuld", BLAUHELL),
               ("t5p", ("tabler", "users", 110, HELLGRUEN), "Teilnahme möglich", HELLGRUEN),
               ("hm", ("tabler", "circle-check", 110, HELLGRUEN), "h. M.", HELLGRUEN)]),
    *stehend("BA", FX, [("t5", "ruhig"), ("t5e", "froh"), ("t5k", "denkt"), ("hm", "ernst")]),
])

# ===========================================================================================================================
# G6 Bundesgerichtshof: § 16 entsprechend (Vorsatz bzw. Vorsatzschuld)
# ===========================================================================================================================
PB = f"{PE_} › Bundesgerichtshof"
folie([("bgh", f"{PB}: § 16 entsprechend"), ("bgh2", f"{PB} › keine Strafe wegen der Vorsatztat")], [
    *tafel("bgh", "Bundesgerichtshof"),
    *okz("§ 16 entsprechend", 180, "bgh", "ExtraBold", 36),
    z("mal: Der Vorsatz entfällt.", 185, 260, beim("bgh2", "Vorsatz"), "Bold", 34),
    zit("BGH, Beschl. v. 25.5.2022 – 4 StR 36/22, Rn. 11", 185, 306, beim("bgh2", "Vorsatz")),
    z("mal: Die Vorsatzschuld entfällt.", 185, 370, beim("bgh2", "Vorsatzschuld"), "Bold", 34),
    zit("BGH, Urt. v. 2.11.2011 – 2 StR 375/11, Rn. 32", 185, 416, beim("bgh2", "Vorsatzschuld")),
    zit("vgl. BGH, Urt. v. 27.10.2015 – 3 StR 199/15, Rn. 12", 185, 452, beim("bgh2", "Vorsatzschuld")),
    blk(110, 520, 1040, 90, HELLGRUEN, beim("bgh2", "Ergebnis"), [("Im Ergebnis: keine Strafe wegen der Vorsatztat", "ExtraBold", 33, INK)]),
    *requisit([("bgh", ("tabler", "gavel", 110, WEISS), "Bundesgerichtshof", WEISS)]),
    *stehend("HE", FX, [("bgh", "ruhig"), ("bgh2", "froh")]),
])

# ===========================================================================================================================
# H Ergebnis: § 229 StGB (Irrtum vermeidbar?)
# ===========================================================================================================================
PF = "B. Bärbel, § 229 StGB"
folie([("erg", "A. Bärbel › Ergebnis: keine Strafe wegen Vorsatztat"), ("fahr", f"{PF} › Irrtum vermeidbar?"),
       ("lat", f"{PF} › Ruf und Laterne"), ("fahr2", f"{PF} › vermeidbar: strafbar"),
       ("gegen", f"{PF} › Gegenfall: unvermeidbar")], [
    *tafel("erg", "Ergebnis"),
    *neinz("nicht strafbar wegen vorsätzlicher Körperverletzung", 180, "erg", "Bold", 32, kreuz=beim("erg", "nicht")),
    z("§ 229: fahrlässige Körperverletzung?", 110, 260, "fahr", "ExtraBold", 35),
    z("fahrlässig nur, wenn der Irrtum vermeidbar war", 110, 312, beim("fahr", "Fahrlässig"), size=33),
    zit("BGH, Urt. v. 2.11.2011 – 2 StR 375/11, Rn. 36; BGHSt 45, 378 (4 StR 558/99)", 110, 360, beim("fahr", "Fahrlässig")),
    *okz("Helge hatte gerufen;", 430, "lat", "Bold", 33),
    *okz("unter der Laterne war das Handy zu erkennen", 476, beim("lat", "unter"), size=33),
    blk(110, 556, 1040, 120, HELLROT, "fahr2", [("Ein kurzer Blick hätte genügt: vermeidbar.", "ExtraBold", 32, INK),
                                             ("Bärbel ist strafbar nach § 229.", "ExtraBold", 32, INK)]),
    blk(110, 706, 1040, 90, BLAUHELL, "gegen", [("Gegenfall: unvermeidbar, dann straflos", "ExtraBold", 34, INK)]),
    *requisit([("erg", ("tabler", "shield-x", 110, HELLGRUEN), "keine Vorsatztat", HELLGRUEN),
               ("lat", ("tabler", "bulb", 110, GELB), "Laterne", GELB),
               ("fahr2", ("tabler", "gavel", 110, HELLROT), "§ 229", HELLROT),
               ("gegen", ("tabler", "moon-stars", 110, BLAUHELL), "unvermeidbar", BLAUHELL)]),
    *paar("BA", [("erg", "ruhig"), ("fahr", "denkt"), ("fahr2", "muede"), ("gegen", "ernst")], "HE",
          [("erg", "ruhig"), ("lat", "froh")]),
])

# ===========================================================================================================================
# I Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Standort: Schuld"), ("k1", "Klausurtipp › zuerst: gerechtfertigt, wenn wahr?"),
       ("k2", "Klausurtipp › Streit nur bei verschiedenen Ergebnissen"), ("k3", "Klausurtipp › strenge Schuldtheorie"),
       ("k4", "Klausurtipp › eingeschränkte Theorien: Teilnehmer")], [
    *tafel("tipp", "Klausurtipp: Wo und wie?", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("h. M.: in der Schuld prüfen,", 200, 200, "tipp", "ExtraBold", 35),
    z("als Frage der Vorsatzschuld", 240, 252, beim("tipp", "Frage"), size=34),
    linienzug([(130, 320), (1130, 320)], "k1", breite=3),
    z("Zuerst: Wäre der Täter gerechtfertigt,", 200, 344, "k1", "ExtraBold", 34),
    z("wenn seine Vorstellung stimmte?", 240, 396, beim("k1", "wenn"), size=34),
    linienzug([(130, 464), (1130, 464)], "k2", breite=3),
    z("Streit nur, wenn die Ergebnisse auseinandergehen:", 200, 488, "k2", "ExtraBold", 32),
    z("strenge Schuldtheorie: wenn Irrtum vermeidbar", 240, 546, "k3", size=33),
    z("eingeschränkte Theorien: nur bei Teilnehmern", 240, 600, "k4", size=33),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# J Gutachtenaufbau (Lexi), Punkt für Punkt
# ===========================================================================================================================
folie([("sch", "Klausurschema · Gutachtenaufbau"), ("s1", "Klausurschema › I. Tatbestand"),
       ("s2", "Klausurschema › II. Rechtswidrigkeit"), ("s3", "Klausurschema › III. Schuld: ETBI"),
       ("s4", "Klausurschema › B. § 229 StGB")], [
    *tafel("sch", "Klausurschema: Bärbel"),
    z("A. §§ 223, 224 Abs. 1 Nr. 2 StGB", 110, 170, "s1", "ExtraBold", 34),
    *plusminus("I. Tatbestand", 150, 230, "s1", True, size=34, stil="Bold"),
    *plusminus("II. Rechtswidrigkeit: keine Notwehrlage", 150, 290, "s2", True, size=34, stil="Bold"),
    z("III. Schuld: Erlaubnistatbestandsirrtum,", 150, 350, "s3", "Bold", 34),
    *plusminus("Vorsatzschuld entfällt", 210, 404, beim("s3", "Vorsatzschuld"), False, size=34),
    *plusminus("B. § 229 StGB: fahrlässige Körperverletzung", 110, 490, "s4", True, size=34, stil="ExtraBold"),
    *redet("LX_erklaert", FX, FB, FR + 40, "sch", "merke"),
    ns("Lexi", FX, FB, "sch", GELB, d=0.2),
])

# ===========================================================================================================================
# K Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Wer sich irrig eine Notwehrlage vorstellt,", 0)], [("wird nicht wegen der ", 0), ("Vorsatztat", "a"),
                 (" bestraft.", 0)]], 750, 300, 42, "merke", {"a": beim("merke", "Vorsatztat")}),
    *markertext([[("Höchstens wegen ", 0), ("Fahrlässigkeit", "b"), (", wenn", 0)],
                 [("er den Irrtum hätte ", 0), ("vermeiden", "c"), (" können.", 0)]],
                750, 500, 42, "m2", {"b": beim("m2", "Fahrlässigkeit"), "c": beim("m2", "vermeiden")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
