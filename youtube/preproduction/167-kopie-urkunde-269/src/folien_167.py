"""Folge 167 · Kopie als Urkunde? Scan, PDF & § 269 StGB – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A1 Fall zu Hause (Zeugnis 2,8, Scan, Note am Rechner auf 1,8, PDF, E-Mail), A2 Fall in der
Personalabteilung (Frau Hagemann, Variante Ausdruck per Post als Kopie, Frage), B Sachverhalt, C einfache Fotokopie
(Urkundenbegriff nur als Verweis), D Streitstand, E Ausnahmen und Grenze (Anschein des Originals, gefälschtes Original/
beglaubigte Kopie, Collage), F Datei: Wortlautkarte § 269 Abs. 1, hypothetischer Urkundenvergleich, G1 Scan oder digitales
Original, G2 PDF-Zeugnis (OLG Celle), Gegenansicht, Wortlautkarte § 270, H1/H2 Lösung beider Varianten und Ausblick Betrug,
I Merktabelle, J Klausurtipp (Lexi), K Merksatz (Lexi). Zeugnis nur als neutrales Dokument mit Note als Ziffer (keine
Schule, kein Logo). Geräusche nur bei sichtbarer Handlung: Scanner, Tastatur, Drucker (Freesound CC0).
Hilfsfunktionen (z, pl, tafel, wortlaut, fb, redet mit hörbarem Wortende, stufen, wechsel, icons, zeile_ok) wie in
Folge 137, Kopie im eigenen Ordner."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont

bausteine.FIGORDNER = "op_167/"
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
NULL = "fall"                     # Szene A steht ab 0,0 s (render_167 setzt alle Elemente bis zur Marke „fall“ auf 0,0 s)

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
FARBE = {"JA": ROT, "HA": LILA}
NAME = {"JA": "Janosch", "HA": "Frau Hagemann"}


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




def st(p, x, folge, **k):
    return stufen(p, x, folge, **k)


DROTT = (215, 60, 45, 255)


def zeugnis(x, y, w, cue, note, note_cue, neu=None, neu_cue=None, bis=None, size=32, gross=72, kopie=False):
    """Neutrales Zeugnis-Dokument (Karte, keine Schule, kein Logo) mit der Note als Ziffer; neu = geänderte Note (rot)."""
    h = int(size * 1.35) * 2 + gross + 70
    k = karte(x, y, w, h, cue, fill=(246, 246, 250, 255) if kopie else WEISS, rund=10, schatten=6, rand=4)
    k.bis = bis
    els = [k, z("Abiturzeugnis", x + 26, y + 20, cue, "ExtraBold", size, rechts=x + w - 14, bis=bis),
           z("Note", x + 26, y + 20 + int(size * 1.35), cue, "Regular", max(26, size - 4), rechts=x + w - 14, bis=bis)]
    yn = y + 30 + int(size * 1.35) * 2
    els.append(z(note, x + 26, yn, note_cue, "ExtraBold", gross, rechts=x + w - 14, bis=(neu_cue if neu else bis)))
    if neu:
        els.append(z(neu, x + 26, yn, neu_cue, "ExtraBold", gross, farbe=DROTT, rechts=x + w - 14, bis=bis))
    return els


# ======================================================================================================================
# A1 Fall: das Zeugnis wird gescannt, geändert und als PDF verschickt (bei Janosch zu Hause)
# ======================================================================================================================
BODEN, FH = 880, 520
FX = 380                                  # Janosch, blickt nach rechts zu Schreibtisch und Zeugnis
ZX, ZY, ZW = 900, 150, 470                # Zeugnis
IX = 1660                                 # Requisiten rechts (Scanner, PDF)
TISCH = ficon("tabler", "desk", 720, BODEN - 2, 300, NULL, fuell=(214, 160, 110, 255))
TT = int(TISCH.y) + 8
folie([(NULL, "Fall · Die Bewerbung"), ("note", "Fall · Das Zeugnis: Note 2,8"), ("scan", "Fall · Der Scan"),
       ("aendern", "Fall · Note am Rechner geändert"), ("pdf", "Fall · PDF per E-Mail")], [
    linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK),
    TISCH,
    ficon("fluent-emoji-flat", "laptop", 720, TT, 150, NULL),
    *st("JA", FX, [("ruhig_r", NULL), ("denkt_r", "note"), ("eifrig_r", "aendern"), ("redet_r", "j1"), ("froh_r", "pdf"),
                   ("ruhig_r", "mail")], rede=("redet_r",), unten=BODEN, hoehe=FH, erst="cut", d=-0.2),
    pl("20 Jahre", FX, 300, beim("fall", "zwanzig"), fill=WEISS, size=28, anker="m", bis="note"),
    pl("Bewerbung als Sachbearbeiter", 70, 40, beim("fall", "Stelle"), fill=GELB, size=34, bis="note"),
    *zeugnis(ZX, ZY, ZW, "note", "2,8", beim("note", "zwei"), neu="1,8", neu_cue=beim("aendern", "eins")),
    szene(ficon("tabler", "scan", IX, 470, 150, "scan", bis="pdf"), "167scan_1", 1.0),
    pl("eingescannt", IX, 520, beim("scan", "scannt"), fill=WEISS, size=30, anker="m", bis="pdf"),
    szene(pl("am Rechner geändert", ZX + ZW // 2, 520, beim("aendern", "ändert"), fill=ROTHELL, size=30, anker="m", bis="j1"),
          "167tasten_1", 1.0),
    blase("sprech", 520, 175, "j1", 640, 215, inhalt=["Eine 1 vorne sieht", "einfach besser aus."], textsize=34,
          figur=("JA_redet_r", FX, BODEN, FH), bis="pdf"),
    ficon("tabler", "file-type-pdf", IX, 470, 150, "pdf"),
    pl("als PDF gespeichert", IX, 520, beim("pdf", "speichert"), fill=WEISS, size=30, anker="m", bis="mail"),
    bewegt(ficon("fluent-emoji-flat", "e-mail", 1200, 760, 110, beim("mail", "schickt")), beim("mail", "schickt"),
           beim("mail", "Frau"), -400, 0),
    pl("per E-Mail an Frau Hagemann", 1520, 520, "mail", fill=LILAHELL, size=30, anker="m", anim="cut"),
])

# ======================================================================================================================
# A2 Fall: Personalabteilung, Variante (Ausdruck per Post als Kopie), Frage
# ======================================================================================================================
HX = 1650
TISCH2 = ficon("tabler", "desk", 1260, BODEN - 2, 280, "h1", fuell=(214, 160, 110, 255))
TT2 = int(TISCH2.y) + 8
folie([("h1", "Fall · In der Personalabteilung"), ("variante", "Fall · Variante: Ausdruck per Post"),
       ("frage", "Fall · Die Frage")], [
    linienzug([(60, BODEN), (1860, BODEN)], "h1", breite=7, farbe=INK),
    TISCH2,
    ficon("fluent-emoji-flat", "desktop-computer", 1260, TT2, 170, "h1"),
    pl("PDF: Note 1,8", 1260, TT2 - 215, "h1", fill=WEISS, size=30, anker="m"),
    *st("HA", HX, [("redet", "h1"), ("ruhig", "variante"), ("denkt", "frage"), ("ernst", "frage2")], rede=("redet",),
        unten=BODEN, hoehe=FH, erst="cut"),
    blase("sprech", 600, 175, "h1", HX - 330, 240, inhalt=["1,8, sehr gut. Sie sind", "in der nächsten Runde."], textsize=34,
          figur=("HA_redet", HX, BODEN, FH), bis="variante"),
    linienzug([(930, 400), (930, BODEN - 4)], "variante", breite=4, farbe=GRAU),
    pl("Variante", 70, 40, "variante", fill=GELB, size=36),
    *st("JA", 280, [("eifrig_r", "variante"), ("ruhig_r", "frage")], unten=BODEN, hoehe=FH),
    szene(ficon("fluent-emoji-flat", "printer", 620, BODEN - 4, 170, beim("variante", "druckt")), "167drucker_1", 1.0),
    bewegt(ficon("fluent-emoji-flat", "envelope", 1060, TT2 - 6, 100, beim("variante", "Post")), beim("variante", "Post"),
           beim("variante", "Kopie"), -440, 0),
    pl("Kopie", 1060, TT2 - 120, beim("variante", "Kopie"), fill=WEISS, size=30, anker="m"),
    pl("Urkundenfälschung, § 267 StGB?", 1000, 50, "frage", fill=PINK, size=36, anker="m"),
    pl("Oder § 269 StGB?", 1000, 140, "frage2", fill=GELB, size=34, anker="m"),
])

# B Sachverhalt --------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    glyphen("Janosch ist 20 und bewirbt sich um eine Stelle als Sachbearbeiter. In seinem Abiturzeugnis steht die Note "
            "2,8. Er scannt das Zeugnis ein und ändert am Rechner die Note in 1,8. Er speichert die Datei als PDF und "
            "schickt sie per E-Mail an Frau Hagemann aus der Personalabteilung."),
    glyphen("Variante: Janosch druckt die bearbeitete Datei aus und schickt den Ausdruck per Post, als Kopie seines "
            "Zeugnisses."),
], "Hat sich Janosch nach § 267 StGB oder nach § 269 StGB strafbar gemacht?")

# C Einfache Fotokopie (Urkundenbegriff nur als Verweis) ---------------------------------------------------------------------
folie([("begriff", "Voraussetzung › Urkundenbegriff"), ("kopie", "Fotokopie › Grundsatz"),
       ("grund", "Fotokopie › keine Urkunde")], rechts_frei([
    *tafel("begriff", "Die einfache Fotokopie"),
    z("Urkunde: verkörperte Gedankenerklärung, zum Beweis", 110, 175, "begriff", "Bold", 31),
    z("geeignet und bestimmt, Aussteller erkennbar", 110, 218, beim("begriff", "geeignet"), "Bold", 31),
    fund("Urkundenbegriff: Folge zur gefälschten Entschuldigung", 150, 264, "begriff"),
    karte(110, 330, 1040, 190, beim("kopie", "Nach"), fill=HELL, rund=18, schatten=6, rand=4),
    z("Bloße Fotokopie, die nach außen als", 140, 350, beim("kopie", "Nach"), "ExtraBold", 33),
    z("Reproduktion erscheint: keine Urkunde", 140, 400, beim("kopie", "Reproduktion"), "ExtraBold", 33),
    fund("st. Rspr.; BGHSt 24, 140, 141 f.; BGH, Beschl. v. 9.3.2011 – 2 StR 428/10, Rn. 11", 140, 460,
         beim("kopie", "Reproduktion")),
    *zeile_ok("Beweiseignung fehlt", 110, 560, "grund", ja=False, size=32),
    *zeile_ok("kein erkennbarer Aussteller", 110, 615, beim("grund", "erkennbarer"), ja=False, size=32),
    z("Sie gibt das Original nur bildlich wieder,", 110, 690, "grund2", "Bold", 32),
    z("verkörpert keine eigene Erklärung", 110, 735, beim("grund2", "verkörpert"), "Bold", 32),
    fund("BGH, Beschl. v. 27.1.2010 – 5 StR 488/09, Rn. 9, 10", 150, 782, beim("grund2", "verkörpert")),
    *st("JA", X1, [("ruhig", "begriff"), ("denkt", "kopie"), ("ernst", "grund2")]),
    *st("HA", X2, [("ruhig", "begriff"), ("denkt", "grund")], d=0.2),
    *wechsel([("Urkunde?", "begriff", WEISS), ("Fotokopie?", "kopie", GELB), ("keine Urkunde", "grund", ROTHELL),
              ("nur ein Abbild", "grund2", WEISS)], MB, 160),
    *icons([("fluent-emoji-flat", "page-facing-up", "begriff", None), ("fluent-emoji-flat", "printer", "kopie", None),
            ("tabler", "copy", "grund2", WEISS)], MB, 390, 110),
]))

# D Streitstand: Ist die Kopie eine Urkunde? ---------------------------------------------------------------------------------
folie([("streit", "Streitstand › Fotokopie als Urkunde?"), ("mm", "Streitstand › Gegenansicht: grundsätzlich Urkunde"),
       ("hm", "Streitstand › Rechtsprechung: keine Urkunde")], rechts_frei([
    *tafel("streit", "Streitstand: Kopie als Urkunde?"),
    z("Ganz unbestritten ist das nicht.", 110, 180, "streit", size=33),
    karte(110, 250, 1040, 200, "mm", fill=LILAHELL, rund=18, schatten=6, rand=4),
    z("Gegenansicht in der Literatur:", 140, 270, "mm", "ExtraBold", 33),
    z("Kopien beweisgeeignet, grundsätzlich Urkunden", 140, 322, beim("mm", "beweisgeeignet"), "Bold", 32),
    fund("z. B. Freund, Heghmanns (nach Nestler, ZJS 2010, 608, Fn. 11, 15)", 140, 385, beim("mm", "beweisgeeignet")),
    karte(110, 490, 1040, 260, "hm", fill=GRUENHELL, rund=18, schatten=6, rand=4),
    z("Rechtsprechung und große Teile der Lehre:", 140, 510, "hm", "ExtraBold", 33),
    z("keine Urkunde – für die bloße Kopie steht kein", 140, 562, beim("hm", "Für"), "Bold", 32),
    z("erkennbarer Aussteller mit seiner Garantie ein", 140, 607, beim("hm", "erkennbarer"), "Bold", 32),
    fund("BGH, Beschl. v. 27.1.2010 – 5 StR 488/09, Rn. 10", 140, 675, beim("hm", "erkennbarer")),
    *st("JA", X1, [("ruhig", "streit"), ("eifrig", "mm"), ("still", "hm")]),
    *st("HA", X2, [("denkt", "streit"), ("ruhig", "mm"), ("froh", "hm")], d=0.2),
    *wechsel([("Streit", "streit", GELB), ("Gegenansicht", "mm", LILA), ("Rechtsprechung", "hm", GRUEN)], MB, 160),
    *icons([("fluent-emoji-flat", "balance-scale", "streit", None), ("fluent-emoji-flat", "books", "mm", None),
            ("tabler", "circle-check", "hm", GRUEN)], MB, 390, 110),
]))

# E Zwei Ausnahmen und eine Grenze ---------------------------------------------------------------------------------------
folie([("aus", "Fotokopie › Ausnahmen"), ("aus1", "Ausnahme 1 › Kopie erscheint als Original"),
       ("aus2", "Ausnahme 2 › Kopie eines gefälschten Originals"), ("beglaub", "Ausnahme 2 › beglaubigte Kopie"),
       ("collage", "Grenze › Collage")], rechts_frei([
    *tafel("aus", "Zwei Ausnahmen und eine Grenze"),
    z("1. Die Kopie erscheint als Original:", 110, 172, "aus1", "ExtraBold", 32),
    z("Verwechslung möglich: Urkunde, nach Manipulation unecht", 150, 216, beim("aus1", "Ist"), size=30),
    fund("BGH, Beschl. v. 27.1.2010 – 5 StR 488/09, Rn. 8", 150, 260, beim("aus1", "Ist")),
    z("2. Es gibt ein gefälschtes Original:", 110, 318, "aus2", "ExtraBold", 32),
    z("Kopie vorlegen, auch beglaubigt: Gebrauchen des Originals", 150, 362, beim("aus2", "Wer"), size=30),
    fund("BGHSt 24, 140, 142; BGH, Beschl. v. 2.5.2001 – 2 StR 149/01, Rn. 8", 150, 406, beim("aus2", "Rechtsprechung")),
    z("Beglaubigung bestätigt nur: Kopie stimmt mit der Vorlage", 150, 456, "beglaub", size=30),
    z("überein – nicht, dass ihr Inhalt stimmt", 150, 498, beim("beglaub", "nicht"), size=30),
    fund("BGH 2 StR 149/01, Rn. 7", 150, 542, beim("beglaub", "nicht")),
    karte(110, 600, 1040, 230, "collage", fill=ROTHELL, rund=18, schatten=6, rand=4),
    z("Grenze: die Collage", 140, 618, "collage", "ExtraBold", 33),
    z("Teile echter Urkunden lose zusammengelegt und kopiert:", 140, 668, beim("collage", "Legt"), size=30),
    z("kein gefälschtes Original, von dem die Kopie", 140, 710, beim("collage", "entsteht"), "Bold", 30),
    z("Gebrauch machen könnte", 140, 752, beim("collage", "Gebrauch"), "Bold", 30),
    fund("BGH, Beschl. v. 26.2.2003 – 2 StR 411/02, Rn. 6", 140, 794, beim("collage", "Gebrauch")),
    *st("JA", X1, [("ruhig", "aus"), ("denkt", "aus1"), ("sorge", "aus2"), ("ruhig", "collage")]),
    *st("HA", X2, [("ruhig", "aus"), ("ernst", "aus2"), ("denkt", "beglaub"), ("ruhig", "collage")], d=0.2),
    *wechsel([("Ausnahmen", "aus", WEISS), ("wie ein Original", "aus1", GELB), ("gefälschtes Original", "aus2", ROTHELL),
              ("Examenszeugnis", "examen", WEISS), ("beglaubigt", "beglaub", LILAHELL), ("Collage", "collage", WEISS)],
             MB, 160),
    *icons([("fluent-emoji-flat", "page-with-curl", "aus1", None), ("fluent-emoji-flat", "page-facing-up", "aus2", None),
            ("fluent-emoji-flat", "graduation-cap", "examen", None), ("tabler", "certificate", "beglaub", WEISS),
            ("fluent-emoji-flat", "scissors", "collage", None)], MB, 390, 110),
]))

# F Datei: § 269 Abs. 1 im Wortlaut, hypothetischer Urkundenvergleich ----------------------------------------------------
W269 = [[("„Wer zur Täuschung im Rechtsverkehr ", 0), ("beweiserhebliche Daten", "a"), (" so", 0)],
        [("speichert oder verändert,", "b"), (" daß bei ihrer Wahrnehmung eine", 0)],
        [("unechte oder verfälschte Urkunde vorliegen würde,", "c"), (" oder derart", 0)],
        [("gespeicherte oder veränderte Daten ", 0), ("gebraucht,", "d"), (" wird mit Freiheitsstrafe", 0)],
        [("bis zu fünf Jahren oder mit Geldstrafe bestraft.“", 0)]]
folie([("datei", "Scan und PDF › Datei: nicht § 267"), ("p269", "§ 269 Abs. 1 StGB › Wortlaut"),
       ("hyp", "§ 269 › hypothetischer Urkundenvergleich")], rechts_frei([
    *tafel("datei", "Datei statt Papier: § 269 StGB"),
    z("PDF-Datei: nicht auf einer Sache verkörpert", 110, 172, beim("datei", "Eine"), "Bold", 32),
    z("Dateien und E-Mails: nicht § 267, sondern § 269", 110, 216, beim("datei", "Für"), "Bold", 32),
    fund("BGH, Beschl. v. 23.5.2017 – 4 StR 141/17, Rn. 9", 150, 262, beim("datei", "Für")),
    *wortlaut(110, 320, 1040, 222, "p269", W269, 29, {"a": beim("w269", "beweiserhebliche"), "b": beim("w269", "speichert"),
                                                      "c": beim("w269", "unechte"), "d": beim("w269", "gebraucht")},
              "§ 269 Abs. 1 StGB"),
    fb(110, 620, 1040, 150, GELB, "hyp", [("Hypothetisch: die Daten als verkörperte", "ExtraBold", 33, INK),
                                          ("Erklärung gedacht – unechte Urkunde?", "ExtraBold", 33, INK)]),
    fund("BGH, Beschl. v. 14.3.2024 – 2 StR 192/23, Rn. 17", 150, 785, "hyp"),
    *st("JA", X1, [("ruhig", "datei"), ("denkt", "p269"), ("ernst", "hyp")]),
    *st("HA", X2, [("ruhig", "datei"), ("ernst", "p269"), ("denkt", "hyp")], d=0.2),
    *wechsel([("Datei", "datei", WEISS), ("§ 269 StGB", "p269", GELB), ("als Papier gedacht?", "hyp", WEISS)], MB, 160),
    *icons([("tabler", "file-type-pdf", "datei", None), ("fluent-emoji-flat", "balance-scale", "p269", None),
            ("fluent-emoji-flat", "page-facing-up", "hyp", None)], MB, 390, 110),
]))

# G1 Scan oder digitales Original? -----------------------------------------------------------------------------------------
folie([("bgh", "§ 269 › Scan oder digitales Original?"), ("scanfall", "§ 269 › Scan eines Papierdokuments: (−)"),
       ("digorig", "§ 269 › digitales Original: in Betracht")], rechts_frei([
    *tafel("bgh", "Scan oder digitales Original?"),
    z("Der BGH unterscheidet:", 110, 175, "bgh", size=33),
    karte(110, 240, 1040, 270, "scanfall", fill=ROTHELL, rund=18, schatten=6, rand=4),
    z("Papierdokument eingescannt und verändert:", 140, 260, "scanfall", "ExtraBold", 32),
    z("Urkundenqualität schon durch den Scan verloren", 140, 310, beim("scanfall", "verliert"), "Bold", 31),
    z("Bild: Datum, aber keine Datenurkunde – § 269 (−)", 140, 355, beim("scanfall", "Das"), "Bold", 31),
    fund("BGH, Beschl. v. 14.3.2024 – 2 StR 192/23, Rn. 27", 140, 420, beim("scanfall", "Das")),
    karte(110, 550, 1040, 270, "digorig", fill=GRUENHELL, rund=18, schatten=6, rand=4),
    z("Von Haus aus digital, z. B. Online-", 140, 570, "digorig", "ExtraBold", 32),
    z("Überweisungsbestätigung: verändert oder", 140, 620, beim("digorig", "Online"), "Bold", 31),
    z("komplett gefälscht – § 269 in Betracht", 140, 665, beim("digorig", "Dann"), "Bold", 31),
    fund("BGH 2 StR 192/23, Rn. 28", 140, 730, beim("digorig", "Dann")),
    *st("JA", X1, [("ruhig", "bgh"), ("sorge", "digorig")]),
    *st("HA", X2, [("ruhig", "bgh"), ("ernst", "scanfall"), ("denkt", "digorig")], d=0.2),
    *wechsel([("Scan?", "bgh", WEISS), ("Scan: (−)", "scanfall", ROTHELL), ("digital: (+)?", "digorig", GRUEN)], MB, 160),
    *icons([("tabler", "scan", "bgh", None), ("tabler", "photo-scan", "scanfall", None),
            ("fluent-emoji-flat", "mobile-phone", "digorig", None)], MB, 390, 110),
]))

# G2 PDF-Zeugnis: OLG Celle, Gegenansicht, § 270 -----------------------------------------------------------------------------
W270 = [[("„Der Täuschung im Rechtsverkehr steht die ", 0), ("fälschliche", "a")],
        [("Beeinflussung einer Datenverarbeitung", "a"), (" im Rechtsverkehr gleich.“", 0)]]
folie([("olg", "Streit › PDF-Zeugnis: nur Reproduktion"), ("gegen", "Streit › Gegenansicht: Datenurkunde"),
       ("p270", "§ 270 StGB › Datenverarbeitung")], rechts_frei([
    *tafel("olg", "Streit: Zeugnis als PDF-Anhang"),
    karte(110, 170, 1040, 235, "olg", fill=GRUENHELL, rund=18, schatten=6, rand=4),
    z("OLG Celle:", 140, 188, "olg", "ExtraBold", 33),
    z("Zeugnisse werden auf Papier ausgegeben – das PDF", 140, 238, beim("olg", "Zeugnisse"), "Bold", 31),
    z("erscheint erkennbar nur als Reproduktion", 140, 282, beim("olg", "erscheint"), "Bold", 31),
    fund("OLG Celle, Urt. v. 15.12.2023 – 1 ORs 2/23 (amtl. Leitsatz)", 140, 340, beim("olg", "erscheint")),
    karte(110, 440, 1040, 175, "gegen", fill=LILAHELL, rund=18, schatten=6, rand=4),
    z("Gegenansicht: auch PDF-Anhänge", 140, 458, "gegen", "ExtraBold", 33),
    z("als Datenurkunden erfassen", 140, 506, beim("gegen", "Datenurkunden"), "Bold", 31),
    fund("z. B. Krell (zitiert bei OLG Celle aaO)", 140, 556, beim("gegen", "Datenurkunden")),
    z("Täuscht der Täter nur ein Programm?", 110, 650, "p270", "Bold", 31),
    *wortlaut(110, 695, 1040, 118, beim("p270", "Der"), W270, 29, {"a": beim("p270", "fälschliche")}, "§ 270 StGB"),
    *st("JA", X1, [("ruhig", "olg"), ("still", "gegen"), ("denkt", "p270")]),
    *st("HA", X2, [("froh", "olg"), ("denkt", "gegen"), ("ruhig", "p270")], d=0.2),
    *wechsel([("PDF = Reproduktion", "olg", GRUEN), ("Gegenansicht", "gegen", LILA), ("nur ein Programm", "p270", WEISS)],
             MB, 160),
    *icons([("fluent-emoji-flat", "e-mail", "olg", None), ("fluent-emoji-flat", "books", "gegen", None),
            ("fluent-emoji-flat", "robot", "p270", None)], MB, 390, 110),
]))

# H1 Lösung: das PDF per E-Mail ----------------------------------------------------------------------------------------------
folie([("loes", "Lösung › PDF per E-Mail"), ("l1", "Lösung › PDF: § 267 (−)"), ("l2", "Lösung › PDF: § 269 (−)"),
       ("l3", "Lösung › anders bei digitalem Original")], rechts_frei([
    *tafel("loes", "Lösung: das PDF per E-Mail"),
    *zeugnis(760, 160, 380, "loes", "1,8", "loes", size=28, gross=56, kopie=True),
    *zeile_ok("§ 267: keine verkörperte Erklärung", 110, 200, "l1", ja=False, size=32, rechts=740),
    *zeile_ok("§ 269: erkennbar nur der Scan eines", 110, 400, "l2", ja=False, size=32),
    z("Papierzeugnisses, also eine Kopie", 175, 448, beim("l2", "Papierzeugnisses"), size=32),
    z("ganz überwiegende Meinung: § 269 (−)", 175, 496, beim("l2", "Mit"), "Bold", 32),
    fund("OLG Celle, Urt. v. 15.12.2023 – 1 ORs 2/23; BGH 2 StR 192/23, Rn. 27", 175, 545, beim("l2", "Mit")),
    karte(110, 620, 1040, 130, "l3", fill=LILAHELL, rund=18, schatten=6, rand=4),
    z("Anders möglich: Zeugnis als", 140, 638, "l3", "ExtraBold", 32),
    z("digitales Original ausgegeben", 140, 686, beim("l3", "digitales"), "ExtraBold", 32),
    *st("JA", X1, [("ruhig", "loes"), ("ernst", "l1"), ("froh", "l2"), ("denkt", "l3")]),
    *st("HA", X2, [("denkt", "loes"), ("ernst", "l2"), ("ruhig", "l3")], d=0.2),
    *wechsel([("Lösung", "loes", WEISS), ("§ 267 (−)", "l1", ROTHELL), ("§ 269 (−)", "l2", ROTHELL),
              ("digitales Original?", "l3", LILAHELL)], MB, 160),
    *icons([("tabler", "file-type-pdf", "loes", None), ("tabler", "x", "l1", None), ("tabler", "photo-scan", "l2", None),
            ("fluent-emoji-flat", "laptop", "l3", None)], MB, 390, 110),
]))

# H2 Lösung: der Ausdruck als Kopie; Ausblick Betrug -----------------------------------------------------------------------
folie([("l4", "Lösung › Variante: Ausdruck als Kopie"), ("l5", "Lösung › kein gefälschtes Original"),
       ("betrug", "Ausblick › Betrug, § 263 StGB")], rechts_frei([
    *tafel("l4", "Lösung: der Ausdruck als Kopie"),
    z("Als Kopie verschickt: erscheint als Reproduktion", 110, 175, beim("l4", "Als"), "Bold", 32),
    *zeile_ok("Urkunde nur, wenn er wie ein Original aussähe,", 110, 240, beim("l4", "Eine"), ja=False, size=31),
    z("mit den typischen Echtheitsmerkmalen", 175, 286, beim("l4", "typischen"), size=31),
    fund("BGH, Beschl. v. 27.1.2010 – 5 StR 488/09, Rn. 8, 9", 175, 333, beim("l4", "typischen")),
    *zeile_ok("In beiden Varianten kein gefälschtes Papierzeugnis,", 110, 400, "l5", ja=False, size=31),
    z("das er über die Kopie gebrauchen könnte", 175, 446, beim("l5", "das"), size=31),
    fund("BGH, Beschl. v. 9.3.2011 – 2 StR 428/10, Rn. 12", 175, 493, beim("l5", "das")),
    karte(110, 570, 1040, 240, "betrug", fill=HELL, rund=18, schatten=6, rand=4),
    z("Ausblick: Betrug, § 263 StGB", 140, 588, "betrug", "ExtraBold", 33),
    z("Wird er eingestellt: Anstellungsbetrug in Betracht", 140, 638, beim("betrug", "Wird"), "Bold", 31),
    z("Schaden nur, wenn die Arbeitsleistung weniger", 140, 683, beim("betrug", "Ein"), "Bold", 31),
    z("wert ist als das Gehalt", 140, 726, beim("betrug", "wert"), "Bold", 31),
    fund("BGH, Beschl. v. 21.8.2019 – 3 StR 221/18, Rn. 30", 140, 770, beim("betrug", "wert")),
    *st("JA", X1, [("ruhig", "l4"), ("still", "l5"), ("sorge", "betrug")]),
    *st("HA", X2, [("ruhig", "l4"), ("denkt", "l5"), ("ernst", "betrug")], d=0.2),
    *wechsel([("Ausdruck: Kopie", "l4", WEISS), ("kein Original", "l5", ROTHELL), ("Betrug?", "betrug", GELB)], MB, 160),
    *icons([("fluent-emoji-flat", "printer", "l4", None), ("fluent-emoji-flat", "envelope", "l5", None),
            ("fluent-emoji-flat", "briefcase", "betrug", None)], MB, 390, 110),
]))

# I Merktabelle: Original, Kopie, Scan -------------------------------------------------------------------------------------
TA, TB = 330, 760
folie([("tab", "Merktabelle"), ("t1", "Merktabelle › Original"), ("t2", "Merktabelle › Kopie"),
       ("t3", "Merktabelle › Scan und PDF")], [
    karte(60, 50, 1800, 900, "tab"),
    titel("Merktabelle: Original, Kopie, Scan", 110, 90, "tab", 52),
    ficon("fluent-emoji-flat", "page-facing-up", 200, 300, 90, "t1"),
    z("Original auf Papier", TA, 230, "t1", "Bold", 38, rechts=1820),
    z("Urkunde: § 267 StGB", TB, 232, beim("t1", "Urkunde"), size=36, rechts=1820),
    linienzug([(110, 345), (1810, 345)], "t2", breite=3, farbe=GRAU),
    ficon("fluent-emoji-flat", "printer", 200, 500, 100, "t2"),
    z("Kopie", TA, 400, "t2", "Bold", 38, rechts=1820),
    z("keine Urkunde – außer sie erscheint als Original", TB, 402, beim("t2", "keine"), size=36, rechts=1820),
    z("Kopie eines gefälschten Originals:", TB, 462, "t2b", size=36, rechts=1820),
    z("Gebrauchen des Originals", TB, 512, beim("t2b", "gebraucht"), "Bold", 36, rechts=1820),
    linienzug([(110, 590), (1810, 590)], "t3", breite=3, farbe=GRAU),
    ficon("tabler", "file-type-pdf", 200, 750, 100, "t3"),
    z("Scan / PDF", TA, 645, "t3", "Bold", 38, rechts=1820),
    z("Datei: § 269 StGB nur, wenn sie als", TB, 647, beim("t3", "Paragraf"), size=36, rechts=1820),
    z("Original auftritt – nicht als bloße Wiedergabe", TB, 697, beim("t3", "Original"), size=36, rechts=1820),
])

# J Klausurtipp (Lexi) -----------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · Was kommt beim Empfänger an?"), ("tipp3", "Klausurtipp · Gefälschtes Original dahinter?")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Frag nicht nur, was gefälscht wurde,", 200, 200, beim("tipp", "Frag"), "Bold", 37),
    z("sondern was beim Empfänger ankommt.", 200, 255, beim("tipp", "sondern"), "Bold", 37),
    z("Ein Original oder erkennbar", 200, 360, "tipp2", "ExtraBold", 36),
    z("eine Wiedergabe?", 200, 412, beim("tipp2", "eine"), "ExtraBold", 36),
    z("Bei jeder Kopie prüfen: Steht", 200, 520, "tipp3", size=35),
    z("dahinter ein gefälschtes Original?", 200, 570, beim("tipp3", "gefälschtes"), "Bold", 35),
    *redet("LX_warnt", LXX, BR, FR + 60, "tipp", "merke"),
    namensschild("Lexi", LXX, BR, "tipp", GELB, d=0.2),
])

# K Merksatz (Lexi) --------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Eine Kopie ist ", 0), ("keine Urkunde", "a"), (",", 0)],
                 [("solange sie ", 0), ("wie eine Kopie aussieht", "b"), (".", 0)]], 750, 320, 46, "merke",
                {"a": beim("merke", "keine"), "b": beim("merke", "wie")}),
    *markertext([[("Und § 269 schützt ", 0), ("digitale Originale", "c"), (",", 0)],
                 [("nicht ihre ", 0), ("Abbilder", "d"), (".", 0)]], 750, 560, 46, "m2",
                {"c": beim("m2", "digitale"), "d": beim("m2", "Abbilder")}),
    *redet("LX_erklaert", 1680, 960, 690, "merke", lexi_bis_ende("merke")),
    namensschild("Lexi", 1680, 960, "merke", GELB, d=0.2),
])
