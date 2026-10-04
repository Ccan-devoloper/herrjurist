"""Folge 137 · Urkunde § 267 StGB: Was ist eine Urkunde? Die 3 Funktionen – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A1 Fall zu Hause (Montag geschwänzt, Femke schreibt die Entschuldigung und ahmt die
Unterschrift der Mutter nach; die Mutter im Nebenzimmer weiß nichts), A2 Fall in der Schule (Abgabe bei Frau Melzer,
Abheften, Frage), B Sachverhalt, C Wortlautkarte § 267 Abs. 1 und Urkundenbegriff, D Perpetuierungs-, E Beweis- (Absichts-/
Zufallsurkunde, Fotokopie), F Garantiefunktion (Beweiszeichen), G Tathandlung: unechte Urkunde (Geistigkeitstheorie),
H schriftliche Lüge, I Verfälschen (Vergleich) und Gebrauchen, J subjektiver Tatbestand, K Gegenvariante (Erlaubnis der
Mutter), L Rechtswidrigkeit, Schuld (§ 19), Ergebnis, eine Tat, M Klausurtipp (Lexi), N Prüfschema, O Merksatz (Lexi).
Femke (16) als Open-Peeps-Figur mit 90 % der Erwachsenenhöhe. Geräusche nur bei sichtbarer Handlung: Stift schreibt
(Zettel), Ordner beim Abheften (Freesound CC0). Hilfsfunktionen (z, pl, tafel, wortlaut, fb, redet mit hörbarem Wortende,
stufen, wechsel, icons, zeile_ok) wie in Folge 131/134, Kopie im eigenen Ordner."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont

bausteine.FIGORDNER = "op_137/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
LILAHELL = (246, 243, 255, 255)
ROTHELL = (253, 232, 228, 255)
GRUENHELL = (232, 247, 233, 255)
BLAUHELL = (228, 238, 253, 255)
CHATGRUEN = (225, 245, 222, 255)
GRAU = (150, 150, 158, 255)
DAUER = bausteine._cj()["dauer"]
NULL = "fall"                     # Szene A steht ab 0,0 s (render_137 setzt alle Elemente bis zur Marke „fall“ auf 0,0 s)

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
    """Wortlautkarte: wörtliches Zitat (gesetze-im-internet.de, Abruf 04.10.2026) in einer hellen Karte, Fundstelle darunter
    rechts. zeilen = Liste von Token-Listen [(text, Schlüssel|0)], hl = {Schlüssel: Cue} (Hervorhebung zum gesprochenen Wort)."""
    for toks in zeilen:
        glyphen("".join(t for t, _ in toks))
    els = [karte(x, y, w, h, cue, fill=(246, 246, 250, 255), rund=18, schatten=6, rand=4)]
    m = markertext(zeilen, x + w / 2, y + 20, size, cue, hl, marker=GELB, lh=1.28)
    assert m[0].x >= x + 10 and m[0].x + m[0].sprite.width <= x + w - 10, f"Wortlaut zu breit ({m[0].sprite.width} > {w})"
    assert m[0].y + m[0].sprite.height <= y + h + 6, f"Wortlaut zu hoch ({m[0].y + m[0].sprite.height} > {y + h})"
    els += m
    q = zeile(glyphen(quelle), 0, 0, quelle_cue or cue, "Bold", 26, farbe=TEXT)
    q.x = x + w - q.sprite.width - 24; q.y = y + h + 8
    els.append(q)
    return els


def fb(x, y, w, h, fill, cue, zeilen, rund=18, anim="rise", d=0.0, bis=None):
    """Wie fl_block, Zeilenabstand passend zur Schriftgröße der Zeilen."""
    from engine import block
    for zz in zeilen:
        glyphen(zz[0])
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


# --- Eigene Hilfsfunktion (wie Folge 131/134): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ------------------
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
X1, X2 = 1420, 1720                     # zwei Figuren
MB = (X1 + X2) // 2
XS = 1580                               # eine Figur rechts
FARBE = {"FE": GRUEN, "ME": LILA, "MU": ROT}
NAME = {"FE": "Femke", "ME": "Frau Melzer", "MU": "Mutter"}
JUNG = 0.9                              # Femke (16): etwa 90 % der Erwachsenenhöhe (FOLGE-ABLAUF Abschnitt 3)


def stufen(p, x, folge, rede=(), bis_=None, unten=BR, hoehe=FR, erst="pop", d=0.0, schild=True, schild_cue=None):
    """Figur im Zwiebelschalenprinzip: folge = [(Ansicht, Cue), …]; Ansichten in rede sprechen (Mund zum Wort).
    Namensschild ab dem ersten Bild und durchgehend."""
    els = []
    for i, (n, c) in enumerate(folge):
        b = folge[i + 1][1] if i + 1 < len(folge) else bis_
        if n in rede:
            els += redet(f"{p}_{n}", x, unten, hoehe, c, b)
        else:
            els.append(peep_voll(f"{p}_{n}", x, unten, hoehe, c, anim=(erst if i == 0 else "cut"), d=(d if i == 0 else 0.0), bis=b))
    if schild:
        els.append(namensschild(NAME[p], x, unten, schild_cue or folge[0][1], FARBE[p], d=d + 0.15, bis=bis_))
    return els


def wechsel(texte, cx, y, size=30, fill=WEISS, anker="m"):
    """Pillen nacheinander an derselben Stelle: texte = [(Text, Cue, Füllung|None), …]; (Text None) = Pause ohne Pille."""
    els = []
    for i, (t, c, f) in enumerate(texte):
        b = texte[i + 1][1] if i + 1 < len(texte) else None
        if t:
            els.append(pl(t, cx, y, c, fill=f or fill, size=size, anker=anker, anim=("pop" if i == 0 else "cut"), bis=b))
    return els


def icons(folge, cx, unten, breite):
    """Requisiten nacheinander an derselben Stelle: folge = [(set, name, Cue, Füllung), …]; (set None) = Lücke."""
    els = []
    for i, (s, n, c, f) in enumerate(folge):
        b = folge[i + 1][2] if i + 1 < len(folge) else None
        if s:
            els.append(ficon(s, n, cx, unten, breite, c, fuell=f, anim=("pop" if i == 0 else "cut"), bis=b))
    return els


def zeile_ok(text, x, y, cue, ja=True, size=32, stil="Regular", **k):
    """Tafelzeile mit Bleistift-Haken bzw. -Kreuz davor (zum gesprochenen Wort)."""
    return [(ok if ja else nein)(x + 25, y + 20, cue, gr=18), z(text, x + 65, y, cue, stil, size, **k)]



def h_(p, h=FR):
    """Femke (16) etwas kleiner als die Erwachsenen."""
    return round(h * JUNG) if p == "FE" else h


def st(p, x, folge, **k):
    k.setdefault("hoehe", h_(p, k.get("hoehe", FR)) if "hoehe" not in k else k["hoehe"])
    return stufen(p, x, folge, **k)


FUNK = ["Perpetuierung", "Beweis", "Garantie"]


def leiste(y, cue, stand, x0=110, size=28, cues=None, bis=None):
    """Funktionenleiste Perpetuierung · Beweis · Garantie; stand = Index der aktuellen Funktion (geprüfte grün,
    aktuelle gelb, folgende weiß), stand=3: alle grün. cues: je Funktion eigener Cue (Aufbau am Wort)."""
    els, x = [], x0
    for i, g in enumerate(FUNK):
        c = cues[i] if cues else cue
        fill = GRUEN if i < stand else (GELB if i == stand else WEISS)
        p = pl(g, x, y, c, fill=fill, size=size, bis=bis)
        els.append(p)
        x = p.x + p.sprite.width + 30
    assert x - 30 <= 1170, f"Leiste zu breit ({x})"
    return els


def zettel(x, y, w, cue, zeilen, size=30, sig=None, sig_cue=None, fill=WEISS, bis=None, extra=None):
    """Die Entschuldigung als Zettel (Karte): zeilen = [(Text, Cue)], darunter die Unterschrift („S. Ohlsen“ und
    Tabler-Icon signature) zum gesprochenen Wort."""
    lh = int(size * 1.35)
    h = 40 + lh * len(zeilen) + (95 if sig else 10)
    k = karte(x, y, w, h, cue, fill=fill, rund=10, schatten=6, rand=4)
    k.bis = bis
    els = [k]
    for i, (t, c) in enumerate(zeilen):
        els.append(z(t, x + 26, y + 22 + i * lh, c, "Bold", size, rechts=x + w - 14, bis=bis))
    if sig:
        yy = y + 22 + lh * len(zeilen) + 12
        els.append(ficon("tabler", "signature", x + 80, yy + 62, 90, sig_cue, bis=bis))
        els.append(z(sig, x + 140, yy + 14, sig_cue, "Bold", 30, rechts=x + w - 14, bis=bis))
    return els


# ======================================================================================================================
# A1 Fall: der Montag und die Entschuldigung (bei Femke zu Hause)
# ======================================================================================================================
BODEN, FH = 880, 520
FX = 300                                  # Femke am Schreibtisch, blickt nach rechts zum Zettel
MUX = 1660                                # Mutter im Nebenzimmer
ZX, ZY, ZW = 610, 220, 640                # Zettel
folie([(NULL, "Fall · Montag: geschwänzt"), ("abend", "Fall · Die Entschuldigung"),
       ("unterschrift", "Fall · Die Unterschrift"), ("mutter", "Fall · Die Mutter weiß nichts")], [
    linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK),
    *st("FE", FX, [("ruhig_r", NULL), ("still_r", "schwaenzt"), ("denkt_r", "abend"), ("eifrig_r", "unterschrift"),
                   ("ruhig_r", "mutter")], unten=BODEN, hoehe=round(FH * JUNG), erst="cut", d=-0.2),
    pl("16 Jahre", FX, 330, beim("fall", "sechzehn"), fill=WEISS, size=28, anker="m", bis="abend"),
    pl("Montag", 70, 40, NULL, fill=GELB, size=36, anim="cut", bis="abend"),
    ficon("fluent-emoji-flat", "school", 1620, 600, 200, "schwaenzt", bis="abend"),
    pl("Femke fehlt", 1620, 640, beim("schwaenzt", "schwänzt"), fill=ROTHELL, size=30, anker="m", bis="abend"),
    pl("Montag, abends", 70, 40, "abend", fill=GELB, size=36, anim="cut"),
    ficon("fluent-emoji-flat", "crescent-moon", 420, 110, 54, "abend"),
    ficon("tabler", "desk", 560, BODEN - 2, 280, "abend", fuell=(214, 160, 110, 255)),
    szene(ficon("fluent-emoji-flat", "pencil", 560, 690, 70, beim("zettel", "Femke")), "137stift_1", 1.0),
    *zettel(ZX, ZY, ZW, beim("zettel", "Femke"), [("Femke war am Montag krank.", beim("zettel", "Femke")),
                                                  ("Bitte entschuldigen Sie", beim("zettel", "Bitte")),
                                                  ("ihr Fehlen.", beim("zettel", "Fehlen"))],
            size=34, sig="S. Ohlsen", sig_cue=beim("unterschrift", "Namen")),
    pl("Name und Unterschrift der Mutter, nachgeahmt", ZX + ZW // 2, 560, beim("unterschrift", "ahmt"), fill=ROTHELL,
       size=28, anker="m"),
    linienzug([(1400, 470), (1400, BODEN - 4)], "mutter", breite=4, farbe=GRAU),
    *st("MU", MUX, [("ruhig", "mutter")], unten=BODEN, hoehe=FH),
    pl("weiß davon nichts", MUX, 300, beim("mutter", "weiß"), fill=WEISS, size=30, anker="m"),
])

# ======================================================================================================================
# A2 Fall: Dienstag in der Schule
# ======================================================================================================================
FX2, MEX = 760, 1560
TISCH = ficon("tabler", "desk", 1240, BODEN - 2, 260, "dienstag", fuell=(214, 160, 110, 255))
TT = int(TISCH.y) + 8
folie([("dienstag", "Fall · Dienstag in der Schule"), ("f1", "Fall · Die Abgabe"), ("ablage", "Fall · Abgeheftet"),
       ("frage", "Fall · Die Frage")], [
    linienzug([(60, BODEN), (1860, BODEN)], "dienstag", breite=7, farbe=INK),
    karte(90, 130, 430, 260, "dienstag", fill=(60, 96, 78, 255), rund=12, schatten=6, rand=6),
    z("Dienstag", 150, 200, "dienstag", "ExtraBold", 54, farbe=WEISS, rechts=510),
    z("Klasse 10", 150, 280, "dienstag", "Bold", 34, farbe=WEISS, rechts=510),
    TISCH,
    *st("FE", FX2, [("ruhig_r", "dienstag"), ("redet_r", "f1"), ("ruhig_r", "m1"), ("froh_r", "ablage"), ("still_r", "frage")],
        rede=("redet_r",), unten=BODEN, hoehe=round(FH * JUNG)),
    *st("ME", MEX, [("ruhig", "dienstag"), ("redet", "m1"), ("ruhig", "ablage"), ("ernst", "frage")], rede=("redet",),
        unten=BODEN, hoehe=FH, d=0.2),
    bewegt(ficon("fluent-emoji-flat", "page-facing-up", 1180, TT, 70, beim("f1", "Hier"), bis="ablage"),
           beim("f1", "Hier"), beim("f1", "Entschuldigung"), -330, 40),
    blase("sprech", 560, 175, "f1", FX2 + 20, 230, inhalt=["Hier ist meine", "Entschuldigung für gestern."], textsize=34,
          figur=("FE_redet_r", FX2, BODEN, round(FH * JUNG)), bis="m1"),
    blase("sprech", 560, 175, "m1", MEX - 130, 200, inhalt=["Danke, Femke. Dann ist", "dein Fehlen entschuldigt."], textsize=34,
          figur=("ME_redet", MEX, BODEN, FH), bis="ablage"),
    szene(ficon("fluent-emoji-flat", "open-file-folder", 1240, TT, 110, beim("ablage", "heftet")), "137ordner_1", 1.0),
    pl("abgeheftet", 1240, TT - 170, beim("ablage", "heftet"), fill=WEISS, size=30, anker="m", bis="frage"),
    pl("Urkundenfälschung, § 267 StGB?", 960, 50, "frage", fill=PINK, size=36, anker="m"),
    pl("Was ist eine Urkunde?", 960, 140, beim("frage2", "Was"), fill=GELB, size=34, anker="m"),
])

# B Sachverhalt --------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    glyphen("Femke ist 16. Am Montag schwänzt sie die Schule. Am Abend schreibt sie auf einen Zettel: „Femke war am Montag "
            "krank. Bitte entschuldigen Sie ihr Fehlen.“ Darunter setzt sie den Namen ihrer Mutter und ahmt deren "
            "Unterschrift nach. Die Mutter weiß davon nichts."),
    glyphen("Am Dienstag gibt Femke den Zettel ihrer Klassenlehrerin, Frau Melzer. Frau Melzer behandelt das Fehlen als "
            "entschuldigt und heftet den Zettel ab."),
], "Hat sich Femke wegen Urkundenfälschung (§ 267 StGB) strafbar gemacht?")

# C Wortlaut § 267 Abs. 1 und Urkundenbegriff -------------------------------------------------------------------------------
W267 = [[("„Wer ", 0), ("zur Täuschung im Rechtsverkehr", "a"), (" eine ", 0), ("unechte Urkunde", "b")],
        [("herstellt", "b"), (", eine ", 0), ("echte Urkunde verfälscht", "c"), (" oder eine unechte oder", 0)],
        [("verfälschte Urkunde ", 0), ("gebraucht", "d"), (", wird mit Freiheitsstrafe bis zu", 0)],
        [("fünf Jahren oder mit Geldstrafe bestraft.“", 0)]]
folie([("p267", "§ 267 Abs. 1 StGB › Wortlaut"), ("def", "Urkundenbegriff › Definition"),
       ("drei", "Urkundenbegriff › drei Funktionen")], rechts_frei([
    *tafel("p267", "Urkundenfälschung: § 267 Abs. 1 StGB", size=46),
    *wortlaut(110, 170, 1040, 186, "p267", W267, 29, {"a": beim("p267w", "Täuschung"), "b": beim("p267w", "unechte"),
                                                      "c": beim("p267w", "echte"), "d": beim("p267w", "gebraucht")},
              "§ 267 Abs. 1 StGB"),
    z("Was eine Urkunde ist, sagt das Gesetz nicht.", 110, 410, "nichtdef", size=32),
    z("Urkunde: jede verkörperte Gedankenerklärung, die zum", 110, 475, "def", "Bold", 32),
    z("Beweis im Rechtsverkehr geeignet und bestimmt ist", 110, 520, beim("def", "Beweis"), "Bold", 32),
    z("und ihren Aussteller erkennen lässt", 110, 565, beim("def", "Aussteller"), "Bold", 32),
    fund("st. Rspr.; BGH, Urt. v. 10.11.2022 – 5 StR 283/22, Rn. 36", 150, 615, beim("def", "Aussteller")),
    *leiste(700, "drei", 3, size=34, cues=["fperp", "fbew", "fgar"]),
    *st("FE", X1, [("ruhig", "p267"), ("denkt", "nichtdef"), ("ernst", "drei")]),
    *st("ME", X2, [("ruhig", "p267"), ("denkt", "def")], d=0.2),
    *wechsel([("§ 267 StGB", "p267", WEISS), ("Urkunde?", "nichtdef", GELB), ("Definition", "def", WEISS),
              ("drei Funktionen", "drei", GRUEN)], MB, 160),
    *icons([("fluent-emoji-flat", "balance-scale", "p267", None), ("fluent-emoji-flat", "page-facing-up", "def", None)],
           MB, 390, 110),
]))

# D 1. a) Perpetuierungsfunktion -----------------------------------------------------------------------------------------
PO = "I. Tatbestand › 1. objektiv › a) Urkunde"
folie([("perp", f"{PO}: Perpetuierungsfunktion"), ("perp3", f"{PO}: Perpetuierungsfunktion (+)")], rechts_frei([
    *tafel("perp", "1. Perpetuierungsfunktion"),
    *leiste(170, "perp", 0),
    z("Die Erklärung muss verkörpert sein,", 110, 275, beim("perp", "Die"), "Bold", 34),
    z("also dauerhaft auf einer Sache festgehalten.", 110, 322, beim("perp", "also"), "Bold", 34),
    *zeile_ok("Anruf in der Schule: keine Urkunde", 110, 420, "perp2", ja=False, size=34),
    *zeile_ok("Zettel: Erklärung auf Papier festgehalten", 110, 490, "perp3", size=34),
    *zettel(160, 580, 560, "perp3", [("Femke war am Montag krank.", "perp3"), ("Bitte entschuldigen Sie ihr Fehlen.", "perp3")],
            size=28),
    *st("FE", X1, [("ruhig", "perp"), ("denkt", "perp2"), ("ruhig", "perp3")]),
    *st("ME", X2, [("ruhig", "perp"), ("ernst", "perp2"), ("froh", "perp3")], d=0.2),
    *wechsel([("verkörpert?", "perp", GELB), ("nur gesprochen", "perp2", ROTHELL), ("auf Papier", "perp3", GRUEN)], MB, 160),
    *icons([("fluent-emoji-flat", "memo", "perp", None), ("fluent-emoji-flat", "telephone-receiver", "perp2", None),
            ("fluent-emoji-flat", "page-facing-up", "perp3", None)], MB, 390, 110),
]))

# E 1. b) Beweisfunktion, Absichts-/Zufallsurkunde, Fotokopie --------------------------------------------------------------
folie([("bew", f"{PO}: Beweisfunktion"), ("absicht", f"{PO}: Absichts- und Zufallsurkunde"),
       ("kopie", f"{PO}: Abgrenzung Fotokopie")], rechts_frei([
    *tafel("bew", "2. Beweisfunktion"),
    *leiste(170, "bew", 1),
    z("geeignet und bestimmt, für ein Rechtsverhältnis", 110, 262, beim("bew", "Die"), "Bold", 32),
    z("Beweis zu erbringen", 110, 305, beim("bew", "Beweis"), "Bold", 32),
    fund("BGH, Beschl. v. 14.3.2024 – 2 StR 192/23, Rn. 36", 150, 350, beim("bew", "Beweis")),
    *zeile_ok("soll der Schule beweisen: Die Mutter entschuldigt", 110, 405, "bew2", size=31),
    *zeile_ok("geeignet und gerade dafür geschrieben", 110, 458, beim("bew2", "Dafür"), size=31),
    z("Lehre: von Anfang an zum Beweis – Absichtsurkunde", 110, 525, "absicht", size=31),
    z("erst später bestimmt, z. B. alter Brief – Zufallsurkunde", 110, 570, "zufall", size=31),
    karte(110, 640, 1040, 200, "kopie", fill=ROTHELL, rund=18, schatten=6, rand=4),
    z("Abgrenzung: bloße Fotokopie, die als Kopie erscheint", 140, 660, "kopie", "ExtraBold", 31),
    z("keine Urkunde: Ihr fehlt die Beweiseignung", 140, 712, beim("kopie", "Ihr"), "Bold", 31),
    fund("BGH, Urt. v. 23.9.2015 – 2 StR 434/14, Rn. 34", 140, 770, beim("kopie", "Ihr")),
    *st("FE", X1, [("ruhig", "bew"), ("ernst", "bew2"), ("denkt", "zufall"), ("ruhig", "kopie")]),
    *st("ME", X2, [("ruhig", "bew"), ("froh", "bew2"), ("ernst", "kopie")], d=0.2),
    *wechsel([("Beweis?", "bew", GELB), ("Beweis für die Schule", "bew2", GRUEN), ("Absichtsurkunde", "absicht", WEISS),
              ("Zufallsurkunde", "zufall", WEISS), ("Kopie: keine Urkunde", "kopie", ROTHELL)], MB, 160),
    *icons([("fluent-emoji-flat", "balance-scale", "bew", None), ("fluent-emoji-flat", "page-facing-up", "bew2", None),
            ("fluent-emoji-flat", "memo", "absicht", None), ("fluent-emoji-flat", "envelope", "zufall", None),
            ("fluent-emoji-flat", "printer", "kopie", None)], MB, 390, 110),
]))

# F 1. c) Garantiefunktion, Beweiszeichen ------------------------------------------------------------------------------
folie([("gar", f"{PO}: Garantiefunktion"), ("bz", f"{PO}: Beweiszeichen"), ("urk", "I. Tatbestand › 1. objektiv › a) Urkunde (+)")],
      rechts_frei([
    *tafel("gar", "3. Garantiefunktion"),
    *leiste(170, "gar", 2),
    z("Die Urkunde lässt ihren Aussteller erkennen:", 110, 262, beim("gar", "Die"), "Bold", 32),
    z("den, der für die Erklärung einsteht", 110, 305, beim("gar", "also"), "Bold", 32),
    *zeile_ok("Unterschrift zeigt die Mutter als Ausstellerin", 110, 375, "gar2", size=32),
    karte(110, 455, 1040, 210, "bz", fill=LILAHELL, rund=18, schatten=6, rand=4),
    z("Auch ein bloßes Zeichen: Beweiszeichen", 140, 475, "bz", "ExtraBold", 31),
    z("Fahrzeugidentifikationsnummer mit dem Auto: Urkunde", 140, 527, beim("bz", "So"), "Bold", 31),
    fund("BGH, Urt. v. 17.10.2019 – 3 StR 521/18, Rn. 33", 140, 585, beim("bz", "So")),
    fb(110, 720, 1040, 100, GRUEN, "urk", [("Die Entschuldigung ist eine Urkunde.", "ExtraBold", 36, INK)]),
    *st("FE", X1, [("ruhig", "gar"), ("still", "gar2"), ("denkt", "bz"), ("ernst", "urk")]),
    *st("ME", X2, [("ruhig", "gar"), ("denkt", "bz"), ("ruhig", "urk")], d=0.2),
    *wechsel([("Aussteller?", "gar", GELB), ("Ausstellerin: Mutter", "gar2", GRUEN), ("Beweiszeichen", "bz", LILA),
              ("Urkunde (+)", "urk", GRUEN)], MB, 160),
    *icons([("fluent-emoji-flat", "magnifying-glass-tilted-left", "gar", None), ("tabler", "signature", "gar2", None),
            ("fluent-emoji-flat", "automobile", "bz", None), ("tabler", "circle-check", "urk", GRUEN)], MB, 390, 120),
]))

# G 1. b) Tathandlung: unechte Urkunde, Geistigkeitstheorie ------------------------------------------------------------
PT = "I. Tatbestand › 1. objektiv › b) Tathandlung"
folie([("tat", PT), ("unecht", f"{PT}: unecht = Täuschung über den Aussteller"), ("geist", f"{PT}: Geistigkeitstheorie"),
       ("sub2", f"{PT}: Herstellen einer unechten Urkunde (+)")], rechts_frei([
    *tafel("tat", "Tathandlung: unechte Urkunde"),
    pl("Herstellen", 110, 170, "herst", fill=GELB, size=30),
    pl("Verfälschen", 380, 170, "verf", fill=WEISS, size=30),
    pl("Gebrauchen", 660, 170, "gebr", fill=WEISS, size=30),
    z("unecht: täuscht über die Identität des Ausstellers,", 110, 265, "unecht", "Bold", 32),
    z("stammt nicht von dem, der als Aussteller hervorgeht", 110, 310, beim("unecht", "Sie"), "Bold", 32),
    fund("BGH 2 StR 192/23, Rn. 35; BGH, Urt. v. 11.11.2020 – 1 StR 328/19, Rn. 70", 150, 357, beim("unecht", "Sie")),
    z("Geistigkeitstheorie: Aussteller ist, wer geistig", 110, 420, "geist", "Bold", 32),
    z("hinter der Erklärung steht, sie sich zurechnen lassen will", 110, 465, beim("geist", "geistig"), "Bold", 32),
    fund("BGH 1 StR 328/19, Rn. 70, 75", 150, 512, beim("geist", "zurechnen")),
    z("Wer den Stift führt, entscheidet nicht.", 110, 565, "hand", size=32),
    *zeile_ok("Mutter will sich den Zettel nicht zurechnen lassen", 110, 625, "sub", ja=False, size=31),
    *zeile_ok("geistig stammt er von Femke", 110, 680, beim("sub", "Er"), size=31),
    fb(110, 745, 1040, 95, GRUEN, "sub2", [("unecht – Femke hat sie hergestellt (+)", "ExtraBold", 34, INK)]),
    *st("FE", X1, [("ruhig", "tat"), ("denkt", "geist"), ("still", "sub"), ("ernst", "sub2")]),
    *st("MU", X2, [("ruhig", "tat"), ("denkt", "sub"), ("ernst", "sub2")], d=0.2),
    *wechsel([("drei Tathandlungen", "tat", WEISS), ("unecht?", "unecht", GELB), ("geistig dahinter?", "geist", WEISS),
              ("Stift egal", "hand", WEISS), ("nicht die Mutter", "sub", ROTHELL), ("unecht (+)", "sub2", GRUEN)], MB, 160),
    *icons([("fluent-emoji-flat", "page-facing-up", "tat", None), ("fluent-emoji-flat", "magnifying-glass-tilted-left", "unecht", None),
            ("fluent-emoji-flat", "brain", "geist", None), ("fluent-emoji-flat", "pencil", "hand", None),
            ("fluent-emoji-flat", "brain", "sub", None), ("tabler", "circle-check", "sub2", GRUEN)], MB, 390, 110),
]))

# H Abgrenzung: schriftliche Lüge ---------------------------------------------------------------------------------------
folie([("luege", "Abgrenzung › Inhalt falsch, Urkunde trotzdem unecht?"), ("luege2", "Abgrenzung › echte, inhaltlich unwahre Urkunde"),
       ("luege3", "Abgrenzung › schriftliche Lüge: § 267 (−)")], rechts_frei([
    *tafel("luege", "Klausurpunkt: schriftliche Lüge", fill=HELL),
    z("Dass der Zettel lügt, macht ihn nicht unecht.", 110, 180, beim("luege", "Dass"), "ExtraBold", 34),
    *zeile_ok("Inhalt falsch: Femke war nicht krank", 110, 245, beim("luege", "Femke"), ja=False, size=32),
    karte(110, 330, 1040, 175, "luege2", fill=WEISS, rund=18, schatten=6, rand=4),
    z("Mutter schreibt selbst die falsche Entschuldigung:", 140, 350, "luege2", "Bold", 32),
    z("echt, nur inhaltlich unwahr", 140, 400, beim("luege2", "wäre"), "ExtraBold", 34),
    z("Aussteller stimmt – nur der Inhalt nicht", 140, 450, beim("luege2", "nur"), size=30),
    z("schriftliche Lüge: von § 267 nicht erfasst", 110, 545, "luege3", "ExtraBold", 34),
    fund("BGH, Beschl. v. 14.3.2024 – 2 StR 192/23, Rn. 29, 35", 150, 595, beim("luege3", "erfasst")),
    fb(110, 660, 1040, 140, GELB, "luege4", [("Echtheit der Urkunde,", "ExtraBold", 36, INK),
                                            ("nicht Wahrheit ihres Inhalts", "ExtraBold", 36, INK)]),
    *st("MU", X1, [("ruhig", "luege"), ("froh", "luege2"), ("ernst", "luege3")]),
    *st("FE", X2, [("ruhig", "luege"), ("still", "luege2"), ("denkt", "luege4")], d=0.2),
    *wechsel([("Lüge = unecht?", "luege", GELB), ("echt, aber unwahr", "luege2", WEISS), ("§ 267 (−)", "luege3", ROTHELL),
              ("Echtheit", "luege4", GELB)], MB, 160),
    *icons([("fluent-emoji-flat", "thought-balloon", "luege", None), ("fluent-emoji-flat", "memo", "luege2", None),
            ("tabler", "x", "luege3", None), ("fluent-emoji-flat", "magnifying-glass-tilted-left", "luege4", None)], MB, 390, 110),
]))

# I Verfälschen (zum Vergleich) und Gebrauchen -------------------------------------------------------------------------
folie([("verf2", f"{PT}: Verfälschen (zum Vergleich)"), ("gebr2", f"{PT}: Gebrauchen"), ("gebr4", f"{PT}: Gebrauchen (+)")],
      rechts_frei([
    *tafel("verf2", "Verfälschen und Gebrauchen"),
    z("Verfälschen: echte Urkunde nachträglich", 110, 180, beim("verf2", "Verfälschen"), "Bold", 32),
    z("inhaltlich ändern", 110, 225, beim("verf2", "nachträglich"), "Bold", 32),
    fund("BGH, Beschl. v. 4.5.2023 – 5 StR 38/23, Rn. 13", 150, 272, beim("verf2", "inhaltlich")),
    *zettel(140, 325, 470, beim("verf2", "etwa"), [("… am Montag krank.", beim("verf2", "etwa"))], size=30),
    pl("+ zweiter Fehltag", 640, 345, beim("verf2", "zweiten"), fill=ROTHELL, size=30),
    z("Gebrauchen: dem zu Täuschenden so zugänglich", 110, 480, "gebr2", "Bold", 32),
    z("machen, dass er sie wahrnehmen kann", 110, 525, beim("gebr2", "zugänglich"), "Bold", 32),
    fund("BGH, Urt. v. 17.10.2019 – 3 StR 521/18, Rn. 34", 150, 572, beim("gebr2", "wahrnehmen")),
    *zeile_ok("Femke gibt Frau Melzer den Zettel in die Hand", 110, 635, "gebr3", size=32),
    fb(110, 720, 1040, 95, GRUEN, "gebr4", [("unechte Urkunde auch gebraucht (+)", "ExtraBold", 34, INK)]),
    *st("FE", X1, [("ruhig", "verf2"), ("eifrig", "gebr3"), ("still", "gebr4")]),
    *st("ME", X2, [("ruhig", "verf2"), ("froh", "gebr3"), ("ernst", "gebr4")], d=0.2),
    bewegt(ficon("fluent-emoji-flat", "page-facing-up", MB, 560, 70, "gebr3"), "gebr3", beim("gebr3", "Zettel"), -140, 0),
    *wechsel([("nur zum Vergleich", "verf2", LILAHELL), ("Gebrauchen?", "gebr2", GELB), ("in die Hand", "gebr3", WEISS),
              ("gebraucht (+)", "gebr4", GRUEN)], MB, 160),
    *icons([("fluent-emoji-flat", "pencil", "verf2", None), ("tabler", "eye", "gebr2", WEISS)], MB, 390, 110),
]))

# J 2. Subjektiver Tatbestand ------------------------------------------------------------------------------------------
PSU = "I. Tatbestand › 2. subjektiv"
folie([("vors", f"{PSU} › a) Vorsatz"), ("rv", f"{PSU} › b) zur Täuschung im Rechtsverkehr"),
       ("rv3", f"{PSU} (+)")], rechts_frei([
    *tafel("vors", "2. Subjektiver Tatbestand"),
    z("a) Vorsatz", 110, 180, "vors", "ExtraBold", 34),
    *zeile_ok("weiß: Die Mutter hat nicht unterschrieben", 110, 235, "vors2", size=32),
    *zeile_ok("will den Zettel abgeben", 110, 290, beim("vors2", "will"), size=32),
    z("b) zur Täuschung im Rechtsverkehr", 110, 370, "rv", "ExtraBold", 34),
    z("gängige Definition: Irrtum über die Echtheit erregen und", 110, 425, beim("rv", "Nach"), size=31),
    z("so ein rechtlich erhebliches Verhalten bewirken wollen", 110, 470, beim("rv", "rechtlich"), size=31),
    *zeile_ok("Frau Melzer soll den Zettel für echt halten", 110, 545, "rv2", size=32),
    *zeile_ok("und das Fehlen als entschuldigt behandeln", 110, 600, beim("rv2", "Fehlen"), size=32),
    fb(110, 690, 1040, 95, GRUEN, "rv3", [("Das genügt: subjektiver Tatbestand (+)", "ExtraBold", 34, INK)]),
    *st("FE", X1, [("ruhig", "vors"), ("denkt", "vors2"), ("eifrig", "rv2"), ("ernst", "rv3")]),
    *st("ME", X2, [("ruhig", "vors"), ("froh", "rv2"), ("ruhig", "rv3")], d=0.2),
    *wechsel([("Vorsatz?", "vors", GELB), ("weiß und will", "vors2", GRUEN), ("Täuschung?", "rv", GELB),
              ("für echt halten", "rv2", WEISS), ("genügt", "rv3", GRUEN)], MB, 160),
    *icons([("fluent-emoji-flat", "brain", "vors", None), ("fluent-emoji-flat", "magnifying-glass-tilted-left", "rv", None),
            ("fluent-emoji-flat", "open-file-folder", "rv2", None), ("tabler", "circle-check", "rv3", GRUEN)], MB, 390, 110),
]))

# K Gegenvariante: Erlaubnis der Mutter -------------------------------------------------------------------------------
folie([("var", "Gegenvariante › Mutter erlaubt vorher"), ("var2", "Gegenvariante › Mutter steht geistig dahinter"),
       ("var3", "Gegenvariante › echte Urkunde")], rechts_frei([
    *tafel("var", "Gegenvariante: Erlaubnis", fill=LILAHELL),
    *zeile_ok("Femke war wirklich krank", 110, 180, beim("var", "Femke"), size=32),
    *zeile_ok("Mutter erlaubt am Telefon, für sie zu unterschreiben", 110, 235, beim("var", "Mutter"), size=31),
    z("Mutter will sich die Erklärung zurechnen lassen", 110, 320, "var2", "Bold", 32),
    z("steht geistig dahinter, Femke unterschreibt nur für sie", 110, 365, beim("var2", "Sie"), "Bold", 32),
    z("echt, solange kein Gesetz eine eigenhändige", 110, 440, "var3", "Bold", 32),
    z("Unterschrift verlangt, z. B. beim Testament", 110, 485, beim("var3", "Unterschrift"), "Bold", 32),
    fund("BGH 1 StR 328/19, Rn. 70–72, 76; BGH 2 StR 192/23, Rn. 18", 150, 532, beim("var3", "Testament")),
    fb(110, 620, 1040, 95, GRUEN, beim("var3", "echt"), [("echte Urkunde", "ExtraBold", 36, INK)]),
    *st("MU", X1, [("ruhig", "var"), ("froh", "var2"), ("ruhig", "var3")]),
    *st("FE", X2, [("sorge", "var"), ("froh", "var2"), ("ruhig", "var3")], d=0.2),
    ficon("fluent-emoji-flat", "mobile-phone", X1 + 85, 640, 54, beim("var", "Telefon"), bis="var2"),
    *wechsel([("erlaubt vorher", "var", LILA), ("geistig dahinter", "var2", WEISS), ("echt", "var3", GRUEN)], MB, 160),
    *icons([("fluent-emoji-flat", "telephone-receiver", "var", None), ("fluent-emoji-flat", "brain", "var2", None),
            ("fluent-emoji-flat", "scroll", beim("var3", "Testament"), None)], MB, 390, 110),
]))

# L Rechtswidrigkeit, Schuld, Ergebnis, Konkurrenz ----------------------------------------------------------------------
folie([("rw", "II. Rechtswidrigkeit"), ("schuld", "III. Schuld › 16 Jahre, § 19 StGB"),
       ("erg", "Ergebnis · Femke strafbar, § 267 Abs. 1 StGB"), ("konk", "Konkurrenzen · eine Tat")], rechts_frei([
    *tafel("rw", "Rechtswidrigkeit, Schuld, Ergebnis"),
    *zeile_ok("II. Rechtswidrigkeit: keine Rechtfertigungsgründe", 110, 180, beim("rw", "Rechtfertigungsgründe"), size=32, stil="Bold"),
    *zeile_ok("III. Schuld: 16 Jahre, strafmündig", 110, 245, "schuld", size=32, stil="Bold"),
    z("schuldunfähig nur unter 14, § 19 StGB", 175, 295, beim("schuld", "schuldunfähig"), size=31),
    z("Jugendstrafrecht (JGG)", 175, 345, "jgg", size=31),
    fb(110, 420, 1040, 150, GRUEN, "erg", [("Femke: strafbar wegen Urkundenfälschung,", "ExtraBold", 34, INK),
                                          ("§ 267 Abs. 1 Var. 1 und 3 StGB", "ExtraBold", 34, INK)]),
    z("Herstellen und Gebrauchen: eine Tat", 110, 615, "konk", "Bold", 33),
    z("Gebrauch war schon beim Schreiben geplant", 110, 662, beim("konk", "weil"), size=32),
    fund("BGH, Beschl. v. 30.10.2008 – 3 StR 156/08, Rn. 11", 150, 712, beim("konk", "weil")),
    *st("FE", X1, [("ruhig", "rw"), ("still", "erg"), ("ernst", "konk")]),
    *st("ME", X2, [("ruhig", "rw"), ("ernst", "erg")], d=0.2),
    *wechsel([("gerechtfertigt?", "rw", WEISS), ("16 Jahre", "schuld", WEISS), ("Jugendstrafrecht", "jgg", LILAHELL),
              ("§ 267 (+)", "erg", GRUEN), ("eine Tat", "konk", WEISS)], MB, 160),
    *icons([("fluent-emoji-flat", "balance-scale", "rw", None), ("tabler", "circle-check", "erg", GRUEN),
            ("tabler", "link", "konk", None)], MB, 390, 110),
]))

# M Klausurtipp (Lexi) -------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · Echtheit und Wahrheit trennen"), ("tipp3", "Klausurtipp · Erlaubnis bei der Unechtheit prüfen")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Trenne Echtheit und Wahrheit.", 200, 200, beim("tipp", "Trenne"), "Bold", 38),
    z("Wer steht geistig hinter der Erklärung?", 200, 290, "tipp2", "ExtraBold", 35),
    z("Nur wenn das ein anderer ist als der", 200, 350, beim("tipp2", "Nur"), size=34),
    z("scheinbare Aussteller: unecht", 200, 398, beim("tipp2", "scheinbare"), size=34),
    z("Erlaubnis des Namensträgers schon bei", 200, 490, "tipp3", "ExtraBold", 35),
    z("der Unechtheit prüfen,", 200, 540, beim("tipp3", "Unechtheit"), "ExtraBold", 35),
    z("nicht erst bei der Rechtswidrigkeit", 200, 590, beim("tipp3", "nicht"), "ExtraBold", 35),
    fund("BGH 1 StR 328/19, Rn. 70; BGH 2 StR 192/23, Rn. 18", 240, 648, beim("tipp3", "Rechtswidrigkeit")),
    *redet("LX_warnt", LXX, BR, FR + 60, "tipp", "sch"),
    namensschild("Lexi", LXX, BR, "tipp", GELB, d=0.2),
])

# N Prüfschema ---------------------------------------------------------------------------------------------------------
K1, K2, K3 = 150, 220, 300
PSCH = "Prüfschema"
folie([("sch", PSCH), ("k1", f"{PSCH} › I. Tatbestand"), ("k1a", f"{PSCH} › I. 1. a) Urkunde"),
       ("k1b", f"{PSCH} › I. 1. b) Tathandlung"), ("k1c", f"{PSCH} › I. 2. a) Vorsatz"),
       ("k1d", f"{PSCH} › I. 2. b) zur Täuschung im Rechtsverkehr"), ("k2", f"{PSCH} › II. Rechtswidrigkeit"),
       ("k3", f"{PSCH} › III. Schuld"), ("k4", f"{PSCH} › IV. Konkurrenzen")], [
    karte(60, 50, 1800, 900, "sch"),
    titel("Prüfschema: Urkundenfälschung, § 267 Abs. 1 StGB", 110, 90, "sch", 52),
    z("I. Tatbestand", K1, 185, "k1", "Bold", 38, rechts=1820),
    z("1. objektiver Tatbestand", K2, 242, "k1a", "Bold", 34, rechts=1820),
    z("a) Urkunde: Perpetuierungs-, Beweis- und Garantiefunktion", K3, 292, beim("k1a", "Urkunde"), size=34, rechts=1820),
    z("b) Tathandlung: Herstellen, Verfälschen oder Gebrauchen", K3, 342, "k1b", size=34, rechts=1820),
    z("2. subjektiver Tatbestand", K2, 410, "k1c", "Bold", 34, rechts=1820),
    z("a) Vorsatz", K3, 460, beim("k1c", "Vorsatz"), size=34, rechts=1820),
    z("b) zur Täuschung im Rechtsverkehr", K3, 510, "k1d", size=34, rechts=1820),
    z("II. Rechtswidrigkeit", K1, 590, "k2", "Bold", 38, rechts=1820),
    z("III. Schuld", K1, 660, "k3", "Bold", 38, rechts=1820),
    z("IV. Konkurrenzen", K1, 730, "k4", "Bold", 38, rechts=1820),
])

# O Merksatz (Lexi) ----------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Eine Urkunde ", 0), ("hält", "a"), (" eine Erklärung fest,", 0)],
                 [("beweist", "b"), (" etwas und ", 0), ("zeigt, wer dafür einsteht", "c"), (".", 0)]], 750, 300, 44, "merke",
                {"a": beim("merke", "hält"), "b": beim("merke", "beweist"), "c": beim("merke", "zeigt")}),
    *markertext([[("Unecht ist sie nur, wenn sie", 0)], [("über den ", 0), ("Aussteller", "d"), (" täuscht.", 0)]],
                750, 480, 44, "m2", {"d": beim("m2", "Aussteller")}),
    *markertext([[("Wer bloß ", 0), ("lügt", "e"), (", fälscht keine Urkunde.", 0)]], 750, 660, 44, "m3",
                {"e": beim("m3", "lügt")}),
    *redet("LX_erklaert", 1680, 960, 690, "merke", lexi_bis_ende("merke")),
    namensschild("Lexi", 1680, 960, "merke", GELB, d=0.2),
])
