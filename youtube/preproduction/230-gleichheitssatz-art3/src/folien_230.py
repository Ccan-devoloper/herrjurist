"""Folge 230 · Gleichheitssatz Art. 3 I GG: Willkürformel und Neue Formel – Serienstandard Open Peeps (Katzenkönig).
Fiktiver Fall, der dem echten Fall BVerfG (K), Beschl. v. 19.7.2016 – 2 BvR 470/08 folgt: Ein Freizeitbad einer kleinen
Gemeinde (Betreiberin: Gesellschaft, die ganz der Gemeinde gehört) verlangt von Einheimischen 6 €, von allen anderen 9 €.
Herr Kühnel an der Kasse, Frau Dittmer (Einwohnerin), Martha (Nachbarort). Danach Wortlautkarten Art. 3 Abs. 1 und Art. 1
Abs. 3 GG, zwei Prüfschritte, Ungleichbehandlung (Vergleichsgruppen, Oberbegriff, derselbe Träger), Maßstab
(Willkürformel BVerfGE 1, 14; Neue Formel BVerfGE 55, 72; stufenlos BVerfGE 88, 87; 138, 136), der Wohnort als Grund
(Rn. 38–40), der echte Fall (Rn. 2–4, 24, 35 f., 41–43, Tenor), zurück zu Martha, Klausurtipp, Schema, Merksatz.
Szenen laut ../SZENENPLAN.md. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/requisit/stehend/paar/
fassade als eigene Kopie aus Folge 208 (gemeinsame Dateien unverändert); neu: preistafel(), kasse(), tresen(), regler(),
zeiger(). Handlungsgeräusche: Kassendrucker (Eintrittskarte) und Schritte (Frau Dittmer geht zum Becken);
../geraeusche_herkunft.json. Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut nach gesetze-im-internet.de (GG),
Abruf 07.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_230/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_230/" in n:
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 160/203/208) -------------------------------------
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




# ===========================================================================================================================
# eigene Bausteine Folge 230: Kasse des Freizeitbads, Preistafel, Regler für den stufenlosen Maßstab
# ===========================================================================================================================
KUX, DIX, MAX0 = 990, 1440, 1760            # Kasse (Herr Kühnel), Frau Dittmer, Martha in der Warteschlange
TUER = 1190                                  # Tür zum Becken hinter der Kasse (absolut, links)
TUERM = TUER + 55                            # Mitte der Tür (Ziel des Weges von Frau Dittmer)


def tuer_offen(cue, bis):
    """Offene Tür zum Becken (dunkle Öffnung), solange Frau Dittmer hindurchgeht."""
    return El(_feld(110, 230, INK, 5, 2), TUER - 6, BODEN - 230 - 6, cue, "cut", 0.0, bis, name="tuer_offen")


def preistafel(cue, sechs, neun):
    """Preistafel an der Fassade: Rahmen ab cue, Preise zum gesprochenen Wort (Ziffern)."""
    return [feld(110, 400, 390, 200, cue, fill=WEISS, rand=5, name="preistafel"),
            hart(z("Eintritt", 135, 412, cue, "ExtraBold", 34, rechts=490)),
            z("wer im Ort wohnt: 6 €", 135, 470, sechs, "Bold", 30, rechts=490),
            z("alle anderen: 9 €", 135, 530, neun, "Bold", 30, rechts=490)]


def kasse(cue):
    """Eingangshalle des Freizeitbads: Fassade mit Tür zum Becken und Fenster, Kassentresen mit Kasse."""
    return [boden(cue),
            fassade(70, 1320, 300, cue, "Freizeitbad", "pool", fenster=[(720, 300, [("tabler", "pool", 110, BLAU)])],
                    tuer_x=TUER - 70, name="bad")]


def tresen(cue):
    return [feld(840, 650, 330, 210, cue, fill=HOLZ, rand=5, name="tresen"),
            hart(ficon("tabler", "cash-register", 1090, 652, 104, cue, fuell=WEISS))]


_RG = {}


def regler(x, y, w, h, cue):
    """Stufenloser Maßstab als Band von Grün (Willkürverbot) über Gelb nach Rot (strenge Verhältnismäßigkeit)."""
    s = 2
    im = Image.new("RGBA", ((w + 12) * s, (h + 12) * s))
    a = np.zeros((h * s, w * s, 4), np.uint8)
    farben = [np.array(GRUEN[:3]), np.array(GELB[:3]), np.array(ROT[:3])]
    for i in range(w * s):
        p = i / (w * s - 1) * 2
        k = min(1, int(p)); f = p - k
        a[:, i, :3] = (farben[k] * (1 - f) + farben[k + 1] * f).astype(np.uint8)
    a[..., 3] = 255
    band = Image.fromarray(a, "RGBA")
    maske = Image.new("L", band.size, 0)
    ImageDraw.Draw(maske).rounded_rectangle((0, 0, band.width - 1, band.height - 1), 18 * s, fill=255)
    im.paste(band, (6 * s, 6 * s), maske)
    ImageDraw.Draw(im).rounded_rectangle((6 * s, 6 * s, (6 + w) * s, (6 + h) * s), 18 * s, outline=INK, width=5 * s)
    im = im.resize((w + 12, h + 12), Image.LANCZOS)
    return El(im, x - 6, y - 6, cue, "fade", 0.0, None, name="regler")


def zeiger(x, y, cue, bis=None):
    """Dreieckiger Zeiger über dem Band (Spitze bei x, y)."""
    s = 2
    im = Image.new("RGBA", (60 * s, 56 * s))
    ImageDraw.Draw(im).polygon([(4 * s, 4 * s), (56 * s, 4 * s), (30 * s, 52 * s)], fill=INK)
    im = im.resize((60, 56), Image.LANCZOS)
    return El(im, x - 30, y - 56, cue, "cut", 0.0, bis, name="zeiger")


NAME = {"KU": "Herr Kühnel", "DI": "Frau Dittmer", "MA": "Martha"}
NFARBE = {"KU": TUERKIS, "DI": LILA, "MA": GRUEN}

# ===========================================================================================================================
# A1 Fall: an der Kasse des Freizeitbads (fiktiv, folgt 2 BvR 470/08 Rn. 2, 42 f.)
# ===========================================================================================================================
WEG_DI = (("mar", 0.5), ("mar", 1.9))        # Frau Dittmer geht durch die Tür zum Becken
WEG_MA = (("mar", 2.8), ("mar", 4.2))        # Martha rückt zur Kasse auf
TICKET = ("mar", -0.25)                      # Eintrittskarte kommt aus der Kasse

folie([(NULL, "Fall · An der Kasse des Freizeitbads"), ("gmbh", "Fall · Betreiberin: Gesellschaft der Gemeinde"),
       ("kas1", "Fall · Einwohner 6 €, alle anderen 9 €"), ("dit", "Fall · Frau Dittmer wohnt im Ort"),
       ("mar", "Fall · Martha wohnt im Nachbarort"), ("ma1", "Fall · Ist das gerecht?")], [
    *kasse(NULL),
    *preistafel(NULL, beim("kas1", "sechs"), beim("kas1", "neun")),
    tuer_offen(("mar", 1.2), WEG_DI[1]),
    # Herr Kühnel hinter dem Tresen (blickt nach rechts zu den Gästen)
    *fig("KU", KUX, BODEN, FH, [(NULL, "ruhig_r")], bis="kas1", erst="cut"),
    *redet("KU_redet_r", KUX, BODEN, FH, "kas1", "dit"),
    *fig("KU", KUX, BODEN, FH, [("dit", "froh_r"), ("ma1", "denkt_r")], erst="cut"),
    *tresen(NULL),
    hart(ns(NAME["KU"], KUX, BODEN, NULL, TUERKIS)),
    hart(pl("Freizeitbad einer kleinen Gemeinde", 70, 40, NULL, fill=TUERKIS, size=32, bis="mar")),
    pl("betrieben von einer Gesellschaft, die ganz der Gemeinde gehört", 70, 108, "gmbh", fill=WEISS, size=28, bis="mar"),
    ficon("tabler", "building-bank", 1440, 300, 120, "gmbh", fuell=WEISS, bis="kas1"),
    pl("wirbt um Urlauber aus der Region · soll Gewinn bringen", 70, 170, "werb", fill=WEISS, size=28, bis="mar"),
    ficon("tabler", "luggage", 1640, 300, 100, "werb", fuell=GELB, bis="kas1"),
    ficon("tabler", "trending-up", 1810, 300, 100, beim("werb", "Gewinn"), bis="kas1"),
    blase("sprech", 760, 190, "kas1", 1400, 195, inhalt=["Wer hier im Ort wohnt, zahlt 6 €.", "Alle anderen zahlen 9 €."],
          textsize=31, figur=("KU_redet_r", KUX, BODEN, FH), bis="dit"),
    # Frau Dittmer zeigt ihren Ausweis, bekommt die Karte und geht zum Becken (Schritte)
    *fig("DI", DIX, BODEN, FH, [("dit", "ruhig")], bis="di1"),
    *redet("DI_redet", DIX, BODEN, FH, "di1", WEG_DI[0]),
    pl("Frau Dittmer wohnt im Ort", 70, 232, "dit", fill=LILA, size=28, bis="mar"),
    ns(NAME["DI"], DIX, BODEN, "dit", LILA, bis=WEG_DI[0]),
    ficon("tabler", "id", 1360, 640, 84, beim("dit", "Ausweis"), fuell=WEISS, bis=TICKET),
    blase("sprech", 640, 190, "di1", 1560, 200, inhalt=["Einmal ermäßigt, bitte.", "Ich wohne gleich um die Ecke."],
          textsize=31, figur=("DI_redet", DIX, BODEN, FH), bis="mar"),
    ring(300, 490, 205, 34, beim("di1", "ermäßigt"), bis="mar"),
    szene(ficon("tabler", "ticket", 930, 652, 78, TICKET, fuell=GELB, bis=WEG_DI[0]), "230kasse*", 0.8, 0.0),
    szene(bewegt(peep_voll("DI_ruhig", TUERM, BODEN, FH, WEG_DI[0], anim="cut", bis=WEG_DI[1]), WEG_DI[0], WEG_DI[1],
                 DIX - TUERM), "230schritte*", 0.9, 0.0),
    bewegt(ns(NAME["DI"], TUERM, BODEN, WEG_DI[0], LILA, bis=WEG_DI[1], anim="cut"), WEG_DI[0], WEG_DI[1], DIX - TUERM),
    # Martha wartet, rückt auf und fragt
    *fig("MA", MAX0, BODEN, FH, [(beim("dit", "Ausweis"), "ruhig")], bis=WEG_MA[0]),
    bis_(ns(NAME["MA"], MAX0, BODEN, beim("dit", "Ausweis"), GRUEN), WEG_MA[0]),
    bewegt(peep_voll("MA_ruhig", DIX, BODEN, FH, WEG_MA[0], anim="cut", bis=beim("mar", "neun")), WEG_MA[0], WEG_MA[1],
           MAX0 - DIX),
    bewegt(ns(NAME["MA"], DIX, BODEN, WEG_MA[0], GRUEN, anim="cut"), WEG_MA[0], WEG_MA[1], MAX0 - DIX),
    peep_voll("MA_sorge", DIX, BODEN, FH, beim("mar", "neun"), anim="cut", bis="ma1"),
    *redet("MA_redet", DIX, BODEN, FH, "ma1", "frage"),
    pl("Martha wohnt im Nachbarort", 70, 40, "mar", fill=GRUEN, size=32),
    pl("für dasselbe Becken: 9 €", 70, 108, beim("mar", "neun"), fill=HELLROT, size=30),
    ring(300, 550, 205, 34, beim("mar", "neun")),
    blase("sprech", 700, 240, "ma1", 1580, 190, inhalt=["Gleiches Becken, gleiches Wasser,", "und ich zahle 3 € mehr.",
                                                     "Ist das gerecht?"],
          textsize=31, figur=("MA_redet", DIX, BODEN, FH)),
])

# ===========================================================================================================================
# A2 Die Frage; der echte Fall (2 BvR 470/08, Rubrum, Rn. 1 f.)
# ===========================================================================================================================
folie([("frage", "Die Frage · Einheimische beim Eintritt bevorzugen?"), ("echt", "Die Frage · BVerfG, 2 BvR 470/08"),
       ("drittel", "Die Frage · Rabatt rund ein Drittel")], [
    *tafel("frage", "Die Frage"),
    z("Darf das Bad der Gemeinde Einheimische", 110, 180, "frage", "Bold", 36),
    z("beim Eintritt bevorzugen?", 110, 232, "frage", "Bold", 36),
    blk(110, 320, 1040, 130, GELB, "echt", [("Unser Fall folgt: BVerfG, Beschl. v. 19.7.2016", "ExtraBold", 33, INK),
                                          ("2 BvR 470/08 (3. Kammer des Zweiten Senats)", "Regular", 32, INK)]),
    zit("Freizeitbad; Rn. 1–61", 110, 462, "echt"),
    blk(110, 530, 1040, 80, WEISS, "drittel", [("Einwohnern gewährt: rund ein Drittel Rabatt", "ExtraBold", 33, INK)]),
    zit("Rn. 2 („etwa einem Drittel“)", 110, 622, "drittel"),
    *paar("MA", [("frage", "denkt")], "DI", [("frage", "ruhig")]),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_230(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=38, zeilenabstand=1.30)
        els += e; y += 24
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 10, cue, fill=PINK, size=36))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_230("sv", [
    "Eine kleine Gemeinde lässt ihr Freizeitbad von einer Gesellschaft betreiben, die ganz der Gemeinde gehört. Das Bad "
    "wirbt um Urlauber aus der ganzen Region und soll Gewinn bringen.",
    "An der Kasse gilt: Wer im Ort wohnt, zahlt 6 €, alle anderen zahlen 9 €. Frau Dittmer wohnt im Ort und zahlt mit "
    "Ausweis 6 €. Martha wohnt im Nachbarort und soll für dasselbe Becken 9 € zahlen.",
    "Einen Ausgleich für besondere Lasten der Einwohner gibt es nicht, ebenso keinen Zuschuss aus dem Gemeindehaushalt. "
    "Einen anderen Grund als den Wohnort nennt die Gemeinde nicht.",
], "Verletzt der Einheimischenpreis Martha in Art. 3 Abs. 1 GG?")

# ===========================================================================================================================
# C Maßstab und Bindung: Wortlautkarten Art. 3 Abs. 1 und Art. 1 Abs. 3 GG (2 BvR 470/08 Rn. 25 f., 29, 34)
# ===========================================================================================================================
PV = "Vorfrage"
w3, w3_y = wortlaut(80, 170, 1100, "„(1) Alle Menschen sind vor dem Gesetz gleich.“", "Art. 3 Abs. 1 GG", "a3",
                    marken=[("gleich", beim("a3", "gleich"))])
w13, w13_y = wortlaut(80, w3_y + 30, 1100, "„(3) Die nachfolgenden Grundrechte binden Gesetzgebung, vollziehende Gewalt und "
                      "Rechtsprechung als unmittelbar geltendes Recht.“", "Art. 1 Abs. 3 GG", "a13",
                      marken=[("Gesetzgebung", beim("a13", "Gesetzgebung")), ("vollziehende", beim("a13", "vollziehende")),
                              ("Rechtsprechung", beim("a13", "Rechtsprechung"))])
folie([("a3", f"{PV} · Maßstab: Art. 3 Abs. 1 GG"), ("a13", f"{PV} · Bindung: Art. 1 Abs. 3 GG"),
       ("gbind", f"{PV} · auch die Betreibergesellschaft")], [
    *tafel("a3", "Gleichheitssatz und Bindung"),
    *w3, *w13,
    blk(110, w13_y + 34, 1040, 130, GRUEN, "gbind", [("Unternehmen ganz in öffentlicher Hand:", "ExtraBold", 33, INK),
                                                   ("unmittelbar gebunden, auch privatrechtlich", "ExtraBold", 33, INK)]),
    zit("2 BvR 470/08, Rn. 25, 29, 34", 110, w13_y + 176, "gbind"),
    *requisit([("a3", ("tabler", "scale", 120, WEISS), "Art. 3 Abs. 1 GG", LILA),
               ("a13", ("tabler", "building-bank", 120, WEISS), "Art. 1 Abs. 3 GG", WEISS),
               ("gbind", ("tabler", "pool", 120, BLAU), "Betreibergesellschaft", GRUEN)]),
    *stehend("MA", FX, [("a3", "ruhig"), ("gbind", "denkt")]),
])

# ===========================================================================================================================
# D1 Prüfung in zwei Schritten (BVerfGE 134, 1 Rn. 55–59; 138, 136 Rn. 121)
# ===========================================================================================================================
folie([("zwei", "Prüfung · zwei Schritte"), ("s1", "Prüfung · I. Ungleichbehandlung"), ("s2", "Prüfung · II. Rechtfertigung")], [
    *tafel("zwei", "Prüfung in zwei Schritten"),
    blk(110, 200, 1040, 80, BLAU, "s1", [("I. Ungleichbehandlung von wesentlich Gleichem", "ExtraBold", 34, INK)]),
    pfeil(630, 300, 630, 380, "s2", breite=10, kopf=30),
    blk(110, 400, 1040, 80, GELB, "s2", [("II. Rechtfertigung", "ExtraBold", 34, INK)]),
    zit("vgl. BVerfGE 134, 1 Rn. 55–59", 110, 500, "s2"),
    *paar("DI", [("zwei", "ruhig")], "MA", [("zwei", "ruhig"), ("s2", "denkt")]),
])

# ===========================================================================================================================
# D2 I. Ungleichbehandlung: Vergleichsgruppen, Oberbegriff, derselbe Träger (BVerfGE 134, 1 Rn. 58, 61)
# ===========================================================================================================================
PI = "I. Ungleichbehandlung"
folie([("vgl", f"{PI} › Vergleichsgruppen"), ("ober", f"{PI} › gemeinsamer Oberbegriff"), ("selbe", f"{PI} › derselbe Träger"),
       ("ungl", f"{PI} › 6 € gegen 9 €")], [
    *tafel("vgl", "I. Ungleichbehandlung"),
    *okz("1. Vergleichsgruppen:", 175, "vgl", "Bold", 34),
    z("einheimische und auswärtige Badegäste", 185, 223, beim("vgl", "einheimische"), "Bold", 34),
    blk(110, 300, 1040, 130, BLAU, "ober", [("Oberbegriff: Gäste desselben Bads,", "ExtraBold", 34, INK),
                                          ("die dieselbe Leistung kaufen", "ExtraBold", 34, INK)]),
    zit("vgl. BVerfGE 134, 1 Rn. 58 (vergleichbare Lage)", 110, 442, "ober"),
    *okz("derselbe Träger: das Bad der Gemeinde", 500, "selbe", "Bold", 34),
    zit("vgl. BVerfGE 134, 1 Rn. 61", 185, 548, "selbe"),
    blk(110, 610, 1040, 80, HELLROT, "ungl", [("6 € gegen 9 €: Ungleichbehandlung", "ExtraBold", 34, INK)]),
    ok(140, 650, beim("ungl", "Ungleichbehandlung")),
    *rechts_frei([pl("einheimisch", X1, PY, beim("vgl", "einheimische"), fill=LILA, size=28, anker="m", bis="ungl"),
                  pl("auswärtig", X2, PY, beim("vgl", "auswärtige"), fill=GRUEN, size=28, anker="m", bis="ungl"),
                  ficon("tabler", "pool", 1560, 360, 110, "ober", fuell=BLAU, bis="ungl"),
                  pl("dasselbe Bad", 1560, 240, "ober", fill=WEISS, size=28, anker="m", bis="ungl"),
                  pl("6 €", X1, PY, "ungl", fill=LILA, size=32, anker="m"),
                  pl("9 €", X2, PY, "ungl", fill=HELLROT, size=32, anker="m")]),
    *paar("DI", [("vgl", "ruhig"), ("ungl", "froh")], "MA", [("vgl", "ruhig"), ("ungl", "sorge")]),
])

# ===========================================================================================================================
# E1 II. Rechtfertigung: Wie streng? Willkürformel (BVerfGE 1, 14 <52>)
# ===========================================================================================================================
PII = "II. Rechtfertigung"
ww, ww_y = wortlaut(80, 300, 1100, "„Der Gleichheitssatz ist verletzt, wenn sich ein vernünftiger, sich aus der Natur der Sache "
                    "ergebender oder sonstwie sachlich einleuchtender Grund für die gesetzliche Differenzierung oder "
                    "Gleichbehandlung nicht finden lässt …“", "BVerfGE 1, 14 <52>", "willk",
                    marken=[("vernünftiger", beim("willk", "vernünftiger")), ("einleuchtender", beim("willk", "einleuchtender")),
                            ("nicht", beim("willk", "nicht"))])
folie([("mass", f"{PII} · Wie streng?"), ("willk", f"{PII} › Willkürformel, BVerfGE 1, 14")], [
    *tafel("mass", "II. Rechtfertigung: Wie streng?"),
    z("Wie streng wird die Rechtfertigung geprüft?", 110, 175, "mass", "Bold", 34),
    z("Anfangs: die Willkürformel", 110, 240, "willk", "ExtraBold", 36),
    *ww,
    *requisit([("mass", ("tabler", "scale", 120, WEISS), "Wie streng?", GELB),
               ("willk", ("tabler", "gavel", 110, WEISS), "nur Willkür", HELLGRUEN)]),
    *stehend("KU", FX, [("mass", "ruhig"), ("willk", "denkt")]),
])

# ===========================================================================================================================
# E2 Die Neue Formel (BVerfGE 55, 72 <88>, Beschl. v. 7.10.1980 – 1 BvL 50/79 u. a.)
# ===========================================================================================================================
wn, wn_y = wortlaut(80, 250, 1100, "„… vor allem dann verletzt, wenn eine Gruppe von Normadressaten im Vergleich zu anderen "
                    "Normadressaten anders behandelt wird, obwohl zwischen beiden Gruppen keine Unterschiede von solcher Art "
                    "und solchem Gewicht bestehen, dass sie die ungleiche Behandlung rechtfertigen könnten.“",
                    "BVerfGE 55, 72 <88>", "nf2",
                    marken=[("Gruppe", beim("nf2", "Gruppe")), ("anders", beim("nf2", "anders")),
                            ("Art", beim("nf2", "Art")), ("Gewicht", beim("nf2", "Gewicht"))])
folie([("neu", f"{PII} › Neue Formel, BVerfGE 55, 72"), ("nf2", f"{PII} › Neue Formel: Art und Gewicht der Unterschiede")], [
    *tafel("neu", "1980: die Neue Formel"),
    z("BVerfGE 55, 72 – Beschl. v. 7.10.1980", 110, 175, "neu", "Bold", 34),
    *wn,
    *requisit([("neu", ("tabler", "calendar", 110, WEISS), "1980", WEISS),
               ("nf2", ("tabler", "scale", 120, GELB), "Art und Gewicht", GELB)]),
    *stehend("DI", FX, [("neu", "ruhig"), ("nf2", "denkt")]),
])

# ===========================================================================================================================
# E3 Heute: stufenloser Maßstab (BVerfGE 88, 87 <96>; 138, 136 Rn. 121 f.)
# ===========================================================================================================================
RX0, RW = 140, 980                                  # Regler: links, Breite
folie([("heute", f"{PII} › heute: stufenloser Maßstab"), ("band", f"{PII} › vom Willkürverbot bis zur Verhältnismäßigkeit"),
       ("str1", f"{PII} › strenger: Merkmal der Person"), ("str2", f"{PII} › strenger: nahe an Art. 3 Abs. 3 GG"),
       ("str3", f"{PII} › strenger: Freiheitsrechte betroffen")], [
    *tafel("heute", "Heute: stufenloser Maßstab"),
    regler(RX0, 250, RW, 60, "heute"),
    z("bloßes Willkürverbot", RX0, 330, beim("band", "bloßen"), "Bold", 30),
    z("strenge Verhältnismäßigkeit", RX0 + RW - F("Bold", 30).getlength("strenge Verhältnismäßigkeit"), 330,
      beim("band", "strengen"), "Bold", 30),
    zeiger(RX0 + 40, 244, beim("band", "bloßen"), bis="str1"),
    zeiger(RX0 + int(RW * 0.5), 244, "str1", bis="str2"),
    zeiger(RX0 + int(RW * 0.72), 244, "str2", bis="str3"),
    zeiger(RX0 + RW - 40, 244, "str3"),
    *okz("Merkmal der Person, kaum zu beeinflussen", 420, "str1", "Bold", 33),
    *okz("nahe an den Merkmalen des Art. 3 Abs. 3 GG", 490, "str2", "Bold", 33),
    zit("z. B. Geschlecht, Abstammung, Herkunft, Glauben", 185, 538, "str2"),
    *okz("Ungleichbehandlung trifft Freiheitsrechte", 600, "str3", "Bold", 33),
    zit("BVerfGE 88, 87 <96>; BVerfGE 138, 136 Rn. 121 f.", 110, 680, "str3"),
    *requisit([("heute", ("tabler", "adjustments-horizontal", 120, WEISS), "stufenlos", GELB),
               ("str1", ("tabler", "user", 110, WEISS), "Person", WEISS),
               ("str2", ("tabler", "scale", 120, WEISS), "Art. 3 Abs. 3 GG", LILA),
               ("str3", ("tabler", "lock-open", 110, WEISS), "Freiheitsrechte", HELLROT)]),
    *stehend("MA", FX, [("heute", "ruhig"), ("str1", "denkt")]),
])

# ===========================================================================================================================
# F Der Wohnort als Grund? (2 BvR 470/08 Rn. 38–40)
# ===========================================================================================================================
folie([("wohn", f"{PII} › Wohnort als Grund?"), ("nicht", f"{PII} › Bevorzugung nicht von vornherein verwehrt"),
       ("sachg", f"{PII} › aber Sachgründe nötig"), ("allein", f"{PII} › Wohnsitz allein: kein Grund"),
       ("untr", f"{PII} › Sachgrund untrennbar mit dem Wohnort"), ("ziele", f"{PII} › mögliche Sachgründe")], [
    *tafel("wohn", "Der Wohnort als Grund?"),
    *okz("nicht von vornherein verwehrt, Einwohner", 175, "nicht", "Bold", 33),
    z("zu bevorzugen", 185, 221, beim("nicht", "bevorzugen"), "Bold", 33),
    zit("Rn. 38", 440, 229, beim("nicht", "bevorzugen")),
    z("aber: Sachgründe nötig", 185, 280, "sachg", "ExtraBold", 33),
    *neinz("Wohnsitz allein: kein Grund", 345, "allein", "Bold", 33, kreuz=beim("allein", "kein")),
    zit("Rn. 39", 690, 353, "allein"),
    blk(110, 410, 1040, 130, GELB, "untr", [("Sachgrund, der mit dem Wohnort", "ExtraBold", 33, INK),
                                          ("untrennbar zusammenhängt", "ExtraBold", 33, INK)]),
    z("· knappe Mittel für die eigenen Aufgaben", 140, 565, beim("ziele", "knappe"), size=32),
    z("· Ausgleich für besondere Lasten der Einwohner", 140, 615, beim("ziele", "Ausgleich"), size=32),
    z("· höherer Aufwand durch Auswärtige", 140, 665, beim("ziele", "höherer"), size=32),
    z("· Stärkung der örtlichen Gemeinschaft", 140, 715, beim("ziele", "Stärkung"), size=32),
    zit("Rn. 39 f.", 110, 770, beim("ziele", "Stärkung")),
    *requisit([("wohn", ("tabler", "map-pin", 100, ROT), "Wohnort", WEISS),
               ("nicht", ("tabler", "home", 110, WEISS), "Einwohner", LILA),
               ("untr", ("tabler", "link", 110, None), "untrennbar", GELB),
               (beim("ziele", "knappe"), ("tabler", "wallet", 110, WEISS), "knappe Mittel", WEISS),
               (beim("ziele", "Ausgleich"), ("tabler", "scale", 120, WEISS), "Ausgleich", WEISS),
               (beim("ziele", "höherer"), ("tabler", "users", 110, BLAU), "Aufwand", WEISS),
               (beim("ziele", "Stärkung"), ("tabler", "heart-handshake", 110, PINK), "Gemeinschaft", WEISS)]),
    *stehend("DI", FX, [("wohn", "ruhig"), ("allein", "denkt"), ("ziele", "ruhig")]),
])

# ===========================================================================================================================
# G1 Der echte Fall (2 BvR 470/08 Rn. 2–4, 8, 24, 35 f., 41–43)
# ===========================================================================================================================
PE = "Der echte Fall"
folie([("real", f"{PE} · Klage auf die Differenz"), ("verk", f"{PE} · Grundrechtsbindung verkannt"),
       ("touri", f"{PE} · Ziel: Auswärtige und Gewinn"), ("last", f"{PE} · kein Ausgleich für Lasten"),
       ("haush", f"{PE} · Haushaltsmittel nicht festgestellt")], [
    *tafel("real", "Der echte Fall: 2 BvR 470/08"),
    z("Besucher aus Österreich verlangt die Differenz zurück", 110, 175, "real", "Bold", 32),
    z("Amtsgericht und Oberlandesgericht: ohne Erfolg", 110, 223, beim("real", "Amtsgericht"), size=32),
    zit("Rn. 2–4, 8", 860, 231, beim("real", "Amtsgericht")),
    blk(110, 285, 1040, 80, LILA, "verk", [("verkannt: unmittelbare Grundrechtsbindung", "ExtraBold", 33, INK)]),
    zit("Rn. 24, 35 f.", 110, 377, "verk"),
    *neinz("Ziel: Auswärtige anziehen, Gewinn erzielen –", 430, "touri", "Bold", 32, kreuz=beim("touri", "nicht")),
    z("nicht die örtliche Gemeinschaft fördern", 185, 476, beim("touri", "nicht"), "Bold", 32),
    zit("Rn. 42 f.", 790, 484, beim("touri", "nicht")),
    *neinz("Ausgleich für Lasten: nicht erkennbar", 545, "last", "Bold", 32, kreuz=beim("last", "nicht")),
    z("die meisten Einwohner des Landkreises ohne Rabatt", 185, 591, beim("last", "meisten"), size=32),
    *neinz("Haushaltsmittel: nicht festgestellt", 660, "haush", "Bold", 32, kreuz=beim("haush", "nicht")),
    zit("Rn. 43", 720, 668, "haush"),
    *requisit([("real", ("tabler", "luggage", 110, GELB), "Besucher aus Österreich", WEISS),
               (beim("real", "Amtsgericht"), ("tabler", "building-bank", 120, WEISS), "AG und OLG", WEISS),
               ("verk", ("tabler", "link", 110, None), "Grundrechtsbindung", LILA),
               ("touri", ("tabler", "trending-up", 110, None), "Auswärtige, Gewinn", WEISS),
               ("last", ("tabler", "users", 110, BLAU), "Landkreis", WEISS),
               ("haush", ("tabler", "pig-money", 120, PINK), "Haushaltsmittel?", WEISS)]),
    *stehend("MA", FX, [("real", "ruhig"), ("touri", "denkt")]),
])

# ===========================================================================================================================
# G2 Ergebnis (Tenor; Rn. 24, 43, 60)
# ===========================================================================================================================
folie([("erg", "Ergebnis · Art. 3 Abs. 1 GG verletzt"), ("aufh", "Ergebnis · aufgehoben und zurückverwiesen")], [
    *tafel("erg", "Ergebnis im echten Fall"),
    blk(110, 190, 1040, 130, HELLROT, "erg", [("Art. 3 Abs. 1 GG verletzt", "ExtraBold", 36, INK),
                                            ("nach den bisherigen Feststellungen", "Regular", 33, INK)]),
    zit("Rn. 24, 43", 110, 332, "erg"),
    *okz("Urteile aufgehoben, Sache zurückverwiesen", 400, "aufh", "Bold", 34),
    zit("Tenor; Rn. 60", 185, 450, "aufh"),
    *requisit([("erg", ("tabler", "scale", 120, HELLROT), "Art. 3 Abs. 1 GG", HELLROT),
               ("aufh", ("tabler", "building-bank", 120, WEISS), "zurückverwiesen", WEISS)]),
    *stehend("MA", FX, [("erg", "ruhig"), ("aufh", "froh")]),
])

# ===========================================================================================================================
# H Zurück an der Kasse (Schauplatz A1: die Geschichte kehrt zum Ausgangsfall zurück)
# ===========================================================================================================================
folie([("martha", "Zurück zu Martha · Mehrpreis nicht gerechtfertigt"), ("anders", "Zurück zu Martha · anders mit echtem Sachgrund")], [
    *kasse("martha"),
    *preistafel("martha", "martha", "martha"),
    nein(470, 550, beim("martha", "nicht"), gr=26),
    *fig("KU", KUX, BODEN, FH, [("martha", "denkt_r"), ("anders", "ruhig_r")], erst="cut"),
    *tresen("martha"),
    hart(ns(NAME["KU"], KUX, BODEN, "martha", TUERKIS)),
    *fig("MA", DIX, BODEN, FH, [("martha", "ruhig"), (beim("martha", "nicht"), "froh")], erst="cut"),
    hart(ns(NAME["MA"], DIX, BODEN, "martha", GRUEN)),
    pl("Martha: Mehrpreis nicht gerechtfertigt", 70, 40, beim("martha", "Mehrpreis"), fill=GRUEN, size=32),
    pl("anders, wenn die Gemeinde mit dem Rabatt", 70, 108, "anders", fill=WEISS, size=30),
    pl("tatsächlich einen Sachgrund verfolgt", 70, 170, "anders", fill=WEISS, size=30),
])

# ===========================================================================================================================
# I Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · zuerst das Vergleichspaar"), ("tipp2", "Klausurtipp · typischer Fehler"),
       ("tipp3", "Klausurtipp · dann der Maßstab")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("1. Zuerst das Vergleichspaar bilden", 200, 200, "tipp", "Bold", 35),
    z("und den gemeinsamen Oberbegriff nennen", 200, 250, beim("tipp", "nenne"), "Bold", 35),
    linienzug([(130, 330), (1130, 330)], "tipp2", breite=3),
    z("Typischer Fehler: Wer sofort rechtfertigt, weiß nicht,", 200, 360, "tipp2", size=34),
    z("welche Ungleichbehandlung er", 200, 408, beim("tipp2", "welche"), size=34),
    z("eigentlich rechtfertigen muss.", 200, 456, beim("tipp2", "eigentlich"), size=34),
    blk(130, 540, 1000, 130, GELB, "tipp3", [("2. Danach den Maßstab festlegen,", "ExtraBold", 33, INK),
                                          ("dann die Gründe abwägen", "ExtraBold", 33, INK)]),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# J Prüfschema
# ===========================================================================================================================
REIHEN = [("k1", 0, 130, "I. Ungleichbehandlung von wesentlich Gleichem", True),
          ("k2", 1, 200, "1. Vergleichsgruppen", False),
          (beim("k2", "gemeinsamem"), 1, 200, "2. gemeinsamer Oberbegriff", False),
          (beim("k2", "demselben"), 1, 200, "3. derselbe Träger", False),
          ("k3", 0, 130, "II. Rechtfertigung", True),
          ("k4", 1, 200, "1. Maßstab: vom Willkürverbot bis zur Verhältnismäßigkeit", False),
          ("k5", 1, 200, "2. Sachgrund", False),
          (beim("k5", "bei"), 1, 200, "bei strenger Prüfung: Eignung, Erforderlichkeit, Angemessenheit", False),
          ("k6", 0, 130, "III. Ergebnis", True)]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Prüfschema: Art. 3 Abs. 1 GG"), 110, 90, "sch", 46)]
y = 190
for c, ebene, x, text, fett in REIHEN:
    if text.startswith("bei strenger"):
        x = 250
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 42 if ebene == 0 else 38, rechts=1800))
    y += {0: 86, 1: 74}[ebene]
assert y <= 970, y
folie([("sch", "Prüfschema"), ("k1", "Prüfschema › I. Ungleichbehandlung"), ("k3", "Prüfschema › II. Rechtfertigung"),
       ("k4", "Prüfschema › II. 1. Maßstab"), ("k5", "Prüfschema › II. 2. Sachgrund"), ("k6", "Prüfschema › III. Ergebnis")],
      els_sch)

# ===========================================================================================================================
# K Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Erst ", 0), ("vergleichen", "a"), (", dann rechtfertigen.", 0)]], 750, 290, 44, "merke",
                {"a": beim("merke", "vergleichen")}),
    *markertext([[("Je mehr das Merkmal an die Person", 0)], [("anknüpft und je stärker Freiheit", 0)],
                 [("betroffen ist, desto ", 0), ("strenger", "b"), (" die Prüfung.", 0)]], 750, 410, 44, "m2",
                {"b": beim("m2", "strenger")}),
    *markertext([[("Der ", 0), ("Wohnort allein", "c"), (" rechtfertigt", 0)], [("keinen Rabatt.", 0)]], 750, 650, 44, "m3",
                {"c": beim("m3", "Wohnort")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
