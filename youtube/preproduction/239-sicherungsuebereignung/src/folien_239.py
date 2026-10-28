"""Folge 239 · Sicherungsübereignung: Du fährst das Auto, es gehört der Bank – Serienstandard Open Peeps (Katzenkönig).
Fiktiver Fall: Sieglinde (Malerbetrieb) braucht einen neuen Transporter; ihre Bank (ohne Namen, keine echte Marke) leiht ihr
30.000 €, Bankberater Herr Lohberg verlangt den Transporter als Sicherheit; Nutzung, solange sie die Raten zahlt. Kauf beim
Händler, Zahlung mit dem Kredit, Übergabe; danach Sicherungsvertrag mit Übereignung; Sieglinde fährt den Wagen täglich.
Szenen laut ../SZENENPLAN.md. Drei Handlungsgeräusche (Transporter fährt vor, Unterschrift, Pfandsiegel;
../geraeusche_herkunft.json). Transporter, Büro, Hof, Lagerhallen und Pfandsiegel als Grundformen, keine Marken.
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/pkt
als eigene Kopie aus Folge 236 (gemeinsame Dateien unverändert); neu: transporter(), buero(), hof(), hallen(), pfandsiegel().
Wortlautkarten wörtlich nach gesetze-im-internet.de (Abruf 07.10.2026): § 929 S. 1 BGB (Auszug), § 930 BGB, § 868 BGB
(Auszug), § 51 Nr. 1 InsO (Auszug). Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_239/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_239/" in n:
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 124/149/196) ------------------------------------
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
NAME = {"SG": "Sieglinde", "LO": "Herr Lohberg", "GV": "Gerichtsvollzieherin"}
NFARBE = {"SG": BLAU, "LO": GRUEN, "GV": LILA}


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
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
G0 = 900                                     # Boden der Fallszenen
FHA = 430                                    # Figurenhöhe in den Fallszenen
IX, JX = 1180, 1650                          # Bank: Herr Lohberg links (blickt nach rechts), Sieglinde rechts (blickt nach links)
HX = 1415                                    # Schreibtisch zwischen beiden
VX, VB = 1000, 500                           # Transporter im Hof: Mitte, Breite
SX, GX = 1720, 1430                          # Hof: Sieglinde, Gerichtsvollzieherin


def boden_(y, c, fill=None, x0=30, x1=1890, h=None):
    hh = h or 60
    im = Image.new("RGBA", (x1 - x0, hh))
    dr = ImageDraw.Draw(im)
    if fill:
        dr.rectangle((0, 0, x1 - x0, hh), fill=fill)
    dr.line((0, 2, x1 - x0, 2), fill=INK, width=6)
    return El(im, x0, y, c, "cut", 0.0, None, name="boden")


def buero(c):
    """Beratungsraum der Bank: Wand mit Fenster und Bank-Symbol (Tabler building-bank, ohne Namen), Schreibtisch."""
    els = [hart(boden_(G0, c, fill=(226, 226, 222, 255), h=100))]
    w, h = 900, 560
    im = Image.new("RGBA", (w, h))
    dr = ImageDraw.Draw(im)
    dr.rounded_rectangle((0, 0, w - 1, h - 1), 14, fill=WAND, outline=INK, width=5)
    fx, fy = 470, 70                              # Fenster
    dr.rectangle((fx, fy, fx + 330, fy + 230), fill=HELLBLAU, outline=INK, width=5)
    dr.line((fx + 165, fy, fx + 165, fy + 230), fill=INK, width=4)
    dr.line((fx, fy + 115, fx + 330, fy + 115), fill=INK, width=4)
    els.append(hart(El(im, 70, G0 - h, c, "cut", 0.0, None, name="buero")))
    els.append(hart(ficon("tabler", "building-bank", 250, G0 - h + 230, 170, c, fuell=GELB, anim="cut")))
    els.append(hart(pl("Bank", 250, G0 - h + 250, c, fill=WEISS, size=30, anker="m")))
    # Schreibtisch
    t = Image.new("RGBA", (300, 170))
    dt = ImageDraw.Draw(t)
    dt.rounded_rectangle((0, 0, 299, 34), 8, fill=(190, 135, 90, 255), outline=INK, width=5)
    for xx in (22, 258):
        dt.rectangle((xx, 30, xx + 20, 169), fill=(190, 135, 90, 255), outline=INK, width=4)
    els.append(hart(El(t, HX - 150, G0 - 170, c, "cut", 0.0, None, name="schreibtisch")))
    return els


def _van_bild(w, spiegeln=False):
    """Transporter (Kastenwagen) als Grundform: Kasten, Fahrerhaus mit Fenster, blauer Streifen, zwei Räder; Aufschrift
    „Malerbetrieb“ (keine Marke, kein Kennzeichen). Blickt nach rechts (spiegeln: nach links)."""
    s = 3
    h = int(w * 0.5)
    W_, H_ = w * s, h * s
    im = Image.new("RGBA", (W_, H_))
    dr = ImageDraw.Draw(im)
    lw = 5 * s
    kasten = (0.02 * W_, 0.10 * H_, 0.70 * W_, 0.80 * H_)
    kabine = [(0.68 * W_, 0.24 * H_), (0.83 * W_, 0.24 * H_), (0.96 * W_, 0.50 * H_), (0.975 * W_, 0.53 * H_),
              (0.975 * W_, 0.80 * H_), (0.68 * W_, 0.80 * H_)]
    dr.rounded_rectangle(kasten, int(0.03 * W_), fill=WEISS)
    dr.polygon(kabine, fill=WEISS)
    dr.rectangle((0.02 * W_ + lw, 0.58 * H_, 0.975 * W_ - lw, 0.65 * H_), fill=BLAU)
    dr.rounded_rectangle(kasten, int(0.03 * W_), outline=INK, width=lw)
    dr.line(kabine + [kabine[0]], fill=INK, width=lw, joint="curve")
    dr.polygon([(0.72 * W_, 0.30 * H_), (0.815 * W_, 0.30 * H_), (0.905 * W_, 0.50 * H_), (0.72 * W_, 0.50 * H_)],
               fill=HELLBLAU, outline=INK, width=4 * s)
    for fx in (0.20, 0.80):
        r = 0.095 * W_
        cx, cy = fx * W_, H_ - r - 2 * s
        dr.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(70, 70, 74, 255), outline=INK, width=lw)
        dr.ellipse((cx - r * 0.45, cy - r * 0.45, cx + r * 0.45, cy + r * 0.45), fill=(200, 200, 200, 255), outline=INK, width=3 * s)
    im = im.resize((w, h), Image.LANCZOS)
    if spiegeln:
        im = ImageOps.mirror(im)
    txt = "Malerbetrieb"
    f = F("ExtraBold", max(26, int(w * 0.06)))
    d2 = ImageDraw.Draw(im)
    tx = (0.36 if not spiegeln else 0.64) * w - f.getlength(txt) / 2
    d2.text((tx, 0.26 * h), txt, font=f, fill=INK)
    return im


def transporter(cx, unten, c, breite=VB, bis=None, anim="pop", spiegeln=False, name="transporter"):
    im = _van_bild(breite, spiegeln)
    return El(im, cx - im.width // 2, unten - im.height, c, anim, 0.0, bis, name=name)


def hof(c):
    """Hof des Malerbetriebs: Werkstattgebäude mit Tor, Fenster und Schild, Farbeimer und Leiter (Tabler)."""
    els = [hart(boden_(G0, c, fill=(222, 218, 210, 255), h=100))]
    w, h = 760, 470
    im = Image.new("RGBA", (w, h))
    dr = ImageDraw.Draw(im)
    dr.rounded_rectangle((0, 0, w - 1, h - 1), 14, fill=(244, 236, 214, 255), outline=INK, width=5)
    dr.rectangle((90, 190, 360, h - 1), fill=(200, 200, 204, 255), outline=INK, width=5)      # Werkstatttor
    for yy in range(230, h - 10, 50):
        dr.line((90, yy, 360, yy), fill=INK, width=3)
    dr.rectangle((470, 200, 680, 340), fill=HELLBLAU, outline=INK, width=5)                   # Fenster
    dr.line((575, 200, 575, 340), fill=INK, width=4)
    els.append(hart(El(im, 70, G0 - h, c, "cut", 0.0, None, name="werkstatt")))
    els.append(hart(pl("Malerbetrieb", 70 + w // 2, G0 - h + 40, c, fill=GELB, size=32, anker="m")))
    els.append(hart(ficon("tabler", "bucket", 640, G0, 90, c, fuell=WEISS, anim="cut")))
    return els


def pfandsiegel(cx, cy, c, bis=None):
    """Pfandsiegel als Aufkleber (Grundform) auf dem Transporter."""
    f = F("ExtraBold", 26)
    t = "Pfandsiegel"
    w, h = int(f.getlength(t)) + 36, 54
    im = Image.new("RGBA", (w, h))
    dr = ImageDraw.Draw(im)
    dr.rounded_rectangle((0, 0, w - 1, h - 1), 10, fill=HELLROT, outline=INK, width=4)
    dr.text((18, 10), t, font=f, fill=INK)
    return El(im, cx - w // 2, cy - h // 2, c, "pop", 0.0, bis, name="pfandsiegel")


def hallen(y, c, mark_c):
    """Zwei Lagerhallen auf der Tafel (Grundformen), Ware als Tabler-Pakete; Halle 2 wird zum Wort markiert."""
    els = []
    for i, x in enumerate((140, 640)):
        w, h = 480, 190
        im = Image.new("RGBA", (w, h))
        dr = ImageDraw.Draw(im)
        dr.polygon([(0, 50), (w // 2, 0), (w - 1, 50)], fill=(226, 226, 222, 255), outline=INK)
        dr.line([(0, 50), (w // 2, 2), (w - 1, 50)], fill=INK, width=5)
        dr.rectangle((4, 50, w - 5, h - 3), fill=WEISS, outline=INK, width=5)
        els.append(El(im, x, y, c, "fade", 0.0, None, name=f"halle{i + 1}"))
        for k in range(4):
            e = ficon("tabler", "package", x + 80 + k * 105, y + h - 12, 80, c, fuell=GELB if (i + k) % 2 else WEISS, anim="fade")
            e.name = "tafelicon:package"          # Ware gehört zur Tafelzeichnung (links), nicht zu den Requisiten rechts
            els.append(e)
        els.append(z(f"Halle {i + 1}", x + 170, y + 58, c, "ExtraBold", 30, rechts=1170))
    rahmen = Image.new("RGBA", (520, 232))
    ImageDraw.Draw(rahmen).rounded_rectangle((3, 3, 516, 228), 22, outline=DGRUEN, width=9)
    els.append(El(rahmen, 620, y - 20, mark_c, "pop", 0.0, None, name="rahmen:halle2"))
    return els


# ===========================================================================================================================
# A1 Fall: in der Bank bei Herrn Lohberg
# ===========================================================================================================================
SG_DA, LO_DA = beim("sieg", "Sieglinde"), beim("lohb", "Lohberg")
folie([(NULL, "Fall · Der Firmenwagen"), (SG_DA, "Fall · Sieglinde"), (beim("maler", "Transporter"), "Fall · Sieglinde braucht einen Transporter"),
       ("lo1", "Fall · Herr Lohberg: Kredit gegen Sicherheit"), ("si1", "Fall · Sieglinde: Womit fahre ich?"),
       ("lo2", "Fall · Herr Lohberg: Sie behalten den Wagen")], [
    *buero(NULL),
    pl("Die Bank finanziert deinen Firmenwagen", 70, 30, beim("fall", "finanziert"), fill=GELB, size=32, bis="lo1"),
    pl("… und lässt ihn sich zur Sicherheit übereignen", 70, 100, beim("fall", "Sicherheit"), fill=WEISS, size=32, bis="lo1"),
    pl("Du fährst das Auto, aber es gehört der Bank", 70, 170, "du", fill=HELLROT, size=32, bis="lo1"),
    pl("Malerbetrieb: neuer Transporter nötig", 70, 240, beim("maler", "Malerbetrieb"), fill=WEISS, size=32, bis="lo1"),
    ficon("tabler", "paint", HX, G0 - 170, 90, beim("maler", "Malerbetrieb"), fuell=GELB, bis=beim("lo1", "dreißigtausend")),
    *fig("SG", JX, G0, FHA, [(SG_DA, "ruhig"), ("maler", "denkt"), ("lohb", "ruhig"), ("lo1", "sorge")], bis="si1"),
    *redet("SG_redet", JX, G0, FHA, "si1", "lo2"),
    *fig("SG", JX, G0, FHA, [("lo2", "denkt"), (beim("lo2", "nutzen"), "froh")], erst="cut"),
    ns("Sieglinde", JX, G0, SG_DA, BLAU, d=0.1),
    *fig("LO", IX, G0, FHA, [(LO_DA, "froh_r")], bis="lo1"),
    *redet("LO_redet_r", IX, G0, FHA, "lo1", "si1"),
    *fig("LO", IX, G0, FHA, [("si1", "ruhig_r")], bis="lo2", erst="cut"),
    *redet("LO_erklaert_r", IX, G0, FHA, "lo2", "kauf"),
    ns("Herr Lohberg", IX, G0, LO_DA, GRUEN, d=0.1),
    pl("Kredit: 30.000 €", 70, 30, beim("lo1", "dreißigtausend"), fill=GELB, size=32),
    ficon("tabler", "cash-banknote", HX, G0 - 170, 110, beim("lo1", "dreißigtausend"), fuell=GRUEN),
    pl("Sicherheit: der Transporter", 70, 100, beim("lo1", "Sicherheit"), fill=WEISS, size=32),
    pl("Nutzung, solange die Raten gezahlt werden", 70, 170, beim("lo2", "nutzen"), fill=GRUEN, size=32),
    blase("sprech", 820, 270, "lo1", 1420, 200, inhalt=["Wir leihen Ihnen 30.000 €.", "Als Sicherheit übereignen",
                                                        "Sie uns den Transporter."],
          textsize=34, figur=("LO_redet_r", IX, G0, FHA), bis="si1"),
    blase("sprech", 760, 200, "si1", 1260, 210, inhalt=["Und womit fahre ich dann", "zu meinen Kunden?"],
          textsize=34, figur=("SG_redet", JX, G0, FHA), bis="lo2"),
    blase("sprech", 880, 270, "lo2", 1420, 200, inhalt=["Den Wagen behalten Sie.", "Sie dürfen ihn nutzen, solange",
                                                        "Sie die Raten zahlen."],
          textsize=34, figur=("LO_erklaert_r", IX, G0, FHA), bis="kauf"),
])

# ===========================================================================================================================
# A2 Fall: der Transporter im Hof des Malerbetriebs
# ===========================================================================================================================
SG2 = beim("kauf", "übergeben")
folie([("kauf", "Fall · Kauf beim Autohändler"), ("unter", "Fall · Sicherungsvertrag mit Übereignung"),
       ("taeg", "Fall · Sieglinde fährt den Wagen"), ("frage", "Fall · Die Frage")], [
    *hof("kauf"),
    szene(bewegt(transporter(VX, G0, "kauf", anim="cut"), "kauf", beim("kauf", "Autohändler", ende=True), -450, 0),
          "239anfahrt*", 0.6),
    pl("beim Autohändler gekauft", 70, 30, beim("kauf", "Autohändler"), fill=WEISS, size=32, bis="frage"),
    pl("bezahlt mit dem Kredit", 70, 100, beim("kauf", "bezahlt"), fill=GELB, size=32, bis="frage"),
    pl("übergeben", 70, 170, SG2, fill=GRUEN, size=32, bis="frage"),
    *fig("SG", SX, G0, FHA, [(SG2, "froh"), ("unter", "ernst"), ("taeg", "freut"), ("frage", "denkt")]),
    ns("Sieglinde", SX, G0, SG2, BLAU, d=0.1),
    ficon("tabler", "building-bank", 1290, 300, 110, beim("unter", "Bank"), fuell=GELB, bis="frage"),
    ficon("tabler", "file-text", 1440, 300, 100, beim("unter", "Sicherungsvertrag"), fuell=WEISS, bis="frage"),
    szene(ficon("tabler", "signature", 1590, 300, 110, beim("unter", "unterschreibt"), bis="frage"), "239unterschrift*", 0.5),
    pl("bei der Bank: Sicherungsvertrag mit Übereignung", 70, 240, beim("unter", "Sicherungsvertrag"), fill=WEISS, size=32,
       bis="frage"),
    pl("jeden Tag zu den Kunden", 70, 310, "taeg", fill=GRUEN, size=32, bis="frage"),
    pl("Wem gehört der Transporter jetzt?", 70, 30, "frage", fill=PINK, size=34),
    pl("Und wenn Sieglinde pleitegeht oder ein anderer", 70, 105, "frage2", fill=WEISS, size=32),
    pl("Gläubiger den Wagen pfänden lässt?", 70, 170, "frage2", fill=WEISS, size=32),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_239(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=35, zeilenabstand=1.3)
        els += e; y += 14
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_239("sv", [
    "Sieglinde führt einen Malerbetrieb und braucht einen neuen Transporter. Ihre Bank leiht ihr dafür 30.000 €. "
    "Bankberater Herr Lohberg verlangt den Transporter als Sicherheit: Sieglinde soll ihn der Bank übereignen, darf ihn "
    "aber nutzen, solange sie die Raten zahlt.",
    "Sieglinde kauft den Transporter beim Autohändler, bezahlt ihn mit dem Kredit und bekommt ihn übergeben. Dann "
    "unterschreibt sie bei der Bank den Sicherungsvertrag mit der Übereignung. Seitdem fährt sie jeden Tag damit zu "
    "ihren Kunden.",
], "Wem gehört der Transporter? Und was gilt bei Insolvenz oder Pfändung?")

_zl = lambda W, wort: next(i for i, t in enumerate(W) if wort in t)

# ===========================================================================================================================
# C Das Problem: Eigentum ohne Übergabe
# ===========================================================================================================================
PC = "Das Problem"
folie([("prob", f"{PC} · Eigentum ohne Übergabe?"), ("prob2", f"{PC} · Übergabe scheidet aus"),
       ("prob3", f"{PC} · Lösung: Besitzkonstitut, § 930 BGB"), ("prob4", f"{PC} · Verweis Besitzkonstitut")], rechts_frei([
    *tafel("prob", "Das Problem: Eigentum ohne Übergabe?"),
    blk(110, 190, 505, 120, BLAU, "prob", [("Bank:", "ExtraBold", 32, INK), ("will Eigentümerin werden", "Bold", 30, INK)]),
    blk(645, 190, 505, 120, GELB, beim("prob", "Sieglinde"), [("Sieglinde:", "ExtraBold", 32, INK),
                                                             ("braucht den Wagen", "Bold", 30, INK)]),
    *neinz("Übergabe nach § 929 S. 1 BGB scheidet aus", 360, "prob2", "Bold", 32, x=160),
    blk(110, 450, 1040, 120, GRUEN, "prob3", [("Lösung: Besitzkonstitut, § 930 BGB", "ExtraBold", 32, INK),
                                            ("statt der Übergabe: Besitzmittlungsverhältnis", "Bold", 30, INK)]),
    zit("Alle Übergabesurrogate: Video „Besitzkonstitut & Co.: Eigentum ohne Übergabe“", 110, 600, "prob4"),
    *requisit([("prob", ("tabler", "building-bank", 120, GELB), "Eigentum?", WEISS),
               (beim("prob", "Sieglinde"), ("tabler", "truck", 130, WEISS), "Wagen bleibt bei ihr", GELB),
               ("prob2", ("tabler", "ban", 100, HELLROT), "keine Übergabe", HELLROT),
               ("prob3", ("tabler", "key", 100, GELB), "Besitzkonstitut", GRUEN)]),
    *zwei("LO", [("prob", "ruhig"), ("prob3", "froh")], "SG", [("prob", "sorge"), ("prob3", "staunt")]),
]))

# ===========================================================================================================================
# D §§ 929 S. 1, 930 BGB (Wortlautkarten), vier Prüfungspunkte
# ===========================================================================================================================
W929 = umbruch("„… dass der Eigentümer die Sache dem Erwerber übergibt und beide darüber einig sind, dass das Eigentum "
               "übergehen soll.“", 30, 1040)
w929, w929_y = wortlaut(80, 170, 1100, W929, "§ 929 Satz 1 BGB (Auszug)", "norm", size=30)
W930 = umbruch("„Ist der Eigentümer im Besitz der Sache, so kann die Übergabe dadurch ersetzt werden, dass zwischen ihm und "
               "dem Erwerber ein Rechtsverhältnis vereinbart wird, vermöge dessen der Erwerber den mittelbaren Besitz "
               "erlangt.“", 30, 1040)
w930, w930_y = wortlaut(80, w929_y + 18, 1100, W930, "§ 930 BGB", "w930",
                        marken=[(_zl(W930, "im Besitz"), "im Besitz", beim("w930", "Besitz")),
                                (_zl(W930, "Übergabe dadurch"), "Übergabe", beim("w930", "Übergabe")),
                                (_zl(W930, "Rechtsverhältnis"), "Rechtsverhältnis", beim("w930", "Rechtsverhältnis")),
                                (_zl(W930, "mittelbaren"), "mittelbaren Besitz", beim("w930", "mittelbaren"))], size=30)
PD = "A. §§ 929 S. 1, 930 BGB"
y4 = w930_y + 22
folie([("norm", PD), ("w930", f"{PD} › Wortlaut § 930 BGB"), ("vier", f"{PD} › 4 Prüfungspunkte")], rechts_frei([
    *tafel("norm", "§ 929 S. 1 i. V. m. § 930 BGB", size=44),
    *w929, *w930,
    pl("I. Einigung", 110, y4, "p1", fill=GELB, size=30),
    pl("II. Besitzmittlungsverhältnis", 400, y4, "p2", fill=GELB, size=30),
    pl("III. Berechtigung", 110, y4 + 68, "p3", fill=GELB, size=30),
    pl("IV. Bestimmtheit", 480, y4 + 68, "p4", fill=GELB, size=30),
    *requisit([("norm", ("tabler", "scale", 120, WEISS), "§§ 929 S. 1, 930 BGB", WEISS),
               ("w930", ("tabler", "file-text", 110, WEISS), "Wortlaut § 930 BGB", GELB),
               ("vier", ("tabler", "list-check", 110, None), "4 Prüfungspunkte", GELB)]),
    *zwei("LO", [("norm", "ruhig"), ("vier", "froh")], "SG", [("norm", "ruhig"), ("w930", "denkt"), ("vier", "froh")]),
]))
assert y4 + 68 + 60 <= 900, y4

# ===========================================================================================================================
# E I. Einigung; Trennung vom Sicherungsvertrag
# ===========================================================================================================================
PE = f"{PD} › I. Einigung"
folie([("einig", PE), (beim("einig", "Sicherheit"), f"{PE} › zur Sicherheit"),
       ("trenn", f"{PE} › Sicherungsvertrag getrennt")], rechts_frei([
    *tafel("einig", "I. Einigung"),
    *okz("Eigentum am Transporter geht auf die Bank über", 190, beim("einig", "Sieglinde"), "Bold", 32, x=160),
    *pkt("zur Sicherheit für den Kredit", 260, beim("einig", "Sicherheit"), "Bold", 32, x=160),
    blk(110, 360, 505, 150, HELLBLAU, "trenn", [("Sicherungsvertrag", "ExtraBold", 32, INK),
                                              ("schuldrechtliches", "Bold", 30, INK), ("Geschäft", "Bold", 30, INK)]),
    blk(645, 360, 505, 150, GELB, beim("trenn", "dingliche"), [("Übereignung", "ExtraBold", 32, INK),
                                                              ("dingliches Geschäft", "Bold", 30, INK),
                                                              ("§§ 929 S. 1, 930 BGB", "Bold", 30, INK)]),
    z("getrennt", 560, 525, beim("trenn", "trennen"), "ExtraBold", 30, farbe=DROT),
    zit("BGH, Urt. v. 12.4.2016 – XI ZR 305/14, Rn. 46: Sicherungsvertrag schuldrechtlich,", 110, 590, beim("trenn", "dingliche")),
    zit("Übereignung abstraktes dingliches Erfüllungsgeschäft", 110, 626, beim("trenn", "dingliche")),
    *requisit([("einig", ("tabler", "truck", 130, WEISS), "Transporter an die Bank", GELB),
               (beim("einig", "Sicherheit"), ("tabler", "shield-check", 110, GRUEN), "zur Sicherheit", GRUEN),
               ("trenn", ("tabler", "file-text", 110, HELLBLAU), "2 Geschäfte", WEISS)]),
    *zwei("LO", [("einig", "froh"), ("trenn", "ruhig")], "SG", [("einig", "ruhig"), ("trenn", "denkt")]),
]))

# ===========================================================================================================================
# F II. Besitzmittlungsverhältnis, § 868 BGB (Wortlautkarte)
# ===========================================================================================================================
W868 = umbruch("„Besitzt jemand eine Sache als … Mieter, Verwahrer oder in einem ähnlichen Verhältnis, vermöge dessen er einem "
               "anderen gegenüber auf Zeit zum Besitz berechtigt oder verpflichtet ist, so ist auch der andere Besitzer "
               "(mittelbarer Besitz).“", 30, 1040)
w868, w868_y = wortlaut(80, 165, 1100, W868, "§ 868 BGB (Auszug)", "w868",
                        marken=[(_zl(W868, "Mieter"), "Mieter", beim("w868", "Miete")),
                                (_zl(W868, "Verwahrer"), "Verwahrer", beim("w868", "Verwahrung")),
                                (_zl(W868, "ähnlichen"), "ähnlichen", beim("w868", "ähnliches")),
                                (_zl(W868, "auf Zeit"), "auf Zeit", beim("w868", "Zeit"))], size=30)
PF = f"{PD} › II. Besitzmittlungsverhältnis"
yf = w868_y + 16
folie([("bmv", PF), ("w868", f"{PF} › § 868 BGB"), ("sa", f"{PF} › h. M.: der Sicherungsvertrag"),
       ("konk", f"{PF} › konkreter Inhalt"), ("besitz", f"{PF} › unmittelbarer und mittelbarer Besitz")], rechts_frei([
    *tafel("bmv", "II. Besitzmittlungsverhältnis"),
    *w868,
    blk(110, yf, 1040, 66, GELB, "sa", [("h. M.: der Sicherungsvertrag selbst genügt", "ExtraBold", 31, INK)]),
    *pkt("Nutzung, solange sie zahlt", yf + 88, "sa2", "Bold", 30, x=160),
    *pkt("zahlt sie nicht mehr: Herausgabe", yf + 136, beim("sa2", "Zahlt", nr=2), "Bold", 30, x=160),
    *okz("konkreter Inhalt: auf Zeit zum Besitz berechtigt", yf + 196, beim("konk", "Bundesgerichtshof"), "Bold", 30, x=160),
    zit("BGH, Urt. v. 26.6.2026 – V ZR 92/25, Rn. 20", 160, yf + 238, beim("konk", "Bundesgerichtshof")),
    *requisit([("bmv", ("tabler", "arrows-exchange", 110, None), "Besitz für die Bank", WEISS),
               ("sa", ("tabler", "file-text", 110, GELB), "Sicherungsvertrag", GELB),
               (beim("sa2", "Zahlt", nr=2), ("tabler", "truck-return", 130, WEISS), "Herausgabe", HELLROT),
               ("konk", ("tabler", "calendar-time", 110, WEISS), "auf Zeit", WEISS),
               ("besitz", None, None, None)]),
    pl("Sieglinde: unmittelbare Besitzerin", 1575, 200, "besitz", fill=BLAU, size=28, anker="m"),
    pl("Bank: mittelbare Besitzerin", 1575, 280, beim("besitz", "Bank"), fill=GRUEN, size=28, anker="m"),
    *zwei("LO", [("bmv", "ruhig"), ("sa", "denkt"), (beim("besitz", "Bank"), "froh")],
          "SG", [("bmv", "ruhig"), ("sa2", "froh"), (beim("sa2", "Zahlt", nr=2), "sorge"), ("besitz", "froh")]),
]))
assert yf + 238 + 40 <= 900, yf

# ===========================================================================================================================
# G III. Berechtigung
# ===========================================================================================================================
PG = f"{PD} › III. Berechtigung"
folie([("ber", PG), ("ber2", f"{PG} › Sieglinde ist Eigentümerin")], rechts_frei([
    *tafel("ber", "III. Berechtigung", h=520),
    *pkt("Sieglinde muss Eigentümerin sein", 200, beim("ber", "Sieglinde"), "Bold", 34, x=160),
    *okz("Händler hat übergeben und übereignet", 290, "ber2", "Bold", 34, x=160),
    zit("§ 929 S. 1 BGB: Erwerb vom Autohändler", 160, 345, "ber2"),
    *requisit([("ber", ("tabler", "user-check", 110, WEISS), "Eigentümerin?", WEISS),
               ("ber2", ("tabler", "truck", 130, WEISS), "vom Händler übereignet", GRUEN)]),
    *stehend("SG", FX, [("ber", "ruhig"), ("ber2", "freut")]),
]))

# ===========================================================================================================================
# H IV. Bestimmtheit, Raumsicherungsvertrag; Zwischenergebnis
# ===========================================================================================================================
PH = f"{PD} › IV. Bestimmtheit"
folie([("best", PH), ("best2", f"{PH} › Transporter: Fahrzeug-Identifizierungsnummer"),
       ("best3", f"{PH} › Warenlager mit wechselndem Bestand"), ("best4", f"{PH} › räumliche Abgrenzung"),
       ("raum", f"{PH} › Raumsicherungsvertrag"), ("zw", f"{PD} › Zwischenergebnis")], rechts_frei([
    *tafel("best", "IV. Bestimmtheit"),
    *pkt("Einigung über eine bestimmte Sache", 170, beim("best", "Einigung"), "Bold", 31, x=160),
    zit("BGH, Urt. v. 16.12.2022 – V ZR 174/21, Rn. 10", 160, 212, beim("best", "Einigung")),
    *okz("Transporter: Fahrzeug-Identifizierungsnummer im Vertrag", 260, "best2", "Bold", 30, x=160),
    *pkt("schwieriger: Warenlager mit wechselndem Bestand", 320, "best3", "Bold", 30, x=160),
    z("nicht anders feststellbar: räumliche Abgrenzung", 160, 370, beim("best4", "verlangt"), "Bold", 30),
    zit("V ZR 174/21, Rn. 13", 160, 412, beim("best4", "verlangt")),
    *hallen(470, "best3", beim("best4", "Halle")),
    pl("alle Waren in Halle 2", 660, 690, beim("best4", "Halle"), fill=GRUEN, size=30),
    pl("Raumsicherungsvertrag", 160, 690, "raum", fill=GELB, size=30),
    zit("BGH, Urt. v. 24.1.2019 – IX ZR 110/17, Rn. 3", 160, 762, "raum"),
    *okz("Zwischenergebnis: Die Bank ist Eigentümerin", 815, "zw", "ExtraBold", 32, x=160),
    *requisit([("best", ("tabler", "target", 110, WEISS), "bestimmte Sache", WEISS),
               ("best2", ("tabler", "truck", 130, WEISS), "Fahrzeug-Ident.-Nr.", GELB),
               ("best3", ("tabler", "packages", 120, GELB), "Warenlager", WEISS),
               ("zw", ("tabler", "building-bank", 120, GELB), "Eigentümerin", GRUEN)]),
    *zwei("LO", [("best", "ruhig"), ("best3", "denkt"), ("zw", "froh")], "SG", [("best", "ruhig"), ("best2", "froh"),
                                                                                ("best3", "denkt"), ("zw", "ernst")]),
]))

# ===========================================================================================================================
# I Volle Eigentümerin, aber gebunden: Treuhand, Rückübereignung, auflösende Bedingung
# ===========================================================================================================================
PI = "B. Die Stellung der Bank"
folie([("treu", f"{PI} › volle Eigentümerin"), ("treu2", f"{PI} › gebunden wie ein Treuhänder"),
       ("verw", f"{PI} › Verwertung erst im Sicherungsfall"), ("rueck", f"{PI} › Rückübereignung nach Tilgung"),
       ("aufl", f"{PI} › auflösende Bedingung, § 158 Abs. 2 BGB")], rechts_frei([
    *tafel("treu", "Volle Eigentümerin – aber gebunden"),
    blk(110, 180, 505, 150, BLAU, "treu", [("außen:", "ExtraBold", 32, INK), ("volle Eigentümerin,", "Bold", 30, INK),
                                         ("echtes Eigentum", "Bold", 30, INK)]),
    zit("BGH, Urt. v. 7.3.2017 – VI ZR 125/16, Rn. 19", 110, 342, beim("treu", "Sicherungseigentum")),
    blk(645, 180, 505, 150, GELB, "treu2", [("innen:", "ExtraBold", 32, INK), ("Sicherungsvertrag bindet", "Bold", 30, INK),
                                          ("wie einen Treuhänder", "Bold", 30, INK)]),
    *pkt("Verwertung erst, wenn Sieglinde nicht mehr zahlt", 410, "verw", "Bold", 31, x=160),
    *okz("Kredit getilgt: Pflicht zur Rückübereignung", 480, "rueck", "Bold", 31, x=160),
    zit("aus dem Zweck des Sicherungsvertrags: BGH, Urt. v. 20.9.2012 – IX ZR 208/11, Rn. 11", 110, 524,
        beim("rueck", "Zweck")),
    *pkt("auflösend bedingt vereinbart: Eigentum fällt mit", 590, "aufl", "Bold", 31, x=160),
    z("der letzten Rate von selbst zurück, § 158 Abs. 2 BGB", 160, 636, beim("aufl", "letzten"), "Bold", 31),
    *requisit([("treu", ("tabler", "building-bank", 120, GELB), "volle Eigentümerin", BLAU),
               ("treu2", ("tabler", "lock", 100, GELB), "gebunden", GELB),
               ("verw", ("tabler", "cash-off", 110, WEISS), "Sicherungsfall", HELLROT),
               ("rueck", ("tabler", "arrow-back-up", 110, None), "zurück an Sieglinde", GRUEN),
               ("aufl", ("tabler", "calendar-check", 110, WEISS), "letzte Rate", GRUEN)]),
    *zwei("LO", [("treu", "froh"), ("treu2", "ruhig"), ("rueck", "froh")],
          "SG", [("treu", "sorge"), ("treu2", "ruhig"), ("verw", "ernst"), ("rueck", "freut")]),
]))

# ===========================================================================================================================
# J Insolvenz von Sieglinde: § 51 Nr. 1 InsO (Wortlautkarte), Absonderung
# ===========================================================================================================================
W51 = umbruch("„Den in § 50 genannten Gläubigern stehen gleich: 1. Gläubiger, denen der Schuldner zur Sicherung eines Anspruchs "
              "eine bewegliche Sache übereignet … hat;“", 30, 1040)
w51, w51_y = wortlaut(80, 245, 1100, W51, "§ 51 Nr. 1 InsO (Auszug)", "w51",
                      marken=[(_zl(W51, "gleich"), "gleich", beim("w51", "gleich")),
                              (_zl(W51, "Sicherung"), "zur Sicherung eines Anspruchs", beim("w51", "Sicherung")),
                              (_zl(W51, "übereignet"), "übereignet", beim("w51", "übereignet"))], size=30)
PJ = "C. Insolvenz und Vollstreckung"
yj = w51_y + 20
folie([("ins", f"{PJ} › Insolvenz von Sieglinde"), ("ins2", f"{PJ} › keine Aussonderung"),
       ("w51", f"{PJ} › § 51 Nr. 1 InsO"), ("abs", f"{PJ} › nur Absonderungsrecht"),
       ("abs2", f"{PJ} › Verwertung durch den Insolvenzverwalter")], rechts_frei([
    *tafel("ins", "Insolvenz von Sieglinde"),
    *neinz("Aussondern wie eine fremde Sache (§ 47 InsO)", 175, "ins2", "Bold", 31, x=160),
    *w51,
    blk(110, yj, 1040, 70, HELLROT, "abs", [("nur ein Absonderungsrecht", "ExtraBold", 33, INK)]),
    *pkt("Insolvenzverwalter hat den Wagen: er verwertet", yj + 95, "abs2", "Bold", 30, x=160),
    zit("§ 166 Abs. 1 InsO", 160, yj + 137, "abs2"),
    *pkt("Bank aus dem Erlös, nach Abzug der Kosten", yj + 180, beim("abs2", "befriedigt"), "Bold", 30, x=160),
    zit("§ 170 Abs. 1 InsO; BGH, Urt. v. 25.9.2014 – IX ZR 156/12, Rn. 9", 160, yj + 222, beim("abs2", "befriedigt")),
    *requisit([("ins", ("tabler", "building-store", 120, WEISS), "Malerbetrieb insolvent", HELLROT),
               ("ins2", ("tabler", "ban", 100, HELLROT), "keine Aussonderung", WEISS),
               ("w51", ("tabler", "scale", 120, WEISS), "wie Pfandgläubiger", GELB),
               ("abs2", ("tabler", "gavel", 110, WEISS), "Verwertung", WEISS),
               (beim("abs2", "befriedigt"), ("tabler", "cash", 120, GRUEN), "Erlös an die Bank", GRUEN)]),
    *zwei("LO", [("ins", "sorge"), ("abs", "ernst"), (beim("abs2", "befriedigt"), "ruhig")],
          "SG", [("ins", "schreck"), ("ins2", "muede"), ("abs2", "sorge")]),
]))
assert yj + 222 + 40 <= 900, yj

# ===========================================================================================================================
# K Einzelvollstreckung: Pfändung im Hof, § 771 ZPO
# ===========================================================================================================================
PF2 = beim("zv2", "pfänden")
folie([("zv", f"{PJ} › Einzelvollstreckung"), ("zv2", f"{PJ} › Pfändung durch einen anderen Gläubiger"),
       ("zv3", f"{PJ} › Drittwiderspruchsklage, § 771 ZPO"), ("zv4", f"{PJ} › Verweis Drittwiderspruchsklage")], [
    *hof("zv"),
    hart(transporter(VX, G0, "zv", anim="cut")),
    pl("Einzelvollstreckung", 70, 30, "zv", fill=GELB, size=32),
    pl("ein anderer Gläubiger lässt pfänden", 70, 100, beim("zv2", "Gläubiger"), fill=WEISS, size=32),
    *fig("GV", GX, G0, FHA, [(beim("zv2", "Gläubiger"), "ernst")]),
    ns("Gerichtsvollzieherin", GX, G0, beim("zv2", "Gläubiger"), LILA, d=0.1),
    szene(pfandsiegel(VX - 110, G0 - 122, PF2), "239siegel*", 0.6),
    *fig("SG", SX, G0, FHA, [("zv", "ruhig"), (PF2, "schreck"), ("zv3", "staunt")], erst="cut"),
    ns("Sieglinde", SX, G0, "zv", BLAU),
    pl("Bank als Eigentümerin: Drittwiderspruchsklage", 70, 170, beim("zv3", "Bank"), fill=GRUEN, size=32),
    ficon("tabler", "building-bank", 1580, 330, 110, beim("zv3", "Bank"), fuell=GELB),
    pl("§ 771 ZPO (h. M.)", 70, 240, beim("zv3", "Paragraf"), fill=WEISS, size=32),
    zit("vgl. BGH, Urt. v. 11.1.2007 – IX ZR 181/05, Rn. 10", 80, 305, beim("zv3", "Paragraf")),
    pl("Mehr: Video „Drittwiderspruchsklage § 771 ZPO“", 70, 350, "zv4", fill=WEISS, size=28),
])

# ===========================================================================================================================
# L Abgrenzung Eigentumsvorbehalt
# ===========================================================================================================================
PL = "D. Abgrenzung"
folie([("ev", f"{PL} › Eigentumsvorbehalt"), ("ev2", f"{PL} › Sicherungsübereignung"), ("ev3", f"{PL} › Verweis")], rechts_frei([
    *tafel("ev", "Nicht verwechseln", h=620),
    blk(110, 190, 1040, 140, HELLBLAU, "ev", [("Eigentumsvorbehalt (§ 449 Abs. 1 BGB):", "ExtraBold", 31, INK),
                                            ("Verkäufer bleibt Eigentümer,", "Bold", 30, INK),
                                            ("bis der Kaufpreis bezahlt ist", "Bold", 30, INK)]),
    blk(110, 360, 1040, 140, GELB, "ev2", [("Sicherungsübereignung:", "ExtraBold", 31, INK),
                                         ("Kreditnehmer überträgt sein Eigentum", "Bold", 30, INK),
                                         ("auf den Kreditgeber", "Bold", 30, INK)]),
    zit("Mehr: Video „Eigentumsvorbehalt: Das Sofa ist da, gehört aber dem Möbelhaus“", 110, 530, "ev3"),
    *requisit([("ev", ("tabler", "sofa", 130, BLAU), "Vorbehalt des Verkäufers", HELLBLAU),
               ("ev2", ("tabler", "truck", 130, WEISS), "Eigentum an die Bank", GELB)]),
    *stehend("SG", FX, [("ev", "denkt"), ("ev2", "froh")]),
]))

# ===========================================================================================================================
# M Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Herausgabeanspruch der Bank, § 985 BGB"), ("tipp2", "Klausurtipp · inzident beim Eigentum"),
       ("tipp3", "Klausurtipp · Recht zum Besitz, § 986 BGB")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Herausgabeanspruch der Bank:", 200, 200, beim("tipp", "Herausgabeanspruch"), "Bold", 36),
    z("§ 985 BGB", 200, 260, beim("tipp", "Paragraf"), "ExtraBold", 36),
    *pkt("Sicherungsübereignung inzident", 350, "tipp2", "Bold", 34, x=245),
    z("beim Eigentum der Bank prüfen", 245, 398, beim("tipp2", "Eigentum"), "Bold", 34),
    linienzug([(130, 480), (1130, 480)], "tipp3", breite=3),
    *pkt("Recht zum Besitz: Sicherungsvertrag", 505, "tipp3", "Bold", 34, x=245),
    z("solange Sieglinde zahlt, darf sie den Wagen", 245, 553, beim("tipp3", "Solange"), "Regular", 33),
    z("behalten, § 986 BGB", 245, 598, beim("tipp3", "Solange"), "Regular", 33),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# N Klausurschema
# ===========================================================================================================================
REIHEN = [("k1", 0, "I. Einigung, zur Sicherheit"),
          ("k2", 0, "II. Besitzmittlungsverhältnis statt Übergabe"),
          ("k2b", 1, "meist der Sicherungsvertrag"),
          ("k3", 0, "III. Berechtigung des Sicherungsgebers"),
          ("k4", 0, "IV. Bestimmtheit"),
          ("k4b", 1, "bei Warenlagern etwa durch Raumsicherung")]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Schema: Sicherungsübereignung"), 110, 90, "sch", 46)]
y = 250
for c, ebene, text in REIHEN:
    x = (130, 220)[ebene]
    cue = {"k2b": beim("k2", "meist"), "k4b": beim("k4", "bei")}.get(c, c)
    els_sch.append(z(text, x, y, cue, "ExtraBold" if ebene == 0 else "Regular", 42 if ebene == 0 else 38, rechts=1800))
    y += {0: 80, 1: 100}[ebene] if c not in ("k2", "k4") else 62
assert y <= 970, y
folie([("sch", "Klausurschema"), ("k1", "Klausurschema › I. Einigung"), ("k2", "Klausurschema › II. Besitzmittlungsverhältnis"),
       ("k3", "Klausurschema › III. Berechtigung"), ("k4", "Klausurschema › IV. Bestimmtheit")], els_sch)

# ===========================================================================================================================
# O Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Bei der Sicherungsübereignung ersetzt ein", 0)], [("Besitzmittlungsverhältnis", "a"), (" die Übergabe,", 0)],
                 [("meist der Sicherungsvertrag selbst.", 0)]], 750, 270, 42, "merke",
                {"a": beim("merke", "Besitzmittlungsverhältnis")}),
    *markertext([[("Die Bank wird ", 0), ("volle Eigentümerin", "b"), (",", 0)], [("bleibt aber ", 0), ("gebunden", "c"), (".", 0)]],
                750, 500, 42, "mk2", {"b": beim("mk2", "volle"), "c": beim("mk2", "gebunden")}),
    *markertext([[("In der Insolvenz des Sicherungsgebers:", 0)], [("nur ein ", 0), ("Absonderungsrecht", "d"), (".", 0)]],
                750, 670, 42, "mk3", {"d": beim("mk3", "Absonderungsrecht")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
