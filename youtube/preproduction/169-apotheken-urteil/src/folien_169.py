"""Folge 169 · Drei-Stufen-Theorie: Das Apotheken-Urteil zur Berufsfreiheit – Serienstandard Open Peeps (Katzenkönig).
Moderner Einstieg mit fiktiven Figuren (Grete, Apothekerin; Herr Dannemann, Sachbearbeiter der Erlaubnisbehörde), danach
der echte Fall sachlich: BVerfG, Urt. v. 11.6.1958 – 1 BvR 596/56, BVerfGE 7, 377 (Seiten der amtlichen Sammlung nach DFR).
Der reale Beschwerdeführer wird weder benannt noch dargestellt; im echten Fall stehen keine Figuren im Bild. Apotheken nur
mit neutralen Icons (Tabler pill/pills), kein geschütztes Apothekenzeichen, keine Ketten oder Logos.
Szenen laut ../SZENENPLAN.md. Hilfsfunktionen glyphen/z/pl/tafel/blk/redet/fig/ns/okz/neinz/requisit/stehend/paar als eigene
Kopie aus Folge 150 (gemeinsame Dateien unverändert); neu: umbruch(), wortlaut() mit automatischem Umbruch, laden(),
treppe(), stufentafel(). Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from ostil import titel, karte, pille
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_169/"

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
FASSADE = (252, 240, 222, 255)
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
    e = pille(glyphen(text), *a, **k)
    assert e.x >= 24 and e.x + e.sprite.width <= 1896, f"Pille aus dem Bild: {text}"
    return e


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
        if n.startswith(("bild:", "ficon:", "bank", "treppe")) or "/op_169/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def umbruch(text, size, breite, stil="Regular"):
    """Zeilenumbruch nach Schriftbreite."""
    f = F(stil, size)
    zeilen, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if f.getlength(t) <= breite:
            cur = t
        else:
            zeilen.append(cur); cur = w
    if cur:
        zeilen.append(cur)
    return zeilen


def wortlaut(x, y, w, text, quelle, cue, marken=(), size=32, bis=None):
    """Wortlautkarte: Normtext wörtlich (Quelle und Abrufdatum in RECHTSSTAND.md), als Zitat mit Normangabe; Umbruch nach
    Schriftbreite. marken = [(wort, cue)] legt synchron zum gesprochenen Wort einen Textmarker hinter das (erste) Vorkommen."""
    zeilen = text if isinstance(text, list) else umbruch(text, size, w - 56)
    lh = int(size * 1.42)
    hgt = 40 + lh * len(zeilen) + 46
    els = [bis_(karte(x, y, w, hgt, cue, fill=ZITAT, rund=18, schatten=6, rand=4), bis)]
    f = F("Regular", size)
    tx, ty = x + 28, y + 26
    for wort, mc in marken:
        zi = next(i for i, t in enumerate(zeilen) if wort in t)
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
    els.append(z(quelle, tx, ty + len(zeilen) * lh + 4, cue, "Bold", max(26, size - 4), farbe=TEXT, rechts=x + w - 16, bis=bis))
    return els, y + hgt


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 103/109/112/150) ----------------------------
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


BODEN = 860
FH = 440                                    # stehende Figur in der Fallszene
X1, X2 = 1430, 1730                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"GR": "Grete", "DA": "Herr Dannemann"}
NFARBE = {"GR": GRUEN, "DA": BLAUHELL}
STUFE = {1: (BLAU, BLAUHELL), 2: (LILA, LILAHELL), 3: (ROT, HELLROT)}


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


def laden(x0, x1, cue, schild_text=None, fenster=(), oben=BODEN - 400):
    """Ladenfassade aus Grundformen: Fassade, Schildband (optional mit Schriftzug und Tabler-Icon „pill“), Schaufenster
    und Tür. fenster = Icons (set, name, breite, fuell) im Schaufenster. Kein geschütztes Apothekenzeichen."""
    w, h = x1 - x0, BODEN - oben
    im, dr, s = _flaeche(w, h)
    o = 6 * s
    dr.rectangle((o, o, o + w * s, o + h * s), fill=FASSADE, outline=INK, width=5 * s)
    dr.rectangle((o, o, o + w * s, o + 76 * s), fill=GRUEN if schild_text else WEISS, outline=INK, width=5 * s)
    fx0, fy0, fx1, fy1 = o + 28 * s, o + 120 * s, o + int(w * 0.58) * s, o + (h - 70) * s
    dr.rectangle((fx0, fy0, fx1, fy1), fill=BLAUHELL, outline=INK, width=5 * s)
    tx0, ty0, tx1 = o + int(w * 0.66) * s, o + 130 * s, o + (w - 30) * s
    dr.rectangle((tx0, ty0, tx1, o + h * s), fill=HOLZ, outline=INK, width=5 * s)
    dr.ellipse((tx0 + 18 * s, ty0 + int((h - 130) * 0.5) * s, tx0 + 32 * s, ty0 + int((h - 130) * 0.5) * s + 14 * s), fill=INK)
    im = im.resize((w + 12, h + 12), Image.LANCZOS)
    if schild_text:
        f = F("ExtraBold", 44)
        ic = ficon("tabler", "pill", 0, 0, 52, "_", fuell=WEISS).sprite
        tw = f.getlength(schild_text)
        gx = int((w + 12 - tw - ic.width - 14) / 2)
        im.alpha_composite(ic, (gx, int(44 - ic.height / 2)))
        ImageDraw.Draw(im).text((gx + ic.width + 14, 16), glyphen(schild_text), font=f, fill=INK)
    fxm, fym = (28 + int(w * 0.58)) / 2 + 6, (120 + h - 70) / 2 + 6
    for k, (st, nm, br, fu) in enumerate(fenster):
        ic = ficon(st, nm, 0, 0, br, "_", fuell=fu).sprite
        dx = (k - (len(fenster) - 1) / 2) * (br + 18)
        im.alpha_composite(ic, (int(fxm + dx - ic.width / 2), int(fym - ic.height / 2)))
    return hart(El(im, x0 - 6, oben - 6, cue, "cut", 0.0, None, name="laden"))


_TR = {}


def treppe(x0, unten, sb, sh, cue, aktiv=None, bis=None, anim="cut", zahlen=True, name="treppe"):
    """Drei Stufen aus Grundformen (Stufe 1 Blau, 2 Lila, 3 Rot); aktiv = hervorgehobene Stufe (übrige hell)."""
    key = (sb, sh, aktiv, zahlen)
    if key not in _TR:
        w, h = 3 * sb, 3 * sh
        im, dr, s = _flaeche(w, h)
        o = 6 * s
        for i in range(3):
            voll, hell = STUFE[i + 1]
            fill = voll if aktiv in (None, i + 1) else hell
            dr.rectangle((o + i * sb * s, o + (h - (i + 1) * sh) * s, o + (i + 1) * sb * s, o + h * s), fill=fill,
                         outline=INK, width=(7 if aktiv == i + 1 else 5) * s)
        im = im.resize((w + 12, h + 12), Image.LANCZOS)
        if zahlen:
            f = F("ExtraBold", max(30, int(sh * 0.55)))
            dr2 = ImageDraw.Draw(im)
            for i in range(3):
                t = str(i + 1)
                tw = f.getlength(t)
                dr2.text((6 + i * sb + (sb - tw) / 2, 6 + h - (i + 1) * sh + sh * 0.18), t, font=f, fill=INK)
        _TR[key] = im
    im = _TR[key]
    return El(im, x0 - 6, unten - im.height + 6, cue, anim, 0.0, bis, name=name)


def stufenkopf(nr, titel_, cue, y=180, zusatz=None, zusatz_cue=None):
    """Farbiger Kopf einer Stufentafel (gleiche Struktur für alle drei Stufen)."""
    voll, _ = STUFE[nr]
    zeilen = [(titel_, "ExtraBold", 34, INK)] + ([(zusatz, "Regular", 32, INK)] if zusatz else [])
    if zusatz and zusatz_cue:
        return [blk(110, y, 1040, 80, voll, cue, zeilen[:1]),
                blk(110, y, 1040, 130, voll, zusatz_cue, zeilen)]
    return [blk(110, y, 1040, 130 if zusatz else 80, voll, cue, zeilen)]


def zeile_label(text, y, cue, farbe=TEXT):
    return z(text, 110, y, cue, "ExtraBold", 30, farbe=farbe)


# ===========================================================================================================================
# A1 Fall: Grete will in ihrem Stadtteil eine Apotheke eröffnen (fiktiv)
# ===========================================================================================================================
GX, DX, DX0 = 1150, 1620, 1745               # Grete vor dem leeren Laden, Herr Dannemann (kommt von rechts herein)


def strasse(cue, leer_icon=False):
    return [boden(cue),
            laden(70, 500, cue, "Apotheke", fenster=[("tabler", "pills", 70, GELB), ("tabler", "first-aid-kit", 70, WEISS)]),
            laden(560, 960, cue, None, fenster=[("tabler", "pill", 90, GRUEN)] if leer_icon else [])]


A_DA = [szene(bewegt(peep_voll("DA_ruhig", DX, BODEN, FH, beim("laden", "Erlaubnis"), anim="cut", bis="h1"),
                     beim("laden", "Erlaubnis"), (beim("laden", "Erlaubnis")[0], round(T_(beim("laden", "Erlaubnis")) - T_("laden") + 1.5, 3)),
                     DX0 - DX, 0), "169schritte*", 0.8, 0.05),
        bewegt(ns("Herr Dannemann", DX, BODEN, beim("laden", "Erlaubnis"), BLAUHELL, anim="cut"), beim("laden", "Erlaubnis"),
               (beim("laden", "Erlaubnis")[0], round(T_(beim("laden", "Erlaubnis")) - T_("laden") + 1.5, 3)), DX0 - DX, 0),
        *redet("DA_redet", DX, BODEN, FH, "h1", "o1"),
        *fig("DA", DX, BODEN, FH, [("o1", "denkt")], bis="frage0", erst="cut")]
folie([(NULL, "Fall · Grete will eine Apotheke eröffnen"), ("h1", "Fall · Die Erlaubnis wird versagt"),
       ("o1", "Fall · Darf der Staat das?")], [
    *strasse(NULL),
    laden(560, 960, beim("laden", "eigene"), None, fenster=[("tabler", "pill", 90, GRUEN)]),
    pl("eigene Apotheke", 760, 380, beim("laden", "eigene"), fill=GRUEN, size=32, anker="m", bis="h1"),
    *fig("GR", GX, BODEN, FH, [(NULL, "froh"), ("laden", "ruhig"), ("h1", "denkt_r"), (beim("h1", "genug"), "sorge_r")],
         bis="o1", erst="cut"),
    *redet("GR_redet_r", GX, BODEN, FH, "o1", "frage0"),
    hart(ns("Grete", GX, BODEN, NULL, GRUEN)),
    ficon("tabler", "certificate", 1150, 330, 110, beim("fall", "Approbation"), fuell=GELB, bis="h1"),
    pl("Apothekerin mit Approbation", 1150, 80, beim("fall", "Approbation"), fill=WEISS, size=30, anker="m", bis="h1"),
    pl("Antrag auf Erlaubnis", 1150, 150, beim("laden", "beantragt"), fill=GELB, size=30, anker="m", bis="h1"),
    ficon("tabler", "file-text", 1390, 640, 90, beim("laden", "beantragt"), fuell=WEISS),
    nein(1445, 560, beim("h1", "nicht"), gr=34),
    pl("Erlaubnis versagt", 1390, 680, beim("h1", "nicht"), fill=HELLROT, size=30, anker="m"),
    pl("schon genug Apotheken", 285, 380, beim("h1", "genug"), fill=HELLROT, size=32, anker="m"),
    *A_DA,
    blase("sprech", 780, 250, "h1", 1290, 230, inhalt=["Die Erlaubnis bekommen Sie nicht.", "In Ihrem Stadtteil gibt es",
                                                    "schon genug Apotheken."], textsize=31,
          figur=("DA_redet", DX, BODEN, FH), bis="o1"),
    blase("sprech", 760, 200, "o1", 1400, 230, inhalt=["Aber ich bin voll ausgebildet!", "Darf der Staat mich deshalb",
                                                    "aussperren?"], textsize=31,
          figur=("GR_redet_r", GX, BODEN, FH), bis="frage0"),
])

# ===========================================================================================================================
# A2 Die Frage
# ===========================================================================================================================
folie([("frage0", "Die Frage · Bedarf als Grenze?"), ("klassiker", "Die Frage · Das Apotheken-Urteil")], [
    *tafel("frage0", "Grete will eine Apotheke eröffnen"),
    z("Die Behörde versagt die Erlaubnis: genug Apotheken.", 110, 190, "frage0", "Bold", 34),
    pl("Darf der Staat die Zahl der Apotheken", 110, 270, beim("frage0", "Darf"), fill=PINK, size=36),
    pl("nach dem Bedarf begrenzen?", 110, 350, beim("frage0", "Bedarf"), fill=PINK, size=36),
    blk(110, 480, 1040, 120, GELB, "klassiker", [("Das Apotheken-Urteil des", "ExtraBold", 34, INK),
                                              ("Bundesverfassungsgerichts, 1958", "ExtraBold", 34, INK)]),
    zit("BVerfG, Urt. v. 11.6.1958 – 1 BvR 596/56, BVerfGE 7, 377", 110, 615, "klassiker"),
    *requisit([("frage0", ("tabler", "pills", 120, GELB), "Bedarf?", WEISS),
               ("klassiker", ("tabler", "scale", 110, GELB), "Apotheken-Urteil", GELB)]),
    *paar("GR", [("frage0", "sorge")], "DA", [("frage0", "ruhig"), ("klassiker", "denkt")]),
])

# ===========================================================================================================================
# B1 Der echte Fall: Traunreut 1956, Art. 3 Abs. 1 ApothekenG (BVerfGE 7, 377 <379 f.>) – ohne Figuren
# ===========================================================================================================================
W3 = ("„(1) Für eine neuzuerrichtende Apotheke darf die Betriebserlaubnis nur erteilt werden, wenn a) die Errichtung "
      "der Apotheke zur Sicherung der Versorgung der Bevölkerung mit Arzneimitteln im öffentlichen Interesse liegt und "
      "b) anzunehmen ist, daß ihre wirtschaftliche Grundlage gesichert ist und durch sie die wirtschaftliche Grundlage der "
      "benachbarten Apotheken nicht soweit beeinträchtigt wird, daß die Voraussetzungen für den ordnungsgemäßen "
      "Apothekenbetrieb nicht mehr gewährleistet sind. …“")
w3, w3_y = wortlaut(80, 345, 1100, W3, "Art. 3 Abs. 1 ApothekenG Bayern (Fassung 1955), zitiert nach BVerfGE 7, 377 <380>",
                    "norm", marken=[("öffentlichen Interesse", beim("norm", "öffentlichen")),
                                    ("wirtschaftliche Grundlage gesichert", beim("wirt", "wirtschaftliche")),
                                    ("benachbarten Apotheken", beim("wirt", "Nachbarapotheken"))], size=30)
assert w3_y <= 890, w3_y
folie([("bf", "Der echte Fall · Traunreut 1956"), ("norm", "Der echte Fall · Art. 3 Abs. 1 ApothekenG"),
       ("wirt", "Der echte Fall · Art. 3 Abs. 1 ApothekenG › wirtschaftliche Grundlage")], [
    *tafel("bf", "Der echte Fall"),
    z("ein angestellter Apotheker", 110, 175, "bf", "Bold", 34),
    z("1956: Antrag auf Erlaubnis für eine eigene Apotheke", 110, 222, beim("bf", "Erlaubnis"), "Bold", 34),
    z("in Traunreut, Oberbayern", 110, 269, beim("bf", "Traunreut"), "Bold", 34),
    zit("BVerfGE 7, 377 <379 f.>", 600, 279, beim("bf", "Traunreut")),
    *w3,
    *requisit([("bf", ("tabler", "certificate", 110, GELB), "angestellter Apotheker", WEISS),
               (beim("bf", "Traunreut"), ("tabler", "map-pin", 100, ROT), "Traunreut, Oberbayern", WEISS),
               ("norm", ("tabler", "book", 100, WEISS), "Art. 3 Abs. 1 ApothekenG", GELB),
               (beim("norm", "öffentlichen"), ("tabler", "pills", 110, GELB), "öffentliches Interesse?", WEISS),
               ("wirt", ("tabler", "coin", 100, GELB), "wirtschaftliche Grundlage?", WEISS)], pu=560, py=230),
    ficon("tabler", "building-store", 1575, 860, 220, beim("bf", "eigene"), fuell=GRUEN),
])

# ===========================================================================================================================
# B2 Ablehnung und Verfassungsbeschwerde (<381 f.>)
# ===========================================================================================================================
folie([("abl", "Der echte Fall · Die Behörde lehnt ab"), ("vb", "Der echte Fall · Verfassungsbeschwerde"),
       ("frage", "Der echte Fall · Die Frage")], [
    *tafel("abl", "Die Behörde lehnt ab"),
    zit("Regierung von Oberbayern, Bescheid vom 29.11.1956", 110, 170, "abl"),
    *neinz("rund 6.000 Menschen: Die eine vorhandene", 230, beim("abl", "sechstausend"), "Bold", 34, x=160),
    z("Apotheke genügt völlig.", 160, 278, beim("abl", "genüge"), "Bold", 34),
    *neinz("Ihr Umsatz würde um 40 % sinken.", 360, "umsatz", "Bold", 34, x=160),
    zit("BVerfGE 7, 377 <381>", 160, 410, "umsatz"),
    blk(110, 480, 1040, 90, GELB, "vb", [("Der Apotheker erhebt Verfassungsbeschwerde.", "ExtraBold", 34, INK)]),
    zit("<382>", 110, 585, "vb"),
    pl("Verletzt die Regelung seine Berufsfreiheit?", 110, 650, "frage", fill=PINK, size=36),
    *requisit([("abl", ("tabler", "building", 110, WEISS), "Regierung von Oberbayern", WEISS),
               (beim("abl", "sechstausend"), ("tabler", "pill", 110, GRUEN), "eine Apotheke genügt", HELLROT),
               ("umsatz", ("tabler", "trending-down", 110, HELLROT), "Umsatz: 40 % weniger", HELLROT),
               ("vb", ("tabler", "building-bank", 120, WEISS), "Verfassungsbeschwerde", GELB),
               ("frage", ("tabler", "scale", 110, PINK), "Berufsfreiheit verletzt?", PINK)], pu=620, py=260),
])


# ===========================================================================================================================
# C Sachverhalt
# ===========================================================================================================================
def sachverhalt_169(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 205
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=32, zeilenabstand=1.28)
        els += e; y += 14
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_169("sv", [
    "Ein seit 1940 approbierter Apotheker arbeitet als Angestellter in einer Apotheke in Traunstein. Im Juli 1956 "
    "beantragt er bei der Regierung von Oberbayern die Erlaubnis, in Traunreut eine eigene Apotheke zu eröffnen.",
    "Nach Art. 3 Abs. 1 des bayerischen Apothekengesetzes darf die Erlaubnis für eine neue Apotheke nur erteilt werden, "
    "wenn ihre Errichtung zur Sicherung der Arzneimittelversorgung im öffentlichen Interesse liegt und wenn ihre "
    "wirtschaftliche Grundlage gesichert ist, ohne die der benachbarten Apotheken so weit zu beeinträchtigen, dass ein "
    "ordnungsgemäßer Apothekenbetrieb nicht mehr gewährleistet ist.",
    "Die Behörde lehnt am 29. November 1956 ab: Für die rund 6.000 Menschen, die von Traunreut aus zu versorgen sind, "
    "genüge die eine vorhandene Apotheke völlig; deren Umsatz würde um 40 % sinken. Der Apotheker erhebt "
    "Verfassungsbeschwerde.",
], "Verletzt die Regelung ihn in seinem Grundrecht aus Art. 12 Abs. 1 GG?")

# ===========================================================================================================================
# D1 Art. 12 Abs. 1 GG (Wortlautkarte), Berufsbegriff (<397>), Schritt in die Selbständigkeit (<399>)
# ===========================================================================================================================
PI = "Berufsfreiheit, Art. 12 Abs. 1 GG"
W12 = ["„(1) Alle Deutschen haben das Recht, Beruf, Arbeitsplatz und",
       "Ausbildungsstätte frei zu wählen. Die Berufsausübung kann",
       "durch Gesetz oder auf Grund eines Gesetzes geregelt werden. …“"]
w12, w12_y = wortlaut(80, 175, 1100, W12, "Art. 12 Abs. 1 GG", "a12", marken=[
    ("Beruf,", beim("a12", "Beruf")), ("frei zu wählen", beim("a12", "wählen")),
    ("Berufsausübung", beim("a12", "Berufsausübung")), ("geregelt", beim("a12", "geregelt"))], size=33)
folie([("a12", f"{PI} · Wortlaut"), ("beruf", f"{PI} › Berufsbegriff"), ("selbst", f"{PI} › Schritt in die Selbständigkeit")], [
    *tafel("a12", "Die Berufsfreiheit"),
    *w12,
    *okz("Beruf: jede erlaubte Tätigkeit, die man zur", w12_y + 40, "beruf", "Bold", 34, x=160),
    z("Grundlage seiner Lebensführung macht", 160, w12_y + 88, beim("beruf", "Grundlage"), "Bold", 34),
    z("auch eine untypische", 160, w12_y + 136, beim("beruf", "untypische"), size=34),
    zit("BVerfGE 7, 377, Leitsatz 1; <397>", 160, w12_y + 186, beim("beruf", "untypische")),
    *okz("vom angestellten zum selbständigen Apotheker:", w12_y + 260, "selbst", "Bold", 34, x=160),
    z("selbst eine Berufswahl", 160, w12_y + 308, beim("selbst", "Berufswahl"), "ExtraBold", 34),
    zit("<399>", 160, w12_y + 358, beim("selbst", "Berufswahl")),
    *requisit([("a12", ("tabler", "book", 100, WEISS), "Art. 12 Abs. 1 GG", GELB),
               ("beruf", ("tabler", "briefcase", 110, HOLZ), "Beruf", WEISS),
               ("selbst", ("tabler", "building-store", 120, GRUEN), "selbständig", GRUEN)]),
    *stehend("GR", FX, [("a12", "ruhig"), ("beruf", "denkt"), ("selbst", "froh")]),
])

# ===========================================================================================================================
# D2 Wahl und Ausübung: einheitliches Grundrecht (<400–403>; Leitsatz 5)
# ===========================================================================================================================
folie([("wahl", f"{PI} › Wahl und Ausübung"), ("einheit", f"{PI} › einheitliches Grundrecht"),
       ("intens", f"{PI} › je näher an der Wahl, desto enger")], [
    *tafel("wahl", "Wahl und Ausübung"),
    pl("Wortlaut: nur die Ausübung regeln?", 110, 175, "wahl", fill=PINK, size=34),
    zit("BVerfGE 7, 377 <400 f.>", 760, 192, "wahl"),
    blk(110, 270, 560, 100, LILA, "trenn", [("Berufswahl", "ExtraBold", 36, INK)]),
    blk(590, 270, 560, 100, BLAU, "trenn", [("Berufsausübung", "ExtraBold", 36, INK)]),
    z("Wer einen Beruf aufnimmt, übt ihn aus und", 110, 395, beim("trenn", "aufnimmt"), "Bold", 34),
    z("wählt ihn zugleich.", 110, 443, beim("trenn", "wählt"), "Bold", 34),
    zit("<401>", 440, 453, beim("trenn", "wählt")),
    blk(110, 515, 1040, 90, GELB, "einheit", [("ein einheitliches Grundrecht der Berufsfreiheit", "ExtraBold", 34, INK)]),
    z("Regelungsvorbehalt in Satz 2: für Ausübung und Wahl", 110, 625, beim("einheit", "Regelungsvorbehalt"), size=33),
    zit("<402>", 110, 672, beim("einheit", "Regelungsvorbehalt")),
    pl("Je mehr die Berufswahl berührt ist,", 110, 725, "intens", fill=HELLROT, size=34),
    pl("desto enger die Grenzen.", 110, 800, beim("intens", "enger"), fill=HELLROT, size=34),
    zit("Leitsatz 5; <402 f.>", 600, 818, beim("intens", "enger")),
    *requisit([("wahl", ("tabler", "book", 100, WEISS), "Wortlaut", WEISS),
               ("trenn", ("tabler", "layers-intersect", 110, LILA), "nicht trennbar", WEISS),
               ("einheit", ("tabler", "shield-check", 110, GELB), "ein Grundrecht", GELB),
               ("intens", ("tabler", "lock", 100, HELLROT), "Berufswahl: enger", HELLROT)]),
    *paar("GR", [("wahl", "denkt"), ("einheit", "froh")], "DA", [("wahl", "ruhig"), ("intens", "denkt")]),
])

# ===========================================================================================================================
# E0 Mehrere Stufen (<405>); die Lehre: Drei-Stufen-Theorie
# ===========================================================================================================================
PS_ = "Die drei Stufen"
folie([("stufen", f"{PS_} › Drei-Stufen-Theorie")], [
    *tafel("stufen", "Mehrere Stufen"),
    zit("BVerfGE 7, 377 <405>: „gewissermaßen mehrere ‚Stufen‘“", 110, 168, "stufen"),
    hart(treppe(250, 700, 230, 140, "stufen", anim="fade", name="treppe_tafel")),
    pl("die Lehre: Drei-Stufen-Theorie", 110, 760, beim("stufen", "Lehre"), fill=PINK, size=36),
    *paar("GR", [("stufen", "ruhig")], "DA", [("stufen", "denkt")]),
])


def stufenfolie(nr, pfade, kopf, kopf_cue, def_zeilen, bsp, recht, extra, figur, mini_cue):
    """Gleiche Struktur für jede Stufe: farbiger Kopf (Was?), Beispiel, Rechtfertigung (+ Zusatz); rechts die
    Treppe mit der aktiven Stufe und eine Figur."""
    els = [*tafel(kopf_cue, f"Stufe {nr}"), *stufenkopf(nr, kopf, kopf_cue)]
    y = 285
    for text, c in def_zeilen:
        els.append(z(text, 110, y, c, "Bold", 33)); y += 46
    if bsp:
        y += 14
        els.append(zeile_label("Beispiel", y, bsp[0][1])); y += 44
        for text, c, _q in bsp:
            els.append(z(text, 110, y, c, size=34)); y += 48
        els.append(zit(bsp[-1][2], 110, y, bsp[-1][1])); y += 40
    y += 14
    els.append(zeile_label("Rechtfertigung", y, recht[0][1])); y += 44
    voll, hell = STUFE[nr]
    rz = [(t, "ExtraBold", 33, INK) for t, _ in recht]
    # Block wächst Zeile für Zeile mit dem gesprochenen Wort (kein Text vor dem Wort)
    stufen_ = [k for k in range(len(recht)) if k + 1 == len(recht) or recht[k + 1][1] != recht[k][1]]
    for j, k in enumerate(stufen_):
        nxt = recht[stufen_[j + 1]][1] if j + 1 < len(stufen_) else None
        c0 = recht[stufen_[j - 1] + 1][1] if j else recht[0][1]
        els.append(blk(110, y, 1040, 30 + 48 * (k + 1), hell, c0, rz[:k + 1], anim="rise" if j == 0 else "cut", bis=nxt))
    y += 30 + 48 * len(recht) + 12
    els.append(zit(extra[0], 110, y, recht[0][1])); y += 50
    if len(extra) > 1:
        els.append(pl(extra[1], 110, y, extra[2], fill=HELLROT, size=34)); y += 70
    assert y <= 890, f"Stufe {nr} zu lang ({y})"
    els.append(hart(treppe(1350, 400, 160, 85, mini_cue, aktiv=nr, anim="fade")))
    els += stehend(*figur)
    folie(pfade, rechts_frei(els))


stufenfolie(1, [("s1", f"{PS_} › Stufe 1: Berufsausübung"), ("s1r", f"{PS_} › Stufe 1 › Rechtfertigung")],
            "Berufsausübung", "s1", [("wie jemand seinen Beruf ausübt", beim("s1", "wie"))],
            [("Pflichten zur Vorratshaltung in der Apotheke", beim("s1", "Vorratshaltung"), "BVerfGE 7, 377 <414, 441>")],
            [("„soweit vernünftige Erwägungen des Gemeinwohls", "s1r"), ("es zweckmäßig erscheinen lassen“", beim("s1r", "zweckmäßig"))],
            ["BVerfGE 7, 377 <405>; Leitsatz 6 a"], ("DA", FX, [("s1", "ruhig"), ("s1r", "denkt")]), "s1")
stufenfolie(2, [("s2", f"{PS_} › Stufe 2: subjektive Zulassungsvoraussetzung"), ("s2r", f"{PS_} › Stufe 2 › Rechtfertigung")],
            "subjektive Zulassungsvoraussetzung", "s2", [("liegt in der Person", beim("s2", "Person"))],
            [("vor allem die Ausbildung,", beim("s2", "Ausbildung"), ""),
             ("beim Apotheker die Approbation", beim("s2", "Approbation"), "<406>; Approbation: <380, 444>")],
            [("Schutz besonders wichtiger Gemeinschaftsgüter;", "s2r"),
             ("nicht außer Verhältnis zum Zweck ordnungsgemäßer", beim("s2r", "Verhältnis")),
             ("Berufsausübung", beim("s2r", "Verhältnis"))],
            ["Leitsatz 6 b, c; <405, 407>"], ("GR", FX, [("s2", "ruhig"), (beim("s2", "Approbation"), "froh")]), "s2")
stufenfolie(3, [("s3", f"{PS_} › Stufe 3: objektive Zulassungsvoraussetzung"), ("s3r", f"{PS_} › Stufe 3 › Rechtfertigung"),
                ("konk", f"{PS_} › Stufe 3 › kein Konkurrenzschutz")],
            "objektive Zulassungsvoraussetzung", "s3",
            [("hat mit der Person nichts zu tun:", beim("s3", "Person")),
             ("Der Bewerber kann sie nicht beeinflussen.", beim("s3", "beeinflussen"))], None,
            [("„nachweisbarer oder höchstwahrscheinlicher", beim("s3r", "nachweisbarer")),
             ("schwerer Gefahren für ein überragend", beim("s3r", "schwerer")),
             ("wichtiges Gemeinschaftsgut“", beim("s3r", "wichtiges"))],
            ["BVerfGE 7, 377 <406–408>; Leitsatz 6 c", "Bloßer Konkurrenzschutz reicht nie.", "konk"],
            ("GR", FX, [("s3", "denkt"), ("konk", "sorge")]), "s3")

# ===========================================================================================================================
# E4 Grundsatz: niedrigste Stufe zuerst (<408>); Lehre: konkretisierte Verhältnismäßigkeit
# ===========================================================================================================================
folie([("gr", f"{PS_} › niedrigste Stufe zuerst"), ("naechst", f"{PS_} › nächste Stufe nur, wenn die vorige nicht reicht"),
       ("vh", f"{PS_} › konkretisierte Verhältnismäßigkeit")], [
    *tafel("gr", "Die niedrigste Stufe zuerst"),
    *okz("Der Gesetzgeber wählt die Stufe, die am", 185, "gr", "Bold", 34, x=160),
    z("wenigsten in die Berufswahl eingreift.", 160, 233, beim("gr", "wenigsten"), "Bold", 34),
    zit("BVerfGE 7, 377 <408>; Leitsatz 6 d", 160, 283, beim("gr", "wenigsten")),
    blk(110, 345, 1040, 130, GELB, "naechst", [("Die nächste Stufe erst, wenn die Gefahren", "ExtraBold", 34, INK),
                                            ("mit Mitteln der vorigen Stufe nicht", "ExtraBold", 34, INK)]),
    blk(110, 345, 1040, 180, GELB, beim("naechst", "wirksam"), [("Die nächste Stufe erst, wenn die Gefahren", "ExtraBold", 34, INK),
                                                             ("mit Mitteln der vorigen Stufe nicht", "ExtraBold", 34, INK),
                                                             ("wirksam zu bekämpfen sind", "ExtraBold", 34, INK)]),
    zit("<408>", 110, 540, beim("naechst", "wirksam")),
    pl("Lehre: konkretisierte Verhältnismäßigkeit", 110, 610, "vh", fill=PINK, size=36),
    zit("Wie man die Verhältnismäßigkeit prüft: eigene Folge", 110, 700, beim("vh", "Folge")),
    hart(treppe(1330, 820, 175, 150, "gr", aktiv=1, anim="fade", bis="naechst")),
    hart(treppe(1330, 820, 175, 150, "naechst", aktiv=2, bis="vh")),
    hart(treppe(1330, 820, 175, 150, "vh")),
    pfeil(1420, 600, 1590, 480, beim("naechst", "nächste"), breite=10, kopf=30, bis="vh"),
    pl("geringster Eingriff", 1590, 200, "gr", fill=BLAUHELL, size=30, anker="m", bis="naechst"),
    pl("nächste Stufe erst später", 1590, 200, "naechst", fill=GELB, size=30, anker="m", bis="vh"),
    pl("Verhältnismäßigkeit", 1590, 200, "vh", fill=PINK, size=30, anker="m"),
    ficon("tabler", "scale", 1590, 380, 110, "vh", fuell=PINK),
])

# ===========================================================================================================================
# F1 Anwendung: Bedürfnisprüfung = objektive Zulassungsvoraussetzung (<393 f., 431>)
# ===========================================================================================================================
PA = "Anwendung"
folie([("einord", f"{PA} › das bayerische Gesetz"), ("obj", f"{PA} › objektive Zulassungsvoraussetzung (Stufe 3)")], [
    *tafel("einord", "Und das bayerische Gesetz?"),
    *stufenkopf(3, "Stufe 3: objektive Zulassungsvoraussetzung", "obj", y=470),
    zeile_label("Beispiel", 185, "einord"),
    z("Wird am Ort noch eine Apotheke gebraucht?", 110, 229, beim("einord", "gebraucht"), size=34),
    z("Trägt sie sich wirtschaftlich?", 110, 277, beim("einord", "trägt"), size=34),
    *neinz("nicht in der Hand des Bewerbers", 345, beim("einord", "Hand"), "Bold", 34, x=160),
    zit("BVerfGE 7, 377 <393 f., 407>", 160, 395, beim("einord", "Hand")),
    *okz("Prüfung von Bedarf und Tragfähigkeit: die", 580, beim("obj", "Prüfung"), "Bold", 34, x=160),
    z("schärfste Stufe", 160, 628, beim("obj", "schärfste"), "ExtraBold", 34),
    zit("<431>", 160, 678, beim("obj", "schärfste")),
    hart(treppe(1350, 400, 160, 85, "einord", aktiv=None, anim="fade", bis="obj")),
    hart(treppe(1350, 400, 160, 85, "obj", aktiv=3)),
    *stehend("GR", FX, [("einord", "denkt"), ("obj", "sorge")]),
])

# ===========================================================================================================================
# F2 Volksgesundheit, keine Gefahr, mildere Stufen (<414–416, 431 f., 438>)
# ===========================================================================================================================
folie([("volk", f"{PA} › Volksgesundheit"), ("gefahr", f"{PA} › keine Gefahr belegt (−)"),
       ("milder", f"{PA} › mildere Stufen genügen")], [
    *tafel("volk", "Droht eine Gefahr?"),
    *okz("Volksgesundheit: unbestritten ein wichtiges", 180, "volk", "Bold", 34, x=160),
    z("Gemeinschaftsgut", 160, 228, beim("volk", "wichtiges"), "Bold", 34),
    zit("BVerfGE 7, 377 <414>", 160, 278, beim("volk", "wichtiges")),
    *neinz("Das Gericht ist nicht überzeugt, dass ohne", 345, "gefahr", "Bold", 34, x=160),
    z("die Beschränkung eine Gefahr droht.", 160, 393, beim("gefahr", "Gefahr"), "Bold", 34),
    zit("<415>", 160, 443, beim("gefahr", "Gefahr")),
    z("vergleichbare Staaten wie die Schweiz:", 160, 505, "schweiz", size=34),
    z("volle Niederlassungsfreiheit, keine ernste Gefahr", 160, 553, beim("schweiz", "Niederlassungsfreiheit"), size=34),
    zit("<415 f.>", 160, 603, beim("schweiz", "Niederlassungsfreiheit")),
    blk(110, 660, 1040, 130, GRUEN, "milder", [("mildere Stufen genügen,", "ExtraBold", 34, INK),
                                            ("etwa eine Berufsgerichtsbarkeit", "ExtraBold", 34, INK)]),
    zit("<431 f., 438>", 110, 805, beim("milder", "Berufsgerichtsbarkeit")),
    *requisit([("volk", ("tabler", "heartbeat", 110, ROT), "Volksgesundheit", WEISS),
               ("gefahr", ("tabler", "search", 100, WEISS), "Gefahr?", HELLROT),
               ("schweiz", ("tabler", "world", 110, BLAUHELL), "Schweiz: Niederlassungsfreiheit", WEISS),
               ("milder", ("tabler", "gavel", 120, HOLZ), "Berufsgerichtsbarkeit", GRUEN)]),
    *paar("GR", [("volk", "ruhig"), ("milder", "froh")], "DA", [("volk", "denkt"), ("gefahr", "ruhig")]),
])

# ===========================================================================================================================
# F3 Ergebnis (Entscheidungsformel <379>; Leitsatz 8; <443 f.>)
# ===========================================================================================================================
folie([("erg", "Ergebnis · Art. 12 Abs. 1 GG verletzt"), ("nichtig", "Ergebnis · Art. 3 Abs. 1 ApothekenG nichtig"),
       ("nl", "Ergebnis · allein die Niederlassungsfreiheit")], [
    *tafel("erg", "Ergebnis: Urteil vom 11.6.1958"),
    *okz("Die Bescheide verletzen das Grundrecht aus", 180, beim("erg", "Bescheide"), "Bold", 34, x=160),
    z("Art. 12 Abs. 1 GG und werden aufgehoben.", 160, 228, beim("erg", "aufgehoben"), "Bold", 34),
    blk(110, 300, 1040, 90, ROT, "nichtig", [("Art. 3 Abs. 1 ApothekenG ist nichtig.", "ExtraBold", 36, INK)]),
    zit("BVerfGE 7, 377 <379> (Entscheidungsformel); <444>", 110, 405, "nichtig"),
    blk(110, 475, 1040, 130, GRUEN, "nl", [("Im Apothekenrecht entspricht der Verfassung", "ExtraBold", 34, INK),
                                        ("allein die Niederlassungsfreiheit:", "ExtraBold", 34, INK)]),
    z("keine objektiven Zulassungsschranken", 110, 625, beim("nl", "objektiver"), "Bold", 34),
    zit("Leitsatz 8; <443>", 110, 675, beim("nl", "objektiver")),
    *requisit([("erg", ("tabler", "building-bank", 120, WEISS), "aufgehoben", GELB),
               ("nichtig", ("tabler", "file-x", 110, HELLROT), "nichtig", HELLROT),
               ("nl", ("tabler", "lock-open", 110, GRUEN), "Niederlassungsfreiheit", GRUEN)]),
    *stehend("GR", FX, [("erg", "ruhig"), ("nl", "froh")]),
])

# ===========================================================================================================================
# G1 Zurück zum Fall: Grete fragt (Schauplatz A1, die Geschichte kehrt dorthin zurück)
# ===========================================================================================================================
O2 = "o2"
folie([(O2, "Zurück zum Fall · Grete")], [
    *strasse(O2, leer_icon=True),
    *fig("DA", DX, BODEN, FH, [(O2, "ruhig")], erst="cut", bis="heute"),
    hart(ns("Herr Dannemann", DX, BODEN, O2, BLAUHELL)),
    *redet("GR_redet_r", GX, BODEN, FH, O2, "heute"),
    hart(ns("Grete", GX, BODEN, O2, GRUEN)),
    blase("sprech", 640, 170, O2, 1350, 250, inhalt=["Und was heißt das", "für meine Apotheke?"], textsize=32,
          figur=("GR_redet_r", GX, BODEN, FH), bis="heute"),
])

# ===========================================================================================================================
# G2 § 2 Abs. 1 ApoG heute (Wortlautkarte, Abruf 04.10.2026)
# ===========================================================================================================================
W2 = ["„(1) Die Erlaubnis ist auf Antrag zu erteilen, wenn der",
      "Antragsteller … 3. die deutsche Approbation als Apotheker",
      "besitzt; …“"]
w2, w2_y = wortlaut(80, 170, 1100, W2, "§ 2 Abs. 1 ApoG (Auszug)", "heute", marken=[
    ("auf Antrag zu erteilen", beim("heute", "Antrag")), ("Approbation", beim("heute", "Approbation"))], size=33)
PZ = "Zurück zum Fall"
folie([("heute", f"{PZ} · § 2 Abs. 1 ApoG heute"), ("kein", f"{PZ} · kein Bedarf als Voraussetzung"),
       ("gr2", f"{PZ} · Grete bekommt die Erlaubnis")], [
    *tafel("heute", "Gretes Apotheke heute"),
    *w2,
    *neinz("Genug Apotheken im Stadtteil? Gehört nicht dazu.", w2_y + 40, "kein", "Bold", 34, x=160),
    *okz("Eine Bedürfnisprüfung wäre eine objektive", w2_y + 120, "gr2", "Bold", 34, x=160),
    z("Zulassungsschranke.", 160, w2_y + 168, beim("gr2", "Zulassungsschranke"), "Bold", 34),
    zit("BVerfGE 7, 377, Leitsatz 8; <443 f.>", 160, w2_y + 218, beim("gr2", "Zulassungsschranke")),
    pl("Voraussetzungen erfüllt: Grete bekommt die Erlaubnis", 110, w2_y + 290, beim("gr2", "bekommt"), fill=GRUEN, size=33),
    *requisit([("heute", ("tabler", "book", 100, WEISS), "§ 2 ApoG", WEISS),
               (beim("heute", "Approbation"), ("tabler", "certificate", 110, GELB), "Approbation", GELB),
               ("kein", ("tabler", "map-pins", 110, WEISS), "Bedarf: kein Kriterium", HELLROT),
               (beim("gr2", "bekommt"), ("tabler", "building-store", 120, GRUEN), "Erlaubnis", GRUEN)]),
    *paar("GR", [("heute", "denkt"), (beim("gr2", "bekommt"), "froh")], "DA", [("heute", "ruhig"), ("kein", "denkt")]),
])

# ===========================================================================================================================
# H Klausurtipp (Lexi) – Stufe bestimmen; Ausübungsregelung, die der Berufswahl nahekommt (BVerfGE 77, 84 <106>)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · erst die Stufe, dann der Maßstab"), ("tipp2", "Klausurtipp · Wirkung nahe der Berufswahl")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Bestimme zuerst die Stufe,", 200, 200, beim("tipp", "Stufe"), "Bold", 36),
    z("dann den Maßstab der Rechtfertigung.", 200, 250, beim("tipp", "Maßstab"), "Bold", 36),
    linienzug([(130, 335), (1130, 335)], "tipp2", breite=3),
    pl("Achtung", 200, 365, "tipp2", fill=PINK, size=34),
    z("Auch eine Berufsausübungsregelung kann in", 200, 450, beim("tipp2", "Berufsausübungsregelung"), size=34),
    z("ihren Auswirkungen einem Eingriff in die", 200, 498, beim("tipp2", "Auswirkungen"), size=34),
    z("Berufswahl nahekommen.", 200, 546, beim("tipp2", "Berufswahl"), "Bold", 34),
    *neinz("Dann genügt nicht jede vernünftige", 625, beim("tipp2", "genügt"), "Bold", 34, x=245),
    z("Erwägung des Gemeinwohls.", 245, 673, beim("tipp2", "Erwägung"), "Bold", 34),
    zit("BVerfGE 77, 84 <106>; ebenso BVerfGE 30, 292 <313>", 200, 740, beim("tipp2", "Erwägung")),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# I Prüfschema
# ===========================================================================================================================
REIHEN = [("k1", 0, "I. Schutzbereich: Beruf, auch der Schritt in die Selbständigkeit", True),
          ("k2", 0, "II. Eingriff: auf welcher Stufe?", True),
          (beim("k2", "Ausübung"), 1, "Ausübung, subjektive oder objektive Zulassung", False),
          ("k3", 0, "III. Rechtfertigung", True),
          (beim("k3", "gesetzlicher"), 1, "gesetzliche Grundlage nach Art. 12 Abs. 1 Satz 2 GG", False),
          ("k4", 1, "Maßstab der jeweiligen Stufe", False),
          ("k5", 1, "niedrigste Stufe, die zum Ziel führt", False)]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Prüfschema: Berufsfreiheit, Art. 12 Abs. 1 GG"), 110, 90, "sch", 46)]
y = 215
for c, ebene, text, fett in REIHEN:
    x = (130, 200)[ebene]
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 40 if ebene == 0 else 36, rechts=1800))
    y += {0: 92, 1: 82}[ebene]
assert y <= 970, y
folie([("sch", "Prüfschema"), ("k1", "Prüfschema › I. Schutzbereich"), ("k2", "Prüfschema › II. Eingriff"),
       ("k3", "Prüfschema › III. Rechtfertigung"), ("k4", "Prüfschema › III. Maßstab der Stufe"),
       ("k5", "Prüfschema › III. niedrigste Stufe")], els_sch)

# ===========================================================================================================================
# J Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Je näher eine Regelung an die", 0)], [("freie Berufswahl", "a"), (" rückt, desto", 0)],
                 [("gewichtiger muss ihr Grund sein.", 0)]], 750, 290, 44, "merke", {"a": beim("merke", "freie")}),
    *markertext([[("Objektive Zulassungsschranken", "b")], [("rechtfertigt in aller Regel nur die Abwehr", 0)],
                 [("schwerer Gefahren für ein überragend", 0)], [("wichtiges Gemeinschaftsgut.", 0)]], 750, 520, 40, "m2",
                {"b": beim("m2", "Objektive")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
