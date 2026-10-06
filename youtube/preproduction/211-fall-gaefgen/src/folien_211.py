"""Folge 211 · Fall Gäfgen: Folterdrohung, § 136a StPO & Fernwirkung – Serienstandard Open Peeps (Katzenkönig).
Fiktiver Rahmen, der dem echten Fall folgt (EGMR [GK] Gäfgen/Deutschland, 1.6.2010, Nr. 22978/05, §§ 10–51): Herr Wallmann
holt das Lösegeld ab und wird festgenommen; der stellvertretende Polizeipräsident Herr Rombach lässt ihm durch Kommissar
Leitner Schmerzen androhen; er nennt das Versteck; dort Spuren. Danach § 136a StPO (Wortlautkarten Abs. 1, Abs. 3 S. 2),
Fortwirkung und qualifizierte Belehrung, Fernwirkung (BGH; LG Frankfurt), Hauptverhandlung mit neuem Geständnis, EGMR
(Art. 3 EMRK Wortlautkarte; Art. 6), die Polizisten (LG Frankfurt 20.12.2004; § 34 StGB, Art. 1 Abs. 1 GG Wortlautkarte),
Klausurtipp mit Prüfungsaufbau, Merksatz.
DARSTELLUNG: Das Kind wird nie gezeigt und nie benannt; keine Gewalt, keine Folterinstrumente, keine Fesseln; die Drohung
steht nur als Sprechblase. Alle Figuren fiktiv; „Gäfgen“ nur als Fallbezeichnung auf der Frage-Tafel.
Szenen laut ../SZENENPLAN.md. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/feld/requisit/
stehend/paar als eigene Kopie aus Folge 208 (gemeinsame Dateien unverändert); neu: raum(), tisch(), richtertisch(),
haltestelle(), kette().
Handlungsgeräusch: Tür fällt hinter Kommissar Leitner zu (Freesound CC0 341300); ../geraeusche_herkunft.json.
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut StPO/GG nach gesetze-im-internet.de, Art. 3 EMRK nach der
deutschen Übersetzung des EGMR (die EMRK steht nicht auf gesetze-im-internet.de), Abruf 06.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_211/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_211/" in n:
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
NAME = {"WA": "Herr Wallmann", "RO": "Herr Rombach", "LE": "Kommissar Leitner", "VE": "Verteidigerin", "RI": "Vorsitzende Richterin"}
NFARBE = {"WA": TUERKIS_, "RO": LILA, "LE": BLAU, "VE": PINK, "RI": GELB}
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


# ===========================================================================================================================
# A1 Fall: Entführung, Lösegeld, Festnahme (EGMR §§ 12–14)
# ===========================================================================================================================
WAX1 = 1380
folie([(NULL, "Fall · Frankfurt am Main, Herbst 2002"), ("entf", "Fall · Ein Kind ist entführt"),
       ("fest", "Fall · Die Festnahme"), ("falsch", "Fall · Nur falsche Hinweise")], [
    boden(NULL),
    hart(linienzug([(900, BODEN), (900, 470)], NULL, breite=8)),
    hart(ficon("tabler", "bus-stop", 900, 470, 120, NULL, fuell=GELB)),
    hart(pl("Haltestelle", 900, 640, NULL, fill=WEISS, size=28, anker="m")),
    hart(ficon("tabler", "building", 1700, BODEN, 300, NULL, fuell=WAND)),
    hart(pl("Frankfurt am Main, Herbst 2002", 70, 40, NULL, fill=ORANGE, size=32)),
    pl("Ein Kind ist entführt.", 70, 108, "entf", fill=HELLGRAU, size=30),
    pl("Lösegeld: 1 Mio. €", 70, 172, beim("entf", "Million"), fill=GELB, size=30),
    ficon("tabler", "moneybag", 1150, BODEN, 110, "fest", fuell=GELB, bis=beim("fest", "nimmt")),
    ficon("tabler", "binoculars", 560, 400, 110, "fest", fuell=BLAUHELL),
    pl("Die Polizei beobachtet die Geldabholung.", 70, 236, "fest", fill=BLAUHELL, size=30),
    pl("Festnahme", 70, 300, beim("fest", "nimmt"), fill=HELLROT, size=30),
    *fig("WA", WAX1, BODEN, FH, [("fest", "ruhig"), (beim("fest", "nimmt"), "ernst"), ("falsch", "denkt")]),
    ns(NAME["WA"], WAX1, BODEN, "fest", TUERKIS_, d=0.1),
    pl("Wo ist das Kind?", 70, 364, "falsch", fill=WEISS, size=30),
    pl("nur falsche Hinweise", 160, 428, beim("falsch", "falsche"), fill=HELLROT, size=30),
    nein(100, 452, beim("falsch", "falsche")),
])

# ===========================================================================================================================
# A2 Fall: Büro des stellvertretenden Polizeipräsidenten, am Morgen (EGMR §§ 15, 47)
# ===========================================================================================================================
ROX, LEX = 760, 1300
folie([("vize", "Fall · Der stellvertretende Polizeipräsident"), ("ro1", "Fall · Die Anweisung")], [
    *raum("vize", fenster_x=120),
    hart(ficon("tabler", "sunrise", 270, 420, 110, "vize", fuell=GELB)),
    pl("1.10.2002, früh am Morgen", 70, 40, "vize", fill=GELB, size=32),
    pl("stellvertretender Polizeipräsident", 70, 104, "vize", fill=LILAHELL, size=30),
    *fig("RO", ROX, BODEN, FH, [("vize", "drang_r")], bis="ro1", erst="cut"),
    *redet("RO_redet_r", ROX, BODEN, FH, "ro1", "leit"),
    hart(ns(NAME["RO"], ROX, BODEN, "vize", LILA)),
    *fig("LE", LEX, BODEN, FH, [("vize", "ernst"), ("ro1", "sorge")], erst="cut"),
    hart(ns(NAME["LE"], LEX, BODEN, "vize", BLAU)),
    *tisch(560, 980, "vize"),
    blase("sprech", 700, 200, "ro1", 1180, 230, inhalt=["Drohen Sie ihm Schmerzen an.", "Er muss sagen, wo das Kind ist."],
          textsize=32, figur=("RO_redet_r", ROX, BODEN, FH)),
])

# ===========================================================================================================================
# A3 Fall: Vernehmungsraum (EGMR §§ 15 f., 26, 47)
# ===========================================================================================================================
TUER = 230
LE_START, LE_ZIEL = 305, 820
WAX3 = 1450
GEHT = ("leit", 1.6)
ZU3 = ("leit", 1.9)


def tuer_offen3(cue, bis):
    return El(_feld(150, 300, INK, 5, 2), TUER - 6, BODEN - 300 - 6, cue, "cut", 0.0, bis, name="tuer_offen")


folie([("leit", "Fall · Im Vernehmungsraum"), ("le1", "Fall · Die Drohung"), ("nennt", "Fall · Er nennt das Versteck"),
       ("spaet", "Fall · Für das Kind zu spät")], [
    *raum("leit", tuer_x=TUER),
    pl("Vernehmungsraum", 70, 40, "leit", fill=BLAUHELL, size=32),
    tuer_offen3("leit", ZU3),
    szene(hart(feld(TUER, BODEN - 300, 150, 300, ZU3, fill=HOLZ, rand=5, rund=4, name="tuer_zu")), "211tuer*", 0.8, -0.08),
    *fig("WA", WAX3, BODEN, FH, [("leit", "ernst"), ("le1", "angst"), ("nennt", "sorge"), ("spaet", "muede")], erst="cut"),
    hart(ns(NAME["WA"], WAX3, BODEN, "leit", TUERKIS_)),
    bewegt(peep_voll("LE_ernst_r", LE_ZIEL, BODEN, FH, "leit", anim="cut", bis="le1"), "leit", GEHT, LE_START - LE_ZIEL),
    bewegt(ns(NAME["LE"], LE_ZIEL, BODEN, "leit", BLAU, bis="le1", anim="cut"), "leit", GEHT, LE_START - LE_ZIEL),
    *redet("LE_redet_r", LE_ZIEL, BODEN, FH, "le1", "nennt"),
    *fig("LE", LE_ZIEL, BODEN, FH, [("nennt", "feierlich_r")], erst="cut"),
    ns(NAME["LE"], LE_ZIEL, BODEN, "le1", BLAU, anim="cut"),
    *tisch(1000, 1600, "leit"),
    blase("sprech", 760, 200, "le1", 1100, 230, inhalt=["Sagen Sie, wo das Kind ist. Sonst werden",
                                                      "Ihnen große Schmerzen zugefügt."],
          textsize=30, figur=("LE_redet_r", LE_ZIEL, BODEN, FH), bis="nennt"),
    pl("nach rund 10 Minuten: Er nennt das Versteck.", 70, 108, "nennt", fill=WEISS, size=30),
    ficon("tabler", "map-pin", 1450, 330, 90, "nennt", fuell=ROT),
    pl("Für das Kind kommt jede Hilfe zu spät.", 70, 172, "spaet", fill=HELLGRAU, size=30),
])

# ===========================================================================================================================
# A4 Fall: Am Versteck – Spuren (EGMR § 18); keine Darstellung des Opfers
# ===========================================================================================================================
folie([("spur", "Fall · Spuren am Versteck")], [
    boden("spur"),
    *[hart(ficon("tabler", "trees", x, BODEN, w, "spur", fuell=GRUEN)) for x, w in ((220, 260), (560, 200), (1720, 240))],
    hart(linienzug([(760, BODEN - 40), (1500, BODEN - 40)], "spur", breite=6, farbe=TEXT)),
    hart(linienzug([(760, BODEN - 90), (1500, BODEN - 90)], "spur", breite=6, farbe=TEXT)),
    pl("Am Versteck: Beweise gegen ihn", 70, 40, "spur", fill=GELB, size=32),
    ficon("tabler", "car", 1130, 620, 170, beim("spur", "Reifenspuren"), fuell=BLAUHELL),
    ficon("tabler", "search", 1130, 420, 100, beim("spur", "Reifenspuren"), fuell=WEISS),
    pl("Reifenspuren seines Autos", 1130, 700, beim("spur", "Reifenspuren"), fill=WEISS, size=30, anker="m"),
])

# ===========================================================================================================================
# A5 Die Fragen; der echte Fall (Rubrum)
# ===========================================================================================================================
folie([("frage", "Die Fragen · Ist die Aussage verwertbar?"), ("frage2", "Die Fragen · Und die Spuren vom Versteck?"),
       ("frage3", "Die Fragen · Durfte die Polizei so handeln?"), ("echt", "Die Fragen · Fall Gäfgen, EGMR 2010")], [
    *tafel("frage", "Die Fragen"),
    z("1. Darf das Gericht seine Aussage verwerten?", 110, 190, "frage", "Bold", 36),
    z("2. Was ist mit den Spuren vom Versteck?", 110, 270, "frage2", "Bold", 36),
    z("3. Durfte die Polizei so handeln?", 110, 350, "frage3", "Bold", 36),
    blk(110, 450, 1040, 130, GELB, "echt", [("Fall Gäfgen: EGMR (Große Kammer)", "ExtraBold", 34, INK),
                                         ("Urt. v. 1.6.2010 – Nr. 22978/05", "Regular", 32, INK)]),
    zit("unser Fall folgt dem echten Fall (EGMR §§ 10–51)", 110, 594, "echt"),
    *paar("WA", [("frage", "denkt")], "RO", [("frage", "ernst"), ("frage3", "feierlich")]),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_211(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=31, zeilenabstand=1.28)
        els += e; y += 14
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=30))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_211("sv", [
    "Frankfurt am Main, Herbst 2002: Ein Kind ist entführt, die Eltern sollen 1 Mio. € Lösegeld zahlen. Die Polizei "
    "beobachtet, wie Herr Wallmann das Geld abholt, und nimmt ihn fest. Wo das Kind ist, verrät er nicht; er gibt nur "
    "falsche Hinweise.",
    "Am nächsten Morgen weist der stellvertretende Polizeipräsident Rombach an, ihm Schmerzen anzudrohen. Kommissar "
    "Leitner droht Herrn Wallmann große Schmerzen an, falls er nicht sagt, wo das Kind ist. Nach rund 10 Minuten nennt "
    "er das Versteck. Für das Kind kommt jede Hilfe zu spät. Am Versteck sichert die Polizei Beweise, etwa Reifenspuren "
    "seines Autos.",
    "Später belehrt man ihn nur über sein Schweigerecht; er wiederholt sein Geständnis bei Polizei, Staatsanwaltschaft "
    "und Richter. In der Hauptverhandlung beantragt seine Verteidigerin, auch die Beweise vom Versteck nicht zu verwerten.",
], "Was darf das Gericht verwerten – und durfte die Polizei so handeln?")

# ===========================================================================================================================
# C1 § 136a StPO: Wortlautkarte Abs. 1
# ===========================================================================================================================
PA = "§ 136a StPO"
w1, w1_y = wortlaut(80, 180, 1100,
                    "„(1) Die Freiheit der Willensentschließung und der Willensbetätigung des Beschuldigten darf nicht "
                    "beeinträchtigt werden durch Mißhandlung, durch Ermüdung, durch körperlichen Eingriff, durch "
                    "Verabreichung von Mitteln, durch Quälerei, durch Täuschung oder durch Hypnose. … Die Drohung mit "
                    "einer nach seinen Vorschriften unzulässigen Maßnahme und das Versprechen eines gesetzlich nicht "
                    "vorgesehenen Vorteils sind verboten. …“", "§ 136a Abs. 1 StPO", "norm",
                    marken=[("Willensentschließung", beim("wl", "Willensentschließung")),
                            ("Mißhandlung", beim("wl", "Misshandlung")), ("Quälerei", beim("wl", "Quälerei")),
                            ("Drohung", beim("wl2", "Drohung")), ("unzulässigen", beim("wl2", "unzulässigen")),
                            ("verboten", beim("wl2", "verboten"))])
folie([("norm", f"{PA} · Wortlaut"), ("wl", f"{PA} › Freiheit der Willensentschließung"),
       ("wl2", f"{PA} › Drohung mit unzulässiger Maßnahme verboten")], [
    *tafel("norm", "§ 136a StPO: verbotene Methoden"),
    *w1,
    *requisit([("norm", ("tabler", "book", 110, WEISS), "§ 136a StPO", WEISS),
               ("wl2", ("tabler", "hand-stop", 110, HELLROT), "Drohung verboten", HELLROT)]),
    *stehend("WA", FX, [("norm", "ruhig"), ("wl2", "ernst")]),
])

# ===========================================================================================================================
# C2 Im Fall: Drohung verboten; Abs. 3 S. 2 (EGMR §§ 26, 29)
# ===========================================================================================================================
w3, w3_y = wortlaut(80, 410, 1100,
                    "„Aussagen, die unter Verletzung dieses Verbots zustande gekommen sind, dürfen auch dann nicht "
                    "verwertet werden, wenn der Beschuldigte der Verwertung zustimmt.“", "§ 136a Abs. 3 S. 2 StPO", "abs3",
                    marken=[("nicht", beim("abs3", "nicht")), ("zustimmt", beim("abs3", "zustimmt"))])
folie([("sub", f"{PA} › im Fall: Schmerzen nie erlaubt"), ("sub2", f"{PA} › schon die Drohung verboten"),
       ("abs3", f"{PA} › Abs. 3: Aussage unverwertbar"), ("gesetz", f"{PA} › das Gesetz entscheidet, keine Abwägung"),
       ("v171", f"{PA} › siehe Folge 171")], [
    *tafel("sub", "Im Fall: die Drohung mit Schmerzen"),
    *neinz("Schmerzen zufügen, um eine Aussage zu", 175, "sub", "Bold", 33, kreuz=beim("sub", "nie")),
    z("erzwingen: nie erlaubt", 185, 221, "sub", "Bold", 33),
    blk(110, 285, 1040, 80, HELLROT, "sub2", [("Schon die Drohung war verboten.", "ExtraBold", 34, INK)]),
    zit("§ 136a Abs. 1 S. 3 StPO; LG Frankfurt, 9.4.2003 (EGMR §§ 26, 29)", 110, 374, "sub2"),
    *w3,
    blk(110, w3_y + 20, 1040, 80, GELB, "gesetz", [("Das Gesetz entscheidet selbst, keine Abwägung", "ExtraBold", 33, INK)]),
    blk(110, w3_y + 120, 1040, 80, BLAUHELL, "v171", [("Mehr dazu: Folge 171 · Belehrungsverstoß", "ExtraBold", 33, INK)]),
    *requisit([("sub", ("tabler", "hand-stop", 110, HELLROT), "verboten", HELLROT),
               ("abs3", ("tabler", "microphone-off", 110, WEISS), "unverwertbar", HELLROT),
               ("gesetz", ("tabler", "book", 110, WEISS), "Gesetz", GELB)]),
    *paar("LE", [("sub", "feierlich"), ("abs3", "muede")], "WA", [("sub", "ernst")]),
])
assert w3_y + 200 <= 900, w3_y

# ===========================================================================================================================
# C3 Fortwirkung und qualifizierte Belehrung (EGMR §§ 22, 28–30)
# ===========================================================================================================================
PF = "Fortwirkung"
folie([("fort", f"{PF} · LG Frankfurt, 9.4.2003"), ("fort2", f"{PF} › spätere Aussagen unverwertbar"),
       ("qual", f"{PF} › nur qualifizierte Belehrung hätte geholfen"), ("nurs", f"{PF} › belehrt nur über das Schweigerecht")], [
    *tafel("fort", "Fortwirkung: die späteren Aussagen"),
    z("LG Frankfurt, Beschl. v. 9.4.2003:", 110, 180, "fort", "Bold", 34),
    *neinz("spätere Aussagen bei Polizei, Staatsanwalt-", 250, "fort2", "Bold", 33, kreuz=beim("fort2", "unverwertbar")),
    z("schaft und Richter: ebenfalls unverwertbar", 185, 296, "fort2", "Bold", 33),
    zit("Grund: Die Drohung wirkte fort (EGMR §§ 28 f.).", 185, 344, beim("fort2", "fortwirkte")),
    blk(110, 410, 1040, 130, GELB, "qual", [("Heilung nur durch qualifizierte Belehrung:", "ExtraBold", 33, INK),
                                         ("frühere Aussagen dürfen nicht verwertet werden", "Regular", 32, INK)]),
    zit("EGMR § 30", 110, 552, "qual"),
    *neinz("belehrt nur über das Schweigerecht", 610, "nurs", "Bold", 34, kreuz=beim("nurs", "nur")),
    zit("EGMR §§ 14, 30", 185, 660, "nurs"),
    *requisit([("fort", ("tabler", "building-bank", 120, WEISS), "Landgericht", WEISS),
               ("fort2", ("tabler", "repeat", 110, HELLROT), "Fortwirkung", HELLROT),
               ("qual", ("tabler", "info-circle", 110, GELB), "qualifizierte Belehrung", GELB),
               ("nurs", ("tabler", "microphone-off", 110, WEISS), "nur Schweigerecht", WEISS)]),
    *stehend("WA", FX, [("fort", "ruhig"), ("fort2", "denkt"), ("nurs", "ernst")]),
])

# ===========================================================================================================================
# D1 Hauptverhandlung: Antrag der Verteidigerin (EGMR § 25)
# ===========================================================================================================================
VEX, WAX4, RIX = 380, 760, 1520


def saal(cue):
    return [boden(cue),
            hart(pl("Landgericht Frankfurt am Main", 70, 40, cue, fill=WEISS, size=32))]


folie([("hv", "Fernwirkung · Die Hauptverhandlung"), ("ve1", "Fernwirkung · Antrag der Verteidigerin")], [
    *saal("hv"),
    *fig("RI", RIX, BODEN, FH, [("hv", "ruhig")], erst="cut"),
    *richtertisch(1240, 1820, "hv"),
    hart(ns(NAME["RI"], RIX, BODEN, "hv", GELB)),
    *fig("WA", WAX4, BODEN, FH, [("hv", "ernst_r")], erst="cut"),
    hart(ns(NAME["WA"], WAX4, BODEN, "hv", TUERKIS_)),
    *fig("VE", VEX, BODEN, FH, [("hv", "denkt_r")], bis="ve1", erst="cut"),
    *redet("VE_redet_r", VEX, BODEN, FH, "ve1", "fern"),
    hart(ns(NAME["VE"], VEX, BODEN, "hv", PINK)),
    blase("sprech", 820, 170, "ve1", 760, 200, inhalt=["Dann dürfen auch die Beweise vom Versteck",
                                                      "nicht verwertet werden!"],
          textsize=30, figur=("VE_redet_r", VEX, BODEN, FH)),
])

# ===========================================================================================================================
# D2 Fernwirkung: BGH und LG Frankfurt (BGH 1 StR 316/05 Rn. 22 f.; BGHSt 34, 362, 364; EGMR §§ 25, 31)
# ===========================================================================================================================
folie([("fern", "Fernwirkung · Früchte des vergifteten Baumes?"), ("bgh", "Fernwirkung › BGH: grundsätzlich abgelehnt"),
       ("bgh2", "Fernwirkung › Verfahren nicht lahmlegen"), ("lg", "Fernwirkung › LG Frankfurt: Abwägung"),
       ("lg3", "Fernwirkung › Spuren verwertbar")], [
    *tafel("fern", "Fernwirkung: die Spuren vom Versteck"),
    z("Lehre von den Früchten des vergifteten Baumes?", 110, 180, "fern", "Bold", 34),
    zit("„fruit of the poisonous tree“ – Antrag der Verteidigung (EGMR § 25)", 110, 228, "fern"),
    *neinz("BGH: Fernwirkung grundsätzlich abgelehnt", 290, "bgh", "Bold", 34, kreuz=beim("bgh", "ab", ende=True)),
    zit("BGH, Beschl. v. 7.3.2006 – 1 StR 316/05, Rn. 22 f.; BGHSt 34, 362, 364", 185, 338, "bgh"),
    z("Ein Verfahrensfehler soll nicht das ganze", 185, 390, "bgh2", size=33),
    z("Strafverfahren „lahmlegen“.", 185, 436, "bgh2", size=33),
    zit("1 StR 316/05, Rn. 23", 600, 444, "bgh2"),
    z("LG Frankfurt, 9.4.2003: Abwägung", 110, 510, "lg", "Bold", 34),
    z("Schwere des Eingriffs gegen Schwere des Vorwurfs", 185, 560, "lg2", size=33),
    z("(Mord an einem Kind)", 185, 606, beim("lg2", "Mord"), size=33),
    blk(110, 670, 1040, 130, GRUEN, "lg3", [("Ausschluss unverhältnismäßig:", "ExtraBold", 34, INK),
                                         ("Die Spuren bleiben verwertbar.", "ExtraBold", 34, INK)]),
    zit("EGMR § 31", 110, 812, "lg3"),
    *requisit([("fern", ("tabler", "tree", 120, GRUEN), "Fernwirkung?", WEISS),
               ("bgh", ("tabler", "building-bank", 120, WEISS), "BGH: nein", HELLROT),
               ("lg", ("tabler", "scale", 120, WEISS), "Abwägung", GELB),
               ("lg3", ("tabler", "car", 130, BLAUHELL), "Spuren verwertbar", HELLGRUEN)]),
    *paar("VE", [("fern", "ernst"), ("lg3", "denkt")], "WA", [("fern", "ruhig")]),
])

# ===========================================================================================================================
# D3 Hauptverhandlung: neue Belehrung, neues Geständnis, Urteil (EGMR §§ 32–34, 179, 182 f.)
# ===========================================================================================================================
folie([("rich", "Hauptverhandlung · qualifizierte Belehrung"), ("gest", "Hauptverhandlung · neues Geständnis"),
       ("urt", "Hauptverhandlung › Urteil stützt sich auf das neue Geständnis"),
       ("pruef", "Hauptverhandlung › Spuren nur zur Überprüfung"), ("lebens", "Hauptverhandlung › lebenslange Freiheitsstrafe")], [
    *saal("rich"),
    *fig("RI", RIX, BODEN, FH, [("rich", "ernst")], bis="ri1", erst="cut"),
    *redet("RI_redet", RIX, BODEN, FH, "ri1", "gest"),
    *fig("RI", RIX, BODEN, FH, [("gest", "ruhig"), ("lebens", "ernst")], erst="cut"),
    *richtertisch(1240, 1820, "rich"),
    hart(ns(NAME["RI"], RIX, BODEN, "rich", GELB)),
    *fig("WA", WAX4, BODEN, FH, [("rich", "ruhig_r"), ("gest", "reue_r"), ("lebens", "muede_r")], erst="cut"),
    hart(ns(NAME["WA"], WAX4, BODEN, "rich", TUERKIS_)),
    *fig("VE", VEX, BODEN, FH, [("rich", "ruhig_r"), ("urt", "ernst_r")], erst="cut"),
    hart(ns(NAME["VE"], VEX, BODEN, "rich", PINK)),
    pl("qualifizierte Belehrung", 70, 104, "rich", fill=GELB, size=30),
    blase("sprech", 700, 200, "ri1", 1080, 300, inhalt=["Sie dürfen schweigen. Ihre früheren", "Aussagen werden nicht",
                                                      "gegen Sie verwertet."],
          textsize=30, figur=("RI_redet", RIX, BODEN, FH), bis="gest"),
    pl("neues Geständnis, aus Reue, wie er sagt", 70, 168, "gest", fill=WEISS, size=30),
    pl("Verurteilung stützt sich auf das neue Geständnis", 70, 232, "urt", fill=BLAUHELL, size=30),
    pl("Spuren: nur zur Überprüfung", 70, 296, "pruef", fill=WEISS, size=30),
    pl("Urteil 28.7.2003: lebenslange Freiheitsstrafe", 70, 360, "lebens", fill=HELLROT, size=30),
])

# ===========================================================================================================================
# E1 EGMR: Art. 3 EMRK (Wortlautkarte; §§ 87, 107 f., 131 f.; Tenor Nr. 3)
# ===========================================================================================================================
PE = "EGMR · Art. 3 EMRK"
wA3, wA3_y = wortlaut(80, 250, 1100, "„Niemand darf der Folter oder unmenschlicher oder erniedrigender Behandlung oder Strafe "
                                     "unterworfen werden.“", "Art. 3 EMRK (deutsche Übersetzung des EGMR)", "a3",
                      marken=[("Folter", beim("a3", "Folter")), ("unmenschlicher", beim("a3", "unmenschlicher"))])
folie([("egmr", "EGMR · Große Kammer, 1.6.2010"), ("a3", f"{PE} · Wortlaut"), ("ub", f"{PE} › unmenschliche Behandlung"),
       ("abs", f"{PE} › absolut"), ("verl", f"{PE} › verletzt")], [
    *tafel("egmr", "EGMR: Verbot der Folter"),
    z("Große Kammer, Urt. v. 1.6.2010 – Nr. 22978/05", 110, 180, "egmr", "Bold", 34),
    *wA3,
    *okz("unmenschliche Behandlung", wA3_y + 30, "ub", "Bold", 34),
    *neinz("aber noch keine Folter", wA3_y + 85, beim("ub", "keine"), "Bold", 34, kreuz=beim("ub", "keine")),
    zit("EGMR § 108", 600, wA3_y + 93, beim("ub", "keine")),
    blk(110, wA3_y + 160, 1040, 80, GELB, "abs", [("absolut: auch wenn ein Leben auf dem Spiel steht", "ExtraBold", 32, INK)]),
    zit("EGMR §§ 87, 107", 110, wA3_y + 250, "abs"),
    blk(110, wA3_y + 300, 1040, 80, HELLROT, "verl", [("Art. 3 EMRK verletzt", "ExtraBold", 34, INK)]),
    zit("Tenor Nr. 3; §§ 131 f.", 110, wA3_y + 390, "verl"),
    *requisit([("egmr", ("tabler", "building-bank", 130, BLAUHELL), "EGMR", BLAUHELL),
               ("ub", ("tabler", "alert-triangle", 110, GELB), "unmenschlich", HELLROT),
               ("verl", ("tabler", "circle-x", 110, HELLROT), "Art. 3 verletzt", HELLROT)]),
    *stehend("WA", FX, [("egmr", "ruhig"), ("ub", "ernst")]),
])
assert wA3_y + 430 <= 900, wA3_y


# ===========================================================================================================================
# E2 EGMR: Art. 6 EMRK (§§ 165–167, 178–188; Tenor Nr. 4)
# ===========================================================================================================================
def kette(cue, bruch):
    """Rechts: Drohung → Spuren → Urteil; bei bruch springt die Kette (Kreuz zwischen Spuren und Urteil)."""
    els = [pl("Drohung", 1560, 170, cue, fill=HELLROT, size=28, anker="m"),
           pfeil(1560, 220, 1560, 290, cue, breite=8, kopf=22),
           pl("Spuren", 1560, 300, cue, fill=WEISS, size=28, anker="m"),
           pfeil(1560, 350, 1560, 420, cue, breite=8, kopf=22),
           pl("Urteil", 1560, 430, cue, fill=BLAUHELL, size=28, anker="m"),
           nein(1462, 372, bruch, gr=26),
           ficon("tabler", "link-off", 1700, 420, 80, bruch, fuell=WEISS)]
    return rechts_frei(els)


PE6 = "EGMR · Art. 6 EMRK"
folie([("a6", f"{PE6} · faires Verfahren?"), ("regel", f"{PE6} › Aussagen nie verwertbar"),
       ("bear", f"{PE6} › Sachbeweise: Urteil beeinflusst?"), ("kette", f"{PE6} › Kette unterbrochen"),
       ("a6nein", f"{PE6} › nicht verletzt")], [
    *tafel("a6", "Art. 6 EMRK: faires Verfahren?"),
    *neinz("Aussagen nach Verstoß gegen Art. 3: nie verwerten", 180, "regel", "Bold", 33,
           kreuz=beim("regel", "nie")),
    zit("EGMR § 166", 185, 228, "regel"),
    *neinz("Sachbeweise aus Folter: ebenso wenig", 280, beim("regel", "Sachbeweise"), "Bold", 33,
           kreuz=beim("regel", "wenig")),
    zit("EGMR § 167", 185, 328, beim("regel", "Sachbeweise")),
    blk(110, 390, 1040, 130, GELB, "bear", [("Sachbeweise nach unmenschlicher Behandlung:", "ExtraBold", 33, INK),
                                         ("Haben sie das Urteil beeinflusst?", "ExtraBold", 33, INK)]),
    zit("EGMR § 178", 110, 532, "bear"),
    *okz("Urteil beruht auf dem neuen Geständnis:", 590, "kette", "Bold", 33),
    z("Die Kette war unterbrochen.", 185, 636, beim("kette", "Kette"), "Bold", 33),
    zit("EGMR §§ 179 f.", 640, 644, beim("kette", "Kette")),
    blk(110, 700, 1040, 80, GRUEN, "a6nein", [("Art. 6 EMRK nicht verletzt (11 : 6 Stimmen)", "ExtraBold", 33, INK)]),
    zit("Tenor Nr. 4; §§ 187 f.", 110, 790, "a6nein"),
    *kette(beim("bear", "Urteil"), beim("kette", "Kette")),
    *paar("VE", [("a6", "ruhig"), ("kette", "ernst")], "WA", [("a6", "ruhig"), ("a6nein", "reue")]),
])

# ===========================================================================================================================
# F1 Die Polizisten vor Gericht (LG Frankfurt, Urt. v. 20.12.2004, nach EGMR §§ 47–49)
# ===========================================================================================================================
PP = "Die Polizisten"
folie([("pol", f"{PP} · strafbar?"), ("lg04", f"{PP} › Kommissar Leitner: Nötigung"),
       ("lg04b", f"{PP} › Herr Rombach: Verleiten des Untergebenen"), ("n34", f"{PP} › Notstand, § 34 StGB?"),
       ("gef", f"{PP} › § 34: Leben des Kindes retten")], [
    *tafel("pol", "Die Polizisten vor Gericht"),
    z("LG Frankfurt am Main, Urt. v. 20.12.2004", 110, 180, "lg04", "Bold", 34),
    zit("5/27 KLs 7570 Js 203814/03 (4/04), NJW 2005, 692; EGMR § 49", 110, 228, "lg04"),
    *okz("Kommissar Leitner: Nötigung", 290, beim("lg04", "Nötigung"), "Bold", 34),
    *okz("Herr Rombach: Verleiten seines Untergebenen", 350, "lg04b", "Bold", 34),
    z("zur Nötigung", 185, 396, beim("lg04b", "verleitet"), "Bold", 34),
    z("Gerechtfertigt durch Notstand, § 34 StGB?", 110, 480, "n34", "ExtraBold", 36),
    z("Ziel: das Leben des Kindes retten", 185, 550, "gef", "Bold", 34),
    zit("EGMR §§ 47, 95", 185, 598, "gef"),
    *requisit([("pol", ("tabler", "scale", 120, WEISS), "strafbar?", WEISS),
               ("lg04", ("tabler", "gavel", 110, WEISS), "Landgericht", WEISS),
               ("n34", ("tabler", "shield-check", 110, GELB), "§ 34 StGB?", GELB),
               ("gef", ("tabler", "heart-handshake", 110, HELLGRUEN), "retten wollen", HELLGRUEN)]),
    *paar("RO", [("pol", "ernst"), ("gef", "sorge")], "LE", [("pol", "ernst"), ("lg04", "muede")]),
])

# ===========================================================================================================================
# F2 Notstand scheitert an der Menschenwürde (Art. 1 Abs. 1 GG; LG Frankfurt nach EGMR § 48); Verweise 013, 189
# ===========================================================================================================================
wGG, wGG_y = wortlaut(80, 180, 1100, "„(1) Die Würde des Menschen ist unantastbar. …“", "Art. 1 Abs. 1 GG", "mw",
                      marken=[("Würde", beim("mw", "Menschenwürde")), ("unantastbar", beim("mw", "Menschenwürde", ende=True))])
folie([("mw", f"{PP} › Menschenwürde, Art. 1 Abs. 1 GG"), ("abs2", f"{PP} › keine Abwägung, kein Notstand"),
       ("v013", f"{PP} › siehe Folgen 013 und 189")], [
    *tafel("mw", "Notstand? Die Menschenwürde"),
    *wGG,
    z("Die Drohung verletzte die Menschenwürde.", 110, wGG_y + 40, "mw", "Bold", 34),
    *neinz("absolut geschützt: keine Abwägung,", wGG_y + 120, "abs2", "Bold", 34, kreuz=beim("abs2", "keinen")),
    z("also auch kein Notstand", 185, wGG_y + 166, beim("abs2", "keinen"), "Bold", 34),
    zit("LG Frankfurt, 20.12.2004 (EGMR § 48)", 185, wGG_y + 214, beim("abs2", "keinen")),
    blk(110, wGG_y + 280, 1040, 80, BLAUHELL, "v013", [("Mehr dazu: Folge 013 · Luftsicherheitsgesetz", "ExtraBold", 33, INK)]),
    blk(110, wGG_y + 380, 1040, 80, BLAUHELL, "v189", [("Schema: Folge 189 · Notstand, § 34 StGB", "ExtraBold", 33, INK)]),
    *requisit([("mw", ("tabler", "user-shield", 120, LILAHELL), "Menschenwürde", LILA),
               ("abs2", ("tabler", "shield-x", 110, HELLROT), "kein Notstand", HELLROT)]),
    *paar("RO", [("mw", "feierlich")], "LE", [("mw", "feierlich")]),
])
assert wGG_y + 470 <= 900, wGG_y

# ===========================================================================================================================
# F3 Die Sanktion (EGMR §§ 49 f., 124; § 59 StGB)
# ===========================================================================================================================
folie([("strafe", f"{PP} › Verwarnung mit Strafvorbehalt"), ("tagess", f"{PP} › Geldstrafen nur vorbehalten"),
       ("mild", f"{PP} › EGMR: zu mild")], [
    *tafel("strafe", "Die Sanktion"),
    blk(110, 180, 1040, 80, GELB, "strafe", [("Verwarnung mit Strafvorbehalt, § 59 StGB", "ExtraBold", 34, INK)]),
    zit("LG Frankfurt, 20.12.2004 (EGMR § 49)", 110, 270, "strafe"),
    z("Geldstrafen nur zu zahlen, wenn sie in der", 110, 340, "tagess", "Bold", 34),
    z("Bewährungszeit erneut straffällig werden", 110, 388, "tagess", "Bold", 34),
    blk(110, 470, 1040, 80, HELLROT, "mild", [("EGMR: zu mild für einen Verstoß gegen Art. 3", "ExtraBold", 33, INK)]),
    zit("EGMR § 124", 110, 560, "mild"),
    *requisit([("strafe", ("tabler", "hourglass", 110, GELB), "Strafvorbehalt", GELB),
               ("mild", ("tabler", "building-bank", 120, BLAUHELL), "EGMR: zu mild", HELLROT)]),
    *paar("RO", [("strafe", "ernst"), ("mild", "muede")], "LE", [("strafe", "ernst")]),
])

# ===========================================================================================================================
# G Klausurtipp mit Prüfungsaufbau (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · drei Fragen trennen"), ("t1", "Klausurtipp › I. Aussage verwertbar?"),
       ("t2", "Klausurtipp › II. Folgebeweise verwertbar?"), ("t3", "Klausurtipp › III. Beamte strafbar?")], [
    *tafel("tipp", "Klausurtipp: drei Fragen trennen", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("I. Ist die Aussage verwertbar?", 200, 200, "t1", "ExtraBold", 36),
    z("§ 136a Abs. 3 S. 2 StPO, Fortwirkung,", 240, 254, beim("t1", "Paragraf"), size=34),
    z("qualifizierte Belehrung", 240, 302, beim("t1", "qualifizierter"), size=34),
    linienzug([(130, 370), (1130, 370)], "t2", breite=3),
    z("II. Sind die Folgebeweise verwertbar?", 200, 395, "t2", "ExtraBold", 36),
    z("grundsätzlich keine Fernwirkung;", 240, 449, beim("t2", "Grundsätzlich"), size=34),
    z("Art. 6 EMRK: Hat der Beweis das Urteil beeinflusst?", 240, 497, "t2b", size=33),
    linienzug([(130, 565), (1130, 565)], "t3", breite=3),
    z("III. Sind die Beamten strafbar?", 200, 590, "t3", "ExtraBold", 36),
    z("§ 34 StGB scheitert an der Menschenwürde", 240, 644, beim("t3", "Notstand"), size=34),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "merke"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# H Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Eine Aussage unter verbotener", 0)], [("Drohung ist stets ", 0), ("unverwertbar", "a"), (".", 0)]],
                750, 280, 44, "merke", {"a": beim("merke", "unverwertbar")}),
    *markertext([[("Für die Spuren daraus gibt es grund-", 0)], [("sätzlich ", 0), ("keine Fernwirkung", "b"), (".", 0)]],
                750, 460, 44, "m2", {"b": beim("m2", "keine")}),
    *markertext([[("Die Menschenwürde kennt ", 0), ("keine", "c")], [("Ausnahme", "d"), (", auch nicht zur Rettung.", 0)]],
                750, 640, 44, "m3", {"c": beim("m3", "keine"), "d": beim("m3", "Ausnahme")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
