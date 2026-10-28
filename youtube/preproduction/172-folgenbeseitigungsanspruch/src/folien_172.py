"""Folge 172 · Folgenbeseitigungsanspruch: Die Stadt pflastert deinen Vorgarten – Serienstandard Open Peeps (Katzenkönig).
Übungsfall: Beim Ausbau des Gehwegs pflastern Bauarbeiter der (namenlosen) Gemeinde versehentlich einen 30 cm breiten
Streifen von Ottilies Vorgarten mit; Herr Wernicke vom Bauamt bietet Geld an, Ottilie will den Vorgarten zurück.
Szenen laut ../SZENENPLAN.md: A Fall (Vorgarten, Gehweg, Haus; Gespräch, Frage), B Sachverhalt, C Einordnung, D1 I. ungeschrieben/
Herleitung, D2 Art. 20 Abs. 3 GG (Wortlaut), E1 Art. 14 Abs. 1 GG (Wortlaut), E2 § 113 Abs. 1 Satz 2 VwGO (Wortlaut,
Herleitungsstreit), F II. Überblick (vier Farben), G1 1. hoheitlicher Eingriff, G2 2. subjektives Recht, H 3. rechtswidriger
Zustand/Radweg-Fall, I 4. Wiederherstellung möglich/zumutbar, J1 III. Rechtsfolge, J2 Kontrast Amtshaftung (Art. 34 Satz 1 GG,
Wortlaut), K Mitverschulden, L Prozessuales, M1 Lösung, M2 zurück im Vorgarten, N Klausurtipp (Lexi), O Schema, P Merksatz.
Bauarbeiter ruhig, keine Gewalt; keine echten Gemeinden oder Wappen.
Handlungsgeräusche: Pflasterstein beim Pflastern des Streifens, Schaufel beim Entfernen (../geraeusche_herkunft.json).
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/hand/okz/
neinz als eigene Kopie aus Folge 170 (gemeinsame Dateien unverändert); neu: boden_bild(), haus(), rosen(), Farbschema der vier
Voraussetzungen. Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_172/"

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
HELLROT = (250, 205, 198, 255)
HELLGRUEN = (214, 240, 214, 255)
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
    """Rechtstafel links, rechts bleibt Platz für die Figuren; frei = rechte Grenze des Titels (Rechenleiste)."""
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
    """Figuren und Requisiten der Tafelfolien stehen rechts der Tafel (Diagramm-Icons des Zeitstrahls ausgenommen)."""
    for e in els:
        n = e.name or ""
        if n.startswith(("bild:", "ficon:")) or "/op_172/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def dicon(*a, **k):
    """Icon als Teil eines Diagramms innerhalb der Tafel (Zeitstrahl), nicht als Requisit."""
    e = ficon(*a, **k)
    e.name = "diagramm:" + (e.name or "")
    return e


def wortlaut(x, y, w, zeilen, quelle, cue, marken=(), size=32, bis=None):
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de, als Zitat mit Normangabe;
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 027/073/083/103) --------------------------------
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


def hand(name, cx, unten, hoehe, seite):
    """Äußerster Punkt der Figur (Hand) im Band 40–62 % der Höhe; seite = -1 links, +1 rechts."""
    e = peep_voll(name, cx, unten, hoehe, "_")
    a = np.asarray(e.sprite)[:, :, 3] > 40
    h = a.shape[0]
    band = a[int(h * 0.40):int(h * 0.62)]
    ys, xs = np.nonzero(band)
    i = xs.argmin() if seite < 0 else xs.argmax()
    return int(e.x + xs[i]), int(e.y + int(h * 0.40) + ys[i])


def okz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Haken davor (zur gesprochenen Bejahung)."""
    return [ok(x - 45, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]


def neinz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Kreuz davor (zur gesprochenen Verneinung)."""
    return [nein(x - 45, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]



def punkt(cx, cy, cue, farbe=ROT, r=11):
    im = Image.new("RGBA", (2 * r + 8, 2 * r + 8))
    ImageDraw.Draw(im).ellipse((4, 4, 2 * r + 4, 2 * r + 4), fill=farbe, outline=INK, width=4)
    return El(im, cx - r - 4, cy - r - 4, cue, "pop", 0.0, None, name="punkt")





BODEN, FH = 860, 480
X1, X2 = 1420, 1720                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
OT_N, WE_N, BA_N = ROT, TUERKIS, ORANGE     # Farben der Namensschilder
PX, PY, PU = 1570, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"OT": "Ottilie", "WE": "Herr Wernicke"}
NFARBE = {"OT": OT_N, "WE": WE_N}
F1, F2, F3, F4 = BLAU, GRUEN, LILA, GELB     # eigene Farbe je Voraussetzung
OX, WX, BX = 1250, 560, 260                 # Fallszene: Ottilie (im Garten), Herr Wernicke, Bauarbeiter (Gehweg)
GRENZE, STR_ENDE, HAUS0 = 780, 900, 1500    # Grundstücksgrenze, Ende des 30-cm-Streifens (überzeichnet), Haus
PFL = (198, 198, 206, 255); ALT = (222, 222, 226, 255); KIES = (232, 214, 170, 255); ERDE = (170, 122, 82, 255)
ASPH = (120, 120, 128, 255)


def boden_bild(cue, gehweg="alt", streifen="gras", bis=None):
    """Boden der Fallszene (programmatisch aus Grundformen): Fahrbahn, Bordstein, Gehweg (alt/kies/pflaster),
    Grenzstein, Streifen des Vorgartens (gras/pflaster/erde), Vorgarten (Gras)."""
    s, x0, y0, w, h = 2, 40, 852, 1840, 60
    im = Image.new("RGBA", (w * s, h * s)); dr = ImageDraw.Draw(im)
    X = lambda x: (x - x0) * s
    top, bot = 8 * s, h * s - 4

    def flaeche(a, b, fill):
        dr.rectangle((X(a), top, X(b), bot), fill=fill)

    def pflaster(a, b):
        flaeche(a, b, PFL)
        bw, bh = 44 * s, 16 * s
        for r, yy in enumerate(range(top, bot, bh)):
            xx = X(a) - (bw // 2 if r % 2 else 0)
            while xx < X(b):
                dr.rectangle((max(xx, X(a)), yy, min(xx + bw, X(b)), min(yy + bh, bot)), outline=INK, width=2 * s)
                xx += bw

    flaeche(40, 200, ASPH)
    if gehweg == "alt":
        flaeche(222, GRENZE, ALT)
        for xx in range(222, GRENZE, 140):
            dr.line((X(xx), top, X(xx), bot), fill=INK, width=2 * s)
    elif gehweg == "kies":
        flaeche(222, GRENZE, KIES)
        import random
        rnd = random.Random(172)
        for _ in range(260):
            px, py = rnd.uniform(X(226), X(GRENZE - 6)), rnd.uniform(top + 6, bot - 6)
            dr.ellipse((px - 3 * s, py - 2 * s, px + 3 * s, py + 2 * s), fill=(180, 160, 120, 255))
    else:
        pflaster(222, GRENZE)
    if streifen == "pflaster":
        pflaster(GRENZE, STR_ENDE)
    elif streifen == "erde":
        flaeche(GRENZE, STR_ENDE, ERDE)
    else:
        flaeche(GRENZE, STR_ENDE, GRUEN)
    flaeche(STR_ENDE, 1880, GRUEN)
    dr.rectangle((X(200), 0, X(222), bot), fill=WEISS, outline=INK, width=3 * s)          # Bordstein
    dr.line((0, top, w * s, top), fill=INK, width=5 * s)
    dr.rectangle((0, top, w * s - 1, bot), outline=INK, width=3 * s)
    im = im.resize((w, h), Image.LANCZOS)
    return El(im, x0, y0, cue, "cut", 0.0, bis, name="boden")


def grenzstein(cue):
    """Grenzstein an der Grundstücksgrenze (Grundform) mit gestrichelter Grenzlinie."""
    im = Image.new("RGBA", (24, 200)); dr = ImageDraw.Draw(im)
    for y in range(0, 160, 22):
        dr.line((12, y, 12, y + 12), fill=INK, width=3)
    dr.rectangle((2, 168, 22, 198), fill=WEISS, outline=INK, width=3)
    return El(im, GRENZE - 12, 690, cue, "cut", 0.0, None, name="grenzstein")


def haus(cue):
    """Ottilies Haus (Grundformen: Wand, Satteldach, Tür, Fenster; Palettenflächen, Tuschekontur)."""
    s = 2; w, h = 400, 500
    im = Image.new("RGBA", (w * s, h * s)); dr = ImageDraw.Draw(im)
    dach = 150
    dr.rectangle((30 * s, dach * s, (w - 30) * s, (h - 4) * s), fill=WEISS, outline=INK, width=5 * s)
    dr.polygon([(6 * s, (dach + 4) * s), (w * s // 2, 8 * s), ((w - 6) * s, (dach + 4) * s)], fill=ROT)
    dr.line([(6 * s, (dach + 4) * s), (w * s // 2, 8 * s), ((w - 6) * s, (dach + 4) * s), (6 * s, (dach + 4) * s)], fill=INK,
            width=6 * s, joint="curve")
    dr.rectangle((70 * s, 300 * s, 160 * s, (h - 4) * s), fill=GELB, outline=INK, width=5 * s)                 # Tür
    dr.rectangle((220 * s, 220 * s, 330 * s, 320 * s), fill=BLAU, outline=INK, width=5 * s)                    # Fenster
    dr.line((275 * s, 220 * s, 275 * s, 320 * s), fill=INK, width=4 * s)
    im = im.resize((w, h), Image.LANCZOS)
    return El(im, HAUS0 - 20, BODEN - h + 4, cue, "cut", 0.0, None, name="haus")


ROSEN_STR = [810, 868]
ROSEN_GART = [960, 1040, 1120, 1440]


def rosen(xs, cue, bis=None, anim="cut"):
    return [ficon("fluent-emoji-high-contrast", "rose", x, BODEN + 2, 64, cue, fuell=ROT, nebenfarbe=GRUEN, bis=bis, anim=anim)
            for x in xs]


def requisit(folge):
    """Wechselndes Requisit über den Figuren: folge = [(cue, (set, icon, breite, fuell), pillentext, pillenfarbe)]."""
    els = []
    for i, (c, ic, txt, pf) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else None
        if ic:
            s_, n_, br, fu = ic
            els.append(ficon(s_, n_, PX, PU, br, c, fuell=fu, bis=b))
        if txt:
            els.append(pl(txt, PX, PY, c, fill=pf, size=28, anker="m", bis=b))
    return els


def paar(c0, of, wf):
    """Tafelszene: Ottilie und Herr Wernicke rechts der Tafel, beide blicken zur Tafel (nach links)."""
    return [*fig("OT", X1, FB, FR, of), ns(NAME["OT"], X1, FB, c0, OT_N, d=0.1),
            *fig("WE", X2, FB, FR, wf, d=0.2), ns(NAME["WE"], X2, FB, c0, WE_N, d=0.3)]


def nummer(n, x, y, cue, farbe, gr=60):
    """Farbiges Nummernfeld einer Voraussetzung (1–4)."""
    return [karte(x, y, gr, gr, cue, fill=farbe, rund=12, schatten=4, rand=4),
            z(n, x + gr / 2 - F("ExtraBold", 36).getlength(n) / 2, y + gr / 2 - 25, cue, "ExtraBold", 36)]


def ptitel(cue, n, text, farbe, size=46):
    """Tafel mit farbigem Nummernfeld vor dem Titel (Voraussetzung n)."""
    return [karte(60, 60, 1140, 840, cue), *nummer(n, 105, 92, cue, farbe, gr=66),
            titel(glyphen(text), 195, 100, cue, size)]


def fall_figuren(teil):
    """Figuren der Fallszene: teil = Liste der Mimikfolgen je Person."""
    return teil


# ===========================================================================================================================
# A Fall: der Gehweg wird ausgebaut, Gespräch am Gartenrand, Frage
# ===========================================================================================================================
BAU = "bau"
STR = beim("streifen", "pflastern")
WEIN = beim("rosen", "Wo")
folie([(NULL, "Fall · Der Gehweg wird ausgebaut"), ("ot1", "Fall · Am Gartenrand"), ("frage", "Fall · Die Frage")], [
    boden_bild(NULL, "alt", "gras", bis=BAU), boden_bild(BAU, "kies", "gras", bis=STR), boden_bild(STR, "pflaster", "pflaster"),
    hart(haus(NULL)), hart(grenzstein(NULL)),
    *rosen(ROSEN_STR, NULL, bis=STR), *rosen(ROSEN_GART, NULL),
    pl("Vorgarten mit Rosen", 70, 30, beim("fall", "Vorgarten"), fill=GRUEN, size=36, bis="frage"),
    pl("Die Gemeinde baut den Gehweg aus", 70, 110, BAU, fill=WEISS, size=36, bis="frage"),
    ficon("tabler", "barrier-block", 120, BODEN - 2, 110, BAU, fuell=ORANGE),
    szene(pl("30 cm mitgepflastert", 70, 190, STR, fill=ROT, size=36, bis="frage"), "172pflaster*", 0.6, 0.0),
    pl("30 cm", (GRENZE + STR_ENDE) / 2, 728, STR, fill=WEISS, size=28, anker="m", bis="frage"),
    pl("Wo Rosen standen: Pflaster", 70, 270, WEIN, fill=WEISS, size=36, bis="frage"),
    ficon("fluent-emoji-high-contrast", "wilted-flower", 840, BODEN + 2, 56, WEIN, fuell=ROT, nebenfarbe=GRUEN, bis="frage"),
    # Ottilie im Vorgarten (blickt nach links zum Gehweg)
    *fig("OT", OX, BODEN, FH, [(NULL, "ruhig"), (STR, "staunt"), (WEIN, "sorge")], bis="ot1", erst="cut"),
    hart(ns("Ottilie", OX, BODEN, NULL, OT_N)),
    *redet("OT_redet", OX, BODEN, FH, "ot1", "we1"),
    peep_voll("OT_denkt", OX, BODEN, FH, "we1", anim="cut", bis="ot2"),
    *redet("OT_bestimmt", OX, BODEN, FH, "ot2", "frage"),
    peep_voll("OT_ernst", OX, BODEN, FH, "frage", anim="cut"),
    blase("sprech", 600, 230, "ot1", 1580, 215, inhalt=["Herr Wernicke, das ist", "mein Vorgarten! Die Steine",
                                                        "müssen wieder weg."], textsize=33, figur=("OT_redet", OX, BODEN, FH), bis="we1"),
    blase("sprech", 560, 210, "ot2", 1580, 215, inhalt=["Ich will kein Geld.", "Ich will meinen",
                                                        "Vorgarten zurück."], textsize=34, figur=("OT_bestimmt", OX, BODEN, FH), bis="frage"),
    # Bauarbeiter auf dem Gehweg (blickt nach rechts zum Streifen)
    *fig("BA", BX, BODEN, FH, [(BAU, "ruhig_r"), (STR, "froh_r"), (WEIN, "sorge_r")]),
    ns("Bauarbeiter", BX, BODEN, BAU, BA_N, d=0.1),
    # Herr Wernicke vom Bauamt kommt dazu (blickt nach rechts zu Ottilie)
    *fig("WE", WX, BODEN, FH, [(WEIN, "ruhig_r"), ("ot1", "verlegen_r")], bis="we1"),
    ns("Herr Wernicke", WX, BODEN, WEIN, WE_N, d=0.1),
    *redet("WE_redet_r", WX, BODEN, FH, "we1", "ot2"),
    *fig("WE", WX, BODEN, FH, [("ot2", "verlegen_r"), ("frage", "denkt_r")], erst="cut"),
    blase("sprech", 560, 210, "we1", 960, 290, inhalt=["Das war ein Versehen.", "Ich kann Ihnen dafür",
                                                       "Geld anbieten."], textsize=34, figur=("WE_redet_r", WX, BODEN, FH), bis="ot2"),
    pl("Kann Ottilie verlangen, dass die Gemeinde das Pflaster entfernt", 70, 30, "frage", fill=PINK, size=34),
    pl("und den Vorgarten wiederherstellt?", 70, 115, "frage2", fill=PINK, size=34),
])
_hx, _hy = hand("BA_ruhig_r", BX, BODEN, FH, +1)
FOLIEN[-1]["els"].append(ficon("tabler", "trowel", _hx + 26, _hy + 30, 60, BAU, fuell=WEISS))


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_172(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=34, zeilenabstand=1.30)
        els += e; y += 18
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_172("sv", [
    "Ottilie hat vor ihrem Haus einen kleinen Vorgarten mit Rosen. Die Gemeinde baut den Gehweg davor aus. Dabei pflastern "
    "die Bauarbeiter versehentlich einen 30 cm breiten Streifen ihres Vorgartens mit. Wo vorher Rosen standen, liegen jetzt "
    "Pflastersteine.",
    "Eine Einwilligung von Ottilie, eine Widmung oder eine Enteignung gibt es nicht. Herr Wernicke vom Bauamt der Gemeinde "
    "spricht von einem Versehen und bietet Ottilie Geld an. Ottilie will kein Geld, sondern ihren Vorgarten zurück.",
], "Kann Ottilie verlangen, dass die Gemeinde das Pflaster entfernt und den Vorgarten wiederherstellt?")

# ===========================================================================================================================
# C Einordnung
# ===========================================================================================================================
folie([("einord", "Einordnung › Kontrast: § 1004 BGB"), ("hoheit", "Einordnung › hoheitliches Handeln"),
       ("stsh", "Einordnung › Staatshaftungsrecht")], rechts_frei([
    *tafel("einord", "Einordnung"),
    z("Unter Privaten:", 110, 185, beim("einord", "Unter"), "Bold", 36),
    z("Beseitigungsanspruch, § 1004 BGB", 150, 240, beim("einord", "Beseitigungsanspruch"), size=36),
    blk(110, 310, 1040, 80, LILA, beim("einord", "dazu"), [("Mehr dazu: Video „Beseitigungsanspruch § 1004 BGB“", "ExtraBold", 32, INK)]),
    linienzug([(110, 430), (1150, 430)], "hoheit", breite=3),
    *okz("Hier: Die Gemeinde baut hoheitlich", 465, beim("hoheit", "hoheitlich"), "Bold", 36, x=160),
    blk(110, 560, 1040, 90, F1, beim("fba", "Folgenbeseitigungsanspruch"), [("Folgenbeseitigungsanspruch", "ExtraBold", 40, INK)]),
    z("ein Teil des Staatshaftungsrechts", 110, 690, "stsh", size=36),
    *requisit([("einord", ("tabler", "users", 110, WEISS), "unter Privaten", WEISS),
               ("hoheit", ("tabler", "building-bank", 100, BLAU), "die Gemeinde", BLAU),
               (beim("fba", "Folgenbeseitigungsanspruch"), ("tabler", "arrow-back-up", 100, GRUEN), "Folgenbeseitigung", GRUEN),
               ("stsh", ("tabler", "scale", 100, WEISS), "Staatshaftungsrecht", WEISS)]),
    *paar("einord", [("einord", "ruhig"), ("hoheit", "denkt")], [("einord", "ruhig"), ("hoheit", "ernst")]),
]))

# ===========================================================================================================================
# D1 I. Rechtsgrundlage: ungeschrieben, Herleitung
# ===========================================================================================================================
folie([("rg", "I. Rechtsgrundlage › ungeschrieben"), ("herl", "I. Rechtsgrundlage › Grundrechte, Rechtsstaatsprinzip")],
      rechts_frei([
    *tafel("rg", "I. Rechtsgrundlage"),
    *neinz("steht in keinem Gesetz", 185, beim("rg", "Gesetz"), "Bold", 36, x=160),
    *okz("in ständiger Rechtsprechung anerkannt", 260, beim("stRspr", "ständiger"), "Bold", 36, x=160),
    z("oft spricht man von Gewohnheitsrecht", 160, 315, beim("stRspr", "Gewohnheitsrecht"), size=34),
    z("BVerwG verankert ihn in:", 110, 410, beim("herl", "verankert"), "Bold", 36),
    blk(110, 480, 500, 90, F2, beim("herl", "Grundrechten"), [("Grundrechten", "ExtraBold", 38, INK)]),
    blk(650, 480, 500, 90, F1, beim("herl", "Rechtsstaatsprinzip"), [("Rechtsstaatsprinzip", "ExtraBold", 38, INK)]),
    zit("BVerwG, Urt. v. 29.7.2015 – 6 C 35.14, Rn. 8;", 110, 610, beim("herl", "Rechtsstaatsprinzip")),
    zit("Urt. v. 19.2.2015 – 1 C 13.14, Rn. 25", 110, 650, beim("herl", "Rechtsstaatsprinzip")),
    *requisit([("rg", ("tabler", "file-off", 100, WEISS), "in keinem Gesetz", WEISS),
               ("stRspr", ("tabler", "gavel", 100, WEISS), "ständige Rechtsprechung", WEISS),
               ("herl", ("tabler", "building-bank", 100, GELB), "Bundesverwaltungsgericht", GELB)]),
    *paar("rg", [("rg", "ruhig"), ("stRspr", "denkt")], [("rg", "ruhig"), ("herl", "denkt")]),
]))

# ===========================================================================================================================
# D2 Art. 20 Abs. 3 GG (Wortlaut)
# ===========================================================================================================================
W20 = ["„(3) Die Gesetzgebung ist an die verfassungsmäßige Ordnung,",
       "die vollziehende Gewalt und die Rechtsprechung sind an",
       "Gesetz und Recht gebunden.“"]
w20, w20_y = wortlaut(80, 180, 1100, W20, "Art. 20 Abs. 3 GG", beim("w20", "Artikel"), marken=[
    (1, "die vollziehende Gewalt", beim("w20", "vollziehende")), (2, "Gesetz und Recht gebunden", beim("w20", "Gesetz", 2))], size=33)
folie([("w20", "I. Rechtsgrundlage › Rechtsstaatsprinzip, Art. 20 Abs. 3 GG")], rechts_frei([
    *tafel("w20", "I. Rechtsstaatsprinzip"),
    *w20,
    blk(110, w20_y + 60, 1040, 90, F1, "w20b", [("Verwaltung rechtswidrig: Folgen beseitigen", "ExtraBold", 36, INK)]),
    *requisit([("w20", ("tabler", "book", 100, WEISS), "Art. 20 Abs. 3 GG", WEISS),
               ("w20b", ("tabler", "arrow-back-up", 100, BLAU), "Folgen beseitigen", BLAU)]),
    *paar("w20", [("w20", "ruhig"), ("w20b", "froh")], [("w20", "ruhig"), ("w20b", "verlegen")]),
]))

# ===========================================================================================================================
# E1 Art. 14 Abs. 1 Satz 1 GG (Wortlaut)
# ===========================================================================================================================
W14 = ["„(1) Das Eigentum und das Erbrecht werden gewährleistet. …“"]
w14, w14_y = wortlaut(80, 240, 1100, W14, "Art. 14 Abs. 1 Satz 1 GG", beim("w14", "Artikel"), marken=[
    (0, "Eigentum", beim("w14", "Eigentum")), (0, "gewährleistet", beim("w14", "gewährleistet"))], size=34)
folie([("w14", "I. Rechtsgrundlage › Grundrecht, Art. 14 Abs. 1 GG")], rechts_frei([
    *tafel("w14", "I. Grundrecht: Eigentum"),
    z("das betroffene Grundrecht", 110, 175, "w14", "Bold", 34),
    *w14,
    blk(110, w14_y + 60, 1040, 90, F2, "abwehr", [("Abwehrrecht: auch gegenüber dem Staat", "ExtraBold", 36, INK)]),
    zit("BVerwG, Beschl. v. 12.7.2013 – 9 B 12.13, Rn. 4", 110, w14_y + 180, "abwehr"),
    *requisit([("w14", ("tabler", "home", 110, GRUEN), "das Eigentum", GRUEN),
               ("abwehr", ("tabler", "shield-check", 100, GRUEN), "Abwehrrecht", GRUEN)]),
    *paar("w14", [("w14", "ruhig"), ("abwehr", "froh")], [("w14", "ruhig"), ("abwehr", "denkt")]),
]))

# ===========================================================================================================================
# E2 § 113 Abs. 1 Satz 2 VwGO (Wortlaut), Herleitungsstreit, kein Verwaltungsakt
# ===========================================================================================================================
W113 = ["„Ist der Verwaltungsakt schon vollzogen, so kann das Gericht",
        "auf Antrag auch aussprechen, daß und wie die",
        "Verwaltungsbehörde die Vollziehung rückgängig zu machen hat.“"]
w113, w113_y = wortlaut(80, 180, 1100, W113, "§ 113 Abs. 1 Satz 2 VwGO", beim("w113", "Paragraf"), marken=[
    (0, "vollzogen", beim("w113", "vollzogen")), (2, "rückgängig zu machen", beim("w113", "rückgängig"))], size=32)
folie([("w113", "I. Rechtsgrundlage › § 113 Abs. 1 Satz 2 VwGO"), ("streit", "I. Rechtsgrundlage › Herleitungsstreit"),
       ("keinva", "I. Rechtsgrundlage › kein Verwaltungsakt")], rechts_frei([
    *tafel("w113", "I. § 113 Abs. 1 Satz 2 VwGO"),
    *w113,
    z("Anspruch daraus? umstritten", 110, w113_y + 30, "streit", "Bold", 34),
    *okz("BVerwG: prozessuales Mittel für den Anspruch", w113_y + 90, beim("prozess", "prozessuales"), size=34, x=160),
    zit("BVerwG, Beschl. v. 2.12.2015 – 6 B 33.15, Rn. 14", 160, w113_y + 140, beim("prozess", "prozessuales")),
    blk(110, w113_y + 190, 1040, 76, LILA, beim("prozess", "dazu"), [("Mehr dazu: Video „Anfechtungsklage“", "ExtraBold", 32, INK)]),
    *neinz("Ottilie: kein Verwaltungsakt", w113_y + 300, beim("keinva", "keinen"), "Bold", 36, x=160),
    *requisit([("w113", ("tabler", "file-text", 100, WEISS), "§ 113 Abs. 1 Satz 2", WEISS),
               ("streit", ("tabler", "arrows-split", 100, WEISS), "umstritten", WEISS),
               ("prozess", ("tabler", "gavel", 100, WEISS), "prozessuales Mittel", LILA),
               ("keinva", ("tabler", "file-off", 100, WEISS), "kein Verwaltungsakt", ROT)]),
    *paar("w113", [("w113", "ruhig"), ("streit", "denkt"), ("keinva", "sorge")], [("w113", "ruhig"), ("prozess", "denkt")]),
]))

# ===========================================================================================================================
# F II. Voraussetzungen im Überblick (vier Farben)
# ===========================================================================================================================
VOR = [("v1", "1", "hoheitlicher Eingriff", F1), ("v2", "2", "in ein subjektives Recht", F2),
       ("v3", "3", "rechtswidriger Zustand, der andauert", F3), ("v4", "4", "Wiederherstellung möglich und zumutbar", F4)]
folie([("vor", "II. Voraussetzungen › Überblick")], rechts_frei([
    *tafel("vor", "II. Voraussetzungen"),
    *[e for k, (c, n, t, fa) in enumerate(VOR) for e in (
        *nummer(n, 120, 200 + k * 140, c, fa, gr=80),
        z(t, 240, 212 + k * 140, c, "Bold", 38))],
    zit("BVerwG, Urt. v. 19.9.2019 – 9 C 5.19, Rn. 13; Beschl. v. 2.12.2015 – 6 B 33.15, Rn. 14", 110, 780, "v4"),
    *requisit([("vor", ("tabler", "checklist", 100, WEISS), "vier Punkte", WEISS),
               ("v1", ("tabler", "shovel", 100, F1), "hoheitlicher Eingriff", F1),
               ("v2", ("tabler", "user-check", 100, F2), "subjektives Recht", F2),
               ("v3", ("tabler", "alert-triangle", 100, F3), "rechtswidriger Zustand", F3),
               ("v4", ("tabler", "restore", 100, F4), "Wiederherstellung", F4)]),
    *paar("vor", [("vor", "ruhig"), ("v3", "denkt")], [("vor", "ruhig"), ("v4", "denkt")]),
]))

# ===========================================================================================================================
# G1 II. 1. Hoheitlicher Eingriff
# ===========================================================================================================================
folie([("a1", "II. 1. hoheitlicher Eingriff"), ("a2", "II. 1. hoheitlicher Eingriff › Realakt"),
       ("a4", "II. 1. hoheitlicher Eingriff › Funktionszusammenhang")], rechts_frei([
    *ptitel("a1", "1", "Hoheitlicher Eingriff", F1),
    z("kein Bescheid: Die Gemeinde hat gebaut", 110, 195, beim("a1", "Bescheid"), size=36),
    blk(110, 265, 1040, 86, F1, beim("a2", "Realakt"), [("Realakt: schlicht-hoheitliches Handeln", "ExtraBold", 36, INK)]),
    *okz("auch das kann ein Eingriff sein", 385, "a3", "Bold", 36, x=160),
    z("hoheitlich: öffentlich-rechtlicher Planungs- und", 110, 465, "a4", size=34),
    z("Funktionszusammenhang", 150, 515, beim("a4", "Funktionszusammenhang"), size=34),
    zit("BVerwG, Beschl. v. 27.5.2015 – 7 B 14.15, Rn. 8", 150, 570, beim("a4", "Funktionszusammenhang")),
    *okz("Gehweg: Straßenbau, öffentliche Aufgabe", 640, beim("a5", "Straßenbau"), "Bold", 36, x=160),
    *requisit([("a1", ("tabler", "file-off", 100, WEISS), "kein Bescheid", WEISS),
               ("a2", ("tabler", "shovel", 100, F1), "Realakt", F1),
               ("a5", ("tabler", "road", 110, WEISS), "Straßenbau", WEISS)]),
    *paar("a1", [("a1", "ruhig"), ("a3", "denkt")], [("a1", "ruhig"), ("a2", "verlegen"), ("a5", "ernst")]),
]))

# ===========================================================================================================================
# G2 II. 2. Subjektives Recht
# ===========================================================================================================================
folie([("b1", "II. 2. subjektives Recht › Eigentum")], rechts_frei([
    *ptitel("b1", "2", "In ein subjektives Recht", F2),
    *okz("Ottilies Eigentum am Vorgarten", 200, beim("b1", "Eigentum"), "Bold", 38, x=160),
    blk(110, 290, 1040, 86, F2, beim("b1", "subjektives"), [("subjektives Recht, Art. 14 Abs. 1 GG", "ExtraBold", 36, INK)]),
    zit("BVerwG, Beschl. v. 27.5.2015 – 7 B 14.15, Rn. 9", 110, 410, beim("b1", "geschützt")),
    *requisit([("b1", ("tabler", "home", 110, GRUEN), "Ottilies Eigentum", GRUEN)]),
    *paar("b1", [("b1", "ruhig"), (beim("b1", "geschützt"), "froh")], [("b1", "ruhig")]),
]))

# ===========================================================================================================================
# H II. 3. Rechtswidriger Zustand, der andauert; Radweg-Fall
# ===========================================================================================================================
folie([("c1", "II. 3. rechtswidriger Zustand › keine Duldungspflicht"), ("c4", "II. 3. rechtswidriger Zustand › dauert an"),
       ("c5", "II. 3. rechtswidriger Zustand › Legalisierung")], rechts_frei([
    *ptitel("c1", "3", "Rechtswidriger Zustand", F3),
    z("Recht, Ottilies Boden zu nutzen?", 110, 190, "c2", "Bold", 36),
    *neinz("Einwilligung", 250, beim("c2", "Einwilligung"), size=34, x=160),
    *neinz("Widmung", 250, beim("c2", "Widmung"), size=34, x=500),
    *neinz("Enteignung", 250, beim("c2", "Enteignung"), size=34, x=800),
    *okz("Ottilie muss das Pflaster nicht dulden", 320, "c3", "Bold", 36, x=160),
    *okz("Pflaster liegt noch da: Zustand dauert an", 390, "c4", "Bold", 36, x=160),
    linienzug([(110, 460), (1150, 460)], "c5", breite=3),
    z("anders, wenn inzwischen legalisiert", 110, 480, "c5", "Bold", 36),
    blk(110, 545, 1040, 80, F3, "c6", [("Radweg der Gemeinde auf Privatgrundstück", "ExtraBold", 34, INK)]),
    z("später: Bebauungsplan weist Radweg aus", 150, 650, "c7", size=34),
    z("vieles spricht gegen die Beseitigung", 150, 700, beim("c7", "vieles"), size=34),
    zit("BVerwG, Urt. v. 19.9.2019 – 9 C 5.19, Rn. 2, 4, 13 f.", 150, 755, "c6"),
    *requisit([("c2", ("tabler", "license", 100, WEISS), "kein Recht zur Nutzung", WEISS),
               ("c4", ("tabler", "hourglass", 90, F3), "dauert an", F3),
               ("c6", ("tabler", "bike", 120, WEISS), "Radweg-Fall", F3),
               ("c7", ("tabler", "map-2", 100, WEISS), "Bebauungsplan", WEISS)]),
    *paar("c1", [("c1", "ruhig"), ("c3", "froh"), ("c5", "denkt")], [("c1", "ruhig"), ("c2", "verlegen"), ("c7", "denkt")]),
]))

# ===========================================================================================================================
# I II. 4. Wiederherstellung möglich und zumutbar
# ===========================================================================================================================
folie([("d1", "II. 4. Wiederherstellung › tatsächlich möglich"), ("d3", "II. 4. Wiederherstellung › rechtlich möglich"),
       ("d4", "II. 4. Wiederherstellung › zumutbar")], rechts_frei([
    *ptitel("d1", "4", "Wiederherstellung", F4),
    z("tatsächlich möglich?", 110, 190, beim("d1", "tatsächlich"), "Bold", 36),
    z("Radweg-Fall: Eigentümer hatte den Weg selbst beseitigt", 150, 245, "d2", size=32),
    zit("BVerwG, Urt. v. 19.9.2019 – 9 C 5.19, Rn. 15", 150, 292, "d2"),
    z("rechtlich ausgeschlossen, wenn der angestrebte", 110, 350, "d3", "Bold", 34),
    z("Zustand der Rechtsordnung widerspräche", 150, 400, beim("d3", "Rechtsordnung"), size=34),
    zit("BVerwG, Beschl. v. 2.12.2015 – 6 B 33.15, Rn. 14", 150, 450, beim("d3", "Rechtsordnung")),
    z("zumutbar für die Gemeinde?", 110, 505, "d4", "Bold", 36),
    zit("BVerwG, Beschl. v. 12.7.2013 – 9 B 12.13, Rn. 5", 150, 558, "d4"),
    blk(110, 620, 1040, 86, F4, "d5", [("Steine herausnehmen, Erde auffüllen", "ExtraBold", 36, INK)]),
    *okz("möglich und zumutbar", 740, beim("d5", "möglich"), "Bold", 38, x=160),
    *requisit([("d1", ("tabler", "restore", 100, F4), "tatsächlich möglich?", F4),
               ("d2", ("tabler", "bike", 120, WEISS), "Radweg-Fall", WEISS),
               ("d3", ("tabler", "scale", 100, WEISS), "rechtlich möglich?", WEISS),
               ("d4", ("tabler", "hand-stop", 100, WEISS), "zumutbar?", WEISS),
               ("d5", ("tabler", "shovel", 100, F4), "Steine heraus", F4)]),
    *paar("d1", [("d1", "ruhig"), ("d4", "denkt"), (beim("d5", "möglich"), "froh")], [("d1", "ruhig"), ("d5", "ernst")]),
]))

# ===========================================================================================================================
# J1 III. Rechtsfolge: Status quo ante, kein Schadensersatz
# ===========================================================================================================================
folie([("rf", "III. Rechtsfolge › Status quo ante"), ("rf2", "III. Rechtsfolge › kein Schadensersatz")], rechts_frei([
    *tafel("rf", "III. Rechtsfolge"),
    blk(110, 185, 1040, 90, GRUEN, beim("rf1", "Wiederherstellung"), [("Wiederherstellung: Status quo ante", "ExtraBold", 38, INK)]),
    z("der Zustand vor dem Eingriff", 150, 305, beim("rf1", "Zustands"), size=36),
    zit("BVerwG, Urt. v. 19.9.2019 – 9 C 5.19, Rn. 13; Beschl. v. 27.5.2015 – 7 B 14.15, Rn. 9", 150, 360, beim("rf1", "Status")),
    *neinz("kein Schadensersatzanspruch", 440, "rf2", "Bold", 38, x=160),
    *okz("Ottilie muss sich nicht mit Geld abfinden lassen", 530, "rf3", "Bold", 34, x=160),
    *requisit([("rf", ("tabler", "restore", 100, GRUEN), "Rechtsfolge", WEISS),
               (beim("rf1", "Status"), ("fluent-emoji-high-contrast", "rose", 80, ROT), "Status quo ante", GRUEN),
               ("rf2", ("tabler", "cash-banknote-off", 120, WEISS), "kein Schadensersatz", WEISS),
               ("rf3", ("tabler", "cash-banknote-off", 120, WEISS), "nicht mit Geld abfinden", ROT)]),
    *paar("rf", [("rf", "ruhig"), ("rf3", "froh")], [("rf", "ruhig"), ("rf2", "verlegen")]),
]))

# ===========================================================================================================================
# J2 Kontrast Amtshaftung: Art. 34 Satz 1 GG (Wortlaut), § 839 BGB
# ===========================================================================================================================
W34 = ["„Verletzt jemand in Ausübung eines ihm anvertrauten",
       "öffentlichen Amtes die ihm einem Dritten gegenüber obliegende",
       "Amtspflicht, so trifft die Verantwortlichkeit grundsätzlich den",
       "Staat oder die Körperschaft, in deren Dienst er steht. …“"]
w34, w34_y = wortlaut(80, 180, 1100, W34, "Art. 34 Satz 1 GG", beim("w34", "Artikel"), marken=[
    (2, "Verantwortlichkeit", beim("w34", "Verantwortlichkeit")), (2, "grundsätzlich den", beim("w34", "Staat")),
    (3, "Staat", beim("w34", "Staat"))], size=32)
folie([("w34", "III. Rechtsfolge › Kontrast: Amtshaftung")], rechts_frei([
    *tafel("w34", "Kontrast: Amtshaftung"),
    *w34,
    blk(110, w34_y + 50, 1040, 86, ROT, "w839", [("§ 839 Abs. 1 Satz 1 BGB: vorsätzlich oder fahrlässig", "ExtraBold", 33, INK)]),
    *requisit([("w34", ("tabler", "cash", 110, WEISS), "Schadensersatz", WEISS),
               (beim("w34", "Staat"), ("tabler", "building-bank", 100, WEISS), "den Staat", WEISS),
               ("w839", ("tabler", "alert-triangle", 100, ROT), "Vorsatz oder Fahrlässigkeit", ROT)]),
    *paar("w34", [("w34", "ruhig"), ("w839", "denkt")], [("w34", "ruhig"), ("w839", "ernst")]),
]))

# ===========================================================================================================================
# K Mitverschulden
# ===========================================================================================================================
folie([("mv", "III. Rechtsfolge › Mitverschulden, § 254 BGB")], rechts_frei([
    *tafel("mv", "Grenze: Mitverschulden"),
    z("Betroffene hat mitverursacht:", 110, 190, "mv1", "Bold", 36),
    *okz("BVerwG berücksichtigt das", 250, beim("mv1", "berücksichtigt"), size=36, x=160),
    z("Rechtsgedanke des § 254 BGB", 160, 310, beim("mv1", "Rechtsgedanken"), size=36),
    zit("BVerwG, Urt. v. 28.1.2010 – 3 C 17.09, Rn. 28 (zu BVerwGE 82, 24)", 160, 365, beim("mv1", "Rechtsgedanken")),
    blk(110, 440, 1040, 90, F4, "mv2", [("Beispiel: Ottilie entfernt die Grenzsteine", "ExtraBold", 36, INK)]),
    z("niemand kann die Grenze sehen", 150, 560, beim("mv2", "niemand"), size=34),
    *neinz("hier: Ottilie hat nichts beigetragen", 650, "mv3", "Bold", 36, x=160),
    *requisit([("mv", ("tabler", "percentage", 100, WEISS), "Mitverschulden", WEISS),
               ("mv2", ("tabler", "map-pin", 100, WEISS), "Grenzsteine", F4),
               ("mv3", ("tabler", "user-check", 100, GRUEN), "nichts beigetragen", GRUEN)]),
    *paar("mv", [("mv", "ruhig"), ("mv2", "staunt"), ("mv3", "froh")], [("mv", "ruhig"), ("mv2", "denkt")]),
]))

# ===========================================================================================================================
# L Prozessuales
# ===========================================================================================================================
folie([("proz", "Prozessuales › § 40 Abs. 1 VwGO"), ("lk", "Prozessuales › allgemeine Leistungsklage")], rechts_frei([
    *tafel("proz", "Prozessuales"),
    *okz("Verwaltungsrechtsweg, § 40 Abs. 1 VwGO", 200, beim("proz", "Verwaltungsrechtsweg"), "Bold", 38, x=160),
    *okz("statthaft: allgemeine Leistungsklage", 290, "lk", "Bold", 38, x=160),
    zit("BVerwG, Urt. v. 27.2.2019 – 6 C 1.18, Rn. 14; Urt. v. 19.9.2019 – 9 C 5.19, Rn. 12", 160, 350, "lk"),
    *requisit([("proz", ("tabler", "building-bank", 100, WEISS), "Verwaltungsrechtsweg", WEISS),
               ("lk", ("tabler", "gavel", 100, WEISS), "Leistungsklage", BLAU)]),
    *paar("proz", [("proz", "ruhig"), ("lk", "denkt")], [("proz", "ruhig")]),
]))

# ===========================================================================================================================
# M1 Lösung
# ===========================================================================================================================
folie([("loes", "Lösung")], rechts_frei([
    *tafel("loes", "Die Lösung"),
    *nummer("1", 110, 195, "l1", F1, gr=56), *nummer("2", 176, 195, "l1", F2, gr=56),
    *okz("hoheitlicher Eingriff in Ottilies Eigentum", 200, beim("l1", "hoheitlich"), "Bold", 34, x=325),
    *nummer("3", 110, 295, "l2", F3, gr=56),
    *okz("rechtswidriger Zustand dauert an", 300, "l2", "Bold", 34, x=325),
    *nummer("4", 110, 395, "l3", F4, gr=56),
    *okz("Wiederherstellung möglich und zumutbar", 400, "l3", "Bold", 34, x=325),
    *requisit([("loes", ("tabler", "clipboard-check", 100, WEISS), "Lösung", WEISS)]),
    *paar("loes", [("loes", "ruhig"), ("l3", "froh")], [("loes", "ruhig"), ("l2", "verlegen")]),
]))

# ===========================================================================================================================
# M2 Zurück im Vorgarten: Die Gemeinde entfernt das Pflaster
# ===========================================================================================================================
BX2, WX2 = 690, 380
ORD = beim("we2", "Ordnung")
folie([("l4", "Lösung · Zurück im Vorgarten")], [
    boden_bild("l4", "pflaster", "pflaster", bis=beim("l4", "entfernen")),
    boden_bild(beim("l4", "entfernen"), "pflaster", "erde", bis=ORD), boden_bild(ORD, "pflaster", "gras"),
    haus("l4"), grenzstein("l4"), *rosen(ROSEN_GART, "l4"), *rosen(ROSEN_STR, ORD, anim="pop"),
    pl("Pflaster entfernen, Vorgarten wiederherstellen", 70, 30, "l4", fill=GRUEN, size=36),
    szene(ficon("fluent-emoji-high-contrast", "brick", 520, BODEN + 2, 70, beim("l4", "entfernen"), fuell=ROT),
          "172schaufel*", 0.7, 0.0),
    *fig("BA", BX2, BODEN, FH, [("l4", "ruhig_r"), (beim("l4", "entfernen"), "froh_r")]),
    ns("Bauarbeiter", BX2, BODEN, "l4", BA_N, d=0.1),
    *fig("WE", WX2, BODEN, FH, [("l4", "ruhig_r")], bis="we2"),
    *redet("WE_redet_r", WX2, BODEN, FH, "we2", "tipp"),
    ns("Herr Wernicke", WX2, BODEN, "l4", WE_N, d=0.2),
    blase("sprech", 600, 220, "we2", 760, 210, inhalt=["Gut. Wir nehmen die Steine", "wieder heraus und bringen",
                                                       "Ihren Vorgarten in Ordnung."], textsize=32,
          figur=("WE_redet_r", WX2, BODEN, FH)),
    *fig("OT", OX, BODEN, FH, [("l4", "denkt"), ("we2", "staunt"), (ORD, "froh")]),
    ns("Ottilie", OX, BODEN, "l4", OT_N, d=0.3),
])
_hx, _hy = hand("BA_froh_r", BX2, BODEN, FH, +1)
FOLIEN[-1]["els"].append(ficon("tabler", "shovel", _hx + 30, _hy + 60, 80, beim("l4", "entfernen"), fuell=WEISS))

# ===========================================================================================================================
# N Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · kein Schadensersatz")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("nicht wie einen Schadensersatz prüfen", 200, 200, beim("tipp", "Prüfe"), "Bold", 38),
    z("kein Verschulden nötig", 240, 290, beim("t1", "Verschulden"), size=38),
    z("Ziel: Wiederherstellung, nicht Geld", 240, 360, beim("t1", "Wiederherstellung"), size=38),
    z("Herleitung: ein Satz genügt", 240, 430, "t2", size=38),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# O Klausurschema
# ===========================================================================================================================
REIHEN = [("k1", "I.", "Rechtsgrundlage: Folgenbeseitigungsanspruch", "Art. 20 III GG, Grundrechte", BLAU, 0, None),
          ("k2", "II.", "Voraussetzungen", "", GELB, 0, None),
          ("k21", "1.", "hoheitlicher Eingriff", "auch Realakt", None, 1, F1),
          ("k22", "2.", "in ein subjektives Recht", "z. B. Art. 14 GG", None, 1, F2),
          ("k23", "3.", "rechtswidriger Zustand, der andauert", "", None, 1, F3),
          ("k24", "4.", "Wiederherstellung möglich und zumutbar", "", None, 1, F4),
          ("k3", "III.", "Rechtsfolge: Wiederherstellung des früheren Zustands", "", GRUEN, 0, None),
          ("k31", "", "Mitverschulden: Rechtsgedanke des § 254 BGB", "", None, 1, None)]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Klausurschema: Folgenbeseitigungsanspruch"), 110, 90, "sch", 50)]
y = 205
for c, r, kopf, norm, farbe, ebene, punkt_f in REIHEN:
    if ebene == 0:
        els_sch += [karte(110, y, 110, 70, c, fill=farbe, rund=14, schatten=5, rand=4),
                    z(r, 165 - F("ExtraBold", 38).getlength(r) / 2, y + 10, c, "ExtraBold", 38, rechts=1820),
                    z(kopf, 255, y + 10, c, "ExtraBold", 40, rechts=1820)]
        hh = 92
    else:
        if punkt_f:
            els_sch.append(karte(262, y + 12, 34, 34, c, fill=punkt_f, rund=8, schatten=3, rand=3))
        if r:
            els_sch.append(z(r, 312, y + 4, c, "Bold", 36, rechts=1820))
        els_sch.append(z(kopf, 370, y + 4, c, "Bold", 36, rechts=1820))
        hh = 76
    if norm:
        els_sch.append(zit(norm, 1420, y + (18 if ebene == 0 else 12), c, size=30, rechts=1820))
    y += hh
assert y <= 970, y
folie([("sch", "Klausurschema"), ("k1", "Klausurschema › I. Rechtsgrundlage"), ("k2", "Klausurschema › II. Voraussetzungen"),
       ("k3", "Klausurschema › III. Rechtsfolge")], els_sch)

# ===========================================================================================================================
# P Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Der Folgenbeseitigungsanspruch", 0)], [("stellt den früheren Zustand", "a")], [("wieder her.", "a")]],
                750, 290, 44, "merke", {"a": beim("merke", "stellt")}),
    *markertext([[("Für Schadensersatz brauchst du", 0)], [("eine andere Grundlage,", "b")], [("etwa die Amtshaftung.", 0)]],
                750, 560, 42, "mk2", {"b": beim("mk2", "andere")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
