"""Folge 252 · Anklageschrift § 200 StPO: Aufbau Schritt für Schritt – Serienstandard Open Peeps (Katzenkönig).
Fall: Montagmorgen, Staatsanwaltschaft Ahornstadt (erfunden). Referendar Hiller soll für Oberstaatsanwalt Endres die Anklage
zum Schöffengericht schreiben. In der Akte: Am 10.3.2026 gegen 14 Uhr steigt jemand durch das offene Küchenfenster in die
Erdgeschosswohnung von Frau Probst, Schmuck für 2.400 € verschwindet; Fingerabdrücke von Herrn Unger am Fensterrahmen;
Ring am 11.3. im Ankaufsladen verkauft; Unger schweigt, hat einen Verteidiger. Szenen laut ../SZENENPLAN.md: A Büro
(Hiller am Schreibtisch, Endres kommt herein), B In der Akte (Wohnung, Kommode, Fenster; keine Tatszene, keine Gewalt),
B2 Frage, C Sachverhalt, D § 200 Abs. 1 (Wortlautkarte), E § 200 Abs. 2 (Wortlautkarte) und Nr. 110 RiStBV, F–K Muster der
Anklageschrift Schritt 1–5 (eigenes Muster), L typische Fehler (Wortlautkarte BGH StB 39/21 Rn. 18), M Klausurtipp (Lexi),
N Schema, O Merksatz (Lexi). Kein Richterhammer (Gericht als Säulengebäude). Ein Handlungsgeräusch (Tür;
../geraeusche_herkunft.json). Namensschild jeder Figur, solange sie im Bild ist.
Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/flurboden/tisch als eigene Kopie aus Folge 249
(gemeinsame Dateien unverändert); neu: muster(), buero(), schreibtisch(), requisit() mit eigenem Ende. Zahlen auf Tafeln,
Pillen und Blasen als Ziffern. Wortlautkarten wörtlich nach gesetze-im-internet.de bzw. dem amtlichen BGH-Volltext
(Abruf 08.10.2026)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from ostil import lichtkegel
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_252/"

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
TUERKIS_ = (127, 214, 208, 255)
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
        if n.startswith(("bild:", "ficon:", "bank")) or "/op_252/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def wortlaut(x, y, w, zeilen, quelle, cue, marken=(), size=32, bis=None):
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 08.10.2026), als Zitat mit Normangabe;
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


# --- eigene Szenenbausteine: Treppenhaus, Atelier, Wohnzimmer der Richterin (Palettenflächen, Tuschekontur) ------------
BODEN_T = (214, 206, 192, 255)               # Fliesen im Treppenhaus
BODEN_H = (222, 196, 160, 255)               # Holzboden im Atelier / Wohnzimmer
F_O, F_U = 930, 1000                         # Bodenfläche (Oberkante, Unterkante)
FH = 500                                     # Figurenhöhe in den Fallszenen
FU = 942                                     # Unterkante der Figuren in den Fallszenen


def flurboden(cue, farbe, fugen=True):
    s = 2
    im = Image.new("RGBA", (1860 * s, (F_U - F_O) * s))
    dr = ImageDraw.Draw(im)
    dr.rectangle((0, 0, 1860 * s, (F_U - F_O) * s), fill=farbe)
    dr.line((0, 0, 1860 * s, 0), fill=INK, width=6 * s)
    if fugen:
        for x in range(100, 1860, 220):
            dr.line(((x + 30) * s, 6 * s, (x - 10) * s, (F_U - F_O) * s), fill=(176, 166, 150, 255), width=4 * s)
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    return El(im, 30, F_O, cue, "cut", 0.0, None, name="boden")


def deckenlampe(cx, cue, boden=F_O):
    """Deckenlampe (Tabler bulb, gelb) mit Lichtkegel bis zum Boden (Abendlicht, Lampe brennt)."""
    birne = ficon("tabler", "bulb", cx, 150, 90, cue, fuell=GELB, anim="cut")
    kabel = linienzug([(cx, 30), (cx, 70)], cue, breite=5)
    kegel = lichtkegel(cx, 150, 260, boden, cue)
    return [hart(kegel), hart(kabel), birne]


def tisch(x0, x1, y, cue, fill=HOLZ):
    """Arbeitstisch (Platte + zwei Beine) bis zum Boden."""
    return [karte(x0, y, x1 - x0, 40, cue, fill=fill, rund=10, schatten=4, rand=4, anim="cut"),
            linienzug([(x0 + 50, y + 42), (x0 + 50, F_O)], cue, breite=10),
            linienzug([(x1 - 50, y + 42), (x1 - 50, F_O)], cue, breite=10)]




X1, X2 = 1430, 1730                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"HI": "Referendar Hiller", "EN": "OStA Endres", "UN": "Herr Unger", "PR": "Frau Probst"}   # neben der Tafel kurz (Schildbreite)
NFARBE = {"HI": BLAUHELL, "EN": LILAHELL, "UN": WEISS, "PR": LILA}


def requisit(folge, px=PX):
    """Wechselndes Requisit über den Figuren: folge = [(cue, (set, icon, breite, fuell), pillentext, pillenfarbe[, bis])]."""
    els = []
    for i, eintrag in enumerate(folge):
        c, ic, txt, pf = eintrag[:4]
        b = eintrag[4] if len(eintrag) > 4 else (folge[i + 1][0] if i + 1 < len(folge) else None)
        if ic:
            s_, n_, br, fu = ic
            els.append(ficon(s_, n_, px, PU, br, c, fuell=fu, bis=b))
        if txt:
            els.append(pl(txt, px, PY, c, fill=pf, size=28, anker="m", bis=b))
    return els


def stehend(k, x, folge, unten=FB, hoehe=FR, bis=None):
    return [*fig(k, x, unten, hoehe, folge, bis=bis), ns(NAME[k], x, unten, folge[0][0], NFARBE[k], d=0.1)]


def muster(x, y, w, cue, zeilen, size=30, bis=None):
    """Musterblatt der Anklageschrift (eigenes Muster, kein Anbieter-Muster): weißes Blatt mit Randlinie.
    zeilen = [(text, cue, stil, art)] mit art "label" (Pille), "text" (Mustertext) oder "abstand"."""
    lh = int(size * 1.45)
    hoehe = 34 + sum({"label": 64, "text": lh, "abstand": 14}[a] for _, _, _, a in zeilen) + 20
    els = [bis_(karte(x, y, w, hoehe, cue, fill=WEISS, rund=12, schatten=6, rand=4), bis),
           bis_(linienzug([(x + 40, y + 14), (x + 40, y + hoehe - 14)], cue, breite=4, farbe=ROT), bis)]
    yy = y + 24
    for t, c, st, a in zeilen:
        if a == "label":
            els.append(bis_(pl(t, x + 64, yy, c, fill=GELB, size=26), bis)); yy += 64
        elif a == "text":
            els.append(z(t, x + 64, yy, c, st, size, rechts=x + w - 16, bis=bis)); yy += lh
        else:
            yy += 14
    return els, y + hoehe


# ===========================================================================================================================
# A Fall: Montagmorgen im Büro der Staatsanwaltschaft (Referendar Hiller am Schreibtisch, Endres kommt herein)
# ===========================================================================================================================
HX, EX, TX = 690, 1330, 1680                # Hiller (hinter dem Schreibtisch), Endres, Tür


def buero(c0, tuer_auf=None, mit_tuer_geraeusch=False):
    """Büro: Holzboden, Fenster, Bücherregal, Tür rechts. Der Schreibtisch wird nach Hiller gezeichnet (verdeckt die Beine:
    Hiller sitzt am Tisch)."""
    els = [hart(flurboden(c0, BODEN_H, fugen=False)),
           hart(ficon("tabler", "window", 240, 600, 230, c0, fuell=BLAUHELL, anim="cut")),
           hart(ficon("tabler", "books", 1060, 600, 170, c0, fuell=GELB, anim="cut"))]
    if tuer_auf is None:
        els.append(hart(ficon("tabler", "door", TX, F_O + 8, 420, c0, fuell=HOLZ, anim="cut")))
    else:
        els.append(hart(ficon("tabler", "door", TX, F_O + 8, 420, c0, fuell=HOLZ, anim="cut", bis=tuer_auf)))
        auf = ficon("tabler", "door", TX, F_O + 8, 420, tuer_auf, fuell=(255, 238, 180, 255), anim="cut")
        els.append(szene(auf, "252tuer*", 0.7, 0.0) if mit_tuer_geraeusch else hart(auf))
    return els


def schreibtisch(c0, akte_offen=True):
    els = [karte(360, 690, 640, 34, c0, fill=HOLZ, rund=8, schatten=4, rand=4, anim="cut"),
           karte(400, 722, 560, 208, c0, fill=(196, 140, 92, 255), rund=6, schatten=0, rand=4, anim="cut"),
           ficon("tabler", "lamp", 930, 692, 110, c0, fuell=GELB, anim="cut"),
           ficon("tabler", "folders" if akte_offen else "folder", 470, 692, 120, c0, fuell=GELB, anim="cut")]
    return [hart(e) for e in els]


P0 = "Fall"
folie([(NULL, f"{P0} · Staatsanwaltschaft Ahornstadt"), ("hiller", f"{P0} · Referendar Hiller"),
       ("endres", f"{P0} · Oberstaatsanwalt Endres"), ("e1", f"{P0} · „Schreiben Sie die Anklage“"),
       ("h1", f"{P0} · Womit fange ich an?")], [
    *buero(NULL, tuer_auf="endres", mit_tuer_geraeusch=True),
    hart(pl("Montagmorgen: Staatsanwaltschaft Ahornstadt", 70, 30, NULL, fill=GELB, size=40)),
    *fig("HI", HX, FU, FH, [("hiller", "ruhig_r"), ("e1", "denkt_r")], bis="h1", erst="pop"),
    *redet("HI_redet_r", HX, FU, FH, "h1", "akte"),
    *schreibtisch(NULL),
    ns("Referendar Hiller", HX, FU, "hiller", BLAUHELL, d=0.1),
    *fig("EN", EX, FU, FH, [(beim("endres", "Oberstaatsanwalt"), "ruhig")], bis="e1", erst="pop"),
    *redet("EN_redet", EX, FU, FH, "e1", "h1"),
    *fig("EN", EX, FU, FH, [("h1", "froh")], bis="akte", erst="cut"),
    ns("Oberstaatsanwalt Endres", EX, FU, beim("endres", "Oberstaatsanwalt"), LILAHELL, d=0.1),
    blase("sprech", 700, 260, "e1", 1180, 250, inhalt=["Den hinreichenden Tatverdacht", "haben Sie bejaht. Jetzt schreiben",
          "Sie die Anklage zum Schöffengericht."], textsize=32, figur=("EN_redet", EX, FU, FH), bis="h1"),
    blase("sprech", 640, 230, "h1", 700, 250, inhalt=["Gern. Aber womit fange ich an,", "und was gehört alles hinein?"],
          textsize=32, figur=("HI_redet_r", HX, FU, FH), bis="akte"),
])

# ===========================================================================================================================
# B Fall: was in der Akte steht (Wohnung von Frau Probst, Fingerabdrücke, Ankaufsbeleg; keine Gewalt, keine Tatszene)
# ===========================================================================================================================
WX, KX0, KX1 = 300, 560, 860                # Küchenfenster, Kommode
PRX, UNX = 1110, 1690                       # Frau Probst, Herr Unger
folie([("akte", "Fall · In der Akte"), ("tag", "Fall · 10.3.2026, gegen 14 Uhr"), ("fenster", "Fall · durch das offene Küchenfenster"),
       ("schmuck", "Fall · Schmuck für 2.400 €"), ("finger", "Fall · Fingerabdrücke von Herrn Unger"),
       ("beleg", "Fall · Ring im Ankaufsladen verkauft"), ("schweigt", "Fall · Unger schweigt, hat einen Verteidiger")], [
    hart(flurboden("akte", BODEN_T)),
    pl("In der Akte", 70, 30, "akte", fill=GELB, size=40),
    ficon("tabler", "folder", 1780, 140, 110, "akte", fuell=GELB, anim="cut", bis="tag"),
    pl("10.3.2026, gegen 14 Uhr", 70, 105, "tag", fill=WEISS, size=32),
    ficon("tabler", "calendar-event", 1780, 150, 110, "tag", fuell=WEISS, bis="fenster"),
    ficon("tabler", "window", WX, 820, 260, "akte", fuell=BLAUHELL, anim="cut", bis="fenster"),
    ficon("tabler", "window", WX, 820, 260, "fenster", fuell=(255, 238, 180, 255), anim="cut"),
    pl("offenes Küchenfenster, Erdgeschosswohnung", 70, 172, "fenster", fill=WEISS, size=32),
    karte(KX0, 720, KX1 - KX0, 210, "akte", fill=HOLZ, rund=10, schatten=4, rand=4, anim="cut"),
    linienzug([(KX0 + 20, 825), (KX1 - 20, 825)], "akte", breite=4),
    ficon("tabler", "diamonds", (KX0 + KX1) // 2, 722, 100, "akte", fuell=BLAU, anim="cut", bis="schmuck"),
    pl("Schmuck weg: 2.400 €", 70, 239, "schmuck", fill=HELLROT, size=32),
    ring((KX0 + KX1) // 2, 680, 120, 70, "schmuck", bis="finger"),
    ficon("tabler", "fingerprint", WX + 105, 720, 80, "finger", fuell=GELB),
    ring(WX + 105, 680, 70, 60, beim("finger", "Fingerabdrücke"), bis="beleg"),
    pl("Fingerabdrücke am Fensterrahmen: Herr Unger", 70, 306, "finger", fill=WEISS, size=32),
    ficon("tabler", "receipt", UNX, 420, 100, "beleg", fuell=WEISS),
    pl("11.3.: Ring im Ankaufsladen verkauft, mit Ausweis", 70, 373, "beleg", fill=WEISS, size=32),
    pl("Unger schweigt · er hat einen Verteidiger", 70, 440, "schweigt", fill=WEISS, size=32),
    *fig("PR", PRX, FU, FH, [(beim("fenster", "Probst"), "ruhig"), ("schmuck", "sorge"), ("finger", "muede")], erst="pop"),
    ns("Frau Probst", PRX, FU, beim("fenster", "Probst"), LILA, d=0.1),
    *fig("UN", UNX, FU, FH, [(beim("finger", "Unger"), "ruhig"), ("schweigt", "still")], erst="pop"),
    ns("Herr Unger", UNX, FU, beim("finger", "Unger"), WEISS, d=0.1),
])

# ===========================================================================================================================
# B2 Die Frage (zurück im Büro)
# ===========================================================================================================================
folie([("frage", "Fall · Die Frage")], [
    *buero("frage"),
    *fig("HI", HX, FU, FH, [("frage", "denkt_r")], erst="cut"),
    *schreibtisch("frage"),
    ns("Referendar Hiller", HX, FU, "frage", BLAUHELL),
    *fig("EN", EX, FU, FH, [("frage", "ruhig")], erst="cut"),
    ns("Oberstaatsanwalt Endres", EX, FU, "frage", LILAHELL),
    pl("Was gehört in die Anklageschrift –", 70, 40, "frage", fill=PINK, size=40),
    pl("und in welcher Reihenfolge?", 70, 120, beim("frage", "und"), fill=PINK, size=40),
])

# ===========================================================================================================================
# C Sachverhalt
# ===========================================================================================================================
def sachverhalt_252(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 205
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=34, zeilenabstand=1.3)
        els += e; y += 18
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_252("sv", [
    "Am 10. März 2026 gegen 14 Uhr steigt jemand durch das offene Küchenfenster in die Erdgeschosswohnung von Frau Probst "
    "im Lindenweg 4 in Ahornstadt, in der sie lebt, und nimmt aus der Kommode Schmuck im Wert von 2.400 € mit.",
    "Am Fensterrahmen findet die Polizei Fingerabdrücke von Herrn Unger (41, nicht vorbestraft). Am 11. März verkauft er "
    "einen Ring aus dem Schmuck mit seinem Ausweis in einem Ankaufsladen. Lichtbilder vom Tatort liegen vor. Unger schweigt; "
    "er hat einen Verteidiger.",
    "Referendar Hiller hat den hinreichenden Tatverdacht bejaht; mehr als vier Jahre Freiheitsstrafe sind nicht zu erwarten. "
    "Oberstaatsanwalt Endres: „Schreiben Sie die Anklage zum Schöffengericht.“",
], "Was gehört in die Anklageschrift, und in welcher Reihenfolge?")

# ===========================================================================================================================
# D § 200 Abs. 1 StPO (Wortlautkarte)
# ===========================================================================================================================
W200 = ["„(1) Die Anklageschrift hat den Angeschuldigten, die Tat, die",
        "ihm zur Last gelegt wird, Zeit und Ort ihrer Begehung, die",
        "gesetzlichen Merkmale der Straftat und die anzuwendenden",
        "Strafvorschriften zu bezeichnen (Anklagesatz). In ihr sind",
        "ferner die Beweismittel, das Gericht, vor dem die Haupt-",
        "verhandlung stattfinden soll, und der Verteidiger anzugeben. …“"]
w200, w200_y = wortlaut(80, 160, 1100, W200, "§ 200 Abs. 1 S. 1, 2 StPO", "p200", marken=[
    (0, "Angeschuldigten", beim("ang", "Angeschuldigten")), (0, "die Tat", beim("tat", "Tat")),
    (1, "Zeit und Ort", beim("zeit", "Zeit")), (2, "gesetzlichen Merkmale", beim("merk", "gesetzlichen")),
    (2, "anzuwendenden", beim("vorschr", "anzuwendenden")), (3, "Strafvorschriften", beim("vorschr", "Strafvorschriften")),
    (3, "(Anklagesatz)", beim("asatz", "Anklagesatz")), (4, "Beweismittel", beim("bew", "Beweismittel")),
    (4, "das Gericht", beim("ger", "Gericht")), (5, "Verteidiger", beim("vert", "Verteidiger"))], size=32)
PD = "§ 200 StPO › Abs. 1"
folie([("p200", "§ 200 StPO › Inhalt der Anklageschrift"), ("abs1", f"{PD} › Angeschuldigter, Tat"),
       ("zeit", f"{PD} › Zeit und Ort"), ("merk", f"{PD} › gesetzliche Merkmale"), ("vorschr", f"{PD} › Strafvorschriften"),
       ("asatz", f"{PD} › Anklagesatz"), ("s2", f"{PD} › Beweismittel, Gericht, Verteidiger")], rechts_frei([
    *tafel("p200", "§ 200 StPO: Was hineingehört", h=w200_y + 250 - 60, size=46),
    *w200,
    blk(110, w200_y + 30, 1040, 80, GELB, "asatz", [("Anklagesatz: Tat · Zeit und Ort · Merkmale · Vorschriften", "ExtraBold", 32, INK)]),
    z("außerdem: Beweismittel · Gericht · Verteidiger", 110, w200_y + 135, "s2", "Bold", 32),
    *requisit([("p200", ("tabler", "book", 100, WEISS), "§ 200 StPO", GELB),
               ("ang", ("tabler", "user", 100, WEISS), "Angeschuldigter", WEISS),
               ("tat", ("tabler", "file-description", 100, WEISS), "die Tat", WEISS),
               ("zeit", ("tabler", "calendar-event", 100, WEISS), "Zeit und Ort", WEISS),
               ("merk", ("tabler", "list-check", 100, WEISS), "gesetzliche Merkmale", WEISS),
               ("vorschr", ("tabler", "book", 100, WEISS), "Strafvorschriften", WEISS),
               ("asatz", ("tabler", "file-text", 100, GELB), "Anklagesatz", GELB),
               ("bew", ("tabler", "fingerprint", 100, GELB), "Beweismittel", WEISS),
               ("ger", ("tabler", "building-bank", 120, BLAU), "Gericht", WEISS),
               ("vert", ("tabler", "briefcase", 100, WEISS), "Verteidiger", WEISS)]),
    *stehend("HI", X1, [("p200", "ruhig"), ("asatz", "denkt"), ("s2", "fest")]),
    *stehend("EN", X2, [("p200", "ruhig"), ("asatz", "ernst")]),
]))

# ===========================================================================================================================
# E § 200 Abs. 2 StPO (Wortlautkarte) und Nr. 110 RiStBV
# ===========================================================================================================================
W200b = ["„(2) In der Anklageschrift wird auch das wesentliche Ergebnis",
         "der Ermittlungen dargestellt. Davon kann abgesehen werden,",
         "wenn Anklage beim Strafrichter erhoben wird.“"]
w2, w2_y = wortlaut(80, 160, 1100, W200b, "§ 200 Abs. 2 StPO", "abs2", marken=[
    (0, "wesentliche Ergebnis", beim("abs2", "wesentliche")), (1, "der Ermittlungen", beim("abs2", "Ermittlungen")),
    (2, "beim Strafrichter", beim("ausn", "Strafrichter"))], size=32)
PE = "§ 200 StPO › Abs. 2"
folie([("abs2", f"{PE} › wesentliches Ergebnis"), ("ausn", f"{PE} › Ausnahme: Strafrichter"),
       ("hier", f"{PE} › Schöffengericht: gehört hinein"), ("rist", "RiStBV › Nr. 110: was hineingehört"),
       ("klar", "RiStBV › Nr. 110 Abs. 1: klar und verständlich"), ("land", "RiStBV › Form: von Land zu Land")], rechts_frei([
    *tafel("abs2", "Abs. 2 und die Richtlinien", h=840, size=46),
    *w2,
    *okz("Schöffengericht: wesentliches Ergebnis gehört hinein", w2_y + 30, "hier", "Bold", 32, x=160),
    z("Was im Einzelnen hineingehört: Nr. 110 RiStBV", 110, w2_y + 110, "rist", "Bold", 32),
    z("klar, übersichtlich und vor allem für den", 110, w2_y + 170, "klar", size=32),
    z("Angeschuldigten verständlich", 110, w2_y + 216, beim("klar", "Angeschuldigten"), size=32),
    zit("Nr. 110 Abs. 1 RiStBV (Fassung vom 28.3.2023)", 110, w2_y + 264, beim("klar", "verständlich")),
    blk(110, w2_y + 320, 1040, 120, GELB, "land", [("Form: von Land zu Land verschieden –", "ExtraBold", 32, INK),
                                                   ("maßgeblich: Hinweise deines Prüfungsamts", "ExtraBold", 32, INK)]),
    *requisit([("abs2", ("tabler", "file-search", 100, WEISS), "wesentliches Ergebnis", WEISS),
               ("ausn", ("tabler", "user", 100, WEISS), "nur Strafrichter: entbehrlich", WEISS),
               ("hier", ("tabler", "users", 110, GRUEN), "Schöffengericht: Pflicht", GRUEN),
               ("rist", ("tabler", "list-check", 100, WEISS), "Nr. 110 RiStBV", GELB),
               ("klar", ("tabler", "eye", 100, WEISS), "verständlich", WEISS),
               ("land", ("tabler", "map-pin", 100, ROT), "Prüfungsamt", GELB)]),
    *stehend("HI", X1, [("abs2", "ruhig"), ("hier", "fest"), ("land", "denkt")]),
    *stehend("EN", X2, [("abs2", "ernst"), ("hier", "froh")]),
]))

# ===========================================================================================================================
# F Schritt 1: Kopf, Personalien, Verteidiger
# ===========================================================================================================================
PM = "Muster"
m1, m1_y = muster(80, 160, 1100, "kopf1", [
    ("Staatsanwaltschaft Ahornstadt · 41 Js 2087/26 · 21.9.2026", "kopf1", "Regular", "text"),
    ("Anklageschrift", beim("kopf1", "Überschrift"), "ExtraBold", "text"),
    ("", "kopf", "", "abstand"),
    ("Herr Dominik Unger, geb. 4.5.1985 in Ahornstadt,", "pers", "Regular", "text"),
    ("Elektriker, Birkenweg 7, Ahornstadt, ledig,", beim("pers", "Beruf"), "Regular", "text"),
    ("deutscher Staatsangehöriger", beim("pers", "Staatsangehörigkeit"), "Regular", "text"),
    ("Verteidiger: Rechtsanwalt Brack, Ahornstadt", "vertr", "Bold", "text"),
])
folie([("kopf", f"{PM} › 1. Kopf"), ("pers", f"{PM} › 1. Personalien"), ("vertr", f"{PM} › 1. Verteidiger"),
       ("notw", f"{PM} › 1. notwendige Verteidigung")], rechts_frei([
    *tafel("kopf", "Schritt 1: Kopf und Personalien", h=840, size=46),
    *m1,
    zit("Nr. 110 Abs. 2 lit. a, b RiStBV", 110, m1_y + 14, beim("pers", "Name")),
    blk(110, m1_y + 70, 1040, 120, HELLGRUEN, "notw", [("notwendige Verteidigung: Verbrechen,", "ExtraBold", 32, INK),
                                                      ("Verhandlung vor dem Schöffengericht", "ExtraBold", 32, INK)]),
    zit("§ 140 Abs. 1 Nr. 1, 2 StPO", 110, m1_y + 202, beim("notw", "Schöffengericht")),
    *requisit([("kopf", ("tabler", "file-text", 100, WEISS), "Anklageschrift", GELB),
               ("pers", ("tabler", "id", 110, WEISS), "Personalien", WEISS),
               ("vertr", ("tabler", "briefcase", 100, WEISS), "Verteidiger", WEISS),
               ("notw", ("tabler", "briefcase", 100, GRUEN), "notwendige Verteidigung", GRUEN)]),
    *stehend("HI", X1, [("kopf", "fest"), ("notw", "denkt")]),
    *stehend("EN", X2, [("kopf", "ruhig"), ("vertr", "ernst")]),
]))

# ===========================================================================================================================
# G Schritt 2: Anklagesatz – Einleitung, Zeit und Ort, gesetzliche Merkmale
# ===========================================================================================================================
m2, m2_y = muster(80, 160, 1100, "einl", [
    ("Einleitung", "einl", "", "label"),
    ("Der Angeschuldigte wird angeklagt,", beim("einl", "Der"), "Bold", "text"),
    ("Zeit und Ort", "einl2", "", "label"),
    ("am 10.3.2026 in Ahornstadt", "einl2", "Bold", "text"),
    ("gesetzliche Merkmale", "abstr", "", "label"),
    ("eine fremde bewegliche Sache einem anderen in der Absicht", "abstr", "Regular", "text"),
    ("weggenommen zu haben, sie sich rechtswidrig zuzueignen,", beim("abstr", "weggenommen"), "Regular", "text"),
    ("wobei er zur Ausführung der Tat in eine dauerhaft", "abstr2", "Regular", "text"),
    ("genutzte Privatwohnung einstieg.", beim("abstr2", "genutzte"), "Regular", "text"),
])
PA = f"{PM} › 2. Anklagesatz"
folie([("as", f"{PA}"), ("einl", f"{PA} › Einleitung"), ("einl2", f"{PA} › Zeit und Ort"),
       ("abstr", f"{PA} › gesetzliche Merkmale"), ("abstr3", f"{PA} › auf Unger bezogen")], rechts_frei([
    *tafel("as", "Schritt 2: der Anklagesatz", h=840, size=46),
    *m2,
    blk(110, m2_y + 26, 1040, 76, GELB, "abstr3", [("gesetzliche Merkmale, auf Unger bezogen", "ExtraBold", 32, INK)]),
    zit("§§ 242 Abs. 1, 244 Abs. 1 Nr. 3, Abs. 4 StGB", 110, m2_y + 112, beim("abstr3", "Unger")),
    *requisit([("as", ("tabler", "file-text", 100, GELB), "Herzstück", GELB),
               ("einl", ("tabler", "user", 100, WEISS), "Der Angeschuldigte …", WEISS),
               ("einl2", ("tabler", "calendar-event", 100, WEISS), "10.3.2026, Ahornstadt", WEISS),
               ("abstr", ("tabler", "list-check", 100, WEISS), "gesetzliche Merkmale", WEISS),
               ("abstr2", ("tabler", "home", 110, LILA), "dauerhaft genutzte Privatwohnung", WEISS)]),
    *stehend("HI", X1, [("as", "fest"), ("abstr", "denkt"), ("abstr3", "froh")]),
    *stehend("EN", X2, [("as", "ruhig"), ("einl2", "ernst")]),
]))

# ===========================================================================================================================
# H Schritt 2: konkreter Tatvorwurf und Paragrafenkette
# ===========================================================================================================================
m3, m3_y = muster(80, 160, 1100, "konkr", [
    ("konkreter Tatvorwurf", "konkr", "", "label"),
    ("Gegen 14 Uhr stieg der Angeschuldigte durch das offene", "k1", "Regular", "text"),
    ("Küchenfenster in die Erdgeschosswohnung der Zeugin", beim("k1", "Küchenfenster"), "Regular", "text"),
    ("Probst im Lindenweg 4 ein, in der sie lebt. Er nahm aus", beim("k1", "Probst"), "Regular", "text"),
    ("der Kommode Schmuck im Wert von 2.400 € und verließ", beim("k2", "Kommode"), "Regular", "text"),
    ("damit die Wohnung, um ihn für sich zu behalten.", beim("k3", "damit"), "Regular", "text"),
    ("Paragrafenkette", "kette", "", "label"),
    ("Verbrechen des Wohnungseinbruchdiebstahls, strafbar", "kette2", "Bold", "text"),
    ("nach §§ 242 Abs. 1, 244 Abs. 1 Nr. 3, Abs. 4 StGB.", beim("kette2", "Paragraf"), "Bold", "text"),
])
folie([("konkr", f"{PA} › konkreter Tatvorwurf"), ("k2", f"{PA} › konkreter Tatvorwurf: Schmuck"),
       ("kette", f"{PA} › Paragrafenkette")], rechts_frei([
    *tafel("konkr", "Schritt 2: konkreter Tatvorwurf", h=840, size=46),
    *m3,
    *requisit([("konkr", ("tabler", "window", 110, BLAUHELL), "Küchenfenster", WEISS),
               ("k2", ("tabler", "diamonds", 100, BLAU), "Schmuck: 2.400 €", WEISS),
               ("kette", ("tabler", "book", 100, WEISS), "§§ 242, 244 StGB", GELB)]),
    *stehend("HI", X1, [("konkr", "fest"), ("kette", "froh")]),
    *stehend("EN", X2, [("konkr", "ruhig"), ("k2", "denkt"), ("kette", "froh")]),
]))

# ===========================================================================================================================
# I Schritt 3: Beweismittel
# ===========================================================================================================================
m4, m4_y = muster(80, 330, 1100, beim("bm3", "Zeugin"), [
    ("Beweismittel", beim("bm3", "Zeugin"), "", "label"),
    ("1. Zeugin Probst, Ahornstadt", beim("bm3", "Zeugin"), "Bold", "text"),
    ("2. Gutachten zu den Fingerabdrücken", "bm4", "Regular", "text"),
    ("3. Ankaufsbeleg vom 11.3.2026", "bm5", "Regular", "text"),
    ("4. Lichtbilder vom Tatort", "bm6", "Regular", "text"),
])
PB = f"{PM} › 3. Beweismittel"
folie([("bm", f"{PB}"), ("bm1", f"{PB} › nur Wesentliches"), ("bm2", f"{PB} › Zeugen: Wohn- oder Aufenthaltsort"),
       ("bm3", f"{PB} › im Fall")], rechts_frei([
    *tafel("bm", "Schritt 3: die Beweismittel", h=840, size=46),
    *okz("nur, was wesentlich ist", 180, "bm1", "Bold", 32, x=160),
    zit("Nr. 111 Abs. 1 RiStBV", 160, 226, beim("bm1", "wesentlich")),
    *okz("Zeugen: Wohn- oder Aufenthaltsort genügt", 266, "bm2", "Bold", 32, x=160),
    zit("§ 200 Abs. 1 S. 3 StPO", 160, 312, beim("bm2", "Aufenthaltsort")),
    *m4,
    *requisit([("bm", ("tabler", "list-check", 100, WEISS), "Beweismittel", GELB),
               ("bm3", ("tabler", "user", 100, LILA), "Zeugin Probst", LILA),
               ("bm4", ("tabler", "fingerprint", 100, GELB), "Gutachten", WEISS),
               ("bm5", ("tabler", "receipt", 100, WEISS), "Ankaufsbeleg", WEISS),
               ("bm6", ("tabler", "camera", 100, WEISS), "Lichtbilder", WEISS)]),
    *stehend("HI", X1, [("bm", "ruhig"), ("bm3", "fest")]),
    *stehend("EN", X2, [("bm", "ernst"), ("bm2", "denkt"), ("bm6", "froh")]),
]))

# ===========================================================================================================================
# J Schritt 4: wesentliches Ergebnis der Ermittlungen
# ===========================================================================================================================
m5, m5_y = muster(80, 160, 1100, "we", [
    ("Wesentliches Ergebnis der Ermittlungen", "we", "", "label"),
    ("Person · Geschehen · Beweislage", "we1", "Bold", "text"),
    ("Der Angeschuldigte schweigt. Ihn belasten seine", "we2", "Regular", "text"),
    ("Fingerabdrücke am Fensterrahmen und der Verkauf", beim("we2", "Fingerabdrücke"), "Regular", "text"),
    ("des Rings am 11.3.2026.", "we3", "Regular", "text"),
])
PW = f"{PM} › 4. wesentliches Ergebnis"
folie([("we", f"{PW}"), ("we2", f"{PW} › Beweislage"), ("we4", f"{PW} › hier: warum die Beweise tragen"),
       ("we5", f"{PW} › kein zweites Gutachten")], rechts_frei([
    *tafel("we", "Schritt 4: wesentliches Ergebnis", h=840, size=46),
    *m5,
    blk(110, m5_y + 30, 1040, 120, GELB, "we4", [("hier – nicht im Anklagesatz:", "ExtraBold", 32, INK),
                                               ("warum die Beweise tragen", "ExtraBold", 32, INK)]),
    *neinz("kein zweites Gutachten", m5_y + 185, "we5", "Bold", 32, x=160),
    *requisit([("we", ("tabler", "file-search", 100, WEISS), "Ermittlungsergebnis", GELB),
               ("we2", ("tabler", "fingerprint", 100, GELB), "Fingerabdrücke", WEISS),
               ("we3", ("tabler", "receipt", 100, WEISS), "Verkauf des Rings", WEISS),
               ("we4", ("tabler", "scale", 110, WEISS), "Beweise tragen", GELB),
               ("we5", ("tabler", "x", 90, None), "kein Gutachten", HELLROT)]),
    *stehend("HI", X1, [("we", "fest"), ("we4", "denkt")]),
    *stehend("EN", X2, [("we", "ruhig"), ("we5", "ernst")]),
]))

# ===========================================================================================================================
# K Schritt 5: Antrag und Gericht; Endres liest gegen
# ===========================================================================================================================
m6, m6_y = muster(80, 160, 1100, "an1", [
    ("Antrag", "an1", "", "label"),
    ("Ich beantrage, das Hauptverfahren zu eröffnen", beim("an1", "Hauptverfahren"), "Bold", "text"),
    ("und die Anklage zur Hauptverhandlung vor dem", "an2", "Bold", "text"),
    ("Amtsgericht Ahornstadt – Schöffengericht – zuzulassen.", beim("an2", "Amtsgericht"), "Bold", "text"),
])
PN = f"{PM} › 5. Antrag"
folie([("an", f"{PN}"), ("an2", f"{PN} › Gericht: Schöffengericht"), ("zust", f"{PN} › Warum Schöffengericht?"),
       ("z1", f"{PN} › kein Strafrichter: Verbrechen"), ("z2", f"{PN} › Amtsgericht: bis 4 Jahre"),
       ("f114", f"{PN} › Zuständigkeit: Folge 114"), ("e2", "Fall · Endres liest gegen")], rechts_frei([
    *tafel("an", "Schritt 5: der Antrag", h=860, size=46),
    *m6,
    zit("§ 199 Abs. 2 S. 1, § 207 Abs. 1 StPO; Nr. 110 Abs. 3 RiStBV", 110, m6_y + 12, beim("an2", "Schöffengericht")),
    z("Warum Schöffengericht?", 110, m6_y + 66, "zust", "ExtraBold", 34),
    *neinz("Strafrichter nur bei Vergehen – hier ein Verbrechen", m6_y + 126, "z1", size=32, x=160),
    zit("§ 25 GVG; § 12 Abs. 1 StGB", 160, m6_y + 172, beim("z1", "Verbrechen")),
    *okz("nicht mehr als 4 Jahre zu erwarten: Amtsgericht", m6_y + 222, "z2", size=32, x=160),
    zit("§ 24 Abs. 1 S. 1 Nr. 2 GVG; Schöffengericht: § 28 GVG", 160, m6_y + 268, beim("z2", "Amtsgericht")),
    z("Zuständigkeit im Einzelnen: Folge 114", 110, m6_y + 330, "f114", "Bold", 32),
    *requisit([("an", ("tabler", "file-check", 100, WEISS), "Antrag", GELB),
               ("an2", ("tabler", "building-bank", 120, BLAU), "Amtsgericht Ahornstadt", WEISS),
               ("zust", ("tabler", "users", 110, WEISS), "Schöffengericht?", WEISS),
               ("z1", ("tabler", "user", 100, WEISS), "kein Strafrichter", HELLROT),
               ("z2", ("tabler", "building-bank", 120, BLAU), "Amtsgericht", GRUEN),
               ("f114", ("tabler", "book", 100, WEISS), "Folge 114", GELB, "e2")]),
    *stehend("HI", X1, [("an", "fest"), ("zust", "denkt"), ("z2", "froh"), ("e2", "staunt")]),
    *fig("EN", X2, FB, FR, [("an", "ruhig"), ("z1", "ernst")], bis="e2"),
    *redet("EN_redet", X2, FB, FR, "e2", "fehler"),
    ns(NAME["EN"], X2, FB, "an", NFARBE["EN"], d=0.1),
    blase("sprech", 640, 230, "e2", 1530, 210, inhalt=["Gut. Jetzt lese ich gegen: Ist die", "Tat unverwechselbar beschrieben?"],
          textsize=31, figur=("EN_redet", X2, FB, FR)),
]))

# ===========================================================================================================================
# L Typische Fehler (Umgrenzungsfunktion, BGH StB 39/21)
# ===========================================================================================================================
WB = ["„Die Umgrenzungsfunktion erfordert neben der Bezeichnung",
      "des Angeschuldigten Angaben, welche die Tat als geschicht-",
      "lichen Vorgang unverwechselbar kennzeichnen.“"]
wb, wb_y = wortlaut(80, 440, 1100, WB, "BGH, Beschl. v. 21.12.2021 – StB 39/21, Rn. 18", "umgr", marken=[
    (1, "die Tat", beim("umgr", "Tat")), (1, "geschicht-", beim("umgr", "geschichtlichen")),
    (2, "lichen Vorgang", beim("umgr", "geschichtlichen")), (2, "unverwechselbar", beim("umgr", "unverwechselbar"))], size=30)
PF = "Typische Fehler"
folie([("fehler", f"{PF}"), ("fe1", f"{PF} › 1. Tatzeit oder Tatort fehlt"), ("fe2", f"{PF} › 2. Tat zu ungenau"),
       ("umgr", f"{PF} › 2. Umgrenzungsfunktion"), ("umgr2", f"{PF} › 2. worüber das Gericht urteilt"),
       ("unw", f"{PF} › 2. Anklage unwirksam")], rechts_frei([
    *tafel("fehler", "Zwei typische Fehler", h=880, size=46),
    *neinz("1. Anklagesatz ohne Tatzeit oder Tatort", 175, "fe1", "Bold", 32, x=160),
    zit("§ 200 Abs. 1 S. 1 StPO: „Zeit und Ort ihrer Begehung“", 160, 221, beim("fe1", "obwohl")),
    *neinz("2. Tat zu ungenau beschrieben, etwa:", 270, "fe2", "Bold", 32, x=160),
    blk(160, 322, 990, 76, HELLROT, "fe3", [("„Unger hat im Frühjahr in Ahornstadt Schmuck gestohlen.“", "Bold", 30, INK)]),
    *wb,
    z("worüber das Gericht urteilt · wie weit der Strafklageverbrauch reicht", 110, wb_y + 20, "umgr2", size=30),
    blk(110, wb_y + 76, 1040, 76, ROT, "unw", [("fehlt die Umgrenzung: Anklage unwirksam, Verfahren einstellen", "ExtraBold", 30, INK)]),
    zit("BGH, Beschl. v. 21.12.2021 – StB 39/21, Rn. 17", 110, wb_y + 162, beim("unw", "unwirksam")),
    *requisit([("fehler", ("tabler", "alert-triangle", 100, HELLROT), "typische Fehler", HELLROT),
               ("fe1", ("tabler", "calendar-event", 100, WEISS), "Zeit und Ort fehlen", HELLROT),
               ("fe2", ("tabler", "search", 100, WEISS), "zu ungenau", HELLROT),
               ("umgr", ("tabler", "map-pin", 100, ROT), "unverwechselbar", GELB),
               ("umgr2", ("tabler", "building-bank", 120, BLAU), "Strafklageverbrauch", WEISS),
               ("unw", ("tabler", "x", 90, None), "unwirksam", HELLROT)]),
    *stehend("HI", X1, [("fehler", "sorge"), ("umgr", "denkt"), ("unw", "staunt")]),
    *stehend("EN", X2, [("fehler", "ernst"), ("umgr2", "denkt"), ("unw", "still")]),
]))

# ===========================================================================================================================
# M Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · erst das Gutachten"), ("tipp1", "Klausurtipp · Tateinheit oder Tatmehrheit"),
       ("tipp2", "Klausurtipp · passt alles zum Gutachten?")], [
    *tafel("tipp", "Klausurtipp: Reihenfolge der Arbeit", fill=HELL, h=680, size=44),
    warnung_i(150, 225, "tipp", gr=26),
    z("1. Anklagesatz erst, wenn dein Gutachten steht", 200, 205, "tipp", "Bold", 34),
    z("2. mehrere Gesetzesverletzungen:", 200, 300, "tipp1", "Bold", 34),
    z("Tateinheit oder Tatmehrheit angeben", 200, 350, beim("tipp1", "Tateinheit"), size=32),
    zit("Nr. 110 Abs. 2 lit. c RiStBV", 200, 398, beim("tipp1", "Tatmehrheit")),
    z("3. Prüfe am Ende: Passen Paragrafenkette,", 200, 470, "tipp2", "Bold", 34),
    z("Gericht und Antrag zu deinem Gutachten?", 200, 520, beim("tipp2", "Gericht"), "Bold", 34),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# N Schema
# ===========================================================================================================================
REIHEN = [("s1", 0, "I. Kopf, Personalien, Verteidiger", True),
          ("s2t", 0, "II. Anklagesatz", True),
          ("s2a", 1, "1. Einleitung mit Zeit und Ort, gesetzliche Merkmale", False),
          ("s2b", 1, "2. konkreter Tatvorwurf", False),
          ("s2c", 1, "3. Paragrafenkette", False),
          ("s3", 0, "III. Beweismittel", True),
          ("s4", 0, "IV. Wesentliches Ergebnis der Ermittlungen", True),
          ("s5", 0, "V. Antrag auf Eröffnung vor dem zuständigen Gericht", True)]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Schema: Anklageschrift nach § 200 StPO"), 110, 90, "sch", 46)]
y = 210
for c, ebene, text, fett in REIHEN:
    x = (130, 200)[ebene]
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 40 if ebene == 0 else 36, rechts=1800))
    y += {0: 96, 1: 80}[ebene]
assert y <= 990, y
folie([("sch", "Schema"), ("s1", "Schema › I. Kopf, Personalien, Verteidiger"), ("s2t", "Schema › II. Anklagesatz"),
       ("s3", "Schema › III. Beweismittel"), ("s4", "Schema › IV. wesentliches Ergebnis"),
       ("s5", "Schema › V. Antrag auf Eröffnung")], els_sch)

# ===========================================================================================================================
# O Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Der ", 0), ("Anklagesatz", "a"), (" umgrenzt die Tat:", 0)],
                 [("wer, wann, wo, was und", "b")], [("nach welcher Vorschrift.", 0)]], 750, 290, 46, "merke",
                {"a": beim("merke", "Anklagesatz"), "b": beim("merke", "wer")}),
    *markertext([[("Danach folgen ", 0), ("Beweismittel", "c"), (",", 0)],
                 [("wesentliches Ergebnis", "d"), (" und", 0)],
                 [("der ", 0), ("Antrag auf Eröffnung", "e"), (".", 0)]], 750, 560, 46, "m2",
                {"c": beim("m2", "Beweismittel"), "d": beim("m2", "wesentliches"), "e": beim("m2", "Antrag")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
