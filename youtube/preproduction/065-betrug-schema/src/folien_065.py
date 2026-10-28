"""Folge 065 · Betrug § 263 Schema: Täuschung, Irrtum, Verfügung, Schaden – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A Die Kleinanzeige (Anzeige, Anruf, Vorkasse, Paket, gesprungenes Display), B Sachverhalt,
C Wortlaut § 263 Abs. 1 und Kette, D Täuschung (Tatsachen, ausdrücklich, konkludent), E Abgrenzung Anpreisung, F Irrtum,
G Vermögensverfügung (Abgrenzung Trickdiebstahl), H Schaden (Gesamtsaldierung, Eingehungs-/Erfüllungsschaden),
I Rechnung und Bezifferung, J subjektiver Tatbestand, K Rechtswidrigkeit, Schuld, Ergebnis, L Ausblick, M Klausurtipp (Lexi),
N Prüfschema, O Merksatz (Lexi).
Die Kette Täuschung › Irrtum › Vermögensverfügung › Schaden steht als Leiste oben auf jeder Merkmalstafel (aktuelles Glied
gelb, geprüfte Glieder grün). Keine Anleitung zum Betrügen: gezeigt wird nur, was der Sachverhalt mitteilt.
Geräusche nur bei sichtbarer Handlung: Paket kommt an, Waltraud packt aus (Freesound CC0)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont

bausteine.FIGORDNER = "op_065/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
LILAHELL = (246, 243, 255, 255)
ROTHELL = (253, 232, 228, 255)
GRUENHELL = (232, 247, 233, 255)
GRAU = (205, 205, 210, 255)
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


def tafel(cue, titel_, h=840, fill=WEISS, size=50):
    """Rechtstafel links, rechts bleibt Platz für die Figuren."""
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(glyphen(titel_), 110, 100, cue, size)]


def wortlaut(x, y, w, h, cue, zeilen, size, hl, quelle, quelle_cue=None):
    """Wortlautkarte: wörtliches Zitat (gesetze-im-internet.de, Abruf 02.10.2026) in einer hellen Karte, Fundstelle
    darunter rechts. zeilen = Liste von Token-Listen [(text, Schlüssel|0)], hl = {Schlüssel: Cue} (synchron zum Wort)."""
    for toks in zeilen:
        glyphen("".join(t for t, _ in toks))
    els = [karte(x, y, w, h, cue, fill=(246, 246, 250, 255), rund=18, schatten=6, rand=4)]
    m = markertext(zeilen, x + w / 2, y + 18, size, cue, hl, marker=GELB, lh=1.28)
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


def kb(*a, bis=None, **k):
    """Karte mit Ende (karte() kennt kein bis)."""
    e = karte(*a, **k)
    e.bis = bis
    return e


def fund(text, x, y, cue, **k):
    """Fundstelle (mobil lesbar: 26 px)."""
    return z(text, x, y, cue, size=26, farbe=TEXT, **k)


GLIEDER = ["Täuschung", "Irrtum", "Vermögensverfügung", "Schaden"]


def kette(y, cue, stand, x0=110, size=28, cues=None, bis=None):
    """Kettenleiste Täuschung › Irrtum › Vermögensverfügung › Schaden; stand = Index des aktuellen Glieds
    (geprüfte grün, aktuelles gelb, folgende weiß), stand=4: alle grün. cues: je Glied eigener Cue (Aufbau am Wort)."""
    els, x = [], x0
    for i, g in enumerate(GLIEDER):
        c = cues[i] if cues else cue
        fill = GRUEN if i < stand else (GELB if i == stand else WEISS)
        p = pl(g, x, y, c, fill=fill, size=size, bis=bis)
        els.append(p)
        x = p.x + p.sprite.width + 6
        if i < 3:
            c2 = cues[i + 1] if cues else cue          # Pfeil erscheint mit dem nächsten Glied
            pf = ficon("tabler", "arrow-narrow-right", x + 19, y + p.sprite.height / 2 + 16, 36, c2, bis=bis)
            pf.name = "kettenpfeil"           # Teil der Tafel (nicht rechts_frei-pflichtig)
            els.append(pf)
            x += 44
    assert x - 6 <= 1170, f"Kette zu breit ({x - 6})"
    return els


# --- Eigene Hilfsfunktion (wie Folge 062): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ---------------
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
X1, X2 = 1420, 1720                     # Waltraud (näher an der Tafel), Detlef
MB = (X1 + X2) // 2
FW = ("Waltraud", GRUEN)
FD = ("Detlef", BLAU)


def paar(cue, wa, de, wa_cues=(), de_cues=()):
    """Waltraud (X1) und Detlef (X2) neben der Tafel mit Namensschild; *_cues = [(Cue, Ansicht)] für Mimikwechsel."""
    els = []
    for x, basis, wechsel, (name, farbe), dd in ((X1, wa, wa_cues, FW, 0.0), (X2, de, de_cues, FD, 0.2)):
        folge = [(cue, basis)] + list(wechsel)
        for i, (c, ans) in enumerate(folge):
            bis = folge[i + 1][0] if i + 1 < len(folge) else None
            els.append(peep_voll(ans, x, BR, FR, c, anim=("fade" if i == 0 else "cut"), d=(dd if i == 0 else 0.0), bis=bis))
        els.append(namensschild(name, x, BR, cue, farbe, d=dd + 0.2))
    return els


def symbol(sets, name, c, bis=None, fuell=None, breite=100, anim="pop"):
    return ficon(sets, name, MB, 380, breite, c, fuell=fuell, bis=bis, anim=anim)


def mpille(text, c, bis=None, fill=WEISS, size=30, anim="pop"):
    return pl(text, MB, 160, c, fill=fill, size=size, anker="m", bis=bis, anim=anim)


# A Fall: die Kleinanzeige -----------------------------------------------------------------------------------------------
DX, WX = 360, 1560                      # Detlef (links, blickt nach rechts), Waltraud (rechts, blickt nach links)
DEa = ("DE_redet_r", DX, BODEN, FH)
WAa = ("WA_redet", WX, BODEN, FH)
WAb = ("WA_entsetzt", WX, BODEN, FH)
tisch = ficon("tabler", "desk", 650, BODEN - 2, 240, NULL, fuell=HOLZ)
TOP = int(tisch.y) + 8                  # Tischplatte
AX, AY, AW, AH = 660, 140, 600, 420     # Anzeige
an = beim("anzeige", "Smartphone")
geld = bewegt(ficon("fluent-emoji-flat", "euro-banknote", 590, TOP, 90, "vorkasse", bis="sv"), "vorkasse",
              beim("vorkasse", "Vorkasse"), 810, -230)
lauf = round(bausteine._t(beim("paket", "Paket")) - bausteine._t("paket"), 3)
paket = szene(bewegt(ficon("fluent-emoji-flat", "package", 1330, BODEN - 2, 120, "paket", bis="sv"), "paket",
                     beim("paket", "Paket"), -720), "065paket*", 1.0, versatz=lauf)
folie([(NULL, "Fall · Die Kleinanzeige"), ("waltraud", "Fall · Der Anruf"), ("vorkasse", "Fall · Vorkasse und Paket"),
       ("auspacken", "Fall · Das Display"), ("frage", "Fall · Die Frage")], [
    linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK),
    linienzug([(960, 600), (960, BODEN - 4)], NULL, breite=4, farbe=GRAU),
    pl("Sonntagabend: die Kleinanzeige", 70, 40, NULL, fill=GELB, size=40),
    tisch,
    ficon("fluent-emoji-flat", "laptop", 700, TOP, 110, beim("detlef", "stellt")),
    # Detlef (ab 0,0 s im Bild, kein leerer erster Bildhalt)
    peep_voll("DE_ruhig_r", DX, BODEN, FH, NULL, bis="display"),
    namensschild("Detlef", DX, BODEN, NULL, BLAU),
    # Die Anzeige
    kb(AX, AY, AW, AH, "anzeige", fill=WEISS, rund=18, schatten=6, rand=4, bis="vorkasse"),
    z("Kleinanzeige", AX + 30, AY + 22, "anzeige", "Bold", 28, farbe=TEXT, rechts=1240, bis="vorkasse"),
    z("Smartphone", AX + 210, AY + 75, an, "ExtraBold", 36, rechts=1240, bis="vorkasse"),
    z("neu und", AX + 210, AY + 130, beim("anzeige", "neu"), size=32, rechts=1240, bis="vorkasse"),
    z("originalverpackt", AX + 210, AY + 172, beim("anzeige", "originalverpackt"), size=32, rechts=1240, bis="vorkasse"),
    z("400 €", AX + 210, AY + 225, beim("anzeige", "vierhundert"), "ExtraBold", 46, rechts=1240, bis="vorkasse"),
    kb(AX + 30, AY + 75, 150, 210, "foto", fill=(246, 246, 250, 255), rund=10, schatten=4, rand=4, bis="vorkasse"),
    ficon("tabler", "device-mobile", AX + 105, AY + 265, 90, "foto", fuell=WEISS, bis="vorkasse"),
    pl("Foto: unbeschädigt", AX + 105, AY + 300, beim("foto", "unbeschädigtes"), fill=GRUEN, size=26, anker="m",
       bis="vorkasse"),
    z("„Top-Handy, ein echtes Schnäppchen!“", AX + 30, AY + 360, beim("preis", "Top"), "Bold", 29, rechts=1240,
      bis="vorkasse"),
    # Detlef weiß: Display gesprungen
    peep_voll("DE_denkt_r", DX, BODEN, FH, "display", anim="cut", bis="preis"),
    blase("denk", 380, 250, beim("display", "Display"), DX - 30, 220, inhalt=[" ", " ", "Display gesprungen"], textsize=28,
          figur=("DE_denkt_r", DX, BODEN, FH), bis="preis"),
    ficon("streamline-freehand", "broken-smartphone-1", DX - 30, 222, 52, beim("display", "Display"), fuell=WEISS, bis="preis"),
    peep_voll("DE_froh_r", DX, BODEN, FH, "preis", anim="cut", bis="d1"),
    # Waltraud ruft an
    peep_voll("WA_ruhig", WX, BODEN, FH, "waltraud", anim="fade", bis="w1"),
    namensschild("Waltraud", WX, BODEN, "waltraud", GRUEN),
    ficon("fluent-emoji-flat", "telephone-receiver", WX + 170, 470, 60, beim("waltraud", "ruft"), bis="vorkasse"),
    ficon("fluent-emoji-flat", "telephone-receiver", DX - 175, 470, 60, beim("waltraud", "ruft"), spiegeln=True, bis="vorkasse"),
    *redet("WA_redet", WX, BODEN, FH, "w1", "d1"),
    blase("sprech", 440, 200, "w1", WX, 215, inhalt=["Ist das Handy", "wirklich neu?"], textsize=34, figur=WAa, bis="d1"),
    *redet("DE_redet_r", DX, BODEN, FH, "d1", "vorkasse"),
    blase("sprech", 480, 200, "d1", DX + 20, 215, inhalt=["Ja, ganz neu,", "noch nie benutzt."], textsize=34, figur=DEa,
          bis="vorkasse"),
    peep_voll("WA_froh", WX, BODEN, FH, "d1", anim="cut", bis="vorkasse"),
    # Vorkasse: 400 € wandern zu Detlef; zwei Tage später das Paket
    peep_voll("WA_ruhig", WX, BODEN, FH, "vorkasse", anim="cut", bis="auspacken"),
    peep_voll("DE_froh_r", DX, BODEN, FH, "vorkasse", anim="cut", bis="frage"),
    geld,
    pl("400 € per Vorkasse", 960, 300, beim("vorkasse", "vierhundert"), fill=WEISS, size=32, anker="m", bis="paket"),
    paket,
    pl("2 Tage später", 960, 300, "paket", fill=WEISS, size=32, anker="m", bis="auspacken"),
    # Auspacken: das gesprungene Display
    peep_voll("WA_denkt", WX, BODEN, FH, "auspacken", anim="cut", bis="w2"),
    szene(ficon("streamline-freehand", "broken-smartphone-1", 1330, BODEN - 140, 72, beim("auspacken", "packt"), fuell=WEISS,
                bis="sv"), "065auspacken*", 1.0, versatz=0.0),
    *redet("WA_entsetzt", WX, BODEN, FH, "w2", "wert"),
    blase("sprech", 460, 200, "w2", WX - 20, 215, inhalt=["Das Display ist", "ja gesprungen!"], textsize=34, figur=WAb,
          bis="wert"),
    pl("nur noch 150 € wert", 1200, 540, beim("wert", "hundertfünfzig"), fill=ROTHELL, size=30, anker="m", bis="sv"),
    peep_voll("WA_sorge", WX, BODEN, FH, "wert", anim="cut"),
    # Die Frage
    peep_voll("DE_ernst_r", DX, BODEN, FH, "frage", anim="cut"),
    pl("Betrug, § 263 StGB?", 960, 140, "frage", fill=WEISS, size=34, anker="m"),
    pl("Glied für Glied prüfen", 960, 230, beim("frage2", "Glied"), fill=PINK, size=32, anker="m"),
])

# B Sachverhalt --------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    glyphen("An einem Sonntagabend stellt Detlef eine Kleinanzeige ins Netz: ein Smartphone, „neu und originalverpackt“, "
            "für 400 €. Das Foto zeigt ein unbeschädigtes Gerät. Detlef weiß, dass das Display des Geräts, das er verschicken "
            "will, gesprungen ist. Dazu schreibt er: „Top-Handy, ein echtes Schnäppchen!“"),
    glyphen("Waltraud ruft an und fragt, ob das Handy wirklich neu ist. Detlef antwortet: „Ja, ganz neu, noch nie benutzt.“ "
            "Waltraud überweist die 400 € per Vorkasse. Zwei Tage später packt sie das Gerät aus: Das Display ist gesprungen. "
            "So ist das Gerät nur noch 150 € wert."),
], "Hat sich Detlef wegen Betrugs nach § 263 StGB strafbar gemacht?")

# C Wortlaut § 263 Abs. 1 und Kette ------------------------------------------------------------------------------------------
folie([("p263", "§ 263 Abs. 1 StGB › Wortlaut"), ("kette", "§ 263 Abs. 1 StGB › Kette: Täuschung, Irrtum, Verfügung, Schaden"),
       ("subj0", "§ 263 Abs. 1 StGB › subjektiver Tatbestand")], rechts_frei([
    *tafel("p263", "Betrug: § 263 Abs. 1 StGB"),
    *wortlaut(110, 170, 1040, 262, "p263", [
        [("„Wer in der ", 0), ("Absicht", "a"), (", sich oder einem Dritten einen rechtswidrigen", 0)],
        [("Vermögensvorteil zu verschaffen, das Vermögen eines anderen", 0)],
        [("dadurch ", 0), ("beschädigt", "b"), (", daß er durch Vorspiegelung falscher oder durch", 0)],
        [("Entstellung oder Unterdrückung wahrer ", 0), ("Tatsachen", "c"), (" einen ", 0), ("Irrtum", "d")],
        [("erregt oder unterhält, wird mit Freiheitsstrafe bis zu fünf Jahren", 0)],
        [("oder mit Geldstrafe bestraft.“", 0)],
    ], 28, {"a": beim("p263w", "Absicht"), "b": beim("p263w", "beschädigt"), "c": beim("p263w", "Tatsachen"),
            "d": beim("p263w", "Irrtum")}, "§ 263 Abs. 1 StGB"),
    *kette(500, "kette", 4, cues=[beim("kette", "Täuschung"), beim("kette", "Irrtum"), beim("kette", "Vermögensverfügung"),
                                 beim("kette", "Schaden")]),
    z("Verfügung: ungeschrieben, verbindet Irrtum und Schaden", 110, 590, "verf0", "Bold", 32),
    z("jedes Glied beruht auf dem vorigen", 110, 650, "glied", "Bold", 32),
    fl_block(110, 730, 1040, 100, LILAHELL, "subj0", [("subjektiv: Vorsatz und Bereicherungsabsicht", "ExtraBold", 34, INK)]),
    *paar("p263", "WA_ruhig", "DE_ruhig", wa_cues=[("subj0", "WA_denkt")], de_cues=[("kette", "DE_ernst")]),
    mpille("§ 263 StGB", beim("p263", "Paragraf"), bis="kette"),
    ficon("fluent-emoji-flat", "chains", MB, 380, 100, "kette"),
    mpille("eine Kette", "kette", anim="cut", bis="glied"),
    mpille("Glied für Glied", "glied", anim="cut"),
]))

# D 1. Täuschung über Tatsachen ----------------------------------------------------------------------------------------------
PO = "I. Tatbestand › 1. objektiv"
folie([("t1", f"{PO} › a) Täuschung über Tatsachen"), ("konkl", f"{PO} › a) Täuschung: ausdrücklich und konkludent")],
      rechts_frei([
    *tafel("t1", "a) Täuschung über Tatsachen"),
    *kette(170, "t1", 0),
    z("Tatsachen: gegenwärtige oder vergangene Ereignisse", 110, 260, "tats", "Bold", 32),
    z("oder Zustände, die dem Beweis zugänglich sind", 110, 305, beim("tats", "Zustände"), "Bold", 32),
    fund("BGH, Urt. v. 17.12.2019 – 1 StR 171/19, Rn. 48", 150, 352, beim("tats", "Beweis")),
    ok(135, 425, "neu", gr=20),
    z("„neu und unbeschädigt“: prüfbar", 175, 405, "neu", size=32),
    ok(135, 480, beim("ausdr", "ausdrücklich"), gr=20),
    z("ausdrücklich: in der Anzeige und am Telefon", 175, 460, beim("ausdr", "ausdrücklich"), size=32),
    z("konkludent: Unwahrheit nicht ausgesprochen, aber", 110, 545, "konkl", "Bold", 32),
    z("nach der Verkehrsanschauung miterklärt", 110, 590, beim("konkl", "Verkehrsanschauung"), "Bold", 32),
    fund("BGH, Urt. v. 15.12.2006 – 5 StR 181/06, Rn. 20", 150, 637, beim("konkl", "Verkehrsanschauung")),
    ok(135, 715, "konkl2", gr=20),
    z("Foto: „So sieht das Gerät aus.“", 175, 695, "konkl2", size=32),
    *paar("t1", "WA_ruhig", "DE_ruhig", wa_cues=[("konkl2", "WA_denkt")], de_cues=[("ausdr", "DE_ernst")]),
    symbol("tabler", "device-mobile", "neu", bis="konkl2", fuell=WEISS, breite=80),
    mpille("„neu“", beim("neu", "neu"), bis="konkl"),
    mpille("ausdrücklich", "ausdr", anim="cut", bis="konkl"),
    mpille("konkludent", "konkl", anim="cut"),
    symbol("tabler", "photo", "konkl2", fuell=WEISS, anim="cut"),
]))

# E Abgrenzung: Werturteil und Anpreisung -------------------------------------------------------------------------------------
folie([("anpreis", f"{PO} › a) Täuschung: keine bloße Anpreisung"), ("tok", f"{PO} › a) Täuschung (+)")], rechts_frei([
    *tafel("anpreis", "a) Täuschung: Abgrenzung"),
    *kette(170, "anpreis", 0),
    pl("„Top-Handy, ein echtes Schnäppchen!“", 110, 265, "anpreis", fill=HELL, size=32),
    nein(135, 385, beim("anpreis", "reklamehafte"), gr=18),
    z("reklamehafte Anpreisung", 175, 365, beim("anpreis", "reklamehafte"), "Bold", 34),
    z("Werturteil ohne greifbaren Tatsachenkern", 175, 415, beim("anpreis", "Werturteil"), size=32),
    fund("BGH, Urt. v. 17.12.2019 – 1 StR 171/19, Rn. 48", 215, 462, beim("anpreis", "Werturteil")),
    fl_block(110, 560, 1040, 110, GRUEN, "tok", [("Täuschung (+): Angabe „neu“ und Foto", "ExtraBold", 36, INK)]),
    *paar("anpreis", "WA_denkt", "DE_ruhig", wa_cues=[("tok", "WA_ernst")]),
    ficon("fluent-emoji-flat", "sparkles", MB, 380, 90, "anpreis", bis="tok"),
    mpille("Anpreisung", beim("anpreis", "reklamehafte"), fill=HELL, bis="tok"),
    symbol("tabler", "circle-check", "tok", fuell=GRUEN, anim="cut"),
    mpille("Täuschung (+)", "tok", fill=GRUEN, anim="cut"),
]))

# F 2. Irrtum ----------------------------------------------------------------------------------------------------------------
WAi = ("WA_froh", X1, BR, FR)
folie([("irr", f"{PO} › b) Irrtum")], rechts_frei([
    *tafel("irr", "b) Irrtum"),
    *kette(170, "irr", 1),
    z("Irrtum: jeder Widerspruch zwischen der Vorstellung", 110, 260, beim("irr", "Das"), "Bold", 32),
    z("des Getäuschten und der Wirklichkeit", 110, 305, beim("irr", "Vorstellung"), "Bold", 32),
    fund("BGH, Urt. v. 22.11.2013 – 3 StR 162/13, Rn. 8", 150, 352, beim("irr", "Wirklichkeit")),
    ok(135, 445, "irr2", gr=20),
    z("Waltraud glaubt: neues, heiles Gerät", 175, 425, "irr2", size=34),
    ok(135, 505, "irr3", gr=20),
    z("weil Detlef es behauptet hat", 175, 485, "irr3", size=34),
    fl_block(110, 580, 1040, 100, GRUEN, beim("irr3", "Irrtum"), [("Der Irrtum beruht auf der Täuschung.", "ExtraBold", 34, INK)]),
    *paar("irr", "WA_ruhig", "DE_ruhig", wa_cues=[("irr2", "WA_froh")], de_cues=[("irr3", "DE_ernst")]),
    blase("denk", 300, 210, "irr2", 1520, 260, inhalt=[" "], figur=WAi),
    ficon("tabler", "device-mobile", 1520, 295, 60, "irr2", fuell=WEISS),
]))

# G 3. Vermögensverfügung ------------------------------------------------------------------------------------------------------
folie([("vf", f"{PO} › c) Vermögensverfügung"), ("trick", f"{PO} › c) Abgrenzung: Trickdiebstahl, § 242 StGB")],
      rechts_frei([
    *tafel("vf", "c) Vermögensverfügung"),
    *kette(170, "vf", 2),
    z("jedes Handeln, Dulden oder Unterlassen des Getäuschten,", 110, 260, "vfdef", "Bold", 31),
    z("das unmittelbar eine Vermögensminderung herbeiführt", 110, 305, beim("vfdef", "unmittelbar"), "Bold", 31),
    fund("BGH, Urt. v. 25.4.2024 – 4 StR 456/22, Rn. 22", 150, 352, beim("vfdef", "unmittelbar")),
    ok(135, 425, "vf2", gr=20),
    z("Überweisung von 400 €", 175, 405, "vf2", size=32),
    ok(135, 480, beim("vf2", "Ihr"), gr=20),
    z("Vermögen sinkt sofort, ohne weiteren Schritt", 175, 460, beim("vf2", "Ihr"), size=32),
    ok(135, 535, "vf3", gr=20),
    z("gezahlt gerade wegen des Irrtums", 175, 515, "vf3", size=32),
    karte(110, 600, 1040, 230, "trick", fill=ROTHELL, rund=18, schatten=6, rand=4),
    z("Abgrenzung: Trickdiebstahl, § 242 StGB", 140, 620, "trick", "ExtraBold", 32),
    z("Handy nur zum Telefonieren, Täter läuft damit weg:", 140, 670, beim("trick", "Lässt"), size=30),
    z("eigenmächtiges Nehmen, kein Betrug", 140, 715, beim("trick", "eigenmächtig"), "Bold", 30),
    fund("BGH, Urt. v. 12.10.2016 – 1 StR 402/16, Rn. 11", 140, 770, beim("trick", "eigenmächtig")),
    *paar("vf", "WA_ruhig", "DE_ruhig", wa_cues=[("trick", "WA_denkt")], de_cues=[("vf2", "DE_froh"), ("trick", "DE_ruhig")]),
    symbol("fluent-emoji-flat", "euro-banknote", "vf2", bis="trick", breite=110),
    mpille("400 € überwiesen", "vf2", bis="trick"),
    symbol("tabler", "hand-grab", "trick", fuell=WEISS, anim="cut"),
    mpille("eigenmächtig genommen", beim("trick", "eigenmächtig"), fill=ROTHELL, size=28, anim="cut"),
]))

# H 4. Vermögensschaden: Gesamtsaldierung, Eingehungs- und Erfüllungsschaden ------------------------------------------------
folie([("schad", f"{PO} › d) Vermögensschaden"), ("eing", f"{PO} › d) Schaden: Eingehungs- und Erfüllungsschaden")],
      rechts_frei([
    *tafel("schad", "d) Vermögensschaden"),
    *kette(170, "schad", 3),
    z("Gesamtsaldierung: Vermögenswert unmittelbar", 110, 260, "saldo", "Bold", 32),
    z("vor und nach der Verfügung", 110, 305, beim("saldo", "Vermögenswert"), "Bold", 32),
    fund("BGH, Beschl. v. 6.4.2018 – 1 StR 13/18, Rn. 8", 150, 352, beim("saldo", "unmittelbar")),
    z("Eingehungsschaden: bei Vertragsschluss", 110, 430, "eing", "ExtraBold", 32),
    z("Anspruch weniger wert als die Verpflichtung", 150, 478, beim("eing", "Anspruch"), size=32),
    z("Erfüllungsschaden: mit der Zahlung", 110, 560, "erf", "ExtraBold", 32),
    z("Differenz zwischen Leistung und Gegenleistung", 150, 608, beim("erf", "Differenz"), size=32),
    fund("BGH, Beschl. v. 6.4.2018 – 1 StR 13/18, Rn. 9", 150, 655, beim("erf", "Differenz")),
    *paar("schad", "WA_ruhig", "DE_ruhig", wa_cues=[("erf", "WA_sorge")]),
    ficon("fluent-emoji-flat", "balance-scale", MB, 380, 110, "saldo", bis="eing"),
    mpille("vor und nach", beim("saldo", "vor"), size=28, bis="eing"),
    symbol("tabler", "file-text", "eing", fuell=WEISS, bis="erf", anim="cut"),
    mpille("Vertragsschluss", "eing", size=28, bis="erf", anim="cut"),
    symbol("fluent-emoji-flat", "euro-banknote", "erf", breite=110, anim="cut"),
    mpille("Zahlung", "erf", anim="cut"),
]))

# I Rechnung, Bezifferung, Kette steht -------------------------------------------------------------------------------------
folie([("rech", f"{PO} › d) Schaden: 250 €"), ("bezif", f"{PO} › d) Schaden der Höhe nach beziffern"),
       ("kette2", "I. Tatbestand › 1. objektiver Tatbestand (+)")], rechts_frei([
    *tafel("rech", "d) Schaden: konkret beziffert"),
    z("Zahlung von Waltraud", 150, 190, beim("rech", "zahlt"), size=34),
    z("− 400 €", 820, 190, beim("rech", "vierhundert"), "Bold", 34),
    z("Gerät mit gesprungenem Display", 150, 245, beim("rech", "Gerät"), size=34),
    z("+ 150 €", 820, 245, beim("rech", "hundertfünfzig"), "Bold", 34),
    linienzug([(150, 305), (980, 305)], "rech2", breite=4, farbe=INK),
    z("Schaden", 150, 320, "rech2", "ExtraBold", 38),
    z("250 €", 820, 320, beim("rech2", "zweihundertfünfzig"), "ExtraBold", 38),
    z("BVerfG: Schaden der Höhe nach beziffern und", 110, 420, "bezif", "Bold", 32),
    z("wirtschaftlich nachvollziehbar darlegen", 110, 465, beim("bezif", "wirtschaftlich"), "Bold", 32),
    fund("BVerfG, Beschl. v. 23.6.2010 – 2 BvR 2559/08, Rn. 112;", 150, 512, beim("bezif", "wirtschaftlich")),
    fund("BVerfG, Beschl. v. 7.12.2011 – 2 BvR 2500/09, Rn. 176", 150, 548, beim("bezif", "wirtschaftlich")),
    *kette(640, "kette2", 4, cues=[beim("kette2", "Täuschung"), beim("kette2", "Irrtum"), beim("kette2", "Verfügung"),
                                  beim("kette2", "Schaden", 1)]),
    fl_block(110, 730, 1040, 90, GRUEN, beim("kette2", "objektive"), [("objektiver Tatbestand erfüllt", "ExtraBold", 34, INK)]),
    *paar("rech", "WA_sorge", "DE_ruhig", wa_cues=[("kette2", "WA_ernst")], de_cues=[("kette2", "DE_ernst")]),
    symbol("tabler", "calculator", "rech", fuell=WEISS, bis="bezif"),
    mpille("400 € − 150 €", beim("rech", "hundertfünfzig"), bis="bezif"),
    symbol("tabler", "report-money", "bezif", fuell=WEISS, bis="kette2", anim="cut"),
    mpille("beziffern", beim("bezif", "beziffern"), anim="cut", bis="kette2"),
    ficon("fluent-emoji-flat", "chains", MB, 380, 100, "kette2", anim="cut"),
    mpille("Kette steht", "kette2", fill=GRUEN, anim="cut"),
]))

# J Subjektiver Tatbestand --------------------------------------------------------------------------------------------------
PS_ = "I. Tatbestand › 2. subjektiv"
geld2 = bewegt(ficon("fluent-emoji-flat", "euro-banknote", MB + 20, 560, 80, "stoff2"), "stoff2", beim("stoff2", "Detlef"),
               -90, 0)
folie([("vors", f"{PS_} › a) Vorsatz"), ("abs", f"{PS_} › b) Absicht rechtswidriger Bereicherung"),
       ("stoff", f"{PS_} › b) Stoffgleichheit")], rechts_frei([
    *tafel("vors", "2. Subjektiver Tatbestand"),
    z("a) Vorsatz für jedes Glied", 110, 180, "vors", "ExtraBold", 34),
    ok(135, 255, "vors2", gr=20),
    z("kennt das gesprungene Display, will die Zahlung", 175, 235, "vors2", size=32),
    z("b) Absicht: rechtswidriger Vermögensvorteil", 110, 315, "abs", "ExtraBold", 34),
    ok(135, 390, "abs2", gr=20),
    z("es kommt ihm gerade auf die 400 € an", 175, 370, "abs2", size=32),
    ok(135, 450, "rwv", gr=20),
    z("rechtswidrig: kein Anspruch auf 400 € für ein", 175, 430, "rwv", size=32),
    z("Gerät mit gesprungenem Display; vereinbart: neu", 175, 475, beim("rwv", "Gerät"), size=32),
    fund("BGH, Beschl. v. 9.7.2003 – 5 StR 65/02, Rn. 7", 215, 520, beim("rwv", "Gerät")),
    ok(135, 600, "stoff", gr=20),
    z("stoffgleich: Vorteil ist Kehrseite des Schadens", 175, 580, "stoff", size=32),
    z("Geld fließt unmittelbar von Waltraud an Detlef", 175, 625, "stoff2", size=32),
    fund("BGH, Beschl. v. 28.3.2024 – 4 StR 66/24, Rn. 4", 215, 670, "stoff2"),
    *paar("vors", "WA_ruhig", "DE_ruhig", wa_cues=[("stoff", "WA_ernst")], de_cues=[("abs2", "DE_eifrig"), ("stoff", "DE_ruhig")]),
    symbol("tabler", "bulb", "vors", fuell=GELB, bis="abs"),
    mpille("kennt und will", "vors2", bis="abs"),
    symbol("tabler", "target-arrow", "abs", fuell=WEISS, bis="stoff", anim="cut"),
    mpille("Absicht", beim("abs", "Absicht"), anim="cut", bis="rwv"),
    mpille("kein Anspruch", beim("rwv", "keinen"), fill=ROTHELL, anim="cut", bis="stoff"),
    mpille("Kehrseite des Schadens", beim("stoff", "Kehrseite"), size=28, anim="cut"),
    geld2,
]))

# K Rechtswidrigkeit, Schuld, Ergebnis ----------------------------------------------------------------------------------------
folie([("rw", "II. Rechtswidrigkeit, III. Schuld"), ("erg", "Ergebnis · Detlef strafbar, § 263 Abs. 1 StGB")], rechts_frei([
    *tafel("rw", "Rechtswidrigkeit, Schuld, Ergebnis"),
    ok(135, 220, "rw", gr=20),
    z("II. Rechtswidrigkeit: keine Rechtfertigungsgründe", 175, 200, "rw", "Bold", 34),
    ok(135, 290, "schuld", gr=20),
    z("III. Schuld: Detlef handelt schuldhaft", 175, 270, "schuld", "Bold", 34),
    fl_block(110, 380, 1040, 150, GRUEN, beim("erg", "Detlef"), [("Detlef: strafbar wegen Betrugs,", "ExtraBold", 36, INK),
                                                                ("§ 263 Abs. 1 StGB", "ExtraBold", 36, INK)]),
    *paar("rw", "WA_ruhig", "DE_ruhig", de_cues=[("erg", "DE_sorge")]),
    symbol("tabler", "circle-check", beim("erg", "Detlef"), fuell=GRUEN),
    mpille("Betrug (+)", beim("erg", "Detlef"), fill=GRUEN),
]))

# L Ausblick: Versuch, § 263 Abs. 3, § 263a -------------------------------------------------------------------------------------
folie([("versuch", "Ausblick › Versuch, § 263 Abs. 2 StGB"), ("p3", "Ausblick › besonders schwerer Fall, § 263 Abs. 3 StGB"),
       ("p263a", "Ausblick › Computerbetrug, § 263a StGB")], rechts_frei([
    *tafel("versuch", "Ausblick", fill=LILAHELL),
    z("Schwindel bemerkt, nicht gezahlt:", 110, 190, beim("versuch", "Hätte"), size=32),
    z("Versuch kommt in Betracht, § 263 Abs. 2 StGB", 110, 240, beim("versuch", "Versuch"), "ExtraBold", 34),
    z("Betrügt Detlef gewerbsmäßig:", 110, 340, "p3", size=32),
    z("in der Regel besonders schwerer Fall, § 263 Abs. 3", 110, 390, beim("p3", "Regel"), "ExtraBold", 34),
    z("kein Mensch getäuscht, sondern", 110, 490, beim("p263a", "kein"), size=32),
    z("ein Datenverarbeitungsvorgang beeinflusst:", 110, 535, beim("p263a", "Datenverarbeitungsvorgang"), size=32),
    z("Computerbetrug, § 263a StGB", 110, 585, beim("p263a", "Computerbetrug"), "ExtraBold", 34),
    *paar("versuch", "WA_denkt", "DE_ruhig", wa_cues=[("p3", "WA_ruhig")], de_cues=[("p3", "DE_ernst")]),
    symbol("tabler", "hand-stop", beim("versuch", "Hätte"), fuell=WEISS, bis="p3"),
    mpille("nicht gezahlt", beim("versuch", "nicht"), bis="p3"),
    symbol("tabler", "repeat", "p3", fuell=WEISS, bis="p263a", anim="cut"),
    mpille("gewerbsmäßig", beim("p3", "gewerbsmäßig"), anim="cut", bis="p263a"),
    symbol("tabler", "cpu", "p263a", fuell=BLAU, anim="cut"),
    mpille("§ 263a StGB", beim("p263a", "Computerbetrug"), anim="cut"),
]))

# M Klausurtipp (Lexi) --------------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · Kette sauber verknüpfen"), ("tipp3", "Klausurtipp · Schaden konkret berechnen")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Verknüpfe die Kette sauber.", 200, 200, beim("tipp", "Verknüpfe"), "Bold", 38),
    z("Bei jedem Glied fragen: beruht es auf dem vorigen?", 200, 275, "tipp2", size=32),
    ficon("tabler", "arrow-narrow-right", 245, 375, 40, beim("tipp2", "Irrtum")),
    z("Irrtum durch Täuschung", 290, 340, beim("tipp2", "Irrtum"), "Bold", 34),
    ficon("tabler", "arrow-narrow-right", 245, 435, 40, beim("tipp2", "Verfügung")),
    z("Verfügung wegen des Irrtums", 290, 400, beim("tipp2", "Verfügung"), "Bold", 34),
    ficon("tabler", "arrow-narrow-right", 245, 495, 40, beim("tipp2", "Schaden")),
    z("Schaden durch die Verfügung", 290, 460, beim("tipp2", "Schaden"), "Bold", 34),
    z("Schaden konkret ausrechnen:", 200, 560, "tipp3", size=34),
    z("400 € − 150 €", 200, 615, beim("tipp3", "vierhundert"), "ExtraBold", 40),
    *redet("LX_warnt", LXX, BR, FR + 60, "tipp", "sch"),
    namensschild("Lexi", LXX, BR, "tipp", GELB, d=0.2),
])

# N Prüfschema ---------------------------------------------------------------------------------------------------------------
K1, K2, K3 = 150, 220, 300
PSCH = "Prüfschema"
folie([("sch", PSCH), ("k1", f"{PSCH} › I. Tatbestand"), ("k1a", f"{PSCH} › I. 1. a) Täuschung über Tatsachen"),
       ("k1b", f"{PSCH} › I. 1. b) Irrtum"), ("k1c", f"{PSCH} › I. 1. c) Vermögensverfügung"),
       ("k1d", f"{PSCH} › I. 1. d) Vermögensschaden"), ("k1e", f"{PSCH} › I. 1. e) Kausal- und Funktionszusammenhang"),
       ("k1f", f"{PSCH} › I. 2. a) Vorsatz"), ("k1g", f"{PSCH} › I. 2. b) Absicht rechtswidriger, stoffgleicher Bereicherung"),
       ("k2", f"{PSCH} › II. Rechtswidrigkeit"), ("k3", f"{PSCH} › III. Schuld"),
       ("k4", f"{PSCH} › IV. Strafzumessung: besonders schwerer Fall")], [
    karte(60, 50, 1800, 900, "sch"),
    titel("Prüfschema: Betrug, § 263 Abs. 1 StGB", 110, 90, "sch", 54),
    z("I. Tatbestand", K1, 180, "k1", "Bold", 38, rechts=1820),
    z("1. objektiver Tatbestand", K2, 235, "k1a", "Bold", 34, rechts=1820),
    z("a) Täuschung über Tatsachen", K3, 285, beim("k1a", "Täuschung"), size=34, rechts=1820),
    z("b) Irrtum", K3, 333, "k1b", size=34, rechts=1820),
    z("c) Vermögensverfügung", K3, 381, "k1c", size=34, rechts=1820),
    z("d) Vermögensschaden", K3, 429, "k1d", size=34, rechts=1820),
    z("e) Kausal- und Funktionszusammenhang", K3, 477, beim("k1e", "Kausal"), size=34, rechts=1820),
    z("2. subjektiver Tatbestand", K2, 535, "k1f", "Bold", 34, rechts=1820),
    z("a) Vorsatz", K3, 585, beim("k1f", "Vorsatz"), size=34, rechts=1820),
    z("b) Absicht rechtswidriger, stoffgleicher Bereicherung", K3, 633, "k1g", size=34, rechts=1820),
    z("II. Rechtswidrigkeit", K1, 700, "k2", "Bold", 38, rechts=1820),
    z("III. Schuld", K1, 765, "k3", "Bold", 38, rechts=1820),
    z("IV. Strafzumessung: besonders schwerer Fall, § 263 Abs. 3 StGB", K1, 830, "k4", "Bold", 38, rechts=1820),
])

# O Merksatz (Lexi) ----------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Betrug ist eine ", 0), ("Kette", "a"), (": Täuschung, Irrtum,", 0)],
                 [("Verfügung und Schaden müssen", 0)], [("aufeinander beruhen", "b"), (".", 0)]], 750, 290, 44, "merke",
                {"a": beim("merke", "Kette"), "b": beim("merke", "aufeinander")}),
    *markertext([[("Bloße ", 0), ("Anpreisungen", "c"), (" sind keine Tatsachen.", 0)]], 750, 530, 44, "m2",
                {"c": beim("m2", "Anpreisungen")}),
    *markertext([[("Den ", 0), ("Schaden", "d"), (" zeigt der Vergleich vor und", 0)],
                 [("nach der Verfügung, in Euro beziffert.", 0)]], 750, 650, 44, "m3", {"d": beim("m3", "Schaden")}),
    *redet("LX_erklaert", 1680, 960, 690, "merke", lexi_bis_ende("merke")),
    namensschild("Lexi", 1680, 960, "merke", GELB, d=0.2),
])
