"""Folge 166 · Trierer Weinversteigerung: Erklärungsbewusstsein beim Winken? – Serienstandard Open Peeps (Katzenkönig).
Fiktiver Fall im Versteigerungssaal (Frau Haller, Auktionatorin; Ekkehard, winkt; Reinhild, an der Tür), danach der
Lehrbuchfall (Isay 1899) und der BGH-Fall BGHZ 91, 324 (Sparkasse, ohne Figuren). Szenen laut ../SZENENPLAN.md.
Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz als eigene Kopie aus Folge 146 (gemeinsame
Dateien unverändert); neu: saal(), requisit()/stehend()/paar() mit Folge-166-Namen. Wein nur als Fass-Icon.
Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from ostil import titel, karte, pille
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_166/"

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
        if n.startswith(("bild:", "ficon:", "bank")) or "/op_166/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def wortlaut(x, y, w, zeilen, quelle, cue, marken=(), size=32, bis=None):
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 04.10.2026, Folge 166), als Zitat mit Normangabe;
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
def _flaeche(w, h):
    s = 2
    im = Image.new("RGBA", ((w + 12) * s, (h + 12) * s))
    return im, ImageDraw.Draw(im), s



BODEN = 860
FH = 440                                    # stehende Figur in der Saalszene
X1, X2 = 1430, 1730                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"EK": "Ekkehard", "HA": "Frau Haller", "RE": "Reinhild"}
NFARBE = {"EK": BLAU, "HA": TUERKIS, "RE": ORANGE}


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


# ===========================================================================================================================
# A1 Fall: die Weinversteigerung (fiktiv) – Saal mit Pult, Fass und Tür
# ===========================================================================================================================
HAX, PUX, FAX, EKX, TUX = 230, 455, 700, 1060, 1660


def saal(cue):
    """Grundbild des Saals: Boden, Pult, Fass (nur Icon), Saaltür."""
    return [boden(cue),
            hart(ficon("tabler", "podium", PUX, BODEN, 200, cue, fuell=HOLZ, anim="cut")),
            hart(ficon("tabler", "barrel", FAX, BODEN, 190, cue, fuell=HOLZ, anim="cut")),
            hart(ficon("tabler", "door", TUX, BODEN, 360, cue, fuell=BLAUHELL, anim="cut"))]


H2Z = beim("h2", "zugeschlagen")
folie([(NULL, "Fall · Die Weinversteigerung"), ("h2", "Fall · Der Zuschlag"), ("e1", "Fall · Der Widerspruch")], [
    *saal(NULL),
    hart(pl("Weinversteigerung", 60, 40, NULL, fill=GELB, size=34)),
    pl("Wer die Hand hebt, bietet.", 470, 40, "regel", fill=WEISS, size=32, bis="h1"),
    ficon("tabler", "hand-stop", 1000, 150, 100, beim("regel", "Hand"), fuell=GELB, bis="h1"),
    # Frau Haller am Pult, blickt nach rechts in den Saal
    *fig("HA", HAX, BODEN, FH, [("haller", "ruhig_r")], bis="h1"),
    *redet("HA_redet_r", HAX, BODEN, FH, "h1", "ekke"),
    *fig("HA", HAX, BODEN, FH, [("ekke", "ruhig_r")], bis="h2", erst="cut"),
    *redet("HA_redet_r", HAX, BODEN, FH, "h2", "e1"),
    *fig("HA", HAX, BODEN, FH, [("e1", "denkt_r")], erst="cut"),
    ns("Frau Haller", HAX, BODEN, "haller", TUERKIS, d=0.1),
    pl("Auktionatorin, eigener Weinkeller", 60, 120, beim("haller", "versteigert"), fill=WEISS, size=28, bis="h1"),
    pl("1 Fass Riesling", FAX, 580, "h1", fill=WEISS, size=30, anker="m"),
    pl("Gebot: 850 €", FAX, 500, beim("h1", "Achthundertfünfzig"), fill=GELB, size=30, anker="m", bis="h2"),
    pl("Gebot: 900 €", FAX, 500, "h2", fill=GELB, size=30, anker="m"),
    blase("sprech", 600, 210, "h1", 640, 250, inhalt=["Ein Fass Riesling.", "850 € sind geboten.",
                                                  "Wer bietet 900?"], textsize=31,
          figur=("HA_redet_r", HAX, BODEN, FH), bis="ekke"),
    blase("sprech", 660, 210, "h2", 660, 250, inhalt=["900 € vom Herrn in der Mitte!", "Zum Ersten, zum Zweiten,",
                                                  "und zugeschlagen!"], textsize=31,
          figur=("HA_redet_r", HAX, BODEN, FH), bis="e1"),
    szene(ficon("tabler", "gavel", PUX + 10, BODEN - 196, 120, H2Z, fuell=HOLZ, anim="cut"), "166hammer*", 0.9, 0.0),
    # Ekkehard in der Mitte: blickt zu Frau Haller (links), entdeckt Reinhild (rechts), winkt, staunt, redet
    *fig("EK", EKX, BODEN, FH, [("ekke", "ruhig"), ("rein", "froh_r"), ("wink", "winkt_r"), (H2Z, "staunt")],
         bis="e1"),
    *redet("EK_redet", EKX, BODEN, FH, "e1", "p156"),
    ns("Ekkehard", EKX, BODEN, "ekke", BLAU, d=0.1),
    pl("nur zum Zusehen da", EKX, 360, beim("ekke", "zuzusehen"), fill=WEISS, size=28, anker="m", bis="rein"),
    pl("winkt seiner Freundin zu", 1330, 300, beim("wink", "zuzuwinken"), fill=HELL, size=28, anker="m", bis="h2"),
    blase("sprech", 660, 210, "e1", 1330, 250, inhalt=["Moment! Ich habe nicht geboten.", "Ich habe nur meiner",
                                                   "Freundin zugewinkt!"], textsize=31,
          figur=("EK_redet", EKX, BODEN, FH), bis="p156"),
    # Reinhild kommt an die Tür, blickt nach links zu Ekkehard
    bewegt(peep_voll("RE_ruhig", TUX, BODEN, FH, "rein", anim="cut", bis="wink"), "rein", ("rein", 1.0), 90, 0),
    *fig("RE", TUX, BODEN, FH, [("wink", "froh"), (H2Z, "staunt")], erst="cut"),
    bewegt(ns("Reinhild", TUX, BODEN, "rein", ORANGE, anim="cut"), "rein", ("rein", 1.0), 90, 0),
])

# ===========================================================================================================================
# A2 Die Frage: § 156 BGB
# ===========================================================================================================================
W156 = ["„Bei einer Versteigerung kommt der Vertrag erst durch",
        "den Zuschlag zustande. …“"]
w156, w156_y = wortlaut(80, 190, 1100, W156, "§ 156 Satz 1 BGB", "p156", marken=[
    (1, "Zuschlag", beim("p156", "Zuschlag"))], size=34)
folie([("p156", "Die Frage · § 156 BGB: Vertrag durch Zuschlag"), ("frage", "Die Frage · War das Winken ein Gebot?")], [
    *tafel("p156", "Wann kommt der Vertrag zustande?"),
    *w156,
    pl("War Ekkehards Winken ein Gebot?", 110, w156_y + 50, "frage", fill=PINK, size=36),
    z("obwohl er nicht daran dachte, etwas zu erklären", 110, w156_y + 140, beim("frage", "obwohl"), "Bold", 34),
    *requisit([("p156", ("tabler", "gavel", 110, HOLZ), "Zuschlag", WEISS),
               ("frage", ("tabler", "hand-stop", 100, GELB), "Gebot?", PINK)]),
    *paar("EK", [("p156", "denkt"), ("frage", "sorge")], "HA", [("p156", "ernst")]),
])

# ===========================================================================================================================
# A3 Der Klassiker: Lehrbuchfall 1899 und BGHZ 91, 324 (ohne Figuren; reale Beteiligte nicht dargestellt)
# ===========================================================================================================================
folie([("klassiker", "Der Klassiker · Lehrbuchfall von 1899"), ("bgh", "Der Klassiker · BGH, 7.6.1984: die Sparkasse")], [
    *tafel("klassiker", "Die Trierer Weinversteigerung"),
    blk(110, 180, 1040, 80, GELB, "klassiker", [("ein klassischer Lehrbuchfall von 1899", "ExtraBold", 34, INK)]),
    zit("H. Isay, Die Willenserklärung im Thatbestande des Rechtsgeschäfts, 1899, S. 25", 110, 275, "klassiker"),
    *neinz("kein Gerichtsfall", 330, beim("klassiker", "kein"), "Bold", 34, x=160),
    blk(110, 420, 1040, 80, BLAUHELL, "bgh", [("BGH, Urteil vom 7.6.1984 (1984)", "ExtraBold", 34, INK)]),
    zit("IX ZR 66/83, BGHZ 91, 324 – ein anderer Fall", 110, 515, "bgh"),
    z("Sparkasse an eine Firma:", 110, 575, "spk", "Bold", 34),
    z("„… die selbstschuldnerische Bürgschaft … übernommen.“", 110, 625, beim("spk", "Bürgschaft"), size=33),
    zit("Schreiben vom 8.9.1981, BGHZ 91, 324, 325", 110, 675, beim("spk", "Bürgschaft")),
    pl("gewollt: nur eine Mitteilung, keine Bürgschaft", 110, 740, "mitt", fill=HELLROT, size=32),
    zit("BGHZ 91, 324, 327", 110, 815, "mitt"),
    *requisit([("klassiker", ("tabler", "book", 150, GELB), "Lehrbuch, 1899", GELB),
               ("bgh", ("tabler", "building-bank", 170, WEISS), "Bundesgerichtshof", BLAUHELL),
               ("spk", ("tabler", "mail", 160, WEISS), "Brief der Sparkasse", WEISS)], pu=640, py=260),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_166(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=36, zeilenabstand=1.3)
        els += e; y += 20
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=36))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_166("sv", [
    "Auktionatorin Frau Haller versteigert Fässer aus ihrem eigenen Weinkeller. Im Saal gilt: Wer die Hand hebt, "
    "bietet. Für ein Fass Riesling sind 850 € geboten. Ekkehard ist nur zum Zusehen mitgekommen. Als er an der Tür "
    "seine Freundin Reinhild entdeckt, hebt er die Hand, um ihr zuzuwinken.",
    "Frau Haller hält das für ein Gebot über 900 € und erteilt Ekkehard den Zuschlag. Sofort ruft er: „Moment! Ich "
    "habe nicht geboten. Ich habe nur meiner Freundin zugewinkt!“ Frau Haller verlangt 900 €.",
], "Muss Ekkehard zahlen?")

# ===========================================================================================================================
# C1 Tatbestand der Willenserklärung: Anspruch, objektiv/subjektiv
# ===========================================================================================================================
PI = "I. Willenserklärung"
folie([("tb", f"{PI} · Anspruch auf 900 €"), ("ot", f"{PI} · objektiv und subjektiv"),
       ("ausl", f"{PI} › objektiver Tatbestand")], [
    *tafel("tb", "Frau Haller verlangt 900 €"),
    zit("§ 433 Abs. 2 BGB", 110, 168, "tb"),
    z("nötig: ein Kaufvertrag,", 110, 225, beim("tb", "Kaufvertrag"), "Bold", 36),
    z("also ein Gebot von Ekkehard", 110, 275, beim("tb", "Gebot"), "Bold", 36),
    blk(110, 360, 505, 120, GELB, beim("ot", "objektiven"), [("objektiver", "ExtraBold", 34, INK),
                                                          ("Tatbestand", "ExtraBold", 34, INK)]),
    blk(645, 360, 505, 120, LILA, beim("ot", "subjektiven"), [("subjektiver", "ExtraBold", 34, INK),
                                                           ("Tatbestand", "ExtraBold", 34, INK)]),
    *okz("objektiv: Wie durfte der Empfänger", 530, "ausl", "Bold", 36, x=160),
    z("das Verhalten verstehen?", 160, 580, beim("ausl", "Empfänger"), "Bold", 36),
    zit("vgl. BGHZ 91, 324, 327, 330", 160, 632, beim("ausl", "Empfänger")),
    *requisit([("tb", ("tabler", "coins", 100, GELB), "Kaufpreis: 900 €", GELB),
               ("ot", ("tabler", "scale", 100, WEISS), "Tatbestand", WEISS),
               ("ausl", ("tabler", "eye", 100, BLAUHELL), "Sicht des Empfängers", BLAUHELL)]),
    *paar("EK", [("tb", "sorge"), ("ausl", "denkt")], "HA", [("tb", "ruhig"), ("ot", "denkt")]),
])

# ===========================================================================================================================
# C1b Auslegung §§ 133, 157 BGB (Wortlautkarten) und Subsumtion objektiv
# ===========================================================================================================================
W133 = ["„Bei der Auslegung einer Willenserklärung ist der wirkliche",
        "Wille zu erforschen und nicht an dem buchstäblichen Sinne",
        "des Ausdrucks zu haften.“"]
W157 = ["„Verträge sind so auszulegen, wie Treu und Glauben mit",
        "Rücksicht auf die Verkehrssitte es erfordern.“"]
w133, w133_y = wortlaut(80, 160, 1100, W133, "§ 133 BGB", "p133", marken=[
    (0, "wirkliche", beim("p133", "wirkliche")), (1, "Wille zu erforschen", beim("p133", "wirkliche"))], size=31)
w157, w157_y = wortlaut(80, w133_y + 20, 1100, W157, "§ 157 BGB", "p157", marken=[
    (0, "Treu und Glauben", beim("p157", "Treu")), (1, "Verkehrssitte", beim("p157", "Verkehrssitte"))], size=31)
folie([("p133", f"{PI} › Auslegung, §§ 133, 157 BGB"), ("saal", f"{PI} › erhobene Hand im Saal"),
       ("objok", f"{PI} › objektiv: Gebot (+)")], [
    *tafel("p133", "Auslegung: §§ 133, 157 BGB"),
    *w133, *w157,
    z("Im Saal heißt die erhobene Hand:", 110, w157_y + 30, "saal", "Bold", 34),
    z("„Ich biete mehr.“", 110, w157_y + 78, beim("saal", "Ich"), "ExtraBold", 36),
    *okz("objektiv: Gebot (+)", w157_y + 150, "objok", "ExtraBold", 36, x=160),
    *requisit([("p133", ("tabler", "book", 100, WEISS), "Auslegung", WEISS),
               ("saal", ("tabler", "hand-stop", 100, GELB), "Hand gehoben", GELB),
               ("objok", ("tabler", "circle-check", 100, GRUEN), "Gebot (+)", GRUEN)]),
    *paar("EK", [("p133", "denkt"), ("objok", "sorge")], "HA", [("p133", "ruhig"), ("objok", "froh")]),
])

# ===========================================================================================================================
# C2 Subjektiver Tatbestand
# ===========================================================================================================================
folie([("st", f"{PI} › subjektiver Tatbestand"), ("hw", f"{PI} › Handlungswille (+)"),
       ("eb", f"{PI} › Erklärungsbewusstsein"), ("ebn", f"{PI} › Erklärungsbewusstsein fehlt"),
       ("gw", f"{PI} › Geschäftswille fehlt"), ("frage2", f"{PI} › ohne Erklärungsbewusstsein?")], [
    *tafel("st", "Der subjektive Tatbestand: drei Elemente"),
    *okz("Handlungswille: Hand bewusst gehoben,", 185, "hw", "Bold", 34, x=160),
    z("kein Reflex", 160, 233, beim("hw", "Reflex"), size=34),
    z("Erklärungsbewusstsein: Bewusstsein, überhaupt", 160, 310, "eb", "Bold", 34),
    z("eine rechtsgeschäftliche Erklärung abzugeben", 160, 358, beim("eb", "rechtsgeschäftliche"), size=34),
    *neinz("fehlt: Er wollte nur winken.", 415, "ebn", "ExtraBold", 34, x=160),
    *neinz("Geschäftswille: ein bestimmtes Geschäft", 500, "gw", "Bold", 34, x=160),
    z("schließen – fehlt erst recht", 160, 548, beim("gw", "Den"), size=34),
    pl("Willenserklärung ohne Erklärungsbewusstsein?", 110, 640, "frage2", fill=PINK, size=36),
    *requisit([("hw", ("tabler", "hand-stop", 100, GELB), "Handlungswille", GELB),
               ("ebn", ("tabler", "mood-confused", 100, HELLROT), "nur gewinkt", HELLROT),
               ("frage2", ("tabler", "help", 100, PINK), "Willenserklärung?", PINK)]),
    *stehend("EK", FX, [("st", "ruhig"), ("ebn", "denkt"), ("frage2", "sorge")]),
])

# ===========================================================================================================================
# D1 Der Streit: Willenstheorie und Gegenansicht (BGHZ 91, 324, 327 f.)
# ===========================================================================================================================
PII = "II. Der Streit"
folie([("wt", f"{PII} · Willenstheorie"), ("w118", f"{PII} › Stütze: § 118 BGB"),
       ("et", f"{PII} › Gegenansicht: Vertrauensschutz")], [
    *tafel("wt", "Ohne Erklärungsbewusstsein?"),
    blk(110, 180, 1040, 120, HELLROT, "wt", [("Willenstheorie: nein –", "ExtraBold", 34, INK),
                                          ("Erklärungsbewusstsein unverzichtbar", "ExtraBold", 34, INK)]),
    z("Stütze: § 118 BGB – nicht ernstlich gemeint, nichtig", 110, 320, "w118", "Bold", 33),
    z("allenfalls Vertrauensschaden analog § 122 BGB", 110, 370, "w122", size=33),
    zit("Meinungsstand: BGHZ 91, 324, 327 f.", 110, 420, "w122"),
    blk(110, 490, 1040, 120, HELLGRUEN, "et", [("Gegenansicht: Schutz des Empfängers", "ExtraBold", 34, INK),
                                            ("und des Verkehrs", "ExtraBold", 34, INK)]),
    *okz("zunächst wirksam, aber anfechtbar", 635, "et2", "Bold", 34, x=160),
    zit("BGHZ 91, 324, 328, 330", 160, 685, "et2"),
    *requisit([("wt", ("tabler", "scale", 110, WEISS), "der Streit", WEISS),
               ("et", ("tabler", "shield-check", 100, HELLGRUEN), "Vertrauensschutz", HELLGRUEN)]),
    *paar("EK", [("wt", "froh"), ("et", "sorge")], "HA", [("wt", "denkt"), ("et", "froh")]),
])

# ===========================================================================================================================
# D2 Die BGH-Formel (Leitsatz BGHZ 91, 324, wörtlich in Originalschreibung)
# ===========================================================================================================================
WL = ["„Trotz fehlenden Erklärungsbewußtseins … liegt eine",
      "Willenserklärung vor, wenn der Erklärende bei Anwendung",
      "der im Verkehr erforderlichen Sorgfalt hätte erkennen und",
      "vermeiden können, daß seine Äußerung nach Treu und",
      "Glauben und der Verkehrssitte als Willenserklärung",
      "aufgefaßt werden durfte, und wenn der Empfänger sie",
      "auch tatsächlich so verstanden hat.“"]
wl, wl_y = wortlaut(80, 230, 1100, WL, "BGHZ 91, 324 (Leitsatz)", "formel", marken=[
    (2, "hätte erkennen und", beim("formel", "hätte")), (3, "vermeiden können", beim("formel", "vermeiden")),
    (6, "tatsächlich so verstanden", beim("verst", "tatsächlich"))], size=31)
folie([("bghz", f"{PII} › BGH: Zurechnung"), ("verst", f"{PII} › Empfänger hat so verstanden"),
       ("pot", f"{PII} › potentielles Erklärungsbewusstsein")], [
    *tafel("bghz", "Der Bundesgerichtshof"),
    z("folgt der Gegenansicht – mit einer Einschränkung", 110, 170, "bghz", "Bold", 34),
    *wl,
    pl("potentielles Erklärungsbewusstsein", 110, wl_y + 30, "pot", fill=PINK, size=38),
    zit("bestätigt: BGH, Urt. v. 14.2.2023 – XI ZR 537/21, Rn. 29", 110, wl_y + 110, "pot"),
    *requisit([("bghz", ("tabler", "building-bank", 110, WEISS), "BGH, 7.6.1984", BLAUHELL),
               ("pot", ("tabler", "eye", 100, PINK), "hätte erkennen können", PINK)]),
    *stehend("EK", FX, [("bghz", "denkt"), ("verst", "sorge"), ("pot", "ruhig")]),
])

# ===========================================================================================================================
# D3 Das Wahlrecht; § 118 passt nicht (BGHZ 91, 324, 329 f.)
# ===========================================================================================================================
folie([("wahl", f"{PII} › Wahlrecht des Erklärenden"), ("p118", f"{PII} › § 118 BGB passt nicht")], [
    *tafel("wahl", "Der Grund: Der Erklärende behält die Wahl"),
    blk(110, 185, 1040, 120, GELB, "wa", [("Weg 1: anfechten –", "ExtraBold", 34, INK),
                                       ("dann Vertrauensschaden ersetzen", "Regular", 33, INK)]),
    blk(110, 335, 1040, 120, GRUEN, "wb", [("Weg 2: bei der Erklärung bleiben –", "ExtraBold", 34, INK),
                                        ("dann die Gegenleistung erhalten", "Regular", 33, INK)]),
    zit("BGHZ 91, 324, 329 f.", 110, 470, "wb"),
    *neinz("§ 118 BGB passt nicht:", 545, "p118", "ExtraBold", 34, x=160),
    z("Er meint den, der bewusst keine Bindung will.", 160, 595, beim("p118", "Er"), "Bold", 34),
    zit("BGHZ 91, 324, 329", 160, 645, beim("p118", "Er")),
    *requisit([("wahl", ("tabler", "arrows-split", 110, WEISS), "Wahlrecht", WEISS),
               ("p118", ("tabler", "mood-smile-beam", 100, HELLROT), "§ 118: nicht ernst", HELLROT)]),
    *paar("EK", [("wahl", "denkt"), ("wb", "froh")], "HA", [("wahl", "ruhig"), ("p118", "denkt")]),
])

# ===========================================================================================================================
# D4 Subsumtion: Willenserklärung (+), Kaufvertrag (+)
# ===========================================================================================================================
folie([("sub", f"{PII} › Ekkehard: erkennbar"), ("hver", f"{PII} › Frau Haller: so verstanden"),
       ("weok", f"{PII} › Kaufvertrag (+)")], [
    *tafel("sub", "Ekkehard im Versteigerungssaal"),
    *okz("Hand heben im Saal: Er hätte erkennen", 190, beim("sub", "hätte"), "Bold", 34, x=160),
    z("können, dass das als Gebot gilt.", 160, 238, beim("sub", "Gebot"), "Bold", 34),
    *okz("Frau Haller hat es auch so verstanden.", 320, "hver", "Bold", 34, x=160),
    blk(110, 410, 1040, 80, GRUEN, "weok", [("Willenserklärung (+)", "ExtraBold", 36, INK)]),
    blk(110, 520, 1040, 80, GRUEN, "kv", [("mit dem Zuschlag: Kaufvertrag (+)", "ExtraBold", 36, INK)]),
    zit("§ 156 Satz 1 BGB", 110, 615, "kv"),
    *requisit([("sub", ("tabler", "hand-stop", 100, GELB), "erkennbar", GELB),
               ("hver", ("tabler", "ear", 100, WEISS), "so verstanden", WEISS),
               ("kv", ("tabler", "gavel", 110, HOLZ), "Kaufvertrag", GRUEN)]),
    *paar("EK", [("sub", "sorge")], "HA", [("sub", "ruhig"), ("hver", "froh")]),
])

# ===========================================================================================================================
# E1 Anfechtung: § 119 Abs. 1 BGB (Wortlautkarte), BGH 329, analog
# ===========================================================================================================================
PIII = "III. Anfechtung"
W119 = ["„(1) Wer bei der Abgabe einer Willenserklärung … eine",
        "Erklärung dieses Inhalts überhaupt nicht abgeben wollte,",
        "kann die Erklärung anfechten, …“"]
w119, w119_y = wortlaut(80, 180, 1100, W119, "§ 119 Abs. 1 BGB (Auszug)", "p119", marken=[
    (2, "anfechten", beim("p119", "anfechten")), (1, "überhaupt nicht abgeben wollte", beim("p119", "überhaupt"))],
    size=33)
folie([("anf", f"{PIII} · Ekkehard kann sich lösen"), ("p119", f"{PIII} · § 119 Abs. 1 BGB"),
       ("bgh119", f"{PIII} › BGH: auch ohne Erklärungsbewusstsein"), ("analog", f"{PIII} › analog § 119 BGB")], [
    *tafel("anf", "Ekkehard kann sich lösen"),
    *w119,
    *okz("BGH: auch wer gar keine rechtsgeschäftliche", w119_y + 40, "bgh119", "Bold", 34, x=160),
    z("Erklärung abgeben wollte", 160, w119_y + 88, beim("bgh119", "rechtsgeschäftliche"), "Bold", 34),
    zit("BGHZ 91, 324, 329", 160, w119_y + 138, beim("bgh119", "rechtsgeschäftliche")),
    pl("oft: Anfechtung analog § 119 Abs. 1 BGB", 110, w119_y + 200, "analog", fill=PINK, size=36),
    zit("z. B. BGH, Beschl. v. 30.10.2013 – V ZB 9/13, Rn. 9", 110, w119_y + 280, "analog"),
    *requisit([("anf", ("tabler", "door-exit", 100, WEISS), "sich lösen", WEISS),
               ("p119", ("tabler", "book", 100, WEISS), "§ 119 Abs. 1", GELB),
               ("analog", ("tabler", "arrows-right-left", 100, PINK), "analog", PINK)]),
    *stehend("EK", FX, [("anf", "ruhig"), ("analog", "froh")]),
])

# ===========================================================================================================================
# E2 Unverzüglich (§ 121 Abs. 1 S. 1, Wortlautkarte), Willensmangel erkennbar, Sparkasse zu spät (ohne Figuren)
# ===========================================================================================================================
W121 = ["„Die Anfechtung muss in den Fällen der §§ 119, 120 ohne",
        "schuldhaftes Zögern (unverzüglich) erfolgen, nachdem der",
        "Anfechtungsberechtigte von dem Anfechtungsgrund",
        "Kenntnis erlangt hat.“"]
w121, w121_y = wortlaut(80, 180, 1100, W121, "§ 121 Abs. 1 Satz 1 BGB", "p121", marken=[
    (1, "(unverzüglich)", beim("p121", "unverzüglich")), (1, "schuldhaftes Zögern", beim("p121", "schuldhaftes")),
    (2, "Anfechtungsgrund", beim("p121", "Anfechtungsgrund"))], size=32)
folie([("p121", f"{PIII} › § 121: unverzüglich"), ("mangel", f"{PIII} › Willensmangel erkennbar"),
       ("spk2", f"{PIII} › Sparkasse: zu spät")], [
    *tafel("p121", "Unverzüglich – und mit Grund"),
    *w121,
    *okz("Willensmangel muss erkennbar sein", w121_y + 35, "mangel", "Bold", 34, x=160),
    zit("BGHZ 91, 324, 331 f.", 160, w121_y + 85, "mangel"),
    *neinz("Sparkasse: erster Brief bestritt nur", w121_y + 145, "spk2", "Bold", 34, x=160),
    *neinz("Anfechtung erst 15 Tage nach Kenntnis:", w121_y + 225, "tage", "Bold", 34, x=160),
    z("zu spät", 160, w121_y + 273, beim("tage", "zu"), "ExtraBold", 34),
    zit("BGHZ 91, 324, 332 f.", 160, w121_y + 323, beim("tage", "zu")),
    *requisit([("p121", ("tabler", "clock", 150, WEISS), "unverzüglich", GELB),
               ("mangel", ("tabler", "message", 150, WEISS), "Grund nennen", WEISS),
               ("spk2", ("tabler", "mail", 150, WEISS), "nur bestritten", HELLROT),
               ("tage", ("tabler", "calendar", 150, HELLROT), "15 Tage: zu spät", HELLROT)], pu=640, py=260),
])

# ===========================================================================================================================
# E3 Folgen: Anfechtung wirksam, § 142 Abs. 1, § 122 Abs. 1 (Wortlautkarte)
# ===========================================================================================================================
W122 = ["„… so hat der Erklärende … den Schaden zu ersetzen, den",
        "der andere … dadurch erleidet, dass er auf die Gültigkeit",
        "der Erklärung vertraut, jedoch nicht über den Betrag des",
        "Interesses hinaus, welches der andere … an der",
        "Gültigkeit der Erklärung hat.“"]
w122, w122_y = wortlaut(80, 330, 1100, W122, "§ 122 Abs. 1 BGB (Auszug)", "p122", marken=[
    (0, "Schaden zu ersetzen", beim("p122", "Schaden")), (1, "auf die Gültigkeit", beim("p122", "Gültigkeit")),
    (2, "vertraut", beim("p122", "vertraut")), (2, "nicht über den Betrag des", beim("deckel", "Höchstens"))], size=31)
folie([("eok", f"{PIII} › Ekkehard: sofort, mit Grund"), ("p142", f"{PIII} › § 142 Abs. 1: nichtig"),
       ("p122", f"{PIII} › § 122: Vertrauensschaden"), ("deckel", f"{PIII} › höchstens das Erfüllungsinteresse")], [
    *tafel("eok", "Die Folgen"),
    *okz("Ekkehard: sofort widersprochen, Grund genannt", 175, "eok", "Bold", 34, x=160),
    *okz("§ 142 Abs. 1: Kaufvertrag von Anfang an nichtig", 245, "p142", "Bold", 34, x=160),
    *w122,
    pl("z. B. Kosten, das Fass noch einmal anzubieten", 110, w122_y + 25, "kost", fill=GELB, size=32),
    *requisit([("eok", ("tabler", "message", 100, WEISS), "„nur gewinkt“", WEISS),
               ("p142", ("tabler", "file-x", 100, HELLROT), "nichtig", HELLROT),
               ("p122", ("tabler", "barrel", 110, HOLZ), "Vertrauensschaden", GELB)]),
    *paar("EK", [("eok", "froh"), ("p122", "sorge")], "HA", [("eok", "denkt"), ("kost", "ruhig")]),
])

# ===========================================================================================================================
# F Lösung im Saal (gleicher Schauplatz wie A1, die Geschichte kehrt dorthin zurück)
# ===========================================================================================================================
LK = (70, 120, 760, 290)
folie([("loes", "Lösung · Willenserklärung (+)"), ("loes2", "Lösung · wirksam angefochten"),
       ("loes3", "Lösung · nur Vertrauensschaden")], [
    *saal("loes"),
    hart(karte(*LK, "loes", fill=WEISS, rund=18, schatten=6, rand=4)),
    hart(z("Ergebnis", 100, 135, "loes", "ExtraBold", 34)),
    ok(120, 222, beim("loes", "Willenserklärung"), gr=18),
    z("Willenserklärung (+)", 160, 200, beim("loes", "Willenserklärung"), "Bold", 32, rechts=820),
    ok(120, 277, beim("loes", "Vertrag"), gr=18),
    z("Kaufvertrag zustande gekommen", 160, 255, beim("loes", "Vertrag"), "Bold", 32, rechts=820),
    ok(120, 332, "loes2", gr=18),
    z("wirksam angefochten", 160, 310, "loes2", "Bold", 32, rechts=820),
    pl("keine 900 €", 1240, 120, beim("loes2", "neunhundert"), fill=GRUEN, size=32),
    pl("nur Vertrauensschaden", 1240, 200, "loes3", fill=GELB, size=32),
    pl("1 Fass Riesling", FAX, 580, "loes", fill=WEISS, size=30, anker="m"),
    *fig("HA", HAX, BODEN, FH, [("loes", "ernst_r"), ("loes3", "ruhig_r")], erst="cut"),
    hart(ns("Frau Haller", HAX, BODEN, "loes", TUERKIS)),
    *fig("EK", EKX, BODEN, FH, [("loes", "denkt"), ("loes2", "froh")], erst="cut"),
    hart(ns("Ekkehard", EKX, BODEN, "loes", BLAU)),
    *fig("RE", TUX, BODEN, FH, [("loes", "ruhig"), ("loes2", "froh")], erst="cut"),
    hart(ns("Reinhild", TUX, BODEN, "loes", ORANGE)),
])

# ===========================================================================================================================
# G Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Prüfungsort: subjektiver Tatbestand"), ("tipp2", "Klausurtipp · erst dann die Anfechtung")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Erklärungsbewusstsein prüfst du im", 200, 200, beim("tipp", "Erklärungsbewusstsein"), "Bold", 36),
    z("subjektiven Tatbestand der Willenserklärung", 200, 250, beim("tipp", "subjektiven"), "Bold", 36),
    linienzug([(130, 330), (1130, 330)], "tipp2", breite=3),
    *okz("Erst wenn die Erklärung steht:", 360, "tipp2", "Bold", 36, x=200),
    z("die Anfechtung", 200, 410, beim("tipp2", "kommt"), "ExtraBold", 36),
    *neinz("nicht vorschnell: „kein Vertrag“", 490, beim("tipp2", "Schreib"), "Bold", 36, x=200),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# H Prüfschema
# ===========================================================================================================================
REIHEN = [("k1", 0, "I. Kaufvertrag durch Gebot und Zuschlag", True),
          ("k2", 1, "1. Objektiver Tatbestand: Erklärungswert aus Sicht des Empfängers", False),
          ("k3", 1, "2. Subjektiver Tatbestand: Handlungswille, Erklärungsbewusstsein", False),
          ("k4", 2, "fehlt es: potentielles Erklärungsbewusstsein genügt", False),
          ("k5", 0, "II. Nichtigkeit durch Anfechtung analog § 119 Abs. 1 BGB", True),
          (beim("k5", "unverzüglich"), 1, "unverzüglich, § 121 Abs. 1 BGB", False),
          ("k6", 0, "III. Vertrauensschaden, § 122 BGB", True)]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfschema: fehlendes Erklärungsbewusstsein"), 110, 90, "sch", 46)]
y = 215
for c, ebene, text, fett in REIHEN:
    x = (130, 200, 270)[ebene]
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 40 if ebene == 0 else 36, rechts=1800))
    y += {0: 100, 1: 84, 2: 84}[ebene]
assert y <= 970, y
folie([("sch", "Prüfschema"), ("k1", "Prüfschema › I. Kaufvertrag"), ("k2", "Prüfschema › I. 1. objektiver Tatbestand"),
       ("k3", "Prüfschema › I. 2. subjektiver Tatbestand"), ("k4", "Prüfschema › potentielles Erklärungsbewusstsein"),
       ("k5", "Prüfschema › II. Anfechtung"), ("k6", "Prüfschema › III. Vertrauensschaden")], els_sch)

# ===========================================================================================================================
# I Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Wer bei nötiger Sorgfalt erkennen konnte,", 0)], [("dass sein Verhalten als Willenserklärung", 0)],
                 [("verstanden wird, muss es sich ", 0), ("zurechnen", "a"), (" lassen.", 0)]], 750, 290, 42, "merke",
                {"a": beim("merke", "zurechnen")}),
    *markertext([[("Er kann anfechten, zahlt dann aber", 0)], [("den ", 0), ("Vertrauensschaden", "b"), (".", 0)]],
                750, 600, 42, "m2", {"b": beim("m2", "Vertrauensschaden")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
