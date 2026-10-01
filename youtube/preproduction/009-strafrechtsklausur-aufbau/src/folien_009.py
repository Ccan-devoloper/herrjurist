"""Folge 009 · Strafrechtsklausur Aufbau: Tatkomplexe, Beteiligte, Reihenfolge (Methodik) – Serienstandard Open Peeps.
Szenen laut ../SZENENPLAN.md: A Werkstatt, B Fahrradladen, C Ecke (Flucht), D Klausurfrage, E Sachverhalt, F Tatkomplexe,
G1–G3 Tatkomplex 1 (Kim, Tara, Bruno), H1–H4 Tatkomplex 2 (Kim, Tara, Zurechnung), I Konkurrenzen, J Klausurtipp (Lexi),
K Klausurschema, L Merksatz (Lexi). Geräusche nur bei sichtbarer Handlung (Ladenglocke, Sturz)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *

bausteine.FIGORDNER = "op_009/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = bausteine.BG_FARBE
PFAD_FARBE = bausteine.PFAD_FARBE
HELL = (255, 251, 230, 255)
GRAU = (176, 178, 190, 255)
DAUER = bausteine._cj()["dauer"]
TK1 = "1. TK Diebstahl im Laden"
TK2 = "2. TK Flucht an der Ecke"


def z(text, x, y, cue, stil="Regular", size=38, farbe=INK, d=0.0, rechts=1170, **k):
    """Tafelzeile, die rechts nicht über die Karte hinausragen darf."""
    e = zeile(text, x, y, cue, stil, size, farbe=farbe, d=d, **k)
    assert e.x + e.sprite.width <= rechts, f"Zeile zu breit: {text} ({e.x + e.sprite.width:.0f} > {rechts})"
    return e


def tafel(cue, titel_, h=840, fill=WEISS, size=50):
    """Rechtstafel links, rechts bleibt Platz für die Figuren."""
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(titel_, 110, 100, cue, size)]


def wortring(text, wort, x, y, size, stil, cue, farbe=ORANGE, bis=None):
    """Handgezeichneter Ring um 'wort' in einer mit z() gesetzten Zeile (text an x, y)."""
    f = F(stil, size)
    i = text.index(wort)
    x0 = x + f.getlength(text[:i]); w = f.getlength(wort)
    return ring(int(x0 + w / 2), int(y + size * 0.42), int(w / 2 + 16), int(size * 0.62), cue, farbe=farbe, breite=6, bis=bis)


def mit_bis(e, bis):
    e.bis = bis
    return e


def lexi_bis_ende(cue):
    return (cue, round(DAUER - bausteine._t(cue) - 0.05, 3))


def fig(name, cx, unten, hoehe, folge, d=0.0):
    """Mimikfolge einer Figur am selben Platz: folge = [(cue, suffix)] → harte Schnitte; erstes Bild poppt."""
    els = []
    for i, (c, s) in enumerate(folge):
        bis = folge[i + 1][0] if i + 1 < len(folge) else None
        els.append(peep_voll(f"{name}_{s}", cx, unten, hoehe, c, anim="pop" if i == 0 else "cut", d=d if i == 0 else 0.0, bis=bis))
    return els


BODEN, FH = 880, 480
SITZ = 232                                   # Ohm am Boden (sitting/hands_back-2): Kopf gleich groß wie stehend

# A Fall: Werkstatt ---------------------------------------------------------------------------------------------------------
BRX, KIX, TAX = 700, 1330, 1640
BRR = ("BR_redet_r", BRX, BODEN, FH)
KIR = ("KI_redet", KIX, BODEN, FH)
folie([("werk", "Fall · In der Werkstatt")], [
    pille("Der Akku-Fall", 70, 40, "werk", fill=GELB, size=48),
    linienzug([(60, BODEN), (1860, BODEN)], "werk", breite=7, farbe=INK),
    ficon("ph", "bicycle", 330, BODEN - 2, 380, "werk", fuell=WEISS, nebenfarbe=WEISS, d=0.2),
    ficon("tabler", "tools", 330, 470, 130, "werk", fuell=GRAU, d=0.4),
    pille("Werkstatt im Hinterhof", 330, 250, beim("werk", "Werkstatt"), fill=WEISS, size=30, anker="m"),
    # Bruno
    peep_voll("BR_ruhig_r", BRX, BODEN, FH, "bruno", bis="b1"),
    *redet("BR_redet_r", BRX, BODEN, FH, "b1", "k1"),
    peep_voll("BR_zufrieden_r", BRX, BODEN, FH, "k1", anim="cut"),
    pille("Bruno", BRX, BODEN + 22, "bruno", fill=GRAU, size=30, anker="m", d=0.2),
    ficon("tabler", "battery-vertical", 330, 580, 70, beim("bruno", "Akkus"), fuell=WEISS, bis="b1"),
    pille("Akku fehlt", 470, 520, beim("bruno", "Akkus"), fill=WEISS, size=26, anker="m", bis="b1"),
    # Kim und Tara
    peep_voll("KI_ruhig", KIX, BODEN, FH, "zwei", bis="k1"),
    *redet("KI_redet", KIX, BODEN, FH, "k1", "laden"),
    pille("Kim", KIX, BODEN + 22, "zwei", fill=ROT, size=30, anker="m", d=0.2),
    peep_voll("TA_ruhig", TAX, BODEN, FH, "zwei", d=0.25, bis=beim("k1", "Tara")),
    peep_voll("TA_cool", TAX, BODEN, FH, beim("k1", "Tara"), anim="cut"),
    pille("Tara", TAX, BODEN + 22, "zwei", fill=LILA, size=30, anker="m", d=0.45),
    # Auftrag: zwei Akkus, zweihundert Euro
    blase("sprech", 720, 200, "b1", 960, 190, inhalt=["Holt mir zwei Akkus aus Ohms Laden.", "Ich zahle euch zweihundert Euro."],
          textsize=31, figur=BRR, bis="k1"),
    ficon("tabler", "battery-vertical-charging", 980, 700, 80, beim("b1", "Akkus"), fuell=GRUEN),
    ficon("tabler", "battery-vertical-charging", 1070, 700, 80, beim("b1", "Akkus"), fuell=GRUEN, d=0.1),
    pille("200 €", 1025, 740, beim("b1", "zweihundert"), fill=GELB, size=34, anker="m"),
    blase("sprech", 640, 200, "k1", 1280, 190, inhalt=["Abgemacht. Tara lenkt ihn ab,", "ich packe ein."], textsize=32,
          figur=KIR, bis="laden"),
])

# B Fall: Fahrradladen ------------------------------------------------------------------------------------------------------
DX, OHX, TBX, KBX = 190, 560, 870, 1180          # Tür, Ohm, Tara, Kim
RG0, RG1, RY1, RY2 = 1380, 1840, 560, 760        # Regal: x-Bereich, Böden
AKX = [1440, 1550, 1660, 1770]                  # Akkus auf dem oberen Boden
folie([("laden", "Fall · Im Fahrradladen"), ("ecke", "Fall · Ohm bemerkt die Lücke")], [
    pille("Fahrradladen Ohm", 960, 40, "laden", fill=GRUEN, size=44, anker="m"),
    linienzug([(60, BODEN), (1860, BODEN)], "laden", breite=7, farbe=INK),
    # Ladentür mit Glocke
    ficon("tabler", "door", DX, BODEN - 2, 300, "laden", fuell=BLAU, bis="raus"),
    szene(ficon("tabler", "door-exit", DX, BODEN - 2, 300, "raus", fuell=BLAU, anim="cut"), "009glocke*", 0.8, versatz=-0.1),
    ficon("tabler", "bell", DX + 20, 450, 60, "laden", fuell=GELB, d=0.3, bis="raus"),
    ficon("tabler", "bell-ringing", DX + 20, 450, 70, "raus", fuell=GELB, anim="cut", bis="ecke"),
    # Regal mit Akkus und Helmen
    linienzug([(RG0, RY1), (RG1, RY1)], "laden", breite=7, farbe=INK),
    linienzug([(RG0, RY2), (RG1, RY2)], "laden", breite=7, farbe=INK),
    linienzug([(RG0, 360), (RG0, BODEN)], "laden", breite=7, farbe=INK),
    linienzug([(RG1, 360), (RG1, BODEN)], "laden", breite=7, farbe=INK),
    *[ficon("tabler", "battery-vertical-charging", x, RY1 - 6, 86, "laden", fuell=GRUEN, d=0.1 * i,
            bis=(beim("einpack", "Akkus") if i in (1, 2) else None)) for i, x in enumerate(AKX)],
    *[ficon("tabler", "helmet", x, RY2 - 6, 100, "laden", fuell=c, d=0.3 + 0.1 * i) for i, (x, c) in
      enumerate([(1470, ROT), (1610, BLAU), (1750, GELB)])],
    pille("E-Bike-Akkus", (RG0 + RG1) // 2, 380, "laden", fill=WEISS, size=28, anker="m", d=0.5),
    ring((AKX[1] + AKX[2]) // 2, RY1 - 45, 130, 70, "ecke", farbe=DROT, breite=7),
    pille("Lücke!", (AKX[1] + AKX[2]) // 2, 610, "ecke", fill=ROT, size=32, anker="m", d=0.2),
    # Ohm
    *fig("OH", OHX, BODEN, FH, [("laden", "ruhig_r"), ("ablenk", "freundlich_r"), ("ecke", "schreck_r")]),
    pille("Herr Ohm", OHX, BODEN + 22, "laden", fill=GRUEN, size=30, anker="m", d=0.2),
    # Tara lenkt ab (Gespräch über Helme)
    *[mit_bis(e, "raus") for e in fig("TA", TBX, BODEN, FH, [("ablenk", "freundlich")])],
    ficon("tabler", "helmet", (OHX + TBX) // 2, 640, 100, beim("ablenk", "Helme"), fuell=LILA, bis="raus"),
    pille("Gespräch über Helme", (OHX + TBX) // 2, 250, beim("ablenk", "Helme"), fill=WEISS, size=30, anker="m", bis="raus"),
    pille("Tara", TBX, BODEN + 22, "ablenk", fill=LILA, size=30, anker="m", d=0.2, bis="raus"),
    # Kim packt ein
    *[mit_bis(e, "raus") for e in fig("KI", KBX, BODEN, FH, [("ablenk", "ruhig_r"), ("einpack", "cool_r")], d=0.3)],
    pille("Kim", KBX, BODEN + 22, "ablenk", fill=ROT, size=30, anker="m", d=0.5, bis="raus"),
    ficon("tabler", "backpack", KBX + 150, BODEN - 2, 100, "ablenk", fuell=ROT, d=0.5, bis="raus"),
    ficon("tabler", "battery-vertical-charging", KBX + 150, BODEN - 120, 60, beim("einpack", "Akkus"), fuell=GRUEN, bis="raus"),
    pille("2 Akkus im Rucksack", KBX, 300, beim("einpack", "Rucksack"), fill=GELB, size=30, anker="m", bis="raus"),
    pille("Kim und Tara verlassen den Laden", 960, 160, "raus", fill=WEISS, size=32, anker="m", d=0.2, bis="ecke"),
])

# C Fall: Flucht an der Ecke ---------------------------------------------------------------------------------------------------
OC1, OC2, KC1, KC2, TC1, TC2 = 640, 900, 1180, 1760, 1500, 1500
OHR = ("OH_ruft_r", OC1, BODEN, FH)
folie([("o1", "Fall · Flucht an der Ecke")], [
    linienzug([(60, BODEN), (1860, BODEN)], "o1", breite=7, farbe=INK),
    ficon("tabler", "building", 200, BODEN - 2, 300, "o1", fuell=GELB, nebenfarbe=WEISS),
    pille("Ecke", 200, 440, "o1", fill=WEISS, size=30, anker="m", d=0.2),
    # Ohm ruft und läuft hinterher, packt zu, stürzt
    *redet("OH_ruft_r", OC1, BODEN, FH, "o1", "reisst"),
    peep_voll("OH_ruft_r", OC2, BODEN, FH, "reisst", anim="cut", bis="stoss"),
    szene(peep_voll("OH_sitzt_r", OC2, BODEN, SITZ, "stoss", anim="cut", bis="vorbei"), "009sturz*", 0.9, versatz=-0.22),
    peep_voll("OH_sitzt_schreck_r", OC2, BODEN, SITZ, "vorbei", anim="cut"),
    pille("Ohm", OC1, BODEN + 22, "o1", fill=GRUEN, size=30, anker="m", d=0.2, bis="reisst"),
    pille("Ohm", OC2, BODEN + 22, "reisst", fill=GRUEN, size=30, anker="m", bis="stoss"),
    pille("Ohm", OC2, BODEN + 22, "stoss", fill=GRUEN, size=30, anker="m"),
    blase("sprech", 560, 170, "o1", 760, 200, inhalt=["Halt! Das sind", "meine Akkus!"], textsize=36, figur=OHR, bis="reisst"),
    # Rucksack: erst bei Kim, dann bei Ohm
    ficon("tabler", "backpack", KC1 + 150, BODEN - 2, 100, "o1", fuell=ROT, bis="reisst"),
    ficon("tabler", "backpack", OC2 - 120, 730, 100, "reisst", fuell=ROT, anim="cut", bis="stoss"),
    ficon("tabler", "backpack", OC2 - 190, BODEN - 2, 100, "stoss", fuell=ROT, anim="cut"),
    pille("Rucksack zurück bei Ohm", 600, 430, beim("reisst", "Rucksack"), fill=WEISS, size=30, anker="m", bis="stoss"),
    ficon("tabler", "hand-stop", (OC2 + KC1) // 2, 560, 80, "arm", fuell=GELB, bis="stoss"),
    pille("hält Kim am Arm fest", (OC2 + KC1) // 2, 250, "arm", fill=WEISS, size=30, anker="m", bis="stoss"),
    pille("Kim will nur noch weg", KC1 + 120, 330, beim("arm", "Kim"), fill=GELB, size=30, anker="m", bis="stoss"),
    # Kim
    peep_voll("KI_schreck", KC1, BODEN, FH, "o1", bis="reisst"),
    peep_voll("KI_wuetend", KC1, BODEN, FH, "reisst", anim="cut", bis="stoss"),
    peep_voll("KI_wuetend", KC1, BODEN, FH, "stoss", anim="cut", bis="flasche"),
    peep_voll("KI_schreck_r", KC2, BODEN, FH, "flasche", anim="cut"),
    pille("Kim", KC1, BODEN + 22, "o1", fill=ROT, size=30, anker="m", d=0.2, bis="flasche"),
    pille("Kim", KC2, BODEN + 22, "flasche", fill=ROT, size=30, anker="m"),
    pille("stößt Ohm weg", (OC2 + KC1) // 2, 300, "stoss", fill=WEISS, size=30, anker="m", bis="flasche"),
    pille("Prellung am Ellenbogen", OC2, 470, beim("stoss", "prellt"), fill=ROT, size=28, anker="m"),
    pille("Kim flieht", KC2, 330, "flasche", fill=WEISS, size=28, anker="m"),
    # Tara wirft die Flasche
    peep_voll("TA_ertappt", TC1, BODEN, FH, "o1", d=0.3, bis="flasche"),
    peep_voll("TA_wuetend", TC2, BODEN, FH, "flasche", anim="cut"),
    pille("Tara", TC1, BODEN + 22, "o1", fill=LILA, size=30, anker="m", d=0.5),
    ficon("ph", "beer-bottle", TC2 - 160, 560, 80, beim("flasche", "Glasflasche"), fuell=GRUEN, spiegeln=True, bis="vorbei"),
    pfeil(TC2 - 200, 540, OC2 + 70, 640, beim("flasche", "Kopf"), breite=8, kopf=30, farbe=DROT, bis="vorbei"),
    pfeil(TC2 - 200, 540, 520, 720, "vorbei", breite=8, kopf=30, farbe=DROT),
    ficon("ph", "beer-bottle", 470, BODEN - 2, 80, beim("vorbei", "knapp"), fuell=GRUEN, spiegeln=True),
    pille("knapp vorbei", 470, 640, beim("vorbei", "knapp"), fill=GELB, size=30, anker="m"),
])

# D Klausurfrage ----------------------------------------------------------------------------------------------------------------
FR, FB = 420, 930
PX = {"KI": 1365, "TA": 1600, "BR": 1805}         # Reihenfolge-Leiste rechts (D, G1–G3)
NAME = {"KI": ("Kim", ROT), "TA": ("Tara", LILA), "BR": ("Bruno", GRAU)}


def leiste(cue, folgen, d=0.0):
    """Kim, Tara, Bruno rechts neben der Tafel; folgen = {Person: [(cue, suffix)]}."""
    els = []
    for k, p in enumerate(("KI", "TA", "BR")):
        els += fig(p, PX[p], FB, FR, folgen[p], d=d + 0.1 * k)
        els.append(pille(NAME[p][0], PX[p], FB + 22, cue, fill=NAME[p][1], size=28, anker="m", d=d + 0.2 + 0.1 * k))
    return els


def platz(p, nr, cue, fill=GELB):
    return pille(str(nr), PX[p], 420, cue, fill=fill, size=40, anker="m")


ORT = [("tools", "Werkstatt", GRAU), ("building-store", "Laden", GRUEN), ("map-pin", "Ecke", ROT)]
folie([("frage", "Fallfrage · Wen prüfst du zuerst?")], [
    *tafel("frage", "Klausur · Strafrecht"),
    ficon("tabler", "clock", 1100, 170, 80, "frage", fuell=GELB, d=0.3),
    z("Bearbeitervermerk:", 110, 200, "frage", "Bold", 38),
    z("Wie haben sich Kim, Tara und Bruno", 110, 260, beim("frage", "Wie"), size=38),
    z("strafbar gemacht?", 110, 315, beim("frage", "strafbar"), size=38),
    pille("3 Beteiligte", 110, 420, beim("orte", "Beteiligte"), fill=GELB, size=34),
    *[ficon("tabler", ic, 230 + 330 * i, 650, 110, beim("orte", "Orte"), fuell=f, d=0.15 * i) for i, (ic, _, f) in enumerate(ORT)],
    *[pille(t, 230 + 330 * i, 670, beim("orte", "Orte"), fill=WEISS, size=28, anker="m", d=0.15 * i) for i, (_, t, _) in enumerate(ORT)],
    pille("Wen prüfst du zuerst?", 110, 780, beim("orte", "Wen"), fill=PINK, size=38),
    *leiste("frage", {"KI": [("frage", "ruhig"), (beim("orte", "Wen"), "denkt")],
                      "TA": [("frage", "ruhig"), (beim("orte", "Wen"), "denkt")],
                      "BR": [("frage", "ruhig"), (beim("orte", "Wen"), "denkt")]}),
])

# E Sachverhalt -------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Bruno bittet Kim und Tara in seiner Werkstatt, ihm zwei E-Bike-Akkus aus dem Fahrradladen von Ohm zu holen; er zahlt "
    "200 €. Die beiden sind einverstanden: Tara soll Ohm ablenken, Kim einpacken, das Geld wollen sie teilen.",
    "Im Laden verwickelt Tara Ohm in ein Gespräch, Kim steckt zwei Akkus in ihren Rucksack, beide gehen. Ohm rennt hinterher, "
    "reißt Kim an der Ecke den Rucksack vom Rücken und hält sie am Arm fest. Kim will nur noch fliehen und stößt Ohm weg; er "
    "stürzt und prellt sich den Ellenbogen. Tara wirft im Weglaufen wütend eine Glasflasche nach Ohms Kopf, um ihn zu treffen; "
    "sie fliegt knapp vorbei. Eine weitere Flasche hat Tara nicht. Für die Flucht gab es keine Absprache. Ohm stellt Strafantrag.",
    "(Frei erfundener Übungsfall.)",
], "Wie haben sich Kim, Tara und Bruno strafbar gemacht?")

# F Tatkomplexe bilden -----------------------------------------------------------------------------------------------------------
TLX, TY = 1420, {0: 200, 1: 515, 2: 765}
folie([("tk", "Aufbau › Tatkomplexe bilden"), ("auftrag", "Aufbau › Brunos Auftrag: kein eigener Tatkomplex"),
       ("konv", "Aufbau › Klausurregel, kein Gesetz")], [
    *tafel("tk", "Tatkomplexe bilden"),
    z("Ordnung nach der Zeit", 110, 195, beim("tk", "Zeit"), "Bold", 38),
    fl_block(110, 265, 1040, 90, BLAU, "tk1", [("1. Tatkomplex: Diebstahl im Laden", "Bold", 36, INK)]),
    fl_block(110, 375, 1040, 90, ORANGE, "tk2", [("2. Tatkomplex: Flucht an der Ecke", "Bold", 36, INK)]),
    z("Brunos Auftrag in der Werkstatt:", 110, 510, "auftrag", "Bold", 36),
    z("kein eigener Tatkomplex", 150, 562, beim("auftrag", "keinen"), size=36),
    z("→ Anstiftung bei der Haupttat prüfen", 150, 622, "beitat", size=36),
    pille("Klausurregel, kein Gesetz", 110, 720, beim("konv", "keinem"), fill=PINK, size=34),
    z("macht das Gutachten lesbar", 600, 732, beim("konv", "lesbar"), size=30, farbe=TEXT),
    # Zeitleiste rechts
    pfeil(1285, 140, 1285, 850, "tk", breite=8, kopf=28, farbe=INK),
    pille("Zeit", 1285, 860, "tk", fill=WEISS, size=26, anker="m", d=0.2),
    *[ficon("tabler", ic, TLX, TY[i] + 50, 100, "tk", fuell=f, d=0.15 * i) for i, (ic, _, f) in enumerate(ORT)],
    *[pille(t, TLX + 70, TY[i] - 22, "tk", fill=WEISS, size=28, d=0.15 * i) for i, (_, t, _) in enumerate(ORT)],
    ring(TLX + 110, TY[1] + 2, 190, 85, "tk1", farbe=BLAU, breite=7),
    pille("TK 1", 1735, TY[1] - 28, "tk1", fill=BLAU, size=32),
    ring(TLX + 110, TY[2] + 2, 190, 85, "tk2", farbe=ORANGE, breite=7),
    pille("TK 2", 1735, TY[2] - 28, "tk2", fill=ORANGE, size=32),
    pille("kein eigener TK", TLX + 70, TY[0] + 45, beim("auftrag", "keinen"), fill=GELB, size=26),
    pfeil(TLX - 75, TY[0] + 70, TLX - 75, TY[1] - 50, "beitat", breite=8, kopf=28, farbe=BLAU),
    pille("Anstiftung: bei TK 1", TLX + 70, TY[0] + 125, "beitat", fill=BLAU, size=26),
])

# G1 Tatkomplex 1: A. Kim ---------------------------------------------------------------------------------------------------------
Q1, Q2 = "„… in der Absicht wegnimmt, die Sache sich", "oder einem Dritten rechtswidrig zuzueignen“"
folie([("naechst", f"{TK1} › Tatnächste zuerst"), ("kim", f"{TK1} › A. Kim"), ("p242", f"{TK1} › A. Kim › § 242 I StGB")], [
    *tafel("naechst", "1. Tatkomplex: Diebstahl im Laden", size=46),
    z("Wer steht der Tat am nächsten?", 110, 195, "naechst", "Bold", 38),
    z("A. Kim: hat die Akkus selbst weggenommen", 110, 280, "kim", "Bold", 36),
    z("I. Diebstahl, § 242 I StGB", 150, 360, "p242", "Bold", 38),
    z(Q1, 150, 440, "dritter", size=32, farbe=TEXT), z(Q2, 170, 485, "dritter", size=32, farbe=TEXT),
    wortring(Q2, "einem Dritten", 170, 485, 32, "Regular", beim("dritter", "Absicht")),
    ok(175, 580, beim("dritter", "genügt"), gr=22), z("Akkus für Bruno: Drittzueignung genügt", 215, 560, beim("dritter", "genügt"), size=34),
    *leiste("naechst", {"KI": [("naechst", "ruhig"), ("kim", "cool")], "TA": [("naechst", "ruhig")], "BR": [("naechst", "ruhig")]}),
    platz("KI", 1, "kim"),
    ficon("tabler", "backpack", PX["KI"] + 80, 475, 70, "kim", fuell=ROT, d=0.2),
])

# G2 Tatkomplex 1: B. Tara --------------------------------------------------------------------------------------------------------
P25A, P25B = "§ 25 II StGB: „Begehen mehrere die Straftat", "gemeinschaftlich, so wird jeder als Täter bestraft“"
folie([("tara", f"{TK1} › B. Tara"), ("p25", f"{TK1} › B. Tara › §§ 242 I, 25 II StGB"),
       ("getrennt", f"{TK1} › Mittäter getrennt prüfen")], [
    *tafel("tara", "1. Tatkomplex · B. Tara", size=46),
    z("nichts eingepackt, aber nach Plan abgelenkt", 110, 195, beim("tara", "Sie"), "Bold", 34),
    z("und soll die Hälfte bekommen", 110, 245, beim("tara", "Hälfte"), "Bold", 34),
    z(P25A, 110, 320, "p25", size=32, farbe=TEXT), z(P25B, 130, 365, "p25", size=32, farbe=TEXT),
    ok(135, 455, beim("p25", "zugerechnet"), gr=22),
    z("Kims Wegnahme wird zugerechnet: Mittäterin", 175, 435, beim("p25", "zugerechnet"), size=34),
    fl_block(110, 530, 1040, 130, GELB, "getrennt", [("unterschiedliche Beiträge: getrennt prüfen,", "Bold", 34, INK),
                                                   ("Kim zuerst", "Bold", 34, INK)]),
    z("gleiche Beiträge: gemeinsame Prüfung möglich", 110, 700, "gemeinsam", size=34, farbe=TEXT),
    *leiste("tara", {"KI": [("tara", "ruhig")], "TA": [("tara", "ruhig"), ("p25", "cool")], "BR": [("tara", "ruhig")]}),
    platz("KI", 1, "tara", fill=WEISS), platz("TA", 2, "p25"),
    ficon("tabler", "helmet", PX["TA"] + 75, 470, 70, beim("tara", "abgelenkt"), fuell=LILA),
    ficon("tabler", "backpack", PX["KI"] + 80, 475, 70, "tara", fuell=ROT),
    pille("Mittäterinnen", (PX["KI"] + PX["TA"]) // 2, 300, beim("p25", "Mittäterin"), fill=GELB, size=30, anker="m"),
])

# G3 Tatkomplex 1: C. Bruno --------------------------------------------------------------------------------------------------------
P26 = ["§ 26 StGB: „Als Anstifter wird gleich einem Täter", "bestraft, wer vorsätzlich einen anderen zu dessen",
       "vorsätzlich begangener rechtswidriger Tat", "bestimmt hat.“"]
folie([("bruno2", f"{TK1} › C. Bruno"), ("p26", f"{TK1} › C. Bruno › §§ 242 I, 26 StGB"),
       ("tvt", "Aufbau › Täter vor Teilnehmer")], [
    *tafel("bruno2", "1. Tatkomplex · C. Bruno", size=46),
    z("war gar nicht im Laden", 110, 195, beim("bruno2", "Er"), "Bold", 36),
    *[z(t, 110 + (20 if i else 0), 280 + 48 * i, "p26", size=33, farbe=TEXT) for i, t in enumerate(P26)],
    wortring(P26[2], "vorsätzlich begangener rechtswidriger Tat", 130, 376, 33, "Regular", beim("p26", "vorsätzlich", nr=2)),
    z("ohne geprüfte Haupttat keine Anstiftung", 110, 540, "haupt", "Bold", 36),
    fl_block(110, 630, 1040, 110, GRUEN, "tvt", [("Täter vor Teilnehmer", "ExtraBold", 42, INK)]),
    *leiste("bruno2", {"KI": [("bruno2", "ruhig")], "TA": [("bruno2", "ruhig")],
                       "BR": [("bruno2", "ruhig"), ("p26", "ertappt")]}),
    platz("KI", 1, "bruno2", fill=WEISS), platz("TA", 2, "bruno2", fill=WEISS), platz("BR", 3, "tvt"),
    pille("Haupttat: Diebstahl", (PX["KI"] + PX["TA"]) // 2, 300, "haupt", fill=BLAU, size=28, anker="m"),
    pfeil(PX["BR"], 405, PX["TA"] + 40, 365, "haupt", breite=7, kopf=26, farbe=INK),
])

# H1 Tatkomplex 2: A. Kim, § 252 -----------------------------------------------------------------------------------------------------
OHT, KIT = 1490, 1750                            # Ohm am Boden, Kim stehend (Tatkomplex 2)
Q252A, Q252B = "„… Gewalt verübt oder Drohungen … anwendet, um", "sich im Besitz des gestohlenen Gutes zu erhalten“"
folie([("flucht", f"{TK2} › A. Kim"), ("schwer", f"{TK2} › A. Kim › I. § 252 StGB"),
       ("beute", f"{TK2} › A. Kim › § 252 StGB: Beute schon weg")], [
    *tafel("flucht", "2. Tatkomplex: Flucht · A. Kim", size=46),
    pille("schwerstes Delikt zuerst", 110, 180, beim("schwer", "schwersten"), fill=PINK, size=32),
    z("I. Räuberischer Diebstahl, § 252 StGB", 110, 270, beim("schwer", "räuberischer"), "Bold", 38),
    z(Q252A, 150, 345, "p252", size=32, farbe=TEXT), z(Q252B, 170, 390, "p252", size=32, farbe=TEXT),
    wortring(Q252B, "im Besitz des gestohlenen Gutes", 170, 390, 32, "Regular", beim("p252", "Besitz")),
    nein(175, 495, "beute", gr=22), z("Akkus schon wieder bei Ohm", 215, 475, "beute", size=36),
    z("Kim will nur fliehen", 215, 530, beim("beute", "Kim"), size=36),
    *plusminus("§ 252 StGB", 110, 620, beim("beute", "fliehen"), False, size=38, stil="Bold"),
    *fig("OH", OHT, FB, SITZ * FR // FH, [("flucht", "sitzt_r")]),
    pille("Ohm", OHT, FB + 22, "flucht", fill=GRUEN, size=28, anker="m", d=0.2),
    *fig("KI", KIT, FB, FR, [("flucht", "wuetend"), ("beute", "ertappt")], d=0.1),
    pille("Kim", KIT, FB + 22, "flucht", fill=ROT, size=28, anker="m", d=0.3),
    ficon("tabler", "backpack", OHT - 160, FB - 2, 90, "flucht", fuell=ROT, d=0.2),
    ring(OHT - 160, FB - 45, 70, 60, beim("beute", "Akkus"), farbe=DROT, breite=6),
    pille("Beute bei Ohm", OHT - 60, 620, beim("beute", "Akkus"), fill=WEISS, size=28, anker="m"),
])

# H2 Tatkomplex 2: A. Kim, §§ 223, 240, Rechtswidrigkeit --------------------------------------------------------------------------
folie([("leicht", f"{TK2} › A. Kim › leichtere Delikte"), ("p223", f"{TK2} › A. Kim › II. § 223 I StGB"),
       ("p240", f"{TK2} › A. Kim › III. § 240 I StGB"), ("p127", f"{TK2} › A. Kim › RW: § 127 I StPO")], [
    *tafel("leicht", "2. Tatkomplex · A. Kim", size=46),
    z("Danach die leichteren Delikte", 110, 190, "leicht", "Bold", 36),
    ok(135, 290, beim("p223", "Körperverletzung"), gr=22), z("II. Körperverletzung, § 223 I StGB", 175, 270, beim("p223", "Körperverletzung"), "Bold", 36),
    z("Stoß, Sturz, Prellung", 215, 325, beim("p223", "Körperverletzung"), size=32, farbe=TEXT),
    ok(135, 410, beim("p240", "Nötigung"), gr=22), z("III. Nötigung, § 240 I StGB", 175, 390, beim("p240", "Nötigung"), "Bold", 36),
    z("Ohm sollte loslassen", 215, 445, beim("p240", "loslassen"), size=32, farbe=TEXT),
    z("Rechtswidrigkeit: keine Notwehr", 175, 530, "p127", "Bold", 36),
    z("Ohm durfte Kim festhalten:", 215, 590, beim("p127", "Ohm"), size=32, farbe=TEXT),
    z("§ 127 I StPO (vorläufige Festnahme)", 215, 635, beim("p127", "Paragraf"), size=32, farbe=TEXT),
    *fig("OH", OHT, FB, SITZ * FR // FH, [("leicht", "sitzt_r")]),
    pille("Ohm", OHT, FB + 22, "leicht", fill=GRUEN, size=28, anker="m", d=0.2),
    *fig("KI", KIT, FB, FR, [("leicht", "denkt"), ("p127", "ertappt")], d=0.1),
    pille("Kim", KIT, FB + 22, "leicht", fill=ROT, size=28, anker="m", d=0.3),
    ficon("tabler", "backpack", OHT - 160, FB - 2, 90, "leicht", fuell=ROT, d=0.2),
    pille("Prellung", OHT, 600, beim("p223", "Körperverletzung"), fill=ROT, size=28, anker="m"),
    ficon("tabler", "hand-stop", (OHT + KIT) // 2, 420, 80, beim("p240", "Nötigung"), fuell=GELB),
    pille("loslassen!", (OHT + KIT) // 2, 440, beim("p240", "loslassen"), fill=WEISS, size=28, anker="m"),
    pille("§ 127 I StPO", (OHT + KIT) // 2, 250, beim("p127", "Paragraf"), fill=GRUEN, size=30, anker="m"),
])

# H3 Tatkomplex 2: B. Tara, Versuch ------------------------------------------------------------------------------------------------
TAT = 1730
folie([("tara3", f"{TK2} › B. Tara"), ("versuch", f"{TK2} › B. Tara › §§ 223 I, 224 I Nr. 2, 22, 23 I StGB"),
       ("p224b", f"{TK2} › B. Tara › Strafbarkeit des Versuchs, § 224 II")], [
    *tafel("tara3", "2. Tatkomplex · B. Tara", size=46),
    pille("Vollendetes vor Versuchtem", 110, 180, beim("vollendet", "Vollendetes"), fill=PINK, size=32),
    nein(135, 300, beim("vollendet", "nichts"), gr=22), z("vollendet? Flasche hat Ohm verfehlt", 175, 280, beim("vollendet", "nichts"), size=36),
    z("Versuchte gefährliche Körperverletzung,", 110, 365, "versuch", "Bold", 36),
    z("§§ 223 I, 224 I Nr. 2, 22, 23 I StGB", 150, 415, "versuch", "Bold", 34),
    z("Tatentschluss: Flasche als gefährliches Werkzeug", 150, 480, "p224", size=32, farbe=TEXT),
    fl_block(110, 555, 1040, 100, GELB, "quali", [("Qualifikation und Grunddelikt zusammen prüfen", "Bold", 34, INK)]),
    z("§ 224 II: „Der Versuch ist strafbar.“", 110, 700, "p224b", "Bold", 36),
    z("(Vergehen: § 23 I verlangt eine ausdrückliche Regel)", 150, 755, "p224b", size=28, farbe=TEXT),
    *fig("OH", OHT - 60, FB, SITZ * FR // FH, [("tara3", "sitzt_r")]),
    pille("Ohm", OHT - 60, FB + 22, "tara3", fill=GRUEN, size=28, anker="m", d=0.2),
    *fig("TA", TAT, FB, FR, [("tara3", "wuetend"), ("vollendet", "ertappt")], d=0.1),
    pille("Tara", TAT, FB + 22, "tara3", fill=LILA, size=28, anker="m", d=0.3),
    ficon("ph", "beer-bottle", 1560, 300, 80, "tara3", fuell=GRUEN, spiegeln=True, d=0.3),
    pfeil(1530, 320, 1330, 560, "tara3", breite=7, kopf=26, farbe=DROT, d=0.4),
    pille("verfehlt", 1340, 300, beim("vollendet", "verfehlt"), fill=ROT, size=28, anker="m"),
    pille("gefährliches Werkzeug", 1560, 160, "p224", fill=GELB, size=28, anker="m"),
])

# H4 Tatkomplex 2: keine Zurechnung, Bruno außen vor ----------------------------------------------------------------------------------
folie([("zurech", f"{TK2} › keine wechselseitige Zurechnung"), ("bruno3", f"{TK2} › Bruno: kein Auftrag zur Gewalt")], [
    *tafel("zurech", "2. Tatkomplex · Zurechnung?", size=46),
    nein(135, 220, beim("zurech", "Kims"), gr=22), z("Kims Stoß → nicht für Tara", 175, 200, beim("zurech", "Kims"), size=36),
    nein(135, 290, beim("zurech", "umgekehrt"), gr=22), z("Taras Wurf → nicht für Kim", 175, 270, beim("zurech", "umgekehrt"), size=36),
    z("kein gemeinsamer Plan für die Flucht", 175, 340, beim("zurech", "keinen"), "Bold", 36),
    nein(135, 470, beim("bruno3", "Gewalt"), gr=22), z("Bruno: Gewalt nicht Teil seines Auftrags", 175, 450, beim("bruno3", "Gewalt"), "Bold", 36),
    *leiste("zurech", {"KI": [("zurech", "denkt")], "TA": [("zurech", "denkt")], "BR": [("zurech", "ruhig"), ("bruno3", "zufrieden")]}),
    ring((PX["KI"] + PX["TA"]) // 2, 250, 190, 70, beim("zurech", "keinen"), farbe=DROT, breite=6),
    pille("kein Plan", (PX["KI"] + PX["TA"]) // 2, 220, beim("zurech", "keinen"), fill=WEISS, size=28, anker="m"),
    pille("kein Auftrag zur Gewalt", 1880, 420, beim("bruno3", "Gewalt"), fill=WEISS, size=28, anker="r"),
])

# I Konkurrenzen ----------------------------------------------------------------------------------------------------------------------
KX0, KW = 1270, 600
folie([("konk", "Konkurrenzen"), ("p52", "Konkurrenzen › Tateinheit, § 52 StGB"), ("p53", "Konkurrenzen › Tatmehrheit, § 53 StGB")], [
    *tafel("konk", "Konkurrenzen"),
    z("§ 52 I: „Verletzt dieselbe Handlung mehrere", 110, 190, "p52", size=32, farbe=TEXT),
    z("Strafgesetze …, so wird nur auf eine Strafe erkannt.“", 130, 235, "p52", size=32, farbe=TEXT),
    ok(135, 320, beim("p52", "Tateinheit"), gr=22), z("Kim: ein Stoß, §§ 223, 240 → Tateinheit", 175, 300, beim("p52", "Tateinheit"), "Bold", 34),
    z("§ 53 I: „Hat jemand mehrere Straftaten", 110, 400, "p53", size=32, farbe=TEXT),
    z("begangen …, so wird auf eine Gesamtstrafe erkannt.“", 130, 445, "p53", size=32, farbe=TEXT),
    ok(135, 530, beim("p53", "Tatmehrheit"), gr=22), z("Kim: Diebstahl und Stoß → Tatmehrheit", 175, 510, beim("p53", "Tatmehrheit"), "Bold", 34),
    ok(135, 600, "ebenso", gr=22), z("Tara: Diebstahl und Flaschenwurf → Tatmehrheit", 175, 580, "ebenso", "Bold", 32),
    # Diagramm rechts
    pille("Kim", KX0, 110, "konk", fill=ROT, size=32),
    fl_block(KX0, 180, 240, 110, BLAU, "konk", [("TK 1", "Bold", 28, INK), ("§ 242", "Bold", 32, INK)], d=0.2),
    fl_block(KX0 + 360, 180, 240, 110, ORANGE, "konk", [("TK 2: Stoß", "Bold", 28, INK), ("§§ 223, 240", "Bold", 30, INK)], d=0.3),
    pille("§ 52", KX0 + 480, 310, beim("p52", "Tateinheit"), fill=GELB, size=30, anker="m"),
    pille("§ 53", KX0 + 300, 208, beim("p53", "Tatmehrheit"), fill=GRUEN, size=28, anker="m"),
    pille("Tara", KX0, 470, "ebenso", fill=LILA, size=32),
    fl_block(KX0, 540, 240, 110, BLAU, "ebenso", [("TK 1", "Bold", 28, INK), ("§§ 242, 25 II", "Bold", 28, INK)], d=0.1),
    fl_block(KX0 + 360, 540, 240, 110, ORANGE, "ebenso", [("TK 2: Wurf", "Bold", 28, INK), ("§§ 224, 22", "Bold", 28, INK)], d=0.2),
    pille("§ 53", KX0 + 300, 568, beim("ebenso", "Diebstahl"), fill=GRUEN, size=28, anker="m"),
])

# J Klausurtipp (Lexi) ---------------------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · Aufbau zeigen, nicht erklären")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Aufbau nicht erklären, sondern zeigen", 200, 200, beim("tipp", "Erkläre"), "Bold", 36),
    z("Überschrift = Tatkomplex, Person, Delikt:", 150, 300, "t1", "Bold", 34),
    z("1. Tatkomplex: Diebstahl im Laden", 190, 365, "t1", size=34),
    z("A. Strafbarkeit der Kim", 230, 420, beim("t1", "Person"), size=34),
    z("I. Diebstahl, § 242 I StGB", 270, 475, beim("t1", "Delikt"), size=34),
    z("C. Bruno: Haupttat steht fest (s. o.)", 190, 580, "t2", "Bold", 34),
    pille("nach oben verweisen", 190, 660, beim("t2", "oben"), fill=GELB, size=32),
    *redet("LX_warnt", LXX, FB, 560, "tipp", "sch"),
    pille("Lexi", LXX, FB + 22, "tipp", fill=GELB, size=30, anker="m", d=0.2),
])

# K Klausurschema ----------------------------------------------------------------------------------------------------------------------
K1, K2 = 150, 210
SCH = [("s1", K1, "1. Tatkomplex: Diebstahl im Laden", "Bold", 44, INK, 195),
       ("s2", K2, "A. Kim: Diebstahl, § 242 I StGB", "Regular", 38, TEXT, 265),
       ("s3", K2, "B. Tara: Diebstahl in Mittäterschaft, §§ 242 I, 25 II StGB", "Regular", 38, TEXT, 325),
       ("s4", K2, "C. Bruno: Anstiftung zum Diebstahl, §§ 242 I, 26 StGB", "Regular", 38, TEXT, 385),
       ("s5", K1, "2. Tatkomplex: Flucht an der Ecke", "Bold", 44, INK, 480),
       ("s6", K2, "A. Kim: § 252 StGB (−); §§ 223 I, 240 I StGB in Tateinheit, § 52", "Regular", 38, TEXT, 550),
       ("s7", K2, "B. Tara: versuchte gefährliche KV, §§ 223 I, 224 I Nr. 2, II, 22, 23 I StGB", "Regular", 38, TEXT, 610),
       ("s8", K1, "Gesamtergebnis: Tatmehrheit, § 53 StGB (Kim, Tara)", "Bold", 44, INK, 710)]
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel("Klausurschema: Akku-Fall", 110, 90, "sch", 54),
    *[z(t, x, y, c, st, sz, farbe=f, rechts=1820) for c, x, t, st, sz, f, y in SCH],
])

# L Merksatz (Lexi) ---------------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Ordne erst nach der ", 0), ("Zeit", "a"), (",", 0)], [("dann nach der ", 0), ("Nähe zur Tat", "b"), (".", 0)]],
                750, 300, 52, "merke", {"a": beim("merke", "Zeit"), "b": beim("merke", "Nähe")}),
    *markertext([[("Täter vor Teilnehmer", "c")], [("Vollendung vor Versuch", "d")], [("Schweres vor Leichtem", "e")]],
                750, 480, 44, "m2", {"c": beim("m2", "Täter"), "d": beim("m2", "Vollendung"), "e": beim("m2", "Schweres")}),
    *markertext([[("Konkurrenzen zum Schluss", "f")]], 750, 720, 44, "m3", {"f": beim("m3", "Konkurrenzen")}),
    *redet("LX_erklaert", 1680, 1000, 720, "merke", lexi_bis_ende("merke")),
])
