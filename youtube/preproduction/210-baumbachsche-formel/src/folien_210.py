"""Folge 210 · Baumbachsche Kostenformel: Schritt für Schritt mit Tabelle – Serienstandard Open Peeps (Katzenkönig).
Beispielfall: Frau Eschenbach verklagt Herrn Lohmann und Frau Kreutzer (Fahrradladen) als Gesamtschuldner auf 20.000 €
Darlehen; Herr Lohmann (Beklagter zu 1) verliert voll, die Klage gegen Frau Kreutzer (Beklagte zu 2) wird abgewiesen.
Szenen laut ../SZENENPLAN.md: A Fahrradladen, B Landgericht (Akte, Hauptsachetenor des Richters, Frage), C Sachverhalt,
D Problem (zwei Prozessrechtsverhältnisse, Wortlaut § 61), E § 100 ZPO (Wortlaut Abs. 1 und 4), F Grundgedanke und
fiktiver Streitwert, G Tabelle Schritt für Schritt mit Probe, H Kostentenor, I Klausurtipp (Lexi), J Schema, K Merksatz (Lexi).
Handlungsgeräusche: Ladenglocke, als Frau Eschenbach den Laden betritt (A); Akte landet auf dem Richtertisch (B);
../geraeusche_herkunft.json.
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz
als eigene Kopie aus Folge 195 (gemeinsame Dateien unverändert); neu: zelle(), linie().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut nach gesetze-im-internet.de (ZPO), Abruf 06.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave
import datetime as _dt

bausteine.FIGORDNER = "op_210/"

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
BEIGE = (201, 166, 107, 255)
ROSE = (242, 167, 195, 255)
FELD1 = (246, 232, 170, 255)
FELD2 = (205, 232, 190, 255)
FELD3 = (176, 218, 160, 255)
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
        if n.startswith(("bild:", "ficon:")) or "/op_210/" in n:
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
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 06.10.2026), als Zitat mit Normangabe; der
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
    return [bis_(ok(x - 45, y + 20, cue, gr=gr), k.get("bis")), z(text, x, y, cue, stil, size, **k)]


def neinz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Kreuz davor (zur gesprochenen Verneinung)."""
    return [bis_(nein(x - 45, y + 20, cue, gr=gr), k.get("bis")), z(text, x, y, cue, stil, size, **k)]


# --- eigene Szenenbausteine (programmatisch, Palettenflächen, Tuschekontur) ---------------------------------------------------
BODEN_Y = 905                                # Boden = Unterkante der Figuren in den Fallszenen
FHA = 470                                    # Figurenhöhe in den Fallszenen
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
WAND = (232, 240, 238, 255)
WAND2 = (242, 232, 214, 255)
GRAUW = (205, 205, 200, 255)


def _flaeche(w, h, zeichne):
    s = 2
    im = Image.new("RGBA", (w * s, h * s))
    zeichne(ImageDraw.Draw(im), s)
    return im.resize((w, h), Image.LANCZOS)


def boden(c, x0=60, x1=1860):
    return hart(linienzug([(x0, BODEN_Y), (x1, BODEN_Y)], c, breite=7, farbe=INK))




def schreibtisch(c, x0, x1, h=170):
    w = x1 - x0
    def zz(dr, s):
        dr.rounded_rectangle((3 * s, 0, (w - 3) * s, 28 * s), 6 * s, fill=HOLZ, outline=INK, width=5 * s)
        for xl in (30, w - 60):
            dr.rectangle((xl * s, 28 * s, (xl + 26) * s, (h - 3) * s), fill=HOLZ, outline=INK, width=4 * s)
    return hart(El(_flaeche(w, h, zz), x0, BODEN_Y - h, c, "cut", 0.0, None, name="schreibtisch"))


def fenster(c, x0, y0, w=300, h=260):
    def zz(dr, s):
        dr.rounded_rectangle((3 * s, 3 * s, (w - 3) * s, (h - 3) * s), 10 * s, fill=(214, 232, 250, 255), outline=INK, width=5 * s)
        dr.line((w // 2 * s, 3 * s, w // 2 * s, (h - 3) * s), fill=INK, width=4 * s)
        dr.line((3 * s, h // 2 * s, (w - 3) * s, h // 2 * s), fill=INK, width=4 * s)
    return hart(El(_flaeche(w, h, zz), x0, y0, c, "cut", 0.0, None, name="fenster"))


X1, X2 = 1395, 1730                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"ES": "Frau Eschenbach", "LO": "Herr Lohmann", "KR": "Frau Kreutzer", "RI": "Richter"}
NFARBE = {"ES": BLAU, "LO": ORANGE, "KR": GRUEN, "RI": LILA}


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


def zwei(folge_l, folge_r, links="ES", rechts="KR"):
    """Zwei Figuren rechts neben der Tafel (blicken nach links zur Tafel)."""
    return [*stehend(links, X1, folge_l), *stehend(rechts, X2, folge_r)]


def allein(k, folge):
    return stehend(k, FX, folge)







# --- eigene Szenenbausteine Folge 210 ----------------------------------------------------------------------------------------
DUNKEL = (58, 58, 72, 255)
GRAU = (205, 205, 210, 255)


def linie(x0, y0, x1, y1, cue, breite=4, farbe=INK):
    return linienzug([(x0, y0), (x1, y1)], cue, breite=breite, farbe=farbe)


def zelle(text, cx, y, cue, size=34, stil="ExtraBold", farbe=INK, breite=150):
    """Tabellenzelle: Text mittig in der Spalte, darf die Spaltenbreite nicht überschreiten."""
    w = F(stil, size).getlength(glyphen(text))
    assert w <= breite, f"Zelle zu breit: {text} ({w:.0f} > {breite})"
    return z(text, cx - w / 2, y, cue, stil, size, farbe=farbe)


# ===========================================================================================================================
# A Fall: im Fahrradladen
# ===========================================================================================================================
LOX, KRX, ESX = 1060, 1330, 1700
RX, RY, RU = 720, 520, 480                   # Requisit links über dem Fahrrad: Mitte, Pillenhöhe, Icon-Unterkante
glocke = szene(peep_voll("ES_froh", ESX, BODEN_Y, FHA, beim("leiht", "Eschenbach"), anim="pop", bis="faellig"), "210glocke*",
               1.0, versatz=0.05)
folie([(NULL, "Fall · Der Fahrradladen"), ("leiht", "Fall · 20.000 € Darlehen"),
       ("vertrag", "Fall · Nur Herr Lohmann unterschreibt"), ("faellig", "Fall · Das Darlehen ist fällig"),
       ("es1", "Fall · Frau Eschenbach fordert"), ("kr1", "Fall · Frau Kreutzer bestreitet")], [
    boden(NULL),
    hart(ficon("tabler", "sun", 1780, 190, 100, NULL, fuell=GELB, anim="cut")),
    hart(ficon("ph", "storefront", 320, BODEN_Y + 2, 440, NULL, fuell=WEISS, nebenfarbe=BLAU, anim="cut")),
    hart(ficon("ph", "bicycle", 760, BODEN_Y, 240, NULL, fuell=ROT, anim="cut")),
    hart(pl("Fahrradladen Lohmann & Kreutzer", 70, 40, NULL, fill=GRUEN, size=36)),
    *fig("LO", LOX, BODEN_Y, FHA, [(NULL, "ruhig_r"), ("vertrag", "froh_r"), ("faellig", "skeptisch_r"), ("es1", "sorge_r"),
                                   ("kr1", "muede_r")], erst="cut"),
    hart(ns("Herr Lohmann", LOX, BODEN_Y, NULL, NFARBE["LO"])),
    *fig("KR", KRX, BODEN_Y, FHA, [(NULL, "ruhig_r"), ("vertrag", "denkt_r"), ("es1", "skeptisch_r")], erst="cut", bis="kr1"),
    *redet("KR_redet_r", KRX, BODEN_Y, FHA, "kr1", "klage"),
    hart(ns("Frau Kreutzer", KRX, BODEN_Y, NULL, NFARBE["KR"])),
    glocke,
    *fig("ES", ESX, BODEN_Y, FHA, [("faellig", "sorge"), (beim("faellig", "Cent"), "aerger")], erst="cut", bis="es1"),
    *redet("ES_redet", ESX, BODEN_Y, FHA, "es1", "kr1"),
    *fig("ES", ESX, BODEN_Y, FHA, [("kr1", "aerger")], erst="cut"),
    ns("Frau Eschenbach", ESX, BODEN_Y, beim("leiht", "Eschenbach"), NFARBE["ES"]),
    ficon("ph", "hand-coins", RX, RU, 120, beim("leiht", "zwanzigtausend"), fuell=GELB, bis="vertrag"),
    pl("Darlehen: 20.000 €", RX, RY, beim("leiht", "zwanzigtausend"), fill=GELB, size=30, anker="m", bis="vertrag"),
    ficon("ph", "signature", RX, RU, 120, beim("vertrag", "Darlehensvertrag"), fuell=WEISS, bis="faellig"),
    pl("Vertrag: nur Herr Lohmann", RX, RY, beim("vertrag", "Lohmann"), fill=WEISS, size=30, anker="m", bis="faellig"),
    pl("Geld auf sein Konto", RX, RY + 72, beim("vertrag", "Konto"), fill=BLAU, size=28, anker="m", bis="faellig"),
    ficon("ph", "calendar-x", RX, RU, 110, beim("faellig", "fällig"), fuell=WEISS, bis="kr1"),
    pl("fällig: kein Cent zurück", RX, RY, beim("faellig", "Cent"), fill=HELLROT, size=30, anker="m", bis="kr1"),
    blase("sprech", 820, 200, "es1", 1330, 210, inhalt=["Sie haben sich das Geld beide", "geliehen, also zahlen Sie", "auch beide!"],
          textsize=34, figur=("ES_redet", ESX, BODEN_Y, FHA), bis="kr1"),
    blase("sprech", 840, 200, "kr1", 1060, 210, inhalt=["Ich habe nichts unterschrieben.", "Das Darlehen hat er", "allein aufgenommen."],
          textsize=34, figur=("KR_redet_r", KRX, BODEN_Y, FHA), bis="klage"),
])

# ===========================================================================================================================
# B Fall: im Landgericht
# ===========================================================================================================================
RIX, RIU, RIH = 900, 700, 380
ESB, LOB, KRB = 300, 1310, 1690
akte = szene(bewegt(ficon("tabler", "file-text", 740, 522, 70, "klage", fuell=WEISS), "klage", ("klage", 0.35), 0, -70),
             "210akte*", 1.0, versatz=0.3)
folie([("klage", "Fall · Die Klage gegen beide"), ("beweis", "Fall · Nach der Beweisaufnahme"),
       ("ri1", "Fall · Das Urteil in der Hauptsache"), ("frage", "Fall · B1 verliert voll, B2 gewinnt komplett"),
       ("frage2", "Fall · Wer trägt welche Kosten?")], [
    boden("klage"),
    hart(pl("Landgericht · Sitzungssaal", 70, 40, "klage", fill=GRAU, size=36)),
    *fig("RI", RIX, RIU, RIH, [("klage", "ruhig")], erst="cut", bis="ri1"),
    *redet("RI_redet", RIX, RIU, RIH, "ri1", "frage"),
    *fig("RI", RIX, RIU, RIH, [("frage", "denkt")], erst="cut"),
    hart(fl_block(680, 520, 440, 200, DUNKEL, "klage", [("Gericht", "Bold", 32, WEISS)], rand=5)),
    hart(pl("Richter", RIX, 750, "klage", fill=LILA, size=28, anker="m")),
    akte,
    *fig("ES", ESB, BODEN_Y, FHA, [("klage", "ruhig_r"), (beim("beweis", "beweisen"), "sorge_r"), ("frage2", "denkt_r")], erst="cut"),
    hart(ns("Klägerin: Frau Eschenbach", ESB, BODEN_Y, "klage", NFARBE["ES"])),
    *fig("LO", LOB, BODEN_Y, FHA, [("klage", "ruhig"), ("beweis", "skeptisch"), ("ri1", "muede")], erst="cut"),
    hart(ns("Bekl. zu 1: Herr Lohmann", LOB, BODEN_Y, "klage", NFARBE["LO"])),
    *fig("KR", KRB, BODEN_Y, FHA, [("klage", "sorge"), (beim("beweis", "beweisen"), "froh"), ("frage2", "ruhig")], erst="cut"),
    hart(ns("Bekl. zu 2: Frau Kreutzer", KRB, BODEN_Y, "klage", NFARBE["KR"])),
    pl("Klage: 20.000 €", ESB + 60, 370, beim("klage", "zwanzigtausend"), fill=GELB, size=30, anker="m", bis="frage"),
    pl("beide als Gesamtschuldner", ESB + 60, 300, beim("klage", "Gesamtschuldner"), fill=WEISS, size=28, anker="m", bis="frage"),
    pl("ihre Mitverpflichtung: nicht bewiesen", KRB - 160, 360, beim("beweis", "beweisen"), fill=HELLROT, size=28, anker="m",
       bis="frage"),
    blase("sprech", 1180, 160, "ri1", 1250, 128, inhalt=["Der Beklagte zu 1 wird verurteilt, an die Klägerin",
                                                       "20.000 € zu zahlen. Im Übrigen wird die Klage abgewiesen."],
          textsize=32, figur=("RI_redet", RIX, RIU, RIH), bis="frage"),
    pl("Herr Lohmann: verliert voll", LOB - 60, 300, "frage", fill=HELLROT, size=30, anker="m"),
    pl("Frau Kreutzer: gewinnt komplett", KRB - 150, 370, beim("frage", "gewinnt"), fill=GRUEN, size=30, anker="m"),
    pl("Wer trägt welche Kosten?", 960, 140, "frage2", fill=PINK, size=38, anker="m"),
])

# ===========================================================================================================================
# C Sachverhalt
# ===========================================================================================================================
def sachverhalt_210(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=36, zeilenabstand=1.32)
        els += e; y += 16
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=30))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_210("sv", [
    "Herr Lohmann und Frau Kreutzer führen zusammen einen Fahrradladen. Frau Eschenbach überweist 20.000 Euro auf das "
    "Konto von Herrn Lohmann. Den Darlehensvertrag hat nur Herr Lohmann unterschrieben; nach Darstellung von Frau "
    "Eschenbach hat sich Frau Kreutzer mündlich mitverpflichtet.",
    "Das Darlehen wird fällig, niemand zahlt. Frau Kreutzer sagt, das Darlehen habe Herr Lohmann allein aufgenommen. Frau "
    "Eschenbach verklagt beide vor dem Landgericht als Gesamtschuldner auf Zahlung von 20.000 Euro; Zinsen verlangt sie "
    "nicht. Jede Partei hat einen eigenen Anwalt.",
    "Nach der Beweisaufnahme schuldet Herr Lohmann die 20.000 Euro. Eine Mitverpflichtung von Frau Kreutzer kann Frau "
    "Eschenbach nicht beweisen. Das Gericht verurteilt Herrn Lohmann zur Zahlung und weist die Klage gegen Frau Kreutzer ab.",
], "Wie werden Gerichtskosten und außergerichtliche Kosten verteilt, und wie lautet der Kostentenor?")

# ===========================================================================================================================
# D Problem: drei Parteien, zwei Prozessrechtsverhältnisse
# ===========================================================================================================================
PP = "Problem"
W61 = ("„Streitgenossen stehen, soweit nicht … sich ein anderes ergibt, dem Gegner dergestalt als Einzelne gegenüber, dass "
       "die Handlungen des einen Streitgenossen dem anderen weder zum Vorteil noch zum Nachteil gereichen.“")
w61, w61_y = wortlaut(80, 410, 1100, W61, "§ 61 ZPO", "p61", marken=[("als Einzelne gegenüber,", beim("p61", "Einzelner"))],
                      size=30)
folie([("problem", f"{PP} · §§ 91, 92 ZPO: zwei Parteien"), ("drei", f"{PP} › hier: drei Parteien"),
       ("p59", f"{PP} › Streitgenossen, § 59 ZPO"), ("p61", f"{PP} › § 61 ZPO: jeder als Einzelner"),
       ("zwei", f"{PP} › zwei Prozessrechtsverhältnisse")], rechts_frei([
    *tafel("problem", "Das Problem: drei Parteien"),
    z("§§ 91, 92 ZPO denken in zwei Parteien:", 110, 170, "problem", "Bold", 32),
    z("Wer verliert, zahlt. Wer teils verliert, zahlt nach Quote.", 110, 218, beim("problem", "Wer"), size=30),
    blk(110, 275, 1040, 70, GELB, "drei", [("Hier: 3 Parteien – 1 Klägerin, 2 Beklagte", "ExtraBold", 32, INK)]),
    pl("Streitgenossen: § 59 ZPO", 110, 355, "p59", fill=WEISS, size=28),
    *w61,
    blk(110, w61_y + 24, 500, 110, BLAU, beim("zwei", "Eschenbach"), [("Prozessrechtsverhältnis 1", "ExtraBold", 30, INK),
                                                                   ("Eschenbach gegen Lohmann", "Bold", 30, INK)]),
    blk(650, w61_y + 24, 500, 110, GRUEN, beim("zwei", "Eschenbach", 2), [("Prozessrechtsverhältnis 2", "ExtraBold", 30, INK),
                                                                       ("Eschenbach gegen Kreutzer", "Bold", 30, INK)]),
    *requisit([("problem", ("tabler", "scale", 100, WEISS), "zwei Parteien?", WEISS),
               ("drei", ("ph", "users-three", 120, GELB), "3 Parteien", GELB),
               ("zwei", ("tabler", "arrows-split", 100, WEISS), "2 Verhältnisse", WEISS)]),
    *zwei([("problem", "ruhig"), ("drei", "denkt"), ("zwei", "skeptisch")], [("problem", "ruhig"), ("p61", "denkt")],
          links="LO", rechts="KR"),
]))
assert w61_y + 134 <= 890, w61_y

# ===========================================================================================================================
# E § 100 ZPO
# ===========================================================================================================================
PH = "§ 100 ZPO"
W1001 = "„Besteht der unterliegende Teil aus mehreren Personen, so haften sie für die Kostenerstattung nach Kopfteilen.“"
W1004 = ("„Werden mehrere Beklagte als Gesamtschuldner verurteilt, so haften sie auch für die Kostenerstattung, unbeschadet "
         "der Vorschrift des Absatzes 3, als Gesamtschuldner. …“")
w1001, w1001_y = wortlaut(80, 165, 1100, W1001, "§ 100 Abs. 1 ZPO", "p100", marken=[
    ("aus mehreren Personen,", beim("p100", "mehreren")), ("nach Kopfteilen.", beim("p100", "Kopfteilen"))], size=30)
w1004, w1004_y = wortlaut(80, w1001_y + 18, 1100, W1004, "§ 100 Abs. 4 ZPO", "p1004", marken=[
    ("als Gesamtschuldner verurteilt,", beim("p1004", "Gesamtschuldner")),
    ("auch für die Kostenerstattung,", beim("p1004", "Kostenerstattung"))], size=30)
folie([("p100", f"{PH} · Abs. 1: nach Kopfteilen"), ("p1004", f"{PH} › Abs. 4: Gesamtschuldner"),
       ("passt", f"{PH} › setzt voraus: mehrere verlieren"), ("luecke", f"{PH} › Lücke: Baumbachsche Formel")], rechts_frei([
    *tafel("p100", "Hilft § 100 ZPO?"),
    *w1001, *w1004,
    z("Beides setzt voraus: Mehrere verlieren.", 110, w1004_y + 22, "passt", "Bold", 32),
    *neinz("Hier verliert nur Herr Lohmann.", w1004_y + 72, beim("passt", "Hier"), "ExtraBold", 32, x=170),
    blk(110, w1004_y + 140, 1040, 80, GELB, "luecke", [("Unterschiedlicher Erfolg: Baumbachsche Formel", "ExtraBold", 32, INK)]),
    *requisit([("p100", ("ph", "users", 120, WEISS), "mehrere verlieren?", WEISS),
               ("passt", ("tabler", "user", 100, HELLROT), "nur einer verliert", HELLROT),
               ("luecke", ("tabler", "calculator", 100, GELB), "Rechenmethode", GELB)]),
    *zwei([("p100", "ruhig"), ("passt", "froh")], [("p100", "skeptisch"), ("passt", "muede")], links="ES", rechts="LO"),
]))
assert w1004_y + 220 <= 890, w1004_y

# ===========================================================================================================================
# F Grundgedanke und fiktiver Streitwert
# ===========================================================================================================================
PI = "Grundgedanke"
_fs = F("ExtraBold", 36)
_t1, _t2, _t3 = "20.000 € (Lohmann)", " + 20.000 € (Kreutzer)", " = 40.000 €"
_x2 = 110 + _fs.getlength(_t1); _x3 = _x2 + _fs.getlength(_t2)
folie([("idee", f"{PI} · Kosten getrennt verteilen"), ("idee2", f"{PI} › nur eigene Verhältnisse"),
       ("fiktiv", "Fiktiver Streitwert · Summe aller Verhältnisse"), ("summe", "Fiktiver Streitwert › 2 × 20.000 € = 40.000 €"),
       ("echt", "Fiktiver Streitwert › echter Streitwert: 20.000 €")], rechts_frei([
    *tafel("idee", "Die Baumbachsche Formel"),
    blk(110, 165, 500, 90, BLAU, beim("idee", "Gerichtskosten"), [("Gerichtskosten", "ExtraBold", 34, INK)]),
    blk(650, 165, 500, 90, GRUEN, beim("idee", "außergerichtliche"), [("außergerichtliche Kosten", "ExtraBold", 34, INK)]),
    pl("getrennt verteilen", 630, 272, beim("idee", "getrennt"), fill=WEISS, size=28, anker="m"),
    z("Jede Partei trägt nur Kosten aus ihren eigenen", 110, 335, "idee2", "Bold", 32),
    z("Prozessrechtsverhältnissen – soweit sie dort verliert.", 110, 380, "idee2", "Bold", 32),
    blk(110, 450, 1040, 80, HELL, "fiktiv", [("fiktiver Streitwert = Summe aller Prozessrechtsverhältnisse", "ExtraBold", 30, INK)]),
    zit("vgl. BGH, Beschl. v. 21.1.2025 – XI ZB 26/23, Rn. 23", 110, 540, "fiktiv"),
    z(_t1, 110, 600, "summe", "ExtraBold", 36),
    z(_t2, _x2, 600, beim("summe", "plus"), "ExtraBold", 36),
    z(_t3, _x3, 600, beim("summe", "vierzigtausend"), "ExtraBold", 36, farbe=DROT),
    *okz("echter Streitwert: 20.000 € (Gesamtschuld)", 680, "echt", "Bold", 32, x=170),
    zit("keine Addition: BGH, Beschl. v. 16.7.2015 – IX ZR 136/14, Rn. 5", 170, 730, "echt"),
    blk(110, 785, 1040, 80, WEISS, beim("echt", "Rechengröße"), [("40.000 € = nur eine Rechengröße", "ExtraBold", 32, INK)]),
    *requisit([("idee", ("tabler", "arrows-split", 100, WEISS), "getrennt", WEISS),
               ("fiktiv", ("tabler", "sum", 100, GELB), "Summe", GELB),
               ("echt", ("tabler", "scale", 100, WEISS), "echt: 20.000 €", WEISS)]),
    *zwei([("idee", "ruhig"), ("fiktiv", "denkt"), ("echt", "ruhig")], [("idee", "ruhig"), ("summe", "denkt")], links="RI", rechts="KR"),
]))
assert _x3 + _fs.getlength(_t3) <= 1170

# ===========================================================================================================================
# G Die Tabelle Schritt für Schritt
# ===========================================================================================================================
PT = "Tabelle"
SP_ = {"wert": 520, "kl": 690, "lo": 860, "kr": 1020}          # Spaltenmitten
YH, YA, YS, YB, YC, YD = 172, 248, 318, 372, 446, 520           # Kopf, Zeile a, Zwischenzeile, b, c, d
TICK = 1125
els_g = [*tafel("tab", "Die Tabelle Schritt für Schritt"),
         z("Kostenmasse", 110, YH, "tab", "Bold", 30),
         zelle("Wert", SP_["wert"], YH, "tab", 30, "Bold"), zelle("Klägerin", SP_["kl"], YH, "tab", 30, "Bold"),
         zelle("Lohmann", SP_["lo"], YH, "tab", 30, "Bold"), zelle("Kreutzer", SP_["kr"], YH, "tab", 30, "Bold"),
         linie(100, YH + 52, 1150, YH + 52, "tab"),
         # a) Gerichtskosten
         z("a) Gerichtskosten", 110, YA, beim("ga", "Gerichtskosten"), "Bold", 30),
         zelle("40.000 €", SP_["wert"], YA, beim("ga", "vierzigtausend"), 30, "Bold"),
         zelle("½", SP_["kl"], YA, beim("ga2", "Hälfte")),
         zelle("½", SP_["lo"], YA, beim("ga3", "Hälfte")), zelle("0", SP_["kr"], YA, beim("ga3", "Hälfte")),
         # außergerichtliche Kosten
         z("außergerichtliche Kosten:", 110, YS, beim("kb", "außergerichtlichen"), "Bold", 28, farbe=TEXT),
         z("b) der Klägerin", 110, YB, beim("kb", "Klägerin"), "Bold", 30),
         zelle("40.000 €", SP_["wert"], YB, beim("kb", "vierzigtausend"), 30, "Bold"),
         zelle("½", SP_["lo"], YB, beim("kb2", "Hälfte")),
         zelle("½", SP_["kl"], YB, beim("kb3", "Rest")), zelle("0", SP_["kr"], YB, beim("kb3", "nichts")),
         z("c) von Lohmann", 110, YC, beim("kc", "Lohmann"), "Bold", 30),
         zelle("20.000 €", SP_["wert"], YC, beim("kc", "zwanzigtausend"), 30, "Bold"),
         zelle("–", SP_["kr"], YC, beim("kc", "nur")),
         zelle("1", SP_["lo"], YC, beim("kc2", "selbst")), zelle("0", SP_["kl"], YC, beim("kc2", "selbst")),
         z("d) von Kreutzer", 110, YD, beim("kd", "Kreutzer"), "Bold", 30),
         zelle("20.000 €", SP_["wert"], YD, beim("kd", "zwanzigtausend"), 30, "Bold"),
         zelle("–", SP_["lo"], YD, beim("kd", "nur")),
         zelle("1", SP_["kl"], YD, beim("kd2", "ganz")), zelle("0", SP_["kr"], YD, beim("kd2", "ganz")),
         linie(100, YD + 58, 1150, YD + 58, "tab"),
         z("a) 20.000 € : 40.000 € = ½", 110, 600, beim("ga2", "Zwanzig"), "Bold", 30),
         z("– = nicht beteiligt", 780, 600, beim("kc", "nur"), "Bold", 28, farbe=TEXT),
         blk(110, 660, 1040, 80, HELL, beim("jede", "Verhältnis"),
             [("Jedes Prozessrechtsverhältnis wird für sich abgerechnet.", "ExtraBold", 30, INK)]),
         z("Probe: In jeder Zeile zusammen genau 1.", 110, 775, "probe", "ExtraBold", 32),
         bis_(ok(TICK, YA + 20, beim("probe2", "Hälfte"), gr=20), None), bis_(ok(TICK, YB + 20, beim("probe2", "Hälfte", 2), gr=20), None),
         bis_(ok(TICK, YC + 20, beim("probe2", "ganz"), gr=20), None), bis_(ok(TICK, YD + 20, beim("probe2", "ganz", 2), gr=20), None),
         *requisit([("tab", ("tabler", "table", 100, WEISS), "Tabelle", WEISS),
                    ("ga", ("tabler", "building-bank", 100, BLAU), "Gerichtskosten", BLAU),
                    ("kb", ("ph", "briefcase", 110, GRUEN), "Anwalt der Klägerin", GRUEN),
                    ("kc", ("tabler", "user", 100, ORANGE), "Kosten Lohmann", ORANGE),
                    ("kd", ("tabler", "user", 100, GRUEN), "Kosten Kreutzer", GRUEN),
                    ("es2", None, None, None),
                    ("probe", ("tabler", "checklist", 100, WEISS), "Probe", WEISS)]),
         *fig("ES", X1, FB, FR, [("tab", "ruhig"), (beim("kd2", "Klägerin"), "sorge")], bis="es2"),
         *redet("ES_fragt", X1, FB, FR, "es2", "jede"),
         *fig("ES", X1, FB, FR, [("jede", "denkt"), ("probe2", "ruhig")], erst="cut"),
         ns(NAME["ES"], X1, FB, "tab", NFARBE["ES"], d=0.1),
         *fig("KR", X2, FB, FR, [("tab", "ruhig"), (beim("kd2", "ganz"), "froh"), ("probe", "ruhig")]),
         ns(NAME["KR"], X2, FB, "tab", NFARBE["KR"], d=0.1),
         blase("sprech", 560, 200, "es2", 1560, 220, inhalt=["Obwohl ich gegen Herrn", "Lohmann gewonnen habe?"], textsize=34,
               figur=("ES_fragt", X1, FB, FR), bis="jede")]
folie([("tab", f"{PT} · Schritt für Schritt"), ("ga", f"{PT} › a) Gerichtskosten"),
       ("kb", f"{PT} › b) außergerichtliche Kosten der Klägerin"), ("kc", f"{PT} › c) außergerichtliche Kosten Lohmann"),
       ("kd", f"{PT} › d) außergerichtliche Kosten Kreutzer"), ("jede", f"{PT} › jedes Verhältnis für sich"),
       ("probe", f"{PT} › Probe")], rechts_frei(els_g))

# ===========================================================================================================================
# H Kostentenor
# ===========================================================================================================================
PK = "Kostentenor"
TEN = [("tenor", ["„Die Gerichtskosten tragen die Klägerin und", "der Beklagte zu 1 je zur Hälfte."], "a)"),
       ("tenor2", ["Die außergerichtlichen Kosten der Klägerin", "trägt der Beklagte zu 1 zur Hälfte."], "b)"),
       ("tenor3", ["Die Klägerin trägt die außergerichtlichen", "Kosten der Beklagten zu 2."], "d)"),
       ("tenor4", ["Im Übrigen tragen die Parteien ihre", "außergerichtlichen Kosten selbst.“"], "Rest")]
els_h = [*tafel("tenor", "Der Kostentenor"), karte(100, 165, 1060, 560, "tenor", fill=HELL, rund=18, schatten=6, rand=4)]
y = 190
for c, zeilen, tag in TEN:
    els_h.append(pl(tag, 130, y + 4, c, fill=WEISS, size=26))
    for zl in zeilen:
        els_h.append(z(zl, 265, y, c, "ExtraBold", 32, rechts=1150)); y += 48
    y += 32
assert y <= 725, y
els_h += [blk(110, 740, 1040, 100, GELB, "rest", [("Der Schlusssatz deckt den Rest:", "ExtraBold", 30, INK),
                                                ("die eigene Hälfte der Klägerin und die Kosten von Herrn Lohmann", "Bold", 28, INK)]),
          zit("Aufbau des Tenors wie BGH, Beschl. v. 21.1.2025 – XI ZB 26/23", 110, 852, "tenor"),
          *requisit([("tenor", ("tabler", "file-text", 100, GELB), "Kostentenor", GELB),
                     ("rest", ("tabler", "circle-check", 100, WEISS), "Schlusssatz", WEISS)]),
          *zwei([("tenor", "ruhig"), ("rest", "denkt")], [("tenor", "muede"), ("tenor3", "skeptisch")], links="RI", rechts="LO")]
folie([("tenor", f"{PK} · Gerichtskosten"), ("tenor2", f"{PK} › außergerichtliche Kosten der Klägerin"),
       ("tenor3", f"{PK} › Kosten der Beklagten zu 2"), ("tenor4", f"{PK} › im Übrigen: eigene Kosten"),
       ("rest", f"{PK} › der Schlusssatz")], rechts_frei(els_h))

# ===========================================================================================================================
# I Klausurtipp (Lexi)
# ===========================================================================================================================
GX, GY, GW, GH = 130, 330, 1020, 260
els_i = [*tafel("tipp", "Klausurtipp: erst die Tabelle", fill=HELL),
         warnung_i(150, 225, "tipp", gr=26),
         z("Tabelle zuerst auf das Konzeptpapier!", 200, 200, beim("tipp", "Tabelle"), "ExtraBold", 36),
         z("eine Zeile je Kostenmasse, eine Spalte je Partei", 130, 268, beim("tipp2", "Zeile"), "Bold", 30),
         karte(GX, GY, GW, GH, beim("tipp2", "Zeile"), fill=WEISS, rund=14, schatten=6, rand=4)]
for i in range(1, 5):
    els_i.append(linie(GX + 16, GY + 20 + i * 46, GX + GW - 16, GY + 20 + i * 46, beim("tipp2", "Zeile"), breite=3))
for i, (k_, n_) in enumerate((("a)", "Gerichtskosten"), ("b)", "Klägerin"), ("c)", "Lohmann"), ("d)", "Kreutzer"))):
    els_i.append(z(f"{k_} {n_}", GX + 24, GY + 72 + i * 46, beim("tipp2", "Zeile"), size=26, farbe=TEXT))
for i, (xx, n_) in enumerate(((560, "Klägerin"), (750, "Lohmann"), (940, "Kreutzer"))):
    els_i.append(linie(xx - 20, GY + 16, xx - 20, GY + GH - 16, beim("tipp2", "Spalte"), breite=3))
    els_i.append(z(n_, xx, GY + 22, beim("tipp2", "Spalte"), "Bold", 26, rechts=GX + GW - 10))
els_i += [
          *okz("in jeder Zeile die Probe", GY + GH + 40, beim("tipp3", "Probe"), "Bold", 32, x=190),
          *okz("dann der Tenor – mit Schlusssatz für die eigenen Kosten", GY + GH + 100, beim("tipp3", "Tenor"), "Bold", 32, x=190),
          *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
          ns("Lexi", FX, FB, "tipp", GELB, d=0.2)]
folie([("tipp", "Klausurtipp · Tabelle auf dem Konzeptpapier"), ("tipp2", "Klausurtipp › Zeilen und Spalten"),
       ("tipp3", "Klausurtipp › Probe, dann Tenor")], els_i)

# ===========================================================================================================================
# J Schema (Aufbau Punkt für Punkt)
# ===========================================================================================================================
REIHEN = [("k1", 0, "1. Prozessrechtsverhältnisse auflisten"),
          ("k2", 0, "2. Fiktiven Streitwert bilden"), (beim("k2", "Summe"), 1, "Summe aller Verhältnisse"),
          ("k3", 0, "3. Gerichtskosten"), (beim("k3", "Unterliegen"), 1, "nach dem Unterliegen am fiktiven Streitwert"),
          ("k4", 0, "4. Außergerichtliche Kosten"), (beim("k4", "gesondert"), 1, "für jede Partei gesondert, nur aus ihren Verhältnissen"),
          ("k5", 0, "5. Probe und Tenor")]
els_sch = [karte(60, 50, 1800, 940, "sch"), titel(glyphen("Schema: die Baumbachsche Formel"), 110, 90, "sch", 50)]
y = 210
for c, ebene, text in REIHEN:
    x = (130, 200)[ebene]
    els_sch.append(z(text, x, y, c, ("ExtraBold", "Regular")[ebene], (40, 36)[ebene], rechts=1800, farbe=(INK, TEXT)[ebene]))
    y += {0: 80, 1: 92}[ebene]
assert y <= 960, y
folie([("sch", "Schema"), ("k1", "Schema › 1. Prozessrechtsverhältnisse"), ("k2", "Schema › 2. Fiktiver Streitwert"),
       ("k3", "Schema › 3. Gerichtskosten"), ("k4", "Schema › 4. Außergerichtliche Kosten"), ("k5", "Schema › 5. Probe und Tenor")],
      els_sch)

# ===========================================================================================================================
# K Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Bei Streitgenossen rechnest du jedes", 0)], [("Prozessrechtsverhältnis ", 0), ("für sich", "a"), (".", 0)]],
                750, 290, 46, "merke", {"a": beim("merke", "für")}),
    *markertext([[("Gerichtskosten am fiktiven ", 0), ("Gesamtstreitwert", "b"), (",", 0)],
                 [("außergerichtliche Kosten für", 0)], [("jede Partei ", 0), ("getrennt", "c"), (".", 0)]], 750, 500, 46, "m2",
                {"b": beim("m2", "Gesamtstreitwert"), "c": beim("m2", "getrennt")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
