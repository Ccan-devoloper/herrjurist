"""Folge 153 · Vollstreckungserinnerung § 766 ZPO: Das Prüfschema – Serienstandard Open Peeps (Katzenkönig).
Übungsfall: Konditorin Frau Bergmann (Gläubigerin, spricht nicht), Herr Mühlbauer (Schuldner), der Gerichtsvollzieher.
Szenen laut ../SZENENPLAN.md; Belege je Aussage in ../RECHTSSTAND.md. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/
fig/ns/okz/neinz/requisit/stehend/paar als eigene Kopie aus Folge 150 (gemeinsame Dateien unverändert); neu: theke(),
lowboard(), siegelmarke(), zeitstrahl(). Siegelmarke neutral (rote Marke mit Schriftzug „Pfandsiegel“, kein Behördenlogo).
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

bausteine.FIGORDNER = "op_153/"

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
        if n.startswith(("bild:", "ficon:", "bank")) or "/op_153/" in n:
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
NAME = {"MB": "Herr Mühlbauer", "GV": "Gerichtsvollzieher", "BE": "Frau Bergmann"}
NFARBE = {"MB": LILA, "GV": WEISS, "BE": GRUEN}
DUNKEL = (58, 58, 72, 255)
ZA, BG_ = "A. Zulässigkeit", "B. Begründetheit"


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


# --- eigene Szenenbausteine ------------------------------------------------------------------------------------------------
def theke(x0, x1, cue, oben):
    """Ladentheke der Konditorei aus Grundformen: Holzplatte, helle Front mit Glasfeldern bis zum Boden."""
    w, h = x1 - x0, BODEN - oben
    im, dr, s = _flaeche(w, h)
    o = 6 * s
    dr.rectangle((o, o + 30 * s, o + w * s, o + h * s), fill=WEISS, outline=INK, width=5 * s)
    for k in range(3):
        a = o + int(w * (0.06 + k * 0.32)) * s
        dr.rounded_rectangle((a, o + 60 * s, a + int(w * 0.26) * s, o + (h - 40) * s), 10 * s, fill=(228, 238, 253, 255),
                             outline=INK, width=3 * s)
    dr.rounded_rectangle((o - 14 * s, o, o + (w + 14) * s, o + 34 * s), 8 * s, fill=HOLZ, outline=INK, width=5 * s)
    im = im.resize((w + 12, h + 12), Image.LANCZOS)
    return hart(El(im, x0 - 6, oben - 6, cue, "cut", 0.0, None, name="theke"))


def lowboard(x0, x1, cue, hoehe=120):
    """Fernsehschrank aus Grundformen: Holzkorpus mit zwei Fächern, kurze Füße."""
    w = x1 - x0
    im, dr, s = _flaeche(w, hoehe)
    o = 6 * s
    dr.rounded_rectangle((o, o, o + w * s, o + (hoehe - 18) * s), 10 * s, fill=HOLZ, outline=INK, width=5 * s)
    dr.line((o + w * s // 2, o + 12 * s, o + w * s // 2, o + (hoehe - 30) * s), fill=INK, width=3 * s)
    for xx in (o + 24 * s, o + (w - 44) * s):
        dr.rectangle((xx, o + (hoehe - 18) * s, xx + 20 * s, o + hoehe * s), fill=INK)
    im = im.resize((w + 12, hoehe + 12), Image.LANCZOS)
    return hart(El(im, x0 - 6, BODEN - hoehe - 6, cue, "cut", 0.0, None, name="lowboard"))


_SM = {}


def siegelmarke(cx, cy, cue, bis=None, anim="pop", d=0.0, breite=176):
    """Neutrale Pfandsiegelmarke (§ 808 Abs. 2 Satz 2 ZPO): rote Marke mit Tuschekontur und Schriftzug, kein Logo."""
    if breite not in _SM:
        f = F("ExtraBold", 26)
        t = "Pfandsiegel"
        tw = f.getlength(t)
        w, h = breite, 64
        assert tw <= w - 24
        im, dr, s = _flaeche(w, h)
        o = 6 * s
        dr.rounded_rectangle((o, o, o + w * s, o + h * s), 14 * s, fill=ROT, outline=INK, width=5 * s)
        dr.rounded_rectangle((o + 9 * s, o + 9 * s, o + (w - 9) * s, o + (h - 9) * s), 9 * s, outline=WEISS, width=3 * s)
        im = im.resize((w + 12, h + 12), Image.LANCZOS)
        b = f.getbbox(t)
        ImageDraw.Draw(im).text(((w + 12 - tw) / 2 - b[0], (h + 12 - (b[3] - b[1])) / 2 - b[1]), t, font=f, fill=WEISS)
        _SM[breite] = im
    im = _SM[breite]
    return El(im, cx - im.width / 2, cy - im.height / 2, cue, anim, d, bis, name="ficon:siegelmarke")


def zeitstrahl(x0, x1, y, cue, punkte):
    """Zeitstrahl mit Marken: punkte = [(x, cue, text, fill, oben?)]; Linie erscheint mit cue."""
    els = [linienzug([(x0, y), (x1, y)], cue, breite=6, farbe=INK), pfeil(x1 - 40, y, x1 + 10, y, cue, breite=6, kopf=24)]
    for x, c, text, fill, oben in punkte:
        els.append(linienzug([(x, y - 22), (x, y + 22)], c, breite=6, farbe=INK))
        els.append(pl(text, x, y - 92 if oben else y + 40, c, fill=fill, size=28, anker="m"))
    return els


# ===========================================================================================================================
# A1 Fall: die Konditorei – Torte, Urteil, Klausel, Auftrag
# ===========================================================================================================================
BEX, MBX = 560, 1430                        # Frau Bergmann hinter der Theke, Herr Mühlbauer davor
TX0, TX1 = 330, 860                         # Theke
TOBEN = BODEN - 240
RX = 1010                                   # wechselnde Requisiten zwischen den Figuren
KOMMT_MB = beim("torte", "Hochzeit")
A_BE = [*fig("BE", BEX, BODEN, FH, [(NULL, "ruhig_r"), (KOMMT_MB, "froh_r"), ("zahlt", "sorge_r"), ("urteil", "denkt_r"),
                                    ("klausel", "froh_r")], erst="cut")]
folie([(NULL, "Fall · Die Hochzeitstorte"), ("zahlt", "Fall · Die offene Rechnung"), ("urteil", "Fall · Das Urteil"),
       ("klausel", "Fall · Klausel und Vollstreckungsauftrag")], [
    boden(NULL),
    hart(pl("Konditorei Bergmann", 70, 40, NULL, fill=GELB, size=40)),
    *A_BE,
    theke(TX0, TX1, NULL, TOBEN),
    hart(ns("Frau Bergmann", BEX, BODEN, NULL, GRUEN)),
    hart(ficon("tabler", "cookie", 440, TOBEN + 2, 70, NULL, fuell=GELB, anim="cut")),
    ficon("tabler", "cake", 720, TOBEN + 2, 150, beim("torte", "Torte"), fuell=WEISS, nebenfarbe=PINK),
    pl("Hochzeitstorte: 900 €", 720, 300, beim("torte", "neunhundert"), fill=WEISS, size=30, anker="m", bis="klausel"),
    *fig("MB", MBX, BODEN, FH, [(KOMMT_MB, "froh"), ("zahlt", "ruhig"), ("urteil", "sorge"), ("auftrag", "denkt")]),
    ns("Herr Mühlbauer", MBX, BODEN, KOMMT_MB, LILA),
    ficon("tabler", "heart", RX, 330, 90, KOMMT_MB, fuell=ROT, bis="zahlt"),
    pl("Hochzeit", RX, 200, KOMMT_MB, fill=PINK, size=30, anker="m", bis="zahlt"),
    ficon("tabler", "cash-off", RX, 330, 110, "zahlt", fuell=ROT, bis="urteil"),
    pl("nicht bezahlt", RX, 200, "zahlt", fill=HELLROT, size=30, anker="m", bis="urteil"),
    ficon("tabler", "building-bank", RX, 330, 120, "urteil", fuell=WEISS, bis="klausel"),
    pl("Urteil des Amtsgerichts", RX, 130, beim("urteil", "Amtsgericht"), fill=BLAUHELL, size=30, anker="m", bis="klausel"),
    pl("vorläufig vollstreckbar", RX, 380, beim("urteil", "vorläufig"), fill=WEISS, size=30, anker="m", bis="klausel"),
    ficon("tabler", "file-certificate", RX, 330, 110, beim("klausel", "Ausfertigung"), fuell=WEISS),
    pl("Ausfertigung mit Vollstreckungsklausel", RX, 130, beim("klausel", "Ausfertigung"), fill=GELB, size=30, anker="m"),
    pl("Auftrag an den Gerichtsvollzieher", RX, 380, beim("auftrag", "beauftragt"), fill=PINK, size=30, anker="m"),
])

# ===========================================================================================================================
# A2 Fall: die Pfändung in der Wohnung von Herrn Mühlbauer (ohne Zustellung)
# ===========================================================================================================================
MBW, GVW = 560, 1530                        # Herr Mühlbauer (blickt nach rechts), Gerichtsvollzieher (blickt nach links)
TVX, TVU = 1040, BODEN - 118                # Fernseher auf dem Fernsehschrank
SMX, SMY = TVX, BODEN - 275                 # Siegelmarke auf dem Bildschirm
MBa = ("MB_redet_r", MBW, BODEN, FH)
GVa = ("GV_redet", GVW, BODEN, FH)


def wohnung(cue, mb, gv, siegel_bis=None, siegel_cue=None):
    """Schauplatz Wohnzimmer Mühlbauer: Sofa, Pflanze, Fernsehschrank mit Fernseher; Figuren als Elementlisten."""
    els = [boden(cue), hart(pl("Wohnung von Herrn Mühlbauer", 70, 40, cue, fill=LILA, size=40)),
           hart(ficon("tabler", "sofa", 230, BODEN - 2, 300, cue, fuell=BLAUHELL, anim="cut")),
           hart(ficon("tabler", "plant-2", 1840 - 70, BODEN - 2, 110, cue, fuell=GRUEN, anim="cut")),
           lowboard(TVX - 190, TVX + 190, cue),
           hart(ficon("tabler", "device-tv", TVX, TVU, 300, cue, fuell=DUNKEL, anim="cut")),
           *mb, *gv]
    return els


folie([("g1", "Fall · Die Pfändung"), ("zust", "Fall · Ohne Zustellung"), ("frage", "Fall · Die Frage")], [
    *wohnung("g1",
             [*fig("MB", MBW, BODEN, FH, [("g1", "schreck_r")], bis="m1", erst="cut"),
              *redet("MB_redet_r", MBW, BODEN, FH, "m1", "g2"),
              *fig("MB", MBW, BODEN, FH, [("g2", "sorge_r"), ("zust", "denkt_r")], erst="cut"),
              hart(ns("Herr Mühlbauer", MBW, BODEN, "g1", LILA))],
             [*redet("GV_redet", GVW, BODEN, FH, "g1", "siegel"),
              peep_voll("GV_ruhig", GVW, BODEN, FH, "siegel", anim="cut", bis="g2"),
              *redet("GV_redet", GVW, BODEN, FH, "g2", "zust"),
              *fig("GV", GVW, BODEN, FH, [("zust", "ruhig"), ("frage", "denkt")], erst="cut"),
              hart(ns("Gerichtsvollzieher", GVW, BODEN, "g1", WEISS))]),
    szene(siegelmarke(SMX, SMY, beim("siegel", "Siegelmarke")), "153siegel*", 0.9, 0.05),
    pl("gepfändet", TVX, 400, beim("siegel", "Gerät"), fill=ROT, size=32, anker="m", bis="m1"),
    blase("sprech", 780, 200, "g1", 1180, 230, inhalt=["Wegen der Forderung von Frau Bergmann", "pfände ich Ihren Fernseher."],
          textsize=31, figur=GVa, bis="siegel"),
    blase("sprech", 700, 150, "m1", 820, 240, inhalt=["Das Urteil wurde mir nie zugestellt!"], textsize=32, figur=MBa,
          bis="g2"),
    blase("sprech", 760, 200, "g2", 1180, 230, inhalt=["Die Gläubigerin hat eine vollstreckbare", "Ausfertigung. Das genügt mir."],
          textsize=31, figur=GVa, bis="zust"),
    ficon("tabler", "file-x", TVX, 330, 90, "zust", fuell=HELLROT, bis="frage"),
    pl("Urteil nicht zugestellt: weder vorher noch bei der Pfändung", 960, 130, beim("zust", "weder"), fill=HELLROT, size=30,
       anker="m", bis="frage"),
    pl("Wie wehrt sich Herr Mühlbauer?", 960, 130, "frage", fill=PINK, size=38, anker="m"),
    pl("Wann wäre die sofortige Beschwerde der richtige Weg?", 960, 225, "frage2", fill=WEISS, size=32, anker="m"),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_153(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=33, zeilenabstand=1.28)
        els += e; y += 16
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_153("sv", [
    "Frau Bergmann führt eine Konditorei. Für die Hochzeit von Herrn Mühlbauer backt sie eine Torte für 900 €; er zahlt "
    "nicht. Das Amtsgericht verurteilt ihn zur Zahlung, das Urteil ist vorläufig vollstreckbar. Frau Bergmann erhält eine "
    "Ausfertigung mit Vollstreckungsklausel und beauftragt den Gerichtsvollzieher.",
    "Der Gerichtsvollzieher pfändet in der Wohnung von Herrn Mühlbauer dessen Fernseher und klebt eine Siegelmarke auf. "
    "Das Urteil wurde Herrn Mühlbauer weder vorher noch bei der Pfändung zugestellt. Der Fernseher ist noch nicht "
    "versteigert.",
    "Annahme: Der Fernseher ist pfändbar; weitere Fehler gibt es nicht.",
], "Wie wehrt sich Herr Mühlbauer – und wann wäre die sofortige Beschwerde richtig?")

# ===========================================================================================================================
# C1 A. Zulässigkeit · 1. Statthaftigkeit (Wortlautkarte § 766 Abs. 1 Satz 1 ZPO)
# ===========================================================================================================================
W766 = ["„Über Anträge, Einwendungen und Erinnerungen, welche die",
        "Art und Weise der Zwangsvollstreckung oder das vom",
        "Gerichtsvollzieher bei ihr zu beobachtende Verfahren",
        "betreffen, entscheidet das Vollstreckungsgericht. …“"]
w766, w766_y = wortlaut(80, 255, 1100, W766, "§ 766 Abs. 1 Satz 1 ZPO", "wl766", marken=[
    (3, "Vollstreckungsgericht", beim("wl766", "Vollstreckungsgericht")), (0, "Einwendungen", beim("wl766", "Einwendungen")),
    (1, "Art und Weise", beim("wl766", "Art")), (2, "Verfahren", beim("wl766", "Verfahren"))], size=32)
P1 = f"{ZA} › 1. Statthaftigkeit"
folie([("zul", ZA), ("statt", P1), ("wl766", f"{P1}, § 766 Abs. 1 Satz 1 ZPO"), ("vor", f"{P1} › Vollstreckungsvoraussetzungen"),
       ("statt_ok", f"{P1} › statthaft (+)")], [
    *tafel("zul", ZA),
    z("1. Statthaftigkeit", 110, 180, "statt", "ExtraBold", 38),
    *w766,
    z("Dazu gehören die Vollstreckungsvoraussetzungen,", 110, w766_y + 26, "vor", "Bold", 34),
    z("also auch die Zustellung.", 110, w766_y + 72, beim("vor", "Zustellung"), "Bold", 34),
    zit("BGH, Beschl. v. 18.5.2017 – VII ZB 38/16, Rn. 37 (§§ 704 ff. ZPO)", 110, w766_y + 120, beim("vor", "Zustellung")),
    *okz("Herr Mühlbauer rügt das Vorgehen des Gerichtsvollziehers", w766_y + 180, "statt_ok", "Bold", 33, x=160),
    blk(110, w766_y + 245, 1040, 80, GRUEN, beim("statt_ok", "Erinnerung"), [("Die Erinnerung ist statthaft.", "ExtraBold", 36, INK)]),
    *requisit([("zul", ("tabler", "list-check", 100, WEISS), "Prüfung", WEISS),
               ("wl766", ("tabler", "gavel", 110, HOLZ), "§ 766 Abs. 1 ZPO", GELB),
               ("vor", ("tabler", "file-x", 100, HELLROT), "Zustellung?", HELLROT),
               ("statt_ok", ("tabler", "circle-check", 100, GRUEN), "statthaft", GRUEN)]),
    *paar("MB", [("zul", "ruhig"), ("vor", "denkt"), ("statt_ok", "froh")], "GV", [("zul", "ruhig"), ("vor", "denkt")]),
])

# ===========================================================================================================================
# C2 Abgrenzung: sofortige Beschwerde (Wortlautkarte § 793 ZPO), Faustformel
# ===========================================================================================================================
W793 = ["„Gegen Entscheidungen, die im Zwangsvollstreckungsverfahren",
        "ohne mündliche Verhandlung ergehen können, findet sofortige",
        "Beschwerde statt.“"]
w793, w793_y = wortlaut(80, 190, 1100, W793, "§ 793 ZPO", "wl793", marken=[
    (0, "Entscheidungen", beim("wl793", "Entscheidungen")), (1, "ohne mündliche Verhandlung", beim("wl793", "ohne")),
    (1, "sofortige", beim("wl793", "sofortige"))], size=32)
PA = f"{P1} › Abgrenzung, § 793 ZPO"
folie([("a793", PA), ("formel", f"{PA} › Faustformel")], [
    *tafel("a793", "Abgrenzung: sofortige Beschwerde"),
    *w793,
    pl("Faustformel", 110, w793_y + 30, "formel", fill=PINK, size=34),
    blk(110, w793_y + 115, 510, 150, BLAUHELL, beim("formel", "Vollstreckungsmaßnahmen"),
        [("Vollstreckungsmaßnahme", "ExtraBold", 32, INK), ("Erinnerung,", "Bold", 32, INK), ("§ 766 ZPO", "Bold", 32, INK)]),
    blk(640, w793_y + 115, 510, 150, LILA, beim("formel", "Entscheidungen"),
        [("Entscheidung", "ExtraBold", 32, INK), ("sofortige Beschwerde,", "Bold", 32, INK), ("§ 793 ZPO", "Bold", 32, INK)]),
    zit("BGH, Beschl. v. 12.10.2023 – IX ZB 60/21, Rn. 34", 110, w793_y + 285, beim("formel", "Entscheidungen")),
    *requisit([("a793", ("tabler", "file-text", 100, WEISS), "§ 793 ZPO", LILA),
               ("formel", ("tabler", "scale", 110, GELB), "Maßnahme oder Entscheidung?", WEISS)]),
    *paar("MB", [("a793", "denkt")], "GV", [("a793", "ruhig"), ("formel", "denkt")]),
])

# ===========================================================================================================================
# C3 Maßnahme oder Entscheidung? Anhörung, § 834 ZPO, § 11 Abs. 1 RPflG (Wortlautkarte), hier
# ===========================================================================================================================
W11 = ["„Gegen die Entscheidungen des Rechtspflegers ist das",
       "Rechtsmittel gegeben, das nach den allgemeinen",
       "verfahrensrechtlichen Vorschriften zulässig ist.“"]
w11, w11_y = wortlaut(80, 430, 1100, W11, "§ 11 Abs. 1 RPflG", "rpfl", marken=[
    (0, "Entscheidungen des Rechtspflegers", beim("rpfl", "Rechtspfleger")), (1, "allgemeinen", beim("rpfl", "allgemeinen"))],
    size=30)
folie([("anh", f"{PA} › vorherige Anhörung?"), ("pfueb", f"{PA} › Pfändungs- und Überweisungsbeschluss, § 834 ZPO"),
       ("rpfl", f"{PA} › Rechtspfleger, § 11 Abs. 1 RPflG"), ("hier793", f"{PA} › hier: keine Entscheidung")], [
    *tafel("anh", "Maßnahme oder Entscheidung?"),
    pl("oft entscheidend: Hat das Gericht vorher angehört?", 110, 175, "anh", fill=PINK, size=32),
    zit("BGH, Beschl. v. 19.12.2024 – V ZB 77/23, Rn. 13", 110, 250, beim("anh", "angehört")),
    *okz("Pfändungs- und Überweisungsbeschluss: ohne Anhörung,", 300, "pfueb", "Bold", 32, x=160),
    z("§ 834 ZPO: Der Schuldner erhebt Erinnerung.", 160, 344, beim("pfueb", "Schuldner"), "Bold", 32),
    zit("BGH, Beschl. v. 4.5.2022 – VII ZB 18/18, Rn. 25", 160, 390, beim("pfueb", "Schuldner")),
    *w11,
    z("bei Vollstreckungsentscheidungen: § 793 ZPO", 110, w11_y + 20, beim("rpfl", "Vollstreckungsentscheidungen"), "Bold", 32),
    zit("BGH, Beschl. v. 12.10.2023 – IX ZB 60/21, Rn. 34", 110, w11_y + 64, beim("rpfl", "Vollstreckungsentscheidungen")),
    blk(110, w11_y + 110, 1040, 80, GRUEN, "hier793", [("Hier pfändete der Gerichtsvollzieher: keine Entscheidung", "ExtraBold", 31, INK)]),
    *requisit([("anh", ("tabler", "ear", 100, WEISS), "Anhörung?", PINK),
               ("pfueb", ("tabler", "file-text", 100, WEISS), "ohne Anhörung", BLAUHELL),
               ("rpfl", ("tabler", "user", 100, WEISS), "Rechtspfleger", WEISS),
               ("hier793", ("tabler", "device-tv", 120, DUNKEL), "Pfändung", GRUEN)]),
    *stehend("GV", FX, [("anh", "ruhig"), ("rpfl", "denkt"), ("hier793", "ruhig")]),
])

# ===========================================================================================================================
# D 2. Zuständigkeit (§ 766 Abs. 1 S. 1, § 764 Abs. 1, 2, § 802 ZPO; Wortlautkarte § 20 Abs. 1 Nr. 17 RPflG)
# ===========================================================================================================================
W20 = ["„17. die Geschäfte im Zwangsvollstreckungsverfahren nach dem",
       "Achten Buch der Zivilprozessordnung, … mit der Maßgabe,",
       "dass dem Richter die Entscheidungen nach § 766 der",
       "Zivilprozessordnung … vorbehalten bleiben.“"]
w20, w20_y = wortlaut(80, 420, 1100, W20, "§ 20 Abs. 1 Nr. 17 RPflG (Auszug)", "richter", marken=[
    (2, "dem Richter", beim("richter", "Richter")), (3, "vorbehalten", beim("richter", "behält"))], size=30)
P2 = f"{ZA} › 2. Zuständigkeit"
folie([("zust2", P2), ("p802", f"{P2} › ausschließlich, § 802 ZPO"), ("richter", f"{P2} › Richter, § 20 Abs. 1 Nr. 17 RPflG")], [
    *tafel("zust2", "2. Zuständigkeit"),
    z("Vollstreckungsgericht: das Amtsgericht,", 110, 180, "zust2", "Bold", 36),
    z("in dessen Bezirk vollstreckt wird", 110, 228, beim("zust2", "Bezirk"), "Bold", 36),
    zit("§ 766 Abs. 1 Satz 1, § 764 Abs. 1, 2 ZPO", 110, 280, beim("zust2", "Bezirk")),
    *okz("ausschließlich, § 802 ZPO", 335, "p802", "ExtraBold", 36, x=160),
    *w20,
    pl("nicht der Rechtspfleger", 110, w20_y + 22, beim("richter", "Rechtspfleger"), fill=GELB, size=32),
    *requisit([("zust2", ("tabler", "building-bank", 130, WEISS), "Amtsgericht", BLAUHELL),
               ("p802", ("tabler", "lock", 100, GELB), "ausschließlich", GELB),
               ("richter", ("tabler", "gavel", 120, HOLZ), "der Richter entscheidet", WEISS)]),
    *stehend("MB", FX, [("zust2", "ruhig"), ("richter", "denkt")]),
])

# ===========================================================================================================================
# E 3. Erinnerungsbefugnis
# ===========================================================================================================================
P3 = f"{ZA} › 3. Erinnerungsbefugnis"
folie([("bef", P3), ("bef_s", f"{P3} › Schuldner, Gläubiger, Dritte"), ("bef_ok", f"{P3} › Herr Mühlbauer befugt (+)")], [
    *tafel("bef", "3. Erinnerungsbefugnis"),
    blk(110, 175, 1040, 80, GELB, beim("bef", "Befugt"), [("befugt: wer in eigenen Rechten betroffen ist", "ExtraBold", 34, INK)]),
    zit("BGH, Beschl. v. 13.8.2009 – I ZB 91/08, Rn. 9; Beschl. v. 30.4.2013 – VII ZB 22/12, Rn. 25", 110, 270,
        beim("bef", "Befugt")),
    pl("meist: der Schuldner", 110, 330, "bef_s", fill=LILA, size=32),
    pl("auch: die Gläubigerin oder der Gläubiger", 110, 410, "bef_g", fill=GRUEN, size=32),
    z("etwa: Gerichtsvollzieher weigert sich, den", 160, 492, beim("bef_g", "weigert"), size=32),
    z("Vollstreckungsauftrag zu übernehmen, § 766 Abs. 2 ZPO", 160, 536, beim("bef_g", "Vollstreckungsauftrag"), size=32),
    pl("mitunter: ein Dritter", 110, 600, "bef_d", fill=WEISS, size=32),
    zit("BGH, Beschl. v. 17.9.2014 – VII ZB 22/13, Rn. 19", 110, 672, "bef_d"),
    *okz("Herrn Mühlbauers Fernseher ist gepfändet: befugt", 740, "bef_ok", "ExtraBold", 34, x=160),
    *requisit([("bef", ("tabler", "users", 110, WEISS), "Wer darf rügen?", WEISS),
               ("bef_ok", ("tabler", "device-tv", 120, DUNKEL), "sein Fernseher", LILA)]),
    *stehend("MB", X1, [("bef", "ruhig"), ("bef_ok", "froh")]),
    *stehend("BE", X2, [("bef_g", "ruhig")]),
])

# ===========================================================================================================================
# F 4. Frist und Rechtsschutzbedürfnis
# ===========================================================================================================================
P4 = f"{ZA} › 4. Frist und Rechtsschutzbedürfnis"
folie([("frist", f"{ZA} › 4. keine Frist"), ("rsb", f"{P4} › bis zur Beendigung der Maßnahme"),
       ("rsb_ok", f"{ZA} › Ergebnis: zulässig (+)")], [
    *tafel("frist", "4. Frist und Rechtsschutzbedürfnis"),
    *neinz("keine Frist", 175, "frist", "ExtraBold", 38, x=160),
    z("Rechtsschutzbedürfnis: solange die beanstandete", 110, 260, "rsb", "Bold", 34),
    z("Maßnahme nicht beendet ist", 110, 306, beim("rsb", "beendet"), "Bold", 34),
    zit("BGH, Beschl. v. 2.3.2017 – I ZB 66/16, Rn. 5", 110, 352, beim("rsb", "beendet")),
    *zeitstrahl(150, 1120, 520, "rsb", [(250, "rsb", "Pfändung", WEISS, True),
                                        (1000, beim("rsb", "beendet"), "Ende: Versteigerung", WEISS, True),
                                        (620, "rsb_ok", "jetzt: Siegel klebt", GELB, False)]),
    *okz("Fernseher noch nicht versteigert", 650, beim("rsb_ok", "versteigert"), "Bold", 34, x=160),
    blk(110, 730, 1040, 80, GRUEN, beim("rsb_ok", "zulässig"), [("Ergebnis: Die Erinnerung ist zulässig.", "ExtraBold", 36, INK)]),
    *requisit([("frist", ("tabler", "hourglass", 100, WEISS), "keine Frist", WEISS),
               ("rsb", ("tabler", "calendar-event", 100, WEISS), "bis zur Beendigung", WEISS),
               ("rsb_ok", ("tabler", "circle-check", 100, GRUEN), "zulässig", GRUEN)]),
    *stehend("MB", FX, [("frist", "ruhig"), ("rsb", "denkt"), ("rsb_ok", "froh")]),
])

# ===========================================================================================================================
# G1 B. Begründetheit: § 750 Abs. 1 ZPO (Wortlautkarte, Fassung seit 1.10.2026), Zweck
# ===========================================================================================================================
W750 = ["„(1) Die Zwangsvollstreckung darf nur beginnen, wenn …",
        "2. den Personen, gegen die die Zwangsvollstreckung",
        "stattfinden soll, Folgendes zugestellt ist oder gleichzeitig",
        "zugestellt wird: a) das Urteil, …“"]
w750, w750_y = wortlaut(80, 280, 1100, W750, "§ 750 Abs. 1 Satz 1 Nr. 2 Buchst. a ZPO (Auszug)", "wl750", marken=[
    (0, "darf nur beginnen", beim("wl750", "darf")), (3, "das Urteil", beim("wl750", "Urteil")),
    (2, "zugestellt ist", beim("wl750", "zugestellt")), (2, "gleichzeitig", beim("wl750", "gleichzeitig"))], size=32)
folie([("begr", BG_), ("wl750", f"{BG_} › § 750 Abs. 1 ZPO: Zustellung"), ("zweck", f"{BG_} › Zweck: rechtliches Gehör")], [
    *tafel("begr", BG_),
    z("begründet: Verstoß gegen Vorschriften des", 110, 175, beim("begr", "begründet", nr=2), "Bold", 34),
    z("Vollstreckungsverfahrens", 110, 221, beim("begr", "Vollstreckungsverfahrens"), "Bold", 34),
    *w750,
    z("Zweck: rechtliches Gehör – der Schuldner soll die", 110, w750_y + 26, "zweck", "Bold", 33),
    z("Grundlagen der Vollstreckung prüfen können", 110, w750_y + 72, beim("zweck", "Grundlagen"), "Bold", 33),
    zit("BGH, Beschl. v. 26.9.2013 – V ZB 42/13, Rn. 9", 110, w750_y + 118, beim("zweck", "Grundlagen")),
    *requisit([("begr", ("tabler", "list-check", 100, WEISS), "Verfahrensfehler?", WEISS),
               ("wl750", ("tabler", "mail", 110, WEISS), "Zustellung", GELB),
               ("zweck", ("tabler", "ear", 100, WEISS), "rechtliches Gehör", WEISS)]),
    *paar("MB", [("begr", "ruhig"), ("zweck", "denkt")], "GV", [("begr", "ruhig"), ("wl750", "denkt")]),
])

# ===========================================================================================================================
# G2 Verstoß, nur anfechtbar, Ergebnis
# ===========================================================================================================================
folie([("verst", f"{BG_} › Verstoß gegen § 750 Abs. 1 ZPO"), ("anf", f"{BG_} › nicht unwirksam, nur anfechtbar"),
       ("begr_ok", f"{BG_} › Ergebnis: begründet (+)")], [
    *tafel("verst", "Verstoß gegen § 750 Abs. 1 ZPO"),
    *neinz("Das Urteil wurde nicht zugestellt.", 180, "verst", "ExtraBold", 36, x=160),
    z("Die Pfändung verstößt gegen § 750 ZPO.", 160, 250, beim("verst", "Pfändung"), "Bold", 34),
    blk(110, 340, 1040, 120, HELL, "anf", [("nicht unwirksam,", "ExtraBold", 36, INK), ("nur anfechtbar", "ExtraBold", 36, INK)]),
    zit("BGH, Beschl. v. 27.10.2016 – V ZB 48/15, Rn. 10", 110, 475, beim("anf", "anfechtbar")),
    blk(110, 560, 1040, 80, GRUEN, "begr_ok", [("Ergebnis: Die Erinnerung ist begründet.", "ExtraBold", 36, INK)]),
    *requisit([("verst", ("tabler", "file-x", 100, HELLROT), "nicht zugestellt", HELLROT),
               ("anf", ("tabler", "alert-triangle", 100, GELB), "anfechtbar", GELB),
               ("begr_ok", ("tabler", "circle-check", 100, GRUEN), "begründet", GRUEN)]),
    *paar("MB", [("verst", "denkt"), ("begr_ok", "froh")], "GV", [("verst", "ernst")]),
])

# ===========================================================================================================================
# G3 Achtung: der Zeitpunkt – Heilung durch Nachholung der Zustellung
# ===========================================================================================================================
folie([("zeit", f"{BG_} › Zeitpunkt der Entscheidung"), ("heil", f"{BG_} › Heilung durch Nachholung der Zustellung")], [
    *tafel("zeit", "Achtung: der Zeitpunkt"),
    blk(110, 175, 1040, 120, GELB, beim("zeit", "Maßgeblich"), [("maßgeblich: Sach- und Rechtslage bei der", "ExtraBold", 34, INK),
                                                                ("Entscheidung über die Erinnerung", "ExtraBold", 34, INK)]),
    zit("BGH, Beschl. v. 4.5.2022 – VII ZB 18/18, Rn. 23", 110, 310, beim("zeit", "Maßgeblich")),
    *zeitstrahl(150, 1120, 480, beim("zeit", "Maßgeblich"), [(250, beim("zeit", "Maßgeblich"), "Pfändung", WEISS, True),
                                                             (1000, beim("zeit", "entschieden"), "Entscheidung", GELB, True),
                                                             (620, "heil", "Zustellung nachgeholt", WEISS, False)]),
    blk(110, 640, 1040, 120, HELLROT, beim("heil", "geheilt"), [("Mangel kann geheilt werden:", "ExtraBold", 34, INK),
                                                                ("die Erinnerung wird unbegründet", "ExtraBold", 34, INK)]),
    zit("BGH, Beschl. v. 27.10.2016 – V ZB 48/15, Rn. 9 f.", 110, 775, beim("heil", "geheilt")),
    *requisit([("zeit", ("tabler", "clock", 100, WEISS), "Zeitpunkt", GELB),
               ("heil", ("tabler", "mail", 110, WEISS), "nachgeholt?", WEISS)]),
    *paar("MB", [("zeit", "ruhig"), (beim("heil", "unbegründet"), "sorge")], "BE", [("zeit", "ruhig"), ("heil", "denkt")]),
])

# ===========================================================================================================================
# H1 Entscheidung durch Beschluss, Tenor (als üblich gekennzeichnet)
# ===========================================================================================================================
folie([("ent", "Entscheidung · Beschluss, § 764 Abs. 3 ZPO"), ("tenor", "Entscheidung · Tenor (üblich)")], [
    *tafel("ent", "Die Entscheidung"),
    *okz("durch Beschluss, § 764 Abs. 3 ZPO", 180, "ent", "ExtraBold", 36, x=160),
    pl("üblicher Tenor", 110, 280, "tenor", fill=PINK, size=32),
    blk(110, 360, 1040, 150, GRUEN, beim("tenor", "Pfändung"), [("„Die Pfändung des Fernsehers", "ExtraBold", 36, INK),
                                                                ("wird für unzulässig erklärt.“", "ExtraBold", 36, INK)]),
    zit("vgl. BGH, Beschl. v. 2.3.2017 – I ZB 66/16, Rn. 5", 110, 525, beim("tenor", "Pfändung")),
    *requisit([("ent", ("tabler", "file-text", 100, WEISS), "Beschluss", WEISS),
               ("tenor", ("tabler", "gavel", 120, HOLZ), "Tenor", GRUEN)]),
    *paar("MB", [("ent", "ruhig"), (beim("tenor", "unzulässig"), "froh")], "GV", [("ent", "ruhig")]),
])

# ===========================================================================================================================
# H2 Zurück in der Wohnung: Der Gerichtsvollzieher hebt die Pfändung auf (Siegelmarke entfernt)
# ===========================================================================================================================
AB = beim("aufh", "hebt")
folie([("aufh", "Entscheidung · Aufhebung der Pfändung")], [
    *wohnung("aufh",
             [*fig("MB", MBW, BODEN, FH, [("aufh", "ruhig_r"), (AB, "froh_r")], erst="cut"),
              hart(ns("Herr Mühlbauer", MBW, BODEN, "aufh", LILA))],
             [*fig("GV", GVW, BODEN, FH, [("aufh", "ruhig")], erst="cut"),
              hart(ns("Gerichtsvollzieher", GVW, BODEN, "aufh", WEISS))]),
    bis_(hart(siegelmarke(SMX, SMY, "aufh", anim="cut")), AB),
    szene(pl("Pfändung aufgehoben", TVX, 400, AB, fill=GRUEN, size=32, anker="m"), "153abziehen*", 0.8, 0.0),
])

# ===========================================================================================================================
# H3 Eilschutz: einstweilige Anordnung (§ 766 Abs. 1 Satz 2 i. V. m. § 732 Abs. 2 ZPO, Wortlautkarte)
# ===========================================================================================================================
W732 = ["„Das Gericht kann vor der Entscheidung eine einstweilige",
        "Anordnung erlassen; es kann insbesondere anordnen, dass die",
        "Zwangsvollstreckung gegen oder ohne Sicherheitsleistung",
        "einstweilen einzustellen oder nur gegen Sicherheitsleistung",
        "fortzusetzen sei.“"]
w732, w732_y = wortlaut(80, 190, 1100, W732, "§ 732 Abs. 2 ZPO", "eil", marken=[
    (0, "vor der Entscheidung", beim("eil", "Entscheidung")), (0, "einstweilige", beim("eil", "einstweilige")),
    (3, "einstweilen einzustellen", beim("eil", "einstweilen"))], size=31)
folie([("eil", "Eilschutz · § 766 Abs. 1 Satz 2, § 732 Abs. 2 ZPO")], [
    *tafel("eil", "Eilschutz vor der Entscheidung"),
    *w732,
    pl("anwendbar über § 766 Abs. 1 Satz 2 ZPO", 110, w732_y + 30, beim("eil", "Paragraf"), fill=GELB, size=32),
    *requisit([("eil", ("tabler", "hand-stop", 100, GELB), "einstweilen einstellen", GELB)]),
    *stehend("MB", FX, [("eil", "denkt"), (beim("eil", "einstweilen"), "ruhig")]),
])

# ===========================================================================================================================
# I Merktabelle: § 766 / § 767 / § 771 ZPO
# ===========================================================================================================================
ZEILEN = [("t766", ("§ 766 ZPO", "Erinnerung"), "rügt das Verfahren der Vollstreckung", BLAUHELL),
          ("t767", ("§ 767 ZPO", "Vollstreckungsabwehrklage"), "materielle Einwendungen gegen den titulierten Anspruch", GELB),
          ("t771", ("§ 771 ZPO", "Drittwiderspruchsklage"), "ein die Veräußerung hinderndes Recht eines Dritten", LILA)]
els_tab = [karte(60, 50, 1800, 940, "tab"), titel(glyphen("Zur Abgrenzung: je eine Zeile"), 110, 90, "tab", 46)]
y = 200
for c, links, rechts, fill in ZEILEN:
    els_tab.append(blk(110, y, 640, 120, fill, c, [(links[0], "ExtraBold", 34, INK), (links[1], "ExtraBold", 32, INK)]))
    els_tab.append(z(rechts, 790, y + 38, c, "Bold", 34, rechts=1820))
    y += 165
els_tab.append(pl("Mehr dazu: unsere Videos zu den Rechtsbehelfen in der Zwangsvollstreckung,", 110, y + 20, "verw",
                  fill=WEISS, size=30))
els_tab.append(pl("zur Vollstreckungsabwehrklage und zur Drittwiderspruchsklage", 110, y + 100, "verw", fill=WEISS, size=30))
folie([("tab", "Abgrenzung · § 766, § 767, § 771 ZPO")], els_tab)

# ===========================================================================================================================
# J Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Wer hat gehandelt – und wie?"), ("tipp3", "Klausurtipp · Heilung prüfen")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Frag zuerst: Wer hat gehandelt – und wie?", 200, 200, beim("tipp", "wer"), "Bold", 36),
    pl("Faustregel", 200, 290, "tipp2", fill=PINK, size=32),
    z("Gerichtsvollzieher oder Gericht ohne Anhörung:", 200, 370, beim("tipp2", "Gerichtsvollzieher"), "Bold", 33),
    pl("Erinnerung, § 766 ZPO", 200, 420, beim("tipp2", "Erinnerung"), fill=BLAUHELL, size=32),
    z("Gericht nach Anhörung:", 200, 520, beim("tipp2", "Gericht", nr=3), "Bold", 33),
    pl("sofortige Beschwerde, § 793 ZPO", 200, 570, beim("tipp2", "sofortige"), fill=LILA, size=32),
    linienzug([(130, 670), (1130, 670)], "tipp3", breite=3),
    *okz("Begründetheit: Mangel bis zur Entscheidung geheilt?", 700, "tipp3", "Bold", 33, x=200),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# K Prüfschema
# ===========================================================================================================================
REIHEN = [("sA", 0, "A. Zulässigkeit", True),
          ("s1", 1, "1. Statthaftigkeit: Vollstreckungsmaßnahme, keine Entscheidung (sonst § 793)", False),
          ("s2", 1, "2. Zuständigkeit: Vollstreckungsgericht, ausschließlich, der Richter", False),
          ("s3", 1, "3. Erinnerungsbefugnis: in eigenen Rechten betroffen", False),
          ("s4", 1, "4. keine Frist; Rechtsschutzbedürfnis bis zur Beendigung", False),
          ("sB", 0, "B. Begründetheit", True),
          (beim("sB", "Verstoß"), 1, "Verstoß gegen Verfahrensvorschriften, z. B. § 750 Abs. 1 ZPO", False),
          (beim("sB", "Zeitpunkt"), 1, "beurteilt im Zeitpunkt der Entscheidung", False)]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Prüfschema: Erinnerung, § 766 ZPO"), 110, 90, "sch", 46)]
y = 210
for c, ebene, text, fett in REIHEN:
    x = (130, 200)[ebene]
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 40 if ebene == 0 else 35, rechts=1820))
    y += {0: 88, 1: 80}[ebene]
assert y <= 970, y
folie([("sch", "Prüfschema"), ("sA", "Prüfschema › A. Zulässigkeit"), ("sB", "Prüfschema › B. Begründetheit")], els_sch)

# ===========================================================================================================================
# L Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Ohne Zustellung, ", 0), ("spätestens gleichzeitig", "a"), (",", 0)],
                 [("darf die Vollstreckung nicht beginnen.", 0)]], 750, 290, 42, "merke",
                {"a": beim("merke", "spätestens")}),
    *markertext([[("Wer rügt, wie vollstreckt wird: ", 0), ("Erinnerung", "b"), (".", 0)],
                 [("Wer eine Entscheidung angreift:", 0)], [("sofortige Beschwerde", "c"), (".", 0)]], 750, 500, 42, "m2",
                {"b": beim("m2", "Erinnerung"), "c": beim("m2", "sofortige")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
