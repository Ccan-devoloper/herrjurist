"""Folge 163 · Betrunken Auto fahren: a.l.i.c. im Straßenverkehr – BGHSt 42, 235 · Serienstandard Open Peeps (Katzenkönig).
Fall (fiktiv): Leopold weiß schon beim ersten Bier in der Kneipe, dass er nachher selbst heimfährt; nach Mitternacht fährt er
ruhig durch die Nacht und gerät am Ortseingang in eine Polizeikontrolle (kein Unfall); bei Fahrtantritt war er schuldunfähig.
Szenen laut ../SZENENPLAN.md: A1 Kneipe, A2 Nachtfahrt und Kontrolle (Nachtverlauf, weil der Fall nachts spielt), B Sachverhalt,
C § 20 StGB (Wortlautkarte, Koinzidenzprinzip), D a.l.i.c. knapp (Zeitstrahl Ausnahmemodell/Tatbestandsmodell), E der echte
Fall (BGHSt 42, 235, ohne Figuren, ohne Unfallbild), F1/F2 Tatbestandsmodell scheitert (Zitatkarte Rn. 17, „Führen“),
G Ausnahmemodell scheitert (Wortlautkarte Art. 103 Abs. 2 GG), H offen gelassen und § 222, I § 323a (Wortlautkarte),
J Lösung, K Klausurtipp (Lexi), L Prüfschema, M Merksatz (Lexi).
Alkohol nur als neutrale Glas-Icons (Tabler glass/glass-full), kein Anstoßen, keine Flaschen; Fahrt als ruhige Nachtfahrt.
Ein Handlungsgeräusch (Auto fährt heran und hält, ../geraeusche_herkunft.json). Namensschild jeder Figur, solange sie im Bild
ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz als eigene Kopie aus Folge 140 (gemeinsame
Dateien unverändert); neu: stehtisch(), fenster(), strasse_nacht(), ortsschild(), fahrt(), zeitstrahl-Bausteine.
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

bausteine.FIGORDNER = "op_163/"

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
        if n.startswith(("bild:", "ficon:", "bank")) or "/op_163/" in n:
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
BG_FARBE["nacht"] = None                     # Nacht = Verlauf, erzeugt im Renderer (wie Folgen 001, 148)
PFAD_FARBE["nacht"] = (255, 255, 255, 170)
ASPH_N = (78, 84, 108, 255)                  # Asphalt nachts
GRAS_N = (62, 92, 78, 255)
BAUM_N = (96, 150, 110, 255)
NACHT = (44, 52, 98, 255)
STR_O, STR_U = 740, 880                      # Fahrbahn nachts (Seitenansicht)
FAHR = 868                                   # Unterkante Autos/Figuren auf der Fahrbahn
FH = 430                                     # Figurenhöhe in der Kontrolle
TUER = TUERKIS


def nachtfolie(pfade, els):
    pruefe_im_bild(els)
    FOLIEN.append(dict(bg="nacht", pfade=pfade, els=els))


def strasse_nacht(cue):
    """Landstraße nachts in Seitenansicht: Asphalt mit gestrichelter Mittellinie, dunkles Gras darunter."""
    s = 2
    im = Image.new("RGBA", (1860 * s, (1000 - STR_O) * s))
    dr = ImageDraw.Draw(im)
    dr.rectangle((0, 0, 1860 * s, (STR_U - STR_O) * s), fill=ASPH_N)
    dr.line((0, 0, 1860 * s, 0), fill=INK, width=6 * s)
    dr.line((0, (STR_U - STR_O) * s, 1860 * s, (STR_U - STR_O) * s), fill=INK, width=6 * s)
    for x in range(10, 1860, 120):
        dr.rounded_rectangle((x * s, 66 * s, (x + 60) * s, 74 * s), 4 * s, fill=(230, 232, 240, 255))
    dr.rectangle((0, (STR_U - STR_O + 3) * s, 1860 * s, (1000 - STR_O) * s), fill=GRAS_N)
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    return El(im, 30, STR_O, cue, "cut", 0.0, None, name="strasse")


def ortsschild(cx, boden_, cue, anim="pop"):
    """Ortseingangsschild als Grundform: gelbe Tafel mit zwei dunklen Schriftbalken (ohne realen Ortsnamen), Pfosten."""
    s = 2
    w, h, hp = 170, 110, 90
    im = Image.new("RGBA", ((w + 12) * s, (h + hp + 12) * s))
    dr = ImageDraw.Draw(im)
    dr.rounded_rectangle(((w / 2 - 2) * s, h * s, (w / 2 + 14) * s, (h + hp + 6) * s), 4 * s, fill=(150, 150, 150, 255),
                         outline=INK, width=3 * s)
    dr.rounded_rectangle((6 * s, 6 * s, (w + 6) * s, (h + 6) * s), 10 * s, fill=GELB, outline=INK, width=5 * s)
    dr.rounded_rectangle((34 * s, 30 * s, (w - 22) * s, 48 * s), 6 * s, fill=(70, 70, 70, 255))
    dr.rounded_rectangle((50 * s, 66 * s, (w - 38) * s, 82 * s), 6 * s, fill=(70, 70, 70, 255))
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    return El(im, cx - im.width / 2, boden_ - im.height, cue, anim, 0.0, None, name="ortsschild")


def auto(fuell, cx, unten, cue, breite=300, bis=None, anim="cut", spiegeln=False):
    return ficon("tabler", "car", cx, unten, breite, cue, fuell=fuell, bis=bis, anim=anim, spiegeln=spiegeln)


def fahrt(fuell, von, nach, unten, start, dauer, n=12, bis=None, breite=300):
    """Ruhige Fahrt als Folge kurzer Positionen (harte Schnitte, Icon nicht umgezeichnet), sanft abbremsend."""
    c, t0 = start
    els = []
    for i in range(n + 1):
        p = i / n
        q = 1 - (1 - p) ** 2                      # gleichmäßig losrollen, sanft bis zum Halt abbremsen
        a_ = (c, round(t0 + dauer * i / n, 3))
        b_ = (c, round(t0 + dauer * (i + 1) / n, 3)) if i < n else bis
        els.append(auto(fuell, von + (nach - von) * q, unten, a_, breite=breite, bis=b_))
    return els


BODEN_K = 900                                # Boden der Kneipe
HOLZ = (214, 160, 110, 255)
TX = 760                                     # Stehtisch: Mitte


def stehtisch(cue):
    """Stehtisch der Kneipe: runde Platte (Seitenansicht), Säule, Fuß; Holzfarbe mit Tuschekontur."""
    s = 2
    w, h = 300, BODEN_K - 600
    im = Image.new("RGBA", ((w + 10) * s, (h + 10) * s))
    dr = ImageDraw.Draw(im)
    dr.rounded_rectangle((5 * s, 5 * s, (w + 5) * s, 37 * s), 14 * s, fill=HOLZ, outline=INK, width=5 * s)
    dr.rectangle(((w / 2 - 6) * s, 37 * s, (w / 2 + 16) * s, (h - 14) * s), fill=HOLZ, outline=INK, width=4 * s)
    dr.rounded_rectangle(((w / 2 - 80) * s, (h - 18) * s, (w / 2 + 90) * s, (h + 4) * s), 8 * s, fill=HOLZ, outline=INK, width=4 * s)
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    return El(im, TX - w / 2 - 5, 600 - 5, cue, "cut", 0.0, None, name="stehtisch")


FE = (1400, 70, 440, 310)                    # Fenster der Kneipe (x, y, w, h)


def fenster(cue):
    """Fenster mit Nachthimmel und Kreuzsprosse (Tuschekontur)."""
    x, y, w, h = FE
    s = 2
    im = Image.new("RGBA", ((w + 12) * s, (h + 12) * s))
    dr = ImageDraw.Draw(im)
    dr.rounded_rectangle((6 * s, 6 * s, (w + 6) * s, (h + 6) * s), 12 * s, fill=NACHT, outline=INK, width=7 * s)
    dr.line(((w / 2 + 6) * s, 6 * s, (w / 2 + 6) * s, (h + 6) * s), fill=(235, 225, 205, 255), width=8 * s)
    dr.line((6 * s, (h * 0.42 + 6) * s, (w + 6) * s, (h * 0.42 + 6) * s), fill=(235, 225, 205, 255), width=8 * s)
    dr.rounded_rectangle((6 * s, 6 * s, (w + 6) * s, (h + 6) * s), 12 * s, outline=INK, width=7 * s)
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    return El(im, x - 6, y - 6, cue, "cut", 0.0, None, name="fenster")


X1, X2 = 1430, 1730                         # zwei Figuren neben der Tafel
FB, FR_ = 930, 480                          # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"LE": "Leopold", "PO": "Polizistin", "FR": "Freund", "FN": "Freundin"}
NFARBE = {"LE": TUER, "PO": BLAU, "FR": WEISS, "FN": LILA}
HELLROT = (253, 232, 228, 255)
HELLGRUEN = (232, 247, 233, 255)


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


def stehend(k, x, folge, unten=FB, hoehe=FR_):
    return [*fig(k, x, unten, hoehe, folge), ns(NAME[k], x, unten, folge[0][0], NFARBE[k], d=0.1)]


PA = "A. § 316 StGB › III. Schuld"


def tafelicon(*a, **k):
    """Icon als Teil einer Tafelgrafik (Zeitstrahl) – bewusst innerhalb der Tafel."""
    e = ficon(*a, **k)
    e.name = "tafelicon:" + e.name.split(":", 1)[1]
    return e
PB = "BGHSt 42, 235"

# ===========================================================================================================================
# A1 Fall: Freitagabend in der Kneipe (Cremegrund, Fenster mit Nachthimmel)
# ===========================================================================================================================
LEX, FRX, FNX = 1010, 330, 520              # Leopold rechts am Tisch (blickt nach links), Freund/Freundin links (blicken nach rechts)
KH = 470                                    # Figurenhöhe in der Kneipe
folie([(NULL, "Fall · In der Kneipe"), ("erstes", "Fall · Das erste Bier"), ("mitt", "Fall · Nach Mitternacht")], [
    hart(linienzug([(60, BODEN_K), (1860, BODEN_K)], NULL, breite=7)),
    hart(fenster(NULL)),
    hart(mond(1770, 140, 34, NULL)),
    hart(stehtisch(NULL)),
    hart(pl("Freitagabend in der Kneipe", 70, 30, NULL, fill=GELB, size=40)),
    # Wanduhr: 20 Uhr → spät → Mitternacht (Zwiebelschale)
    hart(ficon("tabler", "clock-hour-8", 1080, 150, 90, NULL, fuell=WEISS, anim="cut", bis="spaet")),
    ficon("tabler", "clock-hour-11", 1080, 150, 90, "spaet", fuell=WEISS, anim="cut", bis="mitt"),
    ficon("tabler", "clock-hour-12", 1080, 150, 90, "mitt", fuell=WEISS, anim="cut"),
    # Freund und Freundin stehen ab 0,0 s links am Tisch (sprechen nicht; Mund zu)
    hart(peep_voll("FR_froh_r", FRX, BODEN_K, KH, NULL, anim="cut")),
    hart(ns("Freund", FRX, BODEN_K, NULL, WEISS)),
    hart(peep_voll("FN_froh_r", FNX, BODEN_K, KH, NULL, anim="cut")),
    hart(ns("Freundin", FNX, BODEN_K, NULL, LILA)),
    hart(ficon("tabler", "glass-full", 640, 600, 52, NULL, fuell=WEISS, anim="cut")),
    hart(ficon("tabler", "glass-full", 695, 600, 52, NULL, fuell=WEISS, anim="cut")),
    # Leopold kommt dazu
    pl("Leopold trifft Freunde", 70, 115, "leo", fill=TUER, size=32),
    *fig("LE", LEX, BODEN_K, KH, [(beim("leo", "Leopold"), "froh")], bis="l1", erst="pop"),
    *redet("LE_froh_redet", LEX, BODEN_K, KH, "l1", "spaet"),
    *fig("LE", LEX, BODEN_K, KH, [("spaet", "froh"), ("mitt", "muede")], erst="cut"),
    ns("Leopold", LEX, BODEN_K, beim("leo", "Leopold"), TUER, d=0.1),
    # Sein Auto steht vor der Tür (im Fenster)
    auto(TUER, 1560, FE[1] + FE[3] - 14, "auto", breite=220, anim="pop"),
    pl("Sein Auto steht vor der Tür", 1620, 405, "auto", fill=WEISS, size=30, anker="m"),
    # Das erste Bier: neutrales Glas, Autoschlüssel daneben
    ficon("tabler", "glass-full", 805, 600, 52, "erstes", fuell=WEISS),
    ficon("tabler", "key", 752, 600, 40, beim("erstes", "klar"), fuell=GELB),
    pl("1. Bier: Er fährt nachher selbst", 70, 190, beim("erstes", "klar"), fill=WEISS, size=32),
    blase("sprech", 600, 210, "l1", 1010, 300, inhalt=["Ich fahre nachher selbst heim.", "Das geht schon."], textsize=34,
          figur=("LE_froh_redet", LEX, BODEN_K, KH), bis="spaet"),
    # Es bleibt nicht bei einem Bier (zwei weitere neutrale Gläser)
    pl("Es bleibt nicht bei einem Bier.", 70, 265, "spaet", fill=WEISS, size=32),
    ficon("tabler", "glass", 852, 600, 46, beim("spaet", "bleibt"), fuell=WEISS),
    ficon("tabler", "glass", 893, 600, 46, beim("spaet", "einem"), fuell=WEISS),
    pl("Nach Mitternacht: Leopold steigt ins Auto", 70, 340, "mitt", fill=HELLROT, size=32),
])

# ===========================================================================================================================
# A2 Fall: Nachtfahrt und Polizeikontrolle am Ortseingang (Nachtverlauf; ruhige Fahrt, kein Unfall)
# ===========================================================================================================================
CX0, CX1 = 260, 820                         # Leopolds Auto: Start, Halt vor der Kontrolle
LKX, OSX, POX, PWX = 1065, 1265, 1465, 1735  # Leopold (blickt nach rechts), Ortsschild, Polizistin (blickt nach links), Streifenwagen
FAHRT = (beim("fahrt", "fährt")[0], beim("fahrt", "fährt")[1])
ANK = fahrt(TUER, CX0, CX1, FAHR, FAHRT, 3.6, n=24)
ANK[0] = szene(ANK[0], "163ankunft*", 0.9, 0.0)          # Heranfahren und Halten: Geräusch mit der sichtbaren Bewegung
nachtfolie([("fahrt", "Fall · Die Heimfahrt"), ("kontr", "Fall · Die Polizeikontrolle"),
            ("gut", "Fall · Schuldunfähig bei Fahrtantritt"), ("frage", "Fall · Die Frage"), ("var", "Fall · Variante")], [
    strasse_nacht("fahrt"),
    mond(1780, 120, 46, "fahrt", d=0.0),
    ficon("tabler", "trees", 150, STR_O + 4, 180, "fahrt", fuell=BAUM_N, anim="cut"),
    ficon("tabler", "tree", 330, STR_O + 4, 130, "fahrt", fuell=BAUM_N, anim="cut"),
    pl("Nach Mitternacht: ruhige Fahrt nach Hause", 70, 30, "fahrt", fill=GELB, size=36, bis="blut"),
    # Kontrolle am Ortseingang
    ortsschild(OSX, STR_O + 6, "kontr"),
    ficon("fluent-emoji-flat", "police-car", PWX, FAHR, 300, "kontr"),
    pl("Polizeikontrolle am Ortseingang", 70, 115, "kontr", fill=BLAU, size=32, bis="blut"),
    *fig("PO", POX, FAHR + 8, FH, [(beim("kontr", "Polizeikontrolle"), "ruhig")], bis="p1", erst="pop"),
    *redet("PO_redet", POX, FAHR + 8, FH, "p1", "l2"),
    *fig("PO", POX, FAHR + 8, FH, [("l2", "ernst")], erst="cut"),
    ns("Polizistin", POX, FAHR + 8, beim("kontr", "Polizeikontrolle"), BLAU, d=0.1),
    blase("sprech", 640, 220, "p1", 1290, 260, inhalt=["Guten Abend, Verkehrskontrolle.", "Haben Sie etwas getrunken?"],
          textsize=34, figur=("PO_redet", POX, FAHR + 8, FH), bis="l2"),
    # Leopold steigt aus und antwortet
    *fig("LE", LKX, FAHR + 8, FH, [("p1", "ruhig_r")], bis="l2", erst="pop"),
    *redet("LE_redet_r", LKX, FAHR + 8, FH, "l2", "blut"),
    *fig("LE", LKX, FAHR + 8, FH, [("blut", "muede_r"), ("gut", "still_r"), ("frage", "denkt_r")], erst="cut"),
    ns("Leopold", LKX, FAHR + 8, "p1", TUER, d=0.1),
    blase("sprech", 430, 160, "l2", 760, 320, inhalt=["Nur ein paar Bier."], textsize=34,
          figur=("LE_redet_r", LKX, FAHR + 8, FH), bis="blut"),
    # Blutprobe, Sachverständiger, Frage, Variante (nur als Text)
    ficon("tabler", "test-pipe", 600, 95, 60, "blut", fuell=HELLROT),
    pl("Blutprobe: stark betrunken", 70, 30, "blut", fill=WEISS, size=32),
    pl("Sachverständiger: bei Fahrtantritt schuldunfähig", 70, 115, beim("gut", "Sachverständiger"), fill=HELLROT, size=32),
    pl("§ 316 StGB trotz Schuldunfähigkeit?", 70, 200, "frage", fill=PINK, size=34),
    pl("Er wusste es doch schon beim 1. Bier.", 70, 285, "frage2", fill=PINK, size=32),
    pl("Variante: Ein anderer Fahrer muss scharf bremsen – § 315c?", 70, 370, "var", fill=LILA, size=32),
    *ANK,
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_163(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=38, zeilenabstand=1.32)
        els += e; y += 18
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=33))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_163("sv", [
    "Leopold verbringt einen Freitagabend mit Freunden in der Kneipe; sein Auto steht vor der Tür. Schon beim ersten Bier "
    "ist ihm klar, dass er nachher selbst nach Hause fahren wird: „Das geht schon.“ Er trinkt bewusst weiter; es bleibt "
    "nicht bei einem Bier.",
    "Nach Mitternacht fährt Leopold los. Am Ortseingang gerät er in eine Polizeikontrolle. Die Blutprobe zeigt, dass er "
    "stark betrunken war. Ein Sachverständiger stellt fest: Bei Fahrtantritt war Leopold schuldunfähig. Gefährdet wurde "
    "niemand.",
    "Variante: Unterwegs muss ein anderer Fahrer scharf bremsen; beinahe wäre es zum Zusammenstoß gekommen.",
], "Ist Leopold nach § 316 StGB strafbar – und in der Variante nach § 315c StGB?")

# ===========================================================================================================================
# C § 20 StGB (Wortlautkarte), Koinzidenzprinzip
# ===========================================================================================================================
W20 = ["„Ohne Schuld handelt, wer bei Begehung der Tat wegen einer",
       "krankhaften seelischen Störung, wegen einer tiefgreifenden",
       "Bewußtseinsstörung oder wegen einer Intelligenzminderung",
       "oder einer schweren anderen seelischen Störung unfähig ist,",
       "das Unrecht der Tat einzusehen oder nach dieser Einsicht zu",
       "handeln.“"]
w20, w20_y = wortlaut(80, 160, 1100, W20, "§ 20 StGB", "p20", marken=[
    (0, "bei Begehung der Tat", beim("p20", "Begehung")), (3, "unfähig ist,", beim("p20", "unfähig")),
    (4, "das Unrecht der Tat einzusehen", beim("p20", "einzusehen")), (4, "nach dieser Einsicht zu", beim("p20", "Einsicht")),
    (5, "handeln.", beim("p20", "Einsicht"))], size=30)
ZY = w20_y + 175
folie([("p20", f"{PA} › § 20 StGB"), ("koinz", f"{PA} › Koinzidenzprinzip")], rechts_frei([
    *tafel("p20", "§ 20 StGB: Schuld bei Begehung der Tat"),
    *w20,
    z("schwerer Rausch: Steuerungsfähigkeit aufgehoben", 110, w20_y + 22, "stfg", "Bold", 32),
    zit("BGHSt 42, 235 (BGH, Urt. v. 22.8.1996 – 4 StR 217/96), Rn. 14", 110, w20_y + 70, beim("stfg", "Steuerungsfähigkeit")),
    blk(110, w20_y + 112, 1040, 56, GELB, "koinz", [("Koinzidenzprinzip: Schuld bei Begehung der Tat", "ExtraBold", 32, INK)]),
    blk(110, ZY, 470, 120, GRUEN, "z1", [("1. Bier: schuldfähig", "ExtraBold", 32, INK), ("aber fährt noch nicht", "Regular", 30, INK)]),
    pfeil(600, ZY + 60, 660, ZY + 60, beim("z2", "Am"), breite=8, kopf=24),
    blk(680, ZY, 470, 120, HELLROT, "z2", [("am Steuer: fährt", "ExtraBold", 32, INK), ("aber schuldunfähig", "Regular", 30, INK)]),
    *requisit([("p20", ("tabler", "book", 100, WEISS), "§ 20 StGB", GELB),
               ("koinz", ("tabler", "clock", 100, WEISS), "Zeitpunkt", WEISS),
               ("z1", ("tabler", "glass-full", 80, WEISS), "1. Bier", GRUEN),
               ("z2", ("tabler", "steering-wheel", 100, WEISS), "am Steuer", HELLROT)]),
    *stehend("LE", FX, [("p20", "ruhig"), ("stfg", "muede"), ("koinz", "denkt"), ("z2", "sorge")]),
]))

# ===========================================================================================================================
# D actio libera in causa: Ausnahmemodell und Tatbestandsmodell (Zeitstrahl)
# ===========================================================================================================================
GX, CX_, LY = 300, 900, 410                 # Zeitstrahl: Trinken, Fahrt, Linie
folie([("alic", f"{PA} › actio libera in causa"), ("ausn", f"{PA} › a.l.i.c.: Ausnahmemodell"),
       ("tatb", f"{PA} › a.l.i.c.: Tatbestandsmodell")], rechts_frei([
    *tafel("alic", "actio libera in causa (a.l.i.c.)"),
    z("„die in ihrer Ursache freie Handlung“", 110, 170, beim("alic", "Ursache"), "Bold", 34),
    z("schuldhaft berauscht, schon mit Blick auf die spätere Tat", 110, 222, "idee", size=32),
    tafelicon("tabler", "glass-full", GX, LY - 14, 70, beim("idee", "berauscht"), fuell=WEISS),
    tafelicon("tabler", "car", CX_, LY - 14, 150, beim("idee", "spätere"), fuell=TUER),
    linienzug([(150, LY), (1100, LY)], beim("idee", "berauscht"), breite=6),
    z("Trinken: schuldfähig", GX - 150, LY + 14, beim("idee", "berauscht"), "Bold", 28),
    z("Fahrt: schuldunfähig", CX_ - 150, LY + 14, beim("idee", "spätere"), "Bold", 28),
    pfeil(CX_ - 20, LY + 90, GX + 20, LY + 90, "ausn", breite=9, kopf=28, farbe=DROT),
    z("Ausnahmemodell: Ausnahme vom Koinzidenzprinzip,", 110, LY + 118, "ausn", "Bold", 32),
    z("die Schuld beim Trinken genügt", 110, LY + 164, beim("ausn", "Schuld"), size=32),
    El(Image.new("RGBA", (CX_ - GX, 16), DGRUEN), GX, LY + 232, "tatb", "fade", 0.0, None, name="balken:tathandlung"),
    z("Tatbestandsmodell: Tathandlung nach vorn verlegt,", 110, LY + 262, "tatb", "Bold", 32),
    z("schon das Sich-Betrinken ist Beginn der Tat", 110, LY + 308, beim("tatb", "Schon"), size=32),
    zit("Lehrbegriffe; vgl. BGHSt 42, 235, Rn. 16, 18, 22", 110, LY + 358, beim("tatb", "Schon")),
    *requisit([("alic", ("tabler", "help-circle", 100, WEISS), "a.l.i.c.", GELB),
               ("ausn", ("tabler", "arrow-back-up", 100, WEISS), "Ausnahmemodell", HELLROT),
               ("tatb", ("tabler", "arrow-bar-to-left", 100, WEISS), "Tatbestandsmodell", HELLGRUEN)]),
    *stehend("LE", FX, [("alic", "denkt"), ("ausn", "ruhig"), ("tatb", "still")]),
]))

# ===========================================================================================================================
# E Der echte Fall (BGHSt 42, 235): sachlich, ohne Figuren, ohne Unfallbild
# ===========================================================================================================================
PE = "Der echte Fall · BGHSt 42, 235"
folie([("echt", PE), ("lief", f"{PE} · Sachverhalt"), ("lg", f"{PE} · LG Osnabrück")], rechts_frei([
    *tafel("echt", "Der echte Fall: BGHSt 42, 235"),
    zit("BGH, Urt. v. 22.8.1996 – 4 StR 217/96 (Vorinstanz: LG Osnabrück)", 110, 165, beim("echt", "Bundesgerichtshof")),
    z("Lieferwagenfahrer ohne Fahrerlaubnis", 110, 225, "lief", "Bold", 34),
    z("betrinkt sich in den Niederlanden,", 110, 280, beim("lief", "betrank"), size=34),
    z("obwohl er noch kein Hotel für die Nacht hat", 110, 330, "trank", size=34),
    z("kurz hinter der deutschen Grenze: Unglück an einer Kontrollstelle", 110, 395, "grenze", size=32),
    z("2 Beamte des Grenzschutzes kommen ums Leben", 110, 443, beim("grenze", "zwei"), size=32),
    z("bei der Fahrt schuldunfähig (§ 20 StGB)", 110, 510, "sfu", "Bold", 32),
    blk(110, 590, 1040, 120, LILA, "lg", [("LG Osnabrück: auch § 315c StGB vorsätzlich –", "ExtraBold", 32, INK),
                                         ("über die actio libera in causa", "ExtraBold", 32, INK)]),
    zit("Sachverhalt und Instanz: BGHSt 42, 235, Rn. 1, 6, 13–15", 110, 730, "lg"),
    *requisit([("echt", ("tabler", "gavel", 110, HOLZ), "BGH, 22.8.1996", GELB),
               ("lief", ("tabler", "truck-delivery", 160, WEISS), "Lieferwagen", WEISS),
               (beim("lief", "betrank"), ("tabler", "glass-full", 80, WEISS), "in den Niederlanden", WEISS),
               ("trank", ("tabler", "bed", 120, WEISS), "kein Hotel", WEISS),
               ("grenze", ("tabler", "flag", 100, WEISS), "Grenze", WEISS),
               ("sfu", ("tabler", "steering-wheel", 100, WEISS), "schuldunfähig", HELLROT),
               ("lg", ("tabler", "building-bank", 110, WEISS), "LG Osnabrück", LILA)]),
]))

# ===========================================================================================================================
# F1 BGH: Tatbestandsmodell scheitert am „Führen“ (Zitatkarte Rn. 17)
# ===========================================================================================================================
Q17 = ["„Jedenfalls bei den Delikten der Straßenverkehrsgefährdung",
       "und des Fahrens ohne Fahrerlaubnis ist die Vorverlagerung",
       "der Schuld unzulässig.“"]
q17, q17_y = wortlaut(80, 160, 1100, Q17, "BGHSt 42, 235, Rn. 17", "kern", marken=[
    (1, "Vorverlagerung", beim("kern", "Vorverlagerung")), (2, "der Schuld unzulässig", beim("kern", "Vorverlagerung"))],
    size=31)
folie([("kern", f"{PB} › keine a.l.i.c. bei Verkehrsdelikten"), ("fuehr", f"{PB} › 1. Tatbestandsmodell: „Führen“"),
       ("trink", f"{PB} › 1. Sich-Betrinken ist kein Führen")], rechts_frei([
    *tafel("kern", "BGH: keine a.l.i.c. bei §§ 315c, 316"),
    *q17,
    z("1. Tatbestandsmodell", 110, q17_y + 30, "fuehr", "ExtraBold", 34),
    z("§§ 315c, 316: Der Täter muss ein Fahrzeug „führen“.", 110, q17_y + 82, beim("fuehr", "verlangen"), size=32),
    z("Führen beginnt erst mit dem Anfahren;", 110, q17_y + 140, "anf", "Bold", 32),
    z("nicht einmal Motor anlassen genügt", 110, q17_y + 186, beim("anf", "Anlassen"), size=32),
    zit("BGHSt 42, 235, Rn. 19 (mit BGHSt 35, 390, 394)", 110, q17_y + 232, beim("anf", "Anlassen")),
    *neinz("Sich-Betrinken: noch kein Führen", q17_y + 290, "trink", "Bold", 34, x=160),
    *requisit([("kern", ("tabler", "gavel", 110, HOLZ), "Vorverlagerung unzulässig", HELLROT),
               ("fuehr", ("tabler", "steering-wheel", 100, WEISS), "„führen“", WEISS),
               ("anf", ("tabler", "car", 150, TUER), "erst beim Anfahren", WEISS),
               ("trink", ("tabler", "glass-full", 80, WEISS), "kein Führen", HELLROT)]),
    *stehend("LE", FX, [("kern", "ruhig"), ("trink", "denkt")]),
]))

# ===========================================================================================================================
# F2 Verhalten statt trennbarer Erfolg; eigenhändige Delikte; auch fahrlässig
# ===========================================================================================================================
folie([("verh", f"{PB} › 1. Verhalten statt Erfolg"), ("eigen", f"{PB} › 1. eigenhändige Delikte"),
       ("fahrl", f"{PB} › 1. auch bei Fahrlässigkeit")], rechts_frei([
    *tafel("verh", "1. Verhalten statt Erfolg"),
    z("§§ 315c, 316 verbieten ein Verhalten:", 110, 180, "verh", "Bold", 34),
    z("das Führen eines Fahrzeugs –", 110, 232, beim("verh", "Verhalten"), size=34),
    z("kein davon trennbarer Erfolg", 110, 282, beim("verh", "trennbaren"), size=34),
    zit("BGHSt 42, 235, Rn. 18", 110, 332, beim("verh", "trennbaren")),
    blk(110, 395, 1040, 120, GELB, "eigen", [("Lehre: verhaltensgebundene", "ExtraBold", 34, INK),
                                            ("oder eigenhändige Delikte", "ExtraBold", 34, INK)]),
    zit("vgl. BGHSt 42, 235, Rn. 20 (mit Nachweisen aus der Literatur)", 110, 530, beim("eigen", "eigenhändige")),
    *okz("gilt auch für fahrlässige Verstöße", 600, "fahrl", "Bold", 34, x=160),
    zit("BGHSt 42, 235, Rn. 18 a. E.", 160, 650, beim("fahrl", "fahrlässige")),
    *requisit([("verh", ("tabler", "steering-wheel", 100, WEISS), "Verhalten", WEISS),
               ("eigen", ("tabler", "user", 100, WEISS), "eigenhändig", GELB),
               ("fahrl", ("tabler", "alert-triangle", 100, GELB), "auch fahrlässig", WEISS)]),
    *stehend("LE", FX, [("verh", "ruhig"), ("eigen", "still")]),
]))

# ===========================================================================================================================
# G Ausnahmemodell scheitert: § 20 StGB, Art. 103 Abs. 2 GG (Wortlautkarte)
# ===========================================================================================================================
W103 = ["„(2) Eine Tat kann nur bestraft werden, wenn die",
        "Strafbarkeit gesetzlich bestimmt war, bevor die Tat",
        "begangen wurde.“"]
w103, w103_y = wortlaut(80, 380, 1100, W103, "Art. 103 Abs. 2 GG", "a103", marken=[
    (1, "gesetzlich bestimmt", beim("a103", "gesetzlich")), (1, "bevor die Tat", beim("a103", "bevor")),
    (2, "begangen wurde.", beim("a103", "bevor"))], size=32)
folie([("ausn2", f"{PB} › 2. Ausnahmemodell: § 20 StGB"), ("a103", f"{PB} › 2. Art. 103 Abs. 2 GG")], rechts_frei([
    *tafel("ausn2", "2. Ausnahmemodell scheitert"),
    z("§ 20 StGB: Schuldfähigkeit „bei Begehung der Tat“", 110, 175, "ausn2", "Bold", 32),
    z("eindeutiger Wortlaut: keine Ausnahme", 110, 225, beim("ausn2", "eindeutigen"), size=32),
    *neinz("auch nicht als Gewohnheitsrecht", 290, "gew", "Bold", 32, x=160),
    *w103,
    blk(110, w103_y + 28, 1040, 66, GELB, "verbot", [("verbietet strafbarkeitsbegründendes Gewohnheitsrecht", "ExtraBold", 32, INK)]),
    z("auch im Allgemeinen Teil des StGB", 110, w103_y + 114, "at", "Bold", 32),
    zit("BGHSt 42, 235, Rn. 22 (mit BVerfGE 25, 269, 285)", 110, w103_y + 162, "at"),
    *requisit([("ausn2", ("tabler", "book", 100, WEISS), "§ 20 StGB", GELB),
               ("gew", ("tabler", "ban", 100, ROT), "kein Gewohnheitsrecht", WEISS),
               ("a103", ("tabler", "scale", 110, WEISS), "Art. 103 Abs. 2 GG", GELB)]),
    *stehend("LE", FX, [("ausn2", "ruhig"), ("a103", "still")]),
]))

# ===========================================================================================================================
# H Offen gelassen; fahrlässige Tötung ohne a.l.i.c. (echter Fall, ohne Figuren)
# ===========================================================================================================================
folie([("offen", f"{PB} › offen gelassen"), ("k222", f"{PB} › § 222 StGB ohne a.l.i.c."),
       ("erg222", f"{PB} › Schuldspruch")], rechts_frei([
    *tafel("offen", "Offen gelassen – und § 222 StGB"),
    z("a.l.i.c. bei anderen Delikten? offen gelassen", 110, 180, "offen", "Bold", 34),
    zit("BGHSt 42, 235, Rn. 16, 18", 110, 228, beim("offen", "offen")),
    z("§ 222 StGB (fahrlässige Tötung): keine a.l.i.c. nötig", 110, 300, "k222", "Bold", 32),
    *okz("Vorwurf knüpft an das Trinken an", 360, beim("k222", "Trinken"), size=32, x=160),
    *okz("er musste damit rechnen, danach noch zu fahren", 420, beim("k222", "rechnen"), size=32, x=160),
    zit("BGHSt 42, 235, Rn. 8 f.", 160, 470, beim("k222", "rechnen")),
    blk(110, 540, 1040, 80, LILA, "erg222", [("BGH: fahrlässige Tötung in 2 Fällen", "ExtraBold", 34, INK)]),
    zit("Tenor 1 a", 110, 640, "erg222"),
    *requisit([("offen", ("tabler", "help-circle", 100, WEISS), "offen", WEISS),
               ("k222", ("tabler", "glass-full", 80, WEISS), "Anknüpfung: Trinken", WEISS),
               ("erg222", ("tabler", "gavel", 110, HOLZ), "Schuldspruch", LILA)]),
]))

# ===========================================================================================================================
# I Was bleibt: Vollrausch, § 323a StGB (Wortlautkarte)
# ===========================================================================================================================
PV = "B. § 323a StGB"
W323 = ["„(1) Wer sich vorsätzlich oder fahrlässig durch alkoholische",
        "Getränke oder andere berauschende Mittel in einen Rausch",
        "versetzt, wird mit Freiheitsstrafe bis zu fünf Jahren oder mit",
        "Geldstrafe bestraft, wenn er in diesem Zustand eine rechtswidrige",
        "Tat begeht und ihretwegen nicht bestraft werden kann, weil er",
        "infolge des Rausches schuldunfähig war oder weil dies nicht",
        "auszuschließen ist. (2) Die Strafe darf nicht schwerer sein als",
        "die Strafe, die für die im Rausch begangene Tat angedroht ist. …“"]
w323, w323_y = wortlaut(80, 160, 1100, W323, "§ 323a StGB (Abs. 3 ausgelassen)", "p323", marken=[
    (0, "vorsätzlich oder fahrlässig", beim("w1", "vorsätzlich")), (1, "in einen Rausch", beim("w1", "Rausch")),
    (2, "versetzt,", beim("w1", "Rausch")),
    (3, "eine rechtswidrige", "w2"), (4, "Tat begeht", "w2"),
    (4, "nicht bestraft werden kann,", "w3"), (5, "schuldunfähig war oder weil dies nicht", beim("w3", "schuldunfähig")),
    (6, "auszuschließen ist.", beim("w3", "schuldunfähig")),
    (2, "bis zu fünf Jahren", "rahmen"), (6, "(2) Die Strafe darf nicht schwerer sein als", "abs2"),
    (7, "die Strafe, die für die im Rausch begangene Tat angedroht ist.", "abs2")], size=30)
folie([("p323", f"{PV} › Vollrausch"), ("bed", f"{PV} › Bedingung der Strafbarkeit"), ("rahmen", f"{PV} › Strafrahmen"),
       ("bgh2", f"{PV} › im echten Fall")], rechts_frei([
    *tafel("p323", "Was bleibt: Vollrausch, § 323a StGB"),
    *w323,
    blk(110, w323_y + 22, 1040, 66, GELB, "bed", [("Rauschtat: Bedingung der Strafbarkeit", "ExtraBold", 32, INK)]),
    zit("kein Tatbestandsmerkmal: BGHSt 42, 235, Rn. 25", 110, w323_y + 100, beim("bed", "Tatbestandsmerkmal")),
    blk(110, w323_y + 150, 1040, 66, LILA, "bgh2", [("echter Fall: vorsätzlicher Vollrausch, Rauschtat § 315c", "ExtraBold", 31, INK)]),
    zit("BGHSt 42, 235, Rn. 23", 110, w323_y + 228, "bgh2"),
    *requisit([("p323", ("tabler", "book", 100, WEISS), "§ 323a StGB", GELB),
               ("bed", ("tabler", "glass-full", 80, WEISS), "Rauschtat", WEISS),
               ("rahmen", ("tabler", "gavel", 110, HOLZ), "bis 5 Jahre", WEISS),
               ("abs2", ("tabler", "scale", 110, WEISS), "nicht mehr als Rauschtat", WEISS),
               ("bgh2", ("tabler", "gavel", 110, HOLZ), "BGH 1996", LILA)]),
    *stehend("LE", FX, [("p323", "ruhig"), ("bed", "denkt")]),
]))

# ===========================================================================================================================
# J Lösung des Falls
# ===========================================================================================================================
PL_ = "Lösung · Leopold"
folie([("loes", PL_), ("l316", f"{PL_} · § 316 StGB (−)"), ("l323", f"{PL_} · § 323a StGB (+)"),
       ("lvar", f"{PL_} · Variante: § 315c StGB"), ("l69", f"{PL_} · § 69 StGB")], rechts_frei([
    *tafel("loes", "Lösung: Leopold"),
    *neinz("§ 316: schuldunfähig, a.l.i.c. hilft nicht (−)", 180, "l316", "Bold", 32, x=160),
    *okz("§ 323a: vorsätzlich berauscht, Rauschtat § 316 (+)", 250, "l323", "Bold", 32, x=160),
    z("Strafe höchstens 1 Jahr: § 323a Abs. 2 mit § 316 Abs. 1", 160, 315, "l1j", size=31),
    linienzug([(130, 385), (1130, 385)], "lvar", breite=3),
    z("Variante (scharfe Bremsung): Rauschtat § 315c,", 110, 410, "lvar", "Bold", 32),
    z("wenn ein Beinahe-Unfall feststeht", 110, 458, beim("lvar", "Beinahe"), size=32),
    zit("Beinahe-Unfall: BGH, Beschl. v. 19.6.2024 – 4 StR 73/24, Rn. 6", 110, 505, beim("lvar", "Beinahe")),
    blk(110, 570, 1040, 120, GELB, "l69", [("Fahrerlaubnis: in der Regel entzogen,", "ExtraBold", 33, INK),
                                          ("auch beim Vollrausch: § 69 Abs. 1, 2 Nr. 4", "ExtraBold", 33, INK)]),
    *requisit([("loes", None, "Zurück zu Leopold", TUER), ("l316", ("tabler", "car", 150, TUER), "§ 316 (−)", HELLROT),
               ("l323", ("tabler", "glass-full", 80, WEISS), "§ 323a (+)", GRUEN),
               ("lvar", ("tabler", "alert-triangle", 100, GELB), "Variante § 315c", LILA),
               ("l69", ("tabler", "id", 110, WEISS), "§ 69 StGB", GELB)]),
    *stehend("LE", X1, [("loes", "ruhig"), ("l316", "still"), ("l323", "sorge"), ("l69", "muede")]),
    *stehend("PO", X2, [("loes", "ruhig"), ("l69", "ernst")]),
]))

# ===========================================================================================================================
# K Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Prüfungsreihenfolge")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("1. zuerst das Verkehrsdelikt bis zur Schuld", 200, 205, beim("tipp", "Prüfe"), "Bold", 34),
    z("2. bei § 20 die a.l.i.c. ansprechen", 200, 290, "tipp2", "Bold", 34),
    z("und mit dem BGH ablehnen", 245, 340, beim("tipp2", "lehnst"), size=34),
    zit("BGHSt 42, 235, Rn. 17–22", 245, 390, beim("tipp2", "lehnst")),
    z("3. erst danach: Vollrausch, § 323a StGB", 200, 465, "tipp3", "Bold", 34),
    *redet("LX_warnt", FX, FB, FR_ + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# L Prüfschema
# ===========================================================================================================================
REIHEN = [("s1", 0, "A. Strafbarkeit nach § 316 StGB", True),
          (beim("s1", "Tatbestand"), 1, "I. Tatbestand  ·  II. Rechtswidrigkeit", False),
          ("s2", 1, "III. Schuld: § 20 – schuldunfähig bei Fahrtantritt", False),
          ("s3", 2, "a.l.i.c.? Bei Verkehrsdelikten abgelehnt", False),
          ("s4", 0, "B. Strafbarkeit nach § 323a StGB", True),
          (beim("s4", "Römisch"), 1, "I. vorsätzlich oder fahrlässig in einen Rausch versetzt", False),
          ("s5", 1, "II. Rauschtat als Bedingung der Strafbarkeit", False),
          ("s6", 1, "III. Rechtswidrigkeit und Schuld; Strafrahmen nach Abs. 2", False)]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfschema: Trunkenheitsfahrt im Rausch"), 110, 90, "sch", 46)]
y = 200
for c, ebene, text, fett in REIHEN:
    x = (130, 200, 270)[ebene]
    if c == "s3":
        els_sch.append(karte(250, y - 14, 1560, 70, c, fill=HELLGRUEN, rund=16, schatten=5, rand=4))
    if c == "s4":
        y += 20
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 40 if ebene == 0 else 36, rechts=1800))
    y += {0: 92, 1: 82, 2: 86}[ebene]
assert y <= 970, y
folie([("sch", "Prüfschema"), ("s1", "Prüfschema › A. § 316 StGB"), ("s3", "Prüfschema › A. III. a.l.i.c."),
       ("s4", "Prüfschema › B. § 323a StGB")], els_sch)

# ===========================================================================================================================
# M Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Wer sich betrinkt,", 0)], [("führt noch kein Fahrzeug", "a"), (".", 0)]], 750, 290, 46, "merke",
                {"a": beim("merke", "führt")}),
    *markertext([[("Bei §§ 315c, 316 hilft die", 0)], [("actio libera in causa", "b"), (" nicht;", 0)]], 750, 470, 46,
                "m2", {"b": beim("m2", "actio")}),
    *markertext([[("es bleibt der ", 0), ("Vollrausch", "c"), (".", 0)]], 750, 650, 46, "m3", {"c": beim("m3", "Vollrausch")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
