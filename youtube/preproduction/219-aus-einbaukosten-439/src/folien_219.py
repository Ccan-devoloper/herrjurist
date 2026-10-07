"""Folge 219 · Aus- und Einbaukosten § 439 III BGB: Der Fliesen-Fall Weber/Putz – Serienstandard Open Peeps (Katzenkönig).
Fall: Herr Oltmann kauft im Fliesenhandel von Frau Reinecke Fliesen für 1.400 €; ein Fliesenleger verlegt sie im ganzen Bad;
erst auf der fertigen Fläche zeigen sich deutliche Farbunterschiede (Herstellungsfehler). Ausbau und neu verlegen: 5.200 €.
Szenen laut ../SZENENPLAN.md: A1 Fliesenhandel, A2 Bad (Verlegen, Farbfehler, Fliesenleger), A3 zurück im Fliesenhandel
(Blasen, Frage), B Sachverhalt, C I. Sachmangel und Nacherfüllung, D Hintergrund vor 2018, E EuGH Weber/Putz, F BGH,
G § 439 Abs. 3 (Wortlautkarte), H II. Einbau, I III. Aufwendungen, J1 IV. Verweigerung (Wortlautkarte § 439 Abs. 4),
J2 IV. heute, K Ergebnis und Regress § 445a, L Klausurtipp (Lexi), M Schema, N Merksatz (Lexi).
Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/feld/requisit/stehend/paar als eigene Kopie aus
Folge 217 (gemeinsame Dateien unverändert); neu: fliesen() (Fliesenfläche, mit Farbfehler), regal(), theke().
Ein Handlungsgeräusch: gesetzte Fliese (Freesound CC0 232978, ../geraeusche_herkunft.json).
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut BGB nach gesetze-im-internet.de, Abruf 07.10.2026.
DARSTELLUNG: keine echten Baumarkt- oder Fliesenmarken; alle Personen fiktiv; Weber/Putz nur als Name der Entscheidung."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_219/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_219/" in n:
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 160/203/217) ---------------------------------
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
NAME = {"OL": "Herr Oltmann", "RE": "Frau Reinecke", "FL": "Fliesenleger"}
NFARBE = {"OL": GRUEN, "RE": ROT, "FL": BLAU}


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


def paar(af, bf, a="OL", b="RE"):
    """Tafelszene: Herr Oltmann (links) und Frau Reinecke (rechts) neben der Tafel, beide blicken zur Tafel."""
    return [*stehend(a, X1, af), *stehend(b, X2, bf)]


def fall_ns(k, x, cue, **kw):
    return ns(NAME[k], x, BODEN, cue, NFARBE[k], **kw)


# --- eigene Szenenbausteine Folge 219 --------------------------------------------------------------------------------------
FLIESE = (214, 232, 244, 255)               # hellblaue Fliese
FUGE = (150, 160, 170, 255)


def fliesen(cols, rows, kante, fehler=False, nur=None):
    """Fliesenfläche (programmatisch): cols × rows Fliesen der Kantenlänge kante, Fugen grau, Rahmen Tusche.
    fehler=True: deutliche Farbunterschiede (Schlieren in mehreren Tönen) als sichtbarer Mangel.
    nur = Menge (i, j), die gezeichnet werden (für das Verlegen in Etappen)."""
    s = 2
    W_, H_ = cols * kante, rows * kante
    im = Image.new("RGBA", ((W_ + 12) * s, (H_ + 12) * s)); dr = ImageDraw.Draw(im)
    o = 6 * s
    toene = [(214, 232, 244), (188, 206, 222), (232, 222, 196), (176, 196, 214), (222, 236, 246)]
    for i in range(cols):
        for j in range(rows):
            if nur is not None and (i, j) not in nur:
                continue
            x0, y0 = o + i * kante * s, o + j * kante * s
            farbe = FLIESE[:3]
            if fehler:
                farbe = toene[(i * 3 + j * 2 + (i * j) % 3) % len(toene)]
            dr.rectangle((x0, y0, x0 + kante * s, y0 + kante * s), fill=farbe + (255,), outline=FUGE, width=3 * s)
            if fehler and (i + 2 * j) % 3 == 0:          # Schliere quer über die Fliese
                for k in range(3):
                    yy = y0 + (0.3 + 0.18 * k) * kante * s
                    dr.line((x0 + 6 * s, yy, x0 + kante * s - 6 * s, yy - 0.25 * kante * s), fill=(150, 165, 185, 255),
                            width=4 * s)
    if nur is None:
        dr.rectangle((o, o, o + W_ * s, o + H_ * s), outline=INK, width=5 * s)
    return im.resize((W_ + 12, H_ + 12), Image.LANCZOS)


def fliesen_el(x, y, cols, rows, kante, cue, fehler=False, nur=None, bis=None, anim="cut", name="fliesen"):
    return El(fliesen(cols, rows, kante, fehler, nur), x, y, cue, anim, 0.0, bis, name=name)


THEKE_X, THEKE_Y, THEKE_W = 520, 660, 560   # Ladentheke
RE_X, OL_X = 330, 1400                      # Frau Reinecke links (blickt nach rechts), Herr Oltmann rechts (nach links)


def laden(c0, hart_=True):
    """Fliesenhandel: Bodenlinie, Theke, Wandregal mit Fliesenkartons (eigene Formen, keine Marken)."""
    an = "cut" if hart_ else "pop"
    els = [boden(c0, hart_), karte(THEKE_X, THEKE_Y, THEKE_W, BODEN - THEKE_Y, c0, fill=HOLZ, rund=10, schatten=6, rand=5,
                                   anim="cut" if hart_ else "fade"),
           karte(1500, 318, 360, 18, c0, fill=HOLZ, rund=6, schatten=4, rand=4, anim="cut" if hart_ else "fade")]
    for cx, fu in ((1570, BLAU), (1680, GRUEN), (1790, GELB)):
        els.append(ficon("tabler", "package", cx, 318, 100, c0, fuell=fu, anim=an))
    return els


# ===========================================================================================================================
# A1 Fall: Kauf im Fliesenhandel
# ===========================================================================================================================
folie([(NULL, "Fall · Kauf im Fliesenhandel")], [
    *laden(NULL),
    hart(pl("Im Fliesenhandel von Frau Reinecke", 70, 30, NULL, fill=GELB, size=40)),
    hart(fliesen_el(600, THEKE_Y - 92, 4, 1, 90, NULL, name="muster")),
    ficon("tabler", "package", 1000, THEKE_Y, 120, beim("fall", "neue"), fuell=BLAU),
    pl("neue Fliesen", 870, 470, beim("fall", "neue"), fill=WEISS, size=34),
    ficon("tabler", "bath", 760, 420, 140, beim("fall", "Bad"), fuell=WEISS),
    pl("fürs Bad", 610, 300, beim("fall", "Bad"), fill=WEISS, size=34),
    pl("1.400 €", 1020, 370, beim("fall", "tausendvierhundert"), fill=GELB, size=36),
    *fig("RE", RE_X, BODEN, FH, [(NULL, "froh_r")], erst="cut"),
    hart(fall_ns("RE", RE_X, NULL)),
    *fig("OL", OL_X, BODEN, FH, [(NULL, "ruhig"), (beim("fall", "Bad"), "froh")], erst="cut"),
    hart(fall_ns("OL", OL_X, NULL)),
])

# ===========================================================================================================================
# A2 Fall: Das Bad – verlegt, Farbfehler, der Fliesenleger
# ===========================================================================================================================
WX, WY, WK, WC, WR = 120, 300, 80, 11, 7      # Fliesenwand: links, oben, Kante, Spalten, Zeilen
FLX, OLX2 = 1260, 1660
UNTEN_HAELFTE = {(i, j) for i in range(WC) for j in range(3, WR)}
OHNE_LETZTE = {(i, j) for i in range(WC) for j in range(WR)} - {(WC - 1, 0)}
GANZ = beim("verleg", "ganzen")
LETZTE = beim("verleg", "Bad", ende=True)
TAG = beim("schlier", "Tageslicht")
DEUT = beim("schlier", "deutliche")
folie([("verleg", "Fall · Die Fliesen werden verlegt"), ("schlier", "Fall · Farbfehler im ganzen Bad"),
       ("fl1", "Fall · Alles wieder raus?")], [
    boden("verleg"),
    bis_(fliesen_el(WX, WY, WC, WR, WK, "verleg", nur=UNTEN_HAELFTE, anim="pop", name="fliesen_unten"), GANZ),
    bis_(fliesen_el(WX, WY, WC, WR, WK, GANZ, nur=OHNE_LETZTE, name="fliesen_fast"), LETZTE),
    bis_(szene(fliesen_el(WX, WY, WC, WR, WK, LETZTE, name="fliesen_fertig"), "219fliese*", 0.8), DEUT),
    fliesen_el(WX, WY, WC, WR, WK, DEUT, fehler=True, name="fliesen_fehler"),
    ficon("tabler", "bath", 600, BODEN, 560, "verleg", fuell=WEISS),
    pl("im ganzen Bad", 70, 30, GANZ, fill=GELB, size=40),
    ficon("tabler", "sun", 1100, 250, 110, TAG, fuell=GELB),
    pl("im Tageslicht", 420, 30, TAG, fill=WEISS, size=36),
    pl("deutliche Farbunterschiede", 120, 130, beim("schlier", "Farbunterschiede"), fill=ROT, size=36),
    pl("Fehler aus der Herstellung", 120, 215, beim("schlier", "Herstellung"), fill=WEISS, size=32),
    pl("nicht behebbar", 640, 215, beim("schlier", "beheben"), fill=WEISS, size=32),
    *fig("FL", FLX, BODEN, FH, [("verleg", "ruhig"), (DEUT, "denkt")], erst="pop", bis="fl1"),
    ns(NAME["FL"], FLX, BODEN, "verleg", NFARBE["FL"], d=0.1),
    *redet("FL_redet_r", FLX, BODEN, FH, "fl1", "ol1"),
    *fig("OL", OLX2, BODEN, FH, [("schlier", "ruhig"), (DEUT, "sorge"), ("fl1", "sorge")], erst="pop"),
    fall_ns("OL", OLX2, "schlier", d=0.1),
    blase("sprech", 640, 250, "fl1", 1420, 175, inhalt=["Die Fliesen müssen", "alle wieder raus.", "Ausbauen und neu verlegen",
                                                       "kostet 5.200 €."],
          textsize=34, figur=("FL_redet_r", FLX, BODEN, FH)),
])

# ===========================================================================================================================
# A3 Fall: Zurück im Fliesenhandel – Herr Oltmann und Frau Reinecke
# ===========================================================================================================================
folie([("ol1", "Fall · Zurück im Fliesenhandel"), ("frage", "Fall · Die Frage")], [
    *laden("ol1", hart_=False),
    fliesen_el(600, THEKE_Y - 92, 4, 1, 90, "ol1", fehler=True, anim="fade", name="muster_fehler"),
    *redet("OL_redet", OL_X, BODEN, FH, "ol1", "re1"),
    *fig("OL", OL_X, BODEN, FH, [("re1", "aerger"), ("frage", "denkt")], erst="cut"),
    fall_ns("OL", OL_X, "ol1", d=0.1),
    blase("sprech", 600, 200, "ol1", 1010, 215, inhalt=["Ich brauche neue Fliesen.", "Und Sie zahlen den Ausbau",
                                                        "und das Verlegen."],
          textsize=36, figur=("OL_redet", OL_X, BODEN, FH), bis="re1"),
    *fig("RE", RE_X, BODEN, FH, [("ol1", "ruhig_r")], erst="pop", bis="re1"),
    fall_ns("RE", RE_X, "ol1", d=0.2),
    *redet("RE_redet_r", RE_X, BODEN, FH, "re1", "frage"),
    *fig("RE", RE_X, BODEN, FH, [("frage", "denkt_r")], erst="cut"),
    blase("sprech", 690, 250, "re1", 790, 200, inhalt=["Neue Fliesen bekommen Sie.", "Aber ich habe Ihnen Fliesen",
                                                       "verkauft, nicht das Verlegen."],
          textsize=36, figur=("RE_redet_r", RE_X, BODEN, FH), bis="frage"),
    pl("Muss Frau Reinecke auch Ausbau und Einbau bezahlen?", 120, 170, "frage", fill=PINK, size=38),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_219(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 56)]
    y = 205
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=40, zeilenabstand=1.30)
        els += e; y += 14
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=36))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_219("sv", [
    "Herr Oltmann kauft für sein eigenes Bad im Fliesenhandel von Frau Reinecke neue Fliesen für 1.400 Euro. Ein "
    "Fliesenleger verlegt sie im ganzen Bad. Erst auf der fertigen Fläche zeigen sich im Tageslicht deutliche "
    "Farbunterschiede: ein Fehler aus der Herstellung, der sich nicht beheben lässt. Frau Reinecke wusste davon nichts.",
    "Fliesenleger: „Die Fliesen müssen alle wieder raus. Ausbauen und neu verlegen kostet 5.200 Euro.“ Herr Oltmann "
    "verlangt neue Fliesen und die 5.200 Euro. Frau Reinecke: „Neue Fliesen bekommen Sie. Aber ich habe Ihnen Fliesen "
    "verkauft, nicht das Verlegen.“",
], "Muss Frau Reinecke auch Ausbau und Einbau bezahlen?")

# ===========================================================================================================================
# C I. Sachmangel und Nacherfüllung
# ===========================================================================================================================
folie([("mang", "I. Sachmangel und Nacherfüllung"), ("m1", "I. › Sachmangel, § 434 Abs. 3 BGB"),
       ("ne", "I. › Nacherfüllung, § 439 Abs. 1 BGB")], rechts_frei([
    *tafel("mang", "I. Sachmangel und Nacherfüllung"),
    z("Fliesen mit deutlichen Farbunterschieden:", 110, 190, "m1", "Bold", 34),
    *neinz("nicht die übliche Beschaffenheit", 250, beim("m1", "übliche"), "Bold", 34, x=160),
    *okz("Sachmangel, § 434 Abs. 3 Satz 1 Nr. 2 BGB", 315, beim("m1", "Paragraf"), "Bold", 34, x=160),
    blk(110, 395, 1040, 80, GELB, "m059", [("Mehr dazu: Video zum Sachmangel", "Bold", 34, INK)]),
    *okz("Nacherfüllung, § 439 Abs. 1 BGB", 515, "ne", "Bold", 36, x=160, haken=beim("ne", "verlangen")),
    *neinz("Nachbessern: nicht möglich", 590, beim("ne2", "Nachbessern"), "Bold", 34, x=160, kreuz=beim("ne2", "nicht")),
    *okz("bleibt: Lieferung neuer Fliesen", 655, beim("ne2", "bleibt"), "Bold", 34, x=160),
    blk(110, 745, 1040, 80, GELB, "v063", [("Alle Käuferrechte: Video zu § 437 BGB", "Bold", 34, INK)]),
    *requisit([("mang", ("tabler", "texture", 110, BLAU), "Farbfehler", ROT),
               ("ne", ("tabler", "refresh", 100, WEISS), "Nacherfüllung", GRUEN),
               (beim("ne2", "bleibt"), ("tabler", "package", 110, BLAU), "neue Fliesen", GRUEN)]),
    *paar([("mang", "sorge"), ("ne", "ruhig")], [("mang", "ernst"), ("ne2", "ruhig")]),
]))

# ===========================================================================================================================
# D Hintergrund: Rechtslage vor 2018
# ===========================================================================================================================
folie([("alt", "Hintergrund · Rechtslage vor 2018")], rechts_frei([
    *tafel("alt", "Hintergrund: Rechtslage vor 2018"),
    z("Umfasst die Lieferung neuer Fliesen auch", 110, 190, beim("alt", "umfasst"), "Bold", 34),
    z("den Ausbau der alten und das Verlegen der neuen?", 110, 240, beim("alt", "Ausbau"), "Bold", 34),
    z("Früher in Deutschland:", 110, 340, "alt1", "Bold", 34),
    z("Der Verkäufer bringt nur neue Fliesen.", 160, 395, beim("alt1", "Verkäufer"), "Regular", 34),
    z("Ausbau und Einbau nur als Schadensersatz,", 160, 460, "alt2", "Regular", 34),
    z("also nur bei Verschulden", 160, 515, beim("alt2", "Verschulden"), "Bold", 34),
    *neinz("Händlerin: Herstellungsfehler nicht bekannt,", 615, "alt3", "Bold", 34, x=160, kreuz=beim("alt3", "kein")),
    z("in der Regel kein Verschulden", 160, 670, beim("alt3", "kein"), "Bold", 34),
    zit("vgl. BT-Drs. 18/8486, S. 38 f.", 110, 780, "alt1"),
    *requisit([("alt", ("tabler", "question-mark", 90, WEISS), "Ausbau und Verlegen?", WEISS),
               ("alt1", ("tabler", "truck-delivery", 130, WEISS), "nur neue Fliesen", WEISS),
               ("alt2", ("tabler", "scale", 110, WEISS), "nur bei Verschulden", GELB),
               ("alt3", ("tabler", "building-factory-2", 120, WEISS), "Fehler aus der Herstellung", WEISS)]),
    *paar([("alt", "denkt"), ("alt2", "sorge")], [("alt", "denkt"), ("alt3", "ruhig")]),
]))

# ===========================================================================================================================
# E EuGH, Weber/Putz (2011)
# ===========================================================================================================================
folie([("eugh", "Hintergrund · EuGH, Weber/Putz, 2011"), ("eu1", "Hintergrund · EuGH › Ausbau und Einbau oder Kosten"),
       ("eu4", "Hintergrund · EuGH › keine Verweigerung, angemessener Betrag")], rechts_frei([
    *tafel("eugh", "EuGH: Weber/Putz (2011)"),
    zit("EuGH, Urt. v. 16.6.2011 – C-65/09, C-87/09 (Weber/Putz)", 110, 168, "eugh"),
    z("Verbrauchsgüterkaufrichtlinie: Der Verkäufer muss", 110, 215, "eu1", "Bold", 32),
    blk(110, 270, 500, 92, GRUEN, beim("eu1", "selbst"), [("selbst ausbauen", "Bold", 30, INK), ("und einbauen", "Bold", 30, INK)]),
    z("oder", 620, 296, beim("eu1", "oder"), "ExtraBold", 32),
    blk(700, 270, 450, 92, GRUEN, beim("eu1", "Kosten"), [("die Kosten tragen", "Bold", 30, INK)]),
    z("auch ohne Einbaupflicht im Vertrag", 110, 385, "eu2", "Bold", 32),
    zit("Rn. 62", 1060, 395, "eu2"),
    z("sonst nicht unentgeltlich: Einbau 2 × bezahlt", 110, 450, "eu3", "Bold", 32),
    zit("Rn. 47, 49", 1020, 460, beim("eu3", "zweimal")),
    *neinz("keine Verweigerung der einzig möglichen Abhilfe", 530, "eu4", "Bold", 32, x=160, kreuz=beim("eu4", "verweigern")),
    zit("Rn. 71, 73, 78", 160, 580, beim("eu4", "verweigern")),
    blk(110, 640, 1040, 120, HELL, "eu5", [("aber: Erstattung begrenzt auf", "Bold", 32, INK),
                                          ("einen angemessenen Betrag", "ExtraBold", 34, INK)]),
    zit("Rn. 74, 76–78", 110, 775, beim("eu5", "angemessenen")),
    *requisit([("eugh", ("tabler", "building-bank", 120, BLAU), "Europäischer Gerichtshof", BLAU),
               ("eu3", ("tabler", "coin-euro", 100, GELB), "Einbau 2 × bezahlt?", ROT),
               ("eu5", ("tabler", "scale", 110, WEISS), "angemessener Betrag", GELB)]),
    *paar([("eugh", "denkt"), ("eu1", "froh")], [("eugh", "ernst"), ("eu5", "denkt")]),
]))

# ===========================================================================================================================
# F BGH: Umsetzung und Grenze
# ===========================================================================================================================
DY = 560
folie([("bgh", "Hintergrund · BGH, Fliesen-Fall, VIII ZR 70/08"), ("bgh2", "Hintergrund · BGH › nicht zwischen Unternehmern")],
      rechts_frei([
    *tafel("bgh", "BGH: Umsetzung und Grenze"),
    *okz("deutscher Fliesen-Fall: Ausbaukosten", 190, "bgh", "Bold", 34, x=160),
    z("auf 600 € begrenzt", 160, 245, beim("bgh", "sechshundert"), "ExtraBold", 36),
    zit("BGH, Urt. v. 21.12.2011 – VIII ZR 70/08, Rn. 25, 35, 54", 160, 305, beim("bgh", "sechshundert")),
    *neinz("zwischen Unternehmern galt das nicht", 380, "bgh2", "Bold", 34, x=160, kreuz=beim("bgh2", "nicht")),
    zit("BGH, Urt. v. 17.10.2012 – VIII ZR 226/11, Rn. 17", 160, 435, beim("bgh2", "nicht")),
    dicon("tabler", "building-store", 240, DY + 130, 130, beim("bgh2", "Handwerker"), fuell=GELB),
    pfeil(330, DY + 60, 500, DY + 60, beim("bgh2", "Material"), breite=7, kopf=22, farbe=INK),
    dicon("tabler", "tools", 620, DY + 130, 120, beim("bgh2", "Handwerker"), fuell=WEISS),
    pfeil(720, DY + 60, 890, DY + 60, beim("bgh2", "Kunden"), breite=7, kopf=22, farbe=INK),
    dicon("tabler", "home", 1010, DY + 130, 130, beim("bgh2", "Kunden"), fuell=WEISS),
    pl("Händler", 180, DY + 160, beim("bgh2", "Material"), fill=WEISS, size=28),
    pl("Handwerker", 535, DY + 160, beim("bgh2", "Handwerker"), fill=WEISS, size=28),
    pl("Kunde", 960, DY + 160, beim("bgh2", "Kunden"), fill=WEISS, size=28),
    z("kauft Material", 345, DY + 230, beim("bgh2", "Material"), "Bold", 28),
    z("baut beim Kunden ein", 690, DY + 230, beim("bgh2", "einbaut"), "Bold", 28),
    *requisit([("bgh", ("tabler", "gavel", 110, WEISS), "Bundesgerichtshof", BLAU),
               ("bgh2", ("tabler", "hand-stop", 100, ROT), "nur beim Verbrauchsgüterkauf", ROT)]),
    *paar([("bgh", "ruhig"), ("bgh2", "denkt")], [("bgh", "denkt"), ("bgh2", "ernst")]),
]))

# ===========================================================================================================================
# G § 439 Abs. 3 BGB heute (Wortlautkarte)
# ===========================================================================================================================
W439III = ("„Hat der Käufer die mangelhafte Sache gemäß ihrer Art und ihrem Verwendungszweck in eine andere Sache "
           "eingebaut oder an eine andere Sache angebracht, bevor der Mangel offenbar wurde, ist der Verkäufer im Rahmen "
           "der Nacherfüllung verpflichtet, dem Käufer die erforderlichen Aufwendungen für das Entfernen der mangelhaften "
           "und den Einbau oder das Anbringen der nachgebesserten oder gelieferten mangelfreien Sache zu ersetzen.“")
w3, w3_y = wortlaut(110, 270, 1040, W439III, "§ 439 Abs. 3 BGB", "w1", marken=[
    ("gemäß ihrer Art und ihrem Verwendungszweck", beim("w1", "gemäß")),
    ("eingebaut", beim("w1", "eingebaut")),
    ("bevor der Mangel offenbar wurde", "w2"),
    ("im Rahmen", beim("w3", "Rahmen")),
    ("erforderlichen Aufwendungen", beim("w3", "erforderlichen")),
    ("Entfernen", beim("w3", "Entfernen")),
    ("Einbau", beim("w3", "Einbau"))], size=30)
folie([("heute", "§ 439 Abs. 3 BGB · seit 2018"), ("w1", "§ 439 Abs. 3 BGB › Wortlaut")], rechts_frei([
    *tafel("heute", "Aus- und Einbaukosten heute"),
    z("seit 1.1.2018: für alle Kaufverträge", 110, 180, beim("heute", "alle"), "Bold", 36),
    zit("G v. 28.4.2017, BGBl. I S. 969; BT-Drs. 18/8486, S. 39", 110, 228, beim("heute", "alle")),
    *w3,
    *requisit([("heute", ("tabler", "book", 110, WEISS), "für alle Kaufverträge", GELB),
               ("w2", ("tabler", "eye", 110, WEISS), "vorher nicht offenbar", WEISS),
               ("w3", ("tabler", "cash-banknote", 120, GRUEN), "Aufwendungen ersetzen", GRUEN)]),
    *paar([("heute", "ruhig"), ("w3", "froh")], [("heute", "ernst"), ("w1", "denkt")]),
]))

# ===========================================================================================================================
# H II. Einbau, bevor der Mangel offenbar wurde
# ===========================================================================================================================
folie([("ein", "II. Einbau, § 439 Abs. 3 BGB"), ("ein2", "II. Einbau › bevor der Mangel offenbar wurde"),
       ("kenn", "II. Einbau › früher Satz 2 mit § 442 BGB")], rechts_frei([
    *tafel("ein", "II. Einbau"),
    *okz("Fliesen verlegt: gemäß Art und Verwendungszweck", 190, "ein1", "Bold", 32, x=160, haken=beim("ein1", "gemacht")),
    *okz("Farbunterschiede erst auf der fertigen Fläche:", 260, "ein2", "Bold", 32, x=160, haken=beim("ein2", "nicht")),
    z("vorher nicht offenbar", 160, 310, beim("ein2", "nicht"), "ExtraBold", 34),
    blk(110, 400, 1040, 210, HELL, "kenn", [("Achtung, ältere Bücher:", "ExtraBold", 34, INK),
                                           ("bis 31.12.2021 Satz 2 mit § 442 BGB:", "Bold", 32, INK),
                                           ("schon grob fahrlässige Unkenntnis", "Bold", 32, INK),
                                           ("beim Einbau schadete", "Bold", 32, INK)]),
    *neinz("Satz 2 gibt es nicht mehr", 655, "kenn2", "ExtraBold", 36, x=160, kreuz=beim("kenn2", "nicht")),
    zit("seit 1.1.2022; Art. 229 § 58 EGBGB; BT-Drs. 19/27424, S. 25 f.", 160, 710, beim("kenn2", "nicht")),
    *requisit([("ein", ("tabler", "wall", 110, BLAU), "verlegt", WEISS),
               ("ein2", ("tabler", "texture", 110, BLAU), "erst auf der fertigen Fläche", ROT),
               ("kenn", ("tabler", "books", 110, GELB), "ältere Bücher", GELB),
               ("kenn2", ("tabler", "x", 100, ROT), "Satz 2 aufgehoben", ROT)]),
    *paar([("ein", "ruhig"), ("ein2", "froh"), ("kenn", "denkt")], [("ein", "ruhig"), ("kenn", "ernst")]),
]))

# ===========================================================================================================================
# I III. Erforderliche Aufwendungen
# ===========================================================================================================================
folie([("auf", "III. Erforderliche Aufwendungen"), ("geld", "III. › Geld statt Selbstvornahme"),
       ("vors", "III. › Vorschuss, § 475 Abs. 5 BGB")], rechts_frei([
    *tafel("auf", "III. Erforderliche Aufwendungen"),
    *okz("Ausbau und neu verlegen: 5.200 €", 190, beim("auf1", "fünftausendzweihundert"), "Bold", 36, x=160),
    *neinz("Verschulden: nicht nötig", 270, "auf2", "Bold", 34, x=160, kreuz=beim("auf2", "nicht")),
    *neinz("Einbau im Kaufvertrag: nicht nötig", 340, "auf3", "Bold", 34, x=160, kreuz=beim("auf3", "nicht")),
    blk(110, 430, 1040, 140, GRUEN, "geld", [("Herr Oltmann bekommt Geld", "ExtraBold", 36, INK),
                                            ("Frau Reinecke muss nicht selbst ausbauen", "Bold", 32, INK)]),
    zit("vgl. BT-Drs. 19/27424, S. 26", 110, 585, beim("geld", "selbst")),
    *okz("Verbraucher: Vorschuss, § 475 Abs. 5 BGB", 650, beim("vors", "Vorschuss"), "Bold", 34, x=160),
    *requisit([("auf1", ("tabler", "file-invoice", 110, WEISS), "5.200 €", GELB),
               ("geld", ("tabler", "cash-banknote", 120, GRUEN), "Geld", GRUEN),
               ("vors", ("tabler", "coin-euro", 100, GELB), "Vorschuss", GELB)]),
    *paar([("auf", "ruhig"), ("geld", "froh")], [("auf", "ernst"), ("geld", "denkt")]),
]))

# ===========================================================================================================================
# J1 IV. Verweigerung, § 439 Abs. 4 BGB (Wortlautkarte)
# ===========================================================================================================================
W439IV = ("„Der Verkäufer kann die vom Käufer gewählte Art der Nacherfüllung unbeschadet des § 275 Abs. 2 und 3 "
          "verweigern, wenn sie nur mit unverhältnismäßigen Kosten möglich ist. Dabei sind insbesondere der Wert der "
          "Sache in mangelfreiem Zustand, die Bedeutung des Mangels und die Frage zu berücksichtigen, ob auf die andere "
          "Art der Nacherfüllung ohne erhebliche Nachteile für den Käufer zurückgegriffen werden könnte. …“")
w4, w4_y = wortlaut(110, 175, 1040, W439IV, "§ 439 Abs. 4 Satz 1, 2 BGB", "v1", marken=[
    ("gewählte Art der Nacherfüllung", beim("v1", "gewählte")),
    ("verweigern", beim("v1", "verweigern")),
    ("unverhältnismäßigen Kosten", beim("v1", "unverhältnismäßigen")),
    ("Wert der", beim("v2", "Wert")),
    ("Bedeutung des Mangels", beim("v2", "Bedeutung"))], size=30)
folie([("verw", "IV. Verweigerung, § 439 Abs. 4 BGB"), ("v3", "IV. Verweigerung › Abwägung im Fall")], rechts_frei([
    *tafel("verw", "IV. Kann die Verkäuferin verweigern?"),
    *w4,
    blk(110, w4_y + 30, 500, 110, ROT, beim("v3", "fünftausendzweihundert"), [("5.200 €", "ExtraBold", 38, INK),
                                                                              ("Einbaukosten", "Bold", 30, INK)]),
    z("neben", 625, w4_y + 68, beim("v3", "neben"), "ExtraBold", 32),
    blk(740, w4_y + 30, 410, 110, BLAUHELL, beim("v3", "Fliesen"), [("1.400 €", "ExtraBold", 38, INK),
                                                                   ("Fliesen", "Bold", 30, INK)]),
    *requisit([("verw", ("tabler", "hand-stop", 100, WEISS), "verweigern?", WEISS),
               ("v2", ("tabler", "scale", 120, WEISS), "Abwägung", GELB)]),
    *paar([("verw", "denkt"), ("v3", "sorge")], [("verw", "denkt"), ("v3", "ernst")]),
]))

# ===========================================================================================================================
# J2 IV. Verweigerung heute: Wegfall der Weber/Putz-Sonderregel
# ===========================================================================================================================
folie([("v4", "IV. Verweigerung › § 475 Abs. 4 BGB a. F. gestrichen"), ("v7", "IV. Verweigerung › im Fall")], rechts_frei([
    *tafel("v4", "IV. Verweigerung seit 2022"),
    z("Sonderregel aus Weber/Putz für Verbraucher,", 110, 185, "v4", "Bold", 32),
    *neinz("§ 475 Abs. 4 BGB a. F.: seit 2022 gestrichen", 245, beim("v4", "Paragraf"), "Bold", 34, x=160,
           kreuz=beim("v4", "gestrichen")),
    z("Gesetzesbegründung: auch beim Verbraucher keine", 110, 335, "v5", "Bold", 32),
    z("unverhältnismäßige Leistung", 110, 385, beim("v5", "unverhältnismäßige"), "ExtraBold", 34),
    zit("BT-Drs. 19/27424, S. 29", 110, 435, beim("v5", "unverhältnismäßige")),
    *okz("Käufer: Rücktritt oder Minderung", 490, "v6", "Bold", 34, x=160, haken=beim("v6", "zurücktreten")),
    blk(110, 590, 1040, 140, GRUEN, "v7", [("Frau Reinecke verweigert nicht:", "ExtraBold", 36, INK),
                                          ("sie bietet neue Fliesen an", "Bold", 34, INK)]),
    *requisit([("v4", ("tabler", "x", 100, ROT), "§ 475 Abs. 4 a. F.", ROT),
               ("v6", ("tabler", "arrow-back-up", 100, WEISS), "Rücktritt oder Minderung", WEISS),
               ("v7", ("tabler", "package", 110, BLAU), "neue Fliesen", GRUEN)]),
    *paar([("v4", "denkt"), ("v7", "froh")], [("v4", "ruhig"), ("v7", "froh")]),
]))

# ===========================================================================================================================
# K Ergebnis und Regress, § 445a BGB
# ===========================================================================================================================
RY = 560
folie([("erg", "Ergebnis"), ("regr", "Ausblick · Regress, § 445a BGB")], rechts_frei([
    *tafel("erg", "Ergebnis"),
    *okz("neue Fliesen liefern", 190, beim("erg", "neue"), "Bold", 36, x=160),
    *okz("5.200 € für Ausbau und Einbau ersetzen", 260, "erg2", "Bold", 36, x=160, haken=beim("erg2", "ersetzen")),
    z("Regress, § 445a Abs. 1 BGB:", 110, 370, beim("regr", "Paragraf"), "ExtraBold", 34),
    dicon("tabler", "building-factory-2", 240, RY + 120, 130, beim("regr", "Lieferanten"), fuell=WEISS),
    pfeil(500, RY + 50, 340, RY + 50, beim("regr", "Lieferanten"), breite=7, kopf=22, farbe=INK),
    dicon("tabler", "building-store", 620, RY + 120, 130, beim("regr", "Paragraf"), fuell=GELB),
    pfeil(890, RY + 50, 730, RY + 50, "erg2", breite=7, kopf=22, farbe=INK),
    dicon("tabler", "home", 1010, RY + 120, 130, "erg", fuell=WEISS),
    pl("Lieferant", 170, RY + 150, beim("regr", "Lieferanten"), fill=WEISS, size=28),
    pl("Frau Reinecke", 520, RY + 150, beim("regr", "Paragraf"), fill=ROT, size=28),
    pl("Herr Oltmann", 900, RY + 150, "erg", fill=GRUEN, size=28),
    z("wenn der Mangel schon bei der Lieferung an sie bestand", 110, RY + 240, beim("regr", "schon"), "Bold", 32),
    *requisit([("erg", ("tabler", "package", 110, BLAU), "neue Fliesen", GRUEN),
               ("erg2", ("tabler", "cash-banknote", 120, GRUEN), "5.200 €", GRUEN),
               ("regr", ("tabler", "building-factory-2", 110, WEISS), "Regress", WEISS)]),
    *paar([("erg", "froh")], [("erg", "ruhig"), ("regr", "froh")]),
]))

# ===========================================================================================================================
# L Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Aus- und Einbau in der Nacherfüllung prüfen")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Aus- und Einbaukosten in der Nacherfüllung prüfen,", 200, 200, beim("tipp", "Prüfe"), "Bold", 34),
    *neinz("nicht beim Schadensersatz", 270, beim("tipp", "nicht"), "Bold", 34, x=245),
    z("Anspruchsgrundlage:", 200, 370, "tipp1", "Bold", 34),
    z("§ 437 Nr. 1 mit § 439 Abs. 3 BGB", 245, 425, beim("tipp1", "Paragraf"), "ExtraBold", 36),
    *neinz("Verschulden nicht nötig", 495, beim("tipp1", "Verschulden"), "Bold", 34, x=245),
    z("Geltende Fassung prüfen:", 200, 600, "tipp2", "Bold", 34),
    z("Mangel vor dem Einbau offenbar?", 245, 655, beim("tipp2", "Mangel"), "ExtraBold", 36),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# M Klausurschema (progressiv)
# ===========================================================================================================================
REIHEN = [("k1", "I.", "Kaufvertrag", BLAU, 0),
          (beim("k1", "Sachmangel"), "", "Sachmangel bei Gefahrübergang", None, 1),
          ("k2", "II.", "Einbau gemäß Art und Verwendungszweck", GELB, 0),
          (beim("k2", "bevor"), "", "bevor der Mangel offenbar wurde", None, 1),
          ("k3", "III.", "erforderliche Aufwendungen", GRUEN, 0),
          (beim("k3", "Entfernen"), "", "für Entfernen und Einbau", None, 1),
          ("k4", "IV.", "keine berechtigte Verweigerung, § 439 Abs. 4 BGB", LILA, 0)]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Schema: Aus- und Einbaukosten, §§ 437 Nr. 1, 439 Abs. 3 BGB"), 110, 90, "sch", 46)]
y = 205
for c, r, txt, farbe, ebene in REIHEN:
    if ebene == 0:
        els_sch += [karte(110, y, 110, 70, c, fill=farbe, rund=14, schatten=5, rand=4),
                    z(r, 165 - F("ExtraBold", 38).getlength(r) / 2, y + 10, c, "ExtraBold", 38, rechts=1820),
                    z(txt, 255, y + 10, c, "ExtraBold", 38, rechts=1820)]
        y += 100
    else:
        els_sch.append(z(txt, 330, y + 2, c, "Bold", 36, rechts=1820))
        els_sch.append(ok(290, y + 24, c, gr=18))
        y += 90
assert y <= 975, y
folie([("sch", "Schema: Aus- und Einbaukosten, § 439 Abs. 3 BGB"), ("k1", "Schema › I. Kaufvertrag und Sachmangel"),
       ("k2", "Schema › II. Einbau"), ("k3", "Schema › III. Erforderliche Aufwendungen"),
       ("k4", "Schema › IV. Keine berechtigte Verweigerung")], els_sch)

# ===========================================================================================================================
# N Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Wer mangelhafte Ware ", 0), ("bestimmungsgemäß", "a")], [("einbaut, bevor der Mangel ", 0)],
                 [("offenbar", "b"), (" wird,", 0)]], 750, 300, 46, "merke",
                {"a": beim("merke", "bestimmungsgemäß"), "b": beim("merke", "offenbar")}),
    *markertext([[("bekommt Ausbau und Einbau ", 0), ("ersetzt", "c"), (",", 0)],
                 [("auch ", 0), ("ohne Verschulden", "d"), (" des Verkäufers.", 0)]], 750, 600, 44, "mk2",
                {"c": beim("mk2", "ersetzt"), "d": beim("mk2", "ohne")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
