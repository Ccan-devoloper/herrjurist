"""Folge 182 · Fahrlässigkeitsdelikt Schema: §§ 222, 229 StGB richtig prüfen – Serienstandard Open Peeps (Katzenkönig).
Fall: Herr Berger (Eigentümer und Vermieter) lässt die morsche Holzbrüstung am Balkon seiner Mieterin Frau Specht trotz
dreier Hinweise sechs Wochen unrepariert; ein Gast lehnt sich an, die Brüstung bricht, der Gast wird schwer verletzt.
DARSTELLUNG: kein Sturz, kein Aufprall, keine Verletzten im Bild. Die Brüstung bricht nur im Gebäude-Icon (Tabler „building“
mit Balkonplatte und Tabler „fence“ bzw. „fence-off“) mit Warnsymbol; die Folge steht nur als Text (§ 229, Variante § 222).
Szenen laut ../SZENENPLAN.md: A1 Mietshaus (Hinweise), A2 Besuch, A3 Die Brüstung bricht (Icon), B Sachverhalt, C § 15,
D §§ 229, 222, E Drei Stufen, F 1. Erfolg / 2. Unterlassen und Garant, G 3. Kausalität, H 4. Sorgfaltspflichtverletzung,
I 5. Vorhersehbarkeit, J 6. Pflichtwidrigkeitszusammenhang und Schutzzweck, K II. Rechtswidrigkeit / III. Schuld,
L Ergebnis und Variante, M Abgrenzung zum bedingten Vorsatz, N Klausurtipp (Lexi), O Prüfschema, P Merksatz (Lexi).
Jeder Prüfungspunkt hat eine eigene Farbe (PUNKTFARBE), gleich auf den Punkttafeln und im Prüfschema.
Zwei Handlungsgeräusche: Holz knarrt, als die Brüstung sichtbar wackelt; Türklingel, als der Gast kommt
(../geraeusche_herkunft.json).
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz
als eigene Kopie aus Folge 179 (gemeinsame Dateien unverändert); neu: haus(), punkt(), zitatkarte().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_182/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_182/" in n:
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
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 04.10.2026, Folge 182), als Zitat mit Normangabe;
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
NAME = {"BE": "Herr Berger", "SP": "Frau Specht", "GA": "Gast"}
NFARBE = {"BE": ORANGE, "SP": TUERKIS, "GA": BLAU}


def stehend(k, x, folge, unten=FB, hoehe=FR, bis=None):
    return [*fig(k, x, unten, hoehe, folge, bis=bis), bis_(ns(NAME[k], x, unten, folge[0][0], NFARBE[k], d=0.1), bis)]


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


def zwei(a, folge_a, b, folge_b):
    """Zwei Figuren rechts neben der Tafel (blicken nach links zur Tafel)."""
    return [*stehend(a, X1, folge_a), *stehend(b, X2, folge_b)]


# Eigene Farbe je Prüfungspunkt (Punkttafeln und Prüfschema)
PUNKTFARBE = {1: GELB, 2: LILA, 3: BLAU, 4: ROT, 5: GRUEN, 6: ORANGE, "II": TUERKIS, "III": PINK}


def punkt(nr, text, cue, y=170, h=78, size=36):
    """Kopf eines Prüfungspunkts in seiner Farbe."""
    return blk(110, y, 1040, h, PUNKTFARBE[nr], cue, [(text, "ExtraBold", size, INK)])


def zitatkarte(x, y, w, text, quelle, cue, size=30, bis=None):
    """Wörtliches BGH-Zitat (Anführungszeichen, Fundstelle)."""
    zeilen = umbruch(text, size, w - 60)
    return wortlaut(x, y, w, zeilen, quelle, cue, size=size, bis=bis)


# ===========================================================================================================================
# Bühne der Fallszenen: das Mietshaus (Tabler „building“), Balkonplatte (Grundform) mit Brüstung (Tabler „fence“)
# ===========================================================================================================================
BODEN, FH = 880, 470
HX, HB = 400, 640                           # Haus: Mitte, Iconbreite
_haus_probe = ficon("tabler", "building", HX, BODEN, HB, "_", fuell=GELB)
HAUS_L, HAUS_R, HAUS_O = _haus_probe.x, _haus_probe.x + _haus_probe.sprite.width, _haus_probe.y
# Korpus des Icons: x 5…19 von 3…21 (Tabler-Pfad), Balkon an der rechten Hauswand im 2. Stock
KORPUS_R = HAUS_L + _haus_probe.sprite.width * (19 - 3) / 18
BAL_Y = HAUS_O + _haus_probe.sprite.height * 0.36        # Oberkante der Balkonplatte (oberste Fensterreihe = 2. Stock)
BAL_W = 250
BAL_X = KORPUS_R - 6


ZAUN_B = 210
ZAUN_O = BAL_Y + 6 - ficon("tabler", "fence", 0, 0, ZAUN_B, "_", fuell=HOLZ).sprite.height   # Oberkante der Brüstung


def platte(c):
    s = 2
    im = Image.new("RGBA", ((BAL_W + 8) * s, 30 * s))
    ImageDraw.Draw(im).rounded_rectangle((2 * s, 2 * s, (BAL_W + 4) * s, 26 * s), 5 * s, fill=HELLGRAU, outline=INK, width=4 * s)
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    return El(im, BAL_X, BAL_Y, c, "cut", 0.0, None, name="balkonplatte")


def bruestung(c, art="fest", bis=None):
    """Brüstung auf der Balkonplatte: fest, wackelt (um 7° geneigt, nicht umgezeichnet) oder gebrochen (Tabler „fence-off“)."""
    if art == "gebrochen":
        e = ficon("tabler", "fence-off", BAL_X + BAL_W / 2 + 4, BAL_Y + 6, ZAUN_B, c, fuell=ROT, anim="cut", bis=bis)
        return e
    e = ficon("tabler", "fence", BAL_X + BAL_W / 2 + 4, BAL_Y + 6, ZAUN_B, c, fuell=HOLZ, anim="cut", bis=bis)
    if art == "wackelt":
        sp = e.sprite.rotate(-7, expand=True, resample=Image.BICUBIC)
        e = El(sp, e.x + e.sprite.width / 2 - sp.width / 2 + 6, e.y + e.sprite.height - sp.height + 4, c, "cut", 0.0, bis,
               name="ficon:fence-wackelt")
    return e


def haus(c, h=lambda e: e):
    return [h(boden(BODEN, c)), h(ficon("tabler", "building", HX, BODEN, HB, c, fuell=GELB, anim="cut")), h(platte(c))]


WARN_X, WARN_U = BAL_X + BAL_W / 2 + 4, ZAUN_O - 14     # Warnsymbol über der Brüstung (Unterkante)
BEX, SPX = 1060, 1500                       # Herr Berger (blickt nach rechts), Frau Specht (blickt nach links)
GAX = 1500
_h = lambda e: hart(e)
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig

# ===========================================================================================================================
# A1 Fall: das Mietshaus, die Hinweise der Mieterin
# ===========================================================================================================================
WACKEL = beim("morsch", "wackelt")
folie([(NULL, "Fall · Das Mietshaus"), ("sp1", "Fall · Die Hinweise der Mieterin"), ("nichts", "Fall · Es passiert nichts")], [
    *haus(NULL, _h),
    _h(bruestung(NULL, "fest", bis=WACKEL)),
    szene(bruestung(WACKEL, "wackelt"), "182knarren*", 0.7, 0.0),
    ficon("tabler", "alert-triangle", WARN_X, WARN_U, 90, WACKEL, fuell=GELB),
    _h(pl("Ein Mietshaus in der Stadt", 70, 30, NULL, fill=GELB, size=38)),
    pl("Eigentümer: Herr Berger", 70, 110, "berger", fill=ORANGE, size=34),
    pl("2. Stock: Frau Specht mit Balkon", 70, 190, "specht", fill=TUERKIS, size=34),
    pl("Holzbrüstung: morsch, sie wackelt", 70, 270, "morsch", fill=HELLROT, size=34, bis="nichts"),
    # Herr Berger (blickt nach rechts zu Frau Specht), Frau Specht (blickt nach links, zeigt zum Balkon)
    *fig("BE", BEX, BODEN, FH, [("berger", "ruhig_r")], bis="b1"),
    *redet("BE_redet_r", BEX, BODEN, FH, "b1", "nichts"),
    *fig("BE", BEX, BODEN, FH, [("nichts", "denkt_r"), ("haelt", "ruhig_r")], erst="cut"),
    ns("Herr Berger", BEX, BODEN, "berger", ORANGE, d=0.1),
    *fig("SP", SPX, BODEN, FH, [("specht", "ruhig")], bis="sp1"),
    *redet("SP_redet", SPX, BODEN, FH, "sp1", "b1"),
    *fig("SP", SPX, BODEN, FH, [("b1", "ruhig"), ("nichts", "sorge"), ("haelt", "ernst")], erst="cut"),
    ns("Frau Specht", SPX, BODEN, "specht", TUERKIS, d=0.1),
    blase("sprech", 820, 300, "sp1", 1270, 215, inhalt=["Herr Berger, die Brüstung", "am Balkon ist locker. Bitte", "lassen Sie sie reparieren!"],
          textsize=36, figur=("SP_redet", SPX, BODEN, FH), bis="b1"),
    blase("sprech", 640, 220, "b1", 1290, 240, inhalt=["Ja, ja, ich kümmere", "mich darum."], textsize=38,
          figur=("BE_redet_r", BEX, BODEN, FH), bis="nichts"),
    pl("Doch es passiert nichts.", 70, 270, "nichts", fill=WEISS, size=34),
    ficon("tabler", "mail", 830, 112, 84, beim("zweimal", "E-Mail"), fuell=WEISS),
    pl("2. und 3. Hinweis, zuletzt per E-Mail", 900, 40, "zweimal", fill=TUERKIS, size=32),
    pl("hält einen Unfall für möglich", 900, 120, beim("haelt", "möglich"), fill=WEISS, size=32),
    pl("vertraut: Die Brüstung hält schon.", 900, 200, beim("haelt", "vertraut"), fill=HELLROT, size=32),
])

# ===========================================================================================================================
# A2 Fall: 6 Wochen später, der Besuch (derselbe Ort; die Brüstung wackelt noch); der Gast oben am Balkon
# ===========================================================================================================================
GAST_DA = beim("wochen", "Frau")
GBX, GBH = BAL_X + BAL_W / 2 - 20, 300      # Gast auf dem Balkon hinter der Brüstung (kleiner, weil oben)
folie([("wochen", "Fall · 6 Wochen später: Besuch"), ("gast", "Fall · Auf dem Balkon")], [
    *haus("wochen"),
    bruestung("wochen", "wackelt", bis="gast"),
    ficon("tabler", "alert-triangle", WARN_X, WARN_U, 90, "wochen", fuell=GELB, anim="cut", bis="gast"),
    pl("6 Wochen nach dem 1. Hinweis", 70, 30, "wochen", fill=GELB, size=38),
    ficon("tabler", "calendar-event", 760, 100, 70, "wochen", fuell=WEISS),
    pl("Frau Specht hat Besuch.", 70, 110, beim("wochen", "Besuch"), fill=TUERKIS, size=34),
    # Frau Specht (blickt nach rechts zum Gast), der Gast kommt von rechts (Türklingel)
    *fig("SP", 1130, BODEN, FH, [("wochen", "ruhig_r"), (beim("wochen", "Besuch"), "froh_r")], bis="gast"),
    bis_(ns("Frau Specht", 1130, BODEN, "wochen", TUERKIS, d=0.1), "gast"),
    szene(bewegt(peep_voll("GA_froh", GAX, BODEN, FH - 10, GAST_DA, anim="cut", bis="gast"), GAST_DA,
                 (GAST_DA[0], GAST_DA[1] + 1.0), 200, 0), "182klingel*", 0.8, -0.1),
    bis_(bewegt(ns("Gast", GAX, BODEN, GAST_DA, BLAU, anim="cut"), GAST_DA, (GAST_DA[0], GAST_DA[1] + 1.0), 200, 0), "gast"),
    # auf dem Balkon: der Gast steht an der Brüstung (die Brüstung liegt vor ihm), kein Sturz im Bild
    peep_voll("GA_ruhig_r", GBX, BAL_Y + 4, GBH, "gast", anim="cut"),
    bruestung("gast", "wackelt"),
    pl("Gast", BAL_X + BAL_W + 20, BAL_Y - 20, "gast", fill=BLAU, size=30, anim="cut"),
    pl("Der Gast lehnt sich an die Brüstung.", 70, 190, beim("gast", "lehnt"), fill=WEISS, size=36),
])

# ===========================================================================================================================
# A3 Fall: Die Brüstung bricht – nur Gebäude-Icon mit Warnsymbol, die Folge als Text (kein Sturz, kein Aufprall im Bild)
# ===========================================================================================================================
BRICHT = beim("bricht", "bricht")
folie([("bricht", "Fall · Die Brüstung bricht"), ("gutacht", "Fall · Der Sachverständige"),
       ("frage", "Die Frage · Strafbar trotz Fahrlässigkeit?")], [
    *haus("bricht"),
    bruestung("bricht", "wackelt", bis=BRICHT),
    bruestung(BRICHT, "gebrochen"),
    ficon("tabler", "alert-triangle", WARN_X, WARN_U, 130, BRICHT, fuell=ROT),
    pl("Die Brüstung bricht.", 70, 30, BRICHT, fill=HELLROT, size=36),
    pl("Der Gast stürzt in den Hof: schwer verletzt", 70, 110, "verletzt", fill=HELLROT, size=34),
    ficon("fluent-emoji-flat", "ambulance", 1010, BODEN, 260, beim("verletzt", "verletzt")),
    ficon("tabler", "hammer", 1770, 330, 80, "gutacht", fuell=HOLZ),
    pl("Sachverständiger: Rechtzeitige Reparatur", 900, 250, "gutacht", fill=GRUEN, size=32),
    pl("hätte den Bruch verhindert.", 900, 320, beim("gutacht", "hätte"), fill=GRUEN, size=32),
    # Herr Berger (sachlich, besorgt) zur Frage
    *fig("BE", 1560, BODEN, FH, [("frage", "sorge"), ("frage2", "denkt")]),
    ns("Herr Berger", 1560, BODEN, "frage", ORANGE, d=0.1),
    pl("Wollte niemanden verletzen: trotzdem strafbar?", 900, 40, "frage", fill=WEISS, size=32),
    pl("Wie prüfst du ein Fahrlässigkeitsdelikt?", 900, 120, "frage2", fill=PINK, size=34),
])

# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_182(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=36, zeilenabstand=1.30)
        els += e; y += 18
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=34))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_182("sv", [
    "Herr Berger ist Eigentümer eines Mietshauses. Frau Specht wohnt dort im 2. Stock; die Holzbrüstung ihres Balkons ist "
    "morsch und wackelt. Sie bittet Herrn Berger, die Brüstung reparieren zu lassen. Er antwortet: „Ja, ja, ich kümmere mich "
    "darum.“ Doch es passiert nichts. Frau Specht erinnert ihn noch 2-mal, zuletzt per E-Mail. Herr Berger hält einen "
    "Unfall zwar für möglich, vertraut aber darauf, dass die Brüstung schon hält.",
    "6 Wochen nach dem ersten Hinweis hat Frau Specht Besuch. Ihr Gast lehnt sich auf dem Balkon an die Brüstung. Sie "
    "bricht; der Gast stürzt in den Hof und wird schwer verletzt. Ein Sachverständiger stellt fest: Eine rechtzeitige "
    "Reparatur hätte den Bruch verhindert.",
], "Wie hat sich Herr Berger strafbar gemacht?")

# ===========================================================================================================================
# C § 15 StGB (Wortlautkarte)
# ===========================================================================================================================
W15 = umbruch("„Strafbar ist nur vorsätzliches Handeln, wenn nicht das Gesetz fahrlässiges Handeln ausdrücklich mit Strafe "
              "bedroht.“", 36, 1000)
w15, w15_y = wortlaut(80, 170, 1100, W15, "§ 15 StGB", "p15", marken=[
    (0, "vorsätzliches Handeln", beim("p15", "vorsätzliches")),
    (1, "ausdrücklich", beim("p15", "ausdrücklich"))], size=36)
folie([("p15", "Einordnung · § 15 StGB"), ("ausdr", "Einordnung · Fahrlässigkeit nur bei ausdrücklicher Strafdrohung")],
      rechts_frei([
    *tafel("p15", "Ausgangspunkt: § 15 StGB"),
    *w15,
    blk(110, w15_y + 40, 1040, 120, GELB, "ausdr", [("Fahrlässigkeit ist nur dort strafbar,", "ExtraBold", 34, INK),
                                                    ("wo das Gesetz es ausdrücklich sagt.", "ExtraBold", 34, INK)]),
    *requisit([("p15", ("tabler", "book", 100, WEISS), "§ 15 StGB", GELB),
               ("ausdr", ("tabler", "list-check", 100, WEISS), "ausdrücklich geregelt?", WEISS)]),
    *stehend("BE", FX, [("p15", "ruhig"), ("ausdr", "denkt")]),
]))

# ===========================================================================================================================
# D § 229 und § 222 StGB (Wortlautkarten), Strafrahmen in Ziffern
# ===========================================================================================================================
W229 = umbruch("„Wer durch Fahrlässigkeit die Körperverletzung einer anderen Person verursacht, wird mit Freiheitsstrafe "
               "bis zu drei Jahren oder mit Geldstrafe bestraft.“", 32, 1010)
W222 = umbruch("„Wer durch Fahrlässigkeit den Tod eines Menschen verursacht, wird mit Freiheitsstrafe bis zu fünf Jahren "
               "oder mit Geldstrafe bestraft.“", 32, 1010)
w229, w229_y = wortlaut(80, 165, 1100, W229, "§ 229 StGB", "p229", marken=[
    (0, "durch Fahrlässigkeit", beim("p229", "Fahrlässigkeit")), (0, "Körperverletzung", beim("p229", "Körperverletzung"))],
    size=32)
w222, w222_y = wortlaut(80, w229_y + 26, 1100, W222, "§ 222 StGB", "p222", marken=[
    (0, "den Tod eines Menschen", beim("p222", "Tod"))], size=32)
folie([("p229", "Einordnung · fahrlässige Körperverletzung, § 229 StGB"), ("p222", "Einordnung · fahrlässige Tötung, § 222 StGB"),
       ("gleich", "Einordnung · ein Schema für §§ 229, 222 StGB")], rechts_frei([
    *tafel("p229", "§ 229 und § 222 StGB"),
    *w229, *w222,
    blk(110, w222_y + 30, 1040, 78, GRUEN, "gleich", [("Beide: dasselbe Prüfungsschema", "ExtraBold", 36, INK)]),
    *requisit([("p229", ("tabler", "first-aid-kit", 100, ROT), "§ 229: bis 3 Jahre oder Geldstrafe", WEISS),
               ("p222", ("tabler", "scale", 100, WEISS), "§ 222: bis 5 Jahre oder Geldstrafe", WEISS),
               ("gleich", ("tabler", "list-numbers", 100, WEISS), "ein Schema", GRUEN)]),
    *stehend("BE", FX, [("p229", "ernst"), ("gleich", "ruhig")]),
]))

# ===========================================================================================================================
# E Drei Stufen: Tatbestand, Rechtswidrigkeit, Schuld; Fahrlässigkeit objektiv und subjektiv
# ===========================================================================================================================
folie([("stufen", "Schema · drei Stufen"), ("tb", "Schema · I. Tatbestand"), ("rw0", "Schema · II. Rechtswidrigkeit"),
       ("sd0", "Schema · III. Schuld"), ("zwei", "Schema · Fahrlässigkeit objektiv und subjektiv")], rechts_frei([
    *tafel("stufen", "Das Schema: drei Stufen"),
    blk(110, 190, 1040, 90, BLAU, "tb", [("I. Tatbestand", "ExtraBold", 40, INK)]),
    blk(110, 310, 1040, 90, PUNKTFARBE["II"], "rw0", [("II. Rechtswidrigkeit", "ExtraBold", 40, INK)]),
    blk(110, 430, 1040, 90, PUNKTFARBE["III"], "sd0", [("III. Schuld", "ExtraBold", 40, INK)]),
    z("Fahrlässigkeit zweimal prüfen:", 110, 570, "zwei", "Bold", 36),
    *okz("im Tatbestand objektiv", 640, beim("zwei", "Tatbestand"), "Bold", 36, x=160),
    *okz("in der Schuld subjektiv", 710, beim("zwei", "Schuld"), "Bold", 36, x=160),
    *requisit([("stufen", ("tabler", "list-numbers", 100, WEISS), "3 Stufen", WEISS),
               ("zwei", ("tabler", "eye", 100, WEISS), "objektiv + subjektiv", GELB)]),
    *stehend("BE", FX, [("stufen", "ruhig"), ("zwei", "denkt")]),
]))

# ===========================================================================================================================
# F I. 1. Erfolg, 2. Handlung: Unterlassen und Garantenstellung (§ 13 nur kurz, Verweis Folge 071)
# ===========================================================================================================================
PT = "I. Tatbestand"
folie([("erfolg", f"{PT} › 1. Erfolg"), ("handl", f"{PT} › 2. Handlung: Tun oder Unterlassen?"),
       ("p13", f"{PT} › 2. Unterlassen: Garantenstellung, § 13 StGB")], rechts_frei([
    *tafel("erfolg", "I. Tatbestand: Erfolg und Unterlassen"),
    punkt(1, "1. Erfolg", "erfolg"),
    *okz("Der Gast ist am Körper verletzt.", 270, beim("erfolg", "Gast"), "Bold", 34, x=160),
    punkt(2, "2. Handlung", "handl", y=350),
    *okz("kein Tun, sondern Unterlassen: nicht repariert", 450, beim("unterl", "Unterlassen"), "Bold", 32, x=160),
    z("§ 13 StGB: Herr Berger muss Garant sein.", 160, 515, "p13", "Bold", 32),
    *okz("Eigentümer: Haus als Gefahrenquelle", 580, beim("vsp", "Eigentümer"), size=32, x=210),
    *okz("verkehrssicherungspflichtig: Überwachergarant", 640, beim("vsp", "verkehrssicherungspflichtig"), size=32, x=210),
    zit("vgl. BGH 4 StR 252/08, Rn. 17; 5 StR 394/08, Rn. 23", 210, 690, beim("vsp", "macht")),
    *okz("Reparatur war ihm möglich", 740, "moegl", size=32, x=210),
    z("Einzelheiten: Video „Unterlassungsdelikt“", 160, 805, "verw", "Bold", 30, farbe=TEXT),
    *requisit([("erfolg", ("fluent-emoji-flat", "ambulance", 170, None), "Körper verletzt", HELLROT),
               ("handl", ("tabler", "hammer", 100, HOLZ), "nicht repariert", WEISS),
               ("p13", ("tabler", "shield", 100, LILA), "Garant?", LILA),
               ("vsp", ("tabler", "building", 120, GELB), "Gefahrenquelle Haus", WEISS)]),
    *stehend("BE", FX, [("erfolg", "ernst"), ("unterl", "still"), ("vsp", "ruhig")]),
]))

# ===========================================================================================================================
# G I. 3. Kausalität (beim Unterlassen: hypothetisch)
# ===========================================================================================================================
folie([("kaus", f"{PT} › 3. Kausalität")], rechts_frei([
    *tafel("kaus", "I. Tatbestand: Kausalität"),
    punkt(3, "3. Kausalität", "kaus"),
    z("Beim Unterlassen fragst du:", 110, 290, beim("kaus", "Beim"), "Bold", 34),
    z("Hätte die gebotene Handlung", 160, 350, beim("kaus", "Hätte"), size=34),
    z("den Erfolg verhindert?", 160, 400, beim("kaus", "Hätte"), size=34),
    zit("BGH 1 StR 272/09, Rn. 65 f.", 160, 455, beim("kaus", "verhindert")),
    *okz("Sachverständiger: ja", 530, "kaus2", "Bold", 34, x=160),
    z("Mit Reparatur wäre die Brüstung nicht gebrochen.", 160, 590, beim("kaus2", "Mit"), size=32),
    *requisit([("kaus", ("tabler", "link", 100, BLAU), "Kausalität", BLAU),
               ("kaus2", ("tabler", "hammer", 100, HOLZ), "Reparatur: kein Bruch", GRUEN)]),
    *stehend("BE", FX, [("kaus", "denkt"), ("kaus2", "still")]),
]))

# ===========================================================================================================================
# H I. 4. objektive Sorgfaltspflichtverletzung
# ===========================================================================================================================
folie([("sorg", f"{PT} › 4. objektive Sorgfaltspflichtverletzung"), ("verm", f"{PT} › 4. Sorgfalt eines Vermieters"),
       ("sorg2", f"{PT} › 4. Sorgfaltspflicht verletzt (+)")], rechts_frei([
    *tafel("sorg", "I. Tatbestand: Sorgfaltspflicht"),
    punkt(4, "4. Objektive Sorgfaltspflichtverletzung", "sorg"),
    z("Maßstab: ein besonnener und gewissenhafter Mensch", 110, 290, "mass", "Bold", 32),
    z("in der konkreten Lage und sozialen Rolle des Täters", 110, 340, beim("mass", "in"), "Bold", 32),
    zit("BGH 4 StR 19/20, Rn. 14 (BGHSt 66, 119)", 110, 395, beim("mass", "Täters")),
    z("Ein gewissenhafter Vermieter hätte nach dem", 110, 470, "verm", size=32),
    z("1. Hinweis die Brüstung prüfen und reparieren", 110, 518, beim("verm", "Hinweis"), size=32),
    z("oder den Balkon sperren lassen.", 110, 566, beim("verm", "Balkon"), size=32),
    zit("vgl. BGH 4 StR 252/08, Rn. 17 f.", 110, 620, beim("verm", "Balkon")),
    *okz("Herr Berger: wochenlang nichts getan", 690, "sorg2", "Bold", 34, x=160),
    blk(110, 760, 1040, 78, PUNKTFARBE[4], beim("sorg2", "Damit"), [("Sorgfaltspflicht verletzt", "ExtraBold", 36, INK)]),
    *requisit([("sorg", ("tabler", "scale", 100, ROT), "Herzstück", ROT),
               ("mass", ("tabler", "user-check", 100, WEISS), "besonnen und gewissenhaft", WEISS),
               ("verm", ("tabler", "barrier-block", 110, GELB), "prüfen, reparieren, sperren", WEISS),
               ("sorg2", ("tabler", "calendar-x", 100, WEISS), "6 Wochen nichts", HELLROT)]),
    *stehend("BE", FX, [("sorg", "ernst"), ("verm", "denkt"), ("sorg2", "still")]),
]))

# ===========================================================================================================================
# I I. 5. objektive Vorhersehbarkeit
# ===========================================================================================================================
folie([("vorh", f"{PT} › 5. objektive Vorhersehbarkeit"), ("vorh2", f"{PT} › 5. Vorhersehbarkeit: Warnungen der Mieterin")],
      rechts_frei([
    *tafel("vorh", "I. Tatbestand: Vorhersehbarkeit"),
    punkt(5, "5. Objektive Vorhersehbarkeit", "vorh"),
    z("Erfolg in seinem Gewicht im Wesentlichen", 110, 290, beim("vorh", "Der"), "Bold", 34),
    z("vorhersehbar, nicht in allen Einzelheiten", 110, 342, beim("vorh", "vorhersehbar", nr=2), "Bold", 34),
    zit("BGH 4 StR 19/20, Rn. 18", 110, 400, beim("vorh", "Einzelheiten")),
    *okz("Die Mieterin hatte mehrfach gewarnt.", 480, "vorh2", "Bold", 34, x=160),
    *okz("Anlehnen und Absturz: liegt auf der Hand", 550, beim("vorh2", "Dass"), "Bold", 34, x=160),
    *requisit([("vorh", ("tabler", "eye", 100, GRUEN), "vorhersehbar?", GRUEN),
               ("vorh2", ("tabler", "mail", 100, WEISS), "3 Warnungen", TUERKIS)]),
    *stehend("BE", FX, [("vorh", "ruhig"), ("vorh2", "sorge")]),
]))

# ===========================================================================================================================
# J I. 6. Pflichtwidrigkeitszusammenhang (rechtmäßiges Alternativverhalten) und Schutzzweck
# ===========================================================================================================================
zk, zk_y = zitatkarte(80, 310, 1100, "„… werden Erfolge nur dann zugerechnet, wenn sie im Falle eines pflichtgemäßen "
                      "Verhaltens des Täters nicht eingetreten wären.“", "BGH 4 StR 19/20, Rn. 21", "formel", size=30)
folie([("pwz", f"{PT} › 6. Pflichtwidrigkeitszusammenhang"), ("zweifel", f"{PT} › 6. im Zweifel für den Angeklagten"),
       ("pwz2", f"{PT} › 6. Pflichtwidrigkeitszusammenhang (+)"), ("schutz", f"{PT} › 6. Schutzzweck der Pflicht")],
      rechts_frei([
    *tafel("pwz", "I. Tatbestand: Zurechnung"),
    punkt(6, "6. Pflichtwidrigkeitszusammenhang", "pwz", h=70, size=34),
    z("Stichwort: rechtmäßiges Alternativverhalten", 110, 258, beim("pwz", "rechtmäßiges"), "Bold", 30),
    *zk,
    z("Ernsthaft zweifelhaft: im Zweifel für den Angeklagten.", 110, zk_y + 18, "zweifel", "Bold", 30),
    z("Bloß gedankliche Möglichkeit genügt nicht.", 110, zk_y + 62, beim("zweifel", "Eine"), size=30),
    zit("BGH 1 StR 272/09, Rn. 66", 110, zk_y + 106, beim("zweifel", "Eine")),
    *okz("Reparierte Brüstung hätte gehalten.", zk_y + 160, "pwz2", "Bold", 32, x=160),
    *okz("Schutzzweck: Eine sichere Brüstung soll Menschen", zk_y + 225, "schutz", "Bold", 32, x=160),
    z("auf dem Balkon vor einem Sturz bewahren.", 160, zk_y + 270, beim("schutz", "Eine"), "Bold", 32),
    *requisit([("pwz", ("tabler", "arrows-split", 100, ORANGE), "rechtmäßiges Alternativverhalten", ORANGE),
               ("zweifel", ("tabler", "scale", 100, WEISS), "in dubio pro reo", WEISS),
               ("pwz2", ("tabler", "hammer", 100, HOLZ), "hätte gehalten", GRUEN),
               ("schutz", ("tabler", "shield-check", 100, GRUEN), "Schutzzweck (+)", GRUEN)]),
    *stehend("BE", FX, [("pwz", "ruhig"), ("zweifel", "denkt"), ("pwz2", "still")]),
]))

# ===========================================================================================================================
# K II. Rechtswidrigkeit, III. Schuld: subjektive Sorgfaltspflichtverletzung und Vorhersehbarkeit
# ===========================================================================================================================
folie([("rw", "II. Rechtswidrigkeit"), ("schuld", "III. Schuld › subjektive Sorgfaltspflichtverletzung"),
       ("subj2", "III. Schuld › subjektive Vorhersehbarkeit"), ("subj3", "III. Schuld (+)")], rechts_frei([
    *tafel("rw", "II. Rechtswidrigkeit, III. Schuld"),
    punkt("II", "II. Rechtswidrigkeit", "rw"),
    *okz("keine Rechtfertigungsgründe ersichtlich", 270, beim("rw", "Rechtfertigungsgründe"), "Bold", 34, x=160),
    punkt("III", "III. Schuld: die subjektive Seite", "schuld", y=350),
    z("Konnte er nach persönlichen Kenntnissen und", 110, 450, "subj", "Bold", 32),
    z("Fähigkeiten die Pflicht erkennen und erfüllen?", 110, 498, beim("subj", "Fähigkeiten"), "Bold", 32),
    z("War der Erfolg für ihn vorhersehbar?", 110, 560, "subj2", "Bold", 32),
    zit("vgl. BGH 4 StR 19/20, Rn. 11", 110, 612, "subj2"),
    *okz("kannte die Warnungen", 680, "subj3", "Bold", 34, x=160),
    *okz("hätte einen Handwerker beauftragen können", 745, beim("subj3", "hätte"), "Bold", 34, x=160),
    *requisit([("rw", ("tabler", "shield", 100, TUERKIS), "keine Rechtfertigung", WEISS),
               ("schuld", ("tabler", "user-check", 100, PINK), "subjektiv", PINK),
               ("subj3", ("tabler", "tool", 100, WEISS), "Handwerker möglich", GRUEN)]),
    *stehend("BE", FX, [("rw", "ruhig"), ("schuld", "denkt"), ("subj3", "still")]),
]))

# ===========================================================================================================================
# L Ergebnis, § 230, Variante § 222
# ===========================================================================================================================
folie([("erg", "Ergebnis · fahrlässige Körperverletzung durch Unterlassen, §§ 229, 13 StGB"),
       ("antrag", "Ergebnis · Strafantrag, § 230 Abs. 1 StGB"), ("tod", "Variante · Gast stirbt: §§ 222, 13 StGB")],
      rechts_frei([
    *tafel("erg", "Ergebnis"),
    z("Herr Berger ist strafbar wegen", 110, 180, "erg", "Bold", 36),
    blk(110, 245, 1040, 120, GELB, beim("erg", "fahrlässiger"), [("fahrlässiger Körperverletzung", "ExtraBold", 36, INK),
                                                              ("durch Unterlassen, §§ 229, 13 StGB", "ExtraBold", 36, INK)]),
    z("§ 230 Abs. 1 StGB: auf Strafantrag oder bei", 110, 395, "antrag", size=32),
    z("besonderem öffentlichem Interesse", 110, 443, beim("antrag", "besonderem"), size=32),
    linienzug([(130, 515), (1130, 515)], "tod", breite=3),
    z("Variante: Der Gast stirbt.", 110, 545, "tod", "Bold", 36),
    blk(110, 610, 1040, 120, LILA, beim("tod", "fahrlässige"), [("fahrlässige Tötung durch", "ExtraBold", 36, INK),
                                                             ("Unterlassen, §§ 222, 13 StGB", "ExtraBold", 36, INK)]),
    z("Prüfung nach demselben Schema", 110, 755, beim("tod", "demselben"), "Bold", 34),
    *requisit([("erg", ("ph", "gavel", 100, HOLZ), "Ergebnis", GRUEN),
               ("antrag", ("tabler", "file-text", 100, WEISS), "§ 230 StGB", WEISS),
               ("tod", ("tabler", "list-numbers", 100, WEISS), "Variante § 222", LILA)]),
    *zwei("BE", [("erg", "still"), ("tod", "sorge")], "SP", [("erg", "ernst"), ("tod", "sorge")]),
]))

# ===========================================================================================================================
# M Warum kein Vorsatz? Bewusste Fahrlässigkeit oder bedingter Vorsatz
# ===========================================================================================================================
LX0, RX0, SW = 110, 640, 510
folie([("vors", "Abgrenzung · bewusste Fahrlässigkeit oder bedingter Vorsatz?")], rechts_frei([
    *tafel("vors", "Warum kein Vorsatz?"),
    karte(LX0, 180, SW, 330, beim("vors", "Herr"), fill=HELLGRUEN, rund=18, schatten=6, rand=4),
    z("bewusste Fahrlässigkeit", LX0 + 25, 198, beim("vors", "bewusste"), "ExtraBold", 32, rechts=LX0 + SW - 10),
    z("Unfall für möglich", LX0 + 25, 262, beim("vors", "möglich"), size=30, rechts=LX0 + SW - 10),
    z("gehalten, aber ernsthaft", LX0 + 25, 304, beim("vors", "ernsthaft"), size=30, rechts=LX0 + SW - 10),
    z("darauf vertraut, dass", LX0 + 25, 346, beim("vors", "ernsthaft"), size=30, rechts=LX0 + SW - 10),
    z("nichts passiert", LX0 + 25, 388, beim("vors", "passiert"), size=30, rechts=LX0 + SW - 10),
    *okz("Herr Berger", 450, beim("vors", "bewusste"), "ExtraBold", 32, x=LX0 + 70),
    karte(RX0, 180, SW, 330, "event", fill=HELLROT, rund=18, schatten=6, rand=4),
    z("bedingter Vorsatz", RX0 + 25, 198, beim("event", "bedingter"), "ExtraBold", 32, rechts=RX0 + SW - 10),
    z("mit einer Verletzung", RX0 + 25, 262, beim("event", "mit"), size=30, rechts=RX0 + SW - 10),
    z("abgefunden", RX0 + 25, 304, beim("event", "abgefunden"), size=30, rechts=RX0 + SW - 10),
    zit("BGH 1 StR 474/19, Rn. 14", 110, 545, "event"),
    *requisit([("vors", ("tabler", "bulb", 100, GELB), "kein Vorsatz?", WEISS),
               ("event", ("tabler", "arrows-split", 100, WEISS), "Abgrenzung", WEISS)]),
    *stehend("BE", FX, [("vors", "denkt"), (beim("vors", "bewusste"), "ruhig")]),
]))

# ===========================================================================================================================
# N Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Vorsatz zuerst ausschließen"), ("tipp2", "Klausurtipp · Unterlassungsform beachten")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Zuerst das Vorsatzdelikt prüfen", 200, 200, beim("tipp", "Prüfe"), "Bold", 36),
    z("und den Vorsatz ablehnen.", 200, 255, beim("tipp", "lehne"), "Bold", 36),
    z("Erst dann das Fahrlässigkeitsdelikt.", 200, 320, beim("tipp", "Erst"), size=34),
    linienzug([(130, 400), (1130, 400)], "tipp2", breite=3),
    z("Unterlassungsform beachten:", 200, 430, "tipp2", "Bold", 36),
    z("Garantenstellung und hypothetische", 200, 490, beim("tipp2", "Garantenstellung"), size=34),
    z("Kausalität gehören in den Tatbestand.", 200, 540, beim("tipp2", "Garantenstellung"), size=34),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# O Prüfschema (Farben wie auf den Punkttafeln)
# ===========================================================================================================================
REIHEN = [("s1", None, 0, "I. Tatbestand"),
          ("s1a", 1, 1, "1. Erfolg"),
          ("s1b", 2, 1, "2. Handlung oder Unterlassen mit Garantenstellung (§ 13 StGB)"),
          ("s1c", 3, 1, "3. Kausalität"),
          ("s1d", 4, 1, "4. objektive Sorgfaltspflichtverletzung"),
          ("s1e", 5, 1, "5. objektive Vorhersehbarkeit"),
          ("s1f", 6, 1, "6. Pflichtwidrigkeitszusammenhang und Schutzzweck"),
          ("s2", "II", 0, "II. Rechtswidrigkeit"),
          ("s3", "III", 0, "III. Schuld: subjektive Sorgfaltspflichtverletzung"),
          ("s3", "III", 2, "und subjektive Vorhersehbarkeit")]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfschema: Fahrlässigkeitsdelikt"), 110, 90, "sch", 46),
           z("§§ 229, 222 StGB (bei Unterlassen i. V. m. § 13 StGB)", 110, 160, "sch", "Bold", 32, farbe=TEXT, rechts=1800)]
y = 235
for c, farbe, ebene, text in REIHEN:
    x = (130, 220, 220)[ebene]
    if farbe is not None and ebene != 2:
        ch = Image.new("RGBA", (34, 34))
        ImageDraw.Draw(ch).rounded_rectangle((1, 1, 32, 32), 8, fill=PUNKTFARBE[farbe], outline=INK, width=3)
        els_sch.append(El(ch, x - 50, y + 8, c, "pop", 0.0, None, name="farbpunkt"))
    els_sch.append(z(text, x, y, c, "ExtraBold" if ebene == 0 else "Regular", 38 if ebene == 0 else 34, rechts=1800))
    y += {0: 80, 1: 66, 2: 70}[ebene] if not (ebene == 0 and c == "s3") else 52
assert y <= 970, y
folie([("sch", "Prüfschema"), ("s1", "Prüfschema › I. Tatbestand"), ("s2", "Prüfschema › II. Rechtswidrigkeit"),
       ("s3", "Prüfschema › III. Schuld")], els_sch)

# ===========================================================================================================================
# P Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Fahrlässig handelt, wer die", 0)], [("gebotene Sorgfalt verletzt", "a"), (" und", 0)],
                 [("den Erfolg vorhersehen konnte.", 0)]], 750, 290, 44, "merke", {"a": beim("merke", "gebotene")}),
    *markertext([[("Zugerechnet wird ihm der Erfolg nur,", 0)], [("wenn er bei ", 0), ("pflichtgemäßem Verhalten", "b")],
                 [("ausgeblieben wäre.", 0)]], 750, 580, 42, "m2", {"b": beim("m2", "pflichtgemäßem")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
