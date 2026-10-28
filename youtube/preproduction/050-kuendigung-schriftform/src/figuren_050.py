"""Figuren für Folge 050 (Kündigung per WhatsApp, Schriftform § 623 BGB) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv.
Frau Kuhlmann (um 60, Inhaberin einer Fahrradwerkstatt, Arbeitgeberin): standing/crossed_arms-1, Kopf Gray Bun, Glasses 2,
blaues Oberteil. Bastian (um 25, Mechaniker): standing/walking-2, Kopf Short 2, schwarzes T-Shirt (Pose-Reihe -2), dunkelblaue Arbeitshose.
Frau Petersen (um 45, Werkstattleiterin, nur im Ausblick § 174): standing/easing-1, Kopf Medium Straight, rote Jacke.
Keine Bärte, keine Prothesen-Posen. Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt
nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Smile, Suspicious, Fear, Contempt, Very Angry bzw.
„Augen|geschlossener Mund“ (Concerned|Serious, Smile Big|Smile). Sprechende Ansichten (KU_redet, KU_streng, BA_redet,
PE_redet, Lexi) zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_050")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "KU": ("standing/crossed_arms-1", "Gray Bun", None, "Glasses 2", {"Skin": "#F0C8A8", "Top": "#8DB3F2"}),
    "BA": ("standing/walking-2", "Short 2", None, None, {"Skin": "#E6B48F", "Pants": "#3D4A7A"}),
    "PE": ("standing/easing-1", "Medium Straight", None, None, {"Skin": "#C68E6A", "Jacket": "#F07A6A", "Top": "#FFFFFF"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("KU_ruhig", "KU", "Calm", 0), ("KU_redet", "KU", "Smile", 1), ("KU_streng", "KU", "Serious", 1),
    ("KU_froh", "KU", "Smile Big|Smile", 0), ("KU_denkt", "KU", "Suspicious", 0), ("KU_sorge", "KU", "Concerned|Serious", 0),
    ("KU_aerger", "KU", "Contempt", 0),
    ("BA_ruhig", "BA", "Calm", 0), ("BA_redet", "BA", "Serious", 1), ("BA_schreck", "BA", "Fear", 0),
    ("BA_denkt", "BA", "Suspicious", 0), ("BA_froh", "BA", "Smile", 0), ("BA_strahlt", "BA", "Smile Big|Smile", 0),
    ("BA_sorge", "BA", "Concerned|Serious", 0),
    ("PE_ruhig", "PE", "Calm", 0), ("PE_redet", "PE", "Smile", 1), ("PE_denkt", "PE", "Suspicious", 0),
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
