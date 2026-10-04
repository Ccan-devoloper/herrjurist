"""Folge 191 · Erfolgsqualifiziertes Delikt Schema: Gefahrzusammenhang & § 18 – Serienstandard Open Peeps (Katzenkönig).
Beispielfall: Bertram und Hubertus wohnen in einer Wohnung im 2. Stock. Nach einem Streit schließt Bertram Hubertus in dessen
Zimmer ein; Hubertus steigt aus dem Fenster, stürzt ab und stirbt.
Szenen laut ../SZENENPLAN.md: A1 Die Wohnung, A2 Die Frage, B Sachverhalt, C1 Struktur, C2 Wortlautkarte § 18, C3 Wortlautkarte
§ 11 Abs. 2, D Prüfungsschema, E Wortlautkarte § 239 Abs. 1, 4, F I./II. im Fall, G1 III. Formel, G2 III. Fluchtreaktion,
H IV. Fahrlässigkeit, I V. und Ergebnis, J Versuch, K Rücktritt, L fahrlässig/leichtfertig (Wortlautkarte § 251),
M Klausurtipp (Lexi), N Merksatz (Lexi).
DARSTELLUNG: kein Sturz, keine Leiche, kein Blut; Hubertus verlässt das Bild am offenen Fenster, der Tod steht nur als Text.
Ein Handlungsgeräusch (Schlüssel im Schloss; ../geraeusche_herkunft.json). Namensschild jeder Figur, solange sie im Bild ist.
Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz als eigene Kopie aus Folge 155 (gemeinsame Dateien
unverändert); neu: wohnung(), tuer(), fenster_(). Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from ostil import mond
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_191/"

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
        if n.startswith(("bild:", "ficon:", "bank")) or "/op_191/" in n:
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 103/109/112/155) ----------------------------
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


# --- Konstanten der Tafelszenen ---------------------------------------------------------------------------------------------
FB, FR = 930, 480                           # Figur neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
PX, PY, PU = 1575, 160, 380                 # Requisit über der Figur: Mitte, Pillenhöhe, Unterkante
NAME = {"BE": "Bertram", "HU": "Hubertus"}
NFARBE = {"BE": ORANGE, "HU": LILA}


def requisit(folge, px=PX, bis=None, pu=PU, py=PY):
    """Wechselndes Requisit über der Figur: folge = [(cue, (set, icon, breite, fuell), pillentext, pillenfarbe)]."""
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


# --- eigene Szenenbausteine (programmatisch, Palettenflächen, Tuschekontur) -------------------------------------------------
PFL = 880                                   # Fußboden = Standlinie der Figuren in der Fallszene
DECKE = 330                                 # Oberkante der Wände (Schnitt durch die Wohnung)
WAND_FLUR = (236, 214, 186, 255)
WAND_ZI = (228, 238, 253, 255)
BODEN_F = (214, 176, 132, 255)
GLAS = (205, 222, 246, 255)
NACHT = (84, 98, 150, 255)
TX0, TX1, TY0 = 940, 1080, 480              # Türrahmen (Wand zwischen Flur und Zimmer)
FX0, FX1, FY0, FY1 = 1600, 1800, 440, 690   # Fenster im Zimmer


def _h(c):
    return (lambda e: hart(e)) if c == NULL else (lambda e: e)


def wohnung(cue):
    """Schnitt durch die Wohnung: Flur links, Zimmer rechts, Wand mit Türöffnung, Dielenboden."""
    s = 2
    w, h = 1800, 1000 - DECKE
    im = Image.new("RGBA", (w * s, h * s))
    dr = ImageDraw.Draw(im)
    ox = 60
    P_ = lambda x, y: ((x - ox) * s, (y - DECKE) * s)
    dr.rectangle((*P_(60, DECKE), *P_(TX0 - 20, PFL)), fill=WAND_FLUR)
    dr.rectangle((*P_(TX1 + 20, DECKE), *P_(1860, PFL)), fill=WAND_ZI)
    dr.rectangle((*P_(TX0 - 20, DECKE), *P_(TX1 + 20, TY0)), fill=(222, 222, 216, 255))      # Wand über der Tür
    dr.rectangle((*P_(60, PFL), *P_(1860, 1000)), fill=BODEN_F)
    for x in range(100, 1860, 120):
        dr.line((*P_(x, PFL + 6), *P_(x, 1000)), fill=(186, 146, 104, 255), width=2 * s)
    dr.rectangle((*P_(60, DECKE), *P_(1860, 1000)), outline=INK, width=6 * s)
    dr.line((*P_(60, PFL), *P_(1860, PFL)), fill=INK, width=6 * s)
    dr.line((*P_(TX0 - 20, DECKE), *P_(TX0 - 20, TY0)), fill=INK, width=5 * s)
    dr.line((*P_(TX1 + 20, DECKE), *P_(TX1 + 20, TY0)), fill=INK, width=5 * s)
    dr.line((*P_(TX0 - 20, TY0), *P_(TX1 + 20, TY0)), fill=INK, width=5 * s)
    im = im.resize((w, h), Image.LANCZOS)
    return _h(cue)(El(im, 60, DECKE, cue, "cut", 0.0, None, name="wohnung"))


def tuer(cue, offen, bis=None):
    """Zimmertür im Rahmen: offen (Türblatt in den Flur geklappt) oder geschlossen (Holz, Klinke, Schlüsselloch)."""
    s = 2
    x0, y0, w, h = TX0 - 120, TY0, TX1 - TX0 + 140, PFL - TY0
    im = Image.new("RGBA", (w * s, (h + 4) * s))
    dr = ImageDraw.Draw(im)
    P_ = lambda x, y: ((x - x0) * s, (y - y0) * s)
    if offen:
        dr.rectangle((*P_(TX0, TY0), *P_(TX1, PFL)), fill=WAND_ZI, outline=INK, width=5 * s)
        dr.polygon([P_(TX0, TY0), P_(TX0 - 95, TY0 + 40), P_(TX0 - 95, PFL - 10), P_(TX0, PFL)], fill=HOLZ, outline=INK)
        dr.line([P_(TX0, TY0), P_(TX0 - 95, TY0 + 40), P_(TX0 - 95, PFL - 10), P_(TX0, PFL)], fill=INK, width=5 * s)
    else:
        dr.rectangle((*P_(TX0, TY0), *P_(TX1, PFL)), fill=HOLZ, outline=INK, width=5 * s)
        dr.rounded_rectangle((*P_(TX0 + 18, TY0 + 30), *P_(TX1 - 18, TY0 + 170)), 6 * s, outline=INK, width=4 * s)
        dr.rounded_rectangle((*P_(TX0 + 18, TY0 + 210), *P_(TX1 - 18, PFL - 30)), 6 * s, outline=INK, width=4 * s)
        dr.rounded_rectangle((*P_(TX0 + 8, TY0 + 182), *P_(TX0 + 44, TY0 + 196)), 5 * s, fill=INK)
        dr.ellipse((*P_(TX0 + 18, TY0 + 204), *P_(TX0 + 28, TY0 + 214)), fill=INK)
    im = im.resize((w, h + 4), Image.LANCZOS)
    return El(im, x0, y0, cue, "cut", 0.0, bis, name="tuer_" + ("offen" if offen else "zu"))


def fenster_(cue, offen, nacht=False, bis=None):
    """Fenster im Zimmer: Rahmen mit Sprossen; offen = rechter Flügel nach außen geklappt (Öffnung dunkel)."""
    s = 2
    pad = 70
    w, h = FX1 - FX0 + pad, FY1 - FY0 + 20
    im = Image.new("RGBA", (w * s, h * s))
    dr = ImageDraw.Draw(im)
    P_ = lambda x, y: ((x - FX0 + 10) * s, (y - FY0 + 10) * s)
    hinter = NACHT if nacht else GLAS
    dr.rectangle((*P_(FX0, FY0), *P_(FX1, FY1)), fill=hinter, outline=INK, width=6 * s)
    xm = (FX0 + FX1) // 2
    dr.line((*P_(xm, FY0), *P_(xm, FY1)), fill=INK, width=5 * s)
    if not offen:
        for xa, xb in ((FX0, xm), (xm, FX1)):
            dr.line((*P_(xa, (FY0 + FY1) // 2), *P_(xb, (FY0 + FY1) // 2)), fill=INK, width=4 * s)
    else:
        # rechter Flügel nach außen geklappt (Parallelogramm rechts neben dem Rahmen), Öffnung dunkel
        dr.rectangle((*P_(xm + 3, FY0 + 3), *P_(FX1 - 3, FY1 - 3)), fill=(60, 70, 110, 255) if nacht else (170, 190, 222, 255))
        dr.polygon([P_(FX1, FY0), P_(FX1 + 52, FY0 + 26), P_(FX1 + 52, FY1 - 26), P_(FX1, FY1)], fill=GLAS)
        dr.line([P_(FX1, FY0), P_(FX1 + 52, FY0 + 26), P_(FX1 + 52, FY1 - 26), P_(FX1, FY1)], fill=INK, width=5 * s)
        dr.line((*P_(FX0, (FY0 + FY1) // 2), *P_(xm, (FY0 + FY1) // 2)), fill=INK, width=4 * s)
    dr.rectangle((*P_(FX0 - 14, FY1), *P_(FX1 + 14, FY1 + 10)), fill=INK)                       # Fensterbank
    im = im.resize((w, h), Image.LANCZOS)
    return El(im, FX0 - 10, FY0 - 10, cue, "cut", 0.0, bis, name="fenster_" + ("offen" if offen else "zu"))


# ===========================================================================================================================
# A1 Fall: die Wohnung im 2. Stock
# ===========================================================================================================================
FH = 440                                    # stehende Figur in der Fallszene
BEX, HUX, HUF = 700, 1330, 1480             # Bertram im Flur (blickt nach rechts), Hubertus im Zimmer, am Fenster
folie([(NULL, "Fall · Die Wohnung"), ("streit", "Fall · Der Streit"), ("schloss", "Fall · Die Tür"),
       ("fenster", "Fall · Das Fenster")], [
    wohnung(NULL),
    hart(tuer(NULL, True, bis="schloss")),
    tuer("schloss", False),
    hart(fenster_(NULL, False, bis="streit")),
    fenster_("streit", False, nacht=True, bis=beim("fenster", "steigt")),
    fenster_(beim("fenster", "steigt"), True, nacht=True),
    mond(1650, 515, 26, "streit"),
    hart(pl("Wohnung im 2. Stock", 70, 30, NULL, fill=GELB, size=40)),
    pl("Bertram und Hubertus wohnen zusammen", 70, 120, beim("wg", "wohnen"), fill=WEISS, size=34, bis="schloss"),
    pl("Streit am Abend", 70, 205, "streit", fill=HELLROT, size=34, bis="schloss"),
    # Bertram im Flur, Hubertus im Zimmer
    *fig("BE", BEX, PFL, FH, [("wg", "ruhig_r"), ("streit", "ernst_r"), ("h1", "denkt_r")], bis="b1"),
    *redet("BE_redet_r", BEX, PFL, FH, "b1", "schloss"),
    *fig("BE", BEX, PFL, FH, [("schloss", "ernst_r"), ("fenster", "still_r"), ("nicht", "sorge_r")], erst="cut"),
    ns("Bertram", BEX, PFL, "wg", ORANGE, d=0.1),
    *fig("HU", HUX, PFL, FH, [("wg", "ruhig"), ("streit", "sorge")], bis="h1"),
    *redet("HU_redet", HUX, PFL, FH, "h1", "b1"),
    *fig("HU", HUX, PFL, FH, [("b1", "ernst"), ("schloss", "angst")], bis="h2", erst="cut"),
    *redet("HU_redet", HUX, PFL, FH, "h2", "fenster"),
    bis_(ns("Hubertus", HUX, PFL, "wg", LILA, d=0.1), "fenster"),
    peep_voll("HU_denkt_r", HUF, PFL, FH, "fenster", anim="cut", bis="tod"),
    bis_(ns("Hubertus", HUF, PFL, "fenster", LILA, anim="cut"), "tod"),
    blase("sprech", 520, 190, "h1", 1420, 225, inhalt=["Lass mich einfach", "in Ruhe!"], textsize=38,
          figur=("HU_redet", HUX, PFL, FH), bis="b1"),
    blase("sprech", 600, 190, "b1", 1110, 225, inhalt=["Du bleibst da drin, bis", "du dich beruhigt hast."], textsize=36,
          figur=("BE_redet_r", BEX, PFL, FH), bis="schloss"),
    blase("sprech", 500, 190, "h2", 1420, 225, inhalt=["Mach sofort", "die Tür auf!"], textsize=38,
          figur=("HU_redet", HUX, PFL, FH), bis="fenster"),
    # abgeschlossen: Schloss an der Tür, Schlüssel bei Bertram
    szene(ficon("tabler", "lock", TX1 - 25, TY0 + 260, 56, "schloss", fuell=GELB), "191schloss*", 0.7, -0.2),
    pl("Tür von außen abgeschlossen", 70, 120, "schloss", fill=WEISS, size=34, bis="fenster"),
    ficon("tabler", "key", BEX + 110, PFL - 150, 70, beim("schloss", "Schlüssel"), fuell=GELB),
    pl("Schlüssel nimmt er mit", 70, 205, beim("schloss", "nimmt"), fill=WEISS, size=34, bis="fenster"),
    # Flucht durchs Fenster: nur Fenster und Text, kein Sturz im Bild
    pl("will hinaus: durchs Fenster", 70, 120, "fenster", fill=WEISS, size=34, bis="nicht"),
    pl("stürzt ab und stirbt", 70, 205, "tod", fill=HELLROT, size=34, bis="nicht"),
    pl("wollte ihn nur eine Weile einsperren", 70, 120, "nicht", fill=WEISS, size=34),
    pl("Flucht durchs Fenster: nicht gerechnet", 70, 205, beim("nicht", "Mit"), fill=WEISS, size=34),
])

# ===========================================================================================================================
# A2 Fall: die Frage
# ===========================================================================================================================
folie([("frage", "Fall · Die Frage")], rechts_frei([
    *tafel("frage", "Die Frage"),
    pl("Haftet Bertram für den Tod?", 110, 220, "frage", fill=PINK, size=40),
    pl("Wie prüfst du ein erfolgsqualifiziertes Delikt?", 110, 340, "frage2", fill=WEISS, size=36),
    *requisit([("frage", ("tabler", "scale", 110, GELB), "Tod: Haftung?", PINK),
               ("frage2", ("tabler", "list-numbers", 100, WEISS), "Prüfungsschema", WEISS)]),
    *stehend("BE", FX, [("frage", "sorge")]),
]))


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_191(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=34, zeilenabstand=1.30)
        els += e; y += 18
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_191("sv", [
    "Bertram und Hubertus wohnen zusammen in einer Wohnung im 2. Stock. Eines Abends streiten sie. Hubertus: „Lass mich "
    "einfach in Ruhe!“ Bertram: „Du bleibst da drin, bis du dich beruhigt hast.“",
    "Bertram schließt die Zimmertür von außen ab und nimmt den Schlüssel mit. Hubertus: „Mach sofort die Tür auf!“",
    "Hubertus will hinaus und steigt aus dem Fenster. Er stürzt ab und stirbt. Bertram wollte ihn nur eine Weile "
    "einsperren; mit einer Flucht durchs Fenster hat er nicht gerechnet.",
], "Wie hat sich Bertram strafbar gemacht?")

# ===========================================================================================================================
# C1 Struktur: Grunddelikt + schwere Folge
# ===========================================================================================================================
PE = "Erfolgsqualifikation · Struktur"
folie([("eq", PE), ("eq2", f"{PE} › Grunddelikt + schwere Folge"), ("v155", f"{PE} › allgemeines Schema")], rechts_frei([
    *tafel("eq", "Erfolgsqualifiziertes Delikt"),
    *okz("Bertram: Hubertus vorsätzlich eingesperrt", 190, beim("eq", "vorsätzlich"), "Bold", 34, x=160),
    *okz("daraus folgte der Tod", 250, beim("eq", "Tod"), "Bold", 34, x=160),
    blk(110, 340, 1040, 110, GELB, "eq2", [("vorsätzliches Grunddelikt  +  schwere Folge", "ExtraBold", 40, INK)]),
    z("mit höherer Strafe", 110, 475, beim("eq2", "höherer"), "Bold", 34),
    linienzug([(130, 560), (1130, 560)], "v155", breite=3),
    z("Faustschlag mit tödlichem Sturz:", 110, 590, "v155", "Bold", 32),
    z("Video „Körperverletzung mit Todesfolge“", 110, 640, beim("v155", "Video"), "Bold", 30, farbe=TEXT),
    z("Hier: das allgemeine Schema", 110, 720, beim("v155", "Hier"), "ExtraBold", 36),
    *requisit([("eq", ("tabler", "lock", 90, GELB), "Grunddelikt", WEISS),
               ("eq2", ("tabler", "plus", 100, WEISS), "Erfolgsqualifikation", GELB),
               ("v155", ("tabler", "list-numbers", 100, WEISS), "allgemeines Schema", WEISS)]),
    *stehend("BE", FX, [("eq", "ernst"), ("v155", "denkt")]),
]))

# ===========================================================================================================================
# C2 Wortlautkarte § 18
# ===========================================================================================================================
W18 = ["„Knüpft das Gesetz an eine besondere Folge der Tat eine",
       "schwerere Strafe, so trifft sie den Täter oder den Teilnehmer",
       "nur, wenn ihm hinsichtlich dieser Folge wenigstens",
       "Fahrlässigkeit zur Last fällt.“"]
w18, w18_y = wortlaut(80, 170, 1100, W18, "§ 18 StGB", "p18", marken=[
    (0, "besondere Folge", beim("p18", "besondere")), (1, "schwerere Strafe", beim("p18", "schwerere")),
    (1, "Teilnehmer", beim("p18", "Teilnehmer")), (2, "wenigstens", beim("p18", "wenigstens")),
    (3, "Fahrlässigkeit", beim("p18", "Fahrlässigkeit"))], size=34)
P18 = "Erfolgsqualifikation › § 18 StGB"
folie([("p18", f"{P18}: wenigstens Fahrlässigkeit"), ("wenig", f"{P18}: Vorsatz bezüglich der Folge")], rechts_frei([
    *tafel("p18", "Die Grundregel: § 18 StGB"),
    *w18,
    blk(110, w18_y + 40, 505, 110, BLAU, beim("vf", "Vorsatz"), [("Vorsatz:", "Bold", 32, INK), ("Grunddelikt", "ExtraBold", 36, INK)]),
    blk(645, w18_y + 40, 505, 110, GRUEN, beim("vf", "wenigstens"), [("wenigstens Fahrlässigkeit:", "Bold", 32, INK),
                                                                      ("schwere Folge", "ExtraBold", 36, INK)]),
    pl("Vorsatz bezüglich der Folge schadet nicht", 110, w18_y + 185, "wenig", fill=GELB, size=34),
    *requisit([("p18", ("tabler", "book", 100, WEISS), "§ 18 StGB", GELB),
               ("vf", ("tabler", "scale", 100, GELB), "Vorsatz + Fahrlässigkeit", WEISS),
               ("wenig", None, "wenigstens", GELB)]),
    *stehend("BE", FX, [("p18", "ernst"), ("vf", "denkt"), ("wenig", "ernst")]),
]))

# ===========================================================================================================================
# C3 Wortlautkarte § 11 Abs. 2: Teilnahme und Versuch
# ===========================================================================================================================
W112 = ["„(2) Vorsätzlich im Sinne dieses Gesetzes ist eine Tat auch dann,",
        "wenn sie einen gesetzlichen Tatbestand verwirklicht, der",
        "hinsichtlich der Handlung Vorsatz voraussetzt, hinsichtlich einer",
        "dadurch verursachten besonderen Folge jedoch Fahrlässigkeit",
        "ausreichen läßt.“"]
w112, w112_y = wortlaut(80, 170, 1100, W112, "§ 11 Abs. 2 StGB", "p112", marken=[
    (2, "Vorsatz voraussetzt", beim("p112", "Vorsatz")), (3, "Fahrlässigkeit", beim("p112", "Vorsatz")),
    (0, "Vorsätzlich", beim("p112", "vorsätzliche")), (0, "ist eine Tat", beim("p112", "vorsätzliche"))], size=31)
P11 = "Erfolgsqualifikation › § 11 Abs. 2 StGB"
folie([("p112", f"{P11}: vorsätzliche Tat"), ("teiln", f"{P11} › Teilnahme"), ("versuch", f"{P11} › Versuch")],
      rechts_frei([
    *tafel("p112", "Vorsätzliche Tat: § 11 Abs. 2 StGB", size=42),
    *w112,
    *okz("Anstiftung, Beihilfe: vorsätzliche Haupttat (§§ 26, 27)", w112_y + 40, "teiln", "Bold", 31, x=160),
    z("Teilnehmer: selbst wenigstens fahrlässig bezüglich der Folge", 160, w112_y + 100, "teiln2", size=31),
    *okz("Versuch möglich", w112_y + 165, "versuch", "Bold", 34, x=160),
    *requisit([("p112", ("tabler", "book", 100, WEISS), "§ 11 Abs. 2 StGB", GELB),
               ("teiln", ("tabler", "link", 100, WEISS), "Teilnahme möglich", GRUEN),
               ("versuch", ("tabler", "help-circle", 100, WEISS), "Versuch möglich", GRUEN)]),
    *stehend("BE", FX, [("p112", "ernst"), ("teiln", "denkt")]),
]))

# ===========================================================================================================================
# D Prüfungsschema (progressiv, breit)
# ===========================================================================================================================
REIHEN = [("s1", "I. Grunddelikt: objektiver und subjektiver Tatbestand", None),
          ("s2", "II. schwere Folge und Kausalität", None),
          ("s3", "III. spezifischer Gefahrzusammenhang", None),
          ("s4", "IV. wenigstens Fahrlässigkeit bezüglich der Folge", ("manchmal Leichtfertigkeit, z. B. Raub mit Todesfolge, § 251 StGB", beim("s4", "manchmal"))),
          ("s5", "V. Rechtswidrigkeit und Schuld", ("Schuld: auch die subjektive Vorhersehbarkeit", beim("s5", "dort")))]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfungsschema: erfolgsqualifiziertes Delikt"), 110, 90, "sch", 50)]
y = 210
for c, text, unter in REIHEN:
    if c == "s3":
        els_sch.append(karte(110, y - 16, 1700, 78, c, fill=HELLGRUEN, rund=16, schatten=5, rand=4))
    els_sch.append(z(text, 140, y, c, "ExtraBold", 42, rechts=1800))
    y += 90
    if unter:
        els_sch.append(z(unter[0], 210, y - 18, unter[1], "Regular", 34, farbe=TEXT, rechts=1800))
        y += 62
assert y <= 960, y
PS_ = "Prüfungsschema"
folie([("sch", PS_), ("s1", f"{PS_} › I. Grunddelikt"), ("s2", f"{PS_} › II. schwere Folge, Kausalität"),
       ("s3", f"{PS_} › III. spezifischer Gefahrzusammenhang"), ("s4", f"{PS_} › IV. wenigstens Fahrlässigkeit"),
       ("s5", f"{PS_} › V. Rechtswidrigkeit und Schuld")], els_sch)

# ===========================================================================================================================
# E Wortlautkarte § 239 Abs. 1, 4
# ===========================================================================================================================
W239 = ["„(1) Wer einen Menschen einsperrt oder auf andere Weise der",
        "Freiheit beraubt, wird mit Freiheitsstrafe bis zu fünf Jahren",
        "oder mit Geldstrafe bestraft. …",
        "(4) Verursacht der Täter durch die Tat oder eine während der Tat",
        "begangene Handlung den Tod des Opfers, so ist die Strafe",
        "Freiheitsstrafe nicht unter drei Jahren.“"]
w239, w239_y = wortlaut(80, 170, 1100, W239, "§ 239 Abs. 1, 4 StGB", "p239", marken=[
    (3, "durch die Tat", beim("abs4", "Tat")), (4, "den Tod des Opfers", beim("abs4", "Tod")),
    (5, "nicht unter drei Jahren", beim("abs4", "nicht"))], size=32)
folie([("p239", "Fall › § 239 Abs. 4 StGB: Freiheitsberaubung mit Todesfolge")], rechts_frei([
    *tafel("p239", "Freiheitsberaubung mit Todesfolge", size=44),
    *w239,
    pl("Abs. 4: mindestens 3 Jahre", 110, w239_y + 35, beim("abs4", "nicht"), fill=HELLROT, size=34),
    *requisit([("p239", ("tabler", "book", 100, WEISS), "§ 239 Abs. 4 StGB", GELB),
               (beim("abs4", "Tod"), ("tabler", "alert-triangle", 100, GELB), "Todesfolge", HELLROT)]),
    *stehend("BE", FX, [("p239", "ernst"), (beim("abs4", "nicht"), "still")]),
]))

# ===========================================================================================================================
# F I. Grunddelikt, II. schwere Folge und Kausalität
# ===========================================================================================================================
folie([("gd", "Fall › I. Grunddelikt: Einsperren"), ("fenst", "Fall › I. Einsperren trotz Fenster"),
       ("vors", "Fall › I. Vorsatz"), ("folge", "Fall › II. schwere Folge: Tod"), ("kaus", "Fall › II. Kausalität"),
       ("nurk", "Fall › II. Kausalität genügt nicht")], rechts_frei([
    *tafel("gd", "Im Fall: I. und II."),
    *okz("I. § 239 Abs. 1: Hubertus eingesperrt", 180, beim("gd", "Bertram"), "Bold", 34, x=160),
    z("Fenster? Einsperren muss nicht unüberwindlich sein,", 160, 240, "fenst", size=32),
    z("gewöhnlicher Ausgang versperrt: genügt", 160, 287, beim("fenst", "es"), "Bold", 32),
    zit("BGH, Beschl. v. 8.3.2001 – 1 StR 590/00, Rn. 1", 160, 334, beim("fenst", "es")),
    *okz("Vorsatz (+)", 390, "vors", "Bold", 34, x=160),
    z("Vorsatzformen: Video „Vorsatzformen“", 400, 395, beim("vors", "mehr"), "Bold", 30, farbe=TEXT),
    linienzug([(130, 470), (1130, 470)], "folge", breite=3),
    *okz("II. schwere Folge: Hubertus ist tot", 500, "folge", "Bold", 34, x=160),
    *okz("Kausalität: ohne Einsperren kein Hinausklettern", 565, "kaus", "Bold", 32, x=160),
    *neinz("bloße Kausalität reicht nicht", 630, "nurk", "Bold", 34, x=160),
    *requisit([("gd", ("tabler", "lock", 90, GELB), "eingesperrt", WEISS),
               ("fenst", ("tabler", "window", 100, BLAUHELL), "kein gewöhnlicher Ausgang", WEISS),
               ("vors", None, "Vorsatz (+)", GRUEN),
               ("folge", ("tabler", "alert-triangle", 100, GELB), "Tod", HELLROT),
               ("kaus", ("tabler", "link", 100, WEISS), "Kausalität (+)", WEISS),
               ("nurk", ("tabler", "help-circle", 100, WEISS), "reicht nicht", HELLROT)]),
    *stehend("BE", FX, [("gd", "ernst"), ("folge", "still"), ("nurk", "denkt")]),
]))

# ===========================================================================================================================
# G1 III. Spezifischer Gefahrzusammenhang: Formel
# ===========================================================================================================================
PG = "Fall › III. spezifischer Gefahrzusammenhang"
folie([("spez", PG), ("formel", f"{PG} › Zweck der Erfolgsqualifikation")], rechts_frei([
    *tafel("spez", "III. Spezifischer Gefahrzusammenhang", size=42),
    z("Der Kern der Prüfung", 110, 180, "spez", "Bold", 34),
    blk(110, 250, 1040, 170, LILA, "formel", [("Erfolgsqualifizierte Delikte sollen der", "ExtraBold", 34, INK),
                                              ("Gefahr entgegenwirken, die mit dem", "ExtraBold", 34, INK),
                                              ("jeweiligen Grunddelikt verbunden ist.", "ExtraBold", 34, INK)]),
    zit("BGH, Beschl. v. 15.2.2017 – 4 StR 375/16 (BGHSt 62, 49), Rn. 14 f.", 110, 438, "formel"),
    z("Gerade diese Gefahr muss sich", 110, 500, "nieder", "Bold", 36),
    z("in der Folge niederschlagen.", 110, 552, beim("nieder", "in"), "Bold", 36),
    *requisit([("spez", ("tabler", "alert-triangle", 100, GELB), "spezifische Gefahr", LILA),
               ("nieder", ("tabler", "link", 100, WEISS), "Gefahr verwirklicht?", WEISS)]),
    *stehend("BE", FX, [("spez", "ernst"), ("nieder", "denkt")]),
]))

# ===========================================================================================================================
# G2 III. im Fall: Fluchtreaktion, Abgrenzung Selbstgefährdung
# ===========================================================================================================================
folie([("typ", f"{PG} › Fluchtreaktion"), ("selbst", f"{PG} › Abgrenzung: Selbstgefährdung"),
       ("hier", f"{PG} › Hubertus wollte entkommen"), ("gz_ok", "Fall › III. Gefahrzusammenhang (+)")], rechts_frei([
    *tafel("typ", "III. Im Fall: die Flucht"),
    z("Wer eingesperrt ist, will hinaus.", 110, 180, "typ", "Bold", 36),
    *okz("riskanter Fluchtversuch: typische Gefahr", 245, "typ2", "Bold", 34, x=160),
    z("der Freiheitsberaubung", 160, 292, beim("typ2", "Freiheitsberaubung"), "Bold", 34),
    z("BGH 1964: auch Folgen eines Selbstbefreiungsversuchs", 160, 355, "bgh64", size=32),
    zit("BGHSt 19, 382, 386 f., zitiert nach BGH, Urt. v. 28.1.2021 – 3 StR 279/20, Rn. 18", 160, 402, "bgh64"),
    blk(110, 460, 1040, 110, HELLROT, "selbst", [("anders: frei verantwortliche Selbstgefährdung,", "Bold", 32, INK),
                                                 ("Verhalten nicht von der Tat bestimmt", "Bold", 32, INK)]),
    zit("vgl. BGHSt 62, 49, Rn. 17, 20", 110, 590, "selbst"),
    *okz("Hubertus: Flucht, um der Freiheitsberaubung zu entkommen", 645, "hier", "Bold", 30, x=160),
    blk(110, 720, 1040, 80, GRUEN, "gz_ok", [("III. Gefahrzusammenhang (+)", "ExtraBold", 38, INK)]),
    *requisit([("typ", ("tabler", "window", 110, BLAUHELL), "Flucht durchs Fenster", WEISS),
               ("selbst", ("tabler", "arrows-split", 100, WEISS), "frei verantwortlich?", HELLROT),
               ("hier", ("tabler", "lock", 90, GELB), "Flucht aus dem Einsperren", WEISS),
               ("gz_ok", ("tabler", "link", 100, WEISS), "Gefahrzusammenhang (+)", GRUEN)]),
    *stehend("BE", FX, [("typ", "ernst"), ("selbst", "denkt"), ("gz_ok", "still")]),
]))

# ===========================================================================================================================
# H IV. Fahrlässigkeit
# ===========================================================================================================================
folie([("fahrl", "Fall › IV. Fahrlässigkeit, § 18 StGB"), ("vorh", "Fall › IV. Vorhersehbarkeit"),
       ("v182", "Fall › IV. Fahrlässigkeit, § 18 StGB")], rechts_frei([
    *tafel("fahrl", "IV. Fahrlässigkeit"),
    *okz("Pflichtwidrigkeit: liegt schon im Grunddelikt", 180, beim("fahrl", "Pflichtwidrigkeit"), "Bold", 34, x=160),
    z("entscheidend: die Vorhersehbarkeit", 160, 245, "vorh", "ExtraBold", 34),
    zit("BGH, Beschl. v. 15.2.2017 – 4 StR 375/16 (BGHSt 62, 49), Rn. 22", 160, 293, "vorh"),
    z("BGH 2021, Sturz aus dem Fenster:", 110, 360, "bgh21", "Bold", 34),
    *okz("Fluchtversuch: Folge in der Regel vorhersehbar", 420, beim("bgh21", "Bei"), "Bold", 32, x=160),
    z("natürliches Bestreben, sich der", 160, 475, beim("bgh21", "weil"), size=32),
    z("Freiheitsberaubung zu entziehen", 160, 520, beim("bgh21", "weil"), size=32),
    zit("BGH, Urt. v. 28.1.2021 – 3 StR 279/20, Rn. 18", 160, 567, beim("bgh21", "weil")),
    z("Mehr: Video „Fahrlässigkeitsdelikt“", 110, 640, "v182", "Bold", 30, farbe=TEXT),
    *requisit([("fahrl", ("tabler", "scale", 100, GELB), "§ 18 StGB", WEISS),
               ("vorh", ("tabler", "bulb", 100, GELB), "vorhersehbar?", WEISS),
               ("bgh21", ("tabler", "window", 110, BLAUHELL), "BGH 2021", WEISS),
               (beim("bgh21", "Bei"), ("tabler", "bulb", 100, GELB), "in der Regel vorhersehbar", GRUEN)]),
    *stehend("BE", FX, [("fahrl", "ernst"), ("bgh21", "denkt"), ("v182", "ernst")]),
]))

# ===========================================================================================================================
# I V. Rechtswidrigkeit und Schuld, Ergebnis
# ===========================================================================================================================
folie([("rws", "Fall › V. Rechtswidrigkeit und Schuld"), ("erg", "Fall › Ergebnis: § 239 Abs. 4 StGB")], rechts_frei([
    *tafel("rws", "V. Rechtswidrigkeit, Schuld"),
    *okz("rechtswidrig und schuldhaft", 190, beim("rws", "rechtswidrig"), "Bold", 36, x=160),
    *okz("subjektive Vorhersehbarkeit: auch für Bertram", 260, beim("rws", "auch"), "Bold", 34, x=160),
    z("persönlich war der tödliche Ausgang vorhersehbar", 160, 315, beim("rws", "persönlich"), size=32),
    blk(110, 420, 1040, 130, GRUEN, "erg", [("Ergebnis: Freiheitsberaubung mit Todesfolge,", "Bold", 34, INK),
                                            ("§ 239 Abs. 4 StGB", "ExtraBold", 42, INK)]),
    *requisit([("rws", ("tabler", "scale", 100, GELB), "Rechtswidrigkeit, Schuld", WEISS),
               ("erg", ("tabler", "gavel", 100, HOLZ), "§ 239 Abs. 4 StGB", GRUEN)]),
    *stehend("BE", FX, [("rws", "still"), ("erg", "sorge")]),
]))

# ===========================================================================================================================
# J Versuch: zwei Konstellationen
# ===========================================================================================================================
LX0, RX0, SW = 110, 640, 510
folie([("vers", "Versuch · zwei Fälle"), ("eqv", "Versuch · erfolgsqualifizierter Versuch"),
       ("veq", "Versuch · versuchte Erfolgsqualifikation")], rechts_frei([
    *tafel("vers", "Versuch: zwei Fälle"),
    z("Zwei Fälle trennen", 110, 180, "zwei", "Bold", 34),
    karte(LX0, 240, SW, 560, "eqv", fill=HELL, rund=18, schatten=6, rand=4),
    z("erfolgsqualifizierter", LX0 + 25, 258, "eqv", "ExtraBold", 32, rechts=LX0 + SW - 10),
    z("Versuch", LX0 + 25, 300, "eqv", "ExtraBold", 32, rechts=LX0 + SW - 10),
    z("Grunddelikt: nur versucht", LX0 + 25, 365, beim("eqv", "Grunddelikt"), size=30, rechts=LX0 + SW - 10),
    z("schwere Folge: tritt ein", LX0 + 25, 410, beim("eqv", "doch"), "Bold", 30, rechts=LX0 + SW - 10),
    z("Beispiel: versuchter Raub,", LX0 + 25, 480, "eqv2", size=30, rechts=LX0 + SW - 10),
    z("ein Schuss tötet,", LX0 + 25, 522, beim("eqv2", "löst"), size=30, rechts=LX0 + SW - 10),
    z("keine Beute", LX0 + 25, 564, beim("eqv2", "Beute"), size=30, rechts=LX0 + SW - 10),
    zit("BGH, Urt. v. 14.5.1996 –", LX0 + 25, 625, beim("eqv2", "Beute"), rechts=LX0 + SW - 10),
    zit("1 StR 51/96 (BGHSt 42, 158)", LX0 + 25, 662, beim("eqv2", "Beute"), rechts=LX0 + SW - 10),
    karte(RX0, 240, SW, 560, "veq", fill=LILAHELL, rund=18, schatten=6, rand=4),
    z("versuchte", RX0 + 25, 258, "veq", "ExtraBold", 32, rechts=RX0 + SW - 10),
    z("Erfolgsqualifikation", RX0 + 25, 300, "veq", "ExtraBold", 32, rechts=RX0 + SW - 10),
    z("Grunddelikt: verwirklicht", RX0 + 25, 365, beim("veq", "Grunddelikt"), size=30, rechts=RX0 + SW - 10),
    z("Folge gewollt oder in Kauf", RX0 + 25, 410, beim("veq", "die"), "Bold", 30, rechts=RX0 + SW - 10),
    z("genommen: bleibt aus", RX0 + 25, 450, beim("veq", "bleibt"), "Bold", 30, rechts=RX0 + SW - 10),
    z("Beispiel: Wohnhaus in Brand,", RX0 + 25, 520, "veq2", size=30, rechts=RX0 + SW - 10),
    z("Tod der Bewohner einkalkuliert,", RX0 + 25, 562, beim("veq2", "rechnet"), size=30, rechts=RX0 + SW - 10),
    z("alle überleben", RX0 + 25, 604, beim("veq2", "alle"), size=30, rechts=RX0 + SW - 10),
    zit("BGH, Urt. v. 12.8.2021 –", RX0 + 25, 665, beim("veq2", "alle"), rechts=RX0 + SW - 10),
    zit("3 StR 415/20, Rn. 9, 15", RX0 + 25, 702, beim("veq2", "alle"), rechts=RX0 + SW - 10),
    *requisit([("vers", ("tabler", "arrows-split", 100, WEISS), "Versuch", WEISS),
               ("eqv", None, "Folge tritt ein", GELB),
               ("veq", None, "Folge bleibt aus", LILA)]),
    *stehend("BE", FX, [("vers", "denkt")]),
]))

# ===========================================================================================================================
# K Rücktritt vom erfolgsqualifizierten Versuch
# ===========================================================================================================================
folie([("rt", "Versuch · Rücktritt"), ("rt3", "Versuch · Rücktritt › bezieht sich auf das Grunddelikt"),
       ("rt4", "Versuch · Rücktritt › bleibt: fahrlässige Tötung")], rechts_frei([
    *tafel("rt", "Rücktritt"),
    z("Und der Rücktritt?", 110, 180, "rt", "Bold", 36),
    z("BGH 1996, versuchter Raub mit Todesfolge:", 110, 250, "rt2", "Bold", 34),
    zit("BGH, Urt. v. 14.5.1996 – 1 StR 51/96 (BGHSt 42, 158), Rn. 12, 16 f.", 110, 298, "rt2"),
    *okz("Rücktritt vom Raubversuch noch möglich,", 355, beim("rt2", "Vom"), "Bold", 34, x=160),
    z("auch wenn der Tod schon eingetreten ist", 160, 405, beim("rt2", "auch"), size=34),
    z("Rücktritt bezieht sich auf das Grunddelikt", 110, 485, "rt3", "Bold", 34),
    z("entfällt es, fehlt der Anknüpfungspunkt für die Folge", 110, 535, beim("rt3", "Entfällt"), size=32),
    blk(110, 610, 1040, 90, LILAHELL, "rt4", [("bleibt: fahrlässige Tötung, § 222 StGB", "ExtraBold", 36, INK)]),
    zit("vgl. BGHSt 42, 158, Rn. 26", 110, 720, "rt4"),
    *requisit([("rt", ("tabler", "arrow-back-up", 100, WEISS), "Rücktritt?", WEISS),
               ("rt3", ("tabler", "link", 100, WEISS), "Anknüpfung: Grunddelikt", GELB),
               ("rt4", None, "§ 222 StGB", LILA)]),
    *stehend("BE", FX, [("rt", "denkt"), ("rt4", "ernst")]),
]))

# ===========================================================================================================================
# L Fahrlässig oder leichtfertig (Wortlautkarte § 251)
# ===========================================================================================================================
W251 = ["„Verursacht der Täter durch den Raub (§§ 249 und 250) wenigstens",
        "leichtfertig den Tod eines anderen Menschen, so ist die Strafe",
        "lebenslange Freiheitsstrafe oder Freiheitsstrafe nicht unter",
        "zehn Jahren.“"]
w251, w251_y = wortlaut(80, 300, 1100, W251, "§ 251 StGB", "p251", marken=[
    (0, "wenigstens", beim("p251", "wenigstens")), (1, "leichtfertig", beim("p251", "leichtfertig"))], size=31)
PL = "IV. Fahrlässigkeit oder Leichtfertigkeit"
folie([("wf", PL), ("p251", f"{PL} › § 251 StGB: wenigstens leichtfertig"), ("lf", f"{PL} › Leichtfertigkeit")], rechts_frei([
    *tafel("wf", "Fahrlässig oder leichtfertig?"),
    blk(110, 170, 1040, 100, GRUEN, "wf", [("Norm schweigt: Fahrlässigkeit genügt,", "Bold", 32, INK),
                                           ("z. B. § 239 Abs. 4 StGB", "ExtraBold", 34, INK)]),
    *w251,
    z("leichtfertig = gesteigerte Fahrlässigkeit:", 110, w251_y + 25, "lf", "ExtraBold", 33),
    z("sich aufdrängende Möglichkeit des tödlichen Verlaufs", 110, w251_y + 75, "lf2", size=31),
    z("aus besonderem Leichtsinn oder besonderer", 110, w251_y + 118, beim("lf2", "aus"), size=31),
    z("Gleichgültigkeit außer Acht gelassen", 110, w251_y + 161, beim("lf2", "Gleichgültigkeit"), size=31),
    zit("BGH, Urt. v. 3.6.2015 – 5 StR 628/14, Rn. 8", 110, w251_y + 208, beim("lf2", "Gleichgültigkeit")),
    *requisit([("wf", ("tabler", "scale", 100, GELB), "fahrlässig", GRUEN),
               ("p251", ("tabler", "book", 100, WEISS), "§ 251 StGB", GELB),
               ("lf", ("tabler", "alert-triangle", 100, GELB), "leichtfertig", HELLROT)]),
    *stehend("BE", FX, [("wf", "ernst"), ("lf", "denkt")]),
]))

# ===========================================================================================================================
# M Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · typische Gefahr des Grunddelikts"), ("tipp2", "Klausurtipp · Wortlaut: leichtfertig?")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Gefahrzusammenhang: Welche typische", 200, 200, beim("tipp", "Frag"), "Bold", 36),
    z("Gefahr schafft gerade dieses Grunddelikt?", 200, 250, beim("tipp", "welche"), "Bold", 36),
    z("Einsperren: die Flucht", 200, 320, beim("tipp", "Einsperren"), "ExtraBold", 36),
    linienzug([(130, 400), (1130, 400)], "tipp2", breite=3),
    z("Wortlaut lesen:", 200, 430, "tipp2", "Bold", 36),
    z("„leichtfertig“: einfache Fahrlässigkeit", 200, 490, beim("tipp2", "Steht"), size=34),
    z("reicht nicht", 200, 540, beim("tipp2", "reicht"), "Bold", 34),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "merke"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# N Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Vorsätzliches Grunddelikt,", 0)], [("schwere Folge, ", 0), ("spezifischer", "a")],
                 [("Gefahrzusammenhang", "a"), (",", 0)], [("wenigstens Fahrlässigkeit.", 0)]], 750, 270, 44, "merke",
                {"a": beim("merke", "spezifischer")}),
    *markertext([[("Als vorsätzliche Tat:", 0)], [("Versuch", "b"), (" und ", 0), ("Teilnahme", "c"), (" möglich.", 0)]],
                750, 620, 44, "m2", {"b": beim("m2", "Versuch"), "c": beim("m2", "Teilnahme")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
