"""Folge 170 · Unmöglichkeit § 275 BGB: Wenn die Leistung nicht mehr geht – Serienstandard Open Peeps (Katzenkönig).
Beispielfall: Waldemar verkauft Adelheid privat seinen Oldtimer (Stückschuld) für 20.000 €; Übergabe und Zahlung am Samstag.
In der Nacht davor brennt der Wagen in der Garage aus (Variante A Blitzschlag, Variante B offene Flamme). Marktwert
25.000 €; die Versicherung zahlt Waldemar 25.000 €.
Szenen laut ../SZENENPLAN.md: A1 Verkauf, A2 Nacht, A3 Am Morgen/Frage, B Sachverhalt, C Aufbau, D § 275 Abs. 1 (Wortlaut),
E I. Unmöglichkeit im Fall, F I. Rechtsfolge/§ 275 Abs. 2, 3, G II. § 326 Abs. 1 Satz 1 (Wortlaut), H II. Ausnahmen
(§ 326 Abs. 2, § 446, § 326 Abs. 5), I III. 1. § 283 Satz 1 (Wortlaut), J III. 1. Subsumtion, K III. 2. § 285 Abs. 1
(Wortlaut), L III. 2. Commodum im Fall, M Lösung (Tabelle), N Klausurtipp (Lexi), O Klausurschema, P Merksatz (Lexi).
Brand nur angedeutet (kleines Flammen- und Rauch-Icon an der Garage), keine Verletzten; Oldtimer als neutrales Auto-Icon.
Handlungsgeräusche: Donner beim Blitz (Variante A), Feuerzeug bei der offenen Flamme (Variante B) (../geraeusche_herkunft.json).
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/hand/okz/
neinz als eigene Kopie aus Folge 116 (gemeinsame Dateien unverändert); neu: garage(), auto(), paar(), Lösungstabelle.
Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_170/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_170/" in n:
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
WA_N, AD_N = BLAU, GRUEN                    # Farben der Namensschilder
PX, PY, PU = 1570, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"WA": "Waldemar", "AD": "Adelheid"}
NFARBE = {"WA": WA_N, "AD": AD_N}
GRAU_A = (150, 150, 150, 255)               # ausgebrannter Wagen
GX = 560                                    # Garage: Mitte
WX, AX = 1250, 1680                         # Fallszenen: Waldemar (blickt nach rechts zu Adelheid), Adelheid (blickt nach links)


def boden(cue, hart_=False):
    e = linienzug([(40, BODEN), (1880, BODEN)], cue, breite=7, farbe=INK)
    return hart(e) if hart_ else e


def garage(cue, w=640, h=360):
    """Garage in Frontansicht (programmatisch: Wand, Satteldach, offenes Tor; Palettenflächen, Tuschekontur)."""
    s = 2
    dach = 120
    im = Image.new("RGBA", ((w + 12) * s, (h + dach + 12) * s))
    dr = ImageDraw.Draw(im)
    o = 6 * s
    dr.rectangle((o + 30 * s, o + dach * s, o + (w - 30) * s, o + (h + dach) * s), fill=WEISS, outline=INK, width=5 * s)
    dr.polygon([(o, o + dach * s + 4), (o + w * s // 2, o), (o + w * s, o + dach * s + 4)], fill=GELB, outline=INK)
    dr.line([(o, o + dach * s + 4), (o + w * s // 2, o), (o + w * s, o + dach * s + 4), (o, o + dach * s + 4)], fill=INK,
            width=6 * s, joint="curve")
    dr.rectangle((o + 90 * s, o + (dach + 70) * s, o + (w - 90) * s, o + (h + dach) * s), fill=(236, 226, 208, 255),
                 outline=INK, width=5 * s)
    im = im.resize((w + 12, h + dach + 12), Image.LANCZOS)
    return El(im, GX - w / 2 - 6, BODEN - h - dach - 6, cue, "cut", 0.0, None, name="garage")


def auto(cue, grau=False, bis=None, anim="cut"):
    """Der Oldtimer als neutrales Auto-Icon (Tabler car, ohne Marke); ausgebrannt grau gefüllt."""
    return ficon("tabler", "car", GX, BODEN - 4, 380, cue, fuell=GRAU_A if grau else LILA,
                 nebenfarbe=GRAU_A if grau else WEISS, bis=bis, anim=anim)


def brand(cue, bis=None):
    """Brand nur angedeutet: kleine Flamme am Dach, darüber etwas Rauch."""
    return [ficon("tabler", "flame", GX + 170, BODEN - 380, 70, cue, fuell=ROT, bis=bis),
            ficon("tabler", "cloud-fog", GX + 175, BODEN - 455, 90, cue, fuell=WEISS, bis=bis)]


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


def paar(c0, wf, af):
    """Tafelszene: Waldemar und Adelheid rechts der Tafel, beide blicken zur Tafel (nach links)."""
    return [*fig("WA", X1, FB, FR, wf), ns(NAME["WA"], X1, FB, c0, WA_N, d=0.1),
            *fig("AD", X2, FB, FR, af, d=0.2), ns(NAME["AD"], X2, FB, c0, AD_N, d=0.3)]


# ===========================================================================================================================
# A1 Fall: der Verkauf
# ===========================================================================================================================
folie([(NULL, "Fall · Der Verkauf")], [
    hart(boden(NULL)), hart(garage(NULL)), auto(NULL),
    pl("Privatverkauf", 70, 30, beim("fall", "privat"), fill=WEISS, size=40),
    pl("genau dieser Wagen", 70, 120, beim("fall", "genau"), fill=LILA, size=36),
    pl("Kaufpreis: 20.000 €", 70, 205, beim("fall", "zwanzigtausend"), fill=GELB, size=36),
    pl("Übergabe und Zahlung: Samstag", 70, 290, "termin", fill=WEISS, size=36),
    ficon("tabler", "calendar-event", 760, 350, 70, "termin", fuell=WEISS),
    *fig("WA", WX, BODEN, FH, [(NULL, "ruhig_r")], bis="wa1", erst="cut"),
    hart(ns("Waldemar", WX, BODEN, NULL, WA_N)),
    *redet("WA_redet_r", WX, BODEN, FH, "wa1", "ad1"),
    peep_voll("WA_froh_r", WX, BODEN, FH, "ad1", anim="cut", bis="nacht"),
    blase("sprech", 600, 240, "wa1", 1200, 210, inhalt=["Am Samstag gehört er Ihnen.", "Bis dahin steht er sicher",
                                                        "in meiner Garage."], textsize=34, figur=("WA_redet_r", WX, BODEN, FH), bis="ad1"),
    *fig("AD", AX, BODEN, FH, [(NULL, "ruhig"), ("wa1", "froh")], bis="ad1", erst="cut"),
    hart(ns("Adelheid", AX, BODEN, NULL, AD_N)),
    *redet("AD_redet", AX, BODEN, FH, "ad1", "nacht"),
    blase("sprech", 560, 200, "ad1", 1560, 200, inhalt=["Gut. Dann bringe ich", "die 20.000 € mit."], textsize=36,
          figur=("AD_redet", AX, BODEN, FH), bis="nacht"),
])

# ===========================================================================================================================
# A2 Fall: die Nacht vor der Übergabe (Variante A Blitz, Variante B offene Flamme)
# ===========================================================================================================================
BRENNT = beim("nacht", "brennt")
AUS = beim("aus", "vollständig")
BLITZ = beim("varA", "Blitz")
FLAMME = beim("varB", "offener")
WB = 1560
folie([("nacht", "Fall · Die Nacht"), ("varA", "Fall · Variante A: Blitzschlag"), ("varB", "Fall · Variante B: offene Flamme")], [
    boden("nacht"), garage("nacht"),
    auto("nacht", bis=AUS),
    auto(AUS, grau=True),
    pl("Nacht vor der Übergabe", 70, 30, beim("nacht", "Nacht"), fill=BLAU, size=40),
    ficon("tabler", "moon-stars", 1000, 230, 120, beim("nacht", "Nacht"), fuell=GELB),
    *brand(BRENNT),
    pl("Oldtimer ausgebrannt", 70, 120, AUS, fill=ROT, size=36),
    pl("Variante A: Blitzschlag", 70, 205, beim("varA", "Variante"), fill=GELB, size=36),
    szene(ficon("tabler", "cloud-bolt", 1000, 450, 150, BLITZ, fuell=WEISS, bis="varB"), "170donner*", 0.45, 0.0),
    pl("Variante B: offene Flamme", 70, 290, beim("varB", "Variante"), fill=ROT, size=36),
    *fig("WA", WB, BODEN, FH, [(beim("varB", "Waldemar"), "ernst")], bis="wa2"),
    ns("Waldemar", WB, BODEN, beim("varB", "Waldemar"), WA_N, d=0.1),
])
_hx, _hy = hand("WA_ernst", WB, BODEN, FH, -1)
FOLIEN[-1]["els"].append(szene(ficon("tabler", "lighter", _hx - 30, _hy + 10, 60, FLAMME, fuell=ROT), "170feuerzeug*", 0.5, 0.0))

# ===========================================================================================================================
# A3 Fall: am Morgen, Versicherung, Frage
# ===========================================================================================================================
VERS = beim("vers", "Versicherung")
folie([("wa2", "Fall · Am Morgen"), ("frage", "Fall · Die Frage")], [
    boden("wa2"), garage("wa2"), auto("wa2", grau=True),
    ficon("tabler", "cloud-fog", GX + 175, BODEN - 455, 90, "wa2", fuell=WEISS),
    *fig("WA", WX, BODEN, FH, [("wa2", "sorge_r")], bis="wa2"),
    *redet("WA_sorge_redet_r", WX, BODEN, FH, "wa2", "ad2"),
    *fig("WA", WX, BODEN, FH, [("ad2", "sorge_r"), (VERS, "denkt_r"), ("frage", "muede_r")], erst="cut"),
    ns("Waldemar", WX, BODEN, "wa2", WA_N, d=0.1),
    blase("sprech", 600, 240, "wa2", 1200, 210, inhalt=["Der Wagen ist ausgebrannt.", "Ich kann ihn Ihnen",
                                                        "nicht mehr geben."], textsize=34, figur=("WA_sorge_redet_r", WX, BODEN, FH), bis="ad2"),
    *fig("AD", AX, BODEN, FH, [("wa2", "sorge")], bis="ad2"),
    *redet("AD_bestimmt", AX, BODEN, FH, "ad2", "vers"),
    *fig("AD", AX, BODEN, FH, [("vers", "staunt"), ("frage", "denkt")], erst="cut"),
    ns("Adelheid", AX, BODEN, "wa2", AD_N, d=0.2),
    blase("sprech", 600, 240, "ad2", 1570, 210, inhalt=["Dann zahle ich auch nichts.", "Aber er war",
                                                        "25.000 € wert!"], textsize=34, figur=("AD_bestimmt", AX, BODEN, FH), bis="vers"),
    pl("Marktwert: 25.000 €", 70, 30, beim("ad2", "fünfundzwanzigtausend"), fill=GELB, size=40),
    pl("Versicherung zahlt Waldemar 25.000 €", 70, 120, VERS, fill=GRUEN, size=36),
    ficon("tabler", "shield-check", 850, 190, 90, VERS, fuell=GRUEN),
    pl("Muss Waldemar noch liefern, muss Adelheid noch zahlen?", 70, 205, "frage", fill=PINK, size=34),
    pl("Und was kann sie verlangen?", 70, 290, "frage2", fill=WEISS, size=34),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_170(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=34, zeilenabstand=1.30)
        els += e; y += 18
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_170("sv", [
    "Waldemar verkauft Adelheid privat seinen Oldtimer, genau diesen einen Wagen, für 20.000 Euro. Übergabe und Zahlung "
    "sollen am Samstag sein. Bis dahin steht der Wagen in der Garage von Waldemar.",
    "In der Nacht vor der Übergabe brennt es in der Garage; der Oldtimer brennt vollständig aus. Variante A: Ein Blitz "
    "hat eingeschlagen. Variante B: Waldemar hat am Abend in der Garage mit offener Flamme hantiert.",
    "Der Wagen war 25.000 Euro wert. Die Versicherung zahlt Waldemar für den Wagen 25.000 Euro. Adelheid will nichts "
    "zahlen und fragt, was sie verlangen kann.",
], "Muss Waldemar noch liefern, muss Adelheid noch zahlen – und was kann sie verlangen?")

# ===========================================================================================================================
# C Aufbau: drei Schritte
# ===========================================================================================================================
SCHRITTE = [("p1", "I.", "Anspruch auf den Wagen", BLAU), ("p2", "II.", "Kaufpreis", GELB),
            ("p3", "III.", "Ansprüche auf Ersatz", GRUEN)]
folie([("plan", "Unmöglichkeit, § 275 BGB › Aufbau")], rechts_frei([
    *tafel("plan", "Unmöglichkeit: drei Schritte"),
    *[e for k, (c, r, t, fa) in enumerate(SCHRITTE) for e in (
        karte(130, 220 + k * 150, 110, 90, c, fill=fa, rund=14, schatten=5, rand=4),
        z(r, 185 - F("ExtraBold", 40).getlength(r) / 2, 240 + k * 150, c, "ExtraBold", 40),
        z(t, 280, 240 + k * 150, c, "Bold", 40))],
    *requisit([("plan", ("tabler", "list-numbers", 100, WEISS), "3 Schritte", WEISS),
               ("p1", ("tabler", "car", 130, LILA), "der Wagen", BLAU),
               ("p2", ("tabler", "coin-euro", 100, GELB), "Kaufpreis", GELB),
               ("p3", ("tabler", "shield-check", 100, GRUEN), "Ersatz", GRUEN)]),
    *paar("plan", [("plan", "ruhig"), ("p3", "denkt")], [("plan", "ruhig"), ("p3", "denkt")]),
]))

# ===========================================================================================================================
# D I. § 275 Abs. 1 (Wortlaut)
# ===========================================================================================================================
W275 = ["„(1) Der Anspruch auf Leistung ist ausgeschlossen, soweit",
        "diese für den Schuldner oder für jedermann unmöglich ist.“"]
w275, w275_y = wortlaut(80, 180, 1100, W275, "§ 275 Abs. 1 BGB", beim("w275", "Paragraf"), marken=[
    (0, "ausgeschlossen", beim("w275", "ausgeschlossen")), (1, "für den Schuldner", beim("w275", "Schuldner")),
    (1, "für jedermann", beim("w275", "jedermann")), (1, "unmöglich", beim("w275", "unmöglich"))], size=34)
folie([("w275", "I. Anspruch auf den Wagen › § 275 Abs. 1 BGB")], rechts_frei([
    *tafel("w275", "I. Anspruch auf den Wagen"),
    *w275,
    blk(110, w275_y + 50, 1040, 80, BLAU, beim("w275", "unmöglich"), [("unmöglich: Anspruch ausgeschlossen", "ExtraBold", 36, INK)]),
    *requisit([("w275", ("tabler", "scale", 100, WEISS), "§ 275 Abs. 1", WEISS),
               (beim("w275", "unmöglich"), ("tabler", "car-off", 130, WEISS), "unmöglich", ROT)]),
    *paar("w275", [("w275", "ruhig"), (beim("w275", "unmöglich"), "sorge")], [("w275", "ruhig"), (beim("w275", "unmöglich"), "denkt")]),
]))

# ===========================================================================================================================
# E I. Unmöglichkeit im Fall
# ===========================================================================================================================
folie([("u1", "I. Anspruch auf den Wagen › § 433 Abs. 1 BGB"), ("u2", "I. Unmöglichkeit › Stückschuld"),
       ("u3", "I. Unmöglichkeit › objektiv, subjektiv"), ("u5", "I. Unmöglichkeit › nachträglich")], rechts_frei([
    *tafel("u1", "I. Unmöglichkeit im Fall"),
    *okz("Anspruch auf Übergabe und Übereignung", 185, beim("u1", "Anspruch"), "Bold", 36, x=160),
    zit("§ 433 Abs. 1 BGB", 160, 238, beim("u1", "Paragraf")),
    *okz("Stückschuld: genau dieser Wagen", 295, beim("u2", "Stückschuld"), "Bold", 36, x=160),
    z("kein anderer Wagen zu beschaffen", 160, 348, beim("u2", "Einen"), size=34),
    *okz("objektiv: niemand kann ihn liefern", 425, beim("u3", "niemand"), "Bold", 36, x=160),
    z("subjektiv: nur der Schuldner kann nicht leisten", 160, 478, "u4", size=34),
    *okz("nachträglich: Brand nach Vertragsschluss", 555, beim("u5", "Brand"), "Bold", 36, x=160),
    z("schon vorher? Vertrag trotzdem wirksam,", 160, 625, "u6", size=34),
    z("§ 311a Abs. 1 BGB", 160, 675, beim("u6", "Paragraf"), size=34),
    *requisit([(beim("u1", "Übergabe"), ("tabler", "key", 100, GELB), "Übergabe, Übereignung", WEISS),
               ("u2", ("tabler", "car", 130, LILA), "Stückschuld", LILA),
               ("u3", ("tabler", "car-off", 130, WEISS), "objektiv unmöglich", ROT),
               ("u5", ("tabler", "calendar-event", 100, WEISS), "nachträglich", WEISS),
               ("u6", ("tabler", "file-certificate", 100, WEISS), "§ 311a Abs. 1", WEISS)]),
    *paar("u1", [("u1", "ruhig"), ("u3", "sorge"), ("u6", "denkt")], [("u1", "ruhig"), ("u2", "denkt"), ("u5", "ruhig")]),
]))

# ===========================================================================================================================
# F I. Rechtsfolge: kraft Gesetzes; § 275 Abs. 2, 3 als Einrede
# ===========================================================================================================================
folie([("rf1", "I. Rechtsfolge › kraft Gesetzes"), ("rf2", "I. Rechtsfolge › § 275 Abs. 2, 3 BGB")], rechts_frei([
    *tafel("rf1", "I. Rechtsfolge"),
    blk(110, 180, 1040, 80, BLAU, beim("rf1", "ausgeschlossen"), [("Anspruch ausgeschlossen, kraft Gesetzes", "ExtraBold", 36, INK)]),
    *okz("Waldemar muss sich nicht darauf berufen", 290, beim("rf1", "Waldemar"), size=34, x=160),
    zit("BT-Drucks. 14/6040, S. 129", 160, 340, beim("rf1", "berufen")),
    linienzug([(110, 405), (1150, 405)], "rf2", breite=3),
    z("Anders § 275 Abs. 2 und 3 BGB:", 110, 430, "rf2", "Bold", 36),
    z("Abs. 2: Aufwand im groben Missverhältnis", 150, 495, "rf3", size=34),
    z("zum Leistungsinteresse des Gläubigers", 195, 545, beim("rf3", "Leistungsinteresse"), size=34),
    z("Abs. 3: persönliche Leistung unzumutbar", 150, 610, "rf4", size=34),
    blk(110, 690, 1040, 80, GELB, "rf5", [("Schuldner kann nur verweigern: Einrede", "ExtraBold", 36, INK)]),
    *requisit([("rf1", ("tabler", "scale", 100, WEISS), "kraft Gesetzes", BLAU),
               ("rf2", ("tabler", "hand-stop", 100, WEISS), "Abs. 2, 3", WEISS),
               ("rf5", ("tabler", "hand-stop", 100, GELB), "Einrede", GELB)]),
    *paar("rf1", [("rf1", "ruhig"), ("rf2", "denkt")], [("rf1", "ruhig"), ("rf5", "denkt")]),
]))

# ===========================================================================================================================
# G II. Kaufpreis: § 326 Abs. 1 Satz 1 (Wortlaut)
# ===========================================================================================================================
W326 = ["„Braucht der Schuldner nach § 275 Abs. 1 bis 3 nicht zu",
        "leisten, entfällt der Anspruch auf die Gegenleistung; …“"]
w326, w326_y = wortlaut(80, 180, 1100, W326, "§ 326 Abs. 1 Satz 1 BGB", beim("w326", "Paragraf"), marken=[
    (0, "nicht zu", beim("w326", "nicht")), (1, "entfällt", beim("w326", "entfällt")),
    (1, "Anspruch auf die Gegenleistung", beim("w326", "Anspruch"))], size=34)
folie([("g1", "II. Kaufpreis › § 326 Abs. 1 Satz 1 BGB"), ("g2", "II. Kaufpreis › der Fall")], rechts_frei([
    *tafel("g1", "II. Kaufpreis"),
    *w326,
    *okz("Adelheid muss die 20.000 € nicht zahlen", w326_y + 60, beim("g2", "Adelheid"), "Bold", 36, x=160),
    z("in beiden Varianten", 160, w326_y + 115, beim("g2", "beiden"), size=34),
    *requisit([("g1", ("tabler", "coin-euro", 100, GELB), "Kaufpreis?", GELB),
               (beim("g2", "nicht"), ("tabler", "coin-euro", 100, WEISS), "kein Kaufpreis", GRUEN)]),
    *paar("g1", [("g1", "ruhig"), ("g2", "sorge")], [("g1", "ruhig"), ("g2", "froh")]),
]))

# ===========================================================================================================================
# H II. Ausnahmen: § 326 Abs. 2, § 446, Rücktritt § 326 Abs. 5
# ===========================================================================================================================
folie([("g3", "II. Kaufpreis › Ausnahmen, § 326 Abs. 2 BGB"), ("g4", "II. Kaufpreis › Gefahrübergang, § 446 BGB"),
       ("g5", "II. Kaufpreis › Rücktritt, § 326 Abs. 5 BGB")], rechts_frei([
    *tafel("g3", "II. Ausnahmen"),
    z("§ 326 Abs. 2 BGB: Schuldner behält den Kaufpreis,", 110, 180, beim("g3", "Ausnahme"), "Bold", 34),
    z("Gläubiger allein oder weit überwiegend verantwortlich", 150, 235, beim("g3", "Gläubiger"), size=33),
    z("oder Umstand im Annahmeverzug des Gläubigers", 150, 285, "g3b", size=33),
    *neinz("beides liegt hier nicht vor", 340, "g3f", "Bold", 34, x=195),
    linienzug([(110, 410), (1150, 410)], "g4", breite=3),
    z("§ 446 BGB: Gefahr geht erst mit der Übergabe über", 110, 435, beim("g4", "Paragraf"), "Bold", 34),
    *neinz("Wagen noch nicht übergeben", 495, "g4f", "Bold", 34, x=195),
    blk(110, 580, 1040, 80, GELB, "g5", [("Rücktritt: § 326 Abs. 5 BGB, ohne Frist", "ExtraBold", 36, INK)]),
    blk(110, 690, 1040, 80, LILA, beim("g5", "dazu"), [("Mehr dazu: Video „Rücktritt § 323 BGB“", "ExtraBold", 34, INK)]),
    *requisit([("g3", ("tabler", "user-question", 100, WEISS), "Gläubiger verantwortlich?", WEISS),
               ("g4", ("tabler", "key", 100, GELB), "Übergabe?", WEISS),
               ("g5", ("tabler", "arrow-back-up", 100, WEISS), "Rücktritt", GELB)]),
    *paar("g3", [("g3", "ruhig"), ("g4", "denkt")], [("g3", "ruhig"), ("g3f", "froh")]),
]))

# ===========================================================================================================================
# I III. 1. Schadensersatz statt der Leistung: § 283 Satz 1 (Wortlaut)
# ===========================================================================================================================
W283 = ["„Braucht der Schuldner nach § 275 Abs. 1 bis 3 nicht zu",
        "leisten, kann der Gläubiger unter den Voraussetzungen",
        "des § 280 Abs. 1 Schadensersatz statt der Leistung",
        "verlangen.“"]
w283, w283_y = wortlaut(80, 180, 1100, W283, "§ 283 Satz 1 BGB", beim("w283", "Paragraf"), marken=[
    (1, "unter den Voraussetzungen", beim("w283", "Voraussetzungen")), (2, "des § 280 Abs. 1", beim("w283", "Paragrafen")),
    (2, "Schadensersatz statt der Leistung", beim("w283", "Schadensersatz"))], size=34)
folie([("s1", "III. 1. Schadensersatz › § 283 Satz 1 BGB")], rechts_frei([
    *tafel("s1", "III. 1. Schadensersatz"),
    *w283,
    blk(110, w283_y + 50, 1040, 80, LILA, "s046", [("Mehr dazu: Video „Das System der §§ 280 ff.“", "ExtraBold", 34, INK)]),
    *requisit([("s1", ("tabler", "scale", 100, WEISS), "statt der Leistung", WEISS),
               ("s046", ("tabler", "list-numbers", 100, WEISS), "das System", LILA)]),
    *paar("s1", [("s1", "ruhig"), (beim("w283", "Schadensersatz"), "sorge")], [("s1", "ruhig"), (beim("w283", "Schadensersatz"), "denkt")]),
]))

# ===========================================================================================================================
# J III. 1. Subsumtion: Pflichtverletzung, Vertretenmüssen, Varianten
# ===========================================================================================================================
folie([("s2", "III. 1. Schadensersatz › Pflichtverletzung"), ("s3", "III. 1. Schadensersatz › Vertretenmüssen"),
       ("vb", "III. 1. Schadensersatz › Variante B"), ("va", "III. 1. Schadensersatz › Variante A")], rechts_frei([
    *tafel("s2", "III. 1. §§ 280 Abs. 1, 3, 283 BGB", size=44),
    *okz("Pflichtverletzung: Waldemar leistet nicht", 180, beim("s2", "Waldemar"), "Bold", 36, x=160),
    z("Vertretenmüssen vermutet,", 160, 250, beim("s3", "Vertretenmüssen"), size=34),
    z("§ 280 Abs. 1 Satz 2 BGB: Waldemar muss sich entlasten", 160, 300, beim("s3", "Paragraf"), size=33),
    blk(110, 365, 1040, 75, LILA, "s141", [("Mehr dazu: Videos „Beweislast“, „Anscheinsbeweis“", "ExtraBold", 32, INK)]),
    *okz("Variante B: offene Flamme, fahrlässig", 480, beim("vb", "fahrlässig"), "Bold", 36, x=160),
    z("Wertdifferenz: 25.000 € - 20.000 € = 5.000 €", 160, 540, beim("vb2", "fünfundzwanzigtausend"), size=34),
    blk(110, 600, 1040, 75, GRUEN, beim("vb2", "fünftausend"), [("Variante B: 5.000 € Schadensersatz", "ExtraBold", 34, INK)]),
    *neinz("Variante A: Blitzschlag nicht zu vertreten", 715, beim("va", "Blitzschlag"), "Bold", 36, x=160),
    z("kein Schadensersatz", 160, 770, beim("va", "kein"), size=34),
    *requisit([("s2", ("tabler", "car-off", 130, WEISS), "nicht geleistet", ROT),
               ("s3", ("tabler", "scale", 100, WEISS), "Vertretenmüssen?", WEISS),
               ("vb", ("tabler", "lighter", 80, ROT), "B: fahrlässig", ROT),
               (beim("vb2", "fünftausend"), ("tabler", "coin-euro", 100, GELB), "5.000 €", GELB),
               ("va", ("tabler", "cloud-bolt", 120, WEISS), "A: Blitzschlag", WEISS)]),
    *paar("s2", [("s2", "ruhig"), ("s3", "denkt"), ("vb", "sorge"), ("va", "froh")],
          [("s2", "ruhig"), ("vb", "bestimmt"), ("va", "sorge")]),
]))

# ===========================================================================================================================
# K III. 2. Stellvertretendes Commodum: § 285 Abs. 1 (Wortlaut)
# ===========================================================================================================================
W285 = ["„(1) Erlangt der Schuldner infolge des Umstands, auf Grund",
        "dessen er die Leistung nach § 275 Abs. 1 bis 3 nicht zu",
        "erbringen braucht, für den geschuldeten Gegenstand einen",
        "Ersatz oder einen Ersatzanspruch, so kann der Gläubiger",
        "Herausgabe des als Ersatz Empfangenen oder Abtretung",
        "des Ersatzanspruchs verlangen.“"]
w285, w285_y = wortlaut(80, 180, 1100, W285, "§ 285 Abs. 1 BGB", beim("w285", "Paragraf"), marken=[
    (0, "infolge des Umstands", beim("w285", "Umstands")), (2, "für den geschuldeten Gegenstand", beim("w285", "geschuldeten")),
    (3, "Ersatz oder einen Ersatzanspruch", beim("w285", "Ersatz")), (4, "Herausgabe", beim("w285", "Herausgabe")),
    (4, "Abtretung", beim("w285", "Abtretung"))], size=33)
folie([("c1", "III. 2. Stellvertretendes Commodum › § 285 Abs. 1 BGB")], rechts_frei([
    *tafel("c1", "III. 2. Stellvertretendes Commodum", size=42),
    *w285,
    *requisit([("c1", ("tabler", "bulb", 100, GELB), "Klausurclou", GELB),
               (beim("w285", "Ersatz"), ("tabler", "shield-check", 100, GRUEN), "Ersatz", GRUEN)]),
    *paar("c1", [("c1", "ruhig"), (beim("w285", "Ersatz"), "denkt")], [("c1", "ruhig"), (beim("w285", "Herausgabe"), "staunt")]),
]))

# ===========================================================================================================================
# L III. 2. Commodum im Fall
# ===========================================================================================================================
folie([("c2", "III. 2. Commodum › Versicherung"), ("c4", "III. 2. Commodum › Gegenleistung, § 326 Abs. 3 BGB"),
       ("c7", "III. 2. Commodum › Variante B, § 285 Abs. 2 BGB")], rechts_frei([
    *tafel("c2", "III. 2. Commodum im Fall"),
    *okz("Zahlung der Versicherung: Ersatz", 180, beim("c2", "Zahlung"), "Bold", 36, x=160),
    zit("BT-Drucks. 14/6040, S. 144: Anspruch auf eine Versicherungsleistung", 160, 233, beim("c2", "Gesetzesbegründung")),
    *okz("kein Vertretenmüssen nötig: auch Variante A", 290, "c3", "Bold", 36, x=160),
    z("Adelheid verlangt die 25.000 €", 160, 380, "c4", size=36),
    z("und zahlt die 20.000 €, § 326 Abs. 3 Satz 1 BGB", 160, 435, beim("c5", "Paragraf"), size=34),
    blk(110, 510, 1040, 80, GRUEN, "c6", [("unterm Strich: 5.000 € für Adelheid", "ExtraBold", 36, INK)]),
    z("Variante B: Schadensersatz mindert sich", 160, 630, "c7", "Bold", 34),
    z("um den Wert des Ersatzes, § 285 Abs. 2 BGB", 160, 680, beim("c7", "Wert"), size=34),
    *requisit([("c2", ("tabler", "shield-check", 100, GRUEN), "Versicherungszahlung", GRUEN),
               ("c4", ("tabler", "cash-banknote", 110, GRUEN), "25.000 € an Adelheid", WEISS),
               ("c5", ("tabler", "coin-euro", 100, GELB), "20.000 € an Waldemar", GELB),
               ("c6", ("tabler", "calculator", 100, WEISS), "5.000 €", GRUEN),
               ("c7", ("tabler", "scale", 100, WEISS), "§ 285 Abs. 2", WEISS)]),
    *paar("c2", [("c2", "ruhig"), ("c4", "sorge"), ("c5", "froh"), ("c7", "denkt")],
          [("c2", "staunt"), ("c4", "froh"), ("c5", "denkt"), ("c6", "froh")]),
]))

# ===========================================================================================================================
# M Lösung beider Varianten (Tabelle)
# ===========================================================================================================================
TX0, TXA, TXB = 110, 560, 860
TY = [300, 395, 490, 585]
ZEILEN = [("l1", "Wagen, § 275 Abs. 1", ("ausgeschlossen", 0), ("ausgeschlossen", 0)),
          ("l2", "Kaufpreis, § 326 Abs. 1", ("entfällt", 0), ("entfällt", 0)),
          ("l3", "Schadensersatz, § 283", ("nein", -1), ("5.000 €", 1)),
          ("l4", "Ersatz, § 285", ("ja, aber zahlen", 1), ("ja, aber zahlen", 1))]
els_l = [*tafel("loes", "Die Lösung"),
         blk(TXA - 10, 190, 280, 75, GELB, "loes", [("Variante A", "ExtraBold", 32, INK)]),
         blk(TXB - 10, 190, 290, 75, ROT, "loes", [("Variante B", "ExtraBold", 32, INK)])]
for (c, kopf, a, b), y in zip(ZEILEN, TY):
    els_l.append(z(kopf, TX0, y, c, "Bold", 32))
    for (txt, wert), x in ((a, TXA), (b, TXB)):
        if wert > 0:
            els_l.append(ok(x - 2, y + 18, c, gr=18)); x += 40
        elif wert < 0:
            els_l.append(nein(x - 2, y + 18, c, gr=18)); x += 40
        els_l.append(z(txt, x, y, c, size=32))
    els_l.append(linienzug([(TX0, y + 70), (1150, y + 70)], c, breite=2))
folie([("loes", "Lösung › beide Varianten")], rechts_frei([
    *els_l,
    *requisit([("loes", ("tabler", "table", 100, WEISS), "beide Varianten", WEISS),
               ("l3", ("tabler", "coin-euro", 100, GELB), "nur B: 5.000 €", GELB),
               ("l4", ("tabler", "shield-check", 100, GRUEN), "Versicherung", GRUEN)]),
    *paar("loes", [("loes", "ruhig"), ("l3", "sorge")], [("loes", "ruhig"), ("l2", "froh"), ("l4", "denkt")]),
]))

# ===========================================================================================================================
# N Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Reihenfolge")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Reihenfolge einhalten:", 200, 200, beim("tipp", "Reihenfolge"), "Bold", 38),
    z("1. Primäranspruch", 240, 280, "t1", size=38),
    z("2. Gegenleistung", 240, 345, "t2", size=38),
    z("3. Schadensersatz und Commodum", 240, 410, "t3", size=38),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# O Klausurschema
# ===========================================================================================================================
REIHEN = [("k1", "I.", "Anspruch auf Übergabe und Übereignung", "§ 433 Abs. 1 BGB", BLAU, 0),
          ("k11", "", "ausgeschlossen nach § 275 Abs. 1 BGB", "", None, 1),
          ("k2", "II.", "Anspruch auf den Kaufpreis", "", GELB, 0),
          (beim("k2", "entfallen"), "", "entfallen nach § 326 Abs. 1 BGB", "", None, 1),
          ("k21", "", "Ausnahmen: § 326 Abs. 2 BGB", "", None, 1),
          ("k3", "III.", "Sekundäransprüche", "", GRUEN, 0),
          ("k31", "1.", "Schadensersatz statt der Leistung, mit Vertretenmüssen", "§§ 280, 283", None, 1),
          ("k32", "2.", "Herausgabe des Ersatzes, mit Gegenleistung", "§§ 285, 326 III", None, 1)]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Klausurschema: Unmöglichkeit, § 275 BGB"), 110, 90, "sch", 50)]
y = 205
for c, r, kopf, norm, farbe, ebene in REIHEN:
    if ebene == 0:
        els_sch += [karte(110, y, 110, 70, c, fill=farbe, rund=14, schatten=5, rand=4),
                    z(r, 165 - F("ExtraBold", 38).getlength(r) / 2, y + 10, c, "ExtraBold", 38, rechts=1820),
                    z(kopf, 255, y + 10, c, "ExtraBold", 40, rechts=1820)]
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
folie([("sch", "Klausurschema"), ("k1", "Klausurschema › I. Primäranspruch"), ("k2", "Klausurschema › II. Kaufpreis"),
       ("k3", "Klausurschema › III. Sekundäransprüche")], els_sch)

# ===========================================================================================================================
# P Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Ist die Leistung unmöglich,", 0)], [("fällt der Anspruch weg", "a")]],
                750, 290, 44, "merke", {"a": beim("merke", "fällt")}),
    *markertext([[("und mit ihm grundsätzlich", 0)], [("der Kaufpreis.", "b")]],
                750, 450, 42, "mk2", {"b": beim("mk2", "Kaufpreis")}),
    *markertext([[("Schadensersatz gibt es nur", "c")], [("bei Vertretenmüssen,", "c")]],
                750, 590, 40, "mk3", {"c": beim("mk3", "Schadensersatz")}),
    *markertext([[("den Ersatz nach § 285 auch ohne.", "d")]],
                750, 760, 40, "mk4", {"d": beim("mk4", "Ersatz")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
