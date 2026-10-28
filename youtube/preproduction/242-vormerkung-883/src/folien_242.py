"""Folge 242 · Vormerkung §§ 883 ff. BGB: Schutz vor dem Doppelverkauf – Serienstandard Open Peeps (Katzenkönig).
Fiktiver Fall: Mats kauft von Herrn Stenzel ein Haus für 420.000 €; beim Notar (ohne Namen, kein echter Ort) Kaufvertrag
und Bewilligung einer Vormerkung, zwei Wochen später Eintragung. Frau Ostendorf bietet 470.000 €; Herr Stenzel verkauft ihr
das Haus, erklärt die Auflassung, sie wird als Eigentümerin eingetragen.
Szenen laut ../SZENENPLAN.md. Zwei Handlungsgeräusche (Unterschrift beim Notar, Auflassung; ../geraeusche_herkunft.json).
Notarzimmer, Tisch, Haus und Grundbuchblatt als Grundformen. Namensschild jeder Figur, solange sie im Bild ist.
Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/pkt als eigene Kopie aus Folge 239 (gemeinsame
Dateien unverändert); neu: notarzimmer(), haus(), strassenbild(), grundbuch().
Wortlautkarten wörtlich nach gesetze-im-internet.de (Abruf 07.10.2026): § 883 Abs. 1 S. 1 BGB (Auszug), § 885 Abs. 1 S. 1
BGB (Auszug), § 883 Abs. 2 S. 1 BGB, § 888 Abs. 1 BGB (Auszug). Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_242/"

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


def bl(art, w, h, cue, cx, cy, **k):
    """blase() mit kleinem Versatz, falls blase_c.js an einer Pfadnaht scheitert (Spitze bleibt am Mund, Stil C bleibt)."""
    for dx in (0, 8, -8, 16, -16, 24, -24):
        try:
            return blase(art, w, h, cue, cx + dx, cy, **k)
        except AssertionError as e:
            if "Stil C" not in str(e):
                raise
    raise AssertionError(f"Blase Stil C an keiner Position möglich: {cue}")


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
        if n.startswith(("bild:", "ficon:")) or "/op_242/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def umbruch(text, size, breite, stil="Regular"):
    """Zeilenumbruch für Wortlautkarten (Wortlaut bleibt unverändert)."""
    f = F(stil, size)
    zeilen, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if f.getlength(t) <= breite:
            cur = t
        else:
            zeilen.append(cur); cur = w
    return zeilen + [cur] if cur else zeilen


def wortlaut(x, y, w, zeilen, quelle, cue, marken=(), size=32, bis=None):
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 07.10.2026), als Zitat mit Normangabe;
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 124/149/196/239) ------------------------------------
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




def pkt(text, y, cue, stil="Regular", size=34, x=185, **k):
    """Tafelzeile mit Aufzählungspunkt (Kriterium oder Argument, keine Bewertung)."""
    return [z("•", x - 38, y, cue, "ExtraBold", size), z(text, x, y, cue, stil, size, **k)]



X1, X2 = 1430, 1730                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"MA": "Mats", "ST": "Herr Stenzel", "OS": "Frau Ostendorf"}
NFARBE = {"MA": BLAU, "ST": GRUEN, "OS": PINK}


def stehend(k, x, folge, unten=FB, hoehe=FR):
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


def zwei(k1, folge1, k2, folge2):
    """Zwei Figuren neben der Tafel, beide blicken nach links zur Tafel."""
    return [*stehend(k1, X1, folge1), *stehend(k2, X2, folge2)]


# --- eigene Szenenbausteine (programmatisch, Palettenflächen, Tuschekontur) ---------------------------------------------------
HELLBLAU = (214, 230, 252, 255)
WAND = (236, 230, 220, 255)
PAPIER = (240, 246, 255, 255)
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
G0 = 900                                     # Boden der Fallszenen
FHA = 430                                    # Figurenhöhe in den Fallszenen
IX, JX = 1180, 1650                          # Notartermin: Herr Stenzel links (blickt nach rechts), Mats rechts (blickt nach links)
HX = 1415                                    # Tisch zwischen beiden
SX, OX, MX = 1150, 1470, 1770                # vor dem Haus: Herr Stenzel (blickt nach rechts), Frau Ostendorf, Mats (blicken nach links)


def boden_(y, c, fill=None, x0=30, x1=1890, h=None):
    hh = h or 60
    im = Image.new("RGBA", (x1 - x0, hh))
    dr = ImageDraw.Draw(im)
    if fill:
        dr.rectangle((0, 0, x1 - x0, hh), fill=fill)
    dr.line((0, 2, x1 - x0, 2), fill=INK, width=6)
    return El(im, x0, y, c, "cut", 0.0, None, name="boden")


def notarzimmer(c):
    """Besprechungsraum beim Notar (ohne Namen, kein echter Ort): Wand mit Aktenregal und Fenster, Schild „Notar“, Tisch."""
    els = [hart(boden_(G0, c, fill=(226, 222, 214, 255), h=100))]
    w, h = 900, 560
    im = Image.new("RGBA", (w, h))
    dr = ImageDraw.Draw(im)
    dr.rounded_rectangle((0, 0, w - 1, h - 1), 14, fill=WAND, outline=INK, width=5)
    # Aktenregal links: drei Böden mit Ordnerrücken in Palettenfarben
    rx, ry, rw = 50, 150, 330
    dr.rectangle((rx, ry, rx + rw, ry + 380), fill=(205, 160, 115, 255), outline=INK, width=5)
    farben = [BLAU, GELB, GRUEN, ROT, LILA, WEISS]
    for k in range(3):
        y0 = ry + 12 + k * 124
        for j in range(7):
            x0 = rx + 16 + j * 44
            dr.rectangle((x0, y0, x0 + 36, y0 + 104), fill=farben[(j + k) % 6], outline=INK, width=3)
        dr.line((rx, y0 + 112, rx + rw, y0 + 112), fill=INK, width=5)
    fx, fy = 520, 160                              # Fenster
    dr.rectangle((fx, fy, fx + 300, fy + 220), fill=HELLBLAU, outline=INK, width=5)
    dr.line((fx + 150, fy, fx + 150, fy + 220), fill=INK, width=4)
    dr.line((fx, fy + 110, fx + 300, fy + 110), fill=INK, width=4)
    els.append(hart(El(im, 70, G0 - h, c, "cut", 0.0, None, name="notarzimmer")))
    els.append(hart(pl("Notar", 70 + 670, G0 - h + 40, c, fill=WEISS, size=30, anker="m")))
    t = Image.new("RGBA", (320, 170))
    dt = ImageDraw.Draw(t)
    dt.rounded_rectangle((0, 0, 319, 34), 8, fill=(170, 120, 80, 255), outline=INK, width=5)
    for xx in (22, 278):
        dt.rectangle((xx, 30, xx + 20, 169), fill=(170, 120, 80, 255), outline=INK, width=4)
    els.append(hart(El(t, HX - 160, G0 - 170, c, "cut", 0.0, None, name="tisch")))
    return els


def _haus_bild(w):
    """Einfamilienhaus als Grundform: weiße Wand, rotes Dach mit Schornstein, Tür, zwei Fenster (Tuschekontur)."""
    s = 3
    h = int(w * 0.92)
    W_, H_ = w * s, h * s
    im = Image.new("RGBA", (W_, H_))
    dr = ImageDraw.Draw(im)
    lw = 5 * s
    dach = [(0.02 * W_, 0.42 * H_), (0.50 * W_, 0.03 * H_), (0.98 * W_, 0.42 * H_)]
    dr.rectangle((0.70 * W_, 0.08 * H_, 0.80 * W_, 0.30 * H_), fill=(200, 200, 204, 255), outline=INK, width=lw)
    dr.polygon(dach, fill=ROT)
    dr.line(dach + [dach[0]], fill=INK, width=lw, joint="curve")
    dr.rectangle((0.10 * W_, 0.42 * H_, 0.90 * W_, 0.985 * H_), fill=WEISS, outline=INK, width=lw)
    dr.rectangle((0.42 * W_, 0.64 * H_, 0.58 * W_, 0.985 * H_), fill=(190, 135, 90, 255), outline=INK, width=lw)
    for fx in (0.17, 0.66):
        dr.rectangle((fx * W_, 0.52 * H_, (fx + 0.17) * W_, 0.72 * H_), fill=HELLBLAU, outline=INK, width=4 * s)
        dr.line(((fx + 0.085) * W_, 0.52 * H_, (fx + 0.085) * W_, 0.72 * H_), fill=INK, width=3 * s)
    dr.ellipse((0.375 * W_, 0.20 * H_, 0.625 * W_, 0.33 * H_), fill=GELB, outline=INK, width=4 * s)   # Dachfenster
    return im.resize((w, h), Image.LANCZOS)


def haus(cx, unten, c, breite=560):
    im = _haus_bild(breite)
    return hart(El(im, cx - im.width // 2, unten - im.height, c, "cut", 0.0, None, name="haus"))


def strassenbild(c):
    """Vor dem Haus von Herrn Stenzel: Boden, Haus, Busch."""
    els = [hart(boden_(G0, c, fill=(214, 226, 196, 255), h=100)), haus(430, G0, c, breite=460)]
    els.append(hart(ficon("tabler", "plant-2", 800, G0, 110, c, fuell=GRUEN, anim="cut")))
    return els


def grundbuch(x, y, w, zeilen, c, size=30, bis=None, titel_="Grundbuch"):
    """Grundbuchblatt als Karte (Grundform): zeilen = [(text, cue, streich_cue|None)]. Gestrichene Einträge bekommen zum
    Wort eine rote Linie (nicht mehr maßgeblich). Kein Anspruch auf die amtliche Abteilungsgliederung."""
    lh = int(size * 1.6)
    hgt = 76 + lh * len(zeilen) + 10
    els = [bis_(karte(x, y, w, hgt, c, fill=PAPIER, rund=14, schatten=6, rand=4), bis)]
    els.append(bis_(ficon("tabler", "book-2", x + 46, y + 62, 44, c, fuell=BLAU), bis))
    els.append(z(titel_, x + 80, y + 18, c, "ExtraBold", 32, rechts=x + w - 16, bis=bis))
    f = F("Bold", size)
    for i, (t, zc, sc) in enumerate(zeilen):
        yy = y + 76 + i * lh
        els.append(z(t, x + 30, yy, zc, "Bold", size, rechts=x + w - 16, bis=bis))
        if sc:
            tw = int(f.getlength(t)) + 16
            im = Image.new("RGBA", (tw, 8))
            ImageDraw.Draw(im).rounded_rectangle((0, 0, tw - 1, 7), 3, fill=DROT)
            els.append(El(im, x + 22, yy + size * 0.62, sc, "fade", 0.0, bis, name="streich:" + t))
    return els, y + hgt


# ===========================================================================================================================
# A1 Fall: der Notartermin
# ===========================================================================================================================
MA_DA, ST_DA = beim("mats", "Mats"), beim("haus", "Stenzel")
GB_V = beim("eintr", "Vormerkung")
gb1, _ = grundbuch(70, 30, 760, [("Eigentümer: Herr Stenzel", "eintr", None), ("Vormerkung für Mats", GB_V, None)], "eintr")
folie([(NULL, "Fall · Der Doppelverkauf"), (MA_DA, "Fall · Mats"), ("haus", "Fall · Mats kauft ein Haus"),
       ("notar", "Fall · Kaufvertrag beim Notar"), ("bew", "Fall · Vormerkung bewilligt"),
       ("st1", "Fall · Herr Stenzel: Glückwunsch"), ("ma1", "Fall · Mats wartet auf das Grundbuch"),
       ("eintr", "Fall · Vormerkung im Grundbuch")], [
    *notarzimmer(NULL),
    hart(pl("Nach dem Notartermin …", 70, 30, NULL, fill=GELB, size=32, bis="haus")),
    pl("… verkauft der Verkäufer das Haus noch einmal", 70, 100, beim("fall", "verkauft"), fill=WEISS, size=32, bis="haus"),
    pl("an einen Meistbietenden", 70, 170, beim("fall", "Meistbietenden"), fill=HELLROT, size=32, bis="haus"),
    pl("Mats kauft von Herrn Stenzel ein Haus", 70, 30, "haus", fill=WEISS, size=32, bis="eintr"),
    pl("Kaufpreis: 420.000 €", 70, 100, beim("haus", "vierhundertzwanzigtausend"), fill=GELB, size=32, bis="eintr"),
    pl("beim Notar: Kaufvertrag unterschrieben", 70, 170, beim("notar", "unterschreiben"), fill=WEISS, size=32, bis="eintr"),
    pl("Herr Stenzel bewilligt eine Vormerkung", 70, 240, beim("bew", "bewilligt"), fill=GRUEN, size=32, bis="eintr"),
    ficon("tabler", "home", 285, G0 - 420, 100, "haus", fuell=GELB, bis="eintr"),
    ficon("tabler", "file-text", HX - 70, G0 - 170, 90, beim("notar", "Kaufvertrag"), fuell=WEISS),
    szene(ficon("tabler", "writing-sign", HX + 50, G0 - 170, 90, beim("notar", "unterschreiben")), "242unterschrift*", 0.5),
    ficon("tabler", "file-certificate", HX + 50, G0 - 270, 80, beim("bew", "bewilligt"), fuell=GRUEN, bis="eintr"),
    *fig("MA", JX, G0, FHA, [(MA_DA, "ruhig"), ("haus", "froh"), ("notar", "ernst"), ("bew", "froh"), ("st1", "freut")], bis="ma1"),
    *redet("MA_redet", JX, G0, FHA, "ma1", "eintr"),
    *fig("MA", JX, G0, FHA, [("eintr", "froh"), (GB_V, "freut")], erst="cut"),
    ns("Mats", JX, G0, MA_DA, BLAU, d=0.1),
    *fig("ST", IX, G0, FHA, [(ST_DA, "froh_r"), ("notar", "ruhig_r")], bis="st1"),
    *redet("ST_redet_r", IX, G0, FHA, "st1", "ma1"),
    *fig("ST", IX, G0, FHA, [("ma1", "froh_r"), ("eintr", "ruhig_r")], erst="cut"),
    ns("Herr Stenzel", IX, G0, ST_DA, GRUEN, d=0.1),
    bl("sprech", 700, 220, "st1", 1440, 230, inhalt=["Glückwunsch! Bald gehört", "das Haus Ihnen."],
          textsize=36, figur=("ST_redet_r", IX, G0, FHA), bis="ma1"),
    bl("sprech", 740, 220, "ma1", 1300, 210, inhalt=["Dann warte ich jetzt nur", "noch auf das Grundbuch."],
          textsize=36, figur=("MA_redet", JX, G0, FHA), bis="eintr"),
    *gb1,
    pl("2 Wochen später", 900, 40, "eintr", fill=GELB, size=32),
])

# ===========================================================================================================================
# A2 Fall: vor dem Haus – Frau Ostendorf bietet mehr
# ===========================================================================================================================
OS_DA = beim("west", "Ostendorf")
GB_OS = beim("weg", "Eigentümerin")
gb2, _ = grundbuch(70, 30, 760, [("Eigentümer: Herr Stenzel", "west", GB_OS), ("Vormerkung für Mats", "west", None),
                                 ("Eigentümerin: Frau Ostendorf", GB_OS, None)], "west")
folie([("west", "Fall · Frau Ostendorf meldet sich"), ("we1", "Fall · Frau Ostendorf bietet 470.000 €"),
       ("st2", "Fall · Herr Stenzel: Da sage ich nicht nein"), ("zweit", "Fall · Zweiter Verkauf und Auflassung"),
       ("weg", "Fall · Frau Ostendorf im Grundbuch"), ("frage", "Fall · Die Frage")], [
    *strassenbild("west"),
    *[hart(e) if e.cue == "west" else e for e in gb2],
    *fig("ST", SX, G0, FHA, [("west", "ruhig_r"), ("we1", "denkt_r"), (beim("we1", "vierhundertsiebzigtausend"), "froh_r")],
         bis="st2", erst="cut"),
    *redet("ST_redet_r", SX, G0, FHA, "st2", "zweit"),
    *fig("ST", SX, G0, FHA, [("zweit", "froh_r"), ("frage", "still_r")], erst="cut"),
    ns("Herr Stenzel", SX, G0, "west", GRUEN),
    *fig("OS", OX, G0, FHA, [(OS_DA, "froh")], bis="we1"),
    *redet("OS_redet", OX, G0, FHA, "we1", "st2"),
    *fig("OS", OX, G0, FHA, [("st2", "froh"), (GB_OS, "staunt"), ("frage", "ruhig")], erst="cut"),
    ns("Frau Ostendorf", OX, G0, OS_DA, PINK, d=0.1),
    bl("sprech", 740, 220, "we1", 1280, 230, inhalt=["Ich zahle Ihnen 470.000 €", "für das Haus!"],
          textsize=36, figur=("OS_redet", OX, G0, FHA), bis="st2"),
    bl("sprech", 620, 170, "st2", 1330, 250, inhalt=["Da sage ich nicht nein."],
          textsize=36, figur=("ST_redet_r", SX, G0, FHA), bis="zweit"),
    pl("Kaufvertrag mit Frau Ostendorf: 470.000 €", 70, 320, beim("zweit", "verkauft"), fill=WEISS, size=32, bis="frage"),
    szene(pl("Auflassung erklärt", 70, 390, beim("zweit", "Auflassung"), fill=GELB, size=32, bis="frage"), "242auflassung*", 0.5),
    ficon("tabler", "writing-sign", 500, 452, 70, beim("zweit", "Auflassung"), bis="frage"),
    pl("Hat Mats das Haus verloren?", 960, 40, "frage", fill=PINK, size=34),
    pl("Und was bringt ihm die Vormerkung?", 960, 115, "frage2", fill=WEISS, size=32),
    *fig("MA", MX, G0, FHA, [("frage", "schreck"), ("frage2", "denkt")]),
    ns("Mats", MX, G0, "frage", BLAU, d=0.1),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_242(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=40, zeilenabstand=1.32)
        els += e; y += 16
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_242("sv", [
    "Mats kauft von Herrn Stenzel ein Haus für 420.000 €. Beim Notar unterschreiben beide den Kaufvertrag, und "
    "Herr Stenzel bewilligt eine Vormerkung für Mats. Zwei Wochen später ist die Vormerkung im Grundbuch eingetragen.",
    "Dann bietet Frau Ostendorf Herrn Stenzel 470.000 € für das Haus. Herr Stenzel verkauft ihr das Haus und erklärt die "
    "Auflassung. Frau Ostendorf wird als Eigentümerin ins Grundbuch eingetragen.",
], "Hat Mats das Haus verloren? Was bringt ihm die Vormerkung?")

_zl = lambda W, wort: next(i for i, t in enumerate(W) if wort in t)

# ===========================================================================================================================
# C Das Problem: die Zwischenzeit bis zur Eintragung
# ===========================================================================================================================
PC = "Das Problem"
folie([("prob", f"{PC} · Eigentum erst mit der Eintragung"), ("prob2", f"{PC} · Herr Stenzel kann noch verfügen"),
       ("prob3", f"{PC} · ohne Vormerkung"), ("prob4", f"{PC} · Verweis Hauskauf"),
       ("loes", f"{PC} · Lösung: die Vormerkung")], rechts_frei([
    *tafel("prob", "Das Problem: die Zwischenzeit"),
    pl("Kaufvertrag", 110, 180, "prob", fill=WEISS, size=30),
    pfeil(350, 212, 860, 212, "prob", breite=8, kopf=26),
    pl("Eintragung", 880, 180, beim("prob", "Eintragung"), fill=GRUEN, size=30),
    z("Zwischenzeit", 500, 236, "prob2", "ExtraBold", 30, farbe=DROT),
    *pkt("Eigentum erst mit der Eintragung, §§ 873, 925 BGB", 300, beim("prob", "Eintragung"), "Bold", 31, x=160),
    *pkt("bis dahin: Herr Stenzel bleibt Eigentümer", 360, "prob2", "Bold", 31, x=160),
    z("und kann noch einmal verfügen", 160, 406, beim("prob2", "verfügen"), "Bold", 31),
    blk(110, 470, 1040, 125, HELLROT, "prob3", [("ohne Vormerkung: Erwerb von Frau Ostendorf voll wirksam", "ExtraBold", 31, INK),
                                               ("Mats: nur Ansprüche gegen Herrn Stenzel, etwa Schadensersatz", "Bold", 29, INK)]),
    zit("Mehr: Video „Hauskauf in drei Schritten: Kaufvertrag, Auflassung, Grundbuch“", 110, 615, "prob4"),
    blk(110, 680, 1040, 80, GRUEN, "loes", [("Lösung für die Zwischenzeit: die Vormerkung", "ExtraBold", 33, INK)]),
    *requisit([("prob", ("tabler", "hourglass", 100, GELB), "erst mit der Eintragung", WEISS),
               ("prob2", ("tabler", "home", 120, GELB), "noch einmal verfügen", HELLROT),
               ("prob3", ("tabler", "cash", 120, GRUEN), "nur Schadensersatz", HELLROT),
               ("loes", ("tabler", "shield-lock", 110, GRUEN), "Vormerkung", GRUEN)]),
    *zwei("ST", [("prob", "ruhig"), ("prob2", "denkt"), ("loes", "still")], "MA", [("prob", "denkt"), ("prob3", "sorge"), ("loes", "staunt")]),
]))

# ===========================================================================================================================
# D § 883 Abs. 1 BGB (Wortlautkarte), vier Voraussetzungen
# ===========================================================================================================================
W883 = umbruch("„Zur Sicherung des Anspruchs auf Einräumung oder Aufhebung eines Rechts an einem Grundstück … kann eine "
               "Vormerkung in das Grundbuch eingetragen werden.“", 30, 1040)
w883, w883_y = wortlaut(80, 170, 1100, W883, "§ 883 Abs. 1 Satz 1 BGB (Auszug)", "norm",
                        marken=[(_zl(W883, "Sicherung"), "Sicherung", beim("w883", "Sicherung")),
                                (_zl(W883, "Grundstück"), "Grundstück", beim("w883", "Grundstück")),
                                (_zl(W883, "eingetragen"), "eingetragen", beim("w883", "eingetragen"))], size=30)
PD = "A. Voraussetzungen, § 883 Abs. 1 BGB"
y4 = w883_y + 24
folie([("norm", PD), ("w883", f"{PD} › Wortlaut"), ("vier", f"{PD} › 4 Voraussetzungen")], rechts_frei([
    *tafel("norm", "Die Vormerkung, § 883 Abs. 1 BGB", size=44),
    *w883,
    zit("i. V. m. § 885 Abs. 1 BGB", 110, y4, "vier"),
    pl("1. zu sichernder Anspruch", 110, y4 + 44, "v1", fill=GELB, size=30),
    pl("2. Bewilligung oder einstweilige Verfügung", 110, y4 + 114, "v2", fill=GELB, size=30),
    pl("3. Eintragung", 110, y4 + 184, "v3", fill=GELB, size=30),
    pl("4. Berechtigung des Bewilligenden", 110, y4 + 254, "v4", fill=GELB, size=30),
    *requisit([("norm", ("tabler", "scale", 120, WEISS), "§ 883 Abs. 1 BGB", WEISS),
               ("w883", ("tabler", "shield-lock", 110, GRUEN), "Sicherung des Anspruchs", GELB),
               ("vier", ("tabler", "list-check", 110, None), "4 Voraussetzungen", GELB)]),
    *zwei("ST", [("norm", "ruhig"), ("vier", "denkt")], "MA", [("norm", "ruhig"), ("w883", "denkt"), ("vier", "froh")]),
]))
assert y4 + 254 + 70 <= 900, y4

# ===========================================================================================================================
# E 1. Zu sichernder Anspruch, Akzessorietät
# ===========================================================================================================================
PE = f"{PD} › 1. zu sichernder Anspruch"
folie([("a1", PE), ("a2", f"{PE} › Übereignung aus § 433 BGB"), ("a3", f"{PE} › Kaufvertrag wirksam"),
       ("akz", f"{PE} › Akzessorietät"), ("kuenft", f"{PE} › künftige oder bedingte Ansprüche")], rechts_frei([
    *tafel("a1", "1. Zu sichernder Anspruch"),
    *pkt("auf eine dingliche Rechtsänderung gerichtet", 175, beim("a1", "dingliche"), "Bold", 32, x=160),
    *okz("Mats: Anspruch auf Übereignung des Hauses", 245, beim("a2", "Anspruch"), "Bold", 32, x=160),
    zit("§ 433 Abs. 1 S. 1 BGB", 160, 290, beim("a2", "Anspruch")),
    *okz("Kaufvertrag notariell beurkundet: wirksam", 345, "a3", "Bold", 32, x=160),
    zit("§ 311b Abs. 1 S. 1 BGB", 160, 390, "a3"),
    blk(110, 450, 1040, 125, GELB, "akz", [("Akzessorietät", "ExtraBold", 33, INK),
                                         ("streng akzessorisches Sicherungsmittel", "Bold", 30, INK)]),
    zit("BGH, Urt. v. 8.3.2024 – V ZR 176/22, Rn. 31", 110, 588, beim("akz", "Bundesgerichtshof")),
    *pkt("erlischt, wenn der gesicherte Anspruch nicht mehr besteht", 640, "akz2", "Bold", 30, x=160),
    *pkt("auch künftige oder bedingte Ansprüche, § 883 Abs. 1 S. 2 BGB", 710, "kuenft", "Bold", 30, x=160),
    *requisit([("a1", ("tabler", "home", 120, GELB), "Anspruch auf das Haus", WEISS),
               ("a2", ("tabler", "file-text", 110, WEISS), "Kaufvertrag", WEISS),
               ("akz", ("tabler", "link", 110, None), "akzessorisch", GELB),
               ("akz2", ("tabler", "unlink", 110, None), "ohne Anspruch keine Vormerkung", HELLROT),
               ("kuenft", ("tabler", "calendar-event", 110, WEISS), "künftig oder bedingt", WEISS)]),
    *stehend("MA", FX, [("a1", "ruhig"), ("a2", "froh"), ("akz", "denkt"), ("akz2", "sorge"), ("kuenft", "ruhig")]),
]))

# ===========================================================================================================================
# F 2. Bewilligung, § 885 Abs. 1 BGB (Wortlautkarte), einstweilige Verfügung
# ===========================================================================================================================
W885 = umbruch("„Die Eintragung einer Vormerkung erfolgt auf Grund einer einstweiligen Verfügung oder auf Grund der "
               "Bewilligung desjenigen, dessen Grundstück … von der Vormerkung betroffen wird.“", 30, 1040)
w885, w885_y = wortlaut(80, 165, 1100, W885, "§ 885 Abs. 1 Satz 1 BGB (Auszug)", "w885",
                        marken=[(_zl(W885, "einstweiligen"), "einstweiligen", beim("w885", "einstweiligen")),
                                (_zl(W885, "Bewilligung"), "Bewilligung", beim("w885", "Bewilligung")),
                                (_zl(W885, "betroffen"), "betroffen", beim("w885", "betroffen"))], size=30)
PF = f"{PD} › 2. Bewilligung"
yf = w885_y + 26
folie([("b1", PF), ("w885", f"{PF} › § 885 Abs. 1 BGB"), ("b2", f"{PF} › Herr Stenzel hat bewilligt"),
       ("evf", f"{PF} › oder einstweilige Verfügung")], rechts_frei([
    *tafel("b1", "2. Bewilligung oder einstweilige Verfügung", size=42),
    *w885,
    *okz("Herr Stenzel hat beim Notar bewilligt", yf, "b2", "Bold", 32, x=160),
    *pkt("Verkäufer weigert sich: einstweilige Verfügung", yf + 75, "evf", "Bold", 31, x=160),
    *pkt("Gefährdung des Anspruchs muss nicht", yf + 140, "evf2", "Bold", 31, x=160),
    z("glaubhaft gemacht werden", 160, yf + 186, beim("evf2", "glaubhaft"), "Bold", 31),
    zit("§ 885 Abs. 1 S. 2 BGB", 160, yf + 232, beim("evf2", "glaubhaft")),
    *requisit([("b1", ("tabler", "file-certificate", 110, GRUEN), "Bewilligung", GRUEN),
               ("evf", ("tabler", "gavel", 110, WEISS), "einstweilige Verfügung", WEISS)]),
    *zwei("ST", [("b1", "ruhig"), ("b2", "froh"), ("evf", "ernst")], "MA", [("b1", "ruhig"), ("b2", "froh"), ("evf", "denkt")]),
]))
assert yf + 232 + 40 <= 900, yf

# ===========================================================================================================================
# G 3. Eintragung, 4. Berechtigung (gutgläubiger Ersterwerb nur bei bestehendem Anspruch), Zwischenergebnis
# ===========================================================================================================================
PG = PD
gbG, gbG_y = grundbuch(1290, 70, 580, [("Eigentümer: Herr Stenzel", "e1", None), ("Vormerkung für Mats", beim("e2", "Grundbuch"), None)],
                       "e1", size=29)
folie([("e1", f"{PG} › 3. Eintragung"), ("ber", f"{PG} › 4. Berechtigung"), ("gut", f"{PG} › 4. Berechtigung › gutgläubiger Erwerb"),
       ("zw", f"{PG} › Zwischenergebnis")], rechts_frei([
    *tafel("e1", "3. Eintragung · 4. Berechtigung"),
    *okz("3. Vormerkung für Mats steht im Grundbuch", 175, beim("e2", "Grundbuch"), "Bold", 32, x=160),
    *pkt("schon vor der Übereignung an Frau Ostendorf", 235, beim("e2", "schon"), "Bold", 31, x=160),
    *pkt("4. Herr Stenzel muss Eigentümer sein", 320, beim("ber", "Herr"), "Bold", 32, x=160),
    *okz("er steht zu Recht im Grundbuch", 380, "ber2", "Bold", 32, x=160),
    blk(110, 450, 1040, 125, HELLBLAU, "gut", [("nur zu Unrecht eingetragen: gutgläubiger Erwerb", "ExtraBold", 31, INK),
                                             ("entsprechend § 892 BGB", "Bold", 30, INK)]),
    *pkt("aber nur, wenn der gesicherte Anspruch besteht", 595, "gut2", "Bold", 31, x=160),
    zit("BGH, Urt. v. 9.12.2022 – V ZR 91/21, Rn. 23; V ZR 176/22, Rn. 24", 160, 640, "gut2"),
    *okz("Zwischenergebnis: Mats hat eine wirksame Vormerkung", 720, "zw", "ExtraBold", 32, x=160),
    *gbG,
    *stehend("ST", FX, [("e1", "ruhig"), ("ber", "ernst"), ("ber2", "froh"), ("gut", "denkt"), ("zw", "still")]),
]))

# ===========================================================================================================================
# H B. Wirkung: § 883 Abs. 2 BGB (Wortlautkarte), relative Unwirksamkeit
# ===========================================================================================================================
W8832 = umbruch("„Eine Verfügung, die nach der Eintragung der Vormerkung über das Grundstück oder das Recht getroffen wird, "
                "ist insoweit unwirksam, als sie den Anspruch vereiteln oder beeinträchtigen würde.“", 30, 1040)
w8832, w8832_y = wortlaut(80, 165, 1100, W8832, "§ 883 Abs. 2 Satz 1 BGB", "w8832",
                          marken=[(_zl(W8832, "Verfügung"), "Verfügung", beim("w8832", "Verfügung")),
                                  (_zl(W8832, "Eintragung"), "Eintragung", beim("w8832", "Eintragung")),
                                  (_zl(W8832, "unwirksam"), "unwirksam", beim("w8832", "unwirksam")),
                                  (_zl(W8832, "vereiteln"), "vereiteln", beim("w8832", "vereiteln"))], size=30)
PH = "B. Wirkung, § 883 Abs. 2 BGB"
yh = w8832_y + 24
REL = beim("rel", "relativ")
gbH, _ = grundbuch(1290, 70, 580, [("Eigentümer: Herr Stenzel", "wirk", "wirk"), ("Vormerkung für Mats", "wirk", None),
                                   ("Eigentümerin: Frau Ostendorf", "wirk", None)], "wirk", size=29)
folie([("wirk", PH), ("verf", f"{PH} › zweiter Kaufvertrag: keine Verfügung"), ("verf2", f"{PH} › Übereignung an Frau Ostendorf"),
       ("rel", f"{PH} › relative Unwirksamkeit")], rechts_frei([
    *tafel("wirk", "Wirkung: § 883 Abs. 2 BGB"),
    *w8832,
    *pkt("zweiter Kaufvertrag: keine Verfügung, bleibt wirksam", yh, "verf", "Bold", 31, x=160),
    *pkt("Übereignung an Frau Ostendorf vereitelt den Anspruch", yh + 62, beim("verf2", "vereitelt"), "Bold", 31, x=160),
    blk(110, yh + 130, 1040, 125, GELB, "rel", [("relativ unwirksam: nur Mats gegenüber", "ExtraBold", 32, INK),
                                               ("allen anderen gegenüber: Frau Ostendorf Eigentümerin", "Bold", 30, INK)]),
    zit("BGH, Urt. v. 2.7.2010 – V ZR 240/09, Rn. 7, 10", 110, yh + 268, REL),
    *gbH,
    pl("Mats gegenüber unwirksam", 1580, gbH[0].y + 260, REL, fill=HELLROT, size=28, anker="m"),
    *zwei("OS", [("wirk", "ruhig"), ("verf2", "sorge"), ("rel2", "froh")], "MA", [("wirk", "denkt"), ("verf2", "ernst"), ("rel", "froh")]),
]))
assert yh + 268 + 40 <= 900, yh

# ===========================================================================================================================
# I C. Durchsetzung: § 888 Abs. 1 BGB (Wortlautkarte), Zustimmung
# ===========================================================================================================================
W888 = umbruch("„Soweit der Erwerb eines eingetragenen Rechts … gegenüber demjenigen, zu dessen Gunsten die Vormerkung "
               "besteht, unwirksam ist, kann dieser von dem Erwerber die Zustimmung zu der Eintragung oder der Löschung "
               "verlangen, die zur Verwirklichung des durch die Vormerkung gesicherten Anspruchs erforderlich ist.“", 30, 1040)
w888, w888_y = wortlaut(80, 160, 1100, W888, "§ 888 Abs. 1 BGB (Auszug)", "w888",
                        marken=[(_zl(W888, "Erwerber"), "Erwerber", beim("w888", "Erwerberin")),
                                (_zl(W888, "Zustimmung"), "Zustimmung", beim("w888", "Zustimmung")),
                                (_zl(W888, "Eintragung"), "Eintragung", beim("w888", "Eintragung")),
                                (_zl(W888, "unwirksam"), "unwirksam", beim("w888", "unwirksam"))], size=30)
PI = "C. Durchsetzung, § 888 Abs. 1 BGB"
yi = w888_y + 22
gbI, _ = grundbuch(1290, 70, 580, [("Eigentümerin: Frau Ostendorf", "durch", None), ("Vormerkung für Mats", "durch", None)],
                   "durch", size=29)
folie([("durch", PI), ("w888", f"{PI} › Zustimmung zur Eintragung"), ("bleibt", f"{PI} › Frau Ostendorf bleibt eingetragen"),
       ("zwei", f"{PI} › zwei Ansprüche")], rechts_frei([
    *tafel("durch", "Durchsetzung: § 888 Abs. 1 BGB"),
    *w888,
    *pkt("bis dahin bleibt Frau Ostendorf im Grundbuch", yi, "bleibt", "Bold", 31, x=160),
    *pkt("erst mit ihrer Zustimmung: Eintragung von Mats", yi + 56, "bleibt2", "Bold", 31, x=160),
    blk(110, yi + 120, 505, 120, BLAU, "zwei2", [("von Herrn Stenzel:", "ExtraBold", 31, INK), ("die Übereignung", "Bold", 30, INK)]),
    blk(645, yi + 120, 505, 120, PINK, "zwei3", [("von Frau Ostendorf:", "ExtraBold", 31, INK), ("die Zustimmung", "Bold", 30, INK)]),
    zit("BGH, Urt. v. 2.7.2010 – V ZR 240/09, Rn. 7, 13", 110, yi + 252, "zwei3"),
    *gbI,
    pl("Zustimmung von Frau Ostendorf?", 1580, gbI[0].y + 210, beim("w888", "Zustimmung"), fill=PINK, size=28, anker="m"),
    *zwei("OS", [("durch", "ruhig"), ("w888", "denkt"), ("bleibt", "ernst"), ("zwei3", "sorge")],
          "MA", [("durch", "denkt"), ("w888", "froh"), ("zwei", "ruhig")]),
]))
assert yi + 252 + 40 <= 900, yi

# ===========================================================================================================================
# J Ergebnis vor dem Haus; Insolvenz (§ 106 Abs. 1 InsO)
# ===========================================================================================================================
GB_MA = beim("erg2", "eingetragen")
gbJ, _ = grundbuch(70, 30, 760, [("Eigentümerin: Frau Ostendorf", "erg", GB_MA), ("Vormerkung für Mats", "erg", None),
                                 ("Eigentümer: Mats", GB_MA, None)], "erg")
folie([("erg", "Ergebnis · Mats verliert das Haus nicht"), (GB_MA, "Ergebnis · Mats wird Eigentümer"),
       ("ins", "Ergebnis · Insolvenz, § 106 Abs. 1 InsO")], [
    *strassenbild("erg"),
    *gbJ,
    pl("Mats verliert das Haus nicht", 960, 40, beim("erg", "Mats"), fill=GRUEN, size=34),
    pl("Übereignung durch Herrn Stenzel", 960, 115, beim("erg2", "Übereignung"), fill=WEISS, size=30),
    pl("Zustimmung von Frau Ostendorf", 960, 180, beim("erg2", "Zustimmung"), fill=WEISS, size=30),
    pl("Wird Herr Stenzel insolvent: § 106 Abs. 1 InsO", 70, 320, beim("ins", "Paragraf"), fill=GELB, size=30),
    pl("Befriedigung aus der Insolvenzmasse", 70, 386, beim("ins", "Befriedigung"), fill=WEISS, size=30),
    pl("Vormerkung insolvenzfest", 960, 250, "ins2", fill=GRUEN, size=30),
    zit("BGH, Urt. v. 25.3.2021 – IX ZR 70/20, Rn. 34", 975, 322, "ins2", rechts=1880),
    *fig("ST", SX, G0, FHA, [("erg", "still_r"), (beim("erg2", "Übereignung"), "ruhig_r"), ("ins", "sorge_r")], erst="cut"),
    ns("Herr Stenzel", SX, G0, "erg", GRUEN),
    *fig("OS", OX, G0, FHA, [("erg", "ernst"), (beim("erg2", "Zustimmung"), "ruhig")], erst="cut"),
    ns("Frau Ostendorf", OX, G0, "erg", PINK),
    *fig("MA", MX, G0, FHA, [("erg", "froh"), (GB_MA, "freut"), ("ins", "ruhig"), ("ins2", "froh")], erst="cut"),
    ns("Mats", MX, G0, "erg", BLAU),
])

# ===========================================================================================================================
# K Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Anspruch aus § 888 Abs. 1 BGB"), ("tipp2", "Klausurtipp · inzident prüfen"),
       ("tipp3", "Klausurtipp · Akzessorietät")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Prüfung im Anspruch aus § 888 Abs. 1 BGB:", 200, 200, beim("tipp", "Anspruch"), "Bold", 35),
    z("Mats gegen Frau Ostendorf auf Zustimmung", 200, 255, beim("tipp", "Mats"), "Bold", 34),
    z("inzident:", 245, 335, "tipp2", "ExtraBold", 34),
    *pkt("1. wirksame Vormerkung", 385, beim("tipp2", "wirksame"), "Bold", 33, x=285),
    *pkt("2. vormerkungswidrige Verfügung", 435, beim("tipp2", "vormerkungswidrige"), "Bold", 33, x=285),
    *pkt("3. Frau Ostendorf als Erwerberin", 485, beim("tipp2", "Frau"), "Bold", 33, x=285),
    linienzug([(130, 560), (1130, 560)], "tipp3", breite=3),
    *pkt("Akzessorietät: Frau Ostendorf kann alles", 585, "tipp3", "Bold", 33, x=245),
    z("einwenden, was gegen den gesicherten", 245, 632, beim("tipp3", "einwenden"), "Regular", 33),
    z("Anspruch spricht", 245, 679, beim("tipp3", "einwenden"), "Regular", 33),
    zit("BGH, Urt. v. 2.7.2010 – V ZR 240/09, Rn. 8", 245, 735, beim("tipp3", "einwenden")),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# L Klausurschema
# ===========================================================================================================================
REIHEN = [("k1", 0, "I. Wirksame Vormerkung"),
          ("k1a", 1, "1. gesicherter Anspruch"),
          ("k1b", 1, "2. Bewilligung oder einstweilige Verfügung"),
          ("k1c", 1, "3. Eintragung"),
          ("k1d", 1, "4. Berechtigung"),
          ("k2", 0, "II. Vormerkungswidrige Verfügung nach der Eintragung, § 883 Abs. 2 BGB"),
          ("k3", 0, "III. Anspruchsgegner: der Erwerber"),
          ("k4", 0, "Rechtsfolge: Zustimmung zur Eintragung")]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Schema: Anspruch aus § 888 Abs. 1 BGB"), 110, 90, "sch", 46)]
y = 230
for c, ebene, text in REIHEN:
    x = (130, 220)[ebene]
    cue = {"k1a": beim("k1", "gesicherter"), "k1b": beim("k1", "Bewilligung"), "k1c": beim("k1", "Eintragung"),
           "k1d": beim("k1", "Berechtigung")}.get(c, c)
    els_sch.append(z(text, x, y, cue, "ExtraBold" if ebene == 0 else "Regular", 44 if ebene == 0 else 40, rechts=1820))
    y += {0: 90, 1: 70}[ebene]
    if c == "k1d":
        y += 20
assert y <= 970, y
folie([("sch", "Klausurschema"), ("k1", "Klausurschema › I. Wirksame Vormerkung"),
       ("k2", "Klausurschema › II. Vormerkungswidrige Verfügung"), ("k3", "Klausurschema › III. Anspruchsgegner"),
       ("k4", "Klausurschema › Rechtsfolge")], els_sch)

# ===========================================================================================================================
# M Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Die Vormerkung ", 0), ("sichert den Käufer", "a")], [("bis zu seiner Eintragung.", 0)]], 750, 280, 42,
                "merke", {"a": beim("merke", "sichert")}),
    *markertext([[("Spätere Verfügungen sind ihm gegenüber", 0)], [("unwirksam,", "b"), (" soweit sie seinen Anspruch", 0)],
                 [("vereiteln oder beeinträchtigen.", 0)]], 750, 450, 42, "mk2", {"b": beim("mk2", "unwirksam")}),
    *markertext([[("Durchgesetzt wird das mit dem", 0)], [("Zustimmungsanspruch", "c"), (" aus § 888 BGB.", 0)]],
                750, 680, 42, "mk3", {"c": beim("mk3", "Zustimmungsanspruch")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
