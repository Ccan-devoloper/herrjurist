"""Abschleppfall – Open-Peeps-Stil nach aktuellem Regelwerk.

Figuren: nur Open-Peeps-Posen, nie seitlich/oben angeschnitten. Karten sofort vollständig, Punkte nacheinander.
Geräusche nur bei Haken/Kreuz. Requisiten aus Bibliotheken: Tabler (MIT), Phosphor (MIT), Fluent Emoji (MIT),
Pepicons (CC BY 4.0); Linien-Icons werden nur mit Palettenfarben ausgefüllt, nicht umgezeichnet.
"""
import sys
sys.path.insert(0, "../../etb2/src")
from ostil import *
from ostil import _icsets
import engine
from scipy import ndimage

FOLIEN = []
FIG = SP + "peeps/"
BG_FARBE = {"creme": (255, 248, 236, 255)}
PFAD_FARBE = {"creme": (21, 21, 21, 140)}
RAND = 24


def folie(pfade, els):
    FOLIEN.append(dict(bg="creme", pfade=pfade, els=els))


def peep_voll(name, cx, unten, hoehe, cue, unten_offen=False, **k):
    """Nie links/rechts/oben angeschnitten; unten nur mit unten_offen=True."""
    ordner = "op_we/" if name.startswith("ER_") else "op_ab/"
    e = bild(FIG + ordner + name + ".png", cx, unten, hoehe, cue, **k)
    assert e.x >= RAND and e.y >= RAND and e.x + e.sprite.width <= engine.W - RAND, f"Figur {name} seitlich/oben angeschnitten"
    if not unten_offen:
        assert e.y + e.sprite.height <= engine.H - RAND, f"Figur {name} unten angeschnitten"
    return e


def figuren(liste, cx, unten, hoehe, erst="pop", d=0.0):
    els = []
    for i, (n, c) in enumerate(liste):
        bis = liste[i + 1][1] if i + 1 < len(liste) else None
        if isinstance(n, tuple):
            n, bis = n
        els.append(peep_voll(n, cx, unten, hoehe, c, anim=(erst if i == 0 else "cut"), d=(d if i == 0 else 0.0), bis=bis))
    return els


def ok(x, y, cue, gr=30, d=0.0):
    return ton(haken_i(x, y, cue, gr=gr, d=d), "minimal_check", 0.55)


def nein(x, y, cue, gr=28):
    return ton(kreuz_i(x, y, cue, gr=gr), "minimal_uncheck", 0.6)


def zeile(text, x, y, cue, stil="Regular", size=42, farbe=INK, d=0.0, **k):
    return OT(text, x, y, cue, stil, size, farbe=farbe, d=d, **k)


def plusminus(text, x, y, cue, plus, size=40, stil="Regular", d=0.0):
    z = "(+)" if plus else "(-)"
    breite = OT(text, 0, 0, "_", stil, size).sprite.width - 8 + F(stil, size).getlength(" ")
    return [OT(text, x, y, cue, stil, size, d=d),
            OT(z, x + breite, y, cue, "ExtraBold", size, farbe=(DGRUEN if plus else DROT), d=d)]


_icf = {}
def ficon(setname, name, cx, unten, breite, cue, fuell=None, nebenfarbe=WEISS, spiegeln=False, d=0.0, bis=None, anim="pop"):
    """Linien-Icon aus einer Bibliothek, unten auf 'unten' gestellt. Die größte umschlossene Fläche wird mit
    'fuell' gefüllt, kleinere umschlossene Flächen (Fenster, Radnaben) mit 'nebenfarbe' – die Linien bleiben original."""
    key = (setname, name, breite, fuell, nebenfarbe, spiegeln)
    if key not in _icf:
        if setname not in _icsets:
            _icsets[setname] = json.load(open(SP + f"blasen/{setname}/package/icons.json"))
        d_ = _icsets[setname]
        ic = d_["icons"][name]
        w = ic.get("width", d_.get("width", 24)); h = ic.get("height", d_.get("height", 24))
        svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}">{ic["body"]}</svg>'.replace("currentColor", "#151515")
        im = Image.open(io.BytesIO(cairosvg.svg2png(bytestring=svg.encode(), output_width=breite, output_height=int(breite * h / w)))).convert("RGBA")
        if fuell is not None:
            a = np.asarray(im)[..., 3] > 60
            lab, n = ndimage.label(~a)
            rand = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]])))
            innen = [(int((lab == i).sum()), i) for i in range(1, n + 1) if i not in rand]
            arr = np.asarray(im).copy()
            if innen:
                groesste = max(innen)[1]
                for gr_, i in innen:
                    if gr_ < 30:
                        continue
                    m = ndimage.binary_dilation(lab == i, iterations=1) & (arr[..., 3] < 250)
                    farbe = fuell if i == groesste else nebenfarbe
                    arr[m, :3] = farbe[:3]; arr[m, 3] = np.maximum(arr[m, 3], 255)
            im = Image.fromarray(arr)
            # Linien wieder obenauf, damit die Füllung nicht über die Kontur blutet
            linie = Image.open(io.BytesIO(cairosvg.svg2png(bytestring=svg.encode(), output_width=breite, output_height=int(breite * h / w)))).convert("RGBA")
            im.alpha_composite(linie)
        if spiegeln:
            im = ImageOps.mirror(im)
        im = im.crop(im.getbbox())
        _icf[key] = im
    im = _icf[key]
    return El(im, cx - im.width / 2, unten - im.height, cue, anim, d, bis, name=f"ficon:{name}")


from PIL import ImageOps
BODEN = 870
AUTO = (246, 165, 192, 255)
LKW = (249, 213, 110, 255)

# 1 Fall ------------------------------------------------------------------------------------------------
CX = 1150
folie([("fall", "Fall · Abschleppen")], [
    titel("Hanna parkt vor der Feuerwehrzufahrt", 80, 55, "fall", 64),
    linienzug([(60, BODEN), (1860, BODEN)], "fall", breite=7, farbe=INK),
    icon("fluent-emoji-high-contrast", "prohibited", 1690, 500, 150, "schild", farbe="#D73C2D"),
    pille("Absolutes Halteverbot", 1690, 590, "schild", fill=ROT, size=30, anker="m"),
    icon("ph", "fire-truck-duotone", 1690, 730, 130, "fall", farbe="#151515", d=0.4),
    pille("Feuerwehrzufahrt", 1690, 800, "fall", fill=GELB, size=30, anker="m", d=0.5),
    ficon("tabler", "car", CX, BODEN, 380, "fall", fuell=AUTO, d=0.2, bis="zurueck"),
    # Hanna geht weg (Geh-Pose, nach links) und ist verschwunden, wenn das Ordnungsamt kommt
    bewegt(peep_voll("H_geht", 560, BODEN, 540, "fall", d=0.3, bis="oa"), "weg", ("weg", 1.6), 300),
    blase("denk", 330, 190, "weg", 330, 300, inhalt=["Nur kurz", "zum Bäcker!"], textsize=34, ziel=(520, 360), bis="oa"),
    peep_voll("OA_ruhig", 420, BODEN, 540, "oa", bis="abschl"),
    peep_voll("OA_ruft", 420, BODEN, 540, "abschl", anim="cut", bis="zurueck"),
    pille("Ordnungsamt", 420, BODEN + 18, "oa", fill=BLAU, size=30, anker="m", d=0.2, bis="zurueck"),
    pille("Halterin nicht auffindbar", 420, 250, "niemand", fill=WEISS, size=30, anker="m", bis="abschl"),
    ficon("tabler", "truck", 790, BODEN, 330, "abschl", fuell=LKW, spiegeln=True, bis="zurueck"),
    pille("Abschleppwagen", 790, BODEN + 18, "abschl", fill=GELB, size=30, anker="m", d=0.4, bis="zurueck"),
    peep_voll("H_schreck", CX, BODEN, 540, "zurueck", bis="sauer"),
    peep_voll("H_sauer", CX, BODEN, 540, "sauer", anim="cut"),
    pille("Hanna", CX, BODEN + 18, "zurueck", fill=PINK, size=30, anker="m"),
    blase("sprech", 330, 200, "zurueck", 1450, 290, inhalt=["Mein Auto?!"], textsize=40, spiegeln=True, bis="sauer"),
    ficon("tabler", "receipt-euro", 560, 560, 190, "bescheid", fuell=(255, 255, 255, 255)),
    pille("Kostenbescheid: 250 €", 560, 590, "bescheid", fill=GELB, size=32, anker="m", d=0.2),
    blase("sprech", 520, 230, "sauer", 1460, 290, inhalt=["Mir wurde nichts verfügt", "und nichts angedroht!"], textsize=32, spiegeln=True),
    pille("Muss Hanna zahlen?", 960, 960, "frage", fill=PINK, size=40, anker="m"),
])

# 2 Einstieg: Kostenbescheid (Karte sofort vollständig) --------------------------------------------------
X0, X1, X2 = 170, 230, 290
folie([("schema", "Kostenbescheid › Prüfungsaufbau")], [
    karte(100, 70, 1300, 860, "schema"),
    titel("Rechtmäßigkeit des Kostenbescheids", X0, 120, "schema", 58),
    zeile("I. Rechtsgrundlage", X1, 240, "egl", "Bold", 44),
    zeile("Kostenregelung zur Ersatzvornahme im Landes-VwVG", X2, 305, "egl", size=38, farbe=TEXT, d=0.6),
    *plusminus("II. Formelle Rechtmäßigkeit", X1, 400, "form", True, size=44, stil="Bold"),
    zeile("III. Materielle Rechtmäßigkeit", X1, 490, "mat", "Bold", 44),
    zeile("Kosten nur, wenn die Abschleppmaßnahme", X2, 570, "konnex", "Bold", 40),
    zeile("selbst rechtmäßig war", X2, 625, "konnex", "Bold", 40),
    pille("Erst das Abschleppen prüfen, dann die Kosten", X2, 720, "konnex", fill=GELB, size=36, d=0.8),
    peep_voll("ER_erklaert", 1660, 1000, 720, "schema", d=0.4),
])

# 3 Grundverwaltungsakt -----------------------------------------------------------------------------------
folie([("gva", "III. Rechtmäßiges Abschleppen › Grundverwaltungsakt")], [
    titel("Welcher Verwaltungsakt wird vollstreckt?", 960, 55, "gva", 62, anker="m", d=0.0),
    zeile("Abschleppen = Ersatzvornahme = Vollstreckung eines Verwaltungsakts", 960, 140, "gva", "Bold", 34, farbe=TEXT, anker="m", d=0.6),
    zeile("Welcher?", 300, 220, "welcher", "ExtraBold", 48, anker="m"),
    icon("fluent-emoji-high-contrast", "prohibited", 300, 400, 220, "vz", farbe="#D73C2D"),
    pille("Verkehrszeichen", 300, 530, "vz", fill=ROT, size=34, anker="m", d=0.2),
    fl_block(560, 210, 780, 150, BLAU, "allg", [("Allgemeinverfügung", "ExtraBold", 44, INK), ("§ 35 S. 2 VwVfG", "Regular", 36, INK)]),
    fl_block(560, 385, 780, 150, GELB, "gebot", [("Halteverbot + Wegfahrgebot", "ExtraBold", 42, INK), ("verbotswidrig Parkende müssen wegfahren", "Regular", 32, INK)]),
    fl_block(560, 560, 780, 120, LILA, "bekannt", [("Bekanntgabe durch Aufstellen", "ExtraBold", 42, INK)]),
    zeile("Sichtbarkeitsgrundsatz:", 560, 715, "sicht", "Bold", 40),
    zeile("erkennbar mit raschem, beiläufigem Blick", 560, 770, "sicht", size=38, farbe=TEXT, d=0.4),
    peep_voll("H_nachdenklich", 1640, BODEN, 520, "hanna"),
    ok(590, 870, "hanna", gr=30),
    zeile("gilt auch, wenn Hanna es übersehen hat", 640, 848, "hanna", "Bold", 38, d=0.3),
])

# 4 Vollstreckungsvoraussetzungen (Karte sofort vollständig) ------------------------------------------------
folie([("vv", "III. Rechtmäßiges Abschleppen › Vollstreckung")], [
    karte(100, 60, 1330, 900, "vv"),
    titel("Vollstreckungsvoraussetzungen", X0, 110, "vv", 58),
    zeile("1. Vollziehbarer Grundverwaltungsakt", X1, 225, "sofort", "Bold", 42),
    ok(X2 + 20, 305, "sofort", gr=26), zeile("sofort vollziehbar analog § 80 II 1 Nr. 2 VwGO", X2 + 60, 285, "sofort", size=38, d=0.3),
    zeile("wirkt wie Anordnung eines Polizeivollzugsbeamten", X2 + 60, 340, "grund", size=34, farbe=TEXT),
    zeile("2. Richtiges Zwangsmittel", X1, 430, "vertretbar", "Bold", 42),
    zeile("Wegfahren = vertretbare Handlung", X2 + 60, 490, "vertretbar", size=38, d=0.4),
    ok(X2 + 20, 565, "ev", gr=26), zeile("Ersatzvornahme durch Abschleppunternehmer", X2 + 60, 545, "ev", size=38),
    zeile("3. Androhung und Festsetzung", X1, 635, "andro", "Bold", 42),
    ok(X2 + 20, 715, "eil", gr=26), zeile("im Eilfall nach Landesrecht entbehrlich", X2 + 60, 695, "eil", size=38),
    pille("Je nach Land: sofortiger Vollzug oder unmittelbare Ausführung", X1, 800, "tipp", fill=GELB, size=32),
    ficon("tabler", "truck", 1660, 520, 300, "ev", fuell=LKW),
    peep_voll("ER_arme", 1660, 1000, 440, "tipp"),
])

# 5 Verhältnismäßigkeit ----------------------------------------------------------------------------------------
folie([("vhm", "III. Rechtmäßiges Abschleppen › Verhältnismäßigkeit")], [
    titel("Verhältnismäßigkeit", 960, 55, "vhm", 70, anker="m"),
    fl_block(140, 200, 520, 150, GRUEN, "geeignet", [("geeignet", "ExtraBold", 48, INK)]),
    ok(700, 275, "geeignet"), zeile("Zufahrt wird frei", 750, 252, "geeignet", size=42),
    fl_block(140, 390, 520, 150, BLAU, "erf", [("erforderlich", "ExtraBold", 48, INK)]),
    ok(700, 465, "erf"), zeile("Hanna nicht erreichbar", 750, 442, "erf", size=42),
    zeile("keine lange Suche bei ungewissem Erfolg", 750, 495, "such", size=36, farbe=TEXT),
    fl_block(140, 580, 520, 150, PINK, "angem", [("angemessen", "ExtraBold", 48, INK)]),
    ok(700, 655, "vs"), zeile("Gefahr für Leib und Leben", 750, 610, "leben", "Bold", 42),
    zeile("wiegt schwerer als Hannas Nachteil", 750, 665, "vs", size=38, farbe=TEXT),
    icon("ph", "fire-truck-duotone", 1560, 600, 220, "leben", farbe="#151515"),
    icon("fluent-emoji-high-contrast", "balance-scale", 1560, 350, 170, "vs", farbe="#151515"),
])

# 6 Ergebnis ------------------------------------------------------------------------------------------------------
folie([("erg", "Ergebnis")], [
    titel("Ergebnis", 960, 55, "erg", 74, anker="m"),
    ok(260, 270, "erg", gr=36), zeile("Abschleppen rechtmäßig", 320, 240, "erg", "ExtraBold", 50),
    ok(260, 380, "kosten", gr=36), zeile("Kosten der Ersatzvornahme trägt die Pflichtige", 320, 350, "kosten", "Bold", 44),
    ficon("tabler", "receipt-euro", 520, 760, 200, "zahlen", fuell=(255, 255, 255, 255)),
    pille("Hanna zahlt 250 €", 720, 640, "zahlen", fill=GELB, size=44),
    peep_voll("H_skeptisch", 1560, BODEN, 560, "zahlen"),
    linienzug([(1300, BODEN), (1820, BODEN)], "zahlen", breite=7, farbe=INK),
])

# 7 Klausurschema (Karte sofort vollständig) -------------------------------------------------------------------------
K0, K1, K2 = 250, 310, 380
folie([("sch", "Klausurschema")], [
    karte(180, 50, 1560, 920, "sch"),
    titel("Klausurschema: Kostenbescheid", K0, 95, "sch", 60),
    zeile("I. Rechtsgrundlage: Kostenregelung Ersatzvornahme (Landesrecht)", K1, 205, "s1", "Bold", 40),
    *plusminus("II. Formelle Rechtmäßigkeit", K1, 280, "s2", True, stil="Bold", size=40),
    zeile("III. Materielle Rechtmäßigkeit: rechtmäßige Ersatzvornahme", K1, 355, "s3", "Bold", 40),
    *plusminus("1. Grundverwaltungsakt: Verkehrszeichen (Allgemeinverfügung)", K2, 425, "s4", True, size=38),
    *plusminus("2. Vollziehbarkeit analog § 80 II 1 Nr. 2 VwGO", K2, 485, "s4", True, size=38, d=0.8),
    *plusminus("3. Zwangsmittel Ersatzvornahme; Androhung im Eilfall entbehrlich", K2, 545, "s5", True, size=38),
    *plusminus("4. Verhältnismäßigkeit", K2, 605, "s5", True, size=38, d=1.2),
    *plusminus("IV. Kostenpflicht der Halterin", K1, 685, "s6", True, stil="Bold", size=40),
    pille("Ergebnis: Kostenbescheid rechtmäßig", K1, 780, "s6", fill=GRUEN, size=40, d=0.8),
])

# 8 Merksatz -----------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=(255, 251, 230, 255)),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Erst das ", 0), ("Abschleppen", "a"), (" prüfen,", 0)], [("dann die ", 0), ("Kosten", "b"), (".", 0)]],
                750, 330, 52, "merke", {"a": ("merke", 1.8), "b": ("merke", 3.0)}),
    *markertext([[("Das ", 0), ("Verkehrszeichen", "c"), (" ist der Verwaltungsakt,", 0)],
                 [("den die Behörde vollstreckt.", 0)]], 750, 560, 50, "m2", {"c": ("m2", 0.8)}),
    peep_voll("ER_freut", 1680, 1000, 720, "merke", d=0.4),
])
