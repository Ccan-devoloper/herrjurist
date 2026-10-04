"""Folge 192 · Abgrenzungstheorien: Öffentliches oder privates Recht? (§ 40 VwGO) – Serienstandard Open Peeps (Katzenkönig).
Beispielfall: Frau Kirschner pachtet seit 20 Jahren unmittelbar von der Stadt eine Parzelle in der städtischen
Kleingartenanlage; Anfang Februar kündigt die Stadt den Kleingartenpachtvertrag zum 30. November (Spielplatz). Ihre Nachbarin
Elsa (Jurastudentin) bremst die Klage vor dem Verwaltungsgericht. Szenen laut ../SZENENPLAN.md: A Kleingartenanlage, B
Sachverhalt, C Wortlaut § 40 Abs. 1 S. 1 VwGO und § 13 GVG, D drei Merkmale, E streitentscheidende Norm (Wortlautkarten § 4
Abs. 1, § 9 Abs. 1 BKleingG), F die drei Theorien (Tabelle, h. M.), G Sonderfälle, H1 Lösung, H2 zurück im Garten, H3
§ 17a Abs. 2 S. 1 GVG (Wortlaut), I Handlungsform und Verfahrensrecht, J Klausurtipp (Lexi), K Prüfschema, L Merksatz (Lexi).
Handlungsgeräusch: Frau Kirschner reißt den Brief der Stadt auf (A); ../geraeusche_herkunft.json.
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz
als eigene Kopie aus Folge 188 (gemeinsame Dateien unverändert); neu: zaun(), beet(), theorietabelle().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut nach gesetze-im-internet.de (VwGO, GVG, BKleingG, VwVfG),
recht.nrw.de (GO NRW), Abruf 04.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave
import datetime as _dt

bausteine.FIGORDNER = "op_192/"

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
HELLGRAU = (226, 226, 222, 255)
TUERKIS = (127, 214, 208, 255)
ORANGE = (249, 166, 108, 255)
HOLZ = (214, 160, 110, 255)
BEIGE = (201, 166, 107, 255)
ROSE = (242, 167, 195, 255)
FELD1 = (246, 232, 170, 255)
FELD2 = (205, 232, 190, 255)
FELD3 = (176, 218, 160, 255)
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
    e = pille(glyphen(text), *a, **k)
    return e


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
        if n.startswith(("bild:", "ficon:")) or "/op_192/" in n:
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


def wortlaut(x, y, w, text, quelle, cue, marken=(), size=30, bis=None):
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 04.10.2026), als Zitat mit Normangabe; der
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 168/180) -------------------------------------
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
    """Namensschild unter der Figur (ab ihrem ersten Auftritt, solange sie im Bild ist); lange Schilder in 26 px."""
    return pl(text, cx, unten + 22, cue, fill=fill, size=26 if len(text) > 14 else 30, anker="m", **k)


def okz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Haken davor (zur gesprochenen Bejahung)."""
    return [bis_(ok(x - 45, y + 20, cue, gr=gr), k.get("bis")), z(text, x, y, cue, stil, size, **k)]


def neinz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Kreuz davor (zur gesprochenen Verneinung)."""
    return [bis_(nein(x - 45, y + 20, cue, gr=gr), k.get("bis")), z(text, x, y, cue, stil, size, **k)]


# --- eigene Szenenbausteine (programmatisch, Palettenflächen, Tuschekontur) ---------------------------------------------------
BODEN_Y = 905                                # Boden = Unterkante der Figuren in den Fallszenen
FHA = 470                                    # Figurenhöhe in den Fallszenen
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
WAND = (232, 240, 238, 255)
WAND2 = (242, 232, 214, 255)
GRAUW = (205, 205, 200, 255)


def _flaeche(w, h, zeichne):
    s = 2
    im = Image.new("RGBA", (w * s, h * s))
    zeichne(ImageDraw.Draw(im), s)
    return im.resize((w, h), Image.LANCZOS)


def boden(c, x0=60, x1=1860):
    return hart(linienzug([(x0, BODEN_Y), (x1, BODEN_Y)], c, breite=7, farbe=INK))




def schreibtisch(c, x0, x1, h=170):
    w = x1 - x0
    def zz(dr, s):
        dr.rounded_rectangle((3 * s, 0, (w - 3) * s, 28 * s), 6 * s, fill=HOLZ, outline=INK, width=5 * s)
        for xl in (30, w - 60):
            dr.rectangle((xl * s, 28 * s, (xl + 26) * s, (h - 3) * s), fill=HOLZ, outline=INK, width=4 * s)
    return hart(El(_flaeche(w, h, zz), x0, BODEN_Y - h, c, "cut", 0.0, None, name="schreibtisch"))


def fenster(c, x0, y0, w=300, h=260):
    def zz(dr, s):
        dr.rounded_rectangle((3 * s, 3 * s, (w - 3) * s, (h - 3) * s), 10 * s, fill=(214, 232, 250, 255), outline=INK, width=5 * s)
        dr.line((w // 2 * s, 3 * s, w // 2 * s, (h - 3) * s), fill=INK, width=4 * s)
        dr.line((3 * s, h // 2 * s, (w - 3) * s, h // 2 * s), fill=INK, width=4 * s)
    return hart(El(_flaeche(w, h, zz), x0, y0, c, "cut", 0.0, None, name="fenster"))


X1, X2 = 1395, 1730                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"KI": "Frau Kirschner", "EL": "Elsa"}
NFARBE = {"KI": ORANGE, "EL": BLAU}


def stehend(k, x, folge, unten=930, hoehe=480, bis=None):
    return [*fig(k, x, unten, hoehe, folge, bis=bis), ns(NAME[k], x, unten, folge[0][0], NFARBE[k], d=0.1, bis=bis)]


def requisit(folge, px=PX):
    """Wechselndes Requisit über den Figuren: folge = [(cue, (set, icon, breite, fuell), pillentext, pillenfarbe)];
    ein Eintrag (cue, None, None, None) beendet das vorige Requisit (z. B. vor einer Sprechblase)."""
    els = []
    for i, (c, ic, txt, pf) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else None
        if ic:
            s_, n_, br, fu = ic
            els.append(ficon(s_, n_, px, PU, br, c, fuell=fu, bis=b))
        if txt:
            els.append(pl(txt, px, PY, c, fill=pf, size=28, anker="m", bis=b))
    return els


def zwei(folge_l, folge_r, links="EL", rechts="KI"):
    """Zwei Figuren rechts neben der Tafel (blicken nach links zur Tafel)."""
    return [*stehend(links, X1, folge_l), *stehend(rechts, X2, folge_r)]


def allein(k, folge):
    return stehend(k, FX, folge)





import math

# --- eigene Szenenbausteine Folge 192 ----------------------------------------------------------------------------------------
RASEN = (205, 232, 190, 255)
ERDE = (214, 170, 120, 255)


def rasen(c):
    """Rasenstreifen der Kleingartenanlage (Grundform)."""
    def zz(dr, s):
        dr.rectangle((0, 0, 1800 * s, 70 * s), fill=RASEN)
        dr.line((0, 0, 1800 * s, 0), fill=INK, width=4 * s)
    return hart(El(_flaeche(1800, 70, zz), 60, BODEN_Y - 70, c, "cut", 0.0, None, name="rasen"))


def zaun(c, x0, x1, h=120):
    """Lattenzaun hinter den Beeten (Grundform), Tuschekontur."""
    w = x1 - x0
    def zz(dr, s):
        dr.rectangle((0, 40 * s, w * s, 58 * s), fill=WEISS, outline=INK, width=4 * s)
        for x in range(10, w - 30, 46):
            dr.polygon([((x) * s, 18 * s), ((x + 14) * s, 3 * s), ((x + 28) * s, 18 * s), ((x + 28) * s, (h - 3) * s),
                        (x * s, (h - 3) * s)], fill=WEISS, outline=INK)
            dr.line([((x) * s, 18 * s), ((x + 14) * s, 3 * s), ((x + 28) * s, 18 * s), ((x + 28) * s, (h - 3) * s),
                     (x * s, (h - 3) * s), (x * s, 18 * s)], fill=INK, width=4 * s)
    return hart(El(_flaeche(w, h, zz), x0, BODEN_Y - 70 - h + 10, c, "cut", 0.0, None, name="zaun"))


def beet(c, x0, w=330, h=46):
    """Gemüsebeet (Erde mit Tuschekontur)."""
    def zz(dr, s):
        dr.rounded_rectangle((3 * s, 3 * s, (w - 3) * s, (h - 3) * s), 14 * s, fill=ERDE, outline=INK, width=4 * s)
    return hart(El(_flaeche(w, h, zz), x0, BODEN_Y - 60, c, "cut", 0.0, None, name="beet"))


def zellenrahmen(x, y, breiten, h, cue, kopf=False, fill_erste=HELL):
    """Leere Tabellenzeile (Rahmen); der Text erscheint zeilenweise zum gesprochenen Wort."""
    w = sum(breiten)
    im = Image.new("RGBA", (w + 4, h + 4))
    d = ImageDraw.Draw(im)
    xx = 2
    for i, bw in enumerate(breiten):
        fill = GELB if kopf else (fill_erste if i == 0 else WEISS)
        d.rectangle((xx, 2, xx + bw, h + 2), fill=fill, outline=INK, width=4)
        xx += bw
    return El(im, x, y, cue, "rise", 0.0, None, name="tabzeile")


def zelltext(zeilen, x, y, cue, size=28, stil="Bold", breite=300, lh=34):
    els = []
    for i, t in enumerate(zeilen):
        els.append(z(t, x, y + i * lh, cue, stil, size, rechts=x + breite))
    return els


# ===========================================================================================================================
# A Fall: die Parzelle in der städtischen Kleingartenanlage
# ===========================================================================================================================
KIX, ELX = 1260, 1650
folie([(NULL, "Fall · Die Parzelle in der Kleingartenanlage"), ("vertrag", "Fall · Pachtvertrag mit der Stadt"),
       ("brief", "Fall · Ein Brief der Stadt"), ("kuend", "Fall · Kündigung zum 30.11."),
       ("grund", "Fall · Grund: ein Spielplatz"), ("ki1", "Fall · Frau Kirschner will klagen"),
       ("el1", "Fall · Elsa bremst"), ("frage", "Fall · Zivilgericht oder Verwaltungsgericht?"),
       ("frage2", "Fall · die Abgrenzungstheorien")], [
    rasen(NULL),
    zaun(NULL, 80, 1080),
    boden(NULL),
    hart(ficon("fluent-emoji-high-contrast", "hut", 250, BODEN_Y - 40, 260, NULL, fuell=HOLZ, anim="cut")),
    beet(NULL, 470),
    hart(ficon("fluent-emoji-high-contrast", "sunflower", 520, BODEN_Y - 50, 90, NULL, fuell=GELB, anim="cut")),
    hart(ficon("fluent-emoji-high-contrast", "tulip", 610, BODEN_Y - 50, 70, NULL, fuell=ROT, anim="cut")),
    hart(ficon("fluent-emoji-high-contrast", "carrot", 690, BODEN_Y - 50, 70, NULL, fuell=ORANGE, anim="cut")),
    hart(ficon("fluent-emoji-high-contrast", "tomato", 765, BODEN_Y - 50, 70, NULL, fuell=ROT, anim="cut")),
    hart(ficon("tabler", "sun", 1760, 230, 120, NULL, fuell=GELB, anim="cut")),
    hart(pl("Städtische Kleingartenanlage", 70, 30, NULL, fill=GRUEN, size=38)),
    pl("Pächterin seit 20 Jahren", 70, 110, beim("fall", "zwanzig"), fill=WEISS, size=32),
    pl("Pachtvertrag direkt mit der Stadt", 70, 185, "vertrag", fill=GELB, size=32),
    *fig("KI", KIX, BODEN_Y, FHA, [(NULL, "ruhig_r"), ("brief", "liest_r"), ("kuend", "sorge_r"), ("grund", "denkt_r")],
         erst="cut", bis="ki1"),
    *redet("KI_redet_r", KIX, BODEN_Y, FHA, "ki1", "el1"),
    *fig("KI", KIX, BODEN_Y, FHA, [("el1", "entschlossen_r"), ("frage", "denkt_r")], erst="cut"),
    hart(ns(NAME["KI"], KIX, BODEN_Y, NULL, NFARBE["KI"])),
    *fig("EL", ELX, BODEN_Y, FHA, [(NULL, "ruhig"), ("ki1", "denkt")], erst="cut", bis="el1"),
    *redet("EL_redet", ELX, BODEN_Y, FHA, "el1", "frage"),
    *fig("EL", ELX, BODEN_Y, FHA, [("frage", "ruhig")], erst="cut"),
    hart(ns("Elsa · Nachbarin", ELX, BODEN_Y, NULL, NFARBE["EL"])),
    szene(ficon("fluent-emoji-high-contrast", "envelope", 1000, 760, 120, "brief", fuell=WEISS, bis="kuend"), "192brief*", 1.0, -0.05),
    pl("Brief der Stadt", 1000, 560, "brief", fill=WEISS, size=30, anker="m", bis="kuend"),
    ficon("fluent-emoji-high-contrast", "page-facing-up", 1000, 760, 110, "kuend", fuell=WEISS),
    pl("Kündigung zum 30.11.", 1000, 560, "kuend", fill=HELLROT, size=30, anker="m"),
    ficon("fluent-emoji-high-contrast", "playground-slide", 560, 450, 120, "grund", fuell=BLAU),
    pl("geplant: Spielplatz für die Anlage", 70, 260, "grund", fill=BLAU, size=32),
    blase("sprech", 780, 230, "ki1", 1110, 200, inhalt=["Die Stadt ist doch eine Behörde.", "Dann klage ich vor dem",
                                                      "Verwaltungsgericht!"], textsize=34,
          figur=("KI_redet_r", KIX, BODEN_Y, FHA), bis="el1"),
    blase("sprech", 960, 230, "el1", 1260, 200, inhalt=["Nicht so schnell. Dass die Stadt kündigt,", "sagt noch nicht, welches",
                                                      "Gericht zuständig ist."], textsize=34,
          figur=("EL_redet", ELX, BODEN_Y, FHA), bis="frage"),
    pl("Zivilgericht oder Verwaltungsgericht?", 960, 120, "frage", fill=PINK, size=38),
    pl("Antwort: die Abgrenzungstheorien", 960, 210, "frage2", fill=GELB, size=34),
])

# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_192(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=34, zeilenabstand=1.30)
        els += e; y += 18
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_192("sv", [
    "Frau Kirschner pachtet seit 20 Jahren eine Parzelle in der städtischen Kleingartenanlage. Den "
    "Kleingartenpachtvertrag hat sie direkt mit der Stadt geschlossen.",
    "Anfang Februar erhält sie einen Brief der Stadt: Die Stadt kündigt den Pachtvertrag zum 30. November. Auf der Parzelle "
    "soll ein Spielplatz für die Anlage entstehen.",
    "Frau Kirschner meint: „Die Stadt ist doch eine Behörde. Dann klage ich vor dem Verwaltungsgericht!“ Ihre Nachbarin "
    "Elsa, die Jura studiert, ist skeptisch.",
], "Welcher Rechtsweg ist für den Streit um die Kündigung eröffnet?")

# ===========================================================================================================================
# C Wortlaut: § 40 Abs. 1 S. 1 VwGO, § 13 GVG
# ===========================================================================================================================
PR = "Rechtsweg"
W40 = ("„Der Verwaltungsrechtsweg ist in allen öffentlich-rechtlichen Streitigkeiten nichtverfassungsrechtlicher Art "
       "gegeben, soweit die Streitigkeiten nicht durch Bundesgesetz einem anderen Gericht ausdrücklich zugewiesen sind.“")
w40, w40_y = wortlaut(80, 165, 1100, W40, "§ 40 Abs. 1 S. 1 VwGO", "wl40", marken=[
    ("öffentlich-rechtlichen", beim("wl40", "öffentlich-rechtlichen")),
    ("nichtverfassungsrechtlicher Art", beim("wl40", "nichtverfassungsrechtlicher")),
    ("ausdrücklich zugewiesen", beim("wl40", "ausdrücklich"))], size=32)
W13 = "„Vor die ordentlichen Gerichte gehören die bürgerlichen Rechtsstreitigkeiten, … (Zivilsachen) …“"
w13, w13_y = wortlaut(80, w40_y + 30, 1100, W13, "§ 13 GVG", "wl13", marken=[
    ("bürgerlichen", beim("wl13", "bürgerlichen")), ("Rechtsstreitigkeiten,", beim("wl13", "Rechtsstreitigkeiten"))], size=32)
folie([("wl40", f"{PR} · § 40 Abs. 1 S. 1 VwGO"), ("wl13", f"{PR} · Gegenstück: § 13 GVG")], rechts_frei([
    *tafel("wl40", "Verwaltungsgericht oder Zivilgericht?"),
    *w40, *w13,
    *requisit([("wl40", ("fluent-emoji-high-contrast", "classical-building", 110, BLAU), "Verwaltungsgericht", BLAU),
               ("wl13", ("tabler", "gavel", 100, GELB), "Zivilgericht", GELB)]),
    *allein("KI", [("wl40", "denkt"), ("wl13", "liest")]),
]))
assert w13_y <= 890, w13_y

# ===========================================================================================================================
# D Drei Merkmale
# ===========================================================================================================================
PM = "§ 40 Abs. 1 S. 1 VwGO"
folie([("mm", f"{PM} · drei Merkmale"), ("m1", f"{PM} › 1. öffentlich-rechtliche Streitigkeit"),
       ("m2", f"{PM} › 2. nichtverfassungsrechtlicher Art"), ("m3", f"{PM} › 3. keine abdrängende Sonderzuweisung")],
      rechts_frei([
    *tafel("mm", "§ 40 Abs. 1 S. 1 VwGO: drei Merkmale"),
    blk(110, 190, 1040, 80, GELB, "m1", [("1. öffentlich-rechtliche Streitigkeit", "ExtraBold", 34, INK)]),
    pl("Thema dieses Videos", 160, 290, beim("m1", "Thema"), fill=PINK, size=30),
    blk(110, 400, 1040, 80, WEISS, "m2", [("2. nichtverfassungsrechtlicher Art", "ExtraBold", 34, INK)]),
    z("kein Streit von Verfassungsorganen über Verfassungsrecht", 140, 495, beim("m2", "Verfassungsorgane"), size=30),
    blk(110, 590, 1040, 80, WEISS, "m3", [("3. keine abdrängende Sonderzuweisung", "ExtraBold", 34, INK)]),
    zit("z. B. § 40 Abs. 2 S. 1 VwGO: bestimmte Schadensersatzansprüche", 140, 685, beim("m3", "Paragraf"), size=28),
    *requisit([("mm", ("tabler", "list-check", 100, WEISS), "3 Merkmale", WEISS),
               ("m1", ("tabler", "scale", 100, GELB), "öffentlich oder privat?", GELB),
               ("m2", ("fluent-emoji-high-contrast", "classical-building", 110, WEISS), "kein Verfassungsstreit", WEISS),
               ("m3", ("tabler", "arrows-split", 100, WEISS), "keine Zuweisung", WEISS)]),
    *zwei([("mm", "ruhig"), ("m1", "erklaert"), ("m2", "froh")], [("mm", "denkt"), ("m3", "liest")]),
]))

# ===========================================================================================================================
# E Die streitentscheidende Norm: § 4 Abs. 1, § 9 Abs. 1 BKleingG (Wortlaut)
# ===========================================================================================================================
PN = "1. öffentlich-rechtliche Streitigkeit"
W4 = ("„(1) Für Kleingartenpachtverträge gelten die Vorschriften des Bürgerlichen Gesetzbuchs über den Pachtvertrag, "
      "soweit sich aus diesem Gesetz nichts anderes ergibt.“")
w4, w4_y = wortlaut(80, 380, 1100, W4, "§ 4 Abs. 1 BKleingG", "norm4", marken=[
    ("Gesetzbuchs", beim("norm4", "Gesetzbuchs")), ("über den Pachtvertrag,", beim("norm4", "Pacht"))], size=30)
W9 = "„(1) Der Verpächter kann den Kleingartenpachtvertrag kündigen, wenn …“"
w9, w9_y = wortlaut(80, w4_y + 22, 1100, W9, "§ 9 Abs. 1 BKleingG", "norm5", marken=[
    ("Der Verpächter", beim("norm5", "Verpächter"))], size=30)
folie([("norm", f"{PN} · streitentscheidende Norm"), ("norm2", f"{PN} › Nach welcher Norm?"),
       ("norm3", f"{PN} › Streit: Kündigung des Pachtvertrags"), ("norm4", f"{PN} › § 4 Abs. 1 BKleingG: BGB-Pacht"),
       ("norm5", f"{PN} › § 9 Abs. 1 BKleingG: Kündigung"), ("norm6", f"{PN} › öffentlich oder privat?")], rechts_frei([
    *tafel("norm", "Die streitentscheidende Norm"),
    z("öffentlich-rechtlich, wenn die streitentscheidende", 110, 175, "norm", "Bold", 32),
    z("Norm zum öffentlichen Recht gehört", 110, 220, "norm", "Bold", 32),
    z("Frage 1: Nach welcher Norm wird entschieden?", 110, 280, "norm2", "ExtraBold", 32),
    pl("Streit: Kündigung des Kleingartenpachtvertrags", 110, 325, "norm3", fill=GELB, size=28, anim="pop"),
    *w4, *w9,
    pl("öffentlich oder privat? 3 Theorien", 110, w9_y + 22, "norm6", fill=PINK, size=30),
    *requisit([("norm", ("tabler", "file-text", 100, WEISS), "Welche Norm?", WEISS),
               ("norm3", ("fluent-emoji-high-contrast", "page-facing-up", 100, WEISS), "Kündigung", HELLROT),
               ("norm4", ("tabler", "book", 100, GELB), "BGB: Pacht", GELB),
               ("norm5", ("fluent-emoji-high-contrast", "hut", 120, HOLZ), "§ 9 BKleingG", WEISS),
               ("norm6", ("tabler", "scale", 100, WEISS), "3 Theorien", PINK)]),
    *zwei([("norm", "ruhig"), ("norm4", "erklaert"), ("norm6", "denkt")], [("norm", "denkt"), ("norm3", "sorge"), ("norm6", "liest")]),
]))
assert w9_y + 80 <= 890, w9_y

# ===========================================================================================================================
# F Die drei Theorien (Tabelle; h. M. gekennzeichnet)
# ===========================================================================================================================
PT = "Abgrenzungstheorien"
SP_ = [350, 315, 395]                      # Spaltenbreiten: Theorie und Frage | Beispiel | Kritik
TX0, TY0, KOPF_H, ZH = 110, 165, 58, 160
XS = [TX0 + sum(SP_[:i]) for i in range(3)]


def reihe(nr, cue_name, name_zeilen, frage_cue, frage, bsp_cue, bsp, krit_cue, krit, hm=False):
    y = TY0 + KOPF_H + nr * ZH
    els = [zellenrahmen(TX0, y, SP_, ZH, cue_name)]
    els += zelltext(name_zeilen, XS[0] + 14, y + 10, cue_name, 28, "ExtraBold", SP_[0] - 24)
    els += zelltext(frage, XS[0] + 14, y + 12 + 34 * len(name_zeilen), frage_cue, 26, "Regular", SP_[0] - 24, lh=31)
    els += zelltext(bsp, XS[1] + 14, y + 14, bsp_cue, 28, "Bold", SP_[1] - 24)
    els += zelltext(krit, XS[2] + 14, y + 14, krit_cue, 28, "Bold", SP_[2] - 24)
    return els


tab_kopf = [zellenrahmen(TX0, TY0, SP_, KOPF_H, "th1", kopf=True),
            z("Theorie · Frage", XS[0] + 14, TY0 + 10, "th1", "ExtraBold", 30, rechts=XS[1] - 10),
            z("Beispiel", XS[1] + 14, TY0 + 10, "th1", "ExtraBold", 30, rechts=XS[2] - 10),
            z("Kritik", XS[2] + 14, TY0 + 10, "th1", "ExtraBold", 30, rechts=TX0 + sum(SP_) - 10)]
r1 = reihe(0, "th1", ["Interessentheorie"], "i1", ["Dient die Norm dem", "öffentlichen Interesse?"],
           "i2", ["Spielplatz für alle:", "öffentlich?"],
           "i3", ["Gemeinwohl dient fast", "alles; maßgeblich ist", "die Rechtsform"])
r2 = reihe(1, "th2", ["Subordinations-", "theorie"], "s1", ["Über- und", "Unterordnung?"],
           "s2", ["Bescheid: ja", "Pachtvertrag: nein"],
           "s3", ["öffentlich-rechtlicher", "Vertrag: gleichgeordnet,", "trotzdem öffentlich"])
r3 = reihe(2, "th3", ["modifizierte Subjekts-", "theorie"], "t1", ["Berechtigt die Norm", "gerade den Hoheitsträger?"],
           "t3", ["Gewerbe untersagen:", "nur die Behörde"],
           "t4", ["Norm offen: erst", "der Zusammenhang", "entscheidet"])
TY_ENDE = TY0 + KOPF_H + 3 * ZH
folie([("th1", f"{PT} · 1. Interessentheorie"), ("i3", f"{PT} › Interessentheorie: Kritik"),
       ("th2", f"{PT} · 2. Subordinationstheorie"), ("s3", f"{PT} › Subordinationstheorie: Kritik"),
       ("th3", f"{PT} · 3. modifizierte Subjektstheorie (h. M.)"), ("t2", f"{PT} › Sonderrecht oder Jedermannsrecht"),
       ("bverwg", f"{PT} › so auch das BVerwG"), ("t4", f"{PT} › modifizierte Subjektstheorie: Kritik")], rechts_frei([
    *tafel("th1", "Die drei Abgrenzungstheorien", h=860),
    *tab_kopf, *r1, *r2, *r3,
    z("(h. M.)", XS[0] + 14 + int(F("ExtraBold", 28).getlength("theorie ")), TY0 + KOPF_H + 2 * ZH + 10 + 34, "hm",
      "ExtraBold", 28, farbe=DGRUEN, rechts=XS[1] - 10),
    blk(110, TY_ENDE + 14, 1040, 110, GRUEN, "t2", [("Sonderrecht des Staates = öffentliches Recht", "ExtraBold", 30, INK), (" ", "Bold", 30, INK)]),
    z("für jedermann = Privatrecht", 110 + (1040 - int(F("ExtraBold", 30).getlength("für jedermann = Privatrecht"))) // 2, TY_ENDE + 66,
      beim("t2", "jedermann"), "ExtraBold", 30),
    zit("BVerwG, Beschl. v. 21.11.2016 – 10 AV 1.16, Rn. 5 (stRspr)", 140, TY_ENDE + 136, "bverwg"),
    *requisit([("th1", ("tabler", "scale", 100, WEISS), "1. Interesse", WEISS),
               ("i2", ("fluent-emoji-high-contrast", "playground-slide", 110, BLAU), "Gemeinwohl?", BLAU),
               ("th2", ("fluent-emoji-high-contrast", "classical-building", 110, WEISS), "2. oben und unten?", WEISS),
               ("s2", ("fluent-emoji-high-contrast", "handshake", 110, GELB), "Vertrag", GELB),
               ("th3", ("tabler", "building-bank", 100, GRUEN), "3. Sonderrecht?", GRUEN),
               ("t4", ("tabler", "zoom-question", 100, WEISS), "Zusammenhang", WEISS)]),
    *zwei([("th1", "ruhig"), ("i2", "denkt"), ("th2", "erklaert"), ("s3", "ernst"), ("th3", "froh"), ("t4", "denkt")],
          [("th1", "liest"), ("i2", "ruhig"), ("s2", "denkt"), ("th3", "liest"), ("t2", "ruhig")]),
]))
assert TY_ENDE + 175 <= 900, TY_ENDE

# ===========================================================================================================================
# G Sonderfälle: Zwei-Stufen-Theorie, Hausverbot, Fiskalverwaltung
# ===========================================================================================================================
PS2 = "Sonderfälle"
folie([("sf", f"{PS2} · in Kürze"), ("zs", f"{PS2} › Zwei-Stufen-Theorie"), ("hv", f"{PS2} › Hausverbot"),
       ("fisk", f"{PS2} › Fiskalverwaltung")], rechts_frei([
    *tafel("sf", "Drei Sonderfälle"),
    z("Zwei-Stufen-Theorie (öffentliche Einrichtung, z. B. Stadthalle)", 110, 180, "zs", "ExtraBold", 30),
    blk(140, 230, 480, 110, GRUEN, beim("zs", "Ob"), [("1. Stufe: das Ob", "ExtraBold", 30, INK),
                                                     ("Zulassung: öffentlich-rechtlich", "Bold", 26, INK)]),
    blk(650, 230, 500, 110, WEISS, beim("zs", "Wie"), [("2. Stufe: das Wie", "ExtraBold", 30, INK),
                                                      ("z. B. Mietvertrag: ggf. privat", "Bold", 26, INK)]),
    zit("Zulassungsanspruch z. B. § 8 Abs. 2 GO NRW · BVerwG 6 B 10.07, Rn. 15", 140, 352, beim("zs", "Ob")),
    z("Hausverbot im Rathaus: Der Zweck entscheidet", 110, 430, "hv", "ExtraBold", 30),
    *okz("schützt den Dienstbetrieb: öffentlich-rechtlich", 480, beim("hv", "Schützt"), "Bold", 30, x=180),
    zit("VG Düsseldorf, Beschl. v. 28.6.2018 – 15 L 1022/18, Rn. 20", 180, 528, beim("hv", "Schützt")),
    z("Fiskalverwaltung: Stadt kauft Büromaterial", 110, 610, "fisk", "ExtraBold", 30),
    *okz("wie jeder Marktteilnehmer: privatrechtlich", 660, beim("fisk", "privatrechtlich"), "Bold", 30, x=180),
    zit("BVerwG, Beschl. v. 2.5.2007 – 6 B 10.07, Rn. 6", 180, 708, beim("fisk", "privatrechtlich")),
    *requisit([("sf", ("tabler", "list-check", 100, WEISS), "3 Sonderfälle", WEISS),
               ("zs", ("tabler", "building-community", 110, GRUEN), "Stadthalle", GRUEN),
               ("hv", ("tabler", "hand-stop", 100, HELLROT), "Hausverbot", HELLROT),
               ("fisk", ("tabler", "shopping-cart", 100, GELB), "Büromaterial", GELB)]),
    *zwei([("sf", "ruhig"), ("zs", "erklaert"), ("fisk", "froh")], [("sf", "liest"), ("hv", "ernst"), ("fisk", "ruhig")]),
]))

# ===========================================================================================================================
# H1 Lösung des Falls
# ===========================================================================================================================
PL = "Lösung"
folie([("loes", f"{PL} · Frau Kirschner und die Stadt"), ("l1", f"{PL} › streitentscheidend: § 9 BKleingG"),
       ("l2", f"{PL} › Verpächter kann jeder sein"), ("l3", f"{PL} › Stadt als Verpächterin"),
       ("l4", f"{PL} › Privatrecht: Zivilrechtsweg, § 13 GVG")], rechts_frei([
    *tafel("loes", "Lösung: Wer entscheidet über die Kündigung?"),
    z("streitentscheidend:", 110, 180, "l1", "Bold", 32),
    z("§ 9 BKleingG i. V. m. §§ 581 ff. BGB (Pacht)", 110, 225, "l1", "ExtraBold", 34),
    z("berechtigt: der Verpächter – das kann jeder sein:", 110, 300, "l2", "Bold", 32),
    pl("Verein", 140, 350, beim("l2", "Verein"), fill=WEISS, size=30),
    pl("Privatperson", 330, 350, beim("l2", "Privatperson"), fill=WEISS, size=30),
    pl("Stadt", 610, 350, beim("l2", "Stadt"), fill=GELB, size=30),
    *neinz("Stadt nicht als Hoheitsträgerin,", 450, "l3", "Bold", 32, x=160),
    *okz("sondern als Verpächterin", 500, beim("l3", "sondern"), "Bold", 32, x=160),
    blk(110, 580, 1040, 120, GRUEN, "l4", [("Privatrecht: bürgerliche Rechtsstreitigkeit", "ExtraBold", 32, INK),
                                          ("Zivilrechtsweg, § 13 GVG", "ExtraBold", 32, INK)]),
    zit("vgl. BVerwG, Beschl. v. 21.11.2016 – 10 AV 1.16, Rn. 5 f.", 110, 715, "l4"),
    zit("Kündigung durch eine Stadt vor den Zivilgerichten: BGH, Urt. v. 17.7.2025 – III ZR 92/24", 110, 755, "l4"),
    *requisit([("loes", ("fluent-emoji-high-contrast", "page-facing-up", 100, WEISS), "Kündigung", HELLROT),
               ("l2", ("fluent-emoji-high-contrast", "hut", 120, HOLZ), "Verpächter", WEISS),
               ("l3", ("fluent-emoji-high-contrast", "handshake", 110, GELB), "Vertragspartnerin", GELB),
               ("l4", ("tabler", "gavel", 100, GRUEN), "Zivilgericht", GRUEN)]),
    *zwei([("loes", "ruhig"), ("l2", "erklaert"), ("l4", "froh")], [("loes", "denkt"), ("l3", "liest"), ("l4", "ruhig")]),
]))

# ===========================================================================================================================
# H2 zurück im Garten: Elsa und Frau Kirschner (Blasen)
# ===========================================================================================================================
folie([("el2", "Lösung · zurück im Garten"), ("ki2", "Lösung · Und wenn schon beim Verwaltungsgericht geklagt?")], [
    rasen("el2"),
    zaun("el2", 80, 1080),
    boden("el2"),
    hart(ficon("fluent-emoji-high-contrast", "hut", 250, BODEN_Y - 40, 260, "el2", fuell=HOLZ, anim="cut")),
    beet("el2", 470),
    hart(ficon("fluent-emoji-high-contrast", "sunflower", 520, BODEN_Y - 50, 90, "el2", fuell=GELB, anim="cut")),
    hart(ficon("fluent-emoji-high-contrast", "tulip", 610, BODEN_Y - 50, 70, "el2", fuell=ROT, anim="cut")),
    hart(ficon("fluent-emoji-high-contrast", "carrot", 690, BODEN_Y - 50, 70, "el2", fuell=ORANGE, anim="cut")),
    hart(ficon("fluent-emoji-high-contrast", "tomato", 765, BODEN_Y - 50, 70, "el2", fuell=ROT, anim="cut")),
    hart(ficon("tabler", "sun", 1760, 230, 120, "el2", fuell=GELB, anim="cut")),
    hart(pl("Städtische Kleingartenanlage", 70, 30, "el2", fill=GRUEN, size=38)),
    hart(ficon("fluent-emoji-high-contrast", "page-facing-up", 1000, 760, 110, "el2", fuell=WEISS, anim="cut")),
    hart(pl("Kündigung zum 30.11.", 1000, 560, "el2", fill=HELLROT, size=30, anker="m")),
    *redet("KI_fragt_r", KIX, BODEN_Y, FHA, "ki2", "wl17"),
    *fig("KI", KIX, BODEN_Y, FHA, [("el2", "liest_r")], erst="cut", bis="ki2"),
    hart(ns(NAME["KI"], KIX, BODEN_Y, "el2", NFARBE["KI"])),
    *redet("EL_erklaert", ELX, BODEN_Y, FHA, "el2", "ki2"),
    *fig("EL", ELX, BODEN_Y, FHA, [("ki2", "ruhig")], erst="cut"),
    hart(ns("Elsa · Nachbarin", ELX, BODEN_Y, "el2", NFARBE["EL"])),
    blase("sprech", 960, 230, "el2", 1260, 200, inhalt=["Über die Kündigung entscheidet also", "das Zivilgericht, nicht das",
                                                      "Verwaltungsgericht."], textsize=34,
          figur=("EL_erklaert", ELX, BODEN_Y, FHA), bis="ki2"),
    blase("sprech", 900, 230, "ki2", 960, 200, inhalt=["Und wenn ich schon beim", "Verwaltungsgericht geklagt habe?"],
          textsize=34, figur=("KI_fragt_r", KIX, BODEN_Y, FHA), bis="wl17"),
])

# ===========================================================================================================================
# H3 Verweisung: § 17a Abs. 2 S. 1 GVG (Wortlaut), § 173 S. 1 VwGO, § 17b Abs. 1 S. 2 GVG
# ===========================================================================================================================
PV = "Falscher Rechtsweg"
W17 = ("„Ist der beschrittene Rechtsweg unzulässig, spricht das Gericht dies nach Anhörung der Parteien von Amts wegen aus "
       "und verweist den Rechtsstreit zugleich an das zuständige Gericht des zulässigen Rechtsweges.“")
w17, w17_y = wortlaut(80, 165, 1100, W17, "§ 17a Abs. 2 S. 1 GVG (i. V. m. § 173 S. 1 VwGO)", "wl17", marken=[
    ("unzulässig,", beim("wl17", "unzulässig")), ("von Amts wegen", beim("wl17", "Amts")),
    ("verweist den", beim("wl17b", "verweist")), ("Rechtsstreit zugleich", beim("wl17b", "Rechtsstreit"))], size=32)
folie([("wl17", f"{PV} · § 17a Abs. 2 S. 1 GVG"), ("verw", f"{PV} › Verweisung statt Abweisung"),
       ("verw2", f"{PV} › Rechtshängigkeit bleibt, § 17b Abs. 1 S. 2 GVG")], rechts_frei([
    *tafel("wl17", "Falscher Rechtsweg: Verweisung"),
    *w17,
    *neinz("keine Abweisung als unzulässig", w17_y + 40, "verw", "ExtraBold", 34, x=160),
    *okz("sondern Verweisung an das Zivilgericht", w17_y + 95, beim("verw", "verwiesen"), "ExtraBold", 34, x=160),
    *okz("Rechtshängigkeit bleibt bestehen", w17_y + 170, "verw2", "Bold", 32, x=160),
    zit("§ 17b Abs. 1 S. 2 GVG", 160, w17_y + 216, "verw2"),
    *requisit([("wl17", ("fluent-emoji-high-contrast", "classical-building", 110, BLAU), "Verwaltungsgericht", BLAU),
               ("wl17b", ("tabler", "arrows-split", 100, GELB), "verweist", GELB),
               ("verw", ("tabler", "gavel", 100, GRUEN), "Zivilgericht", GRUEN)]),
    *zwei([("wl17", "ruhig"), ("verw", "erklaert")], [("wl17", "sorge"), ("verw", "denkt"), ("verw2", "ruhig")]),
]))
assert w17_y + 260 <= 890, w17_y

# ===========================================================================================================================
# I Bedeutung: Handlungsform und Verfahrensrecht
# ===========================================================================================================================
PB = "Bedeutung"
folie([("bed", f"{PB} · nicht nur der Rechtsweg"), ("hf", f"{PB} › Handlungsform: VA oder Vertrag"),
       ("vv", f"{PB} › Verfahrensrecht: VwVfG")], rechts_frei([
    *tafel("bed", "Die Einordnung entscheidet mehr"),
    blk(110, 180, 1040, 76, GELB, "hf", [("Handlungsform: Verwaltungsakt oder Vertrag", "ExtraBold", 32, INK)]),
    z("Verwaltungsakt nur auf dem Gebiet des öffentlichen Rechts", 140, 275, "hf", "Bold", 30),
    zit("§ 35 S. 1 VwVfG", 140, 320, "hf"),
    *okz("hier: Kündigung des Pachtvertrags", 375, beim("hf", "Kleingarten"), "Bold", 30, x=180),
    blk(110, 470, 1040, 76, BLAU, "vv", [("Verfahrensrecht: Verwaltungsverfahrensgesetze", "ExtraBold", 32, INK)]),
    z("gelten nur für öffentlich-rechtliche Verwaltungstätigkeit", 140, 565, "vv", "Bold", 30),
    zit("§ 1 Abs. 1 VwVfG · Landesgesetze ebenso, z. B. § 1 Abs. 1 VwVfG NRW", 140, 610, "vv"),
    *neinz("hier: keine Anhörung nach § 28 VwVfG", 665, beim("vv", "Anhörung"), "Bold", 30, x=180),
    *requisit([("bed", ("tabler", "scale", 100, WEISS), "Folgen", WEISS),
               ("hf", ("fluent-emoji-high-contrast", "handshake", 110, GELB), "Vertrag statt VA", GELB),
               ("vv", ("tabler", "clipboard-list", 100, BLAU), "Verfahren", BLAU)]),
    *zwei([("bed", "ruhig"), ("hf", "erklaert"), ("vv", "froh")], [("bed", "liest"), ("vv", "denkt")]),
]))

# ===========================================================================================================================
# J Klausurtipp (Lexi)
# ===========================================================================================================================
els_k = [*tafel("tipp", "Klausurtipp: der Rechtsweg", fill=HELL), warnung_i(150, 225, "tipp", gr=26),
         z("Rechtsweg ausführlich nur bei echtem Problem", 200, 200, "tipp", "Bold", 32),
         blk(130, 300, 1020, 120, GELB, "k1", [("1. streitentscheidende Norm nennen", "ExtraBold", 32, INK),
                                               ("2. mit der modifizierten Subjektstheorie einordnen", "ExtraBold", 30, INK)]),
         blk(130, 460, 1020, 120, HELLROT, "k2", [("Nicht vom Absender täuschen lassen:", "ExtraBold", 32, INK),
                                                  ("Stadt beteiligt – noch kein öffentliches Recht", "ExtraBold", 30, INK)]),
         *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
         ns("Lexi", FX, FB, "tipp", GELB, d=0.2)]
folie([("tipp", "Klausurtipp · Rechtsweg nur, wenn problematisch"), ("k1", "Klausurtipp › Norm nennen und einordnen"),
       ("k2", "Klausurtipp › nicht vom Absender täuschen lassen")], els_k)

# ===========================================================================================================================
# K Prüfschema: Verwaltungsrechtsweg (Aufbau Punkt für Punkt)
# ===========================================================================================================================
REIHEN = [("q1", 0, "I. aufdrängende Sonderzuweisung? (z. B. § 54 Abs. 1 BeamtStG)"),
          ("q2", 0, "II. § 40 Abs. 1 S. 1 VwGO"),
          ("q2a", 1, "1. öffentlich-rechtliche Streitigkeit: streitentscheidende Norm bestimmen"),
          ("q2b", 2, "einordnen: modifizierte Subjektstheorie (h. M.)"),
          ("q2c", 2, "Sonderfälle: Zwei-Stufen-Theorie, Hausverbot, Fiskalverwaltung"),
          ("q2d", 1, "2. nichtverfassungsrechtlicher Art"),
          ("q2e", 1, "3. keine abdrängende Sonderzuweisung (z. B. § 40 Abs. 2 S. 1 VwGO)"),
          ("q3", 0, "III. Ergebnis – sonst Verweisung, § 17a Abs. 2 S. 1 GVG")]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Prüfschema: Verwaltungsrechtsweg"), 110, 90, "sch", 46)]
y = 200
for c, ebene, text in REIHEN:
    x = (130, 200, 270)[ebene]
    els_sch.append(z(text, x, y, c, ("ExtraBold", "Bold", "Regular")[ebene], (40, 36, 34)[ebene], rechts=1800,
                     farbe=(INK, INK, TEXT)[ebene]))
    y += {0: 92, 1: 80, 2: 72}[ebene]
assert y <= 960, y
folie([("sch", "Prüfschema"), ("q1", "Prüfschema › I. aufdrängende Sonderzuweisung"), ("q2", "Prüfschema › II. § 40 Abs. 1 S. 1 VwGO"),
       ("q2a", "Prüfschema › II. 1. öffentlich-rechtliche Streitigkeit"), ("q2b", "Prüfschema › II. 1. modifizierte Subjektstheorie"),
       ("q2c", "Prüfschema › II. 1. Sonderfälle"), ("q2d", "Prüfschema › II. 2. nichtverfassungsrechtlicher Art"),
       ("q2e", "Prüfschema › II. 3. keine abdrängende Sonderzuweisung"), ("q3", "Prüfschema › III. Ergebnis")], els_sch)

# ===========================================================================================================================
# L Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Nicht ", 0), ("wer", "a"), (" streitet, entscheidet,", 0)],
                 [("sondern nach welcher ", 0), ("Norm", "b"), (" gestritten wird.", 0)]], 750, 290, 42, "merke",
                {"a": beim("merke", "wer"), "b": beim("merke", "Norm")}),
    *markertext([[("Gilt sie für ", 0), ("jedermann", "c"), (":", 0)], [("Privatrecht.", 0)]], 750, 470, 42, "mk2",
                {"c": beim("mk2", "jedermann")}),
    *markertext([[("Berechtigt sie gerade den ", 0), ("Staat", "d"), (":", 0)], [("öffentliches Recht.", 0)]], 750, 640, 42,
                "mk3", {"d": beim("mk3", "Staat")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
