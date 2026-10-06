"""Folge 206 · § 179 BGB: Vertreter ohne Vertretungsmacht – haftet er persönlich? – Serienstandard Open Peeps (Katzenkönig).
Fiktiver Fall: Kuno verkauft das Motorrad von Enno, das über den Winter in seiner Garage steht, im Namen von Enno für 4.500 € an
Silja, ohne Vollmacht; Enno verweigert die Genehmigung; Silja kauft ein gleichwertiges Motorrad für 5.300 € und verlangt von
Kuno 800 €. Szenen laut ../SZENENPLAN.md. Ein Handlungsgeräusch (Unterschrift beim Kaufvertrag, ../geraeusche_herkunft.json).
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/pkt
als eigene Kopie aus Folge 202 (gemeinsame Dateien unverändert); neu: garage(), motorrad().
Wortlautkarten wörtlich nach gesetze-im-internet.de (Abruf 06.10.2026): § 177 Abs. 1, § 177 Abs. 2, § 178, § 179 Abs. 1–3 BGB.
Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_206/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_206/" in n:
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
NAME = {"EN": "Enno", "KU": "Kuno", "SI": "Silja"}
NFARBE = {"EN": BLAU, "KU": GRUEN, "SI": GELB}


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


def boden_(y, c, fill=None, x0=30, x1=1890, h=None):
    """Boden in Seitenansicht: Tuschelinie, optional Fläche darunter."""
    hh = h or 60
    im = Image.new("RGBA", (x1 - x0, hh))
    dr = ImageDraw.Draw(im)
    if fill:
        dr.rectangle((0, 0, x1 - x0, hh), fill=fill)
    dr.line((0, 2, x1 - x0, 2), fill=INK, width=6)
    return El(im, x0, y, c, "cut", 0.0, None, name="boden")


def garage(c):
    """Garage von innen: Rückwand mit Lochwand und Regalbrett, Rolltor-Lamellen oben (Grundformen)."""
    els = [hart(boden_(G0, c, fill=(226, 226, 222, 255), h=100))]
    w, h = 980, 560
    im = Image.new("RGBA", (w, h))
    dr = ImageDraw.Draw(im)
    dr.rounded_rectangle((0, 0, w - 1, h - 1), 14, fill=WAND, outline=INK, width=5)
    for i in range(4):                                       # aufgerolltes Tor: Lamellen oben
        dr.line((10, 22 + i * 18, w - 10, 22 + i * 18), fill=(150, 150, 150, 255), width=4)
    dr.rounded_rectangle((560, 140, 920, 330), 10, fill=(214, 160, 110, 255), outline=INK, width=5)   # Lochwand
    for yy in range(165, 320, 30):
        for xx in range(585, 910, 30):
            dr.ellipse((xx - 3, yy - 3, xx + 3, yy + 3), fill=INK)
    dr.rectangle((60, 300, 420, 318), fill=(190, 135, 90, 255), outline=INK, width=4)                 # Regalbrett
    els.append(hart(El(im, 70, G0 - h, c, "cut", 0.0, None, name="garage")))
    els.append(hart(ficon("tabler", "tool", 720, 640, 80, c, fuell=WEISS, anim="cut")))
    els.append(hart(ficon("tabler", "hammer", 890, 640, 80, c, fuell=WEISS, anim="cut")))
    els.append(hart(ficon("tabler", "bucket", 150, 640, 80, c, fuell=BLAU, anim="cut")))
    els.append(hart(ficon("tabler", "box", 300, 640, 90, c, fuell=(214, 160, 110, 255), anim="cut")))
    return els


def motorrad(cx, c, fuell=ROT, breite=430, anim="cut", bis=None):
    return ficon("tabler", "motorbike", cx, G0 + 4, breite, c, fuell=fuell, nebenfarbe=WEISS, anim=anim, bis=bis)


# ===========================================================================================================================
# A0 Fall: das Motorrad in der Garage von Kuno (Hook, Enno, Winter)
# ===========================================================================================================================
G0 = 900                                     # Boden der Fallszenen
FHA = 430                                    # Figurenhöhe in den Fallszenen
MX = 520                                     # Motorrad
folie([(NULL, "Fall · Das Motorrad"), ("enno", "Fall · Enno und sein Motorrad"),
       ("garage", "Fall · Über den Winter in der Garage von Kuno")], [
    *garage(NULL),
    hart(motorrad(MX, NULL)),
    pl("Dein Motorrad – verkauft „in deinem Namen“", 70, 30, beim("fall", "verkauft"), fill=GELB, size=32),
    pl("Du willst davon nichts wissen", 70, 100, beim("fall", "nichts"), fill=HELLROT, size=32),
    *fig("EN", 1230, G0, FHA, [(beim("enno", "Enno"), "froh")]),
    ns("Enno", 1230, G0, beim("enno", "Enno"), BLAU, d=0.1),
    ficon("tabler", "snowflake", 520, 440, 90, beim("garage", "Winter"), fuell=HELLBLAU),
    pl("über den Winter", 520, 470, beim("garage", "Winter"), fill=WEISS, size=28, anker="m"),
    *fig("KU", 1620, G0, FHA, [(beim("garage", "Kuno"), "froh")]),
    ns("Kuno", 1620, G0, beim("garage", "Kuno"), GRUEN, d=0.1),
    pl("Garage von Kuno", 1620, 330, beim("garage", "Garage"), fill=WEISS, size=28, anker="m"),
])

# ===========================================================================================================================
# A1 Fall: Kuno verkauft an Silja (Figurenrede, Kaufvertrag mit Unterschrift, Kuno weiß, Silja vertraut)
# ===========================================================================================================================
KX, SX = 1120, 1640
folie([("silja", "Fall · Silja fragt nach dem Motorrad"), ("k1", "Fall · Kuno verkauft im Namen von Enno"),
       ("s1", "Fall · Silja: Abgemacht!"), ("vertrag", "Fall · Der Kaufvertrag"),
       ("weiss", "Fall · Kuno weiß: Enno hat nie zugestimmt"), ("zweifel", "Fall · Silja hat keinen Anlass zu Zweifeln")], [
    *garage("silja"),
    motorrad(MX, "silja"),
    pl("Eines Tages", 70, 30, beim("silja", "Eines"), fill=GELB, size=32),
    *fig("KU", KX, G0, FHA, [("silja", "ruhig_r")], bis="k1", erst="cut"),
    *redet("KU_redet_r", KX, G0, FHA, "k1", "s1"),
    *fig("KU", KX, G0, FHA, [("s1", "froh_r"), ("weiss", "denkt_r"), ("zweifel", "sorge_r")], erst="cut"),
    ns("Kuno", KX, G0, "silja", GRUEN),
    *fig("SI", SX, G0, FHA, [(beim("silja", "Silja"), "froh")], bis="s1"),
    *redet("SI_redet", SX, G0, FHA, "s1", "vertrag"),
    *fig("SI", SX, G0, FHA, [("vertrag", "froh"), ("zweifel", "freut")], erst="cut"),
    ns("Silja", SX, G0, beim("silja", "Silja"), GELB, d=0.1),
    pl("Zu verkaufen?", 1640, 380, beim("silja", "fragt"), fill=WEISS, size=28, anker="m", bis="k1"),
    blase("sprech", 900, 230, "k1", 1240, 230, inhalt=["Enno will es loswerden. Ich verkaufe", "es dir in seinem Namen, für 4.500 €."],
          textsize=34, figur=("KU_redet_r", KX, G0, FHA), bis="s1"),
    blase("sprech", 760, 200, "s1", 1420, 230, inhalt=["Abgemacht! Ich hole", "es am Samstag ab."],
          textsize=34, figur=("SI_redet", SX, G0, FHA), bis="vertrag"),
    szene(ficon("tabler", "file-text", 1380, 360, 120, "vertrag", fuell=WEISS), "206unterschrift*", 0.55,
          T_(beim("vertrag", "unterschreiben")) - T_("vertrag")),
    ficon("tabler", "writing-sign", 1480, 330, 80, beim("vertrag", "unterschreiben"), fuell=GELB),
    pl("Kaufvertrag: 4.500 €", 1380, 140, beim("vertrag", "Kaufvertrag"), fill=GELB, size=30, anker="m"),
    pl("Kuno weiß: Enno hat nie zugestimmt", 70, 100, beim("weiss", "Enno"), fill=HELLROT, size=32),
    pl("Silja: kein Anlass zu Zweifeln", 70, 170, beim("zweifel", "keinen"), fill=GRUEN, size=32),
])

# ===========================================================================================================================
# A2 Fall: Samstag in der Garage (Enno verweigert die Genehmigung)
# ===========================================================================================================================
KX2, SX2, EX2 = 1160, 1440, 1730
folie([("samstag", "Fall · Samstag: Enno kommt in die Garage"), ("e1", "Fall · Enno verweigert die Genehmigung")], [
    *garage("samstag"),
    motorrad(MX, "samstag"),
    pl("Samstag", 70, 30, beim("samstag", "Samstag"), fill=GELB, size=32),
    *fig("KU", KX2, G0, FHA, [("samstag", "ruhig_r"), ("e1", "schreck_r")], erst="cut"),
    ns("Kuno", KX2, G0, "samstag", GRUEN),
    *fig("SI", SX2, G0, FHA, [("samstag", "froh_r"), ("e1", "staunt_r")], erst="cut"),
    ns("Silja", SX2, G0, "samstag", GELB),
    *fig("EN", EX2, G0, FHA, [(beim("samstag", "Enno"), "ernst")], bis="e1"),
    *redet("EN_redet", EX2, G0, FHA, "e1", "haendler"),
    ns("Enno", EX2, G0, beim("samstag", "Enno"), BLAU, d=0.1),
    blase("sprech", 820, 200, "e1", 1260, 230, inhalt=["Davon will ich nichts wissen.", "Das genehmige ich nicht!"],
          textsize=34, figur=("EN_redet", EX2, G0, FHA)),
])

# ===========================================================================================================================
# A3 Fall: beim Händler (Ersatzkauf 5.300 €, Silja fordert 800 € von Kuno, die Frage)
# ===========================================================================================================================
SX3, KX3 = 1180, 1690
folie([("haendler", "Fall · Silja kauft beim Händler: 5.300 €"), ("s2", "Fall · Silja: 800 € Mehrkosten"),
       ("frage", "Fall · Die Frage")], [
    hart(boden_(G0, "haendler", fill=(236, 230, 220, 255), h=100)),
    ficon("tabler", "building-store", 300, G0 + 4, 330, "haendler", fuell=HELLBLAU, anim="cut"),
    pl("Händler", 300, 480, beim("haendler", "Händler"), fill=WEISS, size=28, anker="m"),
    motorrad(740, "haendler", fuell=BLAU, breite=400),
    pl("gleichwertig: 5.300 €", 740, 560, beim("haendler", "fünftausend"), fill=GELB, size=30, anker="m"),
    *fig("SI", SX3, G0, FHA, [("haendler", "ruhig")], bis="s2", erst="cut"),
    *redet("SI_fordert_r", SX3, G0, FHA, "s2", "frage"),
    *fig("SI", SX3, G0, FHA, [("frage", "ernst_r")], erst="cut"),
    ns("Silja", SX3, G0, "haendler", GELB),
    ficon("tabler", "phone", 1270, 520, 60, "s2", fuell=WEISS),
    *fig("KU", KX3, G0, FHA, [("s2", "schreck"), ("frage", "sorge")]),
    ns("Kuno", KX3, G0, "s2", GRUEN, d=0.1),
    ficon("tabler", "phone", 1600, 520, 60, "s2", fuell=WEISS),
    blase("sprech", 820, 200, "s2", 1440, 230, inhalt=["Kuno, die 800 € Mehrkosten", "zahlst du mir!"],
          textsize=34, figur=("SI_fordert_r", SX3, G0, FHA), bis="frage"),
    pl("Haftet Kuno persönlich?", 70, 30, "frage", fill=PINK, size=34),
    pl("Schritt für Schritt", 70, 105, beim("frage2", "Schritt"), fill=WEISS, size=32),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_206(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=35, zeilenabstand=1.3)
        els += e; y += 14
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_206("sv", [
    "Das Motorrad von Enno steht über den Winter in der Garage seines Bekannten Kuno. Silja fragt, ob es zu verkaufen ist. "
    "Kuno sagt: „Enno will es loswerden. Ich verkaufe es dir in seinem Namen, für 4.500 €.“ Beide unterschreiben einen "
    "Kaufvertrag; am Samstag will Silja das Motorrad abholen.",
    "Kuno weiß, dass Enno nie zugestimmt hat. Silja hat keinen Anlass, daran zu zweifeln.",
    "Am Samstag trifft Enno in der Garage auf Silja: „Davon will ich nichts wissen. Das genehmige ich nicht!“ Silja kauft "
    "ein gleichwertiges Motorrad beim Händler für 5.300 € und verlangt von Kuno 800 € Mehrkosten.",
], "Haftet Kuno persönlich?")

# ===========================================================================================================================
# C Ausgangslage: Voraussetzungen der Stellvertretung (Verweis Folge 043), keine Vertretungsmacht
# ===========================================================================================================================
PC = "Ausgangslage › Stellvertretung, § 164 Abs. 1 BGB"
folie([("vor", "Ausgangslage"), ("drei", PC), ("hier", f"{PC} › Erklärung im Namen von Enno"),
       ("ohne", f"{PC} › keine Vollmacht"), ("schein", f"{PC} › keine Rechtsscheinsvollmacht"),
       ("falsus", "Ausgangslage › Vertreter ohne Vertretungsmacht")], rechts_frei([
    *tafel("vor", "Ausgangslage"),
    z("Wirksame Vertretung (§ 164 Abs. 1 BGB):", 110, 180, "drei", "Bold", 32),
    *pkt("eigene Willenserklärung", 240, beim("drei", "eigene"), "Regular", 32, x=160),
    *pkt("im fremden Namen", 295, beim("drei", "fremden"), "Regular", 32, x=160),
    *pkt("mit Vertretungsmacht", 350, beim("drei", "mit"), "Regular", 32, x=160),
    zit("Die Voraussetzungen im Einzelnen: Folge zur Stellvertretung", 160, 405, beim("drei", "kennst")),
    *okz("Kuno erklärt selbst, ausdrücklich im Namen von Enno", 470, "hier", "Bold", 31, x=160),
    *neinz("Vollmacht: hat Enno nie erteilt", 535, "ohne", "Bold", 31, x=160),
    *neinz("Duldungs- oder Anscheinsvollmacht: Kuno tritt", 600, "schein", "Bold", 31, x=160),
    z("zum ersten Mal für Enno auf", 160, 643, beim("schein", "Kuno"), "Bold", 31),
    blk(110, 715, 1040, 130, GELB, "falsus", [("Kuno ist Vertreter ohne Vertretungsmacht", "ExtraBold", 33, INK),
                                           ("(falsus procurator)", "Bold", 31, INK)]),
    *requisit([("vor", ("tabler", "motorbike", 170, ROT), "Wer ist gebunden?", WEISS),
               ("hier", ("tabler", "file-text", 110, WEISS), "im Namen von Enno", WEISS),
               ("ohne", ("tabler", "license", 110, WEISS), "keine Vollmacht", HELLROT),
               ("falsus", ("tabler", "user-x", 110, WEISS), "falsus procurator", GELB)]),
    *zwei("KU", [("vor", "ruhig"), ("ohne", "sorge"), ("falsus", "still")], "EN", [("vor", "ruhig"), ("hier", "denkt"), ("ohne", "ernst")]),
]))

# ===========================================================================================================================
# D § 177 Abs. 1 BGB: schwebend unwirksam (Wortlautkarte), Genehmigung § 184 Abs. 1
# ===========================================================================================================================
W1771 = umbruch("„Schließt jemand ohne Vertretungsmacht im Namen eines anderen einen Vertrag, so hängt die Wirksamkeit des "
                "Vertrags für und gegen den Vertretenen von dessen Genehmigung ab.“", 32, 1040)
_zl = lambda W, wort: next(i for i, t in enumerate(W) if wort in t)
w1771, w1771_y = wortlaut(80, 180, 1100, W1771, "§ 177 Abs. 1 BGB", "p177",
                          marken=[(_zl(W1771, "Vertretungsmacht"), "Vertretungsmacht", beim("p177", "Vertretungsmacht")),
                                  (_zl(W1771, "Genehmigung"), "Genehmigung", beim("p177", "Genehmigung"))], size=32)
PD = "§ 177 Abs. 1 BGB"
folie([("p177", f"{PD} › Genehmigung"), ("schweb", f"{PD} › schwebend unwirksam"),
       ("genehm", f"{PD} › Genehmigung wirkt zurück, § 184 Abs. 1 BGB"), ("verw", f"{PD} › Verweigerung")], rechts_frei([
    *tafel("p177", "Die Schwebezeit"),
    *w1771,
    blk(110, w1771_y + 40, 1040, 90, HELLBLAU, "schweb", [("Der Kaufvertrag ist schwebend unwirksam", "ExtraBold", 33, INK)]),
    *pkt("Enno genehmigt: rückwirkend Vertragspartner", w1771_y + 175, "genehm", "Bold", 31, x=160),
    zit("§ 184 Abs. 1 BGB; BGH, Urt. v. 11.4.2025 – V ZR 194/23, Rn. 17", 160, w1771_y + 220, beim("genehm", "Paragraf")),
    *pkt("Enno verweigert: Vertrag bleibt für ihn unwirksam", w1771_y + 285, "verw", "Bold", 31, x=160),
    *requisit([("p177", ("tabler", "file-text", 110, WEISS), "Genehmigung?", WEISS),
               ("schweb", ("tabler", "hourglass-high", 100, HELLBLAU), "schwebend unwirksam", HELLBLAU),
               ("genehm", ("tabler", "circle-check", 100, GRUEN), "Genehmigung", GRUEN),
               ("verw", ("tabler", "circle-x", 100, HELLROT), "Verweigerung", HELLROT)]),
    *zwei("SI", [("p177", "ruhig"), ("schweb", "denkt"), ("verw", "sorge")], "EN", [("p177", "ruhig"), ("genehm", "denkt"), ("verw", "ernst")]),
]))
assert w1771_y + 320 <= 930, w1771_y

# ===========================================================================================================================
# E § 177 Abs. 2 BGB: Aufforderung, Zwei-Wochen-Frist (Wortlautkarte)
# ===========================================================================================================================
W1772 = umbruch("„Fordert der andere Teil den Vertretenen zur Erklärung über die Genehmigung auf, so kann die Erklärung nur "
                "ihm gegenüber erfolgen; eine vor der Aufforderung dem Vertreter gegenüber erklärte Genehmigung oder "
                "Verweigerung der Genehmigung wird unwirksam. Die Genehmigung kann nur bis zum Ablauf von zwei Wochen nach "
                "dem Empfang der Aufforderung erklärt werden; wird sie nicht erklärt, so gilt sie als verweigert.“", 30, 1040)
w1772, w1772_y = wortlaut(80, 180, 1100, W1772, "§ 177 Abs. 2 BGB", "p1772",
                          marken=[(_zl(W1772, "Fordert"), "Fordert", beim("p1772", "auffordern")),
                                  (_zl(W1772, "ihm"), "ihm", beim("ihr", "ihr")),
                                  (_zl(W1772, "Vertreter"), "Vertreter", beim("vorher", "Kuno")),
                                  (_zl(W1772, "Wochen"), "Wochen", beim("frist", "zwei")),
                                  (_zl(W1772, "verweigert"), "verweigert", beim("schweigt", "verweigert"))], size=30)
PE = "§ 177 Abs. 2 BGB"
folie([("auff", "Schwebezeit › Silja muss nicht warten"), ("p1772", f"{PE} › Aufforderung"),
       ("ihr", f"{PE} › Erklärung nur ihr gegenüber"), ("vorher", f"{PE} › frühere Erklärung an Kuno unwirksam"),
       ("frist", f"{PE} › zwei Wochen"), ("schweigt", f"{PE} › Schweigen gilt als Verweigerung")], rechts_frei([
    *tafel("auff", "Silja muss nicht ewig warten"),
    *w1772,
    *pkt("Frist: zwei Wochen nach Empfang der Aufforderung", w1772_y + 40, "frist", "Bold", 31, x=160),
    *pkt("Enno schweigt: Genehmigung gilt als verweigert", w1772_y + 100, "schweigt", "Bold", 31, x=160),
    *requisit([("auff", ("tabler", "hourglass-high", 100, HELLBLAU), "nicht ewig warten", WEISS),
               ("p1772", ("tabler", "mail-question", 110, WEISS), "Aufforderung", GELB),
               ("frist", ("tabler", "calendar", 100, WEISS), "2 Wochen", GELB),
               ("schweigt", ("tabler", "message-off", 100, WEISS), "Schweigen = verweigert", HELLROT)]),
    *zwei("SI", [("auff", "ruhig"), ("p1772", "denkt"), ("schweigt", "ernst")], "EN", [("auff", "ruhig"), ("ihr", "denkt"), ("schweigt", "sorge")]),
]))
assert w1772_y + 150 <= 930, w1772_y

# ===========================================================================================================================
# F § 178 BGB: Widerruf des anderen Teils (Wortlautkarte)
# ===========================================================================================================================
W178 = umbruch("„Bis zur Genehmigung des Vertrags ist der andere Teil zum Widerruf berechtigt, es sei denn, dass er den Mangel "
               "der Vertretungsmacht bei dem Abschluss des Vertrags gekannt hat. Der Widerruf kann auch dem Vertreter "
               "gegenüber erklärt werden.“", 32, 1040)
w178, w178_y = wortlaut(80, 180, 1100, W178, "§ 178 BGB", "p178",
                        marken=[(_zl(W178, "Widerruf"), "Widerruf", beim("p178", "widerrufen")),
                                (_zl(W178, "gekannt"), "gekannt", beim("kennt", "gekannt")),
                                (_zl(W178, "Vertreter"), "Vertreter", beim("adr", "Kuno"))], size=32)
PF = "Widerruf, § 178 BGB"
folie([("p178", f"{PF} › bis zur Genehmigung"), ("kennt", f"{PF} › nicht bei Kenntnis des Mangels"),
       ("nurk", f"{PF} › nur echte Kenntnis"), ("adr", f"{PF} › auch gegenüber Kuno")], rechts_frei([
    *tafel("p178", "Silja darf aussteigen"),
    *w178,
    blk(110, w178_y + 40, 1040, 90, HELLBLAU, "nurk", [("Hier zählt nur echte Kenntnis", "ExtraBold", 33, INK)]),
    *okz("Widerruf auch gegenüber Kuno möglich", w178_y + 175, "adr", "Bold", 31, x=160),
    *requisit([("p178", ("tabler", "arrow-back-up", 100, None), "Widerruf", GELB),
               ("kennt", ("tabler", "eye", 110, HELLBLAU), "Kenntnis beim Abschluss?", WEISS),
               ("adr", ("tabler", "message-2", 100, WEISS), "an Kuno", GRUEN)]),
    *zwei("SI", [("p178", "denkt"), ("nurk", "ruhig")], "KU", [("p178", "sorge"), ("adr", "ruhig")]),
]))
assert w178_y + 220 <= 930, w178_y

# ===========================================================================================================================
# G1 § 179 Abs. 1 BGB: Haftung des Vertreters (Wortlautkarte), Beweislast
# ===========================================================================================================================
W1791 = umbruch("„Wer als Vertreter einen Vertrag geschlossen hat, ist, sofern er nicht seine Vertretungsmacht nachweist, dem "
                "anderen Teil nach dessen Wahl zur Erfüllung oder zum Schadensersatz verpflichtet, wenn der Vertretene die "
                "Genehmigung des Vertrags verweigert.“", 32, 1040)
w1791, w1791_y = wortlaut(80, 260, 1100, W1791, "§ 179 Abs. 1 BGB", "p179",
                          marken=[(_zl(W1791, "nachweist"), "nachweist", beim("p179", "nachweist")),
                                  (_zl(W1791, "Wahl"), "Wahl", beim("p179", "Wahl")),
                                  (_zl(W1791, "Erfüllung"), "Erfüllung", beim("p179", "Erfüllung")),
                                  (_zl(W1791, "Schadensersatz"), "Schadensersatz", beim("p179", "Schadensersatz")),
                                  (_zl(W1791, "verweigert"), "verweigert", beim("p179", "verweigert"))], size=32)
PG = "Haftung: § 179 Abs. 1 BGB"
folie([("jetzt", "Genehmigung verweigert"), ("p179", f"{PG} › Erfüllung oder Schadensersatz"),
       ("beweis", f"{PG} › Beweislast beim Vertreter")], rechts_frei([
    *tafel("jetzt", "Haftet Kuno persönlich?"),
    *pkt("Enno hat die Genehmigung verweigert", 180, "jetzt", "Bold", 32, x=160),
    *w1791,
    blk(110, w1791_y + 40, 1040, 90, GELB, "beweis", [("Vertretungsmacht beweisen muss Kuno", "ExtraBold", 33, INK)]),
    zit("BGH, Urt. v. 25.10.2012 – III ZR 266/11, Rn. 39", 110, w1791_y + 145, beim("beweis", "nicht")),
    *requisit([("jetzt", ("tabler", "circle-x", 100, HELLROT), "verweigert", HELLROT),
               ("p179", ("tabler", "scale", 120, WEISS), "Kuno haftet selbst?", WEISS),
               ("beweis", ("tabler", "license", 110, WEISS), "Beweis: Kuno", GELB)]),
    *zwei("SI", [("jetzt", "ernst"), ("p179", "denkt")], "KU", [("jetzt", "sorge"), ("beweis", "schreck")]),
]))
assert w1791_y + 190 <= 930, w1791_y

# ===========================================================================================================================
# G2 Die Wahl: Erfüllung oder Schadensersatz (Erfüllungsinteresse)
# ===========================================================================================================================
PG2 = "§ 179 Abs. 1 BGB › Wahl"
folie([("wahl", PG2), ("erf", f"{PG2} › Erfüllung"), ("se", f"{PG2} › Schadensersatz: Erfüllungsinteresse"),
       ("stellt", f"{PG2} › als wäre der Vertrag erfüllt")], rechts_frei([
    *tafel("wahl", "Silja hat die Wahl"),
    blk(110, 180, 1040, 130, WEISS, "erf", [("Erfüllung? Hilft wenig:", "Bold", 32, INK),
                                         ("Das Motorrad gehört Enno, nicht Kuno", "ExtraBold", 32, INK)]),
    blk(110, 350, 1040, 130, GRUEN, "se", [("Schadensersatz:", "Bold", 32, INK),
                                        ("das Erfüllungsinteresse", "ExtraBold", 34, INK)]),
    z("Silja wird so gestellt, als hätte der Vertrag", 110, 515, "stellt", "Bold", 32),
    z("gegolten und wäre erfüllt worden", 110, 560, beim("stellt", "gegolten"), "Bold", 32),
    zit("BGH, Urt. v. 25.10.2012 – III ZR 266/11, Rn. 34", 110, 625, beim("stellt", "gegolten")),
    zit("BGH, Urt. v. 18.5.2017 – VII ZR 122/14, Rn. 24 (Mehraufwand)", 110, 665, beim("stellt", "gegolten")),
    *requisit([("wahl", ("tabler", "arrows-split", 110, None), "Erfüllung oder Schadensersatz", WEISS),
               ("erf", ("tabler", "motorbike", 170, ROT), "gehört Enno", WEISS),
               ("se", ("tabler", "coin-euro", 110, GELB), "Erfüllungsinteresse", GRUEN)]),
    *zwei("SI", [("wahl", "froh"), ("erf", "denkt"), ("se", "froh")], "KU", [("wahl", "sorge"), ("se", "schreck")]),
]))

# ===========================================================================================================================
# H § 179 Abs. 2 BGB: Vertreter kannte den Mangel nicht (Wortlautkarte)
# ===========================================================================================================================
W1792 = umbruch("„Hat der Vertreter den Mangel der Vertretungsmacht nicht gekannt, so ist er nur zum Ersatz desjenigen Schadens "
                "verpflichtet, welchen der andere Teil dadurch erleidet, dass er auf die Vertretungsmacht vertraut, jedoch "
                "nicht über den Betrag des Interesses hinaus, welches der andere Teil an der Wirksamkeit des Vertrags hat.“",
                31, 1040)
w1792, w1792_y = wortlaut(80, 180, 1100, W1792, "§ 179 Abs. 2 BGB", "p1792",
                          marken=[(_zl(W1792, "gekannt"), "gekannt", beim("p1792", "gekannt")),
                                  (_zl(W1792, "vertraut"), "vertraut", beim("vertr", "vertraut")),
                                  (_zl(W1792, "Wirksamkeit"), "Wirksamkeit", beim("deckel", "Wirksamkeit"))], size=31)
PH = "§ 179 Abs. 2 BGB"
folie([("p1792", f"{PH} › Vertreter kannte den Mangel nicht"), ("vertr", f"{PH} › nur Vertrauensschaden"),
       ("anh", f"{PH} › Beispiel: Anhänger"), ("deckel", f"{PH} › höchstens das Erfüllungsinteresse")], rechts_frei([
    *tafel("p1792", "Milder: Vertreter ahnungslos"),
    *w1792,
    blk(110, w1792_y + 40, 1040, 90, HELLBLAU, "vertr", [("nur der Vertrauensschaden", "ExtraBold", 33, INK)]),
    *pkt("zum Beispiel 90 € Miete für einen Anhänger", w1792_y + 170, "anh", "Regular", 31, x=160),
    *pkt("höchstens: Interesse an der Wirksamkeit", w1792_y + 225, "deckel", "Bold", 31, x=160),
    *requisit([("p1792", ("tabler", "eye-off", 110, WEISS), "Mangel nicht gekannt", WEISS),
               ("vertr", ("tabler", "heart-handshake", 120, PINK), "Vertrauen", PINK),
               ("anh", ("tabler", "truck", 130, HELLBLAU), "Anhänger: 90 €", GELB),
               ("deckel", ("tabler", "arrow-bar-to-up", 100, None), "Obergrenze", WEISS)]),
    *zwei("KU", [("p1792", "denkt"), ("vertr", "ruhig")], "SI", [("p1792", "ruhig"), ("anh", "denkt"), ("deckel", "ruhig")]),
]))
assert w1792_y + 265 <= 930, w1792_y

# ===========================================================================================================================
# I § 179 Abs. 3 BGB: Ausschluss (Wortlautkarte)
# ===========================================================================================================================
W1793 = umbruch("„Der Vertreter haftet nicht, wenn der andere Teil den Mangel der Vertretungsmacht kannte oder kennen musste. "
                "Der Vertreter haftet auch dann nicht, wenn er in der Geschäftsfähigkeit beschränkt war, es sei denn, dass "
                "er mit Zustimmung seines gesetzlichen Vertreters gehandelt hat.“", 31, 1040)
w1793, w1793_y = wortlaut(80, 180, 1100, W1793, "§ 179 Abs. 3 BGB", "p1793",
                          marken=[(_zl(W1793, "kannte"), "kannte", beim("p1793", "kannte")),
                                  (_zl(W1793, "musste"), "musste", beim("p1793", "kennen")),
                                  (_zl(W1793, "beschränkt"), "beschränkt", beim("minder", "beschränkt")),
                                  (_zl(W1793, "Zustimmung"), "Zustimmung", beim("minder", "Zustimmung"))], size=31)
PI = "§ 179 Abs. 3 BGB"
folie([("p1793", f"{PI} › Kenntnis oder Kennenmüssen"), ("minder", f"{PI} › beschränkt geschäftsfähiger Vertreter"),
       ("nichts", f"{PI} › hier kein Ausschluss")], rechts_frei([
    *tafel("p1793", "Kein Ausschluss?"),
    *w1793,
    zit("kennen musste = aus Fahrlässigkeit nicht kannte (§ 122 Abs. 2 BGB)", 110, w1793_y + 20, beim("p1793", "also")),
    *neinz("Silja: kein Anlass zu Zweifeln", w1793_y + 85, beim("nichts", "Silja"), "Bold", 31, x=160),
    *neinz("Kuno: volljährig", w1793_y + 145, beim("nichts", "Kuno"), "Bold", 31, x=160),
    *requisit([("p1793", ("tabler", "eye", 110, HELLBLAU), "kannte oder kennen musste", WEISS),
               ("minder", ("tabler", "user-question", 110, WEISS), "beschränkt geschäftsfähig", WEISS),
               ("nichts", ("tabler", "circle-check", 100, GRUEN), "kein Ausschluss", GRUEN)]),
    *zwei("SI", [("p1793", "ruhig"), ("nichts", "froh")], "KU", [("p1793", "denkt"), ("minder", "ruhig"), ("nichts", "sorge")]),
]))
assert w1793_y + 190 <= 930, w1793_y

# ===========================================================================================================================
# J1 Falllösung (800 €)
# ===========================================================================================================================
PJ = "Lösung"
folie([("loes", PJ), ("geg", f"{PJ} › Silja gegen Enno"), ("gegk", f"{PJ} › Silja gegen Kuno, § 179 Abs. 1 BGB"),
       ("voll", f"{PJ} › Kuno kannte den Mangel"), ("rechn", f"{PJ} › Mehrkosten"), ("erg", "Ergebnis · Kuno zahlt 800 €")], rechts_frei([
    *tafel("loes", "Die Lösung"),
    *neinz("Silja gegen Enno: nicht Vertragspartner", 180, "geg", "Bold", 32, x=160),
    *okz("Silja gegen Kuno: § 179 Abs. 1 BGB", 245, "gegk", "Bold", 32, x=160),
    *okz("Kuno kannte den Mangel: volle Haftung", 310, "voll", "Bold", 32, x=160),
    z("gleichwertiges Motorrad", 160, 400, "rechn", "Regular", 32),
    z("5.300 €", 900, 400, beim("rechn", "fünftausend"), "Bold", 32),
    z("statt Kaufpreis", 160, 450, beim("rechn", "statt"), "Regular", 32),
    z("– 4.500 €", 873, 450, beim("rechn", "viertausend"), "Bold", 32),
    linienzug([(160, 505), (1060, 505)], beim("rechn", "viertausend"), breite=3),
    blk(110, 540, 1040, 110, GRUEN, "erg", [("Kuno muss Silja 800 € ersetzen", "ExtraBold", 36, INK)]),
    *requisit([("loes", ("tabler", "scale", 120, WEISS), "Lösung", WEISS),
               ("geg", ("tabler", "circle-x", 100, HELLROT), "nicht gegen Enno", HELLROT),
               ("gegk", ("tabler", "circle-check", 100, GRUEN), "gegen Kuno", GRUEN),
               ("rechn", ("tabler", "calculator", 100, WEISS), "Mehrkosten", GELB),
               ("erg", ("tabler", "coin-euro", 110, GELB), "800 €", GRUEN)]),
    *zwei("SI", [("loes", "ruhig"), ("gegk", "froh"), ("erg", "freut")], "KU", [("loes", "ruhig"), ("voll", "sorge"), ("erg", "still")]),
]))

# ===========================================================================================================================
# J2 Fall: Kuno zahlt (Figurenrede)
# ===========================================================================================================================
KX4, SX4 = 1160, 1640
folie([("k2", "Fall · Kuno zahlt 800 €")], [
    *garage("k2"),
    motorrad(MX, "k2"),
    *redet("KU_klagt_r", KX4, G0, FHA, "k2", "p180"),
    ns("Kuno", KX4, G0, "k2", GRUEN),
    *fig("SI", SX4, G0, FHA, [("k2", "ernst")], erst="cut"),
    ns("Silja", SX4, G0, "k2", GELB),
    ficon("tabler", "cash-banknote", 1400, 560, 120, "k2", fuell=GRUEN),
    pl("800 €", 1400, 590, "k2", fill=GRUEN, size=30, anker="m"),
    blase("sprech", 760, 180, "k2", 1420, 230, inhalt=["Und ich dachte, Enno", "freut sich über das Geld."],
          textsize=34, figur=("KU_klagt_r", KX4, G0, FHA)),
])

# ===========================================================================================================================
# K § 180 BGB in einem Satz (einseitige Rechtsgeschäfte)
# ===========================================================================================================================
PK = "Einseitige Rechtsgeschäfte: § 180 BGB"
folie([("p180", f"{PK} › unzulässig, nichtig"), ("ausn", f"{PK} › Ausnahme: nicht beanstandet, einverstanden")], rechts_frei([
    *tafel("p180", "Einseitige Rechtsgeschäfte"),
    z("zum Beispiel eine Kündigung", 110, 180, beim("p180", "Kündigung"), "Bold", 32),
    blk(110, 245, 1040, 130, HELLROT, beim("p180", "Hier"), [("Vertretung ohne Vertretungsmacht unzulässig,", "Bold", 32, INK),
                                                          ("die Erklärung ist nichtig", "ExtraBold", 33, INK)]),
    zit("§ 180 Satz 1 BGB; BGH, Urt. v. 1.7.2026 – VIII ZR 4/23, Rn. 37", 110, 390, beim("p180", "nichtig")),
    *pkt("es sei denn, der Empfänger hat die behauptete", 465, "ausn", "Regular", 32, x=160),
    z("Vertretungsmacht nicht beanstandet", 160, 510, beim("ausn", "Vertretungsmacht"), "Regular", 32),
    z("oder war einverstanden", 160, 555, beim("ausn", "oder"), "Regular", 32),
    zit("§ 180 Satz 2 BGB", 160, 610, beim("ausn", "oder")),
    *requisit([("p180", ("tabler", "file-x", 110, WEISS), "Kündigung", WEISS),
               ("ausn", ("tabler", "user-check", 110, WEISS), "einverstanden?", GELB)]),
    *zwei("EN", [("p180", "ruhig"), ("ausn", "denkt")], "KU", [("p180", "ruhig"), ("ausn", "denkt")]),
]))

# ===========================================================================================================================
# L Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · zuerst gegen den Vertretenen"), ("tp1", "Klausurtipp · scheitert der Anspruch?"),
       ("tp2", "Klausurtipp · dann gegen den Vertreter"), ("tp3", "Klausurtipp · § 179 BGB als Anspruchsgrundlage"),
       ("tp4", "Klausurtipp · Beweislast")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Zuerst: Anspruch gegen den Vertretenen", 200, 200, beim("tipp", "Prüfe"), "Bold", 36),
    z("scheitert er an fehlender Vertretungsmacht", 200, 265, "tp1", "Regular", 34),
    z("und verweigerter Genehmigung,", 200, 312, beim("tp1", "verweigerten"), "Regular", 34),
    *pkt("dann: Anspruch gegen den Vertreter", 385, "tp2", "Bold", 34, x=245),
    linienzug([(130, 470), (1130, 470)], "tp3", breite=3),
    z("§ 179 BGB ist selbst Anspruchsgrundlage –", 200, 495, "tp3", "Bold", 34),
    z("anders als § 164 BGB", 200, 543, beim("tp3", "anders"), "Bold", 34),
    z("Kenntnis oder Kennenmüssen des anderen", 200, 625, "tp4", "Regular", 33),
    z("(Abs. 3): Beweislast beim Vertreter", 200, 671, beim("tp4", "muss"), "Regular", 33),
    zit("BGH, Urt. v. 25.10.2012 – III ZR 266/11, Rn. 42", 200, 725, beim("tp4", "muss")),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# M Prüfschema
# ===========================================================================================================================
REIHEN = [("c1", 0, "I. Silja gegen Enno, § 433 Abs. 1 BGB", True),
          ("c2", 1, "kein Vertrag: ohne Vertretungsmacht, Genehmigung verweigert", False),
          ("c3", 0, "II. Silja gegen Kuno, § 179 Abs. 1 BGB", True),
          ("c4", 1, "1. Vertrag als Vertreter im fremden Namen", False),
          ("c5", 1, "2. ohne Vertretungsmacht", False),
          ("c6", 1, "3. Genehmigung verweigert", False),
          ("c7", 1, "4. kein Ausschluss nach § 179 Abs. 3 BGB", False),
          ("c8", 1, "5. Rechtsfolge: Wahl zwischen Erfüllung und Schadensersatz", False),
          (beim("c8", "bei"), 2, "bei Unkenntnis des Vertreters nur Vertrauensschaden (§ 179 Abs. 2 BGB)", False)]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfschema: Haftung des Vertreters ohne Vertretungsmacht"), 110, 90, "sch", 46)]
y = 230
for c, ebene, text, fett in REIHEN:
    x = (130, 200, 260)[ebene]
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 40 if ebene == 0 else 34, rechts=1800))
    y += {0: 88, 1: 74, 2: 66}[ebene]
assert y <= 970, y
folie([("sch", "Prüfschema"), ("c1", "Prüfschema › I. Silja gegen Enno"), ("c2", "Prüfschema › I. kein Vertrag"),
       ("c3", "Prüfschema › II. Silja gegen Kuno, § 179 Abs. 1 BGB"), ("c4", "Prüfschema › II. 1. Vertrag als Vertreter"),
       ("c5", "Prüfschema › II. 2. ohne Vertretungsmacht"), ("c6", "Prüfschema › II. 3. Genehmigung verweigert"),
       ("c7", "Prüfschema › II. 4. kein Ausschluss"), ("c8", "Prüfschema › II. 5. Rechtsfolge")], els_sch)

# ===========================================================================================================================
# N Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Wer ohne Vertretungsmacht", 0)], [("im fremden Namen einen Vertrag", 0)], [("schließt, ", 0), ("haftet selbst", "a"), (",", 0)],
                 [("wenn der Vertretene die", 0)], [("Genehmigung verweigert.", 0)]], 750, 270, 44, "merke",
                {"a": beim("merke", "haftet")}),
    *markertext([[("Kannte er den Mangel, haftet er", 0)], [("auf das volle ", 0), ("Erfüllungsinteresse", "b"), (".", 0)]],
                750, 690, 44, "mk2", {"b": beim("mk2", "Erfüllungsinteresse")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
