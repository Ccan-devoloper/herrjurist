"""Folge 273 · Freischuss Jura: Freiversuch und Verbesserungsversuch erklärt – Serienstandard Open Peeps (Katzenkönig).
Rahmen: Leonore (Jurastudentin in Nordrhein-Westfalen, 7. Fachsemester, ein Auslandssemester) steht im Flur der
Fakultät vor dem Aushang mit den Meldefristen; ihr Freund Rasmus hat das Examen früh geschrieben und die Note verbessert.
Szenen laut ../SZENENPLAN.md: A1 Flur (Aushang), A2 Einstieg, B Sachverhalt, C Freiversuch (Wortlautkarte § 5d Abs. 5
S. 1–3 DRiG), D Folge für Leonore (Versuchsleiste), E Voraussetzungen in 3 Ländern (§ 25 I JAG NRW, § 18 I NJAG, § 29 I
SächsJAPO), F Semester, die nicht mitzählen (§ 25 II, III, V JAG NRW, § 17 NJAVO, § 29 I 4 SächsJAPO), G Leonore konkret
(Semesterleiste), H Verbesserungsversuch (§ 5d Abs. 5 S. 4 DRiG; §§ 26, 65 II Nr. 1 JAG NRW; § 19 NJAG mit Anl. 2 NJG
Nr. 7.3; § 31 SächsJAPO), I Was zählt am Ende (bessere Note, 2. Examen, Rasmus 7 → 9 Punkte), J Strategie, K Ergebnis
(Flur, Formular), L Klausurtipp (Lexi), M Freischuss in 5 Schritten, N Merksatz (Lexi).
Handlungsgeräusch: Leonore nimmt das Formular vom Aushang (K); ../geraeusche_herkunft.json.
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/redet/fig/ns/okz/neinz/requisit
als eigene Kopie aus Folge 237 (gemeinsame Dateien unverändert), wortlaut()/umbruch() aus Folge 201; neu: kasten(), pm(),
tuer(), zettel_bild(), pinnwand(), flur(), versuch(), landzeile(), spalte(), semester(), kopfzeile(), vzeile(),
punktebalken().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Normangaben nach gesetze-im-internet.de, recht.nrw.de,
voris.wolterskluwer-online.de (NI-VORIS) und revosax.sachsen.de, Abruf 08.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_273/"

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
HELLROT = (253, 232, 228, 255)
HELLGRUEN = (232, 247, 233, 255)
HELLBLAU = (226, 236, 252, 255)
HGELB = (253, 240, 196, 255)
HROT = (252, 214, 206, 255)
GRAU = (200, 200, 196, 255)
GRAU2 = (232, 232, 228, 255)
HOLZ = (214, 160, 110, 255)
HOLZ2 = (176, 122, 80, 255)
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


def zit(text, x, y, cue, size=28, **k):
    """Fundstellen-/Verweiszeile (grau, mindestens 26 px)."""
    return z(text, x, y, cue, size=size, farbe=TEXT, **k)


def rechts_frei(els, x0=1250):
    """Figuren und Requisiten der Tafelfolien stehen rechts der Tafel."""
    for e in els:
        n = e.name or ""
        if n.startswith(("bild:", "ficon:")) or "/op_273/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 168/180/201/237) ---------------------------------
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


def okz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Haken davor (zur gesprochenen Bejahung)."""
    return [bis_(ok(x - 45, y + 20, cue, gr=gr), k.get("bis")), z(text, x, y, cue, stil, size, **k)]


def neinz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Kreuz davor (zur gesprochenen Verneinung)."""
    return [bis_(nein(x - 45, y + 20, cue, gr=gr), k.get("bis")), z(text, x, y, cue, stil, size, **k)]


def ticon(*a, **k):
    """Icon als Teil einer Tafelgrafik (darf in der Tafel stehen, rechts_frei() prüft nur Requisiten neben der Tafel)."""
    e = ficon(*a, **k)
    e.name = "tafelicon:" + e.name.split(":", 1)[1]
    return e


def _flaeche(w, h, zeichne):
    s = 2
    im = Image.new("RGBA", (w * s, h * s))
    zeichne(ImageDraw.Draw(im), s)
    return im.resize((w, h), Image.LANCZOS)


# --- Figuren neben der Tafel ----------------------------------------------------------------------------------------------
X1, X2 = 1395, 1730                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Unterkante, Höhe neben der Tafel
FX = 1560                                   # eine Figur neben der Tafel
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"LE": "Leonore", "RA": "Rasmus"}
NFARBE = {"LE": BLAU, "RA": GELB}


def stehend(k, x, folge, unten=FB, hoehe=FR, bis=None):
    return [*fig(k, x, unten, hoehe, folge, bis=bis), ns(NAME[k], x, unten, folge[0][0], NFARBE[k], d=0.1, bis=bis)]


def requisit(folge, px=PX):
    """Wechselndes Requisit über den Figuren: folge = [(cue, (set, icon, breite, fuell), pillentext, pillenfarbe)];
    ein Eintrag (cue, None, None, None) beendet das vorige Requisit (z. B. vor einer Sprechblase)."""
    els = []
    for i, (c, ic, txt, pf) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else None
        if ic:
            s_, n_, br, fu = ic
            els.append(ficon(s_, n_, px, PU, br, c, fuell=fu, bis=b))
        if txt:
            els.append(pl(txt, px, PY, c, fill=pf, size=28, anker="m", bis=b))
    return els


def allein(k, folge):
    return stehend(k, FX, folge)




ZITAT = (246, 246, 250, 255)
KORK = (214, 170, 120, 255)
WAND = (238, 232, 220, 255)


def umbruch(text, size, breite, stil="Regular"):
    f = F(stil, size); zeilen, akt = [], ""
    for w in text.split(" "):
        t = (akt + " " + w).strip()
        if f.getlength(t) <= breite:
            akt = t
        else:
            zeilen.append(akt); akt = w
    return zeilen + [akt]


def wortlaut(x, y, w, text, quelle, cue, marken=(), size=30, bis=None):
    """Wortlautkarte (wie Folge 201): Normtext wörtlich nach gesetze-im-internet.de (Abruf 08.10.2026), als Zitat mit
    Normangabe; marken = [(wort, cue)] legt synchron zum gesprochenen Wort einen Textmarker hinter die erste noch nicht
    markierte Fundstelle von 'wort' (muss in einer Zeile stehen)."""
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


def kasten(x, y, w, h, fill, c, rund=14, rand=4, anim="pop", bis=None, name="kasten"):
    """Leerer Tabellen-/Zellenkasten (Text kommt zeilenweise mit z())."""
    def zz(dr, s):
        dr.rounded_rectangle((2 * s, 2 * s, (w - 2) * s, (h - 2) * s), rund * s, fill=fill, outline=INK, width=rand * s)
    return El(_flaeche(w, h, zz), x, y, c, anim, 0.0, bis, name=name)


def pm(text, x, y, cue, plus, size=32, stil="Bold", rechts=1170):
    """Zeile mit (+)/(−) in Dunkelgrün/Dunkelrot (Bewertung zur gesprochenen Chance bzw. zum Risiko)."""
    zei = "(+)" if plus else "(−)"
    a = z(zei, x, y, cue, "ExtraBold", size, farbe=(DGRUEN if plus else DROT))
    b = z(text, x + 70, y, cue, stil, size, rechts=rechts)
    return [a, b]


# --- Flur der Fakultät: Tür, Aushang (Pinnwand), Boden ---------------------------------------------------------------------
BODEN_Y = 905
FHA = 480
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
LEX, RAX = 520, 1530                         # Leonore (blickt nach rechts), Rasmus (blickt nach links)
PW = (760, 330, 440, 380)                    # Pinnwand x, y, w, h
FORM = (PW[0] + 250, PW[1] + 150, 150, 190)  # Formular am Aushang: x, y, w, h


def boden(c):
    return hart(linienzug([(60, BODEN_Y), (1860, BODEN_Y)], c, breite=7, farbe=INK))


def tuer(c, x0=110, y0=330, w=230):
    h = BODEN_Y - y0
    def zz(dr, s):
        dr.rectangle((3 * s, 3 * s, (w - 3) * s, (h - 1) * s), fill=(176, 122, 80, 255), outline=INK, width=5 * s)
        dr.rectangle((30 * s, 40 * s, (w - 30) * s, (h // 2 - 20) * s), outline=INK, width=4 * s)
        dr.rectangle((30 * s, (h // 2 + 10) * s, (w - 30) * s, (h - 40) * s), outline=INK, width=4 * s)
        dr.ellipse(((w - 52) * s, (h // 2 - 12) * s, (w - 30) * s, (h // 2 + 10) * s), fill=GELB, outline=INK, width=3 * s)
    return hart(El(_flaeche(w, h, zz), x0, y0, c, "cut", 0.0, None, name="tuer"))


def zettel_bild(w, h, kopf=None, linien=4, fill=WEISS, kopfsize=26):
    """Aushang-Zettel (programmatisch): Reißzwecke, Kopfzeile, graue Schreibzeilen."""
    def zz(dr, s):
        dr.rectangle((3 * s, 10 * s, (w - 3) * s, (h - 3) * s), fill=fill, outline=INK, width=3 * s)
        dr.ellipse(((w / 2 - 9) * s, 2 * s, (w / 2 + 9) * s, 20 * s), fill=ROT, outline=INK, width=3 * s)
        y = 34
        if kopf:
            for t in kopf:
                dr.text((14 * s, y * s), glyphen(t), font=F("ExtraBold", kopfsize * s), fill=INK)
                y += kopfsize + 6
            y += 6
        for k in range(linien):
            dr.line((14 * s, (y + k * 22) * s, (w - 20 - (k % 2) * 30) * s, (y + k * 22) * s), fill=GRAU, width=3 * s)
    return _flaeche(w, h, zz)


def pinnwand(c, mit_formular=True):
    x, y, w, h = PW
    def zz(dr, s):
        dr.rounded_rectangle((3 * s, 3 * s, (w - 3) * s, (h - 3) * s), 10 * s, fill=KORK, outline=INK, width=6 * s)
    els = [hart(El(_flaeche(w, h, zz), x, y, c, "cut", 0.0, None, name="pinnwand")),
           hart(El(zettel_bild(220, 230, ["Meldefristen", "Examen"], linien=5, kopfsize=28), x + 20, y + 30, c, "cut", 0.0, None,
                   name="zettel:Meldefristen Examen")),
           hart(El(zettel_bild(150, 110, None, linien=3, fill=HGELB), x + 260, y + 24, c, "cut", 0.0, None, name="zettel:gelb"))]
    return els


def formular_bild():
    return zettel_bild(FORM[2], FORM[3], ["Formular"], linien=4, fill=HELLBLAU, kopfsize=26)


def flur(c, mit_formular=True):
    els = [boden(c), tuer(c), *pinnwand(c)]
    if mit_formular:
        els.append(hart(El(formular_bild(), FORM[0], FORM[1], c, "cut", 0.0, None, name="formular")))
    return els


# ===========================================================================================================================
# A1 Fall: Flur der Fakultät – Aushang mit den Meldefristen
# ===========================================================================================================================
LE_A = ("LE_redet_r", LEX, BODEN_Y, FHA)
RA_A = ("RA_redet", RAX, BODEN_Y, FHA)
folie([(NULL, "Fall · Flur der juristischen Fakultät"), ("l1", "Fall · 7. Semester: jetzt schon melden?"),
       ("r1", "Fall · im Freischuss zählt ein Fehlversuch nicht")], [
    *flur(NULL),
    bis_(hart(pl("Flur der juristischen Fakultät", 70, 30, NULL, fill=GELB, size=38)), "l1"),
    ring(PW[0] + 130, PW[1] + 148, 140, 136, beim("leo", "Meldefristen"), farbe=ORANGE, breite=6, bis="l1"),
    pl("7. Semester", 225, 270, beim("l1", "siebten"), fill=BLAU, size=30, anker="m", bis="r1"),
    pl("Fehlversuch zählt nicht", PW[0] + PW[2] / 2, 270, beim("r1", "Fehlversuch"), fill=HELLGRUEN, size=30, anker="m"),
    # Leonore (links, blickt nach rechts zum Aushang und zu Rasmus)
    *fig("LE", LEX, BODEN_Y, FHA, [(NULL, "denkt_r"), (beim("leo", "Meldefristen"), "sorge_r")], erst="cut", bis="l1"),
    *redet("LE_redet_r", LEX, BODEN_Y, FHA, "l1", "r1"),
    *fig("LE", LEX, BODEN_Y, FHA, [("r1", "staunt_r")], erst="cut", bis="hook"),
    hart(ns(NAME["LE"], LEX, BODEN_Y, NULL, NFARBE["LE"])),
    # Rasmus (rechts, blickt nach links)
    *fig("RA", RAX, BODEN_Y, FHA, [(beim("ras", "Rasmus"), "froh")], erst="pop", bis="r1"),
    ns(NAME["RA"], RAX, BODEN_Y, beim("ras", "Rasmus"), NFARBE["RA"], d=0.1),
    *redet("RA_redet", RAX, BODEN_Y, FHA, "r1", "hook"),
    blase("sprech", 640, 230, "l1", 720, 190, inhalt=["Ich bin im 7. Semester. Soll ich", "mich jetzt schon melden?",
                                                     "Und wenn ich durchfalle?"], textsize=32, figur=LE_A, bis="r1"),
    blase("sprech", 600, 200, "r1", 1440, 180, inhalt=["Im Freischuss zählt ein", "Fehlversuch nicht. Ich habe",
                                                      "auch früh geschrieben."], textsize=32, figur=RA_A, bis="hook"),
])

# ===========================================================================================================================
# A2 Einstieg: früh schreiben – und wenn es schiefgeht?
# ===========================================================================================================================
folie([("hook", "Einstieg · früh schreiben: und wenn es schiefgeht?"), ("hook2", "Einstieg › Freiversuch, genannt Freischuss"),
       ("wie", "Einstieg › Wie? Welche Fristen? Verbesserungsversuch?")], rechts_frei([
    *tafel("hook", "Examen früh: und wenn es schiefgeht?"),
    ticon("tabler", "calendar-event", 200, 330, 120, beim("hook", "früh"), fuell=HELLBLAU),
    z("Du schreibst das Examen früh.", 290, 220, beim("hook", "früh"), "Bold", 36),
    *neinz("Was, wenn es schiefgeht?", 290, beim("hook", "schiefgeht"), "Bold", 36, x=335),
    blk(110, 400, 1040, 100, GELB, beim("hook2", "Freiversuch"), [("Freiversuch, im Studium meist „Freischuss“", "ExtraBold", 38, INK)]),
    z("1. Wie funktioniert er?", 150, 560, beim("wie", "funktioniert"), "Bold", 36),
    z("2. Welche Fristen gelten?", 150, 630, beim("wie", "Fristen"), "Bold", 36),
    z("3. Was bringt der Verbesserungsversuch?", 150, 700, beim("wie", "Verbesserungsversuch"), "Bold", 36),
    *requisit([("hook", ("tabler", "calendar-event", 110, HELLBLAU), "Examen früh", WEISS),
               (beim("hook", "schiefgeht"), ("tabler", "alert-triangle", 100, HROT), "und wenn es schiefgeht?", HROT),
               ("hook2", ("tabler", "lifebuoy", 110, ROT), "Freischuss", GELB),
               ("wie", ("tabler", "list-check", 100, WEISS), "3 Fragen", WEISS)]),
    *stehend("LE", X1, [("hook", "sorge"), ("hook2", "staunt"), ("wie", "ruhig")]),
    *stehend("RA", X2, [("hook", "ruhig"), ("hook2", "froh")]),
]))

# ===========================================================================================================================
# B Sachverhalt (Ausgangslage)
# ===========================================================================================================================
def sachverhalt_273(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 220
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=38, zeilenabstand=1.32)
        els += e; y += 20
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 14, cue, fill=PINK, size=36))
    folie([(cue, "Sachverhalt · Die Ausgangslage von Leonore")], els)


sachverhalt_273("sv", [
    "Leonore studiert Jura in Nordrhein-Westfalen, ohne Unterbrechung. Sie ist im 7. Fachsemester.",
    "1 Semester hat sie an einer Universität im Ausland Recht studiert und dort Leistungsnachweise erworben.",
    "Sie überlegt, sich jetzt zur staatlichen Pflichtfachprüfung zu melden. Ihr Freund Rasmus hat das Examen im "
    "letzten Jahr früh geschrieben und danach seine Note verbessert.",
], "Was gilt, wenn Leonore früh schreibt und durchfällt? Und wenn sie besteht?")

# ===========================================================================================================================
# C Was ist der Freiversuch? Wortlaut § 5d Abs. 5 S. 1–3 DRiG
# ===========================================================================================================================
W5D = ("„Die staatliche Pflichtfachprüfung kann einmal wiederholt werden. Eine erfolglose staatliche "
       "Pflichtfachprüfung gilt als nicht unternommen, wenn der Bewerber sich frühzeitig zu dieser Prüfung gemeldet und "
       "die vorgesehenen Prüfungsleistungen vollständig erbracht hat. Das Nähere, insbesondere den Ablauf der "
       "Meldefrist, … regelt das Landesrecht. …“")
w5d, w5d_y = wortlaut(80, 270, 1100, W5D, "§ 5d Abs. 5 S. 1–3 DRiG", "drig", marken=[
    ("einmal wiederholt", beim("wl1", "einmal")), ("frühzeitig", beim("wl2", "frühzeitig")),
    ("vollständig erbracht", beim("wl3", "vollständig")), ("nicht unternommen", beim("wl4", "nicht")),
    ("Landesrecht", beim("wl5", "Landesrecht"))], size=31)
assert w5d_y <= 760, w5d_y
folie([("was", "Freiversuch · Was ist das?"), ("drig", "Freiversuch › § 5d Abs. 5 DRiG"),
       ("wl2", "Freiversuch › frühzeitig gemeldet, alles vollständig erbracht"),
       ("wl4", "Freiversuch › gilt als nicht unternommen"), ("wl5", "Freiversuch › Meldefrist: Landesrecht")], rechts_frei([
    *tafel("was", "Was ist der Freiversuch?"),
    z("Grundlage: Deutsches Richtergesetz (DRiG)", 110, 190, "drig", "Bold", 34),
    *w5d,
    blk(110, 790, 1040, 80, HGELB, "wl5", [("Was „frühzeitig“ heißt, regelt dein Land.", "ExtraBold", 34, INK)]),
    *requisit([("was", ("tabler", "help", 100, WEISS), "Was ist der Freiversuch?", WEISS),
               ("drig", ("tabler", "book", 100, WEISS), "DRiG", WEISS),
               ("wl4", ("tabler", "lifebuoy", 110, ROT), "zählt nicht", HELLGRUEN),
               ("wl5", ("tabler", "map-pin", 100, GELB), "Landesrecht", GELB)]),
    *allein("LE", [("was", "ruhig"), ("wl2", "denkt"), ("wl4", "staunt"), ("wl5", "ruhig")]),
]))

# ===========================================================================================================================
# D Was heißt das für Leonore? Versuchsleiste
# ===========================================================================================================================
VX, VY, VW, VH, VG = 110, 300, 320, 150, 40


def versuch(c, i, kopf, fill, unter=None):
    x = VX + i * (VW + VG)
    els = [kasten(x, VY, VW, VH, fill, c, name=f"versuch:{kopf}"),
           z(kopf, x + 24, VY + 30, c, "ExtraBold", 34, rechts=x + VW - 10)]
    if unter:
        els.append(z(unter, x + 24, VY + 84, c, "Bold", 28, rechts=x + VW - 10))
    return els


FA_X = beim("fa", "durch")
folie([("folge", "Freiversuch › Was heißt das für Leonore?"), ("fa", "Freiversuch › durchgefallen: zählt nicht"),
       ("fb", "Freiversuch › danach: regulärer Versuch und Wiederholung"),
       ("nur1", "Freiversuch › nur im 1. Examen")], rechts_frei([
    *tafel("folge", "Was heißt das für Leonore?"),
    z("Leonore fällt im Freiversuch durch:", 110, 200, beim("fa", "Fällt"), "Bold", 34),
    *versuch(beim("fa", "Freiversuch"), 0, "Freiversuch", GELB),
    bis_(nein(VX + VW - 60, VY + 40, FA_X, gr=30), None),
    pl("zählt nicht", VX + 24, VY + 90, FA_X, fill=HROT, size=30),
    *versuch(beim("fa", "reguläre"), 1, "regulärer", HELLBLAU, "Versuch"),
    *versuch(beim("fb", "Wiederholung"), 2, "Wiederholung", HELLGRUEN, "1-mal"),
    linienzug([(VX + VW + 4, VY + VH / 2), (VX + VW + VG - 4, VY + VH / 2)], beim("fa", "reguläre"), breite=6, farbe=INK),
    linienzug([(VX + 2 * VW + VG + 4, VY + VH / 2), (VX + 2 * VW + 2 * VG - 4, VY + VH / 2)], beim("fb", "Wiederholung"),
              breite=6, farbe=INK),
    blk(110, 540, 1040, 90, LILA, beim("nur1", "Pflichtfachprüfung"), [("nur für die Pflichtfachprüfung: 1. Examen", "ExtraBold", 36, INK)]),
    zit("§ 5d Abs. 5 S. 2 DRiG", 110, 645, beim("nur1", "Pflichtfachprüfung")),
    *requisit([("folge", ("tabler", "user-question", 100, WEISS), "Leonore", BLAU),
               ("fa", ("tabler", "circle-x", 100, HROT), "durchgefallen", HROT),
               ("fb", ("tabler", "refresh", 100, HELLGRUEN), "noch 2 Versuche", HELLGRUEN),
               ("nur1", ("tabler", "school", 110, LILA), "1. Examen", WEISS)]),
    *stehend("LE", X1, [("folge", "ruhig"), ("fa", "sorge"), ("fb", "froh"), ("nur1", "ruhig")]),
    *stehend("RA", X2, [("folge", "ruhig"), ("fb", "froh")]),
]))

# ===========================================================================================================================
# E Voraussetzungen: Meldefrist in 3 Ländern (§ 25 Abs. 1 JAG NRW, § 18 Abs. 1 NJAG, § 29 Abs. 1 SächsJAPO)
# ===========================================================================================================================
LX0, LW, RW = 110, 300, 740                  # Land-Spalte, Regel-Spalte
LH = 140


def landzeile(c, y, land, fill, zeilen, quelle, c_q=None):
    els = [kasten(LX0, y, LW, LH, fill, c, name=f"land:{land}"),
           z(land, LX0 + 20, y + 20, c, "ExtraBold", 34 if len(land) < 13 else 30, rechts=LX0 + LW - 10),
           kasten(LX0 + LW, y, RW, LH, WEISS, c, name=f"regel:{land}")]
    for i, (t, cz) in enumerate(zeilen):
        els.append(z(t, LX0 + LW + 22, y + 16 + i * 44, cz or c, "Bold", 32, rechts=LX0 + LW + RW - 10))
    els.append(zit(quelle, LX0 + 20, y + LH - 44, c_q or c, size=26, rechts=LX0 + LW - 6))
    return els


folie([("vor", "Voraussetzungen · Was gilt in deinem Land?"), ("nrw", "Voraussetzungen › NRW: bis Ende 8. Fachsemester"),
       ("nds", "Voraussetzungen › Niedersachsen: Durchgang nach dem 8. Fachsemester"),
       ("sn", "Voraussetzungen › Sachsen: Termin nach dem 9. Semester"),
       ("unun", "Voraussetzungen › ununterbrochen studiert")], rechts_frei([
    *tafel("vor", "Voraussetzungen: 3 Beispiele"),
    pl("dein Land regelt das", 110, 170, "land", fill=GELB, size=32),
    *landzeile("nrw", 240, "NRW", HELLBLAU, [("Meldung spätestens bis Ende", None), ("des 8. Fachsemesters", None)],
               "§ 25 I JAG NRW"),
    *landzeile("nds", 390, "Niedersachsen", HELLGRUEN, [("Zulassung zum Prüfungsdurchgang", None),
                                                        ("nach dem 8. Fachsemester", None)], "§ 18 I NJAG"),
    *landzeile("sn", 540, "Sachsen", HGELB, [("Prüfung spätestens im Termin", None),
                                            ("nach dem 9. Semester", None),
                                            ], "§ 29 I SächsJAPO"),
    zit("Sachsen: bei Studienbeginn ab 1.10.2020", LX0 + LW + 22, 540 + 104, beim("sn", "Oktober"), size=26, rechts=1150),
    *okz("in allen 3 Ländern: Studium ununterbrochen", 715, beim("unun", "ununterbrochen"), "Bold", 34, x=170),
    *requisit([("vor", ("tabler", "list-check", 100, WEISS), "Voraussetzungen", WEISS),
               ("land", ("tabler", "map-pin", 100, GELB), "3 Länder", WEISS),
               ("nrw", ("tabler", "calendar", 100, HELLBLAU), "8. Fachsemester", WEISS),
               ("sn", ("tabler", "calendar", 100, HGELB), "9. Semester", WEISS),
               ("unun", ("tabler", "circle-check", 100, HELLGRUEN), "ununterbrochen", HELLGRUEN)]),
    *allein("LE", [("vor", "ruhig"), ("nrw", "denkt"), ("unun", "ruhig")]),
]))

# ===========================================================================================================================
# F Semester, die nicht mitzählen (§ 25 Abs. 2, 3, 5 JAG NRW; § 17 NJAVO; § 29 Abs. 1 S. 4 SächsJAPO)
# ===========================================================================================================================
SPW = 340


def spalte(c, i, land, wert, fill):
    x = 110 + i * (SPW + 10)
    return [kasten(x, 330, SPW, 130, fill, c, name=f"ausland:{land}"),
            z(land, x + 20, 344, c, "ExtraBold", 30, rechts=x + SPW - 10),
            z(wert, x + 20, 398, c, "Bold", 34, rechts=x + SPW - 10)]


folie([("frei", "Semester › Was zählt nicht mit?"), ("aus", "Semester › Ausland: bis 3 bzw. 2 Semester"),
       ("deckel", "Semester › NRW: höchstens 4 insgesamt"), ("krank", "Semester › Krankheit: amtsärztliches Zeugnis")],
      rechts_frei([
    *tafel("frei", "Semester, die nicht mitzählen"),
    z("z. B. schwere Krankheit", 110, 185, beim("frei", "Krankheit"), "Bold", 34),
    z("oder Studium im Ausland", 560, 185, beim("frei", "Ausland"), "Bold", 34),
    z("Ausland, jeweils mit Nachweisen:", 110, 270, "aus", "Bold", 32),
    *spalte(beim("aus", "Nordrhein"), 0, "NRW", "bis zu 3", HELLBLAU),
    *spalte(beim("aus", "Niedersachsen"), 1, "Niedersachsen", "bis zu 3", HELLGRUEN),
    *spalte(beim("aus", "Sachsen"), 2, "Sachsen", "bis zu 2", HGELB),
    zit("§ 25 II 2 Nr. 3 JAG NRW · § 17 Nr. 2 NJAVO · § 29 I 4 Nr. 3 SächsJAPO", 110, 475, beim("aus", "Nachweisen")),
    blk(110, 545, 1040, 80, HELLBLAU, "deckel", [("NRW: insgesamt höchstens 4 Semester", "ExtraBold", 34, INK)]),
    zit("§ 25 V JAG NRW", 110, 633, "deckel"),
    blk(110, 690, 1040, 80, HROT, "krank", [("Krankheit: amtsärztliches Zeugnis (NRW, Niedersachsen)", "ExtraBold", 32, INK)]),
    zit("§ 25 III JAG NRW · § 17 Nr. 1 NJAVO", 110, 778, "krank"),
    *requisit([("frei", ("tabler", "calendar-x", 100, WEISS), "zählt nicht mit", WEISS),
               ("aus", ("tabler", "plane", 110, HELLBLAU), "Ausland", WEISS),
               ("deckel", ("tabler", "calendar", 100, HELLBLAU), "höchstens 4", WEISS),
               ("krank", ("tabler", "stethoscope", 100, HROT), "Amtsarzt", WEISS)]),
    *allein("LE", [("frei", "denkt"), ("aus", "staunt"), ("krank", "ruhig")]),
]))

# ===========================================================================================================================
# G Leonore konkret: 7 Fachsemester, 1 davon im Ausland
# ===========================================================================================================================
SEM_X, SEM_Y, SEM_W, SEM_G = 110, 260, 136, 11
AUS_I = 4                                    # 5. Semester im Ausland (Fallannahme, nur Bild)
LE_G = ("LE_redetfroh", X1, FB, FR)


def semester(c, i, fill, text):
    x = SEM_X + i * (SEM_W + SEM_G)
    return [kasten(x, SEM_Y, SEM_W, 120, fill, (c[0], c[1] + 0.06 * i) if isinstance(c, tuple) else (c, 0.06 * i),
                   name=f"semester:{i + 1}:{text}"),
            z(text, x + 22 if len(text) < 3 else x + 8, SEM_Y + 36, (c[0], c[1] + 0.06 * i) if isinstance(c, tuple)
              else (c, 0.06 * i), "ExtraBold", 40 if len(text) < 3 else 28, rechts=x + SEM_W - 6)]


els_g = [*tafel("leo2", "Leonore: 7 Fachsemester")]
for i in range(7):
    el_ = semester("leo2", i, HELLBLAU, f"{i + 1}.")
    if i == AUS_I:                           # 5. Semester wird beim Wort „Ausland“ zum Auslandssemester
        el_ = [bis_(e, beim("leo2", "Ausland")) for e in el_]
    els_g += el_
els_g += semester(beim("leo2", "Ausland"), AUS_I, LILA, "Ausland")
els_g += [
    z("Ein Semester: Recht im Ausland studiert", 110, 400, beim("leo2", "Ausland"), "Bold", 32),
    pl("zählt nicht mit", SEM_X + AUS_I * (SEM_W + SEM_G) - 40, SEM_Y - 60, beim("leo3", "Erfüllt"), fill=HROT, size=28),
    z("Voraussetzungen in NRW erfüllt:", 110, 480, beim("leo3", "Erfüllt"), "Bold", 32),
    blk(110, 540, 1040, 90, HELLGRUEN, beim("leo3", "sechs"), [("dann zählen erst 6 Semester", "ExtraBold", 38, INK)]),
    blk(110, 680, 1040, 90, HGELB, "leo4", [("Ob das bei dir so ist: frag dein Prüfungsamt.", "ExtraBold", 34, INK)]),
    ticon("tabler", "building-bank", 1090, 770, 80, "leo4", fuell=WEISS),
    *requisit([("leo2", ("tabler", "plane", 110, LILA), "1 Semester Ausland", WEISS),
               ("leo3", ("tabler", "calendar-check", 100, HELLGRUEN), "6 Semester", HELLGRUEN),
               ("leo4", ("tabler", "building-bank", 110, HGELB), "Prüfungsamt", WEISS),
               ("l2", None, None, None)]),
    *fig("LE", X1, FB, FR, [("leo2", "ruhig"), ("leo3", "staunt")], bis="l2"),
    *redet("LE_redetfroh", X1, FB, FR, "l2", "verb"),
    ns(NAME["LE"], X1, FB, "leo2", NFARBE["LE"], d=0.1),
    *stehend("RA", X2, [("leo2", "ruhig"), ("leo4", "froh")]),
    blase("sprech", 560, 170, "l2", 1560, 250, inhalt=["Dann hätte ich sogar noch", "ein Semester mehr Zeit."], textsize=32,
          figur=LE_G, bis="verb"),
]
folie([("leo2", "Fall Leonore › 1 Semester im Ausland"), ("leo3", "Fall Leonore › dann zählen erst 6 Semester"),
       ("leo4", "Fall Leonore › Prüfungsamt fragen"), ("l2", "Fall Leonore › 1 Semester mehr Zeit")], rechts_frei(els_g))

# ===========================================================================================================================
# H Verbesserungsversuch (§ 5d Abs. 5 S. 4 DRiG; § 26, § 65 II Nr. 1 JAG NRW; § 19 NJAG, Anl. 2 NJG Nr. 7.3; § 31 SächsJAPO)
# ===========================================================================================================================
HX = [110, 380, 800]                         # Spalten: Land, Antrag/Termin, Gebühr
HW = [270, 420, 350]
HY0, HHH, HZ = 300, 60, 150


def kopfzeile(c):
    els = []
    for x, w, t in zip(HX, HW, ["Land", "Antrag / Termin", "Gebühr"]):
        els += [kasten(x, HY0 - HHH, w, HHH, GELB, c, rund=8, name=f"kopf:{t}"),
                z(t, x + 16, HY0 - HHH + 10, c, "ExtraBold", 30, rechts=x + w - 8)]
    return els


def vzeile(r, land, fill, quelle, c_land, frist, gebuehr):
    """frist/gebuehr = [(text, cue)] zeilenweise in Sprechreihenfolge."""
    y = HY0 + r * HZ
    els = [kasten(HX[0], y, HW[0], HZ, fill, c_land, rund=8, name=f"vland:{land}"),
           z(land, HX[0] + 16, y + 16, c_land, "ExtraBold", 30, rechts=HX[0] + HW[0] - 8),
           zit(quelle, HX[0] + 16, y + HZ - 46, c_land, size=26, rechts=HX[0] + HW[0] - 6),
           kasten(HX[1], y, HW[1], HZ, WEISS, c_land, rund=8, name=f"vfrist:{land}"),
           kasten(HX[2], y, HW[2], HZ, WEISS, c_land, rund=8, name=f"vgeb:{land}")]
    for i, (t, c) in enumerate(frist):
        els.append(z(t, HX[1] + 16, y + 14 + i * 42, c, "Bold", 29, rechts=HX[1] + HW[1] - 8))
    for i, (t, c) in enumerate(gebuehr):
        els.append(z(t, HX[2] + 16, y + 14 + i * 42, c, "Bold", 29, rechts=HX[2] + HW[2] - 8))
    return els


folie([("verb", "Verbesserungsversuch · bestanden, aber die Note reicht nicht?"),
       ("vb3", "Verbesserungsversuch › § 5d Abs. 5 S. 4 DRiG: Landesrecht"),
       ("vnrw", "Verbesserungsversuch › NRW: nach Freiversuch 1-mal"),
       ("vnds", "Verbesserungsversuch › Niedersachsen: Antrag binnen 1 Jahr"),
       ("vsn", "Verbesserungsversuch › Sachsen: nächster oder übernächster Termin")], rechts_frei([
    *tafel("verb", "Verbesserungsversuch", h=850),
    z("Das Richtergesetz überlässt ihn dem Landesrecht.", 110, 170, "vb3", "Bold", 32),
    *kopfzeile("vnrw"),
    *vzeile(0, "NRW", HELLBLAU, "§§ 26, 65 JAG NRW", "vnrw",
            [("nach Freiversuch: 1-mal", "vnrw"), ("Antrag binnen 1 Jahr", "vnrw2")],
            [("nur nach regulärem", "vnrw3"), ("Versuch", "vnrw3")]),
    *vzeile(1, "Niedersachsen", HELLGRUEN, "§ 19 NJAG", "vnds",
            [("Antrag binnen 1 Jahr", "vnds")],
            [("160 €, entfällt", beim("vnds2", "hundertsechzig")), ("nach Freiversuch", beim("vnds2", "Freiversuch"))]),
    *vzeile(2, "Sachsen", HGELB, "§ 31 SächsJAPO", "vsn",
            [("nächster oder übernächster", "vsn"), ("Termin, vor dem", beim("vsn", "bevor")), ("Referendariat", beim("vsn", "bevor"))],
            [("500 €, entfällt", beim("vsn2", "fünfhundert")), ("nach Freiversuch", beim("vsn2", "Freiversuch"))]),
    *requisit([("verb", ("tabler", "trending-up", 110, WEISS), "Note reicht nicht?", WEISS),
               ("vb2", ("tabler", "repeat", 100, HELLGRUEN), "Verbesserungsversuch", HELLGRUEN),
               ("vnrw", ("tabler", "clock", 100, HELLBLAU), "Frist", WEISS),
               (beim("vnrw3", "Gebühr"), ("tabler", "coin-euro", 100, GELB), "Gebühr?", WEISS),
               ("vsn", ("tabler", "briefcase", 100, HGELB), "vor dem Referendariat", WEISS),
               ("vsn2", ("tabler", "coin-euro", 100, GELB), "nach Freiversuch: 0 €", HELLGRUEN)]),
    *allein("LE", [("verb", "denkt"), ("vb2", "ruhig"), ("vnds2", "froh")]),
]))

# ===========================================================================================================================
# I Was zählt am Ende? Bessere Note; zweites Examen; Rasmus 7 → 9 Punkte
# ===========================================================================================================================
RA_I = ("RA_redetfroh", X2, FB, FR)
PKT_X0, PKT_W = 470, 40                      # 1 Punkt = 40 px


def punktebalken(c, y, text, p, fill):
    w = p * PKT_W
    def zz(dr, s):
        dr.rectangle((2 * s, 2 * s, (w - 2) * s, 68 * s), fill=fill, outline=INK, width=4 * s)
        dr.text(((w - 18) * s, 35 * s), f"{p} Punkte" if p else "", font=F("ExtraBold", 30 * s), fill=INK, anchor="rm")
    assert F("ExtraBold", 30).getlength(f"{p} Punkte") <= w - 30
    return [z(text, 110, y + 16, c, "Bold", 30, rechts=PKT_X0 - 10),
            El(_flaeche(w, 70, zz), PKT_X0, y, c, "pop", 0.0, None, name=f"punkte:{text}:{p}")]


folie([("besser", "Am Ende · die bessere Note bleibt"), ("zwei", "Am Ende › auch nach dem 2. Examen"),
       ("r2", "Am Ende › Rasmus: 7, dann 9 Punkte")], rechts_frei([
    *tafel("besser", "Was zählt am Ende?"),
    *okz("Eine schlechtere Note verdrängt die alte nicht.", 190, beim("besser", "schlechtere"), "Bold", 34, x=170),
    zit("§ 26 II JAG NRW · § 19 II NJAG · § 31 V SächsJAPO", 170, 245, beim("besser", "schlechtere")),
    blk(110, 320, 1040, 80, HELLBLAU, beim("zwei", "zweiten"), [("auch nach dem 2. Examen: Notenverbesserung", "ExtraBold", 34, INK)]),
    zit("§ 56a JAG NRW · § 19 NJAG · § 56 SächsJAPO", 110, 410, beim("zwei", "zweiten")),
    z("Rasmus:", 110, 500, "r2", "ExtraBold", 34),
    *punktebalken(beim("r2", "Freischuss"), 570, "Freischuss", 7, GELB),
    *punktebalken(beim("r2", "Verbesserungsversuch"), 670, "Verbesserungsversuch", 9, GRUEN),
    *requisit([("besser", ("tabler", "shield-check", 100, HELLGRUEN), "bessere Note bleibt", HELLGRUEN),
               ("zwei", ("tabler", "briefcase", 100, HELLBLAU), "2. Examen", WEISS),
               ("r2", None, None, None)]),
    *stehend("LE", X1, [("besser", "ruhig"), ("r2", "staunt")]),
    *fig("RA", X2, FB, FR, [("besser", "ruhig"), ("zwei", "denkt")], bis="r2"),
    *redet("RA_redetfroh", X2, FB, FR, "r2", "strat"),
    ns(NAME["RA"], X2, FB, "besser", NFARBE["RA"], d=0.1),
    blase("sprech", 600, 170, "r2", 1560, 250, inhalt=["Mein Freischuss brachte 7 Punkte,", "der Verbesserungsversuch 9."],
          textsize=30, figur=RA_I, bis="strat"),
]))

# ===========================================================================================================================
# J Strategie: Lohnt sich der Freischuss?
# ===========================================================================================================================
folie([("strat", "Strategie · Lohnt sich der Freischuss?"), ("ch1", "Strategie › Chance: zusätzlicher Versuch"),
       ("ch2", "Strategie › Chance: Verbesserung ohne Gebühr"), ("ri1", "Strategie › Risiko: weniger Lernzeit"),
       ("ri2", "Strategie › Risiko: Fehlversuch kostet Zeit und Kraft"), ("stand", "Strategie › entscheidend: dein Stand")],
      rechts_frei([
    *tafel("strat", "Lohnt sich der Freischuss?"),
    z("Chance", 110, 180, "ch1", "ExtraBold", 36, farbe=DGRUEN),
    *pm("zusätzlicher Versuch, kein regulärer verbraucht", 110, 235, beim("ch1", "zusätzlichen"), True, size=31),
    *pm("bestanden: Note ohne Gebühr verbessern", 110, 290, beim("ch2", "Gebühr"), True, size=31),
    z("Risiko", 110, 370, "ri1", "ExtraBold", 36, farbe=DROT),
    *pm("weniger Zeit zum Lernen", 110, 425, beim("ri1", "weniger"), False, size=31),
    *pm("Fehlversuch kostet einen Durchgang und Kraft", 110, 480, beim("ri2", "Fehlversuch"), False, size=31),
    *pm("Verbesserungsversuch kostet Monate", 110, 535, beim("ri3", "Verbesserungsversuch"), False, size=31),
    blk(110, 625, 1040, 80, GELB, "stand", [("entscheidend: nicht das Semester, sondern dein Stand", "ExtraBold", 33, INK)]),
    z("Probeklausuren schon unter Examensbedingungen?", 110, 735, beim("stand", "Probeklausuren"), "Bold", 34),
    *requisit([("strat", ("tabler", "scale", 110, WEISS), "Chance oder Risiko?", WEISS),
               ("ch1", ("tabler", "lifebuoy", 100, ROT), "zusätzlicher Versuch", HELLGRUEN),
               ("ri1", ("tabler", "hourglass", 100, HROT), "weniger Zeit", HROT),
               ("stand", ("tabler", "writing", 100, GELB), "dein Stand", WEISS)]),
    *stehend("LE", X1, [("strat", "denkt"), ("ch1", "froh"), ("ri1", "sorge"), ("stand", "entschlossen")]),
    *stehend("RA", X2, [("strat", "ruhig"), ("ri1", "ernst"), ("stand", "ruhig")]),
]))

# ===========================================================================================================================
# K Ergebnis: Flur – Leonore nimmt das Formular vom Aushang
# ===========================================================================================================================
LE_K = ("LE_redet2_r", LEX, BODEN_Y, FHA)
RA_K = ("RA_redetfroh", RAX, BODEN_Y, FHA)
NIMMT = beim("erg", "Formular")
GENOMMEN = (NIMMT[0], round(NIMMT[1] + 0.45, 3))
form_el = El(formular_bild(), FORM[0], FORM[1], "erg", "cut", 0.0, None, name="formular")
form_el.bis = NIMMT
HANDX, HANDY = LEX + 40, 560                 # Formular vor Leonore (nach dem Abnehmen)
folie([("erg", "Ergebnis · Leonore nimmt das Formular"), ("l3", "Ergebnis › erst Prüfungsamt fragen, dann melden"),
       ("r3", "Ergebnis › bis dahin jede Woche 1 Probeklausur")], [
    *flur("erg", mit_formular=False),
    bis_(hart(pl("Flur der juristischen Fakultät", 70, 30, "erg", fill=GELB, size=38)), "l3"),
    hart(form_el),
    pl("Prüfungsamt fragen", 1250, 300, beim("l3", "Prüfungsamt"), fill=HGELB, size=30, anker="m", bis="r3"),
    pl("jede Woche 1 Probeklausur", 900, 280, beim("r3", "Woche"), fill=HELLGRUEN, size=30, anker="m"),
    *fig("LE", LEX, BODEN_Y, FHA, [("erg", "entschlossen_r")], erst="cut", bis="l3"),
    *redet("LE_redet2_r", LEX, BODEN_Y, FHA, "l3", "r3"),
    *fig("LE", LEX, BODEN_Y, FHA, [("r3", "froh_r")], erst="cut", bis="tipp"),
    hart(ns(NAME["LE"], LEX, BODEN_Y, "erg", NFARBE["LE"])),
    *fig("RA", RAX, BODEN_Y, FHA, [("erg", "froh")], erst="cut", bis="r3"),
    *redet("RA_redetfroh", RAX, BODEN_Y, FHA, "r3", "tipp"),
    hart(ns(NAME["RA"], RAX, BODEN_Y, "erg", NFARBE["RA"])),
    # Formular vor den Figuren (Leonore hält es vor sich)
    szene(bewegt(El(formular_bild(), HANDX, HANDY, NIMMT, "cut", 0.0, None, name="formular:genommen"),
                 NIMMT, GENOMMEN, FORM[0] - HANDX, FORM[1] - HANDY), "273formular*", 0.9, versatz=0.0),
    blase("sprech", 660, 200, "l3", 740, 180, inhalt=["Ich frage beim Prüfungsamt, ob mein", "Auslandssemester zählt.",
                                                     "Dann melde ich mich."], textsize=30, figur=LE_K, bis="r3"),
    blase("sprech", 560, 170, "r3", 1400, 180, inhalt=["Und schreib bis dahin jede", "Woche eine Probeklausur."], textsize=32,
          figur=RA_K, bis="tipp"),
])

# ===========================================================================================================================
# L Klausurtipp (Lexi): Freiversuch wie einen echten Versuch behandeln
# ===========================================================================================================================
els_k = [*tafel("tipp", "Klausurtipp: wie ein echter Versuch", fill=HELL), warnung_i(150, 225, "tipp", gr=26),
         z("Behandle den Freiversuch wie einen echten Versuch.", 200, 200, beim("tipp", "Behandle"), "Bold", 32)]
for i in range(6):
    xx = 180 + i * 165
    c_ = beim("tipp2", "Schreib"); c_ = (c_[0], round(c_[1] + 0.1 * i, 3))
    els_k += [ticon("tabler", "file-text", xx, 420, 100, c_, fuell=WEISS), bis_(ok(xx + 20, 330, c_, gr=22), None)]
els_k += [z("Schreib jede Klausur zu Ende,", 130, 450, beim("tipp2", "Schreib"), "Bold", 34),
          pl("auch wenn sie schlecht läuft", 650, 446, beim("tipp2", "schlecht"), fill=HROT, size=30),
          blk(110, 560, 1040, 130, HELLGRUEN, "tipp3", [("Schutz nur, wenn du alle Prüfungsleistungen", "Bold", 32, INK),
                                                        ("vollständig erbringst", "ExtraBold", 34, INK)]),
          zit("§ 5d Abs. 5 S. 2 DRiG", 110, 705, "tipp3"),
          *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
          ns("Lexi", FX, FB, "tipp", GELB, d=0.2)]
folie([("tipp", "Klausurtipp · wie ein echter Versuch"), ("tipp2", "Klausurtipp › jede Klausur zu Ende schreiben"),
       ("tipp3", "Klausurtipp › alle Prüfungsleistungen vollständig")], els_k)

# ===========================================================================================================================
# M Dein Freischuss in 5 Schritten (Schema, Punkt für Punkt)
# ===========================================================================================================================
REIHEN = [("k1", "I.", "Meldefrist deines Landes prüfen", BLAU),
          ("k2", "II.", "Semester klären, die nicht mitzählen", GRUEN),
          ("k3", "III.", "alle Prüfungsleistungen vollständig erbringen", HELLBLAU),
          ("k4", "IV.", "durchgefallen: gilt als nicht unternommen", HROT),
          ("k5", "V.", "bestanden: Frist und Gebühr für den Verbesserungsversuch", GELB)]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Dein Freischuss in 5 Schritten"), 110, 90, "sch", 50)]
y = 230
for c, nr, text, f in REIHEN:
    els_sch.append(pl(nr, 130, y - 6, c, fill=f, size=36))
    els_sch.append(z(text, 300, y, c, "ExtraBold", 40, rechts=1820))
    y += 135
assert y <= 960, y
folie([("sch", "Freischuss · 5 Schritte"), ("k1", "Freischuss › I. Meldefrist prüfen"),
       ("k2", "Freischuss › II. Semester klären"), ("k3", "Freischuss › III. alles vollständig erbringen"),
       ("k4", "Freischuss › IV. durchgefallen: nicht unternommen"), ("k5", "Freischuss › V. bestanden: Verbesserungsversuch")],
      els_sch)

# ===========================================================================================================================
# N Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Im Freiversuch zählt ein", 0)], [("Fehlversuch ", 0), ("nicht", "a"), (",", 0)]],
                750, 300, 44, "merke", {"a": beim("merke", "nicht")}),
    *markertext([[("wenn du dich ", 0), ("rechtzeitig", "b"), (" meldest und alle", 0)],
                 [("Leistungen ", 0), ("vollständig", "c"), (" erbringst.", 0)]],
                750, 480, 42, "m2", {"b": beim("m2", "rechtzeitig"), "c": beim("m2", "vollständig")}),
    *markertext([[("Fristen, Semester und Verbesserung regelt", 0)], [("dein Land, also frag dein ", 0), ("Prüfungsamt", "d"), (".", 0)]],
                750, 660, 40, "m3", {"d": beim("m3", "Prüfungsamt")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
