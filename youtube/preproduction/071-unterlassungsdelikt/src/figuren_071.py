"""Figuren für Folge 071 (Unechtes Unterlassen, Garten mit Teich) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Lutz (um 35, Vater, sorgeberechtigt): im Liegestuhl sitting/one_leg_up-1, stehend standing/walking-2 – beide schwarzes
T-Shirt (Pose ohne einfärbbares Oberteil) und Jeans Blau #8DB3F2, weiße Sneaker; Kopf Short 1, Haut #F0C8A8, ohne Bart.
Sachlich, keine Dämonisierung: keine bösen Mimiken (kein Contempt, kein Angry), nur Calm/Serious/Solemn/Concerned|Serious.
Gesa (um 30, Nachbarin): standing/walking-1 (rotes T-Shirt #F07A6A, schwarze Hose) im ganzen Video (gleiches Outfit), Kopf
Long, Haut #E2B088. Keine Prothesen-Posen. Alle Posen blicken im Original nach rechts (Kontaktbild geprüft); Grundansicht
blickt nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts. Grundmimik immer mit geschlossenem Mund
(FOLGE-ABLAUF.md). Sprechende Ansichten zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear /
Hectic (Schnitt bei 60 % der Gesichtshöhe). Das Kind erscheint nicht als Figur (nur abstraktes Icon)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_071")
ORIGINAL_LINKS = set()
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}
LU_F = {"Skin": "#F0C8A8", "Pants": "#8DB3F2"}
GE_F = {"Skin": "#E2B088", "Top": "#F07A6A"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "LS": ("sitting/one_leg_up-1", "Short 1", None, None, LU_F),     # Lutz im Liegestuhl
    "LU": ("standing/walking-2", "Short 1", None, None, LU_F),       # Lutz stehend (Tafelszenen)
    "GE": ("standing/walking-1", "Long", None, None, GE_F),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("LS_ruhig", "LS", "Calm", 0), ("LS_redet", "LS", "Smile", 1), ("LS_ernst", "LS", "Serious", 0),
    ("LS_still", "LS", "Solemn", 0), ("LS_sorge", "LS", "Concerned|Serious", 0),
    ("LU_ruhig", "LU", "Calm", 0), ("LU_ernst", "LU", "Serious", 0), ("LU_still", "LU", "Solemn", 0),
    ("LU_sorge", "LU", "Concerned|Serious", 0),
    ("GE_ruhig", "GE", "Calm", 0), ("GE_schreck", "GE", "Fear", 0), ("GE_redet", "GE", "Smile", 1),
    ("GE_ernst", "GE", "Serious", 0), ("GE_froh", "GE", "Smile", 0),
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
