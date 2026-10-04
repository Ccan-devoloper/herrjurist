"""Folge 174 · Pfändungs- und Überweisungsbeschluss: Konto- und Lohnpfändung – Serienstandard Open Peeps (Katzenkönig).
Übungsfall: Tischler Herr Dorfmann (Gläubiger), Frau Kästner (Schuldnerin, angestellt bei einem großen Arbeitgeber, fiktives
Autowerk ohne Namen und Marke), die Personalleiterin (Drittschuldner Arbeitgeber), der Bankberater (spricht nicht).
Szenen laut ../SZENENPLAN.md; Belege je Aussage in ../RECHTSSTAND.md. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/
fig/ns/okz/neinz/requisit/stehend/paar als eigene Kopie aus Folge 153 (gemeinsame Dateien unverändert); neu: kueche(),
schalter(), lohnbalken(); theke-/tisch-/zeitstrahl-Bausteine aus 153 übernommen. Keine Logos, keine echten Firmennamen.
Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from ostil import titel, karte, pille
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_174/"

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
        if n.startswith(("bild:", "ficon:", "bank")) or "/op_174/" in n:
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



# --- eigene Szenenbausteine (programmatisch, Palettenflächen, Tuschekontur) ---------------------------------------------------
def _flaeche(w, h):
    s = 2
    im = Image.new("RGBA", ((w + 12) * s, (h + 12) * s))
    return im, ImageDraw.Draw(im), s






def tisch(x, breite, cue):
    """Schreibtisch aus Grundformen (Holzplatte, zwei Beine) auf dem Boden."""
    im, dr, s = _flaeche(breite, 210)
    o = 6 * s
    dr.rounded_rectangle((o, o, o + breite * s, o + 34 * s), 8 * s, fill=HOLZ, outline=INK, width=5 * s)
    for xx in (o + 30 * s, o + (breite - 52) * s):
        dr.rectangle((xx, o + 34 * s, xx + 22 * s, o + 210 * s), fill=HOLZ, outline=INK, width=5 * s)
    im = im.resize((breite + 12, 222), Image.LANCZOS)
    return hart(El(im, x, BODEN - 216, cue, "cut", 0.0, None, name="tisch"))




BODEN = 860
FH = 440                                    # stehende Figur in der Fallszene
X1, X2 = 1430, 1730                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"DO": "Herr Dorfmann", "KA": "Frau Kästner", "PL": "Personalleiterin", "BB": "Bankberater"}
NFARBE = {"DO": GELB, "KA": PINK, "PL": GRUEN, "BB": BLAUHELL}
DUNKEL = (58, 58, 72, 255)


def boden(cue):
    return hart(linienzug([(40, BODEN), (1880, BODEN)], cue, breite=7, farbe=INK))
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
    return rechts_frei([*fig(k, x, FB, FR, folge, bis=bis), bis_(ns(NAME[k], x, FB, folge[0][0], NFARBE[k], d=0.1), bis)])


def paar(a, af, b, bf):
    """Tafelszene: zwei Figuren rechts der Tafel (beide blicken nach links zur Tafel)."""
    return [*stehend(a, X1, af), *stehend(b, X2, bf)]


def zeitstrahl(x0, x1, y, cue, punkte):
    """Zeitstrahl mit Marken: punkte = [(x, cue, text, fill, oben?)]; Linie erscheint mit cue."""
    els = [linienzug([(x0, y), (x1, y)], cue, breite=6, farbe=INK), pfeil(x1 - 40, y, x1 + 10, y, cue, breite=6, kopf=24)]
    for x, c, text, fill, oben in punkte:
        els.append(linienzug([(x, y - 22), (x, y + 22)], c, breite=6, farbe=INK))
        els.append(pl(text, x, y - 92 if oben else y + 40, c, fill=fill, size=28, anker="m"))
    return els



# --- eigene Szenenbausteine Folge 174 (programmatisch, Palettenflächen, Tuschekontur) ------------------------------------------
def kueche(x0, x1, cue):
    """Einbauküche aus Grundformen: Unterschränke (Holzfronten mit Griffen), helle Arbeitsplatte, Hängeschränke."""
    w = x1 - x0
    hu, ho, yo0, yo1 = 220, BODEN - 520, 0, 120          # Unterschrank-Höhe, Oberkante Hängeschrank (absolut), Höhe
    im, dr, s = _flaeche(w, BODEN - ho)
    o = 6 * s
    H_ = BODEN - ho
    # Hängeschränke
    n = 3
    for k in range(n):
        a = o + int(w * k / n) * s
        b = o + int(w * (k + 1) / n) * s
        dr.rounded_rectangle((a, o, b, o + yo1 * s), 6 * s, fill=HOLZ, outline=INK, width=5 * s)
        dr.rounded_rectangle(((a + b) // 2 - 14 * s, o + (yo1 - 26) * s, (a + b) // 2 + 14 * s, o + (yo1 - 18) * s), 3 * s, fill=INK)
    # Unterschränke
    top = o + (H_ - hu) * s
    for k in range(n):
        a = o + int(w * k / n) * s
        b = o + int(w * (k + 1) / n) * s
        dr.rectangle((a, top + 30 * s, b, o + H_ * s), fill=HOLZ, outline=INK, width=5 * s)
        dr.rounded_rectangle(((a + b) // 2 - 22 * s, top + 60 * s, (a + b) // 2 + 22 * s, top + 70 * s), 3 * s, fill=INK)
    dr.rounded_rectangle((o - 10 * s, top, o + (w + 10) * s, top + 34 * s), 8 * s, fill=WEISS, outline=INK, width=5 * s)
    im = im.resize((w + 12, H_ + 12), Image.LANCZOS)
    return hart(El(im, x0 - 6, ho - 6, cue, "cut", 0.0, None, name="kueche"))


def schalter(x0, x1, cue, hoehe=250):
    """Bankschalter aus Grundformen: helle Front mit zwei blauen Feldern, Platte Weiß."""
    w = x1 - x0
    im, dr, s = _flaeche(w, hoehe)
    o = 6 * s
    dr.rectangle((o, o + 30 * s, o + w * s, o + hoehe * s), fill=BLAUHELL, outline=INK, width=5 * s)
    for k in range(2):
        a = o + int(w * (0.08 + k * 0.47)) * s
        dr.rounded_rectangle((a, o + 62 * s, a + int(w * 0.37) * s, o + (hoehe - 36) * s), 10 * s, fill=WEISS, outline=INK,
                             width=3 * s)
    dr.rounded_rectangle((o - 14 * s, o, o + (w + 14) * s, o + 34 * s), 8 * s, fill=WEISS, outline=INK, width=5 * s)
    im = im.resize((w + 12, hoehe + 12), Image.LANCZOS)
    return hart(El(im, x0 - 6, BODEN - hoehe - 6, cue, "cut", 0.0, None, name="schalter"))


def balken(x, y, w, h, fill, cue, name):
    """Rechteckfläche mit Tuschekontur (Teil des Lohnbalkens)."""
    im, dr, s = _flaeche(w, h)
    o = 6 * s
    dr.rectangle((o, o, o + w * s, o + h * s), fill=fill, outline=INK, width=5 * s)
    im = im.resize((w + 12, h + 12), Image.LANCZOS)
    return El(im, x - 6, y - 6, cue, "fade", 0.0, None, name="balken:" + name)


def figur_r(k, x, folge, bis=None, erst="cut", unten=BODEN, hoehe=FH):
    """Fallszene: Figur am festen Platz mit Mimikfolge (Suffix in folge enthält _r für Blick nach rechts)."""
    return fig(k, x, unten, hoehe, folge, bis=bis, erst=erst)


# ===========================================================================================================================
# A1 Fall: die Küche von Frau Kästner – Küche, Rechnung, Urteil, Arbeitgeber, Konto, Dorfmann und Kästner sprechen
# ===========================================================================================================================
DOX, KAX = 760, 1560                        # Herr Dorfmann (blickt nach rechts), Frau Kästner (blickt nach links)
RX = 1160                                   # wechselnde Requisiten zwischen den Figuren
KOMMT_KA = beim("kueche", "Kästner")
DOa = ("DO_redet_r", DOX, BODEN, FH)
KAa = ("KA_klagt", KAX, BODEN, FH)
folie([(NULL, "Fall · Die Einbauküche"), ("zahlt", "Fall · Die offene Rechnung"), ("urteil", "Fall · Das Urteil"),
       ("job", "Fall · Lohn und Konto")], [
    boden(NULL),
    hart(pl("Küche von Frau Kästner", 70, 40, NULL, fill=PINK, size=40)),
    kueche(110, 590, NULL),
    *fig("DO", DOX, BODEN, FH, [(NULL, "ruhig_r"), (beim("kueche", "Einbauküche"), "froh_r"), ("zahlt", "denkt_r"),
                                ("urteil", "bestimmt_r")], bis="d1", erst="cut"),
    *redet("DO_redet_r", DOX, BODEN, FH, "d1", "k1"),
    peep_voll("DO_bestimmt_r", DOX, BODEN, FH, "k1", anim="cut"),
    hart(ns("Herr Dorfmann", DOX, BODEN, NULL, GELB)),
    pl("Tischler", DOX, 330, NULL, fill=WEISS, size=30, anker="m", bis="kueche"),
    szene(ficon("tabler", "hammer", 470, BODEN - 230, 90, beim("kueche", "Einbauküche"), fuell=HOLZ), "174hammer*", 0.8, 0.05),
    *fig("KA", KAX, BODEN, FH, [(KOMMT_KA, "froh"), ("zahlt", "ruhig"), ("urteil", "sorge"), ("job", "ruhig")], bis="k1"),
    *redet("KA_klagt", KAX, BODEN, FH, "k1", lexi_bis_ende("k1") if False else ("k1", round(T_("frage") - T_("k1"), 3))),
    ns("Frau Kästner", KAX, BODEN, KOMMT_KA, PINK),
    pl("Einbauküche: 3.600 €", RX, 250, beim("kueche", "dreitausend"), fill=WEISS, size=30, anker="m", bis="zahlt"),
    ficon("tabler", "cash-off", RX, 640, 110, "zahlt", fuell=ROT, bis="urteil"),
    pl("nicht bezahlt", RX, 330, "zahlt", fill=HELLROT, size=30, anker="m", bis="urteil"),
    ficon("tabler", "file-certificate", RX, 640, 110, "urteil", fuell=WEISS, bis="job"),
    pl("Urteil mit Vollstreckungsklausel", RX, 250, beim("urteil", "Urteil"), fill=GELB, size=30, anker="m", bis="job"),
    pl("zugestellt", RX, 330, beim("urteil", "zugestellt"), fill=WEISS, size=30, anker="m", bis="job"),
    ficon("tabler", "building-factory-2", RX - 90, 640, 140, "job", fuell=WEISS),
    ficon("tabler", "car", RX - 90, 700, 90, beim("job", "Autowerk"), fuell=BLAUHELL),
    pl("großer Arbeitgeber: Autowerk", RX, 250, beim("job", "großen"), fill=WEISS, size=30, anker="m", bis="d1"),
    ficon("tabler", "building-bank", RX + 110, 640, 120, "konto", fuell=WEISS),
    pl("Gehalt aufs Girokonto", RX, 330, beim("konto", "Gehalt"), fill=BLAUHELL, size=30, anker="m", bis="d1"),
    blase("sprech", 760, 150, "d1", 1180, 190, inhalt=["Dann hole ich mir mein Geld von Ihrem", "Gehalt und von Ihrem Konto."],
          textsize=31, figur=DOa, bis="k1"),
    blase("sprech", 640, 120, "k1", 1300, 200, inhalt=["Mein Gehalt? Davon lebe ich doch!"], textsize=32, figur=KAa),
])

# ===========================================================================================================================
# A2 Fall: Wer schuldet wem? (Gläubiger, Schuldnerin, Arbeitgeber, Bank) – die Frage
# ===========================================================================================================================
D2, K2 = 330, 960
folie([("frage", "Fall · Die Frage")], [
    boden("frage"),
    hart(pl("Wer schuldet wem?", 70, 40, "frage", fill=GELB, size=40)),
    *fig("DO", D2, BODEN, FH, [("frage", "bestimmt_r")], erst="cut"), hart(ns("Herr Dorfmann", D2, BODEN, "frage", GELB)),
    *fig("KA", K2, BODEN, FH, [("frage", "sorge"), ("frage2", "denkt")], erst="cut"), hart(ns("Frau Kästner", K2, BODEN, "frage", PINK)),
    hart(pfeil(470, 600, 810, 600, "frage", breite=8, kopf=30)),
    hart(pl("Urteil: 3.600 €", 640, 520, "frage", fill=WEISS, size=28, anker="m")),
    hart(ficon("tabler", "building-factory-2", 1560, 500, 170, "frage", fuell=WEISS, anim="cut")),
    hart(pl("Arbeitgeber", 1560, 520, "frage", fill=WEISS, size=28, anker="m")),
    hart(ficon("tabler", "building-bank", 1560, 800, 150, "frage", fuell=WEISS, anim="cut")),
    hart(pl("Bank", 1560, 815, "frage", fill=BLAUHELL, size=28, anker="m")),
    hart(pfeil(1440, 430, 1110, 560, "frage", breite=8, kopf=30)),
    hart(pl("Lohn", 1280, 420, "frage", fill=GRUEN, size=28, anker="m")),
    hart(pfeil(1440, 720, 1110, 680, "frage", breite=8, kopf=30)),
    hart(pl("Guthaben", 1280, 740, "frage", fill=GRUEN, size=28, anker="m")),
    pl("Wie kommt Herr Dorfmann an Lohn und Guthaben?", 960, 130, "frage", fill=PINK, size=36, anker="m"),
    pl("Wann wirkt die Pfändung? Was müssen Arbeitgeber und Bank tun?", 960, 215, "frage2", fill=WEISS, size=32, anker="m"),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_174(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=33, zeilenabstand=1.28)
        els += e; y += 16
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_174("sv", [
    "Der Tischler Herr Dorfmann baut Frau Kästner eine Einbauküche für 3.600 € ein; sie zahlt nicht. Herr Dorfmann erstreitet "
    "ein Urteil. Er hat eine Ausfertigung mit Vollstreckungsklausel, das Urteil ist Frau Kästner zugestellt.",
    "Frau Kästner arbeitet bei einem großen Arbeitgeber, einem Autowerk. Ihr Gehalt geht auf ihr Girokonto bei ihrer Bank. "
    "Herr Dorfmann will an ihren Lohn und an das Guthaben auf dem Konto.",
    "Annahme: Frau Kästner hat keine Unterhaltspflichten; andere Gläubiger haben nicht gepfändet.",
], "Wie kommt Herr Dorfmann an Lohn und Guthaben – und was müssen Arbeitgeber und Bank tun?")

# ===========================================================================================================================
# C1 1. Antrag und Zuständigkeit (Wortlautkarte § 828 Abs. 1, 2 ZPO; § 20 Abs. 1 Nr. 17 RPflG)
# ===========================================================================================================================
W828 = ["„(1) Die gerichtlichen Handlungen, welche die Zwangsvollstreckung",
        "in Forderungen und andere Vermögensrechte zum Gegenstand haben,",
        "erfolgen durch das Vollstreckungsgericht.",
        "(2) Als Vollstreckungsgericht ist das Amtsgericht, bei dem der",
        "Schuldner im Inland seinen allgemeinen Gerichtsstand hat, und",
        "sonst das Amtsgericht zuständig, bei dem nach § 23 gegen den",
        "Schuldner Klage erhoben werden kann. …“"]
w828, w828_y = wortlaut(80, 175, 1100, W828, "§ 828 Abs. 1, 2 ZPO", "wl828", marken=[
    (1, "Forderungen", beim("wl828", "Forderungen")), (2, "Vollstreckungsgericht", beim("wl828", "Vollstreckungsgericht")),
    (4, "allgemeinen Gerichtsstand", beim("p828b", "allgemeinen"))], size=30)
P1 = "1. Antrag und Zuständigkeit"
folie([("antrag", P1), ("wl828", f"{P1} › Vollstreckungsgericht, § 828 ZPO"), ("p828b", f"{P1} › Amtsgericht am Wohnsitz"),
       ("rpfl", f"{P1} › Rechtspfleger, § 20 Abs. 1 Nr. 17 RPflG"), ("voraus", f"{P1} › Titel, Klausel, Zustellung")], [
    *tafel("antrag", P1),
    *w828,
    z("hier: Amtsgericht am Wohnsitz von Frau Kästner", 110, w828_y + 24, beim("p828b", "Wohnsitz"), "Bold", 34),
    zit("§ 828 Abs. 2, § 13 ZPO", 110, w828_y + 70, beim("p828b", "Wohnsitz")),
    *okz("entscheidet: der Rechtspfleger", w828_y + 118, "rpfl", "Bold", 34, x=160),
    zit("§ 20 Abs. 1 Nr. 17 RPflG", 160, w828_y + 164, "rpfl"),
    pl("prüft: Titel, Klausel, Zustellung", 110, w828_y + 214, "voraus", fill=GELB, size=32),
    pl("Video: das Grundschema der Zwangsvollstreckung", 110, w828_y + 290, beim("voraus", "Video"), fill=WEISS, size=28),
    *requisit([("antrag", ("tabler", "file-text", 100, WEISS), "Antrag", WEISS),
               ("wl828", ("tabler", "building-bank", 130, WEISS), "Vollstreckungsgericht", BLAUHELL),
               ("p828b", ("tabler", "map-pin", 100, PINK), "Wohnsitz", PINK),
               ("rpfl", ("tabler", "user", 100, WEISS), "Rechtspfleger", WEISS),
               ("voraus", ("tabler", "list-check", 100, WEISS), "Titel · Klausel · Zustellung", GELB)]),
    *stehend("DO", FX, [("antrag", "ruhig"), ("wl828", "denkt"), ("voraus", "bestimmt")]),
])

# ===========================================================================================================================
# C2 2. Pfändung (Wortlautkarte § 829 Abs. 1 Satz 1, 2 ZPO): Arrestatorium, Inhibitorium, zwei Drittschuldner, § 834
# ===========================================================================================================================
W829 = ["„Soll eine Geldforderung gepfändet werden, so hat das Gericht dem",
        "Drittschuldner zu verbieten, an den Schuldner zu zahlen. Zugleich",
        "hat das Gericht an den Schuldner das Gebot zu erlassen, sich jeder",
        "Verfügung über die Forderung, insbesondere ihrer Einziehung, zu",
        "enthalten. …“"]
w829, w829_y = wortlaut(80, 170, 1100, W829, "§ 829 Abs. 1 Satz 1, 2 ZPO", "wl829", marken=[
    (1, "zu verbieten", beim("wl829", "verbietet")), (1, "an den Schuldner zu zahlen", beim("wl829", "zahlen")),
    (3, "Verfügung über die Forderung", beim("inhib", "Verfügung"))], size=30)
P2 = "2. Pfändung"
folie([("pfaend", P2), ("wl829", f"{P2}, § 829 Abs. 1 ZPO"), ("arrest", f"{P2} › Arrestatorium"), ("inhib", f"{P2} › Inhibitorium"),
       ("dritt", f"{P2} › zwei Drittschuldner"), ("einh", f"{P2} › einheitlicher Beschluss"),
       ("p834", f"{P2} › keine Anhörung, § 834 ZPO")], [
    *tafel("pfaend", P2),
    *w829,
    blk(110, w829_y + 22, 510, 120, BLAUHELL, "arrest", [("Arrestatorium:", "ExtraBold", 32, INK),
                                                       ("Zahlungsverbot an den", "Bold", 30, INK), ("Drittschuldner", "Bold", 30, INK)]),
    blk(640, w829_y + 22, 510, 120, LILA, "inhib", [("Inhibitorium:", "ExtraBold", 32, INK),
                                                    ("Verfügungsverbot an die", "Bold", 30, INK), ("Schuldnerin", "Bold", 30, INK)]),
    z("Drittschuldner: Arbeitgeber (Lohn) und Bank (Guthaben)", 110, w829_y + 168, "dritt", "Bold", 32),
    z("auf Antrag in einem einheitlichen Beschluss", 110, w829_y + 216, "einh", "Bold", 32),
    zit("§ 829 Abs. 1 Satz 3 ZPO", 110, w829_y + 258, "einh"),
    *okz("ohne vorherige Anhörung, § 834 ZPO", w829_y + 300, "p834", "Bold", 32, x=160),
    pl("Rechtsbehelfe: eigene Videos", 110, w829_y + 360, "verw153", fill=WEISS, size=28),
    *requisit([("pfaend", ("tabler", "file-text", 100, WEISS), "Pfändungsbeschluss", WEISS),
               ("arrest", ("tabler", "hand-stop", 100, BLAUHELL), "nicht an sie zahlen", BLAUHELL),
               ("inhib", ("tabler", "lock", 100, LILA), "nicht verfügen", LILA)], bis="dritt"),
    *rechts_frei([ficon("tabler", "building-factory-2", PX - 90, PU, 110, "dritt", fuell=WEISS, bis="einh"),
                 ficon("tabler", "building-bank", PX + 90, PU, 100, "dritt", fuell=WEISS, bis="einh")]),
    *requisit([("dritt", None, "zwei Drittschuldner", GRUEN), ("einh", ("tabler", "file-text", 100, WEISS), "ein Beschluss", WEISS),
               ("p834", ("tabler", "ear", 100, WEISS), "ohne Anhörung", PINK)]),
    *paar("DO", [("pfaend", "ruhig"), ("einh", "froh")], "KA", [("pfaend", "ruhig"), ("arrest", "sorge"), ("p834", "denkt")]),
])

# ===========================================================================================================================
# C3 Wirksamkeit: Zustellung an den Drittschuldner (§ 829 Abs. 2, Wortlautkarte § 829 Abs. 3 ZPO)
# ===========================================================================================================================
W829_3 = ["„Mit der Zustellung des Beschlusses an den Drittschuldner",
          "ist die Pfändung als bewirkt anzusehen.“"]
w8293, w8293_y = wortlaut(80, 370, 1100, W829_3, "§ 829 Abs. 3 ZPO", "wl829_3", marken=[
    (0, "an den Drittschuldner", beim("wl829_3", "Drittschuldner")), (1, "als bewirkt", beim("wl829_3", "bewirkt"))], size=32)
PW = f"{P2} › Wirksamkeit"
folie([("zust", f"{PW}: Zustellung"), ("p829_2", f"{PW} › durch den Gerichtsvollzieher, § 829 Abs. 2 ZPO"),
       ("wl829_3", f"{PW} › bewirkt, § 829 Abs. 3 ZPO"), ("schuldn", f"{PW} › Zustellung an die Schuldnerin")], [
    *tafel("zust", "Wirksam erst mit Zustellung"),
    z("Herr Dorfmann lässt den Beschluss den Drittschuldnern", 110, 180, "p829_2", "Bold", 33),
    z("zustellen: durch den Gerichtsvollzieher", 110, 226, beim("p829_2", "Gerichtsvollzieher"), "Bold", 33),
    zit("§ 829 Abs. 2 Satz 1, § 192 ZPO", 110, 272, beim("p829_2", "Gerichtsvollzieher")),
    *w8293,
    *zeitstrahl(150, 1120, w8293_y + 150, "zust", [(250, "zust", "Beschluss erlassen", WEISS, True),
                                                   (640, beim("wl829_3", "bewirkt"), "an Drittschuldner: gepfändet", GRUEN, True),
                                                   (960, "schuldn", "danach: an Frau Kästner", WEISS, False)]),
    zit("§ 829 Abs. 2 Satz 2 ZPO", 760, w8293_y + 260, "schuldn"),
    *requisit([("zust", ("tabler", "mail", 110, WEISS), "Zustellung", GELB),
               ("wl829_3", ("tabler", "circle-check", 100, GRUEN), "gepfändet", GRUEN)]),
    *stehend("DO", FX, [("zust", "ruhig"), ("wl829_3", "froh")]),
])

# ===========================================================================================================================
# D Personalabteilung: der Beschluss kommt an (Personalleiterin spricht)
# ===========================================================================================================================
PLX = 1500
PLa = ("PL_redet", PLX, BODEN, FH)


def personal(cue):
    return [boden(cue), hart(pl("Personalabteilung im Autowerk", 70, 40, cue, fill=GRUEN, size=40)),
            hart(ficon("tabler", "building-factory-2", 300, BODEN - 2, 330, cue, fuell=WEISS, anim="cut")),
            hart(ficon("tabler", "car", 660, BODEN - 2, 190, cue, fuell=BLAUHELL, anim="cut")),
            tisch(940, 380, cue)]


folie([("p1", "2. Pfändung › beim Drittschuldner: Arbeitgeber")], [
    *personal("p1"),
    szene(ficon("tabler", "mail-opened", 1130, BODEN - 216, 120, "p1", fuell=WEISS, anim="cut"), "174brief*", 0.8, 0.0),
    *redet("PL_redet", PLX, BODEN, FH, "p1", "ueber"),
    hart(ns("Personalleiterin", PLX, BODEN, "p1", GRUEN)),
    pl("Pfändungsbeschluss gegen Frau Kästner", 1130, 520, beim("p1", "Pfändungsbeschluss"), fill=WEISS, size=28, anker="m"),
    blase("sprech", 820, 200, "p1", 1060, 220, inhalt=["Ein Pfändungsbeschluss gegen Frau Kästner.",
                                                        "Den pfändbaren Teil ihres Lohns zahlen", "wir nicht mehr an sie aus."],
          textsize=30, figur=PLa),
])

# ===========================================================================================================================
# E1 3. Überweisung (Wortlautkarte § 835 Abs. 1 ZPO): zur Einziehung oder an Zahlungs statt
# ===========================================================================================================================
W835 = ["„Die gepfändete Geldforderung ist dem Gläubiger nach seiner",
        "Wahl zur Einziehung oder an Zahlungs statt zum Nennwert zu",
        "überweisen.“"]
w835, w835_y = wortlaut(80, 330, 1100, W835, "§ 835 Abs. 1 ZPO", "wl835", marken=[
    (1, "zur Einziehung", beim("wl835", "Einziehung")), (1, "an Zahlungs statt", beim("wl835", "Zahlungs"))], size=32)
P3 = "3. Überweisung"
folie([("ueber", P3), ("wl835", f"{P3}, § 835 Abs. 1 ZPO"), ("unter", f"{P3} › an Zahlungs statt oder zur Einziehung")], [
    *tafel("ueber", P3),
    z("zusammen mit der Pfändung beantragt:", 110, 180, beim("ueber", "Gläubiger"), "Bold", 33),
    pl("Pfändungs- und Überweisungsbeschluss", 110, 232, beim("ueber", "Pfändungs-"), fill=GELB, size=32),
    zit("§ 829a Abs. 1 ZPO", 760, 246, beim("ueber", "Pfändungs-")),
    *w835,
    blk(110, w835_y + 26, 510, 160, GELB, beim("unter", "Zahlungs"), [("an Zahlungs statt:", "ExtraBold", 32, INK),
                                                                      ("Forderung geht über,", "Bold", 30, INK),
                                                                      ("gilt als befriedigt", "Bold", 30, INK)]),
    blk(640, w835_y + 26, 510, 160, BLAUHELL, beim("unter", "Einziehung"), [("zur Einziehung:", "ExtraBold", 32, INK),
                                                                            ("darf die Forderung", "Bold", 30, INK),
                                                                            ("nur einziehen", "Bold", 30, INK)]),
    zit("§ 835 Abs. 2 ZPO", 110, w835_y + 200, beim("unter", "befriedigt")),
    *requisit([("ueber", ("tabler", "file-text", 100, WEISS), "Überweisung", WEISS),
               ("wl835", ("tabler", "arrows-split", 100, WEISS), "Wahl des Gläubigers", GELB),
               ("unter", ("tabler", "scale", 110, GELB), "der Unterschied", WEISS)]),
    *paar("DO", [("ueber", "ruhig"), ("wl835", "denkt")], "KA", [("ueber", "ruhig")]),
])

# ===========================================================================================================================
# E2 Wirkung der Überweisung (Wortlautkarte § 836 Abs. 1 ZPO), hier: zur Einziehung
# ===========================================================================================================================
W836 = ["„Die Überweisung ersetzt die förmlichen Erklärungen des",
        "Schuldners, von denen nach den Vorschriften des bürgerlichen",
        "Rechts die Berechtigung zur Einziehung der Forderung",
        "abhängig ist.“"]
w836, w836_y = wortlaut(80, 180, 1100, W836, "§ 836 Abs. 1 ZPO", "wl836", marken=[
    (0, "ersetzt", beim("wl836", "ersetzt")), (0, "förmlichen Erklärungen", beim("wl836", "förmlichen"))], size=32)
folie([("wl836", f"{P3} › Wirkung, § 836 Abs. 1 ZPO"), ("hier835", f"{P3} › hier: zur Einziehung")], [
    *tafel("wl836", "Wirkung der Überweisung"),
    *w836,
    *okz("Herr Dorfmann wählt die Einziehung.", w836_y + 40, "hier835", "ExtraBold", 34, x=160),
    blk(110, w836_y + 110, 1040, 120, GRUEN, beim("hier835", "darf"), [("Er darf selbst Zahlung verlangen:", "ExtraBold", 34, INK),
                                                                       ("vom Arbeitgeber und von der Bank", "Bold", 32, INK)]),
    *requisit([("wl836", ("tabler", "writing-sign", 100, WEISS), "ersetzt Erklärungen", WEISS),
               ("hier835", ("tabler", "coins", 110, GELB), "Einziehung", GELB)]),
    *paar("DO", [("wl836", "ruhig"), (beim("hier835", "darf"), "froh")], "KA", [("wl836", "ruhig"), ("hier835", "sorge")]),
])

# ===========================================================================================================================
# F 4. Drittschuldnererklärung (Wortlautkarte § 840 Abs. 1 ZPO, Auszug)
# ===========================================================================================================================
W840 = ["„Auf Verlangen des Gläubigers hat der Drittschuldner binnen zwei",
        "Wochen, von der Zustellung des Pfändungsbeschlusses an gerechnet,",
        "dem Gläubiger zu erklären: 1. ob und inwieweit er die Forderung",
        "als begründet anerkenne und Zahlung zu leisten bereit sei; 2. ob",
        "und welche Ansprüche andere Personen an die Forderung machen;",
        "3. ob und wegen welcher Ansprüche die Forderung bereits für",
        "andere Gläubiger gepfändet sei; … 5. ob es sich bei dem Konto, …",
        "um ein Pfändungsschutzkonto im Sinne des § 850k … handelt; …“"]
w840, w840_y = wortlaut(80, 175, 1100, W840, "§ 840 Abs. 1 ZPO (Auszug)", "wl840", marken=[
    (0, "binnen zwei", beim("wl840", "binnen")), (1, "Wochen", beim("wl840", "binnen")),
    (3, "anerkenne", beim("e1", "anerkennt")), (4, "andere Personen", beim("e2", "andere")),
    (6, "andere Gläubiger gepfändet", beim("e3", "andere")), (7, "Pfändungsschutzkonto", beim("e4", "Pfändungsschutzkonto"))],
    size=30)
P4 = "4. Drittschuldnererklärung"
folie([("erkl", P4), ("wl840", f"{P4}, § 840 Abs. 1 ZPO"), ("e4", f"{P4} › Bank: Pfändungsschutzkonto?")], [
    *tafel("erkl", P4),
    *w840,
    pl("binnen 2 Wochen ab Zustellung", 110, w840_y + 26, beim("wl840", "binnen"), fill=GELB, size=32),
    *requisit([("erkl", ("tabler", "file-text", 100, WEISS), "Erklärung", WEISS),
               ("wl840", ("tabler", "calendar-event", 100, WEISS), "2 Wochen", GELB),
               ("e4", ("tabler", "building-bank", 110, WEISS), "Bank", BLAUHELL)]),
    *paar("PL", [("erkl", "ruhig"), ("e1", "denkt")], "DO", [("erkl", "ruhig"), ("e1", "denkt")]),
])

# ===========================================================================================================================
# G Personalabteilung: die Erklärung des Arbeitgebers; Haftung (§ 840 Abs. 2 Satz 2 ZPO)
# ===========================================================================================================================
folie([("p2", f"{P4} › Erklärung des Arbeitgebers"), ("haft", f"{P4} › Haftung, § 840 Abs. 2 Satz 2 ZPO")], [
    *personal("p2"),
    hart(ficon("tabler", "file-text", 1130, BODEN - 216, 110, "p2", fuell=WEISS, anim="cut")),
    *redet("PL_redet", PLX, BODEN, FH, "p2", "haft"),
    peep_voll("PL_ruhig", PLX, BODEN, FH, "haft", anim="cut"),
    hart(ns("Personalleiterin", PLX, BODEN, "p2", GRUEN)),
    pl("Drittschuldnererklärung", 1130, 520, "p2", fill=GELB, size=28, anker="m"),
    blase("sprech", 720, 150, "p2", 1080, 210, inhalt=["Wir erkennen die Lohnforderung an.",
                                                        "Andere Pfändungen liegen nicht vor."], textsize=31, figur=PLa, bis="haft"),
    ficon("tabler", "alert-triangle", 960, 330, 110, "haft", fuell=GELB),
    pl("Pflicht nicht erfüllt: Haftung für den Schaden", 960, 140, beim("haft", "haftet"), fill=HELLROT, size=32, anker="m"),
    pl("§ 840 Abs. 2 Satz 2 ZPO", 960, 220, beim("haft", "haftet"), fill=WEISS, size=28, anker="m"),
])

# ===========================================================================================================================
# H1 5. Pfändungsschutz beim Lohn (§§ 850, 850a, 850c ZPO; Pfändungsfreigrenzenbekanntmachung 2026)
# ===========================================================================================================================
P5 = "5. Pfändungsschutz beim Lohn"
LB_Y, LB_H = 760, 70
LB_X0, LB_X1, LB_X2, LB_X3 = 110, 560, 740, 1150     # Grundbetrag | 3/10 frei | 7/10
folie([("lohn", P5), ("p850", f"{P5}, § 850 ZPO"), ("p850a", f"{P5} › unpfändbare Bezüge, § 850a ZPO"),
       ("p850c", f"{P5} › Grundbetrag, § 850c ZPO"), ("drei", f"{P5} › darüber 3/10 frei")], [
    *tafel("lohn", P5),
    z("Arbeitseinkommen: nur nach §§ 850a bis 850i", 110, 180, beim("p850", "Arbeitseinkommen"), "Bold", 34),
    z("pfändbar", 110, 226, beim("p850", "pfändbar"), "Bold", 34),
    zit("§ 850 Abs. 1 ZPO", 270, 240, beim("p850", "pfändbar")),
    z("teils unpfändbar, etwa: Mehrarbeit zur Hälfte", 110, 290, beim("p850a", "Hälfte"), "Bold", 34),
    zit("§ 850a Nr. 1 ZPO", 110, 336, beim("p850a", "Hälfte")),
    blk(110, 390, 1040, 120, GELB, beim("p850c", "eintausend"), [("Grundbetrag ab 1.7.2026:", "ExtraBold", 34, INK),
                                                               ("1.587,40 € im Monat", "ExtraBold", 36, INK)]),
    z("mehr bei Unterhaltspflichten", 110, 528, beim("p850c", "Unterhaltspflichten"), "Bold", 34),
    zit("§ 850c Abs. 1, 2 ZPO; Pfändungsfreigrenzenbekanntmachung 2026, BGBl. 2026 I Nr. 80", 110, 576,
        beim("p850c", "Unterhaltspflichten")),
    balken(LB_X0, LB_Y, LB_X1 - LB_X0, LB_H, GRUEN, beim("p850c", "eintausend"), "grund"),
    pl("Grundbetrag: frei", (LB_X0 + LB_X1) / 2, LB_Y - 70, beim("p850c", "eintausend"), fill=GRUEN, size=28, anker="m"),
    balken(LB_X1, LB_Y, LB_X2 - LB_X1, LB_H, HELLGRUEN, "drei", "frei"),
    balken(LB_X2, LB_Y, LB_X3 - LB_X2, LB_H, HELLROT, "drei", "rest"),
    pl("darüber: 3/10 frei", (LB_X1 + LB_X3) / 2, LB_Y - 70, "drei", fill=HELLGRUEN, size=28, anker="m"),
    zit("§ 850c Abs. 3 ZPO", 110, LB_Y + 86, "drei"),
    *requisit([("lohn", ("tabler", "wallet", 100, WEISS), "Lohn", WEISS),
               ("p850a", ("tabler", "clock", 100, WEISS), "Mehrarbeit", WEISS),
               ("p850c", ("tabler", "shield-check", 100, GRUEN), "Grundbetrag frei", GRUEN)]),
    *stehend("KA", FX, [("lohn", "sorge"), ("p850c", "ruhig"), ("drei", "denkt")]),
])

# ===========================================================================================================================
# H2 Tabelle, jährliche Anpassung, künftige Gehälter (§ 850c Abs. 4, 5, § 832 ZPO)
# ===========================================================================================================================
folie([("tabelle", f"{P5} › Tabelle, § 850c Abs. 5 ZPO"), ("juli", f"{P5} › Anpassung zum 1. Juli, § 850c Abs. 4 ZPO"),
       ("p832", f"{P5} › künftige Gehälter, § 832 ZPO")], [
    *tafel("tabelle", "Die Pfändungstabelle"),
    z("Der Beschluss verweist nur auf die Tabelle", 110, 180, "tabelle", "Bold", 34),
    z("der amtlichen Bekanntmachung.", 110, 226, beim("tabelle", "amtlichen"), "Bold", 34),
    *okz("Der Arbeitgeber liest den pfändbaren Betrag ab.", 290, beim("tabelle", "liest"), "Bold", 33, x=160),
    zit("§ 850c Abs. 5 Satz 2, 3 ZPO", 160, 336, beim("tabelle", "liest")),
    *okz("Anpassung jedes Jahr zum 1. Juli", 400, "juli", "ExtraBold", 34, x=160),
    zit("§ 850c Abs. 4 ZPO", 160, 446, "juli"),
    blk(110, 520, 1040, 120, GRUEN, "p832", [("Die Pfändung erfasst auch", "ExtraBold", 34, INK),
                                            ("die künftigen Gehälter, § 832 ZPO", "ExtraBold", 34, INK)]),
    *requisit([("tabelle", ("tabler", "table", 100, WEISS), "Tabelle", WEISS),
               ("juli", ("tabler", "calendar-event", 100, WEISS), "jedes Jahr: 1. Juli", GELB),
               ("p832", ("tabler", "calendar-time", 100, WEISS), "auch künftig", GRUEN)]),
    *paar("PL", [("tabelle", "ruhig"), (beim("tabelle", "liest"), "denkt")], "KA", [("tabelle", "ruhig"), ("p832", "sorge")]),
])

# ===========================================================================================================================
# I1 6. Konto: in der Bank (Frau Kästner spricht, der Bankberater nicht)
# ===========================================================================================================================
BBX, KAB = 640, 1430
KAb = ("KA_redet", KAB, BODEN, FH)
folie([("konto2", "6. Konto"), ("k2", "6. Konto › Pfändungsschutzkonto")], [
    boden("konto2"),
    hart(pl("Bank von Frau Kästner", 70, 40, "konto2", fill=BLAUHELL, size=40)),
    *fig("BB", BBX, BODEN, FH, [("konto2", "ruhig_r"), ("wl850k", "froh_r")], erst="cut", bis="wl850k"),
    hart(ns("Bankberater", BBX, BODEN, "konto2", BLAUHELL)),
    schalter(380, 900, "konto2"),
    hart(ficon("tabler", "building-bank", 1050, 360, 150, "konto2", fuell=WEISS, anim="cut")),
    hart(ficon("tabler", "credit-card", 640, BODEN - 252, 90, "konto2", fuell=GELB, anim="cut")),
    *fig("KA", KAB, BODEN, FH, [("konto2", "ruhig")], erst="cut", bis="k2"),
    *redet("KA_redet", KAB, BODEN, FH, "k2", "wl850k"),
    hart(ns("Frau Kästner", KAB, BODEN, "konto2", PINK)),
    pl("Girokonto: gepfändet", 1050, 420, "konto2", fill=HELLROT, size=28, anker="m"),
    blase("sprech", 700, 150, "k2", 1100, 190, inhalt=["Bitte führen Sie mein Girokonto", "als Pfändungsschutzkonto."],
          textsize=30, figur=KAb),
])

# ===========================================================================================================================
# I2 Pfändungsschutzkonto (Wortlautkarte § 850k Abs. 1 Satz 1 ZPO; § 850k Abs. 2, § 835 Abs. 3 Satz 2, § 899 Abs. 1 ZPO)
# ===========================================================================================================================
W850K = ["„Eine natürliche Person kann jederzeit von dem Kreditinstitut",
         "verlangen, dass ein von ihr dort geführtes Zahlungskonto als",
         "Pfändungsschutzkonto geführt wird. …“"]
w850k, w850k_y = wortlaut(80, 170, 1100, W850K, "§ 850k Abs. 1 Satz 1 ZPO", "wl850k", marken=[
    (0, "jederzeit", beim("wl850k", "jederzeit"))], size=32)
P6 = "6. Konto › Pfändungsschutzkonto"
folie([("wl850k", f"{P6}, § 850k ZPO"), ("moni", f"{P6} › Auszahlung erst nach 1 Monat, § 835 Abs. 3 ZPO"),
       ("frei", f"{P6} › Freibetrag, § 899 Abs. 1 ZPO")], [
    *tafel("wl850k", "6. Das Pfändungsschutzkonto"),
    *w850k,
    z("schon gepfändet: ab dem 4. Geschäftstag nach dem Verlangen", 110, w850k_y + 22, beim("wl850k", "vierten"), "Bold", 32),
    zit("§ 850k Abs. 2 Satz 1 ZPO", 110, w850k_y + 64, beim("wl850k", "vierten")),
    z("an den Gläubiger erst 1 Monat nach Zustellung", 110, w850k_y + 116, "moni", "Bold", 32),
    z("des Überweisungsbeschlusses", 110, w850k_y + 160, beim("moni", "Überweisungsbeschlusses"), "Bold", 32),
    zit("§ 835 Abs. 3 Satz 2 ZPO", 110, w850k_y + 202, beim("moni", "Überweisungsbeschlusses")),
    z("Freibetrag: Grundbetrag, aufgerundet auf volle 10 €", 110, w850k_y + 256, beim("frei", "Grundbetrag"), "Bold", 32),
    blk(110, w850k_y + 310, 1040, 80, GRUEN, beim("frei", "eintausend"), [("ab 1.7.2026: 1.590 € im Monat", "ExtraBold", 36, INK)]),
    zit("§ 899 Abs. 1 Satz 1 ZPO; BGBl. 2026 I Nr. 80", 110, w850k_y + 404, beim("frei", "eintausend")),
    *requisit([("wl850k", ("tabler", "shield-lock", 100, BLAUHELL), "Pfändungsschutzkonto", BLAUHELL),
               ("moni", ("tabler", "hourglass", 100, WEISS), "1 Monat", WEISS),
               ("frei", ("tabler", "shield-check", 100, GRUEN), "Freibetrag", GRUEN)]),
    *paar("BB", [("wl850k", "ruhig")], "KA", [("wl850k", "ruhig"), (beim("frei", "eintausend"), "froh")]),
])

# ===========================================================================================================================
# J Ergebnis
# ===========================================================================================================================
folie([("erg", "Ergebnis")], [
    *tafel("erg", "Ergebnis"),
    *okz("Herr Dorfmann kommt an Lohn und Guthaben,", 190, "erg", "ExtraBold", 36, x=160),
    blk(110, 270, 1040, 120, HELL, "erg2", [("aber nur an den pfändbaren Teil,", "ExtraBold", 36, INK),
                                           ("Monat für Monat", "ExtraBold", 36, INK)]),
    *requisit([("erg", ("tabler", "coins", 110, GELB), "Lohn und Guthaben", GELB),
               ("erg2", ("tabler", "shield-check", 100, GRUEN), "nur der pfändbare Teil", GRUEN)]),
    *paar("DO", [("erg", "froh")], "KA", [("erg", "ruhig")]),
])

# ===========================================================================================================================
# K Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Zeitpunkt der Pfändung"), ("tipp2", "Klausurtipp · Wie wurde überwiesen?")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Achte auf den Zeitpunkt:", 200, 200, beim("tipp", "Zeitpunkt"), "Bold", 36),
    z("Die Pfändung wirkt erst mit Zustellung", 200, 270, beim("tipp", "Pfändung"), "Bold", 33),
    z("an den Drittschuldner,", 200, 316, beim("tipp", "Pfändung"), "Bold", 33),
    z("nicht schon mit Erlass des Beschlusses.", 200, 362, beim("tipp", "nicht"), "Bold", 33),
    pl("§ 829 Abs. 3 ZPO", 200, 420, beim("tipp", "nicht"), fill=GELB, size=30),
    linienzug([(130, 520), (1130, 520)], "tipp2", breite=3),
    z("Wie wurde überwiesen?", 200, 560, "tipp2", "Bold", 36),
    *okz("Nur an Zahlungs statt gilt der Gläubiger", 630, beim("tipp2", "Nur"), "Bold", 33, x=200),
    z("als befriedigt.", 200, 676, beim("tipp2", "Nur"), "Bold", 33),
    pl("§ 835 Abs. 2 ZPO", 200, 736, beim("tipp2", "Nur"), fill=GELB, size=30),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# L Prüfschema (fünf Schritte = Merktabelle)
# ===========================================================================================================================
REIHEN = [("s1", 0, "1. Antrag beim Vollstreckungsgericht", True),
          (beim("s1", "Vollstreckungsgericht"), 1, "Amtsgericht am Wohnsitz, Rechtspfleger (§ 828 ZPO)", False),
          ("s2", 0, "2. Pfändungs- und Überweisungsbeschluss", True),
          (beim("s2", "Arrestatorium"), 1, "Arrestatorium und Inhibitorium (§§ 829, 835 ZPO)", False),
          ("s3", 0, "3. Zustellung an den Drittschuldner", True),
          (beim("s3", "Jetzt"), 1, "jetzt ist gepfändet (§ 829 Abs. 3 ZPO)", False),
          ("s4", 0, "4. Drittschuldnererklärung binnen 2 Wochen (§ 840 ZPO)", True),
          ("s5", 0, "5. Einziehung", True),
          (beim("s5", "begrenzt"), 1, "begrenzt durch den Pfändungsschutz (§§ 850 ff., 850k, 899 ZPO)", False)]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Schema: Pfändung in 5 Schritten"), 110, 90, "sch", 46)]
y = 200
for c, ebene, text, fett in REIHEN:
    x = (130, 200)[ebene]
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 38 if ebene == 0 else 34, rechts=1820))
    y += {0: 74, 1: 84}[ebene]
assert y <= 970, y
folie([("sch", "Schema"), ("s1", "Schema › 1. Antrag"), ("s2", "Schema › 2. Pfändungs- und Überweisungsbeschluss"),
       ("s3", "Schema › 3. Zustellung an den Drittschuldner"), ("s4", "Schema › 4. Drittschuldnererklärung"),
       ("s5", "Schema › 5. Einziehung")], els_sch)

# ===========================================================================================================================
# M Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Gepfändet ist erst, wenn der Beschluss", 0)],
                 [("dem Drittschuldner ", 0), ("zugestellt", "a"), (" ist.", 0)]], 750, 290, 42, "merke",
                {"a": beim("merke", "zugestellt")}),
    *markertext([[("Was der Gläubiger bekommt, begrenzt", 0)], [("der Pfändungsschutz: beim Lohn die ", 0), ("Tabelle", "b"), (",", 0)],
                 [("beim Konto das ", 0), ("Pfändungsschutzkonto", "c"), (".", 0)]], 750, 500, 42, "m2",
                {"b": beim("m2", "Tabelle"), "c": beim("m2", "Pfändungsschutzkonto")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
