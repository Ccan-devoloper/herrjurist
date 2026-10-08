"""Folge 283 · § 80a VwGO: Der Bagger rollt – Eilrechtsschutz des Nachbarn – Serienstandard Open Peeps (Katzenkönig).
Übungsfall: Frau Fehling (Haus mit Garten) wehrt sich gegen die Baugenehmigung ihres Nachbarn Herrn Brodbeck für ein
Mehrfamilienhaus mit 3 Geschossen; der Bagger rollt, ihr Widerspruch hat nach § 212a Abs. 1 BauGB keine aufschiebende Wirkung.
Szenen laut ../SZENENPLAN.md: A Garten und Bauplatz (Fall), B Sachverhalt, C 1. Warum stoppt der Widerspruch nichts?
(§ 212a Abs. 1 BauGB, § 80 Abs. 2 S. 1 Nr. 3 VwGO, Wortlautkarten), D 2. Statthaftigkeit (Doppelwirkung, § 80a Abs. 3,
Wortlautkarte), E § 80 Abs. 5 S. 1 (Wortlautkarte), Anordnung, § 123 Abs. 5, F § 80a Abs. 1 Nr. 2 (Wortlautkarte),
G 3. Zulässigkeit (Rechtsweg, Antragsbefugnis), H Rechtsbehelf eingelegt (Zeitstrahl), I 4. Begründetheit (Waage),
J Subsumtion (Schnitt mit Abstandsfläche), K Ergebnis im Garten, L Gegenfall (Abstandsfläche verletzt), M 5. umgekehrter
Fall (§ 80a Abs. 1 Nr. 1, Wortlautkarte), N Klausurtipp (Lexi), O Schema, P Merksatz (Lexi).
Handlungsgeräusche: Bagger fährt auf den Bauplatz (szene_283bagger_1), Baggerschaufel gräbt (szene_283graben_1); Herkunft
../geraeusche_herkunft.json. Namensschild jeder Figur, solange sie im Bild ist.
Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/bau als eigene Kopie aus Folge 277 (dort aus 274/200;
gemeinsame Dateien unverändert); neu: garten(), erdhaufen(), abstand_grafik(), karte_80a1().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut nach gesetze-im-internet.de (VwGO, BauGB), Abruf 08.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave
import datetime as _dt

bausteine.FIGORDNER = "op_283/"

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
TUERKIS = (127, 214, 208, 255)
ORANGE = (249, 166, 108, 255)
HOLZ = (214, 160, 110, 255)
BEIGE = (201, 166, 107, 255)
ROSE = (242, 167, 195, 255)
FELD1 = (246, 232, 170, 255)
FELD2 = (205, 232, 190, 255)
FELD3 = (176, 218, 160, 255)
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
    e = pille(glyphen(text), *a, **k)
    return e


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
        if n.startswith(("bild:", "ficon:")) or "/op_283/" in n:
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


def wortlaut(x, y, w, text, quelle, cue, marken=(), size=30, bis=None):
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 08.10.2026), als Zitat mit Normangabe; der
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 168/180/200) -------------------------------------
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
    """Namensschild unter der Figur (ab ihrem ersten Auftritt, solange sie im Bild ist); lange Schilder in 26 px."""
    return pl(text, cx, unten + 22, cue, fill=fill, size=26 if len(text) > 14 else 30, anker="m", **k)


def okz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Haken davor (zur gesprochenen Bejahung)."""
    return [bis_(ok(x - 45, y + 20, cue, gr=gr), k.get("bis")), z(text, x, y, cue, stil, size, **k)]


def neinz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Kreuz davor (zur gesprochenen Verneinung)."""
    return [bis_(nein(x - 45, y + 20, cue, gr=gr), k.get("bis")), z(text, x, y, cue, stil, size, **k)]


# --- eigene Szenenbausteine (programmatisch, Palettenflächen, Tuschekontur) ---------------------------------------------------
BODEN_Y = 905                                # Boden = Unterkante der Figuren in den Fallszenen
FHA = 480                                    # Figurenhöhe in den Fallszenen
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
WAND = (232, 240, 238, 255)
WAND2 = (242, 232, 214, 255)
GRAUW = (205, 205, 200, 255)


def _flaeche(w, h, zeichne):
    s = 2
    im = Image.new("RGBA", (w * s, h * s))
    zeichne(ImageDraw.Draw(im), s)
    return im.resize((w, h), Image.LANCZOS)


def boden(c, x0=60, x1=1860):
    return hart(linienzug([(x0, BODEN_Y), (x1, BODEN_Y)], c, breite=7, farbe=INK))




def schreibtisch(c, x0, x1, h=170):
    w = x1 - x0
    def zz(dr, s):
        dr.rounded_rectangle((3 * s, 0, (w - 3) * s, 28 * s), 6 * s, fill=HOLZ, outline=INK, width=5 * s)
        for xl in (30, w - 60):
            dr.rectangle((xl * s, 28 * s, (xl + 26) * s, (h - 3) * s), fill=HOLZ, outline=INK, width=4 * s)
    return hart(El(_flaeche(w, h, zz), x0, BODEN_Y - h, c, "cut", 0.0, None, name="schreibtisch"))


def fenster(c, x0, y0, w=300, h=260):
    def zz(dr, s):
        dr.rounded_rectangle((3 * s, 3 * s, (w - 3) * s, (h - 3) * s), 10 * s, fill=(214, 232, 250, 255), outline=INK, width=5 * s)
        dr.line((w // 2 * s, 3 * s, w // 2 * s, (h - 3) * s), fill=INK, width=4 * s)
        dr.line((3 * s, h // 2 * s, (w - 3) * s, h // 2 * s), fill=INK, width=4 * s)
    return hart(El(_flaeche(w, h, zz), x0, y0, c, "cut", 0.0, None, name="fenster"))


X1, X2 = 1395, 1730                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"BR": "Herr Brodbeck", "FE": "Frau Fehling"}
NFARBE = {"BR": BLAU, "FE": ORANGE}


def stehend(k, x, folge, unten=930, hoehe=480, bis=None):
    return [*fig(k, x, unten, hoehe, folge, bis=bis), ns(NAME[k], x, unten, folge[0][0], NFARBE[k], d=0.1, bis=bis)]


def requisit(folge, px=PX):
    """Wechselndes Requisit über den Figuren: folge = [(cue, (set, icon, breite, fuell), pillentext, pillenfarbe)];
    ein Eintrag (cue, None, None, None) beendet das vorige Requisit (z. B. vor einer Sprechblase)."""
    els = []
    for i, (c, ic, txt, pf) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else None
        if ic:
            s_, n_, br, fu = ic
            els.append(ficon(s_, n_, px, PU, br, c, fuell=fu, bis=b))
        if txt:
            els.append(pl(txt, px, PY, c, fill=pf, size=28, anker="m", bis=b))
    return els


def zwei(folge_l, folge_r, links="BR", rechts="FE"):
    """Zwei Figuren rechts neben der Tafel (blicken nach links zur Tafel)."""
    return [*stehend(links, X1, folge_l), *stehend(rechts, X2, folge_r)]


def allein(k, folge):
    return stehend(k, FX, folge)




import math

def tabelle(x, y, spalten, zeilen, size=32, kopf_fill=GELB, zh=78):
    """Tabelle als einzelne Zeilenbilder: zeilen = [(cue, [zelle, …])]; die erste Zeile ist der Kopf (fett, farbig)."""
    els = []
    for zi, (cue, zellen) in enumerate(zeilen):
        w = sum(spalten)
        im = Image.new("RGBA", (w + 4, zh + 4))
        d = ImageDraw.Draw(im)
        xx = 2
        for si, (bw, txt) in enumerate(zip(spalten, zellen)):
            fill = kopf_fill if zi == 0 else (HELL if si == 0 else WEISS)
            d.rectangle((xx, 2, xx + bw, zh + 2), fill=fill, outline=INK, width=4)
            stil = "ExtraBold" if zi == 0 or si == 0 else "Bold"
            fnt = F(stil, size)
            assert fnt.getlength(glyphen(txt)) <= bw - 24, f"Tabellenzelle zu breit: {txt}"
            d.text((xx + 14, zh / 2 + 2), txt, font=fnt, fill=INK, anchor="lm")
            xx += bw
        els.append(El(im, x, y + zi * zh, cue, "rise", 0.0, None, name="tabelle:" + "|".join(zellen)))
    return els, y + len(zeilen) * zh



# --- eigene Szenenbausteine (aus Folge 277) ----------------------------------------------------------------------------------------
HAUSFARBEN = [(246, 232, 170, 255), (242, 214, 196, 255), (214, 232, 250, 255), (226, 240, 214, 255)]
ALTGRAU = (214, 214, 210, 255)
BLOCKF = (253, 226, 160, 255)
NEUF = (205, 232, 190, 255)
FHA = 440                                      # Figurenhöhe in der Fallszene
GH = 34                                        # Geschosshöhe in den Diagrammen


def ti(*a, **k):
    """Icon als Teil einer Tafelgrafik – darf links in der Tafel stehen (nicht unter rechts_frei)."""
    e = ficon(*a, **k)
    e.name = "tafelgrafik:" + e.name
    return e


def _strich(dr, p0, p1, s, w=4, lang=14, luecke=10):
    """gestrichelte Linie (Skalierung s)."""
    (x0, y0), (x1, y1) = p0, p1
    d = math.hypot(x1 - x0, y1 - y0); n = max(1, int(d / (lang + luecke)))
    for i in range(n + 1):
        a = i * (lang + luecke) / d; b = min(1.0, (i * (lang + luecke) + lang) / d)
        if a >= 1:
            break
        dr.line(((x0 + (x1 - x0) * a) * s, (y0 + (y1 - y0) * a) * s, (x0 + (x1 - x0) * b) * s, (y0 + (y1 - y0) * b) * s),
                fill=INK, width=w * s)


def bau(cx, unten, gesch, breite, fill, cue, dach=True, gestrichelt=False, anim="pop", bis=None, d=0.0, gh=None):
    """Gebäude als Geschossdiagramm (Tafelgrafik): gesch Geschosse à GH px, Fenster je Geschoss, Satteldach oder Flachdach;
    gestrichelt = nur gedachter Umriss (Vorbildwirkung)."""
    GH = gh or globals()["GH"]
    dachh = int(breite * 0.34) if dach else 10
    w, h = breite + 8, gesch * GH + dachh + 8

    def zz(dr, s):
        x0, x1, yb, yt = 4, breite + 4, h - 4, h - 4 - gesch * GH
        if gestrichelt:
            for p, q in [((x0, yb), (x0, yt)), ((x1, yb), (x1, yt)), ((x0, yt), (x1, yt))]:
                _strich(dr, p, q, s, w=(4 if GH < 50 else 6))
            return
        dr.rectangle((x0 * s, yt * s, x1 * s, yb * s), fill=fill, outline=INK, width=(4 if GH < 50 else 7) * s)
        if dach:
            dr.polygon([(x0 * s - 6 * s, yt * s), ((x0 + x1) / 2 * s, (yt - dachh + 6) * s), (x1 * s + 6 * s, yt * s)],
                       fill=(240, 122, 106, 255), outline=INK)
            dr.line([(x0 * s - 6 * s, yt * s), ((x0 + x1) / 2 * s, (yt - dachh + 6) * s), (x1 * s + 6 * s, yt * s)], fill=INK,
                    width=4 * s)
        else:
            dr.rectangle((x0 * s - 4 * s, (yt - (8 if GH < 50 else 12)) * s, x1 * s + 4 * s, yt * s), fill=INK)
        nf = max(1, int(breite / 40))
        for g in range(gesch):
            fg = 16 if GH < 50 else 28
            y0 = yb - (g + 1) * GH + (GH - fg) / 2
            for k in range(nf):
                fx = x0 + (breite / nf) * (k + 0.5) - fg / 2
                dr.rectangle((fx * s, y0 * s, (fx + fg) * s, (y0 + fg) * s), fill=(214, 232, 250, 255), outline=INK,
                             width=(3 if GH < 50 else 4) * s)

    im = _flaeche(w + 12, h + 4, lambda dr, s: zz(dr, s))
    return El(im, cx - (w + 12) / 2, unten - (h + 4), cue, anim, d, bis, name=f"tafelgrafik:bau{gesch}")


def gestrichelt_linie(x0, y, x1, cue, bis=None, d=0.0):
    im = _flaeche(int(x1 - x0) + 8, 12, lambda dr, s: _strich(dr, (4, 6), (x1 - x0 + 4, 6), s, w=4))
    return El(im, x0 - 4, y - 6, cue, "fade", d, bis, name="tafelgrafik:linie")




# --- eigene Szenenbausteine Folge 283 ----------------------------------------------------------------------------------------
ERDE = (176, 132, 92, 255)
BX, BRX, ZX, BAUMX, FEX, FHX = 420, 700, 900, 1060, 1290, 1640   # Fallszene von links nach rechts: Bauplatz, Herr Brodbeck,
SONNE = (175, 300)                                                 # Zaun (Grenze), Garten, Frau Fehling, ihr Haus; Abendsonne


def erdhaufen(cx, unten, w, h, cue, bis=None, anim="pop"):
    def zz(dr, s):
        dr.pieslice((4 * s, 4 * s, (w - 4) * s, (2 * h - 4) * s), 180, 360, fill=ERDE, outline=INK, width=5 * s)
    return El(_flaeche(w, h + 4, zz), cx - w / 2, unten - h, cue, anim, 0.0, bis, name="erdhaufen")


def garten(c, mit_umriss=True):
    """Grundbild der Fallszene: Boden, Abendsonne links, Bauplatz von Herrn Brodbeck, Zaun an der Grenze, Garten und Haus
    von Frau Fehling (Tabler sunset-2, fence, trees, home-2)."""
    els = [boden(c),
           hart(ficon("tabler", "sunset-2", SONNE[0], SONNE[1], 150, c, fuell=GELB, anim="cut")),
           hart(ficon("tabler", "fence", ZX, BODEN_Y, 120, c, fuell=WEISS, anim="cut")),
           hart(ficon("tabler", "trees", BAUMX, BODEN_Y, 170, c, fuell=GRUEN, anim="cut")),
           hart(ficon("tabler", "home-2", FHX, BODEN_Y, 250, c, fuell=HAUSFARBEN[1], anim="cut"))]
    return els


def abstand_grafik(c, x_haus, x_grenze, y_boden, verletzt=False, d=0.0):
    """Schnitt als Tafelgrafik: Haus von Herrn Brodbeck (3 Geschosse), Grenze gestrichelt, Abstandsfläche schraffiert
    vor der Außenwand; bei verletzt=True reicht sie über die Grenze auf das Grundstück von Frau Fehling."""
    els = [hart(El(_flaeche(1040, 8, lambda dr, s: dr.rectangle((0, 0, 1040 * s, 8 * s), fill=INK)), 110, y_boden, c,
                   "cut", 0.0, None, name="tafelgrafik:boden"))]
    els.append(hart(bau(x_haus, y_boden, 3, 170, BLOCKF, c, dach=False, anim="cut", gh=52)))
    wand = x_haus + 85 + 6
    tiefe = 210 if verletzt else 150
    def zz(dr, s):
        w_ = tiefe
        dr.rectangle((0, 0, w_ * s, 34 * s), fill=(HELLROT if verletzt else HELLGRUEN), outline=INK, width=3 * s)
        for k in range(0, w_ + 34, 18):
            dr.line(((k) * s, 34 * s, (k - 34) * s, 0), fill=(DROT if verletzt else DGRUEN), width=3 * s)
    els.append(hart(El(_flaeche(tiefe + 4, 38, zz), wand, y_boden - 38, c, "cut", 0.0, None, name="tafelgrafik:abstandsflaeche")))
    def gz(dr, s):
        _strich(dr, (4, 4), (4, 210), s, w=5)
    els.append(hart(El(_flaeche(10, 214, gz), x_grenze - 5, y_boden - 210, c, "cut", 0.0, None, name="tafelgrafik:grenze")))
    els.append(hart(pl("Grenze", x_grenze + 75, y_boden - 185, c, fill=WEISS, size=26, anker="m")))
    els.append(hart(ti("tabler", "trees", x_grenze + 180, y_boden, 120, c, fuell=GRUEN, anim="cut")))
    els.append(hart(ti("tabler", "home-2", x_grenze + 400, y_boden, 150, c, fuell=HAUSFARBEN[1], anim="cut")))
    els.append(hart(ti("tabler", "sunset-2", 165, y_boden - 120, 90, c, fuell=GELB, anim="cut")))
    els.append(hart(pl("Herr Brodbeck", x_haus, y_boden - 240, c, fill=BLAU, size=26, anker="m")))
    els.append(hart(pl("Frau Fehling", x_grenze + 400, y_boden - 200, c, fill=ORANGE, size=26, anker="m")))
    return els, wand, tiefe


NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig

# ===========================================================================================================================
# A Fall: Haus mit Garten, Baugenehmigung nebenan, der Bagger rollt, zwei Stimmen, Widerspruch, Fragen
# ===========================================================================================================================
folie([(NULL, "Fall · Frau Fehling: ein Haus mit Garten"), ("gen", "Fall · Baugenehmigung für Herrn Brodbeck"),
       ("bagger", "Fall · Der Bagger rollt"), ("fe1", "Fall · Frau Fehling: die Abendsonne"),
       ("br1", "Fall · Herr Brodbeck: alles genehmigt"), ("wid", "Fall · Frau Fehling legt Widerspruch ein"),
       ("weiter", "Fall · Der Bagger gräbt weiter"), ("frage", "Fall · Warum stoppt der Widerspruch nichts?")], [
    *garten(NULL),
    hart(pl("Haus mit Garten", FHX, 560, NULL, fill=HAUSFARBEN[1], size=30, anker="m")),
    *fig("FE", FEX, BODEN_Y, FHA, [(NULL, "ruhig"), ("gen", "denkt"), ("bagger", "sorge")], erst="cut", bis="fe1"),
    hart(ns(NAME["FE"], FEX, BODEN_Y, NULL, NFARBE["FE"])),
    bau(BX, BODEN_Y, 3, 260, WEISS, beim("gen", "Mehrfamilienhaus"), dach=False, gestrichelt=True, gh=95),
    pl("genehmigt: 3 Geschosse · 6 Wohnungen", 330, 520, beim("gen", "drei"), fill=GELB, size=28, anker="m", bis="wid"),
    *fig("BR", BRX, BODEN_Y, FHA, [(beim("gen", "Herr"), "froh"), ("bagger", "ruhig")], erst="pop", bis="br1"),
    ns(NAME["BR"], BRX, BODEN_Y, beim("gen", "Herr"), NFARBE["BR"], d=0.1),
    ficon("tabler", "file-certificate", BRX, 400, 90, beim("gen", "Baugenehmigung"), fuell=GELB, bis="bagger"),
    pl("Baugenehmigung", BRX, 265, beim("gen", "Baugenehmigung"), fill=GELB, size=28, anker="m", bis="bagger"),
    szene(bewegt(ficon("tabler", "backhoe", BX, BODEN_Y + 2, 230, beim("bagger", "rollt"), fuell=GELB, bis="weiter"),
                 beim("bagger", "rollt"), beim("bagger", "Bagger", ende=True), -260), "283bagger*", 0.8, 0.0),
    # Frau Fehling: Abendsonne
    *redet("FE_redet", FEX, BODEN_Y, FHA, "fe1", "br1"),
    blase("sprech", 900, 230, "fe1", 1290, 235, inhalt=["Das Haus nimmt meinem Garten die Abendsonne.",
                                                        "Dagegen wehre ich mich."],
          textsize=32, bis="br1", figur=("FE_redet", FEX, BODEN_Y, FHA)),
    pl("Abendsonne", SONNE[0], 340, beim("fe1", "Abendsonne"), fill=GELB, size=28, anker="m"),
    ring(BAUMX, 790, 150, 140, beim("fe1", "Garten"), farbe=ORANGE, breite=7, bis="br1"),
    *fig("FE", FEX, BODEN_Y, FHA, [("br1", "ernst"), ("wid", "ernst"), ("weiter", "sorge"), ("frage2", "denkt")], erst="cut"),
    # Herr Brodbeck: genehmigt, Wohnungen gebraucht
    *redet("BR_redet_r", BRX, BODEN_Y, FHA, "br1", "wid"),
    blase("sprech", 900, 230, "br1", 760, 235, inhalt=["Ich habe alles genehmigen lassen.",
                                                       "Und die Wohnungen werden gebraucht."],
          textsize=32, bis="wid", figur=("BR_redet_r", BRX, BODEN_Y, FHA)),
    *fig("BR", BRX, BODEN_Y, FHA, [("wid", "ruhig_r"), ("weiter", "ruhig"), ("frage", "denkt")], erst="cut"),
    # Widerspruch, Bagger gräbt weiter, Fragen
    ficon("tabler", "mail", FEX, 420, 100, beim("wid", "Widerspruch"), fuell=WEISS, bis="frage"),
    pl("Widerspruch", FEX, 290, beim("wid", "Widerspruch"), fill=WEISS, size=30, anker="m", bis="frage"),
    pl("je nach Land: Widerspruch – sonst gleich Klage", 70, 30, beim("wid", "Je"), fill=BLAU, size=30, bis="frage"),
    szene(ficon("tabler", "backhoe", BX - 40, BODEN_Y + 2, 230, "weiter", fuell=GELB, anim="cut"), "283graben*", 0.7, 0.0),
    erdhaufen(BX + 150, BODEN_Y, 150, 60, beim("weiter", "gräbt")),
    pl("Warum stoppt ihr Widerspruch nichts?", 70, 30, "frage", fill=WEISS, size=32),
    pl("Wie kommt sie schnell zu einem Baustopp?", 70, 105, "frage2", fill=GELB, size=32),
])

# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_283(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=33, zeilenabstand=1.28)
        els += e; y += 16
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_283("sv", [
    "Frau Fehling wohnt in einem Haus mit Garten. Ihr Nachbar, Herr Brodbeck, erhält von der Bauaufsichtsbehörde die "
    "Baugenehmigung für ein Mehrfamilienhaus mit 3 Geschossen und 6 Wohnungen. Kurz darauf rollt der Bagger und hebt die "
    "Baugrube aus.",
    "Frau Fehling meint, das Haus nehme ihrem Garten die Abendsonne und verletze das Gebot der Rücksichtnahme. Sie legt "
    "fristgerecht Widerspruch ein; in ihrem Land ist dafür ein Vorverfahren vorgesehen. Herr Brodbeck baut weiter.",
    "Das Haus hält die Abstandsflächen der Landesbauordnung zum Grundstück von Frau Fehling ein. Weitere Verstöße rügt sie "
    "nicht.",
], "Wie kommt Frau Fehling schnell zu einem Baustopp – und hat sie Erfolg?")

# ===========================================================================================================================
# C 1. Warum stoppt der Widerspruch nichts? § 80 Abs. 1, § 212a Abs. 1 BauGB, § 80 Abs. 2 S. 1 Nr. 3 VwGO (Wortlaut)
# ===========================================================================================================================
P1 = "1. Warum stoppt der Widerspruch nichts?"
W212 = ("„(1) Widerspruch und Anfechtungsklage eines Dritten gegen die bauaufsichtliche Zulassung eines Vorhabens haben "
        "keine aufschiebende Wirkung.“")
W802 = ("„(2) Die aufschiebende Wirkung entfällt nur … 3. in anderen durch Bundesgesetz oder für Landesrecht durch "
        "Landesgesetz vorgeschriebenen Fällen, …“")
w212, w212_y = wortlaut(80, 280, 1100, W212, "§ 212a Abs. 1 BauGB", "w212", marken=[
    ("eines Dritten", beim("w212", "Dritten")), ("bauaufsichtliche Zulassung", beim("w212", "bauaufsichtliche")),
    ("keine aufschiebende", beim("w212", "keine"))], size=31)
w802, w802_y = wortlaut(80, w212_y + 30, 1100, W802, "§ 80 Abs. 2 S. 1 Nr. 3 VwGO", "w802", marken=[
    ("entfällt nur", beim("w802", "entfällt")), ("Bundesgesetz", beim("w802", "Bundesgesetz"))], size=31)
folie([("grund", f"{P1} · Grundsatz: § 80 Abs. 1 VwGO"), ("w212", f"{P1} › § 212a Abs. 1 BauGB"),
       ("w802", f"{P1} › § 80 Abs. 2 S. 1 Nr. 3 VwGO"), ("darf", f"{P1} › Herr Brodbeck darf vorerst bauen")], rechts_frei([
    *tafel("grund", P1, size=44),
    z("Grundsatz: Widerspruch und Anfechtungsklage haben", 110, 170, beim("grund", "Normalerweise"), "Bold", 32),
    z("aufschiebende Wirkung (§ 80 Abs. 1 S. 1 VwGO).", 110, 216, beim("grund", "Normalerweise"), "Bold", 32),
    *w212, *w802,
    *okz("Herr Brodbeck darf deshalb vorerst bauen.", w802_y + 30, "darf", "ExtraBold", 33, x=160),
    *requisit([("grund", ("tabler", "book", 100, WEISS), "VwGO", WEISS),
               ("w212", ("tabler", "backhoe", 130, GELB), "§ 212a BauGB", GELB),
               ("darf", ("tabler", "crane", 110, GELB), "darf vorerst bauen", GELB)]),
    *zwei([("grund", "ruhig"), ("darf", "froh")], [("grund", "denkt"), ("w212", "sorge"), ("darf", "ernst")]),
]))
assert w802_y + 90 <= 890, w802_y

# ===========================================================================================================================
# D 2. Statthaftigkeit: Verwaltungsakt mit Doppelwirkung, § 80a Abs. 3 VwGO (Wortlaut)
# ===========================================================================================================================
P2 = "2. Statthaftigkeit"
W80A3 = ("„(3) Das Gericht kann auf Antrag Maßnahmen nach den Absätzen 1 und 2 ändern oder aufheben oder solche Maßnahmen "
         "treffen. § 80 Abs. 5 bis 8 gilt entsprechend.“")
w80a, w80a_y = wortlaut(80, 470, 1100, W80A3, "§ 80a Abs. 3 VwGO", "w80a", marken=[
    ("auf Antrag", beim("w80a", "Antrag")), ("ändern oder aufheben", beim("w80a", "ändern")),
    ("§ 80 Abs. 5 bis 8", beim("w80a", "Paragraf"))], size=31)
folie([("statt", f"{P2} · Welcher Antrag?"), ("va", f"{P2} › Verwaltungsakt mit Doppelwirkung: § 80a VwGO"),
       ("w80a", f"{P2} › § 80a Abs. 3 VwGO")], rechts_frei([
    *tafel("statt", "2. Die Statthaftigkeit"),
    blk(470, 170, 320, 70, WEISS, "va", [("Bauaufsicht", "ExtraBold", 32, INK)]),
    pfeil(560, 245, 360, 320, "va", breite=8, kopf=24),
    pfeil(700, 245, 900, 320, "va", breite=8, kopf=24),
    z("Baugenehmigung", 520, 262, "va", "Bold", 26, farbe=TEXT),
    blk(110, 330, 470, 76, HELLGRUEN, beim("va", "begünstigt"), [("Herr Brodbeck: begünstigt", "ExtraBold", 31, INK)]),
    blk(680, 330, 470, 76, HELLROT, beim("va", "belastet"), [("Frau Fehling: belastet", "ExtraBold", 31, INK)]),
    z("Also: Fall des § 80a VwGO (§ 80 Abs. 1 S. 2: Doppelwirkung)", 110, 418, beim("va", "Für"), "Bold", 30),
    *w80a,
    zit("Antrag nach § 80a Abs. 3 S. 2 i. V. m. § 80 Abs. 5 S. 1 VwGO", 110, w80a_y + 14, beim("w80a", "Paragraf")),
    zit("BVerwG, Beschl. v. 19.12.2019 – 7 VR 7.19, Rn. 8", 110, w80a_y + 52, beim("w80a", "Paragraf")),
    *requisit([("statt", ("tabler", "file-text", 100, WEISS), "Eilantrag", WEISS),
               ("va", ("tabler", "file-certificate", 100, GELB), "Baugenehmigung", GELB),
               ("w80a", ("tabler", "scale", 110, WEISS), "Gericht", WEISS)]),
    *zwei([("statt", "ruhig"), ("va", "froh"), ("w80a", "ruhig")], [("statt", "denkt"), ("va", "ernst"), ("w80a", "denkt")]),
]))
assert w80a_y + 95 <= 890, w80a_y

# ===========================================================================================================================
# E 2. Statthaftigkeit: § 80 Abs. 5 S. 1 VwGO (Wortlaut), Anordnung, Abgrenzung § 123 Abs. 5
# ===========================================================================================================================
W805 = ("„(5) Auf Antrag kann das Gericht der Hauptsache die aufschiebende Wirkung in den Fällen des Absatzes 2 Satz 1 "
        "Nummer 1 bis 3a ganz oder teilweise anordnen, im Falle des Absatzes 2 Satz 1 Nummer 4 ganz oder teilweise "
        "wiederherstellen. …“")
w805, w805_y = wortlaut(80, 165, 1100, W805, "§ 80 Abs. 5 S. 1 VwGO", "w805", marken=[
    ("Nummer 1 bis 3a", beim("w805", "Nummern")), ("anordnen,", beim("w805", "an.")),
    ("Nummer 4", beim("w805", "Nummer", nr=2)), ("wiederherstellen.", beim("w805", "stellt"))], size=31)
folie([("w805", f"{P2} › § 80 Abs. 5 S. 1 VwGO"), ("anord", f"{P2} › Anordnung, nicht Wiederherstellung"),
       ("p123", f"{P2} › nicht § 123 VwGO (§ 123 Abs. 5)")], rechts_frei([
    *tafel("w805", "2. Anordnen oder wiederherstellen?"),
    *w805,
    blk(110, w805_y + 30, 1040, 76, GRUEN, "anord", [("Hier: Anordnung der aufschiebenden Wirkung", "ExtraBold", 33, INK)]),
    *okz("Sie entfällt kraft Gesetzes (§ 212a BauGB),", w805_y + 130, beim("anord", "kraft"), "Bold", 32, x=160),
    z("nicht durch eine Anordnung der Behörde (Nr. 4).", 160, w805_y + 176, beim("anord", "nicht"), "Bold", 32),
    *neinz("§ 123 VwGO tritt zurück (§ 123 Abs. 5 VwGO).", w805_y + 250, "p123", "Bold", 32, x=160),
    zit("Mehr dazu: Video „Einstweilige Anordnung, § 123 VwGO“", 160, w805_y + 300, beim("p123", "Mehr")),
    *requisit([("w805", ("tabler", "scale", 110, WEISS), "§ 80 Abs. 5", WEISS),
               ("anord", ("tabler", "backhoe", 130, GELB), "kraft Gesetzes", GELB),
               ("p123", ("tabler", "file-x", 100, HELLROT), "nicht § 123", HELLROT)]),
    *allein("FE", [("w805", "ruhig"), ("anord", "denkt"), ("p123", "ruhig")]),
]))
assert w805_y + 340 <= 890, w805_y

# ===========================================================================================================================
# F 2. Antrag bei der Behörde? § 80a Abs. 1 VwGO (Wortlaut), Nr. 2
# ===========================================================================================================================
W80A1 = ("„(1) Legt ein Dritter einen Rechtsbehelf gegen den an einen anderen gerichteten, diesen begünstigenden "
         "Verwaltungsakt ein, kann die Behörde 1. auf Antrag des Begünstigten nach § 80 Absatz 2 Satz 1 Nummer 4 die "
         "sofortige Vollziehung anordnen, 2. auf Antrag des Dritten nach § 80 Abs. 4 die Vollziehung aussetzen und "
         "einstweilige Maßnahmen zur Sicherung der Rechte des Dritten treffen.“")


def karte_80a1(cue, marken, y=165):
    return wortlaut(80, y, 1100, W80A1, "§ 80a Abs. 1 VwGO", cue, marken=marken, size=30)


w801, w801_y = karte_80a1("beh", [("2. auf Antrag des Dritten", beim("beh", "Behörde")),
                                  ("die Vollziehung aussetzen", beim("beh", "auszusetzen"))])
folie([("beh", f"{P2} › Antrag bei der Behörde? § 80a Abs. 1 Nr. 2 VwGO")], rechts_frei([
    *tafel("beh", "Erst zur Behörde? § 80a Abs. 1 Nr. 2"),
    *w801,
    *okz("möglich: Aussetzung bei der Behörde beantragen", w801_y + 30, beim("beh", "Behörde"), "Bold", 32, x=160),
    *neinz("Pflicht vor dem Gericht? Nach dem Wortlaut nein.", w801_y + 95, beim("beh", "Wortlaut"), "ExtraBold", 32, x=160),
    zit("§ 80a Abs. 3 S. 2 i. V. m. § 80 Abs. 6 S. 1 VwGO: Behördenantrag", 160, w801_y + 145, beim("beh", "Wortlaut")),
    zit("nur bei öffentlichen Abgaben und Kosten (§ 80 Abs. 2 S. 1 Nr. 1)", 160, w801_y + 183, beim("beh", "Wortlaut")),
    *requisit([("beh", ("tabler", "building-bank", 110, WEISS), "Bauaufsicht", WEISS)]),
    *allein("FE", [("beh", "denkt"), (beim("beh", "Wortlaut"), "ruhig")]),
]))
assert w801_y + 225 <= 890, w801_y

# ===========================================================================================================================
# G 3. Zulässigkeit: Rechtsweg, Antragsbefugnis analog § 42 Abs. 2 (Verweis Folge 113)
# ===========================================================================================================================
P3 = "3. Zulässigkeit"
folie([("zul", f"{P3} · die übrige Zulässigkeit"), ("weg", f"{P3} › Verwaltungsrechtsweg"),
       ("befugt", f"{P3} › Antragsbefugnis analog § 42 Abs. 2 VwGO"), ("rueck", f"{P3} › Antragsbefugnis: Rücksichtnahmegebot"),
       ("v113", f"{P3} › Drittschutz: Video „Nachbarklage“")], rechts_frei([
    *tafel("zul", "3. Die übrige Zulässigkeit"),
    *okz("Verwaltungsrechtsweg: offen (§ 40 Abs. 1 S. 1 VwGO)", 175, "weg", "Bold", 32, x=160),
    z("Antragsbefugnis analog § 42 Abs. 2 VwGO:", 110, 265, "befugt", "ExtraBold", 33),
    z("Sie muss die Verletzung einer Norm geltend machen,", 110, 315, beim("befugt", "Verletzung"), "Bold", 32),
    z("die auch sie schützt.", 110, 361, beim("befugt", "auch"), "Bold", 32),
    zit("vgl. BVerwG, Beschl. v. 19.12.2019 – 7 VR 7.19, Rn. 5", 110, 410, beim("befugt", "auch")),
    blk(110, 470, 1040, 76, GELB, "rueck", [("Hier: Gebot der Rücksichtnahme", "ExtraBold", 33, INK)]),
    *okz("schützt auch die Nachbarn", 575, beim("rueck", "schützt"), "Bold", 32, x=160),
    *okz("Verletzung möglich: antragsbefugt", 635, beim("rueck", "Verletzung"), "Bold", 32, x=160),
    zit("BVerwG 4 B 52.15, Rn. 9 („Gebot nachbarlicher Rücksichtnahme“)", 160, 684,
        beim("rueck", "Verletzung")),
    zit("Welche Normen Nachbarn schützen: Video „Baurechtliche Nachbarklage“", 110, 760, "v113"),
    *requisit([("zul", ("tabler", "file-text", 100, WEISS), "Zulässigkeit", WEISS),
               ("weg", ("tabler", "building-bank", 110, WEISS), "Verwaltungsgericht", WEISS),
               ("befugt", ("tabler", "shield", 100, GRUEN), "Drittschutz", GRUEN),
               ("rueck", ("tabler", "sunset-2", 120, GELB), "Abendsonne", GELB)]),
    *allein("FE", [("zul", "ruhig"), ("befugt", "denkt"), ("rueck", "froh")]),
]))

# ===========================================================================================================================
# H 3. Rechtsbehelf eingelegt (OVG NRW 8 B 1108/15 Rn. 15; 7 B 334/26 Rn. 3–5), § 80 Abs. 5 S. 2 VwGO
# ===========================================================================================================================
TY = 330                                       # Zeitstrahl
folie([("rbh", f"{P3} › Rechtsbehelf eingelegt?"), ("frist", f"{P3} › ohne Rechtsbehelf, Frist verstrichen: unzulässig"),
       ("vor", f"{P3} › Widerspruch eingelegt; schon vor der Klage (§ 80 Abs. 5 S. 2)")], rechts_frei([
    *tafel("rbh", "3. Ist ein Rechtsbehelf eingelegt?"),
    hart(El(_flaeche(900, 8, lambda dr, s: dr.rectangle((0, 0, 900 * s, 8 * s), fill=INK)), 190, TY, "rbh", "cut", 0.0, None,
            name="tafelgrafik:zeitstrahl")),
    ti("tabler", "file-certificate", 260, TY - 12, 80, "rbh", fuell=GELB),
    pl("Baugenehmigung", 260, TY + 26, "rbh", fill=GELB, size=26, anker="m"),
    ti("tabler", "mail", 640, TY - 12, 80, "vor", fuell=WEISS),
    pl("Widerspruch", 640, TY + 26, "vor", fill=WEISS, size=26, anker="m"),
    bis_(ok(700, TY - 80, "vor", gr=20), None),
    ti("tabler", "scale", 1020, TY - 12, 80, beim("vor", "Antrag"), fuell=WEISS),
    pl("Eilantrag", 1020, TY + 26, beim("vor", "Antrag"), fill=WEISS, size=26, anker="m"),
    z("Ohne Rechtsbehelf keine aufschiebende Wirkung,", 110, 430, "rbh", "Bold", 32),
    z("die das Gericht anordnen könnte.", 110, 476, beim("rbh", "Sonst"), "Bold", 32),
    zit("vgl. OVG NRW, Beschl. v. 18.12.2015 – 8 B 1108/15, Rn. 15", 110, 524, beim("rbh", "Sonst")),
    *neinz("kein Rechtsbehelf, Frist verstrichen: Eilantrag scheitert", 580, "frist", "Bold", 32, x=160),
    zit("OVG NRW, Beschl. v. 16.6.2026 – 7 B 334/26, Rn. 3–5", 160, 628, beim("frist", "scheitert")),
    *okz("Frau Fehling hat Widerspruch eingelegt.", 690, "vor", "Bold", 32, x=160),
    *okz("Antrag schon vor der Klage zulässig (§ 80 Abs. 5 S. 2 VwGO)", 750, beim("vor", "Antrag"), "Bold", 31, x=160),
    *requisit([("rbh", ("tabler", "mail", 100, WEISS), "Rechtsbehelf", WEISS),
               ("frist", ("tabler", "hourglass", 100, WEISS), "Frist", WEISS),
               ("vor", ("tabler", "mail-opened", 100, GRUEN), "Widerspruch eingelegt", GRUEN)]),
    *allein("FE", [("rbh", "denkt"), ("frist", "ernst"), ("vor", "froh")]),
]))

# ===========================================================================================================================
# I 4. Begründetheit: Interessenabwägung (BVerwG 7 VR 7.19 Rn. 8), Wertung des § 212a (OVG NRW 7 B 359/25 Rn. 12)
# ===========================================================================================================================
P4 = "4. Begründetheit"
folie([("begr", f"{P4} · Interessenabwägung"), ("abw", f"{P4} › eigene Abwägung des Gerichts"),
       ("eaus", f"{P4} › Erfolgsaussichten in der Hauptsache, summarisch"), ("folg", f"{P4} › sonst: Folgenabwägung"),
       ("wert", f"{P4} › Wertung des § 212a BauGB")], rechts_frei([
    *tafel("begr", "4. Die Begründetheit"),
    ti("tabler", "scale", 630, 400, 190, "abw", fuell=WEISS),
    blk(110, 220, 430, 112, HELLROT, beim("abw", "Interesse"), [("Frau Fehling:", "ExtraBold", 30, INK),
                                                               ("Arbeiten ruhen lassen", "Bold", 30, INK)]),
    blk(720, 220, 430, 112, HELLGRUEN, beim("abw", "Herrn"), [("Herr Brodbeck:", "ExtraBold", 30, INK),
                                                              ("bauen", "Bold", 30, INK)]),
    z("Aussetzungsinteresse", 140, 345, beim("abw", "Interesse"), "Bold", 26, farbe=TEXT),
    z("Vollzugsinteresse", 760, 345, beim("abw", "Herrn"), "Bold", 26, farbe=TEXT),
    z("Das Gericht wägt selbst ab.", 110, 430, "abw", "ExtraBold", 33),
    blk(110, 495, 1040, 76, GELB, "eaus", [("wesentlich: Erfolgsaussichten, nur summarisch", "ExtraBold", 32, INK)]),
    z("nicht beurteilbar: Abwägung der Folgen", 110, 600, "folg", "Bold", 32),
    zit("BVerwG, Beschl. v. 19.12.2019 – 7 VR 7.19, Rn. 8", 110, 648, "folg"),
    blk(110, 700, 1040, 76, BLAU, "wert", [("Wertung des § 212a: während des Prozesses vollziehbar", "ExtraBold", 30, INK)]),
    zit("OVG NRW, Beschl. v. 29.12.2025 – 7 B 359/25, Rn. 12 („Vorrang der Vollziehbarkeit“)", 110, 790,
        beim("wert", "Genehmigung")),
    *requisit([("begr", ("tabler", "scale", 110, WEISS), "Abwägung", WEISS),
               ("eaus", ("tabler", "search", 100, WEISS), "summarisch", WEISS),
               ("wert", ("tabler", "backhoe", 130, GELB), "§ 212a BauGB", GELB)]),
    *zwei([("begr", "ruhig"), ("wert", "zuversicht")], [("begr", "ruhig"), ("eaus", "denkt"), ("wert", "sorge")]),
]))

# ===========================================================================================================================
# J 4. Subsumtion: Abstandsflächen eingehalten, Rücksichtnahme (BVerwG 4 B 52.15 Rn. 9), Ergebnis (10 B 645/23 Rn. 3, 90)
# ===========================================================================================================================
PS4 = "4. Begründetheit › Rechte von Frau Fehling verletzt?"
ag, wand, tiefe = abstand_grafik("nur", 330, 650, 430)
folie([("nur", f"{PS4}"), ("abst", "4. Begründetheit › Abstandsflächen eingehalten"),
       ("sonne", "4. Begründetheit › Sonne: Abstandsflächen konkretisieren die Rücksichtnahme"),
       ("nicht", "4. Begründetheit › voraussichtlich keine Rechtsverletzung"),
       ("vollz", "4. Begründetheit › Interesse des Bauherrn überwiegt (§ 212a)"),
       ("abgel", "Ergebnis · Der Antrag wird abgelehnt")], rechts_frei([
    *tafel("nur", "Verletzt die Genehmigung ihre Rechte?", size=44),
    *ag,
    pl("Abstandsfläche auf dem eigenen Grundstück", wand + tiefe / 2 + 60, 448, beim("abst", "Abstandsflächen"),
       fill=HELLGRUEN, size=26, anker="m"),
    bis_(ok(wand + tiefe / 2, 355, beim("abst", "Abstandsflächen"), gr=18), None),
    *okz("Abstandsflächen der Landesbauordnung eingehalten", 510, beim("abst", "Abstandsflächen"), "Bold", 31, x=160),
    z("Sonne und Einblick: Das Abstandsflächenrecht konkretisiert", 110, 566, "sonne", "Bold", 31),
    z("die Rücksichtnahme. Mehr grundsätzlich nicht.", 110, 610, beim("sonne", "Mehr"), "Bold", 31),
    zit("BVerwG, Beschl. v. 15.6.2016 – 4 B 52.15, Rn. 9", 110, 654, beim("sonne", "Mehr")),
    *neinz("voraussichtlich keine Verletzung ihrer Rechte", 700, "nicht", "ExtraBold", 32, x=160),
    blk(110, 758, 1040, 66, HELLGRUEN, "vollz", [("Interesse des Bauherrn überwiegt (Wertung § 212a)", "ExtraBold", 30, INK)]),
    zit("OVG NRW, Beschl. v. 15.12.2023 – 10 B 645/23, Rn. 3, 90", 110, 834, "vollz"),
    *requisit([("nur", ("tabler", "shield", 100, WEISS), "Drittschutz?", WEISS),
               ("abst", ("tabler", "ruler-measure", 110, HELLGRUEN), "Abstand eingehalten", HELLGRUEN),
               ("sonne", ("tabler", "sunset-2", 120, GELB), "Sonne", GELB),
               ("abgel", ("tabler", "file-x", 100, HELLROT), "Antrag abgelehnt", HELLROT)]),
    *zwei([("nur", "ruhig"), ("nicht", "froh")], [("nur", "denkt"), ("abst", "ruhig"), ("nicht", "ernst")]),
]))

# ===========================================================================================================================
# K Ergebnis im Garten: Frau Fehling, Herr Brodbeck (Blasen), eigenes Risiko (10 B 645/23 Rn. 90)
# ===========================================================================================================================
folie([("fe2", "Ergebnis · Frau Fehling: das Hauptverfahren"), ("br2", "Ergebnis · Herr Brodbeck baut wie genehmigt"),
       ("risiko", "Ergebnis · Bauen auf eigenes Risiko")], [
    *garten("fe2"),
    hart(pl("Eilantrag abgelehnt", 820, 30, "fe2", fill=PINK, size=32)),
    hart(bau(BX, BODEN_Y, 3, 260, WEISS, "fe2", dach=False, gestrichelt=True, gh=95, anim="cut")),
    hart(bau(BX, BODEN_Y, 1, 260, BLOCKF, "fe2", dach=False, gh=95, anim="cut")),
    *redet("FE_redet2", FEX, BODEN_Y, FHA, "fe2", "br2"),
    ns(NAME["FE"], FEX, BODEN_Y, "fe2", NFARBE["FE"]),
    blase("sprech", 820, 190, "fe2", 1290, 250, inhalt=["Dann warte ich auf das Hauptverfahren."], textsize=32, bis="br2",
          figur=("FE_redet2", FEX, BODEN_Y, FHA)),
    *fig("FE", FEX, BODEN_Y, FHA, [("br2", "ruhig"), ("risiko", "denkt")], erst="cut"),
    *fig("BR", BRX, BODEN_Y, FHA, [("fe2", "ruhig_r")], erst="cut", bis="br2"),
    ns(NAME["BR"], BRX, BODEN_Y, "fe2", NFARBE["BR"]),
    *redet("BR_redet2_r", BRX, BODEN_Y, FHA, "br2", "risiko"),
    blase("sprech", 940, 190, "br2", 760, 250, inhalt=["Und ich baue genau so, wie es genehmigt ist."], textsize=32,
          bis="risiko", figur=("BR_redet2_r", BRX, BODEN_Y, FHA)),
    *fig("BR", BRX, BODEN_Y, FHA, [("risiko", "ernst")], erst="cut"),
    pl("auf eigenes Risiko – bis die Hauptsache entschieden ist", 820, 105, beim("risiko", "eigenes"), fill=WEISS, size=30),
    pl("OVG NRW 10 B 645/23, Rn. 90", 820, 175, beim("risiko", "eigenes"), fill=HELL, size=26),
    hart(ficon("tabler", "backhoe", 160, BODEN_Y + 2, 230, "fe2", fuell=GELB, anim="cut")),
])

# ===========================================================================================================================
# L Gegenfall: Abstandsfläche verletzt → Anordnung trotz § 212a (OVG NRW 10 B 603/20 Rn. 16, Tenor)
# ===========================================================================================================================
ag2, wand2, tiefe2 = abstand_grafik("gegen", 470, 620, 430, verletzt=True)
folie([("gegen", "Gegenfall · Abstandsfläche zu ihr verletzt")], rechts_frei([
    *tafel("gegen", "Gegenfall: Abstandsfläche verletzt"),
    *ag2,
    pl("Abstandsfläche ragt auf ihr Grundstück", wand2 + 150, 448, beim("gegen", "Abstandsflächen"), fill=HELLROT, size=26,
       anker="m"),
    bis_(nein(wand2 + tiefe2 - 40, 355, beim("gegen", "Abstandsflächen"), gr=18), None),
    *okz("Aussetzungsinteresse überwiegt – trotz § 212a BauGB", 520, beim("gegen", "überwiegt"), "Bold", 31, x=160),
    blk(110, 590, 1040, 76, GRUEN, beim("gegen", "ordnet"), [("Das Gericht ordnet die aufschiebende Wirkung an.",
                                                              "ExtraBold", 32, INK)]),
    zit("OVG NRW, Beschl. v. 16.6.2020 – 10 B 603/20, Rn. 16 und Tenor", 110, 680, beim("gegen", "ordnet")),
    *requisit([("gegen", ("tabler", "ruler-measure", 110, HELLROT), "zu nah an der Grenze", HELLROT),
               (beim("gegen", "ordnet"), ("tabler", "barrier-block", 120, GELB), "Baustopp", GELB)]),
    *zwei([("gegen", "denkt"), (beim("gegen", "ordnet"), "ernst")], [("gegen", "ruhig"), (beim("gegen", "ordnet"), "froh")]),
]))

# ===========================================================================================================================
# M 5. Der umgekehrte Fall: § 80a Abs. 1 Nr. 1 VwGO (Wortlaut), Gericht über Abs. 3
# ===========================================================================================================================
P5 = "5. Der umgekehrte Fall"
w801b, w801b_y = karte_80a1("umg", [("auf Antrag des Begünstigten", beim("umg", "Begünstigte")),
                                    ("sofortige Vollziehung anordnen,", beim("umg", "sofortige"))], y=330)
folie([("umg", f"{P5} · § 80a Abs. 1 Nr. 1 VwGO"), ("umg2", f"{P5} › beim Gericht: § 80a Abs. 3 VwGO")], rechts_frei([
    *tafel("umg", "5. Der umgekehrte Fall: § 80a Abs. 1 Nr. 1"),
    z("Rechtsbehelf des Dritten hat aufschiebende Wirkung,", 110, 175, beim("umg", "Hat"), "Bold", 32),
    z("weil kein Gesetz wie § 212a BauGB sie ausschließt.", 110, 221, beim("umg", "weil"), "Bold", 32),
    blk(110, 268, 1040, 50, HELL, beim("umg", "Begünstigte"), [("Der Begünstigte beantragt bei der Behörde:", "Bold", 28, INK)],
        rand=3),
    *w801b,
    blk(110, w801b_y + 20, 1040, 76, BLAU, "umg2", [("beim Gericht: § 80a Abs. 3 S. 1 VwGO", "ExtraBold", 33, INK)]),
    *requisit([("umg", ("tabler", "mail", 100, WEISS), "Rechtsbehelf des Dritten", WEISS),
               (beim("umg", "Begünstigte"), ("tabler", "building-bank", 110, WEISS), "Behörde", WEISS),
               ("umg2", ("tabler", "scale", 110, WEISS), "Gericht", WEISS)]),
]))
assert w801b_y + 100 <= 890, w801b_y

# ===========================================================================================================================
# N Klausurtipp (Lexi): Grund des Entfallens benennen, Anordnung, nur drittschützende Normen
# ===========================================================================================================================
els_k = [*tafel("tipp", "Klausurtipp: Warum fehlt die Wirkung?", fill=HELL), warnung_i(150, 225, "tipp", gr=26),
         z("Zuerst den Grund benennen:", 200, 200, "tipp", "Bold", 34),
         blk(130, 280, 1020, 76, GELB, "k1", [("Baugenehmigung: § 212a Abs. 1 BauGB", "ExtraBold", 32, INK)]),
         blk(130, 380, 1020, 76, GRUEN, "k2", [("Also: Anordnung, nicht Wiederherstellung", "ExtraBold", 32, INK)]),
         blk(130, 480, 1020, 76, BLAU, "k3", [("Begründetheit: nur Normen, die auch ihn schützen", "ExtraBold", 31, INK)]),
         *neinz("„irgendwie rechtswidrig“ genügt nicht", 590, beim("k3", "Dass"), "Bold", 32, x=180),
         *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
         ns("Lexi", FX, FB, "tipp", GELB, d=0.2)]
folie([("tipp", "Klausurtipp · Grund des Entfallens benennen"), ("k1", "Klausurtipp › § 212a BauGB"),
       ("k2", "Klausurtipp › Anordnung, nicht Wiederherstellung"), ("k3", "Klausurtipp › nur drittschützende Normen")], els_k)

# ===========================================================================================================================
# O Schema (Aufbau Punkt für Punkt)
# ===========================================================================================================================
REIHEN = [("s1", 0, "A. Zulässigkeit"),
          ("s1a", 1, "I. Verwaltungsrechtsweg (§ 40 Abs. 1 S. 1 VwGO)"),
          ("s1b", 1, "II. Statthaftigkeit: § 80a Abs. 3 S. 2 i. V. m. § 80 Abs. 5 S. 1 VwGO – Anordnung"),
          ("s1c", 1, "III. Antragsbefugnis analog § 42 Abs. 2 VwGO (drittschützende Norm)"),
          ("s1d", 1, "IV. Rechtsbehelf eingelegt (§ 80 Abs. 5 S. 2 VwGO)"),
          ("s2", 0, "B. Begründetheit: Interessenabwägung"),
          ("s2a", 1, "I. Erfolgsaussichten, summarisch: Normen, die auch den Nachbarn schützen"),
          ("s2b", 1, "II. Wertung des § 212a Abs. 1 BauGB")]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Schema: Eilantrag des Nachbarn, § 80a VwGO"), 110, 90, "sch", 46)]
y = 225
for c, ebene, text in REIHEN:
    x = (130, 200)[ebene]
    els_sch.append(z(text, x, y, c, ("ExtraBold", "Regular")[ebene], (38, 34)[ebene], rechts=1820))
    y += {0: 90, 1: 76}[ebene]
assert y <= 960, y
folie([("sch", "Schema · Eilantrag des Nachbarn"), ("s1", "Schema › A. Zulässigkeit"), ("s1a", "Schema › A. I. Rechtsweg"),
       ("s1b", "Schema › A. II. Statthaftigkeit"), ("s1c", "Schema › A. III. Antragsbefugnis"),
       ("s1d", "Schema › A. IV. Rechtsbehelf eingelegt"), ("s2", "Schema › B. Begründetheit"),
       ("s2a", "Schema › B. I. Erfolgsaussichten"), ("s2b", "Schema › B. II. Wertung des § 212a")], els_sch)

# ===========================================================================================================================
# P Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Gegen die Baugenehmigung des Nachbarn", 0)], [("stoppen ", 0), ("Widerspruch und Klage nichts", "a"),
                  (".", 0)]], 750, 280, 40, "merke", {"a": beim("merke", "Widerspruch")}),
    *markertext([[("Verletzt die Genehmigung voraussichtlich eine Norm,", 0)],
                 [("die auch den Nachbarn schützt, ", 0), ("ordnet das Gericht", "b")],
                 [("die aufschiebende Wirkung", "c"), (" in der Regel an.", 0)]], 750, 430, 40, "m2",
                {"b": beim("m2", "ordnet"), "c": beim("m2", "aufschiebende")}),
    *markertext([[("Sonst setzt sich meist die ", 0), ("Wertung des Gesetzes", "d"), (" durch:", 0)],
                 [("Es wird gebaut.", 0)]], 750, 660, 40, "m3", {"d": beim("m3", "Wertung")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
