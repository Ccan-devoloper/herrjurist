"""Folge 247 · Lederriemen-Fall: Eventualvorsatz oder bewusste Fahrlässigkeit? – Serienstandard Open Peeps (Katzenkönig).
Echter Fall, vereinfacht und mit anderen Namen (BGH, Urt. v. 22.4.1955 – 5 StR 35/55, BGHSt 7, 363): Willi und Hans planen einen
Raub an einem Bekannten (Versicherungskaufmann); Schlaftabletten scheitern; Willi schlägt den Lederriemen vor, Hans rät wegen der
Todesgefahr zum Sandsack; Willi steckt den Riemen heimlich ein; nachts platzt der Sandsack, beide greifen zum Riemen; Beute;
Wiederbelebung scheitert, das Opfer stirbt. DARSTELLUNG: keine Würgeszene, kein Riemen am Hals, keine Gewalt im Bild – nur
Symbole (Pillen, Riemen und Sandsack auf dem Tisch, Riemen als Icon); das Opfer erscheint nicht als Figur, keine Leiche (leeres Bett,
Kerze). Danach § 15 (Wortlautkarte), BGHSt 7, 363 (Billigen im Rechtssinne; über BGH 5 StR 344/05 Rn. 28, 1 StR 333/22 Rn. 2),
heutige Formel (BGHSt 65, 42 Rn. 22 f.), Hemmschwelle (BGHSt 57, 183 Rn. 42, 45), Subsumtion, Mord (§ 211 Abs. 2 als
Wortlautauszug; BGH 2 StR 391/20 Rn. 27 f.), Gegenansichten (Lehre), Klausurtipp, Schema, Merksatz mit Lexi.
Szenen laut ../SZENENPLAN.md. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/feld/requisit als eigene
Kopie aus Folge 235 (gemeinsame Dateien unverändert); neu: tisch(), fenster().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut StGB nach gesetze-im-internet.de, Abruf 07.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_247/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_247/" in n:
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
NAME = {"HI": "Hildegard", "RU": "Rupert"}
NFARBE = {"HI": LILA, "RU": TUERKIS_}
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



# --- Folge 247: Namen, Farben, Raumbausteine --------------------------------------------------------------------------------
NAME = {"WI": "Willi", "HA": "Hans"}
NFARBE = {"WI": ORANGE, "HA": GRUEN}
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


# ===========================================================================================================================
# A1 Fall: der Plan – Tisch, Schlaftabletten, Lederriemen, Sandsack
# ===========================================================================================================================
WIX, HAX = 560, 1360
TX = 800                                   # Tischkante links
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
WEG = beim("heimlich", "steckt"), beim("heimlich", "ein", ende=True)
folie([(NULL, "Fall · Ein echter Fall, vereinfacht"), ("plan", "Fall · Der Plan: ein Raub"),
       ("pillen", "Fall · Schlaftabletten"), ("riemen", "Fall · Der Lederriemen"),
       ("ha1", "Fall · Lieber ein Sandsack"), ("heimlich", "Fall · Der Riemen für alle Fälle")], [
    boden(NULL),
    *fenster(150, 250, 260, 200, NULL, BLAUHELL),
    *tisch(TX, NULL),
    bis_(hart(pl("Ein echter Fall, vereinfacht und mit anderen Namen", 70, 30, NULL, fill=GELB, size=32)), "plan"),
    bis_(hart(pl("BGH, Urt. v. 22.4.1955 – 5 StR 35/55 (BGHSt 7, 363)", 70, 94, NULL, fill=WEISS, size=28)), "plan"),
    # Willi links (blickt nach rechts zu Hans), Hans rechts (blickt nach links)
    *fig("WI", WIX, BODEN, FH, [(NULL, "ruhig_r"), ("plan", "ernst_r"), ("pillen", "denkt_r"), ("riemen", "ernst_r")],
         bis="wi1", erst="cut"),
    *redet("WI_redet_r", WIX, BODEN, FH, "wi1", "ha1"),
    *fig("WI", WIX, BODEN, FH, [("ha1", "sorge_r"), ("sandsack", "ruhig_r"), ("heimlich", "denkt_r")], erst="cut"),
    hart(ns(NAME["WI"], WIX, BODEN, NULL, NFARBE["WI"])),
    *fig("HA", HAX, BODEN, FH, [(NULL, "ruhig"), ("plan", "ernst"), ("pillen", "denkt"), ("riemen", "sorge")],
         bis="ha1", erst="cut"),
    *redet("HA_redet", HAX, BODEN, FH, "ha1", "sandsack"),
    *fig("HA", HAX, BODEN, FH, [("sandsack", "ruhig"), ("heimlich", "ernst")], erst="cut"),
    hart(ns(NAME["HA"], HAX, BODEN, NULL, NFARBE["HA"])),
    bis_(pl("Willi und Hans wollen einen Bekannten ausrauben.", 70, 30, "plan", fill=GELB, size=32), "pillen"),
    bis_(pl("einen Versicherungskaufmann", 70, 94, beim("plan", "Versicherungskaufmann"), fill=WEISS, size=30), "pillen"),
    bis_(ficon("tabler", "briefcase", 1700, 400, 120, beim("plan", "Versicherungskaufmann"), fuell=BLAUHELL), "pillen"),
    bis_(ficon("tabler", "pills", 870, BODEN - 150, 70, "pillen", fuell=WEISS), "riemen"),
    bis_(pl("Schlaftabletten: vergeblich", 70, 30, "pillen", fill=LILA, size=32), "riemen"),
    bis_(ficon("ph", "belt", 960, BODEN - 152, 130, "riemen", fuell=LEDER), "heimlich"),
    bis_(pl("Willi schlägt einen Lederriemen vor.", 70, 30, "riemen", fill=ORANGE, size=32), "sandsack"),
    blase("sprech", 760, 210, "wi1", 520, 250, inhalt=["Mit dem Riemen würgen wir ihn,", "bis er bewusstlos ist."],
          textsize=32, figur=("WI_redet_r", WIX, BODEN, FH), bis="ha1"),
    blase("sprech", 860, 230, "ha1", 1250, 250, inhalt=["Zu gefährlich. Daran kann er sterben.",
                                                       "Nehmen wir lieber einen Sandsack."], textsize=32,
          figur=("HA_redet", HAX, BODEN, FH), bis="sandsack"),
    ficon("ph", "bag-simple", 1040, BODEN - 152, 90, "sandsack", fuell=SAND),
    bis_(pl("Der Sandsack soll nur betäuben.", 70, 30, "sandsack", fill=GELB, size=32), "heimlich"),
    bewegt(ficon("ph", "belt", 700, BODEN - 300, 110, WEG[0], fuell=LEDER, anim="cut"), WEG[0], WEG[1], 260, 148),
    pl("Willi steckt den Riemen heimlich ein, für alle Fälle.", 70, 30, "heimlich", fill=ORANGE, size=32),
])

# ===========================================================================================================================
# A2 Fall: die Nacht in der Wohnung des Bekannten – nur Symbole (leeres Bett, Sandsack, Riemen, Kerze)
# ===========================================================================================================================
WIX2, HAX2 = 620, 900
AUF = beim("nacht", "übernachten")
tuer_auf = ficon("tabler", "door-enter", 300, BODEN + 4, 230, AUF, fuell=HOLZ, anim="cut")
szene(tuer_auf, "247tuer*", 0.7, 0.0)                # Tür geht auf: die beiden übernachten beim Bekannten
folie([("nacht", "Fall · Die Nacht beim Bekannten"), (beim("nacht", "Gegen"), "Fall · Gegen 4 Uhr morgens"),
       ("platzt", "Fall · Der Sandsack platzt"), ("zieh", "Fall · Doch der Riemen"), ("beute", "Fall · Die Beute"),
       ("tot", "Fall · Der Mann ist tot")], [
    boden("nacht"),
    bis_(hart(ficon("tabler", "door", 300, BODEN + 4, 230, "nacht", fuell=HOLZ, anim="cut")), AUF),
    bis_(tuer_auf, beim("nacht", "Gegen")),
    hart(ficon("tabler", "door", 300, BODEN + 4, 230, beim("nacht", "Gegen"), fuell=HOLZ, anim="cut")),
    *fenster(1330, 200, 300, 220, "nacht", NACHTBLAU),
    hart(ficon("tabler", "moon", 1410, 300, 70, "nacht", fuell=GELB, anim="cut")),
    hart(ficon("ph", "bed", 1560, BODEN + 4, 360, "nacht", fuell=WEISS, anim="cut")),
    *fig("WI", WIX2, BODEN, FH, [("nacht", "ruhig_r"), ("platzt", "angst_r"), ("zieh", "ernst_r"), ("beute", "denkt_r"),
                                 ("tot", "angst_r")], erst="cut"),
    hart(ns(NAME["WI"], WIX2, BODEN, "nacht", NFARBE["WI"])),
    *fig("HA", HAX2, BODEN, FH, [("nacht", "ernst_r"), ("platzt", "angst_r"), ("zieh", "ernst_r"), ("beute", "denkt_r"),
                                 ("tot", "sorge_r")], erst="cut"),
    hart(ns(NAME["HA"], HAX2, BODEN, "nacht", NFARBE["HA"])),
    bis_(pl("Die beiden übernachten bei ihrem Bekannten.", 70, 30, "nacht", fill=BLAUHELL, size=32), beim("nacht", "Gegen")),
    bis_(pl("Gegen 4 Uhr morgens schlägt Hans mit dem Sandsack zu.", 70, 30, beim("nacht", "Gegen"), fill=GELB, size=32),
         "platzt"),
    bis_(ficon("tabler", "clock", 1130, 250, 90, beim("nacht", "Gegen"), fuell=WEISS), "platzt"),
    bis_(ficon("ph", "bag-simple", 1130, 420, 110, beim("nacht", "Sandsack"), fuell=SAND), "platzt"),
    bis_(ficon("tabler", "boom", 1130, 420, 130, "platzt", fuell=SAND), "zieh"),
    bis_(pl("Der Sandsack platzt. Es kommt zum Handgemenge.", 70, 30, "platzt", fill=ROT, size=32), "zieh"),
    bis_(ficon("ph", "belt", 1130, 400, 160, "zieh", fuell=LEDER), "beute"),
    bis_(pl("Beide greifen doch zum Riemen.", 70, 30, "zieh", fill=ORANGE, size=32), "beute"),
    bis_(pl("… bis er sich nicht mehr rührt.", 70, 94, beim("zieh", "bis"), fill=WEISS, size=30), "beute"),
    bis_(ficon("tabler", "hanger", 1130, 380, 140, "beute", fuell=WEISS), "tot"),
    bis_(pl("Sie suchen sich Kleidung aus seiner Wohnung aus.", 70, 30, "beute", fill=LILA, size=32), "tot"),
    ficon("tabler", "activity-heartbeat", 1130, 380, 140, "tot", fuell=None),
    pl("Die Wiederbelebung scheitert.", 70, 30, "tot", fill=HELLGRAU, size=32),
    pl("Der Mann ist tot.", 70, 94, beim("tot", "Der"), fill=WEISS, size=30),
    ficon("tabler", "candle", 1820, BODEN + 4, 72, beim("tot", "Der"), fuell=GELB),
])

# ===========================================================================================================================
# A3 Die Frage
# ===========================================================================================================================
folie([("frage", "Die Frage · Den Tod wollten sie nicht"), ("frage2", "Die Frage · Vorsatz oder Fahrlässigkeit?")], [
    *tafel("frage", "Die Frage"),
    z("Den Tod wollten die beiden gerade nicht.", 110, 200, "frage", "Bold", 38),
    blk(110, 300, 1040, 90, GELB, "frage2", [("Haben sie trotzdem vorsätzlich getötet?", "ExtraBold", 38, INK)]),
    blk(110, 430, 1040, 90, LILAHELL, beim("frage2", "oder"), [("Oder nur fahrlässig?", "ExtraBold", 38, INK)]),
    *requisit([("frage", ("ph", "belt", 130, LEDER), "kein Todeswunsch", WEISS),
               ("frage2", ("tabler", "scale", 120, GELB), "Vorsatz oder Fahrlässigkeit?", GELB)]),
    *paar("WI", [("frage", "sorge"), ("frage2", "muede")], "HA", [("frage", "angst"), ("frage2", "sorge")]),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_247(cue, absaetze, quelle, frage):
    els = [karte(140, 40, 1640, 950, cue, fill=HELL), titel("Sachverhalt", 210, 70, cue, 56)]
    y = 160
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=34, zeilenabstand=1.28)
        els += e; y += 10
    els.append(z(quelle, 210, y, cue, size=28, farbe=TEXT, rechts=1740)); y += 48
    assert y + 70 <= 985, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 4, cue, fill=PINK, size=34))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_247("sv", [
    "Willi und Hans wollen einen Bekannten, einen Versicherungskaufmann, ausrauben. Ein Versuch mit Schlaftabletten "
    "scheitert. Willi schlägt vor, den Mann mit einem Lederriemen bis zur Bewusstlosigkeit zu würgen. Hans rät ab: "
    "„Zu gefährlich. Daran kann er sterben.“ Sie einigen sich auf einen Sandsack, der den Mann nur betäuben soll. "
    "Willi steckt den Riemen heimlich für alle Fälle ein.",
    "Die beiden übernachten bei ihrem Bekannten. Gegen 4 Uhr morgens schlägt Hans mit dem Sandsack zu. Der Sandsack "
    "platzt, es kommt zum Handgemenge. Beide drosseln den Mann mit dem Riemen, bis er sich nicht mehr rührt, und suchen "
    "sich Kleidung aus seiner Wohnung aus. Ihre Wiederbelebungsversuche scheitern; der Mann ist tot.",
], "Nach BGH, Urt. v. 22.4.1955 – 5 StR 35/55 (BGHSt 7, 363), vereinfacht; Namen geändert.",
   "Haben Willi und Hans vorsätzlich getötet?")

# ===========================================================================================================================
# C § 15 StGB (Wortlautkarte): Vorsatz oder Fahrlässigkeit
# ===========================================================================================================================
w15, w15_y = wortlaut(80, 170, 1100, "„Strafbar ist nur vorsätzliches Handeln, wenn nicht das Gesetz fahrlässiges Handeln "
                      "ausdrücklich mit Strafe bedroht.“", "§ 15 StGB", "p15",
                      marken=[("vorsätzliches", beim("p15", "vorsätzliches")), ("fahrlässiges", beim("p15", "fahrlässiges"))],
                      size=34)
folie([("p15", "§ 15 StGB · Wortlaut"), ("folge", "§ 15 StGB › Mit Vorsatz: §§ 212, 211"),
       ("p222", "§ 15 StGB › Ohne Vorsatz: §§ 222, 251"), ("problem", "Problem: das Wollen"),
       ("f29", "Problem: Eventualvorsatz oder bewusste Fahrlässigkeit?")], [
    *tafel("p15", "Die Weiche: § 15 StGB"),
    *w15,
    blk(110, w15_y + 24, 505, 120, HELLGRUEN, "folge", [("Mit Vorsatz:", "ExtraBold", 30, INK),
                                                      ("§ 212 Totschlag, ggf. § 211", "Regular", 30, INK)]),
    blk(645, w15_y + 24, 505, 120, HELLROT, "p222", [("Ohne Vorsatz:", "ExtraBold", 30, INK),
                                                   ("§ 222, § 251 (Todesfolge)", "Regular", 30, INK)]),
    *okz("Wissen: Würgen kann tödlich sein", w15_y + 180, "problem", "Bold", 34),
    z("Fraglich ist das Wollen:", 110, w15_y + 244, beim("problem", "Fraglich"), "Bold", 34),
    blk(110, w15_y + 300, 1040, 90, GELB, beim("problem", "Eventualvorsatz"),
        [("Eventualvorsatz oder bewusste Fahrlässigkeit?", "ExtraBold", 34, INK)]),
    zit("Die drei Vorsatzformen: Folge 029", 110, w15_y + 410, "f29"),
    *requisit([("p15", ("tabler", "book", 110, WEISS), "§ 15 StGB", WEISS),
               ("folge", ("tabler", "scale", 120, HELLGRUEN), "mit Vorsatz", HELLGRUEN),
               ("p222", ("tabler", "scale", 120, HELLROT), "ohne Vorsatz", HELLROT),
               ("problem", ("tabler", "help", 110, GELB), "Das Wollen?", GELB)]),
    *paar("WI", [("p15", "ruhig"), ("folge", "sorge"), ("problem", "denkt")],
          "HA", [("p15", "ruhig"), ("p222", "denkt"), ("problem", "ernst")]),
])
assert w15_y + 450 <= 900, w15_y

# ===========================================================================================================================
# D BGHSt 7, 363: Billigen im Rechtssinne
# ===========================================================================================================================
PL = "BGHSt 7, 363 · Lederriemen"
folie([("bgh", PL), ("unerw", f"{PL} › Tod höchst unerwünscht"), ("recht", f"{PL} › Billigen im Rechtssinne"),
       ("notfalls", f"{PL} › notfalls abfinden"), ("heute", f"{PL} › bis heute")], [
    *tafel("bgh", "Der Lederriemen-Fall, BGH 1955"),
    zit("BGH, Urt. v. 22.4.1955 – 5 StR 35/55, BGHSt 7, 363", 110, 172, "bgh"),
    z("Vieles spricht dafür: Der Tod war beiden", 110, 230, "unerw", "Bold", 35),
    z("„höchst unerwünscht“.", 110, 280, beim("unerw", "höchst"), "Bold", 35),
    blk(110, 350, 1040, 130, BLAUHELL, "recht", [("Billigen im Rechtssinne:", "ExtraBold", 34, INK),
                                              ("Erfolg muss nicht den Wünschen entsprechen", "Regular", 33, INK)]),
    z("Es genügt: Der Täter findet sich um seines Zieles", 110, 510, "notfalls", "Bold", 33),
    z("willen notfalls mit dem unerwünschten Erfolg ab.", 110, 558, beim("notfalls", "notfalls"), "Bold", 33),
    zit("BGHSt 7, 363, 369; so zitiert in BGH, Urt. v. 30.11.2005 – 5 StR 344/05, Rn. 28", 110, 614,
        beim("notfalls", "notfalls")),
    blk(110, 690, 1040, 130, HELLGRUEN, "heute", [("Bis heute: „Billigen im Rechtssinne“", "ExtraBold", 33, INK),
                                               ("BGH, Beschl. v. 10.1.2023 – 1 StR 333/22, Rn. 2", "Regular", 30, INK)]),
    *requisit([("bgh", ("tabler", "scale", 120, WEISS), "BGH 1955", WEISS),
               ("unerw", ("tabler", "thumb-down", 110, LILAHELL), "unerwünscht", LILAHELL),
               ("recht", ("tabler", "scale", 120, BLAUHELL), "im Rechtssinne", BLAUHELL),
               ("notfalls", ("ph", "belt", 130, LEDER), "notfalls hingenommen", WEISS),
               ("heute", ("tabler", "calendar", 110, HELLGRUEN), "bis heute", HELLGRUEN)]),
    *paar("WI", [("bgh", "ruhig"), ("unerw", "sorge"), ("notfalls", "muede")],
          "HA", [("bgh", "ruhig"), ("unerw", "angst"), ("recht", "denkt"), ("heute", "ernst")]),
])

# ===========================================================================================================================
# E1 Heutige Formel: Wissens- und Willenselement, bewusste Fahrlässigkeit
# ===========================================================================================================================
PE = "Eventualvorsatz heute"
folie([("formel", PE), ("wissen", f"{PE} › 1. Wissenselement"), ("wollen", f"{PE} › 2. Willenselement"),
       ("bf", "Abgrenzung › bewusste Fahrlässigkeit")], [
    *tafel("formel", "Eventualvorsatz heute"),
    z("1. Wissenselement: Tod als mögliche, nicht", 110, 180, "wissen", "Bold", 35),
    z("ganz fernliegende Folge erkannt", 150, 230, beim("wissen", "mögliche"), size=34),
    z("2. Willenselement: billigt ihn oder findet sich", 110, 310, "wollen", "Bold", 35),
    z("um seines Zieles willen mit ihm ab,", 150, 360, beim("wollen", "findet"), size=34),
    z("mag er ihm auch unerwünscht sein", 150, 408, beim("wollen", "mag"), size=34),
    zit("BGH, Urt. v. 18.6.2020 – 4 StR 482/19, BGHSt 65, 42, Rn. 22", 110, 466, beim("wollen", "mag")),
    blk(110, 540, 1040, 170, HELLROT, "bf", [("Bewusste Fahrlässigkeit:", "ExtraBold", 34, INK),
                                          ("ernsthaft und nicht nur vage darauf vertraut,", "Regular", 33, INK),
                                          ("der Tod werde nicht eintreten", "Regular", 33, INK)]),
    zit("ebd., Rn. 22", 110, 724, beim("bf", "ernsthaft")),
    *requisit([("formel", ("tabler", "list-check", 110, WEISS), "zwei Elemente", WEISS),
               ("wissen", ("tabler", "bulb", 110, GELB), "Wissen", GELB),
               ("wollen", ("tabler", "target", 110, BLAUHELL), "Wollen", BLAUHELL),
               ("bf", ("tabler", "shield-check", 110, HELLROT), "Vertrauen", HELLROT)]),
    *paar("WI", [("formel", "ruhig"), ("wissen", "denkt"), ("bf", "muede")],
          "HA", [("formel", "ruhig"), ("wollen", "denkt"), ("bf", "sorge")]),
])

# ===========================================================================================================================
# E2 Gesamtschau und Hemmschwelle
# ===========================================================================================================================
folie([("gesamt", "Abgrenzung › Gesamtschau aller Umstände"), ("hemm", "Abgrenzung › Tötungsdelikte: Hemmschwelle?")], [
    *tafel("gesamt", "Wie wird entschieden?"),
    z("Gesamtschau aller Umstände", 110, 190, "gesamt", "ExtraBold", 36),
    z("Gefährlichkeit der Handlung:", 110, 260, beim("gesamt", "Gefährlichkeit"), "Bold", 35),
    z("ein wesentlicher Indikator", 150, 310, beim("gesamt", "wesentlicher"), size=34),
    zit("BGHSt 65, 42, Rn. 23", 110, 366, beim("gesamt", "wesentlicher")),
    blk(110, 440, 1040, 130, HELLGRAU, "hemm", [("Tötungsdelikte: Das Schlagwort „Hemmschwelle“", "ExtraBold", 33, INK),
                                             ("ersetzt keine Begründung", "Regular", 33, INK)]),
    z("Es verlangt nur eine sorgfältige Gesamtwürdigung.", 110, 600, beim("hemm", "Es"), "Bold", 33),
    zit("BGH, Urt. v. 22.3.2012 – 4 StR 558/11, BGHSt 57, 183, Rn. 42, 45", 110, 656, beim("hemm", "Es")),
    *requisit([("gesamt", ("tabler", "eye", 110, BLAUHELL), "Gesamtschau", BLAUHELL),
               ("hemm", ("tabler", "alert-triangle", 110, HELLGRAU), "Hemmschwelle?", WEISS)]),
    *paar("WI", [("gesamt", "denkt"), ("hemm", "ernst")], "HA", [("gesamt", "ruhig"), ("hemm", "muede")]),
])

# ===========================================================================================================================
# F Subsumtion
# ===========================================================================================================================
PS_ = "A. Willi und Hans, §§ 212, 211 StGB › Vorsatz"
folie([("sub", PS_), ("s_wissen", f"{PS_} › Wissenselement (+)"), ("s_vertr", f"{PS_} › ernsthaftes Vertrauen?"),
       ("s_ziel", f"{PS_} › Willenselement (+)"), ("s_unerw", f"{PS_} › unerwünscht – egal"),
       ("s_ev", f"{PS_} › Eventualvorsatz (+)")], [
    *tafel("sub", "Zurück zum Fall"),
    z("Beide sahen die Todesgefahr: Riemen zuerst verworfen", 110, 180, "s_wissen", "Bold", 33),
    *okz("Wissenselement", 232, beim("s_wissen", "Wissenselement"), "ExtraBold", 33),
    z("Vertrauen? Sandsack versagt, trotzdem Riemen,", 110, 310, "s_vertr", "Bold", 33),
    z("mit aller Kraft: nur noch vages Hoffen", 150, 358, beim("s_vertr", "Auf"), size=33),
    *okz("Willenselement: Tod um der Beute willen", 430, "s_ziel", "ExtraBold", 33),
    z("notfalls hingenommen", 185, 478, beim("s_ziel", "notfalls"), size=33),
    z("Höchst unerwünscht (Wiederbelebungsversuche):", 110, 556, "s_unerw", "Bold", 33),
    z("ändert am Billigen im Rechtssinne nichts", 150, 604, beim("s_unerw", "Am"), size=33),
    blk(110, 680, 1040, 90, HELLGRUEN, "s_ev", [("Beide: Eventualvorsatz (+)", "ExtraBold", 36, INK)]),
    *requisit([("sub", ("ph", "belt", 130, LEDER), "der Fall", WEISS),
               ("s_wissen", ("tabler", "bulb", 110, GELB), "Gefahr erkannt", GELB),
               ("s_vertr", ("tabler", "boom", 120, SAND), "Sandsack versagt", WEISS),
               ("s_ziel", ("tabler", "hanger", 120, WEISS), "Beute", WEISS),
               ("s_unerw", ("tabler", "activity-heartbeat", 120, None), "Wiederbelebung", LILAHELL),
               ("s_ev", ("tabler", "scale", 120, HELLGRUEN), "Eventualvorsatz", HELLGRUEN)]),
    *paar("WI", [("sub", "ruhig"), ("s_wissen", "sorge"), ("s_vertr", "ernst"), ("s_unerw", "angst"), ("s_ev", "muede")],
          "HA", [("sub", "ruhig"), ("s_wissen", "denkt"), ("s_ziel", "ernst"), ("s_unerw", "sorge"), ("s_ev", "muede")]),
])

# ===========================================================================================================================
# G Ergebnis: Totschlag, Mord (§ 211 Abs. 2 als Wortlautauszug)
# ===========================================================================================================================
w211, w211_y = wortlaut(80, 230, 1100, "„Mörder ist, wer … aus Habgier … oder um eine andere Straftat zu ermöglichen … "
                        "einen Menschen tötet.“", "§ 211 Abs. 2 StGB (Auszug)", "mord",
                        marken=[("Habgier", beim("mord", "Habgier")), ("ermöglichen", beim("mord", "ermöglichen"))], size=34)
folie([("erg", "A. Willi und Hans › Ergebnis: § 212 (+)"), ("mord", "A. Willi und Hans › Mord, § 211?"),
       ("mord2", "A. Willi und Hans › Ermöglichungsabsicht trotz Eventualvorsatz"),
       ("urteil", "A. Willi und Hans › Im echten Fall: Mord")], [
    *tafel("erg", "Ergebnis"),
    *plusminus("Totschlag, § 212 StGB", 110, 160, "erg", True, size=36, stil="ExtraBold"),
    *w211,
    z("Ermöglichungsabsicht verträgt sich auch", 110, w211_y + 30, "mord2", "Bold", 34),
    z("mit bedingtem Tötungsvorsatz.", 110, w211_y + 80, beim("mord2", "mit"), "Bold", 34),
    zit("BGH, Beschl. v. 16.2.2021 – 2 StR 391/20, Rn. 27 f.; BGHSt 39, 159", 110, w211_y + 134, beim("mord2", "mit")),
    blk(110, w211_y + 200, 1040, 130, HELLGRUEN, "urteil", [("Echter Fall: Verurteilung wegen Mordes,", "ExtraBold", 33, INK),
                                                         ("vom BGH bestätigt", "Regular", 33, INK)]),
    *requisit([("erg", ("tabler", "scale", 120, HELLGRUEN), "§ 212 (+)", HELLGRUEN),
               ("mord", ("tabler", "book", 110, WEISS), "§ 211 StGB", WEISS),
               ("mord2", ("tabler", "hanger", 120, WEISS), "um auszurauben", WEISS),
               ("urteil", ("tabler", "scale", 120, HELLGRUEN), "Mord", HELLGRUEN)]),
    *paar("WI", [("erg", "ernst"), ("mord", "sorge"), ("urteil", "muede")],
          "HA", [("erg", "ernst"), ("mord2", "sorge"), ("urteil", "muede")]),
])
assert w211_y + 340 <= 900, w211_y

# ===========================================================================================================================
# H Gegenansichten (Lehre)
# ===========================================================================================================================
PG = "Gegenansichten (Lehre)"
folie([("lehre", PG), ("moegl", f"{PG} › Möglichkeitstheorie"), ("wahr", f"{PG} › Wahrscheinlichkeitstheorie"),
       ("kritik", f"{PG} › Kritik")], [
    *tafel("lehre", "Gegenansichten (Lehre)"),
    z("Ansichten, die auf das Wollen verzichten:", 110, 180, "lehre", "Bold", 35),
    z("1. Möglichkeitstheorie: konkrete Möglichkeit", 110, 260, "moegl", "Bold", 34),
    z("erkannt und trotzdem gehandelt", 150, 308, beim("moegl", "erkennt"), size=34),
    z("2. Wahrscheinlichkeitstheorie: Erfolg für", 110, 390, "wahr", "Bold", 34),
    z("wahrscheinlich gehalten", 150, 438, beim("wahr", "wahrscheinlich"), size=34),
    blk(110, 520, 1040, 170, HELLROT, "kritik", [("Dagegen: Beim Wissen gleichen sich", "ExtraBold", 33, INK),
                                              ("Eventualvorsatz und bewusste Fahrlässigkeit.", "Regular", 33, INK),
                                              ("Den Unterschied macht erst das Wollen.", "Regular", 33, INK)]),
    zit("Lehre: Uni Freiburg (Hefendehl), Vorlesung Strafrecht AT, § 10 KK 200 f.", 110, 706, "moegl"),
    *requisit([("lehre", ("tabler", "book", 110, LILAHELL), "Lehre", LILAHELL),
               ("moegl", ("tabler", "bulb", 110, GELB), "nur Wissen", GELB),
               ("wahr", ("tabler", "dice-5", 110, WEISS), "wahrscheinlich?", WEISS),
               ("kritik", ("tabler", "target", 110, HELLROT), "Wollen entscheidet", HELLROT)]),
    *paar("WI", [("lehre", "ruhig"), ("moegl", "denkt"), ("kritik", "ernst")],
          "HA", [("lehre", "ruhig"), ("wahr", "denkt"), ("kritik", "ernst")]),
])

# ===========================================================================================================================
# I Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Wissen und Wollen trennen"), ("k1", "Klausurtipp › unerwünscht und doch gebilligt"),
       ("k2", "Klausurtipp › Gründe für ein Vertrauen suchen")], [
    *tafel("tipp", "Klausurtipp: Wissen und Wollen", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Im subjektiven Tatbestand Wissens- und", 200, 200, beim("tipp", "subjektiven"), "ExtraBold", 35),
    z("Willenselement sauber trennen", 240, 252, beim("tipp", "Wissens"), size=34),
    linienzug([(130, 320), (1130, 320)], "k1", breite=3),
    z("Unerwünschter Erfolg? Nicht täuschen lassen:", 200, 344, "k1", "ExtraBold", 34),
    z("Auch ihn kann der Täter im Rechtssinne billigen", 240, 396, beim("k1", "Auch"), size=34),
    linienzug([(130, 464), (1130, 464)], "k2", breite=3),
    z("Echte Gründe für ein Vertrauen suchen,", 200, 488, "k2", "ExtraBold", 34),
    z("etwa Vorsichtsmaßnahmen", 240, 540, beim("k2", "etwa"), size=34),
    z("Vages Hoffen genügt nicht.", 240, 592, beim("k2", "Vages"), "Bold", 34),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# J Klausurschema (Lexi), Punkt für Punkt
# ===========================================================================================================================
folie([("sch", "Klausurschema · Willi und Hans"), ("s1", "Klausurschema › §§ 212, 211 › 1. Objektiver Tatbestand"),
       ("s2", "Klausurschema › 2. Vorsatz: Eventualvorsatz"), ("s3", "Klausurschema › 3. Mordmerkmale"),
       ("s4", "Klausurschema › Rechtswidrigkeit, Schuld")], [
    *tafel("sch", "Klausurschema: Willi und Hans"),
    z("§§ 212, 211 StGB", 110, 170, "s1", "ExtraBold", 36),
    *plusminus("1. Objektiver Tatbestand: Tod, ursächlich", 150, 240, beim("s1", "Erstens"), True, size=34, stil="Bold"),
    z("2. Vorsatz:", 150, 310, "s2", "Bold", 34),
    *plusminus("Wissenselement", 196, 364, beim("s2", "Wissenselement"), True, size=34),
    *plusminus("Willenselement", 196, 418, beim("s2", "Willenselement"), True, size=34),
    blk(196, 476, 954, 80, HELLGRUEN, beim("s2", "also"), [("Eventualvorsatz", "ExtraBold", 34, INK)]),
    z("3. Mordmerkmale: Habgier, Ermöglichungsabsicht", 150, 590, "s3", "Bold", 34),
    z("II. Rechtswidrigkeit, III. Schuld", 110, 670, "s4", "ExtraBold", 34),
    *redet("LX_erklaert", FX, FB, FR + 40, "sch", "merke"),
    ns("Lexi", FX, FB, "sch", GELB, d=0.2),
])

# ===========================================================================================================================
# K Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Billigen", "a"), (" heißt nicht wünschen.", 0)]], 750, 290, 42, "merke", {"a": beim("merke", "Billigen")}),
    *markertext([[("Wer den Tod als möglich erkennt und ihn", 0)],
                 [("um seines Zieles willen notfalls hinnimmt,", 0)],
                 [("handelt mit ", 0), ("Eventualvorsatz", "b"), (".", 0)]],
                750, 400, 40, "m2", {"b": beim("m2", "Eventualvorsatz")}),
    *markertext([[("Bewusst fahrlässig handelt nur, wer", 0)],
                 [("ernsthaft auf das Ausbleiben ", 0), ("vertraut", "c"), (".", 0)]],
                750, 640, 40, "m3", {"c": beim("m3", "vertraut")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
