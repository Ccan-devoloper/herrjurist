"""Folge 134 · Beleidigung, üble Nachrede, Verleumdung: §§ 185–187 StGB erklärt – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A Chatgruppe „Nachbarn Ahornweg“ (Henner, Hannelore, Dörte; nur Chat-Blasen und Handys,
keine Kinder, keine Gewalt), B Sachverhalt, C1 Werturteil oder Tatsachenbehauptung, C2 Einordnung der beiden Nachrichten,
D1 § 185 (Wortlautkarte), D2 Subsumtion Hannelore, E Rechtswidrigkeit: § 193 und Abwägung (Hannelore spricht),
F1 § 186 (Wortlautkarte auszugsweise), F2 nicht erweislich wahr, F3 § 193 bei Dörte (Dörte spricht), G1 Variante § 187
(Wortlautkarte auszugsweise, Denkblase), G2 Qualifikation (offen) und Strafantrag § 194, H Abgrenzungstabelle mit Ergebnis,
I Klausurtipp (Lexi), J Klausurschema, K Merksatz (Lexi).
Geräusch nur bei sichtbarer Handlung: Handy vibriert, als eine Nachricht im Chat erscheint (szene_134handy_1, Freesound CC0).
Hilfsfunktionen (z, pl, tafel, wortlaut, fb, redet mit hörbarem Wortende …) wie in Folge 131, Kopie im eigenen Ordner."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont

bausteine.FIGORDNER = "op_134/"
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
NULL = "fall"                     # Szene A steht ab 0,0 s (render_134 setzt alle Elemente bis zur Marke „fall“ auf 0,0 s)

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


# --- Eigene Hilfsfunktion (wie Folge 131): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ------------------
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
FARBE = {"HE": BLAU, "HA": GRUEN, "DO": LILA}
NAME = {"HE": "Henner", "HA": "Hannelore", "DO": "Dörte"}


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


def chat(absender, text, x, y, w, cue, fill=WEISS, bis=None, size=31, zeilen=None, rechts=None, anim="pop"):
    """Chat-Nachricht als abgerundete Karte (keine Marke, kein Logo): Absender fett und grün, darunter der Text."""
    zeilen = zeilen or [text]
    h = 58 + int(size * 1.3) * len(zeilen) + 8
    k = karte(x, y, w, h, cue, fill=fill, rund=22, schatten=5, rand=4, anim=anim)
    k.bis = bis
    els = [k, z(absender, x + 24, y + 12, cue, "ExtraBold", 26, farbe=(40, 150, 85), rechts=x + w - 10, bis=bis)]
    for i, t in enumerate(zeilen):
        els.append(z(t, x + 24, y + 48 + i * int(size * 1.3), cue, "Bold", size, rechts=rechts or x + w - 14, bis=bis))
    return els


def mit_ton(els):
    """Die neue Chat-Nachricht erscheint mit dem Vibrieren eines Handys (Handlungsgeräusch, Freesound CC0)."""
    szene(els[0], "134handy_1")
    return els


def tabelle_zeile(werte, xs, y, cue, size=30, stil="Regular", bis=None):
    """Tabellenzeile: werte[i] (Text oder Liste von Zeilen) in Spalte xs[i]."""
    els = []
    for v, x in zip(werte, xs):
        for j, t in enumerate(v if isinstance(v, list) else [v]):
            els.append(z(t, x, y + j * int(size * 1.25), cue, stil, size, rechts=1820, bis=bis))
    return els


# ======================================================================================================================
# A Fall: Chatgruppe „Nachbarn Ahornweg“
# ======================================================================================================================
BODEN, FH = 880, 520
HAX, DOX, HEX = 230, 480, 1600
CX0, CW = 650, 640                       # Chatfenster (Tisch-/Raumbezug: Handys der drei Nachbarn)
folie([(NULL, "Fall · Die Chatgruppe"), ("party", "Fall · Die Gartenparty"), ("idiot", "Fall · Hannelore schreibt"),
       ("kinder", "Fall · Dörte legt nach"), ("h1", "Fall · Henner stellt Strafantrag"), ("frage", "Fall · Die Frage"),
       ("var", "Fall · Die Variante")], [
    linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK),
    karte(CX0, 150, CW, 640, NULL, fill=WEISS, rund=30, schatten=8, rand=5),
    karte(CX0, 150, CW, 96, NULL, fill=CHATGRUEN, rund=30, schatten=0, rand=5),
    z("Nachbarn Ahornweg", CX0 + 95, 160, NULL, "ExtraBold", 34, rechts=CX0 + CW - 10),
    z("63 Mitglieder", CX0 + 95, 203, beim("fall", "dreiundsechzig"), "Regular", 27, farbe=TEXT, rechts=CX0 + CW - 10),
    ficon("tabler", "messages", CX0 + 50, 226, 58, NULL, fuell=WEISS),
    pl("Thema: die laute Gartenparty von Henner", 960, 60, "party", fill=WEISS, size=30, anker="m", bis="frage"),
    ficon("fluent-emoji-flat", "party-popper", 610, 118, 62, beim("party", "Gartenparty"), bis="frage"),
    *mit_ton(chat("Hannelore", "Henner ist ein Idiot.", CX0 + 30, 280, 470, "idiot")),
    *mit_ton(chat("Dörte", "Henner schlägt seine Kinder.", CX0 + 30, 425, 520, "kinder")),
    pl("Belege: keine", CX0 + 40, 575, "beleg", fill=ROTHELL, size=28),
    pl("Ob es stimmt: nicht zu klären", CX0 + 40, 650, beim("beleg", "Ob"), fill=WEISS, size=28),
    # Figuren: Hannelore und Dörte links (blicken zum Chat), Henner rechts (blickt zum Chat)
    *stufen("HA", HAX, [("entschlossen_r", "idiot"), ("denkt_r", "frage")], unten=BODEN, hoehe=FH, schild_cue="idiot"),
    ficon("fluent-emoji-flat", "mobile-phone", HAX + 105, 640, 52, "idiot"),
    *stufen("DO", DOX, [("ernst_r", "kinder"), ("denkt_r", "beleg"), ("still_r", "var")], unten=BODEN, hoehe=FH),
    ficon("fluent-emoji-flat", "mobile-phone", DOX + 10, 530, 52, "kinder"),
    *stufen("HE", HEX, [("ruhig", "party"), ("staunt", "idiot"), ("sorge", "kinder"), ("redet", "h1"), ("ernst", "frage")],
            rede=("redet",), unten=BODEN, hoehe=FH),
    ficon("fluent-emoji-flat", "mobile-phone", HEX - 100, 650, 52, beim("party", "Henner")),
    blase("sprech", 580, 175, "h1", HEX - 40, 205, inhalt=["Das ist eine Lüge!", "Ich stelle Strafantrag."], textsize=34,
          figur=("HE_redet", HEX, BODEN, FH), bis="frage"),
    pl("Wer hat sich strafbar gemacht?", 960, 60, "frage", fill=PINK, size=36, anker="m", anim="cut"),
    pl("Variante: Dörte weiß, dass es nicht stimmt", CX0 + CW // 2, 812, "var", fill=LILAHELL, size=28, anker="m"),
])

# B Sachverhalt ----------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    glyphen("In der Chatgruppe „Nachbarn Ahornweg“ mit 63 Mitgliedern geht es um die laute Gartenparty von Henner am "
            "Wochenende. Hannelore schreibt: „Henner ist ein Idiot.“ Dörte legt nach: „Henner schlägt seine Kinder.“ "
            "Belege hat sie keine; ob es stimmt, lässt sich nicht klären. Henner stellt Strafantrag."),
    glyphen("Variante: Dörte weiß, dass ihre Behauptung nicht stimmt."),
], "Wer hat sich strafbar gemacht?")

# C1 Werturteil oder Tatsachenbehauptung --------------------------------------------------------------------------------------
P1 = "1. Werturteil oder Tatsache?"
folie([("schritt1", P1), ("wert", f"{P1} › Werturteil"), ("tats", f"{P1} › Tatsachenbehauptung"),
       ("beweis", f"{P1} › Kriterium: Beweisbarkeit"), ("kontext", f"{P1} › Sinn: Wortlaut, Kontext, Umstände")], rechts_frei([
    *tafel("schritt1", "1. Werturteil oder Tatsachenbehauptung?", size=46),
    karte(110, 180, 505, 250, beim("schritt1", "Werturteil"), fill=GRUENHELL, rund=18, schatten=6, rand=4),
    z("Werturteil", 135, 195, beim("schritt1", "Werturteil"), "ExtraBold", 34, rechts=600),
    z("Stellungnahme und", 135, 250, beim("wert", "Stellungnahme"), "Bold", 31, rechts=600),
    z("Dafürhalten", 135, 292, beim("wert", "Dafürhalten"), "Bold", 31, rechts=600),
    z("nicht wahr oder unwahr", 135, 350, beim("wert", "Es"), size=31, rechts=600),
    karte(645, 180, 505, 250, beim("schritt1", "Tatsachenbehauptung"), fill=BLAUHELL, rund=18, schatten=6, rand=4),
    z("Tatsachenbehauptung", 670, 195, beim("schritt1", "Tatsachenbehauptung"), "ExtraBold", 34, rechts=1135),
    z("Beziehung zur", 670, 250, beim("tats", "Beziehung"), "Bold", 31, rechts=1135),
    z("Wirklichkeit", 670, 292, beim("tats", "Wirklichkeit"), "Bold", 31, rechts=1135),
    z("lässt sich überprüfen", 670, 350, beim("tats", "Sie"), size=31, rechts=1135),
    fund("BVerfGE 90, 241 (247), Rn. 26 f.", 150, 445, beim("tats", "Sie")),
    fb(110, 500, 1040, 86, GELB, "beweis", [("Kriterium: Beweisbarkeit", "ExtraBold", 36, INK)]),
    z("Sinn für ein unvoreingenommenes und verständiges Publikum:", 110, 625, "kontext", "Bold", 31),
    z("Wortlaut, Kontext und Begleitumstände", 110, 672, beim("kontext", "Wortlaut"), "Bold", 31),
    fund("BVerfGE 93, 266 (295), Rn. 120", 150, 722, beim("kontext", "Wortlaut")),
    *stufen("HA", X1, [("ruhig", "schritt1"), ("denkt", "wert")]),
    *stufen("DO", X2, [("ruhig", "schritt1"), ("denkt", "tats")], d=0.2),
    *wechsel([("Werturteil oder Tatsache?", "schritt1", None), ("Stellungnahme", "wert", GRUEN), ("Wirklichkeit", "tats", BLAU),
              ("beweisbar?", "beweis", GELB), ("Kontext", "kontext", WEISS)], MB, 160),
    *icons([("fluent-emoji-flat", "balance-scale", "schritt1", None), ("fluent-emoji-flat", "thought-balloon", "wert", None),
            ("fluent-emoji-flat", "magnifying-glass-tilted-left", "tats", None), ("tabler", "microscope", "beweis", GELB),
            ("fluent-emoji-flat", "speech-balloon", "kontext", None)], MB, 390, 120),
]))

# C2 Einordnung der beiden Nachrichten ------------------------------------------------------------------------------------------
P1b = "1. Einordnung"
folie([("sub1", f"{P1b} › „Idiot“: Werturteil"), ("sub2", f"{P1b} › Kinder schlagen: Tatsachenbehauptung")], rechts_frei([
    *tafel("sub1", "Unsere beiden Nachrichten"),
    *chat("Hannelore", "Henner ist ein Idiot.", 110, 185, 560, "sub1"),
    z("eine Bewertung, nicht beweisbar", 150, 335, beim("sub1", "beweisen"), size=32),
    pl("Werturteil", 760, 210, beim("sub1", "Werturteil"), fill=GRUEN, size=34),
    *chat("Dörte", "Henner schlägt seine Kinder.", 110, 440, 620, "sub2"),
    z("ein Vorgang, den man beweisen könnte", 150, 590, beim("sub2", "Vorgang"), size=32),
    pl("Tatsachenbehauptung", 760, 465, beim("sub2", "Tatsachenbehauptung"), fill=BLAU, size=32),
    *stufen("HA", X1, [("ernst", "sub1"), ("still", "sub2")]),
    *stufen("DO", X2, [("ruhig", "sub1"), ("ernst", "sub2")], d=0.2),
    *wechsel([("„Idiot“", "sub1", GRUEN), ("Kinder schlagen?", "sub2", BLAU)], MB, 160),
    *icons([("fluent-emoji-flat", "thought-balloon", "sub1", None), ("fluent-emoji-flat", "magnifying-glass-tilted-left", "sub2", None)],
           MB, 390, 120),
]))

# D1 Beleidigung, § 185 (Wortlautkarte) ---------------------------------------------------------------------------------------
PA = "A. Hannelore: § 185 StGB"
W185 = [[("„Die Beleidigung wird mit ", 0), ("Freiheitsstrafe bis zu einem Jahr", "a"), (" oder", 0)],
        [("mit Geldstrafe und, wenn die Beleidigung öffentlich, in einer", 0)],
        [("Versammlung, durch Verbreiten eines Inhalts (§ 11 Absatz 3) oder", 0)],
        [("mittels einer Tätlichkeit begangen wird, mit Freiheitsstrafe bis", 0)],
        [("zu zwei Jahren oder mit Geldstrafe bestraft.“", 0)]]
folie([("p185", PA), ("wl185", f"{PA} › Wortlaut"), ("kund", f"{PA} › I. Tatbestand: Kundgabe der Missachtung"),
       ("erfasst", f"{PA} › I. Tatbestand: Werturteile"), ("t185", f"{PA} › I. Tatbestand: Tatsachen nur gegenüber dem Betroffenen")],
      rechts_frei([
    *tafel("p185", "2. Beleidigung, § 185 StGB"),
    *wortlaut(110, 175, 1040, 222, "p185", W185, 29, {"a": beim("wl185", "Strafe")}, "§ 185 StGB"),
    z("Das Gesetz sagt nicht, was eine Beleidigung ist.", 110, 450, beim("wl185", "Was"), size=31),
    z("Angriff auf die Ehre durch Kundgabe", 110, 510, "kund", "Bold", 33),
    z("der Missachtung oder Nichtachtung", 110, 555, beim("kund", "Missachtung"), "Bold", 33),
    fund("BGH, Urt. v. 27.3.2009 – 2 StR 302/08, Rn. 26; OLG Hamm, 5 ORs 94/25, Rn. 15", 150, 603, beim("kund", "Missachtung")),
    *zeile_ok("Werturteile: gegenüber Betroffenem oder Dritten", 110, 665, "erfasst"),
    *zeile_ok("allg. Ansicht: Tatsachen nur gegenüber dem Betroffenen", 110, 725, "t185", size=31),
    *stufen("HA", X1, [("ruhig", "p185"), ("denkt", "kund"), ("ernst", "t185")]),
    *stufen("HE", X2, [("ernst", "p185"), ("still", "kund")], d=0.2),
    *wechsel([("§ 185 StGB", "p185", WEISS), ("nur die Strafe", "wl185", GELB), ("Kundgabe", "kund", GRUEN),
              ("Werturteile", "erfasst", GRUEN), ("Tatsachen?", "t185", BLAU)], MB, 160),
    *icons([("fluent-emoji-flat", "balance-scale", "p185", None), ("tabler", "file-text", "wl185", WEISS),
            ("fluent-emoji-flat", "speech-balloon", "kund", None), ("fluent-emoji-flat", "thought-balloon", "erfasst", None),
            ("fluent-emoji-flat", "magnifying-glass-tilted-left", "t185", None)], MB, 390, 120),
]))

# D2 Subsumtion Hannelore -------------------------------------------------------------------------------------------------------
folie([("sub185", f"{PA} › I. Tatbestand: Kundgabe (+)"), ("vors185", f"{PA} › I. Tatbestand: Vorsatz (+)")], rechts_frei([
    *tafel("sub185", "§ 185: Hannelore"),
    *chat("Hannelore", "Henner ist ein Idiot.", 110, 185, 560, "sub185"),
    pl("vor der ganzen Gruppe: 63 Mitglieder", 110, 345, beim("sub185", "ganzen"), fill=WEISS, size=30),
    *zeile_ok("spricht ihm seinen Wert ab", 110, 440, beim("sub185", "spricht"), size=34, stil="Bold"),
    *zeile_ok("Kundgabe der Missachtung", 110, 500, beim("sub185", "Kundgabe"), size=34, stil="Bold"),
    *zeile_ok("Vorsatz: Sie weiß und will es", 110, 580, "vors185", size=34, stil="Bold"),
    *stufen("HA", X1, [("entschlossen", "sub185"), ("ernst", "vors185")]),
    *stufen("HE", X2, [("sorge", "sub185"), ("still", "vors185")], d=0.2),
    *wechsel([("Kundgabe (+)", beim("sub185", "Kundgabe"), GRUEN), ("Vorsatz (+)", "vors185", GRUEN)], MB, 160),
    *icons([("fluent-emoji-flat", "speech-balloon", "sub185", None), ("tabler", "brain", "vors185", GELB)], MB, 390, 120),
]))

# E Rechtswidrigkeit: § 193 und Abwägung --------------------------------------------------------------------------------------
W193 = [[("„… Äußerungen …, welche … zur ", 0), ("Wahrnehmung berechtigter", "a")],
        [("Interessen", "a"), (" vorgenommen werden, … sind nur insofern strafbar, als", 0)],
        [("das Vorhandensein einer Beleidigung aus der Form der Äußerung", 0)],
        [("oder aus den Umständen, unter welchen sie geschah, hervorgeht.“", 0)]]
PR = f"{PA} › II. Rechtswidrigkeit"
folie([("rw185", PR), ("p193", f"{PR}: § 193 StGB"), ("abw", f"{PR}: Abwägung, Art. 5 Abs. 1 GG"),
       ("ehre", f"{PA} (+)")], rechts_frei([
    *tafel("rw185", "Rechtswidrigkeit: § 193 StGB"),
    *wortlaut(110, 175, 1040, 180, "p193", W193, 29, {"a": beim("p193", "Wahrnehmung")}, "§ 193 StGB (Auszug)"),
    z("Art. 5 Abs. 1 GG: Meinungsfreiheit und Ehre", 110, 410, "abw", "Bold", 33),
    z("im Regelfall abwägen", 110, 455, beim("abw", "Regelfall"), "Bold", 33),
    fund("BVerfG, Beschl. v. 19.5.2020 – 1 BvR 2397/19, Rn. 15, 26", 150, 503, beim("abw", "Regelfall")),
    *zeile_ok("trägt zur Sache nichts bei", 110, 565, beim("abw2", "Schimpfwort"), ja=False, size=33),
    *zeile_ok("schriftlich und dauerhaft, vor 63 Nachbarn", 110, 620, "schrift", ja=False, size=33),
    fund("1 BvR 2397/19, Rn. 29, 33, 34", 175, 670, beim("schrift", "dreiundsechzig")),
    fb(110, 725, 1040, 95, GRUENHELL, "ehre", [("Ehre wiegt schwerer: § 185 StGB (+)", "ExtraBold", 36, INK)]),
    *stufen("HA", X1, [("ruhig", "rw185"), ("redet", "ha1"), ("denkt", "abw2"), ("still", "ehre")], rede=("redet",)),
    *stufen("HE", X2, [("ernst", "rw185"), ("still", "ha1"), ("ernst", "abw2")], d=0.2),
    *wechsel([("gerechtfertigt?", "rw185", WEISS), ("§ 193 StGB", "p193", GELB), ("Abwägung", "abw", WEISS), (None, "ha1", None),
              ("Abwägung", "abw2", WEISS), ("Ehre wiegt schwerer", "ehre", GRUEN)], MB, 160),
    *icons([("fluent-emoji-flat", "balance-scale", "abw", None), (None, None, "ha1", None),
            ("fluent-emoji-flat", "balance-scale", "abw2", None)], MB, 390, 130),
    blase("sprech", 600, 175, "ha1", MB - 10, 240, inhalt=["Ich darf doch wohl", "meine Meinung sagen!"], textsize=34,
          figur=("HA_redet", X1, BR, FR), bis="abw2"),
]))

# F1 Üble Nachrede, § 186 (Wortlautkarte auszugsweise) ---------------------------------------------------------------------
PB = "B. Dörte: § 186 StGB"
W186 = [[("„Wer ", 0), ("in Beziehung auf einen anderen", "a"), (" eine ", 0), ("Tatsache behauptet oder", "b")],
        [("verbreitet", "b"), (", welche denselben ", 0), ("verächtlich zu machen", "c"), (" oder in der", 0)],
        [("öffentlichen Meinung herabzuwürdigen", "c"), (" geeignet ist, wird,", 0)],
        [("wenn nicht diese Tatsache erweislich wahr ist, mit Freiheitsstrafe", 0)],
        [("bis zu einem Jahr oder mit Geldstrafe … bestraft.“", 0)]]
folie([("p186", PB), ("wl186", f"{PB} › I. Tatbestand: Tatsache über einen anderen"), ("ehrenr", f"{PB} › I. Tatbestand: ehrenrührig"),
       ("sub186", f"{PB} › I. Tatbestand: Subsumtion"), ("vors186", f"{PB} › I. Tatbestand: Vorsatz (+)")], rechts_frei([
    *tafel("p186", "3. Üble Nachrede, § 186 StGB"),
    *wortlaut(110, 175, 1040, 222, "p186", W186, 29, {"a": beim("wl186", "Beziehung"), "b": beim("wl186", "Tatsache"),
                                                     "c": "ehrenr"}, "§ 186 StGB (Auszug)"),
    *chat("Dörte", "Henner schlägt seine Kinder.", 110, 455, 620, "sub186"),
    *zeile_ok("Tatsache, gegenüber den anderen Mitgliedern", 110, 610, beim("sub186", "gegenüber"), size=33),
    *zeile_ok("ehrenrührig", 110, 668, beim("sub186", "ehrenrührig"), size=33),
    *zeile_ok("Vorsatz", 110, 726, "vors186", size=33),
    *stufen("DO", X1, [("ruhig", "p186"), ("ernst", "sub186"), ("denkt", "vors186")]),
    *stufen("HE", X2, [("ernst", "p186"), ("sorge", "sub186")], d=0.2),
    *wechsel([("§ 186 StGB", "p186", WEISS), ("Tatsache über Henner", "wl186", BLAU), ("ehrenrührig?", "ehrenr", ROTHELL),
              ("vor 63 Mitgliedern", "sub186", WEISS), ("Vorsatz (+)", "vors186", GRUEN)], MB, 160),
    *icons([("fluent-emoji-flat", "balance-scale", "p186", None), ("fluent-emoji-flat", "magnifying-glass-tilted-left", "wl186", None),
            ("tabler", "alert-triangle", "ehrenr", ROT), ("fluent-emoji-flat", "mobile-phone", "sub186", None),
            ("tabler", "brain", "vors186", GELB)], MB, 390, 110),
]))

# F2 Nicht erweislich wahr --------------------------------------------------------------------------------------------------
W186b = [[("„… ", 0), ("wenn nicht diese Tatsache erweislich wahr ist", "a"), (", …“", 0)]]
folie([("erweis", f"{PB} › II. nicht erweislich wahr"), ("obj", f"{PB} › II. objektive Bedingung der Strafbarkeit"),
       ("sub_erw", f"{PB} › II. Bedingung erfüllt")], rechts_frei([
    *tafel("erweis", "Nicht erweislich wahr"),
    *wortlaut(110, 175, 1040, 80, "erweis", W186b, 31, {"a": beim("erweis", "erweislich")}, "§ 186 StGB"),
    z("Bleibt offen, ob es stimmt:", 110, 330, "risiko", "Bold", 33),
    z("das geht zulasten dessen, der es behauptet", 110, 375, beim("risiko", "zulasten"), "Bold", 33),
    fund("BVerfG, Beschl. v. 28.6.2016 – 1 BvR 3388/14, Rn. 17: „Beweisregel“", 150, 423, beim("risiko", "zulasten")),
    z("herrschende Lehre: objektive Bedingung", 110, 490, "obj", "Bold", 33),
    z("der Strafbarkeit", 110, 535, beim("obj", "Bedingung"), "Bold", 33),
    z("Der Vorsatz muss sich darauf nicht beziehen.", 110, 590, beim("obj", "Vorsatz"), size=33),
    fb(110, 665, 1040, 95, GRUENHELL, "sub_erw", [("nicht zu klären: Bedingung erfüllt", "ExtraBold", 36, INK)]),
    *stufen("DO", X1, [("ruhig", "erweis"), ("sorge", "sub_erw")]),
    *stufen("HE", X2, [("ernst", "erweis"), ("still", "obj")], d=0.2),
    *wechsel([("erweislich wahr?", "erweis", WEISS), ("Risiko: wer behauptet", "risiko", ROTHELL), ("objektive Bedingung", "obj", GELB),
              ("erfüllt", "sub_erw", GRUEN)], MB, 160),
    *icons([("fluent-emoji-flat", "magnifying-glass-tilted-left", "erweis", None), ("fluent-emoji-flat", "balance-scale", "risiko", None),
            ("tabler", "file-certificate", "obj", WEISS), ("tabler", "circle-check", "sub_erw", GRUEN)], MB, 390, 110),
]))

# F3 § 193 bei Dörte ------------------------------------------------------------------------------------------------------
PB3 = f"{PB} › III. Rechtswidrigkeit"
folie([("do1", f"{PB3}: § 193 StGB?"), ("sorg", f"{PB3}: Sorgfaltspflicht"), ("sorg2", f"{PB3}: keine Belege"),
       ("erg186", f"{PB} (+)")], rechts_frei([
    *tafel("do1", "Rechtfertigung: § 193 StGB?"),
    *chat("Dörte", "Henner schlägt seine Kinder.", 110, 180, 620, "do1"),
    z("Nicht erweislich wahre Tatsachen:", 110, 330, "sorg", "Bold", 33),
    z("nur nach sorgfältiger Prüfung", 110, 375, beim("sorg", "sorgfältig"), "Bold", 33),
    z("Je schwerer der Vorwurf,", 110, 440, beim("sorg", "Je"), size=33),
    z("desto höher die Anforderungen.", 110, 485, beim("sorg", "desto"), size=33),
    fund("BVerfG 1 BvR 3388/14, Rn. 20 f.; BVerfGE 99, 185 (198), Rn. 55", 150, 535, beim("sorg", "desto")),
    *zeile_ok("Dörte: keine Belege", 110, 605, "sorg2", ja=False, size=33),
    *zeile_ok("schwerer Vorwurf vor 63 Leuten", 110, 663, beim("sorg2", "schweren"), ja=False, size=33),
    fb(110, 750, 1040, 95, GRUENHELL, "erg186", [("Dörte: üble Nachrede, § 186 StGB (+)", "ExtraBold", 36, INK)]),
    *stufen("DO", X1, [("redet", "do1"), ("sorge", "rw186"), ("still", "erg186")], rede=("redet",)),
    *stufen("HE", X2, [("ernst", "do1"), ("still", "erg186")], d=0.2),
    blase("sprech", 600, 175, "do1", MB - 10, 240, inhalt=["Ich wollte die Nachbarn", "doch nur warnen!"], textsize=34,
          figur=("DO_redet", X1, BR, FR), bis="rw186"),
    *wechsel([("§ 193?", "rw186", WEISS), ("Sorgfalt?", "sorg", GELB), ("keine Belege", "sorg2", ROTHELL),
              ("§ 186 (+)", "erg186", GRUEN)], MB, 160),
    *icons([("fluent-emoji-flat", "balance-scale", "rw186", None), ("fluent-emoji-flat", "magnifying-glass-tilted-left", "sorg", None),
            ("tabler", "file-text", "sorg2", ROTHELL), ("fluent-emoji-flat", "balance-scale", "erg186", None)], MB, 390, 110),
]))

# G1 Variante: Verleumdung, § 187 ----------------------------------------------------------------------------------------
PC = "C. Variante: § 187 StGB"
W187 = [[("„Wer ", 0), ("wider besseres Wissen", "a"), (" in Beziehung auf einen anderen eine", 0)],
        [("unwahre Tatsache", "b"), (" behauptet oder verbreitet, welche denselben", 0)],
        [("verächtlich zu machen oder in der öffentlichen Meinung", 0)],
        [("herabzuwürdigen … geeignet ist, wird mit Freiheitsstrafe bis zu", 0)],
        [("zwei Jahren oder mit Geldstrafe … bestraft.“", 0)]]
folie([("p187", f"{PC} – Dörte weiß es besser"), ("wl187", f"{PC} › wider besseres Wissen, unwahre Tatsache"),
       ("unwahr", f"{PC} › Unwahrheit: Tatbestand"), ("schutz", f"{PC} › nicht von Art. 5 Abs. 1 GG geschützt"),
       ("erg187", f"{PC} (+)")], rechts_frei([
    *tafel("p187", "4. Variante: Verleumdung, § 187 StGB", size=46),
    *wortlaut(110, 175, 1040, 222, "p187", W187, 29, {"a": beim("wl187", "wider"), "b": beim("wl187", "unwahre")},
              "§ 187 StGB (Auszug)"),
    *zeile_ok("Unwahrheit: Tatbestandsmerkmal, muss feststehen", 110, 455, "unwahr", size=32),
    *zeile_ok("wider besseres Wissen: Dörte kennt sie sicher", 110, 513, "wissen", size=32),
    z("bewusst unwahre Tatsachenbehauptungen:", 110, 590, "schutz", "Bold", 32),
    z("von der Meinungsfreiheit nicht geschützt", 110, 633, beim("schutz", "schützt"), "Bold", 32),
    fund("BVerfGE 90, 241 (247 f.), Rn. 28; BVerfGE 99, 185 (197), Rn. 52", 150, 680, beim("schutz", "schützt")),
    fb(110, 735, 1040, 95, GRUENHELL, "erg187", [("Variante: Verleumdung, § 187 StGB (+)", "ExtraBold", 36, INK)]),
    *stufen("DO", XS, [("denkt", "p187"), ("ernst", "unwahr"), ("still", "erg187")]),
    blase("denk", 420, 160, "p187", XS - 30, 230, inhalt=["Stimmt nicht."], textsize=36, figur=("DO_denkt", XS, BR, FR)),
]))

# G2 Qualifikation (offen) und Strafantrag ---------------------------------------------------------------------------------
W194 = [[("„Die Beleidigung wird ", 0), ("nur auf Antrag", "a"), (" verfolgt.“", 0)]]
folie([("quali", "Qualifikation · öffentlich, Versammlung, Verbreiten eines Inhalts"),
       ("offen", "Qualifikation · geschlossene Chatgruppe: offen"), ("antrag", "Strafantrag · § 194 Abs. 1 StGB")], rechts_frei([
    *tafel("quali", "Qualifikation und Strafantrag"),
    z("Höherer Strafrahmen in §§ 185, 186, 187, wenn die Tat", 110, 180, "quali", "Bold", 32),
    z("öffentlich, in einer Versammlung oder durch", 150, 228, beim("quali", "öffentlich"), size=32),
    z("Verbreiten eines Inhalts begangen ist", 150, 273, beim("quali", "Verbreiten"), size=32),
    z("Geschlossene Chatgruppe: hängt vom Einzelfall ab", 110, 350, "offen", "Bold", 32),
    pl("unser Sachverhalt: offen", 150, 400, beim("offen", "Unser"), fill=GELB, size=30),
    *wortlaut(110, 505, 1040, 80, "antrag", W194, 31, {"a": beim("antrag", "Antrag")}, "§ 194 Abs. 1 S. 1 StGB"),
    z("grundsätzlich nur auf Antrag", 110, 640, beim("antrag", "Antrag"), "Bold", 33),
    *zeile_ok("Henner hat ihn gestellt", 110, 700, beim("antrag", "Henner"), size=33, stil="Bold"),
    *stufen("HE", XS, [("ruhig", "quali"), ("ernst", "antrag")]),
    *wechsel([("öffentlich?", "quali", WEISS), ("Chatgruppe?", "offen", GELB), ("Strafantrag", "antrag", BLAU)], XS, 160),
    *icons([("fluent-emoji-flat", "megaphone", "quali", None), ("fluent-emoji-flat", "mobile-phone", "offen", None),
            ("fluent-emoji-flat", "page-facing-up", "antrag", None)], XS, 390, 110),
]))

# H Abgrenzungstabelle mit Ergebnis ---------------------------------------------------------------------------------------
TX = [110, 300, 720, 1080, 1450]
folie([("tab", "Abgrenzung · §§ 185, 186, 187 StGB"), ("z185", "Abgrenzung › § 185: Beleidigung"),
       ("z186", "Abgrenzung › § 186: üble Nachrede"), ("z187", "Abgrenzung › § 187: Verleumdung"), ("erg", "Ergebnis")], [
    karte(60, 50, 1800, 920, "tab"),
    titel("Abgrenzung auf einen Blick", 110, 90, "tab", 52),
    *tabelle_zeile(["Norm", "Inhalt", "gegenüber", "Wahrheit", "unser Fall"], TX, 200, "tab", size=34, stil="ExtraBold"),
    linienzug([(100, 258), (1820, 258)], "tab", breite=4, farbe=INK),
    *tabelle_zeile(["§ 185", ["Werturteile", "Tatsachen"], ["jedem", "nur dem Betroffenen"], "–"], TX, 300, "z185", size=36),
    linienzug([(100, 435), (1820, 435)], beim("z185", "Tatsachen"), breite=3, farbe=GRAU),
    *tabelle_zeile(["§ 186", ["ehrenrührige", "Tatsachen"], "Dritten", ["nicht erweislich", "wahr"]], TX, 470, "z186", size=36),
    linienzug([(100, 605), (1820, 605)], "z187", breite=3, farbe=GRAU),
    *tabelle_zeile(["§ 187", ["unwahre", "Tatsachen"], "Dritten", ["wider besseres", "Wissen"]], TX, 640, "z187", size=36),
    pl("Hannelore", TX[4], 318, "erg", fill=GRUEN, size=32),
    pl("Dörte", TX[4], 488, "erg2", fill=LILA, size=32),
    pl("Dörte (Variante)", TX[4], 658, "erg3", fill=LILAHELL, size=32),
])

# I Klausurtipp (Lexi) -------------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · Schmähkritik nicht vorschnell annehmen"), ("tipp3", "Klausurtipp · Regelfall: Abwägung bei § 193")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Schmähkritik nicht vorschnell annehmen", 200, 200, beim("tipp", "Nimm"), "Bold", 35),
    z("nur ohne nachvollziehbaren Bezug", 200, 290, "tipp2", "ExtraBold", 35),
    z("zu einer sachlichen Auseinandersetzung", 200, 340, beim("tipp2", "sachlichen"), "ExtraBold", 35),
    fund("BVerfG, Beschl. v. 19.5.2020 – 1 BvR 2397/19, Rn. 19", 240, 395, beim("tipp2", "sachlichen")),
    z("Regelfall: abwägen,", 200, 470, "tipp3", "ExtraBold", 36),
    z("und zwar bei § 193 StGB", 200, 522, beim("tipp3", "zwar"), "ExtraBold", 36),
    fund("1 BvR 2397/19, Rn. 15, 26", 240, 578, beim("tipp3", "zwar")),
    *redet("LX_warnt", LXX, BR, FR + 60, "tipp", "sch"),
    namensschild("Lexi", LXX, BR, "tipp", GELB, d=0.2),
])

# J Klausurschema -----------------------------------------------------------------------------------------------------------
K1, K2 = 150, 230
PS_ = "Klausurschema"
folie([("sch", PS_), ("k0", f"{PS_} › Vorweg: Werturteil oder Tatsache?"), ("k1", f"{PS_} › I. Tatbestand"),
       ("k1a", f"{PS_} › I. 1. ehrverletzende Äußerung"), ("k1b", f"{PS_} › I. 2. Qualifikation"), ("k1c", f"{PS_} › I. 3. Vorsatz"),
       ("k2", f"{PS_} › II. nur § 186: nicht erweislich wahr"), ("k3", f"{PS_} › III. Rechtswidrigkeit, § 193"),
       ("k4", f"{PS_} › IV. Schuld"), ("k5", f"{PS_} › V. Strafantrag, § 194")], [
    karte(60, 50, 1800, 920, "sch"),
    titel("Klausurschema: §§ 185–187 StGB", 110, 90, "sch", 52),
    z("Vorweg: Werturteil oder Tatsache? Wem gegenüber?", K1, 185, "k0", "Bold", 36, rechts=1820),
    z("I. Tatbestand", K1, 260, "k1", "Bold", 38, rechts=1820),
    z("1. ehrverletzende Äußerung nach § 185, § 186 oder § 187", K2, 318, "k1a", size=34, rechts=1820),
    z("2. ggf. Qualifikation", K2, 370, "k1b", size=34, rechts=1820),
    z("3. Vorsatz; bei § 187: wider besseres Wissen", K2, 422, "k1c", size=34, rechts=1820),
    z("II. nur bei § 186: nicht erweislich wahr", K1, 500, "k2", "Bold", 38, rechts=1820),
    z("III. Rechtswidrigkeit: § 193 StGB und Abwägung", K1, 575, "k3", "Bold", 38, rechts=1820),
    z("IV. Schuld", K1, 650, "k4", "Bold", 38, rechts=1820),
    z("V. Strafantrag, § 194 Abs. 1 StGB", K1, 725, "k5", "Bold", 38, rechts=1820),
])

# K Merksatz (Lexi) ---------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Werturteile", "a"), (" prüfst du bei § 185.", 0)]], 750, 300, 44, "merke", {"a": beim("merke", "Werturteile")}),
    *markertext([[("Ehrenrührige ", 0), ("Tatsachen gegenüber Dritten", "b")], [("bei § 186, wenn sie ", 0),
                 ("nicht erweislich wahr", "c"), (" sind,", 0)]], 750, 410, 44, "m2",
                {"b": beim("m2", "Tatsachen"), "c": beim("m2", "nicht")}),
    *markertext([[("und bei § 187, wenn der Täter", 0)], [("ihre ", 0), ("Unwahrheit kennt", "d"), (".", 0)]], 750, 600, 44, "m3",
                {"d": beim("m3", "Unwahrheit")}),
    *redet("LX_erklaert", 1680, 960, 690, "merke", lexi_bis_ende("merke")),
    namensschild("Lexi", 1680, 960, "merke", GELB, d=0.2),
])
