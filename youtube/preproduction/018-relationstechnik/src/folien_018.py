"""Folge 018 · Relationstechnik: Kläger-, Beklagten- und Beweisstation erklärt – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A Die Akte (Arbeitszimmer der Referendarin), B Im Café (Lieferung des Kühlschranks),
C Sachverhalt, D Die Stationen, E I. Prozessstation, F II. Klägerstation, G III. Beklagtenstation (Bestreiten),
H III. Einwendung Erfüllung, I III. Bestreiten der Zahlung, J IV. Beweisstation, K Beweisaufnahme (Sitzungssaal),
L V. Tenor, M Und im Urteil?, N Klausurtipp (Lexi), O Klausurschema, P Merksatz (Lexi).
Geräusche nur bei sichtbarer Handlung: die Akte fällt auf den Schreibtisch, der Lieferwagen fährt vor (Freesound CC0)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *

bausteine.FIGORDNER = "op_018/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
LILAHELL = (246, 243, 255, 255)
GRAU = (176, 178, 190, 255)
HOLZ = (214, 160, 110, 255)          # Schreibtisch, Pastell aus Orange abgeleitet
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


def hart(e):
    """Harter Schnitt statt Einblendung (erstes Bild nach dem Intro ist ab 0,0 s vollständig)."""
    e.anim = "cut"
    return e


def lexi_bis_ende(cue):
    return (cue, round(DAUER - bausteine._t(cue) - 0.05, 3))


# --- Eigene Hilfsfunktion (wie Folge 012): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ------------------
# ElevenLabs legt das Ende eines Wortes vor Satzzeichen oft in die folgende Pause. redet_018() kürzt jedes Wortende auf
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


def redet_018(basis, cx, unten, hoehe, cue, bis, **k):
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


redet = redet_018


def kuehlschrank(cx, unten, breite, cue, bis=None, d=0.0, anim="pop"):
    return ficon("tabler", "fridge", cx, unten, breite, cue, fuell=TUERKIS, nebenfarbe=WEISS, d=d, bis=bis, anim=anim)


BODEN, FH = 880, 440
FX, BR, FR = 1560, 930, 500                   # Figur rechts neben der Tafel

# A Fall: die Akte (Arbeitszimmer der Referendarin) --------------------------------------------------------------------------
RFX = 1300
RFa = ("RF_fragt", RFX, BODEN, FH + 20)
akte = bewegt(ficon("tabler", "file-stack", 700, 478, 170, "fall", fuell=WEISS), "fall", ("fall", 0.35), 0, -260)
folie([(("fall", -0.4), "Fall · Die Akte")], [
    pille("Die Zivilakte", 70, 40, ("fall", -0.4), fill=GELB, size=48, anim="cut"),
    hart(linienzug([(60, BODEN), (1860, BODEN)], ("fall", -0.4), breite=7, farbe=INK)),
    ficon("tabler", "desk", 700, BODEN - 2, 560, ("fall", -0.4), fuell=HOLZ, anim="cut"),
    ficon("tabler", "coffee", 520, 478, 80, ("fall", -0.4), fuell=WEISS, anim="cut"),
    peep_voll("RF_ruhig", RFX, BODEN, FH + 20, ("fall", -0.4), bis="fall", anim="cut"),
    peep_voll("RF_denkt", RFX, BODEN, FH + 20, "fall", anim="cut", bis="r1"),
    pille("Referendarin", RFX, BODEN + 22, ("fall", -0.4), fill=GRUEN, size=30, anker="m", anim="cut"),
    szene(akte, "018akte*", 1.0, versatz=0.3),
    pille("40 Seiten Schriftsätze", 700, 200, beim("fall", "vierzig"), fill=WEISS, size=34, anker="m"),
    pille("Zivilakte", 930, 380, beim("fall", "Zivilakte"), fill=GELB, size=30, anker="m"),
    *redet("RF_fragt", RFX, BODEN, FH + 20, "r1", "akte"),
    blase("sprech", 600, 190, "r1", 1420, 220, inhalt=["Vierzig Seiten.", "Wo fange ich an?"], textsize=36, figur=RFa),
])

# B Fall: im Café (Lieferung) -----------------------------------------------------------------------------------------------
LX_, BX_, FAX, TRX = 560, 1660, 1350, 1080
LEb = ("LE_redet_r", LX_, BODEN, FH)
BRb = ("BR_redet", BX_, BODEN, FH)
lieferwagen = bewegt(ficon("tabler", "truck-delivery", TRX, BODEN - 2, 300, "liefer", fuell=WEISS, spiegeln=True),
                     "liefer", ("liefer", 1.4), 300, 0)
folie([("akte", "Fall · Im Café"), ("frage", "Fall · Die Frage")], [
    pille("In der Akte", 70, 40, "akte", fill=GELB, size=48),
    linienzug([(60, BODEN), (1860, BODEN)], "akte", breite=7, farbe=INK),
    ficon("tabler", "building-store", 250, BODEN - 2, 280, "akte", fuell=PINK),
    pille("Café", 250, 520, "akte", fill=WEISS, size=30, anker="m"),
    # Frau Lehmann (Café) links, blickt nach rechts
    peep_voll("LE_ruhig_r", LX_, BODEN, FH, "akte", bis="l1"),
    pille("Frau Lehmann", LX_, BODEN + 22, beim("akte", "Lehmann"), fill=ROT, size=30, anker="m"),
    *redet("LE_redet_r", LX_, BODEN, FH, "l1", "frage"),
    peep_voll("LE_trotz_r", LX_, BODEN, FH, "frage", anim="cut"),
    # Herr Brenner rechts, blickt nach links
    peep_voll("BR_ruhig", BX_, BODEN, FH, "brenner", bis="klage"),
    pille("Herr Brenner", BX_, BODEN + 22, "brenner", fill=BLAU, size=30, anker="m", d=0.2),
    peep_voll("BR_aerger", BX_, BODEN, FH, "klage", anim="cut", bis="b1"),
    *redet("BR_redet", BX_, BODEN, FH, "b1", "l1"),
    peep_voll("BR_aerger", BX_, BODEN, FH, "l1", anim="cut", bis="frage"),
    peep_voll("BR_denkt", BX_, BODEN, FH, "frage", anim="cut"),
    # Kühlschrank: erst beim Händler, dann geliefert
    kuehlschrank(1400, BODEN - 2, 150, beim("akte", "Kühlschrank"), bis="liefer"),
    pille("3.000 €", 1400, 470, beim("akte", "dreitausend"), fill=GELB, size=32, anker="m", bis="liefer"),
    szene(lieferwagen, "018transporter*", 1.0, versatz=-0.5),
    kuehlschrank(800, BODEN - 2, 130, ("liefer", 1.4)),
    pille("geliefert", 800, 670, ("liefer", 1.4), fill=GRUEN, size=28, anker="m"),
    peep_voll("FA_ruhig", FAX, BODEN, FH - 20, ("liefer", 1.4)),
    pille("Fahrer", FAX, BODEN + 22, ("liefer", 1.4), fill=WEISS, size=28, anker="m"),
    pille("Klage: 3.000 €", BX_, 330, beim("klage", "klagt"), fill=GELB, size=32, anker="m", bis="b1"),
    blase("sprech", 640, 190, "b1", 1380, 210, inhalt=["Der Kühlschrank ist geliefert.", "Gezahlt hat sie nie!"],
          textsize=34, figur=BRb, bis="l1"),
    blase("sprech", 620, 190, "l1", 700, 230, inhalt=["Doch! Ich habe dem", "Fahrer bar bezahlt."], textsize=34,
          figur=LEb, bis="frage"),
    ficon("tabler", "cash", FAX, 400, 110, beim("l1", "bar"), fuell=GRUEN, bis="frage"),
    pille("Wer gewinnt?", 960, 200, "frage", fill=PINK, size=44, anker="m"),
    pille("Rechtsfragen", 790, 310, beim("trennt", "Rechtsfragen"), fill=BLAU, size=32, anker="m"),
    pille("Tatsachenfragen", 1150, 310, beim("trennt", "Tatsachenfragen"), fill=GRUEN, size=32, anker="m"),
])

# C Sachverhalt ----------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Herr Brenner, ein Händler, verkauft Frau Lehmann für ihr Café einen Kühlschrank für 3.000 Euro und lässt ihn "
    "liefern. Sein Fahrer darf bei der Lieferung kassieren. Brenner klagt vor dem Amtsgericht auf Zahlung von 3.000 Euro.",
    "Frau Lehmann bestreitet Kauf und Lieferung nicht. Sie sagt: „Ich habe dem Fahrer bei der Lieferung 3.000 Euro bar "
    "bezahlt.“ Eine Quittung hat sie nicht. Brenner bestreitet die Zahlung: Der Fahrer habe nur den Lieferschein "
    "unterschreiben lassen. Frau Lehmann benennt den Fahrer als Zeugen.",
    "Annahme: Klage 2026, Amtsgericht auch örtlich zuständig; Zinsen bleiben außen vor.",
], "Wer gewinnt?")

# D Die Stationen ---------------------------------------------------------------------------------------------------------------
folie([("stat", "Die Stationen der Relation"), (beim("konv", "Ausbildungs"), "Die Stationen › Ausbildungs- und Klausurkonvention")], [
    *tafel("stat", "Die Stationen der Relation"),
    z("I. Prozessstation", 150, 190, beim("stat", "Prozess"), "Bold", 38),
    z("II. Klägerstation", 150, 250, beim("stat", "Kläger"), "Bold", 38),
    z("III. Beklagtenstation", 150, 310, beim("stat", "Beklagter"), "Bold", 38),
    z("IV. Beweisstation", 150, 370, beim("stat", "Beweis"), "Bold", 38),
    z("V. Tenor", 150, 430, beim("stat", "Tenor"), "Bold", 38),
    z("Reihenfolge: in keinem Gesetz geregelt,", 150, 540, beim("konv", "Gesetz"), size=34, farbe=TEXT),
    z("sondern Ausbildungs- und Klausurkonvention", 150, 590, beim("konv", "Ausbildungs"), size=34, farbe=TEXT),
    fl_block(110, 670, 1040, 150, GELB, "prinzip", [("Erst das Recht mit unterstellten Tatsachen,", "Bold", 34, INK),
                                                 ("erst am Ende der Beweis.", "Bold", 34, INK)]),
    peep_voll("RF_denkt", FX, BR, FR, "stat", bis="prinzip"),
    peep_voll("RF_froh", FX, BR, FR, "prinzip", anim="cut"),
    pille("Referendarin", FX, BR + 22, "stat", fill=GRUEN, size=28, anker="m", d=0.2),
    ficon("tabler", "file-stack", FX, 330, 120, "stat", fuell=WEISS),
    pille("kein Gesetz", 1760, 260, beim("konv", "Gesetz"), fill=WEISS, size=28, anker="m"),
])

# E I. Prozessstation ------------------------------------------------------------------------------------------------------------
PI = "I. Prozessstation"
folie([("proz", PI), (beim("proz", "zulässig"), f"{PI} › Zulässigkeit"), ("ag", f"{PI} › sachlich zuständig, § 23 Nr. 1 GVG"),
       ("antrag", f"{PI} › bestimmter Antrag, § 253 II Nr. 2 ZPO")], [
    *tafel("proz", "I. Prozessstation"),
    z("Ist die Klage zulässig?", 150, 195, beim("proz", "zulässig"), "Bold", 40),
    ok(170, 315, beim("ag", "zuständig"), gr=22),
    z("sachlich: Amtsgericht bis 10.000 €", 210, 290, beim("ag", "Amtsgericht"), size=36),
    z("§ 23 Nr. 1 GVG", 250, 340, beim("ag", "sachlich"), size=32, farbe=TEXT),
    ok(170, 445, beim("antrag", "bestimmt"), gr=22),
    z("bestimmter Antrag: 3.000 €", 210, 420, "antrag", size=36),
    z("§ 253 II Nr. 2 ZPO", 250, 470, beim("antrag", "bestimmt"), size=32, farbe=TEXT),
    peep_voll("BR_ruhig", FX, BR, FR, "proz"),
    pille("Herr Brenner", FX, BR + 22, "proz", fill=BLAU, size=28, anker="m", d=0.2),
    ficon("tabler", "building-bank", FX, 330, 140, beim("ag", "Amtsgericht"), fuell=GRUEN, bis="antrag"),
    pille("Amtsgericht", FX, 350, beim("ag", "Amtsgericht"), fill=GRUEN, size=28, anker="m", bis="antrag"),
    ficon("tabler", "file-text", FX, 320, 110, "antrag", fuell=WEISS),
    pille("Antrag: 3.000 €", FX, 340, "antrag", fill=GELB, size=30, anker="m"),
])

# F II. Klägerstation ------------------------------------------------------------------------------------------------------------
PII = "II. Klägerstation"
folie([("kl", PII), ("kv", f"{PII} › Kaufvertrag"), (beim("anspr", "Paragraf"), f"{PII} › Kaufpreis, § 433 II BGB"),
       ("schl", f"{PII} › schlüssig"), ("unschl", f"{PII} › fehlt eine Tatsache"),
       (beim("unschl", "abgewiesen"), f"{PII} › unschlüssig: Abweisung")], [
    *tafel("kl", "II. Klägerstation: Schlüssigkeit", size=46),
    z("Klägervortrag als wahr unterstellt:", 150, 190, beim("kl", "Unterstelle"), "Bold", 38),
    z("Trägt er den Antrag?", 190, 245, beim("kl", "Trägt"), size=36, farbe=TEXT),
    z("Kaufvertrag: Kühlschrank für 3.000 €", 150, 325, "kv", "Bold", 36),
    z("daraus: Anspruch auf den Kaufpreis,", 190, 378, "anspr", size=34, farbe=TEXT),
    z("§ 433 II BGB", 190, 425, beim("anspr", "Paragraf"), size=34, farbe=TEXT),
    ok(170, 520, "schl", gr=24), z("schlüssig", 210, 495, "schl", "ExtraBold", 40),
    fl_block(110, 590, 1040, 230, LILAHELL, "unschl", []),
    z("Fehlt eine nötige Tatsache: unschlüssig", 150, 615, "unschl", "Bold", 34),
    z("kein Nachtrag nach Hinweis (§ 139 ZPO): Abweisung", 150, 670, beim("unschl", "Ergänzt"), size=32, farbe=TEXT),
    z("Beklagtenstation entfällt", 150, 725, beim("unschl", "Beklagten"), size=32, farbe=TEXT),
    peep_voll("BR_ruhig", FX, BR, FR, "kl", bis="schl"),
    peep_voll("BR_froh", FX, BR, FR, "schl", anim="cut", bis="unschl"),
    peep_voll("BR_denkt", FX, BR, FR, "unschl", anim="cut"),
    pille("Herr Brenner", FX, BR + 22, "kl", fill=BLAU, size=28, anker="m", d=0.2),
    pille("als wahr unterstellt", FX, 150, beim("kl", "Unterstelle"), fill=WEISS, size=30, anker="m", bis="schl"),
    kuehlschrank(1460, 400, 110, "kv"),
    pille("3.000 €", 1680, 330, "kv", fill=GELB, size=30, anker="m"),
    pille("schlüssig", FX, 150, "schl", fill=GRUEN, size=30, anker="m", bis="unschl"),
])

# G III. Beklagtenstation: Bestreiten -------------------------------------------------------------------------------------------
PIII = "III. Beklagtenstation"
folie([("bk", f"{PIII} › Erheblichkeit"), ("zug", f"{PIII} › nicht bestritten, § 138 III ZPO"),
       ("nw", f"{PIII} › kein Nichtwissen, § 138 IV ZPO")], [
    *tafel("bk", "III. Beklagtenstation: Erheblichkeit", size=44),
    z("Beklagtenvortrag als wahr unterstellt:", 150, 190, beim("bk", "unterstellst"), "Bold", 38),
    z("Bringt er den Anspruch zu Fall?", 190, 245, beim("bk", "Bringt"), size=36, farbe=TEXT),
    ok(170, 350, beim("zug", "zugestanden"), gr=22),
    z("Kauf und Lieferung: nicht bestritten", 210, 325, "zug", "Bold", 36),
    z("gelten als zugestanden, § 138 III ZPO", 250, 375, beim("zug", "zugestanden"), size=32, farbe=TEXT),
    nein(170, 480, "nw", gr=20),
    z("mit Nichtwissen bestreiten? Nein:", 210, 455, "nw", "Bold", 36),
    z("eigene Handlungen und Wahrnehmungen,", 250, 505, beim("nw", "Handlungen"), size=32, farbe=TEXT),
    z("§ 138 IV ZPO", 250, 550, beim("nw", "Absatz"), size=32, farbe=TEXT),
    peep_voll("LE_ruhig", FX, BR, FR, "bk", bis="nw"),
    peep_voll("LE_denkt", FX, BR, FR, "nw", anim="cut"),
    pille("Frau Lehmann", FX, BR + 22, "bk", fill=ROT, size=28, anker="m", d=0.2),
    pille("als wahr unterstellt", FX, 150, beim("bk", "unterstellst"), fill=WEISS, size=30, anker="m"),
    kuehlschrank(1460, 400, 110, "zug"),
    pille("unstreitig", 1700, 330, beim("zug", "zugestanden"), fill=GRUEN, size=30, anker="m"),
    ficon("tabler", "eye", 1790, 620, 100, beim("nw", "Wahrnehmungen"), fuell=WEISS),
])

# H III. Einwendung: Erfüllung -----------------------------------------------------------------------------------------------
LE2, FA2 = 1400, 1740
folie([("zahl", f"{PIII} › erheblich: die Barzahlung"), (beim("zahl", "Erfüllung"), f"{PIII} › Erfüllung, § 362 I BGB"),
       ("einw", f"{PIII} › Einwendung"), ("einr", f"{PIII} › Einrede, z. B. Verjährung")], [
    *tafel("zahl", "III. Beklagtenstation: Einwendung", size=44),
    ok(170, 215, "zahl", gr=22), z("erheblich: die Barzahlung", 210, 190, "zahl", "Bold", 38),
    z("Fahrer durfte kassieren", 250, 245, beim("zahl", "Fahrer"), size=32, farbe=TEXT),
    z("bezahlt: Erfüllung, § 362 I BGB,", 250, 295, beim("zahl", "Erfüllung"), size=32, farbe=TEXT),
    z("der Anspruch ist erloschen", 250, 340, beim("zahl", "erloschen"), size=32, farbe=TEXT),
    z("Einwendung: beachtet, sobald die", 150, 440, "einw", "Bold", 36),
    z("Tatsachen dazu vorgetragen sind", 190, 490, beim("einw", "vorgetragen"), size=34, farbe=TEXT),
    z("Einrede, z. B. Verjährung (§ 214 I BGB):", 150, 590, "einr", "Bold", 36),
    z("muss erhoben werden", 190, 640, beim("einr", "erheben"), size=34, farbe=TEXT),
    peep_voll("LE_ruhig_r", LE2, BR, FR - 60, "zahl"),
    pille("Frau Lehmann", LE2, BR + 22, "zahl", fill=ROT, size=26, anker="m"),
    peep_voll("FA_ruhig", FA2, BR, FR - 80, beim("zahl", "Fahrer")),
    pille("Fahrer", FA2, BR + 22, beim("zahl", "Fahrer"), fill=WEISS, size=26, anker="m"),
    bewegt(ficon("tabler", "cash", 1580, 560, 100, beim("zahl", "bezahlt"), fuell=GRUEN), beim("zahl", "bezahlt"),
           beim("zahl", "erloschen"), -120, 0),
    pille("§ 362 I BGB", 1580, 330, beim("zahl", "Erfüllung"), fill=GELB, size=28, anker="m"),
    ficon("tabler", "hourglass", 1580, 270, 70, "einr", fuell=GELB),
    pille("Verjährung", 1580, 160, beim("einr", "Verjährung"), fill=WEISS, size=28, anker="m"),
])

# I III. Bestreiten der Zahlung ---------------------------------------------------------------------------------------------
folie([("best", f"{PIII} › Bestreiten, § 138 II ZPO"), (beim("subst", "genügt"), f"{PIII} › Bestreiten: kein bloßes Nein")], [
    *tafel("best", "Brenner bestreitet die Zahlung", size=46),
    z("Erklärungspflicht, § 138 II ZPO:", 150, 190, "p2", "Bold", 36),
    z("jede Partei zu den Behauptungen des Gegners", 190, 240, beim("p2", "Behauptungen"), size=32, farbe=TEXT),
    z("Lehmann sagt genau, wann und wem", 150, 330, "subst", "Bold", 36),
    z("kein bloßes Nein: eigene Schilderung nötig", 190, 380, beim("subst", "bloßes"), size=32, farbe=TEXT),
    z("BGH, Beschl. v. 25.2.2026 – IV ZR 158/24, Rn. 10", 190, 425, beim("subst", "Bundesgerichtshof"), size=26,
      farbe=TEXT),
    ok(170, 535, "lief", gr=22), z("Brenner: Der Fahrer ließ nur den", 210, 510, beim("lief", "Fahrer"), "Bold", 36),
    z("Lieferschein unterschreiben", 250, 560, beim("lief", "Lieferschein"), size=34, farbe=TEXT),
    peep_voll("BR_aerger", FX, BR, FR, "best", bis="lief"),
    peep_voll("BR_ruhig", FX, BR, FR, "lief", anim="cut"),
    pille("Herr Brenner", FX, BR + 22, "best", fill=BLAU, size=28, anker="m", d=0.2),
    ficon("tabler", "cash-off", FX, 300, 110, "best", fuell=ROT, bis="lief"),
    ficon("tabler", "clipboard-text", 1480, 320, 100, beim("lief", "Lieferschein"), fuell=WEISS),
    ficon("tabler", "signature", 1660, 300, 100, beim("lief", "unterschreiben"), fuell=WEISS),
    pille("Lieferschein", FX, 380, beim("lief", "Lieferschein"), fill=WEISS, size=28, anker="m"),
])

# J IV. Beweisstation --------------------------------------------------------------------------------------------------------
PIV = "IV. Beweisstation"
folie([("bs", PIV), (beim("bs", "streitig"), f"{PIV} › streitig und erheblich"), ("last", f"{PIV} › Beweislast"), ("zeuge", f"{PIV} › Zeuge, § 373 ZPO")], [
    *tafel("bs", "IV. Beweisstation"),
    z("Beweis nur über streitige, erhebliche Tatsachen", 150, 190, beim("bs", "braucht"), "Bold", 34),
    z("hier allein: die Barzahlung", 190, 240, "nur", size=34, farbe=TEXT),
    z("Beweislast: Wer muss beweisen?", 150, 330, "last", "Bold", 36),
    z("Jede Partei beweist die Tatsachen", 190, 382, beim("last", "Jede"), size=34, farbe=TEXT),
    z("der Norm, die ihr nützt.", 190, 428, beim("last", "Norm"), size=34, farbe=TEXT),
    z("Erfüllung nützt Frau Lehmann", 190, 480, beim("last", "Erfüllung"), "Bold", 34),
    z("Beweismittel: Zeuge (Fahrer), § 373 ZPO", 150, 570, "zeuge", "Bold", 36),
    peep_voll("LE_ruhig", 1430, BR, FR - 60, "bs", bis="last"),
    peep_voll("LE_denkt", 1430, BR, FR - 60, "last", anim="cut"),
    pille("Frau Lehmann", 1430, BR + 22, "bs", fill=ROT, size=26, anker="m"),
    ficon("tabler", "cash", 1430, 330, 100, "nur", fuell=GRUEN, bis="last"),
    pille("streitig", 1430, 350, "nur", fill=WEISS, size=28, anker="m", bis="last"),
    ficon("tabler", "scale", 1500, 330, 120, beim("last", "Lehmann"), fuell=GELB),
    pille("Beweislast: Lehmann", 1500, 360, beim("last", "Lehmann"), fill=GELB, size=28, anker="m"),
    peep_voll("FA_ruhig", 1760, BR, FR - 80, "zeuge"),
    pille("Zeuge", 1760, BR + 22, "zeuge", fill=WEISS, size=26, anker="m"),
])

# K Beweisaufnahme im Sitzungssaal ------------------------------------------------------------------------------------------
RIX, LEK, BRK, FAK = 1010, 270, 590, 1580
FAb = ("FA_redet", FAK, BODEN, FH)
folie([("f1", f"{PIV} › Zeuge: der Fahrer"), ("wuerd", f"{PIV} › freie Beweiswürdigung, § 286 ZPO"),
       (beim("nl", "Zahlung"), f"{PIV} › Ergebnis: Zahlung nicht bewiesen"),
       (beim("lastfolge", "zulasten"), f"{PIV} › Beweislast: Frau Lehmann")], [
    linienzug([(60, BODEN), (1860, BODEN)], "f1", breite=7, farbe=INK),
    pille("Amtsgericht · Beweisaufnahme", 70, 40, "f1", fill=GRAU, size=36),
    peep_voll("RI_ruhig", RIX, 640, 380, "f1", bis="wuerd"),
    peep_voll("RI_denkt", RIX, 640, 380, "wuerd", anim="cut", bis="nl"),
    peep_voll("RI_ruhig", RIX, 640, 380, "nl", anim="cut"),
    fl_block(790, 560, 440, 110, DUNKEL, "f1", [("Gericht", "Bold", 32, WEISS)], rand=5),
    peep_voll("LE_sorge_r", LEK, BODEN, FH, "f1", bis="nl"),
    peep_voll("LE_schreck_r", LEK, BODEN, FH, "nl", anim="cut"),
    pille("Beklagte Lehmann", LEK, BODEN + 22, "f1", fill=ROT, size=28, anker="m", d=0.2),
    peep_voll("BR_ruhig_r", BRK, BODEN, FH, "f1", bis="nl"),
    peep_voll("BR_froh_r", BRK, BODEN, FH, "nl", anim="cut"),
    pille("Kläger Brenner", BRK, BODEN + 22, "f1", fill=BLAU, size=28, anker="m", d=0.2),
    peep_voll("FA_ruhig", FAK, BODEN, FH, ("f1", -0.2), bis="f1"),
    *redet("FA_redet", FAK, BODEN, FH, "f1", "wuerd"),
    peep_voll("FA_ruhig", FAK, BODEN, FH, "wuerd", anim="cut"),
    pille("Zeuge: der Fahrer", FAK, BODEN + 22, "f1", fill=WEISS, size=28, anker="m", d=0.2),
    blase("sprech", 620, 190, "f1", 1420, 210, inhalt=["Geld habe ich nicht bekommen.", "Nur ihre Unterschrift."],
          textsize=34, figur=FAb, bis="wuerd"),
    pille("freie Beweiswürdigung, § 286 I ZPO", 430, 180, "wuerd", fill=GELB, size=30, anker="m"),
    pille("Beweisregeln nur, wo das Gesetz sie anordnet", 430, 260, beim("regel", "Beweisregeln"), fill=WEISS, size=24,
          anker="m"),
    pille("Mitarbeiter des Klägers", FAK, 330, beim("regel", "Mitarbeiter"), fill=WEISS, size=28, anker="m", bis="lastfolge"),
    pille("Zahlung nicht bewiesen", 430, 340, beim("nl", "Zahlung"), fill=ROT, size=30, anker="m"),
    ficon("tabler", "scale", FAK, 300, 110, "lastfolge", fuell=GELB),
    pille("Beweislast: Frau Lehmann", FAK, 340, beim("lastfolge", "Beweislast"), fill=GELB, size=28, anker="m"),
])

# L V. Tenor -----------------------------------------------------------------------------------------------------------------
PV = "V. Tenor"
RFt = ("RF_redet", FX, BR, FR)
folie([("ten", PV), ("neben", f"{PV} › Kosten und vorläufige Vollstreckbarkeit")], [
    *tafel("ten", "V. Tenor"),
    z("Die Referendarin formuliert den Tenor:", 150, 190, beim("ten", "Referendarin"), "Bold", 36),
    fl_block(110, 260, 1040, 160, GELB, "t1", [("Die Beklagte wird verurteilt, an den", "Bold", 36, INK),
                                               ("Kläger 3.000 € zu zahlen.", "Bold", 36, INK)]),
    z("Nebenentscheidungen:", 150, 480, "neben", "Bold", 36),
    z("Kosten, § 91 I ZPO", 190, 535, beim("neben", "Kosten"), size=34, farbe=TEXT),
    z("vorläufige Vollstreckbarkeit, § 709 S. 1 ZPO", 190, 585, beim("neben", "vorläufige"), size=34, farbe=TEXT),
    peep_voll("RF_ruhig", FX, BR, FR, "ten", bis="t1"),
    *redet("RF_redet", FX, BR, FR, "t1", "neben"),
    peep_voll("RF_ruhig", FX, BR, FR, "neben", anim="cut"),
    pille("Referendarin", FX, BR + 22, "ten", fill=GRUEN, size=28, anker="m", d=0.2),
    blase("sprech", 600, 230, "t1", 1560, 240, inhalt=["Die Beklagte wird verurteilt,", "an den Kläger", "3.000 Euro zu zahlen."],
          textsize=30, figur=RFt, bis="neben"),
    ficon("tabler", "file-text", FX, 320, 110, "neben", fuell=WEISS),
])

# M Und im Urteil? -------------------------------------------------------------------------------------------------------------
folie([("urt", "Und im Urteil?"), (beim("urt", "Überschrift"), "Urteil › keine Relations-Überschriften"), ("p313", "Urteil › Aufbau, § 313 ZPO")], [
    *tafel("urt", "Und im Urteil?"),
    z("Relation: keine Überschrift im Urteil", 150, 190, beim("urt", "Überschrift"), "Bold", 38),
    z("Gliederung, § 313 I Nr. 4–6 ZPO:", 150, 290, "p313", "Bold", 36),
    z("1. Urteilsformel (Tenor)", 190, 345, beim("p313", "Urteilsformel"), size=34, farbe=TEXT),
    z("2. Tatbestand", 190, 395, beim("p313", "Tatbestand"), size=34, farbe=TEXT),
    z("3. Entscheidungsgründe", 190, 445, beim("p313", "Entscheidungsgründen"), size=34, farbe=TEXT),
    z("Gründe: tragende Erwägungen kurz,", 150, 545, "ugr", "Bold", 36),
    z("§ 313 III ZPO, im Urteilsstil", 190, 595, beim("ugr", "Urteilsstil"), size=34, farbe=TEXT),
    peep_voll("RF_denkt", FX, BR, FR, "urt", bis="ugr"),
    peep_voll("RF_froh", FX, BR, FR, "ugr", anim="cut"),
    pille("Referendarin", FX, BR + 22, "urt", fill=GRUEN, size=28, anker="m", d=0.2),
    pille("Klägerstation", 1500, 170, beim("urt", "Relation"), fill=WEISS, size=28, anker="m", bis="ugr"),
    pille("Beklagtenstation", 1500, 235, beim("urt", "Relation"), fill=WEISS, size=28, anker="m", bis="ugr"),
    pille("Beweisstation", 1500, 300, beim("urt", "Relation"), fill=WEISS, size=28, anker="m", bis="ugr"),
    bis_(nein(1750, 235, beim("urt", "Überschrift"), gr=34), "ugr"),
    ficon("tabler", "file-text", FX, 330, 120, "ugr", fuell=WEISS),
    pille("Urteil", FX, 350, "ugr", fill=WEISS, size=30, anker="m"),
])

# N Klausurtipp (Lexi) ---------------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · kein Beweis über Unstreitiges"), ("tipp2", "Klausurtipp · Beweislast prüfen")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Nie Beweis über Unstreitiges", 200, 200, beim("tipp", "Erhebe"), "Bold", 38),
    z("Immer fragen: Wer trägt die Beweislast?", 200, 320, beim("tipp2", "frage"), "Bold", 36),
    z("Bestreiten hilft nur gegen Tatsachen,", 240, 385, beim("tipp2", "Bestreiten"), size=34, farbe=TEXT),
    z("die der Gegner beweisen muss.", 240, 435, beim("tipp2", "Gegner"), size=34, farbe=TEXT),
    *redet("LX_warnt", LXX, BR, FR + 60, "tipp", "sch"),
    pille("Lexi", LXX, BR + 22, "tipp", fill=GELB, size=30, anker="m", d=0.2),
])

# O Klausurschema ---------------------------------------------------------------------------------------------------------------
K1, K2 = 150, 210
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel("Klausurschema: Relation", 110, 90, "sch", 54),
    z("I. Prozessstation: Zulässigkeit (z. B. § 23 Nr. 1 GVG, § 253 II ZPO)", K1, 190, "sI", "Bold", 34, rechts=1820),
    z("II. Klägerstation: Schlüssigkeit (Klägervortrag als wahr unterstellt)", K1, 275, "sII", "Bold", 34, rechts=1820),
    z("III. Beklagtenstation: Erheblichkeit", K1, 360, "sIII", "Bold", 34, rechts=1820),
    z("Bestreiten (§ 138 II–IV ZPO)", K2, 410, beim("sIII", "Bestreiten"), size=32, farbe=TEXT, rechts=1820),
    z("Einwendungen (z. B. Erfüllung, § 362 BGB) und Einreden (z. B. Verjährung, § 214 BGB)", K2, 455,
      beim("sIII", "Einwendungen"), size=32, farbe=TEXT, rechts=1820),
    z("IV. Beweisstation: nur streitige, erhebliche Tatsachen", K1, 540, "sIV", "Bold", 34, rechts=1820),
    z("Beweislast, freie Beweiswürdigung (§ 286 ZPO)", K2, 590, beim("sIV", "Beweislast"), size=32, farbe=TEXT,
      rechts=1820),
    z("V. Tenor: Hauptsache, Kosten (§ 91 ZPO), vorläufige Vollstreckbarkeit (§§ 708 ff. ZPO)", K1, 675, "sV", "Bold",
      34, rechts=1820),
])

# P Merksatz (Lexi) -------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Erst prüfst du das Recht", 0)], [("mit unterstellten Tatsachen.", "a")]], 750, 320, 54, "merke",
                {"a": beim("merke", "unterstellten")}),
    *markertext([[("Bewiesen wird nur, was", 0)], [("streitig und erheblich ist.", "b")]], 750, 560, 54, "m2",
                {"b": beim("m2", "streitig")}),
    *redet("LX_erklaert", 1680, 1000, 720, "merke", lexi_bis_ende("merke")),
])
