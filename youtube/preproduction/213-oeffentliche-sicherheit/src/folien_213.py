"""Folge 213 · Öffentliche Sicherheit im Polizeirecht: Was die Polizei schützt – Serienstandard Open Peeps (Katzenkönig).
Beispielfall (Beispielland Nordrhein-Westfalen), Figuren fiktiv: Frau Schulze sprüht ein buntes Bild aus Blumen und Wellen auf
das Tor ihrer eigenen Garage; Nachbar Herr Gebauer ruft die Polizei; Herr Neumann fordert sie auf aufzuhören.
Szenen laut ../SZENENPLAN.md: A Wohnstraße (Fall, Polizei kommt, Frage), B Sachverhalt, C Generalklausel (Wortlaut § 8 Abs. 1
PolG NRW), D drei Schutzgüter, E Legaldefinition Sachsen (Wortlaut § 4 Nr. 1 SächsPVDG), Regel, öffentliche Ordnung,
F 1. Rechtsordnung (Wortlaut § 303 Abs. 2 StGB, Gestaltungssatzung), G 2. Rechte des Einzelnen (Wortlaut § 903 Satz 1 BGB),
3. Staat, Ergebnis, H Gegenfall Mietgarage (Wohnstraße), I Gegenfall: Subsumtion, J nur private Rechte (Kreide),
K Subsidiarität (Wortlaut § 1 Abs. 2 PolG NRW), L Länder-Overlay (NRW, Brandenburg, Sachsen), M Klausurtipp (Lexi),
N Klausurschema, O Merksatz (Lexi).
Handlungsgeräusche: Sprühstoß, wenn Frau Schulze sprüht (A und H); Autotür, wenn der Streifenwagen hält (A);
../geraeusche_herkunft.json. Garage, Garagentor und Graffiti-Wellen programmatisch (Palettenflächen, Tuschekontur);
Blumen auf dem Tor, Haus, Sonne, Streifenwagen, Spraydose usw. aus Icon-Bibliotheken (Tabler, Phosphor, Fluent Emoji HC).
Graffiti neutral: Blumen und Wellen, kein Schriftzug, kein Tag, kein Logo.
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz
als eigene Kopie aus Folge 210 (gemeinsame Dateien unverändert).
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut nach gesetze-im-internet.de (StGB, BGB) und den Landesportalen
recht.nrw.de (PolG NRW, BauO NRW), bravors.brandenburg.de (BbgPolG), revosax.sachsen.de (SächsPVDG), Abruf 06.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_213/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_213/" in n:
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
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 06.10.2026), als Zitat mit Normangabe; der
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




# --- eigene Szenenbausteine Folge 213 ----------------------------------------------------------------------------------------
BODEN_Y = 905                                # Boden = Unterkante der Figuren in den Fallszenen
FHA = 470                                    # Figurenhöhe in den Fallszenen
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
WAND2 = (242, 232, 214, 255)
GRAUW = (214, 214, 208, 255)
HELLROT = (253, 232, 228, 255)
HELLGRUEN = (232, 247, 233, 255)
ORANGE = (249, 166, 108, 255)
TUERKIS = (127, 214, 208, 255)
DUNKEL = (58, 58, 72, 255)
HC = "fluent-emoji-high-contrast"

X1, X2 = 1395, 1730                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
IX, IU = 1560, 380                          # Requisit über der Figur
NAME = {"SC": "Frau Schulze", "NE": "Herr Neumann", "GB": "Herr Gebauer", "DI": "Frau Dietz"}
NFARBE = {"SC": ROT, "NE": BLAU, "GB": GELB, "DI": LILA}


def _flaeche(w, h, zeichne):
    s = 2
    im = Image.new("RGBA", (w * s, h * s))
    zeichne(ImageDraw.Draw(im), s)
    return im.resize((w, h), Image.LANCZOS)


def boden(c, x0=60, x1=1860):
    return hart(linienzug([(x0, BODEN_Y), (x1, BODEN_Y)], c, breite=7, farbe=INK))


def stehend(k, x, folge, unten=930, hoehe=480, bis=None, erst="pop"):
    return [*fig(k, x, unten, hoehe, folge, bis=bis, erst=erst), ns(NAME[k], x, unten, folge[0][0], NFARBE[k], d=0.1, bis=bis)]


def zwei(links, folge_l, rechts, folge_r):
    """Zwei Figuren rechts neben der Tafel (blicken nach links zur Tafel)."""
    return [*stehend(links, X1, folge_l), *stehend(rechts, X2, folge_r)]


def allein(k, folge):
    return stehend(k, FX, folge)


# Garage: Flachdach, Wand, Sektionaltor (programmatisch, Palettenflächen, Tuschekontur)
GX0, GX1, GTOP = 600, 1040, 520             # Garage links/rechts, Dachoberkante
TX0, TX1, TY0 = 650, 990, 610               # Tor links/rechts/oben (unten = Boden)


def garage(c):
    w, h = GX1 - GX0, BODEN_Y - GTOP
    def zz(dr, s):
        dr.rectangle((3 * s, 26 * s, (w - 3) * s, (h - 1) * s), fill=WAND2, outline=INK, width=5 * s)
        dr.rounded_rectangle((0, 0, w * s - 1, 34 * s), 6 * s, fill=DUNKEL, outline=INK, width=5 * s)
        x0, x1, y0 = TX0 - GX0, TX1 - GX0, TY0 - GTOP
        dr.rectangle((x0 * s, y0 * s, x1 * s, (h - 1) * s), fill=GRAUW, outline=INK, width=5 * s)
        for i in range(1, 5):
            yy = y0 + i * (h - y0) / 5
            dr.line((x0 * s, yy * s, x1 * s, yy * s), fill=INK, width=3 * s)
    return hart(El(_flaeche(w, h, zz), GX0, GTOP, c, "cut", 0.0, None, name="garage"))


def welle(c, y, farbe, amp=16, phase=0.0, breite=14, x0=TX0 + 22, x1=TX1 - 22):
    """Bemalte Welle auf dem Garagentor (Sprühlack): Sinuslinie in Palettenfarbe."""
    pts = [(int(x), int(y + amp * np.sin(phase + (x - x0) / 34))) for x in np.linspace(x0, x1, 60)]
    return linienzug(pts, c, breite=breite, farbe=farbe)


def graffiti(c_welle, c_blumen, bis=None):
    """Graffiti neutral: zwei Wellen, dann drei Blumen (Tabler flower, Palettenfüllung) – kein Schriftzug, kein Tag."""
    els = [bis_(welle(c_welle, 840, BLAU, phase=0.0), bis), bis_(welle(c_welle, 875, GRUEN, phase=1.6, amp=12), bis)]
    for cx, fu, br in ((725, GELB, 110), (835, ROT, 130), (930, LILA, 100)):
        els.append(ficon("tabler", "flower", cx, 800 - (br - 100) // 3, br, c_blumen, fuell=fu, nebenfarbe=GELB, bis=bis))
    return els


def haus_gebauer(c):
    return hart(ficon("ph", "house", 200, BODEN_Y + 2, 300, c, fuell=WEISS, nebenfarbe=BLAU, anim="cut"))


def hand_links(name, cx, unten, hoehe):
    """Linkester deckender Punkt der Figur (ausgestreckte Hand der nach links blickenden Frau Schulze)."""
    e = peep_voll(name, cx, unten, hoehe, "_")
    a = np.asarray(e.sprite)[:, :, 3] > 60
    ys, xs = np.nonzero(a)
    i = xs.argmin()
    return e.x + xs[i], e.y + ys[i]


# ===========================================================================================================================
# A Fall: Wohnstraße mit Garage (Tageslicht)
# ===========================================================================================================================
GBX, SCX, NEX, PX = 420, 1150, 1480, 1750
SC_A = ("SC_redet", SCX, BODEN_Y, FHA)
HX_, HY_ = hand_links("SC_ruhig", SCX, BODEN_Y, FHA)
spray_a = szene(welle(beim("spruehen", "sprüht"), 840, BLAU), "213spray*", 1.0, versatz=0.0)
neumann_a = szene(peep_voll("NE_ruhig", NEX, BODEN_Y, FHA, beim("neumann", "steigt"), anim="pop", bis="ne1"), "213tuer*", 1.0,
                  versatz=0.0)
folie([(NULL, "Fall · Die Wohnstraße"), ("spruehen", "Fall · Das bunte Garagentor"), ("gebauer", "Fall · Der Nachbar ruft an"),
       ("neumann", "Fall · Die Polizei kommt"), ("sc1", "Fall · „Das ist meine Garage“"),
       ("frage", "Fall · Darf die Polizei einschreiten?")], [
    boden(NULL),
    hart(ficon("tabler", "sun", 1790, 200, 100, NULL, fuell=GELB, anim="cut")),
    haus_gebauer(NULL),
    garage(NULL),
    hart(pl("Samstagvormittag in Nordrhein-Westfalen", 70, 40, NULL, fill=GELB, size=36)),
    spray_a,
    welle(beim("spruehen", "Bild"), 875, GRUEN, phase=1.6, amp=12),
    *[e for e in graffiti(beim("spruehen", "sprüht"), beim("blumen", "Blumen"))[2:]],
    *fig("SC", SCX, BODEN_Y, FHA, [(NULL, "ruhig"), (beim("spruehen", "sprüht"), "froh"), ("ne1", "skeptisch")], bis="sc1", erst="cut"),
    *redet("SC_redet", SCX, BODEN_Y, FHA, "sc1", "frage"),
    *fig("SC", SCX, BODEN_Y, FHA, [("frage", "denkt")], erst="cut"),
    hart(ns("Frau Schulze", SCX, BODEN_Y, NULL, NFARBE["SC"])),
    hart(ficon("tabler", "spray", HX_ - 14, HY_ + 40, 62, NULL, fuell=ROT, anim="cut")),
    pl("ihre eigene Garage", (GX0 + GX1) // 2, 470, beim("spruehen", "Garage"), fill=WEISS, size=30, anker="m"),
    pl("buntes Bild: Blumen und Wellen", (GX0 + GX1) // 2, 400, beim("blumen", "Blumen"), fill=GELB, size=30, anker="m"),
    *fig("GB", GBX, BODEN_Y, FHA, [("gebauer", "skeptisch_r")], bis="ge1"),
    *redet("GB_redet_r", GBX, BODEN_Y, FHA, "ge1", "neumann"),
    *fig("GB", GBX, BODEN_Y, FHA, [("neumann", "sorge_r"), ("frage", "skeptisch_r")], erst="cut"),
    ns("Herr Gebauer, Nachbar", GBX, BODEN_Y, "gebauer", NFARBE["GB"]),
    ficon(HC, "mobile-phone", GBX + 125, 640, 64, beim("gebauer", "Telefon"), fuell=WEISS, bis="neumann"),
    pl("ruft die Polizei", GBX, 380, beim("gebauer", "Telefon"), fill=BLAU, size=28, anker="m", bis="ge1"),
    blase("sprech", 700, 200, "ge1", 560, 230, inhalt=["Hier beschmiert jemand eine Garage.", "Kommen Sie bitte schnell!"],
          textsize=32, figur=("GB_redet_r", GBX, BODEN_Y, FHA), bis="neumann"),
    ficon("ph", "police-car", PX, BODEN_Y, 250, beim("neumann", "hält"), fuell=WEISS, nebenfarbe=BLAU),
    neumann_a,
    *redet("NE_redet", NEX, BODEN_Y, FHA, "ne1", "sc1"),
    *fig("NE", NEX, BODEN_Y, FHA, [("sc1", "ernst"), ("frage", "denkt")], erst="cut"),
    ns("Herr Neumann, Polizei", NEX, BODEN_Y, beim("neumann", "steigt"), NFARBE["NE"]),
    blase("sprech", 660, 190, "ne1", 1370, 230, inhalt=["Hören Sie bitte sofort", "mit dem Sprühen auf."], textsize=34,
          figur=("NE_redet", NEX, BODEN_Y, FHA), bis="sc1"),
    blase("sprech", 780, 220, "sc1", 900, 210, inhalt=["Warum? Das ist meine Garage.", "Ich darf sie bemalen, wie ich will."],
          textsize=34, figur=SC_A, bis="frage"),
    pl("Darf die Polizei einschreiten?", 1000, 200, "frage", fill=PINK, size=44, anker="m"),
])

# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_213(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=36, zeilenabstand=1.32)
        els += e; y += 16
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=34))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_213("sv", [
    "Nordrhein-Westfalen, Samstagvormittag: Frau Schulze sprüht mit Sprühlack ein großes, buntes Bild aus Blumen und "
    "Wellen auf das Tor ihrer Garage. Haus und Garage gehören ihr; das steht fest. Eine Gestaltungssatzung oder eine andere "
    "Vorschrift über die äußere Gestaltung hat ihre Gemeinde nicht erlassen.",
    "Ihr Nachbar Herr Gebauer findet das Bild hässlich und ruft die Polizei: „Hier beschmiert jemand eine Garage.“ "
    "Herr Neumann von der Polizei fordert Frau Schulze auf, sofort mit dem Sprühen aufzuhören. Sie antwortet: „Das ist "
    "meine Garage.“",
], "Darf die Polizei einschreiten?")

# ===========================================================================================================================
# C Generalklausel: Wortlaut § 8 Abs. 1 PolG NRW, Merkmal öffentliche Sicherheit
# ===========================================================================================================================
W8 = ("„Die Polizei kann die notwendigen Maßnahmen treffen, um eine im einzelnen Falle bestehende, konkrete Gefahr für die "
      "öffentliche Sicherheit oder Ordnung (Gefahr) abzuwehren, soweit nicht die §§ 9 bis 46 die Befugnisse der Polizei "
      "besonders regeln.“")
w8, w8_y = wortlaut(70, 400, 1120, W8, "§ 8 Abs. 1 PolG NRW (Generalklausel)", "wl8", size=30,
                    marken=[("notwendigen Maßnahmen", beim("wl8", "notwendigen")), ("konkrete Gefahr", beim("wl8", "konkrete")),
                            ("Sicherheit", beim("wl8", "Sicherheit"))])
GK = "Generalklausel"
folie([("gk", "Ermächtigungsgrundlage · Generalklausel"), ("land", "Generalklausel · Beispiel Nordrhein-Westfalen"),
       ("wl8", "Generalklausel · § 8 Abs. 1 PolG NRW"), ("merkmal", "Generalklausel › Merkmal: öffentliche Sicherheit")],
      rechts_frei([
    titel(glyphen("Grundlage: die Generalklausel"), 100, 75, "gk", 44),
    *neinz("„Hören Sie auf!“: keine Standardmaßnahme", 160, beim("gk", "keine"), "Bold", 32, x=150),
    z("also: Generalklausel", 150, 212, beim("gk", "Generalklausel"), size=32),
    z("Polizeirecht ist Landesrecht · Beispiel: NRW", 110, 280, "land", "Bold", 32),
    zit("PolG NRW (Fassung ab 13.12.2025)", 150, 325, beim("land", "Beispiel")),
    z("andere Länder: ähnlich, oft andere Nummer", 150, 358, beim("land", "anderen"), size=30),
    *w8,
    blk(110, w8_y + 30, 1040, 80, GELB, "merkmal", [("Merkmal: öffentliche Sicherheit", "ExtraBold", 36, INK)]),
    z("Was schützt sie überhaupt?", 150, w8_y + 130, beim("merkmal", "Was"), "Bold", 34),
    ficon("ph", "police-car", IX, IU, 230, "gk", fuell=WEISS, nebenfarbe=BLAU, bis="merkmal"),
    ficon("tabler", "shield", IX, IU, 130, "merkmal", fuell=BLAU),
    *allein("NE", [("gk", "ruhig"), ("merkmal", "denkt")]),
]))
assert w8_y + 175 <= 950, w8_y

# ===========================================================================================================================
# D Drei Schutzgüter (BVerfGE 69, 315 [352] – Brokdorf)
# ===========================================================================================================================
OS = "Öffentliche Sicherheit"
folie([("drei", f"{OS} · 3 Schutzgüter"), ("s1", f"{OS} › 1. Rechtsordnung"), ("s2", f"{OS} › 2. Rechte des Einzelnen"),
       ("s3", f"{OS} › 3. Staat und seine Einrichtungen"), ("bverfg", f"{OS} › BVerfG, Brokdorf-Beschluss")], rechts_frei([
    *tafel("drei", "Öffentliche Sicherheit: 3 Schutzgüter", size=44),
    blk(110, 180, 1040, 76, BLAU, "s1", [("1. Unverletzlichkeit der objektiven Rechtsordnung", "ExtraBold", 32, INK)]),
    blk(110, 285, 1040, 76, GELB, "s2", [("2. subjektive Rechte und Rechtsgüter des Einzelnen", "ExtraBold", 32, INK)]),
    z("Leben, Gesundheit, Freiheit, Ehre,", 150, 375, beim("s2", "Leben"), size=32),
    z("Eigentum, Vermögen", 150, 420, beim("s2", "Eigentum"), size=32),
    blk(110, 490, 1040, 76, GRUEN, "s3", [("3. Bestand und Funktionsfähigkeit des Staates", "ExtraBold", 32, INK)]),
    z("und seiner Einrichtungen", 150, 580, beim("s3", "Einrichtungen"), size=32),
    z("so auch das BVerfG im Brokdorf-Beschluss:", 110, 665, "bverfg", "Bold", 32),
    zit("BVerfG, Beschl. v. 14.5.1985 – 1 BvR 233, 341/81,", 150, 712, beim("bverfg", "Brokdorf")),
    zit("BVerfGE 69, 315 (352), Rn. 77 (Zählung DFR)", 150, 748, beim("bverfg", "Brokdorf")),
    ficon("tabler", "shield", IX, IU, 120, "drei", fuell=BLAU, bis="s1"),
    ficon("tabler", "gavel", IX, IU, 120, "s1", fuell=WEISS, bis="s2"),
    ficon("tabler", "heart", IX, IU, 120, "s2", fuell=ROT, bis="s3"),
    ficon("tabler", "building-bank", IX, IU, 140, "s3", fuell=WEISS),
    *allein("SC", [("drei", "ruhig"), ("s2", "froh"), ("bverfg", "denkt")]),
]))

# ===========================================================================================================================
# E Legaldefinition Sachsen, Regel, öffentliche Ordnung
# ===========================================================================================================================
W4 = ("„öffentliche Sicherheit: die Unverletzlichkeit der Rechtsordnung, der subjektiven Rechte und Rechtsgüter einzelner "
      "Personen sowie des Bestandes, der Einrichtungen und Veranstaltungen des Staates oder sonstiger Träger der "
      "Hoheitsgewalt“")
titel_sn = titel(glyphen("Sachsen hat es ins Gesetz geschrieben"), 100, 75, "sachsen", 42)
w4, w4_y = wortlaut(70, 145, 1120, W4, "§ 4 Nr. 1 SächsPVDG (Begriffsbestimmungen)", "sachsen", size=30)
folie([("sachsen", f"{OS} › Legaldefinition in Sachsen"), ("regel", f"{OS} › Regel: drohende Straftat"),
       ("ordnung", "Abgrenzung · öffentliche Ordnung")], rechts_frei([
    titel_sn, *w4,
    z("Regel: Gefährdung der öffentlichen Sicherheit,", 110, w4_y + 30, "regel", "Bold", 32),
    z("wenn eine strafbare Verletzung dieser", 150, w4_y + 75, beim("regel", "strafbare"), "Bold", 32),
    z("Schutzgüter droht", 150, w4_y + 120, beim("regel", "Schutzgüter"), "Bold", 32),
    zit("BVerfGE 69, 315 (352), Rn. 77 (DFR)", 150, w4_y + 166, beim("regel", "droht")),
    z("Abgrenzung: öffentliche Ordnung =", 110, w4_y + 225, "ordnung", "Bold", 32),
    z("ungeschriebene Regeln, nach herrschender", 150, w4_y + 270, beim("ordnung", "ungeschriebene"), size=32),
    z("Anschauung unerlässlich für ein geordnetes", 150, w4_y + 315, beim("ordnung", "Anschauung"), size=32),
    z("Zusammenleben", 150, w4_y + 360, beim("ordnung", "Zusammenleben"), size=32),
    ficon("tabler", "book", IX, IU, 120, "sachsen", fuell=WEISS, bis="regel"),
    ficon("tabler", "alert-triangle", IX, IU, 120, "regel", fuell=GELB, bis="ordnung"),
    ficon("tabler", "users", IX, IU, 140, "ordnung", fuell=WEISS),
    *allein("NE", [("sachsen", "ruhig"), ("regel", "ernst"), ("ordnung", "denkt")]),
]))
assert w4_y + 400 <= 950, w4_y

# ===========================================================================================================================
# F Fall: 1. Rechtsordnung – § 303 Abs. 2 StGB, Gestaltungssatzung
# ===========================================================================================================================
W303 = ("„Ebenso wird bestraft, wer unbefugt das Erscheinungsbild einer fremden Sache nicht nur unerheblich und nicht nur "
        "vorübergehend verändert.“")
w303, w303_y = wortlaut(70, 140, 1120, W303, "§ 303 Abs. 2 StGB (Sachbeschädigung)", "wl303", size=30,
                        marken=[("unbefugt", beim("wl303", "unbefugt")), ("Erscheinungsbild", beim("wl303", "Erscheinungsbild")),
                                ("fremden", beim("wl303", "fremden")),
                                ("nicht nur unerheblich", beim("wl303", "unerheblich")),
                                ("vorübergehend", beim("wl303", "vorübergehend"))])
RO = "Fall › 1. Rechtsordnung"
folie([("pr1", f"{RO}: Sachbeschädigung?"), ("wl303", f"{RO}: § 303 Abs. 2 StGB"), ("fremd", f"{RO}: fremde Sache?"),
       ("satzung", f"{RO}: Gestaltungssatzung?"), ("rok", f"{RO}: nicht verletzt")], rechts_frei([
    titel(glyphen("1. Rechtsordnung: Sachbeschädigung?"), 100, 70, "pr1", 42),
    *w303,
    *okz("Bild groß und dauerhaft", w303_y + 25, "dauer", size=32),
    *neinz("fremde Sache? Die Garage gehört Frau Schulze", w303_y + 80, beim("fremd", "gehört"), "Bold", 32),
    blk(140, w303_y + 140, 1010, 70, HELLROT, "keine", [("keine Straftat", "ExtraBold", 34, INK)]),
    z("Gestaltungssatzung möglich:", 110, w303_y + 240, "satzung", "Bold", 32),
    zit("§ 89 Abs. 1 Nr. 1 BauO NRW 2018: „äußere Gestaltung baulicher Anlagen“", 150, w303_y + 285,
        beim("satzung", "Gestaltung")),
    *neinz("hier: keine erlassen", w303_y + 325, beim("satzung", "nicht"), size=32),
    blk(110, w303_y + 390, 1040, 76, GRUEN, "rok", [("Rechtsordnung nicht verletzt", "ExtraBold", 36, INK)]),
    ficon("tabler", "spray", 1560, 300, 90, "pr1", fuell=ROT),
    *zwei("GB", [("pr1", "skeptisch"), ("fremd", "sorge")], "SC", [("pr1", "ruhig"), ("fremd", "froh")]),
]))
assert w303_y + 480 <= 950, w303_y

# ===========================================================================================================================
# G Fall: 2. Rechte des Einzelnen (§ 903 Satz 1 BGB), 3. Staat, öffentliche Ordnung, Ergebnis
# ===========================================================================================================================
W903 = ("„Der Eigentümer einer Sache kann, soweit nicht das Gesetz oder Rechte Dritter entgegenstehen, mit der Sache nach "
        "Belieben verfahren und andere von jeder Einwirkung ausschließen.“")
w903, w903_y = wortlaut(70, 215, 1120, W903, "§ 903 Satz 1 BGB", "p903", size=30,
                        marken=[("Belieben verfahren", beim("p903", "Belieben")),
                                ("soweit nicht das Gesetz oder Rechte", beim("p903", "soweit")),
                                ("Dritter entgegenstehen", beim("p903", "Dritter"))])
RE = "Fall › 2. Rechte des Einzelnen"
folie([("pr2", f"{RE}"), ("p903", f"{RE}: § 903 BGB"), ("pr3", "Fall › 3. Staat"), ("oo", "Fall › öffentliche Ordnung"),
       ("erg", "Ergebnis · keine Gefahr")], rechts_frei([
    titel(glyphen("2. Rechte des Einzelnen"), 100, 75, "pr2", 42),
    z("betroffen: nur das Eigentum von Frau Schulze", 110, 150, beim("eigen", "Betroffen"), "Bold", 32),
    *w903,
    *neinz("Missfallen des Nachbarn: verletzt kein Recht", w903_y + 22, "geschmack", size=32),
    *neinz("3. Staat: keine staatliche Einrichtung betroffen", w903_y + 82, "pr3", "Bold", 32),
    *neinz("öffentliche Ordnung: keine unerlässliche Regel verletzt", w903_y + 142, "oo", size=32),
    blk(110, w903_y + 215, 1040, 80, HELLROT, "erg", [("keine Gefahr: Polizei darf nicht einschreiten", "ExtraBold", 34, INK)]),
    *zwei("SC", [("pr2", "ruhig"), ("p903", "froh")], "GB", [("pr2", "skeptisch"), ("geschmack", "muede")]),
]))
assert w903_y + 300 <= 950, w903_y

# ===========================================================================================================================
# H Gegenfall: die Garage ist gemietet (Wohnstraße)
# ===========================================================================================================================
DIX = 1730
spray_h = hart(welle("gegen", 840, BLAU))   # Bild schon vorhanden: kein Geräusch ohne sichtbare Handlung
folie([("gegen", "Gegenfall · Die Garage ist gemietet"), ("di1", "Gegenfall · Die Vermieterin")], [
    boden("gegen"),
    hart(ficon("tabler", "sun", 1790, 200, 100, "gegen", fuell=GELB, anim="cut")),
    haus_gebauer("gegen"),
    garage("gegen"),
    hart(pl("Gegenfall", 70, 40, "gegen", fill=PINK, size=36)),
    spray_h, welle("gegen", 875, GRUEN, phase=1.6, amp=12),
    *[e for e in graffiti("gegen", "gegen")[2:]],
    *fig("SC", SCX, BODEN_Y, FHA, [("gegen", "froh"), ("di1", "sorge")], erst="cut"),
    hart(ns("Frau Schulze", SCX, BODEN_Y, "gegen", NFARBE["SC"])),
    hart(ficon("tabler", "spray", HX_ - 14, HY_ + 40, 62, "gegen", fuell=ROT)),
    *fig("NE", NEX - 20, BODEN_Y, FHA, [("gegen", "ruhig"), ("di1", "denkt")], erst="cut"),
    hart(ns("Herr Neumann", NEX - 20, BODEN_Y, "gegen", NFARBE["NE"])),
    *fig("GB", GBX, BODEN_Y, FHA, [("gegen", "skeptisch_r")], erst="cut"),
    hart(ns("Herr Gebauer", GBX, BODEN_Y, "gegen", NFARBE["GB"])),
    pl("Mieterin: Frau Schulze", SCX, 360, beim("gegen", "gemietet"), fill=WEISS, size=30, anker="m"),
    *fig("DI", DIX, BODEN_Y, FHA, [(beim("gegen", "Eigentümerin"), "aerger")], bis="di1"),
    *redet("DI_redet", DIX, BODEN_Y, FHA, "di1", "gfremd"),
    ns("Frau Dietz", DIX, BODEN_Y, beim("gegen", "Eigentümerin"), NFARBE["DI"]),
    pl("Eigentümerin: Frau Dietz (Vermieterin)", 1250, 40, beim("gegen", "Eigentümerin"), fill=LILA, size=30),
    blase("sprech", 640, 190, "di1", 1220, 200, inhalt=["Das ist meine Garage.", "Davon war nie die Rede!"], textsize=34,
          figur=("DI_redet", DIX, BODEN_Y, FHA)),
])

# ===========================================================================================================================
# I Gegenfall: Subsumtion – fremde Sache, § 303 Abs. 2, konkrete Gefahr
# ===========================================================================================================================
GF = "Gegenfall"
folie([("gfremd", f"{GF} › fremde Sache"), ("g303", f"{GF} › Sachbeschädigung, § 303 Abs. 2 StGB"),
       ("gschutz", f"{GF} › Rechtsordnung und Eigentum verletzt"), (beim("ggefahr", "konkrete"), f"{GF} › konkrete Gefahr"),
       ("gdarf", f"{GF} › Polizei darf einschreiten")], rechts_frei([
    *tafel("gfremd", "Gegenfall: die Garage ist gemietet", size=44),
    *okz("Garage gehört Frau Dietz: für Frau Schulze fremd", 180, beim("gfremd", "fremde"), "Bold", 32),
    *okz("ohne Erlaubnis: unbefugt", 245, beim("gfremd", "Erlaubnis"), size=32),
    *okz("deutlich und dauerhaft verändert", 305, beim("gfremd", "deutlich"), size=32),
    blk(110, 375, 1040, 76, GELB, "g303", [("Sachbeschädigung, § 303 Abs. 2 StGB", "ExtraBold", 34, INK)]),
    z("verletzt: die Rechtsordnung", 150, 490, "gschutz", "Bold", 32),
    z("und das Eigentum von Frau Dietz", 150, 535, beim("gschutz", "Eigentum"), "Bold", 32),
    *okz("jeder weitere Sprühstoß vergrößert den Schaden:", 600, "ggefahr", size=32),
    z("konkrete Gefahr", 185, 645, beim("ggefahr", "konkrete"), "Bold", 32),
    blk(110, 725, 1040, 80, GRUEN, "gdarf", [("Herr Neumann darf einschreiten", "ExtraBold", 36, INK)]),
    *zwei("DI", [("gfremd", "aerger"), ("gdarf", "ruhig")], "NE", [("gfremd", "denkt"), ("ggefahr", "ernst")]),
]))

# ===========================================================================================================================
# J Nur private Rechte? Kreide
# ===========================================================================================================================
PR = "Schutz privater Rechte"
folie([("subs", f"{PR} · nur private Rechte?"), ("kreide", f"{PR} › Kreide statt Lack"), ("privat", f"{PR} › Mietvertrag, Eigentum")],
      rechts_frei([
    *tafel("subs", "Und wenn nur private Rechte betroffen sind?", size=40),
    z("Angenommen: Kreide statt Sprühlack,", 110, 185, "kreide", "Bold", 32),
    z("der nächste Regen wäscht sie ab", 150, 232, beim("kreide", "Regen"), size=32),
    *neinz("nur vorübergehend: § 303 scheidet aus", 300, beim("kreide", "vorübergehend"), "Bold", 32),
    z("es bleiben die Rechte von Frau Dietz:", 110, 390, "privat", "Bold", 32),
    z("aus Mietvertrag und Eigentum", 150, 437, beim("privat", "Mietvertrag"), size=32),
    blk(110, 510, 1040, 76, GELB, beim("privat", "private"), [("private Rechte", "ExtraBold", 36, INK)]),
    ficon("tabler", "cloud-rain", IX, IU, 140, beim("kreide", "Regen"), fuell=BLAU, bis="privat"),
    ficon("tabler", "contract", IX, IU, 120, "privat", fuell=WEISS),
    *zwei("SC", [("subs", "denkt"), ("kreide", "froh")], "DI", [("subs", "denkt"), ("privat", "aerger")]),
]))

# ===========================================================================================================================
# K Subsidiarität: Wortlaut § 1 Abs. 2 PolG NRW
# ===========================================================================================================================
W12 = ("„Der Schutz privater Rechte obliegt der Polizei nach diesem Gesetz nur dann, wenn gerichtlicher Schutz nicht "
       "rechtzeitig zu erlangen ist und wenn ohne polizeiliche Hilfe die Verwirklichung des Rechts vereitelt oder wesentlich "
       "erschwert werden würde.“")
w12, w12_y = wortlaut(70, 140, 1120, W12, "§ 1 Abs. 2 PolG NRW (Schutz privater Rechte)", "wl12", size=30,
                      marken=[("nur dann", beim("wl12", "nur")), ("gerichtlicher Schutz", beim("wl12", "gerichtlicher")),
                              ("rechtzeitig", beim("wl12", "rechtzeitig")), ("vereitelt", beim("wl12", "vereitelt")),
                              ("wesentlich", beim("wl12", "wesentlich"))])
folie([("wl12", f"{PR} › § 1 Abs. 2 PolG NRW"), (beim("kgericht", "Gericht"), f"{PR} › Gericht erreichbar"),
       ("straf", f"{PR} › bei drohender Straftat: Rechtsordnung")], rechts_frei([
    titel(glyphen("Subsidiarität beim Schutz privater Rechte"), 100, 70, "wl12", 40),
    *w12,
    *neinz("Kreide abwaschbar, Gericht erreichbar:", w12_y + 30, "kgericht", "Bold", 32),
    z("kein Fall für die Polizei", 185, w12_y + 75, beim("kgericht", "Fall"), "Bold", 32),
    *okz("droht eine Straftat: Polizei schützt zugleich", w12_y + 150, "straf", size=32),
    z("die Rechtsordnung, die Klausel sperrt nicht", 185, w12_y + 195, beim("straf", "Rechtsordnung"), size=32),
    zit("vgl. § 1 Abs. 1 Satz 2 PolG NRW: „Straftaten zu verhüten“", 185, w12_y + 245, beim("straf", "sperrt")),
    ficon("tabler", "gavel", IX, IU, 120, beim("wl12", "gerichtlicher"), fuell=WEISS),
    *allein("DI", [("wl12", "denkt"), ("kgericht", "ruhig")]),
]))
assert w12_y + 290 <= 950, w12_y

# ===========================================================================================================================
# L Länder-Overlay: Generalklausel und Schutz privater Rechte (nur am Landesportal geprüfte Normen)
# ===========================================================================================================================
def zelle(text, x, y, cue, size=30, stil="Regular", breite=330, farbe=INK):
    w = F(stil, size).getlength(glyphen(text))
    assert w <= breite, f"Zelle zu breit: {text} ({w:.0f} > {breite})"
    return z(text, x, y, cue, stil, size, farbe=farbe)


def linie(x0, y0, x1, y1, cue, breite=4, farbe=INK):
    return linienzug([(x0, y0), (x1, y1)], cue, breite=breite, farbe=farbe)


CL, CG, CP = 110, 420, 800                  # Spalten: Land, Generalklausel, Schutz privater Rechte
TY = 230
ZEILEN = [("tnrw", "Nordrhein-Westfalen", "§ 8 Abs. 1 PolG NRW", "acht", "§ 1 Abs. 2 PolG NRW", "eins"),
          ("tbb", "Brandenburg", "§ 10 Abs. 1 BbgPolG", "zehn", "§ 1 Abs. 2 BbgPolG", "ebenfalls"),
          ("tsn", "Sachsen", "§ 12 Abs. 1 SächsPVDG", "zwölf", "§ 2 Abs. 2 SächsPVDG", "zwei")]
els_t = [*tafel("tab", "Länder-Overlay: gleiche Struktur, andere Nummern", size=38),
         zelle("Land", CL, TY - 60, "tab", 28, "Bold", farbe=TEXT), zelle("Generalklausel", CG, TY - 60, "tab", 28, "Bold", farbe=TEXT),
         zelle("Schutz privater Rechte", CP, TY - 60, "tab", 28, "Bold", breite=360, farbe=TEXT),
         linie(110, TY - 12, 1160, TY - 12, "tab", breite=3)]
for i, (c, land, gk, wg, pr, wp) in enumerate(ZEILEN):
    y = TY + 10 + i * 105
    els_t += [zelle(land, CL, y, c, 28, "Bold", breite=300), zelle(gk, CG, y, beim(c, wg), 30, breite=360),
              zelle(pr, CP, y, beim(c, wp), 30, breite=360)]
    if i < 2:
        els_t.append(linie(110, y + 80, 1160, y + 80, c, breite=2, farbe=(200, 200, 205, 255)))
els_t += [zelle("+ nur auf Antrag der berechtigten Person", CP - 380, TY + 10 + 2 * 105 + 44, beim("tsn", "Antrag"), 28,
                "Bold", breite=740, farbe=DROT),
          z("andere Länder: eigene Nummern, im Landesgesetz nachschlagen", 110, 640, "teigen", "Bold", 30),
          zit("geprüft an recht.nrw.de, bravors.brandenburg.de,", 110, 700, beim("teigen", "Landesgesetz")),
          zit("revosax.sachsen.de (Abruf 6.10.2026)", 110, 738, beim("teigen", "Landesgesetz")),
          ficon("tabler", "map-2", IX, IU, 140, "tab", fuell=WEISS),
          *allein("NE", [("tab", "ruhig"), ("tsn", "denkt"), ("teigen", "froh")])]
folie([("tab", "Länder-Overlay · gleiche Struktur, andere Nummern"), ("tnrw", "Länder-Overlay › Nordrhein-Westfalen"),
       ("tbb", "Länder-Overlay › Brandenburg"), ("tsn", "Länder-Overlay › Sachsen"), (beim("tsn", "Antrag"), "Länder-Overlay › Sachsen: zusätzlich Antrag"),
       ("teigen", "Länder-Overlay › dein Landesgesetz")], rechts_frei(els_t))

# ===========================================================================================================================
# M Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Rechtsordnung zuerst"), ("tipp2", "Klausurtipp › jedes Merkmal genau lesen"),
       ("tipp3", "Klausurtipp › Subsidiaritätsklausel")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Prüfe zuerst die Rechtsordnung,", 200, 200, beim("tipp", "Prüfe"), "Bold", 36),
    z("vor allem Straf- und Bußgeldnormen", 200, 252, beim("tipp", "Straf"), size=34),
    z("Lies jedes Merkmal genau:", 200, 345, "tipp2", "Bold", 34),
    z("bei der Sachbeschädigung entscheidet", 200, 398, beim("tipp2", "Sachbeschädigung"), size=34),
    z("oft das Wort „fremd“", 200, 448, beim("tipp2", "fremd"), "Bold", 34),
    z("Bleiben nur private Rechte übrig:", 200, 545, "tipp3", "Bold", 34),
    z("Subsidiaritätsklausel ansprechen", 200, 598, beim("tipp3", "Subsidiaritätsklausel"), size=34),
    zit("z. B. § 1 Abs. 2 PolG NRW", 200, 648, beim("tipp3", "an")),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# N Klausurschema (Aufbau Punkt für Punkt)
# ===========================================================================================================================
REIHEN = [("q1", 0, "1. Unverletzlichkeit der Rechtsordnung"),
          (beim("q1", "Verstößt"), 1, "Verstößt das Verhalten gegen ein Gesetz?"),
          ("q2", 0, "2. Rechte und Rechtsgüter des Einzelnen"),
          (beim("q2", "Wessen"), 1, "Wessen Recht ist betroffen?"),
          ("q3", 0, "3. Bestand und Funktionsfähigkeit des Staates"),
          ("q4", 0, "4. Bei rein privaten Rechten: Subsidiarität"),
          (beim("q4", "Gerichtsschutz"), 1, "Gerichtsschutz nicht rechtzeitig, Recht sonst vereitelt"),
          ("q5", 0, "5. Ergebnis: Gefahr für die öffentliche Sicherheit, ja oder nein")]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Klausurschema: Gefahr für die öffentliche Sicherheit?"), 110, 90, "sch", 48)]
y = 215
for c, ebene, text in REIHEN:
    x = (130, 200)[ebene]
    els_sch.append(z(text, x, y, c, ("ExtraBold", "Regular")[ebene], (38, 34)[ebene], rechts=1800, farbe=(INK, TEXT)[ebene]))
    y += {0: 78, 1: 92}[ebene]
assert y <= 960, y
folie([("sch", "Klausurschema"), ("q1", "Klausurschema › 1. Rechtsordnung"), ("q2", "Klausurschema › 2. Rechte des Einzelnen"),
       ("q3", "Klausurschema › 3. Staat"), ("q4", "Klausurschema › 4. Subsidiarität"), ("q5", "Klausurschema › 5. Ergebnis")],
      els_sch)

# ===========================================================================================================================
# O Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Die öffentliche Sicherheit schützt die ", 0), ("Rechtsordnung", "a"), (",", 0)],
                 [("die ", 0), ("Rechte des Einzelnen", "b"), (" und den ", 0), ("Staat", "c"), (".", 0)]], 750, 280, 42,
                beim("merke", "Die"), {"a": beim("merke", "Rechtsordnung"), "b": beim("merke", "Rechte"),
                                       "c": beim("merke", "Staat")}),
    *markertext([[("Die eigene Garage zu bemalen, ist kein Fall", 0)], [("für die Polizei, solange ", 0), ("kein Gesetz", "d"),
                 (" es verbietet.", 0)]], 750, 470, 42, "m2", {"d": beim("m2", "kein", 2)}),
    *markertext([[("Und private Rechte schützt sie nur, wenn", 0)], [("gerichtliche Hilfe ", 0), ("zu spät", "e"),
                 (" käme.", 0)]], 750, 660, 42, "m3", {"e": beim("m3", "zu")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
