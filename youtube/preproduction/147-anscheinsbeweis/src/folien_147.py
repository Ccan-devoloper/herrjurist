"""Folge 147 · Anscheinsbeweis, Vermutung, Beweislastumkehr: Nie mehr verwechseln – Serienstandard Open Peeps (Katzenkönig).
Beispielfall: Auffahrunfall im Stadtverkehr; Frau Kretschmer (vorne) bremst, Herr Hertel fährt auf (unstreitig), nur
Blechschaden (2.400 €). Er behauptet eine grundlose Vollbremsung; Zeugen gibt es nicht.
Szenen laut ../SZENENPLAN.md: A1 Auf der Stadtstraße, A2 Klage und Frage, B Sachverhalt, C1 Drei Werkzeuge, C2 Grundregel,
D1–D3 Anscheinsbeweis (Grundlage / Was ändert sich? / Gegenwehr), E1–E3 gesetzliche Vermutung (§ 292 ZPO, § 477 BGB),
F1–F2 Beweislastumkehr (§ 280 Abs. 1 S. 2 BGB), G1–G3 der Fall (Anschein, Behauptung, § 4 Abs. 1 StVO), G4 zurück auf der
Straße (Ergebnis), H Merktabelle, I Klausurtipp (Lexi), J Merksatz (Lexi).
DARSTELLUNG: kein Aufprall im Bild, keine Verletzten – das hintere Auto rollt heran und steht danach Stoßstange an Stoßstange,
ein Pfeil zeigt auf die eingedrückte Stoßstange. Zwei Handlungsgeräusche: leises Abbremsen (szene_147bremse_1), Autotür
(szene_147tuer_1); Herkunft ../geraeusche_herkunft.json. Kein Aufprallgeräusch.
Gleiche Tafelstruktur für alle drei Werkzeuge: Kopfzeile mit Werkzeugfarbe (Anschein Blau, Vermutung Gelb, Umkehr Grün) und
Rasterleiste „Grundlage · Was ändert sich? · Gegenwehr“, der aktuelle Punkt farbig.
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/
punkt als eigene Kopie aus Folge 141 (gemeinsame Dateien unverändert); neu: strasse(), auto(), raster(), wtafel(), zelle().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_147/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_147/" in n:
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


# --- neue Hilfsfunktionen und Konstanten Folge 147 --------------------------------------------------------------------------
HELLBLAU = (222, 234, 252, 255)
HELLGELB = (253, 242, 205, 255)
BODEN, FH = 860, 480
X1, X2 = 1420, 1720                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
PX, PY, PU = 1570, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"HE": "Herr Hertel", "KR": "Frau Kretschmer"}
NFARBE = {"HE": BLAU, "KR": ROT}            # wie die Autos: ihres rot, seines blau
ROTTEXT = (200, 60, 45, 255)
WFARBE = {"A": BLAU, "V": GELB, "U": GRUEN}   # Werkzeugfarben: Anscheinsbeweis, Vermutung, Umkehr
RASTER = ["Grundlage", "Was ändert sich?", "Gegenwehr"]


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


def paar(c0, l, lf, r, rf, bis=None):
    """Tafelszene: zwei Figuren rechts der Tafel, beide blicken zur Tafel (nach links)."""
    return [*fig(l, X1, FB, FR, lf, bis=bis), ns(NAME[l], X1, FB, c0, NFARBE[l], d=0.1, bis=bis),
            *fig(r, X2, FB, FR, rf, d=0.2, bis=bis), ns(NAME[r], X2, FB, c0, NFARBE[r], d=0.3, bis=bis)]


def wtafel(cue, titel_, farbe, h=840):
    """Werkzeugtafel: Karte links, Farbstreifen der Werkzeugfarbe vor dem Titel (gleiche Struktur für alle drei)."""
    assert 130 + F("ExtraBold", 46).getlength(glyphen(titel_)) <= 1170, f"Titel zu breit: {titel_}"
    return [karte(60, 60, 1140, h, cue), karte(84, 98, 24, 60, cue, fill=farbe, rund=8, schatten=0, rand=3),
            titel(titel_, 130, 100, cue, 46)]


def raster(folge, farbe, y=172):
    """Rasterleiste unter dem Titel: „Grundlage · Was ändert sich? · Gegenwehr“, der aktuelle Punkt in Werkzeugfarbe.
    folge = [(cue, index)]; jeder Zustand ersetzt den vorigen (harter Schnitt)."""
    els = []
    for i, (c, k) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else None
        x = 110
        for j, t in enumerate(RASTER):
            aktiv = j == k
            e = pl(f"{j + 1}. {t}", x, y, c, fill=farbe if aktiv else (240, 240, 240, 255), size=28,
                   farbe=INK if aktiv else TEXT, bis=b, anim="cut" if i else "pop")
            els.append(e)
            x += e.sprite.width + 14
        assert x <= 1180, "Rasterleiste zu breit"
    return els


# --- Straße (Seitenansicht), Autos -------------------------------------------------------------------------------------
GRAUSTR = (206, 206, 202, 255)
GRAS = (205, 234, 196, 255)
STR_O, STR_U = 690, 850                      # Fahrbahn: Oberkante, Unterkante
FAHR = 832                                   # Unterkante der Autos und der Figuren auf der Fahrbahn
CW = 380                                     # Autobreite (Icon tabler:car, Sprite 318 px breit, Front rechts)


def strasse(cue):
    """Stadtstraße in Seitenansicht: graue Fahrbahn mit Mittellinie, Grünstreifen davor (wie Folge 124, eigene Kopie)."""
    s = 2
    im = Image.new("RGBA", (1860 * s, (1000 - STR_O) * s))
    dr = ImageDraw.Draw(im)
    dr.rectangle((0, 0, 1860 * s, (STR_U - STR_O) * s), fill=GRAUSTR)
    dr.line((0, 0, 1860 * s, 0), fill=INK, width=6 * s)
    dr.line((0, (STR_U - STR_O) * s, 1860 * s, (STR_U - STR_O) * s), fill=INK, width=6 * s)
    for x in range(30, 1860, 150):
        dr.rounded_rectangle((x * s, 74 * s, (x + 80) * s, 86 * s), 5 * s, fill=WEISS)
    dr.rectangle((0, (STR_U - STR_O + 3) * s, 1860 * s, (1000 - STR_O) * s), fill=GRAS)
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    e = El(im, 30, STR_O, cue, "cut", 0.0, None, name="strasse")
    return hart(e) if cue == NULL else e


def kulisse(c):
    """Häuser und Bäume hinter der Fahrbahn (keine Ampel: nichts im Bild gibt einen Grund zum Bremsen)."""
    h = (lambda e: hart(e)) if c == NULL else (lambda e: e)
    return [strasse(c),
            h(ficon("tabler", "buildings", 1290, STR_O + 4, 230, c, fuell=GELB, anim="cut")),
            h(ficon("tabler", "tree", 1560, STR_O + 4, 190, c, fuell=GRUEN, anim="cut")),
            h(ficon("tabler", "building", 1760, STR_O + 4, 200, c, fuell=LILA, anim="cut")),
            h(ficon("tabler", "tree", 640, STR_O + 4, 170, c, fuell=GRUEN, anim="cut"))]


def auto(cx, cue, farbe, bis=None):
    return ficon("tabler", "car", cx, FAHR, CW, cue, fuell=farbe, anim="cut", bis=bis)


def zelle(x, y, w, h, fill, cue, zeilen, size=32):
    """Tabellenzelle: Karte + zentrierte Zeilen [(text, stil)] (erste Zeile Bold)."""
    els = [karte(x, y, w, h, cue, fill=fill, rund=14, schatten=4, rand=4)]
    lh = int(size * 1.3)
    y0 = y + (h - lh * len(zeilen)) / 2
    for i, (t, st, sz) in enumerate(zeilen):
        tw = F(st, sz).getlength(glyphen(t))
        assert tw <= w - 24, f"Zelltext zu breit: {t}"
        els.append(z(t, x + (w - tw) / 2, y0 + i * lh, cue, st, sz, rechts=1820,
                     farbe=TEXT if st == "Regular" and sz < 30 else INK))
    return els


# ===========================================================================================================================
# A1 Fall: auf der Stadtstraße – sie bremst, er fährt auf (kein Aufprallbild)
# ===========================================================================================================================
RX0, RX1 = 1000, 1060                        # rotes Auto (Frau Kretschmer): fährt bis RX0, bremst bis RX1
BX = RX1 - 318 + 4                           # blaues Auto (Herr Hertel) steht danach Stoßstange an Stoßstange
BX1 = RX0 - 318 - 150                        # blaues Auto vorher: 150 px Abstand
BRE = beim("bremst", "bremst")
AUF_E = beim("auf", "auf", ende=True)
HEX, KRX = 330, 1440                         # Herr Hertel steigt links aus (blickt nach rechts), Frau Kretschmer rechts
AUS = beim("aus", "steigt")
folie([(NULL, "Fall · Auf der Stadtstraße"), ("auf", "Fall · Der Auffahrunfall"), ("h1", "Fall · Die Behauptung")], [
    *kulisse(NULL),
    hart(pl("Ein Nachmittag im Stadtverkehr", 70, 30, NULL, fill=GELB, size=40)),
    # rotes Auto fährt, bremst sanft und steht; blaues Auto rollt heran und steht danach direkt dahinter
    bewegt(auto(RX0, NULL, ROT, bis=BRE), NULL, BRE, -300, 0),
    szene(bewegt(auto(RX1, BRE, ROT), BRE, (BRE[0], round(BRE[1] + 1.1, 3)), RX0 - RX1, 0), "147bremse*", 1.0, 0.0),
    bewegt(auto(BX1, NULL, BLAU, bis=BRE), NULL, BRE, -300, 0),           # fährt mit Abstand hinterher
    bewegt(auto(BX, BRE, BLAU), BRE, AUF_E, BX1 - BX, 0),                  # rollt beim Bremsen heran, steht dann dahinter
    # Beschriftung der Autos fährt mit, bis die Figur selbst im Bild ist
    bewegt(pl("Frau Kretschmer", RX0, FAHR - 300, "vorn", fill=ROT, size=30, anker="m", bis=BRE), NULL, BRE, -300, 0),
    bis_(pl("Frau Kretschmer", RX1, FAHR - 300, BRE, fill=ROT, size=30, anker="m", anim="cut"), "blech"),
    bewegt(pl("Herr Hertel", BX1, FAHR - 300, "hinten", fill=BLAU, size=30, anker="m", bis=BRE), NULL, BRE, -300, 0),
    bewegt(pl("Herr Hertel", BX, FAHR - 300, BRE, fill=BLAU, size=30, anker="m", anim="cut", bis=AUS), BRE, AUF_E, BX1 - BX, 0),
    bis_(pl("Frau Kretschmer bremst", 70, 120, BRE, fill=WEISS, size=36), "h1"),
    bis_(pl("Herr Hertel fährt ihr hinten auf", 70, 205, beim("auf", "fährt"), fill=WEISS, size=36), "h1"),
    pl("Verletzt: niemand", 1180, 30, beim("blech", "Verletzt"), fill=GRUEN, size=36),
    pl("Stoßstange eingedrückt", 1180, 115, beim("blech", "Stoßstange"), fill=HELLROT, size=36),
    pfeil(1300, 185, RX1 - 150, FAHR - 95, beim("blech", "Stoßstange"), breite=8, kopf=26),
    # Frau Kretschmer steigt aus und sieht nach der Stoßstange (blickt nach links), dann Herr Hertel
    *fig("KR", KRX, FAHR, FH, [(beim("blech", "aber"), "sorge"), ("aus", "ernst"), ("h1", "skeptisch")]),
    ns("Frau Kretschmer", KRX, FAHR, beim("blech", "aber"), NFARBE["KR"], d=0.1),
    szene(peep_voll("HE_ruhig_r", HEX, FAHR, FH, AUS, anim="pop", bis="h1"), "147tuer*", 1.0, 0.0),
    ns("Herr Hertel", HEX, FAHR, AUS, NFARBE["HE"], d=0.1),
    *redet("HE_redet_r", HEX, FAHR, FH, "h1", "klage"),
    blase("sprech", 760, 210, "h1", 770, 250, inhalt=["Sie hat ohne jeden Grund", "eine Vollbremsung gemacht!"],
          textsize=38, figur=("HE_redet_r", HEX, FAHR, FH), bis="klage"),
])

# ===========================================================================================================================
# A2 Fall: Klage und Fragen (freie Bühne)
# ===========================================================================================================================
KL, HR, MX = 330, 1590, 960
folie([("klage", "Fall · Die Klage"), ("frage", "Fall · Die Fragen")], [
    boden("klage"),
    *fig("KR", KL, BODEN, FH, [("klage", "ernst_r"), ("best", "skeptisch_r"), ("frage", "sorge_r"), ("frage2", "ruhig_r")]),
    ns("Frau Kretschmer", KL, BODEN, "klage", NFARBE["KR"], d=0.1),
    *fig("HE", HR, BODEN, FH, [("klage", "ruhig"), ("best", "ernst"), ("zeug", "denkt"), ("frage2", "sorge")], d=0.15),
    ns("Herr Hertel", HR, BODEN, "klage", NFARBE["HE"], d=0.25),
    pl("Frau Kretschmer verlangt Ersatz", 70, 30, beim("klage", "Ersatz"), fill=ROT, size=38),
    ficon("tabler", "coin-euro", MX, 600, 200, beim("klage", "zweitausendvierhundert"), fuell=GELB, bis="zeug"),
    pl("Schaden: 2.400 €", MX, 640, beim("klage", "zweitausendvierhundert"), fill=GELB, size=36, anker="m", bis="zeug"),
    pl("Herr Hertel: nicht schuld", 70, 115, beim("best", "bestreitet"), fill=BLAU, size=38),
    ficon("tabler", "eye-off", MX, 600, 180, "zeug", fuell=WEISS, bis="frage"),
    pl("keine Zeugen", MX, 640, "zeug", fill=WEISS, size=36, anker="m"),
    ficon("tabler", "question-mark", MX, 600, 150, "frage", fuell=PINK),
    pl("Muss sie beweisen: zu dicht aufgefahren?", 70, 200, "frage", fill=PINK, size=38),
    pl("Reicht seine Behauptung?", 70, 285, "frage2", fill=PINK, size=38),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_147(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=38, zeilenabstand=1.30)
        els += e; y += 16
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=34))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_147("sv", [
    "An einem Nachmittag fährt Frau Kretschmer mit ihrem Auto durch die Stadt, Herr Hertel mit seinem Auto direkt "
    "hinter ihr. Frau Kretschmer bremst, Herr Hertel fährt ihr hinten auf. Verletzt wird niemand. Die Stoßstange ihres "
    "Autos ist eingedrückt, der Schaden beträgt 2.400 Euro. Dass er aufgefahren ist, ist unstreitig.",
    "Frau Kretschmer verlangt von Herrn Hertel Ersatz. Herr Hertel bestreitet, schuld zu sein: Sie habe ohne jeden Grund "
    "eine Vollbremsung gemacht. Frau Kretschmer bestreitet das. Zeugen oder andere Beweise gibt es nicht.",
], "Muss sie ihm sein Verschulden beweisen, und wie kann er sich wehren?")

# ===========================================================================================================================
# C1 Drei Werkzeuge, ein Raster
# ===========================================================================================================================
WK = [("w1", "Anscheins-", "beweis", BLAU), ("w2", "gesetzliche", "Vermutung", GELB), ("w3", "Beweislast-", "umkehr", GRUEN)]
FR_ = [("r1", "Worauf beruht es?"), ("r2", "Was ändert sich?"), ("r3", "Wie wehrt sich der Gegner?")]
els_c1 = [*tafel("drei", "Drei Werkzeuge, ein Raster"),
          z("helfen dem, der etwas beweisen muss", 110, 178, beim("drei", "helfen"), "Bold", 34),
          pl("… und werden ständig verwechselt", 110, 238, beim("drei", "ständig"), fill=PINK, size=30)]
for k, (c, a, b, fa) in enumerate(WK):
    x = 110 + k * 355
    els_c1 += [karte(x, 320, 330, 130, c, fill=fa, rund=16, schatten=5, rand=4)]
    for j, t in enumerate((a, b)):
        tw = F("ExtraBold", 36).getlength(t)
        els_c1.append(z(t, x + (330 - tw) / 2, 336 + j * 50, c, "ExtraBold", 36))
els_c1.append(z("Drei Fragen an jedes Werkzeug:", 110, 490, "raster", "ExtraBold", 36))
for k, (c, t) in enumerate(FR_):
    y = 565 + k * 95
    els_c1 += [karte(110, y, 64, 64, c, fill=WEISS, rund=12, schatten=4, rand=4),
               z(f"{k + 1}", 142 - F("ExtraBold", 36).getlength(f"{k + 1}") / 2, y + 7, c, "ExtraBold", 36),
               z(t, 200, y + 7, c, "Bold", 38)]
folie([("drei", "Drei Werkzeuge"), ("raster", "Drei Werkzeuge › drei Fragen")], rechts_frei([
    *els_c1,
    *requisit([("drei", ("tabler", "tool", 110, WEISS), "3 Werkzeuge", WEISS),
               ("raster", ("tabler", "list-check", 100, WEISS), "3 Fragen", GELB)]),
    *paar("drei", "KR", [("drei", "ruhig"), ("raster", "skeptisch")], "HE", [("drei", "ruhig"), ("r3", "denkt")]),
]))

# ===========================================================================================================================
# C2 Ausgangspunkt: die Grundregel (Verweis Folge 141)
# ===========================================================================================================================
folie([("grund", "Ausgangspunkt · Grundregel der Beweislast")], rechts_frei([
    *tafel("grund", "Ausgangspunkt: die Grundregel"),
    blk(110, 180, 760, 64, LILA, beim("grund", "Video"), [("Mehr dazu: Video „Beweislast ZPO“", "ExtraBold", 30, INK)]),
    z("Jede Partei beweist die Voraussetzungen", 110, 290, beim("grund", "Jede"), "Bold", 38),
    z("der Norm, die ihr günstig ist.", 110, 345, beim("grund", "Norm"), "Bold", 38),
    zit("vgl. BGH, Urt. v. 20.3.2024 – IV ZR 68/22, Rn. 68", 110, 405, beim("grund", "Norm")),
    blk(110, 490, 1040, 130, GELB, "grund2", [("Bleibt es unklar, verliert,", "ExtraBold", 38, INK),
                                               ("wer die Beweislast trägt.", "ExtraBold", 38, INK)]),
    *requisit([("grund", ("tabler", "scale", 130, WEISS), "Grundregel", WEISS),
               ("grund2", ("tabler", "question-mark", 100, PINK), "unklar?", PINK)]),
    *paar("grund", "KR", [("grund", "ruhig"), ("grund2", "sorge")], "HE", [("grund", "ernst")]),
]))

# ===========================================================================================================================
# D1–D3 1. Anscheinsbeweis
# ===========================================================================================================================
folie([("a1", "1. Anscheinsbeweis › Grundlage")], rechts_frei([
    *wtafel("a1", "1. Anscheinsbeweis", BLAU), *raster([("a1", 0)], BLAU),
    z("nicht allgemein im Gesetz geregelt", 110, 260, beim("a2", "allgemein"), "Bold", 36),
    z("beruht auf einem Erfahrungssatz:", 110, 320, beim("a2", "Erfahrungssatz"), "Bold", 36),
    blk(110, 390, 1040, 70, HELLBLAU, "a3", [("typischer Geschehensablauf", "ExtraBold", 34, INK)]),
    z("feststehende Tatsachen: Schluss auf", 110, 485, beim("a3", "feststehenden"), size=34),
    z("eine Ursache oder ein Verschulden", 110, 535, beim("a3", "Ursache"), size=34),
    zit("BGH, Urt. v. 3.12.2024 – VI ZR 18/24, Rn. 19", 110, 590, beim("a3", "Ursache")),
    z("Teil der freien Beweiswürdigung, § 286 ZPO", 110, 660, "a4", "Bold", 36),
    zit("vgl. BGH, Urt. v. 11.12.2018 – KZR 26/17, Rn. 49 f.", 110, 715, beim("a4", "freien")),
    *requisit([("a1", ("tabler", "bulb", 100, BLAU), "Anscheinsbeweis", BLAU),
               (beim("a2", "Erfahrungssatz"), ("tabler", "repeat", 100, WEISS), "Erfahrungssatz", WEISS),
               ("a4", ("tabler", "scale", 130, WEISS), "§ 286 ZPO", WEISS)]),
    *paar("a1", "KR", [("a1", "ruhig"), ("a3", "skeptisch")], "HE", [("a1", "ruhig"), (beim("a2", "allgemein"), "denkt")]),
]))

QA = ["„Die Grundsätze des Anscheinsbeweises begründen …",
      "weder eine zwingende Beweisregel noch eine Beweisvermutung",
      "und auch keine Beweislastumkehr …“"]
qa, qa_y = wortlaut(80, 545, 1100, QA, "BGH, Urt. v. 26.1.2016 – XI ZR 91/14, Rn. 24", "a7", marken=[
    (1, "Beweisvermutung", beim("a7", "Beweisvermutung")), (2, "keine Beweislastumkehr", beim("a7", "keine"))], size=32)
folie([("a5", "1. Anscheinsbeweis › Was ändert sich?")], rechts_frei([
    *wtafel("a5", "1. Anscheinsbeweis", BLAU), *raster([("a5", 1)], BLAU),
    z("zu beweisen: nur die Tatsachen,", 110, 260, beim("a5", "Bewiesen"), "Bold", 36),
    z("an die der Erfahrungssatz anknüpft", 110, 312, beim("a5", "Erfahrungssatz"), "Bold", 36),
    zit("BGH, Urt. v. 11.12.2018 – KZR 26/17, Rn. 50", 110, 368, beim("a5", "anknüpft")),
    blk(110, 430, 1040, 74, BLAU, "a6", [("Die Beweislast bleibt, wo sie war.", "ExtraBold", 36, INK)]),
    *qa,
    *requisit([("a5", ("tabler", "file-check", 100, WEISS), "Tatsachen beweisen", WEISS),
               ("a6", ("tabler", "scale", 130, GELB), "Beweislast bleibt", GELB),
               ("a7", ("tabler", "gavel", 100, WEISS), "Bundesgerichtshof", WEISS)]),
    *paar("a5", "KR", [("a5", "ruhig"), ("a6", "froh")], "HE", [("a5", "denkt"), ("a6", "sorge")]),
]))

folie([("a8", "1. Anscheinsbeweis › Gegenwehr: erschüttern")], rechts_frei([
    *wtafel("a8", "1. Anscheinsbeweis", BLAU), *raster([("a8", 2)], BLAU),
    blk(110, 260, 1040, 74, BLAU, beim("a8", "erschüttern"), [("Der Gegner muss den Anschein nur erschüttern.", "ExtraBold", 34, INK)]),
    z("Tatsachen, die einen atypischen Verlauf", 110, 375, "a9", "Bold", 36),
    z("ernsthaft möglich machen", 110, 427, beim("a9", "ernsthaft"), "Bold", 36),
    z("diese Tatsachen: voll beweisen", 110, 505, "a10", "ExtraBold", 36, farbe=ROTTEXT),
    zit("BGH, Urt. v. 26.1.2016 – XI ZR 91/14, Rn. 24; Urt. v. 13.12.2016 – VI ZR 32/16, Rn. 11", 110, 562, "a10"),
    linienzug([(110, 625), (1150, 625)], "a11", breite=3),
    z("Gelingt das: Der Anschein fällt weg.", 110, 650, "a11", "Bold", 36),
    z("beweisbelastete Partei: voller Beweis", 110, 705, beim("a11", "beweisbelastete"), "Bold", 36),
    *requisit([("a8", ("tabler", "hand-stop", 100, WEISS), "erschüttern", BLAU),
               ("a10", ("tabler", "file-search", 100, WEISS), "voll beweisen", HELLROT),
               ("a11", ("tabler", "scale", 130, WEISS), "voller Beweis", WEISS)]),
    *paar("a8", "KR", [("a8", "ruhig"), ("a11", "ernst")], "HE", [("a8", "denkt"), ("a10", "ernst"), ("a11", "sorge")]),
]))

# ===========================================================================================================================
# E1–E3 2. Gesetzliche Vermutung
# ===========================================================================================================================
W292 = ["„Stellt das Gesetz für das Vorhandensein einer Tatsache",
        "eine Vermutung auf, so ist der Beweis des Gegenteils",
        "zulässig, sofern nicht das Gesetz ein anderes",
        "vorschreibt. …“"]
w292, w292_y = wortlaut(80, 335, 1100, W292, "§ 292 S. 1 ZPO", beim("v2", "Paragraf"), marken=[
    (1, "Vermutung", beim("v2", "Vermutung")), (1, "Beweis des Gegenteils", beim("v2", "Beweis"))], size=33)
folie([("v1", "2. Gesetzliche Vermutung › Grundlage: § 292 ZPO")], rechts_frei([
    *wtafel("v1", "2. Gesetzliche Vermutung", GELB), *raster([("v1", 0)], GELB),
    z("Grundlage: das Gesetz selbst", 110, 260, "v2", "Bold", 36),
    *w292,
    *requisit([("v1", ("tabler", "book", 100, GELB), "gesetzliche Vermutung", GELB),
               (beim("v2", "Paragraf"), ("tabler", "file-text", 100, WEISS), "§ 292 ZPO", WEISS)]),
    *paar("v1", "KR", [("v1", "ruhig")], "HE", [("v1", "ruhig"), (beim("v2", "Beweis"), "denkt")]),
]))

W477 = ["„Zeigt sich innerhalb eines Jahres seit Gefahrübergang",
        "ein von den Anforderungen nach § 434 oder § 475b",
        "abweichender Zustand der Ware, so wird vermutet, dass",
        "die Ware bereits bei Gefahrübergang mangelhaft war, …“"]
w477, w477_y = wortlaut(80, 370, 1100, W477, "§ 477 Abs. 1 S. 1 BGB", beim("v4", "Paragraf"), marken=[
    (0, "innerhalb eines Jahres", beim("v4", "innerhalb")), (2, "abweichender Zustand", beim("v4", "abweichender")),
    (2, "wird vermutet", "v5"), (3, "bereits bei Gefahrübergang mangelhaft", beim("v5", "mangelhaft"))], size=31)
folie([("v3", "2. Gesetzliche Vermutung › Was ändert sich?"), ("v4", "2. Gesetzliche Vermutung › Beispiel § 477 BGB")],
      rechts_frei([
    *wtafel("v3", "2. Gesetzliche Vermutung", GELB), *raster([("v3", 1)], GELB),
    z("zu beweisen: nur die Vermutungsbasis", 110, 255, beim("v3", "Bewiesen"), "Bold", 36),
    z("nicht: die vermutete Tatsache selbst", 110, 305, beim("v3", "vermutete"), size=34),
    *w477,
    pl("Vermutungsbasis: abweichender Zustand im 1. Jahr", 110, w477_y + 16, beim("v4", "abweichender"), fill=GELB, size=28),
    pl("vermutet: mangelhaft schon bei Gefahrübergang", 110, w477_y + 84, "v5", fill=WEISS, size=28),
    z("Jahresfrist: Verträge ab dem 1.1.2022", 110, w477_y + 160, "v6", "Bold", 32),
    zit("Art. 229 § 58 EGBGB", 720, w477_y + 166, "v6"),
    *requisit([("v3", ("tabler", "file-check", 100, GELB), "Vermutungsbasis", GELB),
               ("v4", ("tabler", "shopping-cart", 110, WEISS), "§ 477 BGB", WEISS),
               ("v6", ("tabler", "calendar", 100, WEISS), "seit 1.1.2022", WEISS),
               (beim("v6", "Mehr"), ("tabler", "shopping-cart", 110, LILA), "Video „Verbrauchsgüterkauf“", LILA)]),
    *paar("v3", "KR", [("v3", "ruhig"), ("v5", "froh")], "HE", [("v3", "ruhig"), ("v4", "denkt")]),
]))

folie([("v7", "2. Gesetzliche Vermutung › Gegenwehr: Beweis des Gegenteils")], rechts_frei([
    *wtafel("v7", "2. Gesetzliche Vermutung", GELB), *raster([("v7", 2)], GELB),
    *neinz("Erschüttern reicht nicht.", 262, beim("v7", "Erschüttern"), "Bold", 36, x=160),
    blk(110, 340, 1040, 74, GELB, beim("v7", "Gegenteil"), [("Der Gegner muss das Gegenteil voll beweisen.", "ExtraBold", 34, INK)]),
    zit("§ 292 S. 1 ZPO; vgl. BGH, Urt. v. 6.5.2026 – VIII ZR 257/23, Rn. 52 (zu § 477 a. F.)", 110, 432, beim("v7", "Gegenteil")),
    z("Bleibt es unklar: Die Vermutung gilt.", 110, 505, "v8", "Bold", 36),
    zit("vgl. BGH, Urt. v. 6.5.2026 – VIII ZR 257/23, Rn. 55", 110, 560, "v8"),
    linienzug([(110, 625), (1150, 625)], "v9", breite=3),
    z("Überschrift von § 477 BGB:", 110, 650, "v9", "Bold", 36),
    blk(110, 712, 560, 74, GELB, beim("v9", "Beweislastumkehr"), [("„Beweislastumkehr“", "ExtraBold", 36, INK)]),
    *requisit([("v7", ("tabler", "shield-check", 100, WEISS), "Gegenteil beweisen", GELB),
               ("v8", ("tabler", "question-mark", 100, WEISS), "unklar: Vermutung gilt", WEISS),
               ("v9", ("tabler", "book", 100, GELB), "§ 477 BGB", GELB)]),
    *paar("v7", "KR", [("v7", "ruhig"), ("v8", "froh")], "HE", [("v7", "ernst"), ("v8", "sorge"), ("v9", "denkt")]),
]))

# ===========================================================================================================================
# F1–F2 3. Beweislastumkehr
# ===========================================================================================================================
W280 = ["„(1) Verletzt der Schuldner eine Pflicht aus dem",
        "Schuldverhältnis, so kann der Gläubiger Ersatz des hierdurch",
        "entstehenden Schadens verlangen. Dies gilt nicht, wenn der",
        "Schuldner die Pflichtverletzung nicht zu vertreten hat. …“"]
w280, w280_y = wortlaut(80, 450, 1100, W280, "§ 280 Abs. 1 BGB", beim("u3", "Paragraf"), marken=[
    (2, "Dies gilt nicht", beim("u3", "Dies")), (3, "nicht zu vertreten", beim("u3", "vertreten"))], size=31)
folie([("u1", "3. Beweislastumkehr › Grundlage")], rechts_frei([
    *wtafel("u1", "3. Beweislastumkehr", GRUEN), *raster([("u1", 0)], GRUEN),
    *neinz("kein Schluss von Tatsache auf Tatsache", 258, beim("u2", "keinen"), "Bold", 36, x=160),
    z("Beweislastregel: verteilt die Beweislast", 110, 330, beim("u2", "Beweislastregel"), "Bold", 36),
    z("für ein Merkmal anders als die Grundregel", 110, 382, beim("u2", "Merkmal"), "Bold", 36),
    *w280,
    *requisit([("u1", ("tabler", "arrows-exchange", 110, GRUEN), "Beweislastumkehr", GRUEN),
               (beim("u3", "Paragraf"), ("tabler", "file-text", 100, WEISS), "§ 280 Abs. 1 S. 2 BGB", WEISS)]),
    *paar("u1", "KR", [("u1", "ruhig")], "HE", [("u1", "ruhig"), ("u3", "denkt")]),
]))

folie([("u4", "3. Beweislastumkehr › Was ändert sich?"), ("u7", "3. Beweislastumkehr › Gegenwehr: voller Beweis")],
      rechts_frei([
    *wtafel("u4", "3. Beweislastumkehr", GRUEN), *raster([("u4", 1), ("u7", 2)], GRUEN),
    blk(110, 258, 1040, 74, GRUEN, beim("u4", "Die"), [("Die Beweislast selbst wechselt.", "ExtraBold", 36, INK)]),
    karte(110, 370, 505, 190, "u5", fill=HELLBLAU, rund=18, schatten=5, rand=4),
    z("Gläubiger beweist:", 135, 392, "u5", "ExtraBold", 34),
    z("die Pflichtverletzung", 135, 450, "u5", "Bold", 34),
    karte(645, 370, 505, 190, "u6", fill=HELLGRUEN, rund=18, schatten=5, rand=4),
    z("Schuldner beweist:", 670, 392, "u6", "ExtraBold", 34),
    z("nicht zu vertreten", 670, 450, beim("u6", "vertreten"), "Bold", 34),
    zit("vgl. BGH, Urt. v. 13.11.2018 – EnZR 39/17, Rn. 64", 110, 585, beim("u6", "vertreten")),
    linienzug([(110, 650), (1150, 650)], "u7", breite=3),
    z("Gegenwehr: nur mit dem vollen Beweis", 110, 675, beim("u7", "Nur"), "Bold", 36),
    blk(110, 745, 1040, 74, HELLROT, "u8", [("Bleibt es unklar, haftet er.", "ExtraBold", 36, INK)]),
    *requisit([("u4", ("tabler", "arrows-exchange", 110, GRUEN), "Beweislast wechselt", GRUEN),
               ("u7", ("tabler", "shield-check", 100, WEISS), "voller Beweis", WEISS),
               ("u8", ("tabler", "gavel", 100, WEISS), "haftet", HELLROT)]),
    *paar("u4", "KR", [("u4", "ruhig"), ("u5", "froh")], "HE", [("u4", "ruhig"), ("u6", "denkt"), ("u8", "sorge")]),
]))

# ===========================================================================================================================
# G1–G3 Der Fall
# ===========================================================================================================================
DRX = 860                                    # Diagramm: zwei kleine Autos in der Tafel (rotes vorne, blaues dahinter)
folie([("l1", "Der Fall › Anschein gegen den Auffahrenden"), ("l4", "Der Fall › Frau Kretschmer beweist das Auffahren")],
      rechts_frei([
    *wtafel("l1", "Der Fall: Anscheinsbeweis", BLAU),
    z("erster Anschein: Verschulden des Auffahrenden", 110, 180, beim("l2", "Anschein"), "Bold", 36),
    zit("BGH, Urt. v. 13.12.2016 – VI ZR 32/16, Rn. 10", 110, 235, beim("l2", "Anschein")),
    z("Sicherheitsabstand nicht eingehalten, § 4 Abs. 1 StVO,", 130, 300, beim("l3", "Sicherheitsabstand"), size=34),
    z("unaufmerksam, § 1 StVO, oder", 130, 352, beim("l3", "unaufmerksam"), size=34),
    z("zu schnell, § 3 Abs. 1 StVO", 130, 404, beim("l3", "schnell"), size=34),
    linienzug([(110, 475), (1150, 475)], "l4", breite=3),
    *okz("Frau Kretschmer beweist nur: das Auffahren", 500, "l4", "Bold", 36, x=160),
    *okz("unstreitig", 560, beim("l4", "unstreitig"), "Bold", 36, x=160),
    dicon("tabler", "car", DRX, 840, 260, "l1", fuell=ROT),
    dicon("tabler", "car", DRX - 217 + 4, 840, 260, "l1", fuell=BLAU),
    *requisit([("l1", ("tabler", "car", 160, BLAU), "Auffahrunfall", WEISS),
               ("l2", ("tabler", "bulb", 100, BLAU), "erster Anschein", BLAU),
               ("l4", ("tabler", "circle-check", 100, GRUEN), "unstreitig", GRUEN)]),
    *paar("l1", "KR", [("l1", "ruhig"), ("l4", "froh")], "HE", [("l1", "ernst"), ("l3", "sorge")]),
]))

folie([("l5", "Der Fall › Behauptung: grundlose Vollbremsung"), ("l7", "Der Fall › Gegenfall: Spurwechsel")], rechts_frei([
    *wtafel("l5", "Der Fall: die Behauptung", BLAU),
    z("Herr Hertel: „grundlose Vollbremsung“", 110, 180, "l5", "Bold", 36),
    *neinz("bloße Behauptung erschüttert nichts", 248, beim("l6", "erschüttert"), "Bold", 36, x=160),
    z("Er muss Tatsachen beweisen, die den Ablauf", 110, 320, beim("l6", "Tatsachen"), size=34),
    z("untypisch machen.", 110, 370, beim("l6", "untypisch"), size=34),
    zit("BGH, Urt. v. 13.12.2016 – VI ZR 32/16, Rn. 11 f.", 110, 425, beim("l6", "untypisch")),
    linienzug([(110, 490), (1150, 490)], "l7", breite=3),
    z("Anders, wenn feststünde:", 110, 515, "l7", "Bold", 36),
    blk(110, 575, 1040, 74, HELLBLAU, beim("l7", "Spur"), [("Spurwechsel kurz vorher, vor ihm", "ExtraBold", 34, INK)]),
    z("dann fehlt in der Regel der typische Ablauf", 110, 675, beim("l7", "Dann"), "Bold", 34),
    zit("BGH, Urt. v. 13.12.2011 – VI ZR 177/10, Rn. 11", 110, 730, beim("l7", "Dann")),
    *requisit([("l5", ("tabler", "alert-triangle", 100, GELB), "„grundlos gebremst“", WEISS),
               (beim("l6", "erschüttert"), ("tabler", "hand-stop", 100, WEISS), "erschüttert nichts", HELLROT),
               (beim("l7", "Spur"), ("tabler", "road", 110, WEISS), "Spurwechsel", BLAU)]),
    *paar("l5", "KR", [("l5", "skeptisch"), (beim("l6", "erschüttert"), "ruhig")],
          "HE", [("l5", "ernst"), (beim("l6", "erschüttert"), "sorge"), ("l7", "denkt")]),
]))

W4 = ["„(1) Der Abstand zu einem vorausfahrenden Fahrzeug muss in",
      "der Regel so groß sein, dass auch dann hinter diesem gehalten",
      "werden kann, wenn es plötzlich gebremst wird. Wer vorausfährt,",
      "darf nicht ohne zwingenden Grund stark bremsen. …“"]
w4, w4_y = wortlaut(80, 300, 1100, W4, "§ 4 Abs. 1 StVO", "l9", marken=[
    (1, "auch dann hinter diesem gehalten", beim("l9", "halten")),
    (3, "ohne zwingenden Grund stark bremsen", beim("l10", "zwingenden"))], size=31)
folie([("l8", "Der Fall › scharfes Bremsen einkalkulieren"), ("l9", "Der Fall › § 4 Abs. 1 StVO"),
       ("l10", "Der Fall › Abwägung, § 17 StVG")], rechts_frei([
    *wtafel("l8", "Der Fall: Abstand halten", BLAU),
    z("plötzliches scharfes Bremsen: stets einkalkulieren", 110, 180, beim("l8", "stets"), "Bold", 34),
    zit("BGH, Urt. v. 3.12.2024 – VI ZR 18/24, Rn. 16", 110, 232, beim("l8", "stets")),
    *w4,
    z("bewiesen, dass sie grundlos stark bremste?", 110, w4_y + 40, "l10", "Bold", 34),
    z("Dann zählt der Verstoß bei der Abwägung, § 17 StVG.", 110, w4_y + 92, beim("l10", "Abwägung"), size=34),
    zit("vgl. BGH, Urt. v. 13.12.2016 – VI ZR 32/16, Rn. 8", 110, w4_y + 145, beim("l10", "Abwägung")),
    *requisit([("l8", ("tabler", "alert-triangle", 100, GELB), "scharfes Bremsen", GELB),
               ("l9", ("tabler", "ruler-measure", 110, WEISS), "Abstand", WEISS),
               ("l10", ("tabler", "scale", 130, WEISS), "§ 17 StVG", WEISS)]),
    *paar("l8", "KR", [("l8", "ruhig"), ("l10", "skeptisch")], "HE", [("l8", "sorge"), ("l9", "muede"), ("l10", "denkt")]),
]))

# ===========================================================================================================================
# G4 Zurück auf der Straße: das Ergebnis
# ===========================================================================================================================
folie([("l11", "Der Fall › Ergebnis")], [
    *kulisse("l11"),
    hart(auto(RX1, "l11", ROT)), hart(auto(BX, "l11", BLAU)),
    pl("Der Anschein bleibt.", 70, 30, "l11", fill=BLAU, size=40),
    pl("Herr Hertel haftet.", 70, 120, beim("l11", "Herr"), fill=HELLROT, size=40),
    pl("BGH: Auffahrender haftet allein – gebilligt", 70, 210, "l12", fill=WEISS, size=34),
    pl("VI ZR 32/16, Rn. 14", 70, 285, beim("l12", "gebilligt"), fill=WEISS, size=28),
    *fig("HE", HEX, FAHR, FH, [("l11", "ernst_r"), (beim("l11", "Herr"), "muede_r")], erst="cut"),
    hart(ns("Herr Hertel", HEX, FAHR, "l11", NFARBE["HE"])),
    *fig("KR", KRX, FAHR, FH, [("l11", "ruhig"), (beim("l11", "Herr"), "froh")], erst="cut"),
    hart(ns("Frau Kretschmer", KRX, FAHR, "l11", NFARBE["KR"])),
])

# ===========================================================================================================================
# H Merktabelle
# ===========================================================================================================================
SP_X, SP_W = (470, 910, 1350), 420
ZEILEN_Y, ZH = (305, 495, 685), 170
KOPF = [("Anscheinsbeweis", BLAU), ("Vermutung", GELB), ("Beweislastumkehr", GRUEN)]
TINT = [HELLBLAU, HELLGELB, HELLGRUEN]
ZELLEN = [
    [("t1a", [("Erfahrungssatz", "Bold", 34)]),
     ("t1b", [("Gesetz", "Bold", 34), ("§ 292 ZPO, z. B. § 477 BGB", "Regular", 28)]),
     ("t1c", [("Beweislastregel", "Bold", 34), ("z. B. § 280 I 2 BGB", "Regular", 28)])],
    [("t2a", [("bleibt", "Bold", 34)]),
     ("t2b", [("Gegner beweist", "Bold", 34), ("das Gegenteil", "Bold", 34)]),
     ("t2c", [("wechselt", "Bold", 34)])],
    [("t3a", [("erschüttern", "Bold", 34)]),
     ("t3b", [("Gegenteil", "Bold", 34), ("voll beweisen", "Bold", 34)]),
     ("t3c", [("Entlastung", "Bold", 34), ("voll beweisen", "Bold", 34)])],
]
ZK = [("t1", "1. Grundlage"), ("t2", "2. Beweislast"), ("t3", "3. Gegenwehr")]
els_h = [karte(60, 50, 1800, 940, "tab"), titel(glyphen("Merktabelle: drei Werkzeuge"), 110, 90, "tab", 46)]
for k, (t, fa) in enumerate(KOPF):
    els_h += zelle(SP_X[k], 190, SP_W, 90, fa, "tab", [(t, "ExtraBold", 34)])
for r, (c, t) in enumerate(ZK):
    els_h += zelle(110, ZEILEN_Y[r], 330, ZH, WEISS, c, [(t, "ExtraBold", 36)])
    for k, (cc, zz) in enumerate(ZELLEN[r]):
        els_h += zelle(SP_X[k], ZEILEN_Y[r], SP_W, ZH, TINT[k], cc, zz)
assert ZEILEN_Y[-1] + ZH <= 970
folie([("tab", "Merktabelle"), ("t1", "Merktabelle › 1. Grundlage"), ("t2", "Merktabelle › 2. Beweislast"),
       ("t3", "Merktabelle › 3. Gegenwehr")], els_h)

# ===========================================================================================================================
# I Klausurtipp (Lexi)
# ===========================================================================================================================
VERBEN = [("Anschein", "Anschein: erschüttern", BLAU), ("Vermutung", "Vermutung: widerlegen", GELB),
          ("Umkehr", "Umkehr: Gegner trägt die Beweislast", GRUEN)]
els_i = [*tafel("tipp", "Klausurtipp", fill=HELL), warnung_i(150, 225, "tipp", gr=26),
         z("Werkzeug genau benennen, passendes Verb:", 200, 200, beim("tipp", "Benenne"), "Bold", 34)]
for k, (w, t, fa) in enumerate(VERBEN):
    y = 280 + k * 62
    els_i += [karte(205, y + 10, 34, 34, beim("tipp2", w), fill=fa, rund=8, schatten=0, rand=3),
              z(t, 260, y, beim("tipp2", w), "Bold", 34)]
els_i += [linienzug([(130, 485), (1130, 485)], "tipp3", breite=3),
          z("Für den Fall, angelehnt an den BGH:", 200, 505, "tipp3", "Bold", 32),
          blk(160, 565, 1010, 120, WEISS, beim("tipp3", "unfallursächliches"),
              [("„Für ein unfallursächliches Verschulden des Beklagten", "Bold", 32, INK),
               ("spricht ein nicht erschütterter Anscheinsbeweis.“", "Bold", 32, INK)]),
          zit("vgl. BGH, Urt. v. 13.12.2016 – VI ZR 32/16, Rn. 13", 200, 700, beim("tipp3", "unfallursächliches")),
          *neinz("nie: „Der Anscheinsbeweis kehrt die Beweislast um.“", 765, "tipp4", "Bold", 32, x=205),
          *redet("LX_warnt", FX, FB, FR + 40, "tipp", "merke"),
          ns("Lexi", FX, FB, "tipp", GELB, d=0.2)]
folie([("tipp", "Klausurtipp · das passende Verb"), ("tipp3", "Klausurtipp · Formulierung im Urteil")], els_i)

# ===========================================================================================================================
# J Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Den Anschein ", 0), ("erschüttert", "a"), (" man,", 0)],
                 [("die Vermutung ", 0), ("widerlegt", "b"), (" man nur", 0)],
                 [("mit dem vollen Beweis des Gegenteils.", 0)]],
                750, 290, 44, "merke", {"a": beim("merke", "erschüttert"), "b": beim("merke", "widerlegt")}),
    *markertext([[("Bei der Beweislastumkehr verliert", 0)], [("im Zweifel ", 0), ("der Gegner.", "c")]],
                750, 600, 44, "mk2", {"c": beim("mk2", "Gegner")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
