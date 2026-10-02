"""Folge 083 · Gutgläubiger Erwerb §§ 932 ff. BGB: Eigentum vom Nichteigentümer? – Serienstandard Open Peeps (Katzenkönig).
Beispielfall: Erika leiht ihrem Freund Benno ihr Fahrrad für eine Woche; Benno verkauft es als seines für 200 € an Selma und
übergibt es; am Sonntag sieht Erika ihr Rad bei Selma.
Szenen laut ../SZENENPLAN.md: A1 Leihe (Garage), A2 Verkauf (Park), A3 Sonntag/Frage, B Sachverhalt, C § 985 und Wortlaut
§ 932 I 1, D sechs Prüfungspunkte, E I. Verkehrsgeschäft, F II. Einigung und Übergabe, G III. Nichtberechtigung,
H IV. Rechtsschein, I V. guter Glaube (Wortlaut § 932 II), J Beweislast, K VI. kein Abhandenkommen (Wortlaut § 935 I 1),
L Ergebnis, M Abwandlung gestohlenes Rad (§ 935 II), N §§ 933, 934, 936, O § 816 I 1, P Klausurtipp (Lexi),
Q Klausurschema, R Merksatz (Lexi).
Zwei Handlungsgeräusche (Geldscheine bei der Zahlung, Fahrradklingel, als Selma heranfährt; ../geraeusche_herkunft.json).
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/hand als
eigene Kopie aus Folge 080 (gemeinsame Dateien unverändert). Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_083/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_083/" in n:
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
EK_N, BE_N, SE_N = LILA, GRUEN, ORANGE      # Farben der Namensschilder
PX, PY, PU = 1570, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"EK": "Erika", "BE": "Benno", "SE": "Selma"}
NFARBE = {"EK": EK_N, "BE": BE_N, "SE": SE_N}


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
    """Tafelszene: zwei Figuren rechts der Tafel, beide blicken zur Tafel (nach links); l, r = Kürzel EK/BE/SE."""
    return [*fig(l, X1, FB, FR, lf), ns(NAME[l], X1, FB, c0, NFARBE[l], d=0.1),
            *fig(r, X2, FB, FR, rf, d=0.2), ns(NAME[r], X2, FB, c0, NFARBE[r], d=0.3)]


RAD = ("ph", "bicycle", 120, WEISS)
GELD = ("tabler", "cash-banknote", 110, GRUEN)


def rad(cx, cue, breite=300, bis=None, anim="pop", d=0.0):
    """Das Fahrrad von Erika (Phosphor bicycle, Räder weiß gefüllt), auf dem Boden."""
    return ficon("ph", "bicycle", cx, BODEN, breite, cue, fuell=WEISS, bis=bis, anim=anim, d=d)


# A1 Fall: die Leihe vor der Garage von Erika ----------------------------------------------------------------------------------
AX, RX, BX = 560, 950, 1480
RB = BX - 330                                        # Rad bei Benno
UEBER = (beim("er1", "Hier"), beim("er1", "Sonntag", ende=True))
folie([(NULL, "Fall · Die Leihe")], [
    hart(pl("Erika verleiht ihr Fahrrad an Benno", 70, 40, NULL, fill=GELB, size=44)),
    hart(boden(NULL)),
    hart(ficon("ph", "garage", 220, BODEN, 300, NULL, fuell=GELB)),
    hart(rad(RX, NULL, bis=UEBER[0])),
    bewegt(rad(RB, UEBER[0], anim="cut"), *UEBER, RX - RB, 0),
    ficon("tabler", "calendar-event", 950, 520, 80, beim("fall", "Woche"), fuell=WEISS),
    pl("für 1 Woche", 950, 530, beim("fall", "Woche"), fill=WEISS, size=30, anker="m"),
    # Erika (links, blickt zu Benno)
    *fig("EK", AX, BODEN, FH, [(NULL, "ruhig_r")], bis="er1", erst="cut"),
    *redet("EK_redet_r", AX, BODEN, FH, "er1", "be1"),
    *fig("EK", AX, BODEN, FH, [("be1", "froh_r")], erst="cut"),
    hart(ns("Erika", AX, BODEN, NULL, EK_N)),
    # Benno (rechts, blickt zu Erika)
    *fig("BE", BX, BODEN, FH, [(NULL, "ruhig")], bis="be1", erst="cut"),
    *redet("BE_redet", BX, BODEN, FH, "be1", "knapp"),
    hart(ns("Benno", BX, BODEN, NULL, BE_N)),
    blase("sprech", 720, 220, "er1", 800, 230, inhalt=["Hier, bis Sonntag.", "Pass gut darauf auf!"], textsize=34,
          figur=("EK_redet_r", AX, BODEN, FH), bis="be1"),
    blase("sprech", 700, 220, "be1", 1100, 230, inhalt=["Danke! Am Sonntag", "hast du es zurück."], textsize=34,
          figur=("BE_redet", BX, BODEN, FH), bis="knapp"),
])

# A2 Fall: der Verkauf im Park -----------------------------------------------------------------------------------------------------
BX2, RX2, SX = 520, 860, 1480
RS = SX - 330                                        # Rad bei Selma
BH2 = hand("BE_froh_r", BX2, BODEN, FH, +1)          # Hand von Benno (zu Selma hin)
SH2 = hand("SE_ruhig", SX, BODEN, FH, -1)            # Hand von Selma (zu Benno hin)
ZAHLT = (beim("zahlt", "zahlt"), beim("zahlt", "zahlt", ende=True))
GIBT = (beim("gibt", "Rad"), beim("gibt", "einig"))
folie([("knapp", "Fall · Der Verkauf"), ("zahlt", "Fall · Zahlung und Übergabe")], [
    pl("Der Verkauf", 70, 40, "knapp", fill=GELB, size=44),
    boden("knapp"),
    ficon("ph", "tree", 190, BODEN, 260, "knapp", fuell=GRUEN),
    ficon("tabler", "trees", 1800, BODEN, 150, "knapp", fuell=GRUEN),
    rad(RX2, "knapp", bis=GIBT[0]),
    bewegt(rad(RS, GIBT[0], anim="cut"), *GIBT, RX2 - RS, 0),
    ficon("ph", "wallet", 860, 560, 90, beim("knapp", "knapp"), fuell=WEISS, bis="zahlt"),
    pl("knapp bei Kasse", 860, 570, beim("knapp", "knapp"), fill=WEISS, size=30, anker="m", bis="zahlt"),
    pl("als seines ausgegeben", 860, 400, beim("selma", "seines"), fill=PINK, size=30, anker="m", bis="zahlt"),
    # Benno (links, blickt zu Selma)
    *fig("BE", BX2, BODEN, FH, [("knapp", "sorge_r"), (beim("selma", "Er"), "ruhig_r")], bis="be2", erst="cut"),
    *redet("BE_redet_r", BX2, BODEN, FH, "be2", "zahlt"),
    *fig("BE", BX2, BODEN, FH, [("zahlt", "froh_r")], erst="cut"),
    hart(ns("Benno", BX2, BODEN, "knapp", BE_N)),
    # Selma (rechts, blickt zu Benno)
    *fig("SE", SX, BODEN, FH, [(beim("selma", "Selma"), "ruhig"), (beim("gibt", "einig"), "froh")]),
    ns("Selma", SX, BODEN, beim("selma", "Selma"), SE_N),
    blase("sprech", 760, 220, "be2", 880, 230, inhalt=["Das ist mein Rad.", "Für 200 € gehört es dir."], textsize=34,
          figur=("BE_redet_r", BX2, BODEN, FH), bis="zahlt"),
    pl("kein Grund zu zweifeln", SX, 300, beim("zahlt", "Grund"), fill=WEISS, size=30, anker="m"),
    # das Geld: erst in der Hand von Selma, dann bei Benno
    ficon("tabler", "cash-banknote", SH2[0] - 40, SH2[1] + 20, 90, beim("zahlt", "Sie"), fuell=GRUEN, bis=ZAHLT[0]),
    szene(bewegt(ficon("tabler", "cash-banknote", BH2[0] + 40, BH2[1] + 20, 90, ZAHLT[0], fuell=GRUEN, anim="cut"),
                 *ZAHLT, (SH2[0] - 40) - (BH2[0] + 40), 0), "083geld*", 0.8, 0.0),
    pl("200 € bezahlt", 860, 470, beim("zahlt", "zahlt"), fill=GRUEN, size=32, anker="m"),
    pl("übergeben und einig", RS, 580, beim("gibt", "einig"), fill=GRUEN, size=30, anker="m"),
])

# A3 Fall: der Sonntag -------------------------------------------------------------------------------------------------------------
AX3, SX3, RX3 = 520, 1600, 1270
SR_X = 1430                                          # Selma auf dem Rad (Endposition)
folie([("sonntag", "Fall · Am Sonntag"), ("frage", "Fall · Die Frage")], [
    pl("Am Sonntag", 70, 40, "sonntag", fill=GELB, size=44, bis="frage"),
    boden("sonntag"),
    ficon("ph", "tree", 190, BODEN, 240, "sonntag", fuell=GRUEN),
    ficon("tabler", "sun", 1780, 200, 100, "sonntag", fuell=GELB),
    *fig("EK", AX3, BODEN, FH, [("sonntag", "ruhig_r"), (beim("sonntag", "Rad"), "denkt_r")], bis="er2", erst="cut"),
    *redet("EK_empoert_r", AX3, BODEN, FH, "er2", "frage"),
    *fig("EK", AX3, BODEN, FH, [("frage", "denkt_r")], erst="cut"),
    ns("Erika", AX3, BODEN, "sonntag", EK_N),
    # Selma fährt auf dem Rad heran, dann steht sie neben dem Rad
    szene(bewegt(peep_voll("SE_rad", SR_X, BODEN, 440, beim("sonntag", "Rad"), anim="cut", bis="er2"),
                 beim("sonntag", "Rad"), beim("sonntag", "darauf", ende=True), 230, 0), "083klingel*", 0.8, 0.0),
    ns("Selma", SR_X, BODEN, beim("sonntag", "Selma"), SE_N, bis="er2"),
    rad(RX3, "er2", anim="cut"),
    *fig("SE", SX3, BODEN, FH, [("er2", "ruhig")], bis="se1", erst="cut"),
    *redet("SE_redet", SX3, BODEN, FH, "se1", "frage"),
    *fig("SE", SX3, BODEN, FH, [("frage", "denkt")], erst="cut"),
    hart(ns("Selma", SX3, BODEN, "er2", SE_N)),
    blase("sprech", 720, 220, "er2", 820, 230, inhalt=["Das ist mein Fahrrad!", "Gib es mir zurück."], textsize=34,
          figur=("EK_empoert_r", AX3, BODEN, FH), bis="se1"),
    blase("sprech", 760, 220, "se1", 1160, 230, inhalt=["Nein, ich habe es gekauft.", "Es gehört mir."], textsize=34,
          figur=("SE_redet", SX3, BODEN, FH), bis="frage"),
    pl("Wer ist jetzt Eigentümerin?", 960, 40, "frage", fill=PINK, size=42, anker="m"),
    pl("Erika?", AX3, 290, beim("frage", "Erika"), fill=EK_N, size=32, anker="m"),
    pl("Selma?", SX3, 290, beim("frage", "Selma"), fill=SE_N, size=32, anker="m"),
    pl("Eigentum vom Nichteigentümer?", 960, 130, "frage2", fill=WEISS, size=38, anker="m"),
])


# B Sachverhalt ---------------------------------------------------------------------------------------------------------------
def sachverhalt_083(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=38, zeilenabstand=1.34)
        els += e; y += 26
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=38))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_083("sv", [
    "Erika leiht ihrem Freund Benno ihr Fahrrad für eine Woche, bis Sonntag. Benno ist knapp bei Kasse. Er bietet das Rad "
    "Selma für 200 Euro an und gibt es als sein eigenes aus.",
    "Selma hat keinen Grund zu zweifeln. Sie zahlt, Benno übergibt ihr das Rad, und beide sind sich einig, dass es Selma "
    "gehören soll. Erika hat den Verkauf nicht erlaubt.",
    "Am Sonntag sieht Erika ihr Rad bei Selma und verlangt es zurück.",
], "Ist Selma Eigentümerin geworden?")

# C Ausgangspunkt § 985 und Wortlaut § 932 Abs. 1 Satz 1 --------------------------------------------------------------------------
W932 = ["„Durch eine nach § 929 erfolgte Veräußerung wird der Erwerber auch",
        "dann Eigentümer, wenn die Sache nicht dem Veräußerer gehört, es sei",
        "denn, dass er zu der Zeit, zu der er nach diesen Vorschriften das",
        "Eigentum erwerben würde, nicht in gutem Glauben ist.“"]
w932, w932_y = wortlaut(80, 370, 1100, W932, "§ 932 Abs. 1 Satz 1 BGB", "p932", marken=[
    (1, "dann Eigentümer", beim("w932", "Eigentümer")), (1, "nicht dem Veräußerer gehört", beim("w932", "nicht")),
    (1, "es sei", beim("w932", "sei")), (3, "nicht in gutem Glauben", beim("w932", "gutem"))], size=32)
folie([("p985", "Ausgangspunkt · § 985 BGB"), ("p932", "Gutgläubiger Erwerb · § 932 Abs. 1 S. 1 BGB")], rechts_frei([
    *tafel("p985", "Eigentum vom Nichteigentümer?"),
    z("§ 985 BGB: Herausgabe, wenn Erika noch", 110, 190, "p985", "Bold", 36),
    z("Eigentümerin ist", 160, 242, beim("p985", "Eigentümerin"), "Bold", 36),
    *neinz("Benno durfte nicht übereignen", 300, "nb0", "Bold", 36, x=160),
    *w932,
    *requisit([("p985", RAD, "Herausgabe?", WEISS), ("nb0", ("tabler", "key-off", 100, GELB), "nicht berechtigt", WEISS),
               (beim("w932", "Eigentümer"), RAD, "Selma Eigentümerin?", GELB),
               (beim("w932", "gutem"), ("tabler", "shield-check", 110, GRUEN), "guter Glaube", GRUEN)]),
    *paar("p985", "EK", [("p985", "ruhig"), ("nb0", "denkt")], "SE", [("p985", "ruhig"), (beim("w932", "gutem"), "froh")]),
]))

# D sechs Prüfungspunkte ------------------------------------------------------------------------------------------------------------
PUNKTE = [("v1", "I. Rechtsgeschäft"), ("v2", "II. Einigung und Übergabe"), ("v3", "III. Nichtberechtigung"),
          ("v4", "IV. Rechtsschein"), ("v5", "V. guter Glaube"), ("v6", "VI. kein Abhandenkommen")]
folie([("sechs", "Gutgläubiger Erwerb › 6 Prüfungspunkte")], rechts_frei([
    *tafel("sechs", "Gutgläubiger Erwerb: 6 Punkte"),
    *[z(t, 160, 200 + 85 * i, c, "Bold", 40) for i, (c, t) in enumerate(PUNKTE)],
    *requisit([("sechs", ("tabler", "list-check", 110, WEISS), "6 Prüfungspunkte", WEISS)]),
    *paar("sechs", "BE", [("sechs", "ruhig")], "SE", [("sechs", "ruhig")]),
]))

# E I. Rechtsgeschäft: Verkehrsgeschäft ----------------------------------------------------------------------------------------------
folie([("rg", "Gutgläubiger Erwerb › I. Verkehrsgeschäft")], rechts_frei([
    *tafel("rg", "I. Rechtsgeschäft"),
    z("Verkehrsgeschäft", 110, 200, beim("rg", "Verkehrsgeschäft"), "Bold", 40),
    z("Veräußerer und Erwerber weder rechtlich", 160, 270, beim("rg", "Veräußerer"), size=36),
    z("noch wirtschaftlich identisch", 160, 322, beim("rg", "wirtschaftlich"), size=36),
    zit("BGH, Urt. v. 8.4.2015 – IV ZR 161/14, Rn. 12", 160, 380, beim("rg", "identisch")),
    *okz("Benno und Selma: 2 verschiedene Personen", 470, "rg2", "Bold", 36, x=160),
    *requisit([("rg", ("ph", "handshake", 120, WEISS), "Rechtsgeschäft", GELB),
               ("rg2", ("tabler", "arrows-exchange", 120, WEISS), "Verkehrsgeschäft", GRUEN)]),
    *paar("rg", "BE", [("rg", "ruhig"), ("rg2", "froh")], "SE", [("rg", "ruhig"), ("rg2", "froh")]),
]))

# F II. Einigung und Übergabe ---------------------------------------------------------------------------------------------------------
folie([("eu", "Gutgläubiger Erwerb › II. Einigung und Übergabe")], rechts_frei([
    *tafel("eu", "II. Einigung und Übergabe"),
    z("§ 929 Satz 1 BGB", 110, 200, beim("eu", "Paragraf"), "Bold", 40),
    zit("Mehr dazu im Video zur Übereignung", 160, 262, beim("eu", "Video"), size=28),
    *okz("einig: Das Rad soll Selma gehören", 350, beim("eu2", "einig"), "Bold", 36, x=160),
    *okz("Übergabe: Rad in ihre Hand", 420, beim("eu2", "Hand"), "Bold", 36, x=160),
    *requisit([("eu", ("ph", "handshake", 120, WEISS), "Einigung", GELB),
               (beim("eu2", "Hand"), RAD, "übergeben", GRUEN)]),
    *paar("eu", "BE", [("eu", "ruhig")], "SE", [("eu", "ruhig"), (beim("eu2", "Hand"), "froh")]),
]))

# G III. Nichtberechtigung --------------------------------------------------------------------------------------------------------------
folie([("nb", "Gutgläubiger Erwerb › III. Nichtberechtigung")], rechts_frei([
    *tafel("nb", "III. Nichtberechtigung"),
    z("Benno ist nicht berechtigt", 110, 200, beim("nb", "nicht"), "Bold", 40),
    z("Eigentümerin: Erika", 160, 270, beim("nb", "gehört"), size=36),
    z("keine Erlaubnis zum Verkauf (§ 185 BGB)", 160, 325, beim("nb", "erlaubt"), size=36),
    blk(110, 420, 1040, 100, GELB, "luecke", [("Guter Glaube schließt nur diese Lücke", "ExtraBold", 40, INK)]),
    *requisit([("nb", ("tabler", "key-off", 100, GELB), "nicht berechtigt", WEISS),
               ("luecke", ("tabler", "shield-check", 110, GRUEN), "nur diese Lücke", GELB)]),
    *paar("nb", "EK", [("nb", "ruhig"), (beim("nb", "erlaubt"), "sorge")], "BE", [("nb", "sorge")]),
]))

# H IV. Rechtsschein des Besitzes --------------------------------------------------------------------------------------------------------
folie([("rs", "Gutgläubiger Erwerb › IV. Rechtsschein des Besitzes")], rechts_frei([
    *tafel("rs", "IV. Rechtsschein"),
    z("Grundlage: der Besitz", 110, 200, beim("rs", "Besitz"), "Bold", 40),
    zit("vgl. BGH, Urt. v. 18.9.2020 – V ZR 8/19, Rn. 9", 160, 262, beim("rs", "Besitz")),
    z("Veräußerer kann dem Erwerber den Besitz", 110, 340, "bvm", size=36),
    z("verschaffen: Besitzverschaffungsmacht", 160, 392, beim("bvm", "Besitzverschaffungsmacht"), "Bold", 36),
    *okz("Benno hatte das Rad und hat es übergeben", 480, "rs2", "Bold", 36, x=160),
    *requisit([("rs", ("tabler", "hand-grab", 110, WEISS), "Besitz", BLAU),
               ("rs2", RAD, "Benno hatte das Rad", GRUEN)]),
    *paar("rs", "BE", [("rs", "ruhig")], "SE", [("rs", "ruhig")]),
]))

# I V. guter Glaube (Wortlaut § 932 Abs. 2) ----------------------------------------------------------------------------------------------
W932B = ["„Der Erwerber ist nicht in gutem Glauben, wenn ihm bekannt oder",
         "infolge grober Fahrlässigkeit unbekannt ist, dass die Sache nicht",
         "dem Veräußerer gehört.“"]
w932b, w932b_y = wortlaut(80, 180, 1100, W932B, "§ 932 Abs. 2 BGB", "w932b", marken=[
    (0, "bekannt", beim("w932b", "bekannt")), (1, "grober Fahrlässigkeit", beim("w932b", "grober"))], size=32)
folie([("gg", "Gutgläubiger Erwerb › V. guter Glaube"), ("grob", "V. guter Glaube › grobe Fahrlässigkeit"),
       ("zeit", "V. guter Glaube › Zeitpunkt")], rechts_frei([
    *tafel("gg", "V. Guter Glaube"),
    *w932b,
    z("grob fahrlässig: erforderliche Sorgfalt in", 110, w932b_y + 30, "grob", "Bold", 34),
    z("ungewöhnlich großem Maße verletzt, übersehen,", 160, w932b_y + 78, beim("grob", "ungewöhnlich"), size=34),
    z("was jedem hätte einleuchten müssen", 160, w932b_y + 126, beim("grob", "übersieht"), size=34),
    zit("BGH, Urt. v. 18.9.2020 – V ZR 8/19, Rn. 28", 160, w932b_y + 178, beim("grob", "übersieht")),
    *neinz("keine allgemeine Nachforschungspflicht", w932b_y + 240, beim("nachf", "Nachforschungspflicht"), "Bold", 34, x=160),
    zit("BGH, a. a. O., Rn. 29", 160, w932b_y + 290, beim("nachf", "Nachforschungspflicht")),
    z("maßgeblich: Zeitpunkt des Erwerbs (Übergabe)", 110, w932b_y + 350, "zeit", "Bold", 34),
    *requisit([("gg", ("tabler", "shield-check", 110, GRUEN), "guter Glaube", GRUEN),
               (beim("w932b", "bekannt"), ("ph", "eye", 110, WEISS), "Kenntnis?", WEISS),
               ("grob", ("tabler", "alert-triangle", 100, GELB), "grob fahrlässig?", WEISS),
               ("zeit", ("tabler", "calendar-event", 90, WEISS), "Zeitpunkt: Übergabe", WEISS)]),
    *paar("gg", "BE", [("gg", "ruhig")], "SE", [("gg", "ruhig"), ("nachf", "froh")]),
]))

# J Beweislast: „es sei denn“ ------------------------------------------------------------------------------------------------------------
folie([("bew", "V. guter Glaube › Beweislast")], rechts_frei([
    *tafel("bew", "Beweislast: „es sei denn“"),
    z("§ 932 Abs. 1 Satz 1 BGB: „…, es sei denn, …“", 110, 200, beim("bew", "es"), "Bold", 36),
    *neinz("Selma muss ihren guten Glauben nicht beweisen", 290, beim("bew2", "nicht"), "Bold", 34, x=160),
    *okz("Erika muss beweisen: Selma war bösgläubig", 360, beim("bew2", "Erwerb"), "Bold", 34, x=160),
    zit("BGH, Urt. v. 23.9.2022 – V ZR 148/21, Rn. 14", 160, 420, beim("bew2", "Bundesgerichtshof")),
    blk(110, 500, 1040, 100, GRUEN, "selma2", [("Selma ist in gutem Glauben", "ExtraBold", 40, INK)]),
    *requisit([("bew", ("ph", "scales", 120, WEISS), "Beweislast", GELB),
               ("selma2", ("tabler", "shield-check", 110, GRUEN), "gutgläubig", GRUEN)]),
    *paar("bew", "EK", [("bew", "ruhig"), (beim("bew2", "Erwerb"), "denkt")], "SE",
          [("bew", "ruhig"), ("selma2", "froh")]),
]))

# K VI. kein Abhandenkommen (Wortlaut § 935 Abs. 1 Satz 1) -------------------------------------------------------------------------------
W935 = ["„Der Erwerb des Eigentums auf Grund der §§ 932 bis 934 tritt nicht",
        "ein, wenn die Sache dem Eigentümer gestohlen worden, verloren",
        "gegangen oder sonst abhanden gekommen war.“"]
w935, w935_y = wortlaut(80, 180, 1100, W935, "§ 935 Abs. 1 Satz 1 BGB", "w935", marken=[
    (1, "gestohlen", beim("w935", "gestohlen")), (1, "verloren", beim("w935", "verloren")),
    (2, "abhanden gekommen", beim("w935", "abhanden"))], size=32)
folie([("ab", "Gutgläubiger Erwerb › VI. kein Abhandenkommen"), ("leihe", "VI. kein Abhandenkommen › Leihe")], rechts_frei([
    *tafel("ab", "VI. Kein Abhandenkommen"),
    *w935,
    z("abhanden: unfreiwilliger Besitzverlust", 110, w935_y + 30, "unfr", "Bold", 36),
    zit("BGH, Urt. v. 18.9.2020 – V ZR 8/19, Rn. 9", 160, w935_y + 85, beim("unfr", "unfreiwillig")),
    *okz("Erika hat das Rad freiwillig verliehen", w935_y + 160, "leihe", "Bold", 34, x=160),
    *okz("Benno hat es freiwillig weggegeben", w935_y + 220, beim("leihe", "Benno"), "Bold", 34, x=160),
    blk(110, w935_y + 290, 1040, 100, GRUEN, beim("leihe", "Kein"), [("Kein Abhandenkommen", "ExtraBold", 40, INK)]),
    *requisit([("ab", ("tabler", "lock-open", 90, GELB), "abhanden?", WEISS),
               ("leihe", RAD, "freiwillig verliehen", GRUEN)]),
    *paar("ab", "EK", [("ab", "ruhig"), (beim("leihe", "Kein"), "sorge")], "BE", [("ab", "ruhig")]),
]))

# L Ergebnis -------------------------------------------------------------------------------------------------------------------------------
folie([("erg", "Ergebnis · Selma ist Eigentümerin")], rechts_frei([
    *tafel("erg", "Ergebnis"),
    blk(110, 190, 1040, 100, GRUEN, "erg", [("Selma ist Eigentümerin geworden", "ExtraBold", 40, INK)]),
    z("§ 929 Satz 1 BGB i. V. m. § 932 BGB", 160, 330, beim("erg", "Paragraf"), "Bold", 36),
    *neinz("Erika kann das Rad von Selma nicht", 430, "erg2", "Bold", 36, x=160),
    z("herausverlangen (§ 985 BGB)", 160, 482, beim("erg2", "herausverlangen"), "Bold", 36),
    *requisit([("erg", RAD, "gehört Selma", GRUEN)]),
    *paar("erg", "EK", [("erg", "sorge")], "SE", [("erg", "froh")]),
]))

# M Abwandlung: gestohlenes Rad, § 935 Abs. 2 ----------------------------------------------------------------------------------------------
folie([("abw", "Abwandlung · gestohlenes Rad"), ("p935b", "Abwandlung › § 935 Abs. 2 BGB")], rechts_frei([
    *tafel("abw", "Abwandlung: gestohlenes Rad"),
    z("Ein Dieb stiehlt das Rad aus der Garage", 110, 190, "abw", "Bold", 36),
    z("von Erika und verkauft es an Selma", 160, 242, beim("abw", "verkauft"), size=36),
    z("Das Rad ist Erika abhandengekommen", 110, 330, "abw2", "Bold", 36),
    *neinz("Selma wird nicht Eigentümerin,", 400, beim("abw2", "Selma"), "Bold", 36, x=160),
    z("auch wenn sie gutgläubig ist", 160, 452, beim("abw2", "auch"), size=36),
    linienzug([(110, 535), (1150, 535)], "p935b", breite=3),
    z("Ausnahmen, § 935 Abs. 2 BGB: etwa Geld,", 110, 565, "p935b", "Bold", 36),
    z("Sachen aus öffentlicher Versteigerung", 160, 620, beim("p935b", "öffentlichen"), size=36),
    *requisit([("abw", ("ph", "garage", 140, GELB), "gestohlen", HELLROT),
               (beim("abw2", "Selma"), RAD, "Selma: nicht Eigentümerin", HELLROT),
               ("p935b", ("tabler", "cash-banknote", 110, GRUEN), "Geld", WEISS),
               (beim("p935b", "öffentlichen"), ("tabler", "gavel", 100, WEISS), "öffentliche Versteigerung", WEISS)]),
    *paar("abw", "EK", [("abw", "sorge"), (beim("abw2", "Selma"), "ruhig")], "SE", [("abw", "ruhig"), (beim("abw2", "Selma"), "sorge")]),
]))

# N §§ 933, 934, 936 ----------------------------------------------------------------------------------------------------------------------
folie([("p933", "Übergabeersatz · § 933 BGB"), ("p934", "Übergabeersatz · § 934 BGB"), ("p936", "Rechte Dritter · § 936 BGB")],
      rechts_frei([
    *tafel("p933", "Übergabe ersetzt?"),
    z("§ 933 BGB: Besitzkonstitut (§ 930 BGB)", 110, 190, beim("p933", "Besitzkonstitut"), "Bold", 36),
    z("Eigentum erst, wenn der Veräußerer übergibt", 160, 245, beim("p933", "erst"), size=34),
    z("§ 934 BGB: Abtretung (§ 931 BGB)", 110, 330, "p934", "Bold", 36),
    z("Veräußerer mittelbarer Besitzer: mit Abtretung", 160, 385, beim("p934", "wenn"), size=34),
    z("sonst: mit Besitzerwerb vom Dritten", 160, 435, beim("p934", "sonst"), size=34),
    linienzug([(110, 510), (1150, 510)], "p936", breite=3),
    z("§ 936 BGB: Rechte Dritter erlöschen,", 110, 540, "p936", "Bold", 36),
    z("etwa ein Pfandrecht, wenn der Erwerber", 160, 595, beim("p936", "etwa"), size=34),
    z("auch insoweit gutgläubig ist", 160, 645, beim("p936", "auch"), size=34),
    *requisit([("p933", ("ph", "handshake", 120, WEISS), "Besitzkonstitut", WEISS),
               ("p934", ("tabler", "file-certificate", 100, WEISS), "Abtretung", WEISS),
               ("p936", ("tabler", "link-off", 110, WEISS), "Recht erlischt", GELB)]),
    *paar("p933", "BE", [("p933", "ruhig")], "SE", [("p933", "ruhig"), ("p936", "denkt")]),
]))

# O Folgeanspruch: § 816 Abs. 1 Satz 1 ------------------------------------------------------------------------------------------------------
folie([("p816", "Erika gegen Benno · § 816 Abs. 1 S. 1 BGB")], rechts_frei([
    *tafel("p816", "Erika geht nicht leer aus"),
    z("§ 816 Abs. 1 Satz 1 BGB: Benno muss", 110, 200, beim("p816", "Paragraf"), "Bold", 36),
    z("herausgeben, was er durch die Verfügung erlangt hat", 160, 255, beim("p816", "herausgeben"), size=34),
    *okz("Erlös: 200 €", 340, beim("p816", "Erlös"), "Bold", 38, x=160),
    zit("vgl. BGH, Urt. v. 14.6.2013 – V ZR 108/12, Rn. 4", 160, 400, beim("p816", "Erlös")),
    zit("Mehr dazu im Video zum Bereicherungsrecht", 160, 460, beim("p816", "Mehr"), size=28),
    *requisit([("p816", ("ph", "scales", 120, WEISS), "§ 816 BGB", WEISS), (beim("p816", "Erlös"), GELD, "200 €", GRUEN)]),
    *paar("p816", "EK", [("p816", "ruhig"), (beim("p816", "Erlös"), "froh")], "BE", [("p816", "sorge")]),
]))

# P Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · Abhandenkommen immer prüfen")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Abhandenkommen immer prüfen,", 200, 200, beim("tipp", "Prüfe"), "Bold", 38),
    z("auch wenn der Erwerber gutgläubig ist", 200, 260, beim("tipp", "auch"), size=34),
    z("Frage nicht nach dem Erwerber, sondern:", 200, 370, "tipp2", "Bold", 36),
    z("Hat der Eigentümer oder sein Besitzmittler", 200, 430, beim("tipp2", "Eigentümer"), size=34),
    z("den Besitz freiwillig aus der Hand gegeben?", 200, 482, beim("tipp2", "freiwillig"), size=34),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# Q Klausurschema ---------------------------------------------------------------------------------------------------------------------------
K1, K2 = 150, 230
folie([("sch", "Klausurschema"), ("k3", "Klausurschema › III. Nichtberechtigung"), ("k5", "Klausurschema › V. guter Glaube"),
       ("k6", "Klausurschema › VI. kein Abhandenkommen")], [
    karte(60, 50, 1800, 900, "sch"),
    titel(glyphen("Klausurschema: § 929 Satz 1 BGB i. V. m. § 932 BGB"), 110, 90, "sch", 46),
    z("I. Rechtsgeschäft", K1, 200, "k1", "Bold", 40, rechts=1820),
    z("Verkehrsgeschäft", K2, 252, beim("k1", "Verkehrsgeschäft"), size=36, rechts=1820),
    z("II. Einigung und Übergabe", K1, 320, "k2", "Bold", 40, rechts=1820),
    z("III. Nichtberechtigung des Veräußerers", K1, 400, "k3", "Bold", 40, rechts=1820),
    z("IV. Rechtsschein des Besitzes", K1, 480, "k4", "Bold", 40, rechts=1820),
    z("V. guter Glaube, § 932 Abs. 2 BGB", K1, 560, "k5", "Bold", 40, rechts=1820),
    z("weder Kenntnis noch grob fahrlässige Unkenntnis", K2, 612, beim("k5", "weder"), size=36, rechts=1820),
    z("VI. kein Abhandenkommen, § 935 BGB", K1, 690, "k6", "Bold", 40, rechts=1820),
])

# R Merksatz (Lexi) --------------------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Der gute Glaube ersetzt nur", 0)], [("die fehlende ", 0), ("Berechtigung.", "a")]],
                750, 320, 46, "merke", {"a": beim("merke", "Berechtigung")}),
    *markertext([[("Bei ", 0), ("abhandengekommenen", "b"), (" Sachen", 0)], [("hilft er ", 0), ("grundsätzlich nicht.", "c")]],
                750, 560, 46, "m2", {"b": beim("m2", "abhandengekommenen"), "c": beim("m2", "grundsätzlich")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
