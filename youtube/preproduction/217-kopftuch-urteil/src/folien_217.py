"""Folge 217 · Kopftuch-Urteil: Darf eine Lehrerin mit Kopftuch unterrichten? – Serienstandard Open Peeps (Katzenkönig).
Fiktiver Fall nach dem Muster von Kopftuch II: Frau Sander unterrichtet Mathematik in der 8b; das Land verbietet religiöse
Zeichen pauschal an allen Schulen (Ausnahme: christlich-abendländische Bildungs- und Kulturwerte). Danach Art. 4 Abs. 1, 2 GG
(Wortlautkarte), Schutzbereich und Eingriff, Schranken (Art. 6 Abs. 2, Art. 7 Abs. 1 GG als Wortlautkarten), der Vater
Herr Röder, Kopftuch I (BVerfGE 108, 282), Kopftuch II (BVerfGE 138, 296) samt Art. 33 Abs. 3 GG (Wortlautkarte), Ergebnis
im Fall, Rechtsreferendarin (BVerfGE 153, 1), § 34 Abs. 2 S. 4 BeamtStG (Wortlautkarte), Klausurtipp und Merksatz mit Lexi.
DARSTELLUNG: Frau Sander sympathisch und kompetent (Open-Peeps-Kopf „Hijab“, unverändert); Schulleitung, Land und Vater
neutral bzw. mit legitimem Anliegen; keine religiösen Symbole im Bild; reale Beschwerdeführerinnen weder gezeigt noch
benannt (Rechtsreferendarin und Richterin als Funktionsrollen).
Szenen laut ../SZENENPLAN.md. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/feld/requisit/
stehend/paar/raum/tisch/richtertisch als eigene Kopie aus Folge 211 (gemeinsame Dateien unverändert; stehend() um Kinder
ohne Namensschild ergänzt); neu: schultafel(), kreide(), pulte(), kinder().
Handlungsgeräusche: Kreide an der Tafel (Freesound CC0 210319), Pausengong (Freesound CC0 213794); ../geraeusche_herkunft.json.
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut GG/BeamtStG nach gesetze-im-internet.de, Abruf 06.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_217/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_217/" in n:
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
NAME = {"SA": "Frau Sander", "ST": "Herr Steffens", "RD": "Herr Röder", "RF": "Rechtsreferendarin", "RI": "Vorsitzende Richterin"}
NFARBE = {"SA": LILA, "ST": BLAU, "RD": TUERKIS_, "RF": GRUEN, "RI": GELB}
KIND = {"K1", "K2", "K3"}              # Kinder der 8b: ohne Namen, kleiner skaliert
KF = 0.68                              # Kinderhöhe relativ zur Erwachsenenhöhe
FASSADE = (246, 232, 210, 255)


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
    if k in KIND:                                   # Kinder: kleiner, ohne Namensschild (nie benannt)
        return rechts_frei(fig(k, x, FB, round(FR * KF), folge, bis=bis), 1200)
    els = [*fig(k, x, FB, FR, folge, bis=bis), bis_(ns(NAME[k], x, FB, folge[0][0], NFARBE[k], d=0.1), bis)]
    return rechts_frei(els, 1200)


def paar(a, af, b, bf):
    """Tafelszene: zwei Figuren rechts der Tafel (beide blicken nach links zur Tafel)."""
    return [*stehend(a, X1, af), *stehend(b, X2, bf)]


# --- eigene Szenenbausteine (programmatisch, Palettenflächen, Tuschekontur) ---------------------------------------------------
WAND = (246, 236, 220, 255)


def raum(cue, fenster_x=None, tuer_x=None):
    """Innenraum: Bodenlinie, Fenster (hellblau) und Tür (Holz) als Grundformen."""
    els = [boden(cue)]
    if fenster_x is not None:
        els.append(feld(fenster_x, 250, 300, 220, cue, fill=BLAUHELL, rand=5, rund=6, name="fenster"))
        els.append(hart(linienzug([(fenster_x + 150, 250), (fenster_x + 150, 470)], cue, breite=5)))
    if tuer_x is not None:
        els.append(feld(tuer_x, BODEN - 300, 150, 300, cue, fill=HOLZ, rand=5, rund=4, name="tuer"))
    return els


def tisch(x0, x1, cue, oben=690, bis=None):
    """Tisch (Holz) vor den Figuren: Platte und zwei Beine."""
    return [feld(x0, oben, x1 - x0, 34, cue, fill=HOLZ, rand=5, rund=6, bis=bis, name="tischplatte"),
            feld(x0 + 30, oben + 34, 26, BODEN - oben - 34, cue, fill=HOLZ, rand=4, rund=3, bis=bis, name="tischbein"),
            feld(x1 - 56, oben + 34, 26, BODEN - oben - 34, cue, fill=HOLZ, rand=4, rund=3, bis=bis, name="tischbein2")]


def richtertisch(x0, x1, cue):
    """Richtertisch als geschlossene Holzfront vor der Richterin, Hammer-Icon, Pille „Gericht“."""
    return [feld(x0, 715, x1 - x0, BODEN - 715, cue, fill=HOLZ, rand=5, rund=8, name="richtertisch"),
            hart(ficon("tabler", "gavel", x0 + 70, 712, 80, cue, fuell=WEISS)),
            hart(pl("Gericht", (x0 + x1) / 2, 770, cue, fill=WEISS, size=30, anker="m"))]



# --- eigene Szenenbausteine Folge 217 ---------------------------------------------------------------------------------------
TAFELGRUEN = (58, 98, 78, 255)
KREIDE = (244, 244, 236, 255)
KH = round(FH * KF)                          # Kinder in der Fallszene


def schultafel(x, y, w, h, cue):
    """Schultafel (Tafelgrün) mit Holzrahmen und Ablage, programmatisch."""
    return [feld(x - 14, y - 14, w + 28, h + 28, cue, fill=HOLZ, rand=5, rund=8, name="tafelrahmen"),
            feld(x, y, w, h, cue, fill=TAFELGRUEN, rand=4, rund=4, name="schultafel"),
            feld(x + 40, y + h + 14, w - 80, 16, cue, fill=HOLZ, rand=4, rund=3, name="tafelablage")]


def kreide(text, x, y, cue, size=54, **k):
    """Kreideschrift auf der Schultafel (Ziffern, Formel)."""
    return zeile(glyphen(text), x, y, cue, "Bold", size, farbe=KREIDE, **k)


def pulte(x0, x1, cue, oben=700, bis=None):
    """Durchgehende Pultfront vor den Kindern (Holz), verdeckt die Beine bewusst."""
    return [feld(x0, oben, x1 - x0, BODEN - oben, cue, fill=HOLZ, rand=5, rund=8, bis=bis, name="pulte")]


def kinder(xs, folgen, unten=BODEN, hoehe=KH, erst="cut"):
    els = []
    for k, x, folge in zip(("K1", "K2", "K3"), xs, folgen):
        els += fig(k, x, unten, hoehe, folge, erst=erst)
    return els


def fall_ns(k, x, cue, **kw):
    return ns(NAME[k], x, BODEN, cue, NFARBE[k], **kw)


NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig

# ===========================================================================================================================
# A1 Fall: Klassenzimmer, Mathestunde (fiktiv)
# ===========================================================================================================================
SAX1 = 960
KX1 = (1340, 1540, 1740)
folie([(NULL, "Fall · Gymnasium, Montag, 1. Stunde"), ("mathe", "Fall · Mathematik in der 8b"),
       ("tuch", "Fall · Das Kopftuch"), ("nie", "Fall · Nie Streit")], [
    boden(NULL),
    *schultafel(120, 300, 640, 300, NULL),
    hart(pl("Gymnasium · Montag, 1. Stunde", 70, 40, NULL, fill=ORANGE, size=32)),
    szene(kreide("a² + b² = c²", 200, 360, beim("mathe", "Mathematik")), "217kreide*", 0.9, 0.05),
    kreide("Klasse 8b", 200, 470, beim("mathe", "acht"), size=44),
    pl("Mathematik · Klasse 8b · 27 Kinder", 70, 104, beim("mathe", "Mathematik"), fill=BLAUHELL, size=30),
    *fig("SA", SAX1, BODEN, FH, [(NULL, "ruhig_r"), ("tuch", "froh_r"), ("nie", "strahlt_r")], erst="cut"),
    hart(fall_ns("SA", SAX1, NULL)),
    *kinder(KX1, [[(NULL, "ruhig"), ("mathe", "froh")], [(NULL, "froh"), ("nie", "ruhig")],
                  [(NULL, "ruhig"), ("tuch", "froh")]]),
    *pulte(1220, 1860, NULL),
    hart(pl("Klasse 8b", 1540, 760, NULL, fill=WEISS, size=28, anker="m")),
    pl("Kopftuch: für sie ein Gebot ihres Glaubens", 70, 168, "tuch", fill=LILAHELL, size=30),
    pl("Streit darüber gab es nie.", 70, 232, "nie", fill=HELLGRUEN, size=30),
])

# ===========================================================================================================================
# A2 Fall: Büro der Schulleitung – das neue Schulgesetz (fiktiv, Muster § 57 Abs. 4 SchulG NW a. F.)
# ===========================================================================================================================
STX2, SAX2 = 620, 1300
folie([("pause", "Fall · In der Pause"), ("neu", "Fall · Das neue Schulgesetz"), ("st1", "Fall · Das Verbot"),
       ("sa1", "Fall · Frau Sander"), ("ausn", "Fall · Die Ausnahme")], [
    *raum("pause", fenster_x=1520),
    szene(hart(ficon("tabler", "bell-ringing", 1670, 220, 90, "pause", fuell=GELB)), "217gong*", 0.8, 0.0),
    pl("Pause · Büro der Schulleitung", 70, 40, "pause", fill=ORANGE, size=32),
    pl("Neues Schulgesetz des Landes", 960, 520, "neu", fill=WEISS, size=30, anker="m"),
    ficon("tabler", "file-text", 960, 686, 90, "neu", fuell=WEISS),
    *tisch(820, 1100, "pause"),
    *fig("ST", STX2, BODEN, FH, [("pause", "ruhig_r"), ("neu", "ernst_r")], bis="st1", erst="cut"),
    *redet("ST_redet_r", STX2, BODEN, FH, "st1", "sa1"),
    *fig("ST", STX2, BODEN, FH, [("sa1", "bedauert_r"), ("ausn", "ernst_r")], erst="cut"),
    hart(fall_ns("ST", STX2, "pause")),
    *fig("SA", SAX2, BODEN, FH, [("pause", "ruhig"), (beim("st1", "Ab"), "betroffen")], bis="sa1", erst="cut"),
    *redet("SA_redet", SAX2, BODEN, FH, "sa1", "ausn"),
    *fig("SA", SAX2, BODEN, FH, [("ausn", "entschl")], erst="cut"),
    hart(fall_ns("SA", SAX2, "pause")),
    blase("sprech", 1060, 270, "st1", 1000, 250, inhalt=["Lehrkräfte dürfen im Dienst keine religiösen",
                                                      "Zeichen mehr tragen, an allen Schulen",
                                                      "des Landes. Ab dem 1. August gilt das auch für Sie."],
          textsize=30, figur=("ST_redet_r", STX2, BODEN, FH), bis="sa1"),
    blase("sprech", 820, 200, "sa1", 1050, 250, inhalt=["Ich unterrichte Mathe, nicht Religion.",
                                                     "Und mein Glaube verlangt das Kopftuch."],
          textsize=30, figur=("SA_redet", SAX2, BODEN, FH), bis="ausn"),
    pl("Ausnahme nach dem Gesetz: die Darstellung", 70, 190, "ausn", fill=GELB, size=30),
    pl("christlicher und abendländischer Bildungs- und Kulturwerte", 70, 254, "ausn", fill=GELB, size=30),
])

# ===========================================================================================================================
# A3 Die Fragen; die drei Leitentscheidungen
# ===========================================================================================================================
folie([("frage", "Die Fragen · Pauschales Verbot zulässig?"), ("frage2", "Die Fragen · Und vor Gericht?"),
       ("echt", "Die Fragen · Drei Entscheidungen des BVerfG")], [
    *tafel("frage", "Die Fragen"),
    z("1. Darf das Land Frau Sander das Kopftuch", 110, 190, "frage", "Bold", 36),
    z("so pauschal verbieten?", 145, 240, "frage", "Bold", 36),
    z("2. Und gilt vor Gericht dasselbe?", 110, 320, "frage2", "Bold", 36),
    blk(110, 420, 1040, 200, GELB, "echt", [("BVerfGE 108, 282 (2003) · Kopftuch I", "ExtraBold", 34, INK),
                                         ("BVerfGE 138, 296 (2015) · Kopftuch II", "ExtraBold", 34, INK),
                                         ("BVerfGE 153, 1 (2020) · Rechtsreferendarin", "ExtraBold", 34, INK)]),
    *requisit([("frage", ("tabler", "school", 130, WEISS), "Schule", WEISS),
               ("frage2", ("tabler", "gavel", 110, WEISS), "Gericht", WEISS),
               ("echt", ("tabler", "building-bank", 130, BLAUHELL), "Bundesverfassungsgericht", BLAUHELL)]),
    *paar("SA", [("frage", "entschl")], "ST", [("frage", "ernst"), ("echt", "ruhig")]),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_217(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=31, zeilenabstand=1.28)
        els += e; y += 14
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=30))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_217("sv", [
    "Frau Sander unterrichtet an einem staatlichen Gymnasium Mathematik, unter anderem in der Klasse 8b mit 27 Kindern. "
    "Sie trägt ein Kopftuch, weil sie es als verpflichtendes Gebot ihres Glaubens versteht. Streit darüber gab es an der "
    "Schule nie.",
    "Das Land beschließt ein neues Schulgesetz: Lehrkräfte dürfen im Dienst an allen Schulen des Landes keine religiösen "
    "Zeichen tragen. Ausgenommen ist nur die Darstellung christlicher und abendländischer Bildungs- und Kulturwerte. "
    "Schulleiter Steffens teilt Frau Sander mit, dass das Verbot ab dem 1. August auch für sie gilt.",
    "Herr Röder, Vater eines Schülers der 8b, will, dass sein Sohn in der Schule nicht religiös beeinflusst wird.",
], "Ist das pauschale Verbot mit dem Grundgesetz vereinbar?")

# ===========================================================================================================================
# C1 Art. 4 Abs. 1, 2 GG im Wortlaut
# ===========================================================================================================================
w4, w4_y = wortlaut(80, 190, 1100,
                    "„(1) Die Freiheit des Glaubens, des Gewissens und die Freiheit des religiösen und weltanschaulichen "
                    "Bekenntnisses sind unverletzlich. (2) Die ungestörte Religionsausübung wird gewährleistet.“",
                    "Art. 4 Abs. 1, 2 GG", "art4",
                    marken=[("Glaubens", beim("wl4", "Glaubens")), ("Bekenntnisses", beim("wl4", "Bekenntnisses")),
                            ("Religionsausübung", beim("wl4", "Religionsausübung"))])
folie([("art4", "Art. 4 GG · Maßstab"), ("wl4", "Art. 4 GG · Wortlaut")], [
    *tafel("art4", "Art. 4 GG: Glaubensfreiheit"),
    *w4,
    *requisit([("art4", ("tabler", "book", 110, WEISS), "Art. 4 GG", WEISS),
               (beim("wl4", "Religionsausübung"), ("tabler", "heart", 100, LILAHELL), "Religionsausübung", LILAHELL)]),
    *stehend("SA", FX, [("art4", "ruhig"), (beim("wl4", "Religionsausübung"), "froh")]),
])
assert w4_y <= 900, w4_y

# ===========================================================================================================================
# C2 I. Schutzbereich, II. Eingriff (BVerfGE 108, 282 Rn. 36 f., 40; 138, 296 Rn. 85 f., 89, 95 f.)
# ===========================================================================================================================
folie([("einh", "I. Schutzbereich › ein einheitliches Grundrecht"), ("leben", "I. Schutzbereich › Leben nach dem Glauben"),
       ("streit", "I. Schutzbereich › Kopftuchgebot umstritten?"), ("plaus", "I. Schutzbereich › plausibles Glaubensgebot (+)"),
       ("wahl", "II. Eingriff › Beruf oder Glaubensgebot"), ("schwer", "II. Eingriff › schwer (+)")], [
    *tafel("einh", "Schutzbereich und Eingriff"),
    z("Abs. 1 und 2: ein einheitliches Grundrecht", 110, 180, "einh", "Bold", 34),
    z("auch: ein Leben nach den Geboten des Glaubens", 110, 232, "leben", size=34),
    zit("BVerfGE 108, 282 Rn. 37; 138, 296 Rn. 85", 110, 280, "leben"),
    z("Ob der Islam das Kopftuch verlangt, ist umstritten.", 110, 340, "streit", size=34),
    z("Darauf kommt es nicht an:", 110, 390, "plaus", "Bold", 34),
    *okz("plausibel dargelegtes Glaubensgebot genügt", 440, beim("plaus", "plausibel"), "Bold", 34),
    zit("BVerfGE 108, 282 Rn. 40; 138, 296 Rn. 86, 89", 185, 488, beim("plaus", "plausibel")),
    blk(110, 560, 1040, 80, HELLROT, "wahl", [("Verbot: Beruf oder Glaubensgebot", "ExtraBold", 34, INK)]),
    *okz("schwerer Eingriff", 670, "schwer", "ExtraBold", 36),
    zit("BVerfGE 108, 282 Rn. 36; 138, 296 Rn. 90, 95 f.", 185, 722, "schwer"),
    *requisit([("einh", ("tabler", "book", 110, WEISS), "Art. 4 Abs. 1, 2 GG", WEISS),
               ("plaus", ("tabler", "heart", 100, LILAHELL), "Glaubensgebot", LILAHELL),
               ("wahl", ("tabler", "briefcase", 110, BLAUHELL), "Beruf oder Glaube?", HELLROT),
               ("schwer", ("tabler", "alert-triangle", 110, GELB), "schwerer Eingriff", HELLROT)]),
    *stehend("SA", FX, [("einh", "ruhig"), ("plaus", "froh"), ("wahl", "betroffen")]),
])

# ===========================================================================================================================
# D1 III. Rechtfertigung: Schranken (BVerfGE 108, 282 Rn. 38, 41; 138, 296 Rn. 98)
# ===========================================================================================================================
folie([("vorb", "III. Rechtfertigung › kein Gesetzesvorbehalt"), ("kvr", "III. Rechtfertigung › kollidierendes Verfassungsrecht"),
       ("best", "III. Rechtfertigung › hinreichend bestimmtes Gesetz"), ("drei", "III. Rechtfertigung › drei Gegenpositionen")], [
    *tafel("vorb", "III. Rechtfertigung: die Schranken"),
    *neinz("Gesetzesvorbehalt: keiner (vorbehaltlos)", 180, "vorb", "Bold", 34, kreuz=beim("vorb", "keinem")),
    zit("BVerfGE 108, 282 Rn. 38", 185, 228, "vorb"),
    z("Grenzen nur: kollidierendes Verfassungsrecht", 110, 300, "kvr", "Bold", 34),
    z("Grundrechte Dritter, Verfassungswerte", 145, 350, "kvr", size=33),
    blk(110, 420, 1040, 80, GELB, "best", [("und: ein hinreichend bestimmtes Gesetz", "ExtraBold", 34, INK)]),
    zit("BVerfGE 108, 282 Rn. 38, 57", 110, 510, "best"),
    z("Drei Gegenpositionen:", 110, 580, "drei", "ExtraBold", 36),
    z("Schüler · Eltern · staatlicher Erziehungsauftrag", 145, 636, "drei", size=34),
    zit("BVerfGE 108, 282 Rn. 41; 138, 296 Rn. 98", 145, 686, "drei"),
    *requisit([("vorb", ("tabler", "book", 110, WEISS), "Art. 4 GG: vorbehaltlos", WEISS),
               ("kvr", ("tabler", "scale", 120, WEISS), "Verfassung gegen Verfassung", GELB),
               ("best", ("tabler", "file-text", 100, WEISS), "bestimmtes Gesetz", GELB),
               ("drei", ("tabler", "school", 130, WEISS), "drei Gegenpositionen", WEISS)]),
    *stehend("SA", FX, [("vorb", "ruhig"), ("drei", "entschl")]),
])

# ===========================================================================================================================
# D2 Die drei Gegenpositionen (Art. 4, 6 Abs. 2, 7 Abs. 1 GG; BVerfGE 108, 282 Rn. 42–46)
# ===========================================================================================================================
w6, w6_y = wortlaut(80, 250, 1100, "„Pflege und Erziehung der Kinder sind das natürliche Recht der Eltern und die zuvörderst "
                                   "ihnen obliegende Pflicht. …“", "Art. 6 Abs. 2 GG", "a6", size=30,
                    marken=[("Erziehung", beim("a6", "Erziehungsrecht"))])
w7, w7_y = wortlaut(80, w6_y + 24, 1100, "„(1) Das gesamte Schulwesen steht unter der Aufsicht des Staates.“",
                    "Art. 7 Abs. 1 GG", "a7", size=30, marken=[("Aufsicht", beim("a7", "Aufsicht"))])
folie([("neg", "III. Rechtfertigung › 1. negative Glaubensfreiheit der Schüler"),
       ("a6", "III. Rechtfertigung › 2. Elternrecht, Art. 6 Abs. 2 GG"),
       ("a7", "III. Rechtfertigung › 3. Erziehungsauftrag, Art. 7 Abs. 1 GG"),
       ("neutral", "III. Rechtfertigung › 3. Neutralität")], [
    *tafel("neg", "Die drei Gegenpositionen"),
    z("1. negative Glaubensfreiheit der Schüler", 110, 180, "neg", "Bold", 34),
    *w6, *w7,
    blk(110, w7_y + 20, 1040, 80, BLAUHELL, "neutral", [("Auftrag religiös neutral erfüllen", "ExtraBold", 34, INK)]),
    zit("BVerfGE 108, 282 Rn. 41–44; 138, 296 Rn. 98, 109 f.", 110, w7_y + 110, "neutral"),
    *requisit([("neg", ("tabler", "school", 130, WEISS), "Schüler", WEISS),
               ("a6", ("tabler", "home", 110, WEISS), "Eltern", HELLGRUEN),
               ("a7", ("tabler", "building-bank", 120, WEISS), "Schulaufsicht", BLAUHELL),
               ("neutral", ("tabler", "scale", 120, WEISS), "neutral", BLAUHELL)]),
    *stehend("K1", X1, [("neg", "ruhig"), ("a7", "froh")]),
    *stehend("K3", X2, [("neg", "froh"), ("neutral", "ruhig")]),
])
assert w7_y + 150 <= 900, w7_y

# ===========================================================================================================================
# D3 Fall: Herr Röder, Vater eines Schülers (fiktiv)
# ===========================================================================================================================
RDX, K2X = 860, 1180
folie([("roeder", "Fall · Herr Röder, Vater eines Schülers"), ("rd1", "Fall · Das Anliegen der Eltern")], [
    boden("roeder"),
    feld(1500, BODEN - 300, 150, 300, "roeder", fill=HOLZ, rand=5, rund=4, name="tuer"),
    hart(pl("8b", 1575, 610, "roeder", fill=WEISS, size=30, anker="m")),
    hart(pl("Elternabend der Klasse 8b", 70, 40, "roeder", fill=ORANGE, size=32)),
    *fig("RD", RDX, BODEN, FH, [("roeder", "sorge_r")], bis="rd1", erst="cut"),
    *redet("RD_redet_r", RDX, BODEN, FH, "rd1", "k1"),
    hart(fall_ns("RD", RDX, "roeder")),
    *fig("K2", K2X, BODEN, KH, [("roeder", "ruhig")], erst="cut"),
    hart(pl("Röders Sohn", K2X, BODEN + 22, "roeder", fill=HELLGRAU, size=26, anker="m")),
    blase("sprech", 900, 200, "rd1", 1000, 270, inhalt=["Mein Sohn soll in der Schule nicht religiös",
                                                      "beeinflusst werden. Das entscheiden wir als Eltern."],
          textsize=30, figur=("RD_redet_r", RDX, BODEN, FH)),
])

# ===========================================================================================================================
# E Kopftuch I: BVerfGE 108, 282 (2003)
# ===========================================================================================================================
PK1 = "Kopftuch I (2003)"
folie([("k1", f"{PK1} · BVerfGE 108, 282"), ("bw", f"{PK1} › Bewerberin abgelehnt"),
       ("k1erg", f"{PK1} › hinreichend bestimmtes Gesetz nötig"), ("parl", f"{PK1} › Sache des Landesparlaments"),
       ("folge", f"{PK1} › danach: Landesgesetze")], [
    *tafel("k1", "Kopftuch I: BVerfGE 108, 282"),
    zit("Zweiter Senat, Urt. v. 24.9.2003 – 2 BvR 1436/02 (5 : 3 Stimmen)", 110, 176, "k1"),
    z("Baden-Württemberg lehnt eine Bewerberin ab,", 110, 236, "bw", "Bold", 34),
    z("weil sie im Unterricht Kopftuch tragen will", 110, 284, "bw", "Bold", 34),
    *neinz("ausdrückliches Gesetz: fehlte", 344, beim("bw", "ausdrückliches"), "Bold", 34,
           kreuz=beim("bw", "fehlte")),
    zit("Rn. 1, 3, 57–61", 700, 352, beim("bw", "ausdrückliches")),
    blk(110, 420, 1040, 130, GELB, "k1erg", [("Ein Verbot braucht eine hinreichend", "ExtraBold", 34, INK),
                                          ("bestimmte gesetzliche Grundlage.", "ExtraBold", 34, INK)]),
    zit("Leitsatz 1; Rn. 30, 49", 110, 560, "k1erg"),
    *okz("Ausgleich: Sache des Landesparlaments", 620, "parl", "Bold", 34),
    zit("Parlamentsvorbehalt, Rn. 47, 62, 66 f.", 185, 668, "parl"),
    z("danach: Verbote, etwa in Nordrhein-Westfalen", 110, 730, "folge", "Bold", 34),
    zit("BVerfGE 138, 296 Rn. 1, 134", 110, 778, "folge"),
    *requisit([("k1", ("tabler", "building-bank", 130, BLAUHELL), "BVerfG 2003", BLAUHELL),
               ("bw", ("tabler", "file-text", 100, WEISS), "kein Gesetz", HELLROT),
               ("k1erg", ("tabler", "book", 110, GELB), "Gesetz nötig", GELB),
               ("parl", ("tabler", "building-community", 130, WEISS), "Landtag", WEISS),
               ("folge", ("tabler", "book-2", 110, WEISS), "neue Landesgesetze", WEISS)]),
    *paar("SA", [("k1", "ruhig"), ("k1erg", "froh")], "ST", [("k1", "ruhig"), ("folge", "ernst")]),
])

# ===========================================================================================================================
# F1 Kopftuch II: BVerfGE 138, 296 (2015) – abstrakte vs. konkrete Gefahr
# ===========================================================================================================================
PK2 = "Kopftuch II (2015)"
folie([("k2", f"{PK2} · BVerfGE 138, 296"), ("abstr", f"{PK2} › abstrakte Gefahr genügt nicht"),
       ("konkr", f"{PK2} › hinreichend konkrete Gefahr nötig")], [
    *tafel("k2", "Kopftuch II: BVerfGE 138, 296"),
    zit("Erster Senat, Beschl. v. 27.1.2015 – 1 BvR 471/10, 1181/10 (6 : 2 Stimmen)", 110, 176, "k2"),
    z("Schulgesetz Nordrhein-Westfalen", 110, 236, "k2", "Bold", 34),
    z("landesweites Verbot wegen bloß abstrakter Gefahr", 110, 310, "abstr", "Bold", 34),
    z("bei als verpflichtend verstandenem Gebot:", 110, 358, beim("abstr", "wenn"), size=34),
    *neinz("unverhältnismäßig", 410, beim("abstr", "unverhältnismäßig"), "ExtraBold", 36),
    zit("Leitsatz 2; Rn. 101, 103", 185, 460, beim("abstr", "unverhältnismäßig")),
    z("Gesetz eng auslegen:", 110, 520, "konkr", "Bold", 34),
    blk(110, 576, 1040, 130, GRUEN, beim("konkr", "Nötig"), [("nötig: hinreichend konkrete Gefahr für", "ExtraBold", 34, INK),
                                                         ("Schulfrieden oder staatliche Neutralität", "ExtraBold", 34, INK)]),
    zit("Rn. 80, 108, 116", 110, 718, beim("konkr", "Nötig")),
    *requisit([("k2", ("tabler", "building-bank", 130, BLAUHELL), "BVerfG 2015", BLAUHELL),
               ("abstr", ("tabler", "help-circle", 110, WEISS), "abstrakte Gefahr?", HELLROT),
               (beim("konkr", "Nötig"), ("tabler", "alert-triangle", 110, GELB), "konkrete Gefahr", HELLGRUEN)]),
    *stehend("SA", FX, [("k2", "ruhig"), (beim("abstr", "unverhältnismäßig"), "froh")]),
])

# ===========================================================================================================================
# F2 Warum? Zurechnung, Schüler, Eltern, Konfliktlage (BVerfGE 138, 296 Rn. 104 f., 107, 112–114)
# ===========================================================================================================================
folie([("zurech", f"{PK2} › kein Symbol des Staates"), ("wirbt", f"{PK2} › Schüler: grundsätzlich nicht beeinträchtigt"),
       ("antw", f"{PK2} › Eltern: kein Anspruch"), ("stoer", f"{PK2} › anders bei ernsthafter Störung"),
       ("bezirk", f"{PK2} › auch für Schulen oder Bezirke")], [
    *tafel("zurech", "Warum die abstrakte Gefahr nicht reicht"),
    z("Kopftuch einer Lehrerin: kein Zeichen des Staates", 110, 180, "zurech", "Bold", 34),
    zit("anders: ein Symbol, das die Schule selbst aufhängt (Rn. 104, 112)", 110, 228, beim("zurech", "anders")),
    *okz("Schüler: grundsätzlich nicht beeinträchtigt,", 296, "wirbt", "Bold", 34),
    z("solange sie nicht für ihren Glauben wirbt", 185, 342, "wirbt", size=34),
    zit("Rn. 105", 900, 350, "wirbt"),
    *neinz("Eltern: kein Anspruch, Kinder fernzuhalten", 410, "antw", "Bold", 34, kreuz=beim("antw", "keinen")),
    zit("Rn. 107", 900, 458, "antw"),
    blk(110, 520, 1040, 130, HELLROT, "stoer", [("Anders bei heftigem Streit, der den", "ExtraBold", 34, INK),
                                             ("Schulbetrieb ernsthaft stört", "ExtraBold", 34, INK)]),
    z("dann Verbot auch für Schulen oder Bezirke", 110, 680, "bezirk", "Bold", 34),
    zit("Rn. 113 f.", 110, 728, "bezirk"),
    *requisit([("zurech", ("tabler", "school", 130, WEISS), "kein Zeichen des Staates", WEISS),
               ("wirbt", ("tabler", "speakerphone", 110, WEISS), "keine Werbung", WEISS),
               ("antw", ("tabler", "home", 110, WEISS), "Eltern", HELLGRUEN),
               ("stoer", ("tabler", "flame", 100, HELLROT), "ernsthafte Störung", HELLROT),
               ("bezirk", ("tabler", "map-2", 110, WEISS), "Schulen, Bezirke", WEISS)]),
    *stehend("RD", X1, [("zurech", "sorge"), ("antw", "denkt"), ("stoer", "ruhig")]),
    *stehend("K2", X2, [("zurech", "ruhig"), ("wirbt", "froh")]),
])

# ===========================================================================================================================
# F3 Die Ausnahme: Art. 33 Abs. 3, Art. 3 Abs. 3 GG (BVerfGE 138, 296 LS 4, Tenor, Rn. 123–138)
# ===========================================================================================================================
w33, w33_y = wortlaut(80, 240, 1100, "„… Niemandem darf aus seiner Zugehörigkeit oder Nichtzugehörigkeit zu einem "
                                     "Bekenntnisse oder einer Weltanschauung ein Nachteil erwachsen.“", "Art. 33 Abs. 3 S. 2 GG",
                      "a33", marken=[("Nachteil", beim("a33", "Nachteil"))])
folie([("priv", f"{PK2} › die Ausnahme für christliche Werte"), ("a33", f"{PK2} › Art. 33 Abs. 3 GG"),
       ("nichtig", f"{PK2} › Ausnahme nichtig"), ("alle", f"{PK2} › unterschiedslos für alle")], [
    *tafel("priv", "Die Ausnahme: gleichheitswidrig"),
    z("Ausnahme: christliche und abendländische Werte", 110, 176, "priv", "Bold", 34),
    *w33,
    *neinz("benachteiligt andere Religionen, auch Art. 3 Abs. 3 GG", w33_y + 30, "nichtig", "Bold", 33,
           kreuz=beim("nichtig", "benachteiligt")),
    blk(110, w33_y + 100, 1040, 80, HELLROT, beim("nichtig", "nichtig"), [("Die Ausnahme ist nichtig.", "ExtraBold", 34, INK)]),
    zit("Tenor; Rn. 123 f., 128, 138", 110, w33_y + 190, beim("nichtig", "nichtig")),
    blk(110, w33_y + 250, 1040, 80, GELB, "alle", [("Verbot nur unterschiedslos für alle Glaubensrichtungen", "ExtraBold", 31, INK)]),
    zit("Leitsatz 4", 110, w33_y + 340, "alle"),
    *requisit([("priv", ("tabler", "scale", 120, WEISS), "Ausnahme?", WEISS),
               ("nichtig", ("tabler", "circle-x", 110, HELLROT), "nichtig", HELLROT),
               ("alle", ("tabler", "equal", 110, GELB), "für alle gleich", GELB)]),
    *stehend("SA", FX, [("priv", "entschl"), ("alle", "ruhig")]),
])
assert w33_y + 380 <= 900, w33_y

# ===========================================================================================================================
# F4 Ergebnis im Fall: zurück im Klassenzimmer (die Geschichte kehrt in die 8b zurück)
# ===========================================================================================================================
SAX4, STX4 = 960, 1720
KX4 = (1280, 1480)
folie([("erg", "Ergebnis im Fall · keine konkrete Gefahr"), ("darf", "Ergebnis im Fall · Kopftuch erlaubt"),
       ("st2", "Ergebnis im Fall · Frau Sander unterrichtet weiter")], [
    boden("erg"),
    *schultafel(120, 300, 640, 300, "erg"),
    hart(kreide("a² + b² = c²", 200, 360, "erg")),
    hart(kreide("Klasse 8b", 200, 470, "erg", size=44)),
    pl("Im Fall: nie Streit, keine konkrete Gefahr", 70, 40, "erg", fill=WEISS, size=30),
    pl("Frau Sander darf mit Kopftuch unterrichten.", 70, 104, "darf", fill=HELLGRUEN, size=30),
    *fig("SA", SAX4, BODEN, FH, [("erg", "ruhig_r"), ("darf", "strahlt_r")], erst="cut"),
    hart(fall_ns("SA", SAX4, "erg")),
    *kinder(KX4, [[("erg", "ruhig"), ("darf", "froh")], [("erg", "froh")]]),
    *pulte(1180, 1580, "erg"),
    *fig("ST", STX4, BODEN, FH, [("erg", "ruhig")], bis="st2", erst="cut"),
    *redet("ST_redet2", STX4, BODEN, FH, "st2", "ref"),
    hart(fall_ns("ST", STX4, "erg")),
    blase("sprech", 980, 200, "st2", 1260, 270, inhalt=["Dann bleibt es dabei, Frau Sander:",
                                                      "Sie unterrichten die 8b weiter."],
          textsize=30, figur=("ST_redet2", STX4, BODEN, FH)),
])

# ===========================================================================================================================
# G1 Justiz: Gerichtssaal, Rechtsreferendarin (Funktionsrollen; Erlass nach BVerfGE 153, 1 Rn. 5, 9)
# ===========================================================================================================================
RFX, RIX = 820, 1530
folie([("ref", "Justiz · strenger als in der Schule"), ("hessen", "Justiz · Hessen, 2020: Rechtsreferendarin"),
       ("taet", "Justiz · keine Aufgaben als Vertreterin der Justiz"), ("ri1", "Justiz · Platz im Zuschauerraum")], [
    boden("ref"),
    hart(pl("Landgericht · Sitzungssaal", 70, 40, "ref", fill=WEISS, size=32)),
    feld(110, 760, 470, 40, "ref", fill=HOLZ, rand=5, rund=6, name="bank"),
    feld(140, 800, 26, BODEN - 800, "ref", fill=HOLZ, rand=4, rund=3, name="bankbein"),
    feld(524, 800, 26, BODEN - 800, "ref", fill=HOLZ, rand=4, rund=3, name="bankbein2"),
    hart(pl("Zuschauerraum", 345, 700, "ref", fill=WEISS, size=28, anker="m")),
    *fig("RI", RIX, BODEN, FH, [("ref", "ruhig")], bis="ri1", erst="cut"),
    *redet("RI_redet", RIX, BODEN, FH, "ri1", "ref2"),
    *richtertisch(1240, 1820, "ref"),
    hart(fall_ns("RI", RIX, "ref")),
    pl("Hessen, 2020: eine Rechtsreferendarin", 70, 104, "hessen", fill=HELLGRUEN, size=30),
    *fig("RF", RFX, BODEN, FH, [("taet", "ruhig_r"), (beim("ri1", "Sie"), "denkt_r")], erst="pop"),
    fall_ns("RF", RFX, "taet", d=0.1),
    pl("mit Kopftuch: keine Aufgaben als Vertreterin der Justiz", 70, 168, "taet", fill=WEISS, size=30),
    pl("etwa Richterbank, Sitzungsvertretung der Staatsanwaltschaft", 70, 232, beim("taet", "etwa"), fill=WEISS, size=30),
    blase("sprech", 780, 260, "ri1", 1440, 260, inhalt=["Heute bitte nicht auf die Richterbank.",
                                                      "Sie verfolgen die Verhandlung",
                                                      "aus dem Zuschauerraum."],
          textsize=30, figur=("RI_redet", RIX, BODEN, FH)),
])

# ===========================================================================================================================
# G2 BVerfGE 153, 1 (2020): Verbot verfassungsgemäß; Schule und Justiz (LS 5; Rn. 90, 95, 102)
# ===========================================================================================================================
PR = "Rechtsreferendarin (2020)"
folie([("ref2", f"{PR} · BVerfGE 153, 1: Verbot verfassungsgemäß"), ("hoheit", f"{PR} › Justiz: klassisch hoheitlich"),
       ("robe", f"{PR} › Robe und Ritual"), ("spiegel", f"{PR} › Schule: vielfältige Gesellschaft"),
       ("muss", f"{PR} › darf verbieten, muss nicht")], [
    *tafel("ref2", "Rechtsreferendarin: BVerfGE 153, 1"),
    zit("Zweiter Senat, Beschl. v. 14.1.2020 – 2 BvR 1333/17 (7 : 1 Stimmen)", 110, 176, "ref2"),
    *okz("Verbot verfassungsgemäß", 236, beim("ref2", "verfassungsgemäß"), "ExtraBold", 36),
    z("Justiz: Der Staat tritt klassisch hoheitlich auf.", 110, 320, "hoheit", "Bold", 34),
    z("Robe und Ritual: Er prägt das Bild der Verhandlung.", 110, 372, "robe", "Bold", 34),
    zit("Leitsatz 5; Rn. 90, 95", 110, 420, "robe"),
    z("Schule: soll die vielfältige Gesellschaft spiegeln.", 110, 490, "spiegel", "Bold", 34),
    zit("Rn. 95; BVerfGE 138, 296 Rn. 105", 110, 538, "spiegel"),
    blk(110, 610, 1040, 80, GELB, "muss", [("Das Land darf verbieten, muss es aber nicht.", "ExtraBold", 34, INK)]),
    zit("Rn. 102", 110, 700, "muss"),
    *requisit([("ref2", ("tabler", "building-bank", 130, BLAUHELL), "BVerfG 2020", BLAUHELL),
               ("hoheit", ("tabler", "gavel", 110, WEISS), "Justiz", WEISS),
               ("spiegel", ("tabler", "school", 130, WEISS), "Schule", HELLGRUEN),
               ("muss", ("tabler", "scale", 120, WEISS), "darf, muss nicht", GELB)]),
    *paar("RF", [("ref2", "denkt"), ("spiegel", "ruhig")], "RI", [("ref2", "ruhig"), ("hoheit", "ernst"), ("muss", "ruhig")]),
])

# ===========================================================================================================================
# H Heute: § 34 Abs. 2 BeamtStG (Fassung 2021); § 61 Abs. 2 BBG
# ===========================================================================================================================
w34, w34_y = wortlaut(80, 240, 1100,
                      "„Religiös oder weltanschaulich konnotierte Merkmale des Erscheinungsbilds nach Satz 2 können nur "
                      "dann eingeschränkt oder untersagt werden, wenn sie objektiv geeignet sind, das Vertrauen in die "
                      "neutrale Amtsführung der Beamtin oder des Beamten zu beeinträchtigen.“", "§ 34 Abs. 2 S. 4 BeamtStG",
                      "wl34", size=31,
                      marken=[("objektiv", beim("wl34", "objektiv")), ("neutrale", beim("wl34", "neutrale"))])
folie([("heute", "Heute · § 34 Abs. 2 BeamtStG"), ("wl34", "Heute · § 34 Abs. 2 S. 4 BeamtStG, Wortlaut"),
       ("laender", "Heute · Einzelheiten: Landesrecht")], [
    *tafel("heute", "Heute: § 34 Abs. 2 BeamtStG"),
    z("für Landesbeamte, gefasst 2021", 110, 176, "heute", "Bold", 34),
    *w34,
    zit("Bund: § 61 Abs. 2 S. 4 BBG, gleichlautend", 110, w34_y + 20, "wl34"),
    blk(110, w34_y + 90, 1040, 80, BLAUHELL, "laender", [("Einzelheiten: Landesrecht (§ 34 Abs. 2 S. 5)", "ExtraBold", 33, INK)]),
    *requisit([("heute", ("tabler", "book", 110, WEISS), "Beamtenstatusgesetz", WEISS),
               (beim("wl34", "objektiv"), ("tabler", "scale", 120, WEISS), "objektiv geeignet?", GELB),
               ("laender", ("tabler", "map-2", 110, WEISS), "Landesrecht", BLAUHELL)]),
    *stehend("SA", FX, [("heute", "ruhig"), ("laender", "froh")]),
])
assert w34_y + 190 <= 900, w34_y

# ===========================================================================================================================
# I Klausurtipp mit Prüfungsaufbau (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Art. 4 GG im Dreischritt"), ("t1", "Klausurtipp › I. Schutzbereich"),
       ("t2", "Klausurtipp › II. Eingriff"), ("t3", "Klausurtipp › III. Rechtfertigung"),
       ("t3b", "Klausurtipp › III. abstrakte oder konkrete Gefahr?"), ("t4", "Klausurtipp › Schule und Justiz trennen")], [
    *tafel("tipp", "Klausurtipp: Art. 4 GG im Dreischritt", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("I. Schutzbereich: plausibel dargelegtes", 200, 200, "t1", "ExtraBold", 35),
    z("Glaubensgebot genügt", 240, 250, "t1", size=34),
    z("II. Eingriff: Wie schwer wiegt er?", 200, 320, "t2", "ExtraBold", 35),
    z("III. Rechtfertigung:", 200, 390, "t3", "ExtraBold", 35),
    z("bestimmtes Gesetz? kollidierendes Verfassungsgut?", 240, 440, beim("t3", "Gibt"), size=33),
    blk(200, 500, 950, 80, GELB, "t3b", [("Kern: abstrakte oder konkrete Gefahr?", "ExtraBold", 34, INK)]),
    linienzug([(130, 610), (1130, 610)], "t4", breite=3),
    z("Schule und Justiz trennen", 200, 630, "t4", "ExtraBold", 35),
    z("Ausnahmen für einzelne Religionen: Art. 33 Abs. 3 GG", 240, 684, beim("t4", "prüfe"), size=32),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "merke"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# J Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("In der Schule reicht die bloß ", 0), ("abstrakte", "a")],
                 [("Gefahr für ein Kopftuchverbot nicht,", 0)], [("es braucht eine ", 0), ("konkrete", "b"), (".", 0)]],
                750, 270, 42, "merke", {"a": beim("merke", "abstrakte"), "b": beim("merke", "konkrete")}),
    *markertext([[("Vor Gericht darf der Staat ", 0), ("strenger", "c"), (" sein.", 0)]],
                750, 520, 42, "m2", {"c": beim("m2", "strenger")}),
    *markertext([[("Jedes Verbot muss für ", 0), ("alle", "d"), (" Religionen", 0)], [("gleich gelten.", 0)]],
                750, 640, 42, "m3", {"d": beim("m3", "alle")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
