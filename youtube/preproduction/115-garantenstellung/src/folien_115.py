"""Folge 115 · Garantenstellung § 13 StGB: Wann muss ich einen Erfolg verhindern? – Serienstandard Open Peeps (Katzenkönig).
Beispielfall: Winternacht; Karsten sagt der Wirtin zu, den volltrunkenen Wolfgang nach Hause zu bringen (sie ruft deshalb
kein Taxi), führt ihn hinaus, setzt ihn bei -8 °C auf eine Parkbank und geht; eine Passantin findet Wolfgang eine Stunde
später; Unterkühlung, Wolfgang erholt sich.
Szenen laut ../SZENENPLAN.md: A1 Kneipe, A2 Parkbank, A3 eine Stunde später, B Sachverhalt, C Einordnung, D Wortlautkarte
§ 13 Abs. 1 (Auszug), E Funktionenlehre (Tabelle), F im Fall: Familie, Gemeinschaft, G tatsächliche Übernahme,
H Selbstgefährdung (ein Satz, Verweis), I Entsprechung, Vorsatz, Rechtswidrigkeit/Schuld, Ergebnis, J Gegenfall und
§ 323c (Wortlautkarte Auszug), K Klausurtipp (Lexi), L Prüfschema, M Merksatz (Lexi).
Winternacht ruhig und neutral auf Cremegrund: Mond, Laterne mit Lichtkegel, Schneeflocken-Icons; keine Bilder von Leiden;
Alkohol nur als Gläser-Icon in der Kneipe. Zwei Handlungsgeräusche (Kneipentür, Schritte im Schnee; ../geraeusche_herkunft.json).
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz
als eigene Kopie aus Folge 112 (gemeinsame Dateien unverändert); neu: parkbank(), hocker(), fenster().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from ostil import mond, laterne, lichtkegel
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_115/"

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
        if n.startswith(("bild:", "ficon:", "bank")) or "/op_115/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def wortlaut(x, y, w, zeilen, quelle, cue, marken=(), size=32, bis=None):
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 03.10.2026), als Zitat mit Normangabe;
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


# --- eigene Szenenbausteine (programmatisch, Palettenflächen, Tuschekontur) ---------------------------------------------------
def parkbank(cx, boden_, cue, breite=380, sitz=150):
    """Parkbank in Vorderansicht: Lehne, Sitzfläche (Oberkante sitz px über dem Boden), zwei Beine."""
    s = 2
    H_ = sitz + 110
    im = Image.new("RGBA", ((breite + 20) * s, (H_ + 10) * s))
    dr = ImageDraw.Draw(im)
    oben_sitz = H_ - sitz
    for (y0, y1) in ((10, 36), (oben_sitz - 28, oben_sitz - 4), (oben_sitz, oben_sitz + 26)):
        dr.rounded_rectangle((10 * s, y0 * s, (breite + 10) * s, y1 * s), 6 * s, fill=INK)
        dr.rounded_rectangle((14 * s, (y0 + 4) * s, (breite + 6) * s, (y1 - 4) * s), 4 * s, fill=HOLZ)
    for lx in (34, breite - 22):
        dr.rounded_rectangle((lx * s, 36 * s, (lx + 12) * s, (oben_sitz - 28) * s), 4 * s, fill=INK)
        dr.rounded_rectangle((lx * s, (oben_sitz + 26) * s, (lx + 14) * s, H_ * s), 4 * s, fill=INK)
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    return El(im, cx - breite / 2 - 10, boden_ - H_, cue, "fade", 0.0, None, name="bank")


def hocker(cx, boden_, cue, breite=150, sitz=150):
    """Barhocker: Sitzfläche und zwei Beine."""
    s = 2
    im = Image.new("RGBA", ((breite + 12) * s, (sitz + 12) * s))
    dr = ImageDraw.Draw(im)
    dr.rounded_rectangle((6 * s, 6 * s, (breite + 6) * s, 34 * s), 8 * s, fill=INK)
    dr.rounded_rectangle((10 * s, 10 * s, (breite + 2) * s, 30 * s), 6 * s, fill=ROT)
    for lx in (22, breite - 22):
        dr.rounded_rectangle((lx * s, 32 * s, (lx + 12) * s, (sitz + 6) * s), 4 * s, fill=INK)
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    return El(im, cx - breite / 2 - 6, boden_ - sitz - 6, cue, "cut", 0.0, None, name="hocker")


def tisch(cx, unten, cue, w=320, h=240, fill=HOLZ):
    """Kneipentisch in Seitenansicht (Platte, zwei Beine)."""
    s = 2
    im = Image.new("RGBA", ((w + 12) * s, (h + 12) * s))
    dr = ImageDraw.Draw(im)
    o = 6 * s
    dr.rounded_rectangle((o, o, o + w * s, o + 30 * s), 10 * s, fill=fill, outline=INK, width=5 * s)
    for lx in (24, w - 46):
        dr.rectangle((o + lx * s, o + 28 * s, o + (lx + 22) * s, o + h * s), fill=WEISS, outline=INK, width=5 * s)
    im = im.resize((w + 12, h + 12), Image.LANCZOS)
    return El(im, cx - w / 2 - 6, unten - h - 6, cue, "cut", 0.0, None, name="tisch")


def fenster(x, y, w, h, cue):
    """Kneipenfenster mit Nachthimmel (Kreuz, Rahmen)."""
    s = 2
    im = Image.new("RGBA", ((w + 12) * s, (h + 12) * s))
    dr = ImageDraw.Draw(im)
    dr.rounded_rectangle((6 * s, 6 * s, (w + 6) * s, (h + 6) * s), 12 * s, fill=(70, 86, 140, 255), outline=INK, width=6 * s)
    dr.line(((w / 2 + 6) * s, 6 * s, (w / 2 + 6) * s, (h + 6) * s), fill=INK, width=6 * s)
    dr.line((6 * s, (h / 2 + 6) * s, (w + 6) * s, (h / 2 + 6) * s), fill=INK, width=6 * s)
    im = im.resize((w + 12, h + 12), Image.LANCZOS)
    return El(im, x - 6, y - 6, cue, "cut", 0.0, None, name="fenster")


BODEN = 860
FH = 480                                    # stehende Figur
WH = 380                                    # Wolfgang sitzend (Kopfgröße wie stehend)
SITZ = int(WH * 0.37)                       # Sitzhöhe über dem Boden
X1, X2 = 1430, 1730                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
WR = int(FR * WH / FH)                      # Wolfgang sitzend neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"KA": "Karsten", "WO": "Wolfgang", "WI": "Wirtin", "PA": "Passantin"}
NFARBE = {"KA": GRUEN, "WO": BLAU, "WI": LILA, "PA": ROT}


def boden(cue, hart_=False):
    e = linienzug([(40, BODEN), (1880, BODEN)], cue, breite=7, farbe=INK)
    return hart(e) if hart_ else e


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


def stehend(k, x, folge):
    return [*fig(k, x, FB, FR, folge), ns(NAME[k], x, FB, folge[0][0], NFARBE[k], d=0.1)]


def wolfgang_tafel(c0, folge, x=X2):
    """Wolfgang sitzend auf einer kleinen Bank neben der Tafel (blickt nach links zur Tafel)."""
    return [parkbank(x + 10, FB, c0, breite=250, sitz=int(WR * 0.37)), *fig("WO", x, FB, WR, folge, d=0.2),
            ns("Wolfgang", x, FB, c0, BLAU, d=0.3)]


def paar_kw(c0, kf, wf):
    """Tafelszene: Karsten (stehend) und Wolfgang (sitzend) rechts der Tafel."""
    return [*stehend("KA", X1, kf), *wolfgang_tafel(c0, wf)]


def paar_kwi(c0, kf, wif):
    """Tafelszene: Karsten und die Wirtin rechts der Tafel."""
    return [*stehend("KA", X1, kf), *fig("WI", X2, FB, FR, wif, d=0.2), ns("Wirtin", X2, FB, c0, LILA, d=0.3)]


def schnee(cue, punkte):
    """Ruhige Schneeflocken-Icons (Tabler snowflake), statisch."""
    return [hart(ficon("tabler", "snowflake", x, y, br, cue, fuell=WEISS)) if cue == NULL else
            ficon("tabler", "snowflake", x, y, br, cue, fuell=WEISS, anim="cut") for x, y, br in punkte]


# ===========================================================================================================================
# A1 Fall: in der letzten Kneipe
# ===========================================================================================================================
DOOR = 190
WOX, TIX, KAX, WIX = 560, 860, 1170, 1600
RAUS_F = beim("raus", "führt")
HINAUS = beim("raus", "hinaus")
folie([(NULL, "Fall · In der letzten Kneipe"), ("k1", "Fall · Die Zusage"), ("raus", "Fall · Kein Taxi")], [
    hart(boden(NULL)),
    hart(pl("Eine kalte Winternacht", 70, 30, NULL, fill=GELB, size=40)),
    hart(fenster(1300, 90, 250, 190, NULL)),
    hart(mond(1370, 150, 34, NULL)),
    hart(ficon("tabler", "snowflake", 1480, 250, 46, NULL, fuell=WEISS)),
    hart(ficon("tabler", "door-exit", DOOR, BODEN, 190, NULL, fuell=HOLZ)),
    
    pl("seit Stunden durch die Kneipen, jetzt die letzte", 70, 120, beim("kneipe", "letzten"), fill=WEISS, size=34),
    hart(tisch(TIX, BODEN, NULL)),
    hart(ficon("fluent-emoji-flat", "clinking-beer-mugs", TIX, BODEN - 246, 120, NULL)),
    hart(hocker(WOX, BODEN, NULL, sitz=SITZ)),
    # Wolfgang sitzt auf dem Hocker (blickt nach rechts zum Tisch), volltrunken
    *fig("WO", WOX - 20, BODEN, WH, [(NULL, "muede_r"), (beim("voll", "volltrunken"), "doest_r")], erst="cut"),
    hart(ns("Wolfgang", WOX - 20, BODEN, NULL, BLAU)),
    pl("volltrunken", WOX - 20, 400, beim("voll", "volltrunken"), fill=HELLROT, size=32, anker="m", bis="raus"),
    # Karsten (blickt nach rechts zur Wirtin)
    *fig("KA", KAX, BODEN, FH, [(NULL, "ruhig_r"), ("w1", "denkt_r")], bis="k1", erst="cut"),
    *redet("KA_redet_r", KAX, BODEN, FH, "k1", "raus"),
    *fig("KA", KAX, BODEN, FH, [("raus", "ruhig"), (RAUS_F, "ernst")], erst="cut"),
    hart(ns("Karsten", KAX, BODEN, NULL, GRUEN)),
    blase("sprech", 620, 180, "k1", 860, 290, inhalt=["Nicht nötig. Ich bring", "ihn nach Hause."], textsize=36,
          figur=("KA_redet_r", KAX, BODEN, FH), bis="raus"),
    # die Wirtin (blickt nach links zu Karsten)
    *fig("WI", WIX, BODEN, FH, [(NULL, "ruhig"), ("voll", "denkt")], bis="w1", erst="cut"),
    *redet("WI_redet", WIX, BODEN, FH, "w1", "k1"),
    *fig("WI", WIX, BODEN, FH, [("k1", "ruhig"), ("raus", "froh")], erst="cut"),
    hart(ns("Wirtin", WIX, BODEN, NULL, LILA)),
    blase("sprech", 560, 170, "w1", 1340, 240, inhalt=["Soll ich ihm ein", "Taxi rufen?"], textsize=36,
          figur=("WI_redet", WIX, BODEN, FH), bis="k1"),
    # kein Taxi; Karsten führt Wolfgang hinaus (Kneipentür)
    ficon("ph", "taxi", 1790, 330, 120, "raus", fuell=GELB),
    pl("kein Taxi", 1790, 360, "raus", fill=WEISS, size=30, anker="m"),
    pl("Die Wirtin ruft kein Taxi.", 70, 200, "raus", fill=WEISS, size=34),
    szene(pfeil(WOX - 160, 560, DOOR + 110, 560, RAUS_F, breite=8, kopf=26, farbe=INK), "115tuer*", 0.8,
          versatz=round(HINAUS[1] - RAUS_F[1] + 0.25, 3)),
    pl("führt Wolfgang hinaus", 330, 480, RAUS_F, fill=GELB, size=30, anker="m"),
])

# ===========================================================================================================================
# A2 Fall: die Parkbank
# ===========================================================================================================================
BKX = 800                                    # Parkbank
KAB = 1150                                   # Karsten neben der Bank
KAW = 1660                                   # Karsten geht nach rechts weg
BANK_S = beim("bank", "setzt")
BANK_DA = ("bank", round(BANK_S[1] + 1.0, 3))
WEG_DA = ("weg", 1.4)
def park(c):
    """Park in der Winternacht: Boden, Mond, Laterne mit Lichtkegel, ruhige Schneeflocken (für jede Folie neu erzeugt)."""
    lat, kopf = laterne(380, BODEN, 410, c)
    return [boden(c), mond(1730, 140, 50, c), lat, lichtkegel(kopf[0], kopf[1], 150, BODEN, c),
            *schnee(c, [(820, 330, 60), (1010, 190, 56), (1300, 280, 60), (1520, 150, 52)])]
folie([("frost", "Fall · Die Parkbank"), ("weg", "Fall · Karsten geht")], [
    *park("frost"),
    pl("Draußen: -8 °C", 70, 30, "frost", fill=BLAUHELL, size=40),
    ficon("tabler", "temperature-minus", 480, 125, 70, beim("frost", "minus"), fuell=BLAU),
    parkbank(BKX, BODEN, "frost", sitz=SITZ),
    pl("Parkbank", BKX + 120, 420, BANK_S, fill=WEISS, size=30, anker="m", bis="k2"),
    # Wolfgang auf der Bank (dösend, blickt nach rechts zu Karsten)
    peep_voll("WO_doest_r", BKX - 40, BODEN, WH, BANK_S, anim="pop"),
    ns("Wolfgang", BKX - 40, BODEN, BANK_S, BLAU, d=0.1),
    # Karsten kommt mit, steht neben der Bank (blickt nach links zu Wolfgang), dann geht er
    bewegt(peep_voll("KA_ernst", KAB, BODEN, FH, "frost", anim="cut", bis="k2"), "bank", BANK_DA, 360, 0),
    bewegt(ns("Karsten", KAB, BODEN, "frost", GRUEN, anim="cut", bis="weg"), "bank", BANK_DA, 360, 0),
    *redet("KA_ernst", KAB, BODEN, FH, "k2", "weg"),
    blase("sprech", 640, 180, "k2", 1130, 230, inhalt=["Ich muss jetzt los.", "Du schaffst das schon."], textsize=36,
          figur=("KA_ernst", KAB, BODEN, FH), bis="weg"),
    szene(bewegt(peep_voll("KA_ruhig_r", KAW, BODEN, FH, "weg", anim="cut", bis="vors"), "weg", WEG_DA, KAB - KAW, 0),
          "115schritte*", 0.7, 0.05),
    peep_voll("KA_still_r", KAW, BODEN, FH, "vors", anim="cut"),
    bewegt(ns("Karsten", KAW, BODEN, "weg", GRUEN, anim="cut"), "weg", WEG_DA, KAB - KAW, 0),
    pl("Karsten geht.", 70, 120, "weg", fill=WEISS, size=34),
    pl("hält eine Unterkühlung für möglich", 70, 200, "vors", fill=WEISS, size=34),
    pl("und nimmt das in Kauf", 70, 280, beim("vors", "nimmt"), fill=GELB, size=34),
    pl("rechnet nicht mit dem Tod", 70, 360, "tod", fill=WEISS, size=34),
])

# ===========================================================================================================================
# A3 Fall: eine Stunde später
# ===========================================================================================================================
PAX = 1230
STUNDE_DA = ("stunde", 1.2)
folie([("stunde", "Fall · Eine Stunde später"), ("klinik", "Fall · Im Krankenhaus"), ("frage", "Fall · Die Frage")], [
    *park("stunde"),
    pl("1 Stunde später", 70, 30, "stunde", fill=GELB, size=40),
    ficon("tabler", "clock", 500, 125, 70, "stunde", fuell=WEISS),
    parkbank(BKX, BODEN, "stunde", sitz=SITZ),
    *fig("WO", BKX - 40, BODEN, WH, [("stunde", "doest_r"), (beim("klinik", "erholt"), "ruhig_r")], erst="cut"),
    ns("Wolfgang", BKX - 40, BODEN, "stunde", BLAU),
    # die Passantin kommt von rechts (blickt nach links zu Wolfgang)
    bewegt(peep_voll("PA_schreck", PAX, BODEN, FH, "stunde", anim="cut", bis="p1"), "stunde", STUNDE_DA, 420, 0),
    bewegt(ns("Passantin", PAX, BODEN, "stunde", ROT, anim="cut"), "stunde", STUNDE_DA, 420, 0),
    *redet("PA_redet", PAX, BODEN, FH, "p1", "klinik"),
    peep_voll("PA_ruhig", PAX, BODEN, FH, "klinik", anim="cut"),
    blase("sprech", 640, 180, "p1", 1180, 230, inhalt=["Hallo, hören Sie mich?", "Ich rufe den Rettungsdienst."],
          textsize=34, figur=("PA_redet", PAX, BODEN, FH), bis="klinik"),
    ficon("tabler", "phone-call", PAX + 190, 640, 70, beim("p1", "rufe"), fuell=WEISS),
    # Krankenhaus: Unterkühlung, Wolfgang erholt sich
    ficon("fluent-emoji-flat", "ambulance", 1700, BODEN, 230, beim("klinik", "Krankenhaus")),
    pl("Krankenhaus: Unterkühlung", 70, 120, beim("klinik", "Unterkühlung"), fill=BLAUHELL, size=34, bis="frage"),
    pl("Wolfgang erholt sich.", 70, 200, beim("klinik", "erholt"), fill=GRUEN, size=34, bis="frage"),
    pl("Nur gegangen: Unterkühlung verhindern müssen?", 70, 120, "frage", fill=WEISS, size=34),
    pl("War Karsten Garant?", 70, 205, "frage2", fill=PINK, size=36),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_115(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=34, zeilenabstand=1.30)
        els += e; y += 18
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_115("sv", [
    "In einer kalten Winternacht ziehen Karsten und sein Freund Wolfgang seit Stunden durch die Kneipen; jetzt sitzen sie "
    "in der letzten. "
    "Wolfgang ist volltrunken und kann kaum noch stehen. Die Wirtin fragt, ob sie ihm ein Taxi rufen soll. Karsten "
    "antwortet: „Nicht nötig. Ich bring ihn nach Hause.“ Die Wirtin ruft daraufhin kein Taxi.",
    "Karsten führt Wolfgang hinaus. Draußen sind es -8 °C. Nach ein paar Metern setzt er ihn auf eine Parkbank und geht. "
    "Er hält es für möglich, dass Wolfgang sich eine Unterkühlung holt, und nimmt das in Kauf; mit seinem Tod rechnet "
    "er nicht.",
    "Eine Stunde später findet eine Passantin Wolfgang und ruft den Rettungsdienst. Im Krankenhaus stellen die Ärzte eine "
    "Unterkühlung fest. Wolfgang erholt sich.",
], "Hat sich Karsten strafbar gemacht?")

# ===========================================================================================================================
# C Einordnung: Unterlassen, Delikt, Schema-Verweis, offene Garantenstellung
# ===========================================================================================================================
PK = "A. Körperverletzung durch Unterlassen"
PG = f"{PK} › Garantenstellung"
folie([("vorab", "Vorab · Tun oder Unterlassen"), ("delikt", f"{PK}, §§ 223, 13 StGB"),
       ("kurz", f"{PK} › Erfolg und Quasikausalität"), ("heute", f"{PK} › Garantenstellung?")], rechts_frei([
    *tafel("vorab", "Tun oder Unterlassen?"),
    z("Vorwurf: nicht das Hinsetzen auf die Bank,", 110, 180, "vorab", "Bold", 34),
    z("sondern das Zurücklassen", 110, 228, beim("vorab", "zurückgelassen"), "Bold", 34),
    *okz("Schwerpunkt der Vorwerfbarkeit: Unterlassen", 290, beim("vorab", "Schwerpunkt"), "Bold", 34, x=160),
    zit("BGH, Beschl. v. 17.3.2022 – 2 StR 157/21, Rn. 13", 160, 340, beim("vorab", "Unterlassen")),
    blk(110, 395, 1040, 80, GELB, "delikt", [("Körperverletzung durch Unterlassen, §§ 223, 13 StGB", "ExtraBold", 34, INK)]),
    z("Schema: Video „Unechtes Unterlassen“", 110, 500, "s071", "Bold", 32, farbe=TEXT),
    *okz("Erfolg: Unterkühlung = Gesundheitsschädigung", 565, beim("kurz", "Unterkühlung"), "Bold", 32, x=160),
    zit("BGH, Beschl. v. 26.2.2015 – 4 StR 548/14, Rn. 4", 160, 612, beim("kurz", "Gesundheitsschädigung")),
    *okz("Quasikausalität: heimgebracht, keine Unterkühlung", 660, beim("kurz", "hätte"), "Bold", 32, x=160),
    blk(110, 745, 1040, 80, HELLROT, "heute", [("Offen: die Garantenstellung", "ExtraBold", 36, INK)]),
    *requisit([("vorab", ("tabler", "armchair", 100, HOLZ), "Bank oder Zurücklassen?", WEISS),
               ("delikt", ("tabler", "scale", 100, GELB), "§§ 223, 13 StGB", GELB),
               ("kurz", ("tabler", "temperature-minus", 90, BLAU), "Unterkühlung", BLAUHELL),
               ("heute", ("tabler", "shield", 100, WEISS), "Garant?", PINK)]),
    *paar_kw("vorab", [("vorab", "ruhig"), ("heute", "denkt")], [("vorab", "doest"), ("kurz", "ruhig")]),
]))

# ===========================================================================================================================
# D Wortlautkarte § 13 Abs. 1 (Auszug)
# ===========================================================================================================================
W13 = ["„Wer es unterläßt, einen Erfolg abzuwenden, der zum",
       "Tatbestand eines Strafgesetzes gehört, ist nach diesem",
       "Gesetz nur dann strafbar, wenn er rechtlich dafür",
       "einzustehen hat, daß der Erfolg nicht eintritt, …“"]
w13, w13_y = wortlaut(80, 180, 1100, W13, "§ 13 Abs. 1 StGB (Auszug)", "p13", marken=[
    (0, "einen Erfolg abzuwenden", beim("p13", "Erfolg")), (2, "rechtlich dafür", beim("einst", "rechtlich")),
    (3, "einzustehen hat", beim("einst", "einzustehen"))], size=34)
folie([("p13", f"{PG} › § 13 Abs. 1 StGB"), ("einst", f"{PG} › rechtlich einstehen"),
       ("woher", f"{PG} › Woraus folgt die Pflicht?")], rechts_frei([
    *tafel("p13", "Die Norm: § 13 Abs. 1 StGB"),
    *w13,
    *neinz("bloß moralische Pflicht: genügt nicht", w13_y + 50, "moral", "Bold", 36, x=160),
    blk(110, w13_y + 140, 1040, 80, LILA, "woher", [("Woraus die Pflicht folgt, sagt das Gesetz nicht", "ExtraBold", 34, INK)]),
    *requisit([("p13", ("tabler", "book", 100, WEISS), "§ 13 Abs. 1 StGB", GELB),
               ("einst", ("tabler", "shield", 100, BLAU), "rechtlich einstehen", WEISS),
               ("woher", ("tabler", "help-circle", 100, LILA), "Woraus?", LILA)]),
    *stehend("KA", FX, [("p13", "ruhig"), ("moral", "denkt")]),
]))

# ===========================================================================================================================
# E Funktionenlehre (Tabelle)
# ===========================================================================================================================
LX0, RX0, CW = 110, 640, 510
folie([("funk", f"{PG} › Funktionenlehre"), ("besch", f"{PG} › Beschützergaranten"),
       ("ueberw", f"{PG} › Überwachergaranten")], rechts_frei([
    *tafel("funk", "Funktionenlehre"),
    z("Garantenstellungen nach ihrer Funktion (Lehre)", 110, 172, "funk", "Bold", 32, farbe=TEXT),
    karte(LX0, 235, CW, 520, "besch", fill=HELLGRUEN, rund=18, schatten=6, rand=4),
    z("Beschützergarant", LX0 + 25, 250, "besch", "ExtraBold", 36, rechts=LX0 + CW - 10),
    z("ein Rechtsgut schützen", LX0 + 25, 298, beim("besch", "Rechtsgut"), "Bold", 30, farbe=TEXT, rechts=LX0 + CW - 10),
    z("• familiäre Verbundenheit", LX0 + 25, 380, "fam", size=30, rechts=LX0 + CW - 10),
    z("• enge Lebens- oder", LX0 + 25, 460, "gem", size=30, rechts=LX0 + CW - 10),
    z("   Gefahrengemeinschaft", LX0 + 25, 502, "gem", size=30, rechts=LX0 + CW - 10),
    z("• tatsächliche Übernahme", LX0 + 25, 582, "ueb", size=30, rechts=LX0 + CW - 10),
    z("   des Schutzes", LX0 + 25, 624, "ueb", size=30, rechts=LX0 + CW - 10),
    karte(RX0, 235, CW, 520, "ueberw", fill=LILAHELL, rund=18, schatten=6, rand=4),
    z("Überwachergarant", RX0 + 25, 250, "ueberw", "ExtraBold", 36, rechts=RX0 + CW - 10),
    z("eine Gefahr im Zaum halten", RX0 + 25, 298, beim("ueberw", "Gefahr"), "Bold", 30, farbe=TEXT, rechts=RX0 + CW - 10),
    z("• pflichtwidriges", RX0 + 25, 380, "ing", size=30, rechts=RX0 + CW - 10),
    z("   Vorverhalten: Ingerenz", RX0 + 25, 422, "ing", size=30, rechts=RX0 + CW - 10),
    z("• Verantwortung für eine", RX0 + 25, 502, "quelle", size=30, rechts=RX0 + CW - 10),
    z("   Gefahrenquelle", RX0 + 25, 544, "quelle", size=30, rechts=RX0 + CW - 10),
    z("• Aufsicht über andere", RX0 + 25, 624, "aufs", size=30, rechts=RX0 + CW - 10),
    z("   Personen", RX0 + 25, 666, "aufs", size=30, rechts=RX0 + CW - 10),
    zit("vgl. BGH, Urt. v. 11.9.2019 – 2 StR 563/18, Rn. 12, 19, 27", 110, 790, beim("ueberw", "Gefahr")),
    *requisit([("funk", ("tabler", "list-details", 100, WEISS), "Funktionenlehre", WEISS),
               ("besch", ("tabler", "shield-heart", 100, GRUEN), "Beschützergarant", HELLGRUEN),
               ("ueberw", ("tabler", "alert-triangle", 100, GELB), "Überwachergarant", LILAHELL),
               ("aufs", ("tabler", "eye", 100, WEISS), "Aufsicht", LILAHELL)]),
    *stehend("KA", FX, [("funk", "ruhig"), ("ueberw", "denkt")]),
]))

# ===========================================================================================================================
# F Im Fall: Familie? Gefahrengemeinschaft?
# ===========================================================================================================================
folie([("fam2", f"{PG} › Familie?"), ("zech", f"{PG} › Gefahrengemeinschaft?")], rechts_frei([
    *tafel("fam2", "Im Fall: Familie? Gemeinschaft?"),
    *neinz("familiäre Verbundenheit: Wolfgang ist Freund, nicht Familie", 190, "fam2", "Bold", 32, x=160),
    *neinz("Gefahrengemeinschaft: bloßes Zechen reicht nicht", 280, beim("zech", "reicht"), "Bold", 32, x=160),
    z("BGH: abzugrenzen sind lose Zusammenschlüsse,", 160, 360, beim("zech", "grenzt"), size=32),
    z("etwa von Zechkumpanen", 160, 405, beim("zech", "Zechkumpane"), size=32),
    z("dort fehlt regelmäßig die Übernahme", 160, 475, "zech2", size=32),
    z("einer Beistandspflicht", 160, 520, beim("zech2", "Beistandspflicht"), size=32),
    zit("BGH, Urt. v. 11.9.2019 – 2 StR 563/18, Rn. 12, 14", 160, 575, beim("zech", "grenzt")),
    *requisit([("fam2", ("tabler", "home-heart", 100, WEISS), "Familie? nein", WEISS),
               ("zech", ("fluent-emoji-flat", "clinking-beer-mugs", 120, None), "Zechkumpane", WEISS),
               ("zech2", ("tabler", "users", 110, BLAU), "lose Runde", HELLROT)]),
    *paar_kw("fam2", [("fam2", "ruhig"), ("zech2", "denkt")], [("fam2", "ruhig")]),
]))

# ===========================================================================================================================
# G Im Fall: tatsächliche Übernahme
# ===========================================================================================================================
folie([("ueb2", f"{PG} › tatsächliche Übernahme"), ("zusage", f"{PG} › Übernahme: Zusage"),
       ("vertr", f"{PG} › Übernahme: Vertrauen der Wirtin"), ("hinaus", f"{PG} › Übernahme: Herausführen"),
       ("mehr", f"{PG} › mehr als kurze Hilfe"), ("garant", f"{PG} › Beschützergarant (+)"),
       ("ing2", f"{PG} › Ingerenz offen")], rechts_frei([
    *tafel("ueb2", "Tatsächliche Übernahme"),
    zit("BGH, Urt. v. 17.7.2009 – 5 StR 394/08, Rn. 23, 25", 110, 165, beim("ueb2", "Übernahme")),
    *okz("Zusage an die Wirtin: „Ich bring ihn nach Hause.“", 215, beim("zusage", "zugesagt"), "Bold", 32, x=160),
    *okz("Vertrauen: Die Wirtin ruft kein Taxi.", 280, beim("vertr", "Vertrauen"), "Bold", 32, x=160),
    *okz("Herausführen: aus der warmen Kneipe in die Kälte", 345, beim("hinaus", "führt"), "Bold", 32, x=160),
    z("mehr als eine kurze Hilfe, die noch niemanden", 160, 425, "mehr", size=32),
    z("zum Garanten macht: Lage wesentlich verändert", 160, 470, beim("mehr", "Karsten"), size=32),
    zit("vgl. 2 StR 563/18, Rn. 17 f.; BGH, Urt. v. 31.1.2002 – 4 StR 289/01, Rn. 27", 160, 520, beim("mehr", "wesentlich")),
    blk(110, 580, 1040, 120, GRUEN, "garant", [("Karsten: Beschützergarant", "ExtraBold", 36, INK),
                                              ("kraft tatsächlicher Übernahme", "ExtraBold", 36, INK)]),
    z("Ingerenz: kann offenbleiben", 110, 730, "ing2", "Bold", 32, farbe=TEXT),
    *requisit([("ueb2", ("tabler", "shield", 100, WEISS), "Übernahme?", WEISS),
               ("zusage", ("tabler", "heart-handshake", 100, GELB), "Zusage", GELB),
               ("vertr", ("ph", "taxi", 130, WEISS), "kein Taxi", WEISS),
               ("hinaus", ("tabler", "door-exit", 100, HOLZ), "in die Kälte", BLAUHELL),
               ("garant", ("tabler", "shield-check", 100, GRUEN), "Beschützergarant", GRUEN)]),
    *paar_kwi("ueb2", [("ueb2", "ruhig"), ("mehr", "sorge"), ("garant", "still")],
              [("ueb2", "ruhig"), ("vertr", "froh"), ("mehr", "denkt")]),
]))

# ===========================================================================================================================
# H Selbst betrunken? (ein Satz, Verweis auf die Folge zur Selbstgefährdung)
# ===========================================================================================================================
folie([("selbst", f"{PG} › selbst betrunken?")], rechts_frei([
    *tafel("selbst", "Selbst betrunken?"),
    z("Wolfgang hat sich selbst betrunken:", 110, 190, "selbst", "Bold", 34),
    *okz("ändert nichts an der Garantenstellung", 255, beim("selbst", "ändert"), "Bold", 34, x=160),
    z("Wird daraus eine konkrete Gefahr,", 160, 335, beim("selbst", "Wird"), size=34),
    z("muss der Garant handeln.", 160, 383, beim("selbst", "muss"), "Bold", 34),
    zit("BGH, Beschl. v. 5.8.2015 – 1 StR 328/15, Rn. 18", 160, 440, beim("selbst", "muss")),
    blk(110, 520, 1040, 80, LILA, beim("selbst", "Mehr"), [("Mehr: Video „Eigenverantwortliche Selbstgefährdung“",
                                                          "ExtraBold", 32, INK)]),
    *requisit([("selbst", ("fluent-emoji-flat", "clinking-beer-mugs", 120, None), "selbst getrunken", WEISS),
               (beim("selbst", "Wird"), ("tabler", "temperature-minus", 90, BLAU), "konkrete Gefahr", HELLROT)]),
    *paar_kw("selbst", [("selbst", "ruhig")], [("selbst", "doest")]),
]))

# ===========================================================================================================================
# I Entsprechung, Vorsatz, Rechtswidrigkeit und Schuld, Ergebnis
# ===========================================================================================================================
folie([("entspr", f"{PK} › Entsprechung"), ("vors2", f"{PK} › Vorsatz"), ("rw", f"{PK} › Rechtswidrigkeit und Schuld"),
       ("erg", "Ergebnis · Karsten strafbar, §§ 223, 13 StGB"), ("milder", "Strafmilderung · § 13 Abs. 2 StGB")],
      rechts_frei([
    *tafel("entspr", "Rest der Prüfung und Ergebnis"),
    *okz("Entsprechung: reines Erfolgsdelikt, unproblematisch", 190, beim("entspr", "regelmäßig"), "Bold", 32, x=160),
    *okz("Vorsatz: kennt seine Zusage, nimmt", 260, "vors2", "Bold", 32, x=160),
    z("die Unterkühlung in Kauf (bedingter Vorsatz)", 160, 305, beim("vors2", "nimmt"), "Bold", 32),
    *okz("keine Rechtfertigung, keine Entschuldigung", 375, "rw", "Bold", 32, x=160),
    z("Heimbringen war zumutbar.", 160, 420, beim("rw", "Wolfgang"), size=32),
    blk(110, 500, 1040, 120, GRUEN, "erg", [("Karsten: jedenfalls strafbar wegen", "ExtraBold", 36, INK),
                                           ("Körperverletzung durch Unterlassen", "ExtraBold", 36, INK)]),
    z("Strafmilderung möglich: § 13 Abs. 2 StGB", 110, 660, "milder", "Bold", 32),
    *requisit([("entspr", ("tabler", "scale", 100, WEISS), "Entsprechung", WEISS),
               ("vors2", ("tabler", "bulb", 100, GELB), "bedingter Vorsatz", GELB),
               ("rw", ("tabler", "shield-off", 100, WEISS), "keine Rechtfertigung", WEISS),
               ("erg", ("tabler", "gavel", 100, HOLZ), "strafbar", GRUEN),
               ("milder", ("tabler", "scale", 100, GELB), "kann gemildert werden", WEISS)]),
    *stehend("KA", FX, [("entspr", "ruhig"), ("vors2", "sorge"), ("erg", "still")]),
]))

# ===========================================================================================================================
# J Gegenfall und Abgrenzung § 323c (Wortlautkarte, Auszug)
# ===========================================================================================================================
W323 = ["„Wer bei Unglücksfällen oder gemeiner Gefahr oder Not",
        "nicht Hilfe leistet, obwohl dies erforderlich und ihm den",
        "Umständen nach zuzumuten, … möglich ist, wird mit",
        "Freiheitsstrafe bis zu einem Jahr oder mit Geldstrafe bestraft.“"]
w323, w323_y = wortlaut(80, 335, 1100, W323, "§ 323c Abs. 1 StGB (Auszug)", "p323", marken=[
    (0, "Unglücksfällen", beim("p323", "Unglücksfällen")), (1, "erforderlich", beim("p323", "erforderlich")),
    (2, "zuzumuten", beim("p323", "zumutbar"))], size=31)
folie([("gegen", "Gegenfall · nur gezecht, nichts zugesagt"), ("p323", "Abgrenzung › unterlassene Hilfeleistung, § 323c StGB"),
       ("echt", "Abgrenzung › echtes Unterlassungsdelikt")], rechts_frei([
    *tafel("gegen", "Gegenfall: nur gezecht", fill=LILAHELL),
    z("nur mitgetrunken, nichts zugesagt,", 110, 175, "gegen", "Bold", 32),
    z("sieht Wolfgang später auf der Bank", 110, 220, beim("gegen", "sieht"), "Bold", 32),
    *neinz("kein Garant", 270, "kein", "ExtraBold", 34, x=160),
    *w323,
    z("echtes Unterlassungsdelikt: bestraft das Nichthelfen", 110, w323_y + 25, "echt", "Bold", 32),
    z("selbst, nicht die Unterkühlung", 110, w323_y + 70, beim("echt", "selbst"), "Bold", 32),
    zit("vgl. BGH, Urt. v. 11.9.2019 – 2 StR 563/18, Rn. 17", 110, w323_y + 120, beim("echt", "Nichthelfen")),
    *requisit([("gegen", ("fluent-emoji-flat", "clinking-beer-mugs", 120, None), "nur gezecht", WEISS),
               ("kein", ("tabler", "shield-x", 100, WEISS), "kein Garant", HELLROT),
               ("p323", ("tabler", "users", 110, BLAU), "Jedermannspflicht", LILA),
               ("echt", ("tabler", "first-aid-kit", 100, ROT), "Nichthelfen", WEISS)]),
    *paar_kw("gegen", [("gegen", "ruhig"), ("p323", "denkt")], [("gegen", "doest")]),
]))

# ===========================================================================================================================
# K Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Garantenstellung begründen"), ("tipp3", "Klausurtipp · Aussetzung, § 221 StGB")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Garantenstellung nicht nur nennen,", 200, 200, beim("tipp", "Nenne"), "Bold", 36),
    z("sondern mit den Tatsachen begründen", 200, 250, beim("tipp", "begründe"), size=34),
    z("Hier: Zusage, Vertrauen der Wirtin,", 200, 330, "tipp2", size=34),
    z("Herausführen in die Kälte", 200, 378, beim("tipp2", "Herausführen"), size=34),
    linienzug([(130, 455), (1130, 455)], "tipp3", breite=3),
    z("Denk an die Aussetzung, § 221 StGB:", 200, 485, "tipp3", "Bold", 36),
    z("„… ihm sonst beizustehen verpflichtet ist …“", 200, 545, beim("tipp3", "beizustehen"), size=34),
    zit("§ 221 Abs. 1 Nr. 2 StGB; vgl. BGH, Urt. v. 29.9.2021 – 2 StR 491/20, Rn. 27", 200, 600,
        beim("tipp3", "beizustehen")),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# L Prüfschema
# ===========================================================================================================================
REIHEN = [("s1", 0, "I. Tatbestand", True),
          ("s1a", 1, "1. objektiv:", True),
          ("s1a", 2, "Erfolg, Nichtvornahme trotz Möglichkeit, Quasikausalität", False),
          ("s1d", 2, "Garantenstellung, § 13 Abs. 1 StGB", True),
          ("s1d1", 3, "• Beschützergarant: Familie, Gemeinschaft, tatsächliche Übernahme", False),
          ("s1d2", 3, "• Überwachergarant: Ingerenz, Gefahrenquelle, Aufsicht", False),
          ("s1e", 2, "Entsprechung", False),
          ("s1f", 1, "2. subjektiv: Vorsatz", True),
          ("s2", 0, "II. Rechtswidrigkeit  ·  III. Schuld", True),
          ("s4", 0, "IV. Strafmilderung, § 13 Abs. 2 StGB", True)]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfschema: Körperverletzung durch Unterlassen, §§ 223, 13 StGB"), 110, 90, "sch", 46)]
y = 190
for c, ebene, text, fett in REIHEN:
    x = (130, 200, 270, 330)[ebene]
    if c == "s1d":
        els_sch.append(karte(250, y - 18, 1570, 213, c, fill=HELLGRUEN, rund=16, schatten=5, rand=4))
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 36 if ebene == 0 else 33, rechts=1800))
    y += {0: 84, 1: 66, 2: 66, 3: 62}[ebene]
    if c == "s1d2":
        y += 24
assert y <= 970, y
folie([("sch", "Prüfschema"), ("s1", "Prüfschema › I. Tatbestand"), ("s1d", "Prüfschema › I. Garantenstellung"),
       ("s1e", "Prüfschema › I. Entsprechung, Vorsatz"), ("s2", "Prüfschema › II. und III."),
       ("s4", "Prüfschema › IV. Strafmilderung")], els_sch)

# ===========================================================================================================================
# M Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Gemeinsames Trinken allein", 0)], [("macht ", 0), ("niemanden zum Garanten", "a"), (".", 0)]],
                750, 285, 42, "merke", {"a": beim("merke", "niemanden")}),
    *markertext([[("Wer aber den Schutz eines Hilflosen", 0)], [("tatsächlich übernimmt", "b"), (", muss ihn", 0)],
                 [("auch zu Ende bringen.", 0)]], 750, 470, 42, "m2", {"b": beim("m2", "tatsächlich")}),
    *markertext([[("Sonst bleibt nur die", 0)], [("Jedermannspflicht", "c"), (" aus § 323c StGB.", 0)]], 750, 720, 42, "m3",
                {"c": beim("m3", "Jedermannspflicht")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
