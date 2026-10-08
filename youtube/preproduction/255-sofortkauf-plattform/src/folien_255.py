"""Folge 255 · „Sofort kaufen“ geklickt: Ist der Verkäufer an den Preis gebunden? · Serienstandard Open Peeps (Katzenkönig).
Beispielfall: Herr Eichler stellt am Montagmorgen seine seltene Kamera auf einer (fiktiven) Plattform zum festen Preis von
900 € mit „Sofort kaufen“ ein; nach den Regeln der Plattform kommt der Kauf mit dem Klick zustande. Frau Hegemann klickt
mittags und zahlt. Abends sieht er: Vergleichbare Kameras kosten rund 2.500 €; Modell und Zustand kannte er genau. Am
nächsten Tag ficht er an der Haustür an. Danach: Anspruch § 433 Abs. 1 Satz 1, I. Vertragsschluss (Abgrenzung Folge 251,
Sofort kaufen = Angebot, Auslegung §§ 133, 157 mit Plattformregeln, ad incertas personas; Wortlautkarte § 145; Annahme durch
den Klick), II. Anfechtung (Wortlautkarten § 119 Abs. 1 und Abs. 2; Wert keine Eigenschaft; Motivirrtum, Kalkulationsirrtum;
Risiko beim Verkäufer), Ergebnis, Gegenfall Tippfehler 90 € (Erklärungsirrtum, § 122), Klausurtipp, Schema, Merksatz.
Szenen laut ../SZENENPLAN.md. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/feld als eigene Kopie
aus Folge 251 (gemeinsame Dateien unverändert); neu: handy(), wohnzimmer(), park(), haustuer(), knopf().
Keine echten Plattformen oder Marken: Anzeige, Handy und Kamera aus Grundformen und Tabler-Icons, ohne Namen oder Logo.
Handlungsgeräusch: Türklingel (A4, Frau Hegemann klingelt); ../geraeusche_herkunft.json.
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut nach gesetze-im-internet.de (BGB), Abruf 08.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_255/"

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
LILAHELL = (240, 236, 255, 255)
HELLGRAU = (226, 226, 222, 255)
HOLZ = (214, 160, 110, 255)
DUNKELHOLZ = (150, 98, 66, 255)
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
        if n.startswith(("bild:", "ficon:")) or "/op_255/" in n:
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 160/203/205/229) ---------------------------------
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
NAME = {"EI": "Herr Eichler", "HE": "Frau Hegemann"}
BLAU_P, LILA_P = (141, 179, 242, 255), (184, 169, 245, 255)
NFARBE = {"EI": BLAU_P, "HE": LILA_P}
GRUEN_P = (143, 214, 148, 255)


def _flaeche(w, h):
    s = 2
    im = Image.new("RGBA", ((w + 12) * s, (h + 12) * s))
    return im, ImageDraw.Draw(im), s


def _feld(w, h, fill=WEISS, rand=4, rund=14):
    im, dr, s = _flaeche(w, h)
    o = 6 * s
    dr.rounded_rectangle((o, o, o + w * s, o + h * s), rund * s, fill=fill, outline=INK, width=rand * s)
    return im.resize((w + 12, h + 12), Image.LANCZOS)


def feld(x, y, w, h, cue, fill=WEISS, rand=4, rund=14, bis=None, anim="cut", name="feld"):
    return El(_feld(w, h, fill, rand, rund), x, y, cue, anim, 0.0, bis, name=name)


def boden(cue):
    return hart(linienzug([(40, BODEN), (1880, BODEN)], cue, breite=7, farbe=INK))


def fenster(x, y, w, h, cue, fill=None, bis=None):
    """Fenster mit Sprossen (Tageslicht; abends dunkleres Blau)."""
    return [bis_(hart(feld(x, y, w, h, cue, fill=fill or BLAUHELL, rand=5, rund=8, name="fenster")), bis),
            bis_(hart(feld(x + w // 2 - 4, y + 6, 8, h - 12, cue, fill=INK, rand=1, rund=2, name="sprosse1")), bis),
            bis_(hart(feld(x + 6, y + h // 2 - 4, w - 12, 8, cue, fill=INK, rand=1, rund=2, name="sprosse2")), bis)]


# Handy-Anzeige (Bildschirm-Zoom) aus Grundformen, ohne Plattformnamen oder Logo
HX0, HY0, HX1, HY1 = 200, 100, 720, 840
HM = (HX0 + HX1) // 2


def handy(cue, kopf="Plattform"):
    return [hart(feld(HX0, HY0, HX1 - HX0, HY1 - HY0, cue, fill=INK, rand=4, rund=46, name="handy")),
            hart(feld(HX0 + 22, HY0 + 60, HX1 - HX0 - 44, HY1 - HY0 - 110, cue, fill=WEISS, rand=2, rund=14, name="anzeige")),
            hart(feld(HM - 50, HY0 + 24, 100, 14, cue, fill=HELLGRAU, rand=2, rund=7, name="lautsprecher")),
            hart(feld(HX0 + 22, HY0 + 60, HX1 - HX0 - 44, 70, cue, fill=BLAUHELL, rand=2, rund=14, name="kopfleiste")),
            hart(z(kopf, HX0 + 50, HY0 + 72, cue, "ExtraBold", 32, rechts=HX1 - 30))]


def knopf(text, cx, y, cue, fill=GELB, w=360, h=78, bis=None, size=34, anim="pop"):
    """Schaltfläche in der Anzeige (Rechteck mit Text, Ziffern/Text wie gesprochen)."""
    els = [bis_(feld(cx - w // 2, y, w, h, cue, fill=fill, rand=4, rund=36, anim=anim, name="knopf:" + text), bis)]
    f = F("ExtraBold", size)
    els.append(bis_(z(text, cx - f.getlength(glyphen(text)) / 2, y + (h - size * 1.3) / 2, cue, "ExtraBold", size,
                      rechts=cx + w // 2), bis))
    return els


def anzeige(cue, preis_cue, bis=None):
    """Inhalt der Anzeige: Kamera, fester Preis (Schaltfläche separat)."""
    return [bis_(ficon("tabler", "camera", HM, 420, 230, cue, fuell=HELLGRAU, anim="cut"), bis),
            bis_(hart(z("Kamera", HM - F("Bold", 34).getlength("Kamera") / 2, 430, cue, "Bold", 34, rechts=HX1 - 30)), bis),
            bis_(z("900 €", HM - F("ExtraBold", 70).getlength("900 €") / 2, 486, preis_cue, "ExtraBold", 70, rechts=HX1 - 30), bis)]


# Wohnzimmer bei Herrn Eichler: Handy-Anzeige links, Herr Eichler, Sofa und Stehlampe rechts
EIX = 1000


def wohnzimmer(cue, abend=False):
    els = [boden(cue), *fenster(1180, 130, 230, 210, cue, fill=(120, 140, 200, 255) if abend else None),
           ficon("tabler", "sofa", 1640, BODEN + 6, 360, cue, fuell=(184, 169, 245, 255) if not abend else (160, 148, 220, 255),
                 anim="cut"),
           ficon("tabler", "lamp", 1840, BODEN + 4, 120, cue, fuell=GELB if abend else WEISS, anim="cut")]
    return els


# ===========================================================================================================================
# A1 Fall: Herr Eichler stellt seine Kamera mit „Sofort kaufen“ ein
# ===========================================================================================================================
folie([(NULL, "Fall · Bei Herrn Eichler zu Hause"), ("anzeige", "Fall · Kamera für 900 € mit „Sofort kaufen“"),
       ("regel", "Fall · Regel der Plattform: Klick = Kauf")], [
    *wohnzimmer(NULL),
    *handy(NULL),
    hart(pl("Bei Herrn Eichler zu Hause", 760, 22, NULL, fill=GELB, size=30)),
    *anzeige(NULL, beim("fall", "neunhundert")),
    pl("Wert: 2.500 €?", EIX, 330, beim("fall", "zweitausendfünfhundert"), fill=HELLROT, size=32, anker="m", bis="anzeige"),
    pl("Montagmorgen", 760, 96, "anzeige", fill=WEISS, size=30),
    pl("fester Preis", HM, 590, beim("anzeige", "festen"), fill=WEISS, size=28, anker="m"),
    *knopf("Sofort kaufen", HM, 650, beim("anzeige", "Schaltfläche")),
    blk(1110, 380, 760, 150, WEISS, "regel", [("Regel der Plattform:", "ExtraBold", 32, INK),
                                              ("Klick auf „Sofort kaufen“ = Kauf", "Bold", 32, INK)]),
    *fig("EI", EIX, BODEN, FH, [(NULL, "ruhig"), ("eichler", "sorge"), ("anzeige", "froh"), ("regel", "ruhig")], erst="cut"),
    hart(ns(NAME["EI"], EIX, BODEN, NULL, BLAU_P)),
])


# ===========================================================================================================================
# A2 Am Mittag im Park: Frau Hegemann klickt und zahlt
# ===========================================================================================================================
HEX = 1080


def park(cue):
    return [boden(cue),
            ficon("tabler", "tree", 1740, BODEN + 6, 360, cue, fuell=GRUEN_P, anim="cut"),
            hart(feld(1300, 700, 300, 26, cue, fill=HOLZ, rand=4, rund=8, name="bank_sitz")),
            hart(feld(1300, 640, 300, 22, cue, fill=HOLZ, rand=4, rund=8, name="bank_lehne")),
            hart(feld(1320, 726, 20, BODEN - 730, cue, fill=DUNKELHOLZ, rand=3, rund=4, name="bank_bein1")),
            hart(feld(1560, 726, 20, BODEN - 730, cue, fill=DUNKELHOLZ, rand=3, rund=4, name="bank_bein2"))]


folie([("park", "Fall · Am Mittag: Frau Hegemann sieht die Anzeige"), ("klick", "Fall · Frau Hegemann klickt „Sofort kaufen“"),
       ("zahlt", "Fall · Frau Hegemann zahlt 900 €")], [
    *park("park"),
    *handy("park"),
    hart(pl("Am Mittag im Park", 760, 22, "park", fill=GELB, size=30)),
    *anzeige("park", "park"),
    *knopf("Sofort kaufen", HM, 650, "park", anim="cut", bis=beim("klick", "Sofort")),
    *knopf("gekauft", HM, 650, beim("klick", "Sofort"), fill=GRUEN_P, anim="cut"),
    ficon("tabler", "hand-click", HM + 150, 800, 110, beim("klick", "klickt"), fuell=WEISS),
    pl("bezahlt: 900 €", 1080, 250, beim("zahlt", "bezahlt"), fill=GRUEN_P, size=32, anker="m"),
    ficon("tabler", "coin-euro", 1080, 225, 90, beim("zahlt", "bezahlt"), fuell=GELB),
    *fig("HE", HEX, BODEN, FH, [("park", "ruhig"), ("klick", "froh"), ("zahlt", "strahlt")], erst="pop"),
    ns(NAME["HE"], HEX, BODEN, "park", LILA_P, d=0.1),
])


# ===========================================================================================================================
# A3 Am Abend: Vergleichsangebote um 2.500 €; Modell und Zustand kannte er
# ===========================================================================================================================
folie([("abend", "Fall · Am Abend: andere Angebote"), ("vergleich", "Fall · vergleichbare Kameras: rund 2.500 €"),
       ("modell", "Fall · nur den Marktpreis unterschätzt")], [
    *wohnzimmer("abend", abend=True),
    *handy("abend", kopf="Andere Angebote"),
    hart(pl("Am Abend bei Herrn Eichler", 760, 22, "abend", fill=GELB, size=30)),
    *[x for i, p in enumerate(("2.450 €", "2.500 €", "2.550 €")) for x in (
        feld(HX0 + 50, 200 + i * 150, HX1 - HX0 - 100, 120, beim("abend", "Angebote"), fill=HELL, rand=3, rund=14,
             anim="pop", name=f"angebot{i}"),
        ficon("tabler", "camera", HX0 + 120, 200 + i * 150 + 100, 90, beim("abend", "Angebote"), fuell=HELLGRAU),
        z(p, HX0 + 200, 200 + i * 150 + 30, beim("vergleich", "Kameras"), "ExtraBold", 46, rechts=HX1 - 40))],
    pl("rund 2.500 €", EIX, 330, beim("vergleich", "zweitausendfünfhundert"), fill=HELLROT, size=34, anker="m"),
    feld(1110, 350, 760, 220, "modell", fill=WEISS, rand=4, rund=18, anim="pop", name="checkliste"),
    *okz("Modell: gewusst", 370, beim("modell", "Modell"), "Bold", 32, x=1185, rechts=1860),
    *okz("Zustand: gewusst", 430, beim("modell", "Zustand"), "Bold", 32, x=1185, rechts=1860),
    *neinz("Marktpreis: unterschätzt", 490, beim("modell", "Marktpreis"), "Bold", 32, x=1185, rechts=1860),
    *fig("EI", EIX, BODEN, FH, [("abend", "ruhig"), (beim("vergleich", "zweitausendfünfhundert"), "schreck"),
                               ("modell", "denkt"), (beim("modell", "Nur"), "sorge")], erst="pop"),
    ns(NAME["EI"], EIX, BODEN, "abend", BLAU_P, d=0.1),
])


# ===========================================================================================================================
# A4 Am nächsten Tag an der Haustür: Anfechtung und Verlangen – die Frage
# ===========================================================================================================================
ET, HT = 760, 1380


def haustuer(cue, oben=120):
    return [boden(cue),
            hart(feld(70, oben, 600, BODEN - oben - 4, cue, fill=(253, 240, 214, 255), rand=5, rund=6, name="hauswand")),
            hart(feld(250, 360, 240, BODEN - 364, cue, fill=HOLZ, rand=5, rund=10, name="tuer")),
            hart(feld(445, 600, 22, 22, cue, fill=GELB, rand=3, rund=11, name="tuerknauf")),
            *fenster(110, 400 if oben > 200 else 200, 110, 130, cue),
            hart(feld(520, 520, 40, 56, cue, fill=WEISS, rand=3, rund=8, name="klingel")),
            ficon("tabler", "tree", 1750, BODEN + 6, 240, cue, fuell=GRUEN_P, anim="cut")]


folie([("tuer", "Fall · Am nächsten Tag an der Haustür"), ("e1", "Fall · Herr Eichler: „Ich fechte den Kauf an“"),
       ("h1", "Fall · Frau Hegemann: „Ich will die Kamera“"), ("frage", "Die Frage · An den Preis gebunden?"),
       ("frage2", "Die Frage · Angebot schon verbindlich?"), ("frage3", "Die Frage · Anfechtung wegen des Werts?")], [
    *haustuer("tuer"),
    hart(pl("Am nächsten Tag", 70, 30, "tuer", fill=GELB, size=30, bis="frage")),
    szene(ficon("tabler", "bell-ringing", 540, 500, 56, beim("tuer", "abholen"), fuell=GELB, bis="e1"), "255klingel*", 0.8, 0.05),
    *fig("EI", ET, BODEN, FH, [("tuer", "ernst_r")], bis="e1", erst="pop"),
    *redet("EI_redet_r", ET, BODEN, FH, "e1", "h1"),
    *fig("EI", ET, BODEN, FH, [("h1", "still_r"), ("frage", "denkt_r")], erst="cut"),
    ns(NAME["EI"], ET, BODEN, "tuer", BLAU_P, d=0.1),
    *fig("HE", HT, BODEN, FH, [("tuer", "froh"), ("e1", "sorge")], bis="h1", erst="pop"),
    *redet("HE_redet", HT, BODEN, FH, "h1", "frage"),
    *fig("HE", HT, BODEN, FH, [("frage", "ernst")], erst="cut"),
    ns(NAME["HE"], HT, BODEN, "tuer", LILA_P, d=0.1),
    blase("sprech", 600, 210, "e1", 930, 210, inhalt=["Ich habe den Wert völlig", "unterschätzt. Ich fechte", "den Kauf an."],
          textsize=31, figur=("EI_redet_r", ET, BODEN, FH), bis="frage"),
    blase("sprech", 600, 210, "h1", 1500, 210, inhalt=["Ich habe auf Sofort kaufen", "geklickt und bezahlt.", "Ich will die Kamera."],
          textsize=31, figur=("HE_redet", HT, BODEN, FH), bis="frage"),
    pl("Ist Herr Eichler an seinen Preis gebunden?", 720, 30, "frage", fill=PINK, size=34),
    pl("War sein Angebot schon verbindlich?", 720, 108, "frage2", fill=PINK, size=34),
    pl("Darf er wegen des Werts anfechten?", 720, 186, "frage3", fill=PINK, size=34),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_255(cue, absaetze, frage, size=34):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 205
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=size, zeilenabstand=1.28)
        els += e; y += 14
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_255("sv", [
    "Herr Eichler stellt am Montagmorgen seine seltene Kamera auf einer Plattform ein: fester Preis 900 €, Schaltfläche "
    "„Sofort kaufen“. Nach den Regeln der Plattform kommt der Kauf zustande, sobald jemand darauf klickt.",
    "Am Mittag klickt Frau Hegemann auf „Sofort kaufen“ und zahlt die 900 €.",
    "Am Abend sieht Herr Eichler, dass vergleichbare Kameras rund 2.500 € kosten. Modell und Zustand seiner Kamera kannte er "
    "genau; nur den Marktpreis hat er unterschätzt.",
    "Am nächsten Tag erklärt er Frau Hegemann an der Haustür, er fechte den Kauf an. Sie verlangt die Kamera.",
], "Muss Herr Eichler die Kamera für 900 € liefern?")


# ===========================================================================================================================
# Tafel-Helfer
# ===========================================================================================================================
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


def okw(text, y, cue, haken, stil="Bold", size=34, x=185, **k):
    """Tafelzeile zum Satzbeginn, Haken erst zur gesprochenen Bejahung (haken = Cue)."""
    return [ok(x - 45, y + 20, haken, gr=20), z(text, x, y, cue, stil, size, **k)]


# ===========================================================================================================================
# C Anspruch und Aufbau
# ===========================================================================================================================
PA = "Anspruch"
folie([("ansp", f"{PA} · § 433 Abs. 1 Satz 1 BGB: Übergabe und Übereignung"), ("aufbau", f"{PA} › Stufe 1: Kaufvertrag zu 900 €?"),
       ("aufbau2", f"{PA} › Stufe 2: wirksam angefochten?")], [
    *tafel("ansp", "Anspruch auf die Kamera"),
    z("Frau Hegemann gegen Herrn Eichler", 110, 180, "ansp", "Bold", 36),
    z("Übergabe und Übereignung der Kamera", 110, 245, beim("ansp", "Übergabe"), "Bold", 34),
    z("§ 433 Abs. 1 Satz 1 BGB", 110, 297, beim("ansp", "Paragraf"), "ExtraBold", 36),
    blk(110, 390, 1040, 100, GELB, beim("aufbau", "Ist"), [("Stufe 1: Kaufvertrag zu 900 € zustande gekommen?", "ExtraBold", 32, INK)]),
    blk(110, 530, 1040, 100, HELLROT, "aufbau2", [("Stufe 2: Hat Herr Eichler wirksam angefochten?", "ExtraBold", 32, INK)]),
    *requisit([("ansp", ("tabler", "camera", 150, HELLGRAU), "Kamera", WEISS),
               ("aufbau", ("tabler", "list-check", 120, GELB), "zwei Stufen", GELB)], px=1560, pu=330, py=90),
    *paar("HE", [("ansp", "ruhig"), ("aufbau", "denkt")], "EI", [("ansp", "ruhig"), ("aufbau2", "ernst")]),
])

# ===========================================================================================================================
# D1 I. Vertragsschluss: Angebot durch Einstellen mit „Sofort kaufen“ (VIII ZR 59/16 Rn. 12; VIII ZR 305/10 Rn. 15 f.)
# ===========================================================================================================================
PI = "I. Vertragsschluss"
folie([("ang", f"{PI} · Angebot?"), ("v251", f"{PI} › Abgrenzung: Shopseite nur Einladung"),
       ("sofort", f"{PI} › Sofort kaufen: Angebot zum festen Preis"), ("ausl", f"{PI} › Auslegung, §§ 133, 157 BGB"),
       ("jeder", f"{PI} › Angebot an jeden, der zuerst klickt")], [
    *tafel("ang", "I. Vertragsschluss: das Angebot"),
    blk(110, 175, 1040, 110, LILAHELL, "v251", [("Folge „Preisfehler im Onlineshop“:", "ExtraBold", 31, INK),
                                               ("Shopseite nur Einladung zum Angebot", "Bold", 31, INK)]),
    *okw("„Sofort kaufen“: Angebot zum festen Preis", 315, "sofort", beim("sofort", "bietet"), "Bold", 34),
    zit("BGH, Urt. v. 15.2.2017 – VIII ZR 59/16, Rn. 12", 185, 363, beim("sofort", "Bundesgerichtshof")),
    z("Auslegung nach §§ 133, 157 BGB", 185, 425, beim("ausl", "Auslegung"), "Bold", 34),
    z("mit den Regeln der Plattform", 185, 475, beim("ausl", "Regeln"), "Bold", 34),
    zit("BGH, Urt. v. 8.6.2011 – VIII ZR 305/10, Rn. 15", 185, 523, beim("ausl", "Regeln")),
    z("Kauf mit dem Klick, ohne neue Entscheidung", 185, 590, "jeder", "Bold", 34),
    blk(110, 650, 1040, 120, GELB, beim("jeder", "Sein"), [("Angebot an jeden, der zuerst klickt:", "ExtraBold", 32, INK),
                                                          ("ad incertas personas", "ExtraBold", 32, INK)]),
    *requisit([("ang", ("tabler", "help-circle", 110, WEISS), "Angebot?", WEISS),
               ("v251", ("tabler", "building-store", 120, LILAHELL), "Onlineshop", LILAHELL),
               ("sofort", ("tabler", "camera", 140, HELLGRAU), "900 € fest", GELB),
               ("jeder", ("tabler", "users", 130, WEISS), "an jeden", WEISS)]),
    *stehend("EI", FX, [("ang", "ruhig"), ("sofort", "denkt"), ("jeder", "ernst")]),
])

# ===========================================================================================================================
# D2 § 145 BGB (Wortlautkarte), Bindung ausschließbar (VIII ZR 305/10 Rn. 17)
# ===========================================================================================================================
w145, w145_y = wortlaut(80, 170, 1100, "„Wer einem anderen die Schließung eines Vertrags anträgt, ist an den Antrag gebunden, "
                                       "es sei denn, dass er die Gebundenheit ausgeschlossen hat.“", "§ 145 BGB", "w145",
                        size=34, marken=[("gebunden", beim("w145", "gebunden")),
                                         ("ausgeschlossen", beim("w145", "ausgeschlossen"))])
folie([("w145", f"{PI} › Bindung, § 145 BGB"), ("ausschl", f"{PI} › Bindung ausschließbar"),
       ("nicht", f"{PI} › Herr Eichler: Angebot verbindlich")], [
    *tafel("w145", "Bindung an das Angebot"),
    *w145,
    blk(110, w145_y + 30, 1040, 120, GELB, "ausschl", [("Bindung ausschließen oder einschränken:", "ExtraBold", 32, INK),
                                                     ("zulässig", "ExtraBold", 32, INK)]),
    zit("BGH, Urt. v. 8.6.2011 – VIII ZR 305/10, Rn. 17 (Auktion)", 110, w145_y + 162, beim("ausschl", "Bundesgerichtshof")),
    *neinz("Herr Eichler: nichts dergleichen erklärt", w145_y + 230, "nicht", "Bold", 34, kreuz=beim("nicht", "nichts")),
    *okw("Angebot verbindlich", w145_y + 290, beim("nicht", "Sein"), beim("nicht", "verbindlich"), "ExtraBold", 34),
    *requisit([("w145", ("tabler", "lock", 110, GELB), "gebunden", GELB),
               ("ausschl", ("tabler", "lock-open", 110, WEISS), "ausschließbar", WEISS),
               ("nicht", ("tabler", "lock", 110, GELB), "verbindlich", GELB)]),
    *stehend("EI", FX, [("w145", "ruhig"), ("ausschl", "denkt"), ("nicht", "sorge")]),
])
assert w145_y + 290 + 40 <= 895, w145_y

# ===========================================================================================================================
# D3 Annahme durch den Klick (VIII ZR 59/16 Rn. 23); Verweis Folge 014
# ===========================================================================================================================
folie([("klick2", f"{PI} › Annahme: der Klick"), ("vertrag", f"{PI} › Kaufvertrag zu 900 €"),
       ("v014", f"{PI} › Folge „Angebot und Annahme“")], [
    *tafel("klick2", "I. Vertragsschluss: die Annahme"),
    *okw("Klick auf „Sofort kaufen“: Annahme", 185, "klick2", beim("klick2", "angenommen"), "Bold", 34),
    z("ohne Vorbehalt", 185, 235, beim("klick2", "ohne"), "Bold", 34),
    zit("BGH, Urt. v. 15.2.2017 – VIII ZR 59/16, Rn. 23", 185, 287, beim("klick2", "Bundesgerichtshof")),
    blk(110, 370, 1040, 100, HELLGRUEN, "vertrag", [("Kaufvertrag geschlossen: Kamera für 900 €", "ExtraBold", 34, INK)]),
    blk(110, 520, 1040, 90, LILAHELL, "v014", [("mehr dazu: Folge „Angebot und Annahme“", "ExtraBold", 32, INK)]),
    *requisit([("klick2", ("tabler", "hand-click", 120, WEISS), "Klick", WEISS),
               ("vertrag", ("tabler", "file-text", 120, HELLGRUEN), "Kaufvertrag", HELLGRUEN)]),
    *stehend("HE", FX, [("klick2", "ruhig"), ("vertrag", "strahlt"), ("v014", "froh")]),
])

# ===========================================================================================================================
# E II. Anfechtung: Erklärung (§ 143), § 119 Abs. 1 BGB (Wortlautkarte); Wille = Erklärung
# ===========================================================================================================================
PII = "II. Anfechtung"
w119, w119_y = wortlaut(80, 312, 1100, "„(1) Wer bei der Abgabe einer Willenserklärung über deren Inhalt im Irrtum war oder "
                                       "eine Erklärung dieses Inhalts überhaupt nicht abgeben wollte, kann die Erklärung "
                                       "anfechten, wenn anzunehmen ist, dass er sie bei Kenntnis der Sachlage und bei "
                                       "verständiger Würdigung des Falles nicht abgegeben haben würde.“", "§ 119 Abs. 1 BGB",
                        "w119", size=30,
                        marken=[("über deren Inhalt", beim("w119", "Inhalt")), ("überhaupt nicht abgeben", beim("w119", "überhaupt"))])
folie([("anf", f"{PII} · Erklärung gegenüber Frau Hegemann"), ("w119", f"{PII} › Anfechtungsgrund: § 119 Abs. 1 BGB"),
       ("wollte", f"{PII} › gewollt 900 €, erklärt 900 €"), ("kein1", f"{PII} › kein Inhalts-, kein Erklärungsirrtum")], [
    *tafel("anf", "II. Anfechtung"),
    *okz("Anfechtungserklärung gegenüber Frau Hegemann", 168, beim("anf", "Erklärt"), "Bold", 33),
    zit("§ 143 Abs. 1, 2 BGB", 185, 212, beim("anf", "Erklärt")),
    z("Anfechtungsgrund?", 110, 258, beim("anf", "Anfechtungsgrund"), "ExtraBold", 34, rechts=1170),
    *w119,
    blk(110, w119_y + 18, 1040, 80, WEISS, "wollte", [("gewollt: 900 €   =   erklärt: 900 €", "ExtraBold", 34, INK)]),
    *neinz("kein Inhaltsirrtum, kein Erklärungsirrtum", w119_y + 124, "kein1", "Bold", 34, kreuz=beim("kein1", "kein")),
    *requisit([("anf", ("tabler", "message", 110, WEISS), "Anfechtung", WEISS),
               ("wollte", ("tabler", "equal", 110, GELB), "Wille = Erklärung", GELB)]),
    *stehend("EI", FX, [("anf", "ernst"), ("wollte", "denkt"), ("kein1", "sorge")]),
])
assert w119_y + 124 + 40 <= 895, w119_y

# ===========================================================================================================================
# F § 119 Abs. 2 BGB (Wortlautkarte): Wert selbst keine verkehrswesentliche Eigenschaft (OLG Düsseldorf)
# ===========================================================================================================================
w1192, w1192_y = wortlaut(80, 170, 1100, "„(2) Als Irrtum über den Inhalt der Erklärung gilt auch der Irrtum über solche "
                                         "Eigenschaften der Person oder der Sache, die im Verkehr als wesentlich angesehen "
                                         "werden.“", "§ 119 Abs. 2 BGB", "w1192", size=33,
                          marken=[("Eigenschaften", beim("w1192", "Eigenschaften")),
                                  ("wesentlich angesehen", beim("w1192", "wesentlich"))])
folie([("w1192", f"{PII} › § 119 Abs. 2 BGB: Eigenschaftsirrtum?"), ("wert", f"{PII} › Wert selbst: keine Eigenschaft"),
       ("faktor", f"{PII} › nur wertbildende Umstände"), ("hier2", f"{PII} › hier: nur Marktpreis falsch eingeschätzt")], [
    *tafel("w1192", "Irrtum über eine Eigenschaft?"),
    *w1192,
    *neinz("Wert selbst: keine solche Eigenschaft", w1192_y + 26, "wert", "Bold", 34, kreuz=beim("wert", "keine")),
    zit("OLG Düsseldorf, Urt. v. 27.1.2000 – 6 U 168/98, Rn. 34;", 185, w1192_y + 74, beim("wert", "Gerichte")),
    zit("OLG Düsseldorf, Beschl. v. 1.7.2025 – 3 W 63/25, Rn. 25", 185, w1192_y + 110, beim("wert", "Gerichte")),
    *okw("nur Umstände, die den Wert bilden:", w1192_y + 170, "faktor", beim("faktor", "Umstände"), "Bold", 34),
    z("etwa Modell und Zustand", 185, w1192_y + 220, beim("faktor", "Modell"), "Bold", 34),
    blk(110, w1192_y + 290, 1040, 110, HELLGRAU, "hier2", [("Herr Eichler: darüber nicht geirrt,", "ExtraBold", 31, INK),
                                                          ("nur den Marktpreis falsch eingeschätzt", "ExtraBold", 31, INK)]),
    *requisit([("w1192", ("tabler", "camera", 130, HELLGRAU), "Eigenschaft?", WEISS),
               ("wert", ("tabler", "coin-euro", 110, GELB), "Wert", HELLROT),
               ("faktor", ("tabler", "camera", 130, HELLGRAU), "Modell, Zustand", HELLGRUEN),
               ("hier2", ("tabler", "chart-line", 110, WEISS), "Marktpreis", WEISS)]),
    *stehend("EI", FX, [("w1192", "ruhig"), ("wert", "sorge"), ("faktor", "denkt"), ("hier2", "still")]),
])
assert w1192_y + 290 + 110 <= 895, w1192_y

# ===========================================================================================================================
# G Motivirrtum; Kalkulationsirrtum (VIII ZR 79/04 S. 8 f.); Risiko beim Verkäufer (VIII ZR 42/14 Rn. 12)
# ===========================================================================================================================
folie([("motiv", f"{PII} › Irrtum im Beweggrund: Motivirrtum"), ("kalk", f"{PII} › grundsätzlich keine Anfechtung"),
       ("risiko", f"{PII} › Risiko des Preises beim Verkäufer")], [
    *tafel("motiv", "Motivirrtum"),
    blk(110, 175, 1040, 90, LILAHELL, "motiv", [("Irrtum im Beweggrund = Motivirrtum", "ExtraBold", 34, INK)]),
    *neinz("wie Kalkulationsirrtum: grundsätzlich", 310, "kalk", "Bold", 34, kreuz=beim("kalk", "grundsätzlich")),
    z("keine Anfechtung", 185, 358, beim("kalk", "grundsätzlich"), "Bold", 34),
    zit("BGH, Urt. v. 26.1.2005 – VIII ZR 79/04, S. 8 f.", 185, 410, beim("kalk", "grundsätzlich")),
    blk(110, 480, 1040, 150, GELB, beim("risiko", "Wer"), [("BGH zur Auktion: Startpreis unter Marktwert", "ExtraBold", 31, INK),
                                                          ("ohne Mindestpreis – Risiko trägt", "ExtraBold", 31, INK),
                                                          ("der Verkäufer", "ExtraBold", 31, INK)]),
    zit("BGH, Urt. v. 12.11.2014 – VIII ZR 42/14, Rn. 12", 110, 642, beim("risiko", "Wer")),
    *okz("fester Preis: Risiko ebenso beim Verkäufer", 700, beim("risiko", "Bei"), "Bold", 34),
    *requisit([("motiv", ("tabler", "brain", 120, LILAHELL), "Beweggrund", LILAHELL),
               ("kalk", ("tabler", "calculator", 110, WEISS), "Kalkulation", WEISS),
               ("risiko", ("tabler", "alert-triangle", 120, GELB), "Risiko", GELB)]),
    *stehend("EI", FX, [("motiv", "denkt"), ("kalk", "sorge"), ("risiko", "still")]),
])

# ===========================================================================================================================
# H Ergebnis: zurück an der Haustür
# ===========================================================================================================================
folie([("erg", "Ergebnis · an den Preis gebunden"), ("erg2", "Ergebnis › Kamera für 900 € übergeben und übereignen")], [
    *haustuer("erg", oben=250),
    *fig("EI", ET, BODEN, FH, [("erg", "still_r"), ("erg2", "ernst_r")], erst="cut"),
    hart(ns(NAME["EI"], ET, BODEN, "erg", BLAU_P)),
    *fig("HE", HT, BODEN, FH, [("erg", "ruhig"), (beim("erg", "gebunden"), "froh"), ("erg2", "strahlt")], erst="cut"),
    hart(ns(NAME["HE"], HT, BODEN, "erg", LILA_P)),
    *okz("Herr Eichler ist an seinen Preis gebunden", 40, "erg", "Bold", 34, x=130, rechts=1880),
    *okz("Kamera für 900 € übergeben und übereignen", 104, "erg2", "Bold", 34, x=130, rechts=1880),
    zit("§ 433 Abs. 1 Satz 1 BGB; § 145 BGB; keine Anfechtung nach § 119 BGB", 130, 160, beim("erg2", "übergeben"), rechts=1880),
])

# ===========================================================================================================================
# I Gegenfall: Tippfehler 90 statt 900 € – Erklärungsirrtum (VIII ZR 79/04 S. 7), § 122
# ===========================================================================================================================
folie([("gegen", "Gegenfall · vertippt: 90 € statt 900 €"), ("tipp90", "Gegenfall › Erklärungsirrtum, § 119 Abs. 1 Alt. 2 BGB"),
       ("p122", "Gegenfall › nichtig, § 122 BGB: Vertrauensschaden")], [
    *tafel("gegen", "Gegenfall: vertippt"),
    blk(110, 175, 500, 110, WEISS, "gegen", [("gewollt:", "Bold", 30, INK), ("900 €", "ExtraBold", 34, INK)]),
    pfeil(630, 230, 700, 230, beim("gegen", "vertippt"), breite=8, kopf=24),
    blk(720, 175, 430, 110, HELLROT, beim("gegen", "neunzig"), [("in der Anzeige:", "Bold", 30, INK), ("90 €", "ExtraBold", 34, INK)]),
    *okw("Erklärungsirrtum, § 119 Abs. 1 Alt. 2 BGB", 330, "tipp90", beim("tipp90", "Erklärungsirrtum"), "Bold", 34),
    zit("BGH, Urt. v. 26.1.2005 – VIII ZR 79/04, S. 7", 185, 378, beim("tipp90", "Erklärungsirrtum")),
    blk(110, 430, 1040, 90, LILAHELL, beim("tipp90", "wie"), [("wie Folge „Preisfehler im Onlineshop“", "ExtraBold", 32, INK)]),
    z("unverzüglich angefochten: Vertrag nichtig", 110, 560, "p122", "Bold", 34),
    zit("§§ 121 Abs. 1, 142 Abs. 1 BGB", 110, 606, "p122"),
    blk(110, 660, 1040, 120, HELLGRAU, beim("p122", "Frau"), [("§ 122 BGB: Frau Hegemann bekommt grundsätzlich", "ExtraBold", 31, INK),
                                                            ("nur ihren Vertrauensschaden ersetzt", "ExtraBold", 31, INK)]),
    *requisit([("gegen", ("tabler", "keyboard", 150, WEISS), "vertippt", HELLROT),
               ("tipp90", ("tabler", "check", 110, GRUEN_P), "anfechtbar", HELLGRUEN),
               ("p122", ("tabler", "coin-euro", 120, GELB), "Vertrauensschaden", GELB)], px=1560, pu=330, py=90),
    *paar("HE", [("gegen", "ruhig"), ("p122", "denkt")], "EI", [("gegen", "sorge"), ("tipp90", "froh")]),
])

# ===========================================================================================================================
# K Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Wille und Erklärung vergleichen"), ("tipp2", "Klausurtipp · sonst nur Motivirrtum"),
       ("tipp3", "Klausurtipp · § 119 Abs. 2: Wert oder wertbildender Umstand")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Wille und Erklärung nebeneinanderlegen", 200, 200, beim("tipp", "Lege"), "Bold", 35),
    z("stimmen sie überein: nur Irrtum im", 200, 290, "tipp2", "Bold", 34),
    z("Beweggrund – grundsätzlich unbeachtlich", 200, 338, beim("tipp2", "grundsätzlich"), "Bold", 34),
    linienzug([(130, 418), (1130, 418)], "tipp3", breite=3),
    z("§ 119 Abs. 2 BGB sauber trennen:", 200, 448, "tipp3", "ExtraBold", 35),
    *neinz("Wert selbst: keine Eigenschaft", 518, beim("tipp3", "keine"), "Bold", 34, x=245),
    *okz("Umstände, die den Wert bilden: schon", 578, beim("tipp3", "Umstände"), "Bold", 34, x=245),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# L Prüfungsschema
# ===========================================================================================================================
REIHEN = [("s1", 0, "I. Kaufvertrag", True),
          ("s1a", 1, "Angebot durch Einstellen mit „Sofort kaufen“, bindend nach § 145 BGB", False),
          ("s1b", 1, "Annahme durch den Klick", False),
          ("s2", 0, "II. Nichtigkeit durch Anfechtung, § 142 Abs. 1 BGB", True),
          ("s2a", 1, "kein Inhalts- oder Erklärungsirrtum, § 119 Abs. 1 BGB", False),
          ("s2b", 1, "kein Eigenschaftsirrtum (§ 119 Abs. 2 BGB), nur unbeachtlicher Motivirrtum", False),
          ("s3", 0, "III. Ergebnis: Anspruch aus § 433 Abs. 1 Satz 1 BGB besteht", True)]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfungsschema: Frau Hegemann gegen Herrn Eichler"), 110, 90, "sch", 44),
           z("auf Übergabe und Übereignung der Kamera", 110, 158, beim("sch", "Übergabe"), "Bold", 36, rechts=1800)]
y = 240
for c, ebene, text, fett in REIHEN:
    x = (130, 200)[ebene]
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 40 if ebene == 0 else 36, rechts=1800))
    y += {0: 92, 1: 80}[ebene]
assert y <= 975, y
folie([("sch", "Prüfungsschema"), ("s1", "Prüfungsschema › I. Kaufvertrag"), ("s2", "Prüfungsschema › II. Anfechtung"),
       ("s3", "Prüfungsschema › III. Ergebnis")], els_sch)

# ===========================================================================================================================
# M Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Wer mit „Sofort kaufen“ einstellt,", 0)], [("macht in der Regel ein ", 0)],
                 [("verbindliches Angebot", "a"), (".", 0)]],
                750, 270, 44, "merke", {"a": beim("merke", "verbindliches")}),
    *markertext([[("Wer nur den Wert falsch einschätzt,", 0)], [("kann nicht nach § 119 BGB ", 0), ("anfechten", "b"), (".", 0)],
                 [("Das ", 0), ("Risiko", "c"), (" trägt er selbst.", 0)]],
                750, 520, 44, "merk2", {"b": beim("merk2", "anfechten"), "c": beim("merk2", "Risiko")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
