"""Folge 127 · Costa/ENEL: Anwendungsvorrang – EU-Recht verdrängt deutsches Recht – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A Fall in der Limonadenmanufaktur (Hedwig, Herr Lammert), B Sachverhalt, C1 der echte Fall
Costa/ENEL (Herr Costa nur namentlich, keine Figur), C2 Italien gegen den Gerichtshof, C3 Kernsatz (Zitatkarte), D Simmenthal
II und Fratelli Costanzo, E Anwendungsvorrang statt Geltungsvorrang, F1 Erklärung Nr. 17 (Wortlautkarte), F2 Art. 4 Abs. 3
EUV (Wortlautkarte), G Grenzen aus deutscher Sicht, H1 Lösung I (Wortlautkarte Art. 288 Abs. 2 AEUV), H2 Lösung II/III,
H3 Ergebnis (zurück in der Manufaktur), I Klausurtipp (Lexi), J Klausurschema, K Merksatz (Lexi).
Geräusche nur bei sichtbarer Handlung: Flaschenklirren (Flaschen erscheinen), Klopfen (Tür, Herr Lammert kommt), Freesound CC0.
Hilfsfunktionen (z, pl, tafel, wortlaut, fb, redet mit hörbarem Wortende …) wie in Folge 091, Kopie im eigenen Ordner."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont

bausteine.FIGORDNER = "op_127/"
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


def wortlaut(x, y, w, h, cue, zeilen, size, hl, quelle, quelle_cue=None):
    """Wortlautkarte: wörtliches Zitat (EUR-Lex/Cellar, Abruf 03.10.2026) in einer hellen Karte, Fundstelle darunter rechts.
    zeilen = Liste von Token-Listen [(text, Schlüssel|0)], hl = {Schlüssel: Cue} (Hervorhebung zum gesprochenen Wort)."""
    for toks in zeilen:
        glyphen("".join(t for t, _ in toks))
    els = [karte(x, y, w, h, cue, fill=(246, 246, 250, 255), rund=18, schatten=6, rand=4)]
    m = markertext(zeilen, x + w / 2, y + 22, size, cue, hl, marker=GELB, lh=1.28)
    assert m[0].x >= x + 10 and m[0].x + m[0].sprite.width <= x + w - 10, f"Wortlaut zu breit ({m[0].sprite.width} > {w})"
    assert m[0].y + m[0].sprite.height <= y + h + 6, "Wortlaut zu hoch"
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


# --- Eigene Hilfsfunktion (wie Folge 091): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ----------------
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
IX = 1580                               # Requisiten rechts (Folien ohne Figuren)
FARBE = {"HE": GRUEN, "LA": BLAU}
NAME = {"HE": "Hedwig", "LA": "Herr Lammert"}


def kette(prefix, x, folge, bis_=None, d=0.0, hoehe=FR, unten=BR):
    """Eine Figur mit Mimikfolge [(Name, Cue), …] im Zwiebelschalenprinzip (erster Auftritt pop, danach harte Schnitte)."""
    els = []
    for i, (n, c) in enumerate(folge):
        b = folge[i + 1][1] if i + 1 < len(folge) else bis_
        els.append(peep_voll(prefix + n, x, unten, hoehe, c, anim=("pop" if i == 0 else "cut"), d=(d if i == 0 else 0.0), bis=b))
    return els


def paar(cue, f1, f2):
    """Hedwig (links) und Herr Lammert (rechts) neben der Tafel, beide blicken zur Tafel; Namensschilder ab dem ersten Bild."""
    els = kette("HE_", X1, [(f1[0][0], cue)] + list(f1[1:])) + kette("LA_", X2, [(f2[0][0], cue)] + list(f2[1:]), d=0.2)
    return els + [namensschild(NAME["HE"], X1, BR, cue, FARBE["HE"], d=0.2),
                  namensschild(NAME["LA"], X2, BR, cue, FARBE["LA"], d=0.3)]


def stufen(folge, x, unten, hoehe, rede=None, erst="pop"):
    """Figur in der Fallszene: folge = [(Bildname, Cue), …]; rede = {Bildname: 1} für Figurenrede."""
    els = []
    for i, (n, c) in enumerate(folge):
        b = folge[i + 1][1] if i + 1 < len(folge) else None
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


# A Fall: in der Limonadenmanufaktur -------------------------------------------------------------------------------------
BODEN, GH = 900, 520
HEX, LAX = 380, 1620
HEa = ("HE_redet_r", HEX, BODEN, GH)
LAa = ("LA_redet", LAX, BODEN, GH)


def manufaktur(cue, flaschen_cue, mit_ton):
    """Bodenlinie, Arbeitstisch (Grundformen), Zitrone und drei Limonadenflaschen."""
    els = [linienzug([(60, BODEN), (1860, BODEN)], cue, breite=7, farbe=INK),
           karte(720, 742, 360, 34, cue, fill=HOLZ, rund=10, schatten=0, rand=5),
           karte(878, 776, 44, BODEN - 776, cue, fill=HOLZD, rund=6, schatten=0, rand=5),
           ficon("tabler", "lemon", 1040, 744, 60, cue, fuell=GELB)]
    for i, x in enumerate((760, 830, 900)):
        f = ficon("tabler", "bottle", x, 744, 62, flaschen_cue, fuell=GELB, d=0.08 * i)
        els.append(szene(f, "127flaschen*", 1.0, versatz=0.05) if (mit_ton and i == 0) else f)
    return els


folie([("fall", "Fall · Hedwig und ihre Limonade"), ("vo", "Fall · Die EU-Verordnung erlaubt"),
       ("gesetz", "Fall · Das deutsche Gesetz verbietet"), ("amt", "Fall · Die Kontrolle"), ("frage", "Fall · Die Frage")], [
    *manufaktur("fall", beim("suess", "Limonade"), True),
    pl("kleine Limonadenmanufaktur", 70, 40, "fall", fill=GELB, size=34, bis="vo"),
    ficon("tabler", "cube", 970, 744, 50, beim("suess", "Süßstoff"), fuell=WEISS),
    pl("neuer Süßstoff", 970, 640, beim("suess", "Süßstoff"), fill=WEISS, size=28, anker="m", bis="amt"),
    *stufen([("HE_ruhig_r", "fall"), ("HE_froh_r", beim("suess", "Limonade")), ("HE_staunt_r", "gesetz"),
             ("HE_sorge_r", "l1"), ("HE_redet_r", "h1"), ("HE_sorge_r", "l2"), ("HE_denkt_r", "frage")], HEX, BODEN, GH,
            rede={"HE_redet_r": 1}, erst="cut"),
    namensschild("Hedwig", HEX, BODEN, "fall", FARBE["HE"]),
    # EU-Verordnung und deutsches Gesetz
    ficon("tabler", "file-certificate", 650, 280, 110, beim("vo", "EU-Verordnung"), fuell=BLAU),
    pl("EU-Verordnung: ausdrücklich erlaubt", 650, 300, beim("vo", "ausdrücklich"), fill=GRUEN, size=28, anker="m"),
    ficon("tabler", "book", 1180, 280, 110, beim("gesetz", "deutsches"), fuell=ROT),
    ficon("tabler", "ban", 1240, 220, 64, beim("gesetz", "verbietet"), fuell=WEISS),
    pl("deutsches Gesetz: verboten", 1180, 300, beim("gesetz", "verbietet"), fill=ROTHELL, size=28, anker="m"),
    # Herr Lammert kommt zur Kontrolle (Tür, Klopfen)
    szene(ficon("tabler", "door", 1810, BODEN, 100, beim("amt", "Herr"), fuell=HOLZ), "127klopfen*", 1.0, versatz=0.05),
    *stufen([("LA_ernst", beim("amt", "Lebensmittelüberwachung")), ("LA_redet", "l1"), ("LA_denkt", "h1"),
             ("LA_redet", "l2"), ("LA_ernst", "frage")], LAX, BODEN, GH, rede={"LA_redet": 1}),
    namensschild("Herr Lammert", LAX, BODEN, beim("amt", "Lebensmittelüberwachung"), FARBE["LA"], d=0.2),
    ficon("tabler", "clipboard-check", 1440, 640, 70, beim("amt", "Kontrolle"), fuell=WEISS, bis="frage"),
    pl("Lebensmittelüberwachung", LAX, 300, beim("amt", "Lebensmittelüberwachung"), fill=BLAU, size=28, anker="m", bis="l1"),
    # Figurenrede
    blase("sprech", 860, 210, "l1", 1061, 521, inhalt=["Das deutsche Gesetz verbietet diesen Süßstoff.",
          "Sie dürfen die Limonade nicht verkaufen."], textsize=30, figur=LAa, bis="h1"),
    blase("sprech", 600, 200, "h1", 821, 521, inhalt=["Aber die EU-Verordnung", "erlaubt ihn ausdrücklich!"],
          textsize=32, figur=HEa, bis="l2"),
    blase("sprech", 560, 200, "l2", 1181, 521, inhalt=["An das deutsche Gesetz", "bin ich gebunden."], textsize=32,
          figur=LAa, bis="frage"),
    # Die Frage
    pl("2 Regeln, 1 Widerspruch", 1000, 420, "frage", fill=WEISS, size=30, anker="m"),
    pl("Woran hält sich das Amt?", 1000, 500, beim("frage", "Woran"), fill=PINK, size=34, anker="m"),
    pl("Und was wird aus dem deutschen Gesetz?", 1000, 580, "frage2", fill=GELB, size=30, anker="m"),
])

# B Sachverhalt -------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    glyphen("Hedwig betreibt eine kleine Limonadenmanufaktur und süßt ihre neue Limonade mit einem neuen Süßstoff. Eine "
            "EU-Verordnung lässt genau diesen Süßstoff für Limonaden ausdrücklich zu. Ein deutsches Gesetz verbietet ihn "
            "dagegen."),
    glyphen("Herr Lammert von der Lebensmittelüberwachung kommt zur Kontrolle. Er will Hedwig den Verkauf der Limonade "
            "untersagen: Er sei an das deutsche Gesetz gebunden. Hedwig beruft sich auf die EU-Verordnung."),
], "Woran hält sich das Amt – und was wird aus dem deutschen Gesetz?")

# C1 Der echte Fall: Costa/ENEL -------------------------------------------------------------------------------------------
folie([("costa", "Der echte Fall · Costa/ENEL, EuGH 1964"), ("rechn", "Der echte Fall › Die Stromrechnung"),
       ("vorl", "Der echte Fall › Die Vorlage an den Gerichtshof")], rechts_frei([
    *tafel("costa", "Der echte Fall: Costa/ENEL"),
    z("EuGH, Urteil vom 15.7.1964", 110, 185, beim("costa", "Europäischer"), "Bold", 34),
    fund("Rs. 6/64, Slg. 1964, 1253", 110, 235, beim("costa", "Urteil")),
    z("1962: Italien verstaatlicht die Stromwirtschaft", 110, 305, "verst", "Bold", 32),
    z("Versorger ist nun ENEL", 110, 352, beim("verst", "Versorger"), size=32),
    z("Flaminio Costa, Rechtsanwalt in Mailand:", 110, 430, "rechn", "Bold", 32),
    z("Stromrechnung über 1.925 Lire nicht bezahlt", 110, 477, beim("rechn", "Stromrechnung"), size=32),
    z("Verstaatlichungsgesetz verstoße gegen den EWG-Vertrag", 110, 524, beim("rechn", "Verstaatlichungsgesetz"), size=31),
    fund("Sachverhalt nach den Schlussanträgen GA Lagrange vom 25.6.1964", 110, 571, beim("rechn", "Verstaatlichungsgesetz")),
    fb(110, 640, 1040, 140, GELB, "vorl", [("Friedensgericht Mailand legt dem Gerichtshof vor", "ExtraBold", 31, INK),
                                          ("Art. 177 EWGV, heute Art. 267 AEUV", "ExtraBold", 31, INK)]),
    *wechsel([("Costa/ENEL 1964", "costa", GELB), ("1962: Verstaatlichung", "verst", None),
              ("1.925 Lire", "rechn", ROTHELL), ("Vorlage an den Gerichtshof", "vorl", GELB)], IX, 200, size=30),
    *icons([("tabler", "scale", "costa", GELB), ("tabler", "bolt", "verst", GELB), ("tabler", "file-invoice", "rechn", WEISS),
            ("tabler", "building-bank", "vorl", WEISS)], IX, 520, 150),
]))

# C2 Italien gegen den Gerichtshof ----------------------------------------------------------------------------------------
folie([("ital", "Costa/ENEL › Italien: das italienische Gesetz gilt"), ("ro", "Costa/ENEL › EuGH: eigene Rechtsordnung")],
      rechts_frei([
    *tafel("ital", "Italien gegen den Gerichtshof"),
    karte(110, 180, 1040, 230, beim("ital", "italienische"), fill=ROTHELL, rund=18, schatten=6, rand=4),
    z("Italienische Regierung: Das Gericht müsse", 140, 200, beim("ital", "italienische"), "Bold", 31, rechts=1140),
    z("das italienische Gesetz anwenden.", 140, 245, beim("ital", "müsse"), size=31, rechts=1140),
    z("Verfassungsgericht: Das jüngere Gesetz geht", 140, 305, "vg", "Bold", 31, rechts=1140),
    z("dem älteren Vertrag vor.", 140, 350, beim("vg", "jüngere"), size=31, rechts=1140),
    fund("Slg. 1964, 1253, 1269; Schlussanträge GA Lagrange", 110, 422, beim("vg", "jüngere")),
    karte(110, 490, 1040, 230, beim("ro", "Vertrag"), fill=GRUENHELL, rund=18, schatten=6, rand=4),
    nein(1100, 225, beim("ro", "anders"), gr=18),
    z("Gerichtshof: Der Vertrag hat eine eigene", 140, 510, beim("ro", "Vertrag"), "Bold", 31, rechts=1140),
    z("Rechtsordnung geschaffen, aufgenommen in die", 140, 555, beim("ro", "Rechtsordnung"), size=31, rechts=1140),
    z("Rechtsordnungen der Mitgliedstaaten,", 140, 600, beim("ro", "aufgenommen"), size=31, rechts=1140),
    z("von ihren Gerichten anzuwenden", 140, 645, beim("ro", "Gerichten"), size=31, rechts=1140),
    fund("Slg. 1964, 1253, 1269", 110, 732, beim("ro", "Gerichten")),
    *wechsel([("Regierung Italiens", "ital", ROTHELL), ("Verfassungsgericht Italiens", "vg", ROTHELL),
              ("Gerichtshof: eigene Rechtsordnung", "ro", GRUEN)], IX, 200, size=28),
    *icons([("tabler", "building-bank", "ital", WEISS), ("tabler", "scale", "vg", WEISS), ("tabler", "world", "ro", BLAU)],
           IX, 520, 150),
]))

# C3 Kernsatz (Zitatkarte, Slg. 1964, 1253, 1270; wortgleich in der Fußnote zum Gutachten der Erklärung Nr. 17) ------------
WC = [[("„… dass dem vom Vertrag geschaffenen, somit aus", 0)],
      [("einer ", 0), ("autonomen Rechtsquelle", "a"), (" fließenden Recht", 0)],
      [("wegen dieser seiner Eigenständigkeit ", 0), ("keine wie", "b")],
      [("immer gearteten innerstaatlichen Rechtsvorschriften", "b")],
      [("vorgehen können", "b"), (" …“", 0)]]
folie([("zitat", "Costa/ENEL › Der Kernsatz"), ("spaet", "Costa/ENEL › Vorrang auch vor späterem Recht")], rechts_frei([
    *tafel("zitat", "Der Kernsatz von Costa/ENEL"),
    *wortlaut(110, 180, 1040, 270, "zitat", WC, 32, {"a": beim("zitat", "autonomen"), "b": beim("zitat", "keine")},
              "EuGH, Rs. 6/64, Slg. 1964, 1253, 1270"),
    fb(110, 540, 1040, 140, GRUEN, "spaet", [("auch keine späteren einseitigen", "ExtraBold", 34, INK),
                                            ("Maßnahmen der Staaten", "ExtraBold", 34, INK)]),
    fund("Slg. 1964, 1253, 1269 f. und Tenor I („einseitige jüngere Maßnahmen“)", 110, 695, beim("spaet", "späteren")),
    *wechsel([("keine Vorschrift geht vor", "zitat", GELB), ("auch keine späteren Maßnahmen", "spaet", GRUEN)], IX, 200, size=28),
    *icons([("tabler", "arrow-big-up-lines", "zitat", GELB), ("tabler", "calendar-time", "spaet", WEISS)], IX, 520, 150),
]))

# D Simmenthal II und Fratelli Costanzo ------------------------------------------------------------------------------------
folie([("simm", "Simmenthal II · EuGH 1978"), ("jedes", "Simmenthal II › jedes Gericht lässt unangewendet"),
       ("behoerd", "Fratelli Costanzo › auch die Verwaltung")], rechts_frei([
    *tafel("simm", "Wer setzt den Vorrang durch?"),
    z("Simmenthal II, EuGH, Urteil vom 9.3.1978", 110, 185, beim("simm", "Simmenthal"), "Bold", 34),
    fund("Rs. 106/77, Slg. 1978, 629", 110, 235, beim("simm", "Simmenthal")),
    z("Gericht in Susa: Gebühren für Rindfleischeinfuhren", 110, 300, "susa", size=31),
    z("italienische Rspr.: erst Vorlage ans Verfassungsgericht", 110, 347, beim("susa", "Nach"), size=31),
    fund("Rn. 2/7", 110, 394, beim("susa", "Verfassungsgericht")),
    ok(135, 470, "jedes", gr=18),
    z("jedes Gericht lässt entgegenstehendes Recht", 175, 450, "jedes", "Bold", 32),
    z("unangewendet, auch späteres, aus eigener Befugnis", 175, 497, beim("jedes", "auch"), size=31),
    ok(135, 565, "warten", gr=18),
    z("kein Warten auf Gesetzgeber oder Verfassungsgericht", 175, 545, "warten", size=31),
    fund("Rn. 21/23, 24", 175, 592, beim("warten", "Verfassungsgericht")),
    fb(110, 650, 1040, 140, BLAUHELL, "behoerd", [("Fratelli Costanzo (1989): auch die Verwaltung,", "ExtraBold", 31, INK),
                                                 ("bis hin zur Gemeinde", "ExtraBold", 31, INK)]),
    fund("Rs. 103/88, Slg. 1989, 1839, Rn. 31, 33", 110, 805, beim("behoerd", "Verwaltung")),
    *wechsel([("Simmenthal II, 1978", "simm", GELB), ("Rindfleisch-Einfuhren", "susa", None), ("jedes Gericht", "jedes", GRUEN),
              ("auch die Verwaltung", "behoerd", BLAU)], IX, 200, size=30),
    *icons([("tabler", "scale", "simm", GELB), ("tabler", "meat", "susa", ROT), ("tabler", "gavel", "jedes", HOLZ),
            ("tabler", "building-community", "behoerd", WEISS)], IX, 520, 150),
]))

# E Anwendungsvorrang statt Geltungsvorrang -------------------------------------------------------------------------------
folie([("gueltig", "Anwendungsvorrang › Das Gesetz bleibt gültig"), ("gv", "Anwendungsvorrang › nicht Geltungsvorrang"),
       ("rest", "Anwendungsvorrang › ohne Kollision weiter angewendet")], rechts_frei([
    *tafel("gueltig", "Anwendungsvorrang"),
    z("Das nationale Gesetz bleibt gültig.", 110, 180, beim("gueltig", "Es"), "Bold", 34),
    z("EuGH: nicht inexistent, nur nicht angewendet", 110, 245, "inex", size=32),
    fund("verb. Rs. C-10/97 bis C-22/97, IN.CO.GE.'90, Rn. 21", 110, 292, beim("inex", "nicht")),
    z("BVerfG: Geltungsanspruch unberührt,", 110, 350, beim("bv335", "Anwendungsvorrang"), size=32),
    z("nur in der Anwendung zurückgedrängt", 110, 397, beim("bv335", "drängt"), size=32),
    fund("BVerfGE 123, 267 Rn. 335 (Lissabon)", 110, 444, beim("bv335", "drängt")),
    karte(110, 505, 500, 170, "art31", fill=LILAHELL, rund=18, schatten=6, rand=4),
    z("Art. 31 GG:", 135, 520, "art31", "Bold", 31, rechts=600),
    z("Bundesrecht bricht", 135, 565, beim("art31", "Bundesrecht"), size=31, rechts=600),
    z("Landesrecht", 135, 610, beim("art31", "Landesrecht"), size=31, rechts=600),
    karte(650, 505, 500, 170, "gv", fill=GRUENHELL, rund=18, schatten=6, rand=4),
    z("EU-Recht:", 675, 520, "gv", "Bold", 31, rechts=1140),
    z("Anwendungsvorrang,", 675, 565, beim("gv", "Anwendungsvorrang"), size=31, rechts=1140),
    z("nicht Geltungsvorrang", 675, 610, beim("gv", "Geltungsvorrang"), size=31, rechts=1140),
    fb(110, 715, 1040, 90, GELB, "rest", [("keine Kollision: Gesetz wird weiter angewendet", "ExtraBold", 31, INK)]),
    *paar("gueltig", [("denkt",), ("staunt", "inex"), ("ruhig", "rest")], [("ernst",), ("denkt", "bv335"), ("still", "rest")]),
]))

# F1 Rechtsgrundlage: Erklärung Nr. 17 (Wortlaut auszugsweise, ABl. C 202 vom 7.6.2016, S. 344) ----------------------------
W17 = [[("„Die Konferenz weist darauf hin, dass die Verträge und", 0)],
       [("das von der Union auf der Grundlage der Verträge", 0)],
       [("gesetzte Recht im Einklang mit der ", 0), ("ständigen", "a")],
       [("Rechtsprechung", "a"), (" des Gerichtshofs der Europäischen", 0)],
       [("Union … ", 0), ("Vorrang vor dem Recht der", "b")],
       [("Mitgliedstaaten", "b"), (" haben.“", 0)]]
folie([("grund", "Rechtsgrundlage › kein Vorrangartikel"), ("e17", "Rechtsgrundlage › Erklärung Nr. 17"),
       ("gut", "Rechtsgrundlage › Gutachten zur Erklärung Nr. 17")], rechts_frei([
    *tafel("grund", "Wo steht der Vorrang?"),
    nein(135, 205, beim("grund", "Einen"), gr=18),
    z("kein ausdrücklicher Vorrangartikel in den Verträgen", 175, 185, beim("grund", "Einen"), "Bold", 31),
    z("Erklärung Nr. 17 zur Schlussakte von Lissabon", 110, 250, "e17", "Bold", 32),
    *wortlaut(110, 305, 1040, 300, beim("e17", "Erklärung"), W17, 31,
              {"a": beim("e17b", "ständigen"), "b": beim("e17b", "Vorrang")}, "Erklärung Nr. 17, ABl. C 202 vom 7.6.2016, S. 344"),
    z("Gutachten: Bei Costa war der Vorrang im Vertrag", 110, 690, "gut", "Bold", 31),
    z("„nicht erwähnt. Dies ist auch heute noch der Fall.“", 110, 737, beim("gut", "nicht"), size=31),
    *paar("grund", [("denkt",), ("ruhig", "e17b")], [("ernst",), ("still", "gut")]),
]))

# F2 Art. 4 Abs. 3 EUV (Wortlaut UAbs. 2 und 3, ABl. C 202 vom 7.6.2016, S. 18) ---------------------------------------------
W43 = [[("„Die Mitgliedstaaten ", 0), ("ergreifen alle geeigneten", "a")],
       [("Maßnahmen", "a"), (" allgemeiner oder besonderer Art zur", 0)],
       [("Erfüllung der Verpflichtungen, die sich aus den", 0)],
       [("Verträgen oder den Handlungen der Organe der", 0)],
       [("Union ergeben. … Die Mitgliedstaaten … ", 0), ("unterlassen", "b")],
       [("alle Maßnahmen", "b"), (", die die Verwirklichung der Ziele", 0)],
       [("der Union gefährden könnten.“", 0)]]
folie([("a43", "Rechtsgrundlage › Art. 4 Abs. 3 EUV, loyale Zusammenarbeit"),
       ("ausdr", "Rechtsgrundlage › Nichtanwendung als Ausdruck der Loyalität")], rechts_frei([
    *tafel("a43", "Art. 4 Abs. 3 EUV: loyale Zusammenarbeit"),
    *wortlaut(110, 180, 1040, 345, "a43", W43, 31,
              {"a": beim("ergr", "ergreifen"), "b": beim("unterl", "unterlassen")}, "Art. 4 Abs. 3 UAbs. 2 und 3 EUV"),
    fb(110, 600, 1040, 140, GRUEN, "ausdr", [("Pflicht zur Nichtanwendung: Ausdruck", "ExtraBold", 32, INK),
                                            ("der loyalen Zusammenarbeit", "ExtraBold", 32, INK)]),
    fund("EuGH, Urt. v. 22.2.2022, C-430/21 (RS), Rn. 55", 110, 755, beim("ausdr", "Ausdruck")),
    *paar("a43", [("ruhig",), ("denkt", "ausdr")], [("still",), ("ernst", "ausdr")]),
]))

# G Grenzen aus deutscher Sicht --------------------------------------------------------------------------------------------
folie([("grenz", "Grenzen aus deutscher Sicht › Ultra-vires- und Identitätskontrolle"),
       ("nurbv", "Grenzen aus deutscher Sicht › nur das BVerfG stellt fest")], rechts_frei([
    *tafel("grenz", "Grenzen aus deutscher Sicht"),
    z("Vorrang nicht grenzenlos", 110, 185, beim("grenz", "Vorrang"), "Bold", 34),
    z("Das BVerfG behält sich vor:", 110, 255, beim("grenz", "Bundesverfassungsgericht"), size=32),
    z("· Ultra-vires-Kontrolle", 150, 315, beim("grenz", "Ultra-vires-Kontrolle"), "Bold", 32),
    z("· Identitätskontrolle", 150, 365, beim("grenz", "Identitätskontrolle"), "Bold", 32),
    fund("BVerfGE 123, 267 Rn. 240 (Lissabon)", 150, 415, beim("grenz", "Identitätskontrolle")),
    fb(110, 490, 1040, 140, GELB, "nurbv", [("Feststellen darf das nur das BVerfG,", "ExtraBold", 32, INK),
                                           ("nicht das Amt", "ExtraBold", 32, INK)]),
    fund("BVerfGE 123, 267 Rn. 241", 110, 645, beim("nurbv", "Bundesverfassungsgericht")),
    *paar("grenz", [("denkt",), ("ruhig", "nurbv")], [("denkt",), ("still", beim("nurbv", "nicht"))]),
]))

# H1 Lösung I: Art. 288 Abs. 2 AEUV (Wortlaut, ABl. C 202 vom 7.6.2016, S. 171) --------------------------------------------
W288 = [[("„Die Verordnung hat ", 0), ("allgemeine Geltung", "a"), (". Sie ist", 0)],
        [("in allen ihren Teilen ", 0), ("verbindlich", "b"), (" und ", 0), ("gilt", "c")],
        [("unmittelbar in jedem Mitgliedstaat.", "c"), ("“", 0)]]
folie([("zurueck", "Lösung · Hedwig und Herr Lammert"), ("p288", "Lösung › I. unmittelbare Geltung, Art. 288 Abs. 2 AEUV")],
      rechts_frei([
    *tafel("zurueck", "Lösung: Hedwig und Herr Lammert"),
    z("I. Die Verordnung gilt unmittelbar", 110, 185, "p288", "Bold", 34),
    *wortlaut(110, 245, 1040, 180, beim("p288", "Artikel"), W288, 32,
              {"a": beim("p288", "allgemeine"), "b": beim("p288", "verbindlich"), "c": beim("p288", "gilt", nr=2)},
              "Art. 288 Abs. 2 AEUV"),
    ok(135, 520, "quelle", gr=18),
    z("kein Umsetzungsgesetz nötig", 175, 500, "quelle", "Bold", 32),
    ok(135, 580, beim("quelle", "Hedwig"), gr=18),
    z("unmittelbar Rechte, auch für Hedwig", 175, 560, beim("quelle", "Hedwig"), "Bold", 32),
    fund("vgl. Simmenthal, Rn. 14/16 (unmittelbare Quelle von Rechten und Pflichten)", 175, 607, beim("quelle", "Rechte")),
    *paar("zurueck", [("ruhig",), ("froh", "quelle")], [("ernst",), ("denkt", "quelle")]),
]))

# H2 Lösung II und III -------------------------------------------------------------------------------------------------------
folie([("kol", "Lösung › II. Kollision"), ("folge", "Lösung › III. Rechtsfolge: Anwendungsvorrang")], rechts_frei([
    *tafel("kol", "Lösung: Kollision und Rechtsfolge"),
    z("II. Kollision", 110, 185, "kol", "Bold", 34),
    z("Verordnung erlaubt, Gesetz verbietet", 150, 240, beim("kol", "Verordnung"), size=32),
    nein(175, 315, beim("kol", "unionsrechtskonform"), gr=18),
    z("unionsrechtskonforme Auslegung: nicht möglich", 215, 295, beim("kol", "unionsrechtskonform"), size=32),
    z("III. Rechtsfolge: Anwendungsvorrang", 110, 380, "folge", "Bold", 34),
    ok(175, 455, beim("folge", "Herr"), gr=18),
    z("Herr Lammert lässt das Verbot unangewendet", 215, 435, beim("folge", "Herr"), size=32),
    ok(175, 515, beim("folge", "Verordnung"), gr=18),
    z("und wendet die Verordnung an", 215, 495, beim("folge", "Verordnung"), size=32),
    fund("Costanzo, Rn. 31; EuGH, C-378/17, Rn. 38", 215, 542, beim("folge", "Verordnung")),
    fb(110, 610, 1040, 90, GRUEN, "bleibt", [("Das Gesetz bleibt dabei gültig.", "ExtraBold", 34, INK)]),
    *paar("kol", [("denkt",), ("froh", "folge")], [("denkt",), ("staunt", "folge"), ("still", "bleibt")]),
]))

# H3 Ergebnis: zurück in der Manufaktur (dieselbe Szene wie A, Geschichte kehrt dorthin zurück) -----------------------------
folie([("erg", "Ergebnis · Das Amt hält sich an die EU-Verordnung")], [
    *manufaktur("erg", "erg", False),
    ficon("tabler", "cube", 970, 744, 50, "erg", fuell=WEISS),
    *stufen([("HE_froh_r", "erg")], HEX, BODEN, GH),
    namensschild("Hedwig", HEX, BODEN, "erg", FARBE["HE"], d=0.2),
    *stufen([("LA_ruhig", "erg"), ("LA_freundlich", beim("erg", "Es"))], LAX, BODEN, GH),
    namensschild("Herr Lammert", LAX, BODEN, "erg", FARBE["LA"], d=0.3),
    ficon("tabler", "file-certificate", 1000, 330, 110, beim("erg", "EU-Verordnung"), fuell=BLAU),
    ok(1090, 250, beim("erg", "EU-Verordnung"), gr=26),
    pl("Das Amt hält sich an die EU-Verordnung.", 1000, 170, beim("erg", "Amt"), fill=GRUEN, size=34, anker="m"),
    pl("kein Verkaufsverbot für Hedwig", 1000, 420, beim("erg", "Es"), fill=WEISS, size=30, anker="m"),
])

# I Klausurtipp (Lexi) -----------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · erst unionsrechtskonform auslegen"), ("tipp3", "Klausurtipp · unanwendbar, nicht nichtig")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Bevor du ein Gesetz unangewendet lässt:", 200, 200, "tipp", "Bold", 34),
    z("unionsrechtskonform auslegen", 200, 250, beim("tipp", "unionsrechtskonform"), size=34),
    fund("vgl. EuGH, C-430/21 (RS), Rn. 53", 200, 297, beim("tipp", "auszulegen")),
    z("Erst wenn das nicht geht:", 200, 380, "tipp2", "Bold", 34),
    z("Anwendungsvorrang", 200, 430, beim("tipp2", "Anwendungsvorrang"), size=34),
    nein(175, 535, "tipp3", gr=18),
    z("nie „das Gesetz ist nichtig“", 215, 515, "tipp3", "Bold", 34),
    ok(175, 600, beim("tipp3", "Es"), gr=18),
    z("sondern: unanwendbar", 215, 580, beim("tipp3", "Es"), "Bold", 34),
    *redet("LX_warnt", LXX, BR, FR + 60, "tipp", "sch"),
    namensschild("Lexi", LXX, BR, "tipp", GELB, d=0.2),
])

# J Klausurschema ----------------------------------------------------------------------------------------------------------
K1, K2 = 150, 230
PS_ = "Klausurschema"
folie([("sch", PS_), ("k1", f"{PS_} › I. unmittelbar anwendbares Unionsrecht"), ("k2", f"{PS_} › II. Kollision"),
       ("k3", f"{PS_} › III. Rechtsfolge: Anwendungsvorrang"), ("k4", f"{PS_} › IV. Grenzen")], [
    karte(60, 50, 1800, 920, "sch"),
    titel("Klausurschema: Anwendungsvorrang", 110, 90, "sch", 50),
    z("I. Unmittelbar anwendbares Unionsrecht, etwa eine Verordnung (Art. 288 Abs. 2 AEUV)", K1, 190, "k1", "Bold", 34,
      rechts=1820),
    z("II. Kollision mit nationalem Recht", K1, 285, "k2", "Bold", 34, rechts=1820),
    z("erst nach dem Versuch unionsrechtskonformer Auslegung", K2, 340, "k2a", size=32, rechts=1820),
    z("III. Rechtsfolge: Anwendungsvorrang", K1, 435, "k3", "Bold", 34, rechts=1820),
    z("Gerichte und Behörden lassen das nationale Recht unangewendet", K2, 490, "k3a", size=32, rechts=1820),
    z("das Gesetz bleibt gültig", K2, 545, "k3b", size=32, rechts=1820),
    z("IV. Grenzen: Ultra-vires- und Identitätskontrolle,", K1, 640, "k4", "Bold", 34, rechts=1820),
    z("nur durch das BVerfG", K2, 695, beim("k4", "nur"), size=32, rechts=1820),
])

# K Merksatz (Lexi) --------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("EU-Recht bricht deutsches Recht", 0)], [("nicht, es ", 0), ("verdrängt", "a"), (" es nur", 0)],
                 [("in der Anwendung", "a"), (".", 0)]], 750, 300, 44, "merke", {"a": beim("merke", "verdrängt")}),
    *markertext([[("Daran sind nicht nur Gerichte", 0)], [("gebunden, sondern auch ", 0), ("jedes Amt", "b"), (".", 0)]],
                750, 560, 42, "m2", {"b": beim("m2", "jedes")}),
    *redet("LX_erklaert", 1680, 960, 690, "merke", lexi_bis_ende("merke")),
    namensschild("Lexi", 1680, 960, "merke", GELB, d=0.2),
])
