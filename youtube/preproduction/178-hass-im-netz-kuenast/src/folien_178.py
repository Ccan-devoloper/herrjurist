"""Folge 178 · Hass im Netz: Wann schützt die Meinungsfreiheit? Fall Künast – Serienstandard Open Peeps (Katzenkönig).
Fiktiver Rahmen: Sprechstunde bei Professor Ruhland mit dem Studenten Mattes; der Hook (Stadträtin) nur als Text.
Danach der echte Fall sachlich: BVerfG, Beschl. v. 19.12.2021 – 1 BvR 1073/20 (nur mit Rn.), Maßstäbe aus 1 BvR 2397/19.
HÖCHSTE SENSIBILITÄT: keine Beschimpfung wörtlich, angedeutet oder verpixelt – nur die Pille „derbe sexistische
Beschimpfungen“; keine Figur und kein Porträt realer Personen (auch kein Personen-Icon), keine Partei-, Plattform- oder
Social-Media-Logos, nur neutrale Icons (Sprechblase, Bild, Gericht, Datenbank, Waage). Szenen laut ../SZENENPLAN.md.
Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/neinz2/tisch/requisit/stehend/paar/spricht_neben
als eigene Kopie aus Folge 154 (gemeinsame Dateien unverändert). Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from ostil import titel, karte, pille
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_178/"

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
        if n.startswith(("bild:", "ficon:", "bank")) or "/op_178/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def wortlaut(x, y, w, zeilen, quelle, cue, marken=(), size=32, bis=None):
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 04.10.2026), als Zitat mit Normangabe;
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


def neinz2(text, y, cue, kreuz, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile zum Satzbeginn, Kreuz erst zur gesprochenen Verneinung (kreuz = Cue des Wortes „nicht“)."""
    return [nein(x - 45, y + 20, kreuz, gr=gr), z(text, x, y, cue, stil, size, **k)]


# --- eigene Szenenbausteine (programmatisch, Palettenflächen, Tuschekontur) ---------------------------------------------------
def _flaeche(w, h):
    s = 2
    im = Image.new("RGBA", ((w + 12) * s, (h + 12) * s))
    return im, ImageDraw.Draw(im), s






def tisch(x, breite, cue):
    """Schreibtisch aus Grundformen (Holzplatte, zwei Beine) auf dem Boden."""
    im, dr, s = _flaeche(breite, 210)
    o = 6 * s
    dr.rounded_rectangle((o, o, o + breite * s, o + 34 * s), 8 * s, fill=HOLZ, outline=INK, width=5 * s)
    for xx in (o + 30 * s, o + (breite - 52) * s):
        dr.rectangle((xx, o + 34 * s, xx + 22 * s, o + 210 * s), fill=HOLZ, outline=INK, width=5 * s)
    im = im.resize((breite + 12, 222), Image.LANCZOS)
    return hart(El(im, x, BODEN - 216, cue, "cut", 0.0, None, name="tisch"))


BODEN = 860
FH = 440                                    # stehende Figur in der Fallszene
X1, X2 = 1430, 1730                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"MA": "Mattes", "RU": "Prof. Ruhland"}
NFARBE = {"MA": BLAU, "RU": GRUEN}


def boden(cue):
    return hart(linienzug([(40, BODEN), (1880, BODEN)], cue, breite=7, farbe=INK))


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
    return rechts_frei([*fig(k, x, FB, FR, folge, bis=bis), bis_(ns(NAME[k], x, FB, folge[0][0], NFARBE[k], d=0.1), bis)])


def paar(a, af, b, bf):
    """Tafelszene: zwei Figuren rechts der Tafel (beide blicken nach links zur Tafel)."""
    return [*stehend(a, X1, af), *stehend(b, X2, bf)]


def spricht_neben(k, x, cue, bis, davor, danach, zeilen, size=32, cy=250, w=600, h=200, cx=None):
    """Figur neben der Tafel spricht (Grundbild bis cue, Rede cue→bis, danach Folge); Blase über den Figuren."""
    els = [*fig(k, x, FB, FR, davor, bis=cue)] if davor else []
    els += redet(f"{k}_redet", x, FB, FR, cue, bis)
    els += fig(k, x, FB, FR, danach, erst="cut")
    els.append(blase("sprech", w, h, cue, cx or 1560, cy, inhalt=zeilen, textsize=size, figur=(f"{k}_redet", x, FB, FR),
                     bis=bis))
    return rechts_frei(els)



# ===========================================================================================================================
# A Fall: Sprechstunde bei Professor Ruhland (fiktiv) – Regal links, Schreibtisch mit Bericht, Mattes blickt nach rechts
# zu Professor Ruhland, Ruhland blickt nach links zu Mattes. Der Hook (Stadträtin) steht nur als Text auf dem Bericht.
# ===========================================================================================================================
MAX, RUX = 1300, 1680
TISCH_X, TISCH_B = 470, 560
TISCH_O = BODEN - 216 + 8                   # Oberkante der Tischplatte
BER = (420, 60, 700, 480)                   # Bericht (Inhalt des Ausdrucks) über dem Schreibtisch


def regal(x, cue, breite=300, hoehe=600):
    """Bücherregal aus Grundformen (Holzrahmen, drei Böden, Buchrücken in Palettenfarben)."""
    im, dr, s = _flaeche(breite, hoehe)
    o = 6 * s
    dr.rounded_rectangle((o, o, o + breite * s, o + hoehe * s), 6 * s, fill=HOLZ, outline=INK, width=5 * s)
    farben = [ROT, BLAU, GELB, GRUEN, LILA, WEISS, BLAU, ROT, GRUEN]
    fach = (hoehe - 20) // 3
    k = 0
    for i in range(3):
        y0 = o + (10 + i * fach) * s
        dr.rectangle((o + 14 * s, y0 + 10 * s, o + (breite - 14) * s, y0 + (fach - 8) * s), fill=(250, 238, 220, 255),
                     outline=INK, width=4 * s)
        xx = o + 24 * s
        for j in range(6 - i % 2):
            bw = (26 + (j * 7 + i * 5) % 14) * s
            bh = (fach - 40 - (j * 11 + i * 3) % 30) * s
            dr.rectangle((xx, y0 + (fach - 12) * s - bh, xx + bw, y0 + (fach - 12) * s), fill=farben[k % len(farben)],
                         outline=INK, width=4 * s)
            xx += bw + 8 * s; k += 1
    im = im.resize((breite + 12, hoehe + 12), Image.LANCZOS)
    return hart(El(im, x, BODEN - hoehe - 6, cue, "cut", 0.0, None, name="regal"))


def bericht(cue, voll=False, extra=None):
    """Der ausgedruckte Bericht als Karte: Überschrift, Kommentarzeile mit neutralen Sprechblasen-Icons und der Pille
    „derbe sexistische Beschimpfungen“ (keine Beschimpfung wörtlich), Auskunftswunsch; ab ru1 die Fundstelle."""
    x, y, w, h = BER
    c_titel = cue if voll else beim("hook", "Beitrag")
    c_komm = cue if voll else beim("hook", "derbe")
    c_ausk = cue if voll else "hook2"
    c_fund = cue if voll else beim("ru1", "Künast")
    els = [karte(x, y, w, h, cue, fill=WEISS, rund=18, schatten=6, rand=4),
           z("Bericht", x + 30, y + 18, cue, "ExtraBold", 36, rechts=x + w - 20),
           linienzug([(x, y + 78), (x + w, y + 78)], cue, breite=4),
           z("Beitrag über eine Stadträtin", x + 30, y + 95, c_titel, "Bold", 32, rechts=x + w - 20)]
    for i in range(3):
        els.append(ficon("tabler", "message-circle", x + 60 + i * 70, y + 205, 56, c_komm, fuell=HELLROT))
    els += [pl("derbe sexistische Beschimpfungen", x + 30, y + 220, c_komm, fill=HELLROT, size=30),
            pl("Auskunft: Wer hat das geschrieben?", x + 30, y + 295, c_ausk, fill=HELL, size=30),
            zit("Fall Künast: BVerfG, Beschl. v. 19.12.2021", x + 30, y + 368, c_fund, rechts=x + w - 20),
            zit("1 BvR 1073/20", x + 30, y + 402, c_fund, rechts=x + w - 20)]
    if extra:
        els += extra
    if voll:
        els = [hart(e) for e in els]
    return els


def ausdruck_auf_tisch(cue):
    return hart(ficon("tabler", "file-text", TISCH_X + 280, TISCH_O, 90, cue, fuell=WEISS, anim="cut"))


folie([(NULL, "Fall · Die Sprechstunde"), ("hook", "Fall · Beschimpfungen unter einem Beitrag"),
       ("hook2", "Fall · Die Auskunft"), ("ma1", "Die Frage · Muss sie das aushalten?"),
       ("ru1", "Die Frage · Der Fall Künast")], [
    boden(NULL),
    regal(70, NULL),
    tisch(TISCH_X, TISCH_B, NULL),
    hart(ficon("tabler", "device-laptop", TISCH_X + 130, TISCH_O, 150, NULL, fuell=BLAUHELL, anim="cut")),
    # Mattes legt den ausgedruckten Bericht auf den Schreibtisch (gleitet von seiner Seite auf die Platte)
    szene(bewegt(ficon("tabler", "file-text", TISCH_X + 280, TISCH_O, 90, "hook", fuell=WEISS, anim="cut"),
                 ("hook", 0.05), ("hook", 0.55), 300, -40), "178papier*", 0.9, 0.415),
    *bericht("hook"),
    # Mattes blickt zu Professor Ruhland (nach rechts)
    *fig("MA", MAX, BODEN, FH, [(NULL, "ruhig_r"), ("hook", "ernst_r")], bis="ma1", erst="cut"),
    *redet("MA_redet_r", MAX, BODEN, FH, "ma1", "ru1"),
    *fig("MA", MAX, BODEN, FH, [("ru1", "denkt_r")], erst="cut"),
    hart(ns("Mattes", MAX, BODEN, NULL, BLAU)),
    # Professor Ruhland blickt zu Mattes (nach links)
    *fig("RU", RUX, BODEN, FH, [(NULL, "ruhig"), ("hook2", "ernst")], bis="ru1", erst="cut"),
    *redet("RU_redet", RUX, BODEN, FH, "ru1", "echt"),
    hart(ns("Prof. Ruhland", RUX, BODEN, NULL, GRUEN)),
    blase("sprech", 600, 190, "ma1", 1430, 300, inhalt=["Muss eine Politikerin so", "etwas nicht aushalten?"],
          textsize=31, figur=("MA_redet_r", MAX, BODEN, FH), bis="ru1"),
    blase("sprech", 660, 270, "ru1", 1480, 250, inhalt=["So ähnlich argumentierte das", "Kammergericht im Fall Künast.",
                                                     "Das Bundesverfassungsgericht", "hob die Beschlüsse auf."],
          textsize=30, figur=("RU_redet", RUX, BODEN, FH), bis="echt"),
])

# ===========================================================================================================================
# B1 Der echte Fall: Beitrag, Kommentare, Antrag auf Auskunft (1 BvR 1073/20, Rn. 1–8) – ohne Figuren, neutrale Icons
# ===========================================================================================================================
folie([("echt", "Der echte Fall · Der Beitrag"), ("komm", "Der echte Fall · Die Kommentare"),
       ("antrag", "Der echte Fall · Der Antrag auf Auskunft"), ("vor", "Der echte Fall · Die Voraussetzung")], [
    boden("echt"),
    pl("Der echte Fall: Fall Künast", 70, 40, "echt", fill=GELB, size=34),
    pl("2019: ein Beitrag mit dem Bild einer Politikerin", 70, 118, "beitrag", fill=WEISS, size=30),
    pl("und einem Zitat, das so nicht von ihr stammt", 70, 188, beim("beitrag", "Zitat"), fill=WEISS, size=30),
    pl("darunter Kommentare: derbe sexistische Beschimpfungen", 70, 258, "komm", fill=HELLROT, size=30),
    pl("Antrag beim Landgericht Berlin: Auskunft über die Daten der Verfasser", 70, 328, "antrag", fill=WEISS, size=30),
    zit("damals § 14 Abs. 3 TMG a. F., heute § 21 Abs. 2, 3 TDDDG · BVerfG, 1 BvR 1073/20, Rn. 1 f., 8", 80, 400,
        beim("antrag", "Daten"), rechts=1850),
    pl("Voraussetzung: z. B. Beleidigung (§ 185 StGB), nicht gerechtfertigt", 70, 450, "vor", fill=HELL, size=30),
    zit("Rn. 2", 80, 522, "vor"),
    ficon("tabler", "photo", 260, BODEN, 170, "beitrag", fuell=BLAUHELL),
    ficon("tabler", "quote", 430, BODEN - 120, 80, beim("beitrag", "Zitat"), fuell=HELL),
    *[ficon("tabler", "message-circle", 640 + i * 105, BODEN - (i % 2) * 40, 100, beim("komm", "Kommentare"), fuell=HELLROT)
      for i in range(3)],
    ficon("tabler", "building-bank", 1150, BODEN, 170, "antrag", fuell=WEISS),
    ficon("tabler", "database", 1390, BODEN, 120, beim("antrag", "Daten"), fuell=BLAUHELL),
    ficon("tabler", "scale", 1650, BODEN, 160, "vor", fuell=GELB),
])

# ===========================================================================================================================
# B2 Der Weg durch die Instanzen und die Entscheidung des BVerfG (Rn. 9–16; Tenor)
# ===========================================================================================================================
folie([("lg", "Der echte Fall · Landgericht"), ("kg", "Der echte Fall · Landgericht und Kammergericht"),
       ("zehn", "Der echte Fall · 10 Kommentare: Nein"), ("bverfg", "Der echte Fall · Bundesverfassungsgericht"),
       ("frage", "Die Frage · Wann schützt die Meinungsfreiheit?")], [
    *tafel("lg", "Der Weg durch die Instanzen"),
    *neinz("Landgericht, 9.9.2019: alles zulässig,", 180, "lg", "Bold", 34, x=160),
    z("weil die Kommentare einen Sachbezug hätten", 160, 226, beim("lg", "Sachbezug"), size=33),
    zit("BVerfG, 1 BvR 1073/20, Rn. 9", 160, 272, beim("lg", "Sachbezug")),
    *okz("LG (21.1.2020) und KG (11.3.2020):", 320, "kg", "Bold", 34, x=160),
    z("Auskunft für 12 von 22 Kommentaren", 160, 366, beim("kg", "zwölf"), size=33),
    zit("Rn. 10 f.", 160, 412, beim("kg", "zwölf")),
    *neinz("10 Kommentare: keine Schmähkritik", 460, "zehn", "Bold", 34, x=160),
    z("teils: als Politikerin hinzunehmen", 160, 506, beim("hinnehmen", "Politikerin"), size=33),
    zit("Rn. 11–15", 160, 552, beim("hinnehmen", "Politikerin")),
    blk(110, 600, 1040, 80, GRUEN, "bverfg", [("BVerfG, 19.12.2021: Persönlichkeitsrecht verletzt", "ExtraBold", 33, INK)]),
    z("Beschlüsse des KG aufgehoben, Kammergericht entscheidet neu", 110, 695, "auf", size=32),
    zit("1 BvR 1073/20, Tenor; Art. 2 Abs. 1 i. V. m. Art. 1 Abs. 1 GG", 110, 740, "auf"),
    pl("Wann schützt die Meinungsfreiheit solche Kommentare?", 110, 790, "frage", fill=PINK, size=32),
    *requisit([("lg", ("tabler", "building-bank", 170, WEISS), "Landgericht", WEISS),
               ("kg", ("tabler", "gavel", 170, HOLZ), "Kammergericht", WEISS),
               ("bverfg", ("tabler", "scale", 180, GELB), "Bundesverfassungsgericht", GRUEN),
               ("frage", ("tabler", "message-circle", 160, PINK), "Meinungsfreiheit?", PINK)], pu=640, py=260),
])


# ===========================================================================================================================
# C Sachverhalt
# ===========================================================================================================================
def sachverhalt_178(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=33, zeilenabstand=1.28)
        els += e; y += 16
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_178("sv", [
    "Anfang 2019 veröffentlicht ein Blogger auf einer Social-Media-Plattform einen Beitrag mit dem Bild einer bekannten "
    "Politikerin und einem ihr zugeschriebenen Zitat, das so nicht von ihr stammt. Im April und Mai 2019 kommentieren "
    "zahlreiche Nutzer den Beitrag, viele mit derben sexistischen Beschimpfungen.",
    "Die Politikerin beantragt beim Landgericht Berlin, der Plattform die Auskunft über die Daten der Verfasser von "
    "22 Kommentaren zu gestatten (§ 14 Abs. 3 TMG a. F., heute § 21 TDDDG). Das setzt voraus, dass die Kommentare etwa "
    "den Tatbestand des § 185 StGB erfüllen und nicht gerechtfertigt sind.",
    "Das Landgericht hält zunächst alle Kommentare für zulässig. Nach Abhilfe und Beschwerde gestatten Landgericht und "
    "Kammergericht die Auskunft zu 12 Kommentaren, zu 10 nicht: keine Schmähkritik. Die Politikerin erhebt "
    "Verfassungsbeschwerde (BVerfG, 1 BvR 1073/20).",
], "Wann schützt Art. 5 Abs. 1 GG solche Kommentare?")

# ===========================================================================================================================
# D1 1. Grundrechte: Wortlautkarten Art. 5 Abs. 1 Satz 1 und Abs. 2 GG (2397/19, Rn. 12, 14)
# ===========================================================================================================================
PG = "1. Grundrechte"
W5 = ["„(1) Jeder hat das Recht, seine Meinung in Wort, Schrift und",
      "Bild frei zu äußern und zu verbreiten …“"]
w5, w5_y = wortlaut(80, 175, 1100, W5, "Art. 5 Abs. 1 Satz 1 GG (Auszug)", "a5", marken=[
    (1, "äußern", beim("a5", "äußern")), (1, "verbreiten", beim("a5", "verbreiten"))], size=32)
W52 = ["„(2) Diese Rechte finden ihre Schranken in den Vorschriften der",
       "allgemeinen Gesetze, den gesetzlichen Bestimmungen zum Schutze",
       "der Jugend und in dem Recht der persönlichen Ehre.“"]
w52, w52_y = wortlaut(80, w5_y + 140, 1100, W52, "Art. 5 Abs. 2 GG", "a52", marken=[
    (0, "Schranken", beim("a52", "Schranken")), (1, "allgemeinen Gesetze", beim("a52", "allgemeinen"))], size=31)
folie([("a5", f"{PG} · Art. 5 Abs. 1 Satz 1 GG"), ("wert", f"{PG} › auch verletzende Werturteile"),
       ("a52", f"{PG} › Schranken, Art. 5 Abs. 2 GG")], [
    *tafel("a5", "1. Meinungsfreiheit und ihre Schranken"),
    *w5,
    *okz("auch polemische oder verletzende Werturteile", w5_y + 25, "wert", "Bold", 34, x=160),
    zit("BVerfG, 1 BvR 2397/19, Rn. 12", 160, w5_y + 75, beim("wert", "verletzende")),
    *w52,
    *requisit([("a5", ("tabler", "message-circle", 100, WEISS), "Meinungsfreiheit", GELB),
               ("wert", ("tabler", "shield-check", 100, BLAUHELL), "Werturteile", BLAUHELL),
               ("a52", ("tabler", "book", 100, WEISS), "Schranken", WEISS)]),
    *stehend("MA", FX, [("a5", "ruhig"), ("wert", "denkt"), ("a52", "ruhig")]),
])

# ===========================================================================================================================
# D2 § 185 als allgemeines Gesetz, Persönlichkeitsrecht, Wortlautkarte § 193 StGB (2397/19 Rn. 14; 1073/20 Rn. 20, 26)
# ===========================================================================================================================
W193 = ["„… Äußerungen …, welche zur Ausführung oder Verteidigung von",
        "Rechten oder zur Wahrnehmung berechtigter Interessen",
        "vorgenommen werden, … sind nur insofern strafbar, als das",
        "Vorhandensein einer Beleidigung aus der Form der Äußerung",
        "oder aus den Umständen, unter welchen sie geschah, hervorgeht.“"]
w193, w193_y = wortlaut(80, 470, 1100, W193, "§ 193 StGB (Auszug)", "p193", marken=[
    (1, "Wahrnehmung berechtigter Interessen", beim("p193", "Wahrnehmung"))], size=31)
folie([("p185", f"{PG} › § 185 StGB als allgemeines Gesetz"), ("apr", f"{PG} › Gegenüber: Persönlichkeitsrecht"),
       ("p193", f"{PG} › § 193 StGB, Wahrnehmung berechtigter Interessen")], [
    *tafel("p185", "Zwei Grundrechte, eine Strafnorm"),
    blk(110, 175, 1040, 72, BLAUHELL, "p185", [("§ 185 StGB ist ein allgemeines Gesetz", "ExtraBold", 34, INK)]),
    zit("1 BvR 2397/19, Rn. 14 · mehr: Folgen zum Lüth-Urteil und zur Beleidigung", 110, 257, "p185"),
    blk(110, 300, 1040, 110, LILAHELL, "apr", [("Gegenüber: Persönlichkeitsrecht,", "ExtraBold", 34, INK),
                                             ("Art. 2 Abs. 1 i. V. m. Art. 1 Abs. 1 GG", "ExtraBold", 34, INK)]),
    zit("1 BvR 1073/20, Rn. 20, 26", 110, 420, "apr"),
    *w193,
    zit("Über § 193 StGB wirkt die Meinungsfreiheit · 1 BvR 1073/20, Rn. 26", 110, w193_y + 10, beim("p193", "Wahrnehmung")),
    *requisit([("p185", ("tabler", "book-2", 100, ROT), "§ 185 StGB", WEISS),
               ("apr", ("tabler", "shield", 100, LILAHELL), "Persönlichkeitsrecht", LILAHELL),
               ("p193", ("tabler", "scale", 100, GELB), "§ 193 StGB", GELB)]),
    *stehend("RU", FX, [("p185", "ruhig"), ("apr", "ernst"), ("p193", "ruhig")]),
])

# ===========================================================================================================================
# E1 2. Der Kern: Abwägung als Regel, drei enge Ausnahmen (2397/19 Rn. 15, 17, 20; 1073/20 Rn. 29 f.)
# ===========================================================================================================================
PK = "2. Abwägung"
folie([("kern", f"{PK} · Der Kern"), ("regel", f"{PK} › Normalfall: Abwägung"),
       ("ausn", f"{PK} › Ausnahmen ohne Abwägung"), ("eng", f"{PK} › Ausnahmen eng")], [
    *tafel("kern", "2. Der Kern: Wann wird abgewogen?"),
    blk(110, 180, 1040, 110, GELB, "regel", [("Normalfall: Abwägung", "ExtraBold", 36, INK),
                                           ("von Ehre und Meinungsfreiheit", "ExtraBold", 34, INK)]),
    zit("BVerfG, 1 BvR 2397/19, Rn. 15; 1 BvR 1073/20, Rn. 29", 110, 302, "regel"),
    z("Nur ausnahmsweise ohne Abwägung:", 110, 370, "ausn", "Bold", 36),
    pl("Angriff auf die Menschenwürde", 110, 440, beim("ausn", "Menschenwürde"), fill=HELLROT, size=32),
    pl("Formalbeleidigung", 110, 520, beim("ausn", "Formalbeleidigung"), fill=LILAHELL, size=32),
    pl("Schmähung", 470, 520, beim("ausn", "Schmähung"), fill=BLAUHELL, size=32),
    zit("2397/19, Rn. 15, 17", 110, 600, beim("ausn", "Schmähung")),
    blk(110, 650, 1040, 80, HELL, beim("eng", "eng"), [("Diese Ausnahmen sind eng.", "ExtraBold", 36, INK)]),
    zit("2397/19, Rn. 20; 1073/20, Rn. 30", 110, 742, beim("eng", "eng")),
    *requisit([("kern", ("tabler", "scale", 110, WEISS), "Abwägung?", WEISS),
               ("regel", ("tabler", "scale", 110, GELB), "Normalfall", GELB),
               ("ausn", ("tabler", "alert-triangle", 100, HELLROT), "Ausnahmen", HELLROT),
               ("eng", ("tabler", "zoom-question", 100, HELL), "eng", HELL)]),
    *stehend("RU", FX, [("kern", "ruhig"), ("regel", "ernst"), ("eng", "denkt")]),
])

# ===========================================================================================================================
# E2 Die drei Ausnahmen im Einzelnen; sonst offene Abwägung (2397/19 Rn. 18, 19, 21, 22, 26 f.)
# ===========================================================================================================================
folie([("schmaeh", f"{PK} › Schmähung"), ("formal", f"{PK} › Formalbeleidigung"),
       ("mw", f"{PK} › Menschenwürde"), ("sonst", f"{PK} › sonst: umfassende Abwägung")], [
    *tafel("schmaeh", "Die drei Ausnahmen"),
    blk(110, 175, 1040, 110, BLAUHELL, "schmaeh", [("Schmähung: kein nachvollziehbarer Bezug", "ExtraBold", 33, INK),
                                                 ("zur Sache, nur Verächtlichmachen", "Regular", 32, INK)]),
    zit("BVerfG, 1 BvR 2397/19, Rn. 19", 110, 292, "schmaeh"),
    *neinz2("ausfällige Kritik allein: noch keine Schmähung", 335, "steig", beim("steig", "nicht"), "Bold", 33),
    zit("Rn. 18", 185, 380, beim("steig", "nicht")),
    blk(110, 420, 1040, 110, LILAHELL, "formal", [("Formalbeleidigung: krasse Schimpfwörter", "ExtraBold", 33, INK),
                                                ("mit Vorbedacht; es zählt die Form", "Regular", 32, INK)]),
    zit("Rn. 21", 110, 537, "formal"),
    blk(110, 575, 1040, 110, HELLROT, "mw", [("Menschenwürde: spricht den Kern", "ExtraBold", 33, INK),
                                           ("der Persönlichkeit ab", "Regular", 32, INK)]),
    zit("Rn. 22", 110, 692, "mw"),
    blk(110, 735, 1040, 72, HELLGRUEN, "sonst", [("Sonst: umfassende Abwägung", "ExtraBold", 34, INK)]),
    z("mit offenem Ergebnis", 110, 815, "offen", "Bold", 32),
    zit("Rn. 26 f.", 470, 822, "sonst"),
    *paar("MA", [("schmaeh", "ruhig"), ("steig", "denkt"), ("sonst", "ruhig")],
          "RU", [("schmaeh", "ernst"), ("formal", "ruhig"), ("mw", "ernst"), ("offen", "ruhig")]),
])

# ===========================================================================================================================
# F 3. Der Fehler im Fall Künast (1073/20 Rn. 40–48)
# ===========================================================================================================================
PF = "3. Der Fehler"
folie([("fehler", f"{PF} · im Fall Künast"), ("gleich", f"{PF} › Beleidigung = Schmähkritik?"),
       ("sach", f"{PF} › Sachbezug grenzt die Schmähung ab"), ("ausfall", f"{PF} › Abwägungsausfall"),
       ("politik", f"{PF} › „als Politikerin hinnehmen“")], [
    *tafel("fehler", "3. Der Fehler des Kammergerichts"),
    z("KG: Beleidigung nur, wenn bloß Herabsetzung", 110, 175, "gleich", "Bold", 34),
    z("und Schmähung", 110, 221, beim("gleich", "Schmähung"), "Bold", 34),
    blk(110, 275, 1040, 72, HELLROT, beim("gleich", "setzte"), [("Beleidigung mit Schmähkritik gleichgesetzt", "ExtraBold", 34, INK)]),
    zit("BVerfG, 1 BvR 1073/20, Rn. 40, 46", 110, 357, beim("gleich", "setzte")),
    *okz("Sachbezug grenzt vor allem die Schmähung ab,", 405, "sach", "Bold", 33),
    *neinz2("macht eine Äußerung aber nicht zulässig", 451, beim("sach", "zulässig"), beim("sach", "nicht"), size=33),
    zit("Rn. 44 f.", 185, 497, beim("sach", "nicht")),
    *neinz("Abwägung praktisch vollständig ausgefallen", 550, "ausfall", "Bold", 33),
    zit("Rn. 46", 185, 596, "ausfall"),
    *neinz2("„als Politikerin hinnehmen“: ersetzt keine Abwägung", 645, "politik", beim("politik", "keine"), "Bold", 32),
    zit("Rn. 47", 185, 691, beim("politik", "keine")),
    *paar("MA", [("fehler", "ruhig"), ("gleich", "denkt"), ("politik", "ernst")],
          "RU", [("fehler", "ernst"), ("sach", "ruhig"), ("ausfall", "ernst")]),
])

# ===========================================================================================================================
# G1 4. Kriterien der Abwägung (1073/20 Rn. 31–35; 2397/19 Rn. 32)
# ===========================================================================================================================
PA = "4. Kriterien"
folie([("krit", f"{PA} · der Abwägung"), ("beitr", f"{PA} › Beitrag zur Meinungsbildung?"),
       ("macht", f"{PA} › Machtkritik"), ("grenze", f"{PA} › nicht jede Beschimpfung"),
       ("pos", f"{PA} › Position der Person"), ("schutz", f"{PA} › öffentliches Interesse am Schutz")], [
    *tafel("krit", "4. Kriterien der Abwägung"),
    *plusminus("Beitrag zur öffentlichen Meinungsbildung", 110, 175, "beitr", True, size=33, stil="Bold"),
    *plusminus("nur Stimmungsmache gegen eine Person", 110, 221, beim("beitr", "leichter"), False, size=33, stil="Bold"),
    zit("Gewicht der Meinungsfreiheit · BVerfG, 1 BvR 1073/20, Rn. 31", 110, 267, beim("beitr", "leichter")),
    *okz("Machtkritik: besonders geschützt, bei Politikern", 315, "macht", "Bold", 33),
    z("sind die Grenzen der Kritik weiter", 185, 361, beim("macht", "Grenzen"), size=33),
    zit("Rn. 32 f.", 185, 407, beim("macht", "Grenzen")),
    *neinz("aber nicht jede persönliche Beschimpfung", 455, "grenze", "Bold", 33),
    zit("Rn. 34", 185, 501, "grenze"),
    z("Bundesminister: mehr zuzumuten als Lokalpolitiker", 110, 550, "pos", "Bold", 33),
    zit("1 BvR 2397/19, Rn. 32", 110, 596, "pos"),
    blk(110, 645, 1040, 110, GELB, "schutz", [("Schutz von Politikern: auch", "ExtraBold", 34, INK),
                                            ("im öffentlichen Interesse", "ExtraBold", 34, INK)]),
    zit("1 BvR 1073/20, Rn. 35", 110, 765, "schutz"),
    *paar("MA", [("krit", "ruhig"), ("macht", "denkt"), ("schutz", "ruhig")],
          "RU", [("krit", "ruhig"), ("grenze", "ernst"), ("schutz", "ruhig")]),
])

# ===========================================================================================================================
# G2 Form, Anlass, Verbreitung und Wirkung (1073/20 Rn. 36 f.)
# ===========================================================================================================================
folie([("form", f"{PA} › Form: schriftlich"), ("anlass", f"{PA} › Anlass"), ("wirk", f"{PA} › Verbreitung und Wirkung")], [
    *tafel("form", "Form, Anlass, Wirkung"),
    blk(110, 180, 1040, 80, BLAUHELL, "form", [("schriftlich, auch im Netz: mehr Bedacht", "ExtraBold", 34, INK)]),
    zit("BVerfG, 1 BvR 1073/20, Rn. 36", 110, 270, "form"),
    blk(110, 320, 1040, 80, LILAHELL, "anlass", [("Gab es einen nachvollziehbaren Anlass?", "ExtraBold", 34, INK)]),
    zit("Rn. 36", 110, 410, "anlass"),
    z("dauerhaft, für viele sichtbar: wiegt schwerer", 110, 470, beim("wirk", "dauerhafte"), "Bold", 33),
    z("Satz im kleinen Kreis: wiegt leichter", 110, 518, beim("wirk", "kleinen"), "Bold", 33),
    zit("Rn. 37", 110, 566, beim("wirk", "kleinen")),
    *requisit([("form", ("tabler", "writing", 110, BLAUHELL), "schriftlich", BLAUHELL),
               ("anlass", ("tabler", "search", 110, LILAHELL), "Anlass?", LILAHELL),
               ("wirk", ("tabler", "world", 110, HELLROT), "Breitenwirkung", HELLROT),
               (beim("wirk", "kleinen"), ("tabler", "messages", 110, WEISS), "kleiner Kreis", WEISS)]),
    *stehend("MA", FX, [("form", "ruhig"), ("anlass", "denkt"), ("wirk", "ruhig")]),
])

# ===========================================================================================================================
# H 5. § 188 StGB (Wortlautkarte) und § 192a StGB (BT-Drs. 19/17741, 19/20163, 19/31115)
# ===========================================================================================================================
P5 = "5. § 188 und § 192a StGB"
W188 = ["„(1) Wird gegen eine im politischen Leben des Volkes stehende",
        "Person öffentlich, in einer Versammlung oder durch Verbreiten",
        "eines Inhalts (§ 11 Absatz 3) eine Beleidigung (§ 185) aus",
        "Beweggründen begangen, die mit der Stellung des Beleidigten im",
        "öffentlichen Leben zusammenhängen, und ist die Tat geeignet, sein",
        "öffentliches Wirken erheblich zu erschweren, so ist die Strafe",
        "Freiheitsstrafe bis zu drei Jahren oder Geldstrafe. Das politische",
        "Leben des Volkes reicht bis hin zur kommunalen Ebene.“"]
w188, w188_y = wortlaut(80, 160, 1100, W188, "§ 188 Abs. 1 StGB", "p188", marken=[
    (1, "öffentlich", beim("p188", "öffentliche")), (2, "Beleidigung (§ 185)", beim("p188", "Beleidigung")),
    (3, "Beweggründen", beim("p188", "Motiv")), (5, "öffentliches Wirken erheblich zu erschweren", beim("p188", "Wirken")),
    (7, "bis hin zur kommunalen Ebene", beim("kommunal", "kommunalen"))], size=30)
folie([("p188", f"{P5} · § 188 StGB"), ("kommunal", f"{P5} › bis zur kommunalen Ebene"),
       ("neu", f"{P5} › seit dem Gesetz gegen Hasskriminalität"), ("p192a", f"{P5} › § 192a StGB")], [
    *tafel("p188", "5. Das StGB heute: § 188"),
    *w188,
    *okz("neu: auch die Beleidigung, kommunale Ebene", w188_y + 12, "neu", "Bold", 33, x=160),
    z("vorher nur üble Nachrede und Verleumdung", 160, w188_y + 54, beim("neu", "vorher"), size=33),
    zit("Gesetz gegen Hasskriminalität · BT-Drs. 19/17741, 19/20163", 160, w188_y + 96, beim("neu", "vorher")),
    blk(110, w188_y + 134, 1040, 68, LILAHELL, "p192a", [("§ 192a StGB: verhetzende Beleidigung", "ExtraBold", 33, INK)]),
    z("etwa wegen Herkunft oder Behinderung", 185, w188_y + 212, beim("p192a", "Herkunft"), size=32),
    *neinz2("das Geschlecht nennt die Vorschrift nicht", w188_y + 254, beim("p192a", "Geschlecht"),
            beim("p192a", "nicht"), size=32),
    *stehend("RU", FX, [("p188", "ruhig"), ("neu", "ernst"), ("p192a", "denkt")]),
])
assert w188_y + 254 + 46 <= 900, w188_y

# ===========================================================================================================================
# I 6. Lösung des Hooks: die Stadträtin (2397/19 Rn. 18 f., 32; 1073/20 Rn. 31, 34, 36 f.)
# ===========================================================================================================================
PL = "6. Lösung"
folie([("loes", f"{PL} · die Stadträtin"), ("kontext", f"{PL} › Schmähkritik nicht vorschnell"),
       ("abw", f"{PL} › Abwägung"), ("lokal", f"{PL} › Stadträtin"), ("tend", f"{PL} › Ergebnis: Tendenz")], [
    *tafel("loes", "6. Und die Stadträtin?"),
    *neinz2("Schmähkritik nicht vorschnell annehmen", 180, "kontext", beim("kontext", "nicht"), "Bold", 34),
    zit("BVerfG, 1 BvR 2397/19, Rn. 18 ff.", 185, 226, beim("kontext", "nicht")),
    z("In der Abwägung zählt:", 110, 280, "abw", "Bold", 34),
    pl("nichts zur Sache", 110, 335, beim("abw", "nichts"), fill=HELLROT, size=30),
    pl("sexistisch gegen ihre Person", 440, 335, beim("abw", "sexistisch"), fill=HELLROT, size=30),
    pl("für alle sichtbar im Netz", 110, 410, beim("abw", "sichtbar"), fill=HELLROT, size=30),
    zit("1 BvR 1073/20, Rn. 31, 34, 36 f.", 110, 480, beim("abw", "sichtbar")),
    z("Stadträtin: weniger zuzumuten als einer Ministerin", 110, 530, "lokal", "Bold", 33),
    zit("1 BvR 2397/19, Rn. 32", 110, 576, "lokal"),
    blk(110, 625, 1040, 110, HELLGRUEN, "tend", [("Viel spricht für eine Beleidigung", "ExtraBold", 34, INK),
                                               ("und damit für die Auskunft", "ExtraBold", 34, INK)]),
    zit("Abwägung im Einzelfall; Ergebnis nicht vorgegeben (2397/19, Rn. 27)", 110, 745, "tend"),
    *paar("MA", [("loes", "denkt"), ("tend", "ruhig")], "RU", [("loes", "ruhig"), ("abw", "ernst"), ("tend", "ruhig")]),
])

# ===========================================================================================================================
# K Zurück in der Sprechstunde (gleicher Schauplatz wie A: die Geschichte kehrt zur Ausgangsfrage zurück)
# ===========================================================================================================================
bx_, by_, bw_, bh_ = BER
folie([("ma2", "Zurück in der Sprechstunde · Die Frage"), ("ru2", "Zurück in der Sprechstunde · Die Antwort")], [
    boden("ma2"),
    regal(70, "ma2"),
    tisch(TISCH_X, TISCH_B, "ma2"),
    hart(ficon("tabler", "device-laptop", TISCH_X + 130, TISCH_O, 150, "ma2", fuell=BLAUHELL, anim="cut")),
    ausdruck_auf_tisch("ma2"),
    *bericht("ma2", voll=True),
    pl("nicht ohne Abwägung", bx_ + 30, by_ + 428, beim("ru2", "Abwägung"), fill=HELLGRUEN, size=28),
    *redet("MA_redet_r", MAX, BODEN, FH, "ma2", "ru2"),
    *fig("MA", MAX, BODEN, FH, [("ru2", "denkt_r"), (beim("ru2", "reine"), "ruhig_r")], erst="cut"),
    hart(ns("Mattes", MAX, BODEN, "ma2", BLAU)),
    *fig("RU", RUX, BODEN, FH, [("ma2", "ruhig")], bis="ru2", erst="cut"),
    *redet("RU_redet", RUX, BODEN, FH, "ru2", "tipp"),
    hart(ns("Prof. Ruhland", RUX, BODEN, "ma2", GRUEN)),
    blase("sprech", 600, 190, "ma2", 1430, 300, inhalt=["Also muss sie das nicht", "einfach aushalten?"],
          textsize=31, figur=("MA_redet_r", MAX, BODEN, FH), bis="ru2"),
    blase("sprech", 620, 230, "ru2", 1480, 260, inhalt=["Nicht ohne Abwägung.", "Und reine Herabsetzung",
                                                     "wiegt dabei wenig."], textsize=31,
          figur=("RU_redet", RUX, BODEN, FH), bis="tipp"),
])

# ===========================================================================================================================
# L Klausurtipp (Lexi): Prüfungsreihenfolge (2397/19 Rn. 15, 17, 23, 26; 1073/20 Rn. 28, 44–46)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · erst der Sinn: Tatsache oder Werturteil?"), ("tipp2", "Klausurtipp · Schmähkritik nur ausnahmsweise"),
       ("tipp3", "Klausurtipp · sonst Abwägung bei § 193 StGB"), ("tipp4", "Klausurtipp · Sachbezug heißt nicht zulässig")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("1. Sinn der Äußerung ermitteln:", 200, 200, beim("tipp", "Ermittle"), "Bold", 36),
    z("Tatsache oder Werturteil?", 200, 250, beim("tipp", "Tatsache"), "Bold", 36),
    z("2. Schmähkritik nur ausnahmsweise,", 200, 330, "tipp2", "Bold", 36),
    z("mit Begründung", 200, 380, beim("tipp2", "Begründung"), "Bold", 36),
    z("3. sonst Abwägung bei § 193 StGB", 200, 460, "tipp3", "Bold", 36),
    linienzug([(130, 540), (1130, 540)], "tipp4", breite=3),
    *neinz("„Sachbezug vorhanden, also zulässig“", 570, "tipp4", "Bold", 34, x=200),
    zit("1 BvR 2397/19, Rn. 15, 17, 23, 26; 1 BvR 1073/20, Rn. 44–46", 200, 620, "tipp4"),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# M Prüfschema
# ===========================================================================================================================
REIHEN = [("k1", 0, "I. Tatbestand", True),
          ("k1a", 1, "Äußerung und ihr Sinn, Kundgabe der Missachtung, Vorsatz", False),
          ("k1b", 1, "gegen Politiker ggf. § 188 StGB", False),
          ("k2", 0, "II. Rechtswidrigkeit", True),
          ("k2a", 1, "Schmähung, Formalbeleidigung, Menschenwürde? Dann ohne Abwägung", False),
          ("k2b", 1, "sonst Abwägung bei § 193 StGB", False),
          ("k3", 0, "III. Schuld", True),
          ("k4", 0, "IV. Strafantrag", True)]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfschema: Beleidigung, § 185 StGB"), 110, 90, "sch", 46)]
y = 210
for c, ebene, text, fett in REIHEN:
    x = (130, 200)[ebene]
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 40 if ebene == 0 else 36, rechts=1800))
    y += {0: 88, 1: 80}[ebene]
assert y <= 970, y
folie([("sch", "Prüfschema"), ("k1", "Prüfschema › I. Tatbestand"), ("k1b", "Prüfschema › I. ggf. § 188 StGB"),
       ("k2", "Prüfschema › II. Rechtswidrigkeit"), ("k2a", "Prüfschema › II. Ausnahmen ohne Abwägung"),
       ("k2b", "Prüfschema › II. Abwägung, § 193 StGB"), ("k3", "Prüfschema › III. Schuld"),
       ("k4", "Prüfschema › IV. Strafantrag")], els_sch)

# ===========================================================================================================================
# N Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Auch harte Kritik an Politikern", 0)], [("ist geschützt, aber ", 0),
                 ("nicht jede Beschimpfung", "a"), (".", 0)]], 750, 300, 44, "merke",
                {"a": beim("merke", "nicht")}),
    *markertext([[("Die Schmähkritik ist die enge Ausnahme;", 0)],
                 [("der Normalfall ist die ", 0), ("Abwägung", "b")], [("im Einzelfall.", 0)]], 750, 520, 44, "m2",
                {"b": beim("m2", "Abwägung")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
