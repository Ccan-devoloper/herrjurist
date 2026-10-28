"""Folge 269 · Öffentliche Ordnung: Zwergenweitwurf und Laserdrome (Omega) – Serienstandard Open Peeps (Katzenkönig).
Fall: Freitagnachmittag, Diskothek in Nordrhein-Westfalen. Frau Bredemeier wirbt für Samstag mit einem „Zwergenweitwurf“;
der kleinwüchsige Artist Herr Mehring macht freiwillig mit. Frau Leuschner (Ordnungsamt) untersagt die Veranstaltung.
DARSTELLUNG: Herr Mehring als selbstbewusster Erwachsener (eigene Stimme, Namensschild, eigene Position), kein Wurf im Bild,
nur das Veranstaltungsplakat (Text, Stern); Laserdrome nur als Arena-Symbol, keine Spielszene, keine Waffen.
Szenen laut ../SZENENPLAN.md: A Diskothek (Fall), B Sachverhalt, C Begriff (Zitatkarte BVerfGE 69, 315 [352]), D Bestimmtheit
und Länder, E Zwergenweitwurf 1992 (Wortlautkarte Art. 1 Abs. 1 GG), F Würde trotz Einwilligung?, G Laserdrome (Wortlautkarte
§ 14 Abs. 1 OBG NRW), H Unionsrecht (Wortlautkarten Art. 56 Abs. 1, Art. 52 Abs. 1 AEUV), I EuGH Omega, J Gegenfall,
K Klausurtipp (Lexi), L Schema, M Merksatz (Lexi).
Kein Handlungsgeräusch (siehe ../geraeusche_herkunft.json). Namensschild jeder Figur, solange sie im Bild ist.
Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz als eigene Kopie aus Folge 266 (gemeinsame Dateien
unverändert); neu: fassade(), plakat(), arena(), pm(). Zahlen auf Tafeln, Pillen und Blasen als Ziffern. Wortlautkarten
wörtlich nach gesetze-im-internet.de, recht.nrw.de und dem Cellar des Amts für Veröffentlichungen (EUR-Lex-Dokumente,
Abruf 08.10.2026); Zitatkarte wörtlich nach BVerfGE 69, 315 (DFR)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from ostil import lichtkegel
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_269/"

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
        if n.startswith(("bild:", "ficon:", "bank")) or "/op_269/" in n:
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



def pm(text, y, cue, plus, size=30, x=160, stil="Regular"):
    """Argumentzeile mit (+)/(−) dahinter (für / gegen Herrn Mehrings Sicht), Breitenprüfung wie z()."""
    glyphen(text)
    els = plusminus(text, x, y, cue, plus, size=size, stil=stil)
    r = els[-1]
    assert r.x + r.sprite.width <= 1170, f"Argumentzeile zu breit: {text}"
    return els


# --- eigene Szenenbausteine: Diskothek außen (Fassade, Tür, Plakat), Laserdrome (Arena-Symbol) --------------------------
BODEN_ = (214, 206, 192, 255)
FASSADE = (238, 233, 247, 255)
TUER = (92, 82, 128, 255)
F_O, F_U = 930, 1000                         # Boden (Oberkante, Unterkante)
FH = 500                                     # Erwachsene in den Fallszenen
MH = 370                                     # Herr Mehring in den Fallszenen (74 %)
FU = 942                                     # Unterkante der Figuren in den Fallszenen


def boden(cue):
    s = 2
    im = Image.new("RGBA", (1860 * s, (F_U - F_O) * s))
    dr = ImageDraw.Draw(im)
    dr.rectangle((0, 0, 1860 * s, (F_U - F_O) * s), fill=BODEN_)
    dr.line((0, 0, 1860 * s, 0), fill=INK, width=6 * s)
    for x in range(150, 1860, 300):
        dr.line((x * s, 6 * s, x * s, (F_U - F_O) * s), fill=(176, 166, 150, 255), width=4 * s)
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    return El(im, 30, F_O, cue, "cut", 0.0, None, name="boden")


def fassade(cue):
    """Diskothek von außen: Fassade, Tür, Schild (programmatisch, Palettenflächen)."""
    return [hart(karte(30, 200, 1860, F_O - 200 + 4, cue, fill=FASSADE, rund=6, schatten=0, rand=5, anim="cut")),
            hart(karte(1240, 520, 190, F_O - 520 + 4, cue, fill=TUER, rund=8, schatten=0, rand=5, anim="cut")),
            hart(karte(1400, 720, 18, 18, cue, fill=GELB, rund=9, schatten=0, rand=4, anim="cut")),
            hart(pl("Diskothek", 1335, 440, cue, fill=LILA, size=34, anker="m"))]


def plakat(cue):
    """Veranstaltungsplakat: nur Text und Stern, kein Bild eines Wurfs."""
    x0, y0, w, h = 70, 330, 320, 430
    els = [karte(x0, y0, w, h, cue, fill=GELB, rund=10, schatten=6, rand=5, anim="pop")]
    els.append(ficon("tabler", "star", x0 + w // 2, y0 + 150, 110, cue, fuell=WEISS))
    for t, yy, st, g in [("SAMSTAG", y0 + 185, "ExtraBold", 44), ("„Zwergen-", y0 + 255, "ExtraBold", 40),
                         ("weitwurf“", y0 + 310, "ExtraBold", 40), ("21 Uhr", y0 + 370, "Bold", 32)]:
        f = F(st, g); tw = f.getlength(glyphen(t))
        assert tw <= w - 30, t
        els.append(zeile(t, x0 + (w - tw) / 2, yy, cue, st, g))
    return els


X1, X2 = 1430, 1730                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
MR = 355                                    # Herr Mehring neben der Tafel (74 %)
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"LE": "Frau Leuschner", "BR": "Frau Bredemeier", "ME": "Herr Mehring"}
NFARBE = {"LE": GRUEN, "BR": LILA, "ME": BLAU}
HOEHE = {"LE": FR, "BR": FR, "ME": MR}


def requisit(folge, px=PX):
    """Wechselndes Requisit über den Figuren: folge = [(cue, (set, icon, breite, fuell), pillentext, pillenfarbe)]."""
    els = []
    for i, (c, ic, txt, pf) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else None
        if ic:
            s_, n_, br, fu = ic
            els.append(ficon(s_, n_, px, PU, br, c, fuell=fu, bis=b))
        if txt:
            els.append(pl(txt, px, PY, c, fill=pf, size=28, anker="m", bis=b))
    return els


def stehend(k, x, folge, unten=FB):
    return [*fig(k, x, unten, HOEHE[k], folge), ns(NAME[k], x, unten, folge[0][0], NFARBE[k], d=0.1)]


# ===========================================================================================================================
# A Fall: Freitagnachmittag, vor der Diskothek
# ===========================================================================================================================
MEX, BRX, LEX = 640, 1060, 1650             # Mehring (blickt nach rechts), Bredemeier, Leuschner (blickt nach links)
folie([(NULL, "Fall · Freitagnachmittag, vor einer Diskothek"), ("plakat", "Fall · Das Plakat"),
       ("wurf", "Fall · Die geplante Veranstaltung"), ("amt", "Fall · Das Ordnungsamt kommt"),
       ("le1", "Fall · „Wir untersagen die Veranstaltung“"), ("br1", "Fall · „Er macht freiwillig mit“"),
       ("meh", "Fall · Herr Mehring, Artist"), ("me1", "Fall · „Über meine Würde entscheide ich selbst“"),
       ("frage", "Fall · Die Frage")], [
    hart(boden(NULL)),
    *fassade(NULL),
    hart(pl("Freitagnachmittag: eine Diskothek in NRW", 70, 30, NULL, fill=GELB, size=38, bis="frage")),
    *plakat("plakat"),
    *fig("BR", BRX, FU, FH, [(NULL, "ruhig_r"), ("plakat", "froh")], bis="le1", erst="cut"),
    *fig("BR", BRX, FU, FH, [("le1", "skeptisch_r")], bis="br1", erst="cut"),
    *redet("BR_redet_r", BRX, FU, FH, "br1", "meh"),
    *fig("BR", BRX, FU, FH, [("meh", "froh_r"), ("me1", "ruhig_r"), ("frage", "sorge_r")], erst="cut"),
    hart(ns("Frau Bredemeier, Diskothek", BRX, FU, NULL, LILA)),
    pl("Gäste sollen einen kleinwüchsigen Artisten möglichst weit auf eine Matte werfen", 70, 100, "wurf", fill=WEISS, size=30, bis="amt"),
    pl("Frau Leuschner vom Ordnungsamt bringt eine Verfügung", 70, 100, "amt", fill=WEISS, size=32, bis="frage"),
    *fig("LE", LEX, FU, FH, [("amt", "ernst")], bis="le1", erst="pop"),
    *redet("LE_redet", LEX, FU, FH, "le1", "br1"),
    *fig("LE", LEX, FU, FH, [("br1", "denkt"), ("meh", "ruhig"), ("me1", "denkt"), ("frage", "ernst")], erst="cut"),
    ns("Frau Leuschner, Ordnungsamt", LEX, FU, "amt", GRUEN, d=0.1),
    ficon("tabler", "file-text", 1520, 720, 80, beim("amt", "Verfügung"), fuell=WEISS),
    *fig("ME", MEX, FU, MH, [("meh", "fest_r")], bis="me1", erst="pop"),
    *redet("ME_redet_r", MEX, FU, MH, "me1", "frage"),
    *fig("ME", MEX, FU, MH, [("frage", "ruhig_r")], erst="cut"),
    ns("Herr Mehring, Artist", MEX, FU, "meh", BLAU, d=0.1),
    blase("sprech", 720, 200, "le1", 1330, 330, inhalt=["Frau Bredemeier, wir untersagen", "die Veranstaltung.", "Sie verletzt die Menschenwürde."],
          textsize=32, figur=("LE_redet", LEX, FU, FH), bis="br1"),
    blase("sprech", 640, 210, "br1", 1180, 320, inhalt=["Aber Herr Mehring macht", "freiwillig mit, und er wird", "gut bezahlt."],
          textsize=32, figur=("BR_redet_r", BRX, FU, FH), bis="meh"),
    blase("sprech", 620, 170, "me1", 720, 360, inhalt=["Das ist mein Beruf. Über meine", "Würde entscheide ich selbst."],
          textsize=32, figur=("ME_redet_r", MEX, FU, MH), bis="frage"),
    pl("Darf die Behörde verbieten, obwohl alle einverstanden sind?", 70, 30, "frage", fill=PINK, size=36),
    pl("Generalklausel: Gefahr für die öffentliche Ordnung?", 70, 100, "frage2", fill=PINK, size=32),
])

# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_269(cue, absaetze, frage):
    els = [titel("Sachverhalt", 210, 165, cue, 60)]
    y = 270
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=38, zeilenabstand=1.32)
        els += e; y += 22
    assert y + 70 <= 960, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    els.insert(0, karte(140, 130, 1640, int(y + 6 + 80 - 130), cue, fill=HELL))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_269("sv", [
    "Nordrhein-Westfalen: Frau Bredemeier betreibt eine Diskothek. Für Samstag wirbt sie auf einem Plakat mit einem "
    "„Zwergenweitwurf“: Gäste sollen den kleinwüchsigen Artisten Herrn Mehring möglichst weit auf eine Matte werfen. "
    "Herr Mehring macht freiwillig und gegen Bezahlung mit; es ist sein Beruf.",
    "Frau Leuschner vom Ordnungsamt untersagt die Veranstaltung. Sie stützt sich auf die Generalklausel "
    "(§ 14 Abs. 1 OBG NRW): Die Veranstaltung verletze die Menschenwürde und gefährde die öffentliche Ordnung.",
], "Liegt trotz der Einwilligung eine Gefahr für die öffentliche Ordnung vor?")

# ===========================================================================================================================
# C 1. Begriff: öffentliche Ordnung (Zitatkarte BVerfGE 69, 315 [352])
# ===========================================================================================================================
WD = ["„Unter ‚öffentlicher Ordnung‘ wird die Gesamtheit der ungeschriebenen",
      "Regeln verstanden, deren Befolgung nach den jeweils herrschenden",
      "sozialen und ethischen Anschauungen als unerläßliche Voraussetzung",
      "eines geordneten menschlichen Zusammenlebens innerhalb eines",
      "bestimmten Gebiets angesehen wird.“"]
wd, wd_y = wortlaut(80, 235, 1100, WD, "BVerfGE 69, 315 (352) – Brokdorf, Rn. 77 (Zählung DFR)", "def", marken=[
    (0, "ungeschriebenen", beim("def", "ungeschriebenen")), (1, "herrschenden", beim("def", "herrschenden")),
    (2, "unerläßliche", beim("def", "unerlässlich"))], size=30)
PB = "1. Begriff"
folie([("begriff", f"{PB}: öffentliche Ordnung"), ("def", f"{PB} › Definition des BVerfG"),
       ("abgr", f"{PB} › Abgrenzung: öffentliche Sicherheit"), ("sachsen", f"{PB} › Sachsen: § 4 Nr. 2 SächsPVDG")], rechts_frei([
    *tafel("begriff", "1. Begriff: öffentliche Ordnung", h=720, size=44),
    z("Definition des Bundesverfassungsgerichts:", 110, 175, "def", "Bold", 32),
    *wd,
    z("Abgrenzung: Die öffentliche Sicherheit schützt die", 110, wd_y + 24, "abgr", size=30),
    z("Rechtsordnung und zentrale Rechtsgüter (Folge 213).", 110, wd_y + 64, beim("abgr", "Rechtsordnung"), size=30),
    pl("Sachsen: Definition im Gesetz, § 4 Nr. 2 SächsPVDG", 110, wd_y + 130, "sachsen", fill=GELB, size=30),
    zit("revosax.sachsen.de, Stand 1.7.2026, abgerufen am 8.10.2026", 110, wd_y + 196, beim("sachsen", "Gesetz")),
    *requisit([("begriff", ("tabler", "book", 100, WEISS), "öffentliche Ordnung", WEISS),
               ("def", ("tabler", "users", 110, WEISS), "ungeschriebene Regeln", GELB),
               ("abgr", ("tabler", "shield", 100, BLAU), "öffentliche Sicherheit", WEISS),
               ("sachsen", ("tabler", "map-2", 110, GRUEN), "Sachsen", WEISS)]),
    *stehend("LE", X1, [("begriff", "ruhig"), ("def", "ernst"), ("sachsen", "froh")]),
    *stehend("BR", X2, [("begriff", "skeptisch"), ("abgr", "ruhig")]),
]))
assert wd_y + 196 + 40 <= 900, wd_y

# ===========================================================================================================================
# D Bestimmtheit und Länder
# ===========================================================================================================================
SPL, SPR = 120, 1110
els_d = [karte(60, 50, 1800, 940, "unbest"), titel(glyphen("Zu unbestimmt? Und gilt sie überall?"), 110, 85, "unbest", 46),
         *neinz("Kritik: Der Begriff ist zu unbestimmt.", 170, "unbest", "Bold", 32, x=170),
         *okz("BVerfG: Er hat durch das Polizeirecht einen hinreichend klaren Inhalt erlangt.", 225, "bvg", size=31, x=170, rechts=1820),
         zit("BVerfGE 69, 315 (352), Rn. 77 (Zählung DFR)", 170, 272, beim("bvg", "Polizeirecht"), rechts=1820),
         linienzug([(110, 322), (1810, 322)], "land", breite=3),
         z("Nicht jedes Land kennt das Schutzgut:", 120, 340, "land", "ExtraBold", 34, rechts=1820),
         *neinz("Schleswig-Holstein: 1992 aus dem Landesverwaltungsgesetz gestrichen", 400, "sh", "Bold", 31, x=170, rechts=1820),
         zit("Landesregierung SH, LT-Drs. 16/2115 (6.6.2008), S. 3, 9 – heutiger Wortlaut: Landesportal nicht abrufbar",
             170, 446, beim("sh", "gestrichen"), rechts=1820),
         z("Begründung: Bei unterschiedlichem Freizeitverhalten tauge eine ungeschriebene", 170, 494, "shgrund", size=30, rechts=1820),
         z("Sozialnorm nicht mehr als Ermächtigungsgrundlage.", 170, 534, beim("shgrund", "Sozialnorm"), size=30, rechts=1820),
         z("Die öffentliche Ordnung nennen:", 120, 600, "vier", "ExtraBold", 32, rechts=1820)]
for (land, norm, x, y, w) in [("Nordrhein-Westfalen", "§ 8 Abs. 1 PolG NRW, § 14 Abs. 1 OBG NRW", SPL, 648, "Nordrhein"),
                              ("Niedersachsen", "§§ 11, 2 Nr. 1 NPOG", SPR, 648, "Niedersachsen"),
                              ("Sachsen", "§ 12 Abs. 1, § 4 Nr. 2 SächsPVDG", SPL, 700, "Sachsen"),
                              ("Brandenburg", "§ 10 Abs. 1 BbgPolG", SPR, 700, "Brandenburg")]:
    els_d += okz(f"{land}: {norm}", y, beim("vier", w), size=29, x=x + 50, rechts=(SPR - 20 if x == SPL else 1820))
els_d += [blk(110, 790, 1700, 76, GELB, "dein", [("Prüfe also dein Landesgesetz.", "ExtraBold", 34, INK)]),
          zit("Wortlaut geprüft am 8.10.2026: recht.nrw.de, voris.wolterskluwer-online.de, revosax.sachsen.de, bravors.brandenburg.de",
              110, 890, "dein", rechts=1820)]
folie([("unbest", f"{PB} › Bestimmtheit: Kritik"), ("bvg", f"{PB} › BVerfG: hinreichend klar"),
       ("land", f"{PB} › Länder: Schutzgut nicht überall"), ("sh", f"{PB} › Länder › Schleswig-Holstein: 1992 gestrichen"),
       ("vier", f"{PB} › Länder › NRW, NI, SN, BB nennen sie"), ("dein", f"{PB} › Länder › dein Landesgesetz")], els_d)

# ===========================================================================================================================
# E 2. Klassiker: Zwergenweitwurf 1992 (Wortlautkarte Art. 1 Abs. 1 GG)
# ===========================================================================================================================
W1 = ["„(1) Die Würde des Menschen ist unantastbar. Sie zu achten und",
      "zu schützen ist Verpflichtung aller staatlichen Gewalt.“"]
PZ = "2. Klassiker: Zwergenweitwurf"
folie([("zw", f"{PZ}"), ("vorbild", f"{PZ} › Rheinland-Pfalz 1992"), ("vgn", f"{PZ} › VG Neustadt: Gewerberecht"),
       ("wert", f"{PZ} › Maßstab: Wertordnung des Grundgesetzes"), ("art1", f"{PZ} › Art. 1 Abs. 1 GG")], rechts_frei([
    *tafel("zw", "2. Klassiker: Zwergenweitwurf", h=840, size=46),
    z("1992: Eine Behörde in Rheinland-Pfalz untersagt", 110, 175, "vorbild", "Bold", 32),
    z("eine solche Veranstaltung.", 110, 217, beim("vorbild", "Veranstaltung"), "Bold", 32),
    z("VG Neustadt billigt das im Eilverfahren – Gewerberecht:", 110, 285, "vgn", size=31),
    z("Schaustellungen nicht gegen die guten Sitten", 110, 327, beim("vgn", "Schaustellungen"), "Bold", 31),
    zit("§ 33a Abs. 2 Nr. 2 GewO; VG Neustadt, Beschl. v. 21.5.1992 – 7 L 1271/92,", 110, 373, beim("vgn", "Sitten")),
    zit("NVwZ 1993, 98 (Volltext nicht online; nach Sekundärquellen)", 110, 407, beim("vgn", "Sitten")),
    blk(110, 465, 1040, 76, BLAU, "wert", [("Maßstab: die Wertordnung des Grundgesetzes", "ExtraBold", 32, INK)]),
    *wortlaut(80, 580, 1100, W1, "Art. 1 Abs. 1 GG", "art1", marken=[(0, "unantastbar", beim("art1", "unantastbar")),
              (1, "zu schützen", beim("art1", "schützen"))], size=32)[0],
    *requisit([("zw", ("tabler", "file-text", 90, GELB), "Klassiker 1992", WEISS),
               ("vgn", ("tabler", "building-bank", 110, BLAU), "VG Neustadt", WEISS),
               ("wert", ("tabler", "book", 100, WEISS), "Grundgesetz", WEISS),
               ("art1", ("tabler", "heart", 100, ROT), "Menschenwürde", HELLROT)]),
    *stehend("ME", X1, [("zw", "ruhig"), ("vgn", "ernst"), ("art1", "fest")]),
    *stehend("LE", X2, [("zw", "ruhig"), ("wert", "ernst")]),
]))

# ===========================================================================================================================
# F Würde trotz Einwilligung? Argumente beider Seiten
# ===========================================================================================================================
folie([("pro", f"{PZ} › Für Herrn Mehring: freie Entscheidung"), ("subj", f"{PZ} › Würde als Selbstbestimmung"),
       ("contra", f"{PZ} › VG Neustadt: bloßes Objekt"), ("verz", f"{PZ} › kein Verzicht auf die Würde"),
       ("beruf", f"{PZ} › Berufsfreiheit"), ("erg1", f"{PZ} › Ergebnis: öffentliche Ordnung gefährdet"),
       ("un", f"{PZ} › UN-Menschenrechtsausschuss")], rechts_frei([
    *tafel("pro", "Würde trotz Einwilligung?", h=880, size=46),
    z("Für Herrn Mehring:", 110, 172, "pro", "ExtraBold", 32),
    *pm("freie Entscheidung, sein Beruf – Art. 12 Abs. 1 GG", 222, beim("pro", "frei"), True),
    *pm("Würde heißt gerade, selbst zu bestimmen", 266, "subj", True),
    zit("vgl. GA Stix-Hackl, Schlussanträge C-36/02, Nr. 78", 160, 306, beim("subj", "selbst")),
    z("VG Neustadt:", 110, 354, "contra", "ExtraBold", 32),
    *pm("wie ein Sportgerät geworfen: bloßes Objekt", 402, beim("contra", "Sportgerät"), False),
    *pm("herabsetzend schon die Bezeichnung „Zwerg“", 446, "name", False),
    *pm("kein wirksamer Verzicht auf die Würde", 490, "verz", False),
    *pm("der Staat muss sie schützen", 534, beim("verz", "Staat"), False),
    *pm("Berufsfreiheit nur ohne Verstoß gegen die guten Sitten", 578, "beruf", False),
    blk(110, 640, 1040, 112, GRUEN, "erg1", [("Unser Fall: öffentliche Ordnung gefährdet –", "ExtraBold", 31, INK),
                                            ("trotz der Einwilligung", "ExtraBold", 31, INK)]),
    z("UN-Menschenrechtsausschuss: Verbot in Frankreich", 110, 772, "un", size=30),
    z("keine Diskriminierung (2002)", 110, 810, beim("un", "Diskriminierung"), size=30),
    zit("CCPR/C/75/D/854/1999, zitiert nach GA Stix-Hackl, Nr. 94", 110, 852, beim("un", "Diskriminierung")),
    *requisit([("pro", ("tabler", "user-check", 100, BLAU), "freie Entscheidung", WEISS),
               ("contra", ("tabler", "building-bank", 110, BLAU), "VG Neustadt", WEISS),
               ("verz", ("tabler", "heart", 100, ROT), "Würde: unverfügbar", HELLROT),
               ("beruf", ("tabler", "briefcase", 100, WEISS), "Art. 12 GG", WEISS),
               ("erg1", ("tabler", "shield", 100, GRUEN), "Gefahr (+)", GRUEN),
               ("un", ("tabler", "world", 100, BLAU), "UN", WEISS)]),
    *stehend("ME", X1, [("pro", "fest"), ("contra", "ernst"), ("verz", "still"), ("erg1", "ruhig")]),
    *stehend("BR", X2, [("pro", "froh"), ("contra", "sorge"), ("erg1", "muede")]),
]))

# ===========================================================================================================================
# G 3. Klassiker: Laserdrome (Wortlautkarte § 14 Abs. 1 OBG NRW)
# ===========================================================================================================================
W14 = ["„(1) Die Ordnungsbehörden können die notwendigen Maßnahmen treffen,",
       "um eine im einzelnen Falle bestehende Gefahr für die öffentliche",
       "Sicherheit oder Ordnung (Gefahr) abzuwehren.“"]
PL = "3. Klassiker: Laserdrome (Omega)"
folie([("ld", f"{PL}"), ("bonn", f"{PL} › Bonn 1994"), ("verf", f"{PL} › Verfügung: § 14 Abs. 1 OBG NRW"),
       ("bverwg", f"{PL} › BVerwG: Menschenwürde verletzt")], rechts_frei([
    *tafel("ld", "3. Klassiker: das Laserdrome", h=860, size=46),
    z("Bonn 1994: Spieler zielen mit Laserzielgeräten", 110, 175, "bonn", "Bold", 32),
    z("auf Sensoren an den Westen anderer Spieler.", 110, 217, beim("bonn", "Sensoren"), "Bold", 32),
    zit("EuGH, Urt. v. 14.10.2004 – C-36/02 (Omega), Rn. 3, 5", 110, 263, beim("bonn", "Westen")),
    z("Verfügung der Stadt: kein „spielerisches Töten“ von Menschen", 110, 320, "verf", size=31),
    *wortlaut(80, 372, 1100, W14, "§ 14 Abs. 1 OBG NRW (heute wortgleich; Omega, Rn. 6)", beim("verf", "Generalklausel"),
              marken=[(1, "Gefahr für die öffentliche", beim("verf", "Gefahr")), (2, "Ordnung", beim("verf", "Ordnung"))],
              size=30)[0],
    *okz("BVerwG: Menschenwürde verletzt –", 652, "bverwg", "Bold", 31, x=160),
    z("im Unterhaltungsspiel nicht abdingbar", 160, 698, beim("bverwg", "Unterhaltungsspiel"), size=31),
    zit("Vorlagebeschluss vom 24.10.2001, wiedergegeben in Omega, Rn. 11 f.", 160, 744, beim("bverwg", "abbedingen")),
    *requisit([("ld", ("tabler", "building-arch", 130, LILA), "Laserdrome", WEISS),
               ("bonn", ("tabler", "shirt", 100, WEISS), "Sensoren an Westen", WEISS),
               ("verf", ("tabler", "file-text", 90, WEISS), "Verfügung", WEISS),
               ("bverwg", ("tabler", "building-bank", 110, BLAU), "BVerwG", WEISS)]),
    *stehend("LE", X1, [("ld", "ruhig"), ("verf", "ernst"), ("bverwg", "denkt")]),
    *stehend("BR", X2, [("ld", "froh"), ("bonn", "skeptisch"), ("bverwg", "sorge")]),
]))

# ===========================================================================================================================
# H Unionsrecht: Dienstleistungsfreiheit (Wortlautkarten Art. 56 Abs. 1, Art. 52 Abs. 1 AEUV)
# ===========================================================================================================================
W56 = ["„Die Beschränkungen des freien Dienstleistungsverkehrs innerhalb",
       "der Union für Angehörige der Mitgliedstaaten, die in einem anderen",
       "Mitgliedstaat als demjenigen des Leistungsempfängers ansässig sind,",
       "sind nach Maßgabe der folgenden Bestimmungen verboten.“"]
w56, w56_y = wortlaut(80, 260, 1100, W56, "Art. 56 Abs. 1 AEUV (ex-Art. 49 EG)", "art56", marken=[
    (0, "Beschränkungen des freien Dienstleistungsverkehrs", beim("art56", "Beschränkungen")), (3, "verboten", beim("art56", "verboten"))], size=30)
W52 = ["„(1) Dieses Kapitel … beeinträchtigen nicht die Anwendbarkeit der",
       "Rechts- und Verwaltungsvorschriften, die … aus Gründen der öffentlichen",
       "Ordnung, Sicherheit oder Gesundheit gerechtfertigt sind.“"]
w52, w52_y = wortlaut(80, w56_y + 20, 1100, W52, "Art. 52 Abs. 1 i. V. m. Art. 62 AEUV (Omega, Rn. 28 f.)", "art52", marken=[
    (1, "aus Gründen der öffentlichen", beim("art52", "Gründen")), (2, "Ordnung", beim("art52", "Ordnung"))], size=30)
PU_ = f"{PL} › Unionsrecht"
folie([("eu", f"{PU_}"), ("art56", f"{PU_} › Art. 56 AEUV: Dienstleistungsfreiheit"),
       ("art52", f"{PU_} › Rechtfertigung: öffentliche Ordnung")], rechts_frei([
    *tafel("eu", "Unionsrecht: Dienstleistungsfreiheit", h=860, size=44),
    z("Ausrüstung und Spielvariante: von einer britischen Firma", 110, 175, "eu", "Bold", 31),
    zit("Omega, Rn. 3, 25", 110, 219, beim("eu", "britischen")),
    *w56, *w52,
    *requisit([("eu", ("tabler", "world", 110, BLAU), "britische Firma", WEISS),
               ("art56", ("tabler", "arrows-left-right", 100, WEISS), "Art. 56 AEUV", GELB),
               ("art52", ("tabler", "scale", 110, WEISS), "Rechtfertigung?", WEISS)]),
    *stehend("BR", X1, [("eu", "froh"), ("art52", "skeptisch")]),
    *stehend("LE", X2, [("eu", "denkt"), ("art56", "ruhig"), ("art52", "ernst")]),
]))
assert w52_y <= 900, w52_y

# ===========================================================================================================================
# I EuGH Omega: Ergebnis
# ===========================================================================================================================
folie([("eng", f"{PU_} › EuGH: öffentliche Ordnung eng"), ("wuerde", f"{PU_} › Menschenwürde als Rechtsgrundsatz"),
       ("gemein", f"{PU_} › keine gemeinsame Auffassung nötig"), ("vh", f"{PU_} › verhältnismäßig"),
       ("tenor", f"{PL} › Ergebnis")], rechts_frei([
    *tafel("eng", "EuGH, Omega (14.10.2004)", h=860, size=46),
    z("Öffentliche Ordnung eng: tatsächliche und hinreichend", 110, 175, "eng", "Bold", 31),
    z("schwere Gefährdung, die ein Grundinteresse der", 110, 215, beim("eng", "tatsächliche"), "Bold", 31),
    z("Gesellschaft berührt", 110, 255, beim("eng", "Grundinteresse"), "Bold", 31),
    zit("C-36/02, Rn. 30", 110, 300, beim("eng", "berührt")),
    *okz("Menschenwürde: allgemeiner Rechtsgrundsatz", 352, "wuerde", size=31, x=160),
    *okz("ihr Schutz: ein berechtigtes Interesse", 398, beim("wuerde", "Schutz"), size=31, x=160),
    zit("Rn. 34 f.", 160, 444, beim("wuerde", "berechtigtes")),
    *okz("keine gemeinsame Auffassung aller Mitgliedstaaten nötig,", 492, "gemein", size=31, x=160),
    z("wie ein Grundrecht zu schützen ist", 160, 534, beim("gemein", "Grundrecht"), size=31),
    zit("Rn. 37 f.", 160, 578, beim("gemein", "schützen")),
    *okz("verhältnismäßig: nur die Variante mit menschlichen Zielen", 626, "vh", size=31, x=160),
    zit("Rn. 39", 160, 672, beim("vh", "Zielen")),
    blk(110, 722, 1040, 112, GRUEN, "tenor", [("Ergebnis: Das Unionsrecht steht", "ExtraBold", 32, INK),
                                             ("dem Verbot nicht entgegen.", "ExtraBold", 32, INK)]),
    zit("Rn. 41 und Tenor", 110, 846, beim("tenor", "entgegen")),
    *requisit([("eng", ("tabler", "building-bank", 110, BLAU), "EuGH", WEISS),
               ("wuerde", ("tabler", "heart", 100, ROT), "Menschenwürde", HELLROT),
               ("gemein", ("tabler", "map-2", 110, GRUEN), "Mitgliedstaaten", WEISS),
               ("vh", ("tabler", "scale", 110, WEISS), "verhältnismäßig", WEISS),
               ("tenor", ("tabler", "shield", 100, GRUEN), "Verbot hält", GRUEN)]),
    *stehend("LE", X1, [("eng", "denkt"), ("wuerde", "ernst"), ("tenor", "froh")]),
    *stehend("BR", X2, [("eng", "skeptisch"), ("gemein", "ruhig"), ("tenor", "muede")]),
]))

# ===========================================================================================================================
# J Gegenfall: nur feste Sensoren in der Anlage (Arena-Symbol, keine Spielszene)
# ===========================================================================================================================
folie([("gegen", "Gegenfall · nur feste Sensoren"), (beim("gegen", "erfasste"), "Gegenfall · von der Verfügung nicht erfasst")], [
    hart(boden("gegen")),
    hart(karte(30, 200, 1860, F_O - 200 + 4, "gegen", fill=LILAHELL, rund=6, schatten=0, rand=5, anim="cut")),
    hart(ficon("tabler", "building-arch", 300, 720, 300, "gegen", fuell=LILA, anim="cut")),
    hart(pl("Laserdrome", 300, 760, "gegen", fill=WEISS, size=30, anker="m")),
    *[hart(ficon("tabler", "target", x, 560, 110, "gegen", fuell=WEISS, anim="cut")) for x in (640, 860, 1080)],
    pl("Gegenfall: Die Spieler zielen nur auf feste Sensoren in der Anlage", 70, 30, "gegen", fill=GELB, size=34),
    ok(840, 700, beim("gegen", "erfasste"), gr=40),
    pl("Die Verfügung erfasst das gar nicht.", 70, 100, beim("gegen", "erfasste"), fill=GRUEN, size=34),
    *fig("BR", 1500, FU, FH, [("gegen", "skeptisch"), (beim("gegen", "erfasste"), "froh")], erst="pop"),
    ns("Frau Bredemeier", 1500, FU, "gegen", LILA, d=0.1),
])

# ===========================================================================================================================
# K Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · erst die Spezialgesetze"), ("tipp1", "Klausurtipp · die Regel konkret benennen"),
       ("tipp2", "Klausurtipp · grenzüberschreitend: Art. 56 AEUV")], [
    *tafel("tipp", "Klausurtipp: öffentliche Ordnung", fill=HELL, h=640, size=46),
    warnung_i(150, 225, "tipp", gr=26),
    z("1. Erst die Spezialgesetze prüfen – bei", 200, 200, "tipp", "Bold", 34),
    z("Schaustellungen von Personen: § 33a GewO", 200, 248, beim("tipp", "Paragraf"), size=32),
    z("2. Die ungeschriebene Regel konkret benennen", 200, 340, "tipp1", "Bold", 34),
    z("und im Grundgesetz verankern: Menschenwürde", 200, 388, beim("tipp1", "verankere"), size=32),
    z("3. Grenzüberschreitende Dienstleistung?", 200, 480, "tipp2", "Bold", 34),
    z("Dann an Art. 56 AEUV denken", 200, 528, beim("tipp2", "Artikel"), size=32),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# L Schema
# ===========================================================================================================================
REIHEN = [("s1", "1. Ermächtigungsgrundlage", "Spezialgesetz vor Generalklausel; kennt dein Land die öffentliche Ordnung?"),
          ("s2", "2. Gefahr für die öffentliche Ordnung", "ungeschriebene Regel, gemessen am Grundgesetz;"),
          ("s3", "3. Grenzüberschreitende Dienstleistung", "Art. 56 AEUV; Rechtfertigung aus Gründen der öffentlichen Ordnung"),
          ("s4", "4. Ermessen und Verhältnismäßigkeit", None)]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Schema: öffentliche Ordnung"), 110, 85, "sch", 50),
           zit("z. B. § 14 Abs. 1 OBG NRW, § 8 Abs. 1 PolG NRW – in deinem Land ggf. andere Nummer", 110, 168, beim("sch", "Schema"), rechts=1820)]
y = 230
for c, kopf, unter in REIHEN:
    els_sch.append(z(kopf, 130, y, c, "ExtraBold", 38, rechts=1820))
    if unter:
        els_sch.append(z(unter, 180, y + 50, beim(c, {"s1": "Spezialgesetz", "s2": "ungeschriebene", "s3": "Artikel"}[c]), size=32, rechts=1820))
    if c == "s2":
        els_sch.append(z("Einwilligung hilft bei der Menschenwürde nach der Rechtsprechung nicht", 180, y + 92,
                         beim("s2", "Menschenwürde"), size=32, rechts=1820))
        y += 42
    y += 150
assert y <= 990, y
folie([("sch", "Schema"), ("s1", "Schema › 1. Ermächtigungsgrundlage"), ("s2", "Schema › 2. Gefahr für die öffentliche Ordnung"),
       ("s3", "Schema › 3. Grenzüberschreitende Dienstleistung"), ("s4", "Schema › 4. Ermessen und Verhältnismäßigkeit")], els_sch)

# ===========================================================================================================================
# M Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Öffentliche Ordnung sind ", 0), ("ungeschriebene", "a")],
                 [("Regeln, gemessen am ", 0), ("Grundgesetz", "b"), (".", 0)]], 750, 300, 48, "merke",
                {"a": beim("merke", "ungeschriebene"), "b": beim("merke", "Grundgesetz")}),
    *markertext([[("Die ", 0), ("Menschenwürde", "c"), (" schützt sie nach der", 0)],
                 [("Rechtsprechung auch gegen die ", 0), ("Einwilligung", "d"), (",", 0)],
                 [("und das ", 0), ("Unionsrecht", "e"), (" lässt dieses", 0)],
                 [("Schutzniveau zu.", 0)]], 750, 500, 44, "m2",
                {"c": beim("m2", "Menschenwürde"), "d": beim("m2", "Einwilligung"), "e": beim("m2", "Unionsrecht")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
