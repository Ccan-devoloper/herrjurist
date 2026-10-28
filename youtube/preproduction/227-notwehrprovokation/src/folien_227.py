"""Folge 227 · Notwehrprovokation: Absichtsprovokation & Schutzwehr, Trutzwehr – Serienstandard Open Peeps (Katzenkönig).
Fiktiver Fall: Samstagabend auf dem Weinfest am Marktplatz kündigt Ferdinand seiner Kollegin Josefine an, Herrn Pelzer zu reizen
(„Wenn der gleich zuschlägt, ist es Notwehr.“), macht eine beleidigende Bemerkung (nur als Pille), Herr Pelzer holt zum
Faustschlag aus, Frau Höfer ruft Ferdinand hinter ihren Weinstand; Ferdinand sticht mit einem Taschenmesser zu (nur erzählt).
Danach §§ 223, 224 StGB kurz, § 32 Abs. 2 StGB (Wortlautkarte, vorgelesen), Notwehrlage (+), Erforderlichkeit unterstellt,
Gebotenheit (§ 32 Abs. 1, Wortlautkarte), Absichtsprovokation (Rspr./h. M.) und actio illicita in causa, Abwandlung leichtfertige
Provokation mit Voraussetzungen und Stufen Ausweichen – Schutzwehr – Trutzwehr, Ergebnis, Klausurtipp, Schema, Merksatz mit Lexi.
DARSTELLUNG: kein Messer, keine Waffe im Bild, kein Stich, keine Verletzten; Stich und Verletzung nur als Pillentext.
Szenen laut ../SZENENPLAN.md. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/feld/requisit/paar als
eigene Kopie aus Folge 214 (gemeinsame Dateien unverändert); neu: hh(), stehend() mit Körpergröße, weinstand(), lichterkette().
Handlungsgeräusch: Schritte, als Ferdinand zu Herrn Pelzer geht (Freesound CC0 813622); ../geraeusche_herkunft.json.
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut StGB nach gesetze-im-internet.de, Abruf 07.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_227/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_227/" in n:
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
NAME = {"FE": "Ferdinand", "PE": "Herr Pelzer", "JO": "Josefine", "HO": "Frau Höfer"}
NFARBE = {"FE": BLAU, "PE": ORANGE, "JO": GRUEN, "HO": LILA}
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





# --- Folge 227: Größen, Szenenbausteine ---------------------------------------------------------------------------------
GROESSE = {"FE": 1.0, "PE": 1.04, "JO": 0.93, "HO": 0.92}     # Herr Pelzer deutlich kräftiger, die Frauen etwas kleiner


def hh(k, h):
    return round(h * GROESSE[k])


def stehend(k, x, folge, bis=None):
    els = [*fig(k, x, FB, hh(k, FR), folge, bis=bis), bis_(ns(NAME[k], x, FB, folge[0][0], NFARBE[k], d=0.1), bis)]
    return rechts_frei(els, 1200)


STAND_X0, STAND_X1 = 1530, 1870            # Weinstand rechts: Theke von x0 bis x1
DACH_Y, THEKE_H = 360, 200


def weinstand_hinten(cue):
    """Dach und Pfosten des Weinstands (hinter Frau Höfer)."""
    return [hart(linienzug([(STAND_X0 + 20, DACH_Y + 50), (STAND_X0 + 20, BODEN - THEKE_H)], cue, breite=7)),
            hart(linienzug([(STAND_X1 - 20, DACH_Y + 50), (STAND_X1 - 20, BODEN - THEKE_H)], cue, breite=7)),
            hart(feld(STAND_X0 - 20, DACH_Y, STAND_X1 - STAND_X0 + 40, 56, cue, fill=ROT, rand=5, rund=10, name="feld:dach"))]


def weinstand_vorne(cue):
    """Theke mit Flaschen, Gläsern und Trauben (vor Frau Höfer, verdeckt ihre Beine)."""
    y = BODEN - THEKE_H
    return [hart(feld(STAND_X0, y, STAND_X1 - STAND_X0, THEKE_H, cue, fill=HOLZ, rand=5, rund=12, name="feld:theke")),
            hart(ficon("tabler", "bottle", STAND_X0 + 60, y + 4, 58, cue, fuell=GRUEN)),
            hart(ficon("tabler", "glass-full", STAND_X0 + 140, y + 4, 52, cue, fuell=(184, 60, 90, 255))),
            hart(ficon("tabler", "glass-full", STAND_X1 - 150, y + 4, 52, cue, fuell=(184, 60, 90, 255))),
            hart(ficon("tabler", "grape", STAND_X1 - 60, y + 4, 62, cue, fuell=LILA)),
            hart(pl("Weinstand", (STAND_X0 + STAND_X1) / 2, y + 70, cue, fill=WEISS, size=30, anker="m"))]


def lichterkette(cue, x0=980, x1=1880, y=70):
    """Lichterkette des Weinfests: Schnur mit Tabler-Glühbirnen."""
    pts = [(x0 + (x1 - x0) * i / 8, y + (28 if i % 2 else 0)) for i in range(9)]
    els = [hart(linienzug(pts, cue, breite=4))]
    for i, (px, py) in enumerate(pts[1:-1]):
        els.append(hart(ficon("tabler", "bulb", px, py + 52, 38, cue, fuell=GELB if i % 2 else ORANGE)))
    return els


# ===========================================================================================================================
# A1 Fall: Weinfest am Marktplatz – Ankündigung, Bemerkung, Faustschlag droht, Frau Höfer ruft, (Stich nur erzählt)
# ===========================================================================================================================
PEX, FEX0, FEX1, JOX, HOX = 330, 920, 620, 1140, 1390
FH_ = {k: hh(k, FH) for k in GROESSE}
GEH = ("bem", 0.0), beim("bem", "Pelzer", ende=True)      # Ferdinand geht zu Herrn Pelzer
fe_geh = peep_voll("FE_schlau", FEX1, BODEN, FH_["FE"], "bem", anim="cut", bis="messer")
szene(fe_geh, "227schritte*", 0.55, 0.05)
folie([(NULL, "Fall · Weinfest am Marktplatz"), ("stand", "Fall · Am Weinstand von Frau Höfer"),
       ("pelzer", "Fall · Herr Pelzer, seit Langem im Streit"), ("fe1", "Fall · Ferdinands Ankündigung"),
       ("jo1", "Fall · Josefine warnt"), ("bem", "Fall · Die beleidigende Bemerkung"),
       ("faust", "Fall · Herr Pelzer holt zum Schlag aus"), ("ho1", "Fall · Frau Höfer ruft"),
       ("messer", "Fall · Ferdinand sticht zu"), ("arm", "Fall · Herr Pelzer ist verletzt")], [
    boden(NULL), *lichterkette(NULL), *weinstand_hinten(NULL),
    hart(pl("Samstagabend, Weinfest am Marktplatz", 70, 40, NULL, fill=BLAUHELL, size=30)),
    # Frau Höfer vor ihrer Theke (blickt nach links zu den Gästen)
    *fig("HO", HOX, BODEN, FH_["HO"], [("stand", "froh"), ("bem", "sorge")], bis="ho1"),
    *redet("HO_ruft", HOX, BODEN, FH_["HO"], "ho1", "messer"),
    *fig("HO", HOX, BODEN, FH_["HO"], [("messer", "angst")], erst="cut"),
    *weinstand_vorne(NULL),
    ns(NAME["HO"], HOX, BODEN, "stand", NFARBE["HO"], d=0.1),
    pl("Weinstand von Frau Höfer", 70, 104, "stand", fill=WEISS, size=30, bis="bem"),
    # Josefine (blickt zu Ferdinand nach links)
    *fig("JO", JOX, BODEN, FH_["JO"], [("stand", "froh"), ("fe1", "sorge")], bis="jo1"),
    *redet("JO_redet", JOX, BODEN, FH_["JO"], "jo1", "bem"),
    *fig("JO", JOX, BODEN, FH_["JO"], [("bem", "sorge"), ("messer", "angst")], erst="cut"),
    ns(NAME["JO"], JOX, BODEN, "stand", NFARBE["JO"], d=0.1),
    # Ferdinand: erst bei Josefine (blickt nach rechts), schaut zu Herrn Pelzer, kündigt an, geht hin
    *fig("FE", FEX0, BODEN, FH_["FE"], [("stand", "ruhig_r"), ("pelzer", "schlau"), ("leise", "schlau_r")], bis="fe1"),
    *redet("FE_plant_r", FEX0, BODEN, FH_["FE"], "fe1", "jo1"),
    *fig("FE", FEX0, BODEN, FH_["FE"], [("jo1", "froh_r")], bis="bem", erst="cut"),
    bewegt(fe_geh, GEH[0], GEH[1], FEX0 - FEX1),
    *fig("FE", FEX1, BODEN, FH_["FE"], [("messer", "ernst")], erst="cut"),
    ns(NAME["FE"], FEX0, BODEN, "stand", NFARBE["FE"], d=0.1, bis="bem"),
    bewegt(ns(NAME["FE"], FEX1, BODEN, "bem", NFARBE["FE"], anim="cut"), GEH[0], GEH[1], FEX0 - FEX1),
    blase("sprech", 640, 190, "fe1", 1180, 210, inhalt=["Pass auf. Wenn der gleich", "zuschlägt, ist es Notwehr."],
          textsize=32, figur=("FE_plant_r", FEX0, BODEN, FH_["FE"]), bis="jo1"),
    blase("sprech", 600, 190, "jo1", 990, 220, inhalt=["Lass das, Ferdinand.", "Das gibt nur Ärger."], textsize=32,
          figur=("JO_redet", JOX, BODEN, FH_["JO"]), bis="bem"),
    # Herr Pelzer links (blickt nach rechts)
    *fig("PE", PEX, BODEN, FH_["PE"], [("pelzer", "ruhig_r"), ("bem", "denkt_r"), ("faust", "wuetend_r"), ("arm", "schmerz_r")]),
    ns(NAME["PE"], PEX, BODEN, "pelzer", NFARBE["PE"], d=0.1),
    pl("seit Langem Streit mit Ferdinand", 70, 168, "pelzer", fill=WEISS, size=30, bis="bem"),
    # Bemerkung, Faustschlag, Ruf, Stich (nur Pillen)
    ficon("tabler", "message-exclamation", 470, 400, 90, beim("bem", "beleidigende"), fuell=GELB, bis="messer"),
    pl("beleidigende Bemerkung, genau wie geplant", 70, 104, beim("bem", "beleidigende"), fill=GELB, size=30, bis="messer"),
    pl("Herr Pelzer holt zum Faustschlag aus.", 70, 168, "faust", fill=HELLROT, size=30, bis="messer"),
    blase("sprech", 640, 190, "ho1", 1230, 210, inhalt=["Ferdinand, schnell,", "hier hinter den Stand!"], textsize=32,
          figur=("HO_ruft", HOX, BODEN, FH_["HO"]), bis="messer"),
    bis_(pfeil_ink(720, 395, 1200, 395, beim("ho1", "hinter")), "messer"),
    pl("Doch Ferdinand zieht ein Taschenmesser und sticht zu.", 70, 104, "messer", fill=HELLROT, size=30),
    pl("Herr Pelzer: am Arm verletzt", 70, 168, "arm", fill=HELLROT, size=30),
    ficon("tabler", "building-hospital", 900, 400, 100, beim("arm", "Krankenhaus"), fuell=WEISS),
    pl("Krankenhaus", 900, 430, beim("arm", "Krankenhaus"), fill=WEISS, size=28, anker="m"),
])

# ===========================================================================================================================
# A2 Fall: Später bei der Polizei
# ===========================================================================================================================
FEX3 = 1250
folie([("polizei", "Fall · Ferdinand bei der Polizei")], [
    boden("polizei"),
    hart(ficon("tabler", "building", 520, BODEN, 330, "polizei", fuell=WAND)),
    hart(pl("Polizei", 520, 560, "polizei", fill=BLAUHELL, size=30, anker="m")),
    hart(pl("später, bei der Polizei", 70, 40, "polizei", fill=BLAUHELL, size=30)),
    *fig("FE", FEX3, BODEN, FH, [("polizei", "ernst")], bis="fe2", erst="cut"),
    *redet("FE_redet", FEX3, BODEN, FH, "fe2", "frage"),
    hart(ns(NAME["FE"], FEX3, BODEN, "polizei", NFARBE["FE"])),
    blase("sprech", 640, 190, "fe2", 900, 260, inhalt=["Er wollte mich schlagen.", "Ich habe mich nur verteidigt."],
          textsize=32, figur=("FE_redet", FEX3, BODEN, FH)),
])

# ===========================================================================================================================
# A3 Die Frage
# ===========================================================================================================================
folie([("frage", "Die Frage · Notwehr trotz Provokation?"), ("frage2", "Die Frage · Und ohne Absicht?")], [
    *tafel("frage", "Die Frage"),
    z("Kann sich auf Notwehr berufen, wer den", 110, 190, "frage", "Bold", 40),
    z("Angriff selbst herausgefordert hat?", 110, 246, "frage", "Bold", 40),
    blk(110, 360, 1040, 90, GELB, "frage2", [("Und wenn er den Streit gar nicht wollte?", "ExtraBold", 37, INK)]),
    *requisit([("frage", ("tabler", "message-exclamation", 110, GELB), "herausgefordert", WEISS),
               ("frage2", ("tabler", "zoom-question", 110, WEISS), "Streit nicht gewollt?", WEISS)]),
    *paar("FE", [("frage", "denkt"), ("frage2", "sorge")], "PE", [("frage", "ernst")]),
])


# ===========================================================================================================================
# B Sachverhalt (mit Abwandlung)
# ===========================================================================================================================
def sachverhalt_227(cue, absaetze, frage):
    els = [karte(140, 50, 1640, 930, cue, fill=HELL), titel("Sachverhalt", 210, 84, cue, 56)]
    y = 180
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=36, zeilenabstand=1.3)
        els += e; y += 12
    assert y + 66 <= 975, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=34))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_227("sv", [
    "Samstagabend auf dem Weinfest am Marktplatz: Ferdinand hat seit Langem Streit mit Herrn Pelzer. Am Weinstand von "
    "Frau Höfer sagt er leise zu seiner Kollegin Josefine: „Pass auf. Wenn der gleich zuschlägt, ist es Notwehr.“ "
    "Josefine warnt ihn vergeblich.",
    "Ferdinand geht zu Herrn Pelzer und macht, wie geplant, eine beleidigende Bemerkung. Herr Pelzer wird wütend und holt "
    "zum Faustschlag aus. Frau Höfer ruft: „Ferdinand, schnell, hier hinter den Stand!“ Dorthin hätte Ferdinand ausweichen "
    "können. Doch er zieht ein Taschenmesser und sticht zu; Herr Pelzer wird am Arm verletzt. Herr Pelzer ist deutlich "
    "kräftiger als Ferdinand; ein milderes Mittel hätte den Schlag nicht sicher abgewehrt.",
    "Abwandlung: Ferdinand wollte keinen Streit. Die Bemerkung rutschte ihm im Ärger heraus; dass Herr Pelzer darauf "
    "zuschlägt, lag aber nahe.",
], "Ist Ferdinand durch Notwehr gerechtfertigt?")

# ===========================================================================================================================
# C I. Tatbestand: §§ 223, 224 Abs. 1 Nr. 2 StGB (kurz)
# ===========================================================================================================================
PA_ = "A. Ferdinand, §§ 223, 224 StGB"
folie([("tb", f"{PA_} › I. Tatbestand › § 223 Abs. 1"), ("tb2", f"{PA_} › I. Tatbestand › § 224 Abs. 1 Nr. 2: Messer"),
       ("vors", f"{PA_} › I. Tatbestand › Vorsatz"), ("rw", f"{PA_} › II. Rechtswidrigkeit: Notwehr?")], [
    *tafel("tb", "I. Tatbestand: §§ 223, 224 StGB"),
    *okz("§ 223 Abs. 1: Der Stich ist eine Körperverletzung.", 190, beim("tb", "Körperverletzung"), "Bold", 34),
    *okz("§ 224 Abs. 1 Nr. 2: mit dem Messer", 270, beim("tb2", "Messer"), "Bold", 34),
    *okz("Vorsatz: Ferdinand handelte vorsätzlich.", 350, "vors", "Bold", 34),
    blk(110, 450, 1040, 130, GELB, "rw", [("II. Rechtswidrigkeit:", "ExtraBold", 34, INK),
                                       ("gerechtfertigt durch Notwehr, § 32 StGB?", "Regular", 33, INK)]),
    *requisit([("tb", ("tabler", "book", 110, WEISS), "§§ 223, 224 StGB", WEISS),
               ("rw", ("tabler", "shield-check", 110, GELB), "Notwehr?", GELB)]),
    *paar("FE", [("tb", "ernst"), ("rw", "denkt")], "PE", [("tb", "schmerz")]),
])

# ===========================================================================================================================
# D § 32 Abs. 2 StGB: Wortlautkarte (vorgelesen); Verweis Folge 033
# ===========================================================================================================================
PN = "A. Ferdinand › II. Notwehr, § 32 StGB"
w32, w32_y = wortlaut(80, 190, 1100,
                      "„(2) Notwehr ist die Verteidigung, die erforderlich ist, um einen gegenwärtigen rechtswidrigen "
                      "Angriff von sich oder einem anderen abzuwenden.“", "§ 32 Abs. 2 StGB", "p32",
                      marken=[("Verteidigung", beim("p32", "Verteidigung")), ("erforderlich", beim("p32", "erforderlich")),
                              ("gegenwärtigen", beim("p32", "gegenwärtigen")),
                              ("rechtswidrigen", beim("p32", "rechtswidrigen")), ("Angriff", beim("p32", "Angriff"))],
                      size=34)
folie([("p32", f"{PN} · Wortlaut Abs. 2"), ("v033", f"{PN} › Schema: siehe Folge 033")], [
    *tafel("p32", "§ 32 Abs. 2 StGB: Notwehr"),
    *w32,
    blk(110, w32_y + 50, 1040, 80, BLAUHELL, "v033", [("Das ganze Schema: Folge 033 · Notwehr", "ExtraBold", 33, INK)]),
    *requisit([("p32", ("tabler", "book", 110, WEISS), "§ 32 StGB", WEISS)]),
    *stehend("FE", FX, [("p32", "ruhig"), ("v033", "denkt")]),
])
assert w32_y + 150 <= 900, w32_y

# ===========================================================================================================================
# E 1. Notwehrlage (BGH 4 StR 551/12 Rn. 16 f.) und 2. a) Erforderlichkeit (unterstellt)
# ===========================================================================================================================
PL = f"{PN} › 1. Notwehrlage"
folie([("lage", PL), ("angr", f"{PL} › gegenwärtiger Angriff"), ("rechtsw", f"{PL} › rechtswidrig"),
       ("vorbei", f"{PL} › Beleidigung schon vorbei"), ("vergelt", f"{PL} › Schlag wäre Vergeltung"),
       ("lage_ok", f"{PL} (+)"), ("erf", f"{PN} › 2. a) erforderlich (unterstellt)")], [
    *tafel("lage", "1. Notwehrlage"),
    *okz("Angriff: Herr Pelzer holt zum Schlag aus", 180, "angr", "Bold", 34),
    z("gegenwärtig, auf Ferdinands Körper", 185, 228, beim("angr", "gegenwärtiger"), size=33),
    zit("BGH, Urt. v. 25.4.2013 – 4 StR 551/12, Rn. 16 f.", 185, 274, "angr"),
    *okz("rechtswidrig", 330, "rechtsw", "Bold", 34),
    z("Die Beleidigung war schon vorbei:", 185, 380, "vorbei", size=33),
    z("nichts mehr abzuwehren", 185, 424, beim("vorbei", "nichts"), size=33),
    z("Schlag als Antwort: Vergeltung, keine Notwehr", 185, 476, "vergelt", "Bold", 33),
    blk(110, 540, 1040, 80, GRUEN, "lage_ok", [("Notwehrlage (+), obwohl selbst herbeigeführt", "ExtraBold", 34, INK)]),
    *okz("2. a) Erforderlichkeit: unterstellt", 660, "erf", "Bold", 34),
    z("Herr Pelzer deutlich kräftiger;", 185, 710, beim("erf", "Herr"), size=33),
    z("milderes Mittel: hätte nicht sicher abgewehrt", 185, 756, beim("erf", "milderes"), size=33),
    *requisit([("lage", ("tabler", "alert-triangle", 110, GELB), "Notwehrlage?", WEISS),
               ("vorbei", ("tabler", "message-exclamation", 100, WEISS), "Beleidigung: vorbei", WEISS),
               ("lage_ok", ("tabler", "circle-check", 110, HELLGRUEN), "Notwehrlage (+)", HELLGRUEN),
               ("erf", ("tabler", "shield-check", 110, WEISS), "erforderlich", WEISS)]),
    *paar("FE", [("lage", "ruhig"), ("angr", "angst"), ("lage_ok", "schlau")], "PE", [("lage", "ruhig"), ("angr", "wuetend"),
                                                                                    ("vorbei", "denkt")]),
])

# ===========================================================================================================================
# F 2. b) Gebotenheit: § 32 Abs. 1 (Wortlautkarte), sozialethische Einschränkung, Notwehrprovokation, drei Stufen
# ===========================================================================================================================
PH = f"{PN} › 2. b) geboten?"
wG, wG_y = wortlaut(80, 170, 1100, "„(1) Wer eine Tat begeht, die durch Notwehr geboten ist, handelt nicht rechtswidrig.“",
                    "§ 32 Abs. 1 StGB", "geb", marken=[("geboten", beim("geb", "geboten"))], size=33)
folie([("geb", f"{PH} · Wortlaut Abs. 1"), ("sozial", f"{PH} › sozialethische Einschränkung"),
       ("prov", f"{PH} › Fallgruppe Notwehrprovokation"), ("stufen", f"{PH} › Provokation: absichtlich, vorsätzlich, leichtfertig")], [
    *tafel("geb", "2. b) Gebotenheit"),
    *wG,
    z("Aus sozialethischen Gründen eingeschränkt", 110, wG_y + 26, "sozial", "Bold", 34),
    zit("BGH, Beschl. v. 16.6.2021 – 1 StR 126/21, Rn. 18", 110, wG_y + 72, "sozial"),
    blk(110, wG_y + 124, 1040, 80, GELB, "prov", [("Fallgruppe: Notwehrprovokation", "ExtraBold", 36, INK)]),
    z("Wie hat der Täter provoziert?", 110, wG_y + 236, "stufen", "Bold", 34),
    blk(110, wG_y + 290, 330, 80, HELLROT, beim("stufen", "absichtlich"), [("absichtlich", "ExtraBold", 34, INK)]),
    blk(465, wG_y + 290, 330, 80, ORANGE, beim("stufen", "vorsätzlich"), [("vorsätzlich", "ExtraBold", 34, INK)]),
    blk(820, wG_y + 290, 330, 80, GELB, beim("stufen", "leichtfertig"), [("leichtfertig", "ExtraBold", 34, INK)]),
    zit("BGH, Urt. v. 17.1.2019 – 4 StR 456/18, Rn. 6", 110, wG_y + 392, "stufen"),
    *requisit([("geb", ("tabler", "scale", 120, WEISS), "geboten?", WEISS),
               ("prov", ("tabler", "message-exclamation", 100, GELB), "Provokation", GELB)]),
    *stehend("FE", FX, [("geb", "ernst"), ("prov", "sorge")]),
])
assert wG_y + 440 <= 900, wG_y

# ===========================================================================================================================
# G1 Absichtsprovokation: Rspr. und h. M. (BGH 4 StR 456/18 Rn. 6; 3 StR 331/00 Rn. 10)
# ===========================================================================================================================
PB = f"{PN} › 2. b) Absichtsprovokation"
folie([("absicht", f"{PB} · Begriff"), ("hier", f"{PB} › Ferdinand: gezielt"), ("rspr", f"{PB} › Rspr.: Notwehr versagt"),
       ("miss", f"{PB} › Rechtsmissbrauch"), ("hm", f"{PB} › h. L.: im Ergebnis ebenso")], [
    *tafel("absicht", "b) Absichtsprovokation"),
    z("Angriff gezielt herausgefordert, um den Gegner", 110, 180, "absicht", "Bold", 34),
    z("unter dem Deckmantel der Notwehr zu verletzen", 110, 226, beim("absicht", "Deckmantel"), "Bold", 34),
    zit("BGH, Urt. v. 17.1.2019 – 4 StR 456/18, Rn. 6", 110, 274, "absicht"),
    *okz("Ferdinand wollte, dass Herr Pelzer zuschlägt.", 335, "hier", "Bold", 34),
    blk(110, 410, 1040, 80, HELLROT, "rspr", [("Rspr.: Notwehr grundsätzlich ganz versagt", "ExtraBold", 35, INK)]),
    z("Rechtsmissbrauch: Verteidigung nur vorgetäuscht,", 110, 520, "miss", size=34),
    z("in Wirklichkeit will er angreifen", 110, 566, beim("miss", "Wirklichkeit"), size=34),
    zit("BGH, Urt. v. 22.11.2000 – 3 StR 331/00, Rn. 10", 110, 614, "miss"),
    *okz("herrschende Lehre: im Ergebnis genauso", 680, "hm", "Bold", 34),
    *requisit([("absicht", ("tabler", "masks-theater", 120, WEISS), "Deckmantel", WEISS),
               ("hier", ("tabler", "target", 110, GELB), "gezielt", GELB),
               ("rspr", ("tabler", "shield-x", 110, HELLROT), "Notwehr versagt", HELLROT)]),
    *paar("FE", [("absicht", "ernst"), ("hier", "schlau"), ("rspr", "sorge")], "JO", [("absicht", "ernst"), ("miss", "denkt")]),
])

# ===========================================================================================================================
# G2 Gegenansicht: actio illicita in causa (vom BGH nicht anerkannt, 3 StR 331/00 Rn. 15)
# ===========================================================================================================================
folie([("aiic", f"{PB} › Streit: actio illicita in causa"), ("aiic2", f"{PB} › a. i. i. c.: abgelehnt"),
       ("folge", f"{PB} › nicht geboten")], [
    *tafel("aiic", "Lehre: actio illicita in causa"),
    blk(110, 180, 1040, 170, LILAHELL, "aiic", [("Lehre von der actio illicita in causa:", "ExtraBold", 34, INK),
                                              ("Abwehr selbst gerechtfertigt; strafbar", "Regular", 33, INK),
                                              ("wegen des provozierenden Vorverhaltens", "Regular", 33, INK)]),
    *neinz("Bundesgerichtshof: nicht anerkannt", 400, "aiic2", "Bold", 34, kreuz=beim("aiic2", "nicht")),
    zit("BGH, Urt. v. 22.11.2000 – 3 StR 331/00, Rn. 15", 185, 448, "aiic2"),
    *neinz("Schrifttum: ganz überwiegend abgelehnt", 510, beim("aiic2", "Schrifttum"), "Bold", 34,
           kreuz=beim("aiic2", "abgelehnt")),
    zit("Breuer, BRJ 2008, 5 (6)", 185, 558, beim("aiic2", "Schrifttum")),
    blk(110, 630, 1040, 90, HELLROT, "folge", [("Ferdinands Stich war nicht geboten.", "ExtraBold", 36, INK)]),
    *requisit([("aiic", ("tabler", "scale", 120, LILAHELL), "Lehre", LILAHELL),
               ("aiic2", ("tabler", "gavel", 110, WEISS), "nicht anerkannt", WEISS),
               ("folge", ("tabler", "shield-x", 110, HELLROT), "nicht geboten", HELLROT)]),
    *paar("FE", [("aiic", "denkt"), ("folge", "muede")], "JO", [("aiic", "ruhig"), ("folge", "ernst")]),
])

# ===========================================================================================================================
# H1 Abwandlung: leichtfertige Provokation – Voraussetzungen (BGH 4 StR 456/18 Rn. 7; 4 StR 318/20 Rn. 6)
# ===========================================================================================================================
PW = "Abwandlung › leichtfertige Provokation"
folie([("abw", "Abwandlung · Ferdinand wollte keinen Streit"), ("rutsch", "Abwandlung · Bemerkung im Ärger"),
       ("leicht", PW), ("voraus", f"{PW} › Voraussetzungen"), ("erlaubt", f"{PW} › erlaubtes Verhalten genügt nicht"),
       ("ehre", f"{PW} › Beleidigung: rechtswidrig, Schlag sofort")], [
    *tafel("abw", "Abwandlung: ohne Absicht"),
    z("Ferdinand wollte keinen Streit.", 110, 180, "abw", "Bold", 35),
    z("Bemerkung im Ärger herausgerutscht;", 110, 234, "rutsch", size=34),
    z("dass Herr Pelzer zuschlägt, lag nahe", 110, 280, beim("rutsch", "dass"), size=34),
    blk(110, 340, 1040, 80, GELB, "leicht", [("leichtfertige Provokation", "ExtraBold", 36, INK)]),
    z("Notwehr eingeschränkt, wenn das Vorverhalten", 110, 452, "voraus", "Bold", 33),
    *okz("rechtswidrig oder sozialethisch zu missbilligen", 498, beim("voraus", "rechtswidrig"), size=33),
    *okz("und eng mit dem Angriff zusammenhängt", 544, beim("voraus", "eng"), size=33),
    zit("BGH, Urt. v. 17.1.2019 – 4 StR 456/18, Rn. 7", 185, 592, "voraus"),
    *neinz("erlaubtes Verhalten: genügt in der Regel nicht", 650, "erlaubt", size=33, kreuz=beim("erlaubt", "nicht")),
    *okz("Beleidigung: rechtswidrig; Schlag folgt sofort", 720, "ehre", "Bold", 33),
    zit("§ 185 StGB; BGH, Urt. v. 27.9.2012 – 4 StR 197/12, Rn. 15", 185, 768, "ehre"),
    *requisit([("abw", ("tabler", "message-exclamation", 100, WEISS), "keinen Streit gewollt", WEISS),
               ("leicht", ("tabler", "alert-triangle", 110, GELB), "leichtfertig", GELB),
               ("ehre", ("tabler", "circle-check", 110, HELLGRUEN), "rechtswidrig", HELLGRUEN)]),
    *paar("FE", [("abw", "sorge"), ("leicht", "ernst")], "PE", [("abw", "denkt"), ("ehre", "ernst")]),
])

# ===========================================================================================================================
# H2 Abgestufte Einschränkung: Ausweichen – Schutzwehr – Trutzwehr (BGH 4 StR 456/18 Rn. 6; 2 StR 211/24 Rn. 15)
# ===========================================================================================================================
PS_ = f"{PW} › abgestufte Einschränkung"
folie([("einge", PS_), ("aus", f"{PS_} › 1. ausweichen"), ("schutz", f"{PS_} › 2. Schutzwehr"),
       ("trutz", f"{PS_} › 3. Trutzwehr erst zuletzt"), ("vorsatz", f"{PS_} › vorsätzliche Provokation: strenger")], [
    *tafel("einge", "Ausweichen – Schutzwehr – Trutzwehr"),
    z("Notwehrrecht bleibt, aber abgestuft eingeschränkt", 110, 176, "einge", "Bold", 34),
    blk(110, 240, 1040, 80, HELLGRUEN, "aus", [("1. Ausweichen, wenn möglich", "ExtraBold", 35, INK)]),
    blk(170, 340, 980, 120, BLAUHELL, "schutz", [("2. Schutzwehr: Angriff nur abwehren,", "ExtraBold", 33, INK),
                                               ("etwa den Schlag abblocken", "Regular", 33, INK)]),
    blk(230, 480, 920, 160, HELLROT, "trutz", [("3. Trutzwehr: Gegenangriff", "ExtraBold", 33, INK),
                                             ("mit lebensgefährlicher Waffe erst, wenn", "Regular", 32, INK),
                                             ("die Schutzwehr ausgeschöpft ist", "Regular", 32, INK)]),
    zit("BGH 4 StR 456/18, Rn. 6; BGH, Beschl. v. 9.9.2024 – 2 StR 211/24, Rn. 15", 110, 656, "trutz"),
    blk(110, 712, 1040, 120, GELB, "vorsatz", [("vorsätzliche Provokation: noch strenger,", "ExtraBold", 32, INK),
                                             ("ggf. weniger sicheres Abwehrmittel hinnehmen", "Regular", 32, INK)]),
    *requisit([("aus", ("tabler", "arrow-back-up", 110, WEISS), "ausweichen", HELLGRUEN),
               ("schutz", ("tabler", "shield", 110, BLAUHELL), "Schutzwehr", BLAUHELL),
               ("trutz", ("tabler", "bolt", 110, GELB), "Trutzwehr", HELLROT),
               ("vorsatz", ("tabler", "alert-triangle", 110, GELB), "vorsätzlich", GELB)]),
    *stehend("FE", FX, [("einge", "ruhig"), ("aus", "denkt"), ("trutz", "ernst")]),
])

# ===========================================================================================================================
# H3 Im Fall der Abwandlung: Ausweichen hinter den Weinstand möglich → nicht geboten; Gegenfall (BGH 4 StR 197/12 Rn. 15)
# ===========================================================================================================================
folie([("stand2", f"{PW} › im Fall: Ausweichen möglich"), ("nicht2", f"{PW} › Stich nicht geboten"),
       ("anders", f"{PW} › Gegenfall: kein Ausweichen möglich")], [
    *tafel("stand2", "Im Fall der Abwandlung"),
    *okz("Ausweichen hinter den Weinstand möglich:", 180, "stand2", "Bold", 34),
    z("Frau Höfer hatte ihn sogar gerufen.", 185, 228, beim("stand2", "Frau"), size=33),
    *neinz("Sofortiger Stich: auch hier nicht geboten", 310, "nicht2", "ExtraBold", 35, kreuz=beim("nicht2", "nicht")),
    blk(110, 400, 1040, 130, BLAUHELL, "anders", [("Anders: weder ausweichen noch schützen möglich", "ExtraBold", 32, INK),
                                                ("dann am Ende auch mit dem Messer wehren", "Regular", 33, INK)]),
    zit("BGH 4 StR 197/12, Rn. 15; BGH 3 StR 331/00, Rn. 15", 110, 546, "anders"),
    *requisit([("stand2", ("tabler", "arrow-back-up", 110, HELLGRUEN), "hinter den Stand", HELLGRUEN),
               ("nicht2", ("tabler", "shield-x", 110, HELLROT), "nicht geboten", HELLROT),
               ("anders", ("tabler", "barrier-block", 110, ORANGE), "kein Ausweichen", WEISS)]),
    *paar("HO", [("stand2", "ernst"), ("anders", "ruhig")], "FE", [("stand2", "sorge"), ("nicht2", "muede"), ("anders", "denkt")]),
])

# ===========================================================================================================================
# I Ergebnis
# ===========================================================================================================================
PE_ = "A. Ferdinand"
folie([("erg", f"{PE_} › II. Rechtswidrigkeit: nicht gerechtfertigt"), ("strafbar", f"{PE_} › Ergebnis: strafbar")], [
    *tafel("erg", "Ergebnis im Ausgangsfall"),
    *neinz("Ferdinand ist nicht gerechtfertigt.", 190, "erg", "ExtraBold", 36, kreuz=beim("erg", "nicht")),
    *okz("Schuld: Er handelte schuldhaft.", 270, "strafbar", "Bold", 34),
    blk(110, 350, 1040, 130, HELLROT, beim("strafbar", "gefährlicher"), [("strafbar: gefährliche Körperverletzung,", "ExtraBold", 33, INK),
                                                                       ("§§ 223, 224 Abs. 1 Nr. 2 StGB", "ExtraBold", 33, INK)]),
    z("bei Tötungsvorsatz auch versuchter Totschlag,", 110, 520, beim("strafbar", "Tötungsvorsatz"), size=33),
    zit("§§ 212, 22 StGB", 110, 566, beim("strafbar", "Tötungsvorsatz")),
    *requisit([("erg", ("tabler", "shield-x", 110, HELLROT), "nicht gerechtfertigt", HELLROT),
               ("strafbar", ("tabler", "gavel", 110, WEISS), "strafbar", HELLROT)]),
    *paar("FE", [("erg", "ernst"), ("strafbar", "muede")], "PE", [("erg", "ruhig")]),
])

# ===========================================================================================================================
# J Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Provokation in der Gebotenheit"), ("t1", "Klausurtipp › Angriff bleibt rechtswidrig"),
       ("t2", "Klausurtipp › 1. Frage: Absicht?"), ("t3", "Klausurtipp › Signal im Sachverhalt"),
       ("t4", "Klausurtipp › ohne Absicht: die Stufen")], [
    *tafel("tipp", "Klausurtipp: Wo prüfe ich das?", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Provokation in der Gebotenheit prüfen,", 200, 200, "tipp", "ExtraBold", 35),
    z("nicht schon bei der Notwehrlage", 240, 252, beim("tipp", "nicht"), size=34),
    z("Angriff des Provozierten bleibt rechtswidrig", 240, 304, "t1", size=34),
    linienzug([(130, 372), (1130, 372)], "t2", breite=3),
    z("1. Frage: Wollte der Täter den Angriff?", 200, 396, "t2", "ExtraBold", 35),
    z("Signal: eine Ankündigung wie die von Ferdinand", 240, 450, "t3", size=33),
    linienzug([(130, 520), (1130, 520)], "t4", breite=3),
    z("Ohne Absicht: die Stufen prüfen", 200, 544, "t4", "ExtraBold", 35),
    z("ausweichen – Schutzwehr – Trutzwehr", 240, 598, beim("t4", "ausweichen"), size=34),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# K Gutachtenaufbau (Lexi), Punkt für Punkt
# ===========================================================================================================================
folie([("sch", "Klausurschema · Gutachtenaufbau"), ("s1", "Klausurschema › I. Tatbestand"),
       ("s2", "Klausurschema › II. Rechtswidrigkeit"), ("s2b", "Klausurschema › II. 2. b) nicht geboten"),
       ("s3", "Klausurschema › III. Schuld")], [
    *tafel("sch", "Klausurschema: Ferdinand"),
    *plusminus("I. Tatbestand, §§ 223, 224 Abs. 1 Nr. 2", 110, 190, "s1", True, size=36, stil="ExtraBold"),
    z("II. Rechtswidrigkeit: Notwehr, § 32 StGB", 110, 280, "s2", "ExtraBold", 36),
    *plusminus("1. Notwehrlage", 170, 340, beim("s2", "Notwehrlage"), True, size=34),
    *plusminus("2. a) erforderlich", 170, 396, beim("s2", "erforderlich"), True, size=34),
    *plusminus("b) geboten: Absichtsprovokation", 230, 452, "s2b", False, size=34),
    *plusminus("III. Schuld", 110, 540, "s3", True, size=36, stil="ExtraBold"),
    *redet("LX_erklaert", FX, FB, FR + 40, "sch", "merke"),
    ns("Lexi", FX, FB, "sch", GELB, d=0.2),
])

# ===========================================================================================================================
# L Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Wer den Angriff absichtlich provoziert,", 0)], [("hat grundsätzlich ", 0), ("kein Notwehrrecht", "a"),
                 (".", 0)]], 750, 300, 44, "merke", {"a": beim("merke", "kein")}),
    *markertext([[("Wer sonst vorwerfbar provoziert, muss", 0)], [("ausweichen", "b"), (", sich schützen und darf", 0)],
                 [("erst zuletzt zurückschlagen", "c"), (".", 0)]],
                750, 500, 44, "m2", {"b": beim("m2", "ausweichen"), "c": beim("m2", "zuletzt")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
