"""Folge 208 · Rauchverbot-Urteil: Gleichheit trifft Berufsfreiheit (Art. 12, 3 GG) – Serienstandard Open Peeps (Katzenkönig).
Fiktiver Rahmen, der dem echten Fall von BVerfGE 121, 317 folgt: Alfons führt eine Einraumkneipe in Baden-Württemberg
(63 m², überwiegend Stammgäste); größere Lokale dürfen Raucherräume einrichten; Stammgast Herr Stadler geht ins große Lokal am
Markt. Frau Kaltenbach darf in ihrer Großraumdiskothek (Zutritt nur ab 18) keinen Raucherraum einrichten. Danach Art. 12
Abs. 1 GG (Wortlautkarte), Eingriff als Berufsausübungsregelung, Rechtfertigung, striktes Verbot zulässig, Folgerichtigkeit,
Ergebnis, Art. 3 Abs. 1 GG (Wortlautkarte) nur für die Diskothek, Tenor und Übergangsregelung, zurück zu Alfons, Klausurtipp,
Schema, Merksatz. DARSTELLUNG: keine Tabakmarken, keine Zigarette in der Hand, nur das durchgestrichene Symbol
(tabler smoking-no); Wirt sympathisch.
Szenen laut ../SZENENPLAN.md. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/requisit/stehend/paar
als eigene Kopie aus Folge 205 (gemeinsame Dateien unverändert); treppe() nach Folge 169; neu: fassade(), minilokal().
Handlungsgeräusche: Schritte und Tür (Herr Stadler geht ins große Lokal); ../geraeusche_herkunft.json.
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut nach gesetze-im-internet.de (GG), Abruf 06.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_208/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_208/" in n:
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
NAME = {"AL": "Alfons", "SA": "Herr Stadler", "KA": "Frau Kaltenbach"}
NFARBE = {"AL": ORANGE, "SA": BLAU, "KA": PINK}
FASSADE = (246, 232, 210, 255)
STUFE = {1: (BLAU, BLAUHELL), 2: (LILA, LILAHELL), 3: (ROT, HELLROT)}


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



def fassade(x0, x1, oben, cue, schild, icon=None, fenster=(), tuer_x=None, fill=FASSADE, name="fassade"):
    """Hausfassade aus Grundformen: Fläche, Schildband mit Schriftzug (+ Tabler-Icon), Fenster mit Icons, Tür.
    fenster = [(x_links, breite, [(set, icon, breite, fuell)])] relativ zur Fassade. Keine Marken, keine Logos."""
    w, h = x1 - x0, BODEN - oben
    im, dr, s = _flaeche(w, h)
    o = 6 * s
    dr.rectangle((o, o, o + w * s, o + h * s), fill=fill, outline=INK, width=5 * s)
    dr.rectangle((o, o, o + w * s, o + 76 * s), fill=GELB, outline=INK, width=5 * s)
    for fx, fw, _ in fenster:
        dr.rectangle((o + fx * s, o + 120 * s, o + (fx + fw) * s, o + (h - 90) * s), fill=BLAUHELL, outline=INK, width=5 * s)
    if tuer_x is not None:
        dr.rectangle((o + tuer_x * s, o + (h - 230) * s, o + (tuer_x + 110) * s, o + h * s), fill=HOLZ, outline=INK, width=5 * s)
        dr.ellipse((o + (tuer_x + 84) * s, o + (h - 120) * s, o + (tuer_x + 98) * s, o + (h - 106) * s), fill=INK)
    im = im.resize((w + 12, h + 12), Image.LANCZOS)
    f = F("ExtraBold", 40)
    tw = f.getlength(glyphen(schild))
    ic = ficon("tabler", icon, 0, 0, 48, "_", fuell=WEISS).sprite if icon else None
    gx = int((w + 12 - tw - (ic.width + 14 if ic else 0)) / 2)
    if ic:
        im.alpha_composite(ic, (gx, int(44 - ic.height / 2))); gx += ic.width + 14
    ImageDraw.Draw(im).text((gx, 18), schild, font=f, fill=INK)
    for fx, fw, icons in fenster:
        my = (120 + h - 90) / 2 + 6
        for k, (st, nm, br, fu) in enumerate(icons):
            ic2 = ficon(st, nm, 0, 0, br, "_", fuell=fu).sprite
            dx = (k - (len(icons) - 1) / 2) * (br + 16)
            im.alpha_composite(ic2, (int(6 + fx + fw / 2 + dx - ic2.width / 2), int(my - ic2.height / 2)))
    return hart(El(im, x0 - 6, oben - 6, cue, "cut", 0.0, None, name=name))


_TR = {}


def treppe(x0, unten, sb, sh, cue, aktiv=None, bis=None, anim="pop", name="treppe"):
    """Drei Stufen aus Grundformen (wie Folge 169: Stufe 1 Blau, 2 Lila, 3 Rot); aktiv = hervorgehobene Stufe."""
    key = (sb, sh, aktiv)
    if key not in _TR:
        w, h = 3 * sb, 3 * sh
        im, dr, s = _flaeche(w, h)
        o = 6 * s
        for i in range(3):
            voll, hell = STUFE[i + 1]
            fill = voll if aktiv in (None, i + 1) else hell
            dr.rectangle((o + i * sb * s, o + (h - (i + 1) * sh) * s, o + (i + 1) * sb * s, o + h * s), fill=fill,
                         outline=INK, width=(7 if aktiv == i + 1 else 5) * s)
        im = im.resize((w + 12, h + 12), Image.LANCZOS)
        f = F("ExtraBold", max(30, int(sh * 0.55)))
        dr2 = ImageDraw.Draw(im)
        for i in range(3):
            t = str(i + 1)
            dr2.text((6 + i * sb + (sb - f.getlength(t)) / 2, 6 + h - (i + 1) * sh + sh * 0.18), t, font=f, fill=INK)
        _TR[key] = im
    im = _TR[key]
    return El(im, x0 - 6, unten - im.height + 6, cue, anim, 0.0, bis, name="bild:" + name)


# ===========================================================================================================================
# A1 Fall: die Einraumkneipe von Alfons und das große Lokal am Markt (fiktiv, folgt Rn. 37–39)
# ===========================================================================================================================
ALX, SAX, SAX2 = 690, 960, 1775
KN_TUER = 330                       # Tür der kleinen Kneipe (relativ)


def strasse(cue, raucherraum=None):
    els = [boden(cue),
           fassade(70, 520, 430, cue, "Kneipe", "beer", fenster=[(30, 250, [("tabler", "beer", 70, GELB)])], tuer_x=KN_TUER,
                   name="kneipe"),
           fassade(1160, 1860, 330, cue, "Lokal am Markt", "glass-full",
                   fenster=[(30, 260, [("tabler", "beer", 70, GELB), ("tabler", "glass-full", 66, WEISS)]),
                            (320, 200, [])], tuer_x=560, name="lokal"),
           hart(ficon("tabler", "smoking-no", 70 + KN_TUER + 61, BODEN - 250, 74, cue, fuell=WEISS))]
    if raucherraum:
        els.append(pl("Raucherraum", 1160 + 320 + 106, 560, raucherraum, fill=WEISS, size=28, anker="m"))
    return els


TUERX = 1160 + 560                  # Tür des großen Lokals (absolut, links)
WEG = ("umsatz", 2.6)                # Ende des Weges von Herrn Stadler
ZU = ("umsatz", 2.8)                 # Tür fällt zu


def tuer_offen(cue, bis):
    """Offene Tür des großen Lokals (dunkle Öffnung), solange Herr Stadler hineingeht."""
    return El(_feld(110, 230, INK, 5, 2), TUERX - 6, BODEN - 230 - 6, cue, "cut", 0.0, bis, name="tuer_offen")


def tuer_zu(cue):
    im, dr, s_ = _flaeche(110, 230)
    o = 6 * s_
    dr.rectangle((o, o, o + 110 * s_, o + 230 * s_), fill=HOLZ, outline=INK, width=5 * s_)
    dr.ellipse((o + 84 * s_, o + 110 * s_, o + 98 * s_, o + 124 * s_), fill=INK)
    return El(im.resize((122, 242), Image.LANCZOS), TUERX - 6, BODEN - 230 - 6, cue, "cut", 0.0, None, name="tuer_zu")


folie([(NULL, "Fall · Alfons und seine kleine Kneipe"), ("verbot", "Fall · Rauchverbot in Gaststätten"),
       ("nebenraum", "Fall · Größere Lokale: Raucherraum erlaubt"), ("st1", "Fall · Der Stammgast geht"),
       ("a1", "Fall · Ist das gerecht?")], [
    *strasse(NULL, raucherraum="nebenraum"),
    hart(pl("Alfons: kleine Kneipe in Baden-Württemberg", 70, 40, NULL, fill=ORANGE, size=32)),
    pl("1 Gastraum · 63 m²", 70, 108, "raum", fill=WEISS, size=30, bis="st1"),
    pl("überwiegend Stammgäste · rund 70 % Raucher (nach seinen Angaben)", 70, 170, "gaeste", fill=WEISS, size=28, bis="st1"),
    pl("seit August 2007: Rauchverbot in Gaststätten", 70, 232, "verbot", fill=HELLROT, size=30, bis="st1"),
    pl("größere Lokale: Raucherraum erlaubt", 1160, 250, "nebenraum", fill=HELLGRUEN, size=28, bis="st1"),
    pl("Raum nicht teilbar", 255, 512, "kein", fill=HELLROT, size=28, anker="m"),
    nein(100, 538, beim("kein", "nicht")),
    *fig("AL", ALX, BODEN, FH, [(NULL, "ruhig_r"), ("verbot", "denkt_r"), ("kein", "sorge_r")], bis="a1", erst="cut"),
    *redet("AL_redet_r", ALX, BODEN, FH, "a1", "disko"),
    hart(ns(NAME["AL"], ALX, BODEN, NULL, ORANGE)),
    # Herr Stadler verabschiedet sich und geht ins große Lokal am Markt (Schritte, Tür)
    *redet("SA_redet", SAX, BODEN, FH, "st1", "umsatz"),
    ns(NAME["SA"], SAX, BODEN, "st1", BLAU, bis="umsatz"),
    blase("sprech", 700, 220, "st1", 1080, 215, inhalt=["Tut mir leid, Alfons.", "Ich gehe jetzt ins große Lokal",
                                                     "am Markt, da gibt es einen Raucherraum."],
          textsize=30, figur=("SA_redet", SAX, BODEN, FH), bis="umsatz"),
    tuer_offen(("umsatz", 1.9), ZU),
    szene(bewegt(peep_voll("SA_ruhig_r", SAX2, BODEN, FH, "umsatz", anim="cut", bis=ZU), "umsatz", WEG, SAX - SAX2),
          "208schritte*", 0.9, 0.0),
    bewegt(ns(NAME["SA"], SAX2, BODEN, "umsatz", BLAU, bis=ZU, anim="cut"), "umsatz", WEG, SAX - SAX2),
    szene(tuer_zu(ZU), "208tuer*", 0.8, -0.1),
    pl("Umsatz zunächst −30 bis 40 % (nach seinen Angaben)", 70, 108, "umsatz", fill=HELLROT, size=30),
    ficon("tabler", "trending-down", 900, 172, 70, "umsatz"),
    blase("sprech", 660, 220, "a1", 760, 290, inhalt=["Meine Kneipe muss rauchfrei sein,", "das große Lokal nicht.",
                                                    "Ist das gerecht?"],
          textsize=30, figur=("AL_redet_r", ALX, BODEN, FH)),
])

# ===========================================================================================================================
# A2 Fall: die Großraumdiskothek von Frau Kaltenbach (Zutritt nur ab 18; Rn. 54–59; § 7 Abs. 2 Satz 2 LNRSchG BW, Rn. 6)
# ===========================================================================================================================
KAX = 1560
folie([("disko", "Fall · Frau Kaltenbachs Diskothek"), ("disko2", "Fall · Raucherraum? Nicht für Diskotheken"),
       ("ka1", "Fall · Nur wir nicht?")], [
    boden("disko"),
    fassade(80, 1220, 300, "disko", "Diskothek", "music",
            fenster=[(40, 300, [("tabler", "music", 70, LILA), ("tabler", "device-speaker", 64, BLAU)]),
                     (380, 300, [("tabler", "music", 70, PINK)]), (720, 220, [])], tuer_x=990, name="diskothek"),
    hart(pl("ab 18", 80 + 990 + 55, 560, "disko", fill=GELB, size=30, anker="m")),
    pl("Frau Kaltenbach: Großraumdiskothek, Zutritt nur für Erwachsene", 80, 40, "disko", fill=PINK, size=30),
    pl("Raucherraum", 80 + 720 + 110, 560, "disko2", fill=WEISS, size=28, anker="m"),
    nein(80 + 720 + 110, 640, beim("disko2", "nimmt"), gr=34),
    pl("Raucherraum: für Diskotheken ausgeschlossen", 80, 104, beim("disko2", "nimmt"), fill=HELLROT, size=30),
    pl("§ 7 Abs. 2 Satz 2 LNRSchG BW: „Satz 1 gilt nicht für Diskotheken.“", 80, 168, beim("disko2", "nimmt"),
       fill=ZITAT, size=28),
    *fig("KA", KAX, BODEN, FH, [("disko", "ruhig"), ("disko2", "ernst")], bis="ka1", erst="cut"),
    *redet("KA_redet", KAX, BODEN, FH, "ka1", "frage"),
    hart(ns(NAME["KA"], KAX, BODEN, "disko", PINK)),
    blase("sprech", 620, 200, "ka1", 1530, 300, inhalt=["Jede Gaststätte darf einen", "Raucherraum haben, nur wir nicht?"],
          textsize=30, figur=("KA_redet", KAX, BODEN, FH)),
])

# ===========================================================================================================================
# A3 Die Frage; das echte Verfahren (Rubrum, Rn. 1, 45)
# ===========================================================================================================================
folie([("frage", "Die Frage · Berufsfreiheit und Gleichheit verletzt?"), ("grund", "Die Frage · Rauchverbot-Urteil, BVerfGE 121, 317"),
       ("berlin", "Die Frage · auch eine Berliner Wirtin klagte")], [
    *tafel("frage", "Die Frage"),
    z("Verletzt das Rauchverbot mit Ausnahmen …", 110, 180, "frage", "Bold", 36),
    z("1. die Berufsfreiheit, Art. 12 Abs. 1 GG?", 170, 250, beim("frage", "Berufsfreiheit"), "Bold", 36),
    z("2. die Gleichheit, Art. 3 Abs. 1 GG?", 170, 320, beim("frage", "Gleichheit"), "Bold", 36),
    blk(110, 420, 1040, 130, GELB, "grund", [("Rauchverbot-Urteil: BVerfG, Urt. v. 30.7.2008", "ExtraBold", 33, INK),
                                            ("1 BvR 3262/07 u. a. · BVerfGE 121, 317", "Regular", 32, INK)]),
    zit("unser Fall folgt dem echten Fall (Rn. 37–59)", 110, 562, "grund"),
    blk(110, 630, 1040, 80, WEISS, "berlin", [("auch geklagt: eine Berliner Wirtin", "ExtraBold", 33, INK)]),
    zit("Rn. 45–53 (Eckkneipe in Berlin)", 110, 722, "berlin"),
    *paar("AL", [("frage", "denkt")], "KA", [("frage", "ernst"), ("grund", "ruhig")]),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_208(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=31, zeilenabstand=1.28)
        els += e; y += 14
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=30))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_208("sv", [
    "Alfons führt seit über 20 Jahren in Baden-Württemberg eine kleine Kneipe: ein einziger Gastraum von 63 m², der sich "
    "baulich nicht teilen lässt. Er schenkt vor allem Getränke aus; seine Gäste sind überwiegend Stammgäste, nach seinen "
    "Angaben zu rund 70 % Raucher.",
    "Seit August 2007 verbietet das Landesnichtraucherschutzgesetz das Rauchen in Gaststätten. Erlaubt bleibt es in "
    "vollständig abgetrennten, gekennzeichneten Nebenräumen, nicht aber in Diskotheken; Bier-, Wein- und Festzelte sind "
    "ganz ausgenommen. Nach seinen Angaben wandern Stammgäste in größere Lokale mit Raucherraum ab, und sein Umsatz "
    "sinkt zunächst um 30 bis 40 %.",
    "Frau Kaltenbach betreibt eine Großraumdiskothek, zu der nur Erwachsene Zutritt haben. Einen Raucherraum darf sie "
    "nicht einrichten. Auch eine Berliner Wirtin klagt gegen das dortige Gesetz, das ebenfalls Raucherräume zulässt. "
    "Alle erheben Verfassungsbeschwerde.",
], "Verletzen die Regelungen Art. 12 Abs. 1 GG, auch i. V. m. Art. 3 Abs. 1 GG?")

# ===========================================================================================================================
# C1 Berufsfreiheit: Wortlautkarte Art. 12 Abs. 1 GG
# ===========================================================================================================================
PI = "I. Schutzbereich"
w12, w12_y = wortlaut(80, 190, 1100, "„(1) Alle Deutschen haben das Recht, Beruf, Arbeitsplatz und Ausbildungsstätte frei zu "
                                     "wählen. Die Berufsausübung kann durch Gesetz oder auf Grund eines Gesetzes geregelt "
                                     "werden. …“", "Art. 12 Abs. 1 GG", "a12",
                      marken=[("Beruf,", beim("a12", "Beruf", 2)), ("frei zu", beim("a12", "frei")),
                              ("Berufsausübung", beim("a12", "Berufsausübung")), ("geregelt", beim("a12", "geregelt"))])
folie([("a12", f"{PI} · Wortlaut, Art. 12 Abs. 1 GG")], [
    *tafel("a12", "I. Schutzbereich: Berufsfreiheit"),
    *w12,
    *requisit([("a12", ("tabler", "book", 110, WEISS), "Art. 12 Abs. 1 GG", WEISS),
               (beim("a12", "Berufsausübung"), ("tabler", "beer", 110, GELB), "Berufsausübung", BLAUHELL)]),
    *stehend("AL", FX, [("a12", "ruhig"), (beim("a12", "Berufsausübung"), "denkt")]),
])

# ===========================================================================================================================
# C2 Schutzbereich und Eingriff (Rn. 91–95, 114)
# ===========================================================================================================================
folie([("schutz", f"{PI} › Angebot und Gäste"), ("gast", "II. Eingriff › Verbot an die Gäste gerichtet"),
       ("pflicht", "II. Eingriff › Wirt muss Verstöße unterbinden"), ("eingriff", "II. Eingriff › unmittelbar, kein Reflex"),
       ("stufe1", "II. Eingriff › 1. Stufe: Berufsausübungsregelung"), ("eigentum", "II. Eingriff › Art. 14 GG tritt zurück")], [
    *tafel("schutz", "Schutzbereich und Eingriff"),
    *okz("Schutzbereich: Angebot und Gäste", 175, "schutz", "Bold", 33),
    z("selbst festlegen", 185, 221, beim("schutz", "anbietet"), "Bold", 33),
    zit("Rn. 92", 470, 229, beim("schutz", "anbietet")),
    z("Rauchverbot richtet sich zwar an die Gäste", 110, 290, "gast", size=33),
    zit("Rn. 91", 110, 338, "gast"),
    *okz("Wirt darf Rauchen nicht erlauben", 390, "pflicht", "Bold", 33),
    z("und muss Verstöße unterbinden", 185, 436, beim("pflicht", "muss"), "Bold", 33),
    zit("Rn. 93 f.", 720, 444, beim("pflicht", "muss")),
    blk(110, 500, 1040, 80, GELB, "eingriff", [("unmittelbarer Eingriff, kein bloßer Reflex", "ExtraBold", 33, INK)]),
    zit("Rn. 94", 110, 592, "eingriff"),
    blk(110, 640, 1040, 80, BLAU, "stufe1", [("1. Stufe: Berufsausübungsregelung", "ExtraBold", 33, INK)]),
    zit("Rn. 95, 114; Apotheken-Urteil, BVerfGE 7, 377", 110, 732, "stufe1"),
    *neinz("Art. 14 GG tritt zurück: Schwerpunkt Erwerbstätigkeit", 790, "eigentum", "Bold", 31,
           kreuz=beim("eigentum", "tritt")),
    zit("Rn. 91", 1060, 798, "eigentum"),
    *requisit([("schutz", ("tabler", "beer", 110, GELB), "Angebot", GELB),
               ("gast", ("tabler", "smoking-no", 110, WEISS), "an die Gäste", WEISS),
               ("pflicht", ("tabler", "hand-stop", 110, HELLROT), "unterbinden", HELLROT)], bis="stufe1"),
    *rechts_frei([treppe(1420, PU, 100, 60, "stufe1", aktiv=1, bis="eigentum"),
                 pl("Stufe 1: Ausübung", PX, PY, "stufe1", fill=BLAU, size=28, anker="m", bis="eigentum")]),
    *requisit([("eigentum", ("tabler", "home", 110, WEISS), "Art. 14: nein", HELLROT)]),
    *stehend("AL", FX, [("schutz", "ruhig"), ("pflicht", "sorge"), ("stufe1", "ernst")]),
])

# ===========================================================================================================================
# D1 III. Rechtfertigung (Rn. 95–115)
# ===========================================================================================================================
PIII = "III. Rechtfertigung"
folie([("recht", f"{PIII} · Gemeinwohl und Verhältnismäßigkeit"), ("grundl", f"{PIII} › 1. gesetzliche Grundlage"),
       ("ziel", f"{PIII} › 2. legitimes Ziel: Gesundheitsschutz"), ("geeig", f"{PIII} › 3. geeignet"),
       ("erford", f"{PIII} › 4. erforderlich")], [
    *tafel("recht", "III. Rechtfertigung"),
    z("ausreichende Gründe des Gemeinwohls,", 110, 175, "recht", "Bold", 34),
    z("verhältnismäßig", 110, 221, beim("recht", "verhältnismäßig"), "Bold", 34),
    zit("Rn. 95", 420, 229, beim("recht", "verhältnismäßig")),
    *okz("1. gesetzliche Grundlage: Landesgesetze,", 290, "grundl", "Bold", 33),
    z("die Länder sind zuständig", 185, 336, beim("grundl", "Länder"), "Bold", 33),
    zit("Rn. 96 f.", 640, 344, beim("grundl", "Länder")),
    *okz("2. Ziel: Schutz vor Passivrauchen", 400, "ziel", "Bold", 33),
    blk(185, 450, 965, 80, GRUEN, beim("ziel", "überragend"),
        [("überragend wichtiges Gemeinschaftsgut", "ExtraBold", 33, INK)]),
    zit("Rn. 102", 185, 542, beim("ziel", "überragend")),
    *okz("3. geeignet", 600, "geeig", "Bold", 33),
    zit("Rn. 114", 420, 608, "geeig"),
    *okz("4. erforderlich: freie Wahl Raucher- oder", 660, "erford", "Bold", 33),
    z("Nichtraucherlokal durfte als weniger wirksam gelten", 185, 706, beim("erford", "weniger"), size=32),
    zit("Rn. 115", 185, 752, beim("erford", "weniger")),
    *requisit([("recht", ("tabler", "scale", 120, WEISS), "Rechtfertigung", GELB),
               ("grundl", ("tabler", "book", 110, WEISS), "Landesgesetz", WEISS),
               ("ziel", ("tabler", "lungs", 110, HELLGRUEN), "Gesundheit", HELLGRUEN),
               ("geeig", ("tabler", "smoking-no", 110, WEISS), "geeignet", HELLGRUEN),
               ("erford", ("tabler", "shield-check", 110, HELLGRUEN), "erforderlich", HELLGRUEN)]),
    *paar("AL", [("recht", "ernst"), ("ziel", "denkt")], "SA", [("recht", "ruhig")]),
])

# ===========================================================================================================================
# D2 5. Angemessenheit: striktes Verbot wäre zulässig (Rn. 121–125)
# ===========================================================================================================================
folie([("strikt", f"{PIII} › 5. Angemessenheit: striktes Verbot zulässig"), ("eck", f"{PIII} › 5. auch für Eckkneipen")], [
    *tafel("strikt", "5. Angemessenheit"),
    blk(110, 180, 1040, 130, GRUEN, "strikt", [("striktes Rauchverbot ohne Ausnahmen:", "ExtraBold", 34, INK),
                                            ("verfassungsrechtlich zulässig", "ExtraBold", 34, INK)]),
    zit("Rn. 121 f.", 110, 322, "strikt"),
    *okz("auch für Eckkneipen", 390, "eck", "Bold", 36),
    zit("Rn. 123, 125", 185, 440, "eck"),
    *requisit([("strikt", ("tabler", "smoking-no", 130, WEISS), "ohne Ausnahmen", GRUEN),
               ("eck", ("tabler", "beer", 110, GELB), "auch Eckkneipen", WEISS)]),
    *stehend("AL", FX, [("strikt", "ernst"), ("eck", "sorge")]),
])

# ===========================================================================================================================
# E1 Das gewählte Konzept: Ausnahmen (Rn. 128–134)
# ===========================================================================================================================
PA = f"{PIII} › 5. Angemessenheit"
folie([("aber", f"{PA} · das gewählte Konzept"), ("ausn", f"{PA} · Ausnahmen: Raucherräume, Zelte"),
       ("vermind", f"{PA} · verminderte Intensität")], [
    *tafel("aber", "5. Das gewählte Konzept"),
    z("Baden-Württemberg und Berlin:", 110, 180, "aber", "Bold", 36),
    *okz("Raucherräume erlaubt", 250, "ausn", "Bold", 34),
    *okz("BW: Bier-, Wein- und Festzelte ausgenommen", 310, beim("ausn", "Bier"), "Bold", 34),
    zit("Rn. 131", 185, 360, beim("ausn", "Bier")),
    blk(110, 430, 1040, 130, GELB, "vermind", [("Gesundheitsschutz mit", "ExtraBold", 34, INK),
                                            ("„verminderter Intensität“", "ExtraBold", 34, INK)]),
    zit("Rn. 131, 134", 110, 572, "vermind"),
    *requisit([("aber", ("tabler", "map", 110, WEISS), "BW und Berlin", WEISS),
               ("ausn", ("tabler", "door", 110, HOLZ), "Raucherraum", WEISS),
               (beim("ausn", "Bier"), ("tabler", "tent", 120, GELB), "Festzelte", GELB),
               ("vermind", ("tabler", "trending-down", 110, None), "weniger streng", GELB)]),
    *stehend("AL", FX, [("aber", "ruhig"), ("vermind", "denkt")]),
])


# ===========================================================================================================================
# E2 Folgerichtigkeit (Rn. 135–147)
# ===========================================================================================================================
def minilokal(cue, wander, bis=None):
    """Rechts: kleine Kneipe und großes Lokal mit Raucherraum; Stammgäste wandern ab (Pfeil)."""
    els = [ficon("tabler", "building-store", 1360, 700, 150, cue, fuell=ORANGE, bis=bis),
           pl("kleine Kneipe", 1360, 722, cue, fill=ORANGE, size=28, anker="m", bis=bis),
           ficon("tabler", "building-store", 1720, 700, 250, cue, fuell=GELB, bis=bis),
           pl("großes Lokal", 1720, 722, cue, fill=GELB, size=28, anker="m", bis=bis),
           pl("mit Raucherraum", 1720, 790, cue, fill=WEISS, size=28, anker="m", bis=bis),
           ficon("tabler", "users", 1540, 380, 110, wander, fuell=BLAU, bis=bis),
           pl("Stammgäste", 1540, 210, wander, fill=BLAU, size=28, anker="m", bis=bis),
           pfeil(1370, 420, 1700, 420, wander, breite=10, kopf=30)]
    return rechts_frei(els)


folie([("folge", f"{PA} › Folgerichtigkeit"), ("gewicht", f"{PA} › Belastung der Kleinen wiegt stärker"),
       ("wander", f"{PA} › Stammgäste wandern ab"), ("schaerfer", f"{PA} › Ausnahme verschärft die Lage"),
       ("wenig", f"{PA} › wenig Gewinn für den Nichtraucherschutz")], [
    *tafel("folge", "Folgerichtigkeit"),
    blk(110, 172, 1040, 130, GELB, "folge", [("„… so muss er diese Entscheidung", "ExtraBold", 34, INK),
                                          ("auch folgerichtig weiterverfolgen.“", "ExtraBold", 34, INK)]),
    zit("Rn. 135", 110, 314, "folge"),
    *okz("Belastung der kleinen Kneipen wiegt stärker", 370, "gewicht", "Bold", 33),
    zit("Rn. 136", 185, 418, "gewicht"),
    *okz("große Lokale halten ihre Raucher,", 475, "wander", "Bold", 33),
    z("die Einraumkneipe verliert Stammgäste", 185, 521, beim("wander", "Einraumkneipe"), "Bold", 33),
    zit("Rn. 140, 144", 185, 569, beim("wander", "Einraumkneipe")),
    blk(110, 620, 1040, 80, HELLROT, "schaerfer", [("Die Ausnahme verschärft ihre Lage.", "ExtraBold", 33, INK)]),
    zit("Rn. 145", 110, 712, "schaerfer"),
    *okz("Nichtraucherschutz: dort wenig gewonnen", 765, "wenig", "Bold", 33),
    zit("Rn. 147", 185, 813, "wenig"),
    *requisit([("folge", ("tabler", "route", 120, WEISS), "folgerichtig", GELB)], bis="gewicht"),
    *minilokal("gewicht", "wander"),
])

# ===========================================================================================================================
# E3 Ergebnis zu Art. 12 (Rn. 116, 142–147)
# ===========================================================================================================================
folie([("unzu", f"{PA} · unzumutbar für kleine Einraumkneipen")], [
    *tafel("unzu", "Ergebnis zu Art. 12 Abs. 1 GG"),
    blk(110, 190, 1040, 130, HELLROT, "unzu", [("unzumutbar für kleine Einraumkneipen", "ExtraBold", 34, INK),
                                            ("mit getränkegeprägtem Angebot", "ExtraBold", 34, INK)]),
    zit("Rn. 116, 142, 144", 110, 332, "unzu"),
    *plusminus("verhältnismäßig im engeren Sinne", 110, 410, beim("unzu", "verhältnismäßig"), False, size=36,
               stil="Bold"),
    zit("Art. 12 Abs. 1 GG verletzt (Rn. 90)", 110, 470, beim("unzu", "verhältnismäßig")),
    *requisit([("unzu", ("tabler", "beer", 120, GELB), "Einraumkneipe", ORANGE)]),
    *stehend("AL", FX, [("unzu", "ruhig"), (beim("unzu", "verhältnismäßig"), "froh")]),
])

# ===========================================================================================================================
# F1 IV. Gleichheit: Wortlautkarte Art. 3 Abs. 1 GG; Diskothek (Tenor Nr. 1, 2; Rn. 90, 148–153)
# ===========================================================================================================================
PIV = "IV. Gleichheit, Art. 3 Abs. 1 GG"
w3, w3_y = wortlaut(80, 170, 1100, "„(1) Alle Menschen sind vor dem Gesetz gleich.“", "Art. 3 Abs. 1 GG", "a3",
                    marken=[("gleich", beim("a3", "gleich"))])
folie([("a3", f"{PIV} · Wortlaut"), ("nur12", f"{PIV} › Kneipen: allein Art. 12"),
       ("disko3", f"{PIV} › Diskothek: Ausnahme vorenthalten"), ("begue", f"{PIV} › Begünstigungsausschluss"),
       ("streng", f"{PIV} › strenger Maßstab")], [
    *tafel("a3", "IV. Und die Gleichheit?"),
    *w3,
    z("Kneipen: Ergebnis allein aus Art. 12 Abs. 1 GG", 110, w3_y + 40, "nur12", "Bold", 33),
    zit("Tenor Nr. 1; Rn. 90", 110, w3_y + 88, "nur12"),
    *okz("Diskothek: Ausnahme vorenthalten, die anderen", w3_y + 150, "disko3", "Bold", 33),
    z("Gaststätten offensteht", 185, w3_y + 196, beim("disko3", "die"), "Bold", 33),
    zit("Rn. 148, 152", 600, w3_y + 204, beim("disko3", "die")),
    blk(110, w3_y + 260, 1040, 80, LILA, "begue", [("gleichheitswidriger Begünstigungsausschluss", "ExtraBold", 33, INK)]),
    zit("Rn. 151 f.", 110, w3_y + 352, "begue"),
    *okz("strenger Maßstab: trifft die Berufsfreiheit", w3_y + 410, "streng", "Bold", 33),
    zit("Rn. 150, 153", 185, w3_y + 458, "streng"),
    *requisit([("a3", ("tabler", "scale", 120, WEISS), "Art. 3 Abs. 1 GG", LILA),
               ("nur12", ("tabler", "beer", 110, GELB), "Kneipen: Art. 12", WEISS),
               ("disko3", ("tabler", "music", 110, LILA), "Diskothek", PINK)]),
    *stehend("KA", FX, [("a3", "ruhig"), ("disko3", "ernst"), ("streng", "denkt")]),
])

# ===========================================================================================================================
# F2 Diskothek: keine Rechtfertigung (Rn. 154–160; Tenor Nr. 2)
# ===========================================================================================================================
folie([("jugend", f"{PIV} › Jugendschutz trägt nicht"), ("tanz", f"{PIV} › milderes Mittel: ohne Tanzfläche"),
       ("a123", f"{PIV} › Art. 12 Abs. 1 i. V. m. Art. 3 Abs. 1 GG verletzt")], [
    *tafel("jugend", "Diskothek: gerechtfertigt?"),
    *neinz("Jugendschutz: Verbot nur, wo Minderjährige", 180, "jugend", "Bold", 33, kreuz=beim("jugend", "nicht")),
    z("Zutritt haben, genügt", 185, 226, beim("jugend", "genügt"), "Bold", 33),
    zit("Rn. 159", 560, 234, beim("jugend", "genügt")),
    *neinz("Nachahmeffekte: milderes Mittel genügt,", 300, "tanz", "Bold", 33, kreuz=beim("tanz", "genügt")),
    z("etwa Raucherraum ohne Tanzfläche", 185, 346, beim("tanz", "etwa"), "Bold", 33),
    zit("Rn. 158, 160", 760, 354, beim("tanz", "etwa")),
    blk(110, 430, 1040, 130, HELLROT, "a123", [("unvereinbar mit Art. 12 Abs. 1", "ExtraBold", 34, INK),
                                            ("i. V. m. Art. 3 Abs. 1 GG", "ExtraBold", 34, INK)]),
    zit("Tenor Nr. 2; Rn. 148", 110, 572, "a123"),
    *requisit([("jugend", ("tabler", "shield-check", 110, GELB), "Zutritt ab 18", GELB),
               ("tanz", ("tabler", "music", 110, LILA), "ohne Tanzfläche", WEISS),
               ("a123", ("tabler", "scale", 120, HELLROT), "gleichheitswidrig", HELLROT)]),
    *stehend("KA", FX, [("jugend", "ruhig"), ("a123", "froh")]),
])

# ===========================================================================================================================
# G1 Tenor (Tenor Nr. 1, 2; Rn. 161–164)
# ===========================================================================================================================
folie([("tenor", "Ergebnis · unvereinbar, nicht nichtig"), ("frist", "Ergebnis · Neuregelung bis 31.12.2009"),
       ("weg1", "Ergebnis › Weg 1: striktes Verbot"), ("weg2", "Ergebnis › Weg 2: folgerichtige Ausnahmen")], [
    *tafel("tenor", "Ergebnis: der Tenor"),
    blk(110, 180, 1040, 80, HELLROT, "tenor", [("mit dem Grundgesetz unvereinbar", "ExtraBold", 34, INK)]),
    *neinz("nichtig", 290, beim("tenor", "nicht"), "Bold", 34, kreuz=beim("tenor", "nicht")),
    zit("Tenor Nr. 1, 2; Rn. 161", 340, 298, beim("tenor", "nicht")),
    z("Neuregelung bis 31.12.2009", 110, 380, "frist", "ExtraBold", 36),
    zit("Rn. 162", 640, 390, "frist"),
    blk(110, 450, 1040, 80, GRUEN, "weg1", [("Weg 1: striktes Verbot ohne Ausnahmen", "ExtraBold", 33, INK)]),
    blk(110, 560, 1040, 130, GELB, "weg2", [("Weg 2: Ausnahmen, die folgerichtig", "ExtraBold", 33, INK),
                                         ("auch die kleinen Kneipen erfassen", "ExtraBold", 33, INK)]),
    zit("Rn. 163 f.", 110, 702, "weg2"),
    *requisit([("tenor", ("tabler", "building-bank", 130, HELLROT), "unvereinbar", HELLROT),
               ("frist", ("tabler", "calendar", 110, WEISS), "bis 31.12.2009", WEISS),
               ("weg1", ("tabler", "smoking-no", 110, WEISS), "Weg 1", GRUEN),
               ("weg2", ("tabler", "beer", 110, GELB), "Weg 2", GELB)]),
    *paar("AL", [("tenor", "ruhig")], "KA", [("tenor", "ruhig")]),
])

# ===========================================================================================================================
# G2 Übergangsregelung des Gerichts (Rn. 166–169)
# ===========================================================================================================================
folie([("zwischen", "Übergangsregelung · Verbot bleibt anwendbar"), ("ue1", "Übergangsregelung › Einraumkneipen unter 75 m²"),
       ("ue2", "Übergangsregelung › ab 18 und gekennzeichnet"), ("ue3", "Übergangsregelung › Diskotheken ab 18")], [
    *tafel("zwischen", "Übergangsregelung"),
    z("Verbot bis zur Neuregelung anwendbar", 110, 175, "zwischen", "Bold", 34),
    zit("Rn. 166 f.", 760, 183, "zwischen"),
    *okz("Einraumkneipe, Gastfläche unter 75 m²,", 250, "ue1", "Bold", 33),
    z("keine zubereiteten Speisen: Rauchen erlaubt,", 185, 296, beim("ue1", "zubereitete"), "Bold", 33),
    *okz("wenn kein Zutritt unter 18 und", 360, "ue2", "Bold", 33),
    z("als Rauchergaststätte gekennzeichnet", 185, 406, beim("ue2", "Rauchergaststätte"), "Bold", 33),
    zit("Rn. 167 f.", 185, 454, beim("ue2", "Rauchergaststätte")),
    blk(110, 520, 1040, 130, LILA, "ue3", [("Diskotheken nur ab 18: Raucherraum", "ExtraBold", 33, INK),
                                        ("ohne Tanzfläche", "ExtraBold", 33, INK)]),
    zit("Rn. 169", 110, 662, "ue3"),
    *requisit([("zwischen", ("tabler", "hourglass", 100, GELB), "bis dahin", GELB),
               ("ue1", ("tabler", "ruler", 120, WEISS), "unter 75 m²", ORANGE),
               ("ue2", ("tabler", "shield-check", 110, GELB), "ab 18", GELB),
               ("ue3", ("tabler", "music", 110, LILA), "Diskothek ab 18", LILA)]),
    *stehend("AL", FX, [("zwischen", "ruhig"), ("ue1", "froh"), ("ue3", "ruhig")]),
])

# ===========================================================================================================================
# H Zurück zu Alfons (Schauplatz A1: die Geschichte kehrt zum Ausgangsfall zurück); heute
# ===========================================================================================================================
folie([("alfons", "Zurück zu Alfons · die Übergangszeit"), ("alf2", "Zurück zu Alfons › er wählt selbst"),
       ("heute", "Heute · jedes Land regelt selbst")], [
    *strasse("alfons", raucherraum="alfons"),
    *fig("AL", ALX, BODEN, FH, [("alfons", "ruhig_r"), (beim("alf2", "wählen"), "froh_r")], erst="cut"),
    hart(ns(NAME["AL"], ALX, BODEN, "alfons", ORANGE)),
    pl("Übergangszeit: Alfons wählt selbst", 70, 40, "alf2", fill=ORANGE, size=32),
    pl("keine zubereiteten Speisen", 70, 108, beim("alf2", "zubereiteten"), fill=WEISS, size=30),
    pl("kein Zutritt unter 18", 70, 172, beim("alf2", "Minderjährige"), fill=WEISS, size=30),
    pl("Hinweis an der Tür", 70, 236, beim("alf2", "Tür"), fill=WEISS, size=30),
    pl("ab 18", 70 + KN_TUER + 61, 700, beim("alf2", "Tür"), fill=GELB, size=28, anker="m"),
    pl("Heute: jedes Land regelt selbst – Maßstab: BVerfGE 121, 317", 70, 300, "heute", fill=GELB, size=30),
])

# ===========================================================================================================================
# I Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Folgerichtigkeit in der Angemessenheit"), ("tipp2", "Klausurtipp · Wie streng ist das Konzept?"),
       ("tipp3", "Klausurtipp · Gleichheit gesondert prüfen")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("1. Folgerichtigkeit in der Angemessenheit", 200, 200, "tipp", "Bold", 35),
    z("prüfen, wie das Gericht", 200, 250, beim("tipp", "wie"), "Bold", 35),
    zit("Rn. 116, 128–147", 600, 260, beim("tipp", "wie")),
    linienzug([(130, 330), (1130, 330)], "tipp2", breite=3),
    z("2. Wie streng verfolgt der Gesetzgeber", 200, 360, "tipp2", "Bold", 34),
    z("sein Ziel selbst?", 200, 408, beim("tipp2", "sein"), "Bold", 34),
    z("Ausnahmen zugelassen: Lasten derer wiegen", 200, 470, beim("tipp2", "Lässt"), size=34),
    z("schwerer, die von ihnen nichts haben", 200, 518, beim("tipp2", "schwerer"), size=34),
    zit("Rn. 136, 144", 200, 566, beim("tipp2", "schwerer")),
    blk(130, 620, 1000, 130, GELB, "tipp3", [("3. Gleichheitssatz gesondert prüfen, wenn", "ExtraBold", 33, INK),
                                          ("eine Ausnahme vorenthalten wird", "ExtraBold", 33, INK)]),
    zit("Rn. 149", 200, 762, "tipp3"),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# J Prüfschema
# ===========================================================================================================================
REIHEN = [("k1", 0, 130, "I. Schutzbereich: Berufsfreiheit, Art. 12 Abs. 1 GG", True),
          ("k2", 0, 130, "II. Eingriff: Berufsausübungsregelung", True),
          ("k3", 0, 130, "III. Rechtfertigung", True),
          (beim("k3", "gesetzlicher"), 1, 200, "1. gesetzliche Grundlage", False),
          ("k4", 1, 200, "2. legitimes Ziel", False),
          (beim("k4", "Eignung"), 1, 200, "3. Eignung", False),
          (beim("k4", "Erforderlichkeit"), 1, 200, "4. Erforderlichkeit", False),
          ("k5", 1, 200, "5. Angemessenheit, samt Folgerichtigkeit", False),
          ("k6", 0, 130, "IV. Gleichheitssatz, wenn eine Ausnahme vorenthalten wird", True)]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Prüfschema: Rauchverbot"), 110, 90, "sch", 46)]
y = 190
for c, ebene, x, text, fett in REIHEN:
    if text.startswith(("3. ", "4. ")):
        xx = {"3. Eignung": 620, "4. Erforderlichkeit": 900}[text]
        els_sch.append(z(text, xx, y_zeile2, c, "Regular", 38, rechts=1800))
        continue
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 42 if ebene == 0 else 38, rechts=1800))
    if text.startswith("2. "):
        y_zeile2 = y
    y += {0: 92, 1: 80}[ebene]
assert y <= 970, y
folie([("sch", "Prüfschema"), ("k1", "Prüfschema › I. Schutzbereich"), ("k2", "Prüfschema › II. Eingriff"),
       ("k3", "Prüfschema › III. Rechtfertigung"), ("k5", "Prüfschema › III. 5. Angemessenheit"),
       ("k6", "Prüfschema › IV. Gleichheitssatz")], els_sch)

# ===========================================================================================================================
# K Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Ein ", 0), ("striktes", "a"), (" Rauchverbot", 0)], [("darf der Gesetzgeber wählen.", 0)]],
                750, 290, 44, "merke", {"a": beim("merke", "striktes")}),
    *markertext([[("Lässt er Ausnahmen zu, muss er sie", 0)], [("folgerichtig", "b"), (" gestalten, sonst trifft", 0)],
                 [("die Last ", 0), ("unzumutbar", "c"), (" die kleinen", 0)], [("Betriebe, die von der Ausnahme", 0)],
                 [("nichts haben.", 0)]], 750, 470, 44, "m2",
                {"b": beim("m2", "folgerichtig"), "c": beim("m2", "unzumutbar")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
