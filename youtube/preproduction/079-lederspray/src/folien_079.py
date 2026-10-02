"""Folge 079 · Lederspray-Fall: Garantenstellung & Kausalität im Vorstand – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A Sondersitzung (Produkt, Meldungen, Sitzungstisch, Abstimmung), B Sachverhalt,
C der echte Fall (BGHSt 37, 106), D Tun oder Unterlassen, E Wortlautkarte § 13 Abs. 1, F 1. Erfolg und Ursächlichkeit,
G 2. Garantenstellung (Ingerenz), H Rückrufpflicht, I Handlungspflicht des Einzelnen, J 3. Quasikausalität und Einwand,
K Wortlautkarte § 25 Abs. 2 (Mittäterschaft), L Fahrlässigkeit: Teilbeitrag, M 4. Vorsatz/Fahrlässigkeit,
N Wortlautkarte § 224 Abs. 1, O Ergebnis, P Klausurtipp (Lexi), Q Prüfschema, R Merksatz (Lexi).
Zurückhaltend: keine erkrankten Menschen, Atemnot nur als Symbol (Lunge, Warnzeichen, Klinik-Icon), Spraydose ohne Marke,
keine echte Firma. Geräusche nur bei sichtbarer Handlung: Sprühstoß, Telefonklingeln (Freesound CC0)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont

bausteine.FIGORDNER = "op_079/"
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


def tafel(cue, titel_, h=840, fill=WEISS, size=50):
    """Rechtstafel links, rechts bleibt Platz für die Figuren."""
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(glyphen(titel_), 110, 100, cue, size)]


def wortlaut(x, y, w, h, cue, zeilen, size, hl, quelle, quelle_cue=None):
    """Wortlautkarte: wörtliches Zitat (gesetze-im-internet.de, Abruf 02.10.2026) in einer hellen Karte, Fundstelle darunter
    rechts. zeilen = Liste von Token-Listen [(text, Schlüssel|0)], hl = {Schlüssel: Cue} (Hervorhebung zum gesprochenen Wort)."""
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
    """Wie fl_block, aber Zeilenabstand passend zur Schriftgröße der Zeilen (fl_block rechnet mit 64 px, mehrzeilige Blöcke
    ragten sonst über den Rand)."""
    from engine import block
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


# --- Eigene Hilfsfunktion (wie Folge 068/071): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ----------------
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
XS = 1640                               # eine Figur allein neben der Tafel
IX = 1440                               # Requisit neben der Einzelfigur
X1, X2 = 1420, 1720                     # zwei Figuren
MB = (X1 + X2) // 2
FARBE = {"EB": GRUEN, "AL": LILA, "HA": BLAU, "LL": WEISS}
NAME = {"EB": "Eberhard", "AL": "Almut", "HA": "Hauke", "LL": "Laborleiterin"}


def kette(prefix, x, folge, bis_=None, d=0.0, hoehe=FR, unten=BR):
    """Eine Figur mit Mimikfolge [(Name, Cue), …] im Zwiebelschalenprinzip (erster Auftritt pop, danach harte Schnitte)."""
    els = []
    for i, (n, c) in enumerate(folge):
        b = folge[i + 1][1] if i + 1 < len(folge) else bis_
        els.append(peep_voll(prefix + n, x, unten, hoehe, c, anim=("pop" if i == 0 else "cut"), d=(d if i == 0 else 0.0), bis=b))
    return els


def allein(p, cue, folge, x=XS):
    """Eine Figur allein rechts neben der Tafel, mit Namensschild ab dem ersten Bild der Folie."""
    return kette(p + "_", x, [(folge[0][0], cue)] + list(folge[1:])) + [namensschild(NAME[p], x, BR, cue, FARBE[p], d=0.2)]


def paar(cue, p1, f1, p2, f2):
    els = kette(p1 + "_", X1, [(f1[0][0], cue)] + list(f1[1:])) + kette(p2 + "_", X2, [(f2[0][0], cue)] + list(f2[1:]), d=0.2)
    return els + [namensschild(NAME[p1], X1, BR, cue, FARBE[p1], d=0.2), namensschild(NAME[p2], X2, BR, cue, FARBE[p2], d=0.3)]


TX = {"EB": 1370, "AL": 1585, "HA": 1780}
TH = 420


def trio(cue, eb, al, ha):
    els = []
    for p, f, d in (("EB", eb, 0.0), ("AL", al, 0.15), ("HA", ha, 0.3)):
        els += kette(p + "_", TX[p], [(f[0][0], cue)] + list(f[1:]), d=d, hoehe=TH)
        els.append(namensschild(NAME[p], TX[p], BR, cue, FARBE[p], d=0.2 + d))
    return els


# A Fall: Sondersitzung der Geschäftsführung --------------------------------------------------------------------------------
BODEN = 900
GX = {"EB": 1080, "AL": 1370, "HA": 1660}  # Geschäftsführer hinter dem Sitzungstisch (blicken nach links zur Laborleiterin)
GH = 520
LLX = 690                                  # Laborleiterin vor der Meldungstafel
TISCH_Y = 715


def gf(p, folge, rede=None):
    """Geschäftsführer hinter dem Tisch: folge = [(Mimik, Cue), …]; rede = (Cue, Bis) für die Figurenrede."""
    els = []
    for i, (n, c) in enumerate(folge):
        b = folge[i + 1][1] if i + 1 < len(folge) else None
        if rede and n == "redet":
            els += redet(f"{p}_redet", GX[p], BODEN, GH, c, b)
        else:
            els.append(peep_voll(f"{p}_{n}", GX[p], BODEN, GH, c, anim="cut", bis=b))
    return els


EBa = ("EB_redet", GX["EB"], BODEN, GH)
ALa = ("AL_redet", GX["AL"], BODEN, GH)
HAa = ("HA_redet", GX["HA"], BODEN, GH)
LLa = ("LL_redet", LLX, BODEN, GH)
folie([(NULL, "Fall · Die Schuhpflege-Firma"), ("meld", "Fall · Meldungen: Atemnot"), ("sitz", "Fall · Die Sondersitzung"),
       ("abst", "Fall · Kein Rückruf"), ("weiter", "Fall · Weitere Kunden erkranken"), ("h1", "Fall · Der Einwand von Hauke"),
       ("frage", "Fall · Die Frage")], [
    linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK),
    pl("Eine Firma für Schuhpflege", 70, 40, NULL, fill=GELB, size=36),
    # Phase 1: Produkt und Meldungen (links)
    ficon("tabler", "shoe", 200, 330, 190, NULL, fuell=HOLZ, bis="sitz"),
    szene(ficon("tabler", "spray", 420, 330, 120, "spray", fuell=BLAU, bis="sitz"), "079spray*", 1.0, versatz=0.05),
    pl("Imprägnierspray", 330, 360, "spray", fill=BLAUHELL, size=30, anker="m", bis="sitz"),
    szene(ficon("tabler", "phone-call", 160, 560, 110, "meld", fuell=WEISS, bis="sitz"), "079telefon*", 1.0, versatz=0.05),
    pl("Meldungen seit dem Herbst", 230, 470, beim("meld", "Meldungen"), fill=WEISS, size=30, bis="sitz"),
    ficon("tabler", "lungs", 190, 760, 120, beim("meld", "Atemnot"), fuell=ROTHELL, bis="sitz"),
    ficon("tabler", "alert-triangle", 330, 740, 80, beim("meld", "Atemnot"), fuell=GELB, bis="sitz"),
    pl("Atemnot", 400, 650, beim("meld", "Atemnot"), fill=ROTHELL, size=30, bis="sitz"),
    ficon("tabler", "building-hospital", 190, 880, 90, beim("meld", "Krankenhaus"), fuell=WEISS, bis="sitz"),
    pl("Krankenhaus, Intensivstation", 260, 800, beim("meld", "Krankenhaus"), fill=WEISS, size=28, bis="sitz"),
    # Phase 2: Meldungstafel und Laborleiterin
    karte(90, 470, 430, 390, "sitz", fill=WEISS, rund=18, schatten=6, rand=4),
    z("Meldungen", 130, 495, "sitz", "ExtraBold", 34, rechts=500),
    ficon("tabler", "spray", 160, 680, 80, "sitz", fuell=BLAU, anim="cut"),
    ficon("tabler", "lungs", 300, 680, 100, "sitz", fuell=ROTHELL, anim="cut"),
    ficon("tabler", "alert-triangle", 430, 670, 70, "sitz", fuell=GELB, anim="cut"),
    z("Atemnot nach dem Sprühen", 125, 720, "sitz", size=28, rechts=500),
    z("Ursache unbekannt", 125, 770, beim("l1", "Giftstoff"), "Bold", 28, rechts=500),
    peep_voll("LL_ernst", LLX, BODEN, GH, beim("sitz", "Laborleiterin"), anim="pop", bis="l1"),
    *redet("LL_redet", LLX, BODEN, GH, "l1", "e1"),
    peep_voll("LL_ernst", LLX, BODEN, GH, "e1", anim="cut"),
    namensschild("Laborleiterin", LLX, BODEN, beim("sitz", "Laborleiterin"), WEISS, d=0.2),
    blase("sprech", 700, 230, "l1", 600, 230, inhalt=["Einen Giftstoff finden wir nicht.", "Aber andere Ursachen scheiden aus."],
          textsize=30, figur=LLa, bis="e1"),
    # Sitzungstisch mit den drei Geschäftsführern (ab 0,0 s)
    *gf("EB", [("ruhig", NULL), ("redet", "e1"), ("ernst", "a1"), ("still", "frage")], rede=True),
    *gf("AL", [("ruhig", NULL), ("redet", "a1"), ("ernst", "abst"), ("still", "frage")], rede=True),
    *gf("HA", [("ruhig", NULL), ("sorge", "weiter"), ("redet", "h1"), ("zweifel", "frage")], rede=True),
    karte(860, TISCH_Y, 1000, 46, NULL, fill=HOLZ, rund=10, schatten=0, rand=5),
    karte(900, TISCH_Y + 40, 920, BODEN - TISCH_Y - 40, NULL, fill=HOLZD, rund=6, schatten=0, rand=5),
    *[namensschild(NAME[p], GX[p], TISCH_Y + 50, NULL, FARBE[p]) for p in ("EB", "AL", "HA")],
    pl("Geschäftsführung", 1360, 330, beim("sitz", "Geschäftsführern"), fill=WEISS, size=28, anker="m", bis="e1"),
    blase("sprech", 560, 190, "e1", 900, 250, inhalt=["Ein Rückruf kostet uns", "ein Vermögen."], textsize=32, figur=EBa,
          bis="a1"),
    ficon("tabler", "coins", 1238, TISCH_Y + 4, 56, beim("e1", "Vermögen"), fuell=GELB, bis="abst"),
    blase("sprech", 660, 210, "a1", 1420, 240, inhalt=["Dann bleibt das Spray im Handel.", "Wir drucken einen Warnhinweis auf."],
          textsize=30, figur=ALa, bis="abst"),
    # Abstimmung: einstimmig, kein Rückruf
    *[ficon("tabler", "thumb-up", GX[p] + 100, 420, 64, "abst", fuell=GELB, bis="frage") for p in ("EB", "AL", "HA")],
    pl("einstimmig: kein Rückruf", 1360, 170, "abst", fill=ROTHELL, size=32, anker="m", bis="h1"),
    pl("weitere Erkrankungen in Kauf genommen", 1360, 250, "vors", fill=WEISS, size=30, anker="m", bis="h1"),
    # Weitere Kunden erkranken, Dosen schon vor der Sitzung im Laden
    pl("weitere Kunden: Atemnot", 300, 160, "weiter", fill=ROTHELL, size=30, anker="m", bis="frage"),
    pl("Dosen schon vor der Sitzung im Laden", 400, 240, beim("weiter", "Dosen"), fill=WEISS, size=28, anker="m", bis="frage"),
    ficon("tabler", "building-store", 300, 420, 110, beim("weiter", "Dosen"), fuell=WEISS, bis="frage"),
    blase("sprech", 720, 230, "h1", 1310, 220, inhalt=["Meine Stimme hätte nichts geändert.", "Die anderen hätten mich überstimmt."],
          textsize=30, figur=HAa, bis="frage"),
    # Die Frage
    pl("Strafbar, obwohl sie nichts getan haben?", 960, 150, "frage", fill=WEISS, size=34, anker="m"),
    pl("Haftet auch Hauke?", 960, 240, "frage2", fill=PINK, size=34, anker="m"),
])

# B Sachverhalt ----------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    glyphen("Eine Firma stellt Pflegemittel für Schuhe her. Seit dem Herbst melden Kunden, dass sie nach dem Sprühen des "
            "Imprägniersprays Atemnot bekommen; einige kommen ins Krankenhaus, manche auf die Intensivstation. Schon vor der "
            "Sondersitzung erkranken nach den ersten Meldungen weitere Kunden; die Gefahr hätte die Geschäftsführung da "
            "bereits erkennen können."),
    glyphen("In der Sitzung berichtet die Laborleiterin: Einen Giftstoff findet das Labor nicht, andere Ursachen scheiden "
            "aus. Die 3 Geschäftsführer Eberhard, Almut und Hauke beschließen einstimmig, das Spray im Handel zu lassen und "
            "nur einen Warnhinweis aufzudrucken. Weitere Erkrankungen halten sie für möglich und nehmen sie in Kauf. Ein "
            "sofortiger Rückruf hätte die Läden rechtzeitig erreicht. In den folgenden Monaten bekommen weitere Kunden "
            "Atemnot, mit Dosen, die schon vor der Sitzung in den Läden standen. Hauke meint, seine Stimme hätte nichts "
            "geändert."),
], "Haben sich Eberhard, Almut und Hauke strafbar gemacht?")

# C Der echte Fall: BGHSt 37, 106 --------------------------------------------------------------------------------------------
folie([("bgh", "Der echte Fall · Lederspray, BGHSt 37, 106"), ("bgh4", "Der echte Fall › Verurteilungen bestätigt")], rechts_frei([
    *tafel("bgh", "Der Lederspray-Fall"),
    z("BGH, Urteil vom 6.7.1990", 110, 185, beim("bgh", "Bundesgerichtshof"), "Bold", 34),
    fund("2 StR 549/89, BGHSt 37, 106", 110, 235, beim("bgh", "Urteil")),
    z("Meldungen über Atembeschwerden", 110, 310, "bgh2", size=32),
    ok(135, 385, beim("bgh2", "einstimmig"), gr=18),
    z("Mai 1981: einstimmig kein Rückruf", 175, 365, beim("bgh2", "Mai"), "Bold", 32),
    z("Rückruf erst über 2 Jahre später", 110, 445, "bgh3", size=32),
    fund("BGHSt 37, 106, 108–110", 110, 495, "bgh3"),
    fb(110, 570, 1040, 140, GRUEN, "bgh4", [("BGH bestätigt im Kern: fahrlässige und", "ExtraBold", 32, INK),
                                                  ("gefährliche Körperverletzung", "ExtraBold", 32, INK)]),
    fund("BGHSt 37, 106, 111", 110, 725, "bgh4"),
    ficon("tabler", "building-factory-2", 1560, 420, 200, "bgh2", fuell=WEISS),
    pl("ein Hersteller", 1560, 160, "bgh2", fill=WEISS, size=30, anker="m", bis="bgh3"),
    ficon("tabler", "calendar", 1400, 760, 120, "bgh3", fuell=WEISS),
    pl("über 2 Jahre später", 1560, 160, "bgh3", fill=GELB, size=30, anker="m", anim="cut", bis="bgh4"),
    ficon("tabler", "gavel", 1720, 760, 130, "bgh4", fuell=HOLZ),
    pl("BGH bestätigt", 1560, 160, "bgh4", fill=GRUEN, size=30, anker="m", anim="cut"),
]))

# D Vorab: Tun oder Unterlassen ------------------------------------------------------------------------------------------------
PA = "A. Gefährliche Körperverletzung durch Unterlassen"
folie([("tun", "Vorab · Tun oder Unterlassen?"), ("tun2", "Vorab › Verkauf nach der Sitzung: Tun"),
       ("unterl", "Vorab › Dosen im Laden: unterlassener Rückruf"), ("unterl2", f"{PA}")], rechts_frei([
    *tafel("tun", "Vorab: Tun oder Unterlassen?"),
    karte(110, 190, 1040, 140, "tun2", fill=BLAUHELL, rund=18, schatten=6, rand=4),
    z("Verkauf nach der Sitzung:", 140, 210, "tun2", "Bold", 32),
    z("aktiv in Umlauf gebracht: Tun", 140, 262, beim("tun2", "Das"), "ExtraBold", 32),
    karte(110, 370, 1040, 140, "unterl", fill=LILAHELL, rund=18, schatten=6, rand=4),
    z("Dosen schon in den Läden:", 140, 390, "unterl", "Bold", 32),
    z("unterlassener Rückruf: Unterlassen", 140, 442, beim("unterl", "unterlassenen"), "ExtraBold", 32),
    fund("BGHSt 37, 106, 114", 140, 525, beim("unterl", "unterlassenen")),
    fb(110, 600, 1040, 90, GELB, "unterl2", [("Wir prüfen den unterlassenen Rückruf.", "ExtraBold", 32, INK)]),
    *paar("tun", "EB", [("ernst",), ("skeptisch", "unterl")], "AL", [("ruhig",), ("ernst", "tun2")]),
    pl("Tun oder Unterlassen?", MB, 160, "tun", fill=WEISS, size=28, anker="m", bis="tun2"),
    ficon("tabler", "shopping-cart", MB, 380, 110, "tun2", fuell=WEISS, bis="unterl"),
    pl("Verkauf: Tun", MB, 160, "tun2", fill=BLAUHELL, size=30, anker="m", anim="cut", bis="unterl"),
    ficon("tabler", "truck-return", MB, 380, 120, "unterl", fuell=WEISS, anim="cut"),
    pl("kein Rückruf: Unterlassen", MB, 160, "unterl", fill=LILAHELL, size=28, anker="m", anim="cut"),
]))

# E Wortlautkarte § 13 Abs. 1 ----------------------------------------------------------------------------------------------
W13 = [[("„Wer es unterläßt, ", 0), ("einen Erfolg abzuwenden", "a"), (", der zum Tatbestand", 0)],
       [("eines Strafgesetzes gehört, ist nach diesem Gesetz nur dann", 0)],
       [("strafbar, wenn er ", 0), ("rechtlich dafür einzustehen hat", "b"), (", daß der", 0)],
       [("Erfolg nicht eintritt, und wenn das Unterlassen der", 0)],
       [("Verwirklichung des gesetzlichen Tatbestandes ", 0), ("durch ein Tun", "c")],
       [("entspricht", "c"), (".“", 0)]]
folie([("p13", f"{PA} › § 13 Abs. 1 StGB"), ("einst", f"{PA} › § 13: Garantenstellung"),
       ("entspr", f"{PA} › § 13: Entsprechung")], rechts_frei([
    *tafel("p13", "Die Norm: § 13 Abs. 1 StGB"),
    *wortlaut(110, 185, 1040, 300, "p13", W13, 31,
              {"a": beim("p13", "Erfolg"), "b": "einst", "c": beim("entspr", "Tun")}, "§ 13 Abs. 1 StGB"),
    z("rechtlich einstehen müssen: Garantenstellung", 110, 570, "einst", "Bold", 32),
    z("Unterlassen entspricht einem Tun: Entsprechung", 110, 635, "entspr", "Bold", 32),
    ok(135, 720, "entspr2", gr=18),
    z("bei der Körperverletzung regelmäßig unproblematisch", 175, 700, "entspr2", size=30),
    *allein("HA", "p13", [("ernst",), ("ruhig", "entspr2")]),
    pl("§ 13 StGB", IX + 60, 160, beim("p13", "Paragraf"), fill=GELB, size=30, anker="m", bis="einst"),
    pl("Garant?", IX + 60, 160, "einst", fill=WEISS, size=30, anker="m", anim="cut", bis="entspr"),
    ficon("tabler", "shield", IX + 60, 380, 100, "einst", fuell=BLAU, bis="entspr"),
    pl("Entsprechung?", IX + 60, 160, "entspr", fill=WEISS, size=30, anker="m", anim="cut"),
    ficon("tabler", "scale", IX + 60, 380, 100, "entspr", fuell=GELB, anim="cut"),
]))

# F 1. Erfolg und Ursächlichkeit des Produkts ------------------------------------------------------------------------------
folie([("erfolg", f"{PA} › 1. Erfolg, § 223 StGB"), ("kaus", f"{PA} › 1. Ursächlichkeit des Sprays"),
       ("kaus3", f"{PA} › 1. andere Ursachen ausgeschlossen")], rechts_frei([
    *tafel("erfolg", "1. Erfolg und Ursächlichkeit"),
    ok(135, 205, beim("erfolg", "Atemnot"), gr=18),
    z("Atemnot: Gesundheitsschädigung, § 223 StGB", 175, 185, beim("erfolg", "Atemnot"), "Bold", 32),
    z("Ursache, wenn niemand weiß, welcher Stoff wirkt?", 110, 285, "kaus", "Bold", 32),
    ok(135, 365, "kaus2", gr=18),
    z("Wirkmechanismus muss man nicht kennen", 175, 345, beim("kaus2", "Den"), size=32),
    fb(110, 430, 1040, 140, GELB, "kaus3", [("Es genügt: alle anderen in Betracht", "ExtraBold", 32, INK),
                                                  ("kommenden Ursachen ausgeschlossen", "ExtraBold", 32, INK)]),
    fund("BGHSt 37, 106, 111 f. (Leitsatz 1)", 110, 585, beim("kaus3", "ausgeschlossen")),
    *allein("LL", "erfolg", [("ernst",)]),
    pl("Atemnot", IX + 40, 160, beim("erfolg", "Atemnot"), fill=ROTHELL, size=30, anker="m", bis="kaus"),
    ficon("tabler", "lungs", IX + 40, 380, 110, beim("erfolg", "Atemnot"), fuell=ROTHELL, bis="kaus"),
    pl("welcher Stoff?", IX + 40, 160, "kaus", fill=WEISS, size=30, anker="m", anim="cut", bis="kaus3"),
    ficon("tabler", "flask", IX + 40, 380, 100, "kaus", fuell=BLAUHELL, anim="cut", bis="kaus3"),
    pl("andere Ursachen: nein", IX + 40, 160, "kaus3", fill=GRUENHELL, size=28, anker="m", anim="cut"),
    ficon("tabler", "microscope", IX + 40, 380, 100, "kaus3", fuell=WEISS, anim="cut"),
]))

# G 2. Garantenstellung aus Ingerenz ---------------------------------------------------------------------------------------
folie([("garant", f"{PA} › 2. Garantenstellung: Ingerenz"), ("objektiv", f"{PA} › 2. objektiv pflichtwidrig"),
       ("zivil", f"{PA} › 2. offen: Produktbeobachtung")], rechts_frei([
    *tafel("garant", "2. Garantenstellung"),
    z("Ingerenz: pflichtwidriges Vorverhalten", 110, 185, beim("garant", "In-gerenz"), "ExtraBold", 34),
    z("gesundheitsgefährdende Produkte in Verkehr", 110, 260, "ing", size=32),
    z("gebracht: drohenden Schaden abwenden", 110, 305, beim("ing", "muss"), size=32),
    fund("BGHSt 37, 106, 114 f. (Leitsatz 2)", 110, 352, beim("ing", "abwenden")),
    ok(135, 445, "objektiv", gr=18),
    z("objektive Pflichtwidrigkeit genügt,", 175, 425, "objektiv", "Bold", 32),
    z("Verschulden nicht nötig", 175, 470, beim("objektiv", "Verschulden"), "Bold", 32),
    fund("BGHSt 37, 106, 118 f.", 175, 517, beim("objektiv", "Verschulden")),
    karte(110, 590, 1040, 120, "zivil", fill=LILAHELL, rund=18, schatten=6, rand=4),
    z("offen gelassen: genügt schon die zivilrechtliche", 140, 605, "zivil", size=30, rechts=1140),
    z("Produktbeobachtungspflicht?", 140, 650, beim("zivil", "Produktbeobachtungspflicht"), size=30, rechts=1140),
    fund("BGHSt 37, 106, 115", 140, 725, beim("zivil", "offen")),
    *allein("EB", "garant", [("ernst",), ("skeptisch", "objektiv")]),
    pl("Ingerenz", IX + 40, 160, beim("garant", "In-gerenz"), fill=LILAHELL, size=30, anker="m", bis="ing"),
    pl("in Verkehr gebracht", IX + 40, 160, "ing", fill=WEISS, size=28, anker="m", anim="cut", bis="zivil"),
    ficon("tabler", "spray", IX + 40, 380, 90, "ing", fuell=BLAU),
    pl("Zivilrecht?", IX + 40, 160, "zivil", fill=LILAHELL, size=30, anker="m", anim="cut"),
]))

# H Rückrufpflicht und Generalverantwortung ----------------------------------------------------------------------------------
folie([("rueck", f"{PA} › 2. Pflicht zum Rückruf"), ("kosten", f"{PA} › 2. Kosten treten zurück"),
       ("gesamt", f"{PA} › 2. Krise: jeder Geschäftsführer")], rechts_frei([
    *tafel("rueck", "Pflicht zum Rückruf"),
    ok(135, 205, "rueck", gr=18),
    z("aus der Garantenstellung: Rückruf", 175, 185, "rueck", "Bold", 32),
    fund("BGHSt 37, 106, 119 (Leitsatz 3)", 175, 232, beim("rueck", "Rückruf")),
    nein(135, 320, "warn", gr=18),
    z("Warnhinweis reicht nicht:", 175, 300, "warn", "Bold", 32),
    z("erreicht die Dosen in den Läden nicht", 175, 345, beim("warn", "erreicht"), size=32),
    fund("BGHSt 37, 106, 121", 175, 392, beim("warn", "erreicht")),
    z("Kosten, Ruf, Gewinn treten hier zurück", 110, 465, "kosten", "Bold", 32),
    fund("BGHSt 37, 106, 122", 110, 512, beim("kosten", "Gesundheit")),
    karte(110, 580, 1040, 140, "gesamt", fill=GRUENHELL, rund=18, schatten=6, rand=4),
    z("Krise: jeder Geschäftsführer zuständig,", 140, 600, "gesamt", "ExtraBold", 32, rechts=1140),
    z("egal wie die Ressorts verteilt sind", 140, 650, beim("gesamt", "egal"), size=32, rechts=1140),
    fund("BGHSt 37, 106, 123 f.", 140, 735, beim("gesamt", "egal")),
    *paar("rueck", "EB", [("ernst",), ("still", "kosten")], "HA", [("ruhig",), ("sorge", "gesamt")]),
    pl("Rückruf", MB, 160, "rueck", fill=WEISS, size=30, anker="m", bis="warn"),
    ficon("tabler", "truck-return", MB, 380, 120, "rueck", fuell=WEISS, bis="warn"),
    pl("Warnhinweis: zu wenig", MB, 160, "warn", fill=ROTHELL, size=28, anker="m", anim="cut", bis="kosten"),
    ficon("tabler", "alert-triangle", MB, 380, 100, "warn", fuell=GELB, anim="cut", bis="kosten"),
    pl("Gesundheit geht vor", MB, 160, "kosten", fill=GRUENHELL, size=28, anker="m", anim="cut", bis="gesamt"),
    ficon("tabler", "coins", MB, 380, 100, "kosten", fuell=GELB, anim="cut", bis="gesamt"),
    pl("alle zuständig", MB, 160, "gesamt", fill=GRUENHELL, size=30, anker="m", anim="cut"),
    ficon("tabler", "users-group", MB, 380, 120, "gesamt", fuell=BLAU, anim="cut"),
]))

# I Handlungspflicht des Einzelnen --------------------------------------------------------------------------------------------
folie([("einzel", f"{PA} › 2. Was schuldet der Einzelne?"), ("moegl", f"{PA} › 2. alles Mögliche und Zumutbare")], rechts_frei([
    *tafel("einzel", "Was schuldet der Einzelne?"),
    nein(135, 205, beim("einzel", "Allein"), gr=18),
    z("allein den Rückruf anordnen? Nein:", 175, 185, beim("einzel", "Allein"), "Bold", 32),
    z("die Geschäftsführer entscheiden gemeinsam", 175, 230, beim("einzel", "die"), size=32),
    fb(110, 320, 1040, 140, GELB, "moegl", [("alles ihm Mögliche und Zumutbare tun,", "ExtraBold", 32, INK),
                                                  ("damit ein Rückrufbeschluss zustande kommt", "ExtraBold", 32, INK)]),
    fund("BGHSt 37, 106, 125 f. (Leitsatz 4)", 110, 475, beim("moegl", "Zumutbare")),
    nein(135, 575, "keiner", gr=18),
    z("Das hat keiner der 3 getan.", 175, 555, "keiner", "Bold", 32),
    *allein("AL", "einzel", [("ernst",), ("still", "keiner")]),
    pl("allein? nein", IX + 40, 160, beim("einzel", "Allein"), fill=ROTHELL, size=30, anker="m", bis="moegl"),
    ficon("tabler", "hand-stop", IX + 40, 380, 100, beim("einzel", "Allein"), fuell=WEISS, bis="moegl"),
    pl("für den Rückruf eintreten", IX + 40, 160, "moegl", fill=GELB, size=28, anker="m", anim="cut"),
    ficon("tabler", "truck-return", IX + 40, 380, 110, "moegl", fuell=WEISS, anim="cut"),
]))

# J 3. Quasikausalität und der Einwand von Hauke ------------------------------------------------------------------------------
folie([("quasi", f"{PA} › 3. Quasikausalität"), ("einwand", f"{PA} › 3. Einwand: meine Stimme"),
       ("mitt", f"{PA} › 3. Lösung: Mittäterschaft")], rechts_frei([
    *tafel("quasi", "3. Quasikausalität"),
    z("ursächlich, wenn die gebotene Handlung", 110, 185, beim("quasi", "Ein"), "Bold", 32),
    z("den Erfolg verhindert hätte:", 110, 230, beim("quasi", "Erfolg"), "Bold", 32),
    fb(110, 290, 1040, 90, GELB, beim("quasi", "Sicherheit"),
             [("mit an Sicherheit grenzender Wahrscheinlichkeit", "ExtraBold", 32, INK)]),
    fund("BGHSt 37, 106, 126 f.", 110, 395, beim("quasi", "Sicherheit")),
    ok(135, 470, "quasi2", gr=18),
    z("sofortiger Rückruf hätte die Läden erreicht", 175, 450, "quasi2", size=32),
    z("Einwand: allein hätte er nichts geändert", 110, 545, "einwand", "Bold", 32),
    fund("BGHSt 37, 106, 128 f.", 110, 592, beim("einwand", "geändert")),
    fb(110, 650, 1040, 90, GRUEN, "mitt", [("BGH: Mittäterschaft", "ExtraBold", 32, INK)]),
    *allein("HA", "quasi", [("ernst",), ("zweifel", "einwand"), ("ernst", "mitt")]),
    pl("Rückruf hinzudenken", IX + 40, 160, "quasi", fill=WEISS, size=28, anker="m", bis="einwand"),
    ficon("tabler", "truck-return", IX + 40, 380, 110, "quasi", fuell=WEISS, bis="einwand"),
    pl("allein nichts geändert?", IX + 40, 160, "einwand", fill=ROTHELL, size=28, anker="m", anim="cut", bis="mitt"),
    ficon("tabler", "hand-stop", IX + 40, 380, 100, "einwand", fuell=WEISS, anim="cut", bis="mitt"),
    pl("Mittäterschaft", IX + 40, 160, "mitt", fill=GRUEN, size=30, anker="m", anim="cut"),
    ficon("tabler", "users-group", IX + 40, 380, 120, "mitt", fuell=BLAU, anim="cut"),
]))

# K Wortlautkarte § 25 Abs. 2: Mittäterschaft beim Unterlassen ----------------------------------------------------------------
W25 = [[("„Begehen mehrere die Straftat ", 0), ("gemeinschaftlich", "a"), (", so", 0)],
       [("wird ", 0), ("jeder als Täter", "b"), (" bestraft (Mittäter).“", 0)]]
folie([("p25", f"{PA} › 3. Mittäterschaft, § 25 Abs. 2 StGB"), ("gemein", f"{PA} › 3. Mittäterschaft beim Unterlassen"),
       ("zurech", f"{PA} › 3. Zurechnung: Unterlassen aller")], rechts_frei([
    *tafel("p25", "Mittäterschaft, § 25 Abs. 2 StGB"),
    *wortlaut(110, 185, 1040, 135, "p25", W25, 32,
              {"a": beim("p25", "gemeinschaftlich"), "b": beim("p25", "jeder")}, "§ 25 Abs. 2 StGB"),
    z("auch beim Unterlassen:", 110, 380, "gemein", "ExtraBold", 32),
    z("Garanten können die Pflicht nur gemeinsam erfüllen", 110, 430, beim("gemein", "Mehrere"), size=31),
    z("und beschließen gemeinsam, es nicht zu tun", 110, 475, beim("gemein", "beschließen"), size=31),
    fund("BGHSt 37, 106, 129 (Leitsatz 5)", 110, 522, beim("gemein", "beschließen")),
    ok(135, 610, "zurech", gr=18),
    z("jedem wird das Unterlassen aller zugerechnet", 175, 590, "zurech", "Bold", 32),
    ok(135, 675, beim("zurech", "und"), gr=18),
    z("gemeinsamer Rückruf hätte die Schäden verhindert", 175, 655, beim("zurech", "und"), size=31),
    *trio("p25", [("ernst",), ("still", "zurech")], [("ernst",), ("still", "zurech")], [("ernst",), ("still", "zurech")]),
    pl("einstimmig", 1580, 160, "gemein", fill=ROTHELL, size=30, anker="m", bis="zurech"),
    pl("jeder haftet", 1580, 160, "zurech", fill=GRUEN, size=30, anker="m", anim="cut"),
]))

# L Fahrlässigkeit: Teilbeitrag ursächlich --------------------------------------------------------------------------------------
folie([("fahr", f"{PA} › 3. bei Fahrlässigkeit: Teilbeitrag"), ("frei", f"{PA} › 3. Entlastung nur bei vollem Einsatz")],
      rechts_frei([
    *tafel("fahr", "Bei Fahrlässigkeit: Teilbeitrag", fill=LILAHELL),
    z("jeder Teilbeitrag ursächlich,", 110, 190, beim("fahr", "Teilbeitrag"), "Bold", 34),
    z("im Zusammenwirken mit den anderen", 110, 245, beim("fahr", "Zusammenwirken"), "Bold", 34),
    fund("BGHSt 37, 106, 130 f. (Leitsatz 6)", 110, 297, beim("fahr", "ursächlich")),
    fb(110, 380, 1040, 140, WEISS, "frei", [("entlastet nur, wer alles ihm Mögliche", "ExtraBold", 32, INK),
                                                   ("und Zumutbare getan hat", "ExtraBold", 32, INK)]),
    fund("BGHSt 37, 106, 131 f.", 110, 535, beim("frei", "getan")),
    *paar("fahr", "AL", [("ernst",), ("sorge", "frei")], "HA", [("ernst",), ("still", "frei")]),
    pl("Teilbeitrag", MB, 160, "fahr", fill=LILAHELL, size=30, anker="m", bis="frei"),
    ficon("tabler", "users-group", MB, 380, 120, "fahr", fuell=LILA),
    pl("voller Einsatz nötig", MB, 160, "frei", fill=WEISS, size=28, anker="m", anim="cut"),
]))

# M 4. Vorsatz und Fahrlässigkeit -----------------------------------------------------------------------------------------------
folie([("vorsatz", f"{PA} › 4. Vorsatz ab der Sitzung"), ("vorher", "Vor der Sitzung › fahrlässige Körperverletzung, § 229 StGB")],
      rechts_frei([
    *tafel("vorsatz", "4. Vorsatz oder Fahrlässigkeit?"),
    karte(110, 190, 1040, 150, "vorsatz", fill=ROTHELL, rund=18, schatten=6, rand=4),
    z("ab der Sondersitzung: Gefahr bekannt,", 140, 210, "vorsatz", "Bold", 32, rechts=1140),
    z("in Kauf genommen: bedingter Vorsatz", 140, 262, beim("vorsatz", "bedingter"), "ExtraBold", 32, rechts=1140),
    karte(110, 380, 1040, 150, "vorher", fill=BLAUHELL, rund=18, schatten=6, rand=4),
    z("vor der Sitzung erkrankt:", 140, 400, "vorher", "Bold", 32, rechts=1140),
    z("fahrlässige Körperverletzung, § 229 StGB", 140, 452, beim("vorher", "fahrlässige"), "ExtraBold", 32, rechts=1140),
    z("So trennte auch der BGH.", 110, 570, beim("vorher", "So"), "Bold", 32),
    fund("BGHSt 37, 106, 110, 132", 110, 617, beim("vorher", "So")),
    *allein("EB", "vorsatz", [("ernst",), ("still", "vorher")]),
    pl("ab der Sitzung: Vorsatz", IX + 40, 160, "vorsatz", fill=ROTHELL, size=28, anker="m", bis="vorher"),
    ficon("tabler", "calendar", IX + 40, 380, 100, "vorsatz", fuell=WEISS),
    pl("davor: § 229 StGB", IX + 40, 160, "vorher", fill=BLAUHELL, size=30, anker="m", anim="cut"),
]))

# N Wortlautkarte § 224 Abs. 1 ----------------------------------------------------------------------------------------------
W224 = [[("„(1) Wer die Körperverletzung", 0)],
        [("1. ", 0), ("durch Beibringung von Gift oder anderen", "b")],
        [("gesundheitsschädlichen Stoffen", "b"), (",", 0)],
        [("…", 0)],
        [("5. ", 0), ("mittels einer das Leben gefährdenden", "a")],
        [("Behandlung", "a")],
        [("begeht, …“", 0)]]
folie([("p224", f"{PA} › Qualifikation: § 224 Abs. 1 Nr. 5 StGB"), ("nr1", f"{PA} › nach dem Wortlaut auch Nr. 1"),
       ("rw", f"{PA} › Rechtswidrigkeit und Schuld")], rechts_frei([
    *tafel("p224", "Gefährliche Körperverletzung"),
    *wortlaut(110, 180, 1040, 330, "p224", W224, 31,
              {"a": beim("p224", "mittels"), "b": beim("nr1", "Beibringung")}, "§ 224 Abs. 1 StGB"),
    ok(135, 605, "leben", gr=18),
    z("BGH: das Leben gefährdende Behandlung", 175, 585, "leben", "Bold", 31),
    fund("BGHSt 37, 106, 132 (damals § 223a StGB)", 175, 632, "leben"),
    z("nach dem Wortlaut auch Nr. 1 in Betracht", 110, 695, "nr1", "Bold", 31),
    ok(135, 785, "rw", gr=18),
    z("keine Rechtfertigung, Rückruf zumutbar", 175, 765, "rw", "Bold", 31),
    *allein("AL", "p224", [("ernst",), ("still", "rw")]),
    pl("§ 224 Abs. 1 Nr. 5", IX + 40, 160, beim("p224", "Paragraf"), fill=GELB, size=30, anker="m", bis="nr1"),
    ficon("tabler", "lungs", IX + 40, 380, 110, beim("p224", "Paragraf"), fuell=ROTHELL, bis="rw"),
    pl("auch Nr. 1?", IX + 40, 160, "nr1", fill=WEISS, size=30, anker="m", anim="cut", bis="rw"),
    pl("zumutbar", IX + 40, 160, "rw", fill=GRUENHELL, size=30, anker="m", anim="cut"),
    ficon("tabler", "scale", IX + 40, 380, 100, "rw", fuell=GELB, anim="cut"),
]))

# O Ergebnis ------------------------------------------------------------------------------------------------------------------
folie([("erg", "Ergebnis · gefährliche Körperverletzung durch Unterlassen in Mittäterschaft"),
       ("erg2", "Ergebnis › Verkauf nach der Sitzung: Tun")], rechts_frei([
    *tafel("erg", "Ergebnis"),
    fb(110, 190, 1040, 190, GRUEN, "erg", [("Eberhard, Almut und Hauke: gefährliche", "ExtraBold", 32, INK),
                                                 ("Körperverletzung durch Unterlassen", "ExtraBold", 32, INK),
                                                 ("in Mittäterschaft", "ExtraBold", 32, INK)]),
    fund("§§ 223, 224 Abs. 1 Nr. 5, 13, 25 Abs. 2 StGB", 110, 395, beim("erg", "Mittäterschaft")),
    z("Verkauf nach der Sitzung: Haftung wegen Tuns", 110, 470, "erg2", "Bold", 32),
    *trio("erg", [("still",)], [("still",)], [("still",)]),
    ficon("tabler", "gavel", 1580, 380, 120, beim("erg", "Ergebnis"), fuell=HOLZ),
]))

# P Klausurtipp (Lexi) --------------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · Tun und Unterlassen nach den Dosen trennen"),
       ("tipp2", "Klausurtipp · Kausalität im Gremium nicht Stimme für Stimme")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Tun und Unterlassen zuerst", 200, 200, "tipp", "Bold", 36),
    z("nach den Dosen trennen", 200, 250, beim("tipp", "nach"), size=34),
    z("Kausalität im Gremium nicht", 200, 335, "tipp2", "Bold", 36),
    z("Stimme für Stimme prüfen", 200, 385, beim("tipp2", "Stimme"), size=34),
    z("Vorsatz: Mittäterschaft", 200, 470, "tipp3", "Bold", 36),
    z("Fahrlässigkeit: Zusammenwirken", 200, 525, beim("tipp3", "Fahrlässigkeit"), "Bold", 36),
    z("der Teilbeiträge", 200, 575, beim("tipp3", "Teilbeiträge"), size=34),
    *redet("LX_warnt", LXX, BR, FR + 60, "tipp", "sch"),
    namensschild("Lexi", LXX, BR, "tipp", GELB, d=0.2),
])

# Q Prüfschema -------------------------------------------------------------------------------------------------------------
K1, K2, K3 = 150, 230, 310
PS_ = "Prüfschema"
folie([("sch", PS_), ("s0", f"{PS_} › Vorab: Tun oder Unterlassen"), ("s1", f"{PS_} › I. Tatbestand"),
       ("s1a", f"{PS_} › I. 1. a) Erfolg und Ursächlichkeit"), ("s1b", f"{PS_} › I. 1. b) Garantenstellung"),
       ("s1c", f"{PS_} › I. 1. c) Nichtvornahme"), ("s1d", f"{PS_} › I. 1. d) Quasikausalität"),
       ("s1e", f"{PS_} › I. 1. e) Entsprechung"), ("s1f", f"{PS_} › I. 1. f) § 224 StGB"), ("s1g", f"{PS_} › I. 2. Vorsatz"),
       ("s2", f"{PS_} › II. Rechtswidrigkeit"), ("s3", f"{PS_} › III. Schuld")], [
    karte(60, 50, 1800, 920, "sch"),
    titel("Prüfschema: unterlassener Rückruf, §§ 223, 224, 13 StGB", 110, 90, "sch", 46),
    z("Vorab: Tun oder Unterlassen?", K1, 175, "s0", "Bold", 33, rechts=1820),
    z("I. Tatbestand", K1, 235, "s1", "Bold", 35, rechts=1820),
    z("1. objektiv:", K2, 288, beim("s1", "objektiv"), "Bold", 32, rechts=1820),
    z("a) Erfolg (§ 223) und Ursächlichkeit des Produkts", K3, 336, "s1a", size=32, rechts=1820),
    z("b) Garantenstellung aus Ingerenz", K3, 384, "s1b", size=32, rechts=1820),
    z("c) Nichtvornahme: Einsatz für den Rückruf", K3, 432, "s1c", size=32, rechts=1820),
    z("d) Quasikausalität; im Gremium: Mittäterschaft, § 25 Abs. 2", K3, 480, "s1d", size=32, rechts=1820),
    z("e) Entsprechung, § 13 Abs. 1", K3, 528, "s1e", size=32, rechts=1820),
    z("f) Qualifikation: § 224 Abs. 1 Nr. 5", K3, 576, "s1f", size=32, rechts=1820),
    z("2. subjektiv: Vorsatz (sonst § 229)", K2, 628, "s1g", "Bold", 32, rechts=1820),
    z("II. Rechtswidrigkeit", K1, 690, "s2", "Bold", 35, rechts=1820),
    z("III. Schuld", K1, 750, "s3", "Bold", 35, rechts=1820),
])

# R Merksatz (Lexi) ------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Wer gesundheitsgefährdende Produkte", 0)], [("in den Verkehr bringt, muss den Schaden", 0)],
                 [("abwenden, notfalls durch ", 0), ("Rückruf", "a"), (".", 0)]], 750, 290, 40, "merke",
                {"a": beim("merke", "Rückruf")}),
    *markertext([[("Im Gremium muss ", 0), ("jeder", "b"), (" alles ihm Mögliche", 0)],
                 [("und Zumutbare dafür tun.", 0)]], 750, 490, 40, "m2", {"b": beim("m2", "jeder")}),
    *markertext([[("Der Hinweis, die anderen hätten ohnehin", 0)], [("dagegen gestimmt, entlastet ", 0), ("nicht", "c"),
                 (".", 0)]], 750, 650, 40, "m3",
                {"c": beim("m3", "nicht")}),
    *redet("LX_erklaert", 1680, 960, 690, "merke", lexi_bis_ende("merke")),
    namensschild("Lexi", 1680, 960, "merke", GELB, d=0.2),
])
