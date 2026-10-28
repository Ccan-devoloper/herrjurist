"""Figuren für Folge 068 (Tatbestandsirrtum, Jägerin und Pilzsammler) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Jutta (um 40, Jägerin): standing/blazer-4 (grüne Jacke #8FD694, weißes Oberteil, schwarze Hose), Kopf Medium Bangs 2 (braunes
Haar, Zopf), Haut #EDC1A0; sachlich-respektvoll, keine Jäger-Klischees (kein Hut mit Gamsbart, keine Waffe).
Ludwig (um 70, Rentner, Pilzsammler): standing/walking-3 (schwarzes Shirt, schwarze Hose, Sneaker; Pose ohne einfärbbares
Oberteil), Kopf Short 4_2 (graues Haar #BFBFBF; Gray Short verworfen: Haar dort hautfarben verdeckt), Haut #E2B088, ohne Bart.
Keine Prothesen-Posen. Beide Posen blicken im Original nach rechts (im Kontaktbild geprüft); die Grundansicht blickt nach links
(Figur rechts neben der Tafel), Suffix _r blickt nach rechts. Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md):
Calm, Smile, Serious, Suspicious, Fear, Tired bzw. „Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic (Schnitt bei 60 % der Gesichtshöhe)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_068")
ORIGINAL_LINKS = set()
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "JU": ("standing/blazer-4", "Medium Bangs 2", None, None,
           {"Skin": "#EDC1A0", "Jacket": "#8FD694", "Top": "#FFFFFF", "Hair": "#6B4A2B"}),
    "LU": ("standing/walking-3", "Short 4_2", None, None, {"Skin": "#E2B088", "Hair": "#BFBFBF", "Fill": "#BFBFBF"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("JU_ruhig", "JU", "Calm", 0), ("JU_redet", "JU", "Serious", 1), ("JU_spaeht", "JU", "Suspicious", 0),
    ("JU_schreck", "JU", "Fear", 0), ("JU_sorge", "JU", "Concerned|Serious", 0), ("JU_ernst", "JU", "Serious", 0),
    ("JU_beteuert", "JU", "Concerned|Serious", 1), ("JU_muede", "JU", "Tired", 0),
    ("LU_ruhig", "LU", "Calm", 0), ("LU_redet", "LU", "Smile", 1), ("LU_froh", "LU", "Smile", 0),
    ("LU_schreck", "LU", "Fear", 0), ("LU_sorge", "LU", "Concerned|Serious", 0), ("LU_ernst", "LU", "Serious", 0),
    ("LU_muede", "LU", "Tired", 0),
]

if __name__ == "__main__":
    os.makedirs(ZIEL, exist_ok=True)
    n = 0
    for name, p, mimik, mund in LISTE:
        pose, kopf, bart, brille, farben = P[p]
        orig_links = pose in ORIGINAL_LINKS
        for suffix, gespiegelt in (("", not orig_links), ("_r", orig_links)):
            figur(pose, kopf, mimik, bart, brille, farben, hoehe=1200, spiegeln=gespiegelt).save(f"{ZIEL}/{name}{suffix}.png"); n += 1
            if mund:
                for k, m in MUND.items():
                    figur(pose, kopf, f"{mimik.split('|')[0]}|{m}", bart, brille, farben, hoehe=1200,
                          spiegeln=gespiegelt).save(f"{ZIEL}/{name}{suffix}_{k}.png"); n += 1
    # Lexi (feste Moderatorin, Stimme Carla), blickt nach links zur Tafel
    for name, (pose, mimik) in {"LX_erklaert": ("standing/robot_dance-1", "Smile"), "LX_warnt": ("standing/robot_dance-1", "Serious")}.items():
        a = LX.AUSSEHEN
        for k, g in {"": mimik, **{"_" + k: f"{mimik}|{m}" for k, m in MUND.items()}}.items():
            figur(pose, a["kopf"], g, a["bart"], a["brille"], a["farben"], hoehe=1200, spiegeln=True).save(f"{ZIEL}/{name}{k}.png"); n += 1
    print(n, "Figurenbilder ->", ZIEL)
