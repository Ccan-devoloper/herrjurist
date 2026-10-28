"""Folge 271 · Hells-Angels-Fall: Schüsse auf das SEK – Erlaubnistatbestandsirrtum. Serienstandard Open Peeps (Katzenkönig).
Fiktiver Rahmen nach dem echten Fall (BGH, Urt. v. 2.11.2011 – 2 StR 375/11; Rn. nach der amtlichen Fassung): Elmar und Gabi
sind erfundene Figuren, keine Clubsymbole, keine Kutten, keine echten Namen. Darstellung: kein Schuss, kein Mündungsfeuer,
keine Waffe im Bild, keine Verletzten – nur Tür, Geräusch-Symbol, Uhrzeit, Polizeischild als Symbol; der getroffene Beamte
wird nur erwähnt. Szenen laut ../SZENENPLAN.md. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/
feld/requisit/stehend/paar/nachtfolie/hand als eigene Kopie aus Folge 231 (gemeinsame Dateien unverändert); neu: Haus-
Bausteine (Fenster mit Rollladen, Treppe, Haustür mit Ornamentglas, Licht im Flur).
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut StGB nach gesetze-im-internet.de, Abruf 08.10.2026."""


import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_271/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_271/" in n:
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
NAME = {"EL": "Elmar", "GA": "Gabi"}
NFARBE = {"EL": BLAU, "GA": PINK}
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







# --- Folge 271: Größen, Dämmerung im dunklen Haus -----------------------------------------------------------------------------
GROESSE = {"EL": 1.0, "GA": 0.95}         # Gabi etwas kleiner als Elmar


def hh(k, h):
    return round(h * GROESSE[k])


def stehend(k, x, folge, bis=None):
    els = [*fig(k, x, FB, hh(k, FR), folge, bis=bis), bis_(ns(NAME[k], x, FB, folge[0][0], NFARBE[k], d=0.1), bis)]
    return rechts_frei(els, 1200)


BG_FARBE["nacht"] = None                     # Nacht = Verlauf, erzeugt im Renderer (wie Folgen 001, 148)
PFAD_FARBE["nacht"] = (255, 255, 255, 170)


def nachtfolie(pfade, els):
    """Fallszene in der Dämmerung: Im Haus brannte kein Licht; Dunkelheit und geschlossene Tür tragen den Irrtum."""
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


# --- Haus-Bausteine (programmatisch, Palettenflächen, Tuschekontur) -------------------------------------------------------
GLAS = (200, 214, 236, 255)                 # Ornamentglas der Haustür
ROLLO = (176, 178, 196, 255)
NACHTGLAS = (52, 62, 108, 255)
HOLZ_ = (190, 138, 92, 255)


def fenster_rollo(x0, y0, w, h, cue):
    """Schlafzimmerfenster mit halb geschlossenem Rollladen (Rn. 8: Rollläden ganz oder teilweise geschlossen)."""
    def zz(dr, s):
        dr.rectangle((3 * s, 3 * s, (w - 3) * s, (h - 3) * s), fill=NACHTGLAS, outline=INK, width=6 * s)
        ro = int(h * 0.58)
        dr.rectangle((3 * s, 3 * s, (w - 3) * s, ro * s), fill=ROLLO, outline=INK, width=6 * s)
        for yy in range(20, ro, 22):
            dr.line((8 * s, yy * s, (w - 8) * s, yy * s), fill=INK, width=2 * s)
        dr.line((w // 2 * s, ro * s, w // 2 * s, (h - 3) * s), fill=INK, width=5 * s)
    im = Image.new("RGBA", ((w + 2) * 2, (h + 2) * 2)); dr = ImageDraw.Draw(im); zz(dr, 2)
    return hart(El(im.resize((w + 2, h + 2), Image.LANCZOS), x0, y0, cue, "cut", 0.0, None, name="fenster"))


def treppe(x0, x1, oben, unten, cue, stufen=9):
    """Treppe in Seitenansicht: steigt nach links zum Obergeschoss (Fläche Graublau, Tuschekontur)."""
    w, h = x1 - x0, unten - oben
    sb, sh = w / stufen, h / stufen
    im = Image.new("RGBA", ((w + 8) * 2, (h + 8) * 2)); dr = ImageDraw.Draw(im); s = 2
    pts = [(w + 4, h + 4)]
    for i in range(stufen):
        x = w + 4 - i * sb; y = h + 4 - (i + 1) * sh
        pts += [(x, y + sh), (x, y), (x - sb, y)]
    poly = pts + [(pts[-1][0], h + 4)]
    dr.polygon([(a * s, b * s) for a, b in poly], fill=(122, 132, 160, 255))
    dr.line([(a * s, b * s) for a, b in pts], fill=INK, width=6 * s, joint="curve")
    im = im.resize((w + 8, h + 8), Image.LANCZOS)
    return hart(El(im, x0 - 4, oben - 4, cue, "cut", 0.0, None, name="treppe"))


TX, TW, TH = 1380, 210, 560                  # Haustür: links, Breite, Höhe
GL = [(TX + 52, 0), (TX + 124, 0)]           # zwei schmale Ornamentgläser (Rn. 9: 10,5 × 44 cm)
GLW, GLH, GLY = 34, 150, BODEN - TH + 110


def haustuer(cue):
    def zz(dr, s):
        dr.rounded_rectangle((3 * s, 3 * s, (TW - 3) * s, (TH + 2) * s), 8 * s, fill=HOLZ_, outline=INK, width=6 * s)
        for gx, _ in GL:
            x = gx - TX
            dr.rectangle((x * s, 110 * s, (x + GLW) * s, (110 + GLH) * s), fill=GLAS, outline=INK, width=4 * s)
            for yy in range(118, 110 + GLH, 14):
                dr.arc(((x + 4) * s, yy * s, (x + GLW - 4) * s, (yy + 12) * s), 0, 180, fill=(160, 176, 205, 255), width=2 * s)
        dr.ellipse((22 * s, (TH // 2) * s, 40 * s, (TH // 2 + 18) * s), fill=INK)
    im = Image.new("RGBA", ((TW + 2) * 2, (TH + 6) * 2)); dr = ImageDraw.Draw(im); zz(dr, 2)
    return hart(El(im.resize((TW + 2, TH + 6), Image.LANCZOS), TX, BODEN - TH, cue, "cut", 0.0, None, name="haustuer"))


def umrisse(cue, bis=None):
    """Durch das Ornamentglas nur Umrisse einer Person (Rn. 9): dunkle, unscharfe Fläche in beiden Gläsern."""
    im = Image.new("RGBA", (TW, GLH + 2))
    m = Image.new("L", im.size, 0); md = ImageDraw.Draw(m)
    md.ellipse((70, 4, 140, 70), fill=230); md.rounded_rectangle((40, 60, 170, GLH + 40), 40, fill=230)
    m = m.filter(ImageFilter.GaussianBlur(6))
    maske = Image.new("L", im.size, 0); dd = ImageDraw.Draw(maske)
    for gx, _ in GL:
        dd.rectangle((gx - TX + 3, 3, gx - TX + GLW - 3, GLH - 3), fill=255)
    from PIL import ImageChops
    m = ImageChops.multiply(m, maske)
    lay = Image.new("RGBA", im.size, (70, 74, 92, 255)); lay.putalpha(m)
    return El(lay, TX, GLY, cue, "fade", 0.0, bis, name="umrisse")


def raumlicht(cue):
    """Licht im Flur: warmer, halbtransparenter Schein über dem Innenraum (links der Tür)."""
    im = Image.new("RGBA", (TX - 46, BODEN - 44), (255, 230, 165, 115))
    return El(im, 44, 44, cue, "fade", 0.0, None, name="raumlicht")


def wand(x, cue):
    """Hauswand neben der Haustür (Trennlinie innen/außen)."""
    return hart(linienzug([(x, 60), (x, BODEN)], cue, breite=7, farbe=INK))


FHA = {k: hh(k, FH) for k in GROESSE}

# ===========================================================================================================================
# A1 Fall: frühmorgens im Schlafzimmer (Dämmerung, kein Licht im Haus)
# ===========================================================================================================================
GAX, ELX0, ELX1 = 690, 1050, 1300
FW = beim("fenster", "schaut"), beim("fenster", "Fenster", ende=True)       # Elmar geht zum Fenster
knack1 = ficon("tabler", "volume", 1820, 620, 92, beim("gabi", "knackt"), fuell=GELB, spiegeln=True, bis="elmar")
szene(knack1, "271knacken*", 0.6)
el_fenster = bewegt(peep_voll("EL_denkt_r", ELX1, BODEN, FHA["EL"], FW[0], anim="cut", bis="ueberfall"), FW[0], FW[1], ELX0 - ELX1)
nachtfolie([(NULL, "Fall · Frühmorgens, gegen 6 Uhr"), ("gabi", "Fall · Geräusche an der Haustür"),
            ("elmar", "Fall · Elmar"), ("geruecht", "Fall · Gerüchte über einen Anschlag"),
            ("fenster", "Fall · Blick aus dem Fenster"), ("ueberfall", "Fall · Er glaubt an einen Überfall"),
            ("pistole", "Fall · Er bewaffnet sich"), ("handy", "Fall · Gabi soll Hilfe holen")], [
    boden(NULL),
    fenster_rollo(1430, 230, 330, 330, NULL),
    hart(ficon("tabler", "bed", 330, BODEN + 4, 400, NULL, fuell=LILA, anim="cut")),
    hart(ficon("tabler", "clock", 1230, 190, 84, NULL, fuell=WEISS, anim="cut")),
    hart(pl("Frühmorgens, gegen 6 Uhr – es dämmert", 70, 30, NULL, fill=GELB, size=32)),
    # Gabi wacht auf, hört das Knacken, weckt Elmar
    *fig("GA", GAX, BODEN, FHA["GA"], [(NULL, "ruhig_r"), ("gabi", "schreck_r")], bis="ga1", erst="cut"),
    *redet("GA_ruft_r", GAX, BODEN, FHA["GA"], "ga1", "elmar"),
    *fig("GA", GAX, BODEN, FHA["GA"], [("elmar", "sorge_r"), ("ueberfall", "angst_r"), ("handy", "angst_r")], erst="cut"),
    hart(ns(NAME["GA"], GAX, BODEN, NULL, NFARBE["GA"], anim="cut")),
    ficon("tabler", "ear", GAX + 130, 390, 74, beim("gabi", "Unten"), fuell=PINK, bis="ga1"),
    knack1,
    pl("lautes Knacken an der Haustür", 70, 94, beim("gabi", "knackt"), fill=WEISS, size=30, bis="elmar"),
    blase("sprech", 520, 200, "ga1", 900, 200, inhalt=["Elmar, wach auf!", "Da ist jemand an der Tür!"], textsize=32,
          figur=("GA_ruft_r", GAX, BODEN, FHA["GA"]), bis="elmar"),
    # Elmar: aufgeweckt, Gerüchte, Fenster, Überfall, Pistole (nur gesprochen, nicht im Bild)
    *fig("EL", ELX0, BODEN, FHA["EL"], [("ga1", "muede"), ("elmar", "ernst"), ("geruecht", "sorge")], bis=FW[0]),
    bis_(ns(NAME["EL"], ELX0, BODEN, "ga1", NFARBE["EL"], d=0.1), FW[0]),
    el_fenster,
    bis_(bewegt(ns(NAME["EL"], ELX1, BODEN, FW[0], NFARBE["EL"], anim="cut"), FW[0], FW[1], ELX0 - ELX1), "ueberfall"),
    *fig("EL", ELX1, BODEN, FHA["EL"], [("ueberfall", "angst_r"), ("pistole", "ernst"), ("handy", "ernst")], erst="cut"),
    ns(NAME["EL"], ELX1, BODEN, "ueberfall", NFARBE["EL"], anim="cut"),
    pl("Elmar: führendes Mitglied eines Rockerclubs", 70, 94, beim("elmar", "führendes"), fill=WEISS, size=30, bis="fenster"),
    ficon("tabler", "alert-triangle", ELX0, 330, 70, "geruecht", fuell=HELLROT, bis="fenster"),
    pl("Gerücht: Ein verfeindeter Club will töten.", 70, 158, "geruecht", fill=HELLROT, size=30, bis="fenster"),
    pl("Am Vortag: neue Hinweise", 70, 222, beim("geruecht", "Vortag"), fill=WEISS, size=30, bis="fenster"),
    pl("Draußen: niemand zu erkennen", 1595, 600, beim("fenster", "erkennt"), fill=WEISS, size=28, anker="m", bis="ueberfall"),
    blase("denk", 400, 190, "ueberfall", 980, 260, inhalt=["Der Überfall!"], textsize=36,
          figur=("EL_angst_r", ELX1, BODEN, FHA["EL"]), bis="pistole"),
    pl("Er nimmt seine Pistole – mit Waffenerlaubnis.", 70, 94, "pistole", fill=WEISS, size=30),
    ficon("tabler", "device-mobile", GAX + 90, 640, 54, beim("handy", "Handy"), fuell=BLAU),
    pl("Gabi: zurück ins Schlafzimmer, Familie verständigen", 70, 158, "handy", fill=PINK, size=30),
])

# ===========================================================================================================================
# A2 Fall: Flur, Treppe und Haustür – Licht, Ruf, Schüsse (nur gesprochen), Polizei
# ===========================================================================================================================
EXT, EXB = 470, 900                          # Elmar: auf der Treppe, unten am Treppenabsatz
UT = 650                                     # Unterkante auf der Treppe
TREPPAB = beim("licht", "geht"), beim("licht", "hinunter", ende=True)
knack2 = ficon("tabler", "volume", 1700, 580, 92, "knack", fuell=GELB, spiegeln=True, bis="nichts")
szene(knack2, "271knacken*", 0.5)
licht = szene(raumlicht(beim("licht", "Licht")), "271schalter*", 0.7)
PO = beim("polizei", "Hier")
folie_els = [
    boden("licht"), treppe(60, 760, 470, BODEN, "licht"), haustuer("licht"), wand(TX - 4, "licht"), wand(TX + TW + 6, "licht"),
    hart(ficon("tabler", "bulb", 700, 170, 70, "licht", fuell=WEISS, anim="cut")),
    hart(linienzug([(700, 46), (700, 100)], "licht", breite=5, farbe=INK)),
    licht,
    ficon("tabler", "bulb-filled", 700, 170, 70, beim("licht", "Licht"), fuell=GELB, anim="cut"),
    pl("Licht im Flur", 760, 120, beim("licht", "Licht"), fill=GELB, size=28, bis="knack"),
    # Elmar kommt die Treppe herunter (bewegt dx/dy), bleibt am Treppenabsatz
    bis_(bewegt(peep_voll("EL_ernst_r", EXB, BODEN, FHA["EL"], "licht", anim="cut"), TREPPAB[0], TREPPAB[1],
                EXT - EXB, UT - BODEN), "knack"),
    bis_(bewegt(ns(NAME["EL"], EXB, BODEN, "licht", NFARBE["EL"], anim="cut"), TREPPAB[0], TREPPAB[1], EXT - EXB, UT - BODEN), "weg"),
    *fig("EL", EXB, BODEN, FHA["EL"], [("knack", "sorge_r"), ("umriss", "denkt_r"), ("keine", "angst_r")], bis="el1", erst="cut"),
    *redet("EL_ruft_r", EXB, BODEN, FHA["EL"], "el1", "nichts"),
    *fig("EL", EXB, BODEN, FHA["EL"], [("nichts", "angst_r"), ("weg", "schreck_r")], bis="el2", erst="cut"),
    *redet("EL_klagt_r", EXB, BODEN, FHA["EL"], "el2", "sek"),
    *fig("EL", EXB, BODEN, FHA["EL"], [("sek", "still_r"), ("verdeckt", "augen_r")], erst="cut"),
    ns(NAME["EL"], EXB, BODEN, "weg", NFARBE["EL"], anim="cut"),
    knack2,
    pl("draußen: weiter an der Tür gearbeitet", 70, 30, "knack", fill=WEISS, size=30, bis="el1"),
    umrisse("umriss"),
    pl("durch das Glas: nur Umrisse", 70, 94, "umriss", fill=WEISS, size=30, bis="el1"),
    pl("keine normalen Einbrecher – die Rivalen", 70, 158, beim("keine", "keine"), fill=HELLROT, size=30, bis="el1"),
    blase("sprech", 420, 170, "el1", 1110, 250, inhalt=["Verschwindet!"], textsize=40,
          figur=("EL_ruft_r", EXB, BODEN, FHA["EL"]), bis="nichts"),
    pl("Draußen hört ihn niemand.", 70, 30, "nichts", fill=WEISS, size=30, bis="sek"),
    pl("Er schießt 2-mal auf die geschlossene Tür.", 70, 94, beim("schuss", "schießt"), fill=HELLROT, size=30, bis="sek"),
    pl("Der 2. Schuss trifft einen Polizeibeamten tödlich.", 70, 158, "beamter", fill=HELLGRAU, size=30, bis="sek"),
    # Polizeischild als Symbol vor der Tür (keine Beamten im Bild)
    ficon("tabler", "shield", 1745, 700, 150, PO, fuell=BLAU),
    pl("Polizei", 1745, 470, PO, fill=BLAU, size=30, anker="m"),
    pl("„Hier ist die Polizei!“", 70, 222, PO, fill=BLAU, size=30, bis="sek"),
    pl("Er legt die Waffe sofort weg.", 70, 286, "weg", fill=WEISS, size=30, bis="el2"),
    blase("sprech", 520, 190, "el2", 1080, 260, inhalt=["Warum habt ihr", "nicht geklingelt?"], textsize=36,
          figur=("EL_klagt_r", EXB, BODEN, FHA["EL"]), bis="sek"),
    pl("Draußen: ein Spezialeinsatzkommando (SEK)", 70, 30, "sek", fill=BLAU, size=30),
    ficon("tabler", "file-search", 1745, 850, 110, "durchs", fuell=WEISS),
    pl("Auftrag: Haus durchsuchen, ihn im Schlaf überraschen", 70, 94, "durchs", fill=WEISS, size=30),
    pl("Auch nach dem Licht: nicht zu erkennen gegeben", 70, 158, "verdeckt", fill=HELLROT, size=30),
]
nachtfolie([("licht", "Fall · Licht im Flur"), ("knack", "Fall · Weiter an der Tür"), ("umriss", "Fall · Nur Umrisse"),
            ("keine", "Fall · Er glaubt: die Rivalen"), ("nichts", "Fall · Schüsse durch die Tür"),
            ("polizei", "Fall · Hier ist die Polizei"), ("sek", "Fall · Draußen: ein Spezialeinsatzkommando"),
            ("verdeckt", "Fall · Verdeckt geblieben")], folie_els)

# ===========================================================================================================================
# A3 Die Frage: Landgericht und Bundesgerichtshof
# ===========================================================================================================================
folie([("lg", "Die Frage · Landgericht: Totschlag"), ("bgh", "Die Frage · BGH: Freispruch"),
       ("frage", "Die Frage · Notwehrlage vorgestellt? Warnen?")], [
    *tafel("lg", "Die Frage"),
    blk(110, 180, 1040, 130, HELLROT, "lg", [("Landgericht: Totschlag", "ExtraBold", 36, INK),
                                          ("Er hätte zuerst warnen müssen (Warnschuss).", "Regular", 32, INK)]),
    zit("LG Koblenz, Urt. v. 28.2.2011; BGH 2 StR 375/11, Rn. 10", 110, 322, "lg"),
    blk(110, 390, 1040, 90, HELLGRUEN, "bgh", [("Bundesgerichtshof: Freispruch vom Totschlag", "ExtraBold", 34, INK)]),
    zit("„Hells-Angels-Fall“: BGH, Urt. v. 2.11.2011 – 2 StR 375/11", 110, 492, beim("bgh", "Hells")),
    blk(110, 570, 1040, 90, GELB, "frage", [("Durfte er sich eine Notwehrlage vorstellen?", "ExtraBold", 34, INK)]),
    blk(110, 690, 1040, 90, GELB, beim("frage", "musste"), [("Musste er vorher warnen?", "ExtraBold", 34, INK)]),
    *requisit([("lg", ("tabler", "scale", 120, HELLROT), "Landgericht", HELLROT),
               ("bgh", ("tabler", "building-bank", 110, HELLGRUEN), "Bundesgerichtshof", HELLGRUEN),
               ("frage", ("tabler", "question-mark", 90, GELB), "Die Frage", GELB)]),
    *stehend("EL", FX, [("lg", "still"), ("bgh", "ruhig"), ("frage", "denkt")]),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_271(cue, absaetze, frage):
    els = [karte(140, 50, 1640, 930, cue, fill=HELL), titel("Sachverhalt", 210, 84, cue, 56)]
    y = 180
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=34, zeilenabstand=1.3)
        els += e; y += 10
    assert y + 60 <= 975, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 4, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_271("sv", [
    "Elmar, führendes Mitglied eines Rockerclubs, glaubt nach Gerüchten und Hinweisen vom Vortag, ein verfeindeter Club "
    "wolle ihn töten. Gegen 6 Uhr morgens, in der Dämmerung, weckt ihn seine Verlobte Gabi: An der Haustür knackt es laut. "
    "Elmar sieht aus dem Fenster niemanden, nimmt seine Pistole (mit Waffenerlaubnis), schaltet im Flur das Licht ein und "
    "geht die Treppe hinunter.",
    "Draußen wird weiter an der Tür gearbeitet; durch das Glas sieht er nur Umrisse. Er hält die Leute für Rivalen, die ihn "
    "und Gabi töten wollen. Er ruft „Verschwindet!“, draußen hört ihn niemand. Weil er erwartet, gleich durch die Tür "
    "beschossen zu werden, schießt er ohne Warnschuss zweimal auf die geschlossene Tür und nimmt in Kauf, einen Menschen "
    "tödlich zu treffen. Der zweite Schuss tötet einen Polizeibeamten.",
    "Draußen war ein Spezialeinsatzkommando, das sein Haus durchsuchen und ihn im Schlaf überraschen sollte. Auch nach dem "
    "Einschalten des Lichts gaben sich die Beamten nicht zu erkennen.",
], "Hat sich Elmar strafbar gemacht?")

# ===========================================================================================================================
# C I. Tatbestand: § 212 StGB
# ===========================================================================================================================
PT = "A. Elmar, § 212 StGB"
folie([("tb", f"{PT} › I. Tatbestand"), (beim("tb", "billigend"), f"{PT} › I. Tatbestand › Vorsatz"),
       ("ident", f"{PT} › I. Tatbestand › Irrtum über die Person")], [
    *tafel("tb", "I. Totschlag, § 212 StGB"),
    *okz("Elmar hat einen Menschen getötet.", 190, beim("tb", "getötet"), "Bold", 35),
    *okz("Vorsatz: Er nahm billigend in Kauf,", 270, beim("tb", "billigend"), "Bold", 35),
    z("jemanden tödlich zu treffen.", 185, 320, beim("tb", "billigend"), size=34),
    zit("BGH, Urt. v. 2.11.2011 – 2 StR 375/11, Rn. 9", 185, 368, beim("tb", "billigend")),
    blk(110, 440, 1040, 130, GELB, "ident", [("Polizist statt Rivale:", "ExtraBold", 35, INK),
                                          ("unbeachtlicher Irrtum über die Person", "Regular", 34, INK)]),
    zit("Rotsch, ZJS 2012, 109, 111 (gleichwertige Tatobjekte: Mensch)", 110, 582, "ident"),
    *requisit([("tb", ("tabler", "book", 110, WEISS), "§ 212 StGB", WEISS),
               ("ident", ("tabler", "user-question", 110, GELB), "Irrtum über die Person", GELB)]),
    *stehend("EL", FX, [("tb", "still"), ("ident", "denkt")]),
])

# ===========================================================================================================================
# D II. Rechtswidrigkeit: § 32 Abs. 2 StGB (Wortlautkarte) – Notwehr gegen die Polizei?
# ===========================================================================================================================
PR = f"{PT} › II. Rechtswidrigkeit: Notwehr, § 32 StGB"
w32, w32_y = wortlaut(80, 170, 1100,
                      "„(2) Notwehr ist die Verteidigung, die erforderlich ist, um einen gegenwärtigen rechtswidrigen "
                      "Angriff von sich oder einem anderen abzuwenden.“", "§ 32 Abs. 2 StGB", "p32",
                      marken=[("Verteidigung", beim("p32", "Verteidigung")), ("erforderlich", beim("p32", "erforderlich")),
                              ("gegenwärtigen", beim("p32", "gegenwärtigen")),
                              ("rechtswidrigen", beim("p32", "rechtswidrigen")), ("Angriff", beim("p32", "Angriff"))],
                      size=33)
folie([("rw", f"{PR}?"), ("p32", f"{PR} · Wortlaut Abs. 2"), ("poli", f"{PR} › Angriff durch die Polizei rechtswidrig?"),
       ("zweifel", f"{PR} › Durchsuchung grundsätzlich offen"), ("offen", f"{PR} › vom BGH offengelassen")], [
    *tafel("rw", "II. Rechtswidrigkeit: Notwehr?"),
    *w32,
    z("Gegen die Polizei nur, wenn ihr Einsatz in seiner", 110, w32_y + 30, "poli", "Bold", 33),
    z("konkreten Gestalt rechtswidrig war", 110, w32_y + 76, beim("poli", "konkreten"), "Bold", 33),
    zit("BGH, Urt. v. 2.11.2011 – 2 StR 375/11, Rn. 19", 110, w32_y + 122, "poli"),
    z("Zweifel: Eine Durchsuchung ist grundsätzlich offen.", 110, w32_y + 176, "zweifel", size=33),
    blk(110, w32_y + 240, 1040, 120, HELLGRUEN, "offen", [("BGH: offengelassen", "ExtraBold", 34, INK),
                                                       ("jedenfalls Erlaubnistatbestandsirrtum", "Regular", 33, INK)]),
    zit("BGH, Urt. v. 2.11.2011 – 2 StR 375/11, Rn. 20", 110, w32_y + 372, "offen"),
    *requisit([("rw", ("tabler", "shield-check", 110, GELB), "Notwehr?", GELB),
               ("poli", ("tabler", "shield", 110, BLAU), "Polizei", BLAU),
               ("zweifel", ("tabler", "file-search", 100, WEISS), "Durchsuchung: offen", WEISS),
               ("offen", ("tabler", "help-circle", 110, HELLGRUEN), "offengelassen", HELLGRUEN)]),
    *stehend("EL", FX, [("rw", "denkt"), ("poli", "ernst"), ("offen", "ruhig")]),
])
assert w32_y + 410 <= 900, w32_y

# ===========================================================================================================================
# E Erlaubnistatbestandsirrtum: die vorgestellte Lage
# ===========================================================================================================================
PE = f"{PT} › Erlaubnistatbestandsirrtum"
folie([("vorst", f"{PE} › vorgestellt: Überfall der Rivalen"), ("akut", f"{PE} › vorgestellt: Angriff gegenwärtig"),
       ("lage", f"{PE} › vorgestellte Notwehrlage (+)"), ("spaeter", f"{PE} › Vermeidbarkeit: später")], [
    *tafel("vorst", "Seine Vorstellung"),
    z("Überfall der Rivalen", 110, 180, "vorst", "ExtraBold", 38),
    *okz("Tür fast aufgebrochen", 260, "akut", "Bold", 34),
    *okz("mehrere bewaffnete Angreifer", 310, beim("akut", "mehreren"), "Bold", 34),
    zit("BGH, Urt. v. 2.11.2011 – 2 StR 375/11, Rn. 9, 22", 185, 360, beim("akut", "mehreren")),
    blk(110, 430, 1040, 130, HELLGRUEN, "lage", [("vorgestellt: gegenwärtiger rechtswidriger", "ExtraBold", 33, INK),
                                              ("Angriff auf sein Leben und das von Gabi", "Regular", 33, INK)]),
    blk(110, 600, 1040, 90, BLAUHELL, "spaeter", [("Vermeidbar? Später bei der Fahrlässigkeit", "ExtraBold", 33, INK)]),
    *requisit([("vorst", ("tabler", "door", 100, HOLZ_), "Überfall?", WEISS),
               ("lage", ("tabler", "alert-triangle", 110, HELLROT), "Angriff (vorgestellt)", HELLROT),
               ("spaeter", ("tabler", "hourglass", 90, BLAUHELL), "später", BLAUHELL)]),
    *paar("GA", [("vorst", "angst"), ("lage", "sorge")], "EL", [("vorst", "angst"), ("lage", "ernst"), ("spaeter", "denkt")]),
])

# ===========================================================================================================================
# F Erforderlichkeit aus seiner Sicht: Warnschuss?
# ===========================================================================================================================
PF = f"{PE} › Erforderlichkeit aus seiner Sicht"
folie([("erf", f"{PF}?"), ("regel", f"{PF} › Regel: androhen, Warnschuss"), ("geeignet", f"{PF} › nur wenn geeignet"),
       ("hier", f"{PF} › Warnschuss: Eskalation"), ("kampf", f"{PF} › kein Kampf mit ungewissem Ausgang"),
       ("ruf", f"{PF} › Ruf ohne Wirkung"), ("erfja", f"{PF} (+)")], [
    *tafel("erf", "Erforderlich aus seiner Sicht?"),
    z("Erlaubt: das Mittel, das die Gefahr sicher beendet", 110, 175, "regel", "Bold", 32),
    z("In der Regel: erst androhen oder Warnschuss", 110, 222, beim("regel", "Regel"), size=32),
    z("aber nur, wenn ein Warnschuss den Angriff beenden würde", 110, 269, "geeignet", size=32),
    zit("BGH, Urt. v. 2.11.2011 – 2 StR 375/11, Rn. 23", 110, 314, "geeignet"),
    *neinz("Warnschuss: Angreifer würden durch die Tür", 380, "hier", "Bold", 32, kreuz=beim("hier", "Gegenteil")),
    z("schießen; keine Zeit zum Abwägen", 185, 426, beim("hier", "Zeit"), size=32),
    *okz("kein Kampf mit ungewissem Ausgang", 492, "kampf", "Bold", 32),
    *okz("gerufen hatte er schon, ohne Wirkung", 542, "ruf", size=32),
    zit("BGH, Urt. v. 2.11.2011 – 2 StR 375/11, Rn. 22, 24", 185, 590, "kampf"),
    blk(110, 650, 1040, 90, HELLGRUEN, "erfja", [("Aus seiner Sicht: beide Schüsse erforderlich", "ExtraBold", 33, INK)]),
    zit("BGH, Rn. 24; anders das Landgericht (Rn. 10)", 110, 752, "erfja"),
    *requisit([("erf", ("tabler", "scale", 120, WEISS), "erforderlich?", WEISS),
               ("regel", ("tabler", "hand-stop", 100, GELB), "erst warnen?", GELB),
               ("hier", ("tabler", "door", 100, HOLZ_), "durch die Tür", HELLROT),
               ("erfja", ("tabler", "circle-check", 110, HELLGRUEN), "erforderlich", HELLGRUEN)]),
    *stehend("EL", FX, [("erf", "denkt"), ("hier", "angst"), ("kampf", "ernst"), ("erfja", "ruhig")]),
])

# ===========================================================================================================================
# G Folge: Erlaubnistatbestandsirrtum, § 16 Abs. 1 StGB (Wortlautkarte), Vorsatzschuld entfällt
# ===========================================================================================================================
w16, w16_y = wortlaut(80, 170, 1100,
                      "„(1) Wer bei Begehung der Tat einen Umstand nicht kennt, der zum gesetzlichen Tatbestand gehört, "
                      "handelt nicht vorsätzlich. Die Strafbarkeit wegen fahrlässiger Begehung bleibt unberührt.“",
                      "§ 16 Abs. 1 StGB", "p16",
                      marken=[("Umstand", beim("p16", "Umstand")), ("vorsätzlich", beim("p16", "vorsätzlich")),
                              ("fahrlässiger", beim("p16", "fahrlässiger"))], size=32)
folie([("eti", f"{PE} (+)"), ("p16", f"{PE} › § 16 Abs. 1 StGB"), ("entspr", f"{PE} › § 16 entsprechend: Vorsatzschuld entfällt"),
       ("streit", f"{PE} › Theorienstreit: Folge 231")], [
    *tafel("eti", "Erlaubnistatbestandsirrtum"),
    *w16,
    *okz("BGH: § 16 entsprechend", w16_y + 34, "entspr", "ExtraBold", 34),
    *neinz("Vorsatzschuld entfällt: kein Totschlag", w16_y + 84, beim("entspr", "Vorsatzschuld"), "Bold", 34,
           kreuz=beim("entspr", "scheidet")),
    zit("BGH, Urt. v. 2.11.2011 – 2 StR 375/11, Rn. 21, 24", 185, w16_y + 134, beim("entspr", "Vorsatzschuld")),
    blk(110, w16_y + 196, 1040, 90, LILAHELL, "streit", [("Theorienstreit: Folge 231", "ExtraBold", 34, INK)]),
    *requisit([("eti", ("tabler", "eye", 110, GELB), "Irrtum", GELB),
               ("entspr", ("tabler", "book", 110, WEISS), "§ 16 entsprechend", WEISS),
               ("streit", ("tabler", "arrows-split", 110, LILAHELL), "Folge 231", LILAHELL)]),
    *stehend("EL", FX, [("eti", "ruhig"), ("entspr", "still"), ("streit", "denkt")]),
])
assert w16_y + 290 <= 900, w16_y

# ===========================================================================================================================
# H B. Fahrlässige Tötung, § 222 StGB
# ===========================================================================================================================
PB = "B. Elmar, § 222 StGB"
folie([("fahr", f"{PB} › Irrtum vermeidbar?"), ("unverm", f"{PB} › plausible Gründe"),
       ("nicht_erk", f"{PB} › Polizei nicht erkennbar"), ("frei", f"{PB} › unvermeidbar: Freispruch")], [
    *tafel("fahr", "B. Fahrlässige Tötung, § 222"),
    z("nur, wenn er den Irrtum hätte vermeiden können", 110, 180, beim("fahr", "Sie"), "Bold", 34),
    zit("§ 16 Abs. 1 Satz 2 StGB; BGH, Urt. v. 2.11.2011 – 2 StR 375/11, Rn. 25", 110, 228, beim("fahr", "Sie")),
    z("Vermeidbar? Nein:", 110, 300, "unverm", "ExtraBold", 35),
    *okz("plausible Gründe für einen Überfall", 360, beim("unverm", "plausiblen"), size=34),
    *okz("Beamte gaben sich nicht zu erkennen", 412, "nicht_erk", size=34),
    *okz("Polizeieinsatz nicht rechtzeitig erkennbar", 464, beim("nicht_erk", "Polizeieinsatz"), size=34),
    blk(110, 550, 1040, 90, HELLGRUEN, "frei", [("Freispruch", "ExtraBold", 38, INK)]),
    zit("BGH, Urt. v. 2.11.2011 – 2 StR 375/11, Rn. 25 f.", 110, 652, "frei"),
    *requisit([("fahr", ("tabler", "hourglass", 90, WEISS), "vermeidbar?", WEISS),
               ("nicht_erk", ("tabler", "eye-off", 110, HELLGRAU), "nicht erkennbar", WEISS),
               ("frei", ("tabler", "circle-check", 110, HELLGRUEN), "Freispruch", HELLGRUEN)]),
    *stehend("EL", FX, [("fahr", "sorge"), ("unverm", "ernst"), ("frei", "still")]),
])

# ===========================================================================================================================
# I Kritik (ein Satz, Beleg)
# ===========================================================================================================================
folie([("kritik", "Kritik · bundesweite Empörung"), ("lehre", "Kritik · Urteilsbesprechung: Freispruch richtig")], [
    *tafel("kritik", "Kritik"),
    blk(110, 180, 1040, 90, HELLROT, "kritik", [("Freispruch: bundesweite Empörung", "ExtraBold", 35, INK)]),
    blk(110, 320, 1040, 130, HELLGRUEN, "lehre", [("Urteilsbesprechung: Freispruch richtig", "ExtraBold", 34, INK),
                                               ("bedauert: offen, ob der Einsatz rechtmäßig war", "Regular", 32, INK)]),
    zit("Rotsch, ZJS 2012, 109 f., 114 f. (mit Nachweisen der Reaktionen)", 110, 462, "lehre"),
    *requisit([("kritik", ("tabler", "speakerphone", 110, HELLROT), "Empörung", HELLROT),
               ("lehre", ("tabler", "book", 110, HELLGRUEN), "Fachliteratur", HELLGRUEN)]),
    *stehend("EL", FX, [("kritik", "still"), ("lehre", "ruhig")]),
])

# ===========================================================================================================================
# J Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · zuerst echte Notwehr"), ("k1", "Klausurtipp › Irrtum nur ohne Notwehrlage"),
       ("k2", "Klausurtipp › alle Merkmale nach seiner Vorstellung"), ("k3", "Klausurtipp › sonst Irrtum über die Grenzen, § 17"),
       ("k4", "Klausurtipp › so das Landgericht")], [
    *tafel("tipp", "Klausurtipp: erst echt, dann Irrtum", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Zuerst die echte Notwehr prüfen:", 200, 200, "tipp", "ExtraBold", 34),
    z("Polizeieinsatz rechtmäßig?", 240, 250, beim("tipp", "War"), size=34),
    linienzug([(130, 316), (1130, 316)], "k1", breite=3),
    z("Nur ohne Notwehrlage: Irrtum prüfen", 200, 338, "k1", "ExtraBold", 34),
    linienzug([(130, 404), (1130, 404)], "k2", breite=3),
    z("Alle Notwehrmerkmale nach seiner Vorstellung,", 200, 426, "k2", "ExtraBold", 33),
    z("auch die Erforderlichkeit", 240, 476, beim("k2", "auch"), size=33),
    linienzug([(130, 540), (1130, 540)], "k3", breite=3),
    z("Selbst danach nicht erforderlich:", 200, 562, "k3", "ExtraBold", 33),
    z("Irrtum über die Grenzen der Notwehr, § 17", 240, 612, beim("k3", "irrt"), size=33),
    z("So das Landgericht: Irrtum vermeidbar", 240, 676, "k4", size=33),
    zit("BGH, Urt. v. 2.11.2011 – 2 StR 375/11, Rn. 10; Rotsch, ZJS 2012, 109, 114", 240, 724, "k4"),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# K Klausurschema (Lexi), Punkt für Punkt
# ===========================================================================================================================
folie([("sch", "Klausurschema · Aufbau"), ("s1", "Klausurschema › A. § 212: I. Tatbestand"),
       ("s2", "Klausurschema › II. Rechtswidrigkeit"), ("s3", "Klausurschema › III. Schuld: ETI"),
       ("s4", "Klausurschema › B. § 222 StGB")], [
    *tafel("sch", "Klausurschema: Elmar"),
    z("A. Totschlag, § 212 StGB", 110, 170, "s1", "ExtraBold", 34),
    *plusminus("I. Tatbestand", 150, 230, beim("s1", "Tatbestand"), True, size=34, stil="Bold"),
    z("II. Rechtswidrigkeit: Notwehr scheitert,", 150, 290, "s2", "Bold", 34),
    z("wenn der Einsatz rechtmäßig war", 210, 342, beim("s2", "wenn"), size=34),
    z("III. Schuld: Erlaubnistatbestandsirrtum,", 150, 410, "s3", "Bold", 34),
    *plusminus("Vorsatzschuld entfällt", 210, 462, beim("s3", "Vorsatzschuld"), False, size=34),
    z("B. Fahrlässige Tötung, § 222 StGB", 110, 550, "s4", "ExtraBold", 34),
    *plusminus("Irrtum unvermeidbar: straflos", 150, 610, beim("s4", "unvermeidbar"), False, size=34),
    *redet("LX_erklaert", FX, FB, FR + 40, "sch", "merke"),
    ns("Lexi", FX, FB, "sch", GELB, d=0.2),
])

# ===========================================================================================================================
# L Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Beim Erlaubnistatbestandsirrtum misst du die", 0)], [("Notwehr an der ", 0), ("Vorstellung", "a"),
                 (" des Täters,", 0)], [("auch die ", 0), ("Erforderlichkeit", "b"), (".", 0)]],
                750, 290, 40, "merke", {"a": beim("merke", "Vorstellung"), "b": beim("merke", "Erforderlichkeit")}),
    *markertext([[("Passt alles, entfällt die ", 0), ("Vorsatzschuld", "c"), (".", 0)],
                 [("Fahrlässig strafbar nur, wenn er den", 0)], [("Irrtum hätte ", 0), ("vermeiden", "d"), (" können.", 0)]],
                750, 520, 40, "m2", {"c": beim("m2", "Vorsatzschuld"), "d": beim("m2", "vermeiden")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
