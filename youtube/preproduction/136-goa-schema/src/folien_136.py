"""Folge 136 · GoA Schema: Wann bekommt der Helfer seine Kosten? (§ 683 BGB) – Serienstandard Open Peeps (Katzenkönig).
Beispielfall: Frau Huber ist verreist; die Mülltonne vor ihrem Haus brennt, das Feuer droht auf ihren Carport
überzugreifen. Ihr Nachbar Harald erstickt die Flammen mit seiner Jacke (noch 250 € wert), die Jacke ist ruiniert.
Szenen laut ../SZENENPLAN.md: A1 Frau Huber verreist, A2 Die Mülltonne brennt, A3 Harald löscht mit der Jacke,
A4 Frau Huber kommt zurück, B Sachverhalt, C Anspruchsgrundlage und Aufbau, D 1. Geschäftsbesorgung, E 2. fremdes
Geschäft, F 3. ohne Auftrag (Wortlaut § 677), G 4. Berechtigung (Wortlaut § 683 S. 1), H §§ 679, 680, I1 5. Rechtsfolge
(Wortlaut § 670), I2 Jacke als Aufwendung, J Abgrenzung § 684 S. 1 (Wortlaut), K Ergebnis, L Klausurtipp (Lexi),
M Schema, N Merksatz (Lexi). Zwei Handlungsgeräusche (Koffer, Feuer; ../geraeusche_herkunft.json).
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/hand/okz/
neinz als eigene Kopie aus Folge 129 (gemeinsame Dateien unverändert); neu: Haus, Carport, Mülltonne mit Flamme.
Zahlen auf Tafeln, Pillen und Blasen als Ziffern (Wortlautkarten wörtlich)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_136/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_136/" in n:
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
    els.append(z(quelle, tx, ty + len(zeilen) * lh + 4, cue, "Bold", max(26, size - 4), farbe=TEXT, rechts=x + w - 16, bis=bis))
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



BODEN, FH = 860, 480
X1, X2 = 1420, 1730                         # zwei Figuren neben der Tafel (Harald, Frau Huber)
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
HA_N, HU_N = BLAU, GRUEN                    # Farben der Namensschilder
PX, PY, PU = 1575, 120, 340                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
GRAU = (190, 190, 196, 255)
DGRAU = (120, 122, 130, 255)
RUSS = (92, 92, 98, 255)
ZIEGEL = (214, 92, 70, 255)
JACKE = (91, 143, 217, 255)                 # Haralds Jacke (wie in figuren_136.py)


def boden(cue, hart_=False):
    e = linienzug([(40, BODEN), (1880, BODEN)], cue, breite=7, farbe=INK)
    return hart(e) if hart_ else e


def requisit(folge, bis_ende=None):
    """Wechselndes Requisit über den Figuren: folge = [(cue, (set, icon, breite, fuell), pillentext, pillenfarbe)]."""
    els = []
    for i, (c, ic, txt, pf) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else bis_ende
        if ic:
            s_, n_, br, fu = ic
            els.append(ficon(s_, n_, PX, PU, br, c, fuell=fu, bis=b))
        if txt:
            els.append(pl(txt, PX, PY, c, fill=pf, size=30, anker="m", bis=b))
    return els


def paar(c0, ha, hu, bis=None):
    """Tafelszene: Harald (links) und Frau Huber (rechts) neben der Tafel, beide blicken zur Tafel (nach links)."""
    return [*fig("HA", X1, FB, FR, ha, bis=bis), ns("Harald", X1, FB, c0, HA_N, d=0.1),
            *fig("HU", X2, FB, FR, hu, bis=bis, d=0.2), ns("Frau Huber", X2, FB, c0, HU_N, d=0.3)]


# --- Haus, Carport und Mülltonne (programmatisch aus Palettenflächen bzw. Tabler-Icons) -----------------------------------
HX0, HX1, HY = 120, 540, 600               # Hauswand links/rechts, Traufe
DX0, DX1, DFIRST = 80, 580, (330, 410)     # Dachfuß links/rechts, First
CX0, CX1, CY = 620, 1010, 560              # Carport: Pfosten links/rechts, Dachunterkante
TX = 1120                                  # Mülltonne (Mitte)
TONNE_OBEN = BODEN - 132                   # ungefähre Oberkante der Tonne


def dach(cue, anim="cut"):
    s = 2
    x0, y0 = DX0 - 10, DFIRST[1] - 10
    w, h = DX1 - DX0 + 20, HY - DFIRST[1] + 20
    im = Image.new("RGBA", (w * s, h * s)); dr = ImageDraw.Draw(im)
    P = lambda x, y: ((x - x0) * s, (y - y0) * s)
    poly = [P(DX0, HY), P(*DFIRST), P(DX1, HY)]
    dr.polygon(poly, fill=ZIEGEL)
    for k in range(1, 5):
        y = DFIRST[1] + k * (HY - DFIRST[1]) / 5
        xl = DFIRST[0] - (y - DFIRST[1]) / (HY - DFIRST[1]) * (DFIRST[0] - DX0)
        xr = DFIRST[0] + (y - DFIRST[1]) / (HY - DFIRST[1]) * (DX1 - DFIRST[0])
        dr.line([P(xl + 4, y), P(xr - 4, y)], fill=INK, width=3 * s)
    dr.line(poly + [poly[0]], fill=INK, width=6 * s, joint="curve")
    im = im.resize((w, h), Image.LANCZOS)
    return El(im, x0, y0, cue, anim, 0.0, None, name="dach")


def kulisse(c0, hart_=True, tonne=True):
    """Haus von Frau Huber, Carport mit Auto, Mülltonne – in allen Fallszenen an derselben Stelle."""
    an = "cut" if hart_ else "fade"
    els = [boden(c0, hart_),
           karte(HX0, HY, HX1 - HX0, BODEN - HY, c0, fill=WEISS, rund=6, schatten=6, rand=5, anim=an),
           karte(170, 655, 130, 105, c0, fill=BLAU, rund=8, schatten=0, rand=5, anim=an),
           karte(380, 665, 105, BODEN - 665, c0, fill=GELB, rund=6, schatten=0, rand=5, anim=an),
           dach(c0, anim=an),
           karte(CX0, CY, 18, BODEN - CY, c0, fill=DGRAU, rund=3, schatten=0, rand=4, anim=an),
           karte(CX1 - 18, CY, 18, BODEN - CY, c0, fill=DGRAU, rund=3, schatten=0, rand=4, anim=an),
           karte(CX0 - 25, CY - 34, CX1 - CX0 + 50, 36, c0, fill=GRAU, rund=6, schatten=4, rand=5, anim=an)]
    car = ficon("tabler", "car", (CX0 + CX1) // 2, BODEN - 3, 300, c0, fuell=BLAU, anim=an)
    els.append(car)
    if tonne:
        els.append(ficon("tabler", "trash", TX, BODEN - 3, 120, c0, fuell=GRAU, anim=an))
    return els


def flamme(cue, bis=None, gross=True, d=0.0):
    return ficon("tabler", "flame", TX, TONNE_OBEN + 18, 120 if gross else 80, cue, fuell=ORANGE, nebenfarbe=GELB,
                 bis=bis, d=d)


def jacke_icon(cx, unten, cue, verbrannt=False, bis=None, breite=130, anim="pop"):
    return ficon("tabler", "jacket", cx, unten, breite, cue, fuell=RUSS if verbrannt else JACKE,
                 nebenfarbe=(70, 70, 76, 255) if verbrannt else WEISS, bis=bis, anim=anim)


HX, UX = 1420, 1730                         # Fallszenen: Harald, Frau Huber

# ===========================================================================================================================
# A1 Fall: Frau Huber verreist
# ===========================================================================================================================
URL = beim("fall", "Urlaub")
GEHT = beim("fall", "fährt")                # Frau Huber zieht ihren Koffer nach rechts
folie([(NULL, "Fall · Frau Huber verreist"), ("nachbar", "Fall · Der Nachbar Harald")], [
    *kulisse(NULL),
    hart(pl("Haus von Frau Huber", 70, 30, NULL, fill=GELB, size=40)),
    pl("2 Wochen Urlaub", 70, 112, beim("fall", "zwei"), fill=WEISS, size=32),
    ficon("tabler", "plane-departure", 480, 190, 90, URL, fuell=WEISS),
    szene(bewegt(peep_voll("HU_froh_r", UX, BODEN, FH, NULL, anim="cut"), GEHT, "nachbar", -300), "136koffer*", 0.6, T_(GEHT)),
    bewegt(ficon("tabler", "luggage", UX - 175, BODEN - 3, 80, NULL, fuell=LILA, anim="cut"), GEHT, "nachbar", -300),
    bewegt(hart(ns("Frau Huber", UX, BODEN, NULL, HU_N)), GEHT, "nachbar", -300),
    *fig("HJ", HX - 60, BODEN, FH, [("nachbar", "ruhig_r")], erst="pop"),
    ns("Harald", HX - 60, BODEN, "nachbar", HA_N, d=0.1),
    pl("Nachbar", HX - 60, 330, beim("nachbar", "Nachbar"), fill=BLAU, size=30, anker="m"),
])

# ===========================================================================================================================
# A2 Fall: Die Mülltonne brennt
# ===========================================================================================================================
BRENNT = beim("feuer", "brennt")
folie([("feuer", "Fall · Die Mülltonne brennt")], [
    *kulisse("feuer", hart_=False),
    pl("Am 3. Tag", 70, 30, "feuer", fill=GELB, size=40),
    szene(flamme(BRENNT), "136feuer*", 0.7),
    pl("Mülltonne brennt", 70, 112, BRENNT, fill=ROT, size=32),
    pl("Carport von Frau Huber", 600, 470, beim("carport", "Carport"), fill=WEISS, size=30),
    pfeil(1068, 640, 1022, 560, beim("ha1", "greift"), breite=9, kopf=26, farbe=DROT),
    blase("sprech", 640, 210, "ha1", 1010, 230, inhalt=["Das Feuer greift gleich", "auf den Carport über!"], textsize=36,
          figur=("HJ_redet", HX, BODEN, FH), bis="loesch"),
    *fig("HJ", HX, BODEN, FH, [("feuer", "ruhig"), (BRENNT, "sorge")], erst="pop", bis="ha1"),
    *redet("HJ_redet", HX, BODEN, FH, "ha1", "loesch"),
    ns("Harald", HX, BODEN, "feuer", HA_N, d=0.1),
])

# ===========================================================================================================================
# A3 Fall: Harald löscht mit der Jacke
# ===========================================================================================================================
ZIEHT, ERST = beim("loesch", "zieht"), beim("loesch", "erstickt")
_hx, _hy = hand("HA_entschlossen", HX, BODEN, FH, -1)
_HAND = (_hx + 10, _hy + 70)                # Jacke hängt an Haralds ausgestreckter Hand
folie([("loesch", "Fall · Harald löscht mit der Jacke"), ("kaputt", "Fall · Die Jacke ist ruiniert")], [
    *kulisse("loesch", hart_=False),
    flamme("loesch", bis="aus"),
    ficon("tabler", "fire-extinguisher", 1660, 320, 120, beim("loesch", "Feuerlöscher"), fuell=WEISS, bis="aus"),
    bis_(nein(1660, 262, beim("loesch", "nicht"), gr=34), "aus"),
    pl("kein Feuerlöscher zur Hand", 70, 30, beim("loesch", "nicht"), fill=GELB, size=34),
    jacke_icon(*_HAND, ZIEHT, bis=ERST, breite=110),
    jacke_icon(TX, TONNE_OBEN + 40, ERST, bis="kaputt", breite=150, anim="cut"),
    pl("Flammen mit der Jacke erstickt", 70, 112, ERST, fill=WEISS, size=32),
    pl("Feuer aus, niemand verletzt", 70, 194, "aus", fill=GRUEN, size=32),
    jacke_icon(TX, TONNE_OBEN + 40, "kaputt", verbrannt=True, breite=150, anim="cut"),
    pl("Jacke ruiniert", 1580, 290, beim("kaputt", "ruiniert"), fill=ROT, size=32),
    pl("Wert: 250 €", 1580, 372, beim("wert", "zweihundertfünfzig"), fill=GELB, size=32),
    *fig("HJ", HX, BODEN, FH, [("loesch", "entschlossen")], erst="cut", bis=ZIEHT),
    *fig("HA", HX, BODEN, FH, [(ZIEHT, "entschlossen"), ("aus", "froh"), (beim("kaputt", "ruiniert"), "sorge")], erst="cut"),
    hart(ns("Harald", HX, BODEN, "loesch", HA_N)),
])

# ===========================================================================================================================
# A4 Fall: Frau Huber kommt zurück
# ===========================================================================================================================
folie([("zurueck", "Fall · Frau Huber kommt zurück"), ("frage", "Fall · Die Frage")], [
    *kulisse("zurueck", hart_=False),
    jacke_icon(TX, TONNE_OBEN + 40, "zurueck", verbrannt=True, breite=150),
    pl("2 Wochen später", 70, 30, "zurueck", fill=GELB, size=40),
    ficon("tabler", "luggage", UX - 175, BODEN - 3, 80, "zurueck", fuell=LILA),
    blase("sprech", 660, 270, "ha2", 960, 220, inhalt=["Ihre Mülltonne hat gebrannt.", "Ich habe das Feuer mit meiner",
                                                     "Jacke gelöscht. Bitte zahlen", "Sie mir 250 €."], textsize=32,
          figur=("HA_redet_r", HX, BODEN, FH), bis="hu1"),
    blase("sprech", 560, 200, "hu1", 1250, 230, inhalt=["Danke! Aber um Hilfe", "gebeten habe ich Sie nicht."],
          textsize=34, figur=("HU_redet", UX, BODEN, FH), bis="frage"),
    pl("Muss Frau Huber die Jacke bezahlen?", 70, 112, "frage", fill=PINK, size=36),
    *fig("HA", HX, BODEN, FH, [("zurueck", "ruhig_r")], erst="pop", bis="ha2"),
    *redet("HA_redet_r", HX, BODEN, FH, "ha2", "hu1"),
    *fig("HA", HX, BODEN, FH, [("hu1", "denkt_r"), ("frage", "ernst_r")], erst="cut"),
    ns("Harald", HX, BODEN, "zurueck", HA_N, d=0.1),
    *fig("HU", UX, BODEN, FH, [("zurueck", "froh"), ("ha2", "staunt")], erst="pop", d=0.2, bis="hu1"),
    *redet("HU_redet", UX, BODEN, FH, "hu1", "frage"),
    *fig("HU", UX, BODEN, FH, [("frage", "denkt")], erst="cut"),
    ns("Frau Huber", UX, BODEN, "zurueck", HU_N, d=0.3),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_136(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 56)]
    y = 205
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=38, zeilenabstand=1.30)
        els += e; y += 14
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=36))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_136("sv", [
    "Frau Huber fährt für zwei Wochen in den Urlaub. Am dritten Tag brennt die Mülltonne vor ihrem Haus; die Flammen "
    "drohen auf ihren Carport überzugreifen. Ihr Nachbar Harald hat keinen Feuerlöscher zur Hand. Er zieht seine Jacke "
    "aus und erstickt damit die Flammen. Verletzt ist niemand, aber die Jacke ist ruiniert. Sie war noch 250 Euro wert.",
    "Als Frau Huber zurückkommt, erzählt Harald ihr alles und verlangt 250 Euro. Frau Huber bedankt sich, sagt aber: "
    "„Um Hilfe gebeten habe ich Sie nicht.“",
], "Muss Frau Huber die Jacke bezahlen?")

# ===========================================================================================================================
# C Anspruchsgrundlage und Aufbau
# ===========================================================================================================================
PUNKTE = [("auf1", "1. Geschäftsbesorgung", BLAU), ("auf2", "2. fremdes Geschäft", GRUEN), ("auf3", "3. ohne Auftrag", GELB),
          ("auf4", "4. Berechtigung", LILA), ("auf5", "5. Rechtsfolge", ROT)]
els_c = [*tafel("agl", "Anspruch auf Aufwendungsersatz"),
         z("Harald gegen Frau Huber: 250 € für die Jacke", 110, 190, "agl", "Bold", 34),
         z("Geschäftsführung ohne Auftrag (GoA)", 110, 255, beim("agl", "Geschäftsführung"), "Regular", 34),
         z("§§ 677, 683 Satz 1, 670 BGB", 110, 310, beim("agl", "Paragrafen"), "ExtraBold", 40)]
y = 400
for c, txt, farbe in PUNKTE:
    els_c.append(blk(110, y, 620, 74, farbe, beim(c, txt.split(" ", 1)[1].split()[0]) if c != "auf1" else beim("auf1", "Geschäftsbesorgung"),
                     [(txt, "Bold", 34, INK)]))
    y += 88
folie([("agl", "Anspruch: §§ 677, 683 S. 1, 670 BGB"), ("auf1", "Anspruch › Prüfung in 5 Punkten")], rechts_frei([
    *els_c,
    *requisit([("agl", ("tabler", "cash-banknote", 110, GRUEN), "250 € für die Jacke?", GRUEN),
               ("auf1", ("tabler", "list-numbers", 100, WEISS), "5 Punkte", WEISS)]),
    *paar("agl", [("agl", "ruhig"), ("auf5", "zufrieden")], [("agl", "ruhig"), ("auf3", "denkt")]),
]))

# ===========================================================================================================================
# D 1. Geschäftsbesorgung
# ===========================================================================================================================
folie([("p1", "1. Geschäftsbesorgung")], rechts_frei([
    *tafel("p1", "1. Geschäftsbesorgung"),
    z("Jede Tätigkeit, auch eine rein tatsächliche", 110, 200, beim("p1a", "jede"), "Bold", 36),
    zit("vgl. BGH, Urt. v. 21.6.2012 – III ZR 291/11, Rn. 12 (zu § 662 BGB)", 110, 255, beim("p1a", "tatsächliche")),
    *okz("Feuer löschen: Geschäftsbesorgung", 330, "p1b", "Bold", 36, x=160),
    *requisit([("p1", ("tabler", "flame", 90, ORANGE), "Feuer löschen", WEISS),
               ("p1b", ("tabler", "checklist", 100, WEISS), "1. erfüllt", GRUEN)]),
    *paar("p1", [("p1", "ruhig"), ("p1b", "zufrieden")], [("p1", "ruhig")]),
]))

# ===========================================================================================================================
# E 2. Fremdes Geschäft
# ===========================================================================================================================
folie([("p2", "2. Fremdes Geschäft"), ("p2b", "2. › Fremdgeschäftsführungswille vermutet"),
       ("p2c", "2. › auch-fremdes Geschäft")], rechts_frei([
    *tafel("p2", "2. Fremdes Geschäft"),
    z("Harald schützt den Carport von Frau Huber", 110, 190, "p2a", "Bold", 34),
    *okz("objektiv fremd: Rechtskreis von Frau Huber", 250, beim("p2a", "objektiv"), "Bold", 34, x=160),
    blk(110, 330, 1040, 80, GELB, beim("p2b", "vermutet"), [("Fremdgeschäftsführungswille wird vermutet", "Bold", 34, INK)]),
    zit("BGH, Urt. v. 5.7.2018 – III ZR 273/16, Rn. 20; Urt. v. 1.2.2018 – III ZR 53/17, Rn. 8", 110, 425,
        beim("p2b", "Bundesgerichtshof")),
    *okz("Harald wollte für Frau Huber handeln", 480, beim("p2b", "Harald"), "Bold", 34, x=160),
    z("Ebenso beim auch-fremden Geschäft:", 110, 580, "p2c", "Bold", 34),
    z("zugleich eigene Interessen berührt", 110, 630, beim("p2c", "zugleich"), "Regular", 34),
    pl("z. B. Feuer bedroht auch Haralds Haus", 110, 700, beim("p2c", "etwa"), fill=GELB, size=30),
    zit("BGH III ZR 273/16, Rn. 20 („auch-fremdes“ Geschäft)", 110, 780, beim("p2c", "etwa")),
    *requisit([("p2", ("tabler", "car-garage", 110, WEISS), "Carport von Frau Huber", WEISS),
               ("p2b", ("tabler", "heart-handshake", 100, ROT), "für sie handeln", GRUEN),
               ("p2c", ("tabler", "home", 100, ZIEGEL), "auch eigenes Haus?", GELB)]),
    *paar("p2", [("p2", "ruhig"), ("p2b", "froh"), ("p2c", "denkt")], [("p2", "ruhig"), ("p2a", "zufrieden")]),
]))

# ===========================================================================================================================
# F 3. Ohne Auftrag, § 677 BGB (Wortlautkarte)
# ===========================================================================================================================
W677 = ["„Wer ein Geschäft für einen anderen besorgt, ohne von ihm",
        "beauftragt oder ihm gegenüber sonst dazu berechtigt zu sein,",
        "hat das Geschäft so zu führen, wie das Interesse des Geschäftsherrn",
        "mit Rücksicht auf dessen wirklichen oder mutmaßlichen Willen",
        "es erfordert.“"]
w677, w677_y = wortlaut(110, 165, 1040, W677, "§ 677 BGB", "p3", marken=[
    (0, "für einen anderen besorgt", beim("p3a", "anderen")),
    (0, "ohne von ihm", beim("p3a", "ohne")),
    (1, "beauftragt", beim("p3a", "beauftragt")),
    (1, "sonst dazu berechtigt", beim("p3a", "sonst"))], size=30)
folie([("p3", "3. Ohne Auftrag, § 677 BGB")], rechts_frei([
    *tafel("p3", "3. Ohne Auftrag"),
    *w677,
    *okz("kein Auftrag: Frau Huber hat um nichts gebeten", w677_y + 40, "p3b", "Bold", 34, x=160),
    *okz("kein Vertrag", w677_y + 110, "p3c", "Bold", 34, x=160),
    *requisit([("p3", ("tabler", "file-x", 100, WEISS), "ohne Auftrag", WEISS),
               ("p3b", ("tabler", "hand-stop", 100, GELB), "nicht gebeten", GELB)]),
    *paar("p3", [("p3", "ruhig"), ("p3c", "denkt")], [("p3", "ruhig"), ("p3b", "ernst")]),
]))

# ===========================================================================================================================
# G 4. Berechtigung, § 683 Satz 1 BGB (Wortlautkarte)
# ===========================================================================================================================
W683 = ["„Entspricht die Übernahme der Geschäftsführung dem Interesse",
        "und dem wirklichen oder dem mutmaßlichen Willen des",
        "Geschäftsherrn, so kann der Geschäftsführer wie ein Beauftragter",
        "Ersatz seiner Aufwendungen verlangen.“"]
w683, w683_y = wortlaut(110, 165, 1040, W683, "§ 683 Satz 1 BGB", "p4", marken=[
    (0, "Übernahme", beim("p4a", "Übernahme")),
    (0, "dem Interesse", beim("p4a", "Interesse")),
    (1, "wirklichen oder dem mutmaßlichen Willen", beim("p4a", "wirklichen"))], size=30)
folie([("p4", "4. Berechtigung, § 683 S. 1 BGB"), ("p4b", "4. › Interesse"), ("p4c", "4. › wirklicher oder mutmaßlicher Wille"),
       ("p4e", "4. › Zeitpunkt der Übernahme")], rechts_frei([
    *tafel("p4", "4. Berechtigung"),
    *w683,
    *okz("Interesse: objektiv nützlich, Brand am Carport verhindert", w683_y + 26, "p4b", "Bold", 32, x=160),
    zit("BGH, Urt. v. 11.3.2016 – V ZR 102/15, Rn. 8", 160, w683_y + 72, beim("p4b", "objektiv")),
    *neinz("wirklicher Wille: unbekannt, sie ist verreist", w683_y + 130, "p4c", "Bold", 32, x=160),
    *okz("mutmaßlicher Wille: bei objektiver Beurteilung,", w683_y + 200, "p4d", "Bold", 32, x=160),
    z("ohne andere Anhaltspunkte wie das Interesse", 160, w683_y + 246, beim("p4d", "Ohne"), "Bold", 32),
    zit("BGH V ZR 102/15, Rn. 12", 160, w683_y + 292, beim("p4d", "Ohne")),
    blk(110, w683_y + 340, 1040, 80, GELB, "p4e", [("Maßgeblich: Zeitpunkt der Übernahme", "Bold", 34, INK)]),
    *requisit([("p4", ("tabler", "scale", 100, WEISS), "berechtigt?", WEISS),
               ("p4b", ("tabler", "shield-check", 100, GRUEN), "Brand verhindert", GRUEN),
               ("p4c", ("tabler", "plane-departure", 100, WEISS), "verreist", WEISS),
               ("p4e", ("tabler", "clock", 100, GELB), "bei der Übernahme", GELB)]),
    *paar("p4", [("p4", "ruhig"), ("p4b", "froh"), ("p4e", "ernst")], [("p4", "ruhig"), ("p4c", "denkt"), ("p4d", "zufrieden")]),
]))

# ===========================================================================================================================
# H Sonderregeln §§ 679, 680 BGB
# ===========================================================================================================================
folie([("p679", "4. › Sonderregel § 679 BGB"), ("p680", "4. › Sonderregel § 680 BGB")], rechts_frei([
    *tafel("p679", "Zwei Sonderregeln"),
    z("§ 679: entgegenstehender Wille unbeachtlich,", 110, 200, beim("p679", "entgegenstehender"), "Bold", 34),
    z("etwa wenn sonst eine Pflicht des Geschäftsherrn", 110, 250, beim("p679", "etwa"), "Regular", 34),
    z("im öffentlichen Interesse nicht rechtzeitig", 110, 295, beim("p679", "öffentlichen"), "Regular", 34),
    z("erfüllt würde", 110, 340, beim("p679", "öffentlichen"), "Regular", 34),
    zit("Wortlaut § 679 BGB; Beispiel Verkehrssicherungspflicht: BGH III ZR 273/16, Rn. 20", 110, 395,
        beim("p679", "öffentlichen")),
    z("§ 680: Abwendung einer dringenden Gefahr für", 110, 490, beim("p680", "dem"), "Bold", 34),
    z("den Geschäftsherrn: Haftung für Fehler nur bei", 110, 540, beim("p680", "haftet"), "Regular", 34),
    z("Vorsatz und grober Fahrlässigkeit", 110, 585, beim("p680", "Vorsatz"), "Bold", 34),
    zit("BGH, Urt. v. 14.6.2018 – III ZR 54/17, Rn. 48, 55", 110, 640, beim("p680", "Vorsatz")),
    *requisit([("p679", ("tabler", "building-community", 110, WEISS), "öffentliches Interesse", WEISS),
               ("p680", ("tabler", "alert-triangle", 100, GELB), "dringende Gefahr", GELB)]),
    *paar("p679", [("p679", "ruhig"), ("p680", "zufrieden")], [("p679", "denkt"), ("p680", "ruhig")]),
]))

# ===========================================================================================================================
# I1 5. Rechtsfolge, § 670 BGB (Wortlautkarte)
# ===========================================================================================================================
W670 = ["„Macht der Beauftragte zum Zwecke der Ausführung des Auftrags",
        "Aufwendungen, die er den Umständen nach für erforderlich halten",
        "darf, so ist der Auftraggeber zum Ersatz verpflichtet.“"]
w670, w670_y = wortlaut(110, 165, 1040, W670, "§ 670 BGB (über § 683 Satz 1 BGB)", "p5", marken=[
    (1, "Aufwendungen", beim("p5a", "Aufwendungen")),
    (1, "den Umständen nach für erforderlich halten", beim("p5a", "Umständen")),
    (2, "darf", beim("p5a", "darf"))], size=30)
folie([("p5", "5. Rechtsfolge, § 670 BGB"), ("p5b", "5. › erforderlich?")], rechts_frei([
    *tafel("p5", "5. Rechtsfolge"),
    *w670,
    z("wie ein Beauftragter: Ersatz der Aufwendungen", 110, w670_y + 30, beim("p5", "Beauftragter"), "Bold", 34),
    *okz("Jacke durfte er einsetzen: kein Löscher da,", w670_y + 110, "p5b", "Bold", 34, x=160),
    z("Feuer drohte überzugreifen", 160, w670_y + 160, beim("p5b", "Feuer"), "Bold", 34),
    *requisit([("p5", ("tabler", "receipt-euro", 100, WEISS), "Aufwendungsersatz", WEISS),
               ("p5b", ("tabler", "fire-extinguisher", 90, ROT), "kein Löscher da", GELB)]),
    *paar("p5", [("p5", "ruhig"), ("p5b", "zufrieden")], [("p5", "ruhig"), ("p5b", "denkt")]),
]))

# ===========================================================================================================================
# I2 5. Die Jacke als Aufwendung
# ===========================================================================================================================
folie([("p5c", "5. › Jacke als Aufwendung?"), ("p5e", "5. › risikotypische Begleitschäden"), ("p5f", "5. › Höhe")], rechts_frei([
    *tafel("p5c", "5. Die Jacke als Aufwendung?"),
    z("Aufwendungen: freiwillige Vermögensopfer", 110, 190, beim("p5c", "freiwillige"), "Bold", 36),
    zit("BGH, Urt. v. 5.7.2018 – III ZR 273/16, Rn. 28; Urt. v. 19.5.2016 – III ZR 399/14, Rn. 17", 110, 243,
        beim("p5c", "freiwillige")),
    *okz("Jacke bewusst geopfert, um das Feuer zu ersticken", 300, "p5d", "Bold", 34, x=160),
    z("Selbst wenn Schaden: nach h. M. ersetzt, wenn sich", 110, 390, beim("p5e", "herrschender"), "Bold", 34),
    z("die typische Gefahr der Hilfe verwirklicht", 110, 438, beim("p5e", "typische"), "Bold", 34),
    pl("risikotypische Begleitschäden", 110, 500, beim("p5e", "risikotypische"), fill=LILA, size=32),
    z("Neupreis oder Zeitwert? Kann offenbleiben:", 110, 610, "p5f", "Bold", 34),
    blk(110, 670, 1040, 90, GRUEN, beim("p5f", "Harald"), [("Harald verlangt nur den Wert der Jacke: 250 €", "Bold", 34, INK)]),
    *requisit([("p5c", ("tabler", "jacket", 110, RUSS), "die Jacke", WEISS),
               ("p5e", ("tabler", "flame", 90, ORANGE), "typische Gefahr", ROT),
               ("p5f", ("tabler", "cash-banknote", 110, GRUEN), "250 €", GRUEN)]),
    *paar("p5c", [("p5c", "ruhig"), ("p5d", "sorge"), ("p5f", "froh")], [("p5c", "ruhig"), ("p5e", "denkt")]),
]))

# ===========================================================================================================================
# J Abgrenzung: unberechtigte GoA, § 684 Satz 1 BGB (Wortlautkarte)
# ===========================================================================================================================
W684 = ["„Liegen die Voraussetzungen des § 683 nicht vor, so ist der",
        "Geschäftsherr verpflichtet, dem Geschäftsführer alles, was er",
        "durch die Geschäftsführung erlangt, nach den Vorschriften über die",
        "Herausgabe einer ungerechtfertigten Bereicherung herauszugeben.“"]
w684, w684_y = wortlaut(110, 165, 1040, W684, "§ 684 Satz 1 BGB", "p684", marken=[
    (0, "Voraussetzungen des § 683 nicht vor", beim("p684", "fehlt")),
    (1, "alles, was er", beim("p684", "was")),
    (2, "durch die Geschäftsführung erlangt", beim("p684", "durch")),
    (3, "ungerechtfertigten Bereicherung", beim("p684", "Bereicherungsrecht"))], size=30)
folie([("p684", "Abgrenzung: unberechtigte GoA, § 684 S. 1 BGB")], rechts_frei([
    *tafel("p684", "Abgrenzung: unberechtigte GoA"),
    *w684,
    z("Berechtigung fehlt? Nur Herausgabe des Erlangten", 110, w684_y + 30, beim("p684", "fehlt"), "Bold", 34),
    z("nach Bereicherungsrecht", 110, w684_y + 80, beim("p684", "Bereicherungsrecht"), "Bold", 34),
    pl("Mehr dazu: Video zum Bereicherungsrecht", 110, w684_y + 160, "p073", fill=GELB, size=30),
    *requisit([("p684", ("tabler", "arrow-back-up", 100, WEISS), "nur Herausgabe", WEISS)]),
    *paar("p684", [("p684", "denkt")], [("p684", "ruhig"), ("p073", "zufrieden")]),
]))

# ===========================================================================================================================
# K Ergebnis
# ===========================================================================================================================
folie([("erg", "Ergebnis")], rechts_frei([
    *tafel("erg", "Ergebnis"),
    *okz("Harald hat ein Geschäft von Frau Huber", 200, "erg", "Bold", 36, x=160),
    z("berechtigt geführt", 160, 252, beim("erg", "berechtigt"), "Bold", 36),
    blk(110, 350, 1040, 130, GRUEN, "erg2", [("Frau Huber muss Harald", "ExtraBold", 38, INK),
                                            ("250 € für die Jacke zahlen", "Bold", 36, INK)]),
    zit("§§ 677, 683 Satz 1, 670 BGB", 110, 500, "erg2"),
    *requisit([("erg", ("tabler", "checklist", 100, WEISS), "berechtigte GoA", GRUEN),
               ("erg2", ("tabler", "cash-banknote", 110, GRUEN), "250 €", GRUEN)]),
    *paar("erg", [("erg", "ruhig"), ("erg2", "froh")], [("erg", "ernst"), ("erg2", "zufrieden")]),
]))

# ===========================================================================================================================
# L Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · ohne Auftrag ist nicht gegen den Willen")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("„ohne Auftrag“ ist nicht „gegen den Willen“", 200, 200, beim("tipp", "Verwechsle"), "Bold", 36),
    *okz("niemand hat um Hilfe gebeten: Punkt 3", 300, "tipp2", "Bold", 34, x=250),
    *okz("Berechtigung: wirklicher oder mutmaßlicher", 400, "tipp3", "Bold", 34, x=250),
    z("Wille bei der Übernahme, Punkt 4", 250, 450, beim("tipp3", "Übernahme"), "Bold", 34),
    dicon("tabler", "clock", 980, 820, 130, beim("tipp3", "Übernahme"), fuell=GELB),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# M Klausurschema (progressiv)
# ===========================================================================================================================
REIHEN = [("k1", "I.", "Geschäftsbesorgung", None, BLAU),
          ("k2", "II.", "fremdes Geschäft mit Fremdgeschäftsführungswillen", "beim objektiv fremden Geschäft vermutet", GRUEN),
          ("k3", "III.", "ohne Auftrag oder sonstige Berechtigung, § 677 BGB", None, GELB),
          ("k4", "IV.", "Berechtigung: § 683 Satz 1 BGB (Interesse und Wille)", "oder § 679 BGB", LILA),
          ("k5", "V.", "Ersatz der erforderlichen Aufwendungen, § 670 BGB", "auch risikotypischer Begleitschäden", ROT)]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Schema: Aufwendungsersatz, §§ 677, 683 Satz 1, 670 BGB"), 110, 90, "sch", 46)]
y = 200
for c, r, txt, sub, farbe in REIHEN:
    els_sch += [karte(110, y, 120, 70, c, fill=farbe, rund=14, schatten=5, rand=4),
                z(r, 170 - F("ExtraBold", 36).getlength(r) / 2, y + 11, c, "ExtraBold", 36, rechts=1820),
                z(txt, 265, y + 11, c, "Bold", 36, rechts=1820)]
    if sub:
        c2 = {"k2": beim("k2", "beim"), "k4": beim("k4", "oder"), "k5": beim("k5", "auch")}[c]
        els_sch.append(z(sub, 265, y + 64, c2, "Regular", 32, rechts=1820))
        y += 40
    y += 110
assert y <= 975, y
folie([("sch", "Schema: §§ 677, 683 S. 1, 670 BGB"), ("k1", "Schema › I. Geschäftsbesorgung"),
       ("k2", "Schema › II. fremdes Geschäft"), ("k3", "Schema › III. ohne Auftrag"), ("k4", "Schema › IV. Berechtigung"),
       ("k5", "Schema › V. Rechtsfolge")], els_sch)

# ===========================================================================================================================
# N Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Wer ungefragt im ", 0), ("Interesse", "a"), (" und", 0)],
                 [("mutmaßlichen Willen", "b"), (" eines anderen hilft,", 0)]], 750, 290, 42, "merke",
                {"a": beim("merke", "Interesse"), "b": beim("merke", "mutmaßlichen")}),
    *markertext([[("bekommt seine erforderlichen", 0)], [("Aufwendungen ersetzt,", "c")]], 750, 480, 42, "mk2",
                {"c": beim("mk2", "Aufwendungen")}),
    *markertext([[("nach herrschender Meinung auch", 0)], [("typische Schäden", "d"), (" beim Helfen.", 0)]],
                750, 670, 42, "mk3", {"d": beim("mk3", "typische")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
