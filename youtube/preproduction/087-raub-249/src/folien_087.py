"""Folge 087 · Raub § 249 StGB: Prüfungsschema mit Gewalt, Wegnahme & Finalität – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A1 Fall vorher (Weg vom Wochenmarkt zur Bushaltestelle, Margit mit Handtasche, Hagen),
A2 Fall nachher (Stoß nur als Warnsymbol, Tasche am Boden, Hagen rennt mit der Tasche davon, Margit unverletzt, Frage),
B Sachverhalt, C Wortlaut § 249 Abs. 1 und Aufbau, D fremde bewegliche Sache und Wegnahme (Verweis auf Folge 051),
E qualifiziertes Nötigungsmittel (Unterschied zu § 240, Gewalt gegen eine Person), F finaler Zusammenhang, G Abwandlung 1
(Gewalt aus Wut, Entschluss danach), H Abgrenzung §§ 252, 255, I subjektiver Tatbestand, J Ergebnis und §§ 250, 251,
K Abwandlung 2 (Entreißen), L Klausurtipp (Lexi), M Klausurschema, N Merksatz (Lexi).
Zurückhaltend: kein Stoß, kein Sturz, keine Verletzung im Bild; Margit respektvoll (erschrocken, nicht leidend), Hagen
gewöhnlich gekleidet, keine Karikatur. Zahlen auf Tafeln, Pillen und Blasen als Ziffern.
Geräusch nur bei sichtbarer Handlung: Laufschritte, als Hagen mit der Tasche davonrennt (szene_087laufen_1, Freesound CC0)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import wave as _wave

bausteine.FIGORDNER = "op_087/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
LILAHELL = (246, 243, 255, 255)
ROTHELL = (253, 232, 228, 255)
GRUENHELL = (232, 247, 233, 255)
BLAUHELL = (233, 241, 253, 255)
DAUER = bausteine._cj()["dauer"]
NULL = "fall"                     # Szene A1 steht ab 0,0 s (render_087 setzt alle Elemente bis zur Marke „fall“ auf 0,0 s)

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
    """Wortlautkarte: wörtliches Zitat (gesetze-im-internet.de, Abruf 02.10.2026) in einer hellen Karte, Fundstelle darunter
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
SCHILD = {"MG": ("Margit", BLAU), "HG": ("Hagen", GRUEN)}


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


def paar(cue, mg_folge=(), hg_folge=(), mg="ruhig", hg="ruhig"):
    """Hagen bei X1 (seine ausgestreckte Hand zeigt zur Tafel, nicht auf Margit), Margit bei X2; beide blicken zur Tafel."""
    return figur_kette("HG", X1, cue, hg, hg_folge) + figur_kette("MG", X2, cue, mg, mg_folge, d=0.2, schild_d=0.3)


def tasche(cx, unten, breite, cue, bis=None, anim="pop", d=0.0):
    """Die Handtasche (Fluent Emoji „handbag“)."""
    return ficon("fluent-emoji-flat", "handbag", cx, unten, breite, cue, bis=bis, anim=anim, d=d)


def kulisse(cue):
    """Weg vom Wochenmarkt zur Bushaltestelle: Boden, Marktstand links, Baum, Bushaltestelle rechts."""
    return [
        linienzug([(60, BODEN), (1860, BODEN)], cue, breite=7, farbe=INK),
        karte(90, 700, 300, 180, cue, fill=WEISS, rund=12, schatten=6, rand=5),
        ficon("fluent-emoji-flat", "basket", 170, 700, 110, cue),
        ficon("fluent-emoji-flat", "red-apple", 290, 700, 64, cue),
        ficon("fluent-emoji-flat", "carrot", 350, 700, 50, cue),
        pl("Wochenmarkt", 240, 790, cue, fill=GELB, size=28, anker="m"),
        ficon("fluent-emoji-flat", "deciduous-tree", 1010, BODEN, 230, cue),
        ficon("fluent-emoji-flat", "bus-stop", 1780, BODEN, 150, cue),
    ]


def bewegungslinien(x, y, cue, bis=None, n=3, laenge=70, abstand=26):
    """Dezente Bewegungslinien hinter einer laufenden Figur (nur Striche, kein Aufprall)."""
    return [bis_(linienzug([(x - laenge, y + i * abstand), (x, y + i * abstand)], cue, breite=5, farbe=TEXT), bis)
            for i in range(n)]


# A1 Fall vorher: Weg vom Wochenmarkt zur Bushaltestelle ---------------------------------------------------------------------
GX, RX, FH = 620, 1330, 540             # Margit (blickt nach rechts), Hagen (blickt nach links)
MGa = ("MG_ruhig_r", GX, BODEN, FH)
HGb = ("HG_redet", RX, BODEN, FH)
Z0 = beim("stoss", "stößt")             # A2 beginnt beim Wort „stößt“ (Hagens Satz endet vor der Schiebeblende)
folie([(NULL, "Fall · Auf dem Weg zum Bus"), ("hagen", "Fall · Hagen hat Margit gesehen")], [
    *kulisse(NULL),
    pl("Dienstagnachmittag", 100, 64, NULL, fill=GELB, size=32),
    pl("Bushaltestelle", 1720, 930, beim("fall", "Bushaltestelle"), fill=WEISS, size=28, anker="m"),
    *figur_kette("MG", GX, NULL, "ruhig_r", [("froh_r", "geld"), ("ruhig_r", "hagen")], unten=BODEN, hoehe=FH,
                 schild=False),
    namensschild("Margit", GX, BODEN - 8, NULL, BLAU),
    tasche(GX + 70, BODEN - 300, 95, NULL),
    pl("Handtasche über der Schulter", GX, 230, beim("margit", "Handtasche"), fill=WEISS, size=28, anker="m", bis="geld"),
    ficon("fluent-emoji-flat", "purse", GX + 250, 600, 70, "geld"),
    pl("Geldbörse · 80 €", GX + 250, 470, "geld", fill=GELB, size=30, anker="m"),
    peep_voll("HG_listig", RX, BODEN, FH, "hagen", bis="h1"),
    namensschild("Hagen", RX, BODEN - 8, "hagen", GRUEN, d=0.2),
    pl("hat sie beim Bezahlen gesehen", RX, 230, beim("hagen", "Bezahlen"), fill=WEISS, size=28, anker="m", bis="h1"),
    *redet("HG_redet", RX, BODEN, FH, "h1", "stoss"),
    blase("sprech", 600, 170, "h1", 1330, 190, inhalt=["Die Handtasche hole ich mir."], textsize=34, figur=HGb, bis="stoss"),
    peep_voll("HG_entschlossen", RX, BODEN, FH, "stoss", anim="cut"),
    pl("läuft auf Margit zu", RX, 230, "stoss", fill=PINK, size=28, anker="m"),
])

# A2 Fall nachher: der Stoß nur als Warnsymbol, Tasche weg, Margit unverletzt, Frage ------------------------------------------
TX = 700                                # Tasche am Boden (wo Margit stand)
HR = 1560                               # Hagen läuft nach rechts davon
W0 = beim("weg", "rennt")
folie([(Z0, "Fall · Der Stoß"), (beim("nimmt", "nimmt"), "Fall · Hagen nimmt die Handtasche"),
       ("schreck", "Fall · Margit steht wieder auf"), ("frage", "Fall · Die Frage")], [
    *kulisse(Z0),
    ficon("fluent-emoji-flat", "warning", 440, 640, 150, Z0, bis="schreck"),
    pl("stößt Margit zu Boden", 440, 300, Z0, fill=ROTHELL, size=30, anker="m", bis="schreck"),
    pl("um an die Tasche zu kommen", 440, 370, beim("stoss", "um"), fill=WEISS, size=28, anker="m", bis="schreck"),
    tasche(TX, BODEN - 4, 95, Z0, bis=beim("nimmt", "nimmt")),
    # Hagen nimmt die Tasche und rennt davon
    *figur_kette("HG", 800, beim("nimmt", "nimmt"), "entschlossen", bis=W0, unten=BODEN, hoehe=FH, schild=False),
    namensschild("Hagen", 800, BODEN - 8, beim("nimmt", "nimmt"), GRUEN, d=0.1, bis=W0),
    tasche(720, BODEN - 215, 95, beim("nimmt", "nimmt"), bis=W0, anim="cut"),
    szene(bewegt(peep_voll("HG_entschlossen_r", HR, BODEN, FH, W0, anim="cut"), W0, beim("weg", "davon", ende=True), -480, 0),
          "087laufen_1", 0.8),
    bewegt(namensschild("Hagen", HR, BODEN - 8, W0, GRUEN, anim="cut"), W0, beim("weg", "davon", ende=True), -480, 0),
    bewegt(tasche(HR + 95, BODEN - 215, 95, W0, anim="cut"), W0, beim("weg", "davon", ende=True), -480, 0),
    *bewegungslinien(HR - 150, 470, beim("weg", "davon", ende=True), bis="frage"),
    pl("will sie samt Geld behalten", HR, 230, beim("weg", "behalten"), fill=PINK, size=28, anker="m", bis="frage"),
    # Margit steht wieder auf: erschrocken, nicht verletzt
    *figur_kette("MG", GX - 60, "schreck", "erschrickt_r", [("sorge_r", beim("schreck", "verletzt"))], bis="m1",
                 unten=BODEN, hoehe=FH, schild=False),
    namensschild("Margit", GX - 60, BODEN - 8, "schreck", BLAU, d=0.1),
    pl("erschrocken, nicht verletzt", GX - 60, 230, beim("schreck", "erschrocken"), fill=WEISS, size=28, anker="m", bis="m1"),
    *redet("MG_redet_r", GX - 60, BODEN, FH, "m1", "frage"),
    blase("sprech", 520, 170, "m1", 700, 200, inhalt=["Meine Tasche ist weg!"], textsize=36,
          figur=("MG_redet_r", GX - 60, BODEN, FH), bis="frage"),
    peep_voll("MG_ernst_r", GX - 60, BODEN, FH, "frage", anim="cut"),
    pl("Hat Hagen einen Raub begangen?", 1080, 200, "frage", fill=PINK, size=38, anker="m"),
    pl("§ 249 Schritt für Schritt", 940, 300, beim("frage2", "Paragraf"), fill=WEISS, size=30, anker="m"),
    pl("2 Abwandlungen", 1300, 300, beim("frage2", "zwei"), fill=GELB, size=30, anker="m"),
])

# B Sachverhalt -------------------------------------------------------------------------------------------------------------
sachverhalt_klein("sv", [
    "Dienstagnachmittag auf dem Weg vom Wochenmarkt zur Bushaltestelle: Margit trägt ihre Handtasche über der Schulter, "
    "darin ihre Geldbörse mit 80 €. Hagen hat sie am Marktstand beim Bezahlen gesehen. Um an die Tasche zu kommen, stößt er "
    "Margit zu Boden, nimmt die Handtasche und rennt davon. Er will sie samt Geld behalten. Margit hat sich erschrocken, "
    "verletzt ist sie nicht.",
    "Abwandlung 1: Hagen stößt Margit nur aus Wut, weil sie ihn angerempelt hat. Erst als die Tasche am Boden liegt, "
    "beschließt er, sie mitzunehmen.",
    "Abwandlung 2: Hagen kommt von hinten und reißt Margit die locker hängende Tasche im Vorbeilaufen von der Schulter, "
    "ehe sie reagieren kann.",
], "Hat sich Hagen nach § 249 StGB strafbar gemacht?")

# C Wortlaut § 249 Abs. 1 und Aufbau -------------------------------------------------------------------------------------------
W1 = [[("„Wer mit ", 0), ("Gewalt gegen eine Person", "a"), (" oder unter Anwendung von", 0)],
      [("Drohungen mit gegenwärtiger Gefahr für Leib oder Leben", "d"), (" eine", 0)],
      [("fremde bewegliche Sache", "b"), (" einem anderen in der Absicht ", 0), ("wegnimmt", "c"), (",", 0)],
      [("die Sache sich oder einem Dritten ", 0), ("rechtswidrig zuzueignen", "e"), (", wird", 0)],
      [("mit Freiheitsstrafe nicht unter einem Jahr bestraft.“", 0)]]
PO = "A. § 249 StGB › I. Tatbestand › 1. objektiv"
PS_ = "A. § 249 StGB › I. Tatbestand › 2. subjektiv"
folie([("p249", "A. Raub, § 249 StGB › Wortlaut"), ("aufbau", "A. Raub, § 249 StGB › Aufbau")], rechts_frei([
    *tafel("p249", "Raub: § 249 Abs. 1 StGB"),
    *wortlaut(100, 175, 1060, 245, "p249", W1, 30,
              {"a": beim("p249w", "Gewalt"), "d": beim("p249w", "Drohungen"), "b": beim("p249w", "fremde"),
               "c": beim("p249w", "wegnimmt"), "e": beim("p249w", "rechtswidrig")}, "§ 249 Abs. 1 StGB",
              farben={"a": GELB, "d": GELB, "b": BLAU, "c": BLAU, "e": LILA}),
    blk(110, 480, 1040, 80, GELB, "aufbau", [("Wegnahme + qualifiziertes Nötigungsmittel", "ExtraBold", 34, INK)]),
    blk(110, 590, 505, 200, GRUEN, "obj", [("objektiv", "ExtraBold", 32, INK), ("Sache, Wegnahme,", "Bold", 30, INK),
                                           ("Nötigungsmittel, Finalität", "Bold", 30, INK)]),
    blk(645, 590, 505, 200, BLAU, "subj", [("subjektiv", "ExtraBold", 32, INK), ("Vorsatz,", "Bold", 30, INK),
                                           ("Zueignungsabsicht", "Bold", 30, INK)]),
    *paar("p249", mg_folge=[("ernst", "aufbau")], hg_folge=[("ernst", "obj")]),
    pl("§ 249 StGB", MB, 160, "p249", fill=WEISS, size=30, anker="m", bis="aufbau"),
    ficon("fluent-emoji-flat", "balance-scale", MB, 390, 130, "p249", bis="aufbau"),
    pl("Wegnahme + Nötigung", MB, 160, "aufbau", fill=GELB, size=30, anker="m", anim="cut"),
    tasche(MB - 70, 390, 100, "aufbau", anim="cut"),
    ficon("fluent-emoji-flat", "warning", MB + 70, 390, 100, "aufbau", anim="cut"),
]))

# D Fremde bewegliche Sache und Wegnahme -----------------------------------------------------------------------------------------
folie([("sache", f"{PO} › a) fremde bewegliche Sache"), ("wegn", f"{PO} › b) Wegnahme"),
       ("wegok", f"{PO} › b) Wegnahme (+)")], rechts_frei([
    *tafel("sache", "Sache und Wegnahme"),
    ok(135, 200, beim("sache", "fremde"), gr=20),
    z("Handtasche: fremde bewegliche Sache", 175, 180, beim("sache", "Handtasche"), "Bold", 34),
    z("gehört Margit", 175, 225, beim("sache", "gehört"), size=33),
    z("Wegnahme: Bruch fremden und Begründung", 110, 305, "wegn", "Bold", 34),
    z("neuen Gewahrsams", 110, 350, beim("wegn", "Begründung"), "Bold", 34),
    fund("BGH, Beschl. v. 3.3.2021 – 4 StR 338/20, Rn. 5", 150, 400, beim("wegn", "Gewahrsams")),
    blk(110, 450, 1040, 80, LILAHELL, beim("wegn", "Einzelheiten"), [("Einzelheiten: unsere Folge zum Diebstahl", "Bold", 33, INK)]),
    z("Hagen nimmt Margit die Tasche gegen ihren Willen ab", 110, 570, "wegn2", size=33),
    z("und rennt damit davon: neuer Gewahrsam", 110, 615, beim("wegn2", "rennt"), size=33),
    blk(110, 680, 1040, 80, GRUENHELL, "wegok", [("Wegnahme (+)", "ExtraBold", 36, INK)]),
    *paar("sache", mg_folge=[("ernst", "wegn2")], hg_folge=[("ernst", "wegn"), ("still", "wegok")]),
    pl("gehört Margit", MB, 160, beim("sache", "gehört"), fill=BLAU, size=30, anker="m", bis="wegn"),
    tasche(MB, 390, 120, "sache", bis="wegn2"),
    pl("Gewahrsam", MB, 160, "wegn", fill=WEISS, size=30, anker="m", anim="cut", bis="wegn2"),
    ficon("tabler", "hand-grab", MB + 90, 300, 70, "wegn", fuell=WEISS, bis="wegn2"),
    pl("gegen ihren Willen", MB, 160, "wegn2", fill=ROTHELL, size=30, anker="m", anim="cut", bis="wegok"),
    tasche(MB + 60, 390, 100, "wegn2", anim="cut"),
    ficon("tabler", "arrow-right", MB - 70, 370, 70, beim("wegn2", "rennt")),
    pl("Wegnahme (+)", MB, 160, "wegok", fill=GRUEN, size=30, anker="m", anim="cut"),
]))

# E Qualifiziertes Nötigungsmittel -----------------------------------------------------------------------------------------------
folie([("nm", f"{PO} › c) Nötigungsmittel"), ("quali", f"{PO} › c) qualifiziertes Nötigungsmittel"),
       ("gdef", f"{PO} › c) Gewalt gegen eine Person"), (beim("g_ja", "Gewalt"), f"{PO} › c) Gewalt gegen eine Person (+)")], rechts_frei([
    *tafel("nm", "Qualifiziertes Nötigungsmittel"),
    z("anders als § 240: nicht jedes empfindliche Übel", 110, 175, "nm2", "Bold", 33),
    karte(110, 235, 505, 140, beim("quali", "Gewalt"), fill=GELB, rund=18, schatten=6, rand=4),
    z("Gewalt gegen", 135, 252, beim("quali", "Gewalt"), "ExtraBold", 32, rechts=600),
    z("eine Person", 135, 300, beim("quali", "Gewalt"), "ExtraBold", 32, rechts=600),
    karte(645, 235, 505, 140, beim("quali", "Drohung"), fill=GELB, rund=18, schatten=6, rand=4),
    z("Drohung: gegenwärtige", 670, 252, beim("quali", "Drohung"), "ExtraBold", 32, rechts=1135),
    z("Gefahr für Leib, Leben", 670, 300, beim("quali", "Drohung"), "ExtraBold", 32, rechts=1135),
    nein(135, 425, "anzeige", gr=18),
    z("nur Drohung mit einer Anzeige: kein Raub", 175, 405, "anzeige", size=33),
    z("Gewalt: Kraft des Täters ist wesentlicher", 110, 480, "gdef", "Bold", 33),
    z("Bestandteil der Wegnahme,", 110, 525, beim("gdef", "Bestandteil"), "Bold", 33),
    z("vom Opfer als körperlicher Zwang empfunden", 110, 570, "gdef2", "Bold", 33),
    fund("BGH, Beschl. v. 26.1.2022 – 3 StR 445/21, Rn. 5, 8", 150, 620, beim("gdef2", "empfunden")),
    ok(135, 700, beim("g_ja", "Gewalt"), gr=20),
    blk(175, 670, 975, 80, GRUENHELL, beim("g_ja", "Gewalt"), [("Stoß zu Boden: Gewalt gegen eine Person (+)", "ExtraBold", 32, INK)]),
    *paar("nm", mg_folge=[("ernst", "quali"), ("sorge", "g_ja")], hg_folge=[("ernst", "quali"), ("still", "g_ja")]),
    pl("nicht jedes Übel", MB, 160, "nm2", fill=WEISS, size=30, anker="m", bis="quali"),
    ficon("fluent-emoji-flat", "balance-scale", MB, 390, 130, "nm2", bis="quali"),
    pl("qualifiziert", MB, 160, "quali", fill=GELB, size=30, anker="m", anim="cut", bis="anzeige"),
    ficon("fluent-emoji-flat", "warning", MB, 380, 110, "quali", anim="cut", bis="anzeige"),
    pl("Anzeige: kein Raub", MB, 160, "anzeige", fill=ROTHELL, size=30, anker="m", anim="cut", bis="gdef"),
    ficon("tabler", "file-alert", MB, 380, 100, "anzeige", fuell=WEISS, anim="cut", bis="gdef"),
    pl("körperlicher Zwang", MB, 160, "gdef", fill=WEISS, size=30, anker="m", anim="cut", bis=beim("g_ja", "Gewalt")),
    ficon("fluent-emoji-flat", "leftwards-pushing-hand", MB, 380, 100, "gdef", anim="cut"),
    pl("Gewalt (+)", MB, 160, beim("g_ja", "Gewalt"), fill=GRUEN, size=30, anker="m", anim="cut"),
]))

# F Finaler Zusammenhang ------------------------------------------------------------------------------------------------------
folie([("final", f"{PO} › d) finaler Zusammenhang"), ("fvor", f"{PO} › d) Finalität: Vorstellung des Täters"),
       (beim("f_ja", "Finalität"), f"{PO} › d) Finalität (+)")], rechts_frei([
    *tafel("final", "Finaler Zusammenhang"),
    z("Die Gewalt muss das Mittel sein,", 110, 175, "fdef", "Bold", 34),
    z("um die Wegnahme zu ermöglichen", 110, 220, beim("fdef", "Weck"), "Bold", 34),
    fund("BGH, Beschl. v. 20.3.2024 – 6 StR 572/23, Rn. 5", 150, 270, beim("fdef", "ermöglichen")),
    blk(110, 320, 330, 80, GELB, beim("fdef", "Mittel"), [("Gewalt", "ExtraBold", 34, INK)]),
    pfeil(460, 360, 770, 360, beim("fdef", "Weck"), breite=8, kopf=24),
    pl("um zu", 540, 300, beim("fdef", "Weck"), fill=WEISS, size=28),
    blk(790, 320, 360, 80, BLAU, beim("fdef", "Weck"), [("Wegnahme", "ExtraBold", 34, INK)]),
    z("maßgeblich: die Vorstellung des Täters", 110, 445, "fvor", "Bold", 34),
    fund("BGH, Urt. v. 20.1.2016 – 1 StR 398/15, Rn. 17", 150, 495, beim("fvor", "Vorstellung")),
    ok(135, 570, "f_ja", gr=20),
    z("Hagen stößt, um an die Tasche zu kommen,", 175, 550, "f_ja", size=33),
    z("und nimmt sie gleich danach", 175, 595, beim("f_ja", "nimmt"), size=33),
    blk(110, 660, 1040, 80, GRUENHELL, beim("f_ja", "Finalität"), [("Finalität (+)", "ExtraBold", 36, INK)]),
    *paar("final", mg_folge=[("ernst", "fvor")], hg_folge=[("ernst", "fdef"), ("listig", "fvor"), ("still", "f_ja")]),
    pl("Kern: Finalität", MB, 160, "final", fill=GELB, size=30, anker="m", bis="fdef"),
    ficon("fluent-emoji-flat", "link", MB, 390, 120, "final", bis="fvor"),
    pl("Gewalt als Mittel", MB, 160, "fdef", fill=WEISS, size=30, anker="m", anim="cut", bis="fvor"),
    pl("Vorstellung des Täters", MB, 160, "fvor", fill=WEISS, size=30, anker="m", anim="cut", bis=beim("f_ja", "Finalität")),
    ficon("tabler", "bulb", MB, 380, 100, "fvor", fuell=GELB, anim="cut", bis="f_ja"),
    tasche(MB, 390, 110, "f_ja", anim="cut"),
    pl("Finalität (+)", MB, 160, beim("f_ja", "Finalität"), fill=GRUEN, size=30, anker="m", anim="cut"),
]))

# G Abwandlung 1: Gewalt aus Wut, Entschluss erst danach -----------------------------------------------------------------------
PA1 = "Abwandlung 1 › Gewalt aus Wut"
folie([("ab1", PA1), ("ab1c", "Abwandlung 1 › Finalität (−)"), ("ab1e", "Abwandlung 1 › Diebstahl, § 242 StGB")], rechts_frei([
    *tafel("ab1", "Abwandlung 1: Gewalt aus Wut", fill=BLAUHELL),
    z("Hagen stößt Margit nur aus Wut,", 110, 175, "ab1", "Bold", 34),
    z("weil sie ihn angerempelt hat", 110, 220, beim("ab1", "weil"), size=33),
    z("Entschluss zur Wegnahme erst danach", 110, 290, "ab1b", "Bold", 34),
    nein(135, 380, "ab1c", gr=18),
    z("Gewalt nicht Mittel zur Wegnahme:", 175, 360, "ab1c", size=33),
    z("Finalität (−)", 175, 405, beim("ab1c", "Gewalt"), "ExtraBold", 34),
    z("Wirkung früherer Gewalt bloß ausnutzen:", 110, 480, "ab1d", "Bold", 33),
    z("genügt nicht", 110, 525, beim("ab1d", "ausnutzt"), "Bold", 33),
    fund("BGH 6 StR 572/23, Rn. 5; BGH, Beschl. v. 24.10.2024 – 4 StR 368/24, Rn. 7", 150, 575, beim("ab1d", "ausnutzt")),
    blk(110, 630, 1040, 80, ROTHELL, "ab1e", [("kein Raub: Diebstahl, § 242 StGB", "ExtraBold", 36, INK)]),
    z("den Stoß gesondert prüfen", 110, 740, beim("ab1e", "Stoß"), size=33),
    *paar("ab1", mg="sorge", mg_folge=[("ernst", "ab1c")], hg="wut", hg_folge=[("listig", "ab1b"), ("ernst", "ab1c")]),
    pl("aus Wut", MB, 160, "ab1", fill=ROTHELL, size=30, anker="m", bis="ab1b"),
    ficon("fluent-emoji-flat", "cloud-with-lightning", MB, 380, 120, "ab1", bis="ab1b"),
    pl("erst danach", MB, 160, "ab1b", fill=WEISS, size=30, anker="m", anim="cut", bis="ab1c"),
    ficon("tabler", "clock", MB - 70, 380, 90, "ab1b", fuell=WEISS, anim="cut", bis="ab1c"),
    tasche(MB + 70, 380, 90, "ab1b", anim="cut", bis="ab1c"),
    pl("Finalität (−)", MB, 160, "ab1c", fill=ROTHELL, size=30, anker="m", anim="cut", bis="ab1e"),
    ficon("fluent-emoji-flat", "broken-chain", MB, 380, 120, "ab1c", anim="cut", bis="ab1e"),
    pl("Diebstahl", MB, 160, "ab1e", fill=WEISS, size=30, anker="m", anim="cut"),
    tasche(MB, 380, 100, "ab1e", anim="cut"),
]))

# H Abgrenzung: §§ 252, 255 ----------------------------------------------------------------------------------------------------
folie([("p252", "Abgrenzung › räuberischer Diebstahl, § 252 StGB"),
       ("p255", "Abgrenzung › räuberische Erpressung, § 255 StGB")], rechts_frei([
    *tafel("p252", "Abgrenzung: §§ 252, 255 StGB", size=44),
    z("Gewalt erst nach der Wegnahme, um die Beute", 110, 175, "p252", "Bold", 33),
    z("zu behalten: räuberischer Diebstahl, § 252", 110, 220, beim("p252", "behalten"), "Bold", 33),
    nein(135, 300, "flucht", gr=18),
    z("nur Flucht: dafür fehlt die nötige Absicht", 175, 280, "flucht", size=33),
    fund("BGH, Beschl. v. 4.9.2014 – 1 StR 389/14, Rn. 11", 175, 328, beim("flucht", "Absicht")),
    z("Opfer gibt die Sache unter Gewalt selbst heraus:", 110, 395, "p255", "Bold", 33),
    z("räuberische Erpressung, § 255", 110, 440, beim("p255", "räuberische"), "Bold", 33),
    karte(110, 510, 505, 200, "streit", fill=BLAUHELL, rund=18, schatten=6, rand=4),
    z("BGH: äußeres", 135, 525, "streit", "ExtraBold", 32, rechts=600),
    z("Erscheinungsbild,", 135, 572, beim("streit", "Erscheinungsbild"), "Bold", 32, rechts=600),
    z("Nehmen oder Geben", 135, 619, beim("streit", "Nehmen"), "Bold", 32, rechts=600),
    karte(645, 510, 505, 200, beim("streit", "weite"), fill=LILAHELL, rund=18, schatten=6, rand=4),
    z("weite Teile der Lehre:", 670, 525, beim("streit", "weite"), "ExtraBold", 32, rechts=1135),
    z("Vermögens-", 670, 572, beim("streit", "Vermögensverfügung"), "Bold", 32, rechts=1135),
    z("verfügung nötig", 670, 619, beim("streit", "Vermögensverfügung"), "Bold", 32, rechts=1135),
    fund("BGH, Beschl. v. 24.4.2018 – 5 StR 606/17, Rn. 13", 150, 730, beim("streit", "Erscheinungsbild")),
    *figur_kette("HG", XS, "p252", "ernst", [("still", "p255")]),
    pl("Beute behalten: § 252", XS, 160, "p252", fill=WEISS, size=30, anker="m", bis="flucht"),
    tasche(XS, 380, 110, "p252", bis="flucht"),
    pl("nur Flucht", XS, 160, "flucht", fill=ROTHELL, size=30, anker="m", anim="cut", bis="p255"),
    ficon("tabler", "arrow-right", XS, 370, 100, "flucht", anim="cut", bis="p255"),
    pl("Geben: § 255", XS, 160, "p255", fill=LILA, size=30, anker="m", anim="cut", bis="streit"),
    ficon("fluent-emoji-flat", "open-hands", XS, 380, 120, "p255", anim="cut", bis="streit"),
    pl("Nehmen oder Geben?", XS, 160, "streit", fill=WEISS, size=30, anker="m", anim="cut"),
    ficon("fluent-emoji-flat", "balance-scale", XS, 390, 130, "streit", anim="cut"),
]))

# I Subjektiver Tatbestand ---------------------------------------------------------------------------------------------------
folie([("vors", f"{PS_} › a) Vorsatz"), ("zueig", f"{PS_} › b) Zueignungsabsicht"),
       ("rwz", f"{PS_} › b) Rechtswidrigkeit der Zueignung")], rechts_frei([
    *tafel("vors", "Subjektiver Tatbestand"),
    ok(135, 195, beim("vors", "Vorsatz"), gr=18),
    z("Vorsatz: alle objektiven Merkmale", 175, 175, beim("vors", "Vorsatz"), "Bold", 34),
    z("Zueignungsabsicht:", 110, 255, "zueig", "ExtraBold", 34),
    karte(110, 310, 505, 140, "zueig2", fill=BLAUHELL, rund=18, schatten=6, rand=4),
    z("Aneignung:", 135, 325, "zueig2", "ExtraBold", 32, rechts=600),
    z("beabsichtigt", 135, 372, beim("zueig2", "beabsichtigen"), "Bold", 32, rechts=600),
    karte(645, 310, 505, 140, beim("zueig2", "Enteignung"), fill=LILAHELL, rund=18, schatten=6, rand=4),
    z("Enteignung:", 670, 325, beim("zueig2", "Enteignung"), "ExtraBold", 32, rechts=1135),
    z("bedingter Vorsatz", 670, 372, beim("zueig2", "bedingter"), "Bold", 32, rechts=1135),
    fund("BGH, Beschl. v. 3.5.2018 – 3 StR 148/18, Rn. 7", 150, 470, beim("zueig2", "Vorsatz")),
    ok(135, 545, "zueig3", gr=18),
    z("Hagen will die Tasche samt Geld behalten", 175, 525, "zueig3", size=33),
    ok(135, 625, beim("rwz", "Zueignung"), gr=18),
    z("kein Anspruch: Zueignung rechtswidrig", 175, 605, "rwz", "Bold", 34),
    fund("BGH, Beschl. v. 28.10.2025 – 3 StR 458/25, Rn. 5", 175, 655, beim("rwz", "rechtswidrig")),
    *figur_kette("HG", XS, "vors", "ernst", [("listig", "zueig3"), ("still", "rwz")]),
    pl("Vorsatz", XS, 160, "vors", fill=WEISS, size=30, anker="m", bis="zueig"),
    ficon("tabler", "brain", XS, 380, 100, "vors", fuell=GELB, bis="zueig3"),
    pl("Zueignungsabsicht", XS, 160, "zueig", fill=BLAU, size=30, anker="m", anim="cut", bis="zueig3"),
    pl("Tasche samt Geld", XS, 160, "zueig3", fill=GELB, size=30, anker="m", anim="cut", bis="rwz"),
    tasche(XS - 60, 380, 100, "zueig3", anim="cut"),
    ficon("fluent-emoji-flat", "purse", XS + 60, 380, 80, "zueig3", anim="cut"),
    pl("kein Anspruch", XS, 160, "rwz", fill=ROTHELL, size=30, anker="m", anim="cut"),
]))

# J Ergebnis, §§ 250, 251 ----------------------------------------------------------------------------------------------------
folie([("rs", "A. § 249 StGB › II. Rechtswidrigkeit, III. Schuld"), ("erg", "Ergebnis · Hagen: Raub, § 249 StGB"),
       ("qual", "Ausblick › Qualifikationen, §§ 250, 251 StGB")], rechts_frei([
    *tafel("rs", "Ergebnis und Ausblick"),
    ok(135, 200, beim("rs", "Schuld"), gr=18),
    z("II. Rechtswidrigkeit, III. Schuld (+)", 175, 180, "rs", "Bold", 34),
    karte(110, 260, 1040, 110, "erg", fill=GRUENHELL, rund=18, schatten=6, rand=4),
    z("Hagen: Raub, § 249 Abs. 1 StGB", 140, 290, "erg", "ExtraBold", 38),
    z("Qualifikationen:", 110, 420, "qual", "ExtraBold", 34),
    z("§ 250: etwa Täter führt eine Waffe bei sich", 150, 475, beim("qual", "etwa"), size=33),
    z("§ 251: Raub verursacht wenigstens", 150, 540, beim("qual", "Paragraf", nr=2), size=33),
    z("leichtfertig den Tod eines Menschen", 150, 585, beim("qual", "leichtfertig"), size=33),
    *figur_kette("HG", XS, "rs", "ernst", [("still", "erg")]),
    pl("Schuld (+)", XS, 160, beim("rs", "Schuld"), fill=WEISS, size=30, anker="m", bis="erg"),
    pl("Raub, § 249", XS, 160, "erg", fill=GRUEN, size=30, anker="m", anim="cut", bis="qual"),
    ficon("tabler", "gavel", XS, 380, 110, "erg", fuell=GELB),
    pl("§§ 250, 251", XS, 160, "qual", fill=WEISS, size=30, anker="m", anim="cut"),
]))

# K Abwandlung 2: Entreißen ------------------------------------------------------------------------------------------------
folie([("ab2", "Abwandlung 2 › Entreißen im Vorbeilaufen"), ("ab2c", "Abwandlung 2 › Überraschung: Diebstahl"),
       ("ab2d", "Abwandlung 2 › Festhalten: Gewalt, Raub")], rechts_frei([
    *tafel("ab2", "Abwandlung 2: Entreißen", fill=BLAUHELL),
    z("von hinten, Tasche im Vorbeilaufen von der", 110, 175, "ab2", "Bold", 33),
    z("Schulter gerissen, ehe Margit reagieren kann", 110, 220, beim("ab2", "Schulter"), "Bold", 33),
    z("Kraft wirkt vor allem auf die Tasche", 110, 290, "ab2b", size=33),
    z("Überraschung, Schnelligkeit, Geschick prägen", 110, 360, "ab2c", "Bold", 33),
    z("das Bild, nicht körperlicher Zwang", 110, 405, beim("ab2c", "Bild"), "Bold", 33),
    blk(110, 455, 1040, 80, ROTHELL, beim("ab2c", "Diebstahl"), [("nur Diebstahl", "ExtraBold", 36, INK)]),
    fund("BGH, Beschl. v. 26.1.2022 – 3 StR 445/21, Rn. 5, 8", 150, 548, beim("ab2c", "Diebstahl")),
    z("Anders: Margit hält die Tasche fest, Hagen", 110, 610, "ab2d", "Bold", 33),
    z("kann sie nur mit erheblicher Kraft entreißen", 110, 655, beim("ab2d", "Hagen"), "Bold", 33),
    blk(110, 715, 1040, 80, GRUENHELL, "ab2e", [("Gewalt gegen eine Person: Raub", "ExtraBold", 36, INK)]),
    *paar("ab2", mg="ruhig", mg_folge=[("staunt", beim("ab2", "ehe")), ("ernst", "ab2c"), ("sorge", "ab2d")],
          hg="ernst", hg_folge=[("listig", "ab2b"), ("ertappt", "ab2e")]),
    pl("im Vorbeilaufen", MB, 160, "ab2", fill=WEISS, size=30, anker="m", bis="ab2b"),
    tasche(MB + 40, 380, 100, "ab2", bis="ab2d"),
    ficon("tabler", "arrow-right", MB - 70, 370, 70, "ab2", bis="ab2c"),
    pl("Kraft auf die Tasche", MB, 160, "ab2b", fill=WEISS, size=30, anker="m", anim="cut", bis="ab2c"),
    pl("Überraschung", MB, 160, "ab2c", fill=ROTHELL, size=30, anker="m", anim="cut", bis="ab2d"),
    ficon("fluent-emoji-flat", "high-voltage", MB - 80, 370, 70, "ab2c", anim="cut", bis="ab2d"),
    pl("hält fest", MB, 160, "ab2d", fill=WEISS, size=30, anker="m", anim="cut", bis="ab2e"),
    tasche(MB + 40, 380, 100, "ab2d", anim="cut"),
    ficon("tabler", "hand-grab", MB - 70, 360, 80, "ab2d", fuell=WEISS, anim="cut"),
    pl("Gewalt: Raub", MB, 160, "ab2e", fill=GRUEN, size=30, anker="m", anim="cut"),
]))

# L Klausurtipp (Lexi) -------------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · Finalität sauber prüfen"), ("tipp3", "Klausurtipp · bloßes Ausnutzen genügt nicht")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Finalität sauber prüfen", 200, 200, beim("tipp", "Prüfe"), "ExtraBold", 36),
    z("Wann hat der Täter den Entschluss", 200, 290, "tipp2", "Bold", 34),
    z("zur Wegnahme gefasst?", 200, 337, beim("tipp2", "zur"), "Bold", 34),
    z("Erst nach der Gewalt: bloßes Ausnutzen", 200, 425, "tipp3", size=34),
    z("ihrer Wirkung reicht nicht", 200, 472, beim("tipp3", "reicht"), size=34),
    z("Dann: neue, zumindest konkludente Drohung?", 200, 560, "tipp4", "Bold", 34),
    z("Sonst: Diebstahl", 200, 607, beim("tipp4", "Sonst"), "ExtraBold", 34),
    fund("BGH, Beschl. v. 24.10.2024 – 4 StR 368/24, Rn. 7", 240, 660, beim("tipp4", "konkludente")),
    *redet("LX_warnt", LXX, BR, FR_H + 60, "tipp", "sch"),
    namensschild("Lexi", LXX, BR, "tipp", GELB, d=0.2),
])

# M Klausurschema --------------------------------------------------------------------------------------------------------------
K1, K2, K3 = 150, 230, 310
PSS = "Klausurschema"
folie([("sch", PSS), ("s_i", f"{PSS} › I. Tatbestand"), ("s1a", f"{PSS} › I. 1. objektiver Tatbestand"),
       ("s1e", f"{PSS} › I. 2. subjektiver Tatbestand"), ("s_ii", f"{PSS} › II. Rechtswidrigkeit"),
       ("s_iii", f"{PSS} › III. Schuld"), (beim("s_iv", "Qualifikationen"), f"{PSS} › Qualifikationen, §§ 250, 251")], [
    karte(60, 50, 1800, 920, "sch"),
    titel("Klausurschema: Raub, § 249 Abs. 1 StGB", 110, 90, "sch", 52),
    z("I. Tatbestand", K1, 180, "s_i", "Bold", 38, rechts=1820),
    z("1. objektiv", K2, 238, "s1a", "Bold", 34, rechts=1820),
    z("a) fremde bewegliche Sache", K3, 288, beim("s1a", "fremde"), size=34, rechts=1820),
    z("b) Wegnahme", K3, 338, "s1b", size=34, rechts=1820),
    z("c) Gewalt gegen eine Person oder Drohung mit gegenwärtiger Gefahr für Leib oder Leben", K3, 388, "s1c", size=33,
      rechts=1820),
    z("d) finaler Zusammenhang", K3, 438, "s1d", size=34, rechts=1820),
    z("2. subjektiv", K2, 498, "s1e", "Bold", 34, rechts=1820),
    z("a) Vorsatz", K3, 548, beim("s1e", "Vorsatz"), size=34, rechts=1820),
    z("b) Absicht rechtswidriger Zueignung", K3, 598, "s1f", size=34, rechts=1820),
    z("II. Rechtswidrigkeit", K1, 668, "s_ii", "Bold", 38, rechts=1820),
    z("III. Schuld", K1, 736, "s_iii", "Bold", 38, rechts=1820),
    z("ggf. Qualifikationen: §§ 250, 251", K1, 804, beim("s_iv", "Qualifikationen"), "Bold", 38, rechts=1820),
])

# N Merksatz (Lexi) ----------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 170, "merke", 84, anker="m"),
    *markertext([[("Raub", "a"), (" = Wegnahme mit ", 0), ("Gewalt gegen eine Person", "b")],
                 [("oder mit Drohung mit gegenwärtiger", 0)], [("Gefahr für Leib oder Leben.", 0)]], 750, 275, 42, "merke",
                {"a": beim("merke", "Raub"), "b": beim("merke", "Gewalt")}),
    *markertext([[("Die Gewalt muss das ", 0), ("Mittel der Wegnahme", "c"), (" sein.", 0)]], 750, 500, 42, "m_2",
                {"c": beim("m_2", "Mittel")}),
    *markertext([[("Entschluss erst nach der Gewalt:", 0)], [("ohne neue Drohung nur ", 0), ("Diebstahl", "d"), (".", 0)]],
                750, 615, 42, "m_3", {"d": beim("m_3", "Diebstahl")}),
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
