"""Folge 151 · Durchsuchung StPO: Wann darf die Polizei in meine Wohnung? – Serienstandard Open Peeps (Katzenkönig).
Fall: Dienstag, 23 Uhr. Polizeikommissar Steiger klingelt bei Helene und will wegen Gefahr im Verzug ohne Beschluss
durchsuchen (Verdacht der Hehlerei mit gestohlenen Fahrrädern); Rückblick auf 14 Uhr (Anzeige, Inserat, Abholadresse,
7 Räder, kein Beschluss beantragt, Bereitschaftsdienst bis 21 Uhr); Helene widerspricht, tritt zur Seite, im Flur steht
das E-Bike. Szenen laut ../SZENENPLAN.md: A1 Wohnungstür bei Nacht (Nachtverlauf, weil der Fall in der Nachtzeit spielt),
A2 Wache am Nachmittag (Rückblick, Tageslicht), A3 Flur der Wohnung bei Nacht, B Sachverhalt, C Art. 13 GG (Wortlautkarte),
D § 102 (Wortlautkarte), E § 103 (Wortlautkarte), F § 105 (Wortlautkarte), G BVerfGE 103, 142, H selbst herbeigeführt
(Zitatkarte Rn. 39), I Bereitschaftsdienst (Tagesband 6–21 Uhr), J § 104 (Wortlautkarte), K Lösung, L Verwertungsverbot,
M Klausurtipp (Lexi), N Prüfschema, O Merksatz (Lexi).
Keine Gewalt, keine Waffen, keine Abzeichen oder Wappen, kein Blaulicht. Zwei Handlungsgeräusche (Klingel, Tür;
../geraeusche_herkunft.json). Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/
wortlaut/redet/fig/ns/okz/neinz als eigene Kopie aus Folge 148 (gemeinsame Dateien unverändert); neu: flurboden(),
wohnungstuer(), deckenlampe(), tagesband(), nachtfolie() (mit pruefe_im_bild). Zahlen auf Tafeln, Pillen und Blasen als
Ziffern. Wortlautkarten wörtlich nach gesetze-im-internet.de (Abruf 04.10.2026; Originalschreibung „daß“)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from ostil import mond, laterne, lichtkegel
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_151/"

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
        assert F(s, g).getlength(glyphen(t)) <= w - 30, f"Blockzeile zu breit: {t}"
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
        if n.startswith(("bild:", "ficon:", "bank")) or "/op_151/" in n:
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 103/109/112) --------------------------------
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




# --- eigene Szenenbausteine: Treppenhaus und Flur (Palettenflächen, Tuschekontur) ----------------------------------------
BG_FARBE["nacht"] = None                     # Nacht = Verlauf, erzeugt im Renderer (wie Folgen 001, 148)
PFAD_FARBE["nacht"] = (255, 255, 255, 170)
BODEN_N = (96, 102, 128, 255)                # Fliesenboden im Treppenhaus/Flur nachts
BODEN_T = (214, 206, 192, 255)               # Boden der Wache am Tag
F_O, F_U = 930, 1000                         # Bodenfläche (Oberkante, Unterkante)
FH = 500                                     # Figurenhöhe in den Fallszenen
FU = 942                                     # Unterkante der Figuren in den Fallszenen


def flurboden(cue, farbe, fugen=True):
    s = 2
    im = Image.new("RGBA", (1860 * s, (F_U - F_O) * s))
    dr = ImageDraw.Draw(im)
    dr.rectangle((0, 0, 1860 * s, (F_U - F_O) * s), fill=farbe)
    dr.line((0, 0, 1860 * s, 0), fill=INK, width=6 * s)
    if fugen:
        for x in range(100, 1860, 220):
            dr.line(((x + 30) * s, 6 * s, (x - 10) * s, (F_U - F_O) * s), fill=(130, 136, 160, 255), width=4 * s)
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    return El(im, 30, F_O, cue, "cut", 0.0, None, name="boden")


def wohnungstuer(cx, cue, breite=800, bis=None):
    """Wohnungstür (Tabler door, Holzfüllung), unten auf dem Boden."""
    return ficon("tabler", "door", cx, F_O + 8, breite, cue, fuell=HOLZ, bis=bis, anim="cut")


def deckenlampe(cx, cue, boden=F_O):
    """Deckenlampe (Tabler bulb, gelb) mit Lichtkegel bis zum Boden."""
    birne = ficon("tabler", "bulb", cx, 150, 90, cue, fuell=GELB, anim="cut")
    kabel = linienzug([(cx, 30), (cx, 70)], cue, breite=5)
    kegel = lichtkegel(cx, 150, 260, boden, cue)
    return [hart(kegel), hart(kabel), birne]


def nachtfolie(pfade, els):
    pruefe_im_bild(els)
    FOLIEN.append(dict(bg="nacht", pfade=pfade, els=els))


X1, X2 = 1430, 1730                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"HE": "Helene", "ST": "Steiger"}
NFARBE = {"HE": LILA, "ST": BLAU}


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


def stehend(k, x, folge, unten=FB, hoehe=FR):
    return [*fig(k, x, unten, hoehe, folge), ns(NAME[k], x, unten, folge[0][0], NFARBE[k], d=0.1)]


P = "Durchsuchung"

# ===========================================================================================================================
# A1 Fall: Dienstag, 23 Uhr, an der Wohnungstür (Nacht: der Fall spielt in der Nachtzeit des § 104 StPO)
# ===========================================================================================================================
TX = 1060                                   # Wohnungstür
HX, SX = 1290, 680                          # Helene (vor ihrer Tür, blickt nach links), Steiger (blickt nach rechts)
KL = ficon("tabler", "bell-ringing", 1340, 560, 70, "klingel", fuell=GELB, bis="tuer")
KL = szene(KL, "151klingel*", 0.9, 0.0)
TUER_ZU = wohnungstuer(TX, NULL, bis="tuer")
TUER_AUF = szene(ficon("tabler", "door", TX, F_O + 8, 800, "tuer", fuell=(255, 238, 180, 255), anim="cut"), "151tuer*", 0.7, 0.0)   # offen: Licht aus der Wohnung
nachtfolie([(NULL, "Fall · Dienstag, 23 Uhr"), ("klingel", "Fall · Es klingelt"), ("tuer", "Fall · Polizeikommissar Steiger"),
            ("st1", "Fall · „Gefahr im Verzug“"), ("h1", "Fall · Wo ist der Beschluss?"), ("st2", "Fall · Ohne Beschluss")], [
    hart(flurboden(NULL, BODEN_N)),
    *deckenlampe(560, NULL),
    hart(ficon("tabler", "window", 200, 520, 220, NULL, fuell=(58, 66, 112, 255), anim="cut")),
    hart(mond(205, 405, 34, NULL)),
    hart(TUER_ZU),
    hart(pl("Dienstag, 23 Uhr: ein Mietshaus", 70, 30, NULL, fill=GELB, size=40)),
    KL,
    pl("Es klingelt.", 1340, 470, "klingel", fill=WEISS, size=28, anker="m", bis="tuer"),
    TUER_AUF,
    # Helene öffnet und steht vor ihrer Tür; Steiger steht im Treppenhaus
    *fig("HE", HX, FU, FH, [("tuer", "schreck"), ("st2", "sorge")], bis="h1", erst="pop"),
    *redet("HE_redet", HX, FU, FH, "h1", "st2"),
    *fig("HE", HX, FU, FH, [("st2", "sorge")], bis="weiss", erst="cut"),
    ns("Helene", HX, FU, "tuer", LILA, d=0.1),
    *fig("ST", SX, FU, FH, [(beim("tuer", "Polizeikommissar"), "ernst_r")], bis="st1", erst="pop"),
    *redet("ST_redet_r", SX, FU, FH, "st1", "h1"),
    *fig("ST", SX, FU, FH, [("h1", "ernst_r")], bis="st2", erst="cut"),
    *redet("ST_redet_r", SX, FU, FH, "st2", "weiss"),
    ns("Steiger", SX, FU, beim("tuer", "Polizeikommissar"), BLAU, d=0.1),
    blase("sprech", 900, 330, "st1", 560, 240, inhalt=["Wir haben den Verdacht, dass Sie", "gestohlene Fahrräder verkaufen.",
          "Wegen Gefahr im Verzug durchsuche", "ich jetzt Ihre Wohnung."], textsize=34,
          figur=("ST_redet_r", SX, FU, FH), bis="h1"),
    blase("sprech", 760, 250, "h1", 1480, 235, inhalt=["Jetzt, mitten in der Nacht?", "Wo ist denn Ihr Beschluss?"],
          textsize=36, figur=("HE_redet", HX, FU, FH), bis="st2"),
    blase("sprech", 820, 250, "st2", 560, 255, inhalt=["Den brauche ich nicht. Bis morgen", "könnten die Räder weg sein."],
          textsize=36, figur=("ST_redet_r", SX, FU, FH)),
])

# ===========================================================================================================================
# A2 Fall: Rückblick – 14 Uhr auf der Wache (Tageslicht)
# ===========================================================================================================================
WX = 1000                                   # Steiger an seinem Schreibtisch, blickt nach links zum Laptop
TISCH = [karte(150, 700, 640, 40, "weiss", fill=HOLZ, rund=10, schatten=4, rand=4),
         linienzug([(200, 742), (200, F_O)], "weiss", breite=10), linienzug([(740, 742), (740, F_O)], "weiss", breite=10)]
RAEDER = []
for i in range(7):                          # 7 Räder in 3 Wochen (Tabler bike, je ein Icon)
    r, c = divmod(i, 4)
    c0, v0 = beim("sieben", "sieben")
    RAEDER.append(ficon("ph", "bicycle", 1300 + c * 150 + r * 75, 300 + r * 130, 120, (c0, round(v0 + 0.12 * i, 3)),
                        fuell=WEISS))
folie([("weiss", "Fall · Rückblick: 14 Uhr"), ("mittag", "Fall · Die Anzeige"), ("abhol", "Fall · Die Abholadresse"),
       ("sieben", "Fall · 7 Räder in 3 Wochen"), ("keinr", "Fall · Kein Beschluss beantragt"),
       ("ahnt", "Fall · Helene weiß von nichts?")], [
    flurboden("weiss", BODEN_T, fugen=False),
    *TISCH,
    ficon("tabler", "device-laptop", 470, 702, 420, "weiss", fuell=WEISS, anim="cut"),
    ficon("tabler", "sun", 1780, 170, 120, "weiss", fuell=GELB, anim="cut"),
    pl("Was Helene nicht weiß", 70, 30, "weiss", fill=GELB, size=40),
    ficon("tabler", "clock-2", 1590, 170, 120, beim("mittag", "vierzehn"), fuell=WEISS),
    pl("14 Uhr: Anzeige – gestohlenes E-Bike im Internet", 70, 105, beim("mittag", "vierzehn"), fill=WEISS, size=32),
    ficon("ph", "bicycle", 470, 600, 150, beim("mittag", "E-Bike"), fuell=WEISS),
    pl("Abholadresse: Wohnung von Helene", 70, 172, "abhol", fill=WEISS, size=32),
    ficon("tabler", "home", 720, 700, 90, "abhol", fuell=LILA),
    pl("über dasselbe Konto: 7 teure Räder in 3 Wochen", 70, 239, "sieben", fill=WEISS, size=32),
    *RAEDER,
    *neinz("Um einen Beschluss: nicht bemüht", 312, "keinr", "Bold", 32, x=115),
    ficon("tabler", "building-bank", 1450, 760, 200, beim("keinr", "Bereitschaftsdienst"), fuell=BLAU),
    ficon("tabler", "phone-call", 1690, 760, 130, beim("keinr", "Bereitschaftsdienst"), fuell=WEISS),
    pl("Bereitschaftsdienst bis 21 Uhr erreichbar", 1560, 800, beim("keinr", "Bereitschaftsdienst"), fill=GRUEN, size=30,
       anker="m"),
    pl("kein Hinweis, dass Helene etwas weiß", 70, 372, "ahnt", fill=WEISS, size=32),
    *fig("ST", WX, FU, FH, [("weiss", "ruhig"), ("keinr", "denkt")], erst="pop"),
    ns("Steiger", WX, FU, "weiss", BLAU, d=0.1),
])

# ===========================================================================================================================
# A3 Fall: zurück an der Tür – Helene tritt zur Seite, im Flur steht das E-Bike (Nacht)
# ===========================================================================================================================
TRITT = beim("wider", "tritt")
BIKE_X = 1010
nachtfolie([("wider", "Fall · Helene widerspricht"), ("flur", "Fall · Im Flur: das E-Bike"), ("frage", "Fall · Die Frage")], [
    hart(flurboden("wider", BODEN_N)),
    *deckenlampe(BIKE_X, "wider"),
    hart(wohnungstuer(330, "wider", breite=760)),
    hart(ficon("ph", "bicycle", BIKE_X, F_O + 6, 420, "wider", fuell=WEISS, anim="cut")),
    pl("Helene widerspricht", 70, 30, "wider", fill=HELLROT, size=36),
    pl("… tritt aber zur Seite", 70, 105, TRITT, fill=WEISS, size=32),
    pl("Im Flur: das E-Bike", 70, 180, "flur", fill=WEISS, size=32),
    ring(BIKE_X, F_O - 120, 240, 150, beim("flur", "E-Bike"), bis="frage"),
    pl("Durfte Steiger die Wohnung durchsuchen?", 70, 270, "frage", fill=PINK, size=36),
    pl("Darf das E-Bike als Beweis verwertet werden?", 70, 350, "frage2", fill=PINK, size=36),
    # Helene steht zuerst in der Tür (vor dem Rad), tritt bei „tritt“ nach rechts zur Seite
    *fig("HE", 1330, FU, FH, [("wider", "sorge")], bis=TRITT, erst="cut"),
    *fig("HE", 1600, FU, FH, [(TRITT, "sorge"), ("frage", "denkt")], erst="cut"),
    bis_(ns("Helene", 1330, FU, "wider", LILA), TRITT),
    ns("Helene", 1600, FU, TRITT, LILA),
    *fig("ST", 600, FU, FH, [("wider", "ernst_r"), ("frage", "still_r")], erst="cut"),
    ns("Steiger", 600, FU, "wider", BLAU),
])

# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_151(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 205
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=34, zeilenabstand=1.3)
        els += e; y += 18
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_151("sv", [
    "Dienstag, 23 Uhr: Polizeikommissar Steiger, Ermittlungsperson der Staatsanwaltschaft, klingelt bei Helene. Er sagt, "
    "sie stehe im Verdacht, gestohlene Fahrräder zu verkaufen; wegen Gefahr im Verzug durchsuche er jetzt ihre Wohnung. "
    "Einen Beschluss hat er nicht.",
    "Schon um 14 Uhr hatte ein Mann angezeigt, dass sein gestohlenes E-Bike im Internet angeboten wird; Abholadresse ist die "
    "Wohnung von Helene. Über dasselbe Konto wurden in 3 Wochen 7 teure Räder angeboten. Um einen Beschluss hat sich Steiger "
    "nicht bemüht, obwohl der richterliche Bereitschaftsdienst bis 21 Uhr erreichbar war. Nichts deutet darauf hin, dass "
    "Helene von den Ermittlungen weiß.",
    "Helene widerspricht, tritt aber zur Seite. Im Flur steht das E-Bike.",
], "Durfte Steiger durchsuchen? Darf das E-Bike als Beweis verwertet werden?")

# ===========================================================================================================================
# C 1. Art. 13 GG (Wortlautkarte Abs. 1 und 2)
# ===========================================================================================================================
W13 = ["„(1) Die Wohnung ist unverletzlich.",
       "(2) Durchsuchungen dürfen nur durch den Richter, bei Gefahr",
       "im Verzuge auch durch die in den Gesetzen vorgesehenen anderen",
       "Organe angeordnet und nur in der dort vorgeschriebenen Form",
       "durchgeführt werden.“"]
w13, w13_y = wortlaut(80, 160, 1100, W13, "Art. 13 Abs. 1, 2 GG", "art13", marken=[
    (0, "unverletzlich", beim("art13", "unverletzlich")), (1, "nur durch den Richter", beim("abs2", "Richter")),
    (1, "bei Gefahr", beim("giv", "Gefahr")), (2, "im Verzuge", beim("giv", "Gefahr")),
    (2, "anderen", beim("giv", "anderen")), (3, "Organe", beim("giv", "Organe"))], size=32)
folie([("art13", "1. Art. 13 GG › Die Wohnung ist unverletzlich"), ("abs2", "1. Art. 13 GG › Abs. 2: Richtervorbehalt"),
       ("giv", "1. Art. 13 GG › Abs. 2: Gefahr im Verzuge"), ("regel", "1. Art. 13 GG › Richter: Regel, sonst Ausnahme")],
      rechts_frei([
    *tafel("art13", "1. Art. 13 GG: Unverletzlichkeit der Wohnung", h=w13_y + 300 - 60, size=42),
    *w13,
    blk(110, w13_y + 40, 1040, 80, GELB, "regel", [("Richter: die Regel · ohne Richter: die Ausnahme", "ExtraBold", 34, INK)]),
    zit("BVerfG, Urt. v. 20.2.2001 – 2 BvR 1444/00, Rn. 31 (BVerfGE 103, 142)", 110, w13_y + 135, beim("regel", "Ausnahme")),
    z("Grundrechtsschema: Folge 20", 110, w13_y + 195, "gr020", "Bold", 32),
    *requisit([("art13", ("tabler", "home", 110, LILA), "Art. 13 Abs. 1 GG", GELB),
               ("abs2", ("tabler", "gavel", 110, HOLZ), "Richtervorbehalt", WEISS),
               ("giv", ("tabler", "hourglass", 100, GELB), "Gefahr im Verzuge", WEISS),
               ("regel", ("tabler", "scale", 110, WEISS), "Regel und Ausnahme", GELB)]),
    *stehend("HE", X1, [("art13", "ruhig"), ("giv", "denkt")]),
    *stehend("ST", X2, [("art13", "ernst")]),
]))

# ===========================================================================================================================
# D 2. Ermächtigungsgrundlage: § 102 StPO (Wortlautkarte)
# ===========================================================================================================================
W102 = ["„Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder",
        "der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei",
        "verdächtig ist, kann eine Durchsuchung der Wohnung und anderer",
        "Räume sowie seiner Person und der ihm gehörenden Sachen sowohl",
        "zum Zweck seiner Ergreifung als auch dann vorgenommen werden,",
        "wenn zu vermuten ist, daß die Durchsuchung zur Auffindung von",
        "Beweismitteln führen werde.“"]
w102, w102_y = wortlaut(80, 160, 1100, W102, "§ 102 StPO", "p102", marken=[
    (0, "Täter oder Teilnehmer", beim("verd", "Täter")), (1, "Hehlerei", beim("verd", "Hehlerei")),
    (2, "verdächtig", beim("verd", "verdächtig")), (5, "wenn zu vermuten ist", beim("vermut", "vermuten")),
    (5, "Auffindung von", beim("vermut", "Auffindung")), (6, "Beweismitteln", beim("vermut", "Beweismitteln"))], size=30)
PE = "2. Ermächtigungsgrundlage"
folie([("p102", f"{P} › {PE} › § 102 StPO"), ("verd", f"{P} › {PE} › § 102: Verdächtiger"),
       ("vermut", f"{P} › {PE} › § 102: Auffindevermutung"), ("anf", f"{P} › {PE} › Anfangsverdacht"),
       ("hier102", f"{P} › {PE} › Anfangsverdacht (+)"), ("auff", f"{P} › {PE} › Auffindevermutung (+)")], rechts_frei([
    *tafel("p102", "2. Ermächtigungsgrundlage: § 102 StPO", h=w102_y + 330 - 60, size=44),
    *w102,
    z("Anfangsverdacht: konkret, auf bestimmte Tatsachen gestützt", 110, w102_y + 30, "anf", "Bold", 32),
    zit("BGH, Beschl. v. 6.9.2023 – StB 40/23, Rn. 11", 110, w102_y + 78, beim("anf", "gestützt")),
    *okz("hier: Anzeige, Inserat, Abholadresse", w102_y + 140, "hier102", size=32, x=160),
    *okz("Auffindevermutung: E-Bike in der Wohnung", w102_y + 200, "auff", size=32, x=160),
    *requisit([("p102", ("tabler", "book", 100, WEISS), "§ 102 StPO", GELB),
               ("verd", ("tabler", "user", 100, LILA), "verdächtig: Hehlerei", WEISS),
               ("vermut", ("tabler", "search", 100, WEISS), "Beweismittel vermutet", WEISS),
               ("anf", ("tabler", "file-search", 100, WEISS), "Anfangsverdacht", WEISS),
               ("hier102", ("ph", "bicycle", 150, WEISS), "Anzeige und Inserat", GRUEN),
               ("auff", ("tabler", "home", 110, LILA), "E-Bike in der Wohnung?", GRUEN)]),
    *stehend("HE", FX, [("p102", "ruhig"), ("hier102", "sorge")]),
]))

# ===========================================================================================================================
# E 2. Kontrast: § 103 Abs. 1 S. 1 StPO (Wortlautkarte, Auszug)
# ===========================================================================================================================
W103 = ["„(1) Bei anderen Personen sind Durchsuchungen nur … und nur dann",
        "zulässig, wenn Tatsachen vorliegen, aus denen zu schließen ist,",
        "daß die gesuchte Person, Spur oder Sache sich in den zu",
        "durchsuchenden Räumen befindet. …“"]
w103, w103_y = wortlaut(80, 160, 1100, W103, "§ 103 Abs. 1 S. 1 StPO", "p103", marken=[
    (0, "Bei anderen Personen", beim("p103", "anderen")), (1, "wenn Tatsachen vorliegen", beim("p103b", "Tatsachen")),
    (1, "aus denen zu schließen ist", beim("p103b", "schließen")), (2, "Sache", beim("p103b", "Sache"))], size=30)
folie([("p103", f"{P} › {PE} › § 103: andere Personen"), ("p103b", f"{P} › {PE} › § 103: Tatsachen nötig")], rechts_frei([
    *tafel("p103", "Strenger bei Dritten: § 103 StPO", h=w103_y + 200 - 60, size=44),
    *w103,
    blk(110, w103_y + 40, 1040, 80, LILA, "p103b", [("§ 103: Tatsachen statt bloßer Vermutung", "ExtraBold", 34, INK)]),
    zit("BGH, Beschl. v. 6.9.2023 – StB 40/23, Rn. 14", 110, w103_y + 135, beim("p103b", "befindet")),
    *requisit([("p103", ("tabler", "users", 110, WEISS), "andere Personen", GELB),
               ("p103b", ("tabler", "list-check", 100, WEISS), "Tatsachen nötig", LILA)]),
    *stehend("ST", FX, [("p103", "ruhig"), ("p103b", "denkt")]),
]))

# ===========================================================================================================================
# F 3. Anordnungskompetenz: § 105 Abs. 1 S. 1 StPO (Wortlautkarte)
# ===========================================================================================================================
W105 = ["„(1) Durchsuchungen dürfen nur durch den Richter, bei Gefahr",
        "im Verzug auch durch die Staatsanwaltschaft und ihre",
        "Ermittlungspersonen (§ 152 des Gerichtsverfassungsgesetzes)",
        "angeordnet werden. …“"]
w105, w105_y = wortlaut(80, 160, 1100, W105, "§ 105 Abs. 1 S. 1 StPO", "p105", marken=[
    (0, "nur durch den Richter", beim("p105", "Richter")), (0, "bei Gefahr", beim("p105b", "Gefahr")),
    (1, "im Verzug", beim("p105b", "Gefahr")), (1, "Staatsanwaltschaft", beim("p105b", "Staatsanwaltschaft")),
    (2, "Ermittlungspersonen", beim("p105b", "Ermittlungspersonen"))], size=32)
PA = "3. Anordnungskompetenz"
folie([("p105", f"{P} › {PA} › § 105 Abs. 1 S. 1: Richter"),
       ("p105b", f"{P} › {PA} › bei Gefahr im Verzug: StA, Ermittlungspersonen"),
       ("kompet", f"{P} › {PA} › Steiger: nur bei Gefahr im Verzug")], rechts_frei([
    *tafel("p105", "3. Anordnungskompetenz: § 105 StPO", h=w105_y + 230 - 60, size=44),
    *w105,
    *okz("Steiger: Ermittlungsperson der Staatsanwaltschaft", w105_y + 30, "kompet", size=32, x=160),
    blk(110, w105_y + 100, 1040, 80, GELB, beim("kompet", "ohne"),
        [("ohne Beschluss nur bei Gefahr im Verzug", "ExtraBold", 34, INK)]),
    *requisit([("p105", ("tabler", "gavel", 110, HOLZ), "Richter", GELB),
               ("p105b", ("tabler", "hourglass", 100, GELB), "nur bei Gefahr im Verzug", WEISS),
               ("kompet", ("tabler", "file-x", 100, WEISS), "kein Beschluss", HELLROT)]),
    *stehend("ST", FX, [("p105", "ernst"), ("kompet", "denkt")]),
]))

# ===========================================================================================================================
# G 4. Gefahr im Verzug: BVerfGE 103, 142
# ===========================================================================================================================
PG = "4. Gefahr im Verzug"
RN = 1035                                   # Spalte der Randnummern
GZ = [("eng", 230, [("eng auszulegen", "Bold")], "Rn. 32"),
      ("def", 290, [("nur wenn schon die Einholung der richterlichen", "Bold"),
                    ("Anordnung den Erfolg gefährden würde", "Bold")], "Rn. 34"),
      ("tats", 400, [("Tatsachen des Einzelfalls – keine Spekulation,", "Regular"),
                     ("keine fallunabhängige Vermutung", "Regular")], "Rn. 38"),
      ("versuch", 510, [("regelmäßig zuerst versuchen, einen Richter", "Regular"),
                        ("zu erreichen", "Regular")], "Rn. 40"),
      ("doku", 620, [("Gründe in den Akten dokumentieren", "Regular")], "Rn. 54"),
      ("kontr", 680, [("volle gerichtliche Kontrolle", "Regular")], "Rn. 44")]
els_g = [*tafel("bverfg", "4. Gefahr im Verzug: BVerfGE 103, 142", h=720, size=44),
         zit("BVerfG, Urt. v. 20.2.2001 – 2 BvR 1444/00", 110, 165, "bverfg")]
for i, (c, y, zeilen, rn) in enumerate(GZ):
    els_g.append(z(f"{i + 1}.", 110, y, c, "ExtraBold", 32))
    for j, (t, st) in enumerate(zeilen):
        els_g.append(z(t, 160, y + j * 46, c, st, 32, rechts=RN - 10))
    els_g.append(zit(rn, RN, y + 4, c, rechts=1170))
folie([("bverfg", f"{P} › {PG} › BVerfGE 103, 142"), ("eng", f"{P} › {PG} › eng auszulegen"),
       ("def", f"{P} › {PG} › Erfolg der Durchsuchung gefährdet"), ("tats", f"{P} › {PG} › Tatsachen des Einzelfalls"),
       ("versuch", f"{P} › {PG} › zuerst den Richter versuchen"), ("doku", f"{P} › {PG} › Dokumentation"),
       ("kontr", f"{P} › {PG} › volle gerichtliche Kontrolle")], rechts_frei([
    *els_g,
    *requisit([("bverfg", ("tabler", "building-bank", 120, WEISS), "BVerfG 2001", GELB),
               ("eng", ("tabler", "hourglass", 100, GELB), "eng auszulegen", WEISS),
               ("tats", ("tabler", "list-check", 100, WEISS), "Tatsachen, keine Spekulation", WEISS),
               ("versuch", ("tabler", "phone-call", 100, WEISS), "Richter anrufen", WEISS),
               ("doku", ("tabler", "file-text", 100, WEISS), "in den Akten", WEISS),
               ("kontr", ("tabler", "scale", 110, WEISS), "volle Kontrolle", GELB)]),
    *stehend("HE", X1, [("bverfg", "ruhig"), ("tats", "denkt")]),
    *stehend("ST", X2, [("bverfg", "ernst"), ("versuch", "denkt"), ("doku", "still")]),
]))

# ===========================================================================================================================
# H 4. Selbst herbeigeführte Eile (Zitatkarte BVerfGE 103, 142, Rn. 39)
# ===========================================================================================================================
W39 = ["„Gefahr im Verzug kann im Rechtssinne auch nicht dadurch",
       "entstehen, dass die Strafverfolgungsbehörden ihre tatsächlichen",
       "Voraussetzungen selbst herbeiführen.“"]
w39, w39_y = wortlaut(80, 160, 1100, W39, "BVerfGE 103, 142, Rn. 39", "selbst", marken=[
    (2, "selbst herbeiführen", beim("selbst", "herbeiführen"))], size=32)
folie([("selbst", f"{P} › {PG} › nicht selbst herbeigeführt"), ("zuw", f"{P} › {PG} › nicht abwarten")], rechts_frei([
    *tafel("selbst", "Eile selbst herbeigeführt?", h=w39_y + 230 - 60, size=46),
    *w39,
    *neinz("nicht mit dem Antrag warten, bis ein", w39_y + 40, "zuw", "Bold", 32, x=160),
    z("Beweismittelverlust tatsächlich droht", 160, w39_y + 88, beim("zuw", "Beweismittelverlust"), "Bold", 32),
    *requisit([("selbst", ("tabler", "hourglass", 100, GELB), "selbst herbeigeführt", HELLROT),
               ("zuw", ("tabler", "clock", 100, WEISS), "nicht abwarten", WEISS)]),
    *stehend("ST", FX, [("selbst", "ernst"), ("zuw", "sorge")]),
]))

# ===========================================================================================================================
# I 4. Bereitschaftsdienst: Tagesband 6–21 Uhr (BVerfGE 151, 67)
# ===========================================================================================================================
def tagesband(x0, y0, w, h, cue_tag, cue_nacht):
    """Band 0–24 Uhr: Tageszeit 6–21 Uhr grün (uneingeschränkte Erreichbarkeit), Nachtzeit grau-blau."""
    px = lambda std: x0 + w * std / 24
    els = [karte(x0, y0, w, h, cue_tag, fill=(200, 205, 225, 255), rund=12, schatten=4, rand=4)]
    tag = karte(int(px(6)), y0, int(px(21) - px(6)), h, cue_tag, fill=GRUEN, rund=12, schatten=0, rand=4)
    els.append(tag)
    for std in (0, 6, 21, 24):
        dx = {0: 0, 24: -40}.get(std, -40)
        els.append(z(f"{std} Uhr" if std in (6, 21) else f"{std}", int(px(std)) + dx, y0 + h + 10, cue_tag, "Bold", 28))
    els.append(z("Tag: Richter erreichbar", int(px(7)), y0 + 12, cue_tag, "Bold", 30))
    els.append(z("Nacht", int(px(21.4)), y0 + 12, cue_nacht, "Bold", 30))
    els.append(z("Nacht", int(px(1.2)), y0 + 12, cue_nacht, "Bold", 30))
    return els


PB = "4. Gefahr im Verzug › Bereitschaftsdienst"
folie([("bereit", f"{P} › {PB}"), ("tag", f"{P} › {PB} › tagsüber 6 bis 21 Uhr"),
       ("nacht", f"{P} › {PB} › nachts bei Bedarf")], rechts_frei([
    *tafel("bereit", "Ist ein Richter erreichbar?", h=720, size=46),
    z("Gerichte müssen einen Ermittlungsrichter erreichbar", 110, 175, "bereit", "Bold", 32),
    z("halten – auch durch einen Bereitschaftsdienst", 110, 223, beim("bereit", "Bereitschaftsdienst"), "Bold", 32),
    zit("BVerfGE 103, 142, Rn. 40", 110, 271, beim("bereit", "Bereitschaftsdienst")),
    *tagesband(110, 340, 1040, 70, "tag", "nacht"),
    z("tagsüber, ganzjährig 6 bis 21 Uhr: uneingeschränkt", 110, 480, beim("tag", "Tagsüber"), size=32),
    zit("BVerfG, Beschl. v. 12.3.2019 – 2 BvR 675/14, Rn. 58 (BVerfGE 151, 67)", 110, 528, beim("tag", "ganzjährig")),
    z("nachts: Bereitschaftsdienst, wenn der Bedarf über", 110, 590, "nacht", size=32),
    z("den Ausnahmefall hinausgeht", 110, 638, beim("nacht", "Bedarf"), size=32),
    *requisit([("bereit", ("tabler", "building-bank", 120, BLAU), "Bereitschaftsdienst", GELB),
               ("tag", ("tabler", "sun", 110, GELB), "6 bis 21 Uhr", GRUEN),
               ("nacht", ("tabler", "moon", 100, GELB), "nachts nach Bedarf", WEISS)]),
    *stehend("HE", FX, [("bereit", "ruhig"), ("tag", "denkt")]),
]))

# ===========================================================================================================================
# J 5. Nachtzeit: § 104 StPO (Wortlautkarte Abs. 1 und 3)
# ===========================================================================================================================
W104 = ["„(1) Zur Nachtzeit dürfen die Wohnung, die Geschäftsräume und das",
        "befriedete Besitztum nur in folgenden Fällen durchsucht werden:",
        "1. bei Verfolgung auf frischer Tat,",
        "2. bei Gefahr im Verzug,",
        "3. wenn bestimmte Tatsachen den Verdacht begründen, dass …",
        "auf ein elektronisches Speichermedium zugegriffen werden wird, …",
        "4. zur Wiederergreifung eines entwichenen Gefangenen. …",
        "(3) Die Nachtzeit umfasst den Zeitraum von 21 bis 6 Uhr.“"]
w104, w104_y = wortlaut(80, 160, 1100, W104, "§ 104 Abs. 1, 3 StPO", "p104", marken=[
    (0, "Zur Nachtzeit", beim("p104", "Nachtzeit")), (7, "von 21 bis 6 Uhr", beim("nachtz", "einundzwanzig")),
    (1, "nur in folgenden Fällen", beim("p104b", "Ausnahmefällen")), (2, "auf frischer Tat", beim("p104b", "frischer")),
    (3, "bei Gefahr im Verzug", beim("p104b", "Gefahr")), (6, "entwichenen Gefangenen", beim("p104c", "entwichenen"))],
    size=30)
PN = "5. Nachtzeit, § 104 StPO"
folie([("p104", f"{P} › {PN}"), ("nachtz", f"{P} › {PN} › 21 bis 6 Uhr"), ("p104b", f"{P} › {PN} › nur in Ausnahmefällen"),
       ("ngiv", f"{P} › {PN} › Gefahr im Verzug: Warten bis zum Morgen")], rechts_frei([
    *tafel("p104", "5. Nachtzeit: § 104 StPO", h=w104_y + 210 - 60, size=46),
    *w104,
    blk(110, w104_y + 30, 1040, 120, GELB, "ngiv", [("Gefahr im Verzug hier: schon das Warten", "ExtraBold", 32, INK),
                                                    ("bis zum Morgen gefährdet den Erfolg", "ExtraBold", 32, INK)]),
    zit("BVerfGE 151, 67, Rn. 62", 110, w104_y + 160, beim("ngiv", "Morgen")),
    *requisit([("p104", ("tabler", "moon", 100, GELB), "Nachtzeit", GELB),
               ("nachtz", ("tabler", "clock", 100, WEISS), "21 bis 6 Uhr", WEISS),
               ("p104b", ("tabler", "list-numbers", 100, WEISS), "nur Ausnahmefälle", WEISS),
               ("ngiv", ("tabler", "sun", 110, GELB), "Warten bis zum Morgen?", GELB)]),
    *stehend("HE", X1, [("p104", "ruhig"), ("nachtz", "muede")]),
    *stehend("ST", X2, [("p104", "ernst")]),
]))

# ===========================================================================================================================
# K 6. Lösung
# ===========================================================================================================================
PL = "6. Lösung"
folie([("loes", f"{PL} › Zurück zu Helene"), ("l102", f"{PL} › § 102: Anfangsverdacht (+)"),
       ("lgiv", f"{PL} › Gefahr im Verzug?"), ("lspek", f"{PL} › Gefahr im Verzug › bloße Vermutung"),
       ("lselbst", f"{PL} › Gefahr im Verzug › selbst herbeigeführt"), ("lneg", f"{PL} › Gefahr im Verzug (−)"),
       ("lnacht", f"{PL} › Nachtzeit (−)"), ("lerg", f"{PL} › Durchsuchung rechtswidrig")], rechts_frei([
    *tafel("loes", "Lösung: Durfte Steiger durchsuchen?", h=820, size=44),
    *okz("§ 102: Anfangsverdacht der Hehlerei", 175, "l102", size=32, x=160),
    *okz("verhältnismäßig: wohl ja (7 Räder)", 230, beim("l102", "verhältnismäßig"), size=32, x=160),
    z("Gefahr im Verzug?", 110, 300, "lgiv", "ExtraBold", 34),
    *neinz("„bis morgen weg“: bloße Vermutung", 360, "lspek", size=32, x=160),
    *neinz("Eile selbst herbeigeführt", 420, "lselbst", size=32, x=160),
    z("seit 14 Uhr: über die Staatsanwaltschaft zum Richter", 160, 468, beim("lselbst", "Seit"), size=30),
    blk(110, 530, 1040, 76, HELLROT, "lneg", [("Gefahr im Verzug (−)", "ExtraBold", 34, INK)]),
    *neinz("Nachtzeit: keine Ausnahme nach § 104", 630, "lnacht", size=32, x=160),
    blk(110, 700, 1040, 80, ROT, "lerg", [("Die Durchsuchung war rechtswidrig.", "ExtraBold", 36, INK)]),
    *requisit([("loes", ("tabler", "door", 120, HOLZ), "Helene", LILA),
               ("l102", ("ph", "bicycle", 150, WEISS), "Anfangsverdacht (+)", GRUEN),
               ("lgiv", ("tabler", "hourglass", 100, GELB), "Gefahr im Verzug?", WEISS),
               ("lselbst", ("tabler", "clock-2", 100, WEISS), "seit 14 Uhr", WEISS),
               ("lneg", ("tabler", "hourglass", 100, GELB), "Gefahr im Verzug (−)", HELLROT),
               ("lnacht", ("tabler", "moon", 100, GELB), "Nachtzeit (−)", HELLROT),
               ("lerg", ("tabler", "gavel", 110, HOLZ), "rechtswidrig", HELLROT)]),
    *stehend("HE", X1, [("loes", "ruhig"), ("lspek", "denkt"), ("lerg", "froh")]),
    *stehend("ST", X2, [("loes", "ernst"), ("lneg", "still"), ("lerg", "sorge")]),
]))

# ===========================================================================================================================
# L 7. Verwertungsverbot?
# ===========================================================================================================================
PV = "7. Verwertungsverbot"
folie([("bvv", f"{PV} › für das E-Bike?"), ("nichtj", f"{PV} › Abwägung im Einzelfall"),
       ("bewusst", f"{PV} › bewusste oder grobe Missachtung"), ("stunden", f"{PV} › BGH 2007"),
       ("hier", f"{PV} › bei Steiger: naheliegend"), ("hypo", f"{PV} › kein hypothetischer Beschluss"),
       ("f132", f"{PV} › Widerspruchslösung: Folge 132")], rechts_frei([
    *tafel("bvv", "7. Verwertungsverbot für das E-Bike?", h=840, size=44),
    z("kein Automatismus: Abwägung im Einzelfall", 110, 170, "nichtj", "Bold", 32),
    zit("BGH, Urt. v. 18.4.2007 – 5 StR 546/06, Rn. 20 (BGHSt 51, 285)", 110, 218, beim("nichtj", "abzuwägen")),
    blk(110, 270, 1040, 120, GELB, "bewusst", [("aber: Verwertungsverbot bei bewusster Missachtung", "ExtraBold", 32, INK),
                                               ("oder gleichgewichtig grober Verkennung", "ExtraBold", 32, INK)]),
    zit("BGHSt 51, 285, Leitsatz, Rn. 24, 28", 110, 400, beim("bewusst", "verkannt")),
    z("2007: über Stunden kein Gedanke an einen Richter", 110, 460, "stunden", size=32),
    zit("BGHSt 51, 285, Rn. 26, 28", 110, 508, beim("stunden", "Stunden")),
    *okz("bei Steiger: spricht viel für ein Verwertungsverbot", 570, "hier", "Bold", 32, x=160),
    *neinz("„Richter hätte ohnehin erlassen“: zählt nicht", 640, "hypo", size=32, x=160),
    zit("BGHSt 51, 285, Rn. 29; BGH, Urt. v. 6.10.2016 – 2 StR 46/15, Rn. 26", 160, 688, beim("hypo", "ein")),
    z("Mehr: Folge 132, Widerspruchslösung", 110, 760, "f132", "Bold", 32),
    *requisit([("bvv", ("ph", "bicycle", 150, WEISS), "Beweis verloren?", WEISS),
               ("nichtj", ("tabler", "scale", 110, WEISS), "Abwägung", WEISS),
               ("bewusst", ("tabler", "eye-off", 100, WEISS), "bewusst missachtet?", GELB),
               ("stunden", ("tabler", "clock", 100, WEISS), "über Stunden", WEISS),
               ("hier", ("tabler", "file-x", 100, WEISS), "Verwertungsverbot?", GELB),
               ("hypo", ("tabler", "gavel", 110, HOLZ), "hypothetisch: zählt nicht", HELLROT),
               ("f132", ("tabler", "book", 100, WEISS), "Folge 132", WEISS)]),
    *stehend("HE", X1, [("bvv", "denkt"), ("hier", "ruhig")]),
    *stehend("ST", X2, [("bvv", "ernst"), ("hier", "still")]),
]))

# ===========================================================================================================================
# M Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Trenne sauber"), ("tipp1", "Klausurtipp · Ermächtigungsgrundlage: ob"),
       ("tipp2", "Klausurtipp · § 105: wer"), ("tipp3", "Klausurtipp · Zeitpunkt der Gefahr im Verzug")], [
    *tafel("tipp", "Klausurtipp: Trenne sauber", fill=HELL, h=600),
    warnung_i(150, 225, "tipp", gr=26),
    z("1. Ermächtigungsgrundlage: ob durchsucht", 200, 200, "tipp1", "Bold", 34),
    z("werden darf (§§ 102, 103 StPO)", 200, 250, beim("tipp1", "durchsucht"), size=32),
    z("2. § 105 StPO: wer anordnen darf", 200, 325, "tipp2", "Bold", 34),
    z("3. Gefahr im Verzug ab dem Zeitpunkt, zu dem", 200, 400, "tipp3", "Bold", 34),
    z("die Polizei die Durchsuchung für erforderlich", 200, 450, beim("tipp3", "Polizei"), size=32),
    z("hielt – nicht erst an der Haustür", 200, 500, beim("tipp3", "hielt"), size=32),
    zit("BGHSt 51, 285, Rn. 17", 200, 555, beim("tipp3", "Haustür")),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# N Prüfschema
# ===========================================================================================================================
REIHEN = [("s1", 0, "I. Ermächtigungsgrundlage: § 102 (Verdächtiger), § 103 (Dritte)", True),
          ("s1b", 1, "1. Anfangsverdacht   2. Auffindevermutung", False),
          ("s2", 0, "II. Anordnungskompetenz: grundsätzlich der Richter, § 105 Abs. 1 S. 1", True),
          ("s3", 0, "III. Ohne Beschluss: Gefahr im Verzug", True),
          (beim("s3", "Tatsachen"), 1, "auf Tatsachen gestützt, nicht selbst herbeigeführt, dokumentiert", False),
          ("s4", 0, "IV. Nachtzeit, § 104 StPO", True),
          ("s5", 0, "V. Verhältnismäßigkeit", True),
          ("s6", 0, "Folge: Verwertungsverbot nur bei bewusster oder grober Missachtung", False)]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfschema: Durchsuchung"), 110, 90, "sch", 46),
           z("§§ 102 ff. StPO, Art. 13 Abs. 2 GG", 110, 160, "sch", "Bold", 32, farbe=TEXT, rechts=1800)]
y = 245
for c, ebene, text, fett in REIHEN:
    x = (130, 200)[ebene]
    if c == "s6":
        els_sch.append(karte(110, y - 16, 1700, 84, c, fill=HELLROT, rund=16, schatten=5, rand=4))
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 38 if ebene == 0 else 34, rechts=1800))
    y += {0: 92, 1: 82}[ebene]
assert y <= 990, y
folie([("sch", "Prüfschema"), ("s1", "Prüfschema › I. Ermächtigungsgrundlage"), ("s2", "Prüfschema › II. Anordnungskompetenz"),
       ("s3", "Prüfschema › III. Gefahr im Verzug"), ("s4", "Prüfschema › IV. Nachtzeit"),
       ("s5", "Prüfschema › V. Verhältnismäßigkeit"), ("s6", "Prüfschema › Folge eines Verstoßes")], els_sch)

# ===========================================================================================================================
# O Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Die Durchsuchung ordnet ", 0), ("der Richter", "a"), (" an.", 0)]], 750, 300, 46, "merke",
                {"a": beim("merke", "Richter")}),
    *markertext([[("Gefahr im Verzug ist die ", 0), ("Ausnahme", "b"), (",", 0)],
                 [("und wer die Eile ", 0), ("selbst herbeiführt", "c"), (",", 0)],
                 [("kann sich nicht auf sie berufen.", 0)]], 750, 470, 46, "m2",
                {"b": beim("m2", "Ausnahme"), "c": beim("m2", "selbst")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
