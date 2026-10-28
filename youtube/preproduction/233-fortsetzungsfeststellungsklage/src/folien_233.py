"""Folge 233 · Fortsetzungsfeststellungsklage § 113 I 4 VwGO – Prüfungsschema – Serienstandard Open Peeps (Katzenkönig).
Fiktiver Fall (Beispiel NRW): Samstagmittag auf dem Marktplatz, Jördis leitet eine angemeldete Demo für mehr Radwege (Schilder
ohne Parolen). Ein einzelner Teilnehmer sprüht Farbe an eine Hauswand; Polizeihauptkommissar Hinze löst die ganze Versammlung
auf. Die Demo ist vorbei, Jördis klagt zwei Wochen später. Danach: Erledigung (§ 43 Abs. 2 VwVfG, Wortlautkarte), A. Zulässigkeit
(Rechtsweg, § 113 Abs. 1 Satz 4 VwGO als Wortlautkarte, direkt/analog, Fortsetzungsfeststellungsinteresse in vier Fallgruppen,
Klagebefugnis, Vorverfahren, Frist), B. Begründetheit (§ 13 Abs. 2 Satz 1 VersG NRW als Wortlautkarte, formell, materiell,
Rechtsverletzung), Klausurtipp, Schema, Merksatz mit Lexi.
Szenen laut ../SZENENPLAN.md. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/feld/requisit/paar als
eigene Kopie aus Folge 231 (dort aus 227; gemeinsame Dateien unverändert); neu: plakat(), haus(), farbspur(), hand() mit Band.
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut nach gesetze-im-internet.de bzw. recht.nrw.de, Abruf 07.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_233/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_233/" in n:
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
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 07.10.2026 (Folge 233)), als Zitat mit Normangabe; der
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
NAME = {"JO": "Jördis", "HI": "Herr Hinze"}
NFARBE = {"JO": TUERKIS_, "HI": BLAU}
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



# --- Folge 233: Größen, Marktplatz-Bausteine ------------------------------------------------------------------------------
GROESSE = {"JO": 0.94, "HI": 1.0}            # Jördis etwas kleiner als Herr Hinze


def hh(k, h):
    return round(h * GROESSE.get(k, 1.0))


def stehend(k, x, folge, bis=None):
    els = [*fig(k, x, FB, hh(k, FR), folge, bis=bis), bis_(ns(NAME[k], x, FB, folge[0][0], NFARBE[k], d=0.1), bis)]
    return rechts_frei(els, 1200)


def hand(name, cx, unten, hoehe, b0=0.35, b1=0.60, links=True):
    """Äußerster deckender Punkt einer Figur im Höhenband b0–b1 (ausgestreckte bzw. erhobene Hand)."""
    e = peep_voll(name, cx, unten, hoehe, "_")
    a = np.asarray(e.sprite)[:, :, 3] > 40
    h_ = a.shape[0]
    band = a[int(h_ * b0):int(h_ * b1)]
    ys, xs = np.nonzero(band)
    i = xs.argmin() if links else xs.argmax()
    return e.x + xs[i], e.y + int(h_ * b0) + ys[i]


def plakat(text, cx, oben, unten, cue, bis=None, fill=WEISS, size=30):
    """Demo-Schild ohne Parole: weiße Tafel mit Tuschekontur auf einem Holzstiel (programmatisch, Palette)."""
    f = F("ExtraBold", size)
    b = f.getbbox(glyphen(text))
    w, h = b[2] - b[0] + 44, size + 34
    H_ = unten - oben
    s = 2
    im = Image.new("RGBA", (w * s, H_ * s))
    dr = ImageDraw.Draw(im)
    dr.rounded_rectangle(((w / 2 - 6) * s, h * s, (w / 2 + 6) * s, H_ * s), 4 * s, fill=INK)
    dr.rounded_rectangle(((w / 2 - 3) * s, h * s, (w / 2 + 3) * s, (H_ - 3) * s), 2 * s, fill=HOLZ)
    dr.rounded_rectangle((0, 0, w * s, h * s), 10 * s, fill=INK)
    dr.rounded_rectangle((5 * s, 5 * s, (w - 5) * s, (h - 5) * s), 7 * s, fill=fill)
    im = im.resize((w, H_), Image.LANCZOS)
    ImageDraw.Draw(im).text((22 - b[0], (h - (b[3] - b[1])) / 2 - b[1]), text, font=f, fill=INK)
    return El(im, cx - w / 2, oben, cue, "cut", 0.0, bis, name="plakat:" + text)


HAUSFARBE = (246, 222, 190, 255)


def haus(cue, x0=60, x1=470, oben=250):
    """Hausfassade am Marktplatz (programmatisch): Fläche, Fenster, Tür, Dachkante."""
    w, h = x1 - x0, BODEN - oben
    s = 2
    im = Image.new("RGBA", ((w + 12) * s, (h + 40) * s))
    dr = ImageDraw.Draw(im)
    o = 6 * s
    dr.polygon([(o, 40 * s), ((w / 2 + 6) * s, 0), ((w + 6) * s, 40 * s)], fill=INK)
    dr.polygon([(o + 10 * s, 37 * s), ((w / 2 + 6) * s, 6 * s), ((w + 6) * s - 10 * s, 37 * s)], fill=ROT)
    dr.rectangle((o, 40 * s, o + w * s, (h + 40) * s), fill=INK)
    dr.rectangle((o + 5 * s, 45 * s, o + (w - 5) * s, (h + 40) * s), fill=HAUSFARBE)
    for fx in (40, w - 130):
        for fy in (80, 230):
            dr.rounded_rectangle((o + fx * s, fy * s, o + (fx + 90) * s, (fy + 100) * s), 6 * s, fill=INK)
            dr.rounded_rectangle((o + (fx + 5) * s, (fy + 5) * s, o + (fx + 85) * s, (fy + 95) * s), 4 * s, fill=BLAUHELL)
    tx = w / 2 - 50
    dr.rounded_rectangle((o + tx * s, (h - 130) * s, o + (tx + 100) * s, (h + 40) * s), 8 * s, fill=INK)
    dr.rounded_rectangle((o + (tx + 5) * s, (h - 125) * s, o + (tx + 95) * s, (h + 40) * s), 6 * s, fill=HOLZ)
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    return El(im, x0 - 6, oben - 40, cue, "cut", 0.0, None, name="haus")


def farbspur(cue, bis=None):
    """Sichtbare Farbe an der Hauswand (rote Schlieren, kein Schriftzug)."""
    pts = [(330, 600), (360, 575), (390, 610), (420, 580), (450, 620), (430, 650), (380, 640), (340, 668)]
    return linienzug(pts, cue, breite=13, farbe=ROT)


# ===========================================================================================================================
# A1 Fall: Samstagmittag auf dem Marktplatz – Demo für mehr Radwege, Farbe an der Wand, Auflösung, Demo vorbei
# ===========================================================================================================================
FH_ = 440
SPX, JOX, ALX, RAX, HIX = 600, 860, 1060, 1340, 1770
RAH = 340                                    # Radfahrerin (sitzend auf dem Rad)
NULL = ("fall", -round(T_("fall"), 3))
WEGG = beim("vorbei", "gehen"), beim("vorbei", "Hause", ende=True)   # die Teilnehmenden gehen nach Hause
sp_hand = hand("SP_ruhig", SPX, BODEN, FH_, 0.15, 0.42, links=True)
jo_hand = hand("JO_froh", JOX, BODEN, hh("JO", FH_), 0.40, 0.62, links=True)
al_hand = hand("AL_froh", ALX, BODEN, 420, 0.40, 0.62, links=True)
SPRUEHT = beim("farbe", "sprüht")
dose = ficon("tabler", "spray", sp_hand[0] - 10, sp_hand[1] + 40, 70, SPRUEHT, fuell=GRUEN, bis="hinze")
szene(dose, "233spray*", 0.5, 0.0)                    # Sprühstoß, wenn die Dose in der Hand erscheint
weg_ra = bewegt(peep_voll("RA_sorge_r", RAX + 100, BODEN, RAH, WEGG[0], anim="cut", bis=WEGG[1]), WEGG[0], WEGG[1], -100)
szene(weg_ra, "233schritte*", 0.55, 0.0)              # Schritte, solange die Teilnehmenden sichtbar weggehen
FALL_PFADE = [(NULL, "Fall · Samstagmittag auf dem Marktplatz"), ("joerdis", "Fall · Demo für mehr Radwege"),
              ("farbe", "Fall · Farbe an der Hauswand"), ("hinze", "Fall · Die Polizei greift ein"),
              ("hi1", "Fall · Die Auflösung"), ("vorbei", "Fall · Die Demo ist vorbei"),
              ("naechst", "Fall · Die nächste Demo")]
folie(FALL_PFADE, [
    hart(boden(NULL)),
    hart(haus(NULL)),
    hart(ficon("tabler", "sun", 1830, 150, 96, NULL, fuell=GELB, anim="cut")),
    hart(pl("Samstagmittag auf dem Marktplatz", 560, 30, NULL, fill=GELB, size=32)),
    # Demo: Schilder ohne Parolen, Teilnehmende als Open Peeps
    plakat("Mehr Radwege", JOX - 40, 330, 690, NULL),                          # Stiel hinter dem Körper: Jördis hält das Schild
    *fig("JO", JOX, BODEN, hh("JO", FH_), [(NULL, "froh"), ("farbe", "schreck"), (beim("farbe", "obwohl"), "sorge"),
                                            ("hinze", "sorge_r")], bis="jo1", erst="cut"),
    *redet("JO_ruft_r", JOX, BODEN, hh("JO", FH_), "jo1", "vorbei"),
    *fig("JO", JOX, BODEN, hh("JO", FH_), [("vorbei", "muede_r"), ("naechst", "entschl_r")], erst="cut"),
    ns(NAME["JO"], JOX, BODEN, NULL, NFARBE["JO"], anim="cut"),
    *fig("AL", ALX, BODEN, 420, [(NULL, "froh"), ("hi1", "sorge")], bis=WEGG[0], erst="cut"),
    bewegt(peep_voll("AL_sorge_r", ALX + 80, BODEN, 420, WEGG[0], anim="cut", bis=WEGG[1]), WEGG[0], WEGG[1], -80),
    *fig("RA", RAX, BODEN, RAH, [(NULL, "froh"), ("hi1", "sorge")], bis=WEGG[0], erst="cut"),
    weg_ra,
    *fig("SP", SPX, BODEN, FH_, [(NULL, "ruhig"), ("hinze", "denkt")], bis=WEGG[0], erst="cut"),
    bewegt(peep_voll("SP_denkt", SPX - 140, BODEN, FH_, WEGG[0], anim="cut", bis=WEGG[1]), WEGG[0], WEGG[1], 140),
    pl("Demo für mehr Radwege, angemeldet", 70, 94, beim("joerdis", "Demo"), fill=WEISS, size=30, bis="farbe"),
    # Farbe an der Hauswand
    dose,
    farbspur(beim("farbe", "Farbe")),
    pl("Ein einzelner Teilnehmer sprüht Farbe", 560, 94, beim("farbe", "einzelner"), fill=HELLROT, size=30, bis="hi1"),
    pl("Jördis bittet ihn aufzuhören.", 560, 158, beim("farbe", "obwohl"), fill=WEISS, size=30, bis="hinze"),
    # Herr Hinze: greift ein, löst auf
    *fig("HI", HIX, BODEN, FH_, [("hinze", "ernst")], bis="hi1"),
    *redet("HI_spricht", HIX, BODEN, FH_, "hi1", "jo1"),
    *fig("HI", HIX, BODEN, FH_, [("jo1", "streng"), ("vorbei", "ruhig"), ("naechst", "ernst")], erst="cut"),
    ns(NAME["HI"], HIX, BODEN, "hinze", NFARBE["HI"], d=0.1),
    pl("Polizeihauptkommissar Hinze", 560, 158, beim("hinze", "Polizeihauptkommissar"), fill=BLAU, size=30, bis="hi1"),
    blase("sprech", 640, 240, "hi1", 1400, 200, inhalt=["Wegen der Farbe an der Wand:", "Die Versammlung ist aufgelöst.",
                                                        "Bitte verlassen Sie den Platz."], textsize=30,
          figur=("HI_spricht", HIX, BODEN, FH_), bis="jo1"),
    ficon("tabler", "ban", 1420, 420, 70, beim("hi1", "aufgelöst"), fuell=HELLROT, bis="jo1"),
    blase("sprech", 520, 170, "jo1", 1250, 190, inhalt=["Aber wir anderen", "sind doch friedlich!"], textsize=32,
          figur=("JO_ruft_r", JOX, BODEN, hh("JO", FH_)), bis="vorbei"),
    # Die Demo ist vorbei; die nächste ist geplant
    pl("Alle gehen nach Hause: Die Demo ist vorbei.", 560, 94, beim("vorbei", "Die", 2), fill=GELB, size=30, bis="naechst"),
    ficon("tabler", "calendar-event", 1180, 560, 110, "naechst", fuell=GELB),
    pl("nächste Demo: selber Ort", 1180, 580, beim("naechst", "nächste"), fill=GELB, size=28, anker="m"),
    ficon("tabler", "repeat", 1520, 560, 100, beim("naechst", "Polizei"), fuell=BLAUHELL),
    pl("Polizei: würde wieder so handeln", 1440, 650, beim("naechst", "würde"), fill=BLAUHELL, size=28, anker="m"),
])

# ===========================================================================================================================
# A2 Die Klage beim Verwaltungsgericht
# ===========================================================================================================================
folie([("klage", "Fall · Die Klage")], [
    hart(boden("klage")),
    ficon("fluent-emoji-high-contrast", "classical-building", 560, BODEN, 520, "klage", fuell=WEISS),
    pl("Verwaltungsgericht", 560, 250, "klage", fill=WEISS, size=32, anker="m"),
    pl("2 Wochen später: Jördis klagt.", 70, 30, beim("klage", "Zwei"), fill=GELB, size=32),
    ficon("tabler", "file-text", 1160, 640, 110, beim("klage", "klagt"), fuell=WEISS),
    pl("Klage", 1160, 680, beim("klage", "klagt"), fill=WEISS, size=28, anker="m"),
    *fig("JO", 1450, BODEN, hh("JO", FH_), [("klage", "entschl")]),
    ns(NAME["JO"], 1450, BODEN, "klage", NFARBE["JO"], d=0.1),
])

# ===========================================================================================================================
# A3 Die Frage
# ===========================================================================================================================
folie([("frage", "Die Frage · Klage gegen eine vergangene Auflösung?"), ("frage2", "Die Frage · Fortsetzungsfeststellungsklage")], [
    *tafel("frage", "Die Frage"),
    z("Kann man gegen eine Auflösung klagen,", 110, 190, "frage", "Bold", 38),
    z("die längst vorbei ist?", 110, 244, "frage", "Bold", 38),
    blk(110, 340, 1040, 140, GELB, "frage2", [("Prüfungsschema der", "ExtraBold", 37, INK),
                                             ("Fortsetzungsfeststellungsklage", "ExtraBold", 37, INK)]),
    z("Beispiel: Nordrhein-Westfalen", 110, 510, beim("frage2", "Nordrhein"), "Bold", 34),
    z("in deinem Land ggf. andere Nummern", 110, 560, beim("frage2", "Nordrhein"), size=30, farbe=TEXT),
    *requisit([("frage", ("tabler", "hourglass", 110, GELB), "längst vorbei", GELB),
               ("frage2", ("fluent-emoji-high-contrast", "classical-building", 130, WEISS), "§ 113 Abs. 1 Satz 4 VwGO", WEISS)]),
    *paar("JO", [("frage", "denkt"), ("frage2", "entschl")], "HI", [("frage", "ruhig")]),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_233(cue, absaetze, frage):
    els = [karte(140, 50, 1640, 930, cue, fill=HELL), titel("Sachverhalt", 210, 84, cue, 56)]
    y = 180
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=38, zeilenabstand=1.32)
        els += e; y += 12
    assert y + 66 <= 975, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=34))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_233("sv", [
    "Samstagmittag auf dem Marktplatz einer Stadt in Nordrhein-Westfalen: Jördis leitet eine ordnungsgemäß angezeigte "
    "Demonstration für mehr Radwege mit rund 40 Menschen. Alle sind friedlich, bis ein einzelner Teilnehmer Farbe an eine "
    "Hauswand sprüht. Jördis bittet ihn aufzuhören, er macht weiter.",
    "Polizeihauptkommissar Hinze von der Kreispolizeibehörde löst daraufhin die ganze Versammlung auf: „Wegen der Farbe an "
    "der Wand: Die Versammlung ist aufgelöst.“ Andere Maßnahmen ergreift er nicht. Alle gehen nach Hause.",
    "Jördis plant weitere Demos am selben Ort; die Polizei erklärt, sie würde wieder so handeln. Weitere Folgen hat die "
    "Auflösung nicht. 2 Wochen später erhebt Jördis Klage beim Verwaltungsgericht.",
], "Hat die Klage Erfolg?")

# ===========================================================================================================================
# C Ausgangslage: Erledigung, § 43 Abs. 2 VwVfG (Wortlautkarte)
# ===========================================================================================================================
PE = "Ausgangslage · Erledigung"
w43, w43_y = wortlaut(80, 330, 1100,
                      "„(2) Ein Verwaltungsakt bleibt wirksam, solange und soweit er nicht zurückgenommen, widerrufen, "
                      "anderweitig aufgehoben oder durch Zeitablauf oder auf andere Weise erledigt ist.“",
                      "§ 43 Abs. 2 VwVfG (NRW: § 43 Abs. 2 VwVfG NRW, gleichlautend)", "wl43",
                      marken=[("aufgehoben", beim("wl43", "aufgehoben")), ("erledigt", beim("wl43", "erledigt"))], size=32)
folie([("va", f"{PE} › Auflösung = Verwaltungsakt"), ("wl43", f"{PE} › § 43 Abs. 2 VwVfG"),
       ("erl", f"{PE} › Die Auflösung hat sich erledigt"), ("leer", f"{PE} › Anfechtungsklage geht ins Leere")], [
    *tafel("va", "Ausgangslage: Erledigung"),
    *okz("Die Auflösung ist ein Verwaltungsakt:", 180, "va", "Bold", 34),
    z("Sie beendet die Versammlung, alle müssen gehen.", 185, 228, beim("va", "beendet"), size=32),
    zit("§ 35 VwVfG NRW; § 13 Abs. 2 Satz 3 VersG NRW", 185, 272, beim("va", "beendet")),
    *w43,
    blk(110, w43_y + 30, 1040, 90, GELB, "erl", [("Demo vorbei: Die Auflösung hat sich erledigt.", "ExtraBold", 33, INK)]),
    *neinz("Anfechtungsklage geht ins Leere", w43_y + 160, "leer", "Bold", 34),
    *requisit([("va", ("tabler", "speakerphone", 110, BLAU), "Auflösung", BLAU),
               ("erl", ("tabler", "hourglass", 110, GELB), "erledigt", GELB),
               ("leer", ("tabler", "ban", 100, HELLROT), "geht ins Leere", HELLROT)]),
    *paar("JO", [("va", "ernst"), ("erl", "denkt"), ("leer", "sorge")], "HI", [("va", "ernst"), ("erl", "ruhig")]),
])
assert w43_y + 220 <= 900, w43_y

# ===========================================================================================================================
# D1 A. Zulässigkeit: I. Rechtsweg, II. statthafte Klageart – § 113 Abs. 1 Satz 4 VwGO (Wortlautkarte)
# ===========================================================================================================================
PZ = "A. Zulässigkeit"
w113, w113_y = wortlaut(80, 330, 1100,
                        "„… Hat sich der Verwaltungsakt vorher durch Zurücknahme oder anders erledigt, so spricht das Gericht "
                        "auf Antrag durch Urteil aus, daß der Verwaltungsakt rechtswidrig gewesen ist, wenn der Kläger ein "
                        "berechtigtes Interesse an dieser Feststellung hat.“", "§ 113 Abs. 1 Satz 4 VwGO", "wl113",
                        marken=[("erledigt", beim("wl113", "erledigt")), ("rechtswidrig gewesen", beim("wl113", "rechtswidrig")),
                                ("berechtigtes Interesse", beim("wl113", "berechtigtes"))], size=32)
folie([("rweg", f"{PZ} › I. Verwaltungsrechtsweg, § 40 Abs. 1 Satz 1 VwGO"),
       ("wl113", f"{PZ} › II. Statthafte Klageart, § 113 Abs. 1 Satz 4 VwGO")], [
    *tafel("rweg", "A. Zulässigkeit"),
    *okz("I. Verwaltungsrechtsweg: Versammlungsrecht", 180, beim("rweg", "Erstens"), "Bold", 34),
    z("ist öffentliches Recht.", 185, 228, beim("rweg", "öffentliches"), size=32),
    zit("§ 40 Abs. 1 Satz 1 VwGO", 600, 236, beim("rweg", "öffentliches")),
    z("II. Statthafte Klageart", 110, 280, "wl113", "ExtraBold", 36),
    *w113,
    *requisit([("rweg", ("fluent-emoji-high-contrast", "classical-building", 130, WEISS), "Verwaltungsgericht", WEISS),
               ("wl113", ("tabler", "file-text", 100, WEISS), "§ 113 Abs. 1 Satz 4", WEISS)]),
    *paar("JO", [("rweg", "ruhig"), ("wl113", "denkt")], "HI", [("rweg", "ruhig")]),
])
assert w113_y <= 900, w113_y

# ===========================================================================================================================
# D2 II. direkt oder entsprechend? Streit; Verpflichtungssituation
# ===========================================================================================================================
PS2 = f"{PZ} › II. Statthafte Klageart"
folie([("direkt", f"{PS2} › nach Klageerhebung erledigt: direkt"),
       ("analog", f"{PS2} › vor Klageerhebung erledigt: entsprechend"),
       ("streit", f"{PS2} › a. A.: Feststellungsklage, § 43 VwGO"),
       ("verpfl", f"{PS2} › Verpflichtungssituation: entsprechend")], [
    *tafel("direkt", "II. Direkt oder entsprechend?"),
    blk(110, 175, 1040, 100, BLAUHELL, "direkt", [("Erledigung nach Klageerhebung:", "Bold", 32, INK),
                                                ("§ 113 Abs. 1 Satz 4 VwGO direkt", "ExtraBold", 32, INK)]),
    blk(110, 300, 1040, 100, GELB, "analog", [("Erledigung vor Klageerhebung (Jördis):", "Bold", 32, INK),
                                            ("§ 113 Abs. 1 Satz 4 VwGO entsprechend", "ExtraBold", 32, INK)]),
    zit("BVerwG, Urt. v. 24.4.2024 – 6 C 2.22, Rn. 15; OVG NRW, Urt. v. 7.12.2021", 110, 412, beim("analog", "Rechtsprechung")),
    zit("– 5 A 2000/20, Rn. 25 f. (mit BVerwG 1 C 12.88, 2 B 81.84)", 110, 446, beim("analog", "Rechtsprechung")),
    blk(110, 510, 1040, 100, LILAHELL, "streit", [("a. A. (Teil der Literatur):", "Bold", 32, INK),
                                                ("allgemeine Feststellungsklage, § 43 VwGO", "Regular", 32, INK)]),
    zit("vgl. BayVGH, Urt. v. 10.7.2018 – 10 BV 17.2405, Rn. 20", 110, 622, "streit"),
    blk(110, 690, 1040, 100, HELLGRUEN, "verpfl", [("Verpflichtungsbegehren erledigt:", "Bold", 32, INK),
                                                 ("§ 113 Abs. 1 Satz 4 VwGO entsprechend", "ExtraBold", 32, INK)]),
    zit("BVerwG, Urt. v. 4.12.2014 – 4 C 33.13, Rn. 13", 110, 802, "verpfl"),
    *requisit([("direkt", ("tabler", "file-text", 100, BLAUHELL), "erst Klage, dann erledigt", BLAUHELL),
               ("analog", ("tabler", "hourglass", 110, GELB), "erst erledigt, dann Klage", GELB),
               ("streit", ("tabler", "arrows-split", 110, LILAHELL), "Streit", LILAHELL),
               ("verpfl", ("tabler", "certificate", 110, HELLGRUEN), "Verpflichtung", HELLGRUEN)]),
    *stehend("JO", FX, [("direkt", "ruhig"), ("analog", "denkt"), ("streit", "ernst"), ("verpfl", "froh")]),
])

# ===========================================================================================================================
# E1 III. Fortsetzungsfeststellungsinteresse: Maßstab, 1. Wiederholungsgefahr
# ===========================================================================================================================
PF = f"{PZ} › III. Fortsetzungsfeststellungsinteresse"
folie([("ffi", PF), ("fg", f"{PF} › 4 Fallgruppen"), ("wh", f"{PF} › 1. Wiederholungsgefahr"),
       ("wh2", f"{PF} › 1. Wiederholungsgefahr (+)")], [
    *tafel("ffi", "III. Fortsetzungsfeststellungsinteresse", size=42),
    z("Das Urteil muss die Lage der Klägerin", 110, 180, beim("ffi", "Urteil"), "Bold", 34),
    z("rechtlich, wirtschaftlich oder ideell verbessern können.", 110, 228, beim("ffi", "rechtlich"), size=32),
    zit("BVerwG, Urt. v. 16.5.2013 – 8 C 14.12, BVerwGE 146, 303, Rn. 20", 110, 274, beim("ffi", "rechtlich")),
    blk(110, 330, 1040, 80, WEISS, "fg", [("4 Fallgruppen", "ExtraBold", 34, INK)]),
    z("1. Wiederholungsgefahr", 110, 450, "wh", "ExtraBold", 36),
    z("konkret droht ein gleichartiger Verwaltungsakt", 150, 502, beim("wh", "konkret"), size=32),
    z("unter im Wesentlichen gleichen Umständen", 150, 548, beim("wh", "unter"), size=32),
    zit("8 C 14.12, Rn. 21; Versammlung: BVerfG, Beschl. v. 3.3.2004 – 1 BvR 461/03,", 150, 594, beim("wh", "unter")),
    zit("BVerfGE 110, 77, Rn. 41–43", 150, 628, beim("wh", "unter")),
    *plusminus("Jördis: nächste Demo geplant, Polizei bleibt dabei", 150, 690, "wh2", True, size=32, stil="Bold"),
    *requisit([("ffi", ("tabler", "scale", 120, WEISS), "berechtigtes Interesse", WEISS),
               ("wh", ("tabler", "repeat", 110, GELB), "Wiederholungsgefahr", GELB),
               ("wh2", ("tabler", "calendar-event", 110, HELLGRUEN), "nächste Demo", HELLGRUEN)]),
    *stehend("JO", FX, [("ffi", "ruhig"), ("wh", "denkt"), ("wh2", "entschl")]),
])

# ===========================================================================================================================
# E2 2. Rehabilitation, 3. Präjudizinteresse
# ===========================================================================================================================
folie([("reha", f"{PF} › 2. Rehabilitation"), ("reha2", f"{PF} › 2. Rehabilitation (−)"),
       ("praej", f"{PF} › 3. Präjudizinteresse"), ("praej2", f"{PF} › 3. Präjudiz nur nach Klageerhebung"),
       ("praej3", f"{PF} › 3. Präjudizinteresse (−)")], [
    *tafel("reha", "III. Fortsetzungsfeststellungsinteresse", size=42),
    z("2. Rehabilitation", 110, 170, "reha", "ExtraBold", 36),
    z("die Maßnahme stempelt ab: nach außen sichtbar,", 150, 222, beim("reha", "stempelt"), size=32),
    z("und die Wirkung dauert an", 150, 268, beim("reha", "bis"), size=32),
    zit("8 C 14.12, Rn. 25; BVerwG 6 C 2.22, Rn. 18", 150, 312, beim("reha", "bis")),
    *plusminus("kein ehrenrühriger Vorwurf an Jördis", 150, 362, "reha2", False, size=32, stil="Bold"),
    z("3. Präjudizinteresse", 110, 450, "praej", "ExtraBold", 36),
    z("Vorbereitung eines Amtshaftungsprozesses,", 150, 502, beim("praej", "Urteil"), size=32),
    z("der nicht offensichtlich aussichtslos ist", 150, 548, beim("praej", "nicht"), size=32),
    zit("8 C 14.12, Rn. 44", 150, 592, beim("praej", "nicht")),
    blk(150, 640, 1000, 120, HELLROT, "praej2", [("nur bei Erledigung nach Klageerhebung:", "ExtraBold", 32, INK),
                                               ("Mühe des Prozesses nicht umsonst", "Regular", 32, INK)]),
    zit("OVG NRW, Urt. v. 7.12.2021 – 5 A 2000/20, Rn. 68; BVerwG 2 C 27.15, Rn. 15", 150, 772, beim("praej2", "Mühe")),
    *plusminus("Jördis: vor der Klage erledigt", 150, 822, "praej3", False, size=32, stil="Bold"),
    *requisit([("reha", ("tabler", "user-x", 110, HELLROT), "Rehabilitation", HELLROT),
               ("praej", ("tabler", "coin", 110, GELB), "Amtshaftung", GELB),
               ("praej3", ("tabler", "hourglass", 110, HELLROT), "vor der Klage erledigt", HELLROT)]),
    *stehend("JO", FX, [("reha", "ruhig"), ("reha2", "froh"), ("praej", "denkt"), ("praej3", "ernst")]),
])

# ===========================================================================================================================
# E3 4. Tiefgreifender Grundrechtseingriff (BVerwG 6 C 2.22; BVerfGE 110, 77)
# ===========================================================================================================================
folie([("tief", f"{PF} › 4. Tiefgreifender Grundrechtseingriff"), ("tief2", f"{PF} › 4. kurze Dauer und gewichtiger Eingriff"),
       ("tief3", f"{PF} › 4. Auflösung: schwerste Beeinträchtigung"), ("tief4", f"{PF} › 4. Tiefgreifender Grundrechtseingriff (+)")], [
    *tafel("tief", "III. Fortsetzungsfeststellungsinteresse", size=42),
    z("4. Tiefgreifender Grundrechtseingriff", 110, 170, "tief", "ExtraBold", 36),
    z("Maßnahme erledigt sich typischerweise, bevor ein", 150, 222, beim("tief", "Maßnahmen"), size=32),
    z("Gericht in der Hauptsache entscheiden kann", 150, 268, beim("tief", "Gericht"), size=32),
    blk(150, 330, 1000, 120, GELB, "tief2", [("BVerwG 2024: beides muss vorliegen,", "ExtraBold", 32, INK),
                                            ("kurze Dauer und gewichtiger Eingriff", "Regular", 32, INK)]),
    zit("BVerwG, Urt. v. 24.4.2024 – 6 C 2.22, Rn. 21 f.", 150, 462, beim("tief2", "Beides")),
    *okz("Auflösung: schwerste Beeinträchtigung", 520, "tief3", "Bold", 33, x=195),
    z("der Versammlungsfreiheit", 195, 566, beim("tief3", "Versammlungsfreiheit"), size=32),
    zit("BVerfG, Beschl. v. 3.3.2004 – 1 BvR 461/03, BVerfGE 110, 77, Rn. 37", 195, 610, beim("tief3", "Versammlungsfreiheit")),
    *okz("endet mit der Demo", 660, beim("tief3", "Und"), "Bold", 33, x=195),
    blk(110, 740, 1040, 90, HELLGRUEN, "tief4", [("Fortsetzungsfeststellungsinteresse (+)", "ExtraBold", 34, INK)]),
    *requisit([("tief", ("tabler", "clock-hour-4", 110, WEISS), "schnell erledigt", WEISS),
               ("tief2", ("tabler", "scale", 120, GELB), "beides nötig", GELB),
               ("tief3", ("tabler", "users-group", 120, HELLGRUEN), "Art. 8 GG", HELLGRUEN)]),
    *stehend("JO", FX, [("tief", "ruhig"), ("tief2", "denkt"), ("tief3", "ernst"), ("tief4", "froh")]),
])

# ===========================================================================================================================
# F IV.–VII. Klagebefugnis, Vorverfahren, Frist, übrige Voraussetzungen
# ===========================================================================================================================
folie([("kb", f"{PZ} › IV. Klagebefugnis, § 42 Abs. 2 VwGO analog"), ("vv", f"{PZ} › V. Vorverfahren: NRW, § 110 JustG NRW"),
       ("frist", f"{PZ} › VI. Frist"), ("frist2", f"{PZ} › VI. Frist › a. A. Teil der Literatur"),
       ("frist3", f"{PZ} › VI. Frist › 2 Wochen"), ("rest", f"{PZ} › VII. Übrige Voraussetzungen"),
       ("zul", f"{PZ} › Ergebnis: zulässig")], [
    *tafel("kb", "A. Zulässigkeit: IV. bis VII."),
    *okz("IV. Klagebefugnis, § 42 Abs. 2 VwGO analog:", 170, "kb", "Bold", 32),
    z("Art. 8 GG kann verletzt sein (Leiterin der Demo)", 185, 214, beim("kb", "Leiterin"), size=31),
    *okz("V. Vorverfahren: entfällt in NRW", 286, "vv", "Bold", 32),
    z("§ 110 Abs. 1 Satz 1 JustG NRW; in deinem Land ggf. anders", 185, 330, beim("vv", "Paragraf"), size=28, farbe=TEXT),
    z("VI. Frist: § 74 VwGO gilt nicht, wenn sich der VA vor", 185, 400, "frist", "Bold", 32),
    z("der Klage und innerhalb der Frist erledigt hat", 185, 444, beim("frist", "gilt"), size=31),
    zit("BayVGH, Urt. v. 10.7.2018 – 10 BV 17.2405, Rn. 21 f.; vgl. BVerwG,", 185, 488, beim("frist", "Rechtsprechung")),
    zit("Urt. v. 14.7.1999 – 6 C 7.98 (zitiert nach BayVGH)", 185, 522, beim("frist", "Rechtsprechung")),
    z("a. A. Teil der Literatur", 185, 570, "frist2", size=31, farbe=TEXT),
    *okz("2 Wochen: unproblematisch", 626, "frist3", "Bold", 32),
    z("VII. Übrige Voraussetzungen: wie bei der Anfechtungsklage", 185, 690, "rest", "Bold", 31),
    blk(110, 760, 1040, 90, HELLGRUEN, "zul", [("Die Klage ist zulässig.", "ExtraBold", 34, INK)]),
    *requisit([("kb", ("tabler", "users-group", 120, WEISS), "Art. 8 GG", WEISS),
               ("vv", ("tabler", "file-text", 100, WEISS), "kein Widerspruch", WEISS),
               ("frist", ("tabler", "calendar-time", 110, GELB), "Frist?", GELB),
               ("zul", ("tabler", "circle-check", 110, HELLGRUEN), "zulässig", HELLGRUEN)]),
    *paar("JO", [("kb", "ernst"), ("frist", "denkt"), ("zul", "froh")], "HI", [("kb", "ruhig"), ("zul", "denkt")]),
])

# ===========================================================================================================================
# G1 B. Begründetheit: Ermächtigungsgrundlage (Wortlautkarte § 13 Abs. 2 Satz 1 VersG NRW), formell
# ===========================================================================================================================
PB = "B. Begründetheit"
w13, w13_y = wortlaut(80, 350, 1100,
                      "„(2) Die zuständige Behörde kann eine Versammlung verbieten oder auflösen, wenn ihre Durchführung die "
                      "öffentliche Sicherheit unmittelbar gefährdet und die Gefahr nicht anders abgewehrt werden kann. …“",
                      "§ 13 Abs. 2 Satz 1 VersG NRW", "egl",
                      marken=[("auflösen,", beim("egl2", "Auflösen")), ("unmittelbar", beim("egl2", "unmittelbar")),
                              ("nicht anders", beim("egl2", "nicht"))], size=32)
folie([("begr", f"{PB}, § 113 Abs. 1 Satz 4 VwGO analog"),
       ("egl", f"{PB} › I. Rechtswidrigkeit › 1. Ermächtigungsgrundlage, § 13 Abs. 2 VersG NRW"),
       ("bund", f"{PB} › I. 1. ohne Landesgesetz: § 15 Abs. 3 VersG"),
       ("formell", f"{PB} › I. Rechtswidrigkeit › 2. formell")], [
    *tafel("begr", "B. Begründetheit"),
    z("begründet, wenn die Auflösung rechtswidrig war", 110, 170, beim("begr", "Die"), "Bold", 34),
    z("und Jördis in ihren Rechten verletzt hat", 110, 218, beim("begr", "und"), "Bold", 34),
    z("I. 1. Ermächtigungsgrundlage (Beispiel NRW)", 110, 288, "egl", "ExtraBold", 34),
    *w13,
    z("Land ohne eigenes Gesetz: § 15 Abs. 3 VersG (Bund)", 110, w13_y + 20, "bund", "Bold", 31),
    *okz("2. formell: Kreispolizeibehörde zuständig,", w13_y + 84, "formell", "Bold", 32),
    z("Grund genannt", 185, w13_y + 128, beim("formell", "Herr"), size=31),
    zit("§ 32, § 13 Abs. 4 Satz 2 VersG NRW", 420, w13_y + 136, beim("formell", "Herr")),
    *requisit([("begr", ("fluent-emoji-high-contrast", "balance-scale", 130, WEISS), "rechtswidrig?", WEISS),
               ("egl", ("tabler", "book", 110, WEISS), "VersG NRW", WEISS),
               ("bund", ("tabler", "book", 110, BLAUHELL), "VersG (Bund)", BLAUHELL),
               ("formell", ("tabler", "speakerphone", 110, BLAU), "Grund genannt", BLAU)]),
    *paar("JO", [("begr", "ernst"), ("egl", "denkt")], "HI", [("begr", "ruhig"), ("formell", "ernst")]),
])
assert w13_y + 180 <= 900, w13_y

# ===========================================================================================================================
# G2 3. materiell: Gefahr ja, aber milderes Mittel; Brokdorf (nur verwiesen); Rechtsverletzung; Ergebnis
# ===========================================================================================================================
folie([("mat", f"{PB} › I. Rechtswidrigkeit › 3. materiell: Gefahr"),
       ("mild", f"{PB} › I. 3. nicht anders abwehrbar? (−)"), ("brok", f"{PB} › I. 3. Brokdorf: Friedliche geschützt"),
       ("rw", f"{PB} › I. Auflösung rechtswidrig"), ("rv", f"{PB} › II. Rechtsverletzung, Art. 8 GG"),
       ("erg", "Ergebnis · zulässig und begründet")], [
    *tafel("mat", "I. 3. Materielle Rechtmäßigkeit", size=44),
    *okz("Farbe an der Wand: Sachbeschädigung,", 170, "mat", "Bold", 33),
    z("die öffentliche Sicherheit ist gefährdet", 185, 216, beim("mat", "öffentliche"), size=32),
    zit("§ 303 Abs. 2 StGB; BVerfGE 69, 315 (Brokdorf), Rn. 77", 185, 260, beim("mat", "öffentliche")),
    *neinz("aber die Gefahr ging von einem Einzelnen aus:", 316, "mild", "Bold", 33, kreuz=beim("mild", "ausschließen")),
    z("Ausschluss möglich, § 14 Abs. 3 VersG NRW", 185, 362, beim("mild", "ausschließen"), size=32),
    blk(110, 430, 1040, 120, LILAHELL, "brok", [("Friedliche bleiben geschützt, wenn", "ExtraBold", 32, INK),
                                             ("Einzelne Ausschreitungen begehen", "ExtraBold", 32, INK)]),
    zit("BVerfGE 69, 315 (Brokdorf), Rn. 92 – mehr im Video zum Brokdorf-Beschluss", 110, 562, beim("brok", "Mehr")),
    *neinz("Auflösung rechtswidrig", 620, "rw", "ExtraBold", 34),
    *okz("II. verletzte Jördis in Art. 8 Abs. 1 GG", 680, "rv", "Bold", 33),
    blk(110, 760, 1040, 90, HELLGRUEN, "erg", [("Die Klage ist zulässig und begründet.", "ExtraBold", 34, INK)]),
    *requisit([("mat", ("tabler", "spray", 90, GRUEN), "Sachbeschädigung", WEISS),
               ("mild", ("tabler", "user-minus", 110, GELB), "Ausschluss", GELB),
               ("brok", ("tabler", "users-group", 120, LILAHELL), "Friedliche geschützt", LILAHELL),
               ("rw", ("fluent-emoji-high-contrast", "balance-scale", 130, HELLROT), "rechtswidrig", HELLROT),
               ("erg", ("tabler", "circle-check", 110, HELLGRUEN), "Erfolg", HELLGRUEN)]),
    *paar("JO", [("mat", "ernst"), ("mild", "denkt"), ("brok", "entschl"), ("erg", "froh")], "HI",
          [("mat", "ernst"), ("mild", "denkt"), ("rw", "streng")]),
])

# ===========================================================================================================================
# H Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Zeitpunkt der Erledigung zuerst"), ("tipp1", "Klausurtipp › direkt oder entsprechend"),
       ("tipp2", "Klausurtipp › Präjudizinteresse möglich?"), ("tipp3", "Klausurtipp › Frist?"),
       ("tipp4", "Klausurtipp › Begründetheit in der Vergangenheit")], [
    *tafel("tipp", "Klausurtipp: Wann erledigt?", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Zeitpunkt der Erledigung an den Anfang:", 200, 200, "tipp", "ExtraBold", 35),
    z("vor oder nach der Klageerhebung?", 240, 252, beim("tipp", "Anfang"), size=34),
    linienzug([(130, 320), (1130, 320)], "tipp1", breite=3),
    z("Er entscheidet:", 200, 344, "tipp1", "ExtraBold", 34),
    z("1. § 113 Abs. 1 Satz 4 direkt oder entsprechend?", 240, 400, beim("tipp1", "Paragraf"), size=33),
    z("2. Präjudizinteresse möglich?", 240, 454, "tipp2", size=33),
    z("3. Läuft eine Frist?", 240, 508, "tipp3", size=33),
    linienzug([(130, 576), (1130, 576)], "tipp4", breite=3),
    z("Begründetheit wie bei der Anfechtungsklage,", 200, 600, "tipp4", "ExtraBold", 33),
    z("nur in der Vergangenheit: „war rechtswidrig“", 240, 652, beim("tipp4", "Vergangenheit"), size=33),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# I Klausurschema (Lexi), Punkt für Punkt
# ===========================================================================================================================
folie([("sch", "Klausurschema · Fortsetzungsfeststellungsklage"), ("sa", "Klausurschema › A. Zulässigkeit"),
       ("s2", "Klausurschema › II. Statthafte Klageart"), ("s3", "Klausurschema › III. Fortsetzungsfeststellungsinteresse"),
       ("s5", "Klausurschema › V. Vorverfahren, VI. Frist"), ("sb", "Klausurschema › B. Begründetheit")], [
    *tafel("sch", "Klausurschema: FFK"),
    z("A. Zulässigkeit", 110, 165, "sa", "ExtraBold", 34),
    z("I. Verwaltungsrechtsweg, § 40 Abs. 1 VwGO", 150, 215, "s1", size=31),
    z("II. Statthafte Klageart: § 113 Abs. 1 Satz 4 direkt/analog", 150, 262, "s2", size=31),
    z("III. Fortsetzungsfeststellungsinteresse", 150, 309, "s3", size=31),
    z("IV. Klagebefugnis, § 42 Abs. 2 VwGO analog", 150, 356, "s4", size=31),
    z("V. Vorverfahren (Landesrecht)", 150, 403, "s5", size=31),
    z("VI. Frist", 150, 450, "s6", size=31),
    z("VII. Übrige Voraussetzungen", 150, 497, "s7", size=31),
    z("B. Begründetheit", 110, 565, "sb", "ExtraBold", 34),
    z("I. Der Verwaltungsakt war rechtswidrig", 150, 615, "s8", size=31),
    z("II. und verletzte den Kläger in seinen Rechten", 150, 662, "s9", size=31),
    *redet("LX_erklaert", FX, FB, FR + 40, "sch", "merke"),
    ns("Lexi", FX, FB, "sch", GELB, d=0.2),
])

# ===========================================================================================================================
# J Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Erledigt heißt nicht ", 0), ("schutzlos", "a"), (".", 0)]], 750, 300, 44, "merke",
                {"a": beim("merke", "schutzlos")}),
    *markertext([[("Bei ", 0), ("berechtigtem Interesse", "b"), (" stellt das", 0)],
                 [("Gericht fest, dass der Verwaltungsakt", 0)], [("rechtswidrig", "c"), (" war.", 0)]],
                750, 440, 42, "m2", {"b": beim("m2", "berechtigtem"), "c": beim("m2", "rechtswidrig")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
