"""Folge 125 · Verbrauchsgüterkauf §§ 474 ff. BGB: Was beim Händler anders ist – Serienstandard Open Peeps (Katzenkönig).
Beispielfall: Dirk kauft im Laden von Frau Tillmann einen gebrauchten Fernseher für 250 €; im vorgedruckten Formular steht
„Gekauft wie gesehen, keine Gewährleistung“. Nach vier Monaten fällt das Bild aus.
Szenen laut ../SZENENPLAN.md: A1 Kauf im Laden, A2 Wohnzimmer (Bild fällt aus), A3 zurück im Laden (Blasen, Fragen),
B Sachverhalt, C Aufbau (Zweispalter „von privat“ / „vom Händler“), D 1. Anwendungsbereich (Wortlaut § 474 Abs. 1 S. 1),
E 2. Abweichungsverbot (Wortlaut § 476 Abs. 1 S. 1), F1 3. negative Beschaffenheitsvereinbarung (Wortlaut § 476 Abs. 1
S. 2), F2 Subsumtion, G1 4. Beweislastumkehr (Wortlaut § 477 Abs. 1 S. 1), G2 Zeitstrahl/Subsumtion, H 5. Verjährung
(Wortlaut § 476 Abs. 2), I 6. Versand (§ 475 Abs. 2), J Ergebnis, K Klausurtipp (Lexi), L Schema, M Merksatz (Lexi).
Zwei Handlungsgeräusche (Unterschrift, Fernseher geht aus; ../geraeusche_herkunft.json).
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/hand/okz/
neinz als eigene Kopie aus Folge 122 (gemeinsame Dateien unverändert); neu spalte() für den Zweispalter.
Zahlen auf Tafeln, Pillen und Blasen als Ziffern (Wortlautkarten wörtlich)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_125/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_125/" in n:
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
    els.append(z(quelle, tx, ty + len(zeilen) * lh + 4, cue, "Bold", max(26, size - 4), farbe=TEXT, rechts=x + w - 16, bis=bis))
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




BODEN, FH = 860, 480
X1, X2 = 1400, 1720                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
DI_N, TI_N = BLAU, ROT                      # Farben der Namensschilder
PX, PY, PU = 1560, 120, 340                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
HOLZ = (214, 160, 110, 255)
DUNKEL = (70, 70, 78, 255)                  # schwarzer Bildschirm (Bild ausgefallen)
PRIV, HAEN = (214, 228, 250, 255), (253, 236, 186, 255)   # Spaltenfarben „von privat“ (hellblau) / „vom Händler“ (hellgelb)


def boden(cue, hart_=False):
    e = linienzug([(40, BODEN), (1880, BODEN)], cue, breite=7, farbe=INK)
    return hart(e) if hart_ else e


def requisit(folge, bis_ende=None):
    """Wechselndes Requisit über den Figuren: folge = [(cue, (set, icon, breite, fuell), pillentext, pillenfarbe)]."""
    els = []
    for i, (c, ic, txt, pf) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else bis_ende
        if ic:
            s_, n_, br, fu = ic
            els.append(ficon(s_, n_, PX, PU, br, c, fuell=fu, bis=b))
        if txt:
            els.append(pl(txt, PX, PY, c, fill=pf, size=30, anker="m", bis=b))
    return els


def paar(c0, di, ti, bis=None):
    """Tafelszene: Dirk (links) und Frau Tillmann (rechts) neben der Tafel, beide blicken zur Tafel (nach links)."""
    return [*fig("DI", X1, FB, FR, di, bis=bis), ns("Dirk", X1, FB, c0, DI_N, d=0.1),
            *fig("TI", X2, FB, FR, ti, bis=bis, d=0.2), ns("Frau Tillmann", X2, FB, c0, TI_N, d=0.3)]


def spalte(x, y, w, h, fill, kopf, cue, zeilen, size=30):
    """Eine Spalte des Zweispalters: Karte mit Kopf („von privat“ / „vom Händler“) erscheint bei cue, die Zeilen
    folgen je zu ihrem gesprochenen Wort. zeilen = [(text, cue, stil, zeichen)] mit zeichen None/'ok'/'nein'/'zit'."""
    els = [karte(x, y, w, h, cue, fill=fill, rund=18, schatten=6, rand=4),
           z(kopf, x + 22, y + 14, cue, "ExtraBold", 32, rechts=x + w - 12)]
    yy = y + 66
    for text, c, stil, zeichen in zeilen:
        if zeichen == "zit":
            els.append(zit(text, x + 22, yy, c, rechts=x + w - 12)); yy += 38; continue
        xt = x + 22
        if zeichen == "ok":
            els.append(ok(x + 34, yy + 19, c, gr=17)); xt = x + 62
        elif zeichen == "nein":
            els.append(nein(x + 34, yy + 19, c, gr=16)); xt = x + 62
        els.append(z(text, xt, yy, c, stil, size, rechts=x + w - 12)); yy += int(size * 1.38)
    assert yy <= y + h + 4, f"Spalte zu voll: {kopf} ({yy} > {y + h})"
    return els


def zwei(y, h, privat, haendler):
    """Zweispalter unten auf der Tafel: links „von privat“, rechts „vom Händler“ (wie in Szene C eingeführt)."""
    (cp, zp), (ch, zh) = privat, haendler
    noetig = lambda zs: 66 + sum(38 if zz[3] == "zit" else int(30 * 1.38) for zz in zs) + 14
    h = max(h, noetig(zp), noetig(zh))
    assert y + h <= 895, f"Zweispalter ragt aus der Tafel ({y + h})"
    return [*spalte(110, y, 505, h, PRIV, "von privat", cp, zp), *spalte(645, y, 505, h, HAEN, "vom Händler", ch, zh)]


# ===========================================================================================================================
# A1 Fall: Kauf im Laden von Frau Tillmann
# ===========================================================================================================================
TX, DX = 330, 1400                          # Frau Tillmann links (blickt nach rechts), Dirk rechts (blickt nach links)
THEKE_X, THEKE_Y, THEKE_W = 520, 660, 560   # Ladentheke
TVX = 860                                    # Fernseher auf der Theke


def laden(c0, hart_=True):
    an = "cut" if hart_ else "pop"
    els = [boden(c0, hart_), karte(THEKE_X, THEKE_Y, THEKE_W, BODEN - THEKE_Y, c0, fill=HOLZ, rund=10, schatten=6, rand=5,
                                   anim="cut" if hart_ else "fade"),
           karte(1500, 318, 360, 18, c0, fill=HOLZ, rund=6, schatten=4, rand=4, anim="cut" if hart_ else "fade")]
    for cx in (1590, 1770):
        els.append(ficon("tabler", "device-tv-old", cx, 318, 150, c0, fuell=BLAU, anim=an))
    return els


UNTER = beim("unter", "unterschreibt")
MIT = beim("unter", "mit")
folie([(NULL, "Fall · Kauf im Laden"), ("form", "Fall · Das Kaufformular")], [
    *laden(NULL),
    hart(pl("Im Laden von Frau Tillmann", 70, 30, NULL, fill=GELB, size=40)),
    bis_(ficon("tabler", "device-tv", TVX, THEKE_Y, 220, NULL, fuell=BLAU, anim="cut"), MIT),
    pl("gebraucht", 760, 360, beim("fall", "gebrauchten", nr=1), fill=WEISS, size=34),
    pl("250 €", 1000, 420, beim("fall", "zweihundertfünfzig"), fill=GELB, size=34),
    ficon("tabler", "file-text", 630, THEKE_Y, 110, "form", fuell=WEISS),
    pl("„Gekauft wie gesehen, keine Gewährleistung“", 520, 150, beim("form", "Gekauft"), fill=WEISS, size=32),
    pl("vorgedruckt", 330, 240, beim("form", "vorgedruckten"), fill=WEISS, size=30),
    szene(ficon("tabler", "writing-sign", 700, THEKE_Y - 100, 80, UNTER, fuell=WEISS), "125unterschrift*", 0.7),
    ficon("tabler", "device-tv", 1170, BODEN, 190, MIT, fuell=BLAU),
    *fig("TI", TX, BODEN, FH, [(NULL, "froh_r"), ("form", "ruhig_r")], erst="cut"),
    hart(ns("Frau Tillmann", TX, BODEN, NULL, TI_N)),
    *fig("DI", DX, BODEN, FH, [(NULL, "ruhig"), (UNTER, "froh")], erst="cut"),
    hart(ns("Dirk", DX, BODEN, NULL, DI_N)),
])

# ===========================================================================================================================
# A2 Fall: Vier Monate später im Wohnzimmer
# ===========================================================================================================================
BANK_X, BANK_W, BANK_Y = 330, 520, 720
WTVX = BANK_X + BANK_W // 2
AUS = beim("ausfall", "fällt")
folie([("ausfall", "Fall · Vier Monate später")], [
    boden("ausfall"),
    karte(BANK_X, BANK_Y, BANK_W, BODEN - BANK_Y, "ausfall", fill=HOLZ, rund=10, schatten=6, rand=5),
    ficon("tabler", "sofa", 1020, BODEN, 300, "ausfall", fuell=LILA),
    pl("4 Monate später", 70, 30, beim("ausfall", "Vier"), fill=GELB, size=40),
    bis_(ficon("tabler", "device-tv", WTVX, BANK_Y, 300, "ausfall", fuell=BLAU), AUS),
    szene(ficon("tabler", "device-tv-off", WTVX, BANK_Y, 300, AUS, fuell=DUNKEL, anim="cut"), "125tv*", 0.6),
    pl("Bild fällt aus", 400, 300, beim("ausfall", "Bild"), fill=ROT, size=34),
    pl("ganz normal benutzt", 1000, 230, beim("normal", "ganz"), fill=WEISS, size=34),
    *fig("DI", DX, BODEN, FH, [("ausfall", "ruhig"), (AUS, "sorge"), ("normal", "denkt")], erst="pop"),
    ns("Dirk", DX, BODEN, "ausfall", DI_N, d=0.1),
])

# ===========================================================================================================================
# A3 Fall: Zurück im Laden – Dirk und Frau Tillmann
# ===========================================================================================================================
folie([("di1", "Fall · Zurück im Laden"), ("frage", "Fall · Die Frage")], [
    *laden("di1", hart_=False),
    ficon("tabler", "device-tv-off", TVX, THEKE_Y, 220, "di1", fuell=DUNKEL),
    ficon("tabler", "file-text", 630, THEKE_Y, 110, "di1", fuell=WEISS),
    *fig("DI", DX, BODEN, FH, [("di1", "sorge")], erst="pop", bis="di1"),
    ns("Dirk", DX, BODEN, "di1", DI_N, d=0.1),
    *redet("DI_redet", DX, BODEN, FH, "di1", "ti1"),
    *fig("DI", DX, BODEN, FH, [("ti1", "sorge"), ("frage", "denkt")], erst="cut"),
    blase("sprech", 620, 250, "di1", 1000, 230, inhalt=["Das Bild ist weg.", "Bitte reparieren Sie", "den Fernseher."],
          textsize=38, figur=("DI_redet", DX, BODEN, FH), bis="ti1"),
    *fig("TI", TX, BODEN, FH, [("di1", "ruhig_r")], erst="pop", bis="ti1"),
    ns("Frau Tillmann", TX, BODEN, "di1", TI_N, d=0.2),
    *redet("TI_redet_r", TX, BODEN, FH, "ti1", "frage"),
    *fig("TI", TX, BODEN, FH, [("frage", "ernst_r")], erst="cut"),
    blase("sprech", 720, 300, "ti1", 760, 210, inhalt=["Gekauft wie gesehen,", "keine Gewährleistung.", "Und kaputtgegangen ist er",
                                                       "erst bei Ihnen."],
          textsize=36, figur=("TI_redet_r", TX, BODEN, FH), bis="frage"),
    pl("Muss Frau Tillmann trotzdem einstehen?", 470, 150, "frage", fill=PINK, size=36),
    pl("Was wäre anders beim Kauf von privat?", 470, 240, "frage2", fill=PINK, size=36),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_125(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 56)]
    y = 205
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=40, zeilenabstand=1.30)
        els += e; y += 14
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=36))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_125("sv", [
    "Dirk kauft privat für sein Wohnzimmer im Laden von Frau Tillmann, die dort gewerblich gebrauchte Elektrogeräte "
    "verkauft, einen gebrauchten Fernseher für 250 Euro. Im vorgedruckten Kaufformular steht: „Gekauft wie gesehen, keine "
    "Gewährleistung.“ Auf eine bestimmte Schwäche des Geräts weist Frau Tillmann nicht hin. Dirk unterschreibt und nimmt "
    "den Fernseher gleich mit.",
    "Vier Monate später fällt das Bild aus. Dirk hat den Fernseher ganz normal benutzt; woran der Ausfall liegt, ist "
    "unklar. Dirk: „Bitte reparieren Sie den Fernseher.“ Frau Tillmann: „Gekauft wie gesehen, keine Gewährleistung. Und "
    "kaputtgegangen ist er erst bei Ihnen.“",
], "Muss Frau Tillmann einstehen? Was wäre beim Kauf von privat anders?")

# ===========================================================================================================================
# C Aufbau: Sonderregeln und Zweispalter
# ===========================================================================================================================
folie([("plan", "Verbrauchsgüterkauf · §§ 474 ff. BGB"), ("plan3", "Verbrauchsgüterkauf › von privat und vom Händler")],
      rechts_frei([
    *tafel("plan", "Verbrauchsgüterkauf, §§ 474 ff. BGB"),
    z("Regeln über den Verbrauchsgüterkauf", 110, 190, beim("plan", "Regeln"), "Bold", 38),
    *neinz("keine eigene Anspruchsgrundlage", 280, "plan2", "Bold", 36, x=160),
    *okz("ändern die Käuferrechte aus § 437 BGB", 350, beim("plan2", "sondern"), "Bold", 36, x=160),
    z("Punkt für Punkt:", 110, 450, "plan3", "Bold", 36),
    karte(110, 520, 505, 200, "links", fill=PRIV, rund=18, schatten=6, rand=4),
    z("von privat", 140, 580, "links", "ExtraBold", 44),
    dicon("tabler", "user", 520, 690, 90, "links", fuell=WEISS),
    karte(645, 520, 505, 200, "rechts", fill=HAEN, rund=18, schatten=6, rand=4),
    z("vom Händler", 675, 580, "rechts", "ExtraBold", 44),
    dicon("tabler", "building-store", 1060, 690, 90, "rechts", fuell=WEISS),
    *requisit([("plan", ("tabler", "device-tv-off", 110, DUNKEL), "gebrauchter Fernseher", WEISS),
               ("plan2", ("tabler", "scale", 110, WEISS), "Käuferrechte, § 437 BGB", WEISS)]),
    *paar("plan", [("plan", "ruhig"), ("plan3", "denkt")], [("plan", "ernst"), ("rechts", "denkt")]),
]))

# ===========================================================================================================================
# D 1. Anwendungsbereich, § 474 Abs. 1 Satz 1 BGB (Wortlautkarte)
# ===========================================================================================================================
W474 = ["„Verbrauchsgüterkäufe sind Verträge, durch die ein Verbraucher",
        "von einem Unternehmer eine Ware (§ 241a Absatz 1) kauft.“"]
w474, w474_y = wortlaut(110, 175, 1040, W474, "§ 474 Abs. 1 Satz 1 BGB", "a1", marken=[
    (0, "ein Verbraucher", beim("a2", "Verbraucher")),
    (1, "Unternehmer", beim("a2", "Unternehmer")),
    (1, "eine Ware", beim("a2", "Ware"))], size=30)
folie([("a1", "1. Anwendungsbereich, § 474 Abs. 1 BGB"), ("a3", "1. Anwendungsbereich › Subsumtion")], rechts_frei([
    *tafel("a1", "1. Anwendungsbereich"),
    *w474,
    *okz("Dirk kauft privat: Verbraucher, § 13 BGB", w474_y + 30, "a3", "Bold", 34, x=160),
    *okz("Frau Tillmann verkauft gewerblich: Unternehmerin, § 14", w474_y + 90, "a4", "Bold", 32, x=160),
    *okz("Fernseher: bewegliche Sache, also Ware", w474_y + 150, beim("a5", "bewegliche"), "Bold", 34, x=160),
    *zwei(w474_y + 230, 190,
          ("apr", [("Sonderregeln gelten nicht:", "apr", "Bold", None),
                   ("allgemeines Kaufrecht", beim("apr", "allgemeinen"), "Bold", None)]),
          (beim("a5", "Ware"), [("Verbrauchsgüterkauf", beim("a5", "Ware"), "Bold", "ok"),
                                ("§§ 474 ff. BGB gelten", beim("a5", "Ware"), "Bold", None)])),
    *requisit([("a1", ("tabler", "building-store", 110, GELB), "Unternehmer und Verbraucher", WEISS),
               ("a106", ("tabler", "user", 100, WEISS), "Mehr dazu: Video zum Verbraucherbegriff", GELB)]),
    *paar("a1", [("a1", "ruhig"), ("a3", "froh")], [("a1", "ruhig"), ("a4", "ernst")]),
]))

# ===========================================================================================================================
# E 2. Abweichungsverbot, § 476 Abs. 1 Satz 1 BGB (Wortlautkarte)
# ===========================================================================================================================
W476 = ["„Auf eine vor Mitteilung eines Mangels an den Unternehmer getroffene",
        "Vereinbarung, die zum Nachteil des Verbrauchers von den §§ 433 bis 435,",
        "437, 439 bis 441 und 443 sowie von den Vorschriften dieses Untertitels",
        "abweicht, kann der Unternehmer sich nicht berufen.“"]
w476, w476_y = wortlaut(110, 165, 1040, W476, "§ 476 Abs. 1 Satz 1 BGB", "b1", marken=[
    (0, "vor Mitteilung eines Mangels", beim("b2", "Mitteilung")),
    (1, "zum Nachteil des Verbrauchers", beim("b2", "Nachteil")),
    (3, "kann der Unternehmer sich nicht berufen", beim("b3", "nicht"))], size=28)
folie([("b1", "2. Abweichungsverbot, § 476 Abs. 1 Satz 1 BGB"), ("b5", "2. Abweichungsverbot › Schadensersatz, Abs. 3"),
       ("bpr", "2. Abweichungsverbot › von privat, § 444 BGB")], rechts_frei([
    *tafel("b1", "2. Abweichungsverbot"),
    *w476,
    z("Ausnahme Schadensersatz, § 476 Abs. 3 BGB:", 110, w476_y + 22, "b5", "Bold", 32),
    z("im Formular nur in den Grenzen der §§ 307–309 BGB", 110, w476_y + 66, beim("b5", "Formular"), "Bold", 32),
    *zwei(w476_y + 140, 230,
          ("bpr", [("Ausschluss grundsätzlich", "bpr", "Bold", "ok"), ("möglich", "bpr", "Bold", None),
                   ("Grenze: Arglist oder", "b444", "Bold", None), ("Garantie, § 444 BGB", "b444", "Bold", None)]),
          ("b4", [("„keine Gewährleistung“:", "b4", "Bold", None),
                  ("Frau Tillmann kann sich", beim("b4", "Darauf"), "Bold", "nein"),
                  ("nicht darauf berufen", beim("b4", "Darauf"), "Bold", None)])),
    *requisit([("b1", ("tabler", "file-text", 100, WEISS), "„keine Gewährleistung“", WEISS),
               ("b4", ("tabler", "file-x", 100, ROT), "kein Berufen darauf", ROT),
               ("bpr", ("tabler", "user", 100, WEISS), "von privat", BLAU)]),
    *paar("b1", [("b1", "ruhig"), ("b4", "froh"), ("bpr", "denkt")], [("b1", "denkt"), ("b4", "ernst")]),
]))

# ===========================================================================================================================
# F1 3. Negative Beschaffenheitsvereinbarung, § 476 Abs. 1 Satz 2 BGB (Wortlautkarte)
# ===========================================================================================================================
W476S2 = ["„Von den Anforderungen nach § 434 Absatz 3 oder § 475b Absatz 4 kann vor",
          "Mitteilung eines Mangels an den Unternehmer durch Vertrag abgewichen",
          "werden, wenn 1. der Verbraucher vor der Abgabe seiner Vertragserklärung",
          "eigens davon in Kenntnis gesetzt wurde, dass ein bestimmtes Merkmal der",
          "Ware von den objektiven Anforderungen abweicht, und 2. die Abweichung",
          "im Sinne der Nummer 1 im Vertrag ausdrücklich und gesondert vereinbart",
          "wurde.“"]
w2, w2_y = wortlaut(110, 245, 1040, W476S2, "§ 476 Abs. 1 Satz 2 BGB", beim("c2", "Paragraf"), marken=[
    (3, "eigens davon in Kenntnis gesetzt", beim("c2", "eigens")),
    (3, "ein bestimmtes Merkmal", beim("c2", "bestimmtes")),
    (5, "ausdrücklich und gesondert", beim("c3", "ausdrücklich"))], size=28)
folie([("c1", "3. Negative Beschaffenheitsvereinbarung, § 476 Abs. 1 Satz 2 BGB")], rechts_frei([
    *tafel("c1", "3. Schlechter als üblich vereinbaren?"),
    z("Abweichung von den objektiven Anforderungen?", 110, 180, beim("c1", "vereinbaren"), "Bold", 34),
    *w2,
    z("Nicht genügend: neben vielen anderen Klauseln", 110, w2_y + 22, "c4", "Bold", 32),
    z("in einem Formular", 110, w2_y + 66, beim("c4", "Formular"), "Bold", 32),
    zit("Gesetzesbegründung, BT-Drs. 19/27424, S. 42", 110, w2_y + 114, beim("c4", "Gesetzesbegründung")),
    *requisit([("c1", ("tabler", "device-tv-off", 110, DUNKEL), "schlechter als üblich?", WEISS),
               (beim("c2", "eigens"), ("tabler", "info-circle", 100, WEISS), "eigens hinweisen", GELB),
               ("c3", ("tabler", "writing-sign", 100, WEISS), "ausdrücklich und gesondert", GELB),
               ("c4", ("tabler", "file-text", 100, WEISS), "Formular reicht nicht", ROT)]),
    *paar("c1", [("c1", "denkt"), ("c4", "ruhig")], [("c1", "ruhig"), ("c2", "denkt"), ("c4", "ernst")]),
]))

# ===========================================================================================================================
# F2 3. Subsumtion: „Gekauft wie gesehen“
# ===========================================================================================================================
folie([("c5", "3. Negative Beschaffenheitsvereinbarung › im Fall"),
       ("c6", "3. › objektive Anforderungen, § 434 Abs. 3 BGB")], rechts_frei([
    *tafel("c5", "3. „Gekauft wie gesehen“ im Fall"),
    *zwei(185, 230,
          ("cpr", [("Abweichung auch ohne", "cpr", "Bold", "ok"), ("diese Form möglich", "cpr", "Bold", None),
                   ("§ 434 Abs. 3 BGB: „soweit nicht", beim("cpr", "Form"), "Bold", "zit"),
                   ("wirksam etwas anderes vereinbart“", beim("cpr", "Form"), "Bold", "zit")]),
          ("c5", [("kein bestimmtes Merkmal", beim("c5", "bestimmtes"), "Bold", "nein"),
                  ("vorgedruckt im Formular", beim("c5", "vorgedruckt"), "Bold", "nein"),
                  ("keine wirksame Abweichung", beim("c5", "Formular"), "ExtraBold", None)])),
    z("Also gilt: gewöhnliche Verwendung, auch gebraucht", 110, 470, "c6", "Bold", 34),
    zit("§ 434 Abs. 3 Satz 1 Nr. 1 BGB", 110, 520, beim("c6", "Verwendung")),
    *neinz("Fernseher ohne Bild: eignet sich nicht", 580, "c7", "Bold", 36, x=160),
    blk(110, 680, 1040, 100, GELB, "c059", [("Mehr dazu: Video zum Sachmangel", "Bold", 36, INK)]),
    *requisit([("c5", ("tabler", "file-x", 100, ROT), "„Gekauft wie gesehen“", WEISS),
               ("c7", ("tabler", "device-tv-off", 110, DUNKEL), "kein Bild: Sachmangel", ROT),
               ("cpr", ("tabler", "user", 100, WEISS), "von privat", BLAU)]),
    *paar("c5", [("c5", "ruhig"), ("c7", "sorge"), ("cpr", "denkt")], [("c5", "ernst"), ("cpr", "ruhig")]),
]))

# ===========================================================================================================================
# G1 4. Beweislastumkehr, § 477 Abs. 1 Satz 1 BGB (Wortlautkarte)
# ===========================================================================================================================
W477 = ["„Zeigt sich innerhalb eines Jahres seit Gefahrübergang ein von den",
        "Anforderungen nach § 434 oder § 475b abweichender Zustand der Ware, so",
        "wird vermutet, dass die Ware bereits bei Gefahrübergang mangelhaft war,",
        "es sei denn, diese Vermutung ist mit der Art der Ware oder des mangelhaften",
        "Zustands unvereinbar.“"]
w477, w477_y = wortlaut(110, 165, 1040, W477, "§ 477 Abs. 1 Satz 1 BGB", "d1", marken=[
    (0, "innerhalb eines Jahres", beim("d2", "innerhalb")),
    (1, "abweichender Zustand", beim("d2", "abweichender")),
    (2, "bereits bei Gefahrübergang mangelhaft", beim("d2", "schon")),
    (3, "es sei denn", beim("d3", "es"))], size=28)
folie([("d1", "4. Beweislastumkehr, § 477 Abs. 1 BGB"), ("d4", "4. Beweislastumkehr › Mangelerscheinung genügt"),
       ("d5", "4. Beweislastumkehr › Beweis des Gegenteils")], rechts_frei([
    *tafel("d1", "4. Beweislastumkehr"),
    *w477,
    *neinz("Käufer muss die Ursache nicht beweisen", w477_y + 26, beim("d4", "nicht"), "Bold", 34, x=160),
    *okz("mangelhafter Zustand zeigt sich in der Frist", w477_y + 86, beim("d4", "genügt"), "Bold", 34, x=160),
    zit("BGH, Urt. v. 6.5.2026 – VIII ZR 257/23, Rn. 25, 27 (zu § 477 a. F.)", 160, w477_y + 140, beim("d4", "genügt")),
    blk(110, w477_y + 200, 1040, 120, GELB, "d5", [("Frau Tillmann: Beweis des Gegenteils,", "Bold", 34, INK),
                                                   ("z. B. ein Bedienungsfehler", "Bold", 34, INK)]),
    zit("BGH, Urt. v. 12.10.2016 – VIII ZR 103/15, Rn. 59", 110, w477_y + 336, beim("d5", "Bedienungsfehler")),
    *requisit([("d1", ("tabler", "scale", 110, WEISS), "Wer muss beweisen?", WEISS),
               ("d2", ("tabler", "hourglass", 100, GELB), "1 Jahr", GELB),
               ("d4", ("tabler", "device-tv-off", 110, DUNKEL), "Mangelerscheinung", WEISS),
               ("d5", ("tabler", "zoom-question", 100, WEISS), "Gegenteil beweisen", ROT)]),
    *paar("d1", [("d1", "sorge"), ("d4", "froh")], [("d1", "denkt"), ("d5", "ernst")]),
]))

# ===========================================================================================================================
# G2 4. Beweislastumkehr im Fall (Zeitstrahl)
# ===========================================================================================================================
T0, T1, TY = 170, 1060, 330                 # Zeitstrahl Übergabe bis 1 Jahr (12 Monate)
mon = lambda m: T0 + m / 12 * (T1 - T0)
D6 = "d6"
strahl = [linienzug([(T0 - 20, TY), (T1 + 20, TY)], D6, breite=5)]
for m_ in range(13):
    gross = m_ in (0, 4, 12)
    strahl.append(linienzug([(mon(m_), TY - (12 if gross else 7)), (mon(m_), TY + (12 if gross else 7))], D6,
                            breite=5 if gross else 3))
folie([("d6", "4. Beweislastumkehr › im Fall"), ("dpr", "4. Beweislastumkehr › von privat, § 363 BGB")], rechts_frei([
    *tafel("d6", "4. Beweislast im Fall"),
    *strahl,
    blk(int(mon(0)), TY - 66, int(mon(12) - mon(0)), 48, GELB, beim("d6", "innerhalb"), [("Vermutung: 1 Jahr", "ExtraBold", 28, INK)],
        anim="pop"),
    pl("Übergabe", mon(0) - 60, TY + 30, D6, fill=WEISS, size=28),
    pl("4 Monate: Bild fällt aus", mon(4) - 40, TY + 30, beim("d6", "vier"), fill=ROT, size=28),
    pl("1 Jahr", mon(12) - 70, TY + 30, beim("d6", "Jahres"), fill=GELB, size=28),
    *okz("auch bei gebrauchter Ware", 490, "d7", "Bold", 36, x=160),
    zit("BGH, Urt. v. 6.5.2026 – VIII ZR 257/23, Rn. 1, 24–26 (Motorroller)", 160, 545,
        beim("d7", "Motorroller")),
    dicon("tabler", "moped", 1050, 560, 110, beim("d7", "Motorroller"), fuell=WEISS),
    *zwei(610, 230,
          ("dpr", [("Dirk muss beweisen:", "dpr", "Bold", None), ("Mangel schon bei der", beim("dpr", "Mangel"), "Bold", None),
                   ("Übergabe", beim("dpr", "Mangel"), "Bold", None), ("§ 363 BGB", beim("dpr", "Übergabe"), "Bold", "zit")]),
          (beim("d6", "innerhalb"), [("Vermutung greift", beim("d6", "innerhalb"), "Bold", "ok"),
                                     ("Mangel schon bei der", beim("d6", "innerhalb"), "Bold", None),
                                     ("Übergabe vermutet", beim("d6", "innerhalb"), "Bold", None)])),
    *requisit([("d6", ("tabler", "calendar-time", 100, WEISS), "nach 4 Monaten", ROT),
               ("d7", ("tabler", "moped", 110, WEISS), "auch gebraucht", GRUEN),
               ("dpr", ("tabler", "user", 100, WEISS), "von privat", BLAU)]),
    *paar("d6", [("d6", "ruhig"), (beim("d6", "innerhalb"), "froh"), ("dpr", "sorge")], [("d6", "ernst"), ("d7", "denkt")]),
]))

# ===========================================================================================================================
# H 5. Verjährung, § 476 Abs. 2 BGB (Wortlautkarte)
# ===========================================================================================================================
W476A2 = ["„Die Verjährung der in § 437 bezeichneten Ansprüche kann vor Mitteilung",
          "eines Mangels an den Unternehmer nicht durch Rechtsgeschäft erleichtert",
          "werden, wenn die Vereinbarung zu einer Verjährungsfrist ab dem gesetzlichen",
          "Verjährungsbeginn von weniger als zwei Jahren, bei gebrauchten Waren von",
          "weniger als einem Jahr führt. Die Vereinbarung ist nur wirksam, wenn 1. der",
          "Verbraucher vor der Abgabe seiner Vertragserklärung von der Verkürzung der",
          "Verjährungsfrist eigens in Kenntnis gesetzt wurde und 2. die Verkürzung der",
          "Verjährungsfrist im Vertrag ausdrücklich und gesondert vereinbart wurde.“"]
wv, wv_y = wortlaut(110, 245, 1040, W476A2, "§ 476 Abs. 2 BGB", "e2", marken=[
    (3, "bei gebrauchten Waren von", beim("e2", "gebrauchten")),
    (4, "weniger als einem Jahr", beim("e2", "gebrauchten")),
    (6, "eigens in Kenntnis gesetzt", beim("e3", "eigenem")),
    (7, "ausdrücklich und gesondert", beim("e3", "ausdrücklicher"))], size=28)
folie([("e1", "5. Verjährung, § 438 BGB"), ("e2", "5. Verjährung › Verkürzung, § 476 Abs. 2 BGB")], rechts_frei([
    *tafel("e1", "5. Verjährung"),
    z("Regel: 2 Jahre ab Ablieferung", 110, 180, beim("e1", "zwei"), "Bold", 36),
    zit("§ 438 Abs. 1 Nr. 3, Abs. 2 BGB", 680, 192, beim("e1", "Paragraf")),
    *wv,
    *zwei(wv_y + 20, 180,
          ("epr", [("Verkürzung grundsätzlich", "epr", "Bold", "ok"), ("auch stärker möglich", beim("epr", "stärker"), "Bold", None),
                   ("Grenze: § 202 BGB", beim("epr", "verkürzen"), "Bold", "zit")]),
          ("e4", [("Formular genügt nicht", "e4", "Bold", "nein"), ("es bleibt bei 2 Jahren", beim("e4", "Es"), "Bold", "ok")])),
    *requisit([("e1", ("tabler", "calendar-time", 100, WEISS), "2 Jahre", GELB),
               ("e2", ("tabler", "hourglass", 100, WEISS), "gebraucht: mind. 1 Jahr", GELB),
               ("e4", ("tabler", "file-x", 100, ROT), "Formular genügt nicht", ROT),
               ("epr", ("tabler", "user", 100, WEISS), "von privat", BLAU)]),
    *paar("e1", [("e1", "ruhig"), ("e4", "froh")], [("e1", "denkt"), ("e3", "ernst")]),
]))

# ===========================================================================================================================
# I 6. Versand, § 475 Abs. 2 BGB (Abgrenzung)
# ===========================================================================================================================
VY = 470
folie([("f1", "6. Abgrenzung: Versand, § 475 Abs. 2 BGB"), ("fpr", "6. Versand › von privat, § 447 BGB")], rechts_frei([
    *tafel("f1", "6. Abgrenzung: Versand"),
    z("Wann geht die Gefahr über?", 110, 180, "f1", "Bold", 36),
    dicon("tabler", "building-store", 230, VY, 140, beim("f1", "Verschickt"), fuell=GELB),
    pfeil(320, VY - 60, 500, VY - 60, beim("f1", "Verschickt"), breite=7, kopf=22, farbe=INK),
    dicon("tabler", "truck-delivery", 620, VY, 160, beim("f1", "Verschickt"), fuell=WEISS),
    pfeil(720, VY - 60, 900, VY - 60, beim("f1", "Verschickt"), breite=7, kopf=22, farbe=INK),
    dicon("tabler", "home", 1010, VY, 140, beim("f1", "Verschickt"), fuell=WEISS),
    pl("Händler: Gefahrübergang hier", 800, VY + 20, beim("f1", "Übergabe"), fill=HAEN, size=28),
    pl("privat: schon hier", 470, VY + 90, beim("fpr", "Übergabe"), fill=PRIV, size=28),
    *zwei(VY + 180, 210,
          ("fpr", [("Versendungskauf:", "fpr", "Bold", None), ("schon mit Übergabe an das", beim("fpr", "Übergabe"), "Bold", None),
                   ("Transportunternehmen", beim("fpr", "Transportunternehmen"), "Bold", None),
                   ("§ 447 Abs. 1 BGB", beim("fpr", "Paragraf"), "Bold", "zit")]),
          (beim("f1", "Verschickt"), [("in der Regel erst mit", beim("f1", "Regel"), "Bold", None), ("Übergabe an den", beim("f1", "Übergabe"), "Bold", None),
                  ("Verbraucher", beim("f1", "Verbraucher"), "Bold", None),
                  ("§ 475 Abs. 2 BGB", beim("f1", "Paragraf"), "Bold", "zit")])),
    *requisit([("f1", ("tabler", "truck-delivery", 120, WEISS), "nur zur Abgrenzung", WEISS),
               ("fpr", ("tabler", "user", 100, WEISS), "von privat", BLAU)]),
    *paar("f1", [("f1", "denkt"), ("fpr", "ruhig")], [("f1", "ruhig"), ("fpr", "denkt")]),
]))

# ===========================================================================================================================
# J Ergebnis
# ===========================================================================================================================
folie([("erg", "Ergebnis")], rechts_frei([
    *tafel("erg", "Ergebnis"),
    *okz("Verbrauchsgüterkauf, § 474 Abs. 1 BGB", 190, "erg", "Bold", 36, x=160),
    *neinz("kein Berufen auf den Ausschluss, § 476 Abs. 1 S. 1", 270, "erg2", "Bold", 34, x=160),
    *neinz("keine wirksame Abweichung, § 476 Abs. 1 S. 2", 350, "erg3", "Bold", 34, x=160),
    *okz("Mangel bei Übergabe vermutet, § 477 Abs. 1", 430, "erg4", "Bold", 34, x=160),
    blk(110, 530, 1040, 150, GRUEN, "erg5", [("Dirk: Rechte aus § 437 BGB", "ExtraBold", 38, INK),
                                            ("zuerst Nacherfüllung – hier die Reparatur", "Bold", 34, INK)]),
    blk(110, 720, 1040, 100, GELB, "v063", [("Wie es weitergeht: Video zu den Käuferrechten", "Bold", 34, INK)]),
    *requisit([("erg", ("tabler", "building-store", 110, GELB), "Verbrauchsgüterkauf", GELB),
               ("erg5", ("tabler", "tools", 100, WEISS), "Reparatur", GRUEN)]),
    *paar("erg", [("erg", "ruhig"), ("erg2", "froh")], [("erg", "ernst"), ("erg5", "ruhig")]),
]))

# ===========================================================================================================================
# K Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Sonderregeln im § 437 einbauen")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Früh feststellen: Verbrauchsgüterkauf", 200, 200, beim("tipp", "Stelle"), "Bold", 38),
    z("Sonderregeln dort einbauen, wo sie wirken:", 200, 300, "tipp2", "Bold", 36),
    *okz("beim Mangel: §§ 476 Abs. 1 S. 2, 477 BGB", 380, beim("tipp3", "Mangel"), "Bold", 34, x=230),
    *okz("beim Ausschluss: § 476 Abs. 1 S. 1 BGB", 450, beim("tipp3", "Ausschluss"), "Bold", 34, x=230),
    *okz("bei der Verjährung: § 476 Abs. 2 BGB", 520, beim("tipp3", "Verjährung"), "Bold", 34, x=230),
    dicon("tabler", "puzzle", 980, 800, 150, "tipp2", fuell=GELB),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# L Klausurschema (progressiv)
# ===========================================================================================================================
REIHEN = [("k1", "I.", "Kaufvertrag", BLAU, 0),
          ("k11", "", "hier: Verbrauchsgüterkauf, § 474 Abs. 1 BGB", None, 1),
          ("k2", "II.", "Sachmangel bei Gefahrübergang", GELB, 0),
          ("k21", "1.", "Abweichung nur nach § 476 Abs. 1 Satz 2 BGB", None, 1),
          ("k22", "2.", "Vermutung nach § 477 Abs. 1 BGB", None, 1),
          ("k3", "III.", "kein wirksamer Ausschluss, § 476 Abs. 1 Satz 1 BGB", GRUEN, 0),
          ("k4", "IV.", "keine Verjährung, § 438 mit § 476 Abs. 2 BGB", LILA, 0)]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Schema: Nacherfüllung, §§ 437 Nr. 1, 439 BGB, beim Verbrauchsgüterkauf"), 110, 90, "sch", 46)]
y = 200
for c, r, txt, farbe, ebene in REIHEN:
    if ebene == 0:
        els_sch += [karte(110, y, 110, 70, c, fill=farbe, rund=14, schatten=5, rand=4),
                    z(r, 165 - F("ExtraBold", 38).getlength(r) / 2, y + 10, c, "ExtraBold", 38, rechts=1820),
                    z(txt, 255, y + 10, c, "ExtraBold", 38, rechts=1820)]
        y += 100
    else:
        if r:
            els_sch.append(z(r, 270, y + 2, c, "Bold", 36, rechts=1820))
        els_sch.append(z(txt, 330, y + 2, c, "Bold", 36, rechts=1820))
        els_sch.append(ok(230, y + 24, c, gr=18))
        y += 76
assert y <= 975, y
folie([("sch", "Schema: Nacherfüllung beim Verbrauchsgüterkauf"), ("k1", "Schema › I. Kaufvertrag"),
       ("k2", "Schema › II. Sachmangel bei Gefahrübergang"), ("k3", "Schema › III. kein Ausschluss"),
       ("k4", "Schema › IV. keine Verjährung")], els_sch)

# ===========================================================================================================================
# M Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Beim Händler hilft ", 0)], [("„gekauft wie gesehen“", "a"), (" nicht.", 0)]], 750, 290, 46, "merke",
                {"a": beim("merke", "gekauft")}),
    *markertext([[("Abweichen geht nur ", 0), ("eigens und gesondert,", "b")]], 750, 500, 42, "mk2",
                {"b": beim("mk2", "eigens")}),
    *markertext([[("und im ersten Jahr wird ", 0), ("vermutet,", "c")], [("dass der Mangel schon bei der Übergabe da war.", 0)]],
                750, 640, 40, "mk3", {"c": beim("mk3", "vermutet")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
