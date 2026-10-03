"""Folge 122 · Widerrufsrecht Fernabsatz §§ 312g, 355 BGB: 14 Tage und Ausnahmen – Serienstandard Open Peeps (Katzenkönig).
Beispielfall: Ilka bestellt im Onlineshop von Herrn Riemann Sneaker für 120 €, trägt sie einen Nachmittag draußen im Park
und widerruft per E-Mail; Herr Riemann will getragene Schuhe nicht zurücknehmen.
Szenen laut ../SZENENPLAN.md: A1 Bestellung (Wohnung), A2 Park, A3 Rücksendung (Wohnung), A4 Retourenannahme bei Herrn
Riemann, B Sachverhalt, C Aufbau, D I. 1. Verbrauchervertrag, E I. 2. Fernabsatzvertrag (Wortlaut § 312c Abs. 1),
F I. 3. Widerrufsrecht (Wortlaut § 312g Abs. 1), G1 Ausnahmen (Wortlaut § 312g Abs. 2 Nr. 1–3), G2 Subsumtion,
H II. 1. Erklärung, I II. 2. Frist (Zeitstrahl), J III. 1. Rückgewähr, K III. 2. Wertersatz (Wortlaut § 357a Abs. 1),
L Ergebnis, M Klausurtipp (Lexi), N Schema, O Merksatz (Lexi).
Zwei Handlungsgeräusche (Schritte im Park, Karton wird geöffnet; ../geraeusche_herkunft.json).
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/hand/okz/
neinz als eigene Kopie aus Folge 117 (gemeinsame Dateien unverändert); wortlaut() hier mit Fundstelle ≥ 26 px.
Zahlen auf Tafeln, Pillen und Blasen als Ziffern (Wortlautkarten wörtlich)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_122/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_122/" in n:
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
    els.append(z(quelle, tx, ty + len(zeilen) * lh + 4, cue, "Bold", max(26, size - 4), farbe=TEXT, rechts=x + w - 16, bis=bis))
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
X1, X2 = 1400, 1720                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
IL_N, RI_N = LILA, TUERKIS                  # Farben der Namensschilder
PX, PY, PU = 1560, 120, 340                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
HOLZ = (214, 160, 110, 255)
ERDE = (176, 132, 96, 255)                  # verschmutzte Sohle / Sneaker nach dem Park


def boden(cue, hart_=False):
    e = linienzug([(40, BODEN), (1880, BODEN)], cue, breite=7, farbe=INK)
    return hart(e) if hart_ else e


def requisit(folge, bis_ende=None):
    """Wechselndes Requisit über den Figuren: folge = [(cue, (set, icon, breite, fuell), pillentext, pillenfarbe)]."""
    els = []
    for i, (c, ic, txt, pf) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else bis_ende
        if ic:
            s_, n_, br, fu = ic
            els.append(ficon(s_, n_, PX, PU, br, c, fuell=fu, bis=b))
        if txt:
            els.append(pl(txt, PX, PY, c, fill=pf, size=30, anker="m", bis=b))
    return els


def paar(c0, il, ri, bis=None, il_bis=None, ri_bis=None):
    """Tafelszene: Ilka (links) und Herr Riemann (rechts) neben der Tafel, beide blicken zur Tafel (nach links)."""
    return [*fig("IL", X1, FB, FR, il, bis=il_bis or bis), ns("Ilka", X1, FB, c0, IL_N, d=0.1),
            *fig("RI", X2, FB, FR, ri, bis=ri_bis or bis, d=0.2), ns("Herr Riemann", X2, FB, c0, RI_N, d=0.3)]


# ===========================================================================================================================
# A1 Fall: Die Bestellung (Wohnung von Ilka)
# ===========================================================================================================================
IX = 1380                                   # Ilka in der Wohnung (blickt nach links zu Sofa und Tür)
TUERX, SOFAX = 250, 720


def wohnung(c0, hart_=True):
    els = [boden(c0, hart_),
           ficon("tabler", "door", TUERX, BODEN, 240, c0, fuell=WEISS, anim="cut" if hart_ else "pop"),
           ficon("tabler", "sofa", SOFAX, BODEN, 420, c0, fuell=BLAU, anim="cut" if hart_ else "pop")]
    return els


ih = hand("IL_ruhig", IX, BODEN, FH, -1)    # linke Hand (zur Tafel/Raum hin)
BEST = beim("fall", "Onlineshop")
folie([(NULL, "Fall · Die Bestellung"), ("liefer", "Fall · Das Paket kommt")], [
    *wohnung(NULL),
    hart(pl("4.9.2026: Ilka bestellt", 70, 30, NULL, fill=GELB, size=40)),
    ficon("tabler", "device-mobile", ih[0] - 10, ih[1] + 20, 70, BEST, fuell=WEISS),
    pl("Onlineshop von Herrn Riemann", 700, 150, BEST, fill=WEISS, size=34),
    ficon("ph", "sneaker", 1020, 430, 200, beim("fall", "Sneaker"), fuell=WEISS),
    pl("Sneaker: 120 €", 900, 250, beim("fall", "hundertzwanzig"), fill=GELB, size=34),
    ficon("tabler", "package", TUERX + 200, BODEN, 150, "liefer", fuell=HOLZ),
    pl("8.9.2026: Paket kommt", 110, 520, beim("liefer", "Paket"), fill=WEISS, size=34),
    *fig("IL", IX, BODEN, FH, [(NULL, "ruhig"), (beim("fall", "Sneaker"), "froh")], erst="cut", bis="il1"),
    hart(ns("Ilka", IX, BODEN, NULL, IL_N)),
    *redet("IL_redet", IX, BODEN, FH, "il1", "park"),
    blase("sprech", 560, 170, "il1", 1020, 640, inhalt=["Die passen perfekt."], textsize=40,
          figur=("IL_redet", IX, BODEN, FH)),
])

# ===========================================================================================================================
# A2 Fall: Ein Nachmittag im Park
# ===========================================================================================================================
PW0, PW1 = 640, 1060                        # Ilka geht von links nach rechts durch den Park
GEHT = beim("park", "trägt")
GEHT_DA = ("park", round(GEHT[1] + 2.6, 3))
folie([("park", "Fall · Ein Nachmittag im Park"), ("sohle", "Fall · Die Sohlen")], [
    boden("park"),
    ficon("tabler", "trees", 300, BODEN, 380, "park", fuell=GRUEN),
    ficon("tabler", "tree", 1640, BODEN, 300, "park", fuell=GRUEN),
    ficon("tabler", "sun", 1330, 300, 150, "park", fuell=GELB),
    pl("12.9.2026: ein Nachmittag draußen im Park", 70, 30, beim("park", "Am"), fill=GELB, size=40),
    szene(bewegt(peep_voll("IL_froh_r", PW1, BODEN, FH, "park", anim="cut", bis="sohle"), GEHT, GEHT_DA, PW0 - PW1, 0),
          "122schritte*", 0.55),
    bewegt(ns("Ilka", PW1, BODEN, "park", IL_N), GEHT, GEHT_DA, PW0 - PW1, 0),
    *fig("IL", PW1, BODEN, FH, [("sohle", "sorge_r"), ("gef", "denkt_r")], erst="cut"),
    ficon("ph", "footprints", 760, BODEN - 4, 130, "sohle", fuell=ERDE),
    ficon("ph", "sneaker", 1360, BODEN - 2, 170, beim("sohle", "Sohlen"), fuell=ERDE),
    pl("Sohlen verschmutzt", 1230, 620, beim("sohle", "verschmutzt"), fill=ROT, size=34),
    pl("gefallen ihr doch nicht", 1180, 300 + 60, "gef", fill=WEISS, size=34),
])

# ===========================================================================================================================
# A3 Fall: Widerruf und Rücksendung (zurück in der Wohnung)
# ===========================================================================================================================
SCHICKT = beim("zurueck", "schickt")
MAIL = beim("zurueck", "E-Mail")
ib = hand("IL_bestimmt", IX, BODEN, FH, -1)
folie([("zurueck", "Fall · Der Widerruf")], [
    *wohnung("zurueck", hart_=False),
    pl("15.9.2026: Ilka schickt die Sneaker zurück", 70, 30, beim("zurueck", "Am"), fill=GELB, size=40),
    ficon("tabler", "package-export", TUERX + 200, BODEN, 150, SCHICKT, fuell=HOLZ),
    ficon("tabler", "device-mobile", ib[0] - 10, ib[1] + 20, 70, MAIL, fuell=WEISS),
    ficon("tabler", "mail", ib[0] - 10, ib[1] - 70, 80, MAIL, fuell=WEISS),
    pl("E-Mail an Herrn Riemann", 700, 150, MAIL, fill=WEISS, size=34),
    *fig("IL", IX, BODEN, FH, [("zurueck", "bestimmt")], erst="pop", bis="il2"),
    ns("Ilka", IX, BODEN, "zurueck", IL_N, d=0.1),
    *redet("IL_bestimmt", IX, BODEN, FH, "il2", "ri"),
    blase("sprech", 640, 270, "il2", 1000, 330, inhalt=["Ich widerrufe den Kauf.", "Bitte erstatten Sie mir", "die 120 €."],
          textsize=38, figur=("IL_bestimmt", IX, BODEN, FH)),
])

# ===========================================================================================================================
# A4 Fall: Retourenannahme bei Herrn Riemann
# ===========================================================================================================================
RX = 1420
TISCHX = 820
tisch = ficon("tabler", "desk", TISCHX, BODEN - 2, 460, "ri", fuell=HOLZ)
TT = int(tisch.y) + 8
AUS = beim("ri", "aus")
SPUR = beim("spur", "Spuren")
folie([("ri", "Fall · Herr Riemann packt aus"), ("ri1", "Fall · Getragen zurück?"), ("frage", "Fall · Die Frage")], [
    boden("ri"), tisch,
    pl("Herr Riemann packt das Paket aus", 70, 30, "ri", fill=GELB, size=40),
    szene(ficon("tabler", "package", TISCHX - 110, TT + 4, 150, beim("ri", "packt"), fuell=HOLZ), "122karton*", 0.8),
    ficon("ph", "sneaker", TISCHX + 100, TT + 2, 170, AUS, fuell=ERDE),
    ficon("tabler", "zoom", TISCHX + 140, TT - 70, 110, SPUR, fuell=WEISS),
    bis_(pl("Spuren an den Sohlen", 330, 300, SPUR, fill=ROT, size=34), "ri1"),
    *fig("RI", RX, BODEN, FH, [("ri", "ruhig"), (SPUR, "staunt")], erst="pop", bis="ri1"),
    ns("Herr Riemann", RX, BODEN, "ri", RI_N, d=0.1),
    *redet("RI_redet", RX, BODEN, FH, "ri1", "wert"),
    blase("sprech", 700, 280, "ri1", 1000, 240, inhalt=["Die sind ja getragen!", "Getragene Schuhe", "nehme ich nicht zurück."],
          textsize=38, figur=("RI_redet", RX, BODEN, FH), bis="wert"),
    *fig("RI", RX, BODEN, FH, [("wert", "ernst"), ("frage", "denkt")], erst="cut"),
    pl("mit den Spuren: nur noch 80 € wert", 110, 160, "wert", fill=GELB, size=34),
    ficon("tabler", "coin-euro", TISCHX + 100, TT - 200, 90, beim("wert", "achtzig"), fuell=GELB),
    pl("Kann Ilka trotzdem widerrufen?", 110, 260, "frage", fill=PINK, size=36),
    pl("Muss sie für das Tragen bezahlen?", 110, 350, "frage2", fill=PINK, size=36),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_122(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 56)]
    y = 205
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=35, zeilenabstand=1.30)
        els += e; y += 14
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=36))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_122("sv", [
    "Ilka bestellt am 4.9.2026 privat im Onlineshop von Herrn Riemann, der den Shop gewerblich betreibt, ein Paar "
    "Sneaker für 120 Euro und zahlt sofort. Versand und Rückversand sind kostenlos. Herr Riemann hat ordnungsgemäß über "
    "das Widerrufsrecht belehrt.",
    "Am 8.9.2026 erhält Ilka die Sneaker. Am 12.9.2026 trägt sie sie einen ganzen Nachmittag draußen im Park; danach "
    "sind die Sohlen verschmutzt.",
    "Am 15.9.2026 schickt sie die Sneaker zurück und schreibt Herrn Riemann per E-Mail: „Ich widerrufe den Kauf. Bitte "
    "erstatten Sie mir die 120 Euro.“ Herr Riemann meint: „Getragene Schuhe nehme ich nicht zurück.“ Mit den Spuren "
    "sind die Sneaker nur noch 80 Euro wert.",
], "Kann Ilka widerrufen? Und muss sie für das Tragen zahlen?")

# ===========================================================================================================================
# C Aufbau
# ===========================================================================================================================
folie([("plan", "Widerruf › Aufbau in drei Schritten")], rechts_frei([
    *tafel("plan", "Der Widerruf in drei Schritten"),
    blk(110, 200, 1040, 150, BLAU, "p1", [("I. Widerrufsrecht", "ExtraBold", 42, INK),
                                          ("Besteht ein Widerrufsrecht?", "Bold", 34, INK)]),
    blk(110, 390, 1040, 150, GELB, "p2", [("II. Ausübung", "ExtraBold", 42, INK),
                                          ("Wurde es wirksam ausgeübt?", "Bold", 34, INK)]),
    blk(110, 580, 1040, 110, GRUEN, "p3", [("III. Rechtsfolgen", "ExtraBold", 42, INK)]),
    *requisit([("plan", ("ph", "sneaker", 150, ERDE), "getragen zurück?", WEISS),
               ("p3", ("tabler", "coin-euro", 100, GELB), "Rechtsfolgen", GRUEN)]),
    *paar("plan", [("plan", "ruhig"), ("p1", "denkt")], [("plan", "ernst"), ("p3", "denkt")]),
]))

# ===========================================================================================================================
# D I. 1. Verbrauchervertrag
# ===========================================================================================================================
folie([("v1", "I. Widerrufsrecht › 1. Verbrauchervertrag, § 310 Abs. 3 BGB")], rechts_frei([
    *tafel("v1", "I. 1. Verbrauchervertrag"),
    z("Vertrag zwischen einem Unternehmer", 110, 190, beim("v1", "Vertrag"), "Bold", 38),
    z("und einem Verbraucher", 110, 245, beim("v1", "Vertrag"), "Bold", 38),
    zit("§ 310 Abs. 3 BGB", 110, 305, beim("v1", "Paragraf")),
    *okz("Ilka kauft privat", 390, beim("v2", "Ilka"), "Bold", 36, x=160),
    zit("Verbraucherin, § 13 BGB", 560, 400, beim("v2", "privat")),
    *okz("Herr Riemann betreibt den Shop gewerblich", 470, beim("v2", "Herr"), "Bold", 36, x=160),
    zit("Unternehmer, § 14 Abs. 1 BGB", 160, 525, beim("v2", "gewerblich")),
    blk(110, 640, 1040, 100, GELB, "v106", [("Mehr dazu: Video zum Verbraucherbegriff", "Bold", 36, INK)]),
    *requisit([("v1", ("tabler", "building-store", 110, GELB), "Unternehmer und Verbraucher", WEISS)]),
    *paar("v1", [("v1", "ruhig"), ("v2", "froh")], [("v1", "ruhig"), (beim("v2", "Herr"), "ernst")]),
]))

# ===========================================================================================================================
# E I. 2. Fernabsatzvertrag, § 312c Abs. 1 BGB (Wortlautkarte)
# ===========================================================================================================================
W312C = ["„Fernabsatzverträge sind Verträge, bei denen der Unternehmer oder eine in",
         "seinem Namen oder Auftrag handelnde Person und der Verbraucher für die",
         "Vertragsverhandlungen und den Vertragsschluss ausschließlich",
         "Fernkommunikationsmittel verwenden, es sei denn, dass der Vertragsschluss",
         "nicht im Rahmen eines für den Fernabsatz organisierten Vertriebs- oder",
         "Dienstleistungssystems erfolgt.“"]
w312c, w312c_y = wortlaut(110, 175, 1040, W312C, "§ 312c Abs. 1 BGB", "fa1", marken=[
    (2, "ausschließlich", beim("fa2", "ausschließlich")),
    (3, "Fernkommunikationsmittel", beim("fa2", "Fernkommunikationsmittel")),
    (4, "für den Fernabsatz organisierten Vertriebs- oder", beim("fa3", "organisierten")),
    (5, "Dienstleistungssystems", beim("fa3", "organisierten"))], size=28)
assert w312c_y <= 560, w312c_y
folie([("fa1", "I. 2. Fernabsatzvertrag, § 312c Abs. 1 BGB"), ("fa4", "I. 2. Fernabsatzvertrag › Onlineshop")], rechts_frei([
    *tafel("fa1", "I. 2. Fernabsatzvertrag"),
    *w312c,
    *okz("Onlineshop: ein solches System", 600, beim("fa4", "Onlineshop"), "Bold", 36, x=160),
    *okz("Ilka hat nur über die Website bestellt", 680, beim("fa4", "Website"), "Bold", 36, x=160),
    *requisit([("fa1", ("tabler", "device-mobile", 90, WEISS), "ausschließlich aus der Ferne", WEISS),
               ("fa4", ("tabler", "browser", 110, WEISS), "Onlineshop", GELB)]),
    *paar("fa1", [("fa1", "ruhig"), ("fa2", "denkt"), ("fa4", "froh")], [("fa1", "ruhig"), ("fa4", "ernst")]),
]))

# ===========================================================================================================================
# F I. 3. Widerrufsrecht, § 312g Abs. 1 BGB (Wortlautkarte)
# ===========================================================================================================================
W312G = ["„Dem Verbraucher steht bei außerhalb von Geschäftsräumen geschlossenen",
         "Verträgen und bei Fernabsatzverträgen ein Widerrufsrecht gemäß § 355 zu.“"]
w312g, w312g_y = wortlaut(110, 200, 1040, W312G, "§ 312g Abs. 1 BGB", beim("wr1", "Paragraf"), marken=[
    (1, "bei Fernabsatzverträgen", beim("wr1", "Fernabsatzverträgen")),
    (1, "ein Widerrufsrecht gemäß § 355", beim("wr1", "Widerrufsrecht", nr=2))], size=28)
folie([("wr1", "I. 3. Widerrufsrecht, § 312g Abs. 1 BGB")], rechts_frei([
    *tafel("wr1", "I. 3. Widerrufsrecht"),
    *w312g,
    z("Fernabsatzvertrag", 160, w312g_y + 70, beim("wr1", "Fernabsatzverträgen"), "ExtraBold", 40),
    pfeil(560, w312g_y + 96, 680, w312g_y + 96, beim("wr1", "Widerrufsrecht", nr=2), breite=7, kopf=22, farbe=INK),
    z("Widerrufsrecht", 710, w312g_y + 70, beim("wr1", "Widerrufsrecht", nr=2), "ExtraBold", 40),
    zit("Ausübung und Folgen: §§ 355 ff. BGB", 710, w312g_y + 130, beim("wr1", "Paragraf", nr=2)),
    *requisit([("wr1", ("tabler", "arrow-back-up", 100, WEISS), "Widerrufsrecht", GRUEN)]),
    *paar("wr1", [("wr1", "ruhig"), (beim("wr1", "Widerrufsrecht", nr=2), "froh")], [("wr1", "denkt")]),
]))

# ===========================================================================================================================
# G1 Ausnahmen, § 312g Abs. 2 Nr. 1–3 BGB (Wortlaut-Auswahl)
# ===========================================================================================================================
N1 = ["„1. Verträge zur Lieferung von Waren, die nicht vorgefertigt sind und für",
      "deren Herstellung eine individuelle Auswahl oder Bestimmung durch den",
      "Verbraucher maßgeblich ist oder die eindeutig auf die persönlichen",
      "Bedürfnisse des Verbrauchers zugeschnitten sind,“"]
N2 = ["„2. Verträge zur Lieferung von Waren, die schnell verderben können oder",
      "deren Verfallsdatum schnell überschritten würde,“"]
N3 = ["„3. Verträge zur Lieferung versiegelter Waren, die aus Gründen des",
      "Gesundheitsschutzes oder der Hygiene nicht zur Rückgabe geeignet sind,",
      "wenn ihre Versiegelung nach der Lieferung entfernt wurde,“"]
n1, y1 = wortlaut(110, 165, 1040, N1, "§ 312g Abs. 2 Nr. 1 BGB", "au2", marken=[
    (0, "nicht vorgefertigt", beim("au2", "vorgefertigt")),
    (3, "Bedürfnisse des Verbrauchers zugeschnitten", beim("au2", "Schuhe"))], size=28)
n2, y2 = wortlaut(110, y1 + 18, 1040, N2, "§ 312g Abs. 2 Nr. 2 BGB", "au3", marken=[
    (0, "schnell verderben können", beim("au3", "verderben"))], size=28)
n3, y3 = wortlaut(110, y2 + 18, 1040, N3, "§ 312g Abs. 2 Nr. 3 BGB", "au4", marken=[
    (0, "versiegelter Waren", beim("au4", "versiegelte")),
    (2, "Versiegelung nach der Lieferung entfernt", beim("au4", "Versiegelung"))], size=28)
assert y3 <= 830, y3
EUGH = "eugh"
folie([("au1", "I. 3. Widerrufsrecht › Ausnahmen, § 312g Abs. 2 BGB"), ("au2", "Ausnahmen › Nr. 1: nicht vorgefertigt"),
       ("au3", "Ausnahmen › Nr. 2: schnell verderblich"), ("au4", "Ausnahmen › Nr. 3: versiegelte Hygieneware")],
      rechts_frei([
    *tafel("au1", "Ausnahmen, § 312g Abs. 2 BGB (Auswahl)"),
    bis_(z("drei sind beim Onlinekauf wichtig:", 110, 175, beim("au1", "drei"), "Bold", 36), "au2"),
    *n1, *n2, *n3,
    zit("EuGH, Urt. v. 27.3.2019 – C-681/17, Rn. 34, 40, 41 (zu Art. 16 Buchst. e RL 2011/83/EU)", 110, y3 + 12,
        beim(EUGH, "Europäische")),
    *requisit([("au1", ("tabler", "list-numbers", 100, WEISS), "Ausnahmen", WEISS),
               ("au2", ("tabler", "ruler-measure", 110, GELB), "z. B. Schuhe nach Maß", GELB),
               ("au3", ("tabler", "fish", 110, BLAU), "z. B. frischer Fisch", BLAU),
               ("au4", ("ph", "seal-check", 110, GRUEN), "versiegelt", GRUEN),
               (EUGH, ("tabler", "bed", 120, LILA), "EuGH: eng auslegen", LILA)]),
    pl("Matratze ohne Schutzfolie:", PX, 360, beim(EUGH, "Matratze"), fill=WEISS, size=30, anker="m"),
    pl("keine Ausnahme", PX, 430, beim(EUGH, "nicht"), fill=ROT, size=30, anker="m"),
    *paar("au1", [("au1", "ruhig"), ("au2", "denkt"), (EUGH, "froh")], [("au1", "denkt"), (EUGH, "staunt")]),
]))

# ===========================================================================================================================
# G2 Ausnahmen: Subsumtion
# ===========================================================================================================================
folie([("au5", "Ausnahmen › Subsumtion"), ("au6", "I. 3. Widerrufsrecht › keine Ausnahme")], rechts_frei([
    *tafel("au5", "Ausnahmen für die Sneaker?"),
    *neinz("Nr. 1: Die Sneaker sind Serienware.", 200, beim("au5", "Serienware"), "Bold", 38, x=160),
    *neinz("Nr. 2: Sie verderben nicht.", 290, beim("au5", "verderben"), "Bold", 38, x=160),
    *neinz("Nr. 3: Sie waren nicht versiegelt.", 380, beim("au5", "versiegelt"), "Bold", 38, x=160),
    dicon("ph", "sneaker", 960, 600, 240, beim("au5", "Serienware"), fuell=ERDE),
    z("Keine Ausnahme greift.", 110, 540, "au6", "ExtraBold", 40),
    blk(110, 640, 1040, 100, GRUEN, beim("au6", "Ilka"), [("Ilka hat ein Widerrufsrecht.", "ExtraBold", 40, INK)]),
    *requisit([("au5", ("ph", "sneaker", 150, ERDE), "Serienware", WEISS),
               ("au6", ("tabler", "arrow-back-up", 100, GRUEN), "Widerrufsrecht", GRUEN)]),
    *paar("au5", [("au5", "denkt"), ("au6", "froh")], [("au5", "ernst"), ("au6", "denkt")]),
]))

# ===========================================================================================================================
# H II. 1. Erklärung, § 355 Abs. 1 BGB
# ===========================================================================================================================
folie([("e1", "II. Ausübung › 1. Erklärung, § 355 Abs. 1 BGB"), ("e4", "II. 1. Erklärung › Rücksendung allein?"),
       ("e6", "II. 1. Erklärung › Widerrufsfunktion, § 356a BGB")], rechts_frei([
    *tafel("e1", "II. 1. Erklärung"),
    z("gegenüber dem Unternehmer", 110, 180, beim("e1", "Erklärung"), "Bold", 36),
    zit("§ 355 Abs. 1 Satz 2 BGB", 640, 190, beim("e1", "Paragraf")),
    z("Entschluss zum Widerruf: eindeutig", 110, 250, "e2", "Bold", 36),
    zit("Satz 3", 780, 260, beim("e2", "eindeutig")),
    z("keine Begründung nötig", 110, 320, "e3", "Bold", 36),
    zit("Satz 4", 560, 330, "e3"),
    *neinz("kommentarlos zurückschicken", 410, "e4", "Bold", 36, x=160),
    zit("Gesetzesbegründung, BT-Drs. 17/12637, S. 60", 160, 462, beim("e4", "Gesetzesbegründung")),
    *okz("Zettel mit eindeutiger Erklärung im Paket", 520, "e5", "Bold", 36, x=160),
    z("Onlineshops: Widerrufsfunktion anbieten", 110, 610, "e6", "Bold", 36),
    zit("§ 356a Abs. 1 BGB", 110, 662, beim("e6", "Paragraf")),
    blk(110, 730, 1040, 120, GRUEN, "e7", [("E-Mail von Ilka: „Ich widerrufe den Kauf.“", "Bold", 34, INK),
                                          ("eindeutig", "ExtraBold", 36, INK)]),
    *requisit([("e1", ("tabler", "mail", 100, WEISS), "Erklärung", WEISS),
               ("e4", ("tabler", "package-export", 110, HOLZ), "nur zurückschicken?", ROT),
               ("e5", ("tabler", "file-text", 100, WEISS), "Zettel im Paket", GRUEN),
               ("e6", ("tabler", "click", 100, WEISS), "Widerrufsfunktion", WEISS),
               ("e7", ("tabler", "mail-check", 100, GRUEN), "eindeutig", GRUEN)]),
    *paar("e1", [("e1", "ruhig"), ("e4", "denkt"), ("e7", "froh")], [("e1", "ruhig"), ("e4", "denkt"), ("e7", "ernst")]),
]))

# ===========================================================================================================================
# I II. 2. Frist (Zeitstrahl September 2026)
# ===========================================================================================================================
T0, T1, TY = 170, 1060, 500                 # Zeitstrahl 7. bis 23. September
tag = lambda d: T0 + (d - 7) / 16 * (T1 - T0)
F4 = "fr4"
ERH = beim("fr4", "achten")
ENDE = beim("fr4", "zweiundzwanzigsten")
ABS = beim("fr5", "fünfzehnten")
strahl = [linienzug([(T0 - 20, TY), (T1 + 20, TY)], F4, breite=5)]
for d_ in range(7, 24):
    gross = d_ in (8, 15, 22)
    strahl.append(linienzug([(tag(d_), TY - (12 if gross else 7)), (tag(d_), TY + (12 if gross else 7))], F4,
                            breite=5 if gross else 3))
for d_, txt, c in [(8, "8.9.", ERH), (15, "15.9.", ABS), (22, "22.9.", ENDE)]:
    strahl.append(z(txt, tag(d_) - F("Bold", 28).getlength(txt) / 2, TY + 22, c, "Bold", 28, farbe=TEXT))
folie([("fr1", "II. 2. Frist, § 355 Abs. 2 BGB"), ("fr2", "II. 2. Frist › Beginn, § 356 Abs. 2, 3 BGB"),
       ("fr6", "II. 2. Frist › ohne Belehrung, § 356 Abs. 4 BGB")], rechts_frei([
    *tafel("fr1", "II. 2. Frist"),
    z("14 Tage", 110, 175, beim("fr1", "vierzehn"), "ExtraBold", 38),
    zit("§ 355 Abs. 2 Satz 1 BGB", 300, 186, beim("fr1", "Paragraf")),
    z("Beginn: wenn der Verbraucher die Ware erhalten hat", 110, 240, beim("fr2", "beginnt"), "Bold", 34),
    zit("§ 356 Abs. 2 Nr. 1 Buchst. a BGB", 110, 290, beim("fr2", "Paragraf")),
    z("nicht vor ordnungsgemäßer Belehrung", 110, 340, "fr3", "Bold", 34),
    zit("§ 356 Abs. 3 Satz 1 BGB", 740, 350, beim("fr3", "Absatz")),
    *strahl,
    blk(int(tag(8)), TY - 62, int(tag(22) - tag(8)), 46, GELB, ENDE, [("14 Tage", "ExtraBold", 28, INK)], anim="pop"),
    pl("Erhalt", tag(8) - 50, TY + 66, ERH, fill=GELB, size=28),
    pl("E-Mail", tag(15) - 55, TY + 66, ABS, fill=GRUEN, size=28),
    pl("Fristende", tag(22) - 150, TY + 66, beim("fr4", "endet"), fill=ROT, size=28),
    *okz("rechtzeitig, die Absendung genügt", 640, beim("fr5", "rechtzeitig"), "Bold", 34, x=160),
    zit("§ 355 Abs. 1 Satz 5 BGB", 760, 650, beim("fr5", "Absendung")),
    z("Ohne Belehrung: erlischt spätestens", 110, 710, "fr6", "Bold", 34),
    z("12 Monate und 14 Tage nach dem Erhalt", 110, 758, beim("fr6", "zwölf"), "Bold", 34),
    zit("§ 356 Abs. 4 Satz 1 BGB", 110, 812, beim("fr6", "Paragraf")),
    pl("hier: 22.9.2027", 800, 750, "fr7", fill=ROT, size=32),
    *requisit([("fr1", ("tabler", "calendar-due", 100, GELB), "14 Tage", GELB),
               ("fr117", ("tabler", "calendar-due", 100, WEISS), "Video: Klausurfehler", WEISS),
               ("fr6", ("tabler", "hourglass", 100, WEISS), "ohne Belehrung", ROT)]),
    *paar("fr1", [("fr1", "ruhig"), ("fr2", "denkt"), ("fr5", "froh")], [("fr1", "ruhig"), ("fr6", "denkt")]),
]))

# ===========================================================================================================================
# J III. 1. Rückgewähr
# ===========================================================================================================================
folie([("rf1", "III. Rechtsfolgen › 1. Rückgewähr, §§ 355 Abs. 3, 357 BGB")], rechts_frei([
    *tafel("rf1", "III. 1. Rückgewähr"),
    z("Die empfangenen Leistungen sind", 110, 185, beim("rf1", "Die"), "Bold", 36),
    z("zurückzugewähren, spätestens nach 14 Tagen.", 110, 238, beim("rf1", "spätestens"), "Bold", 36),
    zit("§ 355 Abs. 3 Satz 1, § 357 Abs. 1 BGB", 110, 295, beim("rf1", "Paragrafen")),
    pl("Ilka", 140, 430, beim("rf1", "Die"), fill=LILA, size=36),
    pl("Herr Riemann", 820, 430, beim("rf1", "Die"), fill=TUERKIS, size=36),
    dicon("ph", "sneaker", 560, 470, 130, beim("rf1", "zurückzugewähren"), fuell=ERDE),
    pfeil(300, 500, 790, 500, beim("rf1", "zurückzugewähren"), breite=7, kopf=22, farbe=INK),
    pfeil(790, 610, 300, 610, "rf2", breite=7, kopf=22, farbe=INK),
    pl("120 €", 490, 630, "rf2", fill=GELB, size=34),
    *okz("Herr Riemann muss die 120 € erstatten.", 740, beim("rf2", "Herr"), "Bold", 36, x=160),
    *requisit([("rf1", ("tabler", "arrow-back-up", 100, WEISS), "zurückgewähren", WEISS),
               ("rf2", ("tabler", "coin-euro", 100, GELB), "120 € zurück", GELB)]),
    *paar("rf1", [("rf1", "ruhig"), ("rf2", "froh")], [("rf1", "ruhig"), ("rf2", "ernst")]),
]))

# ===========================================================================================================================
# K III. 2. Wertersatz, § 357a Abs. 1 BGB (Wortlautkarte)
# ===========================================================================================================================
W357A = ["„Der Verbraucher hat Wertersatz für einen Wertverlust der Ware zu leisten,",
         "wenn 1. der Wertverlust auf einen Umgang mit den Waren zurückzuführen ist,",
         "der zur Prüfung der Beschaffenheit, der Eigenschaften und der",
         "Funktionsweise der Waren nicht notwendig war, und 2. der Unternehmer den",
         "Verbraucher nach Artikel 246a § 1 Absatz 2 Satz 1 Nummer 1 des",
         "Einführungsgesetzes zum Bürgerlichen Gesetzbuche über dessen",
         "Widerrufsrecht unterrichtet hat.“"]
w357, w357_y = wortlaut(110, 165, 1040, W357A, "§ 357a Abs. 1 BGB", "we1", marken=[
    (0, "Wertersatz für einen Wertverlust", beim("we1", "Wertersatz")),
    (2, "zur Prüfung der Beschaffenheit", beim("we2", "Prüfung")),
    (3, "nicht notwendig war", beim("we2", "notwendig")),
    (6, "Widerrufsrecht unterrichtet hat", beim("we6", "belehrt"))], size=28)
assert w357_y <= 540, w357_y
UY = w357_y + 20
folie([("we1", "III. 2. Wertersatz, § 357a Abs. 1 BGB"), ("we2", "III. 2. Wertersatz › Nr. 1: nicht zur Prüfung notwendig"),
       ("we6", "III. 2. Wertersatz › Nr. 2: Belehrung")], rechts_frei([
    *tafel("we1", "III. 2. Wertersatz"),
    *w357,
    bis_(z("Prüfen wie in einem Geschäft", 110, UY, "we3", "Bold", 34), "we6"),
    bis_(z("„… ein Kleidungsstück nur anprobieren, nicht jedoch tragen …“", 110, UY + 50, "we4", "Bold", 32), "we6"),
    bis_(zit("Erwägungsgrund 47 RL 2011/83/EU; BT-Drs. 17/12637, S. 63", 110, UY + 98, beim("we4", "Kleidungsstück")), "we6"),
    *[bis_(e, "we6") for e in okz("anprobieren in der Wohnung: erlaubt", UY + 150, "we5", "Bold", 34, x=160)],
    *[bis_(e, "we6") for e in neinz("Nachmittag draußen im Park: mehr als Prüfen", UY + 215, beim("we5", "Ein", nr=1),
                                    "Bold", 34, x=160)],
    *okz("Nr. 2: ordnungsgemäß belehrt", UY + 10, beim("we6", "Das"), "Bold", 36, x=160),
    blk(110, UY + 90, 1040, 120, GRUEN, "we7", [("Das Widerrufsrecht bleibt.", "ExtraBold", 38, INK),
                                               ("Ilka haftet nur für den Wertverlust.", "Bold", 34, INK)]),
    zit("EuGH, Urt. v. 27.3.2019 – C-681/17, Rn. 47; Erwägungsgrund 47 RL 2011/83/EU", 110, UY + 230, beim("we7", "Sie")),
    *requisit([("we1", ("tabler", "coin-euro", 100, GELB), "Wertersatz?", GELB),
               ("we3", ("tabler", "building-store", 110, WEISS), "wie im Geschäft", WEISS),
               ("we5", ("ph", "sneaker", 150, ERDE), "draußen getragen", ROT),
               ("we6", ("tabler", "file-check", 100, WEISS), "belehrt", GRUEN),
               ("we7", ("tabler", "scale", 110, WEISS), "Widerrufsrecht bleibt", GRUEN)]),
    *paar("we1", [("we1", "sorge"), ("we3", "denkt"), ("we5", "muede"), ("we7", "ruhig")],
          [("we1", "denkt"), ("we5", "froh"), ("we7", "ruhig")]),
]))

# ===========================================================================================================================
# L Ergebnis
# ===========================================================================================================================
folie([("erg", "Ergebnis")], rechts_frei([
    *tafel("erg", "Ergebnis"),
    *okz("Ilka hat wirksam widerrufen.", 190, "erg", "Bold", 38, x=160),
    *okz("Herr Riemann muss die 120 € zurückzahlen.", 280, "erg2", "Bold", 38, x=160),
    z("Ilka schuldet Wertersatz für den Wertverlust:", 110, 380, "erg3", "Bold", 36),
    pl("40 €", 110, 440, beim("erg3", "vierzig"), fill=GELB, size=36),
    zit("neu 120 €, mit den Spuren 80 € wert", 260, 455, beim("erg3", "vierzig")),
    blk(110, 560, 1040, 150, GELB, "erg4", [("Rechnet Herr Riemann auf:", "Bold", 36, INK),
                                           ("120 € − 40 € = 80 € an Ilka", "ExtraBold", 40, INK)]),
    zit("Aufrechnung, §§ 387, 389 BGB", 110, 730, beim("erg4", "achtzig")),
    *requisit([("erg", ("tabler", "arrow-back-up", 100, GRUEN), "Widerruf wirksam", GRUEN),
               ("erg3", ("tabler", "coin-euro", 100, GELB), "Wertersatz 40 €", GELB),
               ("erg4", ("tabler", "coin-euro", 100, GRUEN), "80 € an Ilka", GRUEN)]),
    *paar("erg", [("erg", "froh"), ("erg3", "denkt"), ("erg4", "ruhig")], [("erg", "ernst"), ("erg3", "froh")]),
]))

# ===========================================================================================================================
# M Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Gebrauch erst beim Wertersatz")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Getragene Ware ist kein Ausschlussgrund.", 200, 200, beim("tipp", "Getragene"), "Bold", 38),
    *neinz("nicht beim Widerrufsrecht prüfen", 330, beim("tipp2", "nicht"), "Bold", 36, x=200),
    *okz("sondern bei den Rechtsfolgen: Wertersatz", 410, beim("tipp2", "sondern"), "Bold", 36, x=200),
    zit("§ 357a Abs. 1 BGB", 200, 465, beim("tipp2", "Wertersatz")),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# N Klausurschema (progressiv)
# ===========================================================================================================================
REIHEN = [("k1", "I.", "Widerrufsrecht", BLAU, 0),
          ("k11", "1.", "Verbrauchervertrag, § 310 Abs. 3 BGB", None, 1),
          ("k12", "2.", "Fernabsatzvertrag, § 312c Abs. 1 BGB", None, 1),
          ("k13", "3.", "Widerrufsrecht, § 312g Abs. 1 BGB", None, 1),
          ("k14", "", "keine Ausnahme nach § 312g Abs. 2 BGB", None, 2),
          ("k2", "II.", "Ausübung", GELB, 0),
          ("k21", "1.", "eindeutige Erklärung, § 355 Abs. 1 BGB", None, 1),
          ("k22", "2.", "innerhalb der Frist, §§ 355 Abs. 2, 356 BGB", None, 1),
          ("k3", "III.", "Rechtsfolgen", GRUEN, 0),
          ("k31", "1.", "Rückgewähr, §§ 355 Abs. 3, 357 BGB", None, 1),
          ("k32", "2.", "ggf. Wertersatz, § 357a Abs. 1 BGB", None, 1)]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Schema: Widerruf im Fernabsatz"), 110, 90, "sch", 50)]
y = 185
for c, r, txt, farbe, ebene in REIHEN:
    if ebene == 0:
        els_sch += [karte(110, y, 110, 70, c, fill=farbe, rund=14, schatten=5, rand=4),
                    z(r, 165 - F("ExtraBold", 38).getlength(r) / 2, y + 10, c, "ExtraBold", 38, rechts=1820),
                    z(txt, 255, y + 10, c, "ExtraBold", 38, rechts=1820)]
        y += 88
    else:
        if r:
            els_sch.append(z(r, 270, y + 2, c, "Bold", 36, rechts=1820))
        els_sch.append(z(txt, 330 if ebene == 1 else 380, y + 2, c, "Bold", 36, rechts=1820))
        els_sch.append(ok(230 if ebene == 1 else 340, y + 24, c, gr=18))
        y += 64
assert y <= 975, y
folie([("sch", "Schema: Widerruf im Fernabsatz"), ("k1", "Schema › I. Widerrufsrecht"), ("k2", "Schema › II. Ausübung"),
       ("k3", "Schema › III. Rechtsfolgen")], els_sch)

# ===========================================================================================================================
# O Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Getragen heißt ", 0), ("nicht ausgeschlossen.", "a")]], 750, 300, 46, "merke",
                {"a": beim("merke", "nicht")}),
    *markertext([[("Widerrufen kannst du ", 0)], [("auch nach dem Tragen.", "b")]], 750, 430, 42, "mk2",
                {"b": beim("mk2", "auch")}),
    *markertext([[("Was über das Prüfen hinausgeht,", 0)], [("zahlst du als ", 0), ("Wertersatz.", "c")]], 750, 640, 42,
                "mk3", {"c": beim("mk3", "Wertersatz")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
