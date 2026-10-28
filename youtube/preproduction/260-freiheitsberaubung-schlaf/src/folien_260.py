"""Folge 260 · Freiheitsberaubung § 239 im Schlaf: Muss das Opfer es merken? – Serienstandard Open Peeps (Katzenkönig).
Fall (Plan-Hook): Nachts in einer Altbauwohnung schließt Vermieter Herr Gerber das Zimmer seines schlafenden Untermieters
Joscha von außen ab (kein anderer Ausgang), sicher, dass Joscha durchschläft; um 3 Uhr schließt er wieder auf, Joscha merkt
nichts. Szenen laut ../SZENENPLAN.md: A Wohnung bei Nacht (Fall), B Sachverhalt, C § 239 Abs. 1 (Wortlautkarte) und Rechtsgut,
D 1. Ansicht (potenzielle Fortbewegungsfreiheit), E 2. Ansicht (aktuelle), F Was sagt der BGH (Linie seit 1960, Urteil
5 StR 406/21, Sachverhalt), G1 Kernsatz (Zitatkarte Rn. 21), G2 Gründe, H Lösung 1. Ansicht, I Lösung 2. Ansicht mit
Versuch (Wortlautkarte § 239 Abs. 2), J Streitentscheid, K Klausurtipp (Lexi), L Schema, M Merksatz (Lexi).
Kein Gewaltbild: Joscha schläft ruhig im Bett (sitzende Open-Peeps-Pose unter einer programmatisch gezeichneten Decke),
Schlüssel/Schloss-Icons (Tabler). Ein Handlungsgeräusch (Schlüssel im Schloss, ../geraeusche_herkunft.json), zweimal.
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz
als eigene Kopie aus Folge 257 (gemeinsame Dateien unverändert); neu: boden(), bett(), zzz(), schlafbett(), arg().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern. Wortlautkarten wörtlich nach gesetze-im-internet.de (Abruf 08.10.2026);
Zitatkarte wörtlich nach dem Volltext (HRRS 2022 Nr. 801, Rn. 21)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from ostil import lichtkegel
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_260/"

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
        if n.startswith(("bild:", "ficon:", "bank")) or "/op_260/" in n:
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


# --- eigene Szenenbausteine: Wohnung bei Nacht, Bett mit Decke (Palettenflächen, Tuschekontur) ---------------------------
from scipy import ndimage as _nd

BODEN = (222, 196, 160, 255)
WAND_FLUR = (246, 238, 222, 255)
NACHTBLAU = (52, 62, 112, 255)
MORGENBLAU = (196, 220, 250, 255)
F_O = 930                                    # Bodenlinie
FU = 942                                     # Unterkante stehender Figuren in der Fallszene
FH = 520                                     # Höhe stehender Figuren in der Fallszene
X1, X2 = 1430, 1730                          # zwei Plätze neben der Tafel
FB, FR = 930, 480                            # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                    # eine Figur neben der Tafel (Lexi)
NULL = ("fall", -round(T_("fall"), 3))       # = 0,0 s: erstes Bild nach dem Intro vollständig
PX, PY, PU = 1575, 160, 380                  # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"GE": "Herr Gerber", "JO": "Joscha"}
NFARBE = {"GE": ORANGE, "JO": LILA}


def boden(cue, bis=None):
    im = Image.new("RGBA", (1860, 70))
    dr = ImageDraw.Draw(im)
    dr.rectangle((0, 0, 1860, 70), fill=BODEN)
    dr.line((0, 0, 1860, 0), fill=INK, width=6)
    for x in range(90, 1860, 180):
        dr.line((x, 8, x, 70), fill=(196, 168, 130, 255), width=3)
    return El(im, 30, F_O, cue, "cut", 0.0, bis, name="boden")


def _decke(w, h, huegel):
    """Bettdecke als eine Fläche mit Tuschekontur: abgerundetes Rechteck plus flacher Hügel über dem Knie."""
    m = Image.new("L", (w, h)); d = ImageDraw.Draw(m)
    d.rounded_rectangle((6, int(h * 0.30), w - 6, h - 6), 30, fill=255)
    cx, cy, rx, ry = huegel
    d.ellipse((cx - rx, cy - ry, cx + rx, cy + ry), fill=255)
    a = np.asarray(m) > 0
    innen = _nd.binary_erosion(a, iterations=5)
    out = np.zeros((h, w, 4), np.uint8)
    out[a] = BLAU; out[a & ~innen] = INK
    for k in (0.55, 0.75):                    # zwei Falten als dünne Linien
        y = int(h * k); out[y:y + 3, int(w * 0.12):int(w * 0.38)] = INK
    return Image.fromarray(out)


def bett(cx, unten, H, cue, folge, bis=None, redet_=None, rechts=None, nr=""):
    """Bett mit Joscha: Kopfteil und Kissen hinten, Joscha (sitzend, sitting/one_leg_up-2, blickt nach rechts), Decke
    und Bettrahmen vorn. folge = [(cue, suffix)] → Mimikfolge; redet_ = (cue_von, cue_bis) für Figurenrede.
    Gibt (Elemente, (name, fx, funten, H) für Blasen) zurück."""
    fw = int(H * 802 / 1185)                  # Seitenverhältnis der Pose
    fx, fu = cx, unten - 28                    # Figur sitzt auf der Matratze
    x0 = fx - fw // 2
    if rechts is not None:
        assert x0 - 34 >= rechts, f"Bett ragt in die Tafel ({x0 - 34} < {rechts})"
    hinten = Image.new("RGBA", (int(fw * 0.62) + 12, int(H * 0.86) + 12))
    dh = ImageDraw.Draw(hinten)
    dh.rounded_rectangle((3, 3, 74, hinten.height - 3), 14, fill=HOLZ, outline=INK, width=5)
    dh.rounded_rectangle((30, int(H * 0.22), int(fw * 0.50), int(H * 0.22) + int(H * 0.18)), 22, fill=WEISS, outline=INK, width=4)
    els = [El(hinten, x0 - 34, unten - hinten.height + 4, cue, "cut", 0.0, bis, name=f"bett{nr}:hinten")]
    for i, (c, s) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else bis
        if redet_ and s == "redet":
            els += redet("JO_redet_r", fx, fu, H, redet_[0], redet_[1])
            continue
        els.append(peep_voll(f"JO_{s}_r", fx, fu, H, c, anim="cut", bis=b))
    bw, bh = fw + 70, int(H * 0.50)
    els.append(El(_decke(bw, bh, (int(0.62 * fw), int(0.20 * H), int(0.20 * fw), int(0.13 * H))), x0 - 10,
                  unten - bh - 6, cue, "cut", 0.0, bis, name=f"bett{nr}:decke"))
    rahmen = Image.new("RGBA", (fw + 110, 46))
    ImageDraw.Draw(rahmen).rounded_rectangle((2, 2, fw + 107, 43), 10, fill=HOLZ, outline=INK, width=5)
    els.append(El(rahmen, x0 - 34, unten - 44, cue, "cut", 0.0, bis, name=f"bett{nr}:rahmen"))
    return els, ("JO_redet_r", fx, fu, H)


def zzz(cx, unten, H, cue, bis=None, gr=70):
    """Schlaf-Zeichen über Joschas Kopf."""
    return ficon("tabler", "zzz", cx + int(H * 0.30), unten - 28 - int(H * 0.86), gr, cue, fuell=WEISS, bis=bis)


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


def stehend(k, x, folge, unten=FB, hoehe=FR):
    return [*fig(k, x, unten, hoehe, folge), ns(NAME[k], x, unten, folge[0][0], NFARBE[k], d=0.1)]


def schlafbett(cue, folge, cx=1400, H=330, bis=None, mit_zzz=True):
    """Joscha im Bett neben der Tafel (rechts), mit Namensschild."""
    els, _ = bett(cx, FB, H, cue, folge, bis=bis, rechts=1250)
    if mit_zzz:
        els.append(zzz(cx, FB, H, cue, bis=next((c for c, s in folge if s != "schlaeft"), bis)))
    els.append(ns("Joscha", cx, FB, cue, LILA, d=0.1))
    return els


def arg(text, y, cue, size=32, x=160, **k):
    """Argumentzeile mit Aufzählungspunkt."""
    return [z("•", x - 40, y, cue, "ExtraBold", size), z(text, x, y, cue, size=size, **k)]


K_SCHLOSS = ("tabler", "lock", 96, ROT)
K_TUER = ("tabler", "door", 96, HOLZ)
K_ZZZ = ("tabler", "zzz", 96, WEISS)
K_BUCH = ("tabler", "book", 100, WEISS)

# ===========================================================================================================================
# A Fall: nachts in der Altbauwohnung
# ===========================================================================================================================
JX, JH = 330, 430                            # Joscha im Bett (links, im eigenen Zimmer)
GX = 1420                                    # Herr Gerber im Flur (blickt nach links zur Tür)
TX0, TX1, TY0 = 1060, 1220, 560              # Zimmertür (Flurseite)
SCHLOSS_ZU = ficon("tabler", "lock", 1186, 790, 58, beim("schliesst", "ab"), fuell=ROT, bis="drei")
SCHLOSS_AUF = ficon("tabler", "lock-open", 1186, 790, 58, beim("drei", "auf"), fuell=GRUEN)
szene(SCHLOSS_ZU, "260schloss*", 0.8, -0.45)
szene(SCHLOSS_AUF, "260schloss*", 0.7, -0.45)
bett_a, JO_FIG = bett(JX, F_O, JH, "joscha", [("joscha", "schlaeft"), ("morgen", "ruhig"), ("j1", "redet"), ("frage", "froh")],
                      redet_=("j1", "frage"))
folie([(NULL, "Fall · Nachts in der Altbauwohnung"), ("joscha", "Fall · Untermieter Joscha schläft"),
       ("gerber", "Fall · Vermieter Herr Gerber"), ("schliesst", "Fall · Gerber schließt ab"),
       ("ausgang", "Fall · kein anderer Ausgang"), ("g1", "Fall · „Merkt er ja eh nicht.“"),
       ("sicher", "Fall · Gerber ist sicher: Joscha schläft durch"), ("drei", "Fall · 3 Uhr: wieder aufgeschlossen"),
       ("morgen", "Fall · 7 Uhr: Joscha wacht auf"), ("j1", "Fall · „Super geschlafen!“"), ("frage", "Fall · Die Frage")], [
    hart(boden(NULL)),
    hart(karte(60, 250, 960, 684, NULL, fill=LILAHELL, rund=6, schatten=0, rand=5, anim="cut")),
    hart(karte(1020, 250, 840, 684, NULL, fill=WAND_FLUR, rund=6, schatten=0, rand=5, anim="cut")),
    hart(karte(TX0, TY0, TX1 - TX0, F_O - TY0 + 4, NULL, fill=HOLZ, rund=6, schatten=0, rand=5, anim="cut")),
    hart(karte(TX0 + 18, TY0 + 24, TX1 - TX0 - 36, 140, NULL, fill=(226, 178, 130, 255), rund=6, schatten=0, rand=4, anim="cut")),
    hart(karte(TX1 - 44, 720, 22, 22, NULL, fill=GELB, rund=11, schatten=0, rand=3, anim="cut")),
    hart(karte(700, 330, 250, 200, NULL, fill=NACHTBLAU, rund=8, schatten=0, rand=5, anim="cut", )),
    bis_(hart(ficon("tabler", "moon-stars", 825, 505, 130, NULL, fuell=GELB, anim="cut")), "morgen"),
    karte(700, 330, 250, 200, "morgen", fill=MORGENBLAU, rund=8, schatten=0, rand=5, anim="cut"),
    ficon("tabler", "sun", 825, 500, 120, "morgen", fuell=GELB, anim="cut"),
    bis_(hart(ficon("tabler", "clock-hour-1", 1140, 432, 96, NULL, fuell=WEISS, anim="cut")), "drei"),
    ficon("tabler", "clock-hour-3", 1140, 432, 96, "drei", fuell=WEISS, anim="cut", bis="morgen"),
    ficon("tabler", "clock-hour-7", 1140, 432, 96, "morgen", fuell=WEISS, anim="cut"),
    bis_(hart(pl("1 Uhr", 1140, 272, NULL, fill=WEISS, size=30, anker="m")), "drei"),
    pl("3 Uhr", 1140, 272, "drei", fill=WEISS, size=30, anker="m", bis="morgen"),
    pl("7 Uhr", 1140, 272, "morgen", fill=WEISS, size=30, anker="m"),
    hart(pl("Altbauwohnung, kurz vor 1 Uhr nachts", 70, 30, NULL, fill=GELB, size=38, bis="frage")),
    pl("Untermieter Joscha schläft fest", 70, 100, "joscha", fill=WEISS, size=32, bis="frage"),
    pl("Vermieter Herr Gerber wohnt in derselben Wohnung", 70, 166, "gerber", fill=WEISS, size=32, bis="frage"),
    *bett_a,
    zzz(JX, F_O, JH, "joscha", bis="morgen", gr=80),
    ns("Joscha", JX, F_O, "joscha", LILA, d=0.1),
    *fig("GE", GX, FU, FH, [("gerber", "denkt"), ("schliesst", "ernst")], bis="g1", erst="pop"),
    *redet("GE_redet", GX, FU, FH, "g1", "sicher"),
    *fig("GE", GX, FU, FH, [("sicher", "froh"), ("drei", "ruhig")], bis="morgen", erst="cut"),
    bis_(ns("Herr Gerber", GX, FU, "gerber", ORANGE, d=0.1), "morgen"),
    ficon("tabler", "key", 1268, 700, 60, "schliesst", fuell=GELB, bis=beim("schliesst", "ein", ende=True)),
    SCHLOSS_ZU,
    pl("von außen abgeschlossen", 1140, 482, beim("schliesst", "ab"), fill=HELLROT, size=28, anker="m", bis="sicher"),
    pl("kein anderer Ausgang", 380, 280, "ausgang", fill=HELLROT, size=30, anker="m", bis="morgen"),
    blase("sprech", 640, 210, "g1", 1560, 300, inhalt=["Bis 3 bleibt die Tür zu.", "Merkt er ja eh nicht."], textsize=34,
          figur=("GE_redet", GX, FU, FH), bis="sicher"),
    pl("Gerber ist sicher: Joscha schläft durch", 1530, 370, "sicher", fill=GELB, size=30, anker="m", bis="drei"),
    SCHLOSS_AUF,
    pl("wieder aufgeschlossen", 1140, 482, beim("drei", "auf"), fill=HELLGRUEN, size=28, anker="m", bis="morgen"),
    pl("Joscha wacht auf", 380, 280, "morgen", fill=WEISS, size=30, anker="m", bis="frage"),
    blase("sprech", 640, 160, "j1", 395, 330, inhalt=["Ah, ich hab super geschlafen!"], textsize=34, figur=JO_FIG, bis="frage"),
    pl("Joscha hat nichts gemerkt. Freiheitsberaubung?", 70, 30, "frage", fill=PINK, size=36),
    pl("Muss das Opfer es bemerken?", 70, 100, "frage2", fill=PINK, size=34),
])

# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_260(cue, absaetze, frage):
    els = [karte(140, 90, 1640, 800, cue, fill=HELL), titel("Sachverhalt", 210, 130, cue, 60)]
    y = 235
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=38, zeilenabstand=1.30)
        els += e; y += 20
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_260("sv", [
    "Kurz vor 1 Uhr nachts in einer Altbauwohnung: Untermieter Joscha schläft fest in seinem Zimmer. Sein Vermieter, "
    "Herr Gerber, wohnt in derselben Wohnung und ärgert sich über ihn. Er schließt das Zimmer von außen ab und steckt den "
    "Schlüssel ein; einen anderen Ausgang hat das Zimmer nicht. Gerber: „Bis 3 bleibt die Tür zu. Merkt er ja eh nicht.“",
    "Gerber ist sicher, dass Joscha bis zum Morgen durchschläft. Um 3 Uhr schließt er wieder auf. Joscha wacht um 7 Uhr "
    "auf und hat nichts bemerkt.",
], "Hat Gerber sich wegen Freiheitsberaubung (§ 239 StGB) strafbar gemacht?")

# ===========================================================================================================================
# C § 239 Abs. 1 StGB (Wortlautkarte), Rechtsgut
# ===========================================================================================================================
W1 = ["„(1) Wer einen Menschen einsperrt oder auf andere Weise der",
      "Freiheit beraubt, wird mit Freiheitsstrafe bis zu fünf Jahren",
      "oder mit Geldstrafe bestraft.“"]
w1, w1_y = wortlaut(80, 170, 1100, W1, "§ 239 Abs. 1 StGB", "norm", marken=[
    (0, "einsperrt", beim("wl", "einsperrt")), (1, "Freiheit beraubt", beim("wl", "Freiheit"))], size=32)
PN = "§ 239 Abs. 1 StGB"
folie([("norm", f"{PN} › Wortlaut"), ("rg", f"{PN} › Rechtsgut: Fortbewegungsfreiheit"),
       ("einsp", f"{PN} › am Fall: die einzige Tür abgeschlossen"), ("kern", "Streitstand · Was heißt Fortbewegungsfreiheit?")],
      rechts_frei([
    karte(60, 60, 1140, 840, "norm"), titel(glyphen("Freiheitsberaubung, § 239 StGB"), 110, 90, "norm", 46),
    *w1,
    z("Rechtsgut: die Fortbewegungsfreiheit", 110, w1_y + 30, "rg", "Bold", 34),
    z("den eigenen Aufenthalt nach Belieben verändern", 110, w1_y + 80, beim("rg", "Aufenthalt"), size=32),
    zit("BGH, Urt. v. 8.6.2022 – 5 StR 406/21, Rn. 21", 110, w1_y + 126, beim("rg", "Belieben")),
    *okz("Gerber schließt die einzige Tür ab", w1_y + 190, "einsp", size=32, x=160),
    *okz("Joscha könnte nicht hinaus, selbst wenn er wollte", w1_y + 240, beim("einsp", "Joscha"), size=32, x=160),
    blk(110, w1_y + 320, 1040, 120, GELB, "kern", [("Aber er will gar nicht: Er schläft.", "ExtraBold", 34, INK),
                                                  ("Hier beginnt der Streit.", "ExtraBold", 34, INK)]),
    *requisit([("norm", K_BUCH, "§ 239 Abs. 1 StGB", GELB),
               ("rg", ("tabler", "walk", 100, WEISS), "Fortbewegungsfreiheit", WEISS),
               ("einsp", K_SCHLOSS, "Tür abgeschlossen", HELLROT),
               ("kern", K_ZZZ, "Er schläft.", WEISS)]),
    *schlafbett("norm", [("norm", "schlaeft")]),
]))

# ===========================================================================================================================
# D 1. Ansicht: potenzielle Fortbewegungsfreiheit
# ===========================================================================================================================
P1 = "Streitstand › 1. Ansicht: potenzielle Fortbewegungsfreiheit"
folie([("pot", P1), ("pot2", f"{P1} › könnte das Opfer weg?"), ("pot3", f"{P1} › Bemerken ohne Belang"),
       ("potarg", f"{P1} › Argument: Wortlaut")], rechts_frei([
    *tafel("pot", "1. Ansicht: potenzielle Freiheit", h=840),
    blk(110, 175, 1040, 80, GRUEN, "pot", [("Geschützt: die potenzielle Fortbewegungsfreiheit", "ExtraBold", 33, INK)]),
    z("Entscheidend: Könnte das Opfer sich fortbewegen,", 110, 290, "pot2", "Bold", 32),
    z("wenn es wollte?", 110, 336, beim("pot2", "wenn"), "Bold", 32),
    *okz("Ob es die Beschränkung bemerkt: ohne Belang", 410, "pot3", size=32, x=160),
    *okz("auch Schlafende geschützt", 460, beim("pot3", "Geschützt"), "Bold", 32, x=160),
    zit("BGH, Urt. v. 8.6.2022 – 5 StR 406/21, Rn. 21 (mit BGHSt 14, 314, 316)", 160, 508, beim("pot3", "Schlafende")),
    z("Argument:", 110, 580, "potarg", "ExtraBold", 32),
    *arg("Wortlaut: der Freiheit beraubt ist, wer nicht weg kann", 630, beim("potarg", "Wortlaut"), size=31),
    *arg("anders als § 240: kein aufgezwungenes Verhalten nötig", 680, beim("potarg", "Anders"), size=31),
    zit("BGH, a. a. O., Rn. 24", 160, 728, beim("potarg", "aufgezwungen")),
    *requisit([("pot", ("tabler", "walk", 100, WEISS), "potenzielle Freiheit", GRUEN),
               ("pot2", K_TUER, "Könnte er weg?", GRUEN),
               ("pot3", K_ZZZ, "merkt nichts", WEISS),
               ("potarg", K_BUCH, "Wortlaut", WEISS)]),
    *schlafbett("pot", [("pot", "schlaeft")]),
]))

# ===========================================================================================================================
# E 2. Ansicht: aktuelle Fortbewegungsfreiheit
# ===========================================================================================================================
P2 = "Streitstand › 2. Ansicht: aktuelle Fortbewegungsfreiheit"
folie([("akt", P2), ("akt2", f"{P2} › will das Opfer gerade weg?"), ("aktarg", f"{P2} › Argument: Versuch strafbar"),
       ("aktarg2", f"{P2} › Argument: Spezialfall der Nötigung")], rechts_frei([
    *tafel("akt", "2. Ansicht: aktuelle Freiheit", h=840),
    blk(110, 175, 1040, 80, ORANGE, "akt", [("Geschützt: nur die aktuelle Fortbewegungsfreiheit", "ExtraBold", 33, INK)]),
    zit("im Schrifttum weit verbreitet; Nachweise bei BGH, Urt. v. 8.6.2022 – 5 StR 406/21, Rn. 22", 110, 268, beim("akt", "Geschützt")),
    z("Der Freiheit beraubt ist nur, wer sich zu einem", 110, 330, "akt2", "Bold", 32),
    z("bestimmten Zeitpunkt wegbewegen will, aber nicht kann", 110, 376, beim("akt2", "bestimmten"), "Bold", 32),
    z("Argumente:", 110, 460, "aktarg", "ExtraBold", 32),
    *arg("seit der Reform von 1998 ist der Versuch strafbar (§ 239 Abs. 2)", 510, beim("aktarg", "Seit"), size=31),
    zit("6. Strafrechtsreformgesetz v. 26.1.1998, BGBl. I S. 164", 160, 556, beim("aktarg", "Versuch")),
    *arg("sonst wäre die Vollendung zu weit vorverlegt", 610, beim("aktarg", "Wer"), size=31),
    *arg("§ 239 sei letztlich ein Spezialfall der Nötigung", 660, "aktarg2", size=31),
    *requisit([("akt", ("tabler", "walk", 100, WEISS), "aktuelle Freiheit", ORANGE),
               ("akt2", K_TUER, "Will er gerade weg?", ORANGE),
               ("aktarg", K_BUCH, "§ 239 Abs. 2: Versuch", WEISS),
               ("aktarg2", K_BUCH, "§ 240 Nötigung", WEISS)]),
    *schlafbett("akt", [("akt", "schlaeft")]),
]))

# ===========================================================================================================================
# F Was sagt der BGH? Linie seit 1960, Urteil 2022, Sachverhalt der Entscheidung
# ===========================================================================================================================
PB = "Was sagt der BGH?"
folie([("bgh", f"{PB} › seit Langem: 1. Ansicht"), ("bgh2", f"{PB} › Urteil vom 8.6.2022 – 5 StR 406/21"),
       ("bghfall", f"{PB} › der Fall: kein Schlafender"),
       (beim("bghfall", "getäuscht"), f"{PB} › der Fall: getäuscht")], rechts_frei([
    *tafel("bgh", "Was sagt der BGH?", h=840),
    *okz("folgt seit Langem der 1. Ansicht", 180, "bgh", "Bold", 34, x=160),
    z("schon in einem Urteil von 1960", 160, 232, beim("bgh", "neunzehnhundertsechzig"), size=32),
    zit("BGH, Urt. v. 31.5.1960 – 1 StR 212/60, BGHSt 14, 314, 316 (zitiert in Rn. 21)", 160, 278, beim("bgh", "neunzehnhundertsechzig")),
    *okz("Urteil vom 8.6.2022: daran festgehalten", 345, "bgh2", "Bold", 34, x=160),
    zit("BGH, Urt. v. 8.6.2022 – 5 StR 406/21, Rn. 23; HRRS 2022 Nr. 801", 160, 395, beim("bgh2", "festgehalten")),
    blk(110, 470, 1040, 80, BLAUHELL, "bghfall", [("Der Fall: kein Schlafender", "ExtraBold", 34, INK)]),
    z("Angehörige brachten eine junge Frau unter einem", 110, 580, beim("bghfall", "Angehörige"), size=32),
    z("Vorwand im Auto und im Flugzeug ins Ausland", 110, 626, beim("bghfall", "Vorwand"), size=32),
    *okz("Sie fuhr mit, weil sie getäuscht war.", 700, beim("bghfall", "Sie"), "Bold", 32, x=160),
    zit("BGH, a. a. O., Rn. 8 f., 13", 160, 748, beim("bghfall", "getäuscht")),
    *requisit([("bgh", ("tabler", "building-bank", 110, WEISS), "BGH", BLAU),
               (beim("bghfall", "Auto"), ("tabler", "car", 150, BLAU), "im Auto", WEISS),
               (beim("bghfall", "Flugzeug"), ("tabler", "plane", 130, WEISS), "ins Ausland", WEISS),
               (beim("bghfall", "getäuscht"), ("tabler", "masks-theater", 110, GELB), "getäuscht", GELB)]),
    *stehend("GE", X2, [("bgh", "denkt"), ("bghfall", "ruhig")]),
]))

# ===========================================================================================================================
# G1 Der Kernsatz (Zitatkarte Rn. 21) und das Ergebnis
# ===========================================================================================================================
WB = ["„§ 239 StGB schützt die potentielle persönliche Bewegungsfreiheit.",
      "[…] Ob er seine Freiheitsbeschränkung überhaupt realisiert,",
      "ist danach ohne Belang.“"]
wb, wb_y = wortlaut(80, 190, 1100, WB, "BGH, Urt. v. 8.6.2022 – 5 StR 406/21, Rn. 21", "bghrn", marken=[
    (0, "potentielle persönliche Bewegungsfreiheit", beim("bghrn", "potenzielle")), (2, "ohne Belang", beim("bghrn", "ohne"))],
    size=30)
folie([("bghrn", f"{PB} › potenzielle Bewegungsfreiheit (Rn. 21)"),
       ("bgherg", f"{PB} › erschlichenes Einverständnis: Verurteilung bleibt")], rechts_frei([
    *tafel("bghrn", "Der BGH: Bemerken ist ohne Belang", h=580, size=44),
    *wb,
    *okz("erschlichenes Einverständnis: kein Ausschluss", wb_y + 50, "bgherg", "Bold", 32, x=160),
    z("Verurteilung wegen Freiheitsberaubung bleibt bestehen", 160, wb_y + 100, beim("bgherg", "Verurteilung"), size=32),
    zit("BGH, a. a. O., Rn. 19, 29 f.; Revisionen verworfen", 160, wb_y + 146, beim("bgherg", "bestehen")),
    *requisit([("bghrn", ("tabler", "building-bank", 110, WEISS), "BGH, Rn. 21", BLAU),
               ("bgherg", ("tabler", "masks-theater", 110, GELB), "Einverständnis erschlichen", WEISS)]),
    *stehend("GE", X2, [("bghrn", "ernst"), ("bgherg", "sorge")]),
]))

# ===========================================================================================================================
# G2 Die Gründe des BGH
# ===========================================================================================================================
folie([("bghgr", f"{PB} › Gründe: Wortlaut, hohes Gut"), ("bghsys", f"{PB} › Gründe: Systematik"),
       ("bghvers", f"{PB} › Gründe: Anwendungsbereich des Versuchs")], rechts_frei([
    *tafel("bghgr", "Die Gründe des BGH", h=840),
    *okz("1. der Wortlaut", 180, beim("bghgr", "Wortlaut"), "Bold", 34, x=160),
    *okz("2. das hohe Gut der Bewegungsfreiheit", 240, beim("bghgr", "hohe"), "Bold", 34, x=160),
    zit("BGH, a. a. O., Rn. 24 f.", 160, 290, beim("bghgr", "Bewegungsfreiheit")),
    *okz("3. Systematik: schwerer bestraft als die Nötigung", 350, "bghsys", "Bold", 34, x=160),
    z("und steht im Strafgesetzbuch vor ihr", 160, 400, beim("bghsys", "steht"), size=32),
    zit("§ 239 Abs. 1: bis 5 Jahre · § 240 Abs. 1: bis 3 Jahre (BGH, a. a. O., Rn. 25)", 160, 446, beim("bghsys", "steht")),
    z("also: kein bloßer Spezialfall der Nötigung", 160, 500, beim("bghsys", "Spezialfall"), "Bold", 32),
    *okz("4. für den Versuch bleibt ein Anwendungsbereich", 580, "bghvers", "Bold", 34, x=160),
    z("etwa: Der Täter will einschließen,", 160, 630, beim("bghvers", "etwa"), size=32),
    z("aber der Schlüssel passt nicht.", 160, 676, beim("bghvers", "Schlüssel"), size=32),
    zit("BGH, a. a. O., Rn. 26", 160, 722, beim("bghvers", "passt")),
    *requisit([("bghgr", K_BUCH, "Wortlaut", WEISS),
               (beim("bghgr", "hohe"), ("tabler", "walk", 100, WEISS), "hohes Gut", GRUEN),
               ("bghsys", ("tabler", "scale", 110, GELB), "§ 239 vor § 240", WEISS),
               ("bghvers", K_BUCH, "Versuch", WEISS),
               (beim("bghvers", "Schlüssel"), ("tabler", "key", 100, GELB), "Schlüssel passt nicht", HELLROT)]),
    *stehend("GE", X2, [("bghgr", "ruhig"), ("bghvers", "denkt")]),
]))

# ===========================================================================================================================
# H Lösung nach der 1. Ansicht und dem BGH
# ===========================================================================================================================
PL1 = "Lösung › 1. Ansicht (BGH)"
folie([("loes", "Lösung · zurück zu Gerber"), ("loes1", f"{PL1} › I. 1. objektiv: der Freiheit beraubt"),
       ("loes2", f"{PL1} › Bemerken ohne Belang"), ("vors", f"{PL1} › I. 2. subjektiv: Vorsatz"),
       ("rw", f"{PL1} › II. Rechtswidrigkeit, III. Schuld"), ("erg1", f"{PL1} › Ergebnis: § 239 Abs. 1 (+)")], rechts_frei([
    *tafel("loes", "Lösung: 1. Ansicht und BGH", h=840),
    z("I. 1. objektiver Tatbestand", 110, 180, "loes1", "ExtraBold", 34),
    *okz("2 Stunden lang der Freiheit beraubt", 235, beim("loes1", "Zwei"), size=32, x=160),
    z("hätte nicht hinausgekonnt, wenn er gewollt hätte", 160, 281, beim("loes1", "hätte"), size=31),
    *okz("dass er schlief und nichts merkte: egal", 341, "loes2", size=32, x=160),
    z("I. 2. subjektiver Tatbestand", 110, 421, "vors", "ExtraBold", 34),
    *okz("Vorsatz: die einzige Tür abgeschlossen, gewollt", 476, beim("vors", "einzige"), size=32, x=160),
    z("II. Rechtswidrigkeit, III. Schuld", 110, 556, "rw", "ExtraBold", 34),
    *okz("keine Rechtfertigungs- oder Entschuldigungsgründe", 611, beim("rw", "nicht"), size=32, x=160),
    blk(110, 700, 1040, 80, GRUEN, "erg1", [("Ergebnis: vollendete Freiheitsberaubung, § 239 Abs. 1", "ExtraBold", 32, INK)]),
    *requisit([("loes", K_TUER, "zurück zu Gerber", WEISS),
               ("loes1", ("tabler", "clock-hour-3", 100, WEISS), "2 Stunden", WEISS),
               ("loes2", K_ZZZ, "nichts gemerkt: egal", WEISS),
               ("vors", ("tabler", "key", 100, GELB), "Vorsatz", WEISS),
               ("rw", ("tabler", "scale", 110, WEISS), "keine Gründe", WEISS),
               ("erg1", K_SCHLOSS, "§ 239 Abs. 1 (+)", GRUEN)]),
    *schlafbett("loes", [("loes", "schlaeft")]),
    *stehend("GE", X2, [("loes", "ruhig"), ("loes2", "denkt"), ("erg1", "sorge")]),
]))

# ===========================================================================================================================
# I Lösung nach der 2. Ansicht; Versuch § 239 Abs. 2 (Wortlautkarte) als Auffang
# ===========================================================================================================================
W2 = ["„(2) Der Versuch ist strafbar.“"]
w2, w2_y = wortlaut(80, 300, 700, W2, "§ 239 Abs. 2 StGB", "vers", marken=[(0, "Versuch", beim("vers", "Versuch", nr=2))], size=32)
PL2 = "Lösung › 2. Ansicht"
folie([("erg2", f"{PL2} › Erfolg: Joscha wollte nirgendwohin"), ("vers", f"{PL2} › Versuch, § 239 Abs. 2 StGB"),
       ("tatent", f"{PL2} › Versuch › Tatentschluss?"), ("erg3", f"{PL2} › Ergebnis: § 239 (−)"),
       ("abw", f"{PL2} › anders bei eingeplantem Aufwachen")], rechts_frei([
    *tafel("erg2", "Lösung: 2. Ansicht", h=880),
    *neinz("Erfolg: Joscha wollte nirgendwohin", 180, "erg2", "Bold", 34, x=160),
    z("Auffang: der Versuch", 110, 250, "vers", "ExtraBold", 34),
    *w2,
    z("Tatentschluss nötig: Joscha an einem", 110, w2_y + 34, "tatent", "Bold", 32),
    z("Fortbewegungswillen hindern", 110, w2_y + 80, beim("tatent", "Fortbewegungswillen"), "Bold", 32),
    *neinz("Gerber war sicher: Joscha schläft durch", w2_y + 150, beim("tatent", "Er"), size=32, x=160),
    zit("vgl. BGH, a. a. O., Rn. 26; § 22 StGB", 160, w2_y + 198, beim("tatent", "durchschläft")),
    blk(110, w2_y + 255, 1040, 80, HELLROT, "erg3", [("Ergebnis: keine Strafbarkeit nach § 239", "ExtraBold", 34, INK)]),
    z("Anders nur, wenn er damit gerechnet hätte,", 110, w2_y + 360, "abw", size=31, farbe=TEXT),
    z("dass Joscha aufwacht und hinauswill", 110, w2_y + 404, beim("abw", "dass"), size=31, farbe=TEXT),
    *requisit([("erg2", K_ZZZ, "will nirgendwohin", WEISS),
               ("vers", K_BUCH, "§ 239 Abs. 2 StGB", GELB),
               ("tatent", ("tabler", "bulb", 100, WEISS), "Tatentschluss?", WEISS),
               ("erg3", ("tabler", "lock-open", 96, WEISS), "§ 239 (−)", HELLROT),
               ("abw", ("tabler", "clock-hour-7", 100, WEISS), "mit Aufwachen gerechnet?", WEISS)]),
    *schlafbett("erg2", [("erg2", "schlaeft")]),
    *stehend("GE", X2, [("erg2", "ruhig"), ("tatent", "froh"), ("abw", "denkt")]),
]))

# ===========================================================================================================================
# J Streitentscheid
# ===========================================================================================================================
folie([("streit", "Streitentscheid · verschiedene Ergebnisse"), ("streit2", "Streitentscheid · 1. Ansicht, mit dem BGH")],
      rechts_frei([
    *tafel("streit", "Streitentscheid", h=760),
    blk(110, 180, 500, 120, GRUEN, "streit", [("1. Ansicht, BGH:", "ExtraBold", 32, INK), ("§ 239 Abs. 1 (+)", "ExtraBold", 32, INK)]),
    blk(650, 180, 500, 120, HELLROT, "streit", [("2. Ansicht:", "ExtraBold", 32, INK), ("§ 239 (−)", "ExtraBold", 32, INK)]),
    z("verschiedene Ergebnisse: Streit entscheiden", 110, 350, beim("streit", "musst"), "Bold", 34),
    *okz("gut begründbar: die 1. Ansicht, mit dem BGH", 440, "streit2", size=32, x=160),
    *okz("Wortlaut und Systematik sprechen für sie", 495, beim("streit2", "Wortlaut"), size=32, x=160),
    blk(110, 580, 1040, 80, GRUEN, beim("streit2", "Dann"), [("Dann ist Gerber strafbar.", "ExtraBold", 34, INK)]),
    *requisit([("streit", ("tabler", "arrows-split", 100, WEISS), "zwei Ergebnisse", WEISS),
               ("streit2", ("tabler", "scale", 110, GELB), "Streitentscheid", GELB)]),
    *schlafbett("streit", [("streit", "ruhig")], mit_zzz=False),
    *stehend("GE", X2, [("streit", "denkt"), (beim("streit2", "Dann"), "still")]),
]))

# ===========================================================================================================================
# K Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Streit nur, wenn er entscheidet"), ("tipp1", "Klausurtipp · Opfer wollte weg: ein Satz"),
       ("tipp2", "Klausurtipp · Schlafende, Getäuschte: Streit im Taterfolg"),
       ("tipp3", "Klausurtipp · 2. Ansicht: Versuch, Tatentschluss")], [
    *tafel("tipp", "Klausurtipp: Streit nur, wo er zählt", fill=HELL, h=700, size=44),
    warnung_i(150, 225, "tipp", gr=26),
    z("1. Den Streit nur, wenn er den Fall entscheidet", 200, 200, "tipp", "Bold", 34),
    z("2. Opfer wollte weg und konnte nicht:", 200, 285, "tipp1", "Bold", 34),
    z("beide Ansichten einig – ein Satz genügt", 200, 333, beim("tipp1", "beide"), size=32),
    z("3. Schlafende oder Getäuschte: Streit in", 200, 418, "tipp2", "Bold", 34),
    z("den Taterfolg „der Freiheit beraubt“", 200, 466, beim("tipp2", "Streit"), size=32),
    z("4. Folgst du der 2. Ansicht: danach den", 200, 551, "tipp3", "Bold", 34),
    z("Versuch, Schwerpunkt Tatentschluss", 200, 599, beim("tipp3", "Versuch"), size=32),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# L Schema
# ===========================================================================================================================
REIHEN = [("s1", "I. Tatbestand", 0, "ExtraBold", 40),
          (beim("s1", "Objektiv"), "1. objektiv: ein Mensch", 1, "Bold", 36),
          ("s2", "eingesperrt oder auf andere Weise der Freiheit beraubt – hier liegt der Streit", 2, "Regular", 34),
          ("s3", "2. subjektiv: Vorsatz", 1, "Bold", 36),
          ("s4", "II. Rechtswidrigkeit", 0, "ExtraBold", 40),
          ("s5", "III. Schuld", 0, "ExtraBold", 40),
          ("s6", "Scheitert die Vollendung: Versuch, § 239 Abs. 2", 0, "Bold", 36)]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Schema: Freiheitsberaubung, § 239 StGB"), 110, 90, "sch", 50)]
y = 210
for c, text, ebene, stil, gr in REIHEN:
    els_sch.append(z(text, 130 + ebene * 60, y, c, stil, gr, rechts=1820))
    y += 92
els_sch.append(zit("Dreistufiger Aufbau: Folge 011", 130, y + 10, "s7", size=30, rechts=1820))
assert y + 60 <= 990, y
folie([("sch", "Schema"), ("s1", "Schema › I. Tatbestand"), ("s2", "Schema › I. 1. der Freiheit beraubt (Streit)"),
       ("s3", "Schema › I. 2. Vorsatz"), ("s4", "Schema › II. Rechtswidrigkeit"), ("s5", "Schema › III. Schuld"),
       ("s6", "Schema › Versuch, § 239 Abs. 2"), ("s7", "Schema › Aufbau: Folge 011")], els_sch)

# ===========================================================================================================================
# M Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Nach dem BGH schützt § 239 die", 0)], [("potenzielle", "a"), (" Fortbewegungsfreiheit.", 0)]],
                750, 300, 46, "merke", {"a": beim("merke", "potenzielle")}),
    *markertext([[("Der Freiheit beraubt ist, wer ", 0), ("nicht weg", "b")],
                 [("könnte, wenn er wollte.", 0)], [("Merken", "c"), (" muss er es nicht.", 0)]], 750, 520, 46, "m2",
                {"b": beim("m2", "nicht"), "c": beim("m2", "Merken")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
