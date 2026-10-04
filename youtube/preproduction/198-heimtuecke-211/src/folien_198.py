"""Folge 198 · Heimtücke § 211: Arglosigkeit, Wehrlosigkeit & Schlafende – Serienstandard Open Peeps (Katzenkönig).
Fall: Heribert und Siegmund führen zusammen eine kleine Firma und streiten seit Wochen ums Geld. Heribert beschließt,
Siegmund zu töten, und lädt ihn zum Versöhnungsessen ein (Donnerstag, 12.3., 19 Uhr). Siegmund glaubt an die Versöhnung;
als er sich an den Tisch setzt, greift Heribert ihn mit Tötungsvorsatz an; Siegmund stirbt.
Szenen laut ../SZENENPLAN.md: A1 Büro der Firma, A2 Esszimmer (Versöhnungsessen, Frage), B Sachverhalt, C Wortlaut
§ 211 Abs. 1 und Abs. 2 (Auszug), D Definition und Prüfschema, E a) Arglosigkeit, F b) Wehrlosigkeit, G c) Ausnutzungs-
bewusstsein, d) feindliche Willensrichtung, H1–H3 Sonderfälle (Schlafende, Kleinkinder, Besinnungslose), I1–I3 Lösung,
J Restriktion, K Klausurtipp (Lexi), L Merksatz (Lexi).
Darstellung: kein Angriff, keine Waffe, kein Blut, keine Leiche im Bild – nur Tisch/Essen-Icons und Text („greift an“);
nach „stirbt“ steht Siegmund nicht mehr am Tisch, der Stuhl bleibt leer. Personen fiktiv.
Handlungsgeräusch: Stuhl (A2, Siegmund setzt sich); ../geraeusche_herkunft.json.
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz
als eigene Kopie aus Folge 194 (gemeinsame Dateien unverändert); neu: wand(), tisch(), schreibtisch().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut nach gesetze-im-internet.de (StGB), Abruf 04.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave
import datetime as _dt

bausteine.FIGORDNER = "op_198/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_198/" in n:
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
NAME = {"HB": "Heribert", "SG": "Siegmund"}
NFARBE = {"HB": LILA, "SG": TUERKIS}
HOLZ = (214, 160, 110, 255)
HELLROT = (253, 232, 228, 255)
HELLGRAU = (226, 226, 222, 255)
ZITAT = (246, 246, 250, 255)
HELL = (255, 251, 230, 255)


def stehend(k, x, folge, unten=930, hoehe=480, bis=None):
    return [*fig(k, x, unten, hoehe, folge, bis=bis), ns(NAME[k], x, unten, folge[0][0], NFARBE[k], d=0.1, bis=bis)]


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


def zwei(folge_sg, folge_hb):
    """Siegmund und Heribert rechts neben der Tafel (blicken nach links zur Tafel)."""
    return [*stehend("SG", X1, folge_sg), *stehend("HB", X2, folge_hb)]


FE = "fluent-emoji-high-contrast"
HOLZ2 = (196, 140, 92, 255)


def wand(c, x0=80, x1=1840, oben=330, farbe=WAND):
    """Rückwand des Raums (Grundform), Tuschekontur."""
    w, h = x1 - x0, BODEN_Y - oben
    def zz(dr, s):
        dr.rectangle((3 * s, 3 * s, (w - 3) * s, (h + 2) * s), fill=farbe, outline=INK, width=5 * s)
    return hart(El(_flaeche(w, h + 4, zz), x0, oben, c, "cut", 0.0, None, name="wand"))


def tisch(c, x0, x1, oben, bein=26, platte=30, farbe=HOLZ):
    """Esstisch: Platte und zwei Beine bis zum Boden."""
    w, h = x1 - x0, BODEN_Y - oben
    def zz(dr, s):
        dr.rounded_rectangle((3 * s, 3 * s, (w - 3) * s, platte * s), 8 * s, fill=farbe, outline=INK, width=5 * s)
        for bx in (30, w - 30 - bein):
            dr.rectangle((bx * s, (platte - 3) * s, (bx + bein) * s, (h - 1) * s), fill=farbe, outline=INK, width=5 * s)
    return hart(El(_flaeche(w, h + 2, zz), x0, oben, c, "cut", 0.0, None, name="tisch"))


# ===========================================================================================================================
# A1 Fall: die Firma, der Streit, die Einladung
# ===========================================================================================================================
HBX, SGX = 560, 1380
folie([(NULL, "Fall · Heribert und Siegmund: eine Firma"), ("streit", "Fall · Seit Wochen Streit ums Geld"),
       ("plan", "Fall · Heribert beschließt die Tat"), ("lock", "Fall · Die Einladung zum Versöhnungsessen"),
       ("he1", "Fall · Heribert lädt ein"), ("le1", "Fall · Siegmund sagt zu")], [
    wand(NULL),
    fenster(NULL, 1500, 420, 260, 220),
    boden(NULL),
    tisch(NULL, 790, 1150, 720, farbe=HOLZ2),
    hart(ficon(FE, "office-building", 1745, 300, 120, NULL, fuell=BLAU, anim="cut")),
    hart(pl("zusammen eine kleine Firma", 70, 30, NULL, fill=LILA, size=38)),
    hart(ficon(FE, "page-facing-up", 900, 720, 70, NULL, fuell=WEISS, anim="cut")),
    ficon(FE, "money-bag", 1040, 720, 90, beim("streit", "Geld"), fuell=GELB),
    pl("seit Wochen: heftiger Streit ums Geld", 70, 110, "streit", fill=WEISS, size=32, bis="he1"),
    ficon(FE, "anger-symbol", HBX + 150, 450, 60, beim("streit", "heftig"), fuell=ROT, bis="plan"),
    ficon(FE, "anger-symbol", SGX - 150, 450, 60, beim("streit", "heftig"), fuell=ROT, bis="lock"),
    pl("Heribert beschließt: Siegmund töten", 70, 185, beim("plan", "Er"), fill=HELLROT, size=32, bis="he1"),
    pl("Einladung zum Versöhnungsessen", 70, 255, "lock", fill=GELB, size=32, bis="he1"),
    ficon(FE, "spaghetti", 970, 610, 100, beim("lock", "Versöhnungsessen"), fuell=GELB),
    *fig("HB", HBX, BODEN_Y, FHA, [(NULL, "ruhig_r"), ("streit", "streit_r"), ("plan", "denkt_r"), ("lock", "laechelt_r")],
         erst="cut", bis="he1"),
    *redet("HB_redet_r", HBX, BODEN_Y, FHA, "he1", "le1"),
    *fig("HB", HBX, BODEN_Y, FHA, [("le1", "laechelt_r")], erst="cut"),
    hart(ns(NAME["HB"], HBX, BODEN_Y, NULL, NFARBE["HB"])),
    *fig("SG", SGX, BODEN_Y, FHA, [(NULL, "ruhig"), ("streit", "streit"), ("lock", "denkt"), ("he1", "ruhig")],
         erst="cut", bis="le1"),
    *redet("SG_redet", SGX, BODEN_Y, FHA, "le1", "abend"),
    hart(ns(NAME["SG"], SGX, BODEN_Y, NULL, NFARBE["SG"])),
    blase("sprech", 1000, 210, "he1", 1060, 200, inhalt=["Lass uns den Streit begraben. Komm am", "Donnerstag um 19 Uhr zu mir zum Essen."],
          textsize=34, figur=("HB_redet_r", HBX, BODEN_Y, FHA), bis="le1"),
    blase("sprech", 900, 170, "le1", 900, 200, inhalt=["Gern. Ich bin froh, dass wir", "uns wieder vertragen."],
          textsize=34, figur=("SG_redet", SGX, BODEN_Y, FHA)),
])

# ===========================================================================================================================
# A2 Fall: das Versöhnungsessen (Donnerstag, 12.3., 19 Uhr) und die Frage
# ===========================================================================================================================
HB2X, SG2X, SG2T = 470, 1560, 1330          # Heribert links; Siegmund kommt rechts herein, dann am Tisch
STUHL_L, STUHL_R = 690, 1210
SETZT = beim("setzt", "setzt")
folie([("abend", "Fall · Donnerstag, 12.3., 19 Uhr: das Versöhnungsessen"), ("kommt", "Fall · Siegmund kommt pünktlich"),
       ("setzt", "Fall · Siegmund setzt sich an den Tisch"), ("angriff", "Fall · Heribert greift an"),
       ("stirbt", "Fall · Siegmund stirbt"), ("frage", "Fall · Ist das Mord?"), ("frage2", "Fall · Trotz Streit arglos?")], [
    wand("abend", farbe=WAND2),
    fenster("abend", 110, 410, 220, 200),
    boden("abend"),
    hart(ficon(FE, "chair", STUHL_L, BODEN_Y, 170, "abend", fuell=HOLZ2, anim="cut")),
    hart(ficon(FE, "chair", STUHL_R, BODEN_Y, 170, "abend", fuell=HOLZ2, spiegeln=True, anim="cut")),
    tisch("abend", 780, 1120, 700),
    hart(ficon(FE, "shallow-pan-of-food", 870, 700, 110, "abend", fuell=ROT, anim="cut")),
    hart(ficon(FE, "green-salad", 990, 700, 90, "abend", fuell=GRUEN, anim="cut")),
    hart(ficon(FE, "bread", 1075, 700, 70, "abend", fuell=GELB, anim="cut")),
    hart(pl("Donnerstag, 12.3., 19 Uhr", 70, 30, "abend", fill=LILA, size=38)),
    hart(ficon(FE, "seven-oclock", 640, 135, 80, "abend", fuell=WEISS, anim="cut")),
    pl("Siegmund kommt pünktlich", 70, 110, "kommt", fill=WEISS, size=32),
    pl("glaubt an die Versöhnung", 70, 185, beim("kommt", "glaubt"), fill=GELB, size=32),
    pl("setzt sich an den Tisch", 70, 255, SETZT, fill=WEISS, size=32),
    pl("Heribert greift ihn mit Tötungsvorsatz an", 70, 330, "angriff", fill=HELLROT, size=34),
    pl("Siegmund stirbt", SG2T - 30, 560, "stirbt", fill=HELLGRAU, size=32, anker="m"),
    pl("Ist das Mord?", 1180, 30, "frage", fill=PINK, size=40),
    pl("wusste vom Streit – trotzdem arglos?", 1050, 110, beim("frage2", "War"), fill=GELB, size=32),
    *fig("HB", HB2X, BODEN_Y, FHA, [("abend", "laechelt_r"), ("angriff", "ernst_r"), ("stirbt", "still_r")], erst="cut"),
    hart(ns(NAME["HB"], HB2X, BODEN_Y, "abend", NFARBE["HB"])),
    *fig("SG", SG2X, BODEN_Y, FHA, [("kommt", "froh")], bis=SETZT),
    ns(NAME["SG"], SG2X, BODEN_Y, "kommt", NFARBE["SG"], d=0.1, bis=SETZT),
    szene(hart(peep_voll("SG_froh", SG2T, BODEN_Y, FHA, SETZT, anim="cut", bis="stirbt")), "198stuhl_1", 1.0, 0.1),
    hart(ns(NAME["SG"], SG2T, BODEN_Y, SETZT, NFARBE["SG"], bis="stirbt")),
])

# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_198(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=34, zeilenabstand=1.30)
        els += e; y += 18
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_198("sv", [
    "Heribert und Siegmund führen zusammen eine kleine Firma und streiten seit Wochen heftig ums Geld. Heribert beschließt, "
    "Siegmund zu töten, und lädt ihn zu einem Versöhnungsessen ein.",
    "Heribert: „Lass uns den Streit begraben. Komm am Donnerstag um 19 Uhr zu mir zum Essen.“ Siegmund: „Gern. Ich bin "
    "froh, dass wir uns wieder vertragen.“",
    "Am Donnerstag, dem 12.3., kommt Siegmund um 19 Uhr pünktlich. Er glaubt an die Versöhnung und rechnet mit einem "
    "friedlichen Abend. Als er sich an den Tisch setzt, greift Heribert ihn mit Tötungsvorsatz an. Siegmund stirbt.",
], "Hat sich Heribert wegen Mordes strafbar gemacht?")

# ===========================================================================================================================
# C Wortlaut § 211 Abs. 1 und Abs. 2 (Auszug)
# ===========================================================================================================================
PW = "Mord, § 211 StGB"
W1 = "„(1) Der Mörder wird mit lebenslanger Freiheitsstrafe bestraft.“"
w1, w1_y = wortlaut(80, 175, 1100, W1, "§ 211 Abs. 1 StGB", "p211", marken=[
    ("lebenslanger Freiheitsstrafe", beim("abs1", "lebenslanger"))], size=34)
W2 = "„(2) Mörder ist, wer … heimtückisch … einen Menschen tötet.“"
w2, w2_y = wortlaut(80, w1_y + 34, 1100, W2, "§ 211 Abs. 2 StGB (Auszug)", "abs2", marken=[
    ("heimtückisch", beim("abs2", "heimtückisch")), ("einen Menschen tötet.", beim("abs2", "einen"))], size=34)
folie([("p211", f"{PW} › Wortlaut"), ("abs1", f"{PW} › Abs. 1: lebenslange Freiheitsstrafe"),
       ("abs2", f"{PW} › Abs. 2: heimtückisch"), ("gruppe", f"{PW} › 2. Gruppe: Art der Tatausführung"),
       ("v075", f"{PW} › alle Mordmerkmale: eigene Folge")], rechts_frei([
    *tafel("p211", "Mord, § 211 StGB"),
    *w1, *w2,
    pl("2. Gruppe der Mordmerkmale: Art der Tatausführung", 80, w2_y + 40, "gruppe", fill=BLAU, size=32),
    pl("Überblick aller Gruppen: Folge zu den Mordmerkmalen", 80, w2_y + 120, beim("v075", "Überblick"), fill=WEISS, size=28),
    *requisit([("p211", (FE, "balance-scale", 110, GELB), "§ 211 StGB", GELB),
               ("abs2", (FE, "spaghetti", 110, GELB), "heimtückisch?", PINK),
               ("gruppe", (FE, "spaghetti", 110, GELB), "Art der Tatausführung", BLAU)]),
    *zwei([("p211", "ruhig"), ("abs2", "denkt")], [("p211", "ernst"), ("abs1", "still")]),
]))
assert w2_y + 190 <= 890, w2_y

# ===========================================================================================================================
# D Definition und Prüfschema
# ===========================================================================================================================
PH = "Heimtücke"
folie([("def", f"{PH} › Was heißt heimtückisch?"), ("def2", f"{PH} › Definition (BGH)"), ("schema", f"{PH} › Prüfschema"),
       ("sa", f"{PH} › Prüfschema › a) Arglosigkeit"), ("sb", f"{PH} › Prüfschema › b) Wehrlosigkeit"),
       ("sc", f"{PH} › Prüfschema › c) Ausnutzungsbewusstsein"), ("sd", f"{PH} › Prüfschema › d) feindliche Willensrichtung")], [
    karte(60, 50, 1800, 940, "def"), titel(glyphen("Heimtücke, § 211 Abs. 2 Gr. 2 StGB"), 110, 90, "def", 46),
    blk(110, 185, 1700, 130, BLAU, "def2", [("heimtückisch handelt, wer in feindlicher Willensrichtung die Arg- und", "Bold", 34, INK),
                                            ("Wehrlosigkeit des Opfers bewusst zur Tötung ausnutzt", "Bold", 34, INK)]),
    zit("BGH, Urt. v. 4.12.2024 – 2 StR 352/24, Rn. 25 (st. Rspr.)", 130, 330, beim("def2", "ausnutzt"), rechts=1800),
    z("Prüfschema", 130, 410, "schema", "ExtraBold", 40, rechts=1800),
    z("a) Arglosigkeit", 200, 490, "sa", "Bold", 38, rechts=1800),
    z("b) Wehrlosigkeit – infolge der Arglosigkeit", 200, 570, "sb", "Bold", 38, rechts=1800),
    z("c) Ausnutzungsbewusstsein", 200, 650, "sc", "Bold", 38, rechts=1800),
    z("d) feindliche Willensrichtung", 200, 730, "sd", "Bold", 38, rechts=1800),
])

# ===========================================================================================================================
# E a) Arglosigkeit
# ===========================================================================================================================
PA = "Heimtücke › a) Arglosigkeit"
folie([("arg", PA), ("zeit", f"{PA} › maßgeblich: Beginn des Angriffs"), ("offen", f"{PA} › auch bei offen feindseligem Angriff"),
       ("angst", f"{PA} › latente Angst genügt nicht")], rechts_frei([
    *tafel("arg", "a) Arglosigkeit"),
    blk(110, 180, 1040, 175, GELB, beim("arg", "Arglos"), [("arglos: rechnet bei Beginn des ersten mit", "Bold", 32, INK),
                                                           ("Tötungsvorsatz geführten Angriffs nicht mit", "Bold", 32, INK),
                                                           ("einem erheblichen Angriff auf den Körper", "Bold", 32, INK)]),
    pl("maßgeblich: genau dieser Moment", 110, 375, "zeit", fill=WEISS, size=32),
    *neinz("heimliches Vorgehen? nicht nötig", 455, "offen", "Bold", 32, x=170),
    *okz("auch offen feindselig – wenn der Angriff", 510, beim("offen", "Arglos"), "Bold", 32, x=170),
    z("so schnell kommt, dass keine Abwehr bleibt", 170, 555, beim("offen", "aber"), "Bold", 32),
    z("latente Angst aus früheren Streitigkeiten: schadet", 170, 630, "angst", "Bold", 32),
    z("erst, wenn das Opfer im Tatzeitpunkt mit", 170, 675, beim("angst", "wenn"), "Bold", 32),
    z("Feindseligkeiten rechnet", 170, 720, beim("angst", "Feindseligkeiten"), "Bold", 32),
    zit("BGH 2 StR 352/24, Rn. 25 f. · BGH 5 StR 423/25, Rn. 13", 170, 775, beim("angst", "Feindseligkeiten")),
    *requisit([("arg", (FE, "dove", 110, WEISS), "arglos?", GELB),
               ("zeit", (FE, "stopwatch", 100, WEISS), "Beginn des Angriffs", WEISS),
               ("offen", (FE, "high-voltage", 90, GELB), "offen, aber blitzschnell", WEISS),
               ("angst", (FE, "anger-symbol", 80, ROT), "früherer Streit", HELLGRAU)]),
    *zwei([("arg", "ruhig"), ("offen", "denkt"), ("angst", "streit")], [("arg", "ruhig"), ("zeit", "still"), ("angst", "ernst")]),
]))

# ===========================================================================================================================
# F b) Wehrlosigkeit
# ===========================================================================================================================
PB = "Heimtücke › b) Wehrlosigkeit"
folie([("wehr", PB), ("wehr2", f"{PB} › verteidigen, fliehen, Hilfe holen"), ("folge", f"{PB} › Folge der Arglosigkeit")],
      rechts_frei([
    *tafel("wehr", "b) Wehrlosigkeit"),
    blk(110, 180, 1040, 130, BLAU, beim("wehr", "Wehrlos"), [("wehrlos: Verteidigungsfähigkeit aufgehoben", "Bold", 32, INK),
                                                            ("oder erheblich eingeschränkt", "Bold", 32, INK)]),
    *neinz("kann sich nicht mehr verteidigen", 345, beim("wehr2", "verteidigen"), "Bold", 32, x=170),
    *neinz("kann nicht fliehen", 400, beim("wehr2", "fliehen"), "Bold", 32, x=170),
    *neinz("kann keine Hilfe holen", 455, beim("wehr2", "Hilfe"), "Bold", 32, x=170),
    zit("BGH 5 StR 423/25, Rn. 13 · BGH 4 StR 337/20, Rn. 12", 170, 510, beim("wehr2", "Hilfe")),
    blk(110, 590, 1040, 80, GRUEN, "folge", [("Wehrlosigkeit gerade als Folge der Arglosigkeit", "ExtraBold", 32, INK)]),
    *requisit([("wehr", (FE, "shield", 100, BLAU), "wehrlos?", BLAU),
               ("wehr2", (FE, "no-entry", 90, ROT), "keine Flucht", WEISS),
               ("folge", (FE, "dove", 110, WEISS), "weil arglos", GRUEN)]),
    *zwei([("wehr", "ruhig"), ("wehr2", "ernst")], [("wehr", "denkt"), ("folge", "ruhig")]),
]))

# ===========================================================================================================================
# G c) Ausnutzungsbewusstsein, d) feindliche Willensrichtung
# ===========================================================================================================================
PC = "Heimtücke › c) Ausnutzungsbewusstsein"
folie([("aus", PC), ("blick", f"{PC} › schon mit einem Blick"), ("feind", "Heimtücke › d) feindliche Willensrichtung")],
      rechts_frei([
    *tafel("aus", "c) Ausnutzungsbewusstsein"),
    z("Täter erkennt die Arg- und Wehrlosigkeit und", 110, 185, beim("aus", "Der"), "Bold", 32),
    z("nutzt sie bewusst aus:", 110, 230, beim("aus", "bewusst"), "Bold", 32),
    blk(110, 285, 1040, 80, GELB, beim("aus", "Ihm"), [("überrascht einen ahnungslosen, schutzlosen Menschen", "ExtraBold", 30, INK)]),
    *okz("schon „mit einem Blick“ möglich", 395, "blick", "Bold", 32, x=170),
    zit("BGH 2 StR 352/24, Rn. 32 (unter Verweis auf BGHSt 23, 119, 121)", 170, 445, "blick"),
    blk(110, 520, 1040, 80, LILA, "feind", [("d) feindliche Willensrichtung", "ExtraBold", 34, INK)]),
    z("fehlt nur ganz ausnahmsweise, etwa wenn die", 170, 625, beim("feind", "fehlt"), "Bold", 32),
    z("Tötung dem ausdrücklichen Willen des Opfers entspricht", 170, 670, beim("feind", "ausdrücklichen"), "Bold", 32),
    zit("BGH, Urt. v. 19.6.2019 – 5 StR 128/19, BGHSt 64, 111, Rn. 28", 170, 725, beim("feind", "ausdrücklichen")),
    *requisit([("aus", (FE, "brain", 110, PINK), "bewusst ausgenutzt", PINK),
               ("blick", (FE, "eye", 100, WEISS), "ein Blick genügt", WEISS),
               ("feind", (FE, "balance-scale", 110, LILA), "feindlich?", LILA)]),
    *zwei([("aus", "ruhig"), ("feind", "denkt")], [("aus", "denkt"), ("blick", "ernst"), ("feind", "still")]),
]))

# ===========================================================================================================================
# H1 Sonderfall: Schlafende
# ===========================================================================================================================
PS2 = "Sonderfälle"
folie([("sf", f"{PS2} · drei Fallgruppen"), ("schlaf", f"{PS2} › 1. Schlafende"), ("schlaf2", f"{PS2} › 1. Schlafende: regelmäßig arglos")],
      rechts_frei([
    *tafel("sf", "Drei Sonderfälle"),
    blk(110, 180, 1040, 76, WEISS, "schlaf", [("1. Schlafende", "ExtraBold", 34, INK)]),
    *okz("nimmt die Arglosigkeit mit in den Schlaf", 280, beim("schlaf", "Wer"), "Bold", 32, x=170),
    *okz("deshalb regelmäßig arglos", 340, "schlaf2", "Bold", 32, x=170),
    *neinz("außer etwa: gegen den Willen vom Schlaf übermannt", 400, beim("schlaf2", "außer"), "Bold", 32, x=170),
    zit("BGHSt 23, 119, 120 f. – wiedergegeben in BGH 2 StR 352/24, Rn. 27", 170, 455, beim("schlaf2", "außer")),
    pl("2. Kleinkinder", 110, 540, "sf", fill=HELLGRAU, size=30),
    pl("3. Besinnungslose", 400, 540, "sf", fill=HELLGRAU, size=30),
    *requisit([("sf", (FE, "white-question-mark", 80, WEISS), "3 Sonderfälle", WEISS),
               ("schlaf", (FE, "bed", 170, BLAU), "Schlaf", BLAU),
               ("schlaf2", (FE, "zzz", 90, WEISS), "arglos", GELB)]),
]))

# ===========================================================================================================================
# H2 Sonderfall: Kleinkinder
# ===========================================================================================================================
folie([("kind", f"{PS2} › 2. Kleinkinder"), ("kind2", f"{PS2} › 2. schutzbereiter Dritter"), ("kind3", f"{PS2} › 2. etwa die Eltern")],
      rechts_frei([
    *tafel("kind", "Drei Sonderfälle"),
    blk(110, 180, 1040, 76, WEISS, "kind", [("2. Kleinkinder (wenige Monate alt)", "ExtraBold", 34, INK)]),
    *neinz("zu keinerlei Argwohn fähig", 280, beim("kind", "ist"), "Bold", 32, x=170),
    z("auf seine Arglosigkeit kommt es nicht an", 170, 325, beim("kind", "Auf"), "Bold", 32),
    zit("BGHSt 4, 11, 13 – wiedergegeben in BGH 2 StR 309/12, Rn. 5", 170, 375, beim("kind", "Auf")),
    *okz("Heimtücke über einen schutzbereiten Dritten", 445, "kind2", "Bold", 32, x=170),
    z("z. B. Eltern: beschützen das Kind oder vertrauen", 170, 500, "kind3", "Bold", 32),
    z("dem Täter", 170, 545, beim("kind3", "vertrauen"), "Bold", 32),
    z("räumlich nah genug", 170, 600, beim("kind3", "räumlich"), "Bold", 32),
    zit("BGH, Beschl. v. 5.8.2014 – 1 StR 340/14, Rn. 7 f.", 170, 650, beim("kind3", "räumlich")),
    *requisit([("kind", (FE, "baby-bottle", 80, WEISS), "Kleinkind", WEISS),
               ("kind2", (FE, "shield", 100, GRUEN), "Schutz durch Dritte", GRUEN),
               ("kind3", (FE, "house", 110, GELB), "Eltern in der Nähe", GELB)]),
]))

# ===========================================================================================================================
# H3 Sonderfall: Besinnungslose
# ===========================================================================================================================
folie([("koma", f"{PS2} › 3. Besinnungslose"), ("koma2", f"{PS2} › 3. schutzbereite Dritte: Pflegepersonal")], rechts_frei([
    *tafel("koma", "Drei Sonderfälle"),
    blk(110, 180, 1040, 76, WEISS, "koma", [("3. Besinnungslose, z. B. im Koma", "ExtraBold", 34, INK)]),
    *neinz("anders als Schlafende: zu keinerlei Argwohn fähig", 280, beim("koma", "Anders"), "Bold", 32, x=170),
    *okz("Heimtücke über schutzbereite Dritte möglich,", 350, "koma2", "Bold", 32, x=170),
    z("z. B. über das Pflegepersonal", 170, 395, beim("koma2", "zum"), "Bold", 32),
    zit("BGH, Urt. v. 18.10.2007 – 3 StR 226/07, Rn. 16", 170, 445, beim("koma2", "zum")),
    *requisit([("koma", (FE, "hospital", 140, WEISS), "Koma", WEISS),
               ("koma2", (FE, "stethoscope", 100, BLAU), "Pflegepersonal", BLAU)]),
]))

# ===========================================================================================================================
# I1 Lösung: a) Arglosigkeit trotz Streit, Lockfall
# ===========================================================================================================================
PL = "Lösung › Heribert"
folie([("loes", "Lösung · Der Fall"), ("la", f"{PL} › a) War Siegmund arglos?"), ("la2", f"{PL} › a) Streit allein genügt nicht"),
       ("la3", f"{PL} › a) Siegmund arglos (+)"), ("falle", f"{PL} › a) planmäßig in die Lage gelockt")], rechts_frei([
    *tafel("loes", "Lösung: Heimtücke durch Heribert?"),
    z("a) Arglosigkeit", 110, 180, "la", "ExtraBold", 34),
    z("Siegmund wusste vom Streit ums Geld", 170, 235, beim("la", "Er"), "Bold", 32),
    *okz("Streit allein hebt die Arglosigkeit nicht auf", 290, "la2", "Bold", 32, x=170),
    zit("BGH 3 StR 171/12, Rn. 5 · BGH 5 StR 338/17, Rn. 12", 170, 340, "la2"),
    z("entscheidend: Angriff beim Hinsetzen erwartet?", 170, 385, beim("la2", "Entscheidend"), "Bold", 32),
    *okz("nein: glaubte an die Versöhnung – arglos", 445, "la3", "ExtraBold", 32, x=170),
    blk(110, 520, 1040, 130, GELB, "falle", [("planmäßig in diese Lage gelockt:", "ExtraBold", 32, INK),
                                            ("Vorkehrungen wirken bis zur Tat fort", "Bold", 30, INK)]),
    zit("BGH 4 StR 337/20, Rn. 13 · BGH 1 StR 393/10, Rn. 5", 170, 665, beim("falle", "Solche")),
    *requisit([("loes", (FE, "spaghetti", 110, GELB), "Versöhnungsessen", WEISS),
               ("la", (FE, "anger-symbol", 80, ROT), "Streit ums Geld", HELLGRAU),
               ("la3", (FE, "dove", 110, WEISS), "arglos (+)", GRUEN),
               ("falle", (FE, "spaghetti", 110, GELB), "gelockt", HELLROT)]),
    *zwei([("loes", "ruhig"), ("la", "denkt"), ("la3", "froh")], [("loes", "ernst"), ("falle", "denkt")]),
]))

# ===========================================================================================================================
# I2 Lösung: b) Wehrlosigkeit, c) Ausnutzungsbewusstsein, d) feindliche Willensrichtung
# ===========================================================================================================================
folie([("lb", f"{PL} › b) wehrlos beim Hinsetzen"), ("lb2", f"{PL} › b) infolge der Arglosigkeit (+)"),
       ("lc", f"{PL} › c) Moment geplant"), ("lc2", f"{PL} › c) Ausnutzungsbewusstsein (+)"),
       ("ld", f"{PL} › d) feindliche Willensrichtung (+)")], rechts_frei([
    *tafel("lb", "Lösung: Heimtücke durch Heribert?"),
    z("b) Wehrlosigkeit", 110, 180, "lb", "ExtraBold", 34),
    z("beim Hinsetzen: weder Verteidigung noch Flucht", 170, 235, beim("lb", "Beim"), "Bold", 32),
    *okz("gerade, weil er keinen Angriff erwartete: (+)", 290, "lb2", "Bold", 32, x=170),
    z("c) Ausnutzungsbewusstsein", 110, 370, "lc", "ExtraBold", 34),
    z("Heribert plant genau diesen Moment, weiß:", 170, 425, beim("lc", "Heribert"), "Bold", 32),
    z("er überrascht einen ahnungslosen Menschen", 170, 470, beim("lc", "dass"), "Bold", 32),
    *okz("Ausnutzungsbewusstsein (+)", 525, "lc2", "Bold", 32, x=170),
    z("d) feindliche Willensrichtung", 110, 605, "ld", "ExtraBold", 34),
    *okz("Siegmund wollte nicht sterben: (+)", 660, beim("ld", "Siegmund"), "Bold", 32, x=170),
    *requisit([("lb", (FE, "chair", 130, HOLZ2), "beim Hinsetzen", WEISS),
               ("lb2", (FE, "shield", 100, BLAU), "wehrlos (+)", GRUEN),
               ("lc", (FE, "brain", 110, PINK), "geplant", PINK),
               ("ld", (FE, "balance-scale", 110, LILA), "feindlich (+)", LILA)]),
    *zwei([("lb", "ruhig"), ("lb2", "ernst")], [("lb", "still"), ("lc", "ernst")]),
]))

# ===========================================================================================================================
# I3 Ergebnis
# ===========================================================================================================================
folie([("erg", "Ergebnis · Heribert: heimtückisch getötet"), ("erg2", "Ergebnis · Mord, § 211 StGB")], rechts_frei([
    *tafel("erg", "Ergebnis"),
    *okz("Heimtücke: a) b) c) d) erfüllt", 185, "erg", "ExtraBold", 34, x=170),
    *okz("keine Rechtfertigungs- und Entschuldigungsgründe", 250, "erg2", "Bold", 32, x=170),
    blk(110, 330, 1040, 130, GRUEN, beim("erg2", "Er"), [("Heribert: strafbar wegen Mordes", "ExtraBold", 36, INK),
                                                       ("§ 211 StGB (heimtückisch)", "Bold", 32, INK)]),
    *requisit([("erg", (FE, "spaghetti", 110, GELB), "Heimtücke (+)", GRUEN),
               ("erg2", (FE, "balance-scale", 110, GRUEN), "Mord", GRUEN)]),
    *stehend("HB", FX, [("erg", "still"), ("erg2", "ernst")]),
]))

# ===========================================================================================================================
# J Restriktion: Rechtsfolgenlösung (Verweis 007), Lehre: verwerflicher Vertrauensbruch
# ===========================================================================================================================
PR = "Einschränkung der Heimtücke?"
folie([("restr", f"{PR} · Grund: lebenslange Strafe"), ("rfl", f"{PR} › BGH: Rechtsfolgenlösung"),
       ("lehre", f"{PR} › Teil der Lehre: verwerflicher Vertrauensbruch"), ("bghn", f"{PR} › BGH: nicht erforderlich"),
       ("hier", f"{PR} › hier: Vertrauen missbraucht")], rechts_frei([
    *tafel("restr", "Einschränkung der Heimtücke?"),
    pl("Grund: lebenslange Freiheitsstrafe", 110, 180, "restr", fill=WEISS, size=32),
    blk(110, 255, 1040, 130, BLAU, "rfl", [("BGH: Rechtsfolgenlösung – bei ganz besonderen", "ExtraBold", 30, INK),
                                          ("schuldmindernden Umständen auf der Strafseite", "Bold", 30, INK)]),
    zit("BGHSt 30, 105 (GSSt 1/81) – wiedergegeben in BGHSt 64, 111, Rn. 28", 170, 400, beim("rfl", "sogenannten")),
    pl("mehr: Folge zum Haustyrannen-Fall", 170, 445, beim("rfl", "Mehr"), fill=WEISS, size=28),
    blk(110, 520, 1040, 130, LILA, "lehre", [("Meinung (Teil der Lehre): schon im Tatbestand", "ExtraBold", 30, INK),
                                            ("besonders verwerflicher Vertrauensbruch nötig", "Bold", 30, INK)]),
    *neinz("BGH: nicht erforderlich", 670, "bghn", "Bold", 32, x=170),
    zit("BGH, Beschl. v. 25.8.2010 – 1 StR 393/10, Rn. 5", 170, 718, "bghn"),
    *okz("Lehre: gut vertretbar – Vertrauen in die", 770, "hier", "Bold", 32, x=170),
    z("Versöhnung gezielt geweckt und missbraucht", 170, 815, beim("hier", "Versöhnung"), "Bold", 32),
    *requisit([("restr", (FE, "balance-scale", 110, GELB), "lebenslang", GELB),
               ("rfl", (FE, "classical-building", 110, BLAU), "BGH", BLAU),
               ("lehre", (FE, "handshake", 110, LILA), "Vertrauensbruch?", LILA),
               ("hier", (FE, "spaghetti", 110, GELB), "Versöhnung missbraucht", HELLROT)]),
    *stehend("HB", FX, [("restr", "ruhig"), ("lehre", "denkt"), ("hier", "ernst")]),
]))

# ===========================================================================================================================
# K Klausurtipp (Lexi)
# ===========================================================================================================================
els_k = [*tafel("tipp", "Klausurtipp: der richtige Zeitpunkt", fill=HELL), warnung_i(150, 225, "tipp", gr=26),
         z("Arglosigkeit bei Beginn des ersten mit", 200, 200, "tipp", "Bold", 32),
         z("Tötungsvorsatz geführten Angriffs prüfen", 200, 245, beim("tipp", "Tötungsvorsatz"), "Bold", 32),
         blk(130, 320, 1020, 160, GELB, "tipp2", [("Streit davor: schließt nicht automatisch aus", "ExtraBold", 32, INK),
                                                  ("Frage: Rechnete das Opfer genau in diesem", "Bold", 30, INK),
                                                  ("Moment mit einem erheblichen Angriff?", "Bold", 30, INK)]),
         blk(130, 520, 1020, 120, HELLROT, "tipp3", [("Einschränkungen der Heimtücke erst,", "ExtraBold", 32, INK),
                                                     ("wenn a) bis d) sauber festgestellt sind", "Bold", 30, INK)]),
         *redet("LX_warnt", FX, FB, FR + 40, "tipp", "merke"),
         ns("Lexi", FX, FB, "tipp", GELB, d=0.2)]
folie([("tipp", "Klausurtipp · Arglosigkeit: der richtige Zeitpunkt"), ("tipp2", "Klausurtipp › Streit davor"),
       ("tipp3", "Klausurtipp › Einschränkungen erst danach")], els_k)

# ===========================================================================================================================
# L Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Heimtückisch handelt, wer die ", 0), ("Arg- und", "a")],
                 [("Wehrlosigkeit", "a2"), (" des Opfers bewusst", 0)], [("zur Tötung ausnutzt.", 0)]], 750, 270, 42, "merke",
                {"a": beim("merke", "Arg-"), "a2": beim("merke", "Arg-")}),
    *markertext([[("Maßgeblich ist der ", 0), ("Beginn des Angriffs", "b"), (":", 0)]], 750, 500, 42, "mk2",
                {"b": beim("mk2", "Beginn")}),
    *markertext([[("Der ", 0), ("Schlafende", "c"), (" bleibt arglos.", 0)], [("Wer mit einem Angriff ", 0), ("rechnet", "d"),
                 (", ist es nicht.", 0)]], 750, 610, 42, "mk3",
                {"c": beim("mk3", "Schlafende"), "d": beim("mk3", "rechnet")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
