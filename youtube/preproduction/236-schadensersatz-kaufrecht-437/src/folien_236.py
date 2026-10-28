"""Folge 236 · Schadensersatz Kaufrecht § 437 Nr. 3 BGB: Welche Anspruchsgrundlage? – Serienstandard Open Peeps (Katzenkönig).
Fiktiver Fall: Katharina kauft für ihren Hobbykeller im Elektrogeschäft von Raimund ein Heizgerät für 600 € (original verpackt
vom Hersteller). Eine Woche später schmort ein Bauteil durch: Rauch, Brandfleck an Regal und Wand, niemand verletzt,
Kellerschaden 4.000 €. Fehler des Herstellers ab Werk, für Raimund nicht erkennbar. Katharina verlangt ein neues Gerät und
4.000 €; Raimund bietet das neue Gerät an, lehnt die 4.000 € ab.
Szenen laut ../SZENENPLAN.md. Zwei Handlungsgeräusche (Karton abstellen, Durchschmoren; ../geraeusche_herkunft.json).
Darstellung: kein Feuer, nur Rauchwolken (Tabler cloud, grau) und Brandflecken (Grundform). Keine Gerätemarken.
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/pkt
als eigene Kopie aus Folge 209 (gemeinsame Dateien unverändert); neu: heizgeraet(), rauch(), brandfleck(), keller(), regal_kisten().
Wortlautkarten wörtlich nach gesetze-im-internet.de (Abruf 07.10.2026): § 437 BGB (mit Auslassung), § 283 Satz 1,
§ 311a Abs. 2 Satz 1, 2 BGB. Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_236/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_236/" in n:
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
NAME = {"KA": "Katharina", "RM": "Raimund"}
NFARBE = {"KA": BLAU, "RM": GRUEN}


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
from PIL import ImageFilter
HELLBLAU = (214, 230, 252, 255)
WAND = (236, 230, 220, 255)
KELLER = (222, 218, 210, 255)
RAUCH = (190, 190, 192, 255)
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
G0 = 900                                     # Boden der Fallszenen
FHA = 430                                    # Figurenhöhe in den Fallszenen
IX, JX = 1180, 1650                          # Raimund links (blickt nach rechts), Katharina rechts (blickt nach links)
HX = 1415                                    # Heizgerät zwischen beiden


def boden_(y, c, fill=None, x0=30, x1=1890, h=None):
    hh = h or 60
    im = Image.new("RGBA", (x1 - x0, hh))
    dr = ImageDraw.Draw(im)
    if fill:
        dr.rectangle((0, 0, x1 - x0, hh), fill=fill)
    dr.line((0, 2, x1 - x0, 2), fill=INK, width=6)
    return El(im, x0, y, c, "cut", 0.0, None, name="boden")


def laden(c, wand=WAND, x=70, w=900, h=560):
    """Elektrogeschäft von innen: Rückwand mit Wandregal (zwei Bretter), Grundformen wie Folge 209."""
    els = [hart(boden_(G0, c, fill=(226, 226, 222, 255), h=100))]
    im = Image.new("RGBA", (w, h))
    dr = ImageDraw.Draw(im)
    dr.rounded_rectangle((0, 0, w - 1, h - 1), 14, fill=wand, outline=INK, width=5)
    for yy in (250, 470):
        dr.rectangle((60, yy, w - 60, yy + 18), fill=(190, 135, 90, 255), outline=INK, width=4)
    for xx in (60, w - 78):
        dr.rectangle((xx, 60, xx + 18, 488), fill=(190, 135, 90, 255), outline=INK, width=4)
    els.append(hart(El(im, x, G0 - h, c, "cut", 0.0, None, name="laden")))
    return els


def _heiz_bild(h, fill=WEISS, verrusst=False):
    """Heizgerät (Ölradiator) als Grundform: sieben Rippen, Bedienkasten mit Drehknopf, Füße mit Rollen; keine Marke."""
    s = 3
    w = int(h * 0.95)
    im = Image.new("RGBA", (w * s, h * s))
    dr = ImageDraw.Draw(im)
    lw = 4 * s
    kasten = int(w * 0.18)
    rip_x0, rip_x1 = kasten + 6 * s // 3, w - 4
    n = 7
    rb = (rip_x1 - rip_x0) / n
    for i in range(n):
        x0 = (rip_x0 + i * rb) * s
        dr.rounded_rectangle((x0, 0.06 * h * s, x0 + rb * s - 2 * s, 0.84 * h * s), int(rb * s / 2), fill=fill, outline=INK, width=lw)
    dr.rounded_rectangle((4 * s, 0.30 * h * s, (kasten + 8) * s, 0.70 * h * s), 8 * s, fill=fill, outline=INK, width=lw)
    r = kasten * 0.28 * s
    cx, cy = (4 + kasten / 2 + 2) * s, 0.42 * h * s
    dr.ellipse((cx - r, cy - r, cx + r, cy + r), fill=GELB, outline=INK, width=3 * s)
    dr.line((cx, cy - r, cx, cy - r * 0.3), fill=INK, width=3 * s)
    dr.rectangle((rip_x0 * s, 0.84 * h * s, rip_x1 * s, 0.88 * h * s), fill=INK)
    for fx in (rip_x0 + rb, rip_x1 - rb):
        dr.line((fx * s, 0.88 * h * s, fx * s, 0.93 * h * s), fill=INK, width=lw)
        rr = 0.035 * h * s
        dr.ellipse((fx * s - rr, h * s - 2 * rr - 2 * s, fx * s + rr, h * s - 2 * s), fill=(120, 120, 120, 255), outline=INK, width=3 * s)
    im = im.resize((w, h), Image.LANCZOS)
    if verrusst:                                  # Rußspuren (Brandfleck) auf den Rippen, kein Feuer
        ov = Image.new("RGBA", im.size)
        od = ImageDraw.Draw(ov)
        for (fx, fy, rx, ry) in ((0.55, 0.30, 0.30, 0.22), (0.70, 0.18, 0.20, 0.15), (0.45, 0.50, 0.18, 0.12)):
            od.ellipse(((fx - rx) * w, (fy - ry) * h, (fx + rx) * w, (fy + ry) * h), fill=(40, 36, 34, 150))
        ov = ov.filter(ImageFilter.GaussianBlur(h * 0.04))
        maske = im.getchannel("A")
        ov.putalpha(Image.fromarray(np.minimum(np.asarray(ov.getchannel("A")), np.asarray(maske))))
        im = Image.alpha_composite(im, ov)
    return im


def heizgeraet(cx, unten, h, c, fill=WEISS, verrusst=False, bis=None, anim="pop"):
    im = _heiz_bild(h, fill, verrusst)
    return El(im, cx - im.width // 2, unten - im.height, c, anim, 0.0, bis, name="heizgeraet" + ("_verrusst" if verrusst else ""))


def rauch(cx, unten, breite, c, bis=None, d=0.0):
    """Rauchwolke (Tabler cloud, grau gefüllt) – Rauchsymbol statt Feuer."""
    return ficon("tabler", "cloud", cx, unten, breite, c, fuell=RAUCH, d=d, bis=bis)


def brandfleck(cx, cy, rx, ry, c, bis=None, name="brandfleck"):
    """Rußfleck als weiche dunkle Fläche (Grundform, keine Flammen)."""
    w, h = int(rx * 2.6), int(ry * 2.6)
    im = Image.new("RGBA", (w, h))
    dr = ImageDraw.Draw(im)
    for (fx, fy, f) in ((0.5, 0.55, 1.0), (0.35, 0.45, 0.65), (0.66, 0.38, 0.6), (0.5, 0.3, 0.5)):
        dr.ellipse((fx * w - rx * f, fy * h - ry * f, fx * w + rx * f, fy * h + ry * f), fill=(52, 44, 40, 105))
    im = im.filter(ImageFilter.GaussianBlur(min(rx, ry) * 0.10))
    kern = Image.new("RGBA", im.size)                       # dunkler Kern des Brandflecks
    ImageDraw.Draw(kern).ellipse((w * 0.5 - rx * 0.45, h * 0.58 - ry * 0.45, w * 0.5 + rx * 0.45, h * 0.58 + ry * 0.45),
                                 fill=(30, 26, 24, 150))
    im = Image.alpha_composite(im, kern.filter(ImageFilter.GaussianBlur(min(rx, ry) * 0.08)))
    return El(im, cx - w // 2, cy - h // 2, c, "fade", 0.0, bis, name=name)


def keller(c, x=70, w=1780, h=580):
    """Hobbykeller: graue Wand mit Kellerfenster, Boden (Grundformen)."""
    els = [hart(boden_(G0, c, fill=(205, 203, 198, 255), h=100))]
    im = Image.new("RGBA", (w, h))
    dr = ImageDraw.Draw(im)
    dr.rounded_rectangle((0, 0, w - 1, h - 1), 14, fill=KELLER, outline=INK, width=5)
    fx, fy = 190, 40                             # Kellerfenster über dem Regal
    dr.rectangle((fx, fy, fx + 220, fy + 100), fill=(214, 230, 252, 255), outline=INK, width=5)
    for k in range(1, 4):
        dr.line((fx + k * 55, fy, fx + k * 55, fy + 100), fill=INK, width=4)
    els.append(hart(El(im, x, G0 - h, c, "cut", 0.0, None, name="keller")))
    return els


def regal_kisten(c, x0=150, w=380):
    """Kellerregal mit Kisten (Tabler package, gelb/weiß gefüllt)."""
    els = []
    im = Image.new("RGBA", (w, 380))
    dr = ImageDraw.Draw(im)
    for yy in (120, 250, 362):
        dr.rectangle((0, yy, w - 1, yy + 16), fill=(190, 135, 90, 255), outline=INK, width=4)
    for xx in (0, w - 18):
        dr.rectangle((xx, 0, xx + 18, 379), fill=(190, 135, 90, 255), outline=INK, width=4)
    els.append(hart(El(im, x0, G0 - 380, c, "cut", 0.0, None, name="regal")))
    for i, yy in enumerate((120, 250, 362)):
        for k in range(2):
            els.append(hart(ficon("tabler", "package", x0 + 105 + k * 170, G0 - 380 + yy + 2, 120, c,
                                  fuell=GELB if (i + k) % 2 else WEISS, anim="cut")))
    return els


# ===========================================================================================================================
# A1 Fall: der Kauf im Elektrogeschäft von Raimund
# ===========================================================================================================================
def ware(c):
    """Ware im Regal: zwei Heizgeräte oben, Mikrowellen und Glühbirnen unten (Tabler), keine Marken."""
    els = [hart(heizgeraet(330 + i * 300, G0 - 560 + 250 + 2, 170, c, anim="cut")) for i in range(2)]
    els += [hart(ficon("tabler", "microwave", 300 + i * 340, G0 - 560 + 470 + 2, 150, c, fuell=WEISS, anim="cut")) for i in range(2)]
    els.append(hart(ficon("tabler", "bulb", 470, G0 - 560 + 470 + 2, 90, c, fuell=GELB, anim="cut")))
    return els


folie([(NULL, "Fall · Das Heizgerät"), ("kauf", "Fall · Der Kauf im Elektrogeschäft"),
       ("verpackt", "Fall · Original verpackt vom Hersteller"), ("ra1", "Fall · Raimund übergibt das Gerät")], [
    *laden(NULL),
    *ware(NULL),
    pl("Heizgerät defekt", 70, 30, beim("fall", "defekt"), fill=GELB, size=32),
    pl("setzt den Keller in Brand", 70, 100, beim("fall", "Brand"), fill=HELLROT, size=32),
    *fig("KA", JX, G0, FHA, [(beim("kath", "Katharina"), "froh")], bis="ra1"),
    *fig("KA", JX, G0, FHA, [("ra1", "freut")], erst="cut"),
    ns("Katharina", JX, G0, beim("kath", "Katharina"), BLAU, d=0.1),
    *fig("RM", IX, G0, FHA, [(beim("kauf", "Raimund"), "froh_r")], bis="ra1"),
    *redet("RM_redet_r", IX, G0, FHA, "ra1", "woche"),
    ns("Raimund", IX, G0, beim("kauf", "Raimund"), GRUEN, d=0.1),
    pl("Elektrogeschäft von Raimund", 520, 270, beim("kauf", "Elektrogeschäft"), fill=WEISS, size=28, anker="m", bis="verpackt"),
    heizgeraet(HX, G0, 190, beim("kauf", "Heizgerät")),
    pl("Heizgerät: 600 €", HX, 560, beim("kauf", "sechshundert"), fill=GELB, size=28, anker="m", bis="verpackt"),
    szene(ficon("tabler", "package", HX, 690, 120, beim("verpackt", "verpackt"), fuell=HOLZ), "236karton*", 0.35),
    pl("original verpackt vom Hersteller", 520, 270, beim("verpackt", "verpackt"), fill=WEISS, size=28, anker="m"),
    blase("sprech", 760, 220, "ra1", 1420, 200, inhalt=["Bitte schön, Ihr neues Heizgerät.", "Viel Freude damit!"],
          textsize=34, figur=("RM_redet_r", IX, G0, FHA), bis="woche"),
])

# ===========================================================================================================================
# A2 Fall: eine Woche später im Hobbykeller
# ===========================================================================================================================
KX, KJ = 720, 1650
folie([("woche", "Fall · Eine Woche später"), ("rauch", "Fall · Rauch im Keller"), ("niemand", "Fall · Schaden 4.000 €"),
       ("werk", "Fall · Fehler des Herstellers"), ("erkenn", "Fall · Für Raimund nicht erkennbar")], [
    *keller("woche"),
    *regal_kisten("woche"),
    hart(heizgeraet(KX, G0, 210, "woche", anim="cut", bis=beim("rauch", "qualmt"))),
    heizgeraet(KX, G0, 210, beim("rauch", "qualmt"), verrusst=True, anim="cut"),
    pl("1 Woche später", 70, 30, beim("woche", "Woche"), fill=GELB, size=32),
    brandfleck(500, G0 - 250, 70, 110, beim("rauch", "Regal")),
    brandfleck(KX + 10, G0 - 330, 120, 110, beim("rauch", "Wand")),
    szene(rauch(KX + 30, G0 - 220, 120, beim("woche", "durch"), bis="werk"), "236schmoren*", 0.5),
    rauch(KX - 40, G0 - 330, 170, beim("rauch", "qualmt"), bis="werk"),
    rauch(KX + 60, G0 - 450, 210, beim("rauch", "qualmt", ende=True), bis="werk"),
    pl("niemand verletzt", 70, 100, beim("niemand", "Verletzt"), fill=GRUEN, size=32),
    pl("Kellerschaden: 4.000 €", 70, 170, beim("niemand", "viertausend"), fill=HELLROT, size=32),
    ficon("tabler", "building-factory", 1270, 640, 150, beim("werk", "Bauteil"), fuell=WEISS),
    pl("Bauteil ab Werk fehlerhaft", 1270, 430, beim("werk", "Bauteil"), fill=WEISS, size=28, anker="m", bis=beim("werk", "Fehler")),
    pl("Fehler des Herstellers", 1270, 430, beim("werk", "Fehler"), fill=HELLROT, size=28, anker="m"),
    pl("für Raimund nicht erkennbar", 70, 240, beim("erkenn", "Raimund"), fill=WEISS, size=32),
    *fig("KA", KJ, G0, FHA, [("woche", "ruhig"), (beim("rauch", "qualmt"), "schreck"), ("niemand", "sorge"), ("werk", "denkt")],
         erst="cut"),
    ns("Katharina", KJ, G0, "woche", BLAU),
])

# ===========================================================================================================================
# A3 Fall: Katharina fordert, Raimund antwortet, die Frage
# ===========================================================================================================================
folie([("ka1", "Fall · Katharina: neues Gerät und 4.000 €"), ("ra2", "Fall · Raimund: neues Gerät ja, Geld nein"),
       ("frage", "Fall · Die Frage")], [
    *laden("ka1"),
    *ware("ka1"),
    hart(heizgeraet(HX, G0, 190, "ka1", verrusst=True, anim="cut")),
    *redet("KA_redet", JX, G0, FHA, "ka1", "ra2"),
    *fig("KA", JX, G0, FHA, [("ra2", "ernst"), ("frage", "denkt")], erst="cut"),
    ns("Katharina", JX, G0, "ka1", BLAU),
    *fig("RM", IX, G0, FHA, [("ka1", "schreck_r")], bis="ra2", erst="cut"),
    *redet("RM_erklaert_r", IX, G0, FHA, "ra2", "frage"),
    *fig("RM", IX, G0, FHA, [("frage", "still_r")], erst="cut"),
    ns("Raimund", IX, G0, "ka1", GRUEN),
    blase("sprech", 880, 260, "ka1", 1240, 200, inhalt=["Ihr Heizgerät hat meinen Keller", "verrußt! Ich will ein neues Gerät",
                                                        "und 4.000 € für den Schaden."],
          textsize=34, figur=("KA_redet", JX, G0, FHA), bis="ra2"),
    blase("sprech", 860, 260, "ra2", 700, 200, inhalt=["Ein neues Gerät bekommen Sie.", "Aber für den Fehler des",
                                                       "Herstellers kann ich nichts."],
          textsize=34, figur=("RM_erklaert_r", IX, G0, FHA), bis="frage"),
    pl("Was kann Katharina verlangen, aus welcher Anspruchsgrundlage?", 70, 30, "frage", fill=PINK, size=32),
    pl("Muss Raimund für den Keller zahlen?", 70, 105, "frage2", fill=WEISS, size=32),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_236(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=35, zeilenabstand=1.3)
        els += e; y += 14
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_236("sv", [
    "Katharina kauft für sich privat im Elektrogeschäft von Raimund ein Heizgerät für ihren Hobbykeller, Preis 600 €. "
    "Raimund hat das Gerät original verpackt vom Hersteller bezogen.",
    "Eine Woche später schmort im Gerät ein Bauteil durch. Es qualmt, ein Regal brennt an, die Wand ist verrußt. Verletzt "
    "wird niemand; der Schaden im Keller beträgt 4.000 €. Das Bauteil war schon ab Werk fehlerhaft, ein Fehler des "
    "Herstellers. Für Raimund war das nicht erkennbar.",
    "Katharina verlangt von Raimund ein neues Gerät und 4.000 € für den Schaden. Raimund antwortet: „Ein neues Gerät "
    "bekommen Sie. Aber für den Fehler des Herstellers kann ich nichts.“",
], "Was kann Katharina verlangen, und muss Raimund für den Keller zahlen?")

_zl = lambda W, wort: next(i for i, t in enumerate(W) if wort in t)

# ===========================================================================================================================
# C § 437 Nr. 3 BGB (Wortlautkarte): Rechtsgrundverweisung, Mangel
# ===========================================================================================================================
W437 = umbruch("„Ist die Sache mangelhaft, kann der Käufer, wenn die Voraussetzungen der folgenden Vorschriften vorliegen "
               "und soweit nicht ein anderes bestimmt ist, … 3. nach den §§ 440, 280, 281, 283 und 311a Schadensersatz oder "
               "nach § 284 Ersatz vergeblicher Aufwendungen verlangen.“", 31, 1040)
w437, w437_y = wortlaut(80, 175, 1100, W437, "§ 437 BGB (Auszug)", "w437",
                        marken=[(_zl(W437, "Voraussetzungen"), "Voraussetzungen", beim("w437", "Voraussetzungen")),
                                (_zl(W437, "vorliegen"), "vorliegen", beim("w437", "vorliegen")),
                                (_zl(W437, "3. nach"), "3.", beim("w437b", "Nummer")),
                                (_zl(W437, "Schadensersatz"), "Schadensersatz", beim("w437b", "Schadensersatz")),
                                (_zl(W437, "311a"), "311a", beim("w437b", "genannten"))], size=31)
PC = "A. Anspruchsgrundlage"
folie([("agl", f"{PC} › § 437 BGB"), ("w437", f"{PC} › § 437 Nr. 3 BGB"),
       ("rgv", f"{PC} › § 437 Nr. 3 BGB › Rechtsgrundverweisung"), ("mangel", f"{PC} › Sachmangel"),
       ("mangel2", f"{PC} › Sachmangel bei Gefahrübergang"), ("sys", f"{PC} › System der §§ 280 ff. BGB")], rechts_frei([
    *tafel("agl", "Der Einstieg: § 437 Nr. 3 BGB"),
    *w437,
    blk(110, w437_y + 22, 1040, 110, GELB, "rgv", [("Rechtsgrundverweisung: Voraussetzungen", "ExtraBold", 32, INK),
                                                ("im allgemeinen Schuldrecht, alle müssen vorliegen", "Bold", 30, INK)]),
    *okz("Mangel: nicht für die gewöhnliche Verwendung geeignet", w437_y + 160, beim("mangel", "Ein"), "Bold", 30, x=160),
    zit("§ 434 Abs. 1, 3 Satz 1 Nr. 1 BGB", 160, w437_y + 202, beim("mangel", "Ein")),
    *okz("schon bei der Übergabe", w437_y + 250, "mangel2", "Bold", 30, x=160),
    zit("§ 446 Satz 1 BGB (Gefahrübergang)", 160, w437_y + 292, "mangel2"),
    zit("Das System: Video „Schadensersatz Schema: Das System der §§ 280 ff. BGB“", 110, w437_y + 345, "sys"),
    *requisit([("agl", ("tabler", "scale", 120, WEISS), "Anspruchsgrundlage?", WEISS),
               ("w437", ("tabler", "file-text", 110, WEISS), "§ 437 Nr. 3 BGB", GELB),
               ("rgv", ("tabler", "route", 110, None), "Verweisung", GELB),
               ("mangel", ("tabler", "alert-triangle", 110, HELLROT), "Sachmangel", HELLROT)]),
    *zwei("RM", [("agl", "ruhig"), ("mangel", "sorge")], "KA", [("agl", "ruhig"), ("rgv", "denkt"), ("mangel", "ernst")]),
]))
assert w437_y + 345 + 40 <= 900, w437_y

# ===========================================================================================================================
# D Die Kontrollfrage
# ===========================================================================================================================
PD = "B. Kontrollfrage"
folie([("kf", PD), ("kf1", f"{PD} › Nacherfüllung beseitigt den Schaden?"), ("kf2", f"{PD} › ja: statt der Leistung"),
       ("kf3", f"{PD} › nein: neben der Leistung"), ("kf4", f"{PD} › so auch der BGH"),
       ("kf5", f"{PD} › Gerät: statt der Leistung"), ("kf6", f"{PD} › Keller: neben der Leistung")], rechts_frei([
    *tafel("kf", "Die Kontrollfrage"),
    z("Welche Vorschrift passt, hängt vom Schaden ab.", 110, 180, "kf", "Regular", 32),
    blk(110, 240, 1040, 150, HELLBLAU, "kf1", [("Würde eine ordnungsgemäße Nacherfüllung im", "Bold", 31, INK),
                                            ("letztmöglichen Zeitpunkt den Schaden", "Bold", 31, INK),
                                            ("noch beseitigen?", "Bold", 31, INK)]),
    zit("Kontrollfrage der Lehre (Klausurformel)", 110, 400, beim("kf1", "Kontrollfrage")),
    blk(110, 450, 505, 120, GRUEN, "kf2", [("ja: Schadensersatz", "ExtraBold", 30, INK), ("statt der Leistung", "ExtraBold", 30, INK)]),
    blk(645, 450, 505, 120, GELB, "kf3", [("nein: neben der Leistung,", "ExtraBold", 30, INK), ("hier § 280 Abs. 1 BGB", "Bold", 30, INK)]),
    z("BGH: ob eine Nacherfüllung den Schaden beseitigen würde", 110, 590, "kf4", "Regular", 29),
    zit("BGH, Urt. v. 3.7.2013 – VIII ZR 169/12, Rn. 26 f.; vgl. VII ZR 63/18, Rn. 17, 19", 110, 632,
        beim("kf4", "fragt")),
    *okz("Gerät: ein neues Gerät ersetzt es – statt der Leistung", 700, "kf5", "Bold", 31, x=160),
    *okz("Keller: Gerät repariert ihn nicht – neben der Leistung", 770, "kf6", "Bold", 31, x=160),
    *requisit([("kf", ("tabler", "help-circle", 110, WEISS), "Welcher Schaden?", WEISS),
               ("kf1", ("tabler", "refresh", 110, None), "Nacherfüllung", HELLBLAU),
               ("kf5", ("tabler", "replace", 110, None), "neues Gerät", GRUEN),
               ("kf6", ("tabler", "home-x", 110, WEISS), "Keller bleibt verrußt", GELB)]),
    *zwei("RM", [("kf", "ruhig"), ("kf2", "denkt"), ("kf5", "froh")], "KA", [("kf", "ruhig"), ("kf1", "denkt"), ("kf6", "sorge")]),
]))

# ===========================================================================================================================
# E1 Welche Norm? Wege 1 und 2 (§ 281, § 283 mit Wortlautkarte)
# ===========================================================================================================================
W283 = umbruch("„Braucht der Schuldner nach § 275 Abs. 1 bis 3 nicht zu leisten, kann der Gläubiger unter den Voraussetzungen "
               "des § 280 Abs. 1 Schadensersatz statt der Leistung verlangen.“", 31, 1040)
w283, w283_y = wortlaut(80, 525, 1100, W283, "§ 283 Satz 1 BGB", "w283",
                        marken=[(_zl(W283, "nicht zu leisten"), "nicht zu leisten", beim("w283", "nicht")),
                                (_zl(W283, "Schadensersatz"), "Schadensersatz", beim("w283", "Schadensersatz"))], size=31)
PE = "C. Die passende Norm"
folie([("wege", f"{PE} · 4 Wege"), ("t1", f"{PE} › 1. Mangel behebbar"), ("t1a", f"{PE} › 1. §§ 280 Abs. 1, 3, 281 BGB: Frist"),
       ("t1b", f"{PE} › 1. Ausnahmen von der Frist"), ("t2", f"{PE} › 2. nachträglich unbehebbar"),
       ("w283", f"{PE} › 2. §§ 280 Abs. 1, 3, 283 BGB"), ("t2b", f"{PE} › 2. keine Frist")], rechts_frei([
    *tafel("wege", "Welche Anspruchsgrundlage?"),
    z("1. Mangel behebbar (Reparatur, neues Gerät)", 110, 175, "t1", "ExtraBold", 32),
    z("§§ 280 Abs. 1, 3, 281 BGB: grundsätzlich erst", 160, 225, "t1a", "Bold", 31),
    z("nach erfolgloser Frist zur Nacherfüllung", 160, 268, beim("t1a", "grundsätzlich"), "Bold", 31),
    *pkt("Ausnahmen: § 281 Abs. 2, § 440 BGB; beim Verbraucher-", 325, "t1b", "Regular", 29, x=200),
    z("güterkauf stattdessen § 475d BGB", 200, 365, beim("t1b", "Verbrauchsgüterkauf"), "Regular", 29),
    zit("Mehr zur Frist: Video „Schadensersatz statt der Leistung §§ 280, 281 BGB“", 160, 410, "t1v"),
    z("2. unbehebbar, Hindernis nach Vertragsschluss", 110, 465, "t2", "ExtraBold", 32),
    *w283,
    *pkt("keine Frist: sie wäre sinnlos", w283_y + 18, "t2b", "Bold", 31, x=160),
    *requisit([("wege", ("tabler", "arrows-split", 110, None), "4 Wege", GELB),
               ("t1", ("tabler", "tool", 110, None), "behebbar", GRUEN),
               ("t1a", ("tabler", "hourglass", 100, HELLBLAU), "Frist", GELB),
               ("t1b", ("tabler", "hourglass-off", 100, WEISS), "ohne Frist?", WEISS),
               ("t2", ("tabler", "ban", 100, HELLROT), "unbehebbar", HELLROT),
               ("t2b", ("tabler", "hourglass-off", 100, WEISS), "keine Frist", WEISS)]),
    *zwei("RM", [("wege", "ruhig"), ("t1a", "denkt"), ("t2", "still")], "KA", [("wege", "ruhig"), ("t1", "froh"), ("t2", "denkt")]),
]))
assert w283_y + 70 <= 900, w283_y

# ===========================================================================================================================
# E2 Welche Norm? Wege 3 und 4, Verzögerungsschaden
# ===========================================================================================================================
W311 = umbruch("„Der Gläubiger kann nach seiner Wahl Schadensersatz statt der Leistung oder Ersatz seiner Aufwendungen in dem "
               "in § 284 bestimmten Umfang verlangen. Dies gilt nicht, wenn der Schuldner das Leistungshindernis bei "
               "Vertragsschluss nicht kannte und seine Unkenntnis auch nicht zu vertreten hat.“", 30, 1040)
w311, w311_y = wortlaut(80, 225, 1100, W311, "§ 311a Abs. 2 Satz 1, 2 BGB", "w311",
                        marken=[(_zl(W311, "nicht kannte"), "nicht kannte", beim("w311b", "kannte")),
                                (_zl(W311, "Unkenntnis"), "Unkenntnis", beim("w311b", "Unkenntnis")),
                                (_zl(W311, "vertreten"), "vertreten", beim("w311b", "vertreten"))], size=30)
folie([("t3", f"{PE} › 3. anfänglich unbehebbar"), ("w311", f"{PE} › 3. § 311a Abs. 2 BGB"),
       ("t4", f"{PE} › 4. Mangelfolgeschaden"), ("t4a", f"{PE} › 4. § 280 Abs. 1 BGB, ohne Frist"),
       ("t5", f"{PE} › Verzögerungsschaden"), ("t5b", f"{PE} › Verzögerungsschaden: Verzug, § 286 BGB")], rechts_frei([
    *tafel("t3", "Welche Anspruchsgrundlage?"),
    z("3. schon bei Vertragsschluss unbehebbar", 110, 172, "t3", "ExtraBold", 32),
    *w311,
    z("4. Mangelfolgeschaden, etwa am Keller", 110, w311_y + 20, "t4", "ExtraBold", 32),
    z("§ 280 Abs. 1 BGB allein, ohne Frist", 160, w311_y + 70, "t4a", "Bold", 31),
    zit("Gesetzesbegründung: Schäden „an anderen Rechtsgütern als der Kaufsache selbst“,", 160, w311_y + 118, "t4b"),
    zit("BT-Drucks. 14/6040, S. 224 f.", 160, w311_y + 152, "t4b"),
    blk(110, w311_y + 200, 1040, 110, HELLBLAU, "t5", [("verzögerte Nacherfüllung: Verzögerungsschaden", "Bold", 30, INK),
                                                    ("Verzug nötig: § 280 Abs. 2 mit § 286 BGB", "ExtraBold", 30, INK)]),
    *requisit([("t3", ("tabler", "file-text", 110, WEISS), "bei Vertragsschluss", WEISS),
               ("w311b", ("tabler", "user-question", 110, WEISS), "kannte er es?", WEISS),
               ("t4", ("tabler", "home-x", 110, WEISS), "Keller", HELLROT),
               ("t4a", ("tabler", "scale", 120, WEISS), "§ 280 Abs. 1 BGB", GELB),
               ("t5", ("tabler", "clock", 100, HELLBLAU), "Verzug", HELLBLAU)]),
    *zwei("RM", [("t3", "ruhig"), ("w311b", "denkt"), ("t5", "ruhig")], "KA", [("t3", "ruhig"), ("t4", "sorge"), ("t4a", "froh")]),
]))
assert w311_y + 320 <= 900, w311_y

# ===========================================================================================================================
# F Vertretenmüssen des Händlers
# ===========================================================================================================================
PF = "D. Vertretenmüssen"
folie([("vm", f"{PF} › Keller: § 280 Abs. 1 BGB"), ("vm2", f"{PF} › vermutet, Entlastung möglich"),
       ("vm3", f"{PF} › keine Untersuchungspflicht"), ("vm4", f"{PF} › Hersteller kein Erfüllungsgehilfe"),
       ("vm5", f"{PF} › anders: Garantie, Anhaltspunkte"), ("vm6", f"{PF} › der Fall"),
       ("vm7", f"{PF} › nicht zu vertreten")], rechts_frei([
    *tafel("vm", "Hat Raimund etwas zu vertreten?"),
    z("Auch beim Keller muss er die Pflichtverletzung zu vertreten haben.", 110, 175, beim("vm", "Auch"), "Regular", 29),
    blk(110, 230, 1040, 110, GELB, "vm2", [("vermutet: § 280 Abs. 1 Satz 2 BGB", "ExtraBold", 32, INK),
                                        ("aber Entlastung möglich", "Bold", 30, INK)]),
    *pkt("Verkäufer muss die Ware regelmäßig nicht untersuchen", 360, "vm3", "Bold", 30, x=160),
    zit("BGH, Urt. v. 19.6.2009 – V ZR 93/08, Rn. 19", 160, 402, beim("vm3", "Bundesgerichtshof")),
    *pkt("Hersteller ist nicht sein Erfüllungsgehilfe (§ 278 BGB)", 460, beim("vm4", "Verschulden"), "Bold", 30, x=160),
    zit("BGH, Urt. v. 15.7.2008 – VIII ZR 211/07, Rn. 29", 160, 502, beim("vm4", "Hersteller", nr=2)),
    *pkt("anders etwa: Garantie oder Anhaltspunkte für einen Mangel", 560, "vm5", "Regular", 30, x=160),
    zit("V ZR 93/08, Rn. 19; § 276 Abs. 1 Satz 1 BGB", 160, 602, beim("vm5", "Garantie")),
    *pkt("Raimund: original verpackt, kein Anlass zum Verdacht", 665, "vm6", "Bold", 30, x=160),
    *neinz("mangelhafte Lieferung nicht zu vertreten", 740, "vm7", "ExtraBold", 32, x=160),
    *requisit([("vm", ("tabler", "user-question", 110, WEISS), "zu vertreten?", WEISS),
               ("vm2", ("tabler", "scale", 120, WEISS), "vermutet", GELB),
               ("vm3", ("tabler", "zoom-cancel", 110, WEISS), "keine Untersuchung", WEISS),
               ("vm4", ("tabler", "building-factory", 120, WEISS), "Hersteller", WEISS),
               ("vm5", ("tabler", "certificate", 110, GELB), "Garantie?", GELB),
               ("vm6", ("tabler", "package", 110, HOLZ), "original verpackt", WEISS),
               ("vm7", ("tabler", "circle-x", 100, HELLROT), "nicht zu vertreten", HELLROT)]),
    *zwei("RM", [("vm", "denkt"), ("vm3", "ruhig"), ("vm7", "froh")], "KA", [("vm", "ernst"), ("vm4", "denkt"), ("vm7", "sorge")]),
]))

# ===========================================================================================================================
# G Anspruch gegen den Hersteller (ein Satz, Verweis)
# ===========================================================================================================================
folie([("ph", "D. Vertretenmüssen › Keller: Anspruch gegen den Hersteller"), ("ph2", "D. Vertretenmüssen › Verweis Produzentenhaftung")],
      rechts_frei([
    *tafel("ph", "Und der Hersteller?", h=480),
    *pkt("Produkthaftungsgesetz: § 1 ProdHaftG", 200, beim("ph", "Produkthaftungsgesetz"), "Bold", 32, x=160),
    *pkt("Produzentenhaftung: § 823 Abs. 1 BGB", 270, beim("ph", "Paragraf"), "Bold", 32, x=160),
    zit("Mehr: Video „Explodierende Flasche: Produzentenhaftung nach § 823 I BGB“", 110, 360, "ph2"),
    *requisit([("ph", ("tabler", "building-factory", 140, WEISS), "Hersteller", GELB)]),
    *stehend("KA", FX, [("ph", "denkt"), (beim("ph", "Produkthaftungsgesetz"), "froh")]),
]))

# ===========================================================================================================================
# H Ergebnis (Fallszene im Elektrogeschäft)
# ===========================================================================================================================
folie([("erg", "Ergebnis · Das Gerät: statt der Leistung"), ("erg2", "Ergebnis · Vorrang der Nacherfüllung"),
       ("erg3", "Ergebnis · Der Keller: § 280 Abs. 1 BGB"), ("erg4", "Ergebnis · Raimund: nichts zu vertreten")], [
    *laden("erg"),
    *ware("erg"),
    pl("Gerät: Schadensersatz statt der Leistung", 70, 30, beim("erg", "Gerät"), fill=GELB, size=30),
    hart(heizgeraet(HX, G0, 190, "erg", verrusst=True, anim="cut", bis=beim("erg2", "neue"))),
    heizgeraet(HX, G0, 190, beim("erg2", "neue")),
    pl("Vorrang: Nacherfüllung, neues Gerät", 70, 100, "erg2", fill=GRUEN, size=30),
    pl("Keller: § 280 Abs. 1 BGB, ohne Frist", 70, 170, "erg3", fill=WEISS, size=30),
    pl("Raimund: nichts zu vertreten", 70, 240, "erg4", fill=HELLROT, size=30),
    ficon("tabler", "building-factory", HX, 640, 130, beim("erg4", "viertausend"), fuell=WEISS),
    pl("4.000 € beim Hersteller", HX, 420, beim("erg4", "viertausend"), fill=GELB, size=28, anker="m"),
    *fig("RM", IX, G0, FHA, [("erg", "ruhig_r"), (beim("erg2", "neue"), "freut_r"), ("erg4", "froh_r")], erst="cut"),
    ns("Raimund", IX, G0, "erg", GRUEN),
    *fig("KA", JX, G0, FHA, [("erg", "ruhig"), (beim("erg2", "neue"), "froh"), ("erg3", "ernst"), ("erg4", "denkt")], erst="cut"),
    ns("Katharina", JX, G0, "erg", BLAU),
])

# ===========================================================================================================================
# I Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · jeden Schadensposten einzeln"), ("tipp2", "Klausurtipp · Vertretenmüssen des Händlers"),
       ("tipp3", "Klausurtipp · Anspruch gegen den Hersteller")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Jeden Schadensposten einzeln prüfen:", 200, 200, beim("tipp", "Prüfe"), "Bold", 36),
    z("mit der Kontrollfrage", 200, 260, beim("tipp", "Kontrollfrage"), "Regular", 34),
    *pkt("Händler: Folgeschaden kann am", 350, "tipp2", "Bold", 34, x=245),
    z("Vertretenmüssen scheitern", 245, 398, beim("tipp2", "Vertretenmüssen"), "Bold", 34),
    linienzug([(130, 480), (1130, 480)], "tipp3", breite=3),
    *pkt("dann Anspruch gegen den Hersteller prüfen", 505, "tipp3", "Bold", 34, x=245),
    zit("§ 1 ProdHaftG; § 823 Abs. 1 BGB", 245, 555, beim("tipp3", "Hersteller")),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# J Klausurschema
# ===========================================================================================================================
REIHEN = [("k0", 0, "Anspruch aus § 437 Nr. 3 BGB mit §§ 280 ff. BGB", True),
          ("k1", 1, "1. Kaufvertrag und Sachmangel bei Gefahrübergang", False),
          ("k2", 1, "2. Kontrollfrage: statt oder neben der Leistung?", False),
          ("k3", 1, "3. passende Norm: § 281, § 283, § 311a Abs. 2", False),
          ("k3b", 1, "    oder § 280 Abs. 1 BGB allein", False),
          ("k4", 1, "4. Vertretenmüssen (vermutet)", False),
          ("k5", 1, "5. Schaden (§§ 249 ff. BGB)", False)]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Schema: Schadensersatz beim Kauf"), 110, 90, "sch", 46)]
y = 240
for c, ebene, text, fett in REIHEN:
    x = (130, 200)[ebene]
    cue = beim("k3", "zweihundertachtzig") if c == "k3b" else c
    els_sch.append(z(text, x, y, cue, "ExtraBold" if fett else "Regular", 40 if ebene == 0 else 36, rechts=1800))
    y += {0: 95, 1: 80}[ebene] if c != "k3" else 60
assert y <= 970, y
folie([("sch", "Klausurschema"), ("k0", "Klausurschema › Anspruchsgrundlage"), ("k1", "Klausurschema › 1. Kaufvertrag, Sachmangel"),
       ("k2", "Klausurschema › 2. Kontrollfrage"), ("k3", "Klausurschema › 3. passende Norm"),
       ("k4", "Klausurschema › 4. Vertretenmüssen"), ("k5", "Klausurschema › 5. Schaden")], els_sch)

# ===========================================================================================================================
# K Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("§ 437 Nr. 3 BGB ", 0), ("verweist", "a")], [("ins allgemeine Schuldrecht.", 0)]], 750, 280, 44, "merke",
                {"a": beim("merke", "verweist")}),
    *markertext([[("Was eine Nacherfüllung noch beseitigen", 0)], [("könnte: ", 0), ("statt der Leistung", "b"), (".", 0)]],
                750, 440, 44, "mk2", {"b": beim("mk2", "statt")}),
    *markertext([[("Den Folgeschaden: ", 0), ("neben der Leistung", "c"), (".", 0)]], 750, 600, 44, "mk3",
                {"c": beim("mk3", "neben")}),
    *markertext([[("Beides nur, wenn der Verkäufer", 0)], [("etwas ", 0), ("zu vertreten", "d"), (" hat.", 0)]], 750, 700, 44,
                "mk4", {"d": beim("mk4", "vertreten")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
