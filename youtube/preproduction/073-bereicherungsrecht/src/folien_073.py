"""Folge 073 · Bereicherungsrecht Überblick: Welche Kondiktion wann? (§ 812 BGB) – Serienstandard Open Peeps (Katzenkönig).
Beispielfall (Plan-Hook „Du überweist versehentlich 500 Euro an eine völlig fremde Person“): Ursula will ihrem Maler 500 €
überweisen, vertauscht zwei Ziffern der IBAN; das Geld landet bei dem fremden Rüdiger, der es behält und am See ausgibt.
Szenen laut ../SZENENPLAN.md: A1 Die Fehlüberweisung, A2 Frage, B Sachverhalt, C § 812 I (Wortlaut) und zwei Grundtypen,
D Leistungsbegriff, E Entscheidungsbaum (progressiv: Weiche, Vorrang, vier Leistungskondiktionen mit Ausschlüssen,
Nichtleistungskondiktionen), F Lösung des Falls, G Ausblick Bankdreieck, H1 Rechtsfolge § 818 I, II, H2 Entreicherung,
verschärfte Haftung, § 822, Ergebnis, I Klausurtipp (Lexi), J Klausurschema, K Merksatz (Lexi).
Zwei Handlungsgeräusche (Tippen auf dem Handy, Vibration beim Anruf; ../geraeusche_herkunft.json). Namensschild jeder Figur,
solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns als eigene Kopie aus Folge 067
(gemeinsame Dateien unverändert). Zahlen auf Tafeln, Pillen und Blasen als Ziffern, im Sprechtext als Wörter.
Keine echte Bank, keine echte IBAN (nur „…74 statt …47“)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_073/"

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
    return (cue, round(DAUER - T_(cue) + 0.5, 3))       # Lexi bleibt bis zum letzten Frame (Befund Folge 063 über 067)


def zit(text, x, y, cue, size=26, **k):
    """Fundstellenzeile (grau, klein)."""
    return z(text, x, y, cue, size=size, farbe=TEXT, **k)


def rechts_frei(els, x0=1250):
    """Figuren und Requisiten der Tafelfolien stehen rechts der Tafel."""
    for e in els:
        n = e.name or ""
        if n.startswith(("bild:", "ficon:")) or "/op_073/" in n:
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


BODEN, FH = 860, 480
X1, X2 = 1420, 1720                         # zwei Figuren neben der Tafel: Ursula links, Rüdiger rechts
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
UR_F, RD_F = LILA, BLAU                     # Farben der Namensschilder
PX, PY, PU = 1570, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante


def boden(cue, hart_=False):
    e = linienzug([(40, BODEN), (1880, BODEN)], cue, breite=7, farbe=INK)
    return hart(e) if hart_ else e


def ursula(cx, unten, hoehe, folge, **k):
    return fig("UR", cx, unten, hoehe, folge, **k)


def ruediger(cx, unten, hoehe, folge, **k):
    return fig("RD", cx, unten, hoehe, folge, **k)


def paar(c0, ur_folge, rd_folge):
    """Tafelszene: Ursula links (X1), Rüdiger rechts (X2), beide blicken zur Tafel."""
    return [*ursula(X1, FB, FR, ur_folge), ns("Ursula", X1, FB, c0, UR_F),
            *ruediger(X2, FB, FR, rd_folge, d=0.2), ns("Rüdiger", X2, FB, c0, RD_F, d=0.2)]


def nur_ursula(c0, folge):
    return [*ursula(FX, FB, FR, folge), ns("Ursula", FX, FB, c0, UR_F)]


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


SCALE = ("tabler", "scale", 130, WEISS)
GELD = ("tabler", "cash-banknote", 150, GRUEN)
HANDY = ("tabler", "device-mobile", 90, WEISS)

# A1 Fall: die Fehlüberweisung ----------------------------------------------------------------------------------------
UX, RX = 380, 1560                           # Ursula links (blickt nach rechts), Rüdiger rechts (blickt nach links)
folie([(NULL, "Fall · Die Fehlüberweisung"), ("rd1", "Fall · Rüdiger behält das Geld"), ("anruf", "Fall · Der Anruf")], [
    hart(pl("Eine Überweisung mit Folgen", 70, 40, NULL, fill=GELB, size=44)),
    hart(boden(NULL)),
    *ursula(UX, BODEN, FH, [(NULL, "ruhig_r"), ("anruf", "schreck_r")], bis="ur1", erst="cut"),
    *redet("UR_redet_r", UX, BODEN, FH, "ur1", "rd2"),
    peep_voll("UR_redet_r", UX, BODEN, FH, "rd2", anim="cut", bis="frage"),   # Mund zu, solange Rüdiger spricht
    hart(ns("Ursula, Überweisende", UX, BODEN, NULL, UR_F)),
    szene(hart(ficon("tabler", "device-mobile", 530, 700, 80, NULL, fuell=WEISS, bis="anruf")), "073tippen*", 0.6,
          T_("ziff") - T_("fall") + 0.2),
    ficon("tabler", "phone-call", 530, 700, 90, "anruf", fuell=WEISS, anim="cut", bis="rd2"),
    ficon("tabler", "file-invoice", 760, 330, 90, beim("fall", "Rechnung"), fuell=WEISS, bis="weg"),
    pl("Rechnung des Malers: 500 €", 760, 370, beim("fall", "fünfhundert"), fill=WEISS, size=30, anker="m", bis="weg"),
    pl("IBAN: …74 statt …47", 760, 450, beim("ziff", "vertauscht"), fill=ORANGE, size=30, anker="m", bis="rd1"),
    bewegt(ficon("fluent-emoji-flat", "money-with-wings", 1290, 620, 120, "weg", bis=beim("see", "Wochenende")), "weg", ("weg", 1.6), -560),
    pl("500 €", 1290, 440, ("weg", 1.6), fill=GRUEN, size=30, anker="m", bis=beim("see", "Wochenende")),
    *ruediger(RX, BODEN, FH, [("weg", "ruhig"), ("see", "froh"), ("anruf", "denkt")], bis="rd2", erst="pop"),
    *redet("RD_grinst", RX, BODEN, FH, "rd1", "see"),
    *redet("RD_redet", RX, BODEN, FH, "rd2", "frage"),
    ns("Rüdiger, Empfänger", RX, BODEN, "weg", RD_F),
    pl("Konto von Rüdiger", RX, 300, beim("weg", "Konto"), fill=BLAU, size=30, anker="m", bis="rd1"),
    blase("sprech", 700, 260, "rd1", 1050, 200, inhalt=["500 €? Die sind gar nicht für mich.", "Egal, die behalte ich!"],
          textsize=36, figur=("RD_grinst", RX, BODEN, FH), bis="see"),
    ficon("tabler", "beach", 1130, BODEN, 230, beim("see", "Wochenende"), fuell=GELB, bis="anruf"),
    pl("Wochenende am See", 1130, 520, beim("see", "Wochenende"), fill=GELB, size=30, anker="m", bis="anruf"),
    pl("2 Tage später", 960, 140, "anruf", fill=WEISS, size=30, anker="m", bis="ur1"),
    szene(ficon("tabler", "device-mobile", 1330, 560, 80, beim("anruf", "ruft"), fuell=WEISS, bis="frage"), "073vibration*", 0.8, 0.0),
    blase("sprech", 780, 260, "ur1", 980, 275, inhalt=["Ich habe mich bei der IBAN vertippt!", "Bitte überweisen Sie mir",
          "die 500 € zurück."], textsize=34, figur=("UR_redet_r", UX, BODEN, FH), bis="rd2"),
    blase("sprech", 620, 220, "rd2", 1150, 220, inhalt=["Tut mir leid, das Geld", "ist schon weg."], textsize=36,
          figur=("RD_redet", RX, BODEN, FH), bis="frage"),
])

# A2 Fall: Frage -------------------------------------------------------------------------------------------------------
AUX, ARX = 330, 1590
folie([("frage", "Fall · Die Frage")], [
    pl("Die Frage", 70, 40, "frage", fill=GELB, size=44),
    boden("frage"),
    *ursula(AUX, BODEN, FH, [("frage", "sorge_r"), ("frage2", "denkt_r")]),
    ns("Ursula", AUX, BODEN, "frage", UR_F),
    *ruediger(ARX, BODEN, FH, [("frage", "ruhig"), ("frage2", "sorge")], d=0.2),
    ns("Rüdiger", ARX, BODEN, "frage", RD_F, d=0.2),
    ficon("tabler", "cash-banknote", 960, 470, 170, "frage", fuell=GRUEN),
    pl("Kann Ursula das Geld zurückverlangen?", 960, 560, beim("frage", "Kann"), fill=PINK, size=36, anker="m"),
    pl("Welche Kondiktion passt?", 960, 660, "frage2", fill=PINK, size=36, anker="m"),
])

# B Sachverhalt --------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Ursula will ihrem Maler 500 Euro für seine Rechnung überweisen. Beim Eintippen der IBAN vertauscht sie zwei "
    "Ziffern. Das Geld landet auf dem Konto von Rüdiger, einem völlig Fremden.",
    "Rüdiger weiß, dass das Geld nicht für ihn ist, behält es aber und gibt es noch am selben Tag für ein Wochenende am "
    "See aus. Zwei Tage später bemerkt Ursula den Fehler, ruft Rüdiger an und bittet um Rückzahlung. Rüdiger: „Tut mir "
    "leid, das Geld ist schon weg.“",
], "Kann Ursula die 500 Euro zurückverlangen, und woraus?")

# C § 812 Abs. 1 BGB (Wortlaut) und zwei Grundtypen ----------------------------------------------------------------------
W812 = ["„Wer durch die Leistung eines anderen oder in sonstiger Weise",
        "auf dessen Kosten etwas ohne rechtlichen Grund erlangt, ist ihm",
        "zur Herausgabe verpflichtet. Diese Verpflichtung besteht auch dann,",
        "wenn der rechtliche Grund später wegfällt oder der mit einer Leistung",
        "nach dem Inhalt des Rechtsgeschäfts bezweckte Erfolg nicht eintritt.“"]
w812, w812_y = wortlaut(80, 170, 1100, W812, "§ 812 Abs. 1 BGB", "norm", marken=[
    (0, "durch die Leistung eines anderen", beim("w812", "Leistung")),
    (0, "in sonstiger Weise", beim("w812", "sonstiger")),
    (1, "ohne rechtlichen Grund", beim("w812", "ohne")),
    (2, "zur Herausgabe verpflichtet", beim("w812", "Herausgabe")),
    (3, "rechtliche Grund später wegfällt", beim("w812b", "später")),
    (4, "bezweckte Erfolg nicht eintritt", beim("w812b", "bezweckte"))], size=32)
folie([("norm", "Anspruchsgrundlage · § 812 Abs. 1 BGB › Wortlaut"), ("typen", "§ 812 Abs. 1 BGB › zwei Grundtypen")], rechts_frei([
    *tafel("norm", "Anspruchsgrundlage: § 812 Abs. 1 BGB"),
    *w812,
    z("Zwei Grundtypen:", 110, w812_y + 40, "typen", "Bold", 36),
    blk(110, w812_y + 110, 1040, 100, BLAU, "lk", [("Leistungskondiktion", "ExtraBold", 36, INK)]),
    blk(110, w812_y + 240, 1040, 100, GELB, "nlk", [("Nichtleistungskondiktion: in sonstiger Weise", "ExtraBold", 34, INK)]),
    *requisit([("norm", SCALE, "§ 812 Abs. 1 BGB", GELB), ("typen", ("tabler", "arrows-split", 130, WEISS), "zwei Grundtypen", WEISS)]),
    *paar("norm", [("norm", "ruhig"), ("w812b", "denkt")], [("norm", "ruhig"), ("typen", "denkt")]),
]))

# D Leistungsbegriff -----------------------------------------------------------------------------------------------------
folie([("lb", "Leistungsbegriff"), ("ehz", "Leistungsbegriff › Sicht des Empfängers")], rechts_frei([
    *tafel("lb", "Die Weiche: der Leistungsbegriff"),
    z("Leistung =", 110, 200, "lb2", "Bold", 38),
    z("bewusste und zweckgerichtete", 160, 265, beim("lb2", "bewusste"), size=38),
    z("Mehrung fremden Vermögens", 160, 320, beim("lb2", "Mehrung"), size=38),
    zit("BGH, Urt. v. 21.6.2012 – III ZR 291/11, Rn. 24", 160, 380, beim("lb2", "Mehrung")),
    z("Zweck verschieden verstanden?", 110, 470, "ehz", "Bold", 38),
    z("Sicht eines vernünftigen Empfängers", 160, 535, beim("ehz", "entscheidet"), size=38),
    zit("BGH, Urt. v. 31.1.2018 – VIII ZR 39/17, Rn. 17", 160, 595, beim("ehz", "entscheidet")),
    *requisit([("lb", ("tabler", "arrows-split", 130, WEISS), "Weiche", WEISS),
               ("lb2", ("tabler", "target-arrow", 120, WEISS), "zweckgerichtet", GELB),
               ("ehz", ("tabler", "eye", 120, WEISS), "Empfängersicht", BLAU)]),
    *paar("lb", [("lb", "ruhig"), ("ehz", "denkt")], [("lb", "denkt"), ("ehz", "ruhig")]),
]))

# E Entscheidungsbaum (progressiv, breite Karte) ----------------------------------------------------------------------------
LX0, RX0 = 110, 1000                         # linke/rechte Spalte des Baums
folie([("baum", "Entscheidungsbaum"), ("b1", "Entscheidungsbaum › Erlangt durch Leistung?"),
       ("vorrang", "Entscheidungsbaum › Vorrang der Leistungskondiktion"), ("lks", "Leistungskondiktionen"),
       ("ci", "Leistungskondiktionen › condictio indebiti, § 812 I 1 Alt. 1 BGB"),
       ("ocf", "Leistungskondiktionen › condictio ob causam finitam, § 812 I 2 Alt. 1 BGB"),
       ("orem", "Leistungskondiktionen › condictio ob rem, § 812 I 2 Alt. 2 BGB"),
       ("p817", "Leistungskondiktionen › § 817 Satz 1 BGB"),
       ("aus", "Leistungskondiktionen › Ausschluss: §§ 814, 817 Satz 2 BGB"),
       ("nls", "Nichtleistungskondiktionen › Eingriffskondiktion, § 812 I 1 Alt. 2 BGB"),
       ("p816", "Nichtleistungskondiktionen › § 816 BGB"), ("rv", "Nichtleistungskondiktionen › Rückgriff, Verwendung")], [
    karte(60, 50, 1800, 900, "baum"),
    titel(glyphen("Entscheidungsbaum: Welche Kondiktion?"), 110, 80, "baum", 44),
    blk(560, 150, 800, 84, PINK, "b1", [("Erlangt durch eine Leistung?", "ExtraBold", 36, INK)], anim="pop"),
    linienzug([(960, 234), (960, 254), (520, 254), (520, 280)], "bja", breite=6),
    blk(LX0, 280, 820, 80, BLAU, "bja", [("Ja: Leistungskondiktion", "ExtraBold", 34, INK)], anim="pop"),
    linienzug([(960, 254), (1410, 254), (1410, 280)], "bnein", breite=6),
    blk(RX0, 280, 820, 80, GELB, "bnein", [("Nein: Nichtleistungskondiktion", "ExtraBold", 34, INK)], anim="pop"),
    pl("Vorrang der Leistungskondiktion", 960, 378, "vorrang", fill=LILA, size=30, anker="m"),
    zit("BGH, Urt. v. 18.1.2012 – I ZR 187/10, Rn. 46; VIII ZR 39/17, Rn. 16", 520, 452, beim("vorrang", "Leistungskondiktion"),
        rechts=1820),
    # linker Ast: Leistungskondiktionen (je Kondiktion zuerst der Fall, dann Norm und Name – wie gesprochen)
    z("4 Leistungskondiktionen:", LX0, 490, "lks", "Bold", 32, rechts=930),
    z("Rechtsgrund fehlt von Anfang an:", LX0, 535, beim("ci", "Rechtsgrund"), "Bold", 30, rechts=930),
    z("§ 812 I 1 Alt. 1 · condictio indebiti", LX0 + 30, 572, beim("ci", "Paragraf"), size=28, rechts=930),
    z("Grund fällt später weg, etwa auflösende Bedingung:", LX0, 617, "ocf", "Bold", 30, rechts=930),
    z("§ 812 I 2 Alt. 1 · condictio ob causam finitam", LX0 + 30, 654, beim("ocf", "condictio"), size=28, rechts=930),
    z("vereinbarter Zweck bleibt aus:", LX0, 699, "orem", "Bold", 30, rechts=930),
    z("§ 812 I 2 Alt. 2 · condictio ob rem", LX0 + 30, 736, beim("orem", "condictio"), size=28, rechts=930),
    z("Annahme verstößt gegen Verbot/gute Sitten:", LX0, 781, beim("p817", "verstößt"), "Bold", 30, rechts=930),
    z("§ 817 Satz 1 BGB", LX0 + 30, 818, beim("p817", "Paragraf"), size=28, rechts=930),
    nein(LX0 + 14, 882, beim("aus", "Ausgeschlossen"), gr=16),
    z("Ausschluss: § 814 (Leistender wusste es),", LX0 + 40, 863, beim("aus", "Ausgeschlossen"), size=28, rechts=930),
    z("§ 817 Satz 2 (eigener Verstoß)", LX0 + 40, 900, "aus2", size=28, rechts=930),
    # rechter Ast: Nichtleistungskondiktionen
    z("Hauptfall: Eingriffskondiktion", RX0, 490, beim("nls", "Eingriffskondiktion"), "Bold", 32, rechts=1820),
    z("§ 812 I 1 Alt. 2 BGB", RX0 + 30, 535, beim("nls", "Paragraf"), "Bold", 30, rechts=1820),
    z("Eingriff in ein fremdes, zugewiesenes Recht", RX0 + 30, 577, "zw", size=28, rechts=1820),
    zit("BGH, Urt. v. 16.5.2013 – IX ZR 204/11, Rn. 15", RX0 + 30, 615, beim("zw", "zugewiesen"), rechts=1820),
    z("Werbung mit fremdem Bild: übliche Lizenzgebühr", RX0 + 30, 660, beim("foto", "Unternehmen"), size=28, rechts=1820),
    zit("BGH, Urt. v. 21.1.2021 – I ZR 120/19, Rn. 26", RX0 + 30, 698, beim("foto", "Lizenzgebühr"), rechts=1820),
    z("Sonderfall § 816 Abs. 1 Satz 1 BGB:", RX0, 750, "p816", "Bold", 30, rechts=1820),
    z("Nichtberechtigter verfügt wirksam: gibt das", RX0 + 30, 787, beim("p816", "Verfügt"), size=28, rechts=1820),
    z("durch die Verfügung Erlangte heraus", RX0 + 30, 822, beim("p816", "herausgeben"), size=28, rechts=1820),
    z("Außerdem: Rückgriffs- und Verwendungskondiktion", RX0, 880, "rv", size=28, rechts=1820),
])

# F Lösung des Falls: condictio indebiti --------------------------------------------------------------------------------
folie([("fl", "Fall · § 812 I 1 Alt. 1 BGB"), ("erl", "Fall › 1. etwas erlangt"), ("auftr", "Fall › 2. durch Leistung von Ursula"),
       ("org", "Fall › 3. ohne rechtlichen Grund"), ("k814", "Fall › 4. kein Ausschluss, § 814 BGB"),
       ("ci2", "Fall › condictio indebiti")], rechts_frei([
    *tafel("fl", "Der Fall: § 812 I 1 Alt. 1 BGB"),
    z("1. Etwas erlangt: Gutschrift über 500 €", 110, 180, beim("erl", "Gutschrift"), "Bold", 34),
    z("also ein Anspruch gegen seine Bank", 160, 230, beim("erl", "Anspruch"), size=32),
    zit("BGH, Urt. v. 5.3.2015 – IX ZR 164/14, Rn. 8", 160, 275, beim("erl", "Anspruch")),
    ok(86, 200, beim("erl", "Bank"), gr=18),
    z("2. Durch Leistung von Ursula?", 110, 330, "auftr", "Bold", 34),
    z("Auftrag selbst erteilt", 160, 380, beim("auftr", "selbst"), size=32),
    z("§ 675r Abs. 1 BGB: Ausführung nach der IBAN", 160, 425, beim("auftr", "IBAN"), size=32),
    z("BGH: versehentliche Fehlüberweisung = Leistung", 160, 475, beim("bgh", "Bundesgerichtshof"), "Bold", 32),
    zit("BGH, Urt. v. 5.3.2015 – IX ZR 164/14, Rn. 8, 10", 160, 520, beim("bgh", "Bundesgerichtshof")),
    ok(86, 350, beim("bgh", "Leistung"), gr=18),
    z("3. Ohne rechtlichen Grund: Ursula schuldet nichts", 110, 575, "org", "Bold", 34),
    ok(86, 595, beim("org", "nichts"), gr=18),
    z("4. Kein Ausschluss nach § 814 BGB:", 110, 645, "k814", "Bold", 34),
    z("Ursula wollte ihren Maler bezahlen", 160, 695, beim("k814", "wollte"), size=32),
    ok(86, 665, beim("k814", "wollte"), gr=18),
    blk(110, 760, 1040, 90, GRUEN, "ci2", [("condictio indebiti greift", "ExtraBold", 36, INK)]),
    *requisit([("fl", None, "Ursula gegen Rüdiger", WEISS),
               (beim("erl", "Gutschrift"), ("tabler", "building-bank", 120, WEISS), "Gutschrift 500 €", GRUEN),
               ("auftr", HANDY, "Auftrag von Ursula", LILA), (beim("bgh", "Leistung"), SCALE, "Leistung", BLAU),
               (beim("org", "schuldet"), ("tabler", "file-invoice", 100, WEISS), "keine Schuld", WEISS),
               ("ci2", GELD, "condictio indebiti", GRUEN)]),
    *paar("fl", [("fl", "ruhig"), ("auftr", "denkt"), ("ci2", "froh")], [("fl", "ruhig"), ("org", "sorge"), ("ci2", "ertappt")]),
]))

# G Ausblick Bankdreieck -----------------------------------------------------------------------------------------------
KI, BK, EM = (330, 330), (930, 330), (630, 610)     # Knoten: Kontoinhaber, Bank, Empfänger (Mitte)
folie([("dreieck", "Ausblick · Bankdreieck"), ("ohne", "Ausblick › ohne wirksamen Auftrag: keine Leistung"),
       ("direkt", "Ausblick › Nichtleistungskondiktion der Bank")], rechts_frei([
    *tafel("dreieck", "Ausblick: das Bankdreieck"),
    linienzug([KI, BK], "dreieck", breite=6), linienzug([BK, EM], "dreieck", breite=6), linienzug([KI, EM], "dreieck", breite=6),
    pl("Kontoinhaber", KI[0], KI[1] - 30, "dreieck", fill=LILA, size=30, anker="m"),
    pl("Bank", BK[0], BK[1] - 30, "dreieck", fill=WEISS, size=30, anker="m"),
    pl("Empfänger", EM[0], EM[1] - 30, "dreieck", fill=BLAU, size=30, anker="m"),
    pl("ohne wirksamen Auftrag", 630, 200, "ohne", fill=ROT, size=30, anker="m"),
    nein(630, 300, beim("ohne", "ohne"), gr=24),
    z("z. B. gefälschte Überweisung", 110, 700, beim("ohne", "gefälschte"), size=32),
    z("Kontoinhaber hat nichts geleistet", 110, 745, beim("ohne", "Kontoinhaber"), size=32),
    pfeil(850, 375, 665, 555, beim("direkt", "direkt"), breite=8, kopf=30, farbe=DGRUEN),
    pl("Nichtleistungskondiktion", 960, 655, beim("direkt", "Nichtleistungskondiktion"), fill=GRUEN, size=28, anker="m"),
    zit("BGH, Urt. v. 16.6.2015 – XI ZR 243/13, Rn. 18, 24", 110, 800, beim("direkt", "Nichtleistungskondiktion")),
    zit("BGH, Urt. v. 21.7.2026 – XI ZR 158/24, Rn. 11", 110, 840, beim("direkt", "Nichtleistungskondiktion")),
    *requisit([("dreieck", ("tabler", "building-bank", 130, WEISS), "Bank", WEISS),
               ("ohne", ("tabler", "ban", 120, ROT), "kein Auftrag", ROT),
               ("direkt", ("tabler", "arrow-back-up", 120, GRUEN), "Bank fordert zurück", GRUEN)]),
    *nur_ursula("dreieck", [("dreieck", "denkt"), ("direkt", "ruhig")]),
]))

# H1 Rechtsfolge § 818 Abs. 1, 2 --------------------------------------------------------------------------------------------
folie([("rf", "Rechtsfolge · §§ 818 ff. BGB"), ("rf1", "Rechtsfolge › Herausgabe, § 818 Abs. 1 BGB"),
       ("rf2", "Rechtsfolge › Wert, § 818 Abs. 2 BGB")], rechts_frei([
    *tafel("rf", "Rechtsfolge: §§ 818 ff. BGB"),
    z("§ 818 Abs. 1 BGB: das Erlangte herausgeben", 110, 200, "rf1", "Bold", 34),
    z("auch gezogene Nutzungen", 160, 255, beim("rf1", "gezogene"), size=34),
    z("§ 818 Abs. 2 BGB: Herausgabe nicht möglich?", 110, 350, "rf2", "Bold", 34),
    z("dann schuldet er den Wert", 160, 405, beim("rf2", "Wert"), size=34),
    z("etwa die Lizenzgebühr für das Bild", 160, 455, beim("rf2", "Lizenzgebühr"), size=34),
    zit("BGH, Urt. v. 21.1.2021 – I ZR 120/19, Rn. 24", 160, 505, beim("rf2", "Lizenzgebühr")),
    *requisit([("rf", ("tabler", "receipt-refund", 120, WEISS), "Rechtsfolge", WEISS),
               ("rf1", ("tabler", "arrow-back-up", 120, WEISS), "Herausgabe", GRUEN),
               (beim("rf2", "Wert"), ("tabler", "photo", 120, WEISS), "Wert", GELB)]),
    *paar("rf", [("rf", "ruhig"), ("rf2", "denkt")], [("rf", "denkt"), ("rf1", "ruhig")]),
]))

# H2 Entreicherung, verschärfte Haftung, § 822, Ergebnis -------------------------------------------------------------------
folie([("rf3", "Rechtsfolge › nicht mehr bereichert, § 818 Abs. 3 BGB"), ("rf5", "Rechtsfolge › Kenntnis, §§ 819 Abs. 1, 818 Abs. 4 BGB"),
       ("p822", "Rechtsfolge › Dritter, § 822 BGB"), ("erg", "Ergebnis")], rechts_frei([
    *tafel("rf3", "„Das Geld ist schon weg“"),
    z("§ 818 Abs. 3 BGB: nicht mehr bereichert?", 110, 180, "rf3", "Bold", 34),
    z("dann keine Herausgabe, kein Wertersatz", 160, 230, beim("rf3", "muss"), size=32),
    z("Rüdiger wusste: Das Geld steht ihm nicht zu", 110, 300, "rf4", "Bold", 34),
    z("§ 819 Abs. 1 BGB: Haftung wie bei Rechtshängigkeit", 110, 370, "rf5", "Bold", 32),
    z("§ 818 Abs. 4 BGB: kein Wegfall der Bereicherung", 110, 430, "rf6", "Bold", 32),
    nein(80, 200, beim("rf6", "nicht"), gr=18),
    zit("BGH, Urt. v. 11.8.2010 – XII ZR 102/09, Rn. 55", 160, 478, beim("rf6", "nicht")),
    z("§ 822 BGB: unentgeltlich weitergegeben und", 110, 545, "p822", "Bold", 32),
    z("Empfänger frei: Der Dritte gibt heraus", 160, 592, beim("p822", "frei"), size=32),
    blk(110, 670, 1040, 100, GRUEN, "erg", [("Rüdiger zahlt Ursula 500 € zurück", "ExtraBold", 36, INK)]),
    z("Das Wochenende am See hilft ihm nicht", 110, 800, beim("erg", "Wochenende"), size=32),
    *requisit([(beim("rf3", "Wer"), ("tabler", "beach", 150, GELB), "nicht mehr bereichert?", GELB),
               ("rf4", ("tabler", "eye", 120, WEISS), "wusste es", ROT),
               ("rf5", SCALE, "wie rechtshängig", ROT),
               ("p822", ("tabler", "gift", 120, WEISS), "§ 822 BGB", WEISS),
               ("erg", GELD, "500 € zurück", GRUEN)]),
    *paar("rf3", [("rf3", "sorge"), ("rf5", "denkt"), ("erg", "froh")], [("rf3", "froh"), ("rf4", "ertappt"), ("erg", "sorge")]),
]))

# I Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · Leistungskondiktion zuerst")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Prüfe zuerst die Leistungskondiktion!", 200, 200, beim("tipp", "Prüfe"), "Bold", 36),
    z("Frage ausdrücklich:", 150, 310, "tipp1", "Bold", 34),
    z("Wer hat aus Sicht des Empfängers", 185, 365, beim("tipp1", "Wer"), size=36),
    z("an wen geleistet?", 185, 415, beim("tipp1", "an"), size=36),
    z("Erst ohne Leistung:", 150, 520, "tipp2", "Bold", 34),
    z("Nichtleistungskondiktion", 185, 575, beim("tipp2", "Nichtleistungskondiktion"), size=36),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# J Klausurschema --------------------------------------------------------------------------------------------------------
K1, K2 = 150, 210
folie([("sch", "Klausurschema"), ("k2", "Klausurschema › Nichtleistungskondiktion"), ("k3", "Klausurschema › Rechtsfolge")], [
    karte(60, 50, 1800, 900, "sch"),
    titel(glyphen("Klausurschema: Bereicherungsrecht"), 110, 90, "sch", 44),
    z("I. Leistungskondiktion", K1, 200, "k1", "Bold", 38, rechts=1820),
    z("etwas erlangt, durch Leistung, ohne rechtlichen Grund", K2, 255, beim("k1", "etwas"), size=32, rechts=1820),
    z("kein Ausschluss nach §§ 814, 817 Satz 2 BGB", K2, 305, beim("k1", "kein"), size=32, rechts=1820),
    z("II. Nur ohne Leistung: Nichtleistungskondiktion", K1, 395, "k2", "Bold", 38, rechts=1820),
    z("etwas in sonstiger Weise auf Kosten des Anspruchstellers erlangt", K2, 450, beim("k2", "etwas"), size=32, rechts=1820),
    z("ohne rechtlichen Grund", K2, 500, beim("k2", "ohne", 2), size=32, rechts=1820),
    z("III. Rechtsfolge, §§ 818 ff. BGB", K1, 590, "k3", "Bold", 38, rechts=1820),
    z("Herausgabe oder Wertersatz, Entreicherung, verschärfte Haftung", K2, 645, beim("k3", "Herausgabe"), size=32, rechts=1820),
])

# K Merksatz (Lexi) -------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Erst fragen, ", 0), ("ob geleistet wurde", "a"), (",", 0)],
                 [("dann die passende Kondiktion wählen.", 0)]],
                750, 300, 40, "merke", {"a": beim("merke", "ob")}),
    *markertext([[("Wer den fehlenden Rechtsgrund kennt,", 0)],
                 [("kann sich ", 0), ("nicht auf Entreicherung", "b"), (" berufen.", 0)]],
                750, 520, 40, "m2", {"b": beim("m2", "nicht")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
