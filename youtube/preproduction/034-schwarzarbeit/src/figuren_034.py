"""Figuren für Folge 034 (Schwarzarbeit, gepflasterte Einfahrt) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
- Frau Ziegler (ZI, um 65, Bestellerin, Hausbesitzerin): standing/blazer-4 (Jackett Lila, Oberteil Weiß, schwarze Hose),
  Kopf Gray Bun, Brille Glasses 2. Stimme lisa (Frau, älter).
- Herr Fuchs (FU, um 45, selbständiger Pflasterer): standing/crossed_arms-1 (Oberteil Blau, schwarze Hose), Kopf hat-beanie
  (Mütze), kein Bart. Stimme stephan (Mann, mittel).
Je Person eine Pose (Outfit konstant), keine Prothesen-Posen, keine Bärte. Alle Posen blicken im Original nach rechts; die
Grundansicht ist gespiegelt und blickt nach links, Suffix _r nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Smile, Serious, Suspicious, Fear, Driven, Tired bzw.
„Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten (ZI_redet, ZI_fordert, FU_redet, FU_fordert, Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_034")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

ZI_F = {"Skin": "#F0C8A8", "Jacket": "#B8A9F5", "Top": "#FFFFFF"}
FU_F = {"Skin": "#D9A47A", "Top": "#8DB3F2"}
# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "ZI": ("standing/blazer-4", "Gray Bun", None, "Glasses 2", ZI_F),
    "FU": ("standing/crossed_arms-1", "hat-beanie", None, None, FU_F),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("ZI_ruhig", "ZI", "Calm", 0), ("ZI_froh", "ZI", "Smile", 0), ("ZI_redet", "ZI", "Smile", 1),
    ("ZI_fordert", "ZI", "Driven", 1), ("ZI_schreck", "ZI", "Fear", 0), ("ZI_sorge", "ZI", "Concerned|Serious", 0),
    ("ZI_ernst", "ZI", "Serious", 0), ("ZI_denkt", "ZI", "Suspicious", 0), ("ZI_muede", "ZI", "Tired", 0),
    ("FU_ruhig", "FU", "Calm", 0), ("FU_froh", "FU", "Smile", 0), ("FU_redet", "FU", "Smile", 1),
    ("FU_fordert", "FU", "Driven", 1), ("FU_ernst", "FU", "Serious", 0), ("FU_denkt", "FU", "Suspicious", 0),
    ("FU_ertappt", "FU", "Concerned|Serious", 0), ("FU_muede", "FU", "Tired", 0),
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
