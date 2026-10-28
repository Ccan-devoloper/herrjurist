"""Folge 177 · Schadensersatz neben der Leistung oder statt? Die eine Kontrollfrage – Serienstandard Open Peeps (Katzenkönig).
Fall: Elfriede (Druckerei) kauft bei Dietrich, der Steuerchips selbst herstellt, einen Chip zum Nachrüsten ihrer
Druckmaschine für 300 €. Der Chip ist fehlerhaft, überhitzt und zerstört die bis dahin einwandfreie Steuerungseinheit;
drei Tage Stillstand. Posten: 1. Chip 300 €, 2. Steuerungseinheit 6.000 €, 3. entgangener Gewinn 4.500 €; keine Frist.
Szenen laut ../SZENENPLAN.md: A1 Kauf, A2 Schaden/Streit, A3 Drei Posten/Frage, B Sachverhalt, C § 280 Abs. 1 (Wortlaut),
D Grundtatbestand im Fall, E §§ 280 Abs. 3, 281 Abs. 1 Satz 1 (Wortlaut), F Kontrollfrage, G/H/I Posten 1–3 (gleiche
Tafelstruktur: Posten – Kontrollfrage – Anspruchsgrundlage), J Lösung (Tabelle), K Klausurtipp (Lexi), L Klausurschema,
M Merksatz (Lexi).
Druckmaschine programmatisch (Palettenflächen, Tuschekontur), Chip als Tabler-Icon „cpu“; keine Marken.
Handlungsgeräusch: Funken, als die Steuerungseinheit zerstört wird (../geraeusche_herkunft.json).
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/hand/okz/
neinz als eigene Kopie aus Folge 170 (gemeinsame Dateien unverändert); neu: maschine(), panel(), posten_tafel().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_177/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_177/" in n:
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
EL_N, DI_N = LILA, GELB                     # Farben der Namensschilder
PX, PY, PU = 1570, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"EL": "Elfriede", "DI": "Dietrich"}
NFARBE = {"EL": EL_N, "DI": DI_N}
GRAU_A = (150, 150, 150, 255)
WX, AX = 1250, 1690                         # Fallszenen: Elfriede (blickt nach rechts), Dietrich (blickt nach links)
SLOT = (820, 765)                           # Chip-Steckplatz an der Steuerungseinheit (Mitte x, Unterkante)


def boden(cue, hart_=False):
    e = linienzug([(40, BODEN), (1880, BODEN)], cue, breite=7, farbe=INK)
    return hart(e) if hart_ else e


def _bild(w, h):
    s = 2
    return Image.new("RGBA", (w * s, h * s)), s


def maschine(cue):
    """Druckmaschine in Seitenansicht (programmatisch: Gehäuse, Walzen, Papierablage; Palettenflächen, Tuschekontur).
    Die Steuerungseinheit ist ein eigenes Element (panel), damit ihr Zustand wechseln kann."""
    W_, H_ = 900, 420
    im, s = _bild(W_, H_)
    dr = ImageDraw.Draw(im)
    S = lambda *v: [int(a * s) for a in v]
    # Papierablage links mit Bogenstapel
    dr.rounded_rectangle(S(10, 300, 150, 410), 10 * s, fill=WEISS, outline=INK, width=5 * s)
    for k in range(4):
        dr.rectangle(S(25, 285 - 10 * k, 135, 295 - 10 * k), fill=WEISS, outline=INK, width=3 * s)
    # Gehäuse
    dr.rounded_rectangle(S(150, 140, 860, 410), 22 * s, fill=BLAU, outline=INK, width=6 * s)
    # Walzenhaube mit zwei Walzen
    dr.rounded_rectangle(S(230, 40, 640, 150), 30 * s, fill=WEISS, outline=INK, width=6 * s)
    for cx in (330, 540):
        dr.ellipse(S(cx - 42, 53, cx + 42, 137), fill=GELB, outline=INK, width=5 * s)
        dr.ellipse(S(cx - 10, 85, cx + 10, 105), fill=INK)
    # Papierbahn
    dr.line(S(150, 300, 240, 260, 600, 260), fill=INK, width=4 * s)
    # Füße
    for x in (200, 780):
        dr.rectangle(S(x, 405, x + 50, 418), fill=INK)
    im = im.resize((W_, H_), Image.LANCZOS)
    return El(im, 70, BODEN - H_ + 2, cue, "cut", 0.0, None, name="maschine")


def panel(cue, zustand="ok", bis=None):
    """Steuerungseinheit am rechten Gehäuseteil: Bildschirm grün (läuft) oder zerstört (grau, Risse)."""
    W_, H_ = 150, 240
    im, s = _bild(W_, H_)
    dr = ImageDraw.Draw(im)
    S = lambda *v: [int(a * s) for a in v]
    kaputt = zustand == "kaputt"
    dr.rounded_rectangle(S(4, 4, 146, 236), 14 * s, fill=(225, 225, 225, 255) if kaputt else WEISS, outline=INK, width=5 * s)
    dr.rounded_rectangle(S(20, 20, 130, 95), 8 * s, fill=GRAU_A if kaputt else GRUEN, outline=INK, width=4 * s)
    if kaputt:
        dr.line(S(30, 28, 62, 60, 52, 72, 92, 90), fill=INK, width=4 * s, joint="curve")
        dr.line(S(118, 26, 88, 52, 104, 66), fill=INK, width=4 * s, joint="curve")
    else:
        dr.line(S(35, 70, 60, 50, 80, 62, 112, 38), fill=INK, width=4 * s, joint="curve")
    for k, f in enumerate((ROT, GELB)):
        dr.ellipse(S(30 + 40 * k, 108, 52 + 40 * k, 130), fill=GRAU_A if kaputt else f, outline=INK, width=3 * s)
    dr.rectangle(S(38, 150, 112, 222), fill=(236, 226, 208, 255), outline=INK, width=4 * s)   # Steckplatz
    im = im.resize((W_, H_), Image.LANCZOS)
    return El(im, SLOT[0] - 75, BODEN - 300, cue, "cut", 0.0, bis, name="panel:" + zustand)


def chip(cx, unten, br, cue, fuell=GRUEN, bis=None, anim="pop"):
    return ficon("tabler", "cpu", cx, unten, br, cue, fuell=fuell, bis=bis, anim=anim)


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


def paar(c0, ef, df):
    """Tafelszene: Elfriede und Dietrich rechts der Tafel, beide blicken zur Tafel (nach links)."""
    return [*fig("EL", X1, FB, FR, ef), ns(NAME["EL"], X1, FB, c0, EL_N, d=0.1),
            *fig("DI", X2, FB, FR, df, d=0.2), ns(NAME["DI"], X2, FB, c0, DI_N, d=0.3)]


# ===========================================================================================================================
# A1 Fall: der Kauf
# ===========================================================================================================================
DIETRICH = beim("kauf", "Dietrich")
CHIP = beim("kauf", "Chip")
folie([(NULL, "Fall · Der Kauf")], [
    hart(boden(NULL)), hart(maschine(NULL)), hart(panel(NULL)),
    pl("Druckerei", 70, 30, beim("fall", "Druckerei"), fill=WEISS, size=40),
    pl("stellt Steuerchips selbst her", 70, 120, beim("kauf", "selbst"), fill=GELB, size=36),
    pl("Chip zum Nachrüsten: 300 €", 70, 205, beim("kauf", "dreihundert"), fill=GRUEN, size=36),
    pl("Techniker setzt ihn ein", 70, 290, "einbau", fill=WEISS, size=36),
    chip(*SLOT, 56, "einbau", anim="cut"),
    ficon("tabler", "tool", 935, 760, 70, "einbau", fuell=GRAU_A),
    *fig("EL", WX, BODEN, FH, [(NULL, "ruhig_r"), (CHIP, "staunt_r"), ("einbau", "froh_r")], erst="cut"),
    hart(ns("Elfriede", WX, BODEN, NULL, EL_N)),
    *fig("DI", AX, BODEN, FH, [(DIETRICH, "ruhig"), ("einbau", "froh")]),
    ns("Dietrich", AX, BODEN, DIETRICH, DI_N, d=0.1),
])
_hx, _hy = hand("DI_ruhig", AX, BODEN, FH, -1)
FOLIEN[-1]["els"].append(chip(_hx - 20, _hy + 5, 60, CHIP, bis="einbau"))

# ===========================================================================================================================
# A2 Fall: der Schaden und der Streit
# ===========================================================================================================================
HEISS = beim("heiss", "überhitzt")
ZERST = beim("zerst", "zerstört")
MELDET = beim("melden", "meldet")
folie([("heiss", "Fall · Der Schaden"), ("el1", "Fall · Der Streit")], [
    boden("heiss"), maschine("heiss"),
    panel("heiss", bis=ZERST), szene(panel(ZERST, "kaputt"), "177funken*", 0.8, 0.0),
    chip(*SLOT, 56, "heiss", bis=HEISS, anim="cut"), chip(*SLOT, 56, HEISS, fuell=ROT, anim="cut"),
    ficon("tabler", "temperature", 935, 565, 85, HEISS, fuell=ROT, bis="still"),
    ficon("tabler", "cloud-fog", 820, 555, 90, ZERST, fuell=WEISS),
    pl("Chip fehlerhaft: überhitzt", 70, 30, HEISS, fill=ROT, size=36),
    pl("Steuerungseinheit zerstört", 70, 120, ZERST, fill=ROT, size=36),
    pl("3 Tage Stillstand", 70, 205, "still", fill=GELB, size=36),
    ficon("tabler", "clock-pause", 1040, 420, 90, "still", fuell=GELB),
    pl("Fehler am selben Tag gemeldet", 70, 290, MELDET, fill=BLAU, size=36),
    *fig("EL", WX, BODEN, FH, [("heiss", "ruhig_r"), (HEISS, "staunt_r"), (ZERST, "sorge_r"), (MELDET, "bestimmt_r")], bis="el1"),
    *redet("EL_bestimmt_r", WX, BODEN, FH, "el1", "di1"),
    *fig("EL", WX, BODEN, FH, [("di1", "denkt_r")], erst="cut"),
    ns("Elfriede", WX, BODEN, "heiss", EL_N, d=0.1),
    blase("sprech", 640, 250, "el1", 1190, 200, inhalt=["Meine Maschine stand", "3 Tage still! Sie zahlen",
                                                        "mir alles, und zwar sofort."], textsize=34, figur=("EL_bestimmt_r", WX, BODEN, FH), bis="di1"),
    *fig("DI", AX, BODEN, FH, [("heiss", "ruhig"), (ZERST, "ernst"), (MELDET, "sorge")], bis="di1"),
    *redet("DI_redet", AX, BODEN, FH, "di1", "pos"),
    ns("Dietrich", AX, BODEN, "heiss", DI_N, d=0.1),
    blase("sprech", 600, 240, "di1", 1560, 200, inhalt=["Ich schicke Ihnen gern", "einen neuen Chip. Aber",
                                                        "zahlen werde ich nichts."], textsize=34, figur=("DI_redet", AX, BODEN, FH), bis="pos"),
])

# ===========================================================================================================================
# A3 Fall: drei Posten, Frage
# ===========================================================================================================================
POSTEN = [("pa", "1", "Chip", "300 €", GELB), ("pb", "2", "neue Steuerungseinheit", "6.000 €", GRUEN),
          ("pc", "3", "entgangener Gewinn", "4.500 €", BLAU)]
folie([("pos", "Fall · Drei Posten"), ("frage", "Fall · Die Frage")], rechts_frei([
    *tafel("pos", "Elfriede verlangt drei Posten"),
    *[e for k, (c, n, t, b, fa) in enumerate(POSTEN) for e in (
        karte(130, 190 + k * 120, 90, 90, c, fill=fa, rund=14, schatten=5, rand=4),
        z(n, 175 - F("ExtraBold", 40).getlength(n) / 2, 207 + k * 120, c, "ExtraBold", 40),
        z(t, 260, 207 + k * 120, c, "Bold", 40),
        z(b, 1130 - F("Bold", 40).getlength(b), 207 + k * 120, c, "Bold", 40))],
    *neinz("keine Frist gesetzt", 570, "frist0", "Bold", 38, x=185),
    pl("Welcher Posten – welcher Anspruch?", 110, 670, "frage", fill=PINK, size=36),
    pl("Wofür braucht sie eine Frist?", 110, 770, "frage2", fill=WEISS, size=36),
    *requisit([("pos", ("tabler", "list-numbers", 100, WEISS), "3 Posten", WEISS),
               ("pa", ("tabler", "cpu", 100, ROT), "Chip", GELB),
               ("pb", ("tabler", "settings-automation", 100, GRAU_A), "Steuerungseinheit", GRUEN),
               ("pc", ("tabler", "clock-pause", 100, GELB), "Stillstand", BLAU),
               ("frist0", ("tabler", "hourglass", 90, WEISS), "keine Frist", ROT),
               ("frage", ("tabler", "zoom-question", 100, WEISS), "welcher Anspruch?", PINK)]),
    *paar("pos", [("pos", "bestimmt"), ("frist0", "denkt")], [("pos", "ruhig"), ("pa", "denkt"), ("frage", "ernst")]),
]))


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_177(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 205
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=34, zeilenabstand=1.30)
        els += e; y += 16
    assert y + 66 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_177("sv", [
    "Elfriede führt eine Druckerei. Bei Dietrich, der Steuerchips selbst herstellt, kauft sie für ihre Druckmaschine einen "
    "Chip zum Nachrüsten, für 300 Euro. Beide sind Kaufleute, der Kauf gehört zu ihrem Geschäft. Ihr Techniker setzt den "
    "Chip ein.",
    "Der Chip ist fehlerhaft: Durch Unsorgfalt in der Fertigung von Dietrich überhitzt er und zerstört die bis dahin "
    "einwandfreie Steuerungseinheit der Maschine. Elfriede meldet den Fehler noch am selben Tag. Drei Tage steht die "
    "Maschine still, bis eine neue Steuerungseinheit eingebaut ist; danach läuft sie vorerst ohne den neuen Chip.",
    "Elfriede verlangt sofort 300 Euro für den Chip (Posten 1), 6.000 Euro für die neue Steuerungseinheit (Posten 2) und "
    "4.500 Euro entgangenen Gewinn (Posten 3). Eine Frist hat sie nicht gesetzt. Dietrich bietet einen neuen Chip an, will aber nichts zahlen.",
], "Welcher Posten über welchen Anspruch – und wofür braucht sie eine Frist?")

# ===========================================================================================================================
# C Grundtatbestand: § 437 Nr. 3, § 280 Abs. 1 (Wortlaut)
# ===========================================================================================================================
W280 = ["„(1) Verletzt der Schuldner eine Pflicht aus dem Schuldverhältnis,",
        "so kann der Gläubiger Ersatz des hierdurch entstehenden",
        "Schadens verlangen. Dies gilt nicht, wenn der Schuldner",
        "die Pflichtverletzung nicht zu vertreten hat.“"]
w280, w280_y = wortlaut(80, 250, 1100, W280, "§ 280 Abs. 1 BGB", beim("w280", "Paragraf"), marken=[
    (0, "Pflicht aus dem Schuldverhältnis", beim("w280", "Pflicht")),
    (1, "Ersatz des hierdurch entstehenden", beim("w280", "Ersatz")),
    (3, "nicht zu vertreten", beim("w280b", "vertreten"))], size=33)
folie([("agl", "Grundtatbestand › § 437 Nr. 3 BGB"), ("w280", "Grundtatbestand › § 280 Abs. 1 BGB")], rechts_frei([
    *tafel("agl", "Grundtatbestand: § 280 Abs. 1 BGB"),
    z("Beim Kauf: § 437 Nr. 3 BGB führt ins allgemeine Schuldrecht", 110, 180, beim("agl", "Paragraf"), "Bold", 32),
    *w280,
    blk(110, w280_y + 40, 1040, 80, LILA, "g046", [("Mehr dazu: Video „Das System der §§ 280 ff.“", "ExtraBold", 34, INK)]),
    *requisit([("agl", ("tabler", "file-text", 100, WEISS), "§ 437 Nr. 3", WEISS),
               ("w280", ("tabler", "scale", 100, WEISS), "§ 280 Abs. 1", WEISS),
               ("g046", ("tabler", "list-numbers", 100, WEISS), "das System", LILA)]),
    *paar("agl", [("agl", "ruhig"), ("w280b", "denkt")], [("agl", "ruhig"), ("w280b", "sorge")]),
]))

# ===========================================================================================================================
# D Grundtatbestand im Fall
# ===========================================================================================================================
folie([("gt1", "Grundtatbestand › Schuldverhältnis"), ("gt2", "Grundtatbestand › Pflichtverletzung"),
       ("gt3", "Grundtatbestand › Rüge, § 377 HGB"), ("gt4", "Grundtatbestand › Vertretenmüssen")], rechts_frei([
    *tafel("gt1", "Grundtatbestand im Fall"),
    *okz("Schuldverhältnis: Kaufvertrag", 175, beim("gt1", "Kaufvertrag"), "Bold", 34, x=160),
    *okz("Sachmangel: Chip überhitzt, nicht für die", 250, beim("gt2", "eignet"), "Bold", 34, x=160),
    z("gewöhnliche Verwendung geeignet", 160, 298, beim("gt2", "gewöhnliche"), "Bold", 34),
    zit("§ 434 Abs. 1, 3 Satz 1 Nr. 1 BGB", 160, 346, beim("gt2", "mangelhaft")),
    *okz("Pflichtverletzung: keine mangelfreie Sache", 405, beim("gt2b", "Pflicht"), "Bold", 34, x=160),
    zit("§ 433 Abs. 1 Satz 2 BGB", 160, 453, beim("gt2b", "mangelfreie")),
    *okz("Mangel unverzüglich angezeigt, § 377 HGB", 510, beim("gt3", "unverzüglich"), "Bold", 34, x=160),
    *okz("Vertretenmüssen vermutet, § 280 Abs. 1 Satz 2", 590, beim("gt4", "Vertretenmüssen"), "Bold", 34, x=160),
    z("keine Entlastung: Unsorgfalt in eigener Fertigung", 160, 638, beim("gt4", "Unsorgfalt"), size=33),
    blk(110, 705, 1040, 115, LILA, "gt5", [("Bloßer Händler: Verschulden des Herstellers", "ExtraBold", 32, INK),
                                          ("wird ihm nicht zugerechnet", "ExtraBold", 32, INK)]),
    zit("BGH V ZR 93/08 Rn. 19; VIII ZR 211/07 Rn. 29", 110, 830, beim("gt5", "Herstellers")),
    *requisit([("gt1", ("tabler", "file-text", 100, WEISS), "Kaufvertrag", WEISS),
               ("gt2", ("tabler", "temperature", 80, ROT), "Sachmangel", ROT),
               ("gt3", ("tabler", "phone", 90, WEISS), "sofort gemeldet", BLAU),
               ("gt4", ("tabler", "scale", 100, WEISS), "vermutet", WEISS),
               ("gt5", ("tabler", "building-factory-2", 110, WEISS), "Hersteller", LILA)]),
    *paar("gt1", [("gt1", "ruhig"), ("gt3", "laechelt"), ("gt5", "denkt")],
          [("gt1", "ruhig"), ("gt2", "sorge"), ("gt4", "muede"), ("gt5", "denkt")]),
]))

# ===========================================================================================================================
# E Statt der Leistung: § 280 Abs. 3, § 281 Abs. 1 Satz 1 (Wortlaut)
# ===========================================================================================================================
W3 = ["„(3) Schadensersatz statt der Leistung kann der Gläubiger nur",
      "unter den zusätzlichen Voraussetzungen des § 281, des § 282",
      "oder des § 283 verlangen.“"]
W281 = ["„Soweit der Schuldner die fällige Leistung nicht oder nicht wie",
        "geschuldet erbringt, kann der Gläubiger unter den Voraussetzungen",
        "des § 280 Abs. 1 Schadensersatz statt der Leistung verlangen,",
        "wenn er dem Schuldner erfolglos eine angemessene Frist zur",
        "Leistung oder Nacherfüllung bestimmt hat.“"]
w3, w3_y = wortlaut(80, 170, 1100, W3, "§ 280 Abs. 3 BGB", beim("w3", "Absatz"), marken=[
    (1, "zusätzlichen Voraussetzungen", beim("w3", "zusätzliche")), (1, "des § 281", beim("w3", "Paragraf"))], size=32)
w281, w281_y = wortlaut(80, w3_y + 18, 1100, W281, "§ 281 Abs. 1 Satz 1 BGB", "w281", marken=[
    (3, "erfolglos", beim("w281", "erfolglos")), (3, "angemessene Frist", beim("w281", "angemessene")),
    (4, "Leistung oder Nacherfüllung", beim("w281", "Leistung"))], size=32)
folie([("w3", "Statt der Leistung › § 280 Abs. 3 BGB"), ("w281", "Statt der Leistung › § 281 Abs. 1 Satz 1 BGB")], rechts_frei([
    *tafel("w3", "Statt der Leistung: §§ 280 Abs. 3, 281", size=44),
    *w3, *w281,
    blk(110, w281_y + 14, 1040, 72, GELB, "sinn", [("Frist: letzte Chance für den Verkäufer", "ExtraBold", 34, INK)]),
    zit("BGH VIII ZR 211/07 Rn. 21; VII ZR 63/18 Rn. 18", 110, w281_y + 96, beim("sinn", "Chance")),
    *requisit([("w3", ("tabler", "list-numbers", 100, WEISS), "zusätzlich", WEISS),
               ("w281", ("tabler", "hourglass", 90, GELB), "Frist", GELB),
               ("sinn", ("tabler", "refresh", 100, WEISS), "letzte Chance", GELB)]),
    *paar("w3", [("w3", "ruhig"), (beim("w281", "Frist"), "denkt")], [("w3", "ruhig"), ("sinn", "froh")]),
]))

# ===========================================================================================================================
# F Die Kontrollfrage
# ===========================================================================================================================
folie([("kf", "Die Kontrollfrage"), ("kf2", "Die Kontrollfrage › ja: statt der Leistung"),
       ("kf3", "Die Kontrollfrage › nein: neben der Leistung"), ("kf4", "Die Kontrollfrage › BGH")], rechts_frei([
    *tafel("kf", "Die Kontrollfrage"),
    z("Welcher Weg passt zu welchem Schaden?", 110, 175, "kf", "Bold", 36),
    blk(110, 265, 1040, 170, BLAU, beim("kf1", "Würde"), [("Würde eine ordnungsgemäße Nacherfüllung", "ExtraBold", 36, INK),
                                                        ("im letztmöglichen Zeitpunkt", "ExtraBold", 36, INK),
                                                        ("den Schaden noch beseitigen?", "ExtraBold", 36, INK)]),
    zit("Lehre, Klausurformel", 110, 222, beim("kf1", "Lehre")),
    blk(110, 465, 1040, 78, GELB, "kf2", [("ja: statt der Leistung, grundsätzlich nur nach Frist", "ExtraBold", 32, INK)]),
    zit("§§ 280 Abs. 1, 3, 281 BGB", 110, 551, beim("kf2", "statt")),
    blk(110, 600, 1040, 78, GRUEN, "kf3", [("nein: neben der Leistung, ohne Frist", "ExtraBold", 32, INK)]),
    zit("§ 280 Abs. 1 BGB", 110, 686, beim("kf3", "Paragraf")),
    z("BGH: ob eine Nacherfüllung den Schaden beseitigen würde", 110, 750, "kf4", "Bold", 32),
    zit("BGH VII ZR 63/18 Rn. 17, 19; VIII ZR 169/12 Rn. 26 f.", 110, 800, beim("kf4", "Nacherfüllung")),
    *requisit([("kf", ("tabler", "zoom-question", 100, WEISS), "Kontrollfrage", BLAU),
               ("kf2", ("tabler", "hourglass", 90, GELB), "statt: Frist", GELB),
               ("kf3", ("tabler", "plus", 90, GRUEN), "neben: ohne Frist", GRUEN),
               ("kf4", ("tabler", "scale", 100, WEISS), "BGH", WEISS)]),
    *paar("kf", [("kf", "ruhig"), ("kf1", "denkt"), ("kf3", "laechelt")], [("kf", "ruhig"), ("kf1", "denkt"), ("kf4", "ernst")]),
]))


# ===========================================================================================================================
# G/H/I Posten 1–3: gleiche Tafelstruktur (Posten – Kontrollfrage – Anspruchsgrundlage)
# ===========================================================================================================================
def posten_tafel(c0, titel_, frage, cue_frage, antwort, cue_antwort, ja, agl, cue_agl):
    """Standardzeilen jeder Posten-Tafel: Kontrollfrage (Frage, Antwort mit Haken/Kreuz), Anspruchsgrundlage (Block gelb =
    statt der Leistung, grün = neben der Leistung)."""
    return [*tafel(c0, titel_),
            z("Kontrollfrage:", 110, 175, cue_frage, "Bold", 30, farbe=TEXT),
            z(frage, 110, 218, cue_frage, size=34),
            *(okz if ja else neinz)(antwort, 285, cue_antwort, "Bold", 36, x=160),
            linienzug([(110, 360), (1150, 360)], cue_agl, breite=3),
            z("Anspruchsgrundlage:", 110, 378, cue_agl, "Bold", 30, farbe=TEXT),
            blk(110, 425, 1040, 80, GELB if ja else GRUEN, cue_agl, [(agl, "ExtraBold", 34, INK)])]


folie([("a1", "Posten 1: Chip › Kontrollfrage"), ("a1e", "Posten 1: Chip › statt der Leistung"),
       ("a1f", "Posten 1: Chip › Frist")], rechts_frei([
    *posten_tafel("a1", "Posten 1: der Chip (300 €)", "Beseitigt ein fehlerfreier Chip den Schaden?", "a1k",
                  "ja, dieser Schaden ist weg", beim("a1k", "weg"), True,
                  "statt der Leistung: §§ 280 Abs. 1, 3, 281 BGB", "a1e"),
    *neinz("ohne Frist kein Geld", 545, "a1f", "Bold", 36, x=160),
    z("zuerst Nacherfüllung verlangen und Frist setzen", 160, 610, beim("a1n", "Nacherfüllung"), size=34),
    z("Ausnahmen: § 281 Abs. 2, § 440 BGB", 160, 690, "a1x", size=34),
    *requisit([("a1", ("tabler", "cpu", 100, ROT), "Chip: 300 €", GELB),
               ("a1k", ("tabler", "cpu", 100, GRUEN), "fehlerfreier Chip", GRUEN),
               ("a1f", ("tabler", "hourglass", 90, WEISS), "keine Frist", ROT),
               ("a1n", ("tabler", "hourglass", 90, GELB), "Frist setzen", GELB)]),
    *paar("a1", [("a1", "ruhig"), ("a1f", "sorge"), ("a1n", "denkt")], [("a1", "ruhig"), ("a1k", "froh")]),
]))

folie([("b1", "Posten 2: Steuerungseinheit › Kontrollfrage"), ("b1e", "Posten 2: Steuerungseinheit › neben der Leistung")], rechts_frei([
    *posten_tafel("b1", "Posten 2: Steuerungseinheit (6.000 €)", "Repariert ein neuer Chip die Steuerungseinheit?", "b1k",
                  "nein, der Schaden bliebe", beim("b1k", "Schaden"), False,
                  "neben der Leistung: § 280 Abs. 1 BGB", "b1e"),
    zit("vgl. BGH VII ZR 63/18 Rn. 17, 19; BT-Drucks. 14/6040, S. 224", 110, 515, beim("b1e", "allein")),
    *okz("6.000 € für Elfriede, ohne Frist", 590, beim("b1s", "sechstausend"), "Bold", 36, x=160),
    *requisit([("b1", ("tabler", "settings-automation", 100, GRAU_A), "Steuerungseinheit", WEISS),
               ("b1k", ("tabler", "cpu", 100, GRUEN), "neuer Chip?", WEISS),
               ("b1e", ("tabler", "plus", 90, GRUEN), "neben der Leistung", GRUEN),
               (beim("b1s", "sechstausend"), ("tabler", "coin-euro", 100, GELB), "6.000 €", GELB)]),
    *paar("b1", [("b1", "ruhig"), ("b1s", "froh")], [("b1", "ruhig"), ("b1k", "sorge"), ("b1s", "muede")]),
]))

folie([("c1", "Posten 3: Produktionsausfall › Kontrollfrage"), ("c1e", "Posten 3: Produktionsausfall › neben der Leistung"),
       ("c1b", "Posten 3: Produktionsausfall › BGH, V ZR 93/08"), ("c1v", "Posten 3 › Verzögerungsschaden, § 280 Abs. 2 BGB")], rechts_frei([
    *posten_tafel("c1", "Posten 3: Produktionsausfall (4.500 €)", "Macht eine Nacherfüllung den Stillstand ungeschehen?", "c1k",
                  "nein, 3 Tage Stillstand bleiben", beim("c1k", "ungeschehen"), False,
                  "neben der Leistung: § 280 Abs. 1 BGB", "c1e"),
    z("BGH: Nutzungsausfall ohne Verzug ersatzfähig", 110, 525, beim("c1b", "Nutzungsausfall"), "Bold", 34),
    zit("BGH, Urt. v. 19.6.2009 – V ZR 93/08, Rn. 12, 14", 110, 572, beim("c1b", "Verzugs")),
    zit("BT-Drucks. 14/6040, S. 225: Betriebsausfall bei mangelhafter Maschine", 110, 610, beim("c1g", "Gesetzesbegründung")),
    *okz("4.500 € für Elfriede, ohne Frist", 655, beim("c1s", "viertausendfünfhundert"), "Bold", 36, x=160),
    linienzug([(110, 725), (1150, 725)], "c1v", breite=3),
    z("verzögerte Nacherfüllung: Verzug nötig,", 110, 740, "c1v", "Bold", 32),
    z("§§ 280 Abs. 2, 286 BGB", 110, 785, beim("c1v", "Paragraf"), "Bold", 32),
    blk(560, 775, 590, 64, LILA, beim("c1v", "Video"), [("Video „Schuldnerverzug“", "ExtraBold", 30, INK)]),
    *requisit([("c1", ("tabler", "clock-pause", 100, GELB), "3 Tage Stillstand", WEISS),
               ("c1e", ("tabler", "plus", 90, GRUEN), "neben der Leistung", GRUEN),
               ("c1b", ("tabler", "scale", 100, WEISS), "BGH 2009", WEISS),
               ("c1g", ("tabler", "printer", 100, BLAU), "Betriebsausfall", BLAU),
               ("c1s", ("tabler", "coin-euro", 100, GELB), "4.500 €", GELB),
               ("c1v", ("tabler", "hourglass", 90, WEISS), "Verzug", LILA)]),
    *paar("c1", [("c1", "sorge"), ("c1s", "froh"), ("c1v", "denkt")], [("c1", "ruhig"), ("c1b", "ernst"), ("c1v", "denkt")]),
]))

# ===========================================================================================================================
# J Lösung (Tabelle)
# ===========================================================================================================================
TX = [110, 470, 700, 905]
ZEILEN = [("l1", "1. Chip", "ja", "statt", ("erst Frist", -1)),
          ("l2", "2. Steuerungseinheit", "nein", "neben", ("6.000 €", 1)),
          ("l3", "3. Produktionsausfall", "nein", "neben", ("4.500 €", 1))]
els_l = [*tafel("loes", "Die Lösung")]
for t, x in zip(("Posten", "Kontrollfrage", "Anspruch", "Ergebnis"), TX):
    els_l.append(z(t, x, 180, "loes", "Bold", 28, farbe=TEXT))
els_l.append(linienzug([(110, 228), (1150, 228)], "loes", breite=3))
for k, (c, p, kf, an, (erg, wert)) in enumerate(ZEILEN):
    y = 255 + k * 105
    els_l += [z(p, TX[0], y, c, "Bold", 32), z(kf, TX[1], y, c, size=32), z(an, TX[2], y, c, "Bold", 32)]
    if wert > 0:
        els_l.append(ok(TX[3] - 2, y + 18, c, gr=18))
    else:
        els_l.append(nein(TX[3] - 2, y + 18, c, gr=18))
    els_l.append(z(erg, TX[3] + 40, y, c, size=32))
    els_l.append(linienzug([(110, y + 72), (1150, y + 72)], c, breite=2))
els_l.append(blk(110, 600, 1040, 80, GRUEN, "l4", [("zusammen sofort: 10.500 €", "ExtraBold", 36, INK)]))
folie([("loes", "Lösung › alle drei Posten")], rechts_frei([
    *els_l,
    *requisit([("loes", ("tabler", "table", 100, WEISS), "drei Posten", WEISS),
               ("l1", ("tabler", "hourglass", 90, GELB), "Chip: erst Frist", GELB),
               ("l2", ("tabler", "settings-automation", 100, GRAU_A), "Steuerungseinheit", GRUEN),
               ("l3", ("tabler", "clock-pause", 100, GELB), "Produktionsausfall", GRUEN),
               ("l4", ("tabler", "cash-banknote", 110, GRUEN), "10.500 €", GRUEN)]),
    *paar("loes", [("loes", "ruhig"), ("l2", "froh")], [("loes", "ruhig"), ("l4", "muede")]),
]))

# ===========================================================================================================================
# K Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Posten für Posten")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Schadensposten für Schadensposten prüfen", 200, 200, beim("tipp", "Prüfe"), "Bold", 38),
    z("1. bei jedem die Kontrollfrage stellen", 240, 285, "t1", size=38),
    z("2. erst dann die Anspruchsgrundlage wählen", 240, 350, "t2", size=38),
    *neinz("nie alle Posten in einen Topf", 440, "t3", "Bold", 38, x=240),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# L Klausurschema
# ===========================================================================================================================
REIHEN = [("k1", "I.", "Kontrollfrage: statt oder neben der Leistung?", "", BLAU),
          ("k2", "II.", "Schuldverhältnis und Pflichtverletzung", "§ 280 Abs. 1 S. 1", GELB),
          ("k3", "III.", "nur statt der Leistung: erfolglose Frist", "§ 281 Abs. 1 S. 1", GELB),
          ("k4", "IV.", "Vertretenmüssen, vermutet", "§ 280 Abs. 1 S. 2", GRUEN),
          ("k5", "V.", "Schaden", "§§ 249 ff.", GRUEN)]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Klausurschema: Schadensersatz je Posten"), 110, 90, "sch", 50)]
y = 215
for c, r, kopf, norm, farbe in REIHEN:
    els_sch += [karte(110, y, 120, 76, c, fill=farbe, rund=14, schatten=5, rand=4),
                z(r, 170 - F("ExtraBold", 38).getlength(r) / 2, y + 12, c, "ExtraBold", 38, rechts=1820),
                z(kopf, 265, y + 12, c, "ExtraBold", 40, rechts=1460)]
    if norm:
        els_sch.append(zit(norm, 1500, y + 20, c, size=30, rechts=1820))
    y += 140
assert y <= 970, y
folie([("sch", "Klausurschema"), ("k1", "Klausurschema › I. Kontrollfrage"), ("k2", "Klausurschema › II. Pflichtverletzung"),
       ("k3", "Klausurschema › III. Frist (nur statt)"), ("k4", "Klausurschema › IV. Vertretenmüssen"),
       ("k5", "Klausurschema › V. Schaden")], els_sch)

# ===========================================================================================================================
# M Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Was eine Nacherfüllung noch", 0)], [("beseitigen könnte, gibt es nur", 0)],
                 [("statt der Leistung,", "a")]], 750, 280, 42, "merke", {"a": beim("merke", "statt")}),
    *markertext([[("also grundsätzlich erst nach Frist.", "b")]], 750, 470, 40, "mk2", {"b": beim("mk2", "Frist")}),
    *markertext([[("Was trotz Nacherfüllung bleibt,", 0)], [("gibt es neben der Leistung,", "c")]],
                750, 590, 42, "mk3", {"c": beim("mk3", "neben")}),
    *markertext([[("ohne Frist.", "d")]], 750, 780, 44, "mk4", {"d": "mk4"}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
