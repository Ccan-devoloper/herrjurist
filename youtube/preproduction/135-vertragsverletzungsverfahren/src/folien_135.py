"""Folge 135 · Vertragsverletzungsverfahren (Art. 258 AEUV): Das Prüfungsschema – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A1 Nitrat im Grundwasser (Feld, Grundwasser, Messstelle; keine Menschen), A2 Der Weg nach
Luxemburg (Zeitleiste des Vorverfahrens), A3 Lerngruppe (Antonia, Konstantin), B Sachverhalt, C1 Aufbau, C2 Wortlaut
Art. 258 AEUV, D1 A. Zulässigkeit 1./2., D2 3. Vorverfahren, D3 Zeitpunkt und 4., E1 B. Begründetheit, E2 Befund,
E3 Rechtfertigung, F1 C. Urteil, F2 Wortlaut Art. 260 Abs. 2 AEUV, Abs. 3, Nachgang, G Ergebnis (Lerngruppe),
H Klausurtipp (Lexi), I Klausurschema, J Merksatz (Lexi).
Geräusch nur bei sichtbarer Handlung: Klausurbogen wird auf den Tisch gelegt (Freesound CC0).
Hilfsfunktionen (z, pl, tafel, wortlaut, fb, redet mit hörbarem Wortende …) wie in Folge 131, Kopie im eigenen Ordner."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont

bausteine.FIGORDNER = "op_135/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
LILAHELL = (246, 243, 255, 255)
ROTHELL = (253, 232, 228, 255)
GRUENHELL = (232, 247, 233, 255)
BLAUHELL = (228, 238, 253, 255)
HOLZ = (214, 160, 110, 255)
HOLZD = (176, 122, 80, 255)
DAUER = bausteine._cj()["dauer"]

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


def tafel(cue, titel_, h=840, fill=WEISS, size=50):
    """Rechtstafel links, rechts bleibt Platz für die Figuren."""
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(glyphen(titel_), 110, 100, cue, size)]


def wortlaut(x, y, w, h, cue, zeilen, size, hl, quelle, quelle_cue=None):
    """Wortlautkarte: wörtliches Zitat (Cellar/EUR-Lex, Abruf 04.10.2026) in einer hellen Karte, Fundstelle darunter rechts.
    zeilen = Liste von Token-Listen [(text, Schlüssel|0)], hl = {Schlüssel: Cue} (Hervorhebung zum gesprochenen Wort)."""
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


def fb(x, y, w, h, fill, cue, zeilen, rund=18, anim="rise", d=0.0, bis=None):
    """Wie fl_block, Zeilenabstand passend zur Schriftgröße der Zeilen."""
    from engine import block
    for zz in zeilen:
        glyphen(zz[0])
    lh = int(max(zz[2] for zz in zeilen) * 1.3)
    assert len(zeilen) * lh * 1.15 <= h - 16, f"Block zu niedrig: {zeilen}"
    return block(x, y, w, h, fill, None, cue, textsize=lh, rund=rund, rand=INK, randbreite=5, anim=anim, d=d, bis=bis,
                 zeilen=zeilen)


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


def fund(text, x, y, cue, **k):
    """Fundstelle (mobil lesbar: 26 px)."""
    return z(text, x, y, cue, size=26, farbe=TEXT, **k)


# --- Eigene Hilfsfunktion (wie Folge 091): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ----------------
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


BR, FR = 930, 480                       # Figuren rechts neben der Tafel
X1, X2 = 1420, 1720                     # zwei Figuren
MB = (X1 + X2) // 2
IX = 1580                               # Requisiten rechts (Folien ohne Figuren)
def kette(prefix, x, folge, bis_=None, d=0.0, hoehe=FR, unten=BR):
    """Eine Figur mit Mimikfolge [(Name, Cue), …] im Zwiebelschalenprinzip (erster Auftritt pop, danach harte Schnitte)."""
    els = []
    for i, (n, c) in enumerate(folge):
        b = folge[i + 1][1] if i + 1 < len(folge) else bis_
        els.append(peep_voll(prefix + n, x, unten, hoehe, c, anim=("pop" if i == 0 else "cut"), d=(d if i == 0 else 0.0), bis=b))
    return els


def stufen(folge, x, unten, hoehe, rede=None, erst="pop", bis_=None):
    """Figur in der Fallszene: folge = [(Bildname, Cue), …]; rede = {Bildname: 1} für Figurenrede."""
    els = []
    for i, (n, c) in enumerate(folge):
        b = folge[i + 1][1] if i + 1 < len(folge) else bis_
        if rede and n in rede:
            els += redet(n, x, unten, hoehe, c, b)
        else:
            els.append(peep_voll(n, x, unten, hoehe, c, anim=(erst if i == 0 else "cut"), bis=b))
    return els


def wechsel(texte, cx, y, size=28, fill=WEISS, anker="m"):
    """Pillen nacheinander an derselben Stelle: texte = [(Text, Cue, Füllung|None), …]."""
    els = []
    for i, (t, c, f) in enumerate(texte):
        b = texte[i + 1][1] if i + 1 < len(texte) else None
        els.append(pl(t, cx, y, c, fill=f or fill, size=size, anker=anker, anim=("pop" if i == 0 else "cut"), bis=b))
    return els


def icons(folge, cx, unten, breite):
    """Requisiten nacheinander an derselben Stelle: folge = [(set, name, Cue, Füllung), …]."""
    els = []
    for i, (s, n, c, f) in enumerate(folge):
        b = folge[i + 1][2] if i + 1 < len(folge) else None
        els.append(ficon(s, n, cx, unten, breite, c, fuell=f, anim=("pop" if i == 0 else "cut"), bis=b))
    return els



def zeile_ok(text, x, y, cue, ja=True, size=32, stil="Regular", **k):
    """Tafelzeile mit Bleistift-Haken bzw. -Kreuz davor (zum gesprochenen Wort)."""
    return [(ok if ja else nein)(x + 25, y + 20, cue, gr=18), z(text, x + 65, y, cue, stil, size, **k)]




FARBE = {"AN": LILA, "KO": BLAU}
NAME = {"AN": "Antonia", "KO": "Konstantin"}
FX = 1560                               # eine Figur rechts neben der Tafel


def figur_rechts(p, folge, cue0, x=FX):
    """Eine Figur rechts der Tafel (blickt zur Tafel nach links), Namensschild ab dem ersten Bild."""
    return kette(p + "_", x, folge) + [namensschild(NAME[p], x, BR, cue0, FARBE[p], d=0.2)]


def zwei_rechts(an, ko, cue0):
    """Antonia (X1) und Konstantin (X2) rechts der Tafel, beide blicken zur Tafel nach links."""
    return figur_rechts("AN", an, cue0, X1) + figur_rechts("KO", ko, cue0, X2)


BODEN = 900
WASSER = (200, 224, 250, 255)
ERDE = (232, 206, 170, 255)

# A1 Nitrat im Grundwasser (keine Menschen; Feld, Grundwasser, Messstelle) ---------------------------------------------
folie([("fall", "Fall · Nitrat im Grundwasser"), (beim("mess", "Messstellen"), "Fall · Messstellen: 50 mg/l oder mehr"),
       ("richt", "Fall · Nitratrichtlinie 91/676/EWG"), ("zusatz", "Fall · Reichen die Maßnahmen nicht?")], [
    karte(60, 560, 1800, 150, "fall", fill=ERDE, rund=10, schatten=0, rand=5),
    karte(60, 700, 1800, 260, "fall", fill=WASSER, rund=10, schatten=0, rand=5),
    pl("Grundwasser", 1500, 790, "fall", fill=WEISS, size=34, anker="m"),
    *[ficon("tabler", "plant-2", x, 566, 110, "fall", fuell=GRUEN) for x in (180, 330, 480, 630)],
    *[ficon("tabler", "wheat", x, 566, 100, "fall", fuell=GELB) for x in (780, 930)],
    *[ficon("tabler", "droplet", x, 930, 70, "fall", fuell=BLAU) for x in (200, 420, 640, 1000)],
    pl("Nitrat im Grundwasser", 70, 40, "fall", fill=GELB, size=34),
    karte(1170, 470, 40, 360, beim("mess", "Messstellen"), fill=WEISS, rund=8, schatten=0, rand=5),
    ficon("tabler", "test-pipe", 1190, 472, 100, beim("mess", "Messstellen"), fuell=GELB),
    pl("Messstelle", 1190, 290, beim("mess", "Messstellen"), fill=WEISS, size=30, anker="m"),
    pl("rund die Hälfte der Messstellen: 50 mg/l oder mehr", 800, 160, beim("mess", "fünfzig"), fill=ROTHELL, size=34,
       anker="m"),
    fund("Belastungsmessnetz; EuGH, C-543/16, Rn. 36, 41, 56", 470, 235, beim("mess", "fünfzig"), rechts=1820),
    pl("Nitratrichtlinie: Aktionsprogramme", 1500, 40, "richt", fill=BLAU, size=30, anker="m"),
    pl("Regeln zum Düngen", 1500, 110, beim("richt", "Regeln"), fill=WEISS, size=30, anker="m"),
    ficon("tabler", "file-certificate", 1800, 250, 100, "richt", fuell=BLAU),
    pl("nicht genug? Dann zusätzliche Maßnahmen", 600, 370, "zusatz", fill=GELB, size=32, anker="m"),
    fund("Art. 5 Abs. 4, 5 RL 91/676/EWG", 330, 438, "zusatz", rechts=1820),
])

# A2 Der Weg nach Luxemburg: Zeitleiste ---------------------------------------------------------------------------------
TX = (240, 590, 940, 1290, 1640)
TL = 600
folie([("bericht", "Fall · 2012: der Nitratbericht"), ("mahn", "Fall · Das Vorverfahren"),
       ("dueng", "Fall · Fristablauf am 11.9.2014"), ("klage", "Fall · Die Klage der Kommission, Oktober 2016")], [
    karte(90, 90, 330, 200, "bericht", fill=BLAU, rund=12, schatten=6, rand=5),
    ficon("tabler", "stars", 255, 270, 150, "bericht", fuell=GELB),
    pl("Kommission, Brüssel", 255, 320, beim("bericht", "Brüssel"), fill=WEISS, size=28, anker="m"),
    linienzug([(120, TL), (1800, TL)], "bericht", breite=7, farbe=INK),
    ficon("tabler", "report-analytics", TX[0], TL - 20, 120, "bericht", fuell=WEISS),
    pl("7/2012", TX[0], TL + 25, "bericht", fill=WEISS, size=30, anker="m"),
    pl("Bericht: Wasserqualität", TX[0], TL + 95, "besser", fill=ROTHELL, size=28, anker="m"),
    pl("nicht verbessert", TX[0], TL + 155, beim("besser", "nicht"), fill=ROTHELL, size=28, anker="m"),
    ficon("tabler", "mail", TX[1], TL - 20, 120, "mahn", fuell=WEISS),
    pl("10/2013", TX[1], TL + 25, "mahn", fill=WEISS, size=30, anker="m"),
    pl("Mahnschreiben", TX[1], TL + 215, beim("mahn", "Mahnschreiben"), fill=HELL, size=28, anker="m"),
    ficon("tabler", "file-text", TX[2], TL - 20, 110, "stell", fuell=GELB),
    pl("7/2014", TX[2], TL + 25, "stell", fill=WEISS, size=30, anker="m"),
    pl("begründete Stellungnahme", TX[2], TL + 95, beim("stell", "begründete"), fill=GELB, size=28, anker="m"),
    pl("Frist: 2 Monate", TX[2], TL + 155, beim("stell", "Frist"), fill=GELB, size=28, anker="m"),
    ficon("tabler", "hourglass", TX[3], TL - 20, 100, "dueng", fuell=WEISS),
    pl("11.9.2014", TX[3], TL + 25, "dueng", fill=WEISS, size=30, anker="m"),
    pl("neue Düngeverordnung?", TX[3], TL + 215, beim("dueng", "Düngeverordnung"), fill=WEISS, size=28, anker="m"),
    pl("bei Fristablauf nicht in Kraft", TX[3], TL + 275, beim("dueng", "Fristablauf"), fill=ROTHELL, size=28, anker="m"),
    nein(TX[3] + 235, TL + 300, beim("dueng", "nicht")),
    ficon("fluent-emoji-high-contrast", "classical-building", TX[4], TL - 20, 140, "klage", fuell=GELB),
    pl("10/2016", TX[4], TL + 25, "klage", fill=WEISS, size=30, anker="m"),
    pl("Klage beim Gerichtshof", TX[4] - 30, TL + 95, beim("klage", "Gerichtshof"), fill=BLAU, size=28, anker="m"),
    fund("EuGH, C-543/16, Rn. 20–25, 30; Klage eingereicht am 27.10.2016", 1000, 960, beim("klage", "Gerichtshof"), rechts=1820),
])

# A3 Lerngruppe: Antonia und Konstantin ----------------------------------------------------------------------------------
GH = 520
AX, KX = 420, 1500


def tisch(cue, x0=700, w=520):
    return [linienzug([(60, BODEN), (1860, BODEN)], cue, breite=7, farbe=INK),
            karte(x0, 742, w, 34, cue, fill=HOLZ, rund=10, schatten=0, rand=5),
            karte(x0 + w // 2 - 22, 776, 44, BODEN - 776, cue, fill=HOLZD, rund=6, schatten=0, rand=5)]


ANa = ("AN_redet_r", AX, BODEN, GH)
KOa = ("KO_redet", KX, BODEN, GH)
folie([("lern", "Fall · Die Klausur in der Lerngruppe"), ("an1", "Fall · Die Klausurfrage"),
       ("ko1", "Fall · Konstantin: die neue Düngeverordnung")], [
    *tisch("lern"),
    ficon("tabler", "books", 790, 744, 120, "lern", fuell=ROT),
    szene(ficon("tabler", "file-text", 960, 744, 110, beim("lern", "Klausur"), fuell=WEISS), "135papier*", 1.0),
    pl("Klausur: Nitrat-Fall", 960, 560, beim("lern", "Klausur"), fill=WEISS, size=28, anker="m"),
    *stufen([("AN_ruhig_r", "lern"), ("AN_redet_r", "an1"), ("AN_denkt_r", "ko1")], AX, BODEN, GH,
            rede={"AN_redet_r": 1}, bis_="sv"),
    namensschild("Antonia", AX, BODEN, "lern", FARBE["AN"], d=0.2),
    *stufen([("KO_ruhig", "lern"), ("KO_denkt", "an1"), ("KO_redet", "ko1")], KX, BODEN, GH,
            rede={"KO_redet": 1}, bis_="sv"),
    namensschild("Konstantin", KX, BODEN, "lern", FARBE["KO"], d=0.2),
    blase("sprech", 640, 190, "an1", 760, 230, inhalt=["Hat die Klage der", "Kommission Erfolg?"], textsize=34,
          figur=ANa, bis="ko1"),
    blase("sprech", 720, 210, "ko1", 1150, 230, inhalt=["Aber 2017 kam doch eine", "neue Düngeverordnung!"],
          textsize=33, figur=KOa, bis="sv"),
])

# B Sachverhalt -------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    glyphen("Nach der Nitratrichtlinie 91/676/EWG muss Deutschland Aktionsprogramme mit Regeln zum Düngen aufstellen und "
            "zusätzliche Maßnahmen treffen, sobald deutlich wird, dass sie nicht reichen. Im Nitratbericht von 2012 lag "
            "an rund der Hälfte der Messstellen des Belastungsmessnetzes der Nitratwert bei 50 mg/l oder darüber; die "
            "Wasserqualität hatte sich nach Ansicht der Kommission nicht verbessert."),
    glyphen("Die Kommission schickt im Oktober 2013 ein Mahnschreiben und im Juli 2014 eine begründete Stellungnahme mit "
            "einer Frist von zwei Monaten (bis 11.9.2014). Die angekündigte neue Düngeverordnung gilt bei Fristablauf "
            "nicht; ihr stimmt der Bundesrat erst 2017 zu. Im Oktober 2016 erhebt die Kommission Klage."),
], "Hat die Klage der Kommission nach Art. 258 AEUV Erfolg?")

# C1 Aufbau ---------------------------------------------------------------------------------------------------------------
PS_ = "Prüfungsschema Art. 258 AEUV"
folie([("verw", f"{PS_} · Überblick: Video zu den Klagearten"), ("heute", f"{PS_} · Aufbau")], rechts_frei([
    *tafel("verw", "Die Vertragsverletzungsklage"),
    z("Verfahren vor dem Gerichtshof im Überblick:", 110, 180, "verw", "Bold", 32),
    z("siehe Video zu den Klagearten", 110, 225, beim("verw", "Video"), size=32),
    z("Hier: das Prüfungsschema der Klage", 110, 310, "heute", "Bold", 34),
    fb(110, 380, 1040, 110, GRUENHELL, beim("heute", "Zulässigkeit"), [("A. Zulässigkeit", "ExtraBold", 40, INK)]),
    fb(110, 520, 1040, 110, BLAUHELL, beim("heute", "Begründetheit"), [("B. Begründetheit", "ExtraBold", 40, INK)]),
    fb(110, 660, 1040, 110, HELL, beim("heute", "Urteil"), [("C. Urteil", "ExtraBold", 40, INK)]),
    *zwei_rechts([("ruhig", "verw"), ("froh", "heute")], [("ruhig", "verw"), ("denkt", "heute")], "verw"),
]))

# C2 Wortlaut Art. 258 AEUV (ABl. C 202 vom 7.6.2016, S. 160) -----------------------------------------------------------------
W258 = [[("„Hat nach Auffassung der Kommission ein Mitgliedstaat", 0)],
        [("gegen eine Verpflichtung aus den Verträgen verstoßen, so", 0)],
        [("gibt sie eine ", 0), ("mit Gründen versehene Stellungnahme", "b")],
        [("hierzu ab; sie hat dem Staat zuvor ", 0), ("Gelegenheit zur", "a")],
        [("Äußerung", "a"), (" zu geben. Kommt der Staat dieser Stellungnahme", 0)],
        [("innerhalb der von der Kommission ", 0), ("gesetzten Frist", "c"), (" nicht", 0)],
        [("nach, so kann die Kommission den ", 0), ("Gerichtshof der", "d")],
        [("Europäischen Union anrufen", "d"), (".“", 0)]]
folie([("wl258", "Art. 258 AEUV · Wortlaut"), ("stell2", "Art. 258 AEUV · begründete Stellungnahme"),
       ("w258b", "Art. 258 AEUV · Frist und Klage")], rechts_frei([
    *tafel("wl258", "Art. 258 AEUV"),
    *wortlaut(110, 175, 1040, 360, "wl258", W258, 31,
              {"a": beim("wl258", "Gelegenheit"), "b": beim("stell2", "Gründen"), "c": beim("w258b", "Frist"),
               "d": beim("w258b", "Gerichtshof")}, "Art. 258 Abs. 1, 2 AEUV"),
    pl("1. Gelegenheit zur Äußerung", 330, 640, beim("wl258", "Gelegenheit"), fill=WEISS, size=29, anker="m"),
    pl("2. Stellungnahme mit Frist", 700, 720, "stell2", fill=GELB, size=29, anker="m"),
    pl("3. Klage", 1000, 640, beim("w258b", "Gerichtshof"), fill=BLAU, size=29, anker="m"),
    *figur_rechts("KO", [("ruhig", "wl258"), ("denkt", "stell2"), ("ernst", "w258b")], "wl258"),
]))

# D1 A. Zulässigkeit: 1. Zuständigkeit, 2. Parteifähigkeit -----------------------------------------------------------------
PA = "A. Zulässigkeit"
folie([("zul", PA), ("zust", f"{PA} › 1. Zuständigkeit des Gerichtshofs"), ("partei", f"{PA} › 2. Parteifähigkeit"),
       ("a259", f"{PA} › 2. Parteifähigkeit: Staatenklage, Art. 259")], rechts_frei([
    *tafel("zul", "A. Zulässigkeit", fill=WEISS),
    *zeile_ok("1. Zuständigkeit: der Gerichtshof selbst", 110, 175, "zust", stil="Bold", size=33),
    z("Art. 256 Abs. 1 AEUV weist Klagen nach Art. 258", 175, 228, beim("zust", "Artikel"), size=30),
    z("nicht dem Gericht der EU (EuG) zu", 175, 268, beim("zust", "Gericht", nr=2), size=30),
    *zeile_ok("2. Parteifähigkeit", 110, 350, "partei", stil="Bold", size=33),
    karte(175, 405, 470, 110, beim("partei", "Klägerin"), fill=BLAUHELL, rund=16, schatten=5, rand=4),
    z("Klägerin: Kommission", 200, 437, beim("partei", "Klägerin"), "Bold", 30, rechts=640),
    karte(680, 405, 470, 110, beim("partei", "Beklagte"), fill=ROTHELL, rund=16, schatten=5, rand=4),
    z("Beklagte: Deutschland", 705, 437, beim("partei", "Beklagte"), "Bold", 30, rechts=1140),
    fb(110, 570, 1040, 135, HELL, "a259", [("Art. 259 AEUV: auch ein Mitgliedstaat kann klagen,", "ExtraBold", 30, INK),
                                          ("muss aber zuerst die Kommission befassen", "ExtraBold", 30, INK)]),
    *figur_rechts("AN", [("ruhig", "zul"), ("denkt", "zust"), ("ruhig", "partei"), ("ernst", "a259")], "zul"),
]))

# D2 3. Vorverfahren ---------------------------------------------------------------------------------------------------------
folie([("vorv", f"{PA} › 3. ordnungsgemäßes Vorverfahren"), ("deck", f"{PA} › 3. deckungsgleicher Streitgegenstand"),
       ("nit3", f"{PA} › 3. Vorverfahren im Nitrat-Fall")], rechts_frei([
    *tafel("vorv", "3. Ordnungsgemäßes Vorverfahren"),
    karte(110, 175, 470, 120, "mahn2", fill=HELL, rund=16, schatten=5, rand=4),
    z("Mahnschreiben:", 135, 188, "mahn2", "Bold", 31, rechts=570),
    z("Gelegenheit zur Äußerung", 135, 233, beim("mahn2", "Gelegenheit"), size=30, rechts=570),
    pfeil(600, 235, 660, 235, "begr", breite=8, kopf=22),
    karte(680, 175, 470, 120, "begr", fill=GELB, rund=16, schatten=5, rand=4),
    z("begründete Stellungnahme:", 705, 188, "begr", "Bold", 31, rechts=1140),
    z("setzt eine Frist", 705, 233, beim("begr", "Frist"), size=30, rechts=1140),
    z("Klage nur mit Rügen aus dem Vorverfahren:", 110, 345, "deck", "Bold", 32),
    fb(110, 395, 1040, 95, GRUENHELL, beim("deck", "Streitgegenstand"),
       [("Streitgegenstand deckungsgleich", "ExtraBold", 34, INK)]),
    fund("EuGH, C-152/98 (Kommission/Niederlande), Rn. 23–25", 110, 500, beim("deck", "deckungsgleich")),
    z("Nitrat-Fall:", 110, 575, "nit3", "ExtraBold", 33),
    *zeile_ok("Stellungnahme hält die Rügen des Mahnschreibens aufrecht", 110, 625, beim("nit3", "Stellungnahme"), size=30),
    *zeile_ok("Frist bis 11.9.2014", 110, 685, beim("nit3", "Frist"), stil="Bold", size=31),
    fund("EuGH, C-543/16, Rn. 21, 23", 175, 735, beim("nit3", "elften")),
    *figur_rechts("KO", [("ruhig", "vorv"), ("denkt", "deck"), ("ernst", "nit3")], "vorv"),
]))

# D3 Maßgeblicher Zeitpunkt und 4. Klageart, Rechtsschutzbedürfnis ------------------------------------------------------------
folie([("zeit", f"{PA} › 3. maßgeblicher Zeitpunkt: Fristablauf"), ("rsb", f"{PA} › 4. Klageart und Rechtsschutzbedürfnis"),
       ("zul2", f"{PA} › Ergebnis: zulässig")], rechts_frei([
    *tafel("zeit", "Zeitpunkt, Klageart, Interesse"),
    fb(110, 175, 1040, 135, LILAHELL, "zeit", [("Maßgeblich: die Lage bei Fristablauf", "ExtraBold", 33, INK),
                                              ("hier am 11.9.2014", "ExtraBold", 31, INK)]),
    *zeile_ok("spätere Änderungen zählen nicht", 110, 330, beim("zeit", "Spätere"), ja=False, stil="Bold", size=31),
    fund("EuGH, C-543/16, Rn. 70; C-152/98, Rn. 21", 175, 378, beim("zeit", "zählen")),
    z("4. Klageart und Rechtsschutzbedürfnis", 110, 445, "rsb", "Bold", 33),
    *zeile_ok("statthaft: Vertragsverletzungsklage", 110, 500, beim("rsb", "Statthaft"), size=31),
    *zeile_ok("kein besonderes Interesse der Kommission nötig,", 110, 560, beim("rsb", "Ein"), size=31),
    z("auch nicht nach Abstellen des Verstoßes", 175, 605, beim("rsb", "auch"), size=31),
    fund("EuGH, C-431/92 (Großkrotzenburg), Rn. 19–21", 175, 650, beim("rsb", "abstellt")),
    fb(110, 715, 1040, 95, GRUEN, "zul2", [("Die Klage ist zulässig.", "ExtraBold", 36, INK)]),
    *figur_rechts("KO", [("denkt", "zeit"), ("staunt", beim("zeit", "Spätere")), ("ruhig", "rsb"), ("froh", "zul2")],
                  "zeit"),
]))

# E1 B. Begründetheit: Verstoß, Zurechnung, Pflicht ----------------------------------------------------------------------------
PB = "B. Begründetheit"
folie([("bgr", f"{PB} › Verstoß gegen Unionsrecht?"), ("zurech", f"{PB} › Zurechnung: alle Stellen des Staates"),
       ("pfl", f"{PB} › Pflicht aus Art. 5 Abs. 5 RL 91/676")], rechts_frei([
    *tafel("bgr", "B. Begründetheit"),
    z("Hat Deutschland gegen Unionsrecht verstoßen?", 110, 175, "bgr", "Bold", 33),
    z("Der Staat steht für alle seine Stellen ein,", 110, 260, "zurech", "Bold", 31),
    z("auch für Länder und Gerichte", 110, 303, beim("zurech", "Länder"), "Bold", 31),
    fund("EuGH, C-416/17 (Kommission/Frankreich), Rn. 106 f.", 110, 345, beim("zurech", "Gerichte")),
    karte(110, 400, 1040, 110, beim("zurech", "Nitrat-Fall"), fill=HELL, rund=16, schatten=5, rand=4),
    z("Nitrat-Fall: Regeln der Länder zur Lagerung von Dung", 135, 418, beim("zurech", "Nitrat-Fall"), size=30,
      rechts=1140),
    fund("EuGH, C-543/16, Rn. 19, 132–136", 135, 462, beim("zurech", "Lagerung")),
    fb(110, 560, 1040, 135, BLAUHELL, "pfl", [("Pflicht: zusätzliche Maßnahmen, sobald deutlich", "ExtraBold", 30, INK),
                                             ("wird, dass das Aktionsprogramm nicht reicht", "ExtraBold", 30, INK)]),
    fund("Art. 5 Abs. 5 RL 91/676/EWG; EuGH, C-543/16, Rn. 52 f.", 110, 705, beim("pfl", "Aktionsprogramm")),
    *figur_rechts("AN", [("ruhig", "bgr"), ("denkt", "zurech"), ("ernst", "pfl")], "bgr"),
]))

# E2 Der Befund des Gerichtshofs -----------------------------------------------------------------------------------------------
folie([("eutro", f"{PB} › Maßnahmen reichten nicht"), ("prog", f"{PB} › Aktionsprogramm mangelhaft")], [
    *tafel("eutro", "Der Befund des Gerichtshofs"),
    ficon("tabler", "ripple", 190, 290, 120, beim("eutro", "Nord-"), fuell=None),
    z("Nord- und Ostsee: Überdüngung (Eutrophierung)", 270, 185, beim("eutro", "Nord-"), "Bold", 30),
    z("der Küstengewässer nicht gebessert", 270, 228, beim("eutro", "Küstengewässer"), "Bold", 30),
    *zeile_ok("Also: Die Maßnahmen reichten nicht.", 270, 280, beim("eutro", "Maßnahmen"), ja=False, size=31),
    fund("EuGH, C-543/16, Rn. 33 f., 59–61", 335, 330, beim("eutro", "reichten")),
    z("Auch das Aktionsprogramm selbst war mangelhaft:", 110, 400, "prog", "Bold", 32),
    ficon("tabler", "calendar", 245, 600, 110, beim("prog", "Sperrzeiten"), fuell=WEISS),
    pl("Sperrzeiten", 245, 620, beim("prog", "Sperrzeiten"), fill=HELL, size=28, anker="m"),
    ficon("tabler", "snowflake", 505, 600, 110, beim("prog", "gefrorenen"), fuell=None),
    pl("gefrorene Böden", 505, 620, beim("prog", "gefrorenen"), fill=BLAUHELL, size=28, anker="m"),
    ficon("tabler", "mountain", 760, 600, 120, beim("prog", "Hanglagen"), fuell=GRUEN),
    pl("Hanglagen", 760, 620, beim("prog", "Hanglagen"), fill=GRUENHELL, size=28, anker="m"),
    ficon("tabler", "building-warehouse", 1040, 600, 110, beim("prog", "Lagerraum"), fuell=HOLZ),
    pl("Lagerraum für Dung", 1040, 620, beim("prog", "Lagerraum"), fill=ROTHELL, size=28, anker="m"),
    fund("EuGH, C-543/16, Rn. 121, 176, 167, 136", 110, 700, beim("prog", "Dung")),
    *figur_rechts("KO", [("ernst", "eutro"), ("staunt", "prog")], "eutro"),
])

# E3 Rechtfertigung? und Ergebnis Begründetheit ---------------------------------------------------------------------------------
ANb = ("AN_redet", X1, BR, FR)
folie([("recht", f"{PB} › Rechtfertigung durch Deutschland?"), ("intern", f"{PB} › keine Berufung auf innerstaatliche Gründe"),
       ("an2", f"{PB} › Düngeverordnung 2017: nach Fristablauf"), ("bgr2", f"{PB} › Ergebnis: begründet")], rechts_frei([
    *tafel("recht", "Rechtfertigung?"),
    z("Deutschland trägt vor:", 110, 175, "recht", "Bold", 33),
    z("· Wirkung früherer Regeln noch nicht bewertbar", 135, 230, beim("recht", "Wirkung"), size=31),
    fund("EuGH, C-543/16, Rn. 48, 62–69", 165, 274, beim("recht", "bewerten")),
    z("· Regeln je nach Region schwer zu verwalten", 135, 325, beim("recht", "Regeln", nr=2), size=31),
    fund("EuGH, C-543/16, Rn. 101, 113", 165, 369, beim("recht", "verwalten")),
    nein(1110, 260, beim("intern", "Das")), nein(1110, 355, beim("intern", "Das")),
    fb(110, 425, 1040, 135, ROTHELL, beim("intern", "Ein"), [("Keine Berufung auf Umstände der", "ExtraBold", 32, INK),
                                                           ("internen Rechtsordnung", "ExtraBold", 32, INK)]),
    fund("EuGH, C-543/16, Rn. 114", 110, 570, beim("intern", "berufen")),
    *zeile_ok("Düngeverordnung 2017: erst nach Fristablauf", 110, 630, beim("an2", "Fristablauf"), ja=False, size=31),
    fund("EuGH, C-543/16, Rn. 49, 70", 175, 678, beim("an2", "zählt")),
    fb(110, 735, 1040, 95, GRUEN, "bgr2", [("Die Klage ist begründet.", "ExtraBold", 36, INK)]),
    *stufen([("AN_ruhig", "recht"), ("AN_denkt", "intern"), ("AN_redet", "an2"), ("AN_froh", "bgr2")], X1, BR, FR,
            rede={"AN_redet": 1}, erst="pop"),
    namensschild("Antonia", X1, BR, "recht", FARBE["AN"], d=0.2),
    *figur_rechts("KO", [("ruhig", "recht"), ("denkt", "intern"), ("staunt", "an2"), ("froh", "bgr2")], "recht", X2),
    blase("sprech", 640, 240, "an2", 1555, 230, inhalt=["Die Düngeverordnung von 2017", "kam erst nach Fristablauf.",
          "Sie zählt nicht."], textsize=29, figur=ANb, bis="bgr2"),
]))

# F1 C. Urteil -----------------------------------------------------------------------------------------------------------------
PC = "C. Urteil"
folie([("urt", f"{PC} › Urteil vom 21.6.2018, C-543/16"), ("fest", f"{PC} › Feststellungsurteil, Art. 260 Abs. 1")],
      rechts_frei([
    *tafel("urt", "C. Urteil"),
    z("EuGH, Urt. v. 21.6.2018 – C-543/16", 110, 175, beim("urt", "einundzwanzigsten"), "Bold", 33),
    *zeile_ok("Verstoß festgestellt", 110, 235, beim("urt", "fest"), stil="Bold", size=33),
    fund("Tenor Nr. 1 (Art. 5 Abs. 5, 7 RL 91/676/EWG); Nr. 2: Kosten", 175, 285, beim("urt", "fest")),
    fb(110, 360, 1040, 95, GELB, "fest", [("Feststellungsurteil", "ExtraBold", 38, INK)]),
    z("Art. 260 Abs. 1 AEUV: Deutschland muss die Maßnahmen", 110, 495, beim("fest", "Artikel"), "Bold", 31),
    z("ergreifen, die sich aus dem Urteil ergeben", 110, 540, beim("fest", "ergreifen"), "Bold", 31),
    *figur_rechts("AN", [("ernst", "urt"), ("ruhig", "fest")], "urt"),
]) + [ficon("tabler", "gavel", 640, 840, 220, beim("fest", "Urteil"), fuell=HOLZ)])

# F2 Wortlaut Art. 260 Abs. 2 AEUV (auszugsweise; ABl. C 202 vom 7.6.2016, S. 161), Abs. 3, Nachgang ------------------------------
W260 = [[("„Hat der betreffende Mitgliedstaat die Maßnahmen, die sich", 0)],
        [("aus dem Urteil des Gerichtshofs ergeben, nach Auffassung der", 0)],
        [("Kommission nicht getroffen, so kann die Kommission den", 0)],
        [("Gerichtshof anrufen", "a"), (", nachdem sie diesem Staat zuvor", 0)],
        [("Gelegenheit zur Äußerung", "b"), (" gegeben hat. … Stellt der", 0)],
        [("Gerichtshof fest, dass der betreffende Mitgliedstaat seinem", 0)],
        [("Urteil nicht nachgekommen ist, so kann er die Zahlung eines", 0)],
        [("Pauschalbetrags oder Zwangsgelds", "c"), (" verhängen.“", 0)]]
folie([("wl260", f"{PC} › Art. 260 Abs. 2: zweites Verfahren"), ("geld", f"{PC} › Pauschalbetrag oder Zwangsgeld"),
       ("abs3", f"{PC} › Art. 260 Abs. 3: schon im ersten Urteil"), ("danach", f"{PC} › Nitrat-Fall: Aufforderung 2019")],
      rechts_frei([
    *tafel("wl260", "Art. 260 Abs. 2 AEUV"),
    *wortlaut(110, 175, 1040, 360, "wl260", W260, 31,
              {"a": beim("wl260", "Gerichtshof"), "b": beim("wl260", "Gelegenheit"), "c": beim("geld", "Pauschalbetrag")},
              "Art. 260 Abs. 2 UAbs. 1, 2 AEUV (auszugsweise)"),
    fb(110, 590, 1040, 120, LILAHELL, "abs3", [("Abs. 3: Umsetzung einer Richtlinie nicht mitgeteilt?", "ExtraBold", 30, INK),
                                              ("Sanktion schon im ersten Urteil möglich", "ExtraBold", 30, INK)]),
    z("Nitrat-Fall: Juli 2019 Aufforderungsschreiben nach Art. 260", 110, 745, "danach", "Bold", 30),
    z("(Kommission: Mängel nicht vollständig behoben)", 110, 788, beim("danach", "Mängel"), size=30),
    fund("Kommission, INF/19/4251 vom 25.7.2019", 110, 832, beim("danach", "behoben")),
    *figur_rechts("KO", [("ruhig", "wl260"), ("ernst", "geld"), ("denkt", "abs3"), ("staunt", "danach")], "wl260"),
]))

# G Ergebnis (zurück in der Lerngruppe) ------------------------------------------------------------------------------------------
KOb = ("KO_redet", KX, BODEN, GH)
folie([("erg", "Ergebnis · Die Klage der Kommission hat Erfolg")], [
    *tisch("erg"),
    ficon("tabler", "books", 790, 744, 120, "erg", fuell=ROT),
    ficon("tabler", "file-text", 960, 744, 110, "erg", fuell=WEISS),
    pl("Ergebnis: Die Klage hat Erfolg.", 470, 90, "erg", fill=GELB, size=40, anker="m"),
    pl("zulässig", 830, 470, beim("erg", "zulässig"), fill=GRUEN, size=32, anker="m"),
    ok(930, 450, beim("erg", "zulässig")),
    pl("begründet", 1060, 470, beim("erg", "begründet"), fill=GRUEN, size=32, anker="m"),
    ok(1170, 450, beim("erg", "begründet")),
    *stufen([("AN_froh_r", "erg"), ("AN_ruhig_r", "ko2")], AX, BODEN, GH, bis_="tipp"),
    namensschild("Antonia", AX, BODEN, "erg", FARBE["AN"], d=0.2),
    *stufen([("KO_ruhig", "erg"), ("KO_redet", "ko2")], KX, BODEN, GH, rede={"KO_redet": 1}, bis_="tipp"),
    namensschild("Konstantin", KX, BODEN, "erg", FARBE["KO"], d=0.2),
    blase("sprech", 740, 210, "ko2", 1170, 240, inhalt=["Dann zählt die neue Düngeverordnung", "erst bei der Umsetzung des Urteils."],
          textsize=31, figur=KOb),
])

# H Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · Streitgegenstand vergleichen"), ("tipp3", "Klausurtipp · Änderungen nach Fristablauf")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Vergleiche:", 200, 200, "tipp", "Bold", 34),
    z("Mahnschreiben · Stellungnahme · Klageantrag", 200, 255, beim("tipp", "Mahnschreiben"), size=32),
    *zeile_ok("Rüge fehlte im Vorverfahren?", 150, 340, "tipp2", stil="Bold", ja=False),
    z("Die Kommission kann sie nicht nachschieben.", 215, 390, beim("tipp2", "nachschieben"), size=32),
    fund("EuGH, C-152/98, Rn. 23–25 (insoweit unzulässig)", 215, 435, beim("tipp2", "nachschieben")),
    fb(110, 520, 1040, 135, GRUEN, "tipp3", [("Änderungen nach Fristablauf: keine", "ExtraBold", 32, INK),
                                            ("Rechtfertigung, der Verstoß bleibt", "ExtraBold", 32, INK)]),
    fund("EuGH, C-543/16, Rn. 70", 110, 665, beim("tipp3", "bestehen")),
    *redet("LX_warnt", LXX, BR, FR + 60, "tipp", "sch"),
    namensschild("Lexi", LXX, BR, "tipp", GELB, d=0.2),
])

# I Klausurschema (progressiv, breit) ----------------------------------------------------------------------------------------
PSC = "Klausurschema"
SZ = [("A. Zulässigkeit", "sa", 0, "ExtraBold"),
      ("1. Zuständigkeit des Gerichtshofs (Art. 256 Abs. 1 AEUV: nicht das EuG)", "sa1", 1, "Regular"),
      ("2. Parteifähigkeit: Kommission gegen Mitgliedstaat (Art. 259: Staatenklage)", "sa2", 1, "Regular"),
      ("3. ordnungsgemäßes Vorverfahren: Mahnschreiben, begründete Stellungnahme mit", "sa3", 1, "Regular"),
      ("    Frist; deckungsgleicher Streitgegenstand", "sa3", 1, "Regular"),
      ("4. Klageart und Rechtsschutzbedürfnis (kein besonderes Interesse nötig)", "sa4", 1, "Regular"),
      ("B. Begründetheit", "sb", 0, "ExtraBold"),
      ("1. Verstoß des Mitgliedstaats gegen Unionsrecht bei Fristablauf (alle Stellen)", "sb1", 1, "Regular"),
      ("2. keine Rechtfertigung durch innerstaatliche Gründe", "sb2", 1, "Regular"),
      ("C. Urteil", "sc", 0, "ExtraBold"),
      ("1. Feststellungsurteil, Art. 260 Abs. 1 AEUV", "sc1", 1, "Regular"),
      ("2. bei Nichtbefolgung: Pauschalbetrag oder Zwangsgeld, Art. 260 Abs. 2 AEUV", "sc2", 1, "Regular")]
folie([("sch", PSC), ("sa", f"{PSC} › A. Zulässigkeit"), ("sb", f"{PSC} › B. Begründetheit"), ("sc", f"{PSC} › C. Urteil")], [
    karte(60, 50, 1800, 930, "sch"), titel(glyphen("Klausurschema: Klage der Kommission nach Art. 258 AEUV"), 110, 90, "sch", 46),
    *[z(t, 110 + 50 * e, 175 + i * 63, c, st, 34 if e == 0 else 31, rechts=1820) for i, (t, c, e, st) in enumerate(SZ)],
])

# J Merksatz (Lexi) --------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Das Vorverfahren ", 0), ("zieht den Rahmen", "a"), (",", 0)],
                 [("der Fristablauf ", 0), ("hält die Lage fest", "b"), (",", 0)],
                 [("und wer das Urteil missachtet,", 0)],
                 [("riskiert ein ", 0), ("Zwangsgeld", "c"), (".", 0)]], 750, 330, 50, "merke",
                {"a": beim("merke", "zieht"), "b": beim("m1", "hält"), "c": beim("m2", "Zwangsgeld")}),
    *redet("LX_erklaert", 1680, 960, 690, "merke", lexi_bis_ende("merke")),
    namensschild("Lexi", 1680, 960, "merke", GELB, d=0.2),
])
