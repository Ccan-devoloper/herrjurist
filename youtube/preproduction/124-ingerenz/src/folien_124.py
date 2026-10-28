"""Folge 124 · Ingerenz: Wer die Gefahr schafft, muss sie beseitigen – § 13 StGB – Serienstandard Open Peeps (Katzenkönig).
Beispielfall: Eckhard fährt im Dorf mit 70 statt 50 km/h, bremst zu spät und erfasst einen älteren Fußgänger, der schwer
verletzt am Straßenrand liegt. Eckhard hält an, sieht ihn, fährt weiter (will nicht entdeckt werden, nimmt den Tod in Kauf).
Eine Radfahrerin findet den Mann und ruft den Rettungsdienst; er überlebt.
Szenen laut ../SZENENPLAN.md: A1 Dorfstraße, A2 Radfahrerin, B Sachverhalt, C Fahrt und Weiterfahren, D Wortlautkarte § 13
Abs. 1 und Ingerenz, E Ingerenz im Fall, F Entsprechung/Vorsatz/Ansetzen/Rücktritt, G Wortlautkarte § 211 Abs. 2 und
Verdeckungsabsicht, H Streit „Verdecken durch Unterlassen“, I Wortlautkarte § 142 Abs. 1, § 323c, Konkurrenzen, J Ergebnis,
K Klausurtipp (Lexi), L Prüfschema, M Merksatz (Lexi).
DARSTELLUNG: kein Blut, keine Verletzungsdetails, kein Aufprall im Bild – nur Auto, Bremsspur-Strich, Warnsymbol, der
Fußgänger liegt ruhig (gedrehte Open-Peeps-Figur), danach Krankenwagen-Icon. Drei Handlungsgeräusche (Bremsen, Einsteigen und
Wegfahren, Fahrradklingel; ../geraeusche_herkunft.json).
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz als
eigene Kopie aus Folge 115 (gemeinsame Dateien unverändert); neu: strasse(), schild50(), bremsspur().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from ostil import mond, laterne, lichtkegel
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_124/"

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
        if n.startswith(("bild:", "ficon:", "bank")) or "/op_124/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def wortlaut(x, y, w, zeilen, quelle, cue, marken=(), size=32, bis=None):
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 03.10.2026), als Zitat mit Normangabe;
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
GRAUSTR = (206, 206, 202, 255)
GRAS = (205, 234, 196, 255)
STR_O, STR_U = 690, 850                      # Fahrbahn (Seitenansicht): Oberkante, Unterkante
FAHR = 832                                   # Unterkante der Autos und der stehenden Figuren auf der Fahrbahn
RANDU = 968                                  # Unterkante des liegenden Fußgängers auf dem Grünstreifen


def strasse(cue):
    """Dorfstraße in Seitenansicht: graue Fahrbahn mit Mittellinie, Grünstreifen davor (für jede Folie neu erzeugt)."""
    s = 2
    im = Image.new("RGBA", (1860 * s, (1000 - STR_O) * s))
    dr = ImageDraw.Draw(im)
    dr.rectangle((0, 0, 1860 * s, (STR_U - STR_O) * s), fill=GRAUSTR)
    dr.line((0, 0, 1860 * s, 0), fill=INK, width=6 * s)
    dr.line((0, (STR_U - STR_O) * s, 1860 * s, (STR_U - STR_O) * s), fill=INK, width=6 * s)
    for x in range(30, 1860, 150):
        dr.rounded_rectangle((x * s, 74 * s, (x + 80) * s, 86 * s), 5 * s, fill=WEISS)
    dr.rectangle((0, (STR_U - STR_O + 3) * s, 1860 * s, (1000 - STR_O) * s), fill=GRAS)
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    return hart(El(im, 30, STR_O, cue, "cut", 0.0, None, name="strasse")) if cue == NULL else \
        El(im, 30, STR_O, cue, "cut", 0.0, None, name="strasse")


def schild50(cx, boden_, cue):
    """Tempo-50-Schild (Grundform: weißer Kreis, roter Ring, Ziffern, Pfosten)."""
    s = 2
    r, hp = 62, 150
    im = Image.new("RGBA", ((2 * r + 12) * s, (2 * r + hp + 12) * s))
    dr = ImageDraw.Draw(im)
    dr.rounded_rectangle(((r - 2) * s, (2 * r) * s, (r + 14) * s, (2 * r + hp + 6) * s), 4 * s, fill=(150, 150, 150, 255),
                         outline=INK, width=3 * s)
    dr.ellipse((6 * s, 6 * s, (2 * r + 6) * s, (2 * r + 6) * s), fill=WEISS, outline=INK, width=4 * s)
    dr.ellipse((13 * s, 13 * s, (2 * r - 1) * s, (2 * r - 1) * s), outline=DROT, width=14 * s)
    f = F("ExtraBold", 56 * s)
    b = f.getbbox("50")
    dr.text(((r + 6) * s - (b[2] - b[0]) / 2 - b[0], (r + 6) * s - (b[3] - b[1]) / 2 - b[1]), "50", font=f, fill=INK)
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    e = El(im, cx - im.width / 2, boden_ - im.height, cue, "cut", 0.0, None, name="schild50")
    return hart(e) if cue == NULL else e


def bremsspur(x0, x1, y, cue):
    """Bremsspur-Strich: zwei dunkle Linien auf der Fahrbahn hinter dem Auto."""
    return [linienzug([(x0, y), (x1, y)], cue, breite=9, farbe=INK),
            linienzug([(x0 + 40, y + 14), (x1 - 20, y + 14)], cue, breite=7, farbe=(60, 60, 60, 255))]


BODEN = 860
FH = 470                                    # stehende Figur auf der Fahrbahn
X1, X2 = 1430, 1730                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"EC": "Eckhard", "FU": "Fußgänger", "RA": "Radfahrerin"}
NFARBE = {"EC": GRUEN, "FU": LILA, "RA": GELB}


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


def stehend(k, x, folge):
    return [*fig(k, x, FB, FR, folge), ns(NAME[k], x, FB, folge[0][0], NFARBE[k], d=0.1)]


def dorf(c):
    """Kulisse: Häuser und Baum hinter der Fahrbahn, Tempo-50-Schild (für jede Folie neu erzeugt)."""
    h = (lambda e: hart(e)) if c == NULL else (lambda e: e)
    return [strasse(c),
            h(ficon("tabler", "home", 1300, STR_O + 4, 200, c, fuell=GELB, anim="cut")),
            h(ficon("tabler", "home", 1500, STR_O + 4, 170, c, fuell=ROT, anim="cut")),
            h(ficon("tabler", "tree", 1680, STR_O + 4, 190, c, fuell=GRUEN, anim="cut")),
            schild50(1830, STR_O + 4, c)]


# ===========================================================================================================================
# A1 Fall: die Dorfstraße
# ===========================================================================================================================
CW = 380                                     # Autobreite
CA, CS, CE = 430, 700, 1640                  # Auto: Start, Halt nach dem Bremsen, Ziel beim Wegfahren
FUX = 1020                                   # Fußgänger auf der Fahrbahn
LGX = 1390                                   # liegt auf dem Grünstreifen
ECX = 990                                    # Eckhard steigt aus, neben dem Auto
ERF = beim("brems", "erfasst")
BREMS = beim("brems", "bremst")
EIN = beim("weg", "steigt")
WEG_F = beim("weg", "fährt")
WEG_DA = ("weg", round(WEG_F[1] + 1.6, 3))
LH = 150                                     # Höhe (Dicke) der liegenden Figur
folie([(NULL, "Fall · Auf der Dorfstraße"), ("fuss", "Fall · Der Fußgänger"), ("liegt", "Fall · Am Straßenrand"),
       ("aus", "Fall · Eckhard hält an"), ("weg", "Fall · Eckhard fährt weiter")], [
    *dorf(NULL),
    hart(pl("Ein Sonntagnachmittag im Dorf", 70, 30, NULL, fill=GELB, size=40)),
    # das Auto: fährt zu schnell, bremst zu spät, steht; Eckhard steigt aus, steigt wieder ein und fährt weiter
    hart(ficon("tabler", "car", CA, FAHR, CW, NULL, fuell=BLAU, anim="cut", bis=BREMS)),
    pl("70 statt 50 km/h", 70, 120, "schnell", fill=HELLROT, size=36),
    ficon("tabler", "gauge", 470, 175, 90, beim("schnell", "siebzig"), fuell=ROT),
    szene(bewegt(ficon("tabler", "car", CS, FAHR, CW, BREMS, fuell=BLAU, anim="cut", bis=WEG_F), BREMS, ERF, CA - CS, 0),
          "124bremse*", 0.9, 0.0),
    *[bis_(e, WEG_F) for e in bremsspur(CA - 230, CS - 150, FAHR - 2, ERF)],
    pl("bremst zu spät", 70, 200, BREMS, fill=WEISS, size=34),
    # der Fußgänger überquert die Straße (blickt nach links zum Auto), liegt danach ruhig auf dem Grünstreifen
    peep_voll("FU_ruhig", FUX, FAHR, FH - 20, "fuss", anim="pop", bis=ERF),
    bis_(ns("Fußgänger", FUX, FAHR, "fuss", LILA, d=0.1), ERF),
    peep_voll("FU_liegt", LGX, RANDU, LH, ERF, anim="cut"),
    ns("Fußgänger", LGX, RANDU, ERF, LILA, anim="cut"),
    ficon("tabler", "alert-triangle", LGX + 40, RANDU - LH - 6, 80, ERF, fuell=GELB),
    pl("mit 50 km/h: rechtzeitig gehalten", 70, 280, "halt", fill=WEISS, size=32, bis="liegt"),
    pl("schwer verletzt am Straßenrand", 70, 280, "liegt", fill=WEISS, size=34),
    pl("ohne schnelle Hilfe: Lebensgefahr", 70, 360, "gefahr", fill=HELLROT, size=34),
    # Eckhard steigt aus (blickt nach rechts zum Fußgänger), redet, steigt wieder ein
    *fig("EC", ECX, FAHR, FH, [("aus", "ruhig_r"), (beim("aus", "sieht"), "schreck_r")], bis="e1", erst="pop"),
    *redet("EC_redet_r", ECX, FAHR, FH, "e1", "weg"),
    bis_(peep_voll("EC_denkt_r", ECX, FAHR, FH, "weg", anim="cut"), EIN),
    bis_(ns("Eckhard", ECX, FAHR, "aus", GRUEN, d=0.1), EIN),
    blase("sprech", 620, 200, "e1", 1420, 230, inhalt=["Wenn ich jetzt Hilfe", "rufe, bin ich dran."], textsize=36,
          figur=("EC_redet_r", ECX, FAHR, FH), bis="weg"),
    szene(bewegt(ficon("tabler", "car", CE, FAHR, CW, WEG_F, fuell=BLAU, anim="cut", bis=WEG_DA), WEG_F, WEG_DA, CS - CE, 0),
          "124wegfahrt*", 0.8, round(EIN[1] - WEG_F[1], 3)),
    pl("fährt weiter", 70, 440, WEG_F, fill=GELB, size=34),
    pl("will nicht entdeckt werden", 70, 520, "vors", fill=WEISS, size=34),
    pl("Tod für möglich gehalten, in Kauf genommen", 70, 600, "tod", fill=HELLROT, size=34),
])

# ===========================================================================================================================
# A2 Fall: die Radfahrerin
# ===========================================================================================================================
RAX = 1000                                   # Radfahrerin hält auf der Fahrbahn (blickt nach rechts zum Mann)
RH = 430                                     # Höhe der Figur auf dem Fahrrad
RAD_DA = ("rad", 1.4)
KLINIK_K = beim("klinik", "Krankenhaus")
folie([("rad", "Fall · Die Radfahrerin"), ("klinik", "Fall · Im Krankenhaus"), ("frage", "Fall · Die Frage")], [
    *dorf("rad"),
    pl("10 Minuten später", 70, 30, "rad", fill=GELB, size=40),
    ficon("tabler", "clock", 500, 92, 64, "rad", fuell=WEISS),
    peep_voll("FU_liegt", LGX, RANDU, LH, "rad", anim="cut"),
    ns("Fußgänger", LGX, RANDU, "rad", LILA, anim="cut"),
    # die Radfahrerin kommt von links und hält beim Mann (blickt nach rechts zu ihm)
    szene(bewegt(peep_voll("RA_schreck_r", RAX, FAHR, RH, "rad", anim="cut", bis="r1"), "rad", RAD_DA, -760, 0),
          "124klingel*", 0.6, 0.15),
    bewegt(ns("Radfahrerin", RAX, FAHR, "rad", GELB, anim="cut"), "rad", RAD_DA, -760, 0),
    *redet("RA_redet_r", RAX, FAHR, RH, "r1", "klinik"),
    peep_voll("RA_ruhig_r", RAX, FAHR, RH, "klinik", anim="cut"),
    blase("sprech", 640, 200, "r1", 1380, 250, inhalt=["Hier liegt ein verletzter Mann.", "Bitte kommen Sie schnell!"],
          textsize=34, figur=("RA_redet_r", RAX, FAHR, RH), bis="klinik"),
    ficon("tabler", "phone-call", RAX + 60, 380, 64, "r1", fuell=WEISS),
    # Rettungsdienst und Krankenhaus: Er überlebt
    ficon("fluent-emoji-flat", "ambulance", 520, FAHR, 300, KLINIK_K),
    pl("Krankenhaus: Er überlebt.", 70, 120, beim("klinik", "überlebt"), fill=GRUEN, size=34),
    pl("nur fahrlässig angefahren: helfen müssen?", 70, 200, "frage", fill=WEISS, size=34),
    pl("Sogar Mord durch Unterlassen?", 70, 285, "frage2", fill=PINK, size=36),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_124(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=34, zeilenabstand=1.30)
        els += e; y += 18
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_124("sv", [
    "An einem Sonntagnachmittag fährt Eckhard mit seinem Auto durch ein Dorf, mit 70 km/h statt der erlaubten 50 km/h. "
    "Ein älterer Mann, den Eckhard nicht kennt, überquert die Straße. Eckhard bremst zu spät und erfasst ihn. Mit 50 km/h "
    "hätte er rechtzeitig halten können. Der Mann liegt schwer verletzt am Straßenrand; ohne schnelle Hilfe droht er zu "
    "sterben.",
    "Eckhard hält an, steigt aus und sieht ihn liegen. Er sagt sich: „Wenn ich jetzt Hilfe rufe, bin ich dran.“ Er steigt "
    "wieder ein und fährt weiter, weil er nicht als Unfallverursacher entdeckt werden will. Dass der Mann ohne Hilfe "
    "stirbt, hält er für möglich und nimmt es in Kauf.",
    "Zehn Minuten später findet eine Radfahrerin den Mann und ruft den Rettungsdienst. Der Mann wird im Krankenhaus "
    "behandelt und überlebt.",
], "Wie hat sich Eckhard strafbar gemacht?")

# ===========================================================================================================================
# C Die Fahrt (§ 229) und das Weiterfahren (Unterlassen)
# ===========================================================================================================================
PA = "A. Fahrt"
PB = "B. Versuchter Totschlag durch Unterlassen"
PC = "C. Mordmerkmal Verdeckungsabsicht"
folie([("fahrt", f"{PA} › fahrlässige Körperverletzung, § 229 StGB"), ("kern", "B. Weiterfahren › Tun oder Unterlassen?"),
       ("delikt", f"{PB}, §§ 212, 22, 23 Abs. 1, 13 StGB"), ("versuch", f"{PB} › Versuch: Mann überlebt")], rechts_frei([
    *tafel("fahrt", "Fahrt und Weiterfahren"),
    z("A. Die Fahrt: zu schnell, Mann verletzt", 110, 180, "fahrt", "Bold", 34),
    *okz("fahrlässige Körperverletzung, § 229 StGB", 240, beim("fahrt", "fahrlässige"), "Bold", 34, x=160),
    linienzug([(130, 320), (1130, 320)], "kern", breite=3),
    z("B. Das Weiterfahren:", 110, 350, "kern", "Bold", 34),
    z("kein Tun, sondern Unterlassen: keine Hilfe gerufen", 160, 405, beim("kern", "Unterlassen"), size=32),
    blk(110, 480, 1040, 80, GELB, "delikt", [("Versuchter Totschlag durch Unterlassen", "ExtraBold", 36, INK)]),
    z("Versuch: Der Mann überlebt.", 110, 600, "versuch", "Bold", 34),
    z("Schema: Video „Versuch“", 110, 655, beim("versuch", "Wie"), "Bold", 32, farbe=TEXT),
    *requisit([("fahrt", ("tabler", "car", 150, BLAU), "§ 229 StGB", WEISS),
               ("kern", ("tabler", "phone-call", 100, WEISS), "keine Hilfe gerufen", HELLROT),
               ("delikt", ("tabler", "scale", 100, GELB), "§§ 212, 13 StGB", GELB),
               ("versuch", ("fluent-emoji-flat", "ambulance", 150, None), "Mann überlebt", GRUEN)]),
    *stehend("EC", FX, [("fahrt", "ruhig"), ("kern", "denkt")]),
]))

# ===========================================================================================================================
# D Wortlautkarte § 13 Abs. 1 (Auszug), Garant? Ingerenz
# ===========================================================================================================================
W13 = ["„Wer es unterläßt, einen Erfolg abzuwenden, der zum",
       "Tatbestand eines Strafgesetzes gehört, ist nach diesem",
       "Gesetz nur dann strafbar, wenn er rechtlich dafür",
       "einzustehen hat, daß der Erfolg nicht eintritt, …“"]
w13, w13_y = wortlaut(80, 170, 1100, W13, "§ 13 Abs. 1 StGB (Auszug)", "p13", marken=[
    (0, "einen Erfolg abzuwenden", beim("p13", "Erfolg")), (2, "rechtlich dafür", beim("einst", "rechtlich")),
    (3, "einzustehen hat", beim("einst", "einzustehen"))], size=34)
PG = f"{PB} › Garantenstellung"
folie([("p13", f"{PG} › § 13 Abs. 1 StGB"), ("garant", f"{PG} › Familie? Übernahme?"), ("ing", f"{PG} › Ingerenz")],
      rechts_frei([
    *tafel("p13", "Die Norm: § 13 Abs. 1 StGB"),
    *w13,
    *neinz("Familie oder Übernahme: scheiden aus", w13_y + 30, beim("garant", "Familie"), "Bold", 34, x=160),
    z("Überblick: Video „Garantenstellung“", 160, w13_y + 82, beim("garant", "Überblick"), "Bold", 30, farbe=TEXT),
    z("In Betracht kommt die Ingerenz:", 110, w13_y + 150, "ing", "Bold", 34),
    blk(110, w13_y + 205, 1040, 120, LILA, "ing2", [("pflichtwidriges Vorverhalten schafft die", "ExtraBold", 34, INK),
                                                   ("nahe Gefahr des Erfolgs", "ExtraBold", 34, INK)]),
    zit("BGH, Beschl. v. 24.3.2021 – 4 StR 416/20, Rn. 22", 110, w13_y + 340, "ing2"),
    *requisit([("p13", ("tabler", "book", 100, WEISS), "§ 13 Abs. 1 StGB", GELB),
               ("einst", ("tabler", "shield", 100, BLAU), "rechtlich einstehen", WEISS),
               ("garant", ("tabler", "help-circle", 100, WEISS), "Garant?", PINK),
               ("ing", ("tabler", "alert-triangle", 100, GELB), "Ingerenz", LILA)]),
    *stehend("EC", FX, [("p13", "ruhig"), ("ing", "sorge")]),
]))

# ===========================================================================================================================
# E Ingerenz im Fall; Abgrenzung verkehrsgerechtes Verhalten
# ===========================================================================================================================
folie([("pfl", f"{PG} › pflichtwidriges Vorverhalten"), ("nahe", f"{PG} › nahe Gefahr"),
       ("garant2", f"{PG} › Garant aus Ingerenz (+)"), ("verkehr", f"{PG} › Abgrenzung: verkehrsgerechtes Verhalten")],
      rechts_frei([
    *tafel("pfl", "Ingerenz im Fall"),
    z("Eckhard: 20 km/h zu schnell", 110, 180, "pfl", "Bold", 34),
    zit("§ 3 Abs. 3 Nr. 1 StVO: innerorts 50 km/h", 110, 228, "pfl"),
    *okz("pflichtwidriges Vorverhalten", 280, beim("pfl", "pflichtwidrig"), "Bold", 34, x=160),
    *okz("nahe Gefahr: Der Mann kann sterben.", 350, beim("nahe", "nahe"), "Bold", 34, x=160),
    blk(110, 430, 1040, 80, GRUEN, "garant2", [("Eckhard: Garant aus Ingerenz", "ExtraBold", 36, INK)]),
    linienzug([(130, 550), (1130, 550)], "verkehr", breite=3),
    *neinz("verkehrsgerecht verhalten: nicht pflichtwidrig", 580, beim("verkehr", "verkehrsgerecht"), "Bold", 34, x=160),
    z("Unfall macht dann nicht zum Garanten aus Ingerenz", 160, 635, beim("verkehr", "Unfall"), size=32),
    zit("vgl. 4 StR 416/20, Rn. 22; BGH, Urt. v. 11.9.2019 – 2 StR 563/18, Rn. 19, 21 f.", 160, 690,
        beim("verkehr", "Garanten")),
    *requisit([("pfl", ("tabler", "gauge", 100, ROT), "70 statt 50 km/h", HELLROT),
               ("nahe", ("tabler", "alert-triangle", 100, GELB), "Lebensgefahr", HELLROT),
               ("garant2", ("tabler", "shield-check", 100, GRUEN), "Garant (+)", GRUEN),
               ("verkehr", ("tabler", "traffic-lights", 100, WEISS), "verkehrsgerecht?", WEISS)]),
    *stehend("EC", FX, [("pfl", "still"), ("garant2", "sorge"), ("verkehr", "ruhig")]),
]))

# ===========================================================================================================================
# F Entsprechung, Vorsatz, unmittelbares Ansetzen, Rücktritt
# ===========================================================================================================================
folie([("entspr", f"{PB} › Entsprechung"), ("vors2", f"{PB} › Tatentschluss: Vorsatz"),
       ("ansetz", f"{PB} › unmittelbares Ansetzen"), ("rueck", f"{PB} › Rücktritt (−)")], rechts_frei([
    *tafel("entspr", "Entsprechung, Vorsatz, Ansetzen"),
    *okz("Entsprechung: beim Tötungsdelikt unproblematisch", 180, beim("entspr", "unproblematisch"), "Bold", 32, x=160),
    *okz("Vorsatz: Tod und Rettung per Notruf für möglich", 255, "vors2", "Bold", 32, x=160),
    z("gehalten, Tod in Kauf genommen: bedingter Vorsatz", 160, 300, beim("vors2", "nimmt"), "Bold", 32),
    zit("BGH, Urt. v. 19.8.2020 – 1 StR 474/19, Rn. 14, 16", 160, 350, beim("vors2", "Das")),
    *okz("unmittelbares Ansetzen: beim Wegfahren", 420, "ansetz", "Bold", 32, x=160),
    z("schon Lebensgefahr, Rettung aus der Hand gegeben", 160, 465, beim("ansetz", "Der"), size=32),
    *neinz("Rücktritt: kein Bemühen um Rettung", 545, "rueck", "Bold", 32, x=160),
    zit("§ 24 Abs. 1 S. 2 StGB", 160, 595, beim("rueck", "Eckhard")),
    *requisit([("entspr", ("tabler", "scale", 100, WEISS), "Entsprechung", WEISS),
               ("vors2", ("tabler", "bulb", 100, GELB), "bedingter Vorsatz", GELB),
               ("ansetz", ("tabler", "car", 150, BLAU), "Wegfahren", HELLROT),
               ("rueck", ("tabler", "shield-x", 100, WEISS), "kein Rücktritt", HELLROT)]),
    *stehend("EC", FX, [("entspr", "ruhig"), ("vors2", "denkt"), ("ansetz", "still")]),
]))

# ===========================================================================================================================
# G Wortlautkarte § 211 Abs. 2 (Auszug), Verdeckungsabsicht
# ===========================================================================================================================
W211 = ["„Mörder ist, wer … um eine andere Straftat zu",
        "ermöglichen oder zu verdecken, einen Menschen tötet.“"]
w211, w211_y = wortlaut(80, 170, 1100, W211, "§ 211 Abs. 2 StGB (Auszug)", "p211", marken=[
    (0, "andere Straftat", beim("p211", "andere")), (1, "verdecken", beim("p211", "verdecken")),
    (1, "einen Menschen tötet", beim("p211", "Menschen"))], size=34)
folie([("mord", f"{PC}, § 211 Abs. 2 StGB"), ("vortat", f"{PC} › andere Straftat"),
       ("entd", f"{PC} › nicht entdeckt werden"), ("bed", f"{PC} › bedingter Tötungsvorsatz genügt")], rechts_frei([
    *tafel("mord", "Und Mord? Verdeckungsabsicht"),
    *w211,
    *okz("andere Straftat: fahrlässige Körperverletzung", w211_y + 30, "vortat", "Bold", 34, x=160),
    *okz("Ziel: nicht als Täter entdeckt werden", w211_y + 100, "entd", "Bold", 34, x=160),
    *okz("nur bedingter Tötungsvorsatz: schadet nicht", w211_y + 170, beim("bed", "schadet"), "Bold", 34, x=160),
    z("Die Flucht verdeckt auch, wenn der Mann überlebt;", 160, w211_y + 225, beim("bed", "Nach"), size=32),
    z("der Mann kennt ihn nicht.", 160, w211_y + 270, beim("bed", "denn"), size=32),
    zit("BGH, Urt. v. 15.2.2018 – 4 StR 361/17, Rn. 11, 14; 4 StR 297/02, Rn. 6", 160,
        w211_y + 325, beim("bed", "Nach")),
    *requisit([("mord", ("tabler", "book", 100, WEISS), "§ 211 Abs. 2 StGB", GELB),
               ("vortat", ("tabler", "car", 150, BLAU), "§ 229 StGB", WEISS),
               ("entd", ("tabler", "eye-off", 100, WEISS), "unentdeckt bleiben", HELLROT),
               ("bed", ("tabler", "bulb", 100, GELB), "bedingter Vorsatz", GELB)]),
    *stehend("EC", FX, [("mord", "ruhig"), ("entd", "denkt"), ("bed", "still")]),
]))

# ===========================================================================================================================
# H Streit: Verdecken durch Unterlassen?
# ===========================================================================================================================
LX0, RX0, SW = 110, 640, 510
folie([("streit", f"{PC} › Streit: Verdecken durch Unterlassen?"), ("entsch", f"{PC} › Stellungnahme"),
       ("verd", f"{PC} › Verdeckungsabsicht (+)"), ("milder", "Strafmilderung · § 13 Abs. 2 StGB")], rechts_frei([
    *tafel("streit", "Verdecken durch Unterlassen?"),
    karte(LX0, 180, SW, 250, "alt", fill=HELLROT, rund=18, schatten=6, rand=4),
    z("früher: BGH, Teile der Lehre", LX0 + 25, 195, "alt", "ExtraBold", 30, rechts=LX0 + SW - 10),
    z("bloßes Wegfahren", LX0 + 25, 260, beim("alt", "Wer"), size=30, rechts=LX0 + SW - 10),
    z("deckt nur nicht auf", LX0 + 25, 302, beim("alt", "decke"), size=30, rechts=LX0 + SW - 10),
    z("also kein Verdecken", LX0 + 25, 360, beim("alt", "decke"), "Bold", 30, rechts=LX0 + SW - 10),
    karte(RX0, 180, SW, 250, "neu", fill=HELLGRUEN, rund=18, schatten=6, rand=4),
    z("heute: BGH, herrschende Lehre", RX0 + 25, 195, "neu", "ExtraBold", 30, rechts=RX0 + SW - 10),
    z("Verdecken auch durch", RX0 + 25, 260, beim("neu", "Verdecken"), size=30, rechts=RX0 + SW - 10),
    z("Unterlassen möglich", RX0 + 25, 302, beim("neu", "Verdecken"), size=30, rechts=RX0 + SW - 10),
    z("4 StR 297/02, Rn. 6", RX0 + 25, 365, beim("neu", "Verdecken"), size=26, farbe=TEXT, rechts=RX0 + SW - 10),
    z("Stellungnahme:", 110, 465, "entsch", "Bold", 34),
    *okz("Wortlaut verlangt kein aktives Tun", 520, beim("entsch", "Wortlaut"), "Bold", 32, x=160),
    *okz("keine Selbstanzeige, nur Notruf (auch anonym)", 580, beim("entsch", "Selbstanzeige"), "Bold", 32, x=160),
    zit("vgl. BGH, Beschl. v. 10.3.2000 – 1 StR 675/99, Rn. 21;", 160, 628, beim("entsch", "Selbstanzeige")),
    zit("Kaspar/Broichmann, ZJS 2013, 346, 351 f.", 160, 662, beim("entsch", "Selbstanzeige")),
    blk(110, 715, 1040, 80, GRUEN, "verd", [("Eckhard: Verdeckungsabsicht (+)", "ExtraBold", 36, INK)]),
    z("Strafmilderung möglich: § 13 Abs. 2 StGB", 110, 820, "milder", "Bold", 32),
    *requisit([("streit", ("tabler", "arrows-split", 100, WEISS), "Streit", WEISS),
               ("entsch", ("tabler", "scale", 100, GELB), "Stellungnahme", GELB),
               ("verd", ("tabler", "eye-off", 100, WEISS), "Verdeckung (+)", GRUEN),
               ("milder", ("tabler", "scale", 100, WEISS), "kann gemildert werden", WEISS)]),
    *stehend("EC", FX, [("streit", "ruhig"), ("verd", "still")]),
]))

# ===========================================================================================================================
# I Wortlautkarte § 142 Abs. 1 (Auszug), § 323c tritt zurück, Konkurrenzen
# ===========================================================================================================================
W142 = ["„Ein Unfallbeteiligter, der sich nach einem Unfall im Straßen-",
        "verkehr vom Unfallort entfernt, bevor er 1. … die Feststellung",
        "seiner Person, … ermöglicht hat oder 2. eine nach den",
        "Umständen angemessene Zeit gewartet hat, …, wird mit",
        "Freiheitsstrafe bis zu drei Jahren oder mit Geldstrafe bestraft.“"]
w142, w142_y = wortlaut(80, 165, 1100, W142, "§ 142 Abs. 1 StGB (Auszug)", "p142", marken=[
    (1, "vom Unfallort entfernt", beim("p142", "Unfallort")), (1, "Feststellung", beim("p142b", "Feststellung")),
    (3, "angemessene Zeit gewartet", beim("p142b", "angemessen"))], size=30)
PD = "D. Unerlaubtes Entfernen vom Unfallort, § 142 Abs. 1 StGB"
folie([("p142", PD), ("p323", "Konkurrenzen · § 323c StGB tritt zurück"), ("konk", "Konkurrenzen · §§ 52, 53 StGB")],
      rechts_frei([
    *tafel("p142", "Unfallort, § 323c, Konkurrenzen"),
    *w142,
    *okz("weggefahren: keine Feststellung, nicht gewartet", w142_y + 20, beim("p142b", "weggefahren"), "Bold", 32, x=160),
    z("§ 323c StGB tritt hinter dem versuchten Mord zurück", 110, w142_y + 95, "p323", "Bold", 32),
    zit("vgl. BGH, Urt. v. 23.7.2015 – 3 StR 633/14, Rn. 21", 110, w142_y + 142, beim("p323", "tritt")),
    z("versuchter Mord und § 142: Tateinheit, § 52 StGB", 110, w142_y + 200, "konk", "Bold", 32),
    z("fahrlässige Körperverletzung dazu: Tatmehrheit, § 53 StGB", 110, w142_y + 248, beim("konk", "fahrlässige"),
      "Bold", 32),
    *requisit([("p142", ("tabler", "car", 150, BLAU), "vom Unfallort entfernt", HELLROT),
               ("p323", ("tabler", "first-aid-kit", 100, ROT), "§ 323c StGB", WEISS),
               ("konk", ("tabler", "link", 100, WEISS), "Konkurrenzen", WEISS)]),
    *stehend("EC", FX, [("p142", "denkt"), ("p323", "ruhig")]),
]))

# ===========================================================================================================================
# J Ergebnis
# ===========================================================================================================================
folie([("erg", "Ergebnis · Eckhard strafbar, §§ 229; 211, 22, 23 Abs. 1, 13; 142 Abs. 1, 52, 53 StGB")], rechts_frei([
    *tafel("erg", "Ergebnis"),
    z("Eckhard ist strafbar wegen", 110, 190, "erg", "Bold", 36),
    blk(110, 260, 1040, 80, GELB, beim("erg", "fahrlässiger"), [("fahrlässiger Körperverletzung", "ExtraBold", 36, INK)]),
    z("und wegen", 110, 365, beim("erg", "und"), "Bold", 34),
    blk(110, 425, 1040, 120, GRUEN, beim("erg", "versuchten"), [("versuchten Mordes durch Unterlassen", "ExtraBold", 36, INK),
                                                              ("in Tateinheit mit", "ExtraBold", 36, INK)]),
    blk(110, 570, 1040, 80, LILA, beim("erg", "unerlaubtem"), [("unerlaubtem Entfernen vom Unfallort", "ExtraBold", 36, INK)]),
    *requisit([("erg", ("tabler", "gavel", 100, HOLZ), "Ergebnis", GRUEN)]),
    *stehend("EC", FX, [("erg", "still")]),
]))

# ===========================================================================================================================
# K Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Tun und Unterlassen trennen"), ("tipp2", "Klausurtipp · andere Straftat?")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Trenne die Fahrt als Tun", 200, 200, beim("tipp", "Trenne"), "Bold", 36),
    z("vom Weiterfahren als Unterlassen", 200, 250, beim("tipp", "Weiterfahren"), size=34),
    linienzug([(130, 330), (1130, 330)], "tipp2", breite=3),
    z("Verdeckungsmord durch Unterlassen:", 200, 360, "tipp2", "Bold", 36),
    z("Vortat schon mit Tötungsvorsatz begangen?", 200, 420, beim("tipp2", "ob"), size=34),
    z("Dann fehlt die andere Straftat.", 200, 475, beim("tipp2", "Dann"), "Bold", 34),
    zit("BGH, Urt. v. 12.12.2002 – 4 StR 297/02, Rn. 6, 11", 200, 535, beim("tipp2", "Dann")),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# L Prüfschema
# ===========================================================================================================================
REIHEN = [("s0", 0, "Vorprüfung: Tat nicht vollendet, Versuch strafbar", True),
          ("s1", 0, "I. Tatentschluss", True),
          ("s1a", 1, "Vorsatz: Tod, mögliche Rettung", False),
          ("s1b", 1, "Garantenstellung, hier aus Ingerenz:", True),
          ("s1b", 2, "pflichtwidriges Vorverhalten, nahe Gefahr des Erfolgs", False),
          ("s1c", 1, "Entsprechung", False),
          ("s1d", 1, "Mordmerkmal: Verdeckungsabsicht", False),
          ("s2", 0, "II. Unmittelbares Ansetzen", True),
          ("s3", 0, "III. Rechtswidrigkeit  ·  IV. Schuld", True),
          ("s5", 0, "V. Rücktritt  ·  Strafmilderung, § 13 Abs. 2 StGB", True)]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfschema: Versuchter Mord durch Unterlassen"), 110, 90, "sch", 46),
           z("§§ 211, 212, 22, 23 Abs. 1, 13 StGB", 110, 160, "sch", "Bold", 32, farbe=TEXT, rechts=1800)]
y = 230
for c, ebene, text, fett in REIHEN:
    x = (130, 200, 270)[ebene]
    if c == "s1b" and ebene == 1:
        els_sch.append(karte(180, y - 16, 1640, 140, c, fill=HELLGRUEN, rund=16, schatten=5, rand=4))
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 36 if ebene == 0 else 33, rechts=1800))
    y += {0: 80, 1: 64, 2: 78}[ebene]
assert y <= 970, y
folie([("sch", "Prüfschema"), ("s0", "Prüfschema › Vorprüfung"), ("s1", "Prüfschema › I. Tatentschluss"),
       ("s1b", "Prüfschema › I. Garantenstellung: Ingerenz"), ("s1d", "Prüfschema › I. Verdeckungsabsicht"),
       ("s2", "Prüfschema › II. Unmittelbares Ansetzen"), ("s3", "Prüfschema › III. und IV."),
       ("s5", "Prüfschema › V. Rücktritt, Strafmilderung")], els_sch)

# ===========================================================================================================================
# M Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Wer durch pflichtwidriges Verhalten", 0)], [("eine Lebensgefahr schafft,", 0)],
                 [("muss sie beseitigen", "a"), (".", 0)]], 750, 290, 44, "merke", {"a": beim("merke", "muss")}),
    *markertext([[("Fährt er weiter, um seine Tat", 0)], [("zu verdecken, droht ein", 0)],
                 [("Mord durch Unterlassen", "b"), (".", 0)]], 750, 580, 44, "m2", {"b": beim("m2", "Mord")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
