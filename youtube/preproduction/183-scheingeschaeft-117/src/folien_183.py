"""Folge 183 · Scheingeschäft § 117 BGB: Schwarzgeld beim Hauskauf – welcher Preis? Serienstandard Open Peeps (Katzenkönig).
Fall: Markus kauft von Frau Meinhardt ein Haus; vereinbart 350.000 €, beurkundet 300.000 €, 50.000 € vorher bar im Umschlag;
Auflassung im selben Termin, Wochen später Eintragung. Notar ohne Namen, ohne Rede, neutral.
Szenen laut ../SZENENPLAN.md: A1 Die Absprache, A2 Beim Notar, A3 Die Frage, B Sachverhalt, C Aufbau, D 1. beurkundeter
Vertrag § 117 Abs. 1 (Wortlaut), E 2. verdeckter Vertrag § 117 Abs. 2 (Wortlaut), F 3. Form § 311b Abs. 1 S. 1 (Wortlaut),
G § 125 S. 1 (Wortlaut), H 4. Heilung § 311b Abs. 1 S. 2 (Wortlaut), I Heilung: Inhalt und Grenzen, J Folgen vor/nach der
Eintragung, K Hinweise Steuer und § 16a GwG, L Abgrenzung §§ 118, 116 (Wortlaut), M Klausurtipp (Lexi), N Klausurschema,
O Merksatz (Lexi).
Schwarzgeld nur als Umschlag-Symbol (Phosphor envelope) mit Pille, keine Geldbündel, keine Verherrlichung.
Handlungsgeräusch: Unterschrift beim Notar (../geraeusche_herkunft.json).
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/
tisch als eigene Kopie aus Folge 145 (gemeinsame Dateien unverändert); neu: paar(), requisit(), option().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_183/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_183/" in n:
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
NAME = {"MA": "Markus", "MH": "Frau Meinhardt", "NT": "Notar"}
NFARBE = {"MA": BLAU, "MH": ROT, "NT": WEISS}
HAUS = GELB                                 # das Haus durchgehend gelb (Phosphor house)
GB = BLAU                                   # Grundbuch durchgehend blau (Tabler book-2)
UMS = WEISS                                 # Umschlag (Phosphor envelope) durchgehend weiß mit Pille


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
# A1 Fall: die Absprache vor dem Haus (Haus links, Frau Meinhardt blickt nach rechts zu Markus, Markus nach links)
# ===========================================================================================================================
HX, MHX, MAX = 300, 800, 1560
folie([(NULL, "Fall · Der Hauskauf"), ("vorher", "Fall · Die Absprache")], [
    boden(NULL, hart_=True),
    hart(ficon("ph", "house", HX, BODEN, 380, NULL, fuell=HAUS)),
    pl("Markus kauft ein Haus", 70, 30, NULL, fill=GELB, size=40, anim="cut", bis="mh1"),
    *fig("MA", MAX, BODEN, FH, [(NULL, "laechelt"), ("verk", "ruhig"), ("preis", "froh"), ("vorher", "ruhig"),
                                ("mh1", "denkt")], erst="cut", bis="ma1"),
    hart(ns("Markus", MAX, BODEN, NULL, NFARBE["MA"])),
    *redet("MA_redet", MAX, BODEN, FH, "ma1", "umschl"),
    pl("Es gehört Frau Meinhardt", 70, 120, beim("verk", "Frau"), fill=WEISS, size=36, bis="mh1"),
    *fig("MH", MHX, BODEN, FH, [(beim("verk", "gehört"), "ruhig_r"), ("preis", "froh_r")], bis="mh1"),
    ns("Frau Meinhardt", MHX, BODEN, beim("verk", "gehört"), NFARBE["MH"], d=0.1),
    *redet("MH_redet_r", MHX, BODEN, FH, "mh1", "ma1"),
    *fig("MH", MHX, BODEN, FH, [("ma1", "froh_r")], erst="cut"),
    ficon("ph", "handshake", 1180, 700, 150, beim("preis", "einigen"), fuell=GRUEN, bis="vorher"),
    pl("vereinbart: 350.000 €", 1180, 730, beim("preis", "dreihundertfünfzigtausend"), fill=GRUEN, size=30, anker="m",
       bis="vorher"),
    pl("vor dem Notartermin", 70, 210, "vorher", fill=WEISS, size=34, bis="mh1"),
    ficon("ph", "envelope", 1180, 700, 140, beim("ma1", "Umschlag"), fuell=UMS),
    pl("50.000 € bar", 1180, 730, beim("ma1", "Umschlag"), fill=WEISS, size=30, anker="m"),
    blase("sprech", 980, 200, "mh1", 1190, 200, inhalt=["In den Vertrag schreiben wir nur 300.000.", "Den Rest geben Sie mir bar."],
          textsize=34, figur=("MH_redet_r", MHX, BODEN, FH), bis="ma1"),
    blase("sprech", 860, 210, "ma1", 1220, 215, inhalt=["Gut. Die 50.000 bekommen Sie", "vorher im Umschlag."], textsize=36,
          figur=("MA_redet", MAX, BODEN, FH), bis="umschl"),
])

# ===========================================================================================================================
# A2 Fall: beim Notar (Frau Meinhardt links, Notar hinter dem Tisch, Markus rechts); Wochen später: Grundbuch
# ===========================================================================================================================
MH2, NTX, MA2 = 330, 960, 1580
UNT = beim("unter", "unterschreiben")
folie([("umschl", "Fall · Die Übergabe"), ("notar", "Fall · Beim Notar"), ("eintr", "Fall · Wochen später")], [
    boden("umschl"),
    pl("So geschieht es: 50.000 € im Umschlag", 70, 30, "umschl", fill=WEISS, size=36, bis="notar"),
    ficon("ph", "envelope", MH2, 360, 120, "umschl", fuell=UMS, bis="notar"),
    *fig("MH", MH2, BODEN, FH, [("umschl", "froh_r"), ("notar", "ruhig_r"), ("eintr", "ruhig_r")], d=0.0),
    ns("Frau Meinhardt", MH2, BODEN, "umschl", NFARBE["MH"], d=0.1),
    *fig("MA", MA2, BODEN, FH, [("umschl", "ruhig"), ("notar", "denkt"), ("unter", "laechelt"), ("eintr", "froh")], d=0.2),
    ns("Markus", MA2, BODEN, "umschl", NFARBE["MA"], d=0.3),
    # Notar hinter dem Tisch (Tisch nach der Figur gezeichnet, verdeckt die Beine)
    *fig("NT", NTX, BODEN, FH, [(beim("notar", "Notar"), "ruhig"), ("unter", "laechelt_r"), ("eintr", "ruhig")]),
    tisch(NTX, BODEN, beim("notar", "Notar"), w=460, h=230, fill=GELB),
    ns("Notar", NTX, BODEN, beim("notar", "Notar"), NFARBE["NT"], d=0.1),
    ficon("tabler", "contract", NTX - 170, BODEN - 236, 90, beim("notar", "Vertrag"), fuell=WEISS),
    pl("Kaufpreis: 300.000 €", 70, 30, beim("notar", "Kaufpreis"), fill=WEISS, size=40, bis="eintr"),
    szene(ficon("tabler", "writing-sign", NTX + 170, BODEN - 236, 90, UNT, fuell=WEISS), "183unterschrift*", 0.7, 0.0),
    pl("Beide unterschreiben", 70, 120, UNT, fill=GRUEN, size=36, bis="eintr"),
    ficon("ph", "handshake", 740, 380, 120, beim("aufl", "Auflassung"), fuell=GRUEN, bis="eintr"),
    pl("Auflassung im selben Termin", 70, 210, beim("aufl", "Auflassung"), fill=GRUEN, size=36, bis="eintr"),
    pl("Wochen später", 70, 30, "eintr", fill=WEISS, size=40),
    ficon("tabler", "book-2", 740, 380, 120, beim("eintr", "Grundbuch"), fuell=GB),
    pl("Grundbuch: Markus ist Eigentümer", 70, 120, beim("eintr", "Grundbuch"), fill=BLAU, size=36),
])

# ===========================================================================================================================
# A3 Die Frage: zwei Verträge links, Markus und Frau Meinhardt rechts
# ===========================================================================================================================


def option(cx, cue, ic, fuell, text, fill):
    return [ficon(ic[0], ic[1], cx, 600, 200, cue, fuell=fuell), pl(text, cx, 640, cue, fill=fill, size=32, anker="m")]


folie([("frage", "Fall · Die Frage")], [
    boden("frage"),
    pl("Welcher Vertrag gilt?", 70, 30, "frage", fill=PINK, size=44),
    pl("Und zu welchem Preis?", 70, 130, "f2", fill=PINK, size=44),
    *option(330, "frage", ("tabler", "contract"), WEISS, "beurkundet: 300.000 €", WEISS),
    *option(860, "frage", ("ph", "handshake"), GRUEN, "vereinbart: 350.000 €", GRUEN),
    ficon("tabler", "question-mark", 330, 370, 90, "f2", fuell=None),
    ficon("tabler", "question-mark", 860, 370, 90, "f2", fuell=None),
    *fig("MH", 1300, BODEN, FH, [("frage", "denkt"), ("f2", "sorge")]),
    ns("Frau Meinhardt", 1300, BODEN, "frage", NFARBE["MH"], d=0.1),
    *fig("MA", 1640, BODEN, FH, [("frage", "denkt"), ("f2", "staunt")], d=0.2),
    ns("Markus", 1640, BODEN, "frage", NFARBE["MA"], d=0.3),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_183(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=42, zeilenabstand=1.32)
        els += e; y += 22
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 10, cue, fill=PINK, size=40))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_183("sv", [
    "Markus kauft von Frau Meinhardt ein Haus. Die beiden einigen sich auf einen Kaufpreis von 350.000 €. Auf Vorschlag "
    "von Frau Meinhardt soll im Vertrag nur ein Preis von 300.000 € stehen; die restlichen 50.000 € gibt Markus ihr vorher "
    "bar im Umschlag.",
    "Beim Notar wird der Kaufvertrag mit einem Kaufpreis von 300.000 € beurkundet. Beide unterschreiben und erklären im "
    "selben Termin die Auflassung. Wochen später wird Markus als Eigentümer ins Grundbuch eingetragen.",
], "Welcher Vertrag gilt, und zu welchem Preis?")

# ===========================================================================================================================
# C Aufbau: vier Schritte
# ===========================================================================================================================
SCHRITTE = [("s1", "1.", "beurkundeter Vertrag (300.000 €)", GELB), ("s2", "2.", "verdeckter Vertrag (350.000 €)", GRUEN),
            ("s3", "3.", "Form", BLAU), ("s4", "4.", "Heilung", LILA)]
folie([("plan", "Scheingeschäft › Aufbau")], rechts_frei([
    *tafel("plan", "Prüfung in vier Schritten"),
    *[e for k, (c, r, t, fa) in enumerate(SCHRITTE) for e in (
        karte(130, 220 + k * 140, 110, 90, c, fill=fa, rund=14, schatten=5, rand=4),
        z(r, 185 - F("ExtraBold", 40).getlength(r) / 2, 240 + k * 140, c, "ExtraBold", 40),
        z(t, 280, 240 + k * 140, c, "Bold", 40))],
    *requisit([("plan", ("ph", "house", 150, HAUS), "4 Schritte", WEISS),
               ("s1", ("tabler", "contract", 100, WEISS), "300.000 €", WEISS),
               ("s2", ("ph", "handshake", 120, GRUEN), "350.000 €", GRUEN),
               ("s3", ("tabler", "writing-sign", 100, WEISS), "Form", BLAU),
               ("s4", ("tabler", "book-2", 110, GB), "Heilung", LILA)]),
    *paar("plan", "MH", [("plan", "ruhig"), ("s2", "denkt"), ("s4", "ruhig")], "MA", [("plan", "ruhig"), ("s3", "denkt")]),
]))

# ===========================================================================================================================
# D 1. beurkundeter Vertrag: § 117 Abs. 1 (Wortlaut)
# ===========================================================================================================================
W117 = ["„(1) Wird eine Willenserklärung, die einem anderen gegenüber",
        "abzugeben ist, mit dessen Einverständnis nur zum Schein",
        "abgegeben, so ist sie nichtig.“"]
w117, w117_y = wortlaut(80, 180, 1100, W117, "§ 117 Abs. 1 BGB", "k1", marken=[
    (1, "mit dessen Einverständnis", beim("w117", "Einverständnis")), (1, "nur zum Schein", beim("w117", "Schein")),
    (2, "nichtig", beim("w117", "nichtig"))], size=33)
folie([("k1", "1. Beurkundeter Vertrag › § 117 Abs. 1 BGB"), ("nicht1", "1. Beurkundeter Vertrag › nichtig")], rechts_frei([
    *tafel("k1", "1. Beurkundeter Vertrag: 300.000 €"),
    *w117,
    z("Scheingeschäft: Das Erklärte soll nach dem", 110, w117_y + 40, "schein", "Bold", 36),
    z("übereinstimmenden Willen beider nicht gelten.", 110, w117_y + 95, beim("schein", "übereinstimmenden"), "Bold", 36),
    zit("vgl. BGH, Urt. v. 20.5.2011 – V ZR 221/10, Rn. 6", 110, w117_y + 150, beim("schein", "übereinstimmenden")),
    *okz("Fall: Keiner will 300.000 € als Preis.", w117_y + 220, beim("fall1", "Keiner"), size=36, x=160),
    *neinz("beurkundeter Vertrag: nichtig, § 117 Abs. 1 BGB", w117_y + 300, beim("nicht1", "nichtig"), "Bold", 36, x=160),
    *requisit([("k1", ("tabler", "contract", 100, WEISS), "beurkundet: 300.000 €", WEISS),
               (beim("w117", "Schein"), ("tabler", "masks-theater", 110, LILA), "nur zum Schein", LILA),
               (beim("nicht1", "nichtig"), ("tabler", "ban", 100, ROT), "nichtig", ROT)]),
    *paar("k1", "MH", [("k1", "ruhig"), ("schein", "denkt"), ("nicht1", "ernst")], "MA",
          [("k1", "ruhig"), ("fall1", "denkt"), ("nicht1", "sorge")]),
]))

# ===========================================================================================================================
# E 2. verdeckter Vertrag: § 117 Abs. 2 (Wortlaut)
# ===========================================================================================================================
W1172 = ["„(2) Wird durch ein Scheingeschäft ein anderes Rechtsgeschäft",
         "verdeckt, so finden die für das verdeckte Rechtsgeschäft",
         "geltenden Vorschriften Anwendung.“"]
w1172, w1172_y = wortlaut(80, 180, 1100, W1172, "§ 117 Abs. 2 BGB", "k2", marken=[
    (0, "ein anderes Rechtsgeschäft", beim("w1172", "anderes")), (1, "verdeckt", beim("w1172", "verdeckt")),
    (2, "geltenden Vorschriften", beim("w1172", "geltenden"))], size=33)
folie([("k2", "2. Verdeckter Vertrag › § 117 Abs. 2 BGB")], rechts_frei([
    *tafel("k2", "2. Verdeckter Vertrag: 350.000 €"),
    *w1172,
    *okz("wirklich gewollt: Kauf zu 350.000 €", w1172_y + 50, beim("gewollt", "wollen"), "Bold", 36, x=160),
    z("Wirksam? Erst, wenn er nach seinen", 160, w1172_y + 140, "regeln", "Bold", 36),
    z("eigenen Regeln besteht.", 160, w1172_y + 195, beim("regeln", "eigenen"), "Bold", 36),
    *requisit([("k2", ("ph", "handshake", 120, GRUEN), "vereinbart: 350.000 €", GRUEN),
               (beim("w1172", "verdeckt"), ("tabler", "eye-off", 100, WEISS), "verdeckt", WEISS),
               ("regeln", ("tabler", "checklist", 100, WEISS), "eigene Regeln", GELB)]),
    *paar("k2", "MH", [("k2", "ruhig"), ("gewollt", "froh"), ("regeln", "denkt")], "MA",
          [("k2", "ruhig"), ("gewollt", "laechelt"), ("regeln", "denkt")]),
]))

# ===========================================================================================================================
# F 3. Form: § 311b Abs. 1 S. 1 (Wortlaut)
# ===========================================================================================================================
W311 = ["„(1) Ein Vertrag, durch den sich der eine Teil verpflichtet,",
        "das Eigentum an einem Grundstück zu übertragen oder zu",
        "erwerben, bedarf der notariellen Beurkundung. …“"]
w311, w311_y = wortlaut(80, 180, 1100, W311, "§ 311b Abs. 1 S. 1 BGB", beim("k3", "Paragraf"), marken=[
    (1, "Eigentum an einem Grundstück", beim("w311", "Eigentum")),
    (2, "notariellen Beurkundung", beim("w311", "notariellen"))], size=33)
folie([("k3", "3. Form › § 311b Abs. 1 S. 1 BGB"), ("nurs", "3. Form › nur der Scheinpreis beurkundet")], rechts_frei([
    *tafel("k3", "3. Form: notarielle Beurkundung"),
    *w311,
    z("Beurkundet werden müssen alle Vereinbarungen,", 110, w311_y + 40, "alle", "Bold", 36),
    z("aus denen sich der Kauf zusammensetzt,", 110, w311_y + 95, beim("alle", "aus"), "Bold", 36),
    z("also auch der wahre Preis.", 110, w311_y + 150, beim("alle", "wahre"), "Bold", 36),
    zit("vgl. BGH, Urt. v. 27.5.2011 – V ZR 122/10, Rn. 6", 110, w311_y + 205, beim("alle", "wahre")),
    *neinz("beurkundet: nur der Scheinpreis (300.000 €)", w311_y + 275, beim("nurs", "Scheinpreis"), "Bold", 36, x=160),
    *requisit([("k3", ("tabler", "writing-sign", 100, WEISS), "notarielle Beurkundung", WEISS),
               ("alle", ("tabler", "checklist", 100, WEISS), "alle Vereinbarungen", GELB),
               (beim("nurs", "Scheinpreis"), ("tabler", "contract", 100, WEISS), "nur 300.000 €", ROT)]),
    *paar("k3", "MH", [("k3", "ruhig"), ("alle", "denkt"), ("nurs", "sorge")], "MA",
          [("k3", "ruhig"), ("alle", "staunt"), ("nurs", "sorge")]),
]))

# ===========================================================================================================================
# G § 125 S. 1 (Wortlaut): zunächst formnichtig; Verweis 050
# ===========================================================================================================================
W125 = ["„Ein Rechtsgeschäft, welches der durch Gesetz vorgeschriebenen",
        "Form ermangelt, ist nichtig. …“"]
w125, w125_y = wortlaut(80, 180, 1100, W125, "§ 125 S. 1 BGB", "w125", marken=[
    (0, "durch Gesetz vorgeschriebenen", beim("w125", "Gesetz")), (1, "nichtig", beim("w125", "nichtig"))], size=33)
folie([("w125", "3. Form › § 125 S. 1 BGB")], rechts_frei([
    *tafel("w125", "3. Form: Folge des Mangels"),
    *w125,
    *neinz("wahrer Kauf (350.000 €): zunächst formnichtig", w125_y + 50, beim("fn", "formnichtig"), "Bold", 36, x=160),
    zit("BGH, Urt. v. 15.3.2024 – V ZR 115/22, Rn. 8", 160, w125_y + 105, beim("fn", "formnichtig")),
    blk(110, w125_y + 180, 1040, 80, LILA, "verw050", [("Mehr dazu: Video „Kündigung per WhatsApp“", "ExtraBold", 32, INK)]),
    *requisit([("w125", ("tabler", "file-x", 100, WEISS), "Formmangel", WEISS),
               (beim("fn", "formnichtig"), ("tabler", "ban", 100, ROT), "formnichtig", ROT),
               ("verw050", ("tabler", "writing-sign", 100, WEISS), "Formvorschriften", LILA)]),
    *paar("w125", "MH", [("w125", "ernst"), ("verw050", "ruhig")], "MA", [("w125", "sorge"), ("verw050", "ruhig")]),
]))

# ===========================================================================================================================
# H 4. Heilung: § 311b Abs. 1 S. 2 (Wortlaut), Verweis 145
# ===========================================================================================================================
W311B = ["„Ein ohne Beachtung dieser Form geschlossener Vertrag wird",
         "seinem ganzen Inhalt nach gültig, wenn die Auflassung und",
         "die Eintragung in das Grundbuch erfolgen.“"]
w311b, w311b_y = wortlaut(80, 180, 1100, W311B, "§ 311b Abs. 1 S. 2 BGB", beim("k4", "Satz"), marken=[
    (1, "seinem ganzen Inhalt nach gültig", beim("w311b", "gültig")), (1, "Auflassung", beim("w311b", "Auflassung")),
    (2, "die Eintragung in das Grundbuch", beim("w311b", "Eintragung"))], size=33)
folie([("k4", "4. Heilung › § 311b Abs. 1 S. 2 BGB")], rechts_frei([
    *tafel("k4", "4. Heilung"),
    *w311b,
    *okz("im Fall: Auflassung erklärt, Markus eingetragen", w311b_y + 50, beim("w311b", "erfolgen"), "Bold", 34, x=160),
    blk(110, w311b_y + 140, 1040, 80, LILA, "verw145", [("Ablauf: Video „Hauskauf in drei Schritten“", "ExtraBold", 32, INK)]),
    *requisit([("k4", ("tabler", "file-check", 100, GRUEN), "Heilung", GRUEN),
               (beim("w311b", "Auflassung"), ("ph", "handshake", 120, GRUEN), "Auflassung", GRUEN),
               (beim("w311b", "Eintragung"), ("tabler", "book-2", 110, GB), "Eintragung", BLAU),
               ("verw145", ("ph", "house", 150, HAUS), "Hauskauf", WEISS)]),
    *paar("k4", "MH", [("k4", "ruhig"), (beim("w311b", "Eintragung"), "denkt")], "MA",
          [("k4", "ruhig"), (beim("w311b", "erfolgen"), "froh")]),
]))

# ===========================================================================================================================
# I Heilung: ganzer Inhalt, BGH 2024, Grenzen
# ===========================================================================================================================
folie([("ganz", "4. Heilung › ganzer Inhalt"), ("exn", "4. Heilung › Grenzen")], rechts_frei([
    *tafel("ganz", "4. Heilung: was sie bewirkt"),
    *okz("ganzer Inhalt: mit dem wahren Preis (350.000 €)", 180, beim("ganz", "wahren"), "Bold", 34, x=160),
    z("BGH 2024, Schwarzgeldabrede: Formmangel durch", 160, 250, "bgh", size=34),
    z("Auflassung und Eintragung geheilt", 160, 300, beim("bgh", "geheilt"), "Bold", 34),
    zit("BGH, Urt. v. 15.3.2024 – V ZR 115/22, Rn. 8", 160, 352, beim("bgh", "geheilt")),
    linienzug([(110, 410), (1150, 410)], "exn", breite=3),
    *okz("wirkt nur für die Zukunft", 435, beim("exn", "Zukunft"), size=34, x=160),
    zit("BGH, Urt. v. 27.5.2011 – V ZR 122/10, Rn. 6", 160, 485, beim("exn", "Zukunft")),
    *okz("Einigung muss bei der Auflassung noch bestehen", 535, beim("fort", "Auflassung"), size=34, x=160),
    zit("BGH, Urt. v. 13.5.2016 – V ZR 265/14, Rn. 29", 160, 585, beim("fort", "Auflassung")),
    *neinz("andere Nichtigkeitsgründe: keine Heilung", 635, beim("nurf", "Nichtigkeitsgründe"), "Bold", 34, x=160),
    zit("BGH, Urt. v. 15.3.2024 – V ZR 115/22, Rn. 10", 160, 685, beim("nurf", "Nichtigkeitsgründe")),
    *requisit([("ganz", ("ph", "handshake", 120, GRUEN), "350.000 €", GRUEN),
               ("bgh", ("tabler", "gavel", 100, WEISS), "BGH 2024", WEISS),
               ("exn", ("tabler", "clock", 100, WEISS), "ab jetzt", WEISS),
               ("nurf", ("tabler", "file-x", 100, WEISS), "nur der Formmangel", ROT)]),
    *paar("ganz", "MH", [("ganz", "ruhig"), ("bgh", "denkt"), ("nurf", "ernst")], "MA",
          [("ganz", "froh"), ("exn", "denkt"), ("nurf", "ruhig")]),
]))

# ===========================================================================================================================
# J Folgen: vor und nach der Eintragung (mit Figurenrede)
# ===========================================================================================================================
MHF, MAF = X1, X2
folie([("vor", "Folgen › vor der Eintragung"), ("nach", "Folgen › nach der Eintragung")], rechts_frei([
    *tafel("vor", "Folgen: vor und nach der Eintragung", size=44),
    blk(110, 175, 1040, 70, HELLROT, beim("vor", "Angenommen"), [("Vor der Eintragung: Vertrag unwirksam", "ExtraBold", 34, INK)]),
    *neinz("Frau Meinhardt muss das Haus nicht übereignen", 270, beim("unw", "übereignen"), size=34, x=160),
    *okz("Markus: Geld grundsätzlich zurück, § 812 BGB", 330, beim("r812", "Paragraf"), "Bold", 34, x=160),
    z("ohne Rechtsgrund gezahlt", 160, 385, beim("r812", "Rechtsgrund"), size=34),
    zit("vgl. BGH, Urt. v. 27.5.2011 – V ZR 122/10, Rn. 15", 160, 437, beim("r812", "Rechtsgrund")),
    blk(110, 500, 1040, 70, HELLGRUEN, "nach", [("Nach der Eintragung: Vertrag geheilt", "ExtraBold", 34, INK)]),
    *neinz("„Ich will mein Haus zurück!“: ohne Erfolg", 595, beim("geb", "Ohne"), size=34, x=160),
    *okz("Vertrag gilt mit 350.000 €", 655, beim("geb", "dreihundertfünfzigtausend"), "Bold", 34, x=160),
    *okz("beide gebunden, Markus ist Eigentümer", 715, beim("geb", "Beide"), "Bold", 34, x=160),
    zit("vgl. BGH, Urt. v. 15.3.2024 – V ZR 115/22, Rn. 7 f.", 160, 770, beim("geb", "Beide")),
    *fig("MH", MHF, FB, FR, [("vor", "ruhig"), ("ma2", "sorge_r"), ("unw", "ruhig"), ("nach", "denkt"), ("nachm", "ernst")], bis="mh2"),
    ns("Frau Meinhardt", MHF, FB, "vor", NFARBE["MH"], d=0.1),
    *redet("MH_streng_r", MHF, FB, FR, "mh2", "geb"),
    *fig("MH", MHF, FB, FR, [("geb", "sorge")], erst="cut"),
    *fig("MA", MAF, FB, FR, [("vor", "ruhig"), ("vorm", "sorge")], bis="ma2", d=0.2),
    ns("Markus", MAF, FB, "vor", NFARBE["MA"], d=0.3),
    *redet("MA_ernst", MAF, FB, FR, "ma2", "unw"),
    *fig("MA", MAF, FB, FR, [("unw", "denkt"), ("r812", "laechelt"), ("nach", "ruhig"), ("mh2", "staunt"), ("geb", "froh")],
         erst="cut"),
    ficon("tabler", "arrow-back-up", PX, PU, 100, beim("r812", "Paragraf"), fuell=None, bis="nach"),
    pl("50.000 € zurück", PX, PY, beim("r812", "Paragraf"), fill=WEISS, size=28, anker="m", bis="nach"),
    ficon("tabler", "book-2", PX, PU, 110, "nach", fuell=GB, bis="mh2"),
    pl("eingetragen", PX, PY, "nach", fill=BLAU, size=28, anker="m", bis="mh2"),
    ficon("ph", "house", PX, PU, 150, beim("geb", "Beide"), fuell=HAUS),
    pl("Eigentümer: Markus", PX, PY, beim("geb", "Beide"), fill=GRUEN, size=28, anker="m"),
    blase("sprech", 620, 200, "ma2", 1560, 210, inhalt=["Dann will ich meine", "50.000 zurück."], textsize=36,
          figur=("MA_ernst", MAF, FB, FR), bis="unw"),
    blase("sprech", 680, 200, "mh2", 1570, 210, inhalt=["Der Vertrag war doch nichtig.", "Ich will mein Haus zurück!"],
          textsize=32, figur=("MH_streng_r", MHF, FB, FR), bis="geb"),
]))

# ===========================================================================================================================
# K Hinweise: Steuer, Barzahlungsverbot § 16a GwG
# ===========================================================================================================================
folie([("steuer", "Hinweis › Steuer"), ("gwg", "Hinweis › Barzahlungsverbot, § 16a GwG")], rechts_frei([
    *tafel("steuer", "Zwei Hinweise"),
    z("Grunderwerbsteuer verkürzt:", 110, 180, beim("steuer", "Grunderwerbsteuer"), "Bold", 34),
    z("strafbar als Steuerhinterziehung möglich", 110, 232, beim("steuer", "Steuerhinterziehung"), size=34),
    zit("§ 370 Abs. 1 Nr. 1 AO", 110, 284, beim("steuer", "Steuerhinterziehung")),
    *okz("Kaufvertrag: in der Regel nicht nichtig", 330, beim("steuer", "Regel"), "Bold", 34, x=160),
    zit("BGH, Urt. v. 15.3.2024 – V ZR 115/22, Rn. 13", 160, 382, beim("steuer", "Regel")),
    linienzug([(110, 438), (1150, 438)], "gwg", breite=3),
    z("Seit April 2023: § 16a GwG", 110, 460, "gwg", "Bold", 34),
    z("Kaufpreis einer Immobilie: nicht mit Bargeld", 110, 512, beim("gwg", "Bargeld"), size=34),
    *neinz("bar Übergebenes tilgt den Preis nicht", 575, beim("gwg2", "tilgt"), "Bold", 34, x=160),
    *okz("Käufer kann es herausverlangen", 635, beim("gwg2", "herausverlangen"), size=34, x=160),
    zit("§ 16a Abs. 1 S. 1, 3 GwG; § 59 Abs. 11 GwG", 160, 687, beim("gwg2", "herausverlangen")),
    z("Folgen für den Vertrag: vom BGH offengelassen", 110, 740, beim("offen", "offengelassen"), "Bold", 34),
    zit("BGH, Urt. v. 15.3.2024 – V ZR 115/22, Rn. 12", 110, 792, beim("offen", "offengelassen")),
    *requisit([("steuer", ("tabler", "receipt-tax", 100, WEISS), "Steuer", WEISS),
               ("gwg", ("tabler", "cash-banknote", 120, WEISS), "kein Bargeld", ROT),
               ("gwg2", ("ph", "envelope", 120, UMS), "herausverlangen", WEISS),
               ("offen", ("tabler", "question-mark", 90, None), "offengelassen", GELB)]),
    *paar("steuer", "MH", [("steuer", "sorge"), ("gwg", "staunt"), ("offen", "denkt")], "MA",
          [("steuer", "sorge"), ("gwg", "staunt"), ("offen", "denkt")]),
]))

# ===========================================================================================================================
# L Abgrenzung: § 118 und § 116 (Wortlaut), Scheingeschäft
# ===========================================================================================================================
W118 = ["„Eine nicht ernstlich gemeinte Willenserklärung, die in der",
        "Erwartung abgegeben wird, der Mangel der Ernstlichkeit werde",
        "nicht verkannt werden, ist nichtig.“"]
w118, w118_y = wortlaut(80, 175, 1100, W118, "§ 118 BGB", "w118", marken=[
    (1, "Mangel der Ernstlichkeit", beim("w118", "fehlenden")), (2, "ist nichtig", beim("w118", "nichtig"))], size=30)
W116 = ["„Eine Willenserklärung ist nicht deshalb nichtig, weil sich der",
        "Erklärende insgeheim vorbehält, das Erklärte nicht zu wollen.",
        "Die Erklärung ist nichtig, wenn sie einem anderen gegenüber",
        "abzugeben ist und dieser den Vorbehalt kennt.“"]
w116, w116_y = wortlaut(80, w118_y + 18, 1100, W116, "§ 116 BGB", "w116", marken=[
    (1, "insgeheim vorbehält", beim("w116", "insgeheim")), (0, "nicht deshalb nichtig", beim("w116", "wirksam")),
    (3, "dieser den Vorbehalt kennt", beim("w116", "kennt"))], size=30)
folie([("abgr", "Abgrenzung › § 118 BGB"), ("w116", "Abgrenzung › § 116 BGB"), ("beide", "Abgrenzung › § 117 BGB")],
      rechts_frei([
    *tafel("abgr", "Abgrenzung: Scherz und Vorbehalt"),
    *w118, *w116,
    blk(110, w116_y + 18, 1040, 70, HELLGRUEN, "beide", [("§ 117: Beide sind einig, das Erklärte soll nicht gelten.", "ExtraBold", 30, INK)]),
    *requisit([("w118", ("tabler", "mood-wink", 100, GELB), "Scherz: nichtig", GELB),
               ("w116", ("tabler", "eye-off", 100, WEISS), "geheimer Vorbehalt", WEISS),
               ("beide", ("tabler", "masks-theater", 110, LILA), "beide einig", LILA)]),
    *paar("abgr", "MH", [("abgr", "ruhig"), ("w118", "froh"), ("w116", "denkt"), ("beide", "ruhig")], "MA",
          [("abgr", "ruhig"), ("w118", "laechelt"), ("w116", "denkt"), ("beide", "ruhig")]),
]))

# ===========================================================================================================================
# M Klausurtipp (Lexi)
# ===========================================================================================================================
TIPP = [("t1", "1. Scheingeschäft"), ("t2", "2. verdecktes Geschäft"), ("t3", "3. Form"), ("t4", "4. Heilung")]
folie([("tipp", "Klausurtipp · Reihenfolge"), ("t5", "Klausurtipp · Was geheilt wird")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Prüfe getrennt, in dieser Reihenfolge:", 200, 200, beim("tipp", "getrennt"), "Bold", 36),
    *[z(t, 240, 270 + i * 55, c if c != "t4" else beim("t4", "Heilung"), size=34) for i, (c, t) in enumerate(TIPP)],
    linienzug([(130, 510), (1130, 510)], "t5", breite=3),
    z("Geheilt wird nur der verdeckte Vertrag.", 200, 535, beim("t5", "Geheilt"), "Bold", 34),
    z("Der Scheinvertrag bleibt nichtig.", 200, 590, beim("t5", "Scheinvertrag"), "Bold", 34),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# N Klausurschema
# ===========================================================================================================================
REIHEN = [("kI", "I.", "Scheingeschäft: beurkundeter Vertrag nichtig", "§ 117 Abs. 1 BGB", GELB, 0),
          ("kII", "II.", "verdecktes Geschäft", "§ 117 Abs. 2 BGB", GRUEN, 0),
          ("kII1", "1.", "Form: notarielle Beurkundung", "§ 311b Abs. 1 S. 1 BGB", None, 1),
          ("kII2", "2.", "Formnichtigkeit", "§ 125 S. 1 BGB", None, 1),
          ("kII3", "3.", "Heilung durch Auflassung und Eintragung", "§ 311b Abs. 1 S. 2 BGB", None, 1),
          ("kIII", "III.", "Ergebnis: Es gilt der wahre Preis.", "", BLAU, 0)]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Klausurschema: Scheingeschäft und verdecktes Geschäft"), 110, 90, "sch", 46),
           zit("§§ 117, 125, 311b Abs. 1 BGB", 110, 150, "sch", size=30)]
y = 225
for c, r, kopf, norm, farbe, ebene in REIHEN:
    if ebene == 0:
        els_sch += [karte(110, y, 110, 70, c, fill=farbe, rund=14, schatten=5, rand=4),
                    z(r, 165 - F("ExtraBold", 38).getlength(r) / 2, y + 10, c, "ExtraBold", 38, rechts=1820),
                    z(kopf, 255, y + 10, c, "ExtraBold", 40, rechts=1280)]
        hh = 110
    else:
        els_sch += [z(r, 270, y + 4, c, "Bold", 36, rechts=1820), z(kopf, 330, y + 4, c, "Bold", 36, rechts=1280)]
        hh = 90
    if norm:
        els_sch.append(zit(norm, 1320, y + (18 if ebene == 0 else 12), c, size=30, rechts=1820))
    y += hh
assert y <= 970, y
folie([("sch", "Klausurschema"), ("kI", "Klausurschema › I. Scheingeschäft"), ("kII", "Klausurschema › II. verdecktes Geschäft"),
       ("kII1", "Klausurschema › II. 1. Form"), ("kII2", "Klausurschema › II. 2. Formnichtigkeit"),
       ("kII3", "Klausurschema › II. 3. Heilung"), ("kIII", "Klausurschema › III. Ergebnis")], els_sch)

# ===========================================================================================================================
# O Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Der Scheinvertrag", 0)], [("ist nichtig.", "a")]],
                750, 290, 42, "merke", {"a": beim("merke", "nichtig")}),
    *markertext([[("Der wahre Vertrag", 0)], [("ist formnichtig,", "b")]],
                750, 480, 42, "mk2", {"b": beim("mk2", "formnichtig")}),
    *markertext([[("bis Auflassung und", 0)], [("Eintragung ihn heilen.", "c")]],
                750, 670, 42, "mk3", {"c": beim("mk3", "heilen")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
