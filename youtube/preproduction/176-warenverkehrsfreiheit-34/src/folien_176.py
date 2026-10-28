"""Folge 176 · Warenverkehrsfreiheit Schema: Art. 34 AEUV mit Dassonville – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A Fall im Lager eines Getränkegroßhandels (Frau Trautmann, Herr Kleinschmidt), B Sachverhalt,
C Norm (Art. 34 AEUV, Wortlautkarte, vorgelesen) und Prüfschema mit eigener Farbe je Punkt (1 Blau, 2 Grün, 3 Lila, 4 Gelb),
D 1. Schutzbereich (Ware, Kommission/Italien 7/68), E 2. Adressat, F 3. Beschränkung und der echte Fall Dassonville, G Dassonville-
Formel (Zitatkarte Rn. 5), H Grenze Keck, I 4. Rechtfertigung: Art. 36 AEUV (Wortlautkarte), J Cassis de Dijon und
Verhältnismäßigkeit, K Dassonville Rn. 6, 7/9, L Lösung, M zurück im Lager, N Klausurtipp (Lexi), O Klausurschema, P Merksatz.
Whisky nur als neutrale Flaschen- und Kisten-Icons ohne Marke; kein Trinken, keine Bar, keine Gläser. Reale Beteiligte
(Dassonville, Keck) nur als Fallnamen; keine Personen-Icons; keine Flaggen.
Geräusche nur bei sichtbarer Handlung: Tür (Herr Kleinschmidt kommt ins Lager), Papier (Rechnungen werden vorgezeigt bzw.
geprüft); Freesound CC0, ../geraeusche_herkunft.json.
Hilfsfunktionen (glyphen, z, pl, tafel, fb, wl_links, zitatkarte, redet mit hörbarem Wortende …) als eigene Kopie aus Folge 164
(gemeinsame Dateien unverändert); neu: tafel_n() mit farbiger Schrittnummer, nr(), lager(). Zahlen auf Tafeln, Pillen und
Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
from engine import El, F

bausteine.FIGORDNER = "op_176/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
LILAHELL = (246, 243, 255, 255)
ROTHELL = (253, 232, 228, 255)
GRUENHELL = (232, 247, 233, 255)
BLAUHELL = (228, 238, 253, 255)
ZITAT = (246, 246, 250, 255)
GRAU = (214, 214, 210, 255)
GRAUD = (176, 176, 170, 255)
HOLZ = (214, 160, 110, 255)
DAUER = bausteine._cj()["dauer"]

# Sprechblasen müssen im Stil C entstehen (kein stiller Rückfall auf Stil e) – wie Folge 161
_run0 = bausteine._sp.run


def _run_c(args, **k):
    r = _run0(args, **k)
    if len(args) > 1 and str(args[1]).endswith("blase_c.js"):
        assert r.returncode == 0, f"Blase Stil C fehlgeschlagen: {args[2]}"
    return r


bausteine._sp.run = _run_c

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
    e = pille(glyphen(text), *a, **k)
    assert e.x >= 30 and e.x + e.sprite.width <= 1890, f"Pille ragt aus dem Bild: {text}"
    return e


def tafel(cue, titel_, h=840, fill=WEISS, size=46):
    """Rechtstafel links, rechts bleibt Platz für die Figuren."""
    assert 110 + F("ExtraBold", size).getlength(glyphen(titel_)) <= 1170, f"Titel zu breit: {titel_}"
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(titel_, 110, 100, cue, size)]


def fb(x, y, w, h, fill, cue, zeilen, rund=18, anim="rise", d=0.0, bis=None):
    """Block mit Zeilen; Zeilenabstand passend zur Schriftgröße, Textbreite geprüft."""
    from engine import block
    for zz in zeilen:
        glyphen(zz[0])
        assert F(zz[1], zz[2]).getlength(zz[0]) <= w - 30, f"Blockzeile zu breit: {zz[0]}"
    lh = int(max(zz[2] for zz in zeilen) * 1.3)
    assert len(zeilen) * lh * 1.15 <= h - 16, f"Block zu niedrig: {zeilen}"
    return block(x, y, w, h, fill, None, cue, textsize=lh, rund=rund, rand=INK, randbreite=5, anim=anim, d=d, bis=bis,
                 zeilen=zeilen)


def wl_links(zeilen, x, y, size, cue, hl, rechts=1170, lh=1.28, marker=GELB):
    """Linksbündiger Wortlaut (wörtliches Zitat, Abruf Cellar/EUR-Lex 04.10.2026) mit Textmarker zum gesprochenen Wort.
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


def zitatkarte(zeilen, x, y, size, cue, hl, fill=ZITAT):
    """Wortlautkarte: Karte + linksbündiger Wortlaut mit Markern; gibt (Elemente, y_ende) zurück."""
    els, y1 = wl_links(zeilen, x + 30, y + 18, size, cue, hl, rechts=x + 1040 - 16)
    return [karte(x, y, 1040, int(y1 - y + 22), cue, fill=fill, rund=18, schatten=6, rand=4)] + els, y1 + 22


def lexi_bis_ende(cue):
    return (cue, round(DAUER - bausteine._t(cue) + 0.5, 3))       # Lexi bleibt bis zum letzten Frame (wie 161)


def rechts_frei(els, x0=1250):
    """Figuren und Requisiten der Tafelfolien stehen rechts der Tafel (x ≥ 1250)."""
    for e in els:
        n = e.name or ""
        if n.startswith(("bild:", "ficon:")) or "/op_176/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def namensschild(text, cx, unten, cue, fill, **k):
    return pille(glyphen(text), cx, unten + 22, cue, fill=fill, size=30, anker="m", **k)


def fund(text, x, y, cue, **k):
    """Fundstelle (mobil lesbar: 26 px)."""
    return z(text, x, y, cue, size=26, farbe=TEXT, **k)


# --- Eigene Hilfsfunktion (wie Folge 127/138): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ------------
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
FARBE = {"TR": ROT, "KL": TUERKIS}
NAME = {"TR": "Frau Trautmann", "KL": "Herr Kleinschmidt"}


def kette(prefix, x, folge, bis_=None, d=0.0, hoehe=FR, unten=BR):
    """Eine Figur mit Mimikfolge [(Name, Cue), …] im Zwiebelschalenprinzip (erster Auftritt pop, danach harte Schnitte)."""
    els = []
    for i, (n, c) in enumerate(folge):
        b = folge[i + 1][1] if i + 1 < len(folge) else bis_
        els.append(peep_voll(prefix + n, x, unten, hoehe, c, anim=("pop" if i == 0 else "cut"), d=(d if i == 0 else 0.0), bis=b))
    return els


def paar(cue, f1, f2):
    """Frau Trautmann (links) und Herr Kleinschmidt (rechts) neben der Tafel, beide blicken zur Tafel; Namensschilder ab Beginn."""
    els = kette("TR_", X1, [(f1[0][0], cue)] + list(f1[1:])) + kette("KL_", X2, [(f2[0][0], cue)] + list(f2[1:]), d=0.2)
    return els + [namensschild(NAME["TR"], X1, BR, cue, FARBE["TR"], d=0.2),
                  namensschild(NAME["KL"], X2, BR, cue, FARBE["KL"], d=0.3)]


def einzeln(p, cue, folge, x=XE):
    """Eine Figur rechts neben der Tafel (blickt zur Tafel) mit Namensschild."""
    return kette(p + "_", x, [(folge[0][0], cue)] + list(folge[1:])) + [namensschild(NAME[p], x, BR, cue, FARBE[p], d=0.2)]


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


def wechsel(texte, cx, y, size=28, fill=WEISS, anker="m", ende=None):
    """Pillen nacheinander an derselben Stelle: texte = [(Text, Cue, Füllung|None), …]."""
    els = []
    for i, (t, c, f) in enumerate(texte):
        b = texte[i + 1][1] if i + 1 < len(texte) else ende
        els.append(pl(t, cx, y, c, fill=f or fill, size=size, anker=anker, anim=("pop" if i == 0 else "cut"), bis=b))
    return els


def icons(folge, cx, unten, breite, ende=None):
    """Requisiten nacheinander an derselben Stelle: folge = [(set, name, Cue, Füllung), …]."""
    els = []
    for i, (s, n, c, f) in enumerate(folge):
        b = folge[i + 1][2] if i + 1 < len(folge) else ende
        els.append(ficon(s, n, cx, unten, breite, c, fuell=f, anim=("pop" if i == 0 else "cut"), bis=b))
    return els


# --- Eigene Ergänzungen Folge 176 ---------------------------------------------------------------------------------------
F1, F2, F3, F4 = BLAU, GRUEN, LILA, GELB          # eigene Farbe je Prüfungspunkt (1 Schutzbereich … 4 Rechtfertigung)
SF = {1: F1, 2: F2, 3: F3, 4: F4}
AMBER = (214, 150, 80, 255)                        # Flaschen (neutral, ohne Etikett/Marke)
KARTON = (222, 184, 135, 255)


def nr(n, x, y, cue, size=30, d=0.0, **k):
    """Farbige Schrittnummer (eigene Farbe je Prüfungspunkt)."""
    return pl(str(n), x, y, cue, fill=SF[n], size=size, d=d, **k)


def tafel_n(cue, n, titel_, h=840, size=46):
    """Rechtstafel eines Prüfungspunkts: farbiger Balken oben, Nummer in der Punktfarbe, Titel."""
    assert 205 + F("ExtraBold", size).getlength(glyphen(titel_)) <= 1170, f"Titel zu breit: {titel_}"
    return [karte(60, 60, 1140, h, cue), karte(60, 60, 1140, 26, cue, fill=SF[n], rund=12, schatten=0, rand=5),
            pl(f"{n}.", 110, 104, cue, fill=SF[n], size=40), titel(titel_, 205, 100, cue, size)]



def okz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Haken davor (zur gesprochenen Bejahung), wie Folge 172."""
    return [ok(x - 45, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]


def neinz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Kreuz davor (zur gesprochenen Verneinung), wie Folge 172."""
    return [nein(x - 45, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]


# A Fall: Lager des Getränkegroßhandels -----------------------------------------------------------------------------------
BODEN, GH = 900, 520
TRX, KLX = 380, 1580
TRa = ("TR_redet_r", TRX, BODEN, GH)
KLa = ("KL_redet", KLX, BODEN, GH)
KLb = ("KL_einsicht", KLX, BODEN, GH)
RX0, RX1 = 700, 1290                               # Regal


def lager(cue):
    """Bodenlinie, Regal aus Grundformen mit neutralen Flaschen (Tabler bottle) und Kartons (Tabler package), ohne Etiketten."""
    els = [linienzug([(60, BODEN), (1860, BODEN)], cue, breite=7, farbe=INK)]
    for xx in (RX0, RX1):
        els.append(linienzug([(xx, 470), (xx, BODEN)], cue, breite=8, farbe=INK))
    for yy in (620, 770):
        els.append(linienzug([(RX0 - 10, yy), (RX1 + 10, yy)], cue, breite=8, farbe=INK))
    for xx in range(760, 1250, 70):                 # Flaschen oben
        els.append(ficon("tabler", "bottle", xx, 616, 58, cue, fuell=AMBER, anim="cut"))
    for xx in (820, 995, 1170):                     # Kisten Mitte und am Boden
        els.append(ficon("tabler", "package", xx, 766, 130, cue, fuell=KARTON, anim="cut"))
    for xx in (850, 1050):
        els.append(ficon("tabler", "package", xx, BODEN - 4, 150, cue, fuell=KARTON, anim="cut"))
    return els


ZB = 990                                            # Mitte des Pillenbands über dem Regal
folie([("fall", "Fall · Frau Trautmann und ihr Whisky"), ("zeug", "Fall · Das Echtheitszeugnis"),
       ("klein", "Fall · Herr Kleinschmidt prüft das Lager"), ("frage", "Fall · Die Frage")], [
    *lager("fall"),
    pl("Getränkegroßhandel", 70, 40, "fall", fill=GELB, size=34, bis="klein"),
    *stufen([("TR_ruhig_r", "fall"), ("TR_froh_r", "kauf"), ("TR_entschlossen_r", "para"), ("TR_sorge_r", "zeug"),
             ("TR_ernst_r", "allein"), ("TR_ruhig_r", "klein"), ("TR_sorge_r", "k1"), ("TR_redet_r", "t1"),
             ("TR_denkt_r", "frage")], TRX, BODEN, GH, rede={"TR_redet_r": 1}, erst="cut"),
    namensschild(NAME["TR"], TRX, BODEN, "fall", FARBE["TR"]),
    # Einkauf im Nachbarland, Parallelimport, Zeugnis
    *icons([("tabler", "truck-delivery", "kauf", GELB), ("tabler", "route", "para", WEISS),
            ("tabler", "certificate", "zeug", HELL)], ZB, 440, 120, ende="klein"),
    *wechsel([("Einkauf beim Großhändler im Nachbarland", "kauf", BLAUHELL),
              ("Parallelimporteurin", "para", GELB),
              ("Verordnung ihres Landes: Echtheitszeugnis", "zeug", ROTHELL)], ZB, 135, size=30, ende="klein"),
    pl("dort rechtmäßig im Handel", ZB, 200, beim("kauf", "rechtmäßig"), fill=WEISS, size=28, anker="m", bis="para"),
    pl("nicht beim offiziellen Alleinimporteur", ZB, 200, beim("para", "nicht"), fill=WEISS, size=28, anker="m", bis="zeug"),
    pl("der Behörden des Herstellerlandes", ZB, 200, beim("zeug", "Behörden"), fill=WEISS, size=28, anker="m", bis="klein"),
    *wechsel([("Herstellerland: anderer EU-Staat", "hland", WEISS),
              ("bekommt praktisch nur, wer direkt beim Hersteller kauft", "allein", ROTHELL)], ZB, 262, size=28, ende="klein"),
    # Herr Kleinschmidt kommt durch die Tür ins Lager
    szene(ficon("tabler", "door", 1830, BODEN, 90, "klein", fuell=HOLZ), "176tuer*", 1.0, versatz=0.05),
    *stufen([("KL_ruhig", "klein"), ("KL_redet", "k1"), ("KL_ernst", "t1"), ("KL_denkt", "frage")],
            KLX, BODEN, GH, rede={"KL_redet": 1}),
    namensschild(NAME["KL"], KLX, BODEN, "klein", FARBE["KL"], d=0.2),
    pl("Lebensmittelüberwachung", ZB, 200, beim("klein", "Lebensmittelüberwachung"), fill=WEISS, size=30, anker="m", bis="k1"),
    blase("sprech", 820, 230, "k1", 1060, 235, inhalt=["Ohne Echtheitszeugnis", "dürfen Sie diese Kisten",
          "nicht verkaufen."], textsize=32, figur=KLa, bis="t1"),
    blase("sprech", 860, 230, "t1", 960, 235, inhalt=["Das Zeugnis bekomme ich nie.", "Die Flaschen sind echt,",
          "hier sind meine Rechnungen."], textsize=31, figur=TRa, bis="frage"),
    szene(ficon("tabler", "receipt", 615, 640, 80, beim("t1", "hier"), fuell=WEISS), "176papier*", 1.0, versatz=0.0),
    pl("Rechnungen", 615, 655, beim("t1", "hier"), fill=WEISS, size=26, anker="m"),
    pl("Verstößt die Pflicht zum Echtheitszeugnis", ZB, 150, "frage", fill=PINK, size=32, anker="m"),
    pl("gegen die Warenverkehrsfreiheit?", ZB, 222, "frage", fill=PINK, size=32, anker="m"),
])

# B Sachverhalt -------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    glyphen("Frau Trautmann betreibt einen Getränkegroßhandel. Whisky kauft sie als Parallelimporteurin bei einem "
            "Großhändler im Nachbarland, wo die Flaschen rechtmäßig im Handel sind, nicht beim offiziellen Alleinimporteur."),
    glyphen("Eine Verordnung ihres Landes verlangt für importierten Whisky ein Echtheitszeugnis der Behörden des "
            "Herstellerlandes, eines anderen EU-Staats. Das bekommt praktisch nur, wer direkt beim Hersteller kauft."),
    glyphen("Herr Kleinschmidt von der Lebensmittelüberwachung verbietet den Verkauf ohne Zeugnis. Frau Trautmann legt "
            "ihre Rechnungen vor."),
], "Verstößt die Pflicht zum Echtheitszeugnis gegen die Warenverkehrsfreiheit?")

# C Norm: Art. 34 AEUV (CELEX 12016E034, ABl. C 202 vom 7.6.2016, S. 61) und Prüfschema -------------------------------------
W34 = [[("„", 0), ("Mengenmäßige Einfuhrbeschränkungen", "a"), (" sowie", 0)],
       [("alle Maßnahmen gleicher Wirkung", "b"), (" sind ", 0), ("zwischen den", "c")],
       [("Mitgliedstaaten", "c"), (" verboten.“", 0)]]
_k34, _y34 = zitatkarte(W34, 110, 245, 33, "a34", {"a": beim("a34", "Mengenmäßige"), "b": beim("a34", "alle"),
                                                  "c": beim("a34", "zwischen")})
folie([("norm", "Norm › Art. 34 AEUV"), ("sch4", "Norm › Prüfschema in 4 Schritten")], rechts_frei([
    *tafel("norm", "Die Norm"),
    z("Art. 34 AEUV", 110, 180, "norm", "Bold", 36),
    *_k34,
    fund("Art. 34 AEUV, ABl. C 202 vom 7.6.2016, S. 61", 110, int(_y34 + 12), "a34"),
    z("Du prüfst in 4 Schritten:", 110, int(_y34 + 85), "sch4", "Bold", 36),
    fb(110, int(_y34 + 155), 505, 80, F1, "p1", [("1. Schutzbereich", "ExtraBold", 34, INK)]),
    fb(645, int(_y34 + 155), 505, 80, F2, "p2", [("2. Adressat", "ExtraBold", 34, INK)]),
    fb(110, int(_y34 + 260), 505, 80, F3, "p3", [("3. Beschränkung", "ExtraBold", 34, INK)]),
    fb(645, int(_y34 + 260), 505, 80, F4, beim("p4", "Rechtfertigung"), [("4. Rechtfertigung", "ExtraBold", 34, INK)]),
    *einzeln("TR", "norm", [("ruhig",), ("denkt", "a34"), ("entschlossen", "sch4")]),
    pl("Warenverkehrsfreiheit", XE, 250, "norm", fill=HELL, size=30, anker="m"),
]))

# D 1. Schutzbereich: Ware (Rs. 7/68, Slg. 1968, 634), grenzüberschreitender Bezug -------------------------------------------
P1 = "1. Schutzbereich"
WW = [[("„Unter Waren … sind Erzeugnisse zu verstehen, die einen", 0)],
      [("Geldwert", "a"), (" haben und deshalb ", 0), ("Gegenstand von Handels-", "b")],
      [("geschäften", "b"), (" sein können.“", 0)]]
_kw, _yw = zitatkarte(WW, 110, 240, 32, "ware", {"a": beim("ware", "Geldwert"), "b": beim("ware", "Gegenstand")})
folie([("s1", P1), ("ware", f"{P1} › Ware"), ("grenz", f"{P1} › grenzüberschreitender Bezug")], rechts_frei([
    *tafel_n("s1", 1, "Schutzbereich"),
    z("Ware", 110, 180, "ware", "Bold", 36),
    *_kw,
    fund("EuGH, Urt. v. 10.12.1968 – Rs. 7/68 (Kommission/Italien), Slg. 1968, 634", 110, int(_yw + 12), "ital"),
    z("sogar Kunstwerke und historische Gegenstände", 110, int(_yw + 62), beim("ital", "Kunstwerke"), size=34),
    *okz("Whisky: eine Ware", int(_yw + 150), "whisky", "Bold", 36),
    *okz("grenzüberschreitend: aus anderen Mitgliedstaaten", int(_yw + 225), "grenz", "Bold", 34),
    pl("Schutzbereich", IX, 200, "s1", fill=F1, size=32, anker="m", bis="ware"),
    *icons([("tabler", "coins", beim("ware", "Geldwert"), GELB), ("tabler", "palette", beim("ital", "Kunstwerke"), BLAUHELL),
            ("tabler", "bottle", "whisky", AMBER), ("tabler", "world", "grenz", BLAU)], IX, 560, 190),
    *wechsel([("Ware?", "ware", F1), ("Geldwert", beim("ware", "Geldwert"), GELB),
              ("Kunstwerke: auch Waren", beim("ital", "Kunstwerke"), BLAUHELL), ("Whisky: Ware", "whisky", GRUENHELL),
              ("aus anderen Mitgliedstaaten", "grenz", BLAUHELL)], IX, 200, size=30),
]))

# E 2. Adressat: Mitgliedstaat, staatliche Maßnahme ---------------------------------------------------------------------------
P2 = "2. Adressat"
folie([("s2", P2), ("vo", f"{P2} › im Fall: Verordnung des Landes")], rechts_frei([
    *tafel_n("s2", 2, "Adressat"),
    z("Art. 34 AEUV bindet die Mitgliedstaaten", 110, 195, "mst", "Bold", 36),
    z("also: eine staatliche Maßnahme", 110, 255, beim("mst", "staatliche"), size=36),
    fund("Art. 34 AEUV („zwischen den Mitgliedstaaten“); Dassonville, Rn. 5", 110, 320, beim("mst", "staatliche")),
    karte(110, 400, 1040, 150, "vo", fill=GRUENHELL, rund=18, schatten=6, rand=4),
    *okz("Im Fall: Das Land selbst verlangt", 420, "vo", "Bold", 34, x=185),
    z("das Zeugnis, durch eine Verordnung", 185, 480, beim("vo", "Verordnung"), size=34),
    *einzeln("KL", "s2", [("ruhig",), ("ernst", "mst"), ("still", "vo")]),
    *wechsel([("Adressat?", "s2", F2), ("staatliche Maßnahme", beim("mst", "staatliche"), F2),
              ("Verordnung des Landes", beim("vo", "Verordnung"), GRUENHELL)], XE, 250, size=30),
]))

# F 3. Beschränkung: mengenmäßig / Maßnahme gleicher Wirkung; der echte Fall Dassonville (Rs. 8/74, Rn. 2/4) -------------------
P3 = "3. Beschränkung"
folie([("s3", P3), ("mgw", f"{P3} › Maßnahme gleicher Wirkung?"), ("dass", f"{P3} › Dassonville, EuGH 1974")],
      rechts_frei([
    *tafel_n("s3", 3, "Beschränkung"),
    z("mengenmäßig: ganze oder teilweise Einfuhrverbote", 110, 185, "menge", size=34),
    fund("EuGH, Rs. 2/73 (Geddo), Slg. 1973, 865, Rn. 7", 110, 237, "menge"),
    z("Maßnahme gleicher Wirkung?", 110, 290, "mgw", "Bold", 36),
    karte(110, 360, 1040, 400, "dass", fill=LILAHELL, rund=18, schatten=6, rand=4),
    z("Der echte Fall: Dassonville, EuGH 1974", 140, 380, "dass", "ExtraBold", 34, rechts=1140),
    z("Belgien verlangte für Scotch Whisky eine Ursprungs-", 140, 445, "bel", size=32, rechts=1140),
    z("bescheinigung der britischen Zollbehörden.", 140, 490, beim("bel", "Ursprungsbescheinigung"), size=32, rechts=1140),
    z("Händler kauften den Whisky in Frankreich,", 140, 555, "frank", size=32, rechts=1140),
    z("wo er im freien Verkehr war.", 140, 600, beim("frank", "wo"), size=32, rechts=1140),
    z("Bescheinigung: nur mit erheblichen Schwierigkeiten", 140, 665, "schwer", "Bold", 32, rechts=1140),
    fund("EuGH, Urt. v. 11.7.1974 – Rs. 8/74 (Dassonville), Slg. 1974, 837, Rn. 2/4", 110, 780, "dass"),
    pl("Beschränkung", IX, 200, "s3", fill=F3, size=32, anker="m", bis="dass"),
    ficon("tabler", "ban", IX, 560, 180, "menge", fuell=ROTHELL, bis="mgw"),
    pl("Einfuhrverbot", IX, 640, "menge", fill=ROTHELL, size=30, anker="m", bis="mgw"),
    *icons([("tabler", "file-certificate", "bel", HELL),
            ("tabler", "truck-delivery", "frank", GELB), ("tabler", "certificate-off", "schwer", ROTHELL)], IX, 560, 180),
    *wechsel([("Ursprungsbescheinigung", "bel", HELL), ("Einkauf in Frankreich", "frank", BLAUHELL),
              ("kaum zu beschaffen", "schwer", ROTHELL)], IX, 640, size=30),
    pl("Dassonville, EuGH 1974", IX, 200, "dass", fill=LILA, size=30, anker="m"),
]))

# G Dassonville-Formel (Rn. 5) -----------------------------------------------------------------------------------------------
WF = [[("„", 0), ("Jede Handelsregelung der Mitgliedstaaten", "a"), (", die ", 0), ("geeignet", "b")],
      [("ist, den innergemeinschaftlichen Handel ", 0), ("unmittelbar", "c")],
      [("oder mittelbar", "c"), (", ", 0), ("tatsächlich oder potentiell", "d"), (" zu behindern,", 0)],
      [("ist als ", 0), ("Maßnahme mit gleicher Wirkung", "e"), (" wie eine", 0)],
      [("mengenmäßige Beschränkung anzusehen.“", 0)]]
_kf, _yf = zitatkarte(WF, 110, 250, 32, "formel", {"a": beim("formel", "Jede"), "b": beim("formel", "geeignet"),
                                                  "c": beim("formel", "unmittelbar"), "d": beim("formel", "tatsächlich"),
                                                  "e": beim("formel", "Maßnahme")})
folie([("formel", f"{P3} › Dassonville-Formel"), ("weit", f"{P3} › Schon die Eignung genügt")], rechts_frei([
    *tafel_n("formel", 3, "Die Dassonville-Formel"),
    z("Maßnahme gleicher Wirkung", 110, 180, "formel", "Bold", 36),
    *_kf,
    fund("EuGH, Rs. 8/74 (Dassonville), Slg. 1974, 837, Rn. 5", 110, int(_yf + 12), "formel"),
    fb(110, int(_yf + 80), 1040, 90, F3, "weit", [("Schon die Eignung zur Behinderung genügt", "ExtraBold", 34, INK)]),
    *einzeln("TR", "formel", [("ruhig",), ("denkt", beim("formel", "tatsächlich")), ("staunt", "weit")]),
    pl("sehr weit", XE, 250, "weit", fill=F3, size=30, anker="m"),
]))

# H Grenze Keck (verb. Rs. C-267/91 und C-268/91, Rn. 16) ---------------------------------------------------------------------
folie([("keck", f"{P3} › Grenze: Keck, EuGH 1993"), ("kfall", f"{P3} › im Fall: Maßnahme gleicher Wirkung")], rechts_frei([
    *tafel_n("keck", 3, "Grenze: Keck"),
    z("Verkaufsmodalitäten fallen nicht darunter, wenn sie", 110, 185, beim("keck", "Verkaufsmodalitäten"), "Bold", 33),
    z("für alle Wirtschaftsteilnehmer im Inland gelten", 140, 240, beim("keck", "alle"), size=33),
    z("und den Absatz inländischer wie eingeführter Waren", 140, 290, beim("keck", "Absatz"), size=33),
    z("rechtlich wie tatsächlich gleich berühren", 140, 340, beim("keck", "rechtlich"), size=33),
    fund("EuGH, Urt. v. 24.11.1993 – verb. Rs. C-267/91 und C-268/91 (Keck), Rn. 16", 110, 395, beim("keck", "rechtlich")),
    karte(110, 455, 1040, 190, "kfall", fill=HELL, rund=18, schatten=6, rand=4),
    z("Im Fall:", 140, 470, "kfall", "Bold", 33, rechts=1140),
    *neinz("keine Verkaufsmodalität, sondern die Einfuhr", 520, beim("kfall", "keine"), size=33, x=200),
    *neinz("trifft nur eingeführten Whisky", 575, beim("kfall", "trifft"), size=33, x=200),
    fb(110, 680, 1040, 90, F3, "mgw2", [("Also: Maßnahme gleicher Wirkung", "ExtraBold", 34, INK)]),
    *paar("keck", [("ruhig",), ("denkt", "kfall"), ("entschlossen", "mgw2")],
          [("ruhig",), ("denkt", beim("keck", "Verkaufsmodalitäten")), ("ernst", "kfall"), ("still", "mgw2")]),
    pl("Keck, EuGH 1993", (X1 + X2) // 2, 250, "keck", fill=F3, size=30, anker="m"),
]))

# I 4. Rechtfertigung: Art. 36 AEUV (CELEX 12016E036, ABl. C 202 vom 7.6.2016, S. 61) ----------------------------------------
P4 = "4. Rechtfertigung"
W36 = [[("„Die Bestimmungen der Artikel 34 und 35 stehen Einfuhr-, Ausfuhr-", 0)],
       [("und Durchfuhrverboten oder -beschränkungen nicht entgegen, die aus", 0)],
       [("Gründen der öffentlichen Sittlichkeit, Ordnung und Sicherheit, zum", 0)],
       [("Schutze der ", 0), ("Gesundheit", "a"), (" und des Lebens von Menschen, Tieren oder", 0)],
       [("Pflanzen, des nationalen Kulturguts von künstlerischem, geschichtlichem", 0)],
       [("oder archäologischem Wert oder des ", 0), ("gewerblichen und kommerziellen", "b")],
       [("Eigentums", "b"), (" gerechtfertigt sind. Diese Verbote oder Beschränkungen dürfen", 0)],
       [("jedoch weder ein Mittel zur ", 0), ("willkürlichen Diskriminierung", "c"), (" noch eine", 0)],
       [("verschleierte Beschränkung", "d"), (" des Handels zwischen den Mitgliedstaaten", 0)],
       [("darstellen.“", 0)]]
_k36, _y36 = zitatkarte(W36, 110, 240, 28, "a36", {"a": beim("a36", "Gesundheit"), "b": beim("eig", "gewerblichen"),
                                                  "c": beim("satz2", "willkürlichen"), "d": beim("satz2", "verschleierte")})
folie([("s4", P4), ("a36", f"{P4} › Art. 36 AEUV"), ("satz2", f"{P4} › Art. 36 Satz 2: keine Diskriminierung")],
      rechts_frei([
    *tafel_n("s4", 4, "Rechtfertigung"),
    z("Art. 36 AEUV", 110, 180, "a36", "Bold", 36),
    *_k36,
    fund("Art. 36 AEUV, ABl. C 202 vom 7.6.2016, S. 61", 110, int(_y36 + 12), "a36"),
    *einzeln("KL", "s4", [("ruhig",), ("denkt", "a36"), ("ernst", "satz2")]),
    *wechsel([("Rechtfertigung?", "s4", F4), ("z. B. Gesundheit", beim("a36", "Gesundheit"), GELB),
              ("gewerbliches und kommerzielles Eigentum", beim("eig", "gewerblichen"), GELB),
              ("Satz 2: keine willkürliche Diskriminierung", "satz2", ROTHELL)], 1530, 250, size=28),
]))

# J Cassis de Dijon (Rs. 120/78, Rn. 8) und Verhältnismäßigkeit (C-110/05, Rn. 59) ---------------------------------------------
folie([("cassis", f"{P4} › zwingende Erfordernisse: Cassis de Dijon"), ("vhm", f"{P4} › Verhältnismäßigkeit")], rechts_frei([
    *tafel_n("cassis", 4, "Zwingende Erfordernisse"),
    z("Cassis de Dijon, EuGH 1979: zwingende Erfordernisse,", 110, 185, "cassis", "Bold", 33),
    z("etwa Verbraucherschutz und Lauterkeit des Handelsverkehrs", 110, 240, beim("cassis", "Verbraucherschutz"), size=33),
    fund("EuGH, Urt. v. 20.2.1979 – Rs. 120/78 (Cassis de Dijon), Slg. 1979, 649, Rn. 8", 110, 295, beim("cassis", "Lauterkeit")),
    z("In beiden Fällen:", 110, 390, "vhm", "Bold", 36),
    fb(110, 450, 1040, 130, F4, beim("vhm", "geeignet"), [("geeignet und nicht über das", "ExtraBold", 34, INK),
                                                       ("Erforderliche hinaus", "ExtraBold", 34, INK)]),
    fund("EuGH (Große Kammer), Urt. v. 10.2.2009 – C-110/05 (Kommission/Italien), Rn. 59", 110, 595, beim("vhm", "Erforderliche")),
    *icons([("tabler", "shield-check", beim("cassis", "Verbraucherschutz"), GRUENHELL), ("tabler", "scale", "vhm", GELB)],
           IX, 560, 200),
    *wechsel([("Cassis de Dijon, EuGH 1979", "cassis", F4), ("Verbraucherschutz", beim("cassis", "Verbraucherschutz"), GRUENHELL),
              ("verhältnismäßig?", "vhm", GELB)], IX, 250, size=30),
]))

# K Dassonville Rn. 6 und 7/9: Nachweis für alle, nicht nur für Direktimporteure ----------------------------------------------
folie([("dfal", f"{P4} › Dassonville: Nachweis für alle")], rechts_frei([
    *tafel_n("dfal", 4, "Dassonville: Nachweis für alle"),
    z("Staat darf gegen unlautere Verhaltensweisen", 110, 185, "dfal", "Bold", 34),
    z("bei Ursprungsbezeichnungen vorgehen", 110, 235, beim("dfal", "Ursprungsbezeichnungen"), "Bold", 34),
    *okz("aber nur mit sinnvollen Maßnahmen", 320, "sinn", size=34),
    *okz("Nachweise von allen Staatsangehörigen erbringbar", 380, beim("sinn", "Nachweise"), size=34),
    fund("Dassonville, Rn. 6", 140, 440, beim("sinn", "Nachweise")),
    fb(110, 510, 1040, 130, ROTHELL, "direkt", [("Formalitäten praktisch nur für Direktimporteure:", "ExtraBold", 32, INK),
                                               ("kann verschleierte Beschränkung sein", "ExtraBold", 32, INK)]),
    fund("Dassonville, Rn. 7/9; Art. 36 Satz 2 AEUV", 110, 655, "direkt"),
    *paar("dfal", [("ruhig",), ("denkt", "sinn"), ("entschlossen", "direkt")],
          [("ernst",), ("denkt", "sinn"), ("staunt", "direkt")]),
    pl("Nachweis für alle?", (X1 + X2) // 2, 250, beim("sinn", "Nachweise"), fill=F4, size=30, anker="m"),
]))

# L Lösung -----------------------------------------------------------------------------------------------------------------
PL_ = "Lösung"
folie([("loes", f"{PL_} · Frau Trautmann"), ("l5", f"{PL_} · Rechtfertigung: unverhältnismäßig")], rechts_frei([
    *tafel("loes", "Lösung: Frau Trautmann"),
    nr(1, 110, 182, "l1"), z("Ware aus anderen Mitgliedstaaten", 200, 180, "l1", size=34), ok(1110, 200, "l1", gr=18),
    nr(2, 110, 247, "l2"), z("Verordnung des Landes: staatliche Maßnahme", 200, 245, "l2", size=34), ok(1110, 265, "l2", gr=18),
    nr(3, 110, 312, "l3"), z("Maßnahme gleicher Wirkung", 200, 310, "l3", size=34), ok(1110, 330, "l3", gr=18),
    nr(4, 110, 377, "l4"), z("Verbraucherschutz: legitimes Ziel", 200, 375, "l4", size=34),
    *neinz("aber: Parallelimporteure faktisch ausgeschlossen", 440, "l5", "Bold", 33, x=220),
    karte(110, 520, 1040, 150, "mild", fill=GRUENHELL, rund=18, schatten=6, rand=4),
    z("milder: Nachweise, die jeder Händler erbringen", 140, 540, "mild", "Bold", 33, rechts=1140),
    z("kann, etwa Rechnungen über die Lieferkette", 140, 590, beim("mild", "etwa"), size=33, rechts=1140),
    fund("Dassonville, Rn. 6; C-110/05, Rn. 59", 110, 685, "mild"),
    *paar("loes", [("ruhig",), ("froh", "l1"), ("sorge", "l5"), ("entschlossen", "mild")],
          [("ruhig",), ("denkt", "l3"), ("ernst", "l4"), ("staunt", "mild")]),
]))

# M Zurück im Lager: Verstoß, unmittelbare Wirkung, Anwendungsvorrang; Herr Kleinschmidt prüft die Rechnungen ------------------
folie([("l6", f"{PL_} · Verstoß gegen Art. 34 AEUV"), ("vorr", f"{PL_} · Anwendungsvorrang"),
       ("k2", f"{PL_} · Herr Kleinschmidt prüft die Rechnungen")], [
    *lager("l6"),
    pl("Pflicht unverhältnismäßig: Verstoß gegen Art. 34 AEUV", ZB, 135, "l6", fill=ROTHELL, size=30, anker="m", bis="k2"),
    pl("Frau Trautmann kann sich unmittelbar darauf berufen", ZB, 205, "unm", fill=WEISS, size=28, anker="m", bis="k2"),
    pl("(Iannelli, Rs. 74/76, Rn. 13)", ZB, 262, beim("unm", "unmittelbar"), fill=WEISS, size=26, anker="m", bis="k2"),
    pl("Verordnung insoweit unangewendet: Anwendungsvorrang", ZB, 330, "vorr", fill=HELL, size=28, anker="m", bis="k2"),
    pl("Video „Costa/ENEL“", ZB, 392, beim("vorr", "Video"), fill=BLAUHELL, size=26, anker="m", bis="k2"),
    ficon("tabler", "door", 1830, BODEN, 90, "l6", fuell=HOLZ, anim="cut"),
    ficon("tabler", "receipt", 615, 640, 80, "l6", fuell=WEISS, anim="cut", bis="k2"),
    pl("Rechnungen", 615, 655, "l6", fill=WEISS, size=26, anker="m", anim="cut", bis="k2"),
    *stufen([("TR_ruhig_r", "l6"), ("TR_froh_r", "unm"), ("TR_entschlossen_r", "vorr"), ("TR_froh_r", "k2")],
            TRX, BODEN, GH, erst="cut", ende="tipp"),
    namensschild(NAME["TR"], TRX, BODEN, "l6", FARBE["TR"]),
    *stufen([("KL_ernst", "l6"), ("KL_denkt", "unm"), ("KL_still", "vorr"), ("KL_einsicht", "k2")], KLX, BODEN, GH,
            rede={"KL_einsicht": 1}, erst="cut", ende="tipp"),
    namensschild(NAME["KL"], KLX, BODEN, "l6", FARBE["KL"]),
    blase("sprech", 700, 190, "k2", 1100, 240, inhalt=["Dann prüfe ich eben", "Ihre Rechnungen."], textsize=34, figur=KLb),
    szene(ficon("tabler", "receipt", 1380, 700, 80, beim("k2", "Rechnungen"), fuell=WEISS), "176papier*", 1.0),
])

# N Klausurtipp (Lexi) ---------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · Zölle und Abgaben: Art. 30 AEUV"), ("tf", "Klausurtipp · Keck nur bei Verkaufsmodalitäten")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Geld, also Zölle oder Abgaben gleicher Wirkung:", 200, 200, beim("tipp", "Geld"), "Bold", 34),
    z("Art. 30 AEUV, nicht Art. 34", 200, 255, beim("tipp", "prüfst"), "Bold", 34),
    fund("Art. 30 AEUV, ABl. C 202 vom 7.6.2016, S. 60", 200, 312, beim("tipp", "prüfst")),
    fb(200, 400, 950, 180, GELB, "tf", [("Keck nur bei Verkaufsmodalitäten,", "ExtraBold", 32, INK),
                                      ("etwa Verbot des Weiterverkaufs", "ExtraBold", 32, INK),
                                      ("unter dem Einkaufspreis", "ExtraBold", 32, INK)]),
    fund("Keck, Rn. 2, 16, 18", 200, 595, "tf"),
    *redet("LX_warnt", LXX, BR, FR + 60, "tipp", "sch"),
    namensschild("Lexi", LXX, BR, "tipp", GELB, d=0.2),
])

# O Klausurschema ------------------------------------------------------------------------------------------------------------
PS_ = "Klausurschema"
FX = 1270                              # Fundstellen rechts
folie([("sch", PS_), ("z1", f"{PS_} › I. Schutzbereich"), ("z2", f"{PS_} › II. Adressat"), ("z3", f"{PS_} › III. Beschränkung"),
       ("z4", f"{PS_} › IV. Rechtfertigung")], [
    karte(60, 50, 1800, 920, "sch"),
    titel("Klausurschema: Art. 34 AEUV", 110, 85, "sch", 48),
    pl("I.", 110, 172, "z1", fill=F1, size=32), z("Schutzbereich", 245, 170, "z1", "Bold", 36, rechts=FX - 20),
    z("1. Ware", 245, 232, "z1a", size=33, rechts=FX - 20),
    z("Rs. 7/68 (Kommission/Italien)", FX, 237, "z1a", size=28, farbe=TEXT, rechts=1840),
    z("2. grenzüberschreitender Bezug", 245, 287, "z1b", size=33, rechts=FX - 20),
    pl("II.", 110, 362, "z2", fill=F2, size=32), z("Adressat: staatliche Maßnahme", 245, 360, "z2", "Bold", 36, rechts=FX - 20),
    z("Art. 34 AEUV", FX, 367, "z2", size=28, farbe=TEXT, rechts=1840),
    pl("III.", 110, 447, "z3", fill=F3, size=32), z("Beschränkung", 245, 445, "z3", "Bold", 36, rechts=FX - 20),
    z("1. mengenmäßig oder gleicher Wirkung (Dassonville)", 245, 507, "z3a", size=33, rechts=FX - 20),
    z("Rs. 8/74, Rn. 5", FX, 512, "z3a", size=28, farbe=TEXT, rechts=1840),
    z("2. Grenze: Keck (Verkaufsmodalitäten)", 245, 562, "z3b", size=33, rechts=FX - 20),
    z("C-267/91 u. C-268/91, Rn. 16", FX, 567, "z3b", size=28, farbe=TEXT, rechts=1840),
    pl("IV.", 110, 642, "z4", fill=F4, size=32), z("Rechtfertigung", 245, 640, "z4", "Bold", 36, rechts=FX - 20),
    z("1. Art. 36 AEUV oder zwingende Erfordernisse", 245, 702, "z4a", size=33, rechts=FX - 20),
    z("Art. 36 AEUV; Rs. 120/78, Rn. 8", FX, 707, "z4a", size=28, farbe=TEXT, rechts=1840),
    z("2. jeweils verhältnismäßig", 245, 757, "z4b", size=33, rechts=FX - 20),
    z("C-110/05, Rn. 59", FX, 762, "z4b", size=28, farbe=TEXT, rechts=1840),
])

# P Merksatz (Lexi) --------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Jede staatliche Regel, die den Handel", 0)],
                 [("zwischen Mitgliedstaaten auch nur", 0)],
                 [("potentiell behindern kann", "a"), (", ist eine", 0)],
                 [("Maßnahme gleicher Wirkung", "b"), (".", 0)]], 750, 300, 42, "merke",
                {"a": beim("merke", "potentiell"), "b": beim("merke", "Maßnahme")}),
    *markertext([[("Ein Echtheitsnachweis muss für jeden", 0)],
                 [("Händler erreichbar sein, ", 0), ("auch für", "c")],
                 [("Parallelimporteure", "c"), (".", 0)]], 750, 620, 42, "m2", {"c": beim("m2", "auch")}),
    *redet("LX_erklaert", 1680, 960, 690, "merke", lexi_bis_ende("merke")),
    namensschild("Lexi", 1680, 960, "merke", GELB, d=0.2),
])
