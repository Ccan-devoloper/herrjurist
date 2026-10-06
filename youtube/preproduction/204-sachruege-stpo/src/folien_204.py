"""Folge 204 · Sachrüge StPO: Wenn die Feststellungen das Urteil nicht tragen – Serienstandard Open Peeps (Katzenkönig).
Beispielfall: Die Strafkammer verurteilt Herrn Wichmann wegen Betrugs zu 2 Jahren und 6 Monaten. Laut den Feststellungen
verkaufte er Frau Danner einen Oldtimer für 85.000 € als „unfallfrei“, obwohl der Wagen einen schweren Unfallschaden hatte;
sie zahlte. Zum Wert des Wagens schweigt das Urteil; strafschärfend nennt es einen „hohen Schaden“. Rechtsanwältin Hellmers
prüft die Sachrüge.
Szenen laut ../SZENENPLAN.md: A1 Kanzlei, A2 Rückblick Oldtimer-Halle, A3 Kanzlei, B Sachverhalt, C Wortlautkarte § 337,
D allgemeine Sachrüge (Wortlautkarte § 344 Abs. 2 S. 1), E Prüfungsgrundlage Urteilsurkunde, F–I vier Prüfungsstufen
(a Subsumtion, b Darstellungsmangel mit Wortlautkarte § 267 Abs. 1 S. 1, c Beweiswürdigung, d Strafzumessung), K Fall:
Vermögensschaden (Waage), L Ergebnis (§§ 337, 353, 354), M Klausurtipp (Lexi), N Prüfschema, O Merksatz (Lexi).
Ein Handlungsgeräusch (Geldscheine, als Frau Danner zahlt; ../geraeusche_herkunft.json). Namensschild jeder Figur, solange sie
im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz als eigene Kopie aus Folge 168
(gemeinsame Dateien unverändert); neu: regal(), fenster() (nach Sichtprüfung nicht verwendet), urkunde(), halle(), chips(), tafelicon().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut nach gesetze-im-internet.de (Abruf 06.10.2026)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_204/"

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
HELLGRAU = (226, 226, 222, 255)
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
        if n.startswith(("bild:", "ficon:")) or "/op_204/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def wortlaut(x, y, w, zeilen, quelle, cue, marken=(), size=32, bis=None):
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 06.10.2026), als Zitat mit Normangabe;
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 103/109/112/124) -----------------------------
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
    """Namensschild unter der Figur (ab ihrem ersten Auftritt, solange sie im Bild ist); das lange Schild
    „Rechtsanwältin Hellmers“ in 26 px, damit es neben der zweiten Figur Platz hat."""
    return pl(text, cx, unten + 22, cue, fill=fill, size=26 if text.startswith("Rechtsanw") else 30, anker="m", **k)


def okz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Haken davor (zur gesprochenen Bejahung)."""
    return [ok(x - 45, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]


def neinz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Kreuz davor (zur gesprochenen Verneinung)."""
    return [nein(x - 45, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]



# --- eigene Szenenbausteine (programmatisch, Palettenflächen, Tuschekontur) ---------------------------------------------------
BODEN_Y = 905                                # Boden = Unterkante der Figuren in den Fallszenen
FHA = 480                                    # Figurenhöhe in den Fallszenen
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
WAND = (238, 230, 214, 255)
HOLZD = (176, 122, 78, 255)
GRAU = (190, 190, 186, 255)


def _flaeche(w, h, zeichne):
    s = 2
    im = Image.new("RGBA", (w * s, h * s))
    zeichne(ImageDraw.Draw(im), s)
    return im.resize((w, h), Image.LANCZOS)


def boden(c, x0=60, x1=1860):
    return hart(linienzug([(x0, BODEN_Y), (x1, BODEN_Y)], c, breite=7, farbe=INK))


def regal(c, x0=110, w=400):
    """Aktenregal der Kanzlei (Grundform): drei Böden mit Ordnerrücken in Palettenfarben."""
    h = 500
    farben = [BLAU, GELB, LILA, GRUEN, ROT, WEISS]
    def zz(dr, s):
        dr.rectangle((3 * s, 3 * s, (w - 3) * s, (h - 3) * s), fill=HOLZ, outline=INK, width=5 * s)
        for r in range(3):
            y0 = 30 + r * 155
            dr.rectangle((24 * s, y0 * s, (w - 24) * s, (y0 + 130) * s), fill=(240, 226, 200, 255), outline=INK, width=4 * s)
            for i in range(8):
                xo = 34 + i * 42
                dr.rounded_rectangle((xo * s, (y0 + 18) * s, (xo + 34) * s, (y0 + 128) * s), 4 * s,
                                     fill=farben[(i + r * 2) % 6], outline=INK, width=3 * s)
    return hart(El(_flaeche(w, h, zz), x0, BODEN_Y - h, c, "cut", 0.0, None, name="regal"))


def fenster(c, x0, y0, w=300, h=240):
    def zz(dr, s):
        dr.rounded_rectangle((3 * s, 3 * s, (w - 3) * s, (h - 3) * s), 10 * s, fill=(214, 232, 250, 255), outline=INK, width=5 * s)
        dr.line((w // 2 * s, 0, w // 2 * s, h * s), fill=INK, width=5 * s)
        dr.line((0, h // 2 * s, w * s, h // 2 * s), fill=INK, width=5 * s)
    return hart(El(_flaeche(w, h, zz), x0, y0, c, "cut", 0.0, None, name="fenster"))


UX, UY, UW, UH = 530, 330, 480, 545           # Urteilsurkunde (vergrößertes Blatt) in der Kanzlei


def urkunde(c, anim="pop"):
    """Das schriftliche Urteil als großes Blatt (Grundform) mit grauen Textzeilen."""
    def zz(dr, s):
        dr.rounded_rectangle((3 * s, 3 * s, (UW - 3) * s, (UH - 3) * s), 12 * s, fill=WEISS, outline=INK, width=5 * s)
        for i in range(9):
            yl = 120 + i * 44
            dr.line((36 * s, yl * s, (UW - 36 - (90 if i % 3 == 2 else 0)) * s, yl * s), fill=(215, 215, 210, 255), width=6 * s)
    e = El(_flaeche(UW, UH, zz), UX, UY, c, anim, 0.0, None, name="urkunde")
    return [e, z("Urteil", UX + 36, UY + 26, c, "ExtraBold", 44, rechts=UX + UW), ]


def halle(c):
    """Oldtimer-Halle (Grundform): Wand, großes Rolltor mit Lamellen, Boden."""
    def zz(dr, s):
        dr.rectangle((0, 0, 1800 * s, 525 * s), fill=WAND)
        dr.rounded_rectangle((520 * s, 40 * s, 1280 * s, 525 * s), 8 * s, fill=(222, 222, 216, 255), outline=INK, width=5 * s)
        for yl in range(90, 525, 48):
            dr.line((524 * s, yl * s, 1276 * s, yl * s), fill=GRAU, width=4 * s)
    return hart(El(_flaeche(1800, 525, zz), 60, 380, c, "cut", 0.0, None, name="halle"))


X1, X2 = 1395, 1730                         # zwei Figuren neben der Tafel (links Hellmers, rechts Wichmann)
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"WI": "Herr Wichmann", "HE": "Rechtsanwältin Hellmers", "DA": "Frau Danner"}
NFARBE = {"WI": BLAU, "HE": LILA, "DA": GRUEN}


def stehend(k, x, folge, unten=930, hoehe=480):
    return [*fig(k, x, unten, hoehe, folge), ns(NAME[k], x, unten, folge[0][0], NFARBE[k], d=0.1)]


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


def zwei(folge_wi, folge_he):
    """Rechtsanwältin Hellmers und Herr Wichmann rechts neben der Tafel (blicken nach links zur Tafel)."""
    return [*stehend("HE", X1, folge_he), *stehend("WI", X2, folge_wi)]


def allein(k, folge):
    return stehend(k, FX, folge)


def tafelicon(e):
    """Icon als Teil der Tafel (Waage im Fall), bewusst links: von rechts_frei() ausgenommen."""
    e.name = "tafelicon:" + e.name.split(":", 1)[1]
    return e


def chips(aktiv, c, erst=None):
    """Vier Prüfungsstufen als Leiste oben auf der Tafel; die aktuelle Stufe farbig."""
    els = []
    for i, b in enumerate("abcd"):
        x = 760 + i * 100
        fill = GELB if b == aktiv else HELLGRAU
        els.append(hart(pl(f"{b})", x, 96, c if erst is None else erst, fill=fill, size=30)))
    return els


# ===========================================================================================================================
# A1 Fall: in der Kanzlei – das schriftliche Urteil ist da
# ===========================================================================================================================
HX, WX = 1230, 1640                          # Rechtsanwältin Hellmers (blickt nach rechts), Herr Wichmann (blickt nach links)
folie([(NULL, "Fall · In der Kanzlei"), ("urteil", "Fall · Das Urteil des Landgerichts"), ("liest", "Fall · Die Urteilsgründe")], [
    boden(NULL),
    regal(NULL),

    hart(pl("Kanzlei Hellmers", 70, 30, NULL, fill=LILA, size=38)),
    pl("Landgericht: Betrug", 70, 110, beim("urteil", "Betrugs"), fill=WEISS, size=34),
    pl("2 Jahre und 6 Monate Freiheitsstrafe", 70, 190, beim("urteil", "zwei"), fill=HELLROT, size=34),
    *urkunde(beim("liest", "liest")),
    *stehend("HE", HX, [(NULL, "ruhig_r"), (beim("liest", "liest"), "ernst_r")], unten=BODEN_Y),
    *stehend("WI", WX, [(NULL, "ruhig"), (beim("urteil", "zwei"), "sorge")], unten=BODEN_Y),
])

# ===========================================================================================================================
# A2 Fall: Rückblick – der Verkauf des Oldtimers
# ===========================================================================================================================
VX, DX = 430, 1500                           # Herr Wichmann (blickt nach rechts), Frau Danner (blickt nach links)
folie([("rueck", "Fall · Rückblick: der Verkauf"), ("w1", "Fall · „unfallfrei“"), ("unfall", "Fall · Der Unfallschaden"),
       ("zahlt", "Fall · Die Zahlung")], [
    halle("rueck"),
    boden("rueck"),
    hart(pl("Rückblick: Oldtimer-Verkauf", 70, 30, "rueck", fill=GELB, size=38)),
    hart(ficon("tabler", "car", 960, BODEN_Y + 4, 560, "rueck", fuell=ROT)),
    pl("85.000 €", 960, 455, beim("rueck", "fünfundachtzigtausend"), fill=GELB, size=40, anker="m"),
    *stehend("WI", VX, [("rueck", "ruhig_r"), ("unfall", "skeptisch_r")], unten=BODEN_Y),
    *stehend("DA", DX, [("rueck", "ruhig"), ("zahlt", "froh")], unten=BODEN_Y),
    *redet("WI_redet_r", VX, BODEN_Y, FHA, "w1", "d1"),
    blase("sprech", 600, 190, "w1", 640, 230, inhalt=["Der Wagen ist unfallfrei."], textsize=40,
          figur=("WI_redet_r", VX, BODEN_Y, FHA), bis="d1"),
    *redet("DA_redet", DX, BODEN_Y, FHA, "d1", "unfall"),
    blase("sprech", 560, 190, "d1", 1340, 230, inhalt=["Dann nehme ich ihn."], textsize=40,
          figur=("DA_redet", DX, BODEN_Y, FHA), bis="unfall"),
    *fig("DA", DX, BODEN_Y, FHA, [("unfall", "ruhig")], erst="cut", bis="zahlt"),
    ficon("tabler", "car-crash", 960, 395, 130, beim("unfall", "Unfall"), fuell=HELLROT),
    pl("schwerer Unfallschaden – verschwiegen", 70, 110, beim("unfall", "Unfall"), fill=HELLROT, size=34),
    pl("Herr Wichmann wusste das", 70, 190, beim("unfall", "wusste"), fill=WEISS, size=34),
    szene(ficon("tabler", "cash-banknote", 1250, 640, 150, beim("zahlt", "zahlte"), fuell=GRUEN), "204geld*", 0.7, -0.2),
    pl("Frau Danner zahlt 85.000 €", 70, 270, beim("zahlt", "zahlte"), fill=GRUEN, size=34),
])

# ===========================================================================================================================
# A3 Fall: zurück in der Kanzlei – was steht im Urteil?
# ===========================================================================================================================
LZ = [("Täuschung: „unfallfrei“", "Täuschung"), ("Irrtum", "Irrtum"), ("Zahlung: 85.000 €", "Zahlung")]
els_a3 = [boden("h1"), regal("h1"),
          hart(pl("Kanzlei Hellmers", 70, 30, "h1", fill=LILA, size=38)),
          *[hart(e) for e in urkunde("h1", anim="cut")]]
for i, (t, w) in enumerate(LZ):
    els_a3 += okz(t, UY + 100 + i * 70, beim("h1", w), "Bold", 32, x=UX + 80, rechts=UX + UW - 10)
els_a3 += [z("Schaden: ?", UX + 80, UY + 330, beim("h1", "wert"), "ExtraBold", 38, farbe=DROT, rechts=UX + UW - 10),
           z("kein Wort", UX + 80, UY + 390, beim("h1", "kein"), "Bold", 32, farbe=DROT, rechts=UX + UW - 10),
           *stehend("HE", HX, [("h1", "ernst_r")], unten=BODEN_Y),
           *redet("HE_redet_r", HX, BODEN_Y, FHA, "h1", "w2"),
           blase("sprech", 820, 260, "h1", 1390, 175, inhalt=["Täuschung, Irrtum, Zahlung. Alles da.",
                 "Aber was war der Wagen wert?", "Dazu steht hier kein Wort."], textsize=34,
                 figur=("HE_redet_r", HX, BODEN_Y, FHA), bis="w2"),
           *fig("HE", HX, BODEN_Y, FHA, [("w2", "skeptisch_r"), ("frage", "ruhig_r")], erst="cut"),
           *stehend("WI", WX, [("h1", "sorge")], unten=BODEN_Y),
           *redet("WI_redet2", WX, BODEN_Y, FHA, "w2", "frage"),
           blase("sprech", 700, 200, "w2", 1420, 190, inhalt=["Der Wagen war", "das Geld doch wert!"], textsize=40,
                 figur=("WI_redet2", WX, BODEN_Y, FHA), bis="frage"),
           *fig("WI", WX, BODEN_Y, FHA, [("frage", "skeptisch")], erst="cut"),
           pl("Rüge: Zum Schaden steht nichts im Urteil?", 70, 110, "frage", fill=PINK, size=34),
           pl("Zählt, was er über den Wert sagt?", 70, 190, "frage2", fill=PINK, size=34)]
folie([("h1", "Fall · Was steht im Urteil?"), (beim("h1", "Aber"), "Fall · Und der Schaden?"), ("w2", "Fall · „das Geld wert“"),
       ("frage", "Fall · Die Fragen")], els_a3)


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_204(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=34, zeilenabstand=1.30)
        els += e; y += 18
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_204("sv", [
    "Die Strafkammer des Landgerichts verurteilt Herrn Wichmann wegen Betrugs zu einer Freiheitsstrafe von 2 Jahren und "
    "6 Monaten. Nach den Urteilsgründen verkaufte er Frau Danner einen Oldtimer für 85.000 € und versicherte, der Wagen "
    "sei unfallfrei. Tatsächlich hatte der Wagen, wie Herr Wichmann wusste, einen schweren Unfallschaden. Frau Danner "
    "glaubte ihm und zahlte.",
    "Den Unfallschaden stützt die Kammer schlüssig auf ein Sachverständigengutachten. Was der Wagen mit diesem Schaden "
    "wert war, teilt das Urteil nicht mit. Strafschärfend wertet es den „hohen Schaden“.",
    "Rechtsanwältin Hellmers hat rechtzeitig Revision eingelegt. Herr Wichmann meint, der Wagen sei das Geld wert gewesen.",
], "Was prüft das Revisionsgericht auf die Sachrüge – und hält der Schuldspruch?")

# ===========================================================================================================================
# C Wortlautkarte § 337 StPO
# ===========================================================================================================================
PR = "Revision"
W337 = ["„(1) Die Revision kann nur darauf gestützt werden, daß das",
        "Urteil auf einer Verletzung des Gesetzes beruhe.",
        "(2) Das Gesetz ist verletzt, wenn eine Rechtsnorm nicht oder",
        "nicht richtig angewendet worden ist.“"]
w337, w337_y = wortlaut(80, 170, 1100, W337, "§ 337 StPO", "p337", marken=[
    (1, "Verletzung des Gesetzes", beim("p337", "Verletzung")), (1, "beruhe", beim("p337", "beruhen")),
    (2, "nicht oder", beim("p337b", "nicht")), (3, "nicht richtig angewendet", beim("p337b", "richtig"))], size=32)
folie([("p337", f"{PR} · nur Rechtsfehler, § 337 StPO"), ("p337b", f"{PR} › Gesetzesverletzung, § 337 Abs. 2"),
       ("zwei", f"{PR} › zwei Prüfpunkte"), ("beruh", f"{PR} › Beruhen, § 337 Abs. 1")], rechts_frei([
    *tafel("p337", "Revision: § 337 StPO"),
    *w337,
    z("Zu prüfen sind zwei Dinge:", 110, w337_y + 30, "zwei", "Bold", 36),
    blk(110, w337_y + 100, 505, 90, GELB, beim("zwei", "Gesetzesverletzung"), [("1. Gesetzesverletzung", "ExtraBold", 34, INK)]),
    blk(645, w337_y + 100, 505, 90, BLAU, "beruh", [("2. Beruhen", "ExtraBold", 34, INK)]),
    *requisit([("p337", ("tabler", "scale", 110, WEISS), "nur Rechtsfehler", WEISS),
               ("p337b", ("tabler", "file-x", 100, HELLROT), "nicht richtig angewendet", HELLROT),
               ("beruh", ("tabler", "link-off", 100, BLAU), "Beruhen", BLAU)]),
    *zwei([("p337", "ruhig"), ("beruh", "skeptisch")], [("p337", "ruhig"), ("zwei", "ernst")]),
]))

# ===========================================================================================================================
# D Allgemeine Sachrüge: § 344 Abs. 2 S. 1 StPO
# ===========================================================================================================================
PS_ = "Sachrüge"
W344 = ["„Aus der Begründung muß hervorgehen, ob das Urteil wegen",
        "Verletzung einer Rechtsnorm über das Verfahren oder wegen",
        "Verletzung einer anderen Rechtsnorm angefochten wird. …“"]
w344, w344_y = wortlaut(80, 245, 1100, W344, "§ 344 Abs. 2 S. 1 StPO", "p344", marken=[
    (1, "Rechtsnorm über das Verfahren", beim("p344", "Verfahren")), (2, "anderen Rechtsnorm", beim("p344", "andere"))], size=32)
folie([("sach", f"{PS_} · Fehler im materiellen Recht"), ("p344", f"{PS_} › § 344 Abs. 2 S. 1 StPO"),
       ("satz", f"{PS_} › allgemeine Sachrüge: 1 Satz"), ("umf", f"{PS_} › umfassende Prüfung")], rechts_frei([
    *tafel("sach", "Die allgemeine Sachrüge"),
    z("Fehler im materiellen Recht: Sachrüge", 110, 175, "sach", "Bold", 34),
    *w344,
    z("Es genügt ein Satz:", 110, w344_y + 28, "satz", "Bold", 34),
    blk(110, w344_y + 90, 1040, 90, GELB, beim("satz", "Ich"), [("„Ich rüge die Verletzung materiellen Rechts.“", "ExtraBold", 36, INK)]),
    *okz("umfassende sachlich-rechtliche Prüfung des Urteils", w344_y + 215, "umf", "Bold", 34, x=160),
    zit("BGH, Beschl. v. 21.4.2021 – 3 StR 300/20, Rn. 2", 160, w344_y + 265, "umf"),
    *requisit([("sach", ("tabler", "file-text", 100, WEISS), "materielles Recht", WEISS),
               ("satz", ("tabler", "writing-sign", 100, GELB), "1 Satz genügt", GELB),
               ("umf", ("tabler", "search", 100, BLAU), "umfassend geprüft", BLAU)]),
    *allein("HE", [("sach", "ruhig"), ("satz", "froh"), ("umf", "ernst")]),
]))

# ===========================================================================================================================
# E Prüfungsgrundlage: nur die Urteilsurkunde
# ===========================================================================================================================
folie([("grund", f"{PS_} › Grundlage: nur die Urteilsurkunde"), ("feld", f"{PS_} › Feststellungen, Beweiswürdigung, Strafzumessung"),
       ("akte", f"{PS_} › keine Akte, keine Rekonstruktion"), ("fremd", f"{PS_} › urteilsfremd: unbeachtlich"),
       ("verf", "Verfahrensfehler: Verfahrensrüge")], rechts_frei([
    *tafel("grund", "Grundlage: nur das Urteil"),
    z("Allein die Urteilsurkunde", 110, 175, "grund", "Bold", 36),
    zit("BGH, Urt. v. 12.5.2016 – 4 StR 569/15, Rn. 23", 110, 223, beim("grund", "Urteilsurkunde")),
    blk(110, 275, 330, 80, GELB, beim("feld", "Feststellungen"), [("Feststellungen", "ExtraBold", 30, INK)]),
    blk(465, 275, 330, 80, BLAU, beim("feld", "Beweiswürdigung"), [("Beweiswürdigung", "ExtraBold", 30, INK)]),
    blk(820, 275, 330, 80, GRUEN, beim("feld", "Strafzumessung"), [("Strafzumessung", "ExtraBold", 30, INK)]),
    *neinz("die Akte", 400, beim("akte", "Akte"), "Bold", 32, x=160),
    *neinz("Hauptverhandlung: keine Rekonstruktion", 452, beim("akte", "rekonstruiert"), "Bold", 32, x=160),
    zit("BGH, Urt. v. 17.7.2025 – 4 StR 298/24, Rn. 10", 160, 500, beim("akte", "rekonstruiert")),
    *neinz("„Das Geld wert“: urteilsfremd, außer Betracht", 568, beim("fremd", "urteilsfremd"), "Bold", 32, x=160),
    zit("BGH, Urt. v. 23.3.2023 – 3 StR 277/22, Rn. 28", 160, 616, beim("fremd", "urteilsfremd")),
    blk(110, 690, 1040, 80, LILA, "verf", [("Fehler im Ablauf der Hauptverhandlung: Verfahrensrüge", "ExtraBold", 30, INK)]),
    zit("eigene Folgen: „Sachrüge vs. Verfahrensrüge“, „Verfahrensrüge“", 110, 790, beim("verf", "eigene")),
    *requisit([("grund", ("tabler", "file-text", 100, WEISS), "Urteilsurkunde", WEISS),
               ("akte", ("tabler", "folder-off", 100, HELLROT), "Akte: nein", HELLROT),
               ("fremd", ("tabler", "message-off", 100, HELLROT), "urteilsfremd", HELLROT),
               ("verf", ("tabler", "gavel", 100, LILA), "Verfahrensrüge", LILA)]),
    *allein("WI", [("grund", "ruhig"), ("fremd", "sorge"), ("verf", "ruhig")]),
]))

# ===========================================================================================================================
# F Prüfungsstufen: a) Subsumtionsfehler
# ===========================================================================================================================
PP = "Prüfungsstufen"
folie([("stufen", f"{PP} · vier Stufen"), ("sa", f"{PP} › a) Subsumtionsfehler"), ("sa2", f"{PP} › a) hier: Tatsache (+)")], rechts_frei([
    *tafel("stufen", "Vier Stufen", size=46),
    *chips(None, "stufen"),
    *chips("a", "sa"),
    z("a) Subsumtionsfehler", 110, 190, "sa", "ExtraBold", 38),
    z("Feststellungen vollständig,", 110, 255, beim("sa", "Feststellungen"), size=34),
    z("aber das Gesetz falsch angewendet", 110, 303, beim("sa", "aber"), size=34),
    linienzug([(110, 380), (1150, 380)], "sa2", breite=3),
    z("Hier:", 110, 405, "sa2", "Bold", 34),
    *okz("„unfallfrei“ ist eine Tatsache, kein bloßes Werturteil", 460, beim("sa2", "Unfallfrei"), "Bold", 32, x=160),
    zit("BGH, Urt. v. 17.12.2019 – 1 StR 171/19, Rn. 47", 160, 510, beim("sa2", "Unfallfrei")),
    *okz("Täuschung richtig bejaht", 575, beim("sa2", "Täuschung"), "ExtraBold", 34, x=160),
    *requisit([("stufen", ("tabler", "list-numbers", 100, WEISS), "4 Stufen", WEISS),
               ("sa", ("tabler", "scale", 100, GELB), "Subsumtion", GELB),
               ("sa2", ("tabler", "file-check", 100, GRUEN), "Täuschung (+)", HELLGRUEN)]),
    *zwei([("stufen", "ruhig"), ("sa2", "skeptisch")], [("stufen", "ruhig"), ("sa", "ernst")]),
]))

# ===========================================================================================================================
# G Prüfungsstufen: b) Darstellungsmangel – Wortlautkarte § 267 Abs. 1 S. 1 StPO
# ===========================================================================================================================
W267 = ["„Wird der Angeklagte verurteilt, so müssen die Urteilsgründe",
        "die für erwiesen erachteten Tatsachen angeben, in denen die",
        "gesetzlichen Merkmale der Straftat gefunden werden. …“"]
w267, w267_y = wortlaut(80, 250, 1100, W267, "§ 267 Abs. 1 S. 1 StPO", "p267", marken=[
    (1, "für erwiesen erachteten Tatsachen", beim("p267", "erwiesen")), (2, "gesetzlichen Merkmale", beim("p267", "gesetzlichen"))],
    size=32)
folie([("sb", f"{PP} › b) Darstellungsmangel"), ("p267", f"{PP} › b) § 267 Abs. 1 S. 1 StPO"),
       ("sb2", f"{PP} › b) Tatsachen für jedes Merkmal")], rechts_frei([
    *tafel("sb", "Vier Stufen", size=46),
    *chips("b", "sb"),
    z("b) Darstellungsmangel", 110, 175, "sb", "ExtraBold", 38),
    *w267,
    blk(110, w267_y + 30, 1040, 80, GELB, beim("sb2", "jedes"), [("Für jedes Merkmal: festgestellte Tatsachen", "ExtraBold", 34, INK)]),
    *neinz("Fehlen sie: keine Nachprüfung der Subsumtion", w267_y + 145, beim("sb2", "Fehlen"), "Bold", 32, x=160),
    zit("BGH, Beschl. v. 19.2.2025 – 1 StR 482/24, Rn. 6", 160, w267_y + 195, beim("sb2", "Fehlen")),
    *requisit([("sb", ("tabler", "file-alert", 100, WEISS), "Darstellungsmangel", HELLROT),
               ("p267", ("tabler", "list-check", 100, WEISS), "§ 267 Abs. 1 S. 1", WEISS),
               (beim("sb2", "Fehlen"), ("tabler", "puzzle-off", 100, HELLROT), "Lücke", HELLROT)]),
    *zwei([("sb", "ruhig"), ("sb2", "sorge")], [("sb", "ernst"), ("sb2", "skeptisch")]),
]))

# ===========================================================================================================================
# H Prüfungsstufen: c) Beweiswürdigung
# ===========================================================================================================================
BW = [("lückenhaft", "lückenhaft"), ("widersprüchlich", "widersprüchlich"), ("unklar", "unklar"),
      ("Verstoß gegen Denkgesetze", "Denkgesetze"), ("oder gesicherte Erfahrungssätze", "Erfahrungssätze")]
els_c = [*tafel("sc", "Vier Stufen", size=46), *chips("c", "sc"),
         z("c) Beweiswürdigung", 110, 175, "sc", "ExtraBold", 38),
         z("Sache des Tatgerichts; angreifbar nur, wenn sie", 110, 245, beim("sc2", "Sache"), "Bold", 34)]
for i, (t, w) in enumerate(BW):
    els_c.append(z(f"– {t}", 150, 300 + i * 50, beim("sc2", w), size=34))
els_c += [zit("BGH, Beschl. v. 13.4.2026 – 1 StR 52/26, Rn. 6", 150, 560, beim("sc2", "Erfahrungssätze")),
          linienzug([(110, 625), (1150, 625)], "sc3", breite=3),
          *okz("Unfallschaden: schlüssig auf Sachverständigen gestützt", 650, beim("sc3", "schlüssig"), "Bold", 32, x=160),
          *requisit([("sc", ("tabler", "zoom-question", 100, WEISS), "Beweiswürdigung", WEISS),
                     ("sc3", ("tabler", "file-certificate", 100, GRUEN), "Gutachten: schlüssig", HELLGRUEN)]),
          *allein("HE", [("sc", "ruhig"), ("sc3", "froh")])]
folie([("sc", f"{PP} › c) Beweiswürdigung"), ("sc2", f"{PP} › c) nur Rechtsfehler"), ("sc3", f"{PP} › c) hier: schlüssig (+)")],
      rechts_frei(els_c))

# ===========================================================================================================================
# I Prüfungsstufen: d) Strafzumessung
# ===========================================================================================================================
folie([("sd", f"{PP} › d) Strafzumessung"), ("sd2", f"{PP} › d) nur Rechtsfehler"), ("sd3", f"{PP} › d) „hoher Schaden“ – unbeziffert")],
      rechts_frei([
    *tafel("sd", "Vier Stufen", size=46), *chips("d", "sd"),
    z("d) Strafzumessung", 110, 175, "sd", "ExtraBold", 38),
    z("Sache des Tatgerichts", 110, 245, beim("sd2", "Sache"), "Bold", 34),
    z("Eingriff nur bei Rechtsfehlern, etwa:", 110, 300, beim("sd2", "Rechtsfehlern"), size=34),
    z("– Erwägungen in sich fehlerhaft", 150, 355, beim("sd2", "Erwägungen"), size=34),
    z("– Strafe löst sich vom gerechten Schuldausgleich", 150, 410, beim("sd2", "Strafe"), size=34),
    zit("BGH, Urt. v. 16.7.2026 – 5 StR 125/26, Rn. 8", 150, 462, beim("sd2", "Strafe")),
    karte(110, 535, 1040, 110, "sd3", fill=ZITAT, rund=18, schatten=6, rand=4),
    z("Urteil: strafschärfend „der hohe Schaden“", 140, 560, "sd3", "Bold", 34, rechts=1140),
    z("… den es nirgends beziffert", 140, 670, beim("sd3", "nirgends"), "ExtraBold", 34, farbe=DROT),
    *requisit([("sd", ("tabler", "scale", 100, WEISS), "Strafzumessung", WEISS),
               ("sd3", ("tabler", "zoom-question", 100, HELLROT), "Schaden: wie hoch?", HELLROT)]),
    *allein("WI", [("sd", "ruhig"), ("sd3", "skeptisch")]),
]))

# ===========================================================================================================================
# K Der Fall: kein festgestellter Vermögensschaden (Waage)
# ===========================================================================================================================
PF = "Fall › b) Darstellungsmangel"
folie([("schaden", f"{PF}: der Schaden"), ("saldo", f"{PF} › Gesamtsaldierung"), ("kauf", f"{PF} › Kauf: Sache den Preis nicht wert?"),
       ("preis", f"{PF} › 85.000 € gezahlt"), ("wert", f"{PF} › Wert des Wagens?"), ("luecke", f"{PF} › Wert nicht festgestellt"),
       ("traegt", f"{PF} › Schuldspruch hält nicht stand (-)")], rechts_frei([
    *tafel("schaden", "Der Vermögensschaden", size=46),
    z("Schaden: Gesamtwert gemindert, ohne ausgleichenden Zuwachs", 110, 170, beim("saldo", "Vermögensschaden"), "Bold", 30),
    zit("BGH, Beschl. v. 19.7.2023 – 2 StR 77/22, Rn. 8", 110, 212, beim("saldo", "Vermögensschaden")),
    z("Kauf: geschädigt regelmäßig nur, wenn die Sache objektiv", 110, 262, beim("kauf", "Wer"), "Bold", 30),
    z("den vereinbarten Preis nicht wert ist", 110, 302, beim("kauf", "regelmäßig"), "Bold", 30),
    zit("BGH, Beschl. v. 13.8.2025 – 2 StR 283/25, Rn. 10", 110, 344, beim("kauf", "regelmäßig")),
    tafelicon(ficon("tabler", "scale", 630, 640, 300, "preis", fuell=WEISS)),
    tafelicon(ficon("tabler", "cash-banknote", 330, 560, 120, "preis", fuell=GRUEN)),
    pl("85.000 € gezahlt", 330, 590, "preis", fill=GRUEN, size=32, anker="m"),
    tafelicon(ficon("tabler", "car", 930, 560, 150, "wert", fuell=ROT)),
    pl("Wert des Wagens: ?", 930, 590, "wert", fill=HELLROT, size=32, anker="m"),
    z("Wert: nicht festgestellt", 640, 660, "luecke", "ExtraBold", 32, farbe=DROT),
    blk(110, 720, 1040, 80, HELLROT, "traegt", [("Feststellungen belegen keinen Vermögensschaden", "ExtraBold", 34, INK)]),
    z("Schuldspruch wegen Betrugs hält nicht stand (-)", 110, 818, beim("traegt", "Schuldspruch"), "Bold", 30),
    zit("BGH 2 StR 283/25, Rn. 11; 2 StR 77/22, Rn. 7", 110, 858, beim("traegt", "Schuldspruch")),
    *requisit([("schaden", ("tabler", "zoom-question", 100, WEISS), "Schaden?", WEISS),
               ("preis", ("tabler", "cash-banknote", 110, GRUEN), "85.000 €", GRUEN),
               ("luecke", ("tabler", "puzzle-off", 100, HELLROT), "Lücke im Urteil", HELLROT),
               ("traegt", ("tabler", "file-x", 100, HELLROT), "Schuldspruch (-)", HELLROT)]),
    *zwei([("schaden", "ruhig"), ("luecke", "skeptisch"), ("traegt", "froh")], [("schaden", "ernst"), ("traegt", "froh")]),
]))

# ===========================================================================================================================
# L Ergebnis: Beruhen, Aufhebung, Zurückverweisung
# ===========================================================================================================================
PE = "Ergebnis"
folie([("beruhen", f"{PE} › Beruhen, § 337 Abs. 1 StPO"), ("strafe", f"{PE} › die Strafe fällt mit"),
       ("selbst", f"{PE} › keine eigene Sachentscheidung"), ("aufh", f"{PE} › Aufhebung, § 353 StPO"),
       ("zur", f"{PE} › Zurückverweisung, § 354 Abs. 2 StPO")], rechts_frei([
    *tafel("beruhen", "Ergebnis der Sachrüge"),
    *okz("Beruhen: nicht auszuschließen, dass der Wagen", 180, beim("beruhen", "nicht"), "Bold", 32, x=160),
    z("den Preis wert war – dann fehlte der Schaden", 160, 228, beim("beruhen", "Dann"), "Bold", 32),
    zit("BGH, Beschl. v. 13.8.2025 – 2 StR 283/25, Rn. 13", 160, 276, beim("beruhen", "Dann")),
    z("Mit dem Schuldspruch fällt die Strafe.", 110, 345, "strafe", "Bold", 34),
    *neinz("selbst entscheiden: nein – neue Feststellungen nötig", 410, beim("selbst", "neue"), "Bold", 32, x=160),
    zit("vgl. § 354 Abs. 1 StPO", 160, 458, beim("selbst", "neue")),
    blk(110, 525, 1040, 80, GELB, "aufh", [("Aufhebung des Urteils, § 353 StPO", "ExtraBold", 34, INK)]),
    blk(110, 635, 1040, 110, BLAU, "zur", [("Zurückverweisung an eine andere", "ExtraBold", 34, INK),
                                           ("Strafkammer, § 354 Abs. 2 StPO", "ExtraBold", 34, INK)]),
    *requisit([("beruhen", ("tabler", "link-off", 100, BLAU), "Beruhen (+)", BLAU),
               ("selbst", ("tabler", "hand-stop", 100, HELLROT), "neue Feststellungen", HELLROT),
               ("aufh", ("tabler", "file-x", 100, GELB), "aufgehoben", GELB),
               ("zur", ("tabler", "arrow-back-up", 100, BLAU), "andere Strafkammer", BLAU)]),
    *zwei([("beruhen", "ruhig"), ("aufh", "froh")], [("beruhen", "ernst"), ("zur", "froh")]),
]))

# ===========================================================================================================================
# M Klausurtipp (Lexi): Revisionsbegründung
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · die Revisionsbegründung"), ("k1", "Klausurtipp · 1. allgemeine Sachrüge"),
       ("k2", "Klausurtipp · 2. Schuldspruch, dann Strafzumessung"), ("k3", "Klausurtipp · 3. eng am Urteil formulieren"),
       ("k4", "Klausurtipp · nur Urteilsgründe, nie die Akte")], [
    *tafel("tipp", "Klausurtipp: Revisionsbegründung", fill=HELL),
    warnung_i(150, 205, "tipp", gr=24),
    z("1. Allgemeine Sachrüge erheben:", 200, 180, "k1", "Bold", 32),
    z("„Ich rüge die Verletzung materiellen Rechts.“", 200, 226, beim("k1", "Satz"), "ExtraBold", 32),
    z("2. Ausführen: erst der Schuldspruch, Merkmal für", 200, 300, "k2", "Bold", 32),
    z("Merkmal, dann die Strafzumessung", 200, 346, beim("k2", "Merkmal"), "Bold", 32),
    z("3. Eng am Urteil formulieren:", 200, 420, "k3", "Bold", 32),
    z("„Die Feststellungen belegen keinen Vermögensschaden;", 200, 466, beim("k3", "Die"), size=30),
    z("den Wert des Wagens teilt das Urteil nicht mit.“", 200, 508, beim("k3", "den"), size=30),
    blk(130, 590, 1020, 80, HELLGRUEN, "k4", [("Nur mit den Urteilsgründen, nie mit der Akte", "ExtraBold", 32, INK)]),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# N Prüfschema
# ===========================================================================================================================
REIHEN = [("s1", 0, "I. Allgemeine Sachrüge, § 344 Abs. 2 S. 1 StPO", True),
          ("s2", 0, "II. Grundlage: allein die Urteilsurkunde", True),
          ("s3", 0, "III. Schuldspruch", True),
          (beim("s3", "Subsumtion"), 1, "1. Subsumtion, § 337 Abs. 2 StPO", False),
          (beim("s3", "Darstellung"), 1, "2. Darstellung: Tatsachen für jedes Merkmal, § 267 Abs. 1 S. 1 StPO", False),
          (beim("s3", "Beweiswürdigung"), 1, "3. Beweiswürdigung: Lücken, Widersprüche, Denkgesetze", False),
          ("s4", 0, "IV. Strafzumessung", True),
          ("s5", 0, "V. Beruhen, § 337 Abs. 1 StPO", True),
          (beim("s5", "Aufhebung"), 1, "Aufhebung, § 353 StPO; Zurückverweisung, § 354 Abs. 2 StPO", False)]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfschema: die Sachrüge"), 110, 90, "sch", 46),
           z("Revisionsbegründung, Strafurteil", 110, 160, "sch", "Bold", 32, farbe=TEXT, rechts=1800)]
y = 240
for c, ebene, text, fett in REIHEN:
    x = (130, 200)[ebene]
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 38 if ebene == 0 else 32, rechts=1800))
    y += {0: 78, 1: 62}[ebene]
assert y <= 970, y
folie([("sch", "Prüfschema"), ("s1", "Prüfschema › I. Allgemeine Sachrüge"), ("s2", "Prüfschema › II. Grundlage: Urteil"),
       ("s3", "Prüfschema › III. Schuldspruch"), ("s4", "Prüfschema › IV. Strafzumessung"),
       ("s5", "Prüfschema › V. Beruhen, Aufhebung")], els_sch)

# ===========================================================================================================================
# O Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Die Sachrüge prüft ", 0), ("nur das Urteil", "a"), (".", 0)]], 750, 290, 44, "merke",
                {"a": beim("merke", "nur")}),
    *markertext([[("Fehlt dort die ", 0), ("Tatsache für ein Merkmal", "b"), (",", 0)],
                 [("trägt das Urteil den Schuldspruch nicht,", 0)],
                 [("und aus der Akte füllt das Revisionsgericht", 0)],
                 [("die ", 0), ("Lücke", "c"), (" nicht.", 0)]], 750, 450, 40, "m2",
                {"b": beim("m2", "Tatsache"), "c": beim("m2", "Lücke")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
