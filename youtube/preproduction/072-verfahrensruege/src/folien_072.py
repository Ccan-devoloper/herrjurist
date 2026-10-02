"""Folge 072 · Verfahrensrüge § 344 II 2 StPO: Warum so viele scheitern – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A Am Bundesgerichtshof (Hook: Revisionsbegründung ohne Antrag und Beschluss), B Rückblick in
die Kanzlei (Urteil, Beweisantrag, Ablehnungsbeschluss, „Darauf verweise ich“), C Zurück am BGH (Frist abgelaufen, Frage),
D Sachverhalt, E Verfahrensrüge (Wortlautkarten § 344 II 1 und 2 StPO), F Maßstab (Wortlautkarte BGH 1 StR 481/24 Rn. 9),
G Checkliste 1–3 (Antrag/Beschluss, Verweise, verschwiegene Umstände), H Checkliste 4–6 (Beruhen, Frist, Widerspruch),
I Ergebnis im Fall, J Korrigierte Fassung (Verfahrenstatsachen – Rechtsfehler – Beruhen, Klausurkonvention),
K Klausurtipp (Lexi), L Schema, M Merksatz (Lexi).
Geräusche nur bei sichtbarer Handlung: die Akte landet auf dem Richtertisch (A), Rechtsanwältin Hellwig tippt den Verweis (B);
Freesound CC0."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont

bausteine.FIGORDNER = "op_072/"
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


# --- Eigene Hilfsfunktion (wie Folge 054/060): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ---------------
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


# A Fall: am Bundesgerichtshof -----------------------------------------------------------------------------------------------
RX = 1600                               # Richter (blickt nach links zum Schriftsatz)
RIa = ("RI_redet", RX, BODEN, FH)


def bgh_zimmer(cue):
    """Richterzimmer am BGH: Bodenlinie, Schreibtisch mit Lampe, Aktenstapel (A und C)."""
    return [hart(linienzug([(60, BODEN), (1860, BODEN)], cue, breite=7, farbe=INK)),
            ficon("tabler", "desk", 1120, BODEN - 2, 420, cue, fuell=HOLZ, anim="cut"),
            ficon("tabler", "lamp", 1260, 702, 90, cue, fuell=GELB, anim="cut"),
            ficon("tabler", "files", 990, 702, 100, cue, fuell=WEISS, anim="cut")]


akte = szene(bewegt(ficon("tabler", "file-text", 1120, 702, 90, "akte", fuell=WEISS), "akte", ("akte", 0.35), 0, -240),
             "072akte*", 1.0, versatz=0.25)

folie([(NULL, "Fall · Am Bundesgerichtshof"), ("zitat", "Fall · Die Revisionsbegründung"),
       ("r1", "Fall · Wo ist der Beschluss?")], [
    *bgh_zimmer(NULL),
    pl("Bundesgerichtshof, Karlsruhe", 70, 40, NULL, fill=GELB, size=40),
    peep_voll("RI_ruhig", RX, BODEN, FH, NULL, bis="zitat"),
    peep_voll("RI_denkt", RX, BODEN, FH, "zitat", anim="cut", bis="r1"),
    *redet("RI_redet", RX, BODEN, FH, "r1", "zurueck"),
    namensschild("Richter am Bundesgerichtshof", RX - 40, BODEN, NULL, WEISS),
    pl("Strafsenat", RX, 330, beim("akte", "Strafsenats"), fill=WEISS, size=28, anker="m", bis="r1"),
    akte,
    karte(70, 150, 790, 520, beim("akte", "Revisionsbegründung"), fill=HELL, rund=10, schatten=6),
    z("Revisionsbegründung für Herrn Bachmann", 105, 175, beim("akte", "Revisionsbegründung"), "ExtraBold", 32, rechts=840),
    z("„Die Ablehnung des Beweisantrags auf", 105, 255, "zitat", size=30, rechts=840),
    z("Vernehmung der Zeugin Haase war", 105, 297, "zitat", size=30, rechts=840),
    z("rechtsfehlerhaft.", 105, 339, "zitat", size=30, rechts=840),
    z("Wegen der Einzelheiten wird auf das", 105, 405, "zitat2", size=30, rechts=840),
    z("Protokoll verwiesen.“", 105, 447, "zitat2", size=30, rechts=840),
    blase("sprech", 700, 220, "r1", 1180, 210, inhalt=["Und wo sind der Antrag", "und der Ablehnungsbeschluss?"],
          textsize=32, figur=RIa, bis="zurueck"),
    pl("Antrag?", 230, 560, beim("r1", "Antrag"), fill=ROTHELL, size=32, anker="m"),
    pl("Ablehnungsbeschluss?", 560, 560, beim("r1", "Ablehnungsbeschluss"), fill=ROTHELL, size=32, anker="m"),
])

# B Rückblick: in der Kanzlei ---------------------------------------------------------------------------------------------------
HX, BX = 1290, 1690                     # Rechtsanwältin Hellwig (blickt nach rechts), Herr Bachmann (blickt nach links)
HWb = ("HW_redet_r", HX, BODEN, FH)
BAb = ("BA_redet", BX, BODEN, FH)
folie([("zurueck", "Fall · Rückblick: in der Kanzlei"), ("lg", "Fall · Das Urteil des Landgerichts"),
       ("antrag", "Fall · Der Beweisantrag"), ("beschl", "Fall · Der Ablehnungsbeschluss"),
       ("b1", "Fall · Die Revisionsbegründung")], [
    hart(linienzug([(60, BODEN), (1860, BODEN)], "zurueck", breite=7, farbe=INK)),
    pl("Rückblick: 4 Wochen vorher", 70, 40, "zurueck", fill=BLAU, size=40, anim="cut"),
    ficon("tabler", "desk", 965, BODEN - 2, 330, "zurueck", fuell=HOLZ, anim="cut"),
    ficon("tabler", "device-laptop", 965, 735, 150, "zurueck", fuell=BLAUHELL, anim="cut"),
    peep_voll("HW_ruhig_r", HX, BODEN, FH, "zurueck", anim="cut", bis="b1"),
    peep_voll("HW_froh_r", HX, BODEN, FH, "b1", anim="cut", bis="h1"),
    *redet("HW_redet_r", HX, BODEN, FH, "h1", "frist"),
    namensschild("Rechtsanwältin Hellwig", HX - 30, BODEN, "zurueck", LILA),
    peep_voll("BA_ruhig", BX, BODEN, FH, "zurueck", anim="cut", bis="lg"),
    peep_voll("BA_sorge", BX, BODEN, FH, "lg", anim="cut", bis="beschl"),
    peep_voll("BA_muede", BX, BODEN, FH, "beschl", anim="cut", bis="b1"),
    *redet("BA_redet", BX, BODEN, FH, "b1", "h1"),
    peep_voll("BA_denkt", BX, BODEN, FH, "h1", anim="cut"),
    namensschild("Herr Bachmann", BX + 20, BODEN, "zurueck", GRUEN),
    pl("Verteidigerin", HX, 330, beim("zurueck", "Rechtsanwältin"), fill=LILA, size=28, anker="m", bis="b1"),
    pl("Mandant", BX, 330, beim("lg", "Mandanten"), fill=WEISS, size=28, anker="m", bis="b1"),
    # Karte 1: das Urteil
    karte(70, 140, 690, 330, beim("lg", "verurteilt"), fill=HELL, rund=10, schatten=6),
    z("Urteil des Landgerichts: Betrug", 105, 160, beim("lg", "verurteilt"), "ExtraBold", 32, rechts=750),
    ficon("tabler", "car", 140, 330, 80, "auto", fuell=PINK),
    z("verkauft mit 60.000 km", 205, 255, "auto", "Bold", 30, rechts=750),
    ficon("tabler", "gauge", 140, 430, 70, beim("auto", "Tatsächlich"), fuell=ROT),
    z("tatsächlich: 160.000 km", 205, 365, beim("auto", "Tatsächlich"), "Bold", 30, rechts=750),
    # Karte 2: Antrag und Beschluss
    karte(70, 500, 690, 350, "antrag", fill=WEISS, rund=10, schatten=6),
    z("Beweisantrag: Zeugin Frau Haase,", 105, 520, "antrag", "ExtraBold", 30, rechts=750),
    z("die Vorbesitzerin: Der Tacho zeigte", 105, 562, beim("antrag", "Vorbesitzerin"), size=30, rechts=750),
    z("bei der Übergabe schon 60.000 km.", 105, 604, beim("antrag", "dass"), size=30, rechts=750),
    nein(125, 700, "beschl", gr=18),
    z("Beschluss: abgelehnt –", 160, 680, "beschl", "ExtraBold", 30, rechts=750),
    z("für die Entscheidung ohne Bedeutung", 160, 722, beim("beschl", "Tatsache"), "Bold", 30, rechts=750),
    fund("§ 244 Abs. 3 S. 3 Nr. 2 StPO", 160, 770, beim("beschl", "Tatsache"), rechts=750),
    blase("sprech", 760, 220, "b1", 1290, 200, inhalt=["Reicht es, wenn wir die Ablehnung", "in der Revision nur rügen?"],
          textsize=30, figur=BAb, bis="h1"),
    blase("sprech", 700, 220, "h1", 1520, 200, inhalt=["Das steht doch alles im Protokoll.", "Darauf verweise ich."],
          textsize=30, figur=HWb, bis="frist"),
    szene(pl("„… auf das Protokoll verwiesen.“", 965, 585, beim("h1", "verweise"), fill=BLAUHELL, size=26, anker="m"),
          "072tippen*", 1.0),
])

# C Zurück am Bundesgerichtshof ------------------------------------------------------------------------------------------------
folie([("frist", "Fall · Die Begründungsfrist ist abgelaufen"), ("frage", "Fall · Die Frage")], [
    *bgh_zimmer("frist"),
    pl("Zurück am Bundesgerichtshof", 70, 40, "frist", fill=GELB, size=40, anim="cut"),
    ficon("tabler", "file-text", 1120, 702, 90, "frist", fuell=WEISS, anim="cut"),
    peep_voll("RI_denkt", RX, BODEN, FH, "frist", anim="cut", bis="frage"),
    peep_voll("RI_streng", RX, BODEN, FH, "frage", anim="cut"),
    namensschild("Richter am Bundesgerichtshof", RX - 40, BODEN, "frist", WEISS, anim="cut"),
    ficon("tabler", "calendar-x", 450, 420, 130, "frist", fuell=ROT),
    pl("Begründungsfrist abgelaufen", 450, 470, beim("frist", "Begründungsfrist"), fill=ROTHELL, size=34, anker="m"),
    pl("Warum scheitert die Verfahrensrüge?", 1000, 160, "frage", fill=WEISS, size=34, anker="m"),
    pl("Wie hätte sie die Rüge schreiben müssen?", 1000, 250, "frage2", fill=GELB, size=34, anker="m"),
])

# D Sachverhalt ------------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    glyphen("Das Landgericht verurteilt Herrn Bachmann wegen Betrugs: Er hatte einen Gebrauchtwagen mit angeblich 60.000 km "
            "verkauft; tatsächlich waren es 160.000 km. In der Hauptverhandlung beantragte seine Verteidigerin, "
            "Rechtsanwältin Hellwig, die Vorbesitzerin Frau Haase als Zeugin dafür zu vernehmen, dass der Tacho schon bei der "
            "Übergabe an Herrn Bachmann 60.000 km zeigte. Die Kammer lehnte den Antrag durch Beschluss ab: Die Tatsache sei für "
            "die Entscheidung ohne Bedeutung."),
    glyphen("In der Revisionsbegründung schreibt Rechtsanwältin Hellwig: „Die Ablehnung des Beweisantrags auf Vernehmung der "
            "Zeugin Haase war rechtsfehlerhaft. Wegen der Einzelheiten wird auf das Protokoll verwiesen.“ Den Antrag und den "
            "Ablehnungsbeschluss gibt sie nicht wieder. Die Begründungsfrist ist inzwischen abgelaufen."),
], "Hat die Verfahrensrüge Erfolg – und wie wäre sie richtig?")

# E Verfahrensrüge: § 344 II StPO -------------------------------------------------------------------------------------------------
PV = "Verfahrensrüge"
folie([("sach", "Sachrüge › prüft nur das Urteil"), ("verf", f"{PV} › Vorgang der Hauptverhandlung"),
       ("p344", f"{PV} › § 344 Abs. 2 Satz 1 StPO"), ("p344b", f"{PV} › § 344 Abs. 2 Satz 2 StPO")], rechts_frei([
    *tafel("sach", "Verfahrensrüge: § 344 Abs. 2 StPO", size=46),
    z("Sachrüge: 1 Satz genügt, aber sie prüft nur das Urteil.", 110, 180, "sach", "Bold", 32),
    z("Ablehnung des Beweisantrags: ein Vorgang der", 110, 240, "verf", "Bold", 32),
    z("Hauptverhandlung, also Verfahrensrüge", 110, 285, beim("verf", "Verfahrensrüge"), "Bold", 32),
    *wortlaut(110, 360, 1040, 150, "p344", [
        [("„Aus der Begründung muß hervorgehen, ob das Urteil", 0)],
        [("wegen Verletzung einer Rechtsnorm ", 0), ("über das Verfahren", "v")],
        [("oder wegen Verletzung einer ", 0), ("anderen Rechtsnorm", "a"), (" angefochten wird.", 0)],
    ], 30, {"v": beim("p344", "Verfahren"), "a": beim("p344", "andere")}, "§ 344 Abs. 2 S. 1 StPO"),
    *wortlaut(110, 590, 1040, 110, "p344b", [
        [("Ersterenfalls müssen die ", 0), ("den Mangel enthaltenden", "m")],
        [("Tatsachen", "t"), (" angegeben werden.“", 0)],
    ], 30, {"m": beim("p344b", "Mangel"), "t": beim("p344b", "Tatsachen")}, "§ 344 Abs. 2 S. 2 StPO"),
    peep_voll("HW_ruhig", X1, BR, FR, "sach", bis="p344b"),
    peep_voll("HW_denkt", X1, BR, FR, "p344b", anim="cut"),
    peep_voll("BA_ruhig", X2, BR, FR, "sach", d=0.2, bis="verf"),
    peep_voll("BA_denkt", X2, BR, FR, "verf", anim="cut"),
    namensschild("Rechtsanwältin Hellwig", X1 - 60, BR, "sach", LILA, d=0.2),
    namensschild("Herr Bachmann", X2 + 20, BR, "sach", GRUEN, d=0.3),
    ficon("tabler", "file-text", MB, 380, 100, "sach", fuell=GRUEN, bis="verf"),
    pl("Sachrüge: nur das Urteil", MB, 160, "sach", fill=GRUEN, size=28, anker="m", bis="verf"),
    ficon("tabler", "building-bank", MB, 380, 110, "verf", fuell=BLAU, anim="cut", bis="p344b"),
    pl("Verfahrensrüge", MB, 160, "verf", fill=BLAU, size=30, anker="m", anim="cut", bis="p344b"),
    ficon("tabler", "file-pencil", MB, 380, 100, "p344b", fuell=GELB, anim="cut"),
    pl("Tatsachen angeben", MB, 160, beim("p344b", "Tatsachen"), fill=GELB, size=30, anker="m"),
]))

# F Der Maßstab --------------------------------------------------------------------------------------------------------------------
PM = "Maßstab"
folie([("mass", PM), ("bgh", f"{PM} › allein anhand der Begründungsschrift"), ("allein", f"{PM} › keine Suche in den Akten"),
       ("wenn", f"{PM} › als stimme der Vortrag")], rechts_frei([
    *tafel("mass", "Der Maßstab"),
    *wortlaut(110, 180, 1040, 245, "bgh", [
        [("„Der Revisionsführer muss dabei die den Mangel", 0)],
        [("enthaltenden Tatsachen so vollständig und genau angeben,", 0)],
        [("dass das Revisionsgericht ", 0), ("allein aufgrund der", "a")],
        [("Begründungsschrift", "a2"), (" prüfen kann, ob ein Verfahrensfehler", 0)],
        [("vorliegt, ", 0), ("wenn die behaupteten Tatsachen bewiesen werden", "b"), (" …“", 0)],
    ], 30, {"a": beim("bgh", "allein"), "a2": beim("bgh", "allein"),
            "b": beim("bgh", "bewiesen")}, "BGH, Urt. v. 15.5.2025 – 1 StR 481/24, Rn. 9"),
    z("„Allein“: Der Senat sucht nichts in den Akten zusammen.", 110, 500, "allein", "Bold", 32),
    fund("vgl. BGH, Urt. v. 20.5.2026 – 2 StR 57/25, Rn. 47", 150, 548, beim("allein", "Senat")),
    z("Er prüft so, als stimme dein Vortrag.", 110, 630, "wenn", "Bold", 32),
    z("Ob er stimmt: erst eine Frage der Begründetheit", 150, 680, beim("wenn", "Ob"), size=32),
    peep_voll("HW_ruhig", X1, BR, FR, "mass", bis="allein"),
    peep_voll("HW_sorge", X1, BR, FR, "allein", anim="cut"),
    peep_voll("RI_ruhig", X2, BR, FR, "mass", d=0.2, bis="bgh"),
    peep_voll("RI_denkt", X2, BR, FR, "bgh", anim="cut", bis="wenn"),
    peep_voll("RI_ruhig", X2, BR, FR, "wenn", anim="cut"),
    namensschild("Rechtsanwältin Hellwig", X1 - 60, BR, "mass", LILA, d=0.2),
    namensschild("Richter am BGH", X2 + 10, BR, "mass", WEISS, d=0.3),
    ficon("tabler", "file-search", MB, 380, 100, "mass", fuell=WEISS, bis="allein"),
    pl("nur die Begründungsschrift", MB, 160, beim("bgh", "Begründungsschrift"), fill=GELB, size=28, anker="m", bis="allein"),
    ficon("tabler", "folders", MB, 380, 100, "allein", fuell=WEISS, anim="cut", bis="wenn"),
    pl("keine Suche in den Akten", MB, 160, "allein", fill=ROTHELL, size=28, anker="m", anim="cut", bis="wenn"),
    ficon("tabler", "scale", MB, 380, 110, "wenn", fuell=GELB, anim="cut"),
    pl("als stimme der Vortrag", MB, 160, "wenn", fill=WEISS, size=28, anker="m", anim="cut", bis=beim("wenn", "Ob")),
    pl("dann: Begründetheit", MB, 160, beim("wenn", "Ob"), fill=BLAU, size=28, anker="m", anim="cut"),
]))

# G Checkliste 1–3 ---------------------------------------------------------------------------------------------------------------
PC = "Checkliste"
folie([("liste", f"{PC}: typische Fehler"), ("c1", f"{PC} › 1. Antrag und Beschluss fehlen"),
       ("c2", f"{PC} › 2. Verweise statt Vortrag"), ("c3", f"{PC} › 3. Verschwiegene Umstände")], rechts_frei([
    *tafel("liste", "Checkliste: typische Fehler"),
    z("1. Antrag und Beschluss fehlen", 110, 180, "c1", "ExtraBold", 34),
    z("Antrag und Ablehnungsbegründung vollständig mitteilen,", 150, 230, "c1b", size=30),
    z("im Wortlaut oder in eigenen Worten", 150, 270, beim("c1b", "Wortlaut"), size=30),
    fund("vgl. BGH 2 StR 281/25, Rn. 14; 3 StR 167/14, Rn. 13", 150, 312, beim("c1b", "Wortlaut")),
    z("2. Verweise statt Vortrag", 110, 380, "c2", "ExtraBold", 34),
    nein(170, 450, beim("c2b", "genügt"), gr=18),
    z("Verweis auf Protokoll oder Akten genügt nicht", 200, 430, "c2b", size=30),
    z("wörtlich oder als Abschrift in die Begründung", 200, 470, "c2c", size=30),
    fund("vgl. BGH 3 StR 167/14, Rn. 12; 2 StR 57/25, Rn. 47", 200, 512, "c2c"),
    z("3. Verschwiegene Umstände", 110, 580, "c3", "ExtraBold", 34),
    z("auch vortragen, was gegen die Rüge spricht", 150, 630, "c3b", size=30),
    nein(170, 690, beim("c3c", "unzulässig"), gr=18),
    z("Ungünstiges weggelassen: Rüge unzulässig", 200, 670, beim("c3c", "unzulässig"), size=30),
    fund("vgl. BGH, Urt. v. 22.5.2025 – 4 StR 576/24, Rn. 11", 200, 712, beim("c3c", "unzulässig")),
    peep_voll("HW_ruhig", X1, BR, FR, "liste", bis="c1c"),
    peep_voll("HW_sorge", X1, BR, FR, "c1c", anim="cut", bis="c2b"),
    peep_voll("HW_schreck", X1, BR, FR, "c2b", anim="cut", bis="c3"),
    peep_voll("HW_denkt", X1, BR, FR, "c3", anim="cut"),
    peep_voll("RI_ruhig", X2, BR, FR, "liste", d=0.2, bis="c1c"),
    peep_voll("RI_streng", X2, BR, FR, "c1c", anim="cut", bis="c3"),
    peep_voll("RI_ruhig", X2, BR, FR, "c3", anim="cut"),
    namensschild("Rechtsanwältin Hellwig", X1 - 60, BR, "liste", LILA, d=0.2),
    namensschild("Richter am BGH", X2 + 10, BR, "liste", WEISS, d=0.3),
    ficon("tabler", "list-check", MB, 380, 100, "liste", fuell=WEISS, bis="c1"),
    pl("6 typische Fehler", MB, 160, "liste", fill=WEISS, size=28, anker="m", bis="c1"),
    ficon("tabler", "file-x", MB, 380, 100, "c1", fuell=ROT, anim="cut", bis="c2"),
    pl("Antrag und Beschluss?", MB, 160, "c1", fill=WEISS, size=28, anker="m", anim="cut", bis="c1c"),
    pl("bei Hellwig: fehlt beides", MB, 160, "c1c", fill=ROTHELL, size=28, anker="m", anim="cut",
       bis=beim("c1c", "Ohne")),
    pl("Senat kann nicht prüfen", MB, 160, beim("c1c", "Ohne"), fill=ROTHELL, size=28, anker="m", anim="cut", bis="c2"),
    ficon("tabler", "link", MB, 380, 100, "c2", fuell=WEISS, anim="cut", bis="c2c"),
    pl("Verweis genügt nicht", MB, 160, beim("c2b", "genügt"), fill=ROTHELL, size=28, anker="m", bis="c2c"),
    ficon("tabler", "file-text", MB, 380, 100, "c2c", fuell=GRUEN, anim="cut", bis="c3"),
    pl("Abschrift hinein", MB, 160, "c2c", fill=GRUEN, size=28, anker="m", anim="cut", bis="c3"),
    ficon("tabler", "eye-off", MB, 380, 100, "c3", fuell=WEISS, anim="cut"),
    pl("nichts weglassen", MB, 160, "c3b", fill=GELB, size=28, anker="m"),
]))

# H Checkliste 4–6 -------------------------------------------------------------------------------------------------------------
folie([("c4", f"{PC} › 4. Das Beruhen"), ("c5", f"{PC} › 5. Die Frist, § 345 Abs. 1 StPO"),
       ("c6", f"{PC} › 6. Der Widerspruch")], rechts_frei([
    *tafel("c4", "Checkliste: typische Fehler"),
    z("1. Antrag und Beschluss fehlen · 2. Verweise statt Vortrag", 110, 175, "c4", size=28, farbe=TEXT),
    z("3. Verschwiegene Umstände", 110, 212, "c4", size=28, farbe=TEXT),
    z("4. Das Beruhen", 110, 280, "c4", "ExtraBold", 34),
    z("grundsätzlich nichts dazu nötig", 150, 330, "c4b", size=30),
    z("nicht auf der Hand: Tatsachen zum Beruhen vortragen", 150, 370, "c4c", size=30),
    fund("vgl. BGH, Urt. v. 15.5.2025 – 1 StR 481/24, Rn. 9", 150, 412, "c4c"),
    z("5. Die Frist", 110, 475, "c5", "ExtraBold", 34),
    z("alle Tatsachen innerhalb der Begründungsfrist,", 150, 525, "c5b", size=30),
    z("§ 345 Abs. 1 StPO", 150, 565, beim("c5b", "Paragraf"), size=30),
    nein(170, 625, beim("c5c", "rettet"), gr=18),
    z("später Nachgereichtes rettet die Rüge nicht", 200, 605, beim("c5c", "rettet"), size=30),
    fund("vgl. BGH 1 StR 544/09, Rn. 20; 2 StR 189/21, Rn. 5; § 352 Abs. 1 StPO", 200, 647, beim("c5c", "rettet")),
    z("6. Der Widerspruch", 110, 710, "c6", "ExtraBold", 34),
    z("rechtzeitigen Widerspruch mitteilen, etwa gegen", 150, 760, beim("c6", "Widerspruch"), size=30),
    z("die Verwertung einer Aussage ohne Belehrung", 150, 800, beim("c6", "Verwertung"), size=30),
    fund("vgl. BGH, Urt. v. 6.10.2016 – 2 StR 46/15, Rn. 14", 150, 842, beim("c6", "gehört")),
    peep_voll("HW_ruhig", X1, BR, FR, "c4", bis="c5c"),
    peep_voll("HW_schreck", X1, BR, FR, "c5c", anim="cut", bis="c6"),
    peep_voll("HW_denkt", X1, BR, FR, "c6", anim="cut"),
    peep_voll("RI_ruhig", X2, BR, FR, "c4", d=0.2, bis="c5c"),
    peep_voll("RI_streng", X2, BR, FR, "c5c", anim="cut", bis="c6"),
    peep_voll("RI_denkt", X2, BR, FR, "c6", anim="cut"),
    namensschild("Rechtsanwältin Hellwig", X1 - 60, BR, "c4", LILA, d=0.2),
    namensschild("Richter am BGH", X2 + 10, BR, "c4", WEISS, d=0.3),
    ficon("tabler", "scale", MB, 380, 110, "c4", fuell=GELB, bis="c5"),
    pl("Beruhen", MB, 160, "c4", fill=WEISS, size=30, anker="m", bis="c4c"),
    pl("nicht auf der Hand?", MB, 160, "c4c", fill=GELB, size=28, anker="m", anim="cut", bis="c5"),
    ficon("tabler", "calendar-x", MB, 380, 100, "c5", fuell=ROT, anim="cut", bis="c6"),
    pl("Begründungsfrist", MB, 160, "c5", fill=WEISS, size=30, anker="m", anim="cut", bis="c5c"),
    pl("nicht mehr nachreichen", MB, 160, beim("c5c", "nachreichen"), fill=ROTHELL, size=28, anker="m", bis="c6"),
    ficon("tabler", "hand-stop", MB, 380, 100, "c6", fuell=WEISS, anim="cut"),
    pl("Widerspruch", MB, 160, beim("c6", "Widerspruch"), fill=WEISS, size=30, anker="m"),
]))

# I Ergebnis im Fall --------------------------------------------------------------------------------------------------------------
PE = "Ergebnis"
folie([("erg", f"{PE} › Verfahrensrüge unzulässig"), ("offen", f"{PE} › Begründetheit nicht mehr entschieden")],
      rechts_frei([
    *tafel("erg", "Ergebnis im Fall"),
    z("Für Herrn Bachmann:", 110, 185, "erg", "Bold", 34),
    fb(110, 250, 1040, 110, ROTHELL, beim("erg", "Verfahrensrüge"), [("Die Verfahrensrüge ist unzulässig.", "ExtraBold", 36, INK)]),
    fund("§ 344 Abs. 2 S. 2 StPO: Antrag und Ablehnungsbeschluss fehlen", 150, 380, beim("erg", "unzulässig")),
    z("Ob die Kammer den Antrag zu Recht abgelehnt hat,", 110, 470, "offen", "Bold", 32),
    z("muss der Senat nicht mehr entscheiden.", 110, 515, beim("offen", "muss"), "Bold", 32),
    peep_voll("BA_ruhig", X2, BR, FR, "erg", bis=beim("erg", "unzulässig")),
    peep_voll("BA_sorge", X2, BR, FR, beim("erg", "unzulässig"), anim="cut", bis="offen"),
    peep_voll("BA_muede", X2, BR, FR, "offen", anim="cut"),
    peep_voll("HW_ruhig", X1, BR, FR, "erg", d=0.2, bis=beim("erg", "unzulässig")),
    peep_voll("HW_schreck", X1, BR, FR, beim("erg", "unzulässig"), anim="cut", bis="offen"),
    peep_voll("HW_sorge", X1, BR, FR, "offen", anim="cut"),
    namensschild("Herr Bachmann", X2 + 20, BR, "erg", GRUEN, d=0.2),
    namensschild("Rechtsanwältin Hellwig", X1 - 60, BR, "erg", LILA, d=0.3),
    ficon("tabler", "file-x", MB, 380, 100, beim("erg", "unzulässig"), fuell=ROT, bis="offen"),
    pl("unzulässig", MB, 160, beim("erg", "unzulässig"), fill=ROTHELL, size=30, anker="m", bis="offen"),
    ficon("tabler", "help-circle", MB, 380, 100, "offen", fuell=WEISS, anim="cut"),
    pl("Ablehnung richtig?", MB, 160, "offen", fill=WEISS, size=28, anker="m", anim="cut", bis=beim("offen", "muss")),
    pl("nicht mehr entschieden", MB, 160, beim("offen", "muss"), fill=WEISS, size=28, anker="m", anim="cut"),
]))

# J Korrigierte Fassung (Klausurkonvention) ---------------------------------------------------------------------------------------
PK = "Korrigierte Fassung"
folie([("besser", f"{PK} › Klausurkonvention"), ("k1", f"{PK} › 1. Verfahrenstatsachen"),
       ("k2", f"{PK} › 2. Rechtsfehler, § 244 Abs. 3 StPO"), ("k3", f"{PK} › 3. Beruhen")], rechts_frei([
    *tafel("besser", "So hätte die Rüge aussehen müssen", size=46),
    karte(120, 170, 1030, 620, beim("besser", "Klausurkonvention"), fill=HELL, rund=10, schatten=6),
    z("Klausurkonvention: 3 Schritte", 160, 190, beim("besser", "Klausurkonvention"), "ExtraBold", 32, rechts=1130),
    ok(180, 290, "k1", gr=18),
    z("1. Verfahrenstatsachen", 215, 270, "k1", "ExtraBold", 32, rechts=1130),
    z("Beweisantrag im Wortlaut, wann er gestellt wurde", 215, 315, beim("k1", "Beweisantrag"), size=30, rechts=1130),
    z("Ablehnungsbeschluss im Wortlaut", 215, 355, "k1b", size=30, rechts=1130),
    z("Frau Haase bis zum Urteil nicht vernommen", 215, 395, beim("k1b", "dass"), size=30, rechts=1130),
    ok(180, 490, "k2", gr=18),
    z("2. Rechtsfehler", 215, 470, "k2", "ExtraBold", 32, rechts=1130),
    z("Ablehnung als bedeutungslos verletzt § 244 Abs. 3 StPO", 215, 515, beim("k2", "warum"), size=30, rechts=1130),
    ok(180, 610, "k3", gr=18),
    z("3. Beruhen", 215, 590, "k3", "ExtraBold", 32, rechts=1130),
    z("Urteil wäre möglicherweise anders ausgefallen", 215, 635, beim("k3", "möglicherweise"), size=30, rechts=1130),
    fund("vgl. BGH, Urt. v. 1.7.2021 – 3 StR 518/19, Rn. 94", 215, 680, beim("k3", "möglicherweise"), rechts=1130),
    peep_voll("HW_denkt", XS, BR, FR, "besser", bis="k1"),
    peep_voll("HW_ruhig", XS, BR, FR, "k1", anim="cut", bis="k3"),
    peep_voll("HW_froh", XS, BR, FR, "k3", anim="cut"),
    namensschild("Rechtsanwältin Hellwig", XS, BR, "besser", LILA, d=0.2),
    ficon("tabler", "writing", XS, 380, 100, "besser", fuell=GELB, bis="k1"),
    pl("Klausurkonvention", XS, 160, beim("besser", "Klausurkonvention"), fill=LILA, size=30, anker="m", bis="k1"),
    ficon("tabler", "file-description", XS, 380, 100, "k1", fuell=WEISS, anim="cut", bis="k2"),
    pl("Verfahrenstatsachen", XS, 160, "k1", fill=WEISS, size=30, anker="m", anim="cut", bis="k2"),
    ficon("tabler", "file-x", XS, 380, 100, "k2", fuell=ROT, anim="cut", bis="k3"),
    pl("Rechtsfehler", XS, 160, "k2", fill=ROTHELL, size=30, anker="m", anim="cut", bis="k3"),
    ficon("tabler", "scale", XS, 380, 110, "k3", fuell=GELB, anim="cut"),
    pl("Beruhen", XS, 160, "k3", fill=GELB, size=30, anker="m", anim="cut"),
]))

# K Klausurtipp (Lexi) -----------------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · Lies wie der Senat"), ("tipp3", "Klausurtipp · jede Rüge aus sich heraus")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Lies deine Rüge wie ein Senat,", 200, 200, beim("tipp", "Lies"), "Bold", 36),
    z("der nur diese Seiten hat.", 200, 250, beim("tipp", "der"), "Bold", 36),
    z("Fehlt ein Schriftstück, auf das es ankommt:", 200, 350, "tipp2", size=34),
    z("Es gehört hinein.", 200, 400, beim("tipp2", "gehört"), "Bold", 34),
    ok(220, 525, "tipp3", gr=18),
    z("Jede Verfahrensrüge muss aus sich heraus", 260, 500, "tipp3", "Bold", 34),
    z("verständlich sein, mit eigenem Vortrag.", 260, 550, beim("tipp3", "verständlich"), "Bold", 34),
    fund("vgl. BGH, Urt. v. 20.5.2026 – 2 StR 57/25, Rn. 47", 260, 605, beim("tipp3", "verständlich")),
    *redet("LX_warnt", LXX, BR, FR + 60, "tipp", "sch"),
    namensschild("Lexi", LXX, BR, "tipp", GELB, d=0.2),
])

# L Schema -------------------------------------------------------------------------------------------------------------------------
K1, K2 = 150, 210
folie([("sch", "Schema"), ("s1", "Schema › I. Verfahrenstatsachen"), ("s2", "Schema › II. Rechtsfehler"),
       ("s3", "Schema › III. Beruhen"), ("s4", "Schema › innerhalb der Begründungsfrist")], [
    karte(60, 50, 1800, 900, "sch"),
    titel("Schema: die Verfahrensrüge", 110, 90, "sch", 54),
    z("I. Verfahrenstatsachen", K1, 200, "s1", "Bold", 38, rechts=1820),
    z("vollständig – Anträge und Beschlüsse im Wortlaut – auch was gegen dich spricht", K2, 255,
      beim("s1", "vollständig"), size=32, farbe=TEXT, rechts=1820),
    z("§ 344 Abs. 2 S. 2 StPO", K2, 300, beim("s1", "vollständig"), size=30, farbe=TEXT, rechts=1820),
    z("II. Rechtsfehler", K1, 390, "s2", "Bold", 38, rechts=1820),
    z("mit der verletzten Norm, hier § 244 Abs. 3 StPO", K2, 445, beim("s2", "mit"), size=32, farbe=TEXT, rechts=1820),
    z("III. Beruhen", K1, 535, "s3", "Bold", 38, rechts=1820),
    z("mit Tatsachen, wo es nicht auf der Hand liegt – § 337 Abs. 1 StPO", K2, 590, beim("s3", "mit"), size=32,
      farbe=TEXT, rechts=1820),
    fb(150, 700, 1620, 110, GELB, "s4", [("Alles innerhalb der Begründungsfrist, § 345 Abs. 1 StPO", "ExtraBold", 36, INK)]),
])

# M Merksatz (Lexi) ------------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Bei der Verfahrensrüge liest", 0)], [("der Senat nur deine ", 0), ("Begründung", "a"), (".", 0)]],
                750, 310, 50, "merke", {"a": beim("merke", "Begründung")}),
    *markertext([[("Was dort nicht steht,", 0)], [("prüft er ", 0), ("nicht", "b"), (".", 0)]], 750, 560, 54, "mz",
                {"b": beim("mz", "nicht")}),
    *redet("LX_erklaert", 1680, 960, 690, "merke", lexi_bis_ende("merke")),
    namensschild("Lexi", 1680, 960, "merke", GELB, d=0.2),
])
