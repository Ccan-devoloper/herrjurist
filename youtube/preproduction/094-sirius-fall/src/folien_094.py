"""Folge 094 · Sirius-Fall: Zur Selbsttötung überredet – mittelbare Täterschaft? – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A1 Gesprächsabend bei Hartwig, A2 Wilmas Wohnung am Abend (keine Methode, keine Verletzung;
Benedikt kommt herein, holt Hilfe; Wilma bleibt unverletzt), B Sachverhalt, C der echte Fall (BGHSt 32, 38; keine Figuren),
D Ausgangspunkt Straflosigkeit (§ 217 nichtig), E § 25 Abs. 1 (Wortlautkarte): Werkzeug gegen sich selbst, F Streit um den
Maßstab, G Täuschung über den Tod, H Subsumtion, I Versuch, J Ergebnis, K Klausurtipp (Lexi), L Klausurschema, M Merksatz
(Lexi), N Hilfsangebot (Telefonseelsorge, ruhige Tafel).
Geräusche nur bei sichtbarer Handlung: Tür, als Benedikt hereinkommt (Freesound CC0 440645).
Hilfsfunktionen (z, pl, tafel, wortlaut, fb, redet mit hörbarem Wortende …) wie in Folge 091, Kopie im eigenen Ordner."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont

bausteine.FIGORDNER = "op_094/"
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
NULL = ("fall", -round(bausteine._t("fall") + 0.4, 3))   # 0,4 s vor Hauptfilmbeginn: ab 0,0 s voll sichtbar

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
    """Wortlautkarte: wörtliches Zitat (gesetze-im-internet.de, Abruf 03.10.2026) in einer hellen Karte, Fundstelle darunter
    rechts. zeilen = Liste von Token-Listen [(text, Schlüssel|0)], hl = {Schlüssel: Cue} (Hervorhebung zum gesprochenen Wort)."""
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
    """Wie fl_block, aber Zeilenabstand passend zur Schriftgröße der Zeilen (fl_block rechnet mit 64 px, mehrzeilige Blöcke
    ragten sonst über den Rand)."""
    from engine import block
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


# --- Eigene Hilfsfunktion (wie Folge 068/071): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ----------------
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
XS = 1640                               # eine Figur allein neben der Tafel
IX = 1440                               # Requisit neben der Einzelfigur
X1, X2 = 1420, 1720                     # zwei Figuren
MB = (X1 + X2) // 2
FARBE = {"HW": LILA, "WI": GRUEN, "BE": BLAU}
NAME = {"HW": "Hartwig", "WI": "Wilma", "BE": "Benedikt"}


def kette(prefix, x, folge, bis_=None, d=0.0, hoehe=FR, unten=BR):
    """Eine Figur mit Mimikfolge [(Name, Cue), …] im Zwiebelschalenprinzip (erster Auftritt pop, danach harte Schnitte)."""
    els = []
    for i, (n, c) in enumerate(folge):
        b = folge[i + 1][1] if i + 1 < len(folge) else bis_
        els.append(peep_voll(prefix + n, x, unten, hoehe, c, anim=("pop" if i == 0 else "cut"), d=(d if i == 0 else 0.0), bis=b))
    return els


def allein(p, cue, folge, x=XS):
    """Eine Figur allein rechts neben der Tafel, mit Namensschild ab dem ersten Bild der Folie."""
    return kette(p + "_", x, [(folge[0][0], cue)] + list(folge[1:])) + [namensschild(NAME[p], x, BR, cue, FARBE[p], d=0.2)]


def paar(cue, p1, f1, p2, f2):
    els = kette(p1 + "_", X1, [(f1[0][0], cue)] + list(f1[1:])) + kette(p2 + "_", X2, [(f2[0][0], cue)] + list(f2[1:]), d=0.2)
    return els + [namensschild(NAME[p1], X1, BR, cue, FARBE[p1], d=0.2), namensschild(NAME[p2], X2, BR, cue, FARBE[p2], d=0.3)]


def stufen(folge, x, unten, hoehe, rede=None, erst="pop"):
    """Figur in der Fallszene: folge = [(Bildname, Cue), …]; rede = {Bildname: 1} für Figurenrede (bis zum nächsten Stand)."""
    els = []
    for i, (n, c) in enumerate(folge):
        b = folge[i + 1][1] if i + 1 < len(folge) else None
        if rede and n in rede:
            els += redet(n, x, unten, hoehe, c, b)
        else:
            els.append(peep_voll(n, x, unten, hoehe, c, anim=(erst if i == 0 and c != NULL else "cut"), bis=b))
    return els


# A1 Fall: der Gesprächsabend bei Hartwig ------------------------------------------------------------------------------------
BODEN, GH = 900, 520
HWX, WIX = 470, 1400
HWa = ("HW_redet_r", HWX, BODEN, GH)
WIa = ("WI_redet", WIX, BODEN, GH)
folie([(NULL, "Fall · Wilma und Hartwig"), ("stern", "Fall · Der ferne Stern"), ("h1", "Fall · Weiterleben?"),
       ("weiss", "Fall · Hartwig weiß es besser")], [
    linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK),
    pl("Wilma und Hartwig", 70, 40, NULL, fill=GELB, size=36, bis="h1"),
    ficon("tabler", "plant-2", 150, BODEN, 120, NULL, fuell=GRUEN),
    ficon("tabler", "lamp", 1760, BODEN, 150, NULL, fuell=GELB),
    ficon("tabler", "armchair", 930, BODEN, 230, NULL, fuell=LILA),
    *stufen([("HW_ruhig_r", NULL), ("HW_redet_r", "h1"), ("HW_ruhig_r", "w1"), ("HW_ernst_r", "weiss")], HWX, BODEN, GH,
            rede={"HW_redet_r": 1}),
    *stufen([("WI_ruhig", NULL), ("WI_vertraut", beim("lehrer", "Wilma")), ("WI_redet", "w1"), ("WI_vertraut", "weiss")],
            WIX, BODEN, GH, rede={"WI_redet": 1}),
    namensschild("Hartwig", HWX, BODEN, NULL, FARBE["HW"]),
    namensschild("Wilma", WIX, BODEN, NULL, FARBE["WI"]),
    pl("Mitte 30", WIX, 300, beim("fall", "Mitte"), fill=WEISS, size=30, anker="m", bis="stern"),
    pl("Gesprächsabende", 930, 560, beim("fall", "Gesprächsabende"), fill=WEISS, size=30, anker="m", bis="h1"),
    pl("„spiritueller Lehrer“", HWX, 300, beim("lehrer", "spiritueller"), fill=LILA, size=30, anker="m", bis="h1"),
    pl("vertraut ihm blind", WIX, 220, beim("lehrer", "vertraut"), fill=WEISS, size=30, anker="m", bis="h1"),
    ficon("tabler", "stars", 930, 330, 150, "stern", fuell=GELB, bis="h1"),
    pl("ein ferner Stern?", 930, 370, "stern", fill=GELB, size=30, anker="m", bis="h1"),
    pl("auserwählte Menschen weiterführen", 930, 450, beim("stern", "auserwählte"), fill=WEISS, size=28, anker="m", bis="h1"),
    # Figurenrede
    blase("sprech", 900, 260, "h1", 930, 200, inhalt=["Dein Körper hält dich zurück.", "Lässt du ihn hinter dir, wachst du sofort",
          "in einem höheren Körper auf und lebst weiter."], textsize=30, figur=HWa, bis="w1"),
    ficon("tabler", "sparkles", 1650, 330, 90, beim("h1", "höheren"), fuell=GELB, bis="weiss"),
    blase("sprech", 640, 220, "w1", 1120, 230, inhalt=["Sterben will ich nicht.", "Aber weiterleben, das schon."], textsize=32,
          figur=WIa, bis="weiss"),
    # Hartwig weiß, dass sie sterben würde
    pl("Er weiß: Sie wäre tot.", HWX, 300, "weiss", fill=ROTHELL, size=30, anker="m"),
    pl("und genau das will er", HWX, 220, beim("weiss", "genau"), fill=ROTHELL, size=30, anker="m"),
    ficon("tabler", "calendar-event", 930, 430, 100, "plan", fuell=WEISS),
    pl("legt alles fest, auch den Abend", 930, 470, "plan", fill=WEISS, size=28, anker="m"),
])

# A2 Fall: Wilmas Wohnung am verabredeten Abend (keine Methode, keine Verletzung) -------------------------------------------
WIX2, BEX = 1250, 560
folie([("abend", "Fall · Der verabredete Abend"), ("lebt", "Fall · Wilma bleibt unverletzt"), ("frage", "Fall · Die Frage")], [
    linienzug([(60, BODEN), (1860, BODEN)], "abend", breite=7, farbe=INK),
    ficon("tabler", "window", 1600, 380, 200, "abend", fuell=BLAUHELL, bis="frage"),
    ficon("tabler", "moon", 1600, 340, 70, "abend", fuell=GELB, bis="frage"),
    ficon("tabler", "lamp-2", 1760, BODEN, 150, "abend", fuell=GELB, bis="frage"),
    szene(ficon("tabler", "door", 220, BODEN, 220, beim("bruder", "Da"), fuell=WEISS), "094tuer*", 1.0, versatz=0.05),
    pl("der verabredete Abend", 930, 450, "abend", fill=WEISS, size=30, anker="m", bis="lebt"),
    pl("beginnt, den Plan umzusetzen", WIX2, 250, beim("abend", "beginnt"), fill=WEISS, size=28, anker="m", bis="b1"),
    *stufen([("WI_ernst", "abend"), ("WI_still", "b1"), ("WI_ruhig", "lebt")], WIX2, BODEN, GH),
    namensschild("Wilma", WIX2, BODEN, "abend", FARBE["WI"], d=0.2),
    *stufen([("BE_sorge_r", beim("bruder", "Benedikt")), ("BE_redet_r", "b1"), ("BE_ruhig_r", "lebt")], BEX, BODEN, GH,
            rede={"BE_redet_r": 1}),
    namensschild("Benedikt", BEX, BODEN, beim("bruder", "Benedikt"), FARBE["BE"], d=0.2),
    pl("ihr Bruder, unerwartet", BEX, 250, beim("bruder", "unerwartet"), fill=BLAU, size=28, anker="m", bis="b1"),
    blase("sprech", 520, 170, "b1", 860, 220, inhalt=["Wilma, hör auf!", "Ich hole Hilfe."], textsize=34,
          figur=("BE_redet_r", BEX, BODEN, GH), bis="lebt"),
    ficon("tabler", "phone-call", 760, 600, 80, beim("b1", "Hilfe"), fuell=GRUEN, bis="frage"),
    ficon("tabler", "heart", WIX2, 300, 90, "lebt", fuell=GRUEN, bis="frage"),
    pl("Wilma bleibt unverletzt.", WIX2, 160, "lebt", fill=GRUEN, size=32, anker="m", bis="frage"),
    # Die Frage: Hartwig im Bild
    *kette("HW_", 1640, [("ernst", "frage")], hoehe=GH, unten=BODEN),
    namensschild("Hartwig", 1640, BODEN, "frage", FARBE["HW"], d=0.2),
    pl("Teilnahme an Selbsttötung: grundsätzlich straflos", 930, 110, "frage", fill=WEISS, size=30, anker="m"),
    pl("Hartwig also straflos?", 1480, 190, beim("frage", "Ist"), fill=WEISS, size=32, anker="m"),
    pl("oder versuchte Tötung durch Wilma selbst?", 900, 270, "frage2", fill=PINK, size=32, anker="m"),
])

# B Sachverhalt -------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    glyphen("Wilma (Mitte 30) vertraut seit Jahren Hartwig, der sich spiritueller Lehrer nennt. Er erzählt ihr, er stamme von "
            "einem fernen Stern, und redet ihr ein: Lasse sie ihren Körper hinter sich, wache sie sofort in einem höheren Körper "
            "auf und lebe weiter. Sterben will Wilma nicht; sie glaubt ihm."),
    glyphen("Hartwig weiß, dass sie sterben würde, und will genau das. Er legt alles fest, auch den Abend. Am verabredeten "
            "Abend beginnt Wilma, den Plan umzusetzen. Ihr Bruder Benedikt kommt unerwartet dazu, hält sie auf und holt Hilfe. "
            "Wilma bleibt unverletzt."),
    glyphen("Vorbild: BGHSt 32, 38 (Sirius-Fall), abgewandelt."),
], "Wie hat sich Hartwig strafbar gemacht?")

# C Der echte Fall (keine Figuren: reale Beteiligte werden nicht dargestellt) ------------------------------------------------
folie([("echt", "Der echte Fall · Sirius-Fall, BGHSt 32, 38"), ("echt3", "Der echte Fall › Verurteilung bestätigt")], rechts_frei([
    *tafel("echt", "Der Sirius-Fall"),
    z("BGH, Urteil vom 5.7.1983", 110, 185, beim("echt", "Bundesgerichtshof"), "Bold", 34),
    fund("1 StR 168/83, BGHSt 32, 38", 110, 235, beim("echt", "Urteil")),
    z("eingeredet: Er stamme vom Stern Sirius,", 110, 310, "echt2", size=32),
    z("sie werde in einem neuen Körper weiterleben", 110, 357, beim("echt2", "sie"), size=32),
    z("zuvor: Lebensversicherung zu seinen Gunsten", 110, 432, "vers", size=32),
    ok(135, 527, "echt3", gr=18),
    z("auch sie überlebte", 175, 507, "echt3", "Bold", 32),
    fb(110, 575, 1040, 90, GELB, beim("echt3", "Der"), [("BGH: versuchter Mord aus Habgier bestätigt", "ExtraBold", 32, INK)]),
    z("Unser Fall ist abgewandelt.", 110, 700, "abgew", size=32, farbe=TEXT),
    ficon("tabler", "stars", 1580, 400, 180, "echt", fuell=GELB, bis="vers"),
    pl("Sirius-Fall", 1580, 160, beim("echt", "Sirius-Fall"), fill=GELB, size=32, anker="m", bis="vers"),
    pl("Lebensversicherung", 1580, 160, "vers", fill=WEISS, size=30, anker="m", anim="cut", bis="echt3"),
    ficon("tabler", "file-certificate", 1580, 400, 160, "vers", fuell=WEISS, anim="cut", bis="echt3"),
    ficon("tabler", "heart", 1480, 400, 120, "echt3", fuell=GRUEN, anim="cut"),
    ficon("tabler", "gavel", 1690, 400, 130, beim("echt3", "bestätigte"), fuell=HOLZ),
    pl("versuchter Mord", 1580, 160, beim("echt3", "bestätigte"), fill=GRUEN, size=30, anker="m"),
]))

# D Ausgangspunkt: Straflosigkeit ---------------------------------------------------------------------------------------------
PA = "A. Hartwig"
folie([("aus", "Ausgangspunkt · Selbsttötung straflos"), ("akz", "Ausgangspunkt › Teilnahme mangels Haupttat straflos"),
       ("p217", "Ausgangspunkt › § 217 StGB nichtig"), ("f058", "Ausgangspunkt › vgl. Folge 058")], rechts_frei([
    *tafel("aus", "Ausgangspunkt"),
    z("eigenverantwortliche Selbsttötung:", 110, 185, beim("aus", "Eine"), "Bold", 34),
    z("kein Tatbestand eines Tötungsdelikts", 110, 235, beim("aus", "Tatbestand"), size=32),
    fund("BGHSt 64, 121 Rn. 17", 110, 282, beim("aus", "Tötungsdelikts")),
    z("Anstiftung, Beihilfe: rechtswidrige Haupttat nötig", 110, 350, "akz", "Bold", 32),
    fund("§§ 26, 27 StGB", 110, 397, beim("akz", "Haupttat")),
    nein(135, 465, beim("akz", "Fehlt"), gr=18),
    z("fehlt sie: auch die Teilnahme straflos", 175, 445, beim("akz", "Fehlt"), size=32),
    z("§ 217 StGB (geschäftsmäßige Förderung): nichtig", 110, 530, "p217", "Bold", 32),
    fund("BVerfG, Urt. v. 26.2.2020 – 2 BvR 2347/15, Rn. 337", 110, 577, beim("p217", "nichtig")),
    fb(110, 645, 1040, 140, GELB, "f058", [("Folge 058: Wer eine eigenverantwortliche", "ExtraBold", 31, INK),
                                         ("Selbstgefährdung nur ermöglicht, tötet nicht.", "ExtraBold", 31, INK)]),
    *paar("aus", "HW", [("ernst",), ("still", "p217")], "WI", [("ruhig",), ("vertraut", "f058")]),
    pl("Selbsttötung: straflos", MB, 160, beim("aus", "Eine"), fill=WEISS, size=28, anker="m", bis="akz"),
    pl("Teilnahme: straflos", MB, 160, "akz", fill=WEISS, size=28, anker="m", anim="cut", bis="p217"),
    pl("§ 217 StGB: nichtig", MB, 160, "p217", fill=GELB, size=28, anker="m", anim="cut", bis="f058"),
    pl("vgl. Folge 058", MB, 160, "f058", fill=GELB, size=28, anker="m", anim="cut"),
]))

# E § 25 Abs. 1: Werkzeug gegen sich selbst --------------------------------------------------------------------------------
W25 = [[("„(1) Als Täter wird bestraft, wer die Straftat selbst", 0)],
       [("oder ", 0), ("durch einen anderen", "a"), (" begeht.“", 0)]]
folie([("hand", f"{PA} › Täter durch einen anderen?"), ("p25", f"{PA} › § 25 Abs. 1 Alt. 2 StGB"),
       ("werkz", f"{PA} › Werkzeug gegen sich selbst"), ("unfrei", f"{PA} › Opfer handelt unfrei?")], rechts_frei([
    *tafel("hand", "Täter durch einen anderen"),
    nein(135, 205, "hand", gr=18),
    z("Tat nicht selbst ausgeführt", 175, 185, "hand", "Bold", 32),
    *wortlaut(110, 260, 1040, 130, "p25", W25, 32, {"a": beim("p25", "durch")}, "§ 25 Abs. 1 StGB"),
    z("der andere: auch das Opfer selbst", 110, 460, "werkz", "Bold", 34),
    z("Werkzeug gegen sich selbst", 110, 510, beim("werkz", "Werkzeug"), size=32),
    fb(110, 590, 1040, 140, GELB, "unfrei", [("Voraussetzung: Opfer handelt unfrei,", "ExtraBold", 32, INK),
                                           ("Wissens- oder Verantwortlichkeitsdefizit", "ExtraBold", 32, INK)]),
    fund("BGHSt 64, 121 Rn. 20 mit BGHSt 32, 38, 41 f.", 110, 745, beim("unfrei", "Verantwortlichkeitsdefizit")),
    *paar("hand", "HW", [("ernst",), ("still", "unfrei")], "WI", [("ruhig",), ("still", "werkz")]),
    pl("selbst ausgeführt? nein", MB, 160, "hand", fill=WEISS, size=28, anker="m", bis="p25"),
    pl("durch einen anderen", MB, 160, beim("p25", "durch"), fill=GELB, size=30, anker="m", anim="cut", bis="werkz"),
    pl("Werkzeug gegen sich selbst", MB, 160, "werkz", fill=WEISS, size=28, anker="m", anim="cut", bis="unfrei"),
    pl("unfrei?", MB, 160, "unfrei", fill=GELB, size=30, anker="m", anim="cut"),
]))

# F Maßstab: der Streit ------------------------------------------------------------------------------------------------------
folie([("streit", f"{PA} › Unfrei? › der Maßstab"), ("exk", f"{PA} › Unfrei? › Exkulpationslösung"),
       ("einw", f"{PA} › Unfrei? › Einwilligungslösung"), ("bgh", f"{PA} › Unfrei? › BGH: Freiverantwortlichkeit"),
       ("mangel", f"{PA} › Unfrei? › Täuschung")], rechts_frei([
    *tafel("streit", "Wann ist der Entschluss nicht frei?"),
    karte(110, 175, 1040, 135, "exk", fill=LILAHELL, rund=18, schatten=6, rand=4),
    z("Exkulpationslösung: Zustand entsprechend", 140, 190, "exk", "Bold", 31, rechts=1140),
    z("§§ 19, 20, 35 StGB, der Verantwortung ausschließt?", 140, 240, beim("exk", "Paragrafen"), size=31, rechts=1140),
    karte(110, 330, 1040, 135, "einw", fill=BLAUHELL, rund=18, schatten=6, rand=4),
    z("Einwilligungslösung: höhere Anforderungen,", 140, 345, "einw", "Bold", 31, rechts=1140),
    z("so frei und ernstlich wie eine Einwilligung", 140, 395, beim("einw", "Der"), size=31, rechts=1140),
    karte(110, 485, 1040, 135, "bgh", fill=GRUENHELL, rund=18, schatten=6, rand=4),
    z("BGH: Einsichts- und Urteilsfähigkeit,", 140, 500, "bgh", "Bold", 31, rechts=1140),
    z("mangelfreier Wille, fester Entschluss", 140, 550, beim("bgh", "mangelfreien"), size=31, rechts=1140),
    fb(110, 645, 1040, 90, GELB, "mangel", [("mangelhaft bei Zwang, Drohung, Täuschung", "ExtraBold", 32, INK)]),
    fund("BGHSt 64, 121 Rn. 21, 25; BGHSt 32, 38, 43", 110, 750, beim("mangel", "Täuschung")),
    *allein("WI", "streit", [("ernst",), ("still", "mangel")]),
    pl("frei entschieden?", IX + 40, 160, "streit", fill=WEISS, size=30, anker="m", bis="exk"),
    pl("Exkulpationslösung", IX + 40, 160, "exk", fill=LILA, size=28, anker="m", anim="cut", bis="einw"),
    pl("Einwilligungslösung", IX + 40, 160, "einw", fill=BLAU, size=28, anker="m", anim="cut", bis="bgh"),
    pl("BGH", IX + 40, 160, "bgh", fill=GRUEN, size=30, anker="m", anim="cut", bis="mangel"),
    pl("Täuschung", IX + 40, 160, "mangel", fill=GELB, size=30, anker="m", anim="cut"),
    ficon("tabler", "help-circle", IX - 60, 400, 90, "streit", fuell=WEISS, bis="mangel"),
    ficon("tabler", "masks-theater", IX - 60, 400, 110, "mangel", fuell=WEISS, anim="cut"),
]))

# G Täuschung über den Tod ---------------------------------------------------------------------------------------------------
folie([("art", f"{PA} › Täuschung über den Tod"), ("verschl", f"{PA} › Täter kraft überlegenen Wissens"),
       ("f091", f"{PA} › vgl. Folge 091 (Katzenkönig)")], rechts_frei([
    *tafel("art", "Täuschung: Art und Tragweite"),
    z("BGH: Es kommt auf Art und Tragweite", 110, 185, beim("art", "Art"), "Bold", 34),
    z("des Irrtums an", 110, 235, beim("art", "Irrtums"), "Bold", 34),
    z("verschleiert: Ursache für den eigenen Tod?", 110, 315, "verschl", size=32),
    ok(135, 405, beim("verschl", "Täter"), gr=18),
    z("dann Täter kraft überlegenen Wissens", 175, 385, beim("verschl", "Täter"), "Bold", 32),
    fb(110, 460, 1040, 90, GRUEN, "selbst", [("das Opfer als Werkzeug gegen sich selbst", "ExtraBold", 32, INK)]),
    fund("BGHSt 32, 38 (Sirius-Fall)", 110, 565, beim("selbst", "Werkzeug")),
    z("wie Folge 091 (Katzenkönig): überlegenes Wissen", 110, 640, "f091", size=32),
    z("hier ist das Werkzeug das Opfer selbst", 110, 690, beim("f091", "Nur"), "Bold", 32),
    *paar("art", "HW", [("ernst",), ("still", "f091")], "WI", [("vertraut",), ("still", "f091")]),
    pl("Art und Tragweite", MB, 160, beim("art", "Art"), fill=WEISS, size=30, anker="m", bis="verschl"),
    pl("überlegenes Wissen", MB, 160, beim("verschl", "Täter"), fill=GRUEN, size=30, anker="m", bis="f091"),
    ficon("tabler", "bulb", MB, 380, 100, beim("verschl", "Täter"), fuell=GELB, bis="f091"),
    pl("vgl. Folge 091", MB, 160, "f091", fill=GELB, size=30, anker="m", anim="cut"),
]))

# H Subsumtion ---------------------------------------------------------------------------------------------------------------
folie([("subs", f"{PA} › Subsumtion › Irrtum über den Tod"), ("beide", f"{PA} › Subsumtion › beide Ansichten: unfrei"),
       ("herr", f"{PA} › Subsumtion › Tatherrschaft")], rechts_frei([
    *tafel("subs", "So liegt es hier"),
    ok(135, 205, beim("subs", "Wilma"), gr=18),
    z("Wilma will nicht sterben", 175, 185, beim("subs", "Wilma"), "Bold", 32),
    ok(135, 275, "glaubt", gr=18),
    z("glaubt, sie lebe sofort weiter:", 175, 255, "glaubt", "Bold", 32),
    z("Irrtum über den Tod selbst", 175, 302, beim("glaubt", "irrt"), size=32),
    fb(110, 375, 1040, 140, GELB, "beide", [("keine Entscheidung über den Tod:", "ExtraBold", 32, INK),
                                          ("beide Ansichten: unfrei", "ExtraBold", 32, INK)]),
    ok(135, 570, "herr", gr=18),
    z("Hartwig: Irrtum erzeugt, Gefahr gekannt,", 175, 550, "herr", "Bold", 32),
    z("Geschehen gesteuert: Tatherrschaft", 175, 597, beim("herr", "steuert"), "Bold", 32),
    z("unglaubhafte Geschichte entlastet nicht", 110, 680, "unglaub", size=32),
    fund("BGHSt 32, 38 (Sirius-Fall)", 110, 727, beim("unglaub", "B.G.H")),
    *paar("subs", "HW", [("ernst",), ("still", "herr")], "WI", [("still",), ("vertraut", "glaubt"), ("still", "beide")]),
    pl("will nicht sterben", MB, 160, beim("subs", "Wilma"), fill=WEISS, size=30, anker="m", bis="glaubt"),
    pl("Irrtum über den Tod", MB, 160, "glaubt", fill=ROTHELL, size=30, anker="m", anim="cut", bis="herr"),
    pl("Tatherrschaft", MB, 160, "herr", fill=GRUEN, size=30, anker="m", anim="cut"),
]))

# I Versuch -------------------------------------------------------------------------------------------------------------------
folie([("versuch", f"{PA} › Versuch"), ("entschl", f"{PA} › Versuch › Tatentschluss"),
       ("ansetz", f"{PA} › Versuch › unmittelbares Ansetzen"), ("rt", f"{PA} › Versuch › Rücktritt")], rechts_frei([
    *tafel("versuch", "Versuch"),
    z("Wilma lebt: Versuch", 110, 185, "versuch", "Bold", 34),
    fund("§§ 212, 22, 23 Abs. 1 StGB", 110, 235, beim("versuch", "Versuch")),
    ok(135, 325, "entschl", gr=18),
    z("Tatentschluss: Tod gewollt,", 175, 305, "entschl", "Bold", 32),
    z("Steuerung des Geschehens gewusst", 175, 352, beim("entschl", "wusste"), size=32),
    ok(135, 445, "ansetz", gr=18),
    z("unmittelbares Ansetzen: jedenfalls, als", 175, 425, "ansetz", "Bold", 32),
    z("Wilma beginnt, den Plan umzusetzen", 175, 472, beim("ansetz", "Wilma"), size=32),
    z("früherer Beginn beim Hintermann: umstritten", 175, 530, beim("ansetz", "Ob"), size=30, farbe=TEXT),
    nein(135, 625, "rt", gr=18),
    z("Rücktritt: nein, Benedikt hielt sie auf", 175, 605, "rt", "Bold", 32),
    fund("§ 24 Abs. 1 StGB", 175, 652, beim("rt", "Benedikt")),
    *allein("HW", "versuch", [("ernst",), ("still", "rt")]),
    pl("Versuch", IX + 40, 160, "versuch", fill=WEISS, size=30, anker="m", bis="entschl"),
    pl("Tatentschluss", IX + 40, 160, "entschl", fill=WEISS, size=30, anker="m", anim="cut", bis="ansetz"),
    pl("Ansetzen", IX + 40, 160, "ansetz", fill=WEISS, size=30, anker="m", anim="cut", bis="rt"),
    pl("kein Rücktritt", IX + 40, 160, "rt", fill=ROTHELL, size=30, anker="m", anim="cut"),
    ficon("tabler", "heart", IX - 20, 400, 90, "versuch", fuell=GRUEN, bis="rt"),
    ficon("tabler", "hand-stop", IX - 20, 400, 100, "rt", fuell=WEISS, anim="cut"),
]))

# J Ergebnis -----------------------------------------------------------------------------------------------------------------
folie([("erg", "Ergebnis · versuchter Totschlag in mittelbarer Täterschaft"), ("mord", "Ergebnis › Mordmerkmal?")], rechts_frei([
    *tafel("erg", "Ergebnis"),
    fb(110, 190, 1040, 140, GRUEN, "erg", [("Hartwig: versuchter Totschlag", "ExtraBold", 32, INK),
                                         ("in mittelbarer Täterschaft", "ExtraBold", 32, INK)]),
    fund("§§ 212, 22, 23 Abs. 1, 25 Abs. 1 Alt. 2 StGB", 110, 345, beim("erg", "Paragrafen")),
    fb(110, 430, 1040, 140, BLAUHELL, "mord", [("Mord nur mit Mordmerkmal,", "ExtraBold", 32, INK),
                                             ("im echten Fall: Habgier", "ExtraBold", 32, INK)]),
    fund("§ 211 Abs. 2 StGB", 110, 585, beim("mord", "Mordmerkmal")),
    z("dazu sagt unser Fall nichts", 110, 650, beim("mord", "Dazu"), size=32, farbe=TEXT),
    *paar("erg", "HW", [("still",)], "WI", [("ruhig",)]),
    ficon("tabler", "gavel", MB, 380, 120, beim("erg", "Ergebnis"), fuell=HOLZ),
]))

# K Klausurtipp (Lexi) -----------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · zuerst die mittelbare Täterschaft"), ("tipp2", "Klausurtipp · Streit nur, wenn es darauf ankommt")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Beim Hintermann zuerst das Tötungsdelikt", 200, 200, "tipp", "Bold", 34),
    z("in mittelbarer Täterschaft,", 200, 250, beim("tipp", "in"), size=34),
    z("nicht die Teilnahme", 200, 300, beim("tipp", "nicht"), size=34),
    z("Streit um den Maßstab nur entscheiden,", 200, 390, "tipp2", "Bold", 34),
    z("wenn die Ansichten auseinandergehen", 200, 440, beim("tipp2", "wenn"), size=34),
    z("Täuschung über den Tod selbst:", 200, 530, "tipp3", "Bold", 34),
    z("beide Ansichten gleich", 200, 580, beim("tipp3", "tun"), size=34),
    *redet("LX_warnt", LXX, BR, FR + 60, "tipp", "sch"),
    namensschild("Lexi", LXX, BR, "tipp", GELB, d=0.2),
])

# L Klausurschema ------------------------------------------------------------------------------------------------------------
K1, K2 = 150, 230
PS_ = "Klausurschema"
folie([("sch", PS_), ("s0", f"{PS_} › Vorprüfung"), ("s1", f"{PS_} › 1. Tatentschluss"), ("s1a", f"{PS_} › 1. Opfer unfrei?"),
       ("s2", f"{PS_} › 2. unmittelbares Ansetzen"), ("s3", f"{PS_} › 3. Rechtswidrigkeit"), ("s4", f"{PS_} › 4. Schuld"),
       ("s5", f"{PS_} › Rücktritt")], [
    karte(60, 50, 1800, 920, "sch"),
    titel("Klausurschema: Sirius-Fall", 110, 90, "sch", 50),
    z("Hartwig: versuchter Totschlag in mittelbarer Täterschaft,", K1, 180, beim("sch", "versuchten"), "Bold", 34, rechts=1820),
    z("§§ 212, 22, 23 Abs. 1, 25 Abs. 1 Alt. 2 StGB", K1, 230, beim("sch", "mittelbarer"), size=32, rechts=1820),
    z("Vorprüfung: nicht vollendet, Versuch strafbar", K1, 300, "s0", size=32, rechts=1820),
    z("1. Tatentschluss: Vorsatz zur Tötung und zur Tatherrschaft über das Werkzeug", K1, 370, "s1", "Bold", 32, rechts=1820),
    z("Opfer unfrei?", K2, 425, "s1a", size=32, rechts=1820),
    z("Streit um den Maßstab · Täuschung über den Tod", K2, 475, "s1b", size=32, rechts=1820),
    z("2. unmittelbares Ansetzen", K1, 545, "s2", "Bold", 32, rechts=1820),
    z("3. Rechtswidrigkeit", K1, 605, "s3", "Bold", 32, rechts=1820),
    z("4. Schuld", K1, 665, "s4", "Bold", 32, rechts=1820),
    z("dann: Rücktritt, § 24 StGB", K1, 725, "s5", "Bold", 32, rechts=1820),
])

# M Merksatz (Lexi) --------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Die Teilnahme an einer freien", 0)], [("Selbsttötung ist ", 0), ("straflos", "a"), (".", 0)]],
                750, 300, 42, "merke", {"a": beim("merke", "straflos")}),
    *markertext([[("Wer aber das Opfer über den Tod", 0)], [("selbst täuscht, tötet ", 0), ("durch das Opfer", "b"), (",", 0)],
                 [("als ", 0), ("mittelbarer Täter", "c"), (".", 0)]], 750, 500, 40, "m2",
                {"b": beim("m2", "durch"), "c": beim("m2", "mittelbarer")}),
    *redet("LX_erklaert", 1680, 960, 690, "merke", "hilfe"),
    namensschild("Lexi", 1680, 960, "merke", GELB, d=0.2),
])

# N Hilfsangebot (ruhige Tafel, Nummern verifiziert auf telefonseelsorge.de, Abruf 03.10.2026) -------------------------------
folie([("hilfe", "Hilfsangebot")], [
    karte(160, 140, 1600, 760, "hilfe", fill=BLAUHELL),
    titel("Wenn dich das Thema selbst betrifft", 960, 200, "hilfe", 50, anker="m"),
    z("Die TelefonSeelsorge ist rund um die Uhr", 260, 320, beim("hilfe", "Die"), "Bold", 36, rechts=1700),
    z("und kostenlos für dich da.", 260, 375, beim("hilfe", "kostenlos"), "Bold", 36, rechts=1700),
    ficon("tabler", "phone-call", 1520, 470, 150, beim("hilfe", "Die"), fuell=GRUEN),
    z("0800 111 0 111", 260, 480, "nummern", "ExtraBold", 56, rechts=1700),
    z("0800 111 0 222", 260, 570, "nummern", "ExtraBold", 56, rechts=1700),
    z("telefonseelsorge.de", 260, 680, "nummern", size=32, farbe=TEXT, rechts=1700),
])
