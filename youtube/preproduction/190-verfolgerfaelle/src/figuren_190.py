"""Figuren für Folge 190 (Verfolgerfall: Kontrolleur stürzt bei der Verfolgung) aus der LexVerse-Figma-Bibliothek
(Open Peeps, CC0). Alle Figuren fiktiv.
Wendelin (WD, um 55, Fahrkartenkontrolleur; Stimme helmut): standing/resting-1 (Oberteil Dunkelblau #3B5B92 wie eine
  Dienstkleidung ohne Logo, schwarze Hose, weiße Schuhe), Kopf No Hair 1, Brille Glasses 4, Haut #E6B897, kein Bart.
  Nach dem Sturz (Präfix WS_) dieselbe Figur mit Armschlinge: weißes Dreieckstuch unter dem angewinkelten Unterarm und Gurt
  zum Hals, als Grundform mit Tuschekontur über die fertige Figur gelegt (die Open-Peeps-Teile selbst bleiben unverändert;
  keine Pose der Bibliothek trägt eine Armschlinge, resting-1 hält den Unterarm angewinkelt vor dem Körper).
Anselm (AS, um 22, Fahrgast ohne gültigen Fahrschein; Stimme niklas): standing/resting-2 (schwarzes Oberteil, Hose Grün
  #8FD694, schwarze Schuhe), beim Weglaufen standing/walking-2 (derselbe Farbaufbau der Reihe -2: schwarzes Oberteil, Hose
  Grün #8FD694), Kopf Short 4, Haut #F2C9A8, keine Brille, kein Bart. Freundliches Aussehen, keine „Täter“-Klischees.
Posen der letzten drei Folgen (187: easing-1, pointing_finger-1; 188: pointing_finger-2, crossed_arms-1; 189: blazer-4,
crossed_arms-2) nicht verwendet; robot_dance-1 bleibt Lexi; keine Polka Dots, keine Prothesen-Posen, keine Bärte.
Präfixe WD_/WS_/AS_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach
links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Suspicious, Fear, Tired, Smile, Solemn bzw.
„Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten WD_redet, WS_redet, AS_redet (und Lexi) zusätzlich mit
a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
from PIL import Image, ImageDraw, ImageOps
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_190")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}
INK = (21, 21, 21, 255)

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "WD": ("standing/resting-1", "No Hair 1", None, "Glasses 4", {"Skin": "#E6B897", "Top": "#3B5B92"}),
    "WS": ("standing/resting-1", "No Hair 1", None, "Glasses 4", {"Skin": "#E6B897", "Top": "#3B5B92"}),
    "AS": ("standing/resting-2", "Short 4", None, None, {"Skin": "#F2C9A8", "Pants": "#8FD694"}),
    "AL": ("standing/walking-2", "Short 4", None, None, {"Skin": "#F2C9A8", "Pants": "#8FD694"}),
}


def schlinge(im):
    """Armschlinge über der nach links blickenden (gespiegelten) resting-1-Figur. Koordinaten in Einheiten der Figurenhöhe
    594 (gemessen am Kontaktbild); rechts 14 Einheiten Rand, damit das Tuch nicht abgeschnitten wird."""
    s = im.height / 594
    out = Image.new("RGBA", (im.width + int(14 * s), im.height)); out.paste(im, (0, 0))
    lay = Image.new("RGBA", out.size); d = ImageDraw.Draw(lay)
    P_ = lambda pts: [(x * s, y * s) for x, y in pts]

    def band(a, b, br):
        d.line(P_([a, b]), fill=INK, width=int((br + 5) * s)); d.line(P_([a, b]), fill=(255, 255, 255, 255), width=int(br * s))
    band((172, 112), (186, 268), 13)
    band((214, 110), (262, 226), 13)
    poly = P_([(272, 218), (176, 266), (186, 302), (270, 262)])
    d.polygon(poly, fill=(255, 255, 255, 255)); d.line(poly + [poly[0]], fill=INK, width=max(3, int(4 * s)), joint="curve")
    out.alpha_composite(lay)
    return out


# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("WD_ruhig", "WD", "Calm", 0), ("WD_ernst", "WD", "Serious", 0), ("WD_redet", "WD", "Serious", 1),
    ("WD_schreck", "WD", "Fear", 0), ("WD_denkt", "WD", "Suspicious", 0),
    ("WS_ruhig", "WS", "Calm", 0), ("WS_ernst", "WS", "Serious", 0), ("WS_redet", "WS", "Calm", 1),
    ("WS_denkt", "WS", "Suspicious", 0), ("WS_muede", "WS", "Tired", 0), ("WS_froh", "WS", "Smile", 0),
    ("WS_sorge", "WS", "Concerned|Serious", 0), ("WS_still", "WS", "Solemn", 0),
    ("AS_ruhig", "AS", "Calm", 0), ("AS_ernst", "AS", "Serious", 0), ("AS_redet", "AS", "Concerned|Serious", 1),
    ("AS_denkt", "AS", "Suspicious", 0), ("AS_sorge", "AS", "Concerned|Serious", 0), ("AS_schreck", "AS", "Fear", 0),
    ("AS_muede", "AS", "Tired", 0), ("AS_still", "AS", "Solemn", 0), ("AS_froh", "AS", "Smile", 0),
    ("AL_lauf", "AL", "Serious", 0),
]

if __name__ == "__main__":
    os.makedirs(ZIEL, exist_ok=True)
    n = 0
    for name, p, mimik, mund in LISTE:
        pose, kopf, bart, brille, farben = P[p]
        varianten = {"": mimik, **({"_" + k: f"{mimik.split('|')[0]}|{m}" for k, m in MUND.items()} if mund else {})}
        for k, g in varianten.items():
            im = figur(pose, kopf, g, bart, brille, farben, hoehe=1200, spiegeln=True)      # blickt nach links
            if p == "WS":
                im = schlinge(im)
            im.save(f"{ZIEL}/{name}{k}.png"); n += 1
            ImageOps.mirror(im).save(f"{ZIEL}/{name}_r{k}.png"); n += 1                   # blickt nach rechts
    # Lexi (feste Moderatorin, Stimme Carla), blickt nach links zur Tafel
    for name, (pose, mimik) in {"LX_erklaert": ("standing/robot_dance-1", "Smile"), "LX_warnt": ("standing/robot_dance-1", "Serious")}.items():
        a = LX.AUSSEHEN
        for k, g in {"": mimik, **{"_" + k: f"{mimik}|{m}" for k, m in MUND.items()}}.items():
            figur(pose, a["kopf"], g, a["bart"], a["brille"], a["farben"], hoehe=1200, spiegeln=True).save(f"{ZIEL}/{name}{k}.png"); n += 1
    print(n, "Figurenbilder ->", ZIEL)
