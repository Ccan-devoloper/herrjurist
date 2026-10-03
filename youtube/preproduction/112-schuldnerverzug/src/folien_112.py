"""Folge 112 · Schuldnerverzug § 286 BGB: Wann gibt es Zinsen und Mahnkosten? – Serienstandard Open Peeps (Katzenkönig).
Beispielfall: Klara (Fahrradwerkstatt mit Laden) verkauft Gustav (privat) am 2.7.2026 ein Elektrorad für 2.400 €; Rechnung
„zahlbar sofort“ ohne Hinweis nach § 286 Abs. 3 Satz 1 Halbs. 2. Erste Mahnung durch Klara selbst (5 € Mahngebühr),
Zugang 10.8.2026; am 1.9.2026 Anwältin (231,95 €); Gustav zahlt nicht.
Szenen laut ../SZENENPLAN.md: A1 Werkstatt, A2 Mahnung, A3 bei Gustav (Briefkasten, Anwaltsschreiben, Frage),
B Sachverhalt, C Vier Voraussetzungen, D 1. Anspruch, E 2. Mahnung (§ 286 Abs. 1 Satz 1, Wortlaut), F Entbehrlichkeit
(§ 286 Abs. 2), G 3. 30-Tage-Regel (§ 286 Abs. 3 Satz 1, Wortlaut), H 4. Vertretenmüssen (§ 286 Abs. 4, Wortlaut),
I Zwischenergebnis am Zeitstrahl, J II. Verzugszinsen (§ 288 Abs. 1, Wortlaut), J2 § 288 Abs. 2, 5, K Verzögerungsschaden,
K2 § 287 (Wortlaut), L Ergebnis am Zeitstrahl, M Klausurtipp (Lexi), N Klausurschema, O Merksatz (Lexi).
Drei Handlungsgeräusche (Freilauf, als Gustav das Rad mitnimmt; Stift, als Klara die Mahnung schreibt; Brief fällt in den
Briefkasten; ../geraeusche_herkunft.json).
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/hand/okz/
neinz als eigene Kopie aus Folge 109 (gemeinsame Dateien unverändert); neu: tisch(), Zeitstrahl nach Tagen (tag()).
Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_112/"

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
HELLROT = (250, 205, 198, 255)
HELLGRUEN = (214, 240, 214, 255)
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
    """Rechtstafel links, rechts bleibt Platz für die Figuren; frei = rechte Grenze des Titels (Rechenleiste)."""
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
    """Figuren und Requisiten der Tafelfolien stehen rechts der Tafel (Diagramm-Icons des Zeitstrahls ausgenommen)."""
    for e in els:
        n = e.name or ""
        if n.startswith(("bild:", "ficon:")) or "/op_112/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def dicon(*a, **k):
    """Icon als Teil eines Diagramms innerhalb der Tafel (Zeitstrahl), nicht als Requisit."""
    e = ficon(*a, **k)
    e.name = "diagramm:" + (e.name or "")
    return e


def wortlaut(x, y, w, zeilen, quelle, cue, marken=(), size=32, bis=None):
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de, als Zitat mit Normangabe;
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 027/073/083/103) --------------------------------
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


def hand(name, cx, unten, hoehe, seite):
    """Äußerster Punkt der Figur (Hand) im Band 40–62 % der Höhe; seite = -1 links, +1 rechts."""
    e = peep_voll(name, cx, unten, hoehe, "_")
    a = np.asarray(e.sprite)[:, :, 3] > 40
    h = a.shape[0]
    band = a[int(h * 0.40):int(h * 0.62)]
    ys, xs = np.nonzero(band)
    i = xs.argmin() if seite < 0 else xs.argmax()
    return int(e.x + xs[i]), int(e.y + int(h * 0.40) + ys[i])


def okz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Haken davor (zur gesprochenen Bejahung)."""
    return [ok(x - 45, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]


def neinz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Kreuz davor (zur gesprochenen Verneinung)."""
    return [nein(x - 45, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]



BODEN, FH = 860, 480
X1, X2 = 1420, 1720                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
KL_N, GU_N = ORANGE, TUERKIS                # Farben der Namensschilder
PX, PY, PU = 1570, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"KL": "Klara", "GU": "Gustav"}
NFARBE = {"KL": KL_N, "GU": GU_N}


def boden(cue, hart_=False):
    e = linienzug([(40, BODEN), (1880, BODEN)], cue, breite=7, farbe=INK)
    return hart(e) if hart_ else e


def requisit(folge):
    """Wechselndes Requisit über den Figuren: folge = [(cue, (set, icon, breite, fuell), pillentext, pillenfarbe)]."""
    els = []
    for i, (c, ic, txt, pf) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else None
        if ic:
            s_, n_, br, fu = ic
            els.append(ficon(s_, n_, PX, PU, br, c, fuell=fu, bis=b))
        if txt:
            els.append(pl(txt, PX, PY, c, fill=pf, size=28, anker="m", bis=b))
    return els


def paar(c0, l, lf, r, rf):
    """Tafelszene: zwei Figuren rechts der Tafel, beide blicken zur Tafel (nach links); l, r = Kürzel GU/KL."""
    return [*fig(l, X1, FB, FR, lf), ns(NAME[l], X1, FB, c0, NFARBE[l], d=0.1),
            *fig(r, X2, FB, FR, rf, d=0.2), ns(NAME[r], X2, FB, c0, NFARBE[r], d=0.3)]


def tisch(cx, unten, cue, w=420, h=250, fill=GELB):
    """Schreibtisch/Ladentheke in Seitenansicht (programmatisch: Platte, zwei Beine; Palettenfläche, Tuschekontur)."""
    s = 2
    im = Image.new("RGBA", ((w + 12) * s, (h + 12) * s))
    dr = ImageDraw.Draw(im)
    o = 6 * s
    dr.rounded_rectangle((o, o, o + w * s, o + 30 * s), 10 * s, fill=fill, outline=INK, width=5 * s)
    for lx in (24, w - 46):
        dr.rectangle((o + lx * s, o + 28 * s, o + (lx + 22) * s, o + h * s), fill=WEISS, outline=INK, width=5 * s)
    im = im.resize((w + 12, h + 12), Image.LANCZOS)
    return El(im, cx - w / 2 - 6, unten - h - 6, cue, "cut", 0.0, None, name="tisch")


def punkt(cx, cy, cue, farbe=ROT, r=11):
    im = Image.new("RGBA", (2 * r + 8, 2 * r + 8))
    ImageDraw.Draw(im).ellipse((4, 4, 2 * r + 4, 2 * r + 4), fill=farbe, outline=INK, width=4)
    return El(im, cx - r - 4, cy - r - 4, cue, "pop", 0.0, None, name="punkt")


# --- Zeitstrahl nach Tagen (1.7. bis 30.9.2026) -----------------------------------------------------------------------------
import datetime as _dt
T0, T1 = _dt.date(2026, 7, 1), _dt.date(2026, 10, 1)


def zeitachse(x0, x1, y, cue, size=28):
    """Achse 1.7.–30.9.2026 mit Monatsstrichen und Monatsnamen. Gibt (els, tag) zurück; tag(m, d) -> x."""
    def tag(m, d):
        return x0 + (_dt.date(2026, m, d) - T0).days / (T1 - T0).days * (x1 - x0)
    els = [linienzug([(x0 - 10, y), (x1 + 10, y)], cue, breite=5)]
    for m, n in ((7, "Juli"), (8, "August"), (9, "September"), (10, None)):
        xm = x0 + (_dt.date(2026, m, 1) - T0).days / (T1 - T0).days * (x1 - x0)
        els.append(linienzug([(xm, y - 14), (xm, y + 14)], cue, breite=4))
        if n:
            xn = x0 + ((_dt.date(2026, m, 15) - T0).days) / (T1 - T0).days * (x1 - x0)
            els.append(z(n, xn - F("Bold", size).getlength(n) / 2, y + 22, cue, "Bold", size, farbe=TEXT))
    return els, tag


# ===========================================================================================================================
# A1 Fall: in der Fahrradwerkstatt, 2. Juli 2026
# ===========================================================================================================================
GUX, KLX = 1000, 1600                       # Gustav (blickt nach rechts zu Klara), Klara (blickt nach links zu Gustav)
RADX = 1300                                 # das Elektrorad steht zwischen beiden
KAUF = "kauf"
RECH = "rech"
RAD_WEG = (RECH, round(beim("rech", "nimmt")[1], 3))
RAD_DA = (RECH, round(beim("rech", "nimmt")[1] + 1.2, 3))
folie([(NULL, "Fall · In der Fahrradwerkstatt")], [
    hart(boden(NULL)),
    # Werkstatt mit Laden: Laden, Werkzeug
    hart(ficon("tabler", "building-store", 300, 560, 190, NULL, fuell=GELB)),
    hart(ficon("ph", "wrench", 480, 560, 90, NULL, fuell=WEISS)),
    hart(pl("Fahrradwerkstatt mit Laden", 330, 610, NULL, fill=WEISS, size=32, anker="m")),
    pl("2. Juli 2026", 70, 30, beim("kauf", "zweiten"), fill=GELB, size=44),
    pl("Elektrorad: 2.400 €", 330, 690, beim("kauf", "Elektrorad"), fill=GELB, size=36, anker="m"),
    pl("Gustav kauft privat", 70, 120, beim("kauf", "privat"), fill=WEISS, size=36),
    # Rechnung „zahlbar sofort“, ohne Hinweis
    ficon("tabler", "receipt-euro", 620, 830, 90, beim("rech", "Rechnung"), fuell=WEISS),
    pl("Rechnung: zahlbar sofort", 330, 770, beim("rech", "Rechnung"), fill=WEISS, size=32, anker="m"),
    pl("kein Hinweis auf Verzug nach 30 Tagen", 70, 200, beim("hinw", "Hinweis"), fill=ROT, size=34),
    # das Rad: erst zwischen beiden, dann rollt Gustav es zu sich
    hart(bis_(ficon("ph", "bicycle", RADX, BODEN, 250, NULL, fuell=None), RAD_WEG)),
    szene(bewegt(ficon("ph", "bicycle", RADX, BODEN, 250, RAD_WEG, fuell=None, anim="cut", bis=RAD_DA), RAD_WEG, RAD_DA,
                 -(RADX - 1200)), "112rad*", 0.7, 0.0),
    ficon("ph", "bicycle", 1200, BODEN, 250, RAD_DA, fuell=None, anim="cut"),
    # Gustav (links, blickt zu Klara)
    *fig("GU", GUX, BODEN, FH, [(NULL, "ruhig_r"), (beim("kauf", "Elektrorad"), "froh_r")], bis="gu1", erst="cut"),
    hart(ns("Gustav", GUX, BODEN, NULL, GU_N)),
    *redet("GU_redet_r", GUX, BODEN, FH, "gu1", "mahn"),
    blase("sprech", 600, 200, "gu1", 1250, 200, inhalt=["Ich überweise das", "in den nächsten Tagen."], textsize=36,
          figur=("GU_redet_r", GUX, BODEN, FH), bis="mahn"),
    # Klara (rechts, blickt zu Gustav)
    *fig("KL", KLX, BODEN, FH, [(NULL, "ruhig"), (beim("kauf", "Elektrorad"), "froh"), ("hinw", "ruhig"),
                                 ("gu1", "denkt")], erst="cut"),
    hart(ns("Klara", KLX, BODEN, NULL, KL_N)),
])

# ===========================================================================================================================
# A2 Fall: Klara schreibt die Mahnung (August)
# ===========================================================================================================================
KLX2 = 1480
TIX = 1000
SCHREIBT = beim("mahn", "schreibt")
folie([("mahn", "Fall · Die Mahnung")], [
    boden("mahn"),
    pl("August 2026", 70, 30, "mahn", fill=GELB, size=44),
    pl("Gustav zahlt nicht", 70, 120, beim("mahn", "zahlt"), fill=ROT, size=36),
    tisch(TIX, BODEN, "mahn"),
    ficon("tabler", "building-store", 300, BODEN, 190, "mahn", fuell=GELB),
    ficon("ph", "toolbox", 520, BODEN, 120, "mahn", fuell=ROT),
    # die Mahnung entsteht auf dem Tisch
    szene(ficon("tabler", "file-text", TIX - 60, BODEN - 256, 110, SCHREIBT, fuell=WEISS), "112stift*", 0.6, 0.0),
    ficon("tabler", "ballpen", TIX + 70, BODEN - 256, 70, SCHREIBT, fuell=GELB),
    pl("Mahnung", TIX - 60, BODEN - 430, SCHREIBT, fill=WEISS, size=32, anker="m"),
    pl("2.400 €", 300, 450, beim("kl1", "zweitausendvierhundert"), fill=GELB, size=36, anker="m"),
    pl("+ 5 € Mahngebühr", 300, 530, beim("kl1", "Mahngebühr"), fill=WEISS, size=34, anker="m"),
    *fig("KL", KLX2, BODEN, FH, [("mahn", "ruhig"), (beim("mahn", "zahlt"), "sorge"), (SCHREIBT, "denkt")], bis="kl1"),
    ns("Klara", KLX2, BODEN, "mahn", KL_N, d=0.1),
    *redet("KL_redet", KLX2, BODEN, FH, "kl1", "zug"),
    blase("sprech", 740, 200, "kl1", 960, 200, inhalt=["Bitte zahlen Sie jetzt die 2.400 €,", "dazu 5 € Mahngebühr."],
          textsize=34, figur=("KL_redet", KLX2, BODEN, FH), bis="zug"),
])

# ===========================================================================================================================
# A3 Fall: bei Gustav zu Hause – Briefkasten, Anwaltsschreiben, Frage
# ===========================================================================================================================
GUX3 = 1450
BKX = 330                                   # Briefkasten
ZUG_FALL = (beim("zug", "Brief")[0], beim("zug", "Brief")[1])
ZUG_DA = (ZUG_FALL[0], round(ZUG_FALL[1] + 0.6, 3))
ANW2 = beim("anw2", "Deren")
ANW2_DA = ("anw2", round(ANW2[1] + 0.6, 3))
folie([("zug", "Fall · Bei Gustav zu Hause"), ("anw", "Fall · Die Anwältin"), ("frage", "Fall · Die Frage")], [
    boden("zug"),
    pl("10. August 2026", 70, 30, beim("zug", "zehnten"), fill=GELB, size=44, bis="anw"),
    pl("1. September 2026", 70, 30, beim("anw", "ersten"), fill=GELB, size=44),
    ficon("tabler", "mailbox", BKX, BODEN, 200, "zug", fuell=ROT),
    ficon("tabler", "armchair", 860, BODEN, 300, "zug", fuell=LILA),
    # Klaras Brief fällt in den Briefkasten
    szene(bewegt(bis_(ficon("tabler", "mail", BKX, BODEN - 330, 90, ZUG_FALL, fuell=WEISS, anim="cut"), ZUG_DA),
                 ZUG_FALL, ZUG_DA, 0, 120), "112brief*", 0.8, 0.05),
    pl("Mahnung im Briefkasten", BKX, 560, ZUG_DA, fill=WEISS, size=32, anker="m", bis=ANW2_DA),
    # Anwaltsschreiben
    ficon("tabler", "scale", 1110, 430, 110, beim("anw", "Anwältin"), fuell=WEISS),
    pl("Klara beauftragt eine Anwältin", 70, 120, beim("anw", "beauftragt"), fill=WEISS, size=34, bis="frage"),
    bewegt(bis_(ficon("tabler", "mail", BKX, BODEN - 330, 90, ANW2, fuell=BLAU, anim="cut"), ANW2_DA), ANW2, ANW2_DA, 0, 120),
    pl("Anwaltsschreiben", BKX, 560, ANW2_DA, fill=BLAU, size=32, anker="m"),
    pl("Kosten: 231,95 €", 70, 200, beim("anw2", "zweihunderteinunddreißig"), fill=GELB, size=36, bis="frage"),
    pl("Gustav meldet sich nicht", 70, 120, "still", fill=WEISS, size=36, bis="anw"),
    pl("Gustav zahlt immer noch nicht", 70, 280, beim("noch", "zahlt"), fill=ROT, size=36, bis="frage"),
    pl("Ab wann schuldet Gustav Verzugszinsen?", 70, 120, "frage", fill=PINK, size=36),
    pl("Muss er Mahngebühr und Anwaltskosten ersetzen?", 70, 205, "frage2", fill=WEISS, size=34),
    # Gustav (rechts, blickt zum Briefkasten)
    *fig("GU", GUX3, BODEN, FH, [("zug", "ruhig"), (ZUG_DA, "staunt")], bis="gu2"),
    ns("Gustav", GUX3, BODEN, "zug", GU_N, d=0.1),
    *redet("GU_frech", GUX3, BODEN, FH, "gu2", "still"),
    blase("sprech", 700, 200, "gu2", 950, 210, inhalt=["Das hat noch Zeit. Gerade", "bin ich knapp bei Kasse."],
          textsize=34, figur=("GU_frech", GUX3, BODEN, FH), bis="still"),
    *fig("GU", GUX3, BODEN, FH, [("still", "frech"), (ANW2_DA, "staunt"), ("noch", "denkt"), ("frage", "ruhig"),
                                 ("frage2", "sorge")], erst="cut"),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_112(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=34, zeilenabstand=1.30)
        els += e; y += 18
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_112("sv", [
    "Klara betreibt eine kleine Fahrradwerkstatt mit Laden. Am 2. Juli 2026 kauft Gustav dort für private Zwecke ein "
    "Elektrorad für 2.400 Euro und nimmt es gleich mit. Die Rechnung lautet „zahlbar sofort“; einen Hinweis, dass er "
    "30 Tage nach Fälligkeit und Zugang der Rechnung in Verzug kommt, enthält sie nicht.",
    "Gustav zahlt nicht. Im August mahnt Klara ihn selbst und verlangt zusätzlich 5 Euro Mahngebühr. Der Brief liegt "
    "am 10. August in seinem Briefkasten. Gustav meldet sich nicht.",
    "Am 1. September beauftragt Klara eine Anwältin. Deren Zahlungsaufforderung kostet Klara 231,95 Euro. Gustav zahlt "
    "weiterhin nicht.",
], "Ab wann schuldet Gustav Verzugszinsen – und muss er Mahngebühr und Anwaltskosten ersetzen?")

# ===========================================================================================================================
# C Vier Voraussetzungen
# ===========================================================================================================================
PUNKTE = [("p1", "1.", "fälliger, durchsetzbarer Anspruch"), ("p2", "2.", "Mahnung oder Entbehrlichkeit"),
          ("p3", "3.", "oder: 30-Tage-Regel"), ("p4", "4.", "Vertretenmüssen")]
folie([("plan", "Schuldnerverzug, § 286 BGB › Aufbau")], rechts_frei([
    *tafel("plan", "Schuldnerverzug, § 286 BGB"),
    z("I. Voraussetzungen", 110, 190, beim("plan", "vier"), "ExtraBold", 40),
    *[e for k, (c, r, t) in enumerate(PUNKTE) for e in (
        karte(150, 262 + k * 96, 78, 70, c, fill=(BLAU, LILA, GELB, GRUEN)[k], rund=14, schatten=5, rand=4),
        z(r, 189 - F("ExtraBold", 36).getlength(r) / 2, 273 + k * 96, c, "ExtraBold", 36),
        z(t, 260, 272 + k * 96, c, "Bold", 38))],
    z("II. Rechtsfolgen", 110, 680, "p5", "ExtraBold", 40),
    *requisit([("plan", ("tabler", "list-numbers", 100, WEISS), "4 Voraussetzungen", WEISS),
               ("p2", ("tabler", "file-text", 100, WEISS), "Mahnung", WEISS),
               ("p3", ("tabler", "calendar-event", 100, WEISS), "30 Tage", GELB),
               ("p5", ("tabler", "percentage", 100, GELB), "Rechtsfolgen", WEISS)]),
    *paar("plan", "GU", [("plan", "ruhig"), ("p3", "denkt")], "KL", [("plan", "ruhig"), ("p5", "froh")]),
]))

# ===========================================================================================================================
# D I. 1. Fälliger, durchsetzbarer Anspruch
# ===========================================================================================================================
folie([("a1", "I. 1. Fälliger, durchsetzbarer Anspruch"), ("afaell", "I. 1. Anspruch › fällig"),
       ("aeinr", "I. 1. Anspruch › durchsetzbar")], rechts_frei([
    *tafel("a1", "1. Fälliger, durchsetzbarer Anspruch", size=44),
    *okz("Anspruch auf den Kaufpreis: 2.400 €", 200, beim("a433", "Anspruch"), "Bold", 38, x=160),
    zit("§ 433 Abs. 2 BGB", 160, 255, beim("a433", "Paragraf")),
    *okz("fällig: sofort", 320, beim("afaell", "sofort"), "Bold", 38, x=160),
    zit("§ 271 Abs. 1 BGB", 160, 375, beim("afaell", "Paragraf")),
    *okz("durchsetzbar: Rad übergeben, keine Einrede", 440, beim("aeinr", "durchsetzbar"), "Bold", 38, x=160),
    blk(110, 560, 1040, 90, LILA, "a103", [("Mehr dazu: Video „Einwendung und Einrede“", "ExtraBold", 34, INK)]),
    *requisit([("a1", ("tabler", "receipt-euro", 90, WEISS), "Anspruch", WEISS),
               ("a433", ("tabler", "receipt-euro", 90, GELB), "Kaufpreis 2.400 €", GELB),
               ("afaell", ("tabler", "calendar-event", 100, WEISS), "fällig: sofort", WEISS),
               ("aeinr", ("ph", "bicycle", 170, None), "Rad übergeben", WEISS),
               ("a103", ("tabler", "hand-stop", 100, WEISS), "Einreden", LILA)]),
    *paar("a1", "GU", [("a1", "ruhig"), ("aeinr", "sorge")], "KL", [("a1", "ruhig"), ("a433", "froh")]),
]))

# ===========================================================================================================================
# E I. 2. Mahnung, § 286 Abs. 1 Satz 1 (Wortlaut)
# ===========================================================================================================================
W286_1 = ["„Leistet der Schuldner auf eine Mahnung des Gläubigers nicht,",
          "die nach dem Eintritt der Fälligkeit erfolgt, so kommt er",
          "durch die Mahnung in Verzug.“"]
w286, w286_y = wortlaut(80, 180, 1100, W286_1, "§ 286 Abs. 1 Satz 1 BGB", beim("m1", "Paragraf"), marken=[
    (0, "auf eine Mahnung", beim("m1", "Mahnung", 2)), (1, "nach dem Eintritt der Fälligkeit", beim("m1", "Eintritt")),
    (2, "in Verzug", beim("m1", "Verzug"))], size=34)
folie([("m1", "I. 2. Mahnung › § 286 Abs. 1 Satz 1 BGB"), ("mdef", "I. 2. Mahnung › Begriff"),
       ("mfall", "I. 2. Mahnung › der Fall")], rechts_frei([
    *tafel("m1", "2. Mahnung"),
    *w286,
    z("Mahnung: jede eindeutige und bestimmte Aufforderung,", 110, w286_y + 40, "mdef", "Bold", 34),
    z("die geschuldete Leistung zu erbringen", 110, w286_y + 88, beim("mdef", "geschuldete"), "Bold", 34),
    zit("BGH, Urt. v. 7.5.2026 – VII ZR 107/25, Rn. 48", 110, w286_y + 140, beim("mdef", "geschuldete")),
    linienzug([(110, w286_y + 200), (1150, w286_y + 200)], "mfall", breite=3),
    *okz("Brief von Klara: Zugang am 10.8.2026", w286_y + 225, beim("mfall", "erreicht"), "Bold", 36, x=160),
    *okz("nach der Fälligkeit (2.7.2026)", w286_y + 290, beim("mfall", "nach"), "Bold", 36, x=160),
    *requisit([("m1", ("tabler", "file-text", 100, WEISS), "Mahnung", WEISS),
               ("mdef", ("tabler", "hand-finger", 100, WEISS), "eindeutig und bestimmt", WEISS),
               ("mfall", ("tabler", "mail", 100, WEISS), "Zugang 10.8.2026", GELB)]),
    *paar("m1", "GU", [("m1", "ruhig"), ("mfall", "sorge")], "KL", [("m1", "ruhig"), ("mdef", "denkt"), ("mfall", "froh")]),
]))

# ===========================================================================================================================
# F Entbehrlichkeit der Mahnung, § 286 Abs. 2
# ===========================================================================================================================
folie([("ent", "I. 2. Entbehrlichkeit › § 286 Abs. 2 BGB"), ("entn", "I. 2. Entbehrlichkeit › der Fall")], rechts_frei([
    *tafel("ent", "Mahnung entbehrlich?"),
    z("§ 286 Abs. 2 BGB, etwa:", 110, 190, beim("ent", "Absatz"), "Bold", 36),
    z("Nr. 1: Zeit für die Leistung nach dem Kalender bestimmt", 150, 260, "ent1", "Bold", 34),
    z("Termin nur vom Gläubiger gesetzt: grundsätzlich nicht", 150, 315, beim("ent1", "Termin"), size=34),
    zit("BGH, Urt. v. 8.6.2016 – VIII ZR 215/15, Rn. 23", 150, 365, beim("ent1", "genügt")),
    z("Nr. 3: ernsthafte und endgültige Verweigerung", 150, 430, "ent3", "Bold", 34),
    linienzug([(110, 510), (1150, 510)], "entn", breite=3),
    *neinz("kein Kalendertermin vereinbart", 535, beim("entn", "Beides"), "Bold", 36, x=160),
    *neinz("keine ernsthafte Verweigerung", 600, beim("entn", "liegt"), "Bold", 36, x=160),
    blk(110, 690, 1040, 80, LILA, beim("entn", "nicht"), [("Hier: beides nicht", "ExtraBold", 38, INK)]),
    *requisit([("ent", ("tabler", "file-text", 100, WEISS), "entbehrlich?", WEISS),
               ("ent1", ("tabler", "calendar-event", 100, WEISS), "Kalender", WEISS),
               ("ent3", ("tabler", "hand-stop", 100, WEISS), "Verweigerung", WEISS),
               ("entn", ("tabler", "x", 100, WEISS), "beides nicht", ROT)]),
    *paar("ent", "GU", [("ent", "ruhig"), ("ent3", "denkt")], "KL", [("ent", "ruhig"), ("entn", "denkt")]),
]))

# ===========================================================================================================================
# G I. 3. Die 30-Tage-Regel, § 286 Abs. 3 Satz 1 (Wortlaut)
# ===========================================================================================================================
W286_3 = ["„Der Schuldner einer Entgeltforderung kommt spätestens in Verzug,",
          "wenn er nicht innerhalb von 30 Tagen nach Fälligkeit und Zugang",
          "einer Rechnung oder gleichwertigen Zahlungsaufstellung leistet;",
          "dies gilt gegenüber einem Schuldner, der Verbraucher ist, nur,",
          "wenn auf diese Folgen in der Rechnung oder Zahlungsaufstellung",
          "besonders hingewiesen worden ist.“"]
w2863, w2863_y = wortlaut(80, 170, 1100, W286_3, "§ 286 Abs. 3 Satz 1 BGB", beim("d1", "Nach"), marken=[
    (1, "innerhalb von 30 Tagen", beim("d1", "dreißig", 2)), (3, "der Verbraucher ist, nur,", beim("d2", "Verbraucher")),
    (5, "besonders hingewiesen", beim("d2", "besonders"))], size=30)
folie([("d1", "I. 3. 30-Tage-Regel › § 286 Abs. 3 Satz 1 BGB"), ("d3", "I. 3. 30-Tage-Regel › der Fall")], rechts_frei([
    *tafel("d1", "3. Die 30-Tage-Regel"),
    *w2863,
    *neinz("Gustav ist Verbraucher, der Hinweis fehlt", w2863_y + 35, "d3", "Bold", 36, x=160),
    zit("vgl. BGH, Urt. v. 8.6.2016 – VIII ZR 215/15, Rn. 18", 160, w2863_y + 92, beim("d3", "Hinweis")),
    blk(110, w2863_y + 150, 1040, 80, HELLROT, "d4", [("Die Regel hilft Klara nicht", "ExtraBold", 38, INK)]),
    *requisit([("d1", ("tabler", "calendar-event", 100, WEISS), "30 Tage", GELB),
               ("d2", ("tabler", "receipt-euro", 90, WEISS), "Hinweis in der Rechnung?", WEISS),
               ("d3", ("tabler", "x", 100, WEISS), "kein Hinweis", ROT)]),
    *paar("d1", "GU", [("d1", "ruhig"), ("d3", "froh")], "KL", [("d1", "ruhig"), ("d2", "denkt"), ("d4", "sorge")]),
]))

# ===========================================================================================================================
# H I. 4. Vertretenmüssen, § 286 Abs. 4 (Wortlaut)
# ===========================================================================================================================
W286_4 = ["„(4) Der Schuldner kommt nicht in Verzug, solange die Leistung",
          "infolge eines Umstands unterbleibt, den er nicht zu vertreten hat.“"]
w2864, w2864_y = wortlaut(80, 180, 1100, W286_4, "§ 286 Abs. 4 BGB", beim("v1", "Nach"), marken=[
    (1, "den er nicht zu vertreten hat", beim("v1", "vertreten", 2))], size=32)
folie([("v1", "I. 4. Vertretenmüssen › § 286 Abs. 4 BGB"), ("vgeld", "I. 4. Vertretenmüssen › knapp bei Kasse")],
      rechts_frei([
    *tafel("v1", "4. Vertretenmüssen"),
    *w2864,
    blk(110, w2864_y + 40, 1040, 80, GELB, "vverm", [("Vertretenmüssen wird vermutet", "ExtraBold", 38, INK)]),
    *neinz("knapp bei Kasse: entlastet nicht", w2864_y + 170, beim("vgeld", "entlastet"), "Bold", 36, x=160),
    z("Für seine finanzielle Leistungsfähigkeit", 160, w2864_y + 235, beim("vgeld", "Für"), size=34),
    z("muss jeder einstehen.", 160, w2864_y + 283, beim("vgeld", "Für"), size=34),
    zit("BGH, Urt. v. 4.2.2015 – VIII ZR 175/14, Rn. 18", 160, w2864_y + 335, beim("vgeld", "einstehen")),
    *requisit([("v1", ("tabler", "scale", 100, WEISS), "Vertretenmüssen", WEISS),
               ("vverm", ("tabler", "scale", 100, GELB), "vermutet", GELB),
               ("vgeld", ("tabler", "coin-euro", 100, WEISS), "knapp bei Kasse", WEISS)]),
    *paar("v1", "GU", [("v1", "ruhig"), ("vgeld", "sorge")], "KL", [("v1", "ruhig"), ("vgeld", "froh")]),
]))

# ===========================================================================================================================
# I Zwischenergebnis am Zeitstrahl
# ===========================================================================================================================
ZY = 520
achse1, tag1 = zeitachse(150, 1130, ZY, "zs")
folie([("zs", "I. Zwischenergebnis › Zeitstrahl"), ("zs3", "I. Zwischenergebnis › Verzug ab 10.8.2026")], rechts_frei([
    *tafel("zs", "Zwischenergebnis"),
    *achse1,
    punkt(tag1(7, 2), ZY, beim("zs1", "Kaufpreis"), farbe=BLAU),
    pl("2.7.: fällig", tag1(7, 2) + 50, 290, beim("zs1", "Kaufpreis"), fill=BLAU, size=28, anker="m"),
    dicon("tabler", "receipt-euro", tag1(7, 2), ZY - 22, 50, beim("zs1", "Kaufpreis"), fuell=WEISS),
    linienzug([(tag1(7, 5), ZY - 70), (tag1(8, 1), ZY - 70)], "zs2", breite=4),
    pl("+ 30 Tage", tag1(7, 18), 380, "zs2", fill=WEISS, size=28, anker="m"),
    dicon("fluent-emoji-high-contrast", "cross-mark", tag1(8, 1), ZY - 8, 44, beim("zs2", "passiert")),
    z("kein Hinweis: kein Verzug", 150, ZY + 80, beim("zs2", "Hinweis"), "Bold", 34),
    punkt(tag1(8, 10), ZY, beim("zs3", "Mahnung"), farbe=ROT),
    dicon("tabler", "mail", tag1(8, 10), ZY - 32, 50, beim("zs3", "Mahnung"), fuell=WEISS),
    ring(int(tag1(8, 10)), ZY, 26, 26, beim("zs3", "Verzug"), farbe=ROT, breite=6),
    pl("10.8.: Mahnung", tag1(8, 10) + 90, 290, beim("zs3", "Mahnung"), fill=WEISS, size=28, anker="m"),
    blk(110, ZY + 150, 1040, 90, ROT, beim("zs3", "Verzug"), [("Gustav ist ab 10.8.2026 in Verzug", "ExtraBold", 38, INK)]),
    *requisit([("zs", ("tabler", "calendar-event", 100, WEISS), "Zeitstrahl", WEISS),
               ("zs2", ("tabler", "calendar-x", 100, WEISS), "30 Tage: nichts", WEISS),
               ("zs3", ("tabler", "mail", 100, WEISS), "Mahnung: Verzug", ROT)]),
    *paar("zs", "GU", [("zs", "ruhig"), ("zs2", "froh"), ("zs3", "sorge")], "KL", [("zs", "ruhig"), ("zs3", "froh")]),
]))

# ===========================================================================================================================
# J II. Rechtsfolgen: Verzugszinsen, § 288 Abs. 1 (Wortlaut)
# ===========================================================================================================================
W288 = ["„(1) Eine Geldschuld ist während des Verzugs zu verzinsen. Der",
        "Verzugszinssatz beträgt für das Jahr fünf Prozentpunkte über",
        "dem Basiszinssatz.“"]
w288, w288_y = wortlaut(80, 180, 1100, W288, "§ 288 Abs. 1 BGB", beim("r1", "Paragraf"), marken=[
    (0, "während des Verzugs", beim("r1", "während")), (1, "fünf Prozentpunkte über", beim("r1", "fünf"))], size=34)
folie([("r1", "II. Rechtsfolgen › Verzugszinsen, § 288 Abs. 1 BGB"), ("rbasis", "II. Verzugszinsen › Basiszinssatz")],
      rechts_frei([
    *tafel("r1", "II. Verzugszinsen"),
    *w288,
    z("Basiszinssatz seit 1.7.2026: 1,52 %", 110, w288_y + 40, "rbasis", "Bold", 36),
    zit("Deutsche Bundesbank, § 247 BGB (abgerufen am 3.10.2026)", 110, w288_y + 92, beim("rbasis", "eins")),
    blk(110, w288_y + 150, 1040, 90, GELB, "rsatz", [("Gustav: 6,52 % im Jahr, rund 13 € im Monat", "ExtraBold", 36, INK)]),
    z("Einen Schaden muss Klara nicht nachweisen.", 110, w288_y + 280, "rnach", "Bold", 36),
    zit("BGH, Urt. v. 12.10.2017 – IX ZR 267/16, Rn. 14", 110, w288_y + 332, beim("rnach", "nachweisen")),
    *requisit([("r1", ("tabler", "percentage", 100, WEISS), "Verzugszinsen", WEISS),
               ("rbasis", ("tabler", "percentage", 100, GELB), "Basiszinssatz 1,52 %", WEISS),
               ("rsatz", ("tabler", "coin-euro", 100, GELB), "rund 13 € im Monat", GELB)]),
    *paar("r1", "GU", [("r1", "ruhig"), ("rsatz", "sorge")], "KL", [("r1", "ruhig"), ("rsatz", "froh")]),
]))

# ===========================================================================================================================
# J2 Abgrenzung: ohne Verbraucher, § 288 Abs. 2 und 5
# ===========================================================================================================================
folie([("r2", "II. Verzugszinsen › ohne Verbraucher, § 288 Abs. 2, 5 BGB")], rechts_frei([
    *tafel("r2", "Ohne Verbraucher"),
    z("Entgeltforderung, kein Verbraucher beteiligt:", 110, 190, "r2", "Bold", 36),
    z("9 Prozentpunkte über dem Basiszinssatz", 150, 260, beim("r2", "neun"), "Bold", 36),
    zit("§ 288 Abs. 2 BGB", 150, 312, beim("r2", "Absatz")),
    z("dazu 40 € Pauschale", 150, 380, "r5", "Bold", 36),
    zit("§ 288 Abs. 5 BGB", 150, 432, beim("r5", "Absatz")),
    linienzug([(110, 500), (1150, 500)], "rnein", breite=3),
    *neinz("hier nicht: Gustav ist Verbraucher", 525, beim("rnein", "Beides"), "Bold", 36, x=160),
    *requisit([("r2", ("tabler", "building-store", 110, WEISS), "Geschäft unter Unternehmern", WEISS),
               ("r5", ("tabler", "coin-euro", 100, GELB), "40 € Pauschale", WEISS),
               ("rnein", ("tabler", "x", 100, WEISS), "scheidet aus", ROT)]),
    *paar("r2", "GU", [("r2", "ruhig"), ("rnein", "froh")], "KL", [("r2", "denkt"), ("rnein", "ruhig")]),
]))

# ===========================================================================================================================
# K Verzögerungsschaden, §§ 280 Abs. 1, 2, 286
# ===========================================================================================================================
folie([("s1", "II. Rechtsfolgen › Verzögerungsschaden"), ("s3", "II. Verzögerungsschaden › Mahngebühr"),
       ("s4", "II. Verzögerungsschaden › Anwaltskosten")], rechts_frei([
    *tafel("s1", "Verzögerungsschaden"),
    z("§§ 280 Abs. 1, 2, 286 BGB", 110, 185, beim("s1", "Paragraf"), "Bold", 38),
    z("Nur, was durch den Verzug entstanden ist", 110, 250, "s2", "Bold", 36),
    zit("BGH, Urt. v. 27.5.2015 – IV ZR 292/13, Rn. 51", 110, 302, beim("s2", "entstanden")),
    *neinz("5 € Mahngebühr: erste Mahnung begründet den Verzug", 370, beim("s3", "scheiden"), "Bold", 34, x=160),
    z("Sache des Gläubigers", 160, 422, beim("s3", "Sache"), size=34),
    zit("BGH, Urt. v. 19.2.2025 – VIII ZR 138/23, Rn. 77", 570, 432, beim("s3", "Sache")),
    *okz("Anwältin erst nach Verzugseintritt beauftragt", 495, beim("s4", "Sie"), "Bold", 34, x=160),
    *okz("231,95 € Anwaltskosten: regelmäßig ersatzfähig", 560, beim("s5", "regelmäßig"), "Bold", 34, x=160),
    z("auch in einfachen Fällen", 160, 612, beim("s5", "auch"), size=34),
    zit("BGH VIII ZR 138/23, Rn. 71; BGH, Urt. v. 17.9.2015 – IX ZR 280/14, Rn. 9", 160, 662, beim("s5", "einfachen")),
    *requisit([("s1", ("tabler", "receipt-euro", 90, WEISS), "Verzögerungsschaden", WEISS),
               ("s3", ("tabler", "file-text", 100, WEISS), "Mahngebühr 5 €", ROT),
               ("s4", ("tabler", "scale", 100, WEISS), "Anwältin", WEISS),
               ("s5", ("tabler", "scale", 100, GRUEN), "231,95 €", GRUEN)]),
    *paar("s1", "GU", [("s1", "ruhig"), ("s3", "froh"), ("s5", "sorge")], "KL", [("s1", "ruhig"), ("s3", "sorge"),
                                                                                ("s4", "froh")]),
]))

# ===========================================================================================================================
# K2 Haftungsverschärfung, § 287 (Wortlaut)
# ===========================================================================================================================
W287 = ["„Der Schuldner hat während des Verzugs jede Fahrlässigkeit zu",
        "vertreten. Er haftet wegen der Leistung auch für Zufall, es sei",
        "denn, dass der Schaden auch bei rechtzeitiger Leistung",
        "eingetreten sein würde.“"]
w287, w287_y = wortlaut(80, 190, 1100, W287, "§ 287 BGB", beim("s287", "Paragraf"), marken=[
    (0, "jede Fahrlässigkeit", beim("s287", "Fahrlässigkeit")), (1, "auch für Zufall", beim("s287", "Zufall"))], size=33)
folie([("s287", "II. Rechtsfolgen › Haftungsverschärfung, § 287 BGB")], rechts_frei([
    *tafel("s287", "Haftungsverschärfung"),
    *w287,
    blk(110, w287_y + 50, 1040, 80, LILA, beim("s287", "haftet"), [("im Verzug: schärfere Haftung", "ExtraBold", 38, INK)]),
    *requisit([("s287", ("tabler", "scale", 100, WEISS), "Haftung", WEISS),
               (beim("s287", "Zufall"), ("tabler", "alarm", 100, WEISS), "auch Zufall", LILA)]),
    *paar("s287", "GU", [("s287", "ruhig"), (beim("s287", "Zufall"), "staunt")], "KL", [("s287", "ruhig")]),
]))

# ===========================================================================================================================
# L Ergebnis am Zeitstrahl
# ===========================================================================================================================
ZY2 = 560
achse2, tag2 = zeitachse(150, 1130, ZY2, "e1")
folie([("e1", "Ergebnis")], rechts_frei([
    *tafel("e1", "Ergebnis"),
    *okz("Kaufpreis: 2.400 €", 190, beim("e1", "zweitausendvierhundert"), "Bold", 38, x=160),
    *achse2,
    punkt(tag2(8, 10), ZY2, beim("e2", "Zugang"), farbe=ROT),
    pl("10.8.: Zugang der Mahnung", tag2(8, 10), 345, beim("e2", "Zugang"), fill=ROT, size=28, anker="m"),
    blk(int(tag2(8, 11)), ZY2 - 62, int(tag2(9, 30) - tag2(8, 11)), 50, GRUEN, beim("e2", "Verzugszinsen"),
        [("Verzugszinsen ab 11.8.", "ExtraBold", 28, INK)], anim="fade"),
    z("Tag des Zugangs zählt nicht mit: § 187 Abs. 1 BGB entsprechend", 150, ZY2 + 75, beim("e2", "Tag"), size=28,
      farbe=TEXT),
    zit("vgl. BGH, Urt. v. 4.7.2017 – XI ZR 562/15, Rn. 103 (zu Prozesszinsen)", 150, ZY2 + 115, beim("e2", "Zugang")),
    punkt(tag2(9, 1), ZY2, beim("e3", "Anwaltskosten"), farbe=GRUEN),
    *okz("Anwaltskosten 231,95 €: ersetzen", ZY2 + 175, beim("e3", "ersetzen"), "Bold", 36, x=160),
    *neinz("Mahngebühr 5 €: nicht", ZY2 + 240, beim("e4", "Mahngebühr"), "Bold", 36, x=160),
    *requisit([("e1", ("tabler", "receipt-euro", 90, GELB), "2.400 €", GELB),
               ("e2", ("tabler", "percentage", 100, GRUEN), "Zinsen ab 11.8.", GRUEN),
               ("e3", ("tabler", "scale", 100, GRUEN), "Anwaltskosten: ja", GRUEN),
               ("e4", ("tabler", "file-text", 100, WEISS), "Mahngebühr: nein", ROT)]),
    *paar("e1", "GU", [("e1", "sorge"), ("e4", "froh")], "KL", [("e1", "ruhig"), ("e3", "froh"), ("e4", "sorge")]),
]))

# ===========================================================================================================================
# M Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Tag des Verzugsbeginns"), ("tipp2", "Klausurtipp · typischer Fehler")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Zuerst den Tag des Verzugsbeginns bestimmen!", 200, 200, beim("tipp", "Bestimme"), "Bold", 36),
    z("Dann jede Kostenposition einzeln prüfen:", 200, 270, beim("tipp", "prüfe"), size=34),
    z("Ist sie erst nach Verzugseintritt entstanden?", 200, 320, beim("tipp", "Kostenposition"), size=34),
    linienzug([(130, 400), (1130, 400)], "tipp2", breite=3),
    z("Typischer Fehler:", 200, 430, "tipp2", "Bold", 36),
    z("Anwalt schreibt schon die erste Mahnung:", 200, 490, beim("tipp2", "Lässt"), size=34),
    z("dessen Kosten sind kein Verzugsschaden.", 200, 540, beim("tipp2", "dessen"), "Bold", 34),
    zit("BGH, Urt. v. 27.5.2015 – IV ZR 292/13, Rn. 51", 200, 595, beim("tipp2", "Verzugsschaden")),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# N Klausurschema
# ===========================================================================================================================
REIHEN = [("k1", "I.", "Voraussetzungen", "§ 286 BGB", BLAU, 0),
          ("k11", "1.", "fälliger, durchsetzbarer Anspruch", "", None, 1),
          ("k12", "2.", "Mahnung oder Entbehrlichkeit", "§ 286 Abs. 1, 2", None, 1),
          ("k13", "3.", "oder: 30-Tage-Regel", "§ 286 Abs. 3", None, 1),
          ("k14", "4.", "Vertretenmüssen, vermutet", "§ 286 Abs. 4", None, 1),
          ("k2", "II.", "Rechtsfolgen", "", GELB, 0),
          ("k21", "•", "Verzugszinsen", "§ 288 BGB", None, 1),
          ("k22", "•", "Verzögerungsschaden", "§§ 280 Abs. 1, 2, 286 BGB", None, 1),
          ("k23", "•", "Haftungsverschärfung", "§ 287 BGB", None, 1)]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Klausurschema: Schuldnerverzug"), 110, 90, "sch", 50)]
y = 190
for c, r, kopf, norm, farbe, ebene in REIHEN:
    if ebene == 0:
        els_sch += [karte(110, y, 100, 70, c, fill=farbe, rund=14, schatten=5, rand=4),
                    z(r, 160 - F("ExtraBold", 38).getlength(r) / 2, y + 10, c, "ExtraBold", 38, rechts=1820),
                    z(kopf, 245, y + 10, c, "ExtraBold", 40, rechts=1820)]
        hh = 88
    else:
        els_sch += [z(r, 260, y + 4, c, "Bold", 36, rechts=1820), z(kopf, 320, y + 4, c, "Bold", 36, rechts=1820)]
        hh = 72
    if norm:
        els_sch.append(zit(norm, 1300, y + (18 if ebene == 0 else 12), c, size=30, rechts=1820))
    y += hh
assert y <= 970, y
folie([("sch", "Klausurschema"), ("k1", "Klausurschema › I. Voraussetzungen"), ("k2", "Klausurschema › II. Rechtsfolgen")],
      els_sch)

# ===========================================================================================================================
# O Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Zinsen und Verzugskosten gibt es", 0)], [("erst ab dem Verzug.", "a")]],
                750, 290, 44, "merke", {"a": beim("merke", "erst")}),
    *markertext([[("Beim Verbraucher löst ihn meist", 0)], [("erst ", 0), ("die Mahnung", "b"), (" aus,", 0)]],
                750, 480, 42, "mk2", {"b": beim("mk2", "Mahnung")}),
    *markertext([[("und diese erste Mahnung", 0)], [("zahlt der Gläubiger selbst.", "c")]], 750, 670, 42, "mk3",
                {"c": beim("mk3", "zahlt")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
