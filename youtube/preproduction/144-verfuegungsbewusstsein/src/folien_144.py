"""Folge 144 · Verfügungsbewusstsein: Versteckte Ware – Diebstahl oder Betrug? – Serienstandard Open Peeps (Katzenkönig).
Fall: Fabian versteckt im Supermarkt Kopfhörer (120 €) in einer Waschmittelpackung, legt an der Kasse nur die Packung aufs
Band; Kassiererin Carina scannt das Waschmittel (8 €); Fabian zahlt und verlässt den Laden.
Szenen laut ../SZENENPLAN.md: A Supermarkt und Kasse (Fall), B Sachverhalt, C Abgrenzung (Fremd-/Selbstschädigung),
D Wortlautkarten § 242 Abs. 1 und § 263 Abs. 1, E Kernfrage Verfügungsbewusstsein, F Gegenansicht und Argumente,
G Subsumtion § 242, H1 Gegenvariante an der Kasse (Etikettentausch), H2 Gegenvariante: Betrug, I Klausurtipp (Lexi),
J Prüfschema, K Merksatz (Lexi). Waschmittelpackung als eigener Baustein (packung(): Palettenfläche mit Tuschekontur,
tabler „wash“ als Aufdruck, kein Markenname); versteckte Kopfhörer als gestrichelter Durchblick (Röntgenblick).
Zwei Handlungsgeräusche (Packung schließen, Scanner; ../geraeusche_herkunft.json).
Namensschild jeder Figur ab ihrem ersten Auftritt, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/
wortlaut/redet/fig/ns/okz/neinz als eigene Kopie aus Folge 140 (gemeinsame Dateien unverändert).
Zahlen auf Tafeln, Pillen und Blasen als Ziffern. beim()-Anker auf „Wegnahme“ stehen auf der gesprochenen Form „Weck“."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_144/"

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
        if n.startswith(("bild:", "ficon:", "bank")) or "/op_144/" in n:
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
# --- eigene Szenenbausteine (programmatisch, Palettenflächen, Tuschekontur) ---------------------------------------------------
from engine import El as _El


def _strich_rechteck(dr, box, farbe, breite, strich=14, luecke=9):
    """Gestrichelter Rahmen (Röntgenblick in die Packung)."""
    x0, y0, x1, y1 = box
    for (ax, ay, bx, by) in ((x0, y0, x1, y0), (x1, y0, x1, y1), (x1, y1, x0, y1), (x0, y1, x0, y0)):
        ln = max(abs(bx - ax), abs(by - ay)); t = 0
        while t < ln:
            e = min(ln, t + strich)
            dr.line((ax + (bx - ax) * t / ln, ay + (by - ay) * t / ln, ax + (bx - ax) * e / ln, ay + (by - ay) * e / ln),
                    fill=farbe, width=breite)
            t += strich + luecke


def packung(cx, unten, w, h, cue, bis=None, offen=False, inhalt=False, anim="cut", fill=TUERKIS):
    """Waschmittelpackung ohne Markennamen: Palettenfläche mit Tuschekontur, weißes Etikettband mit tabler „wash“
    (Waschsymbol, MIT). offen = Laschen hochgeklappt; inhalt = gestrichelter Durchblick mit den versteckten Kopfhörern."""
    s = 2
    fl = int(h * 0.32) if offen else 0
    im = Image.new("RGBA", ((w + 40) * s, (h + fl + 30) * s))
    dr = ImageDraw.Draw(im)
    ox, oy = 14 * s, (12 + fl) * s
    W_, H_ = w * s, h * s
    if offen:
        for poly in ([(ox, oy), (ox + W_ * 0.5, oy), (ox + W_ * 0.38, oy - fl * s * 0.95), (ox - W_ * 0.06, oy - fl * s * 0.7)],
                     [(ox + W_ * 0.5, oy), (ox + W_, oy), (ox + W_ * 1.06, oy - fl * s * 0.7), (ox + W_ * 0.62, oy - fl * s * 0.95)]):
            dr.polygon(poly, fill=fill[:3] + (255,))
            dr.line(poly + [poly[0]], fill=INK, width=5 * s, joint="curve")
    dr.rounded_rectangle((ox + 6 * s, oy + 6 * s, ox + W_ + 6 * s, oy + H_ + 6 * s), 10 * s, fill=INK)
    dr.rounded_rectangle((ox, oy, ox + W_, oy + H_), 10 * s, fill=INK)
    dr.rounded_rectangle((ox + 5 * s, oy + 5 * s, ox + W_ - 5 * s, oy + H_ - 5 * s), 6 * s, fill=fill)
    if offen:
        dr.line((ox + 8 * s, oy + 3 * s, ox + W_ - 8 * s, oy + 3 * s), fill=INK, width=8 * s)
    by0, by1 = oy + int(H_ * 0.10), oy + int(H_ * 0.40)
    dr.rounded_rectangle((ox + 14 * s, by0, ox + W_ - 14 * s, by1), 8 * s, fill=WEISS, outline=INK, width=3 * s)
    if inhalt:
        _strich_rechteck(dr, (ox + 16 * s, oy + int(H_ * 0.48), ox + W_ - 16 * s, oy + H_ - 14 * s), INK, 4 * s)
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    ic = ficon("tabler", "wash", 0, 0, int((by1 - by0) / s * 0.95), "_", fuell=BLAU).sprite
    im.alpha_composite(ic, (int(14 + w / 2 - ic.width / 2), int(12 + fl + h * 0.25 - ic.height / 2)))
    if inhalt:
        kh = ficon("tabler", "headphones", 0, 0, int(w * 0.5), "_", fuell=BLAU).sprite.copy()
        kh.putalpha(kh.getchannel("A").point(lambda v: int(v * 0.7)))
        im.alpha_composite(kh, (int(14 + w / 2 - kh.width / 2), int(12 + fl + h * 0.71 - kh.height / 2)))
    return _El(im, cx - 14 - w / 2, unten - 12 - fl - h, cue, anim, 0.0, bis, name="bild:packung")


def kopfhoerer(cx, unten, breite, cue, bis=None, anim="pop"):
    return ficon("tabler", "headphones", cx, unten, breite, cue, fuell=BLAU, bis=bis, anim=anim)


def kasse(x0, y0, x1, cue, scanner_cue=None):
    """Kassentresen mit Band (graue Fläche) und Scanner (tabler barcode); neutral, ohne Logo."""
    els = [hart(karte(x0, y0, x1 - x0, 900 - y0, cue, fill=WEISS, rund=12, schatten=6, rand=5, anim="cut")),
           hart(karte(x0 + 18, y0 + 18, int((x1 - x0) * 0.55), 34, cue, fill=(200, 200, 198, 255), rund=10, schatten=0, rand=4, anim="cut")),
           hart(ficon("tabler", "barcode", x1 - 330, y0 + 6, 74, cue, fuell=WEISS, anim="cut"))]
    return els


BODEN = 900
SH = 520                                    # Standhöhe im Fall
X1, X2 = 1430, 1730                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"FA": "Fabian", "CA": "Carina"}
NFARBE = {"FA": BLAU, "CA": ORANGE}


def requisit(folge, px=PX):
    """Wechselndes Requisit über den Figuren: folge = [(cue, (set, icon, breite, fuell) | El-Fabrik, pillentext, pillenfarbe)]."""
    els = []
    for i, (c, ic, txt, pf) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else None
        if callable(ic):
            els.append(ic(c, b))
        elif ic:
            s_, n_, br, fu = ic
            els.append(ficon(s_, n_, px, PU, br, c, fuell=fu, bis=b))
        if txt:
            els.append(pl(txt, px, PY, c, fill=pf, size=28, anker="m", bis=b))
    return els


def stehend(k, x, folge, unten=FB, hoehe=FR):
    return [*fig(k, x, unten, hoehe, folge), ns(NAME[k], x, unten, folge[0][0], NFARBE[k], d=0.1)]


def pk_req(offen=False, inhalt=False, w=110, h=150):
    return lambda c, b: packung(PX, PU, w, h, c, bis=b, offen=offen, inhalt=inhalt, anim="pop")


# ===========================================================================================================================
# A Fall: Supermarkt, Regal und Kasse
# ===========================================================================================================================
RG = (100, 330, 420, 570)                   # Regal (Kopfhörer oben, Waschmittel Mitte, Flaschen unten)
FA_A, FA_B, FA_C = 790, 1000, 1760          # Fabian am Regal, an der Kasse, am Ausgang
CA_X = 1560                                 # Carina hinter dem Tresen
KS0, KS1, KSY = 1120, 1690, 680             # Kassentresen
NIMMT = beim("regal", "nimmt")
HINEIN = beim("pack", "hinein")
SCHIEBT = beim("pack", "schiebt")
CAR = beim("scan", "Carina")
WM = beim("scan", "Waschmittel")
FAb = ("FA_redet_r", FA_B, BODEN, SH)
CAb = ("CA_redet", CA_X, BODEN, SH)
folie([(NULL, "Fall · Im Supermarkt"), ("pack", "Fall · Das Versteck"), ("kasse", "Fall · An der Kasse"),
       ("frage", "Fall · Die Frage")], [
    hart(linienzug([(60, BODEN + 2), (1860, BODEN + 2)], NULL, breite=6, farbe=INK)),
    hart(pl("Samstagnachmittag im Supermarkt", 70, 40, NULL, fill=GELB, size=36)),
    # Regal
    hart(karte(*RG, NULL, fill=WEISS, rund=14, schatten=8, rand=5, anim="cut")),
    *[hart(linienzug([(RG[0] + 8, y), (RG[0] + RG[2] - 8, y)], NULL, breite=5, farbe=INK)) for y in (520, 710)],
    *[hart(kopfhoerer(x, 512, 72, NULL, anim="cut")) for x in (175, 265, 355)],
    kopfhoerer(445, 512, 72, NULL, anim="cut", bis=NIMMT),
    *[hart(packung(x, 702, 62, 92, NULL)) for x in (170, 250, 330)],
    packung(410, 702, 62, 92, NULL, bis="pack"),
    *[hart(ficon("tabler", "bottle", x, 890, 58, NULL, fuell=GRUEN, anim="cut")) for x in (180, 270, 360, 450)],
    # Kasse und Ausgang
    *kasse(KS0, KSY, KS1, NULL),
    hart(pl("Kasse", 1300, 800, NULL, fill=GELB, size=28, anker="m")),
    # Fabian am Regal: Kopfhörer in der Hand, Packung, Versteck
    *fig("FA", FA_A, BODEN, SH, [(beim("regal", "Fabian"), "ruhig"), ("pack", "prueft"), ("zu", "ruhig")], bis="kasse"),
    ns("Fabian", FA_A, BODEN, beim("regal", "Fabian"), BLAU, bis="kasse"),
    kopfhoerer(FA_A - 100, 650, 84, NIMMT, bis="pack"),
    pl("Kopfhörer · 120 €", 330, 250, beim("regal", "Kopfhörer"), fill=BLAU, size=30, anker="m", bis="kasse"),
    packung(FA_A - 140, 700, 120, 160, "pack", bis=HINEIN, offen=True, anim="pop"),
    kopfhoerer(FA_A - 140, 515, 80, "pack", bis=HINEIN, anim="cut"),
    bis_(pfeil(FA_A - 140, 520, FA_A - 140, 560, SCHIEBT, breite=8, kopf=22), HINEIN),
    pl("Waschmittelpackung", 600, 250, beim("pack", "Waschmittelpackung"), fill=TUERKIS, size=30, anker="l", bis="kasse"),
    packung(FA_A - 140, 700, 120, 160, HINEIN, bis="zu", offen=True, inhalt=True),
    szene(packung(FA_A - 140, 700, 120, 160, "zu", bis="kasse", inhalt=True), "144packung*", 0.8, 0.05),
    pl("von außen: nichts zu sehen", 600, 170, beim("zu", "außen"), fill=WEISS, size=30, anker="l", bis="kasse"),
    # an der Kasse
    *fig("FA", FA_B, BODEN, SH, [("kasse", "ruhig_r")], bis="f1", erst="cut"),
    *redet("FA_redet_r", FA_B, BODEN, SH, "f1", "raus"),
    ns("Fabian", FA_B, BODEN, "kasse", BLAU, bis="raus"),
    packung(1230, KSY + 18, 100, 140, "kasse", bis="raus", inhalt=True),
    pl("nur die Packung aufs Band", 1000, 250, beim("kasse", "nur"), fill=WEISS, size=30, anker="m", bis="c1"),
    # Carina erscheint mit ihrem Namen; Tresen vor ihr (verdeckt die Beine)
    *fig("CA", CA_X, BODEN, SH, [(CAR, "ruhig")], bis="c1"),
    *redet("CA_redet", CA_X, BODEN, SH, "c1", "f1"),
    *fig("CA", CA_X, BODEN, SH, [("f1", "froh"), ("frage", "ruhig")], erst="cut"),
    *kasse(KS0, KSY, KS1, CAR),
    pl("Kasse", 1300, 800, CAR, fill=GELB, size=28, anker="m"),
    packung(1230, KSY + 18, 100, 140, CAR, bis="raus", inhalt=True),
    ns("Carina", CA_X, BODEN, CAR, ORANGE),
    szene(pl("Waschmittel · 8 €", 1280, 470, WM, fill=TUERKIS, size=30, anker="m", bis="raus"), "144scan*", 0.7, 0.0),
    blase("sprech", 400, 170, "c1", 1560, 200, inhalt=["8 €, bitte."], textsize=38, figur=CAb, bis="f1"),
    blase("sprech", 560, 210, "f1", 760, 200, inhalt=["Hier, bitte.", "Schönen Tag noch."], textsize=36, figur=FAb, bis="raus"),
    # Fabian verlässt mit der Packung den Laden
    *fig("FA", FA_C, BODEN, SH, [("raus", "ruhig_r"), ("frage", "still_r")], erst="cut"),
    ns("Fabian", FA_C, BODEN, "raus", BLAU),
    packung(FA_C + 70, 690, 80, 110, "raus", inhalt=True),
    ficon("tabler", "door-exit", 1800, 330, 90, beim("raus", "verlässt"), fuell=WEISS),
    pl("mit der Packung hinaus", 1560, 140, beim("raus", "verlässt"), fill=WEISS, size=30, anker="m"),
    pl("Diebstahl oder Betrug?", 760, 140, "frage", fill=PINK, size=40, anker="m"),
    pl("Verfügung über die Kopfhörer?", 760, 230, "frage2", fill=PINK, size=34, anker="m"),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_144(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=36, zeilenabstand=1.3)
        els += e; y += 20
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=34))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_144("sv", [
    "Samstagnachmittag im Supermarkt: Fabian nimmt Kopfhörer für 120 € aus dem Regal. Er öffnet eine "
    "Waschmittelpackung, schiebt die Kopfhörer hinein und verschließt die Packung wieder; von außen ist nichts zu sehen.",
    "An der Kasse legt er nur die Packung aufs Band. Kassiererin Carina scannt das Waschmittel für 8 €. Fabian zahlt "
    "und verlässt mit der Packung samt Kopfhörern den Laden.",
    "Gegenvariante: Fabian klebt das Preisetikett des Waschmittels (8 €) auf die Kopfhörer und legt sie offen aufs "
    "Band. Carina scannt sie und gibt sie ihm für 8 € heraus.",
], "Hat sich Fabian wegen Diebstahls (§ 242) oder Betrugs (§ 263 StGB) strafbar gemacht?")

# ===========================================================================================================================
# C Abgrenzung
# ===========================================================================================================================
P1 = "Abgrenzung"
folie([("abgr", f"{P1} · Diebstahl oder Betrug?"), ("fremd", f"{P1} › § 242: eigenmächtig weggenommen"),
       ("selbst", f"{P1} › § 263: getäuscht herausgegeben"), ("bgh1", f"{P1} › Wille des Getäuschten")], rechts_frei([
    *tafel("abgr", "Diebstahl oder Betrug?"),
    z("für dieselbe Sache: § 242 oder § 263", 110, 175, "abgr", "Bold", 34),
    zit("BGHSt 41, 198, 201 (nach BGHSt 17, 205, 209)", 110, 223, beim("abgr", "aus")),
    blk(110, 280, 500, 170, HELLROT, "fremd", [("§ 242 Diebstahl", "ExtraBold", 32, INK), ("Täter führt den Schaden", "Regular", 30, INK),
                                               ("herbei: nimmt eigenmächtig weg", "Regular", 28, INK)]),
    blk(650, 280, 500, 170, BLAUHELL, "selbst", [("§ 263 Betrug", "ExtraBold", 32, INK), ("Opfer schädigt sich selbst:", "Regular", 30, INK),
                                                 ("gibt getäuscht heraus", "Regular", 30, INK)]),
    bis_(karte(110, 490, 1040, 190, "bgh1", fill=ZITAT, rund=18, schatten=6, rand=4), None),
    z("Betrug, wenn der Getäuschte „aufgrund freier, nur durch", 135, 510, "bgh1", size=31),
    z("Irrtum beeinflusster Entschließung Gewahrsam", 135, 553, "bgh1", size=31),
    z("übertragen will und überträgt“", 135, 596, "bgh1", size=31),
    zit("BGH, Urt. v. 12.10.2016 – 1 StR 402/16, Rn. 11; BGHSt 41, 198, 201", 135, 640, beim("bgh1", "überträgt", ende=True)),
    blk(110, 730, 1040, 80, GELB, "wille", [("Entscheidend: der Wille von Carina", "ExtraBold", 34, INK)]),
    *requisit([("abgr", ("tabler", "headphones", 130, BLAU), "§ 242 oder § 263?", WEISS),
               ("fremd", ("tabler", "hand-grab", 100, HELLROT), "nimmt weg", HELLROT),
               ("selbst", ("tabler", "hand-move", 100, BLAUHELL), "gibt heraus", BLAUHELL),
               ("wille", ("tabler", "help-circle", 100, GELB), "Wille von Carina", GELB)]),
    *stehend("FA", X1, [("abgr", "ruhig"), ("fremd", "ernst"), ("wille", "ruhig")]),
    *stehend("CA", X2, [("abgr", "ruhig"), ("selbst", "denkt"), ("wille", "ruhig")]),
]))

# ===========================================================================================================================
# D Wortlautkarten § 242 Abs. 1 und § 263 Abs. 1
# ===========================================================================================================================
W242 = ["„(1) Wer eine fremde bewegliche Sache einem anderen in",
        "der Absicht wegnimmt, die Sache sich oder einem Dritten",
        "rechtswidrig zuzueignen, wird mit Freiheitsstrafe bis zu",
        "fünf Jahren oder mit Geldstrafe bestraft.“"]
w1, w1_y = wortlaut(80, 150, 1100, W242, "§ 242 Abs. 1 StGB", "p242", marken=[
    (0, "fremde bewegliche Sache", beim("p242", "fremde")), (1, "wegnimmt", beim("p242", "wegnimmt"))], size=30)
W263 = ["„(1) Wer in der Absicht, sich oder einem Dritten einen",
        "rechtswidrigen Vermögensvorteil zu verschaffen, das",
        "Vermögen eines anderen dadurch beschädigt, daß er durch",
        "Vorspiegelung falscher oder durch Entstellung oder",
        "Unterdrückung wahrer Tatsachen einen Irrtum erregt oder",
        "unterhält, wird mit Freiheitsstrafe bis zu fünf Jahren",
        "oder mit Geldstrafe bestraft.“"]
w2, w2_y = wortlaut(80, w1_y + 14, 1100, W263, "§ 263 Abs. 1 StGB", "p263", marken=[
    (3, "Vorspiegelung falscher", beim("p263", "Täuschung")), (4, "einen Irrtum", beim("p263", "Irrtum")),
    (2, "Vermögen eines anderen dadurch beschädigt", beim("p263", "Vermögensschaden"))], size=30)
folie([("p242", "Wortlaut › § 242 Abs. 1 StGB"), ("p263", "Wortlaut › § 263 Abs. 1 StGB"),
       ("vf", "Wortlaut › § 263: ungeschriebene Vermögensverfügung")], rechts_frei([
    *tafel("p242", "Wortlaut", h=w2_y + 76 - 60),
    *w1, *w2,
    z("dazwischen: die ungeschriebene Vermögensverfügung", 110, w2_y + 14, "vf", "Bold", 30),
    *requisit([("p242", ("tabler", "book", 100, WEISS), "§ 242 StGB", GELB),
               ("p263", ("tabler", "book", 100, WEISS), "§ 263 StGB", GELB),
               ("vf", ("tabler", "list-numbers", 100, WEISS), "Folge 065: Betrug-Schema", WEISS)]),
    *stehend("FA", FX, [("p242", "ruhig"), ("p263", "ernst")]),
]))

# ===========================================================================================================================
# E Kernfrage: Verfügungsbewusstsein
# ===========================================================================================================================
PK = "Kernfrage"
TIPPT = beim("tippt", "eintippt")
folie([("kern", f"{PK} › Verfügungsbewusstsein"), ("nichts", f"{PK} › Carina weiß nichts"),
       ("tippt", f"{PK} › BGH: Verfügungswille beim Eintippen"), ("hm", f"{PK} › herrschende Meinung")], rechts_frei([
    *tafel("kern", "Kernfrage: Verfügungsbewusstsein"),
    z("Sachbetrug: Opfer muss wissen, worüber es verfügt", 110, 175, "vbw", "Bold", 32),
    z("= Verfügungsbewusstsein", 110, 222, beim("vbw", "Verfügungsbewusstsein"), "ExtraBold", 32),
    *neinz("Carina weiß nichts von den Kopfhörern", 290, "nichts", "Bold", 32, x=160),
    z("scannt das Waschmittel, will nur das herausgeben", 160, 340, "nurw", size=32),
    bis_(karte(110, 405, 1040, 180, "tippt", fill=ZITAT, rund=18, schatten=6, rand=4), None),
    z("„… konkretisiert der Kassierer seinen Verfügungswillen", 135, 422, "tippt", size=30),
    z("grundsätzlich dadurch, daß er die Preise der vorgelegten", 135, 464, "tippt", size=30),
    z("Waren in die Kasse eintippt …“", 135, 506, "tippt", size=30),
    zit("BGHSt 41, 198, 203 (BGH, Beschl. v. 26.7.1995 – 4 StR 234/95)", 135, 548, TIPPT),
    *neinz("nicht wahrgenommene Ware: keine bewusste Verfügung", 625, "wahr", "Bold", 32, x=160),
    zit("BGHSt 41, 198, 202 f.", 160, 673, beim("wahr", "bewusst")),
    blk(110, 730, 1040, 80, GELB, "hm", [("herrschende Meinung: keine Verfügung über die Kopfhörer", "ExtraBold", 31, INK)]),
    hart(packung(1330, FB, 110, 150, "kern", inhalt=True)),
    *requisit([("kern", ("tabler", "help-circle", 100, WEISS), "Verfügungsbewusstsein?", WEISS),
               ("nichts", ("tabler", "headphones-off", 100, WEISS), "weiß nichts", HELLROT),
               ("nurw", ("tabler", "wash", 100, BLAU), "nur das Waschmittel", TUERKIS),
               ("tippt", ("tabler", "barcode", 110, WEISS), "Preise eintippen", WEISS),
               ("hm", ("tabler", "headphones-off", 100, WEISS), "keine Verfügung", HELLROT)], px=1640),
    *stehend("CA", 1640, [("kern", "ruhig"), ("nichts", "froh"), ("tippt", "ruhig"), ("hm", "denkt")]),
]))

# ===========================================================================================================================
# F Gegenansicht und Argumente
# ===========================================================================================================================
PG = "Streit"
folie([("gegen", f"{PG} › Gegenansicht: generelles Verfügungsbewusstsein"), ("fikt", f"{PG} › BGH: „bloße Fiktion“"),
       ("frag", f"{PG} › Nachfrage an der Kasse"), ("raeub", f"{PG} › Wertung: § 252 StGB")], rechts_frei([
    *tafel("gegen", "Gegenansicht und Argumente"),
    z("Gegenansicht: generelles Verfügungsbewusstsein genügt", 110, 172, "gegen", "Bold", 32),
    z("Carina wolle alles herausgeben, was Fabian mitnimmt –", 110, 219, beim("gegen", "Carina"), size=31),
    z("hier: die Packung samt Inhalt", 110, 263, beim("gegen", "Packung"), size=31),
    zit("so OLG Düsseldorf, Beschl. v. 17.11.1992, NJW 1993, 1407: Ware im Einkaufswagen", 110, 310, "olg"),
    zit("(wiedergegeben in BGHSt 41, 198, 199 ff.)", 110, 346, beim("olg", "Einkaufswagen")),
    *neinz("BGH 1995: genereller Verfügungswille „bloße Fiktion“", 405, "fikt", "Bold", 32, x=160),
    zit("BGHSt 41, 198, 203", 160, 452, beim("fikt", "Fiktion")),
    z("Nachfrage „Ist das alles?“ und Lüge: eher Diebstahl", 110, 510, "frag", "Bold", 31),
    z("Täuschung schafft nur die Gelegenheit zur Wegnahme", 110, 556, "gelegen", size=31),
    zit("BGHSt 41, 198, 203", 110, 600, beim("gelegen", "Gelegenheit")),
    linienzug([(130, 650), (1130, 650)], "raeub", breite=3),
    z("Wertung: § 252 knüpft nur an einen Diebstahl an", 110, 670, "raeub", "Bold", 31),
    z("sonst je nach Versteck verschieden bestraft", 110, 716, beim("raeub", "Versteck"), size=31),
    zit("BGHSt 41, 198, 203 f.", 110, 762, beim("raeub", "bestraft")),
    *requisit([("gegen", pk_req(inhalt=True), "Packung samt Inhalt", WEISS),
               ("olg", ("tabler", "shopping-cart", 150, WEISS), "Einkaufswagen", WEISS),
               ("fikt", ("tabler", "ban", 100, ROT), "„bloße Fiktion“", HELLROT),
               ("frag", ("tabler", "help-circle", 100, WEISS), "„Ist das alles?“", WEISS),
               ("gelegen", ("tabler", "hand-grab", 100, HELLROT), "Gelegenheit zur Wegnahme", WEISS),
               ("raeub", ("tabler", "alert-triangle", 100, GELB), "§ 252 StGB", GELB)]),
    *stehend("FA", X1, [("gegen", "ruhig"), ("frag", "prueft"), ("raeub", "ernst")]),
    *stehend("CA", X2, [("gegen", "ruhig"), ("fikt", "denkt"), ("frag", "staunt"), ("raeub", "ruhig")]),
]))

# ===========================================================================================================================
# G Subsumtion § 242
# ===========================================================================================================================
PD = "I. Diebstahl, § 242"
folie([("wegn", f"{PD} › 1. fremde bewegliche Sache"), ("gew", f"{PD} › 2. Wegnahme: Gewahrsamsbruch"),
       ("neu", f"{PD} › 2. Wegnahme vollendet"), ("subj", f"{PD} › 3. subjektiv · II. · III."),
       ("erg", "Ergebnis · § 242 (+), § 263 (−)")], rechts_frei([
    *tafel("wegn", "I. Diebstahl, § 242 StGB"),
    *okz("1. fremde bewegliche Sachen: die Kopfhörer", 172, beim("wegn", "Kopfhörer"), "Bold", 32, x=160),
    z("2. Gewahrsam an den Kopfhörern: der Supermarkt", 160, 232, "gew", "Bold", 32),
    *okz("kein Einverständnis: Carina kennt sie nicht", 286, "bruch", size=32, x=160),
    *okz("Gewahrsamsbruch", 336, beim("bruch", "Gewahrsamsbruch"), "Bold", 32, x=160),
    *okz("neuer Gewahrsam spätestens beim Verlassen des Ladens", 392, "neu", size=31, x=160),
    blk(160, 448, 990, 70, GRUEN, beim("neu", "Weck"), [("Wegnahme vollendet", "ExtraBold", 32, INK)]),
    zit("genauer Zeitpunkt: Umstände des Einzelfalls, BGHSt 41, 198, 205", 160, 535, "enkl"),
    zit("mehr dazu: Folge 055, Gewahrsamsenklave", 160, 571, beim("enkl", "Folge")),
    *okz("3. Vorsatz, Zueignungsabsicht; II. rechtswidrig, III. schuldhaft", 625, "subj", size=30, x=160),
    blk(110, 690, 1040, 80, GELB, "erg", [("Ergebnis: Diebstahl, § 242 StGB", "ExtraBold", 34, INK)]),
    *neinz("§ 263: keine Verfügung über die Kopfhörer", 800, "kein263", "Bold", 32, x=160),
    *requisit([("wegn", ("tabler", "headphones", 130, BLAU), "fremd, beweglich", WEISS),
               ("gew", ("tabler", "building-store", 110, WEISS), "Gewahrsam: Supermarkt", WEISS),
               ("bruch", ("tabler", "hand-grab", 100, HELLROT), "Gewahrsamsbruch", HELLROT),
               ("neu", ("tabler", "door-exit", 100, WEISS), "Laden verlassen", GRUEN),
               ("subj", ("tabler", "headphones", 130, BLAU), "behalten, nicht zahlen", WEISS),
               ("erg", ("tabler", "gavel", 100, HOLZ), "§ 242 StGB", GELB),
               ("kein263", ("tabler", "ban", 100, ROT), "§ 263 (−)", HELLROT)]),
    *stehend("FA", FX, [("wegn", "ruhig"), ("bruch", "prueft"), ("erg", "still"), ("kein263", "muede")]),
]))

# ===========================================================================================================================
# H1 Gegenvariante an der Kasse: Etikettentausch
# ===========================================================================================================================
KH = (1250, KSY + 18)                       # Kopfhörer offen auf dem Band
EK = beim("etik", "Kopfhörer")
folie([("gv", "Gegenvariante · Etikettentausch"), ("gv3", "Gegenvariante · Carina sieht die Kopfhörer")], [
    hart(linienzug([(60, BODEN + 2), (1860, BODEN + 2)], "gv", breite=6, farbe=INK)),
    pl("Gegenvariante", 70, 40, "gv", fill=GELB, size=36),
    *kasse(KS0 - 200, KSY, KS1, "gv"),
    *fig("CA", CA_X, BODEN, SH, [("gv", "ruhig"), ("gv3", "ernst")], erst="cut"),
    *kasse(KS0 - 200, KSY, KS1, "gv"),
    ns("Carina", CA_X, BODEN, "gv", ORANGE),
    *fig("FA", 700, BODEN, SH, [("gv", "ruhig_r"), ("etik", "prueft_r"), ("gv3", "ruhig_r")], erst="cut"),
    ns("Fabian", 700, BODEN, "gv", BLAU),
    packung(1010, KSY + 18, 100, 140, "gv"),
    pl("8 €", 1010, 540, "gv", fill=WEISS, size=30, anker="m", bis=EK),
    pl("Preisetikett des Waschmittels", 560, 140, "etik", fill=WEISS, size=30, anker="m"),
    kopfhoerer(KH[0], KH[1], 120, EK),
    bis_(pfeil(1060, 560, 1200, 560, EK, breite=8, kopf=22), "gv2"),
    pl("8 €", KH[0], 540, EK, fill=WEISS, size=30, anker="m", bis="gv2"),
    pl("offen aufs Band", 560, 220, beim("etik", "offen"), fill=WEISS, size=30, anker="m"),
    szene(pl("Kopfhörer · 8 €", KH[0], 540, "gv2", fill=PINK, size=30, anker="m"), "144scan*", 0.7, 0.0),
    ring(KH[0], KH[1] - 50, 95, 70, beim("gv3", "sieht")),
    pl("sieht die Kopfhörer", 1560, 140, beim("gv3", "sieht"), fill=WEISS, size=30, anker="m"),
    pl("gibt sie bewusst heraus", 1560, 220, beim("gv3", "gibt"), fill=GRUEN, size=30, anker="m"),
    pl("nur zum falschen Preis", 1560, 300, beim("gv3", "falschen"), fill=HELLROT, size=30, anker="m"),
])

# ===========================================================================================================================
# H2 Gegenvariante: Sachbetrug
# ===========================================================================================================================
PV = "Gegenvariante"
folie([("gv4", f"{PV} › § 263: Täuschung, Irrtum, Verfügung"), ("gv5", f"{PV} › Vermögensschaden"),
       ("gv6", f"{PV} › Sachbetrug, § 263 StGB")], rechts_frei([
    *tafel("gv4", "Gegenvariante: § 263 StGB"),
    *okz("Täuschung über den Preis", 175, "gv4", "Bold", 32, x=160),
    *okz("Irrtum bei Carina", 235, beim("gv4", "irrt"), "Bold", 32, x=160),
    *okz("Vermögensverfügung über die Kopfhörer: bewusst", 295, beim("gv4", "verfügt"), "Bold", 32, x=160),
    *okz("Vermögensschaden: Kopfhörer für 120 € gegen 8 €", 355, "gv5", "Bold", 32, x=160),
    blk(110, 430, 1040, 80, GELB, "gv6", [("Sachbetrug, § 263 StGB", "ExtraBold", 34, INK)]),
    zit("Maßstab: BGH 1 StR 402/16, Rn. 11; BGHSt 41, 198, 203", 110, 530, beim("gv6", "Sachbetrug")),
    *requisit([("gv4", ("tabler", "tag", 100, PINK), "falscher Preis", PINK),
               ("gv5", ("tabler", "headphones", 130, BLAU), "120 € gegen 8 €", WEISS),
               ("gv6", ("tabler", "gavel", 100, HOLZ), "§ 263 StGB", GELB)]),
    *stehend("FA", X1, [("gv4", "ruhig"), ("gv6", "still")]),
    *stehend("CA", X2, [("gv4", "ruhig"), ("gv5", "sorge")]),
]))

# ===========================================================================================================================
# I Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · § 242 zuerst"), ("tipp2", "Klausurtipp · Verfügungsbewusstsein bei der Wegnahme"),
       ("tipp3", "Klausurtipp · § 263 kurz ablehnen")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Fang mit dem Delikt an, das näher liegt:", 200, 200, "tipp", "Bold", 34),
    z("versteckte Ware: zuerst § 242", 200, 248, beim("tipp", "versteckter"), size=34),
    z("Verfügungsbewusstsein bei der Wegnahme:", 200, 330, "tipp2", "Bold", 34),
    z("bewusst herausgegeben = kein Gewahrsamsbruch", 200, 378, beim("tipp2", "Gab"), size=34),
    linienzug([(130, 450), (1130, 450)], "tipp3", breite=3),
    z("§ 242 (+): § 263 danach kurz ablehnen", 200, 475, "tipp3", "Bold", 34),
    z("keine Verfügung über die versteckte Sache", 200, 523, beim("tipp3", "keine"), size=34),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# J Prüfschema
# ===========================================================================================================================
REIHEN = [("s1", 0, "I. Diebstahl, § 242 StGB", True),
          (beim("s1", "fremde"), 1, "1. fremde bewegliche Sache", False),
          ("s1b", 1, "2. Wegnahme: Bruch fremden Gewahrsams", False),
          ("s1c", 2, "Kannte die Kassiererin die Sache, gab sie sie bewusst heraus?", False),
          ("s1d", 1, "3. Vorsatz, Zueignungsabsicht · Rechtswidrigkeit · Schuld", False),
          ("s2", 0, "II. Betrug, § 263 StGB", True),
          (beim("s2", "Täuschung"), 1, "Täuschung, Irrtum, Vermögensverfügung mit", False),
          (beim("s2", "Täuschung"), 1, "Verfügungsbewusstsein, Schaden", False),
          ("s3", 0, "für dieselbe Sache: nur eines von beiden", True)]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfschema: Diebstahl oder Betrug an der Kasse"), 110, 90, "sch", 46),
           z("§§ 242, 263 StGB", 110, 160, "sch", "Bold", 32, farbe=TEXT, rechts=1800)]
y = 235
for c, ebene, text, fett in REIHEN:
    x = (130, 200, 270)[ebene]
    if c == "s1c":
        els_sch.append(karte(250, y - 14, 1560, 66, c, fill=HELLGRUEN, rund=16, schatten=5, rand=4))
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 40 if ebene == 0 else 36, rechts=1800))
    y += {0: 90, 1: 74, 2: 82}[ebene]
assert y <= 970, y
folie([("sch", "Prüfschema"), ("s1", "Prüfschema › I. Diebstahl"), ("s1b", "Prüfschema › I. 2. Wegnahme"),
       ("s1c", "Prüfschema › Verfügungsbewusstsein"), ("s2", "Prüfschema › II. Betrug")], els_sch)

# ===========================================================================================================================
# K Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Wer von der Sache ", 0), ("nichts weiß", "a"), (",", 0)], [("verfügt nicht über sie.", 0)]],
                750, 290, 44, "merke", {"a": beim("merke", "nichts")}),
    *markertext([[("Versteckte Ware", "b"), (" an der Kasse:", 0)], [("in der Regel Diebstahl,", 0)]], 750, 470, 44, "m2",
                {"b": beim("m2", "Versteckte")}),
    *markertext([[("offen vorgelegt", "c"), (" zum falschen Preis:", 0)], [("Betrug.", 0)]], 750, 650, 44, "m3",
                {"c": beim("m3", "offen")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])

# Zeichenprüfung für alle übrigen Texte (Pfade, Blöcke, Titel, Blasen)
for f_ in FOLIEN:
    for _, t_ in f_["pfade"]:
        glyphen(t_)
