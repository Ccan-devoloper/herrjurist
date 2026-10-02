"""Folge 064 · Abschleppfall: Musst du die Kosten zahlen? – Serienstandard Open Peeps (Katzenkönig).
Übungsfall (Beispielland Nordrhein-Westfalen), Figuren fiktiv. Szenen laut ../SZENENPLAN.md: A Vor der Apotheke (Frau Kaiser
parkt auf dem Parkplatz für schwerbehinderte Menschen), B Das Ordnungsamt kommt (Herr Meier), C Am Haken (Herr Becker vom
Abschleppdienst), D Kostenbescheid und Frage, E Sachverhalt, F Drei Ebenen und Landesrecht, G Kostenbescheid: Grundlage,
formell, Konnexität, H Das Schild (Wortlaut Anlage 3 StVO, § 12 II StVO), I Allgemeinverfügung, Sichtbarkeit, Wegfahrgebot,
J Ersatzvornahme (Wortlaut § 59 I VwVG NRW), K Gestreckt oder sofort, L Verhältnismäßigkeit: erforderlich, M angemessen und
Gegenfälle, N Ergebnis und Kosten, O Klausurtipp (Lexi), P Klausurschema, Q Merksatz (Lexi).
Geräusche nur bei sichtbarer Handlung: Autotür, als das Auto auf dem Parkplatz steht (Szene A), Kette am Haken (Szene C)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_064/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
ZITAT = (246, 246, 250, 255)
ZARTGRUEN = (236, 248, 236, 255)
HC = "fluent-emoji-high-contrast"
DAUER = bausteine._cj()["dauer"]
T_ = bausteine._t

_CMAP = set(TTFont(SP + "humaaans/fonts/Nunito[wght].ttf").getBestCmap())


def glyphen(text):
    """Nunito muss jedes Zeichen haben (sonst Kästchen)."""
    fehl = {c for c in text if ord(c) not in _CMAP and not c.isspace()}
    assert not fehl, f"Zeichen fehlt in Nunito: {fehl} in {text!r}"
    return text


def z(text, x, y, cue, stil="Regular", size=34, farbe=INK, d=0.0, rechts=1170, **k):
    """Tafelzeile, die rechts nicht über die Karte hinausragen darf; Mindestschrift 26 px (mobile Lesbarkeit)."""
    assert size >= 26, f"Schrift zu klein: {text}"
    e = zeile(glyphen(text), x, y, cue, stil, size, farbe=farbe, d=d, **k)
    assert e.x + e.sprite.width <= rechts, f"Zeile zu breit: {text} ({e.x + e.sprite.width:.0f} > {rechts})"
    return e


def pl(text, *a, **k):
    assert k.get("size", 40) >= 26, f"Pille zu klein: {text}"
    return pille(glyphen(text), *a, **k)


def tafel(cue, titel_, h=840, fill=WEISS, size=46):
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(glyphen(titel_), 110, 100, cue, size)]


def blk(x, y, w, h, fill, cue, zeilen, **k):
    return fl_block(x, y, w, h, fill, cue, [(glyphen(t), s, g, f) for t, s, g, f in zeilen], **k)


def bis_(el, bis):
    el.bis = bis
    return el


def hart(e):
    e.anim = "cut"
    return e


def lexi_bis_ende(cue):
    return (cue, round(DAUER - T_(cue) - 0.05, 3))


def zit(text, x, y, cue, size=26, rechts=1170):
    """Fundstellenzeile (grau, klein, mindestens 26 px)."""
    return z(text, x, y, cue, size=size, farbe=TEXT, rechts=rechts)


def rechts_frei(els, x0=1250):
    """Figuren und Requisiten der Tafelfolien stehen rechts der Tafel."""
    for e in els:
        n = e.name or ""
        if n.startswith(("bild:", "ficon:")) or "/op_064/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def wortlaut(x, y, w, text, quelle, cue, marken=(), size=32, bis=None, zeilen=None):
    """Wortlautkarte: Normtext wörtlich nach der amtlichen Quelle, als Zitat mit Normangabe; feste Zeilen ergeben zusammen
    genau den Normtext. marken = [(Wortgruppe, cue)] legt synchron zum gesprochenen Wort einen Textmarker hinter die
    Wortgruppe (die Wortgruppe muss in einer Zeile stehen)."""
    f = F("Regular", size)
    tx, ty = x + 28, y + 26
    assert " ".join(t.strip() for t in zeilen) == text, "feste Zeilen weichen vom Normtext ab"
    lh = int(size * 1.42)
    hgt = 40 + lh * len(zeilen) + 46
    els = [bis_(karte(x, y, w, hgt, cue, fill=ZITAT, rund=18, schatten=6, rand=4), bis)]
    for wort, mc in marken:
        zi = next((i for i, t in enumerate(zeilen) if wort in t), None)
        assert zi is not None, f"Marker {wort!r} steht nicht in einer Zeile: {zeilen}"
        t = zeilen[zi]; a = t.index(wort)
        x0 = tx + f.getlength(t[:a]) - 4
        x1 = tx + f.getlength(t[:a + len(wort)]) + 4
        y0 = ty + zi * lh + size * 0.30
        im = Image.new("RGBA", (int(x1 - x0) + 2, int(size * 0.85)))
        ImageDraw.Draw(im).rounded_rectangle((0, 0, im.width - 1, im.height - 1), 7, fill=MARKER)
        els.append(El(im, x0, y0, mc, "fade", 0.0, bis, name="marker:" + wort))
    for i, t in enumerate(zeilen):
        els.append(z(t, tx, ty + i * lh, cue, size=size, rechts=x + w - 16, bis=bis))
    els.append(z(quelle, tx, ty + len(zeilen) * lh + 4, cue, "Bold", 26, farbe=TEXT, rechts=x + w - 16, bis=bis))
    return els, y + hgt


# --- Eigene Hilfsfunktion (wie Folge 061/052/049/044): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt -----------
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
    """Wie bausteine.redet(), aber Wortende = hörbares Ende; Viseme aus der Schreibung geschätzt."""
    cj = bausteine._cj(); ta, tb = T_(cue), T_(bis)
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


def fig(name, cx, unten, hoehe, folge, bis=None, erst="pop", d=0.0):
    """Mimikfolge einer Figur am selben Platz: folge = [(cue, suffix)] → harte Schnitte."""
    els = []
    for i, (c, s) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else bis
        els.append(peep_voll(f"{name}_{s}", cx, unten, hoehe, c, anim=erst if i == 0 else "cut", d=d if i == 0 else 0.0, bis=b))
    return els


def schild(text, cx, cue, fill, d=0.2, bis=None, unten=None, size=28):
    """Namensschild unter der Figur (ab dem ersten Auftritt, solange sie im Bild ist)."""
    return pl(text, cx, (unten or FB) + 22, cue, fill=fill, size=size, anker="m", d=d, bis=bis)


def parkschild(cx, cue, boden=None, gross=1.0, anim="pop", bis=None, mast=True):
    """Verkehrsschild Parken (Zeichen 314, Tabler „parking“) mit Zusatzzeichen Rollstuhlfahrersinnbild (Fluent Emoji
    High Contrast „wheelchair-symbol“, weiß gefüllt) an einem Mast; nur Bibliotheks-Icons, Mast als Tuschelinie."""
    boden = boden or BODEN
    g1, g2 = int(130 * gross), int(104 * gross)
    unten2 = boden - int(250 * gross)
    unten1 = unten2 - g2 - int(6 * gross)
    els = []
    if mast:
        els.append(bis_(linienzug([(cx, unten2 - 4), (cx, boden)], cue, breite=max(6, int(10 * gross)), farbe=INK), bis))
        els[-1].anim = "cut" if anim == "cut" else "fade"
    els += [ficon("tabler", "parking", cx, unten1, g1, cue, fuell=BLAU, anim=anim, bis=bis),
            ficon(HC, "wheelchair-symbol", cx, unten2, g2, cue, fuell=WEISS, anim=anim, bis=bis)]
    return els


def auto(cx, unten, cue, anim="pop", bis=None, breite=360):
    """Das Auto von Frau Kaiser (Tabler „car“, rosa) – in jeder Szene gleich."""
    return ficon("tabler", "car", cx, unten, breite, cue, fuell=PINK, anim=anim, bis=bis)


def apotheke(cx, cue, anim="pop", schrift=True):
    els = [ficon("tabler", "building-store", cx, BODEN, 400, cue, fuell=GRUEN, anim=anim)]
    if schrift:
        els.append(pl("Apotheke", cx, BODEN - 470, cue, fill=WEISS, size=30, anker="m", anim=anim))
    return els


BODEN, FH = 880, 480
FX, FB, FR = 1560, 930, 460                 # Figur neben der Tafel
IX, IU = 1560, 400                          # Requisit über der Figur
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
KA_F, ME_F, BE_F = LILA, BLAU, ORANGE       # Farben der Namensschilder
SX, AX, APX = 220, 600, 1580                # Schild, Auto, Apotheke
K1, K2, K3 = 150, 210, 270

# A Fall: Vor der Apotheke ---------------------------------------------------------------------------------------------------
KAX = 1080
KAb = ("KA_redet_r", KAX, BODEN, FH)
PARKT = beim("park", "Parkplatz")
ein = auto(AX, BODEN, beim("park", "stellt"), anim="cut")
bewegt(ein, beim("park", "stellt"), PARKT, -380)
szene(ein, "064tuer*", 0.8, round(T_(PARKT) - T_(beim("park", "stellt")), 3))
folie([(NULL, "Fall · Vor der Apotheke")], [
    hart(linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK)),
    hart(pl("Vormittag in Nordrhein-Westfalen", 70, 40, NULL, fill=GELB, size=40)),
    *apotheke(APX, NULL, anim="cut"),
    ein,
    pl("Parkplatz für schwerbehinderte Menschen", AX, BODEN + 30, beim("park", "schwerbehinderte"), fill=WEISS, size=28, anker="m"),
    *fig("KA", KAX, BODEN, FH, [(PARKT, "froh_r")], bis="ka1"),
    *redet("KA_redet_r", KAX, BODEN, FH, "ka1", "meier"),
    schild("Frau Kaiser", KAX, PARKT, KA_F, unten=BODEN, d=0.0),
    *parkschild(SX, "schild"),
    pl("gut zu sehen", SX + 40, 330, beim("schild", "gut"), fill=WEISS, size=28, anker="m"),
    pl("kein Parkausweis", AX + 40, 560, "ausweis", fill=ROT, size=30, anker="m"),
    blase("sprech", 680, 210, "ka1", 1240, 230, inhalt=["Nur 5 Minuten, ich bin", "gleich wieder da."],
          textsize=31, figur=KAb),
])

# B Fall: Das Ordnungsamt kommt ------------------------------------------------------------------------------------------------
MEX = 1150
MEb = ("ME_redet", MEX, BODEN, FH)
folie([("meier", "Fall · Das Ordnungsamt kommt")], [
    linienzug([(60, BODEN), (1860, BODEN)], "meier", breite=7, farbe=INK),
    pl("Kurz darauf", 70, 40, "meier", fill=GELB, size=40),
    *apotheke(APX, "meier"),
    auto(AX, BODEN, "meier"),
    *parkschild(SX, "meier"),
    pl("Parkplatz für schwerbehinderte Menschen", AX, BODEN + 30, "meier", fill=WEISS, size=28, anker="m"),
    *fig("ME", MEX, BODEN, FH, [(beim("meier", "Herr"), "ernst"), ("ruft", "denkt")], bis="me1"),
    *redet("ME_redet", MEX, BODEN, FH, "me1", "zurueck"),
    schild("Herr Meier, Ordnungsamt", MEX, beim("meier", "Herr"), ME_F, unten=BODEN),
    pl("kein Parkausweis", AX + 40, 200, beim("kein", "Kein"), fill=ROT, size=30, anker="m"),
    pl("niemand am Wagen", AX + 40, 270, beim("kein", "niemand"), fill=ROT, size=30, anker="m"),
    pl("kein Zettel", AX + 40, 340, beim("kein", "Zettel"), fill=ROT, size=30, anker="m"),
    ficon(HC, "mobile-phone", AX + 40, 500, 70, "ruft", fuell=WEISS),
    pl("Abschleppwagen bestellt", AX + 40, 520, beim("ruft", "Abschleppwagen"), fill=GELB, size=28, anker="m"),
    blase("sprech", 700, 210, "me1", 1290, 220, inhalt=["Der Platz muss frei sein.", "Das Auto wird abgeschleppt."],
          textsize=30, figur=MEb),
])

# C Fall: Am Haken ------------------------------------------------------------------------------------------------------------
KC, BX = 1500, 1060
KCb = ("KA_aerger_redet", KC, BODEN, FH)
BEb = ("BE_redet_r", BX, BODEN, FH)
KR, KRU = 760, BODEN                          # Abschleppwagen (Tabler „car-crane“)
HAKEN = "haken"
folie([("zurueck", "Fall · Am Haken")], [
    linienzug([(60, BODEN), (1860, BODEN)], "zurueck", breite=7, farbe=INK),
    pl("10 Minuten später", 70, 40, "zurueck", fill=GELB, size=40),
    *parkschild(SX, "zurueck"),
    *fig("KA", KC, BODEN, FH, [(beim("zurueck", "Frau"), "froh"), (HAKEN, "sorge")], bis="ka2"),
    *redet("KA_aerger_redet", KC, BODEN, FH, "ka2", "be1"),
    *fig("KA", KC, BODEN, FH, [("be1", "aerger")], erst="cut"),
    schild("Frau Kaiser", KC, beim("zurueck", "Frau"), KA_F, unten=BODEN),
    szene(ficon("tabler", "car-crane", KR, KRU, 430, HAKEN, fuell=GELB), "064kette*", 0.8, 0.0),
    auto(400, BODEN - 70, HAKEN, breite=320),
    linienzug([(585, 640), (548, 676)], HAKEN, breite=8, farbe=INK),
    ficon(HC, "hook", 540, 712, 44, HAKEN, fuell=WEISS),
    pl("am Haken", 400, 520, beim("haken", "Haken"), fill=ROT, size=30, anker="m"),
    *fig("BE", BX, BODEN, FH, [(beim("becker", "Herr"), "ruhig_r")], bis="be1"),
    *redet("BE_redet_r", BX, BODEN, FH, "be1", "bescheid"),
    schild("Herr Becker, Abschleppdienst", BX, beim("becker", "Herr"), BE_F, unten=BODEN),
    pl("auf den Hof", KR, 450, beim("becker", "Hof"), fill=WEISS, size=30, anker="m"),
    blase("sprech", 640, 190, "ka2", 1480, 200, inhalt=["Ich war doch nur", "5 Minuten weg!"], textsize=32, figur=KCb,
          bis="be1"),
    blase("sprech", 620, 190, "be1", 900, 210, inhalt=["Den Auftrag hat", "die Stadt gegeben."], textsize=32, figur=BEb),
])

# D Kostenbescheid und Frage --------------------------------------------------------------------------------------------------
folie([("bescheid", "Fall · Der Kostenbescheid"), ("frage", "Fall · Muss Frau Kaiser zahlen?")], [
    pl("Eine Woche später", 70, 40, "bescheid", fill=GELB, size=40),
    ficon("tabler", "receipt-euro", 640, 520, 230, beim("bescheid", "Kostenbescheid"), fuell=WEISS),
    pl("Kostenbescheid der Stadt", 640, 560, beim("bescheid", "Kostenbescheid"), fill=WEISS, size=34, anker="m"),
    pl("250 €: Abschleppkosten und Verwaltungsgebühr", 640, 650, "betrag", fill=GELB, size=34, anker="m"),
    pl("Muss Frau Kaiser zahlen?", 640, 790, "frage", fill=PINK, size=44, anker="m"),
    *fig("KA", FX, FB, FR, [("bescheid", "denkt"), ("frage", "sorge")]),
    schild("Frau Kaiser", FX, "bescheid", KA_F),
])

# E Sachverhalt ---------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Nordrhein-Westfalen: Frau Kaiser parkt ihr Auto ohne Parkausweis auf einem Parkplatz für schwerbehinderte Menschen "
    "vor einer Apotheke. Das Schild mit Zusatzzeichen ist gut zu sehen. „Nur 5 Minuten“, denkt sie. Herr Meier vom "
    "Ordnungsamt findet niemanden am Wagen und keinen Zettel. Er bestellt einen Abschleppwagen. Nach 10 Minuten hängt das "
    "Auto am Haken; Herr Becker vom Abschleppdienst bringt es auf den Hof. Die Stadt hört Frau Kaiser an und schickt einen "
    "Kostenbescheid über 250 €: Abschleppkosten und Verwaltungsgebühr.",
], "Muss Frau Kaiser zahlen?")

# F Drei Ebenen und Landesrecht ------------------------------------------------------------------------------------------------
folie([("ebenen", "Prüfung · Drei Ebenen"), ("land", "Prüfung · Landesrecht, Beispiel Nordrhein-Westfalen")], rechts_frei([
    *tafel("ebenen", "Drei Ebenen im Abschleppfall"),
    blk(110, 180, 1040, 72, BLAU, "e1", [("1. das Verkehrszeichen", "ExtraBold", 36, INK)]),
    blk(110, 270, 1040, 72, GELB, "e2", [("2. das Abschleppen", "ExtraBold", 36, INK)]),
    blk(110, 360, 1040, 72, GRUEN, "e3", [("3. die Kosten", "ExtraBold", 36, INK)]),
    z("Vollstreckungsrecht ist Landesrecht", 110, 485, "land", "Bold", 36),
    z("Beispiel hier: Nordrhein-Westfalen", 150, 545, beim("land", "Nordrhein"), size=34),
    zit("VwVG NRW (ab 1.4.2025), VO VwVG NRW (ab 1.1.2026), OBG NRW (ab 1.7.2026)", 150, 600, beim("land", "Beispiel")),
    z("andere Länder: ähnliche Regeln,", 110, 670, beim("land", "anderen"), size=34),
    z("oft unter anderer Nummer", 150, 725, beim("land", "Nummer"), size=34),
    *parkschild(IX, "e1", boden=IU + 40, gross=0.9, mast=False, bis="e2"),
    ficon("tabler", "car-crane", IX, IU, 230, "e2", fuell=GELB, bis="e3"),
    ficon("tabler", "receipt-euro", IX, IU, 120, "e3", fuell=WEISS),
    *fig("KA", FX, FB, FR, [("ebenen", "denkt")]),
    schild("Frau Kaiser", FX, "ebenen", KA_F),
]))

# G Kostenbescheid: Grundlage, formell, Konnexität --------------------------------------------------------------------------------
folie([("egl", "1. Ermächtigungsgrundlage: § 77 I VwVG NRW"), ("formell", "2. formell: Zuständigkeit, Anhörung"),
       ("konnex", "3. materiell › rechtmäßiges Abschleppen")], rechts_frei([
    *tafel("egl", "Der Kostenbescheid"),
    z("Grundlage: § 77 Abs. 1 VwVG NRW", 110, 180, beim("egl", "Grundlage"), "Bold", 36),
    z("mit der Ausführungsverordnung (VO VwVG NRW)", 150, 238, beim("egl", "Ausführungsverordnung"), size=34),
    z("Abschleppkosten als Auslagen", 150, 310, "ausl", size=34),
    zit("§ 20 Abs. 2 Satz 2 Nr. 7 VO VwVG NRW", 190, 360, beim("ausl", "Auslagen")),
    z("dazu eine Gebühr", 150, 420, "geb", size=34),
    zit("§ 15 Abs. 1 lfd. Nr. 7 VO VwVG NRW: 30 bis 180 €", 190, 470, beim("geb", "Gebühr")),
    z("formell: keine Probleme", 195, 530, "formell", size=34),
    ok(150, 553, beim("formell", "Probleme"), gr=20),
    z("Stadt zuständig, Frau Kaiser angehört", 235, 580, beim("formell", "zuständig"), size=32),
    z("materiell:", 110, 645, "konnex", "Bold", 36),
    blk(110, 695, 1040, 80, GELB, beim("konnex", "Kosten"), [("Kosten nur bei rechtmäßigem Abschleppen", "ExtraBold", 36, INK)]),
    zit("BVerwG, Urt. v. 24.5.2018 – 3 C 25.16, Rn. 11", 150, 792, beim("konnex", "rechtmäßig")),
    ficon("tabler", "receipt-euro", IX, IU, 130, "egl", fuell=WEISS, bis="konnex"),
    ficon("tabler", "car-crane", IX, IU, 230, "konnex", fuell=GELB),
    *fig("KA", FX, FB, FR, [("egl", "denkt"), ("konnex", "sorge")]),
    schild("Frau Kaiser", FX, "egl", KA_F),
]))

# H Das Schild: Wortlaut Anlage 3 StVO, § 12 II StVO ------------------------------------------------------------------------
GVA = "3. materiell › a) Grundverwaltungsakt"
W314 = ("„1. Wer ein Fahrzeug führt, darf hier parken. … d) Durch ein Zusatzzeichen mit Rollstuhlfahrersinnbild kann die "
        "Parkerlaubnis beschränkt sein auf schwerbehinderte Menschen mit außergewöhnlicher Gehbehinderung, beidseitiger "
        "Amelie oder Phokomelie oder mit vergleichbaren Funktionseinschränkungen sowie auf blinde Menschen. e) Die "
        "Parkerlaubnis gilt nur, wenn der Parkschein, die Parkscheibe oder der Parkausweis gut lesbar ausgelegt oder "
        "angebracht ist.“")
Z314 = ["„1. Wer ein Fahrzeug führt, darf hier parken. …",
        "d) Durch ein Zusatzzeichen mit Rollstuhlfahrersinnbild kann die",
        "Parkerlaubnis beschränkt sein auf schwerbehinderte Menschen mit",
        "außergewöhnlicher Gehbehinderung, beidseitiger Amelie oder",
        "Phokomelie oder mit vergleichbaren Funktionseinschränkungen sowie",
        "auf blinde Menschen. e) Die Parkerlaubnis gilt nur, wenn der Parkschein,",
        "die Parkscheibe oder der Parkausweis gut lesbar ausgelegt oder",
        "angebracht ist.“"]
w314, w314_y = wortlaut(70, 150, 1120, W314, "Anlage 3 StVO, lfd. Nr. 7 (Zeichen 314), Ge- oder Verbot Nr. 1, 2 d) und e)",
                        "wl314", size=28, zeilen=Z314,
                        marken=[("darf hier parken", beim("wl314", "erlaubt")),
                                ("Zusatzzeichen mit Rollstuhlfahrersinnbild", beim("wl314", "Zusatzzeichen")),
                                ("außergewöhnlicher Gehbehinderung", beim("wl314", "außergewöhnlicher")),
                                ("vergleichbaren Funktionseinschränkungen", beim("wl314", "vergleichbaren")),
                                ("blinde Menschen", beim("wl314", "blinde")),
                                ("Parkausweis gut lesbar ausgelegt", beim("gilt", "lesbar"))])
folie([("gva", f"{GVA}: das Schild"), ("fuenf", f"{GVA} › Parken, § 12 II StVO")], rechts_frei([
    titel(glyphen("Was hat die Stadt vollstreckt? Das Schild."), 100, 70, "gva", 42),
    *w314,
    z("für alle anderen: Parken dort verboten", 110, w314_y + 25, "andere", "Bold", 34),
    zit("VG Düsseldorf, Urt. v. 28.3.2017 – 14 K 6945/16, Rn. 21", 150, w314_y + 78, beim("andere", "verboten")),
    z("„Nur 5 Minuten“ hilft nicht:", 110, w314_y + 140, "fuenf", "Bold", 34),
    z("„Wer sein Fahrzeug verlässt oder länger als drei", 150, w314_y + 195, beim("fuenf", "Wer"), size=30),
    z("Minuten hält, der parkt.“ (§ 12 Abs. 2 StVO)", 150, w314_y + 238, beim("fuenf", "Wer"), size=30),
    *parkschild(IX, "gva", boden=IU + 40, gross=0.9, mast=False),
    *fig("KA", FX, FB, FR, [("gva", "denkt"), ("fuenf", "sorge")]),
    schild("Frau Kaiser", FX, "gva", KA_F),
]))

# I Allgemeinverfügung, Sichtbarkeit, Wegfahrgebot -----------------------------------------------------------------------------
folie([("va", f"{GVA} › Allgemeinverfügung, Bekanntgabe"), ("weg", f"{GVA} › Wegfahrgebot, sofort vollziehbar")], rechts_frei([
    *tafel("va", "Das Schild als Verwaltungsakt"),
    z("Allgemeinverfügung, § 35 Satz 2 VwVfG", 110, 180, beim("va", "Allgemeinverfügung"), "Bold", 34),
    zit("in NRW wortgleich: § 35 Satz 2 VwVfG NRW", 150, 230, beim("va", "Paragraf")),
    z("bekannt gegeben durch das Aufstellen", 110, 290, "bekannt", size=34),
    z("Sichtbarkeitsgrundsatz: wirkt gegenüber jedem,", 110, 350, "sicht", "Bold", 34),
    z("erfassbar „mit einem raschen und beiläufigen Blick“,", 150, 403, beim("sicht", "raschen"), size=32),
    z("ob man es sieht oder nicht", 150, 453, beim("sicht", "sieht"), size=32),
    z("beim Parken: einfache Umschau nach dem Aussteigen", 110, 515, "umschau", size=33),
    zit("BVerwG, Urt. v. 6.4.2016 – 3 C 10.15, Rn. 16, 19", 150, 565, beim("umschau", "Aussteigen")),
    blk(110, 620, 1040, 72, GELB, "weg", [("zugleich: Wegfahrgebot", "ExtraBold", 36, INK)]),
    z("sofort vollziehbar: § 80 Abs. 2 Satz 1 Nr. 2 VwGO analog", 110, 712, "sofort", "Bold", 32),
    z("Regel für unaufschiebbare Anordnungen von Polizeivollzugsbeamten", 150, 765, "polizei", size=28),
    zit("BVerwG, Urt. v. 24.5.2018 – 3 C 25.16, Rn. 14", 150, 812, beim("polizei", "Polizeivollzugsbeamten")),
    *parkschild(IX, "va", boden=IU + 40, gross=0.9, mast=False, bis="sicht"),
    ficon("tabler", "eye", IX, IU, 150, "sicht", fuell=WEISS, bis="weg"),
    ficon("tabler", "car", IX, IU, 230, "weg", fuell=PINK),
    *fig("KA", FX, FB, FR, [("va", "denkt"), ("sicht", "sorge"), ("weg", "muede")]),
    schild("Frau Kaiser", FX, "va", KA_F),
]))

# J Ersatzvornahme, Wortlaut § 59 Abs. 1 Satz 1 VwVG NRW --------------------------------------------------------------------
EVP = "3. materiell › b) Ersatzvornahme"
W59 = ("„Wird die Verpflichtung, eine Handlung vorzunehmen, deren Vornahme durch einen anderen möglich ist (vertretbare "
       "Handlung), nicht erfüllt, so kann die Vollzugsbehörde auf Kosten des Betroffenen die Handlung selbst ausführen oder "
       "einen anderen mit der Ausführung beauftragen.“")
Z59 = ["„Wird die Verpflichtung, eine Handlung vorzunehmen, deren Vornahme",
       "durch einen anderen möglich ist (vertretbare Handlung), nicht erfüllt,",
       "so kann die Vollzugsbehörde auf Kosten des Betroffenen die Handlung",
       "selbst ausführen oder einen anderen mit der Ausführung beauftragen.“"]
w59, w59_y = wortlaut(70, 300, 1120, W59, "§ 59 Abs. 1 Satz 1 VwVG NRW", "wl59", size=30, zeilen=Z59,
                      marken=[("(vertretbare Handlung)", "wl59"), ("auf Kosten des Betroffenen", beim("wl59", "Kosten")),
                              ("selbst ausführen", beim("wl59", "selbst")),
                              ("einen anderen mit der Ausführung beauftragen", beim("wl59", "anderen"))])
folie([("ev", f"{EVP}, § 59 I VwVG NRW")], rechts_frei([
    titel(glyphen("Das Abschleppen: Ersatzvornahme"), 100, 75, "ev", 46),
    z("Wegfahren kann auch ein anderer:", 110, 175, beim("ev", "Wegfahren"), "Bold", 34),
    z("vertretbare Handlung", 150, 228, beim("ev", "vertretbare"), size=34),
    *w59,
    blk(110, w59_y + 40, 1040, 80, GELB, "evname", [("= Ersatzvornahme", "ExtraBold", 38, INK)]),
    ficon("tabler", "car-crane", IX, IU, 240, "ev", fuell=GELB),
    *fig("BE", FX, FB, FR, [("ev", "ruhig")]),
    schild("Herr Becker", FX, "ev", BE_F),
]))

# K Gestrecktes Verfahren oder Sofortvollzug ----------------------------------------------------------------------------------
folie([("wege", f"{EVP} › gestreckt oder sofort?"), ("nrw", f"{EVP} › sofortiger Vollzug, § 55 II VwVG NRW")], rechts_frei([
    *tafel("wege", "Zwei Wege der Vollstreckung"),
    z("gestreckt, § 55 Abs. 1 VwVG NRW:", 110, 180, "gestr", "Bold", 34),
    z("Verwaltungsakt vollstrecken, hier das Wegfahrgebot", 150, 233, beim("gestr", "Wegfahrgebot"), size=32),
    z("dazu Androhung und Festsetzung", 150, 283, beim("gestr", "Androhung"), size=32),
    nein(150, 358, beim("nrw", "erreichbaren"), gr=18),
    z("Festsetzung braucht einen erreichbaren Adressaten", 195, 335, beim("nrw", "Festsetzung"), size=32),
    blk(110, 395, 1040, 76, GRUEN, beim("nrw", "sofortigen"), [("NRW: sofortiger Vollzug, § 55 Abs. 2 VwVG NRW", "ExtraBold", 34, INK)]),
    zit("OVG NRW, Urt. v. 20.8.2020 – 5 A 2289/18, Rn. 30 f.", 150, 485, beim("nrw", "Paragraf")),
    z("ohne Androhung (§ 63 Abs. 1 Satz 5),", 150, 540, "entb", size=32),
    z("Festsetzung fällt weg (§ 64 Satz 2)", 150, 588, beim("entb", "Festsetzung"), size=32),
    ok(150, 668, beim("gefahr", "liegt"), gr=20),
    z("gegenwärtige Gefahr: Verstoß stört die öffentliche", 195, 645, beim("gefahr", "gegenwärtige"), size=32),
    z("Sicherheit schon jetzt", 195, 690, beim("gefahr", "Sicherheit"), size=32),
    zit("VG Münster, Urt. v. 14.11.2011 – 1 K 605/10, Rn. 17–20", 195, 735, beim("gefahr", "jetzt")),
    z("andere Länder z. T.: unmittelbare Ausführung (Berlin)", 110, 790, "ua", size=32),
    zit("BVerwG, Urt. v. 6.4.2016 – 3 C 10.15, Rn. 10", 150, 838, beim("ua", "Berlin")),
    ficon("tabler", "car-crane", IX, IU, 240, "wege", fuell=GELB),
    *fig("ME", FX, FB, FR, [("wege", "ruhig"), ("nrw", "denkt"), ("gefahr", "ernst")]),
    schild("Herr Meier", FX, "wege", ME_F),
]))

# L Verhältnismäßigkeit: geeignet, erforderlich, Wartezeit ------------------------------------------------------------------
VHM = "3. materiell › c) Verhältnismäßigkeit"
folie([("vhm", f"{VHM}: geeignet"), ("erf", f"{VHM}: erforderlich")], rechts_frei([
    *tafel("vhm", "Verhältnismäßigkeit", fill=ZARTGRUEN),
    ok(150, 203, beim("geeig", "geeignet"), gr=20),
    z("geeignet: Abschleppen macht den Platz frei", 195, 180, beim("geeig", "Platz"), size=34),
    z("erforderlich: kein milderes Mittel", 110, 260, "erf", "Bold", 34),
    z("Suche nur, wenn die Fahrerin ohne Schwierigkeiten", 150, 315, beim("erf", "Herr"), size=32),
    z("und ohne Verzögerung erreichbar ist", 150, 360, beim("erf", "Verzögerung"), size=32),
    zit("BVerwG, Urt. v. 9.4.2014 – 3 C 5.13, Rn. 16", 150, 408, beim("erf", "erreichen")),
    z("Risiko der Erreichbarkeit: wer falsch parkt", 150, 460, "risiko", size=32),
    zit("BVerwG, 3 C 5.13, Rn. 17", 150, 508, beim("risiko", "parkt")),
    z("keine feste Wartezeit; warten, wenn konkret", 150, 560, "warten", size=32),
    z("erkennbar ist, dass der Fahrer gleich zurückkommt", 150, 605, beim("warten", "erkennbar"), size=32),
    zit("BVerwG, 3 C 5.13 (Leitsatz); VG Düsseldorf, 14 K 6945/16, Rn. 26", 150, 653, beim("warten", "zurückkommt")),
    z("hier: niemand zu sehen, kein Hinweis im Auto", 195, 715, "hier", size=34),
    ok(150, 738, beim("hier", "Hinweis"), gr=20),
    blk(110, 780, 1040, 72, GRUEN, beim("hier", "Hinweis"), [("erforderlich", "ExtraBold", 36, INK)]),
    ficon("tabler", "clock", IX, IU, 130, "vhm", fuell=WEISS, bis="hier"),
    ficon("tabler", "car-crane", IX, IU, 240, "hier", fuell=GELB),
    *fig("ME", FX, FB, FR, [("vhm", "ruhig"), ("erf", "denkt"), ("hier", "ernst")]),
    schild("Herr Meier", FX, "vhm", ME_F),
]))

# M Angemessenheit und Gegenfälle -------------------------------------------------------------------------------------------
folie([("angem", f"{VHM}: angemessen"), ("gegen", f"{VHM} › Gegenfälle")], rechts_frei([
    *tafel("angem", "Angemessen?", fill=ZARTGRUEN),
    z("Parkplatz erfüllt seinen Zweck nur, wenn er jederzeit frei ist", 110, 180, "funktion", size=32),
    z("die Berechtigten sollen sich darauf verlassen können", 150, 230, beim("funktion", "Berechtigten"), size=32),
    zit("OVG NRW, Beschl. v. 21.3.2000 – 5 A 2339/99, Rn. 6, 12", 150, 278, beim("funktion", "verlassen")),
    blk(110, 330, 1040, 76, GRUEN, "konkret", [("abschleppen auch ohne konkrete Behinderung", "ExtraBold", 34, INK)]),
    zit("OVG NRW, 5 A 2339/99, Rn. 4", 150, 420, beim("konkret", "gehindert")),
    z("Gegenfälle:", 110, 485, "gegen", "Bold", 36),
    z("Auto steht nur verbotswidrig, behindert niemanden,", 150, 540, beim("gegen", "Auto"), size=32),
    z("etwa auf dem Gehweg: Vorbildwirkung allein reicht nicht", 150, 585, beim("gegen", "Gehweg"), size=32),
    zit("BVerwG, Urt. v. 9.4.2014 – 3 C 5.13, Rn. 12", 150, 633, beim("gegen", "reicht")),
    z("Fahrerin in Sicht- oder Rufweite: Ansprechen ist milder", 150, 690, "sicht2", size=32),
    zit("vgl. VG Düsseldorf, 14 K 6945/16, Rn. 24; BVerwG, 3 C 5.13, Rn. 16", 150, 738, beim("sicht2", "Mittel")),
    ficon(HC, "wheelchair-symbol", IX, IU, 130, "funktion", fuell=WEISS, bis="gegen"),
    ficon("tabler", "car", IX, IU, 230, "gegen", fuell=PINK),
    *fig("KA", FX, FB, FR, [("angem", "denkt"), ("konkret", "muede")]),
    schild("Frau Kaiser", FX, "angem", KA_F),
]))

# N Ergebnis und Kosten -----------------------------------------------------------------------------------------------------
folie([("erg", "3. materiell › Ergebnis: Abschleppen rechtmäßig"), ("pflicht", "4. Kostenpflicht und Höhe")], rechts_frei([
    *tafel("erg", "Ergebnis"),
    blk(110, 175, 1040, 80, GRUEN, beim("erg", "rechtmäßig"), [("Abschleppen rechtmäßig", "ExtraBold", 38, INK)]),
    z("Frau Kaiser hat die Gefahr verursacht:", 110, 290, "pflicht", "Bold", 34),
    z("Verhaltensstörerin, § 17 Abs. 1 OBG NRW, trägt die Kosten", 150, 343, beim("pflicht", "Verhaltensstörerin"), size=32),
    zit("VG Münster, 1 K 605/10, Rn. 23; § 59 Abs. 1 VwVG NRW", 150, 390, beim("pflicht", "Kosten")),
    z("Abschleppkosten: Auslagen", 150, 450, "hoehe", size=34),
    z("Gebühr: Rahmen 30 bis 180 €", 150, 503, beim("hoehe", "Gebühr"), size=34),
    blk(110, 570, 1040, 80, ROT, "zahlt", [("Frau Kaiser muss zahlen", "ExtraBold", 38, INK)]),
    z("Bußgeld: eigenes Verfahren", 110, 690, "bussgeld", size=32),
    zit("§ 49 Abs. 3 Nr. 5 StVO", 150, 738, beim("bussgeld", "Verfahren")),
    z("Zivil- und Strafrecht: nichts zu tun", 110, 790, beim("bussgeld", "Zivil"), size=32),
    ficon("tabler", "receipt-euro", IX, IU, 130, "pflicht", fuell=WEISS),
    *fig("KA", FX, FB, FR, [("erg", "muede"), ("zahlt", "sorge")]),
    schild("Frau Kaiser", FX, "erg", KA_F),
]))

# O Klausurtipp (Lexi) --------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · Drei Ebenen trennen")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Halte die drei Ebenen auseinander:", 200, 200, beim("tipp", "Halte"), "Bold", 36),
    z("Abschleppen inzident im Kostenbescheid prüfen", 200, 260, beim("tipp", "inzident"), size=34),
    z("Auto auf dem Verwahrhof:", 200, 350, "tipp2", "Bold", 34),
    z("manche Gerichte prüfen eine Sicherstellung", 200, 405, beim("tipp2", "Sicherstellung"), size=34),
    zit("heute § 24w OBG NRW, Kosten § 24z Abs. 3 OBG NRW (seit 1.7.2026)", 200, 455, beim("tipp2", "Ordnungsbehördengesetz")),
    z("oft offen, wenn beide Wege zum selben Ergebnis führen", 200, 525, "tipp3", size=32),
    zit("VG Düsseldorf, Urt. v. 28.3.2017 – 14 K 6945/16, Rn. 18–20", 200, 575, beim("tipp3", "Ergebnis")),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    pl("Lexi", FX, FB + 22, "tipp", fill=GELB, size=30, anker="m", d=0.2),
])

# P Klausurschema ---------------------------------------------------------------------------------------------------------------
SZ = 34
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel(glyphen("Klausurschema: Rechtmäßigkeit des Kostenbescheids"), 110, 90, "sch", 46),
    z("1. Ermächtigungsgrundlage: § 77 Abs. 1 VwVG NRW i. V. m. VO VwVG NRW", K1, 195, "q1", "Bold", 36, rechts=1820),
    z("2. formell: Zuständigkeit, Anhörung", K1, 270, "q2", "Bold", 36, rechts=1820),
    z("3. materiell: rechtmäßiges Abschleppen", K1, 345, "q3", "Bold", 36, rechts=1820),
    z("a) Grundverwaltungsakt: Schild, wirksam bekannt gegeben,", K2, 420, "q3a", size=SZ, rechts=1820),
    z("sofort vollziehbar (§ 80 Abs. 2 Satz 1 Nr. 2 VwGO analog)", K3, 470, beim("q3a", "sofort"), size=SZ, rechts=1820),
    z("b) Ersatzvornahme im sofortigen Vollzug, §§ 55 Abs. 2, 59 VwVG NRW", K2, 545, "q3b", size=SZ, rechts=1820),
    z("c) Verhältnismäßigkeit: geeignet, erforderlich, angemessen", K2, 620, "q3c", size=SZ, rechts=1820),
    z("4. Kostenpflicht und Höhe: Auslagen und Gebühr", K1, 705, "q4", "Bold", 36, rechts=1820),
])

# Q Merksatz (Lexi) ------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Ein Auto auf dem Behindertenparkplatz", 0)]], 750, 320, 44, "merke", {}),
    *markertext([[("darf regelmäßig ", 0), ("sofort abgeschleppt", "a"), (" werden,", 0)]], 750, 378, 44,
                beim("merke", "darf"), {"a": beim("merke", "sofort")}),
    *markertext([[("auch nach 5 Minuten.", 0)]], 750, 436, 44, beim("merke", "auch"), {}),
    *markertext([[("Die Kosten zahlt, wer falsch geparkt hat,", 0)]], 750, 560, 44, "m2", {}),
    *markertext([[("aber nur, wenn das Abschleppen ", 0), ("rechtmäßig", "c"), (" war.", 0)]], 750, 618, 44,
                beim("m2", "aber"), {"c": beim("m2", "rechtmäßig")}),
    *redet("LX_erklaert", 1680, 950, 700, "merke", lexi_bis_ende("merke")),
    pl("Lexi", 1680, 968, "merke", fill=GELB, size=30, anker="m", d=0.2),
])
