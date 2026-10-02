"""Folge 066 · Revision Strafrecht: Sachrüge vs. Verfahrensrüge – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A In der Kanzlei (Hook, Urteil des Landgerichts), B Rückblick Hauptverhandlung (Beweisantrag,
nicht beschieden, Urteil, Strafzumessung), C Zurück in der Kanzlei (Revision, Frage), D Sachverhalt, E Revision als
Rechtsprüfung (Wortlautkarten § 337 I, II StPO), F Zulässigkeit kurz (§§ 333, 341, 345 StPO), G Zwei Rügen (Wortlautkarte
§ 344 II 1 StPO, Faustregel), H Sachrüge (allgemeine Sachrüge, Urteil aus sich heraus), I Sachrüge: Beweiswürdigung
(BGH 1 StR 52/26 Rn. 6), J Sachrüge: Strafzumessung (Wortlautkarte § 46 III StGB), K Verfahrensrüge: übergangener Zeuge
(§ 244 III 1, Wortlautkarte § 244 VI 1 StPO), L Verfahrensrüge: Vortrag (Wortlautkarte § 344 II 2 StPO, BGH 2 StR 57/25
Rn. 46, § 274 StPO), M Beruhen (Wortlautkarte BGH 3 StR 518/19 Rn. 94) und § 338 StPO, N Ergebnis (§§ 353, 354 II StPO),
O Revisionsbegründung (Klausurkonvention), P Klausurtipp (Lexi), Q Prüfschema, R Merksatz (Lexi).
Geräusch nur bei sichtbarer Handlung: das Urteil fällt auf den Kanzleischreibtisch (Szene A); Freesound CC0."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont

bausteine.FIGORDNER = "op_066/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
LILAHELL = (246, 243, 255, 255)
ROTHELL = (253, 232, 228, 255)
GRUENHELL = (232, 247, 233, 255)
BLAUHELL = (232, 240, 253, 255)
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
    for t, *_ in zeilen:
        glyphen(t)
    return fl_block(x, y, w, h, fill, cue, zeilen, **k)


def tafel(cue, titel_, h=840, fill=WEISS, size=50):
    """Rechtstafel links, rechts bleibt Platz für die Figuren."""
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(glyphen(titel_), 110, 100, cue, size)]


def wortlaut(x, y, w, h, cue, zeilen, size, hl, quelle, quelle_cue=None):
    """Wortlautkarte: wörtliches Zitat (gesetze-im-internet.de bzw. amtlicher Volltext, Abruf 02.10.2026) in einer hellen
    Karte, Fundstelle darunter rechts. zeilen = Liste von Token-Listen [(text, Schlüssel|0)], hl = {Schlüssel: Cue}
    (Hervorhebung synchron zum gesprochenen Wort)."""
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


def hart(e):
    e.anim = "cut"
    return e


# --- Eigene Hilfsfunktion (wie Folge 054/060): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ---------------
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


BODEN, FH = 880, 480
BR, FR = 930, 480                       # Figuren rechts neben der Tafel
X1, X2 = 1390, 1730                     # zwei Figuren neben der Tafel
MB = (X1 + X2) // 2
XS = 1600                               # eine Figur allein neben der Tafel

# A Fall: in der Kanzlei --------------------------------------------------------------------------------------------------
BX, LX = 400, 1520                      # Herr Brockmann (links, blickt nach rechts), Rechtsanwältin Lenz (rechts)
BRa = ("BR_redet_r", BX, BODEN, FH)
urteil = szene(bewegt(ficon("tabler", "file-text", 1150, 640, 110, "lg", fuell=WEISS), "lg", ("lg", 0.35), 0, -260),
               "066urteil*", 1.0, versatz=0.30)


def kanzlei(cue):
    """Kanzlei: Bodenlinie, Schreibtisch, Bücher (gleicher Schauplatz in A und C)."""
    return [hart(linienzug([(60, BODEN), (1860, BODEN)], cue, breite=7, farbe=INK)),
            ficon("tabler", "desk", 960, BODEN - 2, 460, cue, fuell=HOLZ, anim="cut"),
            ficon("tabler", "books", 820, 640, 90, cue, fuell=BLAU, anim="cut"),
            ficon("tabler", "briefcase", 1700, BODEN - 2, 120, cue, fuell=DUNKEL, anim="cut")]


folie([(NULL, "Fall · In der Kanzlei"), ("lg", "Fall · Das Urteil des Landgerichts")], [
    *kanzlei(NULL),
    pl("In einer Anwaltskanzlei", 70, 40, NULL, fill=GELB, size=40),
    pl("3 Tage nach dem Urteil", 960, 160, beim("fall", "drei"), fill=WEISS, size=30, anker="m", bis="b1"),
    peep_voll("BR_ruhig_r", BX, BODEN, FH, NULL, bis="b1"),
    *redet("BR_redet_r", BX, BODEN, FH, "b1", "lg"),
    peep_voll("BR_sorge_r", BX, BODEN, FH, "lg", anim="cut"),
    namensschild("Herr Brockmann", BX, BODEN, NULL, BLAU),
    pl("Mandant", BX, 330, beim("mandant", "Herr"), fill=WEISS, size=28, anker="m", bis="b1"),
    peep_voll("LZ_ruhig", LX, BODEN, FH, NULL, bis="lg"),
    peep_voll("LZ_denkt", LX, BODEN, FH, "lg", anim="cut"),
    namensschild("Rechtsanwältin Lenz", LX, BODEN, NULL, LILA),
    pl("Verteidigerin", LX, 330, beim("mandant", "Verteidigerin"), fill=LILA, size=28, anker="m", bis="lg"),
    blase("sprech", 820, 230, "b1", 830, 250, inhalt=["Der Richter hat meinen Zeugen nicht gehört.",
                                                     "Und das Urteil ist sowieso falsch."],
          textsize=32, figur=BRa, bis="lg"),
    urteil,
    karte(620, 150, 690, 360, beim("lg", "verurteilt"), fill=HELL, rund=10, schatten=6),
    z("Urteil des Landgerichts", 660, 175, beim("lg", "verurteilt"), "ExtraBold", 36, rechts=1290),
    ficon("tabler", "building-bank", 690, 312, 54, beim("lg", "verurteilt"), fuell=BLAU),
    z("verurteilt wegen Diebstahls", 735, 265, beim("lg", "verurteilt"), "Bold", 32, rechts=1290),
    ficon("tabler", "building-warehouse", 690, 402, 54, beim("lager", "vierzig"), fuell=GELB),
    z("im Lager: 40 Laptops fehlen", 735, 355, beim("lager", "vierzig"), "Bold", 32, rechts=1290),
    ficon("tabler", "id-badge-2", 690, 492, 54, beim("chip", "zweiundzwanzig"), fuell=GRUEN),
    z("Transponder: Lagertür 22:10 Uhr", 735, 445, beim("chip", "zweiundzwanzig"), "Bold", 32, rechts=1290),
])

# B Rückblick: die Hauptverhandlung -----------------------------------------------------------------------------------------
SX, TX, BXb, LXb, RX = 170, 370, 640, 1000, 1610   # Stoll, Saaltür, Brockmann, Lenz, Richter (hinter dem Richtertisch)
LZb = ("LZ_redet_r", LXb, BODEN, FH)
RIb = ("RI_redet", RX, BODEN, FH)
folie([("saal", "Fall · Rückblick: die Hauptverhandlung"), ("antrag", "Fall · Der Beweisantrag"),
       ("nichts", "Fall · Keine Entscheidung über den Antrag"), ("r1", "Fall · Das Urteil"),
       ("gruende", "Fall · Die Urteilsgründe")], [
    hart(linienzug([(60, BODEN), (1860, BODEN)], "saal", breite=7, farbe=INK)),
    pl("Rückblick: die Hauptverhandlung", 70, 40, "saal", fill=BLAU, size=40, anim="cut"),
    ficon("tabler", "door", TX, BODEN - 2, 150, "saal", fuell=HOLZ, anim="cut"),
    peep_voll("RI_ruhig", RX, BODEN, FH, "saal", anim="cut", bis="nichts"),
    peep_voll("RI_streng", RX, BODEN, FH, "nichts", anim="cut", bis="r1"),
    *redet("RI_redet", RX, BODEN, FH, "r1", "gruende"),
    peep_voll("RI_ruhig", RX, BODEN, FH, "gruende", anim="cut"),
    ficon("tabler", "desk", RX, BODEN - 2, 440, "saal", fuell=HOLZ, anim="cut"),
    namensschild("Vorsitzender Richter", RX, BODEN, "saal", WEISS),
    peep_voll("BR_ruhig_r", BXb, BODEN, FH, "saal", anim="cut", bis="r1"),
    peep_voll("BR_schreck_r", BXb, BODEN, FH, "r1", anim="cut", bis="gruende"),
    peep_voll("BR_sorge_r", BXb, BODEN, FH, "gruende", anim="cut"),
    namensschild("Herr Brockmann", BXb, BODEN, "saal", BLAU),
    peep_voll("LZ_ruhig_r", LXb, BODEN, FH, "saal", anim="cut", bis="l1"),
    *redet("LZ_redet_r", LXb, BODEN, FH, "l1", "stoll"),
    peep_voll("LZ_ruhig_r", LXb, BODEN, FH, "stoll", anim="cut", bis="nichts"),
    peep_voll("LZ_sorge_r", LXb, BODEN, FH, "nichts", anim="cut"),
    namensschild("Rechtsanwältin Lenz", LXb, BODEN, "saal", LILA),
    pl("Beweisantrag", LXb, 330, beim("antrag", "Beweisantrag"), fill=GELB, size=30, anker="m", bis="l1"),
    blase("sprech", 980, 270, "l1", 1190, 195,
          inhalt=["Ich beantrage, Herrn Stoll als Zeugen dafür", "zu vernehmen, dass Herr Brockmann am Tatabend",
                  "von 21 bis 23 Uhr mit ihm beim", "Fußballtraining war."],
          textsize=30, figur=LZb, bis="stoll"),
    # Herr Stoll wartet vor dem Saal (links der Tür)
    peep_voll("ST_wartet_r", SX, BODEN, FH, "stoll", anim="fade", bis="r1"),
    peep_voll("ST_sorge_r", SX, BODEN, FH, "r1", anim="cut"),
    namensschild("Herr Stoll", SX, BODEN, "stoll", GRUEN),
    pl("wartet vor dem Saal", SX + 40, 330, beim("stoll", "wartet"), fill=WEISS, size=28, anker="m"),
    pl("keine Entscheidung über den Antrag", 1110, 150, "nichts", fill=ROTHELL, size=30, anker="m", bis="r1"),
    pl("Beweisaufnahme geschlossen", 1110, 235, "schluss", fill=WEISS, size=30, anker="m", bis="r1"),
    blase("sprech", 780, 250, "r1", 1170, 220,
          inhalt=["Der Angeklagte wird wegen Diebstahls", "zu einer Freiheitsstrafe von 1 Jahr", "und 6 Monaten verurteilt."],
          textsize=30, figur=RIb, bis="gruende"),
    ficon("tabler", "file-text", 1110, 225, 90, "gruende", fuell=WEISS),
    pl("Urteilsgründe: strafschärfend", 1110, 240, "gruende", fill=WEISS, size=28, anker="m"),
    pl("„über fremdes Eigentum hinweggesetzt“", 1110, 305, beim("schaerf", "fremdes"), fill=PINK, size=28, anker="m"),
])

# C Zurück in der Kanzlei ------------------------------------------------------------------------------------------------
LZc = ("LZ_redet", LX, BODEN, FH)
folie([("l2", "Fall · Die Revision"), ("frage", "Fall · Die Frage")], [
    *kanzlei("l2"),
    pl("Zurück in der Kanzlei", 70, 40, "l2", fill=GELB, size=40, anim="cut"),
    peep_voll("BR_denkt_r", BX, BODEN, FH, "l2", anim="cut", bis="frage2"),
    peep_voll("BR_sorge_r", BX, BODEN, FH, "frage2", anim="cut"),
    namensschild("Herr Brockmann", BX, BODEN, "l2", BLAU, anim="cut"),
    *redet("LZ_redet", LX, BODEN, FH, "l2", "frage"),
    peep_voll("LZ_froh", LX, BODEN, FH, "frage", anim="cut", bis="frage2"),
    peep_voll("LZ_denkt", LX, BODEN, FH, "frage2", anim="cut"),
    namensschild("Rechtsanwältin Lenz", LX, BODEN, "l2", LILA, anim="cut"),
    blase("sprech", 640, 170, "l2", 1080, 250, inhalt=["Dagegen legen wir Revision ein."], textsize=34, figur=LZc,
          bis="frage"),
    ficon("tabler", "file-text", 1150, 640, 110, "l2", fuell=WEISS, anim="cut"),
    pl("Was kann er rügen?", 960, 160, "frage", fill=WEISS, size=34, anker="m"),
    pl("Sachrüge", 740, 260, beim("frage2", "Sachrüge"), fill=GRUEN, size=34, anker="m"),
    pl("oder", 925, 266, beim("frage2", "oder"), fill=WEISS, size=28, anker="m"),
    pl("Verfahrensrüge?", 1170, 260, beim("frage2", "Verfahrensrüge"), fill=BLAU, size=34, anker="m"),
])

# D Sachverhalt -------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    glyphen("Die Strafkammer des Landgerichts verurteilt Herrn Brockmann im ersten Rechtszug wegen Diebstahls zu einer "
            "Freiheitsstrafe von 1 Jahr und 6 Monaten. Aus dem Lager seines Arbeitgebers fehlten 40 Laptops; sein "
            "Transponder hatte die Lagertür am Tatabend um 22:10 Uhr geöffnet. Darauf stützt die Kammer ihre Überzeugung."),
    glyphen("In der Hauptverhandlung beantragte Rechtsanwältin Lenz, Herrn Stoll als Zeugen dafür zu vernehmen, dass Herr "
            "Brockmann am Tatabend von 21 bis 23 Uhr mit ihm beim Fußballtraining war. Das Gericht entschied über den Antrag "
            "nicht und verkündete das Urteil; das Protokoll verzeichnet den Antrag, aber keinen Beschluss. Strafschärfend "
            "wertete die Kammer, dass er sich über fremdes Eigentum hinweggesetzt habe."),
], "Was kann er mit der Revision rügen – und wie?")

# E Revision als Rechtsprüfung: § 337 StPO -----------------------------------------------------------------------------------
PR = "Revision"
folie([("recht", f"{PR} · reine Rechtsprüfung"), ("p337", f"{PR} › Gesetzesverletzung, § 337 Abs. 1 StPO"),
       ("p337b", f"{PR} › Begriff, § 337 Abs. 2 StPO"), ("keinez", f"{PR} › keine neue Tatsachenprüfung")], rechts_frei([
    *tafel("recht", "Revision: § 337 StPO"),
    z("keine zweite Tatsacheninstanz", 110, 180, beim("recht", "keine"), "Bold", 34),
    *wortlaut(110, 245, 1040, 110, "p337", [
        [("„Die Revision kann ", 0), ("nur", "n"), (" darauf gestützt werden, daß das", 0)],
        [("Urteil auf einer ", 0), ("Verletzung des Gesetzes", "v"), (" ", 0), ("beruhe", "b"), (".“", 0)],
    ], 30, {"n": beim("p337", "nur"), "v": beim("p337", "Verletzung"), "b": beim("p337", "beruhe")}, "§ 337 Abs. 1 StPO"),
    *wortlaut(110, 425, 1040, 110, "p337b", [
        [("„Das Gesetz ist verletzt, wenn eine Rechtsnorm nicht", 0)],
        [("oder ", 0), ("nicht richtig", "r"), (" angewendet worden ist.“", 0)],
    ], 30, {"r": beim("p337b", "richtig")}, "§ 337 Abs. 2 StPO"),
    fb(110, 615, 1040, 120, GELB, "keinez", [("keine Zeugen zur Tat,", "ExtraBold", 34, INK),
                                            ("keine neue Würdigung der Beweise", "ExtraBold", 34, INK)]),
    peep_voll("BR_ruhig", X2, BR, FR, "recht", bis="keinez"),
    peep_voll("BR_sorge", X2, BR, FR, "keinez", anim="cut"),
    peep_voll("LZ_ruhig", X1, BR, FR, "recht", d=0.2, bis="p337b"),
    peep_voll("LZ_denkt", X1, BR, FR, "p337b", anim="cut"),
    namensschild("Herr Brockmann", X2, BR, "recht", BLAU, d=0.2),
    namensschild("Rechtsanwältin Lenz", X1, BR, "recht", LILA, d=0.3),
    ficon("tabler", "scale", MB, 380, 110, "recht", fuell=GELB, bis="keinez"),
    pl("Rechtsprüfung", MB, 160, "recht", fill=GELB, size=30, anker="m", bis="p337b"),
    pl("nur Rechtsfehler", MB, 160, "p337b", fill=WEISS, size=30, anker="m", anim="cut", bis="keinez"),
    ficon("tabler", "ear-off", MB, 380, 100, "keinez", fuell=WEISS, anim="cut"),
    pl("keine neue Beweisaufnahme", MB, 160, "keinez", fill=ROTHELL, size=28, anker="m", anim="cut"),
]))

# F Zulässigkeit (kurz) --------------------------------------------------------------------------------------------------------
PZ = "Zulässigkeit"
folie([("statt", f"{PZ} › Statthaftigkeit, § 333 StPO"), ("frist1", f"{PZ} › Einlegung: 1 Woche, § 341 StPO"),
       ("frist2", f"{PZ} › Begründung: 1 Monat, § 345 Abs. 1 StPO"), ("form", f"{PZ} › Form, § 345 Abs. 2 StPO")],
      rechts_frei([
    *tafel("statt", "Zulässigkeit, kurz"),
    z("Statthaft: Urteile des Landgerichts und", 110, 185, "statt", "Bold", 32),
    z("erstinstanzliche Urteile des OLG, § 333 StPO", 110, 230, beim("statt", "erstinstanzliche"), size=32),
    z("hier: Bundesgerichtshof, § 135 Abs. 1 GVG", 110, 285, "bgh", size=30, farbe=TEXT),
    z("Einlegung: 1 Woche nach Verkündung,", 110, 370, "frist1", "Bold", 32),
    z("beim Landgericht, § 341 Abs. 1 StPO", 110, 415, beim("frist1", "Landgericht"), size=32),
    z("Begründung: 1 Monat nach Ablauf der Woche,", 110, 500, "frist2", "Bold", 32),
    z("meist ab Zustellung des Urteils, § 345 Abs. 1 StPO", 110, 545, beim("frist2", "Zustellung"), size=32),
    z("Form: Unterschrift Verteidiger oder Rechtsanwalt,", 110, 630, "form", "Bold", 32),
    z("sonst Protokoll der Geschäftsstelle, § 345 Abs. 2 StPO", 110, 675, beim("form", "Protokoll"), size=30),
    peep_voll("LZ_ruhig", X1, BR, FR, "statt", bis="form"),
    peep_voll("LZ_froh", X1, BR, FR, "form", anim="cut"),
    peep_voll("BR_ruhig", X2, BR, FR, "statt", d=0.2, bis="frist1"),
    peep_voll("BR_denkt", X2, BR, FR, "frist1", anim="cut"),
    namensschild("Rechtsanwältin Lenz", X1, BR, "statt", LILA, d=0.2),
    namensschild("Herr Brockmann", X2, BR, "statt", BLAU, d=0.3),
    ficon("tabler", "building-bank", MB, 380, 110, "statt", fuell=BLAU, bis="frist1"),
    pl("Landgericht", MB, 160, "statt", fill=WEISS, size=30, anker="m", bis="bgh"),
    pl("BGH", MB, 160, "bgh", fill=BLAU, size=30, anker="m", anim="cut", bis="frist1"),
    ficon("tabler", "calendar-event", MB, 380, 100, "frist1", fuell=GELB, anim="cut", bis="frist2"),
    pl("1 Woche", MB, 160, "frist1", fill=GELB, size=30, anker="m", anim="cut", bis="frist2"),
    ficon("tabler", "calendar-time", MB, 380, 100, "frist2", fuell=GRUEN, anim="cut", bis="form"),
    pl("1 Monat", MB, 160, "frist2", fill=GRUEN, size=30, anker="m", anim="cut", bis="form"),
    ficon("tabler", "signature", MB, 380, 110, "form", fuell=WEISS, anim="cut"),
    pl("Unterschrift", MB, 160, "form", fill=WEISS, size=30, anker="m", anim="cut"),
]))

# G Zwei Rügen: § 344 II 1 StPO -------------------------------------------------------------------------------------------------
PG = "Zwei Rügen"
folie([("p344", f"{PG} › § 344 Abs. 2 Satz 1 StPO"), ("zwei", f"{PG} › Verfahrensrüge und Sachrüge"),
       ("test", f"{PG} › Faustregel: Wo steht der Fehler?")], rechts_frei([
    *tafel("p344", "Zwei Rügen: § 344 Abs. 2 StPO", size=46),
    *wortlaut(110, 180, 1040, 150, "p344", [
        [("„Aus der Begründung muß hervorgehen, ob das Urteil", 0)],
        [("wegen Verletzung einer Rechtsnorm ", 0), ("über das Verfahren", "v")],
        [("oder wegen Verletzung einer ", 0), ("anderen Rechtsnorm", "a"), (" angefochten wird.“", 0)],
    ], 30, {"v": beim("p344", "Verfahren"), "a": beim("p344", "andere")}, "§ 344 Abs. 2 S. 1 StPO"),
    fb(110, 400, 500, 110, BLAU, beim("zwei", "Verfahrensrüge"), [("Verfahrensrüge", "ExtraBold", 38, INK)]),
    fb(650, 400, 500, 110, GRUEN, beim("zwei", "Sachrüge"), [("Sachrüge", "ExtraBold", 38, INK)]),
    z("Faustregel: Wo steht der Fehler?", 110, 560, "test", "ExtraBold", 34),
    z("im Urteil selbst: Sachrüge", 150, 620, beim("test", "Steht"), "Bold", 32),
    z("auf dem Weg zum Urteil, in der", 150, 690, "test2", "Bold", 32),
    z("Hauptverhandlung: Verfahrensrüge", 150, 735, beim("test2", "Hauptverhandlung"), "Bold", 32),
    peep_voll("LZ_ruhig", X1, BR, FR, "p344", bis="test"),
    peep_voll("LZ_froh", X1, BR, FR, "test", anim="cut"),
    peep_voll("BR_denkt", X2, BR, FR, "p344", d=0.2, bis="test2"),
    peep_voll("BR_ruhig", X2, BR, FR, "test2", anim="cut"),
    namensschild("Rechtsanwältin Lenz", X1, BR, "p344", LILA, d=0.2),
    namensschild("Herr Brockmann", X2, BR, "p344", BLAU, d=0.3),
    ficon("tabler", "list-check", MB, 380, 100, "p344", fuell=WEISS, bis="test"),
    pl("2 Rügen", MB, 160, beim("zwei", "Verfahrensrüge"), fill=WEISS, size=30, anker="m", bis="test"),
    ficon("tabler", "file-text", MB, 380, 100, beim("test", "Steht"), fuell=GRUEN, anim="cut", bis="test2"),
    pl("im Urteil", MB, 160, beim("test", "Steht"), fill=GRUEN, size=30, anker="m", anim="cut", bis="test2"),
    ficon("tabler", "building-bank", MB, 380, 110, "test2", fuell=BLAU, anim="cut"),
    pl("Hauptverhandlung", MB, 160, "test2", fill=BLAU, size=30, anker="m", anim="cut"),
]))

# H Sachrüge -------------------------------------------------------------------------------------------------------------------
PS_ = "Sachrüge"
folie([("sach", PS_), ("allg", f"{PS_} › allgemeine Sachrüge genügt"), ("aussich", f"{PS_} › Urteil aus sich heraus"),
       ("felder", f"{PS_} › Schuldspruch und Strafzumessung")], rechts_frei([
    *tafel("sach", "Sachrüge"),
    fb(110, 180, 1040, 110, GELB, "allg", [("„Ich rüge die Verletzung materiellen Rechts.“", "ExtraBold", 34, INK)]),
    z("genügt: § 344 Abs. 2 S. 1, § 352 Abs. 2 StPO;", 110, 305, beim("allg", "Ich"), size=26, farbe=TEXT),
    z("vgl. BGH, Beschl. v. 4.8.2026 – 6 StR 157/26, Rn. 1", 110, 340, beim("allg", "Ich"), size=26, farbe=TEXT),
    z("Prüfung des Urteils aus sich heraus:", 110, 420, "aussich", "ExtraBold", 34),
    z("allein anhand der Urteilsgründe", 150, 472, beim("aussich", "allein"), "Bold", 32),
    z("Trägt die Subsumtion den Schuldspruch?", 150, 560, "felder", size=32),
    z("Ist die Strafzumessung rechtsfehlerfrei?", 150, 610, beim("felder", "ist"), size=32),
    peep_voll("LZ_ruhig", X1, BR, FR, "sach", bis="allg"),
    peep_voll("LZ_froh", X1, BR, FR, "allg", anim="cut", bis="felder"),
    peep_voll("LZ_denkt", X1, BR, FR, "felder", anim="cut"),
    peep_voll("BR_ruhig", X2, BR, FR, "sach", d=0.2, bis="aussich"),
    peep_voll("BR_denkt", X2, BR, FR, "aussich", anim="cut"),
    namensschild("Rechtsanwältin Lenz", X1, BR, "sach", LILA, d=0.2),
    namensschild("Herr Brockmann", X2, BR, "sach", BLAU, d=0.3),
    ficon("tabler", "file-text", MB, 380, 100, "sach", fuell=GRUEN, bis="felder"),
    pl("Sachrüge", MB, 160, "sach", fill=GRUEN, size=30, anker="m", bis="allg"),
    pl("1 Satz genügt", MB, 160, "allg", fill=GELB, size=30, anker="m", anim="cut", bis="aussich"),
    pl("nur das Urteil", MB, 160, "aussich", fill=WEISS, size=30, anker="m", anim="cut", bis="felder"),
    ficon("tabler", "checklist", MB, 380, 100, "felder", fuell=WEISS, anim="cut"),
    pl("Schuldspruch? Strafmaß?", MB, 160, "felder", fill=WEISS, size=28, anker="m", anim="cut"),
]))

# I Sachrüge: Beweiswürdigung --------------------------------------------------------------------------------------------------
folie([("bw", f"{PS_} › Beweiswürdigung"), ("bw2", f"{PS_} › Beweiswürdigung: nur Rechtsfehler"),
       ("chip2", f"{PS_} › hier: schlüssig"), ("falsch", f"{PS_} › „Urteil falsch“ reicht nicht")], rechts_frei([
    *tafel("bw", "Sachrüge: Beweiswürdigung", size=46),
    z("Beweiswürdigung: Sache des Landgerichts", 110, 180, "bw", "ExtraBold", 34),
    *wortlaut(110, 245, 1040, 150, "bw2", [
        [("„… wenn die Beweiswürdigung ", 0), ("widersprüchlich", "w"), (", ", 0), ("unklar", "u"), (" oder", 0)],
        [("lückenhaft", "l"), (" ist oder gegen ein ", 0), ("Denkgesetz", "d"), (" oder einen gesicherten", 0)],
        [("Erfahrungssatz verstößt …“", 0)],
    ], 30, {"w": beim("bw2", "widersprüchlich"), "u": beim("bw2", "unklar"), "l": beim("bw2", "lückenhaft"),
            "d": beim("bw2", "Denkgesetze")}, "BGH, Beschl. v. 13.4.2026 – 1 StR 52/26, Rn. 6"),
    ok(135, 500, "chip2", gr=20),
    z("hier: schlüssig auf den Transponder gestützt", 175, 480, "chip2", "Bold", 32),
    nein(135, 575, beim("falsch", "reicht"), gr=20),
    z("„Das Urteil ist falsch“ allein reicht nicht", 175, 555, "falsch", "Bold", 32),
    z("vgl. BGH, Urt. v. 25.3.2026 – 2 StR 111/25, Rn. 57", 175, 610, beim("falsch", "reicht"), size=26, farbe=TEXT),
    peep_voll("BR_ruhig", X2, BR, FR, "bw", bis="falsch"),
    peep_voll("BR_aerger", X2, BR, FR, "falsch", anim="cut", bis=beim("falsch", "reicht")),
    peep_voll("BR_sorge", X2, BR, FR, beim("falsch", "reicht"), anim="cut"),
    peep_voll("RI_ruhig", X1, BR, FR, "bw", d=0.2, bis="chip2"),
    peep_voll("RI_streng", X1, BR, FR, "chip2", anim="cut"),
    namensschild("Herr Brockmann", X2, BR, "bw", BLAU, d=0.2),
    namensschild("Vorsitzender Richter", X1, BR, "bw", WEISS, d=0.3),
    ficon("tabler", "scale", MB, 380, 110, "bw", fuell=GELB, bis="chip2"),
    pl("Sache des Landgerichts", MB, 160, "bw", fill=WEISS, size=28, anker="m", bis="bw2"),
    pl("nur Rechtsfehler", MB, 160, "bw2", fill=GELB, size=30, anker="m", anim="cut", bis="chip2"),
    ficon("tabler", "id-badge-2", MB, 380, 100, "chip2", fuell=GRUEN, anim="cut"),
    pl("Transponder 22:10 Uhr", MB, 160, "chip2", fill=GRUEN, size=28, anker="m", anim="cut", bis="falsch"),
    pl("reicht nicht", MB, 160, beim("falsch", "reicht"), fill=ROTHELL, size=30, anker="m", anim="cut"),
]))

# J Sachrüge: Strafzumessung, § 46 III StGB --------------------------------------------------------------------------------------
folie([("strafz", f"{PS_} › Strafzumessung"), ("p46", f"{PS_} › Doppelverwertungsverbot, § 46 Abs. 3 StGB"),
       ("doppel2", f"{PS_} › greift beim Strafmaß")], rechts_frei([
    *tafel("strafz", "Sachrüge: Strafzumessung", size=46),
    *wortlaut(110, 180, 1040, 110, "p46", [
        [("„Umstände, die schon ", 0), ("Merkmale des gesetzlichen", "m")],
        [("Tatbestandes", "m2"), (" sind, dürfen ", 0), ("nicht berücksichtigt", "n"), (" werden.“", 0)],
    ], 30, {"m": beim("p46", "Merkmale"), "m2": beim("p46", "Merkmale"), "n": beim("p46", "nicht")}, "§ 46 Abs. 3 StGB"),
    z("Urteil: „über fremdes Eigentum hinweggesetzt“", 110, 360, "doppel", "Bold", 32),
    z("Das gehört zu jedem Diebstahl, § 242 StGB.", 110, 410, beim("doppel", "gehört"), "Bold", 32),
    nein(135, 505, "doppel2", gr=20),
    z("doppelt verwertet: Verstoß gegen § 46 Abs. 3 StGB", 175, 485, "doppel2", "Bold", 32),
    fb(110, 570, 1040, 110, GRUEN, beim("doppel2", "Insoweit"), [("Sachrüge greift beim Strafmaß", "ExtraBold", 34, INK)]),
    z("vgl. BGH, Beschl. v. 12.5.2011 – 3 StR 82/11, Rn. 3;", 110, 700, beim("doppel2", "Insoweit"), size=26, farbe=TEXT),
    z("BGH, Beschl. v. 6.5.2026 – 2 StR 118/26, Rn. 6", 110, 735, beim("doppel2", "Insoweit"), size=26, farbe=TEXT),
    peep_voll("BR_ruhig", X2, BR, FR, "strafz", bis="doppel2"),
    peep_voll("BR_froh", X2, BR, FR, beim("doppel2", "Insoweit"), anim="cut"),
    peep_voll("BR_denkt", X2, BR, FR, "doppel2", anim="cut", bis=beim("doppel2", "Insoweit")),
    peep_voll("RI_ruhig", X1, BR, FR, "strafz", d=0.2, bis="doppel2"),
    peep_voll("RI_denkt", X1, BR, FR, "doppel2", anim="cut"),
    namensschild("Herr Brockmann", X2, BR, "strafz", BLAU, d=0.2),
    namensschild("Vorsitzender Richter", X1, BR, "strafz", WEISS, d=0.3),
    ficon("tabler", "scale", MB, 380, 110, "strafz", fuell=GELB, bis="doppel2"),
    pl("Strafmaß", MB, 160, "strafz", fill=WEISS, size=30, anker="m", bis="doppel"),
    pl("Teil jedes Diebstahls", MB, 160, "doppel", fill=WEISS, size=28, anker="m", anim="cut", bis="doppel2"),
    ficon("tabler", "file-x", MB, 380, 100, "doppel2", fuell=ROT, anim="cut"),
    pl("doppelt verwertet", MB, 160, "doppel2", fill=ROTHELL, size=30, anker="m", anim="cut"),
]))

# K Verfahrensrüge: der übergangene Zeuge --------------------------------------------------------------------------------------
PV = "Verfahrensrüge"
folie([("verf", f"{PV} · der übergangene Zeuge"), ("ba", f"{PV} › Beweisantrag, § 244 Abs. 3 StPO"),
       ("p244", f"{PV} › Gerichtsbeschluss, § 244 Abs. 6 StPO"), ("ohne", f"{PV} › nicht beschieden: Verfahrensfehler")],
      rechts_frei([
    *tafel("verf", "Verfahrensrüge: der Zeuge", size=46),
    z("Fehler auf dem Weg zum Urteil: Verfahrensrüge", 110, 180, "verf", "Bold", 34),
    z("Beweisantrag:", 110, 255, "ba", "ExtraBold", 34),
    z("bestimmte Tatsache: 21 bis 23 Uhr beim Fußballtraining", 150, 305, beim("ba", "bestimmte"), size=30),
    z("bestimmter Zeuge: Herr Stoll, der dabei war", 150, 350, beim("ba", "bestimmter"), size=30),
    z("§ 244 Abs. 3 S. 1 StPO", 150, 395, beim("ba", "Paragraf"), size=28, farbe=TEXT),
    *wortlaut(110, 455, 1040, 110, "p244", [
        [("„Die Ablehnung eines Beweisantrages bedarf", 0)],
        [("eines ", 0), ("Gerichtsbeschlusses", "g"), (".“", 0)],
    ], 30, {"g": beim("p244", "Gerichtsbeschlusses")}, "§ 244 Abs. 6 S. 1 StPO"),
    nein(135, 655, "ohne", gr=20),
    z("hier: gar nicht beschieden", 175, 635, "ohne", "Bold", 34),
    z("Verfahrensfehler", 175, 690, beim("ohne", "Verfahrensfehler"), "ExtraBold", 34, farbe=DROT),
    z("vgl. BGH, Beschl. v. 21.4.2021 – 3 StR 300/20, Rn. 8", 175, 745, beim("ohne", "Verfahrensfehler"), size=26,
      farbe=TEXT),
    peep_voll("LZ_ruhig", X1, BR, FR, "verf", bis="ohne"),
    peep_voll("LZ_sorge", X1, BR, FR, "ohne", anim="cut"),
    peep_voll("ST_ruhig", X2, BR, FR, "verf", d=0.2, bis="ohne"),
    peep_voll("ST_sorge", X2, BR, FR, "ohne", anim="cut"),
    namensschild("Rechtsanwältin Lenz", X1, BR, "verf", LILA, d=0.2),
    namensschild("Herr Stoll", X2, BR, "verf", GRUEN, d=0.3),
    ficon("tabler", "user-question", MB, 380, 100, "verf", fuell=WEISS, bis="ba"),
    pl("übergangener Zeuge", MB, 160, "verf", fill=WEISS, size=28, anker="m", bis="ba"),
    ficon("tabler", "ball-football", MB, 380, 100, "ba", fuell=WEISS, anim="cut", bis="ohne"),
    pl("Beweisantrag", MB, 160, "ba", fill=GELB, size=30, anker="m", anim="cut", bis="ohne"),
    ficon("tabler", "ear-off", MB, 380, 100, "ohne", fuell=WEISS, anim="cut"),
    pl("nicht beschieden", MB, 160, "ohne", fill=ROTHELL, size=30, anker="m", anim="cut"),
]))

# L Verfahrensrüge: der Tatsachenvortrag, § 344 II 2 StPO ----------------------------------------------------------------------
folie([("vortrag", f"{PV} › Tatsachenvortrag"), ("p344b", f"{PV} › § 344 Abs. 2 Satz 2 StPO"),
       ("voll", f"{PV} › vollständig und genau"), ("inhalt", f"{PV} › Antrag, Zeitpunkt, kein Beschluss"),
       ("prot", f"{PV} › Beweis durch das Protokoll, § 274 StPO")], rechts_frei([
    *tafel("vortrag", "Verfahrensrüge: der Vortrag", size=46),
    *wortlaut(110, 180, 1040, 110, "p344b", [
        [("„Ersterenfalls müssen die den Mangel enthaltenden", 0)],
        [("Tatsachen", "t"), (" angegeben werden.“", 0)],
    ], 30, {"t": beim("p344b", "Tatsachen")}, "§ 344 Abs. 2 S. 2 StPO"),
    *wortlaut(110, 345, 1040, 150, "voll", [
        [("„… so ", 0), ("vollständig", "v"), (" und genau darlegen, dass das", 0)],
        [("Revisionsgericht ", 0), ("allein anhand der Revisionsbegründung", "a")],
        [("in die Lage versetzt wird, … endgültig zu entscheiden.“", 0)],
    ], 30, {"v": beim("voll", "vollständig"), "a": beim("voll", "allein")}, "BGH, Urt. v. 20.5.2026 – 2 StR 57/25, Rn. 46"),
    ok(135, 580, beim("inhalt", "Antrag"), gr=20),
    z("der Antrag im Wortlaut", 175, 560, beim("inhalt", "Antrag"), "Bold", 32),
    ok(135, 630, beim("inhalt", "wann"), gr=20),
    z("wann er gestellt wurde", 175, 610, beim("inhalt", "wann"), "Bold", 32),
    ok(135, 680, beim("inhalt", "kein"), gr=20),
    z("bis zum Urteil kein Beschluss", 175, 660, beim("inhalt", "kein"), "Bold", 32),
    z("Beweis: das Protokoll, § 274 StPO", 110, 745, "prot", "ExtraBold", 32),
    peep_voll("LZ_denkt", X1, BR, FR, "vortrag", bis="inhalt"),
    peep_voll("LZ_ruhig", X1, BR, FR, "inhalt", anim="cut", bis="prot"),
    peep_voll("LZ_froh", X1, BR, FR, "prot", anim="cut"),
    peep_voll("BR_ruhig", X2, BR, FR, "vortrag", d=0.2, bis="voll"),
    peep_voll("BR_sorge", X2, BR, FR, "voll", anim="cut"),
    namensschild("Rechtsanwältin Lenz", X1, BR, "vortrag", LILA, d=0.2),
    namensschild("Herr Brockmann", X2, BR, "vortrag", BLAU, d=0.3),
    ficon("tabler", "file-pencil", MB, 380, 100, "vortrag", fuell=GELB, bis="inhalt"),
    pl("die Hürde", MB, 160, "vortrag", fill=WEISS, size=30, anker="m", bis="p344b"),
    pl("Tatsachen angeben", MB, 160, "p344b", fill=GELB, size=28, anker="m", anim="cut", bis="voll"),
    pl("vollständig", MB, 160, "voll", fill=WEISS, size=30, anker="m", anim="cut", bis="inhalt"),
    ficon("tabler", "list-check", MB, 380, 100, "inhalt", fuell=WEISS, anim="cut", bis="prot"),
    ficon("tabler", "file-description", MB, 380, 100, "prot", fuell=WEISS, anim="cut"),
    pl("Protokoll", MB, 160, "prot", fill=WEISS, size=30, anker="m", anim="cut"),
]))

# M Beruhen und absolute Revisionsgründe ------------------------------------------------------------------------------------------
PB = "Beruhen"
folie([("beruh", f"{PB} › § 337 Abs. 1 StPO"), ("beruh2", f"{PB} › möglicherweise anders ausgefallen"),
       ("moegl", f"{PB} › hier: Freispruch möglich"), ("p338", "Absolute Revisionsgründe, § 338 StPO"),
       ("oeff", "Absolute Revisionsgründe › z. B. Öffentlichkeit, § 338 Nr. 6 StPO")], rechts_frei([
    *tafel("beruh", "Beruhen"),
    z("Das Urteil muss auf dem Fehler beruhen, § 337 Abs. 1 StPO.", 110, 180, "beruh", "Bold", 32),
    *wortlaut(110, 240, 1040, 110, "beruh2", [
        [("„Ein Urteil beruht auf einem Rechtsfehler nur dann,", 0)],
        [("wenn es ohne diesen ", 0), ("möglicherweise", "m"), (" anders ausgefallen wäre.“", 0)],
    ], 30, {"m": beim("beruh2", "möglicherweise")}, "BGH, Urt. v. 1.7.2021 – 3 StR 518/19, Rn. 94"),
    ok(135, 445, "moegl", gr=20),
    z("Herr Stoll bestätigt das Alibi: Freispruch möglich", 175, 425, "moegl", "Bold", 32),
    z("Das genügt.", 175, 475, beim("moegl", "genügt"), "ExtraBold", 32),
    fb(110, 555, 1040, 130, LILAHELL, "p338", [("§ 338 StPO: absolute Revisionsgründe", "ExtraBold", 34, INK),
                                              ("Beruhen unwiderleglich vermutet", "Bold", 32, INK)]),
    z("z. B. Nr. 6: Vorschriften über die Öffentlichkeit verletzt", 110, 710, "oeff", size=32),
    peep_voll("BR_ruhig", X1, BR, FR, "beruh", bis="moegl"),
    peep_voll("BR_froh", X1, BR, FR, "moegl", anim="cut"),
    peep_voll("ST_ruhig", X2, BR, FR, "beruh", d=0.2, bis="moegl"),
    peep_voll("ST_froh", X2, BR, FR, "moegl", anim="cut"),
    namensschild("Herr Brockmann", X1, BR, "beruh", BLAU, d=0.2),
    namensschild("Herr Stoll", X2, BR, "beruh", GRUEN, d=0.3),
    ficon("tabler", "scale", MB, 380, 110, "beruh", fuell=GELB, bis="moegl"),
    pl("Beruhen?", MB, 160, "beruh", fill=WEISS, size=30, anker="m", bis="beruh2"),
    pl("möglicherweise anders", MB, 160, beim("beruh2", "möglicherweise"), fill=GELB, size=28, anker="m", bis="moegl"),
    ficon("tabler", "user-check", MB, 380, 100, "moegl", fuell=GRUEN, anim="cut", bis="p338"),
    pl("Freispruch möglich", MB, 160, "moegl", fill=GRUEN, size=30, anker="m", anim="cut", bis="p338"),
    ficon("tabler", "lock", MB, 380, 90, "p338", fuell=LILA, anim="cut", bis="oeff"),
    pl("absolut", MB, 160, "p338", fill=LILA, size=30, anker="m", anim="cut", bis="oeff"),
    ficon("tabler", "users-group", MB, 380, 110, "oeff", fuell=WEISS, anim="cut"),
    pl("Öffentlichkeit", MB, 160, "oeff", fill=WEISS, size=30, anker="m", anim="cut"),
]))

# N Ergebnis ------------------------------------------------------------------------------------------------------------------------
PE = "Ergebnis"
folie([("erg", f"{PE} › Verfahrensrüge hat Erfolg"), ("aufh", f"{PE} › Aufhebung, § 353 StPO"),
       ("zur", f"{PE} › Zurückverweisung, § 354 Abs. 2 StPO")], rechts_frei([
    *tafel("erg", "Ergebnis im Fall"),
    fb(110, 180, 1040, 110, GRUEN, "erg", [("Die Verfahrensrüge hat Erfolg.", "ExtraBold", 36, INK)]),
    z("Aufhebung mit den Feststellungen, § 353 StPO", 110, 345, "aufh", "Bold", 34),
    z("Zurückverweisung an eine andere Strafkammer,", 110, 425, "zur", "Bold", 34),
    z("§ 354 Abs. 2 StPO", 150, 475, beim("zur", "Paragraf"), "Bold", 32),
    peep_voll("BR_ruhig", X2, BR, FR, "erg", bis=beim("erg", "Erfolg")),
    peep_voll("BR_froh", X2, BR, FR, beim("erg", "Erfolg"), anim="cut"),
    peep_voll("LZ_ruhig", X1, BR, FR, "erg", d=0.2, bis="aufh"),
    peep_voll("LZ_froh", X1, BR, FR, "aufh", anim="cut"),
    namensschild("Herr Brockmann", X2, BR, "erg", BLAU, d=0.2),
    namensschild("Rechtsanwältin Lenz", X1, BR, "erg", LILA, d=0.3),
    ficon("tabler", "file-check", MB, 380, 100, "erg", fuell=GRUEN, bis="aufh"),
    pl("Erfolg", MB, 160, beim("erg", "Erfolg"), fill=GRUEN, size=30, anker="m", bis="aufh"),
    ficon("tabler", "file-x", MB, 380, 100, "aufh", fuell=ROT, anim="cut", bis="zur"),
    pl("aufgehoben", MB, 160, "aufh", fill=ROTHELL, size=30, anker="m", anim="cut", bis="zur"),
    ficon("tabler", "arrow-back-up", MB, 380, 100, "zur", fuell=WEISS, anim="cut"),
    pl("zurückverwiesen", MB, 160, "zur", fill=BLAU, size=30, anker="m", anim="cut"),
]))

# O Revisionsbegründung (Klausurkonvention) ----------------------------------------------------------------------------------
folie([("schrift", "Klausur › Revisionsbegründung"), ("rb1", "Revisionsbegründung › I. Antrag"),
       ("rb2", "Revisionsbegründung › II. Verfahrensrügen"), ("rb3", "Revisionsbegründung › III. Sachrüge"),
       ("rb4", "Revisionsbegründung › Klausurkonvention")], rechts_frei([
    *tafel("schrift", "Revisionsbegründung"),
    karte(140, 185, 960, 440, "schrift", fill=HELL, rund=10, schatten=6),
    z("Revisionsbegründung für Herrn Brockmann", 180, 210, "schrift", "ExtraBold", 34, rechts=1080),
    z("I. Antrag: Aufhebung und Zurückverweisung", 180, 290, "rb1", "Bold", 32, rechts=1080),
    z("II. Verfahrensrügen: je mit vollständigem", 180, 370, "rb2", "Bold", 32, rechts=1080),
    z("Tatsachenvortrag (hier § 244 Abs. 6 S. 1 StPO)", 220, 415, beim("rb2", "Tatsachenvortrag"), size=30, rechts=1080),
    z("III. Sachrüge: erst allgemein erhoben,", 180, 495, "rb3", "Bold", 32, rechts=1080),
    z("dann ausgeführt (hier § 46 Abs. 3 StGB)", 220, 540, beim("rb3", "dann"), size=30, rechts=1080),
    fb(110, 680, 1040, 110, LILAHELL, "rb4", [("Dieser Aufbau ist Klausurkonvention.", "ExtraBold", 34, INK)]),
    peep_voll("LZ_ruhig", XS, BR, FR, "schrift", bis="rb4"),
    peep_voll("LZ_froh", XS, BR, FR, "rb4", anim="cut"),
    namensschild("Rechtsanwältin Lenz", XS, BR, "schrift", LILA, d=0.2),
    ficon("tabler", "writing", XS, 380, 100, "schrift", fuell=GELB, bis="rb4"),
    pl("Revisionsbegründung", XS, 160, "schrift", fill=GELB, size=30, anker="m", bis="rb4"),
    ficon("tabler", "school", XS, 380, 110, "rb4", fuell=LILA, anim="cut"),
    pl("Klausurkonvention", XS, 160, "rb4", fill=LILA, size=30, anker="m", anim="cut"),
]))

# P Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · Wo steht der Fehler?"), ("tipp3", "Klausurtipp · Verfahrensrüge mit allen Tatsachen"),
       ("tipp4", "Klausurtipp · immer auch die allgemeine Sachrüge")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Frag bei jedem Fehler: Wo steht er?", 200, 200, beim("tipp", "Frag"), "Bold", 36),
    z("in den Urteilsgründen: Sachrüge", 200, 290, "tipp2", size=34),
    z("nur im Ablauf der Hauptverhandlung:", 200, 370, "tipp3", size=34),
    z("Verfahrensrüge mit allen Tatsachen,", 200, 420, beim("tipp3", "Verfahrensrüge"), "Bold", 34),
    z("auch denen, die gegen dich sprechen", 200, 470, beim("tipp3", "auch"), "Bold", 34),
    z("vgl. BGH, Urt. v. 22.5.2025 – 4 StR 576/24, Rn. 11", 240, 525, beim("tipp3", "auch"), size=26, farbe=TEXT),
    ok(220, 625, "tipp4", gr=18),
    z("immer zusätzlich: allgemeine Sachrüge", 260, 600, "tipp4", "Bold", 36),
    *redet("LX_warnt", LXX, BR, FR + 60, "tipp", "sch"),
    namensschild("Lexi", LXX, BR, "tipp", GELB, d=0.2),
])

# Q Prüfschema ---------------------------------------------------------------------------------------------------------------------
K1, K2 = 150, 210
folie([("sch", "Prüfschema"), ("s1", "Prüfschema › I. Zulässigkeit"), ("s2", "Prüfschema › II. Verfahrensrügen"),
       ("s3", "Prüfschema › III. Sachrüge"), ("s4", "Prüfschema › IV. Antrag")], [
    karte(60, 50, 1800, 900, "sch"),
    titel("Prüfschema: Revision im Strafrecht", 110, 90, "sch", 54),
    z("I. Zulässigkeit", K1, 190, "s1", "Bold", 38, rechts=1820),
    z("statthaft, Frist und Form – §§ 333, 341, 344, 345 StPO", K2, 245, beim("s1", "statthaft"), size=32, farbe=TEXT,
      rechts=1820),
    z("II. Verfahrensrügen", K1, 330, "s2", "Bold", 38, rechts=1820),
    z("Verfahrensfehler – vollständiger Vortrag, § 344 Abs. 2 S. 2 StPO", K2, 385, beim("s2", "Fehler"), size=32,
      farbe=TEXT, rechts=1820),
    z("Beruhen, § 337 StPO, oder absoluter Revisionsgrund, § 338 StPO", K2, 435, beim("s2", "Beruhen"), size=32,
      farbe=TEXT, rechts=1820),
    z("III. Sachrüge", K1, 520, "s3", "Bold", 38, rechts=1820),
    z("Schuldspruch und Strafzumessung – allein am Urteil", K2, 575, beim("s3", "Schuldspruch"), size=32, farbe=TEXT,
      rechts=1820),
    z("IV. Antrag", K1, 660, "s4", "Bold", 38, rechts=1820),
    z("Aufhebung und Zurückverweisung, §§ 353, 354 Abs. 2 StPO", K2, 715, beim("s4", "aufheben"), size=32, farbe=TEXT,
      rechts=1820),
])

# R Merksatz (Lexi) ------------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Was im Urteil steht,", 0)], [("prüft die ", 0), ("Sachrüge", "a"), (".", 0)]],
                750, 300, 50, "merke", {"a": beim("merke", "Sachrüge")}),
    *markertext([[("Was in der Hauptverhandlung geschah,", 0)], [("braucht die ", 0), ("Verfahrensrüge", "b"), (",", 0)],
                 [("mit ", 0), ("allen Tatsachen", "c"), (".", 0)]], 750, 520, 46, "mz",
                {"b": beim("mz", "Verfahrensrüge"), "c": beim("mz", "allen")}),
    *redet("LX_erklaert", 1680, 960, 690, "merke", lexi_bis_ende("merke")),
    namensschild("Lexi", 1680, 960, "merke", GELB, d=0.2),
])
