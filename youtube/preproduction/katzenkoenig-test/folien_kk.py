"""Katzenkönig-Fall (BGHSt 35, 347, vereinfacht) – Open Peeps (LexVerse-Figma-Bibliothek), Pinselblasen, Figurenrede mit
eigenen Stimmen und Mundzuständen, Lexi bei Klausurtipp und Merksatz. Geräusche nur bei sichtbarer Handlung."""
import bausteine
from bausteine import *

bausteine.FIGORDNER = "op_kk/"
FOLIEN = bausteine.FOLIEN
K = FIG + "op_kk/"
BODEN, FH = 880, 480
BX, PX, RX = 300, 560, 1560                     # Barbara, Peter, Richard in der Wohnung


def z(text, x, y, cue, stil="Regular", size=38, farbe=INK, d=0.0, rechts=1170, **k):
    """Tafelzeile, die rechts nicht über die Karte hinausragen darf."""
    e = zeile(text, x, y, cue, stil, size, farbe=farbe, d=d, **k)
    assert e.x + e.sprite.width <= rechts, f"Zeile zu breit: {text} ({e.x + e.sprite.width:.0f} > {rechts})"
    return e


def tafel(cue, titel_, h=840, fill=WEISS):
    """Rechtstafel links, rechts bleibt Platz für die Figuren."""
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(titel_, 110, 100, cue, 50)]


# 1 Fall: Wohnung ---------------------------------------------------------------------------------------------------------
BA = ("BA_listig", BX, BODEN, FH); PE = ("PE_ernst", PX, BODEN, FH); RI = ("RI_zweifel", RX, BODEN, FH)
folie([("fall", "Fall · Barbara, Peter und Richard")], [
    titel("Der Katzenkönig", 80, 55, "fall", 70),
    linienzug([(60, BODEN), (1860, BODEN)], "fall", breite=7, farbe=INK),
    ficon("tabler", "candle", 900, BODEN - 2, 90, "fall", fuell=GELB, d=0.6),
    ficon("tabler", "crystal-ball", 1010, BODEN - 2, 110, "fall", fuell=LILA, d=0.8),
    # Barbara
    peep_voll("BA_ruhig", BX, BODEN, FH, "fall", bis="b1"),
    *redet("BA_listig", BX, BODEN, FH, "b1", "p1"),
    peep_voll("BA_listig", BX, BODEN, FH, "p1", anim="cut", bis="motiv"),
    peep_voll("BA_zufrieden", BX, BODEN, FH, "motiv", anim="cut", bis="b2"),
    *redet("BA_drohend", BX, BODEN, FH, "b2", "tat"),
    pille("Barbara", BX, BODEN + 22, "fall", fill=LILA, size=30, anker="m", d=0.2),
    # Peter
    peep_voll("PE_ruhig", PX, BODEN, FH, "fall", d=0.3, bis="p1"),
    *redet("PE_ernst", PX, BODEN, FH, "p1", "motiv"),
    peep_voll("PE_ruhig", PX, BODEN, FH, "motiv", anim="cut"),
    pille("Peter", PX, BODEN + 22, "fall", fill=BLAU, size=30, anker="m", d=0.5),
    # Richard
    peep_voll("RI_ruhig", RX, BODEN, FH, "glaeubig", bis="kk"),
    peep_voll("RI_staunt", RX, BODEN, FH, "kk", anim="cut", bis="p1"),
    peep_voll("RI_glaubt", RX, BODEN, FH, "p1", anim="cut", bis="r1"),
    *redet("RI_zweifel", RX, BODEN, FH, "r1", "b2"),
    peep_voll("RI_zweifel", RX, BODEN, FH, "b2", anim="cut"),
    pille("Richard", RX, BODEN + 22, "glaeubig", fill=GRUEN, size=30, anker="m", d=0.2),
    pille("leichtgläubig", RX, 300, "glaeubig", fill=GELB, size=32, anker="m", d=1.2, bis="kk"),
    # Der Katzenkönig in Richards Vorstellung
    blase("denk", 380, 300, "kk", 1440, 230, figur=("RI_staunt", RX, BODEN, FH), bis="r1"),
    ficon("tabler", "crown", 1440, 175, 90, "kk", fuell=GELB, d=0.3, bis="r1"),
    szene(ficon("tabler", "cat", 1440, 300, 130, "kk", fuell=(90, 90, 100, 255), nebenfarbe=GELB, d=0.3, bis="r1"), "miau*", 0.8),
    # Sprechblasen
    blase("sprech", 560, 200, "b1", 520, 240, inhalt=["Der Katzenkönig verlangt", "ein Menschenopfer.", "Er will Nora."],
          textsize=32, figur=BA, bis="p1"),
    blase("sprech", 540, 170, "p1", 780, 250, inhalt=["Wenn du es nicht tust, sterben", "Millionen Menschen."], textsize=31,
          figur=PE, bis="motiv"),
    blase("denk", 360, 280, "motiv", 520, 240, figur=("BA_zufrieden", BX, BODEN, FH), bis="r1"),
    bild(K + "NO_ruhig.png", 520, 330, 170, "motiv", d=0.25, bis="r1"),
    pille("Motiv: Rivalin Nora loswerden", 960, 480, "motiv", fill=ROT, size=32, anker="m", d=0.8, bis="r1"),
    blase("sprech", 480, 170, "r1", 1450, 250, inhalt=["Aber töten ist", "doch Unrecht …"], textsize=36, figur=RI, bis="b2"),
    blase("sprech", 520, 170, "b2", 560, 250, inhalt=["Nicht, wenn du damit", "Millionen rettest!"], textsize=34,
          figur=("BA_drohend", BX, BODEN, FH), bis="tat"),
])

# 2 Fall: Noras Laden -----------------------------------------------------------------------------------------------------
NX, RL = 1330, 1010
LIEGT = Image.open(K + "NO_liegt.png"); LH = int(FH * LIEGT.height / LIEGT.width)


def hand(name, cx, unten, hoehe):
    """Vorderste Hand (rechter Rand) der Figur im Band 35–55 % der Höhe – dort sitzt ein gehaltenes Requisit."""
    e = peep_voll(name, cx, unten, hoehe, "_")
    a = np.asarray(e.sprite)[:, :, 3] > 20
    y0, y1 = int(a.shape[0] * 0.35), int(a.shape[0] * 0.55)
    xs = [np.nonzero(r)[0].max() for r in a[y0:y1] if r.any()]
    zeile_ = y0 + int(np.argmax(xs))
    return e.x + max(xs) - 12, e.y + zeile_
folie([("tat", "Fall · In Noras Laden")], [
    titel("In Noras Laden", 80, 55, "tat", 70),
    linienzug([(60, BODEN), (1860, BODEN)], "tat", breite=7, farbe=INK),
    ficon("tabler", "building-store", 1740, BODEN - 2, 220, "tat", fuell=GELB),
    szene(ficon("tabler", "bell", 1740, 650, 64, beim("tat", "Laden"), fuell=GELB), "glocke*", 0.8),
    peep_voll("NO_arglos", NX, BODEN, FH, "tat", bis="ueberlebt"),
    pille("Nora", NX, BODEN + 22, "tat", fill=ORANGE, size=30, anker="m", d=0.2),
    szene(bewegt(peep_voll("RI_geht", RL, BODEN, FH, "tat", anim="fade", bis=beim("tat", "sticht")),
                 ("tat", 0.2), beim("tat", "Laden", ende=True), -780), "schritte*", 0.7, versatz=0.1),
    peep_voll("RI_steht", RL, BODEN, FH, beim("tat", "sticht"), anim="cut"),
    icon("fluent-emoji-high-contrast", "kitchen-knife", *hand("RI_steht", RL, BODEN, FH), 110, beim("tat", "Messer"), bis="ueberlebt"),
    pille("von hinten", NX - 170, 330, beim("tat", "hinten"), fill=ROT, size=32, anker="m", bis="ueberlebt"),
    pille("ahnt nichts", NX + 60, 400, beim("tat", "ahnt"), fill=GELB, size=32, anker="m", bis="ueberlebt"),
    szene(peep_voll("NO_liegt", NX + 50, BODEN - 4, LH, "ueberlebt", anim="cut"), "fall*", 0.9),
    icon("fluent-emoji-high-contrast", "ambulance", 1180, 330, 130, beim("ueberlebt", "schwer"), d=0.1),
    pille("überlebt schwer verletzt", NX + 60, 480, beim("ueberlebt", "schwer"), fill=ORANGE, size=34, anker="m"),
    pille("Wie haben sich Richard, Barbara und Peter strafbar gemacht?", 1100, 968, "frage", fill=PINK, size=34, anker="m"),
])

# 3 Sachverhalt -----------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Barbara und Peter haben großen Einfluss auf den leichtgläubigen Richard. Sie reden ihm ein, der „Katzenkönig“ verlange "
    "ein Menschenopfer: Richard müsse Nora töten, sonst sterben Millionen Menschen. In Wahrheit will Barbara ihre Rivalin "
    "Nora loswerden.",
    "Richard hält die Tötung zwar für Unrecht, glaubt aber, sie sei zur Rettung der vielen Menschen erlaubt. Er sticht der "
    "arglosen Nora in ihrem Laden von hinten ein Messer in den Rücken. Nora überlebt schwer verletzt.",
    "(Nach BGHSt 35, 347 – Katzenkönig-Fall; vereinfacht, Namen geändert.)",
], "Wie haben sich Richard, Barbara und Peter strafbar gemacht?")

# 4 Richard: versuchter Mord -------------------------------------------------------------------------------------------
RR, NR, BR, FR = 1420, 1720, 930, 520
folie([("r_sch", "A. Richard"), ("versuch", "A. Richard › Versuchter Mord"), ("tb", "A. Richard › Versuchter Mord › Tatentschluss, Ansetzen"),
       ("heim", "A. Richard › Versuchter Mord › Heimtücke")], [
    *tafel("r_sch", "A. Strafbarkeit Richard"),
    z("Versuchter Mord, §§ 212, 211, 22, 23 I StGB", 110, 200, "versuch", "Bold", 38),
    ok(135, 285, beim("versuch", "Nora"), gr=24), z("Vorprüfung: Nora lebt, Versuch strafbar", 175, 265, beim("versuch", "Nora"), size=34, farbe=TEXT),
    ok(135, 375, "tb", gr=24), z("I. Tatentschluss: Tötungsvorsatz", 175, 355, "tb", "Bold", 36),
    ok(215, 445, "heim", gr=22), z("auch zur Heimtücke: arglos, wehrlos", 250, 425, "heim", size=34, farbe=TEXT),
    ok(135, 535, beim("tb", "unmittelbar"), gr=24), z("II. Unmittelbares Ansetzen: Stich", 175, 515, beim("tb", "unmittelbar"), "Bold", 36),
    pille("Heimtücke: Angriff von hinten", 110, 640, beim("heim", "heimtückisch"), fill=ROT, size=34),
    peep_voll("RI_steht", RR, BR, FR, "r_sch"),
    icon("fluent-emoji-high-contrast", "kitchen-knife", *hand("RI_steht", RR, BR, FR), 110, "tb"),
    peep_voll("NO_arglos", NR, BR, FR, "heim"),
    pille("arglos", NR, 330, beim("heim", "arglose"), fill=GELB, size=32, anker="m"),
])

# 5 Richard: Rechtswidrigkeit -----------------------------------------------------------------------------------------
folie([("rw", "A. Richard › Rechtswidrigkeit")], [
    *tafel("rw", "Rechtswidrigkeit"),
    nein(135, 225, "rw", gr=24), z("§ 34 StGB: rechtfertigender Notstand", 175, 200, "rw", "Bold", 38),
    z("Leben ist nicht gegen Leben abwägbar", 175, 290, "n34", size=36, farbe=TEXT),
    z("echte Gefahr gab es nicht: nur eingebildet", 175, 360, beim("n34", "echte"), size=36, farbe=TEXT),
    pille("Tat rechtswidrig", 110, 470, beim("n34", "ohnehin"), fill=ROT, size=36),
    icon("fluent-emoji-high-contrast", "balance-scale", 1560, 270, 200, "n34"),
    peep_voll("RI_denkt", 1560, BR, FR, "rw"),
])

# 6 Richard: Schuld, § 35 ----------------------------------------------------------------------------------------------------
folie([("schuld", "A. Richard › Schuld › § 35 StGB")], [
    *tafel("schuld", "Schuld"),
    nein(135, 225, beim("n35", "Millionen"), gr=24), z("§ 35 StGB: entschuldigender Notstand", 175, 200, "schuld", "Bold", 38),
    z("nur Gefahr für:", 175, 290, "n35", size=36, farbe=TEXT),
    ok(215, 370, beim("n35", "selbst"), gr=22), z("den Täter selbst", 250, 350, beim("n35", "selbst"), size=36),
    ok(215, 440, beim("n35", "Angehörige"), gr=22), z("Angehörige", 250, 420, beim("n35", "Angehörige"), size=36),
    ok(215, 510, beim("n35", "nahestehende"), gr=22), z("nahestehende Personen", 250, 490, beim("n35", "nahestehende"), size=36),
    nein(215, 600, beim("n35", "Millionen"), gr=22), z("Millionen Fremde: nicht erfasst", 250, 580, beim("n35", "Millionen"), "Bold", 36),
    peep_voll("RI_denkt", 1560, BR, FR, "schuld"),
    blase("denk", 330, 250, beim("n35", "Millionen"), 1440, 230, figur=("RI_denkt", 1560, BR, FR)),
    icon("fluent-emoji-high-contrast", "globe-showing-europe-africa", 1440, 230, 110, beim("n35", "Millionen"), d=0.2),
])

# 7 Richard: Verbotsirrtum ------------------------------------------------------------------------------------------------------
folie([("irrt", "A. Richard › Schuld › Verbotsirrtum, § 17 StGB"), ("r_erg", "A. Richard › Ergebnis")], [
    *tafel("irrt", "Verbotsirrtum, § 17 StGB"),
    z("Richard hält die Tötung für erlaubt", 110, 200, beim("irrt", "Das"), "Bold", 38),
    z("→ fehlende Unrechtseinsicht", 150, 265, beim("irrt", "Verbotsirrtum"), size=36, farbe=TEXT),
    nein(135, 365, "verm", gr=24), z("aber vermeidbar:", 175, 340, "verm", "Bold", 38),
    z("Gewissensanspannung hätte genügt", 175, 405, "verm", size=36, farbe=TEXT, d=0.8),
    fl_block(110, 510, 1040, 150, GRUEN, "r_erg", [("Richard: versuchter Mord", "ExtraBold", 42, INK),
                                                  ("§§ 212, 211, 22, 23 I StGB – schuldhaft", "Regular", 34, INK)]),
    pille("Strafmilderung möglich, §§ 17 S. 2, 49 I StGB", 110, 710, beim("r_erg", "gemildert"), fill=GELB, size=34),
    peep_voll("RI_glaubt", 1560, BR, FR, "irrt", bis="verm"),
    blase("denk", 400, 220, "irrt", 1430, 240, inhalt=["Ich rette", "Millionen!"], textsize=40, figur=("RI_glaubt", 1560, BR, FR), bis="verm"),
    peep_voll("RI_schuld", 1560, BR, FR, "verm", anim="cut"),
])

# 8 Barbara und Peter: Beteiligungsform ------------------------------------------------------------------------------------------
BB, PB = 1420, 1700
folie([("hp", "B. Barbara und Peter"), ("anst", "B. Barbara und Peter › Täterschaft oder Teilnahme?")], [
    *tafel("hp", "B. Barbara und Peter"),
    nein(135, 225, beim("hp", "selbst"), gr=24), z("haben nicht selbst zugestochen", 175, 200, beim("hp", "selbst"), "Bold", 38),
    z("Anstiftung, § 26 StGB?", 175, 300, "anst", size=38),
    z("oder mittelbare Täterschaft,", 175, 380, "mt", size=38),
    z("§ 25 I Alt. 2 StGB?", 175, 435, "mt", size=38),
    pille("obwohl Richard selbst voll strafbar ist", 110, 560, beim("mt", "obwohl"), fill=PINK, size=34),
    peep_voll("BA_zufrieden", BB, BR, FR, "hp"),
    peep_voll("PE_ruhig", PB, BR, FR, "hp", d=0.2),
])

# 9 Verantwortungsprinzip ------------------------------------------------------------------------------------------------------
folie([("vp", "B. Barbara und Peter › Streit › Verantwortungsprinzip")], [
    *tafel("vp", "Verantwortungsprinzip"),
    z("Vordermann voll verantwortlich", 110, 200, "vp", "Bold", 38),
    z("→ Hintermann ist kein Täter", 150, 270, "vp", size=36, farbe=TEXT, d=1.5),
    pille("Barbara und Peter: nur Anstiftung", 110, 400, beim("vp2", "Anstifter"), fill=ORANGE, size=36),
    peep_voll("RI_ruhig", 1560, BR, FR, "vp"),
    pille("voll verantwortlich", 1560, 300, beim("vp2", "verantwortlichen"), fill=GELB, size=32, anker="m"),
])

# 10 BGH: Täter hinter dem Täter ---------------------------------------------------------------------------------------------------
folie([("bgh", "B. Barbara und Peter › Streit › BGH: Täter hinter dem Täter")], [
    *tafel("bgh", "BGH: Täter hinter dem Täter"),
    ok(135, 225, beim("bgh1", "bewusst"), gr=24), z("Irrtum bewusst hervorgerufen", 175, 200, beim("bgh1", "bewusst"), "Bold", 38),
    ok(135, 305, beim("bgh1", "eingesetzt"), gr=24), z("für eigene Zwecke eingesetzt", 175, 280, beim("bgh1", "eingesetzt"), "Bold", 38),
    ok(135, 385, "bgh2", gr=24), z("steuern kraft überlegenen Wissens", 175, 360, "bgh2", "Bold", 38),
    pille("Irrtumsherrschaft", 110, 490, beim("bgh2", "Täter"), fill=GRUEN, size=38),
    peep_voll("BA_zufrieden", 1380, BR, FR - 60, "bgh"),
    peep_voll("PE_ruhig", 1590, BR, FR - 60, "bgh", d=0.2),
    peep_voll("RI_glaubt", 1790, BR, FR - 60, "bgh", d=0.4),
    icon("fluent-emoji-high-contrast", "light-bulb", 1485, 330, 110, "bgh2"),
])

# 11 Ergebnis Hintermänner ---------------------------------------------------------------------------------------------------
folie([("hp_erg", "B. Barbara und Peter › Ergebnis")], [
    *tafel("hp_erg", "Ergebnis"),
    fl_block(110, 200, 1040, 200, GRUEN, "hp_erg", [("Barbara und Peter:", "ExtraBold", 42, INK),
                                                    ("versuchter Mord in mittelbarer Täterschaft", "Bold", 36, INK),
                                                    ("§§ 212, 211, 22, 23 I, 25 I Alt. 2 StGB", "Regular", 34, INK)]),
    peep_voll("BA_ruhig", BB, BR, FR, "hp_erg"),
    peep_voll("PE_ruhig", PB, BR, FR, "hp_erg", d=0.2),
])

# 12 Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------------------
LX = 1560
folie([("tipp", "Klausurtipp · Fallgruppen")], [
    *tafel("tipp", "Klausurtipp", fill=(255, 251, 230, 255)),
    warnung_i(150, 225, "tipp", gr=26),
    z("Täter hinter dem Täter nur in Fallgruppen:", 200, 200, beim("tipp", "Täter"), "Bold", 36),
    ok(175, 315, beim("tipp2", "Irrtumsherrschaft"), gr=22), z("Irrtumsherrschaft (Katzenkönig)", 215, 295, beim("tipp2", "Irrtumsherrschaft"), size=36),
    ok(175, 395, beim("tipp2", "Organisationsherrschaft"), gr=22), z("Organisationsherrschaft:", 215, 375, beim("tipp2", "Organisationsherrschaft"), size=36),
    z("Befehle in staatlichen Machtapparaten", 215, 430, beim("tipp2", "Befehlen"), size=34, farbe=TEXT),
    *redet("LX_warnt", LX, BR, FR + 40, "tipp", "sch"),
    pille("Lexi", LX, BR + 22, "tipp", fill=GELB, size=30, anker="m", d=0.2),
])

# 13 Klausurschema -------------------------------------------------------------------------------------------------------------
K1, K2 = 150, 210
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel("Klausurschema: Katzenkönig-Konstellation", 110, 90, "sch", 54),
    z("A. Vordermann (Richard): versuchter Mord", K1, 200, "k1", "Bold", 40, rechts=1820),
    z("Tatentschluss (Heimtücke) · unmittelbares Ansetzen · Rechtswidrigkeit", K2, 260, beim("k1", "versuchter"), size=34, farbe=TEXT, rechts=1820),
    z("Schuld: § 35 (–), Verbotsirrtum § 17 vermeidbar → strafbar, Milderung", K2, 312, beim("k1", "Verbotsirrtum"), size=34, farbe=TEXT, rechts=1820),
    z("B. Hintermänner (Barbara, Peter): § 25 I Alt. 2 StGB", K1, 410, "k2", "Bold", 40, rechts=1820),
    z("mittelbare Täterschaft trotz voll verantwortlichem Werkzeug?", K2, 470, beim("k2", "Mittelbare"), size=34, farbe=TEXT, rechts=1820),
    z("Streit: Verantwortungsprinzip vs. BGH „Täter hinter dem Täter“", K2, 522, "k3", size=34, farbe=TEXT, rechts=1820),
    pille("Ergebnis: mittelbare Täter kraft Irrtumsherrschaft", K1, 620, beim("k3", "folgen"), fill=GRUEN, size=38),
])

# 14 Merksatz (Lexi) -----------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=(255, 251, 230, 255)),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Auch wer einen voll", 0)], [("verantwortlichen Menschen", 0)], [("lenkt, kann ", 0), ("mittelbarer Täter", "a")],
                 [("sein.", 0)]], 750, 310, 50, "merke", {"a": beim("merke", "mittelbarer")}),
    *markertext([[("Entscheidend: ", 0), ("bewusst erzeugter Irrtum", "b")]], 750, 700, 44, "m2", {"b": beim("m2", "bewusst")}),
    *redet("LX_erklaert", 1680, 1000, 720, "merke", ("m2", 7.0)),
])
