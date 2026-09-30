"""LexVerse-Figuren aus der Open-Peeps-Figma-Bibliothek (CC0): Pose + Kopf + Gesicht (+ Bart, Brille), exakt nach
den Figma-Vorlagen „a person/standing|sitting|bust“ zusammengesetzt und über die Flächennamen eingefärbt.

    bild = figur("standing/blazer-1", "Medium Straight", "Smile", farben={"Skin": "#B07552", "Jacket": "#7FD6D0"})
    offen = figur("standing/blazer-1", "Medium Straight", "Smile|Explaining", ...)   # Augen von Smile, Mund von Explaining
"""
import io, json, os, re, xml.etree.ElementTree as ET
import cairosvg
from PIL import Image, ImageOps
from svgpathtools import parse_path
from rahmen import R

HIER = os.path.dirname(os.path.abspath(__file__))
BIB = os.environ.get("LEXPEEPS_BIB", os.path.join(HIER, "teile") if os.path.isdir(os.path.join(HIER, "teile")) else HIER)
NS = "{http://www.w3.org/2000/svg}"
S = 4096 / (42055 - 3224)                                   # Maßstab Figma-Einheiten -> Export
IDX = {i["figma_name"]: i for i in json.load(open(os.path.join(BIB, "index.json")))}
OFF = {"face": (159, 186), "facial-hair": (123, 338), "accessories": (47, 241)}   # relativ zum Kopfrahmen (react-peeps)
MUNDSCHNITT = 0.6                                           # Anteil der Gesichtshöhe, ab dem der Mund beginnt
VORLAGE = {"standing": ("a person/standing", "pose/standing/crossed_arms-1", "head/Bun 2"),
           "sitting": ("a person/sitting", None, "head/Bun 2"),
           "bust": ("a person/bust", None, "head/Bun 2")}


def _datei(name):
    return os.path.join(BIB, IDX[name]["datei"].split("/", 1)[1] if IDX[name]["datei"].startswith("teile/") else IDX[name]["datei"])


def _pfade(name):
    return [p for p in ET.parse(_datei(name)).getroot().iter(NS + "path")]


def _ink_box(pfade):
    for p in pfade:
        if "Ink" in (p.get("id") or ""):
            x0, x1, y0, y1 = parse_path(p.get("d")).bbox(); return x0, y0
    raise ValueError("kein Ink-Pfad")


def _klasse(pid):
    n = re.sub(r"[^A-Za-z\- ]", "", pid or "").strip()
    return re.sub(r"\s*\d+$", "", n).strip()


_T = {}
def _vorlage(art):
    """Verschiebung (Export-Einheiten), die Körper- bzw. Kopfsymbol der Vorlage an ihre Vorlagenposition bringt."""
    if art in _T: return _T[art]
    vname, _, kopf = VORLAGE[art]
    root = ET.parse(_datei(vname)).getroot()
    gruppen = {g.get("id"): list(g.iter(NS + "path")) for g in root.iter(NS + "g")}
    body_g = [k for k in gruppen if k and k.startswith("BODY")][0]
    head_g = [k for k in gruppen if k and k.startswith("HEAD")][0]
    # Körpersymbol der Vorlage über die Ink-Größe bestimmen
    def groesse(pf):
        for p in pf:
            if "Ink" in (p.get("id") or ""):
                x0, x1, y0, y1 = parse_path(p.get("d")).bbox(); return x1 - x0, y1 - y0
    zb = groesse(gruppen[body_g])
    kand = [n for n in IDX if (n.startswith("pose/" + art) if art != "bust" else n.startswith("body/"))]
    body = min(kand, key=lambda n: sum(abs(a - b) for a, b in zip(groesse(_pfade(n)), zb)))
    tb = [a - b for a, b in zip(_ink_box(gruppen[body_g]), _ink_box(_pfade(body)))]
    th = [a - b for a, b in zip(_ink_box(gruppen[head_g]), _ink_box(_pfade(kopf)))]
    _T[art] = (body, tb, kopf, th)
    return _T[art]


def _verschoben(name, dx, dy, farben):
    out = []
    for p in _pfade(name):
        f = farben.get(_klasse(p.get("id")), p.get("fill"))
        out.append(f'<path d="{p.get("d")}" fill="{f}" transform="translate({dx:.4f} {dy:.4f})"/>')
    return out


def figur_svg(pose, kopf, gesicht, bart=None, brille=None, farben=None):
    art = pose.split("/")[0] if not pose.startswith("body/") else "bust"
    posename = pose if pose.startswith("body/") else "pose/" + pose
    body0, tb, kopf0, th = _vorlage(art)
    farben = farben or {}
    rb, rp = R[body0], R[posename]
    teile = _verschoben(posename, (rb[0] - rp[0]) * S + tb[0], (rb[1] - rp[1]) * S + tb[1], farben)
    kn = "head/" + kopf
    rk0, rk = R[kopf0], R[kn]
    hx, hy = (rk0[0] - rk[0]) * S + th[0], (rk0[1] - rk[1]) * S + th[1]      # Verschiebung des Kopfes
    teile += _verschoben(kn, hx, hy, farben)
    augen, mund = gesicht.split("|") if "|" in gesicht else (gesicht, None)
    for kat, name in (("face", augen), ("facial-hair", bart), ("accessories", brille)):
        if not name: continue
        n = f"{kat}/{name}"; rt = R[n]; o = OFF[kat]
        dx, dy = (rk[0] - rt[0] + o[0]) * S + hx, (rk[1] - rt[1] + o[1]) * S + hy
        if kat == "face" and mund:
            # Mundzustand: Augen/Nase aus 'augen', Mundpartie aus 'mund' (gleicher Gesichtsrahmen, Schnitt quer)
            y0 = min(parse_path(p.get("d")).bbox()[2] for p in _pfade(n)) + dy
            y1 = max(parse_path(p.get("d")).bbox()[3] for p in _pfade(n)) + dy
            cut = y0 + MUNDSCHNITT * (y1 - y0)
            nm = "face/" + mund; rm = R[nm]
            dxm, dym = (rk[0] - rm[0] + o[0]) * S + hx, (rk[1] - rm[1] + o[1]) * S + hy
            teile.append(f'<clipPath id="oben"><rect x="-99999" y="-99999" width="199999" height="{cut + 99999:.3f}"/></clipPath>'
                         f'<clipPath id="unten"><rect x="-99999" y="{cut:.3f}" width="199999" height="199999"/></clipPath>')
            teile.append('<g clip-path="url(#oben)">' + "".join(_verschoben(n, dx, dy, farben)) + "</g>")
            teile.append('<g clip-path="url(#unten)">' + "".join(_verschoben(nm, dxm, dym, farben)) + "</g>")
            continue
        teile += _verschoben(n, dx, dy, farben)
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4096 1504" width="4096" height="1504">' + "".join(teile) + "</svg>"


def figur(pose, kopf, gesicht, bart=None, brille=None, farben=None, hoehe=1400, spiegeln=False):
    svg = figur_svg(pose, kopf, gesicht, bart, brille, farben)
    grob = Image.open(io.BytesIO(cairosvg.svg2png(bytestring=svg.encode(), scale=1))).convert("RGBA")
    x0, y0, x1, y1 = grob.getbbox()
    k = hoehe / (y1 - y0 + 2)
    svg2 = svg.replace('viewBox="0 0 4096 1504" width="4096" height="1504"',
                       f'viewBox="{x0 - 1} {y0 - 1} {x1 - x0 + 2} {y1 - y0 + 2}" width="{int((x1 - x0 + 2) * k)}" height="{hoehe}"')
    im = Image.open(io.BytesIO(cairosvg.svg2png(bytestring=svg2.encode()))).convert("RGBA")
    im = im.crop(im.getbbox())
    return ImageOps.mirror(im) if spiegeln else im
