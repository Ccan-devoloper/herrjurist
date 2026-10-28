"""Folge 171 · Belehrungsverstoß: Ist das Geständnis verwertbar? – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A Bahnhof (Herr Pieper fährt mit dem fremden Rad los, Besitzerin, Polizeihauptmeister Lohmeyer
fragt „nur informatorisch“, erstes Geständnis), B Wache (ordnungsgemäße, aber nicht qualifizierte Belehrung, zweites Geständnis),
C Hauptverhandlung (Widerspruch der Verteidigerin, Fragen), D Sachverhalt, E/F 1. Schritt Beschuldigtenstellung (Maßstab, Fall),
G–K 2. Schritt Verwertungsverbot (Überblick, Abwägungslehre, Rechtskreistheorie, Schutzzwecklehre – gleiche Tafelstruktur –,
Ergebnis mit Verweis auf Folge 132), L–N 3. Schritt Fortwirkung (qualifizierte Belehrung, Abwägung, BGH-Fall gegen Fall Pieper),
O Fernwirkung und Ergebnis, P Klausurtipp mit Prüfungsaufbau (Lexi), Q Merksatz (Lexi).
Geräusch nur bei sichtbarer Handlung: Freilauf des Rades, als Herr Pieper losfährt (Freesound CC0). Hilfsfunktionen
glyphen/z/pl/fb/tafel/wortlaut/redet/namensschild als eigene Kopie aus Folge 132 (gemeinsame Dateien unverändert).
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlautkarten wörtlich nach dem amtlichen Leitsatz."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont

bausteine.FIGORDNER = "op_171/"

_run0 = bausteine._sp.run


def _run_c(args, **k):
    """Sprechblasen müssen im Stil C gelingen (kein stiller Rückfall auf Stil E)."""
    r = _run0(args, **k)
    if len(args) > 1 and str(args[1]).endswith("blase_c.js"):
        assert r.returncode == 0, f"Blase Stil C fehlgeschlagen: {args[2]}"
    return r


bausteine._sp.run = _run_c

FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
ROTHELL = (253, 232, 228, 255)
GRUENHELL = (232, 247, 233, 255)
BLAUHELL = (232, 240, 253, 255)
HOLZ = (214, 160, 110, 255)
DAUER = bausteine._cj()["dauer"]
NULL = ("fall", -round(bausteine._t("fall") + 0.4, 3))   # 0,4 s vor Hauptfilmbeginn: ab 0,0 s voll sichtbar

_CMAP = set(TTFont(SP + "humaaans/fonts/Nunito[wght].ttf").getBestCmap())


def glyphen(text):
    """Nunito muss jedes Zeichen haben (sonst Kästchen)."""
    fehl = {c for c in text if ord(c) not in _CMAP and not c.isspace()}
    assert not fehl, f"Zeichen fehlt in Nunito: {fehl} in {text!r}"
    return text


def z(text, x, y, cue, stil="Regular", size=34, farbe=INK, d=0.0, rechts=1170, **k):
    """Tafelzeile, die rechts nicht über die Karte hinausragen darf (mobil: mindestens 26 px)."""
    assert size >= 26, f"Schrift zu klein für mobile Lesbarkeit: {text}"
    e = zeile(glyphen(text), x, y, cue, stil, size, farbe=farbe, d=d, **k)
    assert e.x + e.sprite.width <= rechts, f"Zeile zu breit: {text} ({e.x + e.sprite.width:.0f} > {rechts})"
    return e


def pl(text, *a, **k):
    assert k.get("size", 40) >= 26, f"Pille zu klein: {text}"
    return pille(glyphen(text), *a, **k)


def fb(x, y, w, h, fill, cue, zeilen, **k):
    for t, s, g, _ in zeilen:
        glyphen(t)
        assert F(s, g).getlength(t) <= w - 30, f"Blockzeile zu breit: {t}"
    return fl_block(x, y, w, h, fill, cue, zeilen, **k)


def tafel(cue, titel_, h=840, fill=WEISS, size=46):
    """Rechtstafel links, rechts bleibt Platz für die Figuren."""
    assert 110 + F("ExtraBold", size).getlength(glyphen(titel_)) <= 1170, f"Titel zu breit: {titel_}"
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(titel_, 110, 100, cue, size)]


def wortlaut(x, y, w, h, cue, zeilen, size, hl, quelle, quelle_cue=None):
    """Wortlautkarte: wörtliches Zitat (gesetze-im-internet.de bzw. amtlicher Volltext, Abruf 04.10.2026) in einer hellen
    Karte, Fundstelle darunter rechts. zeilen = Liste von Token-Listen [(text, Schlüssel|0)], hl = {Schlüssel: Cue}."""
    for toks in zeilen:
        glyphen("".join(t for t, _ in toks))
    els = [karte(x, y, w, h, cue, fill=(246, 246, 250, 255), rund=18, schatten=6, rand=4)]
    m = markertext(zeilen, x + w / 2, y + 22, size, cue, hl, marker=GELB, lh=1.28)
    assert m[0].x >= x + 10 and m[0].x + m[0].sprite.width <= x + w - 10, f"Wortlaut zu breit ({m[0].sprite.width} > {w})"
    assert m[0].y + m[0].sprite.height <= y + h + 6, "Wortlaut zu hoch"
    els += m
    q = zeile(glyphen(quelle), 0, 0, quelle_cue or cue, "Bold", 26, farbe=TEXT)
    q.x = x + w - q.sprite.width - 24; q.y = y + h + 8
    els.append(q)
    return els


def lexi_bis_ende(cue):
    return (cue, round(DAUER - bausteine._t(cue) - 0.05, 3))


def rechts_frei(els, x0=1250):
    """Figuren und Requisiten der Tafelfolien stehen rechts der Tafel (x ≥ 1250)."""
    for e in els:
        n = e.name or ""
        if n.startswith(("bild:", "ficon:")) or "/op_171/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def namensschild(text, cx, unten, cue, fill, **k):
    return pille(glyphen(text), cx, unten + 22, cue, fill=fill, size=30, anker="m", **k)


def hart(e):
    e.anim = "cut"
    return e


def fund(text, x, y, cue, rechts=1170):
    return z(text, x, y, cue, size=26, farbe=TEXT, rechts=rechts)


# --- Eigene Hilfsfunktion (wie Folge 072): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ---------------
import wave as _wave
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
    """Wie bausteine.redet(), aber Wortende = hörbares Ende; Viseme aus der Schreibung geschätzt (kein Phonem-Alignment)."""
    cj = bausteine._cj(); ta, tb = bausteine._t(cue), bausteine._t(bis)
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


BODEN, FH = 880, 480
BR, FR = 930, 480                       # Figuren rechts neben der Tafel
X1, X2 = 1390, 1730                     # zwei Figuren neben der Tafel
MB = (X1 + X2) // 2
XS = 1600                               # eine Figur allein neben der Tafel


def hand(name, cx, unten, hoehe, seite):
    """Position der ausgestreckten Hand (äußerster Pixel links/rechts im oberen Körperdrittel) für ein Requisit."""
    e = peep_voll(name, cx, unten, hoehe, "_")
    a = np.asarray(e.sprite)[:, :, 3] > 20
    h = a.shape[0]
    band = a[int(h * 0.25):int(h * 0.55)]
    ys, xs = np.nonzero(band)
    x = xs.min() if seite < 0 else xs.max()
    y = int(np.median(ys[xs == x])) + int(h * 0.25)
    return e.x + x, e.y + y


def bis_(e, bis):
    e.bis = bis
    return e


def weg(e, s0, s1, dx, dy=0):
    """Bewegung: bis s0 um (dx, dy) versetzt, bis s1 an die Endposition (Renderer: versatz())."""
    e.weg = (s0, s1, dx, dy)
    return e


import math as _m
def buegel(cx, b=60, h=120):
    """Anlehnbügel eines Fahrradständers als Tuschelinie (umgedrehtes U)."""
    r = b / 2
    pts = [(cx - r, BODEN), (cx - r, BODEN - h + r)]
    pts += [(cx - r * _m.cos(a / 12 * _m.pi), BODEN - h + r - r * _m.sin(a / 12 * _m.pi)) for a in range(1, 12)]
    return pts + [(cx + r, BODEN - h + r), (cx + r, BODEN)]


# A Fall: am Bahnhof ---------------------------------------------------------------------------------------------------------
PX, LX_, BX = 780, 1340, 1720           # Herr Pieper (auf dem Rad), Polizeihauptmeister Lohmeyer, Besitzerin
FAHRT = (beim("rad", "fährt"), beim("frau", "Da"), -170)
PIRa = ("PIR_redet_r", PX, BODEN, FH)
LOa = ("LO_redet", LX_, BODEN, FH)
BEa = ("BE_redet", BX, BODEN, FH)
_pi0 = peep_voll("PIR_ruhig_r", PX, BODEN, FH, NULL, anim="cut", bis="frau")
korb = (_pi0.x + _pi0.sprite.width * 0.785, _pi0.y + _pi0.sprite.height * 0.37)   # Korb vorn am Lenker (Rad blickt nach rechts)
folie([(NULL, "Fall · Am Bahnhof"), ("rad", "Fall · Herr Pieper fährt los"), ("frau", "Fall · Die Besitzerin"),
       ("pol", "Fall · Die Polizei hält ihn an"), ("schloss", "Fall · Schloss aufgebrochen, kein Schlüssel"),
       ("keinbel", "Fall · Keine Belehrung"), ("l1", "Fall · „Nur informatorisch gefragt“"), ("p1", "Fall · Das erste Geständnis")], [
    hart(linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK)),
    pl("Bahnhof · Montagmorgen", 70, 40, NULL, fill=GELB, size=40, anim="cut"),
    ficon("tabler", "train", 1700, 330, 170, NULL, fuell=BLAU, anim="cut", bis="frau"),
    *[hart(linienzug(buegel(x), NULL, breite=7, farbe=INK)) for x in (110, 200, 290)],
    pl("Fahrradständer", 200, BODEN - 200, beim("rad", "Fahrradständer"), fill=WEISS, size=28, anker="m"),
    weg(_pi0, *FAHRT),
    peep_voll("PIR_sorge_r", PX, BODEN, FH, "frau", anim="cut", bis="p1"),
    *redet("PIR_redet_r", PX, BODEN, FH, "p1", "wache"),
    weg(namensschild("Herr Pieper", PX, BODEN, NULL, GELB, anim="cut"), *FAHRT),
    szene(pl("blaues Damenrad", PX + 140, 300, beim("rad", "blauen"), fill=BLAUHELL, size=28, anker="m", bis="frau"),
          "171rad*", 1.0, versatz=-0.35),
    peep_voll("BE_ernst", BX, BODEN, FH, "frau", bis="b1"),
    *redet("BE_redet", BX, BODEN, FH, "b1", "pol"),
    peep_voll("BE_ernst", BX, BODEN, FH, "pol", anim="cut"),
    namensschild("Besitzerin", BX, BODEN, "frau", LILA),
    blase("sprech", 820, 200, "b1", 1180, 200, inhalt=["Halt! Das ist mein Rad!", "Mein Schloss liegt aufgebrochen im Korb!"],
          textsize=30, figur=BEa, bis="pol"),
    peep_voll("LO_ruhig", LX_, BODEN, FH, "pol", bis="l1"),
    *redet("LO_redet", LX_, BODEN, FH, "l1", "p1"),
    peep_voll("LO_denkt", LX_, BODEN, FH, "p1", anim="cut"),
    namensschild("Polizeihauptmeister Lohmeyer", LX_, BODEN, "pol", BLAU),
    ficon("tabler", "lock-open", korb[0], korb[1], 56, beim("schloss", "aufgebrochene"), fuell=ROT),
    pl("Schloss aufgebrochen im Korb", 70, 130, beim("schloss", "aufgebrochene"), fill=WEISS, size=30, bis="wache"),
    pl("kein Schlüssel", 70, 200, beim("schl", "Schlüssel"), fill=WEISS, size=30, bis="wache"),
    pl("keine Belehrung", 115, 270, "keinbel", fill=ROTHELL, size=30, bis="wache"),
    nein(90, 290, beim("keinbel", "nicht"), gr=18),
    blase("sprech", 660, 200, "l1", 1120, 200, inhalt=["Nur informatorisch gefragt:", "Wem gehört das Rad?"], textsize=32,
          figur=LOa, bis="p1"),
    blase("sprech", 700, 200, "p1", 980, 200, inhalt=["Nicht mir. Ich hab es mir genommen,", "ich war spät dran."],
          textsize=30, figur=PIRa, bis="wache"),
])

# B Fall: auf der Wache -----------------------------------------------------------------------------------------------------------
WX, PWX = 560, 1300                      # Lohmeyer hinter dem Schreibtisch, Herr Pieper davor
folie([("wache", "Fall · Auf der Wache"), ("belehrt", "Fall · Belehrung: Schweigerecht, Verteidiger"),
       ("nichtges", "Fall · Kein Hinweis auf das erste Geständnis"), ("p2", "Fall · Das zweite Geständnis")], [
    hart(linienzug([(60, BODEN), (1860, BODEN)], "wache", breite=7, farbe=INK)),
    pl("Polizeiwache · eine Stunde später", 70, 40, "wache", fill=GELB, size=40, anim="cut"),
    peep_voll("LO_ruhig_r", WX, BODEN, FH, "wache", anim="cut", bis="nichtges"),
    peep_voll("LO_ernst_r", WX, BODEN, FH, "nichtges", anim="cut"),
    hart(karte(WX - 260, BODEN - 235, 520, 233, "wache", fill=HOLZ, rund=10, schatten=6)),
    ficon("tabler", "notebook", WX + 150, BODEN - 235, 80, "wache", fuell=WEISS, anim="cut"),
    namensschild("Polizeihauptmeister Lohmeyer", WX, BODEN, "wache", BLAU, anim="cut"),
    peep_voll("PI_ruhig", PWX, BODEN, FH, "wache", anim="cut", bis="nichtges"),
    peep_voll("PI_muede", PWX, BODEN, FH, "nichtges", anim="cut", bis="p2"),
    *redet("PI_redet", PWX, BODEN, FH, "p2", "hv"),
    namensschild("Herr Pieper", PWX, BODEN, "wache", GELB, anim="cut"),
    ok(95, 165, beim("belehrt", "schweigen"), gr=18),
    pl("Schweigerecht", 130, 140, beim("belehrt", "schweigen"), fill=GRUENHELL, size=30),
    ok(95, 235, beim("belehrt", "Verteidiger"), gr=18),
    pl("Verteidiger befragen", 130, 210, beim("belehrt", "Verteidiger"), fill=GRUENHELL, size=30),
    nein(95, 305, beim("nichtges", "sagt"), gr=18),
    pl("kein Hinweis: erstes Geständnis unverwertbar", 130, 280, "nichtges", fill=ROTHELL, size=30),
    blase("sprech", 680, 200, "p2", 1500, 220, inhalt=["Hab ich doch schon gesagt.", "Ich habe das Rad genommen."],
          textsize=32, figur=("PI_redet", PWX, BODEN, FH), bis="hv"),
])

# C Fall: Hauptverhandlung ---------------------------------------------------------------------------------------------------------
GX, VX, AX = 420, 1080, 1460             # Richtertisch, Verteidigerin, Herr Pieper
folie([("hv", "Fall · Hauptverhandlung: Widerspruch"), ("frage", "Fall · Die Fragen")], [
    hart(linienzug([(60, BODEN), (1860, BODEN)], "hv", breite=7, farbe=INK)),
    pl("Hauptverhandlung", 70, 40, "hv", fill=GELB, size=40, anim="cut"),
    hart(karte(GX - 230, BODEN - 235, 460, 233, "hv", fill=HOLZ, rund=10, schatten=6)),
    ficon("tabler", "gavel", GX, BODEN - 235, 110, "hv", fuell=HOLZ, anim="cut"),
    pl("Gericht", GX, BODEN - 120, "hv", fill=WEISS, size=30, anker="m", anim="cut"),
    peep_voll("VE_ruhig", VX, BODEN, FH, "hv", anim="cut", bis=beim("hv", "widerspricht")),
    peep_voll("VE_ernst", VX, BODEN, FH, beim("hv", "widerspricht"), anim="cut", bis="frage"),
    peep_voll("VE_denkt", VX, BODEN, FH, "frage", anim="cut"),
    namensschild("Verteidigerin", VX, BODEN, "hv", WEISS, anim="cut"),
    peep_voll("PI_ruhig", AX, BODEN, FH, "hv", anim="cut", bis="frage"),
    peep_voll("PI_denkt", AX, BODEN, FH, "frage", anim="cut"),
    namensschild("Herr Pieper", AX, BODEN, "hv", GELB, anim="cut"),
    ficon("tabler", "hand-stop", 820, 390, 90, beim("hv", "widerspricht"), fuell=WEISS, bis="frage"),
    pl("Widerspruch: beide Geständnisse", 820, 250, beim("hv", "widerspricht"), fill=WEISS, size=28, anker="m", bis="frage"),
    pl("Darf das Gericht das erste Geständnis verwerten?", 1060, 150, "frage", fill=WEISS, size=34, anker="m"),
    pl("Und das zweite?", 1060, 235, "frage2", fill=GELB, size=34, anker="m"),
])

# D Sachverhalt ----------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    glyphen("Montagmorgen am Bahnhof fährt Herr Pieper auf einem fremden blauen Damenrad los. Die Besitzerin ruft, ihr Schloss "
            "liege aufgebrochen im Korb. Polizeihauptmeister Lohmeyer hält ihn an: Im Korb liegt das aufgebrochene Schloss, "
            "einen Schlüssel hat Herr Pieper nicht. Ohne Belehrung fragt Lohmeyer „nur informatorisch“, wem das Rad gehört. "
            "Herr Pieper gesteht."),
    glyphen("Eine Stunde später belehrt ihn Lohmeyer auf der Wache ordnungsgemäß über Schweigerecht und Verteidiger, sagt aber "
            "nicht, dass das erste Geständnis unverwertbar ist. Herr Pieper wiederholt: „Hab ich doch schon gesagt. Ich habe "
            "das Rad genommen.“ In der Hauptverhandlung widerspricht seine Verteidigerin rechtzeitig der Verwertung beider "
            "Geständnisse."),
], "Darf das Gericht das erste Geständnis verwerten – und das zweite?")

# E 1. Schritt: Beschuldigtenstellung – Maßstab -------------------------------------------------------------------------------
P1 = "1. Schritt: Beweiserhebungsverbot"
folie([("besch", f"{P1} › nur Beschuldigte belehren"), ("akt", f"{P1} › Willensakt (Inkulpationsakt)"),
       ("staerke", f"{P1} › ohne Akt: Stärke des Verdachts"), ("spiel", f"{P1} › Spielraum der Polizei"),
       ("grenze", f"{P1} › Grenze: Willkür")], rechts_frei([
    *tafel("besch", "1. Schritt: War Herr Pieper Beschuldigter?"),
    z("Über das Schweigerecht belehren: nur Beschuldigte", 110, 175, "besch", "Bold", 32),
    fund("§ 163a Abs. 4 S. 2 i. V. m. § 136 Abs. 1 S. 2 StPO", 150, 220, beim("besch", "Beschuldigten")),
    z("Willensakt der Strafverfolger (Inkulpationsakt),", 110, 290, "akt", "Bold", 32),
    z("z. B. förmliches Ermittlungsverfahren, Durchsuchung", 150, 337, "akt2", size=30),
    fund("BGH, Urt. v. 3.7.2007 – 1 StR 3/07, Rn. 17 f. (BGHSt 51, 367)", 150, 380, beim("akt2", "Durchsuchung")),
    z("Auch ohne Akt: belehren, wenn der Verdacht stark genug ist", 110, 450, "staerke", "Bold", 30),
    z("Kommt er ernstlich als Täter in Betracht? Spielraum der Polizei", 110, 500, "spiel", size=30),
    fund("BGH, Urt. v. 18.12.2008 – 4 StR 455/08, Rn. 8 f. (BGHSt 53, 112)", 150, 543, beim("spiel", "Spielraum")),
    fb(110, 610, 1040, 140, GELB, "grenze", [("Wäre alles andere willkürlich:", "ExtraBold", 34, INK),
                                            ("als Beschuldigten vernehmen", "ExtraBold", 34, INK)]),
    peep_voll("LO_ruhig", X1, BR, FR, "besch", bis="spiel"),
    peep_voll("LO_denkt", X1, BR, FR, "spiel", anim="cut", bis="grenze"),
    peep_voll("LO_ernst", X1, BR, FR, "grenze", anim="cut"),
    peep_voll("PI_ruhig", X2, BR, FR, "besch", d=0.2, bis="staerke"),
    peep_voll("PI_denkt", X2, BR, FR, "staerke", anim="cut"),
    namensschild("Polizeihauptmeister Lohmeyer", X1 - 70, BR, "besch", BLAU, d=0.2),
    namensschild("Herr Pieper", X2 + 40, BR, "besch", GELB, d=0.3),
    ficon("tabler", "user-question", MB, 380, 100, "besch", fuell=WEISS, bis="akt"),
    pl("nur Beschuldigte", MB, 160, "besch", fill=WEISS, size=28, anker="m", bis="akt"),
    ficon("tabler", "folder-open", MB, 380, 100, "akt", fuell=GELB, anim="cut", bis=beim("akt2", "Durchsuchung")),
    pl("Inkulpationsakt", MB, 160, beim("akt", "Inkulpationsakt"), fill=GELB, size=28, anker="m", bis="staerke"),
    ficon("tabler", "search", MB, 380, 100, beim("akt2", "Durchsuchung"), fuell=WEISS, anim="cut", bis="staerke"),
    ficon("tabler", "scale", MB, 380, 110, "staerke", fuell=GELB, anim="cut", bis="grenze"),
    pl("Stärke des Verdachts", MB, 160, "staerke", fill=GELB, size=28, anker="m", anim="cut", bis="spiel"),
    pl("Spielraum", MB, 160, "spiel", fill=BLAUHELL, size=28, anker="m", anim="cut", bis="grenze"),
    ficon("tabler", "alert-triangle", MB, 380, 100, "grenze", fuell=GELB, anim="cut"),
    pl("Grenze: willkürlich", MB, 160, "grenze", fill=ROTHELL, size=28, anker="m", anim="cut"),
]))

# F 1. Schritt im Fall ------------------------------------------------------------------------------------------------------------
folie([("sub", f"{P1} › im Fall"), ("jabesch", f"{P1} › Herr Pieper war Beschuldigter"),
       ("etik", f"{P1} › „informatorisch“ ändert nichts"), ("gegen", f"{P1} › vager Verdacht: Zeuge"),
       ("fehlt", f"{P1} › Belehrung fehlte")], rechts_frei([
    *tafel("sub", "1. Schritt im Fall"),
    ok(140, 195, beim("sub", "zeigt"), gr=18),
    z("Die Besitzerin zeigt auf ihr Rad.", 175, 175, beim("sub", "zeigt"), "Bold", 30),
    ok(140, 250, beim("sub", "Schloss"), gr=18),
    z("Das Schloss liegt aufgebrochen im Korb.", 175, 230, beim("sub", "Schloss"), "Bold", 30),
    ok(140, 305, beim("sub", "Schlüssel"), gr=18),
    z("Einen Schlüssel hat Herr Pieper nicht.", 175, 285, beim("sub", "Schlüssel"), "Bold", 30),
    fb(110, 360, 1040, 100, GRUEN, "jabesch", [("Herr Pieper war Beschuldigter.", "ExtraBold", 36, INK)]),
    z("Das Wort „informatorisch“ ändert daran nichts.", 110, 490, "etik", size=30),
    z("Nur vager Verdacht: Befragung als Zeuge zulässig", 110, 560, "gegen", size=30),
    fund("vgl. BGHSt 53, 112 Rn. 16; BGH 1 StR 3/07, Rn. 18", 150, 603, beim("gegen", "Zeuge")),
    nein(150, 700, beim("fehlt", "fehlte"), gr=20),
    z("Belehrung über Schweigerecht und Verteidiger fehlte", 185, 680, "fehlt", "Bold", 30),
    peep_voll("BE_ruhig", X1, BR, FR, "sub", bis="gegen"),
    peep_voll("BE_ernst", X1, BR, FR, "gegen", anim="cut"),
    namensschild("Besitzerin", X1 - 40, BR, "sub", LILA, d=0.2),
    peep_voll("PI_ruhig", X2, BR, FR, "sub", d=0.2, bis="jabesch"),
    peep_voll("PI_sorge", X2, BR, FR, "jabesch", anim="cut", bis="gegen"),
    peep_voll("PI_muede", X2, BR, FR, "gegen", anim="cut"),
    namensschild("Herr Pieper", X2 + 30, BR, "sub", GELB, d=0.3),
    ficon("tabler", "hand-finger", MB, 380, 90, "sub", fuell=WEISS, bis=beim("sub", "Schloss")),
    ficon("tabler", "lock-open", MB, 380, 90, beim("sub", "Schloss"), fuell=ROT, anim="cut", bis=beim("sub", "Schlüssel")),
    ficon("tabler", "key-off", MB, 380, 90, beim("sub", "Schlüssel"), fuell=WEISS, anim="cut", bis="jabesch"),
    pl("starker Verdacht", MB, 160, beim("sub", "Schlüssel"), fill=GELB, size=28, anker="m", bis="jabesch"),
    ficon("tabler", "circle-check", MB, 380, 100, "jabesch", fuell=GRUEN, anim="cut", bis="etik"),
    pl("Beschuldigter", MB, 160, "jabesch", fill=GRUEN, size=28, anker="m", anim="cut", bis="etik"),
    ficon("tabler", "tag", MB, 380, 100, "etik", fuell=GELB, anim="cut", bis="gegen"),
    pl("„informatorisch“?", MB, 160, "etik", fill=GELB, size=28, anker="m", anim="cut", bis="gegen"),
    ficon("tabler", "user-question", MB, 380, 100, "gegen", fuell=WEISS, anim="cut", bis="fehlt"),
    pl("vager Verdacht: Zeuge", MB, 160, "gegen", fill=BLAUHELL, size=28, anker="m", anim="cut", bis="fehlt"),
    ficon("tabler", "circle-x", MB, 380, 100, "fehlt", fuell=ROT, anim="cut"),
    pl("Belehrung fehlte", MB, 160, "fehlt", fill=ROTHELL, size=28, anker="m", anim="cut"),
]))

# G 2. Schritt: Verwertungsverbot – Überblick --------------------------------------------------------------------------------
P2 = "2. Schritt: Verwertungsverbot"
folie([("vv", f"{P2} › Folgt ein Verwertungsverbot?"), ("lehren", f"{P2} › drei Lehren")], rechts_frei([
    *tafel("vv", "2. Schritt: Verwertungsverbot?"),
    z("Folgt aus dem Fehler ein Verwertungsverbot?", 110, 175, "vv", "Bold", 34),
    z("Das Gesetz regelt das hier nicht ausdrücklich.", 110, 240, beim("vv", "Ausdrücklich"), size=30),
    fund("vgl. BGHSt 38, 214, 219", 150, 283, beim("vv", "Ausdrücklich")),
    fb(110, 380, 1040, 110, BLAUHELL, "lehren", [("Drei Lehren stehen sich gegenüber.", "ExtraBold", 36, INK)]),
    peep_voll("VE_ruhig", X1, BR, FR, "vv", bis="lehren"),
    peep_voll("VE_denkt", X1, BR, FR, "lehren", anim="cut"),
    namensschild("Verteidigerin", X1 - 40, BR, "vv", WEISS, d=0.2),
    peep_voll("PI_denkt", X2, BR, FR, "vv", d=0.2),
    namensschild("Herr Pieper", X2 + 30, BR, "vv", GELB, d=0.3),
    ficon("tabler", "help-circle", MB, 380, 100, "vv", fuell=WEISS, bis="lehren"),
    pl("Verwertungsverbot?", MB, 160, "vv", fill=WEISS, size=28, anker="m", bis="lehren"),
    ficon("tabler", "messages", MB, 380, 100, "lehren", fuell=BLAUHELL, anim="cut"),
    pl("drei Lehren", MB, 160, "lehren", fill=BLAUHELL, size=28, anker="m", anim="cut"),
]))


def lehre(cues, pfade, titel_, wer, ansatz, mass, mass_fund, fall, icon, ve, pi):
    """Eine Lehre je Tafel in gleicher Struktur: Titel, Fundstelle/Herkunft, Ansatz, Maßstab mit Fundstelle, Im Fall (Haken)."""
    c0, c_ans, c_mass, c_fall = cues
    els = [*tafel(c0, titel_),
           fund(wer, 110, 160, c0),
           z("Ansatz:", 110, 225, c_ans, "ExtraBold", 30, farbe=TEXT)]
    y = 270
    for t, c in ansatz:
        els.append(z(t, 150, y, c, "Bold", 32)); y += 48
    y += 22
    els.append(z("Maßstab:", 110, y, c_mass, "ExtraBold", 30, farbe=TEXT)); y += 45
    for t, c in mass:
        els.append(z(t, 150, y, c, size=30)); y += 44
    els.append(fund(mass_fund[0], 150, y + 2, mass_fund[1])); y += 70
    els.append(z("Im Fall:", 110, y, c_fall, "ExtraBold", 30, farbe=TEXT)); y += 45
    els.append(fb(110, y, 1040, 46 * len(fall) + 50, GRUENHELL, c_fall, [(t, "ExtraBold", 32, INK) for t in fall]))
    els.append(ok(1110, y + 20 + 23 * len(fall), c_fall, gr=18))
    assert y + 46 * len(fall) + 50 <= 900, f"Lehre-Tafel zu hoch: {titel_}"
    nx = [n for n, _ in ve]
    for i, (n, c) in enumerate(ve):
        els.append(peep_voll(n, X1, BR, FR, c, anim=("pop" if i == 0 else "cut"), bis=(ve[i + 1][1] if i + 1 < len(ve) else None)))
    for i, (n, c) in enumerate(pi):
        els.append(peep_voll(n, X2, BR, FR, c, anim=("pop" if i == 0 else "cut"), d=(0.2 if i == 0 else 0.0),
                             bis=(pi[i + 1][1] if i + 1 < len(pi) else None)))
    els += [namensschild("Verteidigerin", X1 - 40, BR, c0, WEISS, d=0.2), namensschild("Herr Pieper", X2 + 30, BR, c0, GELB, d=0.3)]
    for i, (ic, fill, txt, pfill, c) in enumerate(icon):
        b = icon[i + 1][4] if i + 1 < len(icon) else None
        els.append(ficon("tabler", ic, MB, 380, 100, c, fuell=fill, anim=("pop" if i == 0 else "cut"), bis=b))
        els.append(pl(txt, MB, 160, c, fill=pfill, size=28, anker="m", anim=("pop" if i == 0 else "cut"), bis=b))
    folie(pfade, rechts_frei(els))


# H Lehre 1: Abwägungslehre ----------------------------------------------------------------------------------------------------
lehre(("abw", "abw", "abw4", "abw5"),
      [("abw", f"{P2} › Abwägungslehre"), ("abw4", f"{P2} › Abwägungslehre: Grundlagen der Stellung"),
       ("abw5", f"{P2} › Abwägungslehre im Fall")],
      "Lehre 1: Abwägungslehre", "Rechtsprechung: BGH, Urt. v. 14.8.2009 – 3 StR 552/08, Rn. 47 (BGHSt 54, 69)",
      [("Abwägung: Art des Verbots, Gewicht des Verstoßes", "abw2"), ("gegen das Interesse an der Aufklärung der Tat", "abw3")],
      [("Verbot liegt nahe, wenn die Vorschrift die Grundlagen", "abw4"), ("der Stellung des Beschuldigten sichert", beim("abw4", "der"))],
      ("BGHSt 38, 214, 220", beim("abw4", "sichert")),
      ["Die Belehrung über das Schweigerecht", "sichert genau diese Grundlagen."],
      [("scale", GELB, "Abwägung", GELB, "abw"), ("shield-check", BLAUHELL, "Stellung des Beschuldigten", BLAUHELL, "abw4"),
       ("circle-check", GRUEN, "hier: ja", GRUEN, "abw5")],
      [("VE_ruhig", "abw"), ("VE_denkt", "abw4"), ("VE_froh", "abw5")],
      [("PI_ruhig", "abw"), ("PI_denkt", "abw3")])

# I Lehre 2: Rechtskreistheorie ------------------------------------------------------------------------------------------------
lehre(("rk", "rk", "rk2", "rk3"),
      [("rk", f"{P2} › Rechtskreistheorie"), ("rk2", f"{P2} › Rechtskreistheorie: Schutz des Betroffenen"),
       ("rk3", f"{P2} › Rechtskreistheorie im Fall")],
      "Lehre 2: Rechtskreistheorie", "Rechtsprechung: BGH (GrS), Beschl. v. 21.1.1958 – GSSt 4/57, BGHSt 11, 213, 215",
      [("Berührt der Fehler den Rechtskreis dessen,", "rk"), ("der sich darauf beruft?", beim("rk", "der", 2))],
      [("Dient die verletzte Vorschrift nicht seinem Schutz:", "rk2"), ("für ihn kein Verwertungsverbot", beim("rk2", "folgt"))],
      ("BGH, Beschl. v. 5.7.2022 – 4 StR 61/22, Rn. 12", beim("rk2", "Verwertungsverbot")),
      ["Die Belehrung schützt gerade Herrn Pieper."],
      [("user-shield", BLAUHELL, "Rechtskreis", BLAUHELL, "rk"), ("shield", WEISS, "Schutz wem?", WEISS, "rk2"),
       ("circle-check", GRUEN, "hier: Herr Pieper", GRUEN, "rk3")],
      [("VE_ruhig", "rk"), ("VE_denkt", "rk2"), ("VE_froh", "rk3")],
      [("PI_ruhig", "rk"), ("PI_froh", "rk3")])

# J Lehre 3: Schutzzwecklehre ----------------------------------------------------------------------------------------------------
lehre(("sz", "sz", "sz3", "sz4"),
      [("sz", f"{P2} › Schutzzwecklehre"), ("sz3", f"{P2} › Schutzzwecklehre: Zweck der Belehrung"),
       ("sz4", f"{P2} › Schutzzwecklehre im Fall")],
      "Lehre 3: Schutzzwecklehre", "Ansicht im Schrifttum",
      [("Zweck der verletzten Norm:", "sz"), ("Würde die Verwertung ihn unterlaufen?", "sz2")],
      [("Die Belehrung soll verhindern, dass sich jemand", "sz3"), ("unwissentlich selbst belastet", beim("sz3", "unwissentlich"))],
      ("vgl. BGHSt 53, 112 Rn. 13 (Recht zu schweigen, nemo tenetur)", beim("sz3", "belastet")),
      ["Genau diese Selbstbelastung würde verwertet."],
      [("target", ROTHELL, "Schutzzweck", ROTHELL, "sz"), ("microphone-off", WEISS, "Selbstbelastung", WEISS, "sz3"),
       ("circle-check", GRUEN, "Zweck unterlaufen", GRUEN, "sz4")],
      [("VE_ruhig", "sz"), ("VE_denkt", "sz2"), ("VE_ernst", "sz4")],
      [("PI_ruhig", "sz"), ("PI_sorge", "sz3")])

# K 2. Schritt: Ergebnis des Streits, Widerspruch, Verweis Folge 132 ----------------------------------------------------------
folie([("gleich", f"{P2} › alle drei: unverwertbar"), ("streit", f"{P2} › Streit nicht entscheiden"),
       ("wid", f"{P2} › Widerspruch rechtzeitig"), ("verw", f"{P2} › siehe Folge 132")], rechts_frei([
    *tafel("gleich", "2. Schritt: Ergebnis"),
    *[e for i, n in enumerate(("Abwägungslehre", "Rechtskreistheorie", "Schutzzwecklehre"))
      for e in (z(n, 175, 175 + 52 * i, "gleich", "Bold", 32), ok(140, 195 + 52 * i, "gleich", gr=16))],
    fb(110, 345, 1040, 100, GRUEN, beim("gleich", "Das"), [("Das erste Geständnis ist unverwertbar.", "ExtraBold", 34, INK)]),
    z("Gleiches Ergebnis: Den Streit nicht entscheiden.", 110, 480, "streit", "Bold", 32),
    z("Verteidigter Angeklagter: nur bei rechtzeitigem Widerspruch", 110, 555, "wid", size=30),
    ok(140, 625, beim("wid", "den"), gr=18),
    z("hier: Die Verteidigerin hat widersprochen.", 175, 605, beim("wid", "den"), "Bold", 30),
    fb(110, 690, 1040, 100, BLAUHELL, "verw", [("Mehr dazu: Folge 132 · Widerspruchslösung", "ExtraBold", 32, INK)]),
    peep_voll("VE_froh", X1, BR, FR, "gleich", bis="wid"),
    peep_voll("VE_ernst", X1, BR, FR, "wid", anim="cut"),
    namensschild("Verteidigerin", X1 - 40, BR, "gleich", WEISS, d=0.2),
    peep_voll("PI_froh", X2, BR, FR, "gleich", d=0.2, bis="wid"),
    peep_voll("PI_ruhig", X2, BR, FR, "wid", anim="cut"),
    namensschild("Herr Pieper", X2 + 30, BR, "gleich", GELB, d=0.3),
    ficon("tabler", "circle-check", MB, 380, 100, "gleich", fuell=GRUEN, bis="wid"),
    pl("unverwertbar", MB, 160, beim("gleich", "Das"), fill=GRUEN, size=28, anker="m", bis="streit"),
    pl("Streit offenlassen", MB, 160, "streit", fill=WEISS, size=28, anker="m", anim="cut", bis="wid"),
    ficon("tabler", "hand-stop", MB, 380, 100, "wid", fuell=WEISS, anim="cut", bis="verw"),
    pl("Widerspruch", MB, 160, "wid", fill=WEISS, size=28, anker="m", anim="cut", bis="verw"),
    ficon("tabler", "player-play", MB, 380, 100, "verw", fuell=BLAUHELL, anim="cut"),
    pl("Folge 132", MB, 160, "verw", fill=BLAUHELL, size=28, anker="m", anim="cut"),
]))

# L 3. Schritt: Fortwirkung – qualifizierte Belehrung ----------------------------------------------------------------------------
P3 = "3. Schritt: Fortwirkung"
folie([("fort", f"{P3} › Und das zweite Geständnis?"), ("heil", f"{P3} › erstes bleibt unverwertbar"),
       ("qual", f"{P3} › qualifizierte Belehrung"), ("grund", f"{P3} › Grund: Selbstbelastung „aus der Welt“?")], rechts_frei([
    *tafel("fort", "3. Schritt: Und das zweite Geständnis?"),
    z("Spätere Belehrung macht das erste nicht verwertbar.", 110, 175, "heil", "Bold", 32),
    fund("BGHSt 53, 112 Rn. 10", 150, 220, beim("heil", "verwertbar")),
    *wortlaut(110, 280, 1040, 200, "qual", [
        [("„… bei Beginn der nachfolgenden Vernehmung als", 0)],
        [("Beschuldigter auf die ", 0), ("Nichtverwertbarkeit der früheren", "n")],
        [("Angaben", "n2"), (" hinzuweisen („qualifizierte“ Belehrung).“", 0)],
    ], 30, {"n": beim("qual2", "unverwertbar"), "n2": beim("qual2", "unverwertbar")},
        "BGH, Urt. v. 18.12.2008 – 4 StR 455/08, BGHSt 53, 112 (Leitsatz 1, Auszug)"),
    z("Sonst verzichtet er womöglich nur deshalb auf das", 110, 560, "grund", size=30),
    z("Schweigerecht, weil er glaubt, die erste Selbstbelastung", 110, 602, beim("grund", "Schweigerecht"), size=30),
    z("nicht mehr aus der Welt schaffen zu können.", 110, 644, beim("grund", "Selbstbelastung"), size=30),
    fund("BGHSt 53, 112 Rn. 13; BGH, Urt. v. 3.5.2018 – 3 StR 390/17, Rn. 28", 150, 690, beim("grund", "Welt")),
    peep_voll("LO_ruhig", X1, BR, FR, "fort", bis="qual"),
    peep_voll("LO_ernst", X1, BR, FR, "qual", anim="cut"),
    namensschild("Polizeihauptmeister Lohmeyer", X1 - 70, BR, "fort", BLAU, d=0.2),
    peep_voll("PI_denkt", X2, BR, FR, "fort", d=0.2, bis="grund"),
    peep_voll("PI_muede", X2, BR, FR, "grund", anim="cut"),
    namensschild("Herr Pieper", X2 + 40, BR, "fort", GELB, d=0.3),
    ficon("tabler", "repeat", MB, 380, 100, "fort", fuell=WEISS, bis="qual"),
    pl("2. Geständnis", MB, 160, "fort", fill=WEISS, size=28, anker="m", bis="heil"),
    pl("1. bleibt unverwertbar", MB, 160, "heil", fill=ROTHELL, size=28, anker="m", anim="cut", bis="qual"),
    ficon("tabler", "info-circle", MB, 380, 100, "qual", fuell=BLAU, anim="cut", bis="grund"),
    pl("qualifizierte Belehrung", MB, 160, "qual", fill=BLAUHELL, size=28, anker="m", anim="cut", bis="grund"),
    ficon("tabler", "lock", MB, 380, 90, "grund", fuell=GELB, anim="cut"),
    pl("glaubt: kein Zurück", MB, 160, "grund", fill=GELB, size=28, anker="m", anim="cut"),
]))

# M 3. Schritt: fehlt der Hinweis – Abwägung -------------------------------------------------------------------------------------
folie([("folge", f"{P3} › nicht automatisch unverwertbar"), ("abwg", f"{P3} › Abwägung im Einzelfall"),
       ("k3", f"{P3} › Abwägung: glaubte er, nicht mehr abrücken zu können?"), ("wdh", f"{P3} › besonders bei Wiederholung")],
      rechts_frei([
    *tafel("folge", "3. Schritt: Hinweis fehlt – und nun?"),
    z("Die zweite Aussage ist nicht automatisch unverwertbar.", 110, 175, "folge", "Bold", 32),
    *wortlaut(110, 240, 1040, 200, "abwg", [
        [("„Unterbleibt die ‚qualifizierte‘ Belehrung, sind trotz", 0)],
        [("rechtzeitigen Widerspruchs die nach der Belehrung als", 0)],
        [("Beschuldigter gemachten Angaben nach Maßgabe einer", 0)],
        [("Abwägung im Einzelfall", "a"), (" verwertbar.“", 0)],
    ], 28, {"a": beim("abwg", "Abwägung")}, "BGHSt 53, 112 (Leitsatz 2)"),
    z("• Gewicht des Verstoßes", 130, 500, "k1", "Bold", 30),
    z("• Interesse an der Aufklärung", 130, 545, "k2", "Bold", 30),
    z("• vor allem: Glaubte er, von seinen früheren Angaben", 130, 590, "k3", "Bold", 30),
    z("nicht mehr abrücken zu können?", 160, 632, beim("k3", "nicht"), "Bold", 30),
    fund("BGHSt 53, 112 Rn. 14 f.; BGH 3 StR 390/17, Rn. 29", 160, 675, beim("k3", "können")),
    fb(110, 735, 1040, 100, GELB, "wdh", [("Besonders nahe, wenn er sie nur wiederholt", "ExtraBold", 32, INK)]),
    peep_voll("VE_ruhig", X1, BR, FR, "folge", bis="k3"),
    peep_voll("VE_denkt", X1, BR, FR, "k3", anim="cut"),
    namensschild("Verteidigerin", X1 - 40, BR, "folge", WEISS, d=0.2),
    peep_voll("PI_denkt", X2, BR, FR, "folge", d=0.2, bis="wdh"),
    peep_voll("PI_sorge", X2, BR, FR, "wdh", anim="cut"),
    namensschild("Herr Pieper", X2 + 30, BR, "folge", GELB, d=0.3),
    ficon("tabler", "help-circle", MB, 380, 100, "folge", fuell=WEISS, bis="abwg"),
    pl("nicht automatisch", MB, 160, "folge", fill=WEISS, size=28, anker="m", bis="abwg"),
    ficon("tabler", "scale", MB, 380, 110, "abwg", fuell=GELB, anim="cut", bis="wdh"),
    pl("Abwägung", MB, 160, "abwg", fill=GELB, size=28, anker="m", anim="cut", bis="k3"),
    pl("kein Zurück?", MB, 160, "k3", fill=BLAUHELL, size=28, anker="m", anim="cut", bis="wdh"),
    ficon("tabler", "repeat-once", MB, 380, 100, "wdh", fuell=GELB, anim="cut"),
    pl("nur wiederholt?", MB, 160, "wdh", fill=GELB, size=28, anker="m", anim="cut"),
]))

# N 3. Schritt: BGH-Fall und Fall Pieper ------------------------------------------------------------------------------------------
LK, RK = 110, 650
folie([("bgh", f"{P3} › der Fall des BGH"), ("bgh3", f"{P3} › BGH: kein Verwertungsverbot"),
       ("sub2", f"{P3} › Herr Pieper wiederholt nur"), ("sub4", f"{P3} › kein schweres Delikt"),
       ("sub5", f"{P3} › auch das zweite Geständnis unverwertbar")], rechts_frei([
    *tafel("bgh", "3. Schritt: BGH-Fall und Fall Pieper"),
    hart(linienzug([(625, 175), (625, 800)], "bgh", breite=4, farbe=INK)),
    z("Fall des BGH", LK, 175, "bgh", "ExtraBold", 32),
    fund("BGH, Urt. v. 18.12.2008 – 4 StR 455/08", LK, 220, "bgh", rechts=600),
    z("Nach der Belehrung", LK, 290, "bgh2", size=30, rechts=600),
    z("erstmals neue, sich selbst", LK, 332, beim("bgh2", "erstmals"), size=30, rechts=600),
    z("schwer belastende Angaben", LK, 374, beim("bgh2", "schwer"), size=30, rechts=600),
    fb(LK, 450, 490, 130, GRUENHELL, "bgh3", [("Abwägung: kein", "ExtraBold", 30, INK), ("Verwertungsverbot", "ExtraBold", 30, INK)]),
    fund("BGHSt 53, 112 Rn. 15", LK, 595, beim("bgh3", "Verwertungsverbot"), rechts=600),
    z("Herr Pieper", RK, 175, "sub2", "ExtraBold", 32),
    z("wiederholt nur, was er", RK, 290, "sub2", size=30),
    z("schon gesagt hat", RK, 332, "sub2", size=30),
    z("glaubte offenbar: kein Zurück", RK, 395, "sub3", size=30),
    z("Fahrraddiebstahl:", RK, 458, "sub4", size=30),
    z("kein schweres Delikt", RK, 500, beim("sub4", "kein"), size=30),
    fb(RK, 570, 500, 130, ROTHELL, "sub5", [("Auch das zweite Geständnis", "ExtraBold", 28, INK),
                                          ("ist unverwertbar.", "ExtraBold", 28, INK)]),
    peep_voll("VE_ruhig", X1, BR, FR, "bgh", bis="sub2"),
    peep_voll("VE_denkt", X1, BR, FR, "sub2", anim="cut", bis="sub5"),
    peep_voll("VE_froh", X1, BR, FR, "sub5", anim="cut"),
    namensschild("Verteidigerin", X1 - 40, BR, "bgh", WEISS, d=0.2),
    peep_voll("PI_ruhig", X2, BR, FR, "bgh", d=0.2, bis="sub2"),
    peep_voll("PI_muede", X2, BR, FR, "sub2", anim="cut", bis="sub5"),
    peep_voll("PI_froh", X2, BR, FR, "sub5", anim="cut"),
    namensschild("Herr Pieper", X2 + 30, BR, "bgh", GELB, d=0.3),
    ficon("tabler", "text-plus", MB, 380, 100, "bgh2", fuell=WEISS, bis="sub2"),
    pl("neue Angaben", MB, 160, "bgh2", fill=WEISS, size=28, anker="m", bis="bgh3"),
    pl("BGH: verwertbar", MB, 160, "bgh3", fill=GRUENHELL, size=28, anker="m", anim="cut", bis="sub2"),
    ficon("tabler", "repeat-once", MB, 380, 100, "sub2", fuell=GELB, anim="cut", bis="sub4"),
    pl("nur wiederholt", MB, 160, "sub2", fill=GELB, size=28, anker="m", anim="cut", bis="sub4"),
    ficon("tabler", "scale", MB, 380, 110, "sub4", fuell=BLAUHELL, anim="cut", bis="sub5"),
    pl("kein schweres Delikt", MB, 160, "sub4", fill=BLAUHELL, size=28, anker="m", anim="cut", bis="sub5"),
    ficon("tabler", "circle-x", MB, 380, 100, "sub5", fuell=ROT, anim="cut"),
    pl("unverwertbar", MB, 160, "sub5", fill=ROTHELL, size=28, anker="m", anim="cut"),
]))

# O Fernwirkung und Ergebnis ---------------------------------------------------------------------------------------------------
folie([("fern", "Fernwirkung › Beweise aus dem Geständnis"), ("fern2", "Fernwirkung › grundsätzlich abgelehnt"),
       ("erg", "Ergebnis › beide Geständnisse unverwertbar"), ("erg2", "Ergebnis › es bleiben Zeugin und Schloss")], rechts_frei([
    *tafel("fern", "Fernwirkung und Ergebnis"),
    z("Fernwirkung: Beweise, die die Polizei erst durch", 110, 175, "fern", "Bold", 32),
    z("ein unverwertbares Geständnis findet", 110, 222, beim("fern", "unverwertbares"), "Bold", 32),
    nein(150, 300, "fern2", gr=18),
    z("lehnt der BGH grundsätzlich ab", 185, 280, "fern2", size=30),
    fund("BGH, Beschl. v. 7.3.2006 – 1 StR 316/05, Rn. 22 f. (BGHSt 51, 1)", 185, 323, beim("fern2", "ab")),
    fb(110, 420, 1040, 100, GRUEN, "erg", [("Beide Geständnisse sind unverwertbar.", "ExtraBold", 36, INK)]),
    z("Es bleiben:", 110, 560, "erg2", "Bold", 32),
    ok(140, 625, beim("erg2", "Besitzerin"), gr=18),
    z("die Besitzerin als Zeugin", 175, 605, beim("erg2", "Besitzerin"), size=30),
    ok(140, 680, beim("erg2", "aufgebrochene"), gr=18),
    z("das aufgebrochene Schloss", 175, 660, beim("erg2", "aufgebrochene"), size=30),
    peep_voll("BE_ruhig", X1, BR, FR, "fern", bis="erg2"),
    peep_voll("BE_ernst", X1, BR, FR, "erg2", anim="cut"),
    namensschild("Besitzerin", X1 - 40, BR, "fern", LILA, d=0.2),
    peep_voll("PI_denkt", X2, BR, FR, "fern", d=0.2, bis="erg"),
    peep_voll("PI_froh", X2, BR, FR, "erg", anim="cut", bis="erg2"),
    peep_voll("PI_sorge", X2, BR, FR, "erg2", anim="cut"),
    namensschild("Herr Pieper", X2 + 30, BR, "fern", GELB, d=0.3),
    ficon("tabler", "route", MB, 380, 100, "fern", fuell=WEISS, bis="erg"),
    pl("Fernwirkung?", MB, 160, "fern", fill=WEISS, size=28, anker="m", bis="fern2"),
    pl("grundsätzlich nein", MB, 160, "fern2", fill=ROTHELL, size=28, anker="m", anim="cut", bis="erg"),
    ficon("tabler", "circle-check", MB, 380, 100, "erg", fuell=GRUEN, anim="cut", bis="erg2"),
    pl("beide unverwertbar", MB, 160, "erg", fill=GRUEN, size=28, anker="m", anim="cut", bis="erg2"),
    ficon("tabler", "lock-open", MB, 380, 90, "erg2", fuell=ROT, anim="cut"),
    pl("Zeugin + Schloss", MB, 160, "erg2", fill=WEISS, size=28, anker="m", anim="cut"),
]))

# P Klausurtipp mit Prüfungsaufbau (Lexi) ------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · Prüfungsaufbau"), ("t1", "Klausurtipp · I. Beweiserhebungsverbot"),
       ("t2", "Klausurtipp · II. Verwertungsverbot nach Abwägung"), ("t3", "Klausurtipp · III. rechtzeitiger Widerspruch"),
       ("t4", "Klausurtipp · IV. Fortwirkung auf spätere Aussagen")], [
    *tafel("tipp", "Klausurtipp: Prüfungsaufbau", h=860, fill=HELL),
    warnung_i(150, 205, "tipp", gr=26),
    z("Verwertungsverbot in vier Schritten", 200, 180, beim("tipp", "Prüf"), "Bold", 36),
    z("I. Beweiserhebungsverbot", 130, 270, "t1", "ExtraBold", 34),
    z("Beschuldigter? Belehrung fehlte?", 190, 316, beim("t1", "War"), size=30),
    z("II. Verwertungsverbot nach Abwägung", 130, 390, "t2", "ExtraBold", 34),
    z("Streit der Lehren nur entscheiden,", 190, 436, "t2b", size=30),
    z("wenn sie zu verschiedenen Ergebnissen kommen", 190, 476, beim("t2b", "wenn"), size=30),
    z("III. Rechtzeitiger Widerspruch", 130, 550, "t3", "ExtraBold", 34),
    z("IV. Fortwirkung auf spätere Aussagen", 130, 625, "t4", "ExtraBold", 34),
    z("qualifizierte Belehrung? erneute Abwägung", 190, 671, beim("t4", "qualifizierte"), size=30),
    *redet("LX_warnt", LXX, BR, FR + 60, "tipp", "merke"),
    namensschild("Lexi", LXX, BR, "tipp", GELB, d=0.2),
])

# Q Merksatz (Lexi) ------------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Eine spätere Belehrung ", 0), ("heilt", "a")], [("den ersten Fehler ", 0), ("nicht", "a2"), (".", 0)]],
                750, 310, 52, "merke", {"a": beim("merke", "heilt"), "a2": beim("merke", "heilt")}),
    *markertext([[("Fehlt die qualifizierte Belehrung,", 0)], [("entscheidet die ", 0), ("Abwägung", "b")],
                 [("über das zweite Geständnis.", 0)]], 750, 520, 48, "mz", {"b": beim("mz", "Abwägung")}),
    *redet("LX_erklaert", 1680, 960, 690, "merke", lexi_bis_ende("merke")),
    namensschild("Lexi", 1680, 960, "merke", GELB, d=0.2),
])
