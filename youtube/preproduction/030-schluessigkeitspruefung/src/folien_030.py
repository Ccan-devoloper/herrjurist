"""Folge 030 · Schlüssigkeitsprüfung: Der Test, den jede Klage bestehen muss – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A Am Gartenzaun (Darlehen), B Die Klageschrift (Fall, Frage), C Sachverhalt, D Der Test und
die BGH-Formel, E I. Anspruchsgrundlage (Wortlautkarte § 488 I 2 BGB), F II. Tatsachenvortrag, G II. Fälligkeit
(Wortlautkarte § 488 III BGB), H III. Hinweis (Wortlautkarte § 139 I 2 ZPO, Richterin) und IV. Ergebnis, I Substantiierung,
J Abgrenzung Beweisstation (Sitzungssaal), K Abgrenzung Zulässigkeit (Wortlautkarte § 253 II Nr. 2 ZPO), L Folge der
Unschlüssigkeit und Versäumnisurteil (Wortlautkarten § 331 I 1, II ZPO), M Klausurtipp (Lexi), N Klausurschema,
O Merksatz (Lexi). Geräusch nur bei sichtbarer Handlung: Tippen am Laptop (Szene B, Freesound CC0)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont

bausteine.FIGORDNER = "op_030/"
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


BODEN, FH = 880, 480
BR, FR = 930, 480                       # Figuren rechts neben der Tafel
X1, X2 = 1420, 1720                     # zwei Figuren neben der Tafel
MB = (X1 + X2) // 2

# A Fall: am Gartenzaun ------------------------------------------------------------------------------------------------
SX, FX = 560, 1360
FRa = ("FR_redet", FX, BODEN, FH)
geld = bewegt(ficon("tabler", "cash", 1180, 600, 110, beim("ueberw", "überweist"), fuell=GRUEN, bis="juli"),
              beim("ueberw", "überweist"), beim("ueberw", "Geld", ende=True), -480, 0)
folie([(NULL, "Fall · Das Darlehen"), (beim("juli", "zahlt"), "Fall · Herr Franke zahlt nicht")], [
    linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK),
    pl("Am Gartenzaun", 70, 40, NULL, fill=GELB, size=40),
    ficon("tabler", "home", 230, BODEN - 2, 250, NULL, fuell=BLAU),
    ficon("tabler", "home", 1700, BODEN - 2, 250, NULL, fuell=GELB),
    ficon("tabler", "fence", 960, BODEN - 2, 300, NULL, fuell=HOLZ),
    peep_voll("SC_ruhig_r", SX, BODEN, FH, NULL, bis="f1"),
    peep_voll("SC_froh_r", SX, BODEN, FH, "f1", anim="cut", bis="juli"),
    peep_voll("SC_sorge_r", SX, BODEN, FH, "juli", anim="cut"),
    namensschild("Frau Schubert", SX, BODEN, NULL, BLAU),
    peep_voll("FR_ruhig", FX, BODEN, FH, beim("fall", "Herrn"), bis="f1"),
    *redet("FR_redet", FX, BODEN, FH, "f1", "juli"),
    peep_voll("FR_ruhig", FX, BODEN, FH, "juli", anim="cut", bis=beim("juli", "zahlt")),
    peep_voll("FR_muede", FX, BODEN, FH, beim("juli", "zahlt"), anim="cut"),
    namensschild("Herr Franke", FX, BODEN, beim("fall", "Herrn"), GRUEN),
    pl("Darlehen: 6.000 €", SX, 300, beim("fall", "sechstausend"), fill=GELB, size=32, anker="m"),
    ficon("tabler", "device-mobile", 760, 560, 70, beim("ueberw", "überweist"), fuell=WEISS),
    pl("Januar: überwiesen", 960, 420, beim("ueberw", "Januar"), fill=WEISS, size=30, anker="m", bis="f1"),
    geld,
    blase("sprech", 640, 200, "f1", 1150, 200, inhalt=["Danke! Ende Juni", "haben Sie alles zurück."], textsize=36,
          figur=FRa, bis="juli"),
    ficon("tabler", "calendar-event", 960, 560, 100, beim("f1", "Ende"), fuell=WEISS, bis="juli"),
    pl("Ende Juni", 960, 420, beim("f1", "Ende"), fill=GRUEN, size=30, anker="m", bis="juli"),
    ficon("tabler", "calendar-x", 960, 560, 100, beim("juli", "Juli"), fuell=ROT, anim="cut"),
    pl("Juli", 960, 420, beim("juli", "Juli"), fill=ROT, size=30, anker="m", anim="cut"),
    ficon("tabler", "cash-off", 1180, 600, 110, beim("juli", "zahlt"), fuell=ROT),
    pl("zahlt nicht", 1180, 640, beim("juli", "zahlt"), fill=WEISS, size=28, anker="m"),
])

# B Fall: die Klageschrift ------------------------------------------------------------------------------------------------
SB, GX = 1010, 1650
SCb = ("SC_redet", SB, BODEN, FH)
folie([("klage", "Fall · Die Klage"), ("frage", "Fall · Die Frage")], [
    linienzug([(60, BODEN), (1860, BODEN)], "klage", breite=7, farbe=INK),
    pl("Frau Schuberts Klage", 70, 40, "klage", fill=GELB, size=40),
    ficon("tabler", "desk", 560, BODEN - 2, 560, "klage", fuell=HOLZ),
    ficon("tabler", "device-laptop", 560, 478, 170, "klage", fuell=WEISS),
    peep_voll("SC_denkt", SB, BODEN, FH, "klage", bis="s1"),
    *redet("SC_redet", SB, BODEN, FH, "s1", "frage"),
    peep_voll("SC_ruhig", SB, BODEN, FH, "frage", anim="cut"),
    namensschild("Frau Schubert", SB, BODEN, "klage", BLAU),
    ficon("tabler", "building-bank", GX, BODEN - 2, 280, beim("klage", "Amtsgericht"), fuell=GRUEN),
    pl("Amtsgericht", GX, 520, beim("klage", "Amtsgericht"), fill=GRUEN, size=30, anker="m"),
    szene(ficon("tabler", "file-text", 380, 470, 80, beim("klage", "klagt"), fuell=WEISS), "030tastatur*", 1.0, versatz=0.05),
    pl("Klage: 6.000 €", GX, 430, beim("klage", "sechstausend"), fill=GELB, size=30, anker="m"),
    pl("Klageschrift", 380, 300, "schrift", fill=WEISS, size=30, anker="m", bis="s1"),
    blase("sprech", 940, 270, "s1", 690, 240, inhalt=["Ich habe mit dem Beklagten vereinbart,",
                                                    "ihm 6.000 Euro zu leihen, und sie überwiesen.",
                                                    "Das Darlehen ist fällig."], textsize=32, figur=SCb, bis="frage"),
    pl("Der Test, den jede Klage bestehen muss", 700, 200, "frage", fill=WEISS, size=34, anker="m"),
    pl("Ist sie schlüssig?", 700, 300, "frage2", fill=PINK, size=44, anker="m"),
])

# C Sachverhalt ----------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    glyphen("Frau Schubert leiht ihrem Nachbarn Herrn Franke 6.000 Euro und überweist sie ihm im Januar 2026. Mündlich "
            "vereinbaren beide: Rückzahlung bis Ende Juni. Herr Franke zahlt nicht. Im August klagt Frau Schubert vor dem "
            "Amtsgericht auf Zahlung von 6.000 Euro."),
    glyphen("In der Klageschrift steht nur: „Ich habe mit dem Beklagten vereinbart, ihm 6.000 Euro zu leihen, und sie "
            "überwiesen. Das Darlehen ist fällig.“ Zum Rückzahlungstermin schreibt sie nichts. Gekündigt hat sie das "
            "Darlehen nicht, auch nicht in der Klageschrift."),
    glyphen("Annahme: Zinsen bleiben außen vor; die übrigen Zulässigkeitsvoraussetzungen liegen vor."),
], "Ist die Klage schlüssig?")

# D Der Test und die Formel des BGH ----------------------------------------------------------------------------------------
folie([("stat", "Klägerstation · Schlüssigkeit"),
       (beim("stat", "Ausbildungs"), "Klägerstation › Ausbildungs- und Klausurkonvention"),
       ("test", "Klägerstation › Der Test: als wahr unterstellt"),
       ("formel", "Klägerstation › Die Formel des BGH")], rechts_frei([
    *tafel("stat", "Die Schlüssigkeitsprüfung"),
    z("Ort: die Klägerstation", 110, 185, beim("stat", "Klägerstation"), "Bold", 36),
    z("Stationen: Ausbildungs- und Klausurkonvention", 150, 235, beim("stat", "Ausbildungs"), size=32, farbe=TEXT),
    z("Der Test: Trägt der Vortrag der Klägerin,", 110, 310, beim("test", "Trägt"), "Bold", 36),
    z("als wahr unterstellt, ihren Antrag?", 150, 360, beim("test", "als"), "Bold", 36),
    *wortlaut(110, 450, 1040, 240, "formel", [
        [("„Sachvortrag zur Begründung eines Anspruchs ist dann", 0)],
        [("schlüssig und erheblich, wenn die Partei ", 0), ("Tatsachen", "a"), (" vorträgt,", 0)],
        [("die in Verbindung mit einem ", 0), ("Rechtssatz", "b"), (" ", 0), ("geeignet und", "c")],
        [("erforderlich", "c"), (" sind, das geltend gemachte Recht als in der", 0)],
        [("Person der Partei ", 0), ("entstanden", "d"), (" erscheinen zu lassen.“", 0)],
    ], 30, {"a": beim("formel", "Tatsachen"), "b": beim("formel", "Rechtssatz"), "c": beim("formel", "geeignet"),
            "d": beim("formel", "entstanden")}, "BGH, Beschl. v. 1.7.2025 – VI ZR 357/24, Rn. 11"),
    peep_voll("SC_ruhig", X1, BR, FR, "stat", bis="test"),
    peep_voll("SC_denkt", X1, BR, FR, "test", anim="cut"),
    peep_voll("FR_ruhig", X2, BR, FR, "stat", d=0.2),
    namensschild("Frau Schubert", X1, BR, "stat", BLAU, d=0.2),
    namensschild("Herr Franke", X2, BR, "stat", GRUEN, d=0.3),
    ficon("tabler", "file-text", MB, 380, 100, "stat", fuell=WEISS),
    pl("Klageschrift", MB, 160, "stat", fill=WEISS, size=28, anker="m", bis="test"),
    pl("als wahr unterstellt", MB, 160, beim("test", "als"), fill=GELB, size=28, anker="m", anim="cut"),
]))

# E I. Anspruchsgrundlage ---------------------------------------------------------------------------------------------------
PI = "I. Anspruchsgrundlage"
folie([("rs", PI), (beim("rs", "Paragraf"), f"{PI} › § 488 Abs. 1 S. 2 BGB"), ("drei", f"{PI} › drei Merkmale")], rechts_frei([
    *tafel("rs", "I. Anspruchsgrundlage"),
    z("Rechtssatz: § 488 Abs. 1 S. 2 BGB", 110, 185, beim("rs", "Paragraf"), "Bold", 36),
    *wortlaut(110, 260, 1040, 160, "rs2", [
        [("„Der Darlehensnehmer ist verpflichtet, einen geschuldeten", 0)],
        [("Zins zu zahlen und ", 0), ("bei Fälligkeit", "a"), (" das zur Verfügung", 0)],
        [("gestellte Darlehen ", 0), ("zurückzuzahlen", "b"), (".“", 0)],
    ], 30, {"a": beim("rs2", "Fälligkeit"), "b": beim("rs2", "zurückzahlen")}, "§ 488 Abs. 1 S. 2 BGB"),
    z("Drei Merkmale:", 110, 500, "drei", "Bold", 38),
    z("1. Darlehensvertrag", 150, 560, beim("drei", "Darlehensvertrag"), "Bold", 36),
    z("2. Auszahlung", 150, 615, beim("drei", "Auszahlung"), "Bold", 36),
    z("3. Fälligkeit", 150, 670, beim("drei", "Fälligkeit"), "Bold", 36),
    peep_voll("SC_ruhig", X1, BR, FR, "rs"),
    peep_voll("FR_ruhig", X2, BR, FR, "rs", d=0.2, bis="rs2"),
    peep_voll("FR_denkt", X2, BR, FR, "rs2", anim="cut"),
    namensschild("Frau Schubert", X1, BR, "rs", BLAU, d=0.2),
    namensschild("Herr Franke", X2, BR, "rs", GRUEN, d=0.3),
    ficon("tabler", "book", MB, 380, 110, beim("rs", "Paragraf"), fuell=BLAU),
    pl("§ 488 BGB", MB, 160, beim("rs", "Paragraf"), fill=WEISS, size=30, anker="m", bis="drei"),
    pl("3 Merkmale", MB, 160, "drei", fill=GELB, size=30, anker="m", anim="cut"),
]))

# F II. Tatsachenvortrag ------------------------------------------------------------------------------------------------------
PII = "II. Tatsachenvortrag"
T2 = 560
folie([("tats", PII), ("m1", f"{PII} › Darlehensvertrag"), ("m2", f"{PII} › Auszahlung"), ("m3", f"{PII} › Fälligkeit?")], rechts_frei([
    *tafel("tats", "II. Tatsachenvortrag"),
    z("Merkmal", 150, 190, beim("tats", "Ordne"), "ExtraBold", 34, farbe=TEXT),
    z("vorgetragene Tatsache", T2, 190, beim("tats", "Tatsache"), "ExtraBold", 34, farbe=TEXT),
    z("1. Darlehensvertrag", 150, 270, "m1", "Bold", 34),
    z("vereinbart, ihm das Geld zu leihen", T2, 270, "m1", size=32),
    ok(1110, 290, beim("m1", "trägt"), gr=22),
    z("2. Auszahlung", 150, 350, "m2", "Bold", 34),
    z("überwiesen", T2, 350, "m2", size=32),
    ok(1110, 370, beim("m2", "trägt"), gr=22),
    z("3. Fälligkeit", 150, 430, "m3", "Bold", 34),
    z("„fällig“", T2, 430, "m3", size=32),
    nein(1110, 450, beim("m3", "keine"), gr=20),
    z("keine Tatsache, sondern rechtliche Bewertung", T2 - 60, 490, beim("m3", "keine"), size=30, farbe=TEXT),
    fl_block(110, 600, 1040, 120, LILAHELL, beim("m3", "Als"), [("Als wahr unterstellt werden nur Tatsachen.", "Bold", 36, INK)]),
    peep_voll("SC_ruhig", X1, BR, FR, "tats", bis="m3"),
    peep_voll("SC_sorge", X1, BR, FR, "m3", anim="cut"),
    peep_voll("FR_ruhig", X2, BR, FR, "tats", d=0.2),
    namensschild("Frau Schubert", X1, BR, "tats", BLAU, d=0.2),
    namensschild("Herr Franke", X2, BR, "tats", GRUEN, d=0.3),
    ficon("tabler", "file-text", MB, 380, 100, "tats", fuell=WEISS),
    pl("vereinbart", MB, 160, "m1", fill=GRUEN, size=28, anker="m", bis="m2"),
    pl("überwiesen", MB, 160, "m2", fill=GRUEN, size=28, anker="m", anim="cut", bis="m3"),
    pl("„fällig“?", MB, 160, "m3", fill=PINK, size=28, anker="m", anim="cut"),
]))

# G II. Fälligkeit, § 488 III BGB ------------------------------------------------------------------------------------------
folie([("p488", f"{PII} › Fälligkeit, § 488 Abs. 3 BGB"),
       (beim("fehlt", "Rückzahlungstermin"), f"{PII} › kein Termin, keine Kündigung vorgetragen"),
       (beim("fehlt", "unschlüssig"), f"{PII} › unschlüssig")], rechts_frei([
    *tafel("p488", "II. Tatsachenvortrag: Fälligkeit", size=46),
    *wortlaut(110, 190, 1040, 200, "p488", [
        [("„Ist für die Rückzahlung des Darlehens ", 0), ("eine Zeit nicht bestimmt", "a"), (",", 0)],
        [("so hängt die Fälligkeit davon ab, dass der Darlehensgeber", 0)],
        [("oder der Darlehensnehmer ", 0), ("kündigt", "b"), (". Die Kündigungsfrist", 0)],
        [("beträgt ", 0), ("drei Monate", "c"), (".“", 0)],
    ], 30, {"a": beim("p488", "Zeit"), "b": beim("p488", "Kündigung"), "c": beim("p488", "drei")},
        "§ 488 Abs. 3 S. 1, 2 BGB"),
    z("Rückzahlungstermin vorgetragen?", 150, 480, beim("fehlt", "Rückzahlungstermin"), "Bold", 36),
    nein(1110, 500, beim("fehlt", "schreibt"), gr=20),
    z("Kündigung vorgetragen?", 150, 545, beim("fehlt", "Kündigung"), "Bold", 36),
    nein(1110, 565, beim("fehlt", "nichts"), gr=20),
    fl_block(110, 640, 1040, 120, ROTHELL, beim("fehlt", "unschlüssig"), [("Die Klage ist unschlüssig.", "ExtraBold", 40, INK)]),
    peep_voll("SC_sorge", X1, BR, FR, "p488", bis=beim("fehlt", "unschlüssig")),
    peep_voll("SC_schreck", X1, BR, FR, beim("fehlt", "unschlüssig"), anim="cut"),
    peep_voll("FR_ruhig", X2, BR, FR, "p488", d=0.2, bis=beim("fehlt", "unschlüssig")),
    peep_voll("FR_redet", X2, BR, FR, beim("fehlt", "unschlüssig"), anim="cut"),
    namensschild("Frau Schubert", X1, BR, "p488", BLAU, d=0.2),
    namensschild("Herr Franke", X2, BR, "p488", GRUEN, d=0.3),
    ficon("tabler", "calendar-x", MB, 380, 100, beim("p488", "Zeit"), fuell=WEISS, bis=beim("p488", "Kündigung")),
    pl("keine Zeit bestimmt", MB, 160, beim("p488", "Zeit"), fill=WEISS, size=28, anker="m", bis=beim("p488", "Kündigung")),
    ficon("tabler", "mail", MB, 380, 100, beim("p488", "Kündigung"), fuell=WEISS, anim="cut", bis="fehlt"),
    pl("Kündigung, 3 Monate", MB, 160, beim("p488", "Kündigung"), fill=GELB, size=28, anker="m", anim="cut", bis="fehlt"),
    ficon("tabler", "file-x", MB, 380, 100, "fehlt", fuell=ROT, anim="cut"),
    pl("fehlt im Vortrag", MB, 160, "fehlt", fill=ROT, size=28, anker="m", anim="cut"),
]))

# H III. Hinweis, § 139 ZPO; IV. Ergebnis ------------------------------------------------------------------------------------
RIb = ("RI_redet", X2, BR, FR)
folie([("hinw", "III. Hinweis"), ("hw", "III. Hinweis, § 139 Abs. 1 ZPO"),
       ("frueh", "III. Hinweis › so früh wie möglich, aktenkundig"), ("r1", "III. Hinweis › die Richterin"),
       ("ergz", "III. Hinweis › Ergänzung"), ("schl", "IV. Ergebnis › schlüssig")], rechts_frei([
    *tafel("hinw", "III. Hinweis, § 139 ZPO"),
    z("Sofort abweisen?", 110, 185, "hinw", "Bold", 36),
    nein(445, 210, beim("hinw", "Nein"), gr=20),
    *wortlaut(110, 260, 1040, 160, "hw", [
        [("„Es hat dahin zu wirken, dass die Parteien … insbesondere", 0)],
        [("ungenügende Angaben", "a"), (" zu den geltend gemachten Tatsachen", 0)],
        [("ergänzen", "b"), (", …“", 0)],
    ], 30, {"a": beim("hw", "ungenügende"), "b": beim("hw", "ergänzen")}, "§ 139 Abs. 1 S. 2 ZPO"),
    z("Hinweis so früh wie möglich, aktenkundig", 110, 490, "frueh", "Bold", 34),
    z("§ 139 Abs. 4 S. 1 ZPO", 150, 540, beim("frueh", "aktenkundig"), size=30, farbe=TEXT),
    z("Ergänzung: Rückzahlung bis Ende Juni vereinbart", 110, 620, "ergz", "Bold", 34),
    ok(135, 720, beim("schl", "schlüssig"), gr=22),
    z("IV. Ergebnis: Der Vortrag trägt den Antrag.", 175, 700, "schl", "Bold", 34),
    z("Die Klage ist schlüssig.", 175, 750, beim("schl", "Die"), "ExtraBold", 36),
    peep_voll("SC_sorge", X1, BR, FR, "hinw", bis="ergz"),
    peep_voll("SC_redet", X1, BR, FR, "ergz", anim="cut", bis="schl"),
    peep_voll("SC_froh", X1, BR, FR, "schl", anim="cut"),
    namensschild("Frau Schubert", X1, BR, "hinw", BLAU, d=0.2),
    peep_voll("RI_ruhig", X2, BR, FR, "hinw", d=0.2, bis="r1"),
    *redet("RI_redet", X2, BR, FR, "r1", "ergz"),
    peep_voll("RI_froh", X2, BR, FR, "ergz", anim="cut"),
    namensschild("Richterin", X2, BR, "hinw", LILA, d=0.3),
    ficon("tabler", "file-text", MB, 380, 100, "frueh", fuell=WEISS, bis="r1"),
    pl("Hinweis in der Akte", MB, 160, "frueh", fill=WEISS, size=28, anker="m", bis="r1"),
    blase("sprech", 600, 230, "r1", 1560, 200, inhalt=["Zur Fälligkeit fehlt Vortrag.", "Wann sollte das Geld",
                                                     "zurückgezahlt werden?"], textsize=30, figur=RIb, bis="ergz"),
    ficon("tabler", "calendar-check", MB, 380, 100, beim("ergz", "Ende"), fuell=GRUEN),
    pl("bis Ende Juni", MB, 160, beim("ergz", "Ende"), fill=GRUEN, size=28, anker="m", bis="schl"),
    pl("schlüssig", MB, 160, beim("schl", "schlüssig"), fill=GRUEN, size=30, anker="m", anim="cut"),
]))

# I Substantiierung --------------------------------------------------------------------------------------------------------
folie([("subst", "Substantiierung › Tag und Ort der Abrede?"),
       ("einz", "Substantiierung › Einzelheiten nur, soweit bedeutsam"),
       ("unter", "Schlüssigkeit oder Substantiierung?"),
       (beim("unter", "überspannen"), "Substantiierung › nicht überspannen")], rechts_frei([
    *tafel("subst", "Wie genau muss sie vortragen?", size=46),
    z("Tag und Ort der Abrede nötig?", 110, 185, "subst", "Bold", 36),
    nein(670, 210, beim("subst", "Nein"), gr=20),
    *wortlaut(110, 260, 1040, 120, "einz", [
        [("„Die Angabe näherer Einzelheiten ist ", 0), ("nicht erforderlich", "a"), (",", 0)],
        [("soweit diese für die ", 0), ("Rechtsfolgen", "b"), (" nicht von Bedeutung sind.“", 0)],
    ], 30, {"a": beim("einz", "nicht"), "b": beim("einz", "Rechtsfolgen")}, "BGH, Beschl. v. 1.7.2025 – VI ZR 357/24, Rn. 11"),
    fl_block(110, 470, 500, 200, BLAU, "unter", [("Schlüssigkeit:", "ExtraBold", 34, INK), ("Jedes Merkmal mit", "Bold", 30, INK),
                                               ("Tatsachen belegt?", "Bold", 30, INK)]),
    fl_block(650, 470, 500, 200, GRUEN, beim("unter", "Substantiierung"), [("Substantiierung:", "ExtraBold", 34, INK),
                                                                        ("Wie genau?", "Bold", 30, INK)]),
    z("nicht überspannen (BGH, a. a. O., Rn. 10)", 110, 720, beim("unter", "überspannen"), "Bold", 34),
    peep_voll("SC_denkt", X1, BR, FR, "subst", bis="einz"),
    peep_voll("SC_froh", X1, BR, FR, "einz", anim="cut"),
    peep_voll("FR_ruhig", X2, BR, FR, "subst", d=0.2),
    namensschild("Frau Schubert", X1, BR, "subst", BLAU, d=0.2),
    namensschild("Herr Franke", X2, BR, "subst", GRUEN, d=0.3),
    ficon("tabler", "calendar-event", MB, 380, 100, "subst", fuell=WEISS),
    pl("Tag? Ort?", MB, 160, "subst", fill=PINK, size=30, anker="m", bis="einz"),
    pl("nicht erforderlich", MB, 160, beim("einz", "nicht"), fill=GRUEN, size=28, anker="m", anim="cut"),
]))

# J Abgrenzung Beweisstation (Sitzungssaal) -----------------------------------------------------------------------------------
RIX, SCK, FRK = 960, 330, 1590
FRb = ("FR_trotz", FRK, BODEN, FH)
folie([("f2", "Abgrenzung › Bestreiten"), (beim("best", "Beklagtenstation"), "Abgrenzung › Bestreiten: Beklagtenstation"),
       ("bew", "Abgrenzung › Beweisstation")], [
    linienzug([(60, BODEN), (1860, BODEN)], "f2", breite=7, farbe=INK),
    pl("Amtsgericht · mündliche Verhandlung", 70, 40, "f2", fill=GRAU, size=36),
    peep_voll("RI_ruhig", RIX, 640, 380, "f2", bis="bew"),
    peep_voll("RI_denkt", RIX, 640, 380, "bew", anim="cut"),
    fl_block(740, 560, 440, 110, DUNKEL, "f2", [("Gericht", "Bold", 32, WEISS)], rand=5),
    pille("Richterin", RIX, 690, "f2", fill=LILA, size=28, anker="m", d=0.2),
    peep_voll("SC_ruhig_r", SCK, BODEN, FH, "f2", bis=beim("f2", "Rede")),
    peep_voll("SC_aerger_r", SCK, BODEN, FH, beim("f2", "Rede"), anim="cut", bis="bew"),
    peep_voll("SC_denkt_r", SCK, BODEN, FH, "bew", anim="cut"),
    namensschild("Klägerin Schubert", SCK, BODEN, "f2", BLAU, d=0.2),
    peep_voll("FR_ruhig", FRK, BODEN, FH, ("f2", -0.2), bis="f2"),
    *redet("FR_trotz", FRK, BODEN, FH, "f2", "best"),
    peep_voll("FR_trotz", FRK, BODEN, FH, "best", anim="cut"),
    namensschild("Beklagter Franke", FRK, BODEN, "f2", GRUEN, d=0.2),
    blase("sprech", 560, 170, "f2", 1330, 210, inhalt=["Von Juni war nie die Rede!"], textsize=36, figur=FRb, bis="best"),
    pl("Bestreiten", FRK, 320, "best", fill=WEISS, size=30, anker="m", bis="bew"),
    pl("Thema der Beklagtenstation", 960, 160, beim("best", "Beklagtenstation"), fill=WEISS, size=32, anker="m", bis="bew"),
    ficon("tabler", "scale", 1290, 520, 110, "bew", fuell=GELB),
    pl("Wahr? Das klärt die Beweisstation.", 960, 160, "bew", fill=GELB, size=32, anker="m", anim="cut"),
    pl("benannte Zeugen nach Einzelheiten befragen", 1450, 320, beim("bew", "benannte"), fill=WEISS, size=28, anker="m"),
])

# K Abgrenzung Zulässigkeit, § 253 II Nr. 2 ZPO ----------------------------------------------------------------------------
folie([("zul", "Abgrenzung › Zulässigkeit, § 253 Abs. 2 Nr. 2 ZPO"),
       ("ident", "Abgrenzung › Zulässigkeit: individualisierbar"),
       (beim("hier", "Es"), "Abgrenzung › zulässig, aber nicht schlüssig")], rechts_frei([
    *tafel("zul", "Abgrenzung: Zulässigkeit"),
    *wortlaut(110, 180, 1040, 160, "zul", [
        [("„Die Klageschrift muss enthalten: … 2. die ", 0), ("bestimmte Angabe", "a")],
        [("des Gegenstandes und des ", 0), ("Grundes", "b"), (" des erhobenen Anspruchs,", 0)],
        [("sowie einen ", 0), ("bestimmten Antrag", "c"), (".“", 0)],
    ], 30, {"a": beim("zul", "bestimmte"), "b": beim("zul", "Grundes"), "c": beim("zul", "bestimmt", 2)},
        "§ 253 Abs. 2 Nr. 2 ZPO"),
    z("Dafür genügt: Anspruch individualisierbar", 110, 420, "ident", "Bold", 36),
    z("schlüssig dargelegt muss er dafür nicht sein", 150, 470, beim("ident", "Schlüssig"), size=32, farbe=TEXT),
    z("BGH, Beschl. v. 4.7.2018 – VII ZR 21/16, Rn. 11", 150, 515, beim("ident", "Bundesgerichtshof"), size=28, farbe=TEXT),
    ok(135, 610, beim("hier", "bestimmten"), gr=22),
    z("Hier: 6.000 € aus einem bestimmten Darlehen", 175, 590, "hier", "Bold", 34),
    fl_block(110, 680, 500, 130, GRUEN, beim("hier", "Es"), [("Zulässigkeit:", "ExtraBold", 32, INK), ("gegeben", "Bold", 30, INK)]),
    fl_block(650, 680, 500, 130, ROTHELL, beim("hier", "Schlüssigkeit"), [("Schlüssigkeit:", "ExtraBold", 32, INK),
                                                                        ("fehlte", "Bold", 30, INK)]),
    peep_voll("SC_ruhig", X1, BR, FR, "zul", bis="hier"),
    peep_voll("SC_froh", X1, BR, FR, "hier", anim="cut"),
    peep_voll("RI_ruhig", X2, BR, FR, "zul", d=0.2, bis="ident"),
    peep_voll("RI_denkt", X2, BR, FR, "ident", anim="cut"),
    namensschild("Frau Schubert", X1, BR, "zul", BLAU, d=0.2),
    namensschild("Richterin", X2, BR, "zul", LILA, d=0.3),
    ficon("tabler", "file-text", MB, 380, 100, "zul", fuell=WEISS),
    pl("Klageschrift", MB, 160, "zul", fill=WEISS, size=28, anker="m", bis="ident"),
    pl("individualisierbar", MB, 160, "ident", fill=GRUEN, size=28, anker="m", anim="cut"),
]))

# L Folge der Unschlüssigkeit, Versäumnisurteil § 331 ZPO --------------------------------------------------------------------
folie([("folge", "IV. Ergebnis › unschlüssig: Abweisung als unbegründet"), ("vu", "Versäumnisurteil, § 331 Abs. 1 ZPO"),
       ("tatz", "Versäumnisurteil › nur Tatsachen gelten als zugestanden"), ("vu2", "Versäumnisurteil, § 331 Abs. 2 ZPO"),
       ("vu3", "Versäumnisurteil › ohne Ergänzung: verloren")], rechts_frei([
    *tafel("folge", "Folge der Unschlüssigkeit"),
    z("Ohne Ergänzung: Abweisung als unbegründet,", 110, 175, beim("folge", "abgewiesen"), "Bold", 34),
    z("nicht als unzulässig", 150, 222, beim("folge", "unzulässig"), size=32, farbe=TEXT),
    *wortlaut(110, 290, 1040, 200, "vu", [
        [("„Beantragt der Kläger gegen den im Termin zur mündlichen", 0)],
        [("Verhandlung ", 0), ("nicht erschienenen", "a"), (" Beklagten das Versäumnisurteil,", 0)],
        [("so ist das ", 0), ("tatsächliche", "b"), (" mündliche Vorbringen des Klägers", 0)],
        [("als zugestanden", "c"), (" anzunehmen.“", 0)],
    ], 29, {"a": beim("vu", "nicht"), "b": beim("vu", "tatsächliches"), "c": beim("vu", "zugestanden")},
        "§ 331 Abs. 1 S. 1 ZPO"),
    z("nur Tatsächliches, nicht das Wort „fällig“", 110, 540, "tatz", "Bold", 32),
    *wortlaut(110, 600, 1040, 120, "vu2", [
        [("„Soweit es den Klageantrag ", 0), ("rechtfertigt", "a"), (", ist nach dem Antrag zu", 0)],
        [("erkennen; soweit dies nicht der Fall, ", 0), ("ist die Klage abzuweisen", "b"), (".“", 0)],
    ], 29, {"a": beim("vu2", "rechtfertigt"), "b": beim("vu2", "abzuweisen")}, "§ 331 Abs. 2 ZPO"),
    z("erste Klageschrift: verloren, trotz Säumnis", 110, 785, "vu3", "Bold", 32),
    peep_voll("SC_sorge", X1, BR, FR, "folge", bis="vu"),
    peep_voll("SC_ruhig", X1, BR, FR, "vu", anim="cut", bis="vu3"),
    peep_voll("SC_schreck", X1, BR, FR, "vu3", anim="cut"),
    namensschild("Frau Schubert", X1, BR, "folge", BLAU, d=0.2),
    ficon("tabler", "file-x", MB, 380, 100, "folge", fuell=ROT, bis="vu"),
    pl("abgewiesen", MB, 160, beim("folge", "abgewiesen"), fill=ROT, size=28, anker="m", bis="vu"),
    ficon("tabler", "user-off", X2, 700, 150, beim("vu", "nicht"), fuell=WEISS),
    pl("Beklagter nicht erschienen", MB, 160, beim("vu", "nicht"), fill=WEISS, size=26, anker="m"),
    pl("trotz Säumnis", X2, 780, beim("vu2", "Säumnis"), fill=GELB, size=28, anker="m"),
]))

# M Klausurtipp (Lexi) -------------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · Merkmal für Merkmal"), ("tipp2", "Klausurtipp · Stationen trennen")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Merkmal für Merkmal prüfen:", 200, 200, beim("tipp", "Prüfe"), "Bold", 38),
    z("zu jedem die vorgetragene Tatsache", 240, 255, beim("tipp", "nenne"), size=34, farbe=TEXT),
    z("„fällig“, „grob pflichtwidrig“:", 200, 350, beim("tipp", "Wörter"), "Bold", 36),
    z("ersetzen keine Tatsachen", 240, 405, beim("tipp", "ersetzen"), size=34, farbe=TEXT),
    z("Stationen trennen:", 200, 510, "tipp2", "Bold", 38),
    z("Ob der Vortrag stimmt, gehört erst", 240, 565, beim("tipp2", "Ob"), size=34, farbe=TEXT),
    z("in die Beweisstation.", 240, 615, beim("tipp2", "Beweisstation"), size=34, farbe=TEXT),
    *redet("LX_warnt", LXX, BR, FR + 60, "tipp", "sch"),
    pille("Lexi", LXX, BR + 22, "tipp", fill=GELB, size=30, anker="m", d=0.2),
])

# N Klausurschema ------------------------------------------------------------------------------------------------------------
K1, K2 = 150, 210
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel("Klausurschema: Schlüssigkeit (Klägerstation)", 110, 90, "sch", 54),
    z("I. Anspruchsgrundlage und ihre Merkmale (z. B. § 488 Abs. 1 S. 2 BGB)", K1, 200, "sI", "Bold", 36, rechts=1820),
    z("II. Tatsachenvortrag zu jedem Merkmal, als wahr unterstellt", K1, 300, "sII", "Bold", 36, rechts=1820),
    z("III. Fehlt etwas: Hinweis nach § 139 ZPO", K1, 400, "sIII", "Bold", 36, rechts=1820),
    z("IV. Ergebnis", K1, 500, "sIV", "Bold", 36, rechts=1820),
    z("schlüssig: weiter zur Beklagtenstation", K2, 560, "sIVa", size=34, farbe=TEXT, rechts=1820),
    z("unschlüssig: Abweisung als unbegründet", K2, 615, "sIVb", size=34, farbe=TEXT, rechts=1820),
])

# O Merksatz (Lexi) ----------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Schlüssig ist die Klage, wenn ihre", 0)], [("Tatsachen, als wahr unterstellt,", "a")],
                 [("den Antrag tragen.", 0)]], 750, 300, 50, "merke", {"a": beim("merke", "Tatsachen")}),
    *markertext([[("Einzelheiten braucht es nur, soweit", 0)], [("sie für die Rechtsfolge zählen.", "b")]], 750, 610, 50,
                "mz", {"b": beim("mz", "Rechtsfolge")}),
    *redet("LX_erklaert", 1680, 1000, 720, "merke", lexi_bis_ende("merke")),
])
