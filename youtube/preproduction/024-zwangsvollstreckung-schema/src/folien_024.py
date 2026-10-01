"""Folge 024 · Zwangsvollstreckung Schema: Titel, Klausel, Zustellung – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A Die Wohnung (Fall), B Beim Gerichtsvollzieher (Fall, Frage), C Sachverhalt, D Überblick,
E I. Antrag (§§ 753, 754a ZPO), F II. Vollstreckungsorgan, G III. 1. Titel (Wortlautkarte § 704), H III. 2. Klausel
(Wortlautkarte § 724 I, Urkundsbeamtin, Stempel), I Gegenfall Vollstreckungsbescheid (§ 796 I), J III. 3. Zustellung
(Wortlautkarte § 750 I n. F.), K IV. besondere Voraussetzungen, L V. Vollstreckungshindernisse, M Pfändung bei Herrn Vogel
(Fall), N Ausblick Rechtsbehelfe, O Klausurtipp (Lexi), P Klausurschema, Q Merksatz (Lexi).
Geräusche nur bei sichtbarer Handlung: Farbroller an der Wand (Szene A), Stempel der Urkundsbeamtin (Szene H)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont

bausteine.FIGORDNER = "op_024/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
ABZWEIG = (241, 236, 255, 255)          # hell-lila getönte Tafel für den Gegenfall
GRAU = (205, 205, 210, 255)
WAND = (232, 238, 250, 255)
HOLZ = (214, 160, 110, 255)
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


def block(x, y, w, h, fill, cue, text, size=38, **k):
    return fl_block(x, y, w, h, fill, cue, [(glyphen(text), "ExtraBold", size, INK)], **k)


def wortlaut(x, y, w, h, cue, zeilen, size, hl, quelle, quelle_cue=None):
    """Wortlautkarte: wörtliches Zitat (gesetze-im-internet.de) in einer hellen Karte, Fundstelle darunter rechts.
    zeilen = Liste von Token-Listen [(text, Schlüssel|0)], hl = {Schlüssel: Cue} (Hervorhebung synchron zum Wort)."""
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


# --- Eigene Hilfsfunktion (wie Folge 012): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ---------------
# ElevenLabs legt das Ende eines Wortes vor Satzzeichen oft in die folgende Pause; redet_024() kürzt jedes Wortende auf
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

# A Fall: die Wohnung von Herrn Vogel ---------------------------------------------------------------------------------
KX, VX = 380, 1540
folie([(NULL, "Fall · Die Wohnung von Herrn Vogel"), ("urteil", "Fall · Das Urteil")], [
    linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK),
    pl("Wohnung von Herrn Vogel", 70, 40, NULL, fill=GELB, size=40),
    karte(90, 200, 760, BODEN - 200, NULL, fill=WAND, rund=10, schatten=0, rand=4),
    ficon("tabler", "bucket", 690, BODEN - 4, 100, NULL, fuell=BLAU),
    peep_voll("KO_ruhig_r", KX, BODEN, FH, NULL, bis="zahlt"),
    namensschild("Frau Köhler", KX, BODEN, NULL, GRUEN),
    pl("Malermeisterin", KX, 330, beim("fall", "Malermeisterin"), fill=WEISS, size=30, anker="m", bis="wohnung"),
    # der Farbroller streicht die Wand (Handlungsgeräusch)
    szene(bewegt(ficon("tabler", "paint", 640, 560, 120, "wohnung", fuell=WEISS, bis="zahlt"),
                 beim("wohnung", "streicht"), beim("wohnung", "Wohnung", ende=True), 0, -170), "024rolle*", 0.9,
          round(bausteine._t(beim("wohnung", "streicht")) - bausteine._t("wohnung"), 3)),
    peep_voll("VO_ruhig", VX, BODEN, FH, beim("wohnung", "Herrn"), anim="fade", bis="zahlt"),
    namensschild("Herr Vogel", VX, BODEN, beim("wohnung", "Herrn"), BLAU),
    pl("4.800 €", 1180, 260, beim("wohnung", "viertausendachthundert"), fill=GELB, size=44, anker="m", bis="urteil"),
    # er zahlt nicht
    peep_voll("VO_trotz", VX, BODEN, FH, "zahlt", anim="cut", bis=beim("urteil", "verurteilt")),
    peep_voll("KO_aerger_r", KX, BODEN, FH, "zahlt", anim="cut", bis=beim("urteil", "gewinnt")),
    ficon("tabler", "currency-euro-off", 1180, 470, 110, beim("zahlt", "zahlt"), fuell=ROT, bis="urteil"),
    pl("keine Zahlung", 1180, 490, beim("zahlt", "zahlt"), fill=ROT, size=32, anker="m", bis="urteil"),
    # Klage und Urteil
    pl("Klage", 1180, 260, beim("urteil", "klagt"), fill=WEISS, size=34, anker="m", bis=beim("urteil", "Amtsgericht")),
    peep_voll("KO_froh_r", KX, BODEN, FH, beim("urteil", "gewinnt"), anim="cut"),
    ficon("tabler", "building-bank", 1180, 420, 150, beim("urteil", "Amtsgericht"), fuell=BLAU),
    pl("Amtsgericht", 1180, 200, beim("urteil", "Amtsgericht"), fill=BLAU, size=34, anker="m"),
    peep_voll("VO_muede", VX, BODEN, FH, beim("urteil", "verurteilt"), anim="cut"),
    ficon("tabler", "file-text", 1180, 640, 90, beim("urteil", "verurteilt"), fuell=WEISS),
    pl("Urteil: Vogel zahlt 4.800 €", 1180, 660, beim("urteil", "verurteilt"), fill=WEISS, size=30, anker="m"),
    pl("rechtskräftig", 1180, 450, beim("urteil", "rechtskräftig"), fill=GRUEN, size=32, anker="m"),
])

# B Fall: beim Gerichtsvollzieher ---------------------------------------------------------------------------------------
KX, GX = 460, 1500
KOb = ("KO_redet_r", KX, BODEN, FH)
GVb = ("GV_redet", GX, BODEN, FH)
folie([("buero", "Fall · Beim Gerichtsvollzieher"), ("frage", "Fall · Die Frage")], [
    linienzug([(60, BODEN), (1860, BODEN)], "buero", breite=7, farbe=INK),
    pl("Büro des Gerichtsvollziehers", 70, 40, "buero", fill=TUERKIS, size=40),
    peep_voll("KO_ruhig_r", KX, BODEN, FH, "buero", bis="k1"),
    namensschild("Frau Köhler", KX, BODEN, "buero", GRUEN),
    *redet("KO_redet_r", KX, BODEN, FH, "k1", "g1"),
    peep_voll("KO_ruhig_r", KX, BODEN, FH, "g1", anim="cut", bis="k2"),
    *redet("KO_redet_r", KX, BODEN, FH, "k2", "frage"),
    peep_voll("KO_sorge_r", KX, BODEN, FH, "frage", anim="cut"),
    peep_voll("GV_ruhig", GX, BODEN, FH, beim("buero", "Gerichtsvollzieher"), anim="fade", bis="g1"),
    *redet("GV_redet", GX, BODEN, FH, "g1", "k2"),
    peep_voll("GV_ruhig", GX, BODEN, FH, "k2", anim="cut", bis="frage"),
    peep_voll("GV_denkt", GX, BODEN, FH, "frage", anim="cut"),
    karte(1150, 690, 640, BODEN - 690, "buero", fill=HOLZ, rund=12, schatten=6),          # Schreibtisch vor dem GV
    namensschild("Gerichtsvollzieher", GX, BODEN, beim("buero", "Gerichtsvollzieher"), TUERKIS),
    # das Urteil wandert auf den Schreibtisch
    bewegt(ficon("tabler", "file-text", 1250, 680, 90, "k1", fuell=WEISS),
           beim("k1", "Hier"), beim("k1", "Urteil", ende=True), KX + 160 - 1250, -40),
    blase("sprech", 620, 210, "k1", 700, 240, inhalt=["Hier ist mein Urteil.", "Bitte holen Sie mein Geld!"], textsize=34,
          figur=KOb, bis="g1"),
    blase("sprech", 760, 260, "g1", 1260, 200, inhalt=["Auf Ihrem Urteil fehlt die", "Vollstreckungsklausel.",
                                                      "So darf ich nicht anfangen."], textsize=34, figur=GVb, bis="k2"),
    nein(1330, 610, beim("g1", "fehlt"), gr=26),
    pl("ohne Vollstreckungsklausel", 1150, 510, beim("g1", "Vollstreckungsklausel"), fill=ROT, size=28, anker="m"),
    blase("sprech", 620, 210, "k2", 700, 240, inhalt=["Aber das Urteil ist", "doch rechtskräftig!"], textsize=36,
          figur=KOb, bis="frage"),
    pl("Warum legt der Gerichtsvollzieher nicht los?", 960, 140, "frage", fill=PINK, size=38, anker="m"),
    pl("Was prüft er, bevor er vollstreckt?", 960, 230, beim("frage", "Und"), fill=PINK, size=38, anker="m"),
])

# C Sachverhalt -------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Malermeisterin Köhler streicht die Wohnung von Herrn Vogel für 4.800 Euro. Vogel zahlt nicht. Auf ihre Klage "
    "verurteilt ihn das Amtsgericht zur Zahlung von 4.800 Euro. Das Urteil wird beiden Parteien von Amts wegen "
    "zugestellt und ist inzwischen rechtskräftig.",
    "Frau Köhler legt dem Gerichtsvollzieher ihre Ausfertigung des Urteils vor, auf der keine Vollstreckungsklausel "
    "steht, und bittet ihn, bei Vogel zu pfänden. Der Gerichtsvollzieher lehnt ab.",
    "(Frei erfundener Übungsfall.)",
], "Was muss vorliegen, damit der Gerichtsvollzieher vollstreckt?")

# D Überblick: das Prüfungsschema ---------------------------------------------------------------------------------------
folie([("ueber", "Überblick · Prüfungsschema der Zwangsvollstreckung")], rechts_frei([
    *tafel("ueber", "Das Prüfungsschema"),
    z("I. Antrag", 110, 210, "ue1", "Bold", 40),
    z("II. Zuständiges Vollstreckungsorgan", 110, 290, "ue2", "Bold", 40),
    z("III. Allgemeine Voraussetzungen:", 110, 370, "ue3", "Bold", 40),
    z("Titel, Klausel, Zustellung", 170, 430, beim("ue3", "Titel"), size=38),
    z("IV. Besondere Voraussetzungen", 110, 520, "ue4", "Bold", 40),
    z("V. Keine Vollstreckungshindernisse", 110, 600, "ue5", "Bold", 40),
    ficon("tabler", "list-numbers", MB, 380, 130, "ueber", fuell=WEISS),
    peep_voll("KO_denkt", X1, BR, FR, "ueber"),
    peep_voll("GV_ruhig", X2, BR, FR, "ueber", d=0.2),
    namensschild("Frau Köhler", X1, BR, "ueber", GRUEN, d=0.2),
    namensschild("Gerichtsvollzieher", X2, BR, "ueber", TUERKIS, d=0.3),
]))

# E I. Antrag -----------------------------------------------------------------------------------------------------------
folie([("antrag", "I. Antrag · Vollstreckungsauftrag, § 753 Abs. 1 ZPO"),
       ("elektr", "I. Antrag › elektronischer Auftrag, § 754a ZPO (seit 1.10.2026)")], rechts_frei([
    *tafel("antrag", "I. Antrag"),
    z("Gerichtsvollzieher vollstreckt im Auftrag", 110, 200, beim("antrag", "Gerichtsvollzieher"), "Bold", 36),
    z("der Gläubigerin, § 753 Abs. 1 ZPO", 110, 250, beim("antrag", "Gläubigerin"), "Bold", 36),
    block(110, 340, 1040, 90, GELB, "elektr", "Seit 1.10.2026: § 754a ZPO", size=38),
    z("elektronischer Auftrag wegen einer Geldforderung:", 110, 460, beim("elektr", "elektronischen"), size=34),
    z("Titel und Klausel als elektronische Dokumente", 150, 515, beim("elektr", "Titel"), size=34),
    z("Versicherung der Gläubigerin:", 110, 610, "versich", "Bold", 34),
    z("Forderung besteht noch", 150, 665, beim("versich", "Forderung"), size=34),
    ficon("tabler", "file-text", MB, 380, 110, "antrag", fuell=WEISS, bis="elektr"),
    pl("Auftrag", MB, 160, beim("antrag", "Auftrag"), fill=WEISS, size=30, anker="m", bis="elektr"),
    ficon("tabler", "device-laptop", MB, 380, 150, "elektr", fuell=BLAU, anim="cut", bis="versich"),
    ficon("tabler", "file-check", MB, 380, 110, "versich", fuell=WEISS, anim="cut"),
    peep_voll("KO_ruhig", X1, BR, FR, "antrag", bis="versich"),
    peep_voll("KO_froh", X1, BR, FR, "versich", anim="cut"),
    peep_voll("GV_ruhig", X2, BR, FR, "antrag", d=0.2),
    namensschild("Frau Köhler", X1, BR, "antrag", GRUEN, d=0.2),
    namensschild("Gerichtsvollzieher", X2, BR, "antrag", TUERKIS, d=0.3),
]))

# F II. Vollstreckungsorgan -----------------------------------------------------------------------------------------------
folie([("organ", "II. Zuständiges Vollstreckungsorgan"),
       ("hier", "II. Vollstreckungsorgan › hier: Gerichtsvollzieher, § 808 ZPO")], rechts_frei([
    *tafel("organ", "II. Vollstreckungsorgan"),
    z("Es hängt davon ab, worin vollstreckt wird.", 110, 190, beim("organ", "Es"), size=34, farbe=TEXT),
    z("Bewegliche Sachen: Gerichtsvollzieher, § 808 ZPO", 110, 270, "sachen", "Bold", 34),
    z("Forderungen wie Lohn oder Kontoguthaben:", 110, 350, "ford", "Bold", 34),
    z("Vollstreckungsgericht, § 828 ZPO", 150, 400, beim("ford", "Vollstreckungsgericht"), "Bold", 34),
    z("Zwangshypothek: Grundbuchamt, § 867 ZPO", 110, 480, "grund", "Bold", 34),
    z("Handlungen: Prozessgericht, §§ 887 ff. ZPO", 110, 560, "handl", "Bold", 34),
    z("Frau Köhler will Sachen pfänden lassen:", 110, 640, "hier", size=34),
    ok(135, 740, beim("hier", "Zuständig"), gr=22),
    block(175, 700, 975, 90, GRUEN, beim("hier", "Zuständig"), "Zuständig: Gerichtsvollzieher", size=38),
    ficon("tabler", "sofa", MB, 380, 170, "sachen", fuell=LILA, bis="ford"),
    ficon("tabler", "wallet", MB, 380, 130, "ford", fuell=GELB, anim="cut", bis="grund"),
    ficon("tabler", "home", MB, 380, 140, "grund", fuell=ROT, anim="cut", bis="handl"),
    ficon("tabler", "tools", MB, 380, 130, "handl", fuell=WEISS, anim="cut", bis="hier"),
    ficon("tabler", "sofa", MB, 380, 170, "hier", fuell=LILA, anim="cut"),
    peep_voll("KO_ruhig", X1, BR, FR, "organ", bis="hier"),
    peep_voll("KO_froh", X1, BR, FR, "hier", anim="cut"),
    peep_voll("GV_ruhig", X2, BR, FR, "organ", d=0.2),
    namensschild("Frau Köhler", X1, BR, "organ", GRUEN, d=0.2),
    namensschild("Gerichtsvollzieher", X2, BR, "organ", TUERKIS, d=0.3),
]))

# G III. 1. Titel ---------------------------------------------------------------------------------------------------------
folie([("titel", "III. Allgemeine Voraussetzungen › 1. Titel, § 704 ZPO"),
       ("p794", "III. Allgemeine Voraussetzungen › 1. Titel › weitere Titel, § 794 ZPO")], rechts_frei([
    *tafel("titel", "III. 1. Titel"),
    *wortlaut(110, 180, 1040, 150, "p704", [
        [("„Die Zwangsvollstreckung findet statt aus ", 0), ("Endurteilen,", "a")],
        [("die ", 0), ("rechtskräftig", "b"), (" oder für ", 0), ("vorläufig vollstreckbar", "c"), (" erklärt sind.“", 0)],
    ], 32, {"a": beim("p704", "Endurteilen"), "b": beim("p704", "rechtskräftig"), "c": beim("p704", "vorläufig")}, "§ 704 ZPO"),
    z("vorläufig vollstreckbar: bis 1.250 € ohne Sicherheit,", 110, 400, "vorl", "Bold", 34),
    z("§ 708 Nr. 11 ZPO", 150, 450, beim("vorl", "Paragrafen"), size=32),
    z("sonst grundsätzlich gegen Sicherheit, § 709 ZPO", 110, 500, beim("vorl", "sonst"), "Bold", 34),
    z("Weitere Titel, § 794 Abs. 1 ZPO:", 110, 580, "p794", "Bold", 34),
    z("Prozessvergleich (Nr. 1)", 150, 630, beim("p794", "Prozessvergleich"), size=32),
    z("vollstreckbare notarielle Urkunde (Nr. 5)", 150, 675, beim("p794", "vollstreckbare"), size=32),
    z("Vollstreckungsbescheid (Nr. 4)", 150, 720, beim("p794", "Vollstreckungsbescheid"), size=32),
    ok(135, 810, beim("titel_ok", "Der"), gr=22),
    z("Rechtskräftiges Endurteil: Der Titel liegt vor.", 175, 790, "titel_ok", "Bold", 34),
    ficon("tabler", "file-text", MB, 380, 110, "titel", fuell=WEISS),
    pl("Urteil", MB, 160, "titel", fill=WEISS, size=30, anker="m", bis="titel_ok"),
    pl("rechtskräftig", MB, 160, "titel_ok", fill=GRUEN, size=30, anker="m", anim="cut"),
    peep_voll("KO_ruhig", X1, BR, FR, "titel", bis="titel_ok"),
    peep_voll("KO_froh", X1, BR, FR, "titel_ok", anim="cut"),
    peep_voll("VO_ruhig", X2, BR, FR, "titel", d=0.2, bis="titel_ok"),
    peep_voll("VO_muede", X2, BR, FR, "titel_ok", anim="cut"),
    namensschild("Frau Köhler", X1, BR, "titel", GRUEN, d=0.2),
    namensschild("Herr Vogel", X2, BR, "titel", BLAU, d=0.3),
]))

# H III. 2. Klausel ---------------------------------------------------------------------------------------------------------
UX, KX = 1720, 1420
UBb = ("UB_redet", UX, BR, FR)
DX, DY = 1570, 640                      # das Urteil auf dem Tisch der Geschäftsstelle (Stempel landet darauf)
folie([("klausel", "III. Allgemeine Voraussetzungen › 2. Klausel, § 724 ZPO"),
       ("p725", "III. Allgemeine Voraussetzungen › 2. Klausel › Wortlaut, § 725 ZPO")], rechts_frei([
    *tafel("klausel", "III. 2. Klausel"),
    z("Daran ist Frau Köhler gescheitert.", 110, 180, beim("klausel", "Daran"), size=32, farbe=TEXT),
    *wortlaut(110, 240, 1040, 200, "p724", [
        [("„Die Zwangsvollstreckung wird auf Grund einer mit der", 0)],
        [("Vollstreckungsklausel", "a"), (" versehenen Ausfertigung des Urteils", 0)],
        [("(", 0), ("vollstreckbare Ausfertigung", "b"), (") durchgeführt.“", 0)],
    ], 34, {"a": beim("p724", "Vollstreckungsklausel"), "b": beim("p724", "vollstreckbaren")}, "§ 724 Abs. 1 ZPO"),
    z("Erteilung: Urkundsbeamter der Geschäftsstelle", 110, 510, "ub", "Bold", 34),
    z("des Gerichts erster Instanz, hier des Amtsgerichts", 150, 560, beim("ub", "Gerichts"), size=32),
    z("Wortlaut der Klausel: § 725 ZPO", 110, 690, "p725", "Bold", 34),
    peep_voll("KO_ruhig", KX, BR, FR, "klausel", bis="p725"),
    peep_voll("KO_froh", KX, BR, FR, "p725", anim="cut"),
    namensschild("Frau Köhler", KX, BR, "klausel", GRUEN, d=0.2),
    peep_voll("UB_ruhig", UX, BR, FR, beim("ub", "Urkundsbeamte"), anim="fade", bis="u1"),
    *redet("UB_redet", UX, BR, FR, "u1", "p725"),
    peep_voll("UB_ruhig", UX, BR, FR, "p725", anim="cut"),
    namensschild("Urkundsbeamtin", UX, BR, beim("ub", "Urkundsbeamte"), PINK),
    ficon("tabler", "file-text", KX, 380, 100, "klausel", fuell=WEISS, bis="u1"),
    pl("ohne Klausel", KX, 170, beim("klausel", "gescheitert"), fill=ROT, size=28, anker="m", bis="u1"),
    blase("sprech", 660, 300, "u1", 1530, 190, inhalt=["Vorstehende Ausfertigung", "wird der Klägerin zum Zwecke",
                                                       "der Zwangsvollstreckung erteilt."], textsize=30, figur=UBb, bis="p725"),
    ficon("tabler", "file-certificate", KX, 400, 110, "p725", fuell=GELB),
    szene(bewegt(ficon("tabler", "rubber-stamp", KX + 80, 360, 90, "p725", fuell=ROT),
                 "p725", ("p725", 0.35), 0, -90), "024stempel*", 0.9, 0.33),
    pl("vollstreckbare Ausfertigung", MB, 170, "p725", fill=GELB, size=28, anker="m"),
]))

# I Gegenfall: Vollstreckungsbescheid --------------------------------------------------------------------------------------
folie([("vb", "Gegenfall · Vollstreckungsbescheid, § 794 Abs. 1 Nr. 4 ZPO"),
       ("p796", "Gegenfall · Vollstreckungsbescheid › Klausel? § 796 Abs. 1 ZPO")], rechts_frei([
    *tafel("vb", "Gegenfall: Vollstreckungsbescheid", fill=ABZWEIG, size=46),
    z("aus dem Mahnverfahren", 110, 190, beim("vb", "Mahnverfahren"), "Bold", 36),
    z("Titel nach § 794 Abs. 1 Nr. 4 ZPO", 110, 250, beim("vb", "Titel"), size=34),
    z("§ 796 Abs. 1 ZPO: Klausel nur, wenn für oder gegen", 110, 350, "p796", "Bold", 34),
    z("andere Personen vollstreckt wird", 150, 400, beim("p796", "andere"), size=34),
    z("als die im Bescheid genannten", 150, 445, beim("p796", "Bescheid"), size=34),
    ficon("tabler", "file-certificate", MB, 380, 120, "vb", fuell=LILA),
    pl("Vollstreckungsbescheid", MB, 160, "vb", fill=LILA, size=28, anker="m"),
    peep_voll("KO_denkt", X1, BR, FR, "vb", bis=beim("p796", "Paragraf")),
    peep_voll("KO_froh", X1, BR, FR, beim("p796", "Paragraf"), anim="cut"),
    peep_voll("GV_ruhig", X2, BR, FR, "vb", d=0.2),
    namensschild("Frau Köhler", X1, BR, "vb", GRUEN, d=0.2),
    namensschild("Gerichtsvollzieher", X2, BR, "vb", TUERKIS, d=0.3),
]))

# J III. 3. Zustellung, § 750 I n. F. -------------------------------------------------------------------------------------
folie([("zust", "III. Allgemeine Voraussetzungen › 3. Zustellung, § 750 Abs. 1 ZPO")], rechts_frei([
    *tafel("zust", "III. 3. Zustellung"),
    pl("§ 750 ZPO neu gefasst seit 1.10.2026", 110, 175, beim("zust", "neu"), fill=GELB, size=30),
    *wortlaut(110, 260, 1040, 300, "p750", [
        [("„(1) Die Zwangsvollstreckung darf nur beginnen, wenn", 0)],
        [("1. die Personen, für und gegen die die Zwangsvollstreckung", 0)],
        [("stattfinden soll, in dem Urteil oder in der ihm beigefügten", 0)],
        [("Vollstreckungsklausel ", 0), ("namentlich bezeichnet", "a"), (" sind, und", 0)],
        [("2. den Personen, gegen die … ", 0), ("zugestellt ist oder gleichzeitig", "b")],
        [("zugestellt wird:", "b"), (" a) ", 0), ("das Urteil,", "c"), (" …“", 0)],
    ], 29, {"a": beim("p750", "namentlich"), "b": beim("p750b", "zugestellt"), "c": beim("p750b", "Urteil")},
        "§ 750 Abs. 1 ZPO (BGBl. 2026 I Nr. 152)"),
    ok(135, 680, beim("zust_ok", "zugestellt"), gr=22),
    z("Urteil von Amts wegen zugestellt, § 317 Abs. 1 ZPO", 175, 660, "zust_ok", "Bold", 34),
    z("Auch das liegt vor.", 175, 715, beim("zust_ok", "Auch"), size=34),
    ficon("tabler", "building-bank", X1 - 30, 360, 110, "zust", fuell=BLAU),
    bewegt(ficon("tabler", "mail", X2, 430, 80, beim("zust_ok", "Amts"), fuell=WEISS),
           beim("zust_ok", "Amts"), beim("zust_ok", "zugestellt", ende=True), X1 - 30 - X2, -70),
    peep_voll("KO_ruhig", X1, BR, FR, "zust", bis="zust_ok"),
    peep_voll("KO_froh", X1, BR, FR, beim("zust_ok", "Auch"), anim="cut"),
    peep_voll("KO_denkt", X1, BR, FR, "zust_ok", anim="cut", bis=beim("zust_ok", "Auch")),
    peep_voll("VO_ruhig", X2, BR, FR, "zust", d=0.2, bis="zust_ok"),
    peep_voll("VO_muede", X2, BR, FR, "zust_ok", anim="cut"),
    namensschild("Frau Köhler", X1, BR, "zust", GRUEN, d=0.2),
    namensschild("Herr Vogel", X2, BR, "zust", BLAU, d=0.3),
]))

# K IV. besondere Voraussetzungen ---------------------------------------------------------------------------------------
folie([("bes", "IV. Besondere Vollstreckungsvoraussetzungen, §§ 751, 756 ZPO")], rechts_frei([
    *tafel("bes", "IV. Besondere Voraussetzungen"),
    z("Kalendertag abgelaufen, § 751 Abs. 1 ZPO", 110, 200, "p751", "Bold", 34),
    z("Sicherheitsleistung durch Urkunde nachgewiesen,", 110, 290, "sicher", "Bold", 34),
    z("§ 751 Abs. 2 ZPO", 150, 340, beim("sicher", "Paragraf"), size=32),
    z("Zug um Zug: Gegenleistung grundsätzlich zuerst", 110, 430, "p756", "Bold", 34),
    z("anbieten, § 756 ZPO", 150, 480, beim("p756", "zuerst"), size=32),
    block(110, 590, 1040, 100, GRUEN, "bes_ok", "Bei Frau Köhler greift nichts davon.", size=38),
    z("Urteil rechtskräftig und unbedingt", 150, 720, beim("bes_ok", "Ihr"), size=34),
    ficon("tabler", "calendar-event", MB, 380, 120, "p751", fuell=WEISS, bis="sicher"),
    ficon("tabler", "coins", MB, 380, 130, "sicher", fuell=GELB, anim="cut", bis="p756"),
    ficon("tabler", "arrows-exchange", MB, 380, 130, "p756", fuell=WEISS, anim="cut", bis="bes_ok"),
    ficon("tabler", "file-check", MB, 380, 110, "bes_ok", fuell=GRUEN, anim="cut"),
    peep_voll("KO_denkt", X1, BR, FR, "bes", bis="bes_ok"),
    peep_voll("KO_froh", X1, BR, FR, "bes_ok", anim="cut"),
    peep_voll("GV_ruhig", X2, BR, FR, "bes", d=0.2),
    namensschild("Frau Köhler", X1, BR, "bes", GRUEN, d=0.2),
    namensschild("Gerichtsvollzieher", X2, BR, "bes", TUERKIS, d=0.3),
]))

# L V. keine Vollstreckungshindernisse ------------------------------------------------------------------------------------
folie([("hind", "V. Keine Vollstreckungshindernisse, § 775 ZPO")], rechts_frei([
    *tafel("hind", "V. Vollstreckungshindernisse?"),
    z("§ 775 ZPO: Die Vollstreckung wird etwa eingestellt,", 110, 200, "p775", "Bold", 34),
    z("Nr. 1: Entscheidung, die das Urteil aufhebt", 150, 270, beim("p775", "Entscheidung"), size=34),
    z("Nr. 4: Quittung der Gläubigerin, dass sie nach", 150, 340, "quitt", size=34),
    z("dem Urteil befriedigt ist", 190, 390, beim("quitt", "befriedigt"), size=34),
    ok(135, 500, "hind_ok", gr=22),
    z("Herr Vogel kann nichts davon vorlegen.", 175, 480, "hind_ok", "Bold", 36),
    ficon("tabler", "hand-stop", MB, 380, 110, "p775", fuell=ROT, bis="quitt"),
    ficon("tabler", "receipt", MB, 380, 110, "quitt", fuell=WEISS, anim="cut", bis="hind_ok"),
    ficon("tabler", "receipt-off", MB, 380, 110, "hind_ok", fuell=WEISS, anim="cut"),
    peep_voll("VO_ruhig", X1, BR, FR, "hind", bis="hind_ok"),
    peep_voll("VO_muede", X1, BR, FR, "hind_ok", anim="cut"),
    peep_voll("GV_ruhig", X2, BR, FR, "hind", d=0.2),
    namensschild("Herr Vogel", X1, BR, "hind", BLAU, d=0.2),
    namensschild("Gerichtsvollzieher", X2, BR, "hind", TUERKIS, d=0.3),
]))

# M Fall: Pfändung bei Herrn Vogel ------------------------------------------------------------------------------------------
VX, GX = 420, 1500
VOb = ("VO_redet_r", VX, BODEN, FH)
GVb = ("GV_redet", GX, BODEN, FH)
BX, BY = 900, 520                       # Gemälde an der Wand
folie([("auftrag", "Fall · Der Auftrag"), ("pfand", "Fall · Pfändung bei Herrn Vogel, § 808 ZPO")], [
    linienzug([(60, BODEN), (1860, BODEN)], "auftrag", breite=7, farbe=INK),
    pl("Bei Herrn Vogel", 70, 40, "auftrag", fill=BLAU, size=40),
    ficon("tabler", "sofa", 820, BODEN - 4, 280, "auftrag", fuell=LILA),
    ficon("tabler", "photo", BX, BY, 170, "auftrag", fuell=GELB),
    peep_voll("VO_ruhig_r", VX, BODEN, FH, "auftrag", bis="g2"),
    peep_voll("VO_schreck_r", VX, BODEN, FH, "g2", anim="cut", bis="v1"),
    *redet("VO_redet_r", VX, BODEN, FH, "v1", "rb"),
    namensschild("Herr Vogel", VX, BODEN, "auftrag", BLAU),
    peep_voll("GV_ruhig", GX, BODEN, FH, "auftrag", bis="g2"),
    *redet("GV_redet", GX, BODEN, FH, "g2", "v1"),
    peep_voll("GV_ruhig", GX, BODEN, FH, "v1", anim="cut"),
    namensschild("Gerichtsvollzieher", GX, BODEN, "auftrag", TUERKIS),
    ficon("tabler", "file-certificate", GX + 170, 620, 80, "auftrag", fuell=GELB),
    pl("vollstreckbare Ausfertigung", GX - 40, 300, beim("auftrag", "vollstreckbaren"), fill=GELB, size=28, anker="m", bis="pfand"),
    pl("Auftrag von Frau Köhler", GX - 40, 370, beim("auftrag", "Auftrag"), fill=WEISS, size=28, anker="m", bis="pfand"),
    pl("Pfändung, § 808 ZPO", 1150, 330, beim("pfand", "pfändet"), fill=GELB, size=34, anker="m"),
    blase("sprech", 640, 210, "g2", 1350, 200, inhalt=["Dieses Gemälde ist gepfändet.", "Hier ist das Siegel."],
          textsize=34, figur=GVb, bis="v1"),
    ficon("tabler", "sticker", BX + 50, BY - 20, 60, beim("g2", "Siegel"), fuell=ROT),
    blase("sprech", 640, 200, "v1", 640, 200, inhalt=["Das Gemälde gehört", "doch meiner Schwester!"], textsize=34,
          figur=VOb, bis="rb"),
])

# N Ausblick: Rechtsbehelfe -----------------------------------------------------------------------------------------------
folie([("rb", "Ausblick · Rechtsbehelfe"), ("rb771", "Ausblick · Drittwiderspruchsklage, § 771 ZPO"),
       ("rb767", "Ausblick · Vollstreckungsabwehrklage, § 767 ZPO"), ("rb766", "Ausblick · Erinnerung, § 766 ZPO")], rechts_frei([
    *tafel("rb", "Ausblick: Rechtsbehelfe"),
    z("§ 771 ZPO: Drittwiderspruchsklage", 110, 200, "rb771", "Bold", 36),
    z("Dritter behauptet ein Recht, das die Veräußerung", 150, 255, "rb771", size=32),
    z("hindert", 150, 300, beim("rb771", "hindert"), size=32),
    z("§ 767 ZPO: Vollstreckungsabwehrklage", 110, 400, "rb767", "Bold", 36),
    z("Einwendungen gegen den Anspruch selbst,", 150, 455, "rb767", size=32),
    z("etwa eine spätere Zahlung", 150, 500, beim("rb767", "etwa"), size=32),
    z("§ 766 ZPO: Erinnerung", 110, 600, "rb766", "Bold", 36),
    z("Verfahrensfehler, etwa eine fehlende Klausel", 150, 655, "rb766", size=32),
    ficon("tabler", "photo", MB, 380, 120, "rb771", fuell=GELB, bis="rb767"),
    pl("Schwester", MB, 160, "rb771", fill=PINK, size=28, anker="m", bis="rb767"),
    ficon("tabler", "receipt", MB, 380, 110, "rb767", fuell=WEISS, anim="cut", bis="rb766"),
    ficon("tabler", "file-x", MB, 380, 110, "rb766", fuell=WEISS, anim="cut"),
    peep_voll("VO_ruhig", X1, BR, FR, "rb", bis="rb766"),
    peep_voll("VO_trotz", X1, BR, FR, "rb766", anim="cut"),
    peep_voll("GV_ruhig", X2, BR, FR, "rb", d=0.2),
    namensschild("Herr Vogel", X1, BR, "rb", BLAU, d=0.2),
    namensschild("Gerichtsvollzieher", X2, BR, "rb", TUERKIS, d=0.3),
]))

# O Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · Zustellung: Urteil, nicht die einfache Klausel")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Zustellung: genau den Wortlaut lesen", 200, 200, beim("tipp", "Lies"), "Bold", 38),
    ok(135, 330, beim("tipp", "Urteil"), gr=22),
    z("Zugestellt sein muss das Urteil.", 175, 310, beim("tipp", "Zugestellt"), size=36),
    nein(135, 470, beim("tipp2", "nicht"), gr=22),
    z("Die einfache Klausel nicht zustellen.", 175, 450, "tipp2", size=36),
    z("Nur in Sonderfällen, etwa bei Rechtsnachfolge:", 110, 570, "tipp3", "Bold", 34),
    z("§ 750 Abs. 1 S. 1 Nr. 2 b ZPO", 150, 620, beim("tipp3", "Rechtsnachfolge"), size=32),
    *redet("LX_warnt", LXX, BR, 560, "tipp", "sch"),
    namensschild("Lexi", LXX, BR, "tipp", GELB, d=0.2),
])

# P Klausurschema -----------------------------------------------------------------------------------------------------
K1, K2 = 150, 210
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel("Klausurschema: Zwangsvollstreckung", 110, 90, "sch", 54),
    z("I. Antrag (Vollstreckungsauftrag, § 753 Abs. 1; elektronisch § 754a ZPO)", K1, 200, "s1", "Bold", 36, rechts=1820),
    z("II. Zuständiges Vollstreckungsorgan (§§ 753, 808, 828, 867, 887 ff. ZPO)", K1, 280, "s2", "Bold", 36, rechts=1820),
    z("III. Allgemeine Vollstreckungsvoraussetzungen", K1, 360, "s3", "Bold", 36, rechts=1820),
    z("1. Titel (§§ 704, 708 ff., 794 ZPO)", K2, 420, "s3a", size=34, rechts=1820),
    z("2. Klausel (§§ 724, 725 ZPO; Vollstreckungsbescheid: § 796 Abs. 1 ZPO)", K2, 475, "s3b", size=34, rechts=1820),
    z("3. Zustellung (§ 750 Abs. 1 ZPO)", K2, 530, "s3c", size=34, rechts=1820),
    z("IV. Besondere Vollstreckungsvoraussetzungen (§§ 751, 756 ZPO)", K1, 610, "s4", "Bold", 36, rechts=1820),
    z("V. Keine Vollstreckungshindernisse (§ 775 ZPO)", K1, 690, "s5", "Bold", 36, rechts=1820),
])

# Q Merksatz (Lexi) ---------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Ein Urteil allein reicht nicht.", 0)]], 750, 320, 46, "merke", {}),
    *markertext([[("Vollstreckt wird in der Regel erst mit", 0)],
                 [("Titel, Klausel und Zustellung,", "a")]], 750, 420, 46, beim("merke", "Vollstreckt"),
                {"a": beim("merke", "Titel")}),
    *markertext([[("und zwar durch das Organ, das für den", 0)],
                 [("Gegenstand ", 0), ("zuständig", "b"), (" ist.", 0)]], 750, 600, 42, "m2",
                {"b": beim("m2", "zuständig")}),
    *redet("LX_erklaert", 1680, 1000, 720, "merke", lexi_bis_ende("merke")),
])
