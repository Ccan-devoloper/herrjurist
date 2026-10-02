"""Folge 078 · Vollstreckungsabwehrklage § 767 ZPO – Prüfung im 2. Examen – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A In der Tischlerei (Einbauschrank, Klage, Verhandlung, Urteil, Überweisung, Beleg),
B An der Wohnungstür (Gerichtsvollzieherin), C In der Kanzlei (Rechtsanwältin Kellermann, Frage), D Sachverhalt,
E A. Zulässigkeit: Statthaftigkeit (Wortlautkarte § 767 I ZPO, Abgrenzung §§ 766, 771), F Zuständigkeit (§ 802) und
Rechtsschutzbedürfnis (BGH I ZR 180/21 Rn. 11), G B. Begründetheit: Erfüllung, Präklusion (Wortlautkarte § 767 II ZPO,
Zeitstrahl), H Aufrechnung (BGH II ZR 170/17 Rn. 11 f.) und § 767 III, I Tenor (Klausurkonvention), J einstweilige
Einstellung § 769 (Glaubhaftmachung, § 775 Nr. 2), K Zahlungsbeleg (Wortlautkarte § 775 Nr. 5 ZPO, Nr. 4, § 776, § 770),
L Klausurtipp (Lexi), M Klausurschema, N Merksatz (Lexi).
Geräusche nur bei sichtbarer Handlung: Hammer am Einbauschrank (A), Türklingel (B); Freesound CC0."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont

bausteine.FIGORDNER = "op_078/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
LILAHELL = (246, 243, 255, 255)
ROTHELL = (253, 232, 228, 255)
GRUENHELL = (232, 247, 233, 255)
BLAUHELL = (232, 240, 253, 255)
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


def fb(x, y, w, h, fill, cue, zeilen, **k):
    for t, *_ in zeilen:
        glyphen(t)
    return fl_block(x, y, w, h, fill, cue, zeilen, **k)


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


# --- Eigene Hilfsfunktion (wie Folge 054/072): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ---------------
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
X1, X2 = 1390, 1730                     # zwei Figuren neben der Tafel
MB = (X1 + X2) // 2
XS = 1600                               # eine Figur allein neben der Tafel

ROTHELL2 = ROTHELL
FUND = 26                               # Fundstellen (mobil mindestens 26 px)


def fund(text, x, y, cue, rechts=1170):
    return z(text, x, y, cue, size=FUND, farbe=TEXT, rechts=rechts)



HOLZHELL = (232, 190, 145, 255)
NULL_ = NULL


def schrank(x, y, w, h, cue):
    """Einbauschrank aus Tafelbausteinen (Korpus, zwei Türen, Griffe) – keine Iconvorlage vorhanden."""
    tb = (w - 50) // 2
    return [karte(x, y, w, h, cue, fill=HOLZ, rund=8, schatten=5, anim="pop"),
            karte(x + 18, y + 18, tb, h - 36, cue, fill=HOLZHELL, rund=6, schatten=0, rand=4, anim="pop"),
            karte(x + 32 + tb, y + 18, tb, h - 36, cue, fill=HOLZHELL, rund=6, schatten=0, rand=4, anim="pop"),
            karte(x + 18 + tb - 26, y + h // 2 - 22, 14, 44, cue, fill=DUNKEL, rund=6, schatten=0, rand=3, anim="pop"),
            karte(x + 32 + tb + 12, y + h // 2 - 22, 14, 44, cue, fill=DUNKEL, rund=6, schatten=0, rand=3, anim="pop")]


# A Fall: in der Tischlerei ---------------------------------------------------------------------------------------------------
RX, NX = 330, 1590                      # Rademacher (blickt nach rechts), Neubauer (blickt nach links)
SCH = beim("schrank", "baut")
folie([(NULL, "Fall · Der Einbauschrank"), ("klage", "Fall · Klage und Urteil"), ("ueberw", "Fall · Die Überweisung")], [
    linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK),
    pl("Tischlerei Rademacher", 70, 40, NULL, fill=GELB, size=40),
    peep_voll("RA_ruhig_r", RX, BODEN, FH, NULL, bis="zahlt"),
    peep_voll("RA_streng_r", RX, BODEN, FH, "zahlt", anim="cut", bis=beim("urteil", "rechtskräftig")),
    peep_voll("RA_froh_r", RX, BODEN, FH, beim("urteil", "rechtskräftig"), anim="cut", bis="ueberw"),
    peep_voll("RA_ruhig_r", RX, BODEN, FH, "ueberw", anim="cut"),
    namensschild("Herr Rademacher", RX, BODEN, NULL, GELB),
    *schrank(800, 560, 330, BODEN - 560, SCH),
    # der Hammer schlägt am Schrank (Handlungsgeräusch)
    szene(bewegt(ficon("tabler", "hammer", 1185, 640, 80, beim("schrank", "baut"), fuell=WEISS, bis="zahlt"),
                 beim("schrank", "baut"), beim("schrank", "baut", ende=True), 0, -50), "078hammer*", 0.9, 0.0),
    pl("Einbauschrank: 3.600 €", 965, 160, beim("schrank", "dreitausendsechshundert"), fill=GELB, size=34, anker="m", bis="klage"),
    peep_voll("NB_ruhig", NX, BODEN, FH, beim("schrank", "Herrn"), anim="fade", bis="zahlt"),
    peep_voll("NB_denkt", NX, BODEN, FH, "zahlt", anim="cut", bis="urteil"),
    peep_voll("NB_sorge", NX, BODEN, FH, "urteil", anim="cut", bis="ueberw"),
    peep_voll("NB_ruhig", NX, BODEN, FH, "ueberw", anim="cut", bis="beleg"),
    peep_voll("NB_froh", NX, BODEN, FH, "beleg", anim="cut"),
    namensschild("Herr Neubauer", NX, BODEN, beim("schrank", "Herrn"), GRUEN),
    ficon("tabler", "cash-off", 965, 500, 90, beim("zahlt", "zahlt"), fuell=ROT, bis="klage"),
    pl("zahlt nicht", 965, 245, beim("zahlt", "zahlt"), fill=WEISS, size=32, anker="m", bis="klage"),
    # Klage, Verhandlung, Urteil
    ficon("tabler", "building-bank", 965, 525, 100, "klage", fuell=BLAU, anim="cut", bis=beim("ueberw", "überweist")),
    pl("Klage vor dem Amtsgericht", 965, 140, "klage", fill=BLAU, size=30, anker="m", bis=beim("ueberw", "überweist")),
    pl("mündliche Verhandlung: 4.3.2026", 965, 210, beim("mv", "vierten"), fill=WEISS, size=30, anker="m", bis=beim("ueberw", "überweist")),
    pl("Urteil 18.3.2026: Neubauer zahlt 3.600 €", 965, 280, beim("urteil", "verurteilt"), fill=WEISS, size=30, anker="m", bis=beim("ueberw", "überweist")),
    pl("rechtskräftig", 965, 350, beim("urteil", "rechtskräftig"), fill=GRUEN, size=30, anker="m", bis=beim("ueberw", "überweist")),
    # die Überweisung wandert von Herrn Neubauer zu Herrn Rademacher, die Bank bestätigt sie
    bewegt(ficon("tabler", "cash-banknote", 560, 520, 110, beim("ueberw", "überweist"), fuell=GRUEN),
           beim("ueberw", "überweist"), beim("ueberw", "Betrag", ende=True), NX - 160 - 560, 0),
    pl("Überweisung 4.5.2026: 3.600 €", 965, 160, beim("ueberw", "überweist"), fill=GRUEN, size=32, anker="m"),
    ficon("tabler", "receipt", NX - 150, 610, 70, beim("beleg", "Bank"), fuell=WEISS),
    pl("Überweisungsbeleg der Bank", 965, 245, beim("beleg", "bestätigt"), fill=WEISS, size=30, anker="m"),
])

# B Fall: an der Wohnungstür ----------------------------------------------------------------------------------------------------
NX2, GX = 470, 1330
TX = 760                                # Tür (Rahmen links bei TX)
NBb = ("NB_redet_r", NX2, BODEN, FH)
GVb = ("GV_redet", GX, BODEN, FH)
folie([("tuer", "Fall · Die Gerichtsvollzieherin")], [
    hart(linienzug([(60, BODEN), (1860, BODEN)], "tuer", breite=7, farbe=INK)),
    pl("Wohnung von Herrn Neubauer", 70, 40, "tuer", fill=GRUEN, size=40, anim="cut"),
    hart(karte(TX, 370, 250, BODEN - 370, "tuer", fill=HOLZ, rund=8, schatten=5)),
    hart(karte(TX + 20, 390, 210, BODEN - 390, "tuer", fill=HOLZHELL, rund=6, schatten=0, rand=4)),
    hart(karte(TX + 190, 610, 18, 50, "tuer", fill=DUNKEL, rund=6, schatten=0, rand=3)),
    pl("Trotzdem: Vollstreckungsauftrag", 1420, 150, "tuer", fill=PINK, size=30, anker="m", bis="g1"),
    pl("Juni 2026", 1420, 225, beim("tuer", "Juni"), fill=WEISS, size=30, anker="m", bis="g1"),
    peep_voll("GV_ruhig", GX, BODEN, FH, beim("tuer", "Gerichtsvollzieherin"), anim="fade", bis="g1"),
    *redet("GV_redet", GX, BODEN, FH, "g1", "n1"),
    peep_voll("GV_ruhig", GX, BODEN, FH, "n1", anim="cut", bis="kanzlei"),
    namensschild("Gerichtsvollzieherin", GX, BODEN, beim("tuer", "Gerichtsvollzieherin"), TUERKIS),
    # die Gerichtsvollzieherin klingelt (Handlungsgeräusch)
    szene(ficon("tabler", "bell-ringing", TX + 300, 560, 70, beim("tuer", "klingelt"), fuell=GELB, bis="g1"), "078klingel*", 0.8, 0.0),
    peep_voll("NB_ruhig_r", NX2, BODEN, FH, beim("tuer", "Neubauer"), anim="fade", bis="g1"),
    peep_voll("NB_schreck_r", NX2, BODEN, FH, "g1", anim="cut", bis="n1"),
    *redet("NB_redet_r", NX2, BODEN, FH, "n1", "kanzlei"),
    namensschild("Herr Neubauer", NX2, BODEN, beim("tuer", "Neubauer"), GRUEN),
    blase("sprech", 660, 230, "g1", 1450, 230, inhalt=["Ich vollstrecke im Auftrag", "von Herrn Rademacher aus", "dem Urteil des Amtsgerichts."],
          textsize=32, figur=GVb, bis="n1"),
    blase("sprech", 560, 180, "n1", 560, 245, inhalt=["Aber ich habe doch längst", "alles überwiesen!"], textsize=34,
          figur=NBb, bis="kanzlei"),
])

# C Fall: in der Kanzlei --------------------------------------------------------------------------------------------------------
NX3, KX = 400, 1500
NBc = ("NB_redet_r", NX3, BODEN, FH)
KMc = ("KM_redet", KX, BODEN, FH)
folie([("kanzlei", "Fall · In der Kanzlei"), ("frage", "Fall · Die Frage")], [
    hart(linienzug([(60, BODEN), (1860, BODEN)], "kanzlei", breite=7, farbe=INK)),
    pl("Kanzlei Kellermann", 70, 40, "kanzlei", fill=LILA, size=40, anim="cut"),
    ficon("tabler", "desk", 950, BODEN - 2, 420, "kanzlei", fuell=HOLZ, anim="cut"),
    ficon("tabler", "receipt", 880, 702, 70, beim("kanzlei", "Neubauer"), fuell=WEISS),
    ficon("tabler", "file-text", 1010, 702, 80, beim("kanzlei", "Neubauer"), fuell=WEISS),
    peep_voll("NB_sorge_r", NX3, BODEN, FH, "kanzlei", anim="cut", bis="n2"),
    *redet("NB_redet_r", NX3, BODEN, FH, "n2", "k1"),
    peep_voll("NB_ruhig_r", NX3, BODEN, FH, "k1", anim="cut", bis="frage"),
    peep_voll("NB_denkt_r", NX3, BODEN, FH, "frage", anim="cut"),
    namensschild("Herr Neubauer", NX3, BODEN, "kanzlei", GRUEN, anim="cut"),
    peep_voll("KM_ruhig", KX, BODEN, FH, beim("kanzlei", "Rechtsanwältin"), anim="fade", bis="k1"),
    *redet("KM_redet", KX, BODEN, FH, "k1", "frage"),
    peep_voll("KM_denkt", KX, BODEN, FH, "frage", anim="cut"),
    namensschild("Rechtsanwältin Kellermann", KX, BODEN, beim("kanzlei", "Rechtsanwältin"), LILA),
    blase("sprech", 640, 180, "n2", 660, 250, inhalt=["Wie halte ich die Vollstreckung", "auf, und zwar endgültig?"],
          textsize=32, figur=NBc, bis="k1"),
    blase("sprech", 740, 230, "k1", 1200, 245, inhalt=["Wir erheben Vollstreckungsabwehrklage.", "Und bis zum Urteil sichern wir",
          "Sie mit einem Eilantrag ab."], textsize=30, figur=KMc, bis="frage"),
    pl("Wie prüfst du diese Klage in der Anwaltsklausur?", 960, 150, "frage", fill=PINK, size=38, anker="m"),
    pl("Und wie stoppt er die Vollstreckung, bis das Gericht entscheidet?", 960, 235, "frage2", fill=WEISS, size=32, anker="m"),
])

# D Sachverhalt -----------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    glyphen("Tischlermeister Rademacher baut Herrn Neubauer einen Einbauschrank für 3.600 €. Neubauer zahlt nicht. Nach der "
            "mündlichen Verhandlung am 4.3.2026 verurteilt ihn das Amtsgericht am 18.3.2026 zur Zahlung; das Urteil wird "
            "rechtskräftig."),
    glyphen("Am 4.5.2026 überweist Neubauer den vollen Betrag; das Geld geht auf dem Konto von Rademacher ein. Seine Bank "
            "bestätigt die Überweisung mit einem Beleg. Trotzdem beauftragt Rademacher im Juni die Gerichtsvollzieherin."),
    glyphen("Neubauer geht zu Rechtsanwältin Kellermann. Annahme: Die Überweisung deckt alles, was das Urteil zuspricht."),
], "Wie wehrt sich Neubauer – endgültig und sofort?")

# E A. Zulässigkeit: 1. Statthaftigkeit --------------------------------------------------------------------------------------------
PA = "A. Zulässigkeit"
folie([("zul", PA), ("statt", f"{PA} › 1. Statthaftigkeit"), ("a766", f"{PA} › 1. Statthaftigkeit › Abgrenzung")], rechts_frei([
    *tafel("zul", "A. Zulässigkeit"),
    z("1. Statthaftigkeit", 110, 170, "statt", "Bold", 36),
    *wortlaut(110, 235, 1040, 155, "wl767", [
        [("„", 0), ("Einwendungen", "a"), (", die den durch das Urteil festgestellten ", 0), ("Anspruch", "b")],
        [("selbst", "b"), (" betreffen, sind von dem Schuldner im Wege der ", 0), ("Klage", "c")],
        [("bei dem Prozessgericht des ersten Rechtszuges geltend zu machen.“", 0)],
    ], 29, {"a": beim("wl767", "Einwendungen"), "b": beim("wl767", "Anspruch"), "c": beim("wl767", "Klage")},
        "§ 767 Abs. 1 ZPO"),
    z("Herr Neubauer wendet Erfüllung ein:", 110, 440, "erfE", "Bold", 34),
    z("materielle Einwendung gegen den titulierten Anspruch", 150, 492, beim("erfE", "materielle"), size=32),
    ok(135, 565, beim("erfE", "statthaft"), gr=22),
    z("Klage statthaft", 175, 545, beim("erfE", "statthaft"), "Bold", 34),
    z("Abgrenzung", 110, 615, "a766", "ExtraBold", 32),
    z("nur Art und Weise der Vollstreckung: Erinnerung, § 766 ZPO", 150, 662, beim("a766", "Art"), size=30),
    z("Dritter mit Recht am Gegenstand: Drittwiderspruchsklage, § 771", 150, 707, beim("a771", "Dritter"), size=30),
    pl("Video: Rechtsbehelfe in der Zwangsvollstreckung", 150, 765, beim("verw", "Video"), fill=LILA, size=28),
    peep_voll("NB_ruhig", X1, BR, FR, "zul", bis="erfE"),
    peep_voll("NB_denkt", X1, BR, FR, "erfE", anim="cut", bis=beim("erfE", "statthaft")),
    peep_voll("NB_froh", X1, BR, FR, beim("erfE", "statthaft"), anim="cut"),
    peep_voll("KM_ruhig", X2, BR, FR, "zul", d=0.2, bis="a766"),
    peep_voll("KM_denkt", X2, BR, FR, "a766", anim="cut"),
    namensschild("Herr Neubauer", X1, BR, "zul", GRUEN, d=0.2),
    namensschild("RAin Kellermann", X2, BR, "zul", LILA, d=0.3),
    ficon("tabler", "file-certificate", MB, 380, 110, "zul", fuell=WEISS, bis="erfE"),
    pl("Urteil", MB, 160, "zul", fill=WEISS, size=30, anker="m", bis="erfE"),
    ficon("tabler", "receipt", MB, 380, 100, "erfE", fuell=GRUEN, anim="cut", bis="a766"),
    pl("Erfüllung", MB, 160, beim("erfE", "Erfüllung"), fill=GRUEN, size=30, anker="m", anim="cut", bis="a766"),
    ficon("tabler", "list-check", MB, 380, 100, "a766", fuell=WEISS, anim="cut", bis="a771"),
    pl("§ 766: Art und Weise", MB, 160, beim("a766", "Art"), fill=BLAU, size=28, anker="m", anim="cut", bis="a771"),
    ficon("tabler", "users", MB, 380, 110, "a771", fuell=WEISS, anim="cut"),
    pl("§ 771: Dritter", MB, 160, beim("a771", "Dritter"), fill=LILA, size=28, anker="m", anim="cut"),
]))

# F Zuständigkeit und Rechtsschutzbedürfnis -----------------------------------------------------------------------------------------
folie([("zust", f"{PA} › 2. Zuständigkeit"), ("p802", f"{PA} › 2. Zuständigkeit, § 802 ZPO"),
       ("rsb", f"{PA} › 3. Rechtsschutzbedürfnis"), ("rsb3", f"{PA} › Ergebnis: zulässig")], rechts_frei([
    *tafel("zust", "A. Zulässigkeit"),
    z("2. Zuständigkeit", 110, 170, "zust", "Bold", 36),
    z("Prozessgericht des ersten Rechtszuges (§ 767 Abs. 1 ZPO)", 150, 225, beim("zust", "Prozessgericht"), size=32),
    z("hier: das Amtsgericht, das Herrn Neubauer verurteilt hat", 150, 275, "ag", size=32),
    z("ausschließlich, § 802 ZPO", 150, 325, beim("p802", "ausschließlich"), "Bold", 32),
    z("3. Rechtsschutzbedürfnis", 110, 405, "rsb", "Bold", 36),
    z("hängt nicht davon ab, dass Vollstreckung droht", 150, 460, beim("rsb2", "hängt"), size=32),
    z("besteht grundsätzlich, solange der Gläubiger", 150, 510, beim("rsb2", "Es"), size=32),
    z("den Titel noch in Händen hat", 150, 555, beim("rsb2", "Titel"), size=32),
    fund("BGH, Urt. v. 29.9.2022 – I ZR 180/21, Rn. 11", 150, 605, beim("rsb2", "hängt")),
    ok(135, 680, beim("rsb3", "Urteil"), gr=22),
    z("Herr Rademacher hat das Urteil noch", 175, 660, beim("rsb3", "Urteil"), size=32),
    fb(110, 725, 1040, 85, GRUEN, beim("rsb3", "zulässig"), [("Die Klage ist zulässig.", "ExtraBold", 34, INK)]),
    peep_voll("NB_ruhig", X1, BR, FR, "zust", bis=beim("rsb3", "zulässig")),
    peep_voll("NB_froh", X1, BR, FR, beim("rsb3", "zulässig"), anim="cut"),
    peep_voll("RA_ruhig", X2, BR, FR, "zust", d=0.2, bis="rsb3"),
    peep_voll("RA_streng", X2, BR, FR, "rsb3", anim="cut"),
    namensschild("Herr Neubauer", X1, BR, "zust", GRUEN, d=0.2),
    namensschild("Herr Rademacher", X2, BR, "zust", GELB, d=0.3),
    ficon("tabler", "building-bank", MB, 380, 120, "zust", fuell=BLAU, bis="rsb"),
    pl("Amtsgericht", MB, 160, "ag", fill=BLAU, size=30, anker="m", bis="p802"),
    pl("ausschließlich", MB, 160, beim("p802", "ausschließlich"), fill=WEISS, size=28, anker="m", anim="cut", bis="rsb"),
    ficon("tabler", "file-certificate", MB, 380, 110, "rsb", fuell=WEISS, anim="cut"),
    pl("Titel in Händen?", MB, 160, beim("rsb2", "Es"), fill=PINK, size=28, anker="m", bis="rsb3"),
    pl("ja", MB, 160, beim("rsb3", "Urteil"), fill=GRUEN, size=30, anker="m", anim="cut"),
]))

# G B. Begründetheit: Erfüllung und Präklusion --------------------------------------------------------------------------------------
PB = "B. Begründetheit"
ZX1, ZX2 = 330, 900                      # Zeitstrahl: Schluss der mündlichen Verhandlung, Zahlung
folie([("begr", PB), ("erf", f"{PB} › Einwendung: Erfüllung, § 362 BGB"), ("prae", f"{PB} › Präklusion, § 767 Abs. 2 ZPO")],
      rechts_frei([
    *tafel("begr", "B. Begründetheit"),
    z("Einwendung gegen den titulierten Anspruch, nicht ausgeschlossen", 110, 170, beim("begr", "Einwendung"), "Bold", 32),
    z("Erfüllung: Das Geld ist angekommen.", 110, 228, "erf", size=32),
    ok(135, 298, beim("erf", "erloschen"), gr=20),
    z("Schuld erloschen, § 362 Abs. 1 BGB", 175, 278, beim("erf", "erloschen"), "Bold", 32),
    *wortlaut(110, 345, 1040, 230, "prae", [
        [("„Sie sind ", 0), ("nur insoweit zulässig", "a"), (", als die Gründe, auf denen sie", 0)],
        [("beruhen, ", 0), ("erst nach dem Schluss der mündlichen Verhandlung", "b"), (",", 0)],
        [("in der Einwendungen nach den Vorschriften dieses Gesetzes", 0)],
        [("spätestens hätten geltend gemacht werden müssen, ", 0), ("entstanden", "c")],
        [("sind und durch Einspruch nicht mehr geltend gemacht werden können.“", 0)],
    ], 27, {"a": beim("wl767b", "nur"), "b": beim("wl767b", "Schluss"), "c": beim("wl767b", "entstanden")},
        "§ 767 Abs. 2 ZPO"),
    hart(linienzug([(150, 700), (1130, 700)], beim("prae2", "vierte"), breite=6, farbe=INK)),
    hart(linienzug([(ZX1, 680), (ZX1, 720)], beim("prae2", "vierte"), breite=8, farbe=DROT)),
    z("4.3.2026: Schluss der mündlichen Verhandlung", 150, 730, beim("prae2", "vierte"), "Bold", 28),
    hart(linienzug([(ZX2, 680), (ZX2, 720)], beim("prae3", "vierten"), breite=8, farbe=DGRUEN)),
    z("4.5.2026: Zahlung", 840, 730, beim("prae3", "vierten"), "Bold", 28),
    ok(135, 810, beim("prae3", "nicht"), gr=22),
    z("danach entstanden: nicht ausgeschlossen", 175, 790, beim("prae3", "nicht"), "Bold", 32),
    peep_voll("NB_ruhig", X1, BR, FR, "begr", bis=beim("prae3", "nicht")),
    peep_voll("NB_froh", X1, BR, FR, beim("prae3", "nicht"), anim="cut"),
    peep_voll("RA_ruhig", X2, BR, FR, "begr", d=0.2, bis="erf"),
    peep_voll("RA_denkt", X2, BR, FR, "erf", anim="cut", bis=beim("prae3", "nicht")),
    peep_voll("RA_sorge", X2, BR, FR, beim("prae3", "nicht"), anim="cut"),
    namensschild("Herr Neubauer", X1, BR, "begr", GRUEN, d=0.2),
    namensschild("Herr Rademacher", X2, BR, "begr", GELB, d=0.3),
    ficon("tabler", "cash-banknote", MB, 380, 110, "erf", fuell=GRUEN, bis="prae"),
    pl("erloschen", MB, 160, beim("erf", "erloschen"), fill=GRUEN, size=30, anker="m", bis="prae"),
    ficon("tabler", "calendar-event", MB, 380, 100, "prae", fuell=WEISS, anim="cut"),
    pl("Zeitpunkt?", MB, 160, "prae", fill=PINK, size=30, anker="m", anim="cut", bis="prae3"),
    pl("nach dem 4.3.2026", MB, 160, "prae3", fill=GRUEN, size=28, anker="m", anim="cut"),
]))

# H Präklusion: Aufrechnung und § 767 Abs. 3 ---------------------------------------------------------------------------------------
folie([("gest", f"{PB} › Präklusion: Aufrechnung"), ("abs3", f"{PB} › § 767 Abs. 3 ZPO")], rechts_frei([
    *tafel("gest", "Präklusion: Aufrechnung und Abs. 3"),
    z("Vorsicht bei Gestaltungsrechten wie der Aufrechnung:", 110, 180, "gest", "Bold", 34),
    nein(135, 265, beim("gest", "ausgeschlossen"), gr=20),
    z("ausgeschlossen, wenn die Forderungen sich schon vor", 175, 245, beim("gest", "ausgeschlossen"), size=32),
    z("dem Schluss der Verhandlung aufrechenbar gegenüberstanden,", 175, 292, beim("gest", "Schluss"), size=32),
    z("auch wenn erst später aufgerechnet wird", 175, 339, beim("gest", "auch"), size=32),
    fund("BGH, VU v. 25.6.2019 – II ZR 170/17, Rn. 11 f.", 175, 392, beim("gest", "auch")),
    z("§ 767 Abs. 3 ZPO:", 110, 480, "abs3", "ExtraBold", 34),
    z("Alle Einwendungen, die der Schuldner bei Klageerhebung", 150, 535, beim("abs3", "Alle"), size=32),
    z("geltend machen kann, muss er in dieser Klage vorbringen.", 150, 582, beim("abs3", "geltend"), size=32),
    peep_voll("NB_denkt", X1, BR, FR, "gest", bis="abs3"),
    peep_voll("NB_ruhig", X1, BR, FR, "abs3", anim="cut"),
    peep_voll("KM_ruhig", X2, BR, FR, "gest", d=0.2, bis=beim("gest", "ausgeschlossen")),
    peep_voll("KM_denkt", X2, BR, FR, beim("gest", "ausgeschlossen"), anim="cut", bis="abs3"),
    peep_voll("KM_ruhig", X2, BR, FR, "abs3", anim="cut"),
    namensschild("Herr Neubauer", X1, BR, "gest", GRUEN, d=0.2),
    namensschild("RAin Kellermann", X2, BR, "gest", LILA, d=0.3),
    ficon("tabler", "arrows-exchange", MB, 380, 110, "gest", fuell=WEISS, bis="abs3"),
    pl("Aufrechnung", MB, 160, beim("gest", "Aufrechnung"), fill=WEISS, size=30, anker="m", bis="abs3"),
    ficon("tabler", "checkup-list", MB, 380, 100, "abs3", fuell=WEISS, anim="cut"),
    pl("alle Einwendungen", MB, 160, beim("abs3", "Alle"), fill=GELB, size=28, anker="m", anim="cut"),
]))

# I Tenor (Klausurkonvention) -----------------------------------------------------------------------------------------------------
folie([("tenor", "Tenor (Klausurkonvention)"), ("antrag", "Tenor › Klageantrag in der Anwaltsklausur")], rechts_frei([
    *tafel("tenor", "Tenor (Klausurkonvention)"),
    fb(110, 185, 1040, 230, GRUEN, beim("tenor", "Die"),
       [("Die Zwangsvollstreckung aus dem Urteil des", "Bold", 34, INK),
        ("Amtsgerichts vom 18.3.2026", "Bold", 34, INK),
        ("wird für unzulässig erklärt.", "ExtraBold", 36, INK)]),
    z("Anwaltsklausur, Klageantrag:", 110, 470, "antrag", "Bold", 34),
    z("„… die Zwangsvollstreckung aus dem Urteil des Amtsgerichts", 150, 525, beim("antrag", "beantragst"), size=32),
    z("vom 18.3.2026 für unzulässig zu erklären.“", 150, 572, beim("antrag", "beantragst"), size=32),
    peep_voll("NB_ruhig", X1, BR, FR, "tenor", bis=beim("tenor", "unzulässig")),
    peep_voll("NB_froh", X1, BR, FR, beim("tenor", "unzulässig"), anim="cut"),
    peep_voll("RA_ruhig", X2, BR, FR, "tenor", d=0.2, bis=beim("tenor", "unzulässig")),
    peep_voll("RA_sorge", X2, BR, FR, beim("tenor", "unzulässig"), anim="cut"),
    namensschild("Herr Neubauer", X1, BR, "tenor", GRUEN, d=0.2),
    namensschild("Herr Rademacher", X2, BR, "tenor", GELB, d=0.3),
    ficon("tabler", "gavel", MB, 380, 110, "tenor", fuell=HOLZ, bis="antrag"),
    pl("unzulässig", MB, 160, beim("tenor", "unzulässig"), fill=GRUEN, size=30, anker="m", bis="antrag"),
    ficon("tabler", "file-text", MB, 380, 100, "antrag", fuell=WEISS, anim="cut"),
    pl("Antrag", MB, 160, "antrag", fill=WEISS, size=30, anker="m", anim="cut"),
]))

# J Eilrechtsschutz: einstweilige Einstellung, § 769 ZPO --------------------------------------------------------------------------
PE = "Eilrechtsschutz"
folie([("eil", f"{PE} › einstweilige Einstellung, § 769 ZPO"), ("glaub", f"{PE} › Glaubhaftmachung, § 769 Abs. 1 S. 3 ZPO"),
       ("nr2", f"{PE} › Vorlage bei der Gerichtsvollzieherin, § 775 Nr. 2 ZPO")], rechts_frei([
    *tafel("eil", "Einstweilige Einstellung, § 769 ZPO"),
    z("Die Klage allein hält die Vollstreckung nicht auf.", 110, 175, "eil", "Bold", 34),
    z("Zugleich: Antrag auf einstweilige Einstellung", 110, 245, beim("p769", "zugleich"), "Bold", 34),
    z("Prozessgericht kann einstellen lassen, bis zum Urteil,", 150, 300, beim("p769", "Prozessgericht"), size=32),
    z("gegen oder ohne Sicherheitsleistung (§ 769 Abs. 1 S. 1)", 150, 347, beim("p769", "gegen"), size=32),
    z("Tatsachen glaubhaft machen (§ 769 Abs. 1 S. 3)", 110, 425, "glaub", "Bold", 34),
    z("Überweisungsbeleg und eidesstattliche Versicherung", 150, 480, "glaub2", size=32),
    fund("§ 294 Abs. 1 ZPO", 150, 527, "glaub2"),
    z("Beschluss der Gerichtsvollzieherin vorlegen:", 110, 600, "nr2", "Bold", 34),
    z("sie stellt ein, § 775 Nr. 2 ZPO", 150, 655, beim("nr2", "stellt"), size=32),
    peep_voll("KM_ruhig", X1, BR, FR, "eil", bis="p769"),
    peep_voll("KM_froh", X1, BR, FR, "p769", anim="cut", bis="nr2"),
    peep_voll("KM_ruhig", X1, BR, FR, "nr2", anim="cut"),
    peep_voll("NB_sorge", X2, BR, FR, "eil", d=0.2, bis="glaub"),
    peep_voll("NB_ruhig", X2, BR, FR, "glaub", anim="cut", bis=beim("nr2", "stellt")),
    peep_voll("NB_froh", X2, BR, FR, beim("nr2", "stellt"), anim="cut"),
    namensschild("RAin Kellermann", X1, BR, "eil", LILA, d=0.2),
    namensschild("Herr Neubauer", X2, BR, "eil", GRUEN, d=0.3),
    ficon("tabler", "hourglass", MB, 380, 90, "eil", fuell=GELB, bis="p769"),
    pl("Klage allein: kein Stopp", MB, 160, "eil", fill=ROTHELL, size=26, anker="m", bis="p769"),
    ficon("tabler", "hand-stop", MB, 380, 100, "p769", fuell=GELB, anim="cut", bis="glaub"),
    pl("§ 769: einstweilen einstellen", MB, 160, beim("p769", "einstweilige"), fill=GELB, size=26, anker="m", anim="cut", bis="glaub"),
    ficon("tabler", "receipt", MB, 380, 90, "glaub", fuell=WEISS, anim="cut", bis="nr2"),
    pl("glaubhaft machen", MB, 160, "glaub", fill=WEISS, size=28, anker="m", anim="cut", bis="nr2"),
    ficon("tabler", "file-text", MB, 380, 90, "nr2", fuell=WEISS, anim="cut"),
    pl("Beschluss vorlegen", MB, 160, beim("nr2", "Beschluss"), fill=BLAU, size=28, anker="m", anim="cut"),
]))

# K Zahlungsbeleg, § 775 Nr. 5 ZPO; § 775 Nr. 4, § 776, § 770 ----------------------------------------------------------------------
folie([("p775", f"{PE} › Zahlungsbeleg, § 775 Nr. 5 ZPO"), ("nr4", f"{PE} › Quittung, § 775 Nr. 4 ZPO"),
       ("p776", f"{PE} › Maßregeln bleiben, § 776 ZPO"), ("titel", f"{PE} › Titel bleibt"), ("p770", f"{PE} › § 770 ZPO")],
      rechts_frei([
    *tafel("p775", "Zahlungsbeleg, § 775 Nr. 5 ZPO"),
    *wortlaut(110, 175, 1040, 235, "wl775", [
        [("„Die Zwangsvollstreckung ist ", 0), ("einzustellen", "a"), (" oder zu beschränken: …", 0)],
        [("5. wenn der Einzahlungs- oder ", 0), ("Überweisungsnachweis einer Bank", "b")],
        [("oder Sparkasse vorgelegt wird, aus dem sich ergibt, dass der zur", 0)],
        [("Befriedigung des Gläubigers erforderliche Betrag zur Auszahlung an", 0)],
        [("den Gläubiger oder ", 0), ("auf dessen Konto", "c"), (" eingezahlt oder überwiesen worden ist.“", 0)],
    ], 27, {"a": beim("wl775", "einzustellen"), "b": beim("wl775", "Überweisungsnachweis"), "c": beim("wl775", "Konto")},
        "§ 775 Nr. 5 ZPO"),
    z("Quittung von Herrn Rademacher: § 775 Nr. 4 ZPO", 110, 490, "nr4", "Bold", 32),
    z("Achtung: Maßregeln bleiben einstweilen bestehen (§ 776 S. 2)", 110, 555, "p776", "Bold", 32),
    z("Urteil bleibt Titel – Vollstreckbarkeit beseitigt erst die Klage", 110, 620, "titel", "Bold", 32),
    z("§ 770: Im Urteil kann das Gericht die Anordnung", 110, 700, "p770", size=32),
    z("bestätigen, ändern oder aufheben.", 150, 747, beim("p770", "bestätigen"), size=32),
    peep_voll("NB_froh", X1, BR, FR, "p775", bis="p776"),
    peep_voll("NB_sorge", X1, BR, FR, "p776", anim="cut", bis="p770"),
    peep_voll("NB_ruhig", X1, BR, FR, "p770", anim="cut"),
    peep_voll("GV_ruhig", X2, BR, FR, "p775", d=0.2, bis="p776"),
    peep_voll("GV_denkt", X2, BR, FR, "p776", anim="cut"),
    namensschild("Herr Neubauer", X1, BR, "p775", GRUEN, d=0.2),
    namensschild("Gerichtsvollzieherin", X2 - 30, BR, "p775", TUERKIS, d=0.3),
    ficon("tabler", "receipt", MB, 380, 90, "p775", fuell=WEISS, bis="nr4"),
    pl("Bankbeleg", MB, 160, "p775", fill=GRUEN, size=30, anker="m", bis="nr4"),
    ficon("tabler", "file-invoice", MB, 380, 90, "nr4", fuell=WEISS, anim="cut", bis="p776"),
    pl("Quittung", MB, 160, beim("nr4", "Quittung"), fill=WEISS, size=30, anker="m", anim="cut", bis="p776"),
    ficon("tabler", "lock", MB, 380, 90, "p776", fuell=GELB, anim="cut", bis="titel"),
    pl("bleiben bestehen", MB, 160, beim("p776", "bleiben"), fill=GELB, size=28, anker="m", anim="cut", bis="titel"),
    ficon("tabler", "file-certificate", MB, 380, 100, "titel", fuell=WEISS, anim="cut", bis="p770"),
    pl("Titel bleibt", MB, 160, "titel", fill=PINK, size=28, anker="m", anim="cut", bis="p770"),
    ficon("tabler", "gavel", MB, 380, 100, "p770", fuell=HOLZ, anim="cut"),
    pl("§ 770", MB, 160, "p770", fill=WEISS, size=30, anker="m", anim="cut"),
]))

# L Klausurtipp (Lexi) -------------------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · das richtige Datum"), ("tipp3", "Klausurtipp · Klage und Eilantrag")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Präklusion: das richtige Datum prüfen", 200, 200, beim("tipp", "Prüfe"), "Bold", 34),
    z("Es zählt der Schluss der mündlichen Verhandlung,", 240, 265, beim("tipp", "Es"), size=34),
    z("nicht der Tag der Verkündung.", 240, 320, beim("tipp", "nicht"), size=34),
    z("Zahlung zwischen Verhandlung und Urteil:", 200, 420, "tipp2", "Bold", 34),
    ok(255, 497, beim("tipp2", "nicht"), gr=20),
    z("nicht ausgeschlossen", 290, 475, beim("tipp2", "nicht"), size=34),
    z("Anwaltsklausur: Klage und Eilantrag zusammen", 200, 580, "tipp3", "Bold", 34),
    *redet("LX_warnt", LXX, BR, FR + 60, "tipp", "sch"),
    namensschild("Lexi", LXX, BR, "tipp", GELB, d=0.2),
])

# M Klausurschema -----------------------------------------------------------------------------------------------------------------
K1, K2, K3 = 150, 210, 260
folie([("sch", "Klausurschema"), ("sA", "Klausurschema › A. Zulässigkeit"), ("sB", "Klausurschema › B. Begründetheit"),
       ("sC", "Klausurschema › Eilantrag")], [
    karte(60, 50, 1800, 900, "sch"),
    titel("Klausurschema: Vollstreckungsabwehrklage, § 767 ZPO", 110, 90, "sch", 50),
    z("A. Zulässigkeit", K1, 180, "sA", "ExtraBold", 38, rechts=1820),
    z("1. Statthaftigkeit: materielle Einwendung gegen den titulierten Anspruch", K2, 240, "s1", "Bold", 34, rechts=1820),
    z("2. Zuständigkeit: Prozessgericht des ersten Rechtszuges, ausschließlich (§ 802 ZPO)", K2, 300, "s2", "Bold", 34, rechts=1820),
    z("3. Rechtsschutzbedürfnis: solange der Gläubiger den Titel hat", K2, 360, "s3", "Bold", 34, rechts=1820),
    z("B. Begründetheit", K1, 450, "sB", "ExtraBold", 38, rechts=1820),
    z("1. Einwendung gegen den Anspruch, hier: Erfüllung (§ 362 BGB)", K2, 510, "sb1", "Bold", 34, rechts=1820),
    z("2. keine Präklusion nach § 767 Abs. 2", K2, 570, "sb2", "Bold", 34, rechts=1820),
    z("und Abs. 3 ZPO", K2 + round(F("Bold", 34).getlength("2. keine Präklusion nach § 767 Abs. 2 ")), 570, "sb3", "Bold", 34, rechts=1820),
    fb(K1, 660, 1600, 90, GELB, "sC", [("Daneben: Antrag auf einstweilige Einstellung, § 769 ZPO", "Bold", 34, INK)]),
])

# N Merksatz (Lexi) ---------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Zahlung nach der letzten", 0)], [("mündlichen Verhandlung:", 0)], [("Vollstreckungsabwehrklage", "a"), (".", 0)]],
                750, 300, 46, "merke", {"a": beim("merke", "Vollstreckungsabwehrklage")}),
    *markertext([[("Bis zum Urteil:", 0)], [("einstweilige Einstellung", "b"), (".", 0)]], 750, 560, 46, "m2",
                {"b": beim("m2", "einstweilige")}),
    *redet("LX_erklaert", 1680, 960, 690, "merke", lexi_bis_ende("merke")),
    namensschild("Lexi", 1680, 960, "merke", GELB, d=0.2),
])
