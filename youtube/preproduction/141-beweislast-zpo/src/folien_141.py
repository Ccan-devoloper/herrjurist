"""Folge 141 · Beweislast ZPO: Wer verliert beim non liquet? – Serienstandard Open Peeps (Katzenkönig).
Beispielfall: Herr Wiedemann klagt gegen Frau Krause auf Rückzahlung eines Darlehens über 5.000 € (§ 488 Abs. 1 S. 2 BGB);
die Barauszahlung ohne Quittung ist streitig; Zeuge Herr Reichert (Übergabe) und Zeugin Frau Fischer (keine Übergabe)
widersprechen sich, beide gleich glaubhaft.
Szenen laut ../SZENENPLAN.md: A1 Im Sitzungssaal, A2 In der Küche, A3 Klage und Frage, B Sachverhalt, C Aufbau,
D 1. Streitige Tatsache, E 2. § 286 Abs. 1 ZPO (Wortlaut), F 2. Maßstab und Aussage gegen Aussage (Waage), G 3. Non liquet,
H 4. Normentheorie, I 4. Sonderregeln und subjektive Beweislast, J 5. Der Fall (Waage), K 5. Gegenvariante (Waage),
L 6. Im Urteil, M Klausurtipp (Lexi), N Klausurschema mit Waage, O Merksatz (Lexi).
Handlungsgeräusch: Umschlag wird auf den Küchentisch gelegt (../geraeusche_herkunft.json).
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/hand/okz/
neinz/tisch/punkt als eigene Kopie aus Folge 139 (gemeinsame Dateien unverändert); neu: waage(), richtertisch().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_141/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_141/" in n:
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


# --- neue Hilfsfunktionen Folge 141 -----------------------------------------------------------------------------------------
WAAGE_W = 520                                # Balkenlänge der Waage


def _waage_bild(w=WAAGE_W, fl=WEISS, fr=WEISS):
    """Balkenwaage im Tuschestil (programmatisch, waagrecht = Gleichstand): Säule, Fuß, Balken, Drehpunkt, zwei Schalen."""
    s = 2
    W_, H_ = w + 200, 340
    im = Image.new("RGBA", (W_ * s, H_ * s))
    d = ImageDraw.Draw(im)
    lw = 6 * s
    c = W_ / 2
    l, r = c - w / 2, c + w / 2
    sk = lambda *p: [v * s for v in p]
    d.rounded_rectangle(sk(c - 95, 298, c + 95, 332), 12 * s, fill=GELB, outline=INK, width=lw)        # Fuß
    d.rectangle(sk(c - 9, 60, c + 9, 300), fill=WEISS, outline=INK, width=lw)                         # Säule
    d.rounded_rectangle(sk(l - 6, 44, r + 6, 64), 9 * s, fill=WEISS, outline=INK, width=lw)            # Balken
    for x, f in ((l, fl), (r, fr)):
        d.line(sk(x, 58, x - 82, 200), fill=INK, width=4 * s)
        d.line(sk(x, 58, x + 82, 200), fill=INK, width=4 * s)
        d.chord(sk(x - 92, 150, x + 92, 250), 0, 180, fill=f, outline=INK, width=lw)                    # Schale
    d.ellipse(sk(c - 18, 36, c + 18, 72), fill=GELB, outline=INK, width=lw)                           # Drehpunkt
    return im.resize((W_, H_), Image.LANCZOS)


def waage(cx, oben, cue, bis=None, fl=WEISS, fr=WEISS, anim="pop"):
    """Waage als Diagramm (Gleichstand); gibt (El, (x, y) unter der linken Schale, (x, y) unter der rechten Schale) zurück."""
    im = _waage_bild(fl=fl, fr=fr)
    x0 = cx - im.width / 2
    e = El(im, x0, oben, cue, anim, 0.0, bis, name="diagramm:waage")
    return e, (round(cx - WAAGE_W / 2), oben + 262), (round(cx + WAAGE_W / 2), oben + 262)


def richtertisch(cx, unten, cue, w=440, h=230, text="Gericht"):
    """Richtertisch als Pastellblock mit Aufschrift (programmatisch, wie Folge 018)."""
    s = 2
    im = Image.new("RGBA", ((w + 12) * s, (h + 12) * s))
    d = ImageDraw.Draw(im)
    o = 6 * s
    d.rounded_rectangle((o, o, o + w * s, o + h * s), 14 * s, fill=(120, 132, 160, 255), outline=INK, width=5 * s)
    d.rounded_rectangle((o, o, o + w * s, o + 34 * s), 10 * s, fill=(90, 100, 128, 255), outline=INK, width=5 * s)
    f = F("ExtraBold", 40 * s)
    tw = f.getlength(text)
    d.text((o + (w * s - tw) / 2, o + 70 * s), text, font=f, fill=WEISS)
    im = im.resize((w + 12, h + 12), Image.LANCZOS)
    return El(im, cx - w / 2 - 6, unten - h - 6, cue, "cut", 0.0, None, name="richtertisch")


BODEN, FH = 860, 480
X1, X2 = 1420, 1720                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
PX, PY, PU = 1570, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"WI": "Herr Wiedemann", "KR": "Frau Krause", "RT": "Herr Reichert", "FI": "Frau Fischer", "RI": "Richterin"}
NFARBE = {"WI": BLAU, "KR": LILA, "RT": GRUEN, "FI": TUERKIS, "RI": WEISS}
ROTTEXT = (200, 60, 45, 255)


def boden(cue, hart_=False, x0=40, x1=1880):
    e = linienzug([(x0, BODEN), (x1, BODEN)], cue, breite=7, farbe=INK)
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


def paar(c0, l, lf, r, rf, bis=None):
    """Tafelszene: zwei Figuren rechts der Tafel, beide blicken zur Tafel (nach links)."""
    return [*fig(l, X1, FB, FR, lf, bis=bis), ns(NAME[l], X1, FB, c0, NFARBE[l], d=0.1, bis=bis),
            *fig(r, X2, FB, FR, rf, d=0.2, bis=bis), ns(NAME[r], X2, FB, c0, NFARBE[r], d=0.3, bis=bis)]


def solo(c0, p, folge, bis=None):
    """Tafelszene: eine Figur rechts der Tafel."""
    return [*fig(p, FX, FB, FR + 20, folge, bis=bis), ns(NAME[p], FX, FB, c0, NFARBE[p], d=0.1, bis=bis)]


# ===========================================================================================================================
# A1 Hook: im Sitzungssaal – zwei Zeugen widersprechen sich
# ===========================================================================================================================
RTX, FIX, RIX = 380, 1540, 960              # Zeuge links (blickt nach rechts), Zeugin rechts (blickt nach links), Richterin
ZG = beim("fall", "Zeugen")
folie([(NULL, "Fall · Im Sitzungssaal"), ("niemand", "Fall · Aussage gegen Aussage")], [
    boden(NULL, hart_=True),
    *fig("RI", RIX, 790, 400, [(NULL, "ruhig"), ("zeuge1", "ernst"), ("zeugin", "ernst_r"), ("niemand", "denkt")], erst="cut"),
    hart(richtertisch(RIX, BODEN, NULL)),
    hart(ns("Richterin", RIX, BODEN, NULL, WEISS)),
    pl("eine Frage", 70, 30, beim("fall", "Frage"), fill=GELB, size=36, bis="re1"),
    pl("zwei Antworten", 70, 110, beim("fall", "Antworten"), fill=PINK, size=36, bis="re1"),
    *fig("RT", RTX, BODEN, FH, [(ZG, "ruhig_r"), ("zeuge1", "ernst_r")], bis="re1"),
    ns("Herr Reichert", RTX, BODEN, ZG, NFARBE["RT"], d=0.1),
    *redet("RT_redet_r", RTX, BODEN, FH, "re1", "zeugin"),
    blase("sprech", 820, 200, "re1", 760, 200, inhalt=["Ich war dabei. Herr Wiedemann hat", "ihr 5.000 € bar gegeben."],
          textsize=34, figur=("RT_redet_r", RTX, BODEN, FH), bis="zeugin"),
    *fig("RT", RTX, BODEN, FH, [("zeugin", "ruhig_r"), ("fi1", "denkt_r"), ("niemand", "ernst_r")], erst="cut"),
    *fig("FI", FIX, BODEN, FH, [(ZG, "ruhig"), ("zeugin", "ernst")], bis="fi1", d=0.15),
    ns("Frau Fischer", FIX, BODEN, ZG, NFARBE["FI"], d=0.25),
    *redet("FI_redet", FIX, BODEN, FH, "fi1", "niemand"),
    blase("sprech", 800, 200, "fi1", 1100, 200, inhalt=["Ich saß am selben Tisch.", "Da ist kein Geld übergeben worden."],
          textsize=34, figur=("FI_redet", FIX, BODEN, FH), bis="niemand"),
    *fig("FI", FIX, BODEN, FH, [("niemand", "denkt")], erst="cut"),
    ficon("tabler", "cash-banknote", RIX - 60, 360, 150, beim("niemand", "Darlehen"), fuell=GRUEN),
    ficon("tabler", "question-mark", RIX + 85, 360, 80, beim("niemand", "ausgezahlt"), fuell=WEISS),
    pl("ausgezahlt?", RIX, 140, beim("niemand", "ausgezahlt"), fill=PINK, size=38, anker="m"),
])

# ===========================================================================================================================
# A2 Fall: der Abend in der Küche
# ===========================================================================================================================
KRX, WIX, TX = 560, 1340, 950              # Frau Krause links (blickt nach rechts), Herr Wiedemann rechts, Küchentisch
UM = beim("abend", "bar")
folie([("streit", "Fall · Das Darlehen"), ("abend", "Fall · Der Abend in der Küche")], [
    boden("streit"),
    hart(ficon("tabler", "fridge", 190, BODEN, 190, "streit", fuell=WEISS)),
    hart(tisch(TX, BODEN, "streit", w=460, h=230, fill=GELB)),
    *fig("KR", KRX, BODEN, FH, [("streit", "ruhig_r"), ("abend", "ernst_r"), ("wi1", "skeptisch_r")]),
    ns("Frau Krause", KRX, BODEN, "streit", NFARBE["KR"], d=0.1),
    *fig("WI", WIX, BODEN, FH, [("streit", "ruhig"), ("darl", "froh"), ("abend", "ernst")], bis="wi1", d=0.15),
    ns("Herr Wiedemann", WIX, BODEN, "streit", NFARBE["WI"], d=0.25),
    pl("Darlehen: 5.000 €", 70, 30, beim("darl", "Darlehen"), fill=GELB, size=44),
    pl("rückzahlbar bis Ende März", 70, 125, beim("darl", "rückzahlbar"), fill=WEISS, size=36),
    ficon("tabler", "moon", 1760, 250, 110, beim("abend", "Abend"), fuell=GELB),
    szene(ficon("tabler", "mail", TX, BODEN - 236, 120, UM, fuell=WEISS), "141umschlag*", 0.6, -0.05),
    ficon("tabler", "question-mark", TX + 95, BODEN - 300, 60, beim("abend", "haben"), fuell=WEISS),
    pl("bar übergeben?", 70, 205, UM, fill=PINK, size=36),
    pl("keine Quittung", 70, 285, beim("quitt", "Quittung"), fill=ROT, size=36),
    ficon("tabler", "receipt-off", 470, 420, 90, beim("quitt", "Quittung"), fuell=WEISS),
    *redet("WI_redet", WIX, BODEN, FH, "wi1", "best"),
    blase("sprech", 820, 200, "wi1", 1180, 210, inhalt=["Ich habe ihr das Geld gegeben,", "in einem Umschlag!"], textsize=36,
          figur=("WI_redet", WIX, BODEN, FH), bis="best"),
])

# ===========================================================================================================================
# A3 Fall: Bestreiten, Klage, Zeugen, Frage
# ===========================================================================================================================
KL, WR, MX = 330, 1590, 960
WG, WGL, WGR = waage(MX, 330, "hoert")
folie([("best", "Fall · Das Bestreiten"), ("klage", "Fall · Die Klage"), ("frage", "Fall · Die Frage")], [
    boden("best"),
    *fig("KR", KL, BODEN, FH, [("best", "ernst_r"), (beim("best", "nie"), "skeptisch_r"), ("frage", "sorge_r")], erst="cut"),
    hart(ns("Frau Krause", KL, BODEN, "best", NFARBE["KR"])),
    pl("Frau Krause: nie Geld bekommen", 70, 30, beim("best", "bestreitet"), fill=LILA, size=38),
    ficon("tabler", "cash-banknote-off", MX, 600, 200, beim("best", "nie"), fuell=ROT, bis=beim("klage", "Amtsgericht")),
    *fig("WI", WR, BODEN, FH, [("klage", "ernst"), ("hoert", "ruhig"), ("frage", "denkt")]),
    ns("Herr Wiedemann", WR, BODEN, "klage", NFARBE["WI"], d=0.1),
    ficon("tabler", "building-bank", MX, 600, 240, beim("klage", "Amtsgericht"), fuell=WEISS, bis="hoert"),
    pl("Amtsgericht", MX, 640, beim("klage", "Amtsgericht"), fill=WEISS, size=34, anker="m", bis="hoert"),
    pl("Klage auf Rückzahlung: 5.000 €", 70, 120, beim("klage", "Rückzahlung"), fill=BLAU, size=38),
    WG,
    pl("Herr Reichert", WGL[0], WGL[1], beim("hoert", "beide"), fill=NFARBE["RT"], size=28, anker="m"),
    pl("Frau Fischer", WGR[0], WGR[1], beim("hoert", "beide"), fill=NFARBE["FI"], size=28, anker="m"),
    pl("gleich glaubwürdig", MX, 760, beim("hoert", "gleich"), fill=GELB, size=34, anker="m"),
    pl("Wer verliert?", 70, 210, "frage", fill=PINK, size=44),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_141(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=38, zeilenabstand=1.30)
        els += e; y += 16
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=34))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_141("sv", [
    "Herr Wiedemann und Frau Krause vereinbaren ein zinsloses Darlehen über 5.000 Euro, rückzahlbar bis zum 31. März 2026. "
    "Herr Wiedemann sagt, er habe ihr das Geld an einem Abend in ihrer Küche bar in einem Umschlag gegeben. Eine Quittung "
    "gibt es nicht. Frau Krause bestreitet die Auszahlung: Sie habe nie Geld bekommen.",
    "Im April 2026 klagt Herr Wiedemann vor dem Amtsgericht auf Rückzahlung der 5.000 Euro. Vereinbarung und Fälligkeit "
    "sind unstreitig. Am Tisch saßen Herr Reichert, ein Bekannter von Herrn Wiedemann, und Frau Fischer, eine Freundin von "
    "Frau Krause. Herr Reichert sagt aus, das Geld sei übergeben worden; Frau Fischer sagt, es sei kein Geld übergeben "
    "worden. Beide wirken gleich glaubwürdig. Andere Beweise gibt es nicht.",
], "Wer verliert, wenn sich die Auszahlung nicht klären lässt?")

# ===========================================================================================================================
# C Aufbau: sechs Schritte
# ===========================================================================================================================
SCHRITTE = [("s1", "1.", "streitige Tatsache", BLAU), ("s2", "2.", "freie Beweiswürdigung", GELB),
            ("s3", "3.", "non liquet", PINK), ("s4", "4.", "Beweislast", GRUEN), ("s5", "5.", "der Fall", LILA),
            ("s6", "6.", "Formulierung im Urteil", TUERKIS)]
folie([("plan", "Beweislast › Aufbau")], rechts_frei([
    *tafel("plan", "Beweislast: sechs Schritte"),
    *[e for k, (c, r, t, fa) in enumerate(SCHRITTE) for e in (
        karte(130, 200 + k * 108, 100, 80, c, fill=fa, rund=14, schatten=5, rand=4),
        z(r, 180 - F("ExtraBold", 38).getlength(r) / 2, 215 + k * 108, c, "ExtraBold", 38),
        z(t, 270, 215 + k * 108, c, "Bold", 40))],
    *requisit([("plan", ("tabler", "list-numbers", 100, WEISS), "6 Schritte", WEISS),
               ("s2", ("tabler", "bulb", 100, GELB), "Beweiswürdigung", GELB),
               ("s3", ("tabler", "question-mark", 100, PINK), "non liquet", PINK),
               ("s4", ("tabler", "scale", 130, GRUEN), "Beweislast", GRUEN),
               ("s5", ("tabler", "cash-banknote", 120, GRUEN), "der Fall", LILA),
               ("s6", ("tabler", "file-text", 100, WEISS), "Urteil", TUERKIS)]),
    *paar("plan", "WI", [("plan", "ruhig"), ("s3", "denkt")], "KR", [("plan", "ruhig"), ("s4", "skeptisch")]),
]))

# ===========================================================================================================================
# D 1. Streitige Tatsache
# ===========================================================================================================================
W488 = ["„Der Darlehensnehmer ist verpflichtet, … bei Fälligkeit",
        "das zur Verfügung gestellte Darlehen zurückzuzahlen.“"]
w488, w488_y = wortlaut(80, 330, 1100, W488, "§ 488 Abs. 1 S. 2 BGB", "st3", marken=[
    (1, "zur Verfügung gestellte", beim("st3", "zur"))], size=33)
folie([("st1", "1. Streitige Tatsache"), ("st2", "1. Streitige Tatsache › § 488 Abs. 1 S. 2 BGB"),
       ("st5", "1. Streitige Tatsache › die Auszahlung")], rechts_frei([
    *tafel("st1", "1. Streitige, erhebliche Tatsache"),
    z("Beweis nur über eine streitige, erhebliche Tatsache", 110, 180, beim("st1", "Beweisstation"), "Bold", 34),
    blk(110, 240, 680, 64, LILA, beim("st1", "Mehr"), [("Mehr dazu: Video „Relationstechnik“", "ExtraBold", 30, INK)]),
    z("Anspruch: Rückzahlung, § 488 Abs. 1 S. 2 BGB", 110, 320 - 0, "st2", "Bold", 34, bis="st3"),
    *w488,
    *okz("Vereinbarung: unstreitig", w488_y + 30, beim("st4", "Vereinbarung"), "Bold", 34, x=160),
    *okz("Fälligkeit: unstreitig", w488_y + 90, beim("st4", "Fälligkeit"), "Bold", 34, x=160),
    blk(110, w488_y + 160, 1040, 74, HELLROT, beim("st5", "Streitig"), [("streitig: allein die Auszahlung", "ExtraBold", 36, INK)]),
    z("ohne Auszahlung nichts zurückzuzahlen", 110, w488_y + 260, beim("st5", "ohne"), "Bold", 34, farbe=ROTTEXT),
    *requisit([("st1", ("tabler", "scale", 120, WEISS), "Beweisstation", WEISS),
               ("st2", ("tabler", "coin-euro", 100, GELB), "Rückzahlung", GELB),
               ("st4", ("tabler", "file-check", 100, GRUEN), "unstreitig", GRUEN),
               ("st5", ("tabler", "cash-banknote", 120, GRUEN), "Auszahlung?", PINK)]),
    *paar("st1", "WI", [("st1", "ruhig"), ("st2", "ernst"), ("st5", "sorge")], "KR", [("st1", "ruhig"), ("st5", "skeptisch")]),
]))

# ===========================================================================================================================
# E 2. Freie Beweiswürdigung: § 286 Abs. 1 S. 1 ZPO (Wortlaut)
# ===========================================================================================================================
W286 = ["„(1) Das Gericht hat unter Berücksichtigung des gesamten",
        "Inhalts der Verhandlungen und des Ergebnisses einer",
        "etwaigen Beweisaufnahme nach freier Überzeugung zu",
        "entscheiden, ob eine tatsächliche Behauptung für wahr",
        "oder für nicht wahr zu erachten sei. …“"]
w286, w286_y = wortlaut(80, 180, 1100, W286, "§ 286 Abs. 1 S. 1 ZPO", beim("w286", "Paragraf"), marken=[
    (0, "gesamten", beim("w286", "gesamten")),
    (2, "freier Überzeugung", beim("w286", "freier")),
    (3, "für wahr", beim("w286", "wahr")),
    (4, "für nicht wahr", beim("w286", "nicht"))], size=33)
folie([("bw", "2. Freie Beweiswürdigung"), ("w286", "2. Freie Beweiswürdigung › § 286 Abs. 1 ZPO")], rechts_frei([
    *tafel("bw", "2. Freie Beweiswürdigung"),
    *w286,
    blk(110, w286_y + 50, 1040, 80, GELB, beim("w286", "erachten"), [("wahr oder nicht wahr?", "ExtraBold", 36, INK)]),
    *requisit([("bw", ("tabler", "scale", 130, GELB), "Beweiswürdigung", GELB),
               (beim("w286", "freier"), ("tabler", "bulb", 100, GELB), "freie Überzeugung", WEISS)]),
    *paar("bw", "RT", [("bw", "ruhig"), (beim("w286", "freier"), "denkt")], "FI", [("bw", "ruhig"), (beim("w286", "wahr"), "denkt")]),
]))

# ===========================================================================================================================
# F 2. Maßstab: volle Überzeugung (BGH), Aussage gegen Aussage (Waage)
# ===========================================================================================================================
WF, WFL, WFR = waage(630, 560, "agg")
folie([("voll", "2. Freie Beweiswürdigung › volle Überzeugung"), ("agg", "2. Freie Beweiswürdigung › Aussage gegen Aussage")],
      rechts_frei([
    *tafel("voll", "2. Maßstab: volle Überzeugung"),
    z("keine absolute Gewissheit nötig", 110, 180, "bgh", "Bold", 34),
    z("„ein für das praktische Leben brauchbarer", 110, 240, beim("bgh", "Es"), size=34),
    z("Grad von Gewissheit, der verbleibenden Zweifeln", 110, 290, beim("bgh", "Grad"), size=34),
    z("Schweigen gebietet, ohne sie völlig auszuschließen“", 110, 340, beim("bgh", "Schweigen"), size=34),
    zit("BGH, Urt. v. 12.12.2023 – VI ZR 76/23, Rn. 15", 110, 395, beim("bgh", "Schweigen")),
    linienzug([(110, 455), (1150, 455)], "agg", breite=3),
    z("Aussage gegen Aussage", 110, 480, "agg", "ExtraBold", 38),
    WF,
    pl("Geld übergeben", WFL[0], WFL[1], "agg", fill=NFARBE["RT"], size=28, anker="m"),
    pl("kein Geld", WFR[0], WFR[1], "agg", fill=NFARBE["FI"], size=28, anker="m"),
    pl("Gleichstand", 630, 900 - 40, "gleich", fill=GELB, size=30, anker="m"),
    *requisit([("voll", ("tabler", "shield-check", 100, GRUEN), "volle Überzeugung", GRUEN),
               ("agg", ("tabler", "messages", 110, WEISS), "Aussage gegen Aussage", WEISS),
               ("gleich", ("tabler", "scale", 130, GELB), "gleich glaubwürdig", GELB)]),
    *paar("voll", "RT", [("voll", "ruhig"), ("agg", "ernst")], "FI", [("voll", "ruhig"), ("agg", "ernst")]),
]))

# ===========================================================================================================================
# G 3. Non liquet
# ===========================================================================================================================
folie([("nl", "3. Non liquet"), ("nl3", "3. Non liquet › Urteil, § 300 Abs. 1 ZPO"), ("nl4", "3. Non liquet › jetzt erst: Beweislast")],
      rechts_frei([
    *tafel("nl", "3. Non liquet"),
    z("lateinisch: Es ist nicht klar.", 110, 180, beim("nl", "lateinisch"), "Bold", 36),
    z("Das Gericht ist nicht überzeugt …", 110, 265, "nl2", size=34),
    *neinz("… von der Auszahlung", 325, beim("nl2", "Auszahlung"), "Bold", 34, x=160),
    *neinz("… davon, dass kein Geld geflossen ist", 385, beim("nl2", "dass"), "Bold", 34, x=160),
    *okz("ein Urteil muss trotzdem ergehen", 475, beim("nl3", "Urteil"), "Bold", 34, x=160),
    zit("§ 300 Abs. 1 ZPO", 160, 530, beim("nl3", "Urteil")),
    blk(110, 600, 1040, 80, GELB, "nl4", [("jetzt erst entscheidet die Beweislast", "ExtraBold", 36, INK)]),
    z("Die Unklarheit geht zulasten der Partei,", 110, 720, beim("nl4", "Die"), "Bold", 34),
    z("die die Beweislast trägt.", 110, 770, beim("nl4", "Die"), "Bold", 34),
    *requisit([("nl", ("tabler", "question-mark", 110, PINK), "non liquet", PINK),
               ("nl3", ("tabler", "file-text", 100, WEISS), "Urteil", WEISS),
               ("nl4", ("tabler", "scale", 130, GELB), "Beweislast", GELB)]),
    *solo("nl", "RI", [("nl", "ruhig"), ("nl2", "denkt"), ("nl3", "ernst")]),
]))

# ===========================================================================================================================
# H 4. Beweislast: Normentheorie
# ===========================================================================================================================
folie([("nt", "4. Beweislast › Normentheorie"), ("nt3", "4. Beweislast › Kläger: anspruchsbegründend"),
       ("nt4", "4. Beweislast › Beklagter: rechtshindernd, -vernichtend, -hemmend")], rechts_frei([
    *tafel("nt", "4. Beweislast: Normentheorie"),
    z("Normentheorie (Leo Rosenberg)", 110, 175, beim("nt", "Normentheorie"), "Bold", 34),
    z("„jede Partei [muss] die tatsächlichen Voraussetzungen", 110, 240, "nt2", size=33),
    z("der ihr günstigen Normen darlegen und beweisen“", 110, 288, beim("nt2", "günstigen"), size=33),
    zit("BGH, Urt. v. 20.3.2024 – IV ZR 68/22, Rn. 68", 110, 340, beim("nt2", "günstigen")),
    karte(110, 400, 500, 300, "nt3", fill=BLAU, rund=18, schatten=5, rand=4),
    z("Kläger beweist:", 135, 420, "nt3", "ExtraBold", 34),
    z("anspruchs-", 135, 480, "nt3", "Bold", 34),
    z("begründende", 135, 528, "nt3", "Bold", 34),
    z("Tatsachen", 135, 576, "nt3", "Bold", 34),
    karte(650, 400, 500, 300, "nt4", fill=GRUEN, rund=18, schatten=5, rand=4),
    z("Beklagter beweist:", 675, 420, "nt4", "ExtraBold", 34),
    z("rechtshindernde,", 675, 480, beim("nt4", "hindert"), "Bold", 34),
    z("rechtsvernichtende,", 675, 528, beim("nt4", "vernichtet"), "Bold", 34),
    z("rechtshemmende", 675, 576, beim("nt4", "hemmt"), "Bold", 34),
    blk(110, 735, 1040, 64, LILA, beim("nt4", "Mehr"), [("Mehr dazu: Video „Einwendung und Einrede“", "ExtraBold", 30, INK)]),
    *requisit([("nt", ("tabler", "scale", 130, GELB), "Normentheorie", GELB),
               ("nt3", ("tabler", "coin-euro", 100, BLAU), "Kläger: Anspruch", BLAU),
               ("nt4", ("tabler", "shield-check", 100, GRUEN), "Beklagter: Gegenrechte", GRUEN)]),
    *paar("nt", "WI", [("nt", "ruhig"), ("nt3", "ernst")], "KR", [("nt", "ruhig"), ("nt4", "skeptisch")]),
]))

# ===========================================================================================================================
# I 4. Gesetzliche Sonderregeln, subjektive Beweislast
# ===========================================================================================================================
folie([("sonder", "4. Beweislast › gesetzliche Sonderregeln"), ("subj", "4. Beweislast › subjektive Beweislast")], rechts_frei([
    *tafel("sonder", "4. Gesetzliche Sonderregeln"),
    z("§ 280 Abs. 1 S. 2 BGB: Schuldner muss sich", 110, 180, "s280", "Bold", 34),
    z("vom Vertretenmüssen entlasten", 150, 228, beim("s280", "entlasten"), size=34),
    z("§ 477 BGB: Vermutung beim Verbrauchsgüterkauf", 110, 300, "s477", "Bold", 34),
    z("§ 1006 BGB: Besitzer gilt als Eigentümer (vermutet)", 110, 372, "s1006", "Bold", 34),
    zit("vgl. BGH, Urt. v. 16.5.2019 – III ZR 6/18, Rn. 14 (§ 280 Abs. 1 S. 2 BGB)", 110, 425, beim("s280", "entlasten")),
    linienzug([(110, 485), (1150, 485)], "subj", breite=3),
    z("subjektive Beweislast = Beweisführungslast", 110, 505, "subj", "ExtraBold", 36),
    z("Wer muss Beweis antreten, etwa durch einen Zeugen?", 110, 565, beim("subj", "Sie"), size=34),
    zit("vgl. BGH, Urt. v. 23.6.2023 – V ZR 28/22, Rn. 28; § 373 ZPO", 110, 620, beim("subj", "Sie")),
    *okz("Herr Wiedemann: Zeuge Herr Reichert benannt", 680, "subj2", "Bold", 34, x=160),
    *requisit([("sonder", ("tabler", "book", 100, WEISS), "Sonderregeln", WEISS),
               ("s280", ("tabler", "file-text", 100, WEISS), "§ 280 Abs. 1 S. 2", WEISS),
               ("s477", ("tabler", "receipt", 100, WEISS), "§ 477", WEISS),
               ("s1006", ("tabler", "key", 100, GELB), "§ 1006", GELB),
               ("subj", ("tabler", "user-check", 100, WEISS), "Beweis antreten", WEISS)]),
    *fig("WI", X1, FB, FR, [("sonder", "ruhig"), ("subj", "denkt"), ("subj2", "froh")]),
    ns(NAME["WI"], X1, FB, "sonder", NFARBE["WI"], d=0.1),
    *fig("RT", X2, FB, FR, [("subj2", "ruhig")]),
    ns(NAME["RT"], X2, FB, "subj2", NFARBE["RT"], d=0.1),
]))

# ===========================================================================================================================
# J 5. Der Fall (Waage: Beweislast beim Kläger)
# ===========================================================================================================================
WJ, WJL, WJR = waage(630, 470, "f3")
folie([("fall5", "5. Der Fall › Auszahlung: anspruchsbegründend"), ("f2", "5. Der Fall › Beweislast: Herr Wiedemann"),
       ("f4", "5. Der Fall › Klage abgewiesen")], rechts_frei([
    *tafel("fall5", "5. Der Fall"),
    *okz("Auszahlung: Voraussetzung des Anspruchs", 180, "f1", "Bold", 34, x=160),
    z("also: anspruchsbegründend", 160, 235, beim("f1", "anspruchsbegründend"), size=34),
    *okz("nützt Herrn Wiedemann: er trägt die Beweislast", 300, "f2", "Bold", 34, x=160),
    WJ,
    pl("Beweislast: Kläger", WJL[0], WJL[1], "f3", fill=GELB, size=28, anker="m"),
    pl("non liquet", 630, 430, "f3", fill=PINK, size=30, anker="m"),
    pl("zu seinen Lasten", WJL[0], WJL[1] + 62, beim("f3", "Lasten"), fill=ROT, size=28, anker="m"),
    blk(110, 810, 1040, 74, HELLROT, beim("f4", "Klage"), [("Klage abgewiesen", "ExtraBold", 38, INK)]),
    *requisit([("fall5", ("tabler", "cash-banknote", 120, GRUEN), "Auszahlung", WEISS),
               ("f2", ("tabler", "scale", 130, GELB), "Beweislast: Kläger", GELB),
               ("f4", ("tabler", "file-x", 100, ROT), "abgewiesen", ROT)]),
    *paar("fall5", "WI", [("fall5", "ruhig"), ("f2", "ernst"), ("f3", "sorge"), ("f4", "muede")],
          "KR", [("fall5", "ruhig"), ("f3", "skeptisch"), ("f4", "froh")]),
]))

# ===========================================================================================================================
# K 5. Gegenvariante: Rückzahlung behauptet
# ===========================================================================================================================
WK, WKL, WKR = waage(630, 440, "gv3")
folie([("gv", "5. Gegenvariante › Rückzahlung behauptet"), ("gv2", "5. Gegenvariante › Erfüllung, § 362 BGB"),
       ("gv3", "5. Gegenvariante › Beweislast: Frau Krause")], rechts_frei([
    *tafel("gv", "5. Gegenvariante: Rückzahlung"),
    z("Frau Krause: Geld bekommen, längst zurückgezahlt", 110, 180, "gv1", "Bold", 34),
    *okz("Auszahlung: unstreitig", 250, "gv2", "Bold", 34, x=160),
    z("Rückzahlung = Erfüllung, § 362 BGB:", 110, 320, beim("gv2", "Rückzahlung"), "Bold", 34),
    z("rechtsvernichtende Einwendung", 150, 370, beim("gv2", "rechtsvernichtende"), size=34),
    WK,
    pl("Rückzahlung: non liquet", 870, 392, "gv3", fill=PINK, size=30, anker="m"),
    pl("Beweislast: Beklagte", WKR[0], WKR[1], beim("gv3", "Frau"), fill=GELB, size=28, anker="m"),
    blk(110, 790, 1040, 70, HELLROT, beim("gv4", "verurteilt"), [("Frau Krause wird verurteilt", "ExtraBold", 38, INK)]),
    zit("vgl. BGH, Urt. v. 18.1.2022 – XI ZR 380/20, Rn. 31", 110, 866, beim("gv3", "Frau")),
    *requisit([("gv", ("tabler", "arrow-back-up", 110, WEISS), "Rückzahlung?", WEISS),
               ("gv2", ("tabler", "circle-check", 100, GRUEN), "Erfüllung, § 362", GRUEN),
               ("gv3", ("tabler", "scale", 130, GELB), "Beweislast: Beklagte", GELB)]),
    *paar("gv", "WI", [("gv", "ruhig"), ("gv3", "froh")], "KR", [("gv", "ruhig"), ("gv1", "ernst"), ("gv3", "sorge"),
                                                               ("gv4", "schreck")]),
]))

# ===========================================================================================================================
# L 6. Formulierung im Urteil
# ===========================================================================================================================
W2862 = ["„In dem Urteil sind die Gründe anzugeben, die für",
         "die richterliche Überzeugung leitend gewesen sind.“"]
w2862, w2862_y = wortlaut(80, 420, 1100, W2862, "§ 286 Abs. 1 S. 2 ZPO", "u2", marken=[
    (0, "die Gründe anzugeben", beim("u2", "Gründe"))], size=33)
folie([("urt", "6. Im Urteil"), ("u2", "6. Im Urteil › § 286 Abs. 1 S. 2 ZPO"), ("u3", "6. Im Urteil › Aufbau der Gründe")],
      rechts_frei([
    *tafel("urt", "6. Formulierung im Urteil"),
    z("Entscheidungsgründe, üblich:", 110, 180, "u1", "Bold", 34),
    blk(110, 235, 1040, 80, HELL, beim("u1", "Der"), [("„Der Kläger ist beweisfällig geblieben.“", "ExtraBold", 36, INK)]),
    zit("Formulierung z. B. in BGH, Urt. v. 7.2.2019 – VII ZR 274/17, Rn. 9 (Berufungsgericht)", 110, 335, beim("u1", "Der")),
    *w2862,
    z("1. Warum überzeugt keine der beiden Aussagen?", 110, w2862_y + 40, "u3", "Bold", 34),
    z("2. Wer trägt die Beweislast?", 110, w2862_y + 100, beim("u3", "erst"), "Bold", 34),
    *requisit([("urt", ("tabler", "file-text", 110, WEISS), "Urteil", WEISS),
               ("u2", ("tabler", "writing", 100, WEISS), "Gründe angeben", WEISS),
               ("u3", ("tabler", "list-numbers", 100, WEISS), "erst würdigen", GELB)]),
    *solo("urt", "RI", [("urt", "ruhig"), ("u2", "ernst"), ("u3", "denkt")]),
]))

# ===========================================================================================================================
# M Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · nicht zu früh in die Beweislast"), ("tipp3", "Klausurtipp · Sonderregeln")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Flüchte nicht zu früh in die Beweislast.", 200, 200, beim("tipp", "Flüchte"), "Bold", 36),
    z("1. Erst jede Aussage würdigen.", 200, 300, "tipp2", size=34),
    z("2. Nur wenn wirklich Zweifel bleiben:", 200, 360, beim("tipp2", "Nur"), size=34),
    z("Beweislast entscheidet.", 245, 410, beim("tipp2", "entscheidet"), size=34),
    linienzug([(130, 490), (1130, 490)], "tipp3", breite=3),
    z("Vorher prüfen: Sonderregel oder Vermutung?", 200, 520, "tipp3", "Bold", 34),
    z("z. B. §§ 280 Abs. 1 S. 2, 477, 1006 BGB", 240, 580, beim("tipp3", "Sonderregel"), size=32),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# N Klausurschema mit Waage
# ===========================================================================================================================
REIHEN = [("k1", "I.", "streitige, erhebliche Tatsache", "", BLAU, 0),
          ("k2", "II.", "Beweiswürdigung: volle Überzeugung", "§ 286 Abs. 1 ZPO", GELB, 0),
          ("k3", "III.", "non liquet?", "", PINK, 0),
          ("k4", "IV.", "Beweislast", "", GRUEN, 0),
          (beim("k4", "zuerst"), "1.", "gesetzliche Sonderregeln", "", None, 1),
          (beim("k4", "sonst"), "2.", "sonst: Normentheorie", "", None, 1),
          ("k5", "V.", "Ergebnis zulasten der", "", LILA, 0)]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Klausurschema: Beweisstation"), 110, 90, "sch", 46)]
y = 200
for c, r, kopf, norm, farbe, ebene in REIHEN:
    if ebene == 0:
        els_sch += [karte(110, y, 110, 70, c, fill=farbe, rund=14, schatten=5, rand=4),
                    z(r, 165 - F("ExtraBold", 38).getlength(r) / 2, y + 10, c, "ExtraBold", 38, rechts=1240),
                    z(kopf, 255, y + 10, c, "ExtraBold", 40, rechts=1240)]
        hh = 100
    else:
        els_sch += [z(r, 270, y + 4, c, "Bold", 36, rechts=1240), z(kopf, 330, y + 4, c, "Bold", 36, rechts=1240)]
        hh = 76
    if norm:
        els_sch.append(zit(norm, 255, y + 62, c, size=28, rechts=1240)); hh += 22
    y += hh
els_sch.append(z("beweisbelasteten Partei", 255, y - 45, "k5", "ExtraBold", 40, rechts=1240))
assert y + 20 <= 970, y
WS, WSL, WSR = waage(1470, 430, "k3")
els_sch += [WS, pl("non liquet", 1470, 370, "k3", fill=PINK, size=30, anker="m"),
            pl("Beweislast?", WSL[0], WSL[1], "k4", fill=GELB, size=28, anker="m"),
            pl("zulasten", WSL[0], WSL[1] + 70, "k5", fill=ROT, size=28, anker="m")]
folie([("sch", "Klausurschema"), ("k1", "Klausurschema › I. Streitige Tatsache"), ("k2", "Klausurschema › II. Beweiswürdigung"),
       ("k3", "Klausurschema › III. Non liquet"), ("k4", "Klausurschema › IV. Beweislast"), ("k5", "Klausurschema › V. Ergebnis")],
      els_sch)

# ===========================================================================================================================
# O Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Beim non liquet verliert,", "a")], [("wer die Beweislast trägt.", "b")]],
                750, 300, 44, "merke", {"a": beim("merke", "non"), "b": beim("merke", "Beweislast")}),
    *markertext([[("Sie trägt jede Partei für die", 0)], [("Voraussetzungen der Norm,", "c")], [("die ihr günstig ist.", "d")]],
                750, 520, 44, "mk2", {"c": beim("mk2", "Voraussetzungen"), "d": beim("mk2", "günstig")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
