"""Folge 263 · Leben gegen Leben: Übergesetzlicher entschuldigender Notstand – Serienstandard Open Peeps (Katzenkönig).
Fall (Plan-Hook): Montag, 6:40 Uhr. Frau Seefeld (Ende 20) hat Dienst im Stellwerk; Herr Nordmann aus dem Nachbarstellwerk meldet
einen führerlosen Güterzug. Auf Gleis 1 arbeitet ein Bautrupp (5 Arbeiter), nicht erreichbar; Frau Seefeld stellt Weiche 7 auf
das Nebengleis um, wo ein einzelner Arbeiter steht. Die 5 bleiben unverletzt, der Arbeiter auf dem Nebengleis kommt ums Leben.
Darstellung: kein Zusammenstoß, kein Opfer im Bild – Zug (Tabler-Icon) und Weiche im Schienenplan, Arbeiter als graue
Open-Peeps-Silhouetten mit Abstand; beim Satz „kommt ums Leben“ ist auf dem Nebengleis niemand mehr zu sehen (nur eine Pille).
Ärzteverfahren der Nachkriegszeit nur als Text, ohne Bilder.
Szenen laut ../SZENENPLAN.md: A1 Stellwerk, A2 Nachbarstellwerk (Anruf), A3 Schienenplan, A4 Fragen, B Sachverhalt,
C Tatbestand § 212, D § 34 (Wortlautkarte), E1 Leben gegen Leben, E2 BVerfGE 115, 118, F § 35 (Wortlautkarte),
G Übergesetzlicher Notstand: Herkunft, H Voraussetzungen, I Ansichten, J Gefahrengemeinschaft/Weichensteller, K Ergebnis,
L Stellwerk (Blase), M Klausurtipp (Lexi), N Schema, O Merksatz (Lexi).
Handlungsgeräusche: Telefon klingelt (A1, szene_263telefon_1), Weichenhebel (A3, szene_263weiche_1); ../geraeusche_herkunft.json.
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz
als eigene Kopie aus Folge 189 (gemeinsame Dateien unverändert); neu: raum(), pult(), telefon_tisch(), gleisplan(), zug(),
weichenlage(), silh(), zitatkarte().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut nach gesetze-im-internet.de, BVerfG-Zitat nach dem Volltext auf
bundesverfassungsgericht.de (Abruf 08.10.2026)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave
import datetime as _dt

bausteine.FIGORDNER = "op_263/"

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
HELLGRAU = (226, 226, 222, 255)
TUERKIS = (127, 214, 208, 255)
ORANGE = (249, 166, 108, 255)
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
    e = pille(glyphen(text), *a, **k)
    return e


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
        if n.startswith(("bild:", "ficon:")) or "/op_263/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


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
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 08.10.2026), als Zitat mit Normangabe; der
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 168/180) -------------------------------------
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
    """Namensschild unter der Figur (ab ihrem ersten Auftritt, solange sie im Bild ist); lange Schilder in 26 px."""
    return pl(text, cx, unten + 22, cue, fill=fill, size=26 if len(text) > 14 else 30, anker="m", **k)


def okz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Haken davor (zur gesprochenen Bejahung)."""
    return [ok(x - 45, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]


def neinz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Kreuz davor (zur gesprochenen Verneinung)."""
    return [nein(x - 45, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]






# --- eigene Szenenbausteine (programmatisch, Palettenflächen, Tuschekontur) ---------------------------------------------------
BODEN_Y = 905                                # Boden = Unterkante der Figuren in den Fallszenen
FHA = 480                                    # Figurenhöhe in den Fallszenen
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
WAND = (238, 230, 214, 255)
WAND2 = (226, 236, 232, 255)
PULT = (150, 160, 178, 255)
SCHIRM = (52, 66, 82, 255)
GLEIS = (86, 90, 100, 255)
SCHWELLE = (176, 150, 120, 255)
HIMMEL = (214, 232, 250, 255)
HELLROT2 = (250, 196, 186, 255)


def _flaeche(w, h, zeichne):
    s = 2
    im = Image.new("RGBA", (w * s, h * s))
    zeichne(ImageDraw.Draw(im), s)
    return im.resize((w, h), Image.LANCZOS)


def raum(c, wand=WAND, fenster_x=140, name="raum"):
    """Stellwerksraum (Grundform): Wand, großes Fenster mit Blick auf zwei Gleise, Bodenlinie; ohne Logo."""
    w, h = 1800, BODEN_Y - 100

    def zz(dr, s):
        dr.rectangle((0, 0, w * s, h * s), fill=wand)
        fx0, fy0, fw, fh = fenster_x, 50, 520, 300
        dr.rounded_rectangle((fx0 * s, fy0 * s, (fx0 + fw) * s, (fy0 + fh) * s), 10 * s, fill=HIMMEL, outline=INK, width=6 * s)
        for gy in (fy0 + 200, fy0 + 250):                 # zwei Gleise im Fenster
            dr.line(((fx0 + 6) * s, gy * s, (fx0 + fw - 6) * s, gy * s), fill=GLEIS, width=5 * s)
        dr.line(((fx0 + fw / 2) * s, fy0 * s, (fx0 + fw / 2) * s, (fy0 + fh) * s), fill=INK, width=5 * s)
        dr.line((0, (h - 3) * s, w * s, (h - 3) * s), fill=INK, width=6 * s)
    return hart(El(_flaeche(w, h, zz), 60, 100, c, "cut", 0.0, None, name=name))


def pult(c, x0=700, x1=1300, bild="plan"):
    """Stellpult mit Bildschirm (vereinfachter Gleisplan als Linien, ohne Beschriftung); steht auf dem Boden."""
    w, h = x1 - x0, 470

    def zz(dr, s):
        dr.rounded_rectangle((60 * s, 0, (w - 170) * s, 200 * s), 12 * s, fill=SCHIRM, outline=INK, width=6 * s)
        if bild == "plan":
            dr.line((90 * s, 90 * s, (w - 200) * s, 90 * s), fill=(143, 214, 148, 255), width=6 * s)
            dr.line((210 * s, 90 * s, 290 * s, 150 * s, (w - 200) * s, 150 * s), fill=(143, 214, 148, 255), width=6 * s, joint="curve")
        dr.rectangle(((w / 2 - 75) * s, 200 * s, (w / 2 - 35) * s, 250 * s), fill=PULT, outline=INK, width=5 * s)
        dr.polygon([(0, 250 * s), (w * s, 250 * s), ((w - 30) * s, 300 * s), (30 * s, 300 * s)], fill=PULT, outline=INK)
        dr.line([(0, 250 * s), (w * s, 250 * s), ((w - 30) * s, 300 * s), (30 * s, 300 * s), (0, 250 * s)], fill=INK, width=5 * s)
        dr.rectangle((50 * s, 300 * s, (w - 50) * s, (h - 3) * s), fill=PULT, outline=INK, width=5 * s)
        for xx in (120, w - 160):
            dr.rounded_rectangle((xx * s, 340 * s, (xx + 40) * s, 400 * s), 6 * s, fill=(255, 255, 255, 255), outline=INK, width=3 * s)
    return hart(El(_flaeche(w, h, zz), x0, BODEN_Y - h, c, "cut", 0.0, None, name="pult"))


# Schienenplan (A3): Gleis 1 waagrecht, Weiche 7 bei SW, Nebengleis schräg nach unten und dann waagrecht
SW = (520, 470)
G1_Y, G2_Y, G_ENDE = 470, 650, 1380
KNICK = (760, 650)


def gleisplan(c):
    """Schienenplan als Grundfläche: zwei Gleise mit Schwellen, Weiche 7 (Kreis), ohne Logos."""
    w, h = 1360, 260
    ox, oy = 60, 430

    def zz(dr, s):
        P = lambda x, y: ((x - ox) * s, (y - oy) * s)

        def gleis(a, b):
            import math
            dx, dy = b[0] - a[0], b[1] - a[1]; ln = math.hypot(dx, dy)
            nx, ny = -dy / ln, dx / ln
            for k in range(0, int(ln), 36):
                px, py = a[0] + dx * k / ln, a[1] + dy * k / ln
                dr.line([P(px + nx * 16, py + ny * 16), P(px - nx * 16, py - ny * 16)], fill=SCHWELLE, width=7 * s)
            dr.line([P(*a), P(*b)], fill=GLEIS, width=11 * s)
        gleis((80, G1_Y), (G_ENDE, G1_Y))
        gleis(SW, KNICK)
        gleis(KNICK, (G_ENDE, G2_Y))
        dr.ellipse([P(SW[0] - 16, SW[1] - 16), P(SW[0] + 16, SW[1] + 16)], fill=(255, 255, 255, 255), outline=INK, width=5 * s)
    return hart(El(_flaeche(w, h, zz), ox, oy, c, "cut", 0.0, None, name="gleisplan"))


def weichenlage(c, lage, bis=None):
    """Weichenstellung als gelbe Markierung hinter der Weiche (gerade = Gleis 1, abzweig = Nebengleis)."""
    if lage == "gerade":
        pts = [(SW[0] + 18, G1_Y), (SW[0] + 200, G1_Y)]
    else:
        pts = [(SW[0] + 14, G1_Y + 11), (SW[0] + 150, G1_Y + 113)]
    e = linienzug(pts, c, breite=16, farbe=GELB)
    e.anim, e.bis, e.name = "cut", bis, f"weiche:{lage}"
    return e


def silh(nr, x, unten, cue, bis=None, hoehe=130):
    """Gleisarbeiter als graue Open-Peeps-Silhouette mit Abstand (kein Gesicht, kein Opferbild)."""
    return peep_voll(f"GA_{nr}", x, unten, hoehe, cue, anim="cut", bis=bis)


X1, X2 = 1395, 1730                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"SE": "Frau Seefeld", "NO": "Herr Nordmann"}
NFARBE = {"SE": ORANGE, "NO": BLAU}


def stehend(k, x, folge, unten=930, hoehe=480, bis=None):
    return [*fig(k, x, unten, hoehe, folge, bis=bis), ns(NAME[k], x, unten, folge[0][0], NFARBE[k], d=0.1, bis=bis)]


def requisit(folge, px=PX):
    """Wechselndes Requisit über den Figuren: folge = [(cue, (set, icon, breite, fuell), pillentext, pillenfarbe)]."""
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


def bis_l(els, bis):
    for e in els:
        e.bis = bis
    return els


PA = "A. Frau Seefeld, § 212 StGB"

# ===========================================================================================================================
# A1 Fall: Stellwerk, Montag 6:40 Uhr – Anruf
# ===========================================================================================================================
SEX1 = 1560
folie([(NULL, "Fall · Stellwerk, Montag 6:40 Uhr"), ("anruf", "Fall · Anruf aus dem Nachbarstellwerk")], [
    raum(NULL),
    pult(NULL),
    hart(pl("Montag, 6:40 Uhr", 70, 30, NULL, fill=WEISS, size=38)),
    hart(pl("Stellwerk", 520, 30, NULL, fill=GELB, size=38)),
    *stehend("SE", SEX1, [("seefeld", "ruhig"), ("anruf", "ernst")], unten=BODEN_Y),
    pl("Ende 20, im Dienst", SEX1, 330, beim("seefeld", "hat"), fill=WEISS, size=30, anker="m", bis="anruf"),
    szene(ficon("tabler", "phone-ringing", 1225, BODEN_Y - 222, 80, "anruf", fuell=WEISS), "263telefon*", 0.9, 0.0),
    pl("Anruf: Nachbarstellwerk", SEX1, 330, "anruf", fill=BLAU, size=30, anker="m"),
])

# ===========================================================================================================================
# A2 Fall: Nachbarstellwerk – Herr Nordmann warnt
# ===========================================================================================================================
NOX = 1560
folie([("no1", "Fall · Warnung: Güterzug führerlos")], [
    raum("no1", wand=WAND2, fenster_x=140, name="raum2"),
    pult("no1", bild="plan"),
    hart(pl("Nachbarstellwerk", 70, 30, "no1", fill=BLAU, size=38)),
    ficon("tabler", "phone", 1225, BODEN_Y - 222, 76, "no1", fuell=WEISS),
    ficon("tabler", "train", 400, 400, 120, "no1", fuell=GELB),
    *redet("NO_redet", NOX, BODEN_Y, FHA, "no1", "gleis1"),
    hart(ns(NAME["NO"], NOX, BODEN_Y, "no1", NFARBE["NO"])),
    blase("sprech", 760, 250, "no1", 1000, 240, inhalt=["Ein Güterzug rollt führerlos", "auf deinen Bereich zu!",
                                                       "Die Bremsen greifen nicht."], textsize=34,
          figur=("NO_redet", NOX, BODEN_Y, FHA)),
])

# ===========================================================================================================================
# A3 Fall: Schienenplan – Bautrupp, Funk, Weiche 7, Nebengleis (kein Zusammenstoß, kein Opfer im Bild)
# ===========================================================================================================================
SEX3 = 1660
G1X = [1000, 1075, 1150, 1225, 1300]
EINX = 1180
folie([("gleis1", "Fall · Gleis 1: Bautrupp, 5 Arbeiter"), ("funk", "Fall · Funk: keine Antwort"),
       ("halt", "Fall · Anhalten unmöglich"), ("weiche", "Fall · Weiche 7 auf das Nebengleis?"),
       ("stellt", "Fall · Weiche 7 umgestellt"), ("tot", "Fall · 5 gerettet, 1 Arbeiter tot")], [
    gleisplan("gleis1"),
    hart(pl("Gleis 1", 90, 500, "gleis1", fill=WEISS, size=28)),
    hart(pl("Nebengleis", 880, 676, "gleis1", fill=WEISS, size=28)),
    hart(weichenlage("gleis1", "gerade", bis="stellt")),
    *[silh(i % 5 + 1, x, G1_Y + 6, "gleis1") for i, x in enumerate(G1X)],
    pl("Bautrupp: 5 Arbeiter", 70, 30, beim("gleis1", "Bautrupp"), fill=GELB, size=34),
    *stehend("SE", SEX3, [("gleis1", "sorge")], unten=BODEN_Y, bis="se1"),
    ficon("tabler", "radio", 1470, 650, 90, "funk", fuell=WEISS, bis="halt"),
    *redet("SE_redet", SEX3, BODEN_Y, FHA, "se1", "halt"),
    hart(ns(NAME["SE"], SEX3, BODEN_Y, "se1", NFARBE["SE"], bis="halt")),
    blase("sprech", 700, 220, "se1", 1262, 240, inhalt=["Gleis 1, sofort räumen!", "Bitte melden! Keine Antwort."],
          textsize=34, figur=("SE_redet", SEX3, BODEN_Y, FHA), bis="halt"),
    *stehend("SE", SEX3, [("halt", "angst"), ("stellt", "fest"), ("fuenf", "muede"), ("tot", "zu")], unten=BODEN_Y, bis="se2"),
    ficon("tabler", "train", 230, G1_Y + 4, 150, "halt", fuell=GELB, bis="neben"),
    pl("Anhalten: unmöglich", 70, 110, "halt", fill=HELLROT, size=34),
    pl("Weiche 7", 330, 500, beim("weiche", "Weiche"), fill=GELB, size=30),
    bis_(pfeil(SW[0] + 30, G1_Y + 40, KNICK[0] + 60, G2_Y - 26, beim("weiche", "Nebengleis"), breite=8, kopf=26, farbe=TEXT), "stellt"),
    silh(5, EINX, G2_Y + 6, "einer", bis="tot"),
    pl("1 Arbeiter, nicht erreichbar", EINX, 760, "einer", fill=WEISS, size=28, anker="m", bis="tot"),
    szene(hart(weichenlage("stellt", "abzweig")), "263weiche*", 1.0, 0.0),
    ficon("tabler", "toggle-right", 1470, 780, 90, "stellt", fuell=GELB),
    ficon("tabler", "train", 900, G2_Y + 4, 150, "neben", fuell=GELB, bis="tot"),
    pl("5 Arbeiter unverletzt", 1150, 280, "fuenf", fill=HELLGRUEN, size=32, anker="m", bis="se2"),
    pl("1 Arbeiter kommt ums Leben", EINX, 560, "tot", fill=HELLGRAU, size=28, anker="m"),
    *redet("SE_redet2", SEX3, BODEN_Y, FHA, "se2", "frage"),
    hart(ns(NAME["SE"], SEX3, BODEN_Y, "se2", NFARBE["SE"])),
    blase("sprech", 600, 200, "se2", 1280, 230, inhalt=["Ich hatte nur die Wahl:", "einer oder 5."], textsize=36,
          figur=("SE_redet2", SEX3, BODEN_Y, FHA), bis="frage"),
])

# ===========================================================================================================================
# A4 Fall: die Fragen
# ===========================================================================================================================
folie([("frage", "Fall · Strafbar wegen Totschlags?"), ("frage2", "Fall · 1 Leben opfern, um 5 zu retten?")], [
    raum("frage"),
    pult("frage"),
    *stehend("SE", SEX1, [("frage", "still")], unten=BODEN_Y),
    pl("Totschlag, § 212 StGB?", 70, 30, "frage", fill=PINK, size=38),
    pl("1 Leben opfern, um 5 zu retten?", 70, 110, "frage2", fill=PINK, size=38),
    ficon("tabler", "scale", 430, 860, 180, "frage2", fuell=WEISS),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_263(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=33, zeilenabstand=1.28)
        els += e; y += 16
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_263("sv", [
    "Montag, 6:40 Uhr: Frau Seefeld (Ende 20) hat Dienst im Stellwerk. Herr Nordmann aus dem Nachbarstellwerk meldet, "
    "dass ein Güterzug führerlos auf ihren Bereich zurollt; die Bremsen greifen nicht.",
    "Auf Gleis 1 arbeitet ein Bautrupp mit 5 Arbeitern, über Funk nicht zu erreichen. Anhalten kann Frau Seefeld den Zug "
    "nicht. Sie kann nur Weiche 7 auf das Nebengleis umstellen. Dort steht ein einzelner Arbeiter, auch er ist nicht zu "
    "erreichen. Keinen der Arbeiter kennt sie persönlich.",
    "Sie sieht den Arbeiter und weiß, dass der Zug ihn erfassen wird. Sie stellt die Weiche um. Die 5 Arbeiter bleiben "
    "unverletzt, der Arbeiter auf dem Nebengleis kommt ums Leben.",
], "Hat sich Frau Seefeld wegen Totschlags (§ 212 StGB) strafbar gemacht?")

# ===========================================================================================================================
# C Tatbestand § 212
# ===========================================================================================================================
folie([("tb", f"{PA} › I. Tatbestand"), ("tb212", f"{PA} › I. Tatbestand: § 212 Abs. 1"),
       ("vors", f"{PA} › I. Tatbestand: Vorsatz"), ("rw", f"{PA} › II. Rechtswidrigkeit")], rechts_frei([
    *tafel("tb", "Tatbestand: § 212 Abs. 1 StGB"),
    *okz("einen Menschen getötet", 200, "tb212", "Bold", 34, x=160),
    *okz("Vorsatz: wusste, dass der Zug ihn erfasst", 280, "vors", "Bold", 34, x=160),
    blk(110, 400, 1040, 90, GELB, "rw", [("II. Rechtswidrigkeit: gerechtfertigt?", "ExtraBold", 36, INK)]),
    *requisit([("tb", ("tabler", "train", 120, GELB), "Tatbestand", WEISS),
               ("vors", ("tabler", "eye", 100, WEISS), "Vorsatz", WEISS),
               ("rw", ("tabler", "scale", 100, GELB), "gerechtfertigt?", GELB)]),
    *allein("SE", [("tb", "ruhig"), ("tb212", "still"), ("rw", "skeptisch")]),
]))

# ===========================================================================================================================
# D § 34 StGB (Wortlautkarte)
# ===========================================================================================================================
PN = f"A. Frau Seefeld › II. Rechtswidrigkeit › § 34 StGB"
W34 = ("„Wer in einer gegenwärtigen, nicht anders abwendbaren Gefahr für Leben, Leib, Freiheit, Ehre, Eigentum oder ein "
       "anderes Rechtsgut eine Tat begeht, um die Gefahr von sich oder einem anderen abzuwenden, handelt nicht rechtswidrig, "
       "wenn bei Abwägung der widerstreitenden Interessen, namentlich der betroffenen Rechtsgüter und des Grades der ihnen "
       "drohenden Gefahren, das geschützte Interesse das beeinträchtigte wesentlich überwiegt. Dies gilt jedoch nur, soweit "
       "die Tat ein angemessenes Mittel ist, die Gefahr abzuwenden.“")
w34, w34_y = wortlaut(80, 165, 1100, W34, "§ 34 S. 1, 2 StGB", "p34", marken=[
    ("gegenwärtigen,", beim("lage", "gegenwärtige")), ("Leben,", beim("lage", "Leben")),
    ("nicht anders abwendbaren", beim("mittel", "einzige")), ("das geschützte Interesse", beim("abw", "geschützte")),
    ("wesentlich überwiegt.", beim("abw", "wesentlich"))], size=30)
folie([("p34", f"{PN} · Wortlaut"), ("lage", f"{PN} › Notstandslage (+)"), ("mittel", f"{PN} › einziges Mittel (+)"),
       ("abw", f"{PN} › Interessenabwägung")], rechts_frei([
    *tafel("p34", "Rechtfertigender Notstand"),
    *w34,
    *okz("Notstandslage: gegenwärtige Gefahr für 5 Leben", w34_y + 24, beim("lage", "Leben"), "Bold", 32, x=160),
    *okz("Notstandshandlung: Weiche als einziges Mittel", w34_y + 84, beim("mittel", "einzige"), "Bold", 32, x=160),
    z("Interessenabwägung: wesentlich überwiegend?", 110, w34_y + 150, "abw", "ExtraBold", 34),
    zit("das ganze § 34-Schema im Video zum Berghütten-Fall", 110, w34_y + 210, "v189"),
    *requisit([("p34", ("tabler", "alert-triangle", 100, GELB), "Notstand?", GELB),
               ("lage", ("tabler", "heartbeat", 100, HELLROT), "Gefahr für 5 Leben", HELLROT),
               ("mittel", ("tabler", "git-fork", 100, WEISS), "nur die Weiche", WEISS),
               ("abw", ("tabler", "scale", 100, WEISS), "wesentlich überwiegt?", WEISS)]),
    *allein("SE", [("p34", "ruhig"), ("lage", "sorge"), ("abw", "skeptisch")]),
]))
assert w34_y + 250 <= 890, w34_y

# ===========================================================================================================================
# E1 Leben gegen Leben
# ===========================================================================================================================
PI = f"{PN} › Interessenabwägung"
folie([("zahl", f"{PI}: Leben gegen Leben"), ("nein34", f"{PI} › Leben nicht abwägbar (h. M.)")], rechts_frei([
    *tafel("zahl", "Leben gegen Leben"),
    blk(110, 190, 500, 130, HELLGRUEN, "zahl", [("geschützt:", "ExtraBold", 32, INK), ("Leben von 5 Arbeitern", "Bold", 32, INK)]),
    blk(650, 190, 500, 130, HELLROT, beim("zahl", "eines"), [("beeinträchtigt:", "ExtraBold", 32, INK),
                                                          ("Leben von 1 Arbeiter", "Bold", 32, INK)]),
    z("überwiegt das wesentlich?", 110, 370, beim("zahl", "Überwiegt"), "Bold", 34),
    *neinz("herrschende Meinung: nein", 450, "nein34", "ExtraBold", 36, x=160),
    z("Leben ist nicht abwägbar –", 160, 530, "nicht", "Bold", 34),
    z("auch nicht nach der Zahl", 160, 585, beim("nicht", "auch"), "Bold", 34),
    *requisit([("zahl", ("tabler", "scale", 110, WEISS), "5 gegen 1?", WEISS),
               ("nein34", ("tabler", "ban", 100, HELLROT), "nicht abwägbar", HELLROT)]),
    *allein("SE", [("zahl", "ernst"), ("nein34", "sorge"), ("nicht", "still")]),
]))

# ===========================================================================================================================
# E2 BVerfGE 115, 118 (Zitatkarte Rn. 85; Rn. 124) → rechtswidrig
# ===========================================================================================================================
wq, wq_y = wortlaut(80, 230, 1100, "„Jedes menschliche Leben ist als solches gleich wertvoll.“",
                    "BVerfG, Urt. v. 15.2.2006 – 1 BvR 357/05, Rn. 85", "gleich", size=32)
folie([("bverfg", f"{PI} › BVerfGE 115, 118"), ("objekt", f"{PI} › Tötung als bloßes Mittel"),
       ("staat", f"{PI} › übertragen auf § 34 StGB"), ("rw_erg", f"{PN} (−) › rechtswidrig")], rechts_frei([
    *tafel("bverfg", "BVerfGE 115, 118 (Luftsicherheit)"),
    z("Urteil zum Luftsicherheitsgesetz", 110, 170, "bverfg", "Bold", 34),
    *wq,
    z("Staat tötet Unbeteiligte, um andere zu retten:", 110, wq_y + 20, "objekt", "Bold", 32),
    z("bloßes Mittel – missachtet ihre Würde", 110, wq_y + 66, beim("objekt", "bloßes"), "Bold", 32),
    zit("Rn. 124; Art. 1 Abs. 1 GG: „Die Würde des Menschen ist unantastbar.“", 110, wq_y + 118, "wuerde"),
    z("Das Gericht sprach über den Staat.", 110, wq_y + 180, "staat", size=32),
    z("Strafrechtslehre: gilt auch für § 34 StGB", 110, wq_y + 226, "lehre", "Bold", 32),
    blk(110, wq_y + 290, 1040, 80, HELLROT, "rw_erg", [("§ 34 (−): Frau Seefeld handelt rechtswidrig", "ExtraBold", 34, INK)]),
    zit("mehr im Video „Luftsicherheitsgesetz: Darf der Staat ein Flugzeug abschießen?“", 110, wq_y + 390, "v013"),
    *requisit([("bverfg", ("tabler", "building-bank", 100, WEISS), "BVerfGE 115, 118", WEISS),
               ("objekt", ("tabler", "user-x", 100, HELLROT), "bloßes Mittel", HELLROT),
               ("wuerde", ("tabler", "shield", 100, GELB), "Art. 1 Abs. 1 GG", GELB),
               ("staat", ("tabler", "book", 100, WEISS), "Strafrecht: § 34", WEISS),
               ("rw_erg", ("tabler", "ban", 100, HELLROT), "rechtswidrig", HELLROT)]),
    *allein("SE", [("bverfg", "ruhig"), ("objekt", "ernst"), ("rw_erg", "still")]),
]))
assert wq_y + 430 <= 900, wq_y

# ===========================================================================================================================
# F § 35 StGB (Wortlautkarte Abs. 1 S. 1)
# ===========================================================================================================================
PS_ = "A. Frau Seefeld › III. Schuld › § 35 StGB"
W35 = ("„Wer in einer gegenwärtigen, nicht anders abwendbaren Gefahr für Leben, Leib oder Freiheit eine rechtswidrige Tat "
       "begeht, um die Gefahr von sich, einem Angehörigen oder einer anderen ihm nahestehenden Person abzuwenden, handelt "
       "ohne Schuld.“")
w35, w35_y = wortlaut(80, 165, 1100, W35, "§ 35 Abs. 1 S. 1 StGB", "p35", marken=[
    ("handelt ohne Schuld.", beim("p35", "entschuldigt")), ("gegenwärtigen,", beim("p35", "gegenwärtigen")),
    ("Leben, Leib oder Freiheit", beim("p35", "Leben")), ("von sich,", beim("kreis", "sich")),
    ("einem Angehörigen", beim("kreis", "Angehörigen")), ("nahestehenden", beim("kreis", "nahestehenden"))], size=32)
folie([("p35", f"{PS_} · Wortlaut"), ("kreis", f"{PS_} › Personenkreis"), ("fremd", f"{PS_} › Personenkreis (−)"),
       ("nein35", f"{PS_} (−)")], rechts_frei([
    *tafel("p35", "Entschuldigender Notstand"),
    *w35,
    *neinz("5 Arbeiter: Frau Seefeld kennt sie nicht", w35_y + 30, "fremd", "Bold", 34, x=160),
    blk(110, w35_y + 120, 1040, 80, HELLROT, "nein35", [("§ 35 StGB (−)", "ExtraBold", 36, INK)]),
    *requisit([("p35", ("tabler", "heartbeat", 100, HELLROT), "Gefahr für Leben", HELLROT),
               ("kreis", ("tabler", "users", 110, WEISS), "nahestehende Personen", WEISS),
               ("fremd", ("tabler", "users", 110, HELLROT), "keine Nahestehenden", HELLROT)]),
    *allein("SE", [("p35", "ruhig"), ("kreis", "skeptisch"), ("fremd", "sorge")]),
]))
assert w35_y + 220 <= 890, w35_y

# ===========================================================================================================================
# G Übergesetzlicher entschuldigender Notstand: Herkunft (ohne Bilder zu den Ärzteverfahren, ohne Figur)
# ===========================================================================================================================
PU_ = "A. Frau Seefeld › III. Schuld › übergesetzlicher entschuldigender Notstand"
folie([("ueber", PU_), ("hist", f"{PU_} › Herkunft"), ("offen", f"{PU_} › BVerfG lässt offen")], rechts_frei([
    *tafel("ueber", "Übergesetzlicher Notstand", size=46),
    z("übergesetzlicher entschuldigender Notstand", 110, 175, "ueber", "ExtraBold", 34),
    *neinz("in keinem Gesetz geregelt", 245, "kein_g", "Bold", 34, x=160),
    z("bedeutsam nach dem Krieg: Strafverfahren gegen", 110, 330, "hist", "Bold", 32),
    z("Ärzte, die an NS-Krankenmorden mitgewirkt hatten", 110, 376, beim("hist", "Ärzte"), "Bold", 32),
    z("einzelne Patienten von den Listen gestrichen", 110, 446, "listen", size=32),
    zit("Oberster Gerichtshof für die Britische Zone, OGHSt 1, 321", 110, 500, beim("listen", "gestrichen")),
    blk(110, 570, 1040, 130, GELB, "offen", [("BVerfGE 115, 118, Rn. 130: verweist darauf,", "ExtraBold", 32, INK),
                                             ("lässt die Strafbarkeit offen", "ExtraBold", 32, INK)]),
    *requisit([("ueber", ("tabler", "help", 100, WEISS), "ungeschrieben", WEISS),
               ("kein_g", ("tabler", "book-off", 100, WEISS), "kein Gesetz", WEISS),
               ("hist", ("tabler", "archive", 100, WEISS), "Nachkriegsverfahren", WEISS),
               ("offen", ("tabler", "building-bank", 100, GELB), "offengelassen", GELB)], px=FX),
]))

# ===========================================================================================================================
# H Voraussetzungen (nach den Befürwortern)
# ===========================================================================================================================
folie([("vor", f"{PU_} › Voraussetzungen")], rechts_frei([
    *tafel("vor", "Voraussetzungen"),
    z("nach seinen Befürwortern:", 110, 185, "vor", "Bold", 34),
    blk(110, 250, 1040, 90, WEISS, "v1", [("1. ausweglose Lage: Gefahr für Leben", "ExtraBold", 34, INK)]),
    blk(110, 370, 1040, 130, WEISS, "v2", [("2. Tat als einziges Mittel, um ein", "ExtraBold", 34, INK),
                                           ("größeres Unheil abzuwenden", "ExtraBold", 34, INK)]),
    blk(110, 530, 1040, 130, WEISS, "v3", [("3. gewissenhafte Prüfung,", "ExtraBold", 34, INK),
                                           ("Handeln, um zu retten", "ExtraBold", 34, INK)]),
    *requisit([("vor", ("tabler", "list-details", 100, WEISS), "Voraussetzungen", WEISS),
               ("v1", ("tabler", "alert-triangle", 100, GELB), "ausweglos", GELB),
               ("v2", ("tabler", "git-fork", 100, WEISS), "einziges Mittel", WEISS),
               ("v3", ("tabler", "heart-handshake", 100, HELLGRUEN), "Rettungswille", HELLGRUEN)]),
    *allein("SE", [("vor", "ruhig"), ("v1", "sorge"), ("v3", "still")]),
]))

# ===========================================================================================================================
# I Ansichten: Entschuldigungsgrund / persönlicher Strafausschließungsgrund
# ===========================================================================================================================
folie([("ans", f"{PU_} › Streit: Wie wirkt er?"), ("a1", f"{PU_} › 1. Entschuldigungsgrund"),
       ("a2", f"{PU_} › 2. persönlicher Strafausschließungsgrund")], rechts_frei([
    *tafel("ans", "Streit: Wie wirkt er?"),
    blk(110, 190, 1040, 140, HELLGRUEN, "a1", [("1. Entschuldigungsgrund (wohl h. L.)", "ExtraBold", 34, INK),
                                               ("Tat rechtswidrig, Schuld entfällt", "Bold", 32, INK)]),
    blk(110, 380, 1040, 140, BLAU, "a2", [("2. persönlicher Strafausschließungsgrund", "ExtraBold", 34, INK),
                                          ("OGH BrZ in einem Ärzteverfahren", "Bold", 32, INK)]),
    z("Unrecht und Schuld bleiben, nur die Strafe entfällt", 110, 560, "a2b", "Bold", 32),
    zit("OGHSt 1, 321", 110, 615, "a2b"),
    *requisit([("ans", ("tabler", "help", 100, WEISS), "Rechtsnatur?", WEISS),
               ("a1", ("tabler", "shield-check", 100, HELLGRUEN), "ohne Schuld", HELLGRUEN),
               ("a2", ("tabler", "scale", 100, BLAU), "keine Strafe", BLAU)]),
    *allein("SE", [("ans", "skeptisch"), ("a1", "ruhig"), ("a2", "ernst")]),
]))

# ===========================================================================================================================
# J Gefahrengemeinschaft oder Umlenken (Weichenstellerfall)
# ===========================================================================================================================
folie([("gg", f"{PU_} › Gefahrengemeinschaft"), ("weichen", f"{PU_} › Weichenstellerfall"),
       ("a3", f"{PU_} › 3. Gegenansicht: keine Entschuldigung"), ("a4", f"{PU_} › andere: auch beim Umlenken")], rechts_frei([
    *tafel("gg", "Gefahrengemeinschaft oder Umlenken?"),
    z("Gefahrengemeinschaft: vor allem hier anerkannt", 110, 180, "gg", "ExtraBold", 34),
    z("alle schon in derselben Gefahr, Täter rettet einige", 160, 236, "gg2", size=32),
    zit("so in den Ärztefällen", 160, 284, beim("gg2", "Ärztefällen")),
    z("Weichenstellerfall:", 110, 350, "weichen", "ExtraBold", 34),
    z("Arbeiter auf dem Nebengleis war nicht in Gefahr", 160, 406, "unbet", size=32),
    z("die Gefahr wird erst auf ihn umgelenkt", 160, 456, beim("unbet", "lenkt"), size=32),
    blk(110, 530, 1040, 130, HELLROT, "a3", [("3. Gegenansicht: keine Entschuldigung,", "ExtraBold", 32, INK),
                                             ("wer einen Unbeteiligten opfert", "ExtraBold", 32, INK)]),
    blk(110, 690, 1040, 90, HELLGRUEN, "a4", [("andere: entschuldigt auch dann, wenn ausweglos", "Bold", 32, INK)]),
    *requisit([("gg", ("tabler", "users-group", 110, WEISS), "alle in Gefahr", WEISS),
               ("weichen", ("tabler", "git-fork", 100, GELB), "Umlenken", GELB),
               ("a3", ("tabler", "user-x", 100, HELLROT), "strafbar", HELLROT),
               ("a4", ("tabler", "help", 100, HELLGRUEN), "umstritten", HELLGRUEN)]),
    *allein("SE", [("gg", "ruhig"), ("weichen", "ernst"), ("a3", "sorge"), ("a4", "skeptisch")]),
]))

# ===========================================================================================================================
# K Ergebnis je Ansicht
# ===========================================================================================================================
PE = "Ergebnis je Ansicht"
folie([("lsg", PE), ("l1", f"{PE} › auch beim Umlenken: straflos"), ("l2", f"{PE} › nur Gefahrengemeinschaft: § 212"),
       ("l3", f"{PE} › Strafe: § 213"), ("l4", f"{PE} › Begründung entscheidet")], rechts_frei([
    *tafel("lsg", "Ergebnis je Ansicht"),
    blk(110, 190, 1040, 140, HELLGRUEN, "l1", [("Notstand auch beim Umlenken: straflos", "ExtraBold", 34, INK),
                                               ("als Entschuldigung oder Strafausschließung", "Bold", 32, INK)]),
    blk(110, 380, 1040, 90, HELLROT, "l2", [("nur Gefahrengemeinschaft: Totschlag, § 212", "ExtraBold", 34, INK)]),
    z("Strafe: ggf. minder schwerer Fall, § 213 StGB", 160, 510, "l3", "Bold", 32),
    z("vertretbar ist beides –", 110, 600, "l4", "ExtraBold", 36),
    z("entscheidend ist die Begründung", 110, 656, beim("l4", "entscheidend"), "ExtraBold", 36),
    *requisit([("lsg", ("tabler", "scale", 100, WEISS), "Ergebnis?", WEISS),
               ("l1", ("tabler", "shield-check", 100, HELLGRUEN), "straflos", HELLGRUEN),
               ("l2", ("tabler", "ban", 100, HELLROT), "§ 212", HELLROT),
               ("l3", ("tabler", "scale", 100, WEISS), "§ 213", WEISS),
               ("l4", ("tabler", "file-text", 100, GELB), "Begründung", GELB)]),
    *allein("SE", [("lsg", "ruhig"), ("l1", "ruhig"), ("l2", "sorge"), ("l4", "ernst")]),
]))

# ===========================================================================================================================
# L Stellwerk: Frau Seefeld (Blase)
# ===========================================================================================================================
folie([("se3", "Ergebnis · Frau Seefeld")], [
    raum("se3"),
    pult("se3"),
    hart(pl("Stellwerk", 70, 30, "se3", fill=GELB, size=38)),
    *redet("SE_redet", SEX1, BODEN_Y, FHA, "se3", "tipp"),
    hart(ns(NAME["SE"], SEX1, BODEN_Y, "se3", NFARBE["SE"])),
    blase("sprech", 640, 200, "se3", 1000, 250, inhalt=["Dann hängt alles", "an diesem Streit."], textsize=38,
          figur=("SE_redet", SEX1, BODEN_Y, FHA), bis="tipp"),
])

# ===========================================================================================================================
# M Klausurtipp (Lexi): Reihenfolge und Folge der Rechtswidrigkeit
# ===========================================================================================================================
els_k = [*tafel("tipp", "Klausurtipp: Reihenfolge einhalten", fill=HELL, size=44), warnung_i(150, 215, "tipp", gr=26),
         z("Halte die Reihenfolge ein:", 200, 190, "tipp", "Bold", 34),
         blk(130, 270, 1020, 90, GELB, "k1", [("II. Rechtswidrigkeit: § 34 (−), Leben gegen Leben", "ExtraBold", 32, INK)]),
         blk(130, 385, 1020, 90, BLAU, "k2", [("III. Schuld: § 35 (−), Personenkreis", "ExtraBold", 32, INK)]),
         blk(130, 500, 1020, 90, HELLGRUEN, "k3", [("dann: übergesetzlicher Notstand (Schuld)", "ExtraBold", 32, INK)]),
         blk(130, 625, 1020, 80, HELLROT, "k4", [("Folge: Die Tat bleibt rechtswidrig.", "ExtraBold", 34, INK)]),
         z("Notwehr gegen die Tat möglich", 160, 730, "k5", "Bold", 32),
         z("Helfer: Teilnahme strafbar möglich, §§ 26, 27", 160, 780, beim("k5", "wer"), "Bold", 32),
         *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
         ns("Lexi", FX, FB, "tipp", GELB, d=0.2)]
folie([("tipp", "Klausurtipp · Reihenfolge"), ("k1", "Klausurtipp › § 34 in der Rechtswidrigkeit"),
       ("k2", "Klausurtipp › § 35 in der Schuld"), ("k3", "Klausurtipp › übergesetzlicher Notstand in der Schuld"),
       ("k4", "Klausurtipp › Tat bleibt rechtswidrig")], els_k)

# ===========================================================================================================================
# N Klausurschema (Aufbau Punkt für Punkt)
# ===========================================================================================================================
REIHEN = [("s1", "I. Tatbestand, § 212 Abs. 1 StGB", 130),
          ("s2", "II. Rechtswidrigkeit: § 34 (−), Leben nicht abwägbar", 130),
          ("s3", "III. Schuld: 1. § 35 (−), Personenkreis", 130),
          ("s4", "2. übergesetzlicher entschuldigender Notstand", None),
          ("s5", "Voraussetzungen; Streit beim Umlenken", None),
          ("s6", "IV. Ergebnis je nach Ansicht", 130)]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Schema: Totschlag und übergesetzlicher Notstand"), 110, 90, "sch", 46)]
y = 220
EIN = 130 + int(F("ExtraBold", 40).getlength("III. Schuld: "))     # „2.“ steht unter „1.“
for c, text, xx in REIHEN:
    xx = xx or (EIN if text.startswith("2.") else EIN + 44)
    els_sch.append(z(text, xx, y, c, "ExtraBold", 40, rechts=1800))
    y += 105
assert y <= 960, y
folie([("sch", "Klausurschema · Totschlag, übergesetzlicher Notstand"), ("s1", "Klausurschema › I. Tatbestand"),
       ("s2", "Klausurschema › II. Rechtswidrigkeit"), ("s3", "Klausurschema › III. Schuld: § 35"),
       ("s4", "Klausurschema › III. Schuld: übergesetzlicher Notstand"), ("s6", "Klausurschema › IV. Ergebnis")], els_sch)

# ===========================================================================================================================
# O Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Leben gegen Leben ", 0), ("rechtfertigt nicht,", "a")],
                 [("auch nicht 1 gegen 5.", 0)]], 750, 280, 42, "merke", {"a": beim("merke", "rechtfertigt")}),
    *markertext([[("§ 35: nur Gefahr für dich", 0)], [("und ", 0), ("Nahestehende.", "b")]], 750, 450, 40, "m2",
                {"b": beim("m2", "nahestehende")}),
    *markertext([[("Übergesetzlicher Notstand: ", 0)], [("allenfalls Entschuldigung", "c"), (" –", 0)],
                 [("beim Umlenken umstritten.", 0)]], 750, 610, 40, "m3", {"c": beim("m3", "allenfalls")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
