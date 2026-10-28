"""Folge 146 · Lüth-Urteil: Mittelbare Drittwirkung der Grundrechte erklärt – Serienstandard Open Peeps (Katzenkönig).
Moderner Einstieg mit fiktiven Figuren (Wenke, Bloggerin; Herr Gerstner, Filmproduzent), danach der echte Fall sachlich:
BVerfG, Urt. v. 15.1.1958 – 1 BvR 400/51, BVerfGE 7, 198 (Seiten der amtlichen Sammlung nach DFR). SENSIBEL: Erich Lüth
und Veit Harlan treten nicht als Figuren auf; keine NS-Symbole, keine Filmbilder, keine Plakate; nur neutrale Icons
(Rednerpult, Zeitung, Kino, Gericht). Szenen laut ../SZENENPLAN.md. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/
fig/ns/okz/neinz als eigene Kopie aus Folge 143 (gemeinsame Dateien unverändert); neu: tisch(), requisit(pu=…),
station(). Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from ostil import titel, karte, pille
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_146/"

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
        if n.startswith(("bild:", "ficon:", "bank")) or "/op_146/" in n:
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
NAME = {"WE": "Wenke", "GE": "Herr Gerstner"}
NFARBE = {"WE": GRUEN, "GE": LILA}


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
# A1 Fall: Wenkes Filmblog, die Unterlassungsklage (fiktiv)
# ===========================================================================================================================
WEX, GEX = 980, 1620
BLOG = (70, 120, 840, 330)                  # Blogbeitrag auf dem Bildschirm (Karte links oben)


def blog_karte(cue):
    x, y, w, h = BLOG
    return [hart(karte(x, y, w, h, cue, fill=WEISS, rund=18, schatten=6, rand=4)),
            hart(linienzug([(x, y + 62), (x + w, y + 62)], cue, breite=4)),
            hart(z("Wenkes Filmblog", x + 30, y + 10, cue, "ExtraBold", 32))]


folie([(NULL, "Fall · Wenkes Filmblog"), ("gerst", "Fall · Die Unterlassungsklage")], [
    boden(NULL),
    tisch(250, 520, NULL),
    hart(ficon("tabler", "device-laptop", 510, BODEN - 214, 190, NULL, fuell=BLAUHELL, anim="cut")),
    *blog_karte(NULL),
    ficon("tabler", "movie", 175, 300, 120, "neu", fuell=GELB),
    z("Neuer Kinofilm", 270, 200, "neu", "ExtraBold", 36),
    z("„verherrlicht illegale", 270, 255, beim("w1", "verherrlicht"), "Bold", 32),
    z("Autorennen“", 270, 300, beim("w1", "verherrlicht"), "Bold", 32),
    ficon("tabler", "car", 175, 430, 120, beim("w1", "Autorennen"), fuell=ROT),
    pl("Schaut ihn euch nicht an!", 270, 370, beim("w1", "Schaut"), fill=HELLROT, size=30),
    # Wenke steht am Schreibtisch, blickt zum Laptop (links), ab Gerstners Auftritt zu ihm (rechts)
    *fig("WE", WEX, BODEN, FH, [(NULL, "ruhig")], bis="w1", erst="cut"),
    *redet("WE_redet", WEX, BODEN, FH, "w1", "gerst"),
    *fig("WE", WEX, BODEN, FH, [("gerst", "denkt_r"), ("g1", "sorge_r")], erst="cut"),
    hart(ns("Wenke", WEX, BODEN, NULL, GRUEN)),
    blase("sprech", 640, 200, "w1", 1300, 280, inhalt=["Dieser Film verherrlicht", "illegale Autorennen.",
                                                    "Schaut ihn euch nicht an!"], textsize=31,
          figur=("WE_redet", WEX, BODEN, FH), bis="gerst"),
    # Herr Gerstner (Produzent) kommt von rechts, blickt nach links zu Wenke
    szene(bewegt(peep_voll("GE_ruhig", GEX, BODEN, FH, "gerst", anim="cut", bis="g1"), "gerst", ("gerst", 1.0), 70, 0),
          "146schritte*", 0.8, 0.05),
    *redet("GE_redet", GEX, BODEN, FH, "g1", "frage0"),
    bewegt(ns("Herr Gerstner", GEX, BODEN, "gerst", LILA, anim="cut"), "gerst", ("gerst", 1.0), 70, 0),
    pl("Produzent: Sorge um den Kinostart", 1110, 40, beim("gerst", "Kinostart"), fill=GELB, size=30),
    blase("sprech", 640, 200, "g1", 1330, 300, inhalt=["Ihr Aufruf kostet uns Zuschauer.", "Ich verklage Sie",
                                                    "auf Unterlassung."], textsize=31,
          figur=("GE_redet", GEX, BODEN, FH), bis="frage0"),
    pl("Klage auf Unterlassung", 70, 478, beim("g1", "verklage"), fill=HELLROT, size=30),
])

# ===========================================================================================================================
# A2 Die Frage
# ===========================================================================================================================
folie([("frage0", "Die Frage · Grundrechte zwischen Privaten?"), ("klassiker", "Die Frage · Das Lüth-Urteil")], [
    *tafel("frage0", "Zwei Private streiten"),
    z("Bloggerin gegen Produzent:", 110, 190, "frage0", "Bold", 36),
    z("Klage vor einem Zivilgericht", 110, 240, beim("frage0", "Zivilgericht"), size=36),
    pl("Gelten die Grundrechte auch zwischen ihnen?", 110, 340, beim("frage0", "Gelten"), fill=PINK, size=36),
    blk(110, 470, 1040, 120, GELB, "klassiker", [("Die Antwort gibt das Bundesverfassungsgericht", "ExtraBold", 34, INK),
                                              ("im Lüth-Urteil", "ExtraBold", 34, INK)]),
    zit("BVerfG, Urt. v. 15.1.1958 – 1 BvR 400/51, BVerfGE 7, 198", 110, 605, "klassiker"),
    *requisit([("frage0", ("tabler", "building-bank", 120, WEISS), "Zivilgericht", WEISS),
               ("klassiker", ("tabler", "scale", 110, GELB), "Lüth-Urteil", GELB)]),
    *paar("WE", [("frage0", "denkt")], "GE", [("frage0", "denkt"), ("klassiker", "ruhig")]),
])

# ===========================================================================================================================
# B1 Der echte Fall: Hamburg 1950 (BVerfGE 7, 198 <199 f.>) – ohne Figuren, neutrale Icons
# ===========================================================================================================================
folie([("lueth", "Der echte Fall · Hamburg, 20.9.1950"), ("brief", "Der echte Fall · Der Boykottaufruf")], [
    boden("lueth"),
    pl("Hamburg · 20.9.1950", 70, 40, "lueth", fill=GELB, size=34),
    pl("Erich Lüth: Senatsdirektor, Vorsitzender des Hamburger Presseklubs", 70, 118, "rede", fill=WEISS, size=30),
    pl("Ansprache vor Filmverleihern und Filmproduzenten", 70, 188, beim("rede", "Filmverleihern"), fill=WEISS, size=30),
    pl("gegen das Wiederauftreten des Regisseurs Veit Harlan", 70, 258, "harlan", fill=HELL, size=30),
    pl("Harlan: Regie beim antisemitischen Film „Jud Süß“ (Zeit des Nationalsozialismus)", 70, 328, "jud",
       fill=WEISS, size=30),
    ficon("tabler", "podium", 330, BODEN, 260, "lueth", fuell=HOLZ),
    ficon("tabler", "microphone-2", 330, BODEN - 270, 90, beim("rede", "spricht"), fuell=WEISS),
    ficon("tabler", "news", 960, BODEN, 230, "brief", fuell=WEISS),
    pl("offener Brief: „auch zum Boykott bereitzuhalten“", 960, 470, beim("brief", "Boykott"), fill=HELLROT, size=30,
       anker="m"),
    ficon("tabler", "movie", 1560, BODEN, 230, "film", fuell=BLAUHELL),
    pl("neuer Film: „Unsterbliche Geliebte“", 1560, 560, beim("film", "Unsterbliche"), fill=WEISS, size=30, anker="m"),
])

# ===========================================================================================================================
# B2 Landgericht Hamburg 1951, Verfassungsbeschwerde, Frage (<200–202>)
# ===========================================================================================================================
folie([("klage", "Der echte Fall · LG Hamburg, 22.11.1951"), ("vb", "Der echte Fall · Verfassungsbeschwerde"),
       ("frage", "Der echte Fall · Die Frage")], [
    *tafel("klage", "Das Urteil des Landgerichts Hamburg"),
    z("Klage: Produktionsfirma und Verleiherin", 110, 180, "klage", "Bold", 34),
    *neinz("22.11.1951: Lüth zur Unterlassung verurteilt", 260, "lg", "Bold", 34, x=160),
    z("Boykottaufruf sittenwidrig, § 826 BGB", 160, 330, "sitten", "Bold", 34),
    z("Harlan rechtskräftig freigesprochen,", 160, 390, "frei", size=32),
    z("darf seinen Beruf wieder ausüben", 160, 435, beim("frei", "Beruf"), size=32),
    zit("BVerfGE 7, 198 <200–202>", 160, 485, beim("frei", "Beruf")),
    blk(110, 545, 1040, 80, GELB, "vb", [("Lüth erhebt Verfassungsbeschwerde", "ExtraBold", 34, INK)]),
    zit("BVerfGE 7, 198 <202>", 110, 640, "vb"),
    pl("Welche Rolle spielt die Meinungsfreiheit", 110, 700, "frage", fill=PINK, size=34),
    pl("in einem Streit unter Privaten?", 110, 776, beim("frage", "Streit"), fill=PINK, size=34),
    *requisit([("klage", ("tabler", "file-text", 150, WEISS), "Klage", WEISS),
               ("lg", ("tabler", "gavel", 170, HOLZ), "Landgericht Hamburg", WEISS),
               ("sitten", ("tabler", "book", 150, WEISS), "§ 826 BGB", WEISS),
               ("vb", ("tabler", "building-bank", 180, WEISS), "Verfassungsbeschwerde", GELB),
               ("frage", ("tabler", "message", 160, PINK), "Meinungsfreiheit?", PINK)], pu=640, py=260),
])


# ===========================================================================================================================
# C Sachverhalt
# ===========================================================================================================================
def sachverhalt_146(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=33, zeilenabstand=1.28)
        els += e; y += 16
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_146("sv", [
    "Hamburg, 20. September 1950: Senatsdirektor Erich Lüth spricht als Vorsitzender des Hamburger Presseklubs vor "
    "Filmverleihern und Filmproduzenten gegen das Wiederauftreten des Regisseurs Veit Harlan, der den antisemitischen "
    "Film „Jud Süß“ gedreht hatte. In einem offenen Brief ruft er dazu auf, sich gegen Harlan auch zum Boykott "
    "bereitzuhalten. Harlans neuer Film heißt „Unsterbliche Geliebte“.",
    "Auf die Klage der Produktionsfirma und der Verleiherin verurteilt das Landgericht Hamburg Lüth am 22. November 1951 "
    "zur Unterlassung: Er darf Kinobesitzer und Verleiher nicht auffordern, den Film nicht zu zeigen, und das Publikum "
    "nicht, ihn nicht zu besuchen. Der Boykottaufruf sei sittenwidrig nach § 826 BGB. Lüth erhebt Verfassungsbeschwerde.",
], "Verletzt das Urteil Lüths Meinungsfreiheit aus Art. 5 Abs. 1 Satz 1 GG?")

# ===========================================================================================================================
# D1 Abwehrrechte und objektive Wertordnung (<204 f.>, Leitsatz 1)
# ===========================================================================================================================
PI = "I. Grundrechte im Privatrecht"
folie([("urteil", f"{PI} · BVerfG, 15.1.1958"), ("abwehr", f"{PI} › Abwehrrechte gegen den Staat"),
       ("wert", f"{PI} › objektive Wertordnung"), ("buerg", f"{PI} › auch im bürgerlichen Recht")], [
    *tafel("urteil", "Das Bundesverfassungsgericht, 15.1.1958"),
    zit("BVerfG, Urteil vom 15.1.1958 – 1 BvR 400/51 (BVerfGE 7, 198)", 110, 168, "urteil"),
    *okz("in erster Linie: Abwehrrechte", 240, "abwehr", "Bold", 36, x=160),
    z("des Bürgers gegen den Staat", 160, 290, beim("abwehr", "Bürgers"), "Bold", 36),
    zit("BVerfGE 7, 198 <204>", 160, 342, beim("abwehr", "Bürgers")),
    *okz("aber auch: eine objektive Wertordnung", 410, "wert", "Bold", 36, x=160),
    z("Grundentscheidung für alle Bereiche des Rechts", 160, 460, "alle", size=34),
    zit("<205>; Leitsatz 1", 160, 510, "alle"),
    blk(110, 580, 1040, 120, GRUEN, "buerg", [("auch im bürgerlichen Recht:", "ExtraBold", 36, INK),
                                            ("jede Vorschrift in ihrem Geist auslegen", "ExtraBold", 36, INK)]),
    zit("<205>", 110, 715, "buerg"),
    *requisit([("urteil", ("tabler", "building-bank", 120, WEISS), "BVerfG, 15.1.1958", GELB),
               ("abwehr", ("tabler", "shield-check", 100, BLAUHELL), "Abwehrrechte", BLAUHELL),
               ("wert", ("tabler", "scale", 100, GELB), "objektive Wertordnung", GELB),
               ("buerg", ("tabler", "book", 100, GRUEN), "bürgerliches Recht", GRUEN)]),
    *paar("WE", [("urteil", "ruhig"), ("buerg", "froh")], "GE", [("urteil", "ruhig"), ("buerg", "denkt")]),
])

# ===========================================================================================================================
# D2 Durch das Privatrecht: Generalklauseln als Einbruchstellen (<205 f.>, Leitsatz 2)
# ===========================================================================================================================
folie([("medium", f"{PI} › durch das Privatrecht"), ("einbruch", f"{PI} › Einbruchstellen: Generalklauseln"),
       ("mittelbar", f"{PI} › mittelbare Drittwirkung")], [
    *tafel("medium", "Wie wirken die Grundrechte unter Privaten?"),
    blk(110, 185, 380, 120, GELB, beim("medium", "Grundrechte"), [("Grundrechte", "ExtraBold", 34, INK),
                                                                 ("Wertordnung", "Regular", 30, INK)]),
    pfeil(505, 245, 640, 245, beim("medium", "Medium"), breite=10, kopf=30),
    blk(655, 185, 495, 120, WEISS, beim("medium", "Vorschriften"), [("Vorschriften", "ExtraBold", 34, INK),
                                                                   ("des Privatrechts", "Regular", 30, INK)]),
    *okz("Der Streit bleibt ein bürgerlicher Rechtsstreit.", 345, "bleibt", "Bold", 34, x=160),
    zit("BVerfGE 7, 198 <205 f.>", 160, 395, "bleibt"),
    blk(110, 460, 1040, 120, LILA, "einbruch", [("Einbruchstellen: die Generalklauseln,", "ExtraBold", 34, INK),
                                              ("etwa die „guten Sitten“ in § 826 BGB", "ExtraBold", 34, INK)]),
    zit("<206>", 110, 595, "einbruch"),
    pl("mittelbare Drittwirkung", 110, 660, "mittelbar", fill=PINK, size=40),
    zit("Leitsatz 2: „mittelbar durch die privatrechtlichen Vorschriften“", 110, 750, "mittelbar"),
    *requisit([("medium", ("tabler", "book", 100, WEISS), "Privatrecht", WEISS),
               ("einbruch", ("tabler", "door-enter", 100, LILA), "Einbruchstelle", LILA),
               ("mittelbar", ("tabler", "users-group", 110, WEISS), "unter Privaten", PINK)]),
    *paar("WE", [("medium", "ruhig"), ("einbruch", "denkt")], "GE", [("medium", "denkt"), ("mittelbar", "ruhig")]),
])

# ===========================================================================================================================
# D3 Art. 1 Abs. 3 GG (Wortlautkarte): gebunden ist der Zivilrichter (<206 f.>)
# ===========================================================================================================================
W13 = ["„(3) Die nachfolgenden Grundrechte binden Gesetzgebung,",
       "vollziehende Gewalt und Rechtsprechung als unmittelbar",
       "geltendes Recht.“"]
w13, w13_y = wortlaut(80, 190, 1100, W13, "Art. 1 Abs. 3 GG", "a13", marken=[
    (0, "binden", beim("a13", "binden")), (1, "Rechtsprechung", beim("a13", "Rechtsprechung")),
    (1, "unmittelbar", beim("a13", "unmittelbar", nr=2))], size=33)
folie([("a13", f"{PI} › Art. 1 Abs. 3 GG"), ("richter", f"{PI} › gebunden: der Zivilrichter"),
       ("verkennt", f"{PI} › Verkennen verletzt das Grundrecht")], [
    *tafel("a13", "Wer ist unmittelbar gebunden?"),
    *w13,
    *okz("gebunden ist der Zivilrichter", w13_y + 40, "richter", "Bold", 36, x=160),
    zit("BVerfGE 7, 198 <206>", 160, w13_y + 92, "richter"),
    blk(110, w13_y + 160, 1040, 120, HELLROT, "verkennt", [("Verkennt er den Einfluss der Grundrechte,", "ExtraBold", 34, INK),
                                                        ("verletzt sein Urteil das Grundrecht", "ExtraBold", 34, INK)]),
    zit("<206 f.>; Leitsatz 3", 110, w13_y + 295, "verkennt"),
    *requisit([("a13", ("tabler", "book", 100, WEISS), "Art. 1 Abs. 3 GG", GELB),
               ("richter", ("tabler", "gavel", 110, HOLZ), "Zivilrichter", WEISS),
               ("verkennt", ("tabler", "alert-triangle", 100, HELLROT), "Grundrecht verletzt", HELLROT)]),
    *stehend("GE", FX, [("a13", "ruhig"), ("richter", "denkt"), ("verkennt", "sorge")]),
])

# ===========================================================================================================================
# D4 Kontrast Fraport; Lüth sprach als Privatmann (BVerfGE 128, 226 Rn. 45, 49; BVerfGE 7, 198 <213>)
# ===========================================================================================================================
folie([("kontrast", f"{PI} › Kontrast: Fraport-Fall"), ("privatmann", f"{PI} › Lüth sprach als Privatmann")], [
    *tafel("kontrast", "Kontrast: der Fraport-Fall"),
    blk(110, 190, 1040, 120, BLAUHELL, "kontrast", [("Fraport: Der Staat ist Mehrheitsaktionär,", "ExtraBold", 34, INK),
                                                  ("das Unternehmen selbst unmittelbar gebunden", "ExtraBold", 34, INK)]),
    zit("BVerfG, Urt. v. 22.2.2011 – 1 BvR 699/06, BVerfGE 128, 226, Rn. 45, 49", 110, 325, "kontrast"),
    blk(110, 420, 1040, 120, HELL, "privatmann", [("Lüth: zwar Senatsdirektor,", "ExtraBold", 34, INK),
                                                ("aber er sprach als Privatmann", "ExtraBold", 34, INK)]),
    zit("BVerfGE 7, 198 <213>", 110, 555, "privatmann"),
    *requisit([("kontrast", ("tabler", "building-airport", 120, BLAUHELL), "Fraport", BLAUHELL),
               ("privatmann", ("tabler", "user", 100, HELL), "Privatmann", HELL)]),
    *paar("WE", [("kontrast", "ruhig")], "GE", [("kontrast", "ruhig"), ("privatmann", "denkt")]),
])

# ===========================================================================================================================
# E1 Art. 5 Abs. 1 Satz 1, Abs. 2 GG (Wortlautkarte), Wirkung, § 826 BGB als allgemeines Gesetz (<210, 214>)
# ===========================================================================================================================
PII = "II. Meinungsfreiheit"
W5 = ["„(1) Jeder hat das Recht, seine Meinung in Wort, Schrift und",
      "Bild frei zu äußern und zu verbreiten …",
      "(2) Diese Rechte finden ihre Schranken in den Vorschriften",
      "der allgemeinen Gesetze …“"]
w5, w5_y = wortlaut(80, 190, 1100, W5, "Art. 5 Abs. 1 Satz 1, Abs. 2 GG (Auszug)", "a5", marken=[
    (1, "äußern", beim("a5", "äußern")), (1, "verbreiten", beim("a5", "verbreiten")),
    (2, "Schranken", beim("a52", "Schranken")), (3, "allgemeinen Gesetze", beim("a52", "allgemeinen"))], size=32)
folie([("a5", f"{PII} · Art. 5 Abs. 1 Satz 1 GG"), ("a52", f"{PII} › Schranke: allgemeine Gesetze, Art. 5 Abs. 2 GG"),
       ("wirkung", f"{PII} › auch die Wirkung geschützt"), ("allg", f"{PII} › § 826 BGB: allgemeines Gesetz")], [
    *tafel("a5", "Die Meinungsfreiheit, Art. 5 GG"),
    *w5,
    *okz("geschützt auch die Wirkung:", w5_y + 30, "wirkung", "Bold", 34, x=160),
    z("Wer ein Werturteil fällt, will überzeugen.", 160, w5_y + 78, beim("wirkung", "Werturteil"), size=34),
    zit("BVerfGE 7, 198 <210>; Leitsatz 6", 160, w5_y + 126, beim("wirkung", "Werturteil")),
    blk(110, w5_y + 180, 1040, 80, LILA, "allg", [("auch § 826 BGB ist ein allgemeines Gesetz", "ExtraBold", 34, INK)]),
    zit("<214>; Leitsatz 4", 110, w5_y + 275, "allg"),
    *requisit([("a5", ("tabler", "message", 100, WEISS), "Meinungsfreiheit", GELB),
               ("a52", ("tabler", "fence", 110, WEISS), "Schranken", WEISS),
               ("wirkung", ("tabler", "speakerphone", 100, WEISS), "Wirkung", WEISS),
               ("allg", ("tabler", "book", 100, LILA), "§ 826 BGB", LILA)]),
    *stehend("WE", FX, [("a5", "ruhig"), ("wirkung", "froh"), ("allg", "denkt")]),
])

# ===========================================================================================================================
# E2 Die Wechselwirkung (<208 f.>, Leitsatz 5)
# ===========================================================================================================================
folie([("g2", f"{PII} › Schützt § 826 BGB das Geschäft?"), ("wechsel", f"{PII} › Wechselwirkung")], [
    *tafel("g2", "Die Wechselwirkung"),
    blk(110, 190, 380, 110, GELB, "wechsel", [("Art. 5 Abs. 1 GG", "ExtraBold", 34, INK)]),
    blk(770, 190, 380, 110, LILA, "wechsel", [("§ 826 BGB", "ExtraBold", 34, INK)]),
    pfeil(760, 225, 500, 225, beim("wechsel", "Schranke"), breite=9, kopf=28),
    z("setzt dem Wortlaut nach Schranken", 110, 330, beim("wechsel", "Schranke"), "Bold", 34),
    pfeil(500, 268, 760, 268, "licht", breite=9, kopf=28, farbe=DGRUEN),
    z("wird im Licht der Meinungsfreiheit ausgelegt", 110, 395, beim("licht", "Licht"), "Bold", 34),
    z("und so selbst wieder eingeschränkt", 110, 445, beim("licht", "eingeschränkt"), size=34),
    zit("BVerfGE 7, 198 <208 f.>; Leitsatz 5", 110, 495, beim("licht", "eingeschränkt")),
    pl("Wechselwirkung", 110, 580, "ww", fill=PINK, size=40),
    *spricht_neben("GE", X1, "g2", "wechsel", [], [("wechsel", "denkt"), ("ww", "ruhig")],
                   ["Aber § 826 schützt doch", "auch mein Geschäft."], size=32),
    ns("Herr Gerstner", X1, FB, "g2", LILA, d=0.1),
    *stehend("WE", X2, [("g2", "denkt"), ("licht", "froh")]),
])

# ===========================================================================================================================
# E3 Güterabwägung und Vermutung für die freie Rede (<210 f., 212>)
# ===========================================================================================================================
WV = ["„… ein Beitrag zum geistigen Meinungskampf in einer die",
      "Öffentlichkeit wesentlich berührenden Frage durch einen",
      "dazu Legitimierten …“"]
wv, wv_y = wortlaut(80, 330, 1100, WV, "BVerfGE 7, 198 <212>", "verm", size=32)
folie([("abw", f"{PII} › Güterabwägung"), ("verm", f"{PII} › Vermutung für die freie Rede")], [
    *tafel("abw", "Am Ende: die Güterabwägung"),
    *okz("Güterabwägung auf Grund aller Umstände", 180, "abw", "Bold", 34, x=160),
    z("des Falles", 160, 228, beim("abw", "Umstände"), "Bold", 34),
    zit("BVerfGE 7, 198 <210 f.>", 160, 278, beim("abw", "Umstände")),
    *wv,
    blk(110, wv_y + 30, 1040, 80, GRUEN, beim("verm", "Vermutung"),
        [("Vermutung für die Zulässigkeit der freien Rede", "ExtraBold", 34, INK)]),
    *requisit([("abw", ("tabler", "scale", 110, WEISS), "Güterabwägung", WEISS),
               ("verm", ("tabler", "message", 100, GRUEN), "freie Rede", GRUEN)]),
    *paar("WE", [("abw", "denkt"), (beim("verm", "Vermutung"), "froh")], "GE", [("abw", "ruhig"), (beim("verm", "Vermutung"), "denkt")]),
])

# ===========================================================================================================================
# F Die Abwägung im Fall Lüth (<215–221>)
# ===========================================================================================================================
PIII = "III. Abwägung im Fall Lüth"
folie([("motiv", f"{PIII} › Motive"), ("sorge", f"{PIII} › Ziel"), ("zwang", f"{PIII} › Mittel"),
       ("erwidern", f"{PIII} › Gegenrede")], [
    *tafel("motiv", "Die Abwägung im Fall Lüth"),
    *okz("keine eigenen wirtschaftlichen Interessen,", 180, "motiv", "Bold", 34, x=160),
    z("keine Konkurrenz zu den Filmgesellschaften", 160, 228, beim("motiv", "Konkurrenz"), size=34),
    zit("BVerfGE 7, 198 <215 f.>", 160, 278, beim("motiv", "Konkurrenz")),
    *okz("Sorge um das Ansehen Deutschlands in der Welt", 345, "sorge", "Bold", 34, x=160),
    zit("<216 f.>", 160, 395, "sorge"),
    *okz("keine Zwangsmittel: nur ein Appell an die", 460, "zwang", "Bold", 34, x=160),
    z("freie Entscheidung der Angesprochenen", 160, 508, beim("zwang", "appellierte"), size=34),
    zit("<221>", 160, 558, beim("zwang", "appellierte")),
    *okz("Wer sich angegriffen fühlt, kann öffentlich erwidern.", 625, "erwidern", "Bold", 33, x=160),
    zit("<219>", 160, 673, "erwidern"),
    *requisit([("motiv", ("tabler", "coins", 100, WEISS), "keine Eigeninteressen", WEISS),
               ("sorge", ("tabler", "world", 100, BLAUHELL), "Ansehen in der Welt", BLAUHELL),
               ("zwang", ("tabler", "hand-stop", 100, WEISS), "keine Zwangsmittel", WEISS),
               ("erwidern", ("tabler", "messages", 100, GRUEN), "Gegenrede", GRUEN)]),
    *paar("WE", [("motiv", "ruhig"), ("zwang", "froh")], "GE", [("motiv", "denkt"), ("erwidern", "ruhig")]),
])

# ===========================================================================================================================
# G1 Prüfungsmaßstab des BVerfG (<207>)
# ===========================================================================================================================
PIV = "IV. Prüfungsmaßstab des BVerfG"
folie([("pruef", PIV), ("superrev", f"{PIV} › keine Superrevisionsinstanz"), ("ausstr", f"{PIV} › Ausstrahlungswirkung")], [
    *tafel("pruef", "Was prüft das Bundesverfassungsgericht?"),
    *neinz("nicht jeden Rechtsfehler", 200, "superrev", "Bold", 36, x=160),
    z("keine Superrevisionsinstanz", 160, 252, beim("superrev", "keine"), size=34),
    zit("BVerfGE 7, 198 <207>", 160, 302, beim("superrev", "keine")),
    *okz("sondern: Hat das Zivilgericht die", 380, "ausstr", "Bold", 36, x=160),
    z("Ausstrahlungswirkung der Grundrechte", 160, 432, beim("ausstr", "Ausstrahlungswirkung"), "ExtraBold", 36),
    z("auf das bürgerliche Recht richtig beurteilt?", 160, 484, beim("ausstr", "bürgerliche"), size=34),
    zit("<207>; Leitsatz 3", 160, 534, beim("ausstr", "bürgerliche")),
    *requisit([("pruef", ("tabler", "search", 100, WEISS), "Prüfungsmaßstab", WEISS),
               ("superrev", ("tabler", "ban", 90, HELLROT), "keine Superrevision", HELLROT),
               ("ausstr", ("tabler", "sun", 110, GELB), "Ausstrahlungswirkung", GELB)]),
    *stehend("GE", FX, [("pruef", "denkt"), ("ausstr", "ruhig")]),
])

# ===========================================================================================================================
# G2 Ergebnis (<199 Tenor, 230>)
# ===========================================================================================================================
folie([("erg", "Ergebnis · Bedeutung der Meinungsfreiheit verkannt"), ("aufh", "Ergebnis · Art. 5 Abs. 1 Satz 1 GG verletzt (+)"),
       ("zurueck", "Ergebnis · Zurückverweisung")], [
    *tafel("erg", "Ergebnis"),
    blk(110, 170, 1040, 120, GRUEN, "erg", [("Das Landgericht hat die besondere Bedeutung", "ExtraBold", 34, INK),
                                          ("der Meinungsfreiheit verkannt.", "ExtraBold", 34, INK)]),
    *okz("verletzt: Art. 5 Abs. 1 Satz 1 GG", 330, "aufh", "Bold", 36, x=160),
    z("Das Urteil wird aufgehoben.", 160, 382, beim("aufh", "aufgehoben"), "Bold", 36),
    z("Die Sache geht zurück an das Landgericht.", 160, 450, "zurueck", size=34),
    zit("BVerfGE 7, 198 <199> (Entscheidungsformel), <230>", 160, 500, "zurueck"),
    *requisit([("erg", ("tabler", "circle-check", 100, GRUEN), "Verfassungsbeschwerde (+)", GRUEN),
               ("zurueck", ("tabler", "arrow-back-up", 100, WEISS), "zurück ans Landgericht", WEISS)]),
    *paar("WE", [("erg", "froh")], "GE", [("erg", "denkt")]),
])

# ===========================================================================================================================
# H Zurück zum Einstieg: Wenkes Filmblog (gleicher Schauplatz wie A1, die Geschichte kehrt dorthin zurück)
# ===========================================================================================================================
W2 = beim("w2", "Darf")
folie([("w2", "Zurück zum Fall · Wenke"), ("h3", "Zurück zum Fall · Abwägung"), ("h4", "Zurück zum Fall · Gegenrede")], [
    boden("w2"),
    tisch(250, 520, "w2"),
    hart(ficon("tabler", "device-laptop", 510, BODEN - 214, 190, "w2", fuell=BLAUHELL, anim="cut")),
    *blog_karte("w2"),
    *redet("WE_redet_r", WEX, BODEN, FH, "w2", "h1"),
    *fig("WE", WEX, BODEN, FH, [("h1", "denkt_r"), ("h3", "froh_r")], erst="cut"),
    hart(ns("Wenke", WEX, BODEN, "w2", GRUEN)),
    blase("sprech", 640, 200, "w2", 1300, 280, inhalt=["Darf ich also zum Boykott", "aufrufen, auch wenn es",
                                                    "dem Film schadet?"], textsize=31,
          figur=("WE_redet_r", WEX, BODEN, FH), bis="h1"),
    *fig("GE", GEX, BODEN, FH, [("w2", "ruhig"), ("h3", "denkt"), ("h4", "ruhig")], erst="cut"),
    hart(ns("Herr Gerstner", GEX, BODEN, "w2", LILA)),
    pl("Zivilgericht: gebunden an die Meinungsfreiheit", 1110, 40, "h1", fill=WEISS, size=30),
    z("keine eigenen wirtschaftlichen Ziele?", 150, 200, beim("h2", "wirtschaftlichen"), "Bold", 31, rechts=890),
    z("Äußerung zu einer öffentlichen Frage?", 150, 255, beim("h2", "öffentlichen"), "Bold", 31, rechts=890),
    z("keine Zwangsmittel?", 150, 310, beim("h2", "Zwangsmittel"), "Bold", 31, rechts=890),
    ok(110, 220, beim("h2", "wirtschaftlichen"), gr=18), ok(110, 275, beim("h2", "öffentlichen"), gr=18),
    ok(110, 330, beim("h2", "Zwangsmittel"), gr=18),
    pl("viel spricht für die freie Rede", 100, 380, "h3", fill=GRUEN, size=30),
    pl("Herr Gerstner kann öffentlich widersprechen", 1110, 120, "h4", fill=LILA, size=30),
    ficon("tabler", "messages", GEX - 230, 470, 100, "h4", fuell=LILA),
])

# ===========================================================================================================================
# I Klausurtipp (Lexi) – Prüfungsmaßstab spezifisches Verfassungsrecht (BVerfGE 18, 85 <92>; BVerfGE 7, 198 <214 f.>)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Prüfungsmaßstab: spezifisches Verfassungsrecht"), ("tipp2", "Klausurtipp · Bedeutung und Reichweite verkannt?")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Urteilsverfassungsbeschwerde:", 200, 200, beim("tipp", "Urteilsverfassungsbeschwerde"), "Bold", 36),
    z("Prüfungsmaßstab nur spezifisches Verfassungsrecht", 200, 250, beim("tipp", "Prüfungsmaßstab"), "Bold", 34),
    zit("BVerfGE 18, 85 <92>", 200, 300, beim("tipp", "Prüfungsmaßstab")),
    *neinz("nicht: Zivilrecht richtig angewendet?", 360, beim("tipp", "Frag"), size=34, x=200),
    linienzug([(130, 440), (1130, 440)], "tipp2", breite=3),
    *okz("sondern: Bedeutung und Reichweite des", 470, "tipp2", "Bold", 34, x=200),
    z("Grundrechts verkannt?", 200, 518, beim("tipp2", "Grundrechts"), "Bold", 34),
    zit("BVerfGE 7, 198 <214 f.>", 200, 568, beim("tipp2", "Grundrechts")),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# J Prüfschema
# ===========================================================================================================================
REIHEN = [("k1", 0, "I. Schutzbereich, Art. 5 Abs. 1 Satz 1 GG", True),
          (beim("k1", "Boykottaufruf"), 1, "auch der Boykottaufruf", False),
          ("k2", 0, "II. Eingriff: Zivilurteil als Akt öffentlicher Gewalt", True),
          ("k3", 0, "III. Rechtfertigung", True),
          (beim("k3", "Schranke"), 1, "Schranke: allgemeines Gesetz, hier § 826 BGB", False),
          ("k4", 1, "Wechselwirkung: Auslegung im Licht der Meinungsfreiheit", False),
          ("k5", 1, "Abwägung aller Umstände", False),
          ("k6", 0, "Maßstab: Ausstrahlungswirkung verkannt?", True)]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfschema: Urteilsverfassungsbeschwerde, Begründetheit"), 110, 90, "sch", 46)]
y = 210
for c, ebene, text, fett in REIHEN:
    x = (130, 200)[ebene]
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 40 if ebene == 0 else 36, rechts=1800))
    y += {0: 88, 1: 80}[ebene]
assert y <= 970, y
folie([("sch", "Prüfschema"), ("k1", "Prüfschema › I. Schutzbereich"), ("k2", "Prüfschema › II. Eingriff"),
       ("k3", "Prüfschema › III. Rechtfertigung"), ("k4", "Prüfschema › III. Wechselwirkung"),
       ("k5", "Prüfschema › III. Abwägung"), ("k6", "Prüfschema › Maßstab")], els_sch)

# ===========================================================================================================================
# K Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Zwischen Privaten wirken die Grundrechte", 0)], [("mittelbar", "a"), (" über die Generalklauseln", 0)],
                 [("und über den Richter.", 0)]], 750, 290, 42, "merke", {"a": beim("merke", "mittelbar")}),
    *markertext([[("Bei einem Beitrag zum Meinungskampf in", 0)], [("einer wesentlichen öffentlichen Frage", 0)],
                 [("spricht die ", 0), ("Vermutung", "b"), (" für die freie Rede.", 0)]], 750, 560, 42, "m2",
                {"b": beim("m2", "Vermutung")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
