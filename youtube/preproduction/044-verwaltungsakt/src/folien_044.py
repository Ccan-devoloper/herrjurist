"""Folge 044 · Verwaltungsakt § 35 VwVfG: Alle Merkmale in sechs Minuten – Serienstandard Open Peeps (Katzenkönig).
Übungsfall (Kaffeewagen auf dem Marktplatz), Figuren fiktiv. Szenen laut ../SZENENPLAN.md:
A Marktplatz am Samstag (Bescheid, Unwetter, Durchsagen), B Montag: das neue Schild, C Die Frage, D Sachverhalt,
E Wortlaut § 35 Satz 1, F 1. hoheitliche Maßnahme, G 2. Behörde, H 3. öffentliches Recht, I 4. Regelung,
J 4. Regelung: Abgrenzung, K 5. Einzelfall, L Wortlaut § 35 Satz 2 (Allgemeinverfügung), M Verkehrszeichen,
N 6. Außenwirkung (Rathaus), O Ergebnis, P Bedeutung: Klageart, Q Frist und Vollstreckung, R Klausurtipp (Lexi),
S Klausurschema, T Merksatz (Lexi).
Geräusch nur bei sichtbarer Handlung (Donner, wenn die Gewitterwolke über dem Marktplatz erscheint)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_044/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
ZITAT = (246, 246, 250, 255)
GRAU = (176, 178, 190, 255)
HOLZ = (236, 214, 178, 255)
HC = "fluent-emoji-high-contrast"
DAUER = bausteine._cj()["dauer"]
T_ = bausteine._t

_CMAP = set(TTFont(SP + "humaaans/fonts/Nunito[wght].ttf").getBestCmap())


def glyphen(text):
    """Nunito muss jedes Zeichen haben (sonst Kästchen)."""
    fehl = {c for c in text if ord(c) not in _CMAP and not c.isspace()}
    assert not fehl, f"Zeichen fehlt in Nunito: {fehl} in {text!r}"
    return text


def z(text, x, y, cue, stil="Regular", size=34, farbe=INK, d=0.0, rechts=1170, **k):
    """Tafelzeile, die rechts nicht über die Karte hinausragen darf."""
    e = zeile(glyphen(text), x, y, cue, stil, size, farbe=farbe, d=d, **k)
    assert e.x + e.sprite.width <= rechts, f"Zeile zu breit: {text} ({e.x + e.sprite.width:.0f} > {rechts})"
    return e


def pl(text, *a, **k):
    return pille(glyphen(text), *a, **k)


def tafel(cue, titel_, h=840, fill=WEISS, size=46):
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(glyphen(titel_), 110, 100, cue, size)]


def blk(x, y, w, h, fill, cue, zeilen, **k):
    return fl_block(x, y, w, h, fill, cue, [(glyphen(t), s, g, f) for t, s, g, f in zeilen], **k)


def bis_(el, bis):
    el.bis = bis
    return el


def hart(e):
    e.anim = "cut"
    return e


def lexi_bis_ende(cue):
    return (cue, round(DAUER - T_(cue) - 0.05, 3))


def zit(text, x, y, cue, size=26):
    """Fundstellenzeile (grau, klein)."""
    return z(text, x, y, cue, size=size, farbe=TEXT)


def rechts_frei(els, x0=1250):
    """Figuren und Requisiten der Tafelfolien stehen rechts der Tafel."""
    for e in els:
        n = e.name or ""
        if n.startswith(("bild:", "ficon:")) or "/op_044/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els




def wortlaut(x, y, w, text, quelle, cue, marken=(), size=32, bis=None):
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de, als Zitat mit Normangabe, automatisch umbrochen.
    marken = [(Wortgruppe, cue)] legt synchron zum gesprochenen Wort einen Textmarker hinter die Wortgruppe
    (die Wortgruppe muss in einer Zeile stehen)."""
    f = F("Regular", size)
    tx, ty = x + 28, y + 26
    breite = w - 56
    zeilen, cur = [], ""
    for wort in text.split():
        t = (cur + " " + wort).strip()
        if f.getlength(t) <= breite:
            cur = t
        else:
            zeilen.append(cur); cur = wort
    zeilen.append(cur)
    lh = int(size * 1.42)
    hgt = 40 + lh * len(zeilen) + 46
    els = [bis_(karte(x, y, w, hgt, cue, fill=ZITAT, rund=18, schatten=6, rand=4), bis)]
    for wort, mc in marken:
        zi = next((i for i, t in enumerate(zeilen) if wort in t), None)
        assert zi is not None, f"Marker {wort!r} steht nicht in einer Zeile: {zeilen}"
        t = zeilen[zi]; a = t.index(wort)
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


# --- Eigene Hilfsfunktion (wie Folge 020/025/028/032): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ------
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


def schild(text, cx, cue, fill, d=0.2, bis=None, unten=None, size=28):
    """Namensschild unter der Figur (ab dem ersten Auftritt, solange sie im Bild ist)."""
    return pl(text, cx, (unten or FB) + 22, cue, fill=fill, size=size, anker="m", d=d, bis=bis)


BODEN, FH = 880, 480
FX, FB, FR = 1560, 930, 460                 # Figur neben der Tafel
IX, IU = 1560, 400                          # Requisit über der Figur
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
WI_F, LO_F, GO_F, KE_F = GELB, BLAU, LILA, GRUEN   # Farben der Namensschilder
K1, K2, K3 = 150, 210, 270
VA = "Verwaltungsakt"


def haltverbot(cx, cy, r, cue, bis=None, mast=True, boden=BODEN, anim="pop"):
    """Haltverbotsschild als Baustein (Zeichen 283 StVO nachempfunden): blaue Scheibe, roter Ring, rotes Kreuz,
    Tuschekontur; optional mit Mast bis zum Boden."""
    s = 2 * r + 12
    im = Image.new("RGBA", (s, s))
    d = ImageDraw.Draw(im)
    d.ellipse((6, 6, s - 6, s - 6), fill=ROT, outline=INK, width=5)
    ri = int(r * 0.74)
    c = s // 2
    d.ellipse((c - ri, c - ri, c + ri, c + ri), fill=BLAU, outline=INK, width=4)
    k = int(ri * 0.70)
    for (x0, y0, x1, y1) in ((c - k, c - k, c + k, c + k), (c - k, c + k, c + k, c - k)):
        d.line((x0, y0, x1, y1), fill=INK, width=int(r * 0.26))
        d.line((x0, y0, x1, y1), fill=ROT, width=int(r * 0.17))
    els = []
    if mast:
        els.append(bis_(linienzug([(cx, cy + r), (cx, boden)], cue, breite=10, farbe=INK), bis))
        if anim == "cut":
            els[-1].anim = "cut"
    els.append(El(im, cx - s / 2, cy - s / 2, cue, anim, 0.0, bis, name="baustein:haltverbot"))
    return els


def wagen(cx, cue, anim="pop"):
    """Kaffeewagen: Wohnanhänger-Icon (Tabler caravan) mit Kaffeetasse (Tabler coffee) und Schild."""
    return [ficon("tabler", "caravan", cx, BODEN - 2, 330, cue, fuell=GELB, anim=anim),
            ficon("tabler", "coffee", cx - 20, BODEN - 215, 90, cue, fuell=WEISS, anim=anim),
            pl("Kaffee", cx + 85, BODEN - 260, cue, fill=WEISS, size=26, anker="m", anim=anim)]


def reihe(cue, cues, y=560, anim="pop"):
    """Die vier Maßnahmen des Falls nebeneinander (Szene C und O): Brief, 1. und 2. Durchsage, Schild.
    cues = Erscheinen je Maßnahme."""
    xs = (250, 640, 1030, 1420)
    c1, c2, c3, c4 = cues
    els = [
        ficon("tabler", "file-text", xs[0], y, 170, c1, fuell=WEISS, anim=anim),
        pl("Bescheid", xs[0], y + 40, c1, fill=WEISS, size=30, anker="m", anim=anim),
        ficon("ph", "megaphone", xs[1], y, 170, c2, fuell=GELB, anim=anim),
        pl("1. Durchsage: Warnung", xs[1], y + 40, c2, fill=WEISS, size=30, anker="m", anim=anim),
        ficon("ph", "megaphone", xs[2], y, 170, c3, fuell=ORANGE, anim=anim),
        pl("2. Durchsage: Räumung", xs[2], y + 40, c3, fill=WEISS, size=30, anker="m", anim=anim),
        *haltverbot(xs[3], y - 85, 80, c4, mast=False, anim=anim),
        pl("Schild: Haltverbot", xs[3], y + 40, c4, fill=WEISS, size=30, anker="m", anim=anim),
    ]
    return els, xs


# A Fall: Samstag auf dem Marktplatz – Bescheid, Unwetter, Durchsagen ---------------------------------------------------
WIX, LOX, GOX = 960, 1560, 1560
WIb = ("WI_redet_r", WIX, BODEN, FH)
LOb = ("LO_redet", LOX, BODEN, FH)
GOb = ("GO_redet", GOX, BODEN, FH)
KOMMT = beim("lorenz", "kommt")
MITTAG = "mittag"
POL = beim("goebel", "Polizist")
DONNER = beim("donner", "donnert")
folie([(NULL, "Fall · Samstag auf dem Marktplatz"), ("lorenz", "Fall · Ein Brief vom Amt"),
       (MITTAG, "Fall · Durchsagen der Polizei")], [
    hart(linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK)),
    hart(pl("Samstag auf dem Marktplatz", 70, 40, NULL, fill=GELB, size=40)),
    ficon(HC, "classical-building", 230, BODEN - 2, 300, NULL, fuell=WEISS, anim="cut"),
    hart(pl("Rathaus", 230, BODEN + 22, NULL, fill=WEISS, size=26, anker="m")),
    *wagen(590, NULL, anim="cut"),
    ficon("tabler", "umbrella", 590, BODEN - 330, 150, NULL, fuell=ROT, anim="cut", bis=DONNER),
    ficon("tabler", "sun", 1760, 190, 120, NULL, fuell=GELB, anim="cut", bis=MITTAG),
    ficon("tabler", "users", 1240, BODEN - 2, 150, NULL, fuell=WEISS, anim="cut", bis=beim("go2", "verlassen")),
    # Frau Wiegand
    *fig("WI", WIX, BODEN, FH, [(NULL, "ruhig_r"), (beim("lo1", "abgelehnt"), "sorge_r")], bis="wi1", erst="cut"),
    *redet("WI_redet_r", WIX, BODEN, FH, "wi1", MITTAG),
    *fig("WI", WIX, BODEN, FH, [(MITTAG, "denkt_r"), ("donner", "sorge_r")], erst="cut"),
    hart(schild("Frau Wiegand, Kaffeewagen", WIX, NULL, WI_F, unten=BODEN, d=0.0)),
    # Herr Lorenz bringt den Bescheid
    *fig("LO", LOX, BODEN, FH, [(KOMMT, "ruhig")], bis="lo1"),
    *redet("LO_redet", LOX, BODEN, FH, "lo1", "wi1"),
    bis_(peep_voll("LO_ruhig", LOX, BODEN, FH, "wi1", anim="cut"), MITTAG),
    schild("Herr Lorenz, Ordnungsamt", LOX, KOMMT, LO_F, unten=BODEN, d=0.0, bis=MITTAG),
    ficon("tabler", "file-text", 1400, 690, 90, beim("lorenz", "Brief"), fuell=WEISS, bis=MITTAG),
    blase("sprech", 780, 220, "lo1", 1290, 220, inhalt=["Frau Wiegand, Ihr Antrag auf einen", "festen Standplatz ist abgelehnt.",
                                                      "Hier ist der Bescheid."], textsize=30, figur=LOb, bis="wi1"),
    blase("sprech", 640, 190, "wi1", 860, 250, inhalt=["Abgelehnt? Ich stehe hier", "seit zwanzig Jahren!"],
          textsize=32, figur=WIb, bis=MITTAG),
    # Mittags: Wind, Polizist Göbel, Unwetter
    pl("Mittags", 70, 125, MITTAG, fill=WEISS, size=34),
    ficon("tabler", "cloud", 1760, 210, 150, beim(MITTAG, "Wind"), fuell=WEISS, bis=DONNER),
    ficon(HC, "wind-face", 1560, 200, 130, beim(MITTAG, "Wind"), fuell=WEISS, bis=POL),
    *fig("GO", GOX, BODEN, FH, [(POL, "ruhig")], bis="go1"),
    *redet("GO_redet", GOX, BODEN, FH, "go1", "donner"),
    bis_(peep_voll("GO_ruhig", GOX, BODEN, FH, "donner", anim="cut"), "go2"),
    *redet("GO_redet", GOX, BODEN, FH, "go2", "montag"),
    schild("Polizist Göbel", GOX, POL, GO_F, unten=BODEN, d=0.0),
    ficon("ph", "megaphone", 1420, 560, 110, beim("goebel", "Megafon"), fuell=GELB),
    blase("sprech", 700, 190, "go1", 1200, 230, inhalt=["Achtung! Heute Nachmittag", "zieht ein Unwetter auf."],
          textsize=32, figur=GOb, bis="donner"),
    szene(ficon("tabler", "cloud-storm", 1760, 230, 190, DONNER, fuell=GRAU), "044donner*", 0.9, -0.49),
    ficon("tabler", "bolt", 1180, 260, 110, DONNER, fuell=GELB, bis="go2"),
    blase("sprech", 760, 190, "go2", 1200, 230, inhalt=["Das Unwetter ist da. Alle verlassen", "sofort den Marktplatz!"],
          textsize=30, figur=GOb),
])

# B Fall: Montag – das neue Schild ---------------------------------------------------------------------------------------
WBX = 1560
WBb = ("WI_redet", WBX, BODEN, FH)
SCHILD = beim("montag", "Schild")
folie([("montag", "Fall · Montag: ein neues Schild")], [
    linienzug([(60, BODEN), (1860, BODEN)], "montag", breite=7, farbe=INK),
    pl("Montag", 70, 40, "montag", fill=GELB, size=40),
    karte(260, BODEN - 4, 760, 44, "montag", fill=GELB, rund=8, schatten=0, rand=4),
    pl("Ladezone", 640, BODEN + 70, beim("montag", "Ladezone"), fill=WEISS, size=28, anker="m"),
    *wagen(560, "montag"),
    ficon("tabler", "building-community", 230, BODEN - 2, 260, "montag", fuell=WEISS),
    *haltverbot(1050, 470, 95, SCHILD),
    pl("Haltverbot", 1050, 330, beim("montag", "Haltverbot"), fill=ROT, size=32, anker="m"),
    *fig("WI", WBX, BODEN, FH, [("montag", "ruhig"), (SCHILD, "denkt")], bis="wi2"),
    *redet("WI_redet", WBX, BODEN, FH, "wi2", "frage"),
    schild("Frau Wiegand", WBX, "montag", WI_F, unten=BODEN),
    blase("sprech", 600, 170, "wi2", 1450, 210, inhalt=["Und wo soll ich", "jetzt ausladen?"], textsize=34, figur=WBb),
])

# C Die Frage --------------------------------------------------------------------------------------------------------------
reihe_c, RX = reihe("frage", (beim("frage", "Brief"), beim("frage", "zwei"), beim("frage", "Durchsagen"),
                              beim("frage", "Verkehrsschild")))
WCX = 1730
folie([("frage", "Fall · Was davon ist ein Verwaltungsakt?")], [
    *reihe_c,
    pl("Was davon ist ein Verwaltungsakt?", 960, 70, beim("frage", "Was"), fill=PINK, size=42, anker="m"),
    pl("6 Merkmale", 840, 800, beim("frage2", "sechs"), fill=GELB, size=36, anker="m"),
    pl("Wie kann sie sich wehren?", 840, 890, beim("frage2", "entscheidet"), fill=WEISS, size=32, anker="m"),
    *fig("WI", WCX, BODEN, FH - 60, [("frage", "denkt"), (beim("frage2", "wehren"), "entschl")]),
    schild("Frau Wiegand", WCX, "frage", WI_F, unten=BODEN),
])

# D Sachverhalt --------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Frau Wiegand verkauft Kaffee aus einem kleinen Wagen auf dem Marktplatz. Herr Lorenz vom Ordnungsamt übergibt ihr einen "
    "Bescheid: Ihr Antrag auf eine Erlaubnis für einen festen Standplatz wird abgelehnt. Mittags warnt Polizist Göbel per "
    "Megafon vor einem Unwetter. Als es kurz darauf donnert, ordnet er an: Alle verlassen sofort den Marktplatz. Am Montag "
    "steht vor ihrer Ladezone ein neues Haltverbotsschild. Im Rathaus teilt Amtsleiterin Kessler dem Beamten Lorenz mit, "
    "dass er ab Montag im Bürgerbüro arbeitet.",
    "Bearbeitervermerk: Die Standplatzerlaubnis richtet sich nach öffentlichem Recht.",
], "Welche dieser Maßnahmen sind Verwaltungsakte?")

# E Wortlaut § 35 Satz 1 VwVfG ------------------------------------------------------------------------------------------------
W351 = ("„Verwaltungsakt ist jede Verfügung, Entscheidung oder andere hoheitliche Maßnahme, die eine Behörde zur "
        "Regelung eines Einzelfalls auf dem Gebiet des öffentlichen Rechts trifft und die auf unmittelbare Rechtswirkung "
        "nach außen gerichtet ist.“")
w351, w351_y = wortlaut(80, 180, 1100, W351, "§ 35 Satz 1 VwVfG", "wl35", marken=[
    ("Verwaltungsakt", beim("wl35", "Verwaltungsakt")), ("Verfügung, Entscheidung", beim("wl35", "Verfügung")),
    ("hoheitliche Maßnahme,", beim("wl35", "hoheitliche")), ("Behörde", beim("wl35", "Behörde")),
    ("Regelung", beim("wl35", "Regelung")), ("Einzelfalls", beim("wl35", "Einzelfalls")),
    ("öffentlichen Rechts", beim("wl35", "öffentlichen")), ("Rechtswirkung", beim("wl35", "Rechtswirkung"))], size=36)
folie([("wl35", "Norm · § 35 Satz 1 VwVfG")], rechts_frei([
    titel(glyphen("Was ist ein Verwaltungsakt?"), 110, 80, "wl35", 50),
    *w351,
    pl("6 Merkmale", 110, w351_y + 40, "sechs", fill=GELB, size=36),
    z("Länder: eigene Verfahrensgesetze, meist gleicher Wortlaut", 110, w351_y + 140, "land", "Bold", 34),
    zit("in deinem Land ggf. andere Fundstelle, z. B. Art. 35 BayVwVfG, § 35 LVwVfG BW", 110, w351_y + 195,
        beim("land", "Wortlaut")),
    ficon("tabler", "book", IX, IU, 140, "wl35", fuell=GELB),
    *fig("WI", FX, FB, FR, [("wl35", "ruhig"), ("sechs", "denkt")]),
    schild("Frau Wiegand", FX, "wl35", WI_F),
]))

# F 1. hoheitliche Maßnahme ---------------------------------------------------------------------------------------------------
folie([("m1", f"{VA} › 1. hoheitliche Maßnahme")], rechts_frei([
    *tafel("m1", "1. hoheitliche Maßnahme"),
    z("Verfügung, Entscheidung oder", 110, 190, beim("m1", "Verfügung"), "Bold", 36),
    z("andere hoheitliche Maßnahme", 110, 245, beim("m1", "andere"), "Bold", 36),
    z("hoheitlich: Die Behörde entscheidet einseitig,", 110, 340, "einseitig", size=34),
    z("der Bürger muss nicht zustimmen", 150, 395, beim("einseitig", "Bürger"), size=34),
    z("Vertrag mit Frau Wiegand, § 54 VwVfG:", 110, 490, "vertrag", "Bold", 34),
    nein(150, 568, beim("vertrag", "Einseitigkeit"), gr=20),
    z("keine Einseitigkeit, kein Verwaltungsakt", 195, 545, beim("vertrag", "Einseitigkeit"), size=34),
    zit("§ 54 Satz 2 VwVfG („anstatt einen Verwaltungsakt zu erlassen“)", 150, 610, beim("vertrag", "Einseitigkeit")),
    ficon("tabler", "file-text", IX, IU, 120, "m1", fuell=WEISS, bis="vertrag"),
    ficon("ph", "handshake", IX, IU, 160, "vertrag", fuell=GELB),
    *fig("WI", FX, FB, FR, [("m1", "ruhig"), ("vertrag", "denkt")]),
    schild("Frau Wiegand", FX, "m1", WI_F),
]))

# G 2. Behörde ----------------------------------------------------------------------------------------------------------------
folie([("beh0", f"{VA} › 2. Behörde, § 1 IV VwVfG")], rechts_frei([
    *tafel("beh0", "2. Behörde"),
    z("§ 1 IV VwVfG: jede Stelle, die Aufgaben", 110, 190, beim("beh0", "Nach"), "Bold", 36),
    z("der öffentlichen Verwaltung wahrnimmt", 110, 245, beim("beh0", "Aufgaben"), "Bold", 36),
    ok(150, 365, beim("beh", "Ordnungsamt"), gr=20), z("Ordnungsamt", 195, 342, beim("beh", "Ordnungsamt"), size=34),
    ok(510, 365, beim("beh", "Polizei"), gr=20), z("Polizei", 555, 342, beim("beh", "Polizei"), size=34),
    z("Gericht: spricht Recht", 110, 450, "gericht", "Bold", 34),
    nein(150, 528, beim("gericht", "Urteil"), gr=20),
    z("Urteil: kein Verwaltungsakt", 195, 505, beim("gericht", "Urteil"), size=34),
    zit("Art. 92 GG: rechtsprechende Gewalt", 150, 570, beim("gericht", "Urteil")),
    ficon("tabler", "building", IX - 110, IU, 120, beim("beh", "Ordnungsamt"), fuell=WEISS, bis="gericht"),
    ficon("ph", "megaphone", IX + 100, IU, 110, beim("beh", "Polizei"), fuell=GELB, bis="gericht"),
    ficon("tabler", "gavel", IX, IU, 130, "gericht", fuell=HOLZ),
    *fig("GO", FX, FB, FR, [("beh0", "ruhig")]),
    schild("Polizist Göbel", FX, "beh0", GO_F),
]))

# H 3. öffentliches Recht --------------------------------------------------------------------------------------------------------
folie([("m3", f"{VA} › 3. auf dem Gebiet des öffentlichen Rechts")], rechts_frei([
    *tafel("m3", "3. öffentliches Recht"),
    z("auf dem Gebiet des öffentlichen Rechts", 110, 185, beim("m3", "Gebiet"), size=34, farbe=TEXT),
    z("Befugnis, die Privatleuten nicht zusteht", 110, 245, beim("m3", "Befugnis"), "Bold", 36),
    ok(150, 323, beim("m3", "Erlaubnis"), gr=20),
    z("hier: Erlaubnis für den Standplatz", 195, 300, beim("m3", "Erlaubnis"), size=34),
    zit("vgl. BVerwG, Beschl. v. 6.7.2022 – 3 B 40.21, Rn. 10", 195, 355, beim("m3", "Standplatz")),
    z("Stadt kündigt die gemietete Garage:", 110, 445, "garage", "Bold", 34),
    z("wie jeder Vermieter, nach dem BGB", 150, 500, beim("garage", "Vermieter"), size=34),
    blk(110, 585, 1040, 85, ROT, beim("garage", "Privatrecht"), [("Privatrecht: kein Verwaltungsakt", "ExtraBold", 34, INK)]),
    nein(1110, 628, beim("garage", "Privatrecht"), gr=22),
    ficon("tabler", "file-text", IX, IU, 120, beim("m3", "Erlaubnis"), fuell=WEISS, bis="garage"),
    ficon("ph", "garage", IX, IU, 170, "garage", fuell=WEISS),
    *fig("WI", FX, FB, FR, [("m3", "ruhig"), ("garage", "sorge")]),
    schild("Frau Wiegand", FX, "m3", WI_F),
]))

# I 4. Regelung -------------------------------------------------------------------------------------------------------------------
folie([("m4", f"{VA} › 4. Regelung")], rechts_frei([
    *tafel("m4", "4. Regelung"),
    z("Behörde will eine verbindliche Rechtsfolge setzen:", 110, 190, beim("m4", "Behörde"), "Bold", 38),
    pl("begründen", 110, 265, beim("m4", "begründen"), fill=WEISS, size=30),
    pl("ändern", 330, 265, beim("m4", "ändern"), fill=WEISS, size=30),
    pl("aufheben", 490, 265, beim("m4", "aufheben"), fill=WEISS, size=30),
    pl("feststellen", 700, 265, beim("m4", "feststellen"), fill=WEISS, size=30),
    pl("verneinen", 930, 265, beim("m4", "verneinen"), fill=WEISS, size=30),
    zit("BVerwG, Urt. v. 25.3.2026 – 7 C 4.25, Rn. 10", 110, 355, beim("m4", "verneinen")),
    ok(150, 470, beim("abl", "verneint"), gr=20),
    z("Ablehnung: verneint den Standplatz verbindlich", 195, 447, beim("abl", "verneint"), size=34),
    blk(110, 530, 1040, 85, GRUEN, beim("abl", "Regelung"), [("Regelung", "ExtraBold", 38, INK)]),
    ficon("tabler", "file-text", IX, IU, 120, "m4", fuell=WEISS),
    pl("abgelehnt", IX, IU + 20, beim("abl", "verneint"), fill=ROT, size=28, anker="m"),
    *fig("LO", FX, FB, FR, [("m4", "ruhig")]),
    schild("Herr Lorenz", FX, "m4", LO_F),
]))

# J 4. Regelung: Abgrenzung ---------------------------------------------------------------------------------------------------------
folie([("hinw", f"{VA} › 4. Regelung › Hinweis, Auskunft, Realakt"), ("gebot", f"{VA} › 4. Regelung › Gebot")], rechts_frei([
    *tafel("hinw", "4. Regelung: Abgrenzung"),
    nein(150, 213, beim("hinw", "warnt"), gr=18),
    z("1. Durchsage: warnt nur, keine Rechtsfolge", 195, 190, beim("hinw", "warnt"), size=34),
    zit("Hinweis: vgl. BVerwG, 7 C 4.25, Rn. 10", 195, 245, beim("hinw", "Rechtsfolge")),
    nein(150, 343, beim("ausk", "Auskunft"), gr=18),
    z("Auskunft am Telefon:", 195, 320, beim("ausk", "Auskunft"), size=34),
    z("„Ihr Antrag hat wohl wenig Chancen.“", 195, 372, beim("ausk", "Ihr"), size=34, farbe=TEXT),
    nein(150, 473, beim("real", "Realakt"), gr=18),
    z("Bauhof räumt Schirme weg: Realakt,", 195, 450, beim("real", "Räumt"), size=34),
    z("tatsächliches Handeln ohne Rechtsfolge", 195, 502, beim("real", "tatsächliches"), size=34),
    ok(150, 603, beim("gebot", "gebietet"), gr=20),
    z("2. Durchsage gebietet: Alle verlassen den Platz", 195, 580, beim("gebot", "gebietet"), "Bold", 34),
    blk(110, 650, 1040, 85, GRUEN, beim("gebot", "Regelung"), [("Regelung", "ExtraBold", 38, INK)]),
    ficon("ph", "megaphone", IX, IU, 120, "hinw", fuell=GELB, bis="ausk"),
    ficon("tabler", "device-landline-phone", IX, IU, 120, "ausk", fuell=WEISS, bis="real"),
    ficon("ph", "broom", IX - 70, IU, 120, "real", fuell=HOLZ, bis="gebot"),
    ficon("tabler", "umbrella", IX + 80, IU, 110, beim("real", "Schirme"), fuell=ROT, bis="gebot"),
    ficon("ph", "megaphone", IX, IU, 140, "gebot", fuell=ORANGE),
    *fig("GO", FX, FB, FR, [("hinw", "ruhig"), ("gebot", "denkt")]),
    schild("Polizist Göbel", FX, "hinw", GO_F),
]))

# K 5. Einzelfall -------------------------------------------------------------------------------------------------------------------
folie([("m5", f"{VA} › 5. Einzelfall")], rechts_frei([
    *tafel("m5", "5. Einzelfall"),
    z("klassisch: eine bestimmte Person, ein konkreter Fall", 110, 190, beim("m5", "Klassisch"), "Bold", 36),
    ok(150, 268, beim("m5", "Antrag"), gr=20),
    z("der Antrag von Frau Wiegand", 195, 245, beim("m5", "Antrag"), size=34),
    z("unbestimmt viele gleichartige Fälle,", 110, 355, beim("norm", "unbestimmt"), "Bold", 36),
    z("etwa Satzung für alle künftigen Märkte", 150, 410, beim("norm", "Satzung"), size=34),
    blk(110, 490, 1040, 85, ROT, beim("norm", "Rechtsnorm"), [("Rechtsnorm, kein Einzelfall", "ExtraBold", 36, INK)]),
    zit("BVerwG, Urt. v. 22.1.2021 – 6 C 26.19, Rn. 26", 110, 605, beim("norm", "Rechtsnorm")),
    ficon("tabler", "user", IX, IU, 120, "m5", fuell=WEISS, bis="norm"),
    ficon("tabler", "book", IX, IU, 130, "norm", fuell=BLAU),
    *fig("WI", FX, FB, FR, [("m5", "ruhig")]),
    schild("Frau Wiegand", FX, "m5", WI_F),
]))

# L Wortlaut § 35 Satz 2: Allgemeinverfügung ---------------------------------------------------------------------------------------
W352 = ("„Allgemeinverfügung ist ein Verwaltungsakt, der sich an einen nach allgemeinen Merkmalen bestimmten oder "
        "bestimmbaren Personenkreis richtet oder die öffentlich-rechtliche Eigenschaft einer Sache oder ihre Benutzung "
        "durch die Allgemeinheit betrifft.“")
w352, w352_y = wortlaut(80, 170, 1100, W352, "§ 35 Satz 2 VwVfG", "wl352", marken=[
    ("Personenkreis", beim("av1", "Personenkreis")), ("öffentlich-rechtliche Eigenschaft", beim("av2", "öffentlich-rechtliche")), ("allgemeinen Merkmalen", beim("av1", "allgemeinen")),
    ("Benutzung", beim("av3", "Benutzung")), ("Allgemeinheit", beim("av3", "Allgemeinheit"))], size=34)
folie([("wl352", f"{VA} › 5. Einzelfall › Allgemeinverfügung, § 35 Satz 2")], rechts_frei([
    titel(glyphen("Allgemeinverfügung"), 110, 75, "wl352", 50),
    *w352,
    z("a) Personenkreis: die 2. Durchsage,", 110, w352_y + 30, "av1b", "Bold", 32),
    z("ein Anlass, ein Ort, alle, die gerade dort sind", 150, w352_y + 80, beim("av1b", "Anlass"), size=32),
    z("b) Sache: etwa die Widmung einer Straße", 110, w352_y + 150, beim("av2", "Widmung"), "Bold", 32),
    z("c) Benutzung: Verbot auf einem Gelände für jeden", 110, w352_y + 220, beim("av3", "Verbot"), "Bold", 32),
    zit("BVerwG, 6 C 26.19, Rn. 26–28, 32 f.; BVerwG, Urt. v. 25.10.2018 – 7 C 22.16, Rn. 18", 110, w352_y + 280,
        beim("av3", "gilt")),
    ficon("ph", "megaphone", IX, IU, 120, "av1b", fuell=ORANGE, bis="av2"),
    ficon("tabler", "road", IX, IU, 130, "av2", fuell=WEISS, bis="av3"),
    ficon("tabler", "barrier-block", IX, IU, 140, beim("av3", "Verbot"), fuell=ROT),
    *fig("GO", FX, FB, FR, [("wl352", "ruhig"), ("av1b", "denkt"), ("av2", "ruhig")]),
    schild("Polizist Göbel", FX, "wl352", GO_F),
]))

# M Verkehrszeichen ------------------------------------------------------------------------------------------------------------
folie([("vz", f"{VA} › 5. Einzelfall › Verkehrszeichen")], rechts_frei([
    *tafel("vz", "Und Verkehrszeichen?"),
    z("Verkehrsverbote und Verkehrsgebote:", 110, 190, beim("vz", "Verkehrsverbote"), "Bold", 36),
    z("Allgemeinverfügungen", 150, 250, beim("vz", "Allgemeinverfügungen"), "ExtraBold", 38),
    z("ständige Rechtsprechung des BVerwG", 150, 310, beim("vz", "ständiger"), size=34),
    zit("BVerwG, Urt. v. 23.9.2010 – 3 C 37.09, Rn. 15 (stRspr)", 150, 365, beim("vz", "Allgemeinverfügungen")),
    ok(150, 470, beim("halt", "Haltverbot"), gr=22),
    z("auch das Haltverbot vor der Ladezone", 195, 447, beim("halt", "Haltverbot"), "Bold", 36),
    *haltverbot(1330, 330, 70, "vz", boden=560),
    *fig("WI", 1640, FB, FR, [("vz", "denkt"), ("halt", "sorge")]),
    schild("Frau Wiegand", 1640, "vz", WI_F),
]))

# N 6. Außenwirkung: im Rathaus -------------------------------------------------------------------------------------------------
KEX, LRX = 1390, 1720
KEb = ("KE_redet_r", KEX, FB, FR)
RAT = beim("rathaus", "Rathaus")
folie([("m6", f"{VA} › 6. unmittelbare Außenwirkung"), ("umsetz", f"{VA} › 6. Außenwirkung › innerdienstliche Weisung"),
       ("aussen", f"{VA} › 6. Außenwirkung › Bescheid an Frau Wiegand")], rechts_frei([
    *tafel("m6", "6. unmittelbare Außenwirkung"),
    z("trifft jemanden außerhalb der Verwaltung", 110, 190, beim("m6", "jemanden"), "Bold", 36),
    z("Umsetzung ins Bürgerbüro:", 110, 290, "umsetz", "Bold", 34),
    z("innerdienstliche Weisung", 150, 345, beim("umsetz", "innerdienstliche"), size=34),
    z("berührt seine Rechtsstellung grundsätzlich nicht", 150, 400, beim("umsetz", "berührt"), size=34),
    nein(150, 478, beim("umsetz", "kein"), gr=18),
    z("kein Verwaltungsakt", 195, 455, beim("umsetz", "kein"), "Bold", 34),
    zit("BVerwG, 2 A 6.13, Rn. 18; BVerwG, 2 B 23.12, Rn. 10 (Umsetzung)", 150, 510,
        beim("umsetz", "Verwaltungsakt")),
    nein(150, 598, beim("org", "Organisationsakt"), gr=18),
    z("Organisationsakt: zwei Ämter zusammenlegen", 195, 575, beim("org", "Organisationsakt"), size=34),
    ok(150, 693, beim("aussen", "nach"), gr=20),
    z("Bescheid an Frau Wiegand: wirkt nach außen", 195, 670, beim("aussen", "nach"), "Bold", 34),
    pl("Im Rathaus", 1560, 140, RAT, fill=GELB, size=30, anker="m"),
    *fig("KE", KEX, FB, FR, [(beim("rathaus", "Amtsleiterin"), "ruhig_r")], bis="ke1"),
    *redet("KE_redet_r", KEX, FB, FR, "ke1", "umsetz"),
    peep_voll("KE_ruhig_r", KEX, FB, FR, "umsetz", anim="cut"),
    schild("Frau Kessler, Amtsleiterin", KEX, beim("rathaus", "Amtsleiterin"), KE_F, size=24),
    *fig("LO", LRX, FB, FR, [("m6", "ruhig"), ("umsetz", "denkt")]),
    schild("Herr Lorenz", LRX, "m6", LO_F, size=24),
    blase("sprech", 560, 170, "ke1", 1560, 330, inhalt=["Herr Lorenz, ab Montag", "arbeiten Sie im Bürgerbüro."],
          textsize=28, figur=KEb, bis="umsetz"),
    ficon("tabler", "file-text", 1560, 380, 100, "aussen", fuell=WEISS),
]))

# O Ergebnis ---------------------------------------------------------------------------------------------------------------------
reihe_o, _ = reihe("erg", ("erg", "erg", "erg", "erg"), anim="cut")
folie([("erg", "Ergebnis")], [
    *reihe_o,
    pl("Ergebnis", 960, 70, "erg", fill=PINK, size=42, anker="m"),
    ok(RX[0], 690, beim("erg", "Verwaltungsakt"), gr=30),
    pl("Verwaltungsakt", RX[0], 760, beim("erg", "Verwaltungsakt"), fill=GRUEN, size=28, anker="m"),
    ok(RX[2], 690, beim("erg2", "Allgemeinverfügungen"), gr=30),
    pl("Allgemeinverfügung", RX[2], 760, beim("erg2", "Allgemeinverfügungen"), fill=GRUEN, size=28, anker="m"),
    ok(RX[3], 690, beim("erg2", "Allgemeinverfügungen"), gr=30),
    pl("Allgemeinverfügung", RX[3], 760, beim("erg2", "Allgemeinverfügungen"), fill=GRUEN, size=28, anker="m"),
    z("also auch Verwaltungsakte", 1225 - 225, 830, beim("erg2", "also"), "Bold", 32, rechts=1820),
    nein(RX[1], 690, beim("erg3", "Warnung"), gr=30),
    pl("kein Verwaltungsakt", RX[1], 760, beim("erg3", "Warnung"), fill=ROT, size=28, anker="m"),
    *fig("WI", 1740, BODEN, FH - 60, [("erg", "ruhig"), ("erg3", "froh")]),
    schild("Frau Wiegand", 1740, "erg", WI_F, unten=BODEN),
])

# P Bedeutung: Klageart ------------------------------------------------------------------------------------------------------------
folie([("warum", "Bedeutung › Klageart, § 42 I VwGO")], rechts_frei([
    *tafel("warum", "Warum das zählt"),
    z("gegen belastenden Verwaltungsakt, etwa das Haltverbot:", 110, 190, beim("anf", "Gegen"), size=34),
    z("Anfechtungsklage", 150, 245, beim("anf", "Anfechtungsklage"), "ExtraBold", 38),
    z("auf den abgelehnten Verwaltungsakt, den Standplatz:", 110, 335, beim("verpfl", "abgelehnten"), size=34),
    z("Verpflichtungsklage", 150, 390, beim("verpfl", "Verpflichtungsklage"), "ExtraBold", 38),
    zit("§ 42 Abs. 1 VwGO", 150, 445, beim("verpfl", "Paragraf")),
    nein(150, 553, beim("unst", "unstatthaft"), gr=20),
    z("bloße Warnung: Anfechtungsklage unstatthaft", 195, 530, beim("unst", "unstatthaft"), size=34),
    zit("BVerwG, 7 C 4.25, Rn. 9", 195, 585, beim("unst", "unstatthaft")),
    *haltverbot(IX, IU - 70, 60, beim("anf", "Haltverbot"), mast=False, bis="verpfl"),
    ficon("tabler", "caravan", IX, IU, 190, "verpfl", fuell=GELB),
    *fig("WI", FX, FB, FR, [("warum", "ruhig"), ("anf", "entschl")]),
    schild("Frau Wiegand", FX, "warum", WI_F),
]))

# Q Frist und Vollstreckung ---------------------------------------------------------------------------------------------------------
folie([("frist", "Bedeutung › Frist"), ("vollstr", "Bedeutung › Vollstreckung")], rechts_frei([
    *tafel("frist", "Frist und Vollstreckung"),
    z("Fristen: meist ein Monat", 110, 190, beim("frist", "Fristen"), "Bold", 36),
    zit("§ 74 Abs. 1, 2 VwGO", 150, 245, beim("frist", "Monat")),
    z("Schild ohne Belehrung: ein Jahr,", 110, 320, beim("frist", "Schild"), "Bold", 36),
    z("ab der ersten Begegnung mit dem Schild", 150, 375, beim("frist", "Moment"), size=34),
    zit("§ 58 Abs. 2 VwGO; BVerwG, 3 C 37.09, Rn. 14, 16", 150, 430, beim("frist", "gegenübersteht")),
    z("Gebot: Behörde setzt es selbst durch,", 110, 520, beim("vollstr", "gebietet"), "Bold", 36),
    z("mit Verwaltungszwang, ohne erst zu klagen", 150, 575, beim("vollstr", "Verwaltungszwang"), size=34),
    zit("§ 6 Abs. 1 VwVG (unanfechtbar oder sofort vollziehbar); BVerwG, 3 B 40.21, Rn. 11", 150, 630,
        beim("vollstr", "klagen")),
    ficon("tabler", "calendar", IX, IU, 130, "frist", fuell=WEISS, bis="vollstr"),
    pl("1 Monat", IX, 190, beim("frist", "Monat"), fill=GELB, size=30, anker="m", bis=beim("frist", "Jahr")),
    pl("Schild: 1 Jahr", IX, 190, beim("frist", "Jahr"), fill=GELB, size=30, anker="m", bis="vollstr"),
    ficon("tabler", "file-text", IX, IU, 110, "vollstr", fuell=WEISS),
    pl("Verwaltungszwang", IX, 190, beim("vollstr", "Verwaltungszwang"), fill=ROT, size=30, anker="m"),
    *fig("WI", FX, FB, FR, [("frist", "denkt")]),
    schild("Frau Wiegand", FX, "frist", WI_F),
]))

# R Klausurtipp (Lexi) ---------------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · Verwaltungsakt prüfen")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Verwaltungsakt: meist bei der", 200, 200, beim("tipp", "Verwaltungsakt"), "Bold", 36),
    z("statthaften Klageart prüfen", 200, 255, beim("tipp", "statthaften"), "Bold", 36),
    z("Unproblematisches kurz feststellen", 200, 350, "tipp1", size=34),
    z("argumentieren, wo es hakt:", 200, 405, beim("tipp1", "Argumentiere"), size=34),
    z("meist Regelung oder Außenwirkung", 200, 460, beim("tipp1", "Regelung"), "Bold", 34),
    z("Schreiben lesen wie ein objektiver Empfänger", 200, 555, beim("tipp2", "lies"), size=34),
    z("Unklarheiten gehen zulasten der Behörde", 200, 610, beim("tipp2", "Unklarheiten"), "Bold", 34),
    zit("BVerwG, 7 C 4.25, Rn. 10", 200, 665, beim("tipp2", "Behörde")),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    pl("Lexi", FX, FB + 22, "tipp", fill=GELB, size=30, anker="m", d=0.2),
])

# S Klausurschema ----------------------------------------------------------------------------------------------------------------------
SZ = 36
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel(glyphen("Klausurschema: Verwaltungsakt"), 110, 90, "sch", 48),
    z("Verwaltungsakt, § 35 Satz 1 VwVfG", K1, 185, "q0", "Bold", 40, rechts=1820),
    z("1. hoheitliche Maßnahme", K2, 260, "q1", size=SZ, rechts=1820),
    z("2. Behörde, § 1 IV VwVfG", K2, 320, "q2", size=SZ, rechts=1820),
    z("3. auf dem Gebiet des öffentlichen Rechts", K2, 380, "q3", size=SZ, rechts=1820),
    z("4. Regelung", K2, 440, "q4", size=SZ, rechts=1820),
    z("5. Einzelfall", K2, 500, "q5", size=SZ, rechts=1820),
    z("auch Allgemeinverfügung, § 35 Satz 2 VwVfG", K3, 555, beim("q5", "Allgemeinverfügung"), "Bold", 34, rechts=1820),
    z("6. unmittelbare Außenwirkung", K2, 620, "q6", size=SZ, rechts=1820),
    z("Folge: Anfechtungs- oder Verpflichtungsklage, § 42 I VwGO", K1, 720, "q7", "Bold", 38, rechts=1820),
])

# T Merksatz (Lexi) ---------------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Ein Verwaltungsakt regelt", 0)], [("verbindlich einen Einzelfall", "a")],
                 [("mit Wirkung nach außen.", "b")]],
                750, 310, 48, "merke", {"a": beim("merke", "verbindlich"), "b": beim("merke", "Wirkung")}),
    *markertext([[("Wer nur warnt, informiert oder", 0)], [("intern anweist, erlässt ", 0), ("keinen.", "c")]],
                750, 600, 46, "m2", {"c": beim("m2", "keinen")}),
    *redet("LX_erklaert", 1680, 950, 700, "merke", lexi_bis_ende("merke")),
    pl("Lexi", 1680, 968, "merke", fill=GELB, size=30, anker="m", d=0.2),
])
