"""Folge 047 · Vermögensdelikte Überblick: Diebstahl, Betrug, Raub, Erpressung – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A Kameraladen (Fall), B Sachverhalt (sieben Varianten), C Landkarte (zwei Säulen),
D Diebstahl (Wortlautkarte § 242 I), E Unterschlagung, F Raub (Wortlautkarte § 249 I), G Betrug (Wortlautkarte § 263 I),
H Sachbetrug oder Trickdiebstahl, I Erpressung/räuberische Erpressung, J Streit Raub/räuberische Erpressung,
K Untreue, L Klausurtipp (Lexi), M Entscheidungsbaum, N Merksatz (Lexi).
Rechts oben ab Szene D eine kleine Landkarte (aktuelles Feld gelb, behandelte weiß); sie weicht nur, solange eine
Sprechblase steht. Gewalt zurückhaltend: keine Waffen, kein Blut, keine Schlagbewegung; die Drohung nur als Blase.
Geräusch: nur die Ladenglocke an der sichtbar benutzten Ladentür (szene_047glocke_1)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_047/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
GRAU = (176, 178, 190, 255)
LEER = (246, 244, 240, 255)
DUNKEL = (74, 74, 94, 255)
DAUER = bausteine._cj()["dauer"]
NULL = ("fall", -0.4)                       # Hauptfilmbeginn 0,0 s: Grundbild sofort vollständig

_CMAP = set(TTFont(SP + "humaaans/fonts/Nunito[wght].ttf").getBestCmap())


def glyphen(text):
    """Nunito muss jedes Zeichen haben (sonst Kästchen)."""
    fehl = {c for c in text if ord(c) not in _CMAP and not c.isspace()}
    assert not fehl, f"Zeichen fehlt in Nunito: {fehl} in {text!r}"
    return text


def z(text, x, y, cue, stil="Regular", size=36, farbe=INK, d=0.0, rechts=1170, **k):
    """Tafelzeile, die rechts nicht über die Karte hinausragen darf."""
    e = zeile(glyphen(text), x, y, cue, stil, size, farbe=farbe, d=d, **k)
    assert e.x + e.sprite.width <= rechts, f"Zeile zu breit: {text} ({e.x + e.sprite.width:.0f} > {rechts})"
    return e


def pl(text, *a, **k):
    return pille(glyphen(text), *a, **k)


def tafel(cue, titel_, h=840, fill=WEISS, size=46):
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(glyphen(titel_), 110, 100, cue, size)]


def zitat(text, x, y, cue, size=26, **k):
    """BGH-Fundstelle unter einer Aussage (klein, grau)."""
    return z(text, x, y, cue, "Bold", size, farbe=TEXT, **k)


def blk(x, y, w, h, fill, cue, zeilen, anim="rise", d=0.0, bis=None):
    """Wie fl_block(), aber Zeilenabstand nach der tatsächlichen Schriftgröße (zweizeilige Blöcke bleiben im Kasten)."""
    for t_, *_ in zeilen:
        glyphen(t_)
        assert F(_[0], _[1]).getlength(t_) <= w - 40, f"Block zu breit: {t_}"
    return block(x, y, w, h, fill, None, cue, textsize=zeilen[0][2], rund=18, rand=INK, randbreite=5, anim=anim, d=d,
                 bis=bis, zeilen=zeilen)


def lexi_bis_ende(cue):
    return (cue, round(DAUER - bausteine._t(cue) - 0.05, 3))


def hart(e):
    e.anim = "cut"
    return e


def bis_(e, cue):
    e.bis = cue
    return e


def fig(name, cx, unten, hoehe, folge, d=0.0, bis=None, erst="pop"):
    """Mimikfolge einer Figur am selben Platz: folge = [(cue, suffix)] → harte Schnitte."""
    els = []
    for i, (c, s) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else bis
        els.append(peep_voll(f"{name}_{s}", cx, unten, hoehe, c, anim=erst if i == 0 else "cut", d=d if i == 0 else 0.0, bis=b))
    return els


def umbruch(text, breite, size):
    f = F("Regular", size)
    zeilen, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if f.getlength(t) <= breite:
            cur = t
        else:
            zeilen.append(cur); cur = w
    return zeilen + [cur]


def wortlaut(x, y, w, text, quelle, cue, marken=(), size=30, bis=None):
    """Wortlautkarte: Normtext wörtlich (gesetze-im-internet.de), als Zitat mit Normangabe; marken = [(wort, cue)]
    legt synchron zum gesprochenen Merkmal einen Textmarker hinter die Wortgruppe (sie muss in einer Zeile stehen)."""
    zeilen = umbruch(text, w - 60, size)
    lh = int(size * 1.42)
    hgt = 40 + lh * len(zeilen) + 46
    els = [bis_(karte(x, y, w, hgt, cue, fill=HELL, rund=18, schatten=6, rand=4), bis)]
    f = F("Regular", size)
    tx, ty = x + 28, y + 26
    for wort, mc in marken:
        zi = next((i for i, t in enumerate(zeilen) if wort in t), None)
        assert zi is not None, f"Marker {wort!r} nicht in einer Zeile: {zeilen}"
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


def sachverhalt_klein(cue, absaetze, frage, size=32, pfad="Sachverhalt"):
    """Wie bausteine.sachverhalt(), aber mit kleinerer Schrift (Grundfall und sieben Varianten, je ein Absatz)."""
    els = [karte(140, 50, 1640, 920, cue, fill=HELL), titel("Sachverhalt", 210, 82, cue, 56)]
    y = 172
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=size, zeilenabstand=1.25)
        els += e; y += 9
    els.append(pl(frage, 210, y + 6, cue, fill=PINK, size=32))
    assert y + 6 <= 900, f"Sachverhalt zu lang ({y})"
    folie([(cue, pfad)], els)


# --- Eigene Hilfsfunktion (wie Folge 029/035/042): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt -------
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
    """Wie bausteine.redet(), aber Wortende = hörbares Ende; Viseme aus der Schreibung geschätzt (kein Phonem-Alignment)."""
    cj = bausteine._cj(); ta, tb = bausteine._t(cue), bausteine._t(bis)
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


# --- Figuren und Namensschilder ----------------------------------------------------------------------------------------
NAMEN = {"DA": ("Dagmar", LILA), "KL": ("Klaus", GRUEN)}
BR = 930                                    # Boden der Tafelszenen
FR = 440                                    # Standhöhe in den Tafelszenen
DX, KX = 1430, 1745                         # Dagmar links, Klaus rechts unter der kleinen Landkarte
PY = 398                                    # Pillen zwischen Landkarte und Köpfen


def name(p, cx, cue, unten=BR, size=28, d=0.0, bis=None, anim="cut"):
    t, f = NAMEN[p]
    return pl(t, cx, unten + 26, cue, fill=f, size=size, anker="m", d=d, bis=bis, anim=anim)


def kamera(cx, unten, breite, cue, bis=None, anim="pop", fuell=GELB):
    return ficon("tabler", "camera", cx, unten, breite, cue, fuell=fuell, bis=bis, anim=anim)


def paar(cue, da_folge, kl_folge, dx=DX, kx=KX):
    """Dagmar und Klaus rechts neben der Tafel, je mit Namensschild ab Folienbeginn."""
    return [*fig("DA", dx, BR, FR, da_folge, erst="cut"), name("DA", dx, cue),
            *fig("KL", kx, BR, FR, kl_folge, erst="cut"), name("KL", kx, cue)]


# --- Kleine Landkarte rechts oben ------------------------------------------------------------------------------------
MX0, MY0, MW = 1268, 58, 604
SPX = {"E": (MX0 + 14, 280), "V": (MX0 + 310, 280)}
FELDER = {"242": ("E", 0, "§ 242 Diebstahl"), "246": ("E", 1, "§ 246 Unterschlagung"), "249": ("E", 2, "§ 249 Raub"),
          "263": ("V", 0, "§ 263 Betrug"), "253": ("V", 1, "§ 253 Erpressung"),
          "255": ("V", 2, "§ 255 räub. Erpressung"), "266": ("V", 3, "§ 266 Untreue")}
ZY = [MY0 + 54 + i * 66 for i in range(4)]
# Reihenfolge der ersten Hervorhebung im Film (für „schon behandelt“)
ERST = {}


def _zelle(k, cue, fill, farbe, bis=None, anim="cut"):
    sp, zi, text = FELDER[k]
    x, w = SPX[sp]
    els = [bis_(karte(x, ZY[zi], w, 52, cue, fill=fill, rund=10, schatten=0, rand=3, anim=anim), bis)]
    f = F("Bold", 23)
    tw = f.getlength(text)
    assert tw <= w - 14, f"Landkarte: {text} zu breit"
    els.append(z(text, x + (w - tw) / 2, ZY[zi] + 9, cue, "Bold", 23, farbe=farbe, rechts=x + w, bis=bis, anim=anim))
    return els


def minikarte(start, aktiv, luecke=None):
    """Kleine Landkarte ab Folienbeginn 'start'. aktiv = [(Feld, cue)]: das Feld wird beim gesprochenen Paragrafen gelb.
    Vorher behandelte Felder weiß, noch offene grau. luecke = (cue_aus, cue_an): weicht einer Sprechblase."""
    t0 = bausteine._t(start)
    stuecke = [(start, luecke[0]), (luecke[1], None)] if luecke else [(start, None)]
    els = []
    for von, bis in stuecke:
        e_ = [karte(MX0, MY0, MW, 330, von, fill=WEISS, rund=18, schatten=6, rand=4, anim="cut"),
              z("Eigentum", SPX["E"][0] + 140 - F("Bold", 24).getlength("Eigentum") / 2, MY0 + 14, von, "Bold", 24, rechts=1862, anim="cut"),
              z("Vermögen", SPX["V"][0] + 140 - F("Bold", 24).getlength("Vermögen") / 2, MY0 + 14, von, "Bold", 24, rechts=1862, anim="cut")]
        for e in e_:
            e.bis = bis
        els += e_
        for k in FELDER:
            frueher = k in ERST and ERST[k] < t0 - 0.01
            els += _zelle(k, von, WEISS if frueher else LEER, INK if frueher else GRAU, bis=bis)
        for k, c in aktiv:
            tc = bausteine._t(c)
            an = c if tc >= bausteine._t(von) else von
            if bis is not None and tc >= bausteine._t(bis):
                continue
            els += _zelle(k, an, GELB, INK, bis=bis)
    for k, c in aktiv:
        ERST.setdefault(k, bausteine._t(c))
    return els


# A Fall: Dagmars Kameraladen ------------------------------------------------------------------------------------------
BA = 900                                    # Boden im Laden
SH = 560                                    # Standhöhe im Fall
DAX, KLX = 1600, 1040
THEKE = (1330, 650, 540, 250)
REGAL = [(110, 430, 560), (110, 650, 560)]   # (x0, y, x1) zwei Regalbretter
DAb = ("DA_redet", DAX, BA, SH)
KLb = ("KL_redet", KLX, BA, SH)
folie([(NULL, "Fall · Der Kameraladen"), ("frage", "Fall · Die Frage")], [
    hart(linienzug([(80, BA + 2), (1840, BA + 2)], NULL, breite=6, farbe=INK)),
    *[hart(linienzug([(x0, y), (x1, y)], NULL, breite=8, farbe=INK)) for x0, y, x1 in REGAL],
    hart(linienzug([(110, 300), (110, BA)], NULL, breite=6, farbe=INK)),
    hart(linienzug([(560, 300), (560, BA)], NULL, breite=6, farbe=INK)),
    hart(kamera(200, 430, 90, NULL, fuell=BLAU, anim="cut")), hart(kamera(450, 430, 90, NULL, fuell=WEISS, anim="cut")),
    hart(kamera(200, 650, 80, NULL, fuell=WEISS, anim="cut")),
    hart(kamera(420, 650, 130, NULL, fuell=GELB, anim="cut")),               # die Spiegelreflexkamera
    hart(ficon("tabler", "door", 760, BA, 170, NULL, fuell=WEISS, anim="cut")),
    pl("Samstagvormittag", 100, 64, NULL, fill=GELB, size=34, anim="cut"),
    pl("Altstadt", 100, 140, beim("fall", "Altstadt"), fill=WEISS, size=30),
    # Dagmar hinter der Theke
    *fig("DA", DAX, BA, SH, [(beim("dagmar", "Dagmar"), "ruhig"), ("k1", "skeptisch"), ("frage", "denkt")]),
    hart(karte(*THEKE, NULL, fill=WEISS, rund=14, schatten=8, rand=5, anim="cut")),
    hart(ficon("tabler", "cash-register", 1780, THEKE[1], 120, NULL, fuell=WEISS, anim="cut")),
    name("DA", DAX, beim("dagmar", "Dagmar"), unten=740, size=30, anim="pop"),
    pl("gebrauchte Kameras", 1600, 250, beim("dagmar", "Kameras"), fill=WEISS, size=28, anker="m", bis="klaus"),
    pl("Spiegelreflexkamera · 300 €", 335, 520, beim("kamera", "Spiegelreflexkamera"), fill=GELB, size=28, anker="m"),
    # Klaus kommt durch die Ladentür (Ladenglocke)
    szene(peep_voll("KL_listig", KLX, BA, SH, beim("klaus", "Klaus"), anim="pop", bis="k1"), "047glocke*", 0.8),
    *redet("KL_redet", KLX, BA, SH, "k1", "frage"),
    *fig("KL", KLX, BA, SH, [("frage", "listig")], erst="cut"),
    name("KL", KLX, beim("klaus", "Klaus"), unten=BA - 6, anim="pop"),
    pl("bezahlen will er nicht", KLX, 250, beim("klaus", "bezahlen"), fill=PINK, size=28, anker="m", bis="k1"),
    blase("sprech", 520, 200, "k1", 820, 230, inhalt=["Die Kamera kriege ich", "schon, so oder so."], textsize=34,
          figur=KLb, bis="frage"),
    # Frage
    pl("Wie kommt Klaus an die Kamera?", 1050, 200, "frage", fill=PINK, size=34, anker="m"),
    pl("Diebstahl?", 700, 290, beim("frage2", "Diebstahl"), fill=WEISS, size=28, anker="m"),
    pl("Betrug?", 900, 290, beim("frage2", "Betrug"), fill=WEISS, size=28, anker="m"),
    pl("Raub?", 1060, 290, beim("frage2", "Raub"), fill=WEISS, size=28, anker="m"),
    pl("Erpressung?", 1250, 290, beim("frage2", "Erpressung"), fill=WEISS, size=28, anker="m"),
])

# B Sachverhalt ----------------------------------------------------------------------------------------------------------
sachverhalt_klein("sv", [
    "Samstagvormittag in der Altstadt: Dagmar verkauft in ihrem Laden gebrauchte Kameras, darunter eine alte "
    "Spiegelreflexkamera für 300 Euro. Klaus gefällt die Kamera, bezahlen will er sie nicht.",
    "Variante 1: Klaus steckt die Kamera unbemerkt ein und geht.",
    "Variante 2: Dagmar leiht Klaus die Kamera für ein Wochenende. Erst später beschließt er, sie zu verkaufen, und "
    "verkauft sie.",
    "Variante 3: Klaus droht Dagmar Schläge an („Keine Bewegung, sonst gibt es Schläge!“) und nimmt die Kamera selbst "
    "aus dem Regal.",
    "Variante 4: Klaus behauptet, Dagmars Bruder habe die Kamera schon bezahlt und ihn zum Abholen geschickt. Dagmar "
    "glaubt ihm und gibt sie ihm mit.",
    "Variante 5: Klaus fragt, ob er kurz durch die Kamera schauen darf. Dagmar reicht sie ihm, er rennt damit hinaus.",
    "Variante 6: Klaus droht, Dagmars Laden im Internet mit erfundenen Vorwürfen schlechtzumachen. Dagmar verkauft "
    "ihm die Kamera deshalb für 10 Euro.",
    "Variante 7: wie Variante 3, doch Dagmar reicht Klaus die Kamera.",
], "Wie hat sich Klaus jeweils strafbar gemacht?")

# C Landkarte -----------------------------------------------------------------------------------------------------------
CX0, CX1, CW = 110, 650, 500
CY = [275, 370, 465, 560]
folie([("karte", "Überblick · Landkarte der Vermögensdelikte")], [
    *tafel("karte", "Die Landkarte: zwei Säulen"),
    hart(karte(90, CY[2] - 12, 1080, 100, "bruecke", fill=PINK, rund=16, schatten=0, rand=0, anim="fade")),
    blk(CX0, 180, CW, 70, LILA, "eigen", [("Eigentumsdelikte", "ExtraBold", 34, INK)]),
    *[karte(CX0, CY[i], CW, 76, beim("eigen", w_), fill=WEISS, rund=14, schatten=0, rand=3) for i, w_ in
      enumerate(["Diebstahl", "Unterschlagung", "Raub"])],
    *[z(t_, CX0 + 24, CY[i] + 18, beim("eigen", w_), "Bold", 32) for i, (t_, w_) in
      enumerate([("Diebstahl, § 242", "Diebstahl"), ("Unterschlagung, § 246", "Unterschlagung"), ("Raub, § 249", "Raub")])],
    z("Schutz: Eigentum an fremder", CX0, 690, "eig2", size=30, rechts=CX0 + CW),
    z("beweglicher Sache; kein", CX0, 730, beim("eig2", "Vermögensschaden"), size=30, rechts=CX0 + CW),
    z("Vermögensschaden nötig", CX0, 770, beim("eig2", "Vermögensschaden"), size=30, rechts=CX0 + CW),
    blk(CX1, 180, CW, 70, BLAU, "verm", [("Vermögensdelikte", "ExtraBold", 34, INK)]),
    *[karte(CX1, CY[i], CW, 76, beim("verm", w_), fill=WEISS, rund=14, schatten=0, rand=3) for i, w_ in
      enumerate(["Betrug", "Erpressung", "räuberische", "Untreue"])],
    *[z(t_, CX1 + 24, CY[i] + 18, beim("verm", w_), "Bold", 31, rechts=CX1 + CW) for i, (t_, w_) in
      enumerate([("Betrug, § 263", "Betrug"), ("Erpressung, § 253", "Erpressung"),
                 ("räub. Erpressung, § 255", "räuberische"), ("Untreue, § 266", "Untreue")])],
    z("Schutz: Vermögen;", CX1, 690, "verm2", size=30, rechts=CX1 + CW),
    z("Schaden nötig", CX1, 730, beim("verm2", "Schaden"), size=30, rechts=CX1 + CW),
    z("zusätzlich: Gewalt gegen eine Person oder Drohung", 110, 812, beim("bruecke", "Gewalt"), "Bold", 30),
    z("mit gegenwärtiger Gefahr für Leib oder Leben", 110, 852, beim("bruecke", "Drohung"), "Bold", 30),
    *paar("karte", [("karte", "denkt"), ("verm", "skeptisch"), ("bruecke", "sorge")],
          [("karte", "ruhig"), ("eigen", "denkt"), ("verm2", "listig")]),
    pl("zwei Säulen", 1590, 300, beim("karte", "zwei"), fill=GELB, size=32, anker="m"),
])

# D Diebstahl, § 242 ------------------------------------------------------------------------------------------------------
PA = "A. Eigentumsdelikte"
T242 = ("„Wer eine fremde bewegliche Sache einem anderen in der Absicht wegnimmt, die Sache sich oder einem Dritten "
        "rechtswidrig zuzueignen, wird mit Freiheitsstrafe bis zu fünf Jahren oder mit Geldstrafe bestraft.“")
wl242, y242 = wortlaut(90, 170, 1090, T242, "§ 242 Abs. 1 StGB", "p242w",
                       marken=[("fremde bewegliche Sache", beim("p242w", "fremde")),
                               ("wegnimmt", beim("p242w", "wegnimmt")),
                               ("rechtswidrig zuzueignen", beim("p242w", "rechtswidrig"))])
folie([("p242", f"{PA} › Diebstahl, § 242 StGB"), ("v1", f"{PA} › Diebstahl, § 242 StGB › Variante 1")], [
    *tafel("p242", "Diebstahl, § 242 StGB"),
    *wl242,
    z("Wegnahme: fremden Gewahrsam brechen, neuen begründen", 110, y242 + 30, "wegn", "Bold", 33),
    zitat("BGH, Beschl. v. 3.3.2021 – 4 StR 338/20, Rn. 5", 110, y242 + 80, beim("wegn", "begründen")),
    z("Bruch: ohne oder gegen den Willen des Inhabers", 110, y242 + 135, "bruch", size=33),
    z("Variante 1: unbemerkt eingesteckt", 110, y242 + 220, "v1", "Bold", 36),
    ok(135, y242 + 318, "v1ok", gr=22), z("Diebstahl, § 242 StGB", 175, y242 + 295, "v1ok", "ExtraBold", 38),
    *minikarte("p242", [("242", beim("p242", "Diebstahl"))]),
    *paar("p242", [("p242", "ruhig"), ("v1", "denkt"), ("v1ok", "erschrickt")],
          [("p242", "ruhig"), ("wegn", "denkt"), ("v1", "listig"), ("v1ok", "froh")]),
    kamera(1590, 760, 90, "p242", bis="v1"),
    pl("unbemerkt eingesteckt", 1650, PY, beim("v1", "unbemerkt"), fill=PINK, size=26, anker="m"),
])

# E Unterschlagung, § 246 ---------------------------------------------------------------------------------------------
folie([("p246", f"{PA} › Unterschlagung, § 246 StGB"), ("v2", f"{PA} › Unterschlagung, § 246 StGB › Variante 2")], [
    *tafel("p246", "Unterschlagung, § 246 StGB"),
    z("Klaus hat die Kamera schon in der Hand?", 110, 185, beim("p246", "Klaus"), size=34),
    z("Variante 2: Dagmar leiht ihm die Kamera,", 110, 250, "v2", "Bold", 35),
    z("später beschließt er, sie zu verkaufen", 150, 302, beim("v2", "beschließt"), size=34),
    nein(135, 393, "keinew", gr=20), z("keine Wegnahme: Gewahrsam selbst überlassen", 175, 370, "keinew", size=34),
    blk(110, 440, 1040, 80, GELB, "p246b", [("§ 246: Zueignung ohne Wegnahme", "ExtraBold", 36, INK)]),
    z("Zueignung: Strafsenate sehen das unterschiedlich", 110, 548, "zueig", size=34),
    ok(135, 623, beim("zueig", "Verkauf"), gr=22), z("Verkauf genügt jedenfalls", 175, 600, beim("zueig", "Verkauf"), "Bold", 36),
    zitat("BGH 6 StR 191/23, Rn. 5, 12 · BGH 4 StR 442/23, Rn. 11", 175, 652, beim("zueig", "jedenfalls")),
    z("anvertraut: § 246 Abs. 2, höhere Strafe", 110, 730, "anv", "Bold", 36),
    *minikarte("p246", [("246", beim("p246b", "Unterschlagung"))]),
    *paar("p246", [("p246", "ruhig_r"), ("v2", "froh_r"), ("keinew", "denkt"), ("zueig", "sorge")],
          [("p246", "ruhig"), ("v2", "froh"), (beim("v2", "beschließt"), "listig"), ("p246b", "denkt")]),
    kamera(1590, 760, 90, "v2", bis=beim("v2", "verkaufen")),
    pl("geliehen", 1590, PY, beim("v2", "leiht"), fill=WEISS, size=26, anker="m", bis=beim("v2", "verkaufen")),
    ficon("tabler", "world-www", 1590, 760, 80, beim("v2", "verkaufen"), fuell=WEISS),
    pl("verkauft", 1700, PY, beim("v2", "verkaufen"), fill=PINK, size=26, anker="m"),
])

# F Raub, § 249 ---------------------------------------------------------------------------------------------------------
T249 = ("„Wer mit Gewalt gegen eine Person oder unter Anwendung von Drohungen mit gegenwärtiger Gefahr für Leib oder "
        "Leben eine fremde bewegliche Sache einem anderen in der Absicht wegnimmt, die Sache sich oder einem Dritten "
        "rechtswidrig zuzueignen, wird mit Freiheitsstrafe nicht unter einem Jahr bestraft.“")
wl249, y249 = wortlaut(90, 170, 1090, T249, "§ 249 Abs. 1 StGB", "p249", size=29,
                       marken=[("wegnimmt", beim("p249w", "Diebstahl")),
                               ("mit Gewalt gegen eine Person", beim("p249w", "Gewalt")),
                               ("Drohungen", beim("p249w", "Drohungen")),
                               ("mit gegenwärtiger Gefahr für Leib oder Leben", beim("p249w", "gegenwärtiger")),
                               ("nicht unter einem Jahr", beim("v5ok", "nicht"))])
DAr = ("DA_erschrickt_r", DX, BR, FR)
KLd = ("KL_droht", KX, BR, FR)
folie([("p249", f"{PA} › Raub, § 249 StGB"), ("v5", f"{PA} › Raub, § 249 StGB › Variante 3")], [
    *tafel("p249", "Raub, § 249 StGB"),
    *wl249,
    z("Diebstahl mit Gewalt oder Drohung (Leib, Leben)", 110, y249 + 24, "p249w", "Bold", 33),
    z("Nötigungsmittel soll die Wegnahme ermöglichen", 110, y249 + 84, "final", size=33),
    zitat("BGH, Beschl. v. 24.4.2018 – 5 StR 606/17, Rn. 10", 110, y249 + 132, beim("final", "ermöglichen")),
    z("Variante 3: Drohung mit Schlägen", 110, y249 + 200, "v5", "Bold", 36),
    z("Klaus nimmt die Kamera selbst aus dem Regal", 150, y249 + 252, "v5b", size=34),
    ok(135, y249 + 333, "v5ok", gr=22), z("Raub, § 249 StGB", 175, y249 + 310, "v5ok", "ExtraBold", 38),
    *minikarte("p249", [("249", beim("p249", "Raub"))], luecke=("k3", "v5b")),
    *fig("DA", DX, BR, FR, [("p249", "ruhig_r"), ("v5", "skeptisch_r"), ("k3", "erschrickt_r"), ("v5ok", "sorge_r")], erst="cut"),
    name("DA", DX, "p249"),
    *fig("KL", KX, BR, FR, [("p249", "ruhig"), ("v5", "entschlossen")], bis="k3", erst="cut"),
    *redet("KL_droht", KX, BR, FR, "k3", "v5b"),
    *fig("KL", KX, BR, FR, [("v5b", "entschlossen"), ("v5ok", "veraechtlich")], erst="cut"),
    name("KL", KX, "p249"),
    hart(linienzug([(1525, 640), (1655, 640)], "p249", breite=7, farbe=INK)),               # kleines Regal
    hart(linienzug([(1530, 560), (1530, BR)], "p249", breite=6, farbe=INK)),
    hart(linienzug([(1650, 560), (1650, BR)], "p249", breite=6, farbe=INK)),
    hart(linienzug([(1525, 800), (1655, 800)], "p249", breite=7, farbe=INK)),
    kamera(1590, 640, 80, "p249", bis="v5b"),
    kamera(1700, 770, 70, "v5b"),
    blase("sprech", 560, 220, "k3", 1560, 225, inhalt=["Keine Bewegung, sonst", "gibt es Schläge!"], textsize=34,
          figur=KLd, bis="v5b"),
    pl("nimmt selbst", 1745, PY, beim("v5b", "nimmt"), fill=PINK, size=26, anker="m"),
])

# G Betrug, § 263 ---------------------------------------------------------------------------------------------------------
PB = "B. Vermögensdelikte"
T263 = ("„Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das "
        "Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch Entstellung oder "
        "Unterdrückung wahrer Tatsachen einen Irrtum erregt oder unterhält, …“")
wl263, y263 = wortlaut(90, 170, 1090, T263, "§ 263 Abs. 1 StGB", "p263", size=28,
                       marken=[("Vorspiegelung falscher", beim("p263w", "Täuschung")),
                               ("Irrtum erregt", beim("p263w", "Irrtum")),
                               ("beschädigt", beim("p263w", "Schaden")),
                               ("in der Absicht", beim("p263w", "Bereicherungsabsicht"))])
MERK = [("Täuschung", 110, 0), ("Irrtum", 330, 0), ("Vermögensverfügung", 490, 0), ("Schaden", 860, 0),
        ("Vorsatz", 110, 1), ("Bereicherungsabsicht", 290, 1)]
DAb2 = ("DA_redet_r", DX, BR, FR)
folie([("p263", f"{PB} › Betrug, § 263 StGB"), ("v3", f"{PB} › Betrug, § 263 StGB › Variante 4")], [
    *tafel("p263", "Betrug, § 263 StGB"),
    *wl263,
    *[pl(t_, x_, y263 + 22 + r_ * 58, beim("p263w", t_), fill=(GELB if r_ == 0 else WEISS), size=28) for t_, x_, r_ in MERK],
    z("Variante 4: angeblich vom Bruder bezahlt,", 110, y263 + 150, "v3", "Bold", 35),
    z("Klaus soll sie abholen", 150, y263 + 202, beim("v3", "Abholen"), size=34),
    ok(135, y263 + 283, "verf", gr=22), z("Dagmar glaubt ihm, will Gewahrsam übertragen:", 175, y263 + 260, "verf", size=33),
    z("Vermögensverfügung", 175, y263 + 308, beim("verf", "Vermögensverfügung"), "Bold", 34),
    blk(110, y263 + 370, 1040, 76, GELB, "v3ok", [("Sachbetrug, § 263 StGB", "ExtraBold", 36, INK)]),
    *minikarte("p263", [("263", beim("p263", "Betrug"))], luecke=("d1", "verf")),
    *fig("DA", DX, BR, FR, [("p263", "ruhig_r"), ("v3", "denkt_r")], bis="d1", erst="cut"),
    *redet("DA_redet_r", DX, BR, FR, "d1", "verf"),
    *fig("DA", DX, BR, FR, [("verf", "froh_r")], erst="cut"),
    name("DA", DX, "p263"),
    *fig("KL", KX, BR, FR, [("p263", "ruhig"), ("v3", "froh"), ("v3ok", "listig")], erst="cut"),
    name("KL", KX, "p263"),
    kamera(1590, 760, 90, "v3", bis="verf"),
    kamera(1660, 790, 80, "verf"),
    blase("sprech", 540, 200, "d1", 1520, 230, inhalt=["Ach so, dann", "nehmen Sie sie mit."], textsize=34,
          figur=DAb2, bis="verf"),
    pl("Dagmar gibt", 1590, PY, "verf", fill=WEISS, size=26, anker="m"),
])

# H Sachbetrug oder Trickdiebstahl --------------------------------------------------------------------------------------
KLb2 = ("KL_bittet", KX, BR, FR)
KXW = 1650                                  # Klaus an der Ladentür
folie([("trick", f"{PB} › Sachbetrug oder Trickdiebstahl? › Variante 5")], [
    *tafel("trick", "Sachbetrug oder Trickdiebstahl?", size=44),
    pl("Variante 5", 110, 175, "trick", fill=GELB, size=30),
    z("Dagmar reicht die Kamera, Klaus rennt hinaus", 110, 245, "v4", "Bold", 35),
    z("Täuschung ja, aber Dagmar will sie sofort zurück", 110, 315, "locker", size=34),
    z("nur Gewahrsamslockerung", 110, 375, "mitgew", "Bold", 36),
    zitat("BGH, Urt. v. 12.10.2016 – 1 StR 402/16, Rn. 11–14", 110, 425, beim("mitgew", "lockert")),
    ok(135, 513, "v4ok", gr=22), z("Bruch erst beim Weglaufen: Trickdiebstahl", 175, 490, "v4ok", "Bold", 36),
    z("entscheidend: Willensrichtung der Getäuschten", 110, 590, "wille", size=34),
    blk(110, 650, 505, 110, BLAU, beim("wille", "Gibt"), [("Opfer gibt weg:", "ExtraBold", 33, INK), ("Betrug", "ExtraBold", 33, INK)]),
    blk(645, 650, 505, 110, LILA, beim("wille", "nimmt"), [("Täter nimmt:", "ExtraBold", 33, INK), ("Diebstahl", "ExtraBold", 33, INK)]),
    *minikarte("trick", [("263", "trick"), ("242", "v4ok")], luecke=("k2", "v4")),
    *fig("DA", DX, BR, FR, [("trick", "ruhig_r"), ("k2", "froh_r"), ("v4", "erschrickt_r"), ("mitgew", "sorge"),
                            ("wille", "denkt")], erst="cut"),
    name("DA", DX, "trick"),
    *fig("KL", KX, BR, FR, [("trick", "ruhig")], bis="k2", erst="cut"),
    *redet("KL_bittet", KX, BR, FR, "k2", "v4"),
    name("KL", KX, "trick", bis="v4"),
    kamera(1590, 760, 90, beim("k2", "durchschauen"), bis="v4"),
    blase("sprech", 520, 200, "k2", 1560, 230, inhalt=["Darf ich mal kurz", "durchschauen?"], textsize=34,
          figur=KLb2, bis="v4"),
    szene(ficon("tabler", "door-exit", 1820, BR, 120, "v4", fuell=WEISS), "047glocke*", 0.8),
    *fig("KL", KXW, BR, FR, [("v4", "entschlossen_r"), ("wille", "froh_r")], erst="cut"),
    name("KL", KXW, "v4"),
    kamera(1730, 800, 70, "v4"),
    pl("rennt hinaus", 1700, PY, beim("v4", "rennt"), fill=PINK, size=26, anker="m"),
])

# I Erpressung, §§ 253, 255 --------------------------------------------------------------------------------------------
folie([("p253", f"{PB} › Erpressung, § 253 StGB"), ("v7", f"{PB} › Erpressung, § 253 StGB › Variante 6"),
       ("p255", f"{PB} › räuberische Erpressung, § 255 StGB")], [
    *tafel("p253", "Erpressung, §§ 253, 255 StGB"),
    z("Nötigung: Gewalt oder Drohung mit empfindlichem Übel", 110, 185, beim("p253", "Gewalt"), "Bold", 33),
    z("zu einer Handlung, Duldung oder Unterlassung", 150, 237, beim("p253", "Handlung"), size=33),
    z("dadurch Vermögensnachteil", 150, 289, "nacht", size=33),
    z("Absicht, sich zu Unrecht zu bereichern", 150, 341, beim("nacht", "bereichern"), size=33),
    z("Variante 6: erfundene Vorwürfe im Internet angedroht", 110, 420, "v7", "Bold", 34),
    z("Dagmar verkauft die Kamera für 10 €", 150, 472, "v7b", size=34),
    ok(135, 553, "v7ok", gr=22), z("empfindliches Übel, verwerflich: § 253", 175, 530, "v7ok", "Bold", 36),
    blk(110, 610, 1040, 120, BLAU, "p255", [("§ 255: Gewalt gegen eine Person oder Drohung", "ExtraBold", 33, INK),
                                            ("mit Gefahr für Leib oder Leben", "ExtraBold", 33, INK)]),
    z("gleich einem Räuber bestraft: räuberische Erpressung", 110, 755, beim("p255", "gleich"), "Bold", 34),
    *minikarte("p253", [("253", beim("p253", "Erpressung")), ("255", beim("p255", "Paragraf"))]),
    *paar("p253", [("p253", "ruhig_r"), ("v7", "sorge_r"), ("v7b", "erschrickt_r"), ("p255", "denkt")],
          [("p253", "ruhig"), ("v7", "veraechtlich"), ("v7b", "froh"), ("p255", "denkt")]),
    ficon("tabler", "world-www", 1590, 720, 80, "v7", fuell=WEISS, bis="p255"),
    pl("erfundene Vorwürfe", 1590, PY, beim("v7", "erfundenen"), fill=PINK, size=26, anker="m", bis="v7b"),
    pl("Kamera für 10 €", 1590, PY, "v7b", fill=GELB, size=26, anker="m", bis="p255"),
    kamera(1660, 800, 70, beim("v7b", "verkauft"), bis="p255"),
])

# J Streit Raub / räuberische Erpressung ------------------------------------------------------------------------------
SL, SR_, SW = 110, 645, 505
folie([("streit", "Streit › Raub oder räuberische Erpressung? › Variante 7"),
       ("rspr", "Streit › Raub oder räuberische Erpressung? › Rechtsprechung"),
       ("lehre", "Streit › Raub oder räuberische Erpressung? › Lehre")], [
    *tafel("streit", "Raub oder räuberische Erpressung?", size=42),
    z("Variante 7: Drohung mit Schlägen, Dagmar reicht die Kamera", 110, 175, "v6", "Bold", 31),
    blk(SL, 235, SW, 64, BLAU, "rspr", [("Rechtsprechung (BGH)", "ExtraBold", 32, INK)]),
    z("äußeres Erscheinungsbild:", SL + 10, 315, beim("rspr", "äußeren"), "Bold", 30, rechts=SL + SW),
    z("Täter nimmt: Raub", SL + 10, 357, beim("rspr", "Nimmt"), size=30, rechts=SL + SW),
    z("Opfer gibt: räub. Erpressung", SL + 10, 399, beim("rspr", "gibt"), size=30, rechts=SL + SW),
    zitat("BGH 6 StR 44/23, Rn. 5; 5 StR 606/17, Rn. 13", SL + 10, 445, beim("rspr", "Erpressung"), size=22, rechts=SL + SW),
    z("keine Vermögensverfügung nötig,", SL + 10, 492, "rspr2", size=30, rechts=SL + SW),
    z("Raub = Sonderfall der Erpressung", SL + 10, 534, beim("rspr2", "Sonderfall"), size=30, rechts=SL + SW),
    zitat("BGHSt 41, 123, Rn. 12, 14", SL + 10, 580, beim("rspr2", "Erpressung"), size=22, rechts=SL + SW),
    ok(SL + 30, 650, "v6ok", gr=20), z("Variante 7: § 255", SL + 64, 628, "v6ok", "ExtraBold", 33, rechts=SL + SW),
    blk(SR_, 235, SW, 64, LILA, "lehre", [("Lehre (wohl überwiegend)", "ExtraBold", 32, INK)]),
    z("Vermögensverfügung nötig", SR_ + 10, 315, beim("lehre", "Vermögensverfügung"), "Bold", 30),
    z("jedes willentliche Geben:", SR_ + 10, 375, "lehre2", size=30),
    z("auch räub. Erpressung", SR_ + 10, 417, beim("lehre2", "räuberischen"), size=30),
    z("Schlüsselstellung?", SR_ + 10, 485, "schl", "Bold", 30),
    z("Glaubt Dagmar, Klaus bekommt", SR_ + 10, 527, beim("schl", "Glaubt"), size=30),
    z("sie ohnehin: Geben = Wegnahme", SR_ + 10, 569, beim("schl", "Geben"), size=30),
    pl("es bleibt beim Raub", SR_ + 10, 628, "schl2", fill=PINK, size=30),
    *minikarte("streit", [("249", "streit"), ("255", "streit")]),
    *paar("streit", [("streit", "erschrickt_r"), ("v6", "sorge_r"), ("rspr", "denkt"), ("lehre", "skeptisch")],
          [("streit", "entschlossen"), ("v6", "veraechtlich"), ("rspr", "denkt")]),
    kamera(1600, 770, 80, "v6"),
    pl("Dagmar reicht die Kamera", 1590, PY, beim("v6", "reicht"), fill=WEISS, size=26, anker="m"),
])

# K Untreue, § 266 ------------------------------------------------------------------------------------------------------
folie([("p266", f"{PB} › Untreue, § 266 StGB")], [
    *tafel("p266", "Untreue, § 266 StGB"),
    blk(110, 190, 1040, 80, GELB, "p266b", [("nur mit Vermögensbetreuungspflicht", "ExtraBold", 36, INK)]),
    zitat("BGH, Urt. v. 25.4.2024 – 4 StR 456/22, Rn. 28", 110, 290, beim("p266b", "obliegt")),
    z("z. B. ein Vermögensverwalter, der das Geld", 110, 370, "p266c", size=35),
    z("seiner Kundin für sich ausgibt", 150, 422, beim("p266c", "Kundin"), size=35),
    ficon("tabler", "briefcase", 1060, 480, 90, "p266c", fuell=GELB),
    nein(135, 543, "p266d", gr=20), z("Klaus betreut Dagmars Vermögen nicht", 175, 520, "p266d", "Bold", 36),
    *minikarte("p266", [("266", beim("p266", "Untreue"))]),
    *paar("p266", [("p266", "ruhig"), ("p266d", "froh")], [("p266", "ruhig"), ("p266c", "denkt")]),
])

# L Klausurtipp (Lexi) --------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · Streit nur entscheiden, wo er sich auswirkt")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Streit nur entscheiden, wo er sich auswirkt", 200, 200, beim("tipp", "Entscheide"), "Bold", 36),
    z("Täter nimmt mit Zueignungsabsicht:", 110, 290, "tipp2", size=34),
    z("alle Ansichten: Raub", 150, 342, beim("tipp2", "alle"), "Bold", 34),
    blk(110, 420, 1040, 120, GELB, "tipp3", [("unter Drohung genommen, nur ein Wochenende", "ExtraBold", 33, INK),
                                              ("benutzen: keine Zueignungsabsicht", "ExtraBold", 33, INK)]),
    z("BGH: räuberische Erpressung, wenn Klaus sich", 110, 575, "tipp4", size=34),
    z("durch den Gebrauch bereichern will", 150, 627, beim("tipp4", "Gebrauch"), size=34),
    zitat("BGH, Beschl. v. 3.4.2024 – 1 StR 75/24, Rn. 9", 150, 679, beim("tipp4", "bereichern")),
    z("Lehre: keine Vermögensverfügung", 110, 740, beim("tipp4", "Lehre"), "Bold", 34),
    *redet("LX_warnt", LXX, BR, FR + 60, "tipp", "sch"),
    pl("Lexi", LXX, BR + 22, "tipp", fill=GELB, size=30, anker="m", d=0.0),
    kamera(1760, 500, 80, beim("tipp3", "Wochenende")),
    pl("nur ein Wochenende", 1740, 520, beim("tipp3", "Wochenende"), fill=WEISS, size=26, anker="m"),
])

# M Entscheidungsbaum ---------------------------------------------------------------------------------------------------
QX, RX = 130, 1110
BAUM = [  # (Frage, cue, Ergebnisse [(Text, cue, Größe)])
    ("1. Nimmt der Täter die Sache?", "e1", [("Diebstahl, § 242", "e1a", 36), ("Gewalt/Drohung Leib, Leben: Raub, § 249", "e1b", 32)]),
    ("2. Hat er sie schon und eignet sie sich zu?", "e2", [("Unterschlagung, § 246", beim("e2", "Dann"), 36)]),
    ("3. Gibt das Opfer?", "e3", [("getäuscht: Betrug, § 263", "e3a", 36), ("genötigt: Erpressung, § 253", "e3b", 36),
                                  ("Gewalt/Drohung Leib, Leben: § 255", "e3c", 32)]),
    ("4. Betreut der Täter fremdes Vermögen?", "e4", [("Untreue, § 266", beim("e4", "Dann"), 36)]),
]
baum, yb = [], 200
for frage_, cq, erg in BAUM:
    qe = QX + F("ExtraBold", 36).getlength(frage_)
    assert qe + 30 < RX - 110, f"Frage zu lang: {frage_}"
    baum.append(z(frage_, QX, yb, cq, "ExtraBold", 36, rechts=RX - 100))
    baum.append(pfeil_ink(RX - 110, yb + 24, RX - 20, yb + 24, erg[0][1]))
    for j, (t_, c_, g_) in enumerate(erg):
        baum.append(z(t_, RX, yb + j * 54, c_, "Bold", g_, rechts=1820))
    yb += 54 * len(erg) + 52
folie([("sch", "Entscheidungsbaum")], [
    karte(60, 50, 1800, 900, "sch"),
    titel("Entscheidungsbaum: Vermögensdelikte", 110, 90, "sch", 50),
    *baum,
])

# N Merksatz (Lexi) -----------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 170, "merke", 84, anker="m"),
    *markertext([[("Nehmen", "a"), (" ist Diebstahl, mit Gewalt", 0)], [("oder Drohung für Leib, Leben: Raub.", 0)]],
                750, 300, 42, "merke", {"a": beim("merke", "Nehmen")}),
    *markertext([[("Geben", "b"), (" nach Täuschung ist Betrug,", 0)], [("unter Zwang Erpressung.", 0)]], 750, 470, 42, "m2",
                {"b": beim("m2", "Geben")}),
    *markertext([[("Wer schon hat", "c"), (" und sich zueignet,", 0)], [("begeht Unterschlagung.", 0)]], 750, 640, 42, "m3",
                {"c": beim("m3", "schon")}),
    *redet("LX_erklaert", 1680, 990, 700, "merke", lexi_bis_ende("merke")),
    pl("Lexi", 1680, 1000, "merke", fill=GELB, size=28, anker="m", d=0.0),
])

# Zeichenprüfung für alle übrigen Texte (Pfade, Blöcke, Titel, Blasen, Sachverhalt)
for f_ in FOLIEN:
    for _, t_ in f_["pfade"]:
        glyphen(t_)
    for e_ in f_["els"]:
        n_ = e_.name or ""
        if n_.startswith(("block:", "titel:", "pille:", "blase:")):
            glyphen(n_.split(":", 1)[1].replace("(", "").replace(")", "").replace("'", ""))
        elif not n_.startswith(("bild:", "ficon:", "icon:", "karte", "linie", "pfeil", "ring", "marker", "haken", "kreuz")):
            glyphen(n_)
