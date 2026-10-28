"""Folge 189 · Rechtfertigender Notstand § 34 StGB: Schema mit Berghütten-Fall – Serienstandard Open Peeps (Katzenkönig).
Beispielfall: Samstag, 17:40 Uhr, auf 2.150 m gerät Korbinian (Mitte 30) allein in einen Wettersturz (Schneesturm, −12 °C),
kein Netz, bis ins Tal 3 Stunden. Die Berghütte von Frau Moser ist im Winter verschlossen, ein Schild verbietet das Betreten.
Korbinian bricht die Tür auf (nur als Icon: Werkzeug, offene Tür, kaputtes Schloss; keine Anleitung), übersteht die Nacht.
Am Morgen: Frau Moser, neues Schloss 380 €. Keine Verletzungen; Wetter nur als ruhige Icons; Hütte ohne Logos.
Szenen laut ../SZENENPLAN.md: A1 Bergweg im Wettersturz, A2 an der Berghütte, A3 Nacht in der Hütte, A4 Morgen danach,
B Sachverhalt, C Tatbestand §§ 303, 123, D Wortlautkarte § 34, E 1. Notstandslage, F 2. Notstandshandlung,
G 3. Interessenabwägung, H 4. Angemessenheit, I 5. subjektives Element, J § 904 BGB (Wortlautkarte), K § 228 BGB
(Wortlautkarte), L Spezialität, M Abgrenzung §§ 32, 35, N1 Lösung, N2 Morgen an der Hütte, O Klausurtipp (Lexi),
P Klausurschema, Q Merksatz (Lexi).
Handlungsgeräusch: Tür knarrt auf (A2, szene_189tuer_1); ../geraeusche_herkunft.json.
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz
als eigene Kopie aus Folge 186 (gemeinsame Dateien unverändert); neu: berge(), schnee(), huette(), innen(), schild_189().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut nach gesetze-im-internet.de (Abruf 04.10.2026)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave
import datetime as _dt

bausteine.FIGORDNER = "op_189/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_189/" in n:
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
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 04.10.2026), als Zitat mit Normangabe; der
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 168/180) -------------------------------------
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
    return [ok(x - 45, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]


def neinz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Kreuz davor (zur gesprochenen Verneinung)."""
    return [nein(x - 45, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]




# --- eigene Szenenbausteine (programmatisch, Palettenflächen, Tuschekontur) ---------------------------------------------------
BODEN_Y = 905                                # Boden = Unterkante der Figuren in den Fallszenen
FHA = 480                                    # Figurenhöhe in den Fallszenen
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
FELS = (205, 214, 228, 255)
FELS2 = (186, 198, 218, 255)
HOLZ2 = (176, 118, 76, 255)
DUNKEL = (70, 58, 50, 255)
DACH = (150, 82, 70, 255)
INNENWAND = (238, 214, 180, 255)
HELLROT2 = (250, 196, 186, 255)


def _flaeche(w, h, zeichne):
    s = 2
    im = Image.new("RGBA", (w * s, h * s))
    zeichne(ImageDraw.Draw(im), s)
    return im.resize((w, h), Image.LANCZOS)


def berge(c, x0=60, w=1800, h=470):
    """Bergkulisse (Grundform): drei Gipfel mit Schneekappen, Tuschekontur; Himmel bleibt Cremegrund."""
    gipfel = [(0.00, 0.55, 0.30, 0.10, 0.62), (0.22, 0.75, 0.52, 0.00, 0.80), (0.55, 1.00, 0.80, 0.18, 0.66)]

    def zz(dr, s):
        for a, b, m, top, fuss in gipfel:
            pa, pb, pm = (a * w * s, h * s), (b * w * s, h * s), (m * w * s, top * h * s)
            dr.polygon([pa, pm, pb], fill=FELS if m != 0.52 else FELS2, outline=INK)
            dr.line([pa, pm, pb], fill=INK, width=5 * s, joint="curve")
            # Schneekappe: oberes Viertel des Gipfels
            k = 0.28
            l = (pm[0] + (pa[0] - pm[0]) * k, pm[1] + (pa[1] - pm[1]) * k)
            r = (pm[0] + (pb[0] - pm[0]) * k, pm[1] + (pb[1] - pm[1]) * k)
            mid1 = (l[0] + (pm[0] - l[0]) * 0.0 + (r[0] - l[0]) * 0.33, l[1] + 18 * s)
            mid2 = (l[0] + (r[0] - l[0]) * 0.66, r[1] + 10 * s)
            dr.polygon([pm, l, mid1, mid2, r], fill=(255, 255, 255, 255))
            dr.line([l, pm, r], fill=INK, width=5 * s, joint="curve")
            dr.line([l, mid1, mid2, r], fill=INK, width=4 * s, joint="curve")
    return hart(El(_flaeche(w, h, zz), x0, BODEN_Y - h, c, "cut", 0.0, None, name="berge"))


def schnee(c, x0=60, x1=1860):
    """Schneeboden: weiße Fläche unter der Bodenlinie mit leicht welliger Oberkante."""
    w, h = x1 - x0, 70

    def zz(dr, s):
        pts = [(0, 18 * s)]
        for i in range(0, w + 1, 60):
            pts.append((i * s, (10 + 10 * ((i // 60) % 2)) * s))
        pts += [(w * s, h * s), (0, h * s)]
        dr.polygon(pts, fill=(255, 255, 255, 255))
        dr.line(pts[:-2], fill=INK, width=6 * s, joint="curve")
    return hart(El(_flaeche(w, h, zz), x0, BODEN_Y - 14, c, "cut", 0.0, None, name="schnee"))


HX0, HW = 180, 640                           # Hütte: linke Kante, Breite
TUER = (HX0 + 250, HX0 + 390)                # Tür: x-Bereich
TUER_O = BODEN_Y - 250                       # Türoberkante


def huette(c, tuer="zu", fenster_licht=False, bis=None, morgen=False):
    """Berghütte (Holzwände, Satteldach mit Schnee, Fenster, Tür); tuer = 'zu' | 'offen'. Ohne Logo, ohne Namen."""
    w, h = HW, 560

    def zz(dr, s):
        wand_o = h - 330
        dr.rectangle((40 * s, wand_o * s, (w - 40) * s, (h - 3) * s), fill=HOLZ, outline=INK, width=5 * s)
        for yy in range(wand_o + 40, h - 10, 40):                 # Bretter
            dr.line((44 * s, yy * s, (w - 44) * s, yy * s), fill=(150, 100, 60, 255), width=2 * s)
        dach = [(10 * s, (wand_o + 8) * s), (w / 2 * s, 30 * s), ((w - 10) * s, (wand_o + 8) * s)]
        dr.polygon(dach, fill=DACH)
        dr.line(dach + [dach[0]], fill=INK, width=5 * s, joint="curve")
        # Schnee auf dem Dach
        sn = [(24 * s, (wand_o - 4) * s), (w / 2 * s, 46 * s), ((w - 24) * s, (wand_o - 4) * s),
              ((w - 60) * s, (wand_o - 36) * s), (w / 2 * s, 84 * s), (60 * s, (wand_o - 36) * s)]
        dr.polygon(sn, fill=(255, 255, 255, 255))
        dr.line(sn + [sn[0]], fill=INK, width=4 * s, joint="curve")
        # Fenster links
        fx0, fy0 = 90, wand_o + 70
        dr.rounded_rectangle((fx0 * s, fy0 * s, (fx0 + 120) * s, (fy0 + 110) * s), 8 * s,
                             fill=GELB if fenster_licht else (214, 232, 250, 255), outline=INK, width=5 * s)
        dr.line(((fx0 + 60) * s, fy0 * s, (fx0 + 60) * s, (fy0 + 110) * s), fill=INK, width=4 * s)
        dr.line((fx0 * s, (fy0 + 55) * s, (fx0 + 120) * s, (fy0 + 55) * s), fill=INK, width=4 * s)
        # Tür
        tx0, tx1 = TUER[0] - HX0, TUER[1] - HX0
        ty0 = h - 250
        if tuer == "zu":
            dr.rectangle((tx0 * s, ty0 * s, tx1 * s, (h - 3) * s), fill=HOLZ2, outline=INK, width=5 * s)
            dr.ellipse(((tx1 - 30) * s, (ty0 + 120) * s, (tx1 - 14) * s, (ty0 + 136) * s), fill=INK)
        else:
            dr.rectangle((tx0 * s, ty0 * s, tx1 * s, (h - 3) * s), fill=DUNKEL, outline=INK, width=5 * s)
            blatt = [(tx1 * s, ty0 * s), ((tx1 + 70) * s, (ty0 + 22) * s), ((tx1 + 70) * s, (h - 3 - 4) * s), (tx1 * s, (h - 3) * s)]
            dr.polygon(blatt, fill=HOLZ2)
            dr.line(blatt + [blatt[0]], fill=INK, width=5 * s, joint="curve")
    return hart(El(_flaeche(w, h, zz), HX0, BODEN_Y - h, c, "cut", 0.0, bis, name=f"huette:{tuer}"))


def schild_189(c, cx, bis=None):
    """Schild auf einem Holzpfosten neben der Hütte: „Betreten verboten“ (fiktiv, ohne Logo); steht auf dem Boden."""
    zeilen = [glyphen("Betreten"), glyphen("verboten")]
    f = F("ExtraBold", 30)
    w = int(max(f.getlength(t) for t in zeilen)) + 40
    h = 300

    def zz(dr, s):
        dr.rectangle(((w / 2 - 9) * s, 80 * s, (w / 2 + 9) * s, (h - 2) * s), fill=HOLZ2, outline=INK, width=4 * s)
        dr.rounded_rectangle((3 * s, 3 * s, (w - 3) * s, 100 * s), 8 * s, fill=(255, 255, 255, 255), outline=INK, width=5 * s)
        for i, t in enumerate(zeilen):
            dr.text((w / 2 * s, (30 + 42 * i) * s), t, font=F("ExtraBold", 30 * s), fill=(200, 50, 40, 255), anchor="mm")
    return El(_flaeche(w, h, zz), cx - w / 2, BODEN_Y - h + 4, c, "pop", 0.0, bis, name="schild:Betreten verboten")


def innen(c):
    """Innenraum der Hütte (Grundform): Holzwand, Fenster mit Schneeflocken, Bank; ohne Logo."""
    def zz(dr, s):
        dr.rectangle((0, 0, 1800 * s, 575 * s), fill=INNENWAND)
        for xx in range(0, 1800, 90):
            dr.line((xx * s, 0, xx * s, 575 * s), fill=(214, 182, 140, 255), width=3 * s)
        dr.rounded_rectangle((180 * s, 80 * s, 560 * s, 360 * s), 10 * s, fill=(70, 86, 130, 255), outline=INK, width=6 * s)
        dr.line((370 * s, 80 * s, 370 * s, 360 * s), fill=INK, width=5 * s)
        dr.line((180 * s, 220 * s, 560 * s, 220 * s), fill=INK, width=5 * s)
        # Bank
        dr.rounded_rectangle((760 * s, 400 * s, 1180 * s, 432 * s), 6 * s, fill=HOLZ2, outline=INK, width=5 * s)
        for xb in (790, 1120):
            dr.rectangle((xb * s, 432 * s, (xb + 26) * s, 573 * s), fill=HOLZ2, outline=INK, width=4 * s)
        dr.line((0, 575 * s - 2, 1800 * s, 575 * s - 2), fill=INK, width=4 * s)
    return hart(El(_flaeche(1800, 575, zz), 60, BODEN_Y - 575, c, "cut", 0.0, None, name="innen"))


def boden(c, x0=60, x1=1860):
    return hart(linienzug([(x0, BODEN_Y), (x1, BODEN_Y)], c, breite=7, farbe=INK))


X1, X2 = 1395, 1730                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"KO": "Korbinian", "MO": "Frau Moser"}
NFARBE = {"KO": HELLROT2, "MO": GRUEN}


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


def zwei(folge_l, folge_r, links="MO", rechts="KO"):
    """Zwei Figuren rechts neben der Tafel (blicken nach links zur Tafel)."""
    return [*stehend(links, X1, folge_l), *stehend(rechts, X2, folge_r)]


def allein(k, folge):
    return stehend(k, FX, folge)


def bis_l(els, bis):
    for e in els:
        e.bis = bis
    return els


def flocken(c, punkte, gr=56, bis=None):
    return [ficon("tabler", "snowflake", x, y, gr, c, fuell=WEISS, bis=bis) for x, y in punkte]


# ===========================================================================================================================
# A1 Fall: Bergweg im Wettersturz (Wetter nur als ruhige Icons)
# ===========================================================================================================================
KOX1 = 1300
FLOCKEN = [(640, 310), (860, 210), (1100, 260), (1480, 190), (1700, 270), (1820, 150), (1000, 120)]
folie([(NULL, "Fall · Bergtour auf 2.150 m"), ("sturz", "Fall · Wettersturz"), ("netz", "Fall · kein Netz, Tal 3 Stunden")], [
    berge(NULL),
    schnee(NULL),
    hart(pl("Samstag, 17:40 Uhr", 70, 30, NULL, fill=WEISS, size=38)),
    hart(pl("2.150 m", 520, 30, NULL, fill=BLAU, size=38)),
    *stehend("KO", KOX1, [("korb", "ruhig"), ("sturz", "sorge"), ("netz", "angst")], unten=BODEN_Y),
    pl("allein auf Bergtour", KOX1, 330, beim("korb", "allein"), fill=WEISS, size=30, anker="m", bis="sturz"),
    *flocken("sturz", FLOCKEN),
    ficon("tabler", "wind", 680, 560, 140, "sturz", fuell=WEISS),
    pl("Schneesturm · −12 °C", 70, 110, beim("sturz", "Schneesturm"), fill=WEISS, size=36),
    ficon("tabler", "device-mobile-off", 1030, 760, 110, "netz", fuell=WEISS),
    pl("kein Netz", 1030, 600, "netz", fill=HELLROT, size=30, anker="m"),
    pl("bis ins Tal: 3 Stunden", 70, 190, "tal", fill=GELB, size=36),
])

# ===========================================================================================================================
# A2 Fall: an der Berghütte – verschlossen, Schild, Korbinian bricht die Tür auf (nur Icons)
# ===========================================================================================================================
KOX2 = 1480
folie([("huette", "Fall · die Berghütte von Frau Moser"), ("zu", "Fall · im Winter verschlossen"),
       ("ko1", "Fall · Gefahr zu erfrieren"), ("auf", "Fall · Tür aufgebrochen")], [
    schnee("huette"),
    huette("huette", "zu", bis="auf"),
    huette("auf", "offen"),
    *flocken("huette", [(1700, 170), (1790, 430), (120, 180)]),
    pl("Hütte von Frau Moser", 70, 30, beim("huette", "gehört"), fill=GRUEN, size=36),
    ficon("tabler", "lock", (TUER[0] + TUER[1]) // 2, TUER_O + 150, 70, "zu", fuell=GELB, bis="auf"),
    pl("im Winter verschlossen", 70, 110, "zu", fill=WEISS, size=34),
    schild_189("schild", 920),
    *stehend("KO", KOX2, [("huette", "angst")], unten=BODEN_Y, bis="ko1"),
    *redet("KO_redet", KOX2, BODEN_Y, FHA, "ko1", "auf"),
    hart(ns(NAME["KO"], KOX2, BODEN_Y, "ko1", NFARBE["KO"])),
    blase("sprech", 720, 220, "ko1", 1280, 240, inhalt=["Wenn ich heute Nacht hier", "draußen bleibe,", "erfriere ich."],
          textsize=36, figur=("KO_redet", KOX2, BODEN_Y, FHA), bis="auf"),
    *fig("KO", KOX2, BODEN_Y, FHA, [("auf", "fest"), ("kaputt", "ernst")], erst="cut"),
    szene(ficon("tabler", "tool", 1140, 680, 120, "auf", fuell=WEISS), "189tuer*", 1.0, 0.0),
    pl("Tür aufgebrochen", 1140, 330, "auf", fill=WEISS, size=32, anker="m"),
    ficon("tabler", "lock-open-off", 1140, 860, 110, "kaputt", fuell=HELLROT),
    pl("Schloss kaputt", 1140, 410, beim("kaputt", "kaputt"), fill=HELLROT, size=32, anker="m"),
])

# ===========================================================================================================================
# A3 Fall: Nacht in der Hütte
# ===========================================================================================================================
KOX3 = 1500
folie([("nacht", "Fall · die Nacht in der Hütte")], [
    innen("nacht"),
    boden("nacht"),
    hart(pl("In der Hütte", 70, 30, "nacht", fill=HOLZ, size=38)),
    ficon("tabler", "moon-stars", 370, 290, 120, "nacht", fuell=GELB),
    *flocken("nacht", [(250, 200), (480, 340), (300, 410)], gr=44),
    *stehend("KO", KOX3, [("nacht", "froh")], unten=BODEN_Y),
    pl("Nacht überstanden", 970, 330, beim("nacht", "übersteht"), fill=HELLGRUEN, size=34, anker="m"),
])

# ===========================================================================================================================
# A4 Fall: am nächsten Morgen – Frau Moser, neues Schloss 380 €
# ===========================================================================================================================
MOX4, KOX4 = 1150, 1600
folie([("morgen", "Fall · am nächsten Morgen"), ("mo1", "Fall · Wer bezahlt das Schloss?"),
       ("frage", "Fall · die Fragen")], [
    schnee("morgen"),
    huette("morgen", "offen"),
    ficon("tabler", "sun", 900, 260, 120, "morgen", fuell=GELB),
    hart(pl("am nächsten Morgen", 70, 30, "morgen", fill=GELB, size=36)),
    *stehend("MO", MOX4, [("morgen", "skeptisch_r"), ("preis", "aerger_r")], unten=BODEN_Y, bis="mo1"),
    *stehend("KO", KOX4, [("morgen", "muede"), ("mo1", "sorge"), ("frage", "skeptisch")], unten=BODEN_Y),
    ficon("tabler", "receipt", 1375, 540, 90, "preis", fuell=WEISS, bis="mo1"),
    pl("neues Schloss: 380 €", 70, 110, beim("preis", "neues"), fill=WEISS, size=34),
    *redet("MO_redet_r", MOX4, BODEN_Y, FHA, "mo1", "frage"),
    hart(ns(NAME["MO"], MOX4, BODEN_Y, "mo1", NFARBE["MO"])),
    blase("sprech", 700, 220, "mo1", 1360, 240, inhalt=["Die Tür war abgesperrt!", "Wer bezahlt mir jetzt",
                                                       "das neue Schloss?"], textsize=34,
          figur=("MO_redet_r", MOX4, BODEN_Y, FHA), bis="frage"),
    *fig("MO", MOX4, BODEN_Y, FHA, [("frage", "ernst_r")], erst="cut"),
    pl("Strafbar?", 70, 190, "frage", fill=PINK, size=36),
    pl("Muss er das Schloss bezahlen?", 70, 270, "frage2", fill=PINK, size=36),
    pl("rechtfertigender Notstand, § 34 StGB", 70, 350, "frage3", fill=HELLGRUEN, size=34),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_189(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=34, zeilenabstand=1.30)
        els += e; y += 18
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_189("sv", [
    "Samstag, 17:40 Uhr, auf 2.150 m: Korbinian (Mitte 30) ist allein auf Bergtour, als ein Wettersturz einsetzt – "
    "Schneesturm, −12 °C. Sein Handy hat kein Netz, bis ins Tal sind es 3 Stunden, eine andere Unterkunft gibt es nicht.",
    "Er erreicht eine Berghütte, die Frau Moser gehört. Sie ist im Winter verschlossen; ein Schild verbietet das Betreten. "
    "Um nicht zu erfrieren, bricht Korbinian die Tür auf; das Schloss ist danach kaputt. In der Hütte übersteht er die Nacht.",
    "Am nächsten Morgen kommt Frau Moser. Ein neues Schloss kostet 380 €. Sie fragt: „Wer bezahlt mir jetzt das neue Schloss?“",
], "Hat Korbinian sich strafbar gemacht – und muss er das Schloss bezahlen?")

# ===========================================================================================================================
# C Tatbestand kurz: §§ 303, 123 StGB
# ===========================================================================================================================
PA = "A. Korbinian, §§ 303, 123 StGB"
folie([("tb", f"{PA} › I. Tatbestand"), ("tb303", f"{PA} › I. Tatbestand: § 303 Abs. 1"),
       ("tb123", f"{PA} › I. Tatbestand: § 123 Abs. 1"), ("vors", f"{PA} › I. Tatbestand: Vorsatz"),
       ("rw", f"{PA} › II. Rechtswidrigkeit")], rechts_frei([
    *tafel("tb", "Tatbestand: §§ 303, 123 StGB"),
    *okz("§ 303 Abs. 1: fremde Sache beschädigt (Schloss)", 200, "tb303", "Bold", 34, x=160),
    *okz("§ 123 Abs. 1: in fremde Hütte eingedrungen", 280, "tb123", "Bold", 34, x=160),
    *okz("Vorsatz", 360, "vors", "Bold", 34, x=160),
    blk(110, 470, 1040, 120, GELB, "rw", [("II. Rechtswidrigkeit:", "ExtraBold", 36, INK),
                                         ("gerechtfertigt durch Notstand?", "ExtraBold", 36, INK)]),
    *requisit([("tb", ("tabler", "gavel", 100, WEISS), "Tatbestand", WEISS),
               ("tb303", ("tabler", "lock-open-off", 100, HELLROT), "Schloss kaputt", HELLROT),
               ("tb123", ("tabler", "door-enter", 100, WEISS), "in die Hütte", WEISS),
               ("rw", ("tabler", "scale", 100, GELB), "gerechtfertigt?", GELB)]),
    *allein("KO", [("tb", "ruhig"), ("tb303", "sorge"), ("rw", "skeptisch")]),
]))

# ===========================================================================================================================
# D Wortlautkarte § 34 StGB (S. 1 und S. 2 vollständig)
# ===========================================================================================================================
PN = "A. Korbinian › II. Rechtswidrigkeit › § 34 StGB"
W34 = ("„Wer in einer gegenwärtigen, nicht anders abwendbaren Gefahr für Leben, Leib, Freiheit, Ehre, Eigentum oder ein "
       "anderes Rechtsgut eine Tat begeht, um die Gefahr von sich oder einem anderen abzuwenden, handelt nicht rechtswidrig, "
       "wenn bei Abwägung der widerstreitenden Interessen, namentlich der betroffenen Rechtsgüter und des Grades der ihnen "
       "drohenden Gefahren, das geschützte Interesse das beeinträchtigte wesentlich überwiegt. Dies gilt jedoch nur, soweit "
       "die Tat ein angemessenes Mittel ist, die Gefahr abzuwenden.“")
w34, w34_y = wortlaut(80, 165, 1100, W34, "§ 34 S. 1, 2 StGB", "p34", marken=[
    ("gegenwärtigen,", beim("p34", "gegenwärtige")), ("nicht anders abwendbaren", beim("p34", "nicht")),
    ("Rechtsgut", beim("p34", "Rechtsgut")), ("eine Tat begeht,", beim("p34", "Tat")),
    ("abzuwenden,", beim("p34", "abzuwenden")), ("handelt nicht", beim("p34", "handelt")),
    ("rechtswidrig,", beim("p34", "rechtswidrig")), ("das geschützte Interesse", beim("abw", "geschützte")),
    ("wesentlich überwiegt.", beim("abw", "wesentlich")), ("angemessenes", beim("s2", "angemessenes")),
    ("Mittel ist,", beim("s2", "Mittel"))], size=30)
folie([("p34", f"{PN} · Wortlaut S. 1"), ("abw", f"{PN} · wesentlich überwiegt"), ("s2", f"{PN} · S. 2: angemessenes Mittel")], rechts_frei([
    *tafel("p34", "Rechtfertigender Notstand"),
    *w34,
    *requisit([("p34", ("tabler", "alert-triangle", 100, GELB), "Gefahr", GELB),
               ("abw", ("tabler", "scale", 100, WEISS), "wesentlich überwiegt?", WEISS),
               ("s2", ("tabler", "circle-check", 100, HELLGRUEN), "angemessen?", HELLGRUEN)]),
    *allein("KO", [("p34", "ruhig"), ("abw", "skeptisch")]),
]))
assert w34_y <= 890, w34_y

# ===========================================================================================================================
# E 1. Notstandslage
# ===========================================================================================================================
PL1 = "A. Korbinian › § 34 StGB › 1. Notstandslage"
folie([("lage", f"{PL1} › a) Gefahr für ein Rechtsgut"), ("leben", f"{PL1} › a) hier: Leben und Leib"),
       ("gegenw", f"{PL1} › b) gegenwärtig"), ("lage_ok", f"{PL1} › b) gegenwärtig (+)")], rechts_frei([
    *tafel("lage", "1. Notstandslage"),
    z("a) Gefahr für ein Rechtsgut", 110, 190, "lage", "ExtraBold", 36),
    *okz("Leben und Leib: Erfrieren droht", 250, "leben", "Bold", 34, x=200),
    z("b) gegenwärtig", 110, 350, "gegenw", "ExtraBold", 36),
    z("Schutzmaßnahmen müssen sofort eingeleitet werden,", 160, 410, beim("gegenw", "Schutzmaßnahmen"), size=32),
    z("um den Schaden sicher zu verhindern", 160, 456, beim("gegenw", "um"), size=32),
    zit("BGH, Urt. v. 25.3.2003 – 1 StR 483/02, Rn. 27 (BGHSt 48, 255; zu § 35 StGB)", 160, 510, beim("gegenw", "verhindern")),
    *okz("−12 °C, einbrechende Nacht: gegenwärtig", 590, "lage_ok", "Bold", 34, x=200),
    *requisit([("lage", ("tabler", "alert-triangle", 100, GELB), "Gefahr", GELB),
               ("leben", ("tabler", "heartbeat", 100, HELLROT), "Leben, Leib", HELLROT),
               ("gegenw", ("tabler", "clock", 100, WEISS), "sofort handeln", WEISS),
               ("lage_ok", ("tabler", "snowflake", 100, WEISS), "−12 °C, Nacht", WEISS)]),
    *allein("KO", [("lage", "ernst"), ("leben", "angst"), ("lage_ok", "sorge")]),
]))

# ===========================================================================================================================
# F 2. Notstandshandlung: nicht anders abwendbar (geeignet, erforderlich)
# ===========================================================================================================================
PL2 = "A. Korbinian › § 34 StGB › 2. Notstandshandlung"
folie([("handl", f"{PL2} › nicht anders abwendbar"), ("geeig", f"{PL2} › a) geeignet"),
       ("erf", f"{PL2} › b) erforderlich"), ("nur", f"{PL2} › b) erforderlich (+)")], rechts_frei([
    *tafel("handl", "2. Notstandshandlung"),
    z("Gefahr nicht anders abwendbar:", 110, 185, "handl", "Bold", 34),
    *okz("a) geeignet: Schutz vor Kälte und Wind", 245, "geeig", "Bold", 34, x=160),
    z("b) erforderlich: mildestes gleich wirksames Mittel", 110, 330, "erf", "ExtraBold", 34),
    *neinz("Notruf: kein Netz", 400, beim("kein", "Notruf"), size=32, x=200),
    *neinz("Abstieg: 3 Stunden", 455, beim("kein", "Abstieg"), size=32, x=200),
    *neinz("andere Unterkunft: keine", 510, beim("kein", "Unterkunft"), size=32, x=200),
    *okz("nur die Tür aufgebrochen, nichts sonst", 590, "nur", "Bold", 34, x=160),
    *requisit([("handl", ("tabler", "route", 100, WEISS), "anderer Ausweg?", WEISS),
               ("geeig", ("tabler", "home", 100, GELB), "Schutz in der Hütte", GELB),
               ("kein", ("tabler", "device-mobile-off", 100, HELLROT), "kein Netz", HELLROT),
               ("nur", ("tabler", "door", 100, WEISS), "nur die Tür", WEISS)]),
    *allein("KO", [("handl", "ernst"), ("geeig", "ruhig"), ("kein", "sorge"), ("nur", "fest")]),
]))

# ===========================================================================================================================
# G 3. Interessenabwägung
# ===========================================================================================================================
PL3 = "A. Korbinian › § 34 StGB › 3. Interessenabwägung"
folie([("abwaeg", f"{PL3} · wesentlich überwiegen"), ("krit", f"{PL3} › Rechtsgüter, Grad der Gefahren"),
       ("links", f"{PL3} › geschützt: Leben, Gesundheit"), ("rechts", f"{PL3} › beeinträchtigt: Schloss, Hausrecht"),
       ("ueber", f"{PL3} › wesentlich überwiegend (+)")], rechts_frei([
    *tafel("abwaeg", "3. Interessenabwägung"),
    z("geschütztes Interesse muss wesentlich überwiegen", 110, 185, "abwaeg", "Bold", 34),
    z("vor allem: betroffene Rechtsgüter, Grad der Gefahren", 110, 240, "krit", size=32),
    blk(110, 320, 500, 170, HELLGRUEN, "links", [("geschützt:", "ExtraBold", 32, INK), ("Leben, Gesundheit", "Bold", 32, INK),
                                                ("akute Gefahr", "Bold", 32, INK)]),
    blk(650, 320, 500, 170, HELLROT, "rechts", [("beeinträchtigt:", "ExtraBold", 32, INK), ("Schloss (380 €)", "Bold", 32, INK),
                                               ("Hausrecht, 1 Nacht", "Bold", 32, INK)]),
    *okz("geschütztes Interesse überwiegt wesentlich", 560, "ueber", "ExtraBold", 34, x=160),
    *requisit([("abwaeg", ("tabler", "scale", 100, WEISS), "Abwägung", WEISS),
               ("links", ("tabler", "heartbeat", 100, HELLGRUEN), "Leben", HELLGRUEN),
               ("rechts", ("tabler", "lock-open-off", 100, HELLROT), "Schloss: 380 €", HELLROT),
               ("ueber", ("tabler", "heart", 100, HELLGRUEN), "Leben wiegt schwerer", HELLGRUEN)]),
    *zwei([("abwaeg", "ruhig"), ("rechts", "skeptisch"), ("ueber", "ernst")],
          [("abwaeg", "ernst"), ("links", "sorge"), ("ueber", "froh")]),
]))

# ===========================================================================================================================
# H 4. Angemessenheit, § 34 S. 2
# ===========================================================================================================================
PL4 = "A. Korbinian › § 34 StGB › 4. Angemessenheit, S. 2"
folie([("angem", PL4), ("ausn", f"{PL4} › nur in Ausnahmefällen"), ("angem_ok", f"{PL4} › angemessen (+)")], rechts_frei([
    *tafel("angem", "4. Angemessenheit, § 34 S. 2"),
    z("eigene Rolle nur in Ausnahmefällen", 110, 190, "ausn", "Bold", 34),
    zit("verbreitete Ansicht", 110, 245, beim("ausn", "verbreiteter")),
    z("z. B. Mensch als bloßes Mittel der Rettung", 110, 300, beim("ausn", "Mensch"), size=32),
    *okz("hier: angemessen", 400, "angem_ok", "ExtraBold", 36, x=160),
    *requisit([("angem", ("tabler", "circle-check", 100, WEISS), "angemessenes Mittel?", WEISS),
               ("ausn", ("tabler", "user-x", 100, HELLROT), "Ausnahme", HELLROT),
               ("angem_ok", ("tabler", "circle-check", 100, HELLGRUEN), "angemessen", HELLGRUEN)]),
    *allein("KO", [("angem", "ruhig"), ("ausn", "skeptisch"), ("angem_ok", "froh")]),
]))

# ===========================================================================================================================
# I 5. subjektives Rechtfertigungselement
# ===========================================================================================================================
PL5 = "A. Korbinian › § 34 StGB › 5. subjektives Rechtfertigungselement"
folie([("subj", PL5), ("kennt", f"{PL5} › Kenntnis"), ("um", f"{PL5} › um die Gefahr abzuwenden"),
       ("erg34", "A. Korbinian › § 34 StGB › Voraussetzungen (+)")], rechts_frei([
    *tafel("subj", "5. Subjektives Element"),
    z("subjektives Rechtfertigungselement", 110, 180, "subj", "Bold", 34),
    *okz("Kenntnis der Notstandslage", 250, "kennt", "Bold", 34, x=160),
    *okz("Handeln, um die Gefahr abzuwenden", 320, "um", "Bold", 34, x=160),
    zit("§ 34 S. 1 StGB: „um die Gefahr … abzuwenden“", 160, 375, beim("um", "Wortlaut")),
    *okz("Korbinian will nicht erfrieren", 440, "subj_ok", "Bold", 34, x=160),
    blk(110, 540, 1040, 80, HELLGRUEN, "erg34", [("§ 34 StGB: Voraussetzungen (+)", "ExtraBold", 36, INK)]),
    *requisit([("subj", ("tabler", "brain", 100, WEISS), "Rettungswille", WEISS),
               ("subj_ok", ("tabler", "snowflake-off", 100, GELB), "nicht erfrieren", GELB),
               ("erg34", ("tabler", "shield-check", 100, HELLGRUEN), "§ 34 (+)", HELLGRUEN)]),
    *allein("KO", [("subj", "ruhig"), ("subj_ok", "fest"), ("erg34", "froh")]),
]))

# ===========================================================================================================================
# J § 904 BGB (Wortlautkarte S. 1, S. 2): Aggressivnotstand, Ersatzpflicht
# ===========================================================================================================================
PB = "Zivilrechtlicher Notstand › § 904 BGB"
W904 = ("„Der Eigentümer einer Sache ist nicht berechtigt, die Einwirkung eines anderen auf die Sache zu verbieten, wenn "
        "die Einwirkung zur Abwendung einer gegenwärtigen Gefahr notwendig und der drohende Schaden gegenüber dem aus der "
        "Einwirkung dem Eigentümer entstehenden Schaden unverhältnismäßig groß ist. Der Eigentümer kann Ersatz des ihm "
        "entstehenden Schadens verlangen.“")
w904, w904_y = wortlaut(80, 165, 1100, W904, "§ 904 S. 1, 2 BGB", "p904", marken=[
    ("zu verbieten,", beim("p904", "verbieten")), ("gegenwärtigen Gefahr notwendig", beim("p904", "gegenwärtigen")),
    ("unverhältnismäßig groß", beim("p904b", "unverhältnismäßig"))], size=30)
folie([("bgb", "Zivilrechtlicher Notstand · speziellere Regeln im BGB"), ("p904", f"{PB} S. 1"),
       ("aggr", f"{PB} › Aggressivnotstand"), ("verbot", f"{PB} › Verbot unbeachtlich"),
       ("p904s2", f"{PB} S. 2: Ersatzanspruch")], rechts_frei([
    *tafel("bgb", "Spezieller: § 904 BGB"),
    pl("bei Eingriffen in Sachen: Notstand im BGB", 640, 100, "bgb", fill=PINK, size=28),
    *bis_l(w904, "aggr"),
    z("Aggressivnotstand: Gefahr von außen (Wetter)", 110, 200, "aggr", "ExtraBold", 34),
    *okz("Eingriff in unbeteiligte fremde Sache: die Tür", 270, "unbet", "Bold", 32, x=160),
    *neinz("Schild „Betreten verboten“ hilft nicht", 340, "verbot", "Bold", 32, x=160),
    z("§ 904 S. 2 BGB: „Der Eigentümer kann Ersatz", 110, 440, "p904s2", "Bold", 32),
    z("des ihm entstehenden Schadens verlangen.“", 110, 486, "p904s2", "Bold", 32),
    *requisit([("bgb", ("tabler", "book", 100, WEISS), "BGB", WEISS),
               ("aggr", ("tabler", "cloud-snow", 100, WEISS), "Gefahr: Wetter", WEISS),
               ("unbet", ("tabler", "door", 100, WEISS), "unbeteiligte Tür", WEISS),
               ("verbot", ("tabler", "ban", 100, HELLROT), "Verbot unbeachtlich", HELLROT),
               ("p904s2", ("tabler", "receipt", 100, GELB), "Ersatz des Schadens", GELB),
               ("mo2", None, None, None)]),
    *stehend("MO", X1, [("bgb", "ruhig"), ("verbot", "aerger"), ("p904s2", "skeptisch")], bis="mo2"),
    *redet("MO_redet2", X1, FB, FR, "mo2", "p228"),
    hart(ns(NAME["MO"], X1, FB, "mo2", NFARBE["MO"])),
    blase("sprech", 560, 200, "mo2", 1560, 190, inhalt=["Dann zahlen Sie mir das", "Schloss also trotzdem."],
          textsize=34, figur=("MO_redet2", X1, FB, FR), bis="p228"),
    *stehend("KO", X2, [("bgb", "ruhig"), ("unbet", "ernst"), ("p904s2", "sorge")]),
]))

# ===========================================================================================================================
# K § 228 BGB (Wortlautkarte): Defensivnotstand
# ===========================================================================================================================
PD = "Zivilrechtlicher Notstand › § 228 BGB"
W228 = ("„Wer eine fremde Sache beschädigt oder zerstört, um eine durch sie drohende Gefahr von sich oder einem anderen "
        "abzuwenden, handelt nicht widerrechtlich, wenn die Beschädigung oder die Zerstörung zur Abwendung der Gefahr "
        "erforderlich ist und der Schaden nicht außer Verhältnis zu der Gefahr steht. Hat der Handelnde die Gefahr "
        "verschuldet, so ist er zum Schadensersatz verpflichtet.“")
w228, w228_y = wortlaut(80, 165, 1100, W228, "§ 228 BGB", "p228", marken=[
    ("fremde Sache beschädigt", beim("p228", "fremde")), ("durch sie", beim("p228", "drohende")),
    ("drohende Gefahr", beim("p228", "drohende")), ("handelt nicht", beim("p228", "Nicht")),
    ("widerrechtlich,", beim("p228", "Nicht")), ("erforderlich", beim("p228b", "erforderlich")),
    ("nicht außer Verhältnis", beim("p228b", "außer"))], size=30)
folie([("p228", f"{PD} · Defensivnotstand"), ("hund", f"{PD} › Gefahr geht von der Sache aus"),
       ("tuer", f"{PD} › hier: (−)")], rechts_frei([
    *tafel("p228", "Defensivnotstand: § 228 BGB"),
    *w228,
    z("Gefahr geht von der Sache selbst aus", 110, w228_y + 30, "hund", "ExtraBold", 34),
    zit("z. B. angreifender Hund (Tiere: § 90a S. 3 BGB)", 110, w228_y + 82, beim("hund", "angreifenden")),
    *neinz("hier: Die Tür bedroht Korbinian nicht.", w228_y + 150, "tuer", "Bold", 34, x=160),
    *requisit([("p228", ("tabler", "hammer", 100, WEISS), "Sache beschädigt", WEISS),
               ("hund", ("tabler", "dog", 110, GELB), "Gefahr durch die Sache", GELB),
               ("tuer", ("tabler", "door", 100, WEISS), "Tür: keine Gefahr", WEISS)]),
    *allein("KO", [("p228", "ruhig"), ("hund", "angst"), ("tuer", "froh")]),
]))
assert w228_y + 210 <= 890, w228_y

# ===========================================================================================================================
# L Spezialität (h. M.)
# ===========================================================================================================================
folie([("spez", "Verhältnis: §§ 228, 904 BGB vor § 34 StGB (h. M.)")], rechts_frei([
    *tafel("spez", "Verhältnis zu § 34 StGB"),
    z("nach herrschender Meinung:", 110, 200, beim("spez", "herrschender"), "Bold", 34),
    blk(110, 270, 1040, 90, GELB, beim("spez", "zivilrechtlichen"), [("§§ 228, 904 BGB gehen § 34 StGB vor", "ExtraBold", 36, INK)]),
    z("bei Eingriffen in Sachen", 110, 390, beim("spez", "Eingriffen"), "Bold", 34),
    ficon("tabler", "book", PX - 120, PU, 100, beim("spez", "zivilrechtlichen"), fuell=GELB),
    ficon("tabler", "arrow-right", PX, PU - 20, 70, beim("spez", "vor"), fuell=WEISS),
    ficon("tabler", "scale", PX + 120, PU, 100, beim("spez", "Paragrafen"), fuell=WEISS),
    pl("BGB vor § 34", PX, PY, beim("spez", "vor"), fill=GELB, size=28, anker="m"),
    *allein("KO", [("spez", "ruhig")]),
]))

# ===========================================================================================================================
# M Abgrenzung: § 32 (Verweis Folge 033) und § 35 (BGH 1 StR 483/02)
# ===========================================================================================================================
PG = "Abgrenzung"
folie([("p32", f"{PG} › Notwehr, § 32 StGB: (−)"), ("p35", f"{PG} › entschuldigender Notstand, § 35 StGB"),
       ("ht", f"{PG} › § 35 StGB: BGH, Haustyrannen-Fall")], rechts_frei([
    *tafel("p32", "Abgrenzung: §§ 32, 35 StGB"),
    *neinz("Notwehr, § 32: kein Angriff durch einen Menschen", 190, "p32", "Bold", 32, x=160),
    z("das Wetter greift nicht an", 160, 245, beim("p32", "Wetter"), size=32),
    zit("mehr dazu im Video „Notwehr Schema § 32 StGB“", 160, 300, "v033"),
    z("§ 35: entschuldigender Notstand", 110, 380, "p35", "ExtraBold", 34),
    z("wenn die Abwägung scheitert, z. B. Leben gegen Leben", 160, 435, beim("p35", "scheitert"), size=32),
    z("Tat bleibt rechtswidrig, Schuld kann entfallen", 160, 490, beim("p35", "Tat"), "Bold", 32),
    zit("BGH, Urt. v. 25.3.2003 – 1 StR 483/02 (BGHSt 48, 255, Haustyrann):", 160, 570, "ht"),
    zit("§ 34 an der Abwägung abgelehnt (Rn. 21), § 35 geprüft (Rn. 23 ff.)", 160, 612, "ht"),
    *requisit([("p32", ("tabler", "cloud-snow", 100, WEISS), "kein Angriff", WEISS),
               ("p35", ("tabler", "scale", 100, HELLROT), "§ 35: ohne Schuld", HELLROT),
               ("ht", ("tabler", "gavel", 100, WEISS), "BGHSt 48, 255", WEISS)]),
    *allein("KO", [("p32", "ruhig"), ("p35", "ernst")]),
]))

# ===========================================================================================================================
# N1 Lösung
# ===========================================================================================================================
PE = "Lösung"
folie([("lsg", f"{PE} · Korbinian"), ("l303", f"{PE} › § 303: gerechtfertigt, § 904 S. 1 BGB"),
       ("l123", f"{PE} › § 123: gerechtfertigt, § 34 StGB"), ("straflos", f"{PE} › straflos"),
       ("ersatz", f"{PE} › Ersatz, § 904 S. 2 BGB")], rechts_frei([
    *tafel("lsg", "Lösung"),
    *okz("§ 303 StGB: gerechtfertigt nach § 904 S. 1 BGB", 200, "l303", "Bold", 34, x=160),
    *okz("§ 123 StGB: jedenfalls gerechtfertigt nach § 34 StGB", 280, "l123", "Bold", 34, x=160),
    blk(110, 380, 1040, 80, HELLGRUEN, "straflos", [("Korbinian ist straflos.", "ExtraBold", 38, INK)]),
    blk(110, 500, 1040, 120, GELB, "ersatz", [("aber: Ersatz für das Schloss an", "ExtraBold", 34, INK),
                                             ("Frau Moser, § 904 S. 2 BGB", "ExtraBold", 34, INK)]),
    *requisit([("lsg", ("tabler", "gavel", 100, WEISS), "Ergebnis", WEISS),
               ("straflos", ("tabler", "shield-check", 100, HELLGRUEN), "straflos", HELLGRUEN),
               ("ersatz", ("tabler", "receipt", 100, GELB), "Ersatz für das Schloss", GELB)]),
    *zwei([("lsg", "ruhig"), ("ersatz", "froh")], [("lsg", "ruhig"), ("straflos", "froh"), ("ersatz", "ernst")]),
]))

# ===========================================================================================================================
# N2 Morgen an der Hütte: Korbinian zahlt gern (Blase)
# ===========================================================================================================================
MOX5, KOX5 = 1150, 1600
folie([("ko2", f"{PE} › Korbinian zahlt das Schloss")], [
    schnee("ko2"),
    huette("ko2", "offen"),
    ficon("tabler", "sun", 900, 260, 120, "ko2", fuell=GELB),
    hart(pl("am Morgen an der Hütte", 70, 30, "ko2", fill=GELB, size=36)),
    *stehend("MO", MOX5, [("ko2", "froh_r")], unten=BODEN_Y),
    *redet("KO_redet2", KOX5, BODEN_Y, FHA, "ko2", "tipp"),
    hart(ns(NAME["KO"], KOX5, BODEN_Y, "ko2", NFARBE["KO"])),
    blase("sprech", 700, 220, "ko2", 1340, 240, inhalt=["Das Schloss zahle ich gern.", "Hauptsache, ich bin",
                                                       "nicht erfroren."], textsize=34,
          figur=("KO_redet2", KOX5, BODEN_Y, FHA), bis="tipp"),
])

# ===========================================================================================================================
# O Klausurtipp (Lexi): spezielle Notstände zuerst
# ===========================================================================================================================
els_k = [*tafel("tipp", "Klausurtipp: spezielle Notstände zuerst", fill=HELL, size=44), warnung_i(150, 225, "tipp", gr=26),
         z("Eingriff in fremde Sachen: erst das BGB prüfen", 200, 200, "tipp", "Bold", 34),
         blk(130, 300, 1020, 130, GELB, "k1", [("§ 228 BGB: Gefahr geht von der", "ExtraBold", 34, INK),
                                               ("Sache selbst aus", "ExtraBold", 34, INK)]),
         blk(130, 460, 1020, 130, BLAU, "k2", [("§ 904 BGB: Eingriff in eine", "ExtraBold", 34, INK),
                                               ("unbeteiligte Sache", "ExtraBold", 34, INK)]),
         blk(130, 620, 1020, 90, HELLGRUEN, "k3", [("§ 34 StGB: fängt alle übrigen Fälle auf", "ExtraBold", 34, INK)]),
         *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
         ns("Lexi", FX, FB, "tipp", GELB, d=0.2)]
folie([("tipp", "Klausurtipp · spezielle Notstände zuerst"), ("k1", "Klausurtipp › § 228 BGB"),
       ("k2", "Klausurtipp › § 904 BGB"), ("k3", "Klausurtipp › § 34 StGB als Auffangnorm")], els_k)

# ===========================================================================================================================
# P Klausurschema § 34 StGB (Aufbau Punkt für Punkt)
# ===========================================================================================================================
REIHEN = [("s1", "1. Notstandslage: gegenwärtige Gefahr für ein Rechtsgut"),
          ("s2h", "2. Notstandshandlung: geeignet und erforderlich"),
          ("s3", "3. Interessenabwägung: geschütztes Interesse überwiegt wesentlich"),
          ("s4", "4. Angemessenheit, § 34 S. 2"),
          ("s5", "5. subjektives Rechtfertigungselement")]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Schema: Rechtfertigender Notstand, § 34 StGB"), 110, 90, "sch", 46)]
y = 220
for c, text in REIHEN:
    els_sch.append(z(text, 130, y, c, "ExtraBold", 42, rechts=1800))
    y += 110
assert y <= 960, y
folie([("sch", "Klausurschema · § 34 StGB"), ("s1", "Klausurschema › 1. Notstandslage"),
       ("s2h", "Klausurschema › 2. Notstandshandlung"), ("s3", "Klausurschema › 3. Interessenabwägung"),
       ("s4", "Klausurschema › 4. Angemessenheit"), ("s5", "Klausurschema › 5. subjektives Element")], els_sch)

# ===========================================================================================================================
# Q Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("§ 34 StGB rechtfertigt, wenn das", 0)],
                 [("geschützte Interesse ", 0), ("wesentlich überwiegt.", "a")]], 750, 290, 42, "merke",
                {"a": beim("merke", "wesentlich")}),
    *markertext([[("Bei Sachen gehen ", 0), ("§§ 228, 904 BGB", "b"), (" vor,", 0)]], 750, 470, 40, "m2",
                {"b": beim("m2", "Paragrafen")}),
    *markertext([[("und bei § 904 kann der Eigentümer", 0)],
                 [("Ersatz", "c"), (" verlangen.", 0)]], 750, 590, 40, "m3", {"c": beim("m3", "Ersatz")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
