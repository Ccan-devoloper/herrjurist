"""Folge 186 · Einstellung § 170 II StPO: Beschwerde und Klageerzwingung – Serienstandard Open Peeps (Katzenkönig).
Beispielfall: Am Di, 13.1.2026, operiert Augenarzt Dr. Wallner Frau Rautenberg am rechten Auge (Behandlung nur als Icon,
kein Blut); danach sieht sie auf diesem Auge nichts mehr. Sie zeigt ihn wegen Körperverletzung an und verlangt seine
Bestrafung. Vernehmung als Beschuldigter, Gutachten ohne Behandlungsfehler, unterschriebener Aufklärungsbogen. Im Juni will
Referendarin Hölscher einstellen und die Akte weglegen (Mitteilungen fehlen). Fortsetzung: Bescheid zugestellt Do, 2.7.2026,
Beschwerde Mo, 13.7.; Bescheid der Generalstaatsanwaltschaft zugestellt Mi, 5.8.; Antragsfrist bis Mo, 7.9.2026.
Szenen laut ../SZENENPLAN.md: A1 Augenarztpraxis, A2 zu Hause, A3 Vernehmung, A4 Staatsanwaltschaft, B Sachverhalt,
C § 170 (Wortlautkarte), D Einstellungsverfügung, E § 170 Abs. 2 S. 2 (Wortlautkarte), F § 171 (Wortlautkarte), F2 Entwurf
korrigiert, G § 172 Abs. 1 (Wortlautkarte), H1 § 172 Abs. 2 S. 1, Abs. 4 (Wortlautkarte), H2 § 172 Abs. 3 (Wortlautkarte),
H3 Ausschluss § 172 Abs. 2 S. 3 (Wortlautkarte), I §§ 174, 175, J1 Kalender Juli 2026, J2 Kalender September 2026,
J3 Kanzlei, K Prüfschema, L Klausurtipp (Lexi), M Merksatz (Lexi).
Handlungsgeräusche: Akte auf dem Schreibtisch (A4), Briefumschlag bei der Zustellung (J1); ../geraeusche_herkunft.json.
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz
als eigene Kopie aus Folge 180 (gemeinsame Dateien unverändert); neu: wortlaut_auto() mit Zeilenumbruch, praxis(), wohnung(),
kalender für beliebige Monate. Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut nach gesetze-im-internet.de
(Abruf 04.10.2026, amtliche Schreibung „Anlaß“, „Abschluß“, „muß“)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave
import datetime as _dt

bausteine.FIGORDNER = "op_186/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_186/" in n:
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
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 04.10.2026), als Zitat mit Normangabe; der
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
WAND = (232, 240, 238, 255)
WAND2 = (242, 232, 214, 255)
GRAUW = (205, 205, 200, 255)


def _flaeche(w, h, zeichne):
    s = 2
    im = Image.new("RGBA", (w * s, h * s))
    zeichne(ImageDraw.Draw(im), s)
    return im.resize((w, h), Image.LANCZOS)


def boden(c, x0=60, x1=1860):
    return hart(linienzug([(x0, BODEN_Y), (x1, BODEN_Y)], c, breite=7, farbe=INK))


def praxis(c):
    """Augenarztpraxis (Grundform): helle Wand, Sehtafel mit Buchstabenreihen links, Schrank rechts; ohne Logo."""
    def zz(dr, s):
        dr.rectangle((0, 0, 1800 * s, 575 * s), fill=WAND)
        # Sehtafel
        dr.rounded_rectangle((90 * s, 90 * s, 330 * s, 420 * s), 10 * s, fill=(255, 255, 255, 255), outline=INK, width=5 * s)
        reihen = [("E", 70), ("F P", 48), ("T O Z", 36), ("L P E D", 28), ("P E C F D", 22)]
        y = 110
        for t, g in reihen:
            f = F("ExtraBold", g * s)
            wd = f.getlength(t)
            dr.text(((210 * s - wd / 2), y * s), t, font=f, fill=INK)
            y += g + 16
        # Schrank
        dr.rounded_rectangle((1500 * s, 230 * s, 1760 * s, 575 * s), 8 * s, fill=(226, 226, 222, 255), outline=INK, width=5 * s)
        dr.line((1630 * s, 230 * s, 1630 * s, 575 * s), fill=INK, width=4 * s)
        for xg in (1610, 1650):
            dr.line((xg * s, 380 * s, xg * s, 430 * s), fill=INK, width=5 * s)
        dr.line((0, 575 * s - 2, 1800 * s, 575 * s - 2), fill=INK, width=4 * s)
    return hart(El(_flaeche(1800, 575, zz), 60, BODEN_Y - 575, c, "cut", 0.0, None, name="praxis"))


def wohnung(c):
    """Wohnzimmer (Grundform): warme Wand, Fenster, Stehlampe-Ersatz als Regal; Tisch kommt separat."""
    def zz(dr, s):
        dr.rectangle((0, 0, 1800 * s, 575 * s), fill=WAND2)
        dr.rounded_rectangle((160 * s, 90 * s, 520 * s, 380 * s), 10 * s, fill=(214, 232, 250, 255), outline=INK, width=5 * s)
        dr.line((340 * s, 90 * s, 340 * s, 380 * s), fill=INK, width=4 * s)
        dr.line((160 * s, 235 * s, 520 * s, 235 * s), fill=INK, width=4 * s)
        # Bilderrahmen
        dr.rounded_rectangle((1560 * s, 120 * s, 1740 * s, 260 * s), 8 * s, fill=(143, 214, 148, 255), outline=INK, width=5 * s)
        dr.line((0, 575 * s - 2, 1800 * s, 575 * s - 2), fill=INK, width=4 * s)
    return hart(El(_flaeche(1800, 575, zz), 60, BODEN_Y - 575, c, "cut", 0.0, None, name="wohnung"))


def schreibtisch(c, x0, x1, h=170):
    w = x1 - x0
    def zz(dr, s):
        dr.rounded_rectangle((3 * s, 0, (w - 3) * s, 28 * s), 6 * s, fill=HOLZ, outline=INK, width=5 * s)
        for xl in (30, w - 60):
            dr.rectangle((xl * s, 28 * s, (xl + 26) * s, (h - 3) * s), fill=HOLZ, outline=INK, width=4 * s)
    return hart(El(_flaeche(w, h, zz), x0, BODEN_Y - h, c, "cut", 0.0, None, name="schreibtisch"))


def fenster(c, x0, y0, w=300, h=260):
    def zz(dr, s):
        dr.rounded_rectangle((3 * s, 3 * s, (w - 3) * s, (h - 3) * s), 10 * s, fill=(214, 232, 250, 255), outline=INK, width=5 * s)
        dr.line((w // 2 * s, 3 * s, w // 2 * s, (h - 3) * s), fill=INK, width=4 * s)
        dr.line((3 * s, h // 2 * s, (w - 3) * s, h // 2 * s), fill=INK, width=4 * s)
    return hart(El(_flaeche(w, h, zz), x0, y0, c, "cut", 0.0, None, name="fenster"))


X1, X2 = 1395, 1730                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"RA": "Frau Rautenberg", "WA": "Dr. Wallner", "HO": "Referendarin Hölscher", "AN": "Rechtsanwältin"}
NFARBE = {"RA": ORANGE, "WA": BLAU, "HO": TUERKIS, "AN": HELLGRAU}


def stehend(k, x, folge, unten=930, hoehe=480, bis=None):
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


def zwei(folge_l, folge_r, links="HO", rechts="RA"):
    """Zwei Figuren rechts neben der Tafel (blicken nach links zur Tafel)."""
    return [*stehend(links, X1, folge_l), *stehend(rechts, X2, folge_r)]


def allein(k, folge):
    return stehend(k, FX, folge)


# ===========================================================================================================================
# A1 Fall: Augenarztpraxis – Operation am rechten Auge (Behandlung nur als Icon)
# ===========================================================================================================================
WAX, RAX = 820, 1300                         # Dr. Wallner (blickt nach rechts), Frau Rautenberg (blickt nach links)
folie([(NULL, "Fall · In der Augenarztpraxis"), ("op", "Fall · Operation am rechten Auge"),
       ("danach", "Fall · nach der Operation")], [
    praxis(NULL),
    boden(NULL),
    hart(pl("Augenarztpraxis", 70, 30, NULL, fill=BLAU, size=38)),
    hart(pl("Dienstag, 13.1.2026", 420, 30, NULL, fill=WEISS, size=34)),
    *fig("WA", WAX, BODEN_Y, FHA, [(NULL, "ruhig_r"), ("op", "ernst_r"), ("danach", "sorge_r")], erst="cut"),
    hart(ns(NAME["WA"], WAX, BODEN_Y, NULL, NFARBE["WA"])),
    *fig("RA", RAX, BODEN_Y, FHA, [(NULL, "ruhig"), ("op", "ruhig"), ("danach", "sorge")], erst="cut"),
    hart(ns(NAME["RA"], RAX, BODEN_Y, NULL, NFARBE["RA"])),
    ficon("tabler", "eye", 1060, 560, 150, beim("op", "operiert"), fuell=WEISS, bis="danach"),
    pl("Operation am rechten Auge", 1060, 330, beim("op", "operiert"), fill=WEISS, size=32, anker="m", bis="danach"),
    ficon("tabler", "eye-off", 1060, 560, 150, "danach", fuell=HELLROT),
    pl("danach: rechts kein Sehvermögen", 1060, 330, beim("danach", "sieht"), fill=HELLROT, size=32, anker="m"),
])

# ===========================================================================================================================
# A2 Fall: zu Hause – Vorwurf und Strafanzeige
# ===========================================================================================================================
RA2 = 1250
folie([("ra1", "Fall · der Vorwurf"), ("anz", "Fall · Strafanzeige wegen Körperverletzung")], [
    wohnung("ra1"),
    boden("ra1"),
    hart(pl("Zu Hause", 70, 30, "ra1", fill=ORANGE, size=38)),
    schreibtisch("ra1", 640, 1080, h=150),
    *redet("RA_redet", RA2, BODEN_Y, FHA, "ra1", "anz"),
    hart(ns(NAME["RA"], RA2, BODEN_Y, "ra1", NFARBE["RA"])),
    blase("sprech", 760, 240, "ra1", 860, 235, inhalt=["Über dieses Risiko hat mich", "niemand aufgeklärt.",
                                                     "Ich zeige den Arzt an."], textsize=36,
          figur=("RA_redet", RA2, BODEN_Y, FHA), bis="anz"),
    *fig("RA", RA2, BODEN_Y, FHA, [("anz", "fest")], erst="cut"),
    ficon("tabler", "file-text", 860, BODEN_Y - 150, 120, "anz", fuell=WEISS),
    pl("Strafanzeige wegen Körperverletzung", 70, 110, "anz", fill=GELB, size=34),
    pl("Antrag: „Er soll bestraft werden.“", 70, 190, beim("anz", "verlangt"), fill=WEISS, size=34),
])

# ===========================================================================================================================
# A3 Fall: Vernehmung als Beschuldigter, Gutachten, Aufklärungsbogen
# ===========================================================================================================================
WA3 = 1350
folie([("verm", "Fall · Ermittlungen"), ("wa1", "Fall · Vernehmung als Beschuldigter"), ("gut", "Fall · das Gutachten"),
       ("bogen", "Fall · der Aufklärungsbogen")], [
    boden("verm"),
    fenster("verm", 1500, 300, w=260, h=220),
    schreibtisch("verm", 560, 1120),
    hart(pl("Staatsanwaltschaft · Vernehmung", 70, 30, "verm", fill=LILA, size=38)),
    pl("als Beschuldigter vernommen", 70, 110, beim("verm", "Beschuldigter"), fill=WEISS, size=34),
    *stehend("WA", WA3, [("verm", "ernst")], unten=BODEN_Y, bis="wa1"),
    *redet("WA_redet", WA3, BODEN_Y, FHA, "wa1", "gut"),
    hart(ns(NAME["WA"], WA3, BODEN_Y, "wa1", NFARBE["WA"])),
    blase("sprech", 820, 230, "wa1", 900, 330, inhalt=["Ich habe sie vor der Operation", "über die Risiken aufgeklärt."],
          textsize=36, figur=("WA_redet", WA3, BODEN_Y, FHA), bis="gut"),
    *fig("WA", WA3, BODEN_Y, FHA, [("gut", "ruhig")], erst="cut"),
    ficon("tabler", "file-certificate", 720, BODEN_Y - 170, 130, "gut", fuell=HELLGRUEN),
    pl("Gutachten: kein Behandlungsfehler", 70, 190, "gut", fill=HELLGRUEN, size=34),
    ficon("tabler", "writing-sign", 960, BODEN_Y - 170, 130, "bogen", fuell=WEISS),
    pl("Aufklärungsbogen unterschrieben: Risiko genannt", 70, 270, beim("bogen", "unterschriebene"), fill=WEISS, size=34),
])

# ===========================================================================================================================
# A4 Fall: Staatsanwaltschaft – der Entwurf von Referendarin Hölscher
# ===========================================================================================================================
HOX = 1520
folie([("akte", "Fall · Juni: bei der Staatsanwaltschaft"), ("ho1", "Fall · der Entwurf"),
       ("frage", "Fall · reicht das?"), ("frage2", "Fall · die Fragen")], [
    boden("akte"),
    fenster("akte", 1100, 380),
    schreibtisch("akte", 640, 1220),
    hart(pl("Staatsanwaltschaft", 70, 30, "akte", fill=LILA, size=38)),
    pl("Juni 2026", 470, 30, beim("akte", "Juni"), fill=WEISS, size=34),
    szene(ficon("tabler", "folders", 860, BODEN_Y - 170, 150, beim("akte", "Akte"), fuell=GELB), "186akte*", 1.0, 0.0),
    pl("Akte Wallner", 860, 560, beim("akte", "Akte"), fill=WEISS, size=28, anker="m"),
    *stehend("HO", HOX, [("akte", "froh")], unten=BODEN_Y, bis="ho1"),
    *redet("HO_redet", HOX, BODEN_Y, FHA, "ho1", "frage"),
    hart(ns(NAME["HO"], HOX, BODEN_Y, "ho1", NFARBE["HO"], bis="frage")),
    blase("sprech", 700, 220, "ho1", 1150, 225, inhalt=["Kein hinreichender Tatverdacht.", "Ich stelle ein und",
                                                       "lege die Akte weg."], textsize=34,
          figur=("HO_redet", HOX, BODEN_Y, FHA), bis="frage"),
    *fig("HO", HOX, BODEN_Y, FHA, [("frage", "schreck"), ("frage2", "skeptisch")], erst="cut"),
    hart(ns(NAME["HO"], HOX, BODEN_Y, "frage", NFARBE["HO"])),
    pl("Reicht das?", 70, 110, "frage", fill=HELLROT, size=36),
    pl("Was gehört in die Einstellungsverfügung?", 70, 190, "frage2", fill=PINK, size=36),
    pl("Was kann Frau Rautenberg dagegen tun?", 70, 270, beim("frage2", "was", nr=2), fill=PINK, size=36),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_186(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=34, zeilenabstand=1.30)
        els += e; y += 18
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_186("sv", [
    "Am Dienstag, 13. Januar 2026, operiert Augenarzt Dr. Wallner Frau Rautenberg am rechten Auge. Danach sieht sie auf "
    "diesem Auge nichts mehr. Sie meint, über dieses Risiko nicht aufgeklärt worden zu sein, erstattet Strafanzeige wegen "
    "Körperverletzung und verlangt, dass er bestraft wird.",
    "Dr. Wallner wird als Beschuldigter vernommen und erklärt, er habe sie über die Risiken aufgeklärt. Ein Gutachten findet "
    "keinen Behandlungsfehler; der von Frau Rautenberg unterschriebene Aufklärungsbogen nennt das Risiko.",
    "Im Juni 2026 entwirft Referendarin Hölscher bei der Staatsanwaltschaft die Einstellungsverfügung. Ihr Plan: einstellen "
    "und die Akte weglegen.",
], "Was gehört in die Einstellungsverfügung – und was kann Frau Rautenberg dagegen tun?")

# ===========================================================================================================================
# C Wann: § 170 Abs. 1, Abs. 2 S. 1 StPO (Wortlaut); Gründe; Verweis 060/180
# ===========================================================================================================================
PW = "Einstellung"
W170 = ("„(1) Bieten die Ermittlungen genügenden Anlaß zur Erhebung der öffentlichen Klage, so erhebt die "
        "Staatsanwaltschaft sie durch Einreichung einer Anklageschrift bei dem zuständigen Gericht. "
        "(2) Andernfalls stellt die Staatsanwaltschaft das Verfahren ein. …“")
w170, w170_y = wortlaut(80, 165, 1100, W170, "§ 170 Abs. 1, Abs. 2 S. 1 StPO", "p170", marken=[
    ("genügenden Anlaß", beim("p170", "genügenden")), ("Andernfalls", beim("p170b", "Andernfalls")),
    ("das Verfahren ein", beim("p170b", "Verfahren"))], size=30)
folie([("p170", f"{PW} › § 170 Abs. 1 StPO: Anklage"), ("p170b", f"{PW} › § 170 Abs. 2 S. 1 StPO: andernfalls Einstellung"),
       (beim("tats", "tatsächlichen"), f"{PW} › kein hinreichender Tatverdacht: tatsächlich"), ("recht", f"{PW} › … oder rechtlich"),
       ("hind", f"{PW} › Verfahrenshindernis"), ("fall2", f"{PW} › hier: Einstellung")], rechts_frei([
    *tafel("p170", "Wann wird eingestellt? § 170 StPO"),
    *w170,
    z("kein hinreichender Tatverdacht:", 110, w170_y + 30, "tats", "Bold", 34),
    z("– tatsächlich: Tat nicht beweisbar", 130, w170_y + 80, beim("tats", "tatsächlichen"), size=32),
    z("– rechtlich: z. B. kein Straftatbestand erfüllt", 130, w170_y + 126, "recht", size=32),
    z("oder: Verfahrenshindernis", 110, w170_y + 185, "hind", "Bold", 34),
    zit("mehr dazu in den Videos „Hinreichender Tatverdacht“ und „Verfahrenshindernisse“", 110, w170_y + 238, "verw"),
    blk(110, w170_y + 290, 1040, 76, HELLROT, "fall2", [("hier: kein Behandlungsfehler, Aufklärung belegt", "ExtraBold", 32, INK)]),
    *requisit([("p170", ("tabler", "scale", 100, WEISS), "Anklage oder Einstellung?", WEISS),
               ("tats", ("tabler", "zoom-question", 100, WEISS), "nicht beweisbar", WEISS),
               ("recht", ("tabler", "file-x", 100, WEISS), "kein Straftatbestand", WEISS),
               ("hind", ("tabler", "ban", 100, HELLROT), "Verfahrenshindernis", HELLROT),
               ("fall2", ("tabler", "folder", 100, HELLROT), "Einstellung", HELLROT)]),
    *zwei([("p170", "ruhig"), ("tats", "skeptisch"), ("fall2", "froh")], [("p170", "ruhig"), ("fall2", "froh")],
          links="HO", rechts="WA"),
]))
assert w170_y + 366 <= 890

# ===========================================================================================================================
# D Aufbau der Einstellungsverfügung (übliche Klausurpraxis)
# ===========================================================================================================================
PV = "Einstellungsverfügung"
folie([("verfg", f"{PV} · zwei Teile"), ("z1", f"{PV} › Ziff. 1: Einstellung"), ("z2", f"{PV} › Ziff. 2: Mitteilungen"),
       ("fehlt", f"{PV} › im Entwurf: Mitteilungen fehlen")], rechts_frei([
    *tafel("verfg", "Die Einstellungsverfügung"),
    zit("Staatsanwaltschaft · Az. … · Verfügung", 110, 180, "verfg", size=28),
    blk(110, 240, 1040, 120, GELB, "z1", [("1. Das Verfahren wird nach", "ExtraBold", 34, INK),
                                         ("§ 170 Abs. 2 StPO eingestellt.", "ExtraBold", 34, INK)]),
    blk(110, 390, 1040, 76, BLAU, "z2", [("2. Mitteilungen", "ExtraBold", 34, INK)]),
    *neinz("im Entwurf: fehlen", 500, "fehlt", "Bold", 34, x=200),
    zit("Gliederung: übliche Klausurpraxis, kein Gesetzeswortlaut", 110, 600, "verfg", size=26),
    *requisit([("verfg", ("tabler", "file-pencil", 100, WEISS), "Verfügung", WEISS),
               ("z1", ("tabler", "folder", 100, GELB), "Ziff. 1: Einstellung", GELB),
               ("z2", ("tabler", "mail", 100, BLAU), "Ziff. 2: Mitteilungen", BLAU),
               ("fehlt", ("tabler", "file-alert", 100, HELLROT), "fehlen im Entwurf", HELLROT)]),
    *allein("HO", [("verfg", "ruhig"), ("z2", "skeptisch"), ("fehlt", "schreck")]),
]))

# ===========================================================================================================================
# E Mitteilung an den Beschuldigten: § 170 Abs. 2 S. 2 StPO (Wortlaut), Nr. 88 S. 2 RiStBV
# ===========================================================================================================================
PM = "Mitteilung an den Beschuldigten"
W170S2 = ("„Hiervon setzt sie den Beschuldigten in Kenntnis, wenn er als solcher vernommen worden ist oder ein Haftbefehl "
          "gegen ihn erlassen war; dasselbe gilt, wenn er um einen Bescheid gebeten hat oder wenn ein besonderes Interesse "
          "an der Bekanntgabe ersichtlich ist.“")
w2, w2_y = wortlaut(80, 165, 1100, W170S2, "§ 170 Abs. 2 S. 2 StPO", "p170s2", marken=[
    ("in Kenntnis", beim("p170s2", "Kenntnis")), ("vernommen worden ist", beim("p170s2", "vernommen")),
    ("Haftbefehl", beim("p170s2", "Haftbefehl"))], size=30)
folie([("p170s2", f"{PM} › § 170 Abs. 2 S. 2 StPO"), ("wall", f"{PM} › Dr. Wallner: vernommen"),
       ("nr88", f"{PM} › Inhalt: Nr. 88 RiStBV")], rechts_frei([
    *tafel("p170s2", "Ziff. 2: der Beschuldigte"),
    *w2,
    *okz("Dr. Wallner: als Beschuldigter vernommen", w2_y + 35, "wall", "Bold", 34, x=160),
    z("– er erhält die Mitteilung", 160, w2_y + 85, beim("wall", "erhält"), size=32),
    z("kein begründeter Verdacht mehr: in der", 110, w2_y + 160, "nr88", "Bold", 32),
    z("Mitteilung ausdrücklich aussprechen", 110, w2_y + 206, "nr88", "Bold", 32),
    zit("Nr. 88 S. 2 RiStBV", 110, w2_y + 258, beim("nr88", "Richtlinien")),
    *requisit([("p170s2", ("tabler", "user-check", 100, WEISS), "vernommen?", WEISS),
               ("wall", ("tabler", "mail", 100, BLAU), "Mitteilung an Dr. Wallner", BLAU),
               ("nr88", ("tabler", "circle-check", 100, HELLGRUEN), "kein Verdacht mehr", HELLGRUEN)]),
    *allein("WA", [("p170s2", "ruhig"), ("nr88", "froh")]),
]))
assert w2_y + 300 <= 890

# ===========================================================================================================================
# F Bescheid an die Antragstellerin: § 171 S. 1, 2 StPO (Wortlaut), § 373b StPO, Nr. 91 Abs. 2 RiStBV
# ===========================================================================================================================
PB = "Bescheid an die Antragstellerin"
W171 = ("„Gibt die Staatsanwaltschaft einem Antrag auf Erhebung der öffentlichen Klage keine Folge oder verfügt sie nach "
        "dem Abschluß der Ermittlungen die Einstellung des Verfahrens, so hat sie den Antragsteller unter Angabe der Gründe "
        "zu bescheiden. In dem Bescheid ist der Antragsteller, der zugleich der Verletzte ist, über die Möglichkeit der "
        "Anfechtung und die dafür vorgesehene Frist (§ 172 Abs. 1) zu belehren. …“")
w3, w3_y = wortlaut(80, 160, 1100, W171, "§ 171 S. 1, 2 StPO", "p171", marken=[
    ("Einstellung des Verfahrens", beim("p171", "Einstellung")), ("Angabe der", beim("p171", "Angabe")), ("Gründe", beim("p171", "Angabe")),
    ("zugleich der", beim("p171s2", "zugleich")), ("Verletzte ist", beim("p171s2", "zugleich")), ("zu belehren", beim("p171s2", "belehren"))], size=29)
folie([("p171", f"{PB} › § 171 S. 1 StPO: mit Gründen"), ("antr", f"{PB} › Frau Rautenberg: Antragstellerin"),
       ("p171s2", f"{PB} › § 171 S. 2 StPO: Belehrung"), ("verl", f"{PB} › Verletzte: § 373b Abs. 1 StPO"),
       ("zust", f"{PB} › Zustellung: Nr. 91 Abs. 2 RiStBV")], rechts_frei([
    *tafel("p171", "Ziff. 2: die Antragstellerin"),
    *w3,
    *okz("Frau Rautenberg: verlangt Bestrafung – Antragstellerin", w3_y + 25, "antr", "Bold", 30, x=160),
    *okz("Verletzte: unmittelbar in Rechtsgütern beeinträchtigt", w3_y + 80, "verl", "Bold", 30, x=160),
    zit("§ 373b Abs. 1 StPO („ihre Begehung unterstellt“)", 160, w3_y + 126, beim("verl", "dreihundertdreiundsiebzig")),
    z("Bescheid wird zugestellt (Beschwerde zu erwarten)", 110, w3_y + 185, "zust", "Bold", 30),
    zit("Nr. 91 Abs. 2 S. 2 RiStBV", 110, w3_y + 230, beim("zust", "zugestellt")),
    *requisit([("p171", ("tabler", "file-text", 100, WEISS), "Bescheid mit Gründen", WEISS),
               ("antr", ("tabler", "user-check", 100, ORANGE), "Antragstellerin", ORANGE),
               ("p171s2", ("tabler", "info-circle", 100, GELB), "Belehrung: Beschwerde + Frist", GELB),
               ("verl", ("tabler", "eye-off", 100, HELLROT), "Verletzte", HELLROT),
               ("zust", ("tabler", "mail", 100, WEISS), "Zustellung", WEISS)]),
    *allein("RA", [("p171", "ruhig"), ("antr", "fest"), ("verl", "ernst")]),
]))
assert w3_y + 270 <= 890

# ===========================================================================================================================
# F2 Der korrigierte Entwurf: Referendarin Hölscher (Blase), Ziff. 1 und Ziff. 2a/2b vollständig
# ===========================================================================================================================
folie([("ho2", f"{PV} › der korrigierte Entwurf")], rechts_frei([
    *tafel("ho2", "Einstellungsverfügung (korrigiert)"),
    blk(110, 190, 1040, 76, GELB, "ho2", [("1. Einstellung nach § 170 Abs. 2 StPO", "ExtraBold", 32, INK)]),
    blk(110, 290, 1040, 120, BLAU, beim("ho2", "Bescheid"), [("2. a) Bescheid an Frau Rautenberg:", "ExtraBold", 32, INK),
                                                           ("Gründe + Belehrung (§ 171 S. 1, 2)", "Bold", 32, INK)]),
    blk(110, 435, 1040, 120, BLAU, beim("ho2", "Mitteilung"), [("2. b) Mitteilung an Dr. Wallner", "ExtraBold", 32, INK),
                                                             ("(§ 170 Abs. 2 S. 2)", "Bold", 32, INK)]),
    *redet("HO_redet", FX, FB, FR, "ho2", "p172"),
    ns(NAME["HO"], FX, FB, "ho2", NFARBE["HO"], d=0.1),
    blase("sprech", 640, 210, "ho2", 1560, 225, inhalt=["Also: Bescheid mit Gründen", "und Belehrung, und eine",
                                                       "Mitteilung an den Arzt."], textsize=34,
          figur=("HO_redet", FX, FB, FR), bis="p172"),
]))

# ===========================================================================================================================
# G Vorschaltbeschwerde: § 172 Abs. 1 StPO (Wortlaut), § 147 Nr. 3 GVG
# ===========================================================================================================================
PG = "Beschwerde"
W172 = ("„(1) Ist der Antragsteller zugleich der Verletzte, so steht ihm gegen den Bescheid nach § 171 binnen zwei Wochen "
        "nach der Bekanntmachung die Beschwerde an den vorgesetzten Beamten der Staatsanwaltschaft zu. Durch die Einlegung "
        "der Beschwerde bei der Staatsanwaltschaft wird die Frist gewahrt. Sie läuft nicht, wenn die Belehrung nach § 171 "
        "Satz 2 unterblieben ist.“")
w4, w4_y = wortlaut(80, 160, 1100, W172, "§ 172 Abs. 1 StPO", "p172", marken=[
    ("zugleich der Verletzte", beim("p172", "zugleich")), ("binnen zwei Wochen", beim("p172", "binnen")),
    ("vorgesetzten Beamten", beim("p172", "vorgesetzten")), ("bei der Staatsanwaltschaft", beim("wahr", "Staatsanwaltschaft")),
    ("läuft nicht", beim("nobel", "läuft"))], size=30)
folie([("p172", f"{PG} › § 172 Abs. 1 S. 1 StPO: 2 Wochen"), ("gsta", f"{PG} › an die Generalstaatsanwaltschaft"),
       ("nurv", f"{PG} › nur der Verletzte"), ("wahr", f"{PG} › § 172 Abs. 1 S. 2: Einlegung bei der StA"),
       ("nobel", f"{PG} › § 172 Abs. 1 S. 3: ohne Belehrung keine Frist")], rechts_frei([
    *tafel("p172", "1. Stufe: Beschwerde, § 172 Abs. 1"),
    *w4,
    z("vorgesetzter Beamter = Generalstaatsanwaltschaft", 110, w4_y + 30, "gsta", "Bold", 32),
    zit("§ 147 Nr. 3 GVG", 110, w4_y + 78, "gsta"),
    *neinz("nur Anzeige, nicht verletzt: keine Beschwerde", w4_y + 130, "nurv", "Bold", 32, x=160),
    *okz("Einlegung bei der Staatsanwaltschaft genügt", w4_y + 190, "wahr", "Bold", 32, x=160),
    *requisit([("p172", ("tabler", "hourglass", 90, GELB), "2 Wochen", GELB),
               ("gsta", ("tabler", "building-bank", 100, LILA), "Generalstaatsanwaltschaft", LILA),
               ("nurv", ("tabler", "user-x", 100, HELLROT), "nur der Verletzte", HELLROT),
               ("wahr", ("tabler", "send", 100, WEISS), "Einlegung bei der StA", WEISS),
               ("nobel", ("tabler", "alert-triangle", 100, HELLROT), "ohne Belehrung: keine Frist", HELLROT)]),
    *allein("RA", [("p172", "ruhig"), ("gsta", "fest"), ("nobel", "skeptisch")]),
]))
assert w4_y + 240 <= 890

# ===========================================================================================================================
# H1 Klageerzwingungsantrag: § 172 Abs. 2 S. 1, Abs. 4 S. 1 StPO (Wortlaut)
# ===========================================================================================================================
PK = "Klageerzwingungsantrag"
W172B = ("„(2) Gegen den ablehnenden Bescheid des vorgesetzten Beamten der Staatsanwaltschaft kann der Antragsteller binnen "
         "einem Monat nach der Bekanntmachung gerichtliche Entscheidung beantragen. … (4) Zur Entscheidung über den Antrag "
         "ist das Oberlandesgericht zuständig. …“")
w5, w5_y = wortlaut(80, 165, 1100, W172B, "§ 172 Abs. 2 S. 1, Abs. 4 S. 1 StPO", "p172b", marken=[
    ("ablehnenden Bescheid", beim("p172b", "ablehnenden")), ("einem Monat", beim("p172b", "Monat")),
    ("gerichtliche Entscheidung", beim("p172b", "gerichtliche")), ("Oberlandesgericht", beim("olg", "Oberlandesgericht"))],
    size=30)
folie([("p172b", f"{PK} › § 172 Abs. 2 S. 1 StPO: 1 Monat"), ("olg", f"{PK} › § 172 Abs. 4 StPO: Oberlandesgericht")], rechts_frei([
    *tafel("p172b", "2. Stufe: Antrag ans Gericht"),
    *w5,
    blk(110, w5_y + 40, 1040, 80, GELB, beim("p172b", "Monat"), [("1 Monat ab Bekanntmachung", "ExtraBold", 34, INK)]),
    *okz("zuständig: das Oberlandesgericht", w5_y + 160, "olg", "ExtraBold", 34, x=160),
    *requisit([("p172b", ("tabler", "calendar-event", 100, GELB), "1 Monat", GELB),
               ("olg", ("tabler", "gavel", 100, LILA), "Oberlandesgericht", LILA)]),
    *allein("RA", [("p172b", "ernst"), ("olg", "fest")]),
]))

# ===========================================================================================================================
# H2 Form: § 172 Abs. 3 S. 1, 2 StPO (Wortlaut), BVerfG 2 BvR 1550/17 Rn. 18, 19; Rechtsanwältin kommt dazu
# ===========================================================================================================================
W172C = ("„(3) Der Antrag auf gerichtliche Entscheidung muß die Tatsachen, welche die Erhebung der öffentlichen Klage "
         "begründen sollen, und die Beweismittel angeben. Er muß von einem Rechtsanwalt unterzeichnet sein; …“")
w6, w6_y = wortlaut(80, 165, 1100, W172C, "§ 172 Abs. 3 S. 1, 2 StPO", "p172c", marken=[
    ("die Tatsachen", beim("p172c", "Tatsachen")), ("die Beweismittel", beim("p172c", "Beweismittel")),
    ("Rechtsanwalt unterzeichnet", beim("anw", "Rechtsanwalt"))], size=30)
folie([("p172c", f"{PK} › Form: § 172 Abs. 3 S. 1 StPO"), ("bverfg", f"{PK} › Darlegung nach dem BVerfG"),
       ("nueb", f"{PK} › keine Überspannung"), ("anw", f"{PK} › § 172 Abs. 3 S. 2 StPO: Anwalt")], rechts_frei([
    *tafel("p172c", "Form: § 172 Abs. 3 StPO"),
    *w6,
    z("aus sich selbst heraus verständliche", 110, w6_y + 30, "bverfg", "Bold", 34),
    z("Schilderung des Sachverhalts", 110, w6_y + 78, "bverfg", "Bold", 34),
    *neinz("Anforderungen nicht überspannen", w6_y + 140, "nueb", "Bold", 34, x=160),
    zit("BVerfG, Beschl. v. 2.7.2018 – 2 BvR 1550/17, Rn. 18, 19", 110, w6_y + 196, "bverfg", size=28),
    *okz("Anwaltszwang: unterzeichnet von Rechtsanwalt", w6_y + 260, "anw", "ExtraBold", 32, x=160),
    *requisit([("p172c", ("tabler", "list-check", 100, WEISS), "Tatsachen + Beweismittel", WEISS),
               ("bverfg", ("tabler", "scale", 100, LILA), "verständlich aus sich heraus", LILA),
               ("anw", ("tabler", "signature", 100, HELLGRAU), "Anwalt unterschreibt", HELLGRAU)]),
    *stehend("RA", X2, [("p172c", "ruhig"), ("bverfg", "skeptisch"), ("anw", "froh")]),
    *stehend("AN", X1, [("anw", "ruhig")]),
]))
assert w6_y + 300 <= 890

# ===========================================================================================================================
# H3 Ausschluss: § 172 Abs. 2 S. 3 StPO (Wortlaut, Auszug); Fall: § 226 Abs. 1 Nr. 1 StGB im Raum
# ===========================================================================================================================
PA = "Ausschluss"
W172D = ("„Der Antrag ist nicht zulässig, wenn das Verfahren ausschließlich eine Straftat zum Gegenstand hat, die vom "
         "Verletzten im Wege der Privatklage verfolgt werden kann, oder wenn die Staatsanwaltschaft nach § 153 Abs. 1, "
         "§ 153a Abs. 1 Satz 1, 7 oder § 153b Abs. 1 von der Verfolgung der Tat abgesehen hat; …“")
w7, w7_y = wortlaut(80, 165, 1100, W172D, "§ 172 Abs. 2 S. 3 StPO", "ausschl", marken=[
    ("ausschließlich", beim("ausschl", "nur")), ("Privatklage", beim("ausschl", "Privatklagedelikt")),
    ("§ 153 Abs. 1", beim("opp", "Opportunitätsgründen"))], size=30)
folie([("ausschl", f"{PA} › § 172 Abs. 2 S. 3: nur Privatklagedelikt"), ("opp", f"{PA} › Opportunitätseinstellungen"),
       ("p226", f"{PA} › hier: § 226 Abs. 1 Nr. 1 StGB im Raum"), ("offen", f"{PA} › kein Ausschluss (+)")], rechts_frei([
    *tafel("ausschl", "Ausschluss: § 172 Abs. 2 S. 3"),
    *w7,
    z("z. B. einfache Körperverletzung, §§ 223, 229 StGB", 110, w7_y + 30, beim("ausschl", "einfache"), "Bold", 32),
    zit("§ 374 Abs. 1 Nr. 4 StPO", 110, w7_y + 76, beim("ausschl", "Körperverletzung")),
    z("hier: Verlust des Sehvermögens auf einem Auge", 110, w7_y + 135, "p226", "Bold", 32),
    zit("schwere Körperverletzung, § 226 Abs. 1 Nr. 1 StGB – kein Privatklagedelikt", 110, w7_y + 181, beim("p226", "schwere")),
    *okz("kein Ausschluss: Der Weg ist offen.", w7_y + 240, "offen", "ExtraBold", 34, x=160),
    *requisit([("ausschl", ("tabler", "ban", 100, HELLROT), "nur Privatklagedelikt?", HELLROT),
               ("opp", ("tabler", "scale", 100, WEISS), "§§ 153 ff.?", WEISS),
               ("p226", ("tabler", "eye-off", 100, HELLROT), "§ 226 im Raum", HELLROT),
               ("offen", ("tabler", "lock-open", 100, HELLGRUEN), "Weg offen", HELLGRUEN)]),
    *stehend("AN", X1, [("ausschl", "ernst"), ("offen", "froh")]),
    *stehend("RA", X2, [("ausschl", "sorge"), ("offen", "froh")]),
]))
assert w7_y + 285 <= 890

# ===========================================================================================================================
# I Entscheidung des Oberlandesgerichts: §§ 174, 175 StPO
# ===========================================================================================================================
PO = "Oberlandesgericht"
folie([("p174", f"{PO} › § 174 Abs. 1 StPO: Verwerfung"), ("p175", f"{PO} › § 175 S. 1 StPO: Anklagebeschluss"),
       ("durchf", f"{PO} › § 175 S. 2 StPO: Durchführung durch die StA")], rechts_frei([
    *tafel("p174", "Entscheidung: §§ 174, 175 StPO"),
    z("kein genügender Anlass zur Anklage", 110, 190, "p174", "Bold", 34),
    blk(110, 245, 1040, 76, HELLROT, beim("p174", "verwirft"), [("§ 174 Abs. 1: Verwerfung des Antrags", "ExtraBold", 34, INK)]),
    z("Antrag begründet", 110, 380, "p175", "Bold", 34),
    blk(110, 435, 1040, 120, HELLGRUEN, beim("p175", "beschließt"), [("§ 175 S. 1: Beschluss, die öffentliche", "ExtraBold", 34, INK),
                                                                    ("Klage zu erheben", "ExtraBold", 34, INK)]),
    *okz("§ 175 S. 2: durchführen muss die Staatsanwaltschaft", 600, "durchf", "Bold", 32, x=160),
    *requisit([("p174", ("tabler", "gavel", 100, HELLROT), "Verwerfung", HELLROT),
               ("p175", ("tabler", "gavel", 100, HELLGRUEN), "Anklagebeschluss", HELLGRUEN),
               ("durchf", ("tabler", "building-bank", 100, LILA), "Staatsanwaltschaft klagt an", LILA)]),
    *zwei([("p174", "ernst"), ("p175", "sorge")], [("p174", "ruhig"), ("p175", "fest")], links="WA", rechts="RA"),
]))

# ===========================================================================================================================
# J1/J2 Lösung: Kalender Juli 2026 (Beschwerde) und September 2026 (Antrag), § 43 StPO
# ===========================================================================================================================
KW_, KH_, KCX, KCY = 148, 76, 115, 330       # Kalenderzelle: Breite, Höhe, links, oben
TAGE = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
for t_, wt in [((2026, 1, 13), 1), ((2026, 7, 2), 3), ((2026, 7, 13), 0), ((2026, 7, 16), 3), ((2026, 8, 5), 2),
               ((2026, 9, 5), 5), ((2026, 9, 7), 0)]:
    assert _dt.date(*t_).weekday() == wt, t_
# Fristende § 43 Abs. 1 StPO: 2 Wochen ab Do, 2.7. = Do, 16.7.; 1 Monat ab Mi, 5.8. = Sa, 5.9. → § 43 Abs. 2: Mo, 7.9.
assert _dt.date(2026, 7, 2) + _dt.timedelta(14) == _dt.date(2026, 7, 16)
# Kein bundesweiter Feiertag am 16.7. oder 7.9.2026 (Ostern 5.4.2026: Fronleichnam 4.6., Himmelfahrt 14.5.)


def monat(jahr, m):
    """Wochenzeilen [(tag, im_monat)] ab Montag."""
    erster = _dt.date(jahr, m, 1)
    start = erster - _dt.timedelta(erster.weekday())
    wochen = []
    d = start
    while True:
        w = []
        for _ in range(7):
            w.append((d.day, d.month == m)); d += _dt.timedelta(1)
        wochen.append(w)
        if d.month != m:
            break
    return wochen


def kal_bau(jahr, m):
    W_ = monat(jahr, m)

    def zelle(tag):
        for r, w in enumerate(W_):
            for c, (d, im_m) in enumerate(w):
                if d == tag and im_m:
                    return KCX + c * KW_, KCY + r * KH_
        raise KeyError(tag)

    def kalender(cue):
        s = 2
        im = Image.new("RGBA", (7 * KW_ * s + 8 * s, (len(W_) * KH_ + 50) * s))
        dr = ImageDraw.Draw(im)
        fk, fz = F("Bold", 28 * s), F("Bold", 32 * s)
        for c, t in enumerate(TAGE):
            dr.text(((c * KW_ + KW_ / 2) * s, 22 * s), glyphen(t), font=fk, fill=TEXT if c >= 5 else INK, anchor="mm")
        for r, w in enumerate(W_):
            for c, (d, im_m) in enumerate(w):
                x0, y0 = c * KW_ * s + 4 * s, (50 + r * KH_) * s
                dr.rounded_rectangle((x0, y0, x0 + (KW_ - 8) * s, y0 + (KH_ - 8) * s), 10 * s,
                                     fill=(255, 255, 255, 255) if im_m else (238, 238, 234, 255), outline=INK, width=3 * s)
                dr.text((x0 + 14 * s, y0 + 6 * s), str(d), font=fz, fill=INK if im_m else (150, 150, 150, 255))
        im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
        return El(im, KCX - 4, KCY - 50, cue, "fade", 0.0, None, name="kalender")

    def markiere(tag, cue, fill, text=None, bis=None):
        x, y = zelle(tag)
        im = Image.new("RGBA", (KW_ - 8, KH_ - 8))
        d_ = ImageDraw.Draw(im)
        d_.rounded_rectangle((0, 0, im.width - 1, im.height - 1), 10, fill=fill[:3] + (255,), outline=INK, width=3)
        d_.text((14, 6), str(tag), font=F("Bold", 32), fill=INK)
        if text:
            d_.text((im.width - 8, im.height - 5), glyphen(text), font=F("Bold", 26), fill=INK, anchor="rd")
        return El(im, x, y, cue, "pop", 0.0, bis, name=f"tag:{tag}")

    return kalender, markiere, len(W_)


kal7, mark7, n7 = kal_bau(2026, 7)
PL = "Lösung"
folie([("lsg", f"{PL} › Beschwerde: Frist"), ("zwei", f"{PL} › Bescheid zugestellt: Do, 2.7.2026"),
       (beim("ende1", "sechzehnten"), f"{PL} › Fristende: Do, 16.7.2026, 24 Uhr"), (beim("mo13", "rechtzeitig"), f"{PL} › Beschwerde am 13.7.2026: rechtzeitig (+)")], rechts_frei([
    *tafel("lsg", "Fristen: Beschwerde"),
    pl("Fortsetzung des Falls", 640, 100, "lsg", fill=PINK, size=28),
    z("Bescheid zugestellt: Do, 2.7.2026", 110, 172, "zwei", "Bold", 32),
    z("Juli 2026", 1150 - F("ExtraBold", 30).getlength("Juli 2026"), 222, "zwei", "ExtraBold", 30, farbe=TEXT),
    kal7("zwei"),
    mark7(2, beim("zwei", "zweiten"), GELB, "zu"),
    mark7(16, beim("ende1", "sechzehnten"), HELLROT, "Ende"),
    mark7(13, beim("mo13", "dreizehnten"), GRUEN),
    *okz("Beschwerde am Mo, 13.7.2026: rechtzeitig", 330 + n7 * KH_ + 25, beim("mo13", "rechtzeitig"), "ExtraBold", 32, x=160),
    zit("§ 172 Abs. 1 S. 1, § 43 Abs. 1 StPO", 110, 330 + n7 * KH_ + 80, beim("mo13", "rechtzeitig")),
    *requisit([("lsg", ("tabler", "hourglass", 90, WEISS), "2 Wochen", WEISS),
               ("zwei", None, None, None),
               (beim("ende1", "sechzehnten"), ("tabler", "calendar-x", 100, HELLROT), "Ende: Do, 16.7.", HELLROT),
               ("mo13", ("tabler", "calendar-check", 100, GRUEN), "Beschwerde: 13.7.", HELLGRUEN)]),
    szene(ficon("tabler", "mail-opened", PX, PU, 110, "zwei", fuell=WEISS, bis=beim("ende1", "sechzehnten")), "186brief*", 1.0, 0.0),
    pl("zugestellt: 2.7.", PX, PY, "zwei", fill=GELB, size=28, anker="m", bis=beim("ende1", "sechzehnten")),
    *allein("RA", [("lsg", "ruhig"), ("zwei", "ernst"), ("mo13", "froh")]),
]))
assert 330 + n7 * KH_ + 120 <= 890

kal9, mark9, n9 = kal_bau(2026, 9)
folie([("ablehn", f"{PL} › Antrag: Bescheid zugestellt Mi, 5.8.2026"), (beim("sa5", "Samstag"), f"{PL} › 1 Monat: Sa, 5.9.2026"),
       (beim("mo7", "siebten"), f"{PL} › § 43 Abs. 2 StPO: Ende Mo, 7.9.2026, 24 Uhr")], rechts_frei([
    *tafel("ablehn", "Fristen: Antrag ans OLG"),
    z("Beschwerde zurückgewiesen, zugestellt: Mi, 5.8.2026", 110, 172, beim("ablehn", "Bescheid"), "Bold", 32),
    z("September 2026", 1150 - F("ExtraBold", 30).getlength("September 2026"), 222, "sa5", "ExtraBold", 30, farbe=TEXT),
    kal9("sa5"),
    mark9(5, beim("sa5", "fünfte"), HELLGRAU, "Sa"),
    mark9(7, beim("mo7", "siebten"), HELLROT, "Ende"),
    *okz("Sa, 5.9. – Ende am nächsten Werktag: Mo, 7.9.2026", 330 + n9 * KH_ + 25, beim("mo7", "siebten"), "ExtraBold", 30, x=160),
    zit("§ 172 Abs. 2 S. 1, § 43 Abs. 1, 2 StPO", 110, 330 + n9 * KH_ + 80, beim("mo7", "Paragraf")),
    *requisit([("ablehn", ("tabler", "file-x", 100, HELLROT), "Beschwerde zurückgewiesen", HELLROT),
               ("sa5", ("tabler", "calendar-event", 100, HELLGRAU), "1 Monat: Sa, 5.9.", HELLGRAU),
               (beim("mo7", "siebten"), ("tabler", "calendar-x", 100, HELLROT), "Ende: Mo, 7.9.", HELLROT)]),
    *allein("RA", [("ablehn", "sorge"), ("mo7", "fest")]),
]))
assert 330 + n9 * KH_ + 120 <= 890

# ===========================================================================================================================
# J3 Kanzlei: Frau Rautenberg mit ihrer Anwältin (Blase)
# ===========================================================================================================================
AN3, RA3 = 1000, 1400
folie([("ra2", f"{PL} › mit Anwältin zum Oberlandesgericht")], [
    boden("ra2"),
    fenster("ra2", 160, 330, w=280, h=240),
    hart(pl("Kanzlei", 70, 30, "ra2", fill=HELLGRAU, size=38)),
    schreibtisch("ra2", 520, 820, h=150),
    hart(ficon("tabler", "file-pencil", 670, BODEN_Y - 150, 110, "ra2", fuell=WEISS, anim="cut")),
    *stehend("AN", AN3, [("ra2", "ruhig_r")], unten=BODEN_Y),
    *redet("RA_redet2", RA3, BODEN_Y, FHA, "ra2", "sch"),
    hart(ns(NAME["RA"], RA3, BODEN_Y, "ra2", NFARBE["RA"])),
    blase("sprech", 760, 200, "ra2", 940, 210, inhalt=["Dann gehe ich mit meiner Anwältin", "zum Oberlandesgericht."],
          textsize=34, figur=("RA_redet2", RA3, BODEN_Y, FHA), bis="sch"),
])

# ===========================================================================================================================
# K Prüfschema Klageerzwingungsantrag (Aufbau Punkt für Punkt)
# ===========================================================================================================================
REIHEN = [("s1", 0, "I. Zulässigkeit"),
          ("s1a", 1, "1. Antragsteller und Verletzter (§§ 171, 172 Abs. 1, § 373b StPO)"),
          ("s1b", 1, "2. erfolglose Beschwerde binnen 2 Wochen (§ 172 Abs. 1)"),
          ("s1c", 1, "3. Antrag binnen 1 Monat beim OLG (§ 172 Abs. 2 S. 1, Abs. 4)"),
          ("s1d", 1, "4. Tatsachen, Beweismittel, Anwalt (§ 172 Abs. 3)"),
          ("s1e", 1, "5. kein Ausschluss (§ 172 Abs. 2 S. 3)"),
          ("s2", 0, "II. Begründetheit: genügender Anlass zur Erhebung der öffentlichen Klage"),
          ("s3", 0, "III. Entscheidung: Verwerfung (§ 174) oder Anklagebeschluss (§ 175)")]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfschema: Klageerzwingungsantrag"), 110, 90, "sch", 46)]
y = 190
for c, ebene, text in REIHEN:
    x = (130, 200)[ebene]
    els_sch.append(z(text, x, y, c, "ExtraBold" if ebene == 0 else "Regular", 40 if ebene == 0 else 36, rechts=1800))
    y += {0: 84, 1: 70}[ebene]
assert y <= 960, y
folie([("sch", "Prüfschema"), ("s1", "Prüfschema › I. Zulässigkeit"), ("s1a", "Prüfschema › I. 1. Verletzter"),
       ("s1b", "Prüfschema › I. 2. Beschwerde"), ("s1c", "Prüfschema › I. 3. Antragsfrist"),
       ("s1d", "Prüfschema › I. 4. Form"), ("s1e", "Prüfschema › I. 5. kein Ausschluss"),
       ("s2", "Prüfschema › II. Begründetheit"), ("s3", "Prüfschema › III. Entscheidung")], els_sch)

# ===========================================================================================================================
# L Klausurtipp (Lexi): Mitteilungen nicht vergessen
# ===========================================================================================================================
els_k = [*tafel("tipp", "Klausurtipp: Ziff. 2 nie vergessen", fill=HELL), warnung_i(150, 225, "tipp", gr=26),
         z("die Mitteilungen der Einstellungsverfügung", 200, 200, "tipp", "Bold", 34),
         blk(130, 300, 1020, 90, GELB, "k1", [("Antragsteller: Bescheid mit Gründen", "ExtraBold", 34, INK)]),
         blk(130, 420, 1020, 130, BLAU, "k2", [("Verletzter: Belehrung über Beschwerde", "ExtraBold", 34, INK),
                                               ("und Frist – sonst läuft keine Frist", "ExtraBold", 34, INK)]),
         blk(130, 580, 1020, 90, HELLGRUEN, "k3", [("Beschuldigter: Mitteilung, z. B. nach Vernehmung", "ExtraBold", 32, INK)]),
         *redet("LX_warnt", FX, FB, FR + 40, "tipp", "merke"),
         ns("Lexi", FX, FB, "tipp", GELB, d=0.2)]
folie([("tipp", "Klausurtipp · Mitteilungen"), ("k1", "Klausurtipp › Bescheid mit Gründen"),
       ("k2", "Klausurtipp › Belehrung"), ("k3", "Klausurtipp › Mitteilung an den Beschuldigten")], els_k)

# ===========================================================================================================================
# M Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Wer einstellt, muss den", 0)],
                 [("Antragsteller ", 0), ("bescheiden.", "a")]], 750, 290, 42, "merke", {"a": beim("merke", "bescheiden")}),
    *markertext([[("Der Verletzte hat ", 0), ("2 Wochen", "b"), (" für die", 0)],
                 [("Beschwerde und dann ", 0), ("1 Monat", "c"), (" für den", 0)],
                 [("Klageerzwingungsantrag,", 0)],
                 [("mit Anwalt beim ", 0), ("Oberlandesgericht.", "d")]], 750, 500, 40, "m2",
                {"b": beim("m2", "zwei"), "c": beim("m2", "Monat"), "d": beim("m2", "Oberlandesgericht")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
