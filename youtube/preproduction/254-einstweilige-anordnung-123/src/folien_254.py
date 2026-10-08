"""Folge 254 · § 123 VwGO: Einstweilige Anordnung – Prüfungsschema – Serienstandard Open Peeps (Katzenkönig).
Fall: Das Stadtfest ist in 10 Tagen; Herr Eckstein vom Marktamt verweigert Magda den Standplatz wegen eines kritischen
Leserbriefs, obwohl laut Lageplan noch 3 Plätze frei sind. Danach: A. Zulässigkeit (Rechtsweg, § 123 Abs. 5 VwGO als
Wortlautkarte, Sicherungs-/Regelungsanordnung mit § 123 Abs. 1 VwGO als Wortlautkarte, Antragsbefugnis, Rechtsschutzbedürfnis),
B. Begründetheit (Glaubhaftmachung mit § 123 Abs. 3 VwGO, §§ 920 Abs. 2, 294 Abs. 1 ZPO als Wortlautkarten; Anordnungsanspruch
mit § 70 Abs. 1, 3 GewO als Wortlautkarte; Anordnungsgrund; Vorwegnahme der Hauptsache und Ausnahme), Beschluss, Stadtfest,
Klausurtipp, Schema, Merksatz mit Lexi.
Szenen laut ../SZENENPLAN.md. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/feld/requisit/paar als
eigene Kopie aus Folge 233 (dort aus 231/227; gemeinsame Dateien unverändert); neu: kasten(), lageplan(), theke(), markise().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut nach gesetze-im-internet.de, Abruf 08.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_254/"

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
APRIKOSE = (246, 181, 138, 255)
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
        if n.startswith(("bild:", "ficon:")) or "/op_254/" in n:
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
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 08.10.2026 (Folge 254)), als Zitat mit Normangabe; der
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
NAME = {"MA": "Magda", "EC": "Herr Eckstein"}
NFARBE = {"MA": APRIKOSE, "EC": BLAU}
WAND = (246, 236, 220, 255)


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




# --- Folge 254: Marktamt, Lageplan, Richterbank, Waffelstand (programmatisch, Palettenflächen, Tuschekontur) ---------------
HOLZ_H = (232, 196, 150, 255)
GRAUHELL = (214, 214, 210, 255)


def kasten(x, y, w, h, cue, fill, rand=5, rund=10, bis=None, name="kasten"):
    """Programmatische Fläche mit Tuschekontur (Theke, Richterbank, Standtheke)."""
    return El(_feld(w, h, fill, rand, rund), x - 6, y - 6, cue, "cut", 0.0, bis, name=name)


LP_X, LP_Y, LP_W, LP_H = 90, 170, 560, 430           # Lageplan an der Wand des Marktamts
LP_FREI = [(2, 1), (3, 2), (0, 2)]                     # drei freie Plätze (Spalte, Zeile)


def lageplan(cue, cue_frei, bis=None):
    """Lageplan des Stadtfests: 4 × 3 Standplätze, belegte grau, drei freie grün markiert (programmatisch)."""
    els = [kasten(LP_X, LP_Y, LP_W, LP_H, cue, WEISS, rand=5, rund=14, bis=bis, name="lageplan"),
           pl("Lageplan Stadtfest", LP_X + LP_W / 2, LP_Y + 18, cue, fill=GELB, size=28, anker="m", bis=bis)]
    sw, sh, gx, gy = 110, 90, 22, 26
    x0, y0 = LP_X + 34, LP_Y + 90
    for sp in range(4):
        for ze in range(3):
            x, y = x0 + sp * (sw + gx), y0 + ze * (sh + gy)
            frei = (sp, ze) in LP_FREI
            els.append(kasten(x, y, sw, sh, cue, WEISS if frei else GRAUHELL, rand=3, rund=8, bis=bis, name=f"platz{sp}{ze}"))
            if frei:
                els.append(kasten(x, y, sw, sh, cue_frei, HELLGRUEN, rand=4, rund=8, bis=bis, name=f"frei{sp}{ze}"))
                els.append(z("frei", x + 30, y + 26, cue_frei, "Bold", 28, rechts=x + sw, bis=bis))
    return els


def theke(cue, x0=1250, x1=1850, oben=640):
    """Amtstheke im Marktamt: Holzfront mit Tuschekontur, verdeckt die Beine von Herrn Eckstein."""
    return [kasten(x0, oben, x1 - x0, BODEN - oben, cue, HOLZ_H, name="theke"),
            hart(linienzug([(x0 - 10, oben + 2), (x1 + 10, oben + 2)], cue, breite=9, farbe=INK))]


def markise(cue, x0, x1, oben, h=70):
    """Gestreifte Markise des Waffelstands (Rot/Weiß, Palette)."""
    w = x1 - x0; s = 2
    im = Image.new("RGBA", ((w + 12) * s, (h + 12) * s))
    dr = ImageDraw.Draw(im); o = 6 * s
    n = 8; sw = w / n
    for i in range(n):
        dr.rectangle((o + i * sw * s, o, o + (i + 1) * sw * s, o + h * s), fill=ROT if i % 2 == 0 else WEISS)
    dr.rectangle((o, o, o + w * s, o + h * s), outline=INK, width=5 * s)
    for i in range(n):
        cx = o + (i + 0.5) * sw * s
        dr.pieslice((cx - sw / 2 * s, o + (h - 22) * s, cx + sw / 2 * s, o + (h + 22) * s), 0, 180,
                    fill=ROT if i % 2 == 0 else WEISS, outline=INK, width=4 * s)
    im = im.resize((w + 12, h + 34), Image.LANCZOS)
    return El(im, x0 - 6, oben - 6, cue, "cut", 0.0, None, name="markise")


# ===========================================================================================================================
# A Fall: Im Marktamt – Magda will einen Standplatz, Herr Eckstein lehnt ab
# ===========================================================================================================================
MAX, ECX, FH_ = 900, 1560, 440
NULL = ("fall", -round(T_("fall"), 3))
STEMPEL = beim("bescheid", "schriftlich")
stempel = ficon("ph", "stamp", 1400, 630, 90, STEMPEL, fuell=ROT)
szene(stempel, "254stempel*", 0.9, -0.03)              # Stempel trifft den Bescheid, als er erscheint
FALL_PFADE = [(NULL, "Fall · Im Marktamt: Das Stadtfest ist in 10 Tagen"), ("magda", "Fall · Magda und ihre Waffeln"),
              ("lage", "Fall · Der Lageplan"), ("eckstein", "Fall · Herr Eckstein vom Marktamt"), ("ec1", "Fall · Die Ablehnung"),
              ("bescheid", "Fall · Der Bescheid"), ("monate", "Fall · Keine Zeit")]
folie(FALL_PFADE, [
    hart(boden(NULL)),
    hart(pl("Das Stadtfest ist in 10 Tagen.", 70, 30, NULL, fill=GELB, size=32)),
    hart(ficon("tabler", "calendar-event", 700, 120, 84, NULL, fuell=GELB, anim="cut")),
    *fig("MA", MAX, BODEN, FH_, [(NULL, "froh_r"), ("lage", "denkt_r"), ("eckstein", "ruhig_r"), (beim("ec1", "kritisiert"), "schreck_r"),
                                 (beim("ec1", "keinen"), "sorge_r")], bis="ma1", erst="cut"),
    *redet("MA_redet_r", MAX, BODEN, FH_, "ma1", "bescheid"),
    *fig("MA", MAX, BODEN, FH_, [("bescheid", "sorge_r"), ("monate", "muede_r")], erst="cut"),
    ns(NAME["MA"], MAX, BODEN, NULL, NFARBE["MA"], anim="cut"),
    # Waffeln: ihr wichtigstes Geschäft
    ficon("fluent-emoji-high-contrast", "waffle", 370, 470, 180, beim("magda", "Waffeln"), fuell=GELB, bis="lage"),
    pl("seit Jahren: Waffeln auf dem Stadtfest", 70, 94, beim("magda", "Seit"), fill=APRIKOSE, size=30, bis="lage"),
    pl("ihr wichtigstes Geschäft im Jahr", 70, 158, beim("magda", "wichtigstes"), fill=WEISS, size=30, bis="lage"),
    # Lageplan mit drei freien Plätzen
    *lageplan("lage", beim("lage", "drei")),
    pl("3 Plätze frei", 370, 640, beim("lage", "frei"), fill=HELLGRUEN, size=30, anker="m"),
    # Herr Eckstein hinter der Theke
    *fig("EC", ECX, BODEN, FH_, [(NULL, "ruhig"), ("eckstein", "ernst")], bis="ec1", erst="cut"),
    *redet("EC_redet", ECX, BODEN, FH_, "ec1", "ma1"),
    *fig("EC", ECX, BODEN, FH_, [("ma1", "streng"), ("bescheid", "ernst"), ("monate", "ruhig")], erst="cut"),
    *[hart(e) for e in theke(NULL)],
    hart(pl("Marktamt der Stadt", 1550, 680, NULL, fill=BLAU, size=30, anker="m")),
    ns(NAME["EC"], ECX, BODEN, NULL, NFARBE["EC"], anim="cut"),
    blase("sprech", 700, 230, "ec1", 1000, 220, inhalt=["Sie haben die Stadt in einem", "Leserbrief kritisiert. Für Sie gibt",
                                                        "es dieses Jahr keinen Platz."], textsize=30,
          figur=("EC_redet", ECX, BODEN, FH_), bis="ma1"),
    ficon("fluent-emoji-high-contrast", "newspaper", 1300, 625, 90, beim("ec1", "Leserbrief"), fuell=WEISS, bis="bescheid"),
    ficon("tabler", "ban", 1180, 470, 80, beim("ec1", "keinen"), fuell=HELLROT, bis="ma1"),
    blase("sprech", 520, 180, "ma1", 1000, 190, inhalt=["Aber ich darf doch", "meine Meinung sagen!"], textsize=32,
          figur=("MA_redet_r", MAX, BODEN, FH_), bis="bescheid"),
    # Bescheid und Zeitnot
    ficon("tabler", "file-text", 1300, 630, 100, "bescheid", fuell=WEISS),
    stempel,
    pl("Ablehnung schriftlich", 1150, 300, beim("bescheid", "schriftlich"), fill=HELLROT, size=30, anker="m"),
    ficon("tabler", "hourglass", 1150, 470, 90, "monate", fuell=GELB),
    pl("Klage: dauert Monate", 1150, 210, beim("monate", "Monate"), fill=GELB, size=30, anker="m"),
])

# ===========================================================================================================================
# A2 Die Frage
# ===========================================================================================================================
folie([("frage", "Die Frage · Schnell zum Standplatz?"), ("frage2", "Die Frage · Einstweilige Anordnung, § 123 VwGO")], [
    *tafel("frage", "Die Frage"),
    z("Wie kommt Magda schnell", 110, 190, "frage", "Bold", 38),
    z("zu ihrem Standplatz?", 110, 244, "frage", "Bold", 38),
    blk(110, 340, 1040, 140, GELB, "frage2", [("Prüfungsschema der", "ExtraBold", 37, INK),
                                             ("einstweiligen Anordnung, § 123 VwGO", "ExtraBold", 37, INK)]),
    *requisit([("frage", ("tabler", "hourglass", 110, GELB), "Fest in 10 Tagen", GELB),
               ("frage2", ("fluent-emoji-high-contrast", "classical-building", 130, WEISS), "§ 123 VwGO", WEISS)]),
    *paar("MA", [("frage", "denkt"), ("frage2", "entschl")], "EC", [("frage", "ruhig")]),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_254(cue, absaetze, frage):
    els = [karte(140, 50, 1640, 930, cue, fill=HELL), titel("Sachverhalt", 210, 84, cue, 56)]
    y = 180
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=38, zeilenabstand=1.32)
        els += e; y += 12
    assert y + 66 <= 975, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=34))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_254("sv", [
    "Die Stadt veranstaltet jedes Jahr ihr Stadtfest, festgesetzt als Volksfest nach der Gewerbeordnung. Magda verkauft "
    "dort seit Jahren Waffeln; das Fest ist ihr wichtigstes Geschäft im Jahr. Auch diesmal beantragt sie einen Standplatz.",
    "Herr Eckstein vom Marktamt lehnt ab: „Sie haben die Stadt in einem Leserbrief kritisiert. Für Sie gibt es dieses Jahr "
    "keinen Platz.“ Laut Lageplan sind noch 3 Plätze frei. Die Ablehnung erhält Magda schriftlich.",
    "Das Fest beginnt in 10 Tagen. Eine Klage würde Monate dauern.",
], "Wie kommt Magda schnell zu ihrem Standplatz?")

# ===========================================================================================================================
# C A. Zulässigkeit: I. Verwaltungsrechtsweg, II. Statthaftigkeit – § 123 Abs. 5 VwGO (Wortlautkarte)
# ===========================================================================================================================
PZ = "A. Zulässigkeit"
w5, w5_y = wortlaut(80, 345, 1100, "„(5) Die Vorschriften der Absätze 1 bis 3 gelten nicht für die Fälle der §§ 80 und 80a.“",
                    "§ 123 Abs. 5 VwGO", "wl5", marken=[("80 und 80a", beim("wl5", "Paragrafen"))], size=32)
folie([("zul", PZ), ("rweg", f"{PZ} › I. Verwaltungsrechtsweg, § 40 Abs. 1 Satz 1 VwGO"),
       ("wl5", f"{PZ} › II. Statthaftigkeit, § 123 Abs. 5 VwGO"), ("haupt", f"{PZ} › II. Statthaftigkeit › Hauptsache: Verpflichtungsklage"),
       ("statt", f"{PZ} › II. Statthaftigkeit › Antrag nach § 123 VwGO")], [
    *tafel("zul", "A. Zulässigkeit"),
    *okz("I. Verwaltungsrechtsweg: Die Stadt entscheidet", 166, "rweg", "Bold", 33),
    z("als Veranstalterin durch Bescheid, öffentliches Recht", 185, 210, beim("rweg", "Bescheid"), size=31),
    zit("§ 40 Abs. 1 Satz 1 VwGO", 185, 250, beim("rweg", "öffentliches")),
    z("II. Statthaftigkeit", 110, 296, "wl5", "ExtraBold", 36),
    *w5,
    blk(110, w5_y + 20, 1040, 80, LILAHELL, "subs", [("§ 123 tritt zurück, wo es um aufschiebende Wirkung geht", "Bold", 31, INK)]),
    z("Hauptsache: Magda will die Zulassung,", 110, w5_y + 124, "haupt", "Bold", 33),
    z("also wäre eine Verpflichtungsklage statthaft", 150, w5_y + 170, beim("haupt", "Verpflichtungsklage"), size=31),
    *neinz("aufschiebende Wirkung bringt keinen Platz", w5_y + 230, "statt", "Bold", 32, kreuz=beim("statt", "keinen")),
    *okz("statthaft: Antrag nach § 123 VwGO", w5_y + 284, beim("statt", "Statthaft"), "ExtraBold", 33),
    zit("mehr: Videos zu § 80 Abs. 5 VwGO und zur Verpflichtungsklage", 185, w5_y + 336, "verweis"),
    *requisit([("rweg", ("fluent-emoji-high-contrast", "classical-building", 130, WEISS), "Verwaltungsgericht", WEISS),
               ("wl5", ("tabler", "file-text", 100, WEISS), "§ 123 Abs. 5", WEISS),
               ("haupt", ("tabler", "certificate", 110, GELB), "Zulassung", GELB),
               ("statt", ("tabler", "circle-check", 110, HELLGRUEN), "§ 123 VwGO", HELLGRUEN)]),
    *paar("MA", [("zul", "ruhig"), ("haupt", "entschl"), ("statt", "froh")], "EC", [("zul", "ruhig"), ("statt", "denkt")]),
])
assert w5_y + 336 + 40 <= 900, w5_y

# ===========================================================================================================================
# D II. Sicherungs- oder Regelungsanordnung – § 123 Abs. 1 VwGO (Wortlautkarte)
# ===========================================================================================================================
PS2 = f"{PZ} › II. Statthaftigkeit"
w1, w1_y = wortlaut(80, 165, 1100,
                    "„(1) Auf Antrag kann das Gericht, auch schon vor Klageerhebung, eine einstweilige Anordnung in bezug auf den "
                    "Streitgegenstand treffen, wenn die Gefahr besteht, daß durch eine Veränderung des bestehenden Zustands die "
                    "Verwirklichung eines Rechts des Antragstellers vereitelt oder wesentlich erschwert werden könnte. Einstweilige "
                    "Anordnungen sind auch zur Regelung eines vorläufigen Zustands in bezug auf ein streitiges Rechtsverhältnis "
                    "zulässig, wenn diese Regelung, vor allem bei dauernden Rechtsverhältnissen, um wesentliche Nachteile abzuwenden "
                    "oder drohende Gewalt zu verhindern oder aus anderen Gründen nötig erscheint.“",
                    "§ 123 Abs. 1 VwGO", "wl1",
                    marken=[("Veränderung", beim("sich", "Veränderung")), ("Regelung", beim("regl", "regelt")),
                            ("wesentliche Nachteile", beim("regl", "wesentliche"))], size=28)
folie([("wl1", f"{PS2} › Welche Anordnung? § 123 Abs. 1 VwGO"), ("sich", f"{PS2} › Satz 1: Sicherungsanordnung"),
       ("regl", f"{PS2} › Satz 2: Regelungsanordnung"), ("ma_r", f"{PS2} › hier: Regelungsanordnung")], [
    karte(60, 60, 1140, 840, "wl1"), z("II. Welche Anordnung?", 110, 92, "wl1", "ExtraBold", 40),
    *w1,
    blk(110, w1_y + 20, 505, 110, BLAUHELL, "sich", [("Satz 1: Sicherung", "ExtraBold", 31, INK),
                                                   ("Bestehendes sichern", "Regular", 30, INK)]),
    blk(645, w1_y + 20, 505, 110, GELB, "regl", [("Satz 2: Regelung", "ExtraBold", 31, INK),
                                              ("vorläufig neu regeln", "Regular", 30, INK)]),
    *okz("Magda will einen Platz, den sie noch nicht hat:", w1_y + 152, "ma_r", "Bold", 31),
    z("Regelungsanordnung", 185, w1_y + 196, beim("ma_r", "Regelungsanordnung"), "ExtraBold", 33),
    zit("VG Gelsenkirchen, Beschl. v. 9.4.2026 – 18 L 76/26, Rn. 7 (Kirmes)", 185, w1_y + 242, beim("ma_r", "Regelungsanordnung")),
    *requisit([("sich", ("tabler", "lock", 100, BLAUHELL), "sichern", BLAUHELL),
               ("regl", ("tabler", "arrows-split", 110, GELB), "regeln", GELB),
               ("ma_r", ("fluent-emoji-high-contrast", "waffle", 120, GELB), "neuer Standplatz", GELB)]),
    *stehend("MA", FX, [("wl1", "denkt"), ("ma_r", "entschl")]),
])
assert w1_y + 242 + 40 <= 900, w1_y

# ===========================================================================================================================
# E III. Antragsbefugnis, IV. Rechtsschutzbedürfnis
# ===========================================================================================================================
folie([("befugt", f"{PZ} › III. Antragsbefugnis, § 42 Abs. 2 VwGO analog"), ("rsb", f"{PZ} › IV. Rechtsschutzbedürfnis"),
       ("rsb2", f"{PZ} › IV. Rechtsschutzbedürfnis › Antrag bei der Stadt"), ("vor", f"{PZ} › Antrag schon vor der Klage"),
       ("zul2", f"{PZ} › Ergebnis: zulässig")], [
    *tafel("befugt", "A. Zulässigkeit: III. und IV."),
    *okz("III. Antragsbefugnis, § 42 Abs. 2 VwGO analog:", 170, "befugt", "Bold", 33),
    z("möglicher Anspruch auf Zulassung, § 70 GewO", 185, 216, beim("befugt", "Zulassung"), size=31),
    z("IV. Rechtsschutzbedürfnis:", 185, 290, "rsb", "Bold", 33),
    z("grundsätzlich zuerst Antrag bei der Behörde", 185, 336, beim("rsb", "Grundsätzlich"), size=31),
    zit("BVerwG, Beschl. v. 22.11.2021 – 6 VR 4.21, Rn. 7 f., 10", 185, 380, beim("rsb", "Behörde")),
    *okz("Magda hat beantragt, die Stadt hat abgelehnt", 430, "rsb2", "Bold", 32),
    blk(110, 510, 1040, 110, BLAUHELL, "vor", [("Antrag schon vor Klageerhebung möglich", "ExtraBold", 32, INK),
                                            ("§ 123 Abs. 1 Satz 1 VwGO", "Regular", 30, INK)]),
    blk(110, 660, 1040, 90, HELLGRUEN, "zul2", [("Der Antrag ist zulässig.", "ExtraBold", 34, INK)]),
    *requisit([("befugt", ("tabler", "certificate", 110, WEISS), "§ 70 GewO", WEISS),
               ("rsb", ("tabler", "building", 110, BLAUHELL), "erst zur Behörde", BLAUHELL),
               ("rsb2", ("tabler", "file-text", 100, HELLROT), "abgelehnt", HELLROT),
               ("zul2", ("tabler", "circle-check", 110, HELLGRUEN), "zulässig", HELLGRUEN)]),
    *paar("MA", [("befugt", "ruhig"), ("rsb2", "denkt"), ("zul2", "froh")], "EC", [("befugt", "ruhig"), ("rsb2", "ernst")]),
])

# ===========================================================================================================================
# F B. Begründetheit: Glaubhaftmachung (Wortlautkarten § 123 Abs. 3 VwGO, § 920 Abs. 2, § 294 Abs. 1 ZPO)
# ===========================================================================================================================
PB = "B. Begründetheit"
w3, w3_y = wortlaut(80, 220, 1100, "„(3) Für den Erlaß einstweiliger Anordnungen gelten §§ 920, 921, 923, 926, 928 bis 932, "
                    "938, 939, 941 und 945 der Zivilprozeßordnung entsprechend.“", "§ 123 Abs. 3 VwGO", "wl3",
                    marken=[("§§ 920,", beim("wl3", "Paragraf"))], size=30)
w920, w920_y = wortlaut(80, w3_y + 14, 1100, "„(2) Der Anspruch und der Arrestgrund sind glaubhaft zu machen.“",
                        "§ 920 Abs. 2 ZPO", "wl3", marken=[("glaubhaft zu machen", beim("wl3", "glaubhaft"))],
                        size=30)
w294, w294_y = wortlaut(80, w920_y + 14, 1100, "„(1) Wer eine tatsächliche Behauptung glaubhaft zu machen hat, kann sich aller "
                        "Beweismittel bedienen, auch zur Versicherung an Eides statt zugelassen werden.“", "§ 294 Abs. 1 ZPO",
                        "z294", marken=[("aller", beim("z294", "alle")), ("Versicherung an Eides statt", beim("z294", "Versicherung"))],
                        size=30)
folie([("begr", f"{PB}: Anordnungsanspruch und Anordnungsgrund"),
       ("wl3", f"{PB} › glaubhaft machen, § 123 Abs. 3 VwGO, § 920 Abs. 2 ZPO"),
       ("z294", f"{PB} › Glaubhaftmachung, § 294 Abs. 1 ZPO"), ("mittel", f"{PB} › Glaubhaftmachung › Magda")], [
    *tafel("begr", "B. Begründetheit"),
    z("Anordnungsanspruch und Anordnungsgrund", 110, 166, beim("begr", "Anordnungsanspruch"), "Bold", 34),
    *w3, *w920, *w294,
    blk(110, w294_y + 18, 1040, 80, HELL, "mittel", [("Magda: Bescheid, Lageplan, Versicherung an Eides statt", "Bold", 30, INK)]),
    *requisit([("begr", ("fluent-emoji-high-contrast", "balance-scale", 130, WEISS), "begründet?", WEISS),
               ("wl3", ("tabler", "book", 110, WEISS), "ZPO entsprechend", WEISS),
               ("z294", ("tabler", "writing-sign", 110, GELB), "an Eides statt", GELB),
               ("mittel", ("tabler", "map", 110, HELLGRUEN), "Bescheid, Lageplan", HELLGRUEN)]),
    *stehend("MA", FX, [("begr", "ruhig"), ("z294", "denkt"), ("mittel", "entschl")]),
])
assert w294_y + 18 + 80 <= 900, w294_y

# ===========================================================================================================================
# G I. Anordnungsanspruch: § 70 GewO (Wortlautkarte)
# ===========================================================================================================================
PA = f"{PB} › I. Anordnungsanspruch"
w70, w70_y = wortlaut(80, 300, 1100,
                      "„(1) Jedermann, der dem Teilnehmerkreis der festgesetzten Veranstaltung angehört, ist nach Maßgabe der für "
                      "alle Veranstaltungsteilnehmer geltenden Bestimmungen zur Teilnahme an der Veranstaltung berechtigt. … "
                      "(3) Der Veranstalter kann aus sachlich gerechtfertigten Gründen, insbesondere wenn der zur Verfügung "
                      "stehende Platz nicht ausreicht, einzelne Aussteller, Anbieter oder Besucher von der Teilnahme ausschließen.“",
                      "§ 70 Abs. 1 und 3 GewO", "wl70",
                      marken=[("Jedermann,", beim("wl70", "jeder")), ("sachlich", beim("aus", "sachlich")),
                              ("Platz nicht ausreicht,", beim("aus", "Platz"))], size=28)
folie([("aa", PA), ("wl70", f"{PA} › Volksfest, § 70 Abs. 1 GewO"), ("aus", f"{PA} › Ausschluss, § 70 Abs. 3 GewO"),
       ("frei", f"{PA} › Platzmangel? (−)"), ("kritik", f"{PA} › Leserbrief: kein sachlicher Grund"),
       ("null", f"{PA} › kein Spielraum: Zulassung")], [
    *tafel("aa", "B. I. Anordnungsanspruch"),
    z("Anspruch besteht überwiegend wahrscheinlich", 110, 166, beim("aa", "überwiegend"), "Bold", 33),
    zit("OVG NRW, Beschl. v. 15.2.2024 – 15 B 144/24, Rn. 7", 110, 206, beim("aa", "überwiegend")),
    z("Stadtfest: festgesetztes Volksfest, §§ 60b, 69 GewO", 110, 248, "wl70", "Bold", 32),
    *w70,
    *neinz("Platzmangel? Es sind Plätze frei.", w70_y + 22, "frei", "Bold", 32),
    *neinz("Leserbrief: kein sachlicher Grund, Art. 5 Abs. 1 GG", w70_y + 76, "kritik", "Bold", 32,
           kreuz=beim("kritik", "kein")),
    blk(110, w70_y + 136, 1040, 80, HELLGRUEN, "null", [("Kein Spielraum: Die Stadt muss Magda zulassen.", "ExtraBold", 32, INK)]),
    zit("vgl. OVG NRW, Beschl. v. 26.7.2018 – 4 B 1069/18, Rn. 7", 110, w70_y + 226, beim("null", "zulassen")),
    *requisit([("aa", ("tabler", "scale", 120, WEISS), "Anspruch?", WEISS),
               ("wl70", ("fluent-emoji-high-contrast", "circus-tent", 130, GELB), "Volksfest", GELB),
               ("frei", ("tabler", "map", 110, HELLGRUEN), "3 Plätze frei", HELLGRUEN),
               ("kritik", ("fluent-emoji-high-contrast", "newspaper", 120, WEISS), "Meinungsfreiheit", WEISS),
               ("null", ("tabler", "circle-check", 110, HELLGRUEN), "Zulassung", HELLGRUEN)]),
    *paar("MA", [("aa", "ruhig"), ("frei", "denkt"), ("kritik", "entschl"), ("null", "froh")], "EC",
          [("aa", "ruhig"), ("kritik", "denkt"), ("null", "ernst")]),
])
assert w70_y + 226 + 40 <= 900, w70_y

# ===========================================================================================================================
# H II. Anordnungsgrund; III. Vorwegnahme der Hauptsache (Grundsatz)
# ===========================================================================================================================
folie([("ag", f"{PB} › II. Anordnungsgrund"), ("ag2", f"{PB} › II. Anordnungsgrund (+)"),
       ("vw", f"{PB} › III. Vorwegnahme der Hauptsache"), ("vw2", f"{PB} › III. Vorwegnahme: Hauptsache wäre erledigt"),
       ("verbot", f"{PB} › III. Grundsatz: keine Vorwegnahme")], [
    *tafel("ag", "B. II. Anordnungsgrund"),
    z("Eilbedürftigkeit", 110, 166, beim("ag", "Eilbedürftigkeit"), "Bold", 34),
    *okz("Fest in 10 Tagen: Hauptsache käme zu spät", 226, "ag2", "Bold", 32, x=185),
    zit("vgl. OVG NRW, Beschl. v. 15.2.2024 – 15 B 144/24, Rn. 32", 185, 270, beim("ag2", "spät")),
    z("III. Vorwegnahme der Hauptsache", 110, 340, "vw", "ExtraBold", 36),
    z("Zulassung = alles, was Magda mit der Klage will", 150, 394, beim("vw", "alles"), size=32),
    z("nach dem Fest bliebe nichts mehr übrig", 150, 444, "vw2", size=32),
    z("Die Eilentscheidung nähme die Hauptsache vorweg.", 150, 494, beim("vw2", "Eilentscheidung"), "Bold", 32),
    blk(110, 570, 1040, 110, HELLROT, "verbot", [("Grundsatz: nicht vorwegnehmen,", "ExtraBold", 32, INK),
                                               ("nur vorläufig regeln", "Regular", 32, INK)]),
    zit("BVerwG, Beschl. v. 26.11.2013 – 6 VR 3.13, Rn. 5", 110, 692, beim("verbot", "vorläufig")),
    *requisit([("ag", ("tabler", "calendar-event", 110, GELB), "in 10 Tagen", GELB),
               ("vw", ("tabler", "hourglass", 110, WEISS), "Vorwegnahme?", WEISS),
               ("verbot", ("tabler", "ban", 100, HELLROT), "grundsätzlich nicht", HELLROT)]),
    *stehend("MA", FX, [("ag", "sorge"), ("ag2", "entschl"), ("vw", "denkt"), ("verbot", "sorge")]),
])

# ===========================================================================================================================
# I III. Ausnahme vom Vorwegnahmeverbot (BVerwG 6 VR 3.13; BVerfG 1 BvR 569/05)
# ===========================================================================================================================
PV = f"{PB} › III. Vorwegnahme"
folie([("ausn", f"{PV} › Ausnahme: unzumutbare Nachteile"), ("ausn2", f"{PV} › Ausnahme: Hauptsache erkennbar erfolgreich"),
       ("art19", f"{PV} › effektiver Rechtsschutz, Art. 19 Abs. 4 GG"), ("beides", f"{PV} › Ausnahme (+)")], [
    *tafel("ausn", "III. Ausnahme: Vorwegnahme erlaubt", size=42),
    blk(110, 170, 1040, 120, BLAUHELL, "ausn", [("1. Abwarten: schwere, unzumutbare Nachteile,", "ExtraBold", 31, INK),
                                             ("die später nicht mehr zu beseitigen sind", "Regular", 31, INK)]),
    zit("BVerwG, Beschl. v. 26.11.2013 – 6 VR 3.13, Rn. 5", 110, 302, beim("ausn", "Bundesverwaltungsgericht")),
    blk(110, 350, 1040, 120, GELB, "ausn2", [("2. Hauptsache hätte erkennbar Erfolg,", "ExtraBold", 31, INK),
                                          ("strenger Maßstab", "Regular", 31, INK)]),
    zit("BVerwG 6 VR 3.13, Rn. 7", 110, 482, beim("ausn2", "strenger")),
    z("Grund: effektiver Rechtsschutz, Art. 19 Abs. 4 GG", 110, 530, "art19", "Bold", 32),
    zit("BVerfG, Beschl. v. 12.5.2005 – 1 BvR 569/05, Rn. 23–25", 110, 576, beim("art19", "Bundesverfassungsgericht")),
    *okz("Magda: wichtigstes Fest sonst verloren", 640, beim("beides", "Ihr"), "Bold", 32),
    *okz("Anspruch eindeutig", 694, beim("beides", "Anspruch"), "Bold", 32),
    blk(110, 760, 1040, 80, HELLGRUEN, "beides", [("Beides (+): Vorwegnahme ausnahmsweise zulässig", "ExtraBold", 32, INK)]),
    *requisit([("ausn", ("tabler", "hourglass-empty", 110, BLAUHELL), "unzumutbar", BLAUHELL),
               ("ausn2", ("tabler", "scale", 120, GELB), "strenger Maßstab", GELB),
               ("art19", ("tabler", "shield-check", 110, HELLGRUEN), "Art. 19 Abs. 4 GG", HELLGRUEN)]),
    *stehend("MA", FX, [("ausn", "denkt"), ("art19", "ruhig"), ("beides", "froh")]),
])

# ===========================================================================================================================
# J Ergebnis: Beschluss des Verwaltungsgerichts
# ===========================================================================================================================
RIX, RIU, RIH = 1420, 740, 380
folie([("erg", "Ergebnis · Der Beschluss, § 123 Abs. 4 VwGO")], [
    hart(boden("erg")),
    ficon("fluent-emoji-high-contrast", "balance-scale", 1420, 300, 130, "erg", fuell=WEISS),
    pl("Verwaltungsgericht · Beschluss", 70, 30, "erg", fill=WEISS, size=32),
    peep_voll("RI_ernst", RIX, RIU, RIH, "erg", anim="pop", bis="ri1"),
    *redet("RI_redet", RIX, RIU, RIH, "ri1", "ende"),
    kasten(1080, 600, 680, BODEN - 600, "erg", HOLZ_H, name="richterbank"),
    pl("Richter", RIX, 640, "erg", fill=WEISS, size=30, anker="m"),
    *fig("MA", 560, BODEN, FH_, [("erg", "entschl_r"), (beim("ri1", "zulassen"), "strahlt_r")]),
    ns(NAME["MA"], 560, BODEN, "erg", NFARBE["MA"], d=0.1),
    blase("sprech", 640, 190, "ri1", 1000, 200, inhalt=["Die Stadt muss die Antragstellerin", "zum Stadtfest zulassen."],
          textsize=31, figur=("RI_redet", RIX, RIU, RIH)),
])

# ===========================================================================================================================
# K Zehn Tage später: Magda verkauft Waffeln auf dem Stadtfest
# ===========================================================================================================================
STX, KIX = 900, 1320
folie([("ende", "Ergebnis · 10 Tage später auf dem Stadtfest")], [
    hart(boden("ende")),
    ficon("fluent-emoji-high-contrast", "ferris-wheel", 300, BODEN, 380, "ende", fuell=BLAUHELL),
    ficon("tabler", "sun", 1820, 150, 96, "ende", fuell=GELB),
    pl("10 Tage später: Stadtfest", 70, 30, "ende", fill=GELB, size=32),
    markise("ende", 640, 1160, 300),
    hart(linienzug([(660, 330), (660, 640)], "ende", breite=10)), hart(linienzug([(1140, 330), (1140, 640)], "ende", breite=10)),
    *fig("MA", STX, 860, FH_, [("ende", "strahlt")], erst="cut"),
    kasten(620, 640, 560, BODEN - 640, "ende", HOLZ_H, name="standtheke"),
    pl("Waffeln", STX, 700, "ende", fill=WEISS, size=30, anker="m"),
    ficon("fluent-emoji-high-contrast", "waffle", 760, 640, 90, beim("ende", "Waffeln"), fuell=GELB),
    ficon("fluent-emoji-high-contrast", "waffle", 1040, 640, 90, beim("ende", "Waffeln"), fuell=GELB),
    ns(NAME["MA"], STX, BODEN, "ende", NFARBE["MA"], d=0.1),
    bewegt(peep_voll("KI_froh", KIX, BODEN, 270, beim("ende", "verkauft"), anim="cut", bis=beim("ende", "Stadtfest")),
           beim("ende", "verkauft"), beim("ende", "Stadtfest"), 220),
    peep_voll("KI_strahlt", KIX, BODEN, 270, beim("ende", "Stadtfest"), anim="cut"),
])

# ===========================================================================================================================
# L Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Bleibt der Behörde ein Spielraum?"), ("tipp1", "Klausurtipp › mehr Bewerber als Plätze"),
       ("tipp2", "Klausurtipp › Zulassung nur bei Spielraum null")], [
    *tafel("tipp", "Klausurtipp: Spielraum?", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Bleibt der Behörde noch ein Spielraum?", 200, 200, "tipp", "ExtraBold", 35),
    linienzug([(130, 290), (1130, 290)], "tipp1", breite=3),
    z("Mehr Bewerber als Plätze:", 200, 316, "tipp1", "ExtraBold", 34),
    z("meist nur eine neue Entscheidung (Neubescheidung)", 240, 370, beim("tipp1", "neue"), size=33),
    linienzug([(130, 450), (1130, 450)], "tipp2", breite=3),
    z("Zulassung selbst in der Regel nur,", 200, 476, "tipp2", "ExtraBold", 34),
    z("wenn der Spielraum auf null geschrumpft ist", 240, 530, beim("tipp2", "wenn"), size=33),
    zit("OVG NRW, Beschl. v. 26.7.2018 – 4 B 1069/18, Rn. 7", 240, 584, beim("tipp2", "null")),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# M Klausurschema (Lexi), Punkt für Punkt
# ===========================================================================================================================
folie([("sch", "Klausurschema · Einstweilige Anordnung, § 123 VwGO"), ("sa", "Klausurschema › A. Zulässigkeit"),
       ("s2", "Klausurschema › II. Statthaftigkeit"), ("s4", "Klausurschema › IV. Rechtsschutzbedürfnis"),
       ("sb", "Klausurschema › B. Begründetheit"), ("s7", "Klausurschema › Glaubhaftmachung"),
       ("s8", "Klausurschema › III. Vorwegnahme der Hauptsache")], [
    *tafel("sch", "Klausurschema: § 123 VwGO"),
    z("A. Zulässigkeit", 110, 165, "sa", "ExtraBold", 34),
    z("I. Verwaltungsrechtsweg, § 40 Abs. 1 VwGO", 150, 215, "s1", size=31),
    z("II. Statthaftigkeit: § 123 Abs. 5; Sicherung oder Regelung", 150, 262, "s2", size=31),
    z("III. Antragsbefugnis, § 42 Abs. 2 VwGO analog", 150, 309, "s3", size=31),
    z("IV. Rechtsschutzbedürfnis (Antrag bei der Behörde)", 150, 356, "s4", size=31),
    z("B. Begründetheit", 110, 424, "sb", "ExtraBold", 34),
    z("I. Anordnungsanspruch", 150, 474, "s5", size=31),
    z("II. Anordnungsgrund", 150, 521, beim("s6", "Anordnungsgrund"), size=31),
    z("beide glaubhaft gemacht: § 123 Abs. 3 VwGO, §§ 920 Abs. 2, 294 ZPO", 150, 568, "s7", size=29),
    z("III. bei Vorwegnahme der Hauptsache: strenge Ausnahme", 150, 615, "s8", size=31),
    *redet("LX_erklaert", FX, FB, FR + 40, "sch", "merke"),
    ns("Lexi", FX, FB, "sch", GELB, d=0.2),
])

# ===========================================================================================================================
# N Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Geht es nicht um ", 0), ("aufschiebende Wirkung", "a"), (",", 0)],
                 [("hilft im Eilverfahren § 123.", 0)]], 750, 290, 42, "merke",
                {"a": beim("merke", "aufschiebende")}),
    *markertext([[("Die Hauptsache vorwegnehmen darf das Gericht", 0)],
                 [("nur, wenn sonst ", 0), ("unzumutbare Nachteile", "b"), (" drohen", 0)],
                 [("und die Hauptsache ", 0), ("erkennbar Erfolg", "c"), (" hätte.", 0)]],
                750, 470, 38, "m2", {"b": beim("m2", "unzumutbare"), "c": beim("m2", "erkennbar")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
