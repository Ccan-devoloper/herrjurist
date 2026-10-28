"""Folge 111 · Räuberischer Diebstahl § 252 StGB: Gewalt auf der Flucht – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A1 Fall im Elektromarkt (Regal, Kasse, Ausgang; Gottfried steckt Kopfhörer ein, Edda sieht
es), A2 vor dem Eingang (Edda stellt ihn, Stoß nur als Abstand und Warnsymbol, Gottfried rennt mit den Kopfhörern davon,
Edda unverletzt, Frage), B Sachverhalt, C Wortlaut § 252 und Aufbau, D 1. Vortat (vollendet, nicht beendet; warum kein
Raub), E 2. auf frischer Tat betroffen (Streit Zuvorkommen), F 3. Nötigungsmittel, G 4. subjektiv (Vorsatz,
Besitzerhaltungsabsicht), H Ergebnis, Rechtsfolge, Konkurrenzen, I Gegenvariante, J Klausurtipp (Lexi),
K Klausurschema, L Merksatz (Lexi).
Zurückhaltend: keine Verletzung, kein Sturz; Gottfried gewöhnlich gekleidet, keine Karikatur. Zahlen auf Tafeln, Pillen und
Blasen als Ziffern. Geräusch nur bei sichtbarer Handlung: Laufschritte, als Gottfried davonrennt (szene_111laufen_1)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import wave as _wave

bausteine.FIGORDNER = "op_111/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
LILAHELL = (246, 243, 255, 255)
ROTHELL = (253, 232, 228, 255)
GRUENHELL = (232, 247, 233, 255)
BLAUHELL = (233, 241, 253, 255)
DAUER = bausteine._cj()["dauer"]
NULL = "fall"                     # Szene A1 steht ab 0,0 s (render_111 setzt alle Elemente bis zur Marke „fall“ auf 0,0 s)

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


def tafel(cue, titel_, h=840, fill=WEISS, size=48):
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(glyphen(titel_), 110, 100, cue, size)]


def fund(text, x, y, cue, **k):
    """Fundstelle (mobil lesbar: 26 px)."""
    return z(text, x, y, cue, size=26, farbe=TEXT, **k)


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


def bis_(e, cue):
    e.bis = cue
    return e


def umbruch(text, breite, size):
    f = F("Regular", size)
    zeilen, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if f.getlength(t) <= breite:
            cur = t
        else:
            zeilen.append(cur); cur = w
    return zeilen + [cur]


def sachverhalt_klein(cue, absaetze, frage, size=38, pfad="Sachverhalt"):
    """Wie bausteine.sachverhalt(), aber Schrift passend zu Grundfall und zwei Abwandlungen (wie Folge 051)."""
    els = [karte(140, 50, 1640, 920, cue, fill=HELL), titel("Sachverhalt", 210, 82, cue, 56)]
    y = 175
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=size, zeilenabstand=1.27)
        els += e; y += 14
    els.append(pl(frage, 210, y + 8, cue, fill=PINK, size=34))
    assert y + 8 <= 890, f"Sachverhalt zu lang ({y})"
    folie([(cue, pfad)], els)


def markertext_farbig(zeilen_tokens, cx, y, size, cue, hl_cues, farben, lh=1.3):
    """Wie ostil.markertext, aber mit eigener Markerfarbe je Schlüssel (wie Folge 084)."""
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
        xx = 20 + (maxw - wid) / 2
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
    x0 = cx - im.width / 2
    els = [El(im, x0, y, cue, "rise", 0.0, name="markertext")]
    for key, oim in ov.items():
        els.append(El(oim, x0, y, hl_cues[key], "fade", 0.0, name="marker:" + key))
    return els


def wortlaut(x, y, w, h, cue, zeilen, size, hl, quelle, farben=None):
    """Wortlautkarte: wörtliches Zitat (gesetze-im-internet.de, Abruf 03.10.2026) in einer hellen Karte, Fundstelle darunter
    rechts. zeilen = Liste von Token-Listen [(text, Schlüssel|0)], hl = {Schlüssel: Cue} (Hervorhebung synchron zum Wort)."""
    els = [karte(x, y, w, h, cue, fill=(246, 246, 250, 255), rund=18, schatten=6, rand=4)]
    farben = farben or {k: GELB for k in hl}
    m = markertext_farbig(zeilen, x + w / 2, y + 22, size, cue, hl, farben, lh=1.28)
    assert m[0].x >= x + 10 and m[0].x + m[0].sprite.width <= x + w - 10, f"Wortlaut zu breit ({m[0].sprite.width} > {w})"
    assert m[0].y + m[0].sprite.height <= y + h + 6, "Wortlaut zu hoch"
    els += m
    q = zeile(glyphen(quelle), 0, 0, cue, "Bold", 26, farbe=TEXT)
    q.x = x + w - q.sprite.width - 24; q.y = y + h + 8
    els.append(q)
    return els


# --- Eigene Hilfsfunktion (wie Folge 051/075/084): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ---------------
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
BR, FR_H = 930, 480                     # Figuren rechts neben der Tafel
X1, X2 = 1440, 1740
MB = (X1 + X2) // 2
XS = 1600


def bewegungslinien(x, y, cue, bis=None, n=3, laenge=70, abstand=26):
    """Dezente Bewegungslinien hinter einer laufenden Figur (nur Striche, kein Aufprall)."""
    return [bis_(linienzug([(x - laenge, y + i * abstand), (x, y + i * abstand)], cue, breite=5, farbe=TEXT), bis)
            for i in range(n)]


SCHILD = {"GO": ("Gottfried", LILA), "ED": ("Edda", ROT)}


def figur_kette(p, x, cue, mimik, folge=(), bis=None, d=0.0, unten=BR, hoehe=FR_H, schild=True, schild_d=0.2, erst="pop"):
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


def paar(cue, go_folge=(), ed_folge=(), go="ruhig", ed="ruhig"):
    """Gottfried bei X1, Edda bei X2; beide blicken zur Tafel (Eddas Zeigefinger zeigt zur Tafel, nicht auf Gottfried)."""
    return figur_kette("GO", X1, cue, go, go_folge) + figur_kette("ED", X2, cue, ed, ed_folge, d=0.2, schild_d=0.3)


def kh(cx, unten, breite, cue, bis=None, anim="pop", d=0.0):
    """Die Kopfhörer (Fluent Emoji „headphone“)."""
    return ficon("fluent-emoji-flat", "headphone", cx, unten, breite, cue, bis=bis, anim=anim, d=d)


def markt_innen(cue):
    """Elektromarkt innen: Regal links (Fernseher, Laptop, Kopfhörer, Handy), Kasse in der Mitte, Ausgang rechts."""
    els = [linienzug([(60, BODEN), (1860, BODEN)], cue, breite=7, farbe=INK),
           karte(90, 330, 380, 550, cue, fill=WEISS, rund=12, schatten=6, rand=5)]
    for y in (480, 640, 780):
        els.append(linienzug([(100, y), (460, y)], cue, breite=5, farbe=INK))
    els += [ficon("fluent-emoji-flat", "television", 200, 470, 120, cue),
            ficon("fluent-emoji-flat", "laptop", 360, 470, 110, cue),
            ficon("fluent-emoji-flat", "mobile-phone", 170, 630, 55, cue),
            ficon("fluent-emoji-flat", "mobile-phone", 240, 630, 55, cue),
            ficon("fluent-emoji-flat", "headphone", 180, 770, 80, cue),
            karte(880, 720, 280, 160, cue, fill=BLAUHELL, rund=12, schatten=6, rand=5),
            ficon("fluent-emoji-flat", "receipt", 960, 720, 60, cue),
            ficon("fluent-emoji-flat", "credit-card", 1080, 720, 70, cue),
            pl("Kasse", 1020, 790, cue, fill=WEISS, size=28, anker="m"),
            ficon("fluent-emoji-flat", "door", 1790, BODEN, 120, cue),
            pl("Ausgang", 1800, 680, cue, fill=GRUEN, size=28, anker="m")]
    return els


def markt_aussen(cue):
    """Vor dem Eingang: Fassade mit Schild und Tür links, Gehweg, Baum rechts."""
    return [linienzug([(60, BODEN), (1860, BODEN)], cue, breite=7, farbe=INK),
            karte(70, 260, 560, 620, cue, fill=(240, 240, 246, 255), rund=12, schatten=6, rand=5),
            pl("Elektromarkt", 350, 300, cue, fill=GELB, size=32, anker="m"),
            ficon("fluent-emoji-flat", "door", 450, BODEN, 150, cue),
            ficon("fluent-emoji-flat", "television", 200, 560, 110, cue),
            ficon("fluent-emoji-flat", "deciduous-tree", 1790, BODEN, 200, cue)]


# A1 Fall: im Elektromarkt ------------------------------------------------------------------------------------------------
GX, FH = 640, 540                       # Gottfried am Regal (blickt nach links zum Regal)
EX = 1300                               # Edda beobachtet (blickt nach links zu ihm)
GK = 1560                               # Gottfried hinter der Kasse auf dem Weg zum Ausgang (blickt nach rechts)
folie([(NULL, "Fall · Im Elektromarkt"), ("steckt", "Fall · Gottfried steckt die Kopfhörer ein"),
       ("kasse", "Fall · An der Kasse vorbei")], [
    *markt_innen(NULL),
    pl("Samstagvormittag", 100, 64, NULL, fill=GELB, size=32),
    *figur_kette("GO", GX, NULL, "ruhig", [("listig", "steckt")], bis="kasse", unten=BODEN, hoehe=FH, schild=False),
    namensschild("Gottfried", GX, BODEN - 8, NULL, LILA, bis="kasse"),
    kh(GX - 150, 600, 80, "gott", bis="steckt"),
    pl("Kopfhörer · 129 €", GX, 250, beim("gott", "Kopfhörer"), fill=GELB, size=30, anker="m", bis="steckt"),
    pl("in die Innentasche seiner Jacke", GX, 250, "steckt", fill=WEISS, size=28, anker="m", anim="cut", bis="kasse"),
    *figur_kette("ED", EX, "edda", "ernst", [("ernst_r", "kasse")], unten=BODEN, hoehe=FH, schild=False),
    namensschild("Edda", EX, BODEN - 8, "edda", ROT, d=0.1),
    pl("Mitarbeiterin", EX, 250, "edda", fill=ROT, size=28, anker="m"),
    ficon("fluent-emoji-flat", "eyes", EX - 170, 450, 70, beim("edda", "gesehen"), bis="kasse"),
    peep_voll("GO_ruhig_r", GK, BODEN, FH, "kasse", anim="cut"),
    namensschild("Gottfried", GK, BODEN - 8, "kasse", LILA, anim="cut"),
    pl("vorbei, ohne zu bezahlen", 950, 600, beim("kasse", "ohne"), fill=ROTHELL, size=28, anker="m"),
    ficon("tabler", "arrow-right", GK + 170, 560, 70, beim("kasse", "verlässt")),
])

# A2 Fall: vor dem Eingang ------------------------------------------------------------------------------------------------
EA, GA = 780, 1180                      # Edda kommt aus der Tür (blickt nach rechts), Gottfried dreht sich zu ihr (blickt nach links)
GR = 1600                               # Gottfried rennt nach rechts davon
EDb = ("ED_redet_r", EA, BODEN, FH)
GOb = ("GO_redet", GA, BODEN, FH)
R0 = beim("rennt", "rennt")
folie([("drauss", "Fall · Vor dem Eingang"), ("stoss", "Fall · Der Stoß"), ("rennt", "Fall · Gottfried rennt davon"),
       ("frage", "Fall · Die Frage")], [
    *markt_aussen("drauss"),
    peep_voll("GO_ertappt", GA, BODEN, FH, "drauss", bis="stoss"),
    namensschild("Gottfried", GA, BODEN - 8, "drauss", LILA, d=0.1, bis=R0),
    peep_voll("ED_ernst_r", EA, BODEN, FH, "drauss", d=0.2, bis="e1"),
    namensschild("Edda", EA, BODEN - 8, "drauss", ROT, d=0.3, bis="stoss"),
    pl("direkt vor dem Eingang", 1000, 150, beim("drauss", "Eingang"), fill=WEISS, size=28, anker="m", bis="e1"),
    *redet("ED_redet_r", EA, BODEN, FH, "e1", "greift"),
    blase("sprech", 620, 200, "e1", 1010, 170, inhalt=["Halt! Die Kopfhörer in", "Ihrer Jacke gehören uns!"], textsize=32,
          figur=EDb, bis="greift"),
    peep_voll("ED_ernst_r", EA, BODEN, FH, "greift", anim="cut", bis="stoss"),
    pl("greift nach seiner Jacke", 1000, 150, "greift", fill=WEISS, size=28, anker="m", bis="stoss"),
    ficon("tabler", "hand-grab", 990, 560, 70, "greift", fuell=WEISS, bis="stoss"),
    # der Stoß: Edda weicht zurück (nur Abstand und Warnsymbol, keine Verletzung)
    peep_voll("ED_erschrickt_r", EA - 90, BODEN, FH, "stoss", anim="cut", bis="taumelt"),
    namensschild("Edda", EA - 90, BODEN - 8, "stoss", ROT, anim="cut"),
    peep_voll("GO_entschlossen", GA, BODEN, FH, "stoss", anim="cut", bis="g1"),
    ficon("fluent-emoji-flat", "warning", 960, 520, 90, "stoss", bis=R0),
    pl("stößt Edda weg", 880, 130, "stoss", fill=ROTHELL, size=28, anker="m", bis=R0),
    pl("damit sie ihm die Kopfhörer nicht abnimmt", 880, 195, beim("stoss", "damit"), fill=WEISS, size=28, anker="m", bis=R0),
    *redet("GO_redet", GA, BODEN, FH, "g1", "rennt"),
    blase("sprech", 520, 170, "g1", 1510, 330, inhalt=["Die Kopfhörer behalte ich!"], textsize=32, figur=GOb, bis="rennt"),
    peep_voll("GO_entschlossen", GA, BODEN, FH, "rennt", anim="cut", bis=R0),
    szene(bewegt(peep_voll("GO_entschlossen_r", GR, BODEN, FH, R0, anim="cut"), R0, beim("rennt", "davon", ende=True), -420, 0),
          "111laufen_1", 0.8),
    bewegt(namensschild("Gottfried", GR, BODEN - 8, R0, LILA, anim="cut"), R0, beim("rennt", "davon", ende=True), -420, 0),
    *bewegungslinien(GR - 150, 470, beim("rennt", "davon", ende=True), bis="frage"),
    pl("mit den Kopfhörern davon", GR, 230, beim("rennt", "davon"), fill=PINK, size=28, anker="m", bis="frage"),
    peep_voll("ED_sorge_r", EA - 90, BODEN, FH, "taumelt", anim="cut"),
    pl("taumelt zurück, nicht verletzt", EA - 60, 230, "taumelt", fill=WEISS, size=28, anker="m", bis="frage"),
    pl("Ist Gottfried jetzt ein Räuber?", 1080, 200, "frage", fill=PINK, size=38, anker="m"),
    pl("§ 252 Schritt für Schritt", 940, 300, beim("frage2", "räuberischen"), fill=WEISS, size=30, anker="m"),
    pl("mit Gegenvariante", 1310, 300, beim("frage2", "Gegenvariante"), fill=GELB, size=30, anker="m"),
])

# B Sachverhalt -------------------------------------------------------------------------------------------------------------
sachverhalt_klein("sv", [
    "Samstagvormittag im Elektromarkt: Gottfried nimmt Kopfhörer für 129 € aus dem Regal und steckt sie in die Innentasche "
    "seiner Jacke. Mitarbeiterin Edda hat das gesehen. Gottfried geht an der Kasse vorbei, ohne zu bezahlen, und verlässt den "
    "Markt. Direkt vor dem Eingang holt Edda ihn ein und greift nach seiner Jacke. Gottfried stößt sie weg, damit sie ihm die "
    "Kopfhörer nicht abnimmt, ruft „Die Kopfhörer behalte ich!“ und rennt mit ihnen davon. Edda taumelt zurück, verletzt ist "
    "sie nicht.",
    "Gegenvariante: Gottfried wirft die Kopfhörer weg und stößt Edda nur, um zu entkommen.",
], "Hat sich Gottfried nach § 252 StGB strafbar gemacht?")

# C Wortlaut § 252 und Aufbau ---------------------------------------------------------------------------------------------
W1 = [[("„Wer, bei einem ", 0), ("Diebstahl", "a"), (" ", 0), ("auf frischer Tat betroffen", "b"), (", gegen", 0)],
      [("eine Person ", 0), ("Gewalt", "c"), (" verübt oder ", 0), ("Drohungen mit", "d")],
      [("gegenwärtiger Gefahr für Leib oder Leben", "d"), (" anwendet, um", 0)],
      [("sich im Besitz des gestohlenen Gutes zu erhalten", "e"), (",", 0)],
      [("ist ", 0), ("gleich einem Räuber", "f"), (" zu bestrafen.“", 0)]]
PT = "A. § 252 StGB › I. Tatbestand"
folie([("p252", "A. Räuberischer Diebstahl, § 252 StGB › Wortlaut"), ("aufbau", "A. Räuberischer Diebstahl, § 252 StGB › Aufbau")],
      rechts_frei([
    *tafel("p252", "Räuberischer Diebstahl: § 252 StGB", size=44),
    *wortlaut(100, 165, 1060, 245, "p252", W1, 30,
              {"a": beim("p252w", "Diebstahl"), "b": beim("p252w", "auf"), "c": beim("p252w", "Gewalt"),
               "d": beim("p252w", "Drohungen"), "e": beim("p252w", "um"), "f": beim("p252w", "gleich")}, "§ 252 StGB",
              farben={"a": BLAU, "b": GRUEN, "c": GELB, "d": GELB, "e": LILA, "f": ROT}),
    blk(110, 470, 1040, 68, BLAU, "auf1", [("1. Vortat: Diebstahl", "ExtraBold", 32, INK)]),
    blk(110, 553, 1040, 68, GRUEN, "auf2", [("2. auf frischer Tat betroffen", "ExtraBold", 32, INK)]),
    blk(110, 636, 1040, 68, GELB, "auf3", [("3. Nötigungsmittel", "ExtraBold", 32, INK)]),
    blk(110, 719, 1040, 68, LILA, "auf4", [("4. subjektiv: Vorsatz, Besitzerhaltungsabsicht", "ExtraBold", 32, INK)]),
    *paar("p252", go_folge=[("ernst", "aufbau")], ed_folge=[("ernst", "aufbau")]),
    pl("§ 252 StGB", MB, 160, "p252", fill=WEISS, size=30, anker="m", bis="aufbau"),
    ficon("fluent-emoji-flat", "balance-scale", MB, 390, 130, "p252", bis="aufbau"),
    pl("4 Prüfpunkte", MB, 160, "aufbau", fill=GELB, size=30, anker="m", anim="cut"),
    kh(MB, 390, 110, "aufbau", anim="cut"),
]))

# D 1. Vortat: vollendeter, nicht beendeter Diebstahl; warum kein Raub -----------------------------------------------------
TL = 650                                # Zeitleiste
folie([("vt", f"{PT} › 1. Vortat: Diebstahl vollendet"), ("vt4", f"{PT} › 1. Vortat: nicht beendet"),
       ("p249", "Abgrenzung › Raub, § 249 StGB?")], rechts_frei([
    *tafel("vt", "1. Vortat: Diebstahl"),
    z("Der Diebstahl muss vollendet sein", 110, 170, beim("vt", "Der"), "Bold", 34),
    ok(135, 245, "vt2", gr=18),
    z("eingesteckt: eigener Gewahrsam schon im Laden", 175, 225, "vt2", size=33),
    ok(135, 300, "vt3", gr=18),
    z("Edda sieht zu: ändert nichts, vollendet", 175, 280, "vt3", size=33),
    fund("BGH, Urt. v. 18.2.2010 – 3 StR 556/09, Rn. 11 f.", 175, 328, beim("vt3", "vollendet")),
    z("noch nicht beendet: Beute nicht gesichert", 110, 385, "vt4", "Bold", 33),
    fund("BGH, Urt. v. 8.10.2014 – 5 StR 395/14, Rn. 6", 150, 433, beim("vt4", "gesichert")),
    z("Warum kein Raub?", 110, 490, "p249", "ExtraBold", 34),
    linienzug([(130, TL), (1130, TL)], "p249", breite=7, farbe=INK),
    linienzug([(500, TL - 22), (500, TL + 22)], "p249", breite=7, farbe=INK),
    linienzug([(930, TL - 22), (930, TL + 22)], "p249", breite=7, farbe=INK),
    z("Vollendung", 430, TL + 28, "p249", "Bold", 28),
    z("Beendigung", 860, TL + 28, "p249", "Bold", 28),
    pl("§ 249: Gewalt, um wegzunehmen", 315, 575, "p249b", fill=GELB, size=26, anker="m"),
    pl("§ 252", 715, 575, beim("p249c", "Paragraf"), fill=GRUEN, size=28, anker="m"),
    z("Gottfried stößt erst nach der Vollendung", 110, 735, beim("p249b", "Gottfried"), size=33),
    z("§ 252: Phase zwischen Vollendung und Beendigung", 110, 785, "p249c", "Bold", 33),
    fund("BGH, Urt. v. 18.4.2002 – 3 StR 52/02, Rn. 16", 150, 835, beim("p249c", "Paragraf")),
    *figur_kette("GO", XS, "vt", "ernst", [("listig", "vt2"), ("ernst", "vt4"), ("still", "p249")]),
    pl("vollendet?", XS, 160, "vt", fill=WEISS, size=30, anker="m", bis="vt2"),
    kh(XS - 50, 380, 90, "vt2", bis="vt4"),
    ficon("fluent-emoji-flat", "coat", XS + 60, 380, 90, "vt2", bis="vt4"),
    pl("Folge zur Gewahrsamsenklave", XS, 160, beim("vt2", "Folge"), fill=LILAHELL, size=26, anker="m", anim="cut", bis="vt3"),
    pl("vollendet", XS, 160, "vt3", fill=GRUEN, size=30, anker="m", anim="cut", bis="vt4"),
    pl("nicht beendet", XS, 160, "vt4", fill=WEISS, size=30, anker="m", anim="cut", bis="p249"),
    ficon("fluent-emoji-flat", "running-shoe", XS, 380, 100, "vt4", bis="p249"),
    pl("kein Raub", XS, 160, "p249", fill=ROTHELL, size=30, anker="m", anim="cut", bis="p249c"),
    ficon("fluent-emoji-flat", "balance-scale", XS, 390, 130, "p249", bis="p249c"),
    pl("§ 252", XS, 160, "p249c", fill=GRUEN, size=30, anker="m", anim="cut"),
    ficon("fluent-emoji-flat", "hourglass-not-done", XS, 380, 90, "p249c"),
]))

# E 2. Auf frischer Tat betroffen -------------------------------------------------------------------------------------------
folie([("ft", f"{PT} › 2. auf frischer Tat betroffen"), (beim("ft3", "Er"), f"{PT} › 2. auf frischer Tat betroffen (+)"),
       ("zuvor", f"{PT} › 2. Streit: Zuvorkommen")], rechts_frei([
    *tafel("ft", "2. Auf frischer Tat betroffen", size=46),
    z("frisch, solange enger räumlicher und zeitlicher", 110, 170, "ft2", "Bold", 34),
    z("Zusammenhang besteht", 110, 215, beim("ft2", "Zusammenhang"), "Bold", 34),
    z("Täter noch in unmittelbarer Nähe zum Tatort", 110, 275, beim("ft2", "Täter"), size=33),
    z("und alsbald nach der Tat wahrgenommen", 110, 320, beim("ft2", "alsbald"), size=33),
    fund("BGH, Beschl. v. 14.3.2023 – 4 StR 451/22, Rn. 7", 150, 368, beim("ft2", "wahrgenommen")),
    ok(135, 445, "ft3", gr=18),
    z("Edda stellt ihn direkt vor dem Eingang,", 175, 425, "ft3", size=33),
    z("gleich nach der Tat", 175, 470, beim("ft3", "gleich"), size=33),
    blk(110, 520, 1040, 70, GRUENHELL, beim("ft3", "Er"), [("auf frischer Tat betroffen (+)", "ExtraBold", 34, INK)]),
    z("schon im Laden beobachtet: schadet nicht", 110, 610, "ft4", size=33),
    fund("BGH, Beschl. v. 4.8.2015 – 3 StR 112/15, Rn. 5", 150, 655, beim("ft4", "schadet")),
    karte(110, 705, 1040, 165, "zuvor", fill=BLAUHELL, rund=18, schatten=6, rand=4),
    z("umstritten: Täter kommt der Entdeckung durch", 135, 718, "zuvor", "Bold", 32),
    z("schnelles Zuschlagen zuvor", 135, 763, beim("zuvor", "schnelles"), "Bold", 32),
    z("BGH: auch dann betroffen (BGHSt 26, 95, 96)", 135, 815, beim("zuvor", "Bundesgerichtshof"), size=30),
    *figur_kette("ED", XS, "ft", "ernst", [("staunt", "ft4"), ("ernst", "zuvor")]),
    pl("frische Tat?", XS, 160, "ft", fill=WEISS, size=30, anker="m", bis="ft3"),
    ficon("fluent-emoji-flat", "stopwatch", XS, 380, 100, "ft2", bis="ft3"),
    pl("vor dem Eingang", XS, 160, "ft3", fill=WEISS, size=30, anker="m", anim="cut", bis=beim("ft3", "Er")),
    ficon("fluent-emoji-flat", "door", XS, 390, 100, "ft3", bis="ft4"),
    pl("betroffen (+)", XS, 160, beim("ft3", "Er"), fill=GRUEN, size=30, anker="m", anim="cut", bis="ft4"),
    pl("beobachtet", XS, 160, "ft4", fill=WEISS, size=30, anker="m", anim="cut", bis="zuvor"),
    ficon("fluent-emoji-flat", "eyes", XS, 380, 90, "ft4", bis="zuvor"),
    pl("Zuvorkommen?", XS, 160, "zuvor", fill=BLAUHELL, size=30, anker="m", anim="cut"),
    ficon("fluent-emoji-flat", "balance-scale", XS, 390, 130, "zuvor"),
]))

# F 3. Nötigungsmittel ------------------------------------------------------------------------------------------------------
folie([("nm", f"{PT} › 3. Nötigungsmittel"), ("nm2", f"{PT} › 3. Gewalt gegen eine Person"),
       ("nm5", f"{PT} › 3. Gewalt gegen eine Person (+)")], rechts_frei([
    *tafel("nm", "3. Nötigungsmittel"),
    z("wie beim Raub: Gewalt gegen eine Person oder", 110, 170, beim("nm", "Wie"), "Bold", 33),
    z("Drohung mit gegenwärtiger Gefahr für Leib oder Leben", 110, 215, beim("nm", "Drohung"), "Bold", 31),
    z("Gewalt genügt: Einwirkung auf den Körper,", 110, 285, "nm2", size=33),
    z("geeignet, nach dem Täterwillen Widerstand zu verhindern", 110, 330, beim("nm2", "geeignet"), size=31),
    fund("BGH, Beschl. v. 13.3.2002 – 1 StR 47/02, Rn. 6", 150, 378, beim("nm2", "verhindern")),
    ok(135, 455, "nm3", gr=18),
    z("Gottfried stößt Edda weg, als sie greift", 175, 435, "nm3", size=33),
    z("BGH: Wegschubsen eines Ladendetektivs = Gewalt", 110, 510, "nm4", "Bold", 33),
    fund("BGH, Urt. v. 9.3.2023 – 3 StR 392/22, Rn. 8", 150, 558, beim("nm4", "Gewalt")),
    blk(110, 615, 1040, 80, GRUENHELL, "nm5", [("Nötigungsmittel: Gewalt (+)", "ExtraBold", 36, INK)]),
    *paar("nm", go_folge=[("ernst", "nm2"), ("still", "nm3")], ed_folge=[("ernst", "nm2"), ("sorge", "nm3"), ("ernst", "nm5")]),
    pl("Gewalt oder Drohung", MB, 160, "nm", fill=WEISS, size=30, anker="m", bis="nm2"),
    ficon("fluent-emoji-flat", "warning", MB, 380, 110, "nm", bis="nm3"),
    pl("Einwirkung auf den Körper", MB, 160, "nm2", fill=WEISS, size=28, anker="m", anim="cut", bis="nm3"),
    pl("weggestoßen", MB, 160, "nm3", fill=ROTHELL, size=30, anker="m", anim="cut", bis="nm5"),
    ficon("fluent-emoji-flat", "leftwards-pushing-hand", MB, 380, 100, "nm3", bis="nm5"),
    pl("Gewalt (+)", MB, 160, "nm5", fill=GRUEN, size=30, anker="m", anim="cut"),
]))

# G 4. Subjektiv: Vorsatz, Besitzerhaltungsabsicht --------------------------------------------------------------------------
folie([("subj", f"{PT} › 4. subjektiv › Vorsatz"), ("bea", f"{PT} › 4. subjektiv › Besitzerhaltungsabsicht"),
       ("bea5", f"{PT} › 4. Besitzerhaltungsabsicht (+)")], rechts_frei([
    *tafel("subj", "4. Subjektiver Tatbestand"),
    ok(135, 190, beim("vors", "Vorsatz"), gr=18),
    z("Vorsatz, auch für das Betroffensein", 175, 170, beim("vors", "Vorsatz"), "Bold", 34),
    fund("BGH, Beschl. v. 4.8.2015 – 3 StR 112/15, Rn. 7", 175, 218, beim("vors", "betroffen")),
    z("Besitzerhaltungsabsicht:", 110, 275, "bea", "ExtraBold", 34),
    z("Gewalt, um sich im Besitz der Beute zu erhalten", 110, 322, beim("bea", "Er"), size=33),
    karte(110, 385, 505, 140, "bea2", fill=GRUENHELL, rund=18, schatten=6, rand=4),
    z("nicht einziges Motiv:", 135, 400, "bea2", "ExtraBold", 31, rechts=600),
    z("Flucht daneben schadet nicht", 135, 447, beim("bea2", "Dass"), "Bold", 28, rechts=600),
    karte(645, 385, 505, 140, "bea3", fill=ROTHELL, rund=18, schatten=6, rand=4),
    z("bloße Fluchtabsicht:", 670, 400, "bea3", "ExtraBold", 31, rechts=1135),
    z("genügt nicht", 670, 447, beim("bea3", "genügt"), "Bold", 30, rechts=1135),
    fund("BGH, Beschl. v. 4.9.2014 – 1 StR 389/14, Rn. 11", 150, 540, beim("bea3", "genügt")),
    ok(135, 615, "bea4", gr=18),
    z("stößt Edda weg, damit sie ihm die Kopfhörer", 175, 595, "bea4", size=33),
    z("nicht abnimmt, und ruft, dass er sie behält", 175, 640, beim("bea4", "ruft"), size=33),
    blk(110, 700, 1040, 80, GRUENHELL, "bea5", [("Besitzerhaltungsabsicht (+)", "ExtraBold", 36, INK)]),
    *figur_kette("GO", XS, "subj", "ernst", [("listig", "bea"), ("ernst", "bea2"), ("listig", "bea4"), ("still", "bea5")]),
    pl("Vorsatz", XS, 160, "vors", fill=WEISS, size=30, anker="m", bis="bea"),
    ficon("tabler", "brain", XS, 380, 100, "subj", fuell=GELB, bis="bea"),
    pl("Beute behalten", XS, 160, "bea", fill=LILA, size=30, anker="m", anim="cut", bis="bea2"),
    kh(XS, 380, 100, "bea", bis="bea2"),
    pl("auch Flucht: unschädlich", XS, 160, "bea2", fill=GRUENHELL, size=28, anker="m", anim="cut", bis="bea3"),
    pl("nur Flucht: nein", XS, 160, "bea3", fill=ROTHELL, size=30, anker="m", anim="cut", bis="bea4"),
    ficon("tabler", "arrow-right", XS, 370, 100, "bea2", bis="bea4"),
    pl("„Die Kopfhörer behalte ich!“", XS, 160, "bea4", fill=WEISS, size=26, anker="m", anim="cut", bis="bea5"),
    kh(XS, 380, 100, "bea4", anim="cut"),
    pl("Absicht (+)", XS, 160, "bea5", fill=GRUEN, size=30, anker="m", anim="cut"),
]))

# H Ergebnis, Rechtsfolge, Konkurrenzen ---------------------------------------------------------------------------------------
folie([("rs", "A. § 252 StGB › II. Rechtswidrigkeit, III. Schuld"), ("erg", "Ergebnis · Gottfried: § 252 StGB"),
       ("folge", "Rechtsfolge › gleich einem Räuber"), ("konk", "Konkurrenzen › § 242 tritt zurück")], rechts_frei([
    *tafel("rs", "Ergebnis und Rechtsfolge"),
    ok(135, 190, beim("rs", "Schuld"), gr=18),
    z("II. Rechtswidrigkeit, III. Schuld (+)", 175, 170, "rs", "Bold", 34),
    karte(110, 245, 1040, 100, "erg", fill=GRUENHELL, rund=18, schatten=6, rand=4),
    z("Gottfried: räuberischer Diebstahl, § 252 StGB", 140, 272, "erg", "ExtraBold", 35),
    z("Rechtsfolge: gleich einem Räuber", 110, 390, "folge", "ExtraBold", 34),
    z("Strafrahmen des Raubes, § 249", 150, 440, beim("folge", "Strafrahmen"), size=33),
    z("Qualifikationen §§ 250, 251 anwendbar", 150, 490, "qual", size=33),
    fund("BGH, Urt. v. 9.3.2023 – 3 StR 392/22, Rn. 8; BGH 3 StR 52/02, Rn. 16", 150, 538, beim("qual", "anwendbar")),
    z("Konkurrenzen: § 242 tritt zurück", 110, 610, "konk", "ExtraBold", 34),
    fund("BGH, Beschl. v. 22.11.2012 – 1 StR 378/12, Rn. 9", 150, 658, beim("konk", "zurück")),
    *figur_kette("GO", XS, "rs", "ernst", [("still", "erg")]),
    pl("Schuld (+)", XS, 160, beim("rs", "Schuld"), fill=WEISS, size=30, anker="m", bis="erg"),
    pl("§ 252 (+)", XS, 160, "erg", fill=GRUEN, size=30, anker="m", anim="cut", bis="folge"),
    ficon("tabler", "gavel", XS, 380, 110, "erg", fuell=GELB, bis="konk"),
    pl("gleich einem Räuber", XS, 160, "folge", fill=ROTHELL, size=30, anker="m", anim="cut", bis="qual"),
    pl("§§ 250, 251", XS, 160, "qual", fill=WEISS, size=30, anker="m", anim="cut", bis="konk"),
    pl("§ 242 tritt zurück", XS, 160, "konk", fill=WEISS, size=30, anker="m", anim="cut"),
    ficon("fluent-emoji-flat", "balance-scale", XS, 390, 130, "konk"),
]))

# I Gegenvariante ------------------------------------------------------------------------------------------------------------
folie([("gv", "Gegenvariante › Beute weggeworfen"), ("gv2", "Gegenvariante › Besitzerhaltungsabsicht (−)"),
       ("gv3", "Gegenvariante › Diebstahl, § 242 StGB")], rechts_frei([
    *tafel("gv", "Gegenvariante: nur Flucht", fill=BLAUHELL),
    z("Gottfried wirft die Kopfhörer weg", 110, 175, beim("gv", "Gottfried"), "Bold", 34),
    z("und stößt Edda nur, um zu entkommen", 110, 222, beim("gv", "stößt"), "Bold", 34),
    nein(135, 315, "gv2", gr=18),
    z("Besitzerhaltungsabsicht (−)", 175, 295, "gv2", "ExtraBold", 34),
    blk(110, 375, 1040, 80, ROTHELL, beim("gv2", "kein"), [("kein räuberischer Diebstahl", "ExtraBold", 36, INK)]),
    fund("BGH, Beschl. v. 4.9.2014 – 1 StR 389/14, Rn. 11", 150, 470, beim("gv2", "kein")),
    z("es bleibt beim Diebstahl, § 242", 110, 545, "gv3", "Bold", 34),
    z("den Stoß gesondert prüfen", 110, 595, beim("gv3", "Stoß"), size=33),
    *figur_kette("GO", XS, "gv", "ertappt", [("entschlossen", "gv2"), ("still", "gv3")]),
    pl("Kopfhörer weggeworfen", XS, 160, "gv", fill=WEISS, size=28, anker="m", bis="gv2"),
    kh(XS - 190, BR, 80, beim("gv", "weg")),
    pl("nur Flucht", XS, 160, "gv2", fill=ROTHELL, size=30, anker="m", anim="cut", bis="gv3"),
    ficon("tabler", "arrow-right", XS, 370, 100, "gv2", bis="gv3"),
    pl("Diebstahl", XS, 160, "gv3", fill=WEISS, size=30, anker="m", anim="cut"),
]))

# J Klausurtipp (Lexi) -------------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · Besitzerhaltungsabsicht"), ("tipp3", "Klausurtipp · Anhaltspunkte im Sachverhalt")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Knackpunkt: Besitzerhaltungsabsicht", 200, 200, beim("tipp", "Die"), "ExtraBold", 36),
    z("Flucht mit der Beute beweist sie", 200, 290, "tipp2", "Bold", 34),
    z("allein nicht", 200, 337, beim("tipp2", "allein"), "Bold", 34),
    fund("BGH, Beschl. v. 4.9.2014 – 1 StR 389/14, Rn. 12, 15", 240, 390, beim("tipp2", "nicht")),
    z("Kam es ihm gerade auf die Beute an?", 200, 465, "tipp3", size=34),
    z("etwa: verteidigt sie gegen einen Zugriff", 200, 555, "tipp4", "Bold", 34),
    z("oder will sie ausdrücklich behalten", 200, 602, beim("tipp4", "ausdrücklich"), "Bold", 34),
    *redet("LX_warnt", LXX, BR, FR_H + 60, "tipp", "sch"),
    namensschild("Lexi", LXX, BR, "tipp", GELB, d=0.2),
])

# K Klausurschema -------------------------------------------------------------------------------------------------------------
K1, K2, K3 = 150, 230, 310
PSS = "Klausurschema"
folie([("sch", PSS), ("s_i", f"{PSS} › I. Tatbestand"), ("s1", f"{PSS} › I. 1. Vortat"), ("s2", f"{PSS} › I. 2. frische Tat"),
       ("s3", f"{PSS} › I. 3. Nötigungsmittel"), ("s4", f"{PSS} › I. 4. subjektiv"), ("s_ii", f"{PSS} › II. Rechtswidrigkeit"),
       ("s_iii", f"{PSS} › III. Schuld"), ("s_iv", f"{PSS} › Rechtsfolge")], [
    karte(60, 50, 1800, 920, "sch"),
    titel("Klausurschema: Räuberischer Diebstahl, § 252 StGB", 110, 90, "sch", 50),
    z("I. Tatbestand", K1, 180, "s_i", "Bold", 38, rechts=1820),
    z("1. Vortat: vollendeter, nicht beendeter Diebstahl", K2, 240, "s1", size=34, rechts=1820),
    z("2. bei dem Diebstahl auf frischer Tat betroffen", K2, 295, "s2", size=34, rechts=1820),
    z("3. Gewalt gegen eine Person oder Drohung mit gegenwärtiger Gefahr für Leib oder Leben", K2, 350, "s3", size=33,
      rechts=1820),
    z("4. subjektiv", K2, 405, "s4", size=34, rechts=1820),
    z("a) Vorsatz", K3, 455, beim("s4", "Vorsatz"), size=34, rechts=1820),
    z("b) Besitzerhaltungsabsicht", K3, 505, "s5", size=34, rechts=1820),
    z("II. Rechtswidrigkeit", K1, 580, "s_ii", "Bold", 38, rechts=1820),
    z("III. Schuld", K1, 648, "s_iii", "Bold", 38, rechts=1820),
    z("Rechtsfolge: gleich einem Räuber", K1, 730, beim("s_iv", "Rechtsfolge"), "Bold", 38, rechts=1820),
    z("ggf. §§ 250, 251", K2, 790, beim("s_iv", "wenn"), size=34, rechts=1820),
])

# L Merksatz (Lexi) ------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 170, "merke", 84, anker="m"),
    *markertext([[("Nach ", 0), ("vollendetem Diebstahl", "a"), (" auf frischer Tat", 0)],
                 [("betroffen und Gewalt, um die ", 0), ("Beute zu behalten", "b"), (":", 0)],
                 [("gleich einem Räuber", "c"), (" bestraft.", 0)]], 750, 275, 42, "merke",
                {"a": beim("merke", "vollendetem"), "b": beim("merke", "Beute"), "c": beim("merke", "gleich")}),
    *markertext([[("Wer ", 0), ("nur fliehen", "d"), (" will:", 0)], [("kein räuberischer Diebstahl.", 0)]],
                750, 560, 42, "m_2", {"d": beim("m_2", "nur")}),
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
