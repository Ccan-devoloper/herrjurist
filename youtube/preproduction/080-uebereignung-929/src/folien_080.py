"""Folge 080 · § 929 S. 1 BGB: Einigung und Übergabe – Übereignung Schema – Serienstandard Open Peeps (Katzenkönig).
Beispielfall: Annika verkauft Herrn Brunner am Abend ihr Fahrrad für 300 €, er zahlt bar und holt das Rad erst am nächsten
Morgen ab; über Nacht steht es im Hof von Annika.
Szenen laut ../SZENENPLAN.md: A1 Verkauf am Abend, A2 Nacht/Frage, B Sachverhalt, C Kaufvertrag und Übereignung,
D § 929 S. 1 (Wortlaut, vier Prüfungspunkte), E I. Einigung, F II. Übergabe (Wortlaut § 854 I), G Hof bei Nacht (Subsumtion),
H III. Einigsein, I IV. Berechtigung, J Lösung heute Nacht, K § 930/§ 446, L der nächste Morgen (Übergabe), M Abwandlung
§ 449, N Klausurtipp (Lexi), O Klausurschema, P Merksatz (Lexi).
Zwei Handlungsgeräusche (Geldscheine bei der Zahlung, Fahrradklingel beim Losfahren; ../geraeusche_herkunft.json).
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/hand als
eigene Kopie aus Folge 076 (gemeinsame Dateien unverändert). Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_080/"

FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
ZITAT = (246, 246, 250, 255)
HELLROT = (250, 205, 198, 255)
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


def tafel(cue, titel_, h=840, fill=WEISS, size=46):
    """Rechtstafel links, rechts bleibt Platz für die Figuren."""
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(glyphen(titel_), 110, 100, cue, size)]


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
        if n.startswith(("bild:", "ficon:")) or "/op_080/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 027/073) ------------------------------------
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
AN_F, BR_F = BLAU, WEISS                    # Farben der Namensschilder
PX, PY, PU = 1570, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante


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


def paar(c0, l, lf, r, rf, ln="Annika", lfarbe=AN_F, rn="Herr Brunner", rfarbe=BR_F):
    """Tafelszene: zwei Figuren rechts der Tafel, beide blicken zur Tafel (nach links)."""
    return [*fig(l, X1, FB, FR, lf), ns(ln, X1, FB, c0, lfarbe, d=0.1),
            *fig(r, X2, FB, FR, rf, d=0.2), ns(rn, X2, FB, c0, rfarbe, d=0.3)]


RAD = ("ph", "bicycle", 120, WEISS)
GELD = ("tabler", "cash-banknote", 110, GRUEN)


def rad(cx, cue, breite=300, bis=None, anim="pop", d=0.0):
    """Das Fahrrad von Annika (Phosphor bicycle, Räder weiß gefüllt), auf dem Boden."""
    return ficon("ph", "bicycle", cx, BODEN, breite, cue, fuell=WEISS, bis=bis, anim=anim, d=d)


# A1 Fall: der Verkauf am Abend ----------------------------------------------------------------------------------------------
AX, RX, BX = 520, 930, 1480
AH = hand("AN_ruhig_r", AX, BODEN, FH, +1)          # Hand von Annika (zu Herrn Brunner hin)
BH = hand("BR_redet", BX, BODEN, FH, -1)            # Hand von Herrn Brunner (zu Annika hin)
ZAHLT = (beim("zahlt", "zahlt"), beim("zahlt", "bar", ende=True))
folie([(NULL, "Fall · Der Fahrradverkauf"), ("zahlt", "Fall · Bar bezahlt"), ("fuss", "Fall · Abholung erst morgen")], [
    hart(pl("Annika verkauft ihr Fahrrad", 70, 40, NULL, fill=GELB, size=44, bis="kommt")),
    pl("Am Abend im Hof", 70, 40, "kommt", fill=GELB, size=44),
    hart(boden(NULL)),
    hart(ficon("tabler", "building-cottage", 200, BODEN, 250, NULL, fuell=GELB)),
    hart(rad(RX, NULL)),
    ficon("tabler", "fence", 1790, BODEN, 150, beim("kommt", "Hof"), fuell=WEISS),
    # Annika (links, blickt zu Herrn Brunner)
    *fig("AN", AX, BODEN, FH, [(NULL, "ruhig_r")], bis="an1", erst="cut"),
    *redet("AN_redet_r", AX, BODEN, FH, "an1", "nacht"),
    hart(ns("Annika", AX, BODEN, NULL, AN_F)),
    # Herr Brunner (rechts, blickt zu Annika)
    *fig("BR", BX, BODEN, FH, [(beim("kommt", "Brunner"), "ruhig"), (beim("kommt", "schaut"), "froh")], bis="br1"),
    *redet("BR_redet", BX, BODEN, FH, "br1", "zahlt"),
    *fig("BR", BX, BODEN, FH, [("zahlt", "ruhig")], erst="cut"),
    ns("Herr Brunner", BX, BODEN, beim("kommt", "Brunner"), BR_F),
    blase("sprech", 700, 170, "br1", 1080, 230, inhalt=["Ich nehme es. Hier sind 300 €."], textsize=34,
          figur=("BR_redet", BX, BODEN, FH), bis="zahlt"),
    # das Geld: erst in der Hand von Herrn Brunner, dann bei Annika
    ficon("tabler", "cash-banknote", BH[0] - 40, BH[1] + 20, 90, beim("br1", "Hier"), fuell=GRUEN, bis=ZAHLT[0]),
    szene(bewegt(ficon("tabler", "cash-banknote", AH[0] + 40, AH[1] + 20, 90, ZAHLT[0], fuell=GRUEN, anim="cut"),
                 *ZAHLT, (BH[0] - 40) - (AH[0] + 40), 0), "080geld*", 0.8, 0.0),
    pl("300 €, bar", 930, 440, beim("zahlt", "bar"), fill=GRUEN, size=32, anker="m"),
    pl("zu Fuß gekommen", 1480, 300, beim("fuss", "Fuß"), fill=WEISS, size=30, anker="m", bis="an1"),
    ficon("tabler", "calendar-event", 930, 590, 70, beim("fuss", "morgen"), fuell=WEISS),
    pl("Abholung: morgen", 930, 600, beim("fuss", "morgen"), fill=PINK, size=32, anker="m"),
    blase("sprech", 780, 210, "an1", 1000, 220, inhalt=["Kein Problem. Das Rad bleibt", "bis morgen hier im Hof."],
          textsize=34, figur=("AN_redet_r", AX, BODEN, FH), bis="nacht"),
])

# A2 Fall: die Nacht -------------------------------------------------------------------------------------------------------------
AX2, RX2, HX, BX2, MITTE = 430, 790, 1390, 1690, 1130
NACHT = [
    boden("nacht"),
    linienzug([(MITTE, 330), (MITTE, BODEN)], "nacht", breite=5, farbe=INK),
    ficon("tabler", "moon-stars", 900, 290, 100, "nacht", fuell=GELB),
    pl("heute Nacht", 900, 305, "nacht", fill=WEISS, size=30, anker="m"),
    pl("Hof von Annika", 560, 190, "nacht", fill=BLAU, size=30, anker="m"),
    pl("Herr Brunner zu Hause", 1540, 190, beim("nacht", "Nach"), fill=WEISS, size=30, anker="m"),
    rad(RX2, "nacht", 280),
    ficon("tabler", "home", HX, BODEN, 220, beim("nacht", "Nach"), fuell=WEISS),
]
folie([("nacht", "Fall · Die Nacht"), ("frage", "Fall · Die Frage")], [
    *NACHT,
    *fig("AN", AX2, BODEN, FH, [("nacht", "ruhig_r")], erst="cut"),
    ns("Annika", AX2, BODEN, "nacht", AN_F),
    *fig("BR", BX2, BODEN, FH, [("nacht", "ruhig"), ("frage", "denkt")], erst="cut"),
    ns("Herr Brunner", BX2, BODEN, "nacht", BR_F),
    pl("Wem gehört das Fahrrad heute Nacht?", 960, 70, "frage", fill=PINK, size=40, anker="m"),
    pl("Annika?", AX2, 290, beim("frage2", "Annika"), fill=BLAU, size=32, anker="m"),
    pl("Herr Brunner?", BX2, 290, beim("frage2", "Herrn"), fill=WEISS, size=32, anker="m"),
])

# B Sachverhalt ---------------------------------------------------------------------------------------------------------------
def sachverhalt_080(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=38, zeilenabstand=1.34)
        els += e; y += 26
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=38))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_080("sv", [
    "Annika verkauft ihr Fahrrad. Am Abend sieht sich Herr Brunner das Rad in ihrem Hof an und kauft es für 300 Euro. "
    "Er zahlt sofort bar.",
    "Weil er zu Fuß gekommen ist, will er das Rad erst am nächsten Morgen abholen. Annika ist einverstanden. Das Rad "
    "bleibt über Nacht in ihrem Hof. Weitere Vereinbarungen treffen die beiden nicht.",
], "Wem gehört das Fahrrad in der Nacht?")

# C Kaufvertrag und Übereignung ---------------------------------------------------------------------------------------------------
folie([("kv", "Kaufvertrag · § 433 Abs. 1 S. 1 BGB"), ("eigen", "Kaufvertrag und Übereignung")], rechts_frei([
    *tafel("kv", "Kaufvertrag und Übereignung"),
    z("Kaufvertrag, § 433 Abs. 1 Satz 1 BGB", 110, 200, "kv", "Bold", 38),
    z("verpflichtet Annika: das Rad übergeben", 160, 265, beim("kv", "übergeben"), size=36),
    z("und das Eigentum verschaffen", 160, 320, beim("kv", "Eigentum"), size=36),
    *neinz("überträgt selbst kein Eigentum", 410, "eigen", "Bold", 38, x=160),
    blk(110, 510, 1040, 100, GELB, beim("eigen", "Dafür"), [("Dafür: eine eigene Übereignung", "ExtraBold", 40, INK)]),
    *requisit([("kv", ("tabler", "receipt", 100, WEISS), "Kaufvertrag", WEISS),
               (beim("eigen", "Dafür"), RAD, "Übereignung", GELB)]),
    *paar("kv", "AN", [("kv", "ruhig")], "BR", [("kv", "ruhig"), ("eigen", "denkt")]),
]))

# D § 929 Satz 1 (Wortlaut) und vier Prüfungspunkte -------------------------------------------------------------------------------
W929 = ["„Zur Übertragung des Eigentums an einer beweglichen Sache ist",
        "erforderlich, dass der Eigentümer die Sache dem Erwerber übergibt",
        "und beide darüber einig sind, dass das Eigentum übergehen soll.“"]
w929, w929_y = wortlaut(80, 180, 1100, W929, "§ 929 Satz 1 BGB", "p929", marken=[
    (1, "der Eigentümer", beim("w929", "Eigentümer")), (1, "übergibt", beim("w929", "übergibt")),
    (2, "einig sind", beim("w929", "einig"))], size=32)
VY = w929_y + 45
folie([("p929", "Übereignung · § 929 S. 1 BGB"), ("vier", "§ 929 S. 1 BGB › vier Prüfungspunkte")], rechts_frei([
    *tafel("p929", "Das Fahrrad: § 929 Satz 1 BGB"),
    *w929,
    z("Vier Prüfungspunkte:", 110, VY, "vier", "Bold", 38),
    z("I. Einigung", 160, VY + 65, "v1", "Bold", 36),
    z("II. Übergabe", 160, VY + 120, "v2", "Bold", 36),
    z("III. Einigsein bei der Übergabe", 160, VY + 175, "v3", "Bold", 36),
    z("IV. Berechtigung", 160, VY + 230, "v4", "Bold", 36),
    *requisit([("p929", RAD, "§ 929 S. 1 BGB", GELB), ("vier", ("tabler", "list-check", 100, WEISS), "4 Prüfungspunkte", WEISS)]),
    *paar("p929", "AN", [("p929", "ruhig")], "BR", [("p929", "ruhig")]),
]))

# E I. Einigung ---------------------------------------------------------------------------------------------------------------------
folie([("einig", "§ 929 S. 1 BGB › I. Einigung"), ("best", "I. Einigung › bestimmte Sache"), ("abstr", "I. Einigung › Abstraktion")],
      rechts_frei([
    *tafel("einig", "I. Einigung"),
    z("dinglicher Vertrag: Eigentum soll übergehen", 110, 190, beim("einig", "dinglicher"), "Bold", 36),
    z("Angebot und Annahme, §§ 145 ff. BGB", 160, 255, "p145", size=34),
    zit("BGH, Urt. v. 16.10.2015 – V ZR 240/14, Rn. 9", 160, 305, beim("p145", "allgemeinen")),
    z("bestimmte Sache: genau dieses Fahrrad", 110, 380, "best", "Bold", 36),
    zit("BGH, Urt. v. 16.12.2022 – V ZR 174/21, Rn. 10", 160, 435, beim("best", "bestimmte")),
    z("getrennt und abstrakt vom Kaufvertrag", 110, 510, "abstr", "Bold", 36),
    zit("Mehr dazu im Video zum Abstraktionsprinzip", 160, 565, beim("abstr", "Mehr"), size=28),
    blk(110, 640, 1040, 100, HELL, "offen", [("Heute schon geeinigt? Kann offenbleiben.", "ExtraBold", 38, INK)]),
    *requisit([("einig", ("ph", "handshake", 120, WEISS), "Einigung", GELB), (beim("best", "dieses"), RAD, "dieses Fahrrad", BLAU),
               ("abstr", ("tabler", "link-off", 110, WEISS), "abstrakt", LILA),
               ("offen", ("tabler", "question-mark", 90, WEISS), "heute schon?", WEISS)]),
    *paar("einig", "AN", [("einig", "ruhig"), ("offen", "denkt")], "BR", [("einig", "ruhig"), ("offen", "denkt")]),
]))

# F II. Übergabe (Wortlaut § 854 Abs. 1) -------------------------------------------------------------------------------------------
W854 = ["„Der Besitz einer Sache wird durch die Erlangung der",
        "tatsächlichen Gewalt über die Sache erworben.“"]
w854, w854_y = wortlaut(80, 250, 1100, W854, "§ 854 Abs. 1 BGB", "w854", marken=[
    (0, "Erlangung der", beim("w854", "Erlangung")), (1, "tatsächlichen Gewalt", beim("w854", "tatsächlichen"))], size=34)
folie([("ueberg", "§ 929 S. 1 BGB › II. Übergabe"), ("p854", "II. Übergabe › Besitzerwerb, § 854 Abs. 1 BGB"),
       ("hm", "II. Übergabe › Besitzverlust und Veranlassung"), ("geheiss", "II. Übergabe › Geheißperson")], rechts_frei([
    *tafel("ueberg", "II. Übergabe"),
    z("1. Besitzerwerb des Erwerbers", 110, 180, beim("ueberg", "Erwerber"), "Bold", 36),
    *w854,
    zit("BGH, Urt. v. 16.10.2015 – V ZR 240/14, Rn. 21", 110, w854_y + 10, beim("w854", "erworben")),
    z("nach herrschender Meinung außerdem:", 110, w854_y + 70, "hm", size=34, farbe=TEXT),
    z("2. vollständiger Besitzverlust des Veräußerers", 110, w854_y + 125, "verlust", "Bold", 36),
    z("3. auf Veranlassung des Veräußerers", 110, w854_y + 185, "veranl", "Bold", 36),
    z("Empfang auch durch eine Geheißperson", 110, w854_y + 265, "geheiss", size=34),
    z("des Erwerbers (BGH, a. a. O., Rn. 21)", 160, w854_y + 315, beim("geheiss", "Erwerber"), size=30, farbe=TEXT),
    *requisit([("ueberg", ("tabler", "arrows-exchange", 120, WEISS), "Übergabe", GELB),
               (beim("w854", "tatsächlichen"), ("tabler", "hand-grab", 110, WEISS), "tatsächliche Gewalt", BLAU),
               ("verlust", ("tabler", "hand-off", 110, WEISS), "Besitz ganz aufgeben", WEISS),
               ("veranl", ("tabler", "hand-finger", 100, WEISS), "Veranlassung", WEISS),
               ("geheiss", ("tabler", "truck-delivery", 120, WEISS), "Geheißperson", LILA)]),
    *paar("ueberg", "AN", [("ueberg", "ruhig")], "BR", [("ueberg", "ruhig"), ("hm", "denkt")]),
]))

# G Hof bei Nacht: Subsumtion Übergabe ----------------------------------------------------------------------------------------------
folie([("hof", "II. Übergabe › heute Nacht?"), ("fehlt", "II. Übergabe › fehlt")], [
    ficon("tabler", "moon-stars", 970, 290, 100, "hof", fuell=GELB),
    pl("heute Nacht", 970, 305, "hof", fill=WEISS, size=30, anker="m"),
    pl("Hof von Annika", 560, 190, "hof", fill=BLAU, size=30, anker="m"),
    pl("Herr Brunner zu Hause", 1540, 190, "hof", fill=WEISS, size=30, anker="m"),
    boden("hof"), linienzug([(MITTE, 330), (MITTE, BODEN)], "hof", breite=5, farbe=INK),
    rad(RX2, "hof", 280), ficon("tabler", "home", HX, BODEN, 220, "hof", fuell=WEISS),
    *fig("AN", AX2, BODEN, FH, [("hof", "ruhig_r"), ("gewalt", "froh_r")]),
    ns("Annika", AX2, BODEN, "hof", AN_F),
    *fig("BR", BX2, BODEN, FH, [("hof", "ruhig"), (beim("gewalt", "nicht"), "denkt")]),
    ns("Herr Brunner", BX2, BODEN, "hof", BR_F),
    pl("tatsächliche Gewalt: Annika", 500, 280, "gewalt", fill=GRUEN, size=30, anker="m"),
    ok(250, 300, "gewalt", gr=22),
    pl("Herr Brunner: kein Besitz", 1560, 280, beim("gewalt", "nicht"), fill=HELLROT, size=30, anker="m"),
    nein(1345, 300, beim("gewalt", "nicht"), gr=22),
    pl("Die Übergabe fehlt", 960, 70, "fehlt", fill=PINK, size=44, anker="m"),
])

# H III. Einigsein im Zeitpunkt der Übergabe -----------------------------------------------------------------------------------------
folie([("einigsein", "§ 929 S. 1 BGB › III. Einigsein"), ("widerruf", "III. Einigsein › Widerruf bis zur Übergabe")],
      rechts_frei([
    *tafel("einigsein", "III. Einigsein bei der Übergabe"),
    z("im Zeitpunkt der Übergabe noch einig", 110, 200, beim("einigsein", "Zeitpunkt"), "Bold", 36),
    z("h. M.: Einigung bis zur Übergabe widerruflich", 110, 290, "widerruf", "Bold", 36),
    z("Heute schon geeinigt? Annika könnte", 160, 380, "reue", size=34),
    z("bis morgen noch widerrufen", 160, 430, beim("reue", "bis"), size=34),
    *neinz("dann kein Eigentumsübergang", 500, beim("reue", "Dann"), "Bold", 36, x=210),
    blk(110, 600, 1040, 100, HELL, "bindet", [("Aus § 433 BGB bleibt sie verpflichtet", "ExtraBold", 38, INK)]),
    *requisit([("einigsein", ("ph", "handshake", 120, WEISS), "noch einig?", GELB),
               (beim("widerruf", "widerrufen"), ("tabler", "arrow-back-up", 110, WEISS), "Widerruf", ROT),
               ("bindet", ("tabler", "receipt", 100, WEISS), "Kaufvertrag bindet", WEISS)]),
    *paar("einigsein", "AN", [("einigsein", "ruhig"), ("reue", "denkt"), ("bindet", "sorge")], "BR",
          [("einigsein", "ruhig"), ("reue", "ernst")]),
]))

# I IV. Berechtigung ------------------------------------------------------------------------------------------------------------------
folie([("berecht", "§ 929 S. 1 BGB › IV. Berechtigung"), ("gutgl", "IV. Berechtigung › gutgläubiger Erwerb")], rechts_frei([
    *tafel("berecht", "IV. Berechtigung"),
    z("Eigentümer", 110, 200, beim("berecht", "Eigentümer"), "Bold", 38),
    z("oder mit dessen Einwilligung, § 185 Abs. 1 BGB", 110, 265, "p185", size=36),
    *okz("Annika ist Eigentümerin ihres Fahrrads", 360, "annika", "Bold", 36, x=160),
    z("Gehört die Sache einem anderen:", 110, 470, "gutgl", size=36),
    z("sonst nur gutgläubiger Erwerb, §§ 932 ff. BGB", 160, 525, beim("gutgl", "gutgläubige"), "Bold", 36),
    zit("Mehr dazu im Video zum Sachenrecht im Überblick", 160, 590, beim("gutgl", "Den"), size=28),
    *requisit([("berecht", ("tabler", "key", 110, GELB), "Berechtigung", GELB), ("annika", RAD, "gehört Annika", GRUEN),
               (beim("gutgl", "gutgläubige"), ("tabler", "shield-check", 110, GRUEN), "guter Glaube", WEISS)]),
    *paar("berecht", "AN", [("berecht", "ruhig"), ("annika", "froh")], "BR", [("berecht", "ruhig")]),
]))

# J Lösung: heute Nacht ----------------------------------------------------------------------------------------------------------------
folie([("loes", "Lösung · heute Nacht"), ("geld", "Lösung › das Geld")], rechts_frei([
    *tafel("loes", "Heute Nacht"),
    *neinz("Übergabe fehlt", 190, beim("loes", "fehlt"), "Bold", 38, x=160),
    blk(110, 270, 1040, 100, GRUEN, beim("loes", "Annika"), [("Annika bleibt Eigentümerin", "ExtraBold", 40, INK)]),
    z("Herr Brunner: nur Anspruch aus dem", 110, 410, "anspr", size=36),
    z("Kaufvertrag, § 433 Abs. 1 Satz 1 BGB", 160, 460, beim("anspr", "Kaufvertrag"), size=36),
    z("Geld: übergeben und einig", 110, 560, "geld", "Bold", 36),
    *okz("Am Geld ist Annika schon Eigentümerin", 625, beim("geld", "Am"), "Bold", 36, x=160),
    *requisit([("loes", RAD, "Rad: heute Nacht", BLAU), (beim("loes", "Annika"), RAD, "Rad: gehört Annika", GRUEN), ("anspr", ("tabler", "receipt", 100, WEISS), "nur Anspruch", WEISS),
               ("geld", GELD, "Geld", WEISS), (beim("geld", "Am"), GELD, "Geld: gehört Annika", GRUEN)]),
    *paar("loes", "AN", [("loes", "ruhig"), (beim("geld", "Am"), "froh")], "BR", [("loes", "ruhig"), ("anspr", "denkt")]),
]))

# K § 930 und § 446 --------------------------------------------------------------------------------------------------------------------
folie([("p930", "Übergabeersatz · § 930 BGB"), ("p446", "Gefahrübergang · § 446 S. 1 BGB")], rechts_frei([
    *tafel("p930", "Anders wäre es …"),
    z("ausdrücklich vereinbart: Herr Brunner", 110, 190, "p930", "Bold", 36),
    z("wird sofort Eigentümer, Annika", 160, 245, beim("p930", "sofort"), "Bold", 36),
    z("verwahrt das Rad für ihn", 160, 300, beim("p930", "verwahrt"), "Bold", 36),
    z("Besitzmittlungsverhältnis ersetzt die Übergabe,", 110, 380, "p930b", size=34),
    z("§ 930 BGB", 160, 430, beim("p930b", "Paragraf"), "Bold", 34),
    linienzug([(110, 505), (1150, 505)], "p446", breite=3),
    z("Gefahr des zufälligen Untergangs:", 110, 535, "p446", "Bold", 36),
    z("erst mit der Übergabe auf den Käufer,", 160, 590, beim("p446", "erst"), size=34),
    z("§ 446 Satz 1 BGB", 160, 640, beim("p446", "erst"), size=34),
    blk(110, 710, 1040, 90, HELL, beim("p446", "Das"), [("Kaufrecht, nicht Sachenrecht", "ExtraBold", 38, INK)]),
    *requisit([("p930", ("ph", "handshake", 120, WEISS), "Vereinbarung", WEISS),
               (beim("p930", "verwahrt"), ("tabler", "lock", 100, GELB), "verwahrt für ihn", GELB),
               (beim("p446", "zufälligen"), ("tabler", "cloud-storm", 110, WEISS), "zufälliger Untergang", WEISS)]),
    *paar("p930", "AN", [("p930", "ruhig")], "BR", [("p930", "ruhig"), ("p446", "denkt")]),
]))

# L Fall: der nächste Morgen (Übergabe) ---------------------------------------------------------------------------------------------------
AX3, RX3, BX3 = 520, 930, 1480
LOS = beim("faehrt", "Übergabe")
folie([("morgen", "Fall · Am nächsten Morgen"), ("gibt", "Fall · Die Übergabe"), ("faehrt", "Ergebnis · Herr Brunner ist Eigentümer")], [
    pl("Am nächsten Morgen", 70, 40, "morgen", fill=GELB, size=44),
    boden("morgen"),
    ficon("tabler", "building-cottage", 200, BODEN, 250, "morgen", fuell=GELB),
    ficon("tabler", "sun", 1660, 230, 110, "morgen", fuell=GELB),
    ficon("tabler", "fence", 1790, BODEN, 150, "morgen", fuell=WEISS),
    rad(RX3, "morgen", bis="gibt"),
    *fig("AN", AX3, BODEN, FH, [("morgen", "ruhig_r")], bis="an2"),
    *redet("AN_redet_r", AX3, BODEN, FH, "an2", "gibt"),
    *fig("AN", AX3, BODEN, FH, [("gibt", "froh_r")], erst="cut"),
    ns("Annika", AX3, BODEN, "morgen", AN_F),
    *fig("BR", BX3, BODEN, FH, [(beim("morgen", "Brunner"), "ruhig")], bis="br2"),
    *redet("BR_redet", BX3, BODEN, FH, "br2", "an2"),
    *fig("BR", BX3, BODEN, FH, [("an2", "froh")], erst="cut", bis=LOS),
    ns("Herr Brunner", BX3, BODEN, beim("morgen", "Brunner"), BR_F),
    blase("sprech", 560, 210, "br2", 1120, 220, inhalt=["Guten Morgen!", "Ich hole das Fahrrad ab."], textsize=34,
          figur=("BR_redet", BX3, BODEN, FH), bis="an2"),
    blase("sprech", 540, 210, "an2", 880, 220, inhalt=["Bitte schön.", "Jetzt gehört es Ihnen."], textsize=34,
          figur=("AN_redet_r", AX3, BODEN, FH), bis="gibt"),
    # das Rad wechselt zu Herrn Brunner
    bewegt(rad(BX3 - 330, "gibt", anim="cut", bis=LOS), "gibt", beim("gibt", "Rad", ende=True), RX3 - (BX3 - 330), 0),
    pl("Einigung und Übergabe", 800, 330, beim("gibt", "beide"), fill=GRUEN, size=32, anker="m"),
    szene(peep_voll("BR_rad", BX3 - 120, BODEN, 420, LOS, anim="cut"), "080klingel*", 0.8, 0.0),
    pl("Eigentümer: Herr Brunner", 1400, 370, LOS, fill=GRUEN, size=34, anker="m"),
])

# M Abwandlung: Eigentumsvorbehalt, § 449 ------------------------------------------------------------------------------------------------
folie([("abw", "Abwandlung · Eigentumsvorbehalt"), ("p449", "Abwandlung › § 449 Abs. 1 BGB")], rechts_frei([
    *tafel("abw", "Abwandlung: Eigentumsvorbehalt"),
    z("Rad sofort mitgenommen, Zahlung in Raten", 110, 190, "abw", "Bold", 36),
    z("Eigentum vorbehalten bis zur Zahlung", 160, 250, beim("abw", "behält"), size=36),
    z("§ 449 Abs. 1 BGB: Einigung im Zweifel", 110, 350, "p449", "Bold", 36),
    z("aufschiebend bedingt, § 158 Abs. 1 BGB", 160, 410, beim("p449", "aufschiebend"), size=36),
    blk(110, 510, 1040, 100, BLAU, "raten", [("Eigentum erst mit vollständiger Zahlung", "ExtraBold", 38, INK)]),
    *requisit([("abw", RAD, "sofort mitgenommen", WEISS),
               (beim("abw", "Raten"), ("tabler", "calendar-dollar", 100, WEISS), "in Raten", WEISS),
               (beim("abw", "behält"), ("tabler", "lock", 100, GELB), "Eigentum vorbehalten", GELB),
               ("raten", GELD, "vollständige Zahlung", GRUEN)]),
    *paar("abw", "AN", [("abw", "ruhig"), ("raten", "froh")], "BR", [("abw", "ruhig"), ("p449", "denkt")]),
]))

# N Klausurtipp (Lexi) -------------------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · Einigung und Übergabe getrennt")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Einigung und Übergabe getrennt prüfen", 200, 200, beim("tipp", "Prüfe"), "Bold", 38),
    z("auch wenn beides im selben Moment passiert", 200, 260, beim("tipp", "auch"), size=34),
    *neinz("Nie: „durch den Kaufvertrag Eigentümer“", 380, "tipp2", "Bold", 36),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# O Klausurschema ---------------------------------------------------------------------------------------------------------------------------
K1, K2 = 150, 230
folie([("sch", "Klausurschema"), ("k2", "Klausurschema › II. Übergabe"), ("k3", "Klausurschema › III. Einigsein"),
       ("k4", "Klausurschema › IV. Berechtigung")], [
    karte(60, 50, 1800, 900, "sch"),
    titel(glyphen("Klausurschema: Übereignung, § 929 Satz 1 BGB"), 110, 90, "sch", 46),
    z("I. Einigung", K1, 200, "k1", "Bold", 40, rechts=1820),
    z("dinglicher Vertrag über eine bestimmte Sache", K2, 255, beim("k1", "dinglicher"), size=36, rechts=1820),
    z("II. Übergabe", K1, 330, "k2", "Bold", 40, rechts=1820),
    z("Besitzerwerb des Erwerbers (§ 854 Abs. 1 BGB)", K2, 385, "k2b", size=36, rechts=1820),
    z("vollständiger Besitzverlust des Veräußerers", K2, 435, beim("k2b", "vollständiger"), size=36, rechts=1820),
    z("auf Veranlassung des Veräußerers", K2, 485, beim("k2b", "Veranlassung"), size=36, rechts=1820),
    z("III. Einigsein im Zeitpunkt der Übergabe", K1, 560, "k3", "Bold", 40, rechts=1820),
    z("IV. Berechtigung des Veräußerers", K1, 640, "k4", "Bold", 40, rechts=1820),
    z("sonst gutgläubiger Erwerb, §§ 932 ff. BGB", K2, 695, "k4b", size=36, rechts=1820),
])

# P Merksatz (Lexi) --------------------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Der Kaufvertrag ", 0), ("verpflichtet nur.", "a")]],
                750, 330, 46, "merke", {"a": beim("merke", "verpflichtet")}),
    *markertext([[("Eigentum geht erst mit", 0)], [("Einigung", "b"), (" und ", 0), ("Übergabe", "c"), (" über.", 0)]],
                750, 520, 46, "m2", {"b": beim("m2", "Einigung"), "c": beim("m2", "Übergabe")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
