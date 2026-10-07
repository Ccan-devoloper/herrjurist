"""Folge 238 · Soldaten sind Mörder und ACAB: Wie deutet man Äußerungen? – Serienstandard Open Peeps (Katzenkönig).
Fiktiver Rahmen nach BVerfG (K), Beschl. v. 17.5.2016 – 1 BvR 2150/14 und 1 BvR 257/14: Fan Hannes hält mit Freunden im Fanblock
an der Brüstung ein Banner mit dem Kürzel ACAB hoch (Richtung Spielfeld); Polizistin Roth und ein Kollege sind am Spielfeldrand
im Einsatz; Roth stellt Strafantrag. Gegenfall: Hannes geht nach dem Spiel gezielt mit dem Banner zu den Beamten.
Szenen laut ../SZENENPLAN.md: A Stadion (Fall, Frage), B Sachverhalt, C Art. 5 Abs. 1 S. 1 GG (Wortlautkarte), D Das Kürzel:
Meinung, Eingriff, E Deutung (objektiver Sinn), F Mehrdeutige Äußerungen, G „Soldaten sind Mörder“, H Kollektivbeleidigung
(Skala), I ACAB-Kammerbeschlüsse, J Schranken (Wortlautkarten Art. 5 Abs. 2 GG, § 185 StGB), K Anwendung von § 185:
Wechselwirkung, § 193, L Ergebnis im Stadion, M Gegenfall am Stadionausgang, N Klausurtipp (Lexi), O Prüfschema,
P Merksatz (Lexi). Zwei Handlungsgeräusche (Stimmengewirr der Fans im Stadion, Schritte im Gegenfall; ../geraeusche_herkunft.json).
Darstellung: Das Kürzel steht nur auf dem Banner und als Fallbezeichnung auf Tafeln; die Bedeutung erscheint einmal sachlich auf
Deutsch in normaler Schreibung (Pille und Sachverhalt), nie in Großschrift. Keine Vereinsfarben, Logos, Waffen oder Helme.
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/umbruch/redet/fig/ns/okz/
neinz/requisit als eigene Kopie aus Folge 232 (gemeinsame Dateien unverändert); neu: stadion(), bruestung(), banner(),
ausgang(), skala().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut nach gesetze-im-internet.de, Abruf 07.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_238/"

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
HELLGRAU = (226, 226, 222, 255)
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
        assert g >= 26 and F(s, g).getlength(glyphen(t)) <= w - 30, f"Blockzeile zu breit: {t}"
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
        if n.startswith(("bild:", "ficon:")) or "/op_238/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def umbruch(text, size, breite, stil="Regular"):
    f = F(stil, size); zeilen, akt = [], ""
    for w in text.split(" "):
        t = (akt + " " + w).strip()
        if f.getlength(t) <= breite:
            akt = t
        else:
            zeilen.append(akt); akt = w
    return zeilen + [akt]


def wortlaut(x, y, w, text, quelle, cue, marken=(), size=32, bis=None):
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 07.10.2026), als Zitat mit Normangabe; der
    Zeilenumbruch wird berechnet. marken = [(wort, cue)] legt synchron zum gesprochenen Wort einen Textmarker hinter die
    erste noch nicht markierte Fundstelle von 'wort' (muss in einer Zeile stehen)."""
    zeilen = umbruch(glyphen(text), size, w - 60)
    lh = int(size * 1.42)
    hgt = 40 + lh * len(zeilen) + 46
    els = [bis_(karte(x, y, w, hgt, cue, fill=ZITAT, rund=18, schatten=6, rand=4), bis)]
    f = F("Regular", size)
    tx, ty = x + 28, y + 26
    belegt = []
    for wort, mc in marken:
        treffer = None
        for zi, t in enumerate(zeilen):
            a = t.find(wort)
            while a >= 0 and (zi, a) in belegt:
                a = t.find(wort, a + 1)
            if a >= 0:
                treffer = (zi, a); break
        assert treffer, f"Marker {wort!r} nicht in einer Zeile: {zeilen}"
        belegt.append(treffer)
        zi, a = treffer; t = zeilen[zi]
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 152/231) -------------------------------------
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
    return pl(text, cx, unten + 22, cue, fill=fill, size=26 if len(text) > 14 else 30, anker="m", **k)


def okz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Haken davor (zur gesprochenen Bejahung)."""
    return [bis_(ok(x - 45, y + 20, cue, gr=gr), k.get("bis")), z(text, x, y, cue, stil, size, **k)]


def neinz(text, y, cue, stil="Regular", size=34, x=185, gr=20, kreuz=None, **k):
    """Tafelzeile mit Bleistift-Kreuz davor; kreuz = Cue der gesprochenen Verneinung (sonst mit der Zeile)."""
    return [bis_(nein(x - 45, y + 20, kreuz or cue, gr=gr), k.get("bis")), z(text, x, y, cue, stil, size, **k)]


def plus(text, y, cue, x=150, size=33, stil="Regular"):
    """Tafelzeile mit grünem (+) dahinter: Umstand, der in der Abwägung für der Figur spricht."""
    e = plusminus(glyphen(text), x, y, cue, True, size=size, stil=stil)
    assert e[1].x + e[1].sprite.width <= 1170, f"Zeile zu breit: {text}"
    return e




# --- Größen und Positionen --------------------------------------------------------------------------------------------------
BODEN_Y = 905                                # Boden im Stadion = Unterkante der Figuren
FHA = 470                                    # Figurenhöhe in den Fallszenen
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
X1, X2 = 1430, 1730                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"HA": "Hannes", "RO": "Polizistin Roth"}
NFARBE = {"HA": ORANGE, "RO": BLAU}
TRIBUENE = (222, 222, 216, 255)
STUFE = (204, 204, 198, 255)
BETON = (205, 214, 222, 255)
RASEN = GRUEN
MAUER = (238, 232, 222, 255)
HOLZ = (214, 160, 110, 255)


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
    els = [*fig(k, x, FB, FR, folge, bis=bis), bis_(ns(NAME[k], x, FB, folge[0][0], NFARBE[k], d=0.1), bis)]
    return rechts_frei(els, 1200)


def zwei(folge_ha, folge_ro):
    """Hannes und Polizistin Roth rechts neben der Tafel (blicken nach links zur Tafel)."""
    return [*stehend("HA", X1, folge_ha), *stehend("RO", X2, folge_ro)]


def allein(k, folge):
    return stehend(k, FX, folge)


# --- eigene Szenenbausteine (programmatisch, Palettenflächen, Tuschekontur) ---------------------------------------------------
def _flaeche(w, h, fill, rund=14, rand=5, linien=()):
    s = 2
    im = Image.new("RGBA", ((w + 8) * s, (h + 8) * s))
    dr = ImageDraw.Draw(im)
    dr.rounded_rectangle((3 * s, 3 * s, (w + 3) * s, (h + 3) * s), rund * s, fill=fill, outline=INK, width=rand * s)
    for y_ in linien:
        dr.line((3 * s, (y_ + 3) * s, (w + 3) * s, (y_ + 3) * s), fill=STUFE, width=6 * s)
    return im.resize((im.width // s, im.height // s), Image.LANCZOS)


def stadion(c):
    """Fußballstadion (Grundform): Tribüne mit Stufen links, Rasen mit Seitenlinie rechts, Bodenlinie."""
    trib = _flaeche(880, BODEN_Y - 360, TRIBUENE, linien=(90, 180, 270, 360, 450))
    rasen = _flaeche(930, BODEN_Y - 770, RASEN, rund=8)
    ImageDraw.Draw(rasen).line((8, 34, rasen.width - 8, 34), fill=WEISS, width=6)
    return [El(trib, 57, 357, c, "cut", 0.0, None, name="tribuene"),
            El(rasen, 947, 767, c, "cut", 0.0, None, name="rasen"),
            hart(linienzug([(40, BODEN_Y), (1880, BODEN_Y)], c, breite=7, farbe=INK))]


def bruestung(c):
    """Brüstung des Fanblocks (verdeckt die Beine der Fans)."""
    return El(_flaeche(860, BODEN_Y - 660, BETON, rund=10), 67, 657, c, "cut", 0.0, None, name="bruestung")


def banner(cx, cy, w, h, cue, size=110, bis=None, anim="pop"):
    """Banner mit dem Kürzel (neutrale schwarze Schrift auf Weiß, keine Vereinsfarben)."""
    im = _flaeche(w, h, WEISS, rund=10)
    dr = ImageDraw.Draw(im)
    f = F("ExtraBold", size)
    bb = f.getbbox("ACAB")
    dr.text(((im.width - (bb[2] - bb[0])) / 2 - bb[0], (im.height - (bb[3] - bb[1])) / 2 - bb[1]), "ACAB", font=f, fill=INK)
    return El(im, cx - im.width / 2, cy - im.height / 2, cue, anim, 0.0, bis, name="banner")


def ausgang(c):
    """Stadionausgang (Grundform): Mauer mit Tor, Schild „Ausgang“ (Tabler door-exit)."""
    mauer = _flaeche(1800, BODEN_Y - 400, MAUER, rund=12)
    dr = ImageDraw.Draw(mauer)
    dr.rounded_rectangle((120, 120, 420, mauer.height - 3), 10, fill=(190, 196, 204, 255), outline=INK, width=5)
    for x_ in range(150, 420, 45):
        dr.line((x_, 125, x_, mauer.height - 6), fill=INK, width=3)
    return [El(mauer, 57, 397, c, "cut", 0.0, None, name="mauer"),
            hart(linienzug([(40, BODEN_Y), (1880, BODEN_Y)], c, breite=7, farbe=INK)),
            hart(pl("Ausgang", 330, 430, c, fill=WEISS, size=30, anker="m")),
            ficon("tabler", "door-exit", 470, 460, 54, c, fuell=WEISS, anim="cut")]


# ===========================================================================================================================
# A Fall: im Stadion – Banner im Fanblock, Polizei am Spielfeldrand
# ===========================================================================================================================
HX, F1X, F2X = 470, 220, 720                # Fans im Block (blicken nach rechts zum Spielfeld)
RX, KX = 1330, 1650                         # Polizistin Roth, Kollege (blicken nach links zum Fanblock)
BAN = beim("banner", "Banner")
POL = beim("polizei", "Polizisten")


def fans(c, folge_ha, bis_ha=None, fan_mimik=None):
    """Hannes und zwei Freunde hinter der Brüstung (Fans ohne Vereinsfarben)."""
    fm = fan_mimik or [(c, "froh_r")]
    return [*fig("F1", F1X, BODEN_Y, FHA - 20, fm, erst="cut"),
            *fig("F2", F2X, BODEN_Y, FHA - 10, fm, erst="cut"),
            *fig("HA", HX, BODEN_Y, FHA, folge_ha, erst="cut", bis=bis_ha)]


def schilder_fans(c, bis=None):
    return [hart(bis_(ns("Hannes", HX, BODEN_Y, c, ORANGE), bis)),
            hart(bis_(ns("Freundin", F1X, BODEN_Y, c, WEISS), bis)),
            hart(bis_(ns("Freund", F2X, BODEN_Y, c, WEISS), bis))]


def polizei(c, folge_ro, folge_ko, anim="pop", bis=None):
    return [*fig("RO", RX, BODEN_Y, FHA, folge_ro, erst=anim, bis=bis),
            bis_(ns("Polizistin Roth", RX, BODEN_Y, c, BLAU, d=0.1), bis),
            *fig("KO", KX, BODEN_Y, FHA, folge_ko, erst=anim, bis=bis),
            bis_(ns("Polizist", KX, BODEN_Y, c, BLAU, d=0.1), bis)]


folie([(NULL, "Fall · Im Stadion"), (BAN, "Fall · Das Banner"), ("polizei", "Fall · Polizei im Einsatz"),
       ("ro1", "Fall · Der Strafantrag"), ("frage", "Fall · Die Frage"), ("echt", "Fall · Zwei Klassiker aus Karlsruhe")], [
    *(lambda st: [szene(st[0], "238menge*", 0.8, 0.0), *st[1:]])(stadion(NULL)),
    hart(pl("Fußballstadion, Samstagnachmittag", 70, 30, NULL, fill=GELB, size=38)),
    *fans(NULL, [(NULL, "froh_r"), ("polizei", "ruhig_r"), ("ro1", "ernst_r")], bis_ha="ha1",
          fan_mimik=[(NULL, "froh_r"), ("ro1", "ruhig_r")]),
    *redet("HA_redet_r", HX, BODEN_Y, FHA, "ha1", "frage"),
    *fig("HA", HX, BODEN_Y, FHA, [("frage", "ruhig_r")], erst="cut"),
    bruestung(NULL),
    *schilder_fans(NULL),
    banner(470, 668, 740, 150, BAN),
    pl("Fanblock", HX, 368, "block", fill=WEISS, size=30, anker="m", bis="ro1"),
    pl("Kürzel ACAB", 70, 110, "kuerzel", fill=WEISS, size=34, bis="ro1"),
    pl("auf Deutsch: „Alle Polizisten sind Bastarde“", 70, 190, beim("bedeut", "Deutsch"), fill=WEISS, size=30, bis="ro1"),
    # Polizei am Spielfeldrand
    *fig("RO", RX, BODEN_Y, FHA, [(POL, "ruhig")], bis="ro1"),
    ns("Polizistin Roth", RX, BODEN_Y, POL, BLAU, d=0.1),
    *fig("KO", KX, BODEN_Y, FHA, [(POL, "ruhig"), ("ro1", "ernst"), ("frage", "ruhig")]),
    ns("Polizist", KX, BODEN_Y, POL, BLAU, d=0.1),
    pl("Polizisten im Einsatz", 1180, 310, POL, fill=BLAU, size=30, bis="ro1"),
    *redet("RO_redet", RX, BODEN_Y, FHA, "ro1", "ha1"),
    blase("sprech", 780, 210, "ro1", 1200, 250, inhalt=["Das Banner meint doch uns hier.", "Ich stelle Strafantrag."],
          textsize=36, figur=("RO_redet", RX, BODEN_Y, FHA), bis="ha1"),
    *fig("RO", RX, BODEN_Y, FHA, [("ha1", "skeptisch"), ("frage", "ruhig")], erst="cut"),
    blase("sprech", 900, 210, "ha1", 640, 250, inhalt=["Das ist meine Meinung über die Polizei.", "Gemeint ist niemand persönlich."],
          textsize=34, figur=("HA_redet_r", HX, BODEN_Y, FHA), bis="frage"),
    # Frage und die zwei Klassiker
    pl("Beleidigt Hannes mit dem Banner die Polizisten vor Ort?", 70, 110, "frage", fill=PINK, size=32),
    karte(70, 196, 1000, 140, beim("echt", "Soldaten"), fill=WEISS, rund=18, schatten=6, rand=4),
    z("„Soldaten sind Mörder“ · BVerfGE 93, 266 (1995)", 100, 212, beim("echt", "Soldaten"), "ExtraBold", 32, rechts=1060),
    z("Kürzel ACAB · BVerfG (Kammer) 2016", 100, 272, beim("echt", "Kürzel"), "Bold", 32, rechts=1060),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_238(cue, absaetze, frage, quelle):
    els = [karte(140, 50, 1640, 930, cue, fill=HELL), titel("Sachverhalt", 210, 84, cue, 56)]
    y = 180
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=33, zeilenabstand=1.28)
        els += e; y += 12
    els.append(pille(glyphen(frage), 210, y + 4, cue, fill=PINK, size=32))
    els.append(z(quelle, 210, y + 84, cue, size=26, farbe=TEXT, rechts=1760))
    assert y + 84 + 40 <= 975, f"Sachverhalt zu lang ({y})"
    folie([(cue, "Sachverhalt")], els)


sachverhalt_238("sv", [
    "Samstagnachmittag im Fußballstadion: In der zweiten Halbzeit halten Hannes und seine Freunde im Fanblock an der "
    "Brüstung ein Banner hoch, in Richtung Spielfeld. Darauf steht nur das Kürzel ACAB. Es steht für eine englische "
    "Parole, auf Deutsch: „Alle Polizisten sind Bastarde“.",
    "Am Rand des Spielfelds sind Polizisten im Einsatz, darunter Polizistin Roth. Sie sehen das Banner. An die Beamten "
    "wendet sich Hannes nicht. Polizistin Roth meint, das Banner gelte ihnen, und stellt Strafantrag.",
    "Hannes sagt: Das sei seine Meinung über die Polizei, gemeint sei niemand persönlich.",
], "Beleidigt Hannes mit dem Banner die Polizisten vor Ort?",
    "Nach BVerfG (Kammer), Beschl. v. 17.5.2016 – 1 BvR 2150/14 und 1 BvR 257/14; BVerfGE 93, 266 („Soldaten sind Mörder“)")

# ===========================================================================================================================
# C Art. 5 Abs. 1 S. 1 GG (Wortlautkarte): Meinung
# ===========================================================================================================================
PA5 = "Art. 5 Abs. 1 S. 1 GG"
W5 = "„Jeder hat das Recht, seine Meinung in Wort, Schrift und Bild frei zu äußern und zu verbreiten …“"
w5, w5_y = wortlaut(80, 160, 1100, W5, PA5, "a5", marken=[
    ("Meinung", beim("wl5", "Meinung")), ("äußern", beim("wl5", "äußern")), ("verbreiten", beim("wl5", "verbreiten"))], size=32)
folie([("a5", f"{PA5} › Schutzbereich"), ("mein", f"{PA5} › Meinung"), ("egal", f"{PA5} › geschützt, auch polemisch")],
      rechts_frei([
    *tafel("a5", "Meinungsfreiheit"),
    *w5,
    z("Meinung: Urteil über Sachverhalte, Ideen oder Personen", 110, w5_y + 30, "mein", "Bold", 32),
    *okz("geschützt: begründet oder grundlos,", w5_y + 100, "egal", "Bold", 32, x=160),
    z("emotional oder rational", 160, w5_y + 148, beim("egal", "emotional"), "Bold", 32),
    *okz("auch polemisch oder verletzend formuliert", w5_y + 214, "form", "Bold", 32, x=160),
    zit("BVerfGE 93, 266 <289>; 1 BvR 2150/14, Rn. 11", 160, w5_y + 264, "form"),
    *requisit([("a5", ("tabler", "book", 100, WEISS), "Art. 5 GG", GELB),
               ("mein", ("tabler", "message-circle", 100, WEISS), "Meinung", WEISS),
               ("form", ("tabler", "speakerphone", 100, GELB), "auch verletzend", HELLROT)]),
    *allein("HA", [("a5", "ruhig"), ("mein", "froh"), ("form", "ernst")]),
]))
assert w5_y + 300 <= 900, w5_y

# ===========================================================================================================================
# D Das Kürzel: Meinung, Verweis Folge 025, Eingriff
# ===========================================================================================================================
PK = "Art. 5 Abs. 1 S. 1 GG"
folie([("gleich", f"{PK} › das Kürzel"), ("meinung", f"{PK} › Meinung (+)"), ("eingr", f"{PK} › Eingriff")], rechts_frei([
    *tafel("gleich", "Das Kürzel: eine Meinung?"),
    z("Kürzel = ausgeschriebene Parole", 110, 180, "gleich", "Bold", 34),
    z("denn die Bedeutung ist allgemein bekannt", 110, 232, beim("gleich", "denn"), size=33),
    zit("1 BvR 2150/14, Rn. 12", 110, 280, beim("gleich", "denn")),
    *okz("nicht inhaltslos: allgemeine Ablehnung der Polizei", 346, "ablehn", "Bold", 32, x=160),
    blk(110, 420, 1040, 80, HELLGRUEN, "meinung", [("Also eine Meinung (+)", "ExtraBold", 36, INK)]),
    z("Meinung oder Tatsache? Video „Auschwitzlüge“", 110, 532, "v025", "Bold", 31, farbe=TEXT),
    blk(110, 610, 1040, 80, GELB, "eingr", [("Verurteilung = Eingriff", "ExtraBold", 36, INK)]),
    *requisit([("gleich", ("tabler", "abc", 110, WEISS), "Kürzel ACAB", WEISS),
               ("meinung", ("tabler", "message-circle", 100, HELLGRUEN), "Meinung", HELLGRUEN),
               ("eingr", ("tabler", "gavel", 100, HOLZ), "Verurteilung?", HELLROT)]),
    *allein("HA", [("gleich", "ruhig"), ("meinung", "froh"), ("eingr", "sorge")]),
]))

# ===========================================================================================================================
# E Deutung: objektiver Sinn (BVerfGE 93, 266 <295>)
# ===========================================================================================================================
PD = "Deutung"
folie([("deut", f"{PD} › Sinn der Äußerung"), ("obj", f"{PD} › objektiver Sinn"), ("wort", f"{PD} › Wortlaut"),
       ("kont", f"{PD} › Kontext und Begleitumstände")], rechts_frei([
    *tafel("deut", "1. Was bedeutet die Äußerung?"),
    z("Voraussetzung jeder rechtlichen Würdigung:", 110, 180, "vor", "Bold", 33),
    z("der Sinn ist zutreffend erfasst", 110, 228, "vor", size=33),
    blk(110, 300, 1040, 80, LILA, "obj", [("Maßgeblich: der objektive Sinn", "ExtraBold", 36, INK)]),
    *neinz("nicht die Absicht des Äußernden", 410, "nicht", size=33, x=160),
    *okz("sondern ein unvoreingenommenes und", 466, "publ", "Bold", 33, x=160),
    z("verständiges Publikum", 160, 514, "publ", "Bold", 33),
    z("Ausgangspunkt: der Wortlaut", 110, 590, "wort", "Bold", 33),
    z("dazu: Kontext und erkennbare Begleitumstände", 110, 640, "kont", size=33),
    zit("BVerfGE 93, 266 <295>", 110, 688, "kont"),
    *requisit([("deut", ("tabler", "zoom-question", 100, WEISS), "Sinn?", WEISS),
               ("publ", ("tabler", "users", 110, BLAU), "Publikum", BLAU),
               ("kont", ("tabler", "eye", 100, WEISS), "Kontext", WEISS)]),
    *zwei([("deut", "ruhig"), ("nicht", "staunt"), ("kont", "ruhig")], [("deut", "ruhig"), ("publ", "skeptisch"), ("kont", "ruhig")]),
]))


# ===========================================================================================================================
# F Mehrdeutige Äußerungen (BVerfGE 93, 266 <295 f.>)
# ===========================================================================================================================
def kasten(x, y, w, h, fill, cue, text, size=32):
    els = [karte(x, y, w, h, cue, fill=fill, rund=16, schatten=6, rand=4, anim="pop")]
    tw = F("ExtraBold", size).getlength(glyphen(text))
    els.append(z(text, x + (w - tw) / 2, y + (h - size * 1.35) / 2, cue, "ExtraBold", size, rechts=x + w - 10))
    return els


DEU1, DEU2 = beim("verurt", "Deutung"), beim("ausschl", "anderen")
folie([("mehrd", f"{PD} › mehrdeutige Äußerung"), ("ausschl", f"{PD} › andere Deutungen ausschließen"),
       ("fern", f"{PD} › fernliegende Deutungen")], rechts_frei([
    *tafel("mehrd", "Mehrdeutige Äußerungen"),
    *kasten(420, 180, 380, 76, WEISS, "mehrd", "Äußerung"),
    linienzug([(560, 262), (360, 318)], DEU1, breite=5),
    linienzug([(660, 262), (860, 318)], DEU2, breite=5),
    *kasten(130, 324, 470, 76, HELLROT, DEU1, "Deutung: strafbar"),
    *kasten(640, 324, 470, 76, HELLGRUEN, DEU2, "Deutung: straflos"),
    z("Strafbare Deutung nur, wenn die anderen", 110, 450, "ausschl", "Bold", 33),
    z("mit schlüssigen Gründen ausgeschlossen sind", 110, 498, "ausschl", "Bold", 33),
    *neinz("Fernliegende Deutungen: nicht zu prüfen", 590, "fern", size=33, x=160),
    zit("BVerfGE 93, 266 <295 f.>", 160, 638, "fern"),
    *requisit([("mehrd", ("tabler", "arrows-split", 100, WEISS), "mehrdeutig", WEISS),
               ("verurt", ("tabler", "gavel", 100, HOLZ), "Gericht", WEISS),
               ("fern", ("tabler", "search", 90, WEISS), "fernliegend: nein", WEISS)]),
    *zwei([("mehrd", "ruhig"), ("ausschl", "froh")], [("mehrd", "ruhig"), ("verurt", "ernst"), ("fern", "ruhig")]),
]))

# ===========================================================================================================================
# G „Soldaten sind Mörder“ (BVerfGE 93, 266 <297–299>)
# ===========================================================================================================================
PS_ = "„Soldaten sind Mörder“"
folie([("sold", f"{PS_} › BVerfGE 93, 266"), ("schlecht", f"{PS_} › andere Deutung"),
       ("uebers", f"{PS_} › nicht ausgeschlossen")], rechts_frei([
    *tafel("sold", "„Soldaten sind Mörder“"),
    karte(90, 168, 1060, 124, "sold", fill=ZITAT, rund=18, schatten=6, rand=4),
    z("BVerfGE 93, 266 · Beschl. v. 10.10.1995", 120, 184, "sold", "ExtraBold", 34),
    z("1 BvR 1476/91 u. a.", 120, 236, "sold", "Bold", 30, farbe=TEXT),
    z("Kriegsgegner wegen Beleidigung verurteilt,", 110, 330, "kriegs", "Bold", 33),
    z("etwa wegen eines Transparents", 110, 378, beim("kriegs", "etwa"), size=33),
    z("Mögliche Deutung:", 110, 452, "schlecht", "Bold", 33),
    *okz("gegen Soldatentum und Kriegshandwerk schlechthin", 506, beim("schlecht", "gegen"), size=32, x=160),
    *neinz("nicht gegen einzelne Soldaten", 562, beim("schlecht", "nicht"), size=32, x=160),
    zit("BVerfGE 93, 266 <298 f.>", 160, 610, beim("schlecht", "nicht")),
    blk(110, 670, 1040, 80, HELLROT, "uebers", [("Strafgerichte: nicht ausgeschlossen", "ExtraBold", 34, INK)]),
    zit("BVerfGE 93, 266 <297>", 110, 766, "uebers"),
    *requisit([("sold", ("tabler", "gavel", 100, HOLZ), "BVerfG 1995", WEISS),
               ("kriegs", ("tabler", "flag", 100, WEISS), "Transparent", WEISS),
               ("schlecht", ("tabler", "scale", 110, WEISS), "Kriegshandwerk", WEISS)]),
    *zwei([("sold", "ruhig"), ("schlecht", "staunt"), ("uebers", "ruhig")], [("sold", "ruhig"), ("uebers", "skeptisch")]),
]))

# ===========================================================================================================================
# H Kollektivbeleidigung: Skala (BVerfGE 93, 266 <299–303>)
# ===========================================================================================================================
SY = 455                                     # Skala: Höhe der Linie


def skala():
    """Skala auf der Tafel (bewusst links, daher außerhalb von rechts_frei): Einzelperson … soziale Einrichtungen."""
    return [linienzug([(210, SY), (1080, SY)], "groesse", breite=8),
            ficon("tabler", "user", 210, SY - 14, 64, "skala1", fuell=ORANGE),
            pl("Einzelperson", 210, SY + 22, "skala1", fill=ORANGE, size=28, anker="m"),
            ficon("tabler", "building", 1080, SY - 14, 64, "skala2", fuell=WEISS),
            pl("soziale Einrichtungen", 1000, SY + 22, "skala2", fill=WEISS, size=28, anker="m"),
            ficon("tabler", "map-pin", 880, SY - 6, 50, "welt", fuell=ROT),
            pl("alle Soldaten der Welt", 830, SY + 90, "welt", fill=HELLROT, size=28, anker="m"),
            ficon("tabler", "map-pin", 520, SY - 6, 50, "bw", fuell=GRUEN),
            pl("Bundeswehr", 520, SY + 90, "bw", fill=HELLGRUEN, size=28, anker="m")]
PKO = "Kollektivbeleidigung"
folie([("koll", f"{PKO} › wen trifft die Äußerung?"), ("groesse", f"{PKO} › je größer, desto schwächer"),
       ("welt", f"{PKO} › alle Soldaten der Welt"), ("bw", f"{PKO} › Soldaten der Bundeswehr"),
       ("teil", f"{PKO} › Teilgruppe genügt nicht")], rechts_frei([
    *tafel("koll", "2. Wen trifft die Äußerung?"),
    z("Äußerung über ein Kollektiv kann die", 110, 168, "samm", size=32),
    z("persönliche Ehre der Mitglieder verletzen", 110, 210, "samm", size=32),
    z("Je größer das Kollektiv, desto schwächer", 110, 262, "groesse", "Bold", 32),
    z("die persönliche Betroffenheit", 110, 304, "groesse", "Bold", 32),
    *neinz("Alle Soldaten der Welt: keine überschaubare Gruppe", 640, "welt", size=31, x=160),
    *okz("Aktive Soldaten der Bundeswehr: können es sein", 692, "bw", size=31, x=160),
    z("Teilgruppe allein genügt nicht:", 110, 754, "teil", "Bold", 31),
    z("Gericht muss Umstände für gerade diesen Bezug benennen", 110, 798, "umst", size=31),
    zit("BVerfGE 93, 266 <299–303>", 110, 842, "umst"),
    *requisit([("koll", ("tabler", "users-group", 110, BLAU), "Kollektiv", BLAU),
               ("welt", ("tabler", "flag", 100, WEISS), "Soldaten", WEISS),
               ("umst", ("tabler", "search", 90, WEISS), "Umstände?", WEISS)]),
    *zwei([("koll", "ruhig"), ("groesse", "staunt"), ("teil", "ruhig")], [("koll", "ruhig"), ("bw", "skeptisch"), ("umst", "ruhig")]),
]) + skala())


# ===========================================================================================================================
# I ACAB-Kammerbeschlüsse (1 BvR 2150/14, 1 BvR 257/14)
# ===========================================================================================================================
def banner_klein(cue, bis=None):
    return rechts_frei([banner(PX, 300, 300, 100, cue, size=70, bis=bis)])[0]


PAC = "ACAB-Beschlüsse"
folie([("acab", f"{PAC} › BVerfG (Kammer) 2016"), ("teilg", f"{PAC} › Teilgruppe reicht nicht"),
       ("pers", f"{PAC} › personalisierte Zuordnung"), ("aufent", f"{PAC} › Anwesenheit genügt nicht"),
       ("kontx", f"{PAC} › Kontext")], rechts_frei([
    *tafel("acab", "Das Kürzel ACAB im Stadion"),
    karte(90, 166, 1060, 122, "kammer", fill=ZITAT, rund=18, schatten=6, rand=4),
    z("BVerfG (Kammer), Beschl. v. 17.5.2016", 120, 180, "kammer", "ExtraBold", 33),
    z("1 BvR 2150/14 (Buchstaben im Fanblock); 1 BvR 257/14", 120, 232, "stadion", "Bold", 28, farbe=TEXT),
    *neinz("Teilgruppe aller Polizisten: reicht nicht", 320, "teilg", "Bold", 32, x=160, kreuz=beim("teilg", "reicht")),
    blk(110, 388, 1040, 80, GELB, "pers", [("Nötig: personalisierte Zuordnung", "ExtraBold", 36, INK)]),
    z("zu bestimmten Beamten", 130, 478, beim("pers", "bestimmten"), "Bold", 32),
    *neinz("Polizei im Stadion, könnte es sehen: genügt nicht", 540, "aufent", size=31, x=160, kreuz=beim("aufent", "genügt")),
    zit("1 BvR 2150/14, Rn. 16 f.; 1 BvR 257/14, Rn. 17", 160, 588, "aufent"),
    z("Kontext im Stadionfall:", 110, 650, "kontx", "Bold", 32),
    z("zuvor Banner mit Kritik an Polizeieinsätzen", 130, 698, "krit", size=31),
    z("von den Gerichten nicht gewürdigt", 130, 744, "uebg", size=31),
    zit("1 BvR 2150/14, Rn. 18", 130, 790, "uebg"),
    bis_(banner_klein("acab"), "pers"),
    *requisit([("pers", ("tabler", "user-check", 100, HELLGRUEN), "bestimmte Beamte", HELLGRUEN),
               ("aufent", ("tabler", "eye", 100, WEISS), "sehen: genügt nicht", HELLROT),
               ("kontx", ("tabler", "message-report", 100, WEISS), "Kontext", WEISS)]),
    *zwei([("acab", "ruhig"), ("teilg", "froh"), ("kontx", "ruhig")], [("acab", "ruhig"), ("pers", "skeptisch"), ("kontx", "ruhig")]),
]))

# ===========================================================================================================================
# J Schranken: Art. 5 Abs. 2 GG, § 185 StGB (Wortlautkarten)
# ===========================================================================================================================
W52 = ("„Diese Rechte finden ihre Schranken in den Vorschriften der allgemeinen Gesetze, den gesetzlichen Bestimmungen "
       "zum Schutze der Jugend und in dem Recht der persönlichen Ehre.“")
w52, w52_y = wortlaut(80, 160, 1100, W52, "Art. 5 Abs. 2 GG", "schr", marken=[
    ("allgemeinen", beim("a52", "allgemeinen")), ("persönlichen Ehre", beim("a52", "persönlichen"))], size=30)
W185 = ("„Die Beleidigung wird mit Freiheitsstrafe bis zu einem Jahr oder mit Geldstrafe und, wenn die Beleidigung "
        "öffentlich, in einer Versammlung, durch Verbreiten eines Inhalts (§ 11 Absatz 3) oder mittels einer Tätlichkeit "
        "begangen wird, mit Freiheitsstrafe bis zu zwei Jahren oder mit Geldstrafe bestraft.“")
w185, w185_y = wortlaut(80, w52_y + 24, 1100, W185, "§ 185 StGB", "p185", marken=[
    ("Freiheitsstrafe", beim("nur", "Strafe")), ("Beleidigung", beim("nur", "Beleidigung"))], size=30)
PSR = "Schranken"
folie([("schr", f"{PSR} › Art. 5 Abs. 2 GG"), ("p185", f"{PSR} › § 185 StGB: allgemeines Gesetz"),
       ("nur", f"{PSR} › § 185 StGB definiert die Beleidigung nicht")], rechts_frei([
    *tafel("schr", "Schranken: Art. 5 Abs. 2 GG"),
    *w52, *w185,
    *okz("§ 185 StGB: allgemeines Gesetz", w185_y + 18, beim("p185", "allgemeines"), "Bold", 32, x=160),
    z("nennt nur die Strafe, definiert die Beleidigung nicht", 110, w185_y + 74, "nur", size=31),
    zit("1 BvR 2150/14, Rn. 13; BVerfGE 93, 266 <291 f.>", 110, w185_y + 120, "nur"),
    *requisit([("schr", ("tabler", "book", 100, WEISS), "Art. 5 Abs. 2 GG", GELB),
               ("p185", ("tabler", "book", 100, GELB), "§ 185 StGB", WEISS)]),
    *allein("RO", [("schr", "ruhig"), ("p185", "ernst"), ("nur", "skeptisch")]),
]))
assert w185_y + 150 <= 900, w185_y

# ===========================================================================================================================
# K Anwendung von § 185: Wechselwirkung, Deutung und Personenbezug, § 193
# ===========================================================================================================================
folie([("wechs", f"{PSR} › Wechselwirkung"), ("ort", f"{PSR} › Anwendung: Deutung, Personenbezug"),
       ("p193", f"{PSR} › § 193 StGB: Abwägung")], rechts_frei([
    *tafel("wechs", "Anwendung von § 185 StGB"),
    blk(110, 180, 1040, 80, LILA, "wechs", [("Auslegung im Licht der Meinungsfreiheit", "ExtraBold", 34, INK)]),
    z("Wechselwirkung: Lüth-Urteil, BVerfGE 7, 198", 110, 280, beim("wechs", "Wechselwirkung"), "Bold", 31, farbe=TEXT),
    z("Hier prüfst du:", 110, 356, "ort", "Bold", 34),
    z("1. Deutung der Äußerung", 150, 408, beim("ort", "Deutung"), size=34),
    z("2. Personenbezug", 150, 458, beim("ort", "Personenbezug"), size=34),
    blk(110, 540, 1040, 80, HELLGRUEN, "p193", [("§ 193 StGB: Wahrnehmung berechtigter Interessen", "ExtraBold", 32, INK)]),
    z("im Regelfall abwägen: Meinungsfreiheit gegen Ehre", 110, 640, beim("p193", "Regelfall"), "Bold", 32),
    zit("BVerfGE 93, 266 <290 f., 293 f.>; 1 BvR 2150/14, Rn. 15", 110, 688, beim("p193", "Regelfall")),
    *requisit([("wechs", ("tabler", "arrows-left-right", 100, WEISS), "Wechselwirkung", LILA),
               ("ort", ("tabler", "zoom-question", 100, WEISS), "Deutung, Bezug", WEISS),
               ("p193", ("tabler", "scale", 110, WEISS), "Abwägung", HELLGRUEN)]),
    *allein("RO", [("wechs", "ruhig"), ("p193", "froh")]),
]))

# ===========================================================================================================================
# L Ergebnis im Stadion
# ===========================================================================================================================
folie([("erg", "Ergebnis › zurück im Stadion"), ("erg2", "Ergebnis › kein Bezug auf die Beamten"),
       ("erg4", "Ergebnis › keine Beleidigung der Polizisten vor Ort"),
       ("verl", "Ergebnis › Verurteilung verletzt Art. 5 Abs. 1 S. 1 GG")], [
    *stadion("erg"),
    hart(pl("Zurück ins Stadion", 70, 30, "erg", fill=GELB, size=38)),
    *fans("erg", [("erg", "froh_r"), ("erg4", "froh_r")]),
    bruestung("erg"),
    *schilder_fans("erg"),
    hart(banner(470, 668, 740, 150, "erg")),
    *polizei("erg", [("erg", "ruhig"), ("erg3", "ruhig"), ("erg4", "still")], [("erg", "ruhig")], anim="cut"),
    pl("Banner im Fanblock, Richtung Spielfeld", 70, 110, "erg1", fill=WEISS, size=32, bis="erg4"),
    pl("An die Polizisten wendet er sich nicht.", 70, 190, "erg2", fill=WEISS, size=32, bis="erg4"),
    pl("Dass sie da sind und das Banner sehen, reicht nicht.", 70, 270, "erg3", fill=HELLROT, size=32, bis="erg4"),
    karte(70, 112, 1060, 200, "erg4", fill=WEISS, rund=18, schatten=6, rand=4),
    *neinz("Keine Beleidigung der Polizisten vor Ort", 130, "erg4", "ExtraBold", 34, x=150, kreuz=beim("erg4", "Beleidigung")),
    z("Verurteilung verletzt Art. 5 Abs. 1 S. 1 GG", 150, 196, "verl", "Bold", 32, rechts=1110),
    zit("1 BvR 2150/14, Rn. 17 f.", 150, 248, "verl", rechts=1110),
])

# ===========================================================================================================================
# M Gegenfall am Stadionausgang
# ===========================================================================================================================
HG = 1000                                    # Hannes vor den Beamten (Endposition)
G_LOS, G_DA = beim("gg1", "geht"), beim("gg1", "Polizisten", ende=True)
GDX = -540                                   # Hannes kommt von links


def gehend(e):
    return bewegt(e, G_LOS, G_DA, GDX, 0)


folie([("gegen", "Gegenfall › nach dem Spiel"), ("gg1", "Gegenfall › gezielt zu den Beamten"),
       ("gg2", "Gegenfall › bewusst in ihre Nähe begeben"), ("gg3", "Gegenfall › Bezug auf diese Beamten (+)"),
       ("gg4", "Gegenfall › Beleidigung möglich, § 193 StGB")], [
    *ausgang("gegen"),
    hart(pl("Gegenfall: nach dem Spiel", 70, 30, "gegen", fill=GELB, size=38)),
    *fig("RO", RX, BODEN_Y, FHA, [("gegen", "ruhig"), (G_DA, "ernst")], erst="cut", bis="ro2"),
    *redet("RO_redet", RX, BODEN_Y, FHA, "ro2", "gg2"),
    *fig("RO", RX, BODEN_Y, FHA, [("gg2", "ernst"), ("gg4", "ruhig")], erst="cut"),
    hart(ns("Polizistin Roth", RX, BODEN_Y, "gegen", BLAU)),
    *fig("KO", KX, BODEN_Y, FHA, [("gegen", "ruhig"), ("ro2", "ernst")], erst="cut"),
    hart(ns("Polizist", KX, BODEN_Y, "gegen", BLAU)),
    # Hannes kommt mit dem Banner von links (Schritte)
    szene(gehend(peep_voll("HA_entschl_r", HG, BODEN_Y, FHA, "gegen", anim="cut", bis="gg2")), "238schritte*", 1.0,
          round(T_(G_LOS) - T_("gegen"), 3)),
    gehend(bis_(ns("Hannes", HG, BODEN_Y, "gegen", ORANGE), "gg2")),
    gehend(banner(HG + 40, 640, 300, 110, "gegen", size=64, anim="cut", bis="gg2")),
    *fig("HA", HG, BODEN_Y, FHA, [("gg2", "ernst_r"), ("gg4", "still_r")], erst="cut"),
    hart(ns("Hannes", HG, BODEN_Y, "gg2", ORANGE)),
    hart(banner(HG + 40, 640, 300, 110, "gg2", size=64, anim="cut")),
    pl("gezielt zu einer Gruppe von Polizisten", 70, 110, beim("gg1", "gezielt"), fill=WEISS, size=32),
    blase("sprech", 760, 190, "ro2", 1420, 250, inhalt=["Jetzt sind wirklich wir gemeint."], textsize=36,
          figur=("RO_redet", RX, BODEN_Y, FHA), bis="gg2"),
    pl("bewusst in ihre Nähe, um sie zu konfrontieren", 70, 190, "gg2", fill=HELLROT, size=32),
    *okz("Äußerung auf diese Beamten bezogen", 284, "gg3", "Bold", 32, x=120, rechts=900),
    karte(70, 360, 820, 190, "gg4", fill=WEISS, rund=18, schatten=6, rand=4),
    z("Beleidigung kommt in Betracht", 100, 378, "gg4", "ExtraBold", 34, rechts=870),
    z("nach Abwägung bei § 193 StGB", 100, 432, beim("gg4", "Abwägung"), "Bold", 32, rechts=870),
    zit("1 BvR 257/14, Rn. 17; 1 BvR 1593/16, Rn. 17", 100, 486, beim("gg4", "Abwägung"), rechts=870),
])

# ===========================================================================================================================
# N Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · zuerst den Sinn ermitteln"), ("t2", "Klausurtipp · personalisierte Zuordnung"),
       ("t3", "Klausurtipp · Schmähkritik nicht vorschnell")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Zuerst den Sinn ermitteln:", 200, 200, "t1", "ExtraBold", 38),
    z("Kontext, alle nicht fernliegenden Deutungen", 200, 256, beim("t1", "Kontext"), "Bold", 34),
    linienzug([(130, 336), (1130, 336)], "t2", breite=3),
    z("Sammelbezeichnung? Personalisierte", 200, 362, "t2", "Bold", 36),
    z("Zuordnung zu bestimmten Personen?", 200, 414, beim("t2", "personalisierte"), "Bold", 36),
    linienzug([(130, 494), (1130, 494)], "t3", breite=3),
    z("Schmähkritik nicht vorschnell annehmen:", 200, 520, "t3", "Bold", 36),
    z("auch sie setzt die Zuordnung voraus", 200, 572, beim("t3", "Auch"), "ExtraBold", 36),
    zit("1 BvR 2150/14, Rn. 19; BVerfGE 93, 266 <294>", 200, 630, beim("t3", "Auch")),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# O Prüfschema
# ===========================================================================================================================
REIHEN = [("k1", 0, "I. Schutzbereich: Meinung, Art. 5 Abs. 1 S. 1 GG", True),
          ("k2", 0, "II. Eingriff: strafrechtliche Verurteilung", True),
          ("k3", 0, "III. Rechtfertigung", True),
          ("k3a", 1, "1. Schranke: § 185 StGB als allgemeines Gesetz", False),
          ("k3b", 1, "2. Verfassungsgemäße Anwendung (Wechselwirkung)", False),
          ("k3c", 2, "a) Sinn der Äußerung: objektiv, Kontext, mehrdeutig?", False),
          ("k3d", 2, "b) Bezug auf bestimmte Personen", False),
          ("k3e", 2, "c) Abwägung bei § 193 StGB", False)]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfschema: Verurteilung wegen einer Äußerung"), 110, 90, "sch", 46),
           z("Art. 5 Abs. 1 S. 1, Abs. 2 GG; §§ 185, 193 StGB", 110, 160, "sch", "Bold", 32, farbe=TEXT, rechts=1800)]
y = 240
for c, ebene, text, fett in REIHEN:
    x = (130, 200, 270)[ebene]
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", (40, 36, 34)[ebene], rechts=1800))
    y += {0: 80, 1: 72, 2: 66}[ebene]
assert y <= 970, y
folie([("sch", "Prüfschema"), ("k1", "Prüfschema › I. Schutzbereich"), ("k2", "Prüfschema › II. Eingriff"),
       ("k3", "Prüfschema › III. Rechtfertigung"), ("k3a", "Prüfschema › III. 1. Schranke"),
       ("k3b", "Prüfschema › III. 2. Anwendung"), ("k3c", "Prüfschema › III. 2. a) Sinn der Äußerung"),
       ("k3d", "Prüfschema › III. 2. b) Bezug auf bestimmte Personen"), ("k3e", "Prüfschema › III. 2. c) Abwägung, § 193 StGB")],
      els_sch)

# ===========================================================================================================================
# P Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Erst den ", 0), ("Sinn", "a"), (" ermitteln,", 0)], [("dann strafen.", 0)]], 750, 290, 46, "merke",
                {"a": beim("merke", "Sinn")}),
    *markertext([[("Und eine Parole über alle Polizisten", 0)], [("trifft die Beamten vor Ort nur,", 0)],
                 [("wenn ", 0), ("besondere Umstände", "b")], [("sie gerade auf sie beziehen.", 0)]], 750, 500, 44, "m2",
                {"b": beim("m2", "besondere")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
