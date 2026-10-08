"""Folge 261 · Beurteilungsspielraum: Kann man eine Examensnote einklagen? – Serienstandard Open Peeps (Katzenkönig).
Fall: Jorinde folgt in einer Examensklausur im Öffentlichen Recht einer vertretbaren, folgerichtig begründeten
Gegenansicht; Prüfer Herr Ellerbrock wertet „falsch“, „insgesamt oberflächlich“, 5 Punkte; Überdenken ohne Änderung; Klage.
Szenen laut ../SZENENPLAN.md: A1 Klausur und Korrektur, A2 Der Bescheid (Hook, Frage), B Sachverhalt, C1 Grundsatz
(Wortlautkarte Art. 19 Abs. 4 S. 1 GG), C2 Notenstufen und Berufsfreiheit (Wortlautkarten § 1 JurPrNotSkV, Art. 12 Abs. 1
S. 1 GG), D1 Ausnahme Beurteilungsspielraum, D2 Wertung oder Fachfrage, D3 Antwortspielraum (Zitatkarte BVerfGE 84, 34
<55>), E Grenzen des Spielraums, F1 Überdenkungsverfahren, F2 Beispiel NRW (Wortlautkarten § 27 Abs. 1, § 27a S. 1
JAG NRW), G1 Einwände und Überdenken, G2 Die Klage, G3 Das Urteil, H Klausurtipp (Lexi), I Schema, J Merksatz (Lexi).
Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/feld/requisit/neben/person als eigene Kopie aus
Folge 258 (gemeinsame Dateien unverändert); neu: blatt_linie(), sachverhalt_261().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut nach gesetze-im-internet.de bzw. recht.nrw.de, Abruf 08.10.2026;
Zitat BVerfGE 84, 34 nach dem Volltext bei DFR (servat.unibe.ch), auf bundesverfassungsgericht.de nicht vorhanden."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_261/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_261/" in n:
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 160/203/217/219/222) ---------------------------------
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
NAME = {"JO": "Jorinde", "EL": "Herr Ellerbrock", "RI": "die Richterin"}
NFARBE = {"JO": GRUEN, "EL": TUERKIS, "RI": LILA}


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


def fall_ns(k, x, cue, **kw):
    return ns(NAME[k], x, BODEN, cue, NFARBE[k], **kw)






# --- eigene Szenenbausteine Folge 261 --------------------------------------------------------------------------------------
GRAUHELL = (226, 226, 230, 255)


def zm(text, cx, y, cue, stil="Regular", size=30, **k):
    """Tafelzeile, mittig auf cx gesetzt."""
    return z(text, round(cx - F(stil, size).getlength(glyphen(text)) / 2), y, cue, stil, size, **k)


def person(k, x, unten, hoehe, folge, bis=None, erst="cut", d=0.0):
    """Mimikfolge einer Figur am selben Platz: folge = [(cue, suffix)]; suffix mit '!' = Figur spricht von cue bis zum
    nächsten Eintrag (Mundzustände aus den Wortgrenzen, redet())."""
    els = []
    for i, (c, s) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else bis
        if s.startswith("!"):
            assert b is not None, "Redefenster braucht ein Ende"
            els += redet(f"{k}_{s[1:]}", x, unten, hoehe, c, b)
        else:
            els.append(peep_voll(f"{k}_{s}", x, unten, hoehe, c, anim=erst if i == 0 else "cut", d=d if i == 0 else 0.0,
                                 bis=b))
    return els


def neben(k, x, folge, bis=None, erst="pop"):
    """Figur neben der Tafel (blickt nach links zur Tafel bzw. _r nach rechts), mit Namensschild ab dem ersten Bild."""
    els = [*person(k, x, FB, FR, folge, bis=bis, erst=erst), bis_(ns(NAME[k], x, FB, folge[0][0], NFARBE[k], d=0.1), bis)]
    return rechts_frei(els, 1200)


def sachverhalt_261(cue, absaetze, fragen):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 56)]
    y = 205
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=38, zeilenabstand=1.30)
        els += e; y += 14
    for f_ in fragen:
        els.append(pille(glyphen(f_), 210, y + 6, cue, fill=PINK, size=36)); y += 76
    assert y + 10 <= 950, f"Sachverhalt zu lang ({y})"
    folie([(cue, "Sachverhalt")], els)


def regal(x, y, w, cue):
    """Wandregal (programmatisch: Brett in Holzfarbe mit Tuschekontur)."""
    return feld(x, y, w, 18, cue, fill=HOLZ, rand=4, rund=4, name="regal")


# --- eigene Szenenbausteine Folge 261 --------------------------------------------------------------------------------------
GRAUHELL = (226, 226, 230, 255)
ROTHELL = (253, 220, 214, 255)


def zm(text, cx, y, cue, stil="Regular", size=30, **k):
    """Tafelzeile, mittig auf cx gesetzt."""
    return z(text, round(cx - F(stil, size).getlength(glyphen(text)) / 2), y, cue, stil, size, **k)


def person(k, x, unten, hoehe, folge, bis=None, erst="cut", d=0.0):
    """Mimikfolge einer Figur am selben Platz: folge = [(cue, suffix)]; suffix mit '!' = Figur spricht von cue bis zum
    nächsten Eintrag (Mundzustände aus den Wortgrenzen, redet())."""
    els = []
    for i, (c, s) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else bis
        if s.startswith("!"):
            assert b is not None, "Redefenster braucht ein Ende"
            els += redet(f"{k}_{s[1:]}", x, unten, hoehe, c, b)
        else:
            els.append(peep_voll(f"{k}_{s}", x, unten, hoehe, c, anim=erst if i == 0 else "cut", d=d if i == 0 else 0.0,
                                 bis=b))
    return els


def neben(k, x, folge, bis=None, erst="pop"):
    """Figur neben der Tafel (blickt nach links zur Tafel bzw. _r nach rechts), mit Namensschild ab dem ersten Bild."""
    els = [*person(k, x, FB, FR, folge, bis=bis, erst=erst), bis_(ns(NAME[k], x, FB, folge[0][0], NFARBE[k], d=0.1), bis)]
    return rechts_frei(els, 1200)


def blatt_linie(x, y, w, cue, bis=None):
    """Graue Schreiblinie auf einem Klausurblatt (programmatisch, keine Schrift)."""
    im = Image.new("RGBA", (w, 10)); ImageDraw.Draw(im).rounded_rectangle((0, 2, w - 1, 7), 3, fill=(170, 170, 176, 255))
    return El(im, x, y, cue, "fade", 0.0, bis, name="linie")


# ===========================================================================================================================
# A1 Fall: Klausur (links) und Korrektur (rechts)
# ===========================================================================================================================
JOX, ELX = 330, 1690
KB = (800, 110, 420, 450)          # Klausurblatt in der Mitte
JOa = ("JO_redet", 0, BODEN, FH)   # Platzhalter, wird je Szene gesetzt
ELa = ("EL_redet", ELX, BODEN, FH)
KTOP = ficon("tabler", "desk", 1450, BODEN - 2, 300, NULL).y + 8
stift = ficon("tabler", "pencil", 1180, 230, 60, "el1", fuell=ROT)
szene(stift, "261stift_1", gain=1.0, versatz=0.0)
folie([(NULL, "Fall · Die Examensklausur"), ("ellerbrock", "Fall · Die Korrektur")], [
    hart(boden(NULL)),
    hart(pl("Examensklausur", 70, 30, NULL, fill=GELB, size=40)),
    hart(ficon("tabler", "clock", 600, 330, 90, NULL, fuell=WEISS, anim="cut")),
    hart(ficon("tabler", "desk", 600, BODEN - 2, 300, NULL, fuell=HOLZ, anim="cut")),
    hart(ficon("tabler", "file-pencil", 600, ficon("tabler", "desk", 600, BODEN - 2, 300, NULL).y + 12, 70, NULL,
               fuell=WEISS, anim="cut")),
    *person("JO", JOX, BODEN, FH, [(NULL, "ruhig_r"), ("klausur", "denkt_r"), ("gegen", "entschl_r"), ("el1", "liest_r")]),
    hart(fall_ns("JO", JOX, NULL)),
    # Klausurblatt
    bis_(karte(*KB, "klausur", fill=WEISS, rund=14, schatten=6, rand=4), None),
    z("Klausur Öffentliches Recht", KB[0] + 24, KB[1] + 20, "klausur", "ExtraBold", 28, rechts=KB[0] + KB[2] - 10),
    z("Streitfrage:", KB[0] + 24, KB[1] + 80, beim("klausur", "Streitfrage"), "Bold", 28, rechts=KB[0] + KB[2] - 10),
    z("Ich folge der Gegenansicht,", KB[0] + 24, KB[1] + 125, "gegen", "Regular", 28, rechts=KB[0] + KB[2] - 10),
    z("weil erstens …", KB[0] + 24, KB[1] + 170, beim("gegen", "begründet"), "Regular", 28, rechts=KB[0] + KB[2] - 10),
    z("zweitens …", KB[0] + 24, KB[1] + 215, beim("gegen", "Schritt"), "Regular", 28, rechts=KB[0] + KB[2] - 10),
    z("drittens …", KB[0] + 24, KB[1] + 260, beim("gegen", "Schritt", nr=2), "Regular", 28, rechts=KB[0] + KB[2] - 10),
    pl("falsch", KB[0] + 330, KB[1] + 150, beim("el1", "falsch"), fill=ROT, size=30, anker="m"),
    pl("insgesamt oberflächlich", KB[0] + KB[2] / 2, KB[1] + 320, beim("el1", "Insgesamt"), fill=ROTHELL, size=28,
       anker="m"),
    pl("5 Punkte", KB[0] + KB[2] / 2, KB[1] + 385, beim("el1", "fünf"), fill=GELB, size=30, anker="m"),
    # Korrektur
    pl("bei der Korrektur", 1290, 30, "ellerbrock", fill=TUERKIS, size=34),
    ficon("tabler", "desk", 1450, BODEN - 2, 300, "ellerbrock", fuell=HOLZ),
    ficon("tabler", "lamp", 1350, KTOP + 4, 80, "ellerbrock", fuell=GELB),
    ficon("tabler", "files", 1520, KTOP + 4, 80, "ellerbrock", fuell=WEISS),
    *person("EL", ELX, BODEN, FH, [("ellerbrock", "denkt"), ("el1", "!redet")], bis="bescheid", erst="pop"),
    fall_ns("EL", ELX, "ellerbrock", d=0.1),
    stift,
    blase("sprech", 600, 200, "el1", 1520, 190, inhalt=["Diese Ansicht ist falsch.", "Insgesamt oberflächlich:",
                                                        "5 Punkte."], textsize=32, figur=ELa),
])

# ===========================================================================================================================
# A2 Fall: Der Bescheid zu Hause; Hook und Frage
# ===========================================================================================================================
JHX = 1360
JHa = ("JO_redet", JHX, BODEN, FH)
TISCH2 = 980
KT2 = ficon("tabler", "desk", TISCH2, BODEN - 2, 360, NULL).y + 8
brief_zu = ficon("tabler", "mail", TISCH2, KT2 + 4, 90, "bescheid", fuell=WEISS, bis=beim("bescheid", "Bescheid"))
brief_auf = ficon("tabler", "mail-opened", TISCH2, KT2 + 4, 90, beim("bescheid", "Bescheid"), fuell=WEISS)
szene(brief_auf, "261umschlag_1", gain=1.0, versatz=0.0)
BK = (100, 120, 660, 380)
folie([("bescheid", "Fall · Der Bescheid"), ("hook", "Einstieg · Die Frage")], [
    boden("bescheid", hart_=False),
    pl("Der Bescheid", 70, 30, beim("bescheid", "Bescheid"), fill=GELB, size=40),
    ficon("tabler", "window", 1700, 380, 200, "bescheid", fuell=BLAUHELL),
    ficon("tabler", "plant-2", 1840, BODEN - 2, 100, "bescheid", fuell=GRUEN),
    ficon("tabler", "desk", TISCH2, BODEN - 2, 360, "bescheid", fuell=HOLZ),
    brief_zu, brief_auf,
    *person("JO", JHX, BODEN, FH, [("bescheid", "ruhig"), (beim("bescheid", "sieht"), "liest"), ("jo1", "!redet"),
                                   ("hook", "sorge"), ("frage", "denkt")], erst="pop"),
    fall_ns("JO", JHX, "bescheid", d=0.1),
    bis_(karte(*BK, beim("bescheid", "sieht"), fill=HELL, rund=18, schatten=6, rand=4), "hook"),
    bis_(z("Bescheid des Prüfungsamts", BK[0] + 30, BK[1] + 24, beim("bescheid", "sieht"), "ExtraBold", 32,
           rechts=BK[0] + BK[2] - 10), "hook"),
    bis_(z("Klausur Öffentliches Recht:", BK[0] + 30, BK[1] + 95, beim("bescheid", "sieht"), "Bold", 30,
           rechts=BK[0] + BK[2] - 10), "hook"),
    bis_(z("5 Punkte (ausreichend)", BK[0] + 30, BK[1] + 145, beim("bescheid", "sieht"), "ExtraBold", 36,
           rechts=BK[0] + BK[2] - 10), "hook"),
    bis_(z("Randbemerkung:", BK[0] + 30, BK[1] + 225, beim("bescheid", "Korrektur"), "Bold", 30,
           rechts=BK[0] + BK[2] - 10), "hook"),
    pl("falsch", BK[0] + 310, BK[1] + 215, beim("bescheid", "Korrektur"), fill=ROT, size=30, bis="hook"),
    pl("insgesamt oberflächlich", BK[0] + 30, BK[1] + 285, beim("bescheid", "Korrektur"), fill=ROTHELL, size=28,
       bis="hook"),
    blase("sprech", 660, 210, "jo1", 1020, 210, inhalt=["Falsch? Meine Lösung", "ist vertretbar!", "Ich klage mir 9 Punkte ein."],
          textsize=34, figur=JHa, bis="hook"),
    pl("Deine Examensklausur bekommt 5 Punkte,", 900, 90, "hook", fill=WEISS, size=36, anker="m"),
    pl("obwohl deine Lösung fachlich vertretbar war.", 900, 165, beim("hook", "obwohl"), fill=GELB, size=36, anker="m"),
    pl("Kann man eine Examensnote einklagen?", 900, 250, "frage", fill=PINK, size=38, anker="m"),
    pl("Und was darf das Gericht überhaupt prüfen?", 820, 325, "frage2", fill=PINK, size=32, anker="m"),
])

# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
sachverhalt_261("sv", [
    "Jorinde schreibt ihre Examensklausuren. Im Öffentlichen Recht folgt sie bei einer Streitfrage einer vertretbaren "
    "Gegenansicht und begründet sie mit gewichtigen Argumenten folgerichtig. Ihr Prüfer, Herr Ellerbrock, schreibt an den "
    "Rand „falsch“, unter die Arbeit „Insgesamt oberflächlich“, und vergibt 5 Punkte. Der Zweitprüfer schließt sich an.",
    "Jorinde erhebt Einwände und belegt, dass ihre Ansicht vertreten wird. Herr Ellerbrock überdenkt die Bewertung und "
    "bleibt bei 5 Punkten. Jorinde klagt beim Verwaltungsgericht auf 9 Punkte.",
], ["Kann Jorinde die 9 Punkte einklagen?", "Was darf das Gericht prüfen?"])

# ===========================================================================================================================
# C1 Grundsatz: volle Kontrolle (Art. 19 Abs. 4 GG, Wortlautkarte)
# ===========================================================================================================================
W19 = "„Wird jemand durch die öffentliche Gewalt in seinen Rechten verletzt, so steht ihm der Rechtsweg offen.“"
w19, w19_y = wortlaut(110, 180, 1040, W19, "Art. 19 Abs. 4 S. 1 GG", "wl19", marken=[
    ("öffentliche Gewalt", beim("wl19", "öffentliche")), ("Rechten", beim("wl19", "Rechten")),
    ("Rechtsweg offen", beim("wl19", "Rechtsweg"))], size=32)
Y1 = w19_y + 30
folie([("grund", "Grundsatz · volle Kontrolle, Art. 19 Abs. 4 GG"), ("ubr", "Grundsatz › unbestimmte Rechtsbegriffe"),
       ("erm", "Grundsatz › anders beim Ermessen")], rechts_frei([
    *tafel("grund", "Grundsatz: volle Kontrolle"),
    *w19,
    *okz("wirksame Kontrolle: grundsätzlich rechtlich", Y1, "wirksam", "Bold", 32),
    z("und tatsächlich vollständig", 185, Y1 + 45, beim("wirksam", "tatsächlich"), "Bold", 32),
    zit("BVerfGE 84, 34 (49)", 185, Y1 + 92, beim("wirksam", "vollständig")),
    *okz("unbestimmte Rechtsbegriffe: konkretisieren", Y1 + 150, "ubr", "Bold", 32),
    z("ist Sache der Gerichte", 185, Y1 + 195, beim("ubr", "Sache"), "Bold", 32),
    zit("BVerfGE 84, 34 (49 f.)", 185, Y1 + 242, beim("ubr", "Sache")),
    pl("anders beim Ermessen (Rechtsfolgenseite): Folge 74", 110, Y1 + 300, "erm", fill=GELB, size=28),
    *neben("JO", FX, [("grund", "ruhig"), ("ubr", "denkt"), ("erm", "liest")]),
    *requisit([("grund", ("tabler", "building-bank", 120, WEISS), "Gericht", BLAU),
               ("ubr", ("tabler", "search", 100, WEISS), "voll prüfen", GRUEN)]),
]))
assert Y1 + 370 <= 895, Y1

# ===========================================================================================================================
# C2 Notenstufen (§ 1 JurPrNotSkV) und Berufsfreiheit (Art. 12 Abs. 1 GG)
# ===========================================================================================================================
WNOTE = ("„ausreichend eine Leistung, die trotz ihrer Mängel durchschnittlichen Anforderungen noch entspricht "
         "= 4 bis 6 Punkte“")
wn, wn_y = wortlaut(110, 180, 1040, WNOTE, "§ 1 Verordnung über eine Noten- und Punkteskala (JurPrNotSkV)", "note",
                    marken=[("trotz ihrer Mängel", beim("ausr", "trotz")),
                            ("durchschnittlichen Anforderungen", beim("ausr", "durchschnittlichen"))], size=32)
W12 = "„Alle Deutschen haben das Recht, Beruf, Arbeitsplatz und Ausbildungsstätte frei zu wählen.“"
w12, w12_y = wortlaut(110, wn_y + 40, 1040, W12, "Art. 12 Abs. 1 S. 1 GG", "art12", marken=[
    ("Beruf,", beim("art12", "Beruf"))], size=32)
folie([("note", "Grundsatz › Notenstufen: unbestimmt umschrieben"),
       ("art12", "Grundsatz › Berufsfreiheit, Art. 12 Abs. 1 GG")], rechts_frei([
    *tafel("note", "Auch Noten sind unbestimmt"),
    *wn, *w12,
    z("Examensnoten entscheiden über den Zugang zum Beruf.", 110, w12_y + 30, beim("art12", "Examensnoten"), "Bold", 30),
    *neben("JO", FX, [("note", "liest"), ("art12", "entschl")], erst="cut"),
    *requisit([("note", ("tabler", "certificate", 120, WEISS), "5 Punkte = ausreichend", GELB),
               ("art12", ("tabler", "briefcase", 110, GELB), "Berufszugang", GRUEN)]),
]))
assert w12_y + 80 <= 895, w12_y

# ===========================================================================================================================
# D1 Ausnahme: Beurteilungsspielraum (Vergleich, Chancengleichheit)
# ===========================================================================================================================
folie([("aber", "Ausnahme · Beurteilungsspielraum"), ("chance", "Ausnahme › Chancengleichheit")], rechts_frei([
    *tafel("aber", "Ausnahme: Beurteilungsspielraum"),
    z("Das Gericht setzt keine eigene Note fest.", 110, 175, "aber", "Bold", 34),
    feld(110, 245, 1040, 220, beim("bezug", "Vergleich"), fill=BLAUHELL, anim="pop", name="block"),
    *[dicon("tabler", "file-text", 200 + i * 95, 360, 70, beim("bezug", "vielen"), fuell=WEISS) for i in range(5)],
    zm("Vergleich mit vielen", 860, 290, beim("bezug", "Vergleich"), "Bold", 30),
    zm("anderen Arbeiten", 860, 335, beim("bezug", "anderen"), "Bold", 30),
    zm("und Erfahrung der Prüfer", 860, 390, beim("bezug", "Erfahrung"), "Bold", 30),
    blk(110, 500, 1040, 130, ROTHELL, "chance", [("Bewertung einer Kandidatin ohne diesen Vergleich?", "Bold", 30, INK),
                                               ("Chancengleichheit verletzt", "ExtraBold", 32, INK)]),
    zit("BVerfGE 84, 34 (51 f.)", 110, 645, beim("chance", "verletzt")),
    blk(110, 700, 1040, 130, GELB, "bsr", [("Beurteilungsspielraum der Prüfer,", "ExtraBold", 32, INK),
                                          ("aber nur bei prüfungsspezifischen Wertungen", "Bold", 30, INK)]),
    *neben("EL", FX, [("aber", "ruhig"), ("bezug", "denkt"), ("bsr", "streng")]),
    *requisit([("aber", ("tabler", "certificate", 110, WEISS), "keine Note vom Gericht", ROTHELL),
               ("chance", ("tabler", "scale", 120, WEISS), "Chancengleichheit", BLAU)]),
]))

# ===========================================================================================================================
# D2 Wertung oder Fachfrage
# ===========================================================================================================================
folie([("spez", "Ausnahme › prüfungsspezifische Wertungen"), ("fach", "Ausnahme › Fachfragen: volle Kontrolle")],
      rechts_frei([
    *tafel("spez", "Wertung oder Fachfrage?"),
    feld(110, 180, 500, 560, "spez", fill=HELL, anim="pop", name="spalte_wertung"),
    zm("prüfungsspezifische", 360, 200, "spez", "ExtraBold", 32),
    zm("Wertung", 360, 242, "spez", "ExtraBold", 32),
    *okz("Schwierigkeitsgrad", 320, beim("spez", "Schwierigkeitsgrad"), "Bold", 30, x=185),
    *okz("Gewichtung von Stärken", 390, "gew", "Bold", 30, x=185),
    z("und Schwächen", 185, 432, beim("gew", "Schwächen"), "Bold", 30),
    *okz("Gesamteindruck", 500, beim("eindr", "Gesamteindruck"), "Bold", 30, x=185),
    blk(130, 600, 460, 110, ROTHELL, "eing", [("Gericht prüft nur", "Bold", 30, INK), ("eingeschränkt", "ExtraBold", 32, INK)]),
    feld(650, 180, 500, 560, "fach", fill=HELLGRUEN, anim="pop", name="spalte_fach"),
    zm("Fachfrage", 900, 220, "fach", "ExtraBold", 32),
    zm("Ist die Ansicht richtig", 900, 320, beim("fach", "Ist"), "Bold", 30),
    zm("oder vertretbar?", 900, 362, beim("fach", "vertretbar"), "Bold", 30),
    zm("notfalls mit", 900, 470, beim("fach", "notfalls"), "Bold", 30),
    zm("Sachverständigen", 900, 512, beim("fach", "Sachverständigen"), "Bold", 30),
    blk(670, 600, 460, 110, GRUEN, beim("fach", "voll"), [("Gericht prüft", "Bold", 30, INK), ("voll", "ExtraBold", 32, INK)]),
    zit("BVerwG, Beschl. v. 5.3.2018 – 6 B 71.17, Rn. 9 f.", 110, 770, beim("fach", "voll")),
    *neben("EL", X1, [("spez", "denkt"), ("fach", "streng")]),
    *neben("JO", X2, [("spez", "ruhig"), ("fach", "entschl")]),
]))

# ===========================================================================================================================
# D3 Antwortspielraum (BVerfGE 84, 34 <55>, Wortlautkarte)
# ===========================================================================================================================
WBV = ("„Eine vertretbare und mit gewichtigen Argumenten folgerichtig begründete Lösung darf nicht als falsch gewertet "
       "werden.“")
wbv, wbv_y = wortlaut(110, 260, 1040, WBV, "BVerfG, Beschl. v. 17.4.1991, BVerfGE 84, 34 (55)",
                      "wlbv", marken=[("vertretbare", beim("wlbv", "vertretbare")),
                                      ("gewichtigen Argumenten", beim("wlbv", "gewichtigen")),
                                      ("folgerichtig", beim("wlbv", "folgerichtig")),
                                      ("nicht als falsch", beim("wlbv", "nicht"))], size=34)
folie([("anspr", "Fachfragen › Antwortspielraum, BVerfGE 84, 34")], rechts_frei([
    *tafel("anspr", "Antwortspielraum des Prüflings"),
    z("Bei Fachfragen gilt:", 110, 180, "anspr", "Bold", 34),
    *wbv,
    blk(110, wbv_y + 40, 1040, 130, GELB, "beide", [("Vertretbar allein genügt nicht:", "ExtraBold", 32, INK),
                                                   ("Die Lösung muss auch gut begründet sein.", "Bold", 30, INK)]),
    zit("BVerwG, Beschl. v. 3.9.2020 – 6 B 16.20, Rn. 10", 110, wbv_y + 185, beim("beide", "Lösung")),
    *neben("JO", FX, [("anspr", "liest"), ("wlbv", "entschl"), ("beide", "denkt")], erst="cut"),
    *requisit([("anspr", ("tabler", "books", 120, GELB), "vertretbar?", GELB)]),
]))
assert wbv_y + 230 <= 895, wbv_y

# ===========================================================================================================================
# E Kontrolldichte: Grenzen des Beurteilungsspielraums
# ===========================================================================================================================
GR = [("k1", "Verfahrensfehler", None),
      ("k2", "falscher Sachverhalt", "etwa einen Teil der Arbeit übersehen"),
      ("k3", "allgemeingültige Bewertungsmaßstäbe verletzt", None),
      ("k4", "sachfremde Erwägungen", None)]
els_gr = []
y = 245
for i, (c, t, u) in enumerate(GR):
    els_gr += [karte(110, y, 70, 64, c, fill=BLAU, rund=14, schatten=4, rand=4),
               zm(str(i + 1), 145, y + 10, c, "ExtraBold", 32),
               z(t, 210, y + 10, c, "Bold", 32)]
    if u:
        els_gr.append(z(u, 210, y + 58, beim(c, "etwa"), "Regular", 28))
        y += 50
    y += 95
folie([("kontr", "Kontrolldichte › Grenzen des Beurteilungsspielraums"), ("kaus", "Kontrolldichte › Auswirkung auf die Note")],
      rechts_frei([
    *tafel("kontr", "Auch Wertungen haben Grenzen"),
    z("Ganz frei ist der Prüfer auch dort nicht.", 110, 175, beim("kontr", "Ganz"), "Bold", 34),
    *els_gr,
    zit("BVerfGE 84, 34 (53 f.); BVerwG 6 B 71.17, Rn. 10", 110, y - 10, beim("k4", "Erwägungen")),
    blk(110, y + 40, 1040, 120, ROTHELL, "kaus", [("Korrigiert wird nur, wenn sich der Fehler", "Bold", 30, INK),
                                                ("auf die Note ausgewirkt haben kann.", "ExtraBold", 32, INK)]),
    zit("BVerfGE 84, 34 (55)", 110, y + 175, beim("kaus", "Note")),
    *neben("RI", FX, [("kontr", "ruhig"), ("k1", "denkt"), ("kaus", "ruhig")]),
    *requisit([("kontr", ("tabler", "zoom-check", 110, WEISS), "Gericht prüft", BLAU)]),
]))
assert y + 220 <= 895, y

# ===========================================================================================================================
# F1 Überdenkungsverfahren
# ===========================================================================================================================
folie([("ued", "Überdenkungsverfahren · Ausgleich"), ("subst", "Überdenkungsverfahren › konkrete Einwände"),
       ("mass", "Überdenkungsverfahren › Maßstab bleibt")], rechts_frei([
    *tafel("ued", "Überdenkungsverfahren"),
    z("Ausgleich für die eingeschränkte Kontrolle", 110, 175, beim("ued", "Ausgleich"), "Bold", 32),
    zit("BVerwG, Urt. v. 10.4.2019 – 6 C 19.18, Rn. 25", 110, 220, beim("ued", "Ausgleich")),
    blk(110, 275, 480, 120, BLAUHELL, "ued2", [("Einwände wirksam", "ExtraBold", 32, INK), ("vorbringen", "ExtraBold", 32, INK)]),
    pfeil(605, 335, 660, 335, beim("ued2", "Überdenken"), breite=8, kopf=24),
    blk(670, 275, 480, 120, HELLGRUEN, beim("ued2", "Überdenken"), [("Prüfer überdenken", "ExtraBold", 32, INK),
                                                                    ("die Bewertung", "ExtraBold", 32, INK)]),
    zit("BVerfGE 84, 34 (48 f.)", 110, 410, beim("ued2", "erreichen")),
    *okz("Einwände konkret gegen einzelne Wertungen", 470, "subst", "Bold", 30),
    *neinz("pauschal „zu streng“ genügt nicht", 530, beim("subst", "Pauschal"), "Bold", 30, kreuz=beim("subst", "genügt")),
    blk(110, 610, 1040, 130, GELB, "mass", [("keine völlig neue Bewertung:", "ExtraBold", 32, INK),
                                           ("beanstandete Punkte prüfen, Maßstab bleibt derselbe", "Bold", 30, INK)]),
    zit("BVerwG 6 C 19.18, Rn. 26, 28", 110, 755, beim("mass", "Maßstab")),
    *neben("JO", X1, [("ued", "ruhig_r"), ("ued2", "entschl_r"), ("mass", "ruhig_r")]),
    *neben("EL", X2, [("ued", "ruhig"), ("ued2", "denkt"), ("mass", "streng")]),
]))

# ===========================================================================================================================
# F2 Länderrecht: Beispiel Nordrhein-Westfalen (§ 27 Abs. 1, § 27a S. 1 JAG NRW, Wortlautkarten)
# ===========================================================================================================================
W27 = ("„Über einen Widerspruch gemäß § 68 der Verwaltungsgerichtsordnung entscheidet die oder der Vorsitzende des "
       "Justizprüfungsamtes, bei Angriffen gegen die Beurteilung einer Prüfungsleistung auf Grundlage einer einzuholenden "
       "Stellungnahme der Personen, die an der Beurteilung beteiligt gewesen sind.“")
w27, w27_y = wortlaut(110, 255, 1040, W27, "§ 27 Abs. 1 JAG NRW", "nrw", marken=[
    ("Widerspruch", beim("nrw", "Widerspruchsverfahren")), ("Stellungnahme", beim("nrw", "Stellungnahmen"))], size=28)
W27A = ("„Einwendungen gegen die Bewertung schriftlicher Aufsichtsarbeiten sind spätestens binnen sechs Monaten nach "
        "Bekanntgabe der Prüfungsentscheidung, … im Einzelnen und nachvollziehbar schriftlich oder elektronisch zu "
        "begründen.“")
w27a, w27a_y = wortlaut(110, w27_y + 30, 1040, W27A, "§ 27a S. 1 JAG NRW", "frist", marken=[
    ("sechs Monaten", beim("frist", "sechs")), ("im Einzelnen", beim("frist", "Einzelnen"))], size=28)
folie([("land", "Überdenkungsverfahren › regelt dein Land"), ("nrw", "Überdenkungsverfahren › Beispiel § 27 JAG NRW")],
      rechts_frei([
    *tafel("land", "Wie und wann? Regelt dein Land."),
    pl("Beispiel Nordrhein-Westfalen", 110, 180, "nrw", fill=BLAU, size=30),
    pl("in deinem Land ggf. andere Norm", 620, 180, "nrw", fill=WEISS, size=28),
    *w27, *w27a,
    *neben("JO", FX, [("land", "denkt"), ("nrw", "liest"), ("frist", "entschl")]),
    *requisit([("land", ("tabler", "building", 110, WEISS), "Prüfungsamt", BLAU),
               ("frist", ("tabler", "calendar", 100, WEISS), "6 Monate", GELB)]),
]))
assert w27a_y <= 895, w27a_y

# ===========================================================================================================================
# G1 Fall: Einwände und Überdenken (Rückkehr: Klausur links, Korrektur rechts wie A1)
# ===========================================================================================================================
EK = (720, 110, 520, 300)
folie([("zurueck", "Fall · Einwände und Überdenken")], [
    boden("zurueck", hart_=False),
    pl("Einwände", 70, 30, "zurueck", fill=GELB, size=40),
    ficon("tabler", "desk", 600, BODEN - 2, 300, "zurueck", fuell=HOLZ),
    ficon("tabler", "books", 600, ficon("tabler", "desk", 600, BODEN - 2, 300, NULL).y + 12, 90, "einw", fuell=GELB),
    *person("JO", JOX, BODEN, FH, [("zurueck", "entschl_r"), ("ueb", "ruhig_r"), ("el2", "sorge_r")], erst="pop"),
    fall_ns("JO", JOX, "zurueck", d=0.1),
    bis_(karte(*EK, "einw", fill=WEISS, rund=14, schatten=6, rand=4), None),
    z("Einwände von Jorinde", EK[0] + 24, EK[1] + 20, "einw", "ExtraBold", 30, rechts=EK[0] + EK[2] - 10),
    z("Meine Ansicht wird vertreten:", EK[0] + 24, EK[1] + 85, beim("einw", "belegt"), "Bold", 28, rechts=EK[0] + EK[2] - 10),
    z("Fundstellen 1, 2, 3", EK[0] + 24, EK[1] + 130, beim("einw", "vertreten"), "Regular", 28, rechts=EK[0] + EK[2] - 10),
    pl("überdenkt", EK[0] + EK[2] / 2, EK[1] + 200, "ueb", fill=TUERKIS, size=28, anker="m"),
    ficon("tabler", "desk", 1450, BODEN - 2, 300, "zurueck", fuell=HOLZ),
    ficon("tabler", "lamp", 1350, KTOP + 4, 80, "zurueck", fuell=GELB),
    ficon("tabler", "files", 1520, KTOP + 4, 80, "zurueck", fuell=WEISS),
    *person("EL", ELX, BODEN, FH, [("zurueck", "ruhig"), ("ueb", "denkt"), ("el2", "!redet")], bis="klage", erst="pop"),
    fall_ns("EL", ELX, "zurueck", d=0.1),
    blase("sprech", 560, 190, "el2", 1520, 190, inhalt=["Die Ansicht bleibt falsch.", "Es bleibt bei 5 Punkten."],
          textsize=32, figur=ELa),
])

# ===========================================================================================================================
# G2 Die Klage: Subsumtion
# ===========================================================================================================================
folie([("klage", "Fall · Die Klage"), ("fehler", "Fall › Fachfrage: Bewertungsfehler"),
       ("obfl", "Fall › „oberflächlich“: Wertung"), ("ausw", "Fall › Auswirkung auf die Note")], rechts_frei([
    *tafel("klage", "Jorinde klagt"),
    blk(110, 180, 1040, 130, HELLGRUEN, "fehler", [("Fachfrage: Lösung vertretbar, mit gewichtigen", "Bold", 30, INK),
                                                  ("Argumenten folgerichtig begründet", "Bold", 30, INK)]),
    *neinz("als falsch gewertet: Bewertungsfehler", 330, beim("fehler", "falsch"), "ExtraBold", 32,
           kreuz=beim("fehler", "Bewertungsfehler")),
    blk(110, 420, 1040, 160, HELL, "obfl", [("„oberflächlich“: prüfungsspezifische Wertung", "Bold", 30, INK),
                                            ("hier kein Fehler erkennbar", "ExtraBold", 32, INK)]),
    blk(110, 620, 1040, 120, ROTHELL, "ausw", [("Auswirkung auf die Note: möglich", "ExtraBold", 32, INK)]),
    *neben("JO", X1, [("klage", "entschl_r"), ("ausw", "ruhig_r")]),
    *neben("RI", X2, [("klage", "ruhig"), ("fehler", "denkt"), ("ausw", "ruhig")]),
]))

# ===========================================================================================================================
# G3 Das Urteil im Verwaltungsgericht
# ===========================================================================================================================
RIX, JGX = 1450, 300
RIa = ("RI_redet", RIX, BODEN, FH)
BANK = (1180, 700, 540, 160)
folie([("urteil", "Ergebnis · Das Urteil"), ("bu", "Ergebnis › Bescheidungsurteil, § 113 Abs. 5 S. 2 VwGO")], [
    boden("urteil", hart_=False),
    pl("Die Richterin verkündet", 70, 30, "urteil", fill=GELB, size=40),
    ficon("tabler", "scale", 1450, 330, 150, "urteil", fuell=WEISS),
    *person("RI", RIX, BODEN, FH, [("urteil", "ruhig"), ("ri1", "!redet"), ("ergeb", "ruhig")], erst="pop"),
    feld(*BANK, "urteil", fill=HOLZ, rand=5, rund=12, anim="pop", name="richterbank"),
    fall_ns("RI", RIX, "urteil", d=0.1),
    *person("JO", JGX, BODEN, FH, [("urteil", "ruhig_r"), ("ri1", "liest_r"), ("ergeb", "denkt_r"), ("prue", "ruhig_r"),
                                   ("bu", "froh_r")], erst="pop"),
    fall_ns("JO", JGX, "urteil", d=0.1),
    blase("sprech", 900, 260, "ri1", 960, 200, inhalt=["Das beklagte Land wird verpflichtet,",
                                                       "die Klausur neu bewerten zu lassen und",
                                                       "die Klägerin neu zu bescheiden.",
                                                       "Im Übrigen wird die Klage abgewiesen."], textsize=30,
          figur=RIa, bis="ergeb"),
    pl("in der Regel: Neubewertung", 860, 110, "ergeb", fill=GRUEN, size=34, anker="m"),
    pl("keine Note vom Gericht", 860, 185, beim("ergeb", "keine"), fill=WEISS, size=30, anker="m"),
    pl("9 Punkte einklagen? nein", 860, 255, "neun", fill=ROT, size=30, anker="m"),
    pl("Die Prüfer bewerten neu, ohne den Fehler.", 860, 325, "prue", fill=BLAUHELL, size=30, anker="m"),
    pl("mehr Punkte? offen", 860, 395, "offen", fill=GELB, size=30, anker="m"),
    pl("Bescheidungsurteil, § 113 Abs. 5 S. 2 VwGO", 860, 465, "bu", fill=WEISS, size=30, anker="m"),
])

# ===========================================================================================================================
# H Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Fachfrage oder Wertung")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Trenne sauber:", 200, 200, beim("tipp", "Trenne"), "Bold", 36),
    z("Fachfrage oder prüfungsspezifische Wertung?", 200, 255, beim("tipp", "Fachfrage"), "ExtraBold", 34),
    *okz("Fachfrage: voll, mit dem Antwortspielraum", 360, "tipp2", "Bold", 32, x=245),
    *okz("Wertung: nur die Grenzen", 425, beim("tipp2", "Wertung"), "Bold", 32, x=245),
    z("Klageziel in der Regel:", 200, 530, "tipp3", "Bold", 34),
    z("Neubewertung, nicht eine bestimmte Note", 200, 585, beim("tipp3", "Neubewertung"), "ExtraBold", 34),
    dicon("tabler", "scale", 420, 820, 130, "tipp2", fuell=WEISS),
    dicon("tabler", "reload", 800, 820, 120, beim("tipp3", "Neubewertung"), fuell=WEISS),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# I Klausurschema (progressiv)
# ===========================================================================================================================
REIHEN = [("s1", "1.", "Verfahrensfehler, auch beim Überdenken", BLAU, 0),
          ("s2", "2.", "Fehler bei Fachfragen: Antwortspielraum", GRUEN, 0),
          ("s3", "3.", "Grenzen des Beurteilungsspielraums", GELB, 0),
          ("s3a", "", "Sachverhalt, Maßstäbe, sachfremde Erwägungen", None, 1),
          ("s4", "4.", "Auswirkung auf die Note", LILA, 0),
          ("s5", "5.", "Folge: Neubewertung durch die Prüfer", ORANGE, 0)]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Schema: Begründetheit"), 110, 90, "sch", 46)]
y = 210
for c, r, txt, farbe, ebene in REIHEN:
    if ebene == 0:
        els_sch += [karte(110, y, 110, 66, c, fill=farbe, rund=14, schatten=5, rand=4),
                    z(r, 165 - F("ExtraBold", 36).getlength(r) / 2, y + 9, c, "ExtraBold", 36, rechts=1820),
                    z(txt, 255, y + 9, c, "ExtraBold", 36, rechts=1820)]
        y += 100
    else:
        els_sch.append(ok(290, y + 22, c, gr=18))
        els_sch.append(z(txt, 330, y, c, "Bold", 34, rechts=1820))
        y += 80
assert y <= 960, y
folie([("sch", "Schema · Begründetheit"), ("s1", "Schema › 1. Verfahrensfehler"), ("s2", "Schema › 2. Fachfragen"),
       ("s3", "Schema › 3. Grenzen des Beurteilungsspielraums"), ("s4", "Schema › 4. Auswirkung auf die Note"),
       ("s5", "Schema › 5. Folge: Neubewertung")], els_sch)

# ===========================================================================================================================
# J Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Bei ", 0), ("prüfungsspezifischen", "a"), (" Wertungen", 0)],
                 [("haben die Prüfer ", 0), ("Spielraum.", "b")]],
                750, 300, 50, "merke", {"a": beim("merke", "prüfungsspezifischen"), "b": beim("merke", "Spielraum")}),
    *markertext([[("Bei ", 0), ("Fachfragen", "c"), (" nicht: Was vertretbar", 0)],
                 [("und gut begründet ist,", 0)], [("darf nicht ", 0), ("falsch", "d"), (" sein.", 0)]],
                750, 520, 50, "m2", {"c": beim("m2", "Fachfragen"), "d": beim("m2", "falsch")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
