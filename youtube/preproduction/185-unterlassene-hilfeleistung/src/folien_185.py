"""Folge 185 · Unterlassene Hilfeleistung § 323c: Muss ich jedem helfen? – Serienstandard Open Peeps (Katzenkönig).
Fall (fiktiv, ohne Ort, ohne echte Personen, ohne Bank-Logos): Im Vorraum einer Bankfiliale bricht ein älterer Mann vor den
Geldautomaten zusammen und bleibt bewusstlos liegen. In 20 Minuten steigen 4 Kunden über ihn hinweg (Herr Brauer, Frau Hauser,
Herr Kessel, Frau Weigel); dann wählt Frau Bühler den Notruf und bringt ihn in die stabile Seitenlage (positives Vorbild).
DARSTELLUNG: Der Mann liegt als ruhige Open-Peeps-Figur (Eyes Closed, als Ganzes gedreht), keine Verletzung, kein Blut.
Geldautomaten und Glastür aus Grundformen, keine Logos.
Szenen laut ../SZENENPLAN.md: A Vorraum (Kunden 1–4, Frau Bühler hilft), A3 Krankenhaus und Frage, B Sachverhalt,
C Wortlaut § 323c Abs. 1, D echtes Unterlassungsdelikt, E 1. Unglücksfall, F 2. Nichthilfeleisten, G 3. Erforderlichkeit,
H 4. Zumutbarkeit, I 5. Vorsatz, J § 13 und Abs. 2, K Lösung je Kunde, L Klausurtipp (Lexi), M Prüfschema, N Merksatz (Lexi).
Jeder Prüfungspunkt hat eine eigene Farbe (PUNKTFARBE), gleich auf den Punkttafeln und im Prüfschema.
Zwei Handlungsgeräusche: Geldautomat zählt Scheine (Herr Brauer hebt Geld ab), Tastentöne beim Notruf (Frau Bühler)
(../geraeusche_herkunft.json).
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/
punkt als eigene Kopie aus Folge 182 (gemeinsame Dateien unverändert); neu: automat(), tuer(), lieg_hoehe(), marken_aus().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_185/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_185/" in n:
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
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 04.10.2026, Folge 185), als Zitat mit Normangabe;
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
NAME = {"BR": "Herr Brauer", "HA": "Frau Hauser", "KE": "Herr Kessel", "WE": "Frau Weigel", "BU": "Frau Bühler",
        "MA": "älterer Mann"}
NFARBE = {"BR": GRUEN, "HA": LILA, "KE": BLAU, "WE": ORANGE, "BU": TUERKIS, "MA": WEISS}
FIGDIR = bausteine.FIG + bausteine.FIGORDNER


def lieg_hoehe(name, stehhoehe, kopf=1.0):
    """Höhe einer gedrehten (liegenden) bzw. knienden Ansicht, damit der Kopf so groß ist wie bei der stehenden Figur
    (Kopfmaß an den PNGs gemessen: Seitenlage 0,72, kniend 0,683 der Skala einer stehenden Figur)."""
    im = Image.open(FIGDIR + name + ".png")
    return int(round(im.height * stehhoehe / 1185 * kopf))


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
    return [*stehend(a, X1, folge_a), *stehend(b, X2, folge_b)]


PUNKTFARBE = {1: GELB, 2: LILA, 3: BLAU, 4: ROT, 5: GRUEN, "II": TUERKIS, "III": PINK}


def punkt(nr, text, cue, y=170, h=78, size=36):
    return blk(110, y, 1040, h, PUNKTFARBE[nr], cue, [(text, "ExtraBold", size, INK)])


def marken_aus(zeilen, liste):
    """[(phrase, cue)] → [(zeile, phrase, cue)]; jede Phrase muss vollständig in einer Zeile stehen."""
    aus = []
    for ph, c in liste:
        zi = next((i for i, t in enumerate(zeilen) if ph in t), None)
        assert zi is not None, f"Marker {ph!r} nicht in einer Zeile: {zeilen}"
        aus.append((zi, ph, c))
    return aus


# ===========================================================================================================================
# Bühne der Fallszenen: Vorraum einer Bankfiliale (Grundformen, keine Logos): 2 Geldautomaten links, Glastür rechts
# ===========================================================================================================================
BODEN, FH = 880, 470
HELLGRAU = (226, 226, 222, 255)
GLAS = (226, 238, 250, 255)


def automat(cx, c):
    """Geldautomat aus Grundformen: Gehäuse, Bildschirm, Tastenfeld, Kartenschlitz, Geldausgabe (ohne Logo)."""
    s, w, h = 2, 170, 330
    im = Image.new("RGBA", ((w + 8) * s, (h + 8) * s))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((2 * s, 2 * s, (w + 2) * s, (h + 2) * s), 14 * s, fill=HELLGRAU, outline=INK, width=5 * s)
    d.rounded_rectangle((24 * s, 26 * s, (w - 20) * s, 120 * s), 8 * s, fill=BLAU[:3] + (255,), outline=INK, width=4 * s)
    for r in range(3):
        for q in range(3):
            x0, y0 = (40 + q * 34) * s, (148 + r * 30) * s
            d.rounded_rectangle((x0, y0, x0 + 24 * s, y0 + 20 * s), 4 * s, fill=WEISS, outline=INK, width=3 * s)
    d.rounded_rectangle((40 * s, 252 * s, (w - 36) * s, 268 * s), 6 * s, fill=INK)          # Geldausgabe
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    return El(im, cx - im.width / 2, BODEN - im.height + 4, c, "cut", 0.0, None, name="automat")


def tuer(c):
    """Glastür des Vorraums (Grundform)."""
    s, w, h = 2, 200, 500
    im = Image.new("RGBA", ((w + 8) * s, (h + 8) * s))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((2 * s, 2 * s, (w + 2) * s, (h + 2) * s), 8 * s, fill=GLAS, outline=INK, width=6 * s)
    d.line(((w // 2 + 2) * s, 6 * s, (w // 2 + 2) * s, h * s), fill=INK, width=4 * s)
    d.rounded_rectangle(((w // 2 - 22) * s, 220 * s, (w // 2 - 12) * s, 300 * s), 4 * s, fill=INK)
    d.rounded_rectangle(((w // 2 + 16) * s, 220 * s, (w // 2 + 26) * s, 300 * s), 4 * s, fill=INK)
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    return El(im, 1740 - im.width / 2, BODEN - im.height + 4, c, "cut", 0.0, None, name="tuer")


AX1, AX2 = 190, 380                          # Geldautomaten
MX_S, MX_L = 600, 900                        # Mann stehend (am Automaten), liegend (Mitte)
KX = 520                                     # Kunde am Automaten (rechts vor dem 2. Automaten)
TX = 1740                                    # Tür
H_LIEGT = lieg_hoehe("MA_liegt", FH)
H_SEITE = lieg_hoehe("MA_seite", FH, 0.72)
H_KNIET = lieg_hoehe("BU_kniet", FH, 0.683)
BX = 530                                     # Frau Bühler kniet am Kopf des Mannes (blickt nach rechts)
_h = lambda e: hart(e)
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
GEHT = 1.2                                   # Gehzeit Tür → Automat (über den Mann hinweg)
RP = 1100                                    # Pillen der Fallszene rechts oben


def plus(c, s):
    return (c[0], round(c[1] + s, 3)) if isinstance(c, tuple) else (c, s)


def kommt(name, ziel, start, dx, hoehe=FH, bis=None, dauer=GEHT):
    """Figur läuft von der Tür (bzw. ziel+dx) zum Ziel; der Weg führt über den liegenden Mann hinweg."""
    return bewegt(peep_voll(name, ziel, BODEN, hoehe, start, anim="cut", bis=bis), start, plus(start, dauer), dx, 0)


def schild_mit(k, ziel, start, dx, bis, dauer=GEHT):
    """Namensschild, das mit der gehenden Figur mitläuft (ab ihrem ersten Auftritt)."""
    return bis_(bewegt(ns(NAME[k], ziel, BODEN, start, NFARBE[k], anim="cut"), start, plus(start, dauer), dx, 0), bis)


# ===========================================================================================================================
# A Fall: der Vorraum, 4 Kunden steigen über den Mann hinweg, Frau Bühler hilft
# ===========================================================================================================================
ZUSAMMEN = beim("mann", "zusammen")
B_DA = "brauer"
B_AM = plus(B_DA, GEHT)
H_GEHT = beim("hauser", "geht")
K_DA = "kessel"
W_GEHT = beim("weigel", "geht", nr=1)
BU_DA = "buehler"
BU_KNIET = beim("buehler", "kniet")
SEITE = beim("seite", "Seitenlage")
folie([(NULL, "Fall · Im Vorraum der Bank"), ("mann", "Fall · Ein Mann bricht zusammen"),
       ("brauer", "Fall · Kunde 1: Herr Brauer"), ("hauser", "Fall · Kundin 2: Frau Hauser"),
       ("kessel", "Fall · Kunde 3: Herr Kessel"), ("weigel", "Fall · Kundin 4: Frau Weigel"),
       ("buehler", "Fall · Frau Bühler hilft"), ("seite", "Fall · Stabile Seitenlage")], [
    _h(boden(BODEN, NULL)), _h(automat(AX1, NULL)), _h(automat(AX2, NULL)), _h(tuer(NULL)),
    _h(pl("Montagmorgen: Vorraum einer Bankfiliale", RP, 30, NULL, fill=GELB, size=36)),
    # der ältere Mann: steht am Automaten, bricht zusammen, liegt bewusstlos (ruhige Figur), später stabile Seitenlage
    _h(peep_voll("MA_steht", MX_S, BODEN, FH, NULL, anim="cut", bis=ZUSAMMEN)),
    _h(bis_(ns("älterer Mann", MX_S, BODEN, NULL, WEISS, anim="cut"), ZUSAMMEN)),
    peep_voll("MA_liegt", MX_L, BODEN, H_LIEGT, ZUSAMMEN, anim="cut", bis=SEITE),
    peep_voll("MA_seite", MX_L + 40, BODEN, H_SEITE, SEITE, anim="cut"),
    ns("älterer Mann", MX_L, BODEN, ZUSAMMEN, WEISS, anim="cut"),
    pl("Ein älterer Mann bricht zusammen.", RP, 110, ZUSAMMEN, fill=WEISS, size=34, bis="brauer"),
    pl("bewusstlos am Boden", RP, 190, beim("liegt", "bewusstlos"), fill=HELLROT, size=34, bis="brauer"),
    pl("In 20 Minuten: 4 Kunden", RP, 270, beim("vier", "zwanzig"), fill=WEISS, size=34, bis="brauer"),
    # Kunde 1: Herr Brauer
    kommt("BR_eilig", KX, B_DA, TX - KX, bis=beim("brauer", "hebt")),
    szene(peep_voll("BR_ruhig", KX, BODEN, FH, beim("brauer", "hebt"), anim="cut", bis="br1"), "185geld*", 0.8, 0.1),
    ficon("tabler", "cash-banknote", AX2, BODEN - 70, 70, beim("brauer", "hebt"), fuell=GRUEN, bis="hauser"),
    *redet("BR_redet_r", KX, BODEN, FH, "br1", "hauser"),
    schild_mit("BR", KX, B_DA, TX - KX, "hauser"),
    pl("Herr Brauer steigt über ihn hinweg", RP, 110, beim("brauer", "steigt"), fill=GRUEN, size=34, bis="hauser"),
    pl("und hebt Geld ab.", RP, 190, beim("brauer", "hebt"), fill=WEISS, size=34, bis="hauser"),
    blase("sprech", 560, 200, "br1", 700, 250, inhalt=["Ich hab gleich", "einen Termin."], textsize=38,
          figur=("BR_redet_r", KX, BODEN, FH), bis="hauser"),
    # Kundin 2: Frau Hauser (an der Tür, sieht ihn, zögert, geht zum Automaten)
    *fig("HA", 1450, BODEN, FH, [("hauser", "ruhig"), (beim("hauser", "zögert"), "sorge")], bis=H_GEHT, erst="cut"),
    bis_(ns("Frau Hauser", 1450, BODEN, "hauser", LILA, anim="cut"), H_GEHT),
    kommt("HA_ruhig", KX, H_GEHT, 1450 - KX, bis="ha1"),
    *redet("HA_redet_r", KX, BODEN, FH, "ha1", "kessel"),
    schild_mit("HA", KX, H_GEHT, 1450 - KX, "kessel"),
    pl("Frau Hauser sieht ihn, zögert kurz", RP, 110, "hauser", fill=LILA, size=34, bis="kessel"),
    pl("und geht zum Automaten.", RP, 190, H_GEHT, fill=WEISS, size=34, bis="kessel"),
    blase("sprech", 600, 200, "ha1", 720, 250, inhalt=["Da kommen doch", "gleich andere."], textsize=38,
          figur=("HA_redet_r", KX, BODEN, FH), bis="kessel"),
    # Kunde 3: Herr Kessel (kurzer Blick)
    kommt("KE_ruhig", KX, K_DA, TX - KX, bis=beim("kessel", "Blick")),
    peep_voll("KE_denkt_r", KX, BODEN, FH, beim("kessel", "Blick"), anim="cut", bis="ke1"),
    *redet("KE_redet_r", KX, BODEN, FH, "ke1", "weigel"),
    schild_mit("KE", KX, K_DA, TX - KX, "weigel"),
    pl("Herr Kessel: ein kurzer Blick auf ihn", RP, 110, beim("kessel", "kurzen"), fill=BLAU, size=34, bis="weigel"),
    blase("sprech", 560, 200, "ke1", 700, 250, inhalt=["Der schläft", "doch nur."], textsize=40,
          figur=("KE_redet_r", KX, BODEN, FH), bis="weigel"),
    # Kundin 4: Frau Weigel (bleibt bei den Füßen stehen, geht wieder)
    kommt("WE_ruhig", 1300, "weigel", TX - 1300, bis=beim("weigel", "stehen"), dauer=0.8),
    peep_voll("WE_sorge", 1300, BODEN, FH, beim("weigel", "stehen"), anim="cut", bis=W_GEHT),
    schild_mit("WE", 1300, "weigel", TX - 1300, W_GEHT, dauer=0.8),
    pl("Frau Weigel bleibt kurz stehen.", RP, 110, beim("weigel", "bleibt"), fill=ORANGE, size=34, bis="buehler"),
    pl("nie Erste Hilfe gelernt: geht wieder", RP, 190, beim("weigel", "Sie"), fill=WEISS, size=34, bis="buehler"),
    # Frau Bühler hilft: kommt, kniet sich zum Kopf, spricht ihn an, wählt den Notruf, stabile Seitenlage
    kommt("BU_sorge", 640, BU_DA, TX - 640, bis=BU_KNIET, dauer=1.0),
    schild_mit("BU", 640, BU_DA, TX - 640, BU_KNIET, dauer=1.0),
    peep_voll("BU_kniet_r", BX, BODEN, H_KNIET, BU_KNIET, anim="cut", bis="bu1"),
    *redet("BU_kniet_redet_r", BX, BODEN, H_KNIET, "bu1", "seite"),
    peep_voll("BU_kniet_r", BX, BODEN, H_KNIET, "seite", anim="cut"),
    ns("Frau Bühler", BX, BODEN, BU_KNIET, TUERKIS, anim="cut"),
    pl("Frau Bühler kniet sich zu ihm", RP, 110, BU_KNIET, fill=TUERKIS, size=34, bis="seite"),
    pl("und spricht ihn an.", RP, 190, beim("buehler", "spricht"), fill=WEISS, size=34, bis="seite"),
    szene(ficon("fluent-emoji-flat", "mobile-phone", BX + 120, 615, 70, beim("buehler", "Notruf")), "185notruf*", 0.8, 0.05),
    pl("Sie wählt den Notruf.", RP, 270, beim("buehler", "wählt"), fill=GRUEN, size=34, bis="seite"),
    blase("sprech", 700, 240, "bu1", 800, 250, inhalt=["Hier liegt ein Mann", "bewusstlos am Boden.", "Er atmet."],
          textsize=36, figur=("BU_kniet_redet_r", BX, BODEN, H_KNIET), bis="seite"),
    pl("Stabile Seitenlage", RP, 110, SEITE, fill=GRUEN, size=36),
    pl("Sie bleibt bei ihm.", RP, 190, beim("seite", "bleibt"), fill=WEISS, size=34),
])

# ===========================================================================================================================
# A3 Fall: Krankenhaus, die Frage (die 4 Kunden)
# ===========================================================================================================================
ERHOLT = beim("rtw", "dort")
folie([("rtw", "Fall · Rettungsdienst und Krankenhaus"), ("frage", "Die Frage · Strafbar, wer nicht hilft?")], [
    hart(boden(BODEN, "rtw")),
    bis_(ficon("fluent-emoji-flat", "ambulance", 420, BODEN, 360, "rtw"), "frage"),
    bis_(ficon("tabler", "building-hospital", 980, BODEN, 330, beim("rtw", "Krankenhaus"), fuell=WEISS), "frage"),
    pl("Der Rettungsdienst bringt ihn ins Krankenhaus.", 70, 30, "rtw", fill=WEISS, size=34, bis="frage"),
    bis_(peep_voll("MA_froh", 1450, BODEN, FH, ERHOLT, anim="pop"), "frage"),
    bis_(ns("älterer Mann", 1450, BODEN, ERHOLT, WEISS, d=0.1), "frage"),
    pl("Dort erholt er sich.", 70, 110, ERHOLT, fill=GRUEN, size=34, bis="frage"),
    # die Frage: die 4 Kunden
    *[e for k, x, m in (("BR", 330, "still"), ("HA", 730, "still"), ("KE", 1130, "denkt"), ("WE", 1530, "still"))
      for e in (peep_voll(f"{k}_{m}", x, BODEN, FH, "frage", anim="pop"), ns(NAME[k], x, BODEN, "frage", NFARBE[k], d=0.1))],
    pl("Haben sich die 4 Kunden strafbar gemacht?", 70, 30, "frage", fill=WEISS, size=36),
    pl("Muss man wirklich jedem helfen?", 70, 110, "frage2", fill=PINK, size=36),
])

# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_185(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 205
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=34, zeilenabstand=1.30)
        els += e; y += 16
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=34))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_185("sv", [
    "Ein Montagmorgen im Vorraum einer Bankfiliale: Ein älterer Mann bricht vor den Geldautomaten zusammen und bleibt "
    "bewusstlos am Boden liegen. In den nächsten 20 Minuten kommen 4 Kunden. Herr Brauer steigt über den Mann hinweg, hebt "
    "Geld ab und sagt: „Ich hab gleich einen Termin.“ Frau Hauser sieht den Mann, zögert kurz und geht auch zum Automaten: "
    "„Da kommen doch gleich andere.“ Herr Kessel wirft einen kurzen Blick auf ihn: „Der schläft doch nur.“ Frau Weigel "
    "bleibt kurz stehen. Sie hat nie Erste Hilfe gelernt und geht wieder.",
    "Erst die 5. Kundin, Frau Bühler, kniet sich zu ihm, spricht ihn an und wählt den Notruf. Sie bringt ihn in die stabile "
    "Seitenlage und bleibt bei ihm. Der Rettungsdienst bringt ihn ins Krankenhaus, dort erholt er sich.",
], "Haben sich die 4 Kunden strafbar gemacht?")

# ===========================================================================================================================
# C § 323c Abs. 1 StGB (Wortlautkarte, vollständig vorgelesen)
# ===========================================================================================================================
W323 = umbruch("„(1) Wer bei Unglücksfällen oder gemeiner Gefahr oder Not nicht Hilfe leistet, obwohl dies erforderlich und "
               "ihm den Umständen nach zuzumuten, insbesondere ohne erhebliche eigene Gefahr und ohne Verletzung anderer "
               "wichtiger Pflichten möglich ist, wird mit Freiheitsstrafe bis zu einem Jahr oder mit Geldstrafe bestraft.“",
               34, 1020)
w323, w323_y = wortlaut(80, 170, 1100, W323, "§ 323c Abs. 1 StGB", "p323", marken=marken_aus(W323, [
    ("Unglücksfällen", beim("p323", "Unglücksfällen")), ("Hilfe", beim("p323", "Hilfe")),
    ("erforderlich", beim("p323", "erforderlich")), ("zuzumuten", beim("p323", "zuzumuten")),
    ("erhebliche", beim("p323", "erhebliche")), ("anderer", beim("p323", "anderer")),
    ("bis zu einem Jahr", beim("strafe", "bis"))]), size=34)
folie([("p323", "Die Norm · § 323c Abs. 1 StGB"), ("strafe", "Die Norm · Strafrahmen, § 323c Abs. 1 StGB")], rechts_frei([
    *tafel("p323", "§ 323c StGB: unterlassene Hilfeleistung", size=44),
    *w323,
    blk(110, w323_y + 36, 1040, 78, GELB, beim("strafe", "Freiheitsstrafe"),
        [("Strafrahmen: bis 1 Jahr oder Geldstrafe", "ExtraBold", 36, INK)]),
    *requisit([("p323", ("tabler", "book", 100, WEISS), "§ 323c Abs. 1 StGB", GELB),
               (beim("strafe", "Freiheitsstrafe"), ("tabler", "scale", 100, WEISS), "bis 1 Jahr oder Geldstrafe", WEISS)]),
    *stehend("BU", FX, [("p323", "ruhig")]),
]))

# ===========================================================================================================================
# D Echtes Unterlassungsdelikt
# ===========================================================================================================================
folie([("echt", "Einordnung · echtes Unterlassungsdelikt"), ("jeder", "Einordnung · Pflicht für jeden"),
       ("kein", "Einordnung · auch vergebliche Hilfe ist geschuldet")], rechts_frei([
    *tafel("echt", "Echtes Unterlassungsdelikt"),
    *okz("Bestraft wird das Nichthelfen selbst.", 190, beim("echt", "Bestraft"), "Bold", 36, x=160),
    zit("BGH 2 StR 109/20, Rn. 18", 160, 245, beim("echt", "Nichthelfen")),
    *okz("Die Pflicht trifft jeden,", 320, "jeder", "Bold", 36, x=160),
    z("auch ohne Garantenstellung.", 160, 372, beim("jeder", "auch"), "Bold", 36),
    zit("vgl. BGH 2 StR 563/18, Rn. 14, 17", 160, 427, beim("jeder", "Garantenstellung")),
    *okz("Egal, ob die Hilfe am Ende", 505, "kein", "Bold", 36, x=160),
    z("etwas geändert hätte.", 160, 557, beim("kein", "etwas"), "Bold", 36),
    zit("BGH 1 StR 373/19, Rn. 11", 160, 612, beim("kein", "geändert")),
    *requisit([("echt", ("tabler", "hand-stop", 100, WEISS), "Nichthelfen", HELLROT),
               ("jeder", ("tabler", "users", 110, WEISS), "jeder", GELB),
               ("kein", ("tabler", "first-aid-kit", 100, WEISS), "Hilfe auch, wenn vergeblich", WEISS)]),
    *zwei("KE", [("echt", "ruhig"), ("kein", "denkt")], "WE", [("echt", "sorge"), ("kein", "still")]),
]))

# ===========================================================================================================================
# E I. 1. Unglücksfall (objektivierte ex-ante-Sicht)
# ===========================================================================================================================
PT = "I. Tatbestand"
H_LIEGT_T = lieg_hoehe("MA_liegt", FR)
folie([("ungl", f"{PT} › 1. Unglücksfall"), ("exante", f"{PT} › 1. Unglücksfall: Sicht ex ante"),
       ("ungl2", f"{PT} › 1. Unglücksfall (+)")], rechts_frei([
    *tafel("ungl", "I. Tatbestand: Unglücksfall"),
    punkt(1, "1. Unglücksfall", "ungl"),
    z("Ereignis, das plötzlich eintritt, erheblichen", 110, 275, beim("def", "Ereignis"), "Bold", 32),
    z("Schaden an Menschen oder Sachen anrichtet und", 110, 323, beim("def", "Schaden"), "Bold", 32),
    z("weiteren Schaden zu verursachen droht", 110, 371, beim("def", "weiteren"), "Bold", 32),
    zit("BGH 4 StR 71/11, Rn. 21 (BGHSt 57, 42)", 110, 423, beim("def", "droht")),
    *okz("Schon ein drohender erheblicher Schaden genügt.", 478, "droht", size=32, x=160),
    zit("BGH 2 StR 115/15, Rn. 10", 160, 528, beim("droht", "genügt")),
    blk(110, 580, 1040, 120, GELB, "exante", [("ex ante: Sicht eines verständigen Beobachters", "ExtraBold", 32, INK),
                                              ("im Moment der Hilfe", "ExtraBold", 32, INK)]),
    zit("BGH 1 StR 373/19, Rn. 11 f.", 110, 712, beim("exante", "verständiger")),
    *okz("Bricht zusammen, reagiert nicht: Unglücksfall", 768, "ungl2", "Bold", 34, x=160),
    *requisit([("ungl", ("tabler", "alert-triangle", 100, GELB), "Unglücksfall?", WEISS),
               ("exante", ("tabler", "eye", 100, WEISS), "ex ante", GELB),
               ("ungl2", ("tabler", "alert-triangle", 100, GELB), "Unglücksfall (+)", GRUEN)]),
    peep_voll("MA_liegt", FX, FB, H_LIEGT_T, "ungl", anim="pop"),
    ns("älterer Mann", FX, FB, "ungl", WEISS, d=0.1),
]))

# ===========================================================================================================================
# F I. 2. Nichthilfeleisten
# ===========================================================================================================================
folie([("nicht", f"{PT} › 2. Nichthilfeleisten"), ("was", f"{PT} › 2. Welche Hilfe ist geschuldet?")], rechts_frei([
    *tafel("nicht", "I. Tatbestand: Nichthilfeleisten"),
    punkt(2, "2. Nichthilfeleisten", "nicht"),
    *okz("Die Kunden leisten keine Hilfe.", 285, beim("nicht", "Die"), "Bold", 36, x=160),
    z("Geschuldet ist die Hilfe, die dir möglich ist,", 110, 385, "was", "Bold", 34),
    z("oft schon der Notruf.", 110, 437, beim("was", "oft"), "Bold", 34),
    zit("BGH 5 StR 363/15, Rn. 5; 1 StR 21/93, Rn. 5", 110, 492, beim("was", "Notruf")),
    *requisit([("nicht", ("tabler", "hand-stop", 100, WEISS), "keine Hilfe", HELLROT),
               ("was", ("fluent-emoji-flat", "mobile-phone", 90, None), "Notruf", GRUEN)]),
    *zwei("BR", [("nicht", "still")], "WE", [("nicht", "still"), ("was", "sorge")]),
]))

# ===========================================================================================================================
# G I. 3. Erforderlichkeit
# ===========================================================================================================================
folie([("erf", f"{PT} › 3. Erforderlichkeit"), ("entf", f"{PT} › 3. Wann entfällt die Erforderlichkeit?"),
       ("erf2", f"{PT} › 3. Erforderlichkeit (+)")], rechts_frei([
    *tafel("erf", "I. Tatbestand: Erforderlichkeit"),
    punkt(3, "3. Erforderlichkeit", "erf"),
    *okz("Andere könnten helfen? Ändert nichts,", 275, "andere", "Bold", 34, x=160),
    z("solange keine sofortige Hilfe von anderer", 160, 325, beim("andere", "solange"), "Bold", 34),
    z("Seite gesichert ist.", 160, 375, beim("andere", "Seite"), "Bold", 34),
    zit("BGH 2 StR 109/20, Rn. 18", 160, 430, beim("andere", "gesichert")),
    z("Nicht mehr erforderlich:", 110, 490, "entf", "Bold", 34),
    *neinz("schon ausreichend geholfen", 545, beim("entf", "schon"), size=32, x=210),
    zit("BGH 5 StR 363/15, Rn. 6", 210, 595, beim("entf", "geholfen")),
    *neinz("oder der Verunglückte ist sicher tot", 645, "tot", size=32, x=210),
    zit("BGH 1 StR 373/19, Rn. 11", 210, 695, beim("tot", "tot")),
    blk(110, 755, 1040, 78, PUNKTFARBE[3], "erf2", [("20 Minuten hilft niemand: erforderlich", "ExtraBold", 34, INK)]),
    *requisit([("erf", ("tabler", "first-aid-kit", 100, BLAU), "Hilfe nötig?", BLAU),
               ("andere", ("tabler", "users", 110, WEISS), "andere könnten helfen", WEISS),
               ("entf", ("tabler", "first-aid-kit", 100, GRUEN), "Hilfe läuft schon", GRUEN),
               ("erf2", ("tabler", "clock", 100, WEISS), "20 Minuten", HELLROT)]),
    *stehend("HA", FX, [("erf", "ruhig"), ("andere", "sorge"), ("erf2", "still")]),
]))

# ===========================================================================================================================
# H I. 4. Zumutbarkeit (Wortlaut-Beispiele; im Tatbestand)
# ===========================================================================================================================
folie([("zum", f"{PT} › 4. Zumutbarkeit"), ("termin", f"{PT} › 4. Zumutbarkeit: Termin? Notruf?"),
       ("tb", f"{PT} › 4. Zumutbarkeit im Tatbestand")], rechts_frei([
    *tafel("zum", "I. Tatbestand: Zumutbarkeit"),
    punkt(4, "4. Zumutbarkeit", "zum"),
    z("Das Gesetz nennt 2 Beispiele:", 110, 272, "zumw", "Bold", 34),
    z("„ohne erhebliche eigene Gefahr“", 160, 324, beim("zumw", "ohne"), size=34),
    z("„ohne Verletzung anderer wichtiger Pflichten“", 160, 374, "pfl", size=34),
    *okz("Termin bei der Arbeit: keine solche Pflicht", 448, "termin", "Bold", 32, x=160),
    *okz("Notruf: auch ohne Kenntnisse in Erster Hilfe", 513, "anruf", "Bold", 32, x=160),
    z("und ganz ohne eigene Gefahr", 160, 563, beim("anruf", "ganz"), "Bold", 32),
    blk(110, 630, 1040, 78, PUNKTFARBE[4], "tb", [("Zumutbarkeit im Tatbestand prüfen", "ExtraBold", 34, INK)]),
    zit("BGH 5 StR 132/18, Rn. 46 (BGHSt 64, 121)", 110, 722, beim("tb", "Tatbestand")),
    *requisit([("zum", ("tabler", "scale", 100, ROT), "zumutbar?", ROT),
               ("zumw", ("tabler", "shield", 100, WEISS), "eigene Gefahr?", WEISS),
               ("pfl", ("tabler", "briefcase", 100, WEISS), "andere wichtige Pflichten?", WEISS),
               ("termin", ("tabler", "calendar", 100, WEISS), "Termin: keine solche Pflicht", HELLROT),
               ("anruf", ("fluent-emoji-flat", "mobile-phone", 90, None), "Notruf: ohne Kenntnisse", GRUEN),
               ("tb", ("tabler", "list-check", 100, WEISS), "Tatbestand", ROT)]),
    *zwei("BR", [("zum", "ruhig"), ("termin", "eilig"), ("anruf", "still")], "WE", [("zum", "ruhig"), ("anruf", "sorge")]),
]))

# ===========================================================================================================================
# I I. 5. Vorsatz (Irrtum, § 16), keine Fahrlässigkeitsstrafbarkeit
# ===========================================================================================================================
folie([("vors", f"{PT} › 5. Vorsatz"), ("irrt", f"{PT} › 5. Irrtum über den Unglücksfall, § 16 StGB"),
       ("fahrl", f"{PT} › 5. Fahrlässigkeit nicht strafbar")], rechts_frei([
    *tafel("vors", "I. Tatbestand: Vorsatz"),
    punkt(5, "5. Vorsatz", "vors"),
    z("Unglücksfall erkannt und die Umstände, die", 110, 272, beim("vors", "Der"), "Bold", 32),
    z("Hilfe erforderlich und zumutbar machen", 110, 320, beim("vors", "Hilfe"), "Bold", 32),
    zit("vgl. BGH 2 StR 115/15, Rn. 12", 110, 372, beim("vors", "zumutbar")),
    *okz("Bedingter Vorsatz genügt.", 430, "bed", "Bold", 34, x=160),
    z("Glaubt er wirklich, der Mann schlafe nur?", 110, 505, "irrt", "Bold", 34),
    *neinz("Irrtum über den Unglücksfall", 562, beim("irrt", "irrt"), size=32, x=160),
    *neinz("kein Vorsatz, § 16 Abs. 1 StGB", 622, beim("irrt", "Dann"), size=32, x=160),
    *neinz("fahrlässig: nicht strafbar (§ 15 StGB)", 700, "fahrl", "Bold", 32, x=160),
    *requisit([("vors", ("tabler", "eye", 100, GRUEN), "erkannt?", GRUEN),
               ("irrt", ("tabler", "zzz", 100, WEISS), "„schläft doch nur“", WEISS),
               ("fahrl", ("tabler", "ban", 100, WEISS), "keine Fahrlässigkeit", WEISS)]),
    *stehend("KE", FX, [("vors", "ruhig"), ("irrt", "denkt"), ("fahrl", "still")]),
]))

# ===========================================================================================================================
# J Abgrenzung § 13 (ein Satz), § 323c Abs. 2 (Wortlautkarte)
# ===========================================================================================================================
W2 = umbruch("„(2) Ebenso wird bestraft, wer in diesen Situationen eine Person behindert, die einem Dritten Hilfe leistet "
             "oder leisten will.“", 34, 1020)
w2, w2_y = wortlaut(80, 470, 1100, W2, "§ 323c Abs. 2 StGB", "abs2",
                    marken=marken_aus(W2, [("behindert", beim("abs2", "behindert"))]), size=34)
folie([("p13", "Abgrenzung · Garant: zusätzlich § 13 StGB"), ("abs2", "§ 323c Abs. 2 StGB · Behinderung von Helfern")],
      rechts_frei([
    *tafel("p13", "§ 13 StGB und § 323c Abs. 2"),
    z("Garant, etwa als Vater?", 110, 180, "p13", "Bold", 36),
    z("Zusätzlich: unechtes Unterlassen, § 13 StGB", 110, 236, beim("p13", "zusätzlich"), "Bold", 34),
    z("Videos: „Unterlassungsdelikt“, „Garantenstellung“", 110, 292, beim("p13", "mehr"), "Bold", 30, farbe=TEXT),
    linienzug([(130, 410), (1130, 410)], "abs2", breite=3),
    *w2,
    *requisit([("p13", ("tabler", "shield", 100, LILA), "Garant: § 13 StGB", LILA),
               ("abs2", ("tabler", "hand-stop", 100, WEISS), "Helfer behindern", HELLROT)]),
    *stehend("BU", FX, [("p13", "ruhig"), ("abs2", "sorge")]),
]))

# ===========================================================================================================================
# K Lösung je Kunde
# ===========================================================================================================================
def zeile_l(name, farbe, text, y, c, wort, ergebnis=None, ergebnis_cue=None, text2=None, c2=None):
    els = [pl(name, 110, y, c, fill=farbe, size=30), z(text, 400, y + 6, beim(c, wort), size=30, rechts=1150)]
    if text2:
        els.append(z(text2, 400, y + 52, c2, size=30, rechts=1150))
    if ergebnis:
        els.append(pl(ergebnis, 1150, y + (52 if text2 else 0) + 50, ergebnis_cue, fill=HELLROT, size=28, anker="r"))
    return els


folie([("loes", "Lösung"), ("l1", "Lösung · Herr Brauer"), ("l2", "Lösung · Frau Hauser"), ("l3", "Lösung · Herr Kessel"),
       ("l4", "Lösung · Frau Weigel"), ("l5", "Lösung · Frau Bühler")], rechts_frei([
    *tafel("loes", "Lösung: die 4 Kunden"),
    *zeile_l("Herr Brauer", GRUEN, "Termin macht Hilfe nicht unzumutbar.", 180, "l1", "Sein", "strafbar",
             beim("l1", "Strafbar")),
    *zeile_l("Frau Hauser", LILA, "Andere könnten kommen: bleibt erforderlich.", 315, "l2", "Dass", "strafbar",
             beim("l2", "Strafbar")),
    *zeile_l("Herr Kessel", BLAU, "glaubt an Schlafenden: kein Vorsatz", 450, "l3", "Glaubt", "strafbar", beim("l3b", "strafbar"),
             text2="hält Notfall für möglich, nimmt es in Kauf:", c2="l3b"),
    *zeile_l("Frau Weigel", ORANGE, "Den Notruf hätte sie wählen können.", 635, "l4", "Den", "strafbar",
             beim("l4", "Strafbar")),
    pl("Frau Bühler", 110, 770, "l5", fill=TUERKIS, size=30),
    *okz("hat genau das Richtige getan.", 776, beim("l5", "genau"), "Bold", 30, x=445),
    *stehend("BR", FX, [("l1", "still")], bis="l2"),
    *stehend("HA", FX, [("l2", "still")], bis="l3"),
    *stehend("KE", FX, [("l3", "denkt"), ("l3b", "still")], bis="l4"),
    *stehend("WE", FX, [("l4", "still")], bis="l5"),
    *stehend("BU", X1, [("l5", "froh")]),
    peep_voll("MA_froh", X2, FB, FR, "l5", anim="pop"),
    ns("älterer Mann", X2, FB, "l5", WEISS, d=0.1),
]))

# ===========================================================================================================================
# L Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Ohne Garant an § 323c StGB denken"), ("tipp2", "Klausurtipp · Zumutbarkeit im Tatbestand")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Keine Garantenstellung?", 200, 200, beim("tipp", "Fehlt"), "Bold", 36),
    z("Dann § 323c StGB nicht vergessen.", 200, 255, beim("tipp", "vergiss"), "Bold", 36),
    z("Wegen übersehener unterlassener Hilfeleistung", 200, 320, beim("tipp", "Wegen"), size=32),
    z("hob der BGH schon Freisprüche auf.", 200, 368, beim("tipp", "Freisprüche"), size=32),
    zit("z. B. BGH 4 StR 71/11, Rn. 20; 1 StR 21/93, Rn. 4", 200, 420, beim("tipp", "Freisprüche")),
    linienzug([(130, 490), (1130, 490)], "tipp2", breite=3),
    z("Zumutbarkeit im Tatbestand prüfen,", 200, 520, "tipp2", "Bold", 36),
    z("nicht erst in der Schuld.", 200, 575, beim("tipp2", "nicht"), "Bold", 36),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# M Prüfschema (Farben wie auf den Punkttafeln)
# ===========================================================================================================================
REIHEN = [("s1", None, 0, "I. Tatbestand"),
          ("s1a", 1, 1, "1. Unglücksfall, gemeine Gefahr oder Not (Sicht ex ante)"),
          ("s1b", 2, 1, "2. Nichthilfeleisten (die mögliche Hilfe, oft schon der Notruf)"),
          ("s1c", 3, 1, "3. Erforderlichkeit der Hilfe"),
          ("s1d", 4, 1, "4. Zumutbarkeit: ohne erhebliche eigene Gefahr,"),
          ("s1d", 4, 2, "ohne Verletzung anderer wichtiger Pflichten"),
          ("s1e", 5, 1, "5. Vorsatz (bedingter Vorsatz genügt)"),
          ("s2", "II", 0, "II. Rechtswidrigkeit"),
          ("s3", "III", 0, "III. Schuld")]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfschema: unterlassene Hilfeleistung"), 110, 90, "sch", 46),
           z("§ 323c Abs. 1 StGB (echtes Unterlassungsdelikt)", 110, 160, "sch", "Bold", 32, farbe=TEXT, rechts=1800)]
y = 240
for c, farbe, ebene, text in REIHEN:
    x = (130, 220, 270)[ebene]
    if farbe is not None and ebene != 2:
        ch = Image.new("RGBA", (34, 34))
        ImageDraw.Draw(ch).rounded_rectangle((1, 1, 32, 32), 8, fill=PUNKTFARBE[farbe], outline=INK, width=3)
        els_sch.append(El(ch, x - 50, y + 8, c, "pop", 0.0, None, name="farbpunkt"))
    els_sch.append(z(text, x, y, c, "ExtraBold" if ebene == 0 else "Regular", 38 if ebene == 0 else 34, rechts=1800))
    y += {0: 80, 1: 70, 2: 70}[ebene]
assert y <= 970, y
folie([("sch", "Prüfschema"), ("s1", "Prüfschema › I. Tatbestand"), ("s2", "Prüfschema › II. Rechtswidrigkeit"),
       ("s3", "Prüfschema › III. Schuld")], els_sch)

# ===========================================================================================================================
# N Merksatz (Lexi) mit Notruf 112
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Bei einem Unglücksfall muss", 0)], [("jeder helfen", "a"), (", soweit es", 0)],
                 [("erforderlich und zumutbar ist.", 0)]], 750, 290, 44, "merke", {"a": beim("merke", "jeder")}),
    *markertext([[("Und den Notruf ", 0), ("112", "b"), (" zu wählen,", 0)], [("ist fast immer möglich", 0)],
                 [("und zumutbar.", 0)]], 750, 580, 44, "m2", {"b": beim("m2", "eins")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
