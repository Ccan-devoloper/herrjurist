"""Folge 068 · Tatbestandsirrtum § 16 StGB: Jäger, Pilzsammler & Fahrlässigkeit – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A Abenddämmerung am Waldrand (Hochsitz, Unterholz, Umriss, Rettungswagen), B Sachverhalt,
C Vorsatzdelikt §§ 223, 224 (objektiver Tatbestand, Vorsatz = Wissen und Wollen), D § 16 Abs. 1 Satz 1 (Wortlautkarte),
E Abgrenzung error in persona, F § 16 Abs. 1 Satz 2, § 15 und § 229 (Wortlautkarte), G § 229: Sorgfaltspflicht (BGHSt 66, 119
Rn. 14, UVV Jagd § 3 Abs. 4), H § 229: Vorhersehbarkeit, Zusammenhang, Rechtswidrigkeit, Schuld, Ergebnis, I Abwandlung § 222,
J Abgrenzung § 17, K Klausurtipp (Lexi), L Prüfschema, M Merksatz (Lexi).
Sehr zurückhaltend: keine Waffe im Bild, kein Schuss, kein Blut, keine Verletzung; nur Hochsitz, Mond, Busch, Wildschwein als
Gedankenbild, Rettungswagen-Symbol. Szene A im Dämmerungsverlauf (der Fall verlangt das Dämmerlicht), sonst Cremegrund.
Geräusche nur bei sichtbarer Handlung: Laub raschelt im Gebüsch (Freesound CC0)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont

bausteine.FIGORDNER = "op_068/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE, daemmer=None)        # Dämmerung = Verlauf, erzeugt im Renderer
PFAD_FARBE = dict(bausteine.PFAD_FARBE, daemmer=(21, 21, 21, 150))
HELL = (255, 251, 230, 255)
LILAHELL = (246, 243, 255, 255)
ROTHELL = (253, 232, 228, 255)
GRUENHELL = (232, 247, 233, 255)
HOLZ = (214, 160, 110, 255)
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
    """Wortlautkarte: wörtliches Zitat (gesetze-im-internet.de bzw. Volltext, Abruf 02.10.2026) in einer hellen Karte,
    Fundstelle darunter rechts. zeilen = Liste von Token-Listen [(text, Schlüssel|0)], hl = {Schlüssel: Cue}
    (Hervorhebung synchron zum gesprochenen Wort)."""
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


def daemmerfolie(pfade, els):
    """Fallszene im Dämmerungsverlauf (Grund im Szenenplan: der Irrtum entsteht im Dämmerlicht)."""
    pruefe_im_bild(els)
    FOLIEN.append(dict(bg="daemmer", pfade=pfade, els=els))


def geduckt(e, boden=880):
    """Ludwig bückt sich ins Gebüsch: Figur tiefer gesetzt, der Teil unter der Bodenlinie (hinter dem Gebüsch) entfällt."""
    e.sprite = e.sprite.crop((0, 0, e.sprite.width, int(boden - e.y)))
    return e


def busch(cx, unten, breite, cue, **k):
    """Gebüsch: Krone des Fluent-Emoji „deciduous-tree“ (MIT), nur der obere Teil ohne Stamm, nicht umgezeichnet."""
    e = ficon("fluent-emoji-flat", "deciduous-tree", cx, unten, breite, cue, **k)
    sp = e.sprite
    e.sprite = sp.crop((0, 0, sp.width, int(sp.height * 0.74)))
    e.y = unten - e.sprite.height
    return e


# --- Eigene Hilfsfunktion (wie Folge 062): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ------------------
# ElevenLabs legt das Ende eines Wortes vor Satzzeichen oft in die folgende Pause; redet() kürzt jedes Wortende auf
# das letzte 10-ms-Fenster über −38 dBFS (aus ../stimme.wav) und verteilt die Viseme nur auf diese Spanne.
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


BODEN = 880
BR, FR = 930, 480                       # Figuren rechts neben der Tafel
X1, X2 = 1420, 1720                     # Jutta (links), Ludwig (rechts)
MB = (X1 + X2) // 2
XS = 1600                               # eine Figur allein neben der Tafel


def paar(cue, ju, lu, ju_bis=None, lu_bis=None, ju_folge=(), lu_folge=()):
    """Jutta und Ludwig rechts neben der Tafel mit Namensschild (ab dem ersten Bild der Folie durchgehend).
    ju_folge/lu_folge: weitere Mimiken [(Name, Cue), …] im Zwiebelschalenprinzip."""
    els = []
    for basis, x, folge, bis_, d in (("JU_" + ju, X1, ju_folge, ju_bis, 0.0), ("LU_" + lu, X2, lu_folge, lu_bis, 0.2)):
        kette = [(basis, cue)] + [(("JU_" if x == X1 else "LU_") + n, c) for n, c in folge]
        for i, (n, c) in enumerate(kette):
            b = kette[i + 1][1] if i + 1 < len(kette) else bis_
            els.append(peep_voll(n, x, BR, FR, c, anim=("pop" if i == 0 else "cut"), d=(d if i == 0 else 0.0), bis=b))
    els += [namensschild("Jutta", X1, BR, cue, GRUEN, d=0.2), namensschild("Ludwig", X2, BR, cue, BLAU, d=0.3)]
    return els


# A Fall: Abenddämmerung am Waldrand ------------------------------------------------------------------------------------------
JX, JU_UNTEN, JH = 385, 610, 400        # Jutta in der offenen Kanzel des Hochsitzes (blickt nach rechts)
LX_, LH = 1480, 440                     # Ludwig im Unterholz (blickt nach rechts, sieht die Jägerin nicht)
JUa = ("JU_redet_r", JX, JU_UNTEN, JH)
JUb = ("JU_beteuert_r", JX, JU_UNTEN, JH)
LUa = ("LU_redet_r", LX_, BODEN, LH)
laub = [szene(ficon("fluent-emoji-flat", "leaf-fluttering-in-wind", LX_ - 165, 700, 60, beim("bueckt", "raschelt"), bis="umriss"),
              "068laub*", 1.0, versatz=0.0),
        ficon("fluent-emoji-flat", "fallen-leaf", LX_ + 175, 705, 50, beim("bueckt", "raschelt"), d=0.12, bis="umriss")]
gebuesch = [bewegt(busch(LX_ - 70, BODEN, 260, NULL), beim("bueckt", "raschelt"), (beim("bueckt", "raschelt")[0],
                   beim("bueckt", "raschelt")[1] + 0.35), 16),
            bewegt(busch(LX_ + 95, BODEN, 230, NULL), beim("bueckt", "raschelt"), (beim("bueckt", "raschelt")[0],
                   beim("bueckt", "raschelt")[1] + 0.35), -14)]
daemmerfolie([(NULL, "Fall · Abenddämmerung am Waldrand"), ("ludwig", "Fall · Im Unterholz"),
              ("bueckt", "Fall · Ein Umriss im Gebüsch"), ("treffer", "Fall · Ludwig wird verletzt"), ("frage", "Fall · Die Frage")], [
    linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK),
    pl("Ein Abend im Oktober, kurz nach Sonnenuntergang", 70, 40, NULL, fill=LILA, size=36),
    ficon("tabler", "moon-stars", 1790, 210, 110, NULL, fuell=GELB),
    # Wald im Hintergrund
    ficon("fluent-emoji-flat", "evergreen-tree", 1110, BODEN - 2, 190, NULL),
    ficon("fluent-emoji-flat", "deciduous-tree", 1700, BODEN - 2, 250, NULL),
    ficon("fluent-emoji-flat", "evergreen-tree", 1840 - 80, BODEN - 2, 150, NULL),
    # Hochsitz: zwei Pfosten, Strebe, Leiter (Tabler ladder), offene Kanzel; Jutta steht in der Kanzel
    linienzug([(275, BODEN), (300, JU_UNTEN - 10)], NULL, breite=12, farbe=INK),
    linienzug([(495, BODEN), (470, JU_UNTEN - 10)], NULL, breite=12, farbe=INK),
    linienzug([(285, 790), (485, 690)], NULL, breite=8, farbe=INK),
    ficon("tabler", "ladder", 600, BODEN, 120, NULL, fuell=HOLZ),
    ficon("tabler", "ladder", 600, BODEN - 112, 120, NULL, fuell=HOLZ),
    ficon("tabler", "ladder", 600, BODEN - 224, 120, NULL, fuell=HOLZ),
    peep_voll("JU_ruhig_r", JX, JU_UNTEN, JH, NULL, bis="umriss"),
    peep_voll("JU_spaeht_r", JX, JU_UNTEN, JH, "umriss", anim="cut", bis="j1"),
    *redet("JU_redet_r", JX, JU_UNTEN, JH, "j1", "schuss"),
    peep_voll("JU_ernst_r", JX, JU_UNTEN, JH, "schuss", anim="cut", bis="treffer"),
    peep_voll("JU_schreck_r", JX, JU_UNTEN, JH, "treffer", anim="cut", bis="j2"),
    *redet("JU_beteuert_r", JX, JU_UNTEN, JH, "j2", "frage"),
    peep_voll("JU_sorge_r", JX, JU_UNTEN, JH, "frage", anim="cut"),
    karte(240, JU_UNTEN - 185, 290, 195, NULL, fill=HOLZ, rund=10, schatten=0, rand=5),   # Brüstung vor Juttas Beinen (Kanzel)
    namensschild("Jutta", JX, JU_UNTEN, NULL, GRUEN),
    pl("erfahrene Jägerin, darf hier jagen", 900, 610, beim("jutta", "erfahrene"), fill=WEISS, size=30, anker="m", bis="ludwig"),
    pl("wartet auf Wildschweine", 900, 690, beim("jutta", "wartet"), fill=WEISS, size=30, anker="m", bis="ludwig"),
    # Ludwig im Unterholz (ab „Im Unterholz“), Pilze und Korb
    peep_voll("LU_froh_r", LX_, BODEN, LH, "ludwig", anim="fade", bis="l1"),
    *redet("LU_redet_r", LX_, BODEN, LH, "l1", "bueckt"),
    geduckt(peep_voll("LU_ruhig_r", LX_, BODEN + 70, LH, "bueckt", anim="cut", bis="treffer", unten_offen=True)),
    peep_voll("LU_schreck_r", LX_, BODEN, LH, "treffer", anim="cut", bis="rtw"),
    peep_voll("LU_sorge_r", LX_, BODEN, LH, "rtw", anim="cut"),
    *gebuesch,
    ficon("fluent-emoji-flat", "brown-mushroom", LX_ + 230, BODEN - 2, 46, beim("ludwig", "Pilzen")),
    ficon("fluent-emoji-flat", "basket", LX_ - 230, BODEN - 2, 80, beim("ludwig", "Pilzen")),
    namensschild("Ludwig", LX_, BODEN, "ludwig", BLAU),
    pl("Rentner, sucht Pilze", LX_, 330, beim("ludwig", "Rentner"), fill=WEISS, size=30, anker="m", bis="l1"),
    blase("sprech", 520, 190, "l1", 1150, 330, inhalt=["Noch ein paar Steinpilze,", "dann gehe ich heim."], textsize=32,
          figur=LUa, bis="bueckt"),
    *laub,
    pl("das Gebüsch raschelt", LX_, 400, beim("bueckt", "raschelt"), fill=WEISS, size=30, anker="m", bis="treffer"),
    # Was Jutta sieht und denkt
    pl("nur ein dunkler Umriss", 900, 690, beim("umriss", "dunklen"), fill=WEISS, size=30, anker="m", bis="j1"),
    blase("denk", 380, 240, beim("umriss", "Umriss"), 820, 255, inhalt=[" ", " "], figur=("JU_spaeht_r", JX, JU_UNTEN, JH),
          bis="schuss"),
    ficon("fluent-emoji-flat", "boar", 820, 310, 120, beim("umriss", "Umriss"), bis="schuss"),
    blase("sprech", 470, 180, "j1", 880, 560, inhalt=["Da im Gebüsch,", "ein Wildschwein."], textsize=34, figur=JUa, bis="schuss"),
    # Ohne genaues Hinsehen – Ludwig wird verletzt (kein Schuss, keine Verletzung im Bild)
    pl("ohne genauer hinzusehen", 900, 610, "schuss", fill=WEISS, size=30, anker="m", bis="rtw"),
    ficon("tabler", "eye-off", 900, 760, 80, "schuss", fuell=WEISS, bis="rtw"),
    pl("Ludwig wird am Bein getroffen", LX_, 330, beim("treffer", "Getroffen"), fill=ROTHELL, size=30, anker="m", bis="frage"),
    ficon("fluent-emoji-flat", "ambulance", 920, BODEN - 2, 210, beim("rtw", "Rettungswagen")),
    pl("ins Krankenhaus", 920, 600, beim("rtw", "Rettungswagen"), fill=WEISS, size=30, anker="m", bis="frage"),
    pl("Er überlebt.", 920, 680, beim("rtw", "überlebt"), fill=GRUEN, size=30, anker="m", bis="frage"),
    blase("sprech", 520, 190, "j2", 790, 250, inhalt=["Ich war mir sicher, das", "ist ein Wildschwein."], textsize=32,
          figur=JUb, bis="frage"),
    # Die Frage
    pl("Vorsätzlich verletzt?", 960, 520, "frage", fill=WEISS, size=34, anker="m"),
    pl("Und wenn nicht: Bleibt gar nichts?", 960, 610, "frage2", fill=PINK, size=34, anker="m"),
])

# B Sachverhalt ----------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    glyphen("An einem Abend im Oktober, kurz nach Sonnenuntergang, sitzt die erfahrene Jägerin Jutta auf ihrem Hochsitz am "
            "Waldrand. Sie darf hier jagen und wartet auf Wildschweine. Im Unterholz gegenüber sucht der Rentner Ludwig nach Pilzen."),
    glyphen("Als Ludwig sich bückt, raschelt das Gebüsch. Im Dämmerlicht sieht Jutta nur einen dunklen Umriss. Sie hält ihn für "
            "ein Wildschwein und schießt, ohne genauer hinzusehen. Ludwig wird am Bein getroffen und kommt ins Krankenhaus; er "
            "überlebt. Hätte Jutta genau hingesehen, hätte sie ihn erkannt."),
], "Wie hat sich Jutta strafbar gemacht?")

# C Vorsatzdelikt: §§ 223, 224 StGB ------------------------------------------------------------------------------------------
PA = "A. Gefährliche Körperverletzung"
folie([("p223", f"{PA}, §§ 223, 224 StGB"), ("obj", f"{PA} › objektiver Tatbestand (+)"),
       ("subj", f"{PA} › subjektiver Tatbestand: Vorsatz?"), ("ww", f"{PA} › Vorsatz: Wissen und Wollen")], rechts_frei([
    *tafel("p223", "Vorsatzdelikt: §§ 223, 224 StGB"),
    z("§ 223 Abs. 1 und § 224 Abs. 1 Nr. 2 StGB (Waffe)", 110, 180, beim("p223", "Paragraf"), size=30),
    z("objektiver Tatbestand:", 110, 245, "obj", "ExtraBold", 34),
    ok(135, 320, beim("obj", "Ludwig"), gr=18),
    z("andere Person: Ludwig", 175, 300, beim("obj", "Ludwig"), size=32),
    ok(135, 370, beim("obj", "Gesundheit"), gr=18),
    z("an der Gesundheit geschädigt", 175, 350, beim("obj", "Gesundheit"), size=32),
    ok(135, 420, beim("obj", "Gewehr"), gr=18),
    z("Gewehr: Waffe (Schusswaffe)", 175, 400, beim("obj", "Gewehr"), size=32),
    z("subjektiver Tatbestand: Vorsatz?", 110, 470, "subj", "ExtraBold", 34),
    fl_block(110, 530, 1040, 100, GELB, "ww", [("Vorsatz = Wissen und Wollen aller Tatumstände", "ExtraBold", 32, INK)]),
    fund("mehr dazu: Folge 029 Vorsatzformen", 150, 640, beim("ww", "Folge")),
    z("Jutta wollte: ein Wildschwein treffen", 110, 700, "wollte", "Bold", 32),
    z("wusste nicht: Dort stand ein Mensch.", 110, 750, beim("wollte", "Dass"), "Bold", 32),
    *paar("p223", "ernst", "ruhig", ju_folge=[("sorge", "subj")], lu_folge=[("ernst", "obj")]),
    pl("§ 223 StGB", MB, 160, beim("p223", "Paragraf"), fill=WEISS, size=30, anker="m", bis="obj"),
    pl("objektiv (+)", MB, 160, "obj", fill=GRUEN, size=30, anker="m", anim="cut", bis="subj"),
    ficon("tabler", "user-check", MB, 380, 100, "obj", fuell=GRUEN, bis="subj"),
    pl("Vorsatz?", MB, 160, "subj", fill=GELB, size=30, anker="m", anim="cut", bis="wollte"),
    ficon("tabler", "bulb", MB, 380, 100, "ww", fuell=GELB, bis="wollte"),
    pl("vorgestellt: Wildschwein", MB, 160, "wollte", fill=WEISS, size=28, anker="m", anim="cut"),
    ficon("fluent-emoji-flat", "boar", MB, 380, 110, "wollte", anim="cut"),
]))

# D § 16 Abs. 1 Satz 1 StGB --------------------------------------------------------------------------------------------------
W16 = [[("„Wer bei Begehung der Tat ", 0), ("einen Umstand nicht kennt", "a"), (", der zum", 0)],
       [("gesetzlichen Tatbestand gehört", "b"), (", handelt ", 0), ("nicht vorsätzlich", "c"), (". Die", 0)],
       [("Strafbarkeit wegen ", 0), ("fahrlässiger Begehung", "d"), (" bleibt unberührt.“", 0)]]


def w16(*keys):
    """§ 16 Abs. 1 als Wortlautkarte; hervorgehoben (fett + Marker) nur die in dieser Folie gesprochenen Merkmale."""
    return [[(t, k if k in keys else 0) for t, k in zeile_] for zeile_ in W16]
P16 = "A. Vorsatz"
folie([("p16", f"{P16} › Tatbestandsirrtum, § 16 Abs. 1 Satz 1 StGB"), ("umstand", f"{P16} › Tatumstand „andere Person“"),
       ("vorsneg", f"{P16} (−) · gefährliche Körperverletzung (−)"),
       ("versuch", "Versuchter Totschlag, §§ 212, 22 StGB › kein Tatentschluss")], rechts_frei([
    *tafel("p16", "Tatbestandsirrtum: § 16 Abs. 1 StGB", size=46),
    *wortlaut(110, 180, 1040, 150, "p16", w16("a", "b", "c"), 30,
              {"a": beim("p16", "Umstand"), "b": beim("p16", "gesetzlichen"), "c": beim("p16", "nicht", 2)}, "§ 16 Abs. 1 StGB"),
    z("Tatumstand bei § 223: „andere Person“", 110, 395, "umstand", "Bold", 32),
    z("bei § 212 (Totschlag): „Mensch“", 110, 440, beim("umstand", "Totschlag"), "Bold", 32),
    fund("BGH, Urt. v. 1.3.2018 – 4 StR 399/17, Rn. 14", 150, 487, beim("umstand", "Totschlag")),
    nein(135, 565, "kennt", gr=18),
    z("Jutta kennt ihn nicht: Umriss = Tier", 175, 545, "kennt", size=32),
    fl_block(110, 610, 1040, 100, ROTHELL, "vorsneg", [("Vorsatz (−) · gefährliche Körperverletzung (−)", "ExtraBold", 32, INK)]),
    nein(135, 775, "versuch", gr=18),
    z("versuchter Totschlag: kein Tatentschluss,", 175, 755, "versuch", size=32),
    z("sie wollte keinen Menschen töten", 175, 800, beim("versuch", "Menschen"), size=32),
    *paar("p16", "sorge", "ruhig", ju_folge=[("ernst", "versuch")], lu_folge=[("ernst", "kennt")]),
    pl("§ 16 StGB", MB, 160, beim("p16", "Paragraf"), fill=GELB, size=30, anker="m", bis="umstand"),
    pl("Mensch?", MB, 160, "umstand", fill=WEISS, size=30, anker="m", anim="cut", bis="kennt"),
    ficon("tabler", "user-question", MB, 380, 100, "umstand", fuell=WEISS, bis="kennt"),
    pl("Tier vorgestellt", MB, 160, "kennt", fill=WEISS, size=30, anker="m", anim="cut", bis="vorsneg"),
    ficon("fluent-emoji-flat", "boar", MB, 380, 110, "kennt", anim="cut", bis="vorsneg"),
    pl("Vorsatz (−)", MB, 160, "vorsneg", fill=ROTHELL, size=30, anker="m", anim="cut"),
    ficon("tabler", "bulb-off", MB, 380, 100, "vorsneg", fuell=WEISS, anim="cut"),
]))

# E Abgrenzung: error in persona --------------------------------------------------------------------------------------------
folie([("eip", "Abgrenzung › error in persona"), ("tier", "Abgrenzung › Mensch statt Tier: nicht gleichwertig")], rechts_frei([
    *tafel("eip", "Abgrenzung: error in persona"),
    karte(110, 185, 505, 330, "eip", fill=GRUENHELL, rund=18, schatten=6, rand=4),
    z("error in persona:", 135, 205, "eip", "ExtraBold", 32, rechts=600),
    z("Mensch statt Mensch", 135, 255, beim("eip", "verwechselt"), "Bold", 30, rechts=600),
    z("gleichwertig", 135, 315, "gleich", "Bold", 30, rechts=600),
    ok(150, 385, beim("gleich", "bleibt"), gr=16),
    z("Vorsatz bleibt", 185, 365, beim("gleich", "bleibt"), size=30, rechts=600),
    fund("BGH, Beschl. v. 14.7.2025 –", 135, 425, beim("gleich", "bleibt"), rechts=600),
    fund("4 StR 281/25, Rn. 7, 8", 135, 460, beim("gleich", "bleibt"), rechts=600),
    karte(645, 185, 505, 330, "tier", fill=ROTHELL, rund=18, schatten=6, rand=4),
    z("hier:", 670, 205, "tier", "ExtraBold", 32, rechts=1135),
    z("Mensch statt Tier", 670, 255, "tier", "Bold", 30, rechts=1135),
    z("nicht gleichwertig", 670, 315, beim("tier", "nicht"), "Bold", 30, rechts=1135),
    nein(685, 385, beim("tier", "nicht"), gr=16),
    z("§ 16 greift", 720, 365, beim("tier", "deshalb"), size=30, rechts=1135),
    *paar("eip", "ruhig", "ruhig", ju_folge=[("ernst", "tier")]),
    ficon("tabler", "users", MB, 380, 110, "eip", fuell=BLAU, bis="tier"),
    pl("Mensch / Mensch", MB, 160, beim("eip", "verwechselt"), fill=GRUENHELL, size=28, anker="m", bis="tier"),
    ficon("fluent-emoji-flat", "boar", MB - 70, 380, 100, "tier", anim="cut"),
    ficon("tabler", "user", MB + 70, 380, 90, "tier", fuell=WEISS, anim="cut"),
    pl("Mensch / Tier", MB, 160, "tier", fill=ROTHELL, size=28, anker="m", anim="cut"),
]))

# F § 16 Abs. 1 Satz 2, § 15, § 229 ------------------------------------------------------------------------------------------
W229 = [[("„Wer ", 0), ("durch Fahrlässigkeit", "a"), (" die Körperverletzung", 0)],
        [("einer anderen Person", "b"), (" verursacht, wird mit Freiheitsstrafe", 0)],
        [("bis zu drei Jahren oder mit Geldstrafe bestraft.“", 0)]]
folie([("satz2", "§ 16 Abs. 1 Satz 2 StGB › Fahrlässigkeit bleibt unberührt"), ("p15", "§ 15 StGB › nur, wenn ausdrücklich strafbar"),
       ("p229", "B. Fahrlässige Körperverletzung, § 229 StGB")], rechts_frei([
    *tafel("satz2", "Was bleibt? § 16 Abs. 1 Satz 2 StGB", size=46),
    *wortlaut(110, 180, 1040, 150, "satz2", w16("d"), 30, {"d": beim("satz2", "fahrlässiger")}, "§ 16 Abs. 1 StGB"),
    z("§ 15: fahrlässiges Handeln nur strafbar,", 110, 390, "p15", "Bold", 32),
    z("wenn das Gesetz es ausdrücklich mit Strafe bedroht", 110, 435, beim("p15", "ausdrücklich"), "Bold", 32),
    *wortlaut(110, 510, 1040, 150, "p229", W229, 30,
              {"a": beim("p229", "Fahrlässigkeit"), "b": beim("p229", "anderen")}, "§ 229 StGB"),
    ok(135, 755, beim("p229", "Fahrlässigkeit"), gr=18),
    z("bei der Körperverletzung: ja", 175, 735, beim("p229", "Fahrlässigkeit"), "Bold", 32),
    *paar("satz2", "ruhig", "ruhig", ju_folge=[("ernst", "p229")], lu_folge=[("ernst", "p229")]),
    pl("nur der Vorsatz fällt", MB, 160, "satz2", fill=WEISS, size=28, anker="m", bis="p15"),
    ficon("tabler", "scale", MB, 380, 110, "satz2", fuell=GELB, bis="p229"),
    pl("§ 15 StGB", MB, 160, "p15", fill=WEISS, size=30, anker="m", anim="cut", bis="p229"),
    pl("§ 229 StGB", MB, 160, "p229", fill=GELB, size=30, anker="m", anim="cut"),
    ficon("tabler", "alert-triangle", MB, 380, 100, "p229", fuell=GELB, anim="cut"),
]))

# G § 229: objektive Sorgfaltspflichtverletzung ------------------------------------------------------------------------------
PB = "B. § 229"
folie([("erfolg", f"{PB} › Erfolg, Handlung, Kausalität"), ("pflicht", f"{PB} › objektive Sorgfaltspflichtverletzung"),
       ("uvv", f"{PB} › Sorgfaltspflicht: UVV Jagd"), ("verstoss", f"{PB} › objektive Sorgfaltspflichtverletzung (+)")], rechts_frei([
    *tafel("erfolg", "§ 229: Sorgfaltspflicht", size=48),
    ok(135, 200, beim("erfolg", "Ludwig"), gr=18),
    z("Erfolg, Handlung, Kausalität", 175, 180, beim("erfolg", "Ludwig"), "Bold", 32),
    z("objektive Sorgfaltspflichtverletzung:", 110, 245, "pflicht", "ExtraBold", 34),
    z("Maßstab: besonnener und gewissenhafter Mensch", 110, 300, "mass", size=31),
    z("in der konkreten Lage und sozialen Rolle", 110, 343, beim("mass", "konkreten"), size=31),
    fund("BGH, Beschl. v. 5.5.2021 – 4 StR 19/20, Rn. 14", 150, 388, beim("mass", "konkreten")),
    z("hier: eine sorgfältige Jägerin", 110, 430, beim("mass", "hier"), "Bold", 31),
    *wortlaut(110, 490, 1040, 110, "uvv", [
        [("„Ein Schuss darf erst abgegeben werden, wenn sich der Schütze", 0)],
        [("vergewissert hat", "a"), (", dass ", 0), ("niemand gefährdet wird", "b"), (".“", 0)],
    ], 30, {"a": beim("uvv", "vergewissert"), "b": beim("uvv", "niemand")}, "UVV Jagd (VSG 4.4), § 3 Abs. 4"),
    z("Jägersprache: das Ziel sicher „ansprechen“", 110, 650, "ansp", size=31),
    nein(135, 725, "verstoss", gr=18),
    z("Schuss in der Dämmerung auf einen Umriss,", 175, 705, "verstoss", size=31),
    z("nicht sicher erkannt", 175, 748, beim("verstoss", "nicht"), size=31),
    fl_block(110, 795, 1040, 80, ROTHELL, beim("verstoss", "pflichtwidrig"), [("pflichtwidrig", "ExtraBold", 34, INK)]),
    *paar("erfolg", "ernst", "sorge", ju_folge=[("sorge", "verstoss")]),
    pl("verletzt, kausal", MB, 160, "erfolg", fill=WEISS, size=28, anker="m", bis="pflicht"),
    ficon("tabler", "scale", MB, 380, 110, "pflicht", fuell=GELB, bis="ansp"),
    pl("Sorgfalt?", MB, 160, "pflicht", fill=GELB, size=30, anker="m", anim="cut", bis="ansp"),
    ficon("tabler", "binoculars", MB, 380, 110, "ansp", fuell=WEISS, anim="cut", bis="verstoss"),
    pl("Ziel ansprechen", MB, 160, "ansp", fill=WEISS, size=28, anker="m", anim="cut", bis="verstoss"),
    ficon("tabler", "eye-off", MB, 380, 100, "verstoss", fuell=WEISS, anim="cut"),
    pl("nicht hingesehen", MB, 160, "verstoss", fill=ROTHELL, size=28, anker="m", anim="cut"),
]))

# H § 229: Vorhersehbarkeit, Zusammenhang, Rechtswidrigkeit, Schuld, Ergebnis ------------------------------------------------
folie([("vorh", f"{PB} › objektive Vorhersehbarkeit (+)"), ("zus", f"{PB} › Pflichtwidrigkeitszusammenhang (+)"),
       ("rw", f"{PB} › Rechtswidrigkeit (+)"), ("schuld", f"{PB} › Schuld (+)"),
       ("erg", "Ergebnis · Jutta strafbar nach § 229 StGB")], rechts_frei([
    *tafel("vorh", "§ 229: Vorhersehbarkeit und Schuld", size=46),
    ok(135, 200, "vorh", gr=18),
    z("objektiv vorhersehbar:", 175, 180, "vorh", "ExtraBold", 32),
    z("abends Menschen am Waldrand,", 175, 225, beim("vorh", "Dass"), size=31),
    z("Schuss auf ein nicht erkanntes Ziel", 175, 268, beim("vorh", "Schuss"), size=31),
    fund("BGH 4 StR 19/20, Rn. 11, 18", 175, 313, beim("vorh", "Schuss")),
    ok(135, 380, "zus", gr=18),
    z("genau hingesehen: Ludwig erkannt, kein Schuss", 175, 360, "zus", size=31),
    ok(135, 445, "rw", gr=18),
    z("Rechtswidrigkeit: keine Rechtfertigungsgründe", 175, 425, "rw", size=31),
    ok(135, 510, "schuld", gr=18),
    z("Schuld: persönlich erkennbar und vermeidbar", 175, 490, "schuld", size=31),
    z("erfahrene Jägerin", 175, 535, beim("schuld", "erfahrene"), size=31),
    fl_block(110, 620, 1040, 110, GRUEN, "erg", [("Jutta: strafbar nach § 229 StGB", "ExtraBold", 36, INK)]),
    *paar("vorh", "ernst", "ruhig", ju_folge=[("sorge", "erg")], lu_folge=[("ernst", "zus")]),
    pl("vorhersehbar", MB, 160, "vorh", fill=WEISS, size=30, anker="m", bis="zus"),
    ficon("tabler", "eye-check", MB, 380, 100, "zus", fuell=WEISS, bis="schuld"),
    pl("bei Hinsehen: kein Schuss", MB, 160, "zus", fill=WEISS, size=28, anker="m", anim="cut", bis="rw"),
    pl("rechtswidrig", MB, 160, "rw", fill=WEISS, size=28, anker="m", anim="cut", bis="schuld"),
    pl("vermeidbar", MB, 160, "schuld", fill=WEISS, size=30, anker="m", anim="cut", bis="erg"),
    ficon("tabler", "user-check", MB, 380, 100, "schuld", fuell=GELB, anim="cut", bis="erg"),
    pl("§ 229 (+)", MB, 160, "erg", fill=GRUEN, size=30, anker="m", anim="cut"),
    ficon("tabler", "circle-check", MB, 380, 100, "erg", fuell=GRUEN, anim="cut"),
]))

# I Abwandlung: Ludwig stirbt --------------------------------------------------------------------------------------------------
folie([("ab", "Abwandlung · Ludwig stirbt: § 222 StGB")], rechts_frei([
    *tafel("ab", "Abwandlung: Ludwig stirbt", fill=ROTHELL),
    nein(135, 245, beim("ab", "Kein"), gr=20),
    z("kein Totschlag (§ 16 Abs. 1 Satz 1)", 175, 220, beim("ab", "Kein"), "Bold", 36),
    ok(135, 325, beim("ab", "fahrlässige"), gr=20),
    z("aber fahrlässige Tötung, § 222 StGB", 175, 300, beim("ab", "fahrlässige"), "Bold", 36),
    peep_voll("JU_sorge", XS, BR, FR, "ab"),
    namensschild("Jutta", XS, BR, "ab", GRUEN, d=0.2),
    pl("gilt dasselbe", XS, 160, beim("ab", "gilt"), fill=WEISS, size=30, anker="m"),
]))

# J Abgrenzung: Verbotsirrtum § 17 ---------------------------------------------------------------------------------------------
folie([("p17", "Abgrenzung › Verbotsirrtum, § 17 StGB")], rechts_frei([
    *tafel("p17", "Abgrenzung: Verbotsirrtum", fill=LILAHELL),
    z("Verbotsirrtum, § 17 StGB:", 110, 200, beim("p17", "Verbotsirrtum"), "ExtraBold", 36),
    z("Täter kennt alle Tatumstände,", 110, 270, beim("p17", "Dort"), "Bold", 36),
    z("hält sein Tun aber für erlaubt", 110, 330, beim("p17", "hält"), "Bold", 36),
    pl("eigene Folge", 110, 430, beim("p17", "eigene"), fill=LILA, size=32),
    *paar("p17", "ruhig", "ruhig"),
    ficon("tabler", "book", MB, 380, 100, beim("p17", "eigene"), fuell=LILA),
    pl("§ 17 StGB", MB, 160, beim("p17", "Paragraf"), fill=LILA, size=30, anker="m"),
]))

# K Klausurtipp (Lexi) --------------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · Vorsatzdelikt zuerst"), ("tipp2", "Klausurtipp · neuer Obersatz: Fahrlässigkeit"),
       ("tipp3", "Klausurtipp · Strafantrag, § 230 StGB")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("zuerst das Vorsatzdelikt:", 200, 200, beim("tipp", "Vorsatzdelikt"), "Bold", 36),
    z("scheitert im subjektiven Tatbestand", 200, 250, beim("tipp", "subjektiven"), size=34),
    z("an § 16", 200, 300, beim("tipp", "Paragraf"), size=34),
    z("dann neuer Obersatz:", 200, 385, "tipp2", "Bold", 36),
    z("Fahrlässigkeitsdelikt", 200, 435, beim("tipp2", "Fahrlässigkeitsdelikt"), size=34),
    z("§ 229: Strafantrag, § 230 Abs. 1 StGB", 200, 520, beim("tipp3", "Strafantrag"), "Bold", 36),
    z("außer: besonderes öffentliches Interesse", 200, 570, beim("tipp3", "besondere"), size=34),
    *redet("LX_warnt", LXX, BR, FR + 60, "tipp", "sch"),
    namensschild("Lexi", LXX, BR, "tipp", GELB, d=0.2),
])

# L Prüfschema -------------------------------------------------------------------------------------------------------------
K1, K2, K3 = 150, 230, 310
PS_ = "Prüfschema"
folie([("sch", PS_), ("s1", f"{PS_} › A. Gefährliche Körperverletzung"), ("s1a", f"{PS_} › A. objektiver Tatbestand"),
       ("s1b", f"{PS_} › A. Vorsatz (−), § 16 Abs. 1 Satz 1"), ("s2", f"{PS_} › B. Fahrlässige Körperverletzung"),
       ("s2a", f"{PS_} › B. I. Tatbestand"), ("s2b", f"{PS_} › B. I. Sorgfaltspflichtverletzung"),
       ("s2c", f"{PS_} › B. I. Vorhersehbarkeit"), ("s2d", f"{PS_} › B. I. Zusammenhang"),
       ("s2e", f"{PS_} › B. II. Rechtswidrigkeit"), ("s2f", f"{PS_} › B. III. Schuld"), ("s2g", f"{PS_} › B. IV. Strafantrag")], [
    karte(60, 50, 1800, 920, "sch"),
    titel("Prüfschema: Tatbestandsirrtum und Fahrlässigkeit", 110, 90, "sch", 52),
    z("A. Gefährliche Körperverletzung, §§ 223, 224 Abs. 1 Nr. 2 StGB", K1, 180, "s1", "Bold", 36, rechts=1820),
    z("1. objektiver Tatbestand (+)", K2, 240, "s1a", size=33, rechts=1820),
    z("2. subjektiver Tatbestand: Vorsatz (−), § 16 Abs. 1 Satz 1 StGB", K2, 293, "s1b", size=33, rechts=1820),
    z("B. Fahrlässige Körperverletzung, § 229 StGB", K1, 370, "s2", "Bold", 36, rechts=1820),
    z("I. Tatbestand: Erfolg, Handlung, Kausalität", K2, 430, "s2a", size=33, rechts=1820),
    z("objektive Sorgfaltspflichtverletzung", K3, 483, "s2b", size=33, rechts=1820),
    z("objektive Vorhersehbarkeit", K3, 536, "s2c", size=33, rechts=1820),
    z("Zusammenhang zwischen Pflichtverletzung und Erfolg", K3, 589, "s2d", size=33, rechts=1820),
    z("II. Rechtswidrigkeit", K2, 652, "s2e", size=33, rechts=1820),
    z("III. Schuld: persönlich erkennbar und vermeidbar", K2, 715, "s2f", size=33, rechts=1820),
    z("IV. Strafantrag, § 230 Abs. 1 StGB", K2, 778, "s2g", size=33, rechts=1820),
])

# M Merksatz (Lexi) ------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Wer einen ", 0), ("Tatumstand nicht kennt", "a"), (",", 0)], [("handelt ", 0), ("nicht vorsätzlich", "b"),
                 (".", 0)]], 750, 290, 44, "merke", {"a": beim("merke", "Tatumstand"), "b": beim("merke", "nicht", 2)}),
    *markertext([[("§ 16 nimmt aber ", 0), ("nur den Vorsatz", "c"), (".", 0)]], 750, 470, 44, "m2", {"c": beim("m2", "nur")}),
    *markertext([[("War der Irrtum bei gehöriger Sorgfalt", 0)], [("vermeidbar", "d"), (", bleibt die Strafbarkeit", 0)],
                 [("wegen ", 0), ("Fahrlässigkeit", "e"), (", soweit das Gesetz", 0)], [("sie vorsieht.", 0)]],
                750, 580, 44, "m3", {"d": beim("m3", "vermeidbar"), "e": beim("m3", "Fahrlässigkeit")}),
    *redet("LX_erklaert", 1680, 960, 690, "merke", lexi_bis_ende("merke")),
    namensschild("Lexi", 1680, 960, "merke", GELB, d=0.2),
])
