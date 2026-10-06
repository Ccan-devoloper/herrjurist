"""Folge 212 · § 326 BGB: Konzert fällt aus – wer trägt die Gegenleistungsgefahr? – Serienstandard Open Peeps (Katzenkönig).
Beispielfall: Friedhelm (70) bucht für seine Geburtstagsfeier am Samstagabend den Pianisten Theodor (Privatkonzert, Honorar
2.000 €, 500 € angezahlt). Am Samstagmittag sagt Theodor ab: hohes Fieber; ein anderer Termin kommt nicht in Frage.
Gegenfall: Theodor gesund, Friedhelm sagt ab (spontane Reise); Theodor spart 100 € Taxi.
Szenen laut ../SZENENPLAN.md: A1 Buchung, A2 Anruf/Frage, B Sachverhalt, C Synallagma, D Aufbau, E/F I. entstanden und
II. § 326 Abs. 1 Satz 1 (Wortlaut), G II. im Fall (Fixgeschäft, BGH VII ZR 144/22), H III. § 326 Abs. 2 Satz 1 (Wortlaut) und
Grundfall, I Gegenfall (Absage), J § 326 Abs. 2 Satz 2 (Wortlaut) und Anrechnung, K Hinweis § 648 BGB, L IV. § 326 Abs. 4
(Wortlaut), Abs. 5, Abs. 3, M Klausurtipp (Lexi), N Klausurschema, O Merksatz (Lexi).
Handlungsgeräusch: Telefonklingeln, wenn das Telefon beim Angerufenen erscheint (../geraeusche_herkunft.json).
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/hand/okz/
neinz als eigene Kopie aus Folge 170 (gemeinsame Dateien unverändert); neu: klavier(), trenner(), telefon(), paar().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_212/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_212/" in n:
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



def punkt(cx, cy, cue, farbe=ROT, r=11):
    im = Image.new("RGBA", (2 * r + 8, 2 * r + 8))
    ImageDraw.Draw(im).ellipse((4, 4, 2 * r + 4, 2 * r + 4), fill=farbe, outline=INK, width=4)
    return El(im, cx - r - 4, cy - r - 4, cue, "pop", 0.0, None, name="punkt")





BODEN, FH = 860, 480
X1, X2 = 1420, 1720                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
TH_N, FR_N = GELB, LILA                     # Farben der Namensschilder
PX, PY, PU = 1570, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"TH": "Theodor", "FR": "Friedhelm"}
KX = 560                                    # Wohnzimmer: Klavier, Mitte
TX, AX = 1250, 1680                         # Buchung: Theodor (blickt nach rechts), Friedhelm (blickt nach links)
LX_, RX_ = 760, 1480                        # Telefonszenen: Theodor links (blickt nach rechts), Friedhelm rechts (nach links)
TRENN = 1110                                # Trennlinie zwischen den beiden Orten der Telefonszenen


def boden(cue, hart_=False, x0=40, x1=1880):
    e = linienzug([(x0, BODEN), (x1, BODEN)], cue, breite=7, farbe=INK)
    return hart(e) if hart_ else e


def auf_boden(e, y=BODEN + 2):
    """Icon so verschieben, dass seine sichtbare Unterkante (ohne Innenrand des Icons) auf der Bodenlinie steht."""
    bb = e.sprite.getbbox()
    e.y = y - bb[3]
    return e


def oberkante(e):
    return e.y + e.sprite.getbbox()[1]


def klavier(cue, cx=KX, breite=420, bis=None, anim="cut"):
    """Friedhelms Klavier (Tabler piano), auf dem Boden."""
    return auf_boden(ficon("tabler", "piano", cx, BODEN, breite, cue, fuell=WEISS, bis=bis, anim=anim))


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


def paar(c0, tf, ff):
    """Tafelszene: Theodor und Friedhelm rechts der Tafel, beide blicken zur Tafel (nach links)."""
    return [*fig("TH", X1, FB, FR, tf), ns(NAME["TH"], X1, FB, c0, TH_N, d=0.1),
            *fig("FR", X2, FB, FR, ff, d=0.2), ns(NAME["FR"], X2, FB, c0, FR_N, d=0.3)]


def trenner(cue):
    return linienzug([(TRENN, 90), (TRENN, BODEN)], cue, breite=4, farbe=INK)


def telefon(figname, cx, seite, cue, bis=None, klingeln=False):
    """Telefon an der Hand der Figur (seite -1 links, +1 rechts); beim Angerufenen klingelt es beim Erscheinen."""
    hx, hy = hand(figname, cx, BODEN, FH, seite)
    e = ficon("tabler", "phone-call", hx + seite * 10, hy + 30, 64, cue, fuell=WEISS, bis=bis)
    return szene(e, "212telefon*", 0.55, 0.0) if klingeln else e


# ===========================================================================================================================
# A1 Fall: die Buchung
# ===========================================================================================================================
TH_DA = beim("bucht", "Theodor")
_KL = klavier(NULL)
folie([(NULL, "Fall · Die Buchung")], [
    hart(boden(NULL)), _KL,
    auf_boden(ficon("tabler", "cake", 640, BODEN, 120, NULL, fuell=GELB, anim="cut"), oberkante(_KL) + 3),
    ficon("tabler", "balloon", 170, 600, 110, NULL, fuell=ROT, anim="cut"),
    ficon("tabler", "balloon", 270, 640, 100, NULL, fuell=BLAU, anim="cut"),
    pl("70. Geburtstag", 70, 30, beim("fall", "siebzig"), fill=WEISS, size=40),
    pl("Privatkonzert am Samstagabend", 70, 120, beim("bucht", "Privatkonzert"), fill=LILA, size=36),
    pl("Honorar: 2.000 €", 70, 205, beim("bucht", "zweitausend"), fill=GELB, size=36),
    pl("Anzahlung: 500 €", 70, 290, "anz", fill=GRUEN, size=36),
    ficon("tabler", "cash-banknote", 1465, 600, 110, "anz", fuell=GRUEN),
    *fig("TH", TX, BODEN, FH, [(TH_DA, "ruhig_r")], bis="th1"),
    ns("Theodor", TX, BODEN, TH_DA, TH_N, d=0.1),
    *redet("TH_redet_r", TX, BODEN, FH, "th1", "fr1"),
    peep_voll("TH_froh_r", TX, BODEN, FH, "fr1", anim="cut", bis="krank"),
    blase("sprech", 600, 200, "th1", 1200, 200, inhalt=["Am Samstagabend spiele ich", "für Ihre Gäste."], textsize=34,
          figur=("TH_redet_r", TX, BODEN, FH), bis="fr1"),
    *fig("FR", AX, BODEN, FH, [(NULL, "ruhig"), (TH_DA, "froh")], bis="fr1", erst="cut"),
    hart(ns("Friedhelm", AX, BODEN, NULL, FR_N)),
    *redet("FR_redet", AX, BODEN, FH, "fr1", "krank"),
    blase("sprech", 600, 200, "fr1", 1560, 200, inhalt=["Wunderbar. Den Rest zahle ich", "nach dem Konzert."], textsize=34,
          figur=("FR_redet", AX, BODEN, FH), bis="krank"),
])

# ===========================================================================================================================
# A2 Fall: der Anruf (Theodor zu Hause mit Fieber | Friedhelm im Wohnzimmer)
# ===========================================================================================================================
RUFT = beim("krank", "ruft")
FIEBER = beim("th2", "Fieber")
folie([("krank", "Fall · Der Anruf"), ("aus", "Fall · Das Konzert fällt aus"), ("frage", "Fall · Die Frage")], [
    boden("krank", x0=40, x1=TRENN - 30), boden("krank", x0=TRENN + 30, x1=1880), trenner("krank"),
    auf_boden(ficon("tabler", "bed", 330, BODEN, 330, "krank", fuell=BLAU, anim="cut")),
    klavier("krank", cx=1760, breite=200),
    pl("Samstagmittag", 70, 30, "krank", fill=WEISS, size=40),
    pl("hohes Fieber", 70, 120, FIEBER, fill=ROT, size=36),
    ficon("tabler", "thermometer", 330, 470, 110, FIEBER, fuell=ROT),
    *fig("TH", LX_, BODEN, FH, [("krank", "krank_r")], bis="th2"),
    *redet("TH_krank_redet_r", LX_, BODEN, FH, "th2", "fr2"),
    *fig("TH", LX_, BODEN, FH, [("fr2", "krank_r"), ("aus", "sorge_r")], erst="cut"),
    ns("Theodor", LX_, BODEN, "krank", TH_N, d=0.1),
    blase("sprech", 600, 200, "th2", 760, 205, inhalt=["Ich habe hohes Fieber. Ich kann", "heute Abend nicht spielen."],
          textsize=32, figur=("TH_krank_redet_r", LX_, BODEN, FH), bis="fr2"),
    *fig("FR", RX_, BODEN, FH, [("krank", "ruhig"), (FIEBER, "sorge")], bis="fr2"),
    *redet("FR_sorge_redet", RX_, BODEN, FH, "fr2", "aus"),
    *fig("FR", RX_, BODEN, FH, [("aus", "sorge"), ("frage", "denkt")], erst="cut"),
    ns("Friedhelm", RX_, BODEN, "krank", FR_N, d=0.2),
    blase("sprech", 620, 200, "fr2", 1480, 205, inhalt=["Und an einem anderen Tag?", "Meine Gäste kommen nur heute!"],
          textsize=32, figur=("FR_sorge_redet", RX_, BODEN, FH), bis="aus"),
    pl("Konzert fällt aus", 70, 205, "aus", fill=ROT, size=36),
    pl("Feier nicht verschiebbar", 70, 290, beim("aus", "verschieben"), fill=WEISS, size=36),
    pl("Muss Friedhelm trotzdem zahlen?", 1160, 40, "frage", fill=PINK, size=34),
    pl("Bekommt er die Anzahlung zurück?", 1160, 130, "frage2", fill=WEISS, size=34),
])
FOLIEN[-1]["els"] += [telefon("TH_krank_r", LX_, 1, RUFT), telefon("FR_ruhig", RX_, -1, RUFT, klingeln=True)]


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_212(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=38, zeilenabstand=1.32)
        els += e; y += 18
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 10, cue, fill=PINK, size=36))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_212("sv", [
    "Friedhelm feiert am Samstagabend zu Hause seinen 70. Geburtstag. Für die Feier bucht er den Pianisten Theodor: "
    "ein Privatkonzert für 2.000 Euro Honorar. 500 Euro zahlt er gleich an, den Rest will er nach dem Konzert zahlen.",
    "Am Samstagmittag ruft Theodor an: Er hat hohes Fieber und kann am Abend nicht spielen. Theodor muss persönlich "
    "spielen. Ein anderer Termin kommt nicht in Frage, denn die Gäste kommen nur an diesem Abend.",
    "Friedhelm fragt, ob er trotzdem zahlen muss und ob er die Anzahlung zurückbekommt.",
], "Muss Friedhelm zahlen – und bekommt er die 500 Euro zurück?")

# ===========================================================================================================================
# C Synallagma: gegenseitiger Vertrag, Gegenleistungsgefahr
# ===========================================================================================================================
folie([("syn", "Synallagma › gegenseitiger Vertrag"), ("syn5", "Synallagma › Gegenleistungsgefahr")], rechts_frei([
    *tafel("syn", "Der gegenseitige Vertrag"),
    blk(110, 185, 470, 90, GELB, beim("syn", "gegenseitiger"), [("Theodor: Konzert", "ExtraBold", 36, INK)]),
    blk(680, 185, 470, 90, LILA, beim("syn", "gegenseitiger"), [("Friedhelm: 2.000 €", "ExtraBold", 36, INK)]),
    dicon("tabler", "arrows-exchange", 630, 262, 80, beim("syn", "gegenseitiger"), fuell=WEISS),
    z("Leistung, weil der andere leistet", 110, 310, beim("syn2", "weil"), "Bold", 36),
    linienzug([(110, 385), (1150, 385)], "syn3", breite=3),
    z("Leistung entfällt nach § 275 BGB", 110, 410, "syn3", "Bold", 36),
    blk(110, 475, 1040, 75, LILA, beim("syn3", "Video"), [("Mehr dazu: Video „Unmöglichkeit § 275 BGB“", "ExtraBold", 32, INK)]),
    z("Was wird aus der Gegenleistung?", 110, 585, "syn4", "Bold", 38),
    blk(110, 670, 1040, 85, GELB, beim("syn5", "Gegenleistungsgefahr"), [("Gegenleistungsgefahr", "ExtraBold", 38, INK)]),
    z("auch: Preisgefahr", 110, 775, beim("syn5", "Preisgefahr"), size=34),
    *requisit([("syn", ("tabler", "arrows-exchange", 110, WEISS), "Konzert gegen Honorar", WEISS),
               ("syn3", ("tabler", "music-off", 100, WEISS), "Leistung entfällt", ROT),
               ("syn4", ("tabler", "coin-euro", 100, GELB), "Gegenleistung?", GELB)]),
    *paar("syn", [("syn", "ruhig"), ("syn3", "sorge"), ("syn5", "denkt")], [("syn", "ruhig"), ("syn4", "denkt")]),
]))

# ===========================================================================================================================
# D Aufbau: vier Schritte
# ===========================================================================================================================
SCHRITTE = [("p1", "I.", "entstanden?", BLAU), ("p2", "II.", "untergegangen, § 326 Abs. 1?", GELB),
            ("p3", "III.", "ausnahmsweise erhalten, Abs. 2?", GRUEN), ("p4", "IV.", "die Anzahlung", LILA)]
folie([("plan", "Anspruch auf das Honorar › Aufbau")], rechts_frei([
    *tafel("plan", "Anspruch auf das Honorar"),
    *[e for k, (c, r, t, fa) in enumerate(SCHRITTE) for e in (
        karte(130, 210 + k * 140, 110, 90, c, fill=fa, rund=14, schatten=5, rand=4),
        z(r, 185 - F("ExtraBold", 40).getlength(r) / 2, 230 + k * 140, c, "ExtraBold", 40),
        z(t, 280, 230 + k * 140, c, "Bold", 38))],
    *requisit([("plan", ("tabler", "list-numbers", 100, WEISS), "4 Schritte", WEISS),
               ("p1", ("tabler", "file-certificate", 100, WEISS), "entstanden", BLAU),
               ("p2", ("tabler", "music-off", 100, WEISS), "untergegangen", GELB),
               ("p3", ("tabler", "user-question", 100, WEISS), "Ausnahme", GRUEN),
               ("p4", ("tabler", "cash-banknote", 110, GRUEN), "Anzahlung", LILA)]),
    *paar("plan", [("plan", "ruhig"), ("p3", "denkt")], [("plan", "ruhig"), ("p4", "denkt")]),
]))

# ===========================================================================================================================
# E I. entstanden  ·  F II. § 326 Abs. 1 Satz 1 (Wortlaut)
# ===========================================================================================================================
W326 = ["„(1) Braucht der Schuldner nach § 275 Abs. 1 bis 3 nicht zu",
        "leisten, entfällt der Anspruch auf die Gegenleistung; …“"]
w326, w326_y = wortlaut(80, 380, 1100, W326, "§ 326 Abs. 1 Satz 1 BGB", beim("w326", "Paragraf"), marken=[
    (0, "nicht zu", beim("w326", "nicht")), (1, "entfällt", beim("w326", "entfällt")),
    (1, "Anspruch auf die Gegenleistung", beim("w326", "Anspruch"))], size=34)
folie([("e1", "I. Anspruch entstanden"), ("w326", "II. Untergegangen › § 326 Abs. 1 Satz 1 BGB")], rechts_frei([
    *tafel("e1", "Anspruch auf das Honorar"),
    *okz("I. Vertrag: Anspruch auf 2.000 € entstanden", 185, beim("e1", "entstanden"), "Bold", 36, x=160),
    linienzug([(110, 270), (1150, 270)], "w326", breite=3),
    z("II. Untergegangen?", 110, 295, "w326", "ExtraBold", 40),
    *w326,
    blk(110, w326_y + 40, 1040, 80, GELB, beim("w326", "Gegenleistung"), [("Schuldner frei: Gegenleistung entfällt", "ExtraBold", 36, INK)]),
    *requisit([("e1", ("tabler", "file-certificate", 100, WEISS), "Vertrag", BLAU),
               ("w326", ("tabler", "scale", 100, WEISS), "§ 326 Abs. 1", WEISS),
               (beim("w326", "entfällt"), ("tabler", "coin-euro", 100, WEISS), "entfällt", ROT)]),
    *paar("e1", [("e1", "froh"), ("w326", "ruhig"), (beim("w326", "entfällt"), "sorge")],
          [("e1", "ruhig"), (beim("w326", "entfällt"), "denkt")]),
]))

# ===========================================================================================================================
# G II. im Fall: persönlich, nachholbar?, absolutes Fixgeschäft, unmöglich
# ===========================================================================================================================
folie([("u1", "II. Untergegangen › Schuldner Theodor"), ("u3", "II. Untergegangen › nachholbar?"),
       ("u5", "II. Untergegangen › absolutes Fixgeschäft"), ("u6", "II. Untergegangen › § 275 Abs. 1 BGB"),
       ("u7", "II. Untergegangen › Gegenleistungsgefahr")], rechts_frei([
    *tafel("u1", "II. Untergegangen im Fall?"),
    *okz("Schuldner des Konzerts: Theodor", 180, beim("u1", "Schuldner"), "Bold", 36, x=160),
    *okz("persönlich zu spielen: mit Fieber nicht möglich", 240, beim("u2", "persönlich"), "Bold", 34, x=160),
    z("unmöglich nur, wenn nicht nachholbar", 160, 305, beim("u3", "nicht"), "Bold", 34),
    zit("BGH, 27.4.2023 – VII ZR 144/22, Leitsatz 1, Rn. 14", 160, 362, beim("u4", "Bundesgerichtshof")),
    z("Hochzeit verlegt: Leistung nicht unmöglich", 160, 400, beim("u4", "verlegt"), size=34),
    z("Feier nur an diesem Abend", 160, 462, beim("u5", "Feier"), "Bold", 34),
    zit("später wertlos – vgl. BGH, 28.8.2012 – X ZR 128/11, Rn. 34", 160, 510, beim("u5", "wertlos")),
    *okz("absolutes Fixgeschäft", 550, beim("u5", "Fixgeschäft"), "Bold", 34, x=160),
    *okz("mit dem Abend unmöglich, § 275 Abs. 1 BGB", 605, beim("u6", "unmöglich"), "Bold", 34, x=160),
    blk(110, 670, 1040, 75, GELB, beim("u7", "entfällt"), [("Anspruch auf das Honorar entfällt", "ExtraBold", 36, INK)]),
    blk(110, 765, 1040, 75, ROT, beim("u7", "Gegenleistungsgefahr"), [("Gegenleistungsgefahr trägt Theodor", "ExtraBold", 36, INK)]),
    *requisit([("u1", ("tabler", "piano", 140, WEISS), "Konzert", LILA),
               ("u2", ("tabler", "thermometer", 100, ROT), "Fieber", ROT),
               ("u4", ("tabler", "camera", 110, WEISS), "Hochzeitsfotografin", WEISS),
               ("u5", ("tabler", "calendar-event", 100, WEISS), "nur dieser Abend", GELB),
               ("u6", ("tabler", "music-off", 100, WEISS), "unmöglich", ROT),
               ("u7", ("tabler", "coin-euro", 100, WEISS), "kein Honorar", GELB)]),
    *paar("u1", [("u1", "ruhig"), ("u2", "krank"), ("u4", "denkt"), ("u7", "sorge")],
          [("u1", "ruhig"), ("u3", "denkt"), ("u6", "sorge"), ("u7", "ruhig")]),
]))

# ===========================================================================================================================
# H III. § 326 Abs. 2 Satz 1 (Wortlaut), Grundfall
# ===========================================================================================================================
W2 = ["„(2) Ist der Gläubiger für den Umstand, auf Grund dessen der",
      "Schuldner nach § 275 Abs. 1 bis 3 nicht zu leisten braucht, allein",
      "oder weit überwiegend verantwortlich oder tritt dieser vom",
      "Schuldner nicht zu vertretende Umstand zu einer Zeit ein, zu",
      "welcher der Gläubiger im Verzug der Annahme ist, so behält der",
      "Schuldner den Anspruch auf die Gegenleistung. …“"]
w2, w2_y = wortlaut(80, 180, 1100, W2, "§ 326 Abs. 2 Satz 1 BGB", beim("w2", "Ausnahme"), marken=[
    (5, "Schuldner den Anspruch auf die Gegenleistung", beim("w2a", "behält")),
    (1, "allein", beim("w2a", "allein")), (2, "oder weit überwiegend verantwortlich", beim("w2a", "verantwortlich")),
    (3, "Schuldner nicht zu vertretende Umstand", beim("w2b", "vertreten")),
    (4, "im Verzug der Annahme", beim("w2b", "Annahmeverzug"))], size=32)
folie([("w2", "III. Ausnahme › § 326 Abs. 2 Satz 1 BGB"), ("g1", "III. Ausnahme › Grundfall")], rechts_frei([
    *tafel("w2", "III. Ausnahmsweise erhalten?"),
    *w2,
    *neinz("Friedhelm für das Fieber nicht verantwortlich", w2_y + 30, beim("g1", "nicht"), "Bold", 34, x=160),
    *neinz("kein Annahmeverzug: kein Konzert angeboten", w2_y + 95, beim("g2", "kein"), "Bold", 34, x=160),
    zit("§§ 293, 294 BGB", 160, w2_y + 148, beim("g2", "angeboten")),
    blk(110, w2_y + 200, 1040, 80, GRUEN, beim("g3", "nichts"), [("Friedhelm muss nichts mehr zahlen", "ExtraBold", 36, INK)]),
    *requisit([("w2", ("tabler", "user-question", 100, WEISS), "Gläubiger verantwortlich?", WEISS),
               (beim("w2b", "Annahmeverzug"), ("tabler", "door", 90, WEISS), "Annahmeverzug?", WEISS),
               ("g1", ("tabler", "thermometer", 100, ROT), "Fieber: nein", ROT),
               ("g3", ("tabler", "coin-euro", 100, GRUEN), "nichts zahlen", GRUEN)]),
    *paar("w2", [("w2", "ruhig"), ("g1", "krank"), ("g3", "sorge")], [("w2", "ruhig"), ("g1", "denkt"), ("g3", "froh")]),
]))

# ===========================================================================================================================
# I Gegenfall: Friedhelm sagt ab (Theodor zu Hause gesund | Friedhelm mit Koffer)
# ===========================================================================================================================
RUFT2 = beim("gf2", "ruft")
folie([("gf", "Gegenfall · Die Absage"), ("gf3", "Gegenfall · Friedhelm verantwortlich")], [
    boden("gf", x0=40, x1=TRENN - 30), boden("gf", x0=TRENN + 30, x1=1880), trenner("gf"),
    klavier("gf", cx=330, breite=300),
    pl("Gegenfall", 70, 30, "gf", fill=GELB, size=40),
    pl("Theodor ist gesund", 70, 120, beim("gf", "gesund"), fill=GRUEN, size=36),
    pl("Friedhelm verreist spontan", 70, 205, beim("gf2", "verreisen"), fill=WEISS, size=36),
    auf_boden(ficon("tabler", "luggage", 1700, BODEN, 130, beim("gf2", "verreisen"), fuell=ROT)),
    ficon("tabler", "plane-departure", 1790, 560, 130, beim("gf2", "verreisen"), fuell=WEISS),
    *fig("TH", LX_, BODEN, FH, [(beim("gf", "Theodor"), "froh_r"), ("fr3", "staunt_r"), ("gf3", "sorge_r"), ("gf5", "froh_r")]),
    ns("Theodor", LX_, BODEN, beim("gf", "Theodor"), TH_N, d=0.1),
    *fig("FR", RX_, BODEN, FH, [("gf", "ruhig"), (RUFT2, "ernst")], bis="fr3"),
    *redet("FR_ernst_redet", RX_, BODEN, FH, "fr3", "gf3"),
    *fig("FR", RX_, BODEN, FH, [("gf3", "ernst"), ("gf5", "denkt")], erst="cut"),
    ns("Friedhelm", RX_, BODEN, "gf", FR_N, d=0.2),
    blase("sprech", 600, 200, "fr3", 1480, 205, inhalt=["Die Feier fällt aus.", "Ich brauche Sie heute nicht."],
          textsize=34, figur=("FR_ernst_redet", RX_, BODEN, FH), bis="gf3"),
    pl("Konzert wieder unmöglich", 1160, 40, "gf3", fill=ROT, size=34),
    pl("Friedhelm allein verantwortlich", 1160, 130, beim("gf4", "allein"), fill=LILA, size=34),
    pl("Theodor behält: 2.000 €", 70, 290, beim("gf5", "behält"), fill=GELB, size=36),
])
FOLIEN[-1]["els"] += [telefon("TH_froh_r", LX_, 1, RUFT2, bis="gf3", klingeln=True), telefon("FR_ernst", RX_, -1, RUFT2, bis="gf3")]

# ===========================================================================================================================
# J III. § 326 Abs. 2 Satz 2 (Wortlaut), Anrechnung
# ===========================================================================================================================
W22 = ["„Er muss sich jedoch dasjenige anrechnen lassen, was er",
       "infolge der Befreiung von der Leistung erspart oder durch",
       "anderweitige Verwendung seiner Arbeitskraft erwirbt oder",
       "zu erwerben böswillig unterlässt.“"]
w22, w22_y = wortlaut(80, 180, 1100, W22, "§ 326 Abs. 2 Satz 2 BGB", "w22", marken=[
    (0, "anrechnen lassen", beim("w22", "anrechnen")), (1, "erspart", beim("w22", "erspart")),
    (2, "anderweitige Verwendung seiner Arbeitskraft", beim("w22", "anderweitige")),
    (3, "böswillig unterlässt", beim("w22", "böswillig"))], size=34)
folie([("w22", "III. Gegenfall › Anrechnung, § 326 Abs. 2 Satz 2 BGB")], rechts_frei([
    *tafel("w22", "III. Gegenfall: Anrechnung"),
    *w22,
    *okz("erspart: Taxifahrt, 100 €", w22_y + 30, beim("an1", "Taxifahrt"), "Bold", 36, x=160),
    *neinz("kein anderer Auftritt", w22_y + 90, beim("an2", "anderen"), "Bold", 36, x=160),
    z("2.000 € - 100 € = 1.900 €", 160, w22_y + 160, beim("an3", "neunzehnhundert"), "Bold", 38),
    blk(110, w22_y + 230, 1040, 80, GELB, beim("an4", "vierzehnhundert"), [("abzüglich 500 € Anzahlung: 1.400 € offen", "ExtraBold", 36, INK)]),
    *requisit([("w22", ("tabler", "calculator", 100, WEISS), "Anrechnung", WEISS),
               ("an1", ("tabler", "car", 130, GELB), "Taxi: 100 € erspart", GELB),
               ("an2", ("tabler", "calendar-x", 100, WEISS), "kein anderer Auftritt", WEISS),
               ("an3", ("tabler", "coin-euro", 100, GELB), "1.900 €", GELB),
               ("an4", ("tabler", "cash-banknote", 110, GRUEN), "1.400 € offen", GRUEN)]),
    *paar("w22", [("w22", "ruhig"), ("an1", "denkt"), ("an3", "froh")], [("w22", "ernst"), ("an4", "sorge")]),
]))

# ===========================================================================================================================
# K Hinweis § 648 BGB (Werkvertrag: Absage als Kündigung)
# ===========================================================================================================================
folie([("k648", "III. Gegenfall › Kündigung, § 648 BGB")], rechts_frei([
    *tafel("k648", "Achtung: Werkvertrag"),
    z("Absage kann eine Kündigung sein", 110, 190, beim("k648", "Kündigung"), "Bold", 38),
    zit("§ 648 Satz 1 BGB", 110, 250, beim("k648", "Paragraf")),
    *okz("auch dort: Ersparnis wird abgezogen", 330, beim("k648b", "Ersparnis"), "Bold", 36, x=160),
    zit("§ 648 Satz 2 BGB", 160, 385, beim("k648b", "abgezogen")),
    blk(110, 450, 1040, 120, LILA, beim("k648b", "Bundesgerichtshof"), [("BGH, 27.4.2023 – VII ZR 144/22", "ExtraBold", 34, INK),
                                                                        ("Hochzeitsfotografin, Rn. 33, 37, 39", "Bold", 32, INK)]),
    *requisit([("k648", ("tabler", "file-certificate", 100, WEISS), "Werkvertrag", WEISS),
               (beim("k648b", "Bundesgerichtshof"), ("tabler", "camera", 110, WEISS), "Hochzeitsfotografin", LILA)]),
    *paar("k648", [("k648", "denkt"), ("k648b", "ruhig")], [("k648", "ernst"), ("k648b", "denkt")]),
]))

# ===========================================================================================================================
# L IV. § 326 Abs. 4 (Wortlaut), Abs. 5, Abs. 3
# ===========================================================================================================================
W4 = ["„(4) Soweit die nach dieser Vorschrift nicht geschuldete",
      "Gegenleistung bewirkt ist, kann das Geleistete nach den",
      "§§ 346 bis 348 zurückgefordert werden.“"]
w4, w4_y = wortlaut(80, 180, 1100, W4, "§ 326 Abs. 4 BGB", beim("w4", "Paragraf"), marken=[
    (1, "bewirkt", beim("w4", "bewirkt")), (2, "§§ 346 bis 348", beim("w4", "Paragrafen")),
    (2, "zurückgefordert", beim("w4", "zurückgefordert"))], size=34)
folie([("w4", "IV. Die Anzahlung › § 326 Abs. 4 BGB"), ("r3", "IV. Die Anzahlung › Rücktritt, § 326 Abs. 5 BGB"),
       ("r4", "IV. Ersatz › § 326 Abs. 3 BGB")], rechts_frei([
    *tafel("w4", "IV. Die Anzahlung (Grundfall)"),
    *w4,
    *okz("Friedhelm bekommt die 500 € zurück", w4_y + 30, beim("r1", "fünfhundert"), "Bold", 36, x=160),
    z("Rücktritt dafür nicht nötig", 160, w4_y + 90, beim("r2", "Zurücktreten"), size=34),
    z("möglich: Rücktritt, § 326 Abs. 5 BGB, ohne Frist", 160, w4_y + 145, beim("r3", "Absatz"), size=34),
    linienzug([(110, w4_y + 215), (1150, w4_y + 215)], "r4", breite=3),
    z("§ 326 Abs. 3 BGB: Ersatz nach § 285 verlangt?", 110, w4_y + 240, beim("r4", "Verlangt"), "Bold", 34),
    blk(110, w4_y + 305, 1040, 80, BLAU, beim("r4", "bleibt"), [("Gegenleistung bleibt geschuldet", "ExtraBold", 36, INK)]),
    *requisit([("w4", ("tabler", "cash-banknote", 110, GRUEN), "Anzahlung: 500 €", GRUEN),
               ("r1", ("tabler", "receipt-refund", 100, WEISS), "500 € zurück", GRUEN),
               ("r3", ("tabler", "arrow-back-up", 100, WEISS), "Rücktritt", GELB),
               ("r4", ("tabler", "scale", 100, WEISS), "§ 285: Ersatz", WEISS)]),
    *paar("w4", [("w4", "ruhig"), ("r1", "sorge"), ("r4", "denkt")], [("w4", "ruhig"), ("r1", "froh"), ("r4", "denkt")]),
]))

# ===========================================================================================================================
# M Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Reihenfolge")], [
    *tafel("tipp", "Klausurtipp", fill=HELL, h=560),
    warnung_i(150, 225, "tipp", gr=26),
    z("Reihenfolge einhalten:", 200, 200, beim("tipp", "Reihenfolge"), "Bold", 38),
    z("1. Primäranspruch: ausgeschlossen, § 275?", 240, 280, "t1", size=38),
    z("2. Gegenleistung: § 326 Abs. 1", 240, 345, "t2", size=38),
    z("3. Ausnahmen: § 326 Abs. 2", 240, 410, "t3", size=38),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# N Klausurschema
# ===========================================================================================================================
REIHEN = [("k1", "I.", "Anspruch entstanden", "", BLAU, 0),
          ("k2", "II.", "Anspruch untergegangen, § 326 Abs. 1 Satz 1", "", GELB, 0),
          ("k21", "", "Schuldner muss nach § 275 BGB nicht leisten", "", None, 1),
          ("k3", "III.", "ausnahmsweise erhalten, § 326 Abs. 2 Satz 1", "", GRUEN, 0),
          ("k31", "1.", "Gläubiger allein oder weit überwiegend verantwortlich", "", None, 1),
          (beim("k31", "Annahmeverzug"), "2.", "oder Gläubiger im Annahmeverzug", "", None, 1),
          ("k32", "", "abzüglich der Ersparnis, § 326 Abs. 2 Satz 2", "", None, 1),
          ("k4", "IV.", "Rückforderung des Gezahlten, § 326 Abs. 4", "", LILA, 0)]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Klausurschema: Anspruch auf die Gegenleistung"), 110, 90, "sch", 50)]
y = 205
for c, r, kopf, norm, farbe, ebene in REIHEN:
    if ebene == 0:
        els_sch += [karte(110, y, 110, 70, c, fill=farbe, rund=14, schatten=5, rand=4),
                    z(r, 165 - F("ExtraBold", 38).getlength(r) / 2, y + 10, c, "ExtraBold", 38, rechts=1820),
                    z(kopf, 255, y + 10, c, "ExtraBold", 40, rechts=1480 if norm else 1820)]
        hh = 92
    else:
        if r:
            els_sch.append(z(r, 270, y + 4, c, "Bold", 36, rechts=1820))
        els_sch.append(z(kopf, 330, y + 4, c, "Bold", 36, rechts=1820))
        hh = 76
    if norm:
        els_sch.append(zit(norm, 1500, y + (18 if ebene == 0 else 12), c, size=30, rechts=1820))
    y += hh
assert y <= 970, y
folie([("sch", "Klausurschema"), ("k1", "Klausurschema › I. entstanden"), ("k2", "Klausurschema › II. untergegangen"),
       ("k3", "Klausurschema › III. Ausnahme"), ("k4", "Klausurschema › IV. Rückforderung")], els_sch)

# ===========================================================================================================================
# O Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Muss der Schuldner nach § 275 nicht leisten,", 0)], [("entfällt grundsätzlich die Gegenleistung.", "a")]],
                750, 290, 40, "merke", {"a": beim("merke", "entfällt")}),
    *markertext([[("Ist der Gläubiger dafür verantwortlich", "b")], [("oder im Annahmeverzug,", "b")]],
                750, 470, 40, "mk2", {"b": beim("mk2", "verantwortlich")}),
    *markertext([[("behält der Schuldner sie,", 0)], [("abzüglich der Ersparnis.", "c")]],
                750, 650, 40, "mk3", {"c": beim("mk3", "abzüglich")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
