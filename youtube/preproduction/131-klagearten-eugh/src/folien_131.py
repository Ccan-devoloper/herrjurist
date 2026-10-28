"""Folge 131 · Klagearten EuGH: Vorlage, Nichtigkeitsklage, Vertragsverletzung – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A1 Verwaltungsgericht (Richterin Eichhorn), A2 Baustofffirma (Frau Pfister), A3 Europäische
Kommission (Herr Teichmann), A4 Frage (alle drei), B Sachverhalt, C Überblick (Raster Wer? Wogegen? Voraussetzungen? Folge?),
D1 Wortlaut Art. 267 AEUV, D2 Vorabentscheidung: Wer, Ausnahmen, Gültigkeit, D3 Folge, Art. 101 GG, Fall 1,
E1 Nichtigkeitsklage: Wogegen, Kläger, E2 Wortlaut Art. 263 Abs. 4 AEUV, Plaumann, Inuit, E3 Frist, EuG, Folge, Fall 2,
F1 Wortlaut Art. 258 AEUV, F2 Vertragsverletzung: Wer, Vorverfahren, Folge, F3 Fall 3 und Art. 265/340, G Ergebnis,
H Klausurtipp (Lexi), I Klausurschema als Übersicht (Raster), J Merksatz (Lexi).
Geräusch nur bei sichtbarer Handlung: Briefumschlag gleitet auf den Tisch (Beschluss der Kommission), Freesound CC0.
Hilfsfunktionen (z, pl, tafel, wortlaut, fb, redet mit hörbarem Wortende …) wie in Folge 127, Kopie im eigenen Ordner."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont

bausteine.FIGORDNER = "op_131/"
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



FARBE = {"EI": LILA, "PF": ROT, "TE": BLAU}
NAME = {"EI": "Richterin Eichhorn", "PF": "Frau Pfister", "TE": "Herr Teichmann"}
FX = 1560                               # eine Figur rechts neben der Tafel


def figur_rechts(p, folge, cue0):
    """Eine Fallfigur rechts der Tafel (blickt zur Tafel nach links), Namensschild ab dem ersten Bild."""
    return kette(p + "_", FX, folge) + [namensschild(NAME[p], FX, BR, cue0, FARBE[p], d=0.2)]


def zeile_ok(text, x, y, cue, ja=True, size=32, stil="Regular", **k):
    """Tafelzeile mit Bleistift-Haken bzw. -Kreuz davor (zum gesprochenen Wort)."""
    return [(ok if ja else nein)(x + 25, y + 20, cue, gr=18), z(text, x + 65, y, cue, stil, size, **k)]


# A Drei Mini-Fälle -------------------------------------------------------------------------------------------------------
BODEN, GH = 900, 520
LX_, RX_ = 400, 1540                     # Fallfigur links bzw. rechts


def tisch(cue, x0=720, w=440):
    """Bodenlinie und Tisch aus Grundformen (wie Folge 127)."""
    return [linienzug([(60, BODEN), (1860, BODEN)], cue, breite=7, farbe=INK),
            karte(x0, 742, w, 34, cue, fill=HOLZ, rund=10, schatten=0, rand=5),
            karte(x0 + w // 2 - 22, 776, 44, BODEN - 776, cue, fill=HOLZD, rund=6, schatten=0, rand=5)]


EIa = ("EI_redet_r", LX_, BODEN, GH)
folie([("fall", "Fall · Drei Fälle für Luxemburg"), ("eich", "Fall 1 · Richterin Eichhorn am Verwaltungsgericht"),
       ("unklar", "Fall 1 · Ein Begriff der Verordnung ist unklar")], [
    *tisch("fall"),
    pl("Drei Fälle für Luxemburg", 70, 40, "fall", fill=GELB, size=34, bis="eich"),
    ficon("tabler", "scale", 1600, BODEN, 260, "fall", fuell=GELB),
    pl("Verwaltungsgericht", 1600, 560, beim("eich", "Verwaltungsgericht"), fill=LILAHELL, size=30, anker="m"),
    *stufen([("EI_ruhig_r", "eich"), ("EI_denkt_r", "unklar"), ("EI_redet_r", "ei1")], LX_, BODEN, GH,
            rede={"EI_redet_r": 1}, bis_="pfist"),
    namensschild("Richterin Eichhorn", LX_, BODEN, "eich", FARBE["EI"], d=0.2),
    ficon("tabler", "file-text", 830, 744, 120, beim("eich", "Bescheid"), fuell=WEISS),
    pl("Bescheid", 830, 560, beim("eich", "Bescheid"), fill=WEISS, size=28, anker="m"),
    ficon("tabler", "file-certificate", 1060, 744, 130, beim("eich", "EU-Verordnung"), fuell=BLAU),
    pl("EU-Verordnung", 1060, 560, beim("eich", "EU-Verordnung"), fill=BLAU, size=28, anker="m"),
    ficon("tabler", "question-mark", 1170, 545, 64, "unklar", fuell=None),
    pl("ein Begriff: unklar", 1000, 405, beim("unklar", "Begriff"), fill=PINK, size=30, anker="m", bis="ei1"),
    blase("sprech", 700, 210, "ei1", 900, 250, inhalt=["Wie ist dieser Begriff auszulegen?",
          "Das soll der Gerichtshof klären."], textsize=32, figur=EIa, bis="pfist"),
])

PFa = ("PF_redet_r", LX_, BODEN, GH)
folie([("pfist", "Fall 2 · Frau Pfister und ihre Baustofffirma"), ("busse", "Fall 2 · Geldbuße per Beschluss der Kommission")], [
    *tisch("pfist"),
    ficon("tabler", "wall", 1600, BODEN, 240, "pfist", fuell=ROT),
    ficon("tabler", "truck", 1600, 620, 170, beim("pfist", "Baustofffirma"), fuell=GELB),
    pl("Baustofffirma", 1600, 340, beim("pfist", "Baustofffirma"), fill=GELB, size=30, anker="m"),
    *stufen([("PF_ruhig_r", "pfist"), ("PF_sorge_r", beim("busse", "Geldbuße")), ("PF_redet_r", "pf1")], LX_, BODEN, GH,
            rede={"PF_redet_r": 1}, bis_="teich"),
    namensschild("Frau Pfister", LX_, BODEN, "pfist", FARBE["PF"], d=0.2),
    szene(ficon("tabler", "mail", 840, 744, 130, beim("busse", "Kommission"), fuell=WEISS), "131brief*", 1.0, versatz=0.0),
    pl("Beschluss der Kommission", 900, 560, beim("busse", "Beschluss"), fill=BLAU, size=28, anker="m"),
    ficon("tabler", "coins", 1060, 744, 120, beim("busse", "Geldbuße"), fuell=GELB),
    pl("Geldbuße: Kartellverstoß", 1000, 500, beim("busse", "Kartellverstoßes"), fill=ROTHELL, size=30, anker="m", bis="pf1"),
    blase("sprech", 640, 210, "pf1", 860, 250, inhalt=["Diesen Beschluss lasse ich", "nicht stehen. Ich klage!"],
          textsize=32, figur=PFa, bis="teich"),
])

TEa = ("TE_redet", RX_, BODEN, GH)
folie([("teich", "Fall 3 · Herr Teichmann von der Europäischen Kommission"),
       ("hand", "Fall 3 · Zusatzgenehmigung für Handwerker")], [
    *tisch("teich", 640, 640),
    karte(90, 110, 330, 220, "teich", fill=BLAU, rund=12, schatten=6, rand=5),
    ficon("tabler", "stars", 255, 300, 170, "teich", fuell=GELB),
    pl("Europäische Kommission", 255, 360, beim("teich", "Europäischen"), fill=WEISS, size=28, anker="m"),
    *stufen([("TE_ruhig", "teich"), ("TE_denkt", "hand"), ("TE_redet", "te1")], RX_, BODEN, GH, rede={"TE_redet": 1}, bis_="frage"),
    namensschild("Herr Teichmann", RX_, BODEN, "teich", FARBE["TE"], d=0.2),
    ficon("tabler", "book", 760, 744, 150, beim("teich", "Gesetz"), fuell=ROT),
    pl("deutsches Gesetz", 760, 560, beim("teich", "Gesetz"), fill=ROTHELL, size=28, anker="m"),
    ficon("tabler", "tools", 1030, 744, 130, "hand", fuell=None),
    pl("Handwerker aus anderen Mitgliedstaaten", 900, 470, "hand", fill=WEISS, size=28, anker="m"),
    ficon("tabler", "license", 1190, 744, 110, beim("hand", "zusätzliche"), fuell=GELB),
    pl("+ zusätzliche Genehmigung", 1235, 560, beim("hand", "zusätzliche"), fill=GELB, size=28, anker="m", bis="te1"),
    blase("sprech", 660, 250, "te1", 1000, 230, inhalt=["Das verstößt gegen die", "Dienstleistungsfreiheit.",
          "Wir gehen gegen Deutschland vor."], textsize=31, figur=TEa, bis="frage"),
])

# A4 Die Frage: alle drei --------------------------------------------------------------------------------------------------
DX, DB, DH = (400, 960, 1520), 930, 440
folie([("frage", "Fall · Ein Gericht zweifelt, ein Unternehmen klagt, die Kommission klagt"),
       ("frage2", "Fall · Welches Verfahren passt?")], [
    linienzug([(60, DB), (1860, DB)], "frage", breite=7, farbe=INK),
    *figuren([("EI_denkt_r", "frage")], DX[0], DB, DH),
    namensschild("Richterin Eichhorn", DX[0], DB, "frage", FARBE["EI"], d=0.2),
    *figuren([("PF_entschlossen", "frage")], DX[1], DB, DH, d=0.1),
    namensschild("Frau Pfister", DX[1], DB, "frage", FARBE["PF"], d=0.3),
    *figuren([("TE_ernst", "frage")], DX[2], DB, DH, d=0.2),
    namensschild("Herr Teichmann", DX[2], DB, "frage", FARBE["TE"], d=0.4),
    pl("Gericht zweifelt", DX[0], 400, beim("frage", "Gericht"), fill=LILAHELL, size=30, anker="m"),
    pl("Unternehmen klagt", DX[1], 400, beim("frage", "Unternehmen"), fill=ROTHELL, size=30, anker="m"),
    pl("Kommission verklagt Deutschland", DX[2] - 60, 400, beim("frage", "Kommission"), fill=BLAUHELL, size=30, anker="m"),
    ficon("fluent-emoji-high-contrast", "classical-building", 960, 330, 130, "frage2", fuell=GELB),
    pl("Welches Verfahren passt jeweils?", 960, 90, "frage2", fill=PINK, size=40, anker="m"),
])

# B Sachverhalt -------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    glyphen("Richterin Eichhorn am Verwaltungsgericht entscheidet über einen Bescheid, der auf einer EU-Verordnung beruht. "
            "Ein Begriff der Verordnung ist unklar; sie will ihn vom Gerichtshof klären lassen. Gegen ihr Urteil gibt es "
            "noch ein Rechtsmittel."),
    glyphen("Frau Pfister führt eine Baustofffirma. Die Kommission verhängt gegen ihr Unternehmen per Beschluss eine "
            "Geldbuße wegen eines Kartellverstoßes. Frau Pfister will klagen."),
    glyphen("Herr Teichmann von der Europäischen Kommission prüft ein deutsches Gesetz: Handwerker aus anderen "
            "Mitgliedstaaten brauchen danach eine zusätzliche Genehmigung. Er hält das für einen Verstoß gegen die "
            "Dienstleistungsfreiheit."),
], "Welches Verfahren vor dem Gerichtshof der EU passt jeweils?")


# C Überblick und I Klausurschema: Raster mit drei Spalten ----------------------------------------------------------------
SPX = (430, 905, 1380)                   # Spalten (je 450 breit)
SPW = 450
RY = (300, 455, 610, 765)                # Zeilen (je 150 hoch)
RL = ("1. Wer?", "2. Wogegen?", "3. Voraussetzungen", "4. Folge")
KOPF = (("I. Vorabentscheidung", "Art. 267 AEUV", GELB), ("II. Nichtigkeitsklage", "Art. 263 AEUV", GRUEN),
        ("III. Vertragsverletzung", "Art. 258 AEUV", BLAU))


def raster(cue, titel_, kopf_cues, zeilen_cues):
    """Breite Karte mit drei Spalten (Verfahren) und vier Zeilen (Wer? Wogegen? Voraussetzungen? Folge?)."""
    els = [karte(60, 50, 1800, 920, cue), titel(glyphen(titel_), 110, 90, cue, 48)]
    for (k1, k2, f), x, c in zip(KOPF, SPX, kopf_cues):
        els.append(karte(x, 165, SPW - 20, 110, c, fill=f, rund=16, schatten=5, rand=4))
        els.append(z(k1, x + 20, 175, c, "ExtraBold", 32, rechts=x + SPW - 30))
        els.append(z(k2, x + 20, 220, c, "Bold", 30, rechts=x + SPW - 30))
    for t, y, c in zip(RL, RY, zeilen_cues):
        els.append(linienzug([(100, y - 12), (1820, y - 12)], c, breite=3, farbe=(21, 21, 21, 90)))
        els.append(z(t, 100, y + 45, c, "ExtraBold", 31, rechts=SPX[0] - 10))
    return els


def zelle(texte, sp, ze, cue, size=29):
    """Zelleninhalt (bis zu drei Zeilen) in Spalte sp, Zeile ze."""
    x, y = SPX[sp] + 10, RY[ze] + 8
    return [z(t, x, y + i * 40, cue, "Bold" if i == 0 else "Regular", size, rechts=SPX[sp] + SPW - 15)
            for i, t in enumerate(texte)]


folie([("ueber", "Überblick · Die drei wichtigsten Verfahren"),
       ("raster", "Überblick › Wer? Wogegen? Voraussetzungen? Folge?")], [
    *raster("ueber", "Die drei wichtigsten Verfahren vor dem EuGH", ("u1", "u2", "u3"),
            [beim("raster", "Wer"), beim("raster", "Wogegen"), beim("raster", "Voraussetzungen"), beim("raster", "Folge")]),
])

# D1 Wortlaut Art. 267 AEUV (auszugsweise, ABl. C 202 vom 7.6.2016, S. 164) -----------------------------------------------
W267 = [[("„Der Gerichtshof der Europäischen Union entscheidet im", 0)],
        [("Wege der Vorabentscheidung a) über die ", 0), ("Auslegung der Verträge", "a"), (",", 0)],
        [("b) über die ", 0), ("Gültigkeit und die Auslegung der Handlungen", "b")],
        [("der Organe", "b"), (", Einrichtungen oder sonstigen Stellen der Union,", 0)],
        [("Wird eine derartige Frage einem Gericht eines Mitgliedstaats", 0)],
        [("gestellt und hält dieses Gericht eine Entscheidung darüber zum", 0)],
        [("Erlass seines Urteils für erforderlich, so ", 0), ("kann", "c"), (" es diese Frage", 0)],
        [("dem Gerichtshof zur Entscheidung vorlegen. Wird eine derartige", 0)],
        [("Frage … bei einem einzelstaatlichen Gericht gestellt, dessen", 0)],
        [("Entscheidungen selbst nicht mehr mit Rechtsmitteln des", 0)],
        [("innerstaatlichen Rechts angefochten werden können, so ist", 0)],
        [("dieses Gericht zur Anrufung des Gerichtshofs ", 0), ("verpflichtet", "d"), (".“", 0)]]
P1 = "1. Vorabentscheidung"
folie([("wl267", f"{P1}, Art. 267 AEUV"), ("ausl", f"{P1} › Gegenstand: Auslegung und Gültigkeit"),
       ("abs2", f"{P1} › Vorlagerecht, Abs. 2"), ("abs3", f"{P1} › Vorlagepflicht letzter Instanz, Abs. 3")], rechts_frei([
    *tafel("wl267", "1. Vorabentscheidungsverfahren"),
    *wortlaut(110, 175, 1040, 515, "wl267", W267, 29,
              {"a": beim("ausl", "Auslegung"), "b": beim("guelt", "Gültigkeit"), "c": beim("abs2", "kann"),
               "d": beim("abs3", "muss")}, "Art. 267 Abs. 1–3 AEUV (auszugsweise)"),
    pl("Vorlagerecht", 330, 780, "abs2", fill=GRUEN, size=32, anker="m"),
    pl("Vorlagepflicht letzter Instanz", 790, 780, "abs3", fill=ROTHELL, size=32, anker="m"),
    *figur_rechts("EI", [("ruhig", "wl267"), ("denkt", "abs2"), ("ernst", "abs3")], "wl267"),
]))

# D2 Vorabentscheidung: Wer? Ausnahmen, Gültigkeit -------------------------------------------------------------------------
folie([("wer1", f"{P1} › Wer? Nur das Gericht legt vor"), ("cilf", f"{P1} › Ausnahmen nach CILFIT"),
       ("foto", f"{P1} › Ungültigkeit: immer vorlegen")], rechts_frei([
    *tafel("wer1", "Vorabentscheidung: Wer? Wann?"),
    z("Wer? Nur das Gericht legt vor", 110, 175, "wer1", "Bold", 33),
    z("für die Parteien kein Rechtsbehelf", 110, 220, beim("wer1", "Parteien"), size=31),
    fund("CILFIT, Rs. 283/81, Rn. 9; EuGH, C-561/19, Rn. 54", 110, 262, beim("wer1", "Rechtsbehelf")),
    z("EuGH: legt das Unionsrecht aus", 110, 315, "teil1", "Bold", 31),
    z("nationales Recht und Fall: allein das vorlegende Gericht", 110, 358, beim("teil1", "nationale"), size=30),
    fund("EuGH, C-561/19 (Consorzio Italian Management), Rn. 35", 110, 400, beim("teil1", "vorlegende")),
    karte(110, 455, 1040, 225, "cilf", fill=GELB if False else HELL, rund=18, schatten=6, rand=4),
    z("Keine Vorlagepflicht nach CILFIT, wenn die Frage", 135, 470, "cilf", "Bold", 31, rechts=1140),
    z("· nicht entscheidungserheblich ist,", 160, 515, beim("cilf", "entscheidungserheblich"), size=31, rechts=1140),
    z("· schon vom Gerichtshof geklärt ist (acte éclairé),", 160, 560, "acte", size=31, rechts=1140),
    z("· offenkundig ist, kein vernünftiger Zweifel (acte clair)", 160, 605, beim("acte", "offenkundig"), size=30,
      rechts=1140),
    fund("Rs. 283/81, Rn. 21; C-561/19, Rn. 33", 135, 646, beim("acte", "offenkundig")),
    fb(110, 715, 1040, 120, ROTHELL, "foto", [("Ungültig? Dann immer vorlegen –", "ExtraBold", 31, INK),
                                            ("verwerfen darf nur der Gerichtshof der EU", "ExtraBold", 31, INK)]),
    fund("Foto-Frost, Rs. 314/85, Rn. 15, 20", 110, 845, beim("foto", "Verwerfen")),
    *figur_rechts("EI", [("denkt", "wer1"), ("ruhig", "teil1"), ("staunt", "foto")], "wer1"),
]))

# D3 Folge, Art. 101 GG, Fall 1 ----------------------------------------------------------------------------------------------
folie([("bind", f"{P1} › Folge: Bindung"), ("gg", f"{P1} › Art. 101 Abs. 1 S. 2 GG"),
       ("l1", "Fall 1 · Richterin Eichhorn: Vorlagerecht")], rechts_frei([
    *tafel("bind", "Vorabentscheidung: Folge"),
    *zeile_ok("Folge: Das Urteil bindet das vorlegende Gericht", 110, 175, beim("bind", "Urteil"), stil="Bold"),
    fund("EuGH, C-173/09 (Elchinov), Rn. 29", 175, 222, beim("bind", "bindet")),
    fb(110, 280, 1040, 135, LILAHELL, "gg", [("Vorlagepflicht offensichtlich unhaltbar verletzt:", "ExtraBold", 30, INK),
                                            ("Entzug des gesetzlichen Richters", "ExtraBold", 30, INK)]),
    z("Art. 101 Abs. 1 S. 2 GG", 110, 430, beim("gg", "Artikel"), "Bold", 31),
    fund("BVerfGE 126, 286 Rn. 88 (Honeywell)", 110, 472, beim("gg", "Artikel")),
    z("Richterin Eichhorn:", 110, 545, "l1", "ExtraBold", 33),
    z("Gegen ihr Urteil gibt es noch ein Rechtsmittel.", 110, 592, beim("l1", "Gegen"), size=32),
    fund("§ 124 VwGO (Berufung nach Zulassung); EuGH, C-99/00 (Lyckeskog), Rn. 16", 110, 636, beim("l1", "Rechtsmittel")),
    *zeile_ok("Sie darf vorlegen (Abs. 2),", 110, 700, "l1b", stil="Bold"),
    *zeile_ok("muss aber nicht.", 110, 755, beim("l1b", "muss"), ja=False, stil="Bold"),
    *figur_rechts("EI", [("ernst", "bind"), ("denkt", "gg"), ("ruhig", "l1"), ("froh", "l1b")], "bind"),
]))

# E1 Nichtigkeitsklage: Wogegen? Wer? --------------------------------------------------------------------------------------
P2 = "2. Nichtigkeitsklage"
folie([("ni", f"{P2}, Art. 263 AEUV"), ("wog", f"{P2} › Wogegen? Handlungen mit Rechtswirkung"),
       ("priv", f"{P2} › Wer? Privilegierte Kläger, Abs. 2"), ("tprv", f"{P2} › Teilprivilegierte Kläger, Abs. 3"),
       ("nprv", f"{P2} › Nichtprivilegierte Kläger, Abs. 4")], rechts_frei([
    *tafel("ni", "2. Nichtigkeitsklage, Art. 263 AEUV"),
    z("Wogegen? Handlungen der Union mit Rechtswirkung", 110, 175, "wog", "Bold", 32),
    z("etwa ein Beschluss der Kommission", 110, 220, beim("wog", "Beschluss"), size=31),
    fund("Art. 263 Abs. 1 AEUV; EuGH, C-583/11 P (Inuit), Rn. 56", 110, 262, beim("wog", "Kommission")),
    karte(110, 320, 1040, 150, "priv", fill=GRUENHELL, rund=18, schatten=6, rand=4),
    z("privilegiert: Mitgliedstaaten, Parlament, Rat, Kommission", 135, 335, "priv", "Bold", 30, rechts=1140),
    z("keine eigene Betroffenheit nötig (Abs. 2)", 135, 380, beim("priv", "Sie"), size=30, rechts=1140),
    fund("EuGH, C-370/07, Rn. 16; Rs. 166/78, Rn. 5 f.", 135, 422, beim("priv", "Betroffenheit")),
    karte(110, 500, 1040, 120, "tprv", fill=BLAUHELL, rund=18, schatten=6, rand=4),
    z("teilprivilegiert: Rechnungshof, EZB, Ausschuss der Regionen", 135, 515, "tprv", "Bold", 29, rechts=1140),
    z("nur zur Wahrung ihrer Rechte (Abs. 3)", 135, 560, beim("tprv", "Wahrung"), size=30, rechts=1140),
    karte(110, 650, 1040, 110, "nprv", fill=HELL, rund=18, schatten=6, rand=4),
    z("nichtprivilegiert: natürliche und juristische", 135, 665, "nprv", "Bold", 30, rechts=1140),
    z("Personen (Abs. 4)", 135, 710, beim("nprv", "Personen"), "Bold", 30, rechts=1140),
    *figur_rechts("PF", [("ruhig", "ni"), ("denkt", "priv"), ("entschlossen", "nprv")], "ni"),
]) + [ficon("tabler", "gavel", 630, 640, 300, beim("ni", "Nichtigkeitsklage"), fuell=HOLZ, bis="wog")])

# E2 Wortlaut Art. 263 Abs. 4 AEUV (ABl. C 202 vom 7.6.2016, S. 162), Plaumann, Inuit ------------------------------------
W263 = [[("„Jede natürliche oder juristische Person kann … gegen die", 0)],
        [("an sie gerichteten", "a"), (" oder sie ", 0), ("unmittelbar und individuell", "b")],
        [("betreffenden Handlungen sowie gegen ", 0), ("Rechtsakte mit", "c")],
        [("Verordnungscharakter", "c"), (", die sie unmittelbar betreffen und", 0)],
        [("keine Durchführungsmaßnahmen", "d"), (" nach sich ziehen, Klage erheben.“", 0)]]
folie([("wl263", f"{P2} › Klageberechtigung Privater, Abs. 4"), ("plaum", f"{P2} › individuell betroffen: Plaumann"),
       ("inuit", f"{P2} › Rechtsakte mit Verordnungscharakter")], rechts_frei([
    *tafel("wl263", "Art. 263 Abs. 4 AEUV: Private"),
    *wortlaut(110, 175, 1040, 230, "wl263", W263, 30,
              {"a": beim("wl263", "gerichtete"), "b": beim("unind", "unmittelbar"), "c": beim("vochar", "Rechtsakte"),
               "d": beim("vochar", "keine")}, "Art. 263 Abs. 4 AEUV"),
    z("Plaumann-Formel: individuell betroffen nur, wen die Handlung", 110, 470, "plaum", "Bold", 29),
    z("„wegen bestimmter persönlicher Eigenschaften oder besonderer,", 110, 512, beim("plaum", "persönlicher"), size=29),
    z("ihn aus dem Kreis aller übrigen Personen heraushebender", 110, 552, beim("plaum", "Kreis"), size=29),
    z("Umstände berührt und ihn daher in ähnlicher Weise", 110, 592, beim("plaum", "individualisiert"), size=29),
    z("individualisiert wie den Adressaten“", 110, 632, beim("plaum", "individualisiert"), size=29),
    fund("EuGH, Rs. 25/62 (Plaumann), Slg. 1963, 213, 238; C-583/11 P, Rn. 72", 110, 675, beim("plaum", "Adressaten")),
    fb(110, 735, 1040, 95, GRUEN, "inuit", [("Verordnungscharakter: allgemeine Geltung, kein Gesetzgebungsakt", "ExtraBold", 28, INK)]),
    fund("EuGH, C-583/11 P (Inuit), Rn. 60 f.", 110, 838, beim("inuit", "Gesetzgebungsakte")),
    *figur_rechts("PF", [("denkt", "wl263"), ("sorge", "plaum"), ("ruhig", "inuit")], "wl263"),
]))

# E3 Frist, Gericht der EU, Folge, Fall 2 -----------------------------------------------------------------------------------
folie([("frist", f"{P2} › Frist: 2 Monate, Abs. 6"), ("eug", f"{P2} › zuständig: Gericht der EU, Art. 256"),
       ("nichtig", f"{P2} › Folge: Nichtigerklärung, Art. 264"), ("l2", "Fall 2 · Frau Pfister: Nichtigkeitsklage")],
      rechts_frei([
    *tafel("frist", "Nichtigkeitsklage: Frist, Gericht, Folge"),
    *zeile_ok("Frist: 2 Monate (Abs. 6)", 110, 175, beim("frist", "zwei"), stil="Bold"),
    *zeile_ok("Klagen Einzelner: zuerst das Gericht der EU (EuG)", 110, 240, "eug", stil="Bold", size=31),
    fund("Art. 256 Abs. 1 AEUV; Art. 51 Satzung des Gerichtshofs", 175, 285, beim("eug", "Artikel")),
    *zeile_ok("Folge: Die Handlung wird für nichtig erklärt", 110, 345, "nichtig", stil="Bold", size=31),
    fund("Art. 264 Abs. 1 AEUV", 175, 390, beim("nichtig", "Artikel")),
    karte(110, 470, 1040, 300, "l2", fill=ROTHELL, rund=18, schatten=6, rand=4),
    z("Frau Pfister:", 140, 490, "l2", "ExtraBold", 33, rechts=1140),
    *zeile_ok("Adressatin des Beschlusses (Abs. 4 Var. 1)", 140, 545, beim("l2", "Adressatin"), size=31, rechts=1140),
    *zeile_ok("auf Plaumann kommt es nicht an", 140, 605, beim("l2", "Plaumann"), size=31, rechts=1140),
    *zeile_ok("aber: Klage binnen 2 Monaten", 140, 665, "l2b", stil="Bold", size=31, rechts=1140),
    fund("Art. 263 Abs. 6 AEUV: ab Mitteilung an die Klägerin", 205, 712, beim("l2b", "Monaten")),
    *figur_rechts("PF", [("ruhig", "frist"), ("denkt", "eug"), ("froh", "l2"), ("entschlossen", "l2b")], "frist"),
]))

# F1 Wortlaut Art. 258 AEUV (ABl. C 202 vom 7.6.2016, S. 160) --------------------------------------------------------------
W258 = [[("„Hat nach Auffassung der Kommission ein Mitgliedstaat", 0)],
        [("gegen eine Verpflichtung aus den Verträgen verstoßen, so", 0)],
        [("gibt sie eine ", 0), ("mit Gründen versehene Stellungnahme", "b")],
        [("hierzu ab; sie hat dem Staat zuvor ", 0), ("Gelegenheit zur", "a")],
        [("Äußerung", "a"), (" zu geben. Kommt der Staat dieser Stellungnahme", 0)],
        [("innerhalb der von der Kommission gesetzten Frist nicht", 0)],
        [("nach, so kann die Kommission den ", 0), ("Gerichtshof der", "c")],
        [("Europäischen Union anrufen", "c"), (".“", 0)]]
P3 = "3. Vertragsverletzungsverfahren"
folie([("wl258", f"{P3}, Art. 258 AEUV"), ("stell", f"{P3} › begründete Stellungnahme"),
       ("w258b", f"{P3} › Klage der Kommission")], rechts_frei([
    *tafel("wl258", "3. Vertragsverletzungsverfahren"),
    *wortlaut(110, 175, 1040, 360, "wl258", W258, 31,
              {"a": beim("wl258", "Gelegenheit"), "b": beim("stell", "Gründen"), "c": beim("w258b", "Gerichtshof")},
              "Art. 258 AEUV"),
    pl("1. Gelegenheit zur Äußerung", 330, 640, beim("wl258", "Gelegenheit"), fill=WEISS, size=29, anker="m"),
    pl("2. Stellungnahme", 700, 640, "stell", fill=GELB, size=29, anker="m"),
    pl("3. Klage", 990, 640, "w258b", fill=BLAU, size=29, anker="m"),
    *figur_rechts("TE", [("ruhig", "wl258"), ("ernst", "w258b")], "wl258"),
]))

# F2 Vertragsverletzung: Wer, Vorverfahren, Folge, Art. 260 -----------------------------------------------------------------
folie([("wer3", f"{P3} › Wer? Wogegen?"), ("vor", f"{P3} › Voraussetzung: Vorverfahren"),
       ("fest", f"{P3} › Folge: Feststellungsurteil, Art. 260 Abs. 1"), ("zwang", f"{P3} › Art. 260 Abs. 2")],
      rechts_frei([
    *tafel("wer3", "Vertragsverletzung: Wer? Wann? Folge?"),
    z("Wer? Die Kommission (Art. 258)", 110, 175, "wer3", "Bold", 32),
    z("auch ein anderer Mitgliedstaat (Art. 259)", 110, 220, beim("wer3", "auch"), size=31),
    z("Wogegen? Verstoß eines Mitgliedstaats", 110, 280, beim("wer3", "Wogegen"), "Bold", 32),
    z("Voraussetzung: Vorverfahren", 110, 355, "vor", "ExtraBold", 32),
    karte(110, 410, 470, 110, beim("vor", "Mahnschreiben"), fill=HELL, rund=16, schatten=5, rand=4),
    z("1. Mahnschreiben", 135, 440, beim("vor", "Mahnschreiben"), "Bold", 31, rechts=570),
    pfeil(600, 465, 660, 465, beim("vor", "begründete"), breite=8, kopf=22),
    karte(680, 410, 470, 110, beim("vor", "begründete"), fill=GELB, rund=16, schatten=5, rand=4),
    z("2. begründete", 705, 422, beim("vor", "begründete"), "Bold", 31, rechts=1140),
    z("Stellungnahme", 705, 465, beim("vor", "begründete"), "Bold", 31, rechts=1140),
    fund("EuGH, C-152/98, Rn. 23 f. (Vorverfahren, Mahnschreiben)", 110, 535, beim("vor", "Stellungnahme")),
    *zeile_ok("Folge: Der Gerichtshof stellt den Verstoß fest", 110, 595, "fest", stil="Bold", size=31),
    z("Staat muss die Maßnahmen aus dem Urteil ergreifen", 175, 640, beim("fest", "Der", nr=2), size=30),
    fund("Art. 260 Abs. 1 AEUV", 175, 682, beim("fest", "Urteil")),
    fb(110, 730, 1040, 120, ROTHELL, "zwang", [("nicht befolgt: zweites Verfahren,", "ExtraBold", 30, INK),
                                              ("Pauschalbetrag oder Zwangsgeld, Art. 260 Abs. 2", "ExtraBold", 30, INK)]),
    *figur_rechts("TE", [("ernst", "wer3"), ("denkt", "vor"), ("ruhig", "fest"), ("still", "zwang")], "wer3"),
]))

# F3 Fall 3 und weitere Verfahren --------------------------------------------------------------------------------------------
folie([("l3", "Fall 3 · Herr Teichmann: Vertragsverletzungsverfahren"), ("rest", "Weitere Verfahren · Art. 265 und 340 AEUV")],
      [
    *tafel("l3", "Herr Teichmann und das deutsche Gesetz"),
    ficon("tabler", "mail", 230, 330, 110, beim("l3", "Zuerst"), fuell=WEISS),
    pl("Mahnschreiben", 230, 350, beim("l3", "Zuerst"), fill=HELL, size=28, anker="m"),
    ficon("tabler", "file-text", 520, 330, 100, beim("l3", "Vorverfahren"), d=0.3, fuell=GELB),
    pl("Stellungnahme", 520, 350, beim("l3", "Vorverfahren"), fill=GELB, size=28, anker="m", d=0.3),
    ficon("tabler", "book", 790, 330, 100, "l3b", fuell=ROT),
    pl("Gesetz bleibt?", 790, 350, "l3b", fill=ROTHELL, size=28, anker="m"),
    ficon("tabler", "building-bank", 1040, 330, 110, beim("l3b", "Kommission"), fuell=BLAU),
    pl("Klage", 1040, 350, beim("l3b", "Kommission"), fill=BLAU, size=28, anker="m"),
    z("Zuerst das Vorverfahren, dann kann die Kommission klagen.", 110, 440, beim("l3b", "Kommission"), "Bold", 30),
    karte(110, 540, 1040, 230, "rest", fill=HELL, rund=18, schatten=6, rand=4),
    z("Daneben:", 140, 560, "rest", "ExtraBold", 32, rechts=1140),
    z("· Untätigkeitsklage, Art. 265 AEUV", 165, 615, beim("rest", "Untätigkeitsklage"), "Bold", 31, rechts=1140),
    z("· Schadensersatzklage gegen die Union, Art. 340 AEUV", 165, 665, beim("rest", "Schadensersatzklage"), "Bold", 30,
      rechts=1140),
    fund("Art. 340 Abs. 2 AEUV (außervertragliche Haftung)", 190, 712, beim("rest", "dreihundertvierzig")),
    *figur_rechts("TE", [("ruhig", "l3"), ("ernst", "l3b"), ("freundlich", "rest")], "l3"),
])

# G Ergebnis: alle drei ------------------------------------------------------------------------------------------------------
folie([("erg", "Ergebnis · Drei Fälle, drei Verfahren")], [
    linienzug([(60, DB), (1860, DB)], "erg", breite=7, farbe=INK),
    pl("Ergebnis", 960, 90, "erg", fill=GELB, size=44, anker="m"),
    *figuren([("EI_ruhig_r", "erg"), ("EI_froh_r", "e1")], DX[0], DB, DH),
    namensschild("Richterin Eichhorn", DX[0], DB, "erg", FARBE["EI"], d=0.2),
    *figuren([("PF_ruhig", "erg"), ("PF_froh", "e2")], DX[1], DB, DH, d=0.1),
    namensschild("Frau Pfister", DX[1], DB, "erg", FARBE["PF"], d=0.3),
    *figuren([("TE_ruhig", "erg"), ("TE_freundlich", "e3")], DX[2], DB, DH, d=0.2),
    namensschild("Herr Teichmann", DX[2], DB, "erg", FARBE["TE"], d=0.4),
    pl("Vorabentscheidung", DX[0], 330, beim("e1", "Vorabentscheidung"), fill=GELB, size=31, anker="m"),
    z("Art. 267 AEUV", DX[0] - 105, 410, beim("e1", "Vorabentscheidung"), "Bold", 30, rechts=1900),
    ok(DX[0] + 150, 300, beim("e1", "Vorabentscheidung"), gr=22),
    pl("Nichtigkeitsklage", DX[1], 330, beim("e2", "Nichtigkeitsklage"), fill=GRUEN, size=31, anker="m"),
    z("Art. 263 AEUV", DX[1] - 105, 410, beim("e2", "Nichtigkeitsklage"), "Bold", 30, rechts=1900),
    ok(DX[1] + 150, 300, beim("e2", "Nichtigkeitsklage"), gr=22),
    pl("Vertragsverletzungsverfahren", DX[2] - 40, 330, beim("e3", "Vertragsverletzungsverfahren"), fill=BLAU, size=31,
       anker="m"),
    z("Art. 258 AEUV", DX[2] - 105, 410, beim("e3", "Vertragsverletzungsverfahren"), "Bold", 30, rechts=1900),
    ok(DX[2] + 230, 300, beim("e3", "Vertragsverletzungsverfahren"), gr=22),
])

# H Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · Die Vorlage ist keine Klage"), ("tipp3", "Klausurtipp · Nichtigkeitsklage Privater: Abs. 4")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Die Vorlage ist keine Klage.", 200, 200, "tipp", "Bold", 34),
    *zeile_ok("keine Klagebefugnis, keine Frist", 150, 265, beim("tipp", "Prüfe"), ja=False),
    z("Sondern prüfen:", 200, 345, "tipp2", "Bold", 34),
    *zeile_ok("Vorlagegegenstand", 150, 400, beim("tipp2", "Vorlagegegenstand")),
    *zeile_ok("vorlageberechtigtes Gericht", 150, 455, beim("tipp2", "vorlageberechtigtes")),
    *zeile_ok("Entscheidungserheblichkeit", 150, 510, beim("tipp2", "Entscheidungserheblichkeit")),
    fund("Art. 267 Abs. 1, 2 AEUV; CILFIT, Rn. 9 f.", 215, 560, beim("tipp2", "Entscheidungserheblichkeit")),
    fb(110, 640, 1040, 120, GRUEN, "tipp3", [("Nichtigkeitsklage Privater:", "ExtraBold", 32, INK),
                                            ("Schwerpunkt Abs. 4", "ExtraBold", 32, INK)]),
    *redet("LX_warnt", LXX, BR, FR + 60, "tipp", "sch"),
    namensschild("Lexi", LXX, BR, "tipp", GELB, d=0.2),
])

# I Klausurschema als Übersicht ----------------------------------------------------------------------------------------------
PS_ = "Klausurschema"
folie([("sch", PS_), ("r1", f"{PS_} › 1. Wer?"), ("r2", f"{PS_} › 2. Wogegen?"), ("r3", f"{PS_} › 3. Voraussetzungen"),
       ("r4", f"{PS_} › 4. Folge")], [
    *raster("sch", "Klausurschema: Verfahren vor dem EuGH", ("sch", "sch", "sch"), ("r1", "r2", "r3", "r4")),
    *zelle(["Gericht eines", "Mitgliedstaats"], 0, 0, "r1a"),
    *zelle(["Kläger: privilegiert,", "teil- oder nicht-", "privilegiert"], 1, 0, "r1b"),
    *zelle(["Kommission", "(Art. 259: Mitgliedstaat)"], 2, 0, "r1c"),
    *zelle(["Frage zum Unionsrecht:", "Auslegung, Gültigkeit"], 0, 1, "r2a"),
    *zelle(["Handlung der Union", "mit Rechtswirkung"], 1, 1, "r2b"),
    *zelle(["Verstoß eines", "Mitgliedstaats"], 2, 1, "r2c"),
    *zelle(["Entscheidungs-", "erheblichkeit; Pflicht:", "letzte Instanz"], 0, 2, "r3a"),
    *zelle(["Klageberechtigung,", "Frist 2 Monate"], 1, 2, "r3b"),
    *zelle(["Vorverfahren: Mahn-", "schreiben, begründete", "Stellungnahme"], 2, 2, "r3c"),
    *zelle(["Bindung des", "vorlegenden Gerichts"], 0, 3, "r4a"),
    *zelle(["Nichtigerklärung", "(Art. 264)"], 1, 3, "r4b"),
    *zelle(["Feststellungsurteil", "(Art. 260)"], 2, 3, "r4c"),
])

# J Merksatz (Lexi) --------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Das Gericht ", 0), ("fragt", "a"), (",", 0)],
                 [("der Betroffene ", 0), ("klagt gegen die Union", "b"), (",", 0)],
                 [("die Kommission ", 0), ("klagt gegen den Staat", "c"), (".", 0)]], 750, 330, 50, "merke",
                {"a": beim("merke", "fragt"), "b": beim("m1", "klagt"), "c": beim("m2", "klagt")}),
    *redet("LX_erklaert", 1680, 960, 690, "merke", lexi_bis_ende("merke")),
    namensschild("Lexi", 1680, 960, "merke", GELB, d=0.2),
])
