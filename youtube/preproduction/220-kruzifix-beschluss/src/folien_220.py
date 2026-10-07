"""Folge 220 · Kruzifix-Beschluss: Muss das Kreuz aus dem Klassenzimmer? – Serienstandard Open Peeps (Katzenkönig).
Fiktiver Fall nach dem Muster von BVerfGE 93, 1: Familie Rohde bittet Schulleiter Kampe, das nach § 13 Abs. 1 S. 3 VSO
angebrachte Kreuz über der Tafel der 2a abzuhängen. Danach Art. 4 Abs. 1 GG (Wortlautkarte), Schutzbereich (negative
Glaubensfreiheit, Elternrecht), Eingriff (Schulpflicht, „unter dem Kreuz“, Glaubenssymbol), Rechtfertigung (vorbehaltlos,
Art. 7 Abs. 1 GG als Wortlautkarte, praktische Konkordanz, positive Glaubensfreiheit, kein Mehrheitsprinzip), Ergebnis
samt abweichender Meinung, Ergebnis im Fall, Folgen in Bayern (Art. 7 Abs. 3 BayEUG 1995 als Wortlautkarte, BVerwG
6 C 18.98, Kreuzerlass/BVerwG 10 C 5.22), Klausurtipp und Merksatz mit Lexi.
DARSTELLUNG: respektvoll gegenüber allen Bekenntnissen; das Kreuz als schlichtes Symbol (Tabler „cross“, holzfarben,
ohne Korpus); Eltern höflich, Schulleiter sachlich; reale Beschwerdeführer weder gezeigt noch benannt.
Szenen laut ../SZENENPLAN.md. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/feld/requisit/
stehend/paar/raum/tisch als eigene Kopie aus Folge 217 (gemeinsame Dateien unverändert; stehend() mit Schild für den
Sohn); neu: wandkreuz(), Kinderhöhe 58 %.
Handlungsgeräusch: Kreide an der Tafel (Freesound CC0 232420); ../geraeusche_herkunft.json.
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut GG nach gesetze-im-internet.de, Abruf 07.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_220/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_220/" in n:
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
NAME = {"RO": "Herr Rohde", "FR": "Frau Rohde", "KA": "Herr Kampe", "SO": "Sohn der Rohdes"}
NFARBE = {"RO": TUERKIS_, "FR": HELLROT, "KA": BLAU, "SO": HELLGRUEN}
KIND = {"K1", "K2", "SO"}              # Kinder der 2a, kleiner skaliert; nur der Sohn mit Schild
KF = 0.58                              # Kinderhöhe (7 Jahre) relativ zur Erwachsenenhöhe
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
    if k in KIND:                                   # Kinder: kleiner; der Sohn mit Schild „Sohn der Rohdes“
        els = fig(k, x, FB, round(FR * KF), folge, bis=bis)
        if k == "SO":
            els.append(bis_(pl(NAME[k], x, FB + 22, folge[0][0], fill=HELLGRUEN, size=26, anker="m", d=0.1), bis))
        return rechts_frei(els, 1200)
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





# --- eigene Szenenbausteine Folge 220 ---------------------------------------------------------------------------------------
TAFELGRUEN = (58, 98, 78, 255)
KREIDE = (244, 244, 236, 255)
KH = round(FH * KF)                          # Kinder in der Fallszene (7 Jahre)
KREUZ = ("tabler", "cross")                  # schlichtes lateinisches Kreuz ohne Korpus (Tabler, MIT), Holzfarbe


def schultafel(x, y, w, h, cue):
    """Schultafel (Tafelgrün) mit Holzrahmen und Ablage, programmatisch."""
    return [feld(x - 14, y - 14, w + 28, h + 28, cue, fill=HOLZ, rand=5, rund=8, name="tafelrahmen"),
            feld(x, y, w, h, cue, fill=TAFELGRUEN, rand=4, rund=4, name="schultafel"),
            feld(x + 40, y + h + 14, w - 80, 16, cue, fill=HOLZ, rand=4, rund=3, name="tafelablage")]


def kreide(text, x, y, cue, size=54, **k):
    """Kreideschrift auf der Schultafel."""
    return zeile(glyphen(text), x, y, cue, "Bold", size, farbe=KREIDE, **k)


def wandkreuz(cx, unten, cue, breite=104, bis=None):
    """Das Kreuz über der Tafel: Tabler-Icon „cross“, holzfarben gefüllt, schlicht (kein Korpus)."""
    return hart(ficon(*KREUZ, cx, unten, breite, cue, fuell=HOLZ, bis=bis))


def pulte(x0, x1, cue, oben=745, bis=None):
    """Durchgehende Pultfront vor den Kindern (Holz), verdeckt die Beine bewusst."""
    return [feld(x0, oben, x1 - x0, BODEN - oben, cue, fill=HOLZ, rand=5, rund=8, bis=bis, name="pulte")]


def fall_ns(k, x, cue, **kw):
    if k == "SO":
        return pl(NAME[k], x, BODEN + 22, cue, fill=HELLGRUEN, size=26, anker="m", **kw)
    return ns(NAME[k], x, BODEN, cue, NFARBE[k], **kw)


NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
TX, TY, TW, TH = 120, 300, 640, 300           # Schultafel in den Klassenzimmerszenen
KRX = TX + TW // 2                            # Kreuz mittig über der Tafel

# ===========================================================================================================================
# A1 Fall: Klassenzimmer der 2a, das Kreuz über der Tafel (fiktiv, Muster BVerfGE 93, 1 Rn. 2–5)
# ===========================================================================================================================
KX1 = (1120, 1420, 1720)                      # K1, Sohn, K2
folie([(NULL, "Fall · Bayern, Anfang der 1990er Jahre"), ("kreuz", "Fall · Das Kreuz über der Tafel")], [
    boden(NULL),
    *schultafel(TX, TY, TW, TH, NULL),
    wandkreuz(KRX, TY - 26, NULL),
    hart(pl("Bayern, Anfang der 1990er · staatliche Grundschule", 70, 40, NULL, fill=ORANGE, size=32)),
    hart(kreide("Klasse 2a", 180, 340, NULL, size=46)),
    szene(kreide("3 + 4 = 7", 180, 440, beim("fall", "Grundschule")), "220kreide*", 0.8, 0.05),
    pl("Volksschulordnung: „In jedem Klassenzimmer", 820, 300, "kreuz", fill=WEISS, size=28),
    pl("ist ein Kreuz anzubringen.“", 820, 360, "kreuz", fill=WEISS, size=28),
    zit("§ 13 Abs. 1 S. 3 VSO (BVerfGE 93, 1 Rn. 2 f.)", 830, 424, "kreuz", rechts=1880),
    *fig("K1", KX1[0], BODEN, KH, [(NULL, "froh"), ("kreuz", "ruhig")], erst="cut"),
    *fig("SO", KX1[1], BODEN, KH, [(NULL, "ruhig"), (beim("kreuz", "Klassenzimmer"), "froh")], erst="cut"),
    *fig("K2", KX1[2], BODEN, KH, [(NULL, "ruhig"), ("kreuz", "froh")], erst="cut"),
    *pulte(960, 1860, NULL),
    hart(pl("Klasse 2a", 1410, 795, NULL, fill=WEISS, size=28, anker="m")),
])

# ===========================================================================================================================
# A2 Fall: Büro der Schulleitung – die Bitte der Eltern (fiktiv)
# ===========================================================================================================================
FRX2, ROX2, SOX2, KAX2 = 380, 620, 900, 1560
folie([("eltern", "Fall · Familie Rohde"), ("gespr", "Fall · Gespräch mit Schulleiter Kampe"),
       ("ro1", "Fall · Die Bitte der Eltern"), ("ka1", "Fall · Die Antwort der Schule")], [
    *raum("eltern", tuer_x=120),
    hart(pl("Büro der Schulleitung", 70, 40, "eltern", fill=ORANGE, size=32)),
    bis_(pl("gehören keiner Kirche an,", 70, 120, beim("eltern", "Kirche"), fill=WEISS, size=30), "ro1"),
    bis_(pl("erziehen ihren Sohn ohne religiöses Bekenntnis", 70, 184, beim("eltern", "erziehen"), fill=WEISS, size=30), "ro1"),
    *fig("FR", FRX2, BODEN, FH, [("eltern", "ruhig_r"), ("ro1", "sorge_r"), ("ka1", "ruhig_r")], erst="cut"),
    hart(fall_ns("FR", FRX2, "eltern")),
    *fig("RO", ROX2, BODEN, FH, [("eltern", "ruhig_r"), ("gespr", "sorge_r")], bis="ro1", erst="cut"),
    *redet("RO_redet_r", ROX2, BODEN, FH, "ro1", "ka1"),
    *fig("RO", ROX2, BODEN, FH, [("ka1", "denkt_r")], erst="cut"),
    hart(fall_ns("RO", ROX2, "eltern")),
    *fig("SO", SOX2, BODEN, KH, [("eltern", "ruhig_r"), ("ka1", "sorge_r")], erst="cut"),
    hart(fall_ns("SO", SOX2, "eltern")),
    *tisch(1320, 1800, "eltern"),
    *fig("KA", KAX2, BODEN, FH, [("gespr", "ruhig")], bis="ka1", erst="pop"),
    *redet("KA_redet", KAX2, BODEN, FH, "ka1", "frage"),
    fall_ns("KA", KAX2, "gespr", d=0.1),
    blase("sprech", 1000, 230, "ro1", 860, 225, inhalt=["Unser Sohn soll nicht jeden Tag unter dem",
                                                     "Kreuz lernen müssen. Bitte hängen Sie es ab."],
          textsize=30, figur=("RO_redet_r", ROX2, BODEN, FH), bis="ka1"),
    blase("sprech", 1000, 230, "ka1", 1180, 225, inhalt=["Das Kreuz schreibt die Schulordnung vor. Und es",
                                                      "steht doch für unsere abendländische Kultur."],
          textsize=30, figur=("KA_redet", KAX2, BODEN, FH)),
])

# ===========================================================================================================================
# A3 Die Frage; die Leitentscheidung
# ===========================================================================================================================
folie([("frage", "Die Frage · Muss das Kreuz abgehängt werden?"), ("echt", "Die Frage · Kruzifix-Beschluss, BVerfGE 93, 1")], [
    *tafel("frage", "Die Frage"),
    z("Muss das Kreuz aus dem Klassenzimmer?", 110, 200, "frage", "ExtraBold", 40),
    blk(110, 300, 1040, 170, GELB, "echt", [("BVerfGE 93, 1 · Kruzifix-Beschluss", "ExtraBold", 36, INK),
                                         ("Erster Senat, Beschl. v. 16.5.1995", "Bold", 32, INK),
                                         ("1 BvR 1087/91", "Bold", 32, INK)]),
    *requisit([("frage", (*KREUZ, 90, HOLZ), "Kreuz im Klassenzimmer", WEISS),
               ("echt", ("tabler", "building-bank", 130, BLAUHELL), "Bundesverfassungsgericht", BLAUHELL)]),
    *paar("RO", [("frage", "sorge"), ("echt", "ruhig")], "KA", [("frage", "ernst"), ("echt", "ruhig")]),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_220(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=31, zeilenabstand=1.28)
        els += e; y += 14
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=30))
    folie([(cue, "Sachverhalt")], els)


SV = ["Bayern, Anfang der 1990er Jahre: Nach § 13 Abs. 1 S. 3 der bayerischen Volksschulordnung (VSO) gilt: „In jedem "
      "Klassenzimmer ist ein Kreuz anzubringen.“ Im Klassenzimmer der 2a einer staatlichen Grundschule hängt deshalb über "
      "der Tafel ein Kreuz. Die Grundschule ist keine Bekenntnisschule.",
      "Herr und Frau Rohde gehören keiner Kirche an und erziehen ihren schulpflichtigen Sohn, der die 2a besucht, ohne "
      "religiöses Bekenntnis. Sie bitten Schulleiter Kampe, das Kreuz abzuhängen. Er lehnt ab: Die Schulordnung schreibe "
      "das Kreuz vor, und es stehe für die abendländische Kultur."]
assert not any("erfunden" in a or "fiktiv" in a.lower() for a in SV)
sachverhalt_220("sv", SV, "Verletzt das Kreuz die Rohdes und ihren Sohn in Art. 4 Abs. 1 GG?")

# ===========================================================================================================================
# C1 Art. 4 Abs. 1 GG im Wortlaut
# ===========================================================================================================================
w4, w4_y = wortlaut(80, 190, 1100,
                    "„(1) Die Freiheit des Glaubens, des Gewissens und die Freiheit des religiösen und weltanschaulichen "
                    "Bekenntnisses sind unverletzlich.“", "Art. 4 Abs. 1 GG", "art4", size=38,
                    marken=[("Glaubens", beim("wl4", "Glaubens")), ("Bekenntnisses", beim("wl4", "Bekenntnisses"))])
folie([("art4", "Art. 4 Abs. 1 GG · Maßstab"), ("wl4", "Art. 4 Abs. 1 GG · Wortlaut")], [
    *tafel("art4", "Art. 4 Abs. 1 GG: Glaubensfreiheit"),
    *w4,
    *requisit([("art4", ("tabler", "book", 110, WEISS), "Art. 4 Abs. 1 GG", WEISS),
               (beim("wl4", "Bekenntnisses"), ("tabler", "heart", 100, LILAHELL), "Bekenntnis", LILAHELL)]),
    *stehend("RO", FX, [("art4", "ruhig"), (beim("wl4", "Bekenntnisses"), "froh")]),
])
assert w4_y <= 900, w4_y

# ===========================================================================================================================
# C2 I. Schutzbereich: positive und negative Glaubensfreiheit, Elternrecht (BVerfGE 93, 1 Rn. 34, 36)
# ===========================================================================================================================
PS1 = "I. Schutzbereich"
folie([("pos", f"{PS1} › positive Glaubensfreiheit"), ("neg", f"{PS1} › negative Glaubensfreiheit"),
       ("alltag", f"{PS1} › kein Schutz im Alltag"), ("lage", f"{PS1} › vom Staat geschaffene Lage"),
       ("a6", f"{PS1} › Eltern: Art. 4 Abs. 1 i. V. m. Art. 6 Abs. 2 GG")], [
    *tafel("pos", "I. Schutzbereich"),
    z("positiv: einen Glauben haben und nach ihm leben", 110, 180, "pos", "Bold", 34),
    z("negativ: Handlungen und Symbolen eines nicht", 110, 240, "neg", "Bold", 34),
    z("geteilten Glaubens fernbleiben", 145, 288, "neg", size=34),
    zit("BVerfGE 93, 1 Rn. 34", 145, 336, "neg"),
    *neinz("kein Schutz vor fremden Symbolen im Alltag", 400, "alltag", "Bold", 34, kreuz=beim("alltag", "nicht")),
    *okz("aber: vom Staat geschaffene Lage", 460, "lage", "Bold", 34),
    z("ohne Ausweichmöglichkeit", 185, 508, beim("lage", "ohne"), size=34),
    blk(110, 580, 1040, 170, BLAUHELL, "a6", [("Eltern: Art. 4 Abs. 1 i. V. m. Art. 6 Abs. 2 GG", "ExtraBold", 33, INK),
                                           ("ihr Kind von Glaubensüberzeugungen fernhalten,", "Bold", 32, INK),
                                           ("die ihnen falsch erscheinen", "Bold", 32, INK)]),
    zit("Rn. 36", 110, 760, "a6"),
    *requisit([("pos", ("tabler", "heart", 100, LILAHELL), "einen Glauben leben", LILAHELL),
               ("neg", ("tabler", "eye-off", 110, WEISS), "fernbleiben", WEISS),
               ("alltag", ("tabler", "road", 110, WEISS), "Alltag", WEISS),
               ("lage", ("tabler", "school", 130, WEISS), "kein Ausweichen", HELLROT),
               ("a6", ("tabler", "home", 110, WEISS), "Eltern", BLAUHELL)]),
    *paar("FR", [("pos", "ruhig"), ("lage", "sorge"), ("a6", "froh")], "RO", [("pos", "ruhig"), ("neg", "denkt"), ("a6", "froh")]),
])

# ===========================================================================================================================
# D1 II. Eingriff: Schulpflicht, „unter dem Kreuz“ (BVerfGE 93, 1 Rn. 37–39)
# ===========================================================================================================================
PE = "II. Eingriff"
folie([("eingr", f"{PE} › das angeordnete Kreuz"), ("pflicht", f"{PE} › Schulpflicht: kein Ausweichen"),
       ("unter", f"{PE} › „unter dem Kreuz“ lernen"), ("strasse", f"{PE} › anders: Kreuz im Straßenbild"),
       ("korpus", f"{PE} › mit und ohne Korpus")], [
    *tafel("eingr", "II. Eingriff"),
    z("Kreuz auf staatliche Anordnung?", 110, 180, "eingr", "Bold", 34),
    zit("§ 13 Abs. 1 S. 3 VSO; Rn. 37 f.", 110, 228, "eingr"),
    *okz("Eingriff: ja", 290, beim("pflicht", "Ja"), "ExtraBold", 36),
    z("Schulpflicht: von Staats wegen, ohne Ausweichen", 185, 342, beim("pflicht", "Schulpflicht"), size=33),
    blk(110, 410, 1040, 80, GELB, "unter", [("Die Kinder lernen „unter dem Kreuz“.", "ExtraBold", 34, INK)]),
    zit("Rn. 39", 110, 500, "unter"),
    z("anders: ein Kreuz im Straßenbild –", 110, 560, "strasse", "Bold", 34),
    z("flüchtig und nicht vom Staat", 145, 608, beim("strasse", "flüchtig"), size=34),
    zit("Rn. 39", 145, 656, beim("strasse", "flüchtig")),
    z("gilt für Kreuze mit und ohne Korpus", 110, 716, "korpus", "Bold", 34),
    zit("Rn. 38", 110, 764, "korpus"),
    *requisit([("eingr", (*KREUZ, 90, HOLZ), "staatlich angeordnet", WEISS),
               ("pflicht", ("tabler", "school", 130, WEISS), "Schulpflicht", HELLROT),
               ("unter", (*KREUZ, 90, HOLZ), "unter dem Kreuz", GELB),
               ("strasse", ("tabler", "road", 110, WEISS), "Straßenbild", WEISS),
               ("korpus", (*KREUZ, 90, HOLZ), "mit und ohne Korpus", WEISS)]),
    *stehend("SO", X1, [("eingr", "ruhig"), ("unter", "sorge"), ("strasse", "ruhig")]),
    *stehend("K1", X2, [("eingr", "ruhig"), ("korpus", "froh")]),
])

# ===========================================================================================================================
# D2 II. Eingriff: Was bedeutet das Kreuz? (BVerfGE 93, 1 Rn. 42–46)
# ===========================================================================================================================
folie([("kultur", f"{PE} › bloß Kultur?"), ("symbol", f"{PE} › Glaubenssymbol des Christentums"),
       ("appell", f"{PE} › appellativer Charakter")], [
    *tafel("kultur", "II. Eingriff: Was bedeutet das Kreuz?"),
    z("Bloß ein Zeichen abendländischer Kultur?", 110, 180, "kultur", "Bold", 34),
    *neinz("nur Kultur: nein", 240, beim("symbol", "Nein"), "Bold", 34),
    blk(110, 310, 1040, 130, LILAHELL, beim("symbol", "Glaubenssymbol"), [("Glaubenssymbol des Christentums", "ExtraBold", 34, INK),
                                                                       ("schlechthin", "ExtraBold", 34, INK)]),
    zit("Rn. 42–44", 110, 450, beim("symbol", "Glaubenssymbol")),
    *okz("im Klassenzimmer: appellativer Charakter,", 520, "appell", "Bold", 34),
    z("gegenüber leicht beeinflussbaren Kindern", 185, 568, beim("appell", "gegenüber"), size=34),
    zit("Rn. 46", 185, 616, beim("appell", "gegenüber")),
    *requisit([("kultur", ("tabler", "building-community", 130, WEISS), "Kultur?", WEISS),
               (beim("symbol", "Glaubenssymbol"), (*KREUZ, 90, HOLZ), "Glaubenssymbol", LILAHELL),
               ("appell", ("tabler", "school", 130, WEISS), "Klassenzimmer", WEISS)]),
    *stehend("KA", FX, [("kultur", "ernst"), (beim("symbol", "Glaubenssymbol"), "denkt")]),
])

# ===========================================================================================================================
# E1 III. Rechtfertigung: vorbehaltlos, Art. 7 Abs. 1 GG (BVerfGE 93, 1 Rn. 48–50)
# ===========================================================================================================================
w7, w7_y = wortlaut(80, 320, 1100, "„(1) Das gesamte Schulwesen steht unter der Aufsicht des Staates.“",
                    "Art. 7 Abs. 1 GG", "a7", marken=[("Aufsicht", beim("a7", "Aufsicht"))])
PR = "III. Rechtfertigung"
folie([("vorb", f"{PR} › vorbehaltlos"), ("a7", f"{PR} › Art. 7 Abs. 1 GG"),
       ("auftrag", f"{PR} › staatlicher Erziehungsauftrag")], [
    *tafel("vorb", "III. Rechtfertigung"),
    *neinz("Gesetzesvorbehalt: keiner (vorbehaltlos)", 180, "vorb", "Bold", 34, kreuz=beim("vorb", "vorbehaltlos")),
    z("Grenzen nur aus der Verfassung selbst", 185, 232, beim("vorb", "Grenzen"), size=34),
    zit("Rn. 48", 900, 240, beim("vorb", "Grenzen")),
    *w7,
    blk(110, w7_y + 30, 1040, 80, BLAUHELL, "auftrag", [("eigener staatlicher Erziehungsauftrag", "ExtraBold", 34, INK)]),
    zit("Rn. 50", 110, w7_y + 120, "auftrag"),
    *requisit([("vorb", ("tabler", "book", 110, WEISS), "Art. 4 GG: vorbehaltlos", WEISS),
               ("a7", ("tabler", "building-bank", 120, WEISS), "Schulaufsicht", BLAUHELL),
               ("auftrag", ("tabler", "school", 130, WEISS), "Erziehungsauftrag", BLAUHELL)]),
    *stehend("KA", FX, [("vorb", "ruhig"), ("a7", "ernst"), ("auftrag", "ruhig")]),
])
assert w7_y + 160 <= 900, w7_y

# ===========================================================================================================================
# E2 Praktische Konkordanz (BVerfGE 93, 1 Rn. 51–56)
# ===========================================================================================================================
folie([("konk", f"{PR} › praktische Konkordanz"), ("bezug", f"{PR} › religiöse Bezüge möglich"),
       ("minimum", f"{PR} › nur das Minimum an Zwang"), ("grenze", f"{PR} › Kreuz: Grenze überschritten")], [
    *tafel("konk", "Praktische Konkordanz"),
    blk(110, 180, 1040, 130, GELB, "konk", [("möglichst schonender Ausgleich,", "ExtraBold", 34, INK),
                                         ("keine Position setzt sich maximal durch", "ExtraBold", 34, INK)]),
    zit("Rn. 51", 110, 320, "konk"),
    *okz("religiöse Bezüge: nicht völlig ausgeschlossen", 390, "bezug", "Bold", 34),
    zit("Rn. 52", 185, 438, "bezug"),
    z("aber: nur das unerlässliche Minimum an Zwang,", 110, 500, "minimum", "Bold", 34),
    z("keine Verbindlichkeit christlicher Glaubensinhalte", 145, 548, beim("minimum", "christliche"), size=33),
    zit("Rn. 55", 145, 596, beim("minimum", "christliche")),
    *neinz("Kreuz in jedem Klassenzimmer: Grenze überschritten", 660, "grenze", "ExtraBold", 33),
    zit("Rn. 56", 185, 708, "grenze"),
    *requisit([("konk", ("tabler", "scale", 120, WEISS), "Ausgleich", GELB),
               ("bezug", ("tabler", "book", 110, WEISS), "religiöse Bezüge", WEISS),
               ("minimum", ("tabler", "hand-stop", 110, WEISS), "Minimum an Zwang", WEISS),
               ("grenze", (*KREUZ, 90, HOLZ), "Grenze überschritten", HELLROT)]),
    *paar("RO", [("konk", "ruhig"), ("grenze", "froh")], "KA", [("konk", "ruhig"), ("grenze", "denkt")]),
])

# ===========================================================================================================================
# E3 Positive Glaubensfreiheit der anderen, Mehrheitsprinzip (BVerfGE 93, 1 Rn. 57)
# ===========================================================================================================================
folie([("posit", f"{PR} › positive Glaubensfreiheit der anderen"), ("allen", f"{PR} › steht allen zu"),
       ("mehr", f"{PR} › Mehrheitsprinzip trägt nicht"), ("frei", f"{PR} › Freiwilligkeit"),
       ("wand", f"{PR} › dem Kreuz kann niemand ausweichen")], [
    *tafel("posit", "Und die Glaubensfreiheit der anderen?"),
    z("positive Glaubensfreiheit christlicher Familien?", 110, 180, "posit", "Bold", 34),
    z("steht allen zu, nicht nur Christen", 145, 230, "allen", size=34),
    *neinz("Mehrheitsprinzip: trägt nicht", 300, "mehr", "Bold", 34, kreuz=beim("mehr", "nicht")),
    blk(110, 360, 1040, 80, LILAHELL, beim("mehr", "schützt"), [("Glaubensfreiheit schützt gerade Minderheiten.", "ExtraBold", 33, INK)]),
    zit("Rn. 57", 110, 450, beim("mehr", "schützt")),
    *okz("Religionsunterricht, Schulgebet: freiwillig,", 520, "frei", "Bold", 34),
    z("mit zumutbaren Ausweichmöglichkeiten", 185, 568, "frei", size=34),
    *neinz("Kreuz an der Wand: kein Ausweichen", 640, "wand", "ExtraBold", 34),
    zit("Rn. 57", 185, 688, "wand"),
    *requisit([("posit", ("tabler", "heart", 100, LILAHELL), "positive Glaubensfreiheit", LILAHELL),
               ("mehr", ("tabler", "scale", 120, WEISS), "keine Mehrheitsfrage", HELLROT),
               ("frei", ("tabler", "book", 110, WEISS), "freiwillig", HELLGRUEN),
               ("wand", (*KREUZ, 90, HOLZ), "kein Ausweichen", HELLROT)]),
    *stehend("K1", X1, [("posit", "froh"), ("mehr", "ruhig")]),
    *stehend("K2", X2, [("posit", "ruhig"), ("frei", "froh")]),
])

# ===========================================================================================================================
# F1 Ergebnis: BVerfGE 93, 1 (Leitsätze, Tenor; abweichende Meinung Rn. 60, 73 f., 87)
# ===========================================================================================================================
folie([("erg", "Ergebnis · Verstoß gegen Art. 4 Abs. 1 GG"), ("nichtig", "Ergebnis · § 13 Abs. 1 S. 3 VSO nichtig"),
       ("abw", "Ergebnis · abweichende Meinung")], [
    *tafel("erg", "Ergebnis: BVerfGE 93, 1"),
    zit("Erster Senat, Beschl. v. 16.5.1995 – 1 BvR 1087/91", 110, 176, "erg"),
    blk(110, 226, 1040, 170, HELLROT, "erg", [("Kreuz im Unterrichtsraum einer staatlichen", "ExtraBold", 33, INK),
                                           ("Pflichtschule, die keine Bekenntnisschule ist:", "ExtraBold", 33, INK),
                                           ("Verstoß gegen Art. 4 Abs. 1 GG", "ExtraBold", 33, INK)]),
    zit("Leitsatz 1; Rn. 56", 110, 406, "erg"),
    z("§ 13 Abs. 1 S. 3 VSO: nichtig", 110, 466, "nichtig", "ExtraBold", 36),
    zit("Leitsatz 2; Tenor", 700, 476, "nichtig"),
    blk(110, 550, 1040, 170, ZITAT, "abw", [("Abweichende Meinung (3 von 8 Richtern):", "ExtraBold", 32, INK),
                                         ("Kreuz steht für die Werte der christlichen", "Regular", 32, INK),
                                         ("Gemeinschaftsschule; Toleranzgebot: hinnehmen", "Regular", 32, INK)]),
    zit("Seidl, Söllner, Haas – Rn. 60, 73 f., 87", 110, 730, "abw"),
    *requisit([("erg", ("tabler", "building-bank", 130, BLAUHELL), "BVerfG 1995", BLAUHELL),
               ("nichtig", ("tabler", "circle-x", 110, HELLROT), "nichtig", HELLROT),
               ("abw", ("tabler", "message-circle", 110, WEISS), "abweichende Meinung", WEISS)]),
    *paar("FR", [("erg", "froh")], "RO", [("erg", "froh"), ("abw", "ruhig")]),
])

# ===========================================================================================================================
# F2 Ergebnis im Fall: zurück im Klassenzimmer, das Kreuz kommt ab
# ===========================================================================================================================
KAX4, ROX4, SOX4, FRX4 = 880, 1210, 1470, 1730
folie([("ka2", "Ergebnis im Fall · Das Kreuz kommt ab")], [
    boden("ka2"),
    hart(pl("Zurück in der Klasse 2a", 70, 40, "ka2", fill=ORANGE, size=32)),
    *schultafel(TX, TY, TW, TH, "ka2"),
    wandkreuz(KRX, TY - 26, "ka2", bis=beim("ka2", "Rohde")),
    hart(kreide("Klasse 2a", 180, 340, "ka2", size=46)),
    hart(kreide("3 + 4 = 7", 180, 440, "ka2")),
    *redet("KA_redet2_r", KAX4, BODEN, FH, "ka2", "bayern"),
    hart(fall_ns("KA", KAX4, "ka2")),
    *fig("RO", ROX4, BODEN, FH, [("ka2", "froh")], erst="cut"),
    hart(fall_ns("RO", ROX4, "ka2")),
    *fig("SO", SOX4, BODEN, KH, [("ka2", "froh")], erst="cut"),
    hart(fall_ns("SO", SOX4, "ka2")),
    *fig("FR", FRX4, BODEN, FH, [("ka2", "froh")], erst="cut"),
    hart(fall_ns("FR", FRX4, "ka2")),
    blase("sprech", 1040, 180, "ka2", 1240, 260, inhalt=["Dann nehmen wir das Kreuz in der Klasse",
                                                      "Ihres Sohnes ab, Herr Rohde."],
          textsize=32, figur=("KA_redet2_r", KAX4, BODEN, FH)),
])

# ===========================================================================================================================
# G1 Bayern: Widerspruchslösung (Art. 7 Abs. 3 BayEUG i. d. F. v. 23.12.1995, Wortlaut nach BayVerfGH Vf. 6-VII-96)
# ===========================================================================================================================
wby, wby_y = wortlaut(80, 350, 1100,
                      "„Wird der Anbringung des Kreuzes aus ernsthaften und einsehbaren Gründen des Glaubens oder der "
                      "Weltanschauung durch die Erziehungsberechtigten widersprochen, versucht der Schulleiter eine "
                      "gütliche Einigung. …“", "Art. 7 Abs. 3 S. 3 BayEUG (1995)", "wid", size=30,
                      marken=[("einsehbaren", beim("wid", "einsehbaren")), ("Einigung", beim("wid", "Einigung"))])
PB = "Folgen in Bayern"
folie([("bayern", f"{PB} · Widerspruchslösung"), ("haengt", f"{PB} › das Kreuz hängt weiter"),
       ("wid", f"{PB} › Widerspruch der Eltern")], [
    *tafel("bayern", "Bayern: die Widerspruchslösung"),
    z("Gesetz vom 23.12.1995: Art. 7 Abs. 3 BayEUG", 110, 180, "bayern", "Bold", 34),
    zit("heute Art. 7 Abs. 4 BayEUG", 110, 228, "bayern"),
    z("Das Kreuz hängt weiter (Satz 1).", 110, 288, "haengt", "Bold", 34),
    *wby,
    zit("Wortlaut nach BayVerfGH, Entsch. v. 1.8.1997 – Vf. 6-VII-96 u. a.", 110, wby_y + 14, "wid"),
    *requisit([("bayern", ("tabler", "map-2", 110, WEISS), "Bayern 1995", WEISS),
               ("haengt", (*KREUZ, 90, HOLZ), "Kreuz bleibt", WEISS),
               ("wid", ("tabler", "message-circle", 110, WEISS), "Widerspruch", GELB)]),
    *stehend("KA", FX, [("bayern", "ruhig"), ("wid", "denkt")]),
])
assert wby_y + 60 <= 900, wby_y

# ===========================================================================================================================
# G2 Folgefälle: BVerwG 6 C 18.98 (1999); Kreuzerlass, BVerwG 10 C 5.22 (2023)
# ===========================================================================================================================
folie([("bverwg", f"{PB} › BVerwG 1999: Widersprechende setzen sich durch"), ("erlass", f"{PB} › Kreuzerlass 2018"),
       ("flucht", f"{PB} › Behörden: Begegnung nur flüchtig")], [
    *tafel("bverwg", "Folgefälle"),
    zit("BVerwG, Urt. v. 21.4.1999 – 6 C 18.98 (BVerwGE 109, 40)", 110, 176, "bverwg"),
    *okz("keine Einigung, keine zumutbare Alternative:", 236, beim("bverwg", "Gelingt"), "Bold", 34),
    z("Der Widersprechende setzt sich durch.", 185, 284, beim("bverwg", "durchsetzen"), "ExtraBold", 34),
    linienzug([(110, 360), (1150, 360)], "erlass", breite=3),
    z("Kreuzerlass 2018: Kreuz im Eingangsbereich", 110, 386, "erlass", "Bold", 34),
    z("bayerischer Behörden (§ 28 AGO)", 145, 434, "erlass", size=34),
    *neinz("Pflicht zur Entfernung: nein", 500, beim("erlass", "nicht"), "Bold", 34),
    zit("BVerwG, Urt. v. 19.12.2023 – 10 C 5.22", 185, 548, beim("erlass", "nicht")),
    z("Kläger: Weltanschauungsgemeinschaften", 110, 610, "flucht", "Bold", 34),
    z("Begegnung im Eingangsbereich: nur flüchtig", 110, 660, beim("flucht", "flüchtig"), size=34),
    *requisit([("bverwg", ("tabler", "building-bank", 130, BLAUHELL), "BVerwG 1999", BLAUHELL),
               ("erlass", ("tabler", "building", 120, WEISS), "Behörde", WEISS),
               ("flucht", ("tabler", "door-enter", 110, WEISS), "Eingangsbereich", WEISS)]),
    *paar("FR", [("bverwg", "froh"), ("erlass", "ruhig")], "RO", [("bverwg", "froh"), ("erlass", "denkt")]),
])

# ===========================================================================================================================
# H Klausurtipp mit Prüfungsaufbau (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Art. 4 GG in drei Schritten"), ("t1", "Klausurtipp › I. Schutzbereich"),
       ("t2", "Klausurtipp › II. Eingriff"), ("t3", "Klausurtipp › III. Rechtfertigung"),
       ("t4", "Klausurtipp › Kopftuch und Kreuz abgrenzen"), ("fehler", "Klausurtipp › nie mit der Mehrheit argumentieren")], [
    *tafel("tipp", "Klausurtipp: Art. 4 GG in drei Schritten", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("I. Schutzbereich: negative Glaubensfreiheit;", 200, 200, "t1", "ExtraBold", 34),
    z("Eltern: i. V. m. Art. 6 Abs. 2 GG", 240, 250, beim("t1", "Eltern"), size=33),
    z("II. Eingriff: Schulpflicht macht das Kreuz", 200, 316, "t2", "ExtraBold", 34),
    z("unausweichlich; es ist ein religiöses Symbol", 240, 364, beim("t2", "unausweichlich"), size=33),
    z("III. Rechtfertigung: Art. 7 Abs. 1 GG,", 200, 430, "t3", "ExtraBold", 34),
    z("positive Glaubensfreiheit, praktische Konkordanz", 240, 480, beim("t3", "positive"), size=33),
    linienzug([(130, 548), (1130, 548)], "t4", breite=3),
    blk(200, 568, 950, 130, GELB, "t4", [("Kopftuch der Lehrerin: ihr Bekenntnis", "ExtraBold", 32, INK),
                                       ("Kreuz an der Wand: hängt der Staat auf", "ExtraBold", 32, INK)]),
    zit("BVerfGE 138, 296 Rn. 104, 112 (Folge 217)", 200, 708, "t4"),
    *neinz("nie mit der Mehrheit in der Klasse argumentieren", 766, "fehler", "Bold", 33, x=245),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "merke"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# I Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Der Staat darf Kinder nicht ", 0), ("zwingen", "a"), (",", 0)],
                 [("unter dem Kreuz zu lernen.", 0)]],
                750, 290, 44, "merke", {"a": beim("merke", "zwingen")}),
    *markertext([[("Wo die Schulpflicht kein ", 0), ("Ausweichen", "b"), (" lässt,", 0)],
                 [("entscheidet nicht die ", 0), ("Mehrheit", "c"), (".", 0)]],
                750, 520, 44, "m2", {"b": beim("m2", "Ausweichen"), "c": beim("m2", "Mehrheit")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
