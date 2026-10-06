"""Folge 209 · Schadensersatz statt der Leistung §§ 280, 281 BGB – Schema – Serienstandard Open Peeps (Katzenkönig).
Fiktiver Fall: Jörn kauft im Reifenhandel von Ingolf vier Felgen für 1.200 € und zahlt sofort; Lieferung bis 8.9. zugesagt,
nichts kommt; am 10.9. E-Mail „Bitte liefern Sie die Felgen umgehend.“; Ingolf vertröstet; drei Wochen später kauft Jörn
gleichwertige Felgen bei Herta für 1.450 € und verlangt von Ingolf die 250 € Mehrkosten (und sein Geld zurück).
Szenen laut ../SZENENPLAN.md. Zwei Handlungsgeräusche (E-Mail tippen, Kasse bei Herta; ../geraeusche_herkunft.json).
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/pkt
als eigene Kopie aus Folge 206 (gemeinsame Dateien unverändert); neu: laden(), regal(), haus().
Wortlautkarten wörtlich nach gesetze-im-internet.de (Abruf 06.10.2026): § 280 Abs. 1 und 3, § 281 Abs. 1 Satz 1, § 281 Abs. 2,
§ 281 Abs. 4 BGB. Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_209/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_209/" in n:
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
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 06.10.2026), als Zitat mit Normangabe;
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
NAME = {"JO": "Jörn", "IN": "Ingolf", "HE": "Herta"}
NFARBE = {"JO": BLAU, "IN": GRUEN, "HE": GELB}


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
WAND2 = (226, 240, 228, 255)
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
G0 = 900                                     # Boden der Fallszenen
FHA = 430                                    # Figurenhöhe in den Fallszenen


def boden_(y, c, fill=None, x0=30, x1=1890, h=None):
    """Boden in Seitenansicht: Tuschelinie, optional Fläche darunter."""
    hh = h or 60
    im = Image.new("RGBA", (x1 - x0, hh))
    dr = ImageDraw.Draw(im)
    if fill:
        dr.rectangle((0, 0, x1 - x0, hh), fill=fill)
    dr.line((0, 2, x1 - x0, 2), fill=INK, width=6)
    return El(im, x0, y, c, "cut", 0.0, None, name="boden")


def laden(c, wand=WAND, x=70, w=900, h=560):
    """Reifenhandel von innen: Rückwand mit Wandregal (zwei Bretter), Grundformen."""
    els = [hart(boden_(G0, c, fill=(226, 226, 222, 255), h=100))]
    im = Image.new("RGBA", (w, h))
    dr = ImageDraw.Draw(im)
    dr.rounded_rectangle((0, 0, w - 1, h - 1), 14, fill=wand, outline=INK, width=5)
    for yy in (250, 470):                                    # Regalbretter
        dr.rectangle((60, yy, w - 60, yy + 18), fill=(190, 135, 90, 255), outline=INK, width=4)
    for xx in (60, w - 78):                                  # Seitenwangen
        dr.rectangle((xx, 60, xx + 18, 488), fill=(190, 135, 90, 255), outline=INK, width=4)
    els.append(hart(El(im, x, G0 - h, c, "cut", 0.0, None, name="laden")))
    return els


def felgen(c, n=4, fuell=HELLGRAU, x0=230, bis=None, anim="cut", reihe=0):
    """Felgen (Tabler wheel) auf dem Regalbrett (reihe 0 oben, 1 unten)."""
    unten = G0 - 560 + (250 if reihe == 0 else 470) + 4
    return [hart(ficon("tabler", "wheel", x0 + i * 165, unten, 150, c, fuell=fuell, anim=anim, bis=bis)) if anim == "cut"
            else ficon("tabler", "wheel", x0 + i * 165, unten, 150, c, fuell=fuell, anim=anim, bis=bis) for i in range(n)]


def tisch(cx, c, breite=300, hoehe=210):
    """Einfacher Tisch (Platte und zwei Beine) als Grundform."""
    im = Image.new("RGBA", (breite, hoehe))
    dr = ImageDraw.Draw(im)
    dr.rectangle((0, 0, breite - 1, 22), fill=HOLZ, outline=INK, width=4)
    for xx in (24, breite - 46):
        dr.rectangle((xx, 22, xx + 20, hoehe - 1), fill=HOLZ, outline=INK, width=4)
    return hart(El(im, cx - breite // 2, G0 - hoehe, c, "cut", 0.0, None, name="tisch"))


def carport(c, x=70, w=1000, h=560):
    """Carport bei Jörn: Dach mit zwei Pfosten (Grundformen)."""
    els = [hart(boden_(G0, c, fill=(220, 220, 214, 255), h=100))]
    im = Image.new("RGBA", (w, h))
    dr = ImageDraw.Draw(im)
    dr.polygon([(0, 60), (w - 1, 0), (w - 1, 40), (0, 100)], fill=(190, 135, 90, 255), outline=INK)
    dr.line([(0, 60), (w - 1, 0), (w - 1, 40), (0, 100), (0, 60)], fill=INK, width=5)
    for xx in (20, w - 50):
        dr.rectangle((xx, 70 if xx < 100 else 30, xx + 28, h - 1), fill=(214, 160, 110, 255), outline=INK, width=4)
    els.append(hart(El(im, x, G0 - h, c, "cut", 0.0, None, name="carport")))
    return els


# ===========================================================================================================================
# A1 Fall: der Kauf im Reifenhandel von Ingolf
# ===========================================================================================================================
IX, JX = 1180, 1650
folie([(NULL, "Fall · Die Felgen"), ("laden", "Fall · Der Kauf im Reifenhandel"), ("zahlt", "Fall · Jörn zahlt sofort"),
       ("in1", "Fall · Lieferung bis 8. September")], [
    *laden(NULL),
    *felgen(NULL),
    pl("Händler liefert bezahlte Felgen nicht", 70, 30, beim("fall", "liefert"), fill=GELB, size=32),
    pl("Du kaufst woanders teurer ein", 70, 100, beim("fall", "teurer"), fill=HELLROT, size=32),
    *fig("JO", JX, G0, FHA, [(beim("joern", "Jörn"), "froh")], bis="in1"),
    *fig("JO", JX, G0, FHA, [("in1", "ruhig")], erst="cut"),
    ns("Jörn", JX, G0, beim("joern", "Jörn"), BLAU, d=0.1),
    *fig("IN", IX, G0, FHA, [(beim("laden", "Ingolf"), "froh_r")], bis="in1"),
    *redet("IN_redet_r", IX, G0, FHA, "in1", "warten"),
    ns("Ingolf", IX, G0, beim("laden", "Ingolf"), GRUEN, d=0.1),
    pl("1. September", 520, 360, beim("laden", "ersten"), fill=WEISS, size=28, anker="m"),
    pl("Reifenhandel von Ingolf", 1180, 140, beim("laden", "Reifenhandel"), fill=WEISS, size=28, anker="m", bis="in1"),
    pl("4 Felgen: 1.200 €", 520, 560, beim("laden", "tausend"), fill=GELB, size=30, anker="m"),
    ficon("tabler", "cash-banknote", 1420, 640, 120, "zahlt", fuell=GRUEN),
    pl("sofort bezahlt", 1420, 670, beim("zahlt", "sofort"), fill=GRUEN, size=28, anker="m"),
    blase("sprech", 780, 200, "in1", 1240, 230, inhalt=["Die Felgen liefere ich Ihnen", "bis zum 8. September."],
          textsize=34, figur=("IN_redet_r", IX, G0, FHA), bis="warten"),
])

# ===========================================================================================================================
# A2 Fall: Warten am Carport, E-Mail „umgehend“
# ===========================================================================================================================
JX2 = 1560
folie([("warten", "Fall · Das Warten"), ("mail", "Fall · Die E-Mail"), ("jo1", "Fall · Jörn: „umgehend“")], [
    *carport("warten"),
    hart(ficon("tabler", "car", 560, G0 + 4, 560, "warten", fuell=BLAU, anim="cut")),
    tisch(1220, "warten"),
    hart(ficon("tabler", "device-laptop", 1220, G0 - 206, 150, "warten", fuell=WEISS, anim="cut")),
    pl("8. September", 70, 30, beim("warten", "achte"), fill=GELB, size=32),
    ficon("tabler", "package-off", 1220, 420, 110, beim("warten", "nichts"), fuell=WEISS, bis="mail"),
    pl("nichts kommt", 1220, 450, beim("warten", "nichts"), fill=HELLROT, size=28, anker="m", bis="mail"),
    pl("10. September", 70, 100, beim("mail", "zehnten"), fill=GELB, size=32),
    szene(ficon("tabler", "mail", 1220, 560, 100, beim("mail", "E-Mail"), fuell=WEISS), "209tippen*", 0.45),
    pl("E-Mail an Ingolf", 1220, 450, beim("mail", "E-Mail"), fill=WEISS, size=28, anker="m"),
    *fig("JO", JX2, G0, FHA, [("warten", "ruhig"), (beim("warten", "nichts"), "denkt"), ("mail", "ernst")], bis="jo1", erst="cut"),
    *redet("JO_redet", JX2, G0, FHA, "jo1", "antw"),
    ns("Jörn", JX2, G0, "warten", BLAU),
    blase("sprech", 700, 200, "jo1", 1380, 230, inhalt=["Bitte liefern Sie die", "Felgen umgehend."],
          textsize=34, figur=("JO_redet", JX2, G0, FHA), bis="antw"),
])

# ===========================================================================================================================
# A3 Fall: Ingolf antwortet aus seinem Laden
# ===========================================================================================================================
IX3 = 1450
folie([("antw", "Fall · Ingolf antwortet")], [
    *laden("antw"),
    tisch(1120, "antw"),
    hart(ficon("tabler", "device-laptop", 1120, G0 - 206, 150, "antw", fuell=WEISS, anim="cut")),
    ficon("tabler", "mail", 1120, 560, 100, "antw", fuell=WEISS),
    pl("Antwort an Jörn", 1120, 450, beim("antw", "antwortet"), fill=WEISS, size=28, anker="m"),
    *fig("IN", IX3, G0, FHA, [("antw", "denkt")], bis="in2", erst="cut"),
    *redet("IN_redet", IX3, G0, FHA, "in2", "drei"),
    ns("Ingolf", IX3, G0, "antw", GRUEN),
    blase("sprech", 660, 200, "in2", 1500, 230, inhalt=["Die Felgen kommen", "bald, versprochen."],
          textsize=34, figur=("IN_redet", IX3, G0, FHA), bis="drei"),
])

# ===========================================================================================================================
# A4 Fall: drei Wochen später, Deckungskauf bei Herta
# ===========================================================================================================================
HX, JX4 = 1180, 1660
folie([("drei", "Fall · Drei Wochen später"), ("herta", "Fall · Bei Herta"), ("kauft", "Fall · Jörn kauft bei Herta")], [
    *laden("drei", wand=WAND2),
    *felgen("drei", fuell=BLAU),
    *felgen("drei", fuell=BLAU, reihe=1),
    pl("3 Wochen später: immer noch nichts da", 70, 30, beim("drei", "Drei"), fill=HELLROT, size=32),
    pl("1. Oktober", 70, 100, beim("herta", "ersten"), fill=GELB, size=32),
    *fig("JO", JX4, G0, FHA, [("drei", "muede"), ("herta", "ruhig"), ("kauft", "freut")], erst="cut"),
    ns("Jörn", JX4, G0, "drei", BLAU),
    *fig("HE", HX, G0, FHA, [(beim("herta", "Herta"), "froh")], bis="he1"),
    *redet("HE_redet", HX, G0, FHA, "he1", "kauft"),
    *fig("HE", HX, G0, FHA, [("kauft", "froh")], erst="cut"),
    ns("Herta", HX, G0, beim("herta", "Herta"), GELB, d=0.1),
    pl("gleichwertige Felgen?", 1660, 380, beim("herta", "gleichwertigen"), fill=WEISS, size=28, anker="m", bis="he1"),
    blase("sprech", 700, 200, "he1", 1260, 230, inhalt=["Die habe ich da,", "für 1.450 €."],
          textsize=34, figur=("HE_redet", HX, G0, FHA), bis="kauft"),
    szene(ficon("tabler", "cash-register", 1420, 660, 130, beim("kauft", "kauft"), fuell=WEISS), "209kasse*", 0.40),
    pl("1.450 € bezahlt", 1420, 350, beim("kauft", "kauft"), fill=GRUEN, size=30, anker="m"),
    ficon("tabler", "mail", 1660, 330, 80, beim("kauft", "schreibt"), fuell=WEISS),
])

# ===========================================================================================================================
# A5 Fall: Jörn schreibt Ingolf, Ingolf protestiert, die Frage
# ===========================================================================================================================
JX5, IX5 = 560, 1500


def trenner(c):
    im = Image.new("RGBA", (8, 560)); ImageDraw.Draw(im).rectangle((0, 0, 7, 559), fill=INK)
    return hart(El(im, 956, G0 - 560, c, "cut", 0.0, None, name="trenner"))


folie([("jo2", "Fall · Jörn: Geld zurück und Mehrkosten"), ("in3", "Fall · Ingolf will noch liefern"),
       ("frage", "Fall · Die Frage")], [
    hart(boden_(G0, "jo2", fill=(226, 226, 222, 255), h=100)),
    trenner("jo2"),
    hart(ficon("tabler", "car", 250, G0 + 4, 380, "jo2", fuell=BLAU, anim="cut")),
    *redet("JO_fordert_r", JX5, G0, FHA, "jo2", "in3"),
    *fig("JO", JX5, G0, FHA, [("in3", "ernst_r")], erst="cut"),
    ns("Jörn", JX5, G0, "jo2", BLAU),
    hart(ficon("tabler", "building-store", 1760, G0 + 4, 200, "jo2", fuell=WAND, anim="cut")),
    *fig("IN", IX5, G0, FHA, [("jo2", "schreck")], bis="in3", erst="cut"),
    *redet("IN_klagt", IX5, G0, FHA, "in3", "frage"),
    *fig("IN", IX5, G0, FHA, [("frage", "sorge")], erst="cut"),
    ns("Ingolf", IX5, G0, "jo2", GRUEN),
    blase("sprech", 900, 260, "jo2", 560, 200, inhalt=["Ihre Felgen will ich nicht mehr.", "Ich will mein Geld zurück, und die",
                                                        "250 € Mehrkosten zahlen Sie auch!"],
          textsize=34, figur=("JO_fordert_r", JX5, G0, FHA), bis="in3"),
    blase("sprech", 720, 200, "in3", 1360, 220, inhalt=["Aber die Felgen kommen", "doch nächste Woche!"],
          textsize=34, figur=("IN_klagt", IX5, G0, FHA), bis="frage"),
    pl("Kann Jörn die Mehrkosten verlangen?", 70, 30, "frage", fill=PINK, size=34),
    pl("War „umgehend“ überhaupt eine Frist?", 70, 105, "frage2", fill=WEISS, size=32),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_209(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=35, zeilenabstand=1.3)
        els += e; y += 14
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_209("sv", [
    "Jörn kauft am 1. September 2026 für sich privat im Reifenhandel von Ingolf vier Felgen für 1.200 € und zahlt sofort. "
    "Ingolf sagt die Lieferung bis zum 8. September zu.",
    "Bis dahin kommt nichts. Am 10. September schreibt Jörn per E-Mail: „Bitte liefern Sie die Felgen umgehend.“ Ingolf "
    "antwortet: „Die Felgen kommen bald, versprochen.“ Einen Grund für die Verzögerung nennt er nicht.",
    "Drei Wochen später ist immer noch nichts geliefert. Am 1. Oktober kauft Jörn gleichwertige Felgen bei Herta für "
    "1.450 €. Dann schreibt er Ingolf: „Ihre Felgen will ich nicht mehr. Ich will mein Geld zurück, und die 250 € "
    "Mehrkosten zahlen Sie auch!“",
], "Kann Jörn die 250 € Mehrkosten verlangen?")

_zl = lambda W, wort: next(i for i, t in enumerate(W) if wort in t)

# ===========================================================================================================================
# C Anspruchsgrundlage
# ===========================================================================================================================
PC = "A. Anspruchsgrundlage"
folie([("agl", f"{PC} › Schadensersatz statt der Leistung"), ("agl2", f"{PC} › §§ 280 Abs. 1, 3, 281 BGB"),
       ("sys", f"{PC} › System der §§ 280 ff. BGB")], rechts_frei([
    *tafel("agl", "Die Anspruchsgrundlage"),
    z("Jörn verlangt die Mehrkosten als", 110, 190, "agl", "Regular", 34),
    z("Schadensersatz statt der Leistung", 110, 240, beim("agl", "Schadensersatz"), "ExtraBold", 36),
    blk(110, 330, 1040, 110, GELB, "agl2", [("§§ 280 Abs. 1, 3, 281 BGB", "ExtraBold", 40, INK)]),
    zit("Das System dahinter: Video „Schadensersatz-Schema, §§ 280 ff. BGB“", 110, 480, "sys"),
    *requisit([("agl", ("tabler", "coin-euro", 110, GELB), "Mehrkosten", WEISS),
               ("agl2", ("tabler", "scale", 120, WEISS), "Anspruchsgrundlage", GELB)]),
    *zwei("JO", [("agl", "ernst"), ("sys", "ruhig")], "IN", [("agl", "sorge"), ("agl2", "denkt")]),
]))

# ===========================================================================================================================
# D § 280 Abs. 1 und 3 BGB (Wortlautkarten)
# ===========================================================================================================================
W2801 = umbruch("„Verletzt der Schuldner eine Pflicht aus dem Schuldverhältnis, so kann der Gläubiger Ersatz des hierdurch "
                "entstehenden Schadens verlangen. Dies gilt nicht, wenn der Schuldner die Pflichtverletzung nicht zu "
                "vertreten hat.“", 31, 1040)
w2801, w2801_y = wortlaut(80, 180, 1100, W2801, "§ 280 Abs. 1 BGB", "w280",
                          marken=[(_zl(W2801, "Pflicht aus"), "Pflicht", beim("w280", "Pflicht")),
                                  (_zl(W2801, "Schadens"), "Schadens", beim("w280", "Schadens")),
                                  (_zl(W2801, "vertreten"), "vertreten", beim("w280", "vertreten"))], size=31)
W2803 = umbruch("„Schadensersatz statt der Leistung kann der Gläubiger nur unter den zusätzlichen Voraussetzungen des "
                "§ 281, des § 282 oder des § 283 verlangen.“", 31, 1040)
w2803, w2803_y = wortlaut(80, w2801_y + 30, 1100, W2803, "§ 280 Abs. 3 BGB", "w3",
                          marken=[(_zl(W2803, "zusätzlichen"), "zusätzlichen Voraussetzungen", beim("w3", "zusätzlichen")),
                                  (_zl(W2803, "§ 281"), "§ 281", beim("w3", "Paragrafen"))], size=31)
PD = "A. Anspruchsgrundlage › § 280 BGB"
folie([("w280", f"{PD} Abs. 1"), ("w3", f"{PD} Abs. 3: zusätzlich § 281 BGB")], rechts_frei([
    *tafel("w280", "Der Ausgangspunkt: § 280 BGB"),
    *w2801, *w2803,
    *requisit([("w280", ("tabler", "scale", 120, WEISS), "Pflichtverletzung", WEISS),
               ("w3", ("tabler", "hourglass", 100, HELLBLAU), "plus § 281 BGB", GELB)]),
    *zwei("JO", [("w280", "ruhig"), ("w3", "denkt")], "IN", [("w280", "ruhig"), (beim("w280", "Dies"), "denkt")]),
]))
assert w2803_y <= 930, w2803_y

# ===========================================================================================================================
# E § 281 Abs. 1 Satz 1 BGB (Wortlautkarte)
# ===========================================================================================================================
W2811 = umbruch("„Soweit der Schuldner die fällige Leistung nicht oder nicht wie geschuldet erbringt, kann der Gläubiger unter "
                "den Voraussetzungen des § 280 Abs. 1 Schadensersatz statt der Leistung verlangen, wenn er dem Schuldner "
                "erfolglos eine angemessene Frist zur Leistung oder Nacherfüllung bestimmt hat.“", 31, 1040)
w2811, w2811_y = wortlaut(80, 180, 1100, W2811, "§ 281 Abs. 1 Satz 1 BGB", "w281",
                          marken=[(_zl(W2811, "fällige Leistung"), "fällige Leistung nicht", beim("w281a", "fällige")),
                                  (_zl(W2811, "erfolglos"), "erfolglos", beim("w281b", "erfolglos")),
                                  (_zl(W2811, "angemessene"), "angemessene Frist", beim("w281b", "angemessene"))], size=31)
PE = "A. Anspruchsgrundlage › § 281 Abs. 1 Satz 1 BGB"
folie([("w281", PE), ("w281a", f"{PE} › Leistung nicht erbracht"), ("w281b", f"{PE} › erfolglose Frist"),
       ("plan", "Das Schema in 6 Schritten")], rechts_frei([
    *tafel("w281", "Die Zusatzvoraussetzungen"),
    *w2811,
    *pkt("fällige Leistung nicht erbracht", w2811_y + 40, "w281a", "Bold", 32, x=160),
    *pkt("erfolglos eine angemessene Frist bestimmt", w2811_y + 100, "w281b", "Bold", 32, x=160),
    blk(110, w2811_y + 175, 1040, 90, GELB, "plan", [("Das Schema in 6 Schritten", "ExtraBold", 34, INK)]),
    *requisit([("w281", ("tabler", "hourglass", 100, HELLBLAU), "§ 281 BGB", WEISS),
               ("w281a", ("tabler", "package-off", 110, WEISS), "nicht geliefert", HELLROT),
               ("w281b", ("tabler", "mail", 100, WEISS), "Frist", GELB),
               ("plan", ("tabler", "list-numbers", 100, WEISS), "6 Schritte", GELB)]),
    *zwei("JO", [("w281", "ruhig"), ("w281b", "denkt")], "IN", [("w281", "ruhig"), ("w281a", "sorge")]),
]))
assert w2811_y + 270 <= 930, w2811_y

# ===========================================================================================================================
# F 1. Schuldverhältnis
# ===========================================================================================================================
folie([("s1", "B. Schema › 1. Schuldverhältnis"), ("s1b", "B. Schema › 1. Schuldverhältnis › Kaufvertrag, § 433 BGB")], rechts_frei([
    *tafel("s1", "1. Schuldverhältnis"),
    *okz("Kaufvertrag zwischen Jörn und Ingolf", 200, "s1b", "Bold", 34, x=160),
    zit("§ 433 BGB", 160, 255, beim("s1b", "Paragraf")),
    *pkt("Ingolf schuldet 4 Felgen, Jörn den Kaufpreis: 1.200 €", 330, beim("s1b", "Kaufvertrag"), "Regular", 32, x=160),
    *requisit([("s1", ("tabler", "file-text", 110, WEISS), "Schuldverhältnis", WEISS),
               ("s1b", ("tabler", "arrows-exchange", 110, None), "Felgen gegen 1.200 €", GELB)]),
    *zwei("JO", [("s1", "ruhig")], "IN", [("s1", "ruhig"), ("s1b", "froh")]),
]))

# ===========================================================================================================================
# G 2. Pflichtverletzung: fällige, durchsetzbare Leistung nicht erbracht
# ===========================================================================================================================
PG = "B. Schema › 2. Pflichtverletzung"
folie([("p1", PG), ("p2", f"{PG} › fällig"), ("p3", f"{PG} › durchsetzbar")], rechts_frei([
    *tafel("p1", "2. Pflichtverletzung"),
    z("fällige, durchsetzbare Leistung nicht erbracht", 110, 190, beim("p1", "Ingolf"), "ExtraBold", 34),
    *okz("fällig: Lieferung bis 8.9.2026 vereinbart", 280, "p2", "Bold", 32, x=160),
    z("spätestens dann fällig, und sie bleibt aus", 160, 325, beim("p2", "Spätestens"), "Regular", 32),
    zit("§ 271 Abs. 2 BGB", 160, 375, beim("p2", "Spätestens")),
    *okz("durchsetzbar: Jörn hat bezahlt, keine Einrede", 450, "p3", "Bold", 32, x=160),
    zit("§ 320 Abs. 1 BGB; Formulierung wie Video „Rücktritt, § 323 BGB“", 160, 500, beim("p3", "Jörn")),
    *requisit([("p1", ("tabler", "package-off", 110, WEISS), "nicht geliefert", HELLROT),
               ("p2", ("tabler", "calendar-event", 100, WEISS), "bis 8.9.2026", GELB),
               ("p3", ("tabler", "cash-banknote", 120, GRUEN), "bezahlt", GRUEN)]),
    *zwei("JO", [("p1", "ernst"), ("p3", "ruhig")], "IN", [("p1", "sorge"), ("p2", "still")]),
]))

# ===========================================================================================================================
# H 3. Frist: „umgehend“ genügt, drei Wochen, erfolglos (Zeitstrahl)
# ===========================================================================================================================
PH = "B. Schema › 3. Frist"


def zeitstrahl(y, c):
    """Zeitstrahl September/Oktober 2026 mit 10.9. (E-Mail) und 1.10. (Deckungskauf)."""
    x0, x1 = 160, 1100
    els = [linienzug([(x0, y), (x1, y)], c, breite=5)]
    tx = lambda tag: x0 + (tag - 1) * (x1 - x0) / 31        # 1.9. … 2.10.
    for tag, txt in ((10, "10.9."), (31, "1.10.")):
        els.append(linienzug([(tx(tag), y - 16), (tx(tag), y + 16)], c, breite=5))
        els.append(z(txt, tx(tag) - 32, y + 24, c, "Bold", 28))
    return els, tx


zs, tx = zeitstrahl(760, "f6")
folie([("f1", f"{PH} › angemessen, erfolglos"), ("f2", f"{PH} › „umgehend“"), ("f3", f"{PH} › „umgehend“ genügt"),
       ("f4", f"{PH} › kein Endtermin nötig"), ("f5", f"{PH} › zu kurze Frist"), ("f6", f"{PH} › 3 Wochen"),
       ("f7", f"{PH} › erfolglos abgelaufen")], rechts_frei([
    *tafel("f1", "3. Frist: angemessen, erfolglos"),
    z("Jörn: „Bitte liefern Sie die Felgen umgehend.“", 110, 180, "f2", "Bold", 32),
    *okz("„umgehend“ genügt: sofortige, unverzügliche", 260, beim("f3", "genügt"), "Bold", 32, x=160),
    z("oder umgehende Leistung verlangt", 160, 305, beim("f3", "unverzügliche"), "Bold", 32),
    zit("BGH, Urt. v. 13.7.2016 – VIII ZR 49/15, Rn. 25", 160, 355, beim("f3", "Bundesgerichtshof")),
    *pkt("kein bestimmter Endtermin nötig", 420, "f4", "Regular", 32, x=160),
    zit("BGH, Urt. v. 12.8.2009 – VIII ZR 254/08, Rn. 10 f.", 160, 465, "f4"),
    *pkt("zu kurze Frist: setzt eine angemessene in Gang", 530, "f5", "Regular", 32, x=160),
    zit("BGH VIII ZR 254/08, Rn. 11; Video „Rücktritt, § 323 BGB“", 160, 575, beim("f5", "kennst")),
    *zs,
    linienzug([(tx(10), 722), (tx(31), 722)], "f6", breite=4, farbe=(40, 150, 85, 255)),
    pl("Jörn wartet 3 Wochen", (tx(10) + tx(31)) / 2, 640, "f6", fill=GRUEN, size=28, anker="m"),
    *okz("Frist erfolglos abgelaufen", 825, "f7", "ExtraBold", 32, x=160),
    *requisit([("f1", ("tabler", "hourglass", 100, HELLBLAU), "Frist?", WEISS),
               ("f2", ("tabler", "mail", 100, WEISS), "„umgehend“", GELB),
               ("f3", ("tabler", "circle-check", 100, GRUEN), "genügt", GRUEN),
               ("f6", ("tabler", "calendar-event", 100, WEISS), "3 Wochen", GELB),
               ("f7", ("tabler", "hourglass-low", 100, HELLROT), "abgelaufen", HELLROT)]),
    *zwei("JO", [("f1", "ruhig"), ("f3", "froh"), ("f6", "muede"), ("f7", "ernst")],
          "IN", [("f1", "ruhig"), ("f2", "denkt"), ("f7", "sorge")]),
]))

# ===========================================================================================================================
# I 4. Entbehrlichkeit, § 281 Abs. 2 BGB (Wortlautkarte)
# ===========================================================================================================================
W2812 = umbruch("„Die Fristsetzung ist entbehrlich, wenn der Schuldner die Leistung ernsthaft und endgültig verweigert oder "
                "wenn besondere Umstände vorliegen, die unter Abwägung der beiderseitigen Interessen die sofortige "
                "Geltendmachung des Schadensersatzanspruchs rechtfertigen.“", 31, 1040)
w2812, w2812_y = wortlaut(80, 180, 1100, W2812, "§ 281 Abs. 2 BGB", "e2",
                          marken=[(_zl(W2812, "ernsthaft"), "ernsthaft und endgültig", beim("e2", "ernsthaft")),
                                  (_zl(W2812, "besondere"), "besondere Umstände", beim("e3", "besondere"))], size=31)
PI = "B. Schema › 4. Entbehrlichkeit, § 281 Abs. 2 BGB"
folie([("e1", "B. Schema › 4. Entbehrlichkeit der Frist"), ("e2", f"{PI} › Verweigerung"), ("e3", f"{PI} › besondere Umstände"),
       ("e5", f"{PI} › strenge Anforderungen"), ("e6", f"{PI} › der Fall"), ("e7", f"{PI} › Frist nötig und gesetzt")], rechts_frei([
    *tafel("e1", "4. Frist entbehrlich?"),
    *w2812,
    blk(110, w2812_y + 30, 1040, 130, HELLBLAU, "e5", [("Verweigerung: strenge Anforderungen", "ExtraBold", 32, INK),
                                                    ("unmissverständlich: unter keinen Umständen", "Bold", 30, INK)]),
    zit("BGH, Urt. v. 1.7.2015 – VIII ZR 226/14, Rn. 33 (§ 281 Abs. 2 Halbsatz 1 BGB)", 110, w2812_y + 175, beim("e5", "Der")),
    *neinz("Ingolf vertröstet nur, er will ja liefern", w2812_y + 240, "e6", "Bold", 32, x=160),
    *okz("Frist also nötig, und Jörn hat sie gesetzt", w2812_y + 305, "e7", "Bold", 32, x=160),
    *requisit([("e1", ("tabler", "hourglass-off", 100, WEISS), "ohne Frist?", WEISS),
               ("e2", ("tabler", "hand-stop", 110, WEISS), "verweigert?", HELLROT),
               ("e5", ("tabler", "scale", 120, WEISS), "strenge Anforderungen", WEISS),
               ("e6", ("tabler", "mail", 100, WEISS), "„kommen bald“", WEISS),
               ("e7", ("tabler", "circle-check", 100, GRUEN), "Frist gesetzt", GRUEN)]),
    *zwei("JO", [("e1", "ruhig"), ("e5", "denkt"), ("e7", "froh")], "IN", [("e1", "ruhig"), ("e6", "froh"), ("e7", "sorge")]),
]))
assert w2812_y + 360 <= 900, w2812_y

# ===========================================================================================================================
# J 5. Vertretenmüssen
# ===========================================================================================================================
PJ = "B. Schema › 5. Vertretenmüssen"
folie([("v1", PJ), ("v2", f"{PJ} › vermutet, § 280 Abs. 1 Satz 2 BGB"), ("v3", f"{PJ} › keine Entlastung")], rechts_frei([
    *tafel("v1", "5. Vertretenmüssen"),
    blk(110, 190, 1040, 110, GELB, "v2", [("vermutet: § 280 Abs. 1 Satz 2 BGB", "ExtraBold", 34, INK)]),
    *pkt("Ingolf müsste sich entlasten", 350, beim("v2", "Ingolf"), "Bold", 32, x=160),
    *pkt("er nennt keinen Grund für die Verzögerung", 415, "v3", "Bold", 32, x=160),
    *requisit([("v1", ("tabler", "user-question", 110, WEISS), "zu vertreten?", WEISS),
               ("v2", ("tabler", "scale", 120, WEISS), "vermutet", GELB),
               ("v3", ("tabler", "message-off", 100, WEISS), "kein Grund", HELLROT)]),
    *zwei("JO", [("v1", "ruhig"), ("v3", "denkt")], "IN", [("v1", "ruhig"), ("v2", "sorge"), ("v3", "still")]),
]))

# ===========================================================================================================================
# K 6. Schaden: Rechenweg
# ===========================================================================================================================
PK = "B. Schema › 6. Schaden"
folie([("d1", PK), ("d2", f"{PK} › § 249 Abs. 1 BGB"), ("d3", f"{PK} › mit Lieferung"), ("d4", f"{PK} › Deckungskauf"),
       ("d5", f"{PK} › Differenz: 250 €"), ("d6", f"{PK} › Schaden statt der Leistung")], rechts_frei([
    *tafel("d1", "6. Schaden"),
    z("so stellen, als hätte Ingolf ordnungsgemäß geliefert", 110, 185, "d2", "Bold", 32),
    zit("§ 249 Abs. 1 BGB", 110, 232, beim("d2", "Paragraf")),
    z("mit Lieferung: Felgen für", 160, 310, "d3", "Regular", 34),
    z("1.200 €", 900, 310, beim("d3", "tausend"), "Bold", 34),
    z("jetzt: gleichwertige Felgen für", 160, 370, "d4", "Regular", 34),
    z("1.450 €", 900, 370, beim("d4", "tausend"), "Bold", 34),
    linienzug([(160, 432), (1060, 432)], "d5", breite=3),
    z("Differenz: 1.450 € – 1.200 € =", 160, 450, "d5", "Regular", 34),
    z("250 €", 900, 450, beim("d5", "zweihundert"), "ExtraBold", 36),
    blk(110, 540, 1040, 130, GRUEN, beim("d5", "Schaden"), [("Schaden: 250 € Mehrkosten", "ExtraBold", 36, INK)]),
    blk(110, 700, 1040, 130, HELLBLAU, "d6", [("Mehrkosten eines Deckungskaufs: kein", "Bold", 31, INK),
                                          ("Verzögerungsschaden, sondern statt der Leistung", "Bold", 31, INK)]),
    zit("BGH, Urt. v. 3.7.2013 – VIII ZR 169/12, Leitsatz, Rn. 27", 110, 845, beim("d6", "Verzögerungsschaden")),
    *requisit([("d1", ("tabler", "calculator", 100, WEISS), "Schaden?", WEISS),
               ("d3", ("tabler", "wheel", 120, HELLGRAU), "Ingolf: 1.200 €", WEISS),
               ("d4", ("tabler", "wheel", 120, BLAU), "Herta: 1.450 €", WEISS),
               ("d5", ("tabler", "coin-euro", 110, GELB), "250 €", GRUEN)]),
    *zwei("JO", [("d1", "ruhig"), ("d4", "denkt"), ("d5", "froh")], "IN", [("d1", "ruhig"), ("d5", "sorge")]),
]))

# ===========================================================================================================================
# L Folge: § 281 Abs. 4 BGB (Wortlautkarte)
# ===========================================================================================================================
W2814 = umbruch("„Der Anspruch auf die Leistung ist ausgeschlossen, sobald der Gläubiger statt der Leistung Schadensersatz "
                "verlangt hat.“", 32, 1040)
w2814, w2814_y = wortlaut(80, 260, 1100, W2814, "§ 281 Abs. 4 BGB", "r2",
                          marken=[(_zl(W2814, "ausgeschlossen"), "ausgeschlossen", beim("r2", "ausgeschlossen")),
                                  (_zl(W2814, "verlangt"), "verlangt", beim("r2", "verlangt"))], size=32)
PL = "C. Folge › § 281 Abs. 4 BGB"
folie([("r1", "C. Folge › Ingolf will noch liefern"), ("r2", PL), ("r3", f"{PL} › Jörn hat Schadensersatz verlangt"),
       ("r4", f"{PL} › nicht beides")], rechts_frei([
    *tafel("r1", "Und die Lieferung nächste Woche?"),
    *pkt("Ingolf will nächste Woche doch noch liefern", 180, "r1", "Bold", 32, x=160),
    *w2814,
    *okz("Jörn hat es mit seiner E-Mail verlangt", w2814_y + 40, "r3", "Bold", 32, x=160),
    blk(110, w2814_y + 120, 1040, 130, GELB, "r4", [("Nicht beides: die Felgen und", "ExtraBold", 33, INK),
                                                 ("Schadensersatz statt der Felgen", "ExtraBold", 33, INK)]),
    zit("BGH, Urt. v. 3.7.2013 – VIII ZR 169/12, Rn. 29", 110, w2814_y + 265, beim("r4", "die")),
    *requisit([("r1", ("tabler", "truck-delivery", 130, WEISS), "nächste Woche?", WEISS),
               ("r2", ("tabler", "ban", 100, HELLROT), "Lieferanspruch ausgeschlossen", HELLROT),
               ("r3", ("tabler", "mail", 100, WEISS), "E-Mail von Jörn", GELB)]),
    *zwei("JO", [("r1", "ruhig"), ("r3", "ernst")], "IN", [("r1", "froh"), ("r2", "staunt"), ("r4", "still")]),
]))
assert w2814_y + 310 <= 900, w2814_y

# ===========================================================================================================================
# M Abgrenzung: Verzögerungsschaden, Rücktritt, § 325 BGB
# ===========================================================================================================================
PM = "D. Abgrenzung"
folie([("ab1", PM), ("ab2", f"{PM} › Verzögerungsschaden"), ("ab2b", f"{PM} › Verzögerungsschaden: Verzug, § 286 BGB"),
       ("ab3", f"{PM} › Rücktritt, § 323 BGB"), ("ab4", f"{PM} › § 325 BGB")], rechts_frei([
    *tafel("ab1", "Zur Abgrenzung"),
    blk(110, 180, 1040, 130, HELLBLAU, "ab2", [("Verzögerungsschaden: allein durch die Verspätung,", "Bold", 30, INK),
                                            ("bleibt auch bei späterer Lieferung", "Bold", 30, INK)]),
    *pkt("etwa: Gebühr für einen geplatzten Montagetermin", 345, beim("ab2", "etwa"), "Regular", 31, x=160),
    *pkt("Verzug nötig: § 280 Abs. 2 mit § 286 BGB", 405, "ab2b", "Bold", 31, x=160),
    zit("Mehr dazu: Video „Schuldnerverzug, § 286 BGB“", 160, 452, beim("ab2b", "mehr")),
    blk(110, 530, 1040, 130, GELB, "ab3", [("bezahlte 1.200 € zurück:", "Bold", 31, INK),
                                        ("Rücktritt, § 323 BGB", "ExtraBold", 33, INK)]),
    zit("Video „Rücktritt, § 323 BGB“; Rückgewähr nach § 346 Abs. 1 BGB", 110, 675, beim("ab3", "Rücktritt")),
    *okz("§ 325 BGB: Rücktritt schließt Schadensersatz nicht aus", 740, "ab4", "Bold", 31, x=160),
    *requisit([("ab1", ("tabler", "arrows-split", 110, None), "Abgrenzung", WEISS),
               ("ab2", ("tabler", "clock", 100, HELLBLAU), "Verspätung", HELLBLAU),
               ("ab3", ("tabler", "arrow-back-up", 100, None), "Rücktritt", GELB),
               ("ab4", ("tabler", "plus", 90, None), "beides möglich", GRUEN)]),
    *zwei("JO", [("ab1", "ruhig"), ("ab3", "froh")], "IN", [("ab1", "ruhig"), ("ab2", "denkt"), ("ab3", "sorge")]),
]))

# ===========================================================================================================================
# N Ergebnis (Fallszene im Laden von Ingolf)
# ===========================================================================================================================
folie([("erg", "Ergebnis · Jörn bekommt 250 €")], [
    *laden("erg"),
    pl("Ergebnis: 250 € Schadensersatz statt der Leistung", 70, 30, beim("erg", "Jörn"), fill=GRUEN, size=32),
    pl("§§ 280 Abs. 1, 3, 281 BGB", 70, 100, beim("erg", "zweihundert"), fill=WEISS, size=30),
    ficon("tabler", "cash-banknote", 1420, 640, 120, beim("erg", "zweihundert"), fuell=GRUEN),
    pl("250 €", 1420, 670, beim("erg", "zweihundert"), fill=GRUEN, size=30, anker="m"),
    *fig("IN", IX, G0, FHA, [("erg", "still_r")], erst="cut"),
    ns("Ingolf", IX, G0, "erg", GRUEN),
    *fig("JO", JX, G0, FHA, [("erg", "ruhig"), (beim("erg", "Schadensersatz"), "froh")], erst="cut"),
    ns("Jörn", JX, G0, "erg", BLAU),
])

# ===========================================================================================================================
# O Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Schaden zuerst einordnen"), ("tipp2", "Klausurtipp · grundsätzlich erfolglose Frist"),
       ("tipp3", "Klausurtipp · auch „umgehend“ ist eine Fristsetzung")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Zuerst den Schaden einordnen:", 200, 200, beim("tipp", "Ordne"), "Bold", 36),
    z("Mehrkosten eines Deckungskaufs", 200, 265, beim("tipp", "Mehrkosten"), "Regular", 34),
    z("= Schaden statt der Leistung", 200, 312, beim("tipp", "Schaden"), "Bold", 34),
    *pkt("also grundsätzlich: erfolglose Frist", 395, "tipp2", "Bold", 34, x=245),
    linienzug([(130, 480), (1130, 480)], "tipp3", breite=3),
    z("Erklärung des Gläubigers genau lesen:", 200, 505, "tipp3", "Regular", 34),
    z("auch „umgehend“ ist eine Fristsetzung", 200, 553, beim("tipp3", "Auch"), "Bold", 34),
    zit("BGH, Urt. v. 13.7.2016 – VIII ZR 49/15, Rn. 25", 200, 610, beim("tipp3", "Auch")),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# P Klausurschema
# ===========================================================================================================================
REIHEN = [("k0", 0, "Anspruch aus §§ 280 Abs. 1, 3, 281 BGB", True),
          ("k1", 1, "1. Schuldverhältnis", False),
          ("k2", 1, "2. Pflichtverletzung: fällige, durchsetzbare Leistung nicht erbracht", False),
          ("k3", 1, "3. angemessene Frist erfolglos abgelaufen", False),
          ("k4", 1, "4. oder Frist entbehrlich (§ 281 Abs. 2 BGB)", False),
          ("k5", 1, "5. Vertretenmüssen (vermutet, § 280 Abs. 1 Satz 2 BGB)", False),
          ("k6", 1, "6. Schaden (§§ 249 ff. BGB)", False),
          ("k7", 0, "Folge: kein Anspruch mehr auf die Leistung (§ 281 Abs. 4 BGB)", True)]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Schema: Schadensersatz statt der Leistung"), 110, 90, "sch", 46)]
y = 240
for c, ebene, text, fett in REIHEN:
    x = (130, 200)[ebene]
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 40 if ebene == 0 else 36, rechts=1800))
    y += {0: 95, 1: 80}[ebene]
assert y <= 970, y
folie([("sch", "Klausurschema"), ("k0", "Klausurschema › Anspruchsgrundlage"), ("k1", "Klausurschema › 1. Schuldverhältnis"),
       ("k2", "Klausurschema › 2. Pflichtverletzung"), ("k3", "Klausurschema › 3. Frist"),
       ("k4", "Klausurschema › 4. Entbehrlichkeit"), ("k5", "Klausurschema › 5. Vertretenmüssen"),
       ("k6", "Klausurschema › 6. Schaden"), ("k7", "Klausurschema › Folge, § 281 Abs. 4 BGB")], els_sch)

# ===========================================================================================================================
# Q Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Wer woanders teurer nachkauft,", 0)], [("verlangt ", 0), ("Schadensersatz", "a")],
                 [("statt der Leistung", "a"), (".", 0)]], 750, 290, 46, "merke",
                {"a": beim("merke", "Schadensersatz")}),
    *markertext([[("Den gibt es grundsätzlich erst", 0)], [("nach einer ", 0), ("erfolglosen Frist", "b"), (".", 0)]],
                750, 600, 46, "mk2", {"b": beim("mk2", "erfolglosen")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
