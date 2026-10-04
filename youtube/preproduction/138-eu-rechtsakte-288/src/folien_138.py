"""Folge 138 · EU-Rechtsakte Art. 288 AEUV: Verordnung, Richtlinie, Beschluss – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A Fall im Reisebüro (Herr Stegemann, Frau Kettner), B Sachverhalt, C Primär- und
Sekundärrecht, D Art. 288 AEUV im Wortlaut (Abs. 1 als Aufzählung, Abs. 2–5 als Wortlautkarte, vorgelesen), E Verordnung
(DSGVO, BDSG), F Richtlinie (Pauschalreiserichtlinie, §§ 651a ff. BGB), G Beschluss/Empfehlung/Stellungnahme,
H nicht umgesetzte Richtlinie: vertikale Wirkung (Ratti, Becker), I keine Wirkung zwischen Privaten (Faccini Dori),
J Auswege (richtlinienkonforme Auslegung, Francovich, Dillenkofer), K Ergebnis (zurück im Reisebüro), L Klausurtipp (Lexi),
M Klausurschema als Tabelle, N Merksatz (Lexi).
Geräusche nur bei sichtbarer Handlung: Klopfen (Tür, Frau Kettner kommt), Ordner auf dem Tisch; Freesound CC0.
Hilfsfunktionen (z, pl, tafel, fb, redet mit hörbarem Wortende …) wie in Folge 127, Kopie im eigenen Ordner; neu:
wl_links() für linksbündige Wortlautkarten mit Textmarker."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
from engine import El, F

bausteine.FIGORDNER = "op_138/"
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


def fb(x, y, w, h, fill, cue, zeilen, rund=18, anim="rise", d=0.0, bis=None):
    """Wie fl_block, Zeilenabstand passend zur Schriftgröße der Zeilen."""
    from engine import block
    for zz in zeilen:
        glyphen(zz[0])
    lh = int(max(zz[2] for zz in zeilen) * 1.3)
    assert len(zeilen) * lh * 1.15 <= h - 16, f"Block zu niedrig: {zeilen}"
    return block(x, y, w, h, fill, None, cue, textsize=lh, rund=rund, rand=INK, randbreite=5, anim=anim, d=d, bis=bis,
                 zeilen=zeilen)


def wl_links(zeilen, x, y, size, cue, hl, rechts=1170, lh=1.28, marker=GELB):
    """Linksbündiger Wortlaut (wörtliches Zitat, Abruf Cellar 04.10.2026) mit Textmarker zum gesprochenen Wort.
    zeilen = [[(text, Schlüssel|0), …], …]; hl = {Schlüssel: Cue}. Gibt (Elemente, y_ende) zurück."""
    fr, fbold = F("Regular", size), F("ExtraBold", size)
    breite = 0
    for toks in zeilen:
        glyphen("".join(t for t, _ in toks))
        breite = max(breite, sum((fbold if h else fr).getlength(t) for t, h in toks))
    assert x + breite <= rechts, f"Wortlaut zu breit ({x + breite:.0f} > {rechts}): {zeilen}"
    hgt = int(len(zeilen) * size * lh + size * 0.5)
    im = Image.new("RGBA", (int(breite) + 20, hgt)); dr = ImageDraw.Draw(im); ov = {}
    yy = 0
    for toks in zeilen:
        xx = 4
        for t, h in toks:
            f = fbold if h else fr
            tw = f.getlength(t)
            if h:
                if h not in ov:
                    ov[h] = Image.new("RGBA", im.size)
                od = ImageDraw.Draw(ov[h])
                od.rounded_rectangle((xx - 5, yy + size * 0.45, xx + tw + 5, yy + size * 1.12), 8, fill=marker)
                od.text((xx, yy), t, font=f, fill=INK)
            dr.text((xx, yy), t, font=f, fill=INK)
            xx += tw
        yy += size * lh
    els = [El(im, x - 4, y, cue, "fade", 0.0, name="wortlaut")]
    for k_, oim in ov.items():
        els.append(El(oim, x - 4, y, hl[k_], "fade", 0.0, name="marker:" + str(k_)))
    return els, y + len(zeilen) * size * lh


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


# --- Eigene Hilfsfunktion (wie Folge 127): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ----------------
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
XE = 1600                               # eine Figur
IX = 1580                               # Requisiten rechts (Folien ohne Figuren)
FARBE = {"ST": BLAU, "KE": ROT}
NAME = {"ST": "Herr Stegemann", "KE": "Frau Kettner"}


def kette(prefix, x, folge, bis_=None, d=0.0, hoehe=FR, unten=BR):
    """Eine Figur mit Mimikfolge [(Name, Cue), …] im Zwiebelschalenprinzip (erster Auftritt pop, danach harte Schnitte)."""
    els = []
    for i, (n, c) in enumerate(folge):
        b = folge[i + 1][1] if i + 1 < len(folge) else bis_
        els.append(peep_voll(prefix + n, x, unten, hoehe, c, anim=("pop" if i == 0 else "cut"), d=(d if i == 0 else 0.0), bis=b))
    return els


def paar(cue, f1, f2):
    """Herr Stegemann (links) und Frau Kettner (rechts) neben der Tafel, beide blicken zur Tafel; Namensschilder ab Beginn."""
    els = kette("ST_", X1, [(f1[0][0], cue)] + list(f1[1:])) + kette("KE_", X2, [(f2[0][0], cue)] + list(f2[1:]), d=0.2)
    return els + [namensschild(NAME["ST"], X1, BR, cue, FARBE["ST"], d=0.2),
                  namensschild(NAME["KE"], X2, BR, cue, FARBE["KE"], d=0.3)]


def einzeln(p, cue, folge):
    """Eine Figur rechts neben der Tafel (blickt zur Tafel) mit Namensschild."""
    return kette(p + "_", XE, [(folge[0][0], cue)] + list(folge[1:])) + [namensschild(NAME[p], XE, BR, cue, FARBE[p], d=0.2)]


def stufen(folge, x, unten, hoehe, rede=None, erst="pop", ende=None):
    """Figur in der Fallszene: folge = [(Bildname, Cue), …]; rede = {Bildname: 1} für Figurenrede."""
    els = []
    for i, (n, c) in enumerate(folge):
        b = folge[i + 1][1] if i + 1 < len(folge) else ende
        if rede and n in rede:
            els += redet(n, x, unten, hoehe, c, b)
        else:
            els.append(peep_voll(n, x, unten, hoehe, c, anim=(erst if i == 0 else "cut"), bis=b))
    return els


def wechsel(texte, cx, y, size=28, fill=WEISS, anker="m"):
    """Pillen nacheinander an derselben Stelle: texte = [(Text, Cue, Füllung|None), …]."""
    els = []
    for i, (t, c, f) in enumerate(texte):
        b = texte[i + 1][1] if i + 1 < len(texte) else None
        els.append(pl(t, cx, y, c, fill=f or fill, size=size, anker=anker, anim=("pop" if i == 0 else "cut"), bis=b))
    return els


def icons(folge, cx, unten, breite):
    """Requisiten nacheinander an derselben Stelle: folge = [(set, name, Cue, Füllung), …]."""
    els = []
    for i, (s, n, c, f) in enumerate(folge):
        b = folge[i + 1][2] if i + 1 < len(folge) else None
        els.append(ficon(s, n, cx, unten, breite, c, fuell=f, anim=("pop" if i == 0 else "cut"), bis=b))
    return els


# A Fall: im Reisebüro ----------------------------------------------------------------------------------------------------
BODEN, GH = 900, 520
STX, KEX = 400, 1560
STa = ("ST_redet_r", STX, BODEN, GH)
STb = ("ST_redetfroh_r", STX, BODEN, GH)
KEa = ("KE_redet", KEX, BODEN, GH)


def buero(cue):
    """Bodenlinie, Schreibtisch (Grundformen), Bildschirm, Globus, Koffer, Reiseplakat (Flugzeug) an der Wand."""
    return [linienzug([(60, BODEN), (1860, BODEN)], cue, breite=7, farbe=INK),
            karte(720, 742, 460, 34, cue, fill=HOLZ, rund=10, schatten=0, rand=5),
            karte(746, 776, 40, BODEN - 776, cue, fill=HOLZD, rund=6, schatten=0, rand=5),
            karte(1114, 776, 40, BODEN - 776, cue, fill=HOLZD, rund=6, schatten=0, rand=5),
            ficon("tabler", "device-desktop", 830, 744, 130, cue, fuell=BLAUHELL),
            ficon("tabler", "world", 980, 744, 70, cue, fuell=BLAU),
            ficon("tabler", "luggage", 640, BODEN, 90, cue, fuell=ROT),
            karte(820, 470, 220, 150, cue, fill=WEISS, rund=12, schatten=6, rand=5),
            ficon("tabler", "plane", 930, 600, 100, cue, fuell=BLAUHELL)]


folie([("fall", "Fall · Herr Stegemann und sein Reisebüro"), ("kett", "Fall · Frau Kettner, die Datenschutzbeauftragte"),
       ("frage", "Fall · Beides kommt aus der EU"), ("warum", "Fall · Die Frage")], [
    *buero("fall"),
    pl("kleines Reisebüro", 70, 40, "fall", fill=GELB, size=34, bis="kett"),
    pl("Pauschalreisen", 930, 400, beim("fall", "Pauschalreisen"), fill=WEISS, size=28, anker="m", bis="k1"),
    *stufen([("ST_ruhig_r", "fall"), ("ST_froh_r", beim("fall", "Pauschalreisen")), ("ST_ruhig_r", "kett"),
             ("ST_denkt_r", "k1"), ("ST_redet_r", "s1"), ("ST_denkt_r", "frage"), ("ST_staunt_r", "prl"),
             ("ST_still_r", "warum")], STX, BODEN, GH, rede={"ST_redet_r": 1}, erst="cut"),
    namensschild(NAME["ST"], STX, BODEN, "fall", FARBE["ST"]),
    # Frau Kettner kommt (Tür, Klopfen) und legt einen Ordner ab
    szene(ficon("tabler", "door", 1810, BODEN, 100, "kett", fuell=HOLZ), "138tuer*", 1.0, versatz=0.05),
    *stufen([("KE_ruhig", "kett"), ("KE_redet", "k1"), ("KE_ruhig", "s1"), ("KE_froh", "frage"),
             ("KE_denkt", "warum")], KEX, BODEN, GH, rede={"KE_redet": 1}),
    namensschild(NAME["KE"], KEX, BODEN, "kett", FARBE["KE"], d=0.2),
    pl("Datenschutzbeauftragte", KEX, 300, beim("kett", "Datenschutzbeauftragte"), fill=ROTHELL, size=28, anker="m", bis="k1"),
    szene(ficon("tabler", "folder", 1090, 744, 80, "ordner", fuell=ROT), "138ordner*", 1.0, versatz=0.05),
    # Figurenrede
    blase("sprech", 900, 240, "k1", 1000, 215, inhalt=["Für Ihre Kundendaten gilt die", "Datenschutz-Grundverordnung. Sie gilt hier",
          "unmittelbar, wie in jedem Mitgliedstaat."], textsize=30, figur=KEa, bis="s1"),
    blase("sprech", 860, 240, "s1", 860, 215, inhalt=["Und warum steht mein Pauschalreiserecht", "dann im BGB und nicht",
          "in der EU-Richtlinie?"], textsize=30, figur=STa, bis="frage"),
    # Die Frage
    pl("Beides kommt aus der EU", 980, 150, "frage", fill=WEISS, size=30, anker="m"),
    ficon("tabler", "shield-lock", 700, 330, 80, "dsg", fuell=GRUEN),
    pl("DSGVO: ab 25.5.2018 unmittelbar in allen Mitgliedstaaten", 980, 230, beim("dsg", "galt"), fill=GRUENHELL, size=28,
       anker="m"),
    ficon("tabler", "book", 1260, 330, 80, "prl", fuell=GELB),
    pl("Pauschalreiserichtlinie: erst ein deutsches Gesetz", 980, 300, beim("prl", "brauchte"), fill=HELL, size=28, anker="m"),
    pl("Warum?", 980, 380, "warum", fill=PINK, size=40, anker="m"),
])

# B Sachverhalt -------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    glyphen("Herr Stegemann führt ein kleines Reisebüro und stellt dort auch Pauschalreisen zusammen. Frau Kettner, seine "
            "Datenschutzbeauftragte, erklärt ihm: Für seine Kundendaten gilt die Datenschutz-Grundverordnung unmittelbar, "
            "wie in jedem Mitgliedstaat."),
    glyphen("Herr Stegemann wundert sich: Sein Pauschalreiserecht steht im BGB und nicht in der EU-Richtlinie."),
    glyphen("Die Datenschutz-Grundverordnung galt ab dem 25.5.2018 unmittelbar in allen Mitgliedstaaten. Die "
            "Pauschalreiserichtlinie brauchte dagegen erst ein deutsches Gesetz."),
], "Warum gilt die eine unmittelbar – und die andere erst über ein deutsches Gesetz?")

# C 1. Primär- und Sekundärrecht ------------------------------------------------------------------------------------------
PE = "1. Primär- und Sekundärrecht"
folie([("ebene", PE), ("prim", f"{PE} › Primärrecht: die Verträge"), ("sek", f"{PE} › Sekundärrecht: Rechtsakte der Organe"),
       ("formen", f"{PE} › Formen: Art. 288 AEUV")], rechts_frei([
    *tafel("ebene", "Primär- und Sekundärrecht"),
    z("Zuerst die Ebenen:", 110, 180, "ebene", "Bold", 34),
    karte(110, 245, 1040, 200, "prim", fill=HELL, rund=18, schatten=6, rand=4),
    z("Primärrecht: vor allem die Verträge selbst", 140, 265, "prim", "Bold", 32, rechts=1140),
    z("EU-Vertrag (EUV) und", 140, 315, beim("prim", "EU-Vertrag"), size=32, rechts=1140),
    z("Vertrag über die Arbeitsweise der Union (AEUV)", 140, 360, beim("prim", "Arbeitsweise"), size=32, rechts=1140),
    fund("Art. 1 Abs. 3 EUV; Art. 1 Abs. 2 AEUV", 110, 455, beim("prim", "Arbeitsweise")),
    linienzug([(630, 500), (630, 545)], "sek", breite=8, farbe=INK),
    linienzug([(608, 525), (630, 550), (652, 525)], "sek", breite=8, farbe=INK),
    karte(110, 560, 1040, 150, "sek", fill=BLAUHELL, rund=18, schatten=6, rand=4),
    z("Sekundärrecht: erlassen die Organe der Union", 140, 580, "sek", "Bold", 32, rechts=1140),
    z("auf Grundlage der Verträge", 140, 630, beim("sek", "Grundlage"), size=32, rechts=1140),
    fb(110, 755, 1040, 90, GRUEN, "formen", [("Welche Formen? Art. 288 AEUV", "ExtraBold", 34, INK)]),
    *paar("ebene", [("ruhig",), ("denkt", "sek"), ("froh", "formen")], [("ruhig",), ("ernst", "prim"), ("froh", "formen")]),
]))

# D 2. Art. 288 AEUV im Wortlaut (Cellar CELEX 12016E288, ABl. C 202 vom 7.6.2016, S. 171) --------------------------------
PA = "2. Art. 288 AEUV"
W2 = [[("(2) „Die Verordnung hat ", 0), ("allgemeine Geltung", "a"), (". Sie ist ", 0), ("in allen", "b")],
      [("ihren Teilen verbindlich", "b"), (" und gilt ", 0), ("unmittelbar in jedem", "c")],
      [("Mitgliedstaat", "c"), (".“", 0)]]
W3 = [[("(3) „Die Richtlinie ist für jeden Mitgliedstaat, an den sie", 0)],
      [("gerichtet wird, ", 0), ("hinsichtlich des zu erreichenden Ziels", "a")],
      [("verbindlich", "a"), (", überlässt jedoch den innerstaatlichen", 0)],
      [("Stellen die ", 0), ("Wahl der Form und der Mittel", "b"), (".“", 0)]]
W4 = [[("(4) „Beschlüsse sind ", 0), ("in allen ihren Teilen verbindlich", "a"), (". Sind", 0)],
      [("sie an bestimmte Adressaten gerichtet, so sind sie ", 0), ("nur", "b")],
      [("für diese verbindlich", "b"), (".“", 0)]]
W5 = [[("(5) „Die Empfehlungen und Stellungnahmen sind ", 0), ("nicht", "a")],
      [("verbindlich", "a"), (".“", 0)]]
_x = 110
_abs1 = []
for _t, _c, _f in (("Verordnungen", "h1", BLAU), ("Richtlinien", "h2", GRUEN), ("Beschlüsse", "h3", GELB),
                   ("Empfehlungen", "h4", WEISS), ("Stellungnahmen", "h5", WEISS)):
    _p = pl(_t, _x, 225, _c, fill=_f, size=26, pad=(16, 10))
    _abs1.append(_p); _x += _p.sprite.width + 6
assert _x <= 1180, f"Abs.-1-Pillen zu breit: {_x}"
_wl = []
_y = 315
for _w, _c, _hl in ((W2, "abs2", {"a": beim("abs2", "allgemeine"), "b": beim("abs2", "allen"), "c": beim("abs2", "unmittelbar")}),
                    (W3, "abs3", {"a": beim("abs3", "hinsichtlich"), "b": beim("abs3", "Wahl")}),
                    (W4, "abs4", {"a": beim("abs4", "allen"), "b": beim("abs4", "nur")}),
                    (W5, "abs5", {"a": beim("abs5", "nicht")})):
    _e, _y = wl_links(_w, 140, _y, 30, _c, _hl)
    _wl += _e; _y += 12
assert _y <= 850, f"Wortlautkarte zu hoch: {_y}"
folie([("abs1", f"{PA} › Abs. 1: fünf Handlungsformen"), ("abs2", f"{PA} › Abs. 2: Verordnung"),
       ("abs3", f"{PA} › Abs. 3: Richtlinie"), ("abs4", f"{PA} › Abs. 4: Beschluss"),
       ("abs5", f"{PA} › Abs. 5: Empfehlung, Stellungnahme")], rechts_frei([
    *tafel("abs1", "Art. 288 AEUV im Wortlaut"),
    z("Abs. 1: fünf Handlungsformen", 110, 170, "abs1", "Bold", 32),
    *_abs1,
    karte(110, 300, 1040, int(_y - 300 + 10), "abs2", fill=(246, 246, 250, 255), rund=18, schatten=6, rand=4),
    *_wl,
    fund("Art. 288 Abs. 2–5 AEUV, ABl. C 202 vom 7.6.2016, S. 171", 110, int(_y + 22), "abs2"),
    *wechsel([("Art. 288 AEUV", "abs1", GELB), ("Verordnung", "abs2", BLAU), ("Richtlinie", "abs3", GRUEN),
              ("Beschluss", "abs4", GELB), ("Empfehlung, Stellungnahme", "abs5", WEISS)], IX, 200, size=30),
    *icons([("tabler", "books", "abs1", GELB), ("tabler", "file-certificate", "abs2", BLAU), ("tabler", "target", "abs3", GRUEN),
            ("tabler", "mail", "abs4", GELB), ("tabler", "message-circle", "abs5", WEISS)], IX, 560, 170),
]))

# E Verordnung -----------------------------------------------------------------------------------------------------------
W99 = [[("„Sie gilt ab dem 25. Mai 2018.", 0)],
       [("Diese Verordnung ist ", 0), ("in allen ihren Teilen verbindlich", "a")],
       [("und ", 0), ("gilt unmittelbar in jedem Mitgliedstaat", "b"), (".“", 0)]]
_w99, _y99 = wl_links(W99, 140, 395, 30, beim("vo2", "Genau"), {"a": beim("vo2", "allen"), "b": beim("vo2", "unmittelbar")})
folie([("vo", f"{PA} › Verordnung: allgemein, vollständig, unmittelbar"), ("vo2", f"{PA} › Verordnung: Beispiel DSGVO"),
       ("bdsg", f"{PA} › Verordnung: das BDSG ergänzt nur")], rechts_frei([
    *tafel("vo", "Die Verordnung"),
    z("wie ein Gesetz in allen Mitgliedstaaten zugleich", 110, 180, beim("vo", "wie"), "Bold", 34),
    ok(135, 262, beim("vo", "allgemein"), gr=18), z("allgemein", 170, 242, beim("vo", "allgemein"), size=32),
    ok(385, 262, beim("vo", "vollständig"), gr=18), z("vollständig", 420, 242, beim("vo", "vollständig"), size=32),
    ok(665, 262, beim("vo", "unmittelbar"), gr=18), z("unmittelbar", 700, 242, beim("vo", "unmittelbar"), size=32),
    z("Datenschutz-Grundverordnung (EU) 2016/679", 110, 330, "vo2", "Bold", 32),
    karte(110, 385, 1040, int(_y99 - 385 + 14), beim("vo2", "Genau"), fill=(246, 246, 250, 255), rund=18, schatten=6, rand=4),
    *_w99,
    fund("Art. 99 Abs. 2 DSGVO, ABl. L 119 vom 4.5.2016, S. 1", 110, int(_y99 + 26), beim("vo2", "Genau")),
    karte(110, 610, 1040, 230, "bdsg", fill=LILAHELL, rund=18, schatten=6, rand=4),
    z("Bundesdatenschutzgesetz: setzt sie nicht um", 140, 630, "bdsg", "Bold", 32, rechts=1140),
    z("ergänzt sie nur, wo sie Spielraum lässt,", 140, 680, beim("bdsg", "ergänzt"), size=32, rechts=1140),
    z("tritt zurück, soweit sie unmittelbar gilt", 140, 725, beim("bdsg", "tritt"), size=32, rechts=1140),
    fund("§ 1 Abs. 5 BDSG; Erwägungsgrund 10 DSGVO", 140, 780, beim("bdsg", "tritt"), rechts=1140),
    pl("DSGVO", XE, 230, "vo2", fill=GRUEN, size=30, anker="m"),
    *einzeln("KE", "vo", [("ruhig",), ("froh", "vo2"), ("ernst", "bdsg")]),
]))

# F Richtlinie -----------------------------------------------------------------------------------------------------------
folie([("rl", f"{PA} › Richtlinie: verbindlich nur das Ziel"), ("form", f"{PA} › Richtlinie: Wahl der Form und der Mittel"),
       ("frist", f"{PA} › Richtlinie: Umsetzungsfrist"), ("bgb", f"{PA} › Richtlinie: Umsetzung im BGB")], rechts_frei([
    *tafel("rl", "Die Richtlinie"),
    z("richtet sich an die Mitgliedstaaten", 110, 180, "rl", "Bold", 34),
    z("verbindlich: nur das Ziel", 110, 235, beim("rl", "Verbindlich"), size=32),
    z("Form und Mittel wählen die Mitgliedstaaten,", 110, 300, "form", "Bold", 32),
    z("etwa durch ein Gesetz", 110, 347, beim("form", "etwa"), size=32),
    z("dafür: eine Umsetzungsfrist", 110, 415, "frist", "Bold", 34),
    karte(110, 480, 1040, 180, "prl2", fill=HELL, rund=18, schatten=6, rand=4),
    z("Pauschalreiserichtlinie (EU) 2015/2302:", 140, 495, "prl2", "Bold", 32, rechts=1140),
    z("Vorschriften erlassen bis 1.1.2018", 140, 545, beim("prl2", "Vorschriften"), size=32, rechts=1140),
    z("anwenden ab 1.7.2018", 140, 592, beim("prl2", "anwenden"), size=32, rechts=1140),
    fund("Art. 28 Abs. 1, 2 RL (EU) 2015/2302", 110, 668, beim("prl2", "anwenden")),
    fb(110, 720, 1040, 90, GRUEN, "bgb", [("Deutschland: Umsetzung im BGB, §§ 651a ff.", "ExtraBold", 32, INK)]),
    fund("BT-Drs. 18/10822, S. 1 f.; Art. 229 § 42 EGBGB", 110, 820, beim("bgb", "Paragrafen")),
    ficon("tabler", "luggage", XE, 420, 120, "prl2", fuell=ROT),
    *einzeln("ST", "rl", [("denkt",), ("ruhig", "form"), ("staunt", "prl2"), ("froh", "bgb")]),
]))

# G Beschluss, Empfehlung, Stellungnahme -------------------------------------------------------------------------------------
folie([("be", f"{PA} › Beschluss: bindet seine Adressaten"), ("beih", f"{PA} › Beschluss: Beispiel Beihilfe"),
       ("empf", f"{PA} › Empfehlung, Stellungnahme: nicht verbindlich")], rechts_frei([
    *tafel("be", "Beschluss, Empfehlung, Stellungnahme"),
    z("Beschluss: in allen Teilen verbindlich", 110, 180, "be", "Bold", 34),
    z("an bestimmte Adressaten gerichtet: bindet nur diese", 110, 235, beim("be", "Richtet"), size=32),
    karte(110, 310, 1040, 230, "beih", fill=HELL, rund=18, schatten=6, rand=4),
    z("Beispiel: Die Kommission beschließt,", 140, 330, "beih", "Bold", 32, rechts=1140),
    z("ein Staat muss eine unvereinbare Beihilfe", 140, 377, beim("beih", "Staat"), size=32, rechts=1140),
    z("aufheben oder umgestalten", 140, 424, beim("beih", "aufheben"), size=32, rechts=1140),
    ok(165, 495, beim("beih", "Gebunden"), gr=18),
    z("gebunden: dieser Staat", 200, 475, beim("beih", "Gebunden"), "Bold", 32, rechts=1140),
    fund("Art. 108 Abs. 2 UAbs. 1 AEUV", 110, 550, beim("beih", "Gebunden")),
    nein(135, 660, "empf", gr=18),
    fb(170, 615, 980, 90, ROTHELL, "empf", [("Empfehlungen, Stellungnahmen: binden niemanden", "ExtraBold", 31, INK)]),
    fund("Art. 288 Abs. 5 AEUV", 170, 715, "empf"),
    *wechsel([("Beschluss", "be", GELB), ("Beihilfe aufheben", "beih", HELL), ("bindet niemanden", "empf", ROTHELL)], IX, 200, size=30),
    *icons([("tabler", "mail", "be", GELB), ("tabler", "building-bank", "beih", BLAU), ("tabler", "message-circle", "empf", WEISS)],
           IX, 560, 170),
]))

# H 3. Nicht umgesetzte Richtlinie: vertikale Wirkung -------------------------------------------------------------------------
PN = "3. Nicht umgesetzte Richtlinie"
folie([("prob", f"{PN} › Frist abgelaufen"), ("ratti", f"{PN} › kein Berufen auf das eigene Versäumnis"),
       ("genau", f"{PN} › unbedingt und hinreichend genau"), ("vert", f"{PN} › vertikale unmittelbare Wirkung")], rechts_frei([
    *tafel("prob", "Richtlinie nicht rechtzeitig umgesetzt?"),
    z("Staat kann dem Einzelnen nach Fristablauf", 110, 180, "ratti", "Bold", 32),
    z("sein eigenes Versäumnis nicht entgegenhalten", 110, 227, beim("ratti", "sein"), "Bold", 32),
    fund("EuGH, Rs. 148/78 (Ratti), Slg. 1979, 1629, Rn. 22 f., 43", 110, 280, beim("ratti", "Ratti")),
    fund("EuGH, Rs. 8/81 (Becker), Slg. 1982, 53, Rn. 24 f.", 110, 315, beim("ratti", "Becker")),
    ok(135, 405, beim("genau", "unbedingt"), gr=18), z("unbedingt", 170, 385, beim("genau", "unbedingt"), size=32),
    ok(365, 405, beim("genau", "hinreichend"), gr=18), z("hinreichend genau", 400, 385, beim("genau", "hinreichend"), size=32),
    z("dann: Der Einzelne kann sich gegenüber dem", 110, 450, beim("genau", "kann"), size=32),
    z("Staat unmittelbar auf sie berufen", 110, 497, beim("genau", "Staat"), size=32),
    fund("Becker, Rn. 25", 110, 545, beim("genau", "Staat")),
    fb(110, 620, 1040, 90, GRUEN, "vert", [("vertikale unmittelbare Wirkung", "ExtraBold", 34, INK)]),
    ficon("tabler", "building-bank", IX, 360, 150, beim("genau", "Staat"), fuell=BLAU),
    pl("Staat", IX, 375, beim("genau", "Staat"), fill=BLAU, size=28, anker="m"),
    ficon("tabler", "user", IX, 800, 130, beim("genau", "Einzelne"), fuell=GELB),
    pl("Einzelner", IX, 815, beim("genau", "Einzelne"), fill=GELB, size=28, anker="m"),
    linienzug([(IX, 640), (IX, 450)], "vert", breite=8, farbe=DGRUEN),
    linienzug([(IX - 22, 475), (IX, 448), (IX + 22, 475)], "vert", breite=8, farbe=DGRUEN),
    pl("vertikal", IX + 140, 520, "vert", fill=GRUEN, size=28, anker="m"),
    pl("Frist abgelaufen?", IX, 200, "prob", fill=HELL, size=30, anker="m", bis=beim("genau", "Staat")),
]))

# I Keine Wirkung zwischen Privaten: Faccini Dori -------------------------------------------------------------------------
folie([("horiz", f"{PN} › keine Wirkung zwischen Privaten"), ("fd", f"{PN} › Faccini Dori, EuGH 1994"),
       ("fd3", f"{PN} › kein Widerruf aus der Richtlinie gegen Private")], rechts_frei([
    *tafel("horiz", "Und zwischen Privaten?"),
    nein(135, 200, beim("horiz", "nicht"), gr=18),
    z("keine unmittelbare Wirkung zwischen Privaten", 170, 180, beim("horiz", "nicht"), "Bold", 32),
    karte(110, 255, 1040, 250, "fd", fill=HELL, rund=18, schatten=6, rand=4),
    z("Faccini Dori, EuGH 1994: Verbraucherin widerruft", 140, 275, "fd", "Bold", 31, rechts=1140),
    z("Vertrag über einen Englisch-Fernkurs,", 140, 322, beim("fd", "Vertrag"), size=31, rechts=1140),
    z("abgeschlossen im Mailänder Hauptbahnhof", 140, 367, beim("fd", "Mailänder"), size=31, rechts=1140),
    z("Italien: Richtlinie nicht umgesetzt", 140, 420, beim("fd", "Italien"), "Bold", 31, rechts=1140),
    fund("Rs. C-91/92, Slg. 1994, I-3325, Rn. 3 f., 8", 110, 515, beim("fd", "Italien")),
    z("Richtlinie kann nicht selbst Pflichten", 110, 570, "fd2", "Bold", 32),
    z("für einen Bürger begründen", 110, 617, beim("fd2", "für"), "Bold", 32),
    fund("Rn. 20, 24", 110, 665, beim("fd2", "begründen")),
    nein(135, 745, "fd3", gr=18),
    z("Widerruf gegenüber dem Unternehmen nicht", 170, 720, "fd3", size=32),
    z("auf die Richtlinie zu stützen", 170, 767, beim("fd3", "Widerrufsrecht"), size=32),
    fund("Rn. 25", 170, 815, beim("fd3", "Richtlinie")),
    pl("zwischen Privaten", IX, 200, "horiz", fill=WEISS, size=30, anker="m"),
    ficon("tabler", "language", IX, 420, 110, beim("fd", "Englisch"), fuell=BLAUHELL),
    ficon("tabler", "user", 1410, 640, 120, beim("fd", "Verbraucherin"), fuell=GELB),
    pl("Verbraucherin", 1410, 655, beim("fd", "Verbraucherin"), fill=GELB, size=28, anker="m"),
    ficon("tabler", "building-store", 1750, 640, 130, beim("fd", "Vertrag"), fuell=HELL),
    pl("Unternehmen", 1750, 655, beim("fd", "Vertrag"), fill=HELL, size=28, anker="m"),
    linienzug([(1490, 580), (1670, 580)], beim("fd", "Vertrag"), breite=8, farbe=INK),
    nein(1580, 580, "fd3", gr=24),
]))

# J Zwei Auswege ------------------------------------------------------------------------------------------------------------
folie([("ausw", f"{PN} › zwei Auswege"), ("rka", f"{PN} › Ausweg 1: richtlinienkonforme Auslegung"),
       ("fran", f"{PN} › Ausweg 2: Staatshaftung nach Francovich"), ("dill", f"{PN} › Staatshaftung: Dillenkofer, EuGH 1996")],
      rechts_frei([
    *tafel("ausw", "Zwei Auswege"),
    z("1. richtlinienkonforme Auslegung:", 110, 170, "rka", "Bold", 32),
    z("nationales Recht so weit wie möglich nach", 150, 215, beim("rka", "Gerichte"), size=31),
    z("Wortlaut und Zweck der Richtlinie auslegen", 150, 258, beim("rka", "Wortlaut"), size=31),
    fund("Faccini Dori, Rn. 26", 150, 302, beim("rka", "Zweck")),
    z("2. Staatshaftung nach Francovich:", 110, 350, "fran", "Bold", 32),
    ok(175, 418, beim("fran", "Rechte"), gr=16), z("Richtlinie soll Rechte verleihen", 205, 398, beim("fran", "Rechte"), size=31),
    ok(175, 463, beim("fran", "Inhalt"), gr=16), z("Inhalt bestimmbar", 205, 443, beim("fran", "Inhalt"), size=31),
    ok(175, 508, beim("fran", "Verstoß"), gr=16), z("Verstoß verursacht den Schaden", 205, 488, beim("fran", "Verstoß"), size=31),
    fund("EuGH, verb. Rs. C-6/90 und C-9/90, Slg. 1991, I-5357, Rn. 39 f.", 150, 535, beim("fran", "Verstoß")),
    karte(110, 590, 1040, 245, "dill", fill=BLAUHELL, rund=18, schatten=6, rand=4),
    z("Dillenkofer, EuGH 1996: alte Pauschalreiserichtlinie;", 140, 605, "dill", "Bold", 30, rechts=1140),
    z("Reisende nach der Pleite ohne ihr Geld,", 140, 648, beim("dill", "Reisende"), size=30, rechts=1140),
    z("Insolvenzschutz zu spät umgesetzt", 140, 691, beim("dill", "Insolvenzschutz"), size=30, rechts=1140),
    z("in der Frist gar nicht umgesetzt: qualifizierter Verstoß", 140, 742, "qual", "Bold", 30, rechts=1140),
    fund("verb. Rs. C-178/94 u. a., Slg. 1996, I-4845, Rn. 10 f., 29", 140, 790, beim("qual", "qualifiziert"), rechts=1140),
    *wechsel([("Auslegung", "rka", GRUEN), ("Schadensersatz vom Staat", "fran", BLAU), ("Pleite der Veranstalter", "dill", ROTHELL)],
             XE, 200, size=28),
    *icons([("tabler", "scale", "rka", GELB), ("tabler", "coins", "fran", GELB), ("tabler", "luggage-off", "dill", ROT)], XE, 420, 120),
    *einzeln("ST", "ausw", [("ruhig",), ("denkt", "fran"), ("staunt", "dill"), ("still", "qual")]),
]))

# K Ergebnis: zurück im Reisebüro (dieselbe Szene wie A, die Geschichte kehrt dorthin zurück) --------------------------------
folie([("erg", "Ergebnis · Verordnung gilt unmittelbar, Richtlinie braucht Umsetzung")], [
    *buero("erg"),
    ficon("tabler", "folder", 1090, 744, 80, "erg", fuell=ROT),
    ficon("tabler", "door", 1810, BODEN, 100, "erg", fuell=HOLZ),
    *stufen([("ST_ruhig_r", "erg"), ("ST_denkt_r", "erg2"), ("ST_froh_r", "erg3"), ("ST_redetfroh_r", "s2")], STX, BODEN, GH,
            rede={"ST_redetfroh_r": 1}, ende="tipp"),
    namensschild(NAME["ST"], STX, BODEN, "erg", FARBE["ST"], d=0.2),
    *stufen([("KE_ruhig", "erg"), ("KE_froh", "erg1"), ("KE_ruhig", "s2"), ("KE_froh", beim("s2", "Reiserecht"))], KEX, BODEN, GH),
    namensschild(NAME["KE"], KEX, BODEN, "erg", FARBE["KE"], d=0.3),
    pl("DSGVO = Verordnung: gilt unmittelbar", 980, 150, beim("erg1", "Verordnung"), fill=GRUEN, size=30, anker="m", bis="s2"),
    pl("Pauschalreiserichtlinie = Richtlinie: bindet nur im Ziel", 980, 225, beim("erg2", "Richtlinie"), fill=HELL, size=30,
       anker="m", bis="s2"),
    pl("§§ 651a ff. BGB, ausgelegt im Licht der Richtlinie", 980, 300, beim("erg3", "Paragrafen"), fill=WEISS, size=30,
       anker="m", bis="s2"),
    blase("sprech", 780, 210, "s2", 862, 215, inhalt=["Also Datenschutz direkt aus der EU,", "Reiserecht aus dem BGB."],
          textsize=32, figur=STb),
])

# L Klausurtipp (Lexi) -----------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · erst die Umsetzungsfrist"), ("tipp3", "Klausurtipp · Staat oder Privater?")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Beruft sich jemand auf eine Richtlinie? Prüfe:", 200, 200, "tipp", "Bold", 33),
    z("1. Ist die Umsetzungsfrist abgelaufen?", 200, 270, beim("tipp", "Ist"), size=34),
    z("2. unbedingt und hinreichend genau?", 200, 340, "tipp2", size=34),
    z("3. Gegner: der Staat oder ein Privater?", 200, 410, "tipp3", size=34),
    fb(200, 500, 950, 140, GELB, "tipp4", [("Gegner privat: nur richtlinienkonforme", "ExtraBold", 32, INK),
                                         ("Auslegung und Staatshaftung", "ExtraBold", 32, INK)]),
    fund("Faccini Dori, Rn. 25–27", 200, 655, "tipp4"),
    *redet("LX_warnt", LXX, BR, FR + 60, "tipp", "sch"),
    namensschild("Lexi", LXX, BR, "tipp", GELB, d=0.2),
])

# M Klausurschema als Tabelle ------------------------------------------------------------------------------------------------
PS_ = "Klausurschema"
C0, C1, C2, C3 = 110, 560, 980, 1400       # Spalten: Merkmal, Verordnung, Richtlinie, Beschluss
RY = {1: 275, 2: 375, 3: 515, 4: 655}       # Zeilen
T_ = []


def zelle(zeilen, x, r, cue, stil="Regular"):
    return [z(t, x, RY[r] + i * 42, cue, stil, 30, rechts=x + 420 if x > C0 else C1 - 10) for i, t in enumerate(zeilen)]


folie([("sch", PS_), ("z1", f"{PS_} › I. verbindlich?"), ("z2", f"{PS_} › II. für wen?"), ("z3", f"{PS_} › III. Umsetzung nötig?"),
       ("z4", f"{PS_} › IV. Beispiele")], [
    karte(60, 50, 1800, 900, "sch"),
    titel("Klausurschema: Rechtsakte nach Art. 288 AEUV", 110, 90, "sch", 48),
    z("Verordnung", C1, 195, "z1a", "ExtraBold", 32, rechts=1820), z("Richtlinie", C2, 195, "z1b", "ExtraBold", 32, rechts=1820),
    z("Beschluss", C3, 195, "z1c", "ExtraBold", 32, rechts=1820),
    linienzug([(110, 250), (1810, 250)], "z1", breite=4, farbe=INK),
    *zelle(["I. verbindlich?"], C0, 1, "z1", "Bold"),
    *zelle(["in allen Teilen"], C1, 1, "z1a"), *zelle(["nur im Ziel"], C2, 1, "z1b"), *zelle(["in allen Teilen"], C3, 1, "z1c"),
    linienzug([(110, 350), (1810, 350)], "z2", breite=3, farbe=TEXT),
    *zelle(["II. für wen?"], C0, 2, "z2", "Bold"),
    *zelle(["allgemein"], C1, 2, "z2a"), *zelle(["Mitgliedstaaten, an", "die sie gerichtet ist"], C2, 2, "z2b"),
    *zelle(["seine Adressaten"], C3, 2, "z2c"),
    linienzug([(110, 490), (1810, 490)], "z3", breite=3, farbe=TEXT),
    *zelle(["III. Umsetzung", "nötig?"], C0, 3, "z3", "Bold"),
    *zelle(["nein"], C1, 3, "z3a"), *zelle(["ja, innerhalb", "der Frist"], C2, 3, "z3b"),
    *zelle(["nein, der Adressat", "muss ihn befolgen"], C3, 3, "z3c"),
    linienzug([(110, 630), (1810, 630)], "z4", breite=3, farbe=TEXT),
    *zelle(["IV. Beispiele"], C0, 4, "z4", "Bold"),
    *zelle(["Datenschutz-", "Grundverordnung"], C1, 4, "z4a"), *zelle(["Pauschalreise-", "richtlinie"], C2, 4, "z4b"),
    *zelle(["Beihilfebeschluss", "der Kommission"], C3, 4, "z4c"),
    linienzug([(540, 180), (540, 750)], "z1", breite=3, farbe=TEXT),
    linienzug([(960, 180), (960, 750)], "z1b", breite=3, farbe=TEXT),
    linienzug([(1380, 180), (1380, 750)], "z1c", breite=3, farbe=TEXT),
    fund("Art. 288 Abs. 2–4 AEUV; DSGVO Art. 99; RL (EU) 2015/2302 Art. 28; Art. 108 Abs. 2 AEUV", 110, 790, beim("z4c", "Kommission"),
         rechts=1820),
])

# N Merksatz (Lexi) --------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Die Verordnung ", 0), ("gilt unmittelbar", "a"), (",", 0)],
                 [("die Richtlinie wirkt über das ", 0), ("Umsetzungsgesetz", "b"), (",", 0)],
                 [("der Beschluss ", 0), ("bindet seine Adressaten", "c"), (".", 0)]], 750, 300, 42, "merke",
                {"a": beim("merke", "gilt"), "b": beim("merke", "Umsetzungsgesetz"), "c": beim("merke", "bindet")}),
    *markertext([[("Auf eine nicht umgesetzte Richtlinie beruft sich", 0)],
                 [("der Bürger ", 0), ("gegen den Staat", "d"), (", ", 0), ("nicht gegen Private", "e"), (".", 0)]],
                750, 570, 40, "m2", {"d": beim("m2", "gegen"), "e": beim("m2", "nicht")}),
    *redet("LX_erklaert", 1680, 960, 690, "merke", lexi_bis_ende("merke")),
    namensschild("Lexi", 1680, 960, "merke", GELB, d=0.2),
])
