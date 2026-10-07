"""Folge 240 · Schwerer Raub § 250 StGB: Spielzeugpistole & Labello-Fall – Serienstandard Open Peeps (Katzenkönig).
Fiktiver Fall: Früh am Morgen steht Wiltrud allein hinter der Theke einer Bäckerei. Alois kommt herein, zieht eine schwarze,
täuschend echt aussehende Pistole aus der Jacke („Keine Bewegung! Das Geld aus der Kasse nehme ich mir selbst.“), Wiltrud
weicht zurück, Alois nimmt 300 € aus der offenen Kasse und rennt hinaus. An der Tür fällt ihm die Pistole aus der Jacke;
Bäckermeister Ottfried hebt sie auf: eine leichte Spielzeugpistole aus Kunststoff. Wiltrud unverletzt. Abwandlung
(Labello-Fall): Lippenpflegestift von hinten in den Rücken, Wiltrud hält ihn für eine Messerspitze.
Szenen laut ../SZENENPLAN.md. Zwei Handlungsgeräusche (Ladenglocke, Kassenschublade; ../geraeusche_herkunft.json).
Darstellung: keine echte Waffe; die Spielzeugpistole nur als stilisiertes, neutral graues Symbol (Fluent Emoji High Contrast
„water-pistol“), nie auf eine Person gerichtet; Lippenpflegestift als neutrale Grundform ohne Marke; keine Gewalt im Bild.
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/pkt
als eigene Kopie aus Folge 236 (gemeinsame Dateien unverändert); neu: baeckerei(), theke(), lippenstift(), pistole().
Wortlautkarten wörtlich nach gesetze-im-internet.de (Abruf 07.10.2026): § 250 Abs. 1 Nr. 1 a, b und Abs. 2 Nr. 1 StGB
(jeweils Auszug). Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_240/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_240/" in n:
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
NAME = {"WI": "Wiltrud", "AL": "Alois", "OT": "Ottfried"}
NFARBE = {"WI": BLAU, "AL": GRUEN, "OT": GELB}


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
WAND = (246, 236, 222, 255)
HOLZ = (214, 160, 110, 255)
HOLZD = (190, 135, 90, 255)
GRAU = (150, 150, 156, 255)
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
G0 = 900                                     # Boden der Fallszenen
FHA = 430                                    # Figurenhöhe in den Fallszenen
WX, WX2 = 1640, 1740                         # Wiltrud hinter der Theke (blickt nach links), nach dem Zurückweichen
AX = 1120                                    # Alois vor der Theke (blickt nach rechts)
TUER_X = 300                                 # Alois an der Ladentür
OX = 700                                     # Ottfried vor dem Brotregal
KX = 1390                                    # Kasse auf der Theke
THEKE_Y = G0 - 250                           # Oberkante der Theke


def boden_(y, c, fill=None, x0=30, x1=1890, h=None):
    hh = h or 60
    im = Image.new("RGBA", (x1 - x0, hh))
    dr = ImageDraw.Draw(im)
    if fill:
        dr.rectangle((0, 0, x1 - x0, hh), fill=fill)
    dr.line((0, 2, x1 - x0, 2), fill=INK, width=6)
    return El(im, x0, y, c, "cut", 0.0, None, name="boden")


def baeckerei(c, backstube=None):
    """Bäckerei von innen: Rückwand, Ladentür links (Glasfenster), Brotregal mit Backwaren (Fluent Emoji High Contrast:
    bread, baguette-bread, croissant, pretzel; Palettenfüllung), Tür zur Backstube; keine Marken."""
    els = [hart(boden_(G0, c, fill=(226, 222, 214, 255), h=100))]
    w, h = 1780, 560
    im = Image.new("RGBA", (w, h))
    dr = ImageDraw.Draw(im)
    dr.rounded_rectangle((0, 0, w - 1, h - 1), 14, fill=WAND, outline=INK, width=5)
    tx0, tx1 = 70, 300                          # Ladentür (relativ zur Wand)
    dr.rectangle((tx0, 130, tx1, h - 1), fill=WEISS, outline=INK, width=5)
    dr.rectangle((tx0 + 30, 160, tx1 - 30, 330), fill=HELLBLAU, outline=INK, width=4)
    dr.ellipse((tx1 - 50, 360, tx1 - 30, 380), fill=INK)
    for yy in (190, 330, 470):                  # Brotregal: drei Bretter
        dr.rectangle((350, yy, 930, yy + 16), fill=HOLZD, outline=INK, width=4)
    for xx in (350, 912):
        dr.rectangle((xx, 60, xx + 18, h - 1), fill=HOLZD, outline=INK, width=4)
    bx0, bx1 = 975, 1145                        # Tür zur Backstube
    dr.rectangle((bx0, 150, bx1, h - 1), fill=(236, 226, 210, 255), outline=INK, width=5)
    dr.ellipse((bx0 + 18, 370, bx0 + 38, 390), fill=INK)
    els.append(hart(El(im, 70, G0 - h, c, "cut", 0.0, None, name="baeckerei")))
    oy = G0 - h
    ware = [("bread", 520, 190), ("croissant", 860, 190),          # Fach 700/oben bleibt frei (hinter Ottfrieds Kopf)
            ("pretzel", 520, 330), ("croissant", 700, 330), ("bread", 860, 330),
            ("baguette-bread", 520, 470), ("pretzel", 700, 470), ("bread", 860, 470)]
    for n, x, yy in ware:
        els.append(hart(ficon("fluent-emoji-high-contrast", n, x, oy + yy + 2, 105, c, fuell=GELB, anim="cut")))
    if backstube:
        els.append(pl("Backstube", 70 + (bx0 + bx1) // 2, oy + 165, backstube, fill=WEISS, size=26, anker="m"))
    return els


def theke(c):
    """Verkaufstheke mit Glasvitrine (Grundform) und Kasse (Tabler cash-register); Figuren dahinter werden verdeckt."""
    x0, x1 = 1255, 1860
    w, h = x1 - x0, G0 - THEKE_Y + 4
    im = Image.new("RGBA", (w, h))
    dr = ImageDraw.Draw(im)
    dr.rectangle((0, 0, w - 1, h - 1), fill=HOLZ, outline=INK, width=5)
    dr.rectangle((20, 22, w - 21, 120), fill=HELLBLAU, outline=INK, width=4)
    dr.rectangle((0, 0, w - 1, 16), fill=HOLZD, outline=INK, width=4)
    els = [hart(El(im, x0, THEKE_Y, c, "cut", 0.0, None, name="theke"))]
    for i, n in enumerate(("croissant", "pretzel", "croissant", "bread")):
        els.append(hart(ficon("fluent-emoji-high-contrast", n, x0 + 90 + i * 140, THEKE_Y + 118, 80, c, fuell=GELB,
                              anim="cut")))
    els.append(hart(ficon("tabler", "cash-register", KX, THEKE_Y + 2, 150, c, fuell=WEISS, anim="cut")))
    return els


def pistole(cx, unten, breite, c, bis=None, anim="pop"):
    """Spielzeugpistole: stilisiertes, neutral graues Symbol (Fluent Emoji High Contrast water-pistol, MIT); Mündung zeigt
    nach links, weg von allen Figuren."""
    return ficon("fluent-emoji-high-contrast", "water-pistol", cx, unten, breite, c, fuell=GRAU, nebenfarbe=GRAU, bis=bis,
                 anim=anim)


def _lippenstift_bild(h):
    """Lippenpflegestift als neutrale Grundform (Kappe weiß, Hülse blau, keine Marke)."""
    s = 3
    w = int(h * 0.30)
    im = Image.new("RGBA", (w * s, h * s))
    dr = ImageDraw.Draw(im)
    lw = 4 * s
    dr.rounded_rectangle((lw, lw, (w - 1) * s - lw, int(h * 0.42) * s), int(w * 0.45) * s, fill=WEISS, outline=INK, width=lw)
    dr.rounded_rectangle((lw, int(h * 0.40) * s, (w - 1) * s - lw, h * s - lw), int(w * 0.18) * s, fill=BLAU, outline=INK,
                         width=lw)
    dr.line((lw, int(h * 0.47) * s, (w - 1) * s - lw, int(h * 0.47) * s), fill=INK, width=3 * s)
    return im.resize((w, h), Image.LANCZOS)


def lippenstift(cx, unten, h, c, bis=None, anim="pop"):
    im = _lippenstift_bild(h)
    return El(im, cx - im.width // 2, unten - im.height, c, anim, 0.0, bis, name="lippenpflegestift")


def figur_x(k, x, folge, unten=G0, hoehe=FHA, bis=None, erst="pop"):
    """Figur an fester Stelle in der Fallszene mit Mimikfolge (harte Schnitte)."""
    return fig(k, x, unten, hoehe, folge, bis=bis, erst=erst)


# ===========================================================================================================================
# A Fall: der Überfall in der Bäckerei (eine Szene, Zwiebelschalen)
# ===========================================================================================================================
folie([(NULL, "Fall · Die Bäckerei"), ("alois", "Fall · Alois kommt herein"), ("zieht", "Fall · Die Pistole"),
       ("a1", "Fall · Alois droht"), ("nimmt", "Fall · Griff in die Kasse"), ("flieht", "Fall · Flucht mit dem Geld"),
       ("faellt", "Fall · Die Pistole an der Tür"), ("o1", "Fall · Ein Spielzeug aus Plastik"),
       ("frage", "Fall · Die Frage")], [
    *baeckerei(NULL, backstube=beim("ottfried", "Backstube")),
    pl("Räuber bedroht Bäckereiverkäuferin", 70, 30, beim("fall", "bedroht"), fill=GELB, size=32, bis="alois"),
    pl("Pistole sieht täuschend echt aus", 70, 100, beim("fall", "täuschend"), fill=WEISS, size=32, bis="alois"),
    # Wiltrud hinter der Theke (vor der Theke gezeichnet = dahinter)
    *fig("WI", WX, G0, FHA, [(beim("wiltrud", "Wiltrud"), "ruhig"), ("zieht", "schreck")], bis="weicht"),
    ns("Wiltrud", WX, G0, beim("wiltrud", "Wiltrud"), BLAU, d=0.1, bis="weicht"),
    *fig("WI", WX2, G0, FHA, [("weicht", "schreck"), ("flieht", "sorge"), (beim("o1", "Spielzeug"), "staunt"),
                              ("unverl", "ruhig"), ("frage", "denkt")], erst="cut"),
    ns("Wiltrud", WX2, G0, "weicht", BLAU),
    *theke(NULL),
    pl("früh am Morgen", 70, 170, beim("wiltrud", "Morgen"), fill=WEISS, size=32, bis="alois"),
    # Alois kommt herein (Ladenglocke), droht, greift in die Kasse, rennt hinaus
    szene(fig("AL", AX, G0, FHA, [(beim("alois", "Alois"), "ernst_r")], bis="a1")[0], "240tuerglocke*", 0.8),
    ns("Alois", AX, G0, beim("alois", "Alois"), GRUEN, d=0.1, bis="flieht"),
    *redet("AL_redet_r", AX, G0, FHA, "a1", "weicht"),
    *fig("AL", AX, G0, FHA, [("weicht", "ernst_r"), ("nimmt", "still_r")], bis="flieht", erst="cut"),
    pistole(AX - 10, 420, 150, beim("zieht", "Pistole"), bis="flieht"),
    pl("schwarze Pistole aus der Jacke", AX - 10, 270, beim("zieht", "Pistole"), fill=WEISS, size=28, anker="m", bis="a1"),
    blase("sprech", 780, 200, "a1", 700, 250, inhalt=["Keine Bewegung! Das Geld aus", "der Kasse nehme ich mir selbst."],
          textsize=34, figur=("AL_redet_r", AX, G0, FHA), bis="weicht"),
    pl("hält die Pistole für echt", WX2 - 40, 380, "weicht", fill=HELLROT, size=28, anker="m", bis="nimmt"),
    szene(ficon("tabler", "cash-banknote", KX, THEKE_Y - 115, 130, beim("nimmt", "Kasse"), fuell=GRUEN, bis="flieht"),
          "240kasse*", 0.8),
    pl("300 €", KX, 400, beim("nimmt", "dreihundert"), fill=GELB, size=30, anker="m", bis="flieht"),
    *fig("AL", TUER_X, G0, FHA, [("flieht", "ernst")], bis="ottfried", erst="cut"),
    ns("Alois", TUER_X, G0, "flieht", GRUEN, bis="ottfried"),
    pl("will das Geld behalten", 70, 30, beim("flieht", "Geld"), fill=WEISS, size=32, bis="unverl"),
    pistole(470, G0 - 4, 120, beim("faellt", "Pistole"), bis=beim("ottfried", "hebt"), anim="cut"),
    pl("Pistole fällt aus der Jacke", 650, 765, beim("faellt", "fällt"), fill=WEISS, size=28, anker="m",
       bis=beim("ottfried", "Ottfried")),
    # Ottfried kommt aus der Backstube und hebt die Pistole auf
    *fig("OT", OX, G0, FHA, [(beim("ottfried", "Ottfried"), "staunt"), (beim("ottfried", "hebt"), "denkt_r")], bis="o1"),
    *redet("OT_redet_r", OX, G0, FHA, "o1", "unverl"),
    *fig("OT", OX, G0, FHA, [("unverl", "ruhig_r"), ("frage", "denkt_r")], erst="cut"),
    ns("Ottfried", OX, G0, beim("ottfried", "Ottfried"), GELB, d=0.1),
    pistole(OX - 120, 700, 110, beim("ottfried", "hebt"), anim="cut"),
    blase("sprech", 820, 200, "o1", 1230, 250, inhalt=["Die ist ja aus Plastik.", "Ein Spielzeug, aber täuschend echt."],
          textsize=34, figur=("OT_redet_r", OX, G0, FHA), bis="unverl"),
    pl("Spielzeug aus Plastik", OX - 230, 390, beim("o1", "Plastik"), fill=GELB, size=28, anker="m"),
    pl("Wiltrud unverletzt", 70, 30, "unverl", fill=GRUEN, size=32),
    pl("Hat Alois einen schweren Raub begangen?", 70, 100, "frage", fill=PINK, size=32),
    pl("Und nur ein Lippenpflegestift im Rücken?", 70, 170, "frage2", fill=WEISS, size=32),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_240(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 205
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=34, zeilenabstand=1.3)
        els += e; y += 12
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_240("sv", [
    "Früh am Morgen steht Wiltrud allein hinter der Theke einer Bäckerei. Alois kommt herein und zieht eine schwarze "
    "Pistole aus der Jacke, die täuschend echt aussieht: „Keine Bewegung! Das Geld aus der Kasse nehme ich mir selbst.“ "
    "Wiltrud hält die Pistole für echt und weicht zurück. Alois greift in die offene Kasse, nimmt 300 € und rennt hinaus; "
    "er will das Geld behalten.",
    "An der Tür fällt ihm die Pistole aus der Jacke. Bäckermeister Ottfried hebt sie auf: eine leichte Spielzeugpistole "
    "aus Kunststoff, aber täuschend echt. Wiltrud ist unverletzt.",
    "Abwandlung: Alois hat keine Pistole. Er drückt Wiltrud von hinten einen Lippenpflegestift in den Rücken; sie hält "
    "ihn für die Spitze eines Messers. Im Übrigen wie oben.",
], "Hat Alois einen schweren Raub nach § 250 StGB begangen?")

_zl = lambda W, wort: next(i for i, t in enumerate(W) if wort in t)

# ===========================================================================================================================
# C Grundtatbestand: Raub, § 249 StGB
# ===========================================================================================================================
PC = "A. Raub, § 249 StGB"
folie([("raub", PC), ("r1", f"{PC} › Sache, Wegnahme"), ("r2", f"{PC} › Drohung mit Gefahr für Leib oder Leben"),
       ("r3", f"{PC} › Drohung mit einem Spielzeug"), ("r4", f"{PC} › Finalität, Vorsatz, Zueignungsabsicht"),
       ("r5", f"{PC} › Verweis Folge Raub"), ("r6", f"{PC} › Herausgabe: § 255 StGB")], rechts_frei([
    *tafel("raub", "Grundtatbestand: Raub, § 249 StGB"),
    *okz("Geld: fremde bewegliche Sache", 180, beim("r1", "fremde"), "Bold", 32, x=160),
    *okz("Wegnahme gegen den Willen von Wiltrud", 240, beim("r1", "Willen"), "Bold", 32, x=160),
    *okz("Drohung mit gegenwärtiger Gefahr für Leib oder Leben", 300, "r2", "Bold", 30, x=160),
    *pkt("Spielzeug schadet nicht: Wiltrud soll die", 370, "r3", "Regular", 30, x=200),
    z("Drohung für möglich halten", 200, 410, beim("r3", "Es"), "Regular", 30),
    zit("BGH, Beschl. v. 11.5.2011 – 2 StR 618/10, Rn. 4", 200, 452, beim("r3", "Es")),
    *okz("Finalität, Vorsatz, Zueignungsabsicht", 505, "r4", "Bold", 32, x=160),
    *okz("Raub (+)", 565, beim("r4", "Raub"), "ExtraBold", 34, x=160),
    zit("Mehr: Video „Raub § 249 StGB: Prüfungsschema mit Gewalt, Wegnahme & Finalität“", 110, 625, "r5"),
    blk(110, 680, 1040, 115, HELLBLAU, "r6", [("Gibt Wiltrud das Geld heraus: § 255 StGB", "Bold", 31, INK),
                                           ("„gleich einem Räuber“: § 250 StGB gilt ebenso", "Bold", 31, INK)]),
    *requisit([("raub", ("tabler", "scale", 120, WEISS), "§ 249 StGB", GELB),
               ("r1", ("tabler", "cash-banknote", 130, GRUEN), "300 €", GELB),
               ("r2", ("tabler", "alert-triangle", 110, HELLROT), "Drohung", HELLROT),
               ("r6", ("tabler", "cash-banknote", 130, GRUEN), "Geben statt Nehmen?", WEISS)]),
    *zwei("AL", [("raub", "ernst"), ("r3", "still"), ("r6", "denkt")], "WI", [("raub", "sorge"), ("r2", "schreck"), ("r4", "ernst")]),
]))

# ===========================================================================================================================
# D1 § 250 Abs. 1 Nr. 1 StGB (Wortlautkarte)
# ===========================================================================================================================
W1 = (umbruch("„(1) Auf Freiheitsstrafe nicht unter drei Jahren ist zu erkennen, wenn 1. der Täter oder ein anderer "
              "Beteiligter am Raub", 31, 1040) +
      umbruch("a) eine Waffe oder ein anderes gefährliches Werkzeug bei sich führt,", 31, 1040) +
      umbruch("b) sonst ein Werkzeug oder Mittel bei sich führt, um den Widerstand einer anderen Person durch Gewalt oder "
              "Drohung mit Gewalt zu verhindern oder zu überwinden, …“", 31, 1040))
w1, w1_y = wortlaut(80, 175, 1100, W1, "§ 250 Abs. 1 Nr. 1 a, b StGB (Auszug)", "w1",
                    marken=[(_zl(W1, "drei Jahren"), "drei Jahren", beim("w1", "drei")),
                            (_zl(W1, "a) eine Waffe"), "Waffe", beim("w1a", "Waffe")),
                            (_zl(W1, "gefährliches Werkzeug"), "gefährliches Werkzeug", beim("w1a", "gefährliches")),
                            (_zl(W1, "sonst ein Werkzeug"), "sonst ein Werkzeug oder Mittel", beim("w1b", "sonst")),
                            (_zl(W1, "Drohung mit Gewalt"), "Drohung mit Gewalt", beim("w1b", "Drohung"))], size=31)
PD = "B. § 250 Abs. 1 Nr. 1 StGB"
folie([("q", "B. Qualifikation, § 250 StGB"), ("w1", f"{PD} › Wortlaut"), ("w1a", f"{PD} › a) Waffe, gefährliches Werkzeug"),
       ("w1b", f"{PD} › b) sonst ein Werkzeug oder Mittel")], rechts_frei([
    *tafel("q", "Die Qualifikation: § 250 StGB"),
    *w1,
    *requisit([("q", ("tabler", "scale", 120, WEISS), "§ 250 StGB", GELB),
               ("w1a", None, "Waffe?", WEISS),
               ("w1b", None, "sonst ein Mittel?", WEISS)]),
    pistole(PX, PU, 170, beim("w1a", "Waffe")),
    *zwei("OT", [("q", "ruhig"), ("w1a", "denkt")], "WI", [("q", "ruhig"), ("w1b", "denkt")]),
]))
assert w1_y + 20 <= 900, w1_y

# ===========================================================================================================================
# D2 Buchstabe a: Waffe oder gefährliches Werkzeug?
# ===========================================================================================================================
folie([("na", f"{PD} › a) Waffe?"), ("na1", f"{PD} › a) Waffe: Beschaffenheit"),
       ("na2", f"{PD} › a) Spielzeugpistolen ausgeklammert"), ("na3", f"{PD} › a) kein gefährliches Werkzeug")], rechts_frei([
    *tafel("na", "Buchstabe a: Waffe?"),
    blk(110, 180, 1040, 150, HELLBLAU, "na1", [("Waffe: nach ihrer Beschaffenheit geeignet,", "Bold", 32, INK),
                                            ("erhebliche Verletzungen zuzufügen", "Bold", 32, INK)]),
    zit("BGH, Urt. v. 11.5.1999 – 4 StR 380/98, BGHSt 45, 92, Rn. 5", 110, 345, beim("na1", "Waffe")),
    *pkt("Spielzeugpistolen ausdrücklich ausgeklammert", 420, "na2", "Bold", 32, x=160),
    zit("BGHSt 45, 92, Rn. 6", 160, 465, beim("na2", "Bundesgerichtshof")),
    *neinz("kein anderes gefährliches Werkzeug:", 540, "na3", "Bold", 32, x=160),
    z("leichtes Plastikspielzeug", 160, 590, beim("na3", "Plastikspielzeug"), "Bold", 32),
    *neinz("Buchstabe a scheidet aus", 680, beim("na3", "scheidet"), "ExtraBold", 34, x=160),
    *requisit([("na", None, "Waffe?", WEISS), ("na2", None, "Spielzeug", GELB), ("na3", None, "Buchstabe a (−)", HELLROT)]),
    pistole(PX, PU, 170, "na"),
    *zwei("OT", [("na", "ruhig"), ("na2", "staunt"), ("na3", "froh")], "AL", [("na", "ernst"), ("na2", "denkt"), ("na3", "still")]),
]))

# ===========================================================================================================================
# E Buchstabe b: Scheinwaffe erfasst
# ===========================================================================================================================
PE = "B. § 250 Abs. 1 Nr. 1 StGB › b)"
folie([("nb", f"{PE} sonst ein Werkzeug oder Mittel"), ("nb1", f"{PE} Gesetzgeber 1998"),
       ("nb2", f"{PE} Beispiel Spielzeugpistole"), ("nb3", f"{PE} BGH: Scheinwaffen erfasst"),
       ("nb4", f"{PE} Verwendungsabsicht"), ("nb5", f"{PE} täuschend echt: erfüllt")], rechts_frei([
    *tafel("nb", "Buchstabe b: Scheinwaffe"),
    *pkt("6. Strafrechtsreformgesetz 1998: Scheinwaffen erfasst", 180, "nb1", "Bold", 30, x=160),
    *pkt("Rechtsausschuss: „z. B. eine Spielzeugpistole“", 240, "nb2", "Bold", 30, x=160),
    zit("Bericht des Rechtsausschusses, BT-Drucks. 13/9064, S. 18", 160, 284, "nb2"),
    blk(110, 340, 1040, 150, HELLBLAU, "nb3", [("BGH: auch objektiv ungefährliche Gegenstände,", "Bold", 31, INK),
                                            ("deren Gefährlichkeit nur vorgetäuscht wird", "Bold", 31, INK)]),
    zit("BGH, Urt. v. 18.1.2007 – 4 StR 394/06, Rn. 6; Beschl. v. 28.3.2023 – 4 StR 61/23, Rn. 5", 110, 502,
        beim("nb3", "Erfasst")),
    *okz("bei sich geführt, um Widerstand durch Drohung", 570, "nb4", "Bold", 31, x=160),
    z("mit Gewalt zu verhindern", 160, 614, beim("nb4", "Drohung"), "Bold", 31),
    *okz("täuschend echt: Drohwirkung vom Gegenstand selbst", 680, "nb5", "Bold", 31, x=160),
    *okz("Buchstabe b erfüllt", 750, beim("nb5", "Buchstabe"), "ExtraBold", 34, x=160),
    *requisit([("nb", None, "sonst ein Mittel?", WEISS), ("nb2", None, "Spielzeugpistole", GELB),
               ("nb5", None, "Buchstabe b (+)", GRUEN)]),
    pistole(PX, PU, 170, "nb"),
    *zwei("AL", [("nb", "ernst"), ("nb4", "still")], "WI", [("nb", "denkt"), ("nb2", "staunt"), ("nb5", "ernst")]),
]))

# ===========================================================================================================================
# F Abwandlung: der Labello-Fall (Fallszene)
# ===========================================================================================================================
LW, LA = 1600, 1780                       # Wiltrud und Alois hinter der Theke, beide blicken nach links
folie([("lab", "C. Grenze › Labello-Fall"), ("lab1", "C. Grenze › Abwandlung: Lippenpflegestift"),
       ("lab2", "C. Grenze › Wiltrud: Messerspitze?")], [
    *baeckerei("lab"),
    *fig("AL", LA, G0, FHA, [(beim("lab1", "Er"), "ernst")]),
    ns("Alois", LA, G0, beim("lab1", "Er"), GRUEN, d=0.1),
    *fig("WI", LW, G0, FHA, [("lab", "ruhig"), (beim("lab1", "Rücken"), "schreck"), ("lab2", "sorge")], erst="cut"),
    ns("Wiltrud", LW, G0, "lab", BLAU),
    *theke("lab"),
    pl("Labello-Fall (BGH NStZ 1997, 184)", 70, 30, beim("lab", "Labello"), fill=GELB, size=32),
    pl("Abwandlung: keine Pistole", 70, 100, "lab1", fill=WEISS, size=32),
    lippenstift(1420, 320, 190, beim("lab1", "Lippenpflegestift")),
    pl("Lippenpflegestift, von hinten in den Rücken", 1000, 170, beim("lab1", "Lippenpflegestift"), fill=WEISS, size=28,
       anker="m"),
    pl("hält ihn für die Spitze eines Messers", 1000, 250, "lab2", fill=HELLROT, size=28, anker="m"),
])

# ===========================================================================================================================
# G1 Die Grenze: offensichtlich ungefährlich
# ===========================================================================================================================
PG = "C. Grenze"
folie([("lab3", f"{PG} › offensichtlich ungefährlich"), ("lab4", f"{PG} › Täuschung im Vordergrund"),
       ("lab5", f"{PG} › objektiver Betrachter"), ("lab6", f"{PG} › Wasserpistole")], rechts_frei([
    *tafel("lab3", "Die Grenze: der Labello-Fall"),
    blk(110, 180, 1040, 150, HELLROT, "lab3", [("äußerlich offensichtlich ungefährlich:", "ExtraBold", 32, INK),
                                            ("nicht Buchstabe b", "ExtraBold", 32, INK)]),
    zit("BGH NStZ 1997, 184 (Labello); BGH 4 StR 394/06, Rn. 7 f.", 110, 345, "lab3"),
    *pkt("Täuschung steht im Vordergrund, nicht der Gegenstand", 410, "lab4", "Bold", 30, x=160),
    *pkt("Maßstab: objektiver Betrachter – nicht, ob das", 480, "lab5", "Bold", 30, x=160),
    z("Opfer den Gegenstand sehen kann", 160, 522, beim("lab5", "nicht"), "Bold", 30),
    zit("4 StR 394/06, Rn. 8; BGH, Beschl. v. 11.5.2011 – 2 StR 618/10, Rn. 4", 160, 566, beim("lab5", "nicht")),
    *neinz("grellbunte Wasserpistole, keiner Waffe ähnlich,", 630, "lab6", "Bold", 30, x=160),
    z("in der Jackentasche verborgen: reicht nicht", 160, 674, beim("lab6", "obwohl"), "Bold", 30),
    zit("2 StR 618/10, Rn. 3–5", 160, 718, beim("lab6", "obwohl")),
    *requisit([("lab3", None, "Lippenpflegestift", WEISS), ("lab5", None, "objektiver Blick", WEISS),
               ("lab6", None, "Wasserpistole", WEISS)]),
    bis_(lippenstift(PX, PU + 20, 150, "lab3"), "lab6"),
    ficon("tabler", "eye", PX + 130, PU, 90, "lab5", fuell=WEISS, bis="lab6"),
    ficon("fluent-emoji-high-contrast", "water-pistol", PX, PU, 170, "lab6", fuell=PINK, nebenfarbe=GELB),
    *stehend("WI", FX, [("lab3", "denkt"), ("lab4", "ernst"), ("lab6", "staunt")]),
]))

# ===========================================================================================================================
# G2 Streitstand: Kritik an der Grenze
# ===========================================================================================================================
folie([("krit", f"{PG} › Kritik der Literatur"), ("krit2", f"{PG} › BGH räumt Spannung ein"),
       ("krit3", f"{PG} › BGH hält an der Grenze fest")], rechts_frei([
    *tafel("krit", "Streitstand: Ist die Grenze richtig?"),
    blk(110, 180, 1040, 150, HELLBLAU, "krit", [("Kritik (Teile der Literatur):", "ExtraBold", 32, INK),
                                             ("Grenze kaum trennscharf", "Bold", 32, INK)]),
    zit("Nachweise bei BGH 4 StR 394/06, Rn. 8", 110, 345, "krit"),
    *pkt("BGH räumt ein: Wortlaut stellt eher auf die", 420, "krit2", "Bold", 31, x=160),
    z("Vorstellung des Täters ab", 160, 464, beim("krit2", "Wortlaut"), "Bold", 31),
    blk(110, 540, 1040, 150, GRUEN, "krit3", [("BGH hält an der Grenze fest,", "ExtraBold", 32, INK),
                                           ("wie vom Gesetzgeber erwartet", "Bold", 32, INK)]),
    zit("4 StR 394/06, Rn. 8; BT-Drucks. 13/9064, S. 18", 110, 705, "krit3"),
    *requisit([("krit", ("tabler", "scale", 120, WEISS), "Streitstand", GELB),
               ("krit3", ("tabler", "scale", 120, WEISS), "Grenze bleibt", GRUEN)]),
    *zwei("OT", [("krit", "denkt"), ("krit3", "ruhig")], "WI", [("krit", "ernst"), ("krit2", "denkt"), ("krit3", "froh")]),
]))

# ===========================================================================================================================
# H § 250 Abs. 2 Nr. 1 StGB (Wortlautkarte): verwendet
# ===========================================================================================================================
W2 = umbruch("„(2) Auf Freiheitsstrafe nicht unter fünf Jahren ist zu erkennen, wenn der Täter oder ein anderer "
             "Beteiligter am Raub 1. bei der Tat eine Waffe oder ein anderes gefährliches Werkzeug verwendet, …“", 31, 1040)
w2, w2_y = wortlaut(80, 175, 1100, W2, "§ 250 Abs. 2 Nr. 1 StGB (Auszug)", "w2",
                    marken=[(_zl(W2, "fünf Jahren"), "fünf Jahren", beim("w2", "fünf")),
                            (_zl(W2, "verwendet"), "verwendet", beim("w2", "verwendet"))], size=31)
PH = "D. § 250 Abs. 2 Nr. 1 StGB"
folie([("abs2", PH), ("w2", f"{PH} › Wortlaut"), ("v1", f"{PH} › Verwenden: auch als Drohmittel"),
       ("v2", f"{PH} › keine Waffe"), ("v3", f"{PH} › Scheinwaffe: nur Abs. 1 Nr. 1 b")], rechts_frei([
    *tafel("abs2", "Und Absatz 2?"),
    *w2,
    *okz("Verwenden: auch als Drohmittel – das tut Alois", w2_y + 35, "v1", "Bold", 31, x=160),
    zit("BGHSt 45, 92, Rn. 7", 160, w2_y + 79, "v1"),
    *neinz("Spielzeugpistole: keine Waffe, kein gefährliches", w2_y + 140, "v2", "Bold", 31, x=160),
    z("Werkzeug", 160, w2_y + 184, beim("v2", "Werkzeug"), "Bold", 31),
    blk(110, w2_y + 250, 1040, 115, GELB, "v3", [("st. Rspr.: Scheinwaffe als Drohmittel", "ExtraBold", 31, INK),
                                              ("nicht Abs. 2 Nr. 1, sondern Abs. 1 Nr. 1 b", "Bold", 31, INK)]),
    zit("BGH, Beschl. v. 6.9.2007 – 4 StR 227/07, Rn. 3", 110, w2_y + 378, "v3"),
    *requisit([("abs2", ("tabler", "scale", 120, WEISS), "5 Jahre?", HELLROT),
               ("v1", None, "als Drohmittel", WEISS), ("v2", None, "keine Waffe", HELLROT),
               ("v3", None, "Abs. 1 Nr. 1 b", GRUEN)]),
    pistole(PX, PU, 170, "v1"),
    *zwei("AL", [("abs2", "ernst"), ("v2", "still")], "OT", [("abs2", "ruhig"), ("v1", "denkt"), ("v3", "froh")]),
]))
assert w2_y + 378 + 40 <= 900, w2_y

# ===========================================================================================================================
# I Ergebnis (Fallszene)
# ===========================================================================================================================
folie([("erg", "Ergebnis · Spielzeugpistole: § 250 Abs. 1 Nr. 1 b StGB"), ("erg2", "Ergebnis · Mindeststrafe 3 Jahre"),
       ("erg3", "Ergebnis · Lippenpflegestift: § 249 StGB")], [
    *baeckerei("erg"),
    *fig("WI", WX, G0, FHA, [("erg", "ernst"), ("erg3", "ruhig")], erst="cut"),
    ns("Wiltrud", WX, G0, "erg", BLAU),
    *theke("erg"),
    *fig("OT", OX, G0, FHA, [("erg", "ernst_r"), ("erg2", "denkt_r")], erst="cut"),
    ns("Ottfried", OX, G0, "erg", GELB),
    pistole(OX - 120, 700, 110, "erg", anim="cut"),
    pl("Spielzeugpistole: § 250 Abs. 1 Nr. 1 b StGB", 70, 30, beim("erg", "Spielzeugpistole"), fill=GELB, size=32),
    pl("Mindeststrafe: 3 Jahre, nicht 5", 70, 100, "erg2", fill=WEISS, size=32),
    pl("Lippenpflegestift: Raub, § 249 StGB", 70, 170, "erg3", fill=WEISS, size=32),
    lippenstift(1160, 330, 170, beim("erg3", "Lippenpflegestift")),
])

# ===========================================================================================================================
# J Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · vom schwersten Fall her"), ("tipp2", "Klausurtipp · zuerst Abs. 2 Nr. 1"),
       ("tipp3", "Klausurtipp · dann Abs. 1 Nr. 1 a und b"), ("tipp4", "Klausurtipp · Labello-Grenze")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("§ 250 StGB vom schwersten Fall her prüfen", 200, 200, beim("tipp", "Prüfe"), "Bold", 36),
    *pkt("1. Abs. 2 Nr. 1: Waffe verwendet?", 300, "tipp2", "Bold", 34, x=245),
    *pkt("2. sonst Abs. 1 Nr. 1 a, dann b", 380, "tipp3", "Bold", 34, x=245),
    linienzug([(130, 470), (1130, 470)], "tipp4", breite=3),
    *pkt("bei b die Labello-Grenze ansprechen:", 500, "tipp4", "Bold", 34, x=245),
    z("äußerlich offensichtlich ungefährlich?", 245, 552, beim("tipp4", "äußerlich"), "Regular", 34),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# K Klausurschema
# ===========================================================================================================================
REIHEN = [("s1", 0, "I. Raub, § 249 StGB", True),
          ("s2", 0, "II. Qualifikation, § 250 StGB", True),
          ("s2a", 1, "1. Abs. 2 Nr. 1: Waffe oder gefährliches Werkzeug verwendet", False),
          ("s2b", 1, "2. Abs. 1 Nr. 1 a: bei sich geführt", False),
          ("s2c", 1, "3. Abs. 1 Nr. 1 b: sonst ein Werkzeug oder Mittel,", False),
          ("s2c2", 1, "    mit Verwendungsabsicht", False),
          ("s2d", 1, "    nicht offensichtlich ungefährlich", False),
          ("s2e", 1, "+ Vorsatz für die Qualifikation", False),
          ("s3", 0, "III. Rechtswidrigkeit und Schuld", True)]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Schema: Schwerer Raub, § 250 StGB"), 110, 90, "sch", 46)]
y = 215
for c, ebene, text, fett in REIHEN:
    x = (130, 200)[ebene]
    cue = beim("s2c", "Verwendungsabsicht") if c == "s2c2" else c
    els_sch.append(z(text, x, y, cue, "ExtraBold" if fett else "Regular", 40 if ebene == 0 else 36, rechts=1800))
    y += {0: 88, 1: 76}[ebene] if c not in ("s2c", "s2c2") else 58
assert y <= 970, y
folie([("sch", "Klausurschema"), ("s1", "Klausurschema › I. Raub"), ("s2", "Klausurschema › II. Qualifikation"),
       ("s2a", "Klausurschema › II. 1. Abs. 2 Nr. 1"), ("s2b", "Klausurschema › II. 2. Abs. 1 Nr. 1 a"),
       ("s2c", "Klausurschema › II. 3. Abs. 1 Nr. 1 b"), ("s2e", "Klausurschema › Vorsatz"),
       ("s3", "Klausurschema › III. Rechtswidrigkeit und Schuld")], els_sch)

# ===========================================================================================================================
# L Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Eine Scheinwaffe ist ", 0), ("keine Waffe", "a"), (",", 0)], [("aber ein ", 0),
                  ("sonstiges Mittel", "b"), (" nach", 0)], [("Abs. 1 Nr. 1 b.", 0)]], 750, 270, 44, "merke",
                {"a": beim("merke", "keine"), "b": beim("merke", "sonstiges")}),
    *markertext([[("Wirkt der Gegenstand äußerlich", 0)], [("offensichtlich harmlos", "c"), (", droht der", 0)],
                 [("Täter nur durch ", 0), ("Täuschung", "d"), (".", 0)]], 750, 500, 44, "mk2",
                {"c": beim("mk2", "offensichtlich"), "d": beim("mk2", "Täuschung")}),
    *markertext([[("Dann bleibt es beim ", 0), ("einfachen Raub", "e"), (".", 0)]], 750, 760, 44, "mk3",
                {"e": beim("mk3", "einfachen")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
