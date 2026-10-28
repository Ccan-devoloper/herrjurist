"""Folge 168 · Revisionsfrist StPO: Einlegung, Begründung, Wiedereinsetzung – Serienstandard Open Peeps (Katzenkönig).
Beispielfall: Die Strafkammer verurteilt Herrn Tiedemann am Montag, 18.5.2026, in seiner Anwesenheit; Rechtsanwältin Sternberg
legt am Dienstag, 26.5.2026 (Pfingstmontag!), elektronisch Revision ein; Zustellung des Urteils am Montag, 6.7.2026; die Kanzlei
notiert die Begründungsfrist für den 6.9. statt 6.8.2026; Fehler bemerkt am 10.8., Wiedereinsetzungsantrag am 12.8.2026.
Szenen laut ../SZENENPLAN.md: A1 Sitzungssaal, A2 Kanzlei, B Sachverhalt, C Aufbau, D Wortlautkarte § 341 Abs. 1, E Wortlautkarte
§ 32d S. 2, F1 Wortlautkarte § 43, F2 Kalender Mai 2026, G Wortlautkarte § 345 Abs. 1 mit Zeitstrahl, H Wortlautkarte § 345 Abs. 2,
§ 344, § 335, I Telefonat (Kanzlei/Wohnung), K Wortlautkarten §§ 44, 45, L Verteidigerverschulden und Lösung, M die Grenze
(Verfahrensrügen), N Merktabelle, O Klausurtipp (Lexi), P Prüfschema, Q Merksatz (Lexi).
Zwei Handlungsgeräusche (Umschlag, als das Urteil in der Kanzlei ankommt; Telefonklingeln, als Rechtsanwältin Sternberg
Herrn Tiedemann anruft; ../geraeusche_herkunft.json). Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen
glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz als eigene Kopie aus Folge 152 (gemeinsame Dateien unverändert); neu:
saal(), richterbank(), schreibtisch(), fristenkalender(), kalender(), markiere(), zeitstrahl(), tabelle().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut nach gesetze-im-internet.de (Abruf 04.10.2026)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_168/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_168/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def wortlaut(x, y, w, zeilen, quelle, cue, marken=(), size=32, bis=None):
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 04.10.2026), als Zitat mit Normangabe;
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 103/109/112/124) -----------------------------
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
    """Namensschild unter der Figur (ab ihrem ersten Auftritt, solange sie im Bild ist); das lange Schild
    „Rechtsanwältin Sternberg“ in 26 px, damit es neben der zweiten Figur Platz hat."""
    return pl(text, cx, unten + 22, cue, fill=fill, size=26 if text.startswith("Rechtsanw") else 30, anker="m", **k)


def okz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Haken davor (zur gesprochenen Bejahung)."""
    return [ok(x - 45, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]


def neinz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Kreuz davor (zur gesprochenen Verneinung)."""
    return [nein(x - 45, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]



# --- eigene Szenenbausteine (programmatisch, Palettenflächen, Tuschekontur) ---------------------------------------------------
BODEN_Y = 905                                # Boden = Unterkante der Figuren in den Fallszenen
FHA = 480                                    # Figurenhöhe in den Fallszenen
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
WAND = (238, 230, 214, 255)
HOLZD = (176, 122, 78, 255)


def _flaeche(w, h, zeichne):
    s = 2
    im = Image.new("RGBA", (w * s, h * s))
    zeichne(ImageDraw.Draw(im), s)
    return im.resize((w, h), Image.LANCZOS)


def boden(c, x0=60, x1=1860):
    return hart(linienzug([(x0, BODEN_Y), (x1, BODEN_Y)], c, breite=7, farbe=INK))


def saal(c):
    """Sitzungssaal (Grundform): Holzvertäfelung hinten, Boden."""
    def zz(dr, s):
        dr.rectangle((0, 0, 1800 * s, 330 * s), fill=WAND)
        dr.rectangle((0, 330 * s, 1800 * s, 525 * s), fill=(222, 196, 160, 255))
        for xs in range(0, 1800, 225):
            dr.line((xs * s, 330 * s, xs * s, 525 * s), fill=(190, 150, 110, 255), width=4 * s)
        dr.line((0, 330 * s, 1800 * s, 330 * s), fill=INK, width=4 * s)
    return hart(El(_flaeche(1800, 525, zz), 60, 380, c, "cut", 0.0, None, name="saal"))


def richterbank(c, x0=200, x1=900):
    """Erhöhte Richterbank (Holz, Tuschekontur) – verdeckt die Beine der Richterin."""
    w, h = x1 - x0, 290
    def zz(dr, s):
        dr.rounded_rectangle((3 * s, 0, (w - 3) * s, 34 * s), 8 * s, fill=HOLZ, outline=INK, width=5 * s)
        dr.rectangle((20 * s, 34 * s, (w - 20) * s, (h - 3) * s), fill=HOLZD, outline=INK, width=5 * s)
        for xs in range(120, w - 60, 160):
            dr.rounded_rectangle((xs * s, 70 * s, (xs + 100) * s, (h - 40) * s), 6 * s, outline=(120, 80, 50, 255), width=3 * s)
    return hart(El(_flaeche(w, h, zz), x0, BODEN_Y - h, c, "cut", 0.0, None, name="richterbank"))


def schreibtisch(c, x0, x1):
    w, h = x1 - x0, 170
    def zz(dr, s):
        dr.rounded_rectangle((3 * s, 0, (w - 3) * s, 28 * s), 6 * s, fill=HOLZ, outline=INK, width=5 * s)
        for xl in (30, w - 60):
            dr.rectangle((xl * s, 28 * s, (xl + 26) * s, (h - 3) * s), fill=HOLZ, outline=INK, width=4 * s)
    return hart(El(_flaeche(w, h, zz), x0, BODEN_Y - h, c, "cut", 0.0, None, name="schreibtisch"))


def fristenkalender(c, x0, y0, w=520, h=420):
    """Fristenkalender an der Kanzleiwand (Grundform: Blatt mit Kopfzeile und Linien)."""
    def zz(dr, s):
        dr.rounded_rectangle((3 * s, 3 * s, (w - 3) * s, (h - 3) * s), 14 * s, fill=WEISS, outline=INK, width=5 * s)
        dr.rounded_rectangle((3 * s, 3 * s, (w - 3) * s, 80 * s), 14 * s, fill=ROT, outline=INK, width=5 * s)
        for i in range(4):
            yl = 150 + i * 70
            dr.line((30 * s, yl * s, (w - 30) * s, yl * s), fill=(200, 200, 200, 255), width=3 * s)
        for xr in (90, w // 2, w - 90):
            dr.ellipse(((xr - 9) * s, -6 * s, (xr + 9) * s, 12 * s), fill=INK)
    els = [hart(El(_flaeche(w, h, zz), x0, y0, c, "cut", 0.0, None, name="fristenkalender"))]
    els.append(hart(z("Fristen", x0 + 30, y0 + 16, c, "ExtraBold", 38, farbe=WEISS, rechts=x0 + w)))
    return els


X1, X2 = 1395, 1730                         # zwei Figuren neben der Tafel (links Sternberg, rechts Tiedemann)
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"TI": "Herr Tiedemann", "SB": "Rechtsanwältin Sternberg", "RI": "Vorsitzende Richterin"}
NFARBE = {"TI": GELB, "SB": LILA, "RI": WEISS}


def stehend(k, x, folge, unten=930, hoehe=480, ns_size=30):
    return [*fig(k, x, unten, hoehe, folge), ns(NAME[k], x, unten, folge[0][0], NFARBE[k], d=0.1)]


def requisit(folge, px=PX):
    """Wechselndes Requisit über den Figuren: folge = [(cue, (set, icon, breite, fuell), pillentext, pillenfarbe)]."""
    els = []
    for i, (c, ic, txt, pf) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else None
        if ic:
            s_, n_, br, fu = ic
            els.append(ficon(s_, n_, px, PU, br, c, fuell=fu, bis=b))
        if txt:
            els.append(pl(txt, px, PY, c, fill=pf, size=28, anker="m", bis=b))
    return els


def zwei(folge_ti, folge_sb):
    """Herr Tiedemann und Rechtsanwältin Sternberg rechts neben der Tafel (blicken nach links zur Tafel)."""
    return [*stehend("SB", X1, folge_sb), *stehend("TI", X2, folge_ti)]


def allein(k, folge):
    return stehend(k, FX, folge)


# ===========================================================================================================================
# A1 Fall: Urteilsverkündung im Sitzungssaal
# ===========================================================================================================================
RX, TX, SX = 550, 1230, 1590                 # Richterin (blickt nach rechts), Herr Tiedemann, Rechtsanwältin Sternberg
folie([(NULL, "Fall · Im Sitzungssaal"), ("urteil", "Fall · Das Urteil"), ("anw", "Fall · anwesend bei der Verkündung"),
       ("ti1", "Fall · Revision!")], [
    saal(NULL),
    *fig("RI", RX, BODEN_Y, FHA, [(NULL, "ruhig_r"), ("urteil", "ernst_r")], erst="cut"),
    richterbank(NULL),
    boden(NULL),
    hart(ns("Vorsitzende Richterin", RX, BODEN_Y, NULL, WEISS)),
    hart(pl("Landgericht · Strafkammer", 70, 30, NULL, fill=GELB, size=38)),
    pl("Montag im Mai", 70, 110, NULL, fill=WEISS, size=34),
    pl("Urteil: Freiheitsstrafe wegen Betrugs", 70, 190, beim("urteil", "verurteilt"), fill=HELLROT, size=34),
    # Herr Tiedemann und seine Verteidigerin blicken zur Richterin, dann einander an
    *fig("TI", TX, BODEN_Y, FHA, [(NULL, "ruhig"), (beim("urteil", "verurteilt"), "schreck"), ("anw", "ernst")], bis="ti1", erst="cut"),
    hart(ns("Herr Tiedemann", TX, BODEN_Y, NULL, GELB)),
    pl("anwesend", TX, 300, beim("anw", "anwesend"), fill=GRUEN, size=30, anker="m", bis="ti1"),
    *fig("SB", SX, BODEN_Y, FHA, [(NULL, "ruhig"), ("urteil", "ernst")], bis="st1", erst="cut"),
    hart(ns("Rechtsanwältin Sternberg", SX, BODEN_Y, NULL, LILA)),
    pl("Verteidigerin", SX, 300, beim("anw", "Verteidigerin"), fill=LILA, size=30, anker="m", bis="ti1"),
    *redet("TI_redet_r", TX, BODEN_Y, FHA, "ti1", "st1"),
    blase("sprech", 600, 210, "ti1", 1080, 210, inhalt=["Das Urteil ist falsch.", "Das nehme ich nicht hin."], textsize=38,
          figur=("TI_redet_r", TX, BODEN_Y, FHA), bis="st1"),
    *fig("TI", TX, BODEN_Y, FHA, [("st1", "ernst_r")], erst="cut"),
    *redet("SB_redet", SX, BODEN_Y, FHA, "st1", "zust"),
    blase("sprech", 660, 230, "st1", 1500, 210, inhalt=["Dann legen wir Revision ein.", "Die Begründung folgt", "mit dem schriftlichen Urteil."],
          textsize=34, figur=("SB_redet", SX, BODEN_Y, FHA), bis="zust"),
])

# ===========================================================================================================================
# A2 Fall: in der Kanzlei – Zustellung und falsche Fristnotiz
# ===========================================================================================================================
KX0, KY0 = 140, 400                          # Fristenkalender an der Wand
SKX = 1560                                   # Rechtsanwältin Sternberg neben dem Schreibtisch
folie([("zust", "Fall · Die Zustellung"), ("notiz", "Fall · Der Fristenkalender"), ("frage", "Fall · Die Fragen")], [
    boden("zust"),
    schreibtisch("zust", 760, 1300),
    *fristenkalender("zust", KX0, KY0, h=400),
    hart(pl("Kanzlei Sternberg", 70, 30, "zust", fill=LILA, size=38)),
    *stehend("SB", SKX, [("zust", "ruhig"), ("notiz", "still"), ("frage", "ruhig")], unten=BODEN_Y),
    szene(ficon("tabler", "mail", 1030, BODEN_Y - 170, 110, beim("zust", "zugestellt"), fuell=WEISS, bis=beim("zust", "zugestellt", ende=True)),
          "168umschlag*", 1.0, 0.0),
    ficon("tabler", "mail-opened", 1030, BODEN_Y - 170, 110, beim("zust", "zugestellt", ende=True), fuell=WEISS, anim="cut"),
    pl("Urteil zugestellt: 7 Wochen später", 760, 110, beim("zust", "sieben"), fill=WEISS, size=34),
    z("Revisionsbegründung", KX0 + 30, KY0 + 105, "notiz", "Bold", 32, rechts=KX0 + 500),
    z("Tiedemann: 6.9.2026", KX0 + 30, KY0 + 175, beim("notiz", "eingetragen"), "ExtraBold", 38, rechts=KX0 + 500),
    linienzug([(KX0 + 20, KY0 + 240), (KX0 + 400, KY0 + 240)], "falsch", breite=6, farbe=DROT),
    pl("1 Monat zu spät", KX0 + 260, KY0 + 290, "falsch", fill=HELLROT, size=34, anker="m"),
    pl("Bis wann einlegen und begründen?", 70, 190, "frage", fill=PINK, size=36),
    pl("Was hilft, wenn die Frist versäumt ist?", 70, 270, "frage2", fill=PINK, size=36),
    ficon("tabler", "hourglass", 850, 335, 70, "frage2", fuell=GELB),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_168(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=34, zeilenabstand=1.30)
        els += e; y += 18
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_168("sv", [
    "Am Montag, 18. Mai 2026, verurteilt die Strafkammer des Landgerichts Herrn Tiedemann im ersten Rechtszug wegen "
    "Betrugs zu einer Freiheitsstrafe. Er ist bei der Verkündung anwesend und wird über das Rechtsmittel belehrt.",
    "Seine Verteidigerin, Rechtsanwältin Sternberg, legt am Dienstag, 26. Mai 2026, über das besondere elektronische "
    "Anwaltspostfach Revision ein. Das schriftliche Urteil wird ihr am Montag, 6. Juli 2026, zugestellt.",
    "In ihrer Kanzlei wird die Begründungsfrist versehentlich für den 6. September 2026 notiert. Am Montag, "
    "10. August 2026, bemerkt sie den Fehler und unterrichtet Herrn Tiedemann noch am selben Tag.",
], "War die Einlegung rechtzeitig, bis wann war zu begründen – und was kann Herr Tiedemann jetzt tun?")

# ===========================================================================================================================
# C Aufbau
# ===========================================================================================================================
folie([("aufbau", "Aufbau · Statthaftigkeit, § 333 StPO"), ("a1", "Aufbau · die Fristen"), ("a2", "Aufbau › 1. Einlegung"),
       ("a3", "Aufbau › 2. Begründung"), ("a4", "Aufbau › 3. Wiedereinsetzung")], rechts_frei([
    *tafel("aufbau", "Revision: die Fristen"),
    *okz("Statthaft gegen Urteile der Strafkammer, § 333 StPO", 180, "aufbau", "Bold", 34, x=160),
    zit("Was die Revision prüft: Video „Sachrüge vs. Verfahrensrüge“", 160, 232, beim("aufbau", "was")),
    z("Hier geht es um die Fristen:", 110, 310, "a1", "Bold", 36),
    blk(110, 380, 1040, 80, GELB, "a2", [("1. Einlegung", "ExtraBold", 36, INK)]),
    blk(110, 490, 1040, 80, BLAU, "a3", [("2. Begründung", "ExtraBold", 36, INK)]),
    blk(110, 600, 1040, 80, HELLGRUEN, "a4", [("3. Wiedereinsetzung", "ExtraBold", 36, INK)]),
    *requisit([("aufbau", ("tabler", "building-bank", 120, BLAU), "Strafkammer", WEISS),
               ("a2", ("tabler", "send", 100, GELB), "Einlegung", GELB),
               ("a3", ("tabler", "file-text", 100, WEISS), "Begründung", BLAU),
               ("a4", ("tabler", "arrow-back-up", 100, GRUEN), "Wiedereinsetzung", HELLGRUEN)]),
    *zwei([("aufbau", "ruhig"), ("a3", "skeptisch")], [("aufbau", "ruhig"), ("a2", "ernst")]),
]))

# ===========================================================================================================================
# D Wortlautkarte § 341 StPO: Einlegung
# ===========================================================================================================================
PA = "Einlegung"
W341 = ["„Die Revision muß bei dem Gericht, dessen Urteil angefochten",
        "wird, binnen einer Woche nach Verkündung des Urteils zu",
        "Protokoll der Geschäftsstelle oder schriftlich eingelegt werden.“"]
w341, w341_y = wortlaut(80, 170, 1100, W341, "§ 341 Abs. 1 StPO", "p341", marken=[
    (0, "bei dem Gericht", beim("p341", "Gericht")), (1, "binnen einer Woche", beim("p341", "Woche")),
    (1, "nach Verkündung", beim("p341", "Verkündung")), (2, "Protokoll der Geschäftsstelle", beim("p341", "Protokoll")),
    (2, "schriftlich", beim("p341", "schriftlich"))], size=32)
folie([("p341", f"{PA} › § 341 Abs. 1 StPO: eine Woche"), ("lg", f"{PA} › beim Landgericht"),
       ("abw", f"{PA} › abwesend: § 341 Abs. 2 StPO")], rechts_frei([
    *tafel("p341", "Einlegung: § 341 StPO"),
    *w341,
    blk(110, w341_y + 34, 1040, 80, GELB, "lg", [("Einlegung beim Landgericht, nicht beim BGH", "ExtraBold", 36, INK)]),
    z("§ 341 Abs. 2: Angeklagter bei der Verkündung", 110, w341_y + 160, "abw", "Bold", 34),
    z("nicht anwesend: Frist grundsätzlich ab Zustellung", 110, w341_y + 208, beim("abw", "beginnt"), size=34),
    *requisit([("p341", ("tabler", "send", 100, GELB), "1 Woche ab Verkündung", GELB),
               ("lg", ("tabler", "building-bank", 120, BLAU), "Landgericht", WEISS),
               ("abw", ("tabler", "mail", 100, WEISS), "abwesend: ab Zustellung", WEISS)]),
    *zwei([("p341", "ruhig"), ("abw", "skeptisch")], [("p341", "ruhig"), ("lg", "ernst")]),
]))

# ===========================================================================================================================
# E Wortlautkarte § 32d S. 2 StPO: elektronische Form
# ===========================================================================================================================
W32 = ["„Verteidiger und Rechtsanwälte sollen … Die folgenden",
       "Dokumente müssen sie elektronisch übermitteln: …",
       "2. die Revision, ihre Begründung, ihre Rücknahme und",
       "die Gegenerklärung, …“"]
w32, w32_y = wortlaut(80, 245, 1100, W32, "§ 32d S. 2 Nr. 2 StPO", "p32d2", marken=[
    (1, "müssen", beim("p32d2", "müssen")), (1, "elektronisch", beim("p32d2", "elektronisch")),
    (2, "2. die Revision, ihre Begründung", beim("p32d2", "Revision"))], size=34)
folie([("p32d", f"{PA} › Form: schriftlich"), ("p32d2", f"{PA} › Form: § 32d S. 2 StPO"),
       ("seit", f"{PA} › elektronisch seit 1.1.2022"), ("fax", f"{PA} › Fax: unwirksam")], rechts_frei([
    *tafel("p32d", "Form: § 32d S. 2 StPO"),
    z("Schriftlich heißt für die Verteidigerin: elektronisch.", 110, 175, "p32d", "Bold", 34),
    *w32,
    *okz("Pflicht seit 1.1.2022", w32_y + 30, "seit", "Bold", 34, x=160),
    zit("BGH, Beschl. v. 7.3.2023 – 6 StR 74/23, Rn. 4", 160, w32_y + 80, "seit"),
    *neinz("Fax der Verteidigerin: unwirksam", w32_y + 140, "fax", "Bold", 34, x=160),
    zit("BGH, Beschl. v. 9.8.2022 – 6 StR 268/22, Rn. 3", 160, w32_y + 190, "fax"),
    *requisit([("p32d", ("tabler", "writing-sign", 100, WEISS), "schriftlich", WEISS),
               ("p32d2", ("tabler", "device-laptop", 120, BLAU), "elektronisch", BLAU),
               ("fax", ("tabler", "printer-off", 100, HELLROT), "Fax: unwirksam", HELLROT)]),
    *allein("SB", [("p32d", "ruhig"), ("seit", "froh"), ("fax", "ernst")]),
]))

# ===========================================================================================================================
# F1 Wortlautkarte § 43 StPO: Fristberechnung
# ===========================================================================================================================
W43 = ["„(1) Eine Frist, die nach Wochen oder Monaten bestimmt ist,",
       "endet mit Ablauf des Tages der letzten Woche oder des letzten",
       "Monats, der durch seine Benennung oder Zahl dem Tag entspricht,",
       "an dem die Frist begonnen hat; …",
       "(2) Fällt das Ende einer Frist auf einen Sonntag, einen",
       "allgemeinen Feiertag oder einen Sonnabend, so endet die Frist",
       "mit Ablauf des nächsten Werktages.“"]
w43, w43_y = wortlaut(80, 165, 1100, W43, "§ 43 StPO", "frist1", marken=[
    (0, "Wochen", beim("p43", "Wochenfrist")), (2, "Benennung", beim("p43", "Benennung")),
    (0, "Monaten", beim("p43", "Monatsfrist")), (2, "Zahl", beim("p43", "Zahl"))], size=30)
folie([("frist1", f"{PA} › Fristberechnung, § 43 StPO"), ("p43", f"{PA} › § 43 Abs. 1: Benennung oder Zahl")], rechts_frei([
    *tafel("frist1", "Fristberechnung: § 43 StPO"),
    *w43,
    blk(110, w43_y + 30, 505, 80, GELB, beim("p43", "Benennung"), [("Woche: gleicher Wochentag", "ExtraBold", 30, INK)]),
    blk(645, w43_y + 30, 505, 80, BLAU, beim("p43", "Zahl"), [("Monat: gleiche Zahl", "ExtraBold", 30, INK)]),
    *requisit([("frist1", ("tabler", "calendar-event", 100, WEISS), "Wann endet die Woche?", WEISS),
               (beim("p43", "Benennung"), ("tabler", "calendar-week", 100, GELB), "gleicher Wochentag", GELB)]),
    *allein("SB", [("frist1", "skeptisch"), ("p43", "ruhig")]),
]))

# ===========================================================================================================================
# F2 Kalender Mai 2026: Pfingstmontag
# ===========================================================================================================================
KW_, KH_, KCX, KCY = 148, 86, 115, 222       # Kalenderzelle: Breite, Höhe, links, oben
TAGE = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
MAI = [[(27, 0), (28, 0), (29, 0), (30, 0), (1, 1), (2, 1), (3, 1)], [(d, 1) for d in range(4, 11)],
       [(d, 1) for d in range(11, 18)], [(d, 1) for d in range(18, 25)], [(d, 1) for d in range(25, 32)]]
import datetime as _dt
assert _dt.date(2026, 5, 18).weekday() == 0 and _dt.date(2026, 5, 25).weekday() == 0 and _dt.date(2026, 5, 1).weekday() == 4
assert _dt.date(2026, 4, 5) + _dt.timedelta(50) == _dt.date(2026, 5, 25)          # Ostern 5.4.2026 → Pfingstmontag 25.5.
assert _dt.date(2026, 7, 6).weekday() == 0 and _dt.date(2026, 8, 6).weekday() == 3 and _dt.date(2026, 8, 10).weekday() == 0
assert _dt.date(2026, 8, 12).weekday() == 2 and (_dt.date(2026, 7, 6) - _dt.date(2026, 5, 18)).days == 49


def zelle(tag):
    for r, w in enumerate(MAI):
        for c, (d, im_m) in enumerate(w):
            if d == tag and im_m:
                return KCX + c * KW_, KCY + r * KH_
    raise KeyError(tag)


def kalender(cue):
    s = 2
    im = Image.new("RGBA", (7 * KW_ * s + 8 * s, (5 * KH_ + 50) * s))
    dr = ImageDraw.Draw(im)
    fk, fz = F("Bold", 28 * s), F("Bold", 34 * s)
    for c, t in enumerate(TAGE):
        dr.text(((c * KW_ + KW_ / 2) * s, 22 * s), glyphen(t), font=fk, fill=TEXT if c >= 5 else INK, anchor="mm")
    for r, w in enumerate(MAI):
        for c, (d, im_m) in enumerate(w):
            x0, y0 = c * KW_ * s + 4 * s, (50 + r * KH_) * s
            dr.rounded_rectangle((x0, y0, x0 + (KW_ - 8) * s, y0 + (KH_ - 8) * s), 10 * s,
                                 fill=(255, 255, 255, 255) if im_m else (238, 238, 234, 255), outline=INK, width=3 * s)
            dr.text((x0 + 14 * s, y0 + 6 * s), str(d), font=fz, fill=INK if im_m else (150, 150, 150, 255))
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    return El(im, KCX - 4, KCY - 50, cue, "fade", 0.0, None, name="kalender")


def markiere(tag, cue, fill, text=None, bis=None):
    x, y = zelle(tag)
    im = Image.new("RGBA", (KW_ - 8, KH_ - 8))
    d_ = ImageDraw.Draw(im)
    d_.rounded_rectangle((0, 0, im.width - 1, im.height - 1), 10, fill=fill[:3] + (255,), outline=INK, width=3)
    d_.text((14, 6), str(tag), font=F("Bold", 34), fill=INK)
    if text:
        d_.text((im.width - 8, im.height - 5), glyphen(text), font=F("Bold", 26), fill=INK, anchor="rd")
    return El(im, x, y, cue, "pop", 0.0, bis, name=f"tag:{tag}")


folie([("mo", f"{PA} › Urteil: Mo, 18.5.2026"), (beim("mo", "fünfundzwanzigsten"), f"{PA} › 1 Woche: Mo, 25.5.2026?"), ("pfi", f"{PA} › Pfingstmontag"),
       ("p432", f"{PA} › § 43 Abs. 2: nächster Werktag"), ("di", f"{PA} › Ende: Di, 26.5.2026, 24 Uhr"),
       ("rz", f"{PA} › eingelegt am 26.5.2026 (+)")], rechts_frei([
    *tafel("mo", "Einlegungsfrist: Mai 2026"),
    kalender("mo"),
    markiere(18, beim("mo", "Montag"), GELB, "Urteil"),
    markiere(25, beim("mo", "fünfundzwanzigsten"), HELLGRUEN, "1 Woche", bis="pfi"),
    markiere(25, "pfi", HELLROT, "Feiertag"),
    markiere(26, beim("di", "Dienstag"), HELLGRUEN, "Ende"),
    ok(zelle(26)[0] + 92, zelle(26)[1] + 18, "rz", gr=20),
    z("§ 43 Abs. 1: Montag + 1 Woche = Montag, 25.5.", 110, 672, beim("mo", "endet"), "Bold", 32),
    z("§ 43 Abs. 2: Feiertag, Sonnabend, Sonntag: nächster Werktag", 110, 720, "p432", "Bold", 30),
    blk(110, 776, 1040, 80, GELB, beim("di", "Dienstag"), [("Einlegung bis Di, 26.5.2026, 24 Uhr", "ExtraBold", 36, INK)]),
    *requisit([("mo", ("tabler", "calendar-event", 100, WEISS), "Urteil: Mo, 18.5.", GELB),
               ("pfi", ("tabler", "calendar-off", 100, HELLROT), "Pfingstmontag", HELLROT),
               (beim("di", "Dienstag"), ("tabler", "alarm", 100, GELB), "Di, 26.5., 24 Uhr", GELB),
               ("rz", ("tabler", "calendar-check", 100, GRUEN), "eingelegt: rechtzeitig", GRUEN)]),
    *allein("SB", [("mo", "ruhig"), ("pfi", "schreck"), ("di", "ernst"), ("rz", "froh")]),
]))

# ===========================================================================================================================
# G Wortlautkarte § 345 Abs. 1 StPO und Zeitstrahl Juli/August
# ===========================================================================================================================
PB = "Begründung"
W345 = ["„Die Revisionsanträge und ihre Begründung sind spätestens binnen",
        "eines Monats nach Ablauf der Frist zur Einlegung des Rechtsmittels",
        "bei dem Gericht, dessen Urteil angefochten wird, anzubringen. …",
        "War bei Ablauf der Frist zur Einlegung des Rechtsmittels das Urteil",
        "noch nicht zugestellt, so beginnt die Frist mit der Zustellung",
        "des Urteils …“"]
w345, w345_y = wortlaut(80, 160, 1100, W345, "§ 345 Abs. 1 S. 1, 3 StPO", "p345", marken=[
    (0, "binnen", beim("p345a", "binnen")), (1, "eines Monats", beim("p345a", "Monats")),
    (1, "nach Ablauf der Frist zur Einlegung", beim("p345a", "Ablauf")),
    (4, "noch nicht zugestellt", beim("p345c", "zugestellt")), (4, "mit der Zustellung", beim("p345c", "Zustellung")),
    (5, "des Urteils", beim("p345c", "Zustellung"))], size=30)
ZY = 720                                     # Zeitstrahl: Höhe der Linie


def zx(tag):
    """x-Position eines Datums auf dem Zeitstrahl (26.5.–6.9.2026)."""
    return 170 + (_dt.date(2026, *tag) - _dt.date(2026, 5, 26)).days * 9.0


def punkt(tag, oben, unten, cue, fill, bis=None, rot=False):
    x = zx(tag)
    r = 16
    im = Image.new("RGBA", (2 * r + 4, 2 * r + 4))
    ImageDraw.Draw(im).ellipse((2, 2, 2 * r + 2, 2 * r + 2), fill=fill[:3] + (255,), outline=INK, width=4)
    els = [El(im, x - r - 2, ZY - r - 2, cue, "pop", 0.0, bis, name=f"punkt:{tag}"),
           z(oben, x - F("ExtraBold", 30).getlength(oben) / 2, ZY - 70, cue, "ExtraBold", 30, farbe=DROT if rot else INK, bis=bis),
           z(unten, x - F("Bold", 26).getlength(unten) / 2, ZY + 30, cue, "Bold", 26, farbe=TEXT, bis=bis)]
    return els


folie([("p345", f"{PB} › § 345 Abs. 1 StPO: ein Monat"), ("p345c", f"{PB} › später zugestellt: ab Zustellung"),
       ("lang", f"{PB} › Verlängerung, § 345 Abs. 1 S. 2"), ("zust2", f"{PB} › Zustellung: Mo, 6.7.2026"),
       ("aug", f"{PB} › Ende: Do, 6.8.2026"), ("sept", f"{PB} › notiert: 6.9. – versäumt (-)")], rechts_frei([
    *tafel("p345", "Begründung: § 345 Abs. 1 StPO"),
    *w345,
    z("S. 2: Verlängerung nur, wenn das Urteil erst nach 21 Wochen", 110, w345_y + 18, "lang", size=28),
    z("zu den Akten kommt – hier nicht", 110, w345_y + 56, beim("lang", "Wochen"), size=28),
    linienzug([(130, ZY), (1150, ZY)], "zust2", breite=5),
    *punkt((5, 26), "26.5.", "Einlegungsfrist", "zust2", WEISS),
    *punkt((7, 6), "Mo, 6.7.", "Zustellung", beim("zust2", "Montag"), GELB),
    linienzug([(zx((7, 6)), ZY + 78), (zx((8, 6)), ZY + 78)], "mon", breite=4, farbe=INK),
    z("1 Monat", (zx((7, 6)) + zx((8, 6))) / 2 - 50, ZY + 88, "mon", "Bold", 26),
    *punkt((8, 6), "Do, 6.8.", "Fristende", beim("aug", "Donnerstag"), HELLGRUEN),
    *punkt((9, 6), "6.9.", "notiert", "sept", HELLROT, rot=True),
    nein(zx((9, 6)) - 18, ZY - 8, beim("sept", "versäumt"), gr=22),
    *requisit([("p345", ("tabler", "file-text", 100, WEISS), "1 Monat", BLAU),
               ("p345c", ("tabler", "mail-opened", 100, WEISS), "ab Zustellung", WEISS),
               ("zust2", ("tabler", "mail-opened", 100, GELB), "zugestellt: 6.7.", GELB),
               ("aug", ("tabler", "alarm", 100, GELB), "Ende: Do, 6.8.", HELLGRUEN),
               ("sept", ("tabler", "calendar-x", 100, HELLROT), "Frist versäumt", HELLROT)]),
    *allein("SB", [("p345", "ruhig"), ("lang", "skeptisch"), ("aug", "ernst"), ("sept", "schreck")]),
]))

# ===========================================================================================================================
# H Wortlautkarte § 345 Abs. 2 StPO; § 344; § 335
# ===========================================================================================================================
W3452 = ["„Seitens des Angeklagten kann dies nur in einer von dem",
         "Verteidiger oder einem Rechtsanwalt unterzeichneten Schrift",
         "oder zu Protokoll der Geschäftsstelle geschehen.“"]
w3452, w3452_y = wortlaut(80, 165, 1100, W3452, "§ 345 Abs. 2 StPO", "p3452", marken=[
    (1, "Verteidiger", beim("p3452", "Verteidiger")), (1, "oder einem Rechtsanwalt", beim("p3452", "Rechtsanwalt")),
    (1, "unterzeichneten Schrift", beim("p3452", "unterzeichneten")), (2, "zu Protokoll der Geschäftsstelle", beim("p3452", "Protokoll"))],
    size=32)
folie([("p3452", f"{PB} › Form: § 345 Abs. 2 StPO"), ("brief", f"{PB} › eigener Brief reicht nicht"),
       ("p344", f"{PB} › Inhalt: § 344 StPO"), ("spr", "Sprungrevision, § 335 StPO")], rechts_frei([
    *tafel("p3452", "Form und Inhalt: §§ 345, 344"),
    *w3452,
    *neinz("Eigener Brief von Herrn Tiedemann: reicht nicht", w3452_y + 30, "brief", "Bold", 34, x=160),
    z("§ 344 Abs. 2: Verfahrensrüge mit allen Tatsachen", 110, w3452_y + 110, beim("p344", "Verfahrensrüge"), "Bold", 32),
    z("Sachrüge: die allgemeine Rüge genügt", 110, w3452_y + 158, beim("p344", "Sachrüge"), "Bold", 32),
    blk(110, w3452_y + 235, 1040, 80, LILA, "spr", [("§ 335: Sprungrevision – dieselben Fristen", "ExtraBold", 34, INK)]),
    z("gegen Urteile, gegen die Berufung zulässig ist", 110, w3452_y + 330, beim("spr", "Berufung"), size=32),
    *requisit([("p3452", ("tabler", "signature", 100, WEISS), "unterzeichnet", WEISS),
               ("brief", ("tabler", "mail", 100, HELLROT), "eigener Brief: nein", HELLROT),
               ("p344", ("tabler", "list-check", 100, WEISS), "Inhalt: § 344", BLAU),
               ("spr", ("tabler", "arrow-bounce", 100, LILA), "Sprungrevision", LILA)]),
    *allein("TI", [("p3452", "ruhig"), ("brief", "sorge"), ("p344", "skeptisch"), ("spr", "ruhig")]),
]))

# ===========================================================================================================================
# I Fall: das Telefonat am 10. August (Kanzlei | Wohnung)
# ===========================================================================================================================
SL, TR = 640, 1460                            # Sternberg links (blickt nach rechts), Tiedemann rechts (blickt nach links)
folie([("entd", "Fall · 10. August: der Fehler"), ("ti2", "Fall · Ist die Revision verloren?"), ("st2", "Fall · Wiedereinsetzung!")], [
    boden("entd", 60, 930), boden("entd", 990, 1860),
    hart(linienzug([(960, 330), (960, 960)], "entd", breite=5, farbe=TEXT)),
    hart(pl("Kanzlei", 70, 30, "entd", fill=LILA, size=38)),
    hart(pl("Zuhause", 1010, 30, "entd", fill=GELB, size=38)),
    schreibtisch("entd", 120, 470),
    ficon("tabler", "calendar-x", 300, BODEN_Y - 172, 100, "entd", fuell=HELLROT),
    ficon("tabler", "sofa", 1720, BODEN_Y, 220, "entd", fuell=BLAU),
    ficon("tabler", "lamp-2", 1150, BODEN_Y, 150, "entd", fuell=GELB),
    pl("Mo, 10.8.2026: Fehler bemerkt", 70, 110, beim("entd", "bemerkt"), fill=HELLROT, size=34, bis="st2"),
    *stehend("SB", SL, [("entd", "schreck_r"), (beim("entd", "ruft"), "ernst_r")], unten=BODEN_Y),
    *stehend("TI", TR, [("entd", "ruhig")], unten=BODEN_Y),
    ficon("tabler", "phone-call", SL + 150, 470, 70, beim("entd", "ruft"), fuell=WEISS),
    szene(ficon("tabler", "phone-ringing", TR - 150, 470, 70, beim("entd", "ruft"), fuell=GELB), "168telefon*", 1.0, 0.0),
    *redet("TI_redet2", TR, BODEN_Y, FHA, "ti2", "st2"),
    blase("sprech", 560, 170, "ti2", 1400, 220, inhalt=["Ist meine Revision", "jetzt verloren?"], textsize=38,
          figur=("TI_redet2", TR, BODEN_Y, FHA), bis="st2"),
    *fig("SB", SL, BODEN_Y, FHA, [("ti2", "ernst_r")], erst="cut", bis="st2"),
    *redet("SB_redet2_r", SL, BODEN_Y, FHA, "st2", "p44"),
    blase("sprech", 620, 230, "st2", 560, 220, inhalt=["Nein. Der Fehler liegt", "bei uns. Wir beantragen", "Wiedereinsetzung."],
          textsize=34, figur=("SB_redet2_r", SL, BODEN_Y, FHA), bis="p44"),
    *fig("TI", TR, BODEN_Y, FHA, [("st2", "sorge"), (beim("st2", "Wiedereinsetzung"), "froh")], erst="cut"),
])

# ===========================================================================================================================
# K Wortlautkarten §§ 44, 45 StPO: Wiedereinsetzung
# ===========================================================================================================================
PW = "Wiedereinsetzung"
W44 = ["„War jemand ohne Verschulden verhindert, eine Frist einzuhalten,",
       "so ist ihm auf Antrag Wiedereinsetzung in den vorigen Stand zu",
       "gewähren. …“"]
w44, w44_y = wortlaut(80, 160, 1100, W44, "§ 44 S. 1 StPO", "p44", marken=[
    (0, "ohne Verschulden", beim("p44", "ohne")), (1, "auf Antrag", beim("p44", "Antrag")),
    (1, "Wiedereinsetzung", beim("p44", "Wiedereinsetzung"))], size=30)
W45 = ["„(1) Der Antrag auf Wiedereinsetzung in den vorigen Stand ist binnen",
       "einer Woche nach Wegfall des Hindernisses … zu stellen …",
       "(2) Die Tatsachen zur Begründung des Antrags sind … glaubhaft zu",
       "machen. Innerhalb der Antragsfrist ist die versäumte Handlung",
       "nachzuholen. …“"]
w45, w45_y = wortlaut(80, w44_y + 24, 1100, W45, "§ 45 StPO", "p45", marken=[
    (1, "einer Woche nach Wegfall des Hindernisses", beim("p45", "Woche")), (2, "glaubhaft zu", beim("glaub", "glaubhaft")),
    (3, "machen", beim("glaub", "glaubhaft")), (3, "Innerhalb der Antragsfrist", beim("nach", "innerhalb")),
    (3, "versäumte Handlung", beim("nach", "versäumte")), (4, "nachzuholen", beim("nach", "nachzuholen"))], size=30)
assert w45_y <= 880, w45_y
folie([("p44", f"{PW} › § 44 S. 1 StPO: ohne Verschulden"), ("p45", f"{PW} › § 45 Abs. 1 StPO: eine Woche"),
       ("glaub", f"{PW} › Glaubhaftmachung, § 45 Abs. 2 S. 1"), ("nach", f"{PW} › Nachholung, § 45 Abs. 2 S. 2")], rechts_frei([
    *tafel("p44", "Wiedereinsetzung: §§ 44, 45"),
    *w44, *w45,
    *requisit([("p44", ("tabler", "arrow-back-up", 100, GRUEN), "ohne Verschulden", HELLGRUEN),
               ("p45", ("tabler", "hourglass", 90, GELB), "1 Woche ab Wegfall", GELB),
               ("glaub", ("tabler", "file-certificate", 100, WEISS), "glaubhaft machen", WEISS),
               ("nach", ("tabler", "send", 100, BLAU), "Begründung nachholen", BLAU)]),
    *zwei([("p44", "sorge"), ("p45", "ruhig")], [("p44", "ruhig"), ("nach", "ernst")]),
]))

# ===========================================================================================================================
# L Verschulden der Kanzlei – Lösung
# ===========================================================================================================================
folie([("zur", f"{PW} › Verschulden der Kanzlei?"), ("zur2", f"{PW} › nicht zugerechnet"),
       ("auftr", f"{PW} › kein eigenes Verschulden (+)"), ("kennt", f"{PW} › Wochenfrist ab 10.8.2026"),
       ("antr", f"{PW} › Antrag am 12.8.2026 (+)"), ("gew", f"{PW} › zu gewähren (+)")], rechts_frei([
    *tafel("zur", "Verschulden der Kanzlei?"),
    z("Anders als im Zivilprozess (§ 85 Abs. 2 ZPO):", 110, 180, beim("zur2", "Anders"), "Bold", 32),
    *okz("dem Angeklagten grundsätzlich nicht zugerechnet", 228, beim("zur2", "zugerechnet"), "ExtraBold", 34, x=160),
    zit("BGH 6 StR 268/22, Rn. 4; BGH 4 StR 134/26, Rn. 1", 160, 280, beim("zur2", "Bundesgerichtshof")),
    *okz("Auftrag rechtzeitig erteilt: kein eigenes Verschulden", 345, "auftr", "Bold", 32, x=160),
    z("Wochenfrist ab Kenntnis von Herrn Tiedemann: 10.8.2026", 110, 420, "kennt", "Bold", 32),
    zit("BGH, Beschl. v. 9.12.2025 – 6 StR 331/25, Rn. 5", 110, 466, beim("kennt", "Maßgeblich")),
    z("Mi, 12.8.2026: Antrag, anwaltliche Versicherung,", 110, 530, "antr", "Bold", 32),
    z("Begründung elektronisch nachgereicht", 110, 576, beim("antr", "reicht"), size=32),
    blk(110, 650, 1040, 80, HELLGRUEN, "gew", [("Wiedereinsetzung ist zu gewähren", "ExtraBold", 36, INK)]),
    *requisit([("zur", ("tabler", "scale", 100, WEISS), "Kanzleiversehen", HELLROT),
               ("auftr", ("tabler", "user-check", 100, GRUEN), "kein eigenes Verschulden", HELLGRUEN),
               ("kennt", ("tabler", "phone-call", 100, WEISS), "Kenntnis: 10.8.", WEISS),
               ("antr", ("tabler", "send", 100, BLAU), "Antrag: 12.8.", BLAU),
               ("gew", ("tabler", "shield-check", 100, GRUEN), "Wiedereinsetzung (+)", HELLGRUEN)]),
    *zwei([("zur", "sorge"), ("auftr", "ruhig"), ("gew", "froh")], [("zur", "still"), ("antr", "ernst"), ("gew", "froh")]),
]))

# ===========================================================================================================================
# M Die Grenze: Verfahrensrügen nachschieben
# ===========================================================================================================================
folie([("grenze", f"{PW} › die Grenze"), ("gr1", f"{PW} › Verfahrensrügen nachschieben? (-)"),
       ("gr2", f"{PW} › §§ 344, 345 nicht unterlaufen"), ("gr3", f"{PW} › Ausnahme: rechtliches Gehör")], rechts_frei([
    *tafel("grenze", "Die Grenze: Rügen nachschieben?", fill=HELL),
    warnung_i(150, 205, "grenze", gr=24),
    z("Revision fristgerecht begründet, etwa nur mit der Sachrüge", 200, 182, beim("gr1", "fristgerecht"), "Bold", 30),
    *neinz("Wiedereinsetzung für neue Verfahrensrügen: grundsätzlich nein", 250, beim("gr1", "grundsätzlich"), "ExtraBold", 30, x=200),
    zit("BGH, Beschl. v. 19.6.2024 – 5 StR 442/23, Rn. 6", 200, 300, beim("gr1", "nachzuschieben")),
    z("Sie darf §§ 344 Abs. 2 S. 2, 345 nicht unterlaufen.", 200, 370, "gr2", "Bold", 32),
    blk(130, 450, 1020, 80, HELLGRUEN, "gr3", [("Ausnahme: rechtliches Gehör, Art. 103 Abs. 1 GG", "ExtraBold", 32, INK)]),
    z("z. B. Sitzungsprotokoll trotz Bemühens nicht rechtzeitig da", 130, 560, beim("gr3", "Sitzungsprotokoll"), size=32),
    zit("BGH, Beschl. v. 8.1.2026 – 3 StR 368/25, Rn. 2", 130, 608, beim("gr3", "Sitzungsprotokoll")),
    *requisit([("grenze", ("tabler", "alert-triangle", 100, GELB), "Achtung, Grenze", HELLROT),
               ("gr1", ("tabler", "file-x", 100, HELLROT), "Rügen nachschieben: nein", HELLROT),
               ("gr3", ("tabler", "ear", 100, GRUEN), "rechtliches Gehör", HELLGRUEN)]),
    *allein("SB", [("grenze", "skeptisch"), ("gr1", "ernst"), ("gr3", "ruhig")]),
]))

# ===========================================================================================================================
# N Merktabelle: die Fristen auf einen Blick
# ===========================================================================================================================
TAB = [("tb1", "Einlegung", ["1 Woche ab Verkündung"], "§ 341 Abs. 1", GELB),
       ("tb2", "Begründung", ["1 Monat nach der Einlegungsfrist;", "bei späterer Zustellung ab Zustellung"], "§ 345 Abs. 1", BLAU),
       ("tb3", "Wiedereinsetzung", ["1 Woche ab Wegfall des Hindernisses"], "§ 45 Abs. 1", HELLGRUEN)]
els_tab = [karte(60, 50, 1800, 940, "tab"), titel(glyphen("Die Fristen auf einen Blick"), 110, 90, "tab", 46),
           z("Frist", 130, 185, "tab", "ExtraBold", 32, farbe=TEXT, rechts=1800),
           z("Dauer und Beginn", 560, 185, "tab", "ExtraBold", 32, farbe=TEXT, rechts=1800),
           z("Norm (StPO)", 1450, 185, "tab", "ExtraBold", 32, farbe=TEXT, rechts=1800),
           linienzug([(110, 240), (1810, 240)], "tab", breite=3)]
y = 270
for c, name, dauer, norm, fill in TAB:
    h = 70 + 48 * (len(dauer) - 1) + 40
    els_tab.append(karte(110, y, 1700, h, c, fill=fill, rund=18, schatten=6, rand=4))
    els_tab.append(z(name, 140, y + 30, c, "ExtraBold", 38, rechts=1800))
    for j, t in enumerate(dauer):
        els_tab.append(z(t, 560, y + 32 + 48 * j, c, "Bold", 36, rechts=1420))
    els_tab.append(z(norm, 1450, y + 32, c, "Bold", 36, rechts=1800))
    y += h + 40
assert y <= 960, y
folie([("tab", "Merktabelle · die Fristen"), ("tb1", "Merktabelle · Einlegung"), ("tb2", "Merktabelle · Begründung"),
       ("tb3", "Merktabelle · Wiedereinsetzung")], els_tab)

# ===========================================================================================================================
# O Klausurtipp (Lexi): der Fristen-Check
# ===========================================================================================================================
SCHRITTE = [("Verkündung", "k1"), ("Einlegung", beim("k1", "Einlegung")), ("Zustellung", beim("k1", "Zustellung")),
            ("Begründung", beim("k1", "Begründung"))]
els_k = [*tafel("tipp", "Klausurtipp: der Fristen-Check", fill=HELL), warnung_i(150, 225, "tipp", gr=26),
         z("Leg dir einen Zeitstrahl an:", 200, 200, "k1", "Bold", 36),
         linienzug([(170, 340), (1130, 340)], "k1", breite=5)]
for i, (t, c) in enumerate(SCHRITTE):
    x = 240 + i * 270
    r = 14
    im = Image.new("RGBA", (2 * r + 4, 2 * r + 4))
    ImageDraw.Draw(im).ellipse((2, 2, 2 * r + 2, 2 * r + 2), fill=GELB[:3] + (255,), outline=INK, width=4)
    els_k.append(El(im, x - r - 2, 340 - r - 2, c, "pop", 0.0, None, name=f"schritt:{t}"))
    els_k.append(z(t, x - F("Bold", 30).getlength(t) / 2, 370, c, "Bold", 30))
els_k += [z("Jedes Fristende mit Wochentag ausrechnen;", 200, 470, "k2", "Bold", 34),
          z("Wochenende und Feiertag prüfen (§ 43 Abs. 2)", 200, 520, beim("k2", "Wochenende"), size=34),
          linienzug([(130, 600), (1130, 600)], "k3", breite=3),
          z("Frist versäumt?", 200, 625, "k3", "Bold", 36),
          z("Wiedereinsetzung genau an dieser Stelle prüfen", 200, 680, beim("k3", "Wiedereinsetzung"), size=34),
          *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
          ns("Lexi", FX, FB, "tipp", GELB, d=0.2)]
folie([("tipp", "Klausurtipp · der Fristen-Check"), ("k2", "Klausurtipp · Wochentag, Wochenende, Feiertag"),
       ("k3", "Klausurtipp · versäumt: Wiedereinsetzung")], els_k)

# ===========================================================================================================================
# P Prüfschema
# ===========================================================================================================================
REIHEN = [("s1", 0, "I. Statthaftigkeit, §§ 333, 335 StPO", True),
          ("s2", 0, "II. Berechtigung und Beschwer", True),
          ("s3", 0, "III. Einlegung, § 341 StPO", True),
          (beim("s3", "Gericht"), 1, "beim Gericht, dessen Urteil angefochten wird", False),
          (beim("s3", "Frist"), 1, "1 Woche ab Verkündung (§ 43 StPO)", False),
          (beim("s3", "Form"), 1, "zu Protokoll oder schriftlich; Verteidiger: elektronisch, § 32d S. 2", False),
          ("s4", 0, "IV. Begründung, §§ 344, 345 StPO", True),
          (beim("s4", "Frist"), 1, "1 Monat nach der Einlegungsfrist, bei späterer Zustellung ab Zustellung", False),
          (beim("s4", "Form"), 1, "Form: § 345 Abs. 2 StPO; Inhalt: § 344 StPO", False),
          ("s5", 0, "V. Bei Versäumung: Wiedereinsetzung, §§ 44, 45 StPO", True)]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfschema: Zulässigkeit der Revision"), 110, 90, "sch", 46),
           z("Fristen, Form und Wiedereinsetzung", 110, 160, "sch", "Bold", 32, farbe=TEXT, rechts=1800)]
y = 232
for c, ebene, text, fett in REIHEN:
    x = (130, 200)[ebene]
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 38 if ebene == 0 else 32, rechts=1800))
    y += {0: 70, 1: 58}[ebene]
assert y <= 970, y
folie([("sch", "Prüfschema"), ("s1", "Prüfschema › I. Statthaftigkeit"), ("s2", "Prüfschema › II. Berechtigung und Beschwer"),
       ("s3", "Prüfschema › III. Einlegung"), ("s4", "Prüfschema › IV. Begründung"), ("s5", "Prüfschema › V. Wiedereinsetzung")], els_sch)

# ===========================================================================================================================
# Q Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Einlegen binnen ", 0), ("einer Woche", "a"), (" ab Verkündung,", 0)],
                 [("begründen binnen ", 0), ("eines Monats", "b"), (" danach,", 0)],
                 [("oder ab Zustellung, wenn das Urteil später kommt.", 0)]], 750, 280, 40, "merke",
                {"a": beim("merke", "einer"), "b": beim("merke", "eines")}),
    *markertext([[("Und versäumt die Verteidigung die Frist,", 0)], [("hilft dem Angeklagten die", 0)],
                 [("Wiedereinsetzung", "c"), (".", 0)]], 750, 600, 44, "m2", {"c": beim("m2", "Wiedereinsetzung")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
