"""Folge 197 · Zweistufentheorie: Stadthalle, Förderkredit und Kita-Platz – Serienstandard Open Peeps (Katzenkönig).
Beispielfall: Die Stadt betreibt ihre Stadthalle über eine eigene GmbH (alle Anteile bei der Stadt). Frau Lammers, Vorsitzende
des Chors Liederkranz, will den großen Saal für das Frühjahrskonzert mieten; Geschäftsführer Herr Scheffler lehnt ab, weil der
Bürgermeister (fiktiv, nicht im Bild) den Chor nicht in der Halle haben möchte. Szenen laut ../SZENENPLAN.md: A Foyer der
Stadthalle, B Sachverhalt, C1 Problem, C2 Zweistufentheorie, D1 § 8 Abs. 2, 4 GO NRW (Wortlaut), D2 Normtabelle und Art. 28
Abs. 2 S. 1 GG (Wortlaut), E Grenzen (Widmung, Kapazität, Gleichbehandlung), F das Wie, G1 Eigengesellschaft und
Einwirkungsanspruch, G2 Rechtsweg, H Förderkredit und Kita-Platz, I Streitstand/Kritik, J1 Lösung, J2 zurück im Foyer,
K Klausurtipp (Lexi), L Prüfschema, M Merksatz (Lexi).
Handlungsgeräusch: Tischglocke an der Empfangstheke, als Frau Lammers ins Foyer kommt (A); ../geraeusche_herkunft.json.
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz
als eigene Kopie aus Folge 192 (gemeinsame Dateien unverändert); neu: tic() (Tafel-Icon mit eigener Randprüfung), tuer(),
theke(), brett(), foyer().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut nach recht.nrw.de (GO NRW, Fassung ab 01.01.2026) und
gesetze-im-internet.de (GG, VwGO, SGB VIII), Abruf 04.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave
import datetime as _dt

bausteine.FIGORDNER = "op_197/"

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
BEIGE = (201, 166, 107, 255)
ROSE = (242, 167, 195, 255)
FELD1 = (246, 232, 170, 255)
FELD2 = (205, 232, 190, 255)
FELD3 = (176, 218, 160, 255)
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
        if n.startswith(("bild:", "ficon:")) or "/op_197/" in n:      # Tafel-Icons heißen 'tafelicon:' (eigene Prüfung)
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
    return [bis_(ok(x - 45, y + 20, cue, gr=gr), k.get("bis")), z(text, x, y, cue, stil, size, **k)]


def neinz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Kreuz davor (zur gesprochenen Verneinung)."""
    return [bis_(nein(x - 45, y + 20, cue, gr=gr), k.get("bis")), z(text, x, y, cue, stil, size, **k)]


# --- eigene Szenenbausteine (programmatisch, Palettenflächen, Tuschekontur) ---------------------------------------------------
BODEN_Y = 905                                # Boden = Unterkante der Figuren in den Fallszenen
FHA = 470                                    # Figurenhöhe in den Fallszenen
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
NAME = {"LA": "Frau Lammers", "SC": "Herr Scheffler"}
NFARBE = {"LA": LILA, "SC": GRUEN}


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


def zwei(folge_l, folge_r, links="LA", rechts="SC"):
    """Zwei Figuren rechts neben der Tafel (blicken nach links zur Tafel)."""
    return [*stehend(links, X1, folge_l), *stehend(rechts, X2, folge_r)]


def allein(k, folge):
    return stehend(k, FX, folge)



import math

# --- eigene Szenenbausteine Folge 197 ----------------------------------------------------------------------------------------
WANDF = (242, 234, 220, 255)


def tic(setname, name, cx, unten, breite, cue, fuell=None, bis=None, anim="pop"):
    """Icon auf der Tafel (Diagramm): muss innerhalb der Karte bleiben (x ≤ 1170)."""
    e = ficon(setname, name, cx, unten, breite, cue, fuell=fuell, bis=bis, anim=anim)
    assert 80 <= e.x and e.x + e.sprite.width <= 1170 and e.y >= 160, f"Tafel-Icon außerhalb der Karte: {name}"
    e.name = "tafelicon:" + name
    return e


def tuer(c, x0, w=300, h=430):
    """Doppeltür zum großen Saal (Holzrahmen, Tuschekontur)."""
    def zz(dr, s):
        dr.rounded_rectangle((3 * s, 3 * s, (w - 3) * s, (h - 3) * s), 8 * s, fill=HOLZ, outline=INK, width=5 * s)
        dr.line((w // 2 * s, 3 * s, w // 2 * s, (h - 3) * s), fill=INK, width=4 * s)
        for xx in (w // 2 - 30, w // 2 + 18):
            dr.rounded_rectangle((xx * s, (h // 2 - 40) * s, (xx + 12) * s, (h // 2 + 40) * s), 4 * s, fill=GELB, outline=INK, width=3 * s)
        for xx in (24, w // 2 + 24):
            dr.rounded_rectangle((xx * s, 30 * s, (xx + w // 2 - 48) * s, 150 * s), 6 * s, fill=(214, 232, 250, 255), outline=INK, width=4 * s)
    return hart(El(_flaeche(w, h, zz), x0, BODEN_Y - h, c, "cut", 0.0, None, name="tuer"))


def theke(c, x0, x1, h=200):
    """Empfangstheke im Foyer."""
    w = x1 - x0
    def zz(dr, s):
        dr.rounded_rectangle((3 * s, 0, (w - 3) * s, 30 * s), 6 * s, fill=HOLZ, outline=INK, width=5 * s)
        dr.rectangle((14 * s, 30 * s, (w - 14) * s, (h - 3) * s), fill=WEISS, outline=INK, width=5 * s)
        dr.line((14 * s, 80 * s, (w - 14) * s, 80 * s), fill=INK, width=3 * s)
    return hart(El(_flaeche(w, h, zz), x0, BODEN_Y - h, c, "cut", 0.0, None, name="theke"))


def brett(c, x0, y0, w=360, h=300):
    """Belegungsplan an der Wand (Pinnwand mit Rahmen)."""
    def zz(dr, s):
        dr.rounded_rectangle((3 * s, 3 * s, (w - 3) * s, (h - 3) * s), 14 * s, fill=(250, 244, 226, 255), outline=INK, width=5 * s)
    return hart(El(_flaeche(w, h, zz), x0, y0, c, "cut", 0.0, None, name="brett"))


def foyer(c):
    """Grundform der Fallszene: Foyer der Stadthalle mit Saaltür, Belegungsplan und Empfangstheke."""
    return [boden(c), tuer(c, 110), hart(pl("Großer Saal", 260, 440, c, fill=WEISS, size=30, anker="m")),
            brett(c, 520, 500), hart(ficon("tabler", "calendar-event", 700, 760, 170, c, fuell=WEISS, anim="cut")),
            hart(pl("Belegungsplan", 700, 520, c, fill=GELB, size=28, anker="m")),
            theke(c, 1400, 1570),
            hart(ficon("fluent-emoji-high-contrast", "bellhop-bell", 1485, BODEN_Y - 198, 70, c, fuell=GELB, anim="cut"))]


# ===========================================================================================================================
# A Fall: Foyer der Stadthalle
# ===========================================================================================================================
LAX, SCX = 1250, 1700
folie([(NULL, "Fall · Die Stadthalle der Stadt"), ("anteile", "Fall · Betreiberin: städtische GmbH"),
       ("chor", "Fall · Der Chor fragt an"), ("la1", "Fall · Frau Lammers möchte den Saal"),
       ("sc1", "Fall · Herr Scheffler lehnt ab"), ("schach", "Fall · Der Schachclub durfte"),
       ("frage", "Fall · Anspruch auf den Saal – gegen wen?"), ("frage2", "Fall · die Zweistufentheorie")], [
    *foyer(NULL),
    hart(pl("Stadthalle · Foyer", 70, 30, NULL, fill=GRUEN, size=38)),
    pl("Betreiberin: Stadthallen-GmbH", 70, 110, beim("fall", "Gesellschaft"), fill=WEISS, size=32),
    pl("alle Anteile: die Stadt", 70, 185, "anteile", fill=GELB, size=32),
    # Herr Scheffler hinter der Theke rechts, blickt nach links zu Frau Lammers
    *fig("SC", SCX, BODEN_Y, FHA, [(NULL, "ruhig"), ("la1", "denkt")], erst="cut", bis="sc1"),
    *redet("SC_redet", SCX, BODEN_Y, FHA, "sc1", "schach"),
    *fig("SC", SCX, BODEN_Y, FHA, [("schach", "verlegen")], erst="cut"),
    hart(ns("Herr Scheffler · GmbH", SCX, BODEN_Y, NULL, NFARBE["SC"])),
    # Frau Lammers kommt ins Foyer (Tischglocke)
    szene(peep_voll("LA_hofft_r", LAX, BODEN_Y, FHA, "chor", anim="pop", bis="la1"), "197glocke*", 1.0, 0.25),
    *redet("LA_redet_r", LAX, BODEN_Y, FHA, "la1", "sc1"),
    *fig("LA", LAX, BODEN_Y, FHA, [("sc1", "sorge_r"), ("schach", "entschlossen_r"), ("frage", "denkt_r")], erst="cut"),
    ns("Frau Lammers · Chor", LAX, BODEN_Y, "chor", NFARBE["LA"], anim="cut"),
    ficon("fluent-emoji-high-contrast", "musical-notes", 1020, 450, 100, "chor", fuell=LILA, bis="la1"),
    pl("Termin frei", 700, 815, beim("la1", "Termin"), fill=GRUEN, size=30, anker="m"),
    blase("sprech", 900, 230, "la1", 1150, 210, inhalt=["Wir möchten den großen Saal für", "unser Frühjahrskonzert mieten.",
                                                     "Der Termin ist doch frei."], textsize=34,
          figur=("LA_redet_r", LAX, BODEN_Y, FHA), bis="sc1"),
    blase("sprech", 960, 230, "sc1", 1270, 210, inhalt=["Das stimmt. Aber der Bürgermeister", "möchte Ihren Chor nicht",
                                                     "in der Halle haben."], textsize=34,
          figur=("SC_redet", SCX, BODEN_Y, FHA), bis="schach"),
    ficon("tabler", "chess-knight", 1000, 470, 100, "schach", fuell=WEISS),
    pl("letzter Monat: Schachturnier", 1000, 290, "schach", fill=WEISS, size=30, anker="m"),
    pl("Anspruch auf den Saal – gegen wen?", 70, 260, "frage", fill=PINK, size=34),
    pl("Antwort: die Zweistufentheorie", 70, 345, "frage2", fill=GELB, size=32),
])

# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_197(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=34, zeilenabstand=1.30)
        els += e; y += 18
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_197("sv", [
    "Die Stadt (Beispielland Nordrhein-Westfalen) betreibt ihre Stadthalle über eine eigene GmbH; alle Anteile gehören der "
    "Stadt. Der große Saal ist für Konzerte und Veranstaltungen der örtlichen Vereine bestimmt.",
    "Frau Lammers, Vorsitzende des Chors Liederkranz (Verein mit Sitz in der Stadt), möchte den Saal für das "
    "Frühjahrskonzert mieten. Der Termin ist frei. Im letzten Monat hat der Schachclub dort sein Turnier gespielt.",
    "Geschäftsführer Scheffler lehnt ab: „Der Bürgermeister möchte Ihren Chor nicht in der Halle haben.“",
], "Hat der Chor einen Anspruch auf den Saal – und gegen wen?")

# ===========================================================================================================================
# C1 Das Problem: Die Stadt handelt durch eine GmbH
# ===========================================================================================================================
PP = "Problem"
folie([("prob", f"{PP} · Die Stadt handelt durch eine GmbH"), ("prob2", f"{PP} › Rechtsweg? Anspruchsgegner?"),
       ("verweis", f"{PP} › Abgrenzung: Folge Abgrenzungstheorien")], rechts_frei([
    *tafel("prob", "Das Problem: Stadt handelt durch GmbH"),
    tic("fluent-emoji-high-contrast", "classical-building", 300, 420, 150, "prob", fuell=WEISS),
    pl("Stadt", 300, 440, "prob", fill=GELB, size=30, anker="m"),
    pfeil(420, 350, 690, 350, "prob", breite=8, kopf=26),
    tic("tabler", "building-community", 840, 420, 150, "prob", fuell=GRUEN),
    pl("Stadthallen-GmbH", 840, 440, "prob", fill=GRUEN, size=30, anker="m"),
    pl("1. Welcher Rechtsweg ist eröffnet?", 110, 540, beim("prob2", "Welcher"), fill=PINK, size=32),
    pl("2. Gegen wen richtet sich der Anspruch?", 110, 625, beim("prob2", "gegen"), fill=PINK, size=32),
    z("Abgrenzung öffentliches / privates Recht: Folge „Abgrenzungstheorien“", 110, 730, "verweis", "Bold", 28, farbe=TEXT),
    *requisit([("prob", ("tabler", "question-mark", 90, WEISS), "Stadt oder GmbH?", WEISS),
               ("verweis", ("tabler", "scale", 100, WEISS), "Abgrenzungstheorien", WEISS)]),
    *zwei([("prob", "denkt"), ("prob2", "sorge")], [("prob", "ruhig"), ("verweis", "denkt")]),
]))

# ===========================================================================================================================
# C2 Die Zweistufentheorie: Ob und Wie
# ===========================================================================================================================
PZ = "Zweistufentheorie"
folie([("zst", f"{PZ} · zwei Stufen"), ("st1", f"{PZ} › 1. Stufe: das Ob"), ("st1b", f"{PZ} › 1. Stufe: öffentlich-rechtlich"),
       ("st2", f"{PZ} › 2. Stufe: das Wie"), ("st2b", f"{PZ} › 2. Stufe: privatrechtlicher Mietvertrag")], rechts_frei([
    *tafel("zst", "Die Zweistufentheorie"),
    z("teilt den Vorgang in zwei Stufen", 110, 165, "zst", "Bold", 30, farbe=TEXT),
    blk(110, 220, 1040, 120, GELB, "st1", [("1. Stufe: das Ob", "ExtraBold", 36, INK),
                                          ("Wird der Chor überhaupt zugelassen?", "Bold", 30, INK)]),
    *okz("öffentlich-rechtlich", 360, "st1b", "ExtraBold", 34, x=180),
    blk(110, 470, 1040, 120, WEISS, "st2", [("2. Stufe: das Wie", "ExtraBold", 36, INK),
                                           ("Miete, Zeiten, Hausordnung", "Bold", 30, INK)]),
    *okz("kann ein privatrechtlicher Mietvertrag regeln", 610, "st2b", "ExtraBold", 34, x=180),
    zit("vgl. BVerwG, Beschl. v. 2.5.2007 – 6 B 10.07, Rn. 15", 110, 700, "st2b"),
    *requisit([("zst", ("tabler", "list-check", 100, WEISS), "2 Stufen", WEISS),
               ("st1", ("fluent-emoji-high-contrast", "key", 100, GELB), "das Ob: Zulassung", GELB),
               ("st2", ("fluent-emoji-high-contrast", "handshake", 110, WEISS), "das Wie: Mietvertrag", WEISS)]),
    *zwei([("zst", "ruhig"), ("st1", "hofft"), ("st2", "liest")], [("zst", "ruhig"), ("st1b", "denkt"), ("st2b", "froh")]),
]))

# ===========================================================================================================================
# D1 1. Stufe: Zulassungsanspruch, § 8 Abs. 2, 4 GO NRW (Wortlaut)
# ===========================================================================================================================
PA = "1. Stufe · Zulassungsanspruch"
W8 = ("„(2) Alle Einwohner einer Gemeinde sind im Rahmen des geltenden Rechts berechtigt, die öffentlichen Einrichtungen der "
      "Gemeinde zu benutzen … (4) Diese Vorschriften gelten entsprechend für juristische Personen und für "
      "Personenvereinigungen.“")
w8, w8_y = wortlaut(80, 230, 1100, W8, "§ 8 Abs. 2, 4 GO NRW (Auszug)", "go", marken=[
    ("Einwohner", beim("go", "Einwohner")), ("im Rahmen des geltenden", beim("go", "Rahmen")),
    ("öffentlichen Einrichtungen", beim("go", "öffentlichen")), ("Personenvereinigungen.“", beim("go4", "Personenvereinigungen"))],
    size=32)
folie([("go", f"{PA} · § 8 Abs. 2 GO NRW (Beispiel NRW)"), ("go4", f"{PA} › § 8 Abs. 4: Personenvereinigungen")], rechts_frei([
    *tafel("go", "Das Ob: Anspruch aus der Gemeindeordnung"),
    z("Beispiel Nordrhein-Westfalen: in deinem Land ggf. andere Nummer", 110, 170, "go", "Bold", 28, farbe=TEXT),
    *w8,
    *okz("Chor (Verein mit Sitz in der Stadt): berechtigt", w8_y + 30, beim("go4", "Chor"), "Bold", 32, x=160),
    *requisit([("go", ("tabler", "book", 100, GELB), "Gemeindeordnung", GELB),
               ("go4", ("fluent-emoji-high-contrast", "musical-notes", 100, LILA), "Chor = Verein", LILA)]),
    *zwei([("go", "liest"), ("go4", "ruhig")], [("go", "ernst")]),
]))
assert w8_y + 90 <= 890, w8_y

# ===========================================================================================================================
# D2 Normtabelle (geprüfte Länder) und Art. 28 Abs. 2 S. 1 GG (Wortlaut)
# ===========================================================================================================================
LAENDER = [("Nordrhein-Westfalen", "§ 8 Abs. 2, 4 GO NRW"), ("Bayern", "Art. 21 Abs. 1 S. 1 BayGO"),
           ("Niedersachsen", "§ 30 Abs. 1, 3 NKomVG"), ("Sachsen", "§ 10 Abs. 2, 5 SächsGemO"),
           ("Brandenburg", "§ 12 Abs. 1 BbgKVerf"), ("weitere Länder", "eigene Gemeindeordnung, Nummer prüfen")]
els_tab = [*tafel("tab", "Andere Länder regeln das ähnlich")]
y = 170
for land, norm in LAENDER:
    els_tab += [z(land, 110, y, "tab", "Bold", 30), z(norm, 450, y, "tab", size=30)]
    y += 48
els_tab += [zit("Wortlaut geprüft am 4.10.2026; Bayern: Nummer nach BVerwG 8 C 35.20, Rn. 13", 110, y + 2, "tab")]
W28 = ("„Den Gemeinden muß das Recht gewährleistet sein, alle Angelegenheiten der örtlichen Gemeinschaft im Rahmen der "
       "Gesetze in eigener Verantwortung zu regeln.“")
w28, w28_y = wortlaut(80, y + 50, 1100, W28, "Art. 28 Abs. 2 S. 1 GG", "a28", marken=[
    ("örtlichen Gemeinschaft", beim("a28", "örtlichen")), ("Verantwortung", beim("a28", "selbst"))], size=30)
folie([("tab", f"{PA} › andere Länder"), ("a28", f"{PA} › Selbstverwaltung, Art. 28 Abs. 2 GG"),
       ("a28b", f"{PA} › Halle an eine GmbH: Einfluss vorbehalten")], rechts_frei([
    *els_tab, *w28,
    *okz("Halle an eigene Gesellschaft übertragen: zulässig", w28_y + 18, beim("a28b", "Halle"), "Bold", 30, x=160),
    *okz("aber Einfluss auf die Gesellschaft vorbehalten", w28_y + 64, beim("a28b", "vorbehalten"), "ExtraBold", 30, x=160),
    zit("BVerwG, Urt. v. 27.5.2009 – 8 C 10.08, Rn. 29, 32 f.", 160, w28_y + 110, beim("a28b", "vorbehalten")),
    *requisit([("tab", ("tabler", "map", 100, WEISS), "Landesrecht", WEISS),
               ("a28", ("fluent-emoji-high-contrast", "classical-building", 110, LILA), "Selbstverwaltung", LILA),
               ("a28b", ("tabler", "building-community", 110, GRUEN), "eigene GmbH", GRUEN)]),
    *zwei([("tab", "ruhig"), ("a28b", "denkt")], [("tab", "ruhig"), ("a28", "ernst"), ("a28b", "froh")]),
]))
assert w28_y + 150 <= 900, w28_y

# ===========================================================================================================================
# E Grenzen des Anspruchs: Widmung, Kapazität, Gleichbehandlung
# ===========================================================================================================================
PG = "1. Stufe › Grenzen"
folie([("vor", f"{PG} des Anspruchs"), ("widm", f"{PG} › 1. Widmung"), ("kap", f"{PG} › 2. Kapazität"),
       ("gleich", f"{PG} › 3. Gleichbehandlung, Art. 3 Abs. 1 GG"), ("kein", f"{PG} › kein sachlicher Grund")], rechts_frei([
    *tafel("vor", "Der Anspruch hat Grenzen"),
    blk(110, 180, 1040, 76, WEISS, "widm", [("1. Widmung", "ExtraBold", 34, INK)]),
    *okz("Konzerte und Veranstaltungen der örtlichen Vereine", 270, beim("widm", "Konzerte"), "Bold", 30, x=180),
    blk(110, 340, 1040, 76, WEISS, "kap", [("2. Kapazität", "ExtraBold", 34, INK)]),
    *okz("Termin frei", 430, beim("kap", "Termin"), "Bold", 30, x=180),
    blk(110, 500, 1040, 76, GELB, "gleich", [("3. Gleichbehandlung, Art. 3 Abs. 1 GG", "ExtraBold", 34, INK)]),
    z("Schachclub ja – Chor nein? Nur mit sachlichem Grund", 140, 592, beim("gleich", "Wer"), "Bold", 30),
    *neinz("„passt dem Bürgermeister nicht“: kein sachlicher Grund", 650, "kein", "ExtraBold", 30, x=180),
    zit("BVerwG, Urt. v. 20.1.2022 – 8 C 35.20, Rn. 14 (Widmungszweck, Kapazität)", 110, 730, "widm"),
    zit("VG Gelsenkirchen, Beschl. v. 14.6.2024 – 15 L 888/24, Rn. 21 (Art. 3 Abs. 1 GG)", 110, 770, beim("gleich", "Wer")),
    *requisit([("vor", ("tabler", "list-check", 100, WEISS), "Grenzen", WEISS),
               ("widm", ("fluent-emoji-high-contrast", "musical-notes", 100, LILA), "Konzert: gewidmet", LILA),
               ("kap", ("tabler", "calendar-check", 100, GRUEN), "Termin frei", GRUEN),
               ("gleich", ("tabler", "chess-knight", 100, WEISS), "Schachclub durfte", WEISS),
               ("kein", ("tabler", "ban", 100, HELLROT), "Willkür", HELLROT)]),
    *zwei([("vor", "ruhig"), ("kap", "hofft"), ("kein", "entschlossen")], [("vor", "ruhig"), ("gleich", "verlegen")]),
]))

# ===========================================================================================================================
# F 2. Stufe: das Wie (Mietvertrag)
# ===========================================================================================================================
PW = "2. Stufe · das Wie"
folie([("wie", f"{PW}: Mietvertrag"), ("wie2", f"{PW} › Streit darüber: Zivilgericht")], rechts_frei([
    *tafel("wie", "Das Wie: der Mietvertrag"),
    blk(110, 190, 1040, 120, WEISS, "wie", [("Mietvertrag zwischen Gesellschaft und Chor", "ExtraBold", 34, INK),
                                           ("privatrechtlich", "Bold", 32, INK)]),
    tic("fluent-emoji-high-contrast", "handshake", 630, 520, 150, beim("wie", "Mietvertrag"), fuell=GELB),
    blk(110, 580, 1040, 120, BLAU, "wie2", [("Streit über Miete oder Nutzungsbedingungen:", "ExtraBold", 32, INK),
                                           ("Zivilgericht", "ExtraBold", 32, INK)]),
    zit("vgl. § 13 GVG; VG Gelsenkirchen, Beschl. v. 14.6.2024 – 15 L 888/24, Rn. 19", 110, 725, "wie2"),
    *requisit([("wie", ("tabler", "writing-sign", 100, WEISS), "Mietvertrag", WEISS),
               ("wie2", ("tabler", "gavel", 100, BLAU), "Zivilgericht", BLAU)]),
    *zwei([("wie", "liest")], [("wie", "froh"), ("wie2", "ruhig")]),
]))

# ===========================================================================================================================
# G1 Die Eigengesellschaft: Einwirkungsanspruch gegen die Stadt
# ===========================================================================================================================
PE = "Eigengesellschaft"
folie([("gmbh", f"{PE} · Die Gemeindeordnung verpflichtet die Stadt"), ("gegen", f"{PE} › kein Anspruch gegen die GmbH"),
       ("einw", f"{PE} › Einwirkungsanspruch gegen die Stadt"), ("bverwg", f"{PE} › so auch das BVerwG"),
       ("macht", f"{PE} › alle Anteile: Einfluss gesichert")], rechts_frei([
    *tafel("gmbh", "Wer schuldet die Zulassung?"),
    tic("fluent-emoji-high-contrast", "classical-building", 610, 330, 130, "gmbh", fuell=WEISS),
    pl("Stadt: verpflichtet", 610, 345, "gmbh", fill=GELB, size=28, anker="m"),
    tic("fluent-emoji-high-contrast", "musical-notes", 240, 610, 110, "gmbh", fuell=LILA),
    pl("Chor", 240, 625, "gmbh", fill=LILA, size=28, anker="m"),
    tic("tabler", "building-community", 980, 610, 130, "gmbh", fuell=GRUEN),
    pl("Stadthallen-GmbH", 980, 625, "gmbh", fill=GRUEN, size=28, anker="m"),
    pfeil(320, 560, 880, 560, "gegen", breite=8, kopf=26, farbe=DROT),
    bis_(nein(600, 540, "gegen", gr=26), None),
    z("kein Zulassungsanspruch aus der GO, kein Verwaltungsrechtsweg", 110, 690, "gegen", "Bold", 28),
    zit("OVG Nds., Beschl. v. 24.10.2007 – 10 OB 231/07, Rn. 7 f.", 110, 730, "gegen"),
    pfeil(280, 505, 445, 385, "einw", breite=9, kopf=28, farbe=DGRUEN),
    pl("Einwirkungsanspruch", 110, 260, "einw", fill=GRUEN, size=28),
    pfeil(745, 365, 920, 495, beim("einw", "einwirken"), breite=8, kopf=26),
    pl("wirkt ein", 990, 395, beim("einw", "einwirken"), fill=WEISS, size=28, anker="m"),
    zit("BVerwG, Urt. v. 20.1.2022 – 8 C 35.20, Rn. 14 (stRspr)", 110, 770, "bverwg"),
    pl("100 % der Anteile", 880, 255, "macht", fill=GELB, size=28, anker="m"),
    zit("VG Gelsenkirchen, Beschl. v. 14.6.2024 – 15 L 888/24, Rn. 38–40, 48", 110, 810, "macht"),
    *requisit([("gmbh", ("tabler", "book", 100, WEISS), "GO: die Stadt", WEISS),
               ("einw", ("fluent-emoji-high-contrast", "classical-building", 110, GRUEN), "Anspruch gegen die Stadt", GRUEN),
               ("macht", ("fluent-emoji-high-contrast", "key", 100, GELB), "Einfluss", GELB)]),
    *zwei([("gmbh", "denkt"), ("einw", "entschlossen")], [("gmbh", "ruhig"), ("gegen", "denkt"), ("macht", "froh")]),
]))

# ===========================================================================================================================
# G2 Rechtsweg für den Einwirkungsanspruch
# ===========================================================================================================================
PR = "Rechtsweg"
folie([("rweg", f"{PR} · Einwirkungsanspruch: § 40 Abs. 1 S. 1 VwGO")], rechts_frei([
    *tafel("rweg", "Rechtsweg für den Einwirkungsanspruch"),
    z("Anspruchsgrundlage: Gemeindeordnung", 110, 190, "rweg", "Bold", 32),
    z("= Sonderrecht der Stadt", 110, 240, beim("rweg", "Sonderrecht"), "ExtraBold", 34),
    blk(110, 330, 1040, 120, GRUEN, beim("rweg", "Verwaltungsrechtsweg"),
        [("Verwaltungsrechtsweg", "ExtraBold", 36, INK), ("§ 40 Abs. 1 S. 1 VwGO", "ExtraBold", 32, INK)]),
    zit("VG Gelsenkirchen, Beschl. v. 14.6.2024 – 15 L 888/24, Rn. 9–21", 110, 475, beim("rweg", "Verwaltungsrechtsweg")),
    *requisit([("rweg", ("tabler", "book", 100, WEISS), "Sonderrecht", WEISS),
               (beim("rweg", "Verwaltungsrechtsweg"), ("fluent-emoji-high-contrast", "classical-building", 110, BLAU),
                "Verwaltungsgericht", BLAU)]),
    *zwei([("rweg", "liest"), (beim("rweg", "Verwaltungsrechtsweg"), "entschlossen")], [("rweg", "ernst")]),
]))

# ===========================================================================================================================
# H Das Muster kehrt wieder: Förderkredit, Kita-Platz
# ===========================================================================================================================
PM = "Weitere Fälle"
folie([("weitere", f"{PM} · das Muster kehrt wieder"), ("kredit", f"{PM} › Förderkredit"),
       ("kita", f"{PM} › Kita-Platz: § 24 SGB VIII")], rechts_frei([
    *tafel("weitere", "Das Muster kehrt wieder"),
    z("Förderkredit", 110, 180, "kredit", "ExtraBold", 36),
    blk(110, 235, 500, 110, GELB, beim("kredit", "Bewilligung"), [("Ob: Bewilligung", "ExtraBold", 30, INK),
                                                                 ("öffentlich-rechtlich", "Bold", 28, INK)]),
    blk(650, 235, 500, 110, WEISS, beim("kredit", "Darlehensvertrag"), [("Wie: Darlehensvertrag", "ExtraBold", 30, INK),
                                                                       ("privatrechtlich", "Bold", 28, INK)]),
    zit("BVerwG, Beschl. v. 2.5.2007 – 6 B 10.07, Rn. 15 (Subvention)", 110, 360, beim("kredit", "Bewilligung")),
    z("Kita-Platz: Vorsicht", 110, 440, "kita", "ExtraBold", 36),
    blk(110, 495, 1040, 120, HELLROT, beim("kita", "eigener"), [("§ 24 SGB VIII: eigener Anspruch", "ExtraBold", 30, INK),
                                                               ("gegen den Träger der öffentlichen Jugendhilfe", "Bold", 28, INK)]),
    *okz("Betreuungsvertrag mit der Kita: ggf. privatrechtlich", 650, beim("kita", "Betreuungsvertrag"), "Bold", 30, x=160),
    zit("OVG Nds., Beschl. v. 15.12.2021 – 10 ME 170/21 (Leitsatz 1)", 160, 700, beim("kita", "Betreuungsvertrag")),
    *requisit([("weitere", ("tabler", "list-check", 100, WEISS), "Ob und Wie", WEISS),
               ("kredit", ("tabler", "coin-euro", 100, GELB), "Förderkredit", GELB),
               ("kita", ("tabler", "baby-carriage", 100, WEISS), "Kita-Platz", WEISS)]),
    *zwei([("weitere", "ruhig"), ("kita", "denkt")], [("weitere", "ruhig"), ("kredit", "froh"), ("kita", "ernst")]),
]))

# ===========================================================================================================================
# I Streitstand: Kritik an der Zweistufentheorie
# ===========================================================================================================================
PK = "Streitstand"
folie([("krit", f"{PK} · Die Zweistufentheorie ist umstritten"), ("k1", f"{PK} › Kritik: künstliche Aufspaltung"),
       ("k2", f"{PK} › Alternative: einheitlich behandeln"), ("k3", f"{PK} › BVerwG: nur bei zwei Phasen"),
       ("k4", f"{PK} › öffentliche Einrichtungen: Ob und Wie")], rechts_frei([
    *tafel("krit", "Streitstand: Kritik an der Zweistufentheorie"),
    pl("Meinung: Kritik aus der Lehre", 110, 170, "k1", fill=LILA, size=30),
    *neinz("künstliche Aufspaltung eines einheitlichen Vorgangs", 245, beim("k1", "künstlich"), "Bold", 30, x=160),
    *neinz("Grenze zwischen Ob und Wie oft unklar", 300, beim("k1", "unklar"), "Bold", 30, x=160),
    blk(110, 370, 1040, 110, LILA, "k2", [("Alternative: einheitlich behandeln,", "ExtraBold", 30, INK),
                                         ("z. B. durch öffentlich-rechtlichen Vertrag", "Bold", 28, INK)]),
    zit("vgl. § 54 S. 1 VwVfG", 110, 492, "k2"),
    *okz("BVerwG: nur bei echter Mehrphasigkeit", 560, "k3", "ExtraBold", 30, x=160),
    zit("BVerwG, Beschl. v. 2.5.2007 – 6 B 10.07, Rn. 15", 160, 606, "k3"),
    *okz("öffentliche Einrichtungen: Gerichte trennen Ob und Wie", 670, "k4", "ExtraBold", 30, x=160),
    zit("VG Gelsenkirchen, Beschl. v. 14.6.2024 – 15 L 888/24, Rn. 18–20", 160, 716, "k4"),
    *requisit([("krit", ("tabler", "scale", 100, WEISS), "umstritten", WEISS),
               ("k1", ("tabler", "arrows-split", 100, HELLROT), "künstlich geteilt?", HELLROT),
               ("k2", ("tabler", "writing-sign", 100, LILA), "ein Vertrag?", LILA),
               ("k3", ("fluent-emoji-high-contrast", "classical-building", 110, WEISS), "BVerwG", WEISS)]),
    *zwei([("krit", "denkt"), ("k3", "liest")], [("krit", "ernst"), ("k2", "denkt"), ("k4", "ruhig")]),
]))

# ===========================================================================================================================
# J1 Lösung des Falls
# ===========================================================================================================================
PL = "Lösung"
folie([("loes", f"{PL} · der Chor und die Stadthalle"), ("l1", f"{PL} › öffentliche Einrichtung der Stadt"),
       ("l2", f"{PL} › berechtigt, Widmung, Kapazität"), ("l3", f"{PL} › kein sachlicher Grund"),
       ("l4", f"{PL} › Einwirkungsanspruch gegen die Stadt")], rechts_frei([
    *tafel("loes", "Lösung: Bekommt der Chor den Saal?"),
    *okz("Stadthalle: öffentliche Einrichtung der Stadt", 180, "l1", "Bold", 32, x=160),
    z("auch wenn ihre GmbH sie betreibt", 160, 228, beim("l1", "auch"), size=28, farbe=TEXT),
    *okz("Chor: Verein aus der Stadt, berechtigt", 300, beim("l2", "berechtigt"), "Bold", 32, x=160),
    *okz("Konzert im Widmungszweck", 360, beim("l2", "Konzert"), "Bold", 32, x=160),
    *okz("Termin frei", 420, beim("l2", "Termin"), "Bold", 32, x=160),
    *neinz("sachlicher Grund für das Nein: fehlt", 490, "l3", "Bold", 32, x=160),
    blk(110, 570, 1040, 120, GRUEN, "l4", [("Anspruch gegen die Stadt auf Einwirkung", "ExtraBold", 32, INK),
                                          ("notfalls vor dem Verwaltungsgericht", "ExtraBold", 32, INK)]),
    zit("vgl. BVerwG, Urt. v. 20.1.2022 – 8 C 35.20, Rn. 14", 110, 715, "l4"),
    *requisit([("loes", ("tabler", "building-community", 110, GRUEN), "Stadthalle", GRUEN),
               ("l2", ("fluent-emoji-high-contrast", "musical-notes", 100, LILA), "Chor", LILA),
               ("l3", ("tabler", "ban", 100, HELLROT), "kein Grund", HELLROT),
               ("l4", ("fluent-emoji-high-contrast", "classical-building", 110, GRUEN), "Stadt muss einwirken", GRUEN)]),
    *zwei([("loes", "ruhig"), ("l2", "hofft"), ("l4", "entschlossen")], [("loes", "ruhig"), ("l3", "verlegen")]),
]))

# ===========================================================================================================================
# J2 zurück im Foyer: Frau Lammers und Herr Scheffler (Blasen)
# ===========================================================================================================================
folie([("la2", "Lösung · zurück im Foyer"), ("sc2", "Lösung · das Wie: der Mietvertrag")], [
    *foyer("la2"),
    hart(pl("Stadthalle · Foyer", 70, 30, "la2", fill=GRUEN, size=38)),
    *redet("LA_froh_redet_r", LAX, BODEN_Y, FHA, "la2", "sc2"),
    *fig("LA", LAX, BODEN_Y, FHA, [("sc2", "ruhig_r")], erst="cut"),
    hart(ns("Frau Lammers · Chor", LAX, BODEN_Y, "la2", NFARBE["LA"])),
    *fig("SC", SCX, BODEN_Y, FHA, [("la2", "denkt")], erst="cut", bis="sc2"),
    *redet("SC_freundlich_redet", SCX, BODEN_Y, FHA, "sc2", "tipp"),
    hart(ns("Herr Scheffler · GmbH", SCX, BODEN_Y, "la2", NFARBE["SC"])),
    blase("sprech", 900, 200, "la2", 1150, 220, inhalt=["Dann wende ich mich an die Stadt", "und nicht an die Gesellschaft."],
          textsize=34, figur=("LA_froh_redet_r", LAX, BODEN_Y, FHA), bis="sc2"),
    blase("sprech", 900, 200, "sc2", 1250, 220, inhalt=["Und den Mietvertrag schließen", "danach wir mit Ihnen."],
          textsize=34, figur=("SC_freundlich_redet", SCX, BODEN_Y, FHA), bis="tipp"),
    ficon("fluent-emoji-high-contrast", "page-facing-up", 1435, BODEN_Y - 200, 50, "sc2", fuell=WEISS),
])

# ===========================================================================================================================
# K Klausurtipp (Lexi)
# ===========================================================================================================================
els_k = [*tafel("tipp", "Klausurtipp: der richtige Gegner", fill=HELL), warnung_i(150, 225, "tipp", gr=26),
         z("Eigengesellschaft? Zuerst den Anspruchsgegner klären", 200, 200, "tipp", "Bold", 32),
         blk(130, 300, 1020, 120, GELB, "kt1", [("Zulassung: Klage gegen die Gemeinde,", "ExtraBold", 32, INK),
                                                ("gerichtet auf Einwirkung", "ExtraBold", 32, INK)]),
         blk(130, 460, 1020, 120, BLAU, "kt2", [("Streit über das Ob: Verwaltungsgericht", "ExtraBold", 32, INK),
                                                ("Streit über den Mietvertrag: Zivilgericht", "ExtraBold", 32, INK)]),
         *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
         ns("Lexi", FX, FB, "tipp", GELB, d=0.2)]
folie([("tipp", "Klausurtipp · zuerst den Anspruchsgegner prüfen"), ("kt1", "Klausurtipp › Klage gegen die Gemeinde"),
       ("kt2", "Klausurtipp › Ob und Wie trennen")], els_k)

# ===========================================================================================================================
# L Prüfschema (Aufbau Punkt für Punkt)
# ===========================================================================================================================
REIHEN = [("q1", 0, "I. Verwaltungsrechtsweg, § 40 Abs. 1 S. 1 VwGO: Streit um das Ob"),
          ("q2", 0, "II. Zulassungsanspruch aus der Gemeindeordnung (z. B. § 8 Abs. 2, 4 GO NRW)"),
          ("q2a", 1, "1. öffentliche Einrichtung"),
          ("q2b", 1, "2. berechtigter Nutzer (Einwohner, Verein mit Sitz in der Gemeinde)"),
          ("q2c", 1, "3. Widmung und Kapazität"),
          ("q2d", 1, "4. Gleichbehandlung, Art. 3 Abs. 1 GG"),
          ("q3", 0, "III. Betrieb durch Gesellschaft: Einwirkungsanspruch gegen die Gemeinde"),
          ("q4", 0, "IV. das Wie: Mietvertrag (Privatrecht, Zivilgericht)")]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Prüfschema: Zulassung zur öffentlichen Einrichtung"), 110, 90, "sch", 46)]
y = 200
for c, ebene, text in REIHEN:
    x = (130, 200)[ebene]
    els_sch.append(z(text, x, y, c, ("ExtraBold", "Bold")[ebene], (38, 34)[ebene], rechts=1800, farbe=INK))
    y += {0: 96, 1: 76}[ebene]
assert y <= 960, y
folie([("sch", "Prüfschema"), ("q1", "Prüfschema › I. Verwaltungsrechtsweg"), ("q2", "Prüfschema › II. Zulassungsanspruch"),
       ("q2a", "Prüfschema › II. 1. öffentliche Einrichtung"), ("q2b", "Prüfschema › II. 2. berechtigter Nutzer"),
       ("q2c", "Prüfschema › II. 3. Widmung und Kapazität"), ("q2d", "Prüfschema › II. 4. Gleichbehandlung"),
       ("q3", "Prüfschema › III. Einwirkungsanspruch"), ("q4", "Prüfschema › IV. das Wie")], els_sch)

# ===========================================================================================================================
# M Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Über das ", 0), ("Ob", "a"), (" entscheidet das", 0)], [("öffentliche Recht,", 0)],
                 [("über das ", 0), ("Wie", "b"), (" oft das Privatrecht.", 0)]], 750, 290, 42, "merke",
                {"a": beim("merke", "Ob"), "b": beim("merke", "Wie")}),
    *markertext([[("Schiebt die Stadt eine Gesellschaft vor,", 0)], [("bleibt sie selbst in der ", 0), ("Pflicht", "c"), (".", 0)]],
                750, 600, 42, "mk2", {"c": beim("mk2", "Pflicht")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
