"""Folge 109 · Regelverjährung in 5 Minuten: Drei Jahre und der Silvester-Trick – Serienstandard Open Peeps (Katzenkönig).
Beispielfall: Im März 2022 leiht Finn seiner guten Freundin Pia 2.000 € für die Kaution ihrer ersten Wohnung,
Rückzahlungstag 1. Juli 2022. Pia zahlt nicht, Finn fragt nicht nach. Im Oktober 2026 treffen sich beide im Park.
Variante: Abschlag von 200 € am 15. Mai 2024.
Szenen laut ../SZENENPLAN.md: A1 Café (März/Juli 2022), A2 Park (Oktober 2026, Frage), B Sachverhalt, C Sechs Schritte,
D I. Anspruch (§ 194 Abs. 1, Wortlaut), E II. Frist (§ 195, Wortlaut), F III. Beginn (§ 199 Abs. 1, Wortlaut),
G Silvester-Trick (Zeitstrahl), H IV. Höchstfristen (§ 199 Abs. 4, Wortlaut), I V. Hemmung, J V. Neubeginn (§ 212 Abs. 1
Nr. 1, Wortlaut auszugsweise; Variante am Zeitstrahl), K VI. Rechtsfolge (§ 214 Abs. 1, Wortlaut), L Ergebnis,
M Klausurtipp (Lexi), N Rechenschema, O Merksatz (Lexi). Zwei Handlungsgeräusche (Geldscheine bei der Übergabe, Schritte
im Laub, als Finn in den Park kommt; ../geraeusche_herkunft.json).
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/hand als
eigene Kopie aus Folge 103 (gemeinsame Dateien unverändert); neu: leiste() (Rechenweg I.–VI. oben rechts auf den
Schritt-Tafeln), zeitstrahl-Helfer, diagramm-Icons innerhalb der Tafel (Name „diagramm:“, von rechts_frei() ausgenommen).
Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_109/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_109/" in n:
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
PI_N, FI_N = PINK, BLAU                     # Farben der Namensschilder
PX, PY, PU = 1570, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"PI": "Pia", "FI": "Finn"}
NFARBE = {"PI": PI_N, "FI": FI_N}


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
    """Tafelszene: zwei Figuren rechts der Tafel, beide blicken zur Tafel (nach links); l, r = Kürzel FI/PI."""
    return [*fig(l, X1, FB, FR, lf), ns(NAME[l], X1, FB, c0, NFARBE[l], d=0.1),
            *fig(r, X2, FB, FR, rf, d=0.2), ns(NAME[r], X2, FB, c0, NFARBE[r], d=0.3)]


# --- Rechenweg I.–VI. als Leiste oben rechts auf den Schritt-Tafeln ------------------------------------------------------
LEISTE = ("I", "II", "III", "IV", "V", "VI")
LX0, LY, LW, LG = 832, 92, 50, 6            # Leiste: linke Kante, Oberkante, Kästchenbreite, Abstand


def leiste(aktiv, cue):
    els = []
    for k, r in enumerate(LEISTE, 1):
        x = LX0 + (k - 1) * (LW + LG)
        els.append(karte(x, LY, LW, 50, cue, fill=GELB if k == aktiv else WEISS, rund=10, schatten=4 if k == aktiv else 0,
                         rand=4 if k == aktiv else 3))
        f = F("ExtraBold" if k == aktiv else "Bold", 26)
        els.append(z(r, x + LW / 2 - f.getlength(r) / 2 - 1, LY + 10, cue, "ExtraBold" if k == aktiv else "Bold", 26,
                     farbe=INK if k == aktiv else TEXT))
    assert LX0 + 6 * (LW + LG) - LG <= 1180
    return els


# --- Zeitstrahl ------------------------------------------------------------------------------------------------------------
def achse(x0, x1, y, j0, j1, cue, size=28, ticks=True):
    """Zeitstrahl von 1.1.j0 bis 1.1.j1; Jahreszahl mittig im Jahr, Striche an den Jahreswechseln. Gibt (els, zx) zurück."""
    zx = lambda j: x0 + (j - j0) / (j1 - j0) * (x1 - x0)
    els = [linienzug([(x0 - 10, y), (x1 + 10, y)], cue, breite=5)]
    for j in range(j0, j1 + 1):
        if ticks:
            els.append(linienzug([(zx(j), y - 14), (zx(j), y + 14)], cue, breite=4))
        if j < j1:
            w = F("Bold", size).getlength(str(j))
            els.append(z(str(j), zx(j + 0.5) - w / 2, y + 22, cue, "Bold", size))
    return els, zx


def punkt(cx, cy, cue, farbe=ROT, r=11):
    im = Image.new("RGBA", (2 * r + 8, 2 * r + 8))
    ImageDraw.Draw(im).ellipse((4, 4, 2 * r + 4, 2 * r + 4), fill=farbe, outline=INK, width=4)
    return El(im, cx - r - 4, cy - r - 4, cue, "pop", 0.0, None, name="punkt")


# ===========================================================================================================================
# A1 Fall: im Café, März 2022 / 1. Juli 2022
# ===========================================================================================================================
FIX, PIX = 1000, 1600                       # Finn (blickt nach rechts zu Pia), Pia (blickt nach links zu Finn)
TX = 1300                                   # Bistrotisch zwischen beiden


def bistro(cx, unten, cue, w=230, h=270):
    """Runder Bistrotisch in Seitenansicht (programmatisch: Platte, Säule, Fuß; Palettenflächen, Tuschekontur)."""
    s = 2
    im = Image.new("RGBA", ((w + 12) * s, (h + 12) * s))
    dr = ImageDraw.Draw(im)
    o = 6 * s
    dr.rounded_rectangle((o, o, o + w * s, o + 26 * s), 10 * s, fill=LILA, outline=INK, width=5 * s)            # Platte
    dr.rectangle((o + (w / 2 - 12) * s, o + 24 * s, o + (w / 2 + 12) * s, o + (h - 22) * s), fill=WEISS, outline=INK,
                 width=5 * s)                                                                                       # Säule
    dr.rounded_rectangle((o + (w / 2 - 70) * s, o + (h - 26) * s, o + (w / 2 + 70) * s, o + h * s), 8 * s, fill=LILA,
                         outline=INK, width=5 * s)                                                                  # Fuß
    im = im.resize((w + 12, h + 12), Image.LANCZOS)
    return El(im, cx - w / 2 - 6, unten - h - 6, cue, "cut", 0.0, None, name="bistrotisch")


FI_HAND = hand("FI_ruhig_r", FIX, BODEN, FH, +1)
PI_HAND = hand("PI_ruhig", PIX, BODEN, FH, -1)
LEIH = beim("leih", "leiht")
JULI = "juli"
folie([(NULL, "Fall · Im Café"), (JULI, "Fall · 1. Juli 2022")], [
    hart(pl("März 2022", 70, 30, NULL, fill=GELB, size=44, bis=JULI)),
    pl("1. Juli 2022", 70, 30, JULI, fill=GELB, size=44),
    hart(boden(NULL)),
    # Café: Bistrotisch mit zwei Kaffeetassen
    hart(bistro(TX, BODEN, NULL)),
    hart(ficon("tabler", "coffee", TX - 50, BODEN - 270, 64, NULL, fuell=WEISS)),
    hart(ficon("tabler", "coffee", TX + 50, BODEN - 270, 64, NULL, fuell=WEISS, spiegeln=True)),
    # Kaution für die erste Wohnung
    hart(ficon("tabler", "home", 300, 560, 190, NULL, fuell=GELB)),
    hart(ficon("tabler", "key", 470, 560, 90, NULL, fuell=WEISS)),
    hart(pl("Kaution für die erste Wohnung", 330, 610, beim("fall", "Kaution"), fill=WEISS, size=32, anker="m")),
    pl("2.000 € geliehen", 330, 690, LEIH, fill=GELB, size=36, anker="m"),
    # die Geldscheine wandern von Finn zu Pia
    szene(bewegt(ficon("tabler", "cash-banknote", PI_HAND[0] - 30, PI_HAND[1] + 40, 100, LEIH, fuell=GRUEN),
                 LEIH, (LEIH[0], LEIH[1] + 0.9), FI_HAND[0] - PI_HAND[0] + 70, FI_HAND[1] - PI_HAND[1]), "109geld*", 0.8, 0.0),
    # Rückzahlungstag
    ficon("tabler", "calendar-event", 620, 830, 90, beim("fi1", "Juli"), fuell=WEISS),
    pl("zurück am 1.7.2022", 330, 770, beim("fi1", "Juli"), fill=WEISS, size=32, anker="m"),
    # 1. Juli: Pia zahlt nicht, Finn fragt nicht nach
    pl("Pia zahlt nicht", 70, 120, beim("juli", "Pia"), fill=ROT, size=36),
    pl("Finn fragt nicht nach", 70, 200, "still", fill=WEISS, size=36),
    # Finn (links, blickt zu Pia)
    *fig("FI", FIX, BODEN, FH, [(NULL, "froh_r")], bis="fi1", erst="cut"),
    hart(ns("Finn", FIX, BODEN, NULL, FI_N)),
    *redet("FI_redet_r", FIX, BODEN, FH, "fi1", "pi1"),
    *fig("FI", FIX, BODEN, FH, [("pi1", "froh_r"), ("juli", "ruhig_r"), ("still", "denkt_r")], erst="cut"),
    blase("sprech", 560, 200, "fi1", 640, 230, inhalt=["Aber bis zum 1. Juli", "will ich es zurück."], textsize=36,
          figur=("FI_redet_r", FIX, BODEN, FH), bis="pi1"),
    # Pia (rechts, blickt zu Finn)
    *fig("PI", PIX, BODEN, FH, [(NULL, "sorge"), (LEIH, "froh")], bis="pi1", erst="cut"),
    hart(ns("Pia", PIX, BODEN, NULL, PI_N)),
    *redet("PI_redet", PIX, BODEN, FH, "pi1", "juli"),
    *fig("PI", PIX, BODEN, FH, [("juli", "ruhig"), (beim("juli", "zahlt"), "denkt")], erst="cut"),
    blase("sprech", 560, 200, "pi1", 1270, 230, inhalt=["Versprochen. Am 1. Juli", "hast du es."], textsize=36,
          figur=("PI_redet", PIX, BODEN, FH), bis="juli"),
])

# ===========================================================================================================================
# A2 Fall: im Park, Oktober 2026 – die Frage
# ===========================================================================================================================
OKT = "okt"
ANK = ("okt", 1.7)                                     # Finn ist angekommen
folie([(OKT, "Fall · Oktober 2026"), ("frage", "Fall · Die Frage")], [
    pl("Oktober 2026", 70, 30, OKT, fill=GELB, size=44),
    boden(OKT),
    # Park im Herbst: Bäume, Bank, Laub
    ficon("ph", "tree", 190, BODEN, 260, OKT, fuell=ORANGE),
    ficon("ph", "tree", 470, BODEN, 220, OKT, fuell=GELB),
    bank(620, BODEN, OKT, breite=240),
    *[ficon("tabler", "leaf", lx, BODEN - 2, 40, OKT, fuell=f_) for lx, f_ in
      ((330, ROT), (560, ORANGE), (900, GELB), (1300, ORANGE), (1450, ROT), (1820, GELB))],
    # Pia (rechts) ist schon da
    *fig("PI", PIX, BODEN, FH, [(OKT, "ruhig"), (ANK, "staunt"), ("fi2", "sorge")], bis="pi2"),
    ns("Pia", PIX, BODEN, OKT, PI_N, d=0.1),
    *redet("PI_frech", PIX, BODEN, FH, "pi2", "frage"),
    *fig("PI", PIX, BODEN, FH, [("frage", "frech"), ("frage2", "denkt")], erst="cut"),
    # Finn kommt durch das Laub
    szene(bewegt(peep_voll("FI_ruhig_r", FIX, BODEN, FH, OKT, anim="cut", bis=ANK), OKT, ANK, -560), "109laub*", 0.9, 0.05),
    *fig("FI", FIX, BODEN, FH, [(ANK, "ruhig_r")], bis="fi2", erst="cut"),
    bewegt(bis_(hart(ns("Finn", FIX, BODEN, OKT, FI_N)), ANK), OKT, ANK, -560),   # Namensschild läuft mit
    hart(ns("Finn", FIX, BODEN, ANK, FI_N)),
    *redet("FI_fordert_r", FIX, BODEN, FH, "fi2", "pi2"),
    *fig("FI", FIX, BODEN, FH, [("pi2", "sorge_r")], erst="cut"),
    blase("sprech", 700, 200, "fi2", 660, 230, inhalt=["Pia, ich hätte gern endlich", "meine 2.000 € zurück!"], textsize=36,
          figur=("FI_fordert_r", FIX, BODEN, FH), bis="pi2"),
    blase("sprech", 640, 200, "pi2", 1240, 230, inhalt=["Das ist über 4 Jahre her. Ist", "das nicht längst verjährt?"],
          textsize=34, figur=("PI_frech", PIX, BODEN, FH), bis="frage"),
    pl("Seit wann darf sich Pia auf die Verjährung berufen?", 70, 130, "frage", fill=PINK, size=36),
    pl("Und was, wenn sie etwas zurückgezahlt hätte?", 70, 215, "frage2", fill=WEISS, size=34),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_109(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=35, zeilenabstand=1.32)
        els += e; y += 20
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=34))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_109("sv", [
    "Im März 2022 leiht Finn seiner guten Freundin Pia 2.000 Euro für die Kaution ihrer ersten Wohnung. Beide "
    "vereinbaren, dass Pia das Geld am 1. Juli 2022 zurückzahlt. Pia zahlt nicht. Finn fragt nicht nach, verhandelt "
    "nicht mit ihr, klagt nicht und beantragt keinen Mahnbescheid.",
    "Im Oktober 2026 verlangt Finn die 2.000 Euro zurück. Pia meint, das sei längst verjährt.",
    "Variante: Pia hat Finn am 15. Mai 2024 einen Abschlag von 200 Euro gezahlt.",
], "Seit wann darf sich Pia auf die Verjährung berufen – und was ändert der Abschlag?")

# ===========================================================================================================================
# C Rechenweg in sechs Schritten
# ===========================================================================================================================
SCHRITTE = [("s1", "I.", "Anspruch"), ("s2", "II.", "Frist"), ("s3", "III.", "Beginn"), ("s4", "IV.", "Höchstfrist"),
            ("s5", "V.", "Hemmung und Neubeginn"), ("s6", "VI.", "Rechtsfolge")]
folie([("plan", "Regelverjährung › Rechenweg")], rechts_frei([
    *tafel("plan", "Regelverjährung in 6 Schritten"),
    *[e for k, (c, r, t) in enumerate(SCHRITTE) for e in (
        karte(130, 200 + k * 104, 92, 76, c, fill=(BLAU, LILA, GELB, GRUEN, ROT, PINK)[k], rund=14, schatten=5, rand=4),
        z(r, 176 - F("ExtraBold", 36).getlength(r) / 2, 214 + k * 104, c, "ExtraBold", 36),
        z(t, 250, 213 + k * 104, c, "Bold", 40))],
    *requisit([("plan", ("tabler", "list-numbers", 100, WEISS), "6 Schritte", WEISS),
               ("s3", ("tabler", "calendar-event", 100, WEISS), "Beginn", GELB),
               ("s5", ("tabler", "clock-pause", 100, WEISS), "Hemmung und Neubeginn", WEISS)]),
    *paar("plan", "FI", [("plan", "ruhig"), ("s4", "denkt")], "PI", [("plan", "ruhig"), ("s6", "denkt")]),
]))

# ===========================================================================================================================
# D I. Anspruch, § 194 Abs. 1 (Wortlaut)
# ===========================================================================================================================
W194 = ["„(1) Das Recht, von einem anderen ein Tun oder Unterlassen",
        "zu verlangen (Anspruch), unterliegt der Verjährung.“"]
w194, w194_y = wortlaut(80, 190, 1100, W194, "§ 194 Abs. 1 BGB", beim("a194", "Paragraf"), marken=[
    (1, "(Anspruch)", beim("a194", "Anspruch", 2)), (1, "unterliegt der Verjährung", beim("a194", "unterliegt"))], size=34)
folie([("a194", "I. Anspruch › § 194 Abs. 1 BGB"), ("a488", "I. Anspruch › Rückzahlung des Darlehens")], rechts_frei([
    *tafel("a194", "I. Anspruch", frei=820), *leiste(1, "a194"),
    *w194,
    z("Hier: Anspruch auf Rückzahlung des Darlehens", 110, w194_y + 50, "a488", "Bold", 36),
    zit("§ 488 Abs. 1 Satz 2 BGB", 110, w194_y + 100, beim("a488", "Paragraf")),
    blk(110, w194_y + 170, 1040, 90, BLAU, beim("a488", "Rückzahlung"), [("Finn gegen Pia: 2.000 € zurück", "ExtraBold", 38, INK)]),
    *requisit([("a194", ("tabler", "file-text", 100, WEISS), "Anspruch", WEISS),
               ("a488", ("tabler", "cash-banknote", 110, GRUEN), "Rückzahlung", GELB)]),
    *paar("a194", "FI", [("a194", "ruhig"), ("a488", "froh")], "PI", [("a194", "ruhig"), ("a488", "sorge")]),
]))

# ===========================================================================================================================
# E II. Frist, § 195 (Wortlaut)
# ===========================================================================================================================
W195 = ["„Die regelmäßige Verjährungsfrist beträgt drei Jahre.“"]
w195, w195_y = wortlaut(80, 190, 1100, W195, "§ 195 BGB", beim("f195", "Paragraf"), marken=[
    (0, "drei Jahre", beim("f195", "drei"))], size=36)
folie([("f195", "II. Frist › § 195 BGB"), ("fdarl", "II. Frist › auch beim Darlehen")], rechts_frei([
    *tafel("f195", "II. Frist", frei=820), *leiste(2, "f195"),
    *w195,
    blk(110, w195_y + 60, 1040, 120, GELB, beim("f195", "Jahre"), [("3 Jahre", "ExtraBold", 64, INK)]),
    z("gilt auch für die Rückzahlung von Darlehen", 110, w195_y + 230, "fdarl", "Bold", 36),
    zit("BGH, Urt. v. 21.6.2018 – IX ZR 129/17, Rn. 6", 110, w195_y + 280, beim("fdarl", "Rückzahlung")),
    *requisit([("f195", ("tabler", "hourglass", 90, WEISS), "Frist", WEISS),
               (beim("f195", "drei"), ("tabler", "hourglass", 90, GELB), "3 Jahre", GELB),
               ("fdarl", ("tabler", "cash-banknote", 110, GRUEN), "Darlehen", WEISS)]),
    *paar("f195", "FI", [("f195", "ruhig"), ("fdarl", "denkt")], "PI", [("f195", "ruhig"), (beim("f195", "drei"), "staunt")]),
]))

# ===========================================================================================================================
# F III. Beginn, § 199 Abs. 1 (Wortlaut)
# ===========================================================================================================================
W199 = ["„(1) Die regelmäßige Verjährungsfrist beginnt, soweit nicht ein",
        "anderer Verjährungsbeginn bestimmt ist, mit dem Schluss des Jahres,",
        "in dem 1. der Anspruch entstanden ist und 2. der Gläubiger von den",
        "den Anspruch begründenden Umständen und der Person des Schuldners",
        "Kenntnis erlangt oder ohne grobe Fahrlässigkeit erlangen müsste.“"]
w199, w199_y = wortlaut(80, 180, 1100, W199, "§ 199 Abs. 1 BGB", beim("b199", "Nach"), marken=[
    (1, "mit dem Schluss des Jahres", beim("b199", "Schluss")), (2, "der Anspruch entstanden ist", beim("bentst", "entstanden")),
    (4, "Kenntnis erlangt", beim("bkennt", "kennt")), (4, "ohne grobe Fahrlässigkeit", beim("bkennt", "grobe"))], size=30)
folie([("b199", "III. Beginn › § 199 Abs. 1 BGB"), ("bfall", "III. Beginn › der Fall")], rechts_frei([
    *tafel("b199", "III. Beginn", frei=820), *leiste(3, "b199"),
    *w199,
    zit("entstanden = in der Regel fällig: BGH, Beschl. v. 1.2.2023 – XII ZB 104/22, Rn. 16", 110, w199_y + 22,
        beim("bentst", "fällig")),
    linienzug([(110, w199_y + 80), (1150, w199_y + 80)], "bfall", breite=3),
    *okz("1. fällig am 1.7.2022", w199_y + 100, "bfall", "Bold", 36, x=160),
    zit("BGH, Urt. v. 21.6.2018 – IX ZR 129/17, Rn. 6 f.", 600, w199_y + 110, beim("bfall", "fällig")),
    *okz("2. Kenntnis: Finn kennt Pia und alle Umstände", w199_y + 165, "bfall2", "Bold", 36, x=160),
    *requisit([("b199", ("tabler", "calendar-event", 100, WEISS), "Beginn", WEISS),
               (beim("b199", "Schluss"), ("tabler", "calendar-event", 100, GELB), "Schluss des Jahres", GELB),
               ("bentst", ("tabler", "receipt-euro", 90, WEISS), "entstanden: fällig", WEISS),
               ("bkennt", ("tabler", "eye", 100, WEISS), "Kenntnis", WEISS),
               ("bfall", ("tabler", "calendar-event", 100, WEISS), "fällig: 1.7.2022", WEISS)]),
    *paar("b199", "FI", [("b199", "ruhig"), ("bkennt", "denkt"), ("bfall2", "froh")],
          "PI", [("b199", "ruhig"), ("bfall", "sorge")]),
]))

# ===========================================================================================================================
# G Der Silvester-Trick (Zeitstrahl)
# ===========================================================================================================================
ZY = 520
ach, zx = achse(150, 1130, ZY, 2022, 2027, "silv")
JAN, DEZ, ENDE = beim("silv", "Januar"), beim("silv", "Dezember"), beim("silv", "Jahresende")
J23, J24, J25 = beim("sjahre", "zweitausenddreiundzwanzig"), beim("sjahre", "vierundzwanzig"), beim("sjahre", "fünfundzwanzig")
folie([("silv", "III. Beginn › der Silvester-Trick"), ("sende", "III. Beginn › Ende der Frist"),
       ("sneu", "Ergebnis der Rechnung › ab 1.1.2026")], rechts_frei([
    *tafel("silv", "Der Silvester-Trick", frei=820), *leiste(3, "silv"),
    z("Entstanden im Januar oder im Dezember:", 110, 185, "silv", "Bold", 36),
    z("Die Frist startet erst mit dem Jahresende.", 110, 237, ENDE, "Bold", 36),
    *ach,
    # Januar und Dezember 2022 → Jahresende
    punkt(zx(2022.06), ZY, JAN, farbe=BLAU), pl("Januar", zx(2022.06), 340, JAN, fill=BLAU, size=28, anker="m"),
    punkt(zx(2022.82), ZY, DEZ, farbe=LILA), pl("Dezember", zx(2022.82) + 40, 340, DEZ, fill=LILA, size=28, anker="m"),
    pfeil(zx(2022.06) + 8, ZY - 22, zx(2023) - 8, ZY - 42, ENDE, breite=6, kopf=20),
    dicon("tabler", "confetti", zx(2023), ZY - 62, 60, ENDE, fuell=GELB),
    # Fristbeginn 31.12.2022, 24 Uhr
    ring(int(zx(2023)), ZY, 26, 26, "s31", farbe=ROT, breite=6),
    z("Beginn: 31.12.2022, 24 Uhr", 150, ZY + 75, "s31", "Bold", 34),
    # drei volle Jahre
    *[blk(int(zx(j)) + 4, ZY + 128, int(zx(j + 1) - zx(j)) - 8, 56, GELB, c, [(f"{n}. Jahr", "ExtraBold", 30, INK)], anim="fade")
      for n, (j, c) in enumerate(((2023, J23), (2024, J24), (2025, J25)), 1)],
    # Ende der Frist
    ring(int(zx(2026)), ZY, 26, 26, "sende", farbe=ROT, breite=6),
    dicon("tabler", "confetti", zx(2026), ZY - 62, 60, "sende", fuell=GELB),
    z("Ablauf 31.12.2025: verjährt", 150, ZY + 205, "sende", "Bold", 34),
    blk(110, ZY + 270, 1040, 80, GRUEN, "sneu", [("Seit 1.1.2026: Pia darf die Zahlung verweigern", "ExtraBold", 34, INK)]),
    *requisit([("silv", ("tabler", "confetti", 100, GELB), "Silvester", GELB),
               ("s31", ("tabler", "clock-hour-12", 100, WEISS), "31.12.2022, 24 Uhr", WEISS),
               ("sjahre", ("tabler", "hourglass", 90, WEISS), "3 volle Jahre", GELB),
               ("sende", ("tabler", "hourglass-empty", 90, WEISS), "verjährt", ROT),
               ("sneu", ("tabler", "hand-stop", 100, GRUEN), "Pia darf verweigern", GRUEN)]),
    *paar("silv", "FI", [("silv", "ruhig"), ("sjahre", "denkt"), ("sende", "sorge")],
          "PI", [("silv", "ruhig"), ("s31", "denkt"), ("sneu", "frech")]),
]))

# ===========================================================================================================================
# H IV. Höchstfristen, § 199 Abs. 4 (Wortlaut)
# ===========================================================================================================================
W199_4 = ["„(4) Andere Ansprüche als die nach den Absätzen 2 bis 3a verjähren",
          "ohne Rücksicht auf die Kenntnis oder grob fahrlässige Unkenntnis",
          "in zehn Jahren von ihrer Entstehung an.“"]
w199_4, w199_4y = wortlaut(80, 260, 1100, W199_4, "§ 199 Abs. 4 BGB", beim("hoech", "Nach"), marken=[
    (1, "ohne Rücksicht auf die Kenntnis", beim("hoech", "Rücksicht")),
    (2, "in zehn Jahren von ihrer Entstehung an", beim("hoech", "zehn"))], size=31)
folie([("hoech", "IV. Höchstfristen › § 199 Abs. 4 BGB"), ("h23", "IV. Höchstfristen › Schadensersatz")], rechts_frei([
    *tafel("hoech", "IV. Höchstfristen", frei=820), *leiste(4, "hoech"),
    z("Ohne Kenntnis: Höchstfrist", 110, 190, beim("hoech", "Fehlt"), "Bold", 38),
    *w199_4,
    blk(110, w199_4y + 40, 1040, 80, GELB, beim("hoech", "Entstehung"), [("10 Jahre ab Entstehung", "ExtraBold", 38, INK)]),
    z("Schadensersatz: § 199 Abs. 2 und 3 BGB", 110, w199_4y + 160, "h23", "Bold", 36),
    *requisit([("hoech", ("tabler", "eye-off", 100, WEISS), "ohne Kenntnis", WEISS),
               (beim("hoech", "zehn"), ("tabler", "calendar-time", 100, WEISS), "10 Jahre", GELB),
               ("h23", ("tabler", "scale", 100, WEISS), "Schadensersatz", WEISS)]),
    *paar("hoech", "FI", [("hoech", "ruhig"), ("h23", "denkt")], "PI", [("hoech", "ruhig"), (beim("hoech", "zehn"), "staunt")]),
]))

# ===========================================================================================================================
# I V. Hemmung
# ===========================================================================================================================
folie([("hemm", "V. Hemmung › die Uhr hält an"), ("h203", "V. Hemmung › §§ 203, 204 BGB"),
       ("hnein", "V. Hemmung › der Fall")], rechts_frei([
    *tafel("hemm", "V. Hemmung", frei=820), *leiste(5, "hemm"),
    z("Die Hemmung hält die Uhr an.", 110, 190, beim("hemm", "Die"), "Bold", 38),
    z("§ 209: Diese Zeit wird nicht mitgerechnet.", 110, 245, beim("hemm", "diese"), size=34),
    z("§ 203: Verhandlungen über den Anspruch", 150, 330, "h203", "Bold", 36),
    z("§ 204 Abs. 1 Nr. 1: Erhebung der Klage", 150, 395, "h204a", "Bold", 36),
    z("§ 204 Abs. 1 Nr. 3: Zustellung des Mahnbescheids", 150, 460, "h204b", "Bold", 36),
    linienzug([(110, 545), (1150, 545)], "hnein", breite=3),
    *neinz("keine Verhandlungen", 570, beim("hnein", "keine"), "Bold", 36, x=160),
    *neinz("keine Klage", 630, beim("hnein", "Klage"), "Bold", 36, x=160),
    *neinz("kein Mahnbescheid", 690, beim("hnein", "Mahnbescheid"), "Bold", 36, x=160),
    blk(110, 770, 1040, 80, LILA, beim("hnein", "Mahnbescheid"), [("Hier nichts davon: keine Hemmung", "ExtraBold", 38, INK)]),
    *requisit([("hemm", ("tabler", "clock-pause", 100, WEISS), "Uhr hält an", WEISS),
               ("h203", ("tabler", "message-circle-question", 100, WEISS), "verhandeln", WEISS),
               ("h204a", ("tabler", "gavel", 100, WEISS), "Klage", WEISS),
               ("h204b", ("tabler", "mail", 100, WEISS), "Mahnbescheid", WEISS),
               ("hnein", ("tabler", "x", 100, WEISS), "nichts davon", ROT)]),
    *paar("hemm", "FI", [("hemm", "ruhig"), ("hnein", "sorge")], "PI", [("hemm", "ruhig"), ("hnein", "froh")]),
]))

# ===========================================================================================================================
# J V. Neubeginn, § 212 Abs. 1 Nr. 1 (Wortlaut auszugsweise) und Variante am Zeitstrahl
# ===========================================================================================================================
W212 = ["„(1) Die Verjährung beginnt erneut, wenn",
        "1. der Schuldner dem Gläubiger gegenüber den Anspruch durch",
        "Abschlagszahlung, … anerkennt …“"]
w212, w212_y = wortlaut(80, 245, 1100, W212, "§ 212 Abs. 1 Nr. 1 BGB", beim("neu", "Paragraf"), marken=[
    (0, "beginnt erneut", beim("neu", "beginnt")), (2, "Abschlagszahlung", beim("neu", "Abschlagszahlung"))], size=31)
ZY2 = 650
ach2, zx2 = achse(150, 1130, ZY2, 2022, 2028, "var", size=26)
VA, VE = 2024 + (31 + 29 + 31 + 30 + 15) / 366, 2027 + (31 + 28 + 31 + 30 + 15) / 365    # 15.5.2024 bzw. 15.5.2027
folie([("neu", "V. Neubeginn › § 212 Abs. 1 Nr. 1 BGB"), ("var", "V. Neubeginn › Variante: Abschlag"),
       ("vrest", "V. Neubeginn › Variante: Ergebnis")], rechts_frei([
    *tafel("neu", "V. Neubeginn", frei=820), *leiste(5, "neu"),
    z("Der Neubeginn stellt die Uhr auf null.", 110, 190, "neu", "Bold", 38),
    *w212,
    *ach2,
    punkt(zx2(VA), ZY2, beim("var", "fünfzehnten"), farbe=GRUEN),
    dicon("tabler", "coin-euro", zx2(VA), ZY2 - 30, 56, beim("var", "zweihundert"), fuell=GELB),
    pl("15.5.2024: Abschlag 200 €", zx2(VA), ZY2 - 150, beim("var", "zweihundert"), fill=GRUEN, size=28, anker="m"),
    blk(int(zx2(VA)), ZY2 + 64, int(zx2(VE) - zx2(VA)), 54, GELB, "vtag", [("neue 3 Jahre, taggenau", "ExtraBold", 28, INK)],
        anim="fade"),
    z("ab 16.5.2024, ohne Silvester-Trick", 150, ZY2 + 128, beim("vtag", "taggenau"), "Bold", 30),
    zit("BGH XII ZR 86/11, Rn. 33", 700, ZY2 + 133, beim("vtag", "taggenau")),
    ring(int(zx2(VE)), ZY2, 19, 19, "vende", farbe=ROT, breite=6),
    pl("Ablauf 15.5.2027", zx2(VE), ZY2 - 150, "vende", fill=WEISS, size=28, anker="m"),
    blk(110, ZY2 + 175, 1040, 64, HELLROT, "vrest", [("Pia müsste die restlichen 1.800 € noch zahlen", "ExtraBold", 32, INK)]),
    *requisit([("neu", ("tabler", "refresh", 100, WEISS), "auf null", WEISS),
               ("var", ("tabler", "calendar-event", 100, WEISS), "15.5.2024", WEISS),
               (beim("var", "zweihundert"), ("tabler", "coin-euro", 100, GELB), "200 € gezahlt", GRUEN),
               ("vtag", ("tabler", "calendar-event", 100, WEISS), "taggenau", GELB),
               ("vrest", ("tabler", "cash-banknote", 110, ROT), "Rest: 1.800 €", ROT)]),
    *paar("neu", "FI", [("neu", "ruhig"), ("var", "denkt"), ("vrest", "froh")], "PI", [("neu", "ruhig"), ("vrest", "sorge")]),
]))

# ===========================================================================================================================
# K VI. Rechtsfolge, § 214 Abs. 1 (Wortlaut)
# ===========================================================================================================================
W214 = ["„(1) Nach Eintritt der Verjährung ist der Schuldner berechtigt,",
        "die Leistung zu verweigern.“"]
w214, w214_y = wortlaut(80, 190, 1100, W214, "§ 214 Abs. 1 BGB", beim("r214", "Nach"), marken=[
    (0, "Nach Eintritt der Verjährung", beim("r214", "Eintritt")), (1, "die Leistung zu verweigern", beim("r214", "Leistung"))],
    size=34)
folie([("r214", "VI. Rechtsfolge › § 214 Abs. 1 BGB")], rechts_frei([
    *tafel("r214", "VI. Rechtsfolge", frei=820), *leiste(6, "r214"),
    *w214,
    z("Der Anspruch erlischt nicht.", 110, w214_y + 55, beim("r214", "erlischt"), "Bold", 38),
    blk(110, w214_y + 140, 1040, 90, GELB, beim("r214", "berufen"), [("Pia muss sich darauf berufen", "ExtraBold", 38, INK)]),
    *requisit([("r214", ("tabler", "file-text", 100, WEISS), "Rechtsfolge", WEISS),
               (beim("r214", "verweigern"), ("tabler", "hand-stop", 100, GELB), "verweigern", GELB),
               (beim("r214", "erlischt"), ("tabler", "file-text", 100, WEISS), "erlischt nicht", WEISS)]),
    *paar("r214", "FI", [("r214", "ruhig"), (beim("r214", "erlischt"), "denkt")],
          "PI", [("r214", "ruhig"), (beim("r214", "berufen"), "frech")]),
]))

# ===========================================================================================================================
# L Ergebnis
# ===========================================================================================================================
folie([("erg", "Ergebnis")], rechts_frei([
    *tafel("erg", "Ergebnis"),
    z("Anspruch von Finn:", 110, 200, "erg", "Bold", 38),
    *neinz("verjährt mit Ablauf des 31.12.2025", 265, beim("erg", "verjährt"), "Bold", 38, x=160),
    blk(110, 360, 1040, 90, GELB, "erg2", [("Beruft sich Pia darauf: Sie muss nicht zahlen", "ExtraBold", 34, INK)]),
    linienzug([(110, 500), (1150, 500)], "erg3", breite=3),
    z("Variante mit Abschlag:", 110, 525, "erg3", "Bold", 36),
    blk(110, 590, 1040, 90, HELLROT, beim("erg3", "Rest"), [("Rest bis Mai 2027 durchsetzbar", "ExtraBold", 36, INK)]),
    *requisit([("erg", ("tabler", "file-text", 100, WEISS), "Anspruch von Finn", WEISS),
               (beim("erg", "verjährt"), ("tabler", "hourglass-empty", 90, WEISS), "verjährt", ROT),
               ("erg2", ("tabler", "hand-stop", 100, GELB), "Einrede", GELB),
               ("erg3", ("tabler", "coin-euro", 100, GELB), "mit Abschlag", WEISS)]),
    *paar("erg", "FI", [("erg", "sorge"), ("erg3", "froh")], "PI", [("erg", "ruhig"), ("erg2", "frech"), ("erg3", "sorge")]),
]))

# ===========================================================================================================================
# M Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · zuerst die Fälligkeit"), ("tipp2", "Klausurtipp · Abschlag nur in laufender Frist")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Prüfe zuerst die Fälligkeit!", 200, 200, beim("tipp", "Prüfe"), "Bold", 38),
    z("Kein Rückzahlungstag vereinbart:", 200, 275, beim("tipp", "Ist"), "Bold", 34),
    z("Fälligkeit hängt von einer Kündigung ab,", 200, 325, beim("tipp", "hängt"), size=34),
    zit("§ 488 Abs. 3 Satz 1 BGB; BGH, Urt. v. 21.6.2018 – IX ZR 129/17, Rn. 6", 200, 375, beim("tipp", "Paragraf")),
    z("erst dann kann die Frist beginnen.", 200, 420, beim("tipp", "erst"), size=34),
    linienzug([(130, 500), (1130, 500)], "tipp2", breite=3),
    z("Ein Abschlag wirkt nur, während die Frist läuft.", 200, 530, "tipp2", "Bold", 36),
    zit("vor Fristbeginn: BGH, Urt. v. 21.6.2018 – IX ZR 129/17, Rn. 8", 200, 585, beim("tipp2", "während")),
    zit("nach Ablauf: BGH, Urt. v. 11.11.2014 – XI ZR 265/13, Rn. 40", 200, 625, beim("tipp2", "läuft")),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# N Rechenschema
# ===========================================================================================================================
REIHEN = [("k1", "I.", "Anspruch", "§ 194 Abs. 1 BGB", None),
          ("k2", "II.", "Frist: 3 Jahre", "§ 195 BGB", None),
          ("k3", "III.", "Beginn", "§ 199 Abs. 1 BGB",
           [("1. Entstehung", "Entstehung"), ("2. Kenntnis", "Kenntnis"), ("3. Jahresschluss", "Jahresschluss")]),
          ("k4", "IV.", "Höchstfristen", "§ 199 Abs. 2 bis 4 BGB", None),
          ("k5", "V.", "Hemmung und Neubeginn", "§§ 203, 204, 209, 212 BGB", None),
          ("k6", "VI.", "Rechtsfolge", "§ 214 Abs. 1 BGB", None)]
FARBEN = (BLAU, LILA, GELB, GRUEN, ROT, PINK)
els_sch = [karte(60, 50, 1800, 920, "sch"), titel(glyphen("Rechenschema: Regelverjährung"), 110, 90, "sch", 50)]
y = 200
for k, (c, r, kopf, norm, unter) in enumerate(REIHEN):
    hh = 150 if unter else 96
    els_sch += [karte(110, y, 100, 74, c, fill=FARBEN[k], rund=14, schatten=5, rand=4),
                z(r, 160 - F("ExtraBold", 38).getlength(r) / 2, y + 12, c, "ExtraBold", 38, rechts=1820),
                z(kopf, 245, y + 12, c, "Bold", 40, rechts=1820),
                zit(norm, 1330, y + 26, c, size=30, rechts=1820)]
    if unter:
        xx = 245
        for t, w in unter:
            els_sch.append(z(t, xx, y + 78, beim(c, w), size=34, rechts=1820))
            xx += F("Regular", 34).getlength(t) + 60
    y += hh + 12
assert y <= 960, y
folie([("sch", "Rechenschema"), ("k1", "Rechenschema › I. Anspruch"), ("k2", "Rechenschema › II. Frist"),
       ("k3", "Rechenschema › III. Beginn"), ("k4", "Rechenschema › IV. Höchstfristen"),
       ("k5", "Rechenschema › V. Hemmung und Neubeginn"), ("k6", "Rechenschema › VI. Rechtsfolge")], els_sch)

# ===========================================================================================================================
# O Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Drei Jahre,", "a"), (" gerechnet ab Silvester des Jahres,", 0)], [("in dem der Anspruch fällig wird", 0)],
                 [("und der Gläubiger davon weiß oder wissen müsste.", 0)]],
                750, 290, 40, "merke", {"a": beim("merke", "Drei")}),
    *markertext([[("Die Hemmung ", 0), ("hält die Uhr an,", "b")]], 750, 560, 44, "mk2", {"b": beim("mk2", "hält")}),
    *markertext([[("ein Anerkenntnis ", 0), ("stellt sie auf null.", "c")]], 750, 670, 44, "mk3", {"c": beim("mk3", "stellt")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
