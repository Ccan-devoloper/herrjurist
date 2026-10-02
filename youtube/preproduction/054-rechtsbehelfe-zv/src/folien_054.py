"""Folge 054 · Rechtsbehelfe Zwangsvollstreckung: §§ 766, 767, 771, 805 ZPO – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A In der Autowerkstatt (Reparatur, Urteil, Zahlung, Vollstreckungsauftrag), B In der
Wohnung (Pfändung des geliehenen Fernsehers, Frage), C Sachverhalt, D Leitfrage „Wer wehrt sich wogegen?“, E Erinnerung
(Wortlautkarte § 766 I 1 ZPO), F sofortige Beschwerde (Wortlautkarte § 793 ZPO), G Vollstreckungsabwehrklage
(Wortlautkarte § 767 I ZPO, Präklusion § 767 II), H kurz: Klauselgegenklage § 768, I Drittwiderspruchsklage (Wortlautkarte
§ 771 I ZPO), J kurz: Vorzugsklage § 805, K Klausurtipp (Lexi), L Klausurschema, M Merksatz (Lexi).
Geräusche nur bei sichtbarer Handlung: Ratsche in der Werkstatt (Szene A), Klebesiegel am Fernseher (Szene B);
Freesound CC0."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont

bausteine.FIGORDNER = "op_054/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
LILAHELL = (246, 243, 255, 255)
ROTHELL = (253, 232, 228, 255)
GRAU = (205, 205, 210, 255)
HOLZ = (214, 160, 110, 255)
WAND = (232, 238, 250, 255)
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
    """Wortlautkarte: wörtliches Zitat (gesetze-im-internet.de, Abruf 02.10.2026) in einer hellen Karte, Fundstelle
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


def hart(e):
    e.anim = "cut"
    return e


# --- Eigene Hilfsfunktion (wie Folge 012/024/048): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt -----------
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

# A Fall: in der Autowerkstatt -------------------------------------------------------------------------------------------
HX, SX = 340, 1580
HOa = ("HO_redet_r", HX, BODEN, FH)
folie([(NULL, "Fall · Die Reparatur"), ("urteil", "Fall · Das Urteil"), ("ueberw", "Fall · Die Zahlung"),
       ("auftr", "Fall · Der Vollstreckungsauftrag")], [
    linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK),
    pl("Autowerkstatt Hollmann", 70, 40, NULL, fill=GELB, size=40),
    ficon("tabler", "car", 960, BODEN - 2, 380, NULL, fuell=ROT),
    # die Ratsche dreht an der Radmutter (Handlungsgeräusch)
    szene(bewegt(ficon("tabler", "tool", 760, 760, 90, beim("rep", "repariert"), fuell=WEISS, bis="zahlt"),
                 beim("rep", "repariert"), beim("rep", "Auto", ende=True), 0, -40), "054ratsche*", 0.9, -0.05),
    peep_voll("HO_ruhig_r", HX, BODEN, FH, NULL, bis="zahlt"),
    peep_voll("HO_streng_r", HX, BODEN, FH, "zahlt", anim="cut", bis="urteil"),
    peep_voll("HO_froh_r", HX, BODEN, FH, beim("urteil", "rechtskräftig"), anim="cut", bis="auftr"),
    peep_voll("HO_ruhig_r", HX, BODEN, FH, "urteil", anim="cut", bis=beim("urteil", "rechtskräftig")),
    peep_voll("HO_streng_r", HX, BODEN, FH, "auftr", anim="cut", bis="h1"),
    *redet("HO_redet_r", HX, BODEN, FH, "h1", "wohn"),
    namensschild("Frau Hollmann", HX, BODEN, NULL, GRUEN),
    peep_voll("ST_ruhig", SX, BODEN, FH, beim("rep", "Herrn"), anim="fade", bis="zahlt"),
    peep_voll("ST_denkt", SX, BODEN, FH, "zahlt", anim="cut", bis="urteil"),
    peep_voll("ST_sorge", SX, BODEN, FH, "urteil", anim="cut", bis="ueberw"),
    peep_voll("ST_froh", SX, BODEN, FH, "ueberw", anim="cut", bis="auftr"),
    namensschild("Herr Steinbach", SX, BODEN, beim("rep", "Herrn"), BLAU, bis="auftr"),
    pl("Reparatur: 2.400 €", 960, 170, beim("rep", "zweitausendvierhundert"), fill=GELB, size=36, anker="m", bis="urteil"),
    ficon("tabler", "cash-off", 960, 500, 100, beim("zahlt", "zahlt"), fuell=ROT, bis="urteil"),
    pl("zahlt nicht", 960, 280, beim("zahlt", "zahlt"), fill=WEISS, size=32, anker="m", bis="urteil"),
    # Klage und Urteil
    ficon("tabler", "building-bank", 960, 520, 130, beim("urteil", "Amtsgericht"), fuell=BLAU, anim="cut", bis="ueberw"),
    pl("Amtsgericht", 960, 150, beim("urteil", "Amtsgericht"), fill=BLAU, size=32, anker="m", bis="ueberw"),
    pl("Urteil: Steinbach zahlt 2.400 €", 960, 225, beim("urteil", "verurteilt"), fill=WEISS, size=30, anker="m", bis="ueberw"),
    pl("rechtskräftig", 960, 300, beim("urteil", "rechtskräftig"), fill=GRUEN, size=30, anker="m", bis="ueberw"),
    # die Überweisung wandert von Herrn Steinbach zu Frau Hollmann
    bewegt(ficon("tabler", "cash-banknote", 600, 560, 110, beim("ueberw", "überweist"), fuell=GRUEN, bis="h1"),
           beim("ueberw", "überweist"), beim("ueberw", "Betrag", ende=True), SX - 160 - 600, 0),
    pl("einen Monat nach dem Urteil", 960, 150, beim("ueberw", "Monat"), fill=WEISS, size=30, anker="m", bis="h1"),
    pl("überwiesen: 2.400 €", 960, 225, beim("ueberw", "überweist"), fill=GRUEN, size=32, anker="m", bis="h1"),
    # trotzdem: Auftrag an den Gerichtsvollzieher
    peep_voll("GV_ruhig", SX, BODEN, FH, beim("auftr", "Gerichtsvollzieher"), anim="fade"),
    namensschild("Gerichtsvollzieher", SX, BODEN, beim("auftr", "Gerichtsvollzieher"), TUERKIS),
    pl("Trotzdem: Vollstreckungsauftrag", 960, 300, beim("auftr", "beauftragt"), fill=PINK, size=30, anker="m"),
    blase("sprech", 600, 190, "h1", 820, 160, inhalt=["Bitte pfänden Sie bei", "Herrn Steinbach."], textsize=34,
          figur=HOa, bis="wohn"),
])

# B Fall: in der Wohnung von Herrn Steinbach ----------------------------------------------------------------------------
SX, WX, GX = 270, 640, 1600
TVX = 1060
STb = ("ST_redet_r", SX, BODEN, FH)
WEb = ("WE_redet_r", WX, BODEN, FH)
GVb = ("GV_redet", GX, BODEN, FH)
folie([("wohn", "Fall · Die Pfändung"), ("frage", "Fall · Die Frage")], [
    hart(linienzug([(60, BODEN), (1860, BODEN)], "wohn", breite=7, farbe=INK)),
    pl("Wohnung von Herrn Steinbach", 70, 40, "wohn", fill=BLAU, size=40, anim="cut"),
    hart(karte(880, 700, 360, BODEN - 700, "wohn", fill=HOLZ, rund=10, schatten=4)),      # Sideboard
    ficon("tabler", "device-tv", TVX, 702, 280, beim("wohn", "zweiter"), fuell=DUNKEL),
    pl("zweiter Fernseher", TVX, 360, beim("wohn", "zweiter"), fill=WEISS, size=28, anker="m", bis="g1"),
    hart(karte(1290, 790, 140, BODEN - 790, "wohn", fill=HOLZ, rund=8, schatten=3)),     # kleines Tischchen
    ficon("tabler", "device-tv-old", 1360, 792, 110, beim("wohn", "alten"), fuell=GRAU),
    pl("altes Gerät", 1360, 620, beim("wohn", "alten"), fill=WEISS, size=28, anker="m", bis="g1"),
    peep_voll("ST_ruhig_r", SX, BODEN, FH, "wohn", anim="cut", bis="st1"),
    *redet("ST_redet_r", SX, BODEN, FH, "st1", "w1"),
    peep_voll("ST_ruhig_r", SX, BODEN, FH, "w1", anim="cut", bis="frage"),
    peep_voll("ST_sorge_r", SX, BODEN, FH, "frage", anim="cut"),
    namensschild("Herr Steinbach", SX, BODEN, "wohn", BLAU, anim="cut"),
    peep_voll("WE_ruhig_r", WX, BODEN, FH, beim("schw", "Schwester"), anim="fade", bis="w1"),
    *redet("WE_redet_r", WX, BODEN, FH, "w1", "g2"),
    peep_voll("WE_ruhig_r", WX, BODEN, FH, "g2", anim="cut", bis="frage"),
    peep_voll("WE_sorge_r", WX, BODEN, FH, "frage", anim="cut"),
    namensschild("Frau Weidner", WX, BODEN, beim("schw", "Schwester"), LILA),
    pl("geliehen von der Schwester", TVX, 290, beim("schw", "geliehen"), fill=LILA, size=28, anker="m", bis="g1"),
    peep_voll("GV_ruhig", GX, BODEN, FH, "wohn", anim="cut", bis="g1"),
    *redet("GV_redet", GX, BODEN, FH, "g1", "st1"),
    peep_voll("GV_ruhig", GX, BODEN, FH, "st1", anim="cut", bis="g2"),
    *redet("GV_redet", GX, BODEN, FH, "g2", "frage"),
    peep_voll("GV_denkt", GX, BODEN, FH, "frage", anim="cut"),
    namensschild("Gerichtsvollzieher", GX, BODEN, "wohn", TUERKIS, anim="cut"),
    # das Klebesiegel kommt auf den Fernseher (Handlungsgeräusch)
    szene(bewegt(ficon("tabler", "sticker", TVX + 75, 615, 70, beim("g1", "Siegel"), fuell=ROT),
                 beim("g1", "Siegel"), beim("g1", "Siegel", ende=True), 120, -60), "054siegel*", 0.9, 0.1),
    pl("gepfändet", TVX, 360, beim("g1", "pfände"), fill=ROT, size=30, anker="m"),
    blase("sprech", 640, 190, "g1", 1420, 200, inhalt=["Diesen Fernseher pfände ich.", "Hier ist das Siegel."],
          textsize=34, figur=GVb, bis="st1"),
    blase("sprech", 600, 180, "st1", 560, 200, inhalt=["Aber ich habe doch", "längst bezahlt!"], textsize=36,
          figur=STb, bis="w1"),
    blase("sprech", 560, 180, "w1", 820, 200, inhalt=["Und der Fernseher", "gehört mir!"], textsize=36,
          figur=WEb, bis="g2"),
    blase("sprech", 640, 190, "g2", 1420, 200, inhalt=["Er steht in Ihrer Wohnung.", "Das genügt für die Pfändung."],
          textsize=32, figur=GVb, bis="frage"),
    pl("Wer kann sich jetzt wogegen wehren?", 960, 150, "frage", fill=PINK, size=40, anker="m"),
    pl("Und mit welchem Rechtsbehelf?", 960, 235, "frage2", fill=WEISS, size=34, anker="m"),
])

# C Sachverhalt ----------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    glyphen("Frau Hollmann repariert in ihrer Autowerkstatt das Auto von Herrn Steinbach für 2.400 Euro. Er zahlt nicht. "
            "Das Amtsgericht verurteilt ihn zur Zahlung; das Urteil wird rechtskräftig. Einen Monat nach dem Urteil "
            "überweist Herr Steinbach die 2.400 Euro an Frau Hollmann."),
    glyphen("Trotzdem beauftragt Frau Hollmann den Gerichtsvollzieher. Er pfändet in der Wohnung von Herrn Steinbach "
            "einen großen Fernseher, den ihm seine Schwester, Frau Weidner, geliehen hat. Daneben steht sein eigenes "
            "altes Gerät."),
    glyphen("Annahme: Titel, Klausel und Zustellung liegen vor; Pfändungsverbote greifen nicht."),
], "Wer kann sich wogegen wehren – und womit?")

# D Leitfrage: Wer wehrt sich wogegen? ---------------------------------------------------------------------------------------
PL = "Leitfrage"
folie([("ueber", f"{PL} · Wer wehrt sich wogegen?"), ("l766", f"{PL} › Art und Weise: § 766 ZPO"),
       ("l767", f"{PL} › titulierter Anspruch: § 767 ZPO"), ("l771", f"{PL} › Recht eines Dritten: §§ 771, 805 ZPO")],
      rechts_frei([
    *tafel("ueber", "Wer wehrt sich wogegen?"),
    z("Art und Weise der Vollstreckung (Verfahrensfehler)", 110, 200, "l766", "Bold", 34),
    z("Erinnerung, § 766 ZPO", 150, 252, beim("l766", "Erinnerung"), size=34),
    z("Schuldner gegen den titulierten Anspruch selbst", 110, 350, "l767", "Bold", 34),
    z("Vollstreckungsabwehrklage, § 767 ZPO", 150, 402, beim("l767", "Vollstreckungsabwehrklage"), size=34),
    z("Dritter mit einem Recht am Gegenstand", 110, 500, "l771", "Bold", 34),
    z("Drittwiderspruchsklage, § 771 ZPO", 150, 552, beim("l771", "Drittwiderspruchsklage"), size=34),
    z("oder Vorzugsklage, § 805 ZPO", 150, 604, "l805", size=34),
    peep_voll("ST_denkt", X1, BR, FR, "ueber"),
    peep_voll("WE_ruhig", X2, BR, FR, "ueber", d=0.2, bis="l771"),
    peep_voll("WE_froh", X2, BR, FR, "l771", anim="cut"),
    namensschild("Herr Steinbach", X1, BR, "ueber", BLAU, d=0.2),
    namensschild("Frau Weidner", X2, BR, "ueber", LILA, d=0.3),
    ficon("tabler", "users", MB, 380, 130, "ueber", fuell=WEISS),
    pl("Wer? Wogegen?", MB, 160, "ueber", fill=PINK, size=30, anker="m"),
]))

# E Erinnerung, § 766 ZPO -----------------------------------------------------------------------------------------------------
PE = "Erinnerung"
folie([("e766", f"{PE}, § 766 ZPO › Art und Weise"), ("vg", f"{PE} › Vollstreckungsgericht, § 764 ZPO"),
       ("p811", f"{PE} › Beispiel: unpfändbare Sache, § 811 ZPO"), ("gew", f"{PE} › hier: kein Verfahrensfehler"),
       ("mat", f"{PE} › Zahlung und Eigentum: nicht hier")], rechts_frei([
    *tafel("e766", "Erinnerung, § 766 ZPO"),
    *wortlaut(110, 170, 1040, 195, "e766", [
        [("„Über Anträge, Einwendungen und Erinnerungen, welche die", 0)],
        [("Art und Weise", "a"), (" der Zwangsvollstreckung oder das vom", 0)],
        [("Gerichtsvollzieher bei ihr ", 0), ("zu beobachtende Verfahren", "b")],
        [("betreffen, entscheidet das ", 0), ("Vollstreckungsgericht", "c"), (". …“", 0)],
    ], 30, {"a": beim("e766", "Art"), "b": beim("e766", "beobachtende"), "c": beim("vg", "Vollstreckungsgericht")},
        "§ 766 Abs. 1 S. 1 ZPO"),
    z("Amtsgericht, in dessen Bezirk vollstreckt wird (§ 764)", 110, 420, beim("vg", "Amtsgericht"), size=32),
    z("typisch: Pfändung einer unpfändbaren Sache, § 811 ZPO", 110, 480, "p811", "Bold", 32),
    nein(135, 565, beim("gew", "kein"), gr=20),
    z("Hier: kein Verfahrensfehler", 175, 545, beim("gew", "kein"), "Bold", 34),
    z("GV prüft grundsätzlich nur den Gewahrsam, nicht das Eigentum", 110, 600, beim("gew", "Gerichtsvollzieher"), size=29),
    z("BGH, Urt. v. 5.7.2007 – III ZR 143/06, Rn. 9", 150, 642, beim("gew", "Bundesgerichtshof"), size=26, farbe=TEXT),
    z("Zahlung, Eigentum: materielle Einwendungen – nicht hier", 110, 700, "mat", "Bold", 32),
    z("Schuldner rügt nur eigene Beschwer, nicht Rechte Dritter", 110, 752, "beschw", size=30),
    z("BGH, Beschl. v. 13.8.2009 – I ZB 91/08, Rn. 9, 13", 150, 796, "beschw", size=26, farbe=TEXT),
    peep_voll("ST_ruhig", X1, BR, FR, "e766", bis="mat"),
    peep_voll("ST_sorge", X1, BR, FR, "mat", anim="cut"),
    peep_voll("GV_ruhig", X2, BR, FR, "e766", d=0.2),
    namensschild("Herr Steinbach", X1, BR, "e766", BLAU, d=0.2),
    namensschild("Gerichtsvollzieher", X2, BR, "e766", TUERKIS, d=0.3),
    ficon("tabler", "list-check", MB, 380, 110, "e766", fuell=WEISS, bis="vg"),
    pl("Verfahren?", MB, 160, "e766", fill=PINK, size=30, anker="m", bis="vg"),
    ficon("tabler", "building-bank", MB, 380, 120, "vg", fuell=BLAU, anim="cut", bis="p811"),
    pl("Vollstreckungsgericht", MB, 160, "vg", fill=BLAU, size=28, anker="m", anim="cut", bis="p811"),
    ficon("tabler", "lock", MB, 380, 100, "p811", fuell=GELB, anim="cut", bis="gew"),
    pl("unpfändbar", MB, 160, "p811", fill=GELB, size=28, anker="m", anim="cut", bis="gew"),
    ficon("tabler", "device-tv", MB, 380, 150, "gew", fuell=DUNKEL, anim="cut"),
    pl("im Gewahrsam", MB, 160, beim("gew", "Gewahrsam"), fill=WEISS, size=28, anker="m", bis="mat"),
    pl("nicht in die Erinnerung", MB, 160, beim("mat", "Sie"), fill=ROT, size=26, anker="m", anim="cut"),
]))

# F Sofortige Beschwerde, § 793 ZPO ------------------------------------------------------------------------------------------
folie([("p793", "Sofortige Beschwerde, § 793 ZPO"), ("frist", "Sofortige Beschwerde › Notfrist, § 569 Abs. 1 ZPO")],
      rechts_frei([
    *tafel("p793", "Sofortige Beschwerde, § 793 ZPO"),
    fl_block(110, 190, 300, 100, WEISS, "p793", [("Erinnerung", "Bold", 32, INK)], rand=4),
    z("›", 445, 200, beim("p793", "Entscheidet"), "ExtraBold", 60),
    fl_block(510, 190, 310, 100, BLAU, beim("p793", "Vollstreckungsgericht"), [("Entscheidung", "Bold", 32, INK)], rand=4),
    z("›", 855, 200, beim("p793", "sofortige"), "ExtraBold", 60),
    fl_block(930, 190, 220, 100, GELB, beim("p793", "sofortige"), [("Beschwerde", "Bold", 30, INK)], rand=4),
    *wortlaut(110, 350, 1040, 160, beim("p793", "sofortige"), [
        [("„Gegen Entscheidungen, die im Zwangsvollstreckungsverfahren", 0)],
        [("ohne mündliche Verhandlung ergehen können, findet", 0)],
        [("sofortige Beschwerde", "a"), (" statt.“", 0)],
    ], 29, {"a": beim("p793", "Beschwerde")}, "§ 793 ZPO"),
    z("Notfrist: zwei Wochen ab Zustellung", 110, 590, "frist", "Bold", 36),
    z("§ 569 Abs. 1 S. 1, 2 ZPO", 150, 645, beim("frist", "Zustellung"), size=30, farbe=TEXT),
    peep_voll("ST_denkt", X1, BR, FR, "p793"),
    peep_voll("GV_ruhig", X2, BR, FR, "p793", d=0.2),
    namensschild("Herr Steinbach", X1, BR, "p793", BLAU, d=0.2),
    namensschild("Gerichtsvollzieher", X2, BR, "p793", TUERKIS, d=0.3),
    ficon("tabler", "file-text", MB, 380, 100, "p793", fuell=WEISS, bis="frist"),
    pl("Beschluss", MB, 160, beim("p793", "Vollstreckungsgericht"), fill=BLAU, size=28, anker="m", bis="frist"),
    ficon("tabler", "calendar-event", MB, 380, 100, "frist", fuell=WEISS, anim="cut"),
    pl("2 Wochen", MB, 160, beim("frist", "zwei"), fill=GELB, size=30, anker="m"),
]))

# G Vollstreckungsabwehrklage, § 767 ZPO ------------------------------------------------------------------------------------
PV = "Vollstreckungsabwehrklage"
folie([("e767", f"{PV}, § 767 ZPO › Einwand: Zahlung"), ("wl767", f"{PV} › Prozessgericht des ersten Rechtszuges"),
       ("erf", f"{PV} › Erfüllung, § 362 BGB"), ("prae", f"{PV} › § 767 Abs. 2 ZPO"),
       ("tenor", f"{PV} › Ergebnis: begründet")], rechts_frei([
    *tafel("e767", "Vollstreckungsabwehrklage, § 767 ZPO"),
    z("Einwand: Zahlung – gegen den Anspruch selbst", 110, 175, beim("e767", "Das"), "Bold", 34),
    *wortlaut(110, 235, 1040, 155, "wl767", [
        [("„", 0), ("Einwendungen", "a"), (", die den durch das Urteil festgestellten Anspruch", 0)],
        [("selbst betreffen, sind von dem Schuldner im Wege der ", 0), ("Klage", "b")],
        [("bei dem ", 0), ("Prozessgericht des ersten Rechtszuges", "c"), (" geltend zu machen.“", 0)],
    ], 29, {"a": beim("wl767", "Einwendungen"), "b": beim("wl767", "Klage"), "c": beim("wl767", "Prozessgericht")},
        "§ 767 Abs. 1 ZPO"),
    z("hier: Amtsgericht, das ihn verurteilt hat", 150, 440, "ag767", size=32),
    z("Zahlung: Schuld erloschen, § 362 Abs. 1 BGB", 110, 505, "erf", "Bold", 34),
    z("Abs. 2: Grund nach Schluss der mündlichen Verhandlung", 110, 575, "prae", "Bold", 32),
    nein(135, 645, "prae2", gr=20),
    z("vorher gezahlt: ausgeschlossen", 175, 625, "prae2", size=32),
    ok(135, 700, "ok767", gr=22),
    z("erst nach dem Urteil gezahlt: nicht ausgeschlossen", 175, 680, "ok767", size=32),
    fl_block(110, 745, 1040, 90, GRUEN, beim("tenor", "Das"),
             [("Zwangsvollstreckung aus dem Urteil: unzulässig", "ExtraBold", 34, INK)]),
    peep_voll("ST_ruhig", X1, BR, FR, "e767", bis="tenor"),
    peep_voll("ST_froh", X1, BR, FR, "tenor", anim="cut"),
    peep_voll("HO_ruhig", X2, BR, FR, "e767", d=0.2, bis="ok767"),
    peep_voll("HO_sorge", X2, BR, FR, "ok767", anim="cut"),
    namensschild("Herr Steinbach", X1, BR, "e767", BLAU, d=0.2),
    namensschild("Frau Hollmann", X2, BR, "e767", GRUEN, d=0.3),
    ficon("tabler", "cash-banknote", MB, 380, 110, "e767", fuell=GRUEN, bis="wl767"),
    pl("bezahlt", MB, 160, "e767", fill=GRUEN, size=30, anker="m", bis="wl767"),
    ficon("tabler", "building-bank", MB, 380, 120, "wl767", fuell=BLAU, anim="cut", bis="erf"),
    pl("Amtsgericht", MB, 160, "ag767", fill=BLAU, size=28, anker="m", bis="erf"),
    ficon("tabler", "receipt", MB, 380, 100, "erf", fuell=WEISS, anim="cut", bis="prae"),
    pl("erloschen", MB, 160, beim("erf", "erloschen"), fill=GRUEN, size=28, anker="m", bis="prae"),
    ficon("tabler", "calendar-event", MB, 380, 100, "prae", fuell=WEISS, anim="cut", bis="tenor"),
    pl("Zeitpunkt?", MB, 160, "prae", fill=PINK, size=28, anker="m", anim="cut", bis="ok767"),
    pl("nach dem Urteil", MB, 160, "ok767", fill=GRUEN, size=28, anker="m", anim="cut", bis="tenor"),
    ficon("tabler", "file-x", MB, 380, 100, "tenor", fuell=WEISS, anim="cut"),
    pl("begründet", MB, 160, beim("tenor", "begründet"), fill=GRUEN, size=30, anker="m"),
]))

# H Kurz: Klauselgegenklage, § 768 ZPO ---------------------------------------------------------------------------------------
folie([("p768", "Kurz: Klauselgegenklage, § 768 ZPO")], rechts_frei([
    *tafel("p768", "Kurz: Klauselgegenklage, § 768 ZPO", fill=LILAHELL, size=46),
    z("Der Schuldner bestreitet die Voraussetzungen,", 110, 200, beim("p768", "Mit"), "Bold", 34),
    z("unter denen die Klausel erteilt wurde,", 110, 252, beim("p768", "unter"), "Bold", 34),
    z("etwa eine Rechtsnachfolge (§ 727 ZPO)", 150, 320, beim("p768", "etwa"), size=34),
    peep_voll("ST_denkt", X1, BR, FR, "p768"),
    peep_voll("HO_ruhig", X2, BR, FR, "p768", d=0.2),
    namensschild("Herr Steinbach", X1, BR, "p768", BLAU, d=0.2),
    namensschild("Frau Hollmann", X2, BR, "p768", GRUEN, d=0.3),
    ficon("tabler", "file-certificate", MB, 380, 110, "p768", fuell=LILA),
    pl("Klausel", MB, 160, "p768", fill=LILA, size=30, anker="m", bis=beim("p768", "etwa")),
    pl("Rechtsnachfolge?", MB, 160, beim("p768", "etwa"), fill=WEISS, size=28, anker="m", anim="cut"),
]))

# I Drittwiderspruchsklage, § 771 ZPO -----------------------------------------------------------------------------------------
PD = "Drittwiderspruchsklage"
folie([("e771", f"{PD}, § 771 ZPO › Frau Weidner ist Dritte"), ("eig", f"{PD} › Eigentum am Fernseher"),
       ("ger771", f"{PD} › Klage gegen die Gläubigerin"), ("ok771", f"{PD} › Ergebnis")], rechts_frei([
    *tafel("e771", "Drittwiderspruchsklage, § 771 ZPO"),
    z("Frau Weidner: nicht Partei des Urteils, sondern Dritte", 110, 175, beim("e771", "Sie"), "Bold", 32),
    *wortlaut(110, 235, 1040, 235, "wl771", [
        [("„Behauptet ein ", 0), ("Dritter", "a"), (", dass ihm an dem Gegenstand der", 0)],
        [("Zwangsvollstreckung ein ", 0), ("die Veräußerung hinderndes Recht", "b")],
        [("zustehe, so ist der Widerspruch gegen die Zwangsvollstreckung", 0)],
        [("im Wege der Klage", "c"), (" bei dem Gericht geltend zu machen, in", 0)],
        [("dessen Bezirk die Zwangsvollstreckung erfolgt", "d"), (".“", 0)],
    ], 29, {"a": beim("wl771", "Dritter"), "b": beim("wl771", "Veräußerung"), "c": beim("wl771", "Klage"),
            "d": beim("ger771", "Bezirk")}, "§ 771 Abs. 1 ZPO"),
    ok(135, 555, beim("eig", "Eigentum"), gr=22),
    z("Recht: ihr Eigentum am Fernseher (geliehen)", 175, 535, beim("eig", "Eigentum"), "Bold", 34),
    z("BGH, Urt. v. 5.7.2007 – III ZR 143/06, Rn. 12", 175, 585, beim("eig", "Fernseher"), size=26, farbe=TEXT),
    z("Klage gegen Frau Hollmann, Gericht des Vollstreckungsbezirks", 110, 645, "ger771", "Bold", 32),
    fl_block(110, 715, 1040, 90, GRUEN, beim("ok771", "erklärt"),
             [("Zwangsvollstreckung in den Fernseher: unzulässig", "ExtraBold", 34, INK)]),
    peep_voll("WE_ruhig", X1, BR, FR, "e771", bis="ok771"),
    peep_voll("WE_froh", X1, BR, FR, beim("ok771", "erklärt"), anim="cut"),
    peep_voll("WE_denkt", X1, BR, FR, "ok771", anim="cut", bis=beim("ok771", "erklärt")),
    peep_voll("HO_ruhig", X2, BR, FR, "e771", d=0.2, bis="ger771"),
    peep_voll("HO_streng", X2, BR, FR, "ger771", anim="cut", bis=beim("ok771", "erklärt")),
    peep_voll("HO_sorge", X2, BR, FR, beim("ok771", "erklärt"), anim="cut"),
    namensschild("Frau Weidner", X1, BR, "e771", LILA, d=0.2),
    namensschild("Frau Hollmann", X2, BR, "e771", GRUEN, d=0.3),
    ficon("tabler", "device-tv", MB, 380, 150, "e771", fuell=DUNKEL),
    pl("Dritte", MB, 160, beim("e771", "Dritte"), fill=LILA, size=30, anker="m", bis="eig"),
    pl("gehört Frau Weidner", MB, 160, "eig", fill=LILA, size=28, anker="m", anim="cut", bis="ok771"),
    pl("unzulässig", MB, 160, beim("ok771", "erklärt"), fill=GRUEN, size=30, anker="m", anim="cut"),
]))

# J Kurz: Vorzugsklage, § 805 ZPO ---------------------------------------------------------------------------------------------
folie([("p805", "Kurz: Vorzugsklage, § 805 ZPO"), ("p805b", "Vorzugsklage › vorzugsweise Befriedigung aus dem Erlös")],
      rechts_frei([
    *tafel("p805", "Kurz: Vorzugsklage, § 805 ZPO", fill=LILAHELL, size=46),
    z("Dritter ohne Besitz, nur mit Pfandrecht", 110, 200, beim("p805", "Dritten"), "Bold", 34),
    z("etwa Vermieterpfandrecht an eingebrachten", 150, 255, beim("p805", "Vermieter"), size=32),
    z("Sachen des Mieters (§ 562 Abs. 1 BGB)", 150, 300, beim("p805", "eingebrachten"), size=32),
    nein(135, 385, "p805b", gr=20),
    z("kein Widerspruch gegen die Pfändung", 175, 365, "p805b", "Bold", 34),
    ok(135, 455, beim("p805b", "klagt"), gr=22),
    z("Klage auf vorzugsweise Befriedigung aus dem Erlös", 175, 435, beim("p805b", "klagt"), "Bold", 32),
    z("BGH, Beschl. v. 13.8.2009 – I ZB 91/08, Rn. 15", 175, 485, beim("p805b", "Erlös"), size=26, farbe=TEXT),
    peep_voll("HO_ruhig", X1, BR, FR, "p805"),
    peep_voll("GV_ruhig", X2, BR, FR, "p805", d=0.2),
    namensschild("Frau Hollmann", X1, BR, "p805", GRUEN, d=0.2),
    namensschild("Gerichtsvollzieher", X2, BR, "p805", TUERKIS, d=0.3),
    ficon("tabler", "home", MB, 380, 110, beim("p805", "Vermieter"), fuell=GELB, bis="p805b"),
    pl("Vermieter", MB, 160, beim("p805", "Vermieter"), fill=GELB, size=30, anker="m", bis="p805b"),
    ficon("tabler", "coins", MB, 380, 110, beim("p805b", "klagt"), fuell=GELB, anim="cut"),
    pl("aus dem Erlös", MB, 160, beim("p805b", "Erlös"), fill=GELB, size=28, anker="m"),
]))

# K Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · mehrere Rechtsbehelfe zugleich"), ("tipp2", "Klausurtipp · einstweilige Einstellung, § 769 ZPO")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Mehrere Beteiligte – verschiedene Rechtsbehelfe", 200, 200, beim("tipp", "Mehrere"), "Bold", 34),
    z("Herr Steinbach: § 767 ZPO", 240, 265, beim("tipp", "Steinbach"), size=34),
    z("Frau Weidner: § 771 ZPO", 240, 320, beim("tipp", "Weidner"), size=34),
    z("Die Klage allein hält die Vollstreckung nicht auf:", 200, 420, "tipp2", "Bold", 34),
    z("zugleich einstweilige Einstellung beantragen,", 240, 478, beim("tipp2", "Beantrage"), size=34),
    z("§ 769 ZPO; bei § 771 über § 771 Abs. 3 ZPO", 240, 533, beim("tipp2", "Paragraf"), "Bold", 34),
    *redet("LX_warnt", LXX, BR, FR + 60, "tipp", "sch"),
    namensschild("Lexi", LXX, BR, "tipp", GELB, d=0.2),
])

# L Klausurschema ----------------------------------------------------------------------------------------------------------------
K1, K2, K3 = 150, 210, 260
folie([("sch", "Klausurschema"), ("sA", "Klausurschema › A. Zulässigkeit"), ("sB", "Klausurschema › B. Begründetheit")], [
    karte(60, 50, 1800, 900, "sch"),
    titel("Klausurschema: Rechtsbehelfe in der Zwangsvollstreckung", 110, 90, "sch", 50),
    z("A. Zulässigkeit", K1, 180, "sA", "ExtraBold", 38, rechts=1820),
    z("1. Statthaftigkeit nach der Leitfrage: Wer wehrt sich wogegen?", K2, 240, "s1", "Bold", 34, rechts=1820),
    z("2. Zuständigkeit, ausschließlich (§ 802 ZPO)", K2, 300, "s2", "Bold", 34, rechts=1820),
    z("§ 766: Vollstreckungsgericht – § 767: Prozessgericht des ersten Rechtszuges – § 771: Gericht am Vollstreckungsort",
      K3, 352, beim("s2", "ausschließlich"), size=28, farbe=TEXT, rechts=1820),
    z("3. Rechtsschutzbedürfnis", K2, 410, "s3", "Bold", 34, rechts=1820),
    z("B. Begründetheit", K1, 500, "sB", "ExtraBold", 38, rechts=1820),
    z("§ 766: Verstoß gegen Vollstreckungsrecht", K2, 560, "sb1", "Bold", 34, rechts=1820),
    z("§ 767: materielle Einwendung, nicht nach § 767 Abs. 2 ZPO ausgeschlossen", K2, 620, "sb2", "Bold", 34, rechts=1820),
    z("§ 771: ein die Veräußerung hinderndes Recht des Dritten", K2, 680, "sb3", "Bold", 34, rechts=1820),
])

# M Merksatz (Lexi) --------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Gegen das Wie der Vollstreckung:", 0)], [("Erinnerung", "a"), (".", 0)]], 750, 300, 46, "merke",
                {"a": beim("merke", "Erinnerung")}),
    *markertext([[("Gegen den Anspruch:", 0)], [("Vollstreckungsabwehrklage", "b"), (".", 0)]], 750, 450, 46,
                beim("merke", "gegen"), {"b": beim("merke", "Vollstreckungsabwehrklage")}),
    *markertext([[("Wem die Sache gehört:", 0)], [("Drittwiderspruchsklage", "c"), (".", 0)]], 750, 600, 46, "m2",
                {"c": beim("m2", "Drittwiderspruchsklage")}),
    *redet("LX_erklaert", 1680, 960, 690, "merke", lexi_bis_ende("merke")),
    namensschild("Lexi", 1680, 960, "merke", GELB, d=0.2),
])
