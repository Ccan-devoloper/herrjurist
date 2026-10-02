"""Folge 062 · Rechtfertigende Einwilligung: Wann ist Körperverletzung erlaubt? – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A Im Tattoostudio (Skizze, Aufklärung, Frage nach den Eltern, Unterschrift, Motiv), B Sachverhalt,
C Tatbestand (Wortlautkarte § 223 Abs. 1), D Rechtswidrigkeit (Wortlautkarte § 228, Einverständnis), E 1. Dispositionsbefugnis,
F 2. Einwilligungsfähigkeit (Zitatkarte BGH 1 StR 368/19 Rn. 57), G Jugendliche und Marie, H Streit Minderjährige/Eltern,
I 3.–5. Erklärung, Willensmängel, Kenntnis, J 6. Grenze § 228, K Ergebnis, L Abwandlung 14 Jahre, M Abwandlung Täuschung,
N Ausblick mutmaßliche Einwilligung, O Klausurtipp (Lexi), P Prüfschema, Q Merksatz (Lexi).
Kein Blut, keine Nadelnahaufnahmen: Studio, Skizze, Formular und Motiv nur als Icons.
Geräusche nur bei sichtbarer Handlung: Skizze wird auf den Tisch geschoben, Marie unterschreibt (Freesound CC0)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont

bausteine.FIGORDNER = "op_062/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
LILAHELL = (246, 243, 255, 255)
ROTHELL = (253, 232, 228, 255)
GRUENHELL = (232, 247, 233, 255)
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


def z(text, x, y, cue, stil="Regular", size=34, farbe=INK, d=0.0, rechts=1170, **k):
    """Tafelzeile, die rechts nicht über die Karte hinausragen darf (mobil: mindestens 26 px)."""
    assert size >= 26, f"Schrift zu klein für mobile Lesbarkeit: {text}"
    e = zeile(glyphen(text), x, y, cue, stil, size, farbe=farbe, d=d, **k)
    assert e.x + e.sprite.width <= rechts, f"Zeile zu breit: {text} ({e.x + e.sprite.width:.0f} > {rechts})"
    return e


def pl(text, *a, **k):
    assert k.get("size", 40) >= 26, f"Pille zu klein: {text}"
    return pille(glyphen(text), *a, **k)


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


# --- Eigene Hilfsfunktion (wie Folge 024/048/054): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ---------
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
XS = 1600                               # eine Figur allein neben der Tafel
HOLZ = (214, 160, 110, 255)


def fund(text, x, y, cue, **k):
    """Fundstelle (mobil lesbar: 26 px)."""
    return z(text, x, y, cue, size=26, farbe=TEXT, **k)


def skizze(cx, unten, cue, breite=200, **k):
    """Motiv-Skizze als Blatt: weiße Karte mit Zweig (Tabler plant-2) und Blüte (Fluent cherry-blossom)."""
    h = int(breite * 0.78)
    x0, y0 = cx - breite // 2, unten - h
    return [karte(x0, y0, breite, h, cue, fill=WEISS, rund=8, schatten=5, rand=4, anim=k.get("anim", "pop"), d=k.get("d", 0.0)),
            ficon("tabler", "plant-2", cx - breite * 0.12, unten - 14, int(breite * 0.45), cue, fuell=GRUEN, anim=k.get("anim", "pop"),
                  d=k.get("d", 0.0)),
            ficon("fluent-emoji-flat", "cherry-blossom", cx + breite * 0.2, unten - h * 0.42, int(breite * 0.3), cue,
                  anim=k.get("anim", "pop"), d=k.get("d", 0.0))]


def mit_bis(els, bis):
    for e in els:
        e.t1 = None
        e.bis = bis
    return els


# A Fall: im Tattoostudio -------------------------------------------------------------------------------------------------------
RX, MX = 760, 1480                      # Herr Riedel (blickt nach rechts zu Marie), Marie (blickt nach links)
TISCH = 1120
RIa = ("RI_redet_r", RX, BODEN, FH)
MAa = ("MA_redet", MX, BODEN, FH)
skz = [szene(bewegt(e, "skizze", ("skizze", 0.45), -150), "062skizze*", 1.0, versatz=0.0) if i == 0 else
       bewegt(e, "skizze", ("skizze", 0.45), -150) for i, e in enumerate(skizze(TISCH - 45, 690, beim("skizze", "Tätowierer"), 160))]
for e in skz:
    e.bis = "sv"
folie([(NULL, "Fall · Im Tattoostudio"), ("erkl", "Fall · Die Aufklärung"), ("r1", "Fall · Ohne die Eltern"),
       ("unter", "Fall · Unterschrift und Motiv"), ("frage", "Fall · Die Frage")], [
    linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK),
    pl("Samstagvormittag im Tattoostudio", 70, 40, NULL, fill=GELB, size=40),
    # Einrichtung: Behandlungsstuhl mit Lampe (links), kleiner Tisch zwischen den beiden
    ficon("tabler", "armchair", 300, BODEN - 2, 260, NULL, fuell=LILA),
    ficon("tabler", "table", TISCH, BODEN - 2, 260, NULL, fuell=HOLZ),
    # Marie kommt herein
    peep_voll("MA_ruhig", MX, BODEN, FH, NULL, bis="skizze"),          # ab 0,0 s im Bild (kein leerer erster Bildhalt)
    namensschild("Marie", MX, BODEN, NULL, GRUEN),
    pl("17 Jahre", MX + 185, 470, beim("marie", "siebzehn"), fill=WEISS, size=30, anker="m", bis="skizze"),
    blase("denk", 520, 360, beim("marie", "wünscht"), 1080, 280, inhalt=["seit Monaten:", "ein großes Motiv", " "], textsize=32,
          figur=("MA_ruhig", MX, BODEN, FH), bis="skizze"),
    pl("auf dem Unterarm", 1080, 470, beim("marie", "Unterarm"), fill=WEISS, size=28, anker="m", bis="skizze"),
    ficon("fluent-emoji-flat", "cherry-blossom", 1080, 372, 56, beim("marie", "Zweig"), bis="skizze"),
    # Herr Riedel zeigt die Skizze
    peep_voll("RI_ruhig_r", RX, BODEN, FH, beim("skizze", "Tätowierer"), anim="fade", bis="r1"),
    namensschild("Herr Riedel", RX, BODEN, beim("skizze", "Tätowierer"), LILA),
    peep_voll("MA_froh", MX, BODEN, FH, "skizze", anim="cut", bis="erkl"),
    *skz,
    pl("die Skizze", TISCH, 450, beim("skizze", "Skizze"), fill=WEISS, size=30, anker="m", bis="erkl"),
    # Aufklärung: drei Punkte zum gesprochenen Wort
    peep_voll("MA_denkt", MX, BODEN, FH, "erkl", anim="cut", bis="r1"),
    pl("bleibt für immer", 960, 150, beim("erkl", "bleibt"), fill=WEISS, size=30, anker="m", bis="r1"),
    ficon("tabler", "infinity", 760, 172, 60, beim("erkl", "bleibt"), fuell=WEISS, bis="r1"),
    pl("tut weh", 960, 235, beim("erkl", "tut"), fill=WEISS, size=30, anker="m", bis="r1"),
    pl("nur schwer zu entfernen", 960, 320, beim("erkl", "entfernen"), fill=WEISS, size=30, anker="m", bis="r1"),
    # „Wissen deine Eltern Bescheid?“ – „Nein. Aber ich bin 17, und es ist mein Arm.“
    *redet("RI_redet_r", RX, BODEN, FH, "r1", "m1"),
    peep_voll("RI_skeptisch_r", RX, BODEN, FH, "m1", anim="cut", bis="unter"),
    blase("sprech", 560, 200, "r1", 520, 230, inhalt=["Wissen deine Eltern", "Bescheid?"], textsize=34, figur=RIa, bis="m1"),
    peep_voll("MA_ruhig", MX, BODEN, FH, "r1", anim="cut", bis="m1"),
    *redet("MA_redet", MX, BODEN, FH, "m1", "unter"),
    blase("sprech", 640, 210, "m1", 1250, 230, inhalt=["Nein. Aber ich bin 17,", "und es ist mein Arm."], textsize=34,
          figur=MAa, bis="unter"),
    # Unterschrift, dann das Motiv
    peep_voll("MA_ernst", MX, BODEN, FH, "unter", anim="cut", bis="sticht"),
    szene(ficon("tabler", "writing-sign", TISCH + 85, 690, 80, beim("unter", "unterschreibt"), fuell=WEISS, bis="frage"),
          "062unterschrift*", 1.0, versatz=0.05),
    pl("unterschreibt", TISCH, 330, beim("unter", "unterschreibt"), fill=WEISS, size=30, anker="m", bis="sticht"),
    peep_voll("RI_ruhig_r", RX, BODEN, FH, "unter", anim="cut", bis="sticht"),
    peep_voll("RI_denkt_r", RX, BODEN, FH, "sticht", anim="cut"),
    peep_voll("MA_froh", MX, BODEN, FH, "sticht", anim="cut", bis="frage"),
    pl("fachgerecht nach der Skizze", TISCH, 330, beim("sticht", "fachgerecht"), fill=GRUEN, size=30, anker="m", anim="cut",
       bis="frage"),
    ficon("fluent-emoji-flat", "cherry-blossom", 1449, 642, 34, beim("sticht", "Motiv"), bis="frage"),
    ring(1449, 622, 34, 40, beim("sticht", "Motiv"), bis="frage"),
    pl("Motiv auf dem Unterarm", 1690, 330, beim("sticht", "Motiv"), fill=WEISS, size=28, anker="m", bis="frage"),
    # Die Frage
    peep_voll("MA_ruhig", MX, BODEN, FH, "frage", anim="cut"),
    pl("Körperverletzung, § 223 StGB?", 960, 150, "frage", fill=WEISS, size=32, anker="m"),
    pl("Wann erlaubt eine Einwilligung die Körperverletzung?", 960, 240, "frage2", fill=PINK, size=32, anker="m"),
])

# B Sachverhalt --------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    glyphen("An einem Samstagvormittag kommt Marie, 17 Jahre alt, in ein Tattoostudio. Seit Monaten wünscht sie sich ein "
            "großes Motiv auf dem Unterarm: einen Zweig mit Blüten. Tätowierer Herr Riedel zeigt ihr die Skizze und erklärt: "
            "Das Motiv bleibt für immer, das Stechen tut weh, und entfernen lässt es sich nur schwer."),
    glyphen("Ihre Eltern hat Marie nicht gefragt. Sie unterschreibt vor dem ersten Stich ein Einwilligungsformular. "
            "Herr Riedel sticht das Motiv fachgerecht nach der gebilligten Skizze."),
], "Hat sich Herr Riedel wegen Körperverletzung strafbar gemacht?")

# C Tatbestand: § 223 Abs. 1 StGB ------------------------------------------------------------------------------------------------
PT = "Tatbestand"
folie([("p223", f"{PT} › § 223 Abs. 1 StGB"), ("mh", f"{PT} › körperliche Misshandlung"),
       ("hamm", f"{PT} › Tätowierung als Körperverletzung"), ("vors", f"{PT} › Vorsatz: Tatbestand erfüllt")], rechts_frei([
    *tafel("p223", "Tatbestand: § 223 Abs. 1 StGB"),
    *wortlaut(110, 180, 1040, 150, "p223", [
        [("„Wer eine ", 0), ("andere Person", "a"), (" ", 0), ("körperlich mißhandelt", "b"), (" oder an der", 0)],
        [("Gesundheit schädigt", "c"), (", wird mit Freiheitsstrafe bis zu fünf Jahren", 0)],
        [("oder mit Geldstrafe bestraft.“", 0)],
    ], 30, {"a": beim("p223", "andere"), "b": beim("p223", "körperlich"), "c": beim("p223", "Gesundheit")}, "§ 223 Abs. 1 StGB"),
    z("Misshandlung: üble, unangemessene Behandlung,", 110, 395, "mh", "Bold", 32),
    z("die Wohlbefinden oder Unversehrtheit", 110, 440, beim("mh", "körperliche", 1), "Bold", 32),
    z("nicht nur unerheblich beeinträchtigt", 110, 485, beim("mh", "nicht"), "Bold", 32),
    fund("BGH, Beschl. v. 13.12.2016 – 3 StR 354/16, Rn. 4", 150, 532, beim("mh", "nicht")),
    ok(135, 610, "haut", gr=20),
    z("Haut verletzt, Farbe bleibt dauerhaft", 175, 590, "haut", size=32),
    ok(135, 665, beim("hamm", "Tätowierung"), gr=20),
    z("Tätowieren: tatbestandlich Körperverletzung", 175, 645, beim("hamm", "Tätowierung"), size=32),
    fund("OLG Hamm, Beschl. v. 5.3.2014 – 12 U 151/13, Rn. 4", 215, 690, beim("hamm", "Tätowierung")),
    fl_block(110, 750, 1040, 90, GRUEN, "vors", [("Vorsatz (+) · Tatbestand erfüllt", "ExtraBold", 34, INK)]),
    peep_voll("MA_ruhig", X1, BR, FR, "p223", bis="vors"),
    peep_voll("MA_ernst", X1, BR, FR, "vors", anim="cut"),
    peep_voll("RI_ruhig", X2, BR, FR, "p223", d=0.2, bis="hamm"),
    peep_voll("RI_denkt", X2, BR, FR, "hamm", anim="cut"),
    namensschild("Marie", X1, BR, "p223", GRUEN, d=0.2),
    namensschild("Herr Riedel", X2, BR, "p223", LILA, d=0.3),
    pl("§ 223 StGB", MB, 160, beim("p223", "Paragraf"), fill=WEISS, size=30, anker="m", bis="mh"),
    ficon("fluent-emoji-flat", "cherry-blossom", MB, 380, 90, "p223", bis="vors"),
    pl("Misshandlung?", MB, 160, "mh", fill=WEISS, size=30, anker="m", anim="cut", bis="vors"),
    pl("Tatbestand (+)", MB, 160, "vors", fill=GRUEN, size=30, anker="m", anim="cut"),
    ficon("tabler", "circle-check", MB, 380, 100, "vors", fuell=GRUEN, anim="cut"),
]))

# D Rechtswidrigkeit: § 228 StGB, Einwilligung und Einverständnis --------------------------------------------------------------
PR = "Rechtswidrigkeit"
folie([("rw", f"{PR} › Einwilligung, § 228 StGB"), ("rf", f"{PR} › Einwilligung als Rechtfertigungsgrund"),
       ("einv", f"{PR} › Abgrenzung: Einverständnis")], rechts_frei([
    *tafel("rw", "Rechtswidrigkeit: § 228 StGB"),
    *wortlaut(110, 180, 1040, 150, "p228", [
        [("„Wer eine Körperverletzung ", 0), ("mit Einwilligung", "a"), (" der verletzten", 0)],
        [("Person vornimmt, handelt ", 0), ("nur dann rechtswidrig", "b"), (", wenn die", 0)],
        [("Tat trotz der Einwilligung gegen die ", 0), ("guten Sitten", "c"), (" verstößt.“", 0)],
    ], 30, {"a": beim("p228", "Einwilligung"), "b": beim("p228", "nur"), "c": beim("p228", "guten")}, "§ 228 StGB"),
    fl_block(110, 400, 1040, 130, GELB, "rf", [("Einwilligung = Rechtfertigungsgrund", "ExtraBold", 34, INK),
                                              ("Tatbestand bleibt, Rechtswidrigkeit entfällt", "Bold", 32, INK)]),
    fl_block(110, 580, 1040, 230, LILAHELL, "einv", [("", "Bold", 30, INK)]),
    z("Anders: Einverständnis", 140, 600, "einv", "ExtraBold", 34),
    z("schließt schon den Tatbestand aus, wo das Delikt", 150, 655, beim("einv", "schließt"), size=31),
    z("ein Handeln gegen den Willen voraussetzt", 150, 700, beim("einv", "Handeln"), size=31),
    z("z. B. Wegnahme beim Diebstahl, § 242 StGB", 150, 750, beim("einv", "Wegnahme"), "Bold", 31),
    peep_voll("MA_ruhig", X1, BR, FR, "rw", bis="rf"),
    peep_voll("MA_froh", X1, BR, FR, "rf", anim="cut", bis="einv"),
    peep_voll("MA_denkt", X1, BR, FR, "einv", anim="cut"),
    peep_voll("RI_denkt", X2, BR, FR, "rw", d=0.2, bis="rf"),
    peep_voll("RI_ruhig", X2, BR, FR, "rf", anim="cut"),
    namensschild("Marie", X1, BR, "rw", GRUEN, d=0.2),
    namensschild("Herr Riedel", X2, BR, "rw", LILA, d=0.3),
    ficon("tabler", "writing-sign", MB, 380, 100, "rw", fuell=WEISS, bis="einv"),
    pl("Einwilligung", MB, 160, beim("p228", "Einwilligung"), fill=GELB, size=30, anker="m", bis="einv"),
    ficon("tabler", "hand-stop", MB, 380, 100, "einv", fuell=WEISS, anim="cut"),
    pl("gegen den Willen?", MB, 160, "einv", fill=LILA, size=28, anker="m", anim="cut"),
]))

# E 1. Dispositionsbefugnis -----------------------------------------------------------------------------------------------------
PE = "Einwilligung"
folie([("disp", f"{PE} › 1. Dispositionsbefugnis")], rechts_frei([
    *tafel("disp", "1. Dispositionsbefugnis"),
    z("Darf Marie über das Rechtsgut verfügen?", 110, 190, beim("disp", "Marie"), "Bold", 34),
    ok(135, 285, beim("disp", "Ihre"), gr=20),
    z("körperliche Unversehrtheit:", 175, 265, beim("disp", "Ihre"), "Bold", 32),
    z("Individualrechtsgut", 175, 310, beim("disp", "Individualrechtsgut"), size=32),
    fund("BGH, Urt. v. 30.1.2019 – 2 StR 325/17, Rn. 25", 175, 360, beim("disp", "Individualrechtsgut")),
    nein(135, 455, "leben", gr=18),
    z("das eigene Leben: nicht disponibel", 175, 435, "leben", "Bold", 32),
    z("§ 216 StGB (Tötung auf Verlangen)", 175, 480, beim("leben", "Paragraf"), size=32),
    fund("BGH, Urt. v. 26.5.2004 – 2 StR 505/03, Rn. 30", 175, 528, beim("leben", "Paragraf")),
    peep_voll("MA_ruhig", X1, BR, FR, "disp", bis="leben"),
    peep_voll("MA_ernst", X1, BR, FR, "leben", anim="cut"),
    peep_voll("RI_ruhig", X2, BR, FR, "disp", d=0.2),
    namensschild("Marie", X1, BR, "disp", GRUEN, d=0.2),
    namensschild("Herr Riedel", X2, BR, "disp", LILA, d=0.3),
    ficon("tabler", "user-check", MB, 380, 100, "disp", fuell=GRUEN, bis="leben"),
    pl("ihr eigener Körper", MB, 160, beim("disp", "Ihre"), fill=GRUEN, size=28, anker="m", bis="leben"),
    ficon("tabler", "heartbeat", MB, 380, 100, "leben", fuell=ROT, anim="cut"),
    pl("Leben: nein", MB, 160, "leben", fill=ROTHELL, size=30, anker="m", anim="cut"),
]))

# F 2. Einwilligungsfähigkeit: Maßstab ------------------------------------------------------------------------------------------
folie([("faehig", f"{PE} › 2. Einwilligungsfähigkeit"), ("alter", f"{PE} › 2. Einwilligungsfähigkeit: keine feste Altersgrenze")],
      rechts_frei([
    *tafel("faehig", "2. Einwilligungsfähigkeit"),
    *wortlaut(110, 175, 1040, 150, "formel", [
        [("„… einwilligungsfähig, wer nach seiner ", 0), ("geistigen und sittlichen", "a")],
        [("Reife", "a"), (" imstande ist, ", 0), ("Bedeutung und Tragweite", "b"), (" des konsentierten", 0)],
        [("Rechtsgutsangriffs zu erkennen und ", 0), ("sachgerecht zu beurteilen", "c"), (" …“", 0)],
    ], 30, {"a": beim("formel", "geistigen"), "b": beim("formel", "Bedeutung"), "c": beim("formel", "sachgerecht")},
        "BGH, Urt. v. 12.5.2020 – 1 StR 368/19, Rn. 57"),
    z("je gewichtiger der Eingriff und je schwerer", 110, 400, "streng", "Bold", 32),
    z("die Folgen absehbar, desto strenger der Maßstab", 110, 445, beim("streng", "schwerer"), "Bold", 32),
    nein(135, 555, beim("alter", "feste"), gr=18),
    z("keine feste Altersgrenze", 175, 535, beim("alter", "feste"), "Bold", 34),
    nein(135, 620, beim("alter", "Geschäftsfähigkeit"), gr=18),
    z("Geschäftsfähigkeit (BGB) nicht maßgeblich", 175, 600, beim("alter", "Geschäftsfähigkeit"), "Bold", 34),
    peep_voll("MA_ruhig", X1, BR, FR, "faehig", bis="alter"),
    peep_voll("MA_froh", X1, BR, FR, "alter", anim="cut"),
    peep_voll("RI_denkt", X2, BR, FR, "faehig", d=0.2),
    namensschild("Marie", X1, BR, "faehig", GRUEN, d=0.2),
    namensschild("Herr Riedel", X2, BR, "faehig", LILA, d=0.3),
    ficon("tabler", "bulb", MB, 380, 100, "faehig", fuell=GELB, bis="streng"),
    pl("Einsicht und Urteil", MB, 160, "formel", fill=GELB, size=28, anker="m", bis="streng"),
    ficon("tabler", "scale", MB, 380, 110, "streng", fuell=GELB, anim="cut", bis="alter"),
    pl("je schwerer, desto strenger", MB, 160, "streng", fill=WEISS, size=28, anker="m", anim="cut", bis="alter"),
    ficon("tabler", "calendar", MB, 380, 100, "alter", fuell=WEISS, anim="cut"),
    pl("kein festes Alter", MB, 160, "alter", fill=WEISS, size=30, anker="m", anim="cut"),
]))

# G 2. Einwilligungsfähigkeit: Jugendliche und Marie ----------------------------------------------------------------------------
folie([("f15", f"{PE} › 2. Einwilligungsfähigkeit: Jugendliche"), ("mf", f"{PE} › 2. Einwilligungsfähigkeit: Marie (+)")],
      rechts_frei([
    *tafel("f15", "2. Einwilligungsfähigkeit: Jugendliche"),
    fl_block(110, 180, 1040, 130, WEISS, "f15", [("BGH: 15-Jährige beim verabredeten Zweikampf", "Bold", 32, INK),
                                               ("in der Regel einwilligungsfähig", "Bold", 32, INK)], rand=4),
    fund("BGH, Urt. v. 12.5.2020 – 1 StR 368/19, Rn. 52", 110, 325, beim("f15", "Fünfzehnjährige")),
    z("Marie:", 110, 410, "mf", "ExtraBold", 36),
    ok(135, 490, beim("mf", "fast"), gr=20),
    z("fast volljährig (17)", 175, 470, beim("mf", "fast"), size=34),
    ok(135, 545, beim("mf", "monatelang"), gr=20),
    z("monatelang überlegt", 175, 525, beim("mf", "monatelang"), size=34),
    ok(135, 600, beim("mf", "kennt"), gr=20),
    z("kennt die Folgen", 175, 580, beim("mf", "kennt"), size=34),
    fl_block(110, 670, 1040, 100, GRUEN, beim("mf", "Sie"), [("Marie ist einwilligungsfähig", "ExtraBold", 36, INK)]),
    peep_voll("MA_ruhig", X1, BR, FR, "f15", bis="mf"),
    peep_voll("MA_froh", X1, BR, FR, "mf", anim="cut"),
    peep_voll("RI_ruhig", X2, BR, FR, "f15", d=0.2),
    namensschild("Marie", X1, BR, "f15", GRUEN, d=0.2),
    namensschild("Herr Riedel", X2, BR, "f15", LILA, d=0.3),
    pl("15 Jahre", MB, 160, beim("f15", "Fünfzehnjährige"), fill=WEISS, size=30, anker="m", bis="mf"),
    pl("17 Jahre", MB, 160, "mf", fill=GRUEN, size=30, anker="m", anim="cut"),
    ficon("tabler", "user-check", MB, 380, 100, "mf", fuell=GRUEN, anim="cut"),
]))

# H Streit: Minderjährige und Eltern --------------------------------------------------------------------------------------------
folie([("streit", f"{PE} › Streit: Minderjährige und Eltern"), ("vertr", f"{PE} › Streit: eigene Einwilligung genügt (vertretbar)"),
       ("zivil", f"{PE} › Zivilrecht: Vertrag, §§ 107 ff. BGB")], rechts_frei([
    *tafel("streit", "Streit: Müssen die Eltern zustimmen?", size=46),
    karte(110, 180, 505, 270, "colit", fill=ROTHELL, rund=18, schatten=6, rand=4),
    z("Teile der Literatur:", 135, 200, "colit", "ExtraBold", 30, rechts=600),
    z("zusätzlich die Eltern", 135, 245, "colit", "Bold", 28, rechts=600),
    z("bei aufschiebbaren, nicht", 135, 290, beim("colit", "aufschiebbaren"), size=28, rechts=600),
    z("notwendigen Eingriffen", 135, 330, beim("colit", "aufschiebbaren"), size=28, rechts=600),
    z("mit größeren Risiken", 135, 370, beim("colit", "größeren"), size=28, rechts=600),
    karte(645, 180, 505, 270, "bgh", fill=GRUENHELL, rund=18, schatten=6, rand=4),
    z("BGH (Zweikampf, 15 J.):", 670, 200, "bgh", "ExtraBold", 30, rechts=1135),
    z("eigene Einwilligung genügt,", 670, 245, beim("bgh", "eigene"), "Bold", 28, rechts=1135),
    z("weil keine ernsthaften", 670, 290, beim("bgh", "weil"), size=28, rechts=1135),
    z("Dauerfolgen zu erwarten", 670, 330, beim("bgh", "weil"), size=28, rechts=1135),
    z("1 StR 368/19, Rn. 58", 670, 385, beim("bgh", "weil"), size=26, farbe=TEXT, rechts=1135),
    z("Tattoo: bleibt – vom BGH damit nicht entschieden", 110, 490, "dauer", "Bold", 32),
    fl_block(110, 560, 1040, 130, GRUEN, "vertr", [("Gut vertretbar: Bei Einsichtsfähigkeit", "ExtraBold", 32, INK),
                                                  ("genügt ihre eigene Einwilligung", "Bold", 32, INK)]),
    z("Vertrag mit dem Studio: Zivilrecht, §§ 107 ff. BGB", 110, 730, "zivil", "Bold", 32),
    peep_voll("MA_ruhig", X1, BR, FR, "streit", bis="dauer"),
    peep_voll("MA_denkt", X1, BR, FR, "dauer", anim="cut", bis="vertr"),
    peep_voll("MA_froh", X1, BR, FR, "vertr", anim="cut"),
    peep_voll("RI_skeptisch", X2, BR, FR, "streit", d=0.2, bis="vertr"),
    peep_voll("RI_ruhig", X2, BR, FR, "vertr", anim="cut"),
    namensschild("Marie", X1, BR, "streit", GRUEN, d=0.2),
    namensschild("Herr Riedel", X2, BR, "streit", LILA, d=0.3),
    ficon("tabler", "users", MB, 380, 110, "streit", fuell=BLAU, bis="dauer"),
    pl("Eltern zustimmen?", MB, 160, "streit", fill=WEISS, size=30, anker="m", bis="dauer"),
    ficon("fluent-emoji-flat", "red-question-mark", MB, 380, 90, "dauer", anim="cut", bis="vertr"),
    pl("offen", MB, 160, "dauer", fill=WEISS, size=30, anker="m", anim="cut", bis="vertr"),
    ficon("tabler", "user-check", MB, 380, 100, "vertr", fuell=GRUEN, anim="cut", bis="zivil"),
    pl("vertretbar", MB, 160, "vertr", fill=GRUEN, size=30, anker="m", anim="cut", bis="zivil"),
    ficon("tabler", "file-text", MB, 380, 100, "zivil", fuell=WEISS, anim="cut"),
    pl("Zivilrecht", MB, 160, "zivil", fill=LILA, size=30, anker="m", anim="cut"),
]))

# I 3.–5.: Erklärung vor der Tat, keine Willensmängel, Kenntnis ------------------------------------------------------------------
folie([("vorher", f"{PE} › 3. Erklärung vor der Tat"), ("wm", f"{PE} › 4. keine Willensmängel"),
       ("subj", f"{PE} › 5. Handeln in Kenntnis der Einwilligung")], rechts_frei([
    *tafel("vorher", "3. bis 5.: Erklärung, Willen, Kenntnis", size=46),
    z("3. Erklärung vor der Tat, fortbestehend", 110, 180, "vorher", "ExtraBold", 34),
    ok(175, 255, beim("vorher", "Marie"), gr=18),
    z("Unterschrift vor dem ersten Stich", 215, 235, beim("vorher", "Marie"), size=32),
    z("4. keine Willensmängel", 110, 320, "wm", "ExtraBold", 34),
    z("weiß, worauf sie sich einlässt", 215, 375, beim("wm", "wissen"), size=32),
    z("nicht getäuscht", 215, 420, beim("wm", "getäuscht"), size=32),
    ok(175, 485, "aufkl", gr=18),
    z("Folgen erklärt", 215, 465, "aufkl", size=32),
    z("Umfang: fachgerechtes Motiv nach der Skizze", 215, 515, "umfang", "Bold", 32),
    fund("OLG Hamm, Beschl. v. 5.3.2014 – 12 U 151/13, Rn. 4", 215, 560, "umfang"),
    ok(175, 625, "genau", gr=18),
    z("genau das sticht er", 215, 605, "genau", size=32),
    z("5. Handeln in Kenntnis der Einwilligung", 110, 690, "subj", "ExtraBold", 34),
    ok(175, 765, beim("subj", "Herr"), gr=18),
    z("Herr Riedel kennt die Einwilligung", 215, 745, beim("subj", "Herr"), size=32),
    peep_voll("MA_ruhig", X1, BR, FR, "vorher", bis="aufkl"),
    peep_voll("MA_froh", X1, BR, FR, "aufkl", anim="cut"),
    peep_voll("RI_ruhig", X2, BR, FR, "vorher", d=0.2, bis="subj"),
    peep_voll("RI_froh", X2, BR, FR, "subj", anim="cut"),
    namensschild("Marie", X1, BR, "vorher", GRUEN, d=0.2),
    namensschild("Herr Riedel", X2, BR, "vorher", LILA, d=0.3),
    ficon("tabler", "writing-sign", MB, 380, 100, "vorher", fuell=WEISS, bis="wm"),
    pl("vorher", MB, 160, "vorher", fill=WEISS, size=30, anker="m", bis="wm"),
    ficon("tabler", "eye", MB, 380, 110, "wm", fuell=GELB, anim="cut", bis="umfang"),
    pl("keine Täuschung", MB, 160, "wm", fill=WEISS, size=30, anker="m", anim="cut", bis="umfang"),
    *mit_bis(skizze(MB, 410, "umfang", 170, anim="cut"), "subj"),
    pl("nach der Skizze", MB, 160, "umfang", fill=GRUEN, size=30, anker="m", anim="cut", bis="subj"),
    ficon("tabler", "bulb", MB, 380, 100, "subj", fuell=GELB, anim="cut"),
    pl("Kenntnis", MB, 160, "subj", fill=GELB, size=30, anker="m", anim="cut"),
]))

# J 6. Grenze: § 228 StGB ------------------------------------------------------------------------------------------------------
folie([("sitten", f"{PE} › 6. keine Sittenwidrigkeit, § 228 StGB"), ("mass", f"{PE} › 6. Maßstab: Art und Gewicht, Gefahr"),
       ("tat", f"{PE} › 6. Tattoo: kein Sittenverstoß")], rechts_frei([
    *tafel("sitten", "6. Grenze: § 228 StGB"),
    z("gute Sitten: nur der rechtliche Kern", 110, 180, "kern", "Bold", 34),
    z("Missbilligung einzelner Gruppen genügt nicht", 110, 228, beim("kern", "Was"), size=32),
    fund("BGH, Urt. v. 26.5.2004 – 2 StR 505/03, Rn. 19", 150, 275, beim("kern", "Was")),
    z("maßgeblich: Art und Gewicht der Verletzung,", 110, 340, "mass", "Bold", 34),
    z("Grad der Gefahr für Leib und Leben", 110, 388, beim("mass", "Grad"), "Bold", 34),
    fund("BGH 2 StR 505/03, Rn. 22, 24; BGH 1 StR 585/12, Rn. 9", 150, 435, beim("mass", "Grad")),
    z("jedenfalls sittenwidrig: konkrete Todesgefahr", 110, 500, "tod", "Bold", 34),
    fund("BGH 2 StR 505/03, Rn. 29", 150, 547, beim("tod", "konkrete")),
    ok(135, 635, "tat", gr=20),
    z("fachgerechtes Tattoo: kein Eingriff dieses Gewichts", 175, 615, "tat", size=32),
    ok(135, 690, beim("tat", "Ob"), gr=20),
    z("ob es den Eltern gefällt: spielt keine Rolle", 175, 670, beim("tat", "Ob"), size=32),
    fl_block(110, 740, 1040, 90, GRUEN, beim("tat", "Ob"), [("kein Verstoß gegen die guten Sitten", "ExtraBold", 34, INK)]),
    peep_voll("MA_ruhig", X1, BR, FR, "sitten", bis="tat"),
    peep_voll("MA_froh", X1, BR, FR, "tat", anim="cut"),
    peep_voll("RI_denkt", X2, BR, FR, "sitten", d=0.2, bis="tat"),
    peep_voll("RI_ruhig", X2, BR, FR, "tat", anim="cut"),
    namensschild("Marie", X1, BR, "sitten", GRUEN, d=0.2),
    namensschild("Herr Riedel", X2, BR, "sitten", LILA, d=0.3),
    ficon("tabler", "scale", MB, 380, 110, "sitten", fuell=GELB, bis="tod"),
    pl("gute Sitten?", MB, 160, "sitten", fill=WEISS, size=30, anker="m", bis="mass"),
    pl("Schwere und Gefahr", MB, 160, "mass", fill=WEISS, size=28, anker="m", anim="cut", bis="tod"),
    ficon("tabler", "heartbeat", MB, 380, 100, "tod", fuell=ROT, anim="cut", bis="tat"),
    pl("Todesgefahr?", MB, 160, "tod", fill=ROTHELL, size=30, anker="m", anim="cut", bis="tat"),
    ficon("fluent-emoji-flat", "cherry-blossom", MB, 380, 90, "tat", anim="cut"),
    pl("kein Sittenverstoß", MB, 160, "tat", fill=GRUEN, size=28, anker="m", anim="cut"),
]))

# K Ergebnis --------------------------------------------------------------------------------------------------------------------
folie([("erg", "Ergebnis · Herr Riedel ist nicht strafbar")], rechts_frei([
    *tafel("erg", "Ergebnis im Fall"),
    fl_block(110, 200, 1040, 130, GRUEN, "erg", [("Die Einwilligung ist wirksam.", "ExtraBold", 38, INK)]),
    ok(135, 445, beim("erg", "Herr"), gr=22),
    z("Herr Riedel ist nicht strafbar.", 180, 420, beim("erg", "Herr"), "Bold", 38),
    peep_voll("MA_froh", X1, BR, FR, "erg"),
    peep_voll("RI_ruhig", X2, BR, FR, "erg", d=0.2, bis=beim("erg", "Herr")),
    peep_voll("RI_froh", X2, BR, FR, beim("erg", "Herr"), anim="cut"),
    namensschild("Marie", X1, BR, "erg", GRUEN, d=0.2),
    namensschild("Herr Riedel", X2, BR, "erg", LILA, d=0.3),
    ficon("tabler", "circle-check", MB, 380, 100, "erg", fuell=GRUEN),
    pl("gerechtfertigt", MB, 160, "erg", fill=GRUEN, size=30, anker="m"),
]))

# L Abwandlung 1: Marie ist erst 14 ----------------------------------------------------------------------------------------------
folie([("ab1", "Abwandlung 1 · Marie ist erst 14"), ("ab1c", "Abwandlung 1 › Einwilligungsfähigkeit eher (−)")], rechts_frei([
    *tafel("ab1", "Abwandlung 1: Marie ist erst 14", fill=ROTHELL),
    z("großes Motiv: ein Leben lang", 110, 200, "ab1b", "Bold", 36),
    z("Folgen in diesem Alter kaum absehbar", 110, 260, beim("ab1b", "diese"), "Bold", 36),
    z("strenger Maßstab (BGH 1 StR 368/19, Rn. 57)", 110, 320, beim("ab1b", "diese"), size=30, farbe=TEXT),
    nein(135, 430, "ab1c", gr=20),
    z("liegt nahe: nicht einwilligungsfähig", 175, 410, "ab1c", "Bold", 36),
    fl_block(110, 520, 1040, 110, WEISS, beim("ab1c", "Dann"), [("Körperverletzung rechtswidrig", "ExtraBold", 36, INK)]),
    peep_voll("MA_ruhig", X1, BR, FR, "ab1", bis="ab1c"),
    peep_voll("MA_sorge", X1, BR, FR, "ab1c", anim="cut"),
    peep_voll("RI_ruhig", X2, BR, FR, "ab1", d=0.2, bis="ab1c"),
    peep_voll("RI_sorge", X2, BR, FR, "ab1c", anim="cut"),
    namensschild("Marie", X1, BR, "ab1", GRUEN, d=0.2),
    namensschild("Herr Riedel", X2, BR, "ab1", LILA, d=0.3),
    pl("14 Jahre", MB, 160, beim("ab1", "vierzehn"), fill=ROTHELL, size=30, anker="m"),
    ficon("tabler", "hourglass", MB, 380, 100, "ab1b", fuell=GELB, bis="ab1c"),
    ficon("tabler", "user-x", MB, 380, 100, "ab1c", fuell=ROT, anim="cut"),
]))

# M Abwandlung 2: Täuschung ------------------------------------------------------------------------------------------------------
RIm = ("RI_luegt", X2, BR, FR)
folie([("ab2", "Abwandlung 2 · Täuschung"), ("ab2c", "Abwandlung 2 › Einwilligung unwirksam"),
       ("ab2d", "Abwandlung 2 › Herr Riedel strafbar, § 223 StGB")], rechts_frei([
    *tafel("ab2", "Abwandlung 2: Täuschung", fill=ROTHELL),
    z("Marie zögert.", 110, 190, beim("ab2", "Marie"), "Bold", 36),
    nein(135, 270, beim("r2", "verblasst"), gr=18),
    z("„Farbe verblasst nach einem Jahr“: falsch", 175, 250, beim("r2", "verblasst"), "Bold", 34),
    z("Nur deshalb willigt Marie ein.", 110, 340, "ab2b", "Bold", 36),
    fl_block(110, 420, 1040, 130, WEISS, "ab2c", [("Durch Täuschung herbeigeführte", "ExtraBold", 34, INK),
                                                 ("Einwilligung: unwirksam", "ExtraBold", 34, INK)]),
    fund("BGH, Beschl. v. 15.10.2003 – 1 StR 300/03, Rn. 9", 150, 565, beim("ab2c", "Bundesgerichtshof")),
    fl_block(110, 640, 1040, 100, ROT, "ab2d", [("Herr Riedel: strafbar, § 223 StGB", "ExtraBold", 36, INK)]),
    peep_voll("MA_sorge", X1, BR, FR, "ab2", bis="ab2b"),
    peep_voll("MA_froh", X1, BR, FR, "ab2b", anim="cut", bis="ab2c"),
    peep_voll("MA_schreck", X1, BR, FR, "ab2c", anim="cut"),
    peep_voll("RI_ruhig", X2, BR, FR, "ab2", d=0.2, bis="r2"),
    *redet("RI_luegt", X2, BR, FR, "r2", "ab2b"),
    peep_voll("RI_froh", X2, BR, FR, "ab2b", anim="cut", bis="ab2d"),
    peep_voll("RI_sorge", X2, BR, FR, "ab2d", anim="cut"),
    namensschild("Marie", X1, BR, "ab2", GRUEN, d=0.2),
    namensschild("Herr Riedel", X2, BR, "ab2", LILA, d=0.3),
    blase("sprech", 620, 230, "r2", 1530, 210, inhalt=["Keine Sorge, diese Farbe", "verblasst nach einem", "Jahr von selbst."],
          textsize=30, figur=RIm, bis="ab2b"),
    ficon("fluent-emoji-flat", "lying-face", MB, 380, 90, "ab2b", bis="ab2c"),
    pl("gelogen", MB, 160, "ab2b", fill=ROTHELL, size=30, anker="m", bis="ab2c"),
    ficon("tabler", "file-x", MB, 380, 100, "ab2c", fuell=ROT, anim="cut"),
    pl("unwirksam", MB, 160, "ab2c", fill=ROTHELL, size=30, anker="m", anim="cut"),
]))

# N Ausblick: mutmaßliche Einwilligung -------------------------------------------------------------------------------------------
folie([("mutm", "Ausblick › mutmaßliche Einwilligung")], rechts_frei([
    *tafel("mutm", "Ausblick: mutmaßliche Einwilligung", fill=LILAHELL, size=46),
    z("Kann jemand gar nicht gefragt werden,", 110, 200, "mutm", "Bold", 36),
    z("etwa weil er bewusstlos ist:", 110, 255, beim("mutm", "etwa"), "Bold", 36),
    z("mutmaßliche Einwilligung kommt in Betracht", 110, 335, beim("mutm", "mutmaßliche"), "ExtraBold", 36),
    fund("BGH 1 StR 300/03, Rn. 10; BGH 2 StR 325/17, Rn. 16", 150, 395, beim("mutm", "mutmaßliche")),
    ficon("tabler", "bed", XS, 560, 220, "mutm", fuell=BLAU),
    ficon("tabler", "zzz", XS + 120, 360, 80, beim("mutm", "bewusstlos"), fuell=WEISS),
    pl("nicht befragbar", XS, 160, beim("mutm", "bewusstlos"), fill=WEISS, size=30, anker="m"),
]))

# O Klausurtipp (Lexi) --------------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · Einwilligung in der Rechtswidrigkeit"), ("tipp2", "Klausurtipp · Schwerpunkt Einwilligungsfähigkeit")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Einwilligung bei der Körperverletzung:", 200, 200, beim("tipp", "Einwilligung"), "Bold", 36),
    z("in der Rechtswidrigkeit prüfen", 200, 250, beim("tipp", "Rechtswidrigkeit"), "Bold", 36),
    z("Minderjährige: Schwerpunkt", 200, 345, "tipp2", size=34),
    z("Einwilligungsfähigkeit", 200, 395, beim("tipp2", "Einwilligungsfähigkeit"), "Bold", 34),
    z("Alter · Reife · Tragweite des Eingriffs", 200, 445, beim("tipp2", "Alter"), size=34),
    nein(220, 560, "tipp3", gr=18),
    z("nicht mit der Geschäftsfähigkeit", 260, 535, "tipp3", "Bold", 36),
    z("verwechseln", 260, 590, beim("tipp3", "Geschäftsfähigkeit"), "Bold", 36),
    *redet("LX_warnt", LXX, BR, FR + 60, "tipp", "sch"),
    namensschild("Lexi", LXX, BR, "tipp", GELB, d=0.2),
])

# P Prüfschema ---------------------------------------------------------------------------------------------------------------
K1, K2 = 150, 230
PS_ = "Prüfschema"
folie([("sch", PS_), ("k1", f"{PS_} › I. Tatbestand"), ("k2", f"{PS_} › II. Rechtswidrigkeit: Einwilligung"),
       ("k2a", f"{PS_} › II. 1. Dispositionsbefugnis"), ("k2b", f"{PS_} › II. 2. Einwilligungsfähigkeit"),
       ("k2c", f"{PS_} › II. 3. Erklärung vor der Tat"), ("k2d", f"{PS_} › II. 4. keine Willensmängel"),
       ("k2e", f"{PS_} › II. 5. Handeln in Kenntnis der Einwilligung"),
       ("k2f", f"{PS_} › II. 6. keine Sittenwidrigkeit, § 228 StGB"),
       ("k3", f"{PS_} › III. Schuld")], [
    karte(60, 50, 1800, 900, "sch"),
    titel("Prüfschema: Körperverletzung mit Einwilligung", 110, 90, "sch", 54),
    z("I. Tatbestand, § 223 Abs. 1 StGB", K1, 190, "k1", "Bold", 38, rechts=1820),
    z("II. Rechtswidrigkeit: Einwilligung", K1, 260, "k2", "Bold", 38, rechts=1820),
    z("1. Dispositionsbefugnis", K2, 325, "k2a", size=34, rechts=1820),
    z("2. Einwilligungsfähigkeit", K2, 380, "k2b", size=34, rechts=1820),
    z("3. Erklärung vor der Tat", K2, 435, "k2c", size=34, rechts=1820),
    z("4. keine Willensmängel", K2, 490, "k2d", size=34, rechts=1820),
    z("5. Handeln in Kenntnis der Einwilligung", K2, 545, "k2e", size=34, rechts=1820),
    z("6. kein Verstoß gegen die guten Sitten, § 228 StGB", K2, 600, "k2f", size=34, rechts=1820),
    z("III. Schuld", K1, 680, "k3", "Bold", 38, rechts=1820),
])

# Q Merksatz (Lexi) ----------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Die Einwilligung rechtfertigt, wenn eine", 0)], [("einsichtsfähige", "a"), (" Person ", 0),
                 ("vor der Tat", "b"), (" frei", 0)], [("von Willensmängeln zustimmt.", 0)]], 750, 290, 44, "merke",
                {"a": beim("merke", "einsichtsfähige"), "b": beim("merke", "vor")}),
    *markertext([[("Auf das ", 0), ("Alter allein", "c"), (" kommt es nicht an.", 0)]], 750, 520, 44, "m2",
                {"c": beim("m2", "Alter")}),
    *markertext([[("Die Grenze ziehen die ", 0), ("guten Sitten", "d"), (":", 0)], [("Schwere der Verletzung und Gefahr", 0)]],
                750, 640, 44, "m3", {"d": beim("m3", "guten")}),
    *redet("LX_erklaert", 1680, 960, 690, "merke", lexi_bis_ende("merke")),
    namensschild("Lexi", 1680, 960, "merke", GELB, d=0.2),
])
