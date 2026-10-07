"""Folge 237 · Probeklausuren Examen: Wie viele schreiben und wie auswerten? – Serienstandard Open Peeps (Katzenkönig).
Rahmen: Friedrich (Jurastudent in Nordrhein-Westfalen) legt seinem Mentor Herrn Seebach in der Sprechstunde einen Stapel von
zwölf korrigierten Probeklausuren auf den Tisch – fast immer sechs Punkte, ausgewertet hat er keine. Szenen laut
../SZENENPLAN.md: A1 Sprechstunde (Büro mit Regal, Fenster, Schreibtisch), A2 Einstieg (Notenkurve), B Sachverhalt,
C Problem (schreiben ohne auswerten), D Wie viele (Faustregel), E Verteilung wie im Examen (§ 10 Abs. 2 JAG NRW),
F Examensbedingungen (§ 13 Abs. 1, 3, § 10 Abs. 1 JAG NRW; Referendariat, § 5d Abs. 6 S. 1 DRiG), G–J Auswertung in vier
Schritten (Korrektur, Musterlösung gegen Gliederung, Fehlerprotokoll, Wiederholungskarten) mit durchgehender Schrittleiste,
K Wochenrhythmus, L Ergebnis (Büro, drei Wochen später), M Klausurtipp (Lexi), N Klausurtraining I.–V., O Merksatz (Lexi).
Handlungsgeräusch: Stapel landet auf dem Schreibtisch (A1); ../geraeusche_herkunft.json.
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/redet/fig/ns/okz/neinz/requisit
als eigene Kopie aus Folge 201 (gemeinsame Dateien unverändert); neu: regal(), stapel_bild(), blatt_bild(), notenkurve(),
balken(), schrittleiste(), gliederung(), zaehler(), karteikarte(), wzelle().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Normangaben nach gesetze-im-internet.de und recht.nrw.de, Abruf 07.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_237/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_237/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 168/180/201) ---------------------------------
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
NAME = {"FR": "Friedrich", "SB": "Herr Seebach"}
NFARBE = {"FR": GRUEN, "SB": ORANGE}


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


# --- Büro des Mentors: Regal, Fenster, Schreibtisch, Stapel -------------------------------------------------------------
BODEN_Y = 905
FHA = 480
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
FRX, SBX = 590, 1560                         # Friedrich (blickt nach rechts), Herr Seebach (blickt nach links)
TISCH = (800, 1330)
TISCH_H = 170
TOP = BODEN_Y - TISCH_H                      # Tischplatte


def boden(c):
    return hart(linienzug([(60, BODEN_Y), (1860, BODEN_Y)], c, breite=7, farbe=INK))


def schreibtisch(c, x0, x1, h=TISCH_H):
    w = x1 - x0
    def zz(dr, s):
        dr.rounded_rectangle((3 * s, 0, (w - 3) * s, 28 * s), 6 * s, fill=HOLZ, outline=INK, width=5 * s)
        dr.rectangle(((w - 190) * s, 28 * s, (w - 40) * s, (h - 3) * s), fill=HOLZ, outline=INK, width=4 * s)
        for yy in (70, 120):                   # Schubladen
            dr.line(((w - 190) * s, yy * s, (w - 40) * s, yy * s), fill=INK, width=4 * s)
            dr.rounded_rectangle(((w - 130) * s, (yy - 24) * s, (w - 100) * s, (yy - 16) * s), 3 * s, fill=INK)
        dr.rectangle((40 * s, 28 * s, 66 * s, (h - 3) * s), fill=HOLZ, outline=INK, width=4 * s)
    return hart(El(_flaeche(w, h, zz), x0, BODEN_Y - h, c, "cut", 0.0, None, name="schreibtisch"))


def regal(c, x0=90, y0=470, w=300):
    """Niedriges Bücherregal links (programmatisch): drei Böden mit Buchrücken in Palettenfarben."""
    h = BODEN_Y - y0
    farben = [BLAU, ROT, GELB, GRUEN, LILA, PINK, ORANGE, TUERKIS]
    def zz(dr, s):
        dr.rectangle((3 * s, 3 * s, (w - 3) * s, (h - 3) * s), fill=HOLZ2, outline=INK, width=5 * s)
        fh = (h - 20) / 3
        for i in range(3):
            y1 = 10 + (i + 1) * fh
            dr.line((3 * s, y1 * s, (w - 3) * s, y1 * s), fill=INK, width=5 * s)
            x = 18; j = i * 3
            while x < w - 50:
                bw = 22 + (j * 7) % 14; bh = fh - 22 - (j * 11) % 26
                dr.rectangle((x * s, (y1 - bh) * s, (x + bw) * s, (y1 - 3) * s), fill=farben[j % len(farben)], outline=INK, width=3 * s)
                x += bw + 5; j += 1
    return hart(El(_flaeche(w, h, zz), x0, y0, c, "cut", 0.0, None, name="regal"))


def fenster(c, x0=880, y0=180, w=260, h=230):
    def zz(dr, s):
        dr.rounded_rectangle((3 * s, 3 * s, (w - 3) * s, (h - 3) * s), 10 * s, fill=(214, 232, 250, 255), outline=INK, width=5 * s)
        dr.line((w // 2 * s, 3 * s, w // 2 * s, (h - 3) * s), fill=INK, width=4 * s)
        dr.line((3 * s, h // 2 * s, (w - 3) * s, h // 2 * s), fill=INK, width=4 * s)
    return hart(El(_flaeche(w, h, zz), x0, y0, c, "cut", 0.0, None, name="fenster"))


def stapel_bild(n=8, w=240):
    """Stapel korrigierter Klausuren (programmatisch): versetzte Blätter, oben ein Blatt mit Schreibzeilen."""
    h = 26 + n * 7
    def zz(dr, s):
        for i in range(n):
            dx = (i * 5) % 11 - 5
            y = h - 30 - i * 7
            dr.rectangle(((12 + dx) * s, y * s, (w - 12 + dx) * s, (y + 26) * s), fill=WEISS, outline=INK, width=3 * s)
        for k in range(3):
            dr.line((40 * s, (h - 26 - (n - 1) * 7 + 7 + k * 6) * s, ((w - 60) - k * 30) * s, (h - 26 - (n - 1) * 7 + 7 + k * 6) * s),
                    fill=GRAU, width=2 * s)
    return _flaeche(w, h, zz)


def blatt_bild(w=200, h=60):
    """Ein einzelnes korrigiertes Blatt flach auf dem Tisch."""
    def zz(dr, s):
        dr.rectangle((4 * s, 8 * s, (w - 4) * s, (h - 4) * s), fill=WEISS, outline=INK, width=3 * s)
        for k in range(3):
            dr.line((24 * s, (20 + k * 10) * s, (w - 50 - k * 20) * s, (20 + k * 10) * s), fill=GRAU, width=3 * s)
        dr.line(((w - 34) * s, 14 * s, (w - 34) * s, (h - 10) * s), fill=ROT, width=3 * s)
    return _flaeche(w, h, zz)


STAPEL_X = 880


def buero(c, mit_stapel=False):
    els = [boden(c), regal(c), fenster(c), schreibtisch(c, *TISCH),
           hart(ficon("tabler", "lamp", TISCH[1] - 70, TOP + 2, 110, c, fuell=GELB, anim="cut"))]
    if mit_stapel:
        st = stapel_bild()
        els.append(hart(El(st, STAPEL_X, TOP - st.height + 6, c, "cut", 0.0, None, name="stapel")))
    return els


# ===========================================================================================================================
# A1 Fall: Sprechstunde – der Stapel Klausuren
# ===========================================================================================================================
FR_A = ("FR_redet_r", FRX, BODEN_Y, FHA)
SB_A = ("SB_redet", SBX, BODEN_Y, FHA)
_st = stapel_bild()
LEGT = beim("stapel", "Stapel")
LANDET = (LEGT[0], round(LEGT[1] + 0.35, 3))
stapel_el = El(_st, STAPEL_X, TOP - _st.height + 6, LEGT, "cut", 0.0, None, name="stapel")
folie([(NULL, "Fall · Sprechstunde an der Uni"), ("f1", "Fall · 12 Klausuren, fast immer 6 Punkte"),
       ("f2", "Fall · nur die Note angeschaut")], [
    *buero(NULL),
    hart(pl("Sprechstunde an der Uni", 70, 30, NULL, fill=GELB, size=38)),
    szene(bewegt(stapel_el, LEGT, LANDET, 0, -90), "237stapel*", 0.9, versatz=0.35 - 0.18),
    pl("6 Punkte", STAPEL_X + 120, TOP - 120, beim("f1", "sechs"), fill=ROT, size=30, anker="m"),
    pl("nur die Note", STAPEL_X + 120, TOP - 190, beim("f2", "Note"), fill=HROT, size=30, anker="m"),
    # Friedrich (links, blickt nach rechts zu Herrn Seebach)
    *fig("FR", FRX, BODEN_Y, FHA, [(NULL, "muede_r")], erst="cut", bis="f1"),
    *redet("FR_redet_r", FRX, BODEN_Y, FHA, "f1", "s1"),
    *fig("FR", FRX, BODEN_Y, FHA, [("s1", "ratlos_r")], erst="cut", bis="f2"),
    *redet("FR_redet_r", FRX, BODEN_Y, FHA, "f2", "hook"),
    hart(ns(NAME["FR"], FRX, BODEN_Y, NULL, NFARBE["FR"])),
    # Herr Seebach (rechts, blickt nach links)
    *fig("SB", SBX, BODEN_Y, FHA, [(beim("seebach", "Seebach"), "ruhig"), (beim("f1", "sechs"), "denkt")], erst="pop", bis="s1"),
    ns(NAME["SB"], SBX, BODEN_Y, beim("seebach", "Seebach"), NFARBE["SB"], d=0.1),
    *redet("SB_redet", SBX, BODEN_Y, FHA, "s1", "f2"),
    *fig("SB", SBX, BODEN_Y, FHA, [("f2", "ernst")], erst="cut", bis="hook"),
    blase("sprech", 560, 220, "f1", 560, 230, inhalt=["12 Klausuren in 12 Wochen.", "Und fast immer 6 Punkte."], textsize=34,
          figur=FR_A, bis="s1"),
    blase("sprech", 560, 190, "s1", 1420, 250, inhalt=["Und was machst du", "mit den Korrekturen?"], textsize=34,
          figur=SB_A, bis="f2"),
    blase("sprech", 680, 220, "f2", 580, 230, inhalt=["Ich schaue auf die Note.", "Und dann schreibe ich die nächste."],
          textsize=32, figur=FR_A, bis="hook"),
])

# ===========================================================================================================================
# A2 Einstieg: Noten bleiben gleich? (Notenkurve)
# ===========================================================================================================================
NOTEN = [6, 5, 6, 7, 6, 6, 6, 5, 6, 6, 7, 6]
KX0, KX1, KY0, KY1 = 250, 1130, 200, 440      # Diagrammfläche: x, y (oben = 18 Punkte, unten = 0)


def ky(p):
    return KY1 - (KY1 - KY0) * p / 18


def notenkurve(c, gleich_c):
    """Notenkurve der 12 Probeklausuren: Achsen (0–18 Punkte), Punkte nacheinander, flaches Band um 6 Punkte."""
    w, h = 1080, 330
    ox, oy = 100, 160
    def achsen(dr, s):
        f = F("Bold", 26 * s)
        dr.line(((KX0 - ox) * s, (KY0 - oy - 10) * s, (KX0 - ox) * s, (KY1 - oy) * s), fill=INK, width=4 * s)
        dr.line(((KX0 - ox) * s, (KY1 - oy) * s, (KX1 - ox) * s, (KY1 - oy) * s), fill=INK, width=4 * s)
        for p in (0, 6, 12, 18):
            yy = ky(p) - oy
            dr.text(((KX0 - ox - 16) * s, yy * s), str(p), font=f, fill=TEXT, anchor="rm")
            if p:
                dr.line(((KX0 - ox) * s, yy * s, (KX1 - ox) * s, yy * s), fill=(225, 225, 220, 255), width=2 * s)
        dr.text(((KX0 - ox - 140) * s, (KY0 - oy + 40) * s), "Punkte", font=f, fill=TEXT, anchor="lm")
        dr.text(((KX1 - ox) * s, (KY1 - oy + 32) * s), "Klausur 1 bis 12", font=f, fill=TEXT, anchor="rm")
    els = [El(_flaeche(w, h, achsen), ox, oy, c, "fade", 0.0, None, name="notenkurve:achsen")]
    dx = (KX1 - KX0 - 40) / 11
    for i, p in enumerate(NOTEN):
        def pk(dr, s):
            dr.ellipse((3 * s, 3 * s, 29 * s, 29 * s), fill=BLAU, outline=INK, width=4 * s)
        els.append(El(_flaeche(32, 32, pk), KX0 + 20 + i * dx - 16, ky(p) - 16, (c[0], c[1] + 0.07 * i) if isinstance(c, tuple)
                      else (c, 0.07 * i), "pop", 0.0, None, name=f"notenkurve:{i + 1}"))
    def band(dr, s):
        dr.rounded_rectangle((3 * s, 3 * s, (KX1 - KX0 - 3) * s, (ky(4.5) - ky(7.5) - 3) * s), 16 * s, outline=DROT, width=5 * s)
    els.append(El(_flaeche(KX1 - KX0, int(ky(4.5) - ky(7.5)), band), KX0, ky(7.5), gleich_c, "pop", 0.0, None,
                  name="notenkurve:band"))
    return els


folie([("hook", "Einstieg · Noten bleiben gleich?"), (beim("hook2", "Punkte"), "Einstieg › aus jeder Korrektur lernen"),
       ("wie", "Einstieg › Wie viele? Wie auswerten?")], rechts_frei([
    *tafel("hook", "Jede Woche 1 Klausur und die Note?"),
    *notenkurve(beim("hook", "Woche"), beim("hook", "gleich")),
    pl("bleibt gleich", 860, 236, beim("hook", "gleich"), fill=HROT, size=28),
    *neinz("nur schreiben", 520, beim("hook2", "Schreiben"), "Bold", 36, x=170),
    *okz("aus jeder Korrektur lernen", 590, beim("hook2", "Korrektur"), "Bold", 36, x=170),
    blk(110, 690, 1040, 90, GELB, "wie", [("Wie viele? Und wie auswerten?", "ExtraBold", 40, INK)]),
    *requisit([("hook", ("tabler", "chart-line", 110, WEISS), "jede Woche 1 Klausur", WEISS),
               (beim("hook2", "Korrektur"), ("tabler", "file-search", 100, HELLGRUEN), "aus der Korrektur lernen", HELLGRUEN),
               ("wie", ("tabler", "list-numbers", 100, GELB), "Wie viele? Wie auswerten?", WEISS)]),
    *stehend("FR", X1, [("hook", "muede"), (beim("hook2", "Korrektur"), "denkt"), ("wie", "ruhig")]),
    *stehend("SB", X2, [("hook", "ruhig"), ("wie", "froh")]),
]))

# ===========================================================================================================================
# B Sachverhalt (Ausgangslage)
# ===========================================================================================================================
def sachverhalt_237(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 220
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=40, zeilenabstand=1.32)
        els += e; y += 22
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 14, cue, fill=PINK, size=38))
    folie([(cue, "Sachverhalt · Die Ausgangslage von Friedrich")], els)


sachverhalt_237("sv", [
    "Friedrich studiert Jura in Nordrhein-Westfalen. In 7 Monaten schreibt er die Klausuren der staatlichen "
    "Pflichtfachprüfung.",
    "Seit 12 Wochen schreibt er jede Woche eine Probeklausur im Klausurenkurs seiner Uni. Fast immer bekommt er 6 Punkte.",
    "Die Korrekturen liest er nicht: Er schaut auf die Note und schreibt die nächste Klausur.",
], "Wie viele Klausuren soll Friedrich schreiben, und wie wertet er sie aus?")

# ===========================================================================================================================
# C Das Problem: schreiben ohne auswerten
# ===========================================================================================================================
SB_C = ("SB_redet2", X2, FB, FR)


def haelfte(c, x, fill, kopf, unter, icon):
    els = [karte(x, 460, 505, 260, c, fill=fill, rund=18, schatten=8, rand=5, anim="pop"),
           z(kopf, x + 30, 485, c, "ExtraBold", 38, rechts=x + 400)]
    for i, t in enumerate(unter):
        els.append(z(t, x + 30, 580 + i * 46, c, "Bold", 32, rechts=x + 490))
    els.append(ticon("tabler", icon, x + 440, 545, 70, c, fuell=WEISS))
    return els


folie([("warum", "Problem · Warum bleibt die Note stehen?"), ("ohne", "Problem › schreiben ohne auswerten"),
       ("zwei", "Problem › 2 Hälften: Schreiben und Auswertung"), ("s2", "Problem › nur zur Hälfte geschrieben")], rechts_frei([
    *tafel("warum", "Warum bleibt die Note stehen?"),
    z("Friedrich schreibt, aber er wertet nicht aus.", 110, 185, "ohne", "Bold", 36),
    *neinz("Korrektur nicht gelesen: wieder dieselben Fehler", 260, beim("gleich", "Korrektur"), "Regular", 34, x=170),
    z("Eine Probeklausur hat 2 Hälften:", 110, 380, "zwei", "Bold", 36),
    *haelfte(beim("z1", "Schreiben"), 110, BLAU, "1. Schreiben", ["trainiert die Routine"], "writing"),
    *haelfte(beim("z2", "Auswertung"), 645, GRUEN, "2. Auswertung", ["zeigt dir, was du", "ändern musst"], "search"),
    *requisit([("warum", ("tabler", "chart-line", 110, WEISS), "Note bleibt stehen", HROT),
               ("ohne", ("tabler", "files", 110, WEISS), "geschrieben, nicht ausgewertet", WEISS),
               ("s2", None, None, None)]),
    *stehend("FR", X1, [("warum", "ratlos"), ("zwei", "denkt"), ("s2", "ruhig")]),
    *fig("SB", X2, FB, FR, [("warum", "ruhig"), ("zwei", "denkt")], bis="s2"),
    *redet("SB_redet2", X2, FB, FR, "s2", "viele"),
    ns(NAME["SB"], X2, FB, "warum", NFARBE["SB"], d=0.1),
    blase("sprech", 600, 250, "s2", 1500, 240, inhalt=["Eine Klausur, die du nicht", "auswertest, hast du nur",
                                                      "zur Hälfte geschrieben."], textsize=32, figur=SB_C, bis="viele"),
]))

# ===========================================================================================================================
# D Wie viele? Faustregel
# ===========================================================================================================================
def menge(c, y, text, n, fill):
    els = [blk(110, y, 1040, 100, fill, c, [(text, "ExtraBold", 36, INK)], anim="pop")]
    for i in range(n):
        els.append(ticon("tabler", "file-text", 1060 - i * 80, y + 88, 70, (c[0], c[1] + 0.15 * i) if isinstance(c, tuple)
                         else (c, 0.15 * i), fuell=WEISS))
    return els


folie([("viele", "Wie viele? · Wie viele Klausuren?"), ("faust", "Wie viele? › Faustregel, keine Vorschrift"),
       ("woche", "Wie viele? › Stoffphase: 1 pro Woche"), ("spurt", "Wie viele? › vor dem Examen: 2 pro Woche"),
       ("mehr", "Wie viele? › nur so viele, wie du auswertest")], rechts_frei([
    *tafel("viele", "Wie viele Klausuren?"),
    pl("Faustregel, keine Vorschrift", 110, 180, beim("faust", "Faustregel"), fill=GELB, size=34),
    *menge(beim("woche", "Stoffphase"), 270, "Stoffphase: 1 Klausur pro Woche", 1, HELLBLAU),
    *menge(beim("spurt", "letzten"), 400, "letzte Wochen vor dem Examen: 2", 2, HROT),
    z("Mehr bringt nur etwas, wenn du jede auswertest.", 110, 545, "mehr", "Bold", 34),
    *okz("lieber 1 Klausur weniger", 625, beim("lieber", "weniger"), "Bold", 36, x=170),
    *neinz("als 1 ohne Auswertung", 695, beim("lieber", "ohne"), "Bold", 36, x=170),
    *requisit([("viele", ("tabler", "files", 110, WEISS), "Wie viele?", WEISS),
               ("woche", ("tabler", "calendar-week", 110, HELLBLAU), "1 pro Woche", WEISS),
               ("spurt", ("tabler", "flag", 100, ROT), "Endspurt: 2 pro Woche", HROT),
               ("mehr", ("tabler", "file-search", 100, HELLGRUEN), "jede auswerten", HELLGRUEN)]),
    *allein("FR", [("viele", "denkt"), ("woche", "ruhig"), ("mehr", "denkt"), ("lieber", "entschlossen")]),
]))

# ===========================================================================================================================
# E Verteilung wie im Examen (Beispiel NRW, § 10 Abs. 2 S. 3 JAG NRW)
# ===========================================================================================================================
BX0, BW = 110, 1040


def balken(c, y, teil0, teil1, gesamt, fill, text, size=30, h=90, name="balken"):
    """Abschnitt eines waagerechten Balkens (teil0..teil1 von gesamt), Text mittig."""
    x0 = BX0 + BW * teil0 / gesamt; x1 = BX0 + BW * teil1 / gesamt
    w = int(round(x1 - x0))
    zeilen = text.split("\n")
    for t in zeilen:
        assert F("ExtraBold", size).getlength(glyphen(t)) <= w - 16, f"Balken zu schmal: {t}"
    def zz(dr, s):
        dr.rectangle((2 * s, 2 * s, (w - 2) * s, (h - 2) * s), fill=fill, outline=INK, width=4 * s)
        lh = size * 1.1
        for i, t in enumerate(zeilen):
            dr.text((w / 2 * s, (h / 2 - lh * (len(zeilen) - 1) / 2 + i * lh) * s), t, font=F("ExtraBold", size * s),
                    fill=INK, anchor="mm")
    return El(_flaeche(w, h, zz), x0, y, c, "pop", 0.0, None, name=f"{name}:{text.replace(chr(10), ' ')}")


folie([("fach", "Wie viele? › verteilt wie im Examen"), ("nrw", "Wie viele? › Beispiel Nordrhein-Westfalen: 6 Klausuren"),
       ("haelfte", "Wie viele? › Probeklausuren: 1/2, 1/3, 1/6"), ("land", "Wie viele? › dein Land kann es anders regeln"),
       ("v201", "Wie viele? › Lernplan: Folge 201")], rechts_frei([
    *tafel("fach", "Verteilt wie im Examen"),
    z("Examen in Nordrhein-Westfalen: 6 Klausuren", 110, 180, "nrw", "Bold", 34),
    balken(beim("nrw3", "drei"), 240, 0, 3, 6, BLAU, "3 Zivilrecht", 30),
    balken(beim("nrw2", "zwei"), 240, 3, 5, 6, GRUEN, "2 Öffentliches Recht", 26),
    balken(beim("nrw1", "eine"), 240, 5, 6, 6, ROT, "1\nStrafrecht", 26),
    zit("§ 10 Abs. 2 S. 3 JAG NRW", 110, 345, "nrw"),
    z("Deine Probeklausuren:", 110, 410, "haelfte", "Bold", 34),
    balken(beim("haelfte", "Hälfte"), 470, 0, 3, 6, BLAU, "1/2 Zivilrecht", 30),
    balken(beim("drittel", "Drittel"), 470, 3, 5, 6, GRUEN, "1/3 Öffentliches Recht", 26),
    balken(beim("sechstel", "Sechstel"), 470, 5, 6, 6, ROT, "1/6\nStrafrecht", 26),
    z("Dein Land kann das anders regeln.", 110, 610, "land", "Bold", 34),
    zit("§ 5d Abs. 6 S. 1 DRiG: Das Nähere regelt das Landesrecht.", 110, 660, "land"),
    blk(110, 730, 1040, 80, HGELB, "v201", [("Wie das in deinen Lernplan passt: Folge 201", "ExtraBold", 32, INK)]),
    *requisit([("fach", ("tabler", "scale", 110, WEISS), "wie im Examen", WEISS),
               ("nrw", ("tabler", "map-pin", 100, ROT), "Beispiel NRW", WEISS),
               ("haelfte", ("tabler", "chart-bar", 100, BLAU), "Probeklausuren", WEISS),
               ("land", ("tabler", "map-pin", 100, GELB), "dein Land", GELB),
               ("v201", ("tabler", "calendar", 100, HGELB), "Folge 201", HGELB)]),
    *allein("FR", [("fach", "ruhig"), ("haelfte", "denkt"), ("v201", "froh")]),
]))

# ===========================================================================================================================
# F Wie im Examen (§ 13 Abs. 1 S. 1, Abs. 3, § 10 Abs. 1 JAG NRW) und Referendariat (§ 5d Abs. 6 S. 1 DRiG)
# ===========================================================================================================================
folie([("bed", "Wie im Examen · Examensbedingungen"), ("zeit", "Wie im Examen › 5 Stunden am Stück"),
       ("hilf", "Wie im Examen › nur erlaubte Hilfsmittel"), ("form", "Wie im Examen › von Hand oder am Computer"),
       ("handy", "Wie im Examen › Handy aus, Lehrbuch zu"), ("abbr", "Wie im Examen › nicht abbrechen"),
       ("ref", "Wie im Examen › Referendariat: genauso auswerten")], rechts_frei([
    *tafel("bed", "Unter Examensbedingungen"),
    blk(110, 170, 1040, 70, HELLBLAU, beim("zeit", "fünf"), [("5 Stunden am Stück", "ExtraBold", 34, INK)]),
    zit("NRW: 5 Stunden je Examensklausur, § 13 Abs. 1 S. 1 JAG NRW", 110, 248, beim("zeit", "fünf")),
    blk(110, 300, 1040, 70, HELLGRUEN, "hilf", [("nur die Hilfsmittel, die dein Land erlaubt", "ExtraBold", 34, INK)]),
    zit("z. B. § 13 Abs. 3 JAG NRW", 110, 378, "hilf"),
    blk(110, 430, 1040, 70, HGELB, "form", [("in deiner Form: von Hand oder am Computer", "ExtraBold", 34, INK)]),
    zit("z. B. § 10 Abs. 1 S. 2, 3 JAG NRW", 110, 508, "form"),
    *okz("Handy aus, Lehrbuch zu", 565, "handy", "Bold", 34, x=170),
    *okz("nicht abbrechen, wenn es schlecht läuft", 630, "abbr", "Bold", 34, x=170),
    blk(110, 715, 1040, 76, LILA, "ref", [("Referendariat: genauso auswerten", "ExtraBold", 34, INK)]),
    zit("Zahl und Dauer regelt dein Land, § 5d Abs. 6 S. 1 DRiG", 110, 800, beim("ref", "Zahl")),
    *requisit([("bed", ("tabler", "school", 110, WEISS), "wie im Examen", WEISS),
               ("zeit", ("tabler", "clock", 100, HELLBLAU), "5 Stunden", WEISS),
               ("hilf", ("tabler", "book", 100, HELLGRUEN), "Hilfsmittel", WEISS),
               ("form", ("tabler", "pencil", 100, GELB), "von Hand oder Computer", WEISS),
               ("handy", ("tabler", "device-mobile-off", 100, WEISS), "Handy aus", WEISS),
               ("abbr", ("tabler", "hand-stop", 100, HROT), "nicht abbrechen", HROT),
               ("ref", ("tabler", "briefcase", 100, LILA), "Referendariat", WEISS)]),
    *allein("FR", [("bed", "ruhig"), ("zeit", "entschlossen"), ("abbr", "denkt"), ("ref", "ruhig")]),
]))

# ===========================================================================================================================
# G–J Auswertung in vier Schritten (Schrittleiste durchgehend)
# ===========================================================================================================================
SCHRITTE = ["Korrektur", "Musterlösung", "Fehlerprotokoll", "Karten"]
SL_Y, SL_H, SL_W = 170, 66, 260


def schritt_kasten(c, i, zustand):
    """zustand: 'leer' (nur Nummer), 'aktiv' (gelb), 'fertig' (grün mit Haken-Zahl)."""
    w, h = SL_W, SL_H
    fill = {"leer": GRAU2, "aktiv": GELB, "fertig": HELLGRUEN}[zustand]
    text = f"{i + 1}" if zustand == "leer" else f"{i + 1} {SCHRITTE[i]}"
    assert F("ExtraBold", 26).getlength(glyphen(text)) <= w - 20, text
    def zz(dr, s):
        dr.rounded_rectangle((3 * s, 3 * s, (w - 3) * s, (h - 3) * s), 12 * s, fill=fill, outline=INK, width=4 * s)
        dr.text((w / 2 * s, h / 2 * s), text, font=F("ExtraBold", 26 * s), fill=INK, anchor="mm")
    return El(_flaeche(w, h, zz), 110 + i * SL_W, SL_Y, c, "pop", 0.0, None, name=f"schritt:{i + 1}:{zustand}")


def schrittleiste(c, aktiv):
    """Schrittleiste im Stand 'aktiv' (Schritte davor fertig), hart ab Folienbeginn."""
    return [hart(schritt_kasten(c, i, "fertig" if i < aktiv else "aktiv" if i == aktiv else "leer")) for i in range(4)]


# --- G Schritt 1: Korrektur lesen -----------------------------------------------------------------------------------------
SEITE = (130, 270, 420, 560)                  # korrigierte Klausur: x, y, w, h


def korrigiert(c, rand_c):
    x, y, w, h = SEITE
    els = [karte(x, y, w, h, c, fill=WEISS, rund=12, schatten=8, rand=4),
           z("Probeklausur 12", x + 26, y + 20, c, "ExtraBold", 30, rechts=x + w - 16),
           linienzug([(x + 320, y + 80), (x + 320, y + h - 24)], c, breite=4, farbe=ROT)]
    for i in range(8):
        yy = y + 100 + i * 52
        els.append(linienzug([(x + 26, yy), (x + 290 - (i % 3) * 40, yy)], c, breite=5, farbe=GRAU))
    for i, (yy, t) in enumerate([(100, "?"), (205, "!"), (310, "?"), (415, "?")]):
        els.append(pl(t, x + 345, y + yy - 20, (rand_c[0], rand_c[1] + 0.12 * i), fill=ROT, size=30))
    return els


folie([("aus", "Auswertung · 4 Schritte"), ("a1", "Auswertung › 1. Korrektur lesen"),
       ("a1b", "Auswertung › 1. jede Randbemerkung")], rechts_frei([
    *tafel("aus", "Die Auswertung in 4 Schritten"),
    *[schritt_kasten(("aus", 0.3 + 0.12 * i), i, "leer") for i in range(4)],
    bis_(schritt_kasten(beim("a1", "Lies"), 0, "aktiv"), None),
    *korrigiert(beim("a1", "Lies"), beim("a1b", "Randbemerkung")),
    pl("6 Punkte", SEITE[0] + 26, SEITE[1] + SEITE[3] - 70, beim("a1", "Note"), fill=ROT, size=32),
    z("Lies die ganze Korrektur,", 600, 300, beim("a1", "Lies"), "Bold", 34),
    z("nicht nur die Note.", 600, 350, beim("a1", "Note"), "Bold", 34),
    z("Jede Randbemerkung zeigt:", 600, 470, beim("a1b", "Randbemerkung"), "Regular", 32),
    z("Hier gingen Punkte verloren.", 600, 516, beim("a1b", "Punkte"), "Bold", 32),
    *requisit([("aus", ("tabler", "list-numbers", 100, GELB), "4 Schritte", WEISS),
               ("a1", ("tabler", "file-search", 100, WEISS), "Korrektur lesen", GELB)]),
    *allein("FR", [("aus", "ruhig"), ("a1", "denkt"), ("a1b", "staunt")]),
]))

# --- H Schritt 2: Musterlösung gegen die eigene Gliederung --------------------------------------------------------------------
def gliederung(c, x, kopf, punkte, fill):
    els = [karte(x, 270, 500, 470, c, fill=fill, rund=16, schatten=6, rand=4),
           z(kopf, x + 26, 290, c, "ExtraBold", 32, rechts=x + 480)]
    for i, t in enumerate(punkte):
        els.append(blk(x + 26, 360 + i * 92, 448, 72, WEISS, (c[0], c[1] + 0.1 * i) if isinstance(c, tuple) else (c, 0.1 * i),
                       [(t, "Bold", 30, INK)], anim="pop"))
    return els


folie([("a2", "Auswertung › 2. Musterlösung neben die Gliederung"), ("a2b", "Auswertung › 2. Problem übersehen?"),
       ("a2c", "Auswertung › 2. anders aufgebaut: warum?")], rechts_frei([
    *tafel("a2", "Die Auswertung in 4 Schritten"),
    *schrittleiste("a2", 1),
    *gliederung(beim("a2", "Musterlösung"), 110, "Musterlösung", ["I. Problem A", "II. Problem B", "III. Problem C",
                                                                  "IV. Problem D"], HELLGRUEN),
    *gliederung(beim("a2", "Gliederung"), 650, "deine Gliederung", ["I. Problem A", "II. Problem C", "III. Problem B"], HELLBLAU),
    ring(110 + 26 + 224, 360 + 3 * 92 + 36, 250, 50, beim("a2b", "Problem"), farbe=DROT, breite=6),
    pl("übersehen?", 676, 360 + 3 * 92 + 8, beim("a2b", "übersehen"), fill=HROT, size=32),
    ring(650 + 26 + 224, 360 + 1.5 * 92 + 36, 262, 112, beim("a2c", "anders"), farbe=ORANGE, breite=6),
    pl("anders aufgebaut: warum?", 110, 790, beim("a2c", "anders"), fill=HGELB, size=32),
    *requisit([("a2", ("tabler", "arrows-diff", 100, WEISS), "Musterlösung neben Gliederung", HELLGRUEN),
               ("a2b", ("tabler", "zoom-question", 100, HROT), "Problem übersehen?", HROT)]),
    *allein("FR", [("a2", "denkt"), ("a2b", "ratlos"), ("a2c", "denkt")]),
]))

# --- I Schritt 3: das Fehlerprotokoll (Fehlerarten, Zählung von Friedrich) ----------------------------------------------------
FEHLER = [("fa", "Aufbau", "pa", 2), ("fs", "Schwerpunkt", "ps", 7), ("fw", "Wissen", "pw", 3), ("fz", "Zeit", "pz", 5)]
FP_Y0, FP_H, FP_D = 330, 74, 90
QX0, QW = 470, 52


def zaehler(c, y, n, fill):
    """n Kästchen nebeneinander (eine Kästchen je Fehler) und die Zahl dahinter."""
    w = n * QW + 70
    def zz(dr, s):
        for i in range(n):
            dr.rounded_rectangle(((i * QW + 3) * s, 12 * s, (i * QW + QW - 6) * s, 58 * s), 8 * s, fill=fill, outline=INK, width=4 * s)
        dr.text(((n * QW + 20) * s, 35 * s), str(n), font=F("ExtraBold", 40 * s), fill=INK, anchor="lm")
    return El(_flaeche(w, 70, zz), QX0, y, c, "pop", 0.0, None, name=f"zaehler:{n}")


FR_I = ("FR_redet2", X1, FB, FR)
folie([("a3", "Auswertung › 3. das Fehlerprotokoll"), ("fa", "Auswertung › 3. Aufbau, Schwerpunkt, Wissen, Zeit"),
       ("v117", "Auswertung › 3. typische Fehler: Folge 117"), ("prot", "Auswertung › 3. Protokoll von Friedrich: 12 Klausuren"),
       ("f3", "Auswertung › 3. die Punkte gehen am Schwerpunkt verloren")], rechts_frei([
    *tafel("a3", "Die Auswertung in 4 Schritten"),
    *schrittleiste("a3", 2),
    z("Jeder Fehler bekommt eine Fehlerart:", 110, 262, beim("a3b", "Fehler"), "Bold", 32),
    *[blk(110, FP_Y0 + i * FP_D, 330, FP_H, (HGELB, HROT, HELLBLAU, HELLGRUEN)[i], beim(c, t[:4]) if c != "fz" else beim("fz", "Zeit"),
          [(t, "ExtraBold", 34, INK)], anim="pop") for i, (c, t, _, _) in enumerate(FEHLER)],
    pl("Friedrich, 12 Klausuren", 760, 255, "prot", fill=GRUEN, size=30),
    *[zaehler(beim(pc, w_), FP_Y0 + i * FP_D + 2, n, (GELB, ROT, BLAU, GRUEN)[i])
      for i, ((_, _, pc, n), w_) in enumerate(zip(FEHLER, ["Aufbau", "Schwerpunkt", "Wissen", "Zeit"]))],
    ring(QX0 + 220, FP_Y0 + FP_D + 36, 245, 56, beim("f3", "Schwerpunkt"), farbe=DROT, breite=7),
    zit("die typischen Fehler im Einzelnen: Folge 117", 110, FP_Y0 + 4 * FP_D + 20, beim("v117", "typischen")),
    *requisit([("a3", ("tabler", "clipboard-list", 100, WEISS), "Fehlerprotokoll", GELB),
               ("prot", ("tabler", "chart-bar", 100, ROT), "12 Klausuren ausgewertet", WEISS),
               ("f3", None, None, None)]),
    *fig("FR", X1, FB, FR, [("a3", "ruhig"), ("prot", "denkt"), (beim("ps", "Schwerpunkt"), "staunt")], bis="f3"),
    *redet("FR_redet2", X1, FB, FR, "f3", "a4"),
    ns(NAME["FR"], X1, FB, "a3", NFARBE["FR"], d=0.1),
    *stehend("SB", X2, [("a3", "ruhig"), ("prot", "denkt"), ("f3", "froh")]),
    blase("sprech", 600, 250, "f3", 1520, 240, inhalt=["Ich dachte, mir fehlt Wissen.", "Dabei verliere ich die Punkte",
                                                      "am Schwerpunkt."], textsize=32, figur=FR_I, bis="a4"),
]))

# --- J Schritt 4: Wiederholungskarten -----------------------------------------------------------------------------------------
def karteikarte(c, x, y, kopf, zeilen, fill):
    els = [karte(x, y, 500, 260, c, fill=fill, rund=14, schatten=8, rand=4),
           z(kopf, x + 30, y + 26, c, "ExtraBold", 36, rechts=x + 480)]
    for i, t in enumerate(zeilen):
        els.append(z(t, x + 30, y + 96 + i * 48, c, "Bold", 32, rechts=x + 480))
    return els


folie([("a4", "Auswertung › 4. Wiederholungskarten"), ("a4b", "Auswertung › 4. vorn der Fehler, hinten die Lösung"),
       ("a4c", "Auswertung › 4. Karten in die Wiederholung")], rechts_frei([
    *tafel("a4", "Die Auswertung in 4 Schritten"),
    *schrittleiste("a4", 3),
    z("Aus jedem Fehler wird eine Wiederholungskarte.", 110, 265, beim("a4", "Fehler"), "Bold", 34),
    *karteikarte(beim("a4b", "Vorn"), 110, 340, "vorn:", ["die Stelle, an der du", "Punkte verloren hast"], HGELB),
    *karteikarte(beim("a4b", "hinten"), 650, 340, "hinten:", ["wie es richtig geht"], HELLGRUEN),
    blk(110, 650, 1040, 90, LILA, beim("a4c", "Wiederholung"), [("Die Karten kommen in deine Wiederholung.", "ExtraBold", 36, INK)]),
    ticon("tabler", "repeat", 1100, 735, 70, beim("a4c", "Wiederholung"), fuell=WEISS),
    zit("Wiederholung in wachsenden Abständen: Folge 201", 110, 760, beim("a4c", "Folge")),
    *requisit([("a4", ("tabler", "cards", 110, GELB), "Wiederholungskarten", WEISS),
               ("a4c", ("tabler", "repeat", 100, LILA), "Wiederholung", WEISS)]),
    *allein("FR", [("a4", "entschlossen"), ("a4c", "froh")]),
]))

# ===========================================================================================================================
# K Wochenrhythmus (Auswertungstag, Klausurtag)
# ===========================================================================================================================
WSP = [120, 300, 620]                         # Tag, morgens, Tagesplan
WX0, WY0, WZH = 110, 170, 86


def wzelle(c, zeile, spalte, text, fill, size=30, stil="Bold", anim="pop", bis=None):
    x = WX0 + sum(WSP[:spalte]); w = WSP[spalte]; y = WY0 + zeile * WZH
    assert size >= 26 and F(stil, size).getlength(glyphen(text)) <= w - 20, f"Tabellenzelle zu breit: {text}"
    def zz(dr, s):
        dr.rectangle((2 * s, 2 * s, (w - 2) * s, (WZH - 2) * s), fill=fill, outline=INK, width=4 * s)
        dr.text((w / 2 * s, WZH / 2 * s), text, font=F(stil, size * s), fill=INK, anchor="mm")
    return El(_flaeche(w, WZH, zz), x, y, c, anim, 0.0, bis, name=f"wzelle:{zeile}:{spalte}:{text}")


TAGE = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
els_w = [*tafel("wr", "Eine Woche von Friedrich")]
els_w += [wzelle("wr", 0, 0, "Tag", GELB, stil="ExtraBold", anim="rise"),
          wzelle("wr", 0, 1, "morgens", GELB, stil="ExtraBold", anim="rise"),
          wzelle("wr", 0, 2, "Tagesplan", GELB, stil="ExtraBold", anim="rise")]
for zi, t in enumerate(TAGE, 1):
    els_w.append(wzelle("wr", zi, 0, t, HELL, stil="ExtraBold", anim="rise"))
assert WY0 + 8 * WZH <= 890
WMO = beim("wmo", "Montag")
els_w += [wzelle(WMO, 1, 2, "Auswertungstag", HROT, bis="wmo2"),
          wzelle("wmo2", 1, 2, "Korrektur, Musterlösung, Protokoll", HROT, size=28, anim="cut")]
for zi in range(2, 6):
    c = beim("wdi", "Dienstag")
    els_w.append(wzelle((c[0], c[1] + 0.08 * zi), zi, 2, "Stoff", HELLBLAU, bis=("wfr" if zi == 5 else None)))
    k = beim("wkarte", "Morgen")
    els_w.append(wzelle((k[0], k[1] + 0.08 * zi), zi, 1, "Fehlerkarten", LILA))
els_w += [wzelle(beim("wfr", "Freitag"), 5, 2, "Stoff, dann Fehlerarten zählen", HELLBLAU, size=28, anim="cut"),
          wzelle(beim("wsa", "Samstag"), 6, 2, "Klausurtag: 5 Stunden", PINK),
          wzelle(beim("wso", "Sonntag"), 7, 2, "frei", GELB)]
folie([("wr", "Wochenrhythmus · eine Woche von Friedrich"), ("wmo", "Wochenrhythmus › Montag: Auswertungstag"),
       ("wdi", "Wochenrhythmus › Dienstag bis Freitag: Stoff"), ("wkarte", "Wochenrhythmus › morgens: Fehlerkarten"),
       ("wfr", "Wochenrhythmus › Freitag: häufigste Fehlerart zählen"), ("wsa", "Wochenrhythmus › Samstag: Klausurtag"),
       ("wso", "Wochenrhythmus › Sonntag: frei")], rechts_frei([
    *els_w,
    *requisit([("wr", ("tabler", "calendar-week", 110, WEISS), "1 Woche", WEISS),
               ("wmo", ("tabler", "file-search", 100, HROT), "Auswertungstag", HROT),
               ("wdi", ("tabler", "books", 120, GELB), "Stoff", WEISS),
               ("wkarte", ("tabler", "cards", 100, LILA), "Fehlerkarten", WEISS),
               ("wfr", ("tabler", "chart-bar", 100, GELB), "häufigste Fehlerart?", WEISS),
               ("wsa", ("tabler", "clock", 100, PINK), "Klausurtag", WEISS),
               ("wso", ("tabler", "sun", 100, GELB), "frei", WEISS)]),
    *allein("FR", [("wr", "ruhig"), ("wmo", "entschlossen"), ("wfr", "denkt"), ("wso", "froh")]),
]))

# ===========================================================================================================================
# L Ergebnis: drei Wochen später (Büro)
# ===========================================================================================================================
FR_L = ("FR_redetfroh_r", FRX, BODEN_Y, FHA)
SB_L = ("SB_redetfroh", SBX, BODEN_Y, FHA)
_bl = blatt_bild()
BLX = 900
folie([("erg", "Ergebnis · 3 Wochen später"), ("erg2", "Ergebnis › kein Schwerpunkt-Fehler am Rand"),
       ("f4", "Ergebnis › 7 Punkte, als Nächstes die Zeit"), ("s3", "Ergebnis › ein Fehler nach dem anderen")], [
    *buero("erg"),
    hart(pl("3 Wochen später", 70, 30, "erg", fill=PINK, size=38)),
    El(_bl, BLX, TOP - _bl.height + 6, beim("erg", "Korrektur"), "pop", 0.0, None, name="blatt"),
    pl("kein Schwerpunkt-Fehler am Rand", BLX + 60, TOP - 150, beim("erg2", "Schwerpunkt"), fill=HELLGRUEN, size=28, anker="m"),
    pl("7 Punkte", BLX + 60, TOP - 225, beim("f4", "Sieben"), fill=GRUEN, size=32, anker="m"),
    *fig("FR", FRX, BODEN_Y, FHA, [("erg", "ruhig_r"), ("erg2", "stolz_r")], erst="cut", bis="f4"),
    *redet("FR_redetfroh_r", FRX, BODEN_Y, FHA, "f4", "s3"),
    *fig("FR", FRX, BODEN_Y, FHA, [("s3", "froh_r")], erst="cut", bis="tipp"),
    hart(ns(NAME["FR"], FRX, BODEN_Y, "erg", NFARBE["FR"])),
    *fig("SB", SBX, BODEN_Y, FHA, [("erg", "ruhig"), ("erg2", "froh")], erst="cut", bis="s3"),
    *redet("SB_redetfroh", SBX, BODEN_Y, FHA, "s3", "tipp"),
    hart(ns(NAME["SB"], SBX, BODEN_Y, "erg", NFARBE["SB"])),
    blase("sprech", 600, 220, "f4", 560, 230, inhalt=["7 Punkte. Und als Nächstes", "nehme ich mir die Zeit vor."], textsize=32,
          figur=FR_L, bis="s3"),
    blase("sprech", 520, 200, "s3", 1420, 250, inhalt=["Genau so. Ein Fehler", "nach dem anderen."], textsize=34,
          figur=SB_L, bis="tipp"),
])

# ===========================================================================================================================
# M Klausurtipp (Lexi): ein Ziel pro Probeklausur
# ===========================================================================================================================
def skizze(c, x, y, w, h):
    els = [karte(x, y, w, h, c, fill=WEISS, rund=12, schatten=8, rand=4),
           z("Lösungsskizze", x + 26, y + 20, c, "ExtraBold", 30, rechts=x + w - 16)]
    for i in range(5):
        yy = y + 150 + i * 46
        els.append(linienzug([(x + 26, yy), (x + w - 60 - (i % 3) * 50, yy)], c, breite=5, farbe=GRAU))
    return els


els_k = [*tafel("tipp", "Klausurtipp: 1 Ziel pro Probeklausur", fill=HELL), warnung_i(150, 225, "tipp", gr=26),
         z("Nimm deine häufigste Fehlerart als Ziel mit.", 200, 200, beim("tipp", "häufigste"), "Bold", 32),
         *skizze(beim("tipp2", "Schreib"), 130, 290, 520, 430),
         pl("Ziel: häufigste Fehlerart", 156, 360, beim("tipp2", "oben"), fill=GELB, size=30),
         z("oben auf die", 700, 340, beim("tipp2", "oben"), "Bold", 34),
         z("Lösungsskizze", 700, 390, beim("tipp2", "oben"), "Bold", 34),
         blk(700, 500, 450, 160, HELLGRUEN, "tipp3", [("Vor dem Ausformulieren:", "Bold", 30, INK),
                                                     ("Gliederung genau", "ExtraBold", 32, INK),
                                                     ("darauf prüfen", "ExtraBold", 32, INK)]),
         *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
         ns("Lexi", FX, FB, "tipp", GELB, d=0.2)]
folie([("tipp", "Klausurtipp · 1 Ziel pro Probeklausur"), ("tipp2", "Klausurtipp › oben auf die Lösungsskizze"),
       ("tipp3", "Klausurtipp › Gliederung darauf prüfen")], els_k)

# ===========================================================================================================================
# N Dein Klausurtraining in 5 Schritten (Schema, Punkt für Punkt)
# ===========================================================================================================================
REIHEN = [("k1", "I.", "1 Klausur pro Woche, im Endspurt 2", BLAU),
          ("k2", "II.", "verteilt wie im Examen", GRUEN),
          ("k3", "III.", "unter Examensbedingungen: 5 Stunden am Stück", HELLBLAU),
          ("k4", "IV.", "auswerten: Korrektur, Musterlösung, Fehlerprotokoll, Karten", GELB),
          ("k5", "V.", "ein fester Auswertungstag in jeder Woche", HROT)]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Dein Klausurtraining in 5 Schritten"), 110, 90, "sch", 50)]
y = 230
for c, nr, text, f in REIHEN:
    els_sch.append(pl(nr, 130, y - 6, c, fill=f, size=36))
    els_sch.append(z(text, 300, y, c, "ExtraBold", 40, rechts=1820))
    y += 135
assert y <= 960, y
folie([("sch", "Klausurtraining · 5 Schritte"), ("k1", "Klausurtraining › I. 1 pro Woche, im Endspurt 2"),
       ("k2", "Klausurtraining › II. verteilt wie im Examen"), ("k3", "Klausurtraining › III. Examensbedingungen"),
       ("k4", "Klausurtraining › IV. auswerten"), ("k5", "Klausurtraining › V. fester Auswertungstag")], els_sch)

# ===========================================================================================================================
# O Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Eine Klausur bringt dir erst Punkte,", 0)], [("wenn du sie ", 0), ("auswertest", "a"), (".", 0)]],
                750, 300, 44, "merke", {"a": beim("merke", "auswertest")}),
    *markertext([[("Schreib so viele, wie du", 0)], [("gründlich auswerten", "b"), (" kannst,", 0)]],
                750, 480, 44, "m2", {"b": beim("m2", "gründlich")}),
    *markertext([[("damit dir jeder Fehler", 0)], [("nur ", 0), ("einmal", "c"), (" passiert.", 0)]], 750, 660, 44, "m3",
                {"c": beim("m3", "einmal")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
