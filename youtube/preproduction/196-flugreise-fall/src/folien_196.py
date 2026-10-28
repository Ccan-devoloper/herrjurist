"""Folge 196 · Flugreise-Fall: Der Minderjährige, der ohne Ticket mitflog (§ 812 BGB) – Serienstandard Open Peeps (Katzenkönig).
Historischer Sachverhalt BGHZ 55, 128 (1968, Urteil 7.1.1971) mit erfundenen Namen: Till (17) fliegt mit gültigem Ticket bis zu
einer Zwischenlandung, steigt mit den Transitpassagieren wieder ein und fliegt ohne Ticket weiter nach New York; Einreise
verweigert (nur als Text), Stationsleiter Ruprecht fliegt ihn zurück; Rechnung für den Hinflug 1.188 DM, die Mutter genehmigt
nichts. Szenen laut ../SZENENPLAN.md.
DARSTELLUNG: Flugzeug als Icon, Fluggesellschaft ohne Namen und Logo, keine Flughäfen; Einreiseverweigerung nur als Pille.
Zwei Handlungsgeräusche (Schritte beim Wiedereinsteigen, Flugzeug beim Weiterflug; ../geraeusche_herkunft.json).
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz
als eigene Kopie aus Folge 193 (gemeinsame Dateien unverändert); neu: boden_(), treppe(), fenster().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_196/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_196/" in n:
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
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 04.10.2026), als Zitat mit Normangabe;
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 124/149) ------------------------------------
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




X1, X2 = 1430, 1730                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"TI": "Till", "RU": "Ruprecht", "MU": "Mutter"}
NFARBE = {"TI": BLAU, "RU": GRUEN, "MU": LILA}


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
    """Zwei Figuren rechts neben der Tafel (blicken nach links zur Tafel)."""
    return [*stehend(k1, X1, folge1), *stehend(k2, X2, folge2)]


# --- eigene Szenenbausteine (programmatisch, Palettenflächen, Tuschekontur) ---------------------------------------------------
HELLBLAU = (214, 230, 252, 255)
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


def treppe(x0, unten, c, stufen=6, sb=46, sh=34, bis=None):
    """Fluggasttreppe in Seitenansicht (Grundformen): Stufen steigen nach links zur Flugzeugtür."""
    w, h = stufen * sb + 20, stufen * sh + 20
    im = Image.new("RGBA", (w, h))
    dr = ImageDraw.Draw(im)
    pts = [(w - 10, h - 4)]
    for i in range(stufen):
        x = w - 10 - i * sb
        y = h - 4 - (i + 1) * sh
        pts += [(x, y + sh), (x, y)] if i == 0 else [(x, y + sh), (x, y)]
        pts += [(x - sb, y)]
    dr.polygon(pts + [(pts[-1][0], h - 4)], fill=HELLGRAU_)
    dr.line(pts, fill=INK, width=5, joint="curve")
    dr.line((pts[-1][0], pts[-1][1], pts[-1][0], h - 4), fill=INK, width=5)
    dr.line((pts[0][0], h - 4, pts[-1][0], h - 4), fill=INK, width=5)
    return bis_(El(im, x0, unten - h + 4, c, "cut", 0.0, bis, name="treppe"), bis)


HELLGRAU_ = (226, 226, 222, 255)


def fenster(x, y, n, c, abstand=150):
    """Kabinenwand mit runden Fenstern (Grundformen)."""
    w = n * abstand + 40
    im = Image.new("RGBA", (w, 120))
    dr = ImageDraw.Draw(im)
    dr.rounded_rectangle((0, 0, w - 1, 119), 30, fill=(240, 236, 228, 255), outline=INK, width=5)
    for i in range(n):
        cx = 20 + abstand / 2 + i * abstand
        dr.rounded_rectangle((cx - 34, 22, cx + 34, 98), 30, fill=HELLBLAU, outline=INK, width=5)
    return El(im, x, y, c, "cut", 0.0, None, name="fenster")


# ===========================================================================================================================
# A1 Fall: Zwischenlandung, Till steigt mit den Transitpassagieren wieder ein
# ===========================================================================================================================
G0 = 900                                     # Boden der Fallszenen
FHA = 430                                    # Figurenhöhe in den Fallszenen
folie([(NULL, "Fall · 1968: Till fliegt mit Ticket"), ("transit", "Fall · Wieder eingestiegen, ohne Ticket")], [
    hart(boden_(G0, NULL)),
    hart(ficon("tabler", "plane-inflight", 560, G0 + 4, 580, NULL, fuell=BLAU, anim="cut")),
    hart(pl("1968", 70, 30, NULL, fill=GELB, size=40)),
    pl("Zwischenlandung", 560, 330, beim("till", "Zwischenlandung"), fill=WEISS, size=32, anker="m"),
    *fig("TI", 1450, G0, FHA, [(beim("till", "Till"), "froh")], bis="transit"),
    ns("Till", 1450, G0, beim("till", "Till"), BLAU, d=0.1, bis="transit"),
    pl("17 Jahre", 1450, 330, beim("till", "siebzehn"), fill=GELB, size=34, anker="m", bis="transit"),
    ficon("tabler", "ticket", 840, 190, 110, beim("till", "gültigem"), fuell=GRUEN, bis="transit"),
    pl("gültiges Ticket bis zur Zwischenlandung", 70, 110, beim("till", "gültigem"), fill=GRUEN, size=32, bis="transit"),
    # Wiedereinstieg: Till an der Treppe zur Kabine
    treppe(845, G0, "transit"),
    szene(peep_voll("TI_froh", 1260, G0, FHA, "transit", anim="cut"), "196schritte*", 0.55, 0.0),
    ns("Till", 1260, G0, "transit", BLAU),
    pl("mit den Transitpassagieren wieder eingestiegen", 70, 110, beim("transit", "Transitpassagieren"), fill=WEISS, size=32),
])

# ===========================================================================================================================
# A2 Fall: Weiterflug nach New York, ohne Ticket (in der Kabine)
# ===========================================================================================================================
folie([("ny", "Fall · Weiterflug nach New York, ohne Ticket"), ("t1", "Fall · Till: Einmal New York sehen!")], [
    boden_(G0, "ny", fill=(236, 230, 220, 255), h=100),
    fenster(60, 420, 6, "ny"),
    ficon("tabler", "armchair", 220, G0 + 4, 170, "ny", fuell=LILA, anim="cut"),
    ficon("tabler", "armchair", 470, G0 + 4, 170, "ny", fuell=LILA, anim="cut"),
    ficon("tabler", "armchair", 720, G0 + 4, 170, "ny", fuell=LILA, anim="cut"),
    szene(ficon("ph", "airplane-in-flight", 260, 250, 240, beim("ny", "weiter"), fuell=BLAU), "196flugzeug*", 0.6, 0.0),
    pl("Weiterflug nach New York", 70, 30, beim("ny", "weiter"), fill=GELB, size=34),
    ficon("tabler", "ticket-off", 640, 250, 120, beim("ny", "ohne"), fuell=HELLROT),
    pl("ohne Ticket", 640, 290, beim("ny", "ohne"), fill=HELLROT, size=32, anker="m"),
    *fig("TI", 1250, G0, FHA, [("ny", "staunt_r")], bis="t1"),
    ns("Till", 1250, G0, "ny", BLAU),
    *redet("TI_redet_r", 1250, G0, FHA, "t1", "visum"),
    blase("sprech", 900, 150, "t1", 1450, 260, inhalt=["Einmal New York sehen! Ein Ticket", "dafür hätte ich mir nie leisten können."],
          textsize=34, figur=("TI_redet_r", 1250, G0, FHA)),
])

# ===========================================================================================================================
# A3 Fall: New York, Einreise verweigert; Stationsleiter Ruprecht
# ===========================================================================================================================
TX, RX = 1020, 1560                          # Till (blickt nach rechts), Ruprecht (blickt nach links)
folie([("visum", "Fall · New York: Einreise verweigert"), ("rup", "Fall · Stationsleiter Ruprecht"),
       ("r1", "Fall · Rückflug noch am selben Tag")], [
    boden_(G0, "visum"),
    ficon("tabler", "building-skyscraper", 200, G0 + 4, 260, "visum", fuell=HELLBLAU, anim="cut"),
    ficon("tabler", "building-skyscraper", 420, G0 + 4, 200, "visum", fuell=BLAU, anim="cut"),
    pl("New York", 70, 30, "visum", fill=GELB, size=34),
    ficon("tabler", "barrier-block", 700, G0 + 4, 200, beim("visum", "Einreise"), fuell=ROT),
    pl("Einreise verweigert: kein Visum", 70, 100, beim("visum", "Einreise"), fill=HELLROT, size=34),
    *fig("TI", TX, G0, FHA, [("visum", "schreck_r"), ("rup", "sorge_r"), ("r1", "muede_r")]),
    ns("Till", TX, G0, "visum", BLAU),
    *fig("RU", RX, G0, FHA, [(beim("rup", "Stationsleiter"), "ruhig")], bis="r1"),
    ns("Ruprecht", RX, G0, beim("rup", "Stationsleiter"), GRUEN, d=0.1),
    pl("Stationsleiter der Fluggesellschaft", 70, 170, beim("rup", "Stationsleiter"), fill=GRUEN, size=32),
    *redet("RU_redet", RX, G0, FHA, "r1", "forder"),
    blase("sprech", 820, 150, "r1", 1350, 290, inhalt=["Ohne Visum geht es nicht weiter.", "Wir fliegen Sie noch heute zurück."],
          textsize=34, figur=("RU_redet", RX, G0, FHA)),
    ficon("tabler", "plane-departure", 860, 330, 130, beim("r1", "zurück"), fuell=BLAU),
])

# ===========================================================================================================================
# A4 Fall: zurück in Deutschland – die Rechnung, die Mutter, die Frage
# ===========================================================================================================================
TX2, MX = 1080, 1580
folie([("forder", "Fall · Die Rechnung: 1.188 DM"), ("mutter", "Fall · Die Mutter genehmigt nichts"),
       ("t2", "Fall · Till: nichts gespart"), ("frage", "Fall · Die Frage"), ("klass", "Fall · Der Flugreise-Fall")], [
    boden_(G0, "forder"),
    ficon("tabler", "home", 250, G0 + 4, 300, "forder", fuell=GELB, anim="cut"),
    pl("Zurück in Deutschland", 70, 30, "forder", fill=WEISS, size=34),
    ficon("tabler", "receipt", 640, 640, 130, beim("forder", "Preis"), fuell=WEISS),
    pl("Preis für den Hinflug: 1.188 DM", 640, 690, beim("forder", "tausendeinhundertachtundachtzig"), fill=GELB, size=30, anker="m"),
    *fig("TI", TX2, G0, FHA, [("forder", "sorge_r"), ("mutter", "still_r")], bis="t2"),
    ns("Till", TX2, G0, "forder", BLAU),
    *fig("MU", MX, G0, FHA, [(beim("mutter", "Mutter"), "ernst"), ("t2", "denkt"), ("frage", "ernst")]),
    ns("Mutter", MX, G0, beim("mutter", "Mutter"), LILA, d=0.1),
    pl("genehmigt nichts", MX, 330, beim("mutter", "genehmigt"), fill=HELLROT, size=32, anker="m", bis="t2"),
    *redet("TI_klagt_r", TX2, G0, FHA, "t2", "frage"),
    blase("sprech", 880, 160, "t2", 960, 250, inhalt=["Ich habe doch nichts gespart! Ohne den", "Gratisflug wäre ich nie geflogen."],
          textsize=34, figur=("TI_klagt_r", TX2, G0, FHA), bis="frage"),
    *fig("TI", TX2, G0, FHA, [("frage", "denkt_r"), ("klass", "ernst_r")], erst="cut"),
    pl("Muss Till den Flug bezahlen?", 70, 100, "frage", fill=PINK, size=34),
    pl("Der Flugreise-Fall des BGH", 70, 170, beim("klass", "Flugreise-Fall"), fill=GELB, size=32),
    zit("BGH, Urt. v. 7.1.1971 – VII ZR 9/70, BGHZ 55, 128", 80, 238, beim("klass2", "entschieden")),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_196(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=35, zeilenabstand=1.3)
        els += e; y += 14
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_196("sv", [
    "1968: Der 17-jährige Till fliegt mit gültigem Ticket bis zu einer Zwischenlandung. Dort steigt er mit den "
    "Transitpassagieren wieder ein und fliegt ohne Ticket weiter nach New York. Er weiß, dass er für den Weiterflug kein "
    "Ticket hat. Die Maschine ist nicht ausgebucht.",
    "In New York wird ihm die Einreise verweigert, weil er kein Visum hat. Die Fluggesellschaft fliegt ihn noch am selben Tag "
    "zurück.",
    "Sie verlangt von Till den Preis für den Hinflug: 1.188 DM. Seine Mutter genehmigt keine Verträge ihres Sohnes mit der "
    "Fluggesellschaft. Till sagt: „Ich habe doch nichts gespart! Ohne den Gratisflug wäre ich nie geflogen.“",
], "Muss Till den Hinflug nach New York bezahlen?")

# ===========================================================================================================================
# C Kein Vertrag, kein Schaden
# ===========================================================================================================================
PV = "Vertrag? Schadensersatz?"
folie([("vertrag", "Vertrag?"), ("minder", "Vertrag? › minderjährig, § 107 BGB"), ("genehm", "Vertrag? › Genehmigung verweigert, § 108 BGB"),
       ("sozial", "Vertrag? › durch bloßes Einsteigen?"), ("delikt", "Schadensersatz? › kein Schaden"),
       ("bleibt", "Bleibt: Bereicherungsrecht")], rechts_frei([
    *tafel("vertrag", PV),
    z("Till: minderjährig; Beförderungsvertrag nicht", 110, 180, "minder", "Bold", 32),
    z("lediglich rechtlich vorteilhaft (§ 107 BGB)", 110, 225, beim("minder", "lediglich"), "Bold", 32),
    *neinz("Mutter verweigert die Genehmigung (§ 108 Abs. 1 BGB)", 300, beim("genehm", "verweigert"), "Bold", 31, x=160),
    zit("mehr dazu: Video „Geschäftsfähigkeit“", 160, 350, beim("genehm", "mehr")),
    *neinz("Vertrag durch bloßes Einsteigen: vom BGH abgelehnt", 420, beim("sozial", "lehnte"), "Bold", 31, x=160),
    z("Flugverkehr: jeder Fluggast namentlich erfasst", 160, 468, beim("sozial", "Flugverkehr"), size=30),
    *neinz("Schadensersatz: Maschine nicht ausgebucht,", 545, beim("delikt", "Maschine"), "Bold", 31, x=160),
    z("kein Schaden dargelegt", 160, 593, beim("delikt", "Schaden", 2), "Bold", 31),
    blk(110, 670, 1040, 80, GRUEN, "bleibt", [("Bleibt: das Bereicherungsrecht", "ExtraBold", 34, INK)]),
    zit("BGH, Urt. v. 7.1.1971 – VII ZR 9/70, BGHZ 55, 128", 110, 770, "bleibt"),
    *requisit([("vertrag", ("tabler", "file-text", 100, WEISS), "Vertrag?", WEISS),
               (beim("delikt", "Maschine"), ("ph", "airplane", 130, BLAU), "Maschine nicht ausgebucht", WEISS),
               ("bleibt", ("tabler", "scale", 110, WEISS), "Bereicherungsrecht", GRUEN)]),
    *zwei("TI", [("vertrag", "ruhig"), ("genehm", "sorge"), ("bleibt", "denkt")],
          "MU", [("vertrag", "ruhig"), ("genehm", "ernst"), ("sozial", "denkt")]),
]))

# ===========================================================================================================================
# D Wortlautkarte § 812 Abs. 1 Satz 1 BGB
# ===========================================================================================================================
W812 = umbruch("„Wer durch die Leistung eines anderen oder in sonstiger Weise auf dessen Kosten etwas ohne rechtlichen Grund "
               "erlangt, ist ihm zur Herausgabe verpflichtet.“", 32, 1040)
_z8 = lambda wort: next(i for i, t in enumerate(W812) if wort in t)
w812, w812_y = wortlaut(80, 170, 1100, W812, "§ 812 Abs. 1 Satz 1 BGB", "norm",
                        marken=[(_z8("Leistung"), "Leistung", beim("w1", "Leistung")),
                                (_z8("sonstiger"), "sonstiger", beim("w1", "sonstiger")),
                                (_z8("ohne"), "ohne", beim("w1", "ohne"))], size=32)
PN = "Anspruch: § 812 Abs. 1 Satz 1 BGB"
folie([("norm", PN), ("leist", f"{PN} › Leistung?"), ("nleist", f"{PN} › keine Leistung"),
       ("sonst", f"{PN} Alt. 2 › Eingriffskondiktion"), ("ogrund", f"{PN} Alt. 2 › ohne rechtlichen Grund")], rechts_frei([
    *tafel("norm", "Die Norm: § 812 Abs. 1 Satz 1 BGB"),
    *w812,
    z("Leistung: bewusste und zweckgerichtete", 110, w812_y + 25, "leist", "Bold", 31),
    z("Vermehrung fremden Vermögens", 110, w812_y + 68, beim("leist", "Vermehrung"), "Bold", 31),
    zit("BGH, Urt. v. 31.1.2018 – VIII ZR 39/17, Rn. 17", 110, w812_y + 112, beim("leist", "Vermehrung")),
    *neinz("Fluggesellschaft wollte Till nicht befördern", w812_y + 170, "nleist", "Bold", 31, x=160),
    *okz("in sonstiger Weise auf ihre Kosten verschafft", w812_y + 235, "sonst", "Bold", 31, x=160),
    blk(110, w812_y + 295, 1040, 76, GELB, beim("sonst", "Eingriffskondiktion"), [("Eingriffskondiktion (Alt. 2)", "ExtraBold", 32, INK)]),
    z("BGH: Art der Kondiktion nicht festgelegt", 110, w812_y + 392, "offen", "Bold", 29, farbe=TEXT),
    *okz("kein rechtlicher Grund", w812_y + 445, "ogrund", "Bold", 32, x=160),
    *requisit([("norm", ("tabler", "book", 100, WEISS), "§ 812 BGB", GELB),
               ("nleist", ("tabler", "ticket-off", 110, HELLROT), "keine Leistung", HELLROT),
               ("sonst", ("tabler", "plane", 130, BLAU), "Beförderung verschafft", WEISS)]),
    *zwei("TI", [("norm", "ruhig"), ("nleist", "still"), ("ogrund", "sorge")],
          "RU", [("norm", "ernst"), ("sonst", "denkt"), ("ogrund", "ernst")]),
]))
assert w812_y + 500 <= 930, w812_y

# ===========================================================================================================================
# E Was ist erlangt? (Meinungsstand)
# ===========================================================================================================================
PE = "Etwas erlangt?"
folie([("erl", PE), ("ma", f"{PE} › Ansicht 1: die Beförderung selbst"), ("mb", f"{PE} › Ansicht 2: ersparte Aufwendungen"),
       ("bg1", f"{PE} › BGH: echte Vermögensvermehrung"), ("bg2", f"{PE} › BGH: erlangte Beförderung, Ersparnis bei § 818 Abs. 3")],
      rechts_frei([
    *tafel("erl", "Was hat Till erlangt?"),
    blk(110, 180, 505, 190, HELLBLAU, "ma", [("Ansicht 1:", "Bold", 30, INK), ("die Beförderung", "ExtraBold", 32, INK),
                                          ("selbst", "ExtraBold", 32, INK)]),
    blk(645, 180, 505, 190, LILA, "mb", [("Ansicht 2:", "Bold", 30, INK), ("nur ersparte", "ExtraBold", 32, INK),
                                      ("Aufwendungen", "ExtraBold", 32, INK)]),
    *neinz("erspart: nichts", 390, beim("mb", "erspart"), "Bold", 30, x=700),
    z("BGH: grundsätzlich echte Vermögensvermehrung", 110, 475, "bg1", "Bold", 32),
    zit("BGHZ 55, 128, 131; BGH, Urt. v. 7.3.2013 – III ZR 231/12, Rn. 27", 110, 520, "bg1"),
    *okz("im Ergebnis: die erlangte Beförderung", 590, beim("bg2", "Ergebnis"), "Bold", 32, x=160),
    z("Ersparnis prüft er wie den Wegfall der", 160, 645, beim("bg2", "prüft"), size=31),
    z("Bereicherung: bei § 818 Abs. 3 BGB", 160, 690, beim("bg2", "Paragraf"), size=31),
    zit("BGHZ 55, 128, 132–135; BGH, Urt. v. 21.2.2022 – VIa ZR 8/21, Rn. 88, 95", 110, 760, beim("bg2", "Paragraf")),
    *requisit([("erl", ("tabler", "plane", 130, BLAU), "erlangt?", WEISS),
               (beim("mb", "erspart"), ("tabler", "coins", 110, GELB), "nichts erspart", HELLROT),
               ("bg2", ("tabler", "plane", 130, BLAU), "die Beförderung", GRUEN)]),
    *zwei("TI", [("erl", "denkt"), ("mb", "froh"), ("bg2", "sorge")], "RU", [("erl", "ernst"), ("ma", "denkt"), ("bg2", "ernst")]),
]))

# ===========================================================================================================================
# F Wortlautkarte § 818 Abs. 2, 3 BGB
# ===========================================================================================================================
W818 = (umbruch("„(2) Ist die Herausgabe wegen der Beschaffenheit des Erlangten nicht möglich …, so hat er den Wert zu "
                "ersetzen.", 32, 1040) +
        umbruch("(3) Die Verpflichtung zur Herausgabe oder zum Ersatz des Wertes ist ausgeschlossen, soweit der Empfänger "
                "nicht mehr bereichert ist.“", 32, 1040))
_z18 = lambda wort: next(i for i, t in enumerate(W818) if wort in t)
w818, w818_y = wortlaut(80, 170, 1100, W818, "§ 818 Abs. 2, 3 BGB (Auslassung: …)", "w2",
                        marken=[(_z18("Wert zu"), "Wert", beim("w2", "Wert")),
                                (_z18("bereichert"), "nicht mehr bereichert", beim("w3", "nicht", 1))], size=32)
PW = "Umfang › Wertersatz"
folie([("w2", f"{PW}, § 818 Abs. 2 BGB"), ("wert", f"{PW}: übliche Vergütung"), ("w3", "Umfang › Entreicherung, § 818 Abs. 3 BGB"),
       ("lux", "Umfang › Entreicherung: Luxus?"), ("lux2", "Umfang › Entreicherung: nur gutgläubig")], rechts_frei([
    *tafel("w2", "Wertersatz und Entreicherung"),
    *w818,
    *okz("Wert = übliche Vergütung für den Flug", w818_y + 30, beim("wert", "übliche"), "Bold", 32, x=160),
    z("Luxus, den man sich sonst nie geleistet hätte:", 110, w818_y + 110, "lux", "Bold", 31),
    z("Entreicherung möglich", 110, w818_y + 155, beim("lux", "Entreicherung"), "Bold", 31),
    zit("BGH, Urt. v. 27.10.2016 – IX ZR 160/14, Rn. 21 („Luxusausgaben“)", 110, w818_y + 200, beim("lux", "Entreicherung")),
    blk(110, w818_y + 250, 1040, 76, GELB, "lux2", [("aber nur beim gutgläubigen Empfänger", "ExtraBold", 32, INK)]),
    *requisit([("w2", ("tabler", "plane", 130, BLAU), "Flug: nicht herausgebbar", WEISS),
               ("wert", ("tabler", "coins", 110, GELB), "übliche Vergütung", GELB),
               ("lux", ("tabler", "gift", 110, PINK), "Luxus?", WEISS)]),
    *zwei("TI", [("w2", "ruhig"), ("lux", "froh"), ("lux2", "denkt")], "RU", [("w2", "ernst"), ("lux", "denkt"), ("lux2", "ernst")]),
]))
assert w818_y + 340 <= 930, w818_y

# ===========================================================================================================================
# G Wortlautkarte § 819 Abs. 1 BGB
# ===========================================================================================================================
W819 = umbruch("„Kennt der Empfänger den Mangel des rechtlichen Grundes bei dem Empfang oder erfährt er ihn später, so ist er "
               "von dem Empfang oder der Erlangung der Kenntnis an zur Herausgabe verpflichtet, wie wenn der Anspruch auf "
               "Herausgabe zu dieser Zeit rechtshängig geworden wäre.“", 32, 1040)
_z19 = lambda wort: next(i for i, t in enumerate(W819) if wort in t)
w819, w819_y = wortlaut(80, 170, 1100, W819, "§ 819 Abs. 1 BGB", "w819",
                        marken=[(_z19("Kennt"), "Kennt", beim("w819", "Kennt")),
                                (_z19("rechtshängig"), "rechtshängig", beim("w819", "rechtshängig"))], size=32)
PK = "Verschärfte Haftung: § 819 Abs. 1 BGB"
folie([("w819", PK), ("r4", f"{PK} › § 818 Abs. 4 BGB"), ("als", f"{PK} › BGH: als hätte er erspart"),
       ("kennt", f"{PK} › Till kannte den Mangel"), ("aber", f"{PK} › Till ist 17: wessen Kenntnis?")], rechts_frei([
    *tafel("w819", "Verschärfte Haftung"),
    *w819,
    z("§ 818 Abs. 4 BGB: Haftung nach den allgemeinen Vorschriften", 110, w819_y + 25, "r4", "Bold", 30),
    *neinz("die Entreicherung hilft ihm nicht", w819_y + 80, beim("r4", "Entreicherung"), "Bold", 31, x=160),
    z("BGH: so behandelt, als hätte er etwas erspart", 110, w819_y + 150, "als", "Bold", 31),
    zit("BGHZ 55, 128, 134 f.; BGH, Urt. v. 21.2.2022 – VIa ZR 8/21, Rn. 95", 110, w819_y + 195, "als"),
    *okz("Till wusste: kein Ticket", w819_y + 255, "kennt", "Bold", 32, x=160),
    blk(110, w819_y + 320, 1040, 76, PINK, "aber", [("Aber: 17 Jahre alt. Wessen Kenntnis zählt?", "ExtraBold", 32, INK)]),
    *requisit([("w819", ("tabler", "book", 100, WEISS), "§ 819 Abs. 1 BGB", GELB),
               ("kennt", ("tabler", "ticket-off", 110, HELLROT), "wusste: kein Ticket", HELLROT),
               ("aber", ("tabler", "users", 110, LILA), "wessen Kenntnis?", PINK)]),
    *zwei("TI", [("w819", "ruhig"), ("r4", "schreck"), ("kennt", "still"), ("aber", "denkt")],
          "RU", [("w819", "ernst"), ("als", "denkt"), ("aber", "ernst")]),
]))
assert w819_y + 410 <= 930, w819_y

# ===========================================================================================================================
# H Wessen Kenntnis? Meinungsstand und BGH
# ===========================================================================================================================
PM = "§ 819 Abs. 1 › Kenntnis des Minderjährigen"
folie([("mst", f"{PM}: Meinungsstand"), ("s1", f"{PM} › Ansicht 1: Eltern"), ("s2", f"{PM} › Ansicht 2: Deliktsregeln"),
       ("s3", f"{PM} › Ansicht 3: unterscheiden"), ("b1", f"{PM} › BGH: Schutzzweck – Eltern"),
       ("b2", f"{PM} › BGH: vorsätzliche unerlaubte Handlung – eigene"), ("b3", f"{PM} › hier: § 265a StGB")], rechts_frei([
    *tafel("mst", "Wessen Kenntnis zählt?"),
    z("Ansicht 1: immer die Kenntnis der Eltern", 110, 175, "s1", "Bold", 31),
    z("Ansicht 2: Deliktsregeln entsprechend –", 110, 222, "s2", "Bold", 31),
    z("Einsicht des Minderjährigen", 300, 264, beim("s2", "Einsicht"), size=30),
    z("Ansicht 3: Leistungskondiktion – Eltern;", 110, 311, "s3", "Bold", 31),
    z("Eingriffskondiktion – Deliktsregeln", 300, 353, beim("s3", "Eingriffskondiktion"), size=30),
    blk(110, 415, 1040, 130, HELLBLAU, "b1", [("BGH: wo der Minderjährigenschutz es verlangt,", "Bold", 30, INK),
                                           ("v. a. Rückabwicklung seiner Verträge: Eltern", "ExtraBold", 31, INK)]),
    blk(110, 565, 1040, 130, HELLGRUEN, "b2", [("Erlangtes durch vorsätzliche unerlaubte Handlung", "Bold", 30, INK),
                                            ("verschafft: seine eigene Kenntnis", "ExtraBold", 31, INK)]),
    *okz("hier: Erschleichen der Beförderung, § 265a StGB", 720, "b3", "Bold", 31, x=160),
    zit("BGHZ 55, 128, 136 f.; BGH, Beschl. v. 20.1.2021 – GSSt 2/20, Rn. 23", 110, 780, "b3"),
    *requisit([("mst", ("tabler", "users", 110, LILA), "Meinungsstand", WEISS),
               ("b1", ("tabler", "file-text", 100, WEISS), "Verträge: Eltern", HELLBLAU),
               ("b2", ("tabler", "ticket-off", 110, HELLROT), "erschlichen: eigene", HELLGRUEN)]),
    *zwei("TI", [("mst", "denkt"), ("b2", "sorge")], "MU", [("mst", "ernst"), ("s1", "denkt"), ("b1", "ernst"), ("b2", "still")]),
]))

# ===========================================================================================================================
# I Wortlautkarte § 828 Abs. 3 BGB (analog)
# ===========================================================================================================================
W828 = umbruch("„Wer das 18. Lebensjahr noch nicht vollendet hat, ist, sofern seine Verantwortlichkeit nicht nach Absatz 1 "
               "oder 2 ausgeschlossen ist, für den Schaden, den er einem anderen zufügt, nicht verantwortlich, wenn er bei der "
               "Begehung der schädigenden Handlung nicht die zur Erkenntnis der Verantwortlichkeit erforderliche Einsicht "
               "hat.“", 32, 1040)
_z28 = lambda wort: next(i for i, t in enumerate(W828) if wort in t)
w828, w828_y = wortlaut(80, 170, 1100, W828, "§ 828 Abs. 3 BGB (hier entsprechend)", "w828",
                        marken=[(_z28("18. Lebensjahr"), "18. Lebensjahr", beim("w828b", "achtzehnte")),
                                (_z28("Einsicht"), "Einsicht", beim("w828b", "Einsicht"))], size=32)
PE3 = "Einsichtsfähigkeit: § 828 Abs. 3 BGB analog"
folie([("w828", PE3), ("damals", f"{PE3} › 1971: § 828 Abs. 2 a. F."), ("ein", f"{PE3} › fast 18, mit Ticket geflogen"),
       ("ein2", f"{PE3} › Einsicht (+)")], rechts_frei([
    *tafel("w828", "Maßstab: § 828 Abs. 3 BGB analog"),
    *w828,
    z("1971 stand die Regel noch in § 828 Abs. 2 BGB", 110, w828_y + 25, "damals", "Bold", 30, farbe=TEXT),
    *okz("Till: fast 18, gerade erst mit Ticket geflogen", w828_y + 95, "ein", "Bold", 32, x=160),
    blk(110, w828_y + 165, 1040, 80, GRUEN, "ein2", [("Einsicht: ohne Ticket kein Weiterflug", "ExtraBold", 33, INK)]),
    *requisit([("w828", ("tabler", "book", 100, WEISS), "§ 828 Abs. 3 BGB", GELB),
               ("ein", ("tabler", "ticket", 110, GRUEN), "fast 18", GELB)]),
    *stehend("TI", FX, [("w828", "ruhig"), ("ein", "still"), ("ein2", "muede")]),
]))
assert w828_y + 260 <= 930, w828_y

# ===========================================================================================================================
# J Ergebnis
# ===========================================================================================================================
folie([("erg", "Ergebnis · Till haftet verschärft"), ("erg2", "Ergebnis › Wertersatz: üblicher Flugpreis"),
       ("erg3", "Ergebnis › keine Entreicherung"), ("rueck", "Ergebnis › Rückflug: Geschäftsführung ohne Auftrag")], rechts_frei([
    *tafel("erg", "Ergebnis"),
    blk(110, 180, 1040, 80, GRUEN, "erg", [("Till haftet verschärft", "ExtraBold", 36, INK)]),
    *okz("Wertersatz: der übliche Flugpreis", 310, beim("erg2", "Wert"), "Bold", 32, x=160),
    z("§§ 812 Abs. 1 Satz 1, 818 Abs. 2 und 4, 819 Abs. 1 BGB", 160, 357, beim("erg2", "Flugpreis"), size=29),
    *neinz("keine Berufung auf die Entreicherung", 425, "erg3", "Bold", 32, x=160),
    z("Rückflug: Geschäftsführung ohne Auftrag", 110, 520, "rueck", "Bold", 32),
    z("(§§ 677, 683, 670 BGB)", 110, 565, beim("rueck", "Geschäftsführung"), size=30),
    zit("BGH, Beschl. v. 27.11.2014 – III ZA 19/14, Rn. 6 (zu NJW 1971, 609, 612)", 110, 625, beim("rueck", "Geschäftsführung")),
    *requisit([("erg", ("tabler", "gavel", 100, HOLZ), "Ergebnis", WEISS),
               ("erg2", ("tabler", "coins", 110, GELB), "üblicher Flugpreis", GELB),
               ("rueck", ("tabler", "plane-arrival", 130, BLAU), "Rückflug", WEISS)]),
    *zwei("TI", [("erg", "muede"), ("rueck", "still")], "RU", [("erg", "ruhig"), ("erg2", "froh"), ("rueck", "ernst")]),
]))

# ===========================================================================================================================
# K Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · zwei Wertungen"), ("tp2", "Klausurtipp · Schutz: Eltern"),
       ("tp3", "Klausurtipp · deliktsähnlich: eigene Einsicht"), ("tp4", "Klausurtipp · bei § 819 BGB entscheiden")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Minderjährige im Bereicherungsrecht:", 200, 200, beim("tipp", "Minderjährigen"), "Bold", 36),
    z("zwei Wertungen stoßen aufeinander", 200, 260, beim("tipp", "zwei"), size=34),
    z("Schutz des Minderjährigen:", 200, 345, "tp2", "Bold", 36),
    z("Kenntnis der Eltern", 200, 400, beim("tp2", "Kenntnis"), size=34),
    z("deliktsähnliches Verhalten:", 200, 480, "tp3", "Bold", 36),
    z("eigene Einsicht", 200, 535, beim("tp3", "eigene"), size=34),
    linienzug([(130, 610), (1130, 610)], "tp4", breite=3),
    z("bei § 819 BGB entscheiden – und begründen", 200, 640, "tp4", "Bold", 36),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# L Prüfschema
# ===========================================================================================================================
REIHEN = [("c1", 0, "I. Anspruch aus § 812 Abs. 1 Satz 1 Alt. 2 BGB", True),
          ("c2", 1, "1. etwas erlangt: die Beförderung", False),
          ("c3", 1, "2. in sonstiger Weise auf Kosten der Fluggesellschaft", False),
          ("c4", 1, "3. ohne rechtlichen Grund: kein Vertrag (§§ 107, 108 BGB)", False),
          ("c5", 0, "II. Umfang", True),
          ("c6", 1, "1. Wertersatz, § 818 Abs. 2 BGB", False),
          ("c7", 1, "2. Entreicherung, § 818 Abs. 3 BGB?", False),
          ("c8", 1, "3. verschärfte Haftung, § 819 Abs. 1 BGB: Wessen Kenntnis zählt?", False)]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfschema: Flugreise-Fall"), 110, 90, "sch", 46)]
y = 250
for c, ebene, text, fett in REIHEN:
    x = (130, 200)[ebene]
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 40 if ebene == 0 else 34, rechts=1800))
    y += {0: 85, 1: 72}[ebene]
assert y <= 970, y
folie([("sch", "Prüfschema"), ("c1", "Prüfschema › I. § 812 Abs. 1 Satz 1 Alt. 2 BGB"), ("c2", "Prüfschema › I. 1. etwas erlangt"),
       ("c3", "Prüfschema › I. 2. in sonstiger Weise"), ("c4", "Prüfschema › I. 3. ohne rechtlichen Grund"),
       ("c5", "Prüfschema › II. Umfang"), ("c6", "Prüfschema › II. 1. Wertersatz"), ("c7", "Prüfschema › II. 2. Entreicherung"),
       ("c8", "Prüfschema › II. 3. verschärfte Haftung")], els_sch)

# ===========================================================================================================================
# M Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Hat sich ein Minderjähriger das Erlangte", 0)], [("durch eine ", 0), ("vorsätzliche", "a"), (" unerlaubte", 0)],
                 [("Handlung verschafft, zählt bei § 819 BGB", 0)], [("seine eigene Kenntnis,", 0)],
                 [("wenn er die nötige Einsicht hat.", 0)]], 750, 260, 42, "merke",
                {"a": beim("merke", "vorsätzliche")}),
    *markertext([[("Dann hilft ihm die ", 0), ("Entreicherung", "b"), (" nicht.", 0)]],
                750, 700, 42, "mk2", {"b": beim("mk2", "Entreicherung")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
