"""Folge 264 · Begleitverfügung StA: Haft, Pflichtverteidiger, Mitteilungen – Serienstandard Open Peeps (Katzenkönig).
Fall: Donnerstagmorgen, Staatsanwaltschaft Ahornstadt (erfunden, wie Folge 252). Referendarin Ortlieb hat die Anklage gegen
Herrn Wittig fertig (Einbruch in das Lager eines Baumarkts, Werkzeug für 7.800 €); Wittig sitzt seit dem 9.7.2026 in
Untersuchungshaft (Fluchtgefahr), hat eine Pflichtverteidigerin. Zweite Anzeige von Herrn Dengler (E-Bike) ohne
hinreichenden Tatverdacht. Oberstaatsanwältin Pfaff fragt nach der Begleitverfügung. Szenen laut ../SZENENPLAN.md:
A Büro (Akte mit Haftvermerk, Pfaff schaut zur Tür herein), B1 In der Akte (Baumarktlager, Kamera, Transporter, Haftbefehl,
Festnahme – Haft nur als Symbol: Akte mit rotem Haftvermerk, keine Zelle), B2 Anzeige Dengler (Hof, E-Bike), B3 Frage,
C Sachverhalt, D Wozu die Begleitverfügung, E Kopf und I. Vermerk (§ 169a, Wortlaut), F1 II. Teileinstellung (§ 170 Abs. 2,
Wortlautkarte), F2 Bescheid (§ 171 S. 1, Wortlautkarte), G1 III. Haft (Fortdauer), G2 Sechsmonatsfrist (§ 121 Abs. 1,
Wortlautkarte), H IV. Pflichtverteidigung (§ 140 Abs. 1 Nr. 4, 5, Wortlautkarte), I V. Mitteilungen und Asservate,
J VI. Anklage mit den Akten an das Gericht (Pfaff liest gegen), K zwei typische Fehler, L Klausurtipp (Lexi), M Schema,
N Merksatz (Lexi). Eigenes Muster der Verfügung (kein Anbieter-Muster). Kein Richterhammer (Gericht als Säulengebäude).
Ein Handlungsgeräusch (Tür; ../geraeusche_herkunft.json). Namensschild jeder Figur, solange sie im Bild ist.
Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/flurboden/tisch/requisit/stehend/muster als eigene
Kopie aus Folge 252 (gemeinsame Dateien unverändert). Zahlen auf Tafeln, Pillen und Blasen als Ziffern. Wortlautkarten
wörtlich nach gesetze-im-internet.de (Abruf 08.10.2026; amtliche Schreibung „Abschluß“)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_264/"

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
HAFTROT = (215, 60, 45, 255)
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
        if n.startswith(("bild:", "ficon:", "bank")) or "/op_264/" in n:
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 249/252) -----------------------------------
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


BODEN_T = (214, 206, 192, 255)               # Steinboden (Lager, Hof)
BODEN_H = (222, 196, 160, 255)               # Holzboden im Büro
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


X1, X2 = 1400, 1745                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"OR": "Referendarin Ortlieb", "PF": "OStAin Pfaff", "WI": "Herr Wittig", "DE": "Herr Dengler"}
NFARBE = {"OR": HELLGRUEN, "PF": BLAUHELL, "WI": WEISS, "DE": LILAHELL}
for _a, _b, _xa, _xb in (("OR", "PF", X1, X2), ("OR", "DE", X1, X2)):   # Schilder nebeneinander dürfen sich nicht berühren
    assert _xa + F("Bold", 30).getlength(NAME[_a]) / 2 + 30 + 12 < _xb - F("Bold", 30).getlength(NAME[_b]) / 2 - 30


def requisit(folge, px=PX, py=PY, pu=PU):
    """Wechselndes Requisit über den Figuren: folge = [(cue, (set, icon, breite, fuell), pillentext, pillenfarbe[, bis])]."""
    els = []
    for i, eintrag in enumerate(folge):
        c, ic, txt, pf = eintrag[:4]
        b = eintrag[4] if len(eintrag) > 4 else (folge[i + 1][0] if i + 1 < len(folge) else None)
        if ic:
            s_, n_, br, fu = ic
            els.append(ficon(s_, n_, px, pu, br, c, fuell=fu, bis=b))
        if txt:
            els.append(pl(txt, px, py, c, fill=pf, size=28, anker="m", bis=b))
    return els


def stehend(k, x, folge, unten=FB, hoehe=FR, bis=None):
    return [*fig(k, x, unten, hoehe, folge, bis=bis), ns(NAME[k], x, unten, folge[0][0], NFARBE[k], d=0.1)]


def muster(x, y, w, cue, zeilen, size=30, bis=None):
    """Musterblatt der Begleitverfügung (eigenes Muster, kein Anbieter-Muster): weißes Blatt mit roter Randlinie.
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


def haftvermerk(x, y, cue, size=30, **k):
    """Roter Vermerk „Haft“ (Nr. 52 RiStBV) als Pille mit weißer Schrift."""
    return pl("Haft", x, y, cue, fill=HAFTROT, size=size, farbe=WEISS, **k)


# ===========================================================================================================================
# A Fall: Donnerstagmorgen im Büro der Referendarin (Akte mit Haftvermerk; Pfaff schaut zur Tür herein)
# ===========================================================================================================================
ORX, PFX, TX = 1010, 1440, 1680             # Ortlieb (neben dem Tisch), Pfaff (in der Tür), Tür
AKX = 600                                   # Akte auf dem Schreibtisch


def buero(c0, tuer_auf=None, mit_tuer_geraeusch=False):
    """Büro der Referendarin: Holzboden, Aktenschrank, Wandkalender, Pflanze, Tür rechts (anders als 252: kein
    Fenster, kein Bücherregal)."""
    els = [hart(flurboden(c0, BODEN_H, fugen=False)),
           hart(ficon("tabler", "archive", 170, F_O + 8, 230, c0, fuell=(196, 140, 92, 255), anim="cut")),
           hart(ficon("tabler", "calendar-event", 210, 430, 170, c0, fuell=WEISS, anim="cut")),
           hart(ficon("tabler", "plant-2", 1230, F_O + 8, 150, c0, fuell=GRUEN, anim="cut"))]
    if tuer_auf is None:
        els.append(hart(ficon("tabler", "door", TX, F_O + 8, 420, c0, fuell=(255, 238, 180, 255), anim="cut")))
    else:
        els.append(hart(ficon("tabler", "door", TX, F_O + 8, 420, c0, fuell=HOLZ, anim="cut", bis=tuer_auf)))
        auf = ficon("tabler", "door", TX, F_O + 8, 420, tuer_auf, fuell=(255, 238, 180, 255), anim="cut")
        els.append(szene(auf, "264tuer*", 0.7, 0.0) if mit_tuer_geraeusch else hart(auf))
    return els


def schreibtisch(c0, haft_ab=None, anklage_ab=None):
    """Schreibtisch mit Akte (roter Haftvermerk) und fertiger Anklage."""
    els = [hart(karte(360, 700, 560, 34, c0, fill=HOLZ, rund=8, schatten=4, rand=4, anim="cut")),
           hart(linienzug([(410, 736), (410, F_O)], c0, breite=10)),
           hart(linienzug([(870, 736), (870, F_O)], c0, breite=10)),
           hart(ficon("tabler", "folder", AKX, 702, 150, c0, fuell=GELB, anim="cut"))]
    if haft_ab is not None:
        els.append(haftvermerk(AKX, 600, haft_ab, size=30, anker="m"))
    if anklage_ab is not None:
        els.append(ficon("tabler", "file-check", 790, 702, 110, anklage_ab, fuell=WEISS))
    return els


P0 = "Fall"
folie([(NULL, f"{P0} · Staatsanwaltschaft Ahornstadt"), ("ortlieb", f"{P0} · Referendarin Ortlieb"),
       ("haft", f"{P0} · Akte mit Haftvermerk"), ("pfaff", f"{P0} · Oberstaatsanwältin Pfaff"),
       ("p1", f"{P0} · „Wo ist Ihre Begleitverfügung?“"), ("o1", f"{P0} · Was gehört hinein?")], [
    *buero(NULL, tuer_auf="pfaff", mit_tuer_geraeusch=True),
    hart(pl("Donnerstagmorgen: Staatsanwaltschaft Ahornstadt", 70, 30, NULL, fill=GELB, size=40)),
    *schreibtisch(NULL, haft_ab="haft", anklage_ab=beim("ortlieb", "Anklage")),
    *fig("OR", ORX, FU, FH, [("ortlieb", "froh_r"), ("p1", "sorge_r")], bis="o1", erst="pop"),
    *redet("OR_redet_r", ORX, FU, FH, "o1", "akte"),
    ns("Referendarin Ortlieb", ORX, FU, "ortlieb", HELLGRUEN, d=0.1),
    *fig("PF", PFX, FU, FH, [(beim("pfaff", "Oberstaatsanwältin"), "ruhig")], bis="p1", erst="pop"),
    *redet("PF_redet", PFX, FU, FH, "p1", "o1"),
    *fig("PF", PFX, FU, FH, [("o1", "denkt")], bis="akte", erst="cut"),
    ns("Oberstaatsanwältin Pfaff", PFX, FU, beim("pfaff", "Oberstaatsanwältin"), BLAUHELL, d=0.1),
    blase("sprech", 760, 270, "p1", 1180, 245, inhalt=["Die Anklage ist gut. Aber Herr Wittig", "sitzt seit 3 Monaten in Untersuchungshaft.",
          "Wo ist Ihre Begleitverfügung?"], textsize=31, figur=("PF_redet", PFX, FU, FH), bis="o1"),
    blase("sprech", 600, 220, "o1", 700, 250, inhalt=["Die fehlt noch. Was gehört", "denn da hinein?"],
          textsize=32, figur=("OR_redet_r", ORX, FU, FH), bis="akte"),
])

# ===========================================================================================================================
# B1 In der Akte: Einbruch ins Baumarktlager, Kamera, Transporter, Haftbefehl, Festnahme (Haft nur als Symbol)
# ===========================================================================================================================
LGX, WKX, TRX, WIX = 300, 640, 960, 1560    # Lager, Werkzeug, Transporter, Herr Wittig
folie([("akte", "Fall · In der Akte"), ("lager", "Fall · Einbruch ins Baumarktlager"), ("kamera", "Fall · Kamera zeigt Herrn Wittig"),
       ("transp", "Fall · Werkzeug im Transporter"), ("hb", "Fall · Haftbefehl wegen Fluchtgefahr"),
       ("fest", "Fall · 9.7.2026: Festnahme, Pflichtverteidigerin")], [
    hart(flurboden("akte", BODEN_T)),
    pl("In der Akte", 70, 30, "akte", fill=GELB, size=40),
    ficon("tabler", "folders", 960, 760, 260, "akte", fuell=GELB, anim="cut", bis="lager"),
    haftvermerk(960, 470, "akte", size=34, anker="m", bis="lager"),
    ficon("tabler", "building-warehouse", LGX, F_O + 8, 400, "lager", fuell=GELB),
    ficon("tabler", "tools", WKX, F_O + 8, 140, beim("lager", "Werkzeug"), fuell=BLAU, bis="transp"),
    pl("Nacht zum 21.6.2026: Einbruch ins Lager eines Baumarkts", 70, 105, "lager", fill=WEISS, size=32),
    pl("Werkzeug für 7.800 € mitgenommen", 70, 172, beim("lager", "Werkzeug"), fill=HELLROT, size=32),
    ficon("tabler", "device-cctv", LGX + 205, 700, 90, "kamera", fuell=WEISS),
    pl("Kamera zeigt Herrn Wittig", 70, 239, "kamera", fill=WEISS, size=32),
    ficon("tabler", "truck", TRX, F_O + 8, 300, "transp", fuell=WEISS),
    ficon("tabler", "tools", TRX - 55, 860, 95, "transp", fuell=BLAU),
    ring(TRX - 55, 812, 80, 66, beim("transp", "Transporter"), bis="hb"),
    pl("Werkzeug im Transporter gefunden", 70, 306, "transp", fill=WEISS, size=32),
    pl("Wohnung gekündigt, Flug gebucht: Haftbefehl wegen Fluchtgefahr", 70, 373, "hb", fill=WEISS, size=32),
    pl("9.7.2026: Festnahme und Vorführung · seitdem Pflichtverteidigerin", 70, 440, "fest", fill=WEISS, size=32),
    *requisit([("hb", ("tabler", "plane-departure", 110, WEISS), "Flug gebucht", WEISS),
               (beim("hb", "Haftbefehl"), ("tabler", "file-text", 100, WEISS), "Haftbefehl: Fluchtgefahr", HELLROT),
               ("fest", ("tabler", "folder", 120, GELB), None, None),
               (beim("fest", "Pflichtverteidigerin"), ("tabler", "briefcase", 100, WEISS), "Pflichtverteidigerin", WEISS)],
              px=WIX, py=170, pu=390),
    haftvermerk(WIX, 160, "fest", size=30, anker="m", bis=beim("fest", "Pflichtverteidigerin")),
    *fig("WI", WIX, FU, FH, [("kamera", "ruhig"), ("hb", "ernst"), ("fest", "still")], erst="pop"),
    ns("Herr Wittig", WIX, FU, "kamera", WEISS, d=0.1),
])

# ===========================================================================================================================
# B2 In der Akte: Anzeige von Herrn Dengler (E-Bike im Hof), Wittig bestreitet; angeklagt nur der Einbruch
# ===========================================================================================================================
BKX, DEX = 250, 940
folie([("dengler", "Fall · Anzeige von Herrn Dengler"), ("d1", "Fall · „Der war doch auch bei uns“"),
       ("d2", "Fall · Wittig bestreitet"), ("nur", "Fall · angeklagt: nur der Einbruch")], [
    hart(flurboden("dengler", BODEN_T, fugen=False)),
    pl("In der Akte: eine zweite Anzeige", 70, 30, "dengler", fill=GELB, size=40),
    ficon("tabler", "fence", BKX, F_O + 8, 380, "dengler", fuell=(222, 196, 160, 255), anim="cut"),
    ficon("ph", "bicycle-bold", BKX + 300, F_O + 8, 230, "dengler", fuell=BLAU, anim="cut", bis=beim("dengler", "verschwunden")),
    ring(BKX + 300, F_O - 100, 135, 95, beim("dengler", "verschwunden"), bis="d2"),
    pl("Anzeige von Herrn Dengler: E-Bike im Mai aus dem Hof verschwunden", 70, 105, "dengler", fill=WEISS, size=32),
    pl("Wittig bestreitet · mehr gibt die Akte nicht her", 70, 172, "d2", fill=WEISS, size=32),
    pl("Angeklagt: nur der Einbruch", 70, 239, "nur", fill=GRUEN, size=32),
    *fig("DE", DEX, FU, FH, [("dengler", "ruhig_r")], bis="d1", erst="pop"),
    *redet("DE_redet_r", DEX, FU, FH, "d1", "d2"),
    *fig("DE", DEX, FU, FH, [("d2", "muede_r")], bis="frage", erst="cut"),
    ns("Herr Dengler", DEX, FU, "dengler", LILAHELL, d=0.1),
    *fig("WI", WIX, FU, FH, [("dengler", "ruhig"), ("d1", "ernst"), ("d2", "still")], erst="cut"),
    ns("Herr Wittig", WIX, FU, "dengler", WEISS),
    blase("sprech", 640, 210, "d1", 1330, 300, inhalt=["Der war damals doch auch", "bei uns in der Straße!"], textsize=32,
          figur=("DE_redet_r", DEX, FU, FH), bis="d2"),
    *requisit([("nur", ("tabler", "file-check", 100, WEISS), "Anklage: Einbruch", GRUEN)], px=WIX, py=170, pu=390),
])

# ===========================================================================================================================
# B3 Die Frage (zurück im Büro)
# ===========================================================================================================================
folie([("frage", "Fall · Die Frage")], [
    *buero("frage"),
    *schreibtisch("frage", haft_ab="frage", anklage_ab="frage"),
    *fig("OR", ORX, FU, FH, [("frage", "denkt_r")], erst="cut"),
    ns("Referendarin Ortlieb", ORX, FU, "frage", HELLGRUEN),
    *fig("PF", PFX, FU, FH, [("frage", "ruhig")], erst="cut"),
    ns("Oberstaatsanwältin Pfaff", PFX, FU, "frage", BLAUHELL),
    pl("Was gehört neben der Anklage", 70, 30, "frage", fill=PINK, size=38),
    pl("in die Begleitverfügung –", 70, 102, beim("frage", "Begleitverfügung"), fill=PINK, size=38),
    pl("und wie vermeidest du Widersprüche?", 70, 174, beim("frage", "und"), fill=PINK, size=38),
])

# ===========================================================================================================================
# C Sachverhalt
# ===========================================================================================================================
def sachverhalt_264(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 205
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=33, zeilenabstand=1.3)
        els += e; y += 16
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_264("sv", [
    "Herr Wittig (38) soll in der Nacht zum 21. Juni 2026 in das Lager eines Baumarkts in Ahornstadt eingebrochen sein und "
    "Werkzeug für 7.800 € mitgenommen haben. Eine Kamera zeigt ihn; das Werkzeug findet die Polizei in seinem Transporter. "
    "Es ist fotografiert, die Aufnahme liegt auf einem USB-Stick bei den Akten.",
    "Weil er seine Wohnung gekündigt und einen Flug gebucht hat, erlässt das Amtsgericht Haftbefehl wegen Fluchtgefahr. "
    "Am 9. Juli wird er festgenommen und vorgeführt; seitdem ist er in Untersuchungshaft und hat eine Pflichtverteidigerin.",
    "Herr Dengler zeigt ihn außerdem an: Im Mai sei aus seinem Hof ein E-Bike verschwunden. Als Beschuldigter vernommen, "
    "bestreitet Wittig; weitere Beweise gibt es nicht.",
    "Am 8. Oktober 2026 ist die Anklage zum Schöffengericht wegen des Einbruchs fertig.",
], "Was gehört in die Begleitverfügung – ohne Widerspruch zur Anklage?")

# ===========================================================================================================================
# D Wozu die Begleitverfügung?
# ===========================================================================================================================
PD = "Begleitverfügung"
folie([("wozu", f"{PD} › Wozu?"), ("anklage", f"{PD} › Anklage: an das Gericht"), ("bv", f"{PD} › Verfügung: was die StA veranlasst"),
       ("kein", f"{PD} › kein Widerspruch zur Anklage"), ("land", f"{PD} › Form: von Land zu Land")], rechts_frei([
    *tafel("wozu", "Wozu die Begleitverfügung?", h=840, size=46),
    blk(110, 190, 1040, 130, BLAUHELL, "anklage", [("Anklageschrift: geht an das Gericht,", "ExtraBold", 34, INK),
                                                    ("beschreibt die angeklagte Tat", "Regular", 34, INK)]),
    blk(110, 350, 1040, 130, HELLGRUEN, "bv", [("Begleitverfügung: ordnet an, was die", "ExtraBold", 34, INK),
                                               ("Staatsanwaltschaft daneben veranlasst", "Regular", 34, INK)]),
    *neinz("nie ein Widerspruch zur Anklage", 520, "kein", "Bold", 34, x=160),
    blk(110, 620, 1040, 130, GELB, "land", [("Form: von Land zu Land verschieden –", "ExtraBold", 32, INK),
                                            ("maßgeblich: Hinweise deines Prüfungsamts", "ExtraBold", 32, INK)]),
    *requisit([("wozu", ("tabler", "clipboard-list", 100, WEISS), "Begleitverfügung", GELB),
               ("anklage", ("tabler", "building-bank", 120, BLAU), "Anklage: an das Gericht", WEISS),
               ("bv", ("tabler", "clipboard-list", 100, GRUEN), "Verfügung: daneben", WEISS),
               ("kein", ("tabler", "x", 90, None), "kein Widerspruch", HELLROT),
               ("land", ("tabler", "map-pin", 100, ROT), "Prüfungsamt", GELB)]),
    *stehend("OR", X1, [("wozu", "ruhig"), ("bv", "denkt"), ("land", "fest")]),
    *stehend("PF", X2, [("wozu", "ruhig"), ("kein", "ernst")]),
]))

# ===========================================================================================================================
# E Kopf und I. Vermerk über den Abschluss der Ermittlungen (§ 169a StPO)
# ===========================================================================================================================
PM = "Muster"
m1, m1_y = muster(80, 160, 1100, "kopf", [
    ("Staatsanwaltschaft Ahornstadt · 52 Js 1418/26 · 8.10.2026", "kopf", "Regular", "text"),
    ("Verfügung", "kopf", "ExtraBold", "text"),
    ("", "kopf", "", "abstand"),
    ("I. Vermerk: Die Ermittlungen sind abgeschlossen.", "v1", "Bold", "text"),
])
W169 = ["„Erwägt die Staatsanwaltschaft, die öffentliche Klage zu",
        "erheben, so vermerkt sie den Abschluß der Ermittlungen",
        "in den Akten.“"]
w169, w169_y = wortlaut(80, m1_y + 24, 1100, W169, "§ 169a StPO", "v1w", marken=[
    (1, "vermerkt", beim("v1w", "vermerkt")), (1, "Abschluß der Ermittlungen", beim("v1w", "Abschluss"))], size=32)
folie([("kopf", f"{PM} › Kopf: Vermerk „Haft“"), ("v1", f"{PM} › I. Vermerk, § 169a StPO"),
       ("v1f", f"{PM} › I. Folge: volle Akteneinsicht")], rechts_frei([
    *tafel("kopf", "Kopf und I. Vermerk", h=860, size=46),
    *m1,
    haftvermerk(1040, 182, "kopf", size=30),
    zit("Nr. 52 RiStBV: alle Verfügungen mit Vermerk „Haft“", 420, 234, beim("kopf2", "Verfügungen")),
    *w169,
    blk(110, w169_y + 26, 1040, 120, HELLGRUEN, "v1f", [("ab jetzt: Akteneinsicht nicht mehr wegen", "ExtraBold", 32, INK),
                                                       ("des Untersuchungszwecks versagbar", "ExtraBold", 32, INK)]),
    zit("§ 147 Abs. 2 S. 1 StPO", 110, w169_y + 156, beim("v1f", "Untersuchungszweck")),
    *requisit([("kopf", ("tabler", "rubber-stamp", 110, WEISS), "Haft", HELLROT),
               ("v1", ("tabler", "file-check", 100, WEISS), "Ermittlungen abgeschlossen", WEISS),
               ("v1f", ("tabler", "eye", 100, WEISS), "Akteneinsicht", GRUEN)]),
    *stehend("OR", X1, [("kopf", "fest"), ("v1f", "staunt")]),
    *stehend("PF", X2, [("kopf", "ruhig"), ("v1", "ernst")]),
]))

# ===========================================================================================================================
# F1 II. Teileinstellung (§ 170 Abs. 2 StPO, Wortlautkarte), Mitteilung an den Beschuldigten, § 154 StPO
# ===========================================================================================================================
W170 = ["„(2) Andernfalls stellt die Staatsanwaltschaft das Verfahren",
        "ein. Hiervon setzt sie den Beschuldigten in Kenntnis, wenn",
        "er als solcher vernommen worden ist oder ein Haftbefehl",
        "gegen ihn erlassen war; …“"]
w170, w170_y = wortlaut(80, 228, 1100, W170, "§ 170 Abs. 2 S. 1, 2 StPO", "e2", marken=[
    (0, "Andernfalls", beim("e2", "Andernfalls")), (0, "stellt die Staatsanwaltschaft das Verfahren", beim("e2", "stellt")),
    (1, "in Kenntnis", beim("e3", "erfährt")), (2, "als solcher vernommen", beim("e3", "vernommen"))], size=31)
m2, m2_y = muster(80, w170_y + 24, 1100, beim("e2", "stellt"), [
    ("II. Das Verfahren wird eingestellt, soweit es den Diebstahl", beim("e2", "stellt"), "Bold", "text"),
    ("des E-Bikes von Herrn Dengler betrifft (§ 170 Abs. 2 StPO).", beim("e2", "Verfahren"), "Bold", "text"),
    ("Mitteilung an den Beschuldigten", "e3", "Regular", "text"),
])
PE = f"{PM} › II. Teileinstellung"
folie([("e", f"{PE}"), ("e1", f"{PE} › andere Tat, kein Verdacht"), ("e2", f"{PE} › § 170 Abs. 2 StPO"),
       ("e3", f"{PE} › Mitteilung an Wittig"), ("e154", f"{PE} › Alternative: § 154 StPO")], rechts_frei([
    *tafel("e", "II. Teileinstellung", h=880, size=46),
    *neinz("E-Bike: andere Tat – Verdacht reicht nicht für eine Anklage", 166, "e1", "Bold", 32, x=160),
    *m2,
    *w170,
    blk(110, m2_y + 22, 1040, 120, GELB, "e154", [("nachweisbar, aber daneben nicht beträchtlich", "ExtraBold", 32, INK),
                                                   ("ins Gewicht: Absehen nach § 154 Abs. 1 StPO", "ExtraBold", 32, INK)]),
    *requisit([("e", ("tabler", "clipboard-list", 100, WEISS), "II. Teileinstellung", GELB),
               ("e1", ("ph", "bicycle-bold", 130, BLAU), "andere Tat: E-Bike", WEISS),
               ("e2", ("tabler", "file-x", 100, WEISS), "eingestellt", HELLROT),
               ("e3", ("tabler", "mail", 100, WEISS), "Mitteilung an Wittig", WEISS),
               ("e154", ("tabler", "scale", 110, WEISS), "§ 154 StPO", GELB)]),
    *stehend("OR", X1, [("e", "fest"), ("e1", "denkt"), ("e3", "ruhig")]),
    *stehend("PF", X2, [("e", "ruhig"), ("e2", "ernst"), ("e154", "denkt")]),
]))

# ===========================================================================================================================
# F2 II. Bescheid an Herrn Dengler (§ 171 S. 1 StPO, Wortlautkarte), Belehrung (§ 171 S. 2, § 172 Abs. 1 StPO)
# ===========================================================================================================================
W171 = ["„Gibt die Staatsanwaltschaft einem Antrag auf Erhebung der",
        "öffentlichen Klage keine Folge oder verfügt sie nach dem",
        "Abschluß der Ermittlungen die Einstellung des Verfahrens,",
        "so hat sie den Antragsteller unter Angabe der Gründe zu",
        "bescheiden. …“"]
w171, w171_y = wortlaut(80, 160, 1100, W171, "§ 171 S. 1 StPO", "e4", marken=[
    (2, "Einstellung des Verfahrens", beim("e4", "Bescheid")), (3, "Antragsteller", beim("e4", "Bescheid")),
    (3, "unter Angabe der Gründe", beim("e4", "Gründen"))], size=31)
m3, m3_y = muster(80, w171_y + 24, 1100, beim("e4", "Bescheid"), [
    ("Bescheid an Herrn Dengler mit Gründen", beim("e4", "Bescheid"), "Bold", "text"),
    ("Belehrung: Beschwerde binnen 2 Wochen", "e5", "Bold", "text"),
])
folie([("e4", f"{PE} › Bescheid, § 171 StPO"), ("e5", f"{PE} › Belehrung des Verletzten")], rechts_frei([
    *tafel("e4", "II. Bescheid an den Anzeigenden", h=880, size=44),
    *w171,
    *m3,
    zit("keine Floskel: Nr. 89 Abs. 2 RiStBV", 110, m3_y + 12, beim("e4", "Floskel")),
    zit("§ 171 S. 2, § 172 Abs. 1 StPO", 110, m3_y + 52, beim("e5", "Frist")),
    *requisit([("e4", ("tabler", "mail", 100, WEISS), "Bescheid mit Gründen", WEISS),
               ("e5", ("tabler", "calendar-event", 100, WEISS), "Beschwerde: 2 Wochen", GELB)]),
    *stehend("OR", X1, [("e4", "fest"), ("e5", "ruhig")]),
    *stehend("DE", X2, [("e4", "muede"), ("e5", "ruhig")]),
]))

# ===========================================================================================================================
# G1 III. Haft: Voraussetzungen noch da? Fortdauerantrag in der Anklageschrift (Nr. 110 Abs. 4 RiStBV)
# ===========================================================================================================================
m4, m4_y = muster(80, 160, 1100, "h", [
    ("III. Haft", "h", "ExtraBold", "text"),
    ("Dringender Tatverdacht und Fluchtgefahr bestehen fort;", "h1", "Regular", "text"),
    ("die Haft ist verhältnismäßig.", beim("h1", "verhältnismäßig"), "Regular", "text"),
    ("Fortdauer: bestimmter Antrag in der Anklageschrift,", "h2", "Regular", "text"),
    ("mit Ort und Dauer der Haft", beim("h2", "Ort"), "Regular", "text"),
])
PH = f"{PM} › III. Haft"
folie([("h", f"{PH}"), ("h1", f"{PH} › Voraussetzungen noch da?"), ("h2", f"{PH} › Fortdauerantrag in der Anklage"),
       ("h3", f"{PH} › Verfügung passt zur Anklage")], rechts_frei([
    *tafel("h", "III. Haft", h=840, size=46),
    *m4,
    zit("§ 120 Abs. 1 StPO; Nr. 54 Abs. 1 RiStBV", 110, m4_y + 10, beim("h1", "verhältnismäßig")),
    zit("Nr. 110 Abs. 4 RiStBV", 110, m4_y + 48, beim("h2", "Richtlinien")),
    *okz("Verfügung und Anklage passen zusammen", m4_y + 110, "h3", "Bold", 34, x=160),
    *requisit([("h", ("tabler", "folder", 120, GELB), None, None),
               ("h1", ("tabler", "scale", 110, WEISS), "verhältnismäßig?", WEISS),
               ("h2", ("tabler", "file-text", 100, WEISS), "Anklage: Fortdauerantrag", WEISS),
               ("h3", ("tabler", "check", 100, None), "passt", GRUEN)]),
    haftvermerk(PX, 170, "h", size=30, anker="m", bis="h1"),
    *stehend("OR", X1, [("h", "ruhig"), ("h1", "denkt"), ("h3", "froh")]),
    *stehend("PF", X2, [("h", "ernst"), ("h3", "froh")]),
]))

# ===========================================================================================================================
# G2 III. Sechsmonatsfrist (§ 121 Abs. 1 StPO, Wortlautkarte), Frist notieren, OLG
# ===========================================================================================================================
W121 = ["„(1) Solange kein Urteil ergangen ist, das auf Freiheitsstrafe",
        "oder eine freiheitsentziehende Maßregel der Besserung und",
        "Sicherung erkennt, darf der Vollzug der Untersuchungshaft",
        "wegen derselben Tat über sechs Monate hinaus nur aufrecht-",
        "erhalten werden, wenn die besondere Schwierigkeit oder der",
        "besondere Umfang der Ermittlungen oder ein anderer wichtiger",
        "Grund das Urteil noch nicht zulassen und die Fortdauer der",
        "Haft rechtfertigen.“"]
w121, w121_y = wortlaut(80, 155, 1100, W121, "§ 121 Abs. 1 StPO", "h121", marken=[
    (3, "über sechs Monate hinaus", beim("h4", "sechs")), (4, "besondere Schwierigkeit", beim("h4", "Schwierigkeit")),
    (5, "besondere Umfang der Ermittlungen", beim("h4", "Umfang")), (5, "anderer wichtiger", beim("h4", "wichtiger")),
    (6, "Grund", beim("h4", "Grund")), (6, "Fortdauer der", beim("h4", "Fortdauer")),
    (7, "Haft rechtfertigen", beim("h4", "rechtfertigen"))], size=30)
m5, m5_y = muster(80, w121_y + 18, 1100, "h5", [
    ("Frist § 121: 6 Monate ab 9.7.2026, Ablauf Anfang Januar 2027", "h5", "Bold", "text"),
    ("notiert – Akten rechtzeitig zum OLG, wenn die Haft länger dauert", "h6", "Regular", "text"),
], size=29)
folie([("h121", f"{PH} › Sechsmonatsfrist, § 121 Abs. 1 StPO"), ("h5", f"{PH} › Ablauf Anfang Januar 2027"),
       ("h6", f"{PH} › Frist notieren, Vorlage an das OLG")], rechts_frei([
    *tafel("h121", "III. Die Sechsmonatsfrist", h=900, size=46),
    *w121,
    *m5,
    zit("§ 122 Abs. 1 StPO; Nr. 56 Abs. 1 RiStBV", 110, m5_y + 8, beim("h6", "Oberlandesgericht")),
    *requisit([("h121", ("tabler", "hourglass", 100, GELB), "6 Monate", GELB),
               ("h5", ("tabler", "calendar-event", 100, WEISS), "Anfang Januar 2027", WEISS),
               ("h6", ("tabler", "building-bank", 120, BLAU), "Oberlandesgericht", WEISS)]),
    *stehend("OR", X1, [("h121", "fest"), ("h5", "denkt"), ("h6", "fest")]),
    *stehend("PF", X2, [("h121", "ruhig"), ("h6", "ernst")]),
]))

# ===========================================================================================================================
# H IV. Pflichtverteidigung (§ 140 Abs. 1 Nr. 4, 5 StPO, Wortlautkarte)
# ===========================================================================================================================
W140 = ["„(1) Ein Fall der notwendigen Verteidigung liegt vor, wenn …",
        "4. der Beschuldigte nach den §§ 115, 115a, 128 Absatz 1",
        "oder § 129 einem Gericht zur Entscheidung über Haft oder",
        "einstweilige Unterbringung vorzuführen ist;",
        "5. der Beschuldigte sich auf Grund richterlicher Anordnung",
        "oder mit richterlicher Genehmigung in einer Anstalt",
        "befindet; …“"]
w140, w140_y = wortlaut(80, 160, 1100, W140, "§ 140 Abs. 1 Nr. 4, 5 StPO", "pv1", marken=[
    (0, "notwendigen Verteidigung", beim("pv1", "notwendig")), (2, "zur Entscheidung über Haft", beim("pv1", "Entscheidung")),
    (3, "vorzuführen ist", beim("pv1", "vorzuführen")), (4, "5.", beim("pv2", "Nummer")),
    (4, "richterlicher Anordnung", beim("pv2", "richterliche")), (5, "in einer Anstalt", beim("pv2", "Anstalt"))], size=30)
m6, m6_y = muster(80, w140_y + 18, 1100, "pv3", [
    ("IV. Pflichtverteidigerin seit 9.7.2026 bestellt", "pv3", "Bold", "text"),
    ("fehlt sie: StA beantragt unverzüglich die Bestellung", "pv4", "Regular", "text"),
])
PV = f"{PM} › IV. Pflichtverteidigung"
folie([("pv", f"{PV}"), ("pv1", f"{PV} › § 140 Abs. 1 Nr. 4: Vorführung"), ("pv2", f"{PV} › Nr. 5: in der Anstalt"),
       ("pv3", f"{PV} › bestellt seit der Vorführung"), ("pv4", f"{PV} › fehlt sie: Antrag der StA")], rechts_frei([
    *tafel("pv", "IV. Pflichtverteidigung", h=880, size=46),
    *w140,
    *m6,
    zit("§ 141 Abs. 2 S. 1 Nr. 1, § 143 Abs. 1 StPO", 110, m6_y + 8, beim("pv3", "Abschluss")),
    zit("§ 142 Abs. 2 StPO", 700, m6_y + 8, beim("pv4", "unverzüglich")),
    *requisit([("pv", ("tabler", "briefcase", 100, WEISS), "Pflichtverteidigung", GELB),
               ("pv1", ("tabler", "building-bank", 120, BLAU), "Vorführung: Haft", WEISS),
               ("pv2", ("tabler", "folder", 120, GELB), None, None),
               ("pv3", ("tabler", "briefcase", 100, GRUEN), "bestellt: 9.7.2026", GRUEN),
               ("pv4", ("tabler", "file-text", 100, WEISS), "Antrag der StA", WEISS)]),
    haftvermerk(PX, 170, "pv2", size=30, anker="m", bis="pv3"),
    *stehend("OR", X1, [("pv", "fest"), ("pv2", "denkt"), ("pv3", "froh")]),
    *stehend("PF", X2, [("pv", "ruhig"), ("pv4", "ernst")]),
]))

# ===========================================================================================================================
# I V. Mitteilungen und Asservate
# ===========================================================================================================================
m7, m7_y = muster(80, 160, 1100, "mi", [
    ("V. Mitteilungen und Asservate", "mi", "ExtraBold", "text"),
    ("1. Verteidigerin zugleich mit dem Beschuldigten unterrichten", "mi1", "Regular", "text"),
    ("2. Mitteilungen nach der MiStra, soweit vorgesehen", "mi2", "Regular", "text"),
    ("", "mi", "", "abstand"),
    ("3. Werkzeug zurück an den Baumarkt, dem es entzogen wurde", beim("as1", "Baumarkt"), "Bold", "text"),
    ("4. USB-Stick mit der Aufnahme bleibt verwahrt (Beweismittel)", "as2", "Bold", "text"),
])
PI = f"{PM} › V. Mitteilungen und Asservate"
folie([("mi", f"{PI}"), ("mi1", f"{PI} › Verteidigerin zugleich"), ("mi2", f"{PI} › MiStra"),
       ("as1", f"{PI} › Werkzeug zurück an den Baumarkt"), ("as2", f"{PI} › USB-Stick bleibt verwahrt")], rechts_frei([
    *tafel("mi", "V. Mitteilungen und Asservate", h=840, size=46),
    *m7,
    zit("Nr. 108 RiStBV; § 145a Abs. 1 StPO", 110, m7_y + 12, beim("mi1", "zugleich")),
    zit("Anordnung über Mitteilungen in Strafsachen (MiStra)", 110, m7_y + 50, beim("mi2", "Strafsachen")),
    zit("§ 111n Abs. 1, 2, 4 StPO; Nr. 75 Abs. 1 RiStBV", 110, m7_y + 88, beim("as1", "entzogen")),
    blk(110, m7_y + 140, 1040, 76, HELLGRUEN, "as1",
        [("das Verfahren braucht es nicht mehr im Original", "Bold", 30, INK)]),
    *requisit([("mi", ("tabler", "mail-forward", 100, WEISS), "Mitteilungen", GELB),
               ("mi1", ("tabler", "briefcase", 100, WEISS), "Verteidigerin zugleich", WEISS),
               ("mi2", ("tabler", "mailbox", 110, WEISS), "MiStra", WEISS),
               ("as1", ("tabler", "tools", 120, BLAU), "zurück an den Baumarkt", GRUEN),
               ("as2", ("tabler", "device-usb", 90, WEISS), "Beweismittel", GELB)]),
    *stehend("OR", X1, [("mi", "ruhig"), ("mi2", "denkt"), ("as1", "fest")]),
    *stehend("PF", X2, [("mi", "ernst"), ("as2", "ruhig")]),
]))

# ===========================================================================================================================
# J VI. Anklage mit den Akten an das Gericht; Pfaff liest gegen
# ===========================================================================================================================
m8, m8_y = muster(80, 160, 1100, "vi", [
    ("VI. Anklageschrift mit den Akten an das", "vi", "Bold", "text"),
    ("Amtsgericht Ahornstadt – Schöffengericht –", beim("vi", "Amtsgericht"), "Bold", "text"),
])
PJ = f"{PM} › VI. Anklage mit den Akten an das Gericht"
folie([("vi", f"{PJ}"), ("vi1", f"{PM} › VI. § 199 Abs. 2 S. 2 StPO"), ("p2", "Fall · Pfaff liest gegen")], rechts_frei([
    *tafel("vi", "VI. Anklage an das Gericht", h=840, size=46),
    *m8,
    *okz("Mit ihr werden die Akten dem Gericht vorgelegt.", m8_y + 30, "vi1", "Bold", 32, x=160),
    zit("§ 199 Abs. 2 S. 2 StPO", 160, m8_y + 78, beim("vi1", "Paragraf")),
    blk(110, m8_y + 140, 1040, 76, HELLGRUEN, "p2", [("Verfügung passt zur Anklage – Punkt für Punkt", "ExtraBold", 32, INK)]),
    *requisit([("vi", ("tabler", "building-bank", 120, BLAU), "Amtsgericht Ahornstadt", WEISS),
               ("vi1", ("tabler", "folders", 110, GELB), "mit den Akten", WEISS, "p2")]),
    *stehend("OR", X1, [("vi", "fest"), ("p2", "froh")]),
    *fig("PF", X2, FB, FR, [("vi", "ruhig")], bis="p2"),
    *redet("PF_redet2", X2, FB, FR, "p2", "fehler"),
    ns(NAME["PF"], X2, FB, "vi", NFARBE["PF"], d=0.1),
    blase("sprech", 660, 230, "p2", 1560, 220, inhalt=["Gut. Jetzt passt die Verfügung", "zur Anklage, Punkt für Punkt."],
          textsize=31, figur=("PF_redet2", X2, FB, FR)),
]))

# ===========================================================================================================================
# K Zwei typische Fehler
# ===========================================================================================================================
PF_ = "Typische Fehler"
folie([("fehler", f"{PF_}"), ("f1", f"{PF_} › 1. Teil der angeklagten Tat eingestellt"), ("f1c", f"{PF_} › 1. nur eine andere Tat"),
       ("f2", f"{PF_} › 2. Sechsmonatsfrist übersehen"), ("f2c", f"{PF_} › 2. Vorlage vor Ablauf: Frist ruht")], rechts_frei([
    *tafel("fehler", "Zwei typische Fehler", h=880, size=46),
    *neinz("1. Teil der angeklagten Tat nach § 170 Abs. 2 eingestellt", 175, "f1", "Bold", 31, x=160),
    blk(160, 228, 990, 70, HELLROT, "f1b", [("Widerspruch zur Anklage", "ExtraBold", 31, INK)]),
    z("eingestellt wird nur eine andere Tat; innerhalb derselben", 160, 318, "f1c", size=31),
    z("Tat allenfalls Beschränkung nach § 154a StPO", 160, 362, beim("f1c", "innerhalb"), size=31),
    zit("§ 264 Abs. 1, § 154a Abs. 1 StPO; Nr. 101a RiStBV", 160, 408, beim("f1c", "Beschränkung")),
    *neinz("2. Sechsmonatsfrist übersehen", 470, "f2", "Bold", 31, x=160),
    z("nach Ablauf: Haftbefehl aufheben – außer das OLG ordnet", 160, 523, "f2b", size=31),
    z("die Fortdauer an oder der Vollzug wird ausgesetzt", 160, 567, beim("f2b", "Oberlandesgericht"), size=31),
    zit("§ 121 Abs. 2 StPO", 160, 613, beim("f2b", "ausgesetzt")),
    *okz("Akten vor Ablauf beim OLG: Frist ruht bis zur Entscheidung", 662, "f2c", "Bold", 31, x=160),
    zit("§ 121 Abs. 3 S. 1 StPO", 160, 712, beim("f2c", "ruht")),
    *requisit([("fehler", ("tabler", "alert-triangle", 100, HELLROT), "typische Fehler", HELLROT),
               ("f1", ("tabler", "file-x", 100, WEISS), "Widerspruch", HELLROT),
               ("f1c", ("ph", "bicycle-bold", 130, BLAU), "nur andere Tat", WEISS),
               ("f2", ("tabler", "hourglass", 100, HELLROT), "Frist übersehen", HELLROT),
               ("f2c", ("tabler", "building-bank", 120, BLAU), "Frist ruht", GRUEN)]),
    *stehend("OR", X1, [("fehler", "sorge"), ("f1c", "denkt"), ("f2", "staunt"), ("f2c", "fest")]),
    *stehend("PF", X2, [("fehler", "ernst"), ("f2c", "ruhig")]),
]))

# ===========================================================================================================================
# L Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · alles nebeneinanderlegen"), ("tipp1", "Klausurtipp · jede Tat angeklagt oder eingestellt"),
       ("tipp2", "Klausurtipp · nur, was verlangt ist")], [
    *tafel("tipp", "Klausurtipp: der Abgleich", fill=HELL, h=680, size=44),
    warnung_i(150, 225, "tipp", gr=26),
    z("1. Gutachten, Anklage und Begleitverfügung", 200, 205, "tipp", "Bold", 34),
    z("nebeneinanderlegen", 200, 255, beim("tipp", "nebeneinander"), size=34),
    z("2. Jede Tat: angeklagt oder eingestellt –", 200, 345, "tipp1", "Bold", 34),
    z("keine doppelt, keine vergessen", 200, 395, beim("tipp1", "keine"), size=34),
    z("3. Nur anordnen, was Akte oder", 200, 485, "tipp2", "Bold", 34),
    z("Bearbeitervermerk verlangen", 200, 535, beim("tipp2", "Bearbeitervermerk"), "Bold", 34),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# M Schema
# ===========================================================================================================================
REIHEN = [("s1", "I. Vermerk über den Abschluss der Ermittlungen"),
          ("s2", "II. Teileinstellung mit Mitteilung und Bescheid"),
          ("s3", "III. Haft: Fortdauer und Sechsmonatsfrist"),
          ("s4", "IV. Pflichtverteidigung"),
          ("s5", "V. Mitteilungen und Asservate"),
          ("s6", "VI. Anklage mit den Akten ans Gericht")]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Schema: Begleitverfügung der Staatsanwaltschaft"), 110, 90, "sch", 46)]
y = 230
for c, text in REIHEN:
    els_sch.append(z(text, 130, y, c, "ExtraBold", 42, rechts=1800))
    y += 110
assert y <= 990, y
folie([("sch", "Schema"), ("s1", "Schema › I. Vermerk"), ("s2", "Schema › II. Teileinstellung"), ("s3", "Schema › III. Haft"),
       ("s4", "Schema › IV. Pflichtverteidigung"), ("s5", "Schema › V. Mitteilungen und Asservate"),
       ("s6", "Schema › VI. Anklage ans Gericht")], els_sch)

# ===========================================================================================================================
# N Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Die ", 0), ("Anklage", "a"), (" sagt dem Gericht,", 0)],
                 [("was angeklagt ist.", "b")]], 750, 300, 48, "merke",
                {"a": beim("merke", "Anklage"), "b": beim("merke", "angeklagt")}),
    *markertext([[("Die ", 0), ("Begleitverfügung", "c"), (" erledigt", 0)],
                 [("alles daneben", "d"), (" und widerspricht", 0)],
                 [("der Anklage ", 0), ("nie", "e"), (".", 0)]], 750, 520, 48, "m2",
                {"c": beim("m2", "Begleitverfügung"), "d": beim("m2", "alles"), "e": beim("m2", "nie")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
