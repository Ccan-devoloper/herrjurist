"""Folge 164 · Richtlinie unmittelbare Wirkung: Nicht umgesetzt – und jetzt? – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A Fall in der Fahrzeughalle der Feuerwache (Herr Ruppert, Herr Goldbach; Annahme deutlich
gekennzeichnet), B Sachverhalt, C Normen I (Art. 288 Abs. 3 AEUV, Wortlautkarte), D Normen II (Art. 4 Abs. 3 UAbs. 2 EUV,
Wortlautkarte, vorgelesen; Verweis Folge 138), E 1. Umsetzungsfrist (Ratti), F 2. nicht umgesetzt, G 3. unbedingt und
hinreichend genau (Art. 6 Buchst. b RL 2003/88/EG, Wortlautkarte), H 4. gegenüber dem Staat, I Foster (Zitatkarte Rn. 20),
J Farrell und die Stadt, K keine Wirkung zwischen Privaten (Verweis 138), L Lösung, M der echte Fall Fuß und der neue
Dienstplan (zurück in der Fahrzeughalle), N Klausurtipp (Lexi), O Klausurschema, P Merksatz (Lexi).
Feuerwehr neutral: Löschfahrzeug als Tabler-Linienicon ohne Beschriftung, kein Wappen. Reale Personen (Ratti, Foster,
Farrell, Fuß, Faccini Dori) nur als Fallnamen; keine Personen-Icons.
Geräusche nur bei sichtbarer Handlung: Tür (Herr Goldbach kommt in die Halle), Stift (der Dienstplan wird geändert);
Freesound CC0, ../geraeusche_herkunft.json.
Hilfsfunktionen (glyphen, z, pl, tafel, fb, wl_links, redet mit hörbarem Wortende …) als eigene Kopie aus Folge 138
(gemeinsame Dateien unverändert); Stil-C-Pflicht für Sprechblasen und lexi_bis_ende() wie in Folge 161.
Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
from engine import El, F

bausteine.FIGORDNER = "op_164/"
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


def zitatkarte(zeilen, x, y, size, cue, hl, fill=ZITAT):
    """Wortlautkarte: Karte + linksbündiger Wortlaut mit Markern; gibt (Elemente, y_ende) zurück."""
    els, y1 = wl_links(zeilen, x + 30, y + 18, size, cue, hl)
    return [karte(x, y, 1040, int(y1 - y + 22), cue, fill=fill, rund=18, schatten=6, rand=4)] + els, y1 + 22


def lexi_bis_ende(cue):
    return (cue, round(DAUER - bausteine._t(cue) + 0.5, 3))       # Lexi bleibt bis zum letzten Frame (wie 161)


def rechts_frei(els, x0=1250):
    """Figuren und Requisiten der Tafelfolien stehen rechts der Tafel (x ≥ 1250)."""
    for e in els:
        n = e.name or ""
        if n.startswith(("bild:", "ficon:")) or "/op_164/" in n:
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
FARBE = {"RU": BLAU, "GO": GRUEN}
NAME = {"RU": "Herr Ruppert", "GO": "Herr Goldbach"}


def kette(prefix, x, folge, bis_=None, d=0.0, hoehe=FR, unten=BR):
    """Eine Figur mit Mimikfolge [(Name, Cue), …] im Zwiebelschalenprinzip (erster Auftritt pop, danach harte Schnitte)."""
    els = []
    for i, (n, c) in enumerate(folge):
        b = folge[i + 1][1] if i + 1 < len(folge) else bis_
        els.append(peep_voll(prefix + n, x, unten, hoehe, c, anim=("pop" if i == 0 else "cut"), d=(d if i == 0 else 0.0), bis=b))
    return els


def paar(cue, f1, f2):
    """Herr Ruppert (links) und Herr Goldbach (rechts) neben der Tafel, beide blicken zur Tafel; Namensschilder ab Beginn."""
    els = kette("RU_", X1, [(f1[0][0], cue)] + list(f1[1:])) + kette("GO_", X2, [(f2[0][0], cue)] + list(f2[1:]), d=0.2)
    return els + [namensschild(NAME["RU"], X1, BR, cue, FARBE["RU"], d=0.2),
                  namensschild(NAME["GO"], X2, BR, cue, FARBE["GO"], d=0.3)]


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


# A Fall: Fahrzeughalle der Feuerwache ----------------------------------------------------------------------------------
BODEN, GH = 900, 520
RUX, GOX = 400, 1560
RUa = ("RU_redet_r", RUX, BODEN, GH)
GOa = ("GO_redet", GOX, BODEN, GH)
GOb = ("GO_einsicht", GOX, BODEN, GH)


def halle(cue):
    """Bodenlinie, offenes Hallentor (Grundformen) mit Löschfahrzeug (Tabler, ohne Beschriftung), Helm am Haken,
    Dienstplan an der Wand."""
    els = [linienzug([(60, BODEN), (1860, BODEN)], cue, breite=7, farbe=INK),
           karte(760, 400, 540, BODEN - 400, cue, fill=GRAU, rund=8, schatten=0, rand=6)]
    for yy in (430, 460):                                   # hochgerolltes Tor (Lamellen oben)
        els.append(linienzug([(766, yy), (1294, yy)], cue, breite=4, farbe=GRAUD))
    els += [ficon("tabler", "firetruck", 1030, BODEN - 4, 430, cue, fuell=ROT),
            linienzug([(1365, 560), (1365, 585)], cue, breite=6, farbe=INK),
            ficon("tabler", "helmet", 1365, 650, 80, cue, fuell=GELB),
            ficon("tabler", "clipboard-list", 655, 560, 110, cue, fuell=WEISS)]
    return els


folie([("fall", "Fall · Herr Ruppert und seine Wochenstunden"), ("gold", "Fall · Herr Goldbach vom Personalamt"),
       ("ann", "Fall · Annahme: nicht rechtzeitig umgesetzt"), ("frage", "Fall · Die Frage")], [
    *halle("fall"),
    pl("Berufsfeuerwehr der Stadt", 70, 40, "fall", fill=GELB, size=34, bis="gold"),
    pl("Dienstplan: 54 Std.", 655, 578, "plan2", fill=ROTHELL, size=26, anker="m", bis="loes1"),
    *stufen([("RU_ruhig_r", "fall"), ("RU_denkt_r", "plan"), ("RU_sorge_r", "plan2"), ("RU_entschlossen_r", "rl"),
             ("RU_redet_r", "r1"), ("RU_ruhig_r", "gold"), ("RU_ernst_r", "g1"), ("RU_denkt_r", "ann"),
             ("RU_staunt_r", "frage")], RUX, BODEN, GH, rede={"RU_redet_r": 1}, erst="cut"),
    namensschild(NAME["RU"], RUX, BODEN, "fall", FARBE["RU"]),
    pl("Landesverordnung: im Schnitt 54 Wochenstunden", 1070, 160, beim("plan", "Landesverordnung"), fill=ROTHELL, size=30,
       anker="m", bis="r1"),
    pl("EU-Arbeitszeitrichtlinie 2003/88/EG", 1070, 240, beim("rl", "EU-Arbeitszeitrichtlinie"), fill=BLAUHELL, size=30,
       anker="m", bis="r1"),
    blase("sprech", 820, 230, "r1", 900, 235, inhalt=["Im Schnitt 48 Stunden, mehr erlaubt", "die Richtlinie nicht. Daran",
          "muss sich die Stadt halten."], textsize=31, figur=RUa, bis="gold"),
    # Herr Goldbach kommt durch die Tür in die Halle
    szene(ficon("tabler", "door", 1815, BODEN, 100, "gold", fuell=HOLZ), "164tuer*", 1.0, versatz=0.05),
    *stufen([("GO_ruhig", "gold"), ("GO_redet", "g1"), ("GO_ernst", "ann"), ("GO_still", "echt"), ("GO_denkt", "frage")],
            GOX, BODEN, GH, rede={"GO_redet": 1}),
    namensschild(NAME["GO"], GOX, BODEN, "gold", FARBE["GO"], d=0.2),
    pl("Personalamt der Stadt", GOX, 330, beim("gold", "Personalamt"), fill=WEISS, size=28, anker="m", bis="g1"),
    blase("sprech", 780, 230, "g1", 1080, 235, inhalt=["Die Richtlinie richtet sich an", "Deutschland, nicht an uns.",
          "Bei uns gilt die Verordnung."], textsize=31, figur=GOa, bis="ann"),
    # Annahme und Frage
    pl("Annahme: Deutschland hätte die Richtlinie nicht rechtzeitig umgesetzt", 980, 150, "ann", fill=HELL, size=28,
       anker="m"),
    pl("In Wirklichkeit ist sie umgesetzt, etwa im Arbeitszeitgesetz", 980, 225, "echt", fill=WEISS, size=28, anker="m"),
    pl("Kann er sich trotzdem direkt auf die Richtlinie berufen?", 980, 305, "frage", fill=PINK, size=32, anker="m"),
])

# B Sachverhalt -------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    glyphen("Herr Ruppert ist Feuerwehrmann bei der Berufsfeuerwehr seiner Stadt. Eine Landesverordnung erlaubt für die "
            "Feuerwehr im Schnitt 54 Wochenstunden; so plant ihn die Stadt ein. Herr Ruppert beruft sich auf die "
            "EU-Arbeitszeitrichtlinie 2003/88/EG: im Schnitt höchstens 48 Stunden pro Woche."),
    glyphen("Herr Goldbach, Leiter des Personalamts der Stadt, hält dagegen: Die Richtlinie richte sich an Deutschland, nicht "
            "an die Stadt. Es gelte die Verordnung."),
    glyphen("Annahme für den Fall: Deutschland hätte die Richtlinie nicht rechtzeitig umgesetzt (in Wirklichkeit ist sie "
            "umgesetzt)."),
], "Kann sich Herr Ruppert gegenüber der Stadt direkt auf die Richtlinie berufen?")

# C Normen I: Art. 288 Abs. 3 AEUV (Cellar CELEX 12016E288, ABl. C 202 vom 7.6.2016, S. 171) ------------------------------
PN = "Normen"
W288 = [[("„Die Richtlinie ist ", 0), ("für jeden Mitgliedstaat, an den sie", "c")],
        [("gerichtet wird", "c"), (", ", 0), ("hinsichtlich des zu erreichenden Ziels", "a")],
        [("verbindlich", "a"), (", überlässt jedoch den innerstaatlichen", 0)],
        [("Stellen die ", 0), ("Wahl der Form und der Mittel", "b"), (".“", 0)]]
_k288, _y288 = zitatkarte(W288, 110, 250, 32, "a288", {"a": beim("a288", "hinsichtlich"), "b": beim("form", "Wahl"),
                                                       "c": beim("gold2", "Adressat")})
folie([("norm", f"{PN} › Art. 288 Abs. 3 AEUV"), ("gold2", f"{PN} › Art. 288 Abs. 3 AEUV: Adressat ist der Mitgliedstaat")],
      rechts_frei([
    *tafel("norm", "Die Normen"),
    z("Art. 288 Abs. 3 AEUV", 110, 185, "a288", "Bold", 36),
    *_k288,
    fund("Art. 288 Abs. 3 AEUV, ABl. C 202 vom 7.6.2016, S. 171", 110, int(_y288 + 12), "a288"),
    z("verbindlich: nur das Ziel", 110, int(_y288 + 75), beim("a288", "nur"), "Bold", 34),
    z("Form und Mittel: innerstaatliche Stellen", 110, int(_y288 + 130), "form", size=34),
    fb(110, int(_y288 + 200), 1040, 90, GRUEN, "gold2", [("Adressat ist der Mitgliedstaat", "ExtraBold", 34, INK)]),
    *einzeln("GO", "norm", [("ruhig",), ("denkt", "a288"), ("ernst", "form"), ("froh", "gold2")]),
    pl("Insoweit hat er recht", XE, 330, "gold2", fill=GRUEN, size=28, anker="m"),
]))

# D Normen II: Art. 4 Abs. 3 UAbs. 2 EUV (CELEX 12016M004, ABl. C 202 vom 7.6.2016, S. 18) -------------------------------------
W4 = [[("„Die Mitgliedstaaten ergreifen ", 0), ("alle geeigneten Maßnahmen", "a")],
      [("allgemeiner oder besonderer Art zur Erfüllung der", 0)],
      [("Verpflichtungen, die sich aus den Verträgen oder den", 0)],
      [("Handlungen der Organe der Union", "b"), (" ergeben.“", 0)]]
_k4, _y4 = zitatkarte(W4, 110, 250, 32, "a4", {"a": beim("a4", "alle"), "b": beim("a4", "Handlungen")})
folie([("a4", f"{PN} › Art. 4 Abs. 3 EUV: Pflicht zur Umsetzung"),
       ("vert", f"{PN} › Pflicht verletzt? Vertikale unmittelbare Wirkung")], rechts_frei([
    *tafel("a4", "Die Pflicht zur Umsetzung"),
    z("Art. 4 Abs. 3 UAbs. 2 EUV", 110, 185, "a4", "Bold", 36),
    *_k4,
    fund("Art. 4 Abs. 3 UAbs. 2 EUV, ABl. C 202 vom 7.6.2016, S. 18", 110, int(_y4 + 12), "a4"),
    fb(110, int(_y4 + 70), 1040, 90, GRUEN, "pfl", [("Eine Richtlinie umzusetzen ist Pflicht", "ExtraBold", 34, INK)]),
    fund("Fuß II, EuGH, Rs. C-429/09, Rn. 39", 110, int(_y4 + 172), "pfl"),
    fb(110, int(_y4 + 230), 1040, 130, HELL, "vert", [("Pflicht verletzt? Vertikale unmittelbare", "ExtraBold", 34, INK),
                                                    ("Wirkung, in 4 Schritten", "ExtraBold", 34, INK)]),
    *wechsel([("Handlungen der Organe", beim("a4", "Handlungen"), WEISS), ("Richtlinie umsetzen: Pflicht", "pfl", GRUEN),
              ("Überblick: Video „EU-Rechtsakte“", "v138", BLAUHELL), ("4 Schritte", "vert", HELL)], IX, 200, size=30),
    *icons([("tabler", "file-certificate", "a4", BLAU), ("tabler", "checkbox", "pfl", GRUEN), ("tabler", "books", "v138", GELB),
            ("tabler", "list-check", "vert", HELL)], IX, 600, 190),
]))

# E 1. Umsetzungsfrist abgelaufen: Ratti (Rs. 148/78) ------------------------------------------------------------------------
P1 = "1. Umsetzungsfrist abgelaufen"
folie([("s1", P1), ("ratti", f"{P1} › Ratti, EuGH 1979"), ("ende", f"{P1} › Wirkung erst am Ende der Frist"),
       ("frist", f"{P1} › im Fall: längst abgelaufen")], rechts_frei([
    *tafel("s1", "1. Umsetzungsfrist abgelaufen"),
    karte(110, 175, 1040, 175, "ratti", fill=HELL, rund=18, schatten=6, rand=4),
    z("Ratti, EuGH 1979: Unternehmen für Lösemittel und Lacke", 135, 190, "ratti", "Bold", 30, rechts=1140),
    z("gekennzeichnet nach 2 europäischen Richtlinien, nicht", 135, 240, "kennz", size=30, rechts=1140),
    z("nach dem italienischen Gesetz (mehr Angaben)", 135, 285, beim("kennz", "italienischen"), size=30, rechts=1140),
    ok(135, 400, "loes", gr=18),
    z("Lösemittel: Frist abgelaufen (8.12.1974)", 170, 380, "loes", "Bold", 30),
    z("altes Recht nicht anwendbar, auch nicht als Strafrecht", 170, 425, beim("loes", "Italien"), size=30),
    nein(135, 500, "lack", gr=18),
    z("Lacke: Frist lief noch (bis 9.11.1979)", 170, 480, "lack", "Bold", 30),
    karte(110, 545, 1040, 92, "ende", fill=ZITAT, rund=18, schatten=6, rand=4),
    z("„… erst am Ende des festgesetzten Zeitraums …“", 140, 568, "ende", "Bold", 32, rechts=1140),
    fund("Rs. 148/78 (Ratti), Slg. 1979, 1629, Rn. 2, 3, 5 f., 22–24, 41–43; Tenor 1, 5", 110, 650, "ende"),
    fb(110, 705, 1040, 90, GRUEN, "frist", [("Im Fall: Frist längst abgelaufen", "ExtraBold", 34, INK)]),
    fund("Vorgängerin RL 93/104/EG: umzusetzen bis 23.11.1996 (Fuß I, Rn. 3)", 110, 805, beim("frist", "Vorgängerrichtlinie")),
    ficon("tabler", "calendar-due", IX, 420, 160, "s1", fuell=HELL, bis="ratti"),
    pl("Frist abgelaufen?", IX, 200, "s1", fill=HELL, size=30, anker="m", bis="ratti"),
    ficon("tabler", "flask", 1430, 560, 130, "ratti", fuell=BLAUHELL),
    pl("Lösemittel", 1430, 575, "ratti", fill=BLAUHELL, size=28, anker="m"),
    ficon("tabler", "brush", 1730, 560, 130, "ratti", fuell=GELB),
    pl("Lacke", 1730, 575, "ratti", fill=GELB, size=28, anker="m"),
    ok(1430, 680, "loes", gr=26),
    nein(1730, 680, "lack", gr=26),
    ficon("tabler", "calendar-check", IX, 330, 140, "frist", fuell=GRUEN),
    pl("im Fall: abgelaufen", IX, 360, "frist", fill=GRUEN, size=28, anker="m"),
]))

# F 2. Nicht oder nicht ordnungsgemäß umgesetzt ------------------------------------------------------------------------------
P2 = "2. Nicht oder nicht ordnungsgemäß umgesetzt"
folie([("s2", P2), ("s2f", f"{P2} › im Fall: Annahme, keine Umsetzung")], rechts_frei([
    *tafel("s2", "2. Nicht ordnungsgemäß umgesetzt"),
    z("Der Staat hat die Richtlinie", 110, 190, "s2", "Bold", 34),
    z("nicht oder nicht ordnungsgemäß umgesetzt", 110, 240, beim("s2", "nicht"), "Bold", 34),
    fund("Fuß I, EuGH, Rs. C-243/09, Rn. 56; Marshall, Rs. 152/84, Rn. 46", 110, 300, beim("s2", "ordnungsgemäß")),
    karte(110, 380, 1040, 250, "s2f", fill=HELL, rund=18, schatten=6, rand=4),
    z("Im Fall (Annahme):", 140, 400, "s2f", "Bold", 34, rechts=1140),
    ok(165, 485, beim("s2f", "ganz"), gr=18),
    z("Umsetzung fehlt ganz", 200, 465, beim("s2f", "ganz"), size=34, rechts=1140),
    ok(165, 555, beim("s2f", "Verordnung"), gr=18),
    z("Verordnung: mehr als 48 Wochenstunden", 200, 535, beim("s2f", "Verordnung"), size=34, rechts=1140),
    *einzeln("RU", "s2", [("ernst",), ("sorge", "s2f"), ("entschlossen", beim("s2f", "Verordnung"))]),
    pl("Annahme", XE, 330, "s2f", fill=HELL, size=30, anker="m"),
]))

# G 3. Unbedingt und hinreichend genau: Art. 6 Buchst. b RL 2003/88/EG (CELEX 32003L0088, ABl. L 299 vom 18.11.2003, S. 9)
P3 = "3. Unbedingt und hinreichend genau"
W6 = [[("„Die Mitgliedstaaten treffen die erforderlichen Maßnahmen,", 0)],
      [("damit … b) die ", 0), ("durchschnittliche Arbeitszeit pro", "a")],
      [("Siebentageszeitraum", "a"), (" ", 0), ("48 Stunden einschließlich der", "b")],
      [("Überstunden", "b"), (" nicht überschreitet.“", 0)]]
_k6, _y6 = zitatkarte(W6, 110, 250, 31, "a6", {"a": beim("a6", "durchschnittliche"), "b": beim("a6", "achtundvierzig")})
folie([("s3", P3), ("a6", f"{P3} › Art. 6 Buchst. b RL 2003/88/EG"), ("abw", f"{P3} › Abweichungen nach Art. 22")],
      rechts_frei([
    *tafel("s3", "3. Unbedingt und hinreichend genau"),
    z("Art. 6 Buchst. b Arbeitszeitrichtlinie", 110, 185, "a6", "Bold", 34),
    *_k6,
    fund("Art. 6 Buchst. b RL 2003/88/EG, ABl. L 299 vom 18.11.2003, S. 9", 110, int(_y6 + 12), "a6"),
    ok(135, int(_y6 + 92), "klar", gr=18),
    z("festes Ergebnis, an keine Bedingung geknüpft", 170, int(_y6 + 72), "klar", size=32),
    z("Abweichungen (Art. 22): nur unter engen Voraussetzungen", 110, int(_y6 + 135), "abw", size=32),
    fb(110, int(_y6 + 200), 1040, 130, GRUEN, "gen", [("„nimmt … nichts von seiner Genauigkeit", "ExtraBold", 32, INK),
                                                    ("und Unbedingtheit“", "ExtraBold", 32, INK)]),
    fund("Fuß I, EuGH, Rs. C-243/09, Rn. 34 f., 57–59; Ratti, Rn. 23", 110, int(_y6 + 342), "gen"),
    pl("unbedingt und hinreichend genau?", IX, 200, "s3", fill=HELL, size=28, anker="m", bis="a6"),
    ficon("tabler", "clock-hour-8", IX, 470, 170, "s3", fuell=BLAUHELL),
    pl("im Schnitt 48 Std.", IX, 490, beim("a6", "achtundvierzig"), fill=BLAUHELL, size=30, anker="m"),
    pl("festes Ergebnis", IX, 200, "klar", fill=GRUEN, size=30, anker="m", bis="abw"),
    pl("Art. 22: enge Voraussetzungen", IX, 200, "abw", fill=HELL, size=28, anker="m"),
    ok(IX, 680, "gen", gr=30),
]))

# H 4. Gegenüber dem Staat ------------------------------------------------------------------------------------------------
P4 = "4. Gegenüber dem Staat (vertikal)"
folie([("s4", P4), ("arb", f"{P4} › als Hoheitsträger oder Arbeitgeber")], rechts_frei([
    *tafel("s4", "4. Gegenüber dem Staat"),
    z("Der Einzelne beruft sich gegenüber dem Staat:", 110, 190, "s4", "Bold", 34),
    z("die vertikale Richtung", 110, 240, beim("s4", "vertikale"), size=34),
    ok(135, 345, beim("arb", "Hoheitsträger"), gr=18),
    z("Staat als Hoheitsträger", 170, 325, beim("arb", "Hoheitsträger"), size=34),
    ok(135, 410, beim("arb", "Arbeitgeber"), gr=18),
    z("Staat als Arbeitgeber", 170, 390, beim("arb", "Arbeitgeber"), size=34),
    fb(110, 490, 1040, 130, HELL, "nutz", [("kein Nutzen aus dem eigenen", "ExtraBold", 34, INK),
                                          ("Versäumnis", "ExtraBold", 34, INK)]),
    fund("Marshall, Rs. 152/84, Rn. 49; Foster, Rn. 17; Fuß I, Rn. 56", 110, 635, "nutz"),
    *paar("s4", [("ruhig",), ("entschlossen", beim("s4", "Einzelne")), ("froh", "arb")],
          [("ruhig",), ("denkt", beim("s4", "Staat")), ("staunt", beim("arb", "Arbeitgeber")), ("still", "nutz")]),
    pl("Einzelner", X1, 330, beim("s4", "Einzelne"), fill=BLAU, size=28, anker="m"),
    pl("Staat", X2, 330, beim("s4", "Staat"), fill=GELB, size=28, anker="m", bis="arb"),
    pl("Arbeitgeber", X2, 330, beim("arb", "Arbeitgeber"), fill=GELB, size=28, anker="m"),
    pl("vertikal", (X1 + X2) // 2, 230, beim("s4", "vertikale"), fill=GRUEN, size=28, anker="m"),
]))

# I Funktionaler Staatsbegriff: Foster (Rs. C-188/89, Slg. 1990, I-3313) ---------------------------------------------------
PF = "4. Gegenüber dem Staat"
WF = [[("„… jedenfalls eine Einrichtung, die ", 0), ("unabhängig von ihrer", "a")],
      [("Rechtsform", "a"), (" ", 0), ("kraft staatlichen Rechtsakts", "b"), (" ", 0), ("unter staatlicher", "c")],
      [("Aufsicht", "c"), (" eine ", 0), ("Dienstleistung im öffentlichen Interesse", "d")],
      [("zu erbringen hat und die hierzu ", 0), ("mit besonderen Rechten", "e")],
      [("ausgestattet", "e"), (" ist, die über das hinausgehen, was für die", 0)],
      [("Beziehungen zwischen Privatpersonen gilt …“", 0)]]
_kf, _yf = zitatkarte(WF, 110, 415, 29, "formel", {"a": beim("formel", "Unabhängig"), "b": beim("formel", "kraft"),
                                                  "c": beim("formel", "unter"), "d": beim("formel", "Dienstleistung"),
                                                  "e": beim("formel", "besonderen")})
folie([("staat", f"{PF} › funktionaler Staatsbegriff"), ("foster", f"{PF} › Foster, EuGH 1990")], rechts_frei([
    *tafel("staat", "Wer ist der Staat?"),
    z("funktional verstanden", 110, 175, beim("staat", "funktional"), "Bold", 34),
    karte(110, 230, 1040, 160, "foster", fill=HELL, rund=18, schatten=6, rand=4),
    z("Foster: British Gas Corporation, Frauen mit 60 in den", 135, 245, "foster", "Bold", 30, rechts=1140),
    z("Ruhestand, Männer erst mit 65", 135, 290, beim("foster", "Männer"), size=30, rechts=1140),
    z("British Gas: durch Gesetz errichtet, Monopol für die Gasversorgung", 135, 335, "bgc", size=30, rechts=1140),
    *_kf,
    fund("Rs. C-188/89 (Foster), Slg. 1990, I-3313, Rn. 3, 8, 20", 110, int(_yf + 12), "formel"),
    pl("Wer ist der Staat?", IX, 200, "staat", fill=HELL, size=30, anker="m", bis="foster"),
    ficon("tabler", "flame", IX, 470, 150, "foster", fuell=BLAU),
    pl("Frauen: 60", 1440, 560, beim("foster", "Frauen"), fill=PINK, size=30, anker="m"),
    pl("Männer: 65", 1720, 560, beim("foster", "Männer"), fill=BLAUHELL, size=30, anker="m"),
    pl("durch Gesetz errichtet", IX, 660, "bgc", fill=WEISS, size=28, anker="m"),
    pl("Monopol Gasversorgung", IX, 730, beim("bgc", "Monopol"), fill=WEISS, size=28, anker="m"),
    pl("Foster, EuGH 1990", IX, 200, "foster", fill=GELB, size=30, anker="m"),
]))

# J Farrell (Rs. C-413/15) und die Stadt ----------------------------------------------------------------------------------
folie([("farrell", f"{PF} › Farrell, EuGH 2017"), ("stadt", f"{PF} › die Stadt: Gebietskörperschaft")], rechts_frei([
    *tafel("farrell", "Farrell und die Stadt"),
    z("Farrell, EuGH 2017:", 110, 185, "farrell", "Bold", 34),
    z("Eine Einrichtung muss nicht alle", 110, 240, beim("farrell", "Einrichtung"), size=34),
    z("diese Merkmale erfüllen.", 110, 290, beim("farrell", "Merkmale"), size=34),
    fund("Rs. C-413/15 (Farrell), Rn. 26, 28 f.; Tenor 1", 110, 345, beim("farrell", "Merkmale")),
    z("Für die Stadt braucht es die Formel nicht:", 110, 430, "stadt", "Bold", 34),
    fb(110, 495, 1040, 130, GRUEN, beim("stadt", "Gebietskörperschaften"),
       [("Gebietskörperschaften wie Städte und", "ExtraBold", 34, INK), ("Gemeinden gehören selbst zum Staat", "ExtraBold", 34, INK)]),
    fund("Foster, Rn. 19; Fuß I, Rn. 61; Farrell, Rn. 33", 110, 640, beim("stadt", "Gemeinden")),
    *einzeln("GO", "farrell", [("ruhig",), ("denkt", beim("farrell", "Merkmale")), ("staunt", "stadt"),
                               ("still", beim("stadt", "Gebietskörperschaften"))]),
    pl("nicht alle Merkmale nötig", XE, 250, beim("farrell", "Merkmale"), fill=HELL, size=28, anker="m", bis="stadt"),
    pl("Stadt = Staat", XE, 250, beim("stadt", "gehören"), fill=GRUEN, size=30, anker="m"),
]))

# K Keine Wirkung zwischen Privaten (Verweis Folge 138), richtlinienkonforme Auslegung -----------------------------------
folie([("priv", f"{PF} › nicht gegenüber Privaten"), ("rka", f"{PF} › bei Privaten: richtlinienkonforme Auslegung")],
      rechts_frei([
    *tafel("priv", "Und ein privater Arbeitgeber?"),
    nein(135, 210, beim("priv", "Privaten"), gr=18),
    z("zwischen Privaten keine unmittelbare Wirkung", 170, 190, beim("priv", "Privaten"), "Bold", 33),
    fund("Faccini Dori, Rs. C-91/92, Rn. 20, 25; Video „EU-Rechtsakte“", 170, 245, beim("priv", "Faccini")),
    fb(110, 330, 1040, 130, HELL, "rka", [("Dann bleibt: das deutsche Recht", "ExtraBold", 34, INK),
                                         ("richtlinienkonform auslegen", "ExtraBold", 34, INK)]),
    fund("Faccini Dori, Rn. 26", 110, 475, "rka"),
    ficon("tabler", "building-store", IX, 520, 220, "priv", fuell=HELL),
    pl("privater Arbeitgeber", IX, 540, "priv", fill=HELL, size=30, anker="m"),
    nein(IX, 640, beim("priv", "Privaten"), gr=30),
    pl("richtlinienkonform auslegen", IX, 200, "rka", fill=GELB, size=28, anker="m"),
]))

# L Lösung ---------------------------------------------------------------------------------------------------------------
PL_ = "Lösung"
folie([("loes1", f"{PL_} · Herr Ruppert gegen die Stadt"), ("folge", f"{PL_} · Rechtsfolge: Anwendungsvorrang")],
      rechts_frei([
    *tafel("loes1", "Lösung: Herr Ruppert gegen die Stadt"),
    ok(135, 200, "l1", gr=16), z("1. Frist abgelaufen", 165, 180, "l1", size=32),
    ok(135, 255, "l2", gr=16), z("2. nicht umgesetzt (Annahme)", 165, 235, "l2", size=32),
    ok(135, 310, "l3", gr=16), z("3. Art. 6 Buchst. b unbedingt und hinreichend genau", 165, 290, "l3", size=32),
    ok(135, 365, "l4", gr=16), z("4. Stadt gehört zum Staat, auch als Arbeitgeberin", 165, 345, "l4", size=32),
    fb(110, 410, 1040, 90, GRUEN, "l5", [("Unmittelbare Berufung auf die 48 Stunden", "ExtraBold", 33, INK)]),
    nein(135, 555, "folge", gr=16),
    z("Verordnung (54 Std.): nicht richtlinienkonform auslegbar", 165, 535, "folge", size=31),
    z("Stadt und jedes Gericht lassen sie insoweit unangewendet", 165, 590, "unang", "Bold", 31),
    fb(110, 650, 1040, 90, HELL, "vorr", [("Anwendungsvorrang: Video „Costa/ENEL“", "ExtraBold", 33, INK)]),
    fund("Fuß I, Rs. C-243/09, Rn. 60, 61, 63; Fuß II, Rs. C-429/09, Rn. 38–40", 110, 755, "vorr"),
    *paar("loes1", [("ruhig",), ("froh", "l5"), ("entschlossen", "unang")],
          [("ernst",), ("denkt", "l4"), ("still", "l5"), ("staunt", "unang")]),
]))

# M Der echte Fall Fuß und der neue Dienstplan (zurück in der Fahrzeughalle; die Geschichte kehrt dorthin zurück) -----------
folie([("fuss", "Lösung · Der echte Fall: Fuß, EuGH 2010"), ("g2", "Lösung · Der neue Dienstplan")], [
    *halle("fuss"),
    ficon("tabler", "door", 1815, BODEN, 100, "fuss", fuell=HOLZ),
    pl("Der echte Fall: EuGH, Urt. v. 14.10.2010 – C-243/09 (Fuß)", 980, 150, "fuss", fill=GELB, size=30, anker="m",
       bis="g2"),
    pl("Feuerwehrmann der Stadt Halle: unmittelbare Berufung auf", 980, 230, beim("fuss", "Feuerwehrmann"), fill=WEISS,
       size=28, anker="m", bis="g2"),
    pl("Art. 6 Buchst. b gegenüber seiner Stadt (Rn. 60)", 980, 295, beim("fuss", "Feuerwehrmann"), fill=WEISS, size=28,
       anker="m", bis="g2"),
    pl("Dienstplan: 54 Std.", 655, 578, "fuss", fill=ROTHELL, size=26, anker="m", bis=beim("g2", "Dienstplan")),
    szene(pl("Dienstplan: 48 Std.", 655, 578, beim("g2", "Dienstplan"), fill=GRUENHELL, size=26, anker="m"),
          "164stift*", 1.0, versatz=0.0),
    *stufen([("RU_ruhig_r", "fuss"), ("RU_froh_r", beim("fuss", "unmittelbar")), ("RU_ruhig_r", "g2"),
             ("RU_froh_r", beim("g2", "Dienstplan"))], RUX, BODEN, GH, erst="cut", ende="tipp"),
    namensschild(NAME["RU"], RUX, BODEN, "fuss", FARBE["RU"]),
    *stufen([("GO_still", "fuss"), ("GO_denkt", beim("fuss", "unmittelbar")), ("GO_einsicht", "g2")], GOX, BODEN, GH,
            rede={"GO_einsicht": 1}, erst="cut", ende="tipp"),
    namensschild(NAME["GO"], GOX, BODEN, "fuss", FARBE["GO"]),
    blase("sprech", 700, 190, "g2", 1100, 240, inhalt=["Dann müssen wir den", "Dienstplan ändern."], textsize=34, figur=GOb),
])

# N Klausurtipp (Lexi) ---------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · Wo prüfen?"), ("tf", "Klausurtipp · Typischer Fehler"),
       ("tf2", "Klausurtipp · Erst richtlinienkonform auslegen")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Prüfe die unmittelbare Wirkung dort,", 200, 200, "tipp", "Bold", 34),
    z("wo deutsches Recht dem Anspruch entgegensteht", 200, 250, beim("tipp", "wo"), "Bold", 34),
    nein(220, 365, "tf", gr=18),
    z("Typischer Fehler: die Stadt als Arbeitgeberin", 255, 345, "tf", size=33),
    z("wie einen Privaten behandeln", 255, 395, beim("tf", "wie"), size=33),
    fb(200, 480, 950, 180, GELB, "tf2", [("Vorher: richtlinienkonform auslegbar?", "ExtraBold", 32, INK),
                                       ("Dann brauchst du die unmittelbare", "ExtraBold", 32, INK),
                                       ("Wirkung nicht.", "ExtraBold", 32, INK)]),
    fund("Fuß II, Rs. C-429/09, Rn. 40", 200, 675, "tf2"),
    *redet("LX_warnt", LXX, BR, FR + 60, "tipp", "sch"),
    namensschild("Lexi", LXX, BR, "tipp", GELB, d=0.2),
])

# O Klausurschema ------------------------------------------------------------------------------------------------------------
PS_ = "Klausurschema"
FX = 1230                              # Fundstellen rechts
folie([("sch", PS_), ("z1", f"{PS_} › I. Umsetzungsfrist"), ("z2", f"{PS_} › II. keine ordnungsgemäße Umsetzung"),
       ("z3", f"{PS_} › III. unbedingt und hinreichend genau"), ("z4", f"{PS_} › IV. gegenüber dem Staat"),
       ("z5", f"{PS_} › Rechtsfolge")], [
    karte(60, 50, 1800, 900, "sch"),
    titel("Klausurschema: vertikale unmittelbare Wirkung", 110, 90, "sch", 48),
    z("I. Umsetzungsfrist abgelaufen", 110, 200, "z1", "Bold", 36, rechts=FX - 20),
    z("Ratti, Rn. 43", FX, 207, "z1", size=28, farbe=TEXT, rechts=1820),
    z("II. nicht oder nicht ordnungsgemäß umgesetzt", 110, 275, "z2", "Bold", 36, rechts=FX - 20),
    z("Fuß I, Rn. 56", FX, 282, "z2", size=28, farbe=TEXT, rechts=1820),
    z("III. inhaltlich unbedingt und hinreichend genau", 110, 350, "z3", "Bold", 36, rechts=FX - 20),
    z("Ratti, Rn. 23; Fuß I, Rn. 57–59", FX, 357, "z3", size=28, farbe=TEXT, rechts=1820),
    z("IV. gegenüber dem Staat", 110, 425, "z4", "Bold", 36, rechts=FX - 20),
    z("1. funktional verstanden", 170, 490, "z4a", size=34, rechts=FX - 20),
    z("Foster, Rn. 20; Farrell, Rn. 29", FX, 495, "z4a", size=28, farbe=TEXT, rechts=1820),
    z("2. auch als Arbeitgeber", 170, 550, "z4b", size=34, rechts=FX - 20),
    z("Marshall, Rn. 49", FX, 555, "z4b", size=28, farbe=TEXT, rechts=1820),
    z("3. nicht gegenüber Privaten", 170, 610, "z4c", size=34, rechts=FX - 20),
    z("Faccini Dori, Rn. 20, 25", FX, 615, "z4c", size=28, farbe=TEXT, rechts=1820),
    fb(110, 700, 1700, 130, GRUEN, "z5", [("Rechtsfolge: Die Bestimmung gilt unmittelbar, entgegenstehendes", "ExtraBold", 34, INK),
                                         ("deutsches Recht bleibt unangewendet (Fuß I, Rn. 63)", "ExtraBold", 34, INK)]),
])

# P Merksatz (Lexi) --------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Nach Fristablauf wirkt eine ", 0), ("unbedingte", "a")],
                 [("und hinreichend genaue", "a"), (" Richtlinie", 0)],
                 [("unmittelbar gegenüber dem Staat", "b"), (".", 0)]], 750, 300, 42, "merke",
                {"a": beim("merke", "unbedingte"), "b": beim("merke", "unmittelbar")}),
    *markertext([[("Und Staat ist auch", 0)],
                 [("die Stadt als Arbeitgeberin", "c"), (".", 0)]], 750, 600, 42, "m2", {"c": beim("m2", "Stadt")}),
    *redet("LX_erklaert", 1680, 960, 690, "merke", lexi_bis_ende("merke")),
    namensschild("Lexi", 1680, 960, "merke", GELB, d=0.2),
])
