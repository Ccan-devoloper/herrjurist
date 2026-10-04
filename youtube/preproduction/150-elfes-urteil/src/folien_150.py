"""Folge 150 · Elfes-Urteil: Allgemeine Handlungsfreiheit nach Art. 2 I GG – Serienstandard Open Peeps (Katzenkönig).
Moderner Einstieg mit fiktiven Figuren (Torben, beantragt einen Reisepass; Herr Haupt, Sachbearbeiter der Passbehörde),
danach der echte Fall sachlich: BVerfG, Urt. v. 16.1.1957 – 1 BvR 253/56, BVerfGE 6, 32 (Seiten der amtlichen Sammlung nach
DFR). NEUTRAL: Wilhelm Elfes tritt nicht als Figur auf, kein Porträt, keine Parteinamen oder Logos; der Grund der
Passversagung nur wie im Volltext (<33>), ohne Bewertung; nur neutrale Icons (Rathaus, Mikrofon, Reisepass, Gericht).
Szenen laut ../SZENENPLAN.md. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/requisit/stehend/
paar/spricht_neben als eigene Kopie aus Folge 146 (gemeinsame Dateien unverändert); neu: schalter(), reisepass(), buehne().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from ostil import titel, karte, pille
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_150/"

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
        if n.startswith(("bild:", "ficon:", "bank")) or "/op_150/" in n:
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
NAME = {"TB": "Torben", "HP": "Herr Haupt"}
NFARBE = {"TB": GRUEN, "HP": BLAUHELL}


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



def schalter(x0, x1, cue, oben=BODEN - 250):
    """Behördenschalter aus Grundformen: Holzplatte und helle Front bis zum Boden (verdeckt die Beine dahinter)."""
    w, h = x1 - x0, BODEN - oben
    im, dr, s = _flaeche(w, h)
    o = 6 * s
    dr.rectangle((o, o + 30 * s, o + w * s, o + h * s), fill=BLAUHELL, outline=INK, width=5 * s)
    for k in (1, 2):
        xx = o + int(w * k / 3) * s
        dr.line((xx, o + 50 * s, xx, o + (h - 20) * s), fill=INK, width=3 * s)
    dr.rounded_rectangle((o - 14 * s, o, o + (w + 14) * s, o + 34 * s), 8 * s, fill=HOLZ, outline=INK, width=5 * s)
    im = im.resize((w + 12, h + 12), Image.LANCZOS)
    return hart(El(im, x0 - 6, oben - 6, cue, "cut", 0.0, None, name="schalter"))


_PASS = {}


def reisepass(cx, unten, breite, cue, anim="pop", bis=None, d=0.0):
    """Reisepass aus Grundformen: rotes Heft mit Tuschekontur, Schriftzug REISEPASS und Globus (Tabler world, MIT)."""
    if breite not in _PASS:
        w, h = breite, int(breite * 1.38)
        im, dr, s = _flaeche(w, h)
        o = 6 * s
        dr.rounded_rectangle((o, o, o + w * s, o + h * s), 12 * s, fill=ROT, outline=INK, width=5 * s)
        dr.line((o + 16 * s, o + 8 * s, o + 16 * s, o + (h - 8) * s), fill=INK, width=3 * s)
        im = im.resize((w + 12, h + 12), Image.LANCZOS)
        gl = ficon("tabler", "world", 0, 0, int(w * 0.48), "_", fuell=GELB).sprite
        im.alpha_composite(gl, (int((w + 12 - gl.width) / 2 + 4), int(h * 0.22)))
        f = F("ExtraBold", max(12, int(w * 0.13)))
        t = "REISEPASS"
        tw = f.getlength(t)
        ImageDraw.Draw(im).text(((w + 12 - tw) / 2 + 4, int(h * 0.68)), t, font=f, fill=WEISS)
        _PASS[breite] = im
    im = _PASS[breite]
    return El(im, cx - im.width / 2, unten - im.height, cue, anim, d, bis, name="ficon:reisepass")


# ===========================================================================================================================
# A1 Fall: Torben bei der Passbehörde (fiktiv; § 7 Abs. 1 Nr. 1 PassG)
# ===========================================================================================================================
HPX, TBX, TBX0 = 660, 1270, 1640            # Herr Haupt hinter dem Schalter, Torben am Schalter (kommt von TBX0)
SX0, SX1 = 400, 960                         # Schalter
SOBEN = BODEN - 250


def schild(cue):
    return [hart(ficon("tabler", "building", 120, 132, 80, cue, fuell=WEISS, anim="cut")),
            hart(pl("Passbehörde", 180, 52, cue, fill=GELB, size=40, anim="cut"))]


def buehne(cue, haupt, stempel_cue=None, schon=False):
    """Schauplatz Passbehörde: Boden, Schild, Herr Haupt (haupt = Elemente, hinter dem Schalter), Schalter, Antrag."""
    els = [boden(cue), *schild(cue), *haupt, schalter(SX0, SX1, cue, SOBEN)]
    return els


A_HAUPT = [*fig("HP", HPX, BODEN, FH, [(NULL, "ruhig_r")], bis="h1", erst="cut"),
           *redet("HP_redet_r", HPX, BODEN, FH, "h1", "o1"),
           *fig("HP", HPX, BODEN, FH, [("o1", "denkt_r")], erst="cut")]
folie([(NULL, "Fall · Torben bei der Passbehörde"), ("h1", "Fall · Der Pass wird versagt"),
       ("o1", "Fall · Welches Grundrecht?")], [
    *buehne(NULL, A_HAUPT),
    hart(ns("Herr Haupt", HPX, BODEN, NULL, BLAUHELL)),
    # Torben steht zuerst rechts, denkt an die Reise, geht dann zum Schalter (Schritte)
    peep_voll("TB_froh", TBX0, BODEN, FH, NULL, anim="cut", bis="antrag"),
    bis_(hart(ns("Torben", TBX0, BODEN, NULL, GRUEN)), "antrag"),
    ficon("tabler", "plane-departure", 1640, 300, 130, beim("fall", "Konferenz"), fuell=BLAUHELL, bis="o1"),
    pl("Konferenz im Ausland", 1640, 120, beim("fall", "Konferenz"), fill=WEISS, size=30, anker="m", bis="o1"),
    szene(bewegt(peep_voll("TB_ruhig", TBX, BODEN, FH, "antrag", anim="cut", bis="h1"), "antrag", ("antrag", 1.2),
                 TBX0 - TBX, 0), "150schritte*", 0.8, 0.05),
    bewegt(ns("Torben", TBX, BODEN, "antrag", GRUEN, anim="cut"), "antrag", ("antrag", 1.2), TBX0 - TBX, 0),
    *fig("TB", TBX, BODEN, FH, [("h1", "denkt"), (beim("h1", "gefährden"), "sorge")], bis="o1", erst="cut"),
    *redet("TB_redet", TBX, BODEN, FH, "o1", "frage0"),
    ficon("tabler", "file-text", 860, SOBEN + 2, 80, beim("antrag", "beantragt"), fuell=WEISS),
    pl("Antrag: neuer Reisepass", 70, 400, beim("antrag", "Reisepass"), fill=WEISS, size=30),
    szene(ficon("streamline-freehand", "office-stamp-document", 860, SOBEN - 60, 90, beim("h1", "versagen"),
                fuell=HELLROT), "150stempel*", 0.9, 0.08),
    reisepass(520, SOBEN + 2, 74, beim("h1", "Pass")),
    pl("Pass versagt", 70, 330, beim("h1", "versagen"), fill=HELLROT, size=30),
    blase("sprech", 780, 290, "h1", 1060, 250, inhalt=["Den Pass müssen wir versagen.", "Bestimmte Tatsachen begründen",
                                                    "die Annahme, dass Sie erhebliche",
                                                    "Belange der Bundesrepublik gefährden."], textsize=29,
          figur=("HP_redet_r", HPX, BODEN, FH), bis="o1"),
    pl("§ 7 Abs. 1 Nr. 1 PassG", 70, 470, beim("h1", "Tatsachen"), fill=HELLROT, size=30),
    blase("sprech", 660, 200, "o1", 1500, 250, inhalt=["Ich will doch nur reisen.", "Welches Grundrecht schützt das?"],
          textsize=31, figur=("TB_redet", TBX, BODEN, FH), bis="frage0"),
])

# ===========================================================================================================================
# A2 Die Frage
# ===========================================================================================================================
folie([("frage0", "Die Frage · Schützt das Grundgesetz die Ausreise?"), ("klassiker", "Die Frage · Das Elfes-Urteil")], [
    *tafel("frage0", "Torben will ausreisen"),
    z("Die Passbehörde versagt den Reisepass.", 110, 190, "frage0", "Bold", 36),
    pl("Schützt das Grundgesetz die Ausreise?", 110, 270, beim("frage0", "Schützt"), fill=PINK, size=36),
    pl("Woran wird die Versagung gemessen?", 110, 365, beim("frage0", "woran"), fill=PINK, size=36),
    blk(110, 490, 1040, 120, GELB, "klassiker", [("Die Antwort gibt das Elfes-Urteil", "ExtraBold", 34, INK),
                                              ("des Bundesverfassungsgerichts", "ExtraBold", 34, INK)]),
    zit("BVerfG, Urt. v. 16.1.1957 – 1 BvR 253/56, BVerfGE 6, 32", 110, 625, "klassiker"),
    *requisit([("frage0", ("tabler", "plane-departure", 120, BLAUHELL), "Ausreise?", WEISS),
               ("klassiker", ("tabler", "scale", 110, GELB), "Elfes-Urteil", GELB)]),
    *paar("TB", [("frage0", "denkt")], "HP", [("frage0", "ruhig"), ("klassiker", "denkt")]),
])

# ===========================================================================================================================
# B1 Der echte Fall: Wilhelm Elfes, Passantrag 1953 (BVerfGE 6, 32 <33>) – ohne Figuren, neutrale Icons
# ===========================================================================================================================
folie([("elfes", "Der echte Fall · Wilhelm Elfes"), ("pass", "Der echte Fall · Der Passantrag 1953")], [
    boden("elfes"),
    pl("Wilhelm Elfes", 70, 40, "elfes", fill=GELB, size=34),
    pl("nach dem Krieg Oberbürgermeister von Mönchengladbach", 70, 118, beim("elfes", "Oberbürgermeister"), fill=WEISS, size=30),
    pl("später dort Oberstadtdirektor", 70, 188, beim("elfes", "Oberstadtdirektor"), fill=WEISS, size=30),
    pl("öffentliche Kritik an der Politik der Bundesregierung, auch im Ausland", 70, 258, "kritik", fill=HELL, size=30),
    pl("vor allem zur Wehrpolitik und zur Frage der Wiedervereinigung", 70, 328, beim("kritik", "Wehrpolitik"),
       fill=HELL, size=30),
    ficon("tabler", "building-community", 330, BODEN, 250, "elfes", fuell=WEISS),
    ficon("tabler", "microphone-2", 880, BODEN, 150, "kritik", fuell=WEISS),
    ficon("tabler", "world", 1060, BODEN, 150, beim("kritik", "Ausland"), fuell=BLAUHELL),
    reisepass(1560, BODEN, 170, "pass"),
    pl("1953: Verlängerung des Reisepasses", 1500, 400, beim("pass", "Reisepass"), fill=WEISS, size=30, anker="m"),
    nein(1700, BODEN - 200, "versagt", gr=40),
    pl("abgelehnt, ohne nähere Begründung", 1500, 470, beim("versagt", "Begründung"), fill=HELLROT, size=30, anker="m"),
    pl("gestützt auf § 7 PaßG", 1500, 540, beim("versagt", "Paragraf"), fill=HELLROT, size=30, anker="m"),
])

# ===========================================================================================================================
# B2 § 7 Abs. 1 Buchst. a PaßG 1952 (Wortlaut nach <34>), BVerwG, Verfassungsbeschwerde (<33 f.>)
# ===========================================================================================================================
W7A = ["„Der Paß ist zu versagen, wenn Tatsachen die Annahme",
       "rechtfertigen, daß a) der Antragsteller als Inhaber eines",
       "Passes die innere oder die äußere Sicherheit oder sonstige",
       "erhebliche Belange der Bundesrepublik Deutschland oder",
       "eines deutschen Landes gefährdet; …“"]
w7a, w7a_y = wortlaut(80, 165, 1100, W7A, "§ 7 Abs. 1 Buchst. a PaßG 1952, zitiert nach BVerfGE 6, 32 <34>", "norm", marken=[
    (0, "Tatsachen", beim("norm", "Tatsachen")), (2, "Sicherheit", beim("norm", "Sicherheit")),
    (2, "sonstige", beim("norm", "sonstige")), (3, "erhebliche Belange", beim("norm", "sonstige"))], size=31)
folie([("norm", "Der echte Fall · § 7 Abs. 1 Buchst. a PaßG"), ("wien", "Der echte Fall · Bundesverwaltungsgericht"),
       ("vb", "Der echte Fall · Verfassungsbeschwerde"), ("frage", "Der echte Fall · Die Frage")], [
    *tafel("norm", "Das Passgesetz von 1952"),
    *w7a,
    z("Bundesverwaltungsgericht: Teilnahme am Friedenskongress", 110, w7a_y + 26, "wien", "Bold", 32),
    z("in Wien und eine dort verlesene Erklärung", 110, w7a_y + 70, beim("wien", "Erklärung"), "Bold", 32),
    zit("BVerfGE 6, 32 <33>", 110, w7a_y + 116, beim("wien", "Erklärung")),
    blk(110, w7a_y + 165, 1040, 80, GELB, "vb", [("erfolglos in allen Instanzen: Verfassungsbeschwerde", "ExtraBold", 33, INK)]),
    pl("Verletzt die Passversagung ein Grundrecht?", 110, w7a_y + 270, "frage", fill=PINK, size=34),
    *requisit([("norm", ("tabler", "book", 110, WEISS), "§ 7 PaßG 1952", WEISS),
               ("wien", ("tabler", "gavel", 130, HOLZ), "Bundesverwaltungsgericht", WEISS),
               ("vb", ("tabler", "building-bank", 140, WEISS), "Verfassungsbeschwerde", GELB),
               ("frage", ("tabler", "scale", 120, PINK), "Grundrecht verletzt?", PINK)], pu=640, py=260),
])


# ===========================================================================================================================
# C Sachverhalt
# ===========================================================================================================================
def sachverhalt_150(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=33, zeilenabstand=1.28)
        els += e; y += 16
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_150("sv", [
    "Wilhelm Elfes ist nach dem Krieg Oberbürgermeister von Mönchengladbach, später dort Oberstadtdirektor. Er "
    "kritisiert öffentlich, auch im Ausland, die Politik der Bundesregierung, vor allem zur Wehrpolitik und zur Frage "
    "der Wiedervereinigung. 1953 beantragt er die Verlängerung seines Reisepasses.",
    "Die Passbehörde lehnt am 6. Juni 1953 ohne nähere Begründung ab, gestützt auf § 7 Abs. 1 Buchst. a PaßG: Der Pass "
    "ist zu versagen, wenn Tatsachen die Annahme rechtfertigen, der Antragsteller gefährde die innere oder äußere "
    "Sicherheit oder sonstige erhebliche Belange der Bundesrepublik. Das Bundesverwaltungsgericht stützt die Versagung "
    "auf seine Teilnahme an einem Friedenskongress in Wien im Dezember 1952 und eine dort verlesene Erklärung. Elfes "
    "bleibt in allen Instanzen erfolglos und erhebt Verfassungsbeschwerde.",
], "Verletzt die Passversagung Elfes in seinen Grundrechten?")

# ===========================================================================================================================
# D I. Art. 11 GG (Wortlautkarte): Ausreise nicht erfasst (<34–36>; Leitsatz 1)
# ===========================================================================================================================
PI = "I. Freizügigkeit, Art. 11 GG"
W11 = ["„(1) Alle Deutschen genießen Freizügigkeit im ganzen", "Bundesgebiet.“"]
w11, w11_y = wortlaut(80, 278, 1100, W11, "Art. 11 Abs. 1 GG", "a11", marken=[
    (0, "Freizügigkeit", beim("a11", "Freizügigkeit")), (0, "im ganzen", beim("a11", "ganzen")),
    (1, "Bundesgebiet", beim("a11", "ganzen"))], size=34)
folie([("urteil", "I. Freizügigkeit · BVerfG, 16.1.1957"), ("a11", f"{PI} · Wortlaut"), ("wortl", f"{PI} › nicht die Ausreise"),
       ("schr", f"{PI} › Schranken des Abs. 2"), ("nein11", f"{PI} › Ausreise nicht erfasst (−)")], [
    *tafel("urteil", "Das Urteil vom 16.1.1957"),
    zit("BVerfG, Urteil vom 16.1.1957 – 1 BvR 253/56 (BVerfGE 6, 32)", 110, 168, "urteil"),
    pl("Erste Frage: Art. 11 Abs. 1 GG", 110, 205, "a11", fill=PINK, size=32),
    *w11,
    *neinz("Wortlaut: kein Recht auf Ausreise", w11_y + 36, "wortl", "Bold", 36, x=160),
    zit("BVerfGE 6, 32 <34>", 160, w11_y + 88, "wortl"),
    z("Schranken des Abs. 2 zielen auf das Inland;", 160, w11_y + 150, "schr", "Bold", 34),
    z("die Passversagung wegen Staatssicherheit fehlt", 160, w11_y + 198, beim("schr", "Passversagung"), size=34),
    zit("<35>", 160, w11_y + 248, beim("schr", "Passversagung")),
    blk(110, w11_y + 300, 1040, 80, HELLROT, "nein11", [("Art. 11 GG erfasst die Ausreise nicht", "ExtraBold", 36, INK)]),
    zit("Leitsatz 1; <35 f.>", 110, w11_y + 395, "nein11"),
    *requisit([("urteil", ("tabler", "building-bank", 120, WEISS), "BVerfG, 16.1.1957", GELB),
               (beim("a11", "ganzen"), ("tabler", "map", 110, BLAUHELL), "im ganzen Bundesgebiet", BLAUHELL),
               ("schr", ("tabler", "fence", 110, WEISS), "Schranken, Abs. 2", WEISS),
               ("nein11", ("tabler", "plane-off", 110, HELLROT), "Ausreise: nicht Art. 11", HELLROT)]),
    *stehend("TB", FX, [("urteil", "ruhig"), ("wortl", "denkt"), ("nein11", "sorge")]),
])

# ===========================================================================================================================
# E1 II. Art. 2 Abs. 1 GG (Wortlautkarte)
# ===========================================================================================================================
PII = "II. Allgemeine Handlungsfreiheit, Art. 2 Abs. 1 GG"
W2 = ["„(1) Jeder hat das Recht auf die freie Entfaltung seiner",
      "Persönlichkeit, soweit er nicht die Rechte anderer verletzt",
      "und nicht gegen die verfassungsmäßige Ordnung oder das",
      "Sittengesetz verstößt.“"]
w2, w2_y = wortlaut(80, 190, 1100, W2, "Art. 2 Abs. 1 GG", "a2", marken=[
    (0, "freie Entfaltung", beim("a2", "freie")), (1, "Rechte anderer", beim("a2", "Rechte")),
    (2, "verfassungsmäßige Ordnung", beim("a2", "verfassungsmäßige")), (3, "Sittengesetz", beim("a2", "Sittengesetz"))],
    size=32)
folie([("a2", f"{PII} · Wortlaut")], [
    *tafel("a2", "Geschützt durch Art. 2 Abs. 1 GG"),
    *w2,
    *requisit([("a2", ("tabler", "book", 100, WEISS), "Art. 2 Abs. 1 GG", GELB),
               (beim("a2", "Rechte"), ("tabler", "fence", 110, WEISS), "Schranken", WEISS)]),
    *stehend("HP", FX, [("a2", "ruhig"), (beim("a2", "Rechte"), "denkt")]),
])

# ===========================================================================================================================
# E2 Kernbereich oder umfassende Handlungsfreiheit? (<36 f.>; Leitsatz 2)
# ===========================================================================================================================
folie([("kern", f"{PII} › Gegenansicht: nur ein Kernbereich"), ("umf", f"{PII} › Handlungsfreiheit im umfassenden Sinn"),
       ("ausfl", f"{PII} › Ausreisefreiheit als Ausfluss")], [
    *tafel("kern", "Wie weit reicht Art. 2 Abs. 1 GG?"),
    blk(110, 180, 1040, 80, HELLROT, "kern", [("Gegenansicht: nur ein Kernbereich der Persönlichkeit", "ExtraBold", 32, INK)]),
    z("Wie sollte die Entfaltung nur in diesem Kern gegen", 110, 290, "warum", "Bold", 32),
    z("die Rechte anderer oder die verfassungsmäßige", 110, 334, beim("warum", "Rechte"), "Bold", 32),
    z("Ordnung verstoßen?", 110, 378, beim("warum", "verfassungsmäßige"), "Bold", 32),
    zit("BVerfGE 6, 32 <36>", 110, 424, beim("warum", "verfassungsmäßige")),
    nein(1120, 220, "umf", gr=26),
    *okz("BVerfG: Handlungsfreiheit im umfassenden Sinn", 480, "umf", "ExtraBold", 34, x=160),
    blk(110, 560, 1040, 110, ZITAT, "tun", [("ursprüngliche Fassung:", "Regular", 30, TEXT),
                                         ("„Jeder kann tun und lassen was er will“", "ExtraBold", 34, INK)]),
    zit("<36 f.>", 110, 682, "tun"),
    pl("Ausreisefreiheit: Ausfluss der allgemeinen Handlungsfreiheit", 110, 740, "ausfl", fill=PINK, size=32),
    zit("Leitsatz 2; <36>", 110, 822, "ausfl"),
    *requisit([("kern", ("tabler", "user", 100, HELLROT), "nur der Kern?", HELLROT),
               ("umf", ("tabler", "users-group", 120, GRUEN), "umfassend", GRUEN),
               ("ausfl", ("tabler", "plane-departure", 120, BLAUHELL), "Ausreisefreiheit", PINK)]),
    *paar("TB", [("kern", "denkt"), ("umf", "froh")], "HP", [("kern", "ruhig"), ("ausfl", "denkt")]),
])

# ===========================================================================================================================
# E3 Das Auffanggrundrecht (<37>)
# ===========================================================================================================================
folie([("auff", f"{PII} › Verhältnis zu den besonderen Grundrechten"), ("auff2", f"{PII} › Auffanggrundrecht")], [
    *tafel("auff", "Besondere Grundrechte und Art. 2 Abs. 1 GG"),
    *[blk(110 + i * 350, 200, 340, 110, BLAUHELL, beim("auff", "besondere"),
          [("besonderes", "ExtraBold", 30, INK), ("Grundrecht", "ExtraBold", 30, INK)]) for i in range(3)],
    z("für bestimmte Lebensbereiche", 110, 330, beim("auff", "besondere"), "Bold", 34),
    pfeil(630, 390, 630, 470, beim("auff", "keines"), breite=10, kopf=30),
    blk(110, 490, 1040, 110, GELB, beim("auff", "keines"), [("greift keines: Art. 2 Abs. 1 GG", "ExtraBold", 36, INK)]),
    zit("BVerfGE 6, 32 <37>", 110, 615, beim("auff", "keines")),
    pl("das Auffanggrundrecht", 110, 680, "auff2", fill=PINK, size=40),
    *requisit([("auff", ("tabler", "shield-check", 110, BLAUHELL), "besondere Grundrechte", BLAUHELL),
               ("auff2", ("tabler", "lifebuoy", 120, GELB), "Auffanggrundrecht", PINK)]),
    *paar("TB", [("auff", "ruhig"), ("auff2", "froh")], "HP", [("auff", "denkt"), ("auff2", "ruhig")]),
])

# ===========================================================================================================================
# F1 III. Schranke: verfassungsmäßige Ordnung (<37–41>; Leitsatz 3)
# ===========================================================================================================================
PIII = "III. Schranke: verfassungsmäßige Ordnung"
folie([("schranke", PIII), ("jede", f"{PIII} › jede verfassungsmäßige Rechtsnorm"), ("leer", f"{PIII} › kein Leerlauf"),
       ("kernber", f"{PIII} › unantastbarer Bereich")], [
    *tafel("schranke", "Die Schranke: verfassungsmäßige Ordnung"),
    *okz("gemeint: die verfassungsmäßige Rechtsordnung", 180, "ordn", "Bold", 34, x=160),
    blk(110, 250, 1040, 120, GELB, "jede", [("jede Rechtsnorm, die formell und materiell", "ExtraBold", 34, INK),
                                         ("der Verfassung gemäß ist", "ExtraBold", 34, INK)]),
    zit("BVerfGE 6, 32 <37 f.>; Leitsatz 3", 110, 385, "jede"),
    pl("Läuft das Grundrecht damit leer?", 110, 450, "leer", fill=PINK, size=34),
    *neinz("Nein: Das Gesetz muss selbst verfassungsmäßig", 540, beim("leer", "Nein"), "Bold", 34, x=160),
    z("sein, vor allem rechtsstaatlich.", 160, 588, beim("leer", "rechtsstaatlich"), "Bold", 34),
    zit("<40 f.>", 160, 636, beim("leer", "rechtsstaatlich")),
    blk(110, 690, 1040, 120, LILA, "kernber", [("ein letzter, unantastbarer Bereich privater", "ExtraBold", 34, INK),
                                            ("Lebensgestaltung bleibt jedem Zugriff entzogen", "ExtraBold", 34, INK)]),
    zit("<41>", 110, 822, "kernber"),
    *requisit([("schranke", ("tabler", "fence", 120, WEISS), "Schranke", WEISS),
               ("jede", ("tabler", "book", 100, GELB), "Rechtsordnung", GELB),
               ("leer", ("tabler", "shield-check", 100, WEISS), "verfassungsmäßig?", WEISS),
               ("kernber", ("tabler", "lock", 100, LILA), "unantastbar", LILA)]),
    *stehend("HP", FX, [("schranke", "ruhig"), ("leer", "denkt"), ("kernber", "ruhig")]),
])

# ===========================================================================================================================
# F2 Gehört das Passgesetz dazu? (<42 f.>)
# ===========================================================================================================================
folie([("passg", f"{PIII} › Passgesetz"), ("vage", f"{PIII} › „sonstige erhebliche Belange“"),
       ("eng", f"{PIII} › enge Auslegung")], [
    *tafel("passg", "Gehört das Passgesetz dazu?"),
    *okz("Anspruch auf den Pass; Versagung nur unter", 180, "anspr", "Bold", 34, x=160),
    z("bestimmten Voraussetzungen: wahrt die Freiheitsvermutung", 160, 228, beim("anspr", "Freiheitsvermutung"), size=32),
    zit("BVerfGE 6, 32 <42>", 160, 274, beim("anspr", "Freiheitsvermutung")),
    blk(110, 330, 1040, 120, HELLROT, "vage", [("Bedenken: „sonstige erhebliche Belange“", "ExtraBold", 34, INK),
                                            ("keine vage Generalklausel ins Ermessen", "Regular", 32, INK)]),
    zit("<42>", 110, 462, beim("vage", "Generalklausel")),
    *okz("Die Gerichte prüfen den Begriff voll nach.", 525, "voll", "Bold", 34, x=160),
    zit("<42 f.>", 160, 573, "voll"),
    *okz("eng: an Gewicht der inneren und äußeren", 635, "eng", "Bold", 34, x=160),
    z("Sicherheit nahekommend", 160, 683, beim("eng", "Sicherheit"), "Bold", 34),
    zit("<43>", 160, 731, beim("eng", "Sicherheit")),
    *requisit([("passg", ("tabler", "book", 100, WEISS), "Passgesetz", WEISS),
               ("anspr", ("tabler", "id-badge-2", 100, GRUEN), "Anspruch auf den Pass", GRUEN),
               ("vage", ("tabler", "alert-triangle", 100, HELLROT), "zu vage?", HELLROT),
               ("voll", ("tabler", "gavel", 110, HOLZ), "volle Kontrolle", WEISS),
               ("eng", ("tabler", "shield-check", 100, GRUEN), "enge Auslegung", GRUEN)]),
    *paar("TB", [("passg", "ruhig"), ("vage", "denkt"), ("eng", "froh")], "HP", [("passg", "denkt"), ("voll", "ruhig")]),
])

# ===========================================================================================================================
# G Ergebnis (<32 Entscheidungsformel, 43–45>)
# ===========================================================================================================================
folie([("erg", "Ergebnis · Vorschrift verfassungsgemäß"), ("zur", "Ergebnis · Verfassungsbeschwerde zurückgewiesen (−)"),
       ("begr", "Ergebnis · Anspruch auf Begründung")], [
    *tafel("erg", "Ergebnis"),
    blk(110, 170, 1040, 120, GRUEN, "erg", [("So verstanden ist § 7 Abs. 1 Buchst. a PaßG", "ExtraBold", 34, INK),
                                         ("verfassungsgemäß.", "ExtraBold", 34, INK)]),
    *okz("auch die Anwendung durch das BVerwG hält stand", 330, "anw", "Bold", 34, x=160),
    zit("BVerfGE 6, 32 <43 f.>", 160, 378, "anw"),
    *neinz("Elfes nicht in seinen Grundrechten verletzt", 440, "zur", "Bold", 36, x=160),
    pl("Die Verfassungsbeschwerde wird zurückgewiesen.", 110, 510, beim("zur", "Verfassungsbeschwerde"), fill=GELB, size=34),
    zit("<32> (Entscheidungsformel), <44>", 110, 590, beim("zur", "Verfassungsbeschwerde")),
    blk(110, 650, 1040, 120, HELL, "begr", [("nicht gebilligt: Versagung ohne Begründung", "ExtraBold", 34, INK),
                                         ("Anspruch darauf, die Gründe zu erfahren", "Regular", 32, INK)]),
    zit("<44 f.>", 110, 782, "begr"),
    *requisit([("erg", ("tabler", "circle-check", 100, GRUEN), "verfassungsgemäß", GRUEN),
               ("zur", ("tabler", "building-bank", 120, WEISS), "zurückgewiesen", GELB),
               ("begr", ("tabler", "file-text", 100, WEISS), "Begründung", HELL)]),
    *stehend("TB", FX, [("erg", "denkt"), ("zur", "sorge"), ("begr", "ruhig")]),
])

# ===========================================================================================================================
# H Die Bedeutung (Leitsatz 4 <32>, <41>; BVerfGE 80, 137 <152 f.>)
# ===========================================================================================================================
folie([("tor", "Bedeutung · Verfassungsbeschwerde für jedermann"), ("messbar", "Bedeutung · am ganzen Grundgesetz messbar"),
       ("reiten", "Bedeutung · Reiten im Walde, 1989"), ("verh", "Bedeutung · Maßstab: Verhältnismäßigkeit")], [
    *tafel("tor", "Die Bedeutung des Elfes-Urteils"),
    blk(110, 175, 1040, 160, GELB, "tor", [("Jeder kann rügen: Die Norm, die seine", "ExtraBold", 33, INK),
                                        ("Handlungsfreiheit beschränkt, gehört nicht", "ExtraBold", 33, INK),
                                        ("zur verfassungsmäßigen Ordnung.", "ExtraBold", 33, INK)]),
    zit("BVerfGE 6, 32, Leitsatz 4; <41>", 110, 348, "tor"),
    *okz("So wird jede solche Norm am ganzen", 410, "messbar", "Bold", 34, x=160),
    z("Grundgesetz messbar.", 160, 458, beim("messbar", "Grundgesetz"), "Bold", 34),
    blk(110, 530, 1040, 120, BLAUHELL, "reiten", [("1989, Reiten im Walde: geschützt ist", "ExtraBold", 34, INK),
                                               ("jede Form menschlichen Handelns", "ExtraBold", 34, INK)]),
    zit("BVerfG, Beschl. v. 6.6.1989 – 1 BvR 921/85, BVerfGE 80, 137 <152 f.>", 110, 662, "reiten"),
    *okz("materieller Maßstab: Grundsatz der", 725, "verh", "Bold", 34, x=160),
    z("Verhältnismäßigkeit", 160, 773, beim("verh", "Verhältnismäßigkeit"), "ExtraBold", 34),
    zit("BVerfGE 80, 137 <153>", 160, 821, beim("verh", "Verhältnismäßigkeit")),
    *requisit([("tor", ("tabler", "building-bank", 120, WEISS), "Verfassungsbeschwerde", GELB),
               ("messbar", ("tabler", "search", 100, WEISS), "ganzes Grundgesetz", WEISS),
               ("reiten", ("tabler", "horse", 120, HOLZ), "Reiten im Walde", BLAUHELL),
               ("verh", ("tabler", "scale", 110, GELB), "Verhältnismäßigkeit", GELB)]),
    *paar("TB", [("tor", "ruhig"), ("reiten", "froh")], "HP", [("tor", "denkt"), ("verh", "ruhig")]),
])

# ===========================================================================================================================
# I1 Zurück zum Fall: Torben fragt (Schauplatz A1, die Geschichte kehrt dorthin zurück)
# ===========================================================================================================================
O2 = "o2"
folie([(O2, "Zurück zum Fall · Torben")], [
    *buehne(O2, fig("HP", HPX, BODEN, FH, [(O2, "ruhig_r")], erst="cut")),
    hart(ns("Herr Haupt", HPX, BODEN, O2, BLAUHELL)),
    hart(ficon("tabler", "file-text", 860, SOBEN + 2, 80, O2, fuell=WEISS, anim="cut")),
    hart(ficon("streamline-freehand", "office-stamp-document", 860, SOBEN - 60, 90, O2, fuell=HELLROT, anim="cut")),
    hart(reisepass(520, SOBEN + 2, 74, O2, anim="cut")),
    *redet("TB_redet", TBX, BODEN, FH, O2, "heute"),
    hart(ns("Torben", TBX, BODEN, O2, GRUEN)),
    blase("sprech", 640, 170, O2, 1500, 260, inhalt=["Und was heißt das", "für meinen Pass?"], textsize=32,
          figur=("TB_redet", TBX, BODEN, FH), bis="heute"),
])

# ===========================================================================================================================
# I2 § 7 PassG heute (Wortlautkarte, Abruf 04.10.2026)
# ===========================================================================================================================
W7 = ["„(1) Der Pass ist zu versagen, wenn bestimmte Tatsachen die",
      "Annahme begründen, dass der Passbewerber 1. die innere oder",
      "äußere Sicherheit oder sonstige erhebliche Belange der",
      "Bundesrepublik Deutschland gefährdet; …",
      "(2) Von der Passversagung ist abzusehen, wenn sie",
      "unverhältnismäßig ist, insbesondere wenn es genügt, den",
      "Geltungsbereich oder die Gültigkeitsdauer des Passes zu",
      "beschränken. …“"]
w7, w7_y = wortlaut(80, 150, 1100, W7, "§ 7 Abs. 1 Nr. 1, Abs. 2 Satz 1 PassG (Auszug)", "heute", marken=[
    (0, "bestimmte Tatsachen", beim("tb2", "bestimmte")), (2, "sonstige erhebliche Belange", beim("tb2", "Belange")),
    (5, "unverhältnismäßig", beim("abs2", "unverhältnismäßig")), (7, "beschränken", beim("abs2", "beschränkter"))], size=30)
PZ = "Zurück zum Fall"
folie([("heute", f"{PZ} · § 7 Abs. 1 Nr. 1 PassG heute"), ("tb1", f"{PZ} · Art. 2 Abs. 1 GG betroffen"),
       ("tb2", f"{PZ} · bestimmte Tatsachen"), ("abs2", f"{PZ} · Verhältnismäßigkeit, § 7 Abs. 2 PassG")], [
    *tafel("heute", "Torbens Pass: § 7 PassG heute"),
    *w7,
    *okz("betroffen: Art. 2 Abs. 1 GG, nicht Art. 11 GG", w7_y + 26, "tb1", "Bold", 34, x=160),
    *okz("Belange: nach Elfes nahe an der Staatssicherheit", w7_y + 86, beim("tb2", "Elfes"), "Bold", 32, x=160),
    zit("BVerfGE 6, 32 <43>", 160, w7_y + 132, beim("tb2", "Elfes")),
    pl("§ 7 Abs. 2: Versagung nicht unverhältnismäßig", 110, w7_y + 190, beim("abs2", "unverhältnismäßig"),
       fill=GRUEN, size=32),
    *requisit([("heute", ("tabler", "book", 100, WEISS), "§ 7 PassG heute", WEISS),
               ("tb1", ("tabler", "user", 100, GRUEN), "Torben: Art. 2 Abs. 1", GRUEN),
               ("tb2", ("tabler", "search", 100, WEISS), "bestimmte Tatsachen?", WEISS),
               ("abs2", ("tabler", "scale", 110, GELB), "verhältnismäßig?", GRUEN)]),
    *paar("TB", [("heute", "denkt"), ("abs2", "froh")], "HP", [("heute", "ruhig"), ("tb2", "denkt")]),
])

# ===========================================================================================================================
# J Klausurtipp (Lexi) – Art. 2 Abs. 1 GG zuletzt (<37>)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Art. 2 Abs. 1 GG zuletzt"), ("tipp2", "Klausurtipp · Auffanggrundrecht")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Art. 2 Abs. 1 GG immer zuletzt prüfen", 200, 200, beim("tipp", "zuletzt"), "Bold", 36),
    z("erst die speziellen Grundrechte,", 200, 270, beim("tipp", "speziellen"), size=34),
    z("hier Art. 11 GG", 200, 318, beim("tipp", "Artikel", nr=2), size=34),
    linienzug([(130, 400), (1130, 400)], "tipp2", breite=3),
    *okz("nur wenn keines greift: die allgemeine", 430, "tipp2", "Bold", 34, x=200),
    z("Handlungsfreiheit", 200, 478, beim("tipp2", "allgemeine"), "Bold", 34),
    pl("als Auffanggrundrecht", 200, 545, beim("tipp2", "Auffanggrundrecht"), fill=PINK, size=36),
    zit("BVerfGE 6, 32 <37>", 200, 625, beim("tipp2", "Auffanggrundrecht")),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# K Prüfschema
# ===========================================================================================================================
REIHEN = [("k1", 0, "I. Schutzbereich", True),
          (beim("k1", "speziellen"), 1, "zuerst spezielle Grundrechte: Art. 11 GG erfasst die Ausreise nicht", False),
          ("k2", 1, "dann Art. 2 Abs. 1 GG: jedes Verhalten, auch die Ausreise", False),
          ("k3", 0, "II. Eingriff: die Passversagung", True),
          ("k4", 0, "III. Rechtfertigung", True),
          (beim("k4", "Schranke"), 1, "Schranke: verfassungsmäßige Ordnung", False),
          ("k5", 1, "Gesetz formell und materiell: Bestimmtheit, Verhältnismäßigkeit", False),
          ("k6", 1, "Anwendung im Einzelfall", False)]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Prüfschema: allgemeine Handlungsfreiheit"), 110, 90, "sch", 46)]
y = 210
for c, ebene, text, fett in REIHEN:
    x = (130, 200)[ebene]
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 40 if ebene == 0 else 36, rechts=1800))
    y += {0: 88, 1: 80}[ebene]
assert y <= 970, y
folie([("sch", "Prüfschema"), ("k1", "Prüfschema › I. Schutzbereich"), ("k3", "Prüfschema › II. Eingriff"),
       ("k4", "Prüfschema › III. Rechtfertigung"), ("k5", "Prüfschema › III. Gesetz"), ("k6", "Prüfschema › III. Anwendung")],
      els_sch)

# ===========================================================================================================================
# L Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Art. 2 Abs. 1 GG schützt", 0)], [("jedes Verhalten", "a"), (", auch die Ausreise.", 0)]],
                750, 300, 44, "merke", {"a": beim("merke", "jedes")}),
    *markertext([[("Beschränken darf diese Freiheit nur", 0)], [("eine Norm, die ", 0), ("formell und materiell", "b")],
                 [("verfassungsmäßig ist.", 0)]], 750, 520, 44, "m2", {"b": beim("m2", "formell")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
