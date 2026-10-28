"""Folge 086 · AGB-Kontrolle Schema §§ 305 ff. BGB: So prüfst du in 7 Schritten – Serienstandard Open Peeps (Katzenkönig).
Beispielfall: Mira bucht online ein Kurs-Abo im Fitnessstudio von Rolf (jede Woche 2 Kurse mit Trainer, 30 € im Monat);
in den AGB steht eine Mindestlaufzeit von 36 Monaten; Anfang Juli will Mira zum Monatsende kündigen.
Szenen laut ../SZENENPLAN.md: A1 Anmeldung (Wohnung, Laptop), A2 Kündigung im Studio/Kleingedrucktes/Frage, B Sachverhalt,
C sieben Schritte, D I. Anwendungsbereich, E II. AGB-Begriff (Wortlaut § 305 I 1), F III. Einbeziehung (§ 305b),
G IV. überraschende Klausel, H V. Auslegung, I VI. Inhaltskontrolle (Kontrollfähigkeit, Reihenfolge),
J § 309 Nr. 9 a (Wortlaut; reiner Gerätevertrag = Miete), K § 309 Nr. 9 b und § 312k, L VII. Rechtsfolge (Wortlaut § 306 I, II),
M Ergebnis, N Klausurtipp (Lexi), O Klausurschema, P Merksatz (Lexi).
Zwei Handlungsgeräusche (Klick beim Buchen, Schritte, als Mira ins Studio geht; ../geraeusche_herkunft.json).
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/hand als
eigene Kopie aus Folge 083 (gemeinsame Dateien unverändert). Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_086/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_086/" in n:
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 027/073/083) ------------------------------------
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
MI_N, RO_N = PINK, BLAU                     # Farben der Namensschilder
PX, PY, PU = 1570, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"MI": "Mira", "RO": "Rolf"}
NFARBE = {"MI": MI_N, "RO": RO_N}


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
    """Tafelszene: zwei Figuren rechts der Tafel, beide blicken zur Tafel (nach links); l, r = Kürzel MI/RO."""
    return [*fig(l, X1, FB, FR, lf), ns(NAME[l], X1, FB, c0, NFARBE[l], d=0.1),
            *fig(r, X2, FB, FR, rf, d=0.2), ns(NAME[r], X2, FB, c0, NFARBE[r], d=0.3)]


# A1 Fall: die Anmeldung online (Wohnung, Laptop) ------------------------------------------------------------------------
MX = 1640                                            # Mira steht am Tisch
SX0, SY0, SW, SH = 80, 120, 1000, 510                # Bildschirm-Ausschnitt (Webseite)
TISCH = ficon("tabler", "desk", 1290, BODEN, 330, "_", fuell=GELB)
TY = int(TISCH.y + 0.12 * TISCH.sprite.height)       # Tischplatte
BUCHT = beim("haken", "bucht")
folie([(NULL, "Fall · Die Anmeldung online"), ("hinw", "Fall · Hinweis auf die AGB")], [
    hart(pl("Mira bucht online ein Kurs-Abo", 70, 30, NULL, fill=GELB, size=44)),
    hart(boden(NULL)),
    hart(ficon("ph", "couch", 330, BODEN, 280, NULL, fuell=LILA)),
    hart(ficon("tabler", "desk", 1290, BODEN, 330, NULL, fuell=GELB)),
    hart(ficon("tabler", "device-laptop", 1290, TY + 6, 170, NULL, fuell=WEISS)),
    # Bildschirm: die Buchungsseite des Studios
    hart(karte(SX0, SY0, SW, SH, NULL, fill=WEISS, rund=18, schatten=8)),
    hart(linienzug([(SX0 + 4, SY0 + 64), (SX0 + SW - 4, SY0 + 64)], NULL, breite=4)),
    hart(z("Fitnessstudio · Kurs-Abo", SX0 + 30, SY0 + 12, NULL, "Bold", 34)),
    ficon("tabler", "barbell", SX0 + 820, SY0 + 230, 200, beim("fall", "Fitnessstudio"), fuell=GRUEN),
    pl("Januar", 1290, 420, beim("fall", "Januar"), fill=WEISS, size=30, anker="m"),
    ficon("tabler", "calendar-event", 1290, 410, 70, beim("fall", "Januar"), fuell=WEISS),
    z("2 Kurse pro Woche mit Trainer", SX0 + 40, SY0 + 100, beim("abo", "zwei"), "Bold", 38),
    z("30 € im Monat", SX0 + 40, SY0 + 160, beim("abo", "dreißig"), size=38),
    z("Es gelten unsere AGB.", SX0 + 40, SY0 + 250, "hinw", size=36),
    ficon("tabler", "link", SX0 + 520, SY0 + 300, 46, beim("hinw", "Link"), fuell=None),
    pl("AGB lesen", SX0 + 560, SY0 + 250, beim("hinw", "Link"), fill=BLAU, size=32),
    ficon("tabler", "square-check", SX0 + 70, SY0 + 400, 56, "haken", fuell=GRUEN),
    z("Ich akzeptiere die AGB.", SX0 + 120, SY0 + 345, "haken", size=36),
    szene(pl("Jetzt buchen", SX0 + 40, SY0 + 420, BUCHT, fill=GRUEN, size=38), "086klick*", 0.6, 0.0),
    # Mira (rechts, blickt zum Laptop nach links)
    *fig("MI", MX, BODEN, FH, [(NULL, "ruhig"), ("hinw", "denkt"), (BUCHT, "froh")], erst="cut"),
    hart(ns("Mira", MX, BODEN, NULL, MI_N)),
])

# A2 Fall: die Kündigung im Studio, das Kleingedruckte, die Frage -------------------------------------------------------------
AX, AX0, RX = 560, 260, 1480
GEHT = (beim("juli", "geht"), beim("juli", "Studio", ende=True))
AGBX, AGBY, AGBW, AGBH = 700, 120, 560, 330
folie([("juli", "Fall · Die Kündigung"), ("klein", "Fall · Das Kleingedruckte"), ("frage", "Fall · Die Frage")], [
    pl("Anfang Juli", 70, 30, "juli", fill=GELB, size=44, bis="frage"),
    boden("juli"),
    ficon("tabler", "calendar-event", 330, 300, 90, "juli", fuell=WEISS, bis=GEHT[0]),
    pl("keine Zeit mehr", 330, 310, beim("juli", "keine"), fill=WEISS, size=30, anker="m", bis=GEHT[0]),
    # das Studio: Hantelbank und Hanteln, Rolf
    ficon("tabler", "barbell", 1060, BODEN, 220, beim("juli", "Rolf"), fuell=GRUEN),
    ficon("tabler", "dumbbell", 1790, BODEN, 120, beim("juli", "Rolf"), fuell=GRUEN),
    ficon("tabler", "building-store", 1780, 300, 110, beim("juli", "Studio"), fuell=BLAU),
    pl("Studio", 1780, 310, beim("juli", "Studio"), fill=BLAU, size=30, anker="m"),
    # Mira: erst nachdenklich links, dann geht sie zu Rolf
    *fig("MI", AX0, BODEN, FH, [("juli", "sorge_r")], bis=GEHT[0], erst="cut"),
    ns("Mira", AX0, BODEN, "juli", MI_N, bis=GEHT[0]),
    szene(bewegt(peep_voll("MI_ruhig_r", AX, BODEN, FH, GEHT[0], anim="cut", bis="mi1"), *GEHT, AX0 - AX, 0),
          "086schritte*", 0.8, 0.0),
    bewegt(ns("Mira", AX, BODEN, GEHT[0], MI_N, anim="cut"), *GEHT, AX0 - AX, 0),
    *redet("MI_redet_r", AX, BODEN, FH, "mi1", "ro1"),
    *fig("MI", AX, BODEN, FH, [("ro1", "sorge_r"), ("mind", "staunt_r"), ("frage", "denkt_r")], erst="cut"),
    # Rolf (rechts, blickt zu Mira)
    *fig("RO", RX, BODEN, FH, [(beim("juli", "Rolf"), "ruhig")], bis="ro1"),
    ns("Rolf", RX, BODEN, beim("juli", "Rolf"), RO_N),
    *redet("RO_redet", RX, BODEN, FH, "ro1", "klein"),
    *fig("RO", RX, BODEN, FH, [("klein", "froh"), ("frage", "ruhig")], erst="cut"),
    blase("sprech", 700, 200, "mi1", 860, 230, inhalt=["Ich möchte kündigen,", "zum Ende des Monats."], textsize=34,
          figur=("MI_redet_r", AX, BODEN, FH), bis="ro1"),
    blase("sprech", 860, 260, "ro1", 1000, 220, inhalt=["Das geht nicht. Lies das", "Kleingedruckte:",
                                                     "Mindestlaufzeit 3 Jahre."], textsize=34,
          figur=("RO_redet", RX, BODEN, FH), bis="klein"),
    # das Kleingedruckte: Auszug aus den AGB
    karte(AGBX, AGBY, AGBW, AGBH, "klein", fill=ZITAT, rund=16, schatten=6, rand=4),
    z("Allgemeine Geschäftsbedingungen", AGBX + 26, AGBY + 20, "klein", "Bold", 30, rechts=AGBX + AGBW - 16),
    z("§ 4 Laufzeit", AGBX + 26, AGBY + 90, beim("klein", "Laufzeit"), "Bold", 34, rechts=AGBX + AGBW - 16),
    z("Die Mindestlaufzeit beträgt", AGBX + 26, AGBY + 160, "mind", size=34, rechts=AGBX + AGBW - 16),
    z("36 Monate.", AGBX + 26, AGBY + 215, beim("mind", "sechsunddreißig"), "Bold", 34, rechts=AGBX + AGBW - 16),
    pl("3 Jahre gebunden?", 960, 520, "frage", fill=PINK, size=40, anker="m"),
    pl("Prüfung in 7 Schritten", 960, 600, "frage2", fill=WEISS, size=34, anker="m"),
])
# Marker hinter „36 Monate.“ zum gesprochenen Wort (Textmarker wie in den Wortlautkarten)
_m = Image.new("RGBA", (int(F("Bold", 34).getlength("36 Monate.")) + 12, 30))
ImageDraw.Draw(_m).rounded_rectangle((0, 0, _m.width - 1, _m.height - 1), 7, fill=MARKER)
FOLIEN[-1]["els"].insert(len(FOLIEN[-1]["els"]) - 3, El(_m, AGBX + 20, AGBY + 225, beim("mind", "sechsunddreißig"), "fade", 0.0,
                                                       None, name="marker:36 Monate"))


# B Sachverhalt ---------------------------------------------------------------------------------------------------------------
def sachverhalt_086(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=36, zeilenabstand=1.32)
        els += e; y += 22
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=38))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_086("sv", [
    "Mira bucht im Januar 2026 online ein Kurs-Abo im Fitnessstudio von Rolf: jede Woche 2 Kurse mit Trainer, 30 Euro im "
    "Monat. Vor dem Klick auf „Jetzt buchen“ weist die Seite auf die AGB hin, mit Link zum Lesen. Mira setzt den Haken "
    "„Ich akzeptiere die AGB“.",
    "In den AGB, die Rolf für alle Mitglieder verwendet, steht unter der Überschrift „Laufzeit“: „Die Mindestlaufzeit "
    "beträgt 36 Monate.“ Ausgehandelt wurde nichts.",
    "Anfang Juli will Mira zum Ende des Monats kündigen. Rolf sagt: „Das geht nicht. Mindestlaufzeit 3 Jahre.“",
], "Ist Mira 3 Jahre gebunden?")

# C sieben Schritte -------------------------------------------------------------------------------------------------------------
SCHRITTE = [("s1", "I. Anwendungsbereich"), ("s2", "II. AGB-Begriff"), ("s3", "III. Einbeziehung"),
            ("s4", "IV. keine überraschende Klausel"), ("s5", "V. Auslegung"), ("s6", "VI. Inhaltskontrolle"),
            ("s7", "VII. Rechtsfolge")]
folie([("sieben", "AGB-Kontrolle › 7 Schritte")], rechts_frei([
    *tafel("sieben", "AGB-Kontrolle: 7 Schritte"),
    *[z(t, 160, 190 + 82 * i, c, "Bold", 40) for i, (c, t) in enumerate(SCHRITTE)],
    *requisit([("sieben", ("tabler", "list-numbers", 110, WEISS), "7 Schritte", WEISS)]),
    *paar("sieben", "MI", [("sieben", "ruhig")], "RO", [("sieben", "ruhig")]),
]))

# D I. Anwendungsbereich, § 310 ----------------------------------------------------------------------------------------------
folie([("anw", "AGB-Kontrolle › I. Anwendungsbereich, § 310 BGB")], rechts_frei([
    *tafel("anw", "I. Anwendungsbereich"),
    z("§ 310 BGB", 110, 190, beim("anw", "Paragraf"), "Bold", 40),
    *neinz("nicht im Erb-, Familien- und Gesellschaftsrecht", 270, "anw4", "Bold", 34, x=160),
    zit("§ 310 Abs. 4 BGB", 160, 322, "anw4"),
    z("gegenüber Unternehmern nur eingeschränkt,", 160, 390, "anw1", "Bold", 34),
    z("etwa ohne § 309 BGB", 160, 440, beim("anw1", "ohne"), size=34),
    zit("§ 310 Abs. 1 BGB", 160, 492, beim("anw1", "ohne")),
    *okz("Mira: Verbraucherin (§ 13 BGB)", 570, beim("anw3", "Verbraucherin"), "Bold", 34, x=160),
    *okz("Rolf: Unternehmer (§ 14 BGB)", 630, beim("anw3", "Unternehmer"), "Bold", 34, x=160),
    blk(110, 710, 1040, 100, GRUEN, beim("anw3", "Verbrauchervertrag"), [("Verbrauchervertrag: alles gilt", "ExtraBold", 40, INK)]),
    *requisit([("anw", ("tabler", "filter", 100, WEISS), "Anwendungsbereich", WEISS),
               ("anw3", ("tabler", "user-check", 110, GRUEN), "Verbrauchervertrag", GRUEN)]),
    *paar("anw", "MI", [("anw", "ruhig"), (beim("anw3", "Verbrauchervertrag"), "froh")], "RO", [("anw", "ruhig")]),
]))

# E II. AGB-Begriff (Wortlaut § 305 Abs. 1 Satz 1) -------------------------------------------------------------------------------
W305 = ["„Allgemeine Geschäftsbedingungen sind alle für eine Vielzahl von",
        "Verträgen vorformulierten Vertragsbedingungen, die eine Vertrags-",
        "partei (Verwender) der anderen Vertragspartei bei Abschluss eines",
        "Vertrags stellt.“"]
w305, w305_y = wortlaut(80, 175, 1100, W305, "§ 305 Abs. 1 Satz 1 BGB", "w305", marken=[
    (0, "Vielzahl", beim("w305", "Vielzahl")), (1, "vorformulierten", beim("w305", "vorformulierten")),
    (2, "(Verwender)", beim("w305", "Verwender")), (3, "stellt", beim("w305", "stellt"))], size=32)
folie([("begr", "AGB-Kontrolle › II. AGB-Begriff, § 305 Abs. 1 BGB")], rechts_frei([
    *tafel("begr", "II. Liegen AGB vor?"),
    *w305,
    z("Vielzahl: schon bei 3 beabsichtigten Verwendungen", 110, w305_y + 30, "viel", "Bold", 34),
    zit("BGH, Urt. v. 14.1.2025 – XI ZR 35/24, Rn. 16", 160, w305_y + 82, beim("viel", "dreimal")),
    *okz("Rolf: dieselben Bedingungen für alle Mitglieder", w305_y + 160, "begr2", "Bold", 34, x=160),
    *okz("nichts ausgehandelt (§ 305 Abs. 1 Satz 3 BGB)", w305_y + 220, beim("begr2", "ausgehandelt"), "Bold", 34, x=160),
    *requisit([("begr", ("tabler", "file-text", 100, WEISS), "AGB?", WEISS),
               ("viel", ("tabler", "copy", 100, WEISS), "3 Verwendungen", WEISS),
               ("begr2", ("tabler", "users-group", 120, BLAU), "alle Mitglieder", GRUEN)]),
    *paar("begr", "MI", [("begr", "ruhig"), ("begr2", "denkt")], "RO", [("begr", "ruhig"), ("begr2", "froh")]),
]))

# F III. Einbeziehung, § 305 Abs. 2, 3; § 305b ---------------------------------------------------------------------------------
folie([("einb", "AGB-Kontrolle › III. Einbeziehung, § 305 Abs. 2 BGB"),
       ("indiv", "III. Einbeziehung › Vorrang der Individualabrede, § 305b BGB")], rechts_frei([
    *tafel("einb", "III. Einbeziehung"),
    z("§ 305 Abs. 2 BGB, bei Vertragsschluss:", 110, 190, beim("einb", "Paragraf"), "Bold", 38),
    z("1. ausdrücklicher Hinweis auf die AGB", 160, 255, "e1", size=34),
    z("2. zumutbare Möglichkeit, sie zu lesen", 160, 310, "e2", size=34),
    z("3. Einverständnis der anderen Seite", 160, 365, "e3", size=34),
    *okz("online: Hinweis vor dem Klick, Link, Haken", 450, "esub", "Bold", 34, x=160),
    linienzug([(110, 530), (1150, 530)], "abs3", breite=3),
    z("§ 305 Abs. 3 BGB: Vereinbarung im Voraus", 110, 555, "abs3", "Bold", 34),
    z("für bestimmte künftige Geschäfte", 160, 605, beim("abs3", "künftige"), size=34),
    blk(110, 680, 1040, 150, GELB, "indiv", [("§ 305b BGB: Individualabrede", "ExtraBold", 38, INK),
                                            ("geht den AGB vor", "Bold", 36, INK)]),
    *requisit([("einb", ("tabler", "square-check", 100, WEISS), "einbezogen?", WEISS),
               ("esub", ("tabler", "link", 100, WEISS), "Hinweis, Link, Haken", GRUEN),
               ("indiv", ("tabler", "writing", 110, WEISS), "Individualabrede", GELB)]),
    *paar("einb", "MI", [("einb", "ruhig"), ("esub", "froh"), ("indiv", "denkt")], "RO", [("einb", "ruhig")]),
]))

# G IV. keine überraschende Klausel, § 305c Abs. 1 ----------------------------------------------------------------------------
folie([("ueber", "AGB-Kontrolle › IV. keine überraschende Klausel, § 305c Abs. 1 BGB")], rechts_frei([
    *tafel("ueber", "IV. Überraschende Klausel?"),
    z("§ 305c Abs. 1 BGB: so ungewöhnlich, dass der", 110, 190, beim("ueber", "Was"), "Bold", 36),
    z("Kunde nicht damit rechnen muss:", 160, 242, beim("ueber", "Kunde"), "Bold", 36),
    z("nicht Vertragsbestandteil", 160, 294, beim("ueber", "Vertragsbestandteil"), size=36),
    *okz("Laufzeiten bei solchen Verträgen üblich", 390, "usub", "Bold", 34, x=160),
    *okz("offen unter der Überschrift „Laufzeit“", 450, beim("usub", "offen"), "Bold", 34, x=160),
    blk(110, 540, 1040, 150, GELB, "ulang", [("3 Jahre zu lang?", "ExtraBold", 40, INK),
                                            ("Frage der Inhaltskontrolle", "Bold", 36, INK)]),
    *requisit([("ueber", ("tabler", "search", 100, WEISS), "überraschend?", WEISS),
               ("usub", ("tabler", "file-text", 100, WEISS), "§ 4 Laufzeit", WEISS),
               ("ulang", ("tabler", "hourglass", 90, GELB), "3 Jahre?", GELB)]),
    *paar("ueber", "MI", [("ueber", "ruhig"), ("ulang", "sorge")], "RO", [("ueber", "ruhig"), ("usub", "froh")]),
]))

# H V. Auslegung, § 305c Abs. 2 -----------------------------------------------------------------------------------------------
folie([("ausl", "AGB-Kontrolle › V. Auslegung, § 305c Abs. 2 BGB")], rechts_frei([
    *tafel("ausl", "V. Auslegung"),
    z("einheitlich: wie verständige und redliche", 110, 190, beim("ausl", "einheitlich"), "Bold", 36),
    z("Vertragspartner sie verstehen", 160, 242, beim("ausl", "Vertragspartner"), size=36),
    zit("BGH, Urt. v. 14.1.2025 – XI ZR 35/24, Rn. 20", 160, 298, beim("ausl", "verstehen")),
    z("§ 305c Abs. 2 BGB: Zweifel gehen zu Lasten", 110, 380, "unkl", "Bold", 36),
    z("des Verwenders", 160, 432, beim("unkl", "Lasten"), size=36),
    *okz("keine Zweifel: 36 Monate sind eindeutig", 530, "asub", "Bold", 36, x=160),
    *requisit([("ausl", ("tabler", "zoom-in", 100, WEISS), "Auslegung", WEISS),
               ("unkl", ("ph", "scales", 120, WEISS), "Zweifel?", WEISS),
               ("asub", ("tabler", "file-check", 100, GRUEN), "eindeutig", GRUEN)]),
    *paar("ausl", "MI", [("ausl", "ruhig"), ("asub", "denkt")], "RO", [("ausl", "ruhig")]),
]))

# I VI. Inhaltskontrolle: Kontrollfähigkeit und Reihenfolge ---------------------------------------------------------------------
folie([("ink", "AGB-Kontrolle › VI. Inhaltskontrolle"), ("reihe", "VI. Inhaltskontrolle › Reihenfolge")], rechts_frei([
    *tafel("ink", "VI. Inhaltskontrolle"),
    z("kontrollfähig (§ 307 Abs. 3 BGB): Klauseln, die", 110, 190, "kf", "Bold", 36),
    z("vom Gesetz abweichen oder es ergänzen", 160, 242, beim("kf", "abweichen"), size=36),
    *okz("feste Mindestlaufzeit: kontrollfähig", 320, beim("kf", "feste"), "Bold", 34, x=160),
    zit("vgl. BGH, Versäumnisurt. v. 8.2.2012 – XII ZR 42/10, Rn. 15", 160, 372, beim("kf", "feste")),
    z("vom Speziellen zum Allgemeinen:", 110, 450, "reihe", "Bold", 36),
    blk(110, 510, 1040, 80, ROT, "r309", [("1. § 309 BGB: ohne Wertungsmöglichkeit", "ExtraBold", 34, INK)]),
    blk(110, 610, 1040, 80, GELB, "r308", [("2. § 308 BGB: mit Wertungsmöglichkeit", "ExtraBold", 34, INK)]),
    blk(110, 710, 1040, 80, GRUEN, "r307", [("3. § 307 BGB: Generalklausel", "ExtraBold", 34, INK)]),
    *requisit([("ink", ("ph", "scales", 120, WEISS), "Inhaltskontrolle", WEISS),
               ("reihe", ("tabler", "list-numbers", 100, WEISS), "Reihenfolge", WEISS)]),
    *paar("ink", "MI", [("ink", "ruhig")], "RO", [("ink", "ruhig"), ("reihe", "denkt")]),
]))

# J § 309 Nr. 9 a) (Wortlaut) ---------------------------------------------------------------------------------------------------
W309 = ["„… ist in Allgemeinen Geschäftsbedingungen unwirksam … 9. bei",
        "einem Vertragsverhältnis, das die regelmäßige Lieferung von Waren",
        "oder die regelmäßige Erbringung von Dienst- oder Werkleistungen",
        "durch den Verwender zum Gegenstand hat, a) eine den anderen",
        "Vertragsteil länger als zwei Jahre bindende Laufzeit des Vertrags, …“"]
w309, w309_y = wortlaut(80, 165, 1100, W309, "§ 309 Nr. 9 Buchst. a BGB", "w309", marken=[
    (2, "regelmäßige Erbringung von Dienst-", beim("w309", "Erbringung")),
    (4, "länger als zwei Jahre", beim("w309", "länger"))], size=32)
folie([("w309", "VI. Inhaltskontrolle › § 309 Nr. 9 a BGB"), ("kurse", "§ 309 Nr. 9 a BGB › Kurse mit Trainer")], rechts_frei([
    *tafel("w309", "VI. § 309 Nr. 9 a BGB"),
    *w309,
    z("nur Geräte und Räume: Mietvertrag", 110, w309_y + 24, beim("miete", "Mietvertrag"), "Bold", 34),
    zit("BGH, Versäumnisurt. v. 8.2.2012 – XII ZR 42/10, Rn. 16–18", 160, w309_y + 74, beim("miete", "Mietvertrag")),
    z("Nr. 9 passt nicht, dann bleibt § 307 BGB", 160, w309_y + 122, beim("miete", "Nummer"), size=34),
    *okz("Rolf: jede Woche Kurse mit Trainer, Dienstleistung", w309_y + 190, "kurse", "Bold", 34, x=160),
    blk(110, w309_y + 260, 1040, 90, HELLROT, "drei", [("3 Jahre länger als 2: Klausel unwirksam", "ExtraBold", 36, INK)]),
    *requisit([("w309", ("tabler", "calendar-time", 100, WEISS), "höchstens 2 Jahre", WEISS),
               ("miete", ("tabler", "barbell", 140, GRUEN), "nur Geräte?", WEISS),
               ("kurse", ("tabler", "users-group", 120, BLAU), "Kurse mit Trainer", GRUEN),
               ("drei", ("tabler", "calendar-x", 100, HELLROT), "unwirksam", HELLROT)]),
    *paar("w309", "MI", [("w309", "ruhig"), ("drei", "froh")], "RO", [("w309", "ruhig"), ("miete", "denkt"), ("drei", "sorge")]),
]))

# K § 309 Nr. 9 b) und § 312k ------------------------------------------------------------------------------------------------------
folie([("bc", "VI. Inhaltskontrolle › § 309 Nr. 9 b BGB"), ("button", "Kündigungsbutton · § 312k BGB")], rechts_frei([
    *tafel("bc", "Weitere Grenzen"),
    z("§ 309 Nr. 9 b BGB, seit 1.3.2022:", 110, 190, "bc", "Bold", 38),
    z("stillschweigende Verlängerung nur auf", 160, 255, beim("bc", "Verlängert"), size=36),
    z("unbestimmte Zeit,", 160, 307, beim("bc", "unbestimmte"), size=36),
    z("Kündigungsfrist höchstens 1 Monat", 160, 359, beim("bc", "höchstens"), size=36),
    zit("Altverträge vor dem 1.3.2022: Art. 229 § 60 Satz 2 EGBGB", 160, 415, beim("bc", "Kündigungsfrist")),
    linienzug([(110, 490), (1150, 490)], "button", breite=3),
    z("§ 312k BGB: Kündigungsbutton", 110, 520, "button", "Bold", 38),
    *okz("Mira hat online gebucht: Rolf muss einen", 590, beim("button", "online"), "Bold", 34, x=160),
    z("Kündigungsbutton anbieten", 160, 642, beim("button", "Kündigungsbutton"), "Bold", 34),
    *requisit([("bc", ("tabler", "refresh", 100, WEISS), "Verlängerung", WEISS),
               ("button", ("tabler", "click", 100, WEISS), "Kündigungsbutton", GRUEN)]),
    *paar("bc", "MI", [("bc", "ruhig"), ("button", "froh")], "RO", [("bc", "ruhig")]),
]))

# L VII. Rechtsfolge (Wortlaut § 306 Abs. 1, 2) ---------------------------------------------------------------------------------
W306A = ["„(1) Sind Allgemeine Geschäftsbedingungen ganz oder teilweise nicht",
         "Vertragsbestandteil geworden oder unwirksam, so bleibt der Vertrag",
         "im Übrigen wirksam."]
W306B = ["(2) Soweit die Bestimmungen nicht Vertragsbestandteil geworden oder",
         "unwirksam sind, richtet sich der Inhalt des Vertrags nach den",
         "gesetzlichen Vorschriften.“"]
w306a, w306a_y = wortlaut(80, 160, 1100, W306A, "§ 306 Abs. 1 BGB", "w306", marken=[
    (2, "im Übrigen wirksam", beim("w306", "Übrigen"))], size=30)
w306b, w306b_y = wortlaut(80, w306a_y + 14, 1100, W306B, "§ 306 Abs. 2 BGB", "w306b", marken=[
    (2, "gesetzlichen Vorschriften", beim("w306b", "gesetzlichen"))], size=30)
folie([("rf", "AGB-Kontrolle › VII. Rechtsfolge, § 306 BGB"), ("red", "VII. Rechtsfolge › keine geltungserhaltende Reduktion")],
      rechts_frei([
    *tafel("rf", "VII. Rechtsfolge"),
    *w306a, *w306b,
    *neinz("nicht auf 2 Jahre gekürzt: Klausel fällt ganz weg", w306b_y + 22, "red", "Bold", 34, x=160),
    z("Verbot der geltungserhaltenden Reduktion", 160, w306b_y + 74, beim("red", "Verbot"), "Bold", 34),
    zit("BGH, Urt. v. 21.12.2011 – VIII ZR 262/09, Rn. 24", 160, w306b_y + 122, beim("red", "Bundesgerichtshof")),
    z("§ 306 Abs. 3 BGB: unzumutbare Härte, Vertrag unwirksam", 110, w306b_y + 178, "abs3h", size=32),
    *requisit([("rf", ("ph", "scales", 120, WEISS), "Rechtsfolge", WEISS),
               (beim("w306", "bleibt"), ("tabler", "file-check", 100, GRUEN), "Vertrag bleibt", GRUEN),
               ("w306b", ("tabler", "book", 100, WEISS), "Gesetz", WEISS),
               ("red", ("tabler", "eraser", 110, WEISS), "fällt ganz weg", HELLROT),
               ("abs3h", ("tabler", "alert-triangle", 100, GELB), "Ausnahme", WEISS)]),
    *paar("rf", "MI", [("rf", "ruhig"), ("red", "froh")], "RO", [("rf", "ruhig"), ("red", "sorge")]),
]))

# M Ergebnis ---------------------------------------------------------------------------------------------------------------------
folie([("erg", "Ergebnis · Kurs-Abo ohne Mindestlaufzeit")], rechts_frei([
    *tafel("erg", "Ergebnis"),
    blk(110, 190, 1040, 150, GRUEN, "erg", [("Kurs-Abo bleibt wirksam,", "ExtraBold", 40, INK),
                                          ("aber ohne Mindestlaufzeit", "ExtraBold", 40, INK)]),
    z("unbestimmte Zeit: Kündigung nach dem Gesetz", 110, 390, "erg2", "Bold", 36),
    z("Monatsbeitrag: spätestens am 15. zum Monatsende", 160, 445, beim("erg2", "Monatsbeitrag"), size=34),
    zit("§ 306 Abs. 2 i. V. m. §§ 620 Abs. 2, 621 Nr. 3 BGB", 160, 497, beim("erg2", "Monatsbeitrag")),
    *okz("Kündigung Anfang Juli: Abo endet am 31.7.", 580, "erg3", "Bold", 36, x=160),
    *requisit([("erg", ("tabler", "file-check", 100, GRUEN), "wirksam", GRUEN),
               ("erg3", ("tabler", "calendar-event", 100, WEISS), "Ende Juli", GRUEN)]),
    *paar("erg", "MI", [("erg", "froh")], "RO", [("erg", "sorge")]),
]))

# N Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · Reihenfolge und Kontrollfähigkeit")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Reihenfolge der Inhaltskontrolle:", 200, 200, beim("tipp", "Reihenfolge"), "Bold", 38),
    z("erst § 309, dann § 308, dann § 307 BGB", 200, 260, beim("tipp", "erst"), size=36),
    z("Vorher: Kontrollfähigkeit, § 307 Abs. 3 BGB", 200, 370, "tipp2", "Bold", 36),
    z("Preis der Hauptleistung: nur Transparenzgebot", 200, 430, beim("tipp2", "Preis"), size=34),
    zit("§ 307 Abs. 3 Satz 2 BGB; BGH, Urt. v. 14.1.2025 – XI ZR 35/24, Rn. 19", 200, 490, beim("tipp2", "Transparenzgebot")),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# O Klausurschema -------------------------------------------------------------------------------------------------------------------
K1, K2 = 150, 230
folie([("sch", "Klausurschema"), ("k3", "Klausurschema › III. Einbeziehung"), ("k6", "Klausurschema › VI. Inhaltskontrolle"),
       ("k7", "Klausurschema › VII. Rechtsfolge")], [
    karte(60, 50, 1800, 900, "sch"),
    titel(glyphen("Klausurschema: AGB-Kontrolle, §§ 305 ff. BGB"), 110, 90, "sch", 46),
    z("I. Anwendungsbereich, § 310 BGB", K1, 190, "k1", "Bold", 40, rechts=1820),
    z("II. AGB-Begriff, § 305 Abs. 1 BGB", K1, 260, "k2", "Bold", 40, rechts=1820),
    z("III. Einbeziehung, § 305 Abs. 2, 3 BGB", K1, 330, "k3", "Bold", 40, rechts=1820),
    z("Vorrang der Individualabrede, § 305b BGB", K2, 382, beim("k3", "Vorrang"), size=36, rechts=1820),
    z("IV. keine überraschende Klausel, § 305c Abs. 1 BGB", K1, 450, "k4", "Bold", 40, rechts=1820),
    z("V. Auslegung, § 305c Abs. 2 BGB", K1, 520, "k5", "Bold", 40, rechts=1820),
    z("Zweifel zu Lasten des Verwenders", K2, 572, beim("k5", "Zweifel"), size=36, rechts=1820),
    z("VI. Inhaltskontrolle, §§ 307–309 BGB", K1, 640, "k6", "Bold", 40, rechts=1820),
    z("§ 309 vor § 308 vor § 307 BGB", K2, 692, beim("k6", "dreihundertneun"), size=36, rechts=1820),
    z("VII. Rechtsfolge, § 306 BGB", K1, 760, "k7", "Bold", 40, rechts=1820),
])

# P Merksatz (Lexi) ------------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Eine unwirksame Klausel", 0)], [("fällt ", 0), ("ganz weg.", "a")]],
                750, 320, 46, "merke", {"a": beim("merke", "ganz")}),
    *markertext([[("Der Vertrag ", 0), ("bleibt,", "b"), (" und in", 0)], [("die Lücke tritt ", 0), ("das Gesetz.", "c")]],
                750, 560, 46, "m2", {"b": beim("m2", "bleibt"), "c": beim("m2", "Gesetz")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
