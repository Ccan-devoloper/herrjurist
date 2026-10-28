"""Folge 059 · Sachmangel § 434 BGB: Wann ist eine Sache mangelhaft? – Serienstandard Open Peeps (Katzenkönig).
Beispielfall (Plan-Hook „Laptop und vereinbarte Software“): Kerstin (Verbraucherin) kauft im Computerladen von Herrn Kranich
(Unternehmer) einen Laptop für 900 €; vereinbart ist, dass ihr Schnittprogramm darauf läuft. Zu Hause funktioniert der
Laptop, das Schnittprogramm startet nicht (Grafikkarte zu schwach).
Szenen laut ../SZENENPLAN.md: A1 Laden, A2 zu Hause, B Sachverhalt, C § 434 I (Wortlaut), D1 § 434 II (Wortlaut),
D2 Subsumtion subjektiv, E1 § 434 III (Wortlaut), E2 Subsumtion objektiv, E3 Werbung, E4 § 434 III 2 (Reparierbarkeit),
F1 Gleichrang, F2 Verbrauchsgüterkauf (§§ 476 I 2, 475b), G Montage § 434 IV, H § 434 V und Menge, I1 § 435 und § 477,
I2 Ergebnis und Ausblick § 437, J Klausurtipp (Lexi), K Klausurschema, L Merksatz (Lexi).
Keine Geräusche (keine passende sichtbare Handlung mit Klang, siehe ../geraeusche_herkunft.json). Namensschild jeder Figur,
solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns als eigene Kopie aus Folge 053
(gemeinsame Dateien unverändert). Zahlen auf Tafeln, Pillen und Blasen als Ziffern, im Sprechtext als Wörter."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_059/"

FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
ZITAT = (246, 246, 250, 255)
GRAU = (176, 178, 190, 255)
DAUER = bausteine._cj()["dauer"]
T_ = bausteine._t

_CMAP = set(TTFont(SP + "humaaans/fonts/Nunito[wght].ttf").getBestCmap())


def glyphen(text):
    """Nunito muss jedes Zeichen haben (sonst Kästchen)."""
    fehl = {c for c in text if ord(c) not in _CMAP and not c.isspace()}
    assert not fehl, f"Zeichen fehlt in Nunito: {fehl} in {text!r}"
    return text


def z(text, x, y, cue, stil="Regular", size=36, farbe=INK, d=0.0, rechts=1170, **k):
    """Tafelzeile, die rechts nicht über die Karte hinausragen darf."""
    e = zeile(glyphen(text), x, y, cue, stil, size, farbe=farbe, d=d, **k)
    assert e.x + e.sprite.width <= rechts, f"Zeile zu breit: {text} ({e.x + e.sprite.width:.0f} > {rechts})"
    return e


def pl(text, *a, **k):
    return pille(glyphen(text), *a, **k)


def tafel(cue, titel_, h=840, fill=WEISS, size=46):
    """Rechtstafel links, rechts bleibt Platz für die Figuren."""
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(glyphen(titel_), 110, 100, cue, size)]


def blk(x, y, w, h, fill, cue, zeilen, **k):
    for t, s, g, f in zeilen:
        assert F(s, g).getlength(glyphen(t)) <= w - 30, f"Blockzeile zu breit: {t}"
    # wie fl_block(), aber Zeilenabstand nach der tatsächlichen Schriftgröße (fl_block nimmt 64 px an)
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
    return (cue, round(DAUER - T_(cue) - 0.05, 3))


def zit(text, x, y, cue, size=26):
    """Fundstellenzeile (grau, klein)."""
    return z(text, x, y, cue, size=size, farbe=TEXT)


def rechts_frei(els, x0=1250):
    """Figuren und Requisiten der Tafelfolien stehen rechts der Tafel."""
    for e in els:
        n = e.name or ""
        if n.startswith(("bild:", "ficon:")) or "/op_059/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def wortlaut(x, y, w, zeilen, quelle, cue, marken=(), size=34, bis=None):
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de, als Zitat mit Normangabe;
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


# --- Eigene Hilfsfunktion (wie Folge 031/037): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt -------------
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



BODEN, FH = 880, 480
X1, X2 = 1420, 1720                         # zwei Figuren neben der Tafel: Herr Kranich links, Kerstin rechts
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
KE_F, KR_F = LILA, BLAU                     # Farben der Namensschilder
PX, PY, PU = 1570, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante


def boden(cue, hart_=False):
    e = linienzug([(40, BODEN), (1880, BODEN)], cue, breite=7, farbe=INK)
    return hart(e) if hart_ else e


def laptop(cx, unten, breite, cue, **k):
    """Kerstins Laptop: Tabler „device-laptop“ (MIT), Bildschirm hellblau."""
    return ficon("tabler", "device-laptop", cx, unten, breite, cue, fuell=(226, 236, 252, 255), **k)


def kerstin(cx, unten, hoehe, folge, **k):
    return fig("KE", cx, unten, hoehe, folge, **k)


def kranich(cx, unten, hoehe, folge, **k):
    return fig("KR", cx, unten, hoehe, folge, **k)


def paar(c0, kr_folge, ke_folge):
    """Tafelszene: Herr Kranich links (X1), Kerstin rechts (X2), beide blicken zur Tafel."""
    return [*kranich(X1, FB, FR, kr_folge), ns("Herr Kranich", X1, FB, c0, KR_F),
            *kerstin(X2, FB, FR, ke_folge, d=0.2), ns("Kerstin", X2, FB, c0, KE_F, d=0.2)]


def requisit(folge):
    """Wechselndes Requisit über den Figuren: folge = [(cue, (set, icon, breite, fuell), pillentext, pillenfarbe)]."""
    els = []
    for i, (c, ic, txt, pf) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else None
        if ic:
            s_, n_, br, fu = ic
            els.append(ficon(s_, n_, PX, PU, br, c, fuell=fu, bis=b))
        if txt:
            els.append(pl(txt, PX, PY, c, fill=pf, size=28, anker="m", bis=b))
    return els


# A1 Fall: Freizeit, im Computerladen, der Kauf -------------------------------------------------------------------------
KRX, KEX = 520, 1500
THEKE = (680, 650, 460, 230)                 # Ladentisch (x, y, b, h), unten auf dem Boden
LAP0 = (930, 652)                            # Laptop auf dem Ladentisch
LAP1 = (1310, 720)                           # Laptop in Kerstins Hand
folie([(NULL, "Fall · Videos in der Freizeit"), ("laden", "Fall · Im Computerladen"), ("kauf", "Fall · Der Kauf")], [
    hart(pl("Kerstin schneidet in ihrer Freizeit Videos", 70, 40, NULL, fill=LILA, size=44, bis="laden")),
    boden(NULL, True),
    hart(ficon("tabler", "movie", 960, 560, 220, NULL, fuell=WEISS, bis="laden")),
    hart(pl("Videoschnitt", 960, 600, NULL, fill=WEISS, size=32, anker="m", bis="laden")),
    *kerstin(KEX, BODEN, FH, [(NULL, "ruhig"), ("laden", "ueberlegt")], bis="ke1", erst="cut"),
    *redet("KE_redet", KEX, BODEN, FH, "ke1", "h1"),
    *kerstin(KEX, BODEN, FH, [("h1", "froh")], bis="haus", erst="cut"),
    hart(ns("Kerstin, Käuferin", KEX, BODEN, NULL, KE_F)),
    # im Computerladen
    pl("Im Computerladen von Herrn Kranich", 70, 40, "laden", fill=GELB, size=44),
    ficon("tabler", "building-store", 250, 400, 190, "laden", fuell=GELB),
    bis_(karte(*THEKE, "laden", fill=(222, 214, 200, 255), rund=12, schatten=6), None),
    bewegt(laptop(*LAP1, 230, beim("laden", "Laptop")), beim("kauf", "nimmt"), beim("kauf", "mit", ende=True),
           LAP0[0] - LAP1[0], LAP0[1] - LAP1[1]),
    *kranich(KRX, BODEN, FH, [("laden", "ruhig_r")], bis="h1"),
    *redet("KR_redet_r", KRX, BODEN, FH, "h1", "kauf"),
    *kranich(KRX, BODEN, FH, [("kauf", "froh_r")], erst="cut"),
    ns("Herr Kranich, Verkäufer", KRX, BODEN, "laden", KR_F),
    blase("sprech", 620, 230, "ke1", 1180, 230, inhalt=["Auf dem Laptop muss mein", "Schnittprogramm laufen.", "Geht das?"],
          textsize=34, figur=("KE_redet", KEX, BODEN, FH), bis="h1"),
    blase("sprech", 640, 230, "h1", 900, 230, inhalt=["Ja, das läuft darauf.", "Netzteil und Anleitung", "sind dabei."],
          textsize=34, figur=("KR_redet_r", KRX, BODEN, FH), bis="kauf"),
    ficon("tabler", "plug", 745, 650, 70, beim("h1", "Netzteil"), fuell=WEISS),
    ficon("tabler", "book", 1095, 650, 70, beim("h1", "Anleitung"), fuell=WEISS),
    ficon("tabler", "cash-banknote", 930, 470, 130, beim("kauf", "neunhundert"), fuell=GRUEN),
    pl("900 €", 930, 330, beim("kauf", "neunhundert"), fill=GELB, size=34, anker="m"),
])

# A2 Fall: zu Hause – der Laptop läuft, das Schnittprogramm nicht -------------------------------------------------------
TISCH = (560, 640, 620, 30)                  # Tischplatte
folie([("haus", "Fall · Zu Hause"), ("prog", "Fall · Das Schnittprogramm startet nicht"), ("frage", "Fall · Die Frage")], [
    pl("Zu Hause", 70, 40, "haus", fill=GELB, size=44),
    boden("haus"),
    karte(*TISCH, "haus", fill=(222, 214, 200, 255), rund=8, schatten=4),
    linienzug([(620, 670), (620, BODEN)], "haus", breite=10, farbe=INK),
    linienzug([(1120, 670), (1120, BODEN)], "haus", breite=10, farbe=INK),
    laptop(870, 642, 300, "haus"),
    ficon("tabler", "world-www", 640, 330, 100, beim("haus", "Internet"), fuell=WEISS, bis="frage"),
    bis_(ok(640, 390, beim("haus", "Internet"), gr=20), "frage"),
    ficon("tabler", "mail", 820, 330, 100, beim("haus", "E-Mail"), fuell=WEISS, bis="frage"),
    bis_(ok(820, 390, beim("haus", "E-Mail"), gr=20), "frage"),
    ficon("tabler", "movie-off", 1000, 330, 100, beim("prog", "Schnittprogramm"), fuell=ROT, bis="frage"),
    bis_(nein(1000, 390, beim("prog", "startet"), gr=20), "frage"),
    pl("Grafikkarte zu schwach", 870, 720, beim("prog", "Grafikkarte"), fill=ROT, size=30, anker="m"),
    *kerstin(KEX, BODEN, FH, [("haus", "froh"), ("prog", "sorge")], bis="ke2", erst="fade"),
    *redet("KE_aerger", KEX, BODEN, FH, "ke2", "frage"),
    *kerstin(KEX, BODEN, FH, [("frage", "denkt")], erst="cut"),
    ns("Kerstin", KEX, BODEN, "haus", KE_F),
    blase("sprech", 640, 210, "ke2", 1380, 175, inhalt=["Der Laptop läuft, aber", "mein Programm nicht!"], textsize=36,
          figur=("KE_aerger", KEX, BODEN, FH), bis="frage"),
    pl("Ist der Laptop mangelhaft, obwohl er funktioniert?", 960, 150, "frage", fill=PINK, size=34, anker="m"),
    pl("Und woran misst man das überhaupt?", 960, 240, "frage2", fill=PINK, size=34, anker="m"),
])

# B Sachverhalt ------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Kerstin schneidet in ihrer Freizeit Videos. Im Computerladen von Herrn Kranich fragt sie: „Auf dem Laptop muss mein "
    "Schnittprogramm laufen. Geht das?“ Herr Kranich antwortet: „Ja, das läuft darauf. Netzteil und Anleitung sind dabei.“",
    "Kerstin kauft den Laptop für 900 Euro und nimmt ihn gleich mit. Zu Hause startet er sofort, Internet und E-Mail "
    "funktionieren. Nur das Schnittprogramm startet nicht, weil die Grafikkarte zu schwach ist.",
], "Ist der Laptop mangelhaft, obwohl er funktioniert?")

# C § 434 Abs. 1 BGB ---------------------------------------------------------------------------------------------------------
W434_1 = ["„Die Sache ist frei von Sachmängeln, wenn sie bei Gefahrübergang",
          "den subjektiven Anforderungen, den objektiven Anforderungen",
          "und den Montageanforderungen dieser Vorschrift entspricht.“"]
w1, w1_y = wortlaut(80, 280, 1100, W434_1, "§ 434 Abs. 1 BGB", beim("norm", "sagt"), marken=[
    (1, "subjektiven Anforderungen", beim("w1", "subjektiven")),
    (1, "objektiven Anforderungen", beim("w1", "objektiven")),
    (2, "Montageanforderungen", beim("w1", "Montageanforderungen")),
    (2, "und", beim("und", "Wort")),
    (0, "bei Gefahrübergang", "gefahr")], size=32)
folie([("norm", "Mangelfreie Sache · § 433 Abs. 1 Satz 2 BGB"), ("w1", "§ 434 Abs. 1 BGB › Wortlaut"),
       ("und", "§ 434 Abs. 1 BGB › drei Anforderungen gleichrangig"),
       ("gefahr", "§ 434 Abs. 1 BGB › bei Gefahrübergang, § 446 Satz 1 BGB")], rechts_frei([
    *tafel("norm", "Ist der Laptop mangelhaft?"),
    z("Anspruch auf mangelfreie Sache: § 433 Abs. 1 Satz 2 BGB", 110, 180, beim("norm", "Anspruch"), size=32),
    z("Was ein Sachmangel ist: § 434 BGB", 110, 225, beim("norm", "Was"), "Bold", 32),
    *w1,
    blk(110, w1_y + 30, 330, 90, BLAU, beim("und", "drei"), [("subjektiv", "ExtraBold", 36, INK)]),
    blk(465, w1_y + 30, 330, 90, GELB, beim("und", "drei"), [("objektiv", "ExtraBold", 36, INK)]),
    blk(820, w1_y + 30, 330, 90, GRUEN, beim("und", "drei"), [("Montage", "ExtraBold", 36, INK)]),
    z("gleichrangig: Die Sache muss alle drei erfüllen.", 110, w1_y + 145, beim("und", "gleichrangig"), "Bold", 34),
    z("Zeitpunkt: Gefahrübergang, in der Regel Übergabe,", 110, w1_y + 215, beim("gefahr", "nach"), size=32),
    z("§ 446 Satz 1 BGB – hier im Laden", 110, w1_y + 260, beim("gefahr", "Laden"), size=32),
    *requisit([("norm", ("tabler", "device-laptop", 190, (226, 236, 252, 255)), "der Laptop", WEISS),
               ("gefahr", ("tabler", "building-store", 150, GELB), "Übergabe im Laden", GELB)]),
    *paar("norm", [("norm", "ruhig"), ("und", "denkt")], [("norm", "ueberlegt"), ("w1", "denkt")]),
]))

# D1 § 434 Abs. 2 BGB: subjektive Anforderungen (Wortlaut) ---------------------------------------------------------------
W434_2 = ["„Die Sache entspricht den subjektiven Anforderungen, wenn sie",
          "1. die vereinbarte Beschaffenheit hat,",
          "2. sich für die nach dem Vertrag vorausgesetzte Verwendung eignet und",
          "3. mit dem vereinbarten Zubehör und den vereinbarten Anleitungen, …",
          "übergeben wird. Zu der Beschaffenheit nach Satz 1 Nummer 1 gehören",
          "Art, Menge, Qualität, Funktionalität, Kompatibilität, …“"]
w2, w2_y = wortlaut(80, 190, 1100, W434_2, "§ 434 Abs. 2 BGB", "sub", marken=[
    (1, "vereinbarte Beschaffenheit", "s1"), (2, "vorausgesetzte Verwendung", beim("s2", "vorausgesetzte")),
    (3, "vereinbarten Zubehör", beim("s3", "Zubehör")), (3, "vereinbarten Anleitungen", beim("s3", "Anleitungen")),
    (5, "Funktionalität", beim("kompat", "Funktionalität")), (5, "Kompatibilität", beim("kompat", "Kompatibilität"))],
    size=30)
folie([("sub", "I. Subjektive Anforderungen › § 434 Abs. 2 BGB"),
       ("kompat", "I. Subjektive Anforderungen › Kompatibilität, § 434 Abs. 2 Satz 2 BGB")], rechts_frei([
    *tafel("sub", "I. Subjektive Anforderungen"),
    *w2,
    z("1. vereinbarte Beschaffenheit", 110, w2_y + 40, "s1", "Bold", 34),
    z("2. vertraglich vorausgesetzte Verwendung", 110, w2_y + 95, "s2", "Bold", 34),
    z("3. vereinbartes Zubehör und Anleitungen", 110, w2_y + 150, "s3", "Bold", 34),
    *requisit([("sub", ("tabler", "device-laptop", 190, (226, 236, 252, 255)), "Vereinbarung im Laden", WEISS),
               ("s2", ("tabler", "movie", 150, WEISS), "Videoschnitt", WEISS),
               ("s3", ("tabler", "plug", 120, WEISS), "Netzteil, Anleitung", WEISS),
               ("kompat", ("tabler", "device-laptop", 190, (226, 236, 252, 255)), "Kompatibilität", BLAU)]),
    *paar("sub", [("sub", "ruhig"), ("s2", "denkt")], [("sub", "denkt"), ("kompat", "ueberlegt")]),
]))

# D2 Subsumtion: subjektive Anforderungen --------------------------------------------------------------------------------
folie([("subs", "I. Subjektive Anforderungen › der Laptop von Kerstin")], rechts_frei([
    *tafel("subs", "I. Subjektiv: der Laptop von Kerstin"),
    z("Vereinbart: „Das Schnittprogramm läuft darauf.“", 110, 190, beim("subs", "vereinbart"), "Bold", 34),
    nein(140, 300, "s1n", gr=22), z("1. Beschaffenheit: Kompatibilität fehlt", 185, 280, "s1n", size=34),
    nein(140, 380, "s2n", gr=22), z("2. Verwendung Videoschnitt: ungeeignet", 185, 360, "s2n", size=34),
    ok(140, 460, "s3j", gr=22), z("3. Netzteil und Anleitung dabei: erfüllt", 185, 440, "s3j", size=34),
    blk(110, 540, 1040, 100, ROT, "sube", [("Subjektive Anforderungen verfehlt", "ExtraBold", 40, INK)]),
    *requisit([("subs", ("tabler", "device-laptop", 190, (226, 236, 252, 255)), "Schnittprogramm läuft", WEISS),
               ("s1n", ("tabler", "movie-off", 150, ROT), "läuft nicht", ROT),
               ("s3j", ("tabler", "plug", 120, WEISS), "Netzteil, Anleitung", GRUEN),
               ("sube", ("tabler", "device-laptop", 190, (226, 236, 252, 255)), "verfehlt", ROT)]),
    *paar("subs", [("subs", "ruhig"), ("s1n", "sorge"), ("s3j", "ruhig"), ("sube", "sorge")],
          [("subs", "denkt"), ("s1n", "aerger"), ("s3j", "ruhig"), ("sube", "denkt")]),
]))

# E1 § 434 Abs. 3 BGB: objektive Anforderungen (Wortlaut) ----------------------------------------------------------------
W434_3 = ["„Soweit nicht wirksam etwas anderes vereinbart wurde, entspricht",
          "die Sache den objektiven Anforderungen, wenn sie",
          "1. sich für die gewöhnliche Verwendung eignet,",
          "2. eine Beschaffenheit aufweist, die bei Sachen derselben Art üblich",
          "ist und die der Käufer erwarten kann unter Berücksichtigung …",
          "3. …",
          "4. mit dem Zubehör … übergeben wird, deren Erhalt der Käufer",
          "erwarten kann.“"]
w3, w3_y = wortlaut(80, 190, 1100, W434_3, "§ 434 Abs. 3 Satz 1 BGB", "obj", marken=[
    (0, "Soweit nicht wirksam etwas anderes vereinbart wurde", beim("obj", "Sie")),
    (2, "gewöhnliche Verwendung", beim("o1", "gewöhnliche")),
    (3, "üblich", beim("o2", "übliche")), (4, "der Käufer erwarten kann", beim("o2", "Käufer")),
    (6, "mit dem Zubehör", beim("o4", "Zubehör"))], size=30)
folie([("obj", "II. Objektive Anforderungen › § 434 Abs. 3 BGB")], rechts_frei([
    *tafel("obj", "II. Objektive Anforderungen"),
    *w3,
    *requisit([("obj", ("tabler", "device-laptop", 190, (226, 236, 252, 255)), "was üblich ist", GELB),
               ("o4", ("tabler", "plug", 120, WEISS), "Zubehör", WEISS)]),
    *paar("obj", [("obj", "ruhig")], [("obj", "denkt"), ("o2", "ueberlegt")]),
]))

# E2 Subsumtion: objektive Anforderungen ---------------------------------------------------------------------------------
folie([("osub", "II. Objektive Anforderungen › der Laptop von Kerstin")], rechts_frei([
    *tafel("osub", "II. Objektiv: der Laptop von Kerstin"),
    ok(140, 220, beim("osub", "Surfen"), gr=22), z("Surfen und Schreiben: gewöhnliche Verwendung", 185, 200,
                                                   beim("osub", "Surfen"), size=34),
    z("Ein Laptop dieser Klasse muss nicht jedes", 185, 280, beim("osub", "Ein"), size=34),
    z("anspruchsvolle Schnittprogramm schaffen.", 185, 330, beim("osub", "anspruchsvolle"), size=34),
    blk(110, 420, 1040, 100, GRUEN, "ook", [("Objektive Anforderungen erfüllt", "ExtraBold", 40, INK)]),
    ficon("tabler", "world-www", PX - 90, PU, 110, beim("osub", "Surfen"), fuell=WEISS),
    ficon("tabler", "file-text", PX + 90, PU, 100, beim("osub", "Schreiben"), fuell=WEISS),
    pl("Laptop eignet sich", PX, PY, beim("osub", "Surfen"), fill=GRUEN, size=28, anker="m"),
    *paar("osub", [("osub", "ruhig"), ("ook", "froh")], [("osub", "denkt"), ("ook", "ueberlegt")]),
]))

# E3 Werbung, Ausnahme § 434 Abs. 3 Satz 3 BGB -----------------------------------------------------------------------------
folie([("werb", "II. Objektive Anforderungen › Werbung, § 434 Abs. 3 Satz 1 Nr. 2 b BGB"),
       ("ausn", "II. Objektive Anforderungen › Ausnahme, § 434 Abs. 3 Satz 3 BGB")], rechts_frei([
    *tafel("werb", "Auch die Werbung zählt"),
    z("Öffentliche Äußerungen von Verkäufer oder", 110, 190, beim("werb", "öffentliche"), "Bold", 34),
    z("Hersteller, etwa in der Werbung", 110, 240, beim("werb", "Hersteller"), "Bold", 34),
    z("Werbung: 10 Stunden Akku – er hält nur 3", 110, 320, "akku", size=34),
    nein(140, 400, beim("akku", "wäre"), gr=22), z("auch objektiv mangelhaft", 185, 380, beim("akku", "wäre"), "Bold", 34),
    z("Nicht gebunden ist der Verkäufer nur, wenn die Äußerung", 110, 475, "ausn", "Bold", 32),
    z("1. ihm unbekannt war und er sie nicht kennen konnte,", 150, 530, beim("ausn", "nicht"), size=32),
    z("2. bei Vertragsschluss berichtigt war oder", 150, 580, beim("ausn", "Vertragsschluss"), size=32),
    z("3. den Kauf nicht beeinflussen konnte.", 150, 630, beim("ausn", "Kauf"), size=32),
    zit("Exposé als öffentliche Äußerung: BGH, Urt. v. 6.12.2024 – V ZR 229/23,", 110, 700, beim("ausn", "Kauf")),
    zit("Rn. 5 (zu § 434 Abs. 1 Satz 3 a. F., heute Abs. 3 Satz 1 Nr. 2 b)", 110, 735, beim("ausn", "Kauf")),
    *requisit([("werb", ("tabler", "speakerphone", 150, GELB), "Werbung", GELB),
               ("akku", ("tabler", "battery-4", 160, GRUEN), "10 Stunden Akku", GELB),
               (beim("akku", "nur"), ("tabler", "battery-1", 160, ROT), "nur 3 Stunden", ROT),
               ("ausn", ("tabler", "speakerphone", 150, GELB), "Ausnahmen", WEISS)]),
    *paar("werb", [("werb", "ruhig"), ("akku", "sorge"), ("ausn", "denkt")], [("werb", "denkt"), ("akku", "aerger"),
                                                                              ("ausn", "ueberlegt")]),
]))

# E4 § 434 Abs. 3 Satz 2 BGB: übliche Beschaffenheit, Reparierbarkeit -----------------------------------------------------
W434_32 = ["„Zu der üblichen Beschaffenheit nach Satz 1 Nummer 2 gehören",
           "Menge, Qualität und sonstige Merkmale der Sache, einschließlich",
           "ihrer Haltbarkeit, Reparierbarkeit, Funktionalität, Kompatibilität",
           "und Sicherheit.“"]
w32, w32_y = wortlaut(80, 190, 1100, W434_32, "§ 434 Abs. 3 Satz 2 BGB", "rep", marken=[
    (2, "Haltbarkeit", beim("rep", "Haltbarkeit")), (3, "Sicherheit", beim("rep", "Sicherheit")),
    (2, "Reparierbarkeit", beim("rep2", "Reparierbarkeit"))], size=32)
folie([("rep", "II. Objektive Anforderungen › übliche Beschaffenheit, § 434 Abs. 3 Satz 2 BGB"),
       ("rep2", "II. Objektive Anforderungen › Reparierbarkeit, Art. 229 § 72 EGBGB")], rechts_frei([
    *tafel("rep", "Übliche Beschaffenheit"),
    *w32,
    pl("Reparierbarkeit: Verträge ab 31.7.2026", 110, w32_y + 50, beim("rep2", "Verträgen"), fill=GELB, size=34),
    z("zwischen Unternehmern erst ab 2028", 130, w32_y + 145, beim("rep2", "Zwischen"), "Bold", 34),
    zit("Art. 229 § 72 EGBGB: B2B für Verträge nach dem 31.12.2027", 130, w32_y + 200, beim("rep2", "Zwischen")),
    *requisit([("rep", ("tabler", "shield-check", 140, GRUEN), "haltbar und sicher", GRUEN),
               ("rep2", ("tabler", "tool", 140, WEISS), "Reparierbarkeit", GELB)]),
    *paar("rep", [("rep", "ruhig"), ("rep2", "froh")], [("rep", "denkt"), ("rep2", "froh")]),
]))

# F1 Gleichrang ------------------------------------------------------------------------------------------------------------
folie([("gleich", "Gleichrang · eine verfehlte Anforderung genügt")], rechts_frei([
    *tafel("gleich", "Deshalb gilt"),
    blk(110, 200, 500, 150, BLAU, "gl1", [("I. subjektiv", "ExtraBold", 40, INK), ("vereinbart", "Regular", 32, INK)]),
    blk(650, 200, 500, 150, GELB, "gl1", [("II. objektiv", "ExtraBold", 40, INK), ("üblich", "Regular", 32, INK)]),
    nein(560, 230, beim("gl1", "aber"), gr=22),
    ok(1100, 230, beim("gl1", "objektiven"), gr=22),
    blk(110, 400, 1040, 100, ROT, "gl2", [("Das genügt für einen Sachmangel.", "ExtraBold", 40, INK)]),
    z("Umgekehrt: Programm läuft, Akku defekt", 110, 560, "gl3", "Bold", 34),
    nein(140, 640, beim("gl3", "ebenfalls"), gr=22), z("ebenfalls mangelhaft", 185, 620, beim("gl3", "ebenfalls"), "Bold", 34),
    *requisit([("gleich", ("tabler", "device-laptop", 190, (226, 236, 252, 255)), "der Laptop", WEISS),
               ("gl2", ("tabler", "device-laptop", 190, (226, 236, 252, 255)), "mangelhaft", ROT),
               ("gl3", ("tabler", "battery-1", 160, ROT), "Akku defekt", ROT)]),
    *paar("gleich", [("gleich", "ruhig"), ("gl2", "sorge")], [("gleich", "denkt"), ("gl2", "froh"), ("gl3", "ueberlegt")]),
]))

# F2 Verbrauchsgüterkauf: § 476 Abs. 1 Satz 2, § 475b BGB --------------------------------------------------------------------
folie([("vgk", "Verbrauchsgüterkauf · Verbraucherin kauft vom Unternehmer"),
       ("p476", "Verbrauchsgüterkauf · Abweichung, § 476 Abs. 1 Satz 2 BGB"),
       ("p475b", "Verbrauchsgüterkauf · Aktualisierungen, § 475b BGB")], rechts_frei([
    *tafel("vgk", "Verbrauchsgüterkauf"),
    z("Kerstin: Verbraucherin, Herr Kranich: Unternehmer", 110, 190, "vgk", "Bold", 34),
    z("Abweichung von den objektiven Anforderungen nur, wenn", 110, 280, "p476", "Bold", 32),
    z("1. vor ihrer Vertragserklärung eigens auf das", 150, 335, beim("p476", "eigens"), size=32),
    z("abweichende Merkmal hingewiesen und", 185, 380, beim("p476", "eigens"), size=32),
    z("2. ausdrücklich und gesondert vereinbart", 150, 435, beim("p476", "ausdrücklich"), size=32),
    z("§ 476 Abs. 1 Satz 2 BGB", 150, 485, beim("p476", "Paragraf"), "Bold", 32),
    z("Digitale Elemente, z. B. Betriebssystem:", 110, 580, "p475b", "Bold", 34),
    z("auch Aktualisierungen, § 475b BGB", 150, 635, beim("p475b", "Aktualisierungen"), size=34),
    pl("Unternehmer", X1, 160, beim("vgk", "Unternehmer"), fill=BLAU, size=28, anker="m", bis="p476"),
    pl("Verbraucherin", X2, 230, beim("vgk", "Verbraucherin"), fill=LILA, size=28, anker="m", bis="p476"),
    *requisit([("p476", ("tabler", "file-certificate", 140, WEISS), "ausdrücklich und gesondert", GELB),
               ("p475b", ("tabler", "refresh", 140, WEISS), "Aktualisierungen", BLAU)]),
    *paar("vgk", [("vgk", "ruhig"), ("p476", "denkt")], [("vgk", "ruhig"), ("p476", "ueberlegt"), ("p475b", "denkt")]),
]))

# G III. Montageanforderungen, § 434 Abs. 4 BGB ----------------------------------------------------------------------------
folie([("mont", "III. Montageanforderungen › § 434 Abs. 4 BGB")], rechts_frei([
    *tafel("mont", "III. Montageanforderungen"),
    z("nur, soweit eine Montage durchzuführen ist,", 110, 190, beim("mont", "soweit"), "Bold", 34),
    z("etwa bei einer Einbauküche", 150, 245, beim("mont", "etwa"), size=34),
    z("Mangelhaft, wenn", 110, 330, "mo1", "Bold", 34),
    nein(170, 410, "mo1", gr=20), z("der Verkäufer unsachgemäß montiert oder", 210, 390, "mo1", size=34),
    nein(170, 470, "mo2", gr=20), z("eine falsche Montage auf einem Fehler", 210, 450, "mo2", size=34),
    z("in seiner Anleitung beruht", 210, 500, beim("mo2", "Fehler"), size=34),
    z("Beim Laptop: nichts zu montieren", 110, 600, "mo3", "Bold", 34),
    *requisit([("mont", ("ph", "wrench", 130, WEISS), "Montage", WEISS),
               (beim("mont", "etwa"), ("ph", "cooking-pot", 150, GELB), "Einbauküche", GELB),
               ("mo1", ("tabler", "tools", 140, WEISS), "unsachgemäß montiert", ROT),
               ("mo2", ("tabler", "book", 130, ROT), "Fehler in der Anleitung", ROT),
               ("mo3", ("tabler", "device-laptop", 190, (226, 236, 252, 255)), "nichts zu montieren", WEISS)]),
    *paar("mont", [("mont", "ruhig"), ("mo3", "froh")], [("mont", "denkt"), ("mo3", "ruhig")]),
]))

# H IV. Gleichstellung: andere Sache, § 434 Abs. 5 BGB; Menge ---------------------------------------------------------------
W434_5 = ["„Einem Sachmangel steht es gleich, wenn der Verkäufer eine andere",
          "Sache als die vertraglich geschuldete Sache liefert.“"]
w5, w5_y = wortlaut(80, 190, 1100, W434_5, "§ 434 Abs. 5 BGB", "ali", marken=[
    (0, "eine andere", beim("ali", "andere")), (1, "Sache als die vertraglich geschuldete Sache", beim("ali", "andere")),
    (0, "Einem Sachmangel steht es gleich", beim("ali", "Sachmangel"))], size=32)
folie([("ali", "IV. Gleichstellung › andere Sache, § 434 Abs. 5 BGB"),
       ("menge", "IV. Gleichstellung › Menge gehört zur Beschaffenheit, § 434 Abs. 2 Satz 2 BGB")], rechts_frei([
    *tafel("ali", "IV. Gleichstellung"),
    *w5,
    z("z. B. ein anderes Modell", 110, w5_y + 40, beim("ali", "Modell"), "Bold", 34),
    z("Zu wenig geliefert: vereinbarte Menge verfehlt", 110, w5_y + 150, "menge", "Bold", 34),
    z("Menge gehört zur Beschaffenheit, § 434 Abs. 2 Satz 2 BGB", 110, w5_y + 205, beim("menge", "gehört"), size=32),
    ficon("tabler", "device-laptop", PX - 95, PU, 160, "ali", fuell=(226, 236, 252, 255), bis="menge"),
    ficon("tabler", "device-laptop", PX + 95, PU, 160, beim("ali", "Modell"), fuell=ORANGE, bis="menge"),
    pl("anderes Modell", PX, PY, beim("ali", "Modell"), fill=ORANGE, size=28, anker="m", bis="menge"),
    ficon("tabler", "packages", PX, PU, 150, "menge", fuell=GELB),
    pl("zu wenig", PX, PY, beim("menge", "zu"), fill=ROT, size=28, anker="m"),
    *paar("ali", [("ali", "ruhig"), ("menge", "denkt")], [("ali", "ueberlegt"), ("menge", "denkt")]),
]))

# I1 Rechtsmangel, § 435; Beweis, § 477 -------------------------------------------------------------------------------------
folie([("recht", "Abgrenzung · Rechtsmangel, § 435 BGB"), ("p477", "Beweis · Vermutung, § 477 Abs. 1 BGB")], rechts_frei([
    *tafel("recht", "Abgrenzung und Beweis"),
    blk(110, 190, 500, 150, LILA, beim("recht", "Rechtsmangel"), [("Rechtsmangel", "ExtraBold", 40, INK),
                                                                   ("§ 435: Rechte Dritter", "Regular", 32, INK)]),
    blk(650, 190, 500, 150, GELB, beim("recht", "Beschaffenheit"), [("nicht Sachmangel", "ExtraBold", 40, INK),
                                                                     ("§ 434: Beschaffenheit", "Regular", 32, INK)]),
    z("Verbrauchsgüterkauf: Abweichung zeigt sich", 110, 420, "p477", "Bold", 34),
    z("im 1. Jahr seit Gefahrübergang", 150, 475, beim("p477", "innerhalb"), size=34),
    z("vermutet: schon bei Gefahrübergang mangelhaft", 150, 530, beim("p477", "vermutet"), size=34),
    z("§ 477 Abs. 1 Satz 1 BGB", 150, 585, beim("p477", "Paragraf"), "Bold", 32),
    *requisit([(beim("recht", "Rechte"), ("tabler", "users", 140, LILA), "Rechte Dritter?", LILA),
               ("p477", ("tabler", "calendar-event", 130, GELB), "1 Jahr", GELB)]),
    *paar("recht", [("recht", "ruhig"), ("p477", "denkt")], [("recht", "denkt"), ("p477", "ueberlegt")]),
]))

# I2 Ergebnis, Ausblick § 437 -----------------------------------------------------------------------------------------------
folie([("erg", "Ergebnis · der Laptop ist mangelhaft"), ("p437", "Ausblick · Käuferrechte, § 437 BGB")], rechts_frei([
    *tafel("erg", "Ergebnis"),
    z("Die Grafikkarte war von Anfang an zu schwach.", 110, 200, beim("erg", "Grafikkarte"), "Bold", 34),
    blk(110, 290, 1040, 110, ROT, beim("erg", "Der"), [("Der Laptop ist mangelhaft.", "ExtraBold", 44, INK)]),
    z("Rechte von Kerstin: § 437 BGB", 110, 470, "p437", "Bold", 36),
    pl("Mehr dazu: Folge zu den Käuferrechten", 110, 550, beim("p437", "Dazu"), fill=WEISS, size=30),
    *requisit([("erg", ("tabler", "movie-off", 150, ROT), "Grafikkarte zu schwach", ROT),
               ("p437", ("tabler", "scale", 140, WEISS), "§ 437 BGB", GELB)]),
    *paar("erg", [("erg", "sorge"), ("p437", "ernst")], [("erg", "ueberlegt"), ("p437", "froh")]),
]))

# J Klausurtipp (Lexi) -------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · alle drei Anforderungen prüfen")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Prüfe alle drei Anforderungen", 200, 200, beim("tipp", "Prüfe"), "Bold", 36),
    z("in der Reihenfolge des Gesetzes,", 150, 290, beim("tipp", "Reihenfolge"), size=36),
    z("zuerst die Vereinbarung.", 150, 350, beim("tipp", "zuerst"), size=36),
    nein(140, 480, "tipp2", gr=22), z("„Die Sache funktioniert,", 185, 460, "tipp2", size=34),
    z("also ist sie mangelfrei.“", 185, 512, "tipp2", size=34),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# K Klausurschema ------------------------------------------------------------------------------------------------------------
K1, K2 = 150, 210
folie([("sch", "Klausurschema"), ("k3", "Klausurschema › Montage und Gleichstellung")], [
    karte(60, 50, 1800, 900, "sch"),
    titel(glyphen("Klausurschema: Sachmangel, § 434 BGB – bei Gefahrübergang"), 110, 90, "sch", 44),
    z("I. Subjektive Anforderungen, Abs. 2", K1, 190, "k1", "Bold", 38, rechts=1820),
    z("vereinbarte Beschaffenheit, vorausgesetzte Verwendung, vereinbartes Zubehör und Anleitungen", K2, 245, "k1a",
      size=32, rechts=1820),
    z("II. Objektive Anforderungen, Abs. 3", K1, 320, "k2", "Bold", 38, rechts=1820),
    z("gewöhnliche Verwendung, übliche Beschaffenheit samt Werbung, erwartbares Zubehör", K2, 375, "k2a", size=32,
      rechts=1820),
    z("III. Montageanforderungen, Abs. 4 – falls montiert wird", K1, 450, "k3", "Bold", 38, rechts=1820),
    z("IV. Gleichstellung: andere Sache, Abs. 5", K1, 530, "k4", "Bold", 38, rechts=1820),
    blk(K1, 630, 1600, 90, ROT, "k5", [("Fehlt nur eine Anforderung: Sachmangel", "ExtraBold", 38, INK)]),
])

# L Merksatz (Lexi) ----------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Mangelfrei ist eine Sache nur,", 0)], [("wenn sie ", 0), ("alle Anforderungen", "a")],
                 [("zugleich erfüllt.", 0)]],
                750, 300, 44, "merke", {"a": beim("merke", "alle")}),
    *markertext([[("Funktioniert sie, aber nicht", 0)], [("wie vereinbart", "b"), (", ist sie mangelhaft.", 0)]],
                750, 560, 42, "m2", {"b": beim("m2", "wie")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
