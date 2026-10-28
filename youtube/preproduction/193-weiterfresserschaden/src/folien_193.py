"""Folge 193 · Weiterfresserschaden: Ein 40-Euro-Teil zerstört den ganzen Motor – Serienstandard Open Peeps (Katzenkönig).
Fall (fiktiv, nach dem Plan-Hook): Hinnerk kauft im Autohaus einen fabrikneuen Kleinwagen (26.000 €); die Spannrolle am
Zahnriemen (Kleinteil, 40 €) hat der Hersteller fehlerhaft gefertigt. Nach 6 Wochen bricht sie, der Motor ist zerstört,
Hinnerk rollt sicher an den Straßenrand. In der Werkstatt: Meister Ottokar (neuer Motor 7.800 €). Szenen laut ../SZENENPLAN.md.
DARSTELLUNG: Auto, Motor und Spannrolle als Tabler-Icons, keine Automarke, kein Unfall mit Personen; zwei Handlungsgeräusche
(Motor stirbt ab, Ratsche in der Werkstatt; ../geraeusche_herkunft.json).
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz
als eigene Kopie aus Folge 187 (gemeinsame Dateien unverändert); neu: boden_(), riss(), strasse().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_193/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_193/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def umbruch(text, size, breite, stil="Regular"):
    """Zeilenumbruch für Wortlautkarten (Wortlaut bleibt unverändert)."""
    f = F(stil, size)
    zeilen, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if f.getlength(t) <= breite:
            cur = t
        else:
            zeilen.append(cur); cur = w
    return zeilen + [cur] if cur else zeilen


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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 124/149) ------------------------------------
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
    return pl(text, cx, unten + 22, cue, fill=fill, size=30, anker="m", **k)


def okz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Haken davor (zur gesprochenen Bejahung)."""
    return [ok(x - 45, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]


def neinz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Kreuz davor (zur gesprochenen Verneinung)."""
    return [nein(x - 45, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]






X1, X2 = 1430, 1730                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"HI": "Hinnerk", "OT": "Ottokar"}
NFARBE = {"HI": BLAU, "OT": GRUEN}


def stehend(k, x, folge, unten=FB, hoehe=FR):
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


def zwei(folge_hi, folge_ot):
    """Hinnerk und Ottokar rechts neben der Tafel (blicken nach links zur Tafel)."""
    return [*stehend("HI", X1, folge_hi), *stehend("OT", X2, folge_ot)]


# --- eigene Szenenbausteine (programmatisch, Palettenflächen, Tuschekontur) ---------------------------------------------------
HELLBLAU = (214, 230, 252, 255)
ASPHALT = (196, 196, 192, 255)
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig


def boden_(y, c, fill=None, x0=30, x1=1890, h=None):
    """Boden in Seitenansicht: Tuschelinie, optional Fläche darunter."""
    hh = h or 60
    im = Image.new("RGBA", (x1 - x0, hh))
    dr = ImageDraw.Draw(im)
    if fill:
        dr.rectangle((0, 0, x1 - x0, hh), fill=fill)
    dr.line((0, 2, x1 - x0, 2), fill=INK, width=6)
    return El(im, x0, y, c, "cut", 0.0, None, name="boden")


def strasse(y, c):
    """Straße in Seitenansicht: Asphaltband mit Mittelstreifen (Grundformen)."""
    im = Image.new("RGBA", (1860, 110))
    dr = ImageDraw.Draw(im)
    dr.rectangle((0, 0, 1860, 110), fill=ASPHALT)
    dr.line((0, 2, 1860, 2), fill=INK, width=6)
    for x in range(40, 1860, 220):
        dr.rounded_rectangle((x, 50, x + 120, 62), 5, fill=WEISS)
    return El(im, 30, y, c, "cut", 0.0, None, name="strasse")


def riss(cx, cy, cue, gr=1.0, bis=None):
    """Bruchlinien (rot) an einem Bauteil: Grundform wie die Risslinien in Folge 187."""
    w = int(120 * gr)
    im = Image.new("RGBA", (w, w))
    dr = ImageDraw.Draw(im)
    m = w / 2
    for (a, b, c_, d_) in [(-0.1, 0, -0.42, -0.3), (0.1, 0, 0.42, -0.3), (-0.1, 0.05, -0.44, 0.32), (0.1, 0.05, 0.44, 0.34),
                           (0, -0.08, 0, -0.45)]:
        dr.line((m + a * w, m + b * w, m + c_ * w, m + d_ * w), fill=DROT, width=max(4, int(6 * gr)))
    return bis_(El(im, cx - m, cy - m, cue, "pop", 0.0, bis, name="riss"), bis)


# ===========================================================================================================================
# A1 Fall: im Autohaus
# ===========================================================================================================================
G0 = 900                                     # Boden der Fallszenen
FHA = 430                                    # Figurenhöhe in den Fallszenen
CAR_X = 820
folie([(NULL, "Fall · Im Autohaus"), ("teil", "Fall · Die fehlerhafte Spannrolle")], [
    hart(boden_(G0, NULL)),
    hart(ficon("tabler", "building-store", 330, G0 + 4, 470, NULL, fuell=BLAU, anim="cut")),
    hart(pl("Autohaus am Stadtrand", 70, 30, NULL, fill=GELB, size=34)),
    hart(ficon("tabler", "car", CAR_X, G0 + 4, 380, NULL, fuell=PINK, anim="cut")),
    *fig("HI", 1170, G0, FHA, [(beim("hinnerk", "Hinnerk"), "froh"), ("teil", "ruhig")]),
    ns("Hinnerk", 1170, G0, beim("hinnerk", "Hinnerk"), BLAU, d=0.1),
    pl("fabrikneuer Kleinwagen", 70, 100, beim("hinnerk", "fabrikneuen"), fill=WEISS, size=32),
    pl("Kaufpreis: 26.000 €", 70, 170, beim("hinnerk", "sechsundzwanzigtausend"), fill=GELB, size=32),
    # Was niemand weiß: die Spannrolle, beim Hersteller fehlerhaft gefertigt (Lupe oben rechts)
    karte(1330, 60, 540, 470, beim("teil", "Hersteller"), fill=HELLBLAU, rund=22, schatten=6, rand=4),
    ficon("tabler", "building-factory-2", 1470, 260, 190, beim("teil", "Hersteller"), fuell=GRUEN),
    pl("Hersteller", 1470, 290, beim("teil", "Hersteller"), fill=WEISS, size=28, anker="m"),
    pfeil(1580, 190, 1660, 190, beim("teil", "Spannrolle"), breite=7, kopf=22),
    ficon("tabler", "disc", 1760, 250, 150, beim("teil", "Spannrolle"), fuell=GELB),
    riss(1760, 175, beim("teil", "fehlerhaft"), gr=0.9),
    pl("Spannrolle, fehlerhaft gefertigt", 1600, 370, beim("teil", "fehlerhaft"), fill=HELLROT, size=28, anker="m"),
    pl("Kleinteil: 40 €", 1600, 450, beim("teil", "vierzig"), fill=GELB, size=30, anker="m"),
    pl("Was niemand weiß", 70, 240, "teil", fill=HELLROT, size=32),
])

# ===========================================================================================================================
# A2 Fall: 6 Wochen später auf der Straße
# ===========================================================================================================================
SY = 790                                     # Straßenoberkante
CAR2 = 760
folie([("fahrt", "Fall · 6 Wochen später"), ("bruch", "Fall · Die Spannrolle bricht"), ("motor", "Fall · Motor zerstört"),
       ("rand", "Fall · Am Straßenrand")], [
    strasse(SY, "fahrt"),
    bis_(ficon("tabler", "car", CAR2, SY + 6, 380, "fahrt", fuell=PINK, anim="cut"), "rand"),
    ficon("tabler", "calendar", 120, 230, 110, "fahrt", fuell=WEISS),
    pl("6 Wochen problemlos", 200, 150, beim("fahrt", "Wochen"), fill=GRUEN, size=34),
    # Bruch: Spannrolle mit Rissen, Zahnriemen springt über
    szene(ficon("tabler", "disc", 1180, 470, 140, "bruch", fuell=GELB), "193motor*", 0.7, 0.0),
    riss(1180, 400, "bruch", gr=1.0),
    pl("Spannrolle bricht", 1180, 500, "bruch", fill=HELLROT, size=30, anker="m"),
    pl("Zahnriemen springt über", 1180, 570, beim("bruch", "Zahnriemen"), fill=WEISS, size=30, anker="m"),
    # Motor zerstört
    ficon("tabler", "engine", 1600, 470, 230, "motor", fuell=HELLGRAU),
    riss(1600, 380, "motor", gr=1.3),
    pl("Motor zerstört", 1600, 520, beim("motor", "zerstört"), fill=ROT, size=32, anker="m"),
    # sicher am Straßenrand: Wagen steht, Warndreieck, Hinnerk steigt aus
    ficon("tabler", "car", CAR2 - 300, SY + 6, 380, "rand", fuell=PINK, anim="cut"),
    ficon("tabler", "alert-triangle", 120, SY + 6, 90, "rand", fuell=ROT),
    *fig("HI", 860, SY + 6, FHA, [("rand", "schreck_r")]),
    ns("Hinnerk", 860, SY + 6, "rand", BLAU, d=0.1),
    pl("sicher am Straßenrand", 200, 230, beim("rand", "sicher"), fill=WEISS, size=32),
])

# ===========================================================================================================================
# A3 Fall: in der Werkstatt
# ===========================================================================================================================
OX, HX = 900, 1450                           # Ottokar (blickt nach rechts), Hinnerk (blickt nach links)
folie([("werk", "Fall · In der Werkstatt"), ("o1", "Fall · Ottokar: Spannrolle gebrochen"), ("o2", "Fall · neuer Motor: 7.800 €"),
       ("h1", "Fall · Hinnerk will Ersatz vom Hersteller"), ("frage", "Fall · Die Frage"), ("klass", "Fall · Ein Klassiker")], [
    boden_(G0, "werk", fill=HELLGRAU, h=100),
    ficon("tabler", "car", 270, G0 + 4, 380, "werk", fuell=PINK, anim="cut"),
    ficon("tabler", "engine", 610, G0 + 4, 180, "werk", fuell=HELLGRAU, anim="cut"),
    riss(610, 800, "werk", gr=0.9),
    szene(ficon("tabler", "tools", 130, 560, 100, "werk", fuell=GELB), "193ratsche*", 0.6, 0.0),
    *fig("OT", OX, G0, FHA, [(beim("werk", "Meister"), "denkt_r")], bis="o1"),
    ns("Ottokar", OX, G0, beim("werk", "Meister"), GRUEN, d=0.1),
    pl("Meister Ottokar", 70, 30, beim("werk", "Meister"), fill=GRUEN, size=32, bis="frage"),
    *fig("HI", HX, G0, FHA, [("werk", "sorge")], bis="o1", erst="cut"),
    ns("Hinnerk", HX, G0, "werk", BLAU),
    # Ottokar redet
    *redet("OT_redet_r", OX, G0, FHA, "o1", "h1"),
    blase("sprech", 960, 150, "o1", 820, 270, inhalt=["Die Spannrolle ist gebrochen. Ein Teil", "für 40 €, und der Motor ist hin."],
          textsize=36, figur=("OT_redet_r", OX, G0, FHA), bis="o2"),
    blase("sprech", 760, 112, "o2", 820, 280, inhalt=["Ein neuer kostet 7.800 €."], textsize=38,
          figur=("OT_redet_r", OX, G0, FHA), bis="h1"),
    ficon("tabler", "disc", 400, 530, 90, beim("o1", "Spannrolle"), fuell=GELB),
    riss(400, 485, beim("o1", "gebrochen"), gr=0.7),
    pl("Spannrolle: 40 €", 400, 560, beim("o1", "vierzig"), fill=GELB, size=28, anker="m"),
    pl("neuer Motor: 7.800 €", 560, 640, beim("o2", "siebentausendachthundert"), fill=HELLROT, size=30, anker="m"),
    *fig("HI", HX, G0, FHA, [("o1", "schreck"), ("o2", "sorge")], bis="h1", erst="cut"),
    # Hinnerk redet
    *redet("HI_redet", HX, G0, FHA, "h1", "frage"),
    blase("sprech", 1080, 150, "h1", 1310, 260, inhalt=["Der Wagen ist 6 Wochen alt! Dann soll", "der Hersteller den Motor bezahlen."],
          textsize=36, figur=("HI_redet", HX, G0, FHA), bis="frage"),
    *fig("OT", OX, G0, FHA, [("h1", "ernst_r"), ("frage", "denkt_r"), ("klass", "ruhig_r")], erst="cut"),
    *fig("HI", HX, G0, FHA, [("frage", "denkt"), ("klass", "ernst")], erst="cut"),
    pl("Kann Hinnerk vom Hersteller Ersatz für den Motor verlangen?", 70, 100, "frage", fill=PINK, size=32),
    pl("Klassiker: der Weiterfresserschaden", 70, 170, beim("klass", "Weiterfresserschaden"), fill=GELB, size=32),
    zit("Schwimmerschalter: BGH, Urt. v. 24.11.1976 – VIII ZR 137/75, BGHZ 67, 359", 80, 238, beim("klass2", "Schwimmerschalter")),
    zit("Gaszug: BGH, Urt. v. 18.1.1983 – VI ZR 310/79, BGHZ 86, 256", 80, 280, beim("klass2", "Gaszug")),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_193(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=36, zeilenabstand=1.32)
        els += e; y += 16
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_193("sv", [
    "Hinnerk kauft in einem Autohaus einen fabrikneuen Kleinwagen für 26.000 €. Der Hersteller hat eine Spannrolle am "
    "Zahnriemen fehlerhaft gefertigt, ein Kleinteil im Wert von 40 €. Rechtzeitig erkannt, hätte man die Rolle mit geringem "
    "Aufwand tauschen können. Eine Garantie des Herstellers gibt es nicht.",
    "Sechs Wochen fährt der Wagen problemlos. Dann bricht die Spannrolle, der Zahnriemen springt über, und der Motor ist "
    "zerstört. Hinnerk rollt sicher an den Straßenrand. Meister Ottokar stellt in der Werkstatt fest: Ein neuer Motor kostet "
    "7.800 €.",
    "Hinnerk sagt: „Der Wagen ist 6 Wochen alt! Dann soll der Hersteller den Motor bezahlen.“",
], "Kann Hinnerk vom Hersteller Ersatz für den Motor aus § 823 Abs. 1 BGB verlangen?")

# ===========================================================================================================================
# C1 Warum Deliktsrecht?
# ===========================================================================================================================
PD = "Warum Deliktsrecht?"
folie([("warum", PD), ("vk", f"{PD} › Autohaus: § 437 BGB"), ("hst", f"{PD} › Hersteller: kein Vertrag")], rechts_frei([
    *tafel("warum", "Warum Deliktsrecht?"),
    blk(110, 185, 1040, 130, GELB, "vk", [("Autohaus (Verkäufer):", "ExtraBold", 34, INK),
                                        ("Mängelrechte aus § 437 BGB", "Bold", 32, INK)]),
    z("Mangelbegriff: Video „Sachmangel“", 110, 335, beim("vk", "Mangelbegriff"), "Bold", 30, farbe=TEXT),
    blk(110, 420, 1040, 130, GRUEN, "hst", [("Hersteller: kein Vertrag", "ExtraBold", 34, INK),
                                         ("nur Deliktsrecht oder Produkthaftungsgesetz", "Bold", 32, INK)]),
    *requisit([("warum", ("tabler", "car", 230, PINK), "Deliktsrecht?", WEISS),
               ("vk", ("tabler", "building-store", 190, BLAU), "Autohaus: § 437 BGB", GELB),
               ("hst", ("tabler", "building-factory-2", 180, GRUEN), "Hersteller: kein Vertrag", GRUEN)]),
    *zwei([("warum", "ernst"), ("hst", "denkt")], [("warum", "ruhig"), ("vk", "denkt"), ("hst", "ernst")]),
]))

# ===========================================================================================================================
# C2 Die Fristen (Wortlaut kurz)
# ===========================================================================================================================
PF = "Warum Deliktsrecht? › Fristen"
folie([("fr1", f"{PF}: § 438 BGB"), ("fr2", f"{PF}: § 195 BGB"), ("fr3", f"{PF}: Beginn, § 199 Abs. 1 BGB"),
       ("fr4", f"{PF}: Anspruch erst mit dem Schaden")], rechts_frei([
    *tafel("fr1", "Die Fristen"),
    karte(90, 170, 1080, 180, "fr1", fill=ZITAT, rund=18, schatten=6, rand=4),
    z("Kaufrecht: „… im Übrigen in zwei Jahren.“", 118, 190, "fr1", size=32, rechts=1150),
    z("„… im Übrigen mit der Ablieferung der Sache.“", 118, 238, beim("fr1", "Ablieferung"), size=32, rechts=1150),
    z("§ 438 Abs. 1 Nr. 3, Abs. 2 BGB", 118, 290, "fr1", "Bold", 28, farbe=TEXT, rechts=1150),
    karte(90, 380, 1080, 130, "fr2", fill=ZITAT, rund=18, schatten=6, rand=4),
    z("Delikt: „Die regelmäßige Verjährungsfrist", 118, 398, "fr2", size=32, rechts=1150),
    z("beträgt drei Jahre.“  § 195 BGB", 118, 446, "fr2", size=32, rechts=1150),
    z("Beginn: Schluss des Jahres, in dem der Anspruch", 110, 545, "fr3", "Bold", 32),
    z("entsteht und Kenntnis von Umständen und Schuldner", 110, 590, beim("fr3", "Umstände"), "Bold", 32),
    z("besteht oder grob fahrlässig fehlt (§ 199 Abs. 1 BGB)", 110, 635, beim("fr3", "Fahrlässigkeit"), "Bold", 30),
    blk(110, 700, 1040, 80, GELB, "fr4", [("Anspruch entsteht erst mit der Zerstörung des Motors", "ExtraBold", 31, INK)]),
    zit("BGH, Urt. v. 23.2.2021 – VI ZR 21/20, Rn. 21", 110, 795, "fr4"),
    *requisit([("fr1", ("tabler", "calendar", 110, WEISS), "Kaufrecht: 2 Jahre", GELB),
               ("fr2", ("tabler", "hourglass", 100, WEISS), "Delikt: 3 Jahre", GRUEN),
               ("fr4", ("tabler", "engine", 170, HELLGRAU), "Teil bricht erst nach Jahren?", WEISS)]),
    *zwei([("fr1", "denkt"), ("fr4", "froh")], [("fr1", "ernst"), ("fr3", "denkt")]),
]))

# ===========================================================================================================================
# D Wortlautkarte § 823 Abs. 1 BGB
# ===========================================================================================================================
W823 = umbruch("„Wer vorsätzlich oder fahrlässig das Leben, den Körper, die Gesundheit, die Freiheit, das Eigentum oder ein "
               "sonstiges Recht eines anderen widerrechtlich verletzt, ist dem anderen zum Ersatz des daraus entstehenden "
               "Schadens verpflichtet.“", 34, 1040)
_zi = lambda wort: next(i for i, t in enumerate(W823) if wort in t)
w823, w823_y = wortlaut(80, 170, 1100, W823, "§ 823 Abs. 1 BGB", "norm",
                        marken=[(_zi("Eigentum"), "Eigentum", beim("w1", "Eigentum")),
                                (_zi("verletzt"), "verletzt", beim("w1", "verletzt"))], size=34)
PN = "Die Norm: § 823 Abs. 1 BGB"
folie([("norm", PN), ("schema", f"{PN} › übrige Merkmale: Video „Deliktsrecht“"), ("prob", f"{PN} › Eigentum: das Problem")],
      rechts_frei([
    *tafel("norm", "Die Norm: § 823 Abs. 1 BGB"),
    *w823,
    z("übrige Merkmale: Video „Deliktsrecht“", 110, w823_y + 30, beim("schema", "übrigen"), "Bold", 30, farbe=TEXT),
    blk(110, w823_y + 90, 1040, 80, GELB, "prob", [("hier: das Eigentum – und das Problem", "ExtraBold", 32, INK)]),
    z("Auto schon mit der fehlerhaften Spannrolle erworben", 110, w823_y + 200, "prob2", "Bold", 32),
    blk(110, w823_y + 265, 1040, 80, PINK, "prob3", [("Sache verletzt, die von Anfang an mangelhaft war?", "ExtraBold", 32, INK)]),
    *requisit([("norm", ("tabler", "book", 100, WEISS), "§ 823 Abs. 1 BGB", GELB),
               ("prob2", ("tabler", "disc", 110, GELB), "fehlerhafte Spannrolle", HELLROT)]),
    *zwei([("norm", "ruhig"), ("prob2", "denkt")], [("norm", "ernst"), ("prob3", "denkt")]),
]))
assert w823_y + 345 <= 900

# ===========================================================================================================================
# E Zwei Interessen, Mangelunwert
# ===========================================================================================================================
PI = "Eigentumsverletzung › Stoffgleichheit"
folie([("int", f"{PI}: zwei Interessen"), ("aeq", f"{PI} › Äquivalenzinteresse"), ("integ", f"{PI} › Integritätsinteresse"),
       ("unwert", f"{PI} › Mangelunwert"), ("deckt", f"{PI} › stoffgleich: kein Delikt"),
       ("mehr", f"{PI} › darüber hinaus: Integritätsinteresse")], rechts_frei([
    *tafel("int", "Zwei Interessen"),
    blk(110, 180, 505, 210, GELB, "aeq", [("Vertragsrecht:", "Bold", 30, INK), ("Äquivalenz-", "ExtraBold", 32, INK),
                                        ("interesse", "ExtraBold", 32, INK)]),
    z("mangelfreie Sache", 130, 405, beim("aeq", "Erwartung"), size=30),
    z("für den Kaufpreis", 130, 445, beim("aeq", "Kaufpreis"), size=30),
    blk(645, 180, 505, 210, GRUEN, "integ", [("Deliktsrecht:", "Bold", 30, INK), ("Integritäts-", "ExtraBold", 32, INK),
                                           ("interesse", "ExtraBold", 32, INK)]),
    z("durch die Sache nicht", 665, 405, beim("integ", "durch"), size=30),
    z("am Eigentum verletzt", 665, 445, beim("integ", "Eigentum"), size=30),
    z("Mangelunwert: steckt von Anfang an in der Sache", 110, 525, "unwert", "Bold", 32),
    *neinz("Schaden = Mangelunwert: stoffgleich, kein Delikt", 595, beim("deckt", "stoffgleich"), "Bold", 31, x=160),
    *okz("Schaden geht darüber hinaus: Integritätsinteresse", 660, beim("mehr", "darüber"), "Bold", 31, x=160),
    z("kann verletzt sein", 160, 705, beim("mehr", "verletzt"), "Bold", 31),
    zit("BGH, Urt. v. 23.2.2021 – VI ZR 21/20, Rn. 11", 110, 770, beim("mehr", "verletzt")),
    *requisit([("int", ("tabler", "scale", 110, WEISS), "zwei Interessen", WEISS),
               ("aeq", ("tabler", "receipt-euro", 100, GELB), "Kaufpreis", GELB),
               ("integ", ("tabler", "shield-check", 100, GRUEN), "Eigentum", GRUEN),
               ("unwert", ("tabler", "disc", 110, GELB), "Mangel von Anfang an", HELLROT)]),
    *zwei([("int", "ruhig"), ("unwert", "denkt"), ("mehr", "froh")], [("int", "ernst"), ("deckt", "denkt")]),
]))

# ===========================================================================================================================
# F Kriterien der Stoffgleichheit (BGH VI ZR 21/20 Rn. 16)
# ===========================================================================================================================
PK = "Stoffgleichheit › Kriterien"
folie([("krit", PK), ("k1", f"{PK} › Fehler erfasst die ganze Sache"), ("k3", f"{PK} › nicht behebbar"),
       ("k4", f"{PK} › Mangel auf ein Teil beschränkt"), ("k6", f"{PK} › nicht stoffgleich")], rechts_frei([
    *tafel("krit", "Wann ist der Schaden stoffgleich?"),
    blk(110, 180, 1040, 260, HELLROT, "k1", [("stoffgleich (kein Delikt), wenn …", "ExtraBold", 32, INK),
                                          ("der Fehler von Anfang an die ganze Sache erfasst", "Bold", 30, INK),
                                          ("", "Bold", 30, INK), ("", "Bold", 30, INK)]),
    z("– etwa: von vornherein nicht oder kaum brauchbar", 140, 320, beim("k2", "etwa"), size=30),
    z("– oder: technisch oder wirtschaftlich nicht behebbar", 140, 370, beim("k3", "technisch"), size=30),
    blk(110, 470, 1040, 210, HELLGRUEN, "k4", [("nicht stoffgleich, wenn …", "ExtraBold", 32, INK),
                                            ("der Mangel zunächst auf ein Teil beschränkt und", "Bold", 30, INK),
                                            ("behebbar ist", "Bold", 30, INK), ("", "Bold", 30, INK)]),
    z("– und erst später den Rest zerstört: Rest hat eigenen Wert", 140, 625, "k5", size=29),
    *okz("Schaden nicht stoffgleich: Delikt möglich", 715, "k6", "ExtraBold", 32, x=160),
    zit("BGH, Urt. v. 23.2.2021 – VI ZR 21/20, Rn. 16", 110, 780, "k6"),
    *requisit([("krit", ("tabler", "zoom-scan", 100, WEISS), "stoffgleich?", WEISS),
               ("k1", ("tabler", "engine-off", 150, HELLROT), "ganze Sache erfasst", HELLROT),
               ("k4", ("tabler", "disc", 110, GELB), "auf ein Teil beschränkt", HELLGRUEN),
               ("k5", ("tabler", "engine", 160, GRUEN), "Rest: eigener Wert", HELLGRUEN)]),
    *zwei([("krit", "denkt"), ("k6", "froh")], [("krit", "ernst"), ("k4", "denkt")]),
]))

# ===========================================================================================================================
# G Anwendung auf den Fall
# ===========================================================================================================================
PA = "Stoffgleichheit › im Fall"
folie([("anw", PA), ("a1", f"{PA} › Fehler nur in der Spannrolle"), ("a2", f"{PA} › behebbar"), ("a3", f"{PA} › Motor mangelfrei"),
       ("a4", "Eigentumsverletzung am Motor (+)"), ("a5", "Spannrolle selbst: Kaufrecht")], rechts_frei([
    *tafel("anw", "Im Fall: stoffgleich?"),
    *okz("Fehler nur in der Spannrolle (Teil für 40 €)", 185, "a1", "Bold", 32, x=160),
    *okz("rechtzeitig getauscht: Motor heil geblieben", 255, "a2", "Bold", 32, x=160),
    z("also mit geringem Aufwand behebbar", 160, 305, beim("a2", "geringem"), size=30),
    *okz("Motor selbst mangelfrei, eigener Wert", 375, "a3", "Bold", 32, x=160),
    blk(110, 450, 1040, 130, GRUEN, "a4", [("nicht stoffgleich:", "ExtraBold", 34, INK),
                                         ("Eigentumsverletzung am Motor", "ExtraBold", 34, INK)]),
    *neinz("Spannrolle selbst: von Anfang an fehlerhaft", 625, "a5", "Bold", 32, x=160),
    z("für sie bleibt es beim Kaufrecht", 160, 672, beim("a5", "Kaufrecht"), size=30),
    zit("BGH, Urt. v. 23.2.2021 – VI ZR 21/20, Rn. 13, 16", 160, 725, beim("a5", "Kaufrecht")),
    *requisit([("anw", ("tabler", "car", 230, PINK), "der Fall", WEISS),
               ("a1", ("tabler", "disc", 110, GELB), "Spannrolle: 40 €", HELLROT),
               ("a3", ("tabler", "engine", 170, GRUEN), "Motor: eigener Wert", HELLGRUEN),
               ("a5", ("tabler", "disc", 110, GELB), "Spannrolle: Kaufrecht", GELB)]),
    *zwei([("anw", "denkt"), ("a4", "froh")], [("anw", "ernst"), ("a2", "froh"), ("a5", "ruhig")]),
]))

# ===========================================================================================================================
# H Gegenbeispiel: ganzer Motor von Anfang an unbrauchbar
# ===========================================================================================================================
PG = "Gegenbeispiel · Fehler erfasst das ganze Gerät"
folie([("gegen", PG), ("g1", f"{PG} › Motor falsch konstruiert"), ("g2", f"{PG} › stoffgleich: nur Kaufrecht")], rechts_frei([
    *tafel("gegen", "Gegenbeispiel"),
    blk(110, 180, 1040, 80, HELL, "gegen", [("Fehler erfasst von Anfang an das ganze Gerät", "ExtraBold", 32, INK)]),
    z("ganzer Motor falsch konstruiert,", 110, 300, beim("g1", "ganze"), "Bold", 32),
    z("nicht mit vertretbarem Aufwand behebbar", 110, 345, beim("g1", "vertretbarem"), "Bold", 32),
    z("von Anfang an kaum zu gebrauchen", 110, 405, beim("g1", "kaum"), size=32),
    *neinz("später kaputt: Schaden stoffgleich", 485, beim("g2", "stoffgleich"), "ExtraBold", 34, x=160),
    blk(110, 560, 1040, 80, ROT, beim("g2", "allein"), [("kein Delikt: allein Kaufrecht", "ExtraBold", 34, INK)]),
    zit("BGH, Urt. v. 23.2.2021 – VI ZR 21/20, Rn. 16", 110, 660, beim("g2", "allein")),
    *requisit([("gegen", ("tabler", "engine-off", 170, HELLROT), "ganzes Gerät erfasst", HELLROT),
               (beim("g2", "allein"), ("tabler", "building-store", 190, BLAU), "allein Kaufrecht", GELB)]),
    *zwei([("gegen", "ernst"), ("g2", "sorge")], [("gegen", "denkt"), ("g2", "ernst")]),
]))

# ===========================================================================================================================
# I1 Kritik (Meinung) und Gesetzgeber
# ===========================================================================================================================
folie([("lehre", "Kritik · Teil der Lehre (Meinung)"), ("bt", "Kritik › Gesetzgeber der Schuldrechtsreform")], rechts_frei([
    *tafel("lehre", "Kritik an der Figur"),
    blk(110, 185, 1040, 130, HELL, "lehre", [("Meinung (Teil der Lehre):", "ExtraBold", 32, INK),
                                          ("umgeht die kürzere Verjährung des Kaufrechts", "Bold", 32, INK)]),
    z("Gesetzgeber bei der Schuldrechtsreform:", 110, 370, "bt", "Bold", 32),
    z("Wertungswiderspruch weitgehend vermieden,", 110, 415, beim("bt", "Wertungswiderspruch"), size=32),
    z("weil die regelmäßige Verjährung nun kürzer ist", 110, 460, beim("bt", "weil"), size=32),
    zit("BT-Drucks. 14/6040, S. 229", 110, 515, beim("bt", "weil")),
    *requisit([("lehre", ("tabler", "book-2", 100, LILA), "Kritik", WEISS),
               ("bt", ("tabler", "building-bank", 110, WEISS), "Gesetzgeber", WEISS)]),
    *zwei([("lehre", "denkt")], [("lehre", "ernst"), ("bt", "ruhig")]),
]))

# ===========================================================================================================================
# I2 Wortlautkarte § 1 Abs. 1 Satz 2 ProdHaftG
# ===========================================================================================================================
WPH = umbruch("„Im Falle der Sachbeschädigung gilt dies nur, wenn eine andere Sache als das fehlerhafte Produkt beschädigt "
              "wird und diese andere Sache ihrer Art nach gewöhnlich für den privaten Ge- oder Verbrauch bestimmt und hierzu "
              "von dem Geschädigten hauptsächlich verwendet worden ist.“", 32, 1040)
_zp = lambda wort: next(i for i, t in enumerate(WPH) if wort in t)
wph, wph_y = wortlaut(80, 170, 1100, WPH, "§ 1 Abs. 1 Satz 2 ProdHaftG", "phg",
                      marken=[(_zp("andere"), "andere", beim("phg1", "andere")),
                              (_zp("Produkt"), "Produkt", beim("phg1", "Produkt"))], size=32)
PP = "Kontrast: Produkthaftungsgesetz"
folie([("phg", PP), ("phg1", f"{PP} › nur andere Sache"), ("phg2", f"{PP} › Motor: Teil des Autos")], rechts_frei([
    *tafel("phg", "Enger: das Produkthaftungsgesetz"),
    *wph,
    *neinz("Motor: Teil des fehlerhaften Autos", wph_y + 40, beim("phg2", "Motor"), "ExtraBold", 34, x=160),
    blk(110, wph_y + 115, 1040, 80, GELB, beim("phg2", "Gegen"), [("gegen den Hersteller hier nur § 823 BGB", "ExtraBold", 32, INK)]),
    *requisit([("phg", ("tabler", "book", 100, WEISS), "Produkthaftungsgesetz", WEISS),
               ("phg2", ("tabler", "car", 230, PINK), "Motor: Teil des Autos", HELLROT)]),
    *zwei([("phg", "denkt"), ("phg2", "ernst")], [("phg", "ernst"), ("phg2", "denkt")]),
]))
assert wph_y + 195 <= 900

# ===========================================================================================================================
# J Ergebnis
# ===========================================================================================================================
folie([("erg", "Ergebnis · Eigentum am Motor verletzt"), ("erg2", "Ergebnis › Hersteller ersetzt den Motor"),
       ("erg3", "Ergebnis › Spannrolle: Mängelrechte")], rechts_frei([
    *tafel("erg", "Ergebnis"),
    blk(110, 180, 1040, 80, GRUEN, "erg", [("Eigentum von Hinnerk am Motor verletzt", "ExtraBold", 34, INK)]),
    z("liegen auch die übrigen Voraussetzungen vor:", 110, 320, beim("erg2", "übrigen"), "Bold", 32),
    *okz("Hersteller ersetzt den Motor (7.800 €)", 375, beim("erg2", "ersetzen"), "Bold", 32, x=160),
    z("Spannrolle selbst: Mängelrechte gegen das Autohaus", 110, 470, "erg3", "Bold", 32),
    *requisit([("erg", ("tabler", "gavel", 100, HOLZ), "Ergebnis", WEISS),
               ("erg2", ("tabler", "building-factory-2", 180, GRUEN), "Hersteller: Motor", GRUEN),
               ("erg3", ("tabler", "building-store", 190, BLAU), "Autohaus: Spannrolle", GELB)]),
    *zwei([("erg", "froh")], [("erg", "ruhig"), ("erg2", "froh")]),
]))

# ===========================================================================================================================
# K Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Stoffgleichheit bei der Eigentumsverletzung"), ("tp2", "Klausurtipp · sauber trennen"),
       ("tp3", "Klausurtipp · Ansprüche gegen den Verkäufer daneben")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Stoffgleichheit bei der Eigentumsverletzung", 200, 200, beim("tipp", "Stoffgleichheit"), "Bold", 36),
    z("prüfen, nicht erst beim Schaden", 200, 260, beim("tipp", "nicht"), size=34),
    z("Trenne: Was war von Anfang an mangelhaft,", 200, 345, "tp2", "Bold", 36),
    z("was war vorher heil?", 200, 405, beim("tp2", "was", 2), size=34),
    linienzug([(130, 485), (1130, 485)], "tp3", breite=3),
    z("Ansprüche gegen den Verkäufer", 200, 515, "tp3", "Bold", 36),
    z("stehen daneben", 200, 575, beim("tp3", "daneben"), size=34),
    zit("BGH, Urt. v. 23.2.2021 – VI ZR 21/20, Rn. 10, 13", 200, 625, beim("tp3", "daneben")),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# L Prüfschema
# ===========================================================================================================================
REIHEN = [("c1", 0, "I. Eigentumsverletzung", True),
          ("c2", 1, "1. Welcher Teil war beim Erwerb mangelhaft?", False),
          ("c3", 1, "2. Stoffgleichheit: Mangel auf ein Teil beschränkt und behebbar,", False),
          ("c3", 2, "Schaden erst später am übrigen Teil?", False),
          ("c4", 0, "II. Übrige Merkmale des § 823 Abs. 1 BGB", True),
          ("c5", 0, "III. Konkurrenzen", True),
          ("c5", 1, "Kaufrecht gegen den Verkäufer; ProdHaftG nur für andere Sachen", False)]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfschema: Weiterfresserschaden"), 110, 90, "sch", 46),
           z("§ 823 Abs. 1 BGB gegen den Hersteller; übriges Schema: Video „Deliktsrecht“", 110, 160, "sch", "Bold", 32,
             farbe=TEXT, rechts=1800)]
y = 250
for c, ebene, text, fett in REIHEN:
    x = (130, 200, 250)[ebene]
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 40 if ebene == 0 else 34, rechts=1800))
    y += {0: 85, 1: 70, 2: 90}[ebene]
assert y <= 970, y
folie([("sch", "Prüfschema"), ("c1", "Prüfschema › I. Eigentumsverletzung"), ("c2", "Prüfschema › I. 1. mangelhafter Teil"),
       ("c3", "Prüfschema › I. 2. Stoffgleichheit"), ("c4", "Prüfschema › II. übrige Merkmale"),
       ("c5", "Prüfschema › III. Konkurrenzen")], els_sch)

# ===========================================================================================================================
# M Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Steckt ein Mangel zunächst nur in einem", 0)], [("behebbaren Teil", "a"), (" und zerstört er später", 0)],
                 [("die übrige Sache, ist das Eigentum", 0)], [("an der übrigen Sache verletzt.", 0)]], 750, 270, 42, "merke",
                {"a": beim("merke", "behebbaren")}),
    *markertext([[("Was ", 0), ("von Anfang an", "b"), (" mangelhaft war,", 0)], [("bleibt beim Kaufrecht.", 0)]],
                750, 640, 42, "m2", {"b": beim("m2", "von")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
