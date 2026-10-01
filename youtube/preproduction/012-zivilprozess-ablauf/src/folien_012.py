"""Folge 012 · Zivilprozess Ablauf: Von der Klage bis zur Vollstreckung – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A Das Klavier (Wohnzimmer Seidel), B Sachverhalt, C I. Zuständiges Gericht, D II. Klageerhebung,
E III. Verfahrenseinleitung, F Abzweig Versäumnisurteil, G IV. Güteverhandlung (Gerichtssaal), H IV. Streitige Verhandlung
und Beweis, I V. Urteil, J VI. Berufung, K VII. Rechtskraft und Zwangsvollstreckung, L Bei Krüger (Gerichtsvollzieher),
M Klausurtipp (Lexi), N Klausurschema, O Merksatz (Lexi). Geräusche nur bei sichtbarer Handlung (Klavier wird weggerollt,
Türklingel des Gerichtsvollziehers)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *

bausteine.FIGORDNER = "op_012/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
GRAU = (176, 178, 190, 255)
HOLZ = (214, 160, 110, 255)          # Klavier (Pastell, aus Orange abgeleitet)
DUNKEL = (58, 58, 72, 255)
DAUER = bausteine._cj()["dauer"]


def z(text, x, y, cue, stil="Regular", size=38, farbe=INK, d=0.0, rechts=1170, **k):
    """Tafelzeile, die rechts nicht über die Karte hinausragen darf."""
    e = zeile(text, x, y, cue, stil, size, farbe=farbe, d=d, **k)
    assert e.x + e.sprite.width <= rechts, f"Zeile zu breit: {text} ({e.x + e.sprite.width:.0f} > {rechts})"
    return e


def tafel(cue, titel_, h=840, fill=WEISS, size=50):
    """Rechtstafel links, rechts bleibt Platz für die Figuren."""
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(titel_, 110, 100, cue, size)]


def bis_(e, cue):
    e.bis = cue
    return e


def lexi_bis_ende(cue):
    return (cue, round(DAUER - bausteine._t(cue) - 0.05, 3))


# --- Eigene Hilfsfunktion (Folge 012): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ---------------------
# ElevenLabs legt das Ende eines Wortes vor Satzzeichen oft in die folgende Pause (z. B. „Gericht!“ 16,42–17,42 s, hörbar
# bis 16,78 s). bausteine.redet() hielte den Mund dann bis zu 0,9 s in der Stille offen. redet_012() kürzt jedes Wortende
# auf das letzte 10-ms-Fenster über −38 dBFS (aus ../stimme.wav) und verteilt die Viseme nur auf diese Spanne.
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


def redet_012(basis, cx, unten, hoehe, cue, bis, **k):
    """Wie bausteine.redet(), aber Wortende = hörbares Ende (siehe oben); Viseme aus der Schreibung geschätzt."""
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


redet = redet_012


def klavier(cx, unten, breite, cue, bis=None, d=0.0, anim="pop"):
    """Klavier: Tabler 'piano', Korpus in Holzton."""
    return ficon("tabler", "piano", cx, unten, breite, cue, fuell=HOLZ, nebenfarbe=WEISS, d=d, bis=bis, anim=anim)


BODEN, FH = 880, 460
FX, BR, FR = 1560, 930, 500                   # Figur rechts neben der Tafel

# A Fall: das Klavier (Wohnzimmer von Frau Seidel) ---------------------------------------------------------------------------
SX, KX = 400, 1560
SE = ("SE_redet_r", SX, BODEN, FH)
KR = ("KR_redet", KX, BODEN, FH)
folie([(("fall", -0.4), "Fall · Das Klavier"), ("frage", "Fall · Die Frage")], [
    pille("Der Klavier-Fall", 70, 40, ("fall", -0.4), fill=GELB, size=48),
    linienzug([(60, BODEN), (1860, BODEN)], ("fall", -0.4), breite=7, farbe=INK),
    ficon("tabler", "lamp", 130, BODEN - 2, 130, ("fall", -0.4), fuell=GELB),
    ficon("tabler", "plant", 1820, BODEN - 2, 110, ("fall", -0.4), fuell=GRUEN),
    # Frau Seidel
    peep_voll("SE_froh_r", SX, BODEN, FH, ("fall", -0.4), bis="zahlt"),
    pille("Frau Seidel", SX, BODEN + 22, ("fall", -0.4), fill=LILA, size=30, anker="m", d=0.2),
    peep_voll("SE_aerger_r", SX, BODEN, FH, "zahlt", anim="cut", bis="s1"),
    *redet("SE_redet_r", SX, BODEN, FH, "s1", "frage"),
    peep_voll("SE_denkt_r", SX, BODEN, FH, "frage", anim="cut"),
    # das Klavier: steht zuerst bei Seidel, wird zu Krüger gerollt
    szene(bewegt(klavier(1170, BODEN - 2, 300, ("fall", -0.4)), "abholen", ("abholen", 1.5), -380), "012rollen*", 1.0,
          versatz=round(bausteine._t("abholen") - bausteine._t(("fall", -0.4)), 3)),
    pille("holt es gleich ab", 960, 400, "abholen", fill=WEISS, size=30, anker="m", bis="zahlt"),
    pille("Kaufpreis: 8.000 €", 960, 300, beim("krueger", "achttausend"), fill=GELB, size=36, anker="m", bis="zahlt"),
    # Herr Krüger
    peep_voll("KR_froh", KX, BODEN, FH, "krueger", bis="zahlt"),
    pille("Herr Krüger", KX, BODEN + 22, "krueger", fill=BLAU, size=30, anker="m", d=0.2),
    peep_voll("KR_trotz", KX, BODEN, FH, "zahlt", anim="cut", bis="k1"),
    ficon("tabler", "currency-euro-off", 960, 330, 110, beim("zahlt", "zahlt"), fuell=ROT, bis="k1"),
    pille("keine Zahlung", 960, 360, beim("zahlt", "zahlt"), fill=ROT, size=32, anker="m", bis="k1"),
    *redet("KR_redet", KX, BODEN, FH, "k1", "s1"),
    peep_voll("KR_trotz", KX, BODEN, FH, "s1", anim="cut"),
    blase("sprech", 660, 200, "k1", 1180, 240, inhalt=["Die Tasten klemmen. Dafür zahle", "ich keine 8.000 Euro!"],
          textsize=34, figur=KR, bis="s1"),
    blase("sprech", 640, 200, "s1", 800, 240, inhalt=["Das Klavier ist in Ordnung.", "Dann sehen wir uns vor Gericht!"],
          textsize=34, figur=SE, bis="frage"),
    pille("Wie kommt Frau Seidel an ihr Geld?", 960, 190, "frage", fill=PINK, size=40, anker="m"),
    ficon("tabler", "building-bank", 960, 420, 130, beim("frage", "Zivilprozess"), fuell=GRAU),
    pille("Zivilprozess", 960, 440, beim("frage", "Zivilprozess"), fill=WEISS, size=30, anker="m"),
])

# B Sachverhalt ----------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Frau Seidel verkauft Herrn Krüger ihr altes Klavier für 8.000 Euro. Krüger holt es sofort ab, zahlt den Kaufpreis "
    "aber nicht. Er meint: „Die Tasten klemmen. Dafür zahle ich keine 8.000 Euro!“ Frau Seidel hält das Klavier für "
    "mangelfrei und will klagen.",
    "Annahme: Die Klage wird 2026 erhoben; Krüger wohnt im Bezirk des Amtsgerichts seiner Stadt.",
], "Wie kommt Frau Seidel an ihr Geld?")

# C I. Zuständiges Gericht -----------------------------------------------------------------------------------------------------
PI = "I. Zuständiges Gericht"
AG, LG = 1420, 1720
folie([("gericht", PI), ("sachl", f"{PI} › sachlich, §§ 23 Nr. 1, 71 GVG"), ("oertl", f"{PI} › örtlich, §§ 12, 13 ZPO"),
       ("anwalt", f"{PI} › kein Anwaltszwang, § 78 I ZPO")], [
    *tafel("gericht", "I. Zuständiges Gericht"),
    z("1. sachlich: Streitwert", 150, 195, "sachl", "Bold", 38),
    z("Amtsgericht: bis 10.000 €, § 23 Nr. 1 GVG", 190, 255, beim("sachl", "Amtsgerichte"), size=34, farbe=TEXT),
    z("Landgericht: alles andere, § 71 I GVG", 190, 305, "lg", size=34, farbe=TEXT),
    z("Grenze seit 1.1.2026; vorher 5.000 €", 190, 355, "neu", size=34, farbe=TEXT),
    z("2. örtlich: Wohnsitz des Beklagten,", 150, 450, "oertl", "Bold", 38),
    z("§§ 12, 13 ZPO", 190, 505, beim("oertl", "Paragrafen"), size=34, farbe=TEXT),
    z("3. Amtsgericht: kein Anwaltszwang,", 150, 600, "anwalt", "Bold", 38),
    z("§ 78 I ZPO", 190, 655, beim("anwalt", "Amtsgericht"), size=34, farbe=TEXT),
    peep_voll("SE_denkt", FX, BR, FR, "gericht", bis="anwalt"),
    peep_voll("SE_froh", FX, BR, FR, "anwalt", anim="cut"),
    pille("Frau Seidel", FX, BR + 22, "gericht", fill=LILA, size=30, anker="m", d=0.2),
    pille("Streitwert: 8.000 €", FX, 120, beim("sachl", "Streitwert"), fill=GELB, size=34, anker="m", bis="oertl"),
    ficon("tabler", "building-bank", AG, 330, 140, beim("sachl", "Amtsgerichte"), fuell=GRUEN, bis="oertl"),
    pille("Amtsgericht", AG, 350, beim("sachl", "Amtsgerichte"), fill=GRUEN, size=28, anker="m", bis="oertl"),
    bis_(ok(AG + 85, 205, beim("sachl", "zuständig"), gr=26), "oertl"),
    ficon("tabler", "building-bank", LG, 330, 140, "lg", fuell=BLAU, bis="oertl"),
    pille("Landgericht", LG, 350, "lg", fill=BLAU, size=28, anker="m", bis="oertl"),
    ficon("tabler", "map-pin", FX, 300, 110, "oertl", fuell=ROT, bis="anwalt"),
    pille("Wohnsitz Krüger", FX, 320, beim("oertl", "Wohnsitz"), fill=WEISS, size=30, anker="m", bis="anwalt"),
    ficon("tabler", "briefcase-off", FX, 300, 120, beim("anwalt", "Anwalt"), fuell=GELB),
    pille("ohne Anwalt", FX, 320, beim("anwalt", "Anwalt"), fill=WEISS, size=30, anker="m"),
])

# D II. Klageerhebung ----------------------------------------------------------------------------------------------------------
PII = "II. Klageerhebung"
MB = 1440
folie([("klage", f"{PII} › Klageschrift, § 253 ZPO"), ("zust", f"{PII} › Zustellung von Amts wegen"),
       ("rh", f"{PII} › Rechtshängigkeit, § 261 ZPO"), ("online", f"{PII} › Online-Verfahren, §§ 1122 ff. ZPO")], [
    *tafel("klage", "II. Klageerhebung"),
    z("Klageschrift, § 253 II ZPO:", 150, 190, beim("klage", "Klageschrift"), "Bold", 38),
    z("Parteien und Gericht", 190, 245, beim("klage", "Parteien"), size=34, farbe=TEXT),
    z("bestimmter Antrag", 190, 292, beim("klage", "bestimmten"), size=34, farbe=TEXT),
    z("Grund des Anspruchs", 190, 339, beim("klage", "Grund"), size=34, farbe=TEXT),
    z("hier: 8.000 € aus Kaufvertrag, § 433 II BGB", 190, 395, "antrag", size=34),
    z("Zustellung von Amts wegen, §§ 166 II, 271 I ZPO", 150, 470, "zust", "Bold", 36),
    ok(170, 555, beim("rh", "erhoben"), gr=20), z("Klage erhoben, § 253 I ZPO", 210, 530, beim("rh", "erhoben"), size=34),
    ok(170, 605, beim("rh", "rechtshängig"), gr=20), z("rechtshängig, § 261 I ZPO", 210, 580, beim("rh", "rechtshängig"), size=34),
    ok(170, 655, "verj", gr=20), z("Verjährung gehemmt, § 204 I Nr. 1 BGB", 210, 630, "verj", size=34),
    z("Neu: Online-Verfahren (Erprobung) für Geldklagen", 150, 720, "online", "Bold", 34),
    z("bis 10.000 €, §§ 1122 ff. ZPO", 190, 770, beim("online", "Geldklagen"), size=32, farbe=TEXT),
    peep_voll("SE_ruhig", 1350, BR, FR - 80, "klage"),
    pille("Frau Seidel", 1350, BR + 22, "klage", fill=LILA, size=28, anker="m", d=0.2),
    ficon("tabler", "file-text", 1350, 470, 100, beim("klage", "Klageschrift"), fuell=WEISS, bis="zust"),
    pille("Klage: 8.000 €", 1350, 300, "antrag", fill=GELB, size=30, anker="m", bis="zust"),
    # Zustellung: Brief wandert von Seidels Klage in Krügers Briefkasten
    ficon("tabler", "mailbox", 1570, 760, 150, "zust", fuell=BLAU),
    bewegt(ficon("tabler", "mail", 1570, 610, 90, "zust", fuell=WEISS, bis="online"), "zust", ("zust", 1.2), -220, -140),
    pille("Zustellung", 1570, 800, beim("zust", "zu"), fill=WEISS, size=26, anker="m"),
    peep_voll("KR_denkt", 1770, BR, FR - 80, "zust"),
    pille("Herr Krüger", 1770, BR + 22, "zust", fill=BLAU, size=28, anker="m"),
    pille("rechtshängig", 1600, 250, beim("rh", "rechtshängig"), fill=GRUEN, size=32, anker="m", bis="online"),
    ficon("tabler", "hourglass", 1600, 475, 80, "verj", fuell=GELB, bis="online"),
    pille("Verjährung gehemmt", 1600, 330, "verj", fill=GELB, size=30, anker="m", bis="online"),
    ficon("tabler", "device-laptop", 1600, 420, 150, "online", fuell=BLAU),
    pille("Online-Verfahren", 1600, 250, "online", fill=BLAU, size=32, anker="m"),
])

# E III. Verfahrenseinleitung --------------------------------------------------------------------------------------------------
PIII = "III. Verfahrenseinleitung"
RX, KX3 = 1420, 1740
folie([("weg", f"{PIII} › § 272 II ZPO"), ("vv", f"{PIII} › schriftliches Vorverfahren, § 276 ZPO")], [
    *tafel("weg", "III. Verfahrenseinleitung"),
    z("§ 272 II ZPO: Die Richterin wählt", 150, 190, beim("weg", "Richterin"), "Bold", 38),
    fl_block(110, 260, 450, 120, WEISS, beim("weg", "frühem"), [("früher erster Termin", "Bold", 32, INK), ("§ 275 ZPO", "Regular", 30, INK)]),
    fl_block(600, 260, 550, 120, GELB, beim("weg", "schriftlichem"), [("schriftliches Vorverfahren", "Bold", 32, INK),
                                                                   ("§ 276 ZPO", "Regular", 30, INK)]),
    ok(1118, 282, "vv", gr=24),
    z("1. Verteidigungsanzeige: 2 Wochen", 150, 450, beim("frist1", "zwei"), "Bold", 36),
    z("(Notfrist), § 276 I 1 ZPO", 190, 500, beim("frist1", "anzeigen"), size=32, farbe=TEXT),
    z("2. Klageerwiderung: mindestens", 150, 580, beim("frist2", "Klageerwiderung"), "Bold", 36),
    z("2 weitere Wochen, § 276 I 2 ZPO", 190, 630, beim("frist2", "zwei"), size=32, farbe=TEXT),
    peep_voll("RI_ruhig", RX, BR, FR - 40, "weg"),
    pille("Richterin", RX, BR + 22, "weg", fill=GRAU, size=28, anker="m", d=0.2),
    ficon("tabler", "file-text", RX, 330, 110, "vv", fuell=GELB),
    pille("Vorverfahren", RX, 350, "vv", fill=GELB, size=28, anker="m"),
    peep_voll("KR_denkt", KX3, BR, FR - 40, "frist1"),
    pille("Herr Krüger", KX3, BR + 22, "frist1", fill=BLAU, size=28, anker="m"),
    ficon("tabler", "calendar", KX3, 300, 100, beim("frist1", "zwei"), fuell=WEISS),
    pille("2 Wochen", KX3, 330, beim("frist1", "zwei"), fill=WEISS, size=28, anker="m"),
    pille("+ 2 Wochen", KX3, 395, beim("frist2", "zwei"), fill=WEISS, size=28, anker="m"),
])

# F Abzweig: Versäumnisurteil --------------------------------------------------------------------------------------------------
folie([("vu", f"{PIII} › Abzweig: Versäumnisurteil, § 331 III ZPO"), ("eins", f"{PIII} › Abzweig: Einspruch, §§ 338, 339 ZPO")], [
    *tafel("vu", "Abzweig: Versäumnisurteil", fill=(246, 243, 255, 255)),
    z("Krüger schweigt: keine Anzeige", 150, 190, beim("vu", "geschwiegen"), "Bold", 36),
    z("Versäumnisurteil auf Antrag, ohne", 150, 265, beim("vu", "Versäumnisurteil"), "Bold", 36),
    z("mündliche Verhandlung, § 331 III ZPO", 190, 315, beim("vu", "mündliche"), size=34, farbe=TEXT),
    z("nur soweit die Klage schlüssig ist", 190, 365, "schl", size=34, farbe=TEXT),
    z("Einspruch: 2 Wochen (Notfrist),", 150, 470, "eins", "Bold", 36),
    z("§§ 338, 339 I ZPO", 190, 520, beim("eins", "Paragraf"), size=34, farbe=TEXT),
    z("zulässig: zurück in die Lage vor", 150, 600, "zurueck", "Bold", 36),
    z("der Säumnis, § 342 ZPO", 190, 650, beim("zurueck", "Säumnis"), size=34, farbe=TEXT),
    peep_voll("KR_muede", FX, BR, FR, "vu", bis="eins"),
    peep_voll("KR_denkt", FX, BR, FR, "eins", anim="cut"),
    pille("Herr Krüger", FX, BR + 22, "vu", fill=BLAU, size=28, anker="m", d=0.2),
    ficon("tabler", "mail-off", FX, 280, 100, beim("vu", "geschwiegen"), fuell=WEISS, bis=beim("vu", "Versäumnisurteil")),
    ficon("tabler", "file-text", FX, 300, 120, beim("vu", "Versäumnisurteil"), fuell=ROT, bis="eins"),
    pille("Versäumnisurteil", FX, 320, beim("vu", "Versäumnisurteil"), fill=ROT, size=30, anker="m", bis="eins"),
    ficon("tabler", "arrow-back-up", FX, 300, 110, beim("eins", "Einspruch"), fuell=GRUEN),
    pille("Einspruch", FX, 320, beim("eins", "Einspruch"), fill=GRUEN, size=30, anker="m"),
])

# G IV. Mündliche Verhandlung: Güteverhandlung im Gerichtssaal ----------------------------------------------------------------
PIV = "IV. Mündliche Verhandlung"
RIX, SX2, KX2 = 960, 380, 1540
RI = ("RI_redet", RIX, 640, 400)
KRg = ("KR_redet", KX2, BODEN, FH)
folie([("mv", f"{PIV} › Termin"), ("guete", f"{PIV} › Güteverhandlung, § 278 II ZPO")], [
    linienzug([(60, BODEN), (1860, BODEN)], "mv", breite=7, farbe=INK),
    pille("Amtsgericht · Sitzungssaal", 70, 40, "mv", fill=GRAU, size=36),
    peep_voll("RI_ruhig", RIX, 640, 400, "mv", bis="r1"),
    *redet("RI_redet", RIX, 640, 400, "r1", "k2"),
    peep_voll("RI_ruhig", RIX, 640, 400, "k2", anim="cut"),
    fl_block(700, 560, 520, 110, DUNKEL, "mv", [("Richterin", "Bold", 32, WEISS)], rand=5),
    peep_voll("SE_ruhig_r", SX2, BODEN, FH, "mv", bis="k2"),
    peep_voll("SE_aerger_r", SX2, BODEN, FH, "k2", anim="cut"),
    pille("Klägerin Seidel", SX2, BODEN + 22, "mv", fill=LILA, size=30, anker="m", d=0.2),
    peep_voll("KR_trotz", KX2, BODEN, FH, "mv", bis="k2"),
    *redet("KR_redet", KX2, BODEN, FH, "k2", "streit"),
    pille("Beklagter Krüger", KX2, BODEN + 22, "mv", fill=BLAU, size=30, anker="m", d=0.2),
    pille("Krüger: Klavier mangelhaft", 1540, 300, beim("mv", "mangelhaft"), fill=ROT, size=30, anker="m", bis="guete"),
    pille("Güteverhandlung, § 278 II ZPO", 560, 250, beim("guete", "Güteverhandlung"), fill=GELB, size=36, anker="m"),
    blase("sprech", 600, 160, "r1", 1430, 150, inhalt=["Können Sie sich nicht einigen?"], textsize=32, figur=RI, bis="k2"),
    blase("sprech", 580, 160, "k2", 1380, 320, inhalt=["Nein. Die Tasten klemmen!"], textsize=34, figur=KRg, bis="streit"),
])

# H IV. Streitige Verhandlung und Beweisaufnahme --------------------------------------------------------------------------------
S3, K3 = 1400, 1740
folie([("streit", f"{PIV} › streitige Verhandlung, § 279 ZPO"), ("beweis", f"{PIV} › Beweisaufnahme, §§ 284 ff. ZPO")], [
    *tafel("streit", "IV. Verhandlung und Beweis"),
    z("streitige Verhandlung, § 279 I ZPO", 150, 195, "streit", "Bold", 38),
    z("streitig: Klemmen die Tasten?", 150, 290, beim("beweis", "Streitig"), "Bold", 38),
    z("Beweis über streitige Tatsachen,", 190, 350, beim("beweis", "Beweis"), size=34, farbe=TEXT),
    z("§ 359 Nr. 1 ZPO", 190, 398, beim("beweis", "Beweis"), size=34, farbe=TEXT),
    z("Sachverständiger, §§ 284 ff., 402 ff. ZPO", 190, 455, beim("beweis", "Sachverständigen"), size=34, farbe=TEXT),
    ok(170, 565, "gutachten", gr=24), z("Gutachten: Klavier in Ordnung", 210, 540, "gutachten", "ExtraBold", 38),
    peep_voll("SE_ruhig", S3, BR, FR - 60, "streit", bis="gutachten"),
    peep_voll("SE_froh", S3, BR, FR - 60, "gutachten", anim="cut"),
    peep_voll("KR_trotz", K3, BR, FR - 60, "streit", bis="gutachten"),
    peep_voll("KR_schreck", K3, BR, FR - 60, "gutachten", anim="cut"),
    pille("Frau Seidel", S3, BR + 22, "streit", fill=LILA, size=28, anker="m"),
    pille("Herr Krüger", K3, BR + 22, "streit", fill=BLAU, size=28, anker="m"),
    klavier(1570, 380, 200, beim("beweis", "Streitig")),
    pille("Tasten klemmen?", 1570, 140, beim("beweis", "Streitig"), fill=WEISS, size=32, anker="m", bis="gutachten"),
    ficon("tabler", "file-certificate", 1760, 380, 90, beim("beweis", "Sachverständigen"), fuell=WEISS),
    pille("Sachverständiger", 1740, 400, beim("beweis", "Sachverständigen"), fill=WEISS, size=26, anker="m", bis="gutachten"),
    pille("Gutachten: in Ordnung", 1570, 140, "gutachten", fill=GRUEN, size=32, anker="m"),
    bis_(haken_i(1400, 300, beim("gutachten", "Ordnung"), gr=36), None),
])

# I V. Urteil ------------------------------------------------------------------------------------------------------------------
PV = "V. Urteil"
RU = ("RI_redet", FX, BR, FR)
folie([("urteil", f"{PV} › Endurteil, § 300 ZPO"), ("aufbau", f"{PV} › Aufbau, § 313 ZPO"), ("r2", f"{PV} › Tenor")], [
    *tafel("urteil", "V. Urteil"),
    z("Endurteil bei Entscheidungsreife, § 300 I ZPO", 150, 195, beim("urteil", "Endurteil"), "Bold", 36),
    z("Aufbau, § 313 I ZPO:", 150, 280, "aufbau", "Bold", 36),
    z("1. Rubrum (Nr. 1–3)", 190, 335, beim("aufbau", "Rubrum"), size=34, farbe=TEXT),
    z("2. Tenor = Urteilsformel (Nr. 4)", 190, 382, beim("aufbau", "Tenor"), size=34, farbe=TEXT),
    z("3. Tatbestand (Nr. 5)", 190, 429, beim("aufbau", "Tatbestand"), size=34, farbe=TEXT),
    z("4. Entscheidungsgründe (Nr. 6)", 190, 476, beim("aufbau", "Entscheidungsgründen"), size=34, farbe=TEXT),
    fl_block(110, 580, 1040, 160, GELB, "r2", [("Tenor: Der Beklagte wird verurteilt,", "Bold", 34, INK),
                                               ("an die Klägerin 8.000 € zu zahlen.", "Bold", 34, INK)]),
    peep_voll("RI_ruhig", FX, BR, FR, "urteil", bis="r2"),
    *redet("RI_redet", FX, BR, FR, "r2", "beruf"),
    pille("Richterin", FX, BR + 22, "urteil", fill=GRAU, size=28, anker="m", d=0.2),
    ficon("tabler", "file-text", FX, 300, 120, beim("urteil", "Endurteil"), fuell=WEISS, bis="r2"),
    pille("Endurteil", FX, 320, beim("urteil", "Endurteil"), fill=WEISS, size=30, anker="m", bis="r2"),
    blase("sprech", 600, 220, "r2", 1560, 230, inhalt=["Der Beklagte wird verurteilt,", "an die Klägerin", "8.000 Euro zu zahlen."],
          textsize=30, figur=RU, bis="beruf"),
])

# J VI. Berufung ---------------------------------------------------------------------------------------------------------------
PVI = "VI. Berufung"
KB = ("KR_denkt", FX, BR, FR)
folie([("beruf", f"{PVI} › Statthaftigkeit, § 511 I ZPO"), ("wert", f"{PVI} › Beschwerdewert, § 511 II ZPO"),
       ("frist", f"{PVI} › Frist, § 517 ZPO")], [
    *tafel("beruf", "VI. Berufung"),
    z("Berufung gegen Endurteile, § 511 I ZPO", 150, 195, "beruf", "Bold", 38),
    z("Wert des Beschwerdegegenstands", 150, 280, "wert", "Bold", 36),
    z("über 1.000 €, § 511 II Nr. 1 ZPO", 190, 330, beim("wert", "tausend"), size=34, farbe=TEXT),
    z("bis 2025: über 600 €", 190, 378, beim("wert", "früher"), size=34, farbe=TEXT),
    z("sonst nur nach Zulassung, § 511 II Nr. 2 ZPO", 190, 426, beim("wert", "Sonst"), size=34, farbe=TEXT),
    ok(170, 525, "beschwer", gr=22), z("Krüger: 8.000 € angreifbar", 210, 500, "beschwer", "Bold", 36),
    z("Frist: 1 Monat ab Zustellung des", 150, 600, "frist", "Bold", 36),
    z("vollständigen Urteils, § 517 ZPO", 190, 650, beim("frist", "vollständigen"), size=34, farbe=TEXT),
    peep_voll("KR_denkt", FX, BR, FR, "beruf"),
    pille("Herr Krüger", FX, BR + 22, "beruf", fill=BLAU, size=28, anker="m", d=0.2),
    blase("denk", 340, 200, "beruf", 1560, 210, inhalt=["Berufung?"], textsize=36, figur=KB, bis="frist"),
    pille("über 1.000 €", 1340, 380, beim("wert", "tausend"), fill=GELB, size=30, anker="m", bis="frist"),
    pille("8.000 €", 1790, 380, "beschwer", fill=GELB, size=30, anker="m", bis="frist"),
    ficon("tabler", "calendar", 1560, 300, 110, "frist", fuell=WEISS),
    pille("1 Monat", 1560, 320, "frist", fill=WEISS, size=30, anker="m"),
])

# K VII. Rechtskraft und Zwangsvollstreckung ------------------------------------------------------------------------------------
PVII = "VII. Rechtskraft und Zwangsvollstreckung"
S7 = 1400
folie([("rk", f"{PVII} › Rechtskraft, § 705 ZPO"), ("zv", f"{PVII} › Voraussetzungen"),
       ("titel", f"{PVII} › 1. Titel, § 704 ZPO"), ("klausel", f"{PVII} › 2. Klausel, § 724 ZPO"),
       ("zustellung", f"{PVII} › 3. Zustellung, § 750 ZPO"), ("gv", f"{PVII} › Gerichtsvollzieher, §§ 753, 754a ZPO")], [
    *tafel("rk", "VII. Rechtskraft und Vollstreckung", size=46),
    z("Frist verstrichen: rechtskräftig, § 705 ZPO", 150, 185, beim("rk", "rechtskräftig"), "Bold", 36),
    z("Krüger zahlt trotzdem nicht", 190, 235, "nichts", size=34, farbe=TEXT),
    z("Zwangsvollstreckung braucht:", 150, 310, "zv", "Bold", 36),
    ok(170, 385, "titel", gr=20), z("1. Titel: Urteil, rechtskräftig oder", 210, 360, "titel", size=34),
    z("vorläufig vollstreckbar, § 704 ZPO", 250, 405, beim("titel", "vorläufig"), size=32, farbe=TEXT),
    ok(170, 480, "klausel", gr=20), z("2. Klausel: vollstreckbare Ausfertigung,", 210, 455, "klausel", size=34),
    z("Geschäftsstelle, §§ 724, 725 ZPO", 250, 500, beim("klausel", "Geschäftsstelle"), size=32, farbe=TEXT),
    ok(170, 575, "zustellung", gr=20), z("3. Zustellung, spätestens bei Beginn,", 210, 550, "zustellung", size=34),
    z("§ 750 I ZPO", 250, 595, beim("zustellung", "Paragraf"), size=32, farbe=TEXT),
    z("Auftrag an den Gerichtsvollzieher, § 753 I ZPO", 150, 670, "gv", "Bold", 34),
    z("seit 1.10.2026: Titel und Klausel als", 190, 720, "digital", size=32, farbe=TEXT),
    z("elektronische Dokumente, § 754a ZPO", 190, 765, beim("digital", "elektronische"), size=32, farbe=TEXT),
    # Rechtskraft: Krüger lässt die Frist verstreichen (bleibt im Bild, Schuldner)
    peep_voll("KR_ruhig", 1790, BR, FR - 80, "rk", bis="gv"),
    peep_voll("KR_schreck", 1790, BR, FR - 80, "gv", anim="cut"),
    pille("Herr Krüger", 1790, BR + 22, "rk", fill=BLAU, size=26, anker="m"),
    ficon("tabler", "hourglass", 1560, 300, 100, "rk", fuell=GELB, bis="zv"),
    pille("rechtskräftig", 1560, 320, beim("rk", "rechtskräftig"), fill=GRUEN, size=30, anker="m", bis="zv"),
    ficon("tabler", "currency-euro-off", 1790, 440, 80, "nichts", fuell=ROT, bis="zv"),
    # Frau Seidel sammelt Titel, Klausel, Zustellung
    peep_voll("SE_denkt", 1370, BR, FR - 80, "rk", bis="titel"),
    peep_voll("SE_ruhig", 1370, BR, FR - 80, "titel", anim="cut", bis="gv"),
    peep_voll("SE_froh", 1370, BR, FR - 80, "gv", anim="cut"),
    pille("Frau Seidel", 1370, BR + 22, "rk", fill=LILA, size=26, anker="m"),
    ficon("tabler", "file-text", 1420, 300, 90, "titel", fuell=WEISS),
    pille("Titel", 1420, 320, "titel", fill=WEISS, size=26, anker="m"),
    ficon("tabler", "rubber-stamp", 1590, 300, 90, "klausel", fuell=GELB),
    pille("Klausel", 1590, 320, "klausel", fill=GELB, size=26, anker="m"),
    ficon("tabler", "mail", 1775, 290, 80, "zustellung", fuell=WEISS),
    pille("Zustellung", 1775, 320, "zustellung", fill=WEISS, size=26, anker="m"),
    peep_voll("GV_ruhig", 1590, BR, FR - 80, "gv"),
    pille("Gerichtsvollzieher", 1590, BR + 70, "gv", fill=TUERKIS, size=24, anker="m"),
    ficon("tabler", "device-laptop", 1590, 480, 100, "digital", fuell=BLAU),
])

# L Bei Krüger: der Gerichtsvollzieher -----------------------------------------------------------------------------------------
KW, GX, TX = 820, 1560, 1180
GVb = ("GV_redet", GX, BODEN, FH)
folie([("g1", "VII. Zwangsvollstreckung › Gerichtsvollzieher bei Krüger"), ("pfand", "VII. Zwangsvollstreckung › Pfändung, § 808 ZPO")], [
    linienzug([(60, BODEN), (1860, BODEN)], ("g1", -0.4), breite=7, farbe=INK),
    pille("Bei Herrn Krüger", 70, 40, ("g1", -0.4), fill=BLAU, size=40),
    klavier(380, BODEN - 2, 300, ("g1", -0.4)),
    szene(ficon("tabler", "door", TX, BODEN - 2, 230, ("g1", -0.4), fuell=HOLZ), "012klingel*", 0.8),
    peep_voll("KR_schreck_r", KW, BODEN, FH, ("g1", -0.4), bis="siegel"),
    peep_voll("KR_muede_r", KW, BODEN, FH, "siegel", anim="cut"),
    pille("Herr Krüger", KW, BODEN + 22, ("g1", -0.4), fill=BLAU, size=30, anker="m"),
    peep_voll("GV_ruhig", GX, BODEN, FH, ("g1", -0.4), bis="g1"),
    *redet("GV_redet", GX, BODEN, FH, "g1", "pfand"),
    peep_voll("GV_ruhig", GX, BODEN, FH, "pfand", anim="cut"),
    pille("Gerichtsvollzieher", GX, BODEN + 22, ("g1", -0.4), fill=TUERKIS, size=30, anker="m"),
    ficon("tabler", "file-text", GX + 150, 560, 80, ("g1", -0.4), fuell=WEISS),
    blase("sprech", 600, 200, "g1", 1430, 250, inhalt=["Guten Tag, Herr Krüger.", "Ich komme wegen des Urteils."], textsize=34,
          figur=GVb, bis="pfand"),
    pille("Pfändung, § 808 ZPO", 380, 330, beim("pfand", "pfänden"), fill=GELB, size=34, anker="m"),
    ficon("tabler", "sticker", 380, 700, 90, beim("siegel", "Siegel"), fuell=ROT),
    pille("Siegel", 380, 420, beim("siegel", "Siegel"), fill=ROT, size=30, anker="m"),
    pille("bleibt in der Regel beim Schuldner", 420, 510, beim("siegel", "bleibt"), fill=WEISS, size=30, anker="m"),
])

# M Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · Anwaltsklausur: Fristen"), ("tipp2", "Klausurtipp · Urteilsklausur: Relation")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Anwaltsklausur: zuerst die Fristen", 200, 200, beim("tipp", "Notiere"), "Bold", 36),
    z("Verteidigungsanzeige: 2 Wochen, § 276 I 1", 240, 260, beim("tipp", "Verteidigungsanzeige"), size=32, farbe=TEXT),
    z("Einspruch: 2 Wochen, § 339 I", 240, 305, beim("tipp", "Einspruch"), size=32, farbe=TEXT),
    z("Berufung: 1 Monat, § 517", 240, 350, beim("tipp", "Berufung"), size=32, farbe=TEXT),
    z("Urteilsklausur: Relation", 200, 450, beim("tipp2", "Relation"), "Bold", 36),
    z("1. Klage schlüssig?", 240, 510, beim("tipp2", "schlüssig"), size=32, farbe=TEXT),
    z("2. Verteidigung erheblich?", 240, 555, beim("tipp2", "erheblich"), size=32, farbe=TEXT),
    z("3. erst dann: Beweis", 240, 600, beim("tipp2", "Beweis"), size=32, farbe=TEXT),
    *redet("LX_warnt", LXX, BR, FR + 60, "tipp", "sch"),
    pille("Lexi", LXX, BR + 22, "tipp", fill=GELB, size=30, anker="m", d=0.2),
])

# N Klausurschema ---------------------------------------------------------------------------------------------------------------
K1, K2 = 150, 210
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel("Klausurschema: Ablauf des Zivilprozesses", 110, 90, "sch", 54),
    z("I. Zuständiges Gericht: sachlich (§§ 23 Nr. 1, 71 GVG), örtlich (§§ 12, 13 ZPO)", K1, 190, "sI", "Bold", 34, rechts=1820),
    z("II. Klageerhebung durch Zustellung (§ 253 I ZPO), Rechtshängigkeit (§ 261 ZPO)", K1, 270, "sII", "Bold", 34, rechts=1820),
    z("III. Schriftliches Vorverfahren (§ 276) oder früher erster Termin (§ 275)", K1, 350, "sIII", "Bold", 34, rechts=1820),
    z("Abzweig: Versäumnisurteil (§ 331 III), Einspruch (§§ 338, 339 ZPO)", K2, 400, beim("sIII", "Abzweig"), size=32,
      farbe=TEXT, rechts=1820),
    z("IV. Verhandlung (Güteverhandlung, § 278 II) und Beweisaufnahme (§§ 284 ff. ZPO)", K1, 480, "sIV", "Bold", 34, rechts=1820),
    z("V. Urteil (§§ 300, 313 ZPO)", K1, 560, "sV", "Bold", 34, rechts=1820),
    z("VI. Berufung (§ 511: über 1.000 € oder Zulassung; Frist § 517 ZPO)", K1, 640, "sVI", "Bold", 34, rechts=1820),
    z("VII. Rechtskraft (§ 705) und Zwangsvollstreckung (§§ 704 ff. ZPO)", K1, 720, "sVII", "Bold", 34, rechts=1820),
    z("Titel, Klausel, Zustellung (§§ 704, 724, 750 ZPO)", K2, 770, beim("sVII", "Zwangsvollstreckung"), size=32,
      farbe=TEXT, rechts=1820),
])

# O Merksatz (Lexi) -------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Das Urteil klärt,", "a")], [("wer recht hat.", 0)]], 750, 320, 54, "merke",
                {"a": beim("merke", "Urteil")}),
    *markertext([[("Durchsetzen lässt es sich erst mit", 0)], [("Titel, Klausel und Zustellung.", "b")]], 750, 560, 50, "m2",
                {"b": beim("m2", "Titel")}),
    *redet("LX_erklaert", 1680, 1000, 720, "merke", lexi_bis_ende("merke")),
])
