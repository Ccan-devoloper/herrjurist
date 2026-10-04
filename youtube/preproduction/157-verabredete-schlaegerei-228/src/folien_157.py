"""Folge 157 · Verabredete Schlägerei: Einwilligung? Sittenwidrigkeit § 228 StGB – Serienstandard Open Peeps (Katzenkönig).
Fiktiver Einstieg (Sönke, Gruppe A; Inken, Gruppe B: Verabredung per Chat zu einem „Match“ auf der Wiese), danach der echte
Fall sachlich ohne Figuren: BGH, Beschl. v. 20.2.2013 – 1 StR 585/12, BGHSt 58, 140 (Rn. nach HRRS); Fortführung
BGH, Urt. v. 22.1.2015 – 3 StR 233/14, BGHSt 60, 166. DARSTELLUNG: keine Prügelszene, keine Schläge, kein Blut, keine
Verletzten im Bild, keine Vereinsfarben/Schals/Logos; Gruppen nur als neutrale farbige Gruppen-Icons mit Pillen, Verabredung
über Chat-Icons, Wiese als Landschafts-Icon, Figuren stehen ruhig. Szenen laut ../SZENENPLAN.md. Hilfsfunktionen
glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/requisit/stehend/paar/spricht_neben als eigene Kopie aus Folge 146
(gemeinsame Dateien unverändert); tisch() entfernt. Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from ostil import titel, karte, pille
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_157/"

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
        if n.startswith(("bild:", "ficon:", "bank")) or "/op_157/" in n:
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






BODEN = 860
FH = 440                                    # stehende Figur in der Fallszene
X1, X2 = 1430, 1730                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"SO": "Sönke", "IN": "Inken"}
NFARBE = {"SO": BLAU, "IN": LILA}


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




GRUPPE = {"A": BLAU, "B": LILA}               # neutrale Palettenfarben, keine Vereinsfarben


def gruppe(x, cue, txt, fill, breite=170, unten=BODEN, py=None, bis=None, icon="users-group"):
    """Gruppen-Icon (Tabler users-group) mit Pille darunter – Gruppen erscheinen nur als Icon, nie als Prügelszene."""
    return [ficon("tabler", icon, x, unten, breite, cue, fuell=fill, bis=bis),
            pl(txt, x, py if py is not None else unten + 22, cue, fill=fill, size=30, anker="m", bis=bis)]


# ===========================================================================================================================
# A Fall: Verabredung per Chat, das Match (fiktiv) – ruhig stehende Figuren, Gruppen als Icons, Wiese als Landschafts-Icon
# ===========================================================================================================================
SX, IX = 330, 1590                           # Sönke links (blickt nach rechts), Inken rechts (blickt nach links)
GA, GB = 760, 1160                           # Gruppen-Icons auf der Wiese


def wiese(cue):
    return [boden(cue),
            hart(ficon("tabler", "trees", 960, BODEN, 150, cue, fuell=GRUEN, anim="cut")),
            hart(ficon("ph", "plant", 880, BODEN, 60, cue, fuell=GRUEN, anim="cut")),
            hart(ficon("ph", "plant", 1045, BODEN, 60, cue, fuell=GRUEN, anim="cut")),
            hart(pl("Wiese am Waldrand", 960, 645, cue, fill=HELLGRUEN, size=30, anker="m"))]


folie([(NULL, "Fall · Die Verabredung per Chat"), ("match", "Fall · Das Match"), ("frage0", "Fall · Die Frage")], [
    *wiese(NULL),
    *[hart(e) for e in gruppe(GA, NULL, "Gruppe A", BLAU)],
    *[hart(e) for e in gruppe(GB, NULL, "Gruppe B", LILA)],
    ficon("tabler", "messages", 960, 205, 100, beim("fall", "Chat"), fuell=WEISS, bis="s1"),
    pl("Verabredung per Chat: ein Match", 960, 60, beim("fall", "Chat"), fill=WEISS, size=30, anker="m", bis="match"),
    # Sönke (Gruppe A) schreibt; das Handy an seiner Seite, Nachrichten-Icon zum Wort
    *fig("SO", SX, BODEN, FH, [("soenke", "ruhig_r")], bis="s1"),
    ns("Sönke", SX, BODEN, "soenke", BLAU, d=0.1),
    ficon("tabler", "device-mobile", SX + 150, 640, 70, "soenke", fuell=BLAUHELL, bis="match"),
    ficon("tabler", "message-circle", SX + 150, 540, 64, beim("soenke", "schreibt"), fuell=BLAU, bis="match"),
    *redet("SO_redet_r", SX, BODEN, FH, "s1", "inken"),
    blase("sprech", 720, 220, "s1", 800, 270, inhalt=["Samstag, 10 gegen 10, auf", "der Wiese am Waldrand. Keine",
                                                    "Waffen, sonst ist alles erlaubt."], textsize=31,
          figur=("SO_redet_r", SX, BODEN, FH), bis="inken"),
    *fig("SO", SX, BODEN, FH, [("inken", "denkt_r"), ("match", "ruhig_r"), ("verl", "ernst_r"), ("frage0", "denkt_r")],
         erst="cut"),
    # Inken (Gruppe B) antwortet
    *fig("IN", IX, BODEN, FH, [("inken", "ruhig")], bis="i1"),
    ns("Inken", IX, BODEN, "inken", LILA, d=0.1),
    szene(ficon("tabler", "device-mobile", IX - 150, 640, 70, "inken", fuell=BLAUHELL, bis="match"), "157handy*", 0.7, 0.05),
    ficon("tabler", "message-circle", IX - 150, 540, 64, beim("inken", "antwortet"), fuell=LILA, bis="match"),
    *redet("IN_redet", IX, BODEN, FH, "i1", "match"),
    blase("sprech", 720, 220, "i1", 1120, 270, inhalt=["Einverstanden. Wer am Boden", "liegt, ist raus. Und wir bringen",
                                                    "2 Schiedsrichter mit."], textsize=31,
          figur=("IN_redet", IX, BODEN, FH), bis="match"),
    *fig("IN", IX, BODEN, FH, [("match", "ruhig"), ("verl", "ernst"), ("frage0", "denkt")], erst="cut"),
    # Das Match: nur Pillen, keine Kampfszene
    ficon("tabler", "calendar", 600, 175, 90, "match", fuell=WEISS),
    pl("Samstag: beide Gruppen auf der abgelegenen Wiese", 660, 100, "match", fill=GELB, size=30),
    *okz("alle wissen: Es wird Verletzte geben", 205, beim("match", "Alle"), "Bold", 30, x=640, rechts=1380),
    *okz("alle sind einverstanden", 260, beim("match", "einverstanden"), "Bold", 30, x=640, rechts=1380),
    pl("einige werden leicht verletzt", 640, 330, "verl", fill=HELLROT, size=30),
    pl("Durch die Einwilligung gerechtfertigt?", 960, 455, "frage0", fill=PINK, size=34, anker="m"),
    pl("Antwort: ein Klassiker des BGH", 960, 540, "klassiker", fill=WEISS, size=30, anker="m"),
])

# ===========================================================================================================================
# B1 Der echte Fall (BGHSt 58, 140, Rn. 3–5) – ohne Figuren, neutrale Gruppen-Icons
# ===========================================================================================================================
P58 = "Der echte Fall · BGHSt 58, 140"
folie([("echt", f"{P58} · zwei Gruppen"), ("faktisch", f"{P58} · die Übereinkunft"), ("minuten", f"{P58} · die Folgen")], [
    boden("echt"),
    pl("Zwei Gruppen junger Leute geraten aneinander", 70, 40, "echt", fill=GELB, size=32),
    *gruppe(430, "echt", "eine Gruppe", GELB, breite=230),
    *gruppe(1490, "echt", "andere Gruppe", GRUEN, breite=230),
    ficon("tabler", "device-mobile", 640, 845, 70, "anruf", fuell=BLAUHELL),
    ficon("tabler", "users-plus", 640, 700, 100, beim("anruf", "weitere"), fuell=GELB),
    pl("Anruf: weitere Mitglieder kommen", 70, 118, beim("anruf", "weitere"), fill=WEISS, size=30),
    pfeil(780, 760, 1160, 760, "gegen", breite=9, kopf=28),
    pfeil(1160, 800, 780, 800, "gegen", breite=9, kopf=28),
    pl("beide Gruppen stehen sich gegenüber", 70, 188, "gegen", fill=WEISS, size=30),
    pl("faktische Übereinkunft: Faustschläge und Fußtritte", 70, 258, "faktisch", fill=HELLROT, size=30),
    pl("auch erhebliche Verletzungen gebilligt", 70, 328, beim("faktisch", "erhebliche"), fill=HELLROT, size=30),
    ficon("tabler", "stopwatch", 960, 520, 110, "minuten", fuell=WEISS),
    pl("4–5 Minuten: mehrere Beteiligte erheblich verletzt", 960, 545, beim("minuten", "mehrere"), fill=WEISS, size=30,
       anker="m"),
])

# ===========================================================================================================================
# B2 LG Stuttgart und BGH (Rn. 1 f.)
# ===========================================================================================================================
folie([("lg", f"{P58} · LG Stuttgart"), ("bgh", f"{P58} · BGH, 20.2.2013"), ("frage", f"{P58} · die Frage")], [
    *tafel("lg", "Landgericht Stuttgart und BGH"),
    *okz("LG Stuttgart: gefährliche Körperverletzung", 190, "lg", "Bold", 34, x=160),
    z("§§ 223, 224 Abs. 1 Nr. 4 StGB", 160, 240, beim("lg", "gefährlicher"), size=34),
    *okz("BGH verwirft die Revisionen", 330, "bgh", "Bold", 34, x=160),
    zit("BGH, Beschl. v. 20.2.2013 – 1 StR 585/12, BGHSt 58, 140, Rn. 1 f.", 160, 382, beim("bgh", "Beschluss")),
    pl("Warum hilft die Einwilligung nicht?", 110, 480, "frage", fill=PINK, size=38),
    *requisit([("lg", ("tabler", "gavel", 170, HOLZ), "LG Stuttgart", WEISS),
               ("bgh", ("tabler", "building-bank", 180, WEISS), "Bundesgerichtshof", GELB),
               ("frage", ("tabler", "help-circle", 150, PINK), "Einwilligung?", PINK)], pu=640, py=260),
])


# ===========================================================================================================================
# C Sachverhalt
# ===========================================================================================================================
def sachverhalt_157(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=33, zeilenabstand=1.28)
        els += e; y += 16
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_157("sv", [
    "Zwei Gruppen junger Leute geraten aneinander. Ein Angeklagter ruft per Telefon weitere Mitglieder seiner Gruppe "
    "herbei. Dann stehen sich beide Gruppen gegenüber. Aufgrund einer faktischen Übereinkunft wollen alle die "
    "Auseinandersetzung mit Faustschlägen und Fußtritten austragen; auch erhebliche Verletzungen billigen sie. Absprachen, "
    "die den Kampf begrenzen, gibt es nicht. In vier bis fünf Minuten werden mehrere Beteiligte erheblich verletzt.",
    "Das Landgericht Stuttgart verurteilt die Angeklagten wegen gefährlicher Körperverletzung (§§ 223, 224 Abs. 1 Nr. 4 "
    "StGB). Der Bundesgerichtshof verwirft die Revisionen (Beschluss vom 20.2.2013 – 1 StR 585/12, BGHSt 58, 140).",
], "Sind die Körperverletzungen durch die Einwilligung der Verletzten gerechtfertigt?")

# ===========================================================================================================================
# D Einwilligung (Verweis Folge 062) und § 228 StGB (Wortlautkarte)
# ===========================================================================================================================
PI = "I. Einwilligung"
W228 = ["„Wer eine Körperverletzung mit Einwilligung der verletzten",
        "Person vornimmt, handelt nur dann rechtswidrig, wenn die",
        "Tat trotz der Einwilligung gegen die guten Sitten verstößt.“"]
w228, w228_y = wortlaut(80, 370, 1100, W228, "§ 228 StGB", "p228", marken=[
    (0, "Einwilligung", beim("p228", "Einwilligung")), (1, "rechtswidrig", beim("p228", "rechtswidrig")),
    (2, "guten Sitten", beim("p228", "guten"))], size=32)
folie([("einw", f"{PI} · Voraussetzungen (eigene Folge)"), ("hier", f"{PI} · in Schläge und Tritte eingewilligt"),
       ("p228", f"{PI} › Grenze: § 228 StGB"), ("ort", f"{PI} › Prüfungsort: Rechtswidrigkeit")], [
    *tafel("einw", "Die Einwilligung und ihre Grenze"),
    z("Wann ist eine Einwilligung wirksam? Eigene Folge", 110, 175, "einw", size=32),
    *okz("zwei Verletzte: eingewilligt in Faustschläge", 235, "hier", "Bold", 32, x=160),
    z("und Fußtritte, auch in die typischen Folgen", 160, 280, beim("hier", "typischen"), size=32),
    zit("BGHSt 58, 140, Rn. 7", 160, 325, beim("hier", "typischen")),
    *w228,
    pl("Prüfungsort: Rechtswidrigkeit", 110, w228_y + 30, "ort", fill=PINK, size=36),
    *requisit([("einw", ("tabler", "writing-sign", 110, WEISS), "Einwilligung", WEISS),
               ("p228", ("tabler", "scale", 110, GELB), "§ 228 StGB", GELB),
               ("ort", ("tabler", "list-check", 100, PINK), "Rechtswidrigkeit", PINK)]),
    *paar("SO", [("einw", "ruhig"), ("p228", "denkt")], "IN", [("einw", "ruhig"), ("ort", "denkt")]),
])

# ===========================================================================================================================
# E Maßstab der guten Sitten (BGHSt 58, 140 Rn. 9, 12; BGHSt 49, 166 Rn. 23, 24, 26, 29)
# ===========================================================================================================================
PII = "II. Gute Sitten"
folie([("mass", f"{PII} › Maßstab: Gewicht und Gefahr"), ("exante", f"{PII} › Sicht vor der Tat"),
       ("tod", f"{PII} › jedenfalls: konkrete Todesgefahr"), ("zweck", f"{PII} › und der Zweck?")], [
    *tafel("mass", "Wann verstößt die Tat gegen die guten Sitten?", size=42),
    *okz("vorrangig: Art und Gewicht der Verletzung", 180, beim("mass", "Vorrangig"), "Bold", 34, x=160),
    z("und Grad der Gefahr für Leib und Leben", 160, 228, beim("mass", "Grad"), "Bold", 34),
    zit("BGHSt 58, 140, Rn. 9; BGHSt 49, 166, Rn. 24", 160, 278, beim("mass", "Grad")),
    *okz("beurteilt aus der Sicht vor der Tat", 330, "exante", "Bold", 34, x=160),
    zit("BGHSt 58, 140, Rn. 12; BGHSt 49, 166, Rn. 29", 160, 380, "exante"),
    blk(110, 430, 1040, 80, HELLROT, "tod", [("jedenfalls sittenwidrig: konkrete Todesgefahr", "ExtraBold", 34, INK)]),
    *neinz("verwerflicher Zweck allein: nicht sittenwidrig", 545, "zweck", "Bold", 34, x=160),
    z("guter Zweck: nur ausnahmsweise, etwa", 160, 610, "heil", size=34),
    z("beim ärztlichen Eingriff", 160, 655, beim("heil", "ärztlichen"), size=34),
    zit("BGHSt 49, 166, Rn. 23, 26; BGHSt 60, 166, Rn. 42", 160, 705, beim("heil", "ärztlichen")),
    *requisit([("mass", ("tabler", "scale", 110, WEISS), "Gewicht und Gefahr", WEISS),
               ("exante", ("tabler", "clock", 100, WEISS), "vor der Tat", WEISS),
               ("tod", ("tabler", "alert-triangle", 100, HELLROT), "konkrete Todesgefahr", HELLROT),
               ("zweck", ("tabler", "target-arrow", 100, WEISS), "Zweck?", WEISS),
               ("heil", ("tabler", "stethoscope", 100, BLAUHELL), "ärztlicher Eingriff", BLAUHELL)]),
    *stehend("IN", FX, [("mass", "denkt"), ("exante", "ruhig"), ("tod", "ernst"), ("heil", "denkt")]),
])

# ===========================================================================================================================
# F Kern BGHSt 58, 140: Eskalationsgefahr, fehlende Absprachen und Sicherungen (Rn. 11, 17, 18, 20, 22; Leitsätze 1, 2)
# ===========================================================================================================================
PIII = "III. BGHSt 58, 140"
folie([("gesamt", f"{PIII} › Gesamtumstände"), ("eskal", f"{PIII} › Eskalationsgefahr"),
       ("abspr", f"{PIII} › keine Absprachen"), ("sicher", f"{PIII} › keine effektiven Sicherungen"),
       ("sitten", f"{PIII} › sittenwidrig")], [
    *tafel("gesamt", "Verabredete Schlägerei zwischen Gruppen"),
    *okz("Gesamtumstände, nicht der einzelne Schlag", 175, "gesamt", "Bold", 34, x=160),
    zit("BGHSt 58, 140, Rn. 18", 160, 225, "gesamt"),
    blk(110, 270, 1040, 80, GELB, "eskal", [("rivalisierende Gruppen: typische Eskalationsgefahr", "ExtraBold", 33, INK)]),
    z("Gruppen beeinflussen sich, Lage unkontrollierbar", 160, 370, "dynamik", size=34),
    zit("Leitsatz 1; Rn. 11, 17", 160, 418, "dynamik"),
    *neinz("keine Absprachen: Schläge gegen Wehrlose,", 470, "abspr", "Bold", 34, x=160),
    z("Überzahl nicht ausgeschlossen", 160, 515, beim("abspr", "Überzahl"), "Bold", 34),
    zit("Rn. 20", 160, 562, beim("abspr", "Überzahl")),
    *neinz("keine effektiven Sicherungen für die Einhaltung", 610, "sicher", "Bold", 34, x=160),
    blk(110, 680, 1040, 120, HELLROT, "sitten", [("sittenwidrig, selbst wenn die einzelnen", "ExtraBold", 34, INK),
                                               ("Verletzungen keine Todesgefahr begründen", "ExtraBold", 34, INK)]),
    zit("Leitsatz 2; Rn. 22", 110, 815, "sitten"),
    *requisit([("gesamt", ("tabler", "users-group", 120, GELB), "Gesamtumstände", GELB),
               ("eskal", ("tabler", "trending-up", 110, HELLROT), "Eskalation", HELLROT),
               ("abspr", ("tabler", "file-x", 100, WEISS), "keine Absprachen", WEISS),
               ("sicher", ("tabler", "lock-open", 100, WEISS), "keine Sicherungen", WEISS),
               ("sitten", ("tabler", "scale", 110, HELLROT), "sittenwidrig", HELLROT)]),
    *paar("SO", [("gesamt", "ruhig"), ("abspr", "denkt"), ("sitten", "ernst")],
          "IN", [("gesamt", "denkt"), ("sicher", "sorge"), ("sitten", "ernst")]),
])

# ===========================================================================================================================
# G § 231 StGB (Wortlautkarte), Schutz im Vorfeld (BGHSt 58, 140 Rn. 17)
# ===========================================================================================================================
W231 = ["„(1) Wer sich an einer Schlägerei oder an einem von mehreren",
        "verübten Angriff beteiligt, wird schon wegen dieser Beteiligung",
        "… bestraft, wenn durch die Schlägerei oder den Angriff der Tod",
        "eines Menschen oder eine schwere Körperverletzung (§ 226)",
        "verursacht worden ist.“"]
w231, w231_y = wortlaut(80, 190, 1100, W231, "§ 231 Abs. 1 StGB (Auszug)", "p231", marken=[
    (0, "Schlägerei", beim("p231", "Schlägerei")), (1, "Beteiligung", beim("p231b", "Beteiligung")),
    (2, "Tod", beim("p231b", "Tod")), (3, "schwere Körperverletzung", beim("p231b", "schwere"))], size=31)
folie([("p231", f"{PIII} › Wertung des § 231 StGB"), ("vorfeld", f"{PIII} › Schutz schon im Vorfeld")], [
    *tafel("p231", "Beteiligung an einer Schlägerei"),
    *w231,
    blk(110, w231_y + 40, 1040, 120, GRUEN, "vorfeld", [("schützt Leben und Gesundheit", "ExtraBold", 34, INK),
                                                       ("schon im Vorfeld", "ExtraBold", 34, INK)]),
    zit("BGHSt 58, 140, Rn. 17", 110, w231_y + 175, "vorfeld"),
    *requisit([("p231", ("tabler", "book", 100, WEISS), "§ 231 StGB", GELB),
               ("vorfeld", ("tabler", "shield-check", 100, GRUEN), "Schutz im Vorfeld", GRUEN)]),
    *stehend("SO", FX, [("p231", "ruhig"), ("p231b", "denkt"), ("vorfeld", "ernst")]),
])

# ===========================================================================================================================
# H Abgrenzung: Boxkampf (BGHSt 58, 140 Rn. 13, 15)
# ===========================================================================================================================
PIV = "IV. Abgrenzung: Sport"
folie([("sport", f"{PIV} › der Boxkampf"), ("gedeckt", f"{PIV} › nach den Regeln gedeckt"),
       ("grob", f"{PIV} › grober Regelverstoß")], [
    *tafel("sport", "Anders beim Boxkampf"),
    *okz("Wettkampfregeln begrenzen die Gefahr,", 190, "regeln", "Bold", 34, x=160),
    z("von Verbänden aufgestellt und überwacht", 160, 238, beim("regeln", "Verbände"), size=34),
    zit("BGHSt 58, 140, Rn. 13, 15", 160, 288, beim("regeln", "Verbände")),
    *okz("Verletzungen nach den Regeln: nicht sittenwidrig", 360, "gedeckt", "Bold", 34, x=160),
    *neinz("grob fahrlässiger oder vorsätzlicher", 450, "grob", "Bold", 34, x=160),
    z("Regelverstoß: nicht mehr gedeckt", 160, 498, beim("grob", "gedeckt"), "Bold", 34),
    zit("Rn. 13", 160, 548, beim("grob", "gedeckt")),
    *requisit([("sport", ("fluent-emoji-flat", "boxing-glove", 110, None), "Boxkampf", WEISS),
               ("regeln", ("tabler", "book", 100, WEISS), "Wettkampfregeln", WEISS),
               ("grob", ("tabler", "alert-triangle", 100, HELLROT), "grober Verstoß", HELLROT)]),
    *stehend("IN", FX, [("sport", "ruhig"), ("grob", "denkt")]),
])

# ===========================================================================================================================
# I1 Und wenn es Absprachen gibt? (BGHSt 58, 140 Rn. 23)
# ===========================================================================================================================
PV = "V. Absprachen und Schiedsrichter"
folie([("offen", f"{PV} › offen gelassen"), ("neigt", f"{PV} › BGH neigt zur Sittenwidrigkeit")], [
    *tafel("offen", "Und wenn es Absprachen gibt?"),
    z("hier nicht zu entscheiden", 160, 190, beim("offen", "Das"), "Bold", 34),
    blk(110, 260, 1040, 120, GELB, "neigt", [("BGH neigt zur Sittenwidrigkeit, wenn die", "ExtraBold", 34, INK),
                                           ("Einhaltung nicht sicher gewährleistet ist", "ExtraBold", 34, INK)]),
    zit("BGHSt 58, 140, Rn. 23", 110, 395, "neigt"),
    *requisit([("offen", ("tabler", "help-circle", 100, WEISS), "Absprachen?", WEISS),
               ("neigt", ("tabler", "scale", 110, GELB), "neigt zu: sittenwidrig", GELB)]),
    *paar("SO", [("offen", "denkt"), ("neigt", "sorge")], "IN", [("offen", "ruhig"), ("neigt", "denkt")]),
])

# ===========================================================================================================================
# I2 Hooligan-Kämpfe mit Regeln (BGHSt 60, 166 Rn. 7, 45, 47, 50, 52, 54)
# ===========================================================================================================================
folie([("hool", f"{PV} › BGHSt 60, 166"), ("wertung", f"{PV} › Wertung des § 231 StGB"),
       ("kopf", f"{PV} › Gefahr schwerer Gesundheitsschäden"), ("box2", f"{PV} › Unterschied zum Boxen")], [
    *tafel("hool", "Hooligan-Kämpfe mit Regeln"),
    zit("BGH, Urt. v. 22.1.2015 – 3 StR 233/14, BGHSt 60, 166", 110, 165, "hool"),
    z("Waffen verboten, teils sogenannte", 160, 210, beim("hool", "Waffen"), "Bold", 34),
    z("Schiedsrichter als Beobachter", 160, 256, beim("hool", "Schiedsrichter"), "Bold", 34),
    zit("Rn. 7", 160, 304, beim("hool", "Schiedsrichter")),
    blk(110, 350, 1040, 120, HELLROT, "wertung", [("sittenwidrig wegen der Wertung des § 231,", "ExtraBold", 34, INK),
                                                ("unabhängig von Vorkehrungen", "ExtraBold", 34, INK)]),
    zit("Rn. 45, 47", 110, 485, "wertung"),
    *okz("jedenfalls: Gefahr schwerer Gesundheitsschäden,", 540, "kopf", "Bold", 33, x=160),
    z("Schläge und Tritte gegen den Kopf erlaubt", 160, 586, beim("kopf", "Schläge"), size=33),
    zit("Rn. 50, 52", 160, 634, beim("kopf", "Schläge")),
    z("Boxen: keine solche gesetzliche Wertung", 160, 700, "box2", "Bold", 34),
    z("für Einzelkämpfe", 160, 746, beim("box2", "Einzelkämpfe"), size=34),
    zit("Rn. 54", 160, 794, beim("box2", "Einzelkämpfe")),
    *requisit([("hool", ("tabler", "flag-2", 100, WEISS), "Regeln, Schiedsrichter", WEISS),
               ("wertung", ("tabler", "scale", 110, HELLROT), "§ 231: sittenwidrig", HELLROT),
               ("kopf", ("tabler", "alert-triangle", 100, HELLROT), "schwere Gefahr", HELLROT),
               ("box2", ("fluent-emoji-flat", "boxing-glove", 100, None), "Einzelkampf", WEISS)]),
    *paar("SO", [("hool", "denkt"), ("wertung", "sorge"), ("box2", "denkt")],
          "IN", [("hool", "denkt"), ("kopf", "ernst"), ("box2", "ruhig")]),
])

# ===========================================================================================================================
# J Zurück zum Fall: Sönke protestiert; Lösung als Prüfliste auf der Wiese (gleicher Schauplatz wie A)
# ===========================================================================================================================
PF = "Lösung des Falls"
LX0, LY0 = 560, 60                             # Prüfliste zwischen den Figuren
folie([("s2", "Zurück zum Fall · Sönke"), ("l1", f"{PF} · Tatbestand, §§ 223, 224 Abs. 1 Nr. 4"),
       ("l3", f"{PF} · Rechtswidrigkeit: Einwilligung"), ("l4", f"{PF} · § 228 StGB"),
       ("l6", f"{PF} · sittenwidrig")], [
    *wiese("s2"),
    *[hart(e) for e in gruppe(GA, "s2", "Gruppe A", BLAU)],
    *[hart(e) for e in gruppe(GB, "s2", "Gruppe B", LILA)],
    *redet("SO_protest_r", SX, BODEN, FH, "s2", "l1"),
    hart(ns("Sönke", SX, BODEN, "s2", BLAU)),
    blase("sprech", 660, 180, "s2", 820, 255, inhalt=["Aber wir hatten doch Regeln", "und Schiedsrichter!"], textsize=32,
          figur=("SO_protest_r", SX, BODEN, FH), bis="l1"),
    *fig("SO", SX, BODEN, FH, [("l1", "denkt_r"), ("l6", "ernst_r")], erst="cut"),
    *fig("IN", IX, BODEN, FH, [("s2", "denkt"), ("l4", "sorge"), ("l6", "ernst")], erst="cut"),
    hart(ns("Inken", IX, BODEN, "s2", LILA)),
    bis_(karte(LX0, LY0, 800, 520, "l1", fill=WEISS, rund=18, schatten=6, rand=4), None),
    *okz("Schläge: körperliche Misshandlung, § 223", LY0 + 30, "l1", "Bold", 28, x=LX0 + 75, rechts=LX0 + 785, gr=16),
    *okz("gemeinschaftlich: § 224 Abs. 1 Nr. 4", LY0 + 95, "l2", "Bold", 28, x=LX0 + 75, rechts=LX0 + 785, gr=16),
    *okz("Rechtswidrigkeit: alle eingewilligt", LY0 + 160, "l3", "Bold", 28, x=LX0 + 75, rechts=LX0 + 785, gr=16),
    z("§ 228: 10 gegen 10 = Schlägerei,", LX0 + 75, LY0 + 225, "l4", "Bold", 28, rechts=LX0 + 785),
    z("Schläge gegen den Kopf nicht ausgeschlossen", LX0 + 75, LY0 + 265, beim("l4", "Schläge"), size=28, rechts=LX0 + 785),
    *neinz("2 Schiedsrichter: keine sichere Begrenzung", LY0 + 330, "l5", "Bold", 28, x=LX0 + 75, rechts=LX0 + 785, gr=16),
    pl("nach dem BGH: sittenwidrig", LX0 + 30, LY0 + 420, "l6", fill=HELLROT, size=32),
])

# ===========================================================================================================================
# K Ergebnis
# ===========================================================================================================================
folie([("erg", "Ergebnis · Einwilligung unwirksam"), ("erg2", "Ergebnis · strafbar, §§ 223, 224 Abs. 1 Nr. 4 StGB"),
       ("p231c", "Ergebnis · § 231 StGB nur bei schwerer Folge")], [
    *tafel("erg", "Ergebnis"),
    blk(110, 170, 1040, 120, HELLROT, "erg", [("Die Einwilligung ist unwirksam,", "ExtraBold", 34, INK),
                                            ("die Körperverletzungen sind rechtswidrig.", "ExtraBold", 34, INK)]),
    *okz("schuldhaft: strafbar wegen gefährlicher", 340, "erg2", "Bold", 34, x=160),
    z("Körperverletzung, §§ 223, 224 Abs. 1 Nr. 4 StGB", 160, 388, beim("erg2", "gefährlicher"), "Bold", 34),
    z("§ 231 selbst: nur bestraft, wenn ein Mensch stirbt", 160, 470, "p231c", size=34),
    z("oder eine schwere Körperverletzung eintritt", 160, 516, beim("p231c", "schwere"), size=34),
    zit("§ 231 Abs. 1 StGB; BGHSt 60, 166, Rn. 44, 48", 160, 564, beim("p231c", "schwere")),
    *requisit([("erg", ("tabler", "scale", 110, HELLROT), "rechtswidrig", HELLROT),
               ("erg2", ("tabler", "gavel", 120, HOLZ), "strafbar", WEISS),
               ("p231c", ("tabler", "book", 100, WEISS), "§ 231 StGB", WEISS)]),
    *paar("SO", [("erg", "ernst")], "IN", [("erg", "ernst"), ("p231c", "denkt")]),
])

# ===========================================================================================================================
# L Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Prüfungsort: Rechtswidrigkeit"), ("tipp2", "Klausurtipp · Gruppen: Eskalationsgefahr")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Sittenwidrigkeit prüfst du in der", 200, 200, beim("tipp", "Sittenwidrigkeit"), "Bold", 36),
    z("Rechtswidrigkeit,", 200, 250, beim("tipp", "Rechtswidrigkeit"), "Bold", 36),
    z("als Grenze der Einwilligung", 200, 300, beim("tipp", "Grenze"), size=34),
    linienzug([(130, 380), (1130, 380)], "tipp2", breite=3),
    *neinz("nicht nur den einzelnen Schlag bewerten,", 410, beim("tipp2", "nicht"), size=34, x=200),
    *okz("sondern die Eskalationsgefahr", 470, beim("tipp2", "Eskalationsgefahr"), "Bold", 36, x=200),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# M Prüfschema
# ===========================================================================================================================
REIHEN = [("k1", 0, "I. Tatbestand: §§ 223, 224 Abs. 1 Nr. 4 StGB", True),
          ("k2", 0, "II. Rechtswidrigkeit", True),
          ("k2a", 1, "1. Voraussetzungen der Einwilligung", False),
          ("k2b", 1, "2. keine Sittenwidrigkeit, § 228 StGB:", False),
          (beim("k2b", "Gewicht"), 2, "Gewicht der Verletzung und Gefahr, Sicht vor der Tat", False),
          ("k2c", 2, "bei Gruppen: Eskalationsgefahr, Absprachen und", False),
          (beim("k2c", "Absprachen"), 2, "Sicherungen, Wertung des § 231 StGB", False),
          ("k3", 0, "III. Schuld", True)]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Prüfschema: Körperverletzung mit Einwilligung"), 110, 90, "sch", 46)]
y = 210
for c, ebene, text, fett in REIHEN:
    x = (130, 200, 260)[ebene]
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 40 if ebene == 0 else 36, rechts=1800))
    y += {0: 92, 1: 80, 2: 72}[ebene]
assert y <= 970, y
folie([("sch", "Prüfschema"), ("k1", "Prüfschema › I. Tatbestand"), ("k2", "Prüfschema › II. Rechtswidrigkeit"),
       ("k2a", "Prüfschema › II. 1. Einwilligung"), ("k2b", "Prüfschema › II. 2. keine Sittenwidrigkeit"),
       ("k2c", "Prüfschema › II. 2. bei Gruppen"), ("k3", "Prüfschema › III. Schuld")], els_sch)

# ===========================================================================================================================
# N Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("§ 228 StGB ist die ", 0), ("Grenze", "a")], [("der Einwilligung.", 0)]], 750, 290, 42, "merke",
                {"a": beim("merke", "Grenze")}),
    *markertext([[("Bei verabredeten Schlägereien zwischen", 0)], [("Gruppen ist die Tat ", 0), ("sittenwidrig", "b"), (",", 0)],
                 [("wenn wirksame Absprachen und effektive", 0)], [("Sicherungen gegen die Eskalation fehlen.", 0)]],
                750, 470, 42, "m2", {"b": beim("m2", "sittenwidrig")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
