"""Folge 104 · Mittäterschaft § 25 II StGB: Tatplan, Tatbeitrag, Zurechnung – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A1 Küche bei Ansgar (der Plan, Rollen, Beute), A2 Kiosk an der Ecke (Thea steht Schmiere,
Kilian droht nur mit Worten und verschränkten Armen, Fenja greift in die Kasse: 650 €, Flucht, niemand verletzt, Frage),
B Sachverhalt, C Wortlaut § 25 Abs. 2, D Aufbau (gemeinsam/getrennt), E Raub durch Kilian und Fenja (kurz, Verweis 087),
F 1. gemeinsamer Tatplan, G 2. gemeinsame Tatausführung, H Abgrenzung Täter/Gehilfe, I Thea: Schmiere, J § 27 Abs. 1
(Wortlaut), K Ansgar: der Streit, L Streitentscheid, M Rechtsfolge und Exzess, N Ergebnis, O Klausurtipp (Lexi),
P Klausurschema, Q Merksatz (Lexi).
Keine Waffe, keine Verletzung, keine „fiese“ Täterfigur; Zahlen auf Tafeln, Pillen und Blasen als Ziffern.
Namensschild jeder Figur ab ihrem ersten Auftritt, solange sie im Bild ist.
Geräusche nur bei sichtbarer Handlung: Kassenschublade (szene_104kasse_1), Laufschritte bei der Flucht (szene_104laufen_1),
beide Freesound CC0 (../geraeusche_herkunft.json).
Hilfsfunktionen glyphen/z/pl/tafel/fund/blk/wortlaut/redet als eigene Kopie aus Folge 087 (gemeinsame Dateien unverändert)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import wave as _wave

bausteine.FIGORDNER = "op_104/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
LILAHELL = (246, 243, 255, 255)
ROTHELL = (253, 232, 228, 255)
GRUENHELL = (232, 247, 233, 255)
BLAUHELL = (233, 241, 253, 255)
DAUER = bausteine._cj()["dauer"]
NULL = "fall"                     # Szene A1 steht ab 0,0 s (render_104 setzt alle Elemente bis zur Marke „fall“ auf 0,0 s)

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


def sachverhalt_klein(cue, absaetze, frage, size=36, pfad="Sachverhalt"):
    """Wie bausteine.sachverhalt(), Schrift passend zur Länge (wie Folge 087)."""
    els = [karte(140, 50, 1640, 920, cue, fill=HELL), titel("Sachverhalt", 210, 82, cue, 56)]
    y = 175
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=size, zeilenabstand=1.27)
        els += e; y += 14
    els.append(pl(frage, 210, y + 8, cue, fill=PINK, size=34))
    assert y + 8 <= 890, f"Sachverhalt zu lang ({y})"
    folie([(cue, pfad)], els)


def markertext_farbig(zeilen_tokens, cx, y, size, cue, hl_cues, farben, lh=1.3):
    """Wie ostil.markertext, aber mit eigener Markerfarbe je Schlüssel (wie Folge 084/087)."""
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
    return els, im.width


def wortlaut(x, y, w, h, cue, zeilen, size, hl, quelle, farben=None):
    """Wortlautkarte: wörtliches Zitat (gesetze-im-internet.de, Abruf 03.10.2026) in einer hellen Karte, Fundstelle darunter
    rechts. zeilen = Liste von Token-Listen [(text, Schlüssel|0)], hl = {Schlüssel: Cue} (Hervorhebung synchron zum Wort)."""
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


# --- Eigene Hilfsfunktion (wie Folge 087): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ---------------------
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
SCHILD = {"AN": ("Ansgar", BLAU), "KI": ("Kilian", ROT), "FE": ("Fenja", LILA), "TH": ("Thea", GRUEN), "EM": ("Emil", GELB)}


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


X4 = {"KI": 1335, "FE": 1480, "TH": 1625, "AN": 1775}       # alle vier rechts neben der Tafel (blicken zur Tafel)
H4 = 420


def vier(cue, folgen=None, start=None):
    """Die vier Beteiligten nebeneinander, jede Figur mit eigener Mimikfolge."""
    folgen = folgen or {}
    start = start or {}
    els = []
    for i, p in enumerate(("KI", "FE", "TH", "AN")):
        els += figur_kette(p, X4[p], cue, start.get(p, "ruhig"), folgen.get(p, ()), hoehe=H4, d=0.1 * i, schild_d=0.2 + 0.1 * i)
    return els


XA, XB = 1440, 1740                        # zwei Figuren rechts
XS = 1600                                  # eine Figur rechts
MB = (XA + XB) // 2


def geld(cx, unten, breite, cue, bis=None, anim="pop", d=0.0):
    return ficon("fluent-emoji-flat", "euro-banknote", cx, unten, breite, cue, bis=bis, anim=anim, d=d)


# ===========================================================================================================================
# A1 Fall: der Plan in der Küche von Ansgar
# ===========================================================================================================================
AX, AH = 720, 560                          # Ansgar (blickt nach rechts zu den anderen)
KX, FX, TX, GH = 1150, 1420, 1690, 520     # Kilian, Fenja, Thea (blicken nach links zu Ansgar)
ANr = ("AN_redet_r", AX, BODEN, AH)
folie([(NULL, "Fall · Der Plan"), ("a1", "Fall · Die Rollen"), ("teil", "Fall · Die Beute")], [
    linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK),
    # Pinnwand mit dem Plan
    karte(90, 90, 500, 300, NULL, fill=WEISS, rund=14, schatten=6, rand=5),
    pl("Plan", 340, 70, NULL, fill=GELB, size=30, anker="m"),
    ficon("fluent-emoji-flat", "pushpin", 130, 160, 44, NULL),
    ficon("fluent-emoji-flat", "convenience-store", 230, 330, 150, "kiosk"),
    ficon("fluent-emoji-flat", "eight-oclock", 410, 330, 100, beim("idee", "Uhrzeit")),
    ficon("fluent-emoji-flat", "clipboard", 525, 330, 80, beim("idee", "Rollen")),
    pl("Kiosk an der Ecke", 340, 425, "kiosk", fill=WEISS, size=28, anker="m"),
    pl("kurz vor Ladenschluss", 340, 490, beim("kiosk", "kurz"), fill=WEISS, size=28, anker="m"),
    pl("Inhaber Emil allein", 340, 555, beim("kiosk", "Inhaber"), fill=GELB, size=28, anker="m"),
    # Ansgar
    peep_voll("AN_ruhig_r", AX, BODEN, AH, NULL, bis="idee"),
    peep_voll("AN_froh_r", AX, BODEN, AH, "idee", anim="cut", bis="a1"),
    *redet("AN_redet_r", AX, BODEN, AH, "a1", "teil"),
    peep_voll("AN_ernst_r", AX, BODEN, AH, "teil", anim="cut", bis="weg_a"),
    peep_voll("AN_entschlossen_r", AX, BODEN, AH, "weg_a", anim="cut"),
    namensschild("Ansgar", AX, BODEN - 8, NULL, BLAU),
    ficon("fluent-emoji-flat", "light-bulb", AX + 150, 330, 80, "idee", bis="a1"),
    pl("Idee: Ansgar", AX, 250, beim("idee", "Idee"), fill=GELB, size=28, anker="m", bis="a1"),
    blase("sprech", 940, 220, "a1", 1200, 150, inhalt=["Kilian redet, Fenja holt das Geld,", "Thea passt draußen auf. Ich bleibe zu Hause."],
          textsize=32, figur=ANr, bis="teil"),
    # die anderen drei, je ab ihrer Nennung
    *figur_kette("KI", KX, beim("a1", "Kilian"), "ruhig", [("ernst", "teil")], unten=BODEN, hoehe=GH, schild_d=0.1),
    *figur_kette("FE", FX, beim("a1", "Fenja"), "ruhig", [("entschlossen", "teil")], unten=BODEN, hoehe=GH, schild_d=0.1),
    *figur_kette("TH", TX, beim("a1", "Thea"), "ruhig", [("ernst", beim("teil", "Thea"))], unten=BODEN, hoehe=GH, schild_d=0.1),
    pl("redet", KX, 310, beim("a1", "redet"), fill=WEISS, size=28, anker="m"),
    pl("holt das Geld", FX, 310, beim("a1", "holt"), fill=WEISS, size=28, anker="m"),
    pl("passt draußen auf", TX, 310, beim("a1", "passt"), fill=WEISS, size=28, anker="m"),
    # die Beute
    pl("Beute: Ansgar, Kilian und Fenja teilen", 1180, 150, "teil", fill=GELB, size=30, anker="m"),
    ficon("fluent-emoji-flat", "money-bag", 1560, 200, 80, "teil"),
    pl("Thea: fest 50 €", TX, 240, beim("teil", "Thea"), fill=GRUEN, size=28, anker="m"),
    # Ansgar während des Überfalls ohne Kontakt
    ficon("fluent-emoji-flat", "mobile-phone-off", AX + 170, 400, 70, "weg_a"),
    pl("während der Tat: kein Kontakt", 810, 250, beim("weg_a", "Kontakt"), fill=ROTHELL, size=28, anker="m"),
])

# ===========================================================================================================================
# A2 Fall: am Kiosk
# ===========================================================================================================================
THX, KIX, FEX, EMX = 250, 830, 1090, 1600
FH = 520
WAND = 480                                  # Außenwand des Kiosks (links davon die Straßenecke)
KIr = ("KI_redet_r", KIX, BODEN, 540)
FEr = ("FE_redet_r", FEX, BODEN, FH)
EMWEG = beim("emil", "zurück")
FL0, FL1 = beim("flucht", "laufen"), beim("flucht", "davon", ende=True)


def kiosk(cue):
    """Kiosk an der Ecke: Wand, Schild, Regal mit Waren, Theke mit Kasse und Telefon."""
    return [
        linienzug([(60, BODEN), (1860, BODEN)], cue, breite=7, farbe=INK),
        karte(WAND, 230, 1380, 650, cue, fill=WEISS, rund=10, schatten=6, rand=5),
        pl("Kiosk", 1170, 205, cue, fill=GELB, size=34, anker="m"),
        # Regale links und rechts von Emil (sein Kopf bleibt frei)
        linienzug([(1280, 440), (1520, 440)], cue, breite=6, farbe=INK),
        linienzug([(1760, 440), (1850, 440)], cue, breite=6, farbe=INK),
        ficon("fluent-emoji-flat", "newspaper", 1320, 440, 70, cue),
        ficon("fluent-emoji-flat", "chocolate-bar", 1405, 440, 60, cue),
        ficon("fluent-emoji-flat", "candy", 1480, 440, 60, cue),
        ficon("fluent-emoji-flat", "cup-with-straw", 1805, 440, 60, cue),
    ]


def theke(cue):
    return [karte(1250, 630, 600, 250, cue, fill=(249, 213, 110, 255), rund=10, schatten=0, rand=5),
            karte(1280, 570, 160, 60, cue, fill=(141, 179, 242, 255), rund=8, schatten=0, rand=5),
            pl("Kasse", 1360, 650, cue, fill=WEISS, size=26, anker="m"),
            ficon("fluent-emoji-flat", "telephone", 1800, 630, 80, cue)]


Z0 = "ecke"
folie([(Z0, "Fall · Thea steht Schmiere"), ("theke", "Fall · Kilian droht"), ("kasse", "Fall · Fenja greift in die Kasse"),
       ("flucht", "Fall · Die drei laufen davon"), ("frage", "Fall · Die Frage")], [
    *kiosk(Z0),
    # Emil hinter der Theke (die Theke verdeckt ihn ab der Hüfte)
    peep_voll("EM_ruhig", EMX, BODEN, 540, Z0, bis="emil"),
    peep_voll("EM_erschrickt", EMX + 60, BODEN, 540, "emil", anim="cut", bis=beim("flucht", "Verletzt")),
    peep_voll("EM_sorge", EMX + 60, BODEN, 540, beim("flucht", "Verletzt"), anim="cut"),
    *theke(Z0),
    namensschild("Emil", EMX, BODEN - 8, Z0, GELB, bis="emil"),
    namensschild("Emil", EMX + 60, BODEN - 8, "emil", GELB, anim="cut"),
    # Thea an der Ecke
    *figur_kette("TH", THX, Z0, "wachsam", [("ernst", "flucht")], unten=BODEN, hoehe=FH, schild_d=0.1),
    ficon("fluent-emoji-flat", "eyes", THX - 150, 420, 70, Z0),
    pl("steht Schmiere an der Ecke", THX, 300, beim("ecke", "steht"), fill=GRUEN, size=28, anker="m", bis="flucht"),
    pl("pfeift, falls jemand kommt", THX, 235, beim("ecke", "pfeifen"), fill=WEISS, size=28, anker="m", bis="flucht"),
    pl("gibt Sicherheit", THX, 170, beim("ecke", "Sicherheit"), fill=WEISS, size=28, anker="m", bis="flucht"),
    # Kilian vor der Theke: droht nur mit Worten und verschränkten Armen
    *figur_kette("KI", KIX, "theke", "entschlossen_r", [("ernst_r", "k1")], bis="k1", unten=BODEN, hoehe=540, schild=False),
    *redet("KI_redet_r", KIX, BODEN, 540, "k1", "emil"),
    peep_voll("KI_ernst_r", KIX, BODEN, 540, "emil", anim="cut", bis="flucht"),
    namensschild("Kilian", KIX, BODEN - 8, "theke", ROT, d=0.1, bis="flucht"),
    pl("baut sich vor der Theke auf", KIX, 290, beim("theke", "baut"), fill=ROTHELL, size=28, anker="m", bis="k1"),
    blase("sprech", 700, 200, "k1", 1060, 175, inhalt=["Hände weg vom Telefon,", "sonst schlage ich zu!"], textsize=34,
          figur=KIr, bis="emil"),
    pl("weicht erschrocken zurück", EMX + 20, 280, "emil", fill=WEISS, size=28, anker="m", bis=beim("flucht", "Verletzt")),
    # Fenja greift in die Kasse
    *figur_kette("FE", FEX, "theke", "ernst_r", [("entschlossen_r", "kasse")], bis="f1", unten=BODEN, hoehe=FH, schild=False, d=0.2),
    *redet("FE_redet_r", FEX, BODEN, FH, "f1", "flucht"),
    namensschild("Fenja", FEX, BODEN - 8, "theke", LILA, d=0.3, bis="flucht"),
    szene(ficon("fluent-emoji-flat", "euro-banknote", 1360, 575, 90, "kasse", anim="cut", bis=(("kasse", 0.9))), "104kasse_1", 0.8),
    bewegt(geld(FEX + 90, 650, 90, ("kasse", 0.9), anim="cut", bis="flucht"), ("kasse", 0.9), ("kasse", 1.6), 180, -75),
    pl("650 €", FEX + 40, 300, beim("kasse", "sechshundertfünfzig"), fill=GELB, size=32, anker="m", bis="flucht"),
    blase("sprech", 560, 170, "f1", 880, 170, inhalt=["Ich hab das Geld. Los!"], textsize=34, figur=FEr, bis="flucht"),
    # Flucht: die drei laufen nach links davon; niemand verletzt
    szene(bewegt(peep_voll("KI_entschlossen", 640, BODEN, 540, "flucht", anim="cut"), FL0, FL1, 200, 0), "104laufen_1", 0.8),
    bewegt(namensschild("Kilian", 640, BODEN - 8, "flucht", ROT, anim="cut"), FL0, FL1, 200, 0),
    bewegt(peep_voll("FE_entschlossen", 900, BODEN, FH, "flucht", anim="cut"), FL0, FL1, 200, 0),
    bewegt(namensschild("Fenja", 900, BODEN - 8, "flucht", LILA, anim="cut"), FL0, FL1, 200, 0),
    bewegt(geld(960, 650, 80, "flucht", anim="cut"), FL0, FL1, 200, 0),
    pl("Verletzt wird niemand.", EMX + 20, 280, beim("flucht", "Verletzt"), fill=GRUENHELL, size=28, anker="m"),
    pl("Mittäter oder nur Gehilfe?", 760, 90, "frage", fill=PINK, size=36, anker="m"),
    pl("Und Ansgar? War nicht dabei.", 760, 160, "frage2", fill=WEISS, size=30, anker="m"),
    ficon("fluent-emoji-flat", "house", 1045, 215, 60, "frage2"),
])

# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
sachverhalt_klein("sv", [
    "Ansgar hat die Idee, den Kiosk an der Ecke kurz vor Ladenschluss zu überfallen, wenn der Inhaber Emil allein ist. Er "
    "sucht den Kiosk aus, legt die Uhrzeit fest und verteilt die Rollen: Kilian redet, Fenja holt das Geld, Thea passt "
    "draußen auf. Ansgar bleibt zu Hause und hat während des Überfalls keinen Kontakt zu den anderen. Die Beute wollen "
    "sich Ansgar, Kilian und Fenja teilen; Thea, die nicht mitgeplant hat, bekommt fest 50 €. Es soll bei diesem einen "
    "Überfall bleiben.",
    "Am Abend steht Thea an der Ecke und soll pfeifen, falls jemand kommt; das gibt den anderen Sicherheit. Kilian baut "
    "sich vor der Theke auf: „Hände weg vom Telefon, sonst schlage ich zu!“ Emil weicht erschrocken zurück. Fenja greift "
    "in die Kasse und nimmt 650 €. Die drei laufen davon. Niemand kommt vorbei, niemand wird verletzt, keiner hat eine "
    "Waffe dabei.",
], "Wie haben sich Ansgar, Kilian, Fenja und Thea strafbar gemacht?")

# ===========================================================================================================================
# C Wortlaut § 25 Abs. 2 und Voraussetzungen
# ===========================================================================================================================
W25 = [[("„Begehen mehrere die Straftat ", 0), ("gemeinschaftlich", "a"), (", so", 0)],
       [("wird ", 0), ("jeder als Täter", "b"), (" bestraft (Mittäter).“", 0)]]
PM = "Mittäterschaft, § 25 Abs. 2 StGB"
folie([("p25", f"{PM} › Wortlaut"), ("vor", f"{PM} › Voraussetzungen")], rechts_frei([
    *tafel("p25", "Mittäterschaft: § 25 Abs. 2 StGB"),
    *wortlaut(110, 175, 1040, 135, "p25", W25, 36, {"a": beim("p25w", "gemeinschaftlich"), "b": beim("p25w", "jeder")},
              "§ 25 Abs. 2 StGB", farben={"a": GELB, "b": BLAU}),
    z("Zwei Voraussetzungen:", 110, 400, "vor", "ExtraBold", 36),
    blk(110, 460, 1040, 90, GELB, "v1", [("1. gemeinsamer Tatplan", "ExtraBold", 36, INK)]),
    blk(110, 580, 1040, 90, BLAU, "v2", [("2. gemeinsame Tatausführung", "ExtraBold", 36, INK)]),
    *vier("p25", {"KI": [("ernst", "vor")], "FE": [("ernst", "v1")], "TH": [("ernst", "v2")], "AN": [("ernst", "vor")]}),
    pl("§ 25 Abs. 2", 1555, 160, "p25", fill=WEISS, size=30, anker="m", bis="vor"),
    pl("Plan + Ausführung", 1555, 160, "vor", fill=GELB, size=30, anker="m", anim="cut"),
    ficon("fluent-emoji-flat", "spiral-notepad", 1480, 330, 80, "v1"),
    ficon("fluent-emoji-flat", "puzzle-piece", 1630, 330, 80, "v2"),
]))

# ===========================================================================================================================
# D Aufbau: gemeinsame oder getrennte Prüfung
# ===========================================================================================================================
folie([("aufbau", "Aufbau › gemeinsame oder getrennte Prüfung"), ("wahl", "Aufbau › Kilian und Fenja gemeinsam"),
       ("wahl2", "Aufbau › Thea und Ansgar getrennt")], rechts_frei([
    *tafel("aufbau", "Aufbau im Gutachten"),
    karte(110, 175, 505, 230, "gem", fill=GRUENHELL, rund=18, schatten=6, rand=4),
    z("gemeinsam:", 135, 190, "gem", "ExtraBold", 32, rechts=600),
    z("Mittäterschaft", 135, 240, beim("gem", "Mittäterschaft"), "Bold", 30, rechts=600),
    z("eindeutig, etwa", 135, 283, beim("gem", "eindeutig"), "Bold", 30, rechts=600),
    z("gleichwertige Beiträge", 135, 326, beim("gem", "gleichwertigen"), "Bold", 30, rechts=600),
    karte(645, 175, 505, 230, "getr", fill=LILAHELL, rund=18, schatten=6, rand=4),
    z("getrennt:", 670, 190, "getr", "ExtraBold", 32, rechts=1135),
    z("bei einem fraglich", 670, 240, beim("getr", "fraglich"), "Bold", 30, rechts=1135),
    z("erst der Tatnächste,", 670, 283, beim("getr", "erst"), "Bold", 30, rechts=1135),
    z("dann mit Zurechnung", 670, 326, beim("getr", "dann"), "Bold", 30, rechts=1135),
    z("Hier:", 110, 450, "wahl", "ExtraBold", 36),
    blk(110, 505, 1040, 80, GRUENHELL, beim("wahl", "Kilian"), [("Kilian und Fenja gemeinsam", "ExtraBold", 34, INK)]),
    z("jeder verwirklicht einen Teil des Raubes,", 140, 605, beim("wahl", "verwirklicht"), size=32),
    z("ihr Zusammenwirken liegt auf der Hand", 140, 648, beim("wahl", "Zusammenwirken"), size=32),
    blk(110, 715, 1040, 80, LILAHELL, "wahl2", [("Thea und Ansgar danach getrennt", "ExtraBold", 34, INK)]),
    z("gerade ihre Täterschaft ist das Problem", 140, 815, beim("wahl2", "gerade"), size=32),
    *vier("aufbau", {"KI": [("entschlossen", "wahl")], "FE": [("entschlossen", "wahl")], "TH": [("sorge", "wahl2")],
                     "AN": [("still", "wahl2")]}),
    pl("gemeinsam oder getrennt?", 1555, 160, "aufbau", fill=WEISS, size=30, anker="m", bis="wahl"),
    pl("gemeinsam", (X4["KI"] + X4["FE"]) // 2, 160, "wahl", fill=GRUEN, size=30, anker="m", anim="cut"),
    pl("getrennt", (X4["TH"] + X4["AN"]) // 2, 160, "wahl2", fill=LILA, size=30, anker="m", anim="cut"),
    ficon("fluent-emoji-flat", "link", (X4["KI"] + X4["FE"]) // 2, 300, 90, "wahl"),
]))

# ===========================================================================================================================
# E A. Kilian und Fenja: Raub, kurz
# ===========================================================================================================================
PA = "A. Kilian und Fenja: Raub, §§ 249, 25 Abs. 2 StGB"
folie([("raub", f"{PA} › Drohung und Wegnahme"), ("keiner", f"{PA} › Zurechnung nötig")], rechts_frei([
    *tafel("raub", "A. Raub durch Kilian und Fenja"),
    ok(135, 200, beim("drohk", "Gefahr"), gr=18),
    z("Kilian: Drohung mit Schlägen,", 175, 180, "drohk", "Bold", 34),
    z("gegenwärtige Gefahr für Leib", 175, 225, beim("drohk", "Gefahr"), size=33),
    ok(135, 305, beim("wegf", "Gewahrsam"), gr=18),
    z("Fenja: nimmt das Geld aus der Kasse,", 175, 285, "wegf", "Bold", 34),
    z("bricht den Gewahrsam von Emil", 175, 330, beim("wegf", "Gewahrsam"), size=33),
    ok(135, 410, "final", gr=18),
    z("Drohung soll die Wegnahme ermöglichen", 175, 390, "final", "Bold", 34),
    blk(110, 455, 1040, 80, LILAHELL, beim("final", "Details"), [("Details: unsere Folge zum Raub", "Bold", 33, INK)]),
    nein(135, 600, "keiner", gr=18),
    z("keiner erfüllt alles allein:", 175, 580, "keiner", "Bold", 34),
    z("Kilian nimmt nichts weg, Fenja droht nicht", 175, 625, beim("keiner", "Kilian"), size=33),
    blk(110, 690, 1040, 80, GELB, beim("keiner", "Deshalb"), [("Deshalb: Zurechnung, § 25 Abs. 2 StGB", "ExtraBold", 34, INK)]),
    *figur_kette("KI", XA, "raub", "ernst", [("entschlossen", "drohk"), ("ernst", "wegf"), ("still", "keiner")]),
    *figur_kette("FE", XB, "raub", "ruhig", [("entschlossen", "wegf"), ("ernst", "final"), ("still", "keiner")], d=0.2, schild_d=0.3),
    pl("Raub, § 249", MB, 160, "raub", fill=WEISS, size=30, anker="m", bis="drohk"),
    pl("droht", XA, 160, "drohk", fill=ROTHELL, size=30, anker="m", anim="cut", bis="keiner"),
    pl("nimmt weg", XB, 160, "wegf", fill=BLAU, size=30, anker="m", anim="cut", bis="keiner"),
    ficon("fluent-emoji-flat", "telephone", XA, 380, 80, "drohk", bis="keiner"),
    geld(XB, 370, 90, "wegf", bis="keiner"),
    pl("nur ein Teil", XA, 160, "keiner", fill=WEISS, size=30, anker="m", anim="cut"),
    pl("nur ein Teil", XB, 160, beim("keiner", "Fenja"), fill=WEISS, size=30, anker="m", anim="cut"),
    ficon("fluent-emoji-flat", "link", MB, 380, 100, beim("keiner", "Zurechnung")),
]))

# ===========================================================================================================================
# F 1. Gemeinsamer Tatplan
# ===========================================================================================================================
folie([("tp", f"{PA} › 1. gemeinsamer Tatplan"), ("sukz", f"{PA} › 1. sukzessive Mittäterschaft")], rechts_frei([
    *tafel("tp", "1. Gemeinsamer Tatplan"),
    ok(135, 200, "tp1", gr=18),
    z("Rollen ausdrücklich verabredet", 175, 180, "tp1", "Bold", 34),
    z("auch stillschweigend möglich,", 110, 270, "konk", "Bold", 34),
    z("etwa durch arbeitsteiliges Handeln", 110, 315, beim("konk", "etwa"), size=33),
    fund("BGH, Urt. v. 13.4.2023 – 5 StR 533/22, Rn. 7", 150, 365, beim("konk", "arbeitsteiliges")),
    karte(110, 430, 1040, 260, "sukz", fill=BLAUHELL, rund=18, schatten=6, rand=4),
    z("sukzessive Mittäterschaft:", 140, 450, beim("sukz", "Ausführung"), "ExtraBold", 34),
    z("Einstieg erst während der Ausführung,", 140, 500, beim("sukz", "Ausführung"), size=33),
    z("Bisheriges bekannt und gebilligt", 140, 545, beim("sukz", "Bisherige"), size=33),
    fund("BGH, Urt. v. 26.9.2024 – 4 StR 115/24, Rn. 56", 140, 610, beim("sukz", "sukzessiver")),
    *figur_kette("KI", XA, "tp", "ernst", [("ruhig", "konk")]),
    *figur_kette("FE", XB, "tp", "ernst", [("ruhig", "konk")], d=0.2, schild_d=0.3),
    pl("verabredet", MB, 160, "tp1", fill=GRUEN, size=30, anker="m", bis="konk"),
    ficon("fluent-emoji-flat", "spiral-notepad", MB, 380, 100, "tp1", bis="konk"),
    pl("auch stillschweigend", MB, 160, "konk", fill=WEISS, size=30, anker="m", anim="cut", bis="sukz"),
    ficon("fluent-emoji-flat", "handshake", MB, 380, 100, "konk", anim="cut", bis="sukz"),
    pl("später Einstieg", MB, 160, "sukz", fill=BLAU, size=30, anker="m", anim="cut"),
    ficon("fluent-emoji-flat", "door", MB, 390, 90, "sukz", anim="cut"),
]))

# ===========================================================================================================================
# G 2. Gemeinsame Tatausführung
# ===========================================================================================================================
folie([("ta", f"{PA} › 2. gemeinsame Tatausführung"), ("zueig", f"{PA} › Zueignungsabsicht in eigener Person"),
       ("kf", "Ergebnis A · Kilian und Fenja: Mittäter eines Raubes")], rechts_frei([
    *tafel("ta", "2. Gemeinsame Tatausführung"),
    z("jeder braucht einen wesentlichen Tatbeitrag", 110, 175, beim("ta", "Jeder"), "Bold", 34),
    fund("BGH, Urt. v. 23.3.2023 – 3 StR 363/22, Rn. 8", 150, 225, beim("ta", "wesentlichen")),
    ok(135, 295, "ta1", gr=18),
    z("Drohung und Griff in die Kasse", 175, 275, "ta1", "Bold", 34),
    z("greifen ineinander: beide wesentlich", 175, 320, beim("ta1", "greifen"), size=33),
    karte(110, 390, 1040, 190, "zueig", fill=LILAHELL, rund=18, schatten=6, rand=4),
    z("nicht zugerechnet: Zueignungsabsicht,", 140, 405, "zueig", "ExtraBold", 33),
    z("die braucht jeder selbst; beide wollen", 140, 450, beim("zueig", "braucht"), size=33),
    z("ihren Anteil behalten", 140, 495, beim("zueig", "Beide"), size=33),
    fund("BGH, Beschl. v. 3.5.2018 – 3 StR 148/18, Rn. 7", 150, 595, beim("zueig", "Anteil")),
    blk(110, 660, 1040, 90, GRUENHELL, "kf", [("Kilian und Fenja: Mittäter eines Raubes (+)", "ExtraBold", 34, INK)]),
    *figur_kette("KI", XA, "ta", "ernst", [("entschlossen", "ta1"), ("still", "kf")]),
    *figur_kette("FE", XB, "ta", "ernst", [("entschlossen", "ta1"), ("still", "kf")], d=0.2, schild_d=0.3),
    pl("wesentlicher Beitrag", MB, 160, "ta", fill=WEISS, size=30, anker="m", bis="ta1"),
    ficon("fluent-emoji-flat", "puzzle-piece", MB - 60, 380, 90, "ta1", bis="zueig"),
    ficon("fluent-emoji-flat", "puzzle-piece", MB + 60, 380, 90, "ta1", bis="zueig"),
    pl("greifen ineinander", MB, 160, "ta1", fill=GELB, size=30, anker="m", anim="cut", bis="zueig"),
    pl("Absicht: jeder selbst", MB, 160, "zueig", fill=LILA, size=30, anker="m", anim="cut", bis="kf"),
    ficon("fluent-emoji-flat", "brain", MB, 380, 100, "zueig", anim="cut", bis="kf"),
    pl("Mittäter (+)", MB, 160, "kf", fill=GRUEN, size=30, anker="m", anim="cut"),
]))

# ===========================================================================================================================
# H Abgrenzung Täter – Gehilfe
# ===========================================================================================================================
PG = "Abgrenzung Täter – Gehilfe"
folie([("abgr", f"{PG} › Thea und Ansgar"), ("thl", f"{PG} › Tatherrschaftslehre"),
       ("bgh", f"{PG} › BGH: wertende Gesamtbetrachtung")], rechts_frei([
    *tafel("abgr", "Täter oder nur Gehilfe?"),
    karte(110, 175, 1040, 140, "thl", fill=BLAUHELL, rund=18, schatten=6, rand=4),
    z("Tatherrschaftslehre:", 140, 190, "thl", "ExtraBold", 34),
    z("arbeitsteilige Mitbeherrschung des Geschehens", 140, 240, beim("thl", "arbeitsteilig"), "Bold", 32),
    karte(110, 350, 1040, 360, "bgh", fill=LILAHELL, rund=18, schatten=6, rand=4),
    z("BGH: wertende Gesamtbetrachtung", 140, 365, "bgh", "ExtraBold", 34),
    z("1. Grad des eigenen Interesses an der Tat", 160, 425, "kr1", "Bold", 32),
    z("2. Umfang der Tatbeteiligung", 160, 480, "kr2", "Bold", 32),
    z("3. Tatherrschaft oder wenigstens", 160, 535, "kr3", "Bold", 32),
    z("der Wille dazu", 200, 580, beim("kr3", "wenigstens"), "Bold", 32),
    fund("BGH, Urt. v. 23.3.2023 – 3 StR 363/22, Rn. 8", 160, 645, beim("kr3", "Wille")),
    *figur_kette("TH", XA, "abgr", "sorge", [("ernst", "bgh")]),
    *figur_kette("AN", XB, "abgr", "ruhig", [("ernst", "bgh")], d=0.2, schild_d=0.3),
    pl("Täter oder Gehilfe?", MB, 160, "abgr", fill=PINK, size=30, anker="m", bis="thl"),
    pl("Mitbeherrschung?", MB, 160, "thl", fill=BLAU, size=30, anker="m", anim="cut", bis="bgh"),
    ficon("fluent-emoji-flat", "puzzle-piece", MB, 380, 90, "thl", bis="bgh"),
    pl("Gesamtbetrachtung", MB, 160, "bgh", fill=LILA, size=30, anker="m", anim="cut"),
    ficon("fluent-emoji-flat", "balance-scale", MB, 390, 120, "bgh"),
]))

# ===========================================================================================================================
# I B. Thea: Schmiere stehen
# ===========================================================================================================================
PB = "B. Thea: Mittäterin?"
folie([("thea", f"{PB} › Schmiere stehen"), ("bgh_s", f"{PB} › untergeordneter Beitrag"),
       ("beide", f"{PB} › keine Mittäterin")], rechts_frei([
    *tafel("thea", "B. Thea: Schmiere stehen"),
    z("Klassiker: je nach Gewicht Mittäterschaft", 110, 175, "klass", "Bold", 34),
    z("oder nur Beihilfe", 110, 220, beim("klass", "Beihilfe"), "Bold", 34),
    nein(135, 300, "thea2", gr=18),
    z("nicht mitgeplant, nur 50 €:", 175, 280, "thea2", size=33),
    z("eigenes Interesse gering", 175, 325, beim("thea2", "Ihr"), "Bold", 33),
    nein(135, 405, "thea3", gr=18),
    z("sichert nur ab, kein Einfluss", 175, 385, "thea3", size=33),
    z("auf Ob und Wie der Tat", 175, 430, beim("thea3", "Ob"), "Bold", 33),
    z("BGH: bloße Absicherung ist ein", 110, 500, "bgh_s", "Bold", 33),
    z("untergeordneter Beitrag", 110, 545, beim("bgh_s", "untergeordneten"), "Bold", 33),
    fund("BGH, Urt. v. 26.4.2012 – 4 StR 665/11, Rn. 24;", 150, 595, beim("bgh_s", "Bundesgerichtshof")),
    fund("BGH, Beschl. v. 29.9.2005 – 4 StR 420/05, Rn. 4 f.", 150, 630, beim("bgh_s", "Bundesgerichtshof")),
    blk(110, 690, 1040, 90, ROTHELL, "beide", [("beide Ansichten: Thea keine Mittäterin", "ExtraBold", 34, INK)]),
    *figur_kette("TH", XS, "thea", "wachsam", [("ernst", "thea2"), ("sorge", "thea3"), ("still", "beide")]),
    pl("Schmiere stehen", XS, 160, "thea", fill=GRUEN, size=30, anker="m", bis="thea2"),
    ficon("fluent-emoji-flat", "eyes", XS, 360, 90, "thea", bis="thea2"),
    pl("nur 50 €", XS, 160, "thea2", fill=WEISS, size=30, anker="m", anim="cut", bis="thea3"),
    ficon("fluent-emoji-flat", "coin", XS, 370, 80, "thea2", anim="cut", bis="thea3"),
    pl("kein Einfluss", XS, 160, "thea3", fill=ROTHELL, size=30, anker="m", anim="cut", bis="bgh_s"),
    pl("untergeordnet", XS, 160, "bgh_s", fill=WEISS, size=30, anker="m", anim="cut", bis="beide"),
    pl("keine Mittäterin", XS, 160, "beide", fill=ROTHELL, size=30, anker="m", anim="cut"),
]))

# ===========================================================================================================================
# J Beihilfe: Wortlaut § 27 Abs. 1
# ===========================================================================================================================
W27 = [[("„Als ", 0), ("Gehilfe", "a"), (" wird bestraft, wer ", 0), ("vorsätzlich", "b"), (" einem", 0)],
       [("anderen zu dessen ", 0), ("vorsätzlich begangener rechtswidriger Tat", "c")],
       [("Hilfe geleistet", "d"), (" hat.“", 0)]]
folie([("p27", f"{PB} › Beihilfe, § 27 Abs. 1 StGB"), ("thea5", "Ergebnis B · Thea: Gehilfin")], rechts_frei([
    *tafel("p27", "Beihilfe: § 27 Abs. 1 StGB"),
    *wortlaut(100, 175, 1060, 185, "p27", W27, 32,
              {"a": beim("p27w", "Gehilfe"), "b": beim("p27w", "vorsätzlich"), "c": beim("p27w", "vorsätzlich", nr=2),
               "d": beim("p27w", "Hilfe")}, "§ 27 Abs. 1 StGB", farben={"a": GELB, "b": LILA, "c": BLAU, "d": GRUEN}),
    z("Hilfe leisten: die Tat fördern oder erleichtern", 110, 430, "hilfe", "Bold", 34),
    fund("BGH, Beschl. v. 10.7.2025 – 3 StR 496/23, Rn. 42", 150, 480, beim("hilfe", "erleichtert")),
    ok(135, 555, "thea4", gr=18),
    z("Thea sichert ab und bestärkt die anderen,", 175, 535, "thea4", size=33),
    z("und das weiß sie", 175, 580, beim("thea4", "und", nr=2), size=33),
    blk(110, 650, 1040, 90, GRUENHELL, "thea5", [("Thea: Gehilfin beim Raub (+)", "ExtraBold", 36, INK)]),
    *figur_kette("TH", XS, "p27", "ernst", [("ruhig", "thea4"), ("still", "thea5")]),
    pl("§ 27 Abs. 1", XS, 160, "p27", fill=WEISS, size=30, anker="m", bis="hilfe"),
    pl("fördert", XS, 160, "hilfe", fill=GRUEN, size=30, anker="m", anim="cut", bis="thea5"),
    ficon("fluent-emoji-flat", "eyes", XS, 360, 90, "thea4", bis="thea5"),
    pl("Gehilfin", XS, 160, "thea5", fill=GRUEN, size=30, anker="m", anim="cut"),
]))

# ===========================================================================================================================
# K C. Ansgar: der Streit um den Planer
# ===========================================================================================================================
PC = "C. Ansgar: Planer ohne Mitwirkung am Tatort"
folie([("ans", f"{PC} › strenge Tatherrschaftslehre"), ("gemae", f"{PC} › gemäßigte Tatherrschaftslehre"),
       ("bgh_a", f"{PC} › BGH")], rechts_frei([
    *tafel("ans", "C. Ansgar: nicht am Tatort"),
    karte(110, 170, 1040, 205, "streng", fill=ROTHELL, rund=18, schatten=6, rand=4),
    z("strenge Tatherrschaftslehre:", 140, 185, "streng", "ExtraBold", 33),
    z("Beitrag im Ausführungsstadium, zumindest", 140, 232, beim("streng", "Beitrag"), size=32),
    z("Kontakt während der Tat", 140, 274, beim("streng", "Kontakt"), size=32),
    z("Ansgar nur Anstifter", 140, 318, "streng2", "Bold", 32),
    karte(110, 400, 1040, 160, "gemae", fill=BLAUHELL, rund=18, schatten=6, rand=4),
    z("gemäßigte Tatherrschaftslehre:", 140, 415, "gemae", "ExtraBold", 33),
    z("Beitrag in der Vorbereitung genügt, wenn ein", 140, 462, beim("gemae", "Vorbereitung"), size=32),
    z("Plus an Planung das Fehlen am Tatort ausgleicht", 140, 504, beim("gemae", "Plus"), size=32),
    karte(110, 585, 1040, 160, "bgh_a", fill=LILAHELL, rund=18, schatten=6, rand=4),
    z("BGH: keine Anwesenheit am Tatort nötig,", 140, 600, "bgh_a", "ExtraBold", 33),
    z("auch eine bloße Vorbereitung kann reichen", 140, 647, beim("bgh_a", "Auch"), size=32),
    fund("BGH 3 StR 363/22, Rn. 8; BGH, Beschl. v. 6.8.2019 – 3 StR 189/19, Rn. 4", 140, 760, beim("bgh_a", "Vorbereitung")),
    fund("Lehre: nach Hefendehl, Vorlesung StGB AT, Uni Freiburg, KK 711 f.", 140, 800, beim("streng", "Ausführungsstadium")),
    *figur_kette("AN", XS, "ans", "ruhig", [("ernst", "streng"), ("still", "streng2"), ("ruhig", "gemae"), ("froh", "bgh_a")]),
    pl("nicht dabei", XS, 160, "ans", fill=WEISS, size=30, anker="m", bis="streng2"),
    ficon("fluent-emoji-flat", "house", XS, 370, 90, "ans", bis="gemae"),
    pl("nur Anstifter?", XS, 160, "streng2", fill=ROTHELL, size=30, anker="m", anim="cut", bis="gemae"),
    pl("Plus an Planung", XS, 160, "gemae", fill=BLAU, size=30, anker="m", anim="cut", bis="bgh_a"),
    ficon("fluent-emoji-flat", "spiral-notepad", XS, 370, 90, "gemae", anim="cut", bis="bgh_a"),
    pl("Gesamtbetrachtung", XS, 160, "bgh_a", fill=LILA, size=30, anker="m", anim="cut"),
    ficon("fluent-emoji-flat", "balance-scale", XS, 380, 110, "bgh_a", anim="cut"),
]))

# ===========================================================================================================================
# L Streitentscheid
# ===========================================================================================================================
folie([("ents", f"{PC} › Streitentscheid"), ("ans3", "Ergebnis C · Ansgar: Mittäter")], rechts_frei([
    *tafel("ents", "Streitentscheid"),
    blk(110, 170, 1040, 80, BLAUHELL, "ents", [("Wir folgen der gemäßigten Ansicht", "ExtraBold", 34, INK)]),
    z("Gewicht des Beitrags entscheidet,", 110, 285, "arg1", "Bold", 34),
    z("nicht sein Zeitpunkt", 110, 330, beim("arg1", "nicht"), "Bold", 34),
    z("sonst stünde besser da, wer so gut plant,", 110, 400, "arg2", size=33),
    z("dass er selbst nicht hingehen muss", 110, 445, beim("arg2", "dass"), size=33),
    ok(135, 535, "ans2", gr=18),
    z("Ansgar: Idee, Ort, Zeit und Rollen,", 175, 515, "ans2", "Bold", 34),
    z("will 1/3 der Beute", 175, 560, beim("ans2", "will"), "Bold", 34),
    z("gleicht das Fehlen am Tatort aus", 175, 610, "ans3", size=33),
    blk(110, 675, 1040, 90, GRUENHELL, beim("ans3", "Auch"), [("Ansgar: Mittäter (+), auch nach dem BGH", "ExtraBold", 34, INK)]),
    fund("vgl. BGH, Beschl. v. 6.8.2019 – 3 StR 189/19, Rn. 7 (Planer als Mittäter)", 150, 780, beim("ans3", "Bundesgerichtshof")),
    *figur_kette("AN", XS, "ents", "ernst", [("entschlossen", "ans2"), ("still", beim("ans3", "Auch"))]),
    pl("Gewicht, nicht Zeitpunkt", XS, 160, "arg1", fill=WEISS, size=30, anker="m", bis="ans2"),
    ficon("fluent-emoji-flat", "balance-scale", XS, 380, 110, "arg1", bis="ans2"),
    pl("1/3 der Beute", XS, 160, "ans2", fill=GELB, size=30, anker="m", anim="cut", bis=beim("ans3", "Auch")),
    ficon("fluent-emoji-flat", "money-bag", XS, 380, 90, "ans2", anim="cut", bis=beim("ans3", "Auch")),
    pl("Mittäter", XS, 160, beim("ans3", "Auch"), fill=GRUEN, size=30, anker="m", anim="cut"),
]))

# ===========================================================================================================================
# M Rechtsfolge und Exzess
# ===========================================================================================================================
folie([("rf", "Rechtsfolge › wechselseitige Zurechnung"), ("exz", "Rechtsfolge › Grenze: Exzess")], rechts_frei([
    *tafel("rf", "Rechtsfolge"),
    z("Drohung und Wegnahme werden allen", 110, 180, "rf", "Bold", 34),
    z("Mittätern wechselseitig zugerechnet", 110, 225, beim("rf", "wechselseitig"), "Bold", 34),
    blk(110, 295, 1040, 80, GELB, beim("rf", "jeder"), [("jeder wird als Täter bestraft", "ExtraBold", 34, INK)]),
    z("Grenze: der Tatplan", 110, 435, "exz", "ExtraBold", 34),
    nein(135, 520, beim("exz", "Weicht"), gr=18),
    z("wesentliche Abweichung = Exzess,", 175, 500, beim("exz", "Weicht"), size=33),
    z("wird den anderen nicht zugerechnet", 175, 545, beim("exz", "wird"), size=33),
    fund("BGH, Urt. v. 26.9.2024 – 4 StR 115/24, Rn. 44", 150, 600, beim("exz", "zugerechnet")),
    *vier("rf", {"KI": [("ernst", "exz")], "FE": [("ernst", "exz")], "TH": [("ernst", "exz")], "AN": [("ernst", "exz")]},
          start={"KI": "still", "FE": "still", "TH": "ruhig", "AN": "still"}),
    pl("wechselseitig", 1555, 160, "rf", fill=GELB, size=30, anker="m", bis="exz"),
    ficon("fluent-emoji-flat", "link", (X4["KI"] + X4["FE"]) // 2, 300, 90, "rf", bis="exz"),
    pl("Grenze: Tatplan", 1555, 160, "exz", fill=ROTHELL, size=30, anker="m", anim="cut"),
    ficon("fluent-emoji-flat", "spiral-notepad", (X4["KI"] + X4["FE"]) // 2, 300, 80, "exz", anim="cut"),
]))

# ===========================================================================================================================
# N Ergebnis für alle vier
# ===========================================================================================================================
folie([("erg", "Ergebnis · Kilian, Fenja, Ansgar: Raub in Mittäterschaft"), ("erg2", "Ergebnis · Thea: Beihilfe zum Raub")],
      rechts_frei([
    *tafel("erg", "Ergebnis"),
    karte(110, 175, 1040, 200, "erg", fill=GRUENHELL, rund=18, schatten=6, rand=4),
    z("Kilian, Fenja und Ansgar:", 140, 195, "erg", "ExtraBold", 36),
    z("Raub in Mittäterschaft,", 140, 250, beim("erg", "Raub"), "Bold", 34),
    z("§§ 249 Abs. 1, 25 Abs. 2 StGB", 140, 300, beim("erg", "Paragrafen"), "Bold", 34),
    karte(110, 410, 1040, 200, "erg2", fill=BLAUHELL, rund=18, schatten=6, rand=4),
    z("Thea: Beihilfe zum Raub,", 140, 430, "erg2", "ExtraBold", 36),
    z("§§ 249 Abs. 1, 27 Abs. 1 StGB", 140, 485, beim("erg2", "Paragraf"), "Bold", 34),
    z("Strafe gemildert, § 27 Abs. 2 StGB", 140, 535, beim("erg2", "Ihre"), size=33),
    *vier("erg", {"KI": [("still", "erg2")], "FE": [("still", "erg2")], "AN": [("still", "erg2")], "TH": [("sorge", "erg2")]},
          start={"KI": "ernst", "FE": "ernst", "TH": "ruhig", "AN": "ernst"}),
    pl("Mittäter", (X4["KI"] + X4["FE"]) // 2, 440, "erg", fill=GRUEN, size=30, anker="m"),
    pl("Mittäter", X4["AN"], 365, beim("erg", "Ansgar"), fill=GRUEN, size=30, anker="m"),
    pl("Gehilfin", X4["TH"], 440, "erg2", fill=BLAU, size=30, anker="m"),
]))

# ===========================================================================================================================
# O Klausurtipp (Lexi)
# ===========================================================================================================================
LXX = 1560
folie([("tipp", "Klausurtipp · Zurechnung am fehlenden Merkmal"), ("tipp3", "Klausurtipp · Streit nur, wenn er zählt")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Zurechnung genau dort prüfen,", 200, 200, beim("tipp", "Zurechnung"), "ExtraBold", 36),
    z("wo dem Beteiligten ein Merkmal fehlt", 200, 247, beim("tipp", "wo"), "ExtraBold", 36),
    z("bei Kilian: bei der Wegnahme", 200, 330, "tipp2", "Bold", 34),
    z("Streit um den Planer nur entscheiden,", 200, 430, "tipp3", "Bold", 34),
    z("wenn die Ansichten zu verschiedenen", 200, 477, beim("tipp3", "wenn"), "Bold", 34),
    z("Ergebnissen kommen", 200, 524, beim("tipp3", "Ergebnissen"), "Bold", 34),
    z("bei Ansgar: ja", 200, 610, beim("tipp3", "Bei"), "ExtraBold", 34),
    *redet("LX_warnt", LXX, BR, 540, "tipp", "sch"),
    namensschild("Lexi", LXX, BR, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# P Klausurschema
# ===========================================================================================================================
K1, K2, K3 = 150, 230, 310
PSS = "Klausurschema"
folie([("sch", PSS), ("s_i", f"{PSS} › I. Tatbestand"), ("s2", f"{PSS} › I. 2. Zurechnung, § 25 Abs. 2 StGB"),
       ("s3", f"{PSS} › I. 3. subjektiver Tatbestand"), ("s_ii", f"{PSS} › II. Rechtswidrigkeit"),
       ("s_iii", f"{PSS} › III. Schuld")], [
    karte(60, 50, 1800, 920, "sch"),
    titel("Klausurschema: Mittäterschaft mit Zurechnung, § 25 Abs. 2 StGB", 110, 90, "sch", 48),
    z("I. Tatbestand", K1, 190, "s_i", "Bold", 38, rechts=1820),
    z("1. objektive Merkmale, die der Beteiligte selbst erfüllt", K2, 255, "s1", size=34, rechts=1820),
    z("2. für die übrigen: Zurechnung nach § 25 Abs. 2 StGB", K2, 320, "s2", "Bold", 34, rechts=1820),
    z("a) gemeinsamer Tatplan (kein Exzess)", K3, 380, "s2a", size=34, rechts=1820),
    z("b) gemeinsame Tatausführung: wesentlicher Tatbeitrag, Abgrenzung zur Beihilfe", K3, 440, "s2b", size=34, rechts=1820),
    z("3. subjektiver Tatbestand in eigener Person", K2, 505, "s3", "Bold", 34, rechts=1820),
    z("II. Rechtswidrigkeit", K1, 590, "s_ii", "Bold", 38, rechts=1820),
    z("III. Schuld", K1, 660, "s_iii", "Bold", 38, rechts=1820),
])

# ===========================================================================================================================
# Q Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 170, "merke", 84, anker="m"),
    *merktext([[("Mittäter", "a"), (" ist, wer auf Grund eines", 0)],
               [("gemeinsamen Tatplans", "b"), (" einen", 0)], [("wesentlichen Beitrag", "c"), (" leistet.", 0)]],
              750, 270, 42, "merke", {"a": beim("merke", "Mittäter"), "b": beim("merke", "gemeinsamen"),
                                      "c": beim("merke", "wesentlichen")}, 1300),
    *merktext([[("Dann wird ihm ", 0), ("zugerechnet", "d"), (", was die", 0)], [("anderen im Rahmen des Plans tun.", 0)]],
              750, 495, 42, "m_2", {"d": beim("m_2", "zugerechnet")}, 1300),
    *merktext([[("Nicht die Anwesenheit am Tatort entscheidet,", 0)], [("sondern das ", 0), ("Gewicht des Beitrags", "e"), (".", 0)]],
              750, 660, 42, "m_3", {"e": beim("m_3", "Gewicht")}, 1300),
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
