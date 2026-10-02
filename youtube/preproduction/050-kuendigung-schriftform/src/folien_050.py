"""Folge 050 · Kündigung per WhatsApp wirksam? Schriftform nach § 623 BGB – Serienstandard Open Peeps (Katzenkönig).
Übungsfall (Frau Kuhlmann schickt ihrem Mechaniker Bastian ein Foto der unterschriebenen Kündigung per WhatsApp), Figuren
fiktiv. Szenen laut ../SZENENPLAN.md: A Werkstatt (Unterschrift, Foto), B Bastian zu Hause (Nachricht), C Arbeitsgericht
(fünf Wochen später, Frage), D Sachverhalt, E Prüfungsaufbau, F I. Kündigungserklärung, G II. Schriftform – Wortlaut
§ 623 BGB und Zweck, H Rechtsstand, I Wortlaut § 126 I BGB und Zugang der Urkunde, J Foto/Fax/E-Mail, K Rechtsfolge
§ 125 S. 1, L III. Zugang, M IV. Vertretung (§ 174, Ausblick, Frau Petersen), N V. Klagefrist (Wortlaut § 4 S. 1 KSchG,
§ 7), O Ergebnis, P Klausurtipp (Lexi), Q Klausurschema, R Merksatz (Lexi).
Geräusche nur bei sichtbarer Handlung (Stift beim Unterschreiben, Kameraauslöser, vibrierendes Handy; Freesound CC0).
Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/schild wie in Folge 043 (eigene Kopie, gemeinsame Dateien
unverändert)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_050/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
ZITAT = (246, 246, 250, 255)
GRAU = (176, 178, 190, 255)
HOLZ = (236, 214, 178, 255)
DAUER = bausteine._cj()["dauer"]
T_ = bausteine._t

_CMAP = set(TTFont(SP + "humaaans/fonts/Nunito[wght].ttf").getBestCmap())


def glyphen(text):
    """Nunito muss jedes Zeichen haben (sonst Kästchen)."""
    fehl = {c for c in text if ord(c) not in _CMAP and not c.isspace()}
    assert not fehl, f"Zeichen fehlt in Nunito: {fehl} in {text!r}"
    return text


def z(text, x, y, cue, stil="Regular", size=34, farbe=INK, d=0.0, rechts=1170, **k):
    """Tafelzeile, die rechts nicht über die Karte hinausragen darf; mobile Lesbarkeit: mindestens 26 px."""
    assert size >= 26, f"Schrift zu klein: {text}"
    e = zeile(glyphen(text), x, y, cue, stil, size, farbe=farbe, d=d, **k)
    assert e.x + e.sprite.width <= rechts, f"Zeile zu breit: {text} ({e.x + e.sprite.width:.0f} > {rechts})"
    return e


def pl(text, *a, **k):
    assert k.get("size", 40) >= 26
    return pille(glyphen(text), *a, **k)


def tafel(cue, titel_, h=840, fill=WEISS, size=46):
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(glyphen(titel_), 110, 100, cue, size)]


def blk(x, y, w, h, fill, cue, zeilen, **k):
    return fl_block(x, y, w, h, fill, cue, [(glyphen(t), s, g, f) for t, s, g, f in zeilen], **k)


def bis_(el, bis):
    el.bis = bis
    return el


def hart(e):
    e.anim = "cut"
    return e


def lexi_bis_ende(cue):
    return (cue, round(DAUER - T_(cue) - 0.05, 3))


def zit(text, x, y, cue, size=26):
    """Fundstellenzeile (grau, mindestens 26 px)."""
    return z(text, x, y, cue, size=size, farbe=TEXT)


def rechts_frei(els, x0=1250):
    """Figuren und Requisiten der Tafelfolien stehen rechts der Tafel."""
    for e in els:
        n = e.name or ""
        if n.startswith(("bild:", "ficon:")) or "/op_050/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def wortlaut(x, y, w, text, quelle, cue, marken=(), size=32, bis=None):
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de, als Zitat mit Normangabe, automatisch umbrochen.
    marken = [(Wortgruppe, cue)] legt synchron zum gesprochenen Wort einen Textmarker hinter die Wortgruppe
    (die Wortgruppe muss in einer Zeile stehen)."""
    f = F("Regular", size)
    tx, ty = x + 28, y + 26
    breite = w - 56
    zeilen, cur = [], ""
    for wort in text.split():
        t = (cur + " " + wort).strip()
        if f.getlength(t) <= breite:
            cur = t
        else:
            zeilen.append(cur); cur = wort
    zeilen.append(cur)
    lh = int(size * 1.42)
    hgt = 40 + lh * len(zeilen) + 46
    els = [bis_(karte(x, y, w, hgt, cue, fill=ZITAT, rund=18, schatten=6, rand=4), bis)]
    for wort, mc in marken:
        zi = next((i for i, t in enumerate(zeilen) if wort in t), None)
        assert zi is not None, f"Marker {wort!r} steht nicht in einer Zeile: {zeilen}"
        t = zeilen[zi]; a = t.index(wort)
        x0 = tx + f.getlength(t[:a]) - 4
        x1 = tx + f.getlength(t[:a + len(wort)]) + 4
        y0 = ty + zi * lh + size * 0.30
        im = Image.new("RGBA", (int(x1 - x0) + 2, int(size * 0.85)))
        ImageDraw.Draw(im).rounded_rectangle((0, 0, im.width - 1, im.height - 1), 7, fill=MARKER)
        els.append(El(im, x0, y0, mc, "fade", 0.0, bis, name="marker:" + wort))
    for i, t in enumerate(zeilen):
        els.append(z(t, tx, ty + i * lh, cue, size=size, rechts=x + w - 16, bis=bis))
    els.append(z(quelle, tx, ty + len(zeilen) * lh + 4, cue, "Bold", size - 4, farbe=TEXT, rechts=x + w - 16, bis=bis))
    return els, y + hgt


# --- Eigene Hilfsfunktion (wie Folge 043): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ------------------
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
    """Wie bausteine.redet(), aber Wortende = hörbares Ende; Viseme aus der Schreibung geschätzt."""
    cj = bausteine._cj(); ta, tb = T_(cue), T_(bis)
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


def fig(name, cx, unten, hoehe, folge, bis=None, erst="pop", d=0.0):
    """Mimikfolge einer Figur am selben Platz: folge = [(cue, suffix)] → harte Schnitte."""
    els = []
    for i, (c, s) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else bis
        els.append(peep_voll(f"{name}_{s}", cx, unten, hoehe, c, anim=erst if i == 0 else "cut", d=d if i == 0 else 0.0, bis=b))
    return els


def schild(text, cx, cue, fill, d=0.2, bis=None, unten=None, size=28):
    """Namensschild unter der Figur (ab dem ersten Auftritt, solange sie im Bild ist)."""
    return pl(text, cx, (unten or FB) + 22, cue, fill=fill, size=size, anker="m", d=d, bis=bis)


BODEN, FH = 880, 480
X1, X2 = 1420, 1720                         # zwei Figuren neben der Tafel
FX, FB, FR = 1560, 930, 460                 # eine Figur neben der Tafel
IX, IU = 1560, 400                          # Requisit über der Figur
MITTE = (X1 + X2) // 2
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
KU_F, BA_F, PE_F = BLAU, GRUEN, ROT         # Namensschilder passend zur Kleidung
K1, K2, K3 = 150, 210, 270


def boden(cue):
    return hart(linienzug([(60, BODEN), (1860, BODEN)], cue, breite=7, farbe=INK))


# A Fall: die Werkstatt, Unterschrift und Foto --------------------------------------------------------------------------
KU_A = 1330
KUa = ("KU_redet", KU_A, BODEN, FH)
DESK, TISCH = 880, 650                       # Schreibtisch (Mitte) und Höhe der Tischplatte
folie([(NULL, "Fall · Die Kündigung"), ("foto", "Fall · Das Foto")], [
    hart(pl("Fahrradwerkstatt Kuhlmann", 70, 40, NULL, fill=GELB, size=44)),
    boden(NULL),
    ficon("tabler", "bike", 330, BODEN - 4, 330, NULL, fuell=WEISS, anim="cut"),
    ficon("tabler", "tool", 250, 470, 110, NULL, fuell=GRAU, anim="cut"),
    ficon("tabler", "desk", DESK, BODEN - 4, 360, NULL, fuell=HOLZ, anim="cut"),
    *fig("KU", KU_A, BODEN, FH, [(NULL, "ruhig"), (beim("unterschr", "unterschreibt"), "denkt"), ("foto", "froh")],
         bis="ku1", erst="cut"),
    *redet("KU_redet", KU_A, BODEN, FH, "ku1", "whats"),
    hart(schild("Frau Kuhlmann, Inhaberin", KU_A, NULL, KU_F, unten=BODEN, d=0.0)),
    # die Kündigung auf dem Tisch
    ficon("tabler", "file-text", DESK + 40, TISCH, 110, beim("unterschr", "Kündigung"), fuell=WEISS,
          bis=beim("ku1", "Ordner")),
    pl("Kündigung", DESK + 40, 470, beim("unterschr", "Kündigung"), fill=ROT, size=30, anker="m", bis="ku1"),
    pl("an Bastian, Mechaniker", DESK + 40, 400, beim("unterschr", "Bastian"), fill=WEISS, size=28, anker="m", bis="ku1"),
    szene(ficon("tabler", "writing-sign", DESK - 70, TISCH, 90, beim("unterschr", "unterschreibt"), fuell=GELB,
                bis="foto"), "050stift*", 0.9, 0.0),
    # das Foto mit dem Handy
    szene(ficon("tabler", "camera", DESK - 90, TISCH - 10, 90, beim("foto", "fotografiert"), fuell=GRAU, bis="ku1"),
          "050kamera*", 0.8, 0.15),
    pl("Foto", DESK - 210, 470, beim("foto", "fotografiert"), fill=GELB, size=30, anker="m", bis="ku1"),
    # Figurenrede: Foto per WhatsApp, Original in den Ordner
    ficon("tabler", "device-mobile-message", DESK - 90, TISCH - 10, 90, "ku1", fuell=GRUEN),
    pl("per WhatsApp an Bastian", DESK - 90, 470, beim("ku1", "WhatsApp"), fill=GRUEN, size=28, anker="m"),
    ficon("tabler", "folder", DESK + 70, TISCH, 110, beim("ku1", "Ordner"), fuell=GELB),
    pl("Original im Ordner", DESK + 110, 400, beim("ku1", "Ordner"), fill=GELB, size=28, anker="m"),
    blase("sprech", 820, 230, "ku1", 1180, 190, inhalt=["Das Foto schicke ich ihm per WhatsApp.",
                                                      "Das Original kommt in den Ordner."], textsize=32,
          figur=KUa, bis="whats"),
])

# B Fall: Bastian bekommt die Nachricht -----------------------------------------------------------------------------------
BA_B = 1250
BAb = ("BA_redet", BA_B, BODEN, FH)
folie([("whats", "Fall · Die Nachricht")], [
    pl("Freitagabend, zu Hause", 70, 40, "whats", fill=GELB, size=44),
    boden("whats"),
    ficon("tabler", "sofa", 480, BODEN - 4, 380, "whats", fuell=LILA),
    ficon("tabler", "lamp", 140 + 60, BODEN - 4, 170, "whats", fuell=GELB),
    *fig("BA", BA_B, BODEN, FH, [("whats", "ruhig"), (beim("whats", "sofort"), "schreck")], bis="b1"),
    *redet("BA_redet", BA_B, BODEN, FH, "b1", "wochen"),
    schild("Bastian, Mechaniker", BA_B, "whats", BA_F, unten=BODEN),
    szene(ficon("tabler", "device-mobile-vibration", BA_B - 190, 600, 110, beim("whats", "Nachricht"), fuell=GRUEN),
          "050vibration*", 0.7, 0.0),
    karte(1480, 300, 380, 400, beim("whats", "Nachricht"), fill=WEISS),
    pl("WhatsApp", 1670, 340, beim("whats", "Nachricht"), fill=GRUEN, size=28, anker="m"),
    ficon("tabler", "photo", 1670, 560, 170, beim("whats", "Nachricht"), fuell=GRAU),
    pl("Kündigung (Foto)", 1670, 600, beim("whats", "sofort"), fill=ROT, size=28, anker="m"),
    blase("sprech", 820, 230, "b1", 760, 210, inhalt=["Gekündigt per WhatsApp?", "Das kann doch nicht wirksam sein!"],
          textsize=34, figur=BAb, bis="wochen"),
])

# C Fall: fünf Wochen später, die Frage --------------------------------------------------------------------------------------
BA_C, KU_C = 1000, 1620
KUc = ("KU_streng", KU_C, BODEN, FH)
folie([("wochen", "Fall · Fünf Wochen später"), ("frage", "Fall · Die Frage")], [
    pl("Fünf Wochen später", 70, 40, "wochen", fill=GELB, size=44, bis="frage"),
    boden("wochen"),
    ficon("tabler", "building-bank", 400, BODEN - 4, 340, "wochen", fuell=BLAU),
    pl("Arbeitsgericht", 400, 450, beim("wochen", "Arbeitsgericht"), fill=WEISS, size=30, anker="m"),
    *fig("BA", BA_C, BODEN, FH, [("wochen", "ruhig_r"), ("frage", "denkt_r")]),
    schild("Bastian", BA_C, "wochen", BA_F, unten=BODEN),
    ficon("tabler", "file-text", BA_C - 170, 640, 90, beim("wochen", "Klage"), fuell=WEISS),
    pl("Klage", BA_C - 170, 520, beim("wochen", "Klage"), fill=WEISS, size=28, anker="m"),
    *fig("KU", KU_C, BODEN, FH, [(beim("wochen", "Klage"), "aerger")], bis="ku2"),
    *redet("KU_streng", KU_C, BODEN, FH, "ku2", "frage"),
    peep_voll("KU_denkt", KU_C, BODEN, FH, "frage", anim="cut"),
    schild("Frau Kuhlmann", KU_C, beim("wochen", "Klage"), KU_F, unten=BODEN),
    blase("sprech", 820, 230, "ku2", 1240, 200, inhalt=["Zu spät! Nach drei Wochen gilt", "die Kündigung als wirksam."],
          textsize=34, figur=KUc, bis="frage"),
    ficon("tabler", "hourglass", 1340, 640, 80, beim("ku2", "drei"), fuell=GELB, bis="frage"),
    pl("3 Wochen?", 1340, 520, beim("ku2", "drei"), fill=GELB, size=28, anker="m", bis="frage"),
    pl("Hat das Foto das Arbeitsverhältnis beendet?", 1000, 160, "frage", fill=PINK, size=40, anker="m"),
    pl("Lief überhaupt eine Klagefrist?", 1000, 250, beim("frage", "Und"), fill=GELB, size=36, anker="m"),
])

# D Sachverhalt ------------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Frau Kuhlmann führt eine kleine Fahrradwerkstatt und beschäftigt den Mechaniker Bastian. An einem Freitagabend "
    "unterschreibt sie eigenhändig eine Kündigung, fotografiert das Schreiben mit dem Handy und schickt das Foto per "
    "WhatsApp an Bastian. Er sieht die Nachricht sofort. Das unterschriebene Original legt Frau Kuhlmann in einen "
    "Ordner; Bastian erhält es nie.",
    "Fünf Wochen später erhebt Bastian Klage beim Arbeitsgericht. Frau Kuhlmann meint, die Kündigung gelte als "
    "wirksam, weil Bastian nicht innerhalb von drei Wochen geklagt habe.",
], "Hat die Kündigung per WhatsApp das Arbeitsverhältnis beendet?")

# E Prüfungsaufbau -------------------------------------------------------------------------------------------------------------
folie([("pruef", "Wirksamkeit der Kündigung")], rechts_frei([
    *tafel("pruef", "Wirksamkeit der Kündigung"),
    z("I. Kündigungserklärung", 150, 200, beim("glied", "Kündigungserklärung"), "Bold", 38),
    z("II. Schriftform", 150, 280, beim("glied", "Schriftform"), "Bold", 38),
    z("III. Zugang", 150, 360, beim("glied", "Zugang"), "Bold", 38),
    z("IV. Vertretung", 150, 440, beim("glied", "Vertretung"), "Bold", 38),
    z("V. Klagefrist", 150, 520, beim("glied", "Klagefrist"), "Bold", 38),
    ficon("tabler", "device-mobile-message", MITTE, IU, 130, "pruef", fuell=GRUEN),
    *fig("KU", X1, FB, FH, [("pruef", "ruhig_r")]),
    *fig("BA", X2, FB, FH, [("pruef", "ruhig"), (beim("glied", "Klagefrist"), "denkt")], d=0.2),
    schild("Frau Kuhlmann", X1, "pruef", KU_F),
    schild("Bastian", X2, "pruef", BA_F, d=0.3),
]))

# F I. Kündigungserklärung ---------------------------------------------------------------------------------------------------
folie([("erkl", "I. Kündigungserklärung")], rechts_frei([
    *tafel("erkl", "I. Kündigungserklärung"),
    z("Frau Kuhlmann will das Arbeitsverhältnis", 110, 200, beim("erkl_ok", "Frau"), size=36),
    z("erkennbar beenden", 150, 255, beim("erkl_ok", "erkennbar"), "Bold", 36),
    ok(140, 360, beim("erkl_ok", "eindeutig"), gr=22),
    z("eindeutig", 185, 340, beim("erkl_ok", "eindeutig"), "Bold", 38),
    ficon("tabler", "file-text", IX, IU, 130, "erkl", fuell=WEISS),
    *fig("KU", FX, FB, FR, [("erkl", "ruhig"), ("erkl_ok", "froh")]),
    schild("Frau Kuhlmann", FX, "erkl", KU_F),
]))

# G II. Schriftform: Wortlaut § 623 BGB, Zweck --------------------------------------------------------------------------------
W623 = ("„Die Beendigung von Arbeitsverhältnissen durch Kündigung oder Auflösungsvertrag bedürfen zu ihrer Wirksamkeit "
        "der Schriftform; die elektronische Form ist ausgeschlossen.“")
w623_els, w623_y = wortlaut(80, 180, 1100, W623, "§ 623 BGB", "p623", marken=[
    ("Kündigung", beim("p623", "Kündigung")), ("oder Auflösungsvertrag", beim("p623", "Auflösungsvertrag")),
    ("Schriftform;", beim("p623", "Schriftform")),
    ("die elektronische Form ist ausgeschlossen.“", beim("p623", "elektronische"))], size=36)
folie([("form", "II. Schriftform › § 623 BGB"), ("zweck", "II. Schriftform › Zweck")], rechts_frei([
    titel(glyphen("II. Schriftform"), 110, 90, "form", 50),
    *w623_els,
    z("Zweck:", 110, w623_y + 50, "zweck", "Bold", 36),
    z("Rechtssicherheit", 260, w623_y + 50, beim("zweck", "Rechtssicherheit"), size=36),
    z("Beweis erleichtern", 260, w623_y + 110, beim("zweck", "Beweis"), size=36),
    z("bewusste Hürde vor der Kündigung", 260, w623_y + 170, beim("zweck", "bewusste"), size=36),
    zit("BAG, Urt. v. 17.12.2015 – 6 AZR 709/14, Rn. 27, 48", 260, w623_y + 230, beim("zweck", "setzen"), size=28),
    ficon("tabler", "signature", MITTE, IU, 150, "form", fuell=WEISS, bis="zweck"),
    ficon("tabler", "shield-check", MITTE, IU, 140, "zweck", fuell=GRUEN),
    *fig("KU", X1, FB, FH, [("form", "ruhig_r"), (beim("p623", "elektronische"), "sorge_r")]),
    *fig("BA", X2, FB, FH, [("form", "ruhig"), (beim("p623", "elektronische"), "froh")], d=0.2),
    schild("Frau Kuhlmann", X1, "form", KU_F),
    schild("Bastian", X2, "form", BA_F, d=0.3),
]))

# H Rechtsstand -------------------------------------------------------------------------------------------------------------------
folie([("stand", "II. Schriftform › Rechtsstand 2. Oktober 2026")], rechts_frei([
    *tafel("stand", "Rechtsstand: 2. Oktober 2026"),
    ok(140, 220, "stand", gr=22),
    z("§ 623 BGB: Wortlaut unverändert", 185, 200, "stand", "Bold", 38),
    z("Viertes Bürokratieentlastungsgesetz 2024:", 110, 320, beim("stand", "Vierte"), "Bold", 34),
    z("andere Formvorschriften gelockert", 150, 375, beim("stand", "andere"), size=34),
    z("z. B. Arbeitszeugnis elektronisch,", 150, 430, beim("stand", "Arbeitszeugnis"), size=34),
    z("§ 109 Abs. 3 GewO", 150, 485, beim("stand", "Arbeitszeugnis"), size=34),
    zit("BGBl. 2024 I Nr. 323, Art. 36 Nr. 3", 150, 540, beim("stand", "Arbeitszeugnis", ende=True), size=28),
    blk(110, 620, 1040, 100, GELB, beim("stand", "aber"), [("§ 623 BGB: nicht geändert", "ExtraBold", 38, INK)]),
    ficon("tabler", "calendar-event", MITTE, IU - 10, 130, "stand", fuell=WEISS, bis=beim("stand", "Arbeitszeugnis")),
    ficon("tabler", "certificate", MITTE, IU - 10, 140, beim("stand", "Arbeitszeugnis"), fuell=GELB),
    *fig("KU", X1, FB, FH, [("stand", "denkt_r")]),
    *fig("BA", X2, FB, FH, [("stand", "ruhig"), (beim("stand", "aber"), "froh")], d=0.2),
    schild("Frau Kuhlmann", X1, "stand", KU_F),
    schild("Bastian", X2, "stand", BA_F, d=0.3),
]))

# I Wortlaut § 126 I BGB, Zugang der Urkunde ----------------------------------------------------------------------------------
W126 = ("„Ist durch Gesetz schriftliche Form vorgeschrieben, so muss die Urkunde von dem Aussteller eigenhändig durch "
        "Namensunterschrift oder mittels notariell beglaubigten Handzeichens unterzeichnet werden.“")
w126_els, w126_y = wortlaut(80, 180, 1100, W126, "§ 126 Abs. 1 BGB", "p126", marken=[
    ("Urkunde", beim("p126", "Urkunde")),
    ("eigenhändig durch", beim("p126", "eigenhändig")),
    ("Namensunterschrift", beim("p126", "Namensunterschrift"))], size=36)
folie([("p126", "II. Schriftform › § 126 Abs. 1 BGB"), ("zugeh", "II. Schriftform › Zugang der Urkunde")], rechts_frei([
    titel(glyphen("Was heißt Schriftform?"), 110, 90, "p126", 50),
    *w126_els,
    blk(110, w126_y + 50, 1040, 150, GELB, "zugeh", [("empfangsbedürftig: genau diese", "Bold", 36, INK),
                                                   ("unterschriebene Urkunde muss zugehen", "ExtraBold", 36, INK)]),
    zit("BAG, Urt. v. 10.5.2016 – 9 AZR 145/15, Rn. 31", 110, w126_y + 220, beim("zugeh", "zugehen"), size=28),
    ficon("tabler", "writing-sign", MITTE, IU, 140, "p126", fuell=GELB, bis="zugeh"),
    bewegt(ficon("tabler", "file-text", X2 - 150, 560, 90, beim("zugeh", "Urkunde"), fuell=WEISS),
           beim("zugeh", "Urkunde"), beim("zugeh", "zugehen", ende=True), X1 + 150 - (X2 - 150), 0),
    *fig("KU", X1, FB, FH, [("p126", "ruhig_r")]),
    *fig("BA", X2, FB, FH, [("p126", "ruhig"), ("zugeh", "denkt")], d=0.2),
    schild("Frau Kuhlmann", X1, "p126", KU_F),
    schild("Bastian", X2, "p126", BA_F, d=0.3),
]))

# J Foto, Fax, E-Mail ------------------------------------------------------------------------------------------------------------
folie([("subs", "II. Schriftform › Foto, Fax, E-Mail")], rechts_frei([
    *tafel("subs", "Foto, Fax, E-Mail?"),
    nein(140, 220, beim("subs", "Foto"), gr=20),
    z("Bastian hat nur ein Foto bekommen", 185, 200, beim("subs", "Foto"), "Bold", 36),
    z("Unterschrift nur als Abbild,", 185, 260, beim("abbild", "Abbild"), size=34),
    z("das Original liegt im Ordner", 185, 312, beim("abbild", "Original"), size=34),
    nein(140, 410, beim("fax", "genügt"), gr=20),
    z("BAG: Fax genügt nicht, nur eine", 185, 390, beim("fax", "Fax"), "Bold", 34),
    z("Ablichtung der Unterschrift", 185, 442, beim("fax", "Ablichtung"), "Bold", 34),
    zit("BAG, Urt. v. 17.12.2015 – 6 AZR 709/14, Rn. 47", 185, 494, beim("fax", "wiedergibt"), size=28),
    nein(140, 580, beim("mail", "dasselbe"), gr=20),
    z("Foto, Scan, E-Mail: dasselbe", 185, 560, beim("mail", "Foto"), "Bold", 34),
    z("elektronische Form: ausgeschlossen,", 185, 615, beim("mail", "elektronische"), size=34),
    z("§ 623 Halbsatz 2 BGB", 185, 667, beim("mail", "elektronische"), size=34),
    ficon("tabler", "photo", IX, IU, 130, "subs", fuell=GRAU, bis="abbild"),
    ficon("tabler", "folder", IX, IU, 130, "abbild", fuell=GELB, bis="fax"),
    ficon("tabler", "printer", IX, IU, 130, "fax", fuell=WEISS, bis="mail"),
    pl("Fax", IX, 160, "fax", fill=WEISS, size=30, anker="m", bis="mail"),
    ficon("tabler", "mail", IX, IU, 130, "mail", fuell=GELB),
    pl("Scan per E-Mail", IX, 160, "mail", fill=GELB, size=30, anker="m"),
    *fig("BA", FX, FB, FR, [("subs", "denkt"), ("fax", "ruhig"), ("mail", "froh")]),
    schild("Bastian", FX, "subs", BA_F),
]))

# K Rechtsfolge § 125 S. 1 BGB, Treu und Glauben --------------------------------------------------------------------------------
folie([("nichtig", "II. Schriftform › Rechtsfolge, § 125 S. 1 BGB"), ("treu", "II. Schriftform › Treu und Glauben")],
      rechts_frei([
    *tafel("nichtig", "Rechtsfolge"),
    nein(140, 220, "nichtig", gr=22),
    z("Schriftform nicht gewahrt", 185, 200, "nichtig", "Bold", 38),
    blk(110, 290, 1040, 110, ROT, beim("nichtig", "Paragraf"), [("§ 125 S. 1 BGB: Kündigung nichtig", "ExtraBold", 40, INK)]),
    z("Treu und Glauben (§ 242 BGB):", 110, 470, "treu", "Bold", 34),
    z("Formmangel nur ganz ausnahmsweise unbeachtlich,", 150, 525, beim("treu", "Formmangel"), size=34),
    z("wenn das Ergebnis schlechthin untragbar wäre", 150, 580, beim("treu", "wenn"), size=34),
    zit("BAG, Urt. v. 17.12.2015 – 6 AZR 709/14, Rn. 46, 51", 150, 640, beim("treu", "untragbar"), size=28),
    ficon("tabler", "file-x", MITTE, IU, 140, beim("nichtig", "nichtig"), fuell=ROT),
    *fig("KU", X1, FB, FH, [("nichtig", "ruhig_r"), (beim("nichtig", "nichtig"), "sorge_r")]),
    *fig("BA", X2, FB, FH, [("nichtig", "ruhig"), (beim("nichtig", "nichtig"), "strahlt")], d=0.2),
    schild("Frau Kuhlmann", X1, "nichtig", KU_F),
    schild("Bastian", X2, "nichtig", BA_F, d=0.3),
]))

# L III. Zugang ------------------------------------------------------------------------------------------------------------------
MB = MITTE
folie([("zug", "III. Zugang, § 130 BGB")], rechts_frei([
    *tafel("zug", "III. Zugang"),
    ok(140, 220, beim("zug2", "sofort"), gr=20),
    z("Foto: sofort auf dem Handy von Bastian", 185, 200, beim("zug2", "Foto"), size=34),
    nein(140, 280, beim("zug2", "formgerechte"), gr=20),
    z("zugehen muss die formgerechte Erklärung", 185, 260, beim("zug2", "Zugehen"), "Bold", 34),
    z("Original später in den Briefkasten:", 110, 360, beim("brief", "Original"), size=34),
    z("wirksam erst mit dessen Zugang,", 150, 415, beim("brief", "erst"), "Bold", 34),
    z("§ 130 Abs. 1 S. 1 BGB", 150, 470, beim("brief", "Paragraf"), "Bold", 34),
    blk(110, 560, 1040, 100, GELB, "frist_ab", [("Erst ab dann läuft die Klagefrist.", "ExtraBold", 38, INK)]),
    ficon("tabler", "device-mobile-message", MB, IU, 120, "zug", fuell=GRUEN, bis="brief"),
    ficon("tabler", "mailbox", MB, IU, 140, "brief", fuell=WEISS, bis=beim("brief", "Briefkasten", ende=True)),
    ficon("tabler", "mailbox", MB, IU, 140, beim("brief", "Briefkasten", ende=True), fuell=GELB, anim="cut"),
    bewegt(ficon("tabler", "mail", MB, 230, 70, beim("brief", "Original"), fuell=WEISS,
                 bis=beim("brief", "Briefkasten", ende=True)),
           beim("brief", "Original"), beim("brief", "Briefkasten", ende=True), X1 - MB, 40),
    ficon("tabler", "hourglass", MB, 210, 70, "frist_ab", fuell=GELB),
    *fig("KU", X1, FB, FH, [("zug", "ruhig_r"), ("brief", "denkt_r")]),
    *fig("BA", X2, FB, FH, [("zug", "ruhig"), ("frist_ab", "denkt")], d=0.2),
    schild("Frau Kuhlmann", X1, "zug", KU_F),
    schild("Bastian", X2, "zug", BA_F, d=0.3),
]))

# M IV. Vertretung (Ausblick § 174) ------------------------------------------------------------------------------------------------
PEm = ("PE_redet_r", X1, FB, FH)
folie([("vertr", "IV. Vertretung › Ausblick"), ("p174", "IV. Vertretung › Zurückweisung, § 174 BGB")], rechts_frei([
    *tafel("vertr", "IV. Vertretung (Ausblick)"),
    z("Werkstattleiterin Frau Petersen", 110, 190, beim("peters", "Werkstattleiterin"), "Bold", 34),
    z("unterschreibt das Original in Vertretung", 150, 242, beim("peters", "Original"), size=34),
    nein(140, 330, beim("p174", "keine"), gr=20),
    z("keine Vollmachtsurkunde vorgelegt", 185, 310, beim("p174", "keine"), size=34),
    z("Bastian kann unverzüglich zurückweisen,", 110, 385, beim("p174", "unverzüglich"), "Bold", 34),
    z("§ 174 S. 1 BGB", 150, 437, beim("p174", "Paragraf"), "Bold", 34),
    z("mehr als eine Woche ohne besondere", 110, 512, "woche", size=34),
    z("Umstände: zu spät", 150, 564, beim("woche", "zu"), size=34),
    zit("BAG, Urt. v. 7.5.2026 – 2 AZR 130/25, Rn. 26", 150, 618, beim("woche", "spät"), size=28),
    blk(110, 680, 1040, 150, GELB, "kennt", [("ausgeschlossen, wenn Frau Kuhlmann ihn", "Bold", 34, INK),
                                           ("in Kenntnis gesetzt hatte, § 174 S. 2 BGB", "ExtraBold", 34, INK)]),
    ficon("tabler", "file-certificate", MITTE, 260, 100, beim("p174", "Vollmachtsurkunde"), fuell=WEISS, bis="woche"),
    ficon("tabler", "hand-stop", MITTE, 260, 100, "woche", fuell=ROT, bis="kennt"),
    ficon("tabler", "message", MITTE, 260, 100, "kennt", fuell=WEISS),
    *fig("PE", X1, FB, FH, [(beim("peters", "Werkstattleiterin"), "ruhig_r")], bis="pe1"),
    *redet("PE_redet_r", X1, FB, FH, "pe1", "p174"),
    peep_voll("PE_denkt_r", X1, FB, FH, "p174", anim="cut"),
    schild("Frau Petersen", X1, beim("peters", "Werkstattleiterin"), PE_F),
    *fig("BA", X2, FB, FH, [("vertr", "ruhig"), ("p174", "denkt"), ("kennt", "sorge")], d=0.2),
    schild("Bastian", X2, "vertr", BA_F, d=0.3),
    blase("sprech", 640, 220, "pe1", 1560, 150, inhalt=["Hier ist deine Kündigung,", "unterschrieben in Vertretung."],
          textsize=32, figur=PEm, bis="p174"),
]))

# N V. Klagefrist: Wortlaut § 4 S. 1 KSchG, § 7 KSchG -------------------------------------------------------------------------------
W4 = ("„Will ein Arbeitnehmer geltend machen, dass eine Kündigung sozial ungerechtfertigt oder aus anderen Gründen "
      "rechtsunwirksam ist, so muss er innerhalb von drei Wochen nach Zugang der schriftlichen Kündigung Klage beim "
      "Arbeitsgericht auf Feststellung erheben, dass das Arbeitsverhältnis durch die Kündigung nicht aufgelöst ist.“")
w4_els, w4_y = wortlaut(80, 160, 1100, W4, "§ 4 Satz 1 KSchG", "klage", marken=[
    ("innerhalb von drei Wochen", beim("p4", "innerhalb")),
    ("schriftlichen Kündigung", beim("schrift", "schriftlich"))], size=30)
folie([("klage", "V. Klagefrist › § 4 S. 1 KSchG"), ("p7", "V. Klagefrist › § 7 KSchG"),
       ("schrift", "V. Klagefrist › nur bei schriftlicher Kündigung")], rechts_frei([
    titel(glyphen("V. Klagefrist"), 110, 80, "klage", 48),
    *w4_els,
    z("§ 7 KSchG: sonst gilt sie als von Anfang an", 110, w4_y + 30, "p7", "Bold", 32),
    z("rechtswirksam", 150, w4_y + 78, beim("p7", "rechtswirksam"), "Bold", 32),
    nein(140, w4_y + 160, beim("schrift", "nie"), gr=20),
    z("Bastian ist nie eine schriftliche Kündigung zugegangen", 185, w4_y + 140, beim("schrift", "Eine"), size=30),
    blk(110, w4_y + 205, 1040, 90, GRUEN, "lauf", [("Frist lief nicht: Formmangel nach 5 Wochen rügbar", "ExtraBold", 32, INK)]),
    zit("BAG, Urt. v. 6.9.2012 – 2 AZR 858/11, Rn. 11", 110, w4_y + 310, beim("lauf", "geltend"), size=28),
    ficon("tabler", "hourglass", MITTE, IU, 120, "klage", fuell=GELB, bis="schrift"),
    ficon("tabler", "file-x", MITTE, IU, 130, "schrift", fuell=ROT),
    *fig("KU", X1, FB, FH, [("klage", "froh_r"), ("schrift", "sorge_r")]),
    *fig("BA", X2, FB, FH, [("klage", "sorge"), ("lauf", "strahlt")], d=0.2),
    schild("Frau Kuhlmann", X1, "klage", KU_F),
    schild("Bastian", X2, "klage", BA_F, d=0.3),
]))

# O Ergebnis ------------------------------------------------------------------------------------------------------------------------
folie([("erg", "Ergebnis · Kündigung nichtig")], rechts_frei([
    *tafel("erg", "Ergebnis"),
    blk(110, 200, 1040, 110, ROT, beim("erg", "Kündigung"), [("Kündigung per WhatsApp: nichtig", "ExtraBold", 40, INK)]),
    blk(110, 360, 1040, 110, GRUEN, beim("erg", "Arbeitsverhältnis"), [("Das Arbeitsverhältnis besteht fort.", "ExtraBold", 40, INK)]),
    ficon("tabler", "bike", MITTE, IU, 170, beim("erg", "Arbeitsverhältnis"), fuell=WEISS),
    *fig("KU", X1, FB, FH, [("erg", "sorge_r")]),
    *fig("BA", X2, FB, FH, [("erg", "ruhig"), (beim("erg", "Arbeitsverhältnis"), "strahlt")], d=0.2),
    schild("Frau Kuhlmann", X1, "erg", KU_F),
    schild("Bastian", X2, "erg", BA_F, d=0.3),
]))

# P Klausurtipp (Lexi) ---------------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · Fehlerquelle Klagefrist"), ("tipp3", "Klausurtipp · gesetzliche oder vereinbarte Schriftform")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Der typische Fehler: die Klagefrist", 200, 200, beim("tipp", "typische"), "Bold", 38),
    z("Nicht vom Fristablauf täuschen lassen:", 110, 300, "tipp2", size=36),
    z("§ 7 KSchG greift nur, wenn eine", 150, 355, beim("tipp2", "Paragraf"), "Bold", 36),
    z("schriftliche Kündigung zugegangen ist", 150, 410, beim("tipp2", "schriftliche"), "Bold", 36),
    z("gesetzliche Schriftform: § 126 BGB", 110, 510, beim("tipp3", "gesetzliche"), size=36),
    z("vereinbarte Schriftform: § 127 Abs. 2 BGB,", 110, 570, beim("tipp3", "vereinbarten", nr=1), size=36),
    z("im Zweifel genügt telekommunikative", 150, 625, beim("tipp3", "Zweifel"), size=36),
    z("Übermittlung", 150, 680, beim("tipp3", "telekommunikative"), size=36),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    schild("Lexi", FX, "tipp", GELB),
])

# Q Klausurschema -------------------------------------------------------------------------------------------------------------------
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel(glyphen("Klausurschema: Wirksamkeit der Kündigung"), 110, 90, "sch", 46),
    z("I. Kündigungserklärung", K1, 200, "k1", "Bold", 38, rechts=1820),
    z("II. Schriftform, § 623 i. V. m. § 126 Abs. 1 BGB", K1, 275, "k2", "Bold", 38, rechts=1820),
    z("eigenhändig unterschriebene Urkunde", K2, 335, "k2a", size=36, rechts=1820),
    z("sonst: nichtig, § 125 S. 1 BGB", K2, 392, "k2b", size=36, farbe=TEXT, rechts=1820),
    z("III. Zugang des Originals, § 130 BGB", K1, 470, "k3", "Bold", 38, rechts=1820),
    z("IV. Vertretung: Zurückweisung nach § 174 BGB", K1, 545, "k4", "Bold", 38, rechts=1820),
    z("V. Klagefrist, §§ 4, 7 KSchG: nur bei schriftlicher Kündigung", K1, 620, "k5", "Bold", 38, rechts=1820),
])

# R Merksatz (Lexi) --------------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Eine Kündigung des Arbeitsverhältnisses", 0)], [("braucht das ", 0), ("eigenhändig unterschriebene", "a")],
                 [("Original", "b"), (" beim Empfänger.", 0)]],
                750, 300, 44, "merke", {"a": beim("merke", "eigenhändig"), "b": beim("merke", "Original")}),
    *markertext([[("Foto, Fax und E-Mail genügen nicht.", 0)]], 750, 560, 44, "m2", {}),
    *markertext([[("Ohne schriftliche Kündigung", 0)], [("läuft ", 0), ("keine Klagefrist", "c"), (".", 0)]],
                750, 660, 44, beim("m2", "Und"), {"c": beim("m2", "keine")}),
    *redet("LX_erklaert", 1680, 950, 690, "merke", lexi_bis_ende("merke")),
    schild("Lexi", 1680, "merke", GELB, unten=950),
])
