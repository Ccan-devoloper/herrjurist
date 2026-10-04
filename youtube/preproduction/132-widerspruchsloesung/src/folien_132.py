"""Folge 132 · Widerspruchslösung: Fehlende Belehrung und Verwertungsverbot – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A Turnhalle (Herr Mangold sprüht, Anwohnerin ruft die Polizei, Kirchhoff fragt „nur mal
informatorisch“, Geständnis, Vermerk), B Amtsgericht (Kirchhoff als Zeugin, Widerspruch von Rechtsanwalt Hufnagel), C Sachverhalt,
D 1. Belehrungspflicht (Wortlautkarte § 136 Abs. 1 S. 2 StPO), E/F 2. Beschuldigtenstellung (Maßstab, Fall), G 3. Verwertungsverbot
(BGHSt 38, 214, Leitsatz-Auszug), H/I 4. Widerspruchslösung (Wortlautkarte § 257 Abs. 1, 2 StPO; ohne Verteidiger; Kritik),
J Ergebnis Grundfall/Variante (Zeitleiste), K 5. Abgrenzung § 136a (Wortlautkarte Abs. 3 S. 2), L 6. Revision, M Klausurtipp
(Lexi), N Schema, O Merksatz (Lexi).
Geräusche nur bei sichtbarer Handlung: Spraydose (A, Mangold sprüht), Stift auf Papier (A, Kirchhoff schreibt den Vermerk);
Freesound CC0. Hilfsfunktionen glyphen/z/pl/fb/tafel/wortlaut/redet/namensschild als eigene Kopie aus Folge 126 (gemeinsame
Dateien unverändert). Zahlen auf Tafeln, Pillen und Blasen als Ziffern (Wortlautkarten wörtlich, amtlich „daß“)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont

bausteine.FIGORDNER = "op_132/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_132/" in n:
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


def hand(name, cx, unten, hoehe, seite):
    """Position der ausgestreckten Hand (äußerster Pixel links/rechts im oberen Körperdrittel) für ein Requisit."""
    e = peep_voll(name, cx, unten, hoehe, "_")
    a = np.asarray(e.sprite)[:, :, 3] > 20
    h = a.shape[0]
    band = a[int(h * 0.25):int(h * 0.55)]
    ys, xs = np.nonzero(band)
    x = xs.min() if seite < 0 else xs.max()
    y = int(np.median(ys[xs == x])) + int(h * 0.25)
    return e.x + x, e.y + y


def bis_(e, bis):
    e.bis = bis
    return e


WAND = (236, 226, 212, 255)
GRUENTON = "#3E9A4A"

# A Fall: an der Turnhalle ---------------------------------------------------------------------------------------------------
MX, KX, AX = 1060, 1420, 1750           # Herr Mangold (an der Wand), Polizistin Kirchhoff, Anwohnerin
hx_l, hy_l = hand("MG_ruhig", MX, BODEN, FH, -1)
hx_r, hy_r = hand("MG_ruhig_r", MX, BODEN, FH, 1)
MGm = ("MG_redet_r", MX, BODEN, FH)
KHa = ("KH_redet", KX, BODEN, FH)
AWa = ("AW_redet", AX, BODEN, FH)
spraydose = szene(ficon("tabler", "spray", hx_l - 12, hy_l + 38, 70, "spray", fuell=GRUEN, bis="mangold"), "132spray*", 1.0,
                  versatz=0.05)
stift = szene(ficon("tabler", "pencil", KX + 140, 640, 60, "notiz", fuell=GELB, d=0.2), "132stift*", 1.0, versatz=0.0)

folie([(NULL, "Fall · An der Turnhalle"), ("spray", "Fall · Der Schriftzug"), ("anw", "Fall · Die Anwohnerin ruft die Polizei"),
       ("pol", "Fall · Die Polizei kommt"), ("mangold", "Fall · Farbe und Spraydose"),
       ("keinbel", "Fall · Keine Belehrung"), ("k1", "Fall · „nur mal informatorisch“"), ("m1", "Fall · Das Geständnis"),
       ("notiz", "Fall · Der Vermerk")], [
    hart(linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK)),
    hart(karte(60, 300, 800, BODEN - 300, NULL, fill=WAND, rund=6, schatten=6)),
    pl("Turnhalle · Samstagabend", 70, 40, NULL, fill=GELB, size=40, anim="cut"),
    pl("Turnhalle der Gesamtschule", 460, 345, NULL, fill=WEISS, size=30, anker="m", anim="cut"),
    peep_voll("MG_ruhig", MX, BODEN, FH, NULL, anim="cut", bis="mangold"),
    peep_voll("MG_denkt_r", MX, BODEN, FH, "mangold", anim="cut", bis="m1"),
    *redet("MG_redet_r", MX, BODEN, FH, "m1", "notiz"),
    peep_voll("MG_sorge_r", MX, BODEN, FH, "notiz", anim="cut"),
    namensschild("Herr Mangold", MX, BODEN, NULL, GRUEN, anim="cut"),
    spraydose,
    icon("tabler", "scribble", 460, 520, 300, beim("spray", "Schriftzug"), farbe=GRUENTON),
    pl("frisch gestrichen", 460, 700, beim("spray", "frisch"), fill=WEISS, size=28, anker="m", bis="mangold"),
    peep_voll("AW_ruhig", AX, BODEN, FH, "anw", bis="a1"),
    *redet("AW_redet", AX, BODEN, FH, "a1", "mangold"),
    peep_voll("AW_ruhig", AX, BODEN, FH, "mangold", anim="cut"),
    namensschild("Anwohnerin", AX, BODEN, "anw", LILA),
    ficon("tabler", "phone-call", AX, 330, 80, beim("anw", "ruft"), fuell=WEISS, bis="pol"),
    pl("ruft die Polizei", AX, 210, beim("anw", "ruft"), fill=WEISS, size=28, anker="m", bis="pol"),
    peep_voll("KH_ruhig", KX, BODEN, FH, "pol", bis="klar"),
    peep_voll("KH_denkt", KX, BODEN, FH, "klar", anim="cut", bis="k1"),
    *redet("KH_redet", KX, BODEN, FH, "k1", "m1"),
    peep_voll("KH_ruhig", KX, BODEN, FH, "m1", anim="cut", bis="notiz"),
    peep_voll("KH_ernst", KX, BODEN, FH, "notiz", anim="cut"),
    namensschild("Polizistin Kirchhoff", KX, BODEN, "pol", BLAU),
    pl("nach wenigen Minuten", KX, 210, "pol", fill=BLAUHELL, size=28, anker="m", bis="a1"),
    blase("sprech", 640, 190, "a1", 1420, 200, inhalt=["Der Mann im grünen Pullover war es.", "Ich habe ihn genau gesehen!"],
          textsize=30, figur=AWa, bis="mangold"),
    ficon("tabler", "spray", hx_r + 12, hy_r + 38, 70, "mangold", fuell=GRUEN, anim="cut"),
    pl("grüne Farbe an den Fingern", 460, 650, beim("farbe", "Fingern"), fill=WEISS, size=30, anker="m", bis="keinbel"),
    pl("Spraydose in der Hand", 460, 720, beim("farbe", "Spraydose"), fill=WEISS, size=30, anker="m", bis="keinbel"),
    blase("denk", 380, 170, "klar", 1300, 210, inhalt=["Er war es."], textsize=32, figur=("KH_denkt", KX, BODEN, FH),
          bis="k1"),
    pl("keine Belehrung über seine Rechte", 460, 680, "keinbel", fill=ROTHELL, size=30, anker="m", bis="notiz"),
    bis_(nein(170, 790, beim("keinbel", "nicht"), gr=22), "notiz"),
    blase("sprech", 720, 200, "k1", 1290, 200, inhalt=["Ich frage Sie nur mal informatorisch:",
          "Haben Sie an die Wand gesprüht?"], textsize=30, figur=KHa, bis="m1"),
    blase("sprech", 560, 170, "m1", 860, 200, inhalt=["Ja, das war ich.", "Tut mir leid."], textsize=32, figur=MGm,
          bis="notiz"),
    ficon("tabler", "notebook", KX + 140, 720, 90, "notiz", fuell=WEISS),
    stift,
    pl("Vermerk: Geständnis", 460, 680, beim("notiz", "Geständnis"), fill=GELB, size=30, anker="m"),
])

# B Fall: Hauptverhandlung beim Amtsgericht -------------------------------------------------------------------------------------
RX, ZX, VX, AGX = 430, 900, 1340, 1690   # Strafrichterin, Zeugin Kirchhoff, Verteidiger Hufnagel, Angeklagter Mangold
HNb = ("HN_redet", VX, BODEN, FH)
folie([("hv", "Fall · Hauptverhandlung beim Amtsgericht"), ("schweigt", "Fall · Herr Mangold schweigt"),
       ("zeugin", "Fall · Die Polizistin als Zeugin"), ("steht", "Fall · Der Widerspruch"), ("frage", "Fall · Die Frage")], [
    hart(linienzug([(60, BODEN), (1860, BODEN)], "hv", breite=7, farbe=INK)),
    pl("Amtsgericht · Monate später", 70, 40, "hv", fill=GELB, size=40, anim="cut"),
    peep_voll("RI_ruhig_r", RX, BODEN, FH, "hv", anim="cut", bis="frage"),
    peep_voll("RI_denkt_r", RX, BODEN, FH, "frage", anim="cut"),
    hart(karte(RX - 230, BODEN - 235, 460, 233, "hv", fill=HOLZ, rund=10, schatten=6)),
    namensschild("Strafrichterin", RX, BODEN, "hv", WEISS, anim="cut"),
    pl("Anklage: Sachbeschädigung", 960, 170, beim("hv", "Sachbeschädigung"), fill=WEISS, size=30, anker="m", bis="h1"),
    peep_voll("HN_ruhig", VX, BODEN, FH, "hv", anim="cut", bis="steht"),
    peep_voll("HN_denkt", VX, BODEN, FH, "steht", anim="cut", bis="h1"),
    *redet("HN_redet", VX, BODEN, FH, "h1", "frage"),
    peep_voll("HN_ernst", VX, BODEN, FH, "frage", anim="cut"),
    namensschild("Rechtsanwalt Hufnagel", VX, BODEN, "hv", WEISS, anim="cut"),
    peep_voll("MG_ruhig", AGX, BODEN, FH, "hv", anim="cut", bis="schweigt"),
    peep_voll("MG_muede", AGX, BODEN, FH, "schweigt", anim="cut", bis="frage"),
    peep_voll("MG_denkt", AGX, BODEN, FH, "frage", anim="cut"),
    namensschild("Herr Mangold", AGX, BODEN, "hv", GRUEN, anim="cut"),
    ficon("tabler", "microphone-off", AGX, 380, 70, "schweigt", fuell=WEISS, bis="h1"),
    pl("schweigt", AGX, 250, "schweigt", fill=WEISS, size=28, anker="m", bis="h1"),
    peep_voll("KH_ruhig", ZX, BODEN, FH, "zeugin", bis="frage"),
    peep_voll("KH_denkt", ZX, BODEN, FH, "frage", anim="cut"),
    namensschild("Polizistin Kirchhoff", ZX, BODEN, "zeugin", BLAU),
    pl("Zeugin: Geständnis am Tatort", 960, 240, beim("zeugin", "gestanden"), fill=BLAUHELL, size=30, anker="m", bis="h1"),
    pl("direkt danach: der Verteidiger", 960, 310, "steht", fill=WEISS, size=28, anker="m", bis="h1"),
    blase("sprech", 820, 190, "h1", 1180, 200, inhalt=["Ich widerspreche der Verwertung. Mein", "Mandant wurde am Tatort nicht belehrt."],
          textsize=30, figur=HNb, bis="frage"),
    pl("Darf sie das Geständnis verwerten?", 1060, 170, "frage", fill=WEISS, size=34, anker="m"),
    pl("Und wenn Hufnagel geschwiegen hätte?", 1060, 255, "frage2", fill=GELB, size=34, anker="m"),
])

# C Sachverhalt ----------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    glyphen("Herr Mangold sprüht abends einen Schriftzug an die frisch gestrichene Wand einer Turnhalle. Eine Anwohnerin ruft "
            "die Polizei und zeigt Polizeikommissarin Kirchhoff den Mann. Er hat grüne Farbe an den Fingern und eine "
            "Spraydose in der Hand. Kirchhoff hält ihn für den Täter und fragt ihn ohne jede Belehrung „nur mal "
            "informatorisch“, ob er gesprüht habe. Er gesteht; sie hält das im Vermerk fest."),
    glyphen("In der Hauptverhandlung wegen Sachbeschädigung schweigt Herr Mangold. Kirchhoff sagt als Zeugin über das "
            "Geständnis aus. Direkt danach widerspricht sein Verteidiger, Rechtsanwalt Hufnagel, der Verwertung. Variante: "
            "Hufnagel schweigt und rügt die fehlende Belehrung erst im Plädoyer."),
], "Darf das Geständnis verwertet werden – im Grundfall und in der Variante?")

# D 1. Belehrungspflicht ------------------------------------------------------------------------------------------------------
P1 = "1. Belehrungspflicht"
folie([("p163", f"{P1} › § 163a Abs. 4 S. 2 StPO"), ("verweis", f"{P1} › § 136 Abs. 1 S. 2 StPO"),
       ("nichts", f"{P1} › hier: kein Hinweis"), ("nurwenn", f"{P1} › nur gegenüber einem Beschuldigten")], rechts_frei([
    *tafel("p163", "1. Belehrungspflicht"),
    z("Vernehmung durch die Polizei: § 163a Abs. 4 S. 2 StPO", 110, 175, "p163", "Bold", 32),
    z("verweist auf § 136 Abs. 1 S. 2 StPO", 150, 225, "verweis", size=30),
    *wortlaut(110, 290, 1040, 200, "p136", [
        [("„Er ist darauf hinzuweisen, daß es ihm nach dem Gesetz", 0)],
        [("freistehe, sich zu der Beschuldigung zu äußern oder", "f")],
        [("nicht zur Sache auszusagen", "f2"), (" und jederzeit … einen von", 0)],
        [("ihm zu wählenden ", 0), ("Verteidiger zu befragen", "v"), (".“", 0)],
    ], 30, {"f": beim("p136", "freisteht"), "f2": beim("p136", "freisteht"), "v": beim("vert", "Verteidiger")},
        "§ 136 Abs. 1 S. 2 StPO (Auszug)"),
    nein(150, 625, beim("nichts", "nichts"), gr=20),
    z("Kirchhoff: kein Hinweis, weder Schweigerecht noch Verteidiger", 185, 605, "nichts", size=30),
    fb(110, 680, 1040, 110, BLAUHELL, "nurwenn", [("Pflicht nur gegenüber einem Beschuldigten", "ExtraBold", 34, INK)]),
    peep_voll("KH_ruhig", X1, BR, FR, "p163", bis="nichts"),
    peep_voll("KH_ernst", X1, BR, FR, "nichts", anim="cut"),
    peep_voll("MG_ruhig", X2, BR, FR, "p163", d=0.2, bis="nurwenn"),
    peep_voll("MG_denkt", X2, BR, FR, "nurwenn", anim="cut"),
    namensschild("Polizistin Kirchhoff", X1 - 60, BR, "p163", BLAU, d=0.2),
    namensschild("Herr Mangold", X2 + 30, BR, "p163", GRUEN, d=0.3),
    ficon("tabler", "notebook", MB, 380, 100, "p163", fuell=WEISS, bis="p136"),
    pl("Vernehmung", MB, 160, "p163", fill=WEISS, size=28, anker="m", bis="p136"),
    ficon("tabler", "microphone-off", MB, 380, 90, "p136", fuell=WEISS, anim="cut", bis="vert"),
    pl("Schweigerecht", MB, 160, "p136", fill=GELB, size=28, anker="m", anim="cut", bis="vert"),
    ficon("tabler", "scale", MB, 380, 100, "vert", fuell=WEISS, anim="cut", bis="nurwenn"),
    pl("Verteidiger befragen", MB, 160, "vert", fill=GELB, size=28, anker="m", anim="cut", bis="nichts"),
    pl("kein Hinweis", MB, 160, "nichts", fill=ROTHELL, size=28, anker="m", anim="cut", bis="nurwenn"),
    ficon("tabler", "help-circle", MB, 380, 100, "nurwenn", fuell=WEISS, anim="cut"),
    pl("Beschuldigter?", MB, 160, "nurwenn", fill=BLAUHELL, size=28, anker="m", anim="cut"),
]))

# E 2. Beschuldigtenstellung: Maßstab ---------------------------------------------------------------------------------------
P2 = "2. Beschuldigtenstellung"
folie([("besch", f"{P2} › zwei Elemente"), ("wille", f"{P2} › subjektiv: Verfolgungswille"),
       ("akt", f"{P2} › objektiv: Willensakt"), ("info", f"{P2} › informatorische Befragung"),
       ("staerke", f"{P2} › Stärke des Tatverdachts"), ("spiel", f"{P2} › Beurteilungsspielraum"),
       ("willk", f"{P2} › Grenze: Willkür")], rechts_frei([
    *tafel("besch", "2. Wann ist man Beschuldigter?"),
    z("subjektiv: Verfolgungswille der Polizei", 110, 175, "wille", "Bold", 32),
    z("objektiv: Willensakt, nach außen sichtbar", 110, 225, "akt", "Bold", 32),
    fund("BGH, Urt. v. 3.7.2007 – 1 StR 3/07, Rn. 17", 150, 272, beim("akt", "Willensakt")),
    z("Am Tatort nur fragen, ob jemand etwas beobachtet hat:", 110, 335, "info", size=30),
    z("noch keine Beschuldigtenvernehmung", 150, 375, beim("info", "vernimmt"), size=30),
    pl("= informatorische Befragung", 150, 420, beim("info", "informatorische"), fill=BLAUHELL, size=30),
    fund("BGHSt 38, 214, 227 f.", 700, 432, beim("info", "informatorische")),
    z("Bedeutsam: die Stärke des Tatverdachts", 110, 510, "staerke", "Bold", 32),
    z("Die Polizei hat einen Beurteilungsspielraum.", 110, 560, "spiel", size=30),
    fb(110, 625, 1040, 150, GELB, "willk", [("Verdacht so stark, dass alles andere willkürlich", "ExtraBold", 32, INK),
                                          ("wäre: Beschuldigtenvernehmung, also belehren", "ExtraBold", 32, INK)]),
    fund("BGH, Beschl. v. 10.3.2026 – 5 StR 547/25, Rn. 6", 110, 790, beim("willk", "übergehen")),
    peep_voll("KH_ruhig", X1, BR, FR, "besch", bis="info"),
    peep_voll("KH_denkt", X1, BR, FR, "info", anim="cut", bis="willk"),
    peep_voll("KH_ernst", X1, BR, FR, "willk", anim="cut"),
    peep_voll("AW_ruhig", X2, BR, FR, "besch", d=0.2),
    namensschild("Polizistin Kirchhoff", X1 - 60, BR, "besch", BLAU, d=0.2),
    namensschild("Anwohnerin", X2 + 30, BR, "besch", LILA, d=0.3),
    ficon("tabler", "user-question", MB, 380, 100, "besch", fuell=WEISS, bis="info"),
    pl("Wille + Akt", MB, 160, "wille", fill=WEISS, size=28, anker="m", bis="info"),
    ficon("tabler", "eye", MB, 380, 100, "info", fuell=WEISS, anim="cut", bis="staerke"),
    pl("Wer hat etwas gesehen?", MB, 160, "info", fill=BLAUHELL, size=28, anker="m", anim="cut", bis="staerke"),
    ficon("tabler", "scale", MB, 380, 110, "staerke", fuell=GELB, anim="cut", bis="willk"),
    pl("Stärke des Verdachts", MB, 160, "staerke", fill=GELB, size=28, anker="m", anim="cut", bis="willk"),
    ficon("tabler", "alert-triangle", MB, 380, 100, "willk", fuell=GELB, anim="cut"),
    pl("Willkür? belehren!", MB, 160, "willk", fill=ROTHELL, size=28, anker="m", anim="cut"),
]))

# F 2. Beschuldigtenstellung: im Fall -----------------------------------------------------------------------------------------
folie([("sub", f"{P2} › im Fall"), ("gezielt", f"{P2} › Kirchhoff fragt gezielt"),
       ("etik", f"{P2} › Ziel und Umstände, nicht das Etikett"), ("jabesch", f"{P2} › Herr Mangold war Beschuldigter")],
      rechts_frei([
    *tafel("sub", "2. Beschuldigtenstellung im Fall"),
    ok(140, 195, beim("sub", "zeigt"), gr=18),
    z("Die Anwohnerin zeigt auf Herrn Mangold.", 175, 175, beim("sub", "zeigt"), "Bold", 30),
    ok(140, 255, beim("sub", "Farbe"), gr=18),
    z("Grüne Farbe an den Fingern, Spraydose in der Hand", 175, 235, beim("sub", "Farbe"), "Bold", 30),
    ok(140, 315, "gezielt", gr=18),
    z("Kirchhoff hält ihn für den Täter,", 175, 295, "gezielt", "Bold", 30),
    z("fragt gezielt nach der Tat", 175, 335, beim("gezielt", "fragt"), "Bold", 30),
    z("Entscheidend: Ziel und Umstände der Befragung,", 110, 420, "etik", size=30),
    z("nicht das Etikett „informatorisch“", 110, 460, beim("etik", "nicht"), size=30),
    fund("vgl. BGH 1 StR 3/07, Rn. 18; StB 14/19, Rn. 31", 110, 505, beim("etik", "nicht")),
    fb(110, 580, 1040, 150, GRUEN, "jabesch", [("Herr Mangold war Beschuldigter.", "ExtraBold", 36, INK),
                                              ("Die Belehrung fehlte.", "ExtraBold", 34, INK)]),
    peep_voll("AW_ruhig", X1, BR, FR, "sub", bis="gezielt"),
    peep_voll("KH_denkt", X1, BR, FR, "gezielt", anim="cut", bis="jabesch"),
    peep_voll("KH_ernst", X1, BR, FR, "jabesch", anim="cut"),
    namensschild("Anwohnerin", X1 - 40, BR, "sub", LILA, d=0.2, bis="gezielt"),
    namensschild("Polizistin Kirchhoff", X1 - 60, BR, "gezielt", BLAU, anim="cut"),
    peep_voll("MG_ruhig", X2, BR, FR, "sub", d=0.2, bis="jabesch"),
    peep_voll("MG_sorge", X2, BR, FR, "jabesch", anim="cut"),
    namensschild("Herr Mangold", X2 + 30, BR, "sub", GRUEN, d=0.3),
    ficon("tabler", "hand-finger", MB, 380, 90, "sub", fuell=WEISS, bis=beim("sub", "Farbe")),
    pl("Zeugin zeigt", MB, 160, "sub", fill=WEISS, size=28, anker="m", bis=beim("sub", "Farbe")),
    ficon("tabler", "spray", MB, 380, 90, beim("sub", "Farbe"), fuell=GRUEN, anim="cut", bis="gezielt"),
    pl("Farbe + Spraydose", MB, 160, beim("sub", "Farbe"), fill=GRUEN, size=28, anker="m", anim="cut", bis="gezielt"),
    ficon("tabler", "message-circle", MB, 380, 100, "gezielt", fuell=WEISS, anim="cut", bis="etik"),
    pl("gezielte Frage", MB, 160, "gezielt", fill=WEISS, size=28, anker="m", anim="cut", bis="etik"),
    ficon("tabler", "tag", MB, 380, 100, "etik", fuell=GELB, anim="cut", bis="jabesch"),
    pl("Etikett egal", MB, 160, "etik", fill=GELB, size=28, anker="m", anim="cut", bis="jabesch"),
    ficon("tabler", "circle-check", MB, 380, 100, "jabesch", fuell=GRUEN, anim="cut"),
    pl("Beschuldigter", MB, 160, "jabesch", fill=GRUEN, size=28, anker="m", anim="cut"),
]))

# G 3. Verwertungsverbot -----------------------------------------------------------------------------------------------------
P3 = "3. Verwertungsverbot"
folie([("vv", f"{P3} › Was folgt daraus?"), ("bghst", f"{P3} › BGHSt 38, 214"), ("grund", f"{P3} › faires Verfahren"),
       ("zeug", f"{P3} › auch über die Polizistin als Zeugin"), ("ausn", f"{P3} › Ausnahme: Schweigerecht bekannt"),
       ("ausn2", f"{P3} › hier: kein Anhaltspunkt")], rechts_frei([
    *tafel("vv", "3. Verwertungsverbot"),
    z("BGH, Beschl. v. 27.2.1992 – 5 StR 190/91 = BGHSt 38, 214", 110, 175, "bghst", "Bold", 30),
    *wortlaut(110, 235, 1040, 160, "vv2", [
        [("„… so dürfen Äußerungen, die der Beschuldigte in", 0)],
        [("dieser Vernehmung gemacht hat, ", 0), ("nicht verwertet", "n")],
        [("werden …“", "n2")],
    ], 30, {"n": beim("vv2", "nicht"), "n2": beim("vv2", "nicht")}, "BGHSt 38, 214 (Leitsatz, Auszug)"),
    z("Schweigerecht: Teil des fairen Verfahrens; die erste", 110, 455, "grund", size=30),
    z("Befragung trifft einen meist unvorbereitet", 110, 495, beim("grund", "erste"), size=30),
    fund("BGHSt 38, 214, 220 ff.", 150, 538, beim("grund", "unvorbereitet")),
    z("Gilt auch, wenn die Polizistin als Zeugin aussagt", 110, 590, "zeug", "Bold", 30),
    fund("BGHSt 38, 214, 216 f., 218", 150, 633, beim("zeug", "Zeugin")),
    z("Ausnahme: Schweigerecht ohne Belehrung bekannt", 110, 690, "ausn", size=30),
    fund("BGHSt 38, 214, 224 f.", 150, 733, beim("ausn", "kannte")),
    nein(150, 805, beim("ausn2", "keinen"), gr=20),
    z("hier: kein Anhaltspunkt", 185, 785, beim("ausn2", "keinen"), "Bold", 30),
    peep_voll("MG_ruhig", X1, BR, FR, "vv", bis="vv2"),
    peep_voll("MG_froh", X1, BR, FR, "vv2", anim="cut", bis="ausn"),
    peep_voll("MG_denkt", X1, BR, FR, "ausn", anim="cut", bis="ausn2"),
    peep_voll("MG_ruhig", X1, BR, FR, "ausn2", anim="cut"),
    peep_voll("KH_ruhig", X2, BR, FR, "vv", d=0.2, bis="zeug"),
    peep_voll("KH_denkt", X2, BR, FR, "zeug", anim="cut"),
    namensschild("Herr Mangold", X1 - 40, BR, "vv", GRUEN, d=0.2),
    namensschild("Polizistin Kirchhoff", X2 - 10, BR, "vv", BLAU, d=0.3),
    ficon("tabler", "gavel", MB, 380, 100, "bghst", fuell=HOLZ, bis="grund"),
    pl("BGH 1992", MB, 160, "bghst", fill=WEISS, size=28, anker="m", bis="vv2"),
    pl("nicht verwertbar", MB, 160, "vv2", fill=ROTHELL, size=28, anker="m", anim="cut", bis="grund"),
    ficon("tabler", "scale", MB, 380, 110, "grund", fuell=GELB, anim="cut", bis="zeug"),
    pl("faires Verfahren", MB, 160, "grund", fill=GELB, size=28, anker="m", anim="cut", bis="zeug"),
    ficon("tabler", "ear-off", MB, 380, 100, "zeug", fuell=WEISS, anim="cut", bis="ausn"),
    pl("auch als Zeugin", MB, 160, "zeug", fill=BLAUHELL, size=28, anker="m", anim="cut", bis="ausn"),
    ficon("tabler", "bulb", MB, 380, 100, "ausn", fuell=GELB, anim="cut", bis="ausn2"),
    pl("Recht bekannt?", MB, 160, "ausn", fill=WEISS, size=28, anker="m", anim="cut", bis="ausn2"),
    ficon("tabler", "circle-x", MB, 380, 100, "ausn2", fuell=ROT, anim="cut"),
    pl("keine Ausnahme", MB, 160, "ausn2", fill=ROTHELL, size=28, anker="m", anim="cut"),
]))

# H 4. Widerspruchslösung und § 257 ------------------------------------------------------------------------------------------
P4 = "4. Widerspruchslösung"
folie([("wl", f"{P4} › kein Verbot von selbst"), ("wl2", f"{P4} › verteidigter Angeklagter widerspricht"),
       ("wl3", f"{P4} › Zeitpunkt des § 257 StPO"), ("direkt", f"{P4} › spätestens nach der Beweiserhebung"),
       ("spaet", f"{P4} › danach nicht nachholbar")], rechts_frei([
    *tafel("wl", "4. Die Widerspruchslösung"),
    z("Das Verwertungsverbot kommt nicht von selbst:", 110, 175, "wl", "Bold", 32),
    z("Der verteidigte Angeklagte muss widersprechen,", 110, 225, "wl2", size=30),
    z("bis zu dem Zeitpunkt des § 257 StPO.", 110, 265, "wl3", size=30),
    *wortlaut(110, 325, 1040, 200, "p257", [
        [("„(1) Nach … ", 0), ("jeder einzelnen Beweiserhebung", "j"), (" soll der", 0)],
        [("Angeklagte befragt werden, ob er dazu etwas zu erklären habe.", 0)],
        [("(2) Auf Verlangen ist auch … dem ", 0), ("Verteidiger", "v"), (" … nach jeder", 0)],
        [("einzelnen Beweiserhebung Gelegenheit zu geben, sich dazu zu erklären.“", 0)],
    ], 28, {"j": beim("p257", "jeder"), "v": beim("p257b", "Verteidiger")}, "§ 257 Abs. 1, 2 StPO (Auszug)"),
    z("Spätestens in der Erklärung nach der Beweiserhebung,", 110, 585, "direkt", "Bold", 30),
    z("hier: nach der Aussage der Polizistin", 110, 625, beim("direkt", "hier"), "Bold", 30),
    fund("BGHSt 38, 214, 225 f.; BGH, Urt. v. 6.10.2016 – 2 StR 46/15, Rn. 14", 110, 668, beim("direkt", "hier")),
    nein(150, 745, beim("spaet", "nicht"), gr=20),
    z("Danach kann er nicht mehr nachgeholt werden.", 185, 725, "spaet", "Bold", 30),
    peep_voll("HN_ruhig", X1, BR, FR, "wl", bis="wl2"),
    peep_voll("HN_denkt", X1, BR, FR, "wl2", anim="cut", bis="direkt"),
    peep_voll("HN_ernst", X1, BR, FR, "direkt", anim="cut"),
    peep_voll("MG_ruhig", X2, BR, FR, "wl", d=0.2, bis="spaet"),
    peep_voll("MG_sorge", X2, BR, FR, "spaet", anim="cut"),
    namensschild("Rechtsanwalt Hufnagel", X1 - 80, BR, "wl", WEISS, d=0.2),
    namensschild("Herr Mangold", X2 + 40, BR, "wl", GRUEN, d=0.3),
    ficon("tabler", "hand-stop", MB, 380, 100, "wl2", fuell=WEISS, bis="wl3"),
    pl("Widerspruch", MB, 160, "wl2", fill=WEISS, size=28, anker="m", bis="wl3"),
    ficon("tabler", "hourglass", MB, 380, 100, "wl3", fuell=GELB, anim="cut", bis="spaet"),
    pl("bis § 257 StPO", MB, 160, "wl3", fill=GELB, size=28, anker="m", anim="cut", bis="direkt"),
    pl("nach der Aussage", MB, 160, "direkt", fill=GELB, size=28, anker="m", anim="cut", bis="spaet"),
    ficon("tabler", "hourglass-empty", MB, 380, 100, "spaet", fuell=WEISS, anim="cut"),
    pl("zu spät = verloren", MB, 160, "spaet", fill=ROTHELL, size=28, anker="m", anim="cut"),
]))

# I 4. Unverteidigter Angeklagter und Kritik -----------------------------------------------------------------------------
folie([("unv", f"{P4} › ohne Verteidiger: Hinweis nötig"), ("kritik", f"{P4} › Frist umstritten")], rechts_frei([
    *tafel("unv", "4. Ohne Verteidiger – und die Kritik"),
    z("Angeklagter ohne Verteidiger:", 110, 180, "unv", "Bold", 32),
    z("Widerspruch nur nötig, wenn ihn der Vorsitzende", 110, 230, beim("unv", "gilt"), size=30),
    z("auf diese Möglichkeit hingewiesen hat", 110, 270, beim("unv", "Möglichkeit"), size=30),
    fund("BGHSt 38, 214, 226; BGH, Urt. v. 9.5.2018 – 5 StR 17/18, Rn. 8", 110, 313, beim("unv", "hingewiesen")),
    z("Kritik: Selbst ein Senat des BGH hat die Frist", 110, 420, "kritik", size=30),
    z("bezweifelt, allerdings für Funde aus Durchsuchungen.", 110, 460, beim("kritik", "bezweifelt"), size=30),
    fund("BGH 2 StR 46/15, Rn. 16; dagegen BGH 5 StR 17/18, Rn. 7", 110, 503, beim("kritik", "Durchsuchungen")),
    peep_voll("RI_ruhig", X1, BR, FR, "unv", bis="kritik"),
    peep_voll("RI_denkt", X1, BR, FR, "kritik", anim="cut"),
    karte(X1 - 160, BR - 235, 320, 233, "unv", fill=HOLZ, rund=10, schatten=6),   # Richtertisch wie in Szene B
    peep_voll("MG_ruhig", X2, BR, FR, "unv", d=0.2, bis="kritik"),
    peep_voll("MG_denkt", X2, BR, FR, "kritik", anim="cut"),
    namensschild("Strafrichterin", X1 - 40, BR, "unv", WEISS, d=0.2),
    namensschild("Herr Mangold", X2 + 30, BR, "unv", GRUEN, d=0.3),
    ficon("tabler", "info-circle", MB, 380, 100, "unv", fuell=BLAU, bis="kritik"),
    pl("Hinweis des Gerichts", MB, 160, beim("unv", "hingewiesen"), fill=BLAUHELL, size=28, anker="m", bis="kritik"),
    ficon("tabler", "messages", MB, 380, 100, "kritik", fuell=WEISS, anim="cut"),
    pl("Frist umstritten", MB, 160, "kritik", fill=WEISS, size=28, anker="m", anim="cut"),
]))

# J Ergebnis: Grundfall und Variante (Zeitleiste der Hauptverhandlung) --------------------------------------------------
PE = "Ergebnis"
ZL = [(130, "Aussage der Zeugin"), (480, "Erklärung, § 257"), (830, "Plädoyer")]
def zeitleiste(y, cue):
    els = [hart(linienzug([(130, y + 70), (1140, y + 70)], cue, breite=5, farbe=INK))]
    for x, t in ZL:
        els.append(pl(t, x, y, cue, fill=WEISS, size=28, anim="cut"))
    return els
folie([("erg", f"{PE} › Grundfall: rechtzeitig widersprochen"), ("erg2", f"{PE} › Grundfall: Geständnis unverwertbar"),
       ("erg3", f"{PE} › Grundfall: nur mit anderen Beweisen"), ("var", f"{PE} › Variante: Widerspruch im Plädoyer"),
       ("var2", f"{PE} › Variante: zu spät"), ("var3", f"{PE} › Variante: Geständnis verwertbar")], rechts_frei([
    *tafel("erg", "Ergebnis: Grundfall und Variante"),
    z("Grundfall", 110, 160, "erg", "ExtraBold", 32),
    *zeitleiste(205, "erg"),
    ok(500, 310, beim("erg", "rechtzeitig"), gr=18),
    z("Widerspruch", 535, 290, beim("erg", "rechtzeitig"), "Bold", 28),
    fb(110, 345, 1040, 125, GRUEN, "erg2", [("Geständnis unverwertbar", "ExtraBold", 34, INK),
                                           ("verurteilen nur mit anderen Beweisen, z. B. Anwohnerin", "Regular", 28, INK)]),
    z("Variante", 110, 500, "var", "ExtraBold", 32),
    *zeitleiste(545, "var"),
    z("Widerspruch erst hier", 835, 630, beim("var", "Plädoyer"), "Bold", 28),
    nein(800, 650, "var2", gr=18),
    fb(110, 690, 1040, 125, ROTHELL, "var3", [("kein Verwertungsverbot", "ExtraBold", 34, INK),
                                            ("das Geständnis darf verwertet werden", "Regular", 28, INK)]),
    peep_voll("HN_froh", X1, BR, FR, "erg", bis="var"),
    peep_voll("HN_ernst", X1, BR, FR, "var", anim="cut"),
    peep_voll("MG_froh", X2, BR, FR, "erg2", anim="cut", bis="var2"),
    peep_voll("MG_ruhig", X2, BR, FR, "erg", anim="cut", bis="erg2"),
    peep_voll("MG_sorge", X2, BR, FR, "var2", anim="cut"),
    namensschild("Rechtsanwalt Hufnagel", X1 - 80, BR, "erg", WEISS, d=0.2),
    namensschild("Herr Mangold", X2 + 40, BR, "erg", GRUEN, d=0.3),
    ficon("tabler", "circle-check", MB, 380, 100, "erg", fuell=GRUEN, bis="erg3"),
    pl("rechtzeitig", MB, 160, beim("erg", "rechtzeitig"), fill=GRUEN, size=28, anker="m", bis="erg2"),
    pl("unverwertbar", MB, 160, "erg2", fill=GRUEN, size=28, anker="m", anim="cut", bis="erg3"),
    ficon("tabler", "users", MB, 380, 100, "erg3", fuell=WEISS, anim="cut", bis="var"),
    pl("andere Beweise?", MB, 160, "erg3", fill=WEISS, size=28, anker="m", anim="cut", bis="var"),
    ficon("tabler", "hourglass-empty", MB, 380, 100, "var", fuell=WEISS, anim="cut", bis="var3"),
    pl("erst im Plädoyer", MB, 160, "var", fill=WEISS, size=28, anker="m", anim="cut", bis="var2"),
    pl("zu spät", MB, 160, "var2", fill=ROTHELL, size=28, anker="m", anim="cut", bis="var3"),
    ficon("tabler", "circle-x", MB, 380, 100, "var3", fuell=ROT, anim="cut"),
    pl("verwertbar", MB, 160, "var3", fill=ROTHELL, size=28, anker="m", anim="cut"),
]))

# K 5. Abgrenzung § 136a StPO -------------------------------------------------------------------------------------------------
P5 = "5. Abgrenzung"
folie([("p136a", f"{P5} › § 136a StPO: verbotene Methoden"), ("p136a2", f"{P5} › § 136a Abs. 3 S. 2 StPO"),
       ("keinw", f"{P5} › kein Widerspruch nötig")], rechts_frei([
    *tafel("p136a", "5. Abgrenzung: § 136a StPO"),
    z("Verbotene Vernehmungsmethoden, z. B. Drohung", 110, 175, "p136a", "Bold", 32),
    z("oder Täuschung, § 136a Abs. 1 StPO", 110, 220, beim("p136a", "Täuschung"), "Bold", 32),
    *wortlaut(110, 300, 1040, 160, "p136a2", [
        [("„Aussagen, die unter Verletzung dieses Verbots zustande", 0)],
        [("gekommen sind, dürfen ", 0), ("auch dann nicht verwertet werden,", "a")],
        [("wenn der Beschuldigte der Verwertung zustimmt.", "a2"), ("“", 0)],
    ], 30, {"a": beim("p136a2", "auch"), "a2": beim("p136a2", "zustimmt")}, "§ 136a Abs. 3 S. 2 StPO"),
    fb(110, 560, 1040, 110, GRUEN, "keinw", [("Kein Widerspruch nötig", "ExtraBold", 36, INK)]),
    peep_voll("HN_ruhig", X1, BR, FR, "p136a", bis="p136a2"),
    peep_voll("HN_denkt", X1, BR, FR, "p136a2", anim="cut", bis="keinw"),
    peep_voll("HN_froh", X1, BR, FR, "keinw", anim="cut"),
    peep_voll("KH_ruhig", X2, BR, FR, "p136a", d=0.2, bis="keinw"),
    peep_voll("KH_ernst", X2, BR, FR, "keinw", anim="cut"),
    namensschild("Rechtsanwalt Hufnagel", X1 - 80, BR, "p136a", WEISS, d=0.2),
    namensschild("Polizistin Kirchhoff", X2 - 10, BR, "p136a", BLAU, d=0.3),
    ficon("tabler", "ban", MB, 380, 100, "p136a", fuell=ROTHELL, bis="p136a2"),
    pl("Drohung, Täuschung", MB, 160, "p136a", fill=ROTHELL, size=28, anker="m", bis="p136a2"),
    ficon("tabler", "lock", MB, 380, 90, "p136a2", fuell=ROT, anim="cut", bis="keinw"),
    pl("trotz Zustimmung", MB, 160, beim("p136a2", "zustimmt"), fill=WEISS, size=28, anker="m", bis="keinw"),
    ficon("tabler", "circle-check", MB, 380, 100, "keinw", fuell=GRUEN, anim="cut"),
    pl("ohne Widerspruch", MB, 160, "keinw", fill=GRUEN, size=28, anker="m", anim="cut"),
]))

# L 6. Revision ----------------------------------------------------------------------------------------------------------------
P6 = "6. Revision"
folie([("rev", f"{P6} › Verwertung trotz Widerspruch"), ("rev2", f"{P6} › Widerspruch vortragen, § 344 Abs. 2 S. 2 StPO"),
       ("rev3", f"{P6} › Tatsachen zur Beschuldigtenstellung"), ("rev4", f"{P6} › siehe Folge 72")], rechts_frei([
    *tafel("rev", "6. In der Revision"),
    z("Verwertung trotz Widerspruch: Verfahrensrüge", 110, 175, "rev", "Bold", 32),
    z("§ 344 Abs. 2 S. 2 StPO: auch vortragen,", 110, 250, "rev2", size=30),
    z("dass und wann widersprochen wurde", 150, 290, beim("rev2", "dass"), "Bold", 30),
    fund("BGH 2 StR 46/15, Rn. 14; BGH 5 StR 17/18, Rn. 6", 150, 333, beim("rev2", "wann")),
    z("Dazu alle Tatsachen zur Beschuldigtenstellung:", 110, 410, "rev3", size=30),
    z("was die Polizei bis zur Befragung wusste", 150, 450, beim("rev3", "was"), "Bold", 30),
    fund("BGH 5 StR 547/25, Rn. 7", 150, 493, beim("rev3", "wusste")),
    fund("siehe Folge 72: Verfahrensrüge nach § 344 Abs. 2 S. 2 StPO", 110, 580, "rev4"),
    peep_voll("HN_ruhig", X1, BR, FR, "rev", bis="rev2"),
    peep_voll("HN_denkt", X1, BR, FR, "rev2", anim="cut", bis="rev4"),
    peep_voll("HN_froh", X1, BR, FR, "rev4", anim="cut"),
    peep_voll("MG_denkt", X2, BR, FR, "rev", d=0.2, bis="rev4"),
    peep_voll("MG_ruhig", X2, BR, FR, "rev4", anim="cut"),
    namensschild("Rechtsanwalt Hufnagel", X1 - 80, BR, "rev", WEISS, d=0.2),
    namensschild("Herr Mangold", X2 + 40, BR, "rev", GRUEN, d=0.3),
    ficon("tabler", "file-text", MB, 380, 100, "rev", fuell=GELB, bis="rev2"),
    pl("Revision", MB, 160, beim("rev", "Revision"), fill=GELB, size=28, anker="m", bis="rev2"),
    ficon("tabler", "list-check", MB, 380, 100, "rev2", fuell=WEISS, anim="cut", bis="rev3"),
    pl("Widerspruch: wann?", MB, 160, "rev2", fill=WEISS, size=28, anker="m", anim="cut", bis="rev3"),
    ficon("tabler", "notebook", MB, 380, 100, "rev3", fuell=WEISS, anim="cut", bis="rev4"),
    pl("Wissen der Polizei", MB, 160, "rev3", fill=BLAUHELL, size=28, anker="m", anim="cut", bis="rev4"),
    ficon("tabler", "file-text", MB, 380, 100, "rev4", fuell=GRUEN, anim="cut"),
    pl("Rüge vollständig", MB, 160, "rev4", fill=GRUEN, size=28, anker="m", anim="cut"),
]))

# M Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · Etikett „informatorisch“"), ("tipp2", "Klausurtipp · Verdacht und Auftreten selbst prüfen"),
       ("tipp3", "Klausurtipp · Widerspruch getrennt prüfen")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Lass dich vom Wort „informatorisch“", 200, 200, beim("tipp", "Lass"), "Bold", 36),
    z("im Vermerk nicht täuschen.", 200, 250, beim("tipp", "Vermerk"), "Bold", 36),
    z("Prüf selbst: Wie stark war der Verdacht?", 200, 350, "tipp2", size=34),
    z("Wie ist die Polizei aufgetreten?", 200, 398, beim("tipp2", "wie", 2), size=34),
    z("Getrennt prüfen: Ob und wann widersprochen?", 200, 500, "tipp3", "Bold", 34),
    z("Ohne Widerspruch ist die Rüge beim verteidigten", 200, 555, beim("tipp3", "Ohne"), size=32),
    z("Angeklagten verloren.", 200, 600, beim("tipp3", "Ohne"), size=32),
    fund("BGH 5 StR 17/18, Rn. 8", 200, 650, beim("tipp3", "verloren")),
    *redet("LX_warnt", LXX, BR, FR + 60, "tipp", "sch"),
    namensschild("Lexi", LXX, BR, "tipp", GELB, d=0.2),
])

# N Schema ------------------------------------------------------------------------------------------------------------------------
K1, K2 = 150, 210
folie([("sch", "Schema"), ("s1", "Schema › I. Belehrungspflicht"), ("s2", "Schema › II. Beschuldigtenstellung"),
       ("s3", "Schema › III. Verwertungsverbot"), ("s4", "Schema › IV. rechtzeitiger Widerspruch"),
       ("s5", "Schema › V. Abgrenzung § 136a StPO"), ("s6", "Schema › VI. Revision")], [
    karte(60, 50, 1800, 900, "sch"),
    titel("Schema: fehlende Belehrung und Widerspruch", 110, 90, "sch", 52),
    z("I. Belehrungspflicht bei der Vernehmung", K1, 190, "s1", "Bold", 36, rechts=1820),
    z("§ 163a Abs. 4 S. 2 i. V. m. § 136 Abs. 1 S. 2 StPO", K2, 238, "s1", size=30, farbe=TEXT, rechts=1820),
    z("II. Beschuldigtenstellung: Verfolgungswille, Stärke des Tatverdachts", K1, 305, "s2", "Bold", 36, rechts=1820),
    z("III. Verwertungsverbot – außer: Schweigerecht bekannt", K1, 385, "s3", "Bold", 36, rechts=1820),
    z("IV. Rechtzeitiger Widerspruch bis zum Zeitpunkt des § 257 StPO", K1, 465, "s4", "Bold", 36, rechts=1820),
    z("ohne Verteidiger: nur nach Hinweis des Vorsitzenden", K2, 513, "s4", size=30, farbe=TEXT, rechts=1820),
    z("V. Bei § 136a StPO: kein Widerspruch nötig", K1, 580, "s5", "Bold", 36, rechts=1820),
    fb(150, 670, 1620, 110, GELB, "s6", [("VI. Revision: den Widerspruch in der Verfahrensrüge vortragen", "ExtraBold", 36, INK)]),
])

# O Merksatz (Lexi) ------------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Ohne Belehrung kein", 0)], [("verwertbares ", 0), ("Geständnis", "a"), (".", 0)]],
                750, 310, 54, "merke", {"a": beim("merke", "Geständnis")}),
    *markertext([[("Aber nur, wenn ", 0), ("rechtzeitig", "b")], [("widersprochen wird.", 0)]], 750, 560, 54, "mz",
                {"b": beim("mz", "rechtzeitig")}),
    *redet("LX_erklaert", 1680, 960, 690, "merke", lexi_bis_ende("merke")),
    namensschild("Lexi", 1680, 960, "merke", GELB, d=0.2),
])
