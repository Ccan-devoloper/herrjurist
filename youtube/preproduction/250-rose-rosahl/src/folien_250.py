"""Folge 250 · Rose-Rosahl-Fall: Error in persona des Täters – und der Anstifter? – Serienstandard Open Peeps (Katzenkönig).
Übungsfall nach dem Plan-Hook (Personen fiktiv): Die Bauunternehmerin Edeltraud bittet ihren Bekannten Vinzenz, ihren Konkurrenten zu
töten, und gibt ihm ein Foto; am Abend wartet Vinzenz am dunklen Kanalweg und tötet einen Spaziergänger, den er für den Konkurrenten
hält. DARSTELLUNG: keine Waffe, kein Schuss, keine Leiche im Bild – nur Dunkelheit, Weg, Kanal, Mond, Silhouetten-Andeutung des
Spaziergängers (einheitlich dunkle Open-Peeps-Fläche ohne Gesicht), Pillen; das Opfer wird nicht gezeigt; reale historische Personen
(Rose, Rosahl, Hoferben-Fall) nicht als Figuren. Danach A. Vinzenz (§ 212, § 16 Abs. 1 S. 1 als Wortlautkarte, error in persona),
B. Edeltraud (§ 26 als Wortlautkarte; Unbeachtlichkeitslehre PrObTr GA 7, 322; Aberratio-Lösung; BGHSt 37, 214), Ergebnis,
Blutbad-Argument, Klausurtipp, Schema, Merksatz mit Lexi. Szenen laut ../SZENENPLAN.md.
Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/feld/requisit/tisch/fenster als eigene Kopie aus Folge 247
(gemeinsame Dateien unverändert); neu: folie_nacht() (Nachtverlauf, nur für die Kanalszene, weil die Dunkelheit die Verwechslung
trägt), kanal(), foto_icon().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut StGB nach gesetze-im-internet.de, Abruf 08.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_250/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_250/" in n:
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
NAME = {"ED": "Edeltraud", "VI": "Vinzenz"}
NFARBE = {"ED": PINK, "VI": BLAU}
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



# --- Folge 250: Raumbausteine -----------------------------------------------------------------------------------------------
HOLZ = (214, 160, 110, 255)
LEDER = (150, 96, 58, 255)
SAND = (230, 205, 150, 255)
NACHTBLAU = (60, 72, 120, 255)


def tisch(x, cue, breite=300, hoehe=150):
    """Tisch: Platte und zwei Beine (Tuschekontur)."""
    return [hart(feld(x, BODEN - hoehe, breite, 22, cue, fill=HOLZ, rand=4, rund=6, name="tischplatte")),
            hart(linienzug([(x + 30, BODEN - hoehe + 22), (x + 30, BODEN)], cue, breite=6, farbe=INK)),
            hart(linienzug([(x + breite - 30, BODEN - hoehe + 22), (x + breite - 30, BODEN)], cue, breite=6, farbe=INK))]


def fenster(x, y, w, h, cue, fill):
    """Fenster mit Kreuzsprosse (Tuschekontur)."""
    return [hart(feld(x, y, w, h, cue, fill=fill, rand=5, rund=8, name="fenster")),
            hart(linienzug([(x + w // 2 + 6, y + 6), (x + w // 2 + 6, y + h + 6)], cue, breite=5, farbe=INK)),
            hart(linienzug([(x + 6, y + h // 2 + 6), (x + w + 6, y + h // 2 + 6)], cue, breite=5, farbe=INK))]

WEG_ = (150, 140, 118, 255)                 # Kanalweg (Kies) in der Nacht
WASSER = (52, 86, 140, 255)
BAUM = (70, 112, 84, 255)
WOLKE = (190, 194, 206, 255)
BG_FARBE["nacht"] = (78, 88, 128, 255)      # Nachtverlauf (render_250.hintergrund), nur Szene A2
PFAD_FARBE["nacht"] = (250, 246, 236, 235)  # Prüfpfad auf dem dunklen Grund hell
bausteine.BG_FARBE.update(BG_FARBE); bausteine.PFAD_FARBE.update(PFAD_FARBE)


def folie_nacht(pfade, els):
    """Kanalszene bei Nacht: die Dunkelheit trägt die Verwechslung (Grund im Szenenplan)."""
    FOLIEN.append(dict(bg="nacht", pfade=pfade, els=els))


def kanal(cue):
    """Kanalweg mit Wasser darunter (Tuschekontur, Palettenflächen)."""
    return [hart(feld(40, BODEN - 4, 1840, 44, cue, fill=WEG_, rand=4, rund=8, name="weg")),
            hart(feld(40, BODEN + 46, 1840, 100, cue, fill=WASSER, rand=4, rund=8, name="kanal")),
            *[hart(ficon("tabler", "ripple", x, BODEN + 126, 90, cue, fuell=None)) for x in (260, 760, 1260, 1700)]]


# ===========================================================================================================================
# A1 Fall: Edeltraud und Vinzenz im Büro der Baufirma
# ===========================================================================================================================
EDX, VIX = 520, 1340
TX = 760
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
GIB = beim("foto", "gibt"), beim("foto", "Foto", ende=True)
folie([(NULL, "Fall · Edeltraud und ihre Baufirma"), ("konk", "Fall · Der Konkurrent"),
       ("auftrag", "Fall · Der Auftrag an Vinzenz"), ("foto", "Fall · Das Foto"), ("ed1", "Fall · Am Kanal"),
       ("vi1", "Fall · Vinzenz sagt zu")], [
    boden(NULL),
    *fenster(1560, 180, 260, 200, NULL, BLAUHELL),
    hart(ficon("tabler", "crane", 1640, 372, 130, NULL, fuell=GELB, anim="cut")),
    *tisch(TX, NULL, breite=340),
    bis_(hart(pl("Edeltraud führt eine Baufirma.", 70, 30, NULL, fill=GELB, size=32)), "konk"),
    # Edeltraud links (blickt nach rechts zu Vinzenz), Vinzenz rechts (blickt nach links)
    *fig("ED", EDX, BODEN, FH, [(NULL, "ruhig_r"), ("konk", "ernst_r"), ("auftrag", "denkt_r"), ("foto", "ernst_r")],
         bis="ed1", erst="cut"),
    *redet("ED_redet_r", EDX, BODEN, FH, "ed1", "vi1"),
    *fig("ED", EDX, BODEN, FH, [("vi1", "ruhig_r")], erst="cut"),
    hart(ns(NAME["ED"], EDX, BODEN, NULL, NFARBE["ED"])),
    *fig("VI", VIX, BODEN, FH, [(NULL, "ruhig"), ("konk", "ruhig"), ("auftrag", "denkt"), ("foto", "ernst"), ("ed1", "denkt")],
         bis="vi1", erst="cut"),
    *redet("VI_redet", VIX, BODEN, FH, "vi1", "nacht"),
    hart(ns(NAME["VI"], VIX, BODEN, NULL, NFARBE["VI"])),
    bis_(pl("Ihr Konkurrent nimmt ihr einen Auftrag nach dem anderen weg.", 70, 30, "konk", fill=ORANGE, size=32), "auftrag"),
    bis_(ficon("tabler", "file-x", 860, BODEN - 150, 80, beim("konk", "Auftrag"), fuell=WEISS), "foto"),
    bis_(pl("Sie bittet ihren Bekannten Vinzenz, ihn zu töten.", 70, 30, "auftrag", fill=LILA, size=32), "foto"),
    bis_(pl("Sie gibt ihm ein Foto.", 70, 30, "foto", fill=GELB, size=32), "ed1"),
    bewegt(ficon("tabler", "photo", 1030, BODEN - 150, 80, GIB[0], fuell=BLAUHELL, anim="cut"), GIB[0], GIB[1], -420, -90),
    blase("sprech", 580, 270, "ed1", 800, 250, inhalt=["Er geht jeden Abend", "allein am Kanal spazieren.", "Dort erwischst du ihn."],
          textsize=31, figur=("ED_redet_r", EDX, BODEN, FH), bis="vi1"),
    blase("sprech", 560, 220, "vi1", 1060, 250, inhalt=["Gut. Morgen Abend", "warte ich dort auf ihn."], textsize=32,
          figur=("VI_redet", VIX, BODEN, FH), bis="nacht"),
])

# ===========================================================================================================================
# A2 Fall: der Abend am Kanalweg (Nacht) – nur Silhouetten-Andeutung, keine Waffe, kein Schuss, kein Opfer im Bild
# ===========================================================================================================================
VIX2, SPX = 1480, 820
LAUF = beim("schritte", "Ein"), beim("schritte", "Foto", ende=True)
schatten = bewegt(peep_voll("SP_schatten_r", SPX, BODEN, FH - 10, "schritte", anim="cut", bis="tat"), LAUF[0], LAUF[1], -520)
szene(schatten, "250schritte*", 0.8, round(T_(LAUF[0]) - T_("schritte"), 3))   # Schritte, sobald die Silhouette geht
folie_nacht([("nacht", "Fall · Am Abend am Kanalweg"), ("schritte", "Fall · Schritte im Dunkeln"),
             ("vi2", "Fall · „Da ist er.“"), ("tat", "Fall · Vinzenz tötet den Mann"),
             ("irrtum", "Fall · Es ist ein Spaziergänger")], [
    *kanal("nacht"),
    bis_(hart(mond(1250, 170, 48, "nacht")), None),
    hart(ficon("ph", "tree", 1750, BODEN - 2, 230, "nacht", fuell=BAUM, anim="cut")),
    *fig("VI", VIX2, BODEN, FH, [("nacht", "ernst"), ("schritte", "denkt")], bis="vi2", erst="cut"),
    *redet("VI_redet", VIX2, BODEN, FH, "vi2", "tat"),
    *fig("VI", VIX2, BODEN, FH, [("tat", "ernst"), ("irrtum", "angst")], erst="cut"),
    hart(ns(NAME["VI"], VIX2, BODEN, "nacht", NFARBE["VI"])),
    bis_(pl("Am nächsten Abend steht Vinzenz im Dunkeln am Kanalweg.", 70, 30, "nacht", fill=BLAUHELL, size=32), "schritte"),
    schatten,
    bis_(pl("Schritte. Ein Mann kommt näher.", 70, 30, "schritte", fill=WEISS, size=32), "vi2"),
    bis_(pl("Statur und Mantel passen zum Foto.", 70, 94, beim("schritte", "Statur"), fill=GELB, size=30), "vi2"),
    bis_(ficon("tabler", "photo", 1180, 400, 90, beim("schritte", "Statur"), fuell=BLAUHELL), "vi2"),
    blase("sprech", 340, 150, "vi2", 1150, 260, inhalt=["Da ist er."], textsize=34, figur=("VI_redet", VIX2, BODEN, FH),
          bis="tat"),
    ficon("tabler", "cloud", 1270, 230, 170, "tat", fuell=WOLKE),
    bis_(pl("Vinzenz tötet den Mann.", 70, 30, "tat", fill=WEISS, size=32), "irrtum"),
    pl("Doch es ist nicht der Konkurrent,", 70, 30, "irrtum", fill=ROT, size=32),
    pl("sondern ein Spaziergänger, der ihm nur ähnlich sieht.", 70, 94, beim("irrtum", "sondern"), fill=WEISS, size=30),
    ficon("tabler", "photo", 1180, 400, 90, "irrtum", fuell=BLAUHELL),
    nein(1240, 330, beim("irrtum", "nicht"), gr=26),
])

# ===========================================================================================================================
# A3 Die Frage
# ===========================================================================================================================
folie([("frage", "Die Frage · Der Falsche ist tot"), ("frage2", "Die Frage · Edeltraud Anstifterin?")], [
    *tafel("frage", "Die Frage"),
    z("Vinzenz hat den Falschen getötet.", 110, 200, "frage", "Bold", 38),
    blk(110, 300, 1040, 90, GELB, "frage2", [("Ist Edeltraud trotzdem Anstifterin zum Totschlag?", "ExtraBold", 34, INK)]),
    blk(110, 430, 1040, 90, LILAHELL, beim("frage2", "obwohl"), [("Obwohl sie diesen Mann nie treffen wollte?", "ExtraBold", 34, INK)]),
    *requisit([("frage", ("tabler", "photo-x", 120, BLAUHELL), "der Falsche", WEISS),
               ("frage2", ("tabler", "scale", 120, GELB), "Anstiftung?", GELB)]),
    *paar("ED", [("frage", "sorge"), ("frage2", "denkt")], "VI", [("frage", "angst"), ("frage2", "muede")]),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_250(cue, absaetze, frage):
    els = [karte(140, 40, 1640, 950, cue, fill=HELL), titel("Sachverhalt", 210, 70, cue, 56)]
    y = 160
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=34, zeilenabstand=1.28)
        els += e; y += 18
    assert y + 70 <= 985, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 4, cue, fill=PINK, size=34))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_250("sv", [
    "Edeltraud führt eine Baufirma. Ihr Konkurrent nimmt ihr einen Auftrag nach dem anderen weg. Sie bittet ihren "
    "Bekannten Vinzenz, den Konkurrenten zu töten, und gibt ihm ein Foto: „Er geht jeden Abend allein am Kanal spazieren. "
    "Dort erwischst du ihn.“ Vinzenz sagt zu.",
    "Am nächsten Abend wartet Vinzenz im Dunkeln am Kanalweg. Ein Mann kommt näher, Statur und Mantel passen zum Foto. "
    "Vinzenz hält ihn für den Konkurrenten und tötet ihn. Es ist ein Spaziergänger, der dem Konkurrenten nur ähnlich sieht.",
], "Ist Edeltraud Anstifterin zum Totschlag am Spaziergänger?")

# ===========================================================================================================================
# C1 A. Vinzenz: objektiver Tatbestand, § 16 Abs. 1 Satz 1 (Wortlautkarte)
# ===========================================================================================================================
PA = "A. Vinzenz, § 212 StGB"
w16, w16_y = wortlaut(80, 350, 1100, "„Wer bei Begehung der Tat einen Umstand nicht kennt, der zum gesetzlichen Tatbestand "
                      "gehört, handelt nicht vorsätzlich.“", "§ 16 Abs. 1 Satz 1 StGB", beim("p16", "Nach"),
                      marken=[("Umstand", beim("p16", "Umstand")), ("gesetzlichen Tatbestand", beim("p16", "gesetzlichen"))],
                      size=34)
folie([("aufbau", "A. Vinzenz · Zuerst der Täter"), ("t_obj", f"{PA} › Objektiver Tatbestand (+)"),
       ("p16", f"{PA} › Vorsatz? § 16 Abs. 1 Satz 1"), ("umstand", f"{PA} › Vorsatz › Tatumstand „einen Menschen“")], [
    *tafel("aufbau", "A. Vinzenz: Totschlag, § 212 StGB"),
    z("Zuerst der Täter", 110, 172, "aufbau", "Bold", 34),
    *okz("Objektiver Tatbestand: einen Menschen getötet", 236, "t_obj", "Bold", 34),
    z("Vorsatz?", 110, 296, "p16", "ExtraBold", 34),
    *w16,
    z("Zum Tatbestand gehört nur: „einen Menschen“", 110, w16_y + 30, "umstand", "Bold", 34),
    z("Wer dieser Mensch ist, gehört nicht dazu.", 110, w16_y + 84, beim("umstand", "Wer"), "Bold", 34),
    *requisit([("aufbau", ("tabler", "list-check", 110, WEISS), "Täter zuerst", WEISS),
               ("t_obj", ("tabler", "book", 110, WEISS), "§ 212 StGB", WEISS),
               ("p16", ("tabler", "book", 110, BLAUHELL), "§ 16 StGB", BLAUHELL),
               ("umstand", ("tabler", "zoom-question", 110, GELB), "Wer genau?", GELB)]),
    *stehend("VI", FX, [("aufbau", "ruhig"), ("t_obj", "ernst"), ("p16", "denkt"), ("umstand", "sorge")]),
])
assert w16_y + 140 <= 900, w16_y

# ===========================================================================================================================
# C2 A. Vinzenz: error in persona – unbeachtlich; Ergebnis § 212
# ===========================================================================================================================
folie([("eip", f"{PA} › Vorsatz › error in persona"), ("gleich", f"{PA} › Vorsatz › gleichwertige Objekte: unbeachtlich"),
       ("t_erg", f"{PA} › Ergebnis: § 212 (+)"), ("f68", "A. Vinzenz › Tatbestandsirrtum: Folge 068")], [
    *tafel("eip", "A. Vinzenz: error in persona"),
    z("Wollte genau den Mann töten, den er vor sich sah", 110, 180, "eip", "Bold", 34),
    blk(110, 250, 1040, 90, GELB, beim("eip", "irrte"), [("error in persona: Irrtum nur über die Identität", "ExtraBold", 34, INK)]),
    *okz("Gleichwertige Objekte (Mensch – Mensch): unbeachtlich", 400, "gleich", "Bold", 33),
    zit("BGHSt 37, 214, 216; BGHSt 11, 268, 270", 185, 454, beim("gleich", "unbeachtlich")),
    *plusminus("Vinzenz: Totschlag, § 212 StGB", 110, 540, "t_erg", True, size=36, stil="ExtraBold"),
    z("Mordmerkmale: hier offen", 110, 610, beim("t_erg", "Ob"), size=34),
    zit("Mehr dazu: Folge 068 (Tatbestandsirrtum)", 110, 690, "f68"),
    *requisit([("eip", ("tabler", "photo", 110, BLAUHELL), "Identität?", BLAUHELL),
               ("gleich", ("tabler", "scale", 120, HELLGRUEN), "gleichwertig", HELLGRUEN),
               ("t_erg", ("tabler", "scale", 120, HELLGRUEN), "§ 212 (+)", HELLGRUEN),
               ("f68", ("tabler", "book", 110, WEISS), "Folge 068", WEISS)]),
    *stehend("VI", FX, [("eip", "denkt"), ("gleich", "ernst"), ("t_erg", "muede"), ("f68", "ruhig")]),
])

# ===========================================================================================================================
# D1 B. Edeltraud: § 26 (Wortlautkarte), Haupttat, Bestimmen
# ===========================================================================================================================
PB = "B. Edeltraud, §§ 212, 26 StGB"
w26, w26_y = wortlaut(80, 170, 1100, "„Als Anstifter wird gleich einem Täter bestraft, wer vorsätzlich einen anderen zu dessen "
                      "vorsätzlich begangener rechtswidriger Tat bestimmt hat.“", "§ 26 StGB", beim("p26", "Als"),
                      marken=[("vorsätzlich", beim("p26", "vorsätzlich")), ("vorsätzlich", beim("p26", "vorsätzlich", 2)),
                              ("bestimmt", beim("p26", "bestimmt"))], size=34)
folie([("p26", "B. Edeltraud · § 26 StGB, Wortlaut"), ("haupt", f"{PB} › Objektiv › Haupttat (+)"),
       ("bestimmt", f"{PB} › Objektiv › Bestimmen (+)")], [
    *tafel("p26", "B. Edeltraud: Anstiftung, §§ 212, 26"),
    *w26,
    *okz("Haupttat: vorsätzlicher, rechtswidriger Totschlag", w26_y + 40, "haupt", "Bold", 33),
    z("von Vinzenz", 185, w26_y + 90, beim("haupt", "von"), size=33),
    *okz("Bestimmen: Tatentschluss hervorgerufen", w26_y + 170, "bestimmt", "Bold", 33),
    zit("BGH, Urt. v. 1.7.2021 – 3 StR 84/21, Rn. 13", 185, w26_y + 224, beim("bestimmt", "Tatentschluss")),
    *requisit([("p26", ("tabler", "book", 110, WEISS), "§ 26 StGB", WEISS),
               ("haupt", ("tabler", "scale", 120, HELLGRUEN), "Haupttat (+)", HELLGRUEN),
               ("bestimmt", ("tabler", "bulb", 110, GELB), "Tatentschluss", GELB)]),
    *stehend("ED", FX, [("p26", "ruhig"), ("haupt", "ernst"), ("bestimmt", "denkt")]),
])
assert w26_y + 270 <= 900, w26_y

# ===========================================================================================================================
# D2 B. Edeltraud: doppelter Vorsatz, das Problem
# ===========================================================================================================================
folie([("doppel", f"{PB} › Subjektiv › doppelter Vorsatz"), ("problem", f"{PB} › Vorsatz bzgl. Haupttat: Irrtum unbeachtlich?"),
       ("problem2", f"{PB} › Vorsatz bzgl. Haupttat: aberratio ictus?")], [
    *tafel("doppel", "B. Edeltraud: der Vorsatz"),
    blk(110, 170, 1040, 130, BLAUHELL, "doppel", [("Doppelter Vorsatz:", "ExtraBold", 34, INK),
                                               ("auf die Haupttat und auf das Bestimmen", "Regular", 34, INK)]),
    zit("BGH, Urt. v. 1.7.2021 – 3 StR 84/21, Rn. 13", 110, 316, beim("doppel", "Haupttat")),
    z("Ihr Vorsatz galt aber dem Konkurrenten.", 110, 400, "problem", "Bold", 35),
    blk(110, 470, 1040, 90, GELB, beim("problem", "Ist"), [("Irrtum von Vinzenz auch für sie unbeachtlich?", "ExtraBold", 34, INK)]),
    blk(110, 600, 1040, 90, LILAHELL, "problem2", [("Oder: Fehlgehen der Tat, aberratio ictus?", "ExtraBold", 34, INK)]),
    *requisit([("doppel", ("tabler", "list-check", 110, BLAUHELL), "doppelter Vorsatz", BLAUHELL),
               ("problem", ("tabler", "photo-x", 120, BLAUHELL), "der Falsche", WEISS),
               ("problem2", ("tabler", "target-off", 110, LILAHELL), "aberratio ictus?", LILAHELL)]),
    *stehend("ED", FX, [("doppel", "ernst"), ("problem", "sorge"), ("problem2", "denkt")]),
])

# ===========================================================================================================================
# E1 Ansicht 1: Unbeachtlichkeitslehre – Rose-Rosahl (PrObTr 1859; historischer Fall, Original nicht online verfügbar)
# ===========================================================================================================================
PV = "B. Edeltraud › Vorsatz bzgl. Haupttat"
folie([("rose", f"{PV} › Streitstand"), ("rose2", f"{PV} › 1. Rose-Rosahl-Fall (1859)"),
       ("probtr", f"{PV} › 1. Preußisches Obertribunal"), ("unbeacht", f"{PV} › 1. Unbeachtlichkeitslehre")], [
    *tafel("rose", "1. Der Rose-Rosahl-Fall"),
    z("Die Frage ist alt:", 110, 172, "rose", "Bold", 34),
    z("Rose-Rosahl-Fall, entschieden 1859", 110, 232, "rose2", "ExtraBold", 35),
    z("Holzhändler Rosahl stiftet Arbeiter Rose an,", 110, 292, beim("rose2", "stiftet"), size=34),
    z("einen Mann zu töten.", 110, 342, beim("rose2", "einen"), size=34),
    z("Rose tötet in der Dämmerung einen Schüler.", 110, 392, beim("rose2", "tötet"), "Bold", 34),
    zit("PrObTr, GA 7 (1859), 322 – Original nicht online, nach Sekundärquellen", 110, 446, beim("rose2", "tötet")),
    blk(110, 510, 1040, 130, BLAUHELL, "probtr", [("Preußisches Obertribunal:", "ExtraBold", 34, INK),
                                               ("Irrtum auch für den Anstifter unbeachtlich", "Regular", 34, INK)]),
    z("Unbeachtlichkeitslehre: zur Tötung eines Menschen", 110, 676, "unbeacht", "Bold", 33),
    z("bestimmt; Verwechslungsrisiko trägt er wie der Täter", 110, 724, beim("unbeacht", "Das"), "Bold", 33),
    *requisit([("rose", ("tabler", "history", 110, WEISS), "alter Streit", WEISS),
               ("rose2", ("tabler", "calendar", 110, WEISS), "1859", WEISS),
               ("probtr", ("fluent-emoji-flat", "classical-building", 120, None), "Obertribunal", BLAUHELL),
               ("unbeacht", ("tabler", "scale", 120, HELLGRUEN), "unbeachtlich", HELLGRUEN)]),
    *paar("ED", [("rose", "ruhig"), ("rose2", "denkt"), ("unbeacht", "sorge")],
          "VI", [("rose", "ruhig"), ("probtr", "denkt"), ("unbeacht", "ernst")]),
])

# ===========================================================================================================================
# E2 Ansicht 2: Aberratio-Lösung (weite Teile der Lehre)
# ===========================================================================================================================
w30, w30_y = wortlaut(80, 500, 1100, "„Wer einen anderen zu bestimmen versucht, ein Verbrechen zu begehen … wird nach den "
                      "Vorschriften über den Versuch des Verbrechens bestraft.“", "§ 30 Abs. 1 Satz 1 StGB (Auszug)",
                      beim("ab_folge", "versuchte"), size=30)
folie([("aberr", f"{PV} › 2. Aberratio-Lösung (Lehre)"), ("ab_folge", f"{PV} › 2. Folge: § 30 Abs. 1, ggf. § 222")], [
    *tafel("aberr", "2. Aberratio-Lösung (Lehre)"),
    z("Weite Teile der Lehre:", 110, 172, "aberr", "Bold", 34),
    z("Täter wie ein Tatmittel, das sein Ziel verfehlt", 110, 228, beim("aberr", "Für"), size=34),
    blk(110, 290, 1040, 80, LILAHELL, beim("aberr", "eine"), [("aberratio ictus", "ExtraBold", 34, INK)]),
    z("Meist folgt daraus:", 110, 396, "ab_folge", "Bold", 33),
    z("versuchte Anstiftung zum", 414, 396, beim("ab_folge", "versuchte"), "Bold", 33),
    z("Totschlag am Konkurrenten, § 30 Abs. 1 StGB", 110, 444, beim("ab_folge", "Totschlag"), "Bold", 33),
    *w30,
    z("+ ggf. fahrlässige Tötung des Spaziergängers, § 222", 110, w30_y + 24, beim("ab_folge", "gegebenenfalls"), "Bold", 33),
    zit("Darstellung: BGHSt 37, 214, 217; Weber, StudZR 2005, 403 ff.", 110, w30_y + 78, beim("ab_folge", "gegebenenfalls")),
    *requisit([("aberr", ("tabler", "target-off", 110, LILAHELL), "Ziel verfehlt", LILAHELL),
               ("ab_folge", ("tabler", "book", 110, WEISS), "§ 30 Abs. 1, § 222", WEISS)]),
    *paar("ED", [("aberr", "denkt"), ("ab_folge", "staunt")], "VI", [("aberr", "ruhig"), ("ab_folge", "denkt")]),
])
assert w30_y + 120 <= 900, w30_y

# ===========================================================================================================================
# E3a Ansicht 3: BGHSt 37, 214 – Hoferben-Fall (Sachverhalt, Ergebnis)
# ===========================================================================================================================
PH = f"{PV} › 3. BGHSt 37, 214 (Hoferben)"
folie([("bgh", PH), ("hof", f"{PH} › der Fall"), ("lg", f"{PH} › vollendete Anstiftung zum Mord")], [
    *tafel("bgh", "3. BGHSt 37, 214: Hoferben-Fall"),
    zit("BGH, Urt. v. 25.10.1990 – 4 StR 371/90", 110, 172, "bgh"),
    z("Mehr als 130 Jahre später", 110, 222, "bgh", "Bold", 34),
    z("Ein Vater will den Sohn, den Hoferben,", 110, 300, "hof", size=34),
    z("töten lassen und zeigt dem Täter ein Foto.", 110, 350, beim("hof", "töten"), size=34),
    z("Im dunklen Pferdestall tötet der Täter", 110, 420, beim("hof", "Im"), "Bold", 34),
    z("einen Nachbarn, der dem Sohn ähnelt.", 110, 470, beim("hof", "Nachbarn"), "Bold", 34),
    blk(110, 560, 1040, 90, HELLGRUEN, "lg", [("BGH: vollendete Anstiftung zum Mord", "ExtraBold", 34, INK)]),
    *requisit([("bgh", ("tabler", "scale", 120, WEISS), "BGH 1990", WEISS),
               ("hof", ("tabler", "photo", 110, BLAUHELL), "das Foto", BLAUHELL),
               (beim("hof", "Im"), ("ph", "barn", 130, HOLZ), "Pferdestall, dunkel", WEISS),
               ("lg", ("tabler", "scale", 120, HELLGRUEN), "vollendet", HELLGRUEN)]),
    *paar("ED", [("bgh", "ruhig"), ("hof", "denkt"), ("lg", "sorge")], "VI", [("bgh", "ruhig"), ("hof", "ernst"), ("lg", "denkt")]),
])

# ===========================================================================================================================
# E3b BGH: Abweichung im Rahmen des Vorhersehbaren; aberratio-Regeln nicht anwendbar; Individualisierung
# ===========================================================================================================================
folie([("abw", f"{PH} › Abweichung vom Geschehen"), ("lebens", f"{PH} › im Rahmen des Vorhersehbaren: unbeachtlich"),
       ("hand", f"{PH} › aus der Hand gegeben"), ("aberr_nein", f"{PH} › keine aberratio ictus"),
       ("indiv", f"{PV} › vermittelnd: Individualisierung")], [
    *tafel("abw", "Der BGH: Grenze der Vorhersehbarkeit"),
    z("Verwechslung: Abweichung vom geplanten Geschehen", 110, 172, "abw", "Bold", 34),
    blk(110, 236, 1040, 130, BLAUHELL, "lebens", [("Unbeachtlich in den Grenzen des nach", "ExtraBold", 33, INK),
                                               ("allgemeiner Lebenserfahrung Vorhersehbaren", "ExtraBold", 33, INK)]),
    zit("BGHSt 37, 214, 218 f.", 110, 380, beim("lebens", "Grenzen")),
    *okz("Der Vater gab das Geschehen bewusst aus der Hand", 446, "hand", "Bold", 33),
    *neinz("aberratio ictus: Regeln passen nicht", 520, "aberr_nein", "Bold", 33, kreuz=beim("aberr_nein", "nicht")),
    z("entwickelt für Fälle: Täter sieht das Angriffsobjekt", 185, 570, beim("aberr_nein", "Sie"), size=33),
    z("vor sich, trifft aber ein anderes", 185, 618, beim("aberr_nein", "aber", 2), size=33),
    zit("BGHSt 37, 214, 219", 185, 670, beim("aberr_nein", "aber", 2)),
    z("Teil der Lehre: Opfer erkennen dem Täter überlassen?", 110, 740, "indiv", "Bold", 33),
    *requisit([("abw", ("tabler", "route", 110, WEISS), "Abweichung", WEISS),
               ("lebens", ("tabler", "eye", 110, BLAUHELL), "vorhersehbar?", BLAUHELL),
               ("hand", ("tabler", "hand-off", 110, GELB), "aus der Hand", GELB),
               ("aberr_nein", ("tabler", "target-off", 110, HELLROT), "keine aberratio", HELLROT),
               ("indiv", ("tabler", "zoom-question", 110, LILAHELL), "Wer erkennt?", LILAHELL)]),
    *paar("ED", [("abw", "denkt"), ("lebens", "ernst"), ("hand", "sorge"), ("indiv", "denkt")],
          "VI", [("abw", "ruhig"), ("lebens", "denkt"), ("aberr_nein", "ernst"), ("indiv", "ruhig")]),
])

# ===========================================================================================================================
# F1 Ergebnis im Fall (nach dem BGH)
# ===========================================================================================================================
PE = "B. Edeltraud › Ergebnis"
folie([("erg", "B. Edeltraud › Subsumtion"), ("s_hand", "B. Edeltraud › Tat aus der Hand gegeben"),
       ("s_vorh", "B. Edeltraud › Verwechslung vorhersehbar"), ("s_unerw", "B. Edeltraud › unerwünscht – egal"),
       ("s_erg", f"{PE}: §§ 212, 26 (+) nach BGH"), ("s_lehre", f"{PE} › aberratio-Lösung: nur versucht")], [
    *tafel("erg", "Zurück zu Edeltraud"),
    *okz("Tat aus der Hand gegeben: allein, im Dunkeln,", 180, "s_hand", "Bold", 33),
    z("nach einem Foto erkennen", 185, 230, beim("s_hand", "nach"), size=33),
    *okz("Am Kanal gehen abends auch andere spazieren:", 310, "s_vorh", "Bold", 33),
    z("Verwechslung nicht außerhalb der Lebenserfahrung", 185, 360, beim("s_vorh", "Eine"), size=33),
    z("Unerwünscht? Ändert nichts.", 110, 440, "s_unerw", "Bold", 34),
    blk(110, 510, 1040, 90, HELLGRUEN, "s_erg", [("BGH: Anstiftung zum Totschlag, §§ 212, 26 (+)", "ExtraBold", 34, INK)]),
    blk(110, 640, 1040, 90, HELLROT, "s_lehre", [("Aberratio-Lösung: nur versuchte Anstiftung", "ExtraBold", 34, INK)]),
    *requisit([("erg", ("tabler", "photo", 110, BLAUHELL), "der Fall", WEISS),
               ("s_hand", ("tabler", "hand-off", 110, GELB), "aus der Hand", GELB),
               ("s_vorh", ("tabler", "moon", 110, GELB), "dunkler Kanalweg", WEISS),
               ("s_unerw", ("tabler", "thumb-down", 110, LILAHELL), "unerwünscht", LILAHELL),
               ("s_erg", ("tabler", "scale", 120, HELLGRUEN), "§§ 212, 26 (+)", HELLGRUEN),
               ("s_lehre", ("tabler", "target-off", 110, HELLROT), "nur versucht", HELLROT)]),
    *stehend("ED", FX, [("erg", "ruhig"), ("s_hand", "ernst"), ("s_vorh", "sorge"), ("s_unerw", "muede"), ("s_erg", "feierlich"),
                        ("s_lehre", "denkt")]),
])

# ===========================================================================================================================
# F2 Blutbad-Argument (ein Satz) und Antwort des BGH
# ===========================================================================================================================
folie([("blut", "B. Edeltraud › Kritik: Blutbad-Argument"), ("blut2", "B. Edeltraud › BGH: Grenze der Vorhersehbarkeit")], [
    *tafel("blut", "Das Blutbad-Argument"),
    blk(110, 180, 1040, 210, HELLROT, beim("blut", "Tötet"), [("Lehre: Tötet der Täter weiter,", "ExtraBold", 34, INK),
                                                          ("bis er den Richtigen trifft, müsste", "Regular", 34, INK),
                                                          ("der Anstifter für jedes Opfer haften.", "Regular", 34, INK)]),
    zit("Weber, StudZR 2005, 403 ff.", 110, 404, beim("blut", "Tötet")),
    blk(110, 480, 1040, 170, HELLGRUEN, "blut2", [("BGH: Haftung begrenzt durch Vorhersehbarkeit", "ExtraBold", 34, INK),
                                               ("Was außerhalb der Lebenserfahrung liegt,", "Regular", 34, INK),
                                               ("wird nicht zugerechnet.", "Regular", 34, INK)]),
    zit("BGHSt 37, 214, 219", 110, 664, beim("blut2", "Was")),
    *requisit([("blut", ("tabler", "alert-triangle", 110, HELLROT), "Blutbad?", HELLROT),
               ("blut2", ("tabler", "eye", 110, HELLGRUEN), "Vorhersehbarkeit", HELLGRUEN)]),
    *paar("ED", [("blut", "angst"), ("blut2", "ernst")], "VI", [("blut", "sorge"), ("blut2", "muede")]),
])

# ===========================================================================================================================
# G Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Täter vor Teilnehmer"), ("k1", "Klausurtipp › Irrtum je Beteiligten getrennt"),
       ("k2", "Klausurtipp › Streit im Vorsatz des Anstifters")], [
    *tafel("tipp", "Klausurtipp: Täter vor Teilnehmer", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Erst den Täter prüfen, dann den Teilnehmer:", 200, 200, beim("tipp", "Prüfe"), "ExtraBold", 34),
    z("Anstiftung braucht eine vorsätzliche,", 240, 252, beim("tipp", "denn"), size=34),
    z("rechtswidrige Haupttat", 240, 302, beim("tipp", "rechtswidrige"), size=34),
    linienzug([(130, 366), (1130, 366)], "k1", breite=3),
    z("Irrtum für jeden Beteiligten getrennt prüfen", 200, 390, "k1", "ExtraBold", 34),
    z("Beim Täter unbeachtlich, beim Anstifter erst", 240, 442, beim("k1", "Was"), size=34),
    z("das Problem", 240, 492, beim("k1", "erst"), size=34),
    linienzug([(130, 556), (1130, 556)], "k2", breite=3),
    z("Streit im Vorsatz des Anstifters erörtern", 200, 580, "k2", "ExtraBold", 34),
    z("und entscheiden: verschiedene Ergebnisse", 240, 632, beim("k2", "und"), size=34),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# H Klausurschema (Lexi), Punkt für Punkt
# ===========================================================================================================================
folie([("sch", "Klausurschema · Vinzenz und Edeltraud"), ("s1", "Klausurschema › A. Vinzenz, § 212"),
       ("s2", "Klausurschema › B. Edeltraud, §§ 212, 26 › objektiv"), ("s3", "Klausurschema › B. › subjektiv: der Streit"),
       ("s4", "Klausurschema › B. › Rechtswidrigkeit, Schuld")], [
    *tafel("sch", "Klausurschema"),
    z("A. Vinzenz: Totschlag, § 212 StGB", 110, 166, "s1", "ExtraBold", 34),
    *plusminus("1. Objektiver Tatbestand", 150, 220, beim("s1", "Objektiver"), True, size=32),
    *plusminus("2. Vorsatz: error in persona unbeachtlich", 150, 268, beim("s1", "Vorsatz"), True, size=32),
    *plusminus("II. Rechtswidrigkeit, III. Schuld", 150, 316, beim("s1", "Rechtswidrig"), True, size=32),
    z("B. Edeltraud: Anstiftung, §§ 212, 26 StGB", 110, 390, "s2", "ExtraBold", 34),
    *plusminus("1. Objektiv: Haupttat, Bestimmen", 150, 444, beim("s2", "Objektiv"), True, size=32),
    z("2. Subjektiv: Vorsatz bzgl. Haupttat – Streit", 150, 494, "s3", "Bold", 32),
    *plusminus("BGH: Verwechslung vorhersehbar", 196, 542, beim("s3", "Nach"), True, size=32),
    *plusminus("Vorsatz bzgl. Bestimmen", 196, 590, beim("s3", "Dazu"), True, size=32),
    z("II. Rechtswidrigkeit, III. Schuld", 150, 650, "s4", "Bold", 32),
    *redet("LX_erklaert", FX, FB, FR + 40, "sch", "merke"),
    ns("Lexi", FX, FB, "sch", GELB, d=0.2),
])

# ===========================================================================================================================
# I Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Der ", 0), ("error in persona", "a"), (" ist für den Täter", 0)], [("unbeachtlich.", 0)]],
                750, 280, 40, "merke", {"a": beim("merke", "error")}),
    *markertext([[("Für den Anstifter ist er eine Abweichung vom Tatplan,", 0)]], 750, 420, 36, "m2", {}),
    *markertext([[("nach dem BGH unbeachtlich, solange sie nach", 0)],
                 [("allgemeiner Lebenserfahrung ", 0), ("vorhersehbar", "b"), (" war.", 0)]],
                750, 467, 36, beim("m2", "Nach"), {"b": beim("m2", "vorhersehbar")}),
    *markertext([[("Wer die Tat aus der Hand gibt, trägt in der Regel", 0)],
                 [("das ", 0), ("Risiko der Verwechslung", "c"), (".", 0)]],
                750, 650, 36, "m3", {"c": beim("m3", "Risiko")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
