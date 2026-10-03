"""Folge 091 · Katzenkönig-Fall: Mittelbare Täterschaft – Täter hinter dem Täter – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A1 Fall in der Wohnung (Katzenkönig als Krone in der Gedankenblase, Kerze), A2 vor dem
Blumenladen (kein Messer, kein Angriff, keine Verletzung; das Opfer erscheint nicht als Figur), B Sachverhalt, C der echte
Fall (BGHSt 35, 347), D A. Ulrich: versuchter Mord, E Rechtswidrigkeit § 34, F Schuld § 35, G Wortlautkarte § 17,
H B. Irmgard und Wolfram: Wortlautkarte § 25 Abs. 1, I Streit Verantwortungsprinzip/BGH, J BGH-Formel (wörtlich, S. 354),
K Subsumtion, L warum der Streit zählt, M Ergebnis, N Klausurtipp (Lexi), O Klausurschema, P Merksatz (Lexi).
Geräusche nur bei sichtbarer Handlung: Streichholz (Kerze erscheint), Ladenglocke (Blumenladen), Freesound CC0.
Hilfsfunktionen (z, pl, tafel, wortlaut, fb, redet mit hörbarem Wortende …) wie in Folge 079, Kopie im eigenen Ordner."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont

bausteine.FIGORDNER = "op_091/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
LILAHELL = (246, 243, 255, 255)
ROTHELL = (253, 232, 228, 255)
GRUENHELL = (232, 247, 233, 255)
BLAUHELL = (228, 238, 253, 255)
HOLZ = (214, 160, 110, 255)
HOLZD = (176, 122, 80, 255)
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
    """Wortlautkarte: wörtliches Zitat (gesetze-im-internet.de, Abruf 03.10.2026) in einer hellen Karte, Fundstelle darunter
    rechts. zeilen = Liste von Token-Listen [(text, Schlüssel|0)], hl = {Schlüssel: Cue} (Hervorhebung zum gesprochenen Wort)."""
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


def fb(x, y, w, h, fill, cue, zeilen, rund=18, anim="rise", d=0.0, bis=None):
    """Wie fl_block, aber Zeilenabstand passend zur Schriftgröße der Zeilen (fl_block rechnet mit 64 px, mehrzeilige Blöcke
    ragten sonst über den Rand)."""
    from engine import block
    lh = int(max(zz[2] for zz in zeilen) * 1.3)
    assert len(zeilen) * lh * 1.15 <= h - 16, f"Block zu niedrig: {zeilen}"
    return block(x, y, w, h, fill, None, cue, textsize=lh, rund=rund, rand=INK, randbreite=5, anim=anim, d=d, bis=bis,
                 zeilen=zeilen)


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


def fund(text, x, y, cue, **k):
    """Fundstelle (mobil lesbar: 26 px)."""
    return z(text, x, y, cue, size=26, farbe=TEXT, **k)


# --- Eigene Hilfsfunktion (wie Folge 068/071): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ----------------
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




BR, FR = 930, 480                       # Figuren rechts neben der Tafel
XS = 1640                               # eine Figur allein neben der Tafel
IX = 1440                               # Requisit neben der Einzelfigur
X1, X2 = 1420, 1720                     # zwei Figuren
MB = (X1 + X2) // 2
FARBE = {"IR": PINK, "WO": GELB, "UL": BLAU}
NAME = {"IR": "Irmgard", "WO": "Wolfram", "UL": "Ulrich"}
ROSA = (246, 165, 192, 255)


def kette(prefix, x, folge, bis_=None, d=0.0, hoehe=FR, unten=BR):
    """Eine Figur mit Mimikfolge [(Name, Cue), …] im Zwiebelschalenprinzip (erster Auftritt pop, danach harte Schnitte)."""
    els = []
    for i, (n, c) in enumerate(folge):
        b = folge[i + 1][1] if i + 1 < len(folge) else bis_
        els.append(peep_voll(prefix + n, x, unten, hoehe, c, anim=("pop" if i == 0 else "cut"), d=(d if i == 0 else 0.0), bis=b))
    return els


def allein(p, cue, folge, x=XS):
    """Eine Figur allein rechts neben der Tafel, mit Namensschild ab dem ersten Bild der Folie."""
    return kette(p + "_", x, [(folge[0][0], cue)] + list(folge[1:])) + [namensschild(NAME[p], x, BR, cue, FARBE[p], d=0.2)]


def paar(cue, p1, f1, p2, f2):
    els = kette(p1 + "_", X1, [(f1[0][0], cue)] + list(f1[1:])) + kette(p2 + "_", X2, [(f2[0][0], cue)] + list(f2[1:]), d=0.2)
    return els + [namensschild(NAME[p1], X1, BR, cue, FARBE[p1], d=0.2), namensschild(NAME[p2], X2, BR, cue, FARBE[p2], d=0.3)]


TX = {"IR": 1370, "WO": 1590, "UL": 1790}
TH = 420


def trio(cue, ir, wo, ul):
    els = []
    for p, f, d in (("IR", ir, 0.0), ("WO", wo, 0.15), ("UL", ul, 0.3)):
        els += kette(p + "_", TX[p], [(f[0][0], cue)] + list(f[1:]), d=d, hoehe=TH)
        els.append(namensschild(NAME[p], TX[p], BR, cue, FARBE[p], d=0.2 + d))
    return els


def stufen(folge, x, unten, hoehe, rede=None):
    """Figur in der Fallszene: folge = [(Bildname, Cue), …]; rede = {Bildname: (Cue, Bis)} für Figurenrede."""
    els = []
    for i, (n, c) in enumerate(folge):
        b = folge[i + 1][1] if i + 1 < len(folge) else None
        if rede and n in rede:
            els += redet(n, x, unten, hoehe, c, b)
        else:
            els.append(peep_voll(n, x, unten, hoehe, c, anim=("pop" if i == 0 and c != NULL else "cut"), bis=b))
    return els


# A1 Fall: in der Wohnung -------------------------------------------------------------------------------------------------
BODEN, GH = 900, 520
IRX, WOX, ULX = 330, 640, 1580
IRa = ("IR_redet_r", IRX, BODEN, GH)
WOa = ("WO_redet_r", WOX, BODEN, GH)
ULa = ("UL_redet", ULX, BODEN, GH)
folie([(NULL, "Fall · Irmgard, Wolfram und Ulrich"), ("kk", "Fall · Der Katzenkönig"), ("motiv", "Fall · Das Motiv"),
       ("i1", "Fall · Das Menschenopfer"), ("glaubt", "Fall · Ein Leben gegen Millionen")], [
    linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK),
    pl("Irmgard, Wolfram und Ulrich", 70, 40, NULL, fill=GELB, size=36, bis="motiv"),
    # kleiner Tisch mit Kerze (Rituale)
    karte(890, 742, 320, 34, NULL, fill=HOLZ, rund=10, schatten=0, rand=5),
    karte(1028, 776, 44, BODEN - 776, NULL, fill=HOLZD, rund=6, schatten=0, rand=5),
    szene(ficon("tabler", "candle", 1050, 744, 64, beim("kk", "Ritualen"), fuell=GELB), "091streichholz*", 1.0, versatz=0.05),
    pl("Tricks und Rituale", 1050, 640, beim("kk", "Ritualen"), fill=WEISS, size=28, anker="m", bis="i1"),
    # Figuren ab 0,0 s
    *stufen([("IR_ruhig_r", NULL), ("IR_kuehl_r", "motiv"), ("IR_redet_r", "i1"), ("IR_ernst_r", "u1")], IRX, BODEN, GH,
            rede={"IR_redet_r": 1}),
    *stufen([("WO_ruhig_r", NULL), ("WO_ernst_r", beim("motiv", "Wolfram")), ("WO_redet_r", "w1"), ("WO_ernst_r", "glaubt")],
            WOX, BODEN, GH, rede={"WO_redet_r": 1}),
    *stufen([("UL_ruhig", NULL), ("UL_staunt", "kk"), ("UL_zweifel", "i1"), ("UL_redet", "u1"), ("UL_zweifel", "w1"),
             ("UL_glaubt", "glaubt")], ULX, BODEN, GH, rede={"UL_redet": 1}),
    *[namensschild(NAME[p], x, BODEN, NULL, FARBE[p]) for p, x in (("IR", IRX), ("WO", WOX), ("UL", ULX))],
    # Ulrich: Polizeibeamter, leicht zu beeinflussen
    pl("Polizeibeamter", ULX, 290, beim("ulrich", "Polizeibeamter"), fill=BLAU, size=30, anker="m", bis="kk"),
    ficon("tabler", "id-badge-2", 1330, 600, 90, beim("ulrich", "Polizeibeamter"), fuell=WEISS, bis="kk"),
    pl("leicht zu beeinflussen", ULX, 200, beim("ulrich", "leicht"), fill=WEISS, size=30, anker="m", bis="kk"),
    # der Katzenkönig nur als Krone in Ulrichs Gedankenblase
    blase("denk", 400, 300, beim("kk", "Katzenkönig"), 1180, 250, figur=("UL_staunt", ULX, BODEN, GH), bis="i1"),
    ficon("tabler", "crown", 1180, 260, 120, beim("kk", "Katzenkönig"), fuell=GELB, bis="i1"),
    pl("der Katzenkönig", 1180, 455, beim("kk", "Katzenkönig"), fill=GELB, size=30, anker="m", bis="i1"),
    pl("seit Jahrtausenden das Böse?", 1180, 535, beim("kk", "Jahrtausenden"), fill=WEISS, size=28, anker="m", bis="i1"),
    # Motiv: Irmgard will die Frau ihres früheren Freundes töten lassen; Wolfram einverstanden
    blase("denk", 400, 280, "motiv", 680, 230, figur=("IR_kuehl_r", IRX, BODEN, GH), bis="i1"),
    ficon("tabler", "flower", 680, 230, 90, "motiv", fuell=ROT, bis="i1"),
    pl("Hass und Eifersucht", 680, 255, beim("motiv", "Hass"), fill=ROTHELL, size=28, anker="m", bis="i1"),
    ficon("tabler", "thumb-up", 830, 640, 70, beim("motiv", "einverstanden"), fuell=GELB, bis="i1"),
    pl("einverstanden", 830, 660, beim("motiv", "einverstanden"), fill=WEISS, size=28, anker="m", bis="i1"),
    # Figurenrede
    blase("sprech", 900, 260, "i1", 720, 200, inhalt=["Der Katzenkönig verlangt ein Menschenopfer:",
          "die Frau aus dem Blumenladen.", "Sonst vernichtet er Millionen Menschen."], textsize=30, figur=IRa, bis="u1"),
    ficon("tabler", "world", 1180, 540, 100, beim("i1", "Millionen"), fuell=BLAU, bis="tat"),
    pl("Millionen Menschen?", 1180, 560, beim("i1", "Millionen"), fill=WEISS, size=28, anker="m", bis="glaubt"),
    blase("sprech", 460, 180, "u1", 1420, 220, inhalt=["Aber das wäre Mord."], textsize=34, figur=ULa, bis="w1"),
    blase("sprech", 720, 220, "w1", 900, 220, inhalt=["Das Tötungsverbot gilt für uns nicht.", "Wir retten die Menschheit."],
          textsize=30, figur=WOa, bis="glaubt"),
    # Ulrich wägt ab
    ficon("tabler", "scale", 1350, 540, 100, "glaubt", fuell=GELB),
    pl("ein Leben gegen Millionen", 1180, 250, "glaubt", fill=GELB, size=32, anker="m"),
])

# A2 Fall: vor dem Blumenladen (kein Angriff im Bild; das Opfer erscheint nicht als Figur) -------------------------------------
LX0 = 1380
folie([("tat", "Fall · Im Blumenladen"), ("lebt", "Fall · Sie überlebt"), ("frage", "Fall · Die Frage")], [
    linienzug([(60, BODEN), (1860, BODEN)], "tat", breite=7, farbe=INK),
    ficon("tabler", "moon", 1720, 210, 90, "tat", fuell=GELB, bis="frage"),
    pl("später Abend", 1720, 230, "tat", fill=WEISS, size=28, anker="m", bis="frage"),
    szene(ficon("tabler", "building-store", LX0, BODEN, 340, beim("tat", "Blumenladen"), fuell=WEISS, bis="frage"), "091glocke*",
          1.0, versatz=0.05),
    ficon("tabler", "flower", 1640, BODEN, 100, beim("tat", "Blumenladen"), fuell=ROT, bis="frage"),
    ficon("tabler", "plant-2", 1760, BODEN, 90, beim("tat", "Blumenladen"), fuell=GRUEN, bis="frage"),
    pl("Blumenladen", LX0, 480, beim("tat", "Blumenladen"), fill=GELB, size=30, anker="m", bis="frage"),
    pl("sie ahnt nichts", LX0, 390, beim("tat", "nichts"), fill=WEISS, size=30, anker="m", bis="flieht"),
    *stufen([("UL_glaubt_r", "tat"), ("UL_still", "flieht"), ("UL_denkt_r", "frage")], 760, BODEN, GH),
    namensschild("Ulrich", 760, BODEN, "tat", FARBE["UL"], d=0.2),
    pl("andere helfen ihr", LX0, 390, beim("flieht", "andere"), fill=WEISS, size=30, anker="m", bis="lebt"),
    ficon("tabler", "door-exit", 520, BODEN, 100, beim("flieht", "flieht"), fuell=WEISS, bis="frage"),
    pl("flieht, rechnet mit ihrem Tod", 640, 290, beim("flieht", "flieht"), fill=ROTHELL, size=28, anker="m", bis="frage"),
    ficon("tabler", "heart", LX0, 440, 90, "lebt", fuell=GRUEN, bis="frage"),
    pl("Sie überlebt.", LX0, 300, "lebt", fill=GRUEN, size=32, anker="m", bis="frage"),
    # Die Frage: Hintermänner treten dazu
    *kette("IR_", 1300, [("ernst", "frage")], hoehe=GH, unten=BODEN),
    *kette("WO_", 1600, [("ernst", "frage")], d=0.15, hoehe=GH, unten=BODEN),
    namensschild("Irmgard", 1300, BODEN, "frage", FARBE["IR"], d=0.2),
    namensschild("Wolfram", 1600, BODEN, "frage", FARBE["WO"], d=0.3),
    pl("hat selbst gehandelt", 760, 290, beim("frage", "hat"), fill=WEISS, size=30, anker="m"),
    pl("nur Anstifter?", 1450, 170, beim("frage", "nur"), fill=WEISS, size=34, anker="m"),
    pl("oder Täter hinter dem Täter?", 1300, 260, "frage2", fill=PINK, size=34, anker="m"),
])

# B Sachverhalt -------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    glyphen("Irmgard und Wolfram bringen den leicht beeinflussbaren Polizeibeamten Ulrich mit Tricks und Ritualen dazu, an "
            "den „Katzenkönig“ zu glauben, der seit Jahrtausenden das Böse verkörpere. Aus Hass und Eifersucht will Irmgard die "
            "Frau ihres früheren Freundes töten lassen; Wolfram ist einverstanden."),
    glyphen("Sie reden Ulrich ein, der Katzenkönig verlange die Frau als Menschenopfer, sonst vernichte er Millionen "
            "Menschen; das Tötungsverbot gelte für sie nicht. Ulrich erkennt, dass das Mord wäre, hält die Tat zur Rettung der "
            "Menschheit aber für erlaubt. Nach den Anweisungen von Wolfram greift er die ahnungslose Frau in ihrem Blumenladen "
            "von hinten an, um sie zu töten. Als andere ihr helfen, flieht er und rechnet mit ihrem Tod. Sie überlebt."),
    glyphen("Nach BGHSt 35, 347 (Katzenkönig), vereinfacht, andere Namen."),
], "Wie haben sich Ulrich, Irmgard und Wolfram strafbar gemacht?")

# C Der echte Fall --------------------------------------------------------------------------------------------------------
folie([("echt", "Der echte Fall · Katzenkönig, BGHSt 35, 347"), ("bgh2", "Der echte Fall › Schuldsprüche bestätigt")], rechts_frei([
    *tafel("echt", "Der Katzenkönig-Fall"),
    z("BGH, Urteil vom 15.9.1988", 110, 185, beim("echt", "Bundesgerichtshof"), "Bold", 34),
    fund("4 StR 352/88, BGHSt 35, 347", 110, 235, beim("echt", "Urteil")),
    z("vereinfacht erzählt, andere Namen", 110, 310, "vereinf", size=32),
    z("Landgericht: alle 3 wegen versuchten Mordes", 110, 385, "lg", size=32),
    fund("BGHSt 35, 347, 347 f.", 110, 432, "lg"),
    ok(135, 525, "bgh2", gr=18),
    z("BGH: Schuldsprüche bleiben bestehen", 175, 505, "bgh2", "Bold", 32),
    fb(110, 590, 1040, 140, GELB, beim("bgh2", "Aufgehoben"), [("aufgehoben nur die Strafen: Milderung beim", "ExtraBold", 31, INK),
                                                                   ("Versuch nicht ausreichend geprüft", "ExtraBold", 31, INK)]),
    fund("BGHSt 35, 347, 355 f. (§§ 23 Abs. 2, 49 Abs. 1 StGB)", 110, 745, beim("bgh2", "Milderung")),
    *trio("echt", [("ruhig",)], [("ruhig",)], [("ruhig",)]),
    pl("Katzenkönig-Fall", 1580, 160, beim("echt", "Katzenkönig-Fall"), fill=GELB, size=30, anker="m", bis="lg"),
    ficon("tabler", "crown", 1580, 380, 110, beim("echt", "Katzenkönig-Fall"), fuell=GELB, bis="lg"),
    pl("Landgericht: versuchter Mord", 1580, 160, "lg", fill=WEISS, size=28, anker="m", anim="cut", bis="bgh2"),
    ficon("tabler", "gavel", 1580, 380, 120, "lg", fuell=HOLZ, anim="cut"),
    pl("BGH: Schuldsprüche halten", 1580, 160, "bgh2", fill=GRUEN, size=28, anker="m", anim="cut"),
]))

# D A. Ulrich: versuchter Mord ---------------------------------------------------------------------------------------------
PA = "A. Ulrich"
folie([("ua", f"{PA} › Versuchter Mord"), ("heim", f"{PA} › Versuchter Mord › Heimtücke"), ("rt", f"{PA} › Rücktritt")], rechts_frei([
    *tafel("ua", "A. Strafbarkeit von Ulrich"),
    z("Die Frau lebt: Versuch", 110, 185, beim("ua", "Frau"), size=32),
    z("Versuchter Mord, §§ 211, 212, 22, 23 Abs. 1 StGB", 110, 240, beim("ua", "versuchter"), "Bold", 34),
    ok(135, 345, "entschl", gr=18),
    z("Tatentschluss: Tötungsvorsatz", 175, 325, "entschl", "Bold", 32),
    ok(135, 415, beim("entschl", "unmittelbar"), gr=18),
    z("unmittelbares Ansetzen", 175, 395, beim("entschl", "unmittelbar"), "Bold", 32),
    ok(135, 485, beim("heim", "Arg-"), gr=18),
    z("Heimtücke: Arg- und Wehrlosigkeit", 175, 465, beim("heim", "Arg-"), "Bold", 32),
    z("bewusst ausgenutzt", 175, 512, beim("heim", "bewusst"), size=32),
    fund("BGHSt 35, 347, 349", 175, 560, beim("heim", "bewusst")),
    nein(135, 645, "rt", gr=18),
    z("Rücktritt: nein, floh ohne Rettungsbemühen", 175, 625, "rt", "Bold", 32),
    *allein("UL", "ua", [("denkt",), ("still", "rt")]),
    pl("versuchter Mord?", IX + 40, 160, beim("ua", "versuchter"), fill=WEISS, size=30, anker="m", bis="heim"),
    ficon("tabler", "heart", IX + 40, 380, 90, beim("ua", "Frau"), fuell=GRUEN, bis="heim"),
    pl("Heimtücke", IX + 40, 160, "heim", fill=ROTHELL, size=30, anker="m", anim="cut", bis="rt"),
    ficon("tabler", "eye-off", IX + 40, 380, 100, "heim", fuell=WEISS, anim="cut", bis="rt"),
    pl("kein Rücktritt", IX + 40, 160, "rt", fill=ROTHELL, size=30, anker="m", anim="cut"),
    ficon("tabler", "door-exit", IX + 40, 380, 100, "rt", fuell=WEISS, anim="cut"),
]))

# E Rechtswidrigkeit: § 34 -------------------------------------------------------------------------------------------------
folie([("n34", f"{PA} › Rechtswidrigkeit, § 34 StGB"), ("bew", f"{PA} › Rechtswidrigkeit › Bewertungsirrtum")], rechts_frei([
    *tafel("n34", "Rechtswidrigkeit: § 34 StGB"),
    nein(135, 205, beim("n34", "Eine"), gr=18),
    z("keine echte Gefahr", 175, 185, beim("n34", "Eine"), "Bold", 32),
    z("Ulrich glaubte an die Gefahr", 175, 260, "glaube", size=32),
    nein(135, 355, beim("glaube", "selbst"), gr=18),
    z("selbst dann: Leben gegen Leben nicht abwägbar", 175, 335, beim("glaube", "selbst"), "Bold", 32),
    fund("BGHSt 35, 347, 350", 175, 382, beim("glaube", "abwägen")),
    fb(110, 460, 1040, 140, GELB, "bew", [("falsche Abwägung: Bewertungsirrtum", "ExtraBold", 32, INK),
                                         ("Vorsatz bleibt, es geht um einen Verbotsirrtum", "ExtraBold", 32, INK)]),
    fund("BGHSt 35, 347, 350", 110, 615, beim("bew", "Verbotsirrtum")),
    *allein("UL", "n34", [("denkt",), ("zweifel", "bew")]),
    pl("§ 34 StGB?", IX + 40, 160, beim("n34", "Paragraf"), fill=GELB, size=30, anker="m", bis="glaube"),
    pl("Leben gegen Leben?", IX + 40, 160, "glaube", fill=WEISS, size=30, anker="m", anim="cut", bis="bew"),
    ficon("tabler", "scale", IX + 40, 380, 110, "glaube", fuell=GELB),
    pl("Bewertungsirrtum", IX + 40, 160, "bew", fill=GELB, size=30, anker="m", anim="cut"),
]))

# F Schuld: § 35 -----------------------------------------------------------------------------------------------------------
folie([("n35", f"{PA} › Schuld › § 35 StGB"), ("abs2", f"{PA} › Schuld › § 35 Abs. 2 StGB")], rechts_frei([
    *tafel("n35", "Schuld: § 35 StGB"),
    z("entschuldigender Notstand?", 110, 185, "n35", "Bold", 34),
    z("nur, wer die Gefahr abwenden will von:", 110, 260, "kreis", size=32),
    ok(175, 340, beim("kreis", "sich"), gr=18), z("sich selbst", 215, 320, beim("kreis", "sich"), size=32),
    ok(175, 400, beim("kreis", "Angehörigen"), gr=18), z("einem Angehörigen", 215, 380, beim("kreis", "Angehörigen"), size=32),
    ok(175, 460, beim("kreis", "nahestehenden"), gr=18),
    z("einer ihm nahestehenden Person", 215, 440, beim("kreis", "nahestehenden"), size=32),
    nein(135, 545, "fremd", gr=18),
    z("Ulrich: Millionen Menschen, nicht sich", 175, 525, "fremd", "Bold", 32),
    z("oder seine Angehörigen", 175, 570, beim("fremd", "nicht"), "Bold", 32),
    fund("BGHSt 35, 347, 350", 175, 617, beim("fremd", "nicht")),
    nein(135, 700, "abs2", gr=18),
    z("auch § 35 Abs. 2: vermeintlicher Notstand", 175, 680, "abs2", "Bold", 32),
    *allein("UL", "n35", [("denkt",), ("glaubt", "fremd")]),
    pl("Notstand?", IX + 40, 160, "n35", fill=WEISS, size=30, anker="m", bis="fremd"),
    pl("Millionen Fremde", IX + 40, 160, "fremd", fill=ROTHELL, size=30, anker="m", anim="cut"),
    ficon("tabler", "world", IX + 40, 380, 100, "fremd", fuell=BLAU),
]))

# G Wortlautkarte § 17 -----------------------------------------------------------------------------------------------------
W17 = [[("„Fehlt dem Täter bei Begehung der Tat ", 0), ("die Einsicht,", "a")],
       [("Unrecht zu tun", "a"), (", so handelt er ohne Schuld, wenn er", 0)],
       [("diesen Irrtum ", 0), ("nicht vermeiden konnte.", "b"), (" Konnte der", 0)],
       [("Täter den Irrtum vermeiden, so ", 0), ("kann die Strafe", "c")],
       [("nach § 49 Abs. 1 ", 0), ("gemildert werden.", "c"), ("“", 0)]]
folie([("p17", f"{PA} › Schuld › Verbotsirrtum, § 17 StGB"), ("verm", f"{PA} › Schuld › Verbotsirrtum vermeidbar"),
       ("uerg", f"{PA} › Ergebnis: schuldhaft")], rechts_frei([
    *tafel("p17", "Verbotsirrtum: § 17 StGB"),
    *wortlaut(110, 180, 1040, 250, "p17", W17, 31,
              {"a": beim("p17", "Einsicht"), "b": beim("p17", "nicht"), "c": beim("satz2", "kann")}, "§ 17 StGB"),
    z("Ulrich hielt die Tötung für erlaubt", 110, 500, "irrt", "Bold", 32),
    z("vermeidbar: als Polizeibeamter bei gebührender", 110, 555, beim("verm", "Gerade"), size=31),
    z("Gewissensanspannung, Befragung etwa eines Geistlichen", 110, 600, beim("verm", "Befragung"), size=31),
    fund("BGHSt 35, 347, 350", 110, 645, beim("verm", "Geistlichen")),
    fb(110, 710, 1040, 90, GRUEN, "uerg", [("Ulrich handelt schuldhaft", "ExtraBold", 34, INK)]),
    *allein("UL", "p17", [("denkt",), ("glaubt", "irrt"), ("schuld", "verm")]),
    pl("§ 17 StGB", IX + 40, 160, beim("p17", "Paragraf"), fill=GELB, size=30, anker="m", bis="irrt"),
    pl("für erlaubt gehalten", IX + 40, 160, "irrt", fill=WEISS, size=28, anker="m", anim="cut", bis="verm"),
    ficon("tabler", "world", IX + 40, 380, 100, "irrt", fuell=BLAU, bis="verm"),
    pl("vermeidbar", IX + 40, 160, "verm", fill=ROTHELL, size=30, anker="m", anim="cut"),
    ficon("tabler", "id-badge-2", IX + 40, 380, 100, "verm", fuell=WEISS, anim="cut"),
]))

# H B. Irmgard und Wolfram: Wortlautkarte § 25 Abs. 1 ---------------------------------------------------------------------
PB = "B. Irmgard und Wolfram"
W25 = [[("„(1) Als Täter wird bestraft, wer die Straftat selbst", 0)],
       [("oder ", 0), ("durch einen anderen", "a"), (" begeht.“", 0)]]
folie([("hb", f"{PB}"), ("p25", f"{PB} › § 25 Abs. 1 Alt. 2 StGB"), ("prob", f"{PB} › Vordermann voll verantwortlich")],
      rechts_frei([
    *tafel("hb", "B. Strafbarkeit von Irmgard und Wolfram"),
    nein(135, 205, beim("hb", "Sie"), gr=18),
    z("Tat nicht selbst ausgeführt", 175, 185, beim("hb", "Sie"), "Bold", 32),
    *wortlaut(110, 260, 1040, 130, "p25", W25, 32, {"a": beim("p25", "durch")}, "§ 25 Abs. 1 StGB"),
    z("Alt. 2: mittelbare Täterschaft", 110, 460, "alt2", "Bold", 34),
    z("meist fehlt dem Werkzeug Vorsatz oder Schuld", 110, 530, "werk", size=32),
    fb(110, 610, 1040, 90, ROTHELL, "prob", [("Ulrich: vorsätzlich und schuldhaft", "ExtraBold", 34, INK)]),
    *paar("hb", "IR", [("ernst",), ("kuehl", "prob")], "WO", [("ruhig",), ("ernst", "prob")]),
    pl("selbst ausgeführt? nein", MB, 160, beim("hb", "Sie"), fill=WEISS, size=28, anker="m", bis="p25"),
    pl("durch einen anderen", MB, 160, beim("p25", "durch"), fill=GELB, size=30, anker="m", bis="werk"),
    pl("Werkzeug?", MB, 160, "werk", fill=WEISS, size=30, anker="m", anim="cut", bis="prob"),
    pl("voll verantwortlich", MB, 160, "prob", fill=ROTHELL, size=30, anker="m", anim="cut"),
]))

# I Streit: Verantwortungsprinzip und BGH --------------------------------------------------------------------------------
folie([("vp", f"{PB} › Streit › Verantwortungsprinzip"), ("bgh", f"{PB} › Streit › BGH"), ("herr", f"{PB} › Streit › Tatherrschaft")],
      rechts_frei([
    *tafel("vp", "Täter oder nur Anstifter?"),
    karte(110, 180, 1040, 150, "vp", fill=LILAHELL, rund=18, schatten=6, rand=4),
    z("Verantwortungsprinzip: mittelbare Täterschaft", 140, 198, "vp", "Bold", 31, rechts=1140),
    z("endet beim voll verantwortlichen Vordermann", 140, 248, beim("vp", "wo"), size=31, rechts=1140),
    z("dann nur Anstiftung, § 26 StGB", 140, 350, "anst", "Bold", 32),
    fund("BGHSt 35, 347, 351 f. (mit Nachweisen)", 140, 397, "anst"),
    karte(110, 460, 1040, 150, "bgh", fill=GRUENHELL, rund=18, schatten=6, rand=4),
    z("BGH: Vermeidbarkeit allein kein taugliches", 140, 478, beim("bgh", "Allein"), "Bold", 31, rechts=1140),
    z("Abgrenzungskriterium, auch Ulrich fehlte", 140, 523, beim("bgh", "Abgrenzungskriterium"), size=31, rechts=1140),
    z("die Unrechtseinsicht", 140, 566, beim("bgh", "Unrechtseinsicht"), size=31, rechts=1140),
    fb(110, 650, 1040, 90, GELB, "herr", [("maßgeblich: Tatherrschaft, wertend im Einzelfall", "ExtraBold", 31, INK)]),
    fund("BGHSt 35, 347, 353", 110, 755, beim("herr", "wertend")),
    *paar("vp", "IR", [("ernst",), ("kuehl", "bgh")], "WO", [("ernst",), ("still", "bgh")]),
    pl("nur Anstifter?", MB, 160, "anst", fill=WEISS, size=30, anker="m", bis="bgh"),
    pl("BGH: nein", MB, 160, "bgh", fill=GRUEN, size=30, anker="m", anim="cut", bis="herr"),
    pl("Tatherrschaft", MB, 160, "herr", fill=GELB, size=30, anker="m", anim="cut"),
]))

# J BGH-Formel (wörtlich, BGHSt 35, 347, 354) --------------------------------------------------------------------------------
WF = [[("„Mittelbarer Täter eines Tötungs- oder versuchten", 0)],
      [("Tötungsdelikts ist jedenfalls derjenige, der mit Hilfe", 0)],
      [("des von ihm ", 0), ("bewußt hervorgerufenen Irrtums", "a"), (" das", 0)],
      [("Geschehen ", 0), ("gewollt auslöst und steuert", "b"), (", so daß der", 0)],
      [("Irrende bei wertender Betrachtung als ein – wenn", 0)],
      [("auch (noch) ", 0), ("schuldhaft handelndes – Werkzeug", "c")],
      [("anzusehen ist.“", 0)]]
folie([("formel", f"{PB} › Die Formel des BGH"), ("thdt", f"{PB} › Täter hinter dem Täter")], rechts_frei([
    *tafel("formel", "Die Formel des BGH"),
    *wortlaut(110, 180, 1040, 340, "formel", WF, 31,
              {"a": beim("formel", "bewusst"), "b": beim("formel", "gewollt"), "c": beim("werkz", "schuldhaft")},
              "BGHSt 35, 347, 354"),
    fb(110, 600, 1040, 90, GRUEN, "thdt", [("Täter hinter dem Täter", "ExtraBold", 34, INK)]),
    z("Begriff aus der Lehre", 110, 705, beim("thdt", "Täter"), size=28, farbe=TEXT),
    *trio("formel", [("kuehl",)], [("kuehl",)], [("glaubt",)]),
    pl("bewusst erzeugter Irrtum", 1580, 160, beim("formel", "bewusst"), fill=WEISS, size=28, anker="m", bis="werkz"),
    pl("schuldhaftes Werkzeug", 1580, 160, "werkz", fill=GELB, size=28, anker="m", anim="cut", bis="thdt"),
    pl("Täter hinter dem Täter", 1580, 160, "thdt", fill=GRUEN, size=28, anker="m", anim="cut"),
]))

# K Subsumtion ---------------------------------------------------------------------------------------------------------------
folie([("subs", f"{PB} › Subsumtion"), ("wissen", f"{PB} › Tatherrschaft kraft überlegenen Wissens")], rechts_frei([
    *tafel("subs", "So liegt es hier"),
    ok(135, 205, beim("subs", "hervorgerufen"), gr=18),
    z("Wahn hervorgerufen", 175, 185, beim("subs", "hervorgerufen"), "Bold", 32),
    ok(135, 270, beim("subs", "bewusst"), gr=18),
    z("bewusst ausgenutzt: Bedenken ausgeschaltet", 175, 250, beim("subs", "bewusst"), "Bold", 32),
    ok(135, 335, "anw", gr=18),
    z("wesentliche Teile der Ausführung bestimmt", 175, 315, "anw", "Bold", 32),
    z("Ulrich hielt sich an ihre Anweisungen", 175, 362, beim("anw", "Ulrich"), size=32),
    fund("BGHSt 35, 347, 354", 175, 409, beim("anw", "Anweisungen")),
    fb(110, 480, 1040, 140, GRUEN, "wissen", [("Tatherrschaft kraft Einwirkung", "ExtraBold", 32, INK),
                                             ("und überlegenen Wissens", "ExtraBold", 32, INK)]),
    fund("BGHSt 35, 347, 354 f.", 110, 635, beim("wissen", "Wissens")),
    z("untereinander: gemeinschaftlich", 110, 700, "gem", "Bold", 32),
    fund("BGHSt 35, 347, 351", 110, 747, "gem"),
    *paar("subs", "IR", [("kuehl",), ("ernst", "gem")], "WO", [("kuehl",), ("ernst", "gem")]),
    pl("Wahn hervorgerufen", MB, 160, beim("subs", "hervorgerufen"), fill=WEISS, size=28, anker="m", bis="anw"),
    ficon("tabler", "crown", MB, 380, 100, beim("subs", "hervorgerufen"), fuell=GELB, bis="anw"),
    pl("Anweisungen", MB, 160, "anw", fill=WEISS, size=30, anker="m", anim="cut", bis="wissen"),
    ficon("tabler", "clipboard-list", MB, 380, 100, "anw", fuell=WEISS, anim="cut", bis="wissen"),
    pl("überlegenes Wissen", MB, 160, "wissen", fill=GRUEN, size=28, anker="m", anim="cut"),
    ficon("tabler", "bulb", MB, 380, 100, "wissen", fuell=GELB, anim="cut"),
]))

# L Warum der Streit zählt -----------------------------------------------------------------------------------------------
folie([("heimt", f"{PB} › Warum der Streit zählt"), ("nb", f"{PB} › niedrige Beweggründe")], rechts_frei([
    *tafel("heimt", "Der Streit zählt hier"),
    karte(110, 180, 1040, 200, "heimt", fill=ROTHELL, rund=18, schatten=6, rand=4),
    z("Anstiftung zum Mord, § 26 StGB:", 140, 200, beim("heimt", "Als"), "Bold", 32, rechts=1140),
    z("Kenntnis der Heimtücke nötig", 140, 250, beim("heimt", "Heimtücke"), size=32, rechts=1140),
    nein(165, 325, beim("heimt", "Das"), gr=16),
    z("nach dem Landgericht nicht nachweisbar", 200, 305, beim("heimt", "Das"), size=32, rechts=1140),
    karte(110, 420, 1040, 140, "nb", fill=GRUENHELL, rund=18, schatten=6, rand=4),
    ok(165, 465, beim("nb", "eigenen"), gr=16),
    z("als Täter: eigene niedrige Beweggründe", 200, 445, beim("nb", "eigenen"), "Bold", 32, rechts=1140),
    z("(Mordmerkmal, § 211 Abs. 2 StGB)", 200, 495, beim("nb", "Beweggründe"), size=28, farbe=TEXT, rechts=1140),
    fund("BGHSt 35, 347, 351", 110, 580, beim("nb", "Beweggründe")),
    *paar("heimt", "IR", [("ernst",), ("still", "nb")], "WO", [("ernst",), ("still", "nb")]),
    pl("Heimtücke gekannt?", MB, 160, beim("heimt", "Heimtücke"), fill=WEISS, size=28, anker="m", bis="nb"),
    pl("niedrige Beweggründe", MB, 160, "nb", fill=ROTHELL, size=28, anker="m", anim="cut"),
]))

# M Ergebnis -----------------------------------------------------------------------------------------------------------------
folie([("erg", "Ergebnis · Irmgard und Wolfram: mittelbare Täter"), ("erg2", "Ergebnis › Ulrich: versuchter Mord")], rechts_frei([
    *tafel("erg", "Ergebnis"),
    fb(110, 190, 1040, 140, GRUEN, "erg", [("Irmgard und Wolfram: versuchter Mord", "ExtraBold", 32, INK),
                                         ("in mittelbarer Täterschaft", "ExtraBold", 32, INK)]),
    fund("§§ 211, 212, 22, 23 Abs. 1, 25 Abs. 1 Alt. 2 StGB", 110, 345, beim("erg", "Paragraf")),
    fb(110, 420, 1040, 140, BLAUHELL, "erg2", [("Ulrich: versuchter Mord,", "ExtraBold", 32, INK),
                                             ("Milderung möglich, § 17 S. 2 StGB", "ExtraBold", 32, INK)]),
    *trio("erg", [("still",)], [("still",)], [("schuld",)]),
    ficon("tabler", "gavel", 1580, 380, 120, beim("erg", "Ergebnis"), fuell=HOLZ),
]))

# N Klausurtipp (Lexi) -----------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · zuerst der Vordermann"), ("tipp2", "Klausurtipp · Streit nur, wenn es darauf ankommt")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Zuerst den Vordermann vollständig prüfen,", 200, 200, "tipp", "Bold", 34),
    z("bis zur Schuld", 200, 250, beim("tipp", "bis"), size=34),
    z("erst dort: voll verantwortlich?", 200, 300, beim("tipp", "Erst"), size=34),
    z("Streit nur entscheiden,", 200, 390, "tipp2", "Bold", 34),
    z("wenn es darauf ankommt", 200, 440, beim("tipp2", "wenn"), size=34),
    z("hier: Anstiftung scheitert", 200, 530, "tipp3", "Bold", 34),
    z("am Vorsatz zur Heimtücke", 200, 580, beim("tipp3", "Vorsatz"), size=34),
    *redet("LX_warnt", LXX, BR, FR + 60, "tipp", "sch"),
    namensschild("Lexi", LXX, BR, "tipp", GELB, d=0.2),
])

# O Klausurschema ------------------------------------------------------------------------------------------------------------
K1, K2 = 150, 230
PS_ = "Klausurschema"
folie([("sch", PS_), ("sa", f"{PS_} › A. Ulrich: versuchter Mord"), ("sa2", f"{PS_} › A. Rechtswidrigkeit"),
       ("sa3", f"{PS_} › A. Schuld"), ("sa4", f"{PS_} › A. Rücktritt"), ("sb", f"{PS_} › B. Irmgard und Wolfram"),
       ("sb1", f"{PS_} › B. Tatentschluss"), ("sb2", f"{PS_} › B. unmittelbares Ansetzen"),
       ("sb3", f"{PS_} › B. Rechtswidrigkeit und Schuld")], [
    karte(60, 50, 1800, 920, "sch"),
    titel("Klausurschema: Katzenkönig-Fall", 110, 90, "sch", 50),
    z("A. Strafbarkeit von Ulrich: versuchter Mord, §§ 211, 212, 22, 23 Abs. 1", K1, 180, "sa", "Bold", 34, rechts=1820),
    z("Vorprüfung · Tatentschluss mit Heimtücke · unmittelbares Ansetzen", K2, 235, "sa1", size=32, rechts=1820),
    z("Rechtswidrigkeit: § 34 scheitert", K2, 285, "sa2", size=32, rechts=1820),
    z("Schuld: kein Notstand (§ 35), Verbotsirrtum (§ 17) vermeidbar", K2, 335, "sa3", size=32, rechts=1820),
    z("kein Rücktritt", K2, 385, "sa4", size=32, rechts=1820),
    z("B. Strafbarkeit von Irmgard und Wolfram:", K1, 465, "sb", "Bold", 34, rechts=1820),
    z("versuchter Mord in mittelbarer Täterschaft, § 25 Abs. 1 Alt. 2", K1, 515, beim("sb", "versuchter"), "Bold", 34,
      rechts=1820),
    z("Tatentschluss: Tatherrschaft trotz voll verantwortlichen Vordermanns", K2, 575, "sb1", size=32, rechts=1820),
    z("mit dem Streit", K2 + 40, 622, beim("sb1", "Streit"), size=30, farbe=TEXT, rechts=1820),
    z("und niedrige Beweggründe", K2, 670, beim("sb1", "niedrige"), size=32, rechts=1820),
    z("unmittelbares Ansetzen: spätestens mit dem Ansetzen von Ulrich", K2, 725, "sb2", size=32, rechts=1820),
    z("Rechtswidrigkeit und Schuld", K2, 780, "sb3", size=32, rechts=1820),
])

# P Merksatz (Lexi) --------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Auch hinter einem voll verantwortlichen", 0)], [("Täter kann ein ", 0), ("mittelbarer Täter", "a")],
                 [("stehen.", 0)]], 750, 300, 42, "merke", {"a": beim("merke", "mittelbarer")}),
    *markertext([[("Entscheidend ist, ob er mit einem", 0)], [("bewusst hervorgerufenen Irrtum", "b")],
                 [("das Geschehen auslöst und ", 0), ("steuert", "c"), (".", 0)]], 750, 540, 40, "m2",
                {"b": beim("m2", "bewusst"), "c": beim("m2", "steuert")}),
    *redet("LX_erklaert", 1680, 960, 690, "merke", lexi_bis_ende("merke")),
    namensschild("Lexi", 1680, 960, "merke", GELB, d=0.2),
])
