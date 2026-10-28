"""Folge 246 · Widerspruchsbescheid schreiben: Tenor, Gründe, Kosten, Belehrung – Serienstandard Open Peeps (Katzenkönig).
Fiktiver Fall (Land und Behörden fiktiv): Herr Holzapfel und sein verspielter Mischling; trotz Leinenanordnung dreimal frei
im Ort, die Gemeinde untersagt die Hundehaltung. Widerspruch, keine Abhilfe (Herr Sperling), Vorlage an das Landratsamt;
Referendarin Körner entwirft den Widerspruchsbescheid. Danach aus Sicht des zweiten Examens: 1. Vorverfahren (Wortlautkarte
§ 68 Abs. 1 VwGO, Länder-Overlay nur amtlich geprüft: NRW, Niedersachsen), 2. Abhilfe § 72 und Zuständigkeit § 73 Abs. 1
(Wortlautkarten), 3. Bescheid: Kopf und Tenor, Gründe (Sachverhalt, Zulässigkeit, Begründetheit mit Zweckmäßigkeit),
Kosten (§ 73 Abs. 3 Satz 3 VwGO, Wortlautkarte § 80 Abs. 1 Satz 3 VwVfG), Rechtsbehelfsbelehrung (Muster), Zustellung
(Wortlautkarte § 73 Abs. 3 VwGO), 4. typische Fehler, Klausurtipp, Schema, Merksatz mit Lexi.
Szenen laut ../SZENENPLAN.md. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/feld/requisit/paar/
hand als eigene Kopie aus Folge 234 (gemeinsame Dateien unverändert); neu: haus(), zaun(), amt(), tisch().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut nach gesetze-im-internet.de bzw. recht.nrw.de, Abruf 07.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_246/"

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
HELLGRAU = (226, 226, 222, 255)
TUERKIS_ = (127, 214, 208, 255)
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
        if n.startswith(("bild:", "ficon:")) or "/op_246/" in n:
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


def wortlaut(x, y, w, text, quelle, cue, marken=(), size=32, bis=None):
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 07.10.2026 (Folge 246)), als Zitat mit Normangabe; der
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 160/203) -------------------------------------
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


def neinz(text, y, cue, stil="Regular", size=34, x=185, gr=20, kreuz=None, **k):
    """Tafelzeile mit Bleistift-Kreuz davor; kreuz = Cue der gesprochenen Verneinung (sonst mit der Zeile)."""
    return [bis_(nein(x - 45, y + 20, kreuz or cue, gr=gr), k.get("bis")), z(text, x, y, cue, stil, size, **k)]


# --- eigene Szenenbausteine (programmatisch, Palettenflächen, Tuschekontur) ---------------------------------------------------
BODEN = 860
FH = 440                                    # stehende Figur in der Fallszene
X1, X2 = 1400, 1720                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"HO": "Herr Holzapfel", "SP": "Herr Sperling", "KO": "Frau Körner"}
NFARBE = {"HO": GRUEN, "SP": BLAU, "KO": LILAHELL}
WAND = (246, 236, 220, 255)


def _flaeche(w, h):
    s = 2
    im = Image.new("RGBA", ((w + 12) * s, (h + 12) * s))
    return im, ImageDraw.Draw(im), s


def boden(cue):
    return hart(linienzug([(40, BODEN), (1880, BODEN)], cue, breite=7, farbe=INK))

def _feld(w, h, fill=WEISS, rand=4, rund=14):
    im, dr, s = _flaeche(w, h)
    o = 6 * s
    dr.rounded_rectangle((o, o, o + w * s, o + h * s), rund * s, fill=fill, outline=INK, width=rand * s)
    return im.resize((w + 12, h + 12), Image.LANCZOS)


def feld(x, y, w, h, cue, fill=WEISS, rand=4, rund=14, bis=None, anim="cut", name="feld"):
    return El(_feld(w, h, fill, rand, rund), x, y, cue, anim, 0.0, bis, name=name)


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


def paar(a, af, b, bf):
    """Tafelszene: zwei Figuren rechts der Tafel (beide blicken nach links zur Tafel)."""
    return [*stehend(a, X1, af), *stehend(b, X2, bf)]



# --- Folge 246: Größen, Szenenbausteine ------------------------------------------------------------------------------
GROESSE = {"HO": 0.96, "SP": 1.0, "KO": 0.95}


def hh(k, h):
    return round(h * GROESSE.get(k, 1.0))


def stehend(k, x, folge, bis=None):
    els = [*fig(k, x, FB, hh(k, FR), folge, bis=bis), bis_(ns(NAME[k], x, FB, folge[0][0], NFARBE[k], d=0.1), bis)]
    return rechts_frei(els, 1200)


def hand(name, cx, unten, hoehe, b0=0.35, b1=0.60, links=True):
    """Äußerster deckender Punkt einer Figur im Höhenband b0–b1 (ausgestreckte bzw. erhobene Hand)."""
    e = peep_voll(name, cx, unten, hoehe, "_")
    a = np.asarray(e.sprite)[:, :, 3] > 40
    h_ = a.shape[0]
    band = a[int(h_ * b0):int(h_ * b1)]
    ys, xs = np.nonzero(band)
    i = xs.argmin() if links else xs.argmax()
    return e.x + xs[i], e.y + int(h_ * b0) + ys[i]


# --- Folge 246: eigene Szenenbausteine ---------------------------------------------------------------------------------
FASSADE = (238, 226, 206, 255)
DACH = ROT
HUND = HOLZ


def haus(cue, x0=80, x1=600, oben=420):
    """Einfamilienhaus (programmatisch): Wand mit Tür und zwei Fenstern, rotes Satteldach, Tuschekontur."""
    w, h = x1 - x0, BODEN - oben
    dachh = 190
    s = 2
    im = Image.new("RGBA", ((w + 60) * s, (h + dachh + 12) * s))
    dr = ImageDraw.Draw(im)
    o = 30 * s
    top = dachh * s
    dr.rectangle((o, top, o + w * s, top + h * s), fill=INK)
    dr.rectangle((o + 5 * s, top, o + (w - 5) * s, top + h * s), fill=FASSADE)
    dr.polygon([(o - 26 * s, top + 4 * s), (o + w * s / 2, 6 * s), (o + (w + 26) * s, top + 4 * s)], fill=INK)
    dr.polygon([(o - 14 * s, top - 3 * s), (o + w * s / 2, 18 * s), (o + (w + 14) * s, top - 3 * s)], fill=DACH)
    for fx in (50, w - 160):
        dr.rounded_rectangle((o + fx * s, top + 70 * s, o + (fx + 110) * s, top + 180 * s), 6 * s, fill=INK)
        dr.rounded_rectangle((o + (fx + 5) * s, top + 75 * s, o + (fx + 105) * s, top + 175 * s), 4 * s, fill=BLAUHELL)
        dr.rectangle((o + (fx + 53) * s, top + 75 * s, o + (fx + 57) * s, top + 175 * s), fill=INK)
    tx = w / 2 - 50
    dr.rounded_rectangle((o + tx * s, top + (h - 190) * s, o + (tx + 100) * s, top + (h + 4) * s), 8 * s, fill=INK)
    dr.rounded_rectangle((o + (tx + 6) * s, top + (h - 184) * s, o + (tx + 94) * s, top + (h + 4) * s), 5 * s, fill=HOLZ)
    dr.ellipse((o + (tx + 74) * s, top + (h - 96) * s, o + (tx + 84) * s, top + (h - 86) * s), fill=INK)
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    return El(im, x0 - 30, oben - dachh, cue, "cut", 0.0, None, name="haus")


def zaun(x0, x1, cue, breite=96, bis=None, name="zaun"):
    """Gartenzaun aus Tabler-Zaunfeldern (MIT), Füllung Weiß."""
    n = max(1, int((x1 - x0) // breite))
    return [ficon("tabler", "fence", x0 + breite / 2 + i * breite, BODEN + 4, breite, cue, fuell=WEISS, anim="cut", bis=bis)
            for i in range(n)]


def amt(text, cue, cx=380, breite=420, icon=("tabler", "building")):
    """Behördengebäude als Icon mit Schild."""
    return [ficon(icon[0], icon[1], cx, BODEN, breite, cue, fuell=WEISS, anim="cut"),
            pl(text, cx, BODEN - breite - 70, cue, fill=GELB, size=34, anker="m", anim="cut")]


def tisch(cx, cue, breite=440, hoehe=150, oben=720):
    """Schreibtisch (programmatisch): Holzfront mit Tuschekontur; steht vor den Beinen der Figur."""
    return feld(cx - breite // 2, oben, breite, hoehe, cue, fill=HOLZ, rand=5, rund=10, name="tisch")


def hund(cx, cue, breite=190, bis=None, spiegeln=False, anim="cut"):
    """Der verspielte Mischling (Fluent Emoji High Contrast „dog“, MIT), Füllung Holzbraun – kein Kampfhund-Klischee."""
    return ficon("fluent-emoji-high-contrast", "dog", cx, BODEN, breite, cue, fuell=HUND, spiegeln=spiegeln, bis=bis, anim=anim)


def reihe(punkte, x, y, abstand=24, size=30, fill=GELB):
    """Pillen nebeneinander, jede zu ihrem gesprochenen Wort; Abstand aus der tatsächlichen Pillenbreite."""
    els = []
    for text, cue in punkte:
        e = pl(text, x, y, cue, fill=fill, size=size)
        els.append(e); x = e.x + e.sprite.width + abstand
    assert x <= 1170, "Pillenreihe zu breit"
    return els


# ===========================================================================================================================
# A1 Fall: Haus mit Garten – Leinenanordnung, dreimal frei, Untersagung, Widerspruch
# ===========================================================================================================================
HOX, HUX = 1400, 1640
PLX = 640
HO_H = hh("HO", 440)
FREI = beim("frei", "läuft"), beim("frei", "Ort", ende=True)
hund_frei = bewegt(hund(1760, FREI[0], spiegeln=True, bis="bescheid"), FREI[0], FREI[1], -120)
kasten = ficon("fluent-emoji-high-contrast", "closed-mailbox-with-raised-flag", 170, BODEN, 120, beim("bescheid", "untersagt"),
               fuell=WEISS, bis="ho1")
szene(kasten, "246briefkasten*", 0.8, -0.2)                  # Klappe, wenn der Bescheid im Briefkasten liegt
folie([(NULL, "Fall · Ein Haus mit Garten am Ortsrand"), ("holz", "Fall · Herr Holzapfel und sein Hund"),
       ("leine", "Fall · Die Leinenanordnung"), ("frei", "Fall · Dreimal frei im Ort"),
       ("bescheid", "Fall · Die Gemeinde untersagt die Hundehaltung"), ("ho1", "Fall · Der Widerspruch")], [
    hart(boden(NULL)),
    hart(haus(NULL)),
    *zaun(620, 1000, NULL, bis=beim("ho1", "Zaun")),
    *zaun(620, 1010, beim("ho1", "Zaun"), breite=130, name="zaun_hoch"),
    hart(ficon("fluent-emoji-high-contrast", "deciduous-tree", 1150, BODEN, 190, NULL, fuell=GRUEN, anim="cut")),
    hart(ficon("tabler", "sun", 1830, 150, 96, NULL, fuell=GELB, anim="cut")),
    hart(pl("Ein Haus mit Garten am Ortsrand", PLX, 30, NULL, fill=GELB, size=32)),
    *fig("HO", HOX, BODEN, HO_H, [(NULL, "ruhig_r"), ("holz", "froh_r"), ("frei", "sorge_r"), ("bescheid", "muede_r")],
         bis="ho1", erst="cut"),
    *redet("HO_redet_r", HOX, BODEN, HO_H, "ho1", "wid"),
    ns(NAME["HO"], HOX, BODEN, NULL, NFARBE["HO"], anim="cut"),
    hund(HUX, NULL, bis=FREI[0]),
    hund_frei,
    hund(HUX, "bescheid", bis="wid"),
    pl("Herr Holzapfel und sein verspielter Mischling", PLX, 94, beim("holz", "Herr"), fill=WEISS, size=30, bis="leine"),
    pl("Anordnung der Gemeinde: draußen an die Leine", PLX, 94, beim("leine", "Gemeinde"), fill=BLAUHELL, size=30, bis="frei"),
    ficon("tabler", "file-text", 1110, 600, 90, beim("leine", "Gemeinde"), fuell=BLAUHELL, bis="frei"),
    pl("3 × frei durch den Ort", PLX, 94, beim("frei", "dreimal"), fill=HELLROT, size=30, bis=beim("bescheid", "untersagt")),
    ficon("fluent-emoji-high-contrast", "paw-prints", 1255, BODEN - 8, 100, beim("frei", "läuft"), bis="bescheid"),
    pl("einmal eine Joggerin angesprungen: sie stürzt", PLX, 158, beim("frei", "Einmal"), fill=HELLROT, size=30, bis=beim("bescheid", "untersagt")),
    pl("Bescheid der Gemeinde: Hundehaltung untersagt", PLX, 94, beim("bescheid", "untersagt"), fill=HELLROT, size=30, bis="ho1"),
    ficon("tabler", "file-text", 170, 700, 80, beim("bescheid", "untersagt"), fuell=WEISS, bis="ho1"),
    kasten,
    blase("sprech", 600, 230, "ho1", 980, 360, inhalt=["Er ist doch ganz lieb! Und den", "Zaun habe ich erhöht.",
                                                     "Ich lege Widerspruch ein."], textsize=31,
          figur=("HO_redet_r", HOX, BODEN, HO_H), bis="wid"),
    pl("Widerspruch", PLX, 94, beim("ho1", "Widerspruch"), fill=GELB, size=32, bis="wid"),
])

# ===========================================================================================================================
# A2 Gemeinde: Widerspruch liegt vor, keine Abhilfe, Vorlage an das Landratsamt
# ===========================================================================================================================
SPX = 1350
folie([("wid", "Fall · Der Widerspruch liegt bei der Gemeinde"), ("sperl", "Fall · Abhilfe?"),
       ("sp1", "Fall · Keine Abhilfe, Vorlage an das Landratsamt")], [
    hart(boden("wid")),
    *amt("Gemeinde", "wid", icon=("tabler", "building-community")),
    pl("2 Wochen später: Widerspruch", 70, 30, beim("wid", "Zwei"), fill=GELB, size=32),
    *fig("SP", SPX, BODEN, FH, [("wid", "ruhig"), ("sperl", "denkt")], bis="sp1"),
    *redet("SP_spricht", SPX, BODEN, FH, "sp1", "lra"),
    tisch(SPX, "wid"),
    ns(NAME["SP"], SPX, BODEN, "wid", NFARBE["SP"]),
    ficon("tabler", "folder", SPX - 120, 730, 120, beim("wid", "Widerspruch"), fuell=GELB),
    pl("Abhilfe?", 70, 94, beim("sperl", "abhilft"), fill=WEISS, size=32, bis="sp1"),
    blase("sprech", 640, 220, "sp1", 900, 330, inhalt=["Die Untersagung bleibt. Wir helfen", "nicht ab und legen die Akte",
                                                     "dem Landratsamt vor."], textsize=31,
          figur=("SP_spricht", SPX, BODEN, FH)),
    pl("keine Abhilfe", 70, 94, beim("sp1", "helfen"), fill=HELLROT, size=32),
    ficon("tabler", "arrow-big-right", 1660, 700, 110, beim("sp1", "Landratsamt"), fuell=GELB),
    pl("Vorlage an das Landratsamt", 70, 158, beim("sp1", "Landratsamt"), fill=GELB, size=32),
])

# ===========================================================================================================================
# A3 Landratsamt: Referendarin Körner entwirft den Widerspruchsbescheid
# ===========================================================================================================================
KOX = 1350
KO_H = hh("KO", FH)
tast = ficon("tabler", "keyboard", KOX - 110, 728, 130, beim("ko1", "entwerfe"), fuell=WEISS)
szene(tast, "246tastatur*", 0.8, 0.0)                         # Tippen, sobald Frau Körner zu entwerfen beginnt
folie([("lra", "Fall · Im Landratsamt"), ("ko1", "Fall · Der Entwurf")], [
    hart(boden("lra")),
    *amt("Landratsamt", "lra", icon=("tabler", "building")),
    pl("Akte bei Referendarin Körner", 70, 30, beim("lra", "Akte"), fill=GELB, size=32),
    *fig("KO", KOX, BODEN, KO_H, [("lra", "ruhig")], bis="ko1"),
    *redet("KO_fragt", KOX, BODEN, KO_H, "ko1", "frage"),
    tisch(KOX, "lra"),
    ns(NAME["KO"], KOX, BODEN, "lra", NFARBE["KO"]),
    ficon("tabler", "folder", KOX + 120, 730, 120, beim("lra", "Akte"), fuell=GELB),
    tast,
    blase("sprech", 620, 240, "ko1", 880, 340, inhalt=["Ich entwerfe den", "Widerspruchsbescheid.",
                                                     "Aber was gehört da alles hinein?"], textsize=30,
          figur=("KO_fragt", KOX, BODEN, KO_H)),
    pl("Entwurf: Widerspruchsbescheid", 70, 94, beim("ko1", "Widerspruchsbescheid"), fill=WEISS, size=32),
])

# ===========================================================================================================================
# A4 Die Frage
# ===========================================================================================================================
folie([("frage", "Die Frage · Vorverfahren und Zuständigkeit"), ("frage2", "Die Frage · Tenor, Gründe, Kosten, Belehrung"),
       ("frage3", "Die Frage · 2. Examen: der Entwurf")], [
    *tafel("frage", "Die Frage"),
    z("1. Gibt es überhaupt ein Vorverfahren?", 110, 190, "frage", size=36),
    z("2. Wer entscheidet?", 110, 250, beim("frage", "wer"), size=36),
    z("3. Wie baust du Tenor, Gründe, Kosten", 110, 330, "frage2", size=36),
    z("und Belehrung?", 150, 380, beim("frage2", "Belehrung"), size=36),
    blk(110, 470, 1040, 140, GELB, "frage3", [("Perspektive des 2. Examens", "ExtraBold", 37, INK),
                                             ("ein Entwurf, Schritt für Schritt", "Bold", 34, INK)]),
    *paar("KO", [("frage", "denkt"), ("frage3", "entschl")], "HO", [("frage", "sorge"), ("frage2", "ruhig")]),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_246(cue, absaetze, frage):
    els = [karte(140, 50, 1640, 930, cue, fill=HELL), titel("Sachverhalt", 210, 84, cue, 56)]
    y = 180
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=35, zeilenabstand=1.30)
        els += e; y += 10
    assert y + 66 <= 975, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=34))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_246("sv", [
    "Herr Holzapfel hält einen verspielten Mischling. Die Gemeinde hat angeordnet, den Hund außerhalb des Grundstücks an "
    "der Leine zu führen. Danach läuft der Hund dreimal frei durch den Ort; einmal springt er eine Joggerin an, die "
    "stürzt. Mit Bescheid vom 2.3.2026, bekannt gegeben am 4.3.2026, untersagt die Gemeinde Herrn Holzapfel die "
    "Hundehaltung.",
    "Am 16.3.2026 legt Herr Holzapfel schriftlich Widerspruch ein: Der Hund sei ganz lieb, den Gartenzaun habe er "
    "erhöht. Herr Sperling von der Gemeinde hilft nicht ab und legt die Akte dem Landratsamt als nächsthöherer Behörde "
    "vor. Das Landesrecht sieht den Widerspruch vor.",
    "Bearbeitervermerk: Die Rechtmäßigkeit der Untersagung ist zu unterstellen. Referendarin Körner entwirft den "
    "Widerspruchsbescheid.",
], "Wie sieht der Widerspruchsbescheid aus?")

# ===========================================================================================================================
# C 1. Vorverfahren: § 68 Abs. 1 VwGO (Wortlautkarte), Landesrecht
# ===========================================================================================================================
P1 = "1. Vorverfahren"
w68, w68_y = wortlaut(80, 160, 1100,
                      "„Vor Erhebung der Anfechtungsklage sind Rechtmäßigkeit und Zweckmäßigkeit des Verwaltungsakts in "
                      "einem Vorverfahren nachzuprüfen. Einer solchen Nachprüfung bedarf es nicht, wenn ein Gesetz dies "
                      "bestimmt oder wenn …“", "§ 68 Abs. 1 Satz 1, 2 VwGO", beim("vv", "Vor", 2),
                      marken=[("Rechtmäßigkeit", beim("vv", "Rechtmäßigkeit")), ("Zweckmäßigkeit", beim("vv", "Zweckmäßigkeit")),
                              ("Gesetz dies", beim("wl68", "Gesetz"))], size=32)
folie([("vv", f"{P1} › Gibt es eines?"), ("wl68", f"{P1} › „wenn ein Gesetz dies bestimmt“"),
       ("land", f"{P1} › Landesrecht: oft abgeschafft"), ("land2", f"{P1} › Landesrecht prüfen")], [
    *tafel("vv", "1. Gibt es ein Vorverfahren?"),
    *w68,
    blk(110, w68_y + 20, 1040, 190, LILAHELL, "land", [("Widerspruch weitgehend abgeschafft, mit Ausnahmen:", "Bold", 31, INK),
                                                      ("Nordrhein-Westfalen: § 110 JustG NRW", "Regular", 31, INK),
                                                      ("Niedersachsen: § 80 NJG", "Regular", 31, INK)]),
    z("in vielen Ländern abgeschafft – Landesrecht prüfen", 110, w68_y + 236, "land2", "Bold", 32),
    *okz("Fall: Das Landesrecht sieht den Widerspruch vor.", w68_y + 300, beim("land2", "In"), "Bold", 32),
    *requisit([(beim("vv", "Rechtmäßigkeit"), ("tabler", "scale", 120, WEISS), "Rechtmäßigkeit + Zweckmäßigkeit", WEISS),
               ("land", ("tabler", "map-2", 120, LILAHELL), "Landesrecht", LILAHELL)]),
    *stehend("KO", FX, [("vv", "ruhig"), ("wl68", "denkt"), ("land2", "froh")]),
])
assert w68_y + 360 <= 900, w68_y

# ===========================================================================================================================
# D 2. Abhilfe § 72 und Zuständigkeit § 73 Abs. 1 VwGO (Wortlautkarten)
# ===========================================================================================================================
P2 = "2. Wer entscheidet?"
w72, w72_y = wortlaut(80, 160, 1100, "„Hält die Behörde den Widerspruch für begründet, so hilft sie ihm ab und entscheidet "
                      "über die Kosten.“", "§ 72 VwGO", beim("abhilfe", "Hält"),
                      marken=[("hilft sie ihm ab", beim("abhilfe", "hilft"))], size=31)
w73, w73_y = wortlaut(80, w72_y + 16, 1100, "„Hilft die Behörde dem Widerspruch nicht ab, so ergeht ein Widerspruchsbescheid. "
                      "Diesen erläßt 1. die nächsthöhere Behörde, soweit nicht durch Gesetz eine andere höhere Behörde "
                      "bestimmt wird, …“", "§ 73 Abs. 1 Satz 1, 2 Nr. 1 VwGO", "wl73",
                      marken=[("ergeht ein", beim("wl73", "ergeht")),
                              ("nächsthöhere Behörde", beim("wl73", "nächsthöhere"))], size=31)
folie([("abhilfe", f"{P2} › Abhilfe, § 72 VwGO"), ("wl73", f"{P2} › nächsthöhere Behörde, § 73 Abs. 1 VwGO"),
       ("naechst", f"{P2} › Fall: das Landratsamt"), ("ausn", f"{P2} › Ausnahmen")], [
    *tafel("abhilfe", "2. Abhilfe und Zuständigkeit"),
    *w72, *w73,
    *okz("Fall: das Landratsamt", w73_y + 14, "naechst", "Bold", 32),
    z("Gesetz kann Ausgangsbehörde zuständig machen (Satz 3)", 110, w73_y + 70, "ausn", size=30),
    z("Selbstverwaltungsangelegenheiten: Selbstverwaltungsbehörde (Nr. 3)", 110, w73_y + 114,
      beim("ausn", "Selbstverwaltungsangelegenheiten"), size=30),
    pl("Ausgangsbehörde", X1, 250, beim("abhilfe", "Ausgangsbehörde"), fill=WEISS, size=28, anker="m"),
    pl("nächsthöhere Behörde", X2, 322, beim("wl73", "nächsthöhere"), fill=GELB, size=28, anker="m"),
    *paar("SP", [("abhilfe", "ruhig"), ("wl73", "ernst")], "KO", [("abhilfe", "denkt"), ("naechst", "entschl")]),
])
assert w73_y + 160 <= 900, w73_y

# ===========================================================================================================================
# E 3. Der Bescheid: Kopf und Tenor
# ===========================================================================================================================
P3 = "3. Bescheid"
folie([("kopf", f"{P3} › Kopf"), ("tenor", f"{P3} › Tenor › 1. Entscheidung"), ("tenor2", f"{P3} › Tenor › 2. Kosten"),
       ("tenor3", f"{P3} › Tenor › 3. Gebühr")], [
    *tafel("kopf", "3. Bescheid: Kopf und Tenor"),
    feld(100, 168, 1060, 236, beim("kopf", "Kopf"), fill=WEISS, rand=3, rund=12, name="briefkopf"),
    z("Landratsamt", 130, 184, beim("kopf", "Behörde"), "Bold", 31),
    z("Datum: 9.4.2026", 680, 184, beim("kopf", "Datum"), size=30),
    z("Az.: …", 130, 230, beim("kopf", "Aktenzeichen"), size=30),
    z("Herrn Holzapfel", 680, 230, beim("kopf", "Adressat"), size=30),
    z("Mit Postzustellungsurkunde", 130, 276, beim("kopf", "Art"), size=30),
    z("Widerspruchsbescheid", 130, 330, beim("kopf", "Überschrift"), "ExtraBold", 38),
    feld(100, 432, 1060, 390, "tenor", fill=HELL, rand=3, rund=12, name="tenorfeld"),
    z("Tenor", 130, 446, "tenor", "ExtraBold", 34),
    z("1. Der Widerspruch wird zurückgewiesen.", 130, 506, beim("tenor", "Der", 2), "Bold", 32),
    z("2. Die Kosten des Verfahrens trägt der", 130, 574, "tenor2", "Bold", 32),
    z("Widerspruchsführer.", 170, 618, beim("tenor2", "Widerspruchsführer"), "Bold", 32),
    z("3. Für diesen Bescheid wird eine Gebühr von … €", 130, 686, "tenor3", "Bold", 32),
    z("erhoben.", 170, 730, beim("tenor3", "erhoben"), "Bold", 32),
    zit("ob und in welcher Höhe: Kostenrecht des Landes", 170, 778, beim("tenor3", "Ob")),
    *requisit([(beim("kopf", "Kopf"), ("tabler", "file-text", 110, WEISS), "Kopf", WEISS),
               ("tenor", ("tabler", "writing", 110, HELL), "Tenor", HELL),
               ("tenor2", ("tabler", "currency-euro", 110, GELB), "Kosten", GELB),
               (beim("tenor3", "Gebühr"), ("tabler", "receipt", 110, WEISS), "Gebühr", WEISS)]),
    *stehend("KO", FX, [("kopf", "ruhig"), ("tenor", "entschl"), ("tenor3", "denkt")]),
])

# ===========================================================================================================================
# F1 Gründe: I. Sachverhalt, II. Zulässigkeit
# ===========================================================================================================================
folie([("gruende", f"{P3} › Gründe › I. Sachverhalt"), ("zul", f"{P3} › Gründe › II. Zulässigkeit")], [
    *tafel("gruende", "3. Gründe"),
    z("I. Sachverhalt", 110, 180, beim("gruende", "römisch"), "ExtraBold", 36),
    z("Bescheid", 150, 240, beim("gruende", "Bescheid"), size=33),
    z("· Widerspruch", 300, 240, beim("gruende", "Widerspruch"), size=33),
    z("· Nichtabhilfe", 520, 240, beim("gruende", "Nichtabhilfe"), size=33),
    z("II. Rechtliche Würdigung", 110, 330, beim("zul", "römisch"), "ExtraBold", 36),
    z("1. Zulässigkeit", 150, 400, beim("zul", "Zulässigkeit"), "Bold", 34),
    *okz("statthaft", 460, beim("zul", "statthaft"), size=33, x=235),
    *okz("innerhalb eines Monats schriftlich erhoben", 520, beim("zul", "innerhalb"), size=33, x=235),
    zit("§ 70 Abs. 1 Satz 1 VwGO; hier: 16.3.2026 nach Bekanntgabe am 4.3.2026", 235, 572, beim("zul", "Paragraf")),
    *requisit([("gruende", ("tabler", "file-text", 110, WEISS), "Gründe", WEISS),
               (beim("zul", "innerhalb"), ("tabler", "calendar-event", 110, HELLGRUEN), "innerhalb 1 Monat", HELLGRUEN)]),
    *stehend("KO", FX, [("gruende", "ruhig"), ("zul", "froh")]),
])

# ===========================================================================================================================
# F2 Gründe: Begründetheit – Rechtmäßigkeit und Zweckmäßigkeit
# ===========================================================================================================================
folie([("begr", f"{P3} › Gründe › 2. Begründetheit"), ("recht", f"{P3} › Gründe › a) Rechtmäßigkeit"),
       ("zweck", f"{P3} › Gründe › b) Zweckmäßigkeit"), ("zweck2", f"{P3} › Gründe › b) Zweckmäßigkeit: Untersagung bleibt")], [
    *tafel("begr", "3. Gründe: Begründetheit"),
    z("2. Begründetheit: Rechtmäßigkeit und Zweckmäßigkeit", 110, 180, beim("begr", "Begründetheit"), "Bold", 33),
    z("Die Widerspruchsbehörde prüft mehr als ein Gericht.", 110, 236, beim("begr", "Hier"), size=31),
    zit("§ 68 Abs. 1 Satz 1 VwGO; BVerwG, Urt. v. 12.8.2014 – 1 C 2.14, Rn. 13", 110, 280, beim("begr", "Rechtmäßigkeit")),
    z("a) Rechtmäßigkeit: wie im Urteil", 110, 350, "recht", "ExtraBold", 34),
    *plusminus("Untersagung rechtmäßig (Bearbeitervermerk)", 150, 404, beim("recht", "Hier"), True, size=31, stil="Bold"),
    z("b) Zweckmäßigkeit: selbst beurteilen –", 110, 486, "zweck", "ExtraBold", 34),
    z("Ist die Untersagung das richtige Mittel?", 150, 538, beim("zweck", "ob"), size=32),
    z("Würde eine neue Leinenpflicht reichen?", 150, 594, beim("zweck", "Würde"), size=32),
    *neinz("Nein: Die alte hat Herr Holzapfel 3 × missachtet.", 660, "zweck2", "Bold", 31, x=195),
    *neinz("Der höhere Zaun hilft beim Spaziergang nicht.", 716, beim("zweck2", "höhere"), "Bold", 31, x=195),
    *requisit([(beim("begr", "mehr"), ("tabler", "scale", 120, WEISS), "mehr als ein Gericht", WEISS),
               (beim("zweck", "Würde"), ("fluent-emoji-high-contrast", "dog", 160, HUND), "neue Leinenpflicht?", BLAUHELL),
               (beim("zweck2", "höhere"), ("tabler", "fence", 140, WEISS), "Zaun hilft unterwegs nicht", HELLROT)]),
    *stehend("KO", FX, [("begr", "ruhig"), ("zweck", "denkt"), ("zweck2", "entschl")]),
])

# ===========================================================================================================================
# G Kosten: § 73 Abs. 3 Satz 3 VwGO, § 80 VwVfG (Wortlautkarte Abs. 1 Satz 3), Abs. 3 Satz 2
# ===========================================================================================================================
w80, w80_y = wortlaut(80, 352, 1100, "„Soweit der Widerspruch erfolglos geblieben ist, hat derjenige, der den Widerspruch "
                      "eingelegt hat, die zur zweckentsprechenden Rechtsverfolgung oder Rechtsverteidigung notwendigen "
                      "Aufwendungen der Behörde, die den angefochtenen Verwaltungsakt erlassen hat, zu erstatten; …“",
                      "§ 80 Abs. 1 Satz 3 VwVfG", "k80b",
                      marken=[("erfolglos", beim("k80b", "erfolglos")), ("Aufwendungen", beim("k80b", "Aufwendungen"))],
                      size=30)
folie([("kosten", f"{P3} › Kosten › § 73 Abs. 3 Satz 3 VwGO"), ("k80", f"{P3} › Kosten › § 80 VwVfG"),
       ("k80b", f"{P3} › Kosten › erfolglos: Aufwendungen der Ausgangsbehörde"),
       ("anwalt", f"{P3} › Kosten › bei Erfolg: Anwalt notwendig?")], [
    *tafel("kosten", "3. Gründe: die Kosten"),
    z("„Der Widerspruchsbescheid bestimmt auch, wer die", 110, 170, beim("kosten", "Dass"), size=31),
    z("Kosten trägt.“", 110, 212, beim("kosten", "Dass"), size=31),
    zit("§ 73 Abs. 3 Satz 3 VwGO", 340, 220, beim("kosten", "Paragraf")),
    z("Erstattung: § 80 VwVfG, bei Landesbehörden", 110, 270, "k80", "Bold", 31),
    z("das Gesetz des Landes", 150, 312, beim("k80", "Landesbehörden"), "Bold", 31),
    zit("z. B. § 80 VwVfG NRW, wortgleich", 520, 320, beim("k80", "Landesbehörden")),
    *w80,
    *okz("bei Erfolg: Anwalt notwendig?", w80_y + 16, "anwalt", "Bold", 32),
    zit("§ 80 Abs. 3 Satz 2 VwVfG", 720, w80_y + 24, beim("anwalt", "Anwalt")),
    *requisit([("kosten", ("tabler", "currency-euro", 110, GELB), "Kosten", GELB),
               ("k80b", ("tabler", "receipt", 110, WEISS), "Aufwendungen erstatten", WEISS),
               ("anwalt", ("tabler", "briefcase", 110, BLAUHELL), "Anwalt notwendig?", BLAUHELL)]),
    *stehend("HO", FX, [("kosten", "ernst"), ("k80b", "sorge"), ("anwalt", "denkt")]),
])
assert w80_y + 80 <= 900, w80_y

# ===========================================================================================================================
# H Rechtsbehelfsbelehrung (§ 58 Abs. 1 VwGO, Muster)
# ===========================================================================================================================
folie([("belehr", f"{P3} › Rechtsbehelfsbelehrung › § 58 Abs. 1 VwGO"), ("muster", f"{P3} › Rechtsbehelfsbelehrung › Muster"),
       ("sitz", f"{P3} › Rechtsbehelfsbelehrung › Name und Sitz")], [
    *tafel("belehr", "3. Rechtsbehelfsbelehrung"),
    z("nennt:", 110, 180, beim("belehr", "nennt"), "Bold", 33),
    *reihe([("Rechtsbehelf", beim("belehr", "Rechtsbehelf", 2)), ("Gericht", beim("belehr", "Gericht")),
            ("Sitz", beim("belehr", "Sitz")), ("Frist", beim("belehr", "Frist"))], 240, 176),
    zit("§ 58 Abs. 1 VwGO", 110, 246, beim("belehr", "Paragraf")),
    blk(110, 300, 1040, 300, HELL, "muster", [("Rechtsbehelfsbelehrung", "ExtraBold", 32, INK),
                                             ("„Gegen den Bescheid der Gemeinde vom 2.3.2026 in", "Regular", 31, INK),
                                             ("Gestalt dieses Widerspruchsbescheids kann innerhalb", "Regular", 31, INK),
                                             ("eines Monats nach Zustellung Klage beim Verwaltungs-", "Regular", 31, INK),
                                             ("gericht [Name, Sitz] erhoben werden.“", "Regular", 31, INK)]),
    zit("§§ 58 Abs. 1, 74 Abs. 1 Satz 1, 79 Abs. 1 Nr. 1 VwGO", 110, 614, beim("muster", "Gegen")),
    *okz("Name und Sitz des Gerichts konkret eintragen", 680, "sitz", "Bold", 32),
    *requisit([("belehr", ("tabler", "info-circle", 110, GELB), "Belehrung", GELB),
               ("muster", ("fluent-emoji-high-contrast", "classical-building", 140, WEISS), "Verwaltungsgericht", WEISS)]),
    *stehend("KO", FX, [("belehr", "ruhig"), ("muster", "entschl"), ("sitz", "froh")]),
])

# ===========================================================================================================================
# I Zustellung: § 73 Abs. 3 VwGO (Wortlautkarte), § 3 VwZG, Klagefrist § 74 Abs. 1 Satz 1 VwGO
# ===========================================================================================================================
w733, w733_y = wortlaut(80, 160, 1100, "„Der Widerspruchsbescheid ist zu begründen, mit einer Rechtsmittelbelehrung zu "
                        "versehen und zuzustellen. Zugestellt wird von Amts wegen nach den Vorschriften des "
                        "Verwaltungszustellungsgesetzes. Der Widerspruchsbescheid bestimmt auch, wer die Kosten trägt.“",
                        "§ 73 Abs. 3 VwGO", beim("zust", "Paragraf"),
                        marken=[("zu begründen", beim("zust", "begründen")), ("Rechtsmittelbelehrung", beim("zust", "Rechtsmittelbelehrung")),
                                ("zuzustellen", beim("zust", "zustellen")), ("von Amts wegen", beim("zust", "Amts")),
                                ("Verwaltungszustellungsgesetzes", beim("zust", "Verwaltungszustellungsgesetz"))], size=32)
post = ficon("fluent-emoji-high-contrast", "closed-mailbox-with-raised-flag", PX, PU, 130, beim("pzu", "Post"), fuell=WEISS)
szene(post, "246briefkasten*", 0.7, -0.2)                   # Klappe, wenn der Bescheid im Briefkasten ankommt
folie([("zust", f"{P3} › Zustellung, § 73 Abs. 3 VwGO"), ("pzu", f"{P3} › Zustellung › Postzustellungsurkunde"),
       ("frist", f"{P3} › Zustellung › Klagefrist 1 Monat")], [
    *tafel("zust", "3. Zustellung"),
    *w733,
    z("etwa: durch die Post mit Zustellungsurkunde", 110, w733_y + 20, "pzu", "Bold", 32),
    zit("§§ 2 Abs. 3, 3 VwZG", 830, w733_y + 28, beim("pzu", "Post")),
    *okz("ab Zustellung: Klagefrist 1 Monat", w733_y + 90, "frist", "Bold", 32),
    zit("§ 74 Abs. 1 Satz 1 VwGO", 730, w733_y + 98, beim("frist", "Paragraf")),
    pl("Zustellung", PX, PY, "zust", fill=GELB, size=28, anker="m"),
    *rechts_frei([ficon("tabler", "mail", PX, PU, 120, "zust", fuell=WEISS, bis=beim("pzu", "Post")), post]),
    *stehend("HO", FX, [("zust", "ruhig"), ("pzu", "denkt"), ("frist", "ernst")]),
])
assert w733_y + 150 <= 900, w733_y

# ===========================================================================================================================
# J 4. Typische Fehler
# ===========================================================================================================================
P4 = "4. Typische Fehler"
folie([("fehler", P4), ("f1", f"{P4} › Zweckmäßigkeit fehlt"), ("f2", f"{P4} › falsche Belehrung")], [
    *tafel("fehler", "4. Typische Fehler"),
    *neinz("Fehler 1: Die Zweckmäßigkeit fehlt.", 180, "f1", "Bold", 34),
    z("Bei Ermessen beurteilt die Widerspruchsbehörde", 185, 236, beim("f1", "Bei"), size=32),
    z("sie grundsätzlich mit.", 185, 280, beim("f1", "Bei"), size=32),
    zit("BVerwG, Urt. v. 12.8.2014 – 1 C 2.14, Rn. 13", 185, 326, beim("f1", "grundsätzlich")),
    *neinz("Fehler 2: eine falsche Belehrung", 410, "f2", "Bold", 34),
    z("Dann läuft statt 1 Monat die Jahresfrist.", 185, 466, beim("f2", "Dann"), size=32),
    zit("§ 58 Abs. 2 VwGO", 185, 512, beim("f2", "Jahresfrist")),
    *requisit([("fehler", ("tabler", "alert-triangle", 110, HELLROT), "Fehler", HELLROT),
               (beim("f2", "Dann"), ("tabler", "calendar-event", 110, HELLROT), "Jahresfrist statt 1 Monat", HELLROT)]),
    *stehend("KO", FX, [("fehler", "ernst"), ("f1", "denkt"), ("f2", "ernst")]),
])

# ===========================================================================================================================
# K Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Wogegen richtet sich die Klage?"), ("tipp2", "Klausurtipp › Belehrung nennt beide Bescheide"),
       ("tipp3", "Klausurtipp › Vorbringen würdigen")], [
    *tafel("tipp", "Klausurtipp: Wogegen richtet sich die Klage?", fill=HELL, size=42),
    warnung_i(150, 225, "tipp", gr=26),
    z("Gegen den ursprünglichen Bescheid in der Gestalt,", 200, 200, "tipp", "ExtraBold", 33),
    z("die er durch den Widerspruchsbescheid gefunden hat.", 200, 248, beim("tipp", "die", 2), size=33),
    zit("§ 79 Abs. 1 Nr. 1 VwGO", 200, 296, beim("tipp", "Paragraf")),
    linienzug([(130, 356), (1130, 356)], "tipp2", breite=3),
    *okz("Deshalb nennt deine Belehrung beide Bescheide.", 386, "tipp2", "Bold", 33, x=240),
    *okz("In den Gründen das Vorbringen würdigen:", 476, "tipp3", "Bold", 33, x=240),
    z("hier den höheren Zaun", 240, 526, beim("tipp3", "hier"), size=33),
    zit("vgl. § 39 Abs. 1 Satz 2 VwVfG", 240, 574, beim("tipp3", "hier")),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# L Schema (Lexi), Punkt für Punkt
# ===========================================================================================================================
folie([("sch", "Schema · Widerspruchsbescheid"), ("s1", "Schema › 1. Kopf"), ("s2", "Schema › 2. Tenor"),
       ("s3", "Schema › 3. Gründe"), ("s3b", "Schema › 3. Gründe › Kosten"), ("s4", "Schema › 4. Rechtsbehelfsbelehrung"),
       ("s5", "Schema › 5. Zustellung")], [
    *tafel("sch", "Schema: Widerspruchsbescheid"),
    z("1. Kopf", 110, 180, "s1", size=33),
    z("2. Tenor: Entscheidung, Kosten, Gebühr", 110, 246, "s2", size=33),
    z("3. Gründe: Sachverhalt, Zulässigkeit,", 110, 312, "s3", size=33),
    z("Begründetheit mit Rechtmäßigkeit und Zweckmäßigkeit", 150, 358, beim("s3", "Begründetheit"), size=33),
    z("dazu die Kosten nach § 80 VwVfG", 150, 404, "s3b", size=33),
    z("4. Rechtsbehelfsbelehrung", 110, 470, "s4", size=33),
    z("5. Zustellung", 110, 536, "s5", size=33),
    *redet("LX_erklaert", FX, FB, FR + 40, "sch", "merke"),
    ns("Lexi", FX, FB, "sch", GELB, d=0.2),
])

# ===========================================================================================================================
# M Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Die Widerspruchsbehörde prüft", 0)], [("Rechtmäßigkeit", "a"), (" und ", 0), ("Zweckmäßigkeit", "b"), (".", 0)]],
                750, 300, 44, "merke", {"a": beim("merke", "Rechtmäßigkeit"), "b": beim("merke", "Zweckmäßigkeit")}),
    *markertext([[("Ihr Bescheid braucht Tenor, Gründe,", 0)], [("Kosten, ", 0), ("Belehrung", "c"), (" und ", 0), ("Zustellung", "d"), (".", 0)]],
                750, 520, 44, "m2", {"c": beim("m2", "Belehrung"), "d": beim("m2", "Zustellung")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
