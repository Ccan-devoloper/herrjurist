"""Folge 039 · Anklageklausur Aufbau: Gutachten, Prozessuales, Abschlussverfügung – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A Im Elektronikmarkt (Diebstahl, Detektiv), B Vor dem Markt (Beleidigung), C Bei der
Staatsanwaltschaft (Akte, Frage), D Sachverhalt, E Aufbau und Länderunterschiede, F Maßstab § 170 I StPO (Wortlautkarte,
BGH StB 58/25 Rn. 5), G1–G3 A. Materiell-rechtliches Gutachten (Diebstahl, Beweiswürdigung, Beleidigung), H1–H3
B. Prozessuales Gutachten (Strafantrag/Frist, Zuständigkeit, prozessuale Tat § 264 StPO mit BGH GSSt 1/23 Rn. 25),
I C. Abschlussverfügung (Wortlautkarte § 170 II 1 StPO, §§ 153, 154, 169a), J Anklageschrift (Wortlautkarte § 200 I StPO),
K Klausurtipp (Lexi), L Klausurschema, M Merksatz (Lexi).
Geräusche nur bei sichtbarer Handlung: Münzen auf der Ladentheke (Szene A), Akte fällt auf den Schreibtisch (Szene C)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont

bausteine.FIGORDNER = "op_039/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
LILAHELL = (246, 243, 255, 255)
ROTHELL = (253, 232, 228, 255)
GRAU = (205, 205, 210, 255)
HOLZ = (214, 160, 110, 255)
DUNKEL = (58, 58, 72, 255)
DAUER = bausteine._cj()["dauer"]
NULL = ("fall", -round(bausteine._t("fall") + 0.4, 3))   # 0,4 s vor Hauptfilmbeginn: ab 0,0 s voll sichtbar

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


def tafel(cue, titel_, h=840, fill=WEISS, size=50):
    """Rechtstafel links, rechts bleibt Platz für die Figuren."""
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(glyphen(titel_), 110, 100, cue, size)]


def wortlaut(x, y, w, h, cue, zeilen, size, hl, quelle, quelle_cue=None):
    """Wortlautkarte: wörtliches Zitat (gesetze-im-internet.de bzw. BGH-Volltext) in einer hellen Karte, Fundstelle
    darunter rechts. zeilen = Liste von Token-Listen [(text, Schlüssel|0)], hl = {Schlüssel: Cue} (Hervorhebung synchron
    zum gesprochenen Wort)."""
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
        if n.startswith(("bild:", "ficon:")):
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def namensschild(text, cx, unten, cue, fill, **k):
    return pille(glyphen(text), cx, unten + 22, cue, fill=fill, size=30, anker="m", **k)


def bis_(e, cue):
    e.bis = cue
    return e


# --- Eigene Hilfsfunktion (wie Folge 012/018/024): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ---------
# ElevenLabs legt das Ende eines Wortes vor Satzzeichen oft in die folgende Pause; redet() kürzt jedes Wortende auf
# das letzte 10-ms-Fenster über −38 dBFS (aus ../stimme.wav) und verteilt die Viseme nur auf diese Spanne.
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



def hart(e):
    e.anim = "cut"
    return e


BODEN, FH = 880, 480
BR, FR = 930, 480                       # Figuren rechts neben der Tafel
X1, X2 = 1420, 1720                     # zwei Figuren neben der Tafel
MB = (X1 + X2) // 2
XS = 1600                               # eine Figur allein neben der Tafel

# A Fall: im Elektronikmarkt -------------------------------------------------------------------------------------------------
RX1, RX2, BX = 640, 1300, 1700          # Rösch am Regal, Rösch an der Kasse, Brehm
ROa = ("RO_redet_r", RX2, BODEN, FH)
BRa = ("BR_redet", BX, BODEN, FH)
r_reg = beim("regal", "Herr")
kh_weg = bewegt(ficon("tabler", "headphones", RX1 - 25, 660, 60, beim("tasche", "Kopfhörer"), fuell=BLAU, bis="leer"),
                beim("tasche", "Kopfhörer"), beim("tasche", "Jackentasche", ende=True), -275, -165)
muenzen = szene(bewegt(ficon("tabler", "coins", 1060, 640, 70, beim("kasse", "bezahlt"), fuell=GELB),
                       beim("kasse", "bezahlt"), beim("kasse", "nur"), 170, -40), "039muenzen*", 1.0, versatz=0.30)
folie([(NULL, "Fall · Im Elektronikmarkt"), (beim("detektiv", "Herr"), "Fall · Der Ladendetektiv")], [
    linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK),
    pl("Im Elektronikmarkt", 70, 40, NULL, fill=GELB, size=40),
    # Regal mit Kopfhörern
    karte(130, 330, 300, 548, NULL, fill=WEISS, rund=10, schatten=6),
    linienzug([(135, 500), (425, 500)], NULL, breite=6, farbe=INK),
    linienzug([(135, 680), (425, 680)], NULL, breite=6, farbe=INK),
    ficon("tabler", "headphones", 210, 495, 80, NULL, fuell=BLAU),
    ficon("tabler", "headphones", 340, 495, 80, NULL, fuell=GELB, bis="leer"),
    ficon("tabler", "package", 340, 495, 75, beim("leer", "leere"), fuell=WEISS, anim="cut"),
    ficon("tabler", "headphones", 210, 675, 80, NULL, fuell=LILA),
    ficon("tabler", "headphones", 340, 675, 80, NULL, fuell=GRUEN),
    ficon("tabler", "device-cctv", 560, 230, 110, NULL, fuell=WEISS),
    # Kasse
    fl_block(780, 640, 380, 240, HOLZ, NULL, [("", "Bold", 30, INK)], rund=10),
    ficon("tabler", "cash-register", 880, 642, 150, NULL, fuell=WEISS),
    pl("Anfang März", 960, 140, beim("fall", "Anfang"), fill=WEISS, size=30, anker="m", bis="regal"),
    # Herr Rösch am Regal
    peep_voll("RO_ruhig", RX1, BODEN, FH, r_reg, bis="tasche"),
    peep_voll("RO_cool", RX1, BODEN, FH, "tasche", anim="cut", bis="kasse"),
    namensschild("Herr Rösch", RX1, BODEN, r_reg, BLAU, bis="kasse"),
    ring(340, 455, 75, 60, beim("regal", "Packung"), bis=beim("tasche", "Kopfhörer")),
    pl("Kopfhörer: 249 €", 280, 250, beim("regal", "zweihundert"), fill=GELB, size=30, anker="m", bis="kasse"),
    kh_weg,
    pl("in die Jackentasche", RX1, 330, beim("tasche", "Jackentasche"), fill=WEISS, size=28, anker="m", bis="leer"),
    pl("leere Packung zurück", RX1, 330, beim("leer", "leere"), fill=WEISS, size=28, anker="m", anim="cut", bis="kasse"),
    # an der Kasse
    peep_voll("RO_ruhig", RX2, BODEN, FH, "kasse", anim="cut", bis=beim("detektiv", "Herr")),
    peep_voll("RO_ruhig_r", RX2, BODEN, FH, beim("detektiv", "Herr"), anim="cut", bis="b1"),
    peep_voll("RO_denkt_r", RX2, BODEN, FH, "b1", anim="cut", bis="fund"),
    peep_voll("RO_schreck_r", RX2, BODEN, FH, "fund", anim="cut", bis="r1"),
    *redet("RO_redet_r", RX2, BODEN, FH, "r1", "drei"),
    namensschild("Herr Rösch", RX2, BODEN, "kasse", BLAU, anim="cut"),
    ficon("tabler", "bottle", 1000, 642, 46, beim("kasse", "Cola"), fuell=ROT),
    muenzen,
    pl("nur die Cola bezahlt", 970, 420, beim("kasse", "nur"), fill=WEISS, size=28, anker="m", bis="b1"),
    # Ladendetektiv Brehm
    peep_voll("BR_ruhig", BX, BODEN, FH, beim("detektiv", "Herr"), anim="cut", bis="b1"),
    *redet("BR_redet", BX, BODEN, FH, "b1", "fund"),
    peep_voll("BR_ruhig", BX, BODEN, FH, "fund", anim="cut", bis="r1"),
    peep_voll("BR_denkt", BX, BODEN, FH, "r1", anim="cut"),
    namensschild("Herr Brehm", BX, BODEN, beim("detektiv", "Herr"), GRUEN, anim="cut"),
    pl("Ladendetektiv", BX, 330, beim("detektiv", "Herr"), fill=GRUEN, size=28, anker="m", anim="cut", bis="b1"),
    blase("sprech", 600, 190, "b1", 1500, 200, inhalt=["Bitte zeigen Sie mir", "Ihre Jackentasche."], textsize=34,
          figur=BRa, bis="fund"),
    ficon("tabler", "headphones", RX2 + 10, 640, 70, "fund", fuell=GELB),
    pl("Kopfhörer in der Tasche", RX2, 330, "fund", fill=GELB, size=28, anker="m", bis="r1"),
    blase("sprech", 640, 210, "r1", 970, 230, inhalt=["Die wollte ich doch bezahlen!", "Das hab ich vergessen."],
          textsize=32, figur=ROa, bis="drei"),
])

# B Fall: vor dem Markt, drei Tage später ---------------------------------------------------------------------------------
RXb, BXb = 980, 1500
ROb = ("RO_wut_r", RXb, BODEN, FH)
folie([("drei", "Fall · Drei Tage später"), ("polizei", "Fall · Kein Strafantrag")], [
    linienzug([(60, BODEN), (1860, BODEN)], "drei", breite=7, farbe=INK),
    pl("Vor dem Markt", 70, 40, "drei", fill=GELB, size=40),
    ficon("tabler", "building-store", 360, BODEN - 2, 440, "drei", fuell=GELB),
    ficon("tabler", "calendar-event", 760, 330, 90, beim("drei", "Drei"), fuell=WEISS),
    pl("drei Tage später", 760, 150, beim("drei", "Drei"), fill=WEISS, size=30, anker="m"),
    peep_voll("RO_cool_r", RXb, BODEN, FH, beim("drei", "Rösch"), bis="r2"),
    *redet("RO_wut_r", RXb, BODEN, FH, "r2", "polizei"),
    peep_voll("RO_cool_r", RXb, BODEN, FH, "polizei", anim="cut"),
    namensschild("Herr Rösch", RXb, BODEN, beim("drei", "Rösch"), BLAU),
    peep_voll("BR_ruhig", BXb, BODEN, FH, beim("drei", "Detektiv"), bis=beim("r2", "Idiot")),
    peep_voll("BR_aerger", BXb, BODEN, FH, beim("r2", "Idiot"), anim="cut", bis="kein"),
    peep_voll("BR_muede", BXb, BODEN, FH, "kein", anim="cut"),
    namensschild("Herr Brehm", BXb, BODEN, beim("drei", "Detektiv"), GRUEN),
    blase("sprech", 560, 200, "r2", 1260, 220, inhalt=["Da ist ja der Detektiv.", "Du Idiot!"], textsize=36,
          figur=ROb, bis="polizei"),
    ficon("tabler", "file-text", 1750, 700, 110, "polizei", fuell=WEISS),
    pl("schildert es der Polizei", 1550, 200, "polizei", fill=WEISS, size=30, anker="m"),
    pl("kein Strafantrag", 1550, 290, beim("kein", "Strafantrag"), fill=ROT, size=30, anker="m"),
    nein(1760, 310, beim("kein", "nicht")),
])

# C Fall: bei der Staatsanwaltschaft ----------------------------------------------------------------------------------------
SAX = 1180
SAc = ("SA_redet", SAX, BODEN, FH)
akte = szene(bewegt(ficon("tabler", "folders", 560, 531, 190, "akte", fuell=GELB), "akte", ("akte", 0.35), 0, -260),
             "039akte*", 1.0, versatz=0.30)
folie([("akte", "Fall · Bei der Staatsanwaltschaft"), ("frage", "Fall · Die Frage")], [
    linienzug([(60, BODEN), (1860, BODEN)], "akte", breite=7, farbe=INK),
    pl("Bei der Staatsanwaltschaft", 70, 40, "akte", fill=GELB, size=40),
    ficon("tabler", "desk", 560, BODEN - 2, 560, "akte", fuell=HOLZ),
    akte,
    pl("August: die Ermittlungsakte", 560, 170, beim("akte", "August"), fill=WEISS, size=30, anker="m"),
    peep_voll("SA_ruhig", SAX, BODEN, FH, "akte", bis="sa1"),
    *redet("SA_redet", SAX, BODEN, FH, "sa1", "frage"),
    peep_voll("SA_denkt", SAX, BODEN, FH, "frage", anim="cut"),
    namensschild("Staatsanwältin", SAX, BODEN, "akte", LILA),
    blase("sprech", 600, 190, "sa1", 1560, 230, inhalt=["Ein Diebstahl, eine Beleidigung.", "Was verfüge ich?"],
          textsize=32, figur=SAc, bis="frage"),
    pl("Tat: Diebstahl", 360, 270, beim("sa1", "Diebstahl"), fill=GELB, size=28, anker="m"),
    pl("Tat: Beleidigung", 770, 270, beim("sa1", "Beleidigung"), fill=ROTHELL, size=28, anker="m"),
    pl("Wie baust du die Anklageklausur auf?", 1460, 160, "frage", fill=WEISS, size=32, anker="m"),
    pl("Vom Gutachten bis zur Abschlussverfügung", 1460, 250, "frage2", fill=PINK, size=32, anker="m"),
])

# D Sachverhalt -------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    glyphen("Herr Rösch (24, nicht vorbestraft) öffnet am 2. März 2026 in einem Elektronikmarkt eine Packung Kopfhörer "
            "für 249 Euro, steckt die Kopfhörer ein und legt die leere Packung zurück. An der Kasse bezahlt er nur eine "
            "Cola. Ladendetektiv Brehm findet die Kopfhörer; ein Video zeigt den Ablauf. Als Beschuldigter vernommen, sagt "
            "Herr Rösch, er habe das Bezahlen vergessen."),
    glyphen("Am 5. März 2026 ruft er Herrn Brehm vor dem Markt „Du Idiot!“ zu. Herr Brehm schildert das am selben Tag "
            "der Polizei, stellt aber keinen Strafantrag."),
    glyphen("Im August 2026 liegt die Akte der Staatsanwältin vor. Herr Rösch hat keinen Verteidiger. Bearbeitervermerk: "
            "Gutachten und Abschlussverfügung entwerfen, keinen Strafbefehl."),
], "Was verfügt die Staatsanwältin?")

# E Aufbau der Anklageklausur -------------------------------------------------------------------------------------------------
folie([("aufbau", "Aufbau · drei Teile"), ("land", "Aufbau › von Land zu Land verschieden"),
       ("vermerk", "Aufbau › Bearbeitervermerk")], rechts_frei([
    *tafel("aufbau", "Aufbau der Anklageklausur"),
    z("A. Materiell-rechtliches Gutachten", 110, 190, "teilA", "Bold", 38),
    z("B. Prozessuales Gutachten", 110, 255, "teilB", "Bold", 38),
    z("C. Praktischer Teil: Abschlussverfügung", 110, 320, "teilC", "Bold", 38),
    fl_block(110, 410, 1040, 130, LILAHELL, "land", [("Ausbildungs- und Prüfungskonvention:", "ExtraBold", 34, INK),
                                                    ("von Land zu Land verschieden", "Bold", 32, INK)]),
    z("z. B. Strafantrag: im materiellen oder im prozessualen Teil?", 110, 590, "strafa", size=32, farbe=TEXT),
    z("Maßgeblich: Bearbeitervermerk und", 110, 670, "vermerk", "Bold", 36),
    z("Hinweise deines Prüfungsamts", 150, 722, beim("vermerk", "Hinweise"), "Bold", 36),
    peep_voll("SA_ruhig", XS, BR, FR, "aufbau", bis="land"),
    peep_voll("SA_denkt", XS, BR, FR, "land", anim="cut", bis="vermerk"),
    peep_voll("SA_froh", XS, BR, FR, "vermerk", anim="cut"),
    namensschild("Staatsanwältin", XS, BR, "aufbau", LILA, d=0.2),
    ficon("tabler", "folders", XS, 380, 120, "aufbau", fuell=GELB, bis="land"),
    pl("A · B · C", XS, 160, "teilC", fill=WEISS, size=30, anker="m", bis="land"),
    ficon("tabler", "map-pin", XS, 380, 90, "land", fuell=ROT, anim="cut", bis="vermerk"),
    pl("von Land zu Land", XS, 160, "land", fill=LILA, size=30, anker="m", anim="cut", bis="vermerk"),
    ficon("tabler", "file-description", XS, 380, 100, "vermerk", fuell=WEISS, anim="cut"),
    pl("Bearbeitervermerk", XS, 160, "vermerk", fill=GELB, size=30, anker="m", anim="cut"),
]))

# F Maßstab: § 170 I StPO, hinreichender Tatverdacht -----------------------------------------------------------------------
folie([("p170", "Maßstab › § 170 Abs. 1 StPO"), ("hinr", "Maßstab › hinreichender Tatverdacht"),
       ("wahr", "Maßstab › Verurteilung wahrscheinlich")], rechts_frei([
    *tafel("p170", "Der Maßstab: § 170 Abs. 1 StPO"),
    *wortlaut(110, 180, 1040, 150, "p170", [
        [("„Bieten die Ermittlungen ", 0), ("genügenden Anlaß", "a"), (" zur Erhebung der", 0)],
        [("öffentlichen Klage, so erhebt die Staatsanwaltschaft sie durch", 0)],
        [("Einreichung einer ", 0), ("Anklageschrift", "b"), (" bei dem zuständigen Gericht.“", 0)],
    ], 30, {"a": beim("p170", "genügenden"), "b": beim("p170", "Anklageschrift")}, "§ 170 Abs. 1 StPO"),
    z("genügender Anlass = hinreichender Tatverdacht", 110, 400, "hinr", "Bold", 36),
    z("BVerfG, Beschl. v. 21.12.2022 – 2 BvR 378/20, Rn. 62, 78", 150, 450, beim("hinr", "hinreichender"), size=26, farbe=TEXT),
    *wortlaut(110, 520, 1040, 190, "wahr", [
        [("„Ein hinreichender Tatverdacht ist zu bejahen, wenn bei", 0)],
        [("vorläufiger Tatbewertung", "a"), (" auf Grundlage des Ermittlungsergebnisses", 0)],
        [("die Verurteilung in einer Hauptverhandlung mit vollgültigen", 0)],
        [("Beweismitteln ", 0), ("wahrscheinlich", "b"), (" ist …“", 0)],
    ], 30, {"a": beim("wahr", "vorläufiger"), "b": beim("wahr", "wahrscheinlich")},
        "BGH, Beschl. v. 10.12.2025 – StB 58/25, Rn. 5"),
    peep_voll("RO_ruhig", X1, BR, FR, "p170", bis="wahr"),
    peep_voll("RO_denkt", X1, BR, FR, "wahr", anim="cut"),
    peep_voll("SA_denkt", X2, BR, FR, "p170", d=0.2, bis="hinr"),
    peep_voll("SA_ruhig", X2, BR, FR, "hinr", anim="cut"),
    namensschild("Herr Rösch", X1, BR, "p170", BLAU, d=0.2),
    namensschild("Staatsanwältin", X2, BR, "p170", LILA, d=0.3),
    ficon("tabler", "file-text", MB, 380, 100, beim("p170", "Anklageschrift"), fuell=WEISS, bis="hinr"),
    pl("Anklage?", MB, 160, beim("p170", "Anklageschrift"), fill=WEISS, size=30, anker="m", bis="hinr"),
    ficon("tabler", "scale", MB, 380, 110, "hinr", fuell=GELB, anim="cut"),
    pl("hinreichender Tatverdacht", MB, 160, "hinr", fill=GELB, size=28, anker="m", anim="cut"),
]))

# G1 A. Materiell-rechtliches Gutachten: Tat 1, Diebstahl ------------------------------------------------------------------
PA = "A. Materiell-rechtliches Gutachten"
folie([("mat", PA), ("dieb", f"{PA} › Tat 1: Diebstahl, § 242 Abs. 1 StGB"),
       ("einl", f"{PA} › Tat 1: Einlassung")], rechts_frei([
    *tafel("mat", "A. Materiell-rechtliches Gutachten", size=46),
    fl_block(110, 180, 500, 110, BLAU, "mat1", [("Strafbar?", "ExtraBold", 38, INK)]),
    fl_block(650, 180, 500, 110, GRUEN, "mat2", [("Nachweisbar?", "ExtraBold", 38, INK)]),
    z("Tat 1: Diebstahl, § 242 Abs. 1 StGB", 110, 350, "dieb", "Bold", 38),
    z("Wegnahme: eingesteckt, nicht bezahlt", 150, 420, "weg", size=34),
    ok(1110, 440, beim("weg", "Weck"), gr=22),
    z("Einlassung: „Bezahlen vergessen“", 150, 500, "einl", size=34),
    z("dann: kein Vorsatz, keine Zueignungsabsicht", 150, 560, beim("einl", "Dann"), size=34, farbe=TEXT),
    peep_voll("RO_ruhig", X1, BR, FR, "mat", bis="einl"),
    peep_voll("RO_cool", X1, BR, FR, "einl", anim="cut"),
    peep_voll("BR_ruhig", X2, BR, FR, "mat", d=0.2, bis="einl"),
    peep_voll("BR_denkt", X2, BR, FR, "einl", anim="cut"),
    namensschild("Herr Rösch", X1, BR, "mat", BLAU, d=0.2),
    namensschild("Herr Brehm", X2, BR, "mat", GRUEN, d=0.3),
    ficon("tabler", "headphones", MB, 380, 100, "dieb", fuell=GELB),
    pl("Diebstahl?", MB, 160, "dieb", fill=WEISS, size=30, anker="m", bis="weg"),
    pl("Kopfhörer eingesteckt", MB, 160, "weg", fill=GELB, size=28, anker="m", anim="cut", bis="einl"),
    pl("„vergessen“?", MB, 160, "einl", fill=PINK, size=28, anker="m", anim="cut"),
]))

# G2 A. Beweiswürdigung aus der Akte ----------------------------------------------------------------------------------------
folie([("bw", f"{PA} › Tat 1: Beweiswürdigung"), ("bw3", f"{PA} › Tat 1: hinreichender Tatverdacht")], rechts_frei([
    *tafel("bw", "Tat 1: Beweiswürdigung aus der Akte", size=46),
    z("Video: Packung geöffnet, leer zurückgelegt", 110, 190, "bw1", "Bold", 36),
    z("spricht gegen ein Versehen", 110, 280, "bw2", "Bold", 36),
    z("zumal: Cola bezahlt", 150, 335, beim("bw2", "Cola"), size=34, farbe=TEXT),
    z("Einlassung überzeugt nicht", 110, 430, "bw3", "Bold", 36),
    nein(1110, 450, "bw3", gr=20),
    z("Verurteilung wahrscheinlich", 110, 500, beim("bw3", "Verurteilung"), "Bold", 36),
    ok(1110, 520, beim("bw3", "wahrscheinlich"), gr=22),
    fl_block(110, 610, 1040, 120, GRUEN, beim("bw3", "hinreichender"), [("hinreichender Tatverdacht", "ExtraBold", 38, INK)]),
    peep_voll("RO_cool", X1, BR, FR, "bw", bis="bw3"),
    peep_voll("RO_schreck", X1, BR, FR, "bw3", anim="cut"),
    peep_voll("BR_ruhig", X2, BR, FR, "bw", d=0.2, bis="bw2"),
    peep_voll("BR_denkt", X2, BR, FR, "bw2", anim="cut"),
    namensschild("Herr Rösch", X1, BR, "bw", BLAU, d=0.2),
    namensschild("Herr Brehm", X2, BR, "bw", GRUEN, d=0.3),
    ficon("tabler", "device-cctv", MB, 380, 110, "bw1", fuell=WEISS, bis=beim("bw2", "Cola")),
    pl("Video", MB, 160, "bw1", fill=WEISS, size=30, anker="m", bis=beim("bw2", "Cola")),
    ficon("tabler", "bottle", MB, 380, 60, beim("bw2", "Cola"), fuell=ROT, anim="cut", bis=beim("bw3", "Verurteilung")),
    pl("nur die Cola bezahlt", MB, 160, beim("bw2", "Cola"), fill=WEISS, size=28, anker="m", anim="cut", bis=beim("bw3", "Verurteilung")),
    ficon("tabler", "scale", MB, 380, 110, beim("bw3", "Verurteilung"), fuell=GELB, anim="cut"),
    pl("Verurteilung wahrscheinlich", MB, 160, beim("bw3", "Verurteilung"), fill=GRUEN, size=26, anker="m", anim="cut"),
]))

# G3 A. Tat 2, Beleidigung --------------------------------------------------------------------------------------------------
folie([("bel", f"{PA} › Tat 2: Beleidigung, § 185 StGB"), ("offen", f"{PA} › Tat 2: kann offenbleiben")], rechts_frei([
    *tafel("bel", "Tat 2: Beleidigung, § 185 StGB", size=46),
    z("Das Schimpfwort: strafbar?", 110, 190, beim("offen", "Schimpfwort"), "Bold", 36),
    z("kann offenbleiben", 150, 250, beim("offen", "offenbleiben"), "Bold", 36),
    z("Zeuge: Herr Brehm", 150, 320, beim("offen", "Brehm"), size=34, farbe=TEXT),
    fl_block(110, 440, 1040, 120, ROTHELL, "scheit", [("Das Verfahren scheitert an etwas anderem.", "ExtraBold", 36, INK)]),
    peep_voll("RO_cool", X1, BR, FR, "bel", bis="scheit"),
    peep_voll("RO_denkt", X1, BR, FR, "scheit", anim="cut"),
    peep_voll("BR_aerger", X2, BR, FR, "bel", d=0.2, bis="scheit"),
    peep_voll("BR_denkt", X2, BR, FR, "scheit", anim="cut"),
    namensschild("Herr Rösch", X1, BR, "bel", BLAU, d=0.2),
    namensschild("Herr Brehm", X2, BR, "bel", GRUEN, d=0.3),
    ficon("tabler", "calendar-event", MB, 380, 100, "bel", fuell=WEISS),
    pl("§ 185 StGB", MB, 160, "bel", fill=ROTHELL, size=30, anker="m", bis="scheit"),
    pl("etwas anderes", MB, 160, "scheit", fill=PINK, size=30, anker="m", anim="cut"),
]))

# H1 B. Prozessuales Gutachten: Strafantrag -------------------------------------------------------------------------------
PB = "B. Prozessuales Gutachten"
folie([("proz", PB), ("pv", f"{PB} › Prozessvoraussetzungen"), ("p194", f"{PB} › Tat 2: Strafantrag, § 194 Abs. 1 StGB"),
       ("frist", f"{PB} › Tat 2: Antragsfrist, § 77b StGB"), ("hind", f"{PB} › Tat 2: Verfahrenshindernis"),
       ("diebst", f"{PB} › Tat 1: kein Strafantrag nötig")], rechts_frei([
    *tafel("proz", "B. Prozessuales Gutachten"),
    z("Prozessvoraussetzungen", 110, 180, "pv", "Bold", 38),
    *wortlaut(110, 240, 1040, 70, "p194", [[("„Die Beleidigung wird ", 0), ("nur auf Antrag", "a"), (" verfolgt.“", 0)]], 30,
              {"a": beim("p194", "Antrag")}, "§ 194 Abs. 1 S. 1 StGB"),
    z("Frist: drei Monate ab Kenntnis von Tat und Täter", 110, 380, "frist", "Bold", 34),
    z("§ 77b Abs. 1 S. 1, Abs. 2 S. 1 StGB", 150, 428, beim("frist", "Paragraf"), size=28, farbe=TEXT),
    z("kein Antrag gestellt", 110, 490, "juni", size=32),
    z("· Frist im Juni abgelaufen", 400, 490, beim("juni", "Frist"), size=32),
    nein(1120, 510, beim("juni", "keinen"), gr=18),
    fl_block(110, 570, 1040, 120, ROTHELL, "hind", [("Verfahrenshindernis:", "ExtraBold", 36, INK),
                                                   ("keine Verurteilung möglich", "Bold", 32, INK)]),
    z("Tat 1, Diebstahl: kein Strafantrag nötig", 110, 735, "diebst", "Bold", 34),
    z("249 €: nicht geringwertig (§ 248a StGB)", 150, 785, beim("diebst", "Kopfhörer"), size=30, farbe=TEXT),
    ok(1110, 755, beim("diebst", "geringwertig"), gr=22),
    peep_voll("BR_ruhig", X1, BR, FR, "proz", bis="juni"),
    peep_voll("BR_muede", X1, BR, FR, "juni", anim="cut"),
    peep_voll("SA_ruhig", X2, BR, FR, "proz", d=0.2, bis="hind"),
    peep_voll("SA_skeptisch", X2, BR, FR, "hind", anim="cut", bis="diebst"),
    peep_voll("SA_froh", X2, BR, FR, "diebst", anim="cut"),
    namensschild("Herr Brehm", X1, BR, "proz", GRUEN, d=0.2),
    namensschild("Staatsanwältin", X2, BR, "proz", LILA, d=0.3),
    ficon("tabler", "signature", MB, 380, 100, "p194", fuell=WEISS, bis="frist"),
    pl("Strafantrag?", MB, 160, "p194", fill=WEISS, size=30, anker="m", bis="frist"),
    ficon("tabler", "hourglass-empty", MB, 380, 90, "frist", fuell=GELB, anim="cut", bis=beim("juni", "Frist")),
    pl("drei Monate", MB, 160, "frist", fill=GELB, size=30, anker="m", anim="cut", bis=beim("juni", "Frist")),
    ficon("tabler", "calendar-x", MB, 380, 100, beim("juni", "Frist"), fuell=ROT, anim="cut", bis="diebst"),
    pl("Frist abgelaufen", MB, 160, beim("juni", "Frist"), fill=ROT, size=28, anker="m", anim="cut", bis="diebst"),
    ficon("tabler", "headphones", MB, 380, 100, "diebst", fuell=GELB, anim="cut"),
    pl("kein Strafantrag nötig", MB, 160, "diebst", fill=GRUEN, size=28, anker="m", anim="cut"),
]))

# H2 B. Zuständigkeit ---------------------------------------------------------------------------------------------------------
folie([("zust", f"{PB} › Zuständigkeit"), ("oertl", f"{PB} › örtlich: § 7 Abs. 1 StPO"),
       ("sachl", f"{PB} › sachlich: § 24 Abs. 1 GVG"), ("strafr", f"{PB} › Vergehen, Straferwartung bis zwei Jahre"), (beim("strafr", "Strafrichter"), f"{PB} › Strafrichter, § 25 Nr. 2 GVG")], rechts_frei([
    *tafel("zust", "B. Prozessuales Gutachten: Zuständigkeit", size=44),
    z("örtlich: nach dem Tatort", 110, 200, beim("oertl", "örtlich"), "Bold", 38),
    z("§ 7 Abs. 1 StPO", 150, 255, beim("oertl", "Paragraf"), size=32, farbe=TEXT),
    z("sachlich: Amtsgericht", 110, 350, "sachl", "Bold", 38),
    z("§ 24 Abs. 1 GVG", 150, 405, beim("sachl", "Paragraf"), size=32, farbe=TEXT),
    z("Vergehen, Straferwartung bis zwei Jahre:", 110, 500, "strafr", "Bold", 38),
    z("Strafrichter, § 25 Nr. 2 GVG", 150, 560, beim("strafr", "Strafrichter"), "Bold", 38),
    fl_block(110, 660, 1040, 110, GRUEN, beim("strafr", "Strafrichter"),
             [("Strafrichter am Amtsgericht", "ExtraBold", 36, INK)]),
    peep_voll("SA_ruhig", XS, BR, FR, "zust", bis="strafr"),
    peep_voll("SA_froh", XS, BR, FR, beim("strafr", "Strafrichter"), anim="cut"),
    peep_voll("SA_denkt", XS, BR, FR, "strafr", anim="cut", bis=beim("strafr", "Strafrichter")),
    namensschild("Staatsanwältin", XS, BR, "zust", LILA, d=0.2),
    ficon("tabler", "map-pin", XS, 380, 90, beim("oertl", "Tatort"), fuell=ROT, bis="sachl"),
    pl("Tatort", XS, 160, beim("oertl", "Tatort"), fill=WEISS, size=30, anker="m", bis="sachl"),
    ficon("tabler", "building-bank", XS, 380, 130, "sachl", fuell=GRUEN, anim="cut", bis=beim("strafr", "Strafrichter")),
    pl("Amtsgericht", XS, 160, "sachl", fill=GRUEN, size=30, anker="m", anim="cut", bis=beim("strafr", "Strafrichter")),
    ficon("tabler", "gavel", XS, 380, 110, beim("strafr", "Strafrichter"), fuell=HOLZ, anim="cut"),
    pl("Strafrichter", XS, 160, beim("strafr", "Strafrichter"), fill=GELB, size=30, anker="m", anim="cut"),
]))

# H3 B. Prozessuale Tat, § 264 StPO ----------------------------------------------------------------------------------------
folie([("tat", f"{PB} › prozessuale Tat, § 264 StPO"), ("zwei", f"{PB} › zwei prozessuale Taten"),
       ("jede", f"{PB} › je Tat eine Entscheidung")], rechts_frei([
    *tafel("tat", "Prozessuale Tat, § 264 StPO", size=46),
    *wortlaut(110, 180, 1040, 230, "ges", [
        [("„… ", 0), ("geschichtlichen Vorgang", "a"), (" …, innerhalb dessen der Angeklagte", 0)],
        [("einen Straftatbestand verwirklicht haben soll und der sich auf", 0)],
        [("das gesamte Verhalten des Täters erstreckt, das nach", 0)],
        [("natürlicher Auffassung", "b"), (" ein mit diesem Vorgang ", 0), ("einheitliches", "c")],
        [("Geschehen", "c"), (" bildet“", 0)],
    ], 30, {"a": beim("ges", "geschichtliche"), "b": beim("ges", "natürlicher"), "c": beim("ges", "einheitliches")},
        "BGH, Beschl. v. 23.5.2023 – GSSt 1/23, Rn. 25 (st. Rspr.)"),
    fl_block(110, 490, 500, 150, GELB, "zwei", [("Tat 1: Diebstahl", "ExtraBold", 34, INK), ("im Markt", "Bold", 30, INK)]),
    fl_block(650, 490, 500, 150, ROTHELL, beim("zwei", "Beleidigung"),
             [("Tat 2: Beleidigung", "ExtraBold", 34, INK), ("drei Tage später", "Bold", 30, INK)]),
    z("Jede Tat braucht ihre eigene Abschlussentscheidung.", 110, 700, "jede", "Bold", 36),
    peep_voll("RO_ruhig", X1, BR, FR, "tat", bis="jede"),
    peep_voll("RO_denkt", X1, BR, FR, "jede", anim="cut"),
    peep_voll("SA_denkt", X2, BR, FR, "tat", d=0.2, bis="zwei"),
    peep_voll("SA_ruhig", X2, BR, FR, "zwei", anim="cut"),
    namensschild("Herr Rösch", X1, BR, "tat", BLAU, d=0.2),
    namensschild("Staatsanwältin", X2, BR, "tat", LILA, d=0.3),
    ficon("tabler", "folders", MB, 380, 110, "tat", fuell=GELB, bis="zwei"),
    pl("prozessuale Tat", MB, 160, "tat", fill=WEISS, size=28, anker="m", bis="zwei"),
    ficon("tabler", "calendar-event", MB, 380, 100, "zwei", fuell=WEISS, anim="cut"),
    pl("zwei Taten", MB, 160, "zwei", fill=GELB, size=30, anker="m", anim="cut"),
]))

# I C. Abschlussverfügung -----------------------------------------------------------------------------------------------------
PC = "C. Abschlussverfügung"
folie([("verf", PC), ("p170b", f"{PC} › Tat 2: Einstellung, § 170 Abs. 2 StPO"),
       ("mitt", f"{PC} › Mitteilung an den Beschuldigten"), ("opp", f"{PC} › Abgrenzung: §§ 153, 154 StPO"),
       ("verm", f"{PC} › Tat 1: Vermerk, § 169a StPO"), ("ankl", f"{PC} › Tat 1: Anklage zum Strafrichter")], rechts_frei([
    *tafel("verf", "C. Abschlussverfügung"),
    z("Tat 2, Beleidigung:", 110, 180, "p170b", "ExtraBold", 36),
    *wortlaut(110, 240, 1040, 70, beim("p170b", "Andernfalls"), [
        [("„Andernfalls stellt die Staatsanwaltschaft das Verfahren ", 0), ("ein", "a"), (".“", 0)]], 30,
        {"a": beim("p170b", "ein", 2)}, "§ 170 Abs. 2 S. 1 StPO"),
    z("Mitteilung an Herrn Rösch, § 170 Abs. 2 S. 2 StPO", 150, 375, "mitt", size=32),
    fl_block(110, 430, 1040, 170, LILAHELL, "opp", [("", "Bold", 30, INK)]),
    z("Etwas anderes: §§ 153, 154 StPO", 140, 450, "opp", "ExtraBold", 32),
    z("§ 153: geringe Schuld, kein öffentliches Interesse", 150, 500, beim("opp2", "geringe"), size=30),
    z("§ 154: Strafe fällt neben anderer Tat kaum ins Gewicht", 150, 545, beim("opp2", "Strafe"), size=30),
    z("Tat 1, Diebstahl:", 110, 650, "verm", "ExtraBold", 36),
    z("Vermerk: Ermittlungen abgeschlossen, § 169a StPO", 150, 705, beim("verm", "Abschluss"), size=32),
    z("Anklage zum Strafrichter", 150, 760, "ankl", "Bold", 34),
    ok(1110, 780, beim("ankl", "Anklage"), gr=22),
    peep_voll("RO_ruhig", X1, BR, FR, "verf", bis="mitt"),
    peep_voll("RO_cool", X1, BR, FR, "mitt", anim="cut", bis="verm"),
    peep_voll("RO_schreck", X1, BR, FR, "ankl", anim="cut"),
    peep_voll("RO_denkt", X1, BR, FR, "verm", anim="cut", bis="ankl"),
    peep_voll("SA_ruhig", X2, BR, FR, "verf", d=0.2, bis="opp"),
    peep_voll("SA_denkt", X2, BR, FR, "opp", anim="cut", bis="verm"),
    peep_voll("SA_froh", X2, BR, FR, "verm", anim="cut"),
    namensschild("Herr Rösch", X1, BR, "verf", BLAU, d=0.2),
    namensschild("Staatsanwältin", X2, BR, "verf", LILA, d=0.3),
    ficon("tabler", "file-x", MB, 380, 100, "p170b", fuell=ROT, bis="mitt"),
    pl("Tat 2: eingestellt", MB, 160, "p170b", fill=ROTHELL, size=28, anker="m", bis="mitt"),
    ficon("tabler", "mail", MB, 380, 100, "mitt", fuell=WEISS, anim="cut", bis="opp"),
    pl("Mitteilung", MB, 160, "mitt", fill=WEISS, size=30, anker="m", anim="cut", bis="opp"),
    ficon("tabler", "file-check", MB, 380, 100, "verm", fuell=GRUEN, anim="cut"),
    pl("Tat 1: Anklage", MB, 160, "ankl", fill=GRUEN, size=28, anker="m"),
]))

# J Anklageschrift, § 200 StPO ----------------------------------------------------------------------------------------------
AX, AY, AW = 1250, 170, 340
SAj = 1745
folie([("p200", f"{PC} › Anklageschrift, § 200 Abs. 1 StPO"), ("satz", f"{PC} › Anklageschrift: Anklagesatz"),
       ("bm", f"{PC} › Anklageschrift: Beweismittel, Gericht"), ("wes", f"{PC} › Anklageschrift, § 200 Abs. 2 StPO")], [
    *tafel("p200", "Die Anklageschrift"),
    *wortlaut(110, 175, 1040, 255, "p200", [
        [("„Die Anklageschrift hat den ", 0), ("Angeschuldigten", "a"), (", ", 0), ("die Tat", "b"), (", die ihm", 0)],
        [("zur Last gelegt wird, ", 0), ("Zeit und Ort", "b"), (" ihrer Begehung, die ", 0), ("gesetzlichen", "c")],
        [("Merkmale", "c"), (" der Straftat und die ", 0), ("anzuwendenden Strafvorschriften", "d")],
        [("zu bezeichnen ", 0), ("(Anklagesatz)", "e"), (". In ihr sind ferner die ", 0), ("Beweismittel", "f"), (",", 0)],
        [("das Gericht", "g"), (", vor dem die Hauptverhandlung stattfinden soll,", 0)],
        [("und der ", 0), ("Verteidiger", "h"), (" anzugeben. …“", 0)],
    ], 28, {"a": beim("p200", "Angeschuldigte"), "b": beim("p200", "Tat"), "c": beim("p200", "gesetzlichen"),
            "d": beim("p200", "anzuwendenden"), "e": "satz", "f": beim("bm", "Beweismittel"), "g": beim("ger", "Gericht"),
            "h": beim("ger", "Verteidiger")}, "§ 200 Abs. 1 S. 1 und 2 StPO"),
    z("Abs. 2: wesentliches Ergebnis der Ermittlungen –", 110, 530, "wes", "Bold", 34),
    z("beim Strafrichter entbehrlich", 150, 580, beim("wes", "Strafrichter"), "Bold", 34),
    fl_block(110, 660, 1040, 130, HELL, "rist", [("Nr. 112 Abs. 1 RiStBV: trotzdem aufnehmen,", "Bold", 32, INK),
                                               ("wenn Sach- oder Rechtslage schwierig ist", "Bold", 32, INK)]),
    # Entwurf der Anklageschrift rechts
    karte(AX, AY, AW, 560, "p200", fill=WEISS, rund=10, schatten=6),
    zeile(glyphen("Anklageschrift"), AX + 25, AY + 25, "p200", "ExtraBold", 32),
    zeile(glyphen("Herr Rösch, 24"), AX + 25, AY + 95, "as1", "Bold", 26),
    zeile(glyphen("2. März 2026,"), AX + 25, AY + 150, "as2", size=26),
    zeile(glyphen("Elektronikmarkt"), AX + 25, AY + 185, "as2", size=26),
    zeile(glyphen("Diebstahl"), AX + 25, AY + 240, "as3", size=26),
    zeile(glyphen("§ 242 Abs. 1 StGB"), AX + 25, AY + 295, "as4", "Bold", 26),
    zeile(glyphen("Zeuge: Herr Brehm"), AX + 25, AY + 370, beim("bm", "Brehm"), size=26),
    zeile(glyphen("Video"), AX + 25, AY + 405, beim("bm", "Video"), size=26),
    zeile(glyphen("AG – Strafrichter –"), AX + 25, AY + 470, beim("ger", "Gericht"), "Bold", 26),
    peep_voll("SA_ruhig", SAj, BR, FR, "p200", bis="satz"),
    peep_voll("SA_froh", SAj, BR, FR, "satz", anim="cut", bis="wes"),
    peep_voll("SA_denkt", SAj, BR, FR, "wes", anim="cut"),
    namensschild("Staatsanwältin", SAj, BR, "p200", LILA, d=0.2),
])

# K Klausurtipp (Lexi) ---------------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · erst die prozessualen Taten"), ("tipp3", "Klausurtipp · Anklagesatz ohne Beweiswürdigung")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Zuerst die prozessualen Taten bilden", 200, 200, beim("tipp", "Bilde"), "Bold", 38),
    z("Für jede Tat eine Entscheidung:", 200, 300, "tipp2", "Bold", 38),
    z("Anklage oder Einstellung", 240, 355, beim("tipp2", "Anklage"), size=34, farbe=TEXT),
    z("Anklagesatz: das Geschehen,", 200, 460, "tipp3", "Bold", 38),
    z("nicht deine Beweiswürdigung", 240, 515, beim("tipp3", "nicht"), size=34, farbe=TEXT),
    nein(820, 535, beim("tipp3", "Beweiswürdigung"), gr=18),
    *redet("LX_warnt", LXX, BR, FR + 60, "tipp", "sch"),
    pille("Lexi", LXX, BR + 22, "tipp", fill=GELB, size=30, anker="m", d=0.2),
])

# L Klausurschema --------------------------------------------------------------------------------------------------------------
K1, K2 = 150, 210
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel("Klausurschema: Anklageklausur", 110, 90, "sch", 54),
    z("A. Materiell-rechtliches Gutachten", K1, 200, "sA", "Bold", 38, rechts=1820),
    z("je Tat: Strafbarkeit und Nachweis (hinreichender Tatverdacht, § 170 Abs. 1 StPO)", K2, 255, beim("sA", "für"),
      size=32, farbe=TEXT, rechts=1820),
    z("B. Prozessuales Gutachten", K1, 345, "sB", "Bold", 38, rechts=1820),
    z("Prozessvoraussetzungen (z. B. Strafantrag), Zuständigkeit, prozessuale Taten (§ 264 StPO)", K2, 400,
      beim("sB", "mit"), size=32, farbe=TEXT, rechts=1820),
    z("C. Abschlussverfügung", K1, 490, "sC", "Bold", 38, rechts=1820),
    z("I. Einstellung, § 170 Abs. 2 StPO: kein Tatverdacht oder Verfahrenshindernis", K2, 550, "sC1", size=34, rechts=1820),
    z("II. für den Rest: Anklageschrift, § 200 StPO", K2, 610, "sC2", size=34, rechts=1820),
])

# M Merksatz (Lexi) ------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Angeklagt wird nur, was", 0)], [("hinreichend verdächtig", "a"), (" und", 0)],
                 [("verfolgbar", "b"), (" ist.", 0)]], 750, 300, 50, "merke",
                {"a": beim("merke", "hinreichend"), "b": beim("merke", "verfolgbar")}),
    *markertext([[("Jede prozessuale Tat bekommt", 0)], [("ihre ", 0), ("eigene Entscheidung", "c"), (".", 0)]], 750, 610, 50,
                "mz", {"c": beim("mz", "eigene")}),
    *redet("LX_erklaert", 1680, 1000, 720, "merke", lexi_bis_ende("merke")),
])
