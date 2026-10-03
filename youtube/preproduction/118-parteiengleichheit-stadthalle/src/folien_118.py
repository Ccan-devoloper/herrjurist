"""Folge 118 · Parteiengleichheit: Stadthalle für eine umstrittene Partei? – Serienstandard Open Peeps (Katzenkönig).
Fiktiver Fall (Vorbild sachlich: Stadthalle Wetzlar, BVerfG (K) 1 BvQ 18/18): Die vom Verfassungsschutz beobachtete, nicht
verbotene Weitblick-Partei (fiktiv, neutrales Berg-Symbol, keine Farben realer Parteien) beantragt für ihren Landesverband
mit Sitz in der Stadt die Stadthalle für den Landesparteitag; die Bürgermeisterin lehnt ab, der Rat ändert eine Woche
später die Widmung; Eilantrag. Beispielland NRW (§ 8 Abs. 2, 4 GO NRW), Normtabelle nur mit am Wortlaut geprüften Normen.
Szenen laut ../SZENENPLAN.md: A1 Antrag, A2 Ratsbeschluss/Eilantrag, B Sachverhalt, C Anspruchsgrundlage (Wortlautkarte
§ 8 GO NRW), D Normtabelle und Art. 28 Abs. 2 GG, E § 5 Abs. 1 PartG (Wortlautkarte), F1 Widmung/Vergabepraxis,
F2 Widmungsänderung aus konkretem Anlass, G1 Art. 21 Abs. 4 GG (Wortlautkarte), G2 Beobachtung/Abs. 3, H Grenzen und
Ergebnis, I Durchsetzung § 123 VwGO (Richterin), J1/J2 Wetzlar, K Klausurtipp, L Prüfschema, M Merksatz.
Keine realen Personen als Figuren (Wetzlar nur als Tafel mit Icons). Zwei Handlungsgeräusche (Antrag auf den Tisch,
Hammer der Richterin; ../geraeusche_herkunft.json). Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/
tisch als eigene Kopie aus Folge 115 (gemeinsame Dateien unverändert); neu: stadthalle(), plakat(), fahne(), pult().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from ostil import titel, karte, pille
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_118/"

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
LILAHELL = (246, 243, 255, 255)
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
        if n.startswith(("bild:", "ficon:", "bank")) or "/op_118/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def wortlaut(x, y, w, zeilen, quelle, cue, marken=(), size=32, bis=None):
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 03.10.2026), als Zitat mit Normangabe;
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 103/109/112) --------------------------------
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


def okz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Haken davor (zur gesprochenen Bejahung)."""
    return [ok(x - 45, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]


def neinz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Kreuz davor (zur gesprochenen Verneinung)."""
    return [nein(x - 45, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]



def tisch(cx, unten, cue, w=320, h=240, fill=HOLZ):
    """Kneipentisch in Seitenansicht (Platte, zwei Beine)."""
    s = 2
    im = Image.new("RGBA", ((w + 12) * s, (h + 12) * s))
    dr = ImageDraw.Draw(im)
    o = 6 * s
    dr.rounded_rectangle((o, o, o + w * s, o + 30 * s), 10 * s, fill=fill, outline=INK, width=5 * s)
    for lx in (24, w - 46):
        dr.rectangle((o + lx * s, o + 28 * s, o + (lx + 22) * s, o + h * s), fill=WEISS, outline=INK, width=5 * s)
    im = im.resize((w + 12, h + 12), Image.LANCZOS)
    return El(im, cx - w / 2 - 6, unten - h - 6, cue, "cut", 0.0, None, name="tisch")




# --- eigene Szenenbausteine (programmatisch, Palettenflächen, Tuschekontur) ---------------------------------------------------
def _flaeche(w, h):
    s = 2
    im = Image.new("RGBA", ((w + 12) * s, (h + 12) * s))
    return im, ImageDraw.Draw(im), s


def stadthalle(x, boden_, w, h, cue, name="halle"):
    """Stadthalle in Vorderansicht: Baukörper, Dachband mit Schriftzug, Fensterreihe, Doppeltür (Grundformen)."""
    im, dr, s = _flaeche(w, h)
    o = 6 * s
    dr.rectangle((o, o + 70 * s, o + w * s, o + h * s), fill=WEISS, outline=INK, width=5 * s)
    dr.rounded_rectangle((o - 2 * s, o, o + w * s + 2 * s, o + 76 * s), 10 * s, fill=GELB, outline=INK, width=5 * s)
    f = F("ExtraBold", 44 * s)
    t = "STADTHALLE"
    tw = f.getlength(t)
    dr.text((o + (w * s - tw) / 2, o + 12 * s), t, font=f, fill=INK)
    fw = (w - 80) // 4
    for i in range(4):
        fx = o + (30 + i * (fw + 7)) * s
        dr.rounded_rectangle((fx, o + 105 * s, fx + (fw - 14) * s, o + 175 * s), 6 * s, fill=BLAUHELL, outline=INK,
                             width=4 * s)
    tx = o + (w / 2 - 70) * s
    dr.rectangle((tx, o + (h - 150) * s, tx + 140 * s, o + h * s), fill=HOLZ, outline=INK, width=5 * s)
    dr.line((tx + 70 * s, o + (h - 150) * s, tx + 70 * s, o + h * s), fill=INK, width=4 * s)
    im = im.resize((w + 12, h + 12), Image.LANCZOS)
    return El(im, x - 6, boden_ - h - 6, cue, "cut", 0.0, None, name=name)


def plakat(x, y, zeilen, cue, w=200, fill=HELL):
    """Plakat am Gebäude (kleine Karte mit zwei Zeilen, 26 px)."""
    els = [karte(x, y, w, 88, cue, fill=fill, rund=10, schatten=4, rand=4, anim="cut")]
    for i, t in enumerate(zeilen):
        els.append(z(t, x + 14, y + 8 + i * 36, cue, "Bold" if i == 0 else "Regular", 26, rechts=x + w - 6))
    return els


def fahne(cx, boden_, cue, hoehe=330, bis=None):
    """Fahne der fiktiven Weitblick-Partei: Mast, weißes Tuch mit Berg-Symbol (Tabler mountain), neutral."""
    mast = linienzug([(cx, boden_), (cx, boden_ - hoehe)], cue, breite=8, farbe=INK)
    tuch = karte(cx, boden_ - hoehe, 190, 120, cue, fill=WEISS, rund=8, schatten=4, rand=5, anim="cut")
    sym = ficon("tabler", "mountain", cx + 95, boden_ - hoehe + 108, 96, cue, fuell=HELL, anim="cut")
    els = [mast, tuch, sym]
    for e in els:
        e.anim = "cut"
        e.bis = bis
    return els


def pult(cx, boden_, cue, w=230, h=300):
    """Rednerpult im Ratssaal (vor der Figur, verdeckt die Beine)."""
    im, dr, s = _flaeche(w, h)
    o = 6 * s
    dr.polygon([(o, o), (o + w * s, o), (o + (w - 30) * s, o + h * s), (o + 30 * s, o + h * s)], fill=HOLZ, outline=INK)
    dr.line([(o, o), (o + w * s, o), (o + (w - 30) * s, o + h * s), (o + 30 * s, o + h * s), (o, o)], fill=INK,
            width=6 * s, joint="curve")
    dr.rounded_rectangle((o + 60 * s, o + 50 * s, o + (w - 60) * s, o + 110 * s), 8 * s, fill=WEISS, outline=INK,
                         width=4 * s)
    im = im.resize((w + 12, h + 12), Image.LANCZOS)
    return El(im, cx - w / 2 - 6, boden_ - h - 6, cue, "cut", 0.0, None, name="pult")


BODEN = 860
FH = 480                                    # stehende Figur in den Fallszenen
X1, X2 = 1430, 1730                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"HA": "Hartmut", "BM": "Bürgermeisterin", "RI": "Richterin"}
NFARBE = {"HA": GRUEN, "BM": LILA, "RI": BLAU}


def boden(cue):
    return hart(linienzug([(40, BODEN), (1880, BODEN)], cue, breite=7, farbe=INK))


def requisit(folge, px=PX, bis=None):
    """Wechselndes Requisit über den Figuren: folge = [(cue, (set, icon, breite, fuell), pillentext, pillenfarbe)]."""
    els = []
    for i, (c, ic, txt, pf) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else bis
        if ic:
            s_, n_, br, fu = ic
            els.append(ficon(s_, n_, px, PU, br, c, fuell=fu, bis=b))
        if txt:
            els.append(pl(txt, px, PY, c, fill=pf, size=28, anker="m", bis=b))
    return els


def stehend(k, x, folge, bis=None):
    return [*fig(k, x, FB, FR, folge, bis=bis), bis_(ns(NAME[k], x, FB, folge[0][0], NFARBE[k], d=0.1), bis)]


def paar(c0, a, af, b, bf):
    """Tafelszene: zwei Figuren rechts der Tafel (beide blicken nach links zur Tafel)."""
    return [*stehend(a, X1, af), *stehend(b, X2, bf)]


# ===========================================================================================================================
# A1 Fall: der Antrag
# ===========================================================================================================================
HAX, BMX = 1010, 1660
HALLE_X, HALLE_W, HALLE_H = 80, 560, 380
FAHNE_X = 680
H1_BLATT = beim("h1", "beantragen")
folie([(NULL, "Fall · Der Antrag"), ("b1", "Fall · Die Absage")], [
    boden(NULL),
    hart(stadthalle(HALLE_X, BODEN, HALLE_W, HALLE_H, NULL)),
    pl("Landesparteitag in der Stadthalle", 70, 30, beim("fall", "Landesparteitag"), fill=GELB, size=36),
    hart(tisch(1400, BODEN, NULL, w=240, h=200)),
    pl("Landesverband: Sitz in der Stadt", 70, 112, "sitz", fill=WEISS, size=32),
    ficon("tabler", "map-pin", 640, 165, 56, "sitz", fuell=ROT),
    pl("vom Verfassungsschutz beobachtet", 70, 186, "beob", fill=BLAUHELL, size=32),
    ficon("tabler", "eye", 712, 240, 70, "beob", fuell=WEISS),
    pl("nicht verboten", 70, 260, "nichtverb", fill=GRUEN, size=32),
    *[hart(e) for e in fahne(FAHNE_X, BODEN, NULL, hoehe=390)],
    hart(pl("Weitblick-Partei", FAHNE_X + 95, BODEN + 22, NULL, fill=WEISS, size=28, anker="m")),
    # Hartmut (blickt nach rechts zur Bürgermeisterin) beantragt die Halle, Antrag wandert auf den Tisch
    *fig("HA", HAX, BODEN, FH, [(NULL, "ruhig_r")], bis="h1", erst="cut"),
    *redet("HA_redet_r", HAX, BODEN, FH, "h1", "frei"),
    *fig("HA", HAX, BODEN, FH, [("frei", "ruhig_r"), ("b1", "sorge_r")], erst="cut"),
    hart(ns("Hartmut", HAX, BODEN, NULL, GRUEN)),
    blase("sprech", 880, 230, "h1", 1330, 200, inhalt=["Wir beantragen die Stadthalle für einen",
                                                       "Samstag im März, für 400 Delegierte."], textsize=32,
          figur=("HA_redet_r", HAX, BODEN, FH), bis="frei"),
    szene(bewegt(ficon("tabler", "file-text", 1400, 656, 80, H1_BLATT, fuell=WEISS, anim="cut"), H1_BLATT,
                 (H1_BLATT[0], round(H1_BLATT[1] + 0.8, 3)), -260, 60), "118papier*", 0.8, 0.0),
    pl("Antrag", 1400, 505, (H1_BLATT[0], round(H1_BLATT[1] + 0.8, 3)), fill=WEISS, size=28, anker="m"),
    # Saal, Termin, frühere Parteitage
    pl("800 Plätze · Termin frei", 70, 340, "frei", fill=WEISS, size=32),
    ficon("tabler", "calendar-check", 560, 400, 64, beim("frei", "Termin"), fuell=GRUEN),
    *plakat(100, 730, ["Parteitag", "Partei A"], "vorher", w=180),
    *plakat(445, 730, ["Parteitag", "Partei B"], beim("vorher", "Parteien"), w=180),
    pl("letztes Jahr: 2 andere Parteien", 70, 420, "vorher", fill=HELL, size=32),
    # die Bürgermeisterin (blickt nach links zu Hartmut) lehnt ab
    *fig("BM", BMX, BODEN, FH, [(NULL, "ruhig"), ("vorher", "denkt")], bis="b1", erst="cut"),
    *redet("BM_redet", BMX, BODEN, FH, "b1", "rat"),
    hart(ns("Bürgermeisterin", BMX, BODEN, NULL, LILA)),
    blase("sprech", 820, 300, "b1", 1330, 210, inhalt=["Diese Partei wird vom", "Verfassungsschutz beobachtet.",
                                                       "Unsere Halle bekommt sie nicht."], textsize=34,
          figur=("BM_redet", BMX, BODEN, FH), bis="rat"),
])

# ===========================================================================================================================
# A2 Fall: Ratsbeschluss und Eilantrag
# ===========================================================================================================================
BM2, HA2 = 1060, 1600
folie([("rat", "Fall · Der Ratsbeschluss"), ("eilan", "Fall · Der Eilantrag"), ("frage", "Fall · Die Frage")], [
    boden("rat"),
    ficon("tabler", "building-bank", 300, BODEN, 260, "rat", fuell=WEISS, anim="cut"),
    pl("Rathaus", 300, BODEN + 22, "rat", fill=WEISS, size=28, anker="m"),
    pl("Stadtrat · 1 Woche später", 70, 30, "rat", fill=GELB, size=36),
    karte(70, 110, 900, 190, "ratb", fill=HELLROT, rund=16, schatten=6, rand=4),
    z("Beschluss des Stadtrats:", 100, 125, "ratb", "ExtraBold", 32),
    z("Die Stadthalle steht künftig nicht mehr", 100, 172, "ratb", "Bold", 32, rechts=950),
    z("für Parteiveranstaltungen zur Verfügung.", 100, 218, "ratb", "Bold", 32, rechts=950),
    # Bürgermeisterin am Rednerpult (blickt nach links zum Rathaus)
    *fig("BM", BM2, BODEN, FH, [("rat", "ruhig"), ("ratb", "denkt"), ("frage", "sorge")], erst="cut"),
    pult(BM2, BODEN, "rat", w=280),
    ns("Bürgermeisterin", BM2, BODEN, "rat", LILA, anim="cut"),
    # Hartmut kommt mit dem Eilantrag (blickt nach links)
    bewegt(peep_voll("HA_ruhig", HA2, BODEN, FH, "eilan", anim="cut", bis="frage"), "eilan",
           ("eilan", 1.0), 140, 0),
    peep_voll("HA_denkt", HA2, BODEN, FH, "frage", anim="cut"),
    bewegt(ns("Hartmut", HA2, BODEN, "eilan", GRUEN, anim="cut"), "eilan", ("eilan", 1.0), 140, 0),
    pl("Eilantrag beim Verwaltungsgericht", 1080, 30, beim("eilan", "Verwaltungsgericht"), fill=WEISS, size=32),
    ficon("tabler", "gavel", 1560, 260, 90, beim("eilan", "einstweilige"), fuell=HOLZ),
    pl("einstweilige Anordnung", 1090, 110, beim("eilan", "einstweilige"), fill=HELL, size=28),
    pl("Darf die Stadt Nein sagen?", 70, 340, "frage", fill=PINK, size=36),
    pl("Gleichbehandlung der Parteien", 70, 425, "frage2", fill=WEISS, size=34),
    pl("Vorbild: ein echter Fall aus Wetzlar", 70, 505, "vorbild", fill=HELL, size=32),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_118(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=33, zeilenabstand=1.28)
        els += e; y += 16
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_118("sv", [
    "Die Weitblick-Partei will im März ihren Landesparteitag in der Stadthalle abhalten. Ihr Landesverband hat seinen "
    "Sitz in der Stadt. Der Verfassungsschutz des Landes beobachtet die Partei; verboten ist sie nicht. "
    "Landesgeschäftsführer Hartmut beantragt die Halle für einen Samstag im März, für 400 Delegierte.",
    "Der Saal fasst 800 Menschen, der Termin ist frei. Im letzten Jahr haben zwei andere Parteien hier ihre Parteitage "
    "abgehalten. Die Bürgermeisterin lehnt ab: „Diese Partei wird vom Verfassungsschutz beobachtet. Unsere Halle "
    "bekommt sie nicht.“",
    "Eine Woche nach dem Antrag beschließt der Stadtrat, die Stadthalle stehe künftig nicht mehr für "
    "Parteiveranstaltungen zur Verfügung. Die Partei beantragt beim Verwaltungsgericht eine einstweilige Anordnung. "
    "Die Stadt liegt in Nordrhein-Westfalen.",
], "Muss die Stadt der Partei die Stadthalle überlassen?")

# ===========================================================================================================================
# C Anspruchsgrundlage: § 8 Abs. 2, 4 GO NRW (Wortlautkarte, Beispiel NRW)
# ===========================================================================================================================
PZ = "Zulassungsanspruch"
PA = f"{PZ} › Anspruchsgrundlage"
W8 = ["„(2) Alle Einwohner einer Gemeinde sind im Rahmen des",
      "geltenden Rechts berechtigt, die öffentlichen Einrichtungen",
      "der Gemeinde zu benutzen …",
      "(4) Diese Vorschriften gelten entsprechend für",
      "juristische Personen und für Personenvereinigungen.“"]
w8, w8_y = wortlaut(80, 220, 1100, W8, "§ 8 Abs. 2, 4 GO NRW (Auszug)", "p8", marken=[
    (0, "Einwohner", beim("p8", "Einwohner")), (0, "im Rahmen des", beim("p8", "Rahmen")),
    (1, "öffentlichen Einrichtungen", beim("p8", "öffentlichen")), (4, "Personenvereinigungen", beim("p8iv", "Personenvereinigungen"))],
    size=31)
folie([("anspr", PA), ("p8", f"{PA} › § 8 Abs. 2 GO NRW (Beispiel NRW)"), ("p8iv", f"{PA} › § 8 Abs. 4: Personenvereinigungen"),
       ("oe", f"{PA} › öffentliche Einrichtung"), ("rahmen", f"{PA} › im Rahmen des geltenden Rechts")], rechts_frei([
    *tafel("anspr", "Anspruch auf Zulassung"),
    z("Beispiel Nordrhein-Westfalen: in deinem Land ggf. andere Nummer", 110, 165, "land", "Bold", 28, farbe=TEXT),
    *w8,
    *okz("Landesverband mit Sitz in der Stadt: berechtigt", w8_y + 25, beim("p8iv", "Landesverband"), "Bold", 32, x=160),
    *okz("Stadthalle: öffentliche Einrichtung", w8_y + 90, "oe", "Bold", 32, x=160),
    zit("OVG NRW, Beschl. v. 12.5.2021 – 15 B 605/21, Rn. 10", 160, w8_y + 136, "oe"),
    blk(110, w8_y + 190, 1040, 80, GELB, "rahmen", [("im Rahmen von Widmung und Kapazität", "ExtraBold", 34, INK)]),
    *requisit([("anspr", ("tabler", "file-text", 90, WEISS), "Zulassung?", WEISS),
               ("p8", ("tabler", "book", 100, WEISS), "§ 8 GO NRW", GELB),
               ("p8iv", ("tabler", "map-pin", 90, ROT), "Sitz in der Stadt", WEISS),
               ("oe", ("tabler", "building-community", 110, WEISS), "öffentliche Einrichtung", WEISS),
               ("rahmen", ("tabler", "calendar-check", 100, GELB), "Widmung, Kapazität", GELB)]),
    *stehend("HA", FX, [("anspr", "ruhig"), ("oe", "froh")]),
]))

# ===========================================================================================================================
# D Normtabelle (am Wortlaut geprüfte Länder) und Art. 28 Abs. 2 GG
# ===========================================================================================================================
LAENDER = [("Nordrhein-Westfalen", "§ 8 Abs. 2, 4 GO NRW"), ("Niedersachsen", "§ 30 Abs. 1, 3 NKomVG"),
           ("Sachsen", "§ 10 Abs. 2, 5 SächsGemO"), ("Brandenburg", "§ 12 Abs. 1 BbgKVerf"),
           ("weitere Länder", "eigene Gemeindeordnung, Nummer prüfen")]
els_tab = [*tafel("tabelle", "Andere Länder regeln das ähnlich")]
y = 175
for land, norm in LAENDER:
    els_tab += [z(land, 110, y, "tabelle", "Bold", 32), z(norm, 480, y, "tabelle", size=32)]
    y += 56
els_tab += [zit("Wortlaut geprüft am 3.10.2026; alle Länder: Beschreibung", 110, y + 4, "tabelle")]
folie([("tabelle", f"{PA} › andere Länder"), ("a28", f"{PA} › Selbstverwaltung, Art. 28 Abs. 2 GG")], rechts_frei([
    *els_tab,
    blk(110, y + 70, 1040, 120, LILA, "a28", [("Art. 28 Abs. 2 GG: Die Stadt entscheidet in", "ExtraBold", 32, INK),
                                            ("Selbstverwaltung, ob die Halle Parteien offensteht", "ExtraBold", 32, INK)]),
    z("aber nicht beliebig", 110, y + 215, beim("a28", "beliebig"), "ExtraBold", 36),
    zit("vgl. OVG NRW, Beschl. v. 12.5.2021 – 15 B 605/21, Rn. 12", 110, y + 265, beim("a28", "beliebig")),
    *requisit([("tabelle", ("tabler", "map", 100, WEISS), "Landesrecht", WEISS),
               ("a28", ("tabler", "building-bank", 110, WEISS), "Selbstverwaltung", LILA)]),
    *stehend("BM", FX, [("tabelle", "ruhig"), ("a28", "denkt")]),
]))

# ===========================================================================================================================
# E § 5 Abs. 1 PartG (Wortlautkarte)
# ===========================================================================================================================
W5 = ["„Wenn ein Träger öffentlicher Gewalt den Parteien",
      "Einrichtungen zur Verfügung stellt …, sollen alle",
      "Parteien gleichbehandelt werden.“"]
w5, w5_y = wortlaut(80, 180, 1100, W5, "§ 5 Abs. 1 Satz 1 PartG (Auszug)", "p5", marken=[
    (1, "Einrichtungen zur Verfügung stellt", beim("p5", "Einrichtungen")), (2, "gleichbehandelt", beim("p5", "gleichbehandelt"))],
    size=34)
folie([("p5", f"{PA} › § 5 Abs. 1 PartG"), ("chanc", f"{PA} › Chancengleichheit, Art. 3, 21 GG"),
       ("ohnesitz", f"{PA} › auch ohne Sitz in der Stadt")], rechts_frei([
    *tafel("p5", "§ 5 Abs. 1 PartG: Gleichbehandlung"),
    *w5,
    z("Chancengleichheit der Parteien: Art. 3, 21 GG", 110, w5_y + 35, "chanc", "Bold", 34),
    zit("BVerfG (K), Beschl. v. 26.8.2016 – 2 BvQ 46/16, Rn. 7", 110, w5_y + 85, beim("chanc", "Chancengleichheit")),
    *okz("hilft auch Parteien ohne Sitz in der Stadt", w5_y + 150, "ohnesitz", "Bold", 34, x=160),
    zit("OVG NRW, Beschl. v. 15.2.2024 – 15 B 144/24, Rn. 10;", 160, w5_y + 200, "ohnesitz"),
    zit("VG Minden, Beschl. v. 3.5.2023 – 2 L 353/23, Rn. 8 f.", 160, w5_y + 236, "ohnesitz"),
    *requisit([("p5", ("tabler", "scale", 100, GELB), "Gleichbehandlung", GELB),
               ("chanc", ("tabler", "flag", 90, WEISS), "Chancengleichheit", WEISS),
               ("ohnesitz", ("tabler", "map-pin-off", 90, WEISS), "ohne Sitz", WEISS)]),
    *stehend("HA", FX, [("p5", "ruhig"), ("ohnesitz", "froh")]),
]))

# ===========================================================================================================================
# F1 Erster Prüfpunkt: Widmung und Vergabepraxis
# ===========================================================================================================================
PW = f"{PZ} › Widmung"
folie([("widm", PW), ("praxis", f"{PW}: Vergabepraxis"), ("imzweck", f"{PW}: Landesparteitag im Widmungszweck (+)")],
      rechts_frei([
    *tafel("widm", "Erster Prüfpunkt: die Widmung"),
    z("Widmung kann sich aus der Vergabepraxis ergeben", 110, 180, beim("widm", "Vergabepraxis"), "Bold", 34),
    zit("OVG NRW, Beschl. v. 15.2.2024 – 15 B 144/24, Rn. 13, 18", 110, 228, beim("widm", "Vergabepraxis")),
    *okz("Halle schon 2 Parteien für Parteitage überlassen", 300, "praxis", "Bold", 34, x=160),
    *plakat(160, 370, ["Parteitag", "Partei A"], beim("praxis", "Parteien")),
    *plakat(400, 370, ["Parteitag", "Partei B"], beim("praxis", "Parteien")),
    blk(110, 510, 1040, 80, GRUEN, "imzweck", [("Landesparteitag: im Widmungszweck", "ExtraBold", 36, INK)]),
    *requisit([("widm", ("tabler", "calendar-event", 100, WEISS), "Vergabepraxis", WEISS),
               ("praxis", ("tabler", "building-community", 110, WEISS), "2 Parteitage", HELL),
               ("imzweck", ("tabler", "circle-check", 100, GRUEN), "im Widmungszweck", GRUEN)]),
    *paar("widm", "HA", [("widm", "ruhig"), ("imzweck", "froh")], "BM", [("widm", "ruhig"), ("praxis", "denkt")]),
]))

# ===========================================================================================================================
# F2 Widmungsänderung aus konkretem Anlass
# ===========================================================================================================================
ANL_ER = beim("anlass", "Er")
folie([("ratsb", f"{PZ} › Widmungsänderung?"), ("anlass", f"{PZ} › Widmungsänderung aus konkretem Anlass"),
       ("alt", f"{PZ} › gestellter Antrag: alte Regeln"), ("zukunft", f"{PZ} › künftig: nur für alle Parteien")],
      rechts_frei([
    *tafel("ratsb", "Und der Ratsbeschluss?"),
    pl("Antrag", 110, 180, ANL_ER, fill=WEISS, size=32),
    pfeil(275, 210, 455, 210, ANL_ER, breite=6, kopf=20, farbe=INK),
    pl("1 Woche später: Ratsbeschluss", 470, 180, ANL_ER, fill=HELLROT, size=32),
    *neinz("Widmung ändern, nur um diesen Antrag abzulehnen:", 280, beim("anlass", "Widmung"), "Bold", 32, x=160),
    z("verstößt gegen die Gleichbehandlung der Parteien", 160, 325, beim("anlass", "verstößt"), "Bold", 32),
    zit("VG Minden, Beschl. v. 3.5.2023 – 2 L 353/23, Rn. 42, 44, 51;", 160, 375, beim("anlass", "verstößt")),
    zit("Nds. OVG, Beschl. v. 8.6.2022 – 10 ME 75/22, Leitsatz 1", 160, 410, beim("anlass", "verstößt")),
    blk(110, 470, 1040, 80, GELB, "alt", [("Gestellter Antrag: nach den alten Regeln", "ExtraBold", 36, INK)]),
    *okz("künftig für alle Parteien schließen: zulässig", 590, "zukunft", "Bold", 32, x=160),
    *neinz("gezielt nur für eine Partei: unzulässig", 650, beim("zukunft", "gezielt"), "Bold", 32, x=160),
    zit("vgl. VG Minden, 2 L 353/23, Rn. 44, 50", 160, 700, beim("zukunft", "gezielt")),
    *requisit([("ratsb", ("tabler", "building-bank", 110, WEISS), "Ratsbeschluss", HELLROT),
               ("anlass", ("tabler", "calendar-event", 100, WEISS), "nach dem Antrag", HELLROT),
               ("alt", ("tabler", "file-text", 90, WEISS), "alte Regeln", GELB),
               ("zukunft", ("tabler", "lock", 90, WEISS), "nur für alle", WEISS)]),
    *paar("ratsb", "HA", [("ratsb", "denkt"), ("alt", "froh")], "BM", [("ratsb", "ruhig"), ("anlass", "sorge")]),
]))

# ===========================================================================================================================
# G1 Zweiter Prüfpunkt: Parteienprivileg, Art. 21 Abs. 4 GG (Wortlautkarte)
# ===========================================================================================================================
PV = f"{PZ} › Verfassungsschutz"
W21 = ["„Über die Frage der Verfassungswidrigkeit nach Absatz 2",
       "… entscheidet das Bundesverfassungsgericht.“"]
w21, w21_y = wortlaut(80, 180, 1100, W21, "Art. 21 Abs. 4 GG (Auszug)", "p21", marken=[
    (0, "Verfassungswidrigkeit", beim("p21", "Verfassungswidrigkeit")),
    (1, "Bundesverfassungsgericht", beim("p21", "Bundesverfassungsgericht"))], size=34)
folie([("privi", PV), ("p21", f"{PV} › Art. 21 Abs. 4 GG"), ("bisdahin", f"{PV} › Parteienprivileg")], rechts_frei([
    *tafel("privi", "Zweiter Prüfpunkt: der Verfassungsschutz"),
    *w21,
    z("Bis dahin: keine Benachteiligung wegen der Ziele", 110, w21_y + 40, "bisdahin", "Bold", 34),
    zit("BVerfG, Beschl. v. 29.10.1975 – 2 BvE 1/75 (BVerfGE 40, 287), Rn. 16", 110, w21_y + 88, "bisdahin"),
    *okz("politisch bekämpfen: erlaubt", w21_y + 150, beim("bekaempf", "politisch"), "Bold", 34, x=160),
    *neinz("behindern: nicht erlaubt", w21_y + 215, beim("bekaempf", "behindert"), "Bold", 34, x=160),
    zit("BVerfG, Urt. v. 17.1.2017 – 2 BvB 1/13, Rn. 526", 160, w21_y + 265, beim("bekaempf", "behindert")),
    *requisit([("privi", ("tabler", "eye", 100, WEISS), "Verfassungsschutz", BLAUHELL),
               ("p21", ("tabler", "gavel", 100, HOLZ), "nur das BVerfG", GELB),
               ("bisdahin", ("tabler", "scale", 100, WEISS), "Parteienprivileg", WEISS)]),
    *paar("privi", "HA", [("privi", "ruhig")], "BM", [("privi", "denkt"), ("bisdahin", "sorge")]),
]))

# ===========================================================================================================================
# G2 Beobachtung, keine rechtlichen Nachteile, Abgrenzung Art. 21 Abs. 3 GG
# ===========================================================================================================================
folie([("vs", f"{PV} › Beobachtung"), ("keinnach", f"{PV} › keine rechtlichen Nachteile"),
       ("abs3", f"{PV} › Abgrenzung: Art. 21 Abs. 3 GG")], rechts_frei([
    *tafel("vs", "Und die Beobachtung?"),
    z("Beobachtung: Einschätzung der Behörde,", 110, 180, "vs", "Bold", 34),
    z("kein Urteil über die Verfassungswidrigkeit", 110, 228, beim("vs", "kein"), "Bold", 34),
    *neinz("rechtliche Nachteile daran knüpfen: unzulässig", 310, "keinnach", "Bold", 34, x=160),
    zit("BVerfGE 40, 287, Rn. 16, 19 (2 BvE 1/75);", 160, 360, "keinnach"),
    zit("vgl. OVG NRW, Urt. v. 13.5.2024 – 5 A 1218/22, Rn. 111, 113", 160, 396, "keinnach"),
    blk(110, 470, 1040, 120, LILA, "abs3", [("Art. 21 Abs. 3 GG: Ausschluss von der staatlichen", "ExtraBold", 32, INK),
                                          ("Finanzierung, entscheidet ebenfalls das BVerfG", "ExtraBold", 32, INK)]),
    zit("Art. 21 Abs. 4 GG", 110, 605, "abs3"),
    *requisit([("vs", ("tabler", "eye", 100, WEISS), "Einschätzung", BLAUHELL),
               ("keinnach", ("tabler", "x", 90, WEISS), "keine Nachteile", HELLROT),
               ("abs3", ("tabler", "coins", 100, GELB), "Finanzierung", LILA)]),
    *paar("vs", "HA", [("vs", "ruhig"), ("keinnach", "froh")], "BM", [("vs", "denkt")]),
]))

# ===========================================================================================================================
# H Grenzen und Ergebnis
# ===========================================================================================================================
PG = f"{PZ} › Grenzen"
folie([("grenz", PG), ("kap", f"{PG} › Kapazität"), ("aufl", f"{PG} › sachliche Bedingungen, § 5 Abs. 3 PartG"),
       ("gefahr", f"{PG} › Gegendemonstrationen"), ("hier", f"{PG} › im Fall: keine"),
       ("erg", "Ergebnis · Anspruch auf Zulassung (+)")], rechts_frei([
    *tafel("grenz", "Grenzen des Anspruchs"),
    z("Termin vergeben: meist zählt, wer zuerst angefragt hat", 110, 180, "kap", "Bold", 32),
    zit("OVG NRW, Beschl. v. 15.2.2024 – 15 B 144/24, Rn. 24", 110, 225, "kap"),
    z("Sachliche Bedingungen wie ein Sicherheitskonzept:", 110, 285, "aufl", "Bold", 32),
    z("erlaubt, wenn sie für alle Parteien gelten", 110, 330, beim("aufl", "erlaubt"), size=32),
    zit("§ 5 Abs. 3 PartG", 110, 375, beim("aufl", "erlaubt")),
    z("Gegendemonstrationen: Gefahrenabwehr ist Sache der Polizei", 110, 435, "gefahr", "Bold", 32),
    z("Ablehnung erst im polizeilichen Notstand", 110, 480, beim("gefahr", "ablehnen"), size=32),
    zit("OVG NRW, 15 B 144/24, Rn. 21", 110, 525, beim("gefahr", "ablehnen")),
    *okz("Hier: Termin frei, keine konkreten Gefahren", 590, "hier", "Bold", 34, x=160),
    blk(110, 670, 1040, 120, GRUEN, "erg", [("Ergebnis: Die Weitblick-Partei hat einen", "ExtraBold", 36, INK),
                                           ("Anspruch auf Zulassung zur Stadthalle", "ExtraBold", 36, INK)]),
    *requisit([("grenz", ("tabler", "alert-triangle", 100, GELB), "Grenzen", WEISS),
               ("kap", ("tabler", "calendar-event", 100, WEISS), "wer zuerst fragt", WEISS),
               ("aufl", ("tabler", "shield-check", 100, WEISS), "Sicherheitskonzept", WEISS),
               ("gefahr", ("fluent-emoji-flat", "police-car", 140, None), "Polizei", BLAUHELL),
               ("hier", ("tabler", "calendar-check", 100, GRUEN), "Termin frei", WEISS),
               ("erg", ("tabler", "circle-check", 100, GRUEN), "Anspruch (+)", GRUEN)]),
    *paar("grenz", "HA", [("grenz", "ruhig"), ("erg", "froh")], "BM", [("grenz", "ruhig"), ("gefahr", "denkt"),
                                                                     ("erg", "sorge")]),
]))

# ===========================================================================================================================
# I Durchsetzung: § 123 VwGO, Beschluss des Verwaltungsgerichts (Richterin spricht)
# ===========================================================================================================================
PD = "Durchsetzung"
HAMMER = beim("r1", "Stadt")
folie([("eil", f"{PD} › Eilantrag, § 123 VwGO"), ("ao", f"{PD} › Anordnungsanspruch"), ("ag", f"{PD} › Anordnungsgrund"),
       ("r1", f"{PD} › Beschluss: Stadt verpflichtet")], rechts_frei([
    *tafel("eil", "Durchsetzung: § 123 VwGO"),
    z("Ein Urteil käme zu spät: Eilantrag, § 123 Abs. 1 VwGO", 110, 180, beim("eil", "Eilantrag"), "Bold", 32),
    *okz("Anordnungsanspruch: der Zulassungsanspruch", 260, "ao", "Bold", 34, x=160),
    *okz("Anordnungsgrund: der nahe Termin", 330, "ag", "Bold", 34, x=160),
    z("hier ausnahmsweise:", 160, 385, beim("ag", "ausnahmsweise"), size=34),
    z("Vorwegnahme der Hauptsache", 160, 432, beim("ag", "Vorwegnahme"), "Bold", 34),
    zit("vgl. OVG NRW, Beschl. v. 15.2.2024 – 15 B 144/24, Rn. 29, 32", 160, 485, beim("ag", "Vorwegnahme")),
    blk(110, 570, 1040, 120, GRUEN, "r1", [("Beschluss: Die Stadt muss der Partei", "ExtraBold", 36, INK),
                                          ("die Stadthalle überlassen", "ExtraBold", 36, INK)]),
    *requisit([("eil", ("tabler", "file-text", 90, WEISS), "Eilantrag", WEISS),
               ("ao", ("tabler", "building-community", 110, WEISS), "Zulassung", WEISS),
               ("ag", ("tabler", "calendar-event", 100, HELLROT), "naher Termin", HELLROT)], bis="r1"),
    *stehend("HA", X1, [("eil", "ruhig"), ("r1", "froh")]),
    # die Richterin (blickt nach links) verkündet den Beschluss; Hammer auf dem Pult
    *fig("RI", X2, FB, FR, [("eil", "ruhig")], bis="r1"),
    *redet("RI_redet", X2, FB, FR, "r1", "wetz"),
    pult(X2, FB, "eil", w=230, h=220),
    ns("Richterin", X2, FB, "eil", BLAU, d=0.1),
    szene(bewegt(ficon("tabler", "gavel", X2 + 55, FB - 226, 80, ("r1", 0.0), fuell=HOLZ, anim="cut"), ("r1", 0.0),
                 (HAMMER[0], round(HAMMER[1] + 0.1, 3)), 0, -40), "118hammer*", 0.8, round(HAMMER[1] + 0.1 - 0.044, 3)),
    blase("sprech", 640, 230, "r1", 1560, 200, inhalt=["Die Stadt wird verpflichtet, der",
                                                     "Partei die Stadthalle zu überlassen."], textsize=31,
          figur=("RI_redet", X2, FB, FR), bis="wetz"),
]))

# ===========================================================================================================================
# J1 Vorbild Wetzlar: Ablauf
# ===========================================================================================================================
PWZ = "Vorbild · Stadthalle Wetzlar 2018"
folie([("wetz", PWZ), ("wetz2", f"{PWZ} › Verwaltungsgericht"), ("verw", f"{PWZ} › Stadt verweigert"),
       ("zwang", f"{PWZ} › Zwangsgeld"), ("karls", f"{PWZ} › BVerfG, 1 BvQ 18/18"), ("nicht", f"{PWZ} › Stadt folgt nicht")],
      rechts_frei([
    *tafel("wetz", "Vorbild: Stadthalle Wetzlar, 2018"),
    z("Und wenn die Stadt nicht folgt?", 110, 170, "wetz", "Bold", 32, farbe=TEXT),
    z("20.12.2017 · VG Gießen: Stadt muss die Halle für eine", 110, 230, "wetz2", "Bold", 32),
    z("Wahlkampfveranstaltung überlassen (Eilverfahren)", 110, 275, beim("wetz2", "Wahlkampfveranstaltung"), size=32),
    z("VGH: Beschwerde der Stadt zurückgewiesen", 110, 335, "vgh", size=32),
    z("Stadt verweigert: Nachweise zu Versicherung und", 110, 395, "verw", "Bold", 32),
    z("Sanitätsdienst fehlten", 110, 440, beim("verw", "Sanitätsdienst"), "Bold", 32),
    z("23.3.2018 · Zwangsgeld festgesetzt", 110, 500, "zwang", size=32),
    z("24.3.2018 · BVerfG: der Entscheidung Folge leisten", 110, 560, "karls", "Bold", 32),
    *neinz("Die Stadt folgt auch dem nicht.", 625, "nicht", "ExtraBold", 34, x=160),
    zit("BVerfG (K), Beschl. v. 24.3.2018 – 1 BvQ 18/18, Rn. 1 f., Tenor;", 110, 690, "karls"),
    zit("BVerfG, Pressemitteilung Nr. 16/2018 v. 26.3.2018", 110, 725, "nicht"),
    *requisit([("wetz", ("tabler", "building-community", 120, WEISS), "Stadthalle", WEISS),
               ("wetz2", ("tabler", "gavel", 100, HOLZ), "Eilverfahren", WEISS),
               ("verw", ("tabler", "lock", 100, WEISS), "Zugang verweigert", HELLROT),
               ("zwang", ("tabler", "coins", 100, GELB), "Zwangsgeld", GELB),
               ("karls", ("tabler", "building-bank", 120, WEISS), "Karlsruhe", WEISS),
               ("nicht", ("tabler", "x", 100, WEISS), "nicht befolgt", HELLROT)]),
]))

# ===========================================================================================================================
# J2 Was Karlsruhe festhielt; Art. 20 Abs. 3 GG
# ===========================================================================================================================
folie([("gruende", "Vorbild · Was Karlsruhe festhielt"),
       ("verl", "Vorbild › Art. 8 Abs. 1 i. V. m. Art. 20 Abs. 3, 19 Abs. 4 GG"),
       ("fehl", "Vorbild › Pressemitteilung Nr. 26/2018"),
       ("a203", "Bindung an Gerichtsentscheidungen, Art. 20 Abs. 3 GG")], rechts_frei([
    *tafel("gruende", "Was Karlsruhe festhielt"),
    z("Gründe vor Gericht nicht rechtzeitig vorgebracht", 110, 180, beim("gruende", "Ihre"), "Bold", 32),
    z("oder von den Gerichten als unerheblich beurteilt", 110, 225, beim("gruende", "unerheblich"), "Bold", 32),
    z("voraussichtlich verletzt: Art. 8 Abs. 1 i. V. m.", 110, 290, "verl", size=32),
    z("Art. 20 Abs. 3, 19 Abs. 4 GG", 110, 335, beim("verl", "Bindung"), "Bold", 32),
    zit("BVerfG (K), Beschl. v. 24.3.2018 – 1 BvQ 18/18, Rn. 5", 110, 380, "verl"),
    karte(110, 430, 1040, 150, "fehl", fill=ZITAT, rund=16, schatten=5, rand=4),
    z("„… Fehlvorstellungen über die Bindungskraft", 140, 445, "fehl", size=32, rechts=1140),
    z("richterlicher Entscheidungen …“", 140, 490, "fehl", size=32, rechts=1140),
    zit("BVerfG, Pressemitteilung Nr. 26/2018 v. 20.4.2018", 140, 535, "fehl", rechts=1140),
    blk(110, 620, 1040, 120, GELB, "a203", [("Art. 20 Abs. 3 GG: an Gesetz und Recht gebunden;", "ExtraBold", 32, INK),
                                           ("vollziehbare Gerichtsentscheidung befolgen", "ExtraBold", 32, INK)]),
    *requisit([("gruende", ("tabler", "building-bank", 120, WEISS), "Karlsruhe", WEISS),
               ("verl", ("tabler", "scale", 100, WEISS), "Art. 8, 20, 19 GG", WEISS),
               ("fehl", ("tabler", "file-text", 90, WEISS), "Pressemitteilung", ZITAT),
               ("a203", ("tabler", "gavel", 100, HOLZ), "Entscheidung befolgen", GELB)]),
]))

# ===========================================================================================================================
# K Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Gemeindeordnung, dann § 5 PartG"), ("tipp2", "Klausurtipp · Daten im Sachverhalt"),
       ("tipp3", "Klausurtipp · Verfassungswidrigkeit nicht prüfen")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Erst die Gemeindeordnung,", 200, 200, beim("tipp", "Gemeindeordnung"), "Bold", 36),
    z("dann § 5 Abs. 1 PartG", 200, 250, beim("tipp", "Paragraf"), "Bold", 36),
    z("Achte auf die Daten: Ratsbeschluss nach dem Antrag?", 200, 330, "tipp2", size=33),
    z("Dann spricht das für eine Widmungsänderung", 200, 378, beim("tipp2", "spricht"), size=33),
    z("aus konkretem Anlass.", 200, 426, beim("tipp2", "konkretem"), "Bold", 33),
    linienzug([(130, 495), (1130, 495)], "tipp3", breite=3),
    z("Ob die Partei verfassungswidrig ist,", 200, 525, "tipp3", "Bold", 34),
    z("prüfst du nicht: Das entscheidet allein", 200, 573, beim("tipp3", "prüfst"), size=34),
    z("das BVerfG, Art. 21 Abs. 4 GG.", 200, 621, beim("tipp3", "Karlsruhe"), size=34),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# L Prüfschema
# ===========================================================================================================================
REIHEN = [("s1", 0, "I. Anspruchsgrundlage", True),
          ("s1", 1, "Gemeindeordnung (z. B. § 8 Abs. 2, 4 GO NRW) und § 5 Abs. 1 PartG", False),
          ("s2", 0, "II. Öffentliche Einrichtung und Berechtigter", True),
          ("s3", 0, "III. Widmung", True),
          ("s3", 1, "Vergabepraxis; Widmungsänderung aus konkretem Anlass?", False),
          ("s4", 0, "IV. Kein sachlicher Grund dagegen", True),
          ("s4", 1, "Kapazität, sachliche Bedingungen, konkrete Gefahr", False),
          (beim("s4", "Ziele"), 1, "Ziele der Partei zählen nicht (Art. 21 Abs. 4 GG)", False),
          ("s5", 0, "V. Durchsetzung: Eilantrag, § 123 VwGO", True)]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfschema: Anspruch auf Zulassung zur Stadthalle"), 110, 90, "sch", 46)]
y = 200
for c, ebene, text, fett in REIHEN:
    x = (130, 200)[ebene]
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 38 if ebene == 0 else 34, rechts=1800))
    y += {0: 78, 1: 72}[ebene]
assert y <= 970, y
folie([("sch", "Prüfschema"), ("s1", "Prüfschema › I. Anspruchsgrundlage"), ("s2", "Prüfschema › II. Einrichtung, Berechtigter"),
       ("s3", "Prüfschema › III. Widmung"), ("s4", "Prüfschema › IV. kein sachlicher Grund"),
       ("s5", "Prüfschema › V. Durchsetzung")], els_sch)

# ===========================================================================================================================
# M Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Bis das BVerfG eine Partei verbietet,", 0)], [("darf die Stadt sie ", 0), ("nicht", "a"),
                 (" wegen", 0)], [("ihrer Ziele benachteiligen.", 0)]], 750, 270, 42, "merke", {"a": beim("merke", "nicht")}),
    *markertext([[("Wer die Halle anderen Parteien", 0)], [("überlässt, muss sie ", 0), ("auch ihr", "b"),
                 (" überlassen.", 0)]], 750, 520, 42, "m2", {"b": beim("m2", "auch")}),
    *markertext([[("Und eine Gerichtsentscheidung", 0)], [("wird ", 0), ("befolgt", "c"), (".", 0)]], 750, 710, 42, "m3",
                {"c": beim("m3", "befolgt")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
