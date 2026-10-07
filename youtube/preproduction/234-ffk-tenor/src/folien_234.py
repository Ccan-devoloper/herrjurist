"""Folge 234 · Fortsetzungsfeststellungsklage: Tenor und Feststellungsinteresse – Serienstandard Open Peeps (Katzenkönig).
Fiktiver Fall (Beispiel NRW): Samstagvormittag, Mahnwache vor der Stadtbücherei (die schließen soll); Herr Strauch leitet sie,
die Teilnehmenden stehen vor dem Eingang. Polizeihauptkommissar Nagel löst die Versammlung auf. Herr Strauch plant die nächste,
die Polizei würde wieder so handeln. Vor Gericht hält Richterin Bollmann die Auflösung für unverhältnismäßig. Danach aus
Sicht des zweiten Examens: 1. Antrag (Feststellung, analog; Umstellung bei Erledigung im Prozess, Wortlautkarte § 264 ZPO),
2. Feststellungsinteresse im Urteil (Wiederholungsgefahr, Rehabilitation, tiefgreifender Grundrechtseingriff),
3. Tenor (Muster und Fall, Verpflichtungssituation), Kosten § 154 I VwGO, vorläufige Vollstreckbarkeit §§ 167 VwGO, 708 Nr. 11,
711 ZPO, 4. typische Fehler und Hilfsantrag, Klausurtipp, Schema, Merksatz mit Lexi.
Szenen laut ../SZENENPLAN.md. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/feld/requisit/paar/
hand/plakat als eigene Kopie aus Folge 233 (gemeinsame Dateien unverändert); neu: buecherei(), pult().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut nach gesetze-im-internet.de bzw. recht.nrw.de, Abruf 07.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_234/"

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
TUERKIS_ = (127, 214, 208, 255)
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
        if n.startswith(("bild:", "ficon:")) or "/op_234/" in n:
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
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 07.10.2026 (Folge 234)), als Zitat mit Normangabe; der
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 160/203) -------------------------------------
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


# --- eigene Szenenbausteine (programmatisch, Palettenflächen, Tuschekontur) ---------------------------------------------------
BODEN = 860
FH = 440                                    # stehende Figur in der Fallszene
X1, X2 = 1400, 1720                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"ST": "Herr Strauch", "NA": "Herr Nagel", "BO": "Frau Bollmann"}
NFARBE = {"ST": HOLZ, "NA": BLAU, "BO": HELLGRAU}
WAND = (246, 236, 220, 255)


def _flaeche(w, h):
    s = 2
    im = Image.new("RGBA", ((w + 12) * s, (h + 12) * s))
    return im, ImageDraw.Draw(im), s


def boden(cue):
    return hart(linienzug([(40, BODEN), (1880, BODEN)], cue, breite=7, farbe=INK))

def _feld(w, h, fill=WEISS, rand=4, rund=14):
    im, dr, s = _flaeche(w, h)
    o = 6 * s
    dr.rounded_rectangle((o, o, o + w * s, o + h * s), rund * s, fill=fill, outline=INK, width=rand * s)
    return im.resize((w + 12, h + 12), Image.LANCZOS)


def feld(x, y, w, h, cue, fill=WEISS, rand=4, rund=14, bis=None, anim="cut", name="feld"):
    return El(_feld(w, h, fill, rand, rund), x, y, cue, anim, 0.0, bis, name=name)


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


def paar(a, af, b, bf):
    """Tafelszene: zwei Figuren rechts der Tafel (beide blicken nach links zur Tafel)."""
    return [*stehend(a, X1, af), *stehend(b, X2, bf)]



# --- Folge 234: Größen, Szenenbausteine ------------------------------------------------------------------------------
GROESSE = {"ST": 0.97, "NA": 1.0, "BO": 0.95}


def hh(k, h):
    return round(h * GROESSE.get(k, 1.0))


def stehend(k, x, folge, bis=None):
    els = [*fig(k, x, FB, hh(k, FR), folge, bis=bis), bis_(ns(NAME[k], x, FB, folge[0][0], NFARBE[k], d=0.1), bis)]
    return rechts_frei(els, 1200)


def hand(name, cx, unten, hoehe, b0=0.35, b1=0.60, links=True):
    """Äußerster deckender Punkt einer Figur im Höhenband b0–b1 (ausgestreckte bzw. erhobene Hand)."""
    e = peep_voll(name, cx, unten, hoehe, "_")
    a = np.asarray(e.sprite)[:, :, 3] > 40
    h_ = a.shape[0]
    band = a[int(h_ * b0):int(h_ * b1)]
    ys, xs = np.nonzero(band)
    i = xs.argmin() if links else xs.argmax()
    return e.x + xs[i], e.y + int(h_ * b0) + ys[i]


def plakat(text, cx, oben, unten, cue, bis=None, fill=WEISS, size=30):
    """Demo-Schild ohne Parole: weiße Tafel mit Tuschekontur auf einem Holzstiel (programmatisch, Palette)."""
    f = F("ExtraBold", size)
    b = f.getbbox(glyphen(text))
    w, h = b[2] - b[0] + 44, size + 34
    H_ = unten - oben
    s = 2
    im = Image.new("RGBA", (w * s, H_ * s))
    dr = ImageDraw.Draw(im)
    dr.rounded_rectangle(((w / 2 - 6) * s, h * s, (w / 2 + 6) * s, H_ * s), 4 * s, fill=INK)
    dr.rounded_rectangle(((w / 2 - 3) * s, h * s, (w / 2 + 3) * s, (H_ - 3) * s), 2 * s, fill=HOLZ)
    dr.rounded_rectangle((0, 0, w * s, h * s), 10 * s, fill=INK)
    dr.rounded_rectangle((5 * s, 5 * s, (w - 5) * s, (h - 5) * s), 7 * s, fill=fill)
    im = im.resize((w, H_), Image.LANCZOS)
    ImageDraw.Draw(im).text((22 - b[0], (h - (b[3] - b[1])) / 2 - b[1]), text, font=f, fill=INK)
    return El(im, cx - w / 2, oben, cue, "cut", 0.0, bis, name="plakat:" + text)

FASSADE = (238, 226, 206, 255)


def buecherei(cue, x0=60, x1=760, oben=300):
    """Stadtbücherei (programmatisch): Fassade mit Flachdachkante, vier Fenstern, großer Glastür und Schild darüber."""
    w, h = x1 - x0, BODEN - oben
    s = 2
    im = Image.new("RGBA", ((w + 12) * s, (h + 12) * s))
    dr = ImageDraw.Draw(im)
    o = 6 * s
    dr.rectangle((o - 4 * s, o, o + (w + 4) * s, o + 26 * s), fill=INK)
    dr.rectangle((o, o + 26 * s, o + w * s, o + h * s), fill=INK)
    dr.rectangle((o + 5 * s, o + 26 * s, o + (w - 5) * s, o + h * s), fill=FASSADE)
    for fx in (40, 160, w - 250, w - 130):
        for fy in (150, 300):
            dr.rounded_rectangle((o + fx * s, fy * s, o + (fx + 90) * s, (fy + 100) * s), 6 * s, fill=INK)
            dr.rounded_rectangle((o + (fx + 5) * s, (fy + 5) * s, o + (fx + 85) * s, (fy + 95) * s), 4 * s, fill=BLAUHELL)
    tx = w / 2 - 80
    dr.rounded_rectangle((o + tx * s, (h - 200) * s, o + (tx + 160) * s, (h + 6) * s), 8 * s, fill=INK)
    dr.rounded_rectangle((o + (tx + 6) * s, (h - 194) * s, o + (tx + 77) * s, (h + 6) * s), 5 * s, fill=BLAUHELL)
    dr.rounded_rectangle((o + (tx + 83) * s, (h - 194) * s, o + (tx + 154) * s, (h + 6) * s), 5 * s, fill=BLAUHELL)
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    return El(im, x0 - 6, oben - 6, cue, "cut", 0.0, None, name="buecherei")


def schild(text, cx, y, cue, size=32):
    """Schild über der Tür (Palette, Tuschekontur, Text programmatisch)."""
    return pl(text, cx, y, cue, fill=GELB, size=size, anker="m", anim="cut")


def pult(cx, cue, breite=520, hoehe=160, oben=700):
    """Richtertisch (programmatisch): Holzfront mit Tuschekontur; steht vor den Beinen der Richterin."""
    return feld(cx - breite // 2, oben, breite, hoehe, cue, fill=HOLZ, rand=5, rund=10, name="pult")


# ===========================================================================================================================
# A1 Fall: Mahnwache vor der Stadtbücherei – Auflösung, Mahnwache vorbei, die nächste ist geplant
# ===========================================================================================================================
FH_ = 440
TAX, TMX, STX, NAX = 300, 520, 900, 1720
TUER = 410
NULL = ("fall", -round(T_("fall"), 3))
WEGG = beim("vorbei", "gehen"), beim("vorbei", "Hause", ende=True)     # die Teilnehmenden gehen nach Hause
weg_ta = bewegt(peep_voll("TA_sorge", TAX - 90, BODEN, 420, WEGG[0], anim="cut", bis="naechst"), WEGG[0], WEGG[1], 90)
szene(weg_ta, "234schritte*", 0.55, 0.0)                # Schritte, solange die Teilnehmenden sichtbar weggehen
FALL_PFADE = [(NULL, "Fall · Samstagvormittag vor der Stadtbücherei"), ("strauch", "Fall · Mahnwache für die Bücherei"),
              ("eingang", "Fall · Direkt vor dem Eingang"), ("nagel", "Fall · Die Polizei kommt"),
              ("na1", "Fall · Die Auflösung"), ("vorbei", "Fall · Die Mahnwache ist vorbei"),
              ("naechst", "Fall · Die nächste Mahnwache")]
folie(FALL_PFADE, [
    hart(boden(NULL)),
    hart(buecherei(NULL)),
    schild("Stadtbücherei", TUER, 236, NULL),
    hart(ficon("tabler", "sun", 1830, 150, 96, NULL, fuell=GELB, anim="cut")),
    hart(pl("Samstagvormittag vor der Stadtbücherei", 820, 30, NULL, fill=GELB, size=32)),
    plakat("Bücherei bleibt!", TAX - 40, 330, 690, NULL, bis=WEGG[0]),        # Stiel hinter dem Körper: die Teilnehmerin hält es
    bewegt(plakat("Bücherei bleibt!", TAX - 130, 330, 690, WEGG[0], bis="naechst"), WEGG[0], WEGG[1], 90),
    *fig("TA", TAX, BODEN, 420, [(NULL, "froh"), ("na1", "sorge")], bis=WEGG[0], erst="cut"),
    weg_ta,
    *fig("TM", TMX, BODEN, 440, [(NULL, "froh"), ("na1", "sorge")], bis=WEGG[0], erst="cut"),
    bewegt(peep_voll("TM_sorge", TMX - 160, BODEN, 440, WEGG[0], anim="cut", bis="naechst"), WEGG[0], WEGG[1], 160),
    # Herr Strauch leitet die Mahnwache: Kerze
    ficon("tabler", "candle", 700, BODEN, 80, NULL, fuell=GELB, anim="cut", bis="naechst"),
    *fig("ST", STX, BODEN, hh("ST", FH_), [(NULL, "ruhig"), ("strauch", "entschl"), ("nagel", "denkt_r"), ("na1", "schreck_r")],
         bis="st1", erst="cut"),
    *redet("ST_ruft_r", STX, BODEN, hh("ST", FH_), "st1", "vorbei"),
    *fig("ST", STX, BODEN, hh("ST", FH_), [("vorbei", "muede_r"), ("naechst", "entschl_r")], erst="cut"),
    ns(NAME["ST"], STX, BODEN, NULL, NFARBE["ST"], anim="cut"),
    pl("Mahnwache: Die Bücherei soll schließen.", 820, 94, beim("strauch", "Mahnwache"), fill=WEISS, size=30, bis="na1"),
    pl("rund 20 Teilnehmer direkt vor dem Eingang", 820, 158, beim("eingang", "rund"), fill=HELLROT, size=30, bis="nagel"),
    # Polizeihauptkommissar Nagel: löst auf
    *fig("NA", NAX, BODEN, FH_, [("nagel", "ernst")], bis="na1"),
    *redet("NA_spricht", NAX, BODEN, FH_, "na1", "st1"),
    *fig("NA", NAX, BODEN, FH_, [("st1", "streng"), ("vorbei", "ruhig"), ("naechst", "ernst")], erst="cut"),
    ns(NAME["NA"], NAX, BODEN, "nagel", NFARBE["NA"], d=0.1),
    pl("Polizeihauptkommissar Nagel", 820, 158, beim("nagel", "Polizeihauptkommissar"), fill=BLAU, size=30, bis="na1"),
    blase("sprech", 600, 190, "na1", 1420, 230, inhalt=["Sie versperren den Eingang.", "Die Versammlung ist aufgelöst."],
          textsize=31, figur=("NA_spricht", NAX, BODEN, FH_), bis="st1"),
    ficon("tabler", "ban", 1180, 560, 80, beim("na1", "aufgelöst"), fuell=HELLROT, bis="st1"),
    blase("sprech", 560, 190, "st1", 1300, 210, inhalt=["Wir können doch ein paar", "Meter zur Seite gehen!"], textsize=32,
          figur=("ST_ruft_r", STX, BODEN, hh("ST", FH_)), bis="vorbei"),
    ficon("tabler", "arrow-move-right", 1180, 560, 90, beim("st1", "Seite"), fuell=GELB, bis="vorbei"),
    # Die Mahnwache ist vorbei; die nächste ist geplant
    pl("Alle gehen nach Hause: Die Mahnwache ist vorbei.", 820, 94, beim("vorbei", "Alle"), fill=GELB, size=30, bis="naechst"),
    ficon("tabler", "calendar-event", 1180, 560, 110, "naechst", fuell=GELB),
    pl("nächste Mahnwache: wieder vor der Bücherei", 820, 94, beim("naechst", "nächste"), fill=GELB, size=28),
    ficon("tabler", "repeat", 1480, 560, 100, beim("naechst", "Polizei"), fuell=BLAUHELL),
    pl("Polizei: würde wieder so handeln", 820, 158, beim("naechst", "würde"), fill=BLAUHELL, size=28),
])

# ===========================================================================================================================
# A2 Verwaltungsgericht: Klage und mündliche Verhandlung
# ===========================================================================================================================
BOX, STG = 1600, 1180
folie([("klage", "Fall · Die Klage"), ("gericht", "Fall · Mündliche Verhandlung"), ("ri1", "Fall · Die Richterin")], [
    hart(boden("klage")),
    ficon("fluent-emoji-high-contrast", "classical-building", 420, BODEN, 460, "klage", fuell=WEISS),
    pl("Verwaltungsgericht", 420, 300, "klage", fill=WEISS, size=32, anker="m"),
    pl("Herr Strauch klagt.", 70, 30, beim("klage", "klagt"), fill=GELB, size=32),
    ficon("tabler", "file-text", 800, 560, 100, beim("klage", "klagt"), fuell=WEISS),
    pl("Mündliche Verhandlung", 70, 94, "gericht", fill=WEISS, size=32),
    *fig("ST", STG, BODEN, hh("ST", FH_), [("klage", "entschl_r"), ("gericht", "ernst_r"), ("ri1", "denkt_r")]),
    ns(NAME["ST"], STG, BODEN, "klage", NFARBE["ST"], d=0.1),
    *fig("BO", BOX, BODEN, hh("BO", FH_), [("gericht", "ruhig")], bis="ri1"),
    *redet("BO_spricht", BOX, BODEN, hh("BO", FH_), "ri1", "frage"),
    pult(BOX, "gericht"),
    ns(NAME["BO"], BOX, BODEN, "gericht", NFARBE["BO"], d=0.1),
    blase("sprech", 600, 230, "ri1", 1050, 220, inhalt=["Ein paar Meter zur Seite", "hätten genügt. Die Auflösung",
                                                       "war unverhältnismäßig."], textsize=30,
          figur=("BO_spricht", BOX, BODEN, hh("BO", FH_))),
    pl("Auflösung: unverhältnismäßig", 70, 158, beim("ri1", "unverhältnismäßig"), fill=HELLROT, size=30),
])

# ===========================================================================================================================
# A3 Die Frage
# ===========================================================================================================================
folie([("frage", "Die Frage · Antrag und Feststellungsinteresse"), ("frage2", "Die Frage · Der Tenor"),
       ("frage3", "Die Frage · 2. Examen, Beispiel NRW")], [
    *tafel("frage", "Die Frage"),
    z("Die Versammlung ist längst vorbei.", 110, 180, "frage", "Bold", 38),
    z("1. Was beantragt Herr Strauch?", 110, 260, beim("frage", "Was"), size=36),
    z("2. Wie begründet das Urteil sein", 110, 316, beim("frage", "wie"), size=36),
    z("Feststellungsinteresse?", 150, 366, beim("frage", "wie"), size=36),
    z("3. Wie lautet der Tenor?", 110, 432, "frage2", size=36),
    blk(110, 520, 1040, 140, GELB, "frage3", [("Perspektive des 2. Examens", "ExtraBold", 37, INK),
                                             ("Beispiel: Nordrhein-Westfalen", "Bold", 34, INK)]),
    *requisit([("frage", ("tabler", "hourglass", 110, GELB), "längst vorbei", GELB),
               ("frage2", ("fluent-emoji-high-contrast", "balance-scale", 130, WEISS), "Tenor?", WEISS)]),
    *paar("ST", [("frage", "denkt"), ("frage2", "ernst")], "BO", [("frage", "ruhig"), ("frage3", "froh")]),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_234(cue, absaetze, frage):
    els = [karte(140, 50, 1640, 930, cue, fill=HELL), titel("Sachverhalt", 210, 84, cue, 56)]
    y = 180
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=36, zeilenabstand=1.30)
        els += e; y += 10
    assert y + 66 <= 975, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=34))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_234("sv", [
    "Samstag, 7.3.2026, vor der Stadtbücherei einer Stadt in Nordrhein-Westfalen: Herr Strauch leitet eine ordnungsgemäß "
    "angezeigte Mahnwache gegen die geplante Schließung der Bücherei. Die rund 20 Teilnehmer stehen direkt vor dem Eingang. "
    "Polizeihauptkommissar Nagel von der Kreispolizeibehörde löst die Versammlung auf: „Sie versperren den Eingang. Die "
    "Versammlung ist aufgelöst.“ Alle gehen nach Hause.",
    "Herr Strauch plant weitere Mahnwachen vor der Bücherei; die Polizei erklärt, sie würde wieder so handeln. Weitere "
    "Folgen hat die Auflösung nicht. 2 Wochen später erhebt Herr Strauch Klage beim Verwaltungsgericht.",
    "In der mündlichen Verhandlung hält das Gericht die Auflösung für unverhältnismäßig: Eine Verlegung um ein paar Meter "
    "hätte genügt (§ 13 Abs. 1, 2 VersG NRW).",
], "Wie lauten Antrag und Tenor? Wie begründet das Urteil das Feststellungsinteresse?")

# ===========================================================================================================================
# C1 1. Der Antrag
# ===========================================================================================================================
P1 = "1. Antrag"
folie([("antrag", f"{P1} › Auflösung erledigt"), ("antrag2", f"{P1} › Feststellungsantrag"),
       ("analog", f"{P1} › § 113 Abs. 1 Satz 4 VwGO entsprechend")], [
    *tafel("antrag", "1. Der Antrag"),
    *okz("Die Auflösung hat sich mit dem Ende", 180, "antrag", "Bold", 34),
    z("der Mahnwache erledigt.", 185, 228, beim("antrag", "Mahnwache"), "Bold", 34),
    *neinz("Aufhebung nicht mehr möglich", 300, beim("antrag", "Aufheben"), "Bold", 34),
    blk(110, 380, 1040, 190, GELB, "antrag2", [("Der Kläger beantragt,", "Bold", 33, INK),
                                              ("festzustellen, dass die Auflösung seiner Versammlung", "Regular", 32, INK),
                                              ("vom 7.3.2026 rechtswidrig gewesen ist.", "ExtraBold", 32, INK)]),
    zit("vgl. VG Gelsenkirchen, Urt. v. 19.7.2022 – 14 K 4207/19, Rn. 34 f., 52", 110, 584, "antrag2"),
    *okz("vor der Klage erledigt: § 113 Abs. 1 Satz 4 VwGO entsprechend", 650, "analog", "Bold", 31),
    zit("BVerwG, Urt. v. 24.4.2024 – 6 C 2.22, Rn. 15", 185, 696, beim("analog", "Paragraf")),
    z("Prüfungsschema: unser Video zur Fortsetzungsfeststellungsklage", 185, 750, beim("analog", "Das"), size=29,
      farbe=TEXT),
    *requisit([("antrag", ("tabler", "hourglass", 110, GELB), "erledigt", GELB),
               ("antrag2", ("tabler", "file-text", 100, GELB), "Feststellung", GELB)]),
    *stehend("ST", FX, [("antrag", "ruhig"), ("antrag2", "entschl"), ("analog", "denkt")]),
])

# ===========================================================================================================================
# C2 Umstellung bei Erledigung im Prozess: keine Klageänderung (Wortlautkarte § 264 ZPO)
# ===========================================================================================================================
w264, w264_y = wortlaut(80, 300, 1100,
                        "„Als eine Änderung der Klage ist es nicht anzusehen, wenn ohne Änderung des Klagegrundes … "
                        "2. der Klageantrag in der Hauptsache oder in Bezug auf Nebenforderungen erweitert oder "
                        "beschränkt wird; …“", "§ 264 Nr. 2 ZPO i. V. m. § 173 Satz 1 VwGO", "wl264",
                        marken=[("nicht anzusehen", beim("wl264", "keine")), ("beschränkt", beim("wl264", "beschränkt"))],
                        size=32)
folie([("umst", f"{P1} › Erledigung im Prozess: Umstellung"), ("wl264", f"{P1} › Umstellung: keine Klageänderung"),
       ("nr3", f"{P1} › Umstellung › teils § 264 Nr. 3 ZPO"), ("tb", f"{P1} › Umstellung im Tatbestand")], [
    *tafel("umst", "1. Umstellung im Prozess"),
    blk(110, 165, 1040, 110, BLAUHELL, "umst", [("Erledigung erst im Prozess, etwa ein Verbot:", "Bold", 32, INK),
                                               ("von der Anfechtung auf die Feststellung", "ExtraBold", 32, INK)]),
    *w264,
    zit("BVerwG, Urt. v. 4.12.2014 – 4 C 33.13, Rn. 11 (Beschränkung des Antrags)", 110, w264_y + 12, beim("wl264", "Bundesverwaltungsgericht")),
    z("teils: § 264 Nr. 3 ZPO", 110, w264_y + 60, "nr3", "Bold", 31),
    zit("VG Düsseldorf, Urt. v. 3.2.2022 – 29 K 78/22, Rn. 18", 480, w264_y + 66, "nr3"),
    blk(110, w264_y + 120, 1040, 140, HELL, "tb", [("Tatbestand:", "ExtraBold", 31, INK),
                                                  ("„Nachdem der Kläger zunächst die Aufhebung beantragt", "Regular", 30, INK),
                                                  ("hatte, hat er seinen Antrag auf die Feststellung umgestellt.“", "Regular", 30, INK)]),
    *requisit([("umst", ("tabler", "switch-horizontal", 110, BLAUHELL), "umstellen", BLAUHELL),
               ("wl264", ("tabler", "circle-check", 110, HELLGRUEN), "keine Klageänderung", HELLGRUEN),
               ("tb", ("tabler", "writing", 110, HELL), "Tatbestand", HELL)]),
    *stehend("BO", FX, [("umst", "ruhig"), ("wl264", "ernst"), ("tb", "froh")]),
])
assert w264_y + 270 <= 900, w264_y

# ===========================================================================================================================
# D1 2. Feststellungsinteresse im Urteil: Maßstab, Wiederholungsgefahr
# ===========================================================================================================================
P2 = "2. Feststellungsinteresse"
folie([("ffi", f"{P2} › in der Zulässigkeit"), ("ffi2", f"{P2} › Maßstab"), ("wh", f"{P2} › a) Wiederholungsgefahr"),
       ("wh2", f"{P2} › a) Wiederholungsgefahr › Versammlungsrecht"), ("wh3", f"{P2} › a) Wiederholungsgefahr › Behörde"),
       ("wh4", f"{P2} › a) Wiederholungsgefahr (+)")], [
    *tafel("ffi", "2. Feststellungsinteresse", size=44),
    z("im Urteil: Zulässigkeit, Zeitpunkt der Entscheidung", 110, 166, "ffi", "Bold", 32),
    z("Lage rechtlich, wirtschaftlich oder ideell verbessern", 110, 212, "ffi2", size=31),
    zit("BVerwG, Urt. v. 16.5.2013 – 8 C 14.12, BVerwGE 146, 303, Rn. 20", 110, 254, beim("ffi2", "rechtlich")),
    z("eine tragende Fallgruppe genügt", 110, 292, beim("ffi2", "Eine"), "Bold", 31),
    z("a) Wiederholungsgefahr", 110, 360, "wh", "ExtraBold", 35),
    z("konkret droht ein vergleichbarer Verwaltungsakt,", 150, 410, beim("wh", "konkret"), size=31),
    z("unter im Wesentlichen unveränderten Umständen", 150, 454, beim("wh", "unter"), size=31),
    zit("8 C 14.12, Rn. 21; BVerwG 6 C 2.22, Rn. 17", 150, 496, beim("wh", "unter")),
    z("Versammlung: Wille zu ähnlichen Versammlungen genügt;", 150, 546, "wh2", size=31),
    z("dasselbe Motto, derselbe Ort nicht nötig", 150, 590, beim("wh2", "Dasselbe"), size=31),
    z("und: Behörde bleibt voraussichtlich bei ihren Gründen", 150, 640, "wh3", size=31),
    zit("BVerfG, Beschl. v. 3.3.2004 – 1 BvR 461/03, BVerfGE 110, 77, Rn. 41–43", 150, 682, beim("wh3", "Behörde")),
    *plusminus("nächste Mahnwache geplant, Polizei bleibt dabei", 150, 740, "wh4", True, size=32, stil="Bold"),
    *requisit([("ffi", ("tabler", "scale", 120, WEISS), "berechtigtes Interesse", WEISS),
               ("wh", ("tabler", "repeat", 110, GELB), "Wiederholungsgefahr", GELB),
               ("wh4", ("tabler", "calendar-event", 110, HELLGRUEN), "nächste Mahnwache", HELLGRUEN)]),
    *stehend("ST", FX, [("ffi", "ruhig"), ("wh", "denkt"), ("wh4", "entschl")]),
])

# ===========================================================================================================================
# D2 b) Rehabilitation, c) tiefgreifender Grundrechtseingriff, Formulierung im Urteil
# ===========================================================================================================================
folie([("reha", f"{P2} › b) Rehabilitation"), ("reha2", f"{P2} › b) Rehabilitation (−)"),
       ("tief", f"{P2} › c) Tiefgreifender Grundrechtseingriff"), ("tief2", f"{P2} › c) Auflösung: schwerste Beeinträchtigung"),
       ("tief3", f"{P2} › Formulierung im Urteil")], [
    *tafel("reha", "2. Feststellungsinteresse", size=44),
    z("b) Rehabilitation", 110, 166, "reha", "ExtraBold", 35),
    z("Maßnahme stempelt ab: nach außen sichtbar, bis heute", 150, 214, beim("reha", "Maßnahme"), size=31),
    zit("8 C 14.12, Rn. 25", 150, 256, beim("reha", "bis")),
    *plusminus("kein ehrenrühriger Vorwurf an Herrn Strauch", 150, 296, "reha2", False, size=31, stil="Bold"),
    z("c) Tiefgreifender Grundrechtseingriff", 110, 366, "tief", "ExtraBold", 35),
    z("beides: typischerweise schnell erledigt", 150, 414, beim("tief", "beides"), size=31),
    z("und gewichtiger Eingriff", 150, 458, beim("tief", "einen"), size=31),
    zit("BVerwG, Urt. v. 24.4.2024 – 6 C 2.22, Rn. 21 f.", 150, 500, beim("tief", "einen")),
    *okz("Auflösung: schwerste mögliche Beeinträchtigung", 548, "tief2", "Bold", 31, x=195),
    z("der Versammlungsfreiheit", 195, 592, beim("tief2", "Versammlungsfreiheit"), size=31),
    zit("BVerfGE 110, 77, Rn. 37", 620, 600, beim("tief2", "Versammlungsfreiheit")),
    blk(110, 650, 1040, 170, HELL, "tief3", [("„Der Kläger hat ein berechtigtes Interesse an der", "Bold", 30, INK),
                                            ("Feststellung. Es folgt aus der Wiederholungsgefahr", "Regular", 30, INK),
                                            ("und aus dem schweren Eingriff in seine", "Regular", 30, INK),
                                            ("Versammlungsfreiheit.“", "Regular", 30, INK)]),
    zit("vgl. VG Gelsenkirchen, Urt. v. 19.7.2022 – 14 K 4207/19, Rn. 59", 110, 830, beim("tief3", "Es")),
    *requisit([("reha", ("tabler", "user-check", 110, HELLROT), "Rehabilitation", HELLROT),
               ("tief", ("tabler", "clock", 110, WEISS), "schnell erledigt", WEISS),
               ("tief2", ("tabler", "users-group", 120, HELLGRUEN), "Art. 8 GG", HELLGRUEN),
               ("tief3", ("tabler", "writing", 110, HELL), "im Urteil", HELL)]),
    *stehend("BO", FX, [("reha", "ruhig"), ("reha2", "denkt"), ("tief", "ernst"), ("tief3", "froh")]),
])

# ===========================================================================================================================
# E1 3. Der Tenor: Muster, Fall, Verpflichtungssituation
# ===========================================================================================================================
P3 = "3. Tenor"
folie([("tenor", f"{P3} › Muster, § 113 Abs. 1 Satz 4 VwGO"), ("tenor2", f"{P3} › Hauptsache im Fall"),
       ("verpfl", f"{P3} › Verpflichtungssituation")], [
    *tafel("tenor", "3. Der Tenor"),
    blk(110, 170, 1040, 140, WEISS, "tenor", [("Muster:", "Bold", 31, INK),
                                             ("„Es wird festgestellt, dass der Bescheid …", "Regular", 32, INK),
                                             ("rechtswidrig gewesen ist.“", "ExtraBold", 32, INK)]),
    zit("§ 113 Abs. 1 Satz 4 VwGO: „… daß der Verwaltungsakt rechtswidrig gewesen ist …“", 110, 322, "tenor"),
    blk(110, 380, 1040, 180, GELB, "tenor2", [("Fall:", "Bold", 31, INK),
                                             ("„Es wird festgestellt, dass die Auflösung der", "Regular", 32, INK),
                                             ("Versammlung des Klägers vom 7.3.2026", "Regular", 32, INK),
                                             ("rechtswidrig gewesen ist.“", "ExtraBold", 32, INK)]),
    zit("vgl. Tenor VG Gelsenkirchen, Urt. v. 19.7.2022 – 14 K 4207/19", 110, 572, "tenor2"),
    blk(110, 630, 1040, 140, HELLGRUEN, "verpfl", [("Verpflichtungssituation, etwa:", "Bold", 31, INK),
                                                  ("„…, dass der Beklagte verpflichtet war,", "Regular", 32, INK),
                                                  ("die beantragte Erlaubnis zu erteilen.“", "Regular", 32, INK)]),
    zit("BVerwG, Urt. v. 4.12.2014 – 4 C 33.13, Rn. 19, 21", 110, 782, "verpfl"),
    *requisit([("tenor", ("fluent-emoji-high-contrast", "balance-scale", 130, WEISS), "Tenor", WEISS),
               ("tenor2", ("tabler", "file-certificate", 110, GELB), "rechtswidrig gewesen", GELB),
               ("verpfl", ("tabler", "license", 110, HELLGRUEN), "Verpflichtung", HELLGRUEN)]),
    *paar("ST", [("tenor", "ruhig"), ("tenor2", "froh")], "BO", [("tenor", "ernst"), ("verpfl", "denkt")]),
])

# ===========================================================================================================================
# E2 Kosten § 154 Abs. 1 VwGO, vorläufige Vollstreckbarkeit § 167 VwGO, §§ 708 Nr. 11, 711 ZPO
# ===========================================================================================================================
folie([("kosten", f"{P3} › Kosten, § 154 Abs. 1 VwGO"), ("vollstr", f"{P3} › vorläufige Vollstreckbarkeit"),
       ("vollstr2", f"{P3} › vorläufige Vollstreckbarkeit › Tenor"),
       ("vollstr3", f"{P3} › vorläufige Vollstreckbarkeit › Abwendung, § 711 ZPO")], [
    *tafel("kosten", "3. Kosten und Vollstreckbarkeit", size=44),
    z("„Der unterliegende Teil trägt die Kosten des Verfahrens.“", 110, 166, beim("kosten", "Nach"), size=31),
    zit("§ 154 Abs. 1 VwGO", 110, 208, beim("kosten", "Nach")),
    blk(110, 250, 1040, 80, GELB, beim("kosten", "Der", 2), [("„Der Beklagte trägt die Kosten des Verfahrens.“", "ExtraBold", 32, INK)]),
    z("vollstreckbar nur die Kostenentscheidung, bis 1.500 €:", 110, 356, "vollstr", "Bold", 31),
    z("§ 167 VwGO i. V. m. §§ 708 Nr. 11, 711 ZPO", 110, 400, beim("vollstr", "Also"), size=31),
    zit("VG Gelsenkirchen, Urt. v. 19.7.2022 – 14 K 4207/19, Rn. 108 f.", 110, 442, beim("vollstr", "Also")),
    blk(110, 492, 1040, 80, GELB, "vollstr2", [("„Das Urteil ist wegen der Kosten vorläufig vollstreckbar.", "Bold", 31, INK)]),
    blk(110, 586, 1040, 230, GELB, "vollstr3", [("Der Beklagte darf die Vollstreckung durch Sicherheits-", "Regular", 30, INK),
                                              ("leistung in Höhe von 110 % des vollstreckbaren Betrages", "Regular", 30, INK),
                                              ("abwenden, wenn nicht der Kläger vor der Vollstreckung", "Regular", 30, INK),
                                              ("Sicherheit in Höhe von 110 % des jeweils zu", "Regular", 30, INK),
                                              ("vollstreckenden Betrages leistet.“", "Regular", 30, INK)]),
    *requisit([(beim("kosten", "Der", 2), ("tabler", "currency-euro", 110, GELB), "Kosten: Beklagter", GELB),
               ("vollstr", ("tabler", "receipt", 110, WEISS), "bis 1.500 €", WEISS),
               ("vollstr3", ("tabler", "shield-check", 110, HELLGRUEN), "Abwendung 110 %", HELLGRUEN)]),
    *stehend("ST", FX, [("kosten", "froh"), ("vollstr", "ruhig"), ("vollstr3", "denkt")]),
])

# ===========================================================================================================================
# F 4. Typische Fehler, Hilfsantrag
# ===========================================================================================================================
P4 = "4. Typische Fehler"
folie([("fehler", P4), ("f1", f"{P4} › „ist rechtswidrig“"), ("f2", f"{P4} › Aufhebungstenor"),
       ("hilfs", f"{P4} › Hilfsantrag")], [
    *tafel("fehler", "4. Typische Fehler"),
    *neinz("Fehler 1: „… rechtswidrig ist.“", 180, "f1", "Bold", 34),
    *okz("richtig: „… rechtswidrig gewesen ist.“", 240, beim("f1", "Richtig"), "ExtraBold", 34),
    z("denn der Verwaltungsakt hat sich erledigt", 185, 290, beim("f1", "denn"), size=31),
    *neinz("Fehler 2: Aufhebungstenor", 380, "f2", "Bold", 34),
    z("Einen erledigten Verwaltungsakt hebt das Gericht", 185, 430, beim("f2", "Einen"), size=31),
    z("nicht mehr auf.", 185, 474, beim("f2", "Einen"), size=31),
    blk(110, 570, 1040, 120, LILAHELL, "hilfs", [("Unsicher, ob schon erledigt?", "Bold", 32, INK),
                                               ("Feststellungsantrag hilfsweise stellen", "ExtraBold", 32, INK)]),
    *requisit([("fehler", ("tabler", "alert-triangle", 110, HELLROT), "Fehler", HELLROT),
               ("f2", ("tabler", "eraser", 110, HELLROT), "nichts mehr aufzuheben", HELLROT),
               ("hilfs", ("tabler", "corner-down-right", 110, LILAHELL), "hilfsweise", LILAHELL)]),
    *stehend("BO", FX, [("fehler", "ernst"), ("f1", "denkt"), ("hilfs", "ruhig")]),
])

# ===========================================================================================================================
# G Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Feststellungsinteresse am Tag der Entscheidung"), ("tipp2", "Klausurtipp › Mahnwache abgesagt?"),
       ("tipp3", "Klausurtipp › schwerer Eingriff trägt allein")], [
    *tafel("tipp", "Klausurtipp: Wann muss es bestehen?", fill=HELL, size=44),
    warnung_i(150, 225, "tipp", gr=26),
    z("Das Feststellungsinteresse muss noch", 200, 200, "tipp", "ExtraBold", 35),
    z("am Tag der Entscheidung bestehen.", 240, 252, beim("tipp", "am"), size=34),
    zit("BVerwG, Urt. v. 16.5.2013 – 8 C 14.12, Rn. 20", 240, 300, beim("tipp", "am")),
    linienzug([(130, 360), (1130, 360)], "tipp2", breite=3),
    *neinz("nächste Mahnwache abgesagt:", 390, "tipp2", "Bold", 34, x=240, kreuz=beim("tipp2", "entfällt")),
    z("Wiederholungsgefahr entfällt", 240, 440, beim("tipp2", "entfällt"), size=34),
    *okz("dann trägt allein der schwere Eingriff", 530, "tipp3", "Bold", 34, x=240),
    z("in die Versammlungsfreiheit", 240, 580, beim("tipp3", "in"), size=34),
    zit("BVerfGE 110, 77, Rn. 37", 240, 628, beim("tipp3", "in")),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# H Schema (Lexi), Punkt für Punkt
# ===========================================================================================================================
folie([("sch", "Schema · Urteil bei der Fortsetzungsfeststellungsklage"), ("s1", "Schema › 1. Antrag"),
       ("s2", "Schema › 2. Feststellungsinteresse"), ("s3", "Schema › 3. Tenor"), ("s4", "Schema › 4. Kosten"),
       ("s5", "Schema › 5. Vorläufige Vollstreckbarkeit")], [
    *tafel("sch", "Schema: Urteil zur FFK"),
    z("1. Antrag: Feststellung statt Aufhebung", 110, 180, "s1", size=33),
    z("2. Zulässigkeit: Feststellungsinteresse,", 110, 250, "s2", size=33),
    z("eine tragende Fallgruppe", 150, 296, beim("s2", "einer"), size=33),
    z("3. Tenor: „rechtswidrig gewesen ist“", 110, 366, "s3", size=33),
    z("4. Kosten: § 154 Abs. 1 VwGO", 110, 436, "s4", size=33),
    z("5. vorläufige Vollstreckbarkeit wegen der Kosten", 110, 506, "s5", size=33),
    *redet("LX_erklaert", FX, FB, FR + 40, "sch", "merke"),
    ns("Lexi", FX, FB, "sch", GELB, d=0.2),
])

# ===========================================================================================================================
# I Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Ein ", 0), ("erledigter", "a"), (" Verwaltungsakt", 0)], [("wird nicht ", 0), ("aufgehoben", "b"), (".", 0)]],
                750, 300, 44, "merke", {"a": beim("merke", "erledigter"), "b": beim("merke", "aufgehoben")}),
    *markertext([[("Das Gericht stellt fest,", 0)], [("dass er ", 0), ("rechtswidrig gewesen", "c"), (" ist.", 0)]],
                750, 520, 44, "m2", {"c": beim("m2", "rechtswidrig")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
