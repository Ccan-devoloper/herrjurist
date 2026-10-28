"""Folge 201 · Lernplan Examen: So teilst du 12 Monate Vorbereitung ein – Serienstandard Open Peeps (Katzenkönig).
Rahmen: Fenna (Jurastudentin in Nordrhein-Westfalen) steht ein Jahr vor den Klausuren der staatlichen Pflichtfachprüfung vor
einem leeren Wandkalender in der WG-Küche; Nils (Referendar) plant mit ihr rückwärts. Szenen laut ../SZENENPLAN.md:
A1 Küche (Wandkalender), A2 Einstieg, B Sachverhalt, C1 Schritt 1 Pflichtfächer (Wortlautkarte § 5a Abs. 2 S. 3 DRiG),
C2 Landesrecht/NRW (§§ 10, 11, 13 JAG NRW), C3 Ampel, D Schritt 2 rückwärts planen (12-Monats-Tafel, Freiversuch § 5d
Abs. 5 DRiG), E Schritt 3 Stoffphase, F Schritt 4 Wiederholung, G Schritt 5 Klausuren (Nils), H Schritt 6 Puffer/Endspurt
(Fenna, Nils), I Beispielwoche (Wochenplan), J Ergebnis (Plan an der Wand, Reißzwecke), K Klausurtipp (Lexi),
L Lernplan als Schema I.–VI., M Merksatz (Lexi).
Die 12-Monats-Tafel (12 Monatsspalten, Bahnen Stoff/Wiederholung/Klausuren) kehrt in D–H im jeweils erreichten Stand wieder
(Zwiebelschale) und hängt am Ende als „Lernplan“ an der Wand.
Handlungsgeräusch: Reißzwecke, als der Plan an die Wand kommt (J); ../geraeusche_herkunft.json.
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz
als eigene Kopie aus Folge 200 (gemeinsame Dateien unverändert); neu: brett_grund(), zelle(), brett(), wandkalender(),
klausuren(), ampelzeile(), tzelle().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut § 5a Abs. 2 S. 3 DRiG nach gesetze-im-internet.de, Abruf 06.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave
import datetime as _dt

bausteine.FIGORDNER = "op_201/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_201/" in n:
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
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 06.10.2026), als Zitat mit Normangabe; der
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
NAME = {"FE": "Fenna", "NI": "Nils"}
NFARBE = {"FE": TUERKIS, "NI": BLAU}


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


def zwei(folge_l, folge_r, links="FE", rechts="NI"):
    """Zwei Figuren rechts neben der Tafel (blicken nach links zur Tafel)."""
    return [*stehend(links, X1, folge_l), *stehend(rechts, X2, folge_r)]


def allein(k, folge):
    return stehend(k, FX, folge)





def ticon(*a, **k):
    """Icon als Teil einer Tafelgrafik (darf in der Tafel stehen, rechts_frei() prüft nur Requisiten neben der Tafel)."""
    e = ficon(*a, **k)
    e.name = "tafelicon:" + e.name.split(":", 1)[1]
    return e


# --- eigene Szenenbausteine Folge 201 ----------------------------------------------------------------------------------------
HGELB = (253, 240, 196, 255)
HROT = (252, 214, 206, 255)
SPURT = (255, 226, 196, 255)                 # Endspurt
GRAU2 = (232, 232, 228, 255)                 # Stoff, noch ohne Gebiet
FZR, FOR, FSR = BLAU, GRUEN, ROT             # Zivilrecht, Öffentliches Recht, Strafrecht (durchgehend gleiche Farben)
FWDH, FKL, FPUF = LILA, PINK, GELB           # Wiederholung, Klausuren, Puffer

# 12-Monats-Tafel (Gantt): 12 Monatsspalten, drei Bahnen
CX0, CW = 318, 71                            # Spalte 1 beginnt bei x = 318, je 71 px → Spalte 12 endet bei 1170
ZAHL_Y = 196                                 # Monatszahlen
BAHN = {"stoff": (240, 110), "wdh": (362, 70), "kl": (444, 70)}   # (oben, Höhe)
BLABEL = {"stoff": "Stoff", "wdh": "Wiederholung", "kl": "Klausuren"}
ANM = [612, 660, 708, 756, 804]              # Zeilen unter der Tafel-Grafik


def spx(m):
    return CX0 + (m - 1) * CW


def brett_grund(c):
    """Raster: Monatszahlen 1–12, drei leere Bahnen mit Beschriftung (programmatisch, Tuschekontur)."""
    w, h = 1170 - 100, 530 - 180
    def zz(dr, s):
        f = F("Bold", 28 * s); fl = F("Bold", 28 * s)
        dr.text(((110 - 100) * s, (ZAHL_Y - 180) * s), glyphen("Monat"), font=f, fill=TEXT)
        for m in range(1, 13):
            x = spx(m) - 100 + CW / 2
            dr.text((x * s, (ZAHL_Y - 180 + 16) * s), str(m), font=f, fill=INK, anchor="mm")
        for k, (o, hh) in BAHN.items():
            dr.text(((110 - 100) * s, (o - 180 + hh / 2) * s), glyphen(BLABEL[k]), font=fl, fill=INK, anchor="lm")
            for m in range(1, 13):
                x0 = spx(m) - 100
                dr.rectangle((x0 * s, (o - 180) * s, (x0 + CW) * s, (o - 180 + hh) * s), fill=(250, 250, 247, 255),
                             outline=(190, 190, 186, 255), width=2 * s)
            dr.rectangle(((CX0 - 100) * s, (o - 180) * s, (1170 - 100) * s, (o - 180 + hh) * s), outline=INK, width=4 * s)
    assert 110 + F("Bold", 28).getlength("Wiederholung") <= CX0 - 10
    return El(_flaeche(w, h, zz), 100, 180, c, "fade", 0.0, None, name="brett")


def zelle(c, bahn, von, bis_m, fill, text=None, size=28, icon=None, anim="pop", bis=None):
    """Farbfeld über die Monate von..bis_m in einer Bahn, Text (eine oder zwei Zeilen) mittig; Zahlen als Ziffern."""
    o, hh = BAHN[bahn]
    x0, x1 = spx(von), spx(bis_m) + CW
    w, h = x1 - x0, hh
    zeilen = text.split("\n") if text else []
    for t in zeilen:
        assert size >= 26 and F("ExtraBold", size).getlength(glyphen(t)) <= w - 12, f"Zelle zu schmal: {t}"
    def zz(dr, s):
        dr.rounded_rectangle((2 * s, 2 * s, (w - 2) * s, (h - 2) * s), 8 * s, fill=fill, outline=INK, width=4 * s)
        lh = size * 1.1
        y0 = h / 2 - lh * len(zeilen) / 2 + lh / 2
        for i, t in enumerate(zeilen):
            dr.text((w / 2 * s, (y0 + i * lh) * s), t, font=F("ExtraBold", size * s), fill=INK, anchor="mm")
    els = [El(_flaeche(w, h, zz), x0, o, c, anim, 0.0, bis, name=f"zelle:{bahn}:{von}-{bis_m}:{text}")]
    if icon:
        s_, n_, br = icon
        els.append(ticon(s_, n_, (x0 + x1) / 2, o + hh - 16, br, c, fuell=WEISS, anim=anim, bis=bis))
    return els


def examen(c, anim="pop"):
    return [ticon("tabler", "flag", spx(12) + CW / 2, 585, 56, c, fuell=ROT, anim=anim),
            pl("Examen", spx(11) - 30, 538, c, fill=HROT, size=28, anker="m", anim=anim)]


def puffer(c, anim="pop"):
    return zelle(c, "stoff", 10, 10, FPUF, icon=("tabler", "lifebuoy", 46), anim=anim)


def endspurt(c, anim="pop"):
    return [*zelle(c, "stoff", 11, 12, SPURT, "Endspurt", 26, anim=anim), *zelle(c, "wdh", 11, 12, FWDH, anim=anim),
            *zelle(c, "kl", 11, 12, FKL, anim=anim)]


def gebiete(c, anim="pop", nur=None):
    teile = {"zr": (1, 4, FZR, "Zivilrecht", 28), "oer": (5, 7, FOR, "Öffentliches\nRecht", 28),
             "sr": (8, 9, FSR, "Strafrecht", 26)}
    els = []
    for k, (a, b, f, t, g) in teile.items():
        if nur is None or k == nur:
            els += zelle(c, "stoff", a, b, f, t, g, anim=anim)
    return els


def brett(c, stand):
    """Der Plan im aktuellen Stand, hart ab Folienbeginn (Zwiebelschale: gleiche Tafel, neue Einträge)."""
    els = [hart(brett_grund(c)), *[hart(e) for e in examen(c)]]
    if "puffer" in stand:
        els += [hart(e) for e in puffer(c)]
    if "endspurt" in stand:
        els += [hart(e) for e in endspurt(c)]
    if "stoff" in stand:
        els += [hart(e) for e in zelle(c, "stoff", 1, 9, GRAU2, "Stoff: 9 Monate", 28)]
    if "gebiete" in stand:
        els += [hart(e) for e in gebiete(c)]
    if "wdh" in stand:
        els += [hart(e) for e in zelle(c, "wdh", 1, 10, FWDH, "jeden Tag die 1. Stunde", 28)]
    if "kl" in stand:
        els += [hart(e) for e in zelle(c, "kl", 1, 10, FKL, "1 Klausur pro Woche", 28)]
    return els


def anm(text, i, c, stil="Bold", size=30, **k):
    return z(text, 110, ANM[i], c, stil, size, **k)


# --- WG-Küche: Wandkalender, Tisch, Bücher, Tassen ----------------------------------------------------------------------------
KAL = (110, 360, 480, 400)                   # Wandkalender: x, y, w, h
FEX, NIX = 760, 1600                         # Fenna, Nils in der Küche
TISCH = (900, 1330)


def wandkalender(c, leer=True):
    x, y, w, h = KAL
    def zz(dr, s):
        dr.rounded_rectangle((3 * s, 20 * s, (w - 3) * s, (h - 3) * s), 14 * s, fill=WEISS, outline=INK, width=5 * s)
        dr.rectangle((5 * s, 22 * s, (w - 5) * s, 80 * s), fill=ROT)
        dr.line((3 * s, 80 * s, (w - 3) * s, 80 * s), fill=INK, width=4 * s)
        for rx in (w * 0.3, w * 0.7):
            dr.rounded_rectangle(((rx - 7) * s, 4 * s, (rx + 7) * s, 40 * s), 6 * s, fill=(180, 180, 180, 255), outline=INK, width=3 * s)
        if leer:
            dr.text((w / 2 * s, 51 * s), glyphen("Kalender"), font=F("ExtraBold", 32 * s), fill=INK, anchor="mm")
            for i in range(12):
                cx, cy = 26 + (i % 4) * 109, 100 + (i // 4) * 96
                dr.rounded_rectangle((cx * s, cy * s, (cx + 94) * s, (cy + 80) * s), 8 * s, fill=(250, 250, 247, 255),
                                     outline=INK, width=3 * s)
                dr.text(((cx + 10) * s, (cy + 6) * s), str(i + 1), font=F("Bold", 26 * s), fill=TEXT)
        else:                                 # fertiger Plan: 12 Spalten, drei Bahnen in den Planfarben
            dr.text((w / 2 * s, 51 * s), glyphen("Lernplan"), font=F("ExtraBold", 32 * s), fill=INK, anchor="mm")
            cw = (w - 40) / 12; x0 = 20
            for m in range(12):
                dr.text(((x0 + m * cw + cw / 2) * s, 112 * s), str(m + 1), font=F("Bold", 26 * s), fill=INK, anchor="mm")
            reihen = [(140, 110, [(0, 4, FZR), (4, 7, FOR), (7, 9, FSR), (9, 10, FPUF), (10, 12, SPURT)]),
                      (262, 50, [(0, 12, FWDH)]), (324, 50, [(0, 12, FKL)])]
            for oy, hh, teile in reihen:
                for a, b, f in teile:
                    dr.rounded_rectangle(((x0 + a * cw + 2) * s, oy * s, (x0 + b * cw - 2) * s, (oy + hh) * s), 6 * s,
                                         fill=f, outline=INK, width=3 * s)
    return El(_flaeche(w, h, zz), x, y, c, "cut", 0.0, None, name="wandkalender:" + ("leer" if leer else "plan"))


def kueche(c, kalender_leer=True, tassen=False):
    els = [boden(c), hart(wandkalender(c, kalender_leer)), schreibtisch(c, *TISCH),
           hart(ficon("tabler", "books", 990, BODEN_Y - 170, 130, c, fuell=GELB, anim="cut"))]
    if tassen:
        els += [hart(ficon("tabler", "coffee", 1150, BODEN_Y - 170, 70, c, fuell=WEISS, anim="cut")),
                hart(ficon("tabler", "coffee", 1235, BODEN_Y - 170, 70, c, fuell=WEISS, anim="cut"))]
    return els


# ===========================================================================================================================
# A1 Fall: ein Jahr vor dem Examen – der leere Wandkalender, Nils kommt dazu
# ===========================================================================================================================
FE_A = ("FE_redet", FEX, BODEN_Y, FHA)
NI_A = ("NI_redet", NIX, BODEN_Y, FHA)
folie([(NULL, "Fall · Noch 1 Jahr bis zum Examen"), ("f1", "Fall · Womit fängt Fenna an?"), ("nils", "Fall · Nils kommt dazu"),
       ("n1", "Fall · Rückwärts planen, vom Examen aus")], [
    boden(NULL),
    hart(wandkalender(NULL)),
    schreibtisch(NULL, *TISCH),
    hart(pl("Noch 1 Jahr bis zum Examen", 70, 30, NULL, fill=GELB, size=38)),
    pl("leer", KAL[0] + KAL[2] / 2, KAL[1] + KAL[3] + 10, beim("fenna", "leeren"), fill=HGELB, size=30, anker="m"),
    ficon("tabler", "books", 990, BODEN_Y - 170, 130, beim("stapel", "Stapel"), fuell=GELB),
    peep_voll("FE_ratlos", FEX, BODEN_Y, FHA, NULL, anim="cut", bis="f1"),
    *redet("FE_redet", FEX, BODEN_Y, FHA, "f1", "nils"),
    *fig("FE", FEX, BODEN_Y, FHA, [("nils", "denkt"), (beim("n1", "Ende"), "ruhig_r")], erst="cut"),
    hart(ns(NAME["FE"], FEX, BODEN_Y, NULL, NFARBE["FE"])),
    blase("sprech", 600, 190, "f1", 560, 230, inhalt=["12 Monate, 3 Rechtsgebiete.", "Womit fange ich bloß an?"], textsize=34,
          figur=FE_A, bis="nils"),
    *fig("NI", NIX, BODEN_Y, FHA, [(beim("nils", "Nils"), "froh")], erst="pop", bis="n1"),
    ns(NAME["NI"], NIX, BODEN_Y, beim("nils", "Nils"), NFARBE["NI"], d=0.1),
    pl("Examen im letzten Jahr geschrieben", 1450, 300, beim("nils", "Examen"), fill=WEISS, size=28, anker="m", bis=beim("tassen", "Tassen")),
    ficon("tabler", "coffee", 1150, BODEN_Y - 170, 70, beim("tassen", "Tassen"), fuell=WEISS),
    ficon("tabler", "coffee", 1235, BODEN_Y - 170, 70, beim("tassen", "Tassen"), fuell=WEISS, d=0.15),
    *redet("NI_redet", NIX, BODEN_Y, FHA, "n1", "hook"),
    blase("sprech", 620, 190, "n1", 1230, 230, inhalt=["Mit dem Ende. Wir planen", "rückwärts, vom Examen aus."], textsize=34,
          figur=NI_A, bis="hook"),
])

# ===========================================================================================================================
# A2 Einstieg: Womit fängst du an?
# ===========================================================================================================================
folie([("hook", "Einstieg · Examen in 1 Jahr: Womit fängst du an?"), (beim("hook2", "Plan"), "Einstieg › nicht das 1. Kapitel, sondern ein Plan"),
       ("sechs", "Einstieg › 6 Schritte, Monat für Monat")], rechts_frei([
    *tafel("hook", "Examen in 1 Jahr: Womit fängst du an?"),
    *neinz("mit dem ersten Kapitel", 230, beim("hook2", "Kapitel"), "Bold", 38, x=170),
    *okz("mit einem Plan", 310, beim("hook2", "Plan"), "Bold", 38, x=170),
    blk(110, 420, 1040, 90, GELB, "sechs", [("6 Schritte, Monat für Monat", "ExtraBold", 40, INK)]),
    *[pl(str(i), 160 + (i - 1) * 170, 570, ("sechs", 0.25 + 0.12 * i), fill=(FZR, FOR, FSR, FWDH, FKL, FPUF)[i - 1], size=40)
      for i in range(1, 7)],
    *requisit([("hook", ("tabler", "calendar", 110, WEISS), "1 Jahr", WEISS),
               (beim("hook2", "Kapitel"), ("tabler", "book", 100, WEISS), "1. Kapitel?", HROT),
               (beim("hook2", "Plan"), ("tabler", "list-check", 100, HELLGRUEN), "Plan", HELLGRUEN)]),
    *zwei([("hook", "ratlos"), (beim("hook2", "Plan"), "denkt"), ("sechs", "froh")], [("hook", "ruhig"), ("sechs", "froh")]),
]))

# ===========================================================================================================================
# B Sachverhalt (Ausgangslage)
# ===========================================================================================================================
def sachverhalt_201(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 220
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=40, zeilenabstand=1.32)
        els += e; y += 22
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 14, cue, fill=PINK, size=38))
    folie([(cue, "Sachverhalt · Die Ausgangslage von Fenna")], els)


sachverhalt_201("sv", [
    "Fenna studiert Jura in Nordrhein-Westfalen. In 12 Monaten will sie die Klausuren der staatlichen "
    "Pflichtfachprüfung schreiben.",
    "Die Vorlesungen hat sie gehört. Eine Klausur über 5 Stunden hat sie noch nie geschrieben.",
    "Im Strafrecht fühlt sie sich sicher, im Zivilrecht halbwegs, im Öffentlichen Recht kaum.",
    "Sie kann an 6 Tagen pro Woche lernen; 1 Tag soll frei bleiben.",
], "Wie teilt Fenna die 12 Monate ein?")

# ===========================================================================================================================
# C1 Schritt 1: Bestandsaufnahme – Pflichtfächer, § 5a Abs. 2 S. 3 DRiG (Wortlaut)
# ===========================================================================================================================
S1 = "Schritt 1"
W5A = ("„… Pflichtfächer sind die Kernbereiche des Bürgerlichen Rechts, des Strafrechts, des Öffentlichen Rechts und des "
       "Verfahrensrechts einschließlich der europarechtlichen Bezüge, der rechtswissenschaftlichen Methoden und der "
       "philosophischen, geschichtlichen und gesellschaftlichen Grundlagen; …“")
w5a, w5a_y = wortlaut(80, 290, 1100, W5A, "§ 5a Abs. 2 S. 3 DRiG", "p5a", marken=[
    ("Bürgerlichen Rechts", beim("p5aw", "Bürgerlichen")), ("Strafrechts", beim("p5aw", "Strafrechts")),
    ("Öffentlichen Rechts", beim("p5aw", "Öffentlichen")), ("Verfahrensrechts", beim("p5aw", "Verfahrensrechts")),
    ("europarechtlichen Bezüge", beim("p5ae", "europarechtliche")), ("Methoden", beim("p5ae", "Methoden")),
    ("Grundlagen", beim("p5ae", "Grundlagen"))], size=30)
folie([("s1", f"{S1} · Bestandsaufnahme: Was wird geprüft?"), ("drig", f"{S1} › Rahmen: Deutsches Richtergesetz"),
       ("p5aw", f"{S1} › Pflichtfächer, § 5a Abs. 2 S. 3 DRiG"), ("p5ae", f"{S1} › dazu Europarecht, Methoden, Grundlagen")], rechts_frei([
    *tafel("s1", "Schritt 1: Bestandsaufnahme"),
    z("Was wird geprüft?", 110, 172, "s1", "Bold", 36),
    z("Rahmen: Deutsches Richtergesetz (DRiG)", 110, 226, "drig", "Regular", 34),
    *w5a,
    *requisit([("s1", ("tabler", "zoom-question", 100, WEISS), "Was wird geprüft?", WEISS),
               ("drig", ("tabler", "book", 100, WEISS), "DRiG", WEISS),
               ("p5aw", ("tabler", "list-check", 100, HELLGRUEN), "Pflichtfächer", HELLGRUEN)]),
    *allein("FE", [("s1", "ruhig"), ("p5aw", "denkt"), ("p5ae", "ruhig")]),
]))
assert w5a_y <= 880, w5a_y

# ===========================================================================================================================
# C2 Schritt 1: Landesrecht – Beispiel Nordrhein-Westfalen (§§ 10, 11, 13 JAG NRW)
# ===========================================================================================================================
def klausuren(c, x, n, fill, label, w=150, gap=14):
    els = []
    for i in range(n):
        xx = x + i * (w + gap)
        def zz(dr, s, f_=fill):
            dr.rounded_rectangle((3 * s, 3 * s, (w - 3) * s, (120 - 3) * s), 14 * s, fill=f_, outline=INK, width=5 * s)
        els.append(El(_flaeche(w, 120, zz), xx, 290, (c, 0.12 * i), "pop", 0.0, None, name=f"klausur:{label}:{i}"))
        els.append(ticon("tabler", "file-text", xx + w / 2, 395, 70, (c, 0.12 * i), fuell=WEISS))
    gb = n * w + (n - 1) * gap
    lab = z(label, 0, 425, c, "Bold", 30)
    lab.x = int(x + gb / 2 - lab.sprite.width / 2)
    assert lab.sprite.width <= gb + 10, label
    return els + [lab], x + gb


kz, xe = klausuren("nrw3", 120, 3, FZR, "Zivilrecht")
ko, xe = klausuren("nrw2", xe + 30, 2, FOR, "Öffentliches Recht")
ks, xe = klausuren("nrw1", xe + 30, 1, FSR, "Strafrecht")
assert xe <= 1170, xe
folie([("land", f"{S1} › Das Nähere regelt das Landesrecht"), ("nrw", f"{S1} › Beispiel Nordrhein-Westfalen: 6 Klausuren"),
       ("fuenf", f"{S1} › je 5 Stunden"), ("katalog", f"{S1} › Stoffkatalog, § 11 Abs. 2 JAG NRW"),
       ("eigen", f"{S1} › dein Land, deine Prüfungsordnung")], rechts_frei([
    *tafel("land", "Das Nähere regelt das Landesrecht"),
    zit("§ 5a Abs. 4, § 5d Abs. 6 S. 1 DRiG", 110, 168, "land", size=28),
    z("Fenna in Nordrhein-Westfalen: 6 Klausuren", 110, 222, "nrw", "Bold", 34),
    *kz, *ko, *ks,
    z("jede Klausur: 5 Stunden", 110, 490, "fuenf", "Bold", 34),
    zit("§ 10 Abs. 2, § 13 Abs. 1 S. 1 JAG NRW", 110, 542, "fuenf", size=28),
    blk(110, 600, 1040, 76, HELLGRUEN, "katalog", [("Stoffkatalog: § 11 Abs. 2 JAG NRW", "ExtraBold", 34, INK)]),
    z("Dein Land: Ausbildungsgesetz oder Prüfungsordnung", 110, 712, "eigen", "Bold", 32),
    *requisit([("land", ("tabler", "map-pin", 100, ROT), "Landesrecht", WEISS),
               ("fuenf", ("tabler", "clock", 100, WEISS), "5 Stunden", WEISS),
               ("katalog", ("tabler", "list-check", 100, HELLGRUEN), "Checkliste", HELLGRUEN),
               ("eigen", ("tabler", "map-pin", 100, GELB), "dein Land", GELB)]),
    *allein("FE", [("land", "ruhig"), ("nrw3", "denkt"), ("katalog", "entschlossen")]),
]))

# ===========================================================================================================================
# C3 Schritt 1: die Ampel
# ===========================================================================================================================
def ampelzeile(c, y, farbe, hell, text):
    def zz(dr, s):
        dr.ellipse((4 * s, 4 * s, 66 * s, 66 * s), fill=farbe, outline=INK, width=5 * s)
    return [blk(110, y, 1040, 96, hell, c, [(text, "ExtraBold", 38, INK)]),
            El(_flaeche(70, 70, zz), 1060, y + 13, c, "pop", 0.0, None, name="ampel:" + text)]


folie([("ampel", f"{S1} › die Ampel"), ("agruen", f"{S1} › Ampel: Strafrecht grün"), ("agelb", f"{S1} › Ampel: Zivilrecht gelb"),
       ("arot", f"{S1} › Ampel: Öffentliches Recht rot")], rechts_frei([
    *tafel("ampel", "Schritt 1: die Ampel"),
    z("Jedes Gebiet bekommt eine Ampelfarbe:", 110, 180, "ampel", "Regular", 34),
    *ampelzeile(beim("agruen", "Strafrecht"), 260, (60, 170, 90, 255), HELLGRUEN, "Strafrecht"),
    *ampelzeile(beim("agelb", "Zivilrecht"), 390, GELB, HGELB, "Zivilrecht"),
    *ampelzeile(beim("arot", "Öffentliche"), 520, ROT, HROT, "Öffentliches Recht"),
    *requisit([("ampel", ("fluent-emoji-high-contrast", "vertical-traffic-light", 70, WEISS), "Ampel", WEISS)]),
    *allein("FE", [("ampel", "denkt"), ("agruen", "froh"), ("agelb", "ruhig"), ("arot", "ratlos")]),
]))

# ===========================================================================================================================
# D Schritt 2: rückwärts planen – die 12 Monate
# ===========================================================================================================================
S2 = "Schritt 2"
folie([("s2", f"{S2} · rückwärts planen"), ("monate", f"{S2} › 12 Monate"), ("ex", f"{S2} › Examen am Ende von Monat 12"),
       ("fv", f"{S2} › Freiversuch, § 5d Abs. 5 S. 2 DRiG"), ("frist", f"{S2} › Meldefrist: Landesrecht"),
       ("acht", f"{S2} › Endspurt: 8 Wochen"), ("puf", f"{S2} › 1 Puffermonat"), ("neun", f"{S2} › 9 Monate Stoff")], rechts_frei([
    *tafel("s2", "Schritt 2: rückwärts planen"),
    brett_grund(beim("monate", "Zwölf")),
    *examen(beim("ex", "Examen")),
    bis_(anm("Freiversuch: frühzeitig melden, alles mitschreiben", 0, beim("fv", "frühzeitig")), "end"),
    bis_(zit("§ 5d Abs. 5 S. 2 DRiG: gilt dann als nicht unternommen", 110, ANM[1], beim("fv", "unternommen"), size=28), "end"),
    bis_(anm("Meldefrist: regelt dein Land", 2, "frist"), "end"),
    bis_(zit("§ 5d Abs. 5 S. 3 DRiG", 110, ANM[3], "frist", size=28), "end"),
    pfeil(spx(12) + CW - 8, 172, CX0 + 10, 172, beim("end", "zurück"), breite=7, kopf=24),
    *endspurt(beim("acht", "acht")),
    anm("Endspurt: 8 Wochen Wiederholung und Klausuren", 0, beim("acht", "acht")),
    *puffer(beim("puf", "Puffermonat")),
    anm("davor: 1 Puffermonat", 1, beim("puf", "Puffermonat")),
    *zelle(beim("neun", "Stoff"), "stoff", 1, 9, GRAU2, "Stoff: 9 Monate", 28),
    anm("bleiben 9 Monate für den Stoff", 2, beim("neun", "neun")),
    *requisit([("s2", ("tabler", "calendar", 110, WEISS), "12 Monate", WEISS),
               ("fv", ("tabler", "file-certificate", 100, HGELB), "Freiversuch", HGELB),
               ("end", ("tabler", "flag", 100, ROT), "vom Termin zurück", WEISS)]),
    *zwei([("s2", "ruhig"), ("fv", "denkt"), ("neun", "froh")], [("s2", "ruhig"), ("acht", "froh")]),
]))

# ===========================================================================================================================
# E Schritt 3: die Stoffphase
# ===========================================================================================================================
S3 = "Schritt 3"
folie([("s3", f"{S3} · die Stoffphase"), ("gew", f"{S3} › Empfehlung, keine Regel"),
       ("gew2", f"{S3} › nach Gewicht in der Prüfung und Ampel"), ("zr", f"{S3} › Zivilrecht: 4 Monate"),
       ("oer", f"{S3} › Öffentliches Recht: 3 Monate"), ("sr", f"{S3} › Strafrecht: 2 Monate"),
       ("proz", f"{S3} › Prozessrecht im jeweiligen Block")], rechts_frei([
    *tafel("s3", "Schritt 3: die Stoffphase"),
    *brett("s3", {"puffer", "endspurt"}),
    *[hart(bis_(e, beim("zr", "Zivilrecht"))) for e in zelle("s3", "stoff", 1, 9, GRAU2, "Stoff: 9 Monate", 28)],
    *[bis_(e, beim("oer", "Öffentliche")) for e in zelle(beim("zr", "Zivilrecht"), "stoff", 5, 9, GRAU2, anim="cut")],
    *[bis_(e, beim("sr", "Strafrecht")) for e in zelle(beim("oer", "Öffentliche"), "stoff", 8, 9, GRAU2, anim="cut")],
    anm("Empfehlung, keine Regel", 0, beim("gew", "Empfehlung")),
    *gebiete(beim("zr", "Zivilrecht"), nur="zr"),
    anm("Zivilrecht: 4 Monate, die Hälfte der Klausuren", 1, beim("zr", "Zivilrecht")),
    *gebiete(beim("oer", "Öffentliche"), nur="oer"),
    anm("Öffentliches Recht: 3 Monate, Ampel rot", 2, beim("oer", "Öffentliche")),
    *gebiete(beim("sr", "Strafrecht"), nur="sr"),
    anm("Strafrecht: 2 Monate", 3, beim("sr", "Strafrecht")),
    anm("Prozessrecht: im jeweiligen Block", 4, beim("proz", "Prozessrecht")),
    *requisit([("s3", ("tabler", "books", 120, GELB), "9 Monate Stoff", WEISS),
               ("gew2", ("tabler", "scale", 100, WEISS), "Prüfungsgewicht und Ampel", WEISS),
               ("proz", ("tabler", "gavel", 100, WEISS), "Prozessrecht", WEISS)]),
    *allein("FE", [("s3", "ruhig"), ("gew2", "denkt"), ("zr", "entschlossen"), ("sr", "froh")]),
]))

# ===========================================================================================================================
# F Schritt 4: das Wiederholungssystem
# ===========================================================================================================================
S4 = "Schritt 4"
folie([("s4", f"{S4} · das Wiederholungssystem"), ("abruf", f"{S4} › später noch abrufen können"),
       ("faust", f"{S4} › Faustregel: wachsende Abstände"), ("i3", f"{S4} › nach 1 Tag, 1 Woche, 1 Monat"),
       ("karte", f"{S4} › Karteikarten und Schemata"), ("kopf", f"{S4} › aus dem Kopf, dann mit dem Gesetz vergleichen"),
       ("stunde", f"{S4} › jeden Tag die 1. Stunde"), ("alt", f"{S4} › auch fertige Gebiete")], rechts_frei([
    *tafel("s4", "Schritt 4: wiederholen"),
    *brett("s4", {"puffer", "endspurt", "gebiete"}),
    anm("Faustregel: in wachsenden Abständen", 0, beim("faust", "Faustregel")),
    pl("nach 1 Tag", 110, ANM[1], beim("i1", "Tag"), fill=FWDH, size=28),
    pl("nach 1 Woche", 330, ANM[1], beim("i2", "Woche"), fill=FWDH, size=28),
    pl("nach 1 Monat", 580, ANM[1], beim("i3", "Monat"), fill=FWDH, size=28),
    z("Schema aus dem Kopf, dann mit dem Gesetz vergleichen", 110, 732, beim("kopf", "Schema"), "Bold", 30),
    zit("Video „Prüfungsschemata lernen“: Folge 123", 110, 778, beim("kopf", "hundert"), size=28),
    *zelle(beim("stunde", "erste"), "wdh", 1, 10, FWDH, "jeden Tag die 1. Stunde", 28),
    z("auch für Gebiete, die schon fertig sind", 110, 826, beim("alt", "fertig"), "Bold", 30),
    *requisit([("s4", ("tabler", "repeat", 100, LILA), "Wiederholung", WEISS),
               ("abruf", ("tabler", "brain", 100, WEISS), "abrufen können", WEISS),
               ("karte", ("tabler", "cards", 100, LILA), "Karteikarten und Schemata", WEISS),
               ("stunde", ("tabler", "clock", 100, LILA), "1. Stunde: Wiederholung", WEISS)]),
    *allein("FE", [("s4", "ruhig"), ("abruf", "denkt"), ("karte", "entschlossen"), ("alt", "froh")]),
]))

# ===========================================================================================================================
# G Schritt 5: Klausuren von Anfang an (Nils, Verweise 045 und 117)
# ===========================================================================================================================
S5 = "Schritt 5"
NI_G = ("NI_redet2", X2, FB, FR)
folie([("s5", f"{S5} · Klausuren von Anfang an"), ("woche", f"{S5} › ab der 1. Woche: jede Woche 1 Klausur"),
       ("bed", f"{S5} › Examensbedingungen: 5 Stunden am Stück"), ("frueh", f"{S5} › auch wenn noch Stoff fehlt"),
       ("korr", f"{S5} › korrigieren lassen"), ("n2", f"{S5} › Nils: Fehler notieren"),
       ("v045", f"{S5} › Zeitplan in der Klausur: Folge 045"), ("v117", f"{S5} › typische Fehler: Folge 117")], rechts_frei([
    *tafel("s5", "Schritt 5: Klausuren von Anfang an"),
    *brett("s5", {"puffer", "endspurt", "gebiete", "wdh"}),
    *zelle(beim("woche", "jede"), "kl", 1, 10, FKL, "1 Klausur pro Woche", 28),
    anm("Examensbedingungen: 5 Stunden am Stück", 0, beim("bed", "Examensbedingungen")),
    anm("auch wenn noch Stoff fehlt", 1, beim("frueh", "Stoff")),
    anm("korrigieren lassen, z. B. im Klausurenkurs an der Uni", 2, beim("korr", "korrigieren"), size=30),
    zit("Zeitplan für die 5-Stunden-Klausur: Folge 045", 110, ANM[3], beim("v045", "fünf"), size=28),
    zit("typische Fehler in der Klausur: Folge 117", 110, ANM[4], beim("v117", "Fehler"), size=28),
    *requisit([("s5", ("tabler", "writing", 100, PINK), "jede Woche 1 Klausur", WEISS),
               ("bed", ("tabler", "clock", 100, WEISS), "5 Stunden", WEISS),
               ("korr", ("tabler", "file-check", 100, HELLGRUEN), "Korrektur", HELLGRUEN),
               ("n2", None, None, None)]),
    *stehend("FE", X1, [("s5", "ruhig"), ("frueh", "denkt"), ("n2", "ruhig")]),
    *fig("NI", X2, FB, FR, [("s5", "ruhig")], bis="n2"),
    *redet("NI_redet2", X2, FB, FR, "n2", "v045"),
    *fig("NI", X2, FB, FR, [("v045", "froh")], erst="cut"),
    ns(NAME["NI"], X2, FB, "s5", NFARBE["NI"], d=0.1),
    blase("sprech", 620, 260, "n2", 1530, 235, inhalt=["Meine ersten Klausuren", "waren schwach. Aber aus",
                                                      "jeder Korrektur habe ich mir", "die Fehler notiert."], textsize=30,
          figur=NI_G, bis="v045"),
]))

# ===========================================================================================================================
# H Schritt 6: Puffer, Pausen, Endspurt (Fenna fragt, Nils antwortet)
# ===========================================================================================================================
S6 = "Schritt 6"
FE_H = ("FE_fragt", X1, FB, FR)
NI_H = ("NI_redet", X2, FB, FR)
folie([("s6", f"{S6} · Puffer und Pausen"), ("frei", f"{S6} › 1 freier Tag pro Woche"), ("urlaub", f"{S6} › Urlaub: 2 Wochen"),
       ("pmonat", f"{S6} › der Puffermonat"), ("f2", f"{S6} › hinter dem Plan?"), ("n3", f"{S6} › dann den Puffer nehmen"),
       ("spurt", f"{S6} › letzte 6 bis 8 Wochen: kein neuer Stoff"), ("spurt2", f"{S6} › Endspurt: 2 Klausuren pro Woche")],
      rechts_frei([
    *tafel("s6", "Schritt 6: Puffer und Pausen"),
    *brett("s6", {"puffer", "endspurt", "gebiete", "wdh", "kl"}),
    anm("1 Tag pro Woche bleibt frei", 0, beim("frei", "Tag")),
    ticon("fluent-emoji-high-contrast", "beach-with-umbrella", spx(6) + CW / 2, 588, 62, beim("urlaub", "Urlaub"), fuell=GELB),
    anm("Urlaub fest eintragen: 2 Wochen", 1, beim("urlaub", "Urlaub")),
    ring(spx(10) + CW / 2, 377, 52, 152, beim("pmonat", "Puffermonat"), farbe=ORANGE, breite=7),
    anm("Puffer: etwa Krankheit oder ein Thema dauert länger", 2, beim("pmonat", "Krankheit"), size=30),
    ring(spx(11) + CW, 377, 90, 156, beim("spurt", "letzten"), farbe=DROT, breite=7),
    anm("letzte 6 bis 8 Wochen: kein neuer Stoff", 3, beim("spurt", "letzten")),
    *zelle(beim("spurt2", "zwei"), "kl", 11, 12, FKL, "2 pro\nWoche", 26),
    anm("Fenna: 8 Wochen wiederholen und Klausuren schreiben", 4, beim("spurt2", "acht"), size=30),
    *requisit([("s6", ("tabler", "lifebuoy", 100, GELB), "Puffer", WEISS),
               ("frei", ("tabler", "sun", 100, GELB), "1 Tag frei", WEISS),
               ("f2", None, None, None),
               ("spurt", ("tabler", "flag", 100, ROT), "Endspurt", SPURT)]),
    *fig("FE", X1, FB, FR, [("s6", "ruhig"), ("pmonat", "denkt")], bis="f2"),
    *redet("FE_fragt", X1, FB, FR, "f2", "n3"),
    *fig("FE", X1, FB, FR, [("n3", "ruhig"), ("spurt", "entschlossen")], erst="cut"),
    ns(NAME["FE"], X1, FB, "s6", NFARBE["FE"], d=0.1),
    *fig("NI", X2, FB, FR, [("s6", "ruhig")], bis="n3"),
    *redet("NI_redet", X2, FB, FR, "n3", "spurt"),
    *fig("NI", X2, FB, FR, [("spurt", "froh")], erst="cut"),
    ns(NAME["NI"], X2, FB, "s6", NFARBE["NI"], d=0.1),
    blase("sprech", 560, 200, "f2", 1500, 230, inhalt=["Und wenn ich trotzdem", "hinter dem Plan liege?"], textsize=32,
          figur=FE_H, bis="n3"),
    blase("sprech", 560, 200, "n3", 1560, 230, inhalt=["Dann nimmst du den Puffer.", "Dafür ist er da."], textsize=32,
          figur=NI_H, bis="spurt"),
]))

# ===========================================================================================================================
# I Beispielwoche (Wochenplan als Tafel)
# ===========================================================================================================================
SP_W = [100, 220, 290, 430]                  # Tag, 1. Stunde, vormittags, nachmittags
TX0, TY0, TZH = 110, 178, 64


def tzelle(c, zeile, spalte, text, fill, bis_spalte=None, size=30, stil="Bold"):
    bis_spalte = spalte if bis_spalte is None else bis_spalte
    x = TX0 + sum(SP_W[:spalte]); w = sum(SP_W[spalte:bis_spalte + 1]); y = TY0 + zeile * TZH
    assert size >= 26 and F(stil, size).getlength(glyphen(text)) <= w - 20, f"Tabellenzelle zu breit: {text}"
    def zz(dr, s):
        dr.rectangle((2 * s, 2 * s, (w - 2) * s, (TZH - 2) * s), fill=fill, outline=INK, width=4 * s)
        dr.text((w / 2 * s, TZH / 2 * s), text, font=F(stil, size * s), fill=INK, anchor="mm")
    return El(_flaeche(w, TZH, zz), x, y, c, "pop" if c != "wp" else "rise", 0.0, None, name=f"tzelle:{zeile}:{spalte}:{text}")


TAGE = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
els_w = [*tafel("wp", "Eine Woche in der Stoffphase")]
for sp, t in enumerate(["Tag", "1. Stunde", "vormittags", "nachmittags"]):
    els_w.append(tzelle("wp", 0, sp, t, GELB, stil="ExtraBold"))
for zi, t in enumerate(TAGE, 1):
    els_w.append(tzelle("wp", zi, 0, t, HELL, stil="ExtraBold"))
for zi in range(1, 6):
    els_w.append(tzelle((beim("wp1", "Stunde")[0], beim("wp1", "Stunde")[1] + 0.08 * zi), zi, 1, "Karteikarten", FWDH))
    els_w.append(tzelle((beim("wp2", "Stoff")[0], beim("wp2", "Stoff")[1] + 0.08 * zi), zi, 2, "Stoff des Blocks", FZR))
for zi in range(2, 5):
    els_w.append(tzelle((beim("wp3", "Fälle")[0], beim("wp3", "Fälle")[1] + 0.08 * zi), zi, 3, "Fälle lösen", HELLGRUEN))
els_w += [tzelle(beim("wp4", "Klausur"), 1, 3, "Klausur auswerten", HROT),
          tzelle(beim("wp5", "anderen"), 5, 3, "andere Gebiete, Plan prüfen", HGELB, size=26),
          tzelle(beim("wp6", "Klausurtag"), 6, 1, "Klausurtag: 5 Stunden", FKL, bis_spalte=3),
          tzelle("wp7", 7, 1, "frei", GELB, bis_spalte=3)]
assert TY0 + 8 * TZH <= 890
folie([("wp", "Beispielwoche · Stoffphase"), ("wp1", "Beispielwoche › Mo bis Fr: 1 Stunde Karteikarten"),
       ("wp2", "Beispielwoche › vormittags: Stoff des Blocks"), ("wp3", "Beispielwoche › nachmittags: Fälle lösen"),
       ("wp4", "Beispielwoche › Montag: Klausur auswerten"), ("wp5", "Beispielwoche › Freitag: andere Gebiete, Plan prüfen"),
       ("wp6", "Beispielwoche › Samstag: Klausurtag"), ("wp7", "Beispielwoche › Sonntag: frei")], rechts_frei([
    *els_w,
    *requisit([("wp", ("tabler", "calendar-week", 110, WEISS), "1 Woche", WEISS),
               ("wp1", ("tabler", "cards", 100, LILA), "Karteikarten", WEISS),
               ("wp2", ("tabler", "books", 120, GELB), "Stoff", WEISS),
               ("wp3", ("tabler", "writing", 100, WEISS), "Fälle", WEISS),
               ("wp5", ("tabler", "list-check", 100, HGELB), "Plan prüfen", HGELB),
               ("wp6", ("tabler", "clock", 100, PINK), "Klausurtag", WEISS),
               ("wp7", ("tabler", "sun", 100, GELB), "frei", WEISS)]),
    *allein("FE", [("wp", "ruhig"), ("wp3", "entschlossen"), ("wp7", "froh")]),
]))

# ===========================================================================================================================
# J Ergebnis: Der Plan hängt an der Wand (Reißzwecke)
# ===========================================================================================================================
FE_J = ("FE_redetfroh_r", FEX, BODEN_Y, FHA)
folie([("erg", "Ergebnis · Der Plan hängt an der Wand"), ("f3", "Ergebnis › Monat 1: Zivilrecht, Samstag: 1. Klausur")], [
    *kueche("erg", kalender_leer=True, tassen=True),
    hart(pl("Ergebnis", 70, 30, "erg", fill=PINK, size=38)),
    szene(bis_(wandkalender(beim("erg", "Plan"), leer=False), None), "201reisszwecke*", 0.5, -0.1),
    ficon("fluent-emoji-high-contrast", "pushpin", KAL[0] + 42, KAL[1] + 70, 46, beim("erg", "Plan"), fuell=ROT, anim="cut"),
    *fig("FE", FEX, BODEN_Y, FHA, [("erg", "stolz")], erst="pop", bis="f3"),
    *redet("FE_redetfroh_r", FEX, BODEN_Y, FHA, "f3", "tipp"),
    ns(NAME["FE"], FEX, BODEN_Y, "erg", NFARBE["FE"], d=0.1),
    *fig("NI", NIX, BODEN_Y, FHA, [("erg", "froh")], erst="pop"),
    ns(NAME["NI"], NIX, BODEN_Y, "erg", NFARBE["NI"], d=0.1),
    pl("Monat 1: Zivilrecht", 110, 190, beim("f3", "Monat"), fill=BLAU, size=30),
    pl("Samstag: 1. Klausur", 110, 270, beim("f3", "Samstag"), fill=PINK, size=30),
    blase("sprech", 680, 230, "f3", 1180, 200, inhalt=["Jetzt weiß ich, womit ich anfange:", "mit Monat 1, Zivilrecht. Und am",
                                                     "Samstag mit der ersten Klausur."], textsize=32, figur=FE_J, bis="tipp"),
])

# ===========================================================================================================================
# K Klausurtipp (Lexi): üben wie im Examen
# ===========================================================================================================================
els_k = [*tafel("tipp", "Klausurtipp: üben wie im Examen", fill=HELL), warnung_i(150, 225, "tipp", gr=26),
         z("Übungsklausuren so schreiben, wie das Examen läuft", 200, 200, "tipp", "Bold", 32),
         blk(130, 290, 1020, 76, WEISS, "tipp2", [("5 Stunden am Stück", "ExtraBold", 34, INK)]),
         blk(130, 386, 1020, 76, GRUEN, beim("tipp2", "Hilfsmitteln"), [("nur die in deinem Land erlaubten Hilfsmittel", "ExtraBold", 34, INK)]),
         zit("z. B. § 13 Abs. 3 JAG NRW: Das Justizministerium bestimmt die Hilfsmittel.", 130, 472, beim("tipp2", "Hilfsmitteln")),
         blk(130, 530, 1020, 76, GELB, "tipp3", [("in deiner Form: von Hand oder am Computer", "ExtraBold", 34, INK)]),
         blk(130, 626, 1020, 76, BLAU, "tipp4", [("Fehlerliste: Was wiederholst du als Nächstes?", "ExtraBold", 34, INK)]),
         *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
         ns("Lexi", FX, FB, "tipp", GELB, d=0.2)]
folie([("tipp", "Klausurtipp · üben wie im Examen"), ("tipp2", "Klausurtipp › 5 Stunden am Stück"),
       (beim("tipp2", "Hilfsmitteln"), "Klausurtipp › nur erlaubte Hilfsmittel"), ("tipp3", "Klausurtipp › von Hand oder am Computer"),
       ("tipp4", "Klausurtipp › Fehlerliste aus den Korrekturen")], els_k)

# ===========================================================================================================================
# L Dein Lernplan in 6 Schritten (Schema, Punkt für Punkt)
# ===========================================================================================================================
REIHEN = [("k1", "I.", "Bestandsaufnahme: Stoffkatalog und Ampel", FZR),
          ("k2", "II.", "rückwärts planen vom Examenstermin", ROT),
          ("k3", "III.", "Stoffphase: gewichtet nach Prüfung und Ampel", FOR),
          ("k4", "IV.", "Wiederholung in wachsenden Abständen", FWDH),
          ("k5", "V.", "jede Woche 1 Klausur, von Anfang an", FKL),
          ("k6", "VI.", "Puffer, freie Tage und 8 Wochen Endspurt", FPUF)]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Dein Lernplan in 6 Schritten"), 110, 90, "sch", 50)]
y = 215
for c, nr, text, f in REIHEN:
    els_sch.append(pl(nr, 130, y - 6, c, fill=f, size=36))
    els_sch.append(z(text, 300, y, c, "ExtraBold", 42, rechts=1820))
    y += 120
assert y <= 960, y
folie([("sch", "Lernplan · 6 Schritte"), ("k1", "Lernplan › I. Bestandsaufnahme"), ("k2", "Lernplan › II. rückwärts planen"),
       ("k3", "Lernplan › III. Stoffphase"), ("k4", "Lernplan › IV. Wiederholung"), ("k5", "Lernplan › V. Klausuren"),
       ("k6", "Lernplan › VI. Puffer und Endspurt")], els_sch)

# ===========================================================================================================================
# M Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Ein Lernplan beginnt beim ", 0), ("Examenstermin", "a")], [("und rechnet ", 0), ("rückwärts", "b"), (".", 0)]],
                750, 300, 44, "merke", {"a": beim("merke", "Examenstermin"), "b": beim("merke", "rückwärts")}),
    *markertext([[("Stoff, Wiederholung und Klausuren", 0)], [("laufen jede Woche ", 0), ("nebeneinander", "c"), (",", 0)]],
                750, 480, 44, "m2", {"c": beim("m2", "nebeneinander")}),
    *markertext([[("und der ", 0), ("Puffer", "d"), (" gehört", 0)], [("von Anfang an dazu.", 0)]], 750, 660, 44, "m3",
                {"d": beim("m3", "Puffer")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
