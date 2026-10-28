"""Folge 016 · Volkszählungsurteil: Die Geburtsstunde des Datenschutzes – Serienstandard Open Peeps (Katzenkönig).
Echter Fall sachlich nacherzählt (BVerfGE 65, 1 – 1 BvR 209/83 u. a., Urt. v. 15.12.1983); Figuren fiktiv, keine realen
Beschwerdeführer, Richter oder Politiker. Szenen laut ../SZENENPLAN.md: A Fragebogen (Wohnzimmer), B Zähler an der Haustür,
C Was mit den Daten geschieht, D Der Nachbar (Bürgerinitiative), E Die Frage, F Sachverhalt, G Zulässigkeit,
H Schutzbereich, I Kein belangloses Datum, J Wer was wann weiß, K Eingriff und Rechtfertigung, L Zweckbindung,
M Erhebungsprogramm, N Umschlag und Nachbesserung, O Melderegisterabgleich, P Übermittlung und Ergebnis, Q Rechtslage heute,
R Klausurtipp (Lexi), S Klausurschema, T Merksatz (Lexi). Geräusche nur bei sichtbarer Handlung (Türklingel, Umschlag)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np

bausteine.FIGORDNER = "op_016/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
GRAU = (176, 178, 190, 255)
PAPIER = (250, 246, 232, 255)
DAUER = bausteine._cj()["dauer"]
HC = "fluent-emoji-high-contrast"

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
    return fl_block(x, y, w, h, fill, cue, [(glyphen(t), s, g, f) for t, s, g, f in zeilen], **k)


def bis_(el, bis):
    el.bis = bis
    return el


def lexi_bis_ende(cue):
    return (cue, round(DAUER - bausteine._t(cue) - 0.05, 3))


def fig(name, cx, unten, hoehe, folge, d=0.0, bis=None, erst="pop"):
    """Mimikfolge einer Figur am selben Platz: folge = [(cue, suffix)] → harte Schnitte."""
    els = []
    for i, (c, s) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else bis
        els.append(peep_voll(f"{name}_{s}", cx, unten, hoehe, c, anim=erst if i == 0 else "cut", d=d if i == 0 else 0.0, bis=b))
    return els


def hand(name, cx, unten, hoehe, seite):
    """Äußerster Punkt der Figur (Hand) im Band 40–62 % der Höhe; seite = -1 links, +1 rechts."""
    e = peep_voll(name, cx, unten, hoehe, "_")
    a = np.asarray(e.sprite)[:, :, 3] > 40
    h = a.shape[0]
    band = a[int(h * 0.40):int(h * 0.62)]
    ys, xs = np.nonzero(band)
    i = xs.argmin() if seite < 0 else xs.argmax()
    return e.x + xs[i], e.y + int(h * 0.40) + ys[i]


def rechts_frei(els, x0=1250):
    """Figuren und Requisiten der Tafelfolien stehen rechts der Tafel."""
    for e in els:
        n = e.name or ""
        if n.startswith(("bild:", "ficon:")) or "/op_016/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


BODEN, FH = 880, 480
FX, FB, FR = 1560, 930, 460                 # Figur neben der Tafel
IX, IU = 1560, 400                          # Requisit über der Figur
NULL = ("fall", -round(bausteine._t("fall") + 0.4, 3))    # 0,4 s vor Hauptfilmbeginn: ab 0,0 s voll sichtbar
HA_X = 1560

# A Fall: der Fragebogen ----------------------------------------------------------------------------------------------
FRAGEN = [("briefcase", "Beruf", "Beruf", GELB), ("building", "Arbeitsstätte", "Arbeitsstätte", BLAU),
          ("bus", "Weg zur Arbeit", "Weg", ORANGE), ("home", "Wohnung", "Wohnung", GRUEN), ("coins", "Miete", "Miete", GELB),
          ("building-church", "Religion", "Religion", LILA)]
folie([(NULL, "Fall · Der Fragebogen")], [
    linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK),
    ficon("tabler", "table", 1120, BODEN - 2, 330, NULL, fuell=ORANGE),
    ficon("tabler", "lamp", 1120, BODEN - 160, 120, NULL, fuell=GELB),
    peep_voll("HA_ruhig", HA_X, BODEN, FH, NULL, bis="bogen"),
    pl("Frühjahr 1983", 1350, 60, beim("fall", "Frühjahr"), fill=GELB, size=36),
    pl("Volkszählung 1983", 1350, 150, beim("fall", "Volkszählung"), fill=BLAU, size=36),
    # Der Bogen
    karte(90, 120, 760, 720, "bogen", fill=PAPIER),
    titel("Fragebogen", 130, 160, "bogen", 48),
    z("Volkszählung 1983", 140, 240, "bogen", "Bold", 32, farbe=TEXT, rechts=840),
    *[e for i, (ic, txt, w, f) in enumerate(FRAGEN) for e in (
        ficon("tabler", ic, 175, 360 + i * 82, 64, beim("fragen", w), fuell=f),
        z(txt, 235, 312 + i * 82, beim("fragen", w), "Bold", 38, rechts=840),
        linienzug([(520, 350 + i * 82), (800, 350 + i * 82)], beim("fragen", w), breite=4, farbe=GRAU))],
    peep_voll("HA_liest", HA_X, BODEN, FH, "bogen", anim="cut"),
    pl("Frau Hartmann", HA_X, BODEN + 22, beim("bogen", "Hartmann"), fill=LILA, size=30, anker="m"),
])

# B Fall: der Zähler an der Haustür -----------------------------------------------------------------------------------
LEX, HBX = 760, 1480
LER = ("LE_redet_r", LEX, BODEN, FH)
HAR = ("HA_redet", HBX, BODEN, FH)
lx, ly = hand("LE_ruhig_r", LEX, BODEN, FH, +1)
folie([("zaehler", "Fall · Der Zähler")], [
    linienzug([(60, BODEN), (1860, BODEN)], "zaehler", breite=7, farbe=INK),
    ficon("tabler", "door", 1130, BODEN - 2, 300, "zaehler", fuell=ORANGE),
    szene(ficon("tabler", "bell", 945, BODEN - 200, 60, beim("zaehler", "Bringen"), fuell=GELB), "016klingel*", 0.9),
    *fig("HA", HBX, BODEN, FH, [("zaehler", "ruhig"), ("h1", "ruhig")], bis="h1"),
    *redet("HA_redet", HBX, BODEN, FH, "h1", "melde"),
    pl("Frau Hartmann", HBX, BODEN + 22, "zaehler", fill=LILA, size=30, anker="m", d=0.2),
    peep_voll("LE_ruhig_r", LEX, BODEN, FH, beim("zaehler", "Bringen"), bis="z1"),
    *redet("LE_redet_r", LEX, BODEN, FH, "z1", "h1"),
    peep_voll("LE_ruhig_r", LEX, BODEN, FH, "h1", anim="cut"),
    ficon("tabler", "clipboard-list", lx + 10, ly + 60, 90, beim("zaehler", "Bringen"), fuell=WEISS),
    pl("Herr Lehmann", LEX, BODEN + 22, beim("zaehler", "Lehmann"), fill=BLAU, size=30, anker="m"),
    pl("ehrenamtlicher Zähler", 330, 560, beim("zaehler", "ehrenamtlicher"), fill=BLAU, size=32, anker="m"),
    blase("sprech", 700, 190, "z1", 620, 210, inhalt=["Ausfüllen müssen Sie das.", "Sonst droht ein Bußgeld."],
          textsize=34, figur=LER, bis="h1"),
    ficon("tabler", "coins", 330, 470, 100, beim("z1", "Bußgeld"), fuell=GELB),
    pl("Bußgeld", 330, 480, beim("z1", "Bußgeld"), fill=ROT, size=32, anker="m"),
    blase("sprech", 740, 200, "h1", 1250, 210, inhalt=["Und wer bekommt meine Angaben", "am Ende alles zu sehen?"],
          textsize=34, figur=HAR),
])

# C Fall: was mit den Daten geschehen soll ----------------------------------------------------------------------------
FBX = 330
folie([("melde", "Fall · Was mit den Daten geschieht")], [
    ficon("tabler", "forms", FBX, 600, 260, "melde", fuell=WEISS),
    pl("Fragebogen", FBX, 620, "melde", fill=WEISS, size=32, anker="m"),
    fig("HA", 1640, BODEN, FH, [("melde", "sorge")])[0],
    pfeil(500, 420, 840, 260, beim("melde", "Melderegister"), breite=8, kopf=26),
    ficon("tabler", "address-book", 1000, 300, 150, beim("melde", "Melderegister"), fuell=GELB),
    pl("Melderegister", 1000, 320, beim("melde", "Melderegister"), fill=GELB, size=32, anker="m"),
    pl("vergleichen", 560, 200, beim("melde", "vergleichen"), fill=WEISS, size=30, anker="m"),
    pl("berichtigen", 1000, 400, beim("melde", "berichtigen"), fill=ROT, size=30, anker="m"),
    pfeil(500, 520, 840, 640, beim("weiter", "Behörden"), breite=8, kopf=26),
    pfeil(500, 560, 840, 830, beim("weiter", "Gemeinden"), breite=8, kopf=26),
    pl("Einzelangaben", 560, 720, "weiter", fill=WEISS, size=30, anker="m"),
    ficon("tabler", "building-bank", 1000, 690, 130, beim("weiter", "Behörden"), fuell=GRAU),
    pl("Behörden", 1000, 700, beim("weiter", "Behörden"), fill=GRAU, size=28, anker="m"),
    ficon("tabler", "building-community", 1000, 900, 130, beim("weiter", "Gemeinden"), fuell=GRUEN),
    pl("Gemeinden", 1240, 845, beim("weiter", "Gemeinden"), fill=GRUEN, size=28, anker="m"),
])

# D Fall: der Nachbar --------------------------------------------------------------------------------------------------
SOX, HDX = 1560, 1060
SOR = ("SO_redet", SOX, BODEN, FH)
folie([("sommer", "Fall · Der Nachbar")], [
    linienzug([(60, BODEN), (1860, BODEN)], "sommer", breite=7, farbe=INK),
    ficon("tabler", "building-cottage", 250, BODEN - 2, 280, "sommer", fuell=GELB),
    peep_voll("HA_ruhig_r", HDX, BODEN, FH, "sommer"),
    *fig("SO", SOX, BODEN, FH, [(beim("sommer", "Herr"), "ruhig")], bis="s1"),
    *redet("SO_redet", SOX, BODEN, FH, "s1", "frage"),
    pl("Herr Sommer", SOX, BODEN + 22, beim("sommer", "Sommer"), fill=GRUEN, size=30, anker="m"),
    ficon("tabler", "users-group", 620, BODEN - 2, 230, beim("sommer", "Bürgerinitiative"), fuell=ORANGE),
    pl("Bürgerinitiative", 620, BODEN + 22, beim("sommer", "Bürgerinitiative"), fill=ORANGE, size=30, anker="m"),
    blase("sprech", 820, 260, "s1", 1180, 210, inhalt=["Wenn der Staat das alles speichert", "und verknüpft, gehe ich da",
                                                       "lieber nicht mehr hin."], textsize=33, figur=SOR),
    ficon("tabler", "database", 330, 480, 120, beim("s1", "speichert"), fuell=BLAU),
    ficon("tabler", "link", 520, 470, 100, beim("s1", "verknüpft"), fuell=WEISS),
    kreuz_i(620, 560, beim("s1", "lieber"), gr=46),
])

# E Fall: die Frage ----------------------------------------------------------------------------------------------------
folie([("frage", "Fall · Die Frage")], [
    *[ficon("tabler", "file-text", x, 760 - i * 25, 120, ("frage", 0.15 * i), fuell=WEISS) for i, x in enumerate((180, 300, 420, 540))],
    pl("Verfassungsbeschwerden", 360, 800, beim("frage", "Verfassungsbeschwerde"), fill=GELB, size=32, anker="m"),
    pfeil(640, 640, 900, 640, beim("frage", "Volkszählungsgesetz"), breite=8, kopf=26),
    ficon("tabler", "file-certificate", 1070, 720, 170, beim("frage", "Volkszählungsgesetz"), fuell=BLAU),
    pl("Volkszählungsgesetz 1983", 1070, 740, beim("frage", "Volkszählungsgesetz"), fill=BLAU, size=30, anker="m"),
    fig("HA", 1640, BODEN, FH, [("frage", "denkt")])[0],
    pl("Darf der Staat so fragen?", 760, 150, beim("frage", "Darf"), fill=PINK, size=40, anker="m"),
    pl("Was darf er mit den Antworten tun?", 760, 260, beim("frage", "Und"), fill=PINK, size=40, anker="m"),
])

# F Sachverhalt --------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Frühjahr 1983: Nach dem Volkszählungsgesetz 1983 sollen alle Auskunftspflichtigen einen Fragebogen ausfüllen, unter "
    "anderem zu Beruf, Arbeitsstätte, Weg zur Arbeit, Wohnung, Miete und Religion. Wer nicht antwortet, dem droht ein "
    "Bußgeld. Frau Hartmann fragt den ehrenamtlichen Zähler Herrn Lehmann, wer ihre Angaben zu sehen bekommt. Das Gesetz "
    "erlaubt, die Angaben mit dem Melderegister zu vergleichen und es zu berichtigen (§ 9 Abs. 1 VZG 1983); Einzelangaben "
    "dürfen an Behörden und Gemeinden gehen (§ 9 Abs. 2, 3). Ihr Nachbar Herr Sommer, aktiv in einer Bürgerinitiative, "
    "fürchtet, dass seine Daten gespeichert und verknüpft werden. Viele Bürger erheben Verfassungsbeschwerde unmittelbar "
    "gegen das Gesetz.",
    "(Nach BVerfGE 65, 1 – 1 BvR 209/83 u. a.; Frau Hartmann, Herr Lehmann und Herr Sommer sind erfunden.)",
], "Sind die Verfassungsbeschwerden zulässig und begründet?")

# G Zulässigkeit -------------------------------------------------------------------------------------------------------
folie([("zul", "A. Zulässigkeit › Verfassungsbeschwerde direkt gegen das Gesetz")], rechts_frei([
    *tafel("zul", "A. Zulässigkeit"),
    z("Verfassungsbeschwerde gegen das VZG 1983", 110, 195, "zul", "Bold", 38),
    ok(140, 290, beim("zul", "ausnahmsweise"), gr=22),
    z("ausnahmsweise direkt gegen das Gesetz", 185, 270, beim("zul", "ausnahmsweise"), size=36),
    z("Bögen binnen weniger Wochen verteilt", 185, 370, "eile", size=36),
    z("und eingesammelt", 185, 420, beim("eile", "eingesammelt"), size=36),
    z("kaum Zeit für die Verwaltungsgerichte", 185, 500, beim("eile", "Für"), size=36),
    z("BVerfGE 65, 1 (36–38) · Rn. 133–141", 110, 600, beim("eile", "Verwaltungsgerichte"), size=28, farbe=TEXT),
    ficon("tabler", "calendar", IX, IU, 150, beim("eile", "Bögen"), fuell=WEISS),
    ficon("tabler", "hourglass", IX + 150, IU, 90, beim("eile", "kaum"), fuell=GELB),
    *fig("HA", FX, FB, FR, [("zul", "denkt")]),
]))

# H Schutzbereich ------------------------------------------------------------------------------------------------------
folie([("sb", "B. Begründetheit › I. Schutzbereich: Art. 2 I i. V. m. Art. 1 I GG"),
       ("ris", "B. Begründetheit › I. Schutzbereich: informationelle Selbstbestimmung")], rechts_frei([
    *tafel("sb", "B. I. Schutzbereich"),
    z("allgemeines Persönlichkeitsrecht", 110, 195, beim("sb", "allgemeine"), "Bold", 38),
    z("Art. 2 I i. V. m. Art. 1 I GG", 110, 255, beim("sb", "Artikel"), size=36),
    blk(110, 330, 1040, 110, GELB, beim("ris", "informationelle"),
        [("Recht auf informationelle Selbstbestimmung", "ExtraBold", 38, INK)]),
    z("Jeder darf grundsätzlich selbst bestimmen", 110, 490, "ris2", size=36),
    z("über Preisgabe und Verwendung", 110, 545, beim("ris2", "Preisgabe"), size=36),
    z("seiner persönlichen Daten", 110, 600, beim("ris2", "persönlichen"), size=36),
    z("BVerfGE 65, 1 (41–43) · Rn. 151–155", 110, 690, beim("ris2", "Daten"), size=28, farbe=TEXT),
    ficon("tabler", "user-shield", IX, IU, 150, "sb", fuell=GELB, bis="ris2"),
    ficon("tabler", "forms", IX, IU, 140, "ris2", fuell=WEISS),
    *fig("HA", FX, FB, FR, [("sb", "ruhig"), ("ris2", "froh")]),
]))

# I Kein belangloses Datum -------------------------------------------------------------------------------------------------
folie([("edv", "B. Begründetheit › I. Schutzbereich › automatische Datenverarbeitung"),
       ("belang", "B. Begründetheit › I. Schutzbereich › kein belangloses Datum")], rechts_frei([
    *tafel("edv", "Warum gerade jetzt?"),
    z("automatische Datenverarbeitung:", 110, 195, beim("edv", "automatischer"), "Bold", 38),
    z("– unbegrenzt speichern", 150, 265, beim("edv", "unbegrenzt"), size=36),
    z("– in Sekunden abrufen", 150, 325, beim("edv", "Sekunden"), size=36),
    z("– zu einem Persönlichkeitsbild zusammenfügen", 150, 385, beim("edv", "Persönlichkeitsbild"), size=36),
    blk(110, 470, 1040, 110, ROT, "belang", [("kein belangloses Datum mehr", "ExtraBold", 40, INK)]),
    z("entscheidend: wofür verwendet,", 110, 630, "wofuer", "Bold", 36),
    z("womit verknüpft", 110, 685, beim("wofuer", "womit"), "Bold", 36),
    z("BVerfGE 65, 1 (42, 45) · Rn. 153, 158", 110, 770, beim("wofuer", "verknüpft"), size=28, farbe=TEXT),
    ficon("tabler", "device-desktop", IX, IU, 170, beim("edv", "automatischer"), fuell=WEISS, bis=beim("edv", "unbegrenzt")),
    ficon("tabler", "database", IX, IU, 140, beim("edv", "unbegrenzt"), fuell=BLAU, bis=beim("edv", "Sekunden")),
    ficon("tabler", "clock", IX, IU, 140, beim("edv", "Sekunden"), fuell=GELB, bis=beim("edv", "Persönlichkeitsbild")),
    ficon("tabler", "puzzle", IX, IU, 140, beim("edv", "Persönlichkeitsbild"), fuell=LILA, bis="belang"),
    ficon("tabler", "file-text", IX, IU, 120, "belang", fuell=WEISS, bis="wofuer"),
    ficon("tabler", "link", IX, IU, 140, "wofuer", fuell=GELB),
    *fig("HA", FX, FB, FR, [("edv", "denkt"), ("belang", "schreck")]),
]))

# J Wer was wann weiß ------------------------------------------------------------------------------------------------------
folie([("wer", "B. Begründetheit › I. Schutzbereich › wer was wann weiß")], rechts_frei([
    *tafel("wer", "Wer was wann über mich weiß"),
    z("Wer nicht weiß, wer was wann über ihn weiß,", 110, 195, "wer", size=36),
    z("wird vorsichtig", 110, 250, beim("wer", "vorsichtig"), "Bold", 36),
    z("Teilnahme an einer Bürgerinitiative registriert?", 110, 350, "bi", size=36),
    z("verzichtet vielleicht darauf", 110, 405, beim("bi", "verzichtet"), "Bold", 36),
    blk(110, 490, 1040, 110, ORANGE, "gemein", [("schadet auch dem Gemeinwohl", "ExtraBold", 40, INK)]),
    z("BVerfGE 65, 1 (43) · Rn. 154", 110, 650, beim("gemein", "Gemeinwohl"), size=28, farbe=TEXT),
    ficon("tabler", "users-group", IX, IU, 190, "bi", fuell=ORANGE),
    ficon("tabler", "eye", IX + 150, IU - 120, 90, beim("bi", "registriert"), fuell=WEISS),
    *fig("SO", FX, FB, FR, [("wer", "denkt"), ("bi", "sorge")]),
    pl("Herr Sommer", FX, FB + 22, "wer", fill=GRUEN, size=28, anker="m", d=0.2),
]))

# K Eingriff und Rechtfertigung -------------------------------------------------------------------------------------------
PR = "B. › III. Rechtfertigung"
folie([("ein", "B. Begründetheit › II. Eingriff: Auskunftspflicht"), ("schranke", f"{PR} › überwiegendes Allgemeininteresse"),
       ("gesetz", f"{PR} › gesetzliche Grundlage, Normenklarheit"), ("vhm", f"{PR} › Verhältnismäßigkeit"),
       ("vork", f"{PR} › Schutzvorkehrungen")], rechts_frei([
    *tafel("ein", "II. Eingriff · III. Rechtfertigung"),
    ok(140, 215, beim("ein", "Eingriff"), gr=22),
    z("II. Eingriff: Auskunftspflicht mit Bußgeld", 185, 195, beim("ein", "Eingriff"), "Bold", 36),
    z("III. Rechtfertigung: nicht schrankenlos", 110, 290, "schranke", "Bold", 36),
    z("Einschränkung im überwiegenden Allgemeininteresse", 150, 350, beim("schranke", "Einschränkungen"), size=34),
    z("gesetzliche Grundlage: Voraussetzungen und", 150, 425, "gesetz", size=34),
    z("Umfang klar erkennbar", 150, 475, beim("gesetz", "Umfang"), size=34),
    pl("Normenklarheit", 150, 525, beim("gesetz", "Normenklarheit"), fill=GELB, size=32),
    z("Verhältnismäßigkeit", 150, 630, "vhm", size=34),
    z("organisatorische und verfahrensrechtliche", 150, 705, "vork", size=34),
    z("Schutzvorkehrungen", 150, 755, beim("vork", "Schutzvorkehrungen"), size=34),
    ficon("tabler", "coins", IX, IU, 120, "ein", fuell=GELB, bis="schranke"),
    ficon("tabler", "users", IX, IU, 140, beim("schranke", "Einschränkungen"), fuell=BLAU, bis="gesetz"),
    ficon("tabler", "book", IX, IU, 130, "gesetz", fuell=GELB, bis="vhm"),
    ficon("tabler", "scale", IX, IU, 150, "vhm", fuell=GELB, bis="vork"),
    ficon("tabler", "shield-lock", IX, IU, 130, "vork", fuell=GRUEN),
    *fig("HA", FX, FB, FR, [("ein", "sorge"), ("schranke", "denkt")]),
]))

# L Zweckbindung ------------------------------------------------------------------------------------------------------------
folie([("zweck", f"{PR} › Zweckbindung"), ("stat", f"{PR} › Zweckbindung bei der Statistik"),
       ("abschott", f"{PR} › Abschottung der Statistik")], rechts_frei([
    *tafel("zweck", "Zweckbindung"),
    z("Daten für die Verwaltung: strenge Zweckbindung", 110, 195, beim("zweck", "Daten"), "Bold", 36),
    z("Zweck bereichsspezifisch und präzise bestimmt", 150, 255, beim("zweck", "bereichsspezifisch"), size=34),
    z("Statistik: dient vielen Zwecken", 110, 350, "stat", "Bold", 36),
    nein(170, 430, beim("stat", "geht"), gr=20),
    z("strenge Zweckbindung geht nicht", 210, 410, beim("stat", "geht"), size=34),
    blk(110, 500, 1040, 90, BLAU, "abschott", [("Ausgleich: Abschottung", "ExtraBold", 38, INK)]),
    z("Statistikgeheimnis", 150, 640, beim("abschott", "Statistikgeheimnis"), size=34),
    z("möglichst frühe Anonymisierung", 150, 695, beim("abschott", "Anonymisierung"), size=34),
    z("BVerfGE 65, 1 (46–51) · Rn. 161 f., 166–171", 110, 775, beim("abschott", "Anonymisierung"), size=28, farbe=TEXT),
    ficon("tabler", "building-bank", IX, IU, 140, "zweck", fuell=GRAU, bis="stat"),
    ficon("tabler", "chart-bar", IX, IU, 140, "stat", fuell=BLAU, bis="abschott"),
    ficon("tabler", "lock", IX, IU, 120, beim("abschott", "Statistikgeheimnis"), fuell=GELB, bis=beim("abschott", "Anonymisierung")),
    ficon("tabler", "eye-off", IX, IU, 130, beim("abschott", "Anonymisierung"), fuell=WEISS),
    *fig("HA", FX, FB, FR, [("zweck", "ruhig")]),
]))

# M Erhebungsprogramm ---------------------------------------------------------------------------------------------------------
PE = "B. › III. Erhebungsprogramm, §§ 2–5 VZG 1983"
folie([("fragenok", PE)], rechts_frei([
    *tafel("fragenok", "Die Fragen selbst"),
    z("§§ 2–5 VZG 1983", 110, 190, "fragenok", size=32, farbe=TEXT),
    ok(140, 280, beim("fragenok", "klar"), gr=22), z("klar genug", 185, 260, beim("fragenok", "klar"), "Bold", 36),
    ok(140, 345, beim("fragenok", "verhältnismäßig"), gr=22),
    z("verhältnismäßig", 185, 325, beim("fragenok", "verhältnismäßig"), "Bold", 36),
    nein(140, 450, "stich", gr=20), z("Stichproben: noch zu fehleranfällig", 185, 430, "stich", size=34),
    nein(140, 520, beim("stich", "vorhandene"), gr=20), z("Register zusammenführen: bräuchte ein", 185, 500, beim("stich", "vorhandene"), size=34),
    z("einheitliches Personenkennzeichen", 185, 550, beim("stich", "einheitliches"), size=34),
    z("BVerfGE 65, 1 (52–58) · Rn. 173–196", 110, 640, beim("stich", "Personenkennzeichen"), size=28, farbe=TEXT),
    ficon("tabler", "forms", IX, IU, 140, "fragenok", fuell=WEISS, bis="stich"),
    ficon("tabler", "chart-pie", IX, IU, 140, "stich", fuell=GELB, bis=beim("stich", "vorhandene")),
    ficon("tabler", "id", IX, IU, 150, beim("stich", "vorhandene"), fuell=ROT),
    *fig("HA", FX, FB, FR, [("fragenok", "ruhig"), ("stich", "denkt")]),
]))

# N Umschlag und Nachbesserung -------------------------------------------------------------------------------------------------
PN = "B. › III. Erhebung › Schutzvorkehrungen"
HNX, BKX = 1690, 1360
hx, hy = hand("HA_froh", HNX, FB, FR, -1)
folie([("umschlag", f"{PE} › verschlossener Umschlag"), ("nach", PN)], rechts_frei([
    *tafel("umschlag", "Umschlag und Nachbesserung"),
    z("Bogen im verschlossenen Umschlag abgeben", 110, 195, "umschlag", "Bold", 36),
    z("oder per Post schicken", 110, 250, beim("umschlag", "Post"), "Bold", 36),
    z("Gesetzgeber muss nachbessern:", 110, 360, "nach", "Bold", 36),
    z("– über diese Rechte belehren", 150, 425, "nach1", size=34),
    z("– Namen und Anschriften früh löschen", 150, 485, "nach2", size=34),
    z("– Zähler nicht in der eigenen Nachbarschaft", 150, 545, "nach3", size=34),
    z("BVerfGE 65, 1 (57–60) · Rn. 194–200", 110, 630, beim("nach3", "Nachbarschaft"), size=28, farbe=TEXT),
    ficon("tabler", "mailbox", BKX, FB - 2, 170, "umschlag", fuell=GELB, bis="nach"),
    szene(bewegt(ficon("tabler", "mail", BKX, FB - 200, 90, beim("umschlag", "Umschlag"), fuell=WEISS, bis="nach"),
                 beim("umschlag", "Umschlag"), beim("umschlag", "abgeben"), hx - BKX, hy - (FB - 240)), "016umschlag*", 0.9),
    *fig("HA", HNX, FB, FR, [("umschlag", "froh")]),
    ficon("tabler", "info-circle", BKX, IU + 100, 120, "nach1", fuell=BLAU, bis="nach2"),
    ficon("tabler", "trash", BKX, IU + 100, 120, "nach2", fuell=GRAU, bis="nach3"),
    ficon("tabler", "home", BKX, IU + 100, 130, "nach3", fuell=GRUEN),
    bis_(kreuz_i(BKX, IU + 40, beim("nach3", "nicht"), gr=56), None),
]))

# O Melderegisterabgleich ------------------------------------------------------------------------------------------------------
folie([("abgl", "B. › III. Melderegisterabgleich, § 9 I VZG 1983")], rechts_frei([
    *tafel("abgl", "§ 9 I VZG 1983: Melderegisterabgleich", size=42),
    z("verbindet Statistik und Verwaltungsvollzug", 110, 200, "unver", "Bold", 36),
    blk(110, 270, 1040, 90, ROT, beim("unver", "tendenziell"), [("tendenziell Unvereinbares", "ExtraBold", 38, INK)]),
    z("Welche Behörde nutzt die Daten wofür?", 110, 410, "wohin", size=36),
    nein(140, 490, beim("wohin", "nicht"), gr=20), z("nicht vorhersehbar", 185, 470, beim("wohin", "nicht"), "Bold", 36),
    z("Nachteilsverbot (§ 9 I 2 VZG 1983):", 110, 570, "nachteil", size=34),
    z("verspricht mehr, als es leisten kann", 110, 625, beim("nachteil", "verspricht"), "Bold", 36),
    z("BVerfGE 65, 1 (61–65) · Rn. 202–209", 110, 710, beim("nachteil", "leisten"), size=28, farbe=TEXT),
    ficon("tabler", "chart-bar", 1380, IU, 120, "abgl", fuell=BLAU),
    ficon("tabler", "address-book", 1740, IU, 120, "abgl", fuell=GELB),
    pfeil(1450, IU - 60, 1660, IU - 60, "abgl", breite=7, kopf=22),
    ficon("tabler", "arrows-shuffle", IX, IU - 150, 90, "unver", fuell=WEISS, bis="wohin"),
    ficon("tabler", "question-mark", IX, IU - 140, 80, "wohin", fuell=WEISS),
    *fig("HA", FX, FB, FR, [("abgl", "denkt"), ("wohin", "sorge")]),
]))

# P Übermittlung und Ergebnis --------------------------------------------------------------------------------------------------
folie([("uebermit", "B. › III. Übermittlung, § 9 II–IV VZG 1983"), ("erg", "Ergebnis · Urteil vom 15.12.1983")], rechts_frei([
    *tafel("uebermit", "Weitergabe und Ergebnis"),
    nein(140, 215, beim("uebermit", "hielten"), gr=20),
    z("§ 9 II, III: an Behörden und Gemeinden", 185, 195, "uebermit", "Bold", 36),
    ok(140, 285, beim("wiss", "Ordnung"), gr=20),
    z("§ 9 IV: für die Wissenschaft", 185, 265, beim("wiss", "Weitergabe"), "Bold", 36),
    blk(110, 360, 1040, 230, GRUEN, "erg", [("Urteil vom 15.12.1983", "ExtraBold", 38, INK), ("", "Regular", 20, INK)]),
    z("Volkszählung als solche zulässig", 150, 470, beim("erg", "Volkszählung"), "Bold", 36),
    blk(110, 620, 1040, 90, ROT, "nichtig", [("§ 9 I–III VZG 1983 nichtig", "ExtraBold", 38, INK)]),
    z("BVerfGE 65, 1 (65–70) · Tenor, Rn. 210–221", 110, 750, beim("nichtig", "nichtig"), size=28, farbe=TEXT),
    ficon("tabler", "building-bank", 1400, IU, 120, "uebermit", fuell=GRAU, bis="wiss"),
    ficon("tabler", "building-community", 1700, IU, 120, "uebermit", fuell=GRUEN, bis="wiss"),
    bis_(kreuz_i(1550, IU - 70, beim("uebermit", "hielten"), gr=34), "wiss"),
    ficon("tabler", "microscope", IX, IU, 130, "wiss", fuell=WEISS, bis="erg"),
    bis_(haken_i(IX + 120, IU - 110, beim("wiss", "Ordnung"), gr=34), "erg"),
    ficon(HC, "classical-building", IX, IU, 170, "erg", fuell=WEISS),
    ficon("tabler", "gavel", IX + 170, IU, 100, "nichtig", fuell=GELB),
    *fig("HA", FX, FB, FR, [("uebermit", "denkt"), ("erg", "froh")]),
]))

# Q Rechtslage heute ------------------------------------------------------------------------------------------------------------
folie([("heute", "Rechtslage heute · DSGVO und Grundrechtecharta")], rechts_frei([
    *tafel("heute", "Rechtslage heute"),
    z("für viele Datenverarbeitungen:", 110, 195, "heute", size=36),
    z("Datenschutz-Grundverordnung der EU", 110, 250, beim("heute", "Datenschutz"), "Bold", 38),
    z("wo sie vollständig vereinheitlicht:", 110, 360, "charta", size=36),
    z("Maßstab in aller Regel die", 110, 415, beim("charta", "prüft"), size=36),
    z("EU-Grundrechtecharta, Art. 7 und 8", 110, 470, beim("charta", "EU"), "Bold", 38),
    z("BVerfGE 152, 216 (Recht auf Vergessen II), LS 2, Rn. 32 ff.", 110, 560, beim("charta", "acht"), size=28, farbe=TEXT),
    ficon("tabler", "flag", IX, IU, 140, "heute", fuell=BLAU, bis="charta"),
    ficon(HC, "classical-building", IX, IU, 160, "charta", fuell=WEISS),
    *fig("HA", FX, FB, FR, [("heute", "ruhig")]),
]))

# R Klausurtipp (Lexi) ---------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · Verwendung und Verknüpfung prüfen")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("nicht nur: Welches Datum wird erhoben?", 200, 200, beim("tipp", "Frag"), "Bold", 36),
    z("sondern: Wofür wird es verwendet,", 200, 290, "tipp1", size=36),
    z("womit kann es verknüpft werden?", 200, 345, beim("tipp1", "womit"), size=36),
    z("Statistik und Verwaltungsvollzug trennen", 200, 440, "tipp2", "Bold", 36),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    pl("Lexi", FX, FB + 22, "tipp", fill=GELB, size=30, anker="m", d=0.2),
])

# S Klausurschema ---------------------------------------------------------------------------------------------------------------
K1, K2, K3 = 150, 210, 270
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel("Klausurschema: Recht auf informationelle Selbstbestimmung", 110, 90, "sch", 48),
    z("I. Schutzbereich: informationelle Selbstbestimmung, Art. 2 I i. V. m. Art. 1 I GG", K1, 200, "k1", "Bold", 38, rechts=1820),
    z("II. Eingriff: Erhebung, Speicherung, Verwendung oder Weitergabe", K1, 280, "k2", "Bold", 38, rechts=1820),
    z("III. Rechtfertigung", K1, 360, "k3", "Bold", 38, rechts=1820),
    z("1. gesetzliche Grundlage im überwiegenden Allgemeininteresse", K2, 430, "k4", size=36, rechts=1820),
    z("2. Normenklarheit", K2, 495, "k5", size=36, rechts=1820),
    z("3. Verhältnismäßigkeit", K2, 560, "k6", size=36, rechts=1820),
    z("4. Zweckbindung", K2, 625, "k7", size=36, rechts=1820),
    z("5. Schutzvorkehrungen", K2, 690, "k8", size=36, rechts=1820),
])

# T Merksatz (Lexi) -------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Unter automatischer", 0)], [("Datenverarbeitung gibt es", 0)], [("kein ", 0), ("belangloses Datum.", "a")]],
                750, 300, 50, "merke", {"a": beim("merke", "belangloses")}),
    *markertext([[("Der Staat darf Daten nur auf ", 0)], [("klarer gesetzlicher Grundlage", "b"), (" verlangen", 0)],
                 [("und nur für ", 0), ("erkennbare Zwecke", "c"), (" verwenden.", 0)]], 750, 590, 46, "m2",
                {"b": beim("m2", "klarer"), "c": beim("m2", "erkennbare")}),
    *redet("LX_erklaert", 1680, 1000, 720, "merke", lexi_bis_ende("merke")),
])
