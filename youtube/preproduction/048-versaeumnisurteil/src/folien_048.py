"""Folge 048 · Versäumnisurteil Voraussetzungen: § 331 ZPO und unechtes VU – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A Auf der Wiese (mündlicher Kauf per Handschlag), B Im Sitzungssaal (Aufruf, leerer Stuhl,
Antrag auf VU, Frage), C Sachverhalt, D Wer ist säumig? (Wortlautkarte § 330 ZPO), E I. Antrag, II. Säumnis (Wortlautkarte
§ 335 I Nr. 2, 3 ZPO), F III. Zulässigkeit, G IV. Schlüssigkeit: Geständnisfiktion (Wortlautkarten § 331 I 1, II ZPO),
H IV. Schlüssigkeit: Form (Wortlautkarten § 311b I 1, § 125 S. 1 BGB; Hinweis der Richterin), I Das unechte VU,
J Gegenfall: echtes VU, Einspruch, § 342, § 345, K § 331 III ZPO, L Klausurtipp (Lexi), M Klausurschema, N Merksatz (Lexi).
Geräusche nur bei sichtbarer Handlung: Handschlag (Szene A), Akte auf dem Richtertisch (Szene B); Freesound CC0."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont

bausteine.FIGORDNER = "op_048/"
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




def hart(e):
    e.anim = "cut"
    return e


BODEN, FH = 880, 480
BR, FR = 930, 480                       # Figuren rechts neben der Tafel
X1, X2 = 1420, 1720                     # zwei Figuren neben der Tafel
MB = (X1 + X2) // 2

# A Fall: auf der Wiese am Dorfrand ----------------------------------------------------------------------------------------
SX, FX = 560, 1360
EHa = ("EH_redet", FX, BODEN, FH)
folie([(NULL, "Fall · Die Wiese"), ("notar", "Fall · Kein Notar"), ("zahlt", "Fall · Frau Ehlers zahlt nicht")], [
    linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK),
    pl("Auf der Wiese am Dorfrand", 70, 40, NULL, fill=GELB, size=40),
    ficon("tabler", "trees", 1720, BODEN - 2, 250, NULL, fuell=GRUEN),
    ficon("tabler", "fence", 960, BODEN - 2, 250, NULL, fuell=HOLZ),
    ficon("tabler", "sign-right", 230, BODEN - 2, 170, NULL, fuell=WEISS),
    pl("zu verkaufen", 230, 620, beim("fall", "verkaufen"), fill=WEISS, size=28, anker="m"),
    peep_voll("BA_ruhig_r", SX, BODEN, FH, NULL, bis="preis"),
    peep_voll("BA_froh_r", SX, BODEN, FH, "preis", anim="cut", bis="zahlt"),
    peep_voll("BA_sorge_r", SX, BODEN, FH, "zahlt", anim="cut"),
    namensschild("Herr Baumann", SX, BODEN, NULL, BLAU),
    peep_voll("EH_ruhig", FX, BODEN, FH, "ehlers", bis="preis"),
    peep_voll("EH_redet", FX, BODEN, FH, "preis", anim="cut", bis="e1"),      # Smile, Mund zu
    *redet("EH_redet", FX, BODEN, FH, "e1", "notar"),
    peep_voll("EH_ruhig", FX, BODEN, FH, "notar", anim="cut", bis="zahlt"),
    peep_voll("EH_denkt", FX, BODEN, FH, "zahlt", anim="cut"),
    namensschild("Frau Ehlers", FX, BODEN, "ehlers", PINK),
    pl("Kaufpreis: 8.500 €", 960, 290, beim("preis", "achttausendfünfhundert"), fill=GELB, size=32, anker="m"),
    szene(ficon("ph", "handshake", 960, 610, 150, "hand", fuell=GELB), "048handschlag*", 1.0, versatz=0.05),
    pl("per Handschlag", 960, 375, beim("hand", "Handschlag"), fill=WEISS, size=28, anker="m"),
    blase("sprech", 560, 190, "e1", 1520, 205, inhalt=["Abgemacht!", "Ich nehme die Wiese."], textsize=36, figur=EHa,
          bis="notar"),
    ficon("tabler", "rubber-stamp-off", 1660, 560, 110, beim("notar", "Notar"), fuell=ROT),
    pl("kein Notar", 1660, 380, beim("notar", "Notar"), fill=ROT, size=28, anker="m"),
    ficon("tabler", "cash-off", 1150, 690, 100, beim("zahlt", "zahlt"), fuell=ROT),
    pl("zahlt nicht", 1150, 525, beim("zahlt", "zahlt"), fill=WEISS, size=28, anker="m"),
])

# B Fall: im Sitzungssaal ------------------------------------------------------------------------------------------------
RIX, BAK, STX = 960, 330, 1590
RIa = ("RI_redet", RIX, 640, 380)
BAb = ("BA_redet_r", BAK, BODEN, FH)
akte = szene(bewegt(ficon("tabler", "file-text", 800, 562, 70, "klage", fuell=WEISS), "klage", ("klage", 0.35), 0, -70),
             "048akte*", 1.0, versatz=0.3)
folie([("klage", "Fall · Die Klage"), ("termin", "Fall · Der Termin"), ("leer", "Fall · Die Beklagte fehlt"),
       ("b1", "Fall · Antrag auf Versäumnisurteil"), ("frage", "Fall · Die Frage")], [
    hart(linienzug([(60, BODEN), (1860, BODEN)], "klage", breite=7, farbe=INK)),
    pl("Amtsgericht · Sitzungssaal", 70, 40, "klage", fill=GRAU, size=36, anim="cut"),
    peep_voll("RI_ruhig", RIX, 640, 380, "klage", bis="r1", anim="cut"),
    *redet("RI_redet", RIX, 640, 380, "r1", "leer"),
    peep_voll("RI_ruhig", RIX, 640, 380, "leer", bis="frage", anim="cut"),
    peep_voll("RI_denkt", RIX, 640, 380, "frage", anim="cut"),
    hart(fl_block(740, 560, 440, 110, DUNKEL, "klage", [("Gericht", "Bold", 32, WEISS)], rand=5)),
    pille("Richterin", RIX, 690, "klage", fill=LILA, size=28, anker="m", anim="cut"),
    akte,
    peep_voll("BA_ruhig_r", BAK, BODEN, FH, "klage", bis="b1", anim="cut"),
    *redet("BA_redet_r", BAK, BODEN, FH, "b1", "frage"),
    peep_voll("BA_denkt_r", BAK, BODEN, FH, "frage", anim="cut"),
    namensschild("Kläger: Herr Baumann", BAK, BODEN, "klage", BLAU, anim="cut"),
    pl("Klage: 8.500 €", BAK, 300, beim("klage", "Kaufpreis"), fill=GELB, size=30, anker="m", bis="b1"),
    pl("Klageschrift: mündlich geeinigt", BAK + 40, 220, beim("schrift", "mündliche"), fill=WEISS, size=28, anker="m",
       bis="b1"),
    ficon("ph", "chair", STX, BODEN - 2, 200, "klage", fuell=BLAU, anim="cut"),
    ficon("tabler", "clock-hour-9", STX, 330, 110, "termin", fuell=WEISS),
    pl("früher erster Termin", STX, 360, beim("termin", "frühen"), fill=WEISS, size=28, anker="m"),
    blase("sprech", 560, 170, "r1", 1000, 135, inhalt=["Ich rufe auf:", "Baumann gegen Ehlers."], textsize=32, figur=RIa,
          bis="leer"),
    pl("Beklagte: Frau Ehlers", STX, BODEN + 22, "leer", fill=PINK, size=28, anker="m"),
    pl("ordnungsgemäß geladen", STX, 470, beim("leer", "ordnungsgemäß"), fill=GRUEN, size=28, anker="m"),
    pl("nicht erschienen", STX, 560, beim("leer", "erscheint"), fill=ROT, size=28, anker="m"),
    blase("sprech", 600, 190, "b1", 470, 220, inhalt=["Dann beantrage ich", "ein Versäumnisurteil!"], textsize=34,
          figur=BAb, bis="frage"),
    pl("Bekommt er es?", 960, 120, "frage", fill=PINK, size=40, anker="m"),
    pl("Was prüft das Gericht, wenn eine Partei säumig ist?", 960, 195, "frage2", fill=WEISS, size=32, anker="m"),
])

# C Sachverhalt ----------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    glyphen("Herr Baumann und Frau Ehlers einigen sich im März 2026 mündlich: Frau Ehlers kauft seine Wiese am Dorfrand, "
            "ein eigenes Grundstück, für 8.500 Euro. Einen Notar beauftragen sie nicht. Frau Ehlers zahlt nicht."),
    glyphen("Herr Baumann klagt vor dem Amtsgericht an ihrem Wohnort auf Zahlung von 8.500 Euro; in der Klageschrift "
            "schildert er die mündliche Einigung. Das Gericht bestimmt einen frühen ersten Termin. Frau Ehlers wird die "
            "Klageschrift zugestellt, sie wird ordnungsgemäß und rechtzeitig geladen. Im Termin erscheint sie nicht. "
            "Herr Baumann beantragt ein Versäumnisurteil."),
    glyphen("Annahme: Auflassung und Eintragung im Grundbuch gibt es nicht; die übrigen Zulässigkeitsvoraussetzungen "
            "liegen vor."),
], "Wie entscheidet das Gericht?")

# D Wer ist säumig? ----------------------------------------------------------------------------------------------------------
PS0 = "Vorab: Wer ist säumig?"
folie([("wer", PS0), ("p330", f"{PS0} › Kläger: § 330 ZPO"), ("p331", f"{PS0} › Beklagter: § 331 ZPO")], rechts_frei([
    *tafel("wer", "Wer ist säumig?"),
    z("Fehlt der Kläger: § 330 ZPO", 110, 185, "p330", "Bold", 36),
    *wortlaut(110, 245, 1040, 160, "p330", [
        [("„Erscheint der Kläger im Termin zur mündlichen Verhandlung", 0)],
        [("nicht, so ist ", 0), ("auf Antrag", "a"), (" das Versäumnisurteil dahin zu erlassen,", 0)],
        [("dass der Kläger mit der Klage ", 0), ("abzuweisen", "b"), (" sei.“", 0)],
    ], 30, {"a": beim("p330", "Antrag"), "b": beim("p330", "abgewiesen")}, "§ 330 ZPO"),
    z("keine Schlüssigkeitsprüfung vorgesehen", 150, 470, beim("p330", "Schlüssigkeitsprüfung"), size=32, farbe=TEXT),
    z("Fehlt der Beklagte: § 331 ZPO", 110, 570, "p331", "Bold", 36),
    ok(135, 650, beim("p331", "So"), gr=22),
    z("So hier: Frau Ehlers fehlt.", 175, 630, beim("p331", "So"), "Bold", 34),
    peep_voll("BA_ruhig", X1, BR, FR, "wer", bis="p331"),
    peep_voll("BA_denkt", X1, BR, FR, "p331", anim="cut"),
    peep_voll("RI_ruhig", X2, BR, FR, "wer", d=0.2),
    namensschild("Herr Baumann", X1, BR, "wer", BLAU, d=0.2),
    namensschild("Richterin", X2, BR, "wer", LILA, d=0.3),
    ficon("ph", "chair", MB, 380, 110, "wer", fuell=BLAU),
    pl("Wer fehlt?", MB, 160, "wer", fill=PINK, size=30, anker="m", bis="p330"),
    pl("Kläger fehlt?", MB, 160, "p330", fill=WEISS, size=28, anker="m", anim="cut", bis="p331"),
    pl("Beklagte fehlt", MB, 160, beim("p331", "So"), fill=GRUEN, size=28, anker="m", anim="cut"),
]))

# E I. Antrag, II. Säumnis ---------------------------------------------------------------------------------------------------
PII = "II. Säumnis der Beklagten"
folie([("antrag", "I. Antrag des Klägers"), ("saeum", PII), ("p335", f"{PII} › kein Hindernis, § 335 ZPO"),
       ("nr2", f"{PII} › ordnungsgemäß geladen, Nr. 2"), ("nr3", f"{PII} › rechtzeitig mitgeteilt, Nr. 3"),
       ("hier2", f"{PII} › gegeben")], rechts_frei([
    *tafel("antrag", "I. Antrag · II. Säumnis"),
    z("I. Antrag des Klägers", 110, 180, "antrag", "Bold", 36),
    ok(560, 205, beim("antrag", "gestellt"), gr=20),
    z("II. Säumnis der Beklagten im Termin", 110, 245, "saeum", "Bold", 36),
    z("auch: erscheint, verhandelt aber nicht (§ 333 ZPO)", 150, 295, beim("saeum", "Säumig"), size=30, farbe=TEXT),
    z("kein Hindernis aus § 335 Abs. 1 ZPO", 110, 350, "p335", "Bold", 34),
    *wortlaut(110, 405, 1040, 262, "p335", [
        [("„Der Antrag auf Erlass eines Versäumnisurteils … ist", 0)],
        [("zurückzuweisen", "z"), (": … 2. wenn die nicht erschienene Partei nicht", 0)],
        [("ordnungsmäßig, insbesondere nicht rechtzeitig geladen", "a"), (" war;", 0)],
        [("3. wenn der nicht erschienenen Partei ein tatsächliches", 0)],
        [("mündliches Vorbringen oder ein Antrag ", 0), ("nicht rechtzeitig", "b")],
        [("mittels Schriftsatzes mitgeteilt", "b"), (" war; …“", 0)],
    ], 29, {"a": beim("nr2", "ordnungsgemäß"), "b": beim("nr3", "rechtzeitig"), "z": beim("zur", "zurückgewiesen")},
        "§ 335 Abs. 1 Nr. 2, 3 ZPO"),
    ok(135, 785, beim("hier2", "säumig"), gr=22),
    z("Hier: geladen, Klageschrift zugestellt: säumig", 175, 765, "hier2", "Bold", 34),
    peep_voll("BA_ruhig", X1, BR, FR, "antrag", bis=beim("antrag", "gestellt")),
    peep_voll("BA_froh", X1, BR, FR, beim("antrag", "gestellt"), anim="cut", bis="saeum"),
    peep_voll("BA_ruhig", X1, BR, FR, "saeum", anim="cut"),
    peep_voll("RI_ruhig", X2, BR, FR, "antrag", d=0.2, bis="p335"),
    peep_voll("RI_denkt", X2, BR, FR, "p335", anim="cut", bis="hier2"),
    peep_voll("RI_ruhig", X2, BR, FR, "hier2", anim="cut"),
    namensschild("Herr Baumann", X1, BR, "antrag", BLAU, d=0.2),
    namensschild("Richterin", X2, BR, "antrag", LILA, d=0.3),
    ficon("tabler", "file-text", MB, 380, 100, "antrag", fuell=WEISS, bis="saeum"),
    pl("Antrag gestellt", MB, 160, beim("antrag", "gestellt"), fill=GRUEN, size=28, anker="m", bis="saeum"),
    ficon("ph", "chair", MB, 380, 110, "saeum", fuell=BLAU, anim="cut", bis="nr2"),
    pl("Stuhl leer", MB, 160, "saeum", fill=WEISS, size=28, anker="m", anim="cut", bis="nr2"),
    ficon("tabler", "mail", MB, 380, 100, "nr2", fuell=WEISS, anim="cut", bis="hier2"),
    pl("Ladung", MB, 160, "nr2", fill=WEISS, size=28, anker="m", anim="cut", bis="nr3"),
    pl("Schriftsatz", MB, 160, "nr3", fill=WEISS, size=28, anker="m", anim="cut", bis="hier2"),
    ficon("ph", "chair", MB, 380, 110, "hier2", fuell=BLAU, anim="cut"),
    pl("säumig", MB, 160, beim("hier2", "säumig"), fill=GRUEN, size=30, anker="m"),
]))

# F III. Zulässigkeit ------------------------------------------------------------------------------------------------------
PIII = "III. Zulässigkeit der Klage"
folie([("zul", PIII), ("amt", f"{PIII} › von Amts wegen"), ("s2", f"{PIII} › § 331 Abs. 1 S. 2 ZPO"),
       (beim("hier3", "zulässig"), f"{PIII} › zulässig")], rechts_frei([
    *tafel("zul", "III. Zulässigkeit der Klage"),
    z("von Amts wegen, auch bei Säumnis", 110, 180, "amt", "Bold", 36),
    z("Prozessfähigkeit fehlt: kein Versäumnisurteil", 150, 240, beim("amt", "Prozessfähigkeit"), size=32),
    nein(1110, 260, beim("amt", "kein"), gr=20),
    z("BGH, Urt. v. 8.7.2021 – III ZR 344/20, Rn. 10", 150, 290, beim("amt", "Bundesgerichtshof"), size=28, farbe=TEXT),
    z("§ 331 Abs. 1 S. 2 ZPO:", 110, 375, "s2", "Bold", 36),
    z("Zuständigkeit aus Vereinbarung (§§ 29 Abs. 2, 38 ZPO)", 150, 430, beim("s2", "Zuständigkeit"), size=32),
    z("gilt nicht als zugestanden", 150, 480, beim("s2", "nicht"), "Bold", 32),
    fl_block(110, 570, 1040, 150, GRUEN, "hier3", [("Hier: Wohnsitz der Beklagten (§§ 12, 13 ZPO),", "Bold", 32, INK),
                                                    ("Streitwert unter 10.000 € (§ 23 Nr. 1 GVG)", "Bold", 32, INK)]),
    ok(135, 785, beim("hier3", "zulässig"), gr=22),
    z("Die Klage ist zulässig.", 175, 765, beim("hier3", "zulässig"), "ExtraBold", 36),
    peep_voll("BA_ruhig", X1, BR, FR, "zul", bis=beim("hier3", "zulässig")),
    peep_voll("BA_froh", X1, BR, FR, beim("hier3", "zulässig"), anim="cut"),
    peep_voll("RI_ruhig", X2, BR, FR, "zul", d=0.2, bis="amt"),
    peep_voll("RI_denkt", X2, BR, FR, "amt", anim="cut", bis="hier3"),
    peep_voll("RI_ruhig", X2, BR, FR, "hier3", anim="cut"),
    namensschild("Herr Baumann", X1, BR, "zul", BLAU, d=0.2),
    namensschild("Richterin", X2, BR, "zul", LILA, d=0.3),
    ficon("tabler", "file-text", MB, 380, 100, "zul", fuell=WEISS, bis="hier3"),
    pl("zulässig?", MB, 160, "zul", fill=PINK, size=30, anker="m", bis="s2"),
    pl("Vereinbarung?", MB, 160, "s2", fill=WEISS, size=28, anker="m", anim="cut", bis="hier3"),
    ficon("tabler", "building-bank", MB, 380, 120, "hier3", fuell=GRUEN, anim="cut"),
    pl("Amtsgericht zuständig", MB, 160, beim("hier3", "Streitwert"), fill=GRUEN, size=26, anker="m"),
]))

# G IV. Schlüssigkeit: Geständnisfiktion ------------------------------------------------------------------------------------
PIV = "IV. Schlüssigkeit"
folie([("schl", PIV), ("gest", f"{PIV} › Geständnisfiktion, § 331 Abs. 1 S. 1 ZPO"),
       ("zug", f"{PIV} › als zugestanden: mündliche Einigung"), ("abs2", f"{PIV} › § 331 Abs. 2 ZPO: trägt das den Antrag?")],
      rechts_frei([
    *tafel("schl", "IV. Schlüssigkeit"),
    *wortlaut(110, 180, 1040, 200, "gest", [
        [("„Beantragt der Kläger gegen den im Termin zur mündlichen", 0)],
        [("Verhandlung nicht erschienenen Beklagten das Versäumnisurteil,", 0)],
        [("so ist das ", 0), ("tatsächliche", "a"), (" mündliche Vorbringen des Klägers", 0)],
        [("als zugestanden", "b"), (" anzunehmen.“", 0)],
    ], 29, {"a": beim("gest", "tatsächliche"), "b": beim("gest", "zugestanden")}, "§ 331 Abs. 1 S. 1 ZPO"),
    z("= Geständnisfiktion", 110, 440, beim("gest", "Geständnisfiktion"), "Bold", 36),
    z("Als zugestanden gilt:", 110, 505, "zug", "Bold", 34),
    z("mündliche Einigung über die Wiese, 8.500 €", 150, 555, beim("zug", "mündlich"), size=32),
    *wortlaut(110, 625, 1040, 120, "abs2", [
        [("„Soweit es den Klageantrag ", 0), ("rechtfertigt", "a"), (", ist nach dem Antrag zu", 0)],
        [("erkennen; soweit dies nicht der Fall, ", 0), ("ist die Klage abzuweisen", "b"), (".“", 0)],
    ], 29, {"a": beim("abs2", "rechtfertigt"), "b": beim("abs2", "abzuweisen")}, "§ 331 Abs. 2 ZPO"),
    peep_voll("BA_ruhig", X1, BR, FR, "schl", bis="zug"),
    peep_voll("BA_froh", X1, BR, FR, "zug", anim="cut", bis="abs2"),
    peep_voll("BA_denkt", X1, BR, FR, "abs2", anim="cut"),
    peep_voll("RI_ruhig", X2, BR, FR, "schl", d=0.2, bis="abs2"),
    peep_voll("RI_denkt", X2, BR, FR, "abs2", anim="cut"),
    namensschild("Herr Baumann", X1, BR, "schl", BLAU, d=0.2),
    namensschild("Richterin", X2, BR, "schl", LILA, d=0.3),
    ficon("tabler", "file-text", MB, 380, 100, "schl", fuell=WEISS, bis="zug"),
    pl("schlüssig?", MB, 160, "schl", fill=PINK, size=30, anker="m", bis="gest"),
    pl("als zugestanden", MB, 160, "gest", fill=GELB, size=28, anker="m", anim="cut", bis="zug"),
    ficon("ph", "handshake", MB, 380, 120, "zug", fuell=GELB, anim="cut"),
    pl("mündlich geeinigt", MB, 160, "zug", fill=GELB, size=28, anker="m", anim="cut", bis="abs2"),
    pl("trägt das den Antrag?", MB, 160, "abs2", fill=PINK, size=26, anker="m", anim="cut"),
]))

# H IV. Schlüssigkeit: die Form ---------------------------------------------------------------------------------------------
RIh = ("RI_redet", X2, BR, FR)
BAh = ("BA_klagt", X1, BR, FR)
folie([("form", f"{PIV} › Form, § 311b Abs. 1 S. 1 BGB"), ("nichtig", f"{PIV} › nichtig, § 125 S. 1 BGB"),
       ("heil", f"{PIV} › keine Heilung"), ("unschl", f"{PIV} › unschlüssig"), ("hinw", "Hinweis, § 139 ZPO")], rechts_frei([
    *tafel("form", "IV. Schlüssigkeit: die Form"),
    *wortlaut(110, 175, 1040, 160, "form", [
        [("„Ein Vertrag, durch den sich der eine Teil verpflichtet, das", 0)],
        [("Eigentum an einem ", 0), ("Grundstück", "a"), (" zu übertragen oder zu erwerben,", 0)],
        [("bedarf der ", 0), ("notariellen Beurkundung", "b"), (".“", 0)],
    ], 30, {"a": beim("form", "Grundstück"), "b": beim("form", "notariellen")}, "§ 311b Abs. 1 S. 1 BGB"),
    *wortlaut(110, 390, 1040, 110, "nichtig", [
        [("„Ein Rechtsgeschäft, welches der durch Gesetz vorgeschriebenen", 0)],
        [("Form ermangelt, ist ", 0), ("nichtig", "a"), (".“", 0)],
    ], 29, {"a": beim("nichtig", "nichtig")}, "§ 125 S. 1 BGB"),
    z("Heilung: Auflassung und Eintragung? (§ 311b Abs. 1 S. 2)", 110, 555, "heil", "Bold", 32),
    nein(1120, 575, beim("heil", "Beides"), gr=20),
    z("als wahr unterstellt: kein Kaufpreisanspruch (§ 433 Abs. 2 BGB)", 110, 615, beim("unschl", "Kaufpreisanspruch"),
      size=30),
    fl_block(110, 665, 1040, 90, ROTHELL, beim("unschl", "unschlüssig"), [("Die Klage ist unschlüssig.", "ExtraBold", 38, INK)]),
    z("Hinweis an den Kläger, § 139 ZPO", 110, 790, "hinw", "Bold", 34),
    peep_voll("BA_ruhig", X1, BR, FR, "form", bis="nichtig"),
    peep_voll("BA_sorge", X1, BR, FR, "nichtig", anim="cut", bis=beim("unschl", "unschlüssig")),
    peep_voll("BA_schreck", X1, BR, FR, beim("unschl", "unschlüssig"), anim="cut", bis="b2"),
    *redet("BA_klagt", X1, BR, FR, "b2", "unecht"),
    peep_voll("RI_ruhig", X2, BR, FR, "form", d=0.2, bis="hinw"),
    peep_voll("RI_denkt", X2, BR, FR, "hinw", anim="cut", bis="r2"),
    *redet("RI_redet", X2, BR, FR, "r2", "b2"),
    peep_voll("RI_ruhig", X2, BR, FR, "b2", anim="cut"),
    namensschild("Herr Baumann", X1, BR, "form", BLAU, d=0.2),
    namensschild("Richterin", X2, BR, "form", LILA, d=0.3),
    ficon("tabler", "rubber-stamp-off", MB, 380, 100, beim("form", "notariellen"), fuell=ROT, bis="r2"),
    pl("kein Notar", MB, 160, beim("form", "notariellen"), fill=ROT, size=28, anker="m", bis="unschl"),
    pl("unschlüssig", MB, 160, beim("unschl", "unschlüssig"), fill=ROT, size=28, anker="m", anim="cut", bis="r2"),
    blase("sprech", 600, 200, "r2", 1500, 230, inhalt=["Ihr Kaufvertrag ist mangels", "notarieller Form nichtig."],
          textsize=30, figur=RIh, bis="b2"),
    blase("sprech", 600, 200, "b2", 1590, 230, inhalt=["Aber wir haben uns", "doch die Hand gegeben!"],
          textsize=32, figur=BAh, bis="unecht"),
]))

# I Das unechte Versäumnisurteil --------------------------------------------------------------------------------------------
PE = "Ergebnis"
folie([("unecht", f"{PE} › Abweisung trotz Säumnis"), ("streit", f"{PE} › unechtes Versäumnisurteil"),
       ("unzul", f"{PE} › unzulässige Klage: Prozessurteil"), ("rm", f"{PE} › Berufung statt Einspruch"),
       ("inhalt", f"{PE} › Inhalt, nicht Überschrift")], rechts_frei([
    *tafel("unecht", "Das unechte Versäumnisurteil"),
    z("Abweisung, obwohl die Beklagte fehlt (§ 331 Abs. 2 ZPO)", 110, 180, beim("unecht", "Das"), "Bold", 34),
    fl_block(110, 245, 500, 100, ROTHELL, beim("streit", "kein"), [("kein Versäumnisurteil", "ExtraBold", 32, INK)]),
    fl_block(650, 245, 500, 100, GRUEN, beim("streit", "streitiges"), [("streitiges Endurteil", "ExtraBold", 32, INK)]),
    z("= „unechtes Versäumnisurteil“", 110, 385, beim("streit", "unechtes"), "Bold", 36),
    z("BGH, Urt. v. 11.3.2026 – I ZR 186/25, Rn. 11", 150, 435, beim("streit", "unechtes"), size=28, farbe=TEXT),
    z("Klage unzulässig: Abweisung durch Prozessurteil", 110, 505, "unzul", "Bold", 34),
    z("BGH, Urt. v. 8.7.2021 – III ZR 344/20, Rn. 19", 150, 552, beim("unzul", "Prozessurteil"), size=28, farbe=TEXT),
    z("kein Einspruch (§ 338 ZPO)", 175, 620, beim("rm", "Einspruch"), "Bold", 34),
    nein(135, 640, beim("rm", "Einspruch"), gr=20),
    z("sondern Berufung (§ 511 ZPO)", 175, 675, beim("rm", "Berufung"), "Bold", 34),
    ok(135, 695, beim("rm", "Berufung"), gr=22),
    z("maßgeblich: nicht die Überschrift, sondern der Inhalt", 110, 750, "inhalt", size=32),
    z("BGH, Beschl. v. 17.2.2022 – IX ZB 59/20, Rn. 6", 150, 797, beim("inhalt", "Bundesgerichtshof"), size=28, farbe=TEXT),
    peep_voll("BA_sorge", X1, BR, FR, "unecht", bis="rm"),
    peep_voll("BA_denkt", X1, BR, FR, "rm", anim="cut"),
    peep_voll("RI_ruhig", X2, BR, FR, "unecht", d=0.2),
    namensschild("Herr Baumann", X1, BR, "unecht", BLAU, d=0.2),
    namensschild("Richterin", X2, BR, "unecht", LILA, d=0.3),
    ficon("ph", "chair", MB, 380, 110, "unecht", fuell=BLAU),
    pl("trotz Säumnis", MB, 160, beim("unecht", "Das"), fill=WEISS, size=28, anker="m", bis="streit"),
    pl("unechtes VU", MB, 160, beim("streit", "unechtes"), fill=GELB, size=28, anker="m", anim="cut", bis="rm"),
    pl("Berufung", MB, 160, beim("rm", "Berufung"), fill=GRUEN, size=30, anker="m", anim="cut"),
]))

# J Gegenfall: das echte Versäumnisurteil ----------------------------------------------------------------------------------
EHj = ("EH_trotz", X2, BR, FR)
folie([("gegen", "Gegenfall › notariell beurkundet: schlüssig"), ("echt", "Gegenfall › echtes Versäumnisurteil"),
       ("einspr", "Einspruch, §§ 338, 339 ZPO"), ("p342", "Einspruch › Wirkung, § 342 ZPO"),
       ("p345", "Einspruch › zweites Versäumnisurteil, § 345 ZPO")], rechts_frei([
    *tafel("gegen", "Gegenfall: echtes Versäumnisurteil"),
    z("Vertrag notariell beurkundet: Klage schlüssig", 175, 180, "gegen", "Bold", 34),
    ok(135, 200, beim("gegen", "schlüssig"), gr=22),
    z("echtes Versäumnisurteil gegen Frau Ehlers", 110, 250, beim("echt", "echtes"), "Bold", 36),
    z("Wahrheit wird nicht geprüft (§ 331 Abs. 1 S. 1 ZPO)", 150, 302, beim("echt", "Ob"), size=30, farbe=TEXT),
    z("Einspruch, §§ 338, 339 Abs. 1 ZPO", 110, 390, "einspr", "Bold", 36),
    z("binnen zwei Wochen ab Zustellung", 150, 442, beim("einspr", "zwei"), size=32),
    z("Notfrist", 150, 490, beim("einspr", "Notfrist"), "Bold", 32),
    z("§ 342 ZPO: zurück in die Lage vor der Säumnis", 110, 570, "p342", "Bold", 34),
    z("§ 345 ZPO: erneut säumig – zweites Versäumnisurteil", 110, 650, "p345", "Bold", 34),
    z("verwirft den Einspruch, kein weiterer Einspruch", 150, 700, beim("p345", "verwirft"), size=32),
    peep_voll("BA_ruhig", X1, BR, FR, "gegen", bis="echt"),
    peep_voll("BA_froh", X1, BR, FR, "echt", anim="cut"),
    peep_voll("EH_ruhig", X2, BR, FR, "gegen", d=0.2, bis="echt"),
    peep_voll("EH_sorge", X2, BR, FR, "echt", anim="cut", bis="e2"),
    *redet("EH_trotz", X2, BR, FR, "e2", "einspr"),
    peep_voll("EH_trotz", X2, BR, FR, "einspr", anim="cut", bis="p345"),
    peep_voll("EH_sorge", X2, BR, FR, "p345", anim="cut"),
    namensschild("Herr Baumann", X1, BR, "gegen", BLAU, d=0.2),
    namensschild("Frau Ehlers", X2, BR, "gegen", PINK, d=0.3),
    ficon("tabler", "file-check", MB, 380, 100, "gegen", fuell=GRUEN, bis="e2"),
    pl("notariell", MB, 160, "gegen", fill=GRUEN, size=28, anker="m", bis="e2"),
    blase("sprech", 560, 190, "e2", 1560, 230, inhalt=["Dagegen lege ich", "Einspruch ein."], textsize=34, figur=EHj,
          bis="einspr"),
    ficon("tabler", "calendar-event", MB, 380, 100, beim("einspr", "zwei"), fuell=WEISS, bis="p342"),
    pl("2 Wochen", MB, 160, beim("einspr", "zwei"), fill=GELB, size=28, anker="m", bis="p342"),
    ficon("tabler", "arrow-back-up", MB, 380, 100, "p342", fuell=WEISS, anim="cut", bis="p345"),
    pl("Lage vor der Säumnis", MB, 160, "p342", fill=WEISS, size=26, anker="m", anim="cut", bis="p345"),
    ficon("ph", "chair", MB, 380, 110, "p345", fuell=BLAU, anim="cut"),
    pl("wieder säumig", MB, 160, "p345", fill=ROT, size=28, anker="m", anim="cut"),
]))

# K Versäumnisurteil im schriftlichen Vorverfahren, § 331 III ZPO -------------------------------------------------------------
PV = "Vorverfahren"
folie([("vv", f"{PV} › Anzeige binnen zwei Wochen"), ("vv2", f"{PV} › § 331 Abs. 3 ZPO"),
       ("vv3", f"{PV} › Antrag schon in der Klageschrift")], rechts_frei([
    *tafel("vv", "Ohne Termin: § 331 Abs. 3 ZPO"),
    z("schriftliches Vorverfahren", 110, 185, beim("vv", "schriftlichen"), "Bold", 36),
    z("Verteidigungsanzeige binnen zwei Wochen", 150, 245, beim("vv", "binnen"), size=32),
    z("(§ 276 Abs. 1 S. 1 ZPO)", 150, 292, beim("vv", "binnen"), size=28, farbe=TEXT),
    z("keine Anzeige: Entscheidung ohne mündliche Verhandlung", 110, 380, "vv2", "Bold", 34),
    z("auf Antrag des Klägers (§ 331 Abs. 3 S. 1 ZPO)", 150, 432, beim("vv2", "Antrag"), size=30, farbe=TEXT),
    z("Antrag schon in der Klageschrift möglich (S. 2)", 110, 520, "vv3", "Bold", 34),
    peep_voll("EH_denkt", X1, BR, FR, "vv", bis="vv2"),
    peep_voll("EH_sorge", X1, BR, FR, "vv2", anim="cut"),
    peep_voll("RI_ruhig", X2, BR, FR, "vv", d=0.2),
    namensschild("Frau Ehlers", X1, BR, "vv", PINK, d=0.2),
    namensschild("Richterin", X2, BR, "vv", LILA, d=0.3),
    ficon("tabler", "mailbox", MB, 380, 110, "vv", fuell=WEISS, bis="vv2"),
    pl("2 Wochen", MB, 160, beim("vv", "binnen"), fill=GELB, size=28, anker="m", bis="vv2"),
    ficon("tabler", "mailbox-off", MB, 380, 110, "vv2", fuell=ROT, anim="cut"),
    pl("kein Termin", MB, 160, beim("vv2", "ohne"), fill=WEISS, size=28, anker="m", bis="vv3"),
    pl("Antrag in der Klage", MB, 160, "vv3", fill=GELB, size=26, anker="m", anim="cut"),
]))

# L Klausurtipp (Lexi) -------------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · Zulässigkeit und Schlüssigkeit"), ("tipp2", "Klausurtipp · streitiges Urteil entwerfen")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Beklagter säumig: nicht nur die Säumnis,", 200, 200, beim("tipp", "prüfst"), "Bold", 36),
    z("auch Zulässigkeit und Schlüssigkeit prüfen", 240, 255, beim("tipp", "Zulässigkeit"), size=34, farbe=TEXT),
    z("Kläger unterliegt:", 200, 360, beim("tipp2", "unterliegt"), "Bold", 38),
    z("kein Versäumnisurteil entwerfen,", 240, 415, beim("tipp2", "kein"), size=34, farbe=TEXT),
    z("sondern ein streitiges Urteil", 240, 465, beim("tipp2", "streitiges"), size=34, farbe=TEXT),
    z("mit Tatbestand und Entscheidungsgründen", 240, 515, beim("tipp2", "Tatbestand"), "Bold", 34),
    z("§ 313 Abs. 1 Nr. 5, 6 ZPO; § 313b gilt nur für das Versäumnisurteil", 240, 570, beim("tipp2", "Entscheidungsgründen"),
      size=26, farbe=TEXT),
    *redet("LX_warnt", LXX, BR, FR + 60, "tipp", "sch"),
    pille("Lexi", LXX, BR + 22, "tipp", fill=GELB, size=30, anker="m", d=0.2),
])

# M Klausurschema ------------------------------------------------------------------------------------------------------------
K1, K2 = 150, 210
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel("Klausurschema: Versäumnisurteil gegen den Beklagten", 110, 90, "sch", 52),
    z("Vorab: Wer fehlt? Kläger: § 330 ZPO – Beklagter: § 331 ZPO", K1, 190, "s0", "Bold", 34, rechts=1820),
    z("I. Antrag des Klägers", K1, 265, "sI", "Bold", 36, rechts=1820),
    z("II. Säumnis des Beklagten", K1, 330, "sII", "Bold", 36, rechts=1820),
    z("ordnungsgemäß geladen, Vorbringen rechtzeitig mitgeteilt (§ 335 Abs. 1 Nr. 2, 3 ZPO)", K2, 382,
      beim("sII", "ordnungsgemäß"), size=32, farbe=TEXT, rechts=1820),
    z("III. Zulässigkeit der Klage", K1, 455, "sIII", "Bold", 36, rechts=1820),
    z("IV. Schlüssigkeit mit Geständnisfiktion (§ 331 Abs. 1 S. 1, Abs. 2 ZPO)", K1, 520, "sIV", "Bold", 36, rechts=1820),
    z("Ergebnis", K1, 610, "serg", "ExtraBold", 36, rechts=1820),
    z("alles gegeben: echtes Versäumnisurteil – dagegen Einspruch (§ 338 ZPO)", K2, 665, "serg", size=34, rechts=1820),
    z("Zulässigkeit oder Schlüssigkeit fehlt: unechtes Versäumnisurteil – dagegen Berufung", K2, 720, "serg2", size=34,
      rechts=1820),
])

# N Merksatz (Lexi) ----------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Die Säumnis ersetzt das Geständnis,", 0)], [("nicht die Schlüssigkeit.", "a")]], 750, 310, 50, "merke",
                {"a": beim("merke", "nicht")}),
    *markertext([[("Trägt der Vortrag den Antrag nicht,", 0)], [("verliert der Kläger auch", 0)],
                 [("vor einem leeren Stuhl.", "b")]], 750, 520, 50, "mz", {"b": beim("mz", "leeren")}),
    *redet("LX_erklaert", 1680, 1000, 720, "merke", lexi_bis_ende("merke")),
])
