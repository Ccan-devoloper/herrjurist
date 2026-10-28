"""Folge 221 · Beweisverwertungsverbote StPO: Das System – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A Fall 1 Vernehmungsraum (Drohung, Geständnis), B Fall 2 Straße (Kratzen, Frage ohne
Belehrung, Geständnis) und B2 Hauptverhandlung (Widerspruch), C Fall 3 Wohnungstür (Durchsuchung ohne Beschluss, Laptops),
D drei Ziffern-Kacheln und Frage, E Sachverhalt, F Erhebungs- vs. Verwertungsverbot, G erste Gruppe (unselbständig/
selbständig), H § 136a Abs. 3 S. 2, I § 252, J § 100d Abs. 2, K § 479 Abs. 2 i. V. m. § 161 Abs. 3, L zweite Gruppe
(Abwägungslehre), M Rechtskreistheorie und Widerspruchslösung, N Reichweite (Fernwirkung, Fortwirkung), O–Q Lösung der drei
Fälle, R Klausurtipp mit Prüfungsschema (Lexi), S Merksatz (Lexi).
Geräusche nur bei sichtbarer Handlung: Kratzen am Lack (Fall 2), Wohnungstür geht auf (Fall 3), Freesound CC0.
Hilfsfunktionen glyphen/z/pl/fb/tafel/wortlaut/redet/namensschild als eigene Kopie aus Folge 171 (gemeinsame Dateien
unverändert). Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlautkarten wörtlich nach gesetze-im-internet.de
(Abruf 07.10.2026)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont

bausteine.FIGORDNER = "op_221/"

_run0 = bausteine._sp.run


def _run_c(args, **k):
    """Sprechblasen müssen im Stil C gelingen (kein stiller Rückfall auf Stil E)."""
    r = _run0(args, **k)
    if len(args) > 1 and str(args[1]).endswith("blase_c.js"):
        assert r.returncode == 0, f"Blase Stil C fehlgeschlagen: {args[2]}"
    return r


bausteine._sp.run = _run_c

FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
ROTHELL = (253, 232, 228, 255)
GRUENHELL = (232, 247, 233, 255)
BLAUHELL = (232, 240, 253, 255)
HOLZ = (214, 160, 110, 255)
GRAU = (225, 225, 230, 255)
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


def fb(x, y, w, h, fill, cue, zeilen, **k):
    for t, s, g, _ in zeilen:
        glyphen(t)
        assert F(s, g).getlength(t) <= w - 30, f"Blockzeile zu breit: {t}"
    # Zeilenabstand nach der tatsächlichen Schriftgröße (fl_block rechnet mit textsize 64)
    return block(x, y, w, h, fill, None, cue, textsize=max(g for _, _, g, _ in zeilen), rund=k.pop("rund", 18), rand=INK,
                 randbreite=5, anim=k.pop("anim", "rise"), d=k.pop("d", 0.0), bis=k.pop("bis", None), zeilen=zeilen)


def tafel(cue, titel_, h=840, fill=WEISS, size=46):
    """Rechtstafel links, rechts bleibt Platz für die Figuren."""
    assert 110 + F("ExtraBold", size).getlength(glyphen(titel_)) <= 1170, f"Titel zu breit: {titel_}"
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(titel_, 110, 100, cue, size)]


def wortlaut(x, y, w, h, cue, zeilen, size, hl, quelle, quelle_cue=None):
    """Wortlautkarte: wörtliches Zitat (gesetze-im-internet.de, Abruf 07.10.2026) in einer hellen Karte, Fundstelle
    darunter rechts. zeilen = Liste von Token-Listen [(text, Schlüssel|0)], hl = {Schlüssel: Cue}."""
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


def lexi_bis_ende(cue):
    return (cue, round(DAUER - bausteine._t(cue) - 0.05, 3))


def rechts_frei(els, x0=1250):
    """Figuren und Requisiten der Tafelfolien stehen rechts der Tafel (x ≥ 1250)."""
    for e in els:
        n = e.name or ""
        if n.startswith(("bild:", "ficon:")) or "/op_221/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def namensschild(text, cx, unten, cue, fill, **k):
    return pille(glyphen(text), cx, unten + 22, cue, fill=fill, size=30, anker="m", **k)


def hart(e):
    e.anim = "cut"
    return e


def fund(text, x, y, cue, rechts=1170):
    return z(text, x, y, cue, size=26, farbe=TEXT, rechts=rechts)


# --- Eigene Hilfsfunktion (wie Folge 171): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ---------------
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


BODEN, FH = 880, 480
BR, FR = 930, 480                       # Figuren rechts neben der Tafel
X1, X2 = 1390, 1730                     # zwei Figuren neben der Tafel
MB = (X1 + X2) // 2
SH = 0.74                               # Herr Kleinert sitzt: Bildhöhe relativ zu stehenden Figuren


def hocker(name, cx, unten, hoehe, cue, **k):
    """Hocker (Baustein karte, Holz) unter dem Gesäß der sitzenden Figur; Lage aus der Figurensilhouette."""
    e = peep_voll(name, cx, unten, hoehe, "_")
    links = name.endswith("_r") or "_r_" in name          # _r blickt nach rechts: Gesäß links
    w = int(e.sprite.width * 0.40); h = int(e.sprite.height * 0.33)
    x = e.x + (int(e.sprite.width * 0.02) if links else e.sprite.width - w - int(e.sprite.width * 0.02))
    return hart(karte(x, unten - h, w, h - 4, cue, fill=HOLZ, rund=8, schatten=4, rand=4)) if k.get("cut", True) else \
        karte(x, unten - h, w, h - 4, cue, fill=HOLZ, rund=8, schatten=4, rand=4)


def hand(name, cx, unten, hoehe, seite):
    """Position der ausgestreckten Hand (äußerster Pixel links/rechts im oberen Körperdrittel) für ein Requisit."""
    e = peep_voll(name, cx, unten, hoehe, "_")
    a = np.asarray(e.sprite)[:, :, 3] > 20
    h = a.shape[0]
    band = a[int(h * 0.25):int(h * 0.62)]
    ys, xs = np.nonzero(band)
    x = xs.min() if seite < 0 else xs.max()
    y = int(np.median(ys[xs == x])) + int(h * 0.25)
    return e.x + x, e.y + y


def kachel_nr(nr, x, y, cue, fill=GELB, **k):
    """Ziffern-Kachel (Fallnummer) als runde Pille."""
    return pl(str(nr), x, y, cue, fill=fill, size=44, **k)


# A Fall 1: Vernehmungsraum ------------------------------------------------------------------------------------------------
KOX, KLX = 640, 1260                    # Kommissar (blickt nach rechts), Herr Kleinert (sitzt, blickt nach links)
KLH = int(FH * SH)
KOa = ("KO_redet_r", KOX, BODEN, FH)
folie([(NULL, "Fall · Drei Ermittlungsfehler"), ("f1", "Fall 1 · Im Vernehmungsraum"), ("verd", "Fall 1 · Verdacht: Kioskeinbruch"),
       ("k1", "Fall 1 · Der Kommissar droht"), ("ges1", "Fall 1 · Das Geständnis")], [
    hart(linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK)),
    pl("Drei Ermittlungsfehler", 70, 40, NULL, fill=GELB, size=40, anim="cut", bis="f1"),
    kachel_nr(1, 70, 40, "f1", anim="cut"),
    pl("Vernehmungsraum", 170, 40, "f1", fill=GELB, size=40, anim="cut"),
    hart(karte(820, BODEN - 200, 240, 198, NULL, fill=GRAU, rund=10, schatten=6)),          # Tisch
    ficon("tabler", "lamp", 940, BODEN - 200, 110, NULL, fuell=GELB, anim="cut"),
    hocker("KL_ruhig", KLX, BODEN, KLH, NULL),
    peep_voll("KL_ruhig", KLX, BODEN, KLH, NULL, anim="cut", bis="ungeduld"),
    peep_voll("KL_sorge", KLX, BODEN, KLH, "ungeduld", anim="cut", bis="ges1"),
    peep_voll("KL_angst", KLX, BODEN, KLH, "ges1", anim="cut"),
    namensschild("Herr Kleinert", KLX, BODEN, NULL, GELB, anim="cut"),
    ficon("tabler", "building-store", 1620, 420, 150, "verd", fuell=BLAU, bis="ges1"),
    pl("Verdacht: Einbruch in einen Kiosk", 1600, 470, beim("verd", "Kiosk"), fill=WEISS, size=28, anker="m", bis="ges1"),
    peep_voll("KO_ruhig_r", KOX, BODEN, FH, "f1", bis="ungeduld"),
    peep_voll("KO_denkt_r", KOX, BODEN, FH, "ungeduld", anim="cut", bis="k1"),
    *redet("KO_redet_r", KOX, BODEN, FH, "k1", "ges1"),
    peep_voll("KO_ernst_r", KOX, BODEN, FH, "ges1", anim="cut"),
    namensschild("Kommissar", KOX, BODEN, "f1", BLAU),
    pl("ungeduldig", KOX, 300, beim("ungeduld", "ungeduldig"), fill=ROTHELL, size=28, anker="m", bis="k1"),
    blase("sprech", 760, 200, "k1", 1100, 190, inhalt=["Reden Sie endlich. Sonst wird es", "für Sie schmerzhaft."],
          textsize=32, figur=KOa, bis="ges1"),
    pl("Angst", KLX, 360, beim("ges1", "Angst"), fill=ROTHELL, size=30, anker="m"),
    pl("Geständnis", KLX, 440, beim("ges1", "gesteht"), fill=GELB, size=30, anker="m"),
])

# B Fall 2: Straße ---------------------------------------------------------------------------------------------------------
AUX, HAX, POX = 470, 830, 1560         # Auto, Herr Haferkamp, Polizistin
_au = ficon("tabler", "car", AUX, BODEN + 6, 520, "_", fuell=ROT)
KR = [(AUX - 150, BODEN - 135), (AUX - 60, BODEN - 125), (AUX + 30, BODEN - 138), (AUX + 120, BODEN - 122)]
_ha0 = ("HA_denkt", HAX, BODEN, FH)
hx, hy = hand(*_ha0, -1)
folie([("f2", "Fall 2 · Auf der Straße"), (beim("f2", "zerkratzt"), "Fall 2 · Der Lack wird zerkratzt"),
       ("ohne", "Fall 2 · Frage ohne Belehrung"), ("h2", "Fall 2 · Das Geständnis")], [
    hart(linienzug([(60, BODEN), (1860, BODEN)], "f2", breite=7, farbe=INK)),
    kachel_nr(2, 70, 40, "f2", anim="cut"),
    pl("Straße vor dem Haus", 170, 40, "f2", fill=GELB, size=40, anim="cut"),
    hart(ficon("tabler", "car", AUX, BODEN + 6, 520, "f2", fuell=ROT)),
    pl("fremdes Auto", AUX, 470, beim("f2", "fremden"), fill=WEISS, size=28, anker="m", bis="ohne"),
    szene(linienzug(KR, beim("f2", "zerkratzt"), breite=6, farbe=INK), "221kratzen*", 1.0, versatz=0.0),
    peep_voll("HA_denkt", HAX, BODEN, FH, "f2", anim="cut", bis="ohne"),
    ficon("tabler", "key", hx - 20, hy + 40, 70, beim("f2", "Schlüssel"), fuell=GELB, bis="ohne"),
    peep_voll("HA_sorge_r", HAX, BODEN, FH, "ohne", anim="cut", bis="h2"),
    *redet("HA_redet_r", HAX, BODEN, FH, "h2", "hv2"),
    namensschild("Herr Haferkamp", HAX, BODEN, "f2", GELB, anim="cut"),
    peep_voll("PO_ernst", POX, BODEN, FH, beim("f2", "Polizistin"), bis="p2"),
    *redet("PO_redet", POX, BODEN, FH, "p2", "h2"),
    peep_voll("PO_ernst", POX, BODEN, FH, "h2", anim="cut"),
    namensschild("Polizistin", POX, BODEN, beim("f2", "Polizistin"), BLAU),
    ficon("tabler", "eye", POX, 300, 90, beim("f2", "sieht"), fuell=WEISS, bis="ohne"),
    pl("keine Belehrung", 1090, 560, "ohne", fill=ROTHELL, size=30, bis="hv2"),
    nein(1070, 582, beim("ohne", "belehren"), gr=18),
    blase("sprech", 640, 180, "p2", 1080, 180, inhalt=["Warum haben Sie", "das gemacht?"], textsize=34,
          figur=("PO_redet", POX, BODEN, FH), bis="h2"),
    blase("sprech", 760, 180, "h2", 1250, 200, inhalt=["Weil der ständig vor", "meiner Einfahrt parkt!"], textsize=34,
          figur=("HA_redet_r", HAX, BODEN, FH), bis="hv2"),
])

# B2 Fall 2: Hauptverhandlung ------------------------------------------------------------------------------------------------
GX, VX, AX = 420, 1080, 1460
folie([("hv2", "Fall 2 · Hauptverhandlung: Widerspruch")], [
    hart(linienzug([(60, BODEN), (1860, BODEN)], "hv2", breite=7, farbe=INK)),
    kachel_nr(2, 70, 40, "hv2", anim="cut"),
    pl("Hauptverhandlung", 170, 40, "hv2", fill=GELB, size=40, anim="cut"),
    hart(karte(GX - 230, BODEN - 235, 460, 233, "hv2", fill=HOLZ, rund=10, schatten=6)),
    ficon("tabler", "gavel", GX, BODEN - 235, 110, "hv2", fuell=HOLZ, anim="cut"),
    pl("Gericht", GX, BODEN - 120, "hv2", fill=WEISS, size=30, anker="m", anim="cut"),
    peep_voll("VE_ruhig", VX, BODEN, FH, "hv2", anim="cut", bis=beim("hv2", "widerspricht")),
    peep_voll("VE_ernst", VX, BODEN, FH, beim("hv2", "widerspricht"), anim="cut"),
    namensschild("Verteidigerin", VX, BODEN, "hv2", WEISS, anim="cut"),
    peep_voll("HA_ruhig", AX, BODEN, FH, "hv2", anim="cut", bis=beim("hv2", "rechtzeitig")),
    peep_voll("HA_denkt", AX, BODEN, FH, beim("hv2", "rechtzeitig"), anim="cut"),
    namensschild("Herr Haferkamp", AX, BODEN, "hv2", GELB, anim="cut"),
    ficon("tabler", "hand-stop", 780, 400, 90, beim("hv2", "widerspricht"), fuell=WEISS),
    pl("Widerspruch: rechtzeitig", 780, 250, beim("hv2", "rechtzeitig"), fill=WEISS, size=30, anker="m"),
])

# C Fall 3: Wohnungstür -------------------------------------------------------------------------------------------------------
SX, TX, RUX, PZX = 230, 560, 900, 1500  # Schrank, Tür, Frau Ruhnke, Polizist
SCHR = (SX - 120, BODEN - 380, 240, 378)
folie([("f3", "Fall 3 · Ein Verkaufskonto im Internet"), ("konto", "Fall 3 · Konto von Frau Ruhnke: gestohlene Laptops"),
       ("anruf", "Fall 3 · Richter nicht sofort erreicht"), ("giv", "Fall 3 · „Gefahr im Verzug“"),
       ("konkret", "Fall 3 · Keine konkreten Anhaltspunkte"), ("fund", "Fall 3 · Die Laptops im Schrank")], [
    hart(linienzug([(60, BODEN), (1860, BODEN)], "f3", breite=7, farbe=INK)),
    kachel_nr(3, 70, 40, "f3", anim="cut"),
    pl("Wohnung von Frau Ruhnke", 170, 40, "f3", fill=GELB, size=40, anim="cut"),
    hart(karte(*SCHR, "f3", fill=HOLZ, rund=10, schatten=6)),
    hart(linienzug([(SX, BODEN - 375), (SX, BODEN - 6)], "f3", breite=5, farbe=INK)),
    pl("Schrank", SX, BODEN - 430, "f3", fill=WEISS, size=28, anker="m", anim="cut"),
    ficon("tabler", "door", TX, BODEN + 4, 300, "f3", fuell=WEISS, anim="cut", bis="giv"),
    szene(ficon("tabler", "door-enter", TX, BODEN + 4, 300, beim("giv", "Durchsuchung"), fuell=WEISS, anim="cut"),
          "221tuer*", 1.0, versatz=-0.05),
    ficon("tabler", "world-www", 660, 330, 110, "f3", fuell=BLAU, bis="fund"),
    ficon("tabler", "device-laptop", 800, 330, 110, beim("f3", "Laptops"), fuell=WEISS, bis="fund"),
    pl("gestohlene Laptops", 730, 190, beim("f3", "Laptops"), fill=WEISS, size=28, anker="m", bis="r3"),
    pl("Konto: Frau Ruhnke", 730, 120, beim("konto", "Ruhnke"), fill=GELB, size=28, anker="m", bis="r3"),
    peep_voll("RU_ruhig_r", RUX, BODEN, FH, beim("konto", "Ruhnke"), bis="giv"),
    peep_voll("RU_sorge_r", RUX, BODEN, FH, "giv", anim="cut", bis="r3"),
    *redet("RU_redet_r", RUX, BODEN, FH, "r3", "fund"),
    peep_voll("RU_sorge_r", RUX, BODEN, FH, "fund", anim="cut"),
    namensschild("Frau Ruhnke", RUX, BODEN, beim("konto", "Ruhnke"), GELB),
    peep_voll("PZ_ruhig", PZX, BODEN, FH, "anruf", bis="giv"),
    peep_voll("PZ_ernst", PZX, BODEN, FH, "giv", anim="cut", bis="konkret"),
    peep_voll("PZ_denkt", PZX, BODEN, FH, "konkret", anim="cut"),
    namensschild("Polizist", PZX, BODEN, "anruf", BLAU),
    ficon("tabler", "phone-x", 1230, 330, 90, beim("anruf", "erreicht"), fuell=ROTHELL, bis="giv"),
    pl("Bereitschaftsrichter: nicht erreicht", 1850, 130, beim("anruf", "erreicht"), fill=WEISS, size=28, anker="r", bis="r3"),
    ficon("tabler", "hourglass", 1230, 330, 90, "giv", fuell=GELB, anim="cut", bis="r3"),
    pl("„Gefahr im Verzug“?", 1850, 200, beim("giv", "Gefahr"), fill=GELB, size=30, anker="r", bis="r3"),
    pl("keine konkreten Anhaltspunkte", 1850, 275, "konkret", fill=ROTHELL, size=28, anker="r", bis="r3"),
    blase("sprech", 700, 180, "r3", 1240, 220, inhalt=["Haben Sie überhaupt einen", "Durchsuchungsbeschluss?"], textsize=32,
          figur=("RU_redet_r", RUX, BODEN, FH), bis="fund"),
    ficon("tabler", "device-laptop", SX, BODEN - 230, 120, "fund", fuell=WEISS),
    ficon("tabler", "device-laptop", SX, BODEN - 70, 120, "fund", fuell=WEISS),
    pl("Laptops im Schrank", 640, 300, beim("fund", "Laptops"), fill=GELB, size=30, anker="m"),
])

# D Drei Ziffern-Kacheln -------------------------------------------------------------------------------------------------------
KX = (70, 680, 1290)
KW, KY, KH = 560, 150, 690
folie([("drei", "Fall · Drei Fehler"), ("d1", "Fall · 1. Drohung"), ("d2", "Fall · 2. fehlende Belehrung"),
       ("d3", "Fall · 3. Durchsuchung ohne Beschluss"), ("frage", "Fall · Die Frage")], [
    pl("Drei Fehler", 70, 40, "drei", fill=GELB, size=40, anim="cut"),
    *[karte(x, KY, KW, KH, "drei", fill=WEISS, d=0.15 * i) for i, x in enumerate(KX)],
    *[kachel_nr(i + 1, x + 30, KY + 25, "drei", d=0.15 * i) for i, x in enumerate(KX)],
    hocker("KL_angst", KX[0] + KW // 2, KY + 520, int(400 * SH), "drei"),
    peep_voll("KL_angst", KX[0] + KW // 2, KY + 520, int(400 * SH), "drei", anim="cut"),
    namensschild("Herr Kleinert", KX[0] + KW // 2, KY + 520, "drei", GELB, anim="cut"),
    peep_voll("HA_sorge", KX[1] + KW // 2, KY + 520, 400, "drei", d=0.15),
    namensschild("Herr Haferkamp", KX[1] + KW // 2, KY + 520, "drei", GELB, d=0.15),
    peep_voll("RU_sorge", KX[2] + KW // 2, KY + 520, 400, "drei", d=0.3),
    namensschild("Frau Ruhnke", KX[2] + KW // 2, KY + 520, "drei", GELB, d=0.3),
    pl("Drohung", KX[0] + KW // 2, KY + 610, "d1", fill=ROTHELL, size=32, anker="m"),
    pl("fehlende Belehrung", KX[1] + KW // 2, KY + 610, "d2", fill=ROTHELL, size=32, anker="m"),
    pl("Durchsuchung ohne Beschluss", KX[2] + KW // 2, KY + 610, "d3", fill=ROTHELL, size=30, anker="m"),
    pl("Welche Beweise darf das Gericht verwerten?", 960, 880, "frage", fill=WEISS, size=34, anker="m"),
    pl("Freispruch?", 1850, 40, beim("frage", "Freispruch"), fill=GELB, size=40, anker="r"),
])

# E Sachverhalt ----------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    glyphen("1. Im Vernehmungsraum soll Herr Kleinert einen Einbruch in einen Kiosk gestehen. Der Kommissar droht: „Reden "
            "Sie endlich. Sonst wird es für Sie schmerzhaft.“ Herr Kleinert bekommt Angst und gesteht."),
    glyphen("2. Eine Polizistin sieht, wie Herr Haferkamp mit einem Schlüssel ein fremdes Auto zerkratzt, und fragt ihn ohne "
            "Belehrung nach dem Grund. Er gesteht. In der Hauptverhandlung widerspricht seine Verteidigerin rechtzeitig."),
    glyphen("3. Über das Verkaufskonto von Frau Ruhnke werden gestohlene Laptops angeboten. Ein Polizist (Ermittlungsperson "
            "der Staatsanwaltschaft) erreicht den Bereitschaftsrichter nicht sofort und ordnet die Durchsuchung selbst an, "
            "weil er fürchtet, die Geräte könnten verschwinden. Konkrete Anhaltspunkte dafür gibt es nicht. Im Schrank "
            "liegen die Laptops."),
], "Welche Beweise darf das Gericht verwerten?")

# F Erhebungs- und Verwertungsverbot ------------------------------------------------------------------------------------------
PF = "Grundlagen"
folie([("ebv", f"{PF} › Beweiserhebungsverbot"), ("bvv", f"{PF} › Beweisverwertungsverbot"),
       ("nicht", f"{PF} › kein Automatismus"), ("ausn", f"{PF} › Wahrheit erforschen")], rechts_frei([
    *tafel("ebv", "Erhebung oder Verwertung?"),
    fb(110, 175, 1040, 130, BLAUHELL, "ebv", [("Beweiserhebungsverbot:", "ExtraBold", 34, INK),
                                            ("Ob und wie dürfen Beweise gewonnen werden?", "Bold", 30, INK)]),
    fb(110, 335, 1040, 130, GELB, "bvv", [("Beweisverwertungsverbot:", "ExtraBold", 34, INK),
                                         ("Darf das Gericht den Beweis im Urteil verwenden?", "Bold", 30, INK)]),
    nein(140, 525, beim("nicht", "Nicht"), gr=18),
    z("Nicht jeder Erhebungsfehler führt", 175, 505, "nicht", "Bold", 32),
    z("zu einem Verwertungsverbot.", 175, 550, beim("nicht", "Verwertungsverbot"), "Bold", 32),
    fund("BGH, Urt. v. 18.4.2007 – 5 StR 546/06, Rn. 20 (BGHSt 51, 285)", 175, 600, beim("nicht", "Verwertungsverbot")),
    z("Grund: Das Gericht soll die Wahrheit erforschen.", 110, 670, "ausn", size=32),
    fund("BVerfG, Beschl. v. 2.7.2009 – 2 BvR 2225/08, Rn. 16", 150, 718, beim("ausn", "Wahrheit")),
    peep_voll("PZ_ruhig", X1, BR, FR, "ebv", bis="bvv"),
    peep_voll("PZ_denkt", X1, BR, FR, "bvv", anim="cut"),
    namensschild("Polizist", X1, BR, "ebv", BLAU, d=0.2),
    peep_voll("RU_ruhig", X2, BR, FR, "ebv", d=0.2, bis="nicht"),
    peep_voll("RU_denkt", X2, BR, FR, "nicht", anim="cut"),
    namensschild("Frau Ruhnke", X2 + 20, BR, "ebv", GELB, d=0.3),
    ficon("tabler", "search", MB, 380, 100, "ebv", fuell=BLAUHELL, bis="bvv"),
    pl("Erhebung", MB, 160, "ebv", fill=BLAUHELL, size=28, anker="m", bis="bvv"),
    ficon("tabler", "gavel", MB, 380, 100, "bvv", fuell=GELB, anim="cut", bis="nicht"),
    pl("Verwertung", MB, 160, "bvv", fill=GELB, size=28, anker="m", anim="cut", bis="nicht"),
    ficon("tabler", "scale", MB, 380, 110, "nicht", fuell=WEISS, anim="cut"),
    pl("kein Automatismus", MB, 160, "nicht", fill=WEISS, size=28, anker="m", anim="cut", bis="ausn"),
    pl("Wahrheit erforschen", MB, 160, "ausn", fill=BLAUHELL, size=28, anker="m", anim="cut"),
]))

# G Erste Gruppe: gesetzlich geregelte Verbote – unselbständig / selbständig ------------------------------------------------
P1 = "Erste Gruppe: gesetzlich geregelt"
folie([("gesetz", f"{P1}"), ("unselb", f"{P1} › unselbständig"), ("selb", f"{P1} › selbständig")], rechts_frei([
    *tafel("gesetz", "Erste Gruppe: im Gesetz geregelt"),
    z("Verwertungsverbote, die das Gesetz ausdrücklich regelt", 110, 175, "gesetz", "Bold", 32),
    fund("BGH, Urt. v. 9.1.2025 – 1 StR 54/24, Rn. 24", 150, 222, beim("gesetz", "regelt")),
    fb(110, 300, 1040, 160, BLAUHELL, "unselb", [("unselbständig:", "ExtraBold", 34, INK),
                                               ("knüpft an einen Fehler bei der Erhebung an", "Bold", 30, INK)]),
    fund("vgl. BGH 1 StR 54/24, Rn. 18; BGH, Urt. v. 6.10.2016 – 2 StR 46/15", 150, 470, beim("unselb", "unselbständig")),
    fb(110, 540, 1040, 160, GRUENHELL, "selb", [("selbständig:", "ExtraBold", 34, INK),
                                              ("folgt unabhängig davon aus der Verfassung", "Bold", 30, INK)]),
    fund("BGH, Urt. v. 22.12.2011 – 2 StR 509/10, Rn. 21", 150, 710, beim("selb", "selbständig")),
    peep_voll("VE_ruhig", X1, BR, FR, "gesetz", bis="selb"),
    peep_voll("VE_denkt", X1, BR, FR, "selb", anim="cut"),
    namensschild("Verteidigerin", X1 - 30, BR, "gesetz", WEISS, d=0.2),
    peep_voll("HA_ruhig", X2, BR, FR, "gesetz", d=0.2, bis="unselb"),
    peep_voll("HA_denkt", X2, BR, FR, "unselb", anim="cut"),
    namensschild("Herr Haferkamp", X2 + 10, BR, "gesetz", GELB, d=0.3),
    ficon("tabler", "book", MB, 380, 100, "gesetz", fuell=GELB, bis="unselb"),
    pl("im Gesetz", MB, 160, "gesetz", fill=GELB, size=28, anker="m", bis="unselb"),
    ficon("tabler", "link", MB, 380, 100, "unselb", fuell=BLAUHELL, anim="cut", bis="selb"),
    pl("an den Fehler geknüpft", MB, 160, "unselb", fill=BLAUHELL, size=28, anker="m", anim="cut", bis="selb"),
    ficon("tabler", "shield", MB, 380, 100, "selb", fuell=GRUENHELL, anim="cut"),
    pl("aus der Verfassung", MB, 160, "selb", fill=GRUENHELL, size=28, anker="m", anim="cut"),
]))

# H § 136a Abs. 3 S. 2 StPO -----------------------------------------------------------------------------------------------------
KLT = int(FR * SH)
folie([("a136", f"{P1} › § 136a StPO"), ("a136b", f"{P1} › § 136a Abs. 1: verbotene Methoden"),
       ("a136c", f"{P1} › § 136a Abs. 3 S. 2 StPO"), ("abs", f"{P1} › keine Abwägung")], rechts_frei([
    *tafel("a136", "§ 136a StPO: verbotene Methoden"),
    pl("unselbständig", 110, 165, "a136", fill=BLAUHELL, size=28),
    z("verboten u. a.:", 110, 245, "a136b", "Bold", 30, farbe=TEXT),
    z("Misshandlung", 360, 245, beim("a136b", "Misshandlung"), "Bold", 30),
    z("Täuschung", 600, 245, beim("a136b", "Täuschung"), "Bold", 30),
    z("Drohung mit einer unzulässigen Maßnahme", 360, 290, beim("a136b", "Drohung"), "Bold", 30),
    fund("§ 136a Abs. 1 S. 1, 3 StPO", 360, 335, beim("a136b", "Drohung")),
    *wortlaut(110, 400, 1040, 210, "a136c", [
        [("„Aussagen, die unter Verletzung dieses Verbots", 0)],
        [("zustande gekommen sind, dürfen auch dann ", 0), ("nicht", "n")],
        [("verwertet", "n2"), (" werden, wenn der Beschuldigte der", 0)],
        [("Verwertung ", 0), ("zustimmt", "zu"), (".“", 0)],
    ], 30, {"n": beim("a136c", "nicht"), "n2": beim("a136c", "nicht"), "zu": beim("a136c", "zustimmt")},
        "§ 136a Abs. 3 S. 2 StPO"),
    fb(110, 690, 1040, 100, ROTHELL, "abs", [("Abgewogen wird hier nicht.", "ExtraBold", 36, INK)]),
    peep_voll("KO_ruhig", X1, BR, FR, "a136", bis="a136b"),
    peep_voll("KO_betr", X1, BR, FR, "a136b", anim="cut"),
    namensschild("Kommissar", X1, BR, "a136", BLAU, d=0.2),
    hocker("KL_ruhig", X2, BR, KLT, "a136"),
    peep_voll("KL_ruhig", X2, BR, KLT, "a136", d=0.2, bis="a136b"),
    peep_voll("KL_sorge", X2, BR, KLT, "a136b", anim="cut", bis="abs"),
    peep_voll("KL_denkt", X2, BR, KLT, "abs", anim="cut"),
    namensschild("Herr Kleinert", X2, BR, "a136", GELB, d=0.3),
    ficon("tabler", "ban", MB, 380, 100, "a136", fuell=ROTHELL, bis="a136c"),
    pl("verbotene Methoden", MB, 160, "a136b", fill=ROTHELL, size=28, anker="m", bis="a136c"),
    ficon("tabler", "file-text", MB, 380, 100, "a136c", fuell=WEISS, anim="cut", bis="abs"),
    pl("unverwertbar", MB, 160, beim("a136c", "nicht"), fill=ROTHELL, size=28, anker="m", bis="abs"),
    ficon("tabler", "scale", MB, 380, 110, "abs", fuell=WEISS, anim="cut"),
    pl("keine Abwägung", MB, 160, "abs", fill=ROTHELL, size=28, anker="m", anim="cut"),
    nein(MB, 330, "abs", gr=22),
]))

# I § 252 StPO -------------------------------------------------------------------------------------------------------------------
folie([("a252", f"{P1} › § 252 StPO"), ("a252b", f"{P1} › § 252 StPO: Verlesungsverbot"),
       ("a252d", f"{P1} › § 252 StPO: Verwertungsverbot"), ("a252e", f"{P1} › § 252 StPO: Ausnahme Richter")], rechts_frei([
    *tafel("a252", "§ 252 StPO: Zeugnis verweigert"),
    z("schützt z. B. Angehörige mit Zeugnisverweigerungsrecht", 110, 170, beim("a252", "Angehörige"), "Bold", 30),
    fund("§ 52 Abs. 1 StPO", 150, 212, beim("a252", "Angehörige")),
    *wortlaut(110, 270, 1040, 205, "a252b", [
        [("„Die Aussage eines vor der Hauptverhandlung vernommenen", 0)],
        [("Zeugen, der erst in der Hauptverhandlung von seinem Recht,", 0)],
        [("das Zeugnis zu verweigern, Gebrauch macht, ", 0), ("darf nicht", "v")],
        [("verlesen werden", "v2"), (".“", 0)],
    ], 28, {"v": beim("a252b", "verlesen"), "v2": beim("a252b", "verlesen")}, "§ 252 StPO"),
    z("Rechtsprechung: auch ein Verwertungsverbot,", 110, 545, "a252d", "Bold", 30),
    z("grundsätzlich auch keine Aussage des Polizisten", 110, 588, beim("a252d", "Polizist"), "Bold", 30),
    fund("BGH (GrS), Beschl. v. 15.7.2016 – GSSt 1/16, Rn. 32 (BGHSt 61, 221)", 150, 632, beim("a252d", "Polizist")),
    fb(110, 690, 1040, 110, GELB, "a252e", [("Ausnahme: Aussage vor dem Richter nach Belehrung", "ExtraBold", 32, INK)]),
    peep_voll("VE_ruhig", X1, BR, FR, "a252", bis="a252d"),
    peep_voll("VE_denkt", X1, BR, FR, "a252d", anim="cut"),
    namensschild("Verteidigerin", X1 - 30, BR, "a252", WEISS, d=0.2),
    peep_voll("PZ_ruhig", X2, BR, FR, "a252", d=0.2, bis=beim("a252d", "Polizist")),
    peep_voll("PZ_betr", X2, BR, FR, beim("a252d", "Polizist"), anim="cut"),
    namensschild("Polizist", X2, BR, "a252", BLAU, d=0.3),
    ficon("tabler", "home", MB, 380, 100, "a252", fuell=GELB, bis="a252b"),
    pl("Angehörige", MB, 160, beim("a252", "Angehörige"), fill=GELB, size=28, anker="m", bis="a252b"),
    ficon("tabler", "file-text", MB, 380, 100, "a252b", fuell=WEISS, anim="cut", bis="a252d"),
    pl("nicht verlesen", MB, 160, beim("a252b", "verlesen"), fill=ROTHELL, size=28, anker="m", bis="a252d"),
    ficon("tabler", "microphone-off", MB, 380, 100, "a252d", fuell=ROTHELL, anim="cut", bis="a252e"),
    pl("nicht verwerten", MB, 160, "a252d", fill=ROTHELL, size=28, anker="m", anim="cut", bis="a252e"),
    ficon("tabler", "gavel", MB, 380, 100, "a252e", fuell=GELB, anim="cut"),
    pl("Ausnahme: Richter", MB, 160, "a252e", fill=GELB, size=28, anker="m", anim="cut"),
]))

# J § 100d Abs. 2 StPO ------------------------------------------------------------------------------------------------------------
folie([("a100", f"{P1} › § 100d Abs. 2 StPO: Kernbereich"), ("a100b", f"{P1} › § 100d Abs. 2 S. 1 StPO")], rechts_frei([
    *tafel("a100", "§ 100d Abs. 2 StPO: Kernbereich"),
    z("Kernbereich privater Lebensgestaltung", 110, 175, "a100", "Bold", 32),
    pl("selbständig: Schutz aus der Verfassung", 110, 235, beim("a100", "selbständiger"), fill=GRUENHELL, size=28),
    fund("vgl. BGH 2 StR 509/10, Leitsatz, Rn. 21; BGH 1 StR 54/24, Rn. 25", 150, 305, beim("a100", "Verfassung")),
    *wortlaut(110, 380, 1040, 205, "a100b", [
        [("„Erkenntnisse aus dem Kernbereich privater", 0)],
        [("Lebensgestaltung, die durch eine Maßnahme nach den", 0)],
        [("§§ 100a bis 100c erlangt wurden, dürfen ", 0), ("nicht", "n")],
        [("verwertet", "n2"), (" werden.“", 0)],
    ], 30, {"n": beim("a100b", "verwertet"), "n2": beim("a100b", "verwertet")}, "§ 100d Abs. 2 S. 1 StPO"),
    z("z. B. Telefonüberwachung, § 100a StPO", 110, 660, beim("a100b", "Telefonüberwachung"), "Bold", 30),
    peep_voll("PO_ruhig", X1, BR, FR, "a100", bis="a100b"),
    peep_voll("PO_denkt", X1, BR, FR, "a100b", anim="cut"),
    namensschild("Polizistin", X1, BR, "a100", BLAU, d=0.2),
    peep_voll("HA_ruhig", X2, BR, FR, "a100", d=0.2, bis="a100b"),
    peep_voll("HA_sorge", X2, BR, FR, "a100b", anim="cut"),
    namensschild("Herr Haferkamp", X2 + 10, BR, "a100", GELB, d=0.3),
    ficon("tabler", "heart", MB, 380, 100, "a100", fuell=ROTHELL, bis=beim("a100b", "Telefonüberwachung")),
    pl("Kernbereich", MB, 160, "a100", fill=GRUENHELL, size=28, anker="m", bis="a100b"),
    ficon("tabler", "phone-call", MB, 380, 100, beim("a100b", "Telefonüberwachung"), fuell=WEISS, anim="cut"),
    pl("nicht verwerten", MB, 160, "a100b", fill=ROTHELL, size=28, anker="m", anim="cut"),
]))

# K § 479 Abs. 2 i. V. m. § 161 Abs. 3 StPO --------------------------------------------------------------------------------------
folie([("a479", f"{P1} › § 479 Abs. 2 StPO: andere Verfahren"), ("a479b", f"{P1} › § 161 Abs. 3 StPO: nur bestimmte Taten")],
      rechts_frei([
    *tafel("a479", "§ 479 Abs. 2 StPO: andere Verfahren"),
    *wortlaut(110, 245, 1040, 205, "a479", [
        [("„Ist eine Maßnahme nach diesem Gesetz nur bei Verdacht", 0)],
        [("bestimmter Straftaten", "b"), (" zulässig, so gilt für die Verwendung der", 0)],
        [("auf Grund einer solchen Maßnahme erlangten Daten in", 0)],
        [("anderen Strafverfahren § 161 Absatz 3 entsprechend.“", 0)],
    ], 28, {"b": beim("a479b", "bestimmten")}, "§ 479 Abs. 2 S. 1 StPO", quelle_cue="a479"),
    *wortlaut(110, 520, 1040, 205, beim("a479", "Strafverfahren"), [
        [("„… dürfen … zu Beweiszwecken im Strafverfahren nur", 0)],
        [("zur Aufklärung solcher Straftaten verwendet werden,", "a")],
        [("zu deren Aufklärung eine solche Maßnahme nach diesem", 0)],
        [("Gesetz hätte angeordnet werden dürfen.“", 0)],
    ], 28, {"a": beim("a479c", "nur")}, "§ 161 Abs. 3 S. 1 StPO (Auszug)"),
    peep_voll("VE_ruhig", X1, BR, FR, "a479", bis="a479c"),
    peep_voll("VE_froh", X1, BR, FR, "a479c", anim="cut"),
    namensschild("Verteidigerin", X1 - 30, BR, "a479", WEISS, d=0.2),
    peep_voll("KO_ruhig", X2, BR, FR, "a479", d=0.2, bis="a479b"),
    peep_voll("KO_denkt", X2, BR, FR, "a479b", anim="cut"),
    namensschild("Kommissar", X2, BR, "a479", BLAU, d=0.3),
    ficon("tabler", "files", MB, 380, 100, "a479", fuell=WEISS, bis="a479b"),
    pl("anderes Verfahren", MB, 160, beim("a479", "Strafverfahren"), fill=WEISS, size=28, anker="m", bis="a479b"),
    ficon("tabler", "list-check", MB, 380, 100, "a479b", fuell=GELB, anim="cut", bis="a479c"),
    pl("bestimmte Straftaten", MB, 160, "a479b", fill=GELB, size=28, anker="m", anim="cut", bis="a479c"),
    ficon("tabler", "lock", MB, 380, 90, "a479c", fuell=BLAUHELL, anim="cut"),
    pl("nur für solche Taten", MB, 160, "a479c", fill=BLAUHELL, size=28, anker="m", anim="cut"),
]))

# L Zweite Gruppe: Abwägungslehre ---------------------------------------------------------------------------------------------------
P2 = "Zweite Gruppe: ungeschrieben"
folie([("unge", f"{P2}"), ("abwl", f"{P2} › Abwägungslehre"), ("auf", f"{P2} › Abwägung: Aufklärungsinteresse"),
       ("gew", f"{P2} › Abwägung: Gewicht des Verstoßes"), ("grob", f"{P2} › bewusst oder grob?")], rechts_frei([
    *tafel("unge", "Zweite Gruppe: Abwägungslehre"),
    z("Verbote, die nicht im Gesetz stehen: Die Rechtsprechung", 110, 170, "unge", "Bold", 30),
    z("wägt ab.", 110, 212, "abwl", "Bold", 30),
    fund("BGH, Urt. v. 9.1.2025 – 1 StR 54/24, Rn. 24", 250, 218, beim("abwl", "ab")),
    fb(110, 270, 1040, 110, GRUENHELL, "auf", [("Für die Verwertung: Aufklärungsinteresse,", "ExtraBold", 30, INK),
                                             ("etwa die Schwere der Tat", "Bold", 30, INK)]),
    z("Dagegen: Gewicht des Verstoßes", 110, 410, "gew", "ExtraBold", 32),
    z("• bewusst oder nur fahrlässig?", 140, 460, "k_vors", "Bold", 30),
    z("• Schutzzweck der verletzten Vorschrift?", 140, 505, "k_zweck", "Bold", 30),
    z("• Beweis auch rechtmäßig erlangbar?", 140, 550, "k_hypo", "Bold", 30),
    fb(110, 630, 1040, 130, ROTHELL, "grob", [("Verbot vor allem bei bewusster Missachtung", "ExtraBold", 30, INK),
                                            ("oder grober Verkennung der Rechtslage", "ExtraBold", 30, INK)]),
    fund("BGH 1 StR 54/24, Rn. 24; BGHSt 51, 285, Rn. 24", 150, 772, beim("grob", "Missachtung")),
    peep_voll("PZ_ruhig", X1, BR, FR, "unge", bis="gew"),
    peep_voll("PZ_denkt", X1, BR, FR, "gew", anim="cut", bis="grob"),
    peep_voll("PZ_ernst", X1, BR, FR, "grob", anim="cut"),
    namensschild("Polizist", X1, BR, "unge", BLAU, d=0.2),
    peep_voll("RU_ruhig", X2, BR, FR, "unge", d=0.2, bis="auf"),
    peep_voll("RU_denkt", X2, BR, FR, "auf", anim="cut"),
    namensschild("Frau Ruhnke", X2 + 20, BR, "unge", GELB, d=0.3),
    ficon("tabler", "book", MB, 380, 100, "unge", fuell=WEISS, bis="abwl"),
    pl("nicht im Gesetz", MB, 160, "unge", fill=WEISS, size=28, anker="m", bis="abwl"),
    ficon("tabler", "scale", MB, 380, 110, "abwl", fuell=GELB, anim="cut", bis="grob"),
    pl("Abwägung", MB, 160, "abwl", fill=GELB, size=28, anker="m", anim="cut", bis="auf"),
    pl("Aufklärung", MB, 160, "auf", fill=GRUENHELL, size=28, anker="m", anim="cut", bis="gew"),
    pl("Gewicht des Verstoßes", MB, 160, "gew", fill=ROTHELL, size=28, anker="m", anim="cut", bis="grob"),
    ficon("tabler", "alert-triangle", MB, 380, 100, "grob", fuell=ROTHELL, anim="cut"),
    pl("bewusst oder grob?", MB, 160, "grob", fill=ROTHELL, size=28, anker="m", anim="cut"),
]))

# M Rechtskreistheorie und Widerspruchslösung -------------------------------------------------------------------------------------
folie([("rkt", f"{P2} › Rechtskreistheorie"), ("wl", f"{P2} › Widerspruchslösung"), ("wl3", f"{P2} › ohne Widerspruch verwertbar"),
       ("verw", f"{P2} › siehe Folgen 132 und 171")], rechts_frei([
    *tafel("rkt", "Rechtskreis und Widerspruch"),
    z("Rechtskreistheorie:", 110, 170, "rkt", "ExtraBold", 32),
    z("Schützt die Vorschrift den Beschuldigten nicht,", 140, 215, "rkt2", "Bold", 30),
    z("kann er sich nicht auf ein Verbot berufen.", 140, 258, beim("rkt2", "kann"), "Bold", 30),
    fund("BGH, Beschl. v. 5.7.2022 – 4 StR 61/22, Rn. 12; BGHSt 11, 213, 215 (GrS)", 140, 302, beim("rkt2", "berufen")),
    z("Widerspruchslösung (Belehrungsfehler):", 110, 375, "wl", "ExtraBold", 32),
    z("Der verteidigte Angeklagte muss widersprechen,", 140, 420, "wl2", "Bold", 30),
    z("spätestens in seiner Erklärung nach der Beweiserhebung", 140, 463, beim("wl2", "spätestens"), "Bold", 30),
    fund("BGH, Beschl. v. 27.2.1992 – 5 StR 190/91, BGHSt 38, 214, 225 f.; § 257 StPO", 140, 507, beim("wl2", "Beweiserhebung")),
    z("Sonst bleibt die Aussage verwertbar.", 140, 570, "wl3", "Bold", 30),
    fb(110, 660, 1040, 110, BLAUHELL, "verw", [("Mehr dazu: Folge 132 · Widerspruchslösung", "ExtraBold", 30, INK),
                                             ("und Folge 171 · Belehrungsverstoß", "ExtraBold", 30, INK)]),
    peep_voll("VE_ruhig", X1, BR, FR, "rkt", bis="wl"),
    peep_voll("VE_ernst", X1, BR, FR, "wl", anim="cut", bis="verw"),
    peep_voll("VE_froh", X1, BR, FR, "verw", anim="cut"),
    namensschild("Verteidigerin", X1 - 30, BR, "rkt", WEISS, d=0.2),
    peep_voll("HA_ruhig", X2, BR, FR, "rkt", d=0.2, bis="wl3"),
    peep_voll("HA_sorge", X2, BR, FR, "wl3", anim="cut"),
    namensschild("Herr Haferkamp", X2 + 10, BR, "rkt", GELB, d=0.3),
    ficon("tabler", "shield-check", MB, 380, 100, "rkt", fuell=BLAUHELL, bis="wl"),
    pl("Rechtskreis", MB, 160, "rkt", fill=BLAUHELL, size=28, anker="m", bis="wl"),
    ficon("tabler", "hand-stop", MB, 380, 100, "wl", fuell=WEISS, anim="cut", bis="verw"),
    pl("Widerspruch", MB, 160, "wl", fill=WEISS, size=28, anker="m", anim="cut", bis="verw"),
    ficon("tabler", "player-play", MB, 380, 100, "verw", fuell=BLAUHELL, anim="cut"),
    pl("Folgen 132 und 171", MB, 160, "verw", fill=BLAUHELL, size=28, anker="m", anim="cut"),
]))

# N Reichweite: Fernwirkung und Fortwirkung ----------------------------------------------------------------------------------------
P3 = "Reichweite"
folie([("fern", f"{P3}"), ("fern2", f"{P3} › Fernwirkung"), (beim("fern2", "Diese"), f"{P3} › Fernwirkung: grundsätzlich nein"),
       ("fern3", f"{P3} › siehe Folge 211"), ("fort", f"{P3} › Fortwirkung"), ("qual", f"{P3} › qualifizierte Belehrung")],
      rechts_frei([
    *tafel("fern", "Wie weit reicht ein Verbot?"),
    z("Fernwirkung: Beweise, die erst durch eine", 110, 170, "fern2", "Bold", 30),
    z("unverwertbare Aussage gefunden werden", 110, 213, beim("fern2", "unverwertbare"), "Bold", 30),
    nein(150, 280, beim("fern2", "grundsätzlich"), gr=18),
    z("grundsätzlich abgelehnt", 185, 260, beim("fern2", "grundsätzlich"), "ExtraBold", 30),
    fund("BGH, Beschl. v. 7.3.2006 – 1 StR 316/05, Rn. 22 f.", 185, 304, beim("fern2", "ab")),
    fb(110, 360, 1040, 90, BLAUHELL, "fern3", [("Mehr dazu: Folge 211 · Fall Gäfgen", "ExtraBold", 30, INK)]),
    z("Fortwirkung: Nach einem Belehrungsfehler vor neuer", 110, 500, "fort", "Bold", 30),
    z("Vernehmung Hinweis, dass die frühere Aussage", 110, 543, beim("fort", "Vernehmung"), "Bold", 30),
    z("unverwertbar ist", 110, 586, beim("fort", "unverwertbar"), "Bold", 30),
    fb(110, 650, 1040, 100, GELB, "qual", [("qualifizierte Belehrung", "ExtraBold", 34, INK)]),
    fund("BGH, Urt. v. 3.5.2018 – 3 StR 390/17, Rn. 28; BGHSt 53, 112", 150, 762, beim("qual", "Belehrung")),
    peep_voll("KO_ruhig", X1, BR, FR, "fern", bis="fort"),
    peep_voll("KO_denkt", X1, BR, FR, "fort", anim="cut"),
    namensschild("Kommissar", X1, BR, "fern", BLAU, d=0.2),
    hocker("KL_denkt", X2, BR, KLT, "fern"),
    peep_voll("KL_denkt", X2, BR, KLT, "fern", d=0.2, bis="fort"),
    peep_voll("KL_ruhig", X2, BR, KLT, "fort", anim="cut"),
    namensschild("Herr Kleinert", X2, BR, "fern", GELB, d=0.3),
    ficon("tabler", "route", MB, 380, 100, "fern", fuell=WEISS, bis="fort"),
    pl("Fernwirkung?", MB, 160, "fern2", fill=WEISS, size=28, anker="m", bis=beim("fern2", "Diese")),
    pl("grundsätzlich nein", MB, 160, beim("fern2", "Diese"), fill=ROTHELL, size=28, anker="m", anim="cut", bis="fern3"),
    pl("Folge 211", MB, 160, "fern3", fill=BLAUHELL, size=28, anker="m", anim="cut", bis="fort"),
    ficon("tabler", "repeat", MB, 380, 100, "fort", fuell=GELB, anim="cut"),
    pl("Fortwirkung", MB, 160, "fort", fill=GELB, size=28, anker="m", anim="cut", bis="qual"),
    pl("qualifizierte Belehrung", MB, 160, "qual", fill=GELB, size=28, anker="m", anim="cut"),
]))

# O Lösung Fall 1 ---------------------------------------------------------------------------------------------------------------------
P4 = "Lösung"
folie([("l1", f"{P4} › Fall 1: Herr Kleinert"), ("l1a", f"{P4} › Fall 1: Drohung mit Schmerzen"),
       ("l1b", f"{P4} › Fall 1: Geständnis unverwertbar")], rechts_frei([
    *tafel("l1", "Lösung Fall 1: Herr Kleinert"),
    kachel_nr(1, 1050, 85, "l1"),
    z("Drohung mit Schmerzen:", 110, 190, "l1a", "ExtraBold", 32),
    z("eine unzulässige Maßnahme", 110, 237, beim("l1a", "unzulässigen"), "Bold", 32),
    fund("§ 136a Abs. 1 S. 3 StPO", 150, 285, beim("l1a", "unzulässigen")),
    fb(110, 360, 1040, 130, ROTHELL, "l1b", [("Geständnis unverwertbar,", "ExtraBold", 34, INK),
                                           ("selbst wenn er zustimmt", "ExtraBold", 34, INK)]),
    fund("§ 136a Abs. 3 S. 2 StPO", 150, 502, beim("l1b", "unverwertbar")),
    peep_voll("KO_betr", X1, BR, FR, "l1"),
    namensschild("Kommissar", X1, BR, "l1", BLAU, d=0.2),
    hocker("KL_sorge", X2, BR, KLT, "l1"),
    peep_voll("KL_sorge", X2, BR, KLT, "l1", d=0.2, bis="l1b"),
    peep_voll("KL_froh", X2, BR, KLT, "l1b", anim="cut"),
    namensschild("Herr Kleinert", X2, BR, "l1", GELB, d=0.3),
    ficon("tabler", "alert-triangle", MB, 380, 100, "l1a", fuell=ROTHELL, bis="l1b"),
    pl("unzulässige Drohung", MB, 160, "l1a", fill=ROTHELL, size=28, anker="m", bis="l1b"),
    ficon("tabler", "circle-x", MB, 380, 100, "l1b", fuell=ROT, anim="cut"),
    pl("unverwertbar", MB, 160, "l1b", fill=ROTHELL, size=28, anker="m", anim="cut"),
]))

# P Lösung Fall 2 ---------------------------------------------------------------------------------------------------------------------
folie([("l2", f"{P4} › Fall 2: Belehrung fehlte"), ("l2a", f"{P4} › Fall 2: Widerspruch, unverwertbar"),
       ("l2b", f"{P4} › Fall 2: Freispruch?"), ("l2c", f"{P4} › Fall 2: Polizistin als Zeugin")], rechts_frei([
    *tafel("l2", "Lösung Fall 2: Herr Haferkamp"),
    kachel_nr(2, 1050, 85, "l2"),
    nein(140, 205, beim("l2", "belehren"), gr=18),
    z("Belehrung über das Schweigerecht fehlte", 175, 185, "l2", "Bold", 32),
    fund("§ 163a Abs. 4 S. 2 i. V. m. § 136 Abs. 1 S. 2 StPO", 175, 232, beim("l2", "belehren")),
    ok(140, 310, "l2a", gr=18),
    z("Die Verteidigerin hat rechtzeitig widersprochen.", 175, 290, "l2a", "Bold", 32),
    fb(110, 360, 1040, 100, ROTHELL, beim("l2a", "unverwertbar"), [("Aussage unverwertbar", "ExtraBold", 34, INK)]),
    z("Freispruch? Nicht automatisch:", 110, 510, "l2b", "ExtraBold", 32),
    fb(110, 570, 1040, 130, GRUENHELL, "l2c", [("Die Polizistin hat die Tat selbst gesehen", "ExtraBold", 30, INK),
                                             ("und kann als Zeugin aussagen.", "ExtraBold", 30, INK)]),
    peep_voll("PO_ruhig", X1, BR, FR, "l2", bis="l2c"),
    peep_voll("PO_froh", X1, BR, FR, "l2c", anim="cut"),
    namensschild("Polizistin", X1, BR, "l2", BLAU, d=0.2),
    peep_voll("HA_ruhig", X2, BR, FR, "l2", d=0.2, bis="l2a"),
    peep_voll("HA_froh", X2, BR, FR, "l2a", anim="cut", bis="l2b"),
    peep_voll("HA_sorge", X2, BR, FR, "l2b", anim="cut"),
    namensschild("Herr Haferkamp", X2 + 10, BR, "l2", GELB, d=0.3),
    ficon("tabler", "microphone-off", MB, 380, 100, "l2", fuell=WEISS, bis="l2a"),
    pl("keine Belehrung", MB, 160, "l2", fill=ROTHELL, size=28, anker="m", bis="l2a"),
    ficon("tabler", "hand-stop", MB, 380, 100, "l2a", fuell=WEISS, anim="cut", bis="l2b"),
    pl("unverwertbar", MB, 160, beim("l2a", "unverwertbar"), fill=ROTHELL, size=28, anker="m", bis="l2b"),
    ficon("tabler", "help-circle", MB, 380, 100, "l2b", fuell=WEISS, anim="cut", bis="l2c"),
    pl("Freispruch?", MB, 160, "l2b", fill=WEISS, size=28, anker="m", anim="cut", bis="l2c"),
    ficon("tabler", "eye", MB, 380, 100, "l2c", fuell=GRUENHELL, anim="cut"),
    pl("Zeugin der Tat", MB, 160, "l2c", fill=GRUENHELL, size=28, anker="m", anim="cut"),
]))

# Q Lösung Fall 3 ---------------------------------------------------------------------------------------------------------------------
folie([("l3", f"{P4} › Fall 3: keine Gefahr im Verzug"), ("l3a", f"{P4} › Fall 3: Richtervorbehalt verletzt"),
       ("l3b", f"{P4} › Fall 3: Abwägung"), ("l3e", f"{P4} › Fall 3: Laptops verwertbar"), ("l3f", f"{P4} › siehe Folge 151")],
      rechts_frei([
    *tafel("l3", "Lösung Fall 3: Frau Ruhnke"),
    kachel_nr(3, 1050, 85, "l3"),
    z("Bloße Befürchtung: keine Gefahr im Verzug", 110, 175, "l3", "Bold", 32),
    fund("BVerfG, Urt. v. 20.2.2001 – 2 BvR 1444/00, Rn. 38 (BVerfGE 103, 142)", 150, 222, beim("l3", "Gefahr")),
    nein(140, 290, "l3a", gr=18),
    z("Richtervorbehalt verletzt, § 105 Abs. 1 S. 1 StPO", 175, 270, "l3a", "Bold", 32),
    z("Abwägung:", 110, 345, "l3b", "ExtraBold", 32),
    ok(140, 410, "l3b", gr=16),
    z("Er hatte versucht, den Richter zu erreichen.", 175, 390, "l3b", "Bold", 30),
    ok(140, 455, "l3c", gr=16),
    z("Beschluss wegen des Kontos sehr wahrscheinlich", 175, 435, "l3c", "Bold", 30),
    ok(140, 500, "l3d", gr=16),
    z("Verstoß weder bewusst noch grob", 175, 480, "l3d", "Bold", 30),
    fund("BGHSt 51, 285, Rn. 22, 24; BVerfG 2 BvR 2225/08, Rn. 17", 175, 525, beim("l3d", "Verstoß")),
    fb(110, 590, 1040, 100, GRUEN, beim("l3e", "Die", 2), [("Die Laptops sind verwertbar.", "ExtraBold", 36, INK)]),
    fb(110, 720, 1040, 90, BLAUHELL, "l3f", [("Mehr dazu: Folge 151 · Durchsuchung", "ExtraBold", 30, INK)]),
    peep_voll("PZ_ruhig", X1, BR, FR, "l3", bis="l3a"),
    peep_voll("PZ_betr", X1, BR, FR, "l3a", anim="cut", bis="l3e"),
    peep_voll("PZ_ruhig", X1, BR, FR, "l3e", anim="cut"),
    namensschild("Polizist", X1, BR, "l3", BLAU, d=0.2),
    peep_voll("RU_ruhig", X2, BR, FR, "l3", d=0.2, bis="l3a"),
    peep_voll("RU_denkt", X2, BR, FR, "l3a", anim="cut", bis="l3e"),
    peep_voll("RU_ernst", X2, BR, FR, "l3e", anim="cut"),
    namensschild("Frau Ruhnke", X2 + 20, BR, "l3", GELB, d=0.3),
    ficon("tabler", "hourglass", MB, 380, 100, "l3", fuell=WEISS, bis="l3a"),
    pl("keine Gefahr im Verzug", MB, 160, "l3", fill=ROTHELL, size=28, anker="m", bis="l3a"),
    ficon("tabler", "gavel", MB, 380, 100, "l3a", fuell=ROTHELL, anim="cut", bis="l3b"),
    pl("Richtervorbehalt", MB, 160, "l3a", fill=ROTHELL, size=28, anker="m", anim="cut", bis="l3b"),
    ficon("tabler", "scale", MB, 380, 110, "l3b", fuell=GELB, anim="cut", bis="l3e"),
    pl("Abwägung", MB, 160, "l3b", fill=GELB, size=28, anker="m", anim="cut", bis="l3e"),
    ficon("tabler", "device-laptop", MB, 380, 110, "l3e", fuell=GRUENHELL, anim="cut", bis="l3f"),
    pl("verwertbar", MB, 160, beim("l3e", "Die", 2), fill=GRUEN, size=28, anker="m", bis="l3f"),
    ficon("tabler", "player-play", MB, 380, 100, "l3f", fuell=BLAUHELL, anim="cut"),
    pl("Folge 151", MB, 160, "l3f", fill=BLAUHELL, size=28, anker="m", anim="cut"),
]))

# R Klausurtipp mit Prüfungsschema (Lexi) --------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · Prüfungsschema"), ("s1", "Klausurtipp · I. Beweiserhebungsverbot verletzt?"),
       ("s2", "Klausurtipp · II. Gesetzliches Verwertungsverbot?"), ("s3", "Klausurtipp · III. Abwägung, Rechtskreis"),
       ("s4", "Klausurtipp · IV. Widerspruch"), ("s5", "Klausurtipp · V. Reichweite")], [
    *tafel("tipp", "Klausurtipp: Prüfungsschema", h=860, fill=HELL),
    warnung_i(150, 205, "tipp", gr=26),
    z("Prüf in dieser Reihenfolge:", 200, 180, beim("tipp", "Prüf"), "Bold", 36),
    z("I. Beweiserhebungsverbot verletzt?", 130, 270, "s1", "ExtraBold", 34),
    z("II. Gesetzliches Verwertungsverbot?", 130, 350, "s2", "ExtraBold", 34),
    fund("z. B. § 136a Abs. 3 S. 2, § 252, § 100d Abs. 2, § 479 Abs. 2 StPO", 190, 396, beim("s2", "Verwertungsverbot")),
    z("III. Sonst: Abwägung", 130, 465, "s3", "ExtraBold", 34),
    z("Rechtskreis beachten", 190, 511, beim("s3", "Rechtskreis"), size=30),
    z("IV. Widerspruch nötig und rechtzeitig?", 130, 585, "s4", "ExtraBold", 34),
    z("V. Reichweite", 130, 665, "s5", "ExtraBold", 34),
    z("Fortwirkung, Fernwirkung", 190, 711, beim("s5", "Fortwirkung"), size=30),
    *redet("LX_warnt", LXX, BR, FR + 60, "tipp", "merke"),
    namensschild("Lexi", LXX, BR, "tipp", GELB, d=0.2),
])

# S Merksatz (Lexi) --------------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Ein Fehler bei der Erhebung macht", 0)], [("einen Beweis ", 0), ("nicht automatisch", "a")],
                 [("unverwertbar.", 0)]], 750, 300, 50, "merke", {"a": beim("merke", "nicht")}),
    *markertext([[("Entscheidend ist, ob das ", 0), ("Gesetz", "b")], [("ein Verbot anordnet oder die", 0)],
                 [("Abwägung", "c"), (" es verlangt.", 0)]], 750, 530, 48, "mz",
                {"b": beim("mz", "Gesetz"), "c": beim("mz", "Abwägung")}),
    *redet("LX_erklaert", 1680, 960, 690, "merke", lexi_bis_ende("merke")),
    namensschild("Lexi", 1680, 960, "merke", GELB, d=0.2),
])
