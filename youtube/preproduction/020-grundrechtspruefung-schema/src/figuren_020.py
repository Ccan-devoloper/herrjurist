"""Figuren für Folge 020 (Grundrechtsprüfung Schema, Skateverbot) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv.
Gudrun (um 60, Skaterin, Grundrechtsträgerin): standing/easing-2 (offene Jacke, Turnschuhe), Kopf Gray Medium (graues Haar).
Frau Krüger (um 75, Passantin): standing/crossed_arms-2 (verschränkte Arme), Kopf Gray Bun, Glasses 2.
Herr Brückner (um 45, Ordnungsamt): standing/blazer-3 (blaues Jackett), Kopf Short 4.
Keine Bärte, keine Prothesen-Posen. Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt
nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Smile, Suspicious, Fear, Tired, Very Angry bzw.
„Augen|geschlossener Mund“ (Rage|Serious, Concerned|Serious). Sprechende Ansichten (GU_redet, KR_redet, BR_redet, Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 % der Gesichtshöhe."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_020")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}
GRAU_HAAR = "#C9C9CF"

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "GU": ("standing/easing-2", "Gray Medium", None, None,
           {"Skin": "#F1C6A5", "Hair": GRAU_HAAR, "Jacket": "#F9A66C", "Top": "#FFFFFF", "Pants": "#8DB3F2"}),
    "KR": ("standing/crossed_arms-2", "Gray Bun", None, "Glasses 2",
           {"Skin": "#EBC4A0", "Hair": GRAU_HAAR, "Pants": "#B8A9F5"}),
    "BR": ("standing/blazer-3", "Short 4", None, None,
           {"Skin": "#D9A07A", "Jacket": "#8DB3F2", "Top": "#FFFFFF", "Pants": "#3D3D58"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("GU_ruhig", "GU", "Calm", 0), ("GU_froh", "GU", "Smile", 0), ("GU_redet", "GU", "Rage|Serious", 1),
    ("GU_denkt", "GU", "Suspicious", 0), ("GU_schreck", "GU", "Fear", 0), ("GU_sorge", "GU", "Concerned|Serious", 0),
    ("GU_muede", "GU", "Tired", 0), ("GU_ernst", "GU", "Serious", 0),
    ("KR_ruhig", "KR", "Calm", 0), ("KR_schreck", "KR", "Fear", 0), ("KR_redet", "KR", "Very Angry", 1),
    ("KR_froh", "KR", "Smile", 0),
    ("BR_ruhig", "BR", "Calm", 0), ("BR_redet", "BR", "Serious", 1), ("BR_froh", "BR", "Smile", 0),
]

if __name__ == "__main__":
    os.makedirs(ZIEL, exist_ok=True)
    n = 0
    for name, p, mimik, mund in LISTE:
        pose, kopf, bart, brille, farben = P[p]
        for suffix, gespiegelt in (("", 1), ("_r", 0)):
            figur(pose, kopf, mimik, bart, brille, farben, hoehe=1200, spiegeln=bool(gespiegelt)).save(f"{ZIEL}/{name}{suffix}.png"); n += 1
            if mund:
                for k, m in MUND.items():
                    figur(pose, kopf, f"{mimik.split('|')[0]}|{m}", bart, brille, farben, hoehe=1200,
                          spiegeln=bool(gespiegelt)).save(f"{ZIEL}/{name}{suffix}_{k}.png"); n += 1
    # Lexi (feste Moderatorin, Stimme Carla), blickt nach links zur Tafel
    for name, (pose, mimik) in {"LX_erklaert": ("standing/robot_dance-1", "Smile"), "LX_warnt": ("standing/robot_dance-1", "Serious")}.items():
        a = LX.AUSSEHEN
        for k, g in {"": mimik, **{"_" + k: f"{mimik}|{m}" for k, m in MUND.items()}}.items():
            figur(pose, a["kopf"], g, a["bart"], a["brille"], a["farben"], hoehe=1200, spiegeln=True).save(f"{ZIEL}/{name}{k}.png"); n += 1
    print(n, "Figurenbilder ->", ZIEL)
