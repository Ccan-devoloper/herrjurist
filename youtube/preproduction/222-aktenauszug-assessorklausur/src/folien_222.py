"""Folge 222 · Aktenauszug Assessorklausur: Die ersten 20 Minuten mit der Akte – Serienstandard Open Peeps (Katzenkönig).
Fall: Zweites Examen, Zivilrechtsklausur, fünf Stunden. Hermine liest zuerst den Bearbeitervermerk (Rubrum,
Streitwertfestsetzung und Rechtsbehelfsbelehrung erlassen), dann die Akte: Herr Rehberg verlangt von Frau Pohlmann die
Mietkaution von 1.500 € zurück; sie behält sie wegen Kratzern im Parkett.
Szenen laut ../SZENENPLAN.md: A1 Klausurraum 9 Uhr, A2 In der Akte (Frage), B Sachverhalt, C Überblick (Aktenauszug,
Zeitachse), D1/D2 1. Bearbeitervermerk (Min. 0–5), E1/E2 2. Erster Durchgang (Min. 5–15), F1 Zivilurteil (Wortlautkarte
§ 313 Abs. 2 ZPO), F2 Verwaltungsurteil (Wortlautkarte § 117 Abs. 2 VwGO), F3 Anklage (Wortlautkarte § 200 Abs. 1 StPO),
G 3. Arbeitsblatt (Min. 15–20, Muster), H1/H2 Fallen, I Klausurtipp (Lexi), J Schema, K Merksatz (Lexi).
Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/feld/requisit/stehend als eigene Kopie aus Folge 219
(gemeinsame Dateien unverändert); neu: zeitachse() (Zeitachse 0–20 Minuten), parkett(), blatt_zeile().
Keine Geräusche: Im Bild gibt es keine Handlung, zu der ein erlaubtes Handlungsgeräusch passt (Blättern ist ausgeschlossen).
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut nach gesetze-im-internet.de, Abruf 07.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_222/"

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
        assert g >= 26 and F(s, g).getlength(glyphen(t)) <= w - 30, f"Blockzeile zu breit: {t}"
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
        if n.startswith(("bild:", "ficon:")) or "/op_222/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def dicon(*a, **k):
    """Icon als Teil eines Diagramms innerhalb der Tafel, nicht als Requisit."""
    e = ficon(*a, **k)
    e.name = "diagramm:" + (e.name or "")
    return e


def umbruch(text, size, breite, stil="Regular"):
    f = F(stil, size); zeilen, akt = [], ""
    for w in text.split(" "):
        t = (akt + " " + w).strip()
        if f.getlength(t) <= breite:
            akt = t
        else:
            zeilen.append(akt); akt = w
    return zeilen + [akt]


def wortlaut(x, y, w, text, quelle, cue, marken=(), size=32, bis=None):
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 07.10.2026), als Zitat mit Normangabe; der
    Zeilenumbruch wird berechnet. marken = [(wort, cue)] legt synchron zum gesprochenen Wort einen Textmarker hinter die
    erste noch nicht markierte Fundstelle von 'wort' (muss in einer Zeile stehen)."""
    zeilen = umbruch(glyphen(text), size, w - 60)
    lh = int(size * 1.42)
    hgt = 40 + lh * len(zeilen) + 46
    els = [bis_(karte(x, y, w, hgt, cue, fill=ZITAT, rund=18, schatten=6, rand=4), bis)]
    f = F("Regular", size)
    tx, ty = x + 28, y + 26
    belegt = []
    for wort, mc in marken:
        treffer = None
        for zi, t in enumerate(zeilen):
            a = t.find(wort)
            while a >= 0 and (zi, a) in belegt:
                a = t.find(wort, a + 1)
            if a >= 0:
                treffer = (zi, a); break
        assert treffer, f"Marker {wort!r} nicht in einer Zeile: {zeilen}"
        belegt.append(treffer)
        zi, a = treffer; t = zeilen[zi]
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 160/203/217/219) ---------------------------------
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
    return pl(text, cx, unten + 22, cue, fill=fill, size=26 if len(text) > 14 else 30, anker="m", **k)


def okz(text, y, cue, stil="Regular", size=34, x=185, gr=20, haken=None, **k):
    """Tafelzeile mit Bleistift-Haken davor; haken = Cue der gesprochenen Bejahung (sonst mit der Zeile)."""
    return [bis_(ok(x - 45, y + 20, haken or cue, gr=gr), k.get("bis")), z(text, x, y, cue, stil, size, **k)]


def neinz(text, y, cue, stil="Regular", size=34, x=185, gr=20, kreuz=None, **k):
    """Tafelzeile mit Bleistift-Kreuz davor; kreuz = Cue der gesprochenen Verneinung (sonst mit der Zeile)."""
    return [bis_(nein(x - 45, y + 20, kreuz or cue, gr=gr), k.get("bis")), z(text, x, y, cue, stil, size, **k)]


def _feld(w, h, fill=WEISS, rand=4, rund=14):
    s = 2
    im = Image.new("RGBA", ((w + 12) * s, (h + 12) * s)); dr = ImageDraw.Draw(im)
    o = 6 * s
    dr.rounded_rectangle((o, o, o + w * s, o + h * s), rund * s, fill=fill, outline=INK, width=rand * s)
    return im.resize((w + 12, h + 12), Image.LANCZOS)


def feld(x, y, w, h, cue, fill=WEISS, rand=4, rund=14, bis=None, anim="cut", name="feld"):
    return El(_feld(w, h, fill, rand, rund), x, y, cue, anim, 0.0, bis, name=name)


# --- Besetzung und Maße ----------------------------------------------------------------------------------------------------
BODEN, FH = 860, 480                        # Fallszenen: Bodenlinie, Figurenhöhe
X1, X2 = 1400, 1720                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
PX, PY, PU = 1575, 150, 370                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"HE": "Hermine", "AU": "Aufsicht", "RB": "Herr Rehberg", "PO": "Frau Pohlmann"}
NFARBE = {"HE": LILA, "AU": BLAU, "RB": GRUEN, "PO": ORANGE}


def boden(cue, hart_=True):
    e = linienzug([(40, BODEN), (1880, BODEN)], cue, breite=7, farbe=INK)
    return hart(e) if hart_ else e


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
    els = [*fig(k, x, FB, FR, folge, bis=bis), bis_(ns(NAME[k], x, FB, folge[0][0], NFARBE[k], d=0.1), bis)]
    return rechts_frei(els, 1200)


def paar(af, bf, a="RB", b="PO"):
    """Tafelszene: Herr Rehberg (links) und Frau Pohlmann (rechts) neben der Tafel, beide blicken zur Tafel."""
    return [*stehend(a, X1, af), *stehend(b, X2, bf)]


def fall_ns(k, x, cue, **kw):
    return ns(NAME[k], x, BODEN, cue, NFARBE[k], **kw)



# --- eigene Szenenbausteine Folge 222 --------------------------------------------------------------------------------------
GRAUHELL = (226, 226, 230, 255)
ZFARBEN = [BLAU, GELB, GRUEN]                                  # Bearbeitervermerk, erster Durchgang, Arbeitsblatt
ZMIN = [(0, 5), (5, 15), (15, 20)]


def zm(text, cx, y, cue, stil="Regular", size=30, **k):
    """Tafelzeile, mittig auf cx gesetzt."""
    return z(text, round(cx - F(stil, size).getlength(glyphen(text)) / 2), y, cue, stil, size, **k)


def zeitachse(x0, y, breite, h, cues, aktiv=None, beschriftung=True, bis=None):
    """Zeitachse der ersten 20 Minuten (maßstäblich, 1 Minute = breite/20). cues = Cue je Abschnitt (Erscheinen);
    aktiv = Index des hervorgehobenen Abschnitts (die übrigen grau)."""
    els = []
    for i, ((a, b), c) in enumerate(zip(ZMIN, cues)):
        xa, xb = x0 + breite * a / 20, x0 + breite * b / 20
        fill = ZFARBEN[i] if aktiv is None or aktiv == i else GRAUHELL
        txt = f"Min. {a}–{b}" if not beschriftung else f"{b - a} Min."
        els.append(blk(round(xa), y, round(xb - xa), h, fill, c, [(txt, "ExtraBold" if aktiv == i or aktiv is None else "Bold",
                                                                    26 if h < 60 else 30, INK)], rund=10, rand=4, anim="pop",
                       bis=bis))
    return els


def parkett(x, y, w, h, kratzer=False):
    """Parkettstreifen (programmatisch: Dielen in Holzfarbe, Fugen in Tusche); kratzer=True zeigt helle Kratzer."""
    s = 2
    im = Image.new("RGBA", ((w + 12) * s, (h + 12) * s)); dr = ImageDraw.Draw(im)
    o = 6 * s
    dl = 46
    for k, xx in enumerate(range(0, w, dl)):
        farbe = (205, 150, 98, 255) if k % 2 else (220, 168, 116, 255)
        dr.rectangle((o + xx * s, o, o + min(w, xx + dl) * s, o + h * s), fill=farbe, outline=INK, width=2 * s)
    dr.rectangle((o, o, o + w * s, o + h * s), outline=INK, width=4 * s)
    if kratzer:
        for (a, b, c, d) in [(0.18, 0.25, 0.42, 0.70), (0.30, 0.20, 0.55, 0.80), (0.60, 0.30, 0.83, 0.65)]:
            dr.line((o + a * w * s, o + b * h * s, o + c * w * s, o + d * h * s), fill=(255, 245, 225, 255), width=5 * s)
            dr.line((o + a * w * s, o + b * h * s + 4 * s, o + c * w * s, o + d * h * s + 4 * s), fill=INK, width=2 * s)
    return im.resize((w + 12, h + 12), Image.LANCZOS)


def parkett_el(x, y, w, h, cue, kratzer=False, bis=None, anim="cut"):
    return El(parkett(x, y, w, h, kratzer), x, y, cue, anim, 0.0, bis, name="parkett" + ("_kratzer" if kratzer else ""))


def he(folge, bis=None, x=FX):
    """Hermine allein neben der Tafel (blickt nach links zur Tafel), mit Namensschild."""
    return stehend("HE", x, folge, bis=bis)


def mini(aktiv, cue):
    """Kleine Zeitachse unten in der Tafel: aktueller Schritt farbig."""
    return zeitachse(110, 836, 1040, 44, [cue] * 3, aktiv=aktiv, beschriftung=False)


def sachverhalt_222(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 56)]
    y = 205
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=38, zeilenabstand=1.30)
        els += e; y += 14
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=36))
    folie([(cue, "Sachverhalt")], els)


# ===========================================================================================================================
# A1 Fall: Klausurraum, 9 Uhr – der Bearbeitervermerk
# ===========================================================================================================================
HEX, AUX, UHRX = 900, 1640, 1640
TISCH = ficon("tabler", "desk", HEX, BODEN - 2, 360, NULL, fuell=HOLZ, anim="cut")
TOP = TISCH.y + 8
HEa = ("HE_redet", HEX, BODEN, FH)
AUa = ("AU_redet", AUX, BODEN, FH)
VK = (70, 120, 620, 470)                                       # Vermerk-Karte links oben
folie([(NULL, "Fall · Zweites Examen, 9 Uhr"), ("hinten", "Fall · Der Bearbeitervermerk")], [
    boden(NULL),
    hart(pl("Zweites Examen: Klausur im Zivilrecht", 70, 30, NULL, fill=GELB, size=40)),
    hart(ficon("tabler", "clock-hour-9", UHRX, 250, 110, NULL, fuell=WEISS)),
    hart(pl("9 Uhr", UHRX, 268, NULL, fill=WEISS, size=30, anker="m")),
    *fig("HE", HEX, BODEN, FH, [(NULL, "ruhig"), ("hinten", "liest")], erst="cut", bis="h1"),
    *redet("HE_redet", HEX, BODEN, FH, "h1", "vorn"),
    hart(fall_ns("HE", HEX, NULL)),
    *fig("AU", AUX, BODEN, FH, [(NULL, "ruhig")], erst="cut", bis="auf1"),
    *redet("AU_redet", AUX, BODEN, FH, "auf1", "hinten"),
    *fig("AU", AUX, BODEN, FH, [("hinten", "ruhig")], erst="cut"),
    hart(fall_ns("AU", AUX, NULL)),
    TISCH,
    bis_(hart(ficon("tabler", "folder", HEX - 40, TOP, 120, NULL, fuell=GELB)), "hinten"),
    pl("30 Seiten Akte", 520, 680, beim("akte", "dreißig"), fill=WEISS, size=30, anker="m", bis="h1"),
    blase("sprech", 600, 210, "auf1", 1250, 190, inhalt=["Bitte beginnen Sie.", "Sie haben 5 Stunden."], textsize=34,
          figur=AUa, bis="hinten"),
    hart(ficon("tabler", "folder-open", HEX - 40, TOP, 130, "hinten", fuell=GELB)),
    pl("ganz hinten", 520, 680, "hinten", fill=WEISS, size=30, anker="m", bis="h1"),
    karte(*VK, "vermerk", fill=HELL, rund=18, schatten=6, rand=4),
    z("Bearbeitervermerk", 100, 140, "vermerk", "ExtraBold", 34),
    z("Die Entscheidung des Gerichts", 100, 200, "entw", "Bold", 30),
    z("ist zu entwerfen.", 100, 240, "entw", "Bold", 30),
    z("Erlassen sind:", 100, 315, "erl", "Bold", 30),
    *neinz("Rubrum", 365, beim("erl", "Rubrum"), "Bold", 30, x=170, gr=18),
    *neinz("Streitwertfestsetzung", 420, beim("erl", "Streitwertfestsetzung"), "Bold", 30, x=170, gr=18),
    *neinz("Rechtsbehelfsbelehrung", 475, beim("erl", "Rechtsbehelfsbelehrung"), "Bold", 30, x=170, gr=18),
    blase("sprech", 600, 240, "h1", 1250, 190, inhalt=["Drei Teile erlassen.", "Was genau muss ich", "also schreiben?"],
          textsize=34, figur=HEa),
])

# ===========================================================================================================================
# A2 Fall: In der Akte – Herr Rehberg und Frau Pohlmann
# ===========================================================================================================================
RBX, POX = 470, 1360
RBa = ("RB_redet_r", RBX, BODEN, FH)
POa = ("PO_redet", POX, BODEN, FH)
folie([("vorn", "Fall · In der Akte"), ("frage", "Fall · Die Frage")], [
    boden("vorn", hart_=False),
    pl("vorn in der Akte", 70, 30, "vorn", fill=GELB, size=40),
    ficon("tabler", "folder-open", 915, BODEN - 40, 260, "vorn", fuell=GELB, bis=beim("streit", "früheren")),
    ficon("tabler", "home", 915, BODEN - 70, 230, beim("streit", "früheren"), fuell=WEISS),
    pl("frühere Mietwohnung", 915, 450, beim("streit", "früheren"), fill=WEISS, size=30, anker="m", bis="frage"),
    pl("Mietkaution: 1.500 €", 915, 372, beim("streit", "Mietkaution"), fill=GELB, size=32, anker="m", bis="frage"),
    parkett_el(700, BODEN - 64, 430, 56, beim("streit", "früheren"), bis=beim("p1", "zerkratzt"), anim="pop"),
    parkett_el(700, BODEN - 64, 430, 56, beim("p1", "zerkratzt"), kratzer=True),
    pl("zerkratzt?", 915, 520, beim("p1", "zerkratzt"), fill=ROT, size=30, anker="m", bis="frage"),
    *fig("RB", RBX, BODEN, FH, [(beim("streit", "Rehberg"), "ruhig_r")], bis="r1"),
    *redet("RB_redet_r", RBX, BODEN, FH, "r1", "p1"),
    *fig("RB", RBX, BODEN, FH, [("p1", "ruhig_r"), ("frage", "redet_r")], erst="cut"),
    fall_ns("RB", RBX, beim("streit", "Rehberg"), d=0.1),
    *fig("PO", POX, BODEN, FH, [(beim("streit", "Pohlmann"), "ruhig")], bis="p1"),
    *redet("PO_redet", POX, BODEN, FH, "p1", "frage"),
    *fig("PO", POX, BODEN, FH, [("frage", "redet")], erst="cut"),
    fall_ns("PO", POX, beim("streit", "Pohlmann"), d=0.1),
    blase("sprech", 600, 200, "r1", 700, 190, inhalt=["Ich will meine Kaution", "zurück, 1.500 €."], textsize=36,
          figur=RBa, bis="p1"),
    blase("sprech", 620, 200, "p1", 1160, 190, inhalt=["Das Parkett ist zerkratzt.", "Die Kaution behalte ich."],
          textsize=36, figur=POa, bis="frage"),
    pl("Was tust du in den ersten 20 Minuten mit der Akte,", 960, 130, "frage", fill=PINK, size=38, anker="m"),
    pl("bevor du eine Zeile schreibst?", 960, 220, "frage2", fill=PINK, size=38, anker="m"),
])

# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
sachverhalt_222("sv", [
    "Zweites Examen, Klausur im Zivilrecht, 5 Stunden. Vor Hermine liegt eine Akte mit 30 Seiten. Ganz hinten steht der "
    "Bearbeitervermerk: „Die Entscheidung des Gerichts ist zu entwerfen. Rubrum, Streitwertfestsetzung und "
    "Rechtsbehelfsbelehrung sind erlassen.“ Hermine: „Drei Teile erlassen. Was genau muss ich also schreiben?“",
    "In der Akte verlangt Herr Rehberg von seiner früheren Vermieterin, Frau Pohlmann, die Mietkaution zurück: "
    "„Ich will meine Kaution zurück, 1.500 €.“ Frau Pohlmann: „Das Parkett ist zerkratzt. Die Kaution behalte ich.“",
], "Was tust du in den ersten 20 Minuten mit der Akte?")

# ===========================================================================================================================
# C Überblick: Aktenauszug und Zeitachse der ersten 20 Minuten
# ===========================================================================================================================
p_s = pl("Schriftsätze", 150, 300, beim("auszug", "Schriftsätze"), fill=BLAU, size=32)
p_a = pl("Anlagen", p_s.x + p_s.sprite.width + 24, 300, beim("auszug", "Anlagen"), fill=GELB, size=32)
p_p = pl("Protokolle", p_a.x + p_a.sprite.width + 24, 300, beim("auszug", "Protokolle"), fill=GRUEN, size=32)
ZA0, ZAY, ZAW = 110, 570, 1040
folie([("auszug", "Überblick · Aktenauszug statt Sachverhalt"), ("empf", "Überblick › die ersten 20 Minuten")], rechts_frei([
    *tafel("auszug", "Im zweiten Examen: der Aktenauszug"),
    z("in der Regel kein fertiger Sachverhalt,", 110, 180, beim("auszug", "keinen"), "Bold", 34),
    z("sondern ein Aktenauszug:", 110, 230, beim("auszug", "sondern"), "Bold", 34),
    p_s, p_a, p_p,
    z("Den Streitstoff ordnest du erst selbst.", 110, 395, "ordnen", "Bold", 34),
    pl("Die ersten 20 Minuten: Empfehlung aus Erfahrung, keine Vorgabe", 110, 470, "empf", fill=PINK, size=28),
    *zeitachse(ZA0, ZAY, ZAW, 80, ["z1", "z2", "z3"]),
    zm("Bearbeitervermerk", ZA0 + ZAW * 2.5 / 20, ZAY + 100, "z1", "Bold", 28),
    zm("erster Durchgang", ZA0 + ZAW * 10 / 20, ZAY + 100, "z2", "Bold", 28),
    zm("Arbeitsblatt", ZA0 + ZAW * 17.5 / 20, ZAY + 100, "z3", "Bold", 28),
    *[zm(t, ZA0 + ZAW * m / 20, ZAY + 160, c, "Regular", 26, farbe=TEXT)
      for t, m, c in [("Min. 0", 0.6, "z1"), ("5", 5, "z1"), ("15", 15, "z2"), ("20", 19.6, "z3")]],
    *he([("auszug", "liest"), ("empf", "denkt"), ("z3", "froh")]),
    *requisit([("auszug", ("tabler", "folders", 120, GELB), "Aktenauszug", WEISS),
               ("empf", ("tabler", "clock", 110, WEISS), "20 Minuten", PINK)]),
]))

# ===========================================================================================================================
# D1 Schritt 1: Bearbeitervermerk – zuerst lesen, Rolle und Entwurf
# ===========================================================================================================================
RX = [(110, 320), (470, 320), (830, 320)]
rollen = [("Gericht", "Gericht", "Urteil", "Urteil"), ("Anwalt", "Anwalt", "Schriftsatz", "Schriftsatz"),
          ("Staatsanwaltschaft", "Staatsanwaltschaft", "Anklage", "Anklage")]
els_r = []
for (x, w), (t1, w1, t2, w2) in zip(RX, rollen):
    els_r += [blk(x, 420, w, 80, BLAUHELL, beim("rolle", w1), [(t1, "ExtraBold", 30 if len(t1) < 12 else 28, INK)]),
              pfeil(x + w / 2, 512, x + w / 2, 560, beim("produkt", w2), breite=7, kopf=20),
              blk(x, 570, w, 80, HELL, beim("produkt", w2), [(t2, "ExtraBold", 30, INK)])]
folie([("s1", "1. Bearbeitervermerk › zuerst lesen"), ("rolle", "1. Bearbeitervermerk › Rolle und Entwurf")], rechts_frei([
    *tafel("s1", "1. Bearbeitervermerk · Min. 0–5"),
    z("zuerst lesen, auch wenn er ganz hinten steht", 110, 180, beim("s1", "Lies"), "Bold", 34),
    blk(110, 245, 1040, 75, GELB, "auftrag", [("Er ist dein Arbeitsauftrag.", "ExtraBold", 34, INK)]),
    z("Wer bist du?", 110, 355, "rolle", "Bold", 36),
    *els_r,
    ring(110 + 160, 460, 190, 60, "her1", farbe=ORANGE, breite=6),
    z("Hermine entscheidet als Gericht.", 110, 700, "her1", "Bold", 34),
    *mini(0, "s1"),
    *he([("s1", "liest"), ("rolle", "denkt"), ("her1", "froh")]),
    *requisit([("s1", ("tabler", "file-description", 100, WEISS), "Bearbeitervermerk", BLAU),
               ("rolle", ("tabler", "users", 120, WEISS), "Wer bist du?", WEISS),
               ("her1", ("tabler", "gavel", 110, HOLZ), "als Gericht", BLAU)]),
]))

# ===========================================================================================================================
# D2 Schritt 1: Bearbeitervermerk – erlassen und Stichtag
# ===========================================================================================================================
els_t = []
for (x, w), wort, t in zip([(110, 250), (390, 300), (720, 430)], ["Tenor", "Tatbestand", "Entscheidungsgründe"],
                           ["Tenor", "Tatbestand", "Entscheidungsgründe"]):
    els_t += [blk(x + 40, 380, w - 40, 75, HELLGRUEN, beim("rest2", wort), [(t, "ExtraBold", 30, INK)]),
              ok(x + 16, 417, beim("rest2", wort), gr=18)]
folie([("erlassen", "1. Bearbeitervermerk › was ist erlassen?"), ("datum", "1. Bearbeitervermerk › Stichtag")], rechts_frei([
    *tafel("erlassen", "1. Bearbeitervermerk · erlassen, Stichtag"),
    z("erlassen = diesen Teil musst du nicht schreiben", 110, 180, beim("erlassen", "Erlassen"), "Bold", 34),
    z("Alles andere gehört grundsätzlich in den Entwurf.", 110, 245, "rest", "Bold", 34),
    z("Bei Hermine also:", 110, 315, "rest2", "Bold", 32),
    *els_t,
    z("Nennt der Vermerk ein Datum: dein Stichtag", 110, 510, "datum", "Bold", 34),
    blk(110, 570, 560, 80, GELB, beim("datum", "dreißigsten"), [("Entscheidung am 30.9.2026", "ExtraBold", 32, INK)]),
    z("Von diesem Tag aus: Welche Fristen sind abgelaufen?", 110, 700, "stich", "Bold", 32),
    *mini(0, "erlassen"),
    *he([("erlassen", "denkt"), ("rest2", "liest"), ("datum", "schreibt"), ("stich", "froh")]),
    *requisit([("erlassen", ("tabler", "file-x", 100, WEISS), "erlassen", HELLROT),
               ("rest", ("tabler", "list-check", 110, WEISS), "in den Entwurf", HELLGRUEN),
               ("datum", ("tabler", "calendar-event", 110, WEISS), "30.9.2026", GELB)]),
]))

# ===========================================================================================================================
# E1 Schritt 2: erster Durchgang – Beteiligte und Anträge
# ===========================================================================================================================
folie([("s2", "2. Erster Durchgang › Beteiligte"), ("antr", "2. Erster Durchgang › Anträge")], rechts_frei([
    *tafel("s2", "2. Erster Durchgang · Min. 5–15"),
    z("mit Stift, aber noch ohne zu prüfen", 110, 180, beim("s2", "Stift"), "Bold", 34),
    z("Beteiligte:", 110, 260, "bet", "Bold", 36),
    pl("Kläger: Herr Rehberg", 150, 320, "kl", fill=GRUEN, size=32),
    pl("Beklagte: Frau Pohlmann", 560, 320, "bk", fill=ORANGE, size=32),
    z("Anträge:", 110, 430, "antr", "Bold", 36),
    blk(110, 490, 1040, 110, HELL, "ak", [("Kläger: Zahlung von 1.500 €", "ExtraBold", 32, INK),
                                         ("nebst Zinsen seit Rechtshängigkeit", "Bold", 30, INK)]),
    blk(110, 625, 1040, 80, HELL, "ab", [("Beklagte: Klageabweisung", "ExtraBold", 32, INK)]),
    *mini(1, "s2"),
    *stehend("RB", X1, [("s2", "ruhig"), ("ak", "redet")]),
    *stehend("PO", X2, [("s2", "ruhig"), ("ab", "redet")]),
    pl("Kläger", X1, PY, "kl", fill=GRUEN, size=30, anker="m"),
    pl("Beklagte", X2, PY, "bk", fill=ORANGE, size=30, anker="m"),
    ficon("tabler", "writing", 1560, 330, 100, "s2", fuell=WEISS, bis="kl"),
    pl("mit Stift", 1560, PY, "s2", fill=WEISS, size=30, anker="m", bis="kl"),
]))

# ===========================================================================================================================
# E2 Schritt 2: erster Durchgang – Chronologie und Daten
# ===========================================================================================================================
ZS0, ZS1, ZSY = 150, 1110, 450
PUNKTE = [(220, "1.4.2021", [("Mietbeginn,", "d1"), ("Kaution gezahlt", beim("d1", "Kaution"))]),
          (470, "31.5.2025", [("Auszug", "d2")]),
          (730, "12.1.2026", [("Klage geht ein", "d3")]),
          (990, "20.1.2026", [("zugestellt", beim("d4", "zugestellt"))])]
els_z = [linienzug([(ZS0, ZSY), (ZS1, ZSY)], "chron", breite=8, farbe=INK),
         pfeil(ZS1 - 10, ZSY, ZS1 + 40, ZSY, "chron", breite=8, kopf=28)]
for x, datum, texte in PUNKTE:
    c0 = texte[0][1]
    els_z += [feld(x - 14, ZSY - 14, 16, 16, c0, fill=ROT, rand=4, rund=8, anim="pop", name="punkt"),
              zm(datum, x, ZSY - 80, c0, "ExtraBold", 32)]
    for i, (t, c) in enumerate(texte):
        els_z.append(zm(t, x, ZSY + 40 + i * 42, c, "Bold", 28))
folie([("chron", "2. Erster Durchgang › Chronologie und Daten")], rechts_frei([
    *tafel("chron", "2. Erster Durchgang · Chronologie"),
    z("die Chronologie mit allen Daten", 110, 180, "chron", "Bold", 34),
    *els_z,
    *mini(1, "chron"),
    *he([("chron", "schreibt"), ("d3", "liest"), ("d4", "froh")]),
    *requisit([("chron", ("tabler", "calendar", 110, WEISS), "Chronologie", GELB),
               ("d3", ("tabler", "inbox", 110, WEISS), "Eingang", WEISS),
               (beim("d4", "zugestellt"), ("tabler", "send", 110, WEISS), "Zustellung", WEISS)]),
]))

# ===========================================================================================================================
# F1 Blick nach Klausurtyp: Zivilurteil, § 313 Abs. 2 ZPO (Wortlautkarte), unstreitig/streitig
# ===========================================================================================================================
W313 = ("„Im Tatbestand sollen die erhobenen Ansprüche und die dazu vorgebrachten Angriffs- und Verteidigungsmittel "
        "unter Hervorhebung der gestellten Anträge nur ihrem wesentlichen Inhalt nach knapp dargestellt werden.“")
w313, w313_y = wortlaut(110, 225, 1040, W313, "§ 313 Abs. 2 S. 1 ZPO", "zpo", marken=[
    ("erhobenen Ansprüche", beim("w313", "Ansprüche")),
    ("Angriffs- und Verteidigungsmittel", beim("w313", "Angriffs")),
    ("Anträge", beim("w313", "Anträge")),
    ("knapp", beim("w313", "knapp"))], size=28)
SPY = w313_y + 30
SP = [(110, 340, "unstreitig", beim("trenn", "unstreitig")), (460, 340, "Kläger behauptet", beim("trenn", "Kläger")),
      (810, 340, "Beklagte behauptet", beim("trenn", "Beklagte"))]
els_sp = []
for x, w, t, c in SP:
    els_sp += [feld(x, SPY, w, 190, c, fill=WEISS, anim="pop", name="spalte"), zm(t, x + w / 2, SPY + 14, c, "ExtraBold", 28)]
folie([("typ", "Klausurtyp · Zivilurteil"), ("zpo", "Zivilurteil › Tatbestand, § 313 Abs. 2 ZPO"),
       ("trenn", "Zivilurteil › unstreitig und streitig")], rechts_frei([
    *tafel("typ", "Blick nach Klausurtyp: Zivilurteil"),
    z("Worauf du achtest, hängt vom Entwurf ab.", 110, 172, "typ", "Bold", 32),
    *w313,
    *els_sp,
    zm("Mietvertrag, Kaution,", 280, SPY + 70, beim("unstr", "Mietvertrag"), "Bold", 28),
    zm("Auszug", 280, SPY + 110, beim("unstr", "Auszug"), "Bold", 28),
    zm("Kratzer im Parkett", 980, SPY + 70, beim("str", "Kratzer"), "Bold", 28),
    zm("bestreitet die Kratzer", 630, SPY + 70, beim("str", "bestreitet"), "Bold", 28),
    blk(110, SPY + 215, 1040, 66, GELB, "rel", [("Die Relation dazu: Folge 18", "ExtraBold", 30, INK)]),
    *he([("typ", "denkt"), ("zpo", "liest"), ("trenn", "schreibt"), ("rel", "froh")]),
    *requisit([("typ", ("tabler", "gavel", 110, HOLZ), "Zivilurteil", BLAU),
               ("trenn", ("tabler", "scale", 120, WEISS), "unstreitig / streitig", WEISS)]),
]))
assert SPY + 215 + 66 <= 895, SPY

# ===========================================================================================================================
# F2 Blick nach Klausurtyp: Verwaltungsurteil, § 117 Abs. 2 VwGO (Wortlautkarte, gekürzt)
# ===========================================================================================================================
W117 = ("„Das Urteil enthält 1. die Bezeichnung der Beteiligten …, 2. die Bezeichnung des Gerichts …, 3. die Urteilsformel, "
        "4. den Tatbestand, 5. die Entscheidungsgründe, 6. die Rechtsmittelbelehrung.“")
w117, w117_y = wortlaut(110, 225, 1040, W117, "§ 117 Abs. 2 VwGO", "vwgo", marken=[
    ("Beteiligten", beim("teile", "Beteiligten")), ("Rechtsmittelbelehrung", beim("teile", "Rechtsmittelbelehrung"))], size=30)
FY = w117_y + 30
q_b = pl("Bescheid", 150, FY + 120, beim("frist", "Bescheid"), fill=BLAU, size=30)
q_w = pl("Widerspruch", q_b.x + q_b.sprite.width + 20, FY + 120, beim("frist", "Widerspruch"), fill=GELB, size=30)
q_z = pl("Zustellungen", q_w.x + q_w.sprite.width + 20, FY + 120, beim("frist", "Zustellungen"), fill=GRUEN, size=30)
folie([("vwgo", "Verwaltungsurteil › § 117 Abs. 2 VwGO"), ("frist", "Verwaltungsurteil › Zustellungen und Klagefrist")],
      rechts_frei([
    *tafel("vwgo", "Blick nach Klausurtyp: Verwaltungsurteil"),
    z("die Teile des Urteils:", 110, 172, "vwgo", "Bold", 32),
    *w117,
    z("Diese Liste mit dem Vermerk abgleichen.", 110, FY, "abgl", "Bold", 34),
    z("markieren:", 110, FY + 70, "frist", "Bold", 34),
    q_b, q_w, q_z,
    blk(110, FY + 200, 1040, 70, HELL, beim("frist", "Monatsfrist"),
        [("Monatsfrist für die Anfechtungsklage, § 74 Abs. 1 VwGO", "ExtraBold", 30, INK)]),
    *he([("vwgo", "liest"), ("abgl", "denkt"), ("frist", "schreibt")]),
    *requisit([("vwgo", ("tabler", "building-bank", 120, WEISS), "Verwaltungsurteil", BLAU),
               (beim("frist", "Monatsfrist"), ("tabler", "calendar-time", 110, WEISS), "1 Monat", GELB)]),
]))
assert FY + 270 <= 895, FY

# ===========================================================================================================================
# F3 Blick nach Klausurtyp: Anklage, § 200 Abs. 1 S. 1 StPO (Wortlautkarte)
# ===========================================================================================================================
W200 = ("„Die Anklageschrift hat den Angeschuldigten, die Tat, die ihm zur Last gelegt wird, Zeit und Ort ihrer Begehung, "
        "die gesetzlichen Merkmale der Straftat und die anzuwendenden Strafvorschriften zu bezeichnen (Anklagesatz).“")
w200, w200_y = wortlaut(110, 225, 1040, W200, "§ 200 Abs. 1 S. 1 StPO", "stpo", marken=[
    ("Angeschuldigten", beim("stpo", "Angeschuldigten")), ("die Tat", beim("stpo", "Tat")),
    ("Zeit und Ort", beim("stpo", "Zeit")), ("gesetzlichen Merkmale", beim("stpo", "gesetzlichen")),
    ("Strafvorschriften", beim("stpo", "Strafvorschriften"))], size=30)
AY = w200_y + 30
r_1 = pl("wer?", 450, AY - 6, beim("jetat", "wer"), fill=GELB, size=32)
r_2 = pl("wann?", r_1.x + r_1.sprite.width + 20, AY - 6, beim("jetat", "wann"), fill=BLAU, size=32)
r_3 = pl("wo?", r_2.x + r_2.sprite.width + 20, AY - 6, beim("jetat", "wo"), fill=GRUEN, size=32)
folie([("stpo", "Anklage › § 200 Abs. 1 StPO"), ("jetat", "Anklage › für jede Tat: wer, wann, wo")], rechts_frei([
    *tafel("stpo", "Blick nach Klausurtyp: Anklage"),
    z("der Anklagesatz:", 110, 172, "stpo", "Bold", 32),
    *w200,
    z("für jede Tat:", 110, AY, "jetat", "Bold", 34),
    r_1, r_2, r_3,
    blk(110, AY + 100, 1040, 70, GELB, "ankl", [("Den Aufbau der Anklageklausur zeigt Folge 39.", "ExtraBold", 30, INK)]),
    *he([("stpo", "liest"), ("jetat", "schreibt"), ("ankl", "froh")]),
    *requisit([("stpo", ("tabler", "file-certificate", 110, WEISS), "Anklage", ROT),
               ("jetat", ("tabler", "notes", 110, WEISS), "je Tat", WEISS)]),
]))
assert AY + 170 <= 895, AY

# ===========================================================================================================================
# G Schritt 3: Arbeitsblatt (Muster) und Zeitplan
# ===========================================================================================================================
TICKS = [(260, "1.4.2021"), (500, "31.5.2025"), (740, "12.1.2026"), (980, "20.1.2026")]
els_g = [feld(110, 170, 1040, 100, "b1", fill=WEISS, anim="pop", name="zeile_auftrag"),
         z("Auftrag: Urteil · Stichtag 30.9.2026", 130, 180, "b1", "ExtraBold", 30),
         z("erlassen: Rubrum, Streitwert, Rechtsbehelfsbelehrung", 130, 225, beim("b1", "erlassenen"), "Regular", 28),
         feld(110, 285, 1040, 100, "b2", fill=WEISS, anim="pop", name="zeile_antraege"),
         z("Kläger Herr Rehberg: 1.500 € nebst Zinsen", 130, 295, "b2", "Bold", 28),
         z("Beklagte Frau Pohlmann: Klageabweisung", 130, 340, beim("b2", "Anträge"), "Bold", 28),
         feld(110, 400, 1040, 100, "b3", fill=WEISS, anim="pop", name="zeile_zeitstrahl"),
         linienzug([(150, 430), (1110, 430)], "b3", breite=6, farbe=INK)]
for x, t in TICKS:
    els_g += [feld(x - 10, 420, 12, 12, "b3", fill=ROT, rand=3, rund=6, anim="pop", name="tick"),
              zm(t, x, 448, "b3", "Bold", 26)]
for x, w, t, c in [(110, 340, "unstreitig", beim("b4", "unstreitig")), (460, 340, "Kläger behauptet", beim("b4", "Kläger")),
                   (810, 340, "Beklagte behauptet", beim("b4", "Beklagte"))]:
    els_g += [feld(x, 515, w, 150, c, fill=WEISS, anim="pop", name="spalte"), zm(t, x + w / 2, 527, c, "ExtraBold", 28)]
els_g += [zm("Vertrag, Kaution, Auszug", 280, 585, beim("b4", "unstreitig"), "Regular", 26),
          zm("keine Kratzer", 630, 585, beim("b4", "Kläger"), "Regular", 26),
          zm("Kratzer im Parkett", 980, 585, beim("b4", "Beklagte"), "Regular", 26)]
folie([("s3", "3. Arbeitsblatt › Muster"), ("zeitpl", "3. Arbeitsblatt › Zeitplan")], rechts_frei([
    *tafel("s3", "3. Arbeitsblatt · Min. 15–20 (Muster)"),
    feld(96, 158, 1068, 520, "blatt", fill=(250, 250, 246, 255), rand=3, rund=10, anim="pop", name="blatt"),
    *els_g,
    pl("beim genauen Lesen danach weiter füllen", 110, 690, "fuell", fill=PINK, size=28),
    z("Zum Schluss: übrige 4 Std. 40 Min. verteilen", 110, 775, "zeitpl", "Bold", 32),
    pl("Zeitplan: Folge 45", 880, 840, "f45", fill=GELB, size=28),
    *he([("s3", "schreibt"), ("fuell", "liest"), ("zeitpl", "froh")]),
    *requisit([("s3", ("tabler", "clipboard-list", 110, WEISS), "Arbeitsblatt", GRUEN),
               ("zeitpl", ("tabler", "hourglass", 100, GELB), "4 Std. 40 Min.", WEISS)]),
]))

# ===========================================================================================================================
# H1 Fallen 1 und 2: Hinweise im Vermerk, Anlagen
# ===========================================================================================================================
a_1 = pl("Mietvertrag", 150, 560, beim("f2", "Mietvertrag"), fill=BLAU, size=30)
a_2 = pl("Kostenvoranschlag", a_1.x + a_1.sprite.width + 20, 560, beim("f2", "Kostenvoranschlag"), fill=GELB, size=30)
a_3 = pl("Schreiben", a_2.x + a_2.sprite.width + 20, 560, beim("f2", "Schreiben"), fill=GRUEN, size=30)
folie([("fallen", "Fallen › 1. Hinweise im Vermerk"), ("f2", "Fallen › 2. Anlagen")], rechts_frei([
    *tafel("fallen", "Drei typische Fallen"),
    z("1. Hinweise im Vermerk", 110, 175, "f1", "ExtraBold", 36),
    z("„Die Zustellungen sind ordnungsgemäß.“", 150, 232, beim("f1", "Zustellungen"), "Regular", 32),
    z("unterstellen und nicht neu prüfen", 150, 282, beim("f1", "unterstellst"), "Bold", 32),
    z("erlassen ist nur das Schreiben, nicht das Denken:", 150, 345, "f1b", "Bold", 32),
    z("den Streitstoff trotzdem vollständig erfassen", 150, 395, beim("f1b", "Streitstoff"), "Bold", 32),
    z("2. Anlagen", 110, 490, "f2", "ExtraBold", 36),
    a_1, a_2, a_3,
    z("mitlesen", 150, 645, "f2b", "Bold", 32),
    z("Bei Hermine steht der Betrag nur im Kostenvoranschlag:", 150, 710, "f2c", "Regular", 30),
    pl("Reparatur: 1.650 €", 150, 770, beim("f2c", "eintausend"), fill=GELB, size=32),
    *he([("fallen", "denkt"), ("f1", "liest"), ("f1b", "denkt"), ("f2", "liest"), ("f2c", "froh")]),
    *requisit([("fallen", ("tabler", "alert-triangle", 110, GELB), "Fallen", ROT),
               ("f1", ("tabler", "file-description", 100, WEISS), "Hinweis im Vermerk", BLAU),
               ("f2", ("tabler", "paperclip", 100, WEISS), "Anlagen", GELB)]),
]))

# ===========================================================================================================================
# H2 Falle 3: die Daten – Eingang und Zustellung
# ===========================================================================================================================
folie([("f3", "Fallen › 3. Daten: Eingang und Zustellung"), ("p167", "Fallen › 3. Daten › Verjährung, § 167 ZPO")],
      rechts_frei([
    *tafel("f3", "3. Die Daten"),
    z("Eingang und Zustellung sind nicht dasselbe.", 110, 175, beim("f3", "Eingang"), "Bold", 34),
    blk(110, 240, 500, 100, BLAUHELL, beim("f3", "Eingang"), [("Eingang", "Bold", 28, INK), ("12.1.2026", "ExtraBold", 34, INK)]),
    blk(650, 240, 500, 100, BLAUHELL, beim("f3", "Zustellung"), [("Zustellung", "Bold", 28, INK), ("20.1.2026", "ExtraBold", 34, INK)]),
    z("rechtshängig erst mit der Zustellung", 110, 380, "rh", "ExtraBold", 34),
    zit("§ 253 Abs. 1, § 261 Abs. 1 ZPO", 110, 428, "rh"),
    z("von da an Prozesszinsen", 110, 480, "zins", "ExtraBold", 34),
    zit("§ 291 BGB", 110, 528, "zins"),
    ring(900, 290, 280, 70, "her3", farbe=ORANGE, breite=6),
    *okz("Zinsen: Zustellung am 20.1., nicht Eingang am 12.1.", 590, "her3", "Bold", 32, x=160,
         haken=beim("her3", "zwanzigsten")),
    blk(110, 680, 1040, 110, HELL, "p167", [("Verjährung: Der Eingang kann genügen,", "ExtraBold", 30, INK),
                                          ("wenn demnächst zugestellt wird, § 167 ZPO.", "Bold", 28, INK)]),
    *he([("f3", "liest"), ("rh", "denkt"), ("her3", "schreibt"), ("p167", "denkt")]),
    *requisit([(beim("f3", "Eingang"), ("tabler", "inbox", 110, WEISS), "Eingang", BLAUHELL),
               (beim("f3", "Zustellung"), ("tabler", "send", 110, WEISS), "Zustellung", BLAUHELL),
               ("zins", ("tabler", "coin-euro", 110, GELB), "Prozesszinsen", GELB),
               ("p167", ("tabler", "hourglass", 100, WEISS), "Verjährung", WEISS)]),
]))

# ===========================================================================================================================
# I Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · den Vermerk noch einmal lesen")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Bearbeitervermerk nach den 20 Minuten", 200, 200, beim("tipp", "Lies"), "Bold", 36),
    z("noch einmal lesen", 200, 255, beim("tipp", "noch"), "ExtraBold", 38),
    z("Mit der Akte im Kopf merkst du:", 200, 390, "tipp2", "Bold", 34),
    z("Habe ich die Aufgabe richtig verstanden?", 200, 445, beim("tipp2", "richtig"), "ExtraBold", 36),
    ficon("tabler", "eye", 640, 700, 150, beim("tipp", "noch"), fuell=WEISS),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# J Klausurschema (progressiv) mit Zeitachse
# ===========================================================================================================================
REIHEN = [("k1", "I.", "Bearbeitervermerk · Min. 0–5", BLAU, 0),
          ("k1a", "", "Rolle, Entwurf, erlassene Teile, Stichtag", None, 1),
          ("k2", "II.", "Erster Durchgang · Min. 5–15", GELB, 0),
          ("k2a", "", "Beteiligte, Anträge, Chronologie, Daten", None, 1),
          ("k2b", "", "je nach Entwurf: Tatbestand, Urteilsteile, Anklagesatz", None, 1),
          ("k3", "III.", "Arbeitsblatt · Min. 15–20", GRUEN, 0),
          ("k3a", "", "Zeitstrahl, Streitstand, Zeitplan", None, 1)]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Schema: Die ersten 20 Minuten mit der Akte"), 110, 90, "sch", 46)]
y = 200
for c, r, txt, farbe, ebene in REIHEN:
    if ebene == 0:
        els_sch += [karte(110, y, 110, 66, c, fill=farbe, rund=14, schatten=5, rand=4),
                    z(r, 165 - F("ExtraBold", 36).getlength(r) / 2, y + 9, c, "ExtraBold", 36, rechts=1820),
                    z(txt, 255, y + 9, c, "ExtraBold", 36, rechts=1820)]
        y += 92
    else:
        els_sch.append(z(txt, 330, y, c, "Bold", 34, rechts=1820))
        els_sch.append(ok(290, y + 22, c, gr=18))
        y += 74
assert y <= 860, y
els_sch += zeitachse(110, 880, 1700, 70, ["k1", "k2", "k3"], beschriftung=False)
folie([("sch", "Schema · die ersten 20 Minuten"), ("k1", "Schema › I. Bearbeitervermerk"),
       ("k2", "Schema › II. Erster Durchgang"), ("k3", "Schema › III. Arbeitsblatt")], els_sch)

# ===========================================================================================================================
# K Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Der ", 0), ("Bearbeitervermerk", "a")], [("bestimmt, was du ", 0), ("schreibst", "b"), (".", 0)]],
                750, 310, 52, "merke", {"a": beim("merke", "Bearbeitervermerk"), "b": beim("merke", "schreibst")}),
    *markertext([[("Was er nicht ", 0), ("erlässt", "c"), (",", 0)], [("gehört in deinen ", 0), ("Entwurf", "d"), (".", 0)]],
                750, 560, 52, "m2", {"c": beim("m2", "erlässt"), "d": beim("m2", "Entwurf")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
