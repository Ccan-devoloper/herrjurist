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
FIGORDNER = "op_ab/"
FIG = SP + "peeps/"
BG_FARBE = {"creme": (255, 248, 236, 255)}
PFAD_FARBE = {"creme": (21, 21, 21, 140)}
RAND = 24


def folie(pfade, els):
    FOLIEN.append(dict(bg="creme", pfade=pfade, els=els))


def peep_voll(name, cx, unten, hoehe, cue, unten_offen=False, **k):
    """Nie links/rechts/oben angeschnitten; unten nur mit unten_offen=True."""
    ordner = "op_we/" if name.startswith("ER_") else FIGORDNER
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



# --- Neue Regeln: alles vollständig im Bild, Sachverhalt-Karte ------------------------------------------
def pruefe_im_bild(els, rand=12):
    for e in els:
        if getattr(e, "unten_offen", False):
            continue
        bb = e.sprite.getbbox()
        if not bb:
            continue
        x0, y0, x1, y1 = e.x + bb[0], e.y + bb[1], e.x + bb[2], e.y + bb[3]
        if hasattr(e, "weg"):
            dx, dy = e.weg[2], e.weg[3]
            x0, x1 = min(x0, x0 + dx), max(x1, x1 + dx)
        assert x0 >= rand and y0 >= rand and x1 <= engine.W - rand and y1 <= engine.H - rand, \
            f"Element ragt aus dem Bild: {e.name} ({x0},{y0})-({x1},{y1})"


def folie(pfade, els):
    pruefe_im_bild(els)
    FOLIEN.append(dict(bg="creme", pfade=pfade, els=els))


def absatz(text, x, y, breite, cue, size=38, stil="Regular", zeilenabstand=1.35, farbe=INK, d=0.0):
    """Fließtext mit Zeilenumbruch; gibt (Elemente, y_ende) zurück."""
    f = F(stil, size)
    worte, zeilen, cur = text.split(), [], ""
    for w in worte:
        t = (cur + " " + w).strip()
        if f.getlength(t) <= breite:
            cur = t
        else:
            zeilen.append(cur); cur = w
    if cur:
        zeilen.append(cur)
    els = []
    for i, z in enumerate(zeilen):
        els.append(OT(z, x, y + i * size * zeilenabstand, cue, stil, size, farbe=farbe, d=d, anim="fade"))
    return els, y + len(zeilen) * size * zeilenabstand


def sachverhalt(cue, absaetze, frage, pfad="Sachverhalt"):
    """Karte mit dem vollständigen Sachverhalt zum Nachlesen (erscheint komplett auf einmal)."""
    els = [karte(140, 60, 1640, 900, cue, fill=(255, 251, 230, 255)), titel("Sachverhalt", 210, 110, cue, 64)]
    y = 225
    for a in absaetze:
        e, y = absatz(a, 210, y, 1480, cue, size=38)
        els += e; y += 22
    els.append(pille(frage, 210, min(y + 10, 860), cue, fill=PINK, size=38))
    folie([(cue, pfad)], els)
