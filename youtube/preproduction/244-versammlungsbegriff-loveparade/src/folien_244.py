"""Folge 244 · Versammlungsbegriff: Ist die Love Parade eine Demo? (Art. 8 GG) – Serienstandard Open Peeps (Katzenkönig).
Fiktiver Fall (Beispiel NRW): Herr Brendel plant einen Sound-Umzug (20 Musikwagen, Techno, Motto „Mehr Raum für Kultur“, keine
Reden/Flugblätter/Transparente); Herr Zander von der Stadt: keine Versammlung, Erlaubnis, Reinigung rund 38.000 €. Danach
1. Wortlaut Art. 8 I GG, 2. Versammlungsbegriff (weit, erweitert, eng; Definition BVerfGE 104, 92; § 2 III VersG NRW; Party
oder Versammlung), 3. gemischte Veranstaltungen (Gesamtgepräge, „Bleiben Zweifel …“, BVerwG 6 C 23.06 drei Schritte, Love
Parade und Gegenveranstaltung), 4. Fall und Folgen (Sondernutzung, StrWG NRW), 5. Gegenfall (Frau Lechner), Klausurtipp,
Schema, Merksatz mit Lexi.
Szenen laut ../SZENENPLAN.md. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/feld/requisit/paar/
hand/plakat als eigene Kopie aus Folge 234 (gemeinsame Dateien unverändert); neu: fassade(), musikwagen().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut nach gesetze-im-internet.de bzw. recht.nrw.de, Abruf 07.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_244/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_244/" in n:
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
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 07.10.2026 (Folge 244)), als Zitat mit Normangabe; der
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
NAME = {"BR": "Herr Brendel", "ZA": "Herr Zander", "LE": "Frau Lechner"}
NFARBE = {"BR": HELLROT, "ZA": HELLGRUEN, "LE": BLAUHELL}
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



# --- Folge 244: Größen, Szenenbausteine ------------------------------------------------------------------------------
GROESSE = {"BR": 1.0, "ZA": 0.97, "LE": 0.94}


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
FASSADE2 = (232, 214, 190, 255)


def fassade(cue, x0, x1, oben, fill=FASSADE, fenster=((40, 150), (160, 150), (40, 300), (160, 300)), tuer=None, bis=None):
    """Hausfassade (programmatisch): Dachkante, Fenster, optional Tür (x-Versatz); Palette, Tuschekontur."""
    w, h = x1 - x0, BODEN - oben
    s = 2
    im = Image.new("RGBA", ((w + 12) * s, (h + 12) * s))
    dr = ImageDraw.Draw(im)
    o = 6 * s
    dr.rectangle((o - 4 * s, o, o + (w + 4) * s, o + 22 * s), fill=INK)
    dr.rectangle((o, o + 22 * s, o + w * s, o + h * s), fill=INK)
    dr.rectangle((o + 5 * s, o + 22 * s, o + (w - 5) * s, o + h * s), fill=fill)
    for fx, fy in fenster:
        dr.rounded_rectangle((o + fx * s, fy * s, o + (fx + 80) * s, (fy + 96) * s), 6 * s, fill=INK)
        dr.rounded_rectangle((o + (fx + 5) * s, (fy + 5) * s, o + (fx + 75) * s, (fy + 91) * s), 4 * s, fill=BLAUHELL)
    if tuer is not None:
        dr.rounded_rectangle((o + tuer * s, (h - 180) * s, o + (tuer + 120) * s, (h + 6) * s), 8 * s, fill=INK)
        dr.rounded_rectangle((o + (tuer + 6) * s, (h - 174) * s, o + (tuer + 114) * s, (h + 6) * s), 5 * s, fill=HOLZ)
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    return El(im, x0 - 6, oben - 6, cue, "cut", 0.0, bis, name="fassade")


def musikwagen(cx, cue, breite=420, fill=GELB, bis=None, anim="pop"):
    """Musikwagen: Tabler-Icon „truck“ (MIT) mit Palettenfüllung, darauf zwei Lautsprecher (Tabler „device-speaker“)."""
    w = ficon("tabler", "truck", cx, BODEN + 4, breite, cue, fuell=fill, bis=bis, anim=anim)
    top = w.y + w.sprite.height * 0.16
    l1 = ficon("tabler", "device-speaker", cx - breite * 0.22, top, 70, cue, fuell=WEISS, bis=bis, anim=anim)
    l2 = ficon("tabler", "device-speaker", cx - breite * 0.02, top, 70, cue, fuell=WEISS, bis=bis, anim=anim)
    return [w, l1, l2]


def zit2(text, x, y, cue, **k):
    return zit(text, x, y, cue, **k)


# ===========================================================================================================================
# A1 Fall: der Sound-Umzug (Plan), Herr Zander von der Stadt, Herr Brendel
# ===========================================================================================================================
FH_ = 440
TAX, TBX, BRX, ZAX = 720, 890, 1170, 1700
NULL = ("fall", -round(T_("fall"), 3))
TANZ = beim("wagen", "tausende")
FALL_PFADE = [(NULL, "Fall · Frühjahr in einer Stadt in NRW"), ("brendel", "Fall · Der geplante Sound-Umzug"),
              ("motto", "Fall · Als Versammlung, mit Motto"), ("zander", "Fall · Die Stadt antwortet"),
              ("za1", "Fall · Keine Versammlung?"), ("br1", "Fall · „Wir haben doch ein Motto!“")]
folie(FALL_PFADE, [
    hart(boden(NULL)),
    hart(fassade(NULL, 60, 360, 380, fenster=((40, 120), (170, 120), (40, 250), (170, 250)))),
    hart(fassade(NULL, 380, 640, 440, fill=FASSADE2, fenster=((30, 110), (150, 110)), tuer=70)),
    hart(ficon("tabler", "sun", 1830, 150, 96, NULL, fuell=GELB, anim="cut")),
    hart(pl("Frühjahr in einer Stadt in Nordrhein-Westfalen", 70, 30, NULL, fill=GELB, size=32)),
    # Herr Brendel plant den Sound-Umzug
    *fig("BR", BRX, BODEN, FH_, [(NULL, "ruhig"), ("brendel", "froh"), ("motto", "entschl"), ("zander", "denkt_r"),
                                 ("za1", "schreck_r")], bis="br1", erst="cut"),
    *redet("BR_redet_r", BRX, BODEN, FH_, "br1", "frage"),
    ns(NAME["BR"], BRX, BODEN, NULL, NFARBE["BR"], anim="cut"),
    pl("Plan für den Sommer: Sound-Umzug durch die Innenstadt", 70, 94, beim("brendel", "plant"), fill=WEISS, size=30,
       bis="motto"),
    *musikwagen(400, "wagen", bis=None),
    pl("20 Musikwagen, Techno, Tausende Tanzende", 70, 158, "wagen", fill=GELB, size=30, bis="motto"),
    ficon("tabler", "music", 250, 330, 70, beim("wagen", "Techno"), fuell=WEISS),
    ficon("tabler", "music", 560, 300, 60, beim("wagen", "Techno"), fuell=WEISS),
    *fig("TA", TAX, BODEN, 400, [(TANZ, "froh"), ("br1", "cute")]),
    *fig("TB", TBX, BODEN, 410, [(TANZ, "froh"), ("br1", "cute")]),
    # Anmeldung als Versammlung mit Motto, ohne Reden, Flugblätter, Transparente
    ficon("tabler", "file-text", BRX, 360, 96, "motto", fuell=WEISS, bis="zander"),
    pl("als Versammlung, Motto: „Mehr Raum für Kultur“", 70, 94, "motto", fill=WEISS, size=30, bis="zander"),
    ficon("tabler", "ban", BRX + 95, 360, 64, beim("motto", "Reden"), fuell=HELLROT, bis="zander"),
    pl("keine Reden, Flugblätter oder Transparente", 70, 158, beim("motto", "Reden"), fill=HELLROT, size=30, bis="zander"),
    # Herr Zander von der Stadt
    *fig("ZA", ZAX, BODEN, hh("ZA", FH_), [("zander", "ernst")], bis="za1"),
    *redet("ZA_spricht", ZAX, BODEN, hh("ZA", FH_), "za1", "br1"),
    *fig("ZA", ZAX, BODEN, hh("ZA", FH_), [("br1", "streng")], erst="cut"),
    ns(NAME["ZA"], ZAX, BODEN, "zander", NFARBE["ZA"], d=0.1),
    pl("Herr Zander von der Stadt", 70, 94, beim("zander", "Herr"), fill=HELLGRUEN, size=30),
    blase("sprech", 700, 270, "za1", 1330, 215, inhalt=["Das ist keine Versammlung,", "sondern eine Party. Sie brauchen",
                                                       "eine Erlaubnis und zahlen die", "Reinigung: rund 38.000 €."],
          textsize=29, figur=("ZA_spricht", ZAX, BODEN, hh("ZA", FH_)), bis="br1"),
    ficon("tabler", "bucket", 1440, 790, 90, beim("za1", "Reinigung"), fuell=BLAUHELL),
    pl("Reinigung: rund 38.000 €", 70, 158, beim("za1", "Reinigung"), fill=BLAUHELL, size=30),
    blase("sprech", 560, 190, "br1", 1330, 210, inhalt=["Wir haben doch ein Motto!", "Als Demo zahlt die Stadt."], textsize=31,
          figur=("BR_redet_r", BRX, BODEN, FH_)),
])

# ===========================================================================================================================
# A2 Die Frage, Love-Parade-Beschluss
# ===========================================================================================================================
folie([("frage", "Die Frage · Versammlung im Sinne von Art. 8 GG?"), ("frage2", "Die Frage · Der Love-Parade-Beschluss")], [
    *tafel("frage", "Die Frage"),
    z("Ist der Sound-Umzug eine Versammlung", 110, 190, "frage", "Bold", 38),
    z("im Sinne von Art. 8 GG?", 110, 244, "frage", "Bold", 38),
    blk(110, 340, 1040, 200, GELB, "frage2", [("Fall: Love Parade", "ExtraBold", 37, INK),
                                             ("Berliner Polizei gegen die Veranstalterin", "Regular", 33, INK),
                                             ("BVerfG im Juli 2001, im Eilverfahren", "Bold", 33, INK)]),
    zit("BVerfG (K), Beschl. v. 12.7.2001 – 1 BvQ 28/01, 1 BvQ 30/01", 110, 556, beim("frage2", "Das")),
    *requisit([("frage", ("tabler", "help", 110, GELB), "Versammlung?", GELB),
               ("frage2", ("fluent-emoji-high-contrast", "balance-scale", 130, WEISS), "BVerfG 2001", WEISS)]),
    *paar("BR", [("frage", "denkt"), ("frage2", "ernst")], "ZA", [("frage", "ruhig"), ("frage2", "denkt")]),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_244(cue, absaetze, frage):
    els = [karte(140, 50, 1640, 930, cue, fill=HELL), titel("Sachverhalt", 210, 84, cue, 56)]
    y = 180
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=36, zeilenabstand=1.30)
        els += e; y += 10
    assert y + 66 <= 975, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=34))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_244("sv", [
    "Frühjahr in einer Stadt in Nordrhein-Westfalen: Herr Brendel plant für den Sommer einen Sound-Umzug durch die "
    "Innenstadt mit 20 Musikwagen, Techno und Tausenden Tanzenden. Er will ihn als Versammlung durchführen, Motto: „Mehr "
    "Raum für Kultur“. Reden, Flugblätter oder Transparente sind nicht geplant.",
    "Herr Zander von der Stadt hält den Umzug für keine Versammlung: Herr Brendel brauche eine Erlaubnis für die Nutzung "
    "der Straße und müsse die Reinigung tragen, rund 38.000 €.",
    "Herr Brendel: „Wir haben doch ein Motto! Als Demo zahlt die Stadt.“",
], "Ist der Sound-Umzug eine Versammlung im Sinne von Art. 8 Abs. 1 GG?")

# ===========================================================================================================================
# C 1. Der Wortlaut (Wortlautkarte Art. 8 Abs. 1 GG)
# ===========================================================================================================================
w8, w8_y = wortlaut(80, 190, 1100, "„Alle Deutschen haben das Recht, sich ohne Anmeldung oder Erlaubnis friedlich und ohne "
                    "Waffen zu versammeln.“", "Art. 8 Abs. 1 GG", "art8",
                    marken=[("versammeln", beim("wl8", "versammeln"))], size=36)
folie([("art8", "1. Wortlaut · Art. 8 Abs. 1 GG"), ("nichtdef", "1. Wortlaut · keine Definition")], [
    *tafel("art8", "1. Der Wortlaut"),
    *w8,
    z("Was eine Versammlung ist,", 110, w8_y + 50, "nichtdef", "ExtraBold", 36),
    z("sagt Art. 8 nicht.", 110, w8_y + 102, "nichtdef", "ExtraBold", 36),
    *requisit([("art8", ("tabler", "book", 110, WEISS), "Art. 8 Abs. 1 GG", WEISS),
               ("nichtdef", ("tabler", "help", 110, GELB), "Definition?", GELB)]),
    *stehend("BR", FX, [("art8", "ruhig"), ("wl8", "froh"), ("nichtdef", "denkt")]),
])
assert w8_y + 160 <= 900, w8_y

# ===========================================================================================================================
# D1 2. Der Versammlungsbegriff: weit, erweitert, eng; Definition des BVerfG
# ===========================================================================================================================
P2 = "2. Versammlungsbegriff"
wdef, wdef_y = wortlaut(80, 470, 1100, "„Versammlungen im Sinne des Art. 8 GG sind … örtliche Zusammenkünfte mehrerer Personen "
                        "zur gemeinschaftlichen, auf die Teilhabe an der öffentlichen Meinungsbildung gerichteten Erörterung "
                        "oder Kundgebung.“", "BVerfGE 104, 92 <104>, Rn. 39 (Sitzblockaden III)", "def",
                        marken=[("örtliche", beim("def", "örtliche")), ("mehrerer Personen", beim("def", "mehrerer")),
                                ("öffentlichen Meinungsbildung", beim("def", "öffentlichen"))], size=30)
ENG = beim("eng", "Bundesverfassungsgericht")
folie([("begriff", f"{P2} · drei Ansichten"), ("weit", f"{P2} › weiter Begriff"), ("erweit", f"{P2} › erweiterter Begriff"),
       ("eng", f"{P2} › enger Begriff (BVerfG)"), ("def", f"{P2} › Definition des BVerfG")], [
    *tafel("begriff", "2. Der Versammlungsbegriff", size=44),
    *neinz("weit: jeder gemeinsame Zweck, auch Tanzen", 170, "weit", "Bold", 32, kreuz=ENG),
    zit("in diese Richtung: Veranstalterin der Love Parade, BVerfG (K) 1 BvQ 28/01, Rn. 10", 185, 214,
        beim("weit", "In")),
    *neinz("erweitert: gemeinsame Meinungsbildung oder", 266, "erweit", "Bold", 32, kreuz=ENG),
    z("Meinungsäußerung, gleich zu welchem Thema", 185, 310, beim("erweit", "Meinungsäußerung"), "Bold", 32),
    *okz("eng (BVerfG): öffentliche Meinungsbildung", 380, ENG, "ExtraBold", 34),
    *wdef,
    *requisit([("begriff", ("tabler", "users-group", 120, WEISS), "3 Ansichten", WEISS),
               ("weit", ("tabler", "music", 100, GELB), "weit", GELB),
               ("erweit", ("tabler", "messages", 110, LILAHELL), "erweitert", LILAHELL),
               ("eng", ("tabler", "speakerphone", 110, HELLGRUEN), "eng", HELLGRUEN)]),
    *stehend("ZA", FX, [("begriff", "ruhig"), ("weit", "denkt"), ("eng", "ernst"), ("def", "froh")]),
])
assert wdef_y <= 900, wdef_y

# ===========================================================================================================================
# D2 Warum eng? § 2 Abs. 3 VersG NRW
# ===========================================================================================================================
wnrw, wnrw_y = wortlaut(80, 400, 1100, "„Versammlung im Sinne dieses Gesetzes ist eine örtliche Zusammenkunft von mindestens drei "
                        "Personen zur gemeinschaftlichen, überwiegend auf die Teilhabe an der öffentlichen Meinungsbildung "
                        "gerichteten Erörterung oder Kundgebung.“", "§ 2 Abs. 3 VersG NRW", "nrw",
                        marken=[("mindestens drei", beim("nrw", "mindestens")), ("überwiegend", beim("nrw", "überwiegend"))],
                        size=30)
folie([("grund", f"{P2} › Warum eng?"), ("nrw", f"{P2} › NRW: § 2 Abs. 3 VersG NRW")], [
    *tafel("grund", "2. Warum eng?"),
    *okz("Art. 8 schützt besonders stark: Er dient", 180, "grund", "Bold", 33),
    z("der öffentlichen Meinungsbildung.", 185, 226, beim("grund", "Meinungsbildung"), "Bold", 33),
    zit("BVerfG (K) 1 BvQ 28/01, Rn. 16; BVerfGE 104, 92, Rn. 38 f.", 185, 272, beim("grund", "Meinungsbildung")),
    *neinz("Ein beliebiger gemeinsamer Zweck reicht nicht.", 320, beim("grund", "Ein"), "Bold", 33),
    *wnrw,
    *requisit([("grund", ("tabler", "speakerphone", 110, HELLGRUEN), "öffentliche Meinungsbildung", HELLGRUEN),
               ("nrw", ("tabler", "book", 110, WEISS), "Nordrhein-Westfalen", WEISS)]),
    *stehend("BR", FX, [("grund", "ernst"), ("nrw", "denkt")]),
])
assert wnrw_y <= 900, wnrw_y

# ===========================================================================================================================
# D3 Party oder Versammlung? Musik und Tanz als Mittel
# ===========================================================================================================================
TX1, TX2 = 1420, 1700
folie([("party", f"{P2} › keine Massenparty"), ("mittel", f"{P2} › Musik und Tanz als Mittel")], [
    *tafel("party", "2. Party oder Versammlung?"),
    *neinz("nicht: Volksfeste, Massenpartys,", 190, "party", "Bold", 34),
    z("bloße Zurschaustellung eines Lebensgefühls", 185, 238, beim("party", "auch"), size=33),
    zit("BVerfG (K) 1 BvQ 28/01, Rn. 18", 185, 286, beim("party", "auch")),
    *okz("aber: Musik und Tanz als Mittel,", 380, "mittel", "Bold", 34),
    z("um auf die öffentliche Meinung einzuwirken", 185, 428, beim("mittel", "Wer"), size=33),
    zit("BVerfG (K) 1 BvQ 28/01, Rn. 20; BVerwG 6 C 23.06, Rn. 15", 185, 476, beim("mittel", "Wer")),
    *requisit([("party", ("tabler", "confetti", 110, HELLROT), "Massenparty", HELLROT),
               ("mittel", ("tabler", "speakerphone", 110, HELLGRUEN), "Musik als Mittel", HELLGRUEN)]),
    *rechts_frei(fig("TA", TX1, FB, FR - 20, [("party", "froh"), ("mittel", "cute")]), 1200),
    *rechts_frei(fig("TB", TX2, FB, FR - 10, [("party", "froh"), ("mittel", "cute")]), 1200),
])

# ===========================================================================================================================
# E1 3. Gemischte Veranstaltungen: Gesamtgepräge, „Bleiben Zweifel …“ (Love-Parade-Beschluss, Rn. 25)
# ===========================================================================================================================
P3 = "3. Gemischte Veranstaltungen"
wzw, wzw_y = wortlaut(80, 450, 1100, "„Bleiben Zweifel, so bewirkt der hohe Rang der Versammlungsfreiheit, dass die Veranstaltung "
                      "wie eine Versammlung behandelt wird.“", "BVerfG (K), Beschl. v. 12.7.2001 – 1 BvQ 28/01, Rn. 25",
                      "zweifel", marken=[("Zweifel", beim("zweifel", "Zweifel")), ("wie eine Versammlung", beim("zweifel", "wie"))],
                      size=33)
folie([("gemischt", f"{P3}"), ("gepraege", f"{P3} › Gesamtgepräge"), ("zweifel", f"{P3} › im Zweifel Versammlung")], [
    *tafel("gemischt", "3. Gemischte Veranstaltungen", size=44),
    *neinz("Meinungen nur bei Gelegenheit: reicht nicht", 180, "gemischt", "Bold", 33, kreuz=beim("gemischt", "nicht")),
    zit("BVerfG (K) 1 BvQ 28/01, Rn. 22", 185, 226, beim("gemischt", "nicht")),
    z("Entscheidend: das Gesamtgepräge", 110, 290, "gepraege", "ExtraBold", 35),
    z("Meinungsbildung oder Spaß im Vordergrund?", 110, 340, beim("gepraege", "Steht"), size=33),
    zit("ebd., Rn. 25", 110, 386, beim("gepraege", "Steht")),
    *wzw,
    *requisit([("gemischt", ("tabler", "confetti", 110, GELB), "Party mit Motto?", GELB),
               ("gepraege", ("fluent-emoji-high-contrast", "balance-scale", 130, WEISS), "Gesamtgepräge", WEISS),
               ("zweifel", ("tabler", "help", 110, HELLGRUEN), "im Zweifel: Versammlung", HELLGRUEN)]),
    *stehend("ZA", FX, [("gemischt", "ruhig"), ("gepraege", "denkt"), ("zweifel", "ernst")]),
])
assert wzw_y <= 900, wzw_y

# ===========================================================================================================================
# E2 Gesamtschau in drei Schritten (BVerwG 6 C 23.06, Rn. 17 f.)
# ===========================================================================================================================
folie([("schritte", f"{P3} › Gesamtschau in 3 Schritten"), ("sa", f"{P3} › 1. Meinungsbildung erfassen"),
       ("sb", f"{P3} › 2. Musik, Tanz, Unterhaltung"), ("sc", f"{P3} › 3. Vergleich")], [
    *tafel("schritte", "3. Gesamtschau in 3 Schritten", size=44),
    zit("BVerwG, Urt. v. 16.5.2007 – 6 C 23.06, Rn. 17 f.", 110, 164, "schritte"),
    z("1. Elemente der Meinungsbildung erfassen", 110, 220, "sa", "Bold", 34),
    z("vorgeschobene Anliegen bleiben außen vor,", 150, 268, beim("sa", "Nur"), size=32),
    z("dabei ist Zurückhaltung geboten", 150, 312, beim("sa", "dabei"), size=32),
    z("2. Gewicht von Musik, Tanz, Unterhaltung", 110, 386, "sb", "Bold", 34),
    z("3. Vergleich: Was überwiegt?", 110, 460, "sc", "Bold", 34),
    z("Sicht eines durchschnittlichen Betrachters", 150, 508, beim("sc", "Sicht"), size=32),
    blk(110, 580, 1040, 130, GELB, beim("sc", "Lässt"), [("nicht zweifelsfrei festzustellen:", "Bold", 33, INK),
                                                       ("wie eine Versammlung behandeln", "ExtraBold", 34, INK)]),
    *requisit([("schritte", ("tabler", "list-numbers", 110, WEISS), "3 Schritte", WEISS),
               ("sb", ("tabler", "music", 100, GELB), "Musik, Tanz", GELB),
               ("sc", ("fluent-emoji-high-contrast", "balance-scale", 130, WEISS), "Was überwiegt?", WEISS)]),
    *stehend("BR", FX, [("schritte", "ruhig"), ("sa", "denkt"), ("sc", "ernst")]),
])

# ===========================================================================================================================
# E3 Love Parade und Gegenveranstaltung (2001)
# ===========================================================================================================================
folie([("lp", f"{P3} › Love Parade"), ("gv", f"{P3} › Gegenveranstaltung"), ("gv2", f"{P3} › wie eine Versammlung")], [
    *tafel("lp", "3. Zwei Techno-Umzüge, 2001", size=44),
    blk(110, 170, 1040, 180, HELLROT, "lp", [("Love Parade", "ExtraBold", 35, INK),
                                            ("BVerfG: tragfähig, sie nicht als", "Regular", 32, INK),
                                            ("Versammlung einzuordnen", "Regular", 32, INK)]),
    zit("BVerfG (K), Beschl. v. 12.7.2001 – 1 BvQ 28/01, 1 BvQ 30/01, Rn. 19, 26", 110, 362, "lp"),
    blk(110, 430, 1040, 130, HELLGRUEN, "gv", [("Gegenveranstaltung, ebenfalls Techno:", "ExtraBold", 33, INK),
                                              ("Spruchbänder, Flugblätter, Podiumsdiskussion", "Regular", 32, INK)]),
    *okz("wie eine Versammlung zu behandeln", 590, "gv2", "ExtraBold", 34),
    zit("BVerwG, Urt. v. 16.5.2007 – 6 C 23.06, Rn. 20–25", 185, 640, "gv2"),
    *requisit([("lp", ("tabler", "music", 100, HELLROT), "Love Parade", HELLROT),
               ("gv", ("tabler", "files", 100, HELLGRUEN), "Flugblätter", HELLGRUEN),
               ("gv2", ("tabler", "speakerphone", 110, HELLGRUEN), "Versammlung", HELLGRUEN)]),
    *paar("BR", [("lp", "ernst"), ("gv", "denkt")], "ZA", [("lp", "froh"), ("gv2", "ruhig")]),
])

# ===========================================================================================================================
# F1 4. Der Fall: Sound-Umzug
# ===========================================================================================================================
P4 = "4. Der Fall"
folie([("subs", f"{P4} · Sound-Umzug"), ("sub1", f"{P4} › Zusammenkunft"), ("sub2", f"{P4} › Was prägt den Umzug?"),
       ("sub3", f"{P4} › Motto vorgeschoben"), ("erg", f"{P4} › Ergebnis: keine Versammlung")], [
    *tafel("subs", "4. Der Fall: Sound-Umzug"),
    *okz("viele Menschen an einem Ort", 180, "sub1", "Bold", 34),
    z("prägend: 20 Musikwagen, Techno, Tanzen", 110, 256, "sub2", "Bold", 34),
    *neinz("Meinungsbildung: nur das Motto auf dem Papier", 320, beim("sub2", "Für"), "Bold", 32),
    z("keine Reden, keine Flugblätter, keine Transparente", 185, 366, beim("sub2", "keine"), size=31),
    blk(110, 430, 1040, 80, HELL, "sub3", [("Herr Brendel selbst: Die Stadt soll zahlen.", "Bold", 33, INK)]),
    *neinz("Motto vorgeschoben, Spaß klar im Vordergrund", 540, beim("sub3", "Das"), "Bold", 32),
    *plusminus("Ergebnis: keine Versammlung", 110, 630, "erg", False, size=40, stil="ExtraBold"),
    *requisit([("subs", ("tabler", "truck", 140, GELB), "Sound-Umzug", GELB),
               ("sub3", ("tabler", "currency-euro", 110, GELB), "Die Stadt soll zahlen", GELB),
               ("erg", ("tabler", "ban", 110, HELLROT), "keine Versammlung", HELLROT)]),
    *stehend("BR", FX, [("subs", "ruhig"), ("sub2", "froh"), ("sub3", "sorge"), ("erg", "muede")]),
])

# ===========================================================================================================================
# F2 Folgen: Sondernutzung (Straßenrecht NRW)
# ===========================================================================================================================
folie([("folge", f"{P4} › Folgen für die Kosten"), ("sonder", f"{P4} › Sondernutzung: Erlaubnis"),
       ("kost", f"{P4} › Auflagen und Kosten"), ("versfrei", f"{P4} › Versammlung: erlaubnisfrei"),
       ("land", f"{P4} › Landesrecht")], [
    *tafel("folge", "4. Folgen: Straßenrecht"),
    z("Sondernutzung der Straße: Erlaubnis nötig", 110, 176, "sonder", "Bold", 34),
    zit("§ 18 Abs. 1 StrWG NRW; bei Erlaubnis nach § 29 Abs. 2 StVO: § 21 StrWG NRW", 110, 222, "sonder"),
    z("so auch bei der Love Parade", 110, 272, beim("sonder", "So"), size=32),
    zit("BVerfG (K) 1 BvQ 28/01, Rn. 9", 560, 280, beim("sonder", "So")),
    z("Auflagen und Ersatz zusätzlicher Kosten,", 110, 346, "kost", "Bold", 34),
    z("also auch die Reinigung", 110, 394, beim("kost", "Reinigung"), "ExtraBold", 34),
    zit("§ 18 Abs. 2 Satz 2, Abs. 3 StrWG NRW", 110, 442, "kost"),
    blk(110, 500, 1040, 80, HELLGRUEN, "versfrei", [("Versammlung: keine Erlaubnis für die Straße", "ExtraBold", 33, INK)]),
    zit("§ 11 VersG NRW; BVerfG (K) 1 BvQ 28/01, Rn. 17", 110, 594, "versfrei"),
    blk(110, 660, 1040, 80, LILAHELL, "land", [("Landesrecht, hier NRW: in deinem Land ggf. andere Norm", "Bold", 31, INK)]),
    *requisit([("folge", ("tabler", "currency-euro", 110, WEISS), "Kosten?", WEISS),
               ("sonder", ("tabler", "road", 110, WEISS), "Sondernutzung", WEISS),
               ("kost", ("tabler", "bucket", 100, BLAUHELL), "Reinigung", BLAUHELL),
               ("versfrei", ("tabler", "speakerphone", 110, HELLGRUEN), "erlaubnisfrei", HELLGRUEN),
               ("land", ("tabler", "map-pin", 100, LILAHELL), "NRW", LILAHELL)]),
    *paar("BR", [("folge", "denkt"), ("kost", "sorge")], "ZA", [("folge", "ruhig"), ("sonder", "ernst"), ("land", "froh")]),
])

# ===========================================================================================================================
# G 5. Gegenfall: Frau Lechner, Umzug gegen die Schließung des Jugendzentrums
# ===========================================================================================================================
P5 = "5. Gegenfall"
LEX, TCX = 1420, 1130
folie([("gegen", P5), ("lechner", f"{P5} · Umzug für das Jugendzentrum"), ("reden", f"{P5} › Reden, Transparente, Flugblätter"),
       ("le1", f"{P5} › Frau Lechner"), ("gegen2", f"{P5} › Musik als Mittel"), ("gegen3", f"{P5} › Versammlung (+)")], [
    hart(boden("gegen")),
    hart(fassade("gegen", 60, 560, 420, fill=FASSADE2, fenster=((40, 110), (370, 110)), tuer=190)),
    pl("5. Der Gegenfall", 70, 30, "gegen", fill=BLAUHELL, size=30, bis="lechner"),
    pl("Jugendzentrum", 310, 352, beim("lechner", "Jugendzentrums"), fill=GELB, size=32, anker="m"),
    hart(ficon("tabler", "sun", 1830, 150, 96, "gegen", fuell=GELB, anim="cut")),
    pl("Gegenfall: Umzug gegen die Schließung des Jugendzentrums", 70, 30, "lechner", fill=BLAUHELL, size=30),
    *musikwagen(760, beim("lechner", "Auch"), breite=360, fill=TUERKIS_),
    pl("auch hier: Musikwagen", 70, 94, beim("lechner", "Auch"), fill=WEISS, size=30, bis="gegen2"),
    plakat("Jugendzentrum bleibt!", TCX - 40, 320, 700, "reden"),
    *fig("TC", TCX, BODEN, 420, [("reden", "froh"), ("gegen3", "entschl")]),
    *fig("LE", LEX, BODEN, hh("LE", FH_), [("lechner", "froh")], bis="le1"),
    *redet("LE_spricht", LEX, BODEN, hh("LE", FH_), "le1", "gegen2"),
    *fig("LE", LEX, BODEN, hh("LE", FH_), [("gegen2", "entschl"), ("gegen3", "freut")], erst="cut"),
    ns(NAME["LE"], LEX, BODEN, "lechner", NFARBE["LE"], d=0.1),
    ficon("tabler", "microphone", 1580, 640, 70, "reden", fuell=WEISS),
    ficon("tabler", "files", 1700, 760, 90, beim("reden", "Flugblätter"), fuell=WEISS),
    pl("Reden, Transparente, Flugblätter", 70, 158, "reden", fill=HELLGRUEN, size=30, bis="gegen2"),
    blase("sprech", 520, 180, "le1", 1215, 215, inhalt=["Mit Musik hören uns", "viel mehr Leute zu!"], textsize=32,
          figur=("LE_spricht", LEX, BODEN, hh("LE", FH_)), bis="gegen2"),
    pl("Musik als Mittel: Gesamtgepräge ist die Meinungskundgabe", 70, 94, "gegen2", fill=GELB, size=30),
    pl("Versammlung, geschützt durch Art. 8 GG (+)", 70, 158, "gegen3", fill=HELLGRUEN, size=30),
])

# ===========================================================================================================================
# H Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Versammlungsbegriff ausführlich"), ("tipp2", "Klausurtipp › erfassen, gewichten, vergleichen"),
       ("tipp3", "Klausurtipp › Anhaltspunkte für „vorgeschoben“")], [
    *tafel("tipp", "Klausurtipp: Musik im Spiel?", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Versammlungsbegriff im Schutzbereich prüfen,", 200, 200, "tipp", "ExtraBold", 34),
    z("ausführlich, wenn Musik im Spiel ist", 240, 252, beim("tipp", "und"), size=34),
    linienzug([(130, 320), (1130, 320)], "tipp2", breite=3),
    *okz("Elemente einzeln erfassen, gewichten, vergleichen", 350, "tipp2", "Bold", 33, x=240),
    linienzug([(130, 430), (1130, 430)], "tipp3", breite=3),
    *neinz("nicht einfach: „Das Motto ist vorgeschoben.“", 460, "tipp3", "Bold", 33, x=240),
    *okz("dafür Anhaltspunkte im Sachverhalt", 530, beim("tipp3", "Dafür"), "Bold", 33, x=240),
    zit("BVerwG, Urt. v. 16.5.2007 – 6 C 23.06, Rn. 17", 240, 580, beim("tipp3", "Dafür")),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# I Schema (Lexi), Punkt für Punkt
# ===========================================================================================================================
folie([("sch", "Schema · Art. 8 Abs. 1 GG"), ("k1", "Schema › I. Schutzbereich: Versammlung"),
       ("k1c", "Schema › I. gemischte Veranstaltung"), ("k2", "Schema › I. friedlich und ohne Waffen"),
       ("k3", "Schema › II. Eingriff"), ("k4", "Schema › III. Rechtfertigung")], [
    *tafel("sch", "Schema: Art. 8 Abs. 1 GG"),
    z("I. Schutzbereich", 110, 176, "k1", "ExtraBold", 35),
    z("1. Versammlung: örtliche Zusammenkunft", 150, 230, beim("k1", "Örtliche"), size=32),
    z("mehrerer Personen", 190, 274, beim("k1", "mehrerer"), size=32),
    z("Zweck: Teilhabe an der öffentlichen Meinungsbildung", 190, 320, "k1b", size=32),
    z("gemischt: Gesamtgepräge, im Zweifel Versammlung", 190, 366, "k1c", size=32),
    z("2. friedlich und ohne Waffen", 150, 420, "k2", size=32),
    z("II. Eingriff", 110, 490, "k3", "ExtraBold", 35),
    z("III. Rechtfertigung", 110, 560, "k4", "ExtraBold", 35),
    *redet("LX_erklaert", FX, FB, FR + 40, "sch", "merke"),
    ns("Lexi", FX, FB, "sch", GELB, d=0.2),
])

# ===========================================================================================================================
# J Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Musik darf das ", 0), ("Mittel", "a"), (" sein,", 0)], [("aber nicht der ganze ", 0), ("Zweck", "b"), (".", 0)]],
                750, 300, 44, "merke", {"a": beim("merke", "Mittel"), "b": beim("merke", "Zweck")}),
    *markertext([[("Es zählt das ", 0), ("Gesamtgepräge", "c"), (",", 0)], [("und im Zweifel gilt die Veranstaltung", 0)],
                 [("als ", 0), ("Versammlung", "d"), (".", 0)]],
                750, 510, 44, "m2", {"c": beim("m2", "Gesamtgepräge"), "d": beim("m2", "Versammlung")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
