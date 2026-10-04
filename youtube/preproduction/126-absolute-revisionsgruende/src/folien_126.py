"""Folge 126 · Absolute Revisionsgründe § 338 StPO: Der Katalog und die Nr. 8 – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A Sitzungssaal 2 (Vorsitzender lässt die Tür abschließen), B Flur (Lene vor verschlossener
Tür), C Flur nach dem Urteil (Strobel: „Das rüge ich.“), D Sachverhalt, E 1. Einordnung (Wortlautkarte § 338 Einleitungssatz),
F 2. Nr. 1 Besetzung (§§ 222a, 222b StPO), G 2. Katalog als Tabelle (Nr. 1, 5, 6, 7, 8), H1/H2 3. Nr. 8 (Wortlautkarten
§ 338 Nr. 8 und BGH 5 StR 52/26 Rn. 8), I 4. Fall: Nr. 6 (Wortlautkarten § 338 Nr. 6 und § 169 Abs. 1 S. 1 GVG),
J Zurechnung und Ausnahmen, K Ergebnis, L Klausurtipp (Lexi), M Schema, N Merksatz (Lexi).
Geräusche nur bei sichtbarer Handlung: Schlüssel im Schloss (A), Lene rüttelt an der Klinke (B); Freesound CC0.
Hilfsfunktionen glyphen/z/pl/fb/tafel/wortlaut/redet/namensschild als eigene Kopie aus Folge 072 (gemeinsame Dateien
unverändert). Zahlen auf Tafeln, Pillen und Blasen als Ziffern (Wortlautkarten wörtlich, amtlich „Beschluß“)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont

bausteine.FIGORDNER = "op_126/"

_run0 = bausteine._sp.run


def _run_c(args, **k):
    """Sprechblasen müssen im Stil C gelingen (kein stiller Rückfall auf Stil E)."""
    r = _run0(args, **k)
    if len(args) > 1 and str(args[1]).endswith("blase_c.js"):
        assert r.returncode == 0, f"Blase Stil C fehlgeschlagen: {args[2]}"
    return r


bausteine._sp.run = _run_c

FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
ROTHELL = (253, 232, 228, 255)
GRUENHELL = (232, 247, 233, 255)
BLAUHELL = (232, 240, 253, 255)
HOLZ = (214, 160, 110, 255)
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


def fb(x, y, w, h, fill, cue, zeilen, **k):
    for t, s, g, _ in zeilen:
        glyphen(t)
        assert F(s, g).getlength(t) <= w - 30, f"Blockzeile zu breit: {t}"
    return fl_block(x, y, w, h, fill, cue, zeilen, **k)


def tafel(cue, titel_, h=840, fill=WEISS, size=46):
    """Rechtstafel links, rechts bleibt Platz für die Figuren."""
    assert 110 + F("ExtraBold", size).getlength(glyphen(titel_)) <= 1170, f"Titel zu breit: {titel_}"
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(titel_, 110, 100, cue, size)]


def wortlaut(x, y, w, h, cue, zeilen, size, hl, quelle, quelle_cue=None):
    """Wortlautkarte: wörtliches Zitat (gesetze-im-internet.de bzw. amtlicher Volltext, Abruf 03.10.2026) in einer hellen
    Karte, Fundstelle darunter rechts. zeilen = Liste von Token-Listen [(text, Schlüssel|0)], hl = {Schlüssel: Cue}."""
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
        if n.startswith(("bild:", "ficon:")) or "/op_126/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def namensschild(text, cx, unten, cue, fill, **k):
    return pille(glyphen(text), cx, unten + 22, cue, fill=fill, size=30, anker="m", **k)


def hart(e):
    e.anim = "cut"
    return e


def fund(text, x, y, cue, rechts=1170):
    return z(text, x, y, cue, size=26, farbe=TEXT, rechts=rechts)


# --- Eigene Hilfsfunktion (wie Folge 072): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ---------------
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
X1, X2 = 1390, 1730                     # zwei Figuren neben der Tafel
MB = (X1 + X2) // 2
XS = 1600                               # eine Figur allein neben der Tafel


def tuer(cx, cue, **k):
    """Saaltür (Tabler „door“, Holzfüllung) auf der Bodenlinie."""
    return ficon("tabler", "door", cx, BODEN - 2, 470, cue, fuell=HOLZ, anim="cut", **k)


# A Fall: im Sitzungssaal ----------------------------------------------------------------------------------------------------
VX, TX, WX = 520, 1330, 1660            # Vorsitzender hinter der Richterbank, Tür, Wachtmeister
VRa = ("VR_redet_r", VX, BODEN, FH)
schluessel = szene(ficon("tabler", "key", TX + 150, 700, 70, "ab", fuell=GELB), "126schluessel*", 1.0, versatz=0.05)

folie([(NULL, "Fall · Im Sitzungssaal"), ("anklage", "Fall · Die Anklage"), ("zeugin", "Fall · Die Aussage der Zeugin"),
       ("v1", "Fall · Die Tür wird abgeschlossen"), ("keinb", "Fall · Kein Beschluss")], [
    hart(linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK)),
    pl("Landgericht · Saal 2", 70, 40, NULL, fill=GELB, size=40, anim="cut"),
    tuer(TX, NULL),
    peep_voll("VR_ruhig_r", VX, BODEN, FH, NULL, anim="cut", bis="v1"),
    *redet("VR_redet_r", VX, BODEN, FH, "v1", "ab"),
    peep_voll("VR_ruhig_r", VX, BODEN, FH, "ab", anim="cut", bis="keinb"),
    peep_voll("VR_denkt_r", VX, BODEN, FH, "keinb", anim="cut"),
    karte(VX - 270, BODEN - 235, 540, 233, NULL, fill=HOLZ, rund=10, schatten=6, anim="cut"),   # Richterbank (Baustein wie 015)
    namensschild("Vorsitzender Richter", VX, BODEN, NULL, WEISS, anim="cut"),
    pl("Strafkammer", VX, 235, beim("fall", "Strafkammer"), fill=WEISS, size=28, anker="m", bis="v1"),
    pl("gegen Herrn Lemke", VX, 300, beim("fall", "Lemke"), fill=WEISS, size=28, anker="m", bis="v1"),
    pl("Anklage: Sexualdelikt", 960, 230, "anklage", fill=WEISS, size=30, anker="m", bis="v1"),
    pl("gleich: Aussage der Zeugin", 960, 300, "zeugin", fill=BLAUHELL, size=30, anker="m", bis="v1"),
    peep_voll("WM_ruhig", WX, BODEN, FH, NULL, anim="cut", bis="ab"),
    peep_voll("WM_ernst", WX, BODEN, FH, "ab", anim="cut"),
    namensschild("Justizwachtmeister", WX, BODEN, NULL, BLAUHELL, anim="cut"),
    blase("sprech", 820, 220, "v1", 1000, 200, inhalt=["Herr Wachtmeister, schließen Sie bitte", "die Saaltür ab. Die Zeugin soll",
          "in Ruhe aussagen können."], textsize=30, figur=VRa, bis="ab"),
    schluessel,
    ficon("tabler", "lock", TX + 90, 700, 70, beim("ab", "schließt"), fuell=ROT, d=0.3),
    pl("abgeschlossen", TX, 420, beim("ab", "schließt"), fill=ROTHELL, size=30, anker="m", d=0.3),
    nein(760, 270, beim("keinb", "nicht"), gr=22),
    pl("kein Beschluss der Kammer", 960, 230, "keinb", fill=ROTHELL, size=32, anker="m"),
    pl("über den Ausschluss der Öffentlichkeit", 960, 300, beim("keinb", "Ausschluss"), fill=WEISS, size=28, anker="m"),
])

# B Fall: auf dem Flur ---------------------------------------------------------------------------------------------------------
TB, LX_ = 700, 1150                    # Tür von außen, Lene
LEb = ("LE_redet", LX_, BODEN, FH)
LE_AN = beim("flur", "Lene")             # Lene kommt beim Wort „Lene“ ins Bild, Namensschild läuft mit
lene_kommt = bewegt(peep_voll("LE_ruhig", LX_, BODEN, FH, LE_AN, anim="cut", bis="l1"), LE_AN, beim("flur", "Jurastudentin"),
                    420, 0)
folie([("flur", "Fall · Auf dem Flur"), ("auf", "Fall · Die Tür wird wieder geöffnet")], [
    hart(linienzug([(60, BODEN), (1860, BODEN)], "flur", breite=7, farbe=INK)),
    pl("Flur vor Saal 2", 70, 40, "flur", fill=GELB, size=40, anim="cut"),
    tuer(TB, "flur"),
    pl("Saal 2", TB, 400, "flur", fill=WEISS, size=30, anker="m", anim="cut"),
    ficon("tabler", "lock", TB + 90, 700, 70, "flur", fuell=ROT, anim="cut", bis="auf"),
    lene_kommt,
    *redet("LE_redet", LX_, BODEN, FH, "l1", "auf"),
    peep_voll("LE_froh", LX_, BODEN, FH, "auf", anim="cut"),
    bewegt(namensschild("Lene, Jurastudentin", LX_, BODEN, LE_AN, LILA, anim="cut"), LE_AN, beim("flur", "Jurastudentin"), 420, 0),
    pl("will zuschauen", LX_, 330, beim("flur", "verfolgen"), fill=WEISS, size=28, anker="m", bis="l1"),
    szene(pl("abgeschlossen!", TB, 320, beim("l1", "Abgeschlossen"), fill=ROTHELL, size=30, anker="m", bis="auf"),
          "126klinke*", 1.0),
    blase("sprech", 700, 200, "l1", 1450, 200, inhalt=["Abgeschlossen? Die Verhandlung", "ist doch öffentlich!"],
          textsize=30, figur=LEb, bis="auf"),
    ficon("tabler", "lock-open", TB + 90, 700, 70, "auf", fuell=GRUEN, anim="cut"),
    pl("erst nach der Aussage wieder offen", TB, 320, "auf", fill=GRUENHELL, size=30, anker="m"),
])

# C Fall: nach dem Urteil ---------------------------------------------------------------------------------------------------------
MX, SX = 1200, 1660                    # Herr Lemke (blickt nach rechts), Rechtsanwalt Strobel (blickt nach links)
STc = ("ST_redet", SX, BODEN, FH)
folie([("urteil", "Fall · Das Urteil"), ("rev", "Fall · Die Revision"), ("frage", "Fall · Die Frage")], [
    hart(linienzug([(60, BODEN), (1860, BODEN)], "urteil", breite=7, farbe=INK)),
    pl("Nach dem Urteil", 70, 40, "urteil", fill=GELB, size=40, anim="cut"),
    peep_voll("LM_sorge_r", MX, BODEN, FH, "urteil", anim="cut", bis="frage"),
    peep_voll("LM_denkt_r", MX, BODEN, FH, "frage", anim="cut"),
    namensschild("Herr Lemke, Angeklagter", MX, BODEN, "urteil", WEISS),
    peep_voll("ST_ruhig", SX, BODEN, FH, beim("rev", "Verteidiger"), bis="st1"),
    *redet("ST_redet", SX, BODEN, FH, "st1", "frage"),
    peep_voll("ST_ernst", SX, BODEN, FH, "frage", anim="cut"),
    namensschild("Rechtsanwalt Strobel", SX, BODEN, beim("rev", "Verteidiger"), GRUEN),
    ficon("tabler", "gavel", 230, 470, 120, "urteil", fuell=HOLZ),
    pl("Urteil: verurteilt", 330, 400, "urteil", fill=WEISS, size=34),
    ficon("tabler", "file-text", 230, 690, 110, beim("rev", "legt"), fuell=GELB),
    pl("Revision", 330, 610, beim("rev", "legt"), fill=GELB, size=34),
    blase("sprech", 820, 200, "st1", 1150, 190, inhalt=["Während der wichtigsten Aussage war", "die Tür zu, ohne jeden Beschluss.",
          "Das rüge ich."], textsize=30, figur=STc, bis="frage"),
    pl("Hat die Revision Erfolg?", 1000, 160, "frage", fill=WEISS, size=34, anker="m"),
    pl("Muss er zeigen: ohne den Fehler anders?", 1000, 250, "frage2", fill=GELB, size=34, anker="m"),
])

# D Sachverhalt ----------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    glyphen("Vor der Strafkammer des Landgerichts wird gegen Herrn Lemke wegen eines Sexualdelikts verhandelt. Vor der "
            "Aussage der betroffenen Zeugin bittet der Vorsitzende den Justizwachtmeister, die Saaltür abzuschließen, damit "
            "die Zeugin in Ruhe aussagen kann. Einen Beschluss der Kammer über den Ausschluss der Öffentlichkeit gibt es "
            "nicht."),
    glyphen("Die Jurastudentin Lene will die Verhandlung verfolgen und steht vor der verschlossenen Tür. Erst nach der "
            "Aussage wird die Tür wieder geöffnet. Die Kammer verurteilt Herrn Lemke. Sein Verteidiger, Rechtsanwalt "
            "Strobel, legt Revision ein und rügt die Verletzung der Öffentlichkeit."),
], "Hat die Revision Erfolg – und muss Herr Lemke das Beruhen zeigen?")

# E 1. Einordnung: § 337 und § 338 ----------------------------------------------------------------------------------------------
PE = "1. Einordnung"
folie([("p337", f"{PE} › § 337 StPO: Beruhen"), ("p338", f"{PE} › § 338 StPO: stets beruhend"),
       ("vermut", f"{PE} › Beruhen unwiderleglich vermutet"), ("ruege", f"{PE} › trotzdem vollständige Verfahrensrüge")],
      rechts_frei([
    *tafel("p337", "1. Einordnung: § 337 und § 338 StPO"),
    z("§ 337 StPO: Das Urteil muss auf dem Fehler beruhen.", 110, 180, "p337", "Bold", 32),
    *wortlaut(110, 250, 1040, 110, "p338", [
        [("„Ein Urteil ist ", 0), ("stets", "s"), (" als auf einer Verletzung des Gesetzes", 0)],
        [("beruhend anzusehen", "b"), (", 1. wenn … 8. wenn …“", 0)],
    ], 30, {"s": beim("p338", "stets"), "b": beim("p338", "beruhend")}, "§ 338 StPO, Einleitungssatz"),
    z("Katalog: Nr. 1 bis 8", 110, 430, "katal", "Bold", 32),
    fb(110, 500, 1040, 100, GELB, "vermut", [("Das Beruhen wird unwiderleglich vermutet.", "ExtraBold", 36, INK)]),
    z("Aber: Den Fehler selbst mit vollständiger", 110, 640, "ruege", "Bold", 32),
    z("Verfahrensrüge vortragen, § 344 Abs. 2 S. 2 StPO", 110, 685, beim("ruege", "Verfahrensrüge"), "Bold", 32),
    fund("siehe Folge 72: Verfahrensrüge nach § 344 Abs. 2 S. 2 StPO", 110, 745, beim("ruege", "Wie")),
    peep_voll("ST_ruhig", X1, BR, FR, "p337", bis="vermut"),
    peep_voll("ST_froh", X1, BR, FR, "vermut", anim="cut", bis="ruege"),
    peep_voll("ST_denkt", X1, BR, FR, "ruege", anim="cut"),
    peep_voll("LM_ruhig", X2, BR, FR, "p337", d=0.2, bis="vermut"),
    peep_voll("LM_denkt", X2, BR, FR, "vermut", anim="cut"),
    namensschild("Rechtsanwalt Strobel", X1 - 70, BR, "p337", GRUEN, d=0.2),
    namensschild("Herr Lemke", X2 + 20, BR, "p337", WEISS, d=0.3),
    ficon("tabler", "scale", MB, 380, 110, "p337", fuell=GELB, bis="katal"),
    pl("§ 337: Beruhen prüfen", MB, 160, "p337", fill=WEISS, size=28, anker="m", bis="p338"),
    pl("§ 338: stets beruhend", MB, 160, "p338", fill=GELB, size=28, anker="m", anim="cut", bis="ruege"),
    ficon("tabler", "list-numbers", MB, 380, 100, "katal", fuell=WEISS, anim="cut", bis="ruege"),
    ficon("tabler", "file-text", MB, 380, 100, "ruege", fuell=GRUEN, anim="cut"),
    pl("Rüge vollständig", MB, 160, "ruege", fill=GRUEN, size=28, anker="m", anim="cut"),
]))

# F 2. Nr. 1: Besetzung ----------------------------------------------------------------------------------------------------------
PK = "2. Katalog"
folie([("kat", f"{PK} › die examensrelevanten Nummern"), ("n1", f"{PK} › Nr. 1: Besetzung"),
       ("n1b", "Nr. 1 › Mitteilung, § 222a StPO"), ("n1c", "Nr. 1 › Einwand binnen 1 Woche, § 222b Abs. 1 StPO"),
       ("n1d", "Nr. 1 › Vorabentscheidung, § 222b Abs. 3 StPO"), ("n1e", "Nr. 1 › Revision nur nach Buchst. a, b")],
      rechts_frei([
    *tafel("kat", "2. Nr. 1: Vorschriftswidrige Besetzung"),
    z("Das Gericht war nicht vorschriftsmäßig besetzt.", 110, 175, "n1", "Bold", 32),
    z("Mitteilung der Besetzung: LG und OLG im 1. Rechtszug", 110, 245, "n1b", size=30),
    fund("§ 222a Abs. 1 StPO", 150, 287, beim("n1b", "Paragraf")),
    z("Einwand binnen 1 Woche nach der Mitteilung", 110, 340, "n1c", size=30),
    fund("§ 222b Abs. 1 StPO · seit 13.12.2019", 150, 382, beim("n1c", "Paragraf")),
    z("Gericht hält ihn für unbegründet: Vorlage an das", 110, 435, "n1d", size=30),
    z("Rechtsmittelgericht, das vorab entscheidet", 110, 475, beim("n1d", "Rechtsmittelgericht"), size=30),
    fund("§ 222b Abs. 3 StPO", 150, 517, beim("n1d", "vorab")),
    fb(110, 575, 1040, 150, BLAUHELL, "n1e", [("Revision: Besetzungsrüge nur nach § 338 Nr. 1 a, b", "ExtraBold", 32, INK),
                                               ("z. B. Einwand übergangen, keine Vorabentscheidung", "Regular", 30, INK)]),
    pl("ältere Darstellungen: überholt", 110, 760, "alt", fill=ROTHELL, size=30),
    peep_voll("VR_ruhig", X2, BR, FR, "kat", d=0.2, bis="n1d"),
    peep_voll("VR_denkt", X2, BR, FR, "n1d", anim="cut", bis="n1e"),
    peep_voll("VR_streng", X2, BR, FR, "n1e", anim="cut"),
    peep_voll("ST_ruhig", X1, BR, FR, "kat", bis="n1c"),
    peep_voll("ST_denkt", X1, BR, FR, "n1c", anim="cut", bis="n1e"),
    peep_voll("ST_ernst", X1, BR, FR, "n1e", anim="cut"),
    namensschild("Rechtsanwalt Strobel", X1 - 70, BR, "kat", GRUEN, d=0.2),
    namensschild("Vorsitzender Richter", X2 - 30, BR, "kat", WEISS, d=0.3),
    pl("5 Nummern im Examen", MB, 160, "kat", fill=GELB, size=28, anker="m", bis="n1"),
    ficon("tabler", "list-numbers", MB, 380, 100, "kat", fuell=WEISS, bis="n1b"),
    pl("Nr. 1: Besetzung", MB, 160, "n1", fill=WEISS, size=28, anker="m", anim="cut", bis="n1c"),
    ficon("tabler", "list-check", MB, 380, 100, "n1b", fuell=WEISS, anim="cut", bis="n1c"),
    ficon("tabler", "calendar-time", MB, 380, 100, "n1c", fuell=GELB, anim="cut", bis="n1d"),
    pl("1 Woche", MB, 160, "n1c", fill=GELB, size=30, anker="m", anim="cut", bis="n1d"),
    ficon("tabler", "building-bank", MB, 380, 110, "n1d", fuell=BLAU, anim="cut", bis="n1e"),
    pl("Vorabentscheidung", MB, 160, "n1d", fill=BLAU, size=28, anker="m", anim="cut", bis="n1e"),
    ficon("tabler", "file-x", MB, 380, 100, "n1e", fuell=ROT, anim="cut"),
    pl("Revision: nur a, b", MB, 160, "n1e", fill=ROTHELL, size=28, anker="m", anim="cut"),
]))

# G 2. Der Katalog als Tabelle ------------------------------------------------------------------------------------------------
C1, C2, C3 = 115, 185, 800             # Spalten: Nr. · Fehler · Normen
folie([("n5", f"{PK} › Nr. 5: Abwesenheit"), ("n6", f"{PK} › Nr. 6: Öffentlichkeit"), ("n7", f"{PK} › Nr. 7: Urteilsgründe"),
       ("n8", f"{PK} › Nr. 8: Verteidigung")], rechts_frei([
    *tafel("n5", "2. Der Katalog des § 338 StPO"),
    z("Nr.", C1, 170, "n5", "ExtraBold", 28, farbe=TEXT),
    z("Fehler", C2, 170, "n5", "ExtraBold", 28, farbe=TEXT),
    z("Normen", C3, 170, "n5", "ExtraBold", 28, farbe=TEXT),
    hart(linienzug([(110, 212), (1150, 212)], "n5", breite=4, farbe=INK)),
    z("1", C1, 225, "n5", "ExtraBold", 30, farbe=TEXT),
    z("Besetzung (siehe oben)", C2, 225, "n5", size=30, farbe=TEXT),
    z("§§ 222a, 222b StPO", C3, 225, "n5", size=30, farbe=TEXT),
    z("5", C1, 285, "n5", "ExtraBold", 32),
    z("Abwesenheit vorgeschriebener Personen", C2, 285, "n5", "Bold", 30),
    z("· Staatsanwalt", C2 + 20, 327, "n5b", size=30), z("§ 226 StPO", C3, 327, "n5b", size=30),
    z("· Angeklagter", C2 + 20, 367, "n5c", size=30), z("§ 230 StPO", C3, 367, "n5c", size=30),
    z("· notwendiger Verteidiger", C2 + 20, 407, "n5d", size=30), z("§ 140 StPO", C3, 407, "n5d", size=30),
    fund("nur bei einem wesentlichen Teil der Verhandlung", C2 + 20, 450, "n5e", rechts=1150),
    z("6", C1, 505, "n6", "ExtraBold", 32),
    z("Öffentlichkeit verletzt", C2, 505, "n6", "Bold", 30), z("§§ 169 ff. GVG", C3, 505, "n6", size=30),
    z("· Ausschluss nur durch Beschluss", C2 + 20, 547, "n6b", size=30), z("§ 174 GVG", C3, 547, "n6b", size=30),
    z("7", C1, 610, "n7", "ExtraBold", 32),
    z("Urteilsgründe fehlen oder zu spät", C2, 610, "n7", "Bold", 30), z("§ 275 StPO", C3, 610, "n7", size=30),
    z("8", C1, 675, "n8", "ExtraBold", 32),
    z("Verteidigung durch Beschluss", C2, 675, "n8", "Bold", 30),
    z("unzulässig beschränkt", C2, 715, beim("n8", "unzulässig"), "Bold", 30),
    z("§ 338 Nr. 8 StPO", C3, 675, "n8", size=30),
    peep_voll("ST_ruhig", X1, BR, FR, "n5", bis="n6"),
    peep_voll("ST_denkt", X1, BR, FR, "n6", anim="cut", bis="n8"),
    peep_voll("ST_ernst", X1, BR, FR, "n8", anim="cut"),
    peep_voll("LM_ruhig", X2, BR, FR, "n5", d=0.2, bis="n6"),
    peep_voll("LM_sorge", X2, BR, FR, "n6", anim="cut", bis="n7"),
    peep_voll("LM_denkt", X2, BR, FR, "n7", anim="cut"),
    namensschild("Rechtsanwalt Strobel", X1 - 70, BR, "n5", GRUEN, d=0.2),
    namensschild("Herr Lemke", X2 + 20, BR, "n5", WEISS, d=0.3),
    ficon("tabler", "armchair", MB, 380, 110, "n5", fuell=WEISS, bis="n6"),
    pl("leerer Platz", MB, 160, "n5", fill=WEISS, size=28, anker="m", bis="n5e"),
    pl("wesentlicher Teil", MB, 160, "n5e", fill=GELB, size=28, anker="m", anim="cut", bis="n6"),
    ficon("tabler", "lock", MB, 380, 90, "n6", fuell=ROT, anim="cut", bis="n7"),
    pl("Öffentlichkeit", MB, 160, "n6", fill=WEISS, size=28, anker="m", anim="cut", bis="n7"),
    ficon("tabler", "file-x", MB, 380, 100, "n7", fuell=ROT, anim="cut", bis="n8"),
    pl("Urteilsgründe", MB, 160, "n7", fill=WEISS, size=28, anker="m", anim="cut", bis="n8"),
    ficon("tabler", "hand-stop", MB, 380, 100, "n8", fuell=WEISS, anim="cut"),
    pl("Verteidigung", MB, 160, "n8", fill=LILA, size=28, anker="m", anim="cut"),
]))

# H1 3. Nr. 8: Wortlaut und BGH -------------------------------------------------------------------------------------------------
P8 = "3. Nr. 8"
folie([("w8", f"{P8} › der Wortlaut"), ("bgh8", f"{P8} › nicht nur abstrakt geeignet"),
       ("konkr", f"{P8} › konkreter Zusammenhang mit dem Urteil")], rechts_frei([
    *tafel("w8", "3. Nr. 8: nur eingeschränkt absolut"),
    *wortlaut(110, 170, 1040, 160, "w8", [
        [("„8. wenn die Verteidigung in einem ", 0), ("für die Entscheidung", "w")],
        [("wesentlichen Punkt", "w2"), (" durch einen Beschluß des Gerichts", 0)],
        [("unzulässig beschränkt worden ist.“", 0)],
    ], 30, {"w": beim("w8b", "für"), "w2": beim("w8b", "für")}, "§ 338 Nr. 8 StPO"),
    nein(150, 435, beim("bgh8", "abstrakt"), gr=20),
    z("Nicht genug: Beschränkung nur abstrakt geeignet,", 185, 415, beim("bgh8", "Es"), size=30),
    z("das Urteil zu beeinflussen", 185, 455, beim("bgh8", "abstrakt"), size=30),
    *wortlaut(110, 530, 1040, 160, "konkr", [
        [("„… nur dann gegeben, wenn die Möglichkeit eines", 0)],
        [("kausalen Zusammenhangs zwischen dem Verfahrens-", 0)],
        [("verstoß und dem Urteil ", 0), ("konkret besteht", "k"), (".“", 0)],
    ], 30, {"k": beim("konkr", "konkret")}, "BGH, Beschl. v. 23.6.2026 – 5 StR 52/26, Rn. 8"),
    peep_voll("ST_ruhig", X1, BR, FR, "w8", bis="bgh8"),
    peep_voll("ST_denkt", X1, BR, FR, "bgh8", anim="cut"),
    peep_voll("VR_ruhig", X2, BR, FR, "w8", d=0.2, bis="konkr"),
    peep_voll("VR_streng", X2, BR, FR, "konkr", anim="cut"),
    namensschild("Rechtsanwalt Strobel", X1 - 70, BR, "w8", GRUEN, d=0.2),
    namensschild("Vorsitzender Richter", X2 - 30, BR, "w8", WEISS, d=0.3),
    ficon("tabler", "hand-stop", MB, 380, 100, "w8", fuell=WEISS, bis="bgh8"),
    pl("wesentlicher Punkt", MB, 160, beim("w8b", "wesentlichen"), fill=GELB, size=28, anker="m", bis="bgh8"),
    ficon("tabler", "link", MB, 380, 100, "bgh8", fuell=WEISS, anim="cut"),
    pl("nur abstrakt? reicht nicht", MB, 160, beim("bgh8", "abstrakt"), fill=ROTHELL, size=28, anker="m", bis="konkr"),
    pl("konkret!", MB, 160, beim("konkr", "konkret"), fill=GRUEN, size=30, anker="m"),
]))

# H2 3. Nr. 8: Beispiel und Folge ---------------------------------------------------------------------------------------------
folie([("bsp8", f"{P8} › Beispiel: Beiziehung von Akten"), ("halb", f"{P8} › nur eingeschränkt absolut"),
       ("beschl8", f"{P8} › Gerichtsbeschluss mitteilen")], rechts_frei([
    *tafel("bsp8", "3. Nr. 8: Was die Rüge zeigen muss"),
    z("Beispiel: Gericht lehnt die Beiziehung von Akten ab", 110, 175, "bsp8", "Bold", 32),
    z("Die Rüge muss darlegen:", 110, 245, beim("bsp8", "muss"), size=30),
    z("· welche Tatsachen sich aus welchen Aktenstellen", 150, 290, beim("bsp8", "welche"), size=30),
    z("  ergeben hätten", 150, 330, beim("bsp8", "welche"), size=30),
    z("· was daraus für die Verteidigung folgte", 150, 375, beim("bsp8", "was"), size=30),
    fund("vgl. BGH 5 StR 52/26, Rn. 8", 150, 420, beim("bsp8", "was")),
    fb(110, 480, 1040, 100, LILA, "halb", [("Nr. 8 ist nur eingeschränkt absolut.", "ExtraBold", 36, INK)]),
    z("Und: den Gerichtsbeschluss mitteilen", 110, 625, "beschl8", "Bold", 32),
    fund("vgl. BGH, Beschl. v. 30.8.2022 – 5 StR 169/22, Rn. 9", 150, 672, beim("beschl8", "Gerichtsbeschluss")),
    peep_voll("ST_denkt", X1, BR, FR, "bsp8", bis="halb"),
    peep_voll("ST_ruhig", X1, BR, FR, "halb", anim="cut"),
    peep_voll("VR_ruhig", X2, BR, FR, "bsp8", d=0.2, bis="beschl8"),
    peep_voll("VR_streng", X2, BR, FR, "beschl8", anim="cut"),
    namensschild("Rechtsanwalt Strobel", X1 - 70, BR, "bsp8", GRUEN, d=0.2),
    namensschild("Vorsitzender Richter", X2 - 30, BR, "bsp8", WEISS, d=0.3),
    ficon("tabler", "folders", MB, 380, 100, "bsp8", fuell=WEISS, bis="halb"),
    pl("Akten abgelehnt", MB, 160, "bsp8", fill=WEISS, size=28, anker="m", bis="halb"),
    ficon("tabler", "scale", MB, 380, 110, "halb", fuell=LILA, anim="cut", bis="beschl8"),
    pl("eingeschränkt absolut", MB, 160, "halb", fill=LILA, size=28, anker="m", anim="cut", bis="beschl8"),
    ficon("tabler", "file-text", MB, 380, 100, "beschl8", fuell=GELB, anim="cut"),
    pl("Beschluss mitteilen", MB, 160, "beschl8", fill=GELB, size=28, anker="m", anim="cut"),
]))

# I 4. Der Fall: Nr. 6 ---------------------------------------------------------------------------------------------------------
P6 = "4. Fall › Nr. 6"
folie([("fall2", "4. Fall › § 338 Nr. 6 StPO"), ("p169", f"{P6} › § 169 Abs. 1 S. 1 GVG"),
       ("p171", f"{P6} › Ausschluss nach § 171b GVG möglich"), ("nurb", f"{P6} › nur durch Gerichtsbeschluss")],
      rechts_frei([
    *tafel("fall2", "4. Der Fall: § 338 Nr. 6 StPO"),
    *wortlaut(110, 165, 1040, 160, "fall2", [
        [("„6. wenn das Urteil auf Grund einer mündlichen", 0)],
        [("Verhandlung ergangen ist, bei der die Vorschriften über", 0)],
        [("die ", 0), ("Öffentlichkeit", "o"), (" des Verfahrens verletzt sind;“", 0)],
    ], 30, {"o": beim("fall2", "sechs")}, "§ 338 Nr. 6 StPO"),
    *wortlaut(110, 385, 1040, 110, "p169", [
        [("„Die Verhandlung vor dem erkennenden Gericht einschließlich der", 0)],
        [("Verkündung der Urteile und Beschlüsse ist ", 0), ("öffentlich", "f"), (".“", 0)],
    ], 30, {"f": beim("p169", "öffentlich")}, "§ 169 Abs. 1 S. 1 GVG"),
    z("Ausschluss für die Aussage: § 171b GVG kam in Betracht", 110, 560, "p171", size=30),
    z("Aber: stets ein Beschluss des Gerichts nötig,", 110, 620, "nurb", "Bold", 32),
    z("§ 174 Abs. 1 S. 2 GVG", 150, 665, beim("nurb", "Beschluss"), size=30),
    nein(150, 745, beim("nurb", "nicht"), gr=20),
    z("Anordnung des Vorsitzenden ersetzt ihn nicht", 185, 725, beim("nurb", "Anordnung"), size=30),
    fund("BGH, Urt. v. 28.2.2024 – 5 StR 413/23, Rn. 7", 185, 770, beim("nurb", "nicht")),
    peep_voll("ST_ruhig", X1, BR, FR, "fall2", bis="nurb"),
    peep_voll("ST_froh", X1, BR, FR, "nurb", anim="cut"),
    peep_voll("VR_ruhig", X2, BR, FR, "fall2", d=0.2, bis="p171"),
    peep_voll("VR_denkt", X2, BR, FR, "p171", anim="cut", bis="nurb"),
    peep_voll("VR_streng", X2, BR, FR, "nurb", anim="cut"),
    namensschild("Rechtsanwalt Strobel", X1 - 70, BR, "fall2", GRUEN, d=0.2),
    namensschild("Vorsitzender Richter", X2 - 30, BR, "fall2", WEISS, d=0.3),
    ficon("tabler", "door", MB, 400, 130, "fall2", fuell=HOLZ, bis="nurb"),
    pl("Saal 2", MB, 160, "fall2", fill=WEISS, size=28, anker="m", bis="p169"),
    pl("öffentlich", MB, 160, beim("p169", "öffentlich"), fill=GELB, size=28, anker="m", bis="p171"),
    pl("§ 171b GVG möglich", MB, 160, "p171", fill=WEISS, size=28, anker="m", anim="cut", bis="nurb"),
    ficon("tabler", "file-x", MB, 380, 100, "nurb", fuell=ROT, anim="cut"),
    pl("kein Beschluss", MB, 160, "nurb", fill=ROTHELL, size=28, anker="m", anim="cut"),
]))

# J Zurechnung und Ausnahmen -------------------------------------------------------------------------------------------------
folie([("zurech", f"{P6} › dem Gericht zurechenbar"), ("versehen", f"{P6} › Gegenfall: ohne Wissen des Gerichts"),
       ("einer", f"{P6} › 1 Zuschauer genügt"), ("ausn", f"{P6} › Ausnahmen nur eng"), ("nr6", f"{P6} › liegt vor")],
      rechts_frei([
    *tafel("zurech", "Nr. 6: Zurechnung und Ausnahmen"),
    ok(140, 195, "zurech", gr=18),
    z("Der Vorsitzende ordnete das Abschließen selbst an.", 175, 175, "zurech", "Bold", 30),
    z("Gegenfall: ohne Wissen des Gerichts verschlossen,", 175, 235, "versehen", size=30),
    z("bei ordnungsgemäßer Sorgfalt nicht erkennbar", 175, 275, beim("versehen", "ordnungsgemäßer"), size=30),
    fund("vgl. BGH, Beschl. v. 21.6.2023 – 5 StR 73/23, Rn. 6", 175, 318, beim("versehen", "ordnungsgemäßer")),
    ok(140, 385, beim("einer", "Schon"), gr=18),
    z("Schon 1 ausgesperrter Zuschauer genügt.", 175, 365, beim("einer", "Schon"), "Bold", 30),
    fund("vgl. BGH, Beschl. v. 2.12.2025 – 5 StR 388/25, Rn. 9", 175, 408, beim("einer", "Schon")),
    z("Ausnahmen nur eng: Beschluss da, nur Begründung", 175, 470, "ausn", size=30),
    z("fehlt, Grund für alle offensichtlich", 175, 510, beim("ausn", "Begründung"), size=30),
    fund("vgl. BGH 5 StR 413/23, Rn. 10 f.", 175, 553, beim("ausn", "Begründung")),
    nein(140, 625, "hier", gr=18),
    z("Hier fehlt der Beschluss ganz.", 175, 605, "hier", "Bold", 30),
    fb(110, 670, 1040, 100, GRUEN, "nr6", [("§ 338 Nr. 6 StPO liegt vor.", "ExtraBold", 36, INK)]),
    z("Beruhen: wird nicht geprüft", 110, 800, "kein337", "Bold", 30),
    peep_voll("LE_denkt", X1, BR, FR, "zurech", bis="einer"),
    peep_voll("LE_froh", X1, BR, FR, "einer", anim="cut"),
    peep_voll("VR_streng", X2, BR, FR, "zurech", d=0.2, bis="versehen"),
    peep_voll("VR_denkt", X2, BR, FR, "versehen", anim="cut", bis="nr6"),
    peep_voll("VR_ruhig", X2, BR, FR, "nr6", anim="cut"),
    namensschild("Lene, Jurastudentin", X1 - 70, BR, "zurech", LILA, d=0.2),
    namensschild("Vorsitzender Richter", X2 - 30, BR, "zurech", WEISS, d=0.3),
    ficon("tabler", "lock", MB, 380, 90, "zurech", fuell=ROT, bis="einer"),
    pl("Anordnung des Vorsitzenden", MB, 160, "zurech", fill=WEISS, size=28, anker="m", bis="versehen"),
    pl("Gegenfall: ohne Wissen", MB, 160, "versehen", fill=BLAUHELL, size=28, anker="m", anim="cut", bis="einer"),
    ficon("tabler", "door", MB, 400, 130, "einer", fuell=HOLZ, anim="cut", bis="ausn"),
    pl("1 Zuschauer genügt", MB, 160, beim("einer", "Schon"), fill=GELB, size=28, anker="m", bis="ausn"),
    ficon("tabler", "help-circle", MB, 380, 100, "ausn", fuell=WEISS, anim="cut", bis="nr6"),
    pl("Ausnahmen eng", MB, 160, "ausn", fill=WEISS, size=28, anker="m", anim="cut", bis="nr6"),
    ficon("tabler", "circle-check", MB, 380, 100, "nr6", fuell=GRUEN, anim="cut"),
    pl("Nr. 6 liegt vor", MB, 160, "nr6", fill=GRUEN, size=28, anker="m", anim="cut"),
]))

# K Ergebnis ------------------------------------------------------------------------------------------------------------------
PR = "Ergebnis"
folie([("erg", f"{PR} › Revision begründet"), ("aufh", f"{PR} › Aufhebung, § 353 StPO"),
       ("zur", f"{PR} › Zurückverweisung, § 354 Abs. 2 StPO")], rechts_frei([
    *tafel("erg", "Ergebnis im Fall"),
    fb(110, 175, 1040, 100, GRUEN, "erg", [("Die Revision hat Erfolg.", "ExtraBold", 38, INK)]),
    z("Urteil mit den Feststellungen aufgehoben,", 110, 330, "aufh", "Bold", 32),
    z("§ 353 StPO", 150, 375, beim("aufh", "Paragraf"), size=30),
    z("Sache an eine andere Strafkammer zurückverwiesen,", 110, 450, "zur", "Bold", 32),
    z("§ 354 Abs. 2 StPO", 150, 495, beim("zur", "Paragraf"), size=30),
    fund("so im Ergebnis BGH, Urt. v. 28.2.2024 – 5 StR 413/23 (Tenor)", 110, 570, beim("zur", "Paragraf")),
    peep_voll("ST_froh", X1, BR, FR, "erg", bis="zur"),
    peep_voll("ST_ruhig", X1, BR, FR, "zur", anim="cut"),
    peep_voll("LM_sorge", X2, BR, FR, "erg", d=0.2, bis=beim("erg", "Erfolg")),
    peep_voll("LM_ruhig", X2, BR, FR, beim("erg", "Erfolg"), anim="cut", bis="zur"),
    peep_voll("LM_denkt", X2, BR, FR, "zur", anim="cut"),
    namensschild("Rechtsanwalt Strobel", X1 - 70, BR, "erg", GRUEN, d=0.2),
    namensschild("Herr Lemke", X2 + 20, BR, "erg", WEISS, d=0.3),
    ficon("tabler", "circle-check", MB, 380, 100, "erg", fuell=GRUEN, bis="aufh"),
    pl("Erfolg", MB, 160, beim("erg", "Erfolg"), fill=GRUEN, size=30, anker="m", bis="aufh"),
    ficon("tabler", "file-x", MB, 380, 100, "aufh", fuell=ROT, anim="cut", bis="zur"),
    pl("aufgehoben", MB, 160, "aufh", fill=ROTHELL, size=30, anker="m", anim="cut", bis="zur"),
    ficon("tabler", "building-bank", MB, 380, 110, "zur", fuell=BLAU, anim="cut"),
    pl("neue Verhandlung", MB, 160, "zur", fill=BLAU, size=28, anker="m", anim="cut"),
]))

# L Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · Gab es einen Beschluss?"), ("tipp2", "Klausurtipp · § 171b GVG im Einzelfall: nicht geprüft"),
       ("tipp3", "Klausurtipp · Nr. 6 nur bei zu wenig Öffentlichkeit")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Bei Nr. 6 zuerst fragen:", 200, 200, beim("tipp", "Frag"), "Bold", 36),
    z("Gab es überhaupt einen Beschluss?", 200, 250, beim("tipp", "ob"), "Bold", 36),
    z("Ob § 171b GVG im Einzelfall vorlag,", 200, 345, "tipp2", size=34),
    z("prüft das Revisionsgericht nicht.", 200, 393, beim("tipp2", "prüft"), size=34),
    fund("§ 171b Abs. 5 GVG, § 336 S. 2 StPO", 200, 445, beim("tipp2", "prüft")),
    fund("BGH, Beschl. v. 27.1.2026 – 2 StR 644/25, Rn. 12", 200, 478, beim("tipp2", "prüft")),
    z("Nr. 6 gilt nur für zu wenig Öffentlichkeit.", 200, 550, "tipp3", "Bold", 34),
    z("Zu viel Öffentlichkeit: Beruhen nötig, § 337 StPO", 200, 600, beim("tipp3", "Bei"), "Bold", 32),
    fund("vgl. BGH 2 StR 644/25, Rn. 8", 200, 650, beim("tipp3", "Bei")),
    *redet("LX_warnt", LXX, BR, FR + 60, "tipp", "sch"),
    namensschild("Lexi", LXX, BR, "tipp", GELB, d=0.2),
])

# M Schema ------------------------------------------------------------------------------------------------------------------------
K1, K2 = 150, 210
folie([("sch", "Schema"), ("s1", "Schema › I. Nummer des § 338 StPO"), ("s2", "Schema › II. Verstoß"),
       ("s3", "Schema › III. bei Nr. 8: konkreter Zusammenhang"), ("s4", "Schema › IV. vollständiger Rügevortrag"),
       ("s5", "Schema › Folge: Beruhen vermutet")], [
    karte(60, 50, 1800, 900, "sch"),
    titel("Schema: absolute Revisionsgründe", 110, 90, "sch", 54),
    z("I. Welche Nummer des § 338 StPO ist betroffen?", K1, 195, "s1", "Bold", 38, rechts=1820),
    z("II. Liegt der Verstoß vor?", K1, 285, "s2", "Bold", 38, rechts=1820),
    z("Nr. 1: Einwand und Vorabverfahren, §§ 222a, 222b StPO", K2, 340, beim("s2", "Bei"), size=32, farbe=TEXT,
      rechts=1820),
    z("Nr. 6: Verstoß dem Gericht zurechenbar", K2, 385, beim("s2", "sechs"), size=32, farbe=TEXT, rechts=1820),
    z("III. Bei Nr. 8: Beschluss – wesentlicher Punkt – konkreter Zusammenhang zum Urteil", K1, 470, "s3", "Bold", 36,
      rechts=1820),
    z("IV. Vollständiger Rügevortrag, § 344 Abs. 2 S. 2 StPO", K1, 560, "s4", "Bold", 38, rechts=1820),
    fb(150, 680, 1620, 110, GELB, "s5", [("Folge: Beruhen vermutet – Aufhebung, §§ 353, 354 StPO", "ExtraBold", 38, INK)]),
])

# N Merksatz (Lexi) ------------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Bei § 338 StPO trägst du", 0)], [("den ", 0), ("Fehler", "a"), (" vor, nicht das Beruhen.", 0)]],
                750, 310, 50, "merke", {"a": beim("merke", "Fehler")}),
    *markertext([[("Nur Nr. 8 verlangt einen", 0)], [("konkreten Bezug", "b"), (" zum Urteil.", 0)]], 750, 560, 54, "mz",
                {"b": beim("mz", "konkreten")}),
    *redet("LX_erklaert", 1680, 960, 690, "merke", lexi_bis_ende("merke")),
    namensschild("Lexi", 1680, 960, "merke", GELB, d=0.2),
])
