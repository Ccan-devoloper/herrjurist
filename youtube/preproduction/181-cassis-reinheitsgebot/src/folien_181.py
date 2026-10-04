"""Folge 181 · Cassis de Dijon: Warum fremdes Bier trotz Reinheitsgebot rein darf – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A Fall im Getränkehandel (Herr Brodersen, Frau Timmermann), B Sachverhalt, C Einordnung (Verweis
auf das Prüfschema aus Folge 176), D1 der echte Fall Cassis de Dijon (ohne Figuren), D2 unterschiedslos anwendbar, D3 Cassis-Formel
(Zitatkarte Rn. 8), D4 Deutschlands Argumente und Etikett, D5 gegenseitige Anerkennung (Zitatkarte Rn. 14), E1 der echte Fall
Reinheitsgebot (ohne Figuren), E2 Bezeichnungsverbot, E3 Etikett und Verstoß, E4a/E4b Zusatzstoffverbot mit Art. 36 AEUV
(Wortlaut, Auszug), E5 Ergebnis und heutige Rechtslage (§ 1 Abs. 2 BierV als Wortlautkarte), F1 Lösung, F2 zurück im
Getränkehandel, G Klausurtipp (Lexi), H Schema der Rechtfertigung, I Merksatz (Lexi).
Bier und Likör nur als neutrale Flaschen-, Kisten- und Fass-Icons ohne Marke; kein Trinken, keine Gläser, keine Flaggen.
Rewe-Zentral nur als Name auf der Tafel. Geräusche nur bei sichtbarer Handlung: Kiste wird abgestellt, Tür (Frau Timmermann
kommt); Freesound CC0, ../geraeusche_herkunft.json.
Hilfsfunktionen (glyphen, z, pl, tafel, fb, wl_links, zitatkarte, redet mit hörbarem Wortende …) als eigene Kopie aus Folge 176
(gemeinsame Dateien unverändert); neu: laden(), belgierkiste(), kasten(). Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
from engine import El, F

bausteine.FIGORDNER = "op_181/"
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
        if n.startswith(("bild:", "ficon:")) or "/op_181/" in n:
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
FARBE = {"BD": LILA, "TM": BLAU}
NAME = {"BD": "Herr Brodersen", "TM": "Frau Timmermann"}


def kette(prefix, x, folge, bis_=None, d=0.0, hoehe=FR, unten=BR):
    """Eine Figur mit Mimikfolge [(Name, Cue), …] im Zwiebelschalenprinzip (erster Auftritt pop, danach harte Schnitte)."""
    els = []
    for i, (n, c) in enumerate(folge):
        b = folge[i + 1][1] if i + 1 < len(folge) else bis_
        els.append(peep_voll(prefix + n, x, unten, hoehe, c, anim=("pop" if i == 0 else "cut"), d=(d if i == 0 else 0.0), bis=b))
    return els


def paar(cue, f1, f2):
    """Herr Brodersen (links) und Frau Timmermann (rechts) neben der Tafel, beide blicken zur Tafel; Namensschilder ab Beginn."""
    els = kette("BD_", X1, [(f1[0][0], cue)] + list(f1[1:])) + kette("TM_", X2, [(f2[0][0], cue)] + list(f2[1:]), d=0.2)
    return els + [namensschild(NAME["BD"], X1, BR, cue, FARBE["BD"], d=0.2),
                  namensschild(NAME["TM"], X2, BR, cue, FARBE["TM"], d=0.3)]


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




# --- Eigene Ergänzungen Folge 181 ---------------------------------------------------------------------------------------
AMBER = (214, 150, 80, 255)                        # Bierflaschen (neutral, ohne Etikett/Marke)
LIKOER = (150, 110, 190, 255)                      # Likörflasche (neutral)
KARTON = (222, 184, 135, 255)
HC = "fluent-emoji-high-contrast"


def okz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Haken davor (zur gesprochenen Bejahung)."""
    return [ok(x - 45, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]


def neinz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Kreuz davor (zur gesprochenen Verneinung)."""
    return [nein(x - 45, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]


def kasten(x, y, w, h, cue, fill):
    return karte(x, y, w, h, cue, fill=fill, rund=18, schatten=6, rand=4)


# A Fall: Getränkehandel ------------------------------------------------------------------------------------------------
BODEN, GH = 900, 520
BDX, TMX = 380, 1580
BDa = ("BD_redet_r", BDX, BODEN, GH)
TMa = ("TM_redet", TMX, BODEN, GH)
TMb = ("TM_einsicht", TMX, BODEN, GH)
RX0, RX1 = 700, 1290                               # Regal
ZB = 995                                           # Mitte des Pillenbands über dem Regal


def laden(cue):
    """Bodenlinie, Regal aus Grundformen mit neutralen Flaschen (Tabler bottle) und Kisten (Tabler package), ein Fass
    (Tabler barrel); keine Etiketten, keine Marken, keine Gläser."""
    els = [linienzug([(60, BODEN), (1860, BODEN)], cue, breite=7, farbe=INK)]
    for xx in (RX0, RX1):
        els.append(linienzug([(xx, 470), (xx, BODEN)], cue, breite=8, farbe=INK))
    for yy in (620, 770):
        els.append(linienzug([(RX0 - 10, yy), (RX1 + 10, yy)], cue, breite=8, farbe=INK))
    for xx in range(760, 1250, 70):
        els.append(ficon("tabler", "bottle", xx, 616, 58, cue, fuell=AMBER, anim="cut"))
    for xx in (820, 995, 1170):
        els.append(ficon("tabler", "package", xx, 766, 130, cue, fuell=KARTON, anim="cut"))
    els.append(ficon("tabler", "barrel", 1050, BODEN - 4, 150, cue, fuell=HOLZ, anim="cut"))
    els.append(ficon("tabler", "barrel", 140, BODEN - 4, 130, cue, fuell=HOLZ, anim="cut"))
    return els


def belgierkiste(cue, bis=None, anim="pop"):
    """Die neue Kiste mit dem Bier aus Belgien (neutral, ohne Marke) vor dem Regal."""
    k = ficon("tabler", "package", 585, BODEN - 4, 150, cue, fuell=GELB, anim=anim, bis=bis)
    return [k, *[ficon("tabler", "bottle", xx, k.y + 8, 44, cue, fuell=AMBER, anim=anim, bis=bis) for xx in (550, 585, 620)]]


folie([("fall", "Fall · Herr Brodersen und das Bier aus Belgien"), ("timm", "Fall · Frau Timmermann prüft"),
       ("frage", "Fall · Die Frage")], [
    *laden("fall"),
    pl("Getränkehandel", 70, 40, "fall", fill=GELB, size=34, bis="timm"),
    *stufen([("BD_ruhig_r", "fall"), ("BD_froh_r", "bel"), ("BD_entschlossen_r", "reis"), ("BD_ruhig_r", "timm"),
             ("BD_sorge_r", "t1"), ("BD_redet_r", "b1"), ("BD_denkt_r", "frage")], BDX, BODEN, GH,
            rede={"BD_redet_r": 1}, erst="cut"),
    namensschild(NAME["BD"], BDX, BODEN, "fall", FARBE["BD"]),
    szene(belgierkiste("bel")[0], "181kiste*", 1.0, versatz=0.05), *belgierkiste("bel")[1:],
    *wechsel([("Neu im Sortiment: Bier aus Belgien", "bel", BLAUHELL),
              ("gebraut aus Gerstenmalz, Reis und Mais", "reis", HELL)], ZB, 135, size=30, ende="t1"),
    *icons([("tabler", "wheat", "reis", GELB)], ZB - 170, 430, 110, ende="t1"),
    ficon(HC, "sheaf-of-rice", ZB, 430, 110, beim("reis", "Reis"), fuell=GRUENHELL, bis="t1"),
    ficon(HC, "ear-of-corn", ZB + 170, 430, 110, beim("reis", "Mais"), fuell=GELB, bis="t1"),
    pl("Gerstenmalz", ZB - 170, 455, "reis", fill=WEISS, size=26, anker="m", bis="t1"),
    pl("Reis", ZB, 455, beim("reis", "Reis"), fill=WEISS, size=26, anker="m", bis="t1"),
    pl("Mais", ZB + 170, 455, beim("reis", "Mais"), fill=WEISS, size=26, anker="m", bis="t1"),
    # Frau Timmermann kommt durch die Tür
    szene(ficon("tabler", "door", 1830, BODEN, 90, "timm", fuell=HOLZ), "181tuer*", 1.0, versatz=0.05),
    *stufen([("TM_ruhig", "timm"), ("TM_redet", "t1"), ("TM_ernst", "b1"), ("TM_denkt", "frage")],
            TMX, BODEN, GH, rede={"TM_redet": 1}),
    namensschild(NAME["TM"], TMX, BODEN, "timm", FARBE["TM"], d=0.2),
    pl("Lebensmittelüberwachung", ZB, 210, beim("timm", "Lebensmittelüberwachung"), fill=WEISS, size=30, anker="m", bis="t1"),
    blase("sprech", 860, 250, "t1", 1050, 240, inhalt=["Mit Reis und Mais gebraut?", "Nach dem Reinheitsgebot ist das",
          "kein Bier. So dürfen Sie es", "nicht verkaufen."], textsize=31, figur=TMa, bis="b1"),
    blase("sprech", 860, 230, "b1", 960, 235, inhalt=["In Belgien ist das", "ganz normales Bier. Warum",
          "soll es hier anders heißen?"], textsize=32, figur=BDa, bis="frage"),
    pl("Darf ein Staat den Namen „Bier“ für Getränke", ZB, 150, "frage", fill=PINK, size=32, anker="m"),
    pl("nach seinen eigenen Regeln reservieren?", ZB, 222, "frage", fill=PINK, size=32, anker="m"),
])

# B Sachverhalt -------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    glyphen("Herr Brodersen betreibt einen Getränkehandel. Neu im Sortiment hat er ein Bier aus Belgien, gebraut aus "
            "Gerstenmalz, Reis und Mais. In Belgien wird es rechtmäßig als Bier verkauft."),
    glyphen("Frau Timmermann von der Lebensmittelüberwachung meint, nach dem Reinheitsgebot sei das kein Bier. Unter "
            "dieser Bezeichnung dürfe er es nicht verkaufen."),
], "Darf ein Staat den Namen „Bier“ nach eigenen Brauregeln reservieren?")

# C Einordnung: Verweis auf Folge 176 (Prüfschema Art. 34 AEUV) --------------------------------------------------------------
folie([("verweis", "Einordnung › Prüfschema Art. 34 AEUV: Video zu Dassonville"),
       ("recht", "Einordnung › heute: die Rechtfertigung")], rechts_frei([
    *tafel("verweis", "Heute: die Rechtfertigung"),
    z("Prüfschema Art. 34 AEUV:", 110, 185, "verweis", "Bold", 36),
    z("siehe Video „Warenverkehrsfreiheit: Dassonville“", 110, 240, beim("verweis", "Video"), size=34),
    fb(110, 340, 1040, 90, GELB, "recht", [("Schwerpunkt: Rechtfertigung", "ExtraBold", 36, INK)]),
    z("an zwei Klassikern:", 110, 470, beim("recht", "zwei"), "Bold", 34),
    fb(110, 540, 505, 150, LILAHELL, "zwei", [("Cassis de Dijon", "ExtraBold", 34, INK), ("EuGH 1979", "Regular", 30, INK)]),
    fb(645, 540, 505, 150, HELL, beim("zwei", "Reinheitsgebot"), [("Reinheitsgebot", "ExtraBold", 34, INK),
                                                                   ("EuGH 1987", "Regular", 30, INK)]),
    *einzeln("BD", "verweis", [("ruhig",), ("denkt", "recht"), ("froh", beim("zwei", "Reinheitsgebot"))]),
]))

# D1 Der echte Fall Cassis de Dijon (Rs. 120/78, Rn. 2, 3) – ohne Figuren ------------------------------------------------------
PC = "Cassis de Dijon, EuGH 1979"
folie([("c79", f"{PC} · Der Fall"), ("monop", f"{PC} · nicht verkehrsfähig")], rechts_frei([
    *tafel("c79", "Der Fall: Cassis de Dijon"),
    z("EuGH, 20.2.1979", 110, 180, "c79", "Bold", 36),
    z("Rewe-Zentral will einen Fruchtsaftlikör aus", 110, 250, "rewe", size=34),
    z("Frankreich einführen: „Cassis de Dijon“", 110, 300, beim("rewe", "Frankreich"), size=34),
    z("Bundesmonopolverwaltung für Branntwein:", 110, 380, "monop", "Bold", 34),
    z("in Deutschland nicht verkehrsfähig", 110, 430, beim("monop", "in"), size=34),
    kasten(110, 510, 1040, 210, "mind", GELB if False else HELL),
    z("Fruchtsaftliköre: mindestens 25 % Weingeist", 140, 530, "mind", "Bold", 34, rechts=1140),
    *neinz("Cassis: nur 15 bis 20 %", 600, "cgehalt", "Bold", 34, x=200),
    fund("EuGH, Urt. v. 20.2.1979 – Rs. 120/78 (Rewe-Zentral), Slg. 1979, 649, Rn. 2, 3", 110, 745, "c79"),
    *icons([("tabler", "bottle", "rewe", LIKOER), ("tabler", "truck-delivery", beim("rewe", "Frankreich"), GELB),
            ("tabler", "building-bank", "monop", BLAUHELL), ("tabler", "ban", beim("monop", "nicht"), ROTHELL),
            ("tabler", "bottle", "mind", LIKOER)], IX, 600, 200),
    *wechsel([("Rewe-Zentral (Handel)", "rewe", WEISS), ("Einfuhr aus Frankreich", beim("rewe", "Frankreich"), BLAUHELL),
              ("Bundesmonopolverwaltung", "monop", BLAUHELL), ("nicht verkehrsfähig", beim("monop", "nicht"), ROTHELL),
              ("mindestens 25 %", "mind", HELL), ("Cassis: 15 bis 20 %", "cgehalt", ROTHELL)], IX, 680, size=30),
]))

# D2 Unterschiedslos anwendbar, Maßnahme gleicher Wirkung (Rn. 3, 7, 14, 15) ---------------------------------------------------
folie([("unter", f"{PC} › unterschiedslos anwendbare Maßnahme"), ("behind", f"{PC} › Maßnahme gleicher Wirkung")],
      rechts_frei([
    *tafel("unter", "Unterschiedslos anwendbar"),
    z("Mindestgehalt gilt für alle Fruchtsaftliköre:", 110, 185, "unter", "Bold", 34),
    *okz("aus Deutschland", 255, beim("unter", "Deutschland"), size=34),
    *okz("aus dem Ausland", 315, beim("unter", "Ausland"), size=34),
    fb(110, 400, 1040, 90, GRUENHELL, beim("unter", "unterschiedslos"),
       [("unterschiedslos anwendbare Maßnahme", "ExtraBold", 34, INK)]),
    z("trotzdem: eingeführte Liköre vom Markt ferngehalten", 110, 530, "behind", size=34),
    fb(110, 600, 1040, 90, LILA, beim("behind", "eine"), [("Maßnahme gleicher Wirkung", "ExtraBold", 34, INK)]),
    fund("Rs. 120/78, Rn. 3, 14, 15; Art. 30 EWG-Vertrag, heute Art. 34 AEUV", 110, 710, beim("behind", "eine")),
    *paar("unter", [("ruhig",), ("denkt", beim("unter", "unterschiedslos")), ("staunt", "behind")],
          [("ruhig",), ("ernst", beim("unter", "unterschiedslos")), ("denkt", "behind")]),
]))

# D3 Die Cassis-Formel (Rn. 8) -----------------------------------------------------------------------------------------------
WC = [[("„", 0), ("Hemmnisse für den Binnenhandel der Gemeinschaft", "a"), (", die sich", 0)],
      [("aus den Unterschieden der nationalen Regelungen über die", 0)],
      [("Vermarktung dieser Erzeugnisse ergeben, ", 0), ("müssen hingenommen", "b")],
      [("werden", "b"), (", soweit diese Bestimmungen ", 0), ("notwendig", "c"), (" sind, um", 0)],
      [("zwingenden Erfordernissen", "d"), (" gerecht zu werden, insbesondere den", 0)],
      [("Erfordernissen einer ", 0), ("wirksamen steuerlichen Kontrolle", "e"), (", des", 0)],
      [("Schutzes der öffentlichen Gesundheit", "f"), (", der ", 0), ("Lauterkeit des", "g")],
      [("Handelsverkehrs", "g"), (" und des ", 0), ("Verbraucherschutzes", "h"), (".“", 0)]]
_kc, _yc = zitatkarte(WC, 110, 240, 31, "formel", {"a": beim("formel", "Hemmnisse"), "b": beim("formel", "müssen"),
                                                  "c": beim("formel", "notwendig"), "d": beim("formel", "zwingenden"),
                                                  "e": beim("vier", "wirksamen"), "f": beim("vier", "Schutzes"),
                                                  "g": beim("vier", "Lauterkeit"), "h": beim("vier", "Verbraucherschutzes")})
folie([("formel", f"{PC} › zwingende Erfordernisse, Rn. 8"), ("neben", f"{PC} › neben Art. 36 AEUV")], rechts_frei([
    *tafel("formel", "Zwingende Erfordernisse"),
    z("Der Gerichtshof, Rn. 8:", 110, 180, "formel", "Bold", 36),
    *_kc,
    fund("EuGH, Rs. 120/78 (Cassis de Dijon), Slg. 1979, 649, Rn. 8", 110, int(_yc + 12), "formel"),
    fb(110, int(_yc + 75), 1040, 90, GELB, "neben", [("neben den Gründen aus Art. 36 AEUV", "ExtraBold", 34, INK)]),
    fund("Rs. 113/80 (Kommission/Irland), Rn. 8–10; VO (EU) 2019/515, Erwägungsgrund 4", 110, int(_yc + 180), "neben"),
    *einzeln("TM", "formel", [("ruhig",), ("denkt", "vier"), ("staunt", "neben")]),
    *wechsel([("zwingende Erfordernisse", beim("formel", "zwingenden"), HELL), ("neben Art. 36 AEUV", "neben", GELB)],
             XE, 250, size=30),
]))

# D4 Deutschlands Argumente, Etikett als milderes Mittel (Rn. 9–13) ------------------------------------------------------------
folie([("gesund", f"{PC} › Gesundheit?"), ("lauter", f"{PC} › unlauterer Wettbewerb?"),
       ("milder", f"{PC} › Etikett als milderes Mittel")], rechts_frei([
    *tafel("gesund", "Deutschlands Argumente"),
    z("1. Gesundheit", 110, 185, "gesund", "Bold", 36),
    *neinz("nicht stichhaltig: sehr viele Getränke mit", 250, "stich", size=34),
    z("geringem oder mittlerem Alkoholgehalt", 185, 300, beim("stich", "sehr"), size=34),
    z("2. Schutz vor unlauterem Wettbewerb", 110, 390, "lauter", "Bold", 36),
    *neinz("trägt nicht: es genügt, Herkunft und Alkohol-", 455, "etik1", size=34),
    z("gehalt auf der Verpackung vorzuschreiben", 185, 505, beim("etik1", "Herkunft"), size=34),
    fb(110, 590, 1040, 90, GRUENHELL, "milder", [("Etikett: das mildere Mittel", "ExtraBold", 34, INK)]),
    fund("Rs. 120/78, Rn. 9–13", 110, 700, "milder"),
    *icons([("tabler", "activity-heartbeat", "gesund", ROTHELL), ("tabler", "scale", "lauter", GELB),
            ("tabler", "label", "etik1", HELL), ("tabler", "bottle", "milder", LIKOER)], IX, 560, 190),
    *wechsel([("Gesundheit?", "gesund", ROTHELL), ("nicht stichhaltig", "stich", ROTHELL),
              ("unlauterer Wettbewerb?", "lauter", GELB), ("Herkunft · Alkoholgehalt", "etik1", HELL),
              ("Etikett: milderes Mittel", "milder", GRUENHELL)], IX, 640, size=30),
]))

# D5 Gegenseitige Anerkennung (Rn. 14; VO (EU) 2019/515, ErwG 4) -------------------------------------------------------------
WA = [[("„Es gibt somit keinen stichhaltigen Grund dafür, zu verhindern,", 0)],
      [("dass in einem Mitgliedstaat ", 0), ("rechtmäßig hergestellte", "a"), (" und", 0)],
      [("in den Verkehr gebrachte", "b"), (" alkoholische Getränke in die anderen", 0)],
      [("Mitgliedstaaten ", 0), ("eingeführt werden", "c"), (" …“", 0)]]
_ka, _ya = zitatkarte(WA, 110, 240, 31, "anerk", {"a": beim("anerk", "rechtmäßig"), "b": beim("anerk", "in", 2),
                                                 "c": beim("anerk", "eingeführt")})
folie([("anerk", f"{PC} › gegenseitige Anerkennung")], rechts_frei([
    *tafel("anerk", "Gegenseitige Anerkennung"),
    z("Ergebnis des Gerichtshofs", 110, 180, "anerk", "Bold", 36),
    *_ka,
    fund("EuGH, Rs. 120/78, Rn. 14", 110, int(_ya + 12), "anerk"),
    fb(110, int(_ya + 80), 1040, 130, LILAHELL, "grundsatz", [("heute: Grundsatz der", "ExtraBold", 34, INK),
                                                              ("gegenseitigen Anerkennung", "ExtraBold", 34, INK)]),
    fund("VO (EU) 2019/515, Erwägungsgrund 4", 110, int(_ya + 225), "grundsatz"),
    *paar("anerk", [("ruhig",), ("froh", beim("anerk", "eingeführt")), ("entschlossen", "grundsatz")],
          [("ruhig",), ("denkt", beim("anerk", "eingeführt")), ("still", "grundsatz")]),
]))

# E1 Der echte Fall Reinheitsgebot (Rs. 178/84, Rn. 1, 5–7, 12, 24) – ohne Figuren ---------------------------------------------
PR = "Reinheitsgebot, EuGH 1987"
folie([("r87", f"{PR} · Der Fall"), ("par10", f"{PR} · § 10 Biersteuergesetz a. F."),
       ("nurde", f"{PR} · Brauvorschrift nur für Brauereien in Deutschland")], rechts_frei([
    *tafel("r87", "Der Fall: Reinheitsgebot"),
    z("EuGH, 12.3.1987: Kommission gegen Deutschland", 110, 180, "klage", "Bold", 34),
    z("Vertragsverletzungsverfahren", 110, 232, beim("klage", "Vertragsverletzung"), size=32),
    z("§ 10 BierStG a. F.: „Bier“ nur nach dem Reinheitsgebot", 110, 300, "par10", "Bold", 33),
    z("untergärig: nur Gerstenmalz, Hopfen, Hefe, Wasser", 140, 360, "zutat", size=33),
    *neinz("Reis und Mais: kein Getreide", 418, "kein", size=33, x=185),
    z("dazu: absolutes Verbot von Zusatzstoffen", 140, 478, "zusatz", size=33),
    kasten(110, 560, 1040, 150, "nurde", GRAU),
    z("Brauvorschrift (§ 9) nur für Brauereien in", 140, 580, "nurde", "Bold", 33, rechts=1140),
    z("Deutschland: keine Maßnahme gleicher Wirkung", 140, 630, beim("nurde", "keine"), size=33, rechts=1140),
    fund("EuGH, Urt. v. 12.3.1987 – Rs. 178/84, Slg. 1987, 1227, Rn. 1, 5–7, 12, 24", 110, 735, "r87"),
    pl("Reinheitsgebot", IX, 250, "r87", fill=HELL, size=32, anker="m"),
    *icons([("tabler", "barrel", "r87", HOLZ), ("tabler", "gavel", "klage", BLAUHELL), ("tabler", "wheat", "zutat", GELB),
            (HC, "sheaf-of-rice", "kein", ROTHELL), ("tabler", "flask", "zusatz", ROTHELL),
            ("tabler", "building-factory-2", "nurde", GRAU)], IX, 600, 200),
    *wechsel([("Klage der Kommission", "klage", BLAUHELL), ("Gerstenmalz, Hopfen, Hefe, Wasser", "zutat", HELL),
              ("Reis, Mais: verboten", "kein", ROTHELL), ("keine Zusatzstoffe", "zusatz", ROTHELL),
              ("nur Brauereien im Inland", "nurde", GRAU)], IX, 680, size=28),
]))

# E2 1. Bezeichnungsverbot (Rn. 26, 29–34) -----------------------------------------------------------------------------------
P1 = f"{PR} › 1. Bezeichnungsverbot"
folie([("name", P1), ("vschutz", f"{P1} › Verbraucherschutz?")], rechts_frei([
    *tafel("name", "1. Der Name „Bier“"),
    *okz("Bezeichnungsverbot kann die Einfuhr behindern", 185, "hemm", "Bold", 34),
    z("Deutschland: Verbraucherschutz", 110, 260, "vschutz", "Bold", 34),
    z("Gerichtshof: Vorstellungen der Verbraucher können", 110, 330, "wandel", size=34),
    z("sich fortentwickeln", 110, 380, beim("wandel", "Vorstellungen"), size=34),
    kasten(110, 450, 1040, 150, "zement", ZITAT),
    z("Recht eines Mitgliedstaats darf „nicht dazu dienen,", 140, 468, "zement", size=33, rechts=1140),
    z("die gegebenen Verbrauchsgewohnheiten zu zementieren“", 140, 520, beim("zement", "gegebenen"), size=33, rechts=1140),
    *okz("„Bier“ in anderen Mitgliedstaaten: Gattungs-", 630, "gattung", size=34),
    z("bezeichnung, auch mit Reis oder Mais", 185, 680, beim("gattung", "Gattungsbezeichnung"), size=34),
    fund("Rs. 178/84, Rn. 26, 29–34", 110, 750, "gattung"),
    *einzeln("TM", "name", [("ruhig",), ("ernst", "vschutz"), ("denkt", "wandel"), ("still", "zement"),
                            ("staunt", "gattung")]),
    *wechsel([("Name „Bier“", "name", HELL), ("Verbraucherschutz?", "vschutz", GELB),
              ("Gattungsbezeichnung", "gattung", GRUENHELL)], XE, 250, size=30),
]))

# E3 Etikett, Verstoß (Rn. 35, 37) --------------------------------------------------------------------------------------------
folie([("etik2", f"{P1} › Etikett als milderes Mittel"), ("v1", f"{P1} › Verstoß")], rechts_frei([
    *tafel("etik2", "Etikett statt Verbot"),
    fb(110, 185, 1040, 90, GRUENHELL, "etik2", [("milder: Angabe der verwendeten Grundstoffe", "ExtraBold", 33, INK)]),
    *okz("Wahl in Kenntnis aller Umstände", 320, beim("etik2", "Wahl"), size=34),
    *neinz("aber: kein negatives Bild von anders gebrautem Bier", 395, "negativ", size=33),
    fb(110, 490, 1040, 90, ROTHELL, "v1", [("Bezeichnungsverbot: Verstoß", "ExtraBold", 34, INK)]),
    fund("Rs. 178/84, Rn. 35, 37 (Art. 30 EWG-Vertrag, heute Art. 34 AEUV)", 110, 600, "v1"),
    *paar("etik2", [("ruhig",), ("froh", beim("etik2", "Wahl")), ("entschlossen", "v1")],
          [("ruhig",), ("denkt", "negativ"), ("still", "v1")]),
    ficon("tabler", "label", (X1 + X2) // 2, 330, 150, "etik2", fuell=HELL),
    pl("Gerstenmalz · Reis · Mais", (X1 + X2) // 2, 350, beim("etik2", "Grundstoffe"), fill=WEISS, size=28, anker="m"),
]))

# E4a 2. Zusatzstoffverbot: Art. 36 AEUV (Wortlaut, Auszug) und Zulassung (Rn. 40, 42, 44) ------------------------------------
P2 = f"{PR} › 2. Zusatzstoffverbot"
W36 = [[("„Die Bestimmungen der Artikel 34 und 35 stehen Einfuhr-, Ausfuhr-", 0)],
       [("und Durchfuhrverboten oder -beschränkungen nicht entgegen, die", 0)],
       [("aus Gründen … ", 0), ("zum Schutze der Gesundheit und des Lebens", "a")],
       [("von Menschen", "a"), (", Tieren oder Pflanzen … gerechtfertigt sind.“", 0)]]
_k36, _y36 = zitatkarte(W36, 110, 240, 30, "a36", {"a": beim("a36", "Gesundheitsschutz")})
folie([("zus", P2), ("a36", f"{P2} › Art. 36 AEUV"), ("erf", f"{P2} › nur so weit tatsächlich erforderlich")],
      rechts_frei([
    *tafel("zus", "2. Die Zusatzstoffe"),
    z("Art. 36 AEUV (Auszug)", 110, 180, "a36", "Bold", 36),
    *_k36,
    fund("Art. 36 AEUV, ABl. C 202 vom 7.6.2016, S. 61", 110, int(_y36 + 12), "a36"),
    *okz("Zulassungspflicht für Zusatzstoffe: grundsätzlich", int(_y36 + 85), "zulass", size=34),
    z("zulässig", 185, int(_y36 + 135), beim("zulass", "Zulassung"), size=34),
    fb(110, int(_y36 + 205), 1040, 130, GELB, "erf", [("aber nur, soweit für den Gesundheits-", "ExtraBold", 33, INK),
                                                     ("schutz tatsächlich erforderlich", "ExtraBold", 33, INK)]),
    fund("Rs. 178/84, Rn. 40, 42, 44", 110, int(_y36 + 350), "erf"),
    *icons([("tabler", "flask", "zus", ROTHELL), ("tabler", "shield-check", "a36", GRUENHELL),
            ("tabler", "certificate", "zulass", HELL), ("tabler", "scale", "erf", GELB)], IX, 560, 190),
    *wechsel([("Zusatzstoffe", "zus", ROTHELL), ("Gesundheit: Art. 36", "a36", GRUENHELL),
              ("Zulassung erlaubt", "zulass", HELL), ("nur soweit erforderlich", "erf", GELB)], IX, 640, size=30),
]))

# E4b Pauschalverbot unverhältnismäßig (Rn. 44, 47, 53) -------------------------------------------------------------------------
folie([("muss", f"{P2} › im anderen Mitgliedstaat zugelassen"), ("pausch", f"{P2} › pauschales Verbot"),
       ("v2", f"{P2} › unverhältnismäßig")], rechts_frei([
    *tafel("muss", "Pauschales Verbot?"),
    z("In einem anderen Mitgliedstaat zugelassen:", 110, 185, "muss", "Bold", 34),
    *okz("keine Gefahr für die Gesundheit", 250, beim("muss", "Gesundheit"), size=34),
    *okz("echtes Bedürfnis", 310, beim("muss", "echten"), size=34),
    fb(110, 385, 1040, 90, GRUENHELL, beim("muss", "entspricht"), [("dann muss der Einfuhrstaat zulassen", "ExtraBold", 33, INK)]),
    *neinz("Deutschland: alle Zusatzstoffe pauschal verboten", 520, "pausch", "Bold", 33),
    *neinz("kein Verfahren für die Zulassung", 580, "verf", "Bold", 33),
    fb(110, 660, 1040, 90, ROTHELL, "v2", [("unverhältnismäßig, nicht durch Art. 36 gedeckt", "ExtraBold", 33, INK)]),
    fund("Rs. 178/84, Rn. 44, 47, 53", 110, 770, "v2"),
    *paar("muss", [("ruhig",), ("denkt", "pausch"), ("froh", "v2")],
          [("ruhig",), ("ernst", "pausch"), ("staunt", "v2")]),
]))

# E5 Ergebnis und heutige Rechtslage (Tenor; § 1 Abs. 1, 2 BierV) ---------------------------------------------------------------
WB = [[("„Abweichend von Absatz 1 dürfen ", 0), ("im Ausland hergestellte", "a"), (" gegorene", 0)],
      [("Getränke, die nicht den in Absatz 1 genannten Vorschriften", 0)],
      [("entsprechen, unter der Bezeichnung ‚Bier‘ gewerbsmäßig in den Verkehr", 0)],
      [("gebracht werden, wenn sie im jeweiligen ", 0), ("Herstellungsland", "b"), (" unter der", 0)],
      [("Bezeichnung ‚Bier‘ oder einer dieser Bezeichnung entsprechenden", 0)],
      [("Bezeichnung des Lebensmittels ", 0), ("verkehrsfähig", "b"), (" sind.“", 0)]]
_kb, _yb = zitatkarte(WB, 110, 335, 28, "bierv", {"a": beim("bierv", "Ausland"), "b": beim("bierv", "Herstellungsland")})
folie([("tenor", f"{PR} · Ergebnis"), ("bierv", "Heute · § 1 Abs. 2 BierV"), ("ilnd", "Heute · Inländerdiskriminierung")],
      rechts_frei([
    *tafel("tenor", "Ergebnis und heute"),
    z("Tenor: Deutschland hat gegen Art. 30 EWG-Vertrag", 110, 180, "tenor", "Bold", 33),
    z("(heute Art. 34 AEUV) verstoßen", 110, 228, beim("tenor", "Deutschland"), size=33),
    fund("§ 1 Abs. 2 Satz 1 BierV (Stand 5.7.2017)", 110, 290, "bierv"),
    *_kb,
    z("in Deutschland hergestellt: grundsätzlich Reinheitsgebot", 110, int(_yb + 30), "inl", "Bold", 33),
    fund("§ 1 Abs. 1 BierV", 110, int(_yb + 85), "inl"),
    fb(110, int(_yb + 140), 1040, 80, LILAHELL, "ilnd", [("Inländerdiskriminierung", "ExtraBold", 34, INK)]),
    *paar("tenor", [("ruhig",), ("froh", "bierv"), ("denkt", "inl")],
          [("ruhig",), ("still", "bierv"), ("staunt", "ilnd")]),
]))

# F1 Lösung (Tafel) -------------------------------------------------------------------------------------------------------------
PL_ = "Lösung · Herr Brodersen"
folie([("loes", PL_), ("l3", f"{PL_} · Etikett statt Verbot")], rechts_frei([
    *tafel("loes", "Lösung: Herr Brodersen"),
    *okz("Verbot des Namens „Bier“: unterschiedslos,", 185, "l1", size=34),
    z("behindert aber die Einfuhr", 185, 235, beim("l1", "behindert"), size=34),
    *okz("Verbraucherschutz: zwingendes Erfordernis", 310, "l2", size=34),
    *okz("milder: Etikett mit Gerstenmalz, Reis und Mais", 385, "l3", "Bold", 34),
    fb(110, 470, 1040, 90, ROTHELL, "l4", [("Verbot wäre unverhältnismäßig", "ExtraBold", 34, INK)]),
    fund("Rs. 178/84, Rn. 28, 35, 37; heute auch § 1 Abs. 2 BierV", 110, 580, "l4"),
    *paar("loes", [("ruhig",), ("denkt", "l2"), ("froh", "l3")], [("ruhig",), ("ernst", "l2"), ("denkt", "l4")]),
]))

# F2 Zurück im Getränkehandel ---------------------------------------------------------------------------------------------------
folie([("l5", "Lösung · Das Bier darf Bier heißen")], [
    *laden("l5"),
    *belgierkiste("l5", anim="cut"),
    ficon("tabler", "door", 1830, BODEN, 90, "l5", fuell=HOLZ, anim="cut"),
    pl("darf als Bier verkauft werden", ZB, 135, "l5", fill=GRUENHELL, size=32, anker="m", bis="t2"),
    pl("Etikett: Gerstenmalz, Reis und Mais", ZB, 205, beim("l5", "belgisches"), fill=HELL, size=28, anker="m", bis="t2"),
    ficon("tabler", "label", 585, BODEN - 45, 70, beim("l5", "belgisches"), fuell=WEISS),
    *stufen([("BD_froh_r", "l5"), ("BD_entschlossen_r", "t2")], BDX, BODEN, GH, erst="cut", ende="tipp"),
    namensschild(NAME["BD"], BDX, BODEN, "l5", FARBE["BD"]),
    *stufen([("TM_ruhig", "l5"), ("TM_einsicht", "t2")], TMX, BODEN, GH, rede={"TM_einsicht": 1}, erst="cut", ende="tipp"),
    namensschild(NAME["TM"], TMX, BODEN, "l5", FARBE["TM"]),
    blase("sprech", 700, 190, "t2", 1100, 240, inhalt=["Gut, dann darf es", "auch hier Bier heißen."], textsize=34, figur=TMb),
])

# G Klausurtipp (Lexi) ---------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · zwingende Erfordernisse nur bei unterschiedslosen Maßnahmen"),
       ("disk", "Klausurtipp · nur eingeführte Waren betroffen: allein Art. 36 AEUV")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Zwingende Erfordernisse: nur bei", 200, 200, beim("tipp", "Zwingende"), "Bold", 34),
    z("unterschiedslos anwendbaren Maßnahmen", 200, 255, beim("tipp", "unterschiedslos"), "Bold", 34),
    fund("Rs. 113/80 (Kommission/Irland), Rn. 10, 11; Rs. 178/84, Rn. 28", 200, 312, beim("tipp", "unterschiedslos")),
    fb(200, 400, 950, 130, GELB, "disk", [("nur eingeführte Waren betroffen:", "ExtraBold", 32, INK),
                                        ("allein Art. 36 AEUV", "ExtraBold", 32, INK)]),
    z("Gründe abschließend, eng auszulegen", 200, 570, "eng", "Bold", 34),
    fund("Rs. 113/80, Rn. 7", 200, 625, "eng"),
    *redet("LX_warnt", LXX, BR, FR + 60, "tipp", "sch"),
    namensschild("Lexi", LXX, BR, "tipp", GELB, d=0.2),
])

# H Schema der Rechtfertigung ------------------------------------------------------------------------------------------------
PS_ = "Schema · Rechtfertigung"
FX = 1270
folie([("sch", PS_), ("s1", f"{PS_} › I. Rechtfertigungsgrund"), ("s2", f"{PS_} › II. Verhältnismäßigkeit")], [
    karte(60, 50, 1800, 920, "sch"),
    titel("Schema: Rechtfertigung bei Art. 34 AEUV", 110, 85, "sch", 48),
    pl("I.", 110, 182, "s1", fill=GELB, size=32), z("Rechtfertigungsgrund", 220, 180, "s1", "Bold", 36, rechts=FX - 20),
    z("1. Art. 36 AEUV", 220, 245, "s1a", size=34, rechts=FX - 20),
    z("Art. 36 AEUV; Rs. 113/80, Rn. 7", FX, 250, "s1a", size=28, farbe=TEXT, rechts=1840),
    z("2. zwingendes Erfordernis", 220, 305, "s1b", size=34, rechts=FX - 20),
    z("Rs. 120/78, Rn. 8", FX, 310, "s1b", size=28, farbe=TEXT, rechts=1840),
    z("nur bei unterschiedslosen Maßnahmen", 265, 360, beim("s1b", "nur"), size=32, rechts=FX - 20),
    z("Rs. 113/80, Rn. 10, 11", FX, 365, beim("s1b", "nur"), size=28, farbe=TEXT, rechts=1840),
    pl("II.", 110, 452, "s2", fill=GRUEN, size=32), z("Verhältnismäßigkeit", 220, 450, "s2", "Bold", 36, rechts=FX - 20),
    z("1. geeignet", 220, 515, "s2a", size=34, rechts=FX - 20),
    z("2. mildestes unter mehreren geeigneten Mitteln", 220, 575, "s2b", size=34, rechts=FX - 20),
    z("Rs. 178/84, Rn. 28", FX, 580, "s2b", size=28, farbe=TEXT, rechts=1840),
    z("z. B. Etikett statt Verbot", 265, 630, beim("s2b", "etwa"), size=32, rechts=FX - 20),
    z("Rs. 120/78, Rn. 13; Rs. 178/84, Rn. 35", FX, 635, beim("s2b", "etwa"), size=28, farbe=TEXT, rechts=1840),
])

# I Merksatz (Lexi) --------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Unterschiedslos anwendbare Regeln", 0)],
                 [("können durch ", 0), ("zwingende Erfordernisse", "a")],
                 [("gerechtfertigt sein, aber nur, soweit", 0)],
                 [("sie ", 0), ("notwendig", "b"), (" sind.", 0)]], 750, 290, 42, "merke",
                {"a": beim("merke", "zwingende"), "b": beim("merke", "notwendig")}),
    *markertext([[("Reicht ein ", 0), ("Etikett", "c"), (", darf, was in einem", 0)],
                 [("Mitgliedstaat rechtmäßig hergestellt", 0)],
                 [("und verkauft wird, auch in den", 0)],
                 [("anderen verkauft werden.", 0)]], 750, 570, 42, "m2", {"c": beim("m2", "Etikett")}),
    *redet("LX_erklaert", 1680, 960, 690, "merke", lexi_bis_ende("merke")),
    namensschild("Lexi", 1680, 960, "merke", GELB, d=0.2),
])
