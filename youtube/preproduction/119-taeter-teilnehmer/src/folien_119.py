"""Folge 119 · Abgrenzung Täter Teilnehmer: Tatherrschaft vs. subjektive Theorie – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A Bibliothek (Luise und Oskar lesen die Akten: Badewannen-Fall 1940, Staschinski-Fall 1962,
Frage), B Sachverhalt, C 1. Problem (Wortlaut § 25 I, § 27 I; § 26), D Strafrahmen, E 2. Reichsgericht (animus auctoris /
socii), F Bundesgerichtshof 1956 und Staschinski 1962, G 3. Kritik und Wende (§ 25 I Alt. 1), H 4. Tatherrschaftslehre,
I 5. Streitstand (Zweispalter, heutige Rechtsprechung), J 6. Streitentscheid, K Ergebnis heute, L Klausurtipp (Lexi),
M Klausurschema, N Merksatz (Lexi).
DARSTELLUNG SENSIBEL: Beim Badewannen-Fall kein Kind, kein Säugling, keine Badewanne, keine Tathandlung im Bild – nur Akte,
Gerichtsgebäude, Jahreszahl; Staschinski ohne Waffe (Akte, Stadtsilhouette, Jahreszahl). Die Beteiligten der echten Fälle
erscheinen nicht als Figuren. Keine Geräusche (keine sichtbare Handlung, die eines trüge).
Namensschild jeder Figur ab ihrem ersten Auftritt, solange sie im Bild ist. Zahlen auf Tafeln, Pillen und Blasen als Ziffern.
Hilfsfunktionen glyphen/z/pl/tafel/fund/blk/wortlaut/redet als eigene Kopie aus Folge 104 (gemeinsame Dateien unverändert)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import wave as _wave

bausteine.FIGORDNER = "op_119/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
LILAHELL = (246, 243, 255, 255)
ROTHELL = (253, 232, 228, 255)
GRUENHELL = (232, 247, 233, 255)
BLAUHELL = (233, 241, 253, 255)
AKTE = (247, 236, 214, 255)                # Aktendeckel (Karton)
DAUER = bausteine._cj()["dauer"]
NULL = "fall"                              # Szene A steht ab 0,0 s (render_119 setzt alle Elemente bis zur Marke „fall“ auf 0,0 s)

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


def tafel(cue, titel_, h=840, fill=WEISS, size=46):
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(glyphen(titel_), 110, 100, cue, size)]


def fund(text, x, y, cue, rechts=1170, **k):
    """Fundstelle (mobil lesbar: 26 px)."""
    return z(text, x, y, cue, size=26, farbe=TEXT, rechts=rechts, **k)


def blk(x, y, w, h, fill, cue, zeilen, anim="rise", d=0.0, bis=None):
    """Block mit Textprüfung (Breite) und Glyphenprüfung."""
    for t_, st, sz, _ in zeilen:
        glyphen(t_)
        assert sz >= 26
        assert F(st, sz).getlength(t_) <= w - 40, f"Block zu breit: {t_}"
    return block(x, y, w, h, fill, None, cue, textsize=zeilen[0][2], rund=18, rand=INK, randbreite=5, anim=anim, d=d,
                 bis=bis, zeilen=zeilen)


def namensschild(text, cx, unten, cue, fill, **k):
    return pille(glyphen(text), cx, unten + 22, cue, fill=fill, size=30, anker="m", **k)


def lexi_bis_ende(cue):
    return (cue, round(DAUER - bausteine._t(cue) - 0.05, 3))


def rechts_frei(els, x0=1250):
    """Figuren und Requisiten der Tafelfolien stehen rechts der Tafel (x ≥ 1250)."""
    for e in els:
        n = e.name or ""
        if n.startswith(("bild:", "ficon:")):
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def sachverhalt_klein(cue, absaetze, frage, size=40, pfad="Sachverhalt"):
    """Wie bausteine.sachverhalt(), Schrift passend zur Länge (wie Folge 104)."""
    els = [karte(140, 50, 1640, 920, cue, fill=HELL), titel("Sachverhalt", 210, 82, cue, 56)]
    y = 175
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=size, zeilenabstand=1.27)
        els += e; y += 18
    els.append(pl(frage, 210, y + 8, cue, fill=PINK, size=34))
    assert y + 8 <= 890, f"Sachverhalt zu lang ({y})"
    folie([(cue, pfad)], els)


def markertext_farbig(zeilen_tokens, cx, y, size, cue, hl_cues, farben, lh=1.3, links=None):
    """Wie ostil.markertext, aber mit eigener Markerfarbe je Schlüssel (wie Folge 104); links=x linksbündig."""
    fr, fb = F("Regular", size), F("ExtraBold", size)
    lines, maxw = [], 0
    for toks in zeilen_tokens:
        glyphen("".join(t for t, _ in toks))
        wid = sum((fb if h else fr).getlength(t) for t, h in toks)
        maxw = max(maxw, wid); lines.append((toks, wid))
    hgt = int(len(lines) * size * lh + size * 0.5)
    im = Image.new("RGBA", (int(maxw) + 40, hgt))
    ov = {}
    dr = ImageDraw.Draw(im)
    yy = 0
    for toks, wid in lines:
        xx = 20 + ((maxw - wid) / 2 if links is None else 0)
        for t, h in toks:
            f = fb if h else fr
            tw = f.getlength(t)
            if h:
                if h not in ov:
                    ov[h] = Image.new("RGBA", im.size)
                od = ImageDraw.Draw(ov[h])
                od.rounded_rectangle((xx - 6, yy + size * 0.45, xx + tw + 6, yy + size * 1.12), 8, fill=farben[h])
                od.text((xx, yy), t, font=f, fill=INK)
            dr.text((xx, yy), t, font=f, fill=INK)
            xx += tw
        yy += size * lh
    x0 = cx - im.width / 2 if links is None else links - 20
    els = [El(im, x0, y, cue, "rise", 0.0, name="markertext")]
    for key, oim in ov.items():
        els.append(El(oim, x0, y, hl_cues[key], "fade", 0.0, name="marker:" + key))
    return els, im.width


def wortlaut(x, y, w, h, cue, zeilen, size, hl, quelle, farben=None):
    """Wortlautkarte: wörtliches Zitat in einer hellen Karte, Fundstelle darunter rechts.
    zeilen = Liste von Token-Listen [(text, Schlüssel|0)], hl = {Schlüssel: Cue} (Hervorhebung synchron zum Wort)."""
    els = [karte(x, y, w, h, cue, fill=(246, 246, 250, 255), rund=18, schatten=6, rand=4)]
    farben = farben or {k: GELB for k in hl}
    m, mw = markertext_farbig(zeilen, x + w / 2, y + 22, size, cue, hl, farben, lh=1.28)
    assert m[0].x >= x + 10 and m[0].x + m[0].sprite.width <= x + w - 10, f"Wortlaut zu breit ({m[0].sprite.width} > {w})"
    assert m[0].y + m[0].sprite.height <= y + h + 6, "Wortlaut zu hoch"
    els += m
    q = zeile(glyphen(quelle), 0, 0, cue, "Bold", 26, farbe=TEXT)
    q.x = x + w - q.sprite.width - 24; q.y = y + h + 8
    els.append(q)
    return els


def merktext(zeilen_tokens, cx, y, size, cue, hl, breite):
    els, mw = markertext_farbig(zeilen_tokens, cx, y, size, cue, hl, {k: PINK for k in hl})
    assert mw <= breite, f"Merksatz zu breit ({mw} > {breite})"
    return els


# --- Eigene Hilfsfunktion (wie Folge 104): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ---------------------
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


BODEN = 880
BR = 930                                   # Fußlinie der Figuren in den Tafelfolien
SCHILD = {"LU": ("Luise", GRUEN), "OS": ("Oskar", BLAU)}


def figur_kette(p, x, cue, mimik, folge=(), bis=None, d=0.0, unten=BR, hoehe=480, schild=True, schild_d=0.2, erst="pop"):
    """Eine Figur mit Mimikfolge [(mimik, cue), …] (Zwiebelschalenprinzip) und Namensschild ab dem ersten Bild."""
    kette = [(mimik, cue)] + list(folge)
    els = []
    for i, (m, c) in enumerate(kette):
        b = kette[i + 1][1] if i + 1 < len(kette) else bis
        els.append(peep_voll(f"{p}_{m}", x, unten, hoehe, c, anim=(erst if i == 0 else "cut"), d=(d if i == 0 else 0.0), bis=b))
    if schild:
        n, f = SCHILD[p]
        els.append(namensschild(n, x, unten, cue, f, d=schild_d, bis=bis))
    return els


XA, XB = 1440, 1740                        # Luise, Oskar rechts neben der Tafel (blicken zur Tafel)
MB = (XA + XB) // 2


def paar(cue, lu=(), os_=(), lu0="ruhig", os0="ruhig"):
    """Luise und Oskar rechts neben der Tafel, je mit eigener Mimikfolge."""
    return [*figur_kette("LU", XA, cue, lu0, lu), *figur_kette("OS", XB, cue, os0, os_, d=0.15, schild_d=0.3)]


def akte(x, y, w, h, cue, bis=None):
    """Aktendeckel: Karton-Karte mit Reiter (nur Bausteine karte)."""
    els = [karte(x + 30, y - 34, 220, 60, cue, fill=AKTE, rund=10, schatten=0, rand=4),
           karte(x, y, w, h, cue, fill=AKTE, rund=14, schatten=6, rand=5)]
    for e in els:
        e.bis = bis
    return els


# ===========================================================================================================================
# A Bibliothek: Luise und Oskar lesen die Akten der beiden Klassiker
# ===========================================================================================================================
LX_, OX_, FH = 1450, 1730, 520
LUr = ("LU_redet", LX_, BODEN, FH)
OSr = ("OS_redet", OX_, BODEN, FH)
BW, ST = "bw", "stasch"
folie([(NULL, "Fall · Badewannen-Fall, Reichsgericht 1940"), ("l1", "Fall · Warum nur Gehilfin?"),
       (BW, "Fall · Staschinski-Fall, Bundesgerichtshof 1962"), ("o1", "Fall · Wer selbst tötet …"),
       ("frage", "Fall · Die Frage")], [
    linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK),
    # Bücherstapel der Bibliothek (zwischen Akte und Figuren auf dem Boden)
    ficon("fluent-emoji-flat", "books", 1240, BODEN, 90, NULL),
    # Akte 1: Badewannen-Fall (nur Akte, Gerichtsgebäude, Jahreszahl)
    *akte(90, 110, 1080, 680, NULL, bis=BW),
    pl("Akte", 230, 76, NULL, fill=WEISS, size=28, anker="m", bis=BW),
    z("Reichsgericht · 1940", 140, 140, NULL, "ExtraBold", 46, bis=BW),
    pl("RGSt 74, 84", 270, 230, beim("fall", "Urteil"), fill=WEISS, size=30, anker="m", bis=BW),
    ficon("fluent-emoji-flat", "classical-building", 1030, 300, 150, NULL, bis=BW),
    z("Schwangerschaft aus Angst verheimlicht", 140, 300, beim("geburt", "Schwangerschaft"), size=34, bis=BW),
    z("Geburt heimlich, mit Hilfe der Schwester", 140, 350, beim("geburt", "heimlich"), size=34, bis=BW),
    z("auf Drängen der Mutter:", 140, 425, "draengen", "Bold", 34, bis=BW),
    z("die Schwester tötet das Neugeborene", 140, 470, beim("draengen", "tötet"), "Bold", 34, bis=BW),
    blk(140, 545, 980, 80, ROTHELL, "rg", [("Reichsgericht: nur Gehilfin", "ExtraBold", 36, INK)], bis=BW),
    z("Täterin: die Mutter, Tat als eigene gewollt", 140, 650, beim("rg", "Täterin"), size=34, bis=BW),
    # Akte 1 kompakt, Akte 2: Staschinski-Fall (Akte, Stadtsilhouette, Jahreszahl; keine Waffe)
    *akte(90, 80, 1080, 170, BW),
    z("Badewannen-Fall", 140, 105, beim("bw", "Badewannen"), "ExtraBold", 40),
    z("Reichsgericht 1940 · RGSt 74, 84 · nur Gehilfin", 140, 170, BW, size=30),
    ficon("fluent-emoji-flat", "classical-building", 1090, 230, 90, BW),
    *akte(90, 330, 1080, 520, ST),
    z("Bundesgerichtshof · 1962", 140, 355, ST, "ExtraBold", 44),
    ficon("fluent-emoji-flat", "cityscape", 1040, 520, 150, "muc"),
    pl("München", 1040, 545, "muc", fill=WEISS, size=28, anker="m"),
    z("Agent des sowjetischen Geheimdienstes", 140, 435, beim("stasch", "Agenten"), size=34, rechts=930),
    z("2 ukrainische Exilpolitiker getötet", 140, 485, beim("muc", "zwei"), size=34, rechts=930),
    z("im Auftrag seiner Vorgesetzten", 140, 535, beim("muc", "Auftrag"), size=34, rechts=930),
    blk(140, 610, 980, 80, ROTHELL, "bgh62", [("BGH: nur Beihilfe zum Mord", "ExtraBold", 36, INK)]),
    z("Staschinski-Fall · BGHSt 18, 87", 140, 720, beim("bgh62", "Staschinski"), "Bold", 34),
    # Luise und Oskar (blicken zu den Akten)
    peep_voll("LU_still", LX_, BODEN, FH, NULL, bis=beim("draengen", "tötet")),
    peep_voll("LU_ernst", LX_, BODEN, FH, beim("draengen", "tötet"), anim="cut", bis="l1"),
    *redet("LU_redet", LX_, BODEN, FH, "l1", BW),
    peep_voll("LU_zweifel", LX_, BODEN, FH, BW, anim="cut", bis="frage"),
    peep_voll("LU_still", LX_, BODEN, FH, "frage", anim="cut"),
    namensschild("Luise", LX_, BODEN - 8, NULL, GRUEN),
    peep_voll("OS_still", OX_, BODEN, FH, NULL, bis="rg"),
    peep_voll("OS_ernst", OX_, BODEN, FH, "rg", anim="cut", bis="bgh62"),
    peep_voll("OS_zweifel", OX_, BODEN, FH, "bgh62", anim="cut", bis="o1"),
    *redet("OS_redet", OX_, BODEN, FH, "o1", "frage"),
    peep_voll("OS_ernst", OX_, BODEN, FH, "frage", anim="cut"),
    namensschild("Oskar", OX_, BODEN - 8, NULL, BLAU),
    blase("sprech", 640, 240, "l1", 1580, 190, inhalt=["Die Schwester hat doch", "selbst gehandelt.", "Warum nur Gehilfin?"],
          textsize=30, figur=LUr, bis=BW),
    blase("sprech", 640, 240, "o1", 1600, 190, inhalt=["Wer selbst tötet,", "ist doch Täter.", "Oder etwa nicht?"],
          textsize=30, figur=OSr, bis="frage"),
    pl("Täter, Anstifter oder Gehilfe?", 1560, 150, "frage", fill=PINK, size=32, anker="m"),
    pl("Rechtsprechung gegen Lehre", 1560, 225, "frage2", fill=WEISS, size=30, anker="m"),
])

# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
sachverhalt_klein("sv", [
    "Badewannen-Fall (Reichsgericht 1940, RGSt 74, 84): Eine junge Frau verheimlicht aus Angst vor ihrem Vater ihre "
    "Schwangerschaft und bringt das Kind mit Hilfe ihrer Schwester heimlich zur Welt. Auf Drängen der Mutter tötet die "
    "Schwester das Neugeborene unmittelbar nach der Geburt. Das Reichsgericht sieht in ihr nur eine Gehilfin; Täterin sei "
    "die Mutter, die die Tat als eigene gewollt habe.",
    "Staschinski-Fall (Bundesgerichtshof 1962, BGHSt 18, 87): Ein Agent des sowjetischen Geheimdienstes tötet in München "
    "zwei ukrainische Exilpolitiker, im Auftrag seiner Vorgesetzten. Der Bundesgerichtshof verurteilt ihn nur wegen "
    "Beihilfe zum Mord.",
], "Wann ist jemand Täter, wann nur Anstifter oder Gehilfe?")

# ===========================================================================================================================
# C 1. Das Problem: Wortlaut § 25 Abs. 1 und § 27 Abs. 1, dazwischen § 26
# ===========================================================================================================================
W25 = [[("„Als ", 0), ("Täter", "a"), (" wird bestraft, wer die Straftat ", 0), ("selbst", "b")],
       [("oder ", 0), ("durch einen anderen", "c"), (" begeht.“", 0)]]
W27 = [[("„Als ", 0), ("Gehilfe", "a"), (" wird bestraft, wer vorsätzlich einem", 0)],
       [("anderen zu dessen vorsätzlich begangener", 0)], [("rechtswidriger Tat ", 0), ("Hilfe geleistet", "d"), (" hat.“", 0)]]
P1 = "1. Problem: Täter oder Teilnehmer?"
folie([("prob", f"{P1} › Täter, § 25 Abs. 1 StGB"), ("p27", f"{P1} › Gehilfe, § 27 Abs. 1 StGB"),
       ("p26", f"{P1} › Anstifter, § 26 StGB")], rechts_frei([
    *tafel("prob", "1. Täter oder Teilnehmer?"),
    *wortlaut(100, 175, 1060, 135, beim("prob", "Paragraf"), W25, 34,
              {"a": beim("p25w", "Täter"), "b": beim("p25w", "selbst"), "c": beim("p25w", "durch")}, "§ 25 Abs. 1 StGB",
              farben={"a": GELB, "b": GRUEN, "c": BLAU}),
    *wortlaut(100, 380, 1060, 185, "p27", W27, 32, {"a": beim("p27w", "Gehilfe"), "d": beim("p27w", "Hilfe")},
              "§ 27 Abs. 1 StGB", farben={"a": LILA, "d": LILA}),
    blk(100, 640, 1060, 120, BLAUHELL, "p26", [("dazwischen: der Anstifter, § 26 StGB", "ExtraBold", 34, INK),
                                               ("bestimmt einen anderen zur Tat", "Regular", 32, INK)]),
    *paar("prob", [("ernst", "p27"), ("ruhig", "p26")], [("ruhig", "p27"), ("ernst", "p26")]),
    pl("Täter: § 25", MB, 160, beim("p25w", "Täter"), fill=GELB, size=30, anker="m", bis="p27"),
    pl("Gehilfe: § 27", MB, 160, beim("p27w", "Gehilfe"), fill=LILA, size=30, anker="m", anim="cut", bis="p26"),
    pl("Anstifter: § 26", MB, 160, beim("p26", "Anstifter"), fill=BLAU, size=30, anker="m", anim="cut"),
    ficon("fluent-emoji-flat", "balance-scale", MB, 390, 120, "prob"),
]))

# ===========================================================================================================================
# D Warum die Abgrenzung zählt: Strafrahmen
# ===========================================================================================================================
folie([("straf", f"{P1} › Strafrahmen")], rechts_frei([
    *tafel("straf", "Warum die Abgrenzung zählt"),
    karte(110, 175, 1040, 150, "anst", fill=BLAUHELL, rund=18, schatten=6, rand=4),
    z("Anstifter:", 140, 190, "anst", "ExtraBold", 34),
    z("gleich einem Täter bestraft, § 26 StGB", 140, 240, beim("anst", "gleich"), "Bold", 34),
    karte(110, 355, 1040, 200, "mild", fill=LILAHELL, rund=18, schatten=6, rand=4),
    z("Gehilfe:", 140, 370, "mild", "ExtraBold", 34),
    z("Strafe zwingend gemildert,", 140, 420, beim("mild", "gemildert"), "Bold", 34),
    z("§ 27 Abs. 2 Satz 2, § 49 Abs. 1 StGB", 140, 470, beim("mild", "Paragraf"), size=33),
    blk(110, 600, 1040, 130, GELB, "mord", [("Beim Mord statt lebenslang:", "ExtraBold", 36, INK),
                                          ("Freiheitsstrafe nicht unter 3 Jahren", "ExtraBold", 36, INK)]),
    fund("§ 211 Abs. 1, § 49 Abs. 1 Nr. 1 StGB", 150, 750, beim("mord", "drei")),
    *paar("straf", [("ernst", "mild"), ("zweifel", "mord")], [("ruhig", "anst"), ("ernst", "mord")]),
    pl("Anstifter = Täter", MB, 160, "anst", fill=BLAU, size=30, anker="m", bis="mild"),
    pl("Gehilfe: milder", MB, 160, beim("mild", "gemildert"), fill=LILA, size=30, anker="m", anim="cut", bis="mord"),
    pl("lebenslang / ab 3 Jahre", MB, 160, beim("mord", "lebenslanger"), fill=GELB, size=30, anker="m", anim="cut"),
    ficon("fluent-emoji-flat", "balance-scale", MB, 390, 120, "anst"),
]))

# ===========================================================================================================================
# E 2. Reichsgericht: extrem subjektive Theorie
# ===========================================================================================================================
P2 = "2. Subjektive Theorie des Reichsgerichts"
folie([("rg1", f"{P2} › innerer Wille"), ("auct", f"{P2} › animus auctoris"), ("socii", f"{P2} › animus socii"),
       ("rgbw", f"{P2} › Badewannen-Fall, RGSt 74, 84")], rechts_frei([
    *tafel("rg1", "2. Reichsgericht: der innere Wille"),
    z("entscheidend: der innere Wille", 110, 175, beim("rg1", "inneren"), "Bold", 36),
    karte(110, 245, 505, 250, "auct", fill=GRUENHELL, rund=18, schatten=6, rand=4),
    z("Täter:", 135, 260, "auct", "ExtraBold", 34, rechts=600),
    z("will die Tat", 135, 310, beim("auct", "eigene"), size=32, rechts=600),
    z("als eigene", 135, 352, beim("auct", "eigene"), "Bold", 32, rechts=600),
    z("animus auctoris", 135, 420, beim("auct", "animus"), "ExtraBold", 32, rechts=600),
    karte(645, 245, 505, 250, "socii", fill=LILAHELL, rund=18, schatten=6, rand=4),
    z("Teilnehmer:", 670, 260, "socii", "ExtraBold", 34, rechts=1135),
    z("will die Tat", 670, 310, beim("socii", "fremde"), size=32, rechts=1135),
    z("als fremde", 670, 352, beim("socii", "fremde"), "Bold", 32, rechts=1135),
    z("animus socii", 670, 420, beim("socii", "animus"), "ExtraBold", 32, rechts=1135),
    z("Badewannen-Fall:", 110, 545, "rgbw", "ExtraBold", 34),
    z("Schwester beugt sich dem Willen der Mutter", 110, 595, beim("rgbw", "Schwester"), size=33),
    blk(110, 665, 1040, 80, ROTHELL, beim("rgbw", "Also"), [("also nur Gehilfin", "ExtraBold", 34, INK)]),
    fund("RGSt 74, 84; nach Hefendehl, Vorlesung StGB AT, Uni Freiburg, KK 682 f.", 140, 770, beim("rgbw", "Badewannen")),
    *paar("rg1", [("ernst", "auct"), ("zweifel", "rgbw")], [("ruhig", "socii"), ("ernst", "rgbw")]),
    pl("Wille entscheidet", MB, 160, beim("rg1", "inneren"), fill=WEISS, size=30, anker="m", bis="auct"),
    pl("Tat als eigene", MB, 160, beim("auct", "eigene"), fill=GRUEN, size=30, anker="m", anim="cut", bis="socii"),
    pl("Tat als fremde", MB, 160, beim("socii", "fremde"), fill=LILA, size=30, anker="m", anim="cut", bis="rgbw"),
    pl("nur Gehilfin?", MB, 160, beim("rgbw", "Also"), fill=ROTHELL, size=30, anker="m", anim="cut"),
    ficon("fluent-emoji-flat", "brain", MB, 380, 100, beim("rg1", "inneren"), bis="rgbw"),
    ficon("fluent-emoji-flat", "classical-building", MB, 390, 110, "rgbw", anim="cut"),
]))

# ===========================================================================================================================
# F Bundesgerichtshof 1956 und Staschinski-Fall 1962
# ===========================================================================================================================
Z56 = [[("„Wer ", 0), ("mit eigener Hand", "a"), (" einen Menschen tötet, ist", 0)],
       [("grundsätzlich auch dann Täter", "b"), (", wenn er es unter dem", 0)],
       [("Einfluss und in Gegenwart eines anderen", 0)], [("nur in dessen Interesse tut.“", 0)]]
folie([("bgh56", f"{P2} › BGH 1956: BGHSt 8, 393"), ("st1", f"{P2} › Staschinski-Fall, BGHSt 18, 87")], rechts_frei([
    *tafel("bgh56", "BGH 1956 und der Staschinski-Fall"),
    *wortlaut(100, 165, 1060, 225, "zit56", Z56, 32, {"a": beim("zit56", "eigener"), "b": beim("zit56", "grundsätzlich")},
              "BGHSt 8, 393 (1956), nach BGH 3 StR 35/92, Rn. 6", farben={"a": GELB, "b": GRUEN}),
    z("Staschinski-Fall (1962):", 110, 460, "st1", "ExtraBold", 34),
    z("wieder entscheidend der Wille", 140, 510, beim("st1", "wieder"), size=33),
    nein(135, 590, "st2", gr=18),
    z("Agent: nur widerwillig gebeugt,", 175, 570, "st2", size=33),
    z("kein eigenes Interesse an der Tat", 175, 615, beim("st2", "kein"), "Bold", 33),
    ok(135, 695, "st3", gr=18),
    z("Auftraggeber beherrschten Ob und Wie:", 175, 675, "st3", size=33),
    z("sie seien die Täter", 175, 720, beim("st3", "Sie"), "Bold", 33),
    fund("BGHSt 18, 87 (93 f., 96), nach Hefendehl, KK 683 ff.", 140, 790, beim("st3", "Täter")),
    *paar("bgh56", [("froh", "zit56"), ("zweifel", "st1"), ("ernst", "st3")], [("ruhig", "zit56"), ("froh", beim("zit56", "grundsätzlich")),
                                                                           ("zweifel", "st1"), ("ernst", "st3")]),
    pl("BGH 1956: abgerückt", MB, 160, "bgh56", fill=GRUEN, size=30, anker="m", bis="st1"),
    ficon("fluent-emoji-flat", "classical-building", MB, 390, 110, "bgh56", bis="st1"),
    pl("1962: wieder der Wille", MB, 160, beim("st1", "wieder"), fill=ROTHELL, size=30, anker="m", anim="cut", bis="st3"),
    ficon("fluent-emoji-flat", "cityscape", MB, 390, 140, "st1", anim="cut"),
    pl("Täter: die Auftraggeber", MB, 160, "st3", fill=WEISS, size=30, anker="m", anim="cut"),
]))

# ===========================================================================================================================
# G 3. Kritik und Wende: § 25 Abs. 1 Alt. 1 StGB
# ===========================================================================================================================
P3 = "3. Kritik und Wende"
W25A = [[("„Als Täter wird bestraft, wer die Straftat ", 0), ("selbst", "a"), (" … begeht.“", 0)]]
folie([("krit", f"{P3} › Täterwille kaum greifbar"), ("wende", f"{P3} › § 25 Abs. 1 Alt. 1 StGB"),
       ("bgh92", f"{P3} › BGH: eigenhändig = grundsätzlich Täter")], rechts_frei([
    *tafel("krit", "3. Kritik und Wende"),
    nein(135, 195, "k1", gr=18),
    z("Täterwille kaum greifbar:", 175, 175, "k1", "Bold", 34),
    z("Abgrenzung nach richterlichem Ermessen", 175, 220, beim("k1", "Abgrenzung"), size=33),
    nein(135, 300, "k2", gr=18),
    z("löst sich vom Tatbestand", 175, 280, "k2", "Bold", 34),
    *wortlaut(100, 375, 1060, 80, "w25", W25A, 34, {"a": beim("w25", "selbst")}, "§ 25 Abs. 1 Alt. 1 StGB, seit 1.1.1975"),
    z("BGH: wer alle Tatbestandsmerkmale selbst", 110, 525, "bgh92", "Bold", 34),
    z("verwirklicht, ist grundsätzlich Täter,", 110, 570, beim("bgh92", "verwirklicht"), "Bold", 34),
    z("auch im Interesse eines anderen", 110, 615, beim("bgh92", "auch"), size=33),
    fund("BGH, Urt. v. 22.7.1992 – 3 StR 35/92 (BGHSt 38, 315), Rn. 4–6", 150, 665, beim("bgh92", "Tatbestandsmerkmale")),
    blk(110, 720, 1040, 80, GELB, "stets", [("Lehre: stets Täter", "ExtraBold", 34, INK)]),
    *paar("krit", [("zweifel", "k2"), ("ernst", "wende"), ("froh", "bgh92")], [("ernst", "k1"), ("ruhig", "w25"),
                                                                              ("froh", "stets")]),
    pl("Kritik", MB, 160, "krit", fill=ROTHELL, size=30, anker="m", bis="wende"),
    pl("Wende: Gesetzgeber", MB, 160, "wende", fill=GELB, size=30, anker="m", anim="cut", bis=beim("w25", "Seit")),
    pl("seit 1975", MB, 160, beim("w25", "Seit"), fill=GELB, size=30, anker="m", anim="cut", bis=beim("bgh92", "selbst")),
    ficon("fluent-emoji-flat", "spiral-calendar", MB, 390, 100, beim("w25", "Seit"), bis="bgh92"),
    pl("selbst = Täter", MB, 160, beim("bgh92", "selbst"), fill=GRUEN, size=30, anker="m", anim="cut"),
    ficon("fluent-emoji-flat", "classical-building", MB, 390, 110, "bgh92", anim="cut"),
]))

# ===========================================================================================================================
# H 4. Tatherrschaftslehre
# ===========================================================================================================================
P4 = "4. Tatherrschaftslehre (h. L.)"
folie([("thl", f"{P4} › Zentralgestalt"), ("formen", f"{P4} › drei Formen der Tatherrschaft")], rechts_frei([
    *tafel("thl", "4. Tatherrschaftslehre"),
    karte(110, 170, 1040, 210, "zg", fill=GRUENHELL, rund=18, schatten=6, rand=4),
    z("Täter: die Zentralgestalt des Geschehens,", 140, 185, "zg", "ExtraBold", 33),
    z("hält es vom Vorsatz umfasst in den Händen", 140, 235, beim("zg", "wer"), size=32),
    z("Teilnehmer: nur eine Randfigur", 140, 300, "rand", "Bold", 32),
    z("Drei Formen:", 110, 420, "formen", "ExtraBold", 36),
    blk(110, 480, 1040, 80, BLAUHELL, "hh", [("Handlungsherrschaft: handelt selbst", "Bold", 33, INK)]),
    blk(110, 580, 1040, 80, LILAHELL, "wh", [("Willensherrschaft: steuert ein Werkzeug", "Bold", 33, INK)]),
    blk(110, 680, 1040, 80, GELB, "fh", [("funktionale Tatherrschaft: arbeitsteilig", "Bold", 33, INK)]),
    fund("Lehre: nach Hefendehl, Vorlesung StGB AT, Uni Freiburg, KK 688 f.", 140, 785, beim("zg", "Zentralgestalt")),
    *paar("thl", [("ernst", "zg"), ("froh", "hh"), ("ruhig", "fh")], [("ruhig", "rand"), ("ernst", "wh"), ("froh", "fh")]),
    pl("Zentralgestalt", MB, 160, beim("zg", "Zentralgestalt"), fill=GRUEN, size=30, anker="m", bis="rand"),
    pl("oder Randfigur?", MB, 160, "rand", fill=WEISS, size=30, anker="m", anim="cut", bis="hh"),
    ficon("fluent-emoji-flat", "bullseye", MB, 380, 100, beim("zg", "Zentralgestalt"), bis="hh"),
    pl("selbst handeln", MB, 160, "hh", fill=BLAU, size=30, anker="m", anim="cut", bis="wh"),
    pl("Werkzeug steuern", MB, 160, "wh", fill=LILA, size=30, anker="m", anim="cut", bis="fh"),
    pl("zusammenwirken", MB, 160, "fh", fill=GELB, size=30, anker="m", anim="cut"),
    ficon("fluent-emoji-flat", "puzzle-piece", MB, 380, 90, "fh", anim="cut"),
]))

# ===========================================================================================================================
# I 5. Streitstand im Zweispalter (heutige Rechtsprechung)
# ===========================================================================================================================
P5 = "5. Streitstand"
LS, RS = 135, 750
folie([("zw", f"{P5} › Rechtsprechung"), ("zr0", f"{P5} › Lehre"), ("v104", f"{P5} › Mittäter: Folge 104")], rechts_frei([
    *tafel("zw", "5. Streitstand"),
    z("Rechtsprechung", LS - 25, 170, "zl0", "ExtraBold", 36, rechts=680),
    linienzug([(695, 175), (695, 750)], "zw", breite=4),
    z("Lehre", RS - 25, 170, "zr0", "ExtraBold", 36),
    z("RG: Täterwille", LS, 235, "zl1", "Bold", 32, rechts=680),
    z("BGH heute: wertende", LS, 290, "zl2", "Bold", 32, rechts=680),
    z("Gesamtbetrachtung", LS, 332, beim("zl2", "Gesamtbetrachtung"), "Bold", 32, rechts=680),
    z("1. eigenes Interesse an der Tat", LS, 395, beim("zl3", "Grad"), size=30, rechts=680),
    z("2. Umfang der Tatbeteiligung", LS, 440, beim("zl3", "Umfang"), size=30, rechts=680),
    z("3. Tatherrschaft oder", LS, 485, beim("zl3", "Tatherrschaft"), size=30, rechts=680),
    z("wenigstens der Wille dazu", LS + 30, 527, beim("zl3", "wenigstens"), size=30, rechts=680),
    z("Tatherrschaft nur ein Kriterium,", LS, 590, "zl4", "Bold", 30, rechts=680),
    z("Schwächen ausgleichbar", LS, 632, beim("zl4", "Schwächen"), "Bold", 30, rechts=680),
    fund("BGH 3 StR 363/22, Rn. 8;", LS, 680, beim("zl3", "Grad"), rechts=680),
    fund("BGH 3 StR 189/19, Rn. 6", LS, 718, beim("zl4", "Schwächen"), rechts=680),
    z("Tatherrschaft:", RS, 235, "zr1", "Bold", 32),
    z("Wer ist", RS, 290, "zr2", size=32),
    z("Zentralgestalt?", RS, 332, beim("zr2", "Zentralgestalt"), "Bold", 32),
    blk(110, 770, 1040, 80, BLAUHELL, beim("v104", "zeigt"), [("Bei Mittätern: unsere Folge zur Mittäterschaft", "Bold", 32, INK)]),
    *paar("zw", [("ernst", "zl2"), ("ruhig", "zr0"), ("froh", "v104")], [("ruhig", "zl3"), ("ernst", "zl4"), ("froh", "zr1")]),
    pl("Rechtsprechung", MB, 160, "zl0", fill=LILA, size=30, anker="m", bis="zr0"),
    ficon("fluent-emoji-flat", "balance-scale", MB, 390, 120, "zl2", bis="zr0"),
    pl("Lehre", MB, 160, "zr0", fill=GRUEN, size=30, anker="m", anim="cut", bis="v104"),
    ficon("fluent-emoji-flat", "bullseye", MB, 380, 100, "zr1", bis="v104"),
    pl("Folge 104", MB, 160, beim("v104", "zeigt"), fill=BLAU, size=30, anker="m", anim="cut"),
]))

# ===========================================================================================================================
# J 6. Streitentscheid
# ===========================================================================================================================
P6 = "6. Streitentscheid"
folie([("ents", f"{P6} › Tatherrschaftslehre"), ("dahin", f"{P6} › Wann der Streit dahinstehen kann")], rechts_frei([
    *tafel("ents", "6. Streitentscheid"),
    blk(110, 170, 1040, 80, GRUENHELL, "ents", [("Wir folgen der Tatherrschaftslehre", "ExtraBold", 34, INK)]),
    ok(135, 305, "e1", gr=18),
    z("knüpft an das Begehen der Tat an", 175, 285, "e1", "Bold", 34),
    nein(135, 390, "e2", gr=18),
    z("Rechtsprechung: Kriterien ohne feste", 175, 370, "e2", size=33),
    z("Rangfolge, fast beliebige Ergebnisse", 175, 415, beim("e2", "So"), size=33),
    z("In der Klausur:", 110, 500, "dahin", "ExtraBold", 36),
    blk(110, 560, 1040, 80, WEISS, beim("dahin", "Kommen"), [("gleiches Ergebnis: Streit kann dahinstehen", "Bold", 33, INK)]),
    blk(110, 660, 1040, 80, GELB, "dahin2", [("verschiedene Ergebnisse: entscheiden", "Bold", 33, INK)]),
    *paar("ents", [("froh", "e1"), ("ernst", "dahin")], [("ruhig", "e2"), ("froh", "dahin2")]),
    pl("Tatherrschaft", MB, 160, "ents", fill=GRUEN, size=30, anker="m", bis="dahin"),
    ficon("fluent-emoji-flat", "balance-scale", MB, 390, 120, "ents", bis="dahin"),
    pl("gleich? dahinstehen", MB, 160, beim("dahin", "Kommen"), fill=WEISS, size=30, anker="m", anim="cut", bis="dahin2"),
    pl("verschieden? entscheiden", MB, 160, "dahin2", fill=GELB, size=30, anker="m", anim="cut"),
    ficon("fluent-emoji-flat", "memo", MB, 380, 90, beim("dahin", "Kommen")),
]))

# ===========================================================================================================================
# K Ergebnis nach heutigem Recht
# ===========================================================================================================================
folie([("erg", "Ergebnis nach heutigem Recht"), ("erg1", "Ergebnis · Badewannen-Fall: Schwester ist Täterin"), ("erg2", "Ergebnis · Staschinski-Fall: Täter"),
       ("erg3", "Ergebnis · Auftraggeber: Täter hinter dem Täter?")], rechts_frei([
    *tafel("erg", "Ergebnis nach heutigem Recht"),
    karte(110, 170, 1040, 200, "erg1", fill=GRUENHELL, rund=18, schatten=6, rand=4),
    z("Badewannen-Fall: Schwester ist Täterin", 140, 185, "erg1", "ExtraBold", 34),
    z("alle Merkmale selbst verwirklicht,", 140, 240, beim("erg1", "Sie"), size=33),
    z("§ 25 Abs. 1 Alt. 1 StGB", 140, 290, beim("erg1", "Paragraf"), "Bold", 33),
    karte(110, 400, 1040, 200, "erg2", fill=BLAUHELL, rund=18, schatten=6, rand=4),
    z("Staschinski-Fall: Täter", 140, 415, "erg2", "ExtraBold", 34),
    z("nach der Tatherrschaftslehre ohnehin,", 140, 470, beim("erg2", "nach"), size=33),
    z("nach dem BGH wohl ebenso", 140, 520, beim("erg2", "nach", nr=2), size=33),
    fund("vgl. Hefendehl, KK 686", 760, 525, beim("erg2", "wohl")),
    z("Auftraggeber: Täter hinter dem Täter?", 110, 650, "erg3", "Bold", 34),
    blk(110, 710, 1040, 80, LILAHELL, beim("erg3", "wie"), [("wie im Katzenkönig-Fall", "Bold", 33, INK)]),
    *paar("erg", [("froh", "erg1"), ("ernst", "erg3")], [("ruhig", "erg1"), ("froh", "erg2"), ("zweifel", "erg3")]),
    pl("Täterin", MB, 160, "erg1", fill=GRUEN, size=30, anker="m", bis="erg2"),
    ficon("fluent-emoji-flat", "classical-building", MB, 390, 110, "erg1", bis="erg2"),
    pl("Täter", MB, 160, "erg2", fill=BLAU, size=30, anker="m", anim="cut", bis="erg3"),
    ficon("fluent-emoji-flat", "cityscape", MB, 390, 140, "erg2", anim="cut", bis="erg3"),
    pl("Täter hinter dem Täter?", MB, 160, "erg3", fill=LILA, size=30, anker="m", anim="cut"),
]))

# ===========================================================================================================================
# L Klausurtipp (Lexi)
# ===========================================================================================================================
LXX = 1560
folie([("tipp", "Klausurtipp · Tatnächsten zuerst"), ("tipp3", "Klausurtipp · Streit nur, wo er zählt")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Prüfe zuerst den Tatnächsten", 200, 200, beim("tipp", "Prüfe"), "ExtraBold", 36),
    z("alle Merkmale selbst erfüllt:", 200, 300, "tipp2", "Bold", 34),
    z("Täter, ein Satz genügt", 200, 347, beim("tipp2", "ist"), "Bold", 34),
    z("Streit nur dort ausbreiten, wo die", 200, 450, "tipp3", "Bold", 34),
    z("Ansichten auseinanderfallen können", 200, 497, beim("tipp3", "Ansichten"), "Bold", 34),
    fund("Tatnächster zuerst: Hefendehl, KK 717", 200, 600, beim("tipp", "Tatnächsten")),
    *redet("LX_warnt", LXX, BR, 540, "tipp", "sch"),
    namensschild("Lexi", LXX, BR, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# M Klausurschema
# ===========================================================================================================================
K1, K2 = 150, 230
PSS = "Klausurschema"
folie([("sch", PSS), ("s_i", f"{PSS} › I. Deliktstyp"), ("s_ii", f"{PSS} › II. eigenhändig: Täter"),
       ("s_iii", f"{PSS} › III. sonst: der Streit"), ("s_iv", f"{PSS} › IV. Anstiftung oder Beihilfe")], [
    karte(60, 50, 1800, 920, "sch"),
    titel("Klausurschema: Abgrenzung Täter – Teilnehmer", 110, 90, "sch", 48),
    z("I. Deliktstyp: Sonderdelikt oder eigenhändiges Delikt?", K1, 190, "s_i", "Bold", 38, rechts=1820),
    z("dann entscheidet schon der Tatbestand", K2, 250, beim("s_i", "entscheidet"), size=34, rechts=1820),
    z("II. Alle Merkmale selbst verwirklicht? Dann Täter, § 25 Abs. 1 Alt. 1", K1, 330, "s_ii", "Bold", 38, rechts=1820),
    z("III. Sonst der Streit:", K1, 420, "s_iii", "Bold", 38, rechts=1820),
    z("1. Tatherrschaftslehre", K2, 480, "s3a", size=34, rechts=1820),
    z("2. wertende Gesamtbetrachtung der Rechtsprechung", K2, 540, "s3b", size=34, rechts=1820),
    z("3. Streitentscheid nur, wenn die Ergebnisse auseinanderfallen", K2, 600, "s3c", size=34, rechts=1820),
    z("IV. Ohne Täterschaft: Anstiftung, § 26, oder Beihilfe, § 27", K1, 690, "s_iv", "Bold", 38, rechts=1820),
])

# ===========================================================================================================================
# N Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 170, "merke", 84, anker="m"),
    *merktext([[("Wer die Tat ", 0), ("selbst begeht", "a"), (", ist Täter,", 0)], [("auch im Interesse eines anderen.", 0)]],
              750, 280, 42, "merke", {"a": beim("merke", "selbst")}, 1300),
    *merktext([[("Bei allen anderen: die Lehre nach der ", 0), ("Tatherrschaft", "b"), (",", 0)],
               [("die Rechtsprechung nach ", 0), ("wertender Gesamtbetrachtung", "c"), (".", 0)]],
              750, 450, 42, "m_2", {"b": beim("m_2", "Tatherrschaft"), "c": beim("m_2", "wertenden")}, 1300),
    *merktext([[("Der ", 0), ("Täterwille allein", "d"), (" entscheidet nicht mehr.", 0)]],
              750, 640, 42, "m_3", {"d": beim("m_3", "Täterwille")}, 1300),
    *redet("LX_erklaert", 1680, 960, 690, "merke", lexi_bis_ende("merke")),
    namensschild("Lexi", 1680, 960, "merke", GELB, d=0.2),
])

# Zeichenprüfung für alle übrigen Texte (Pfade, Blöcke, Titel, Blasen, Sachverhalt)
for f_ in FOLIEN:
    for _, t_ in f_["pfade"]:
        glyphen(t_)
    for e_ in f_["els"]:
        n_ = e_.name or ""
        if n_.startswith(("block:", "titel:", "pille:", "blase:")):
            glyphen(n_.split(":", 1)[1].replace("(", "").replace(")", "").replace("'", ""))
