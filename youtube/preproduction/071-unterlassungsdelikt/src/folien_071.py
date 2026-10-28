"""Folge 071 · Unterlassungsdelikt Schema: Unechtes Unterlassen § 13 StGB – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A Garten am Sommernachmittag (Liegestuhl, Ball, Teich, Zaun, Nachbarin, Rettungswagen),
B Sachverhalt, C Vorab Tun/Unterlassen und Vorprüfung, D Wortlautkarte § 13 Abs. 1, E Tatentschluss 1.–2. (Erfolg,
Nichtvornahme trotz Möglichkeit), F 3. Quasikausalität, G 4. Garantenstellung, H 5. Entsprechungsklausel,
I Ansetzen, Rechtswidrigkeit, Schuld/Zumutbarkeit, Rücktritt, J Ergebnis und Strafmilderung, K Abwandlung § 222,
L Abgrenzung § 323c, M Klausurtipp (Lexi), N Prüfschema, O Merksatz (Lexi).
Sehr zurückhaltend: kein Kind im Wasser, kein Ertrinken, kein Leid; das Kind nur als abstraktes Icon an Land (Tabler
mood-kid), der Sturz nur als Ball und Wellen-Symbol auf dem Teich, der Rettungswagen als Symbol. Lutz sachlich.
Geräusche nur bei sichtbarer Handlung: Ball plumpst ins Wasser (Freesound CC0)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont

bausteine.FIGORDNER = "op_071/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
LILAHELL = (246, 243, 255, 255)
ROTHELL = (253, 232, 228, 255)
GRUENHELL = (232, 247, 233, 255)
BLAUHELL = (228, 238, 253, 255)
HOLZ = (214, 160, 110, 255)
RASEN = (143, 214, 148, 255)
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
    """Wortlautkarte: wörtliches Zitat (gesetze-im-internet.de, Abruf 02.10.2026) in einer hellen Karte, Fundstelle darunter
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


def teich(cx, cy, rx, ry, cue, fill=BLAU, rand=5):
    """Gartenteich als Grundform (gefüllte Ellipse mit Tuschekontur), wie die Karten der Bausteine; keine Figur im Wasser."""
    s = 3
    im = Image.new("RGBA", ((2 * rx + 20) * s, (2 * ry + 20) * s))
    dr = ImageDraw.Draw(im)
    dr.ellipse((10 * s, 10 * s, (2 * rx + 10) * s, (2 * ry + 10) * s), fill=INK)
    dr.ellipse(((10 + rand) * s, (10 + rand) * s, (2 * rx + 10 - rand) * s, (2 * ry + 10 - rand) * s), fill=fill)
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    return El(im, cx - rx - 10, cy - ry - 10, cue, "fade", 0.0, name="teich")


def streifen(p0, p1, cue, breite=34, fill=GELB):
    """Stoffbahn des Liegestuhls: Tuschestreifen mit farbiger Füllung (zwei Linienzüge)."""
    return [linienzug([p0, p1], cue, breite=breite + 10, farbe=INK), linienzug([p0, p1], cue, breite=breite, farbe=fill)]


# --- Eigene Hilfsfunktion (wie Folge 068): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt -----------------
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
X1, X2 = 1420, 1720                     # Lutz (links), Gesa (rechts)
MB = (X1 + X2) // 2
XS = 1640                               # eine Figur allein neben der Tafel
IX = 1440                               # Requisit neben der Einzelfigur


def kette(prefix, x, folge, bis_=None, d=0.0):
    """Eine Figur mit Mimikfolge [(Name, Cue), …] im Zwiebelschalenprinzip (erster Auftritt pop, danach harte Schnitte)."""
    els = []
    for i, (n, c) in enumerate(folge):
        b = folge[i + 1][1] if i + 1 < len(folge) else bis_
        els.append(peep_voll(prefix + n, x, BR, FR, c, anim=("pop" if i == 0 else "cut"), d=(d if i == 0 else 0.0), bis=b))
    return els


def lutz(cue, folge=(), x=XS):
    """Lutz allein rechts neben der Tafel, mit Namensschild ab dem ersten Bild der Folie."""
    return kette("LU_", x, [("ernst", cue)] + list(folge)) + [namensschild("Lutz", x, BR, cue, BLAU, d=0.2)]


def paar(cue, lu, ge, lu_folge=(), ge_folge=()):
    els = kette("LU_", X1, [(lu, cue)] + list(lu_folge)) + kette("GE_", X2, [(ge, cue)] + list(ge_folge), d=0.2)
    return els + [namensschild("Lutz", X1, BR, cue, BLAU, d=0.2), namensschild("Gesa", X2, BR, cue, ROT, d=0.3)]


# A Fall: Sommernachmittag im Garten ------------------------------------------------------------------------------------------
BODEN = 880
LSX, LS_UNTEN, LSH = 430, 815, 410      # Lutz im Liegestuhl (blickt nach rechts zum Teich)
TX, TY = 1000, 905                      # Teich (Mitte), flach am Boden
KX = 720                                # Sohn (Icon) mit Ball auf dem Rasen, links vom Teich
ZX = 1420                               # Zaun zum Nachbargarten
GX, GH = 1700, 540                      # Gesa im Nachbargarten (blickt nach links)
GX2 = 1250                              # Gesa am Teich (rechts neben dem Wasser)
LSa = ("LS_redet_r", LSX, LS_UNTEN, LSH)
GEa = ("GE_redet", GX2, BODEN, GH)
heraus = beim("zaun", "heraus")
folie([(NULL, "Fall · Sommernachmittag im Garten"), ("ball", "Fall · Der Ball rollt ins Wasser"),
       ("sitzt", "Fall · Lutz bleibt sitzen"), ("gesa", "Fall · Die Nachbarin hilft"), ("frage", "Fall · Die Frage")], [
    linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK),
    pl("Ein heißer Sommernachmittag", 70, 40, NULL, fill=GELB, size=36),
    ficon("tabler", "sun", 1790, 200, 110, NULL, fuell=GELB),
    ficon("fluent-emoji-flat", "deciduous-tree", 150, BODEN - 2, 220, NULL),
    # Zaun zum Nachbargarten
    ficon("tabler", "fence", ZX, BODEN, 130, NULL, fuell=HOLZ),
    ficon("tabler", "fence", ZX + 125, BODEN, 130, NULL, fuell=HOLZ),
    # Liegestuhl: Gestell (Linienzüge) und Stoffbahn; Lutz sitzt darin
    linienzug([(LSX - 170, BODEN), (LSX + 130, LS_UNTEN - 60)], NULL, breite=10, farbe=INK),
    linienzug([(LSX + 210, BODEN), (LSX - 120, int(LS_UNTEN - LSH * 0.6))], NULL, breite=10, farbe=INK),
    *streifen((LSX - 165, int(LS_UNTEN - LSH * 0.9)), (LSX - 40, LS_UNTEN - 60), NULL),
    *streifen((LSX - 40, LS_UNTEN - 60), (LSX + 200, LS_UNTEN - 50), NULL),
    peep_voll("LS_ruhig_r", LSX, LS_UNTEN, LSH, NULL, bis="l1"),
    *redet("LS_redet_r", LSX, LS_UNTEN, LSH, "l1", "ball"),
    peep_voll("LS_ruhig_r", LSX, LS_UNTEN, LSH, "ball", anim="cut", bis="sieht"),
    peep_voll("LS_ernst_r", LSX, LS_UNTEN, LSH, "sieht", anim="cut"),
    namensschild("Lutz", LSX, BODEN, NULL, BLAU),
    pl("im Liegestuhl", LSX, 300, beim("lutz", "liegt"), fill=WEISS, size=30, anker="m", bis="l1"),
    # Teich, Sohn (abstraktes Icon), Ball
    teich(TX, TY - 10, 170, 40, beim("sohn", "Gartenteich")),
    pl("Gartenteich, flach", TX, 760, beim("sohn", "Gartenteich"), fill=BLAUHELL, size=30, anker="m", bis="ball"),
    ficon("tabler", "mood-kid", KX, BODEN - 4, 90, "sohn", fuell=GELB, bis="faellt"),
    pl("Sohn, 2 Jahre", KX, 620, beim("sohn", "zweijähriger"), fill=WEISS, size=30, anker="m", bis="ball"),
    ficon("tabler", "ball-football", KX + 75, BODEN - 4, 50, beim("sohn", "Ball"), fuell=WEISS, bis="ball"),
    blase("sprech", 560, 170, "l1", 900, 330, inhalt=["Spiel schön, ich ruh", "mich kurz aus."], textsize=32, figur=LSa,
          bis="ball"),
    szene(bewegt(ficon("tabler", "ball-football", TX - 40, TY - 22, 50, "ball", fuell=WEISS, anim="cut", bis="frage"),
                 "ball", ("ball", 0.9), KX + 75 - (TX - 40), (BODEN - 4) - (TY - 22)), "071plumps*", 1.0, versatz=0.85),
    pl("Der Ball rollt ins Wasser.", TX, 640, "ball", fill=WEISS, size=30, anker="m", bis="faellt"),
    ficon("fluent-emoji-flat", "water-wave", TX + 70, TY - 18, 80, "faellt", bis=heraus),
    pl("Der Junge fällt in den Teich.", TX, 640, "faellt", fill=ROTHELL, size=30, anker="m", bis="sieht"),
    # Lutz sieht es, könnte helfen, bleibt sitzen
    pl("sieht es genau", LSX, 300, "sieht", fill=WEISS, size=30, anker="m", bis="sitzt"),
    pfeil(560, 740, TX - 190, 830, beim("sieht", "wenigen"), breite=8, kopf=26, farbe=INK, bis="sitzt"),
    pl("wenige Schritte: sicher zu retten", TX - 60, 640, beim("sieht", "wenigen"), fill=GRUENHELL, size=30, anker="m",
       bis="sitzt"),
    pl("Er bleibt sitzen.", LSX, 300, "sitzt", fill=GELB, size=30, anker="m", bis="gesa"),
    pl("hält den Tod für möglich,", TX - 60, 600, "vors", fill=WEISS, size=30, anker="m", bis="gesa"),
    pl("nimmt ihn billigend in Kauf", TX - 60, 670, beim("vors", "billigend"), fill=WEISS, size=30, anker="m", bis="gesa"),
    # Die Nachbarin Gesa (blickt nach links), springt über den Zaun, zieht den Jungen heraus
    peep_voll("GE_schreck", GX, BODEN, GH, "gesa", anim="pop", bis="zaun"),
    namensschild("Gesa", GX, BODEN, "gesa", ROT, d=0.2, bis="zaun"),
    pl("Nachbarin", GX, 250, beim("gesa", "Nachbarin"), fill=WEISS, size=30, anker="m", bis="zaun"),
    bewegt(peep_voll("GE_ernst", GX2, BODEN, GH, "zaun", anim="cut", bis="g1"), "zaun", ("zaun", 0.8), GX - GX2, 0),
    bewegt(namensschild("Gesa", GX2, BODEN, "zaun", ROT, anim="cut"), "zaun", ("zaun", 0.8), GX - GX2, 0),
    pl("springt über den Zaun", GX2, 250, beim("zaun", "springt"), fill=WEISS, size=30, anker="m", bis=heraus),
    ficon("tabler", "mood-kid", GX2 - 110, 690, 84, heraus, fuell=GELB),        # Junge an Land in den Armen von Gesa
    pl("zieht ihn heraus", GX2, 250, heraus, fill=GRUENHELL, size=30, anker="m", bis="g1"),
    *redet("GE_redet", GX2, BODEN, GH, "g1", "rtw"),
    peep_voll("GE_froh", GX2, BODEN, GH, "rtw", anim="cut"),
    blase("sprech", 480, 170, "g1", 1490, 210, inhalt=["Ich hab dich!", "Alles gut."], textsize=34, figur=GEa, bis="rtw"),
    # Rettungswagen zur Kontrolle, Junge unverletzt
    ficon("fluent-emoji-flat", "ambulance", 1765, BODEN - 2, 220, beim("rtw", "Rettungswagen")),
    pl("zur Kontrolle ins Krankenhaus", 1650, 560, beim("rtw", "Kontrolle"), fill=WEISS, size=30, anker="m", bis="frage"),
    pl("Ihm fehlt nichts.", 1650, 640, beim("rtw", "fehlt"), fill=GRUEN, size=30, anker="m", bis="frage"),
    # Die Frage
    pl("Nichts getan – trotzdem strafbar?", 860, 180, "frage", fill=WEISS, size=34, anker="m"),
    pl("Tötungsdelikt?", 860, 270, "frage2", fill=PINK, size=34, anker="m"),
])

# B Sachverhalt ----------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    glyphen("An einem heißen Sommernachmittag liegt Lutz in seinem Garten im Liegestuhl. Er ist allein mit seinem "
            "2-jährigen Sohn, für den er sorgeberechtigt ist. Der Junge spielt mit einem Ball; ein paar Meter weiter liegt "
            "ein flacher Gartenteich."),
    glyphen("Der Ball rollt ins Wasser, der Junge läuft hinterher und fällt in den Teich. Lutz sieht das genau. Mit wenigen "
            "Schritten könnte er seinen Sohn sicher herausholen, das weiß er. Er bleibt sitzen; er hält es für möglich, "
            "dass sein Sohn ertrinkt, und nimmt das billigend in Kauf. Nach etwa einer Minute bemerkt die Nachbarin Gesa "
            "den Jungen, springt über den Zaun und zieht ihn heraus. Ihm fehlt nichts."),
], "Hat sich Lutz strafbar gemacht?")

# C Vorab: Tun oder Unterlassen, Vorprüfung ----------------------------------------------------------------------------------
PA = "A. Versuchter Totschlag durch Unterlassen"
folie([("tun", "Vorab · Tun oder Unterlassen?"), ("unterl", "Vorab › Unterlassen"),
       ("vollend", f"{PA} › Vorprüfung: keine Vollendung"), ("verbr", f"{PA} › Vorprüfung: Versuch strafbar"),
       ("versuch", f"{PA}, §§ 212, 13, 22, 23 StGB")], rechts_frei([
    *tafel("tun", "Vorab: Tun oder Unterlassen?"),
    z("Kriterium: Schwerpunkt der Vorwerfbarkeit", 110, 185, beim("tun", "Schwerpunkt"), "Bold", 32),
    fund("BGH, Beschl. v. 17.3.2022 – 2 StR 157/21, Rn. 13", 150, 232, beim("tun", "Schwerpunkt")),
    ok(135, 310, beim("unterl", "Also"), gr=18),
    z("Vorwurf: nicht geholfen – also Unterlassen", 175, 290, "unterl", size=32),
    z("Vorprüfung:", 110, 375, "vollend", "ExtraBold", 34),
    nein(135, 450, "vollend", gr=18),
    z("Sohn lebt: kein vollendeter Totschlag", 175, 430, "vollend", size=32),
    ok(135, 515, "verbr", gr=18),
    z("Totschlag ist Verbrechen: Versuch stets strafbar", 175, 495, "verbr", size=32),
    fund("§ 12 Abs. 1, § 23 Abs. 1 StGB", 175, 542, beim("verbr", "Versuch")),
    fl_block(110, 610, 1040, 130, GELB, "versuch", [("Versuchter Totschlag durch Unterlassen", "ExtraBold", 34, INK),
                                                    ("§§ 212, 13, 22, 23 StGB", "Bold", 32, INK)]),
    *paar("tun", "ernst", "ruhig", lu_folge=[("still", "unterl")], ge_folge=[("ernst", "vollend")]),
    pl("Tun oder Unterlassen?", MB, 160, "tun", fill=WEISS, size=28, anker="m", bis="unterl"),
    pl("nur sitzen geblieben", MB, 160, "unterl", fill=WEISS, size=28, anker="m", anim="cut", bis="vollend"),
    ficon("tabler", "armchair", MB, 380, 100, "unterl", fuell=GELB, bis="vollend"),
    pl("Sohn lebt", MB, 160, "vollend", fill=GRUENHELL, size=30, anker="m", anim="cut", bis="verbr"),
    ficon("tabler", "mood-kid", MB, 380, 100, "vollend", fuell=GELB, bis="verbr"),
    pl("Versuch?", MB, 160, "verbr", fill=GELB, size=30, anker="m", anim="cut"),
    ficon("tabler", "scale", MB, 380, 100, "verbr", fuell=GELB, anim="cut"),
]))

# D Wortlautkarte § 13 Abs. 1 ----------------------------------------------------------------------------------------------
W13 = [[("„Wer es unterläßt, ", 0), ("einen Erfolg abzuwenden", "a"), (", der zum Tatbestand", 0)],
       [("eines Strafgesetzes gehört, ist nach diesem Gesetz nur dann", 0)],
       [("strafbar, wenn er ", 0), ("rechtlich dafür einzustehen hat", "b"), (", daß der", 0)],
       [("Erfolg nicht eintritt, und wenn das Unterlassen der", 0)],
       [("Verwirklichung des gesetzlichen Tatbestandes ", 0), ("durch ein Tun", "c")],
       [("entspricht", "c"), (".“", 0)]]
folie([("p13", f"{PA} › § 13 Abs. 1 StGB"), ("einst", f"{PA} › § 13 Abs. 1: Garantenstellung"),
       ("entspr", f"{PA} › § 13 Abs. 1: Entsprechung")], rechts_frei([
    *tafel("p13", "Die Norm: § 13 Abs. 1 StGB"),
    *wortlaut(110, 185, 1040, 300, "p13", W13, 31,
              {"a": beim("p13", "Erfolg"), "b": "einst", "c": beim("entspr", "durch")}, "§ 13 Abs. 1 StGB"),
    z("rechtlich einstehen müssen: Garantenstellung", 110, 570, "einst", "Bold", 32),
    z("Unterlassen entspricht Tun: Entsprechungsklausel", 110, 635, "entspr", "Bold", 32),
    *lutz("p13"),
    pl("§ 13 StGB", IX + 60, 160, beim("p13", "Paragraf"), fill=GELB, size=30, anker="m", bis="einst"),
    pl("Garant?", IX + 60, 160, "einst", fill=WEISS, size=30, anker="m", anim="cut", bis="entspr"),
    ficon("tabler", "shield", IX + 60, 380, 100, "einst", fuell=BLAU, bis="entspr"),
    pl("Entsprechung?", IX + 60, 160, "entspr", fill=WEISS, size=30, anker="m", anim="cut"),
    ficon("tabler", "scale", IX + 60, 380, 100, "entspr", fuell=GELB, anim="cut"),
]))

# E Tatentschluss: 1. Erfolg, 2. Nichtvornahme trotz Möglichkeit ----------------------------------------------------------
PT = f"{PA} › I. Tatentschluss"
folie([("tat", PT), ("erfolg", f"{PT} › 1. Erfolg"), ("erfolg2", f"{PT} › 1. Erfolg: bedingter Vorsatz"),
       ("moegl", f"{PT} › 2. Nichtvornahme trotz Möglichkeit")], rechts_frei([
    *tafel("tat", "I. Tatentschluss"),
    z("Vorstellung von allen objektiven Merkmalen", 110, 180, "tat", "Bold", 32),
    fund("BGH, Beschl. v. 9.3.2022 – 4 StR 200/21, Rn. 10", 150, 227, beim("tat", "Tatentschluss")),
    z("1. Erfolg: Tod des Sohnes", 110, 300, "erfolg", "ExtraBold", 34),
    ok(135, 375, "erfolg2", gr=18),
    z("sieht die Lebensgefahr, nimmt den Tod", 175, 355, "erfolg2", size=32),
    z("billigend in Kauf: bedingter Vorsatz", 175, 400, beim("erfolg2", "Kauf"), size=32),
    fund("BGH, Urt. v. 31.3.2021 – 2 StR 109/20, Rn. 12", 175, 447, beim("erfolg2", "bedingter")),
    z("2. Nichtvornahme trotz physisch-realer Möglichkeit", 110, 520, "moegl", "ExtraBold", 34),
    ok(135, 595, "moegl2", gr=18),
    z("Teich nah und flach: Lutz kann ihn herausziehen", 175, 575, "moegl2", size=32),
    z("Das weiß er.", 175, 620, beim("moegl2", "Das"), "Bold", 32),
    *lutz("tat", [("sorge", "erfolg2"), ("ernst", "moegl")]),
    pl("Vorstellung", IX + 60, 160, "tat", fill=WEISS, size=30, anker="m", bis="erfolg"),
    ficon("tabler", "bulb", IX + 60, 380, 100, "tat", fuell=GELB, bis="erfolg"),
    pl("Lebensgefahr", IX + 60, 160, "erfolg", fill=ROTHELL, size=30, anker="m", anim="cut", bis="moegl"),
    ficon("fluent-emoji-flat", "water-wave", IX + 60, 380, 100, "erfolg", anim="cut", bis="moegl"),
    pl("Rettung möglich", IX + 60, 160, "moegl", fill=GRUENHELL, size=30, anker="m", anim="cut"),
    ficon("tabler", "lifebuoy", IX + 60, 380, 100, "moegl", fuell=ROT, anim="cut"),
]))

# F 3. Quasikausalität ------------------------------------------------------------------------------------------------------
folie([("quasi", f"{PT} › 3. Quasikausalität"), ("quasi2", f"{PT} › 3. Quasikausalität: Rettung sicher"),
       ("zurech", f"{PT} › 3. objektive Zurechnung")], rechts_frei([
    *tafel("quasi", "3. Quasikausalität"),
    z("Unterlassen ursächlich, wenn die gebotene", 110, 185, beim("quasi", "Ein"), "Bold", 32),
    z("Handlung den Erfolg verhindert hätte:", 110, 230, beim("quasi", "Handlung"), "Bold", 32),
    fl_block(110, 290, 1040, 90, GELB, beim("quasi", "Sicherheit"),
             [("mit an Sicherheit grenzender Wahrscheinlichkeit", "ExtraBold", 32, INK)]),
    fund("BGH, Urt. v. 12.1.2010 – 1 StR 272/09, Rn. 65 f.", 150, 395, beim("quasi", "Sicherheit")),
    fund("BGH, Beschl. v. 9.3.2022 – 4 StR 200/21, Rn. 16 f.", 150, 432, beim("quasi", "Sicherheit")),
    ok(135, 520, "quasi2", gr=18),
    z("Lutz weiß: sofort herausgezogen,", 175, 500, "quasi2", size=32),
    z("überlebt der Junge sicher", 175, 545, beim("quasi2", "überlebt"), size=32),
    ok(135, 640, "zurech", gr=18),
    z("objektive Zurechnung (Lehre): unproblematisch", 175, 620, "zurech", size=32),
    *lutz("quasi", [("ruhig", "zurech")]),
    pl("Rettung hinzudenken", IX + 60, 160, "quasi", fill=WEISS, size=28, anker="m", bis="quasi2"),
    ficon("tabler", "lifebuoy", IX + 60, 380, 100, "quasi", fuell=ROT, bis="quasi2"),
    pl("Junge überlebt", IX + 60, 160, "quasi2", fill=GRUENHELL, size=30, anker="m", anim="cut", bis="zurech"),
    ficon("tabler", "mood-kid", IX + 60, 380, 100, "quasi2", fuell=GELB, anim="cut"),
    pl("zurechenbar", IX + 60, 160, "zurech", fill=WEISS, size=30, anker="m", anim="cut"),
]))

# G 4. Garantenstellung ----------------------------------------------------------------------------------------------------
folie([("garant", f"{PT} › 4. Garantenstellung"), ("eltern", f"{PT} › 4. Beschützergarant: Vater"),
       ("ueberw", f"{PT} › 4. Überblick: Überwachergarant"), ("ing", f"{PT} › 4. Überblick: Ingerenz")], rechts_frei([
    *tafel("garant", "4. Garantenstellung"),
    z("rechtlich dafür einstehen, dass der Erfolg", 110, 185, "garant", "Bold", 32),
    z("nicht eintritt (§ 13 Abs. 1 StGB)", 110, 230, beim("garant", "nicht"), "Bold", 32),
    karte(110, 300, 1040, 180, "eltern", fill=GRUENHELL, rund=18, schatten=6, rand=4),
    z("Beschützergarant: sorgeberechtigter Vater", 140, 320, "eltern", "ExtraBold", 32),
    ok(160, 390, "bgb", gr=16),
    z("sorgen und beaufsichtigen, §§ 1626 Abs. 1, 1631 Abs. 1 BGB", 195, 372, "bgb", size=29, rechts=1140),
    fund("BGH, Urt. v. 7.10.2025 – 3 StR 11/25, Rn. 17 f.", 195, 420, beim("bgb", "beaufsichtigen")),
    karte(110, 520, 1040, 200, "ueberw", fill=LILAHELL, rund=18, schatten=6, rand=4),
    z("Überblick: Überwachergarant", 140, 540, "ueberw", "ExtraBold", 32),
    z("Herrschaft über eine Gefahrenquelle", 140, 592, beim("ueberw", "Gefahrenquelle"), size=30, rechts=1140),
    z("pflichtwidriges Vorverhalten: Ingerenz", 140, 642, "ing", size=30, rechts=1140),
    pl("eigene Folgen", 140, 745, beim("ing", "eigene"), fill=LILA, size=28),
    *lutz("garant", [("ruhig", "ueberw")]),
    pl("rechtlich einstehen?", IX + 60, 160, "garant", fill=WEISS, size=28, anker="m", bis="eltern"),
    ficon("tabler", "shield", IX + 60, 380, 100, "garant", fuell=WEISS, bis="eltern"),
    pl("Vater", IX + 60, 160, "eltern", fill=GRUENHELL, size=30, anker="m", anim="cut", bis="ueberw"),
    ficon("tabler", "shield-check", IX + 60, 380, 100, "eltern", fuell=GRUEN, anim="cut", bis="ueberw"),
    pl("Gefahrenquelle", IX + 60, 160, "ueberw", fill=LILAHELL, size=28, anker="m", anim="cut", bis="ing"),
    ficon("tabler", "alert-triangle", IX + 60, 380, 100, "ueberw", fuell=GELB, anim="cut"),
    pl("Ingerenz", IX + 60, 160, "ing", fill=LILAHELL, size=30, anker="m", anim="cut"),
]))

# H 5. Entsprechungsklausel ------------------------------------------------------------------------------------------------
folie([("entspr2", f"{PT} › 5. Entsprechungsklausel"), ("verh", f"{PT} › 5. Entsprechung (+)")], rechts_frei([
    *tafel("entspr2", "5. Entsprechungsklausel"),
    z("§ 13 Abs. 1 Halbsatz 2 StGB", 110, 185, "entspr2", "Bold", 32),
    ok(135, 270, beim("entspr2", "reinen"), gr=18),
    z("reines Erfolgsdelikt wie der Totschlag:", 175, 250, beim("entspr2", "reinen"), size=32),
    z("regelmäßig unproblematisch", 175, 295, beim("entspr2", "regelmäßig"), "Bold", 32),
    z("Bedeutung bei Delikten mit bestimmter", 110, 390, "verh", size=32),
    z("Begehungsweise", 110, 435, beim("verh", "Begehungsweise"), size=32),
    *lutz("entspr2"),
    pl("§ 212: Erfolgsdelikt", IX + 60, 160, beim("entspr2", "reinen"), fill=WEISS, size=28, anker="m", bis="verh"),
    ficon("tabler", "scale", IX + 60, 380, 100, beim("entspr2", "reinen"), fuell=GELB),
    pl("Begehungsweise", IX + 60, 160, "verh", fill=WEISS, size=28, anker="m", anim="cut"),
]))

# I Ansetzen, Rechtswidrigkeit, Schuld, Rücktritt --------------------------------------------------------------------------
folie([("ansetz", f"{PA} › II. unmittelbares Ansetzen"), ("rw", f"{PA} › III. Rechtswidrigkeit"),
       ("zumut", f"{PA} › IV. Schuld: Zumutbarkeit"), ("rueck", f"{PA} › V. kein Rücktritt, § 24 StGB")], rechts_frei([
    *tafel("ansetz", "II.–V.: Ansetzen bis Rücktritt"),
    ok(135, 200, beim("ansetz", "angesetzt"), gr=18),
    z("II. unmittelbares Ansetzen: spätestens,", 175, 180, beim("ansetz", "angesetzt"), "Bold", 32),
    z("als der Sohn im Wasser liegt und er sitzen bleibt", 175, 225, beim("ansetz", "Sohn"), size=31),
    z("Leben unmittelbar gefährdet", 175, 270, beim("ansetz", "Leben"), size=31),
    ok(135, 345, "rw", gr=18),
    z("III. Rechtswidrigkeit: keine Rechtfertigung", 175, 325, "rw", "Bold", 32),
    ok(135, 420, beim("zumut", "Rettung"), gr=18),
    z("IV. Schuld: Zumutbarkeit", 175, 400, "zumut", "Bold", 32),
    z("Rettung ohne Gefahr möglich: zumutbar", 175, 445, beim("zumut", "Rettung"), size=31),
    fund("Standort der Zumutbarkeit umstritten (Tatbestand oder Schuld)", 175, 492, "standort"),
    nein(135, 575, "rueck", gr=18),
    z("V. Rücktritt, § 24 Abs. 1 Satz 2 StGB:", 175, 555, "rueck", "Bold", 32),
    z("gerettet hat Gesa; Lutz hat sich nicht bemüht", 175, 600, beim("rueck", "Gerettet"), size=31),
    *paar("ansetz", "ernst", "ruhig", lu_folge=[("still", "rueck")], ge_folge=[("froh", beim("rueck", "Gerettet"))]),
    pl("Leben in Gefahr", MB, 160, "ansetz", fill=ROTHELL, size=28, anker="m", bis="rw"),
    ficon("fluent-emoji-flat", "water-wave", MB, 380, 100, "ansetz", bis="zumut"),
    pl("keine Rechtfertigung", MB, 160, "rw", fill=WEISS, size=28, anker="m", anim="cut", bis="zumut"),
    pl("zumutbar", MB, 160, "zumut", fill=GRUENHELL, size=30, anker="m", anim="cut", bis="rueck"),
    ficon("tabler", "lifebuoy", MB, 380, 100, "zumut", fuell=ROT, anim="cut", bis="rueck"),
    pl("Rettung durch Gesa", MB, 160, "rueck", fill=WEISS, size=28, anker="m", anim="cut"),
    ficon("tabler", "mood-kid", MB, 380, 100, "rueck", fuell=GELB, anim="cut"),
]))

# J Ergebnis, Strafmilderung ----------------------------------------------------------------------------------------------
folie([("erg", "Ergebnis · Lutz strafbar nach §§ 212, 13, 22, 23 StGB"), ("milder", "Strafmilderung · § 13 Abs. 2, § 23 Abs. 2 StGB")],
      rechts_frei([
    *tafel("erg", "Ergebnis"),
    fl_block(110, 190, 1040, 130, GRUEN, "erg", [("Lutz: strafbar wegen versuchten", "ExtraBold", 34, INK),
                                                 ("Totschlags durch Unterlassen", "ExtraBold", 34, INK)]),
    z("Strafmilderung möglich:", 110, 380, "milder", "ExtraBold", 34),
    z("§ 13 Abs. 2 StGB i. V. m. § 49 Abs. 1 StGB", 140, 440, beim("milder", "dreizehn"), "Bold", 32),
    z("wegen des Versuchs: § 23 Abs. 2 StGB", 140, 495, beim("milder", "Versuchs"), "Bold", 32),
    *lutz("erg", [("still", "milder")]),
    pl("strafbar", IX + 60, 160, "erg", fill=GRUEN, size=30, anker="m", bis="milder"),
    ficon("tabler", "gavel", IX + 60, 380, 100, "erg", fuell=HOLZ, bis="milder"),
    pl("kann gemildert werden", IX + 60, 160, "milder", fill=WEISS, size=28, anker="m", anim="cut"),
    ficon("tabler", "scale", IX + 60, 380, 100, "milder", fuell=GELB, anim="cut"),
]))

# K Abwandlung § 222 --------------------------------------------------------------------------------------------------------
folie([("ab", "Abwandlung · fahrlässige Tötung durch Unterlassen, §§ 222, 13 StGB")], rechts_frei([
    *tafel("ab", "Abwandlung: nicht aufgepasst", fill=ROTHELL),
    z("Lutz bemerkt den Sturz nicht,", 110, 200, beim("ab", "Bemerkt"), "Bold", 34),
    z("weil er pflichtwidrig nicht aufpasst", 110, 255, beim("ab", "pflichtwidrig"), "Bold", 34),
    z("Hilfe kommt zu spät", 110, 310, beim("ab", "kommt"), "Bold", 34),
    ok(135, 405, beim("ab", "fahrlässige"), gr=20),
    z("fahrlässige Tötung durch Unterlassen,", 175, 385, beim("ab", "fahrlässige"), "Bold", 34),
    z("§§ 222, 13 StGB", 175, 440, beim("ab", "Paragrafen"), "Bold", 34),
    *lutz("ab", [("sorge", beim("ab", "fahrlässige"))]),
    pl("nicht aufgepasst", IX + 60, 160, beim("ab", "pflichtwidrig"), fill=WEISS, size=28, anker="m"),
    ficon("tabler", "eye-off", IX + 60, 380, 100, beim("ab", "pflichtwidrig"), fuell=WEISS),
]))

# L Abgrenzung § 323c ------------------------------------------------------------------------------------------------------
folie([("p323", "Abgrenzung › unterlassene Hilfeleistung, § 323c StGB"), ("echt", "Abgrenzung › echtes Unterlassungsdelikt")],
      rechts_frei([
    *tafel("p323", "Abgrenzung: § 323c StGB", fill=LILAHELL),
    z("unterlassene Hilfeleistung, § 323c StGB:", 110, 200, "p323", "ExtraBold", 34),
    z("echtes Unterlassungsdelikt", 110, 270, "echt", "Bold", 34),
    z("bestraft das Nichthelfen selbst", 110, 325, beim("echt", "Nichthelfen"), "Bold", 34),
    z("trifft jeden, auch ohne Garantenstellung", 110, 380, beim("echt", "jeden"), "Bold", 34),
    fund("vgl. BGH, Urt. v. 31.3.2021 – 2 StR 109/20, Rn. 24", 150, 430, beim("echt", "jeden")),
    pl("eigene Folge", 110, 500, beim("echt", "Garantenstellung"), fill=LILA, size=30),
    *paar("p323", "ruhig", "ruhig"),
    pl("§ 323c StGB", MB, 160, "p323", fill=LILA, size=30, anker="m", bis=beim("echt", "jeden")),
    pl("jeder muss helfen", MB, 160, beim("echt", "jeden"), fill=WEISS, size=28, anker="m", anim="cut"),
    ficon("tabler", "users", MB, 380, 110, beim("echt", "jeden"), fuell=BLAU),
]))

# M Klausurtipp (Lexi) --------------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · Tun oder Unterlassen kurz vorab"), ("tipp2", "Klausurtipp · Versuch: Merkmale im Tatentschluss"),
       ("tipp3", "Klausurtipp · vollendet: objektiver Tatbestand")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Tun oder Unterlassen: nur kurz vorab,", 200, 200, "tipp", "Bold", 36),
    z("außer der Fall ist wirklich zweifelhaft", 200, 250, beim("tipp", "außer"), size=34),
    z("Versuch: in den Tatentschluss gehören", 200, 335, "tipp2", "Bold", 36),
    z("Erfolg, Handlungsmöglichkeit,", 200, 385, beim("tipp2", "Erfolg"), size=34),
    z("Quasikausalität, Garantenstellung", 200, 435, beim("tipp2", "Quasikausalität"), size=34),
    z("vollendet: im objektiven Tatbestand,", 200, 520, "tipp3", "Bold", 36),
    z("den Vorsatz danach", 200, 570, beim("tipp3", "Vorsatz"), size=34),
    *redet("LX_warnt", LXX, BR, FR + 60, "tipp", "sch"),
    namensschild("Lexi", LXX, BR, "tipp", GELB, d=0.2),
])

# N Prüfschema -------------------------------------------------------------------------------------------------------------
K1, K2, K3 = 150, 230, 310
PS_ = "Prüfschema"
folie([("sch", PS_), ("s0", f"{PS_} › Vorab: Tun oder Unterlassen"), ("s1", f"{PS_} › I. Tatbestand"),
       ("s1a", f"{PS_} › I. 1. a) Erfolg"), ("s1b", f"{PS_} › I. 1. b) Nichtvornahme trotz Möglichkeit"),
       ("s1c", f"{PS_} › I. 1. c) Quasikausalität"), ("s1d", f"{PS_} › I. 1. d) Garantenstellung"),
       ("s1e", f"{PS_} › I. 1. e) Entsprechung"), ("s1f", f"{PS_} › I. 2. Vorsatz"), ("s2", f"{PS_} › II. Rechtswidrigkeit"),
       ("s3", f"{PS_} › III. Schuld"), ("s4", f"{PS_} › IV. Strafmilderung"), ("s5", f"{PS_} › Versuch")], [
    karte(60, 50, 1800, 920, "sch"),
    titel("Prüfschema: unechtes Unterlassungsdelikt, § 13 StGB", 110, 90, "sch", 50),
    z("Vorab: Tun oder Unterlassen? (Schwerpunkt der Vorwerfbarkeit)", K1, 175, "s0", "Bold", 33, rechts=1820),
    z("I. Tatbestand", K1, 235, "s1", "Bold", 35, rechts=1820),
    z("1. objektiv:", K2, 288, beim("s1", "objektiv"), "Bold", 32, rechts=1820),
    z("a) Erfolg", K3, 336, "s1a", size=32, rechts=1820),
    z("b) Nichtvornahme der gebotenen Handlung trotz physisch-realer Möglichkeit", K3, 384, "s1b", size=32, rechts=1820),
    z("c) Quasikausalität und objektive Zurechnung", K3, 432, "s1c", size=32, rechts=1820),
    z("d) Garantenstellung", K3, 480, "s1d", size=32, rechts=1820),
    z("e) Entsprechung, § 13 Abs. 1 Halbsatz 2", K3, 528, "s1e", size=32, rechts=1820),
    z("2. subjektiv: Vorsatz", K2, 580, "s1f", "Bold", 32, rechts=1820),
    z("II. Rechtswidrigkeit", K1, 640, "s2", "Bold", 35, rechts=1820),
    z("III. Schuld, mit Zumutbarkeit", K1, 700, "s3", "Bold", 35, rechts=1820),
    z("IV. Strafmilderung, § 13 Abs. 2 StGB", K1, 760, "s4", "Bold", 35, rechts=1820),
    fl_block(K1, 830, 1600, 90, HELL, "s5", [("Versuch: die objektiven Merkmale I. 1. a)–e) im Tatentschluss", "ExtraBold", 32, INK)]),
])

# O Merksatz (Lexi) ------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Für einen Erfolg haftet durch Unterlassen", 0)], [("nur, wer als ", 0), ("Garant", "a"), (" rechtlich", 0)],
                 [("dafür einstehen muss.", 0)]], 750, 290, 42, "merke", {"a": beim("merke", "Garant")}),
    *markertext([[("Die ", 0), ("mögliche Rettung", "b"), (" hätte den Erfolg", 0)],
                 [("mit an Sicherheit grenzender", "c")], [("Wahrscheinlichkeit", "c"), (" verhindern müssen.", 0)]],
                750, 490, 42, "m2", {"b": beim("m2", "mögliche"), "c": beim("m2", "Sicherheit")}),
    *markertext([[("Tritt der Erfolg nicht ein,", 0)], [("prüfst du den ", 0), ("Versuch", "d"), (".", 0)]], 750, 700, 42, "m3",
                {"d": beim("m3", "Versuch")}),
    *redet("LX_erklaert", 1680, 960, 690, "merke", lexi_bis_ende("merke")),
    namensschild("Lexi", 1680, 960, "merke", GELB, d=0.2),
])
