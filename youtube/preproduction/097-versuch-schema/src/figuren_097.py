"""Figuren für Folge 097 (Versuch Schema, §§ 22, 23 StGB) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv.
Herbert (Anfang 60, Täter): standing/pointing_finger-2 (schwarzer Pullover der Pose, Hose Graublau, weiße Turnschuhe),
    Kopf „No Hair 3“ (Halbglatze, grauer Haarkranz), Brille „Glasses 3“. Zeigt mit erhobenem Arm (Streit; beim Zielen sitzt
    die stilisierte Pistole an dieser Hand). Keine Karikatur, keine Prothese, kein Bart.
Gregor (um 45, Nachbar): standing/walking-1 (grünes T-Shirt, schwarze Hose), Kopf „Short 4“, Haut mittel.
Posen nicht aus den Folgen 094–096 (robot_dance-2, polka_dots, blazer-3, easing-1/-2, shirt-3, resting-1, blazer-4,
crossed_arms-1); keine Polka Dots. Präfix HE_/GR_ (nie ER_, weil bausteine.peep_voll ER_* nach op_we umleitet).
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links, Suffix _r nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Driven, Very Angry, Fear, Tired, Suspicious, Awe,
Smile bzw. „Augen|geschlossener Mund“ (Rage|Serious, Concerned|Serious, Concerned Fear|Serious). Sprechende Ansichten
(HE_redet, HE_bestuerzt, GR_redet, Lexi) zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear /
Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_097")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

HE_F = {"Skin": "#EDC3A0", "Pants": "#6E7F9E", "Hair": "#C9C9CF"}
GR_F = {"Skin": "#C98F66", "Top": "#8FD694", "Hair": "#4A3326"}
# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "HE": ("standing/pointing_finger-2", "No Hair 3", None, "Glasses 3", HE_F),
    "GR": ("standing/walking-1", "Short 4", None, None, GR_F),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("HE_ruhig", "HE", "Calm", 0), ("HE_wuetend", "HE", "Very Angry", 0), ("HE_redet", "HE", "Rage|Serious", 1),
    ("HE_entschlossen", "HE", "Driven", 0), ("HE_bestuerzt", "HE", "Concerned|Serious", 1), ("HE_muede", "HE", "Tired", 0),
    ("HE_ernst", "HE", "Serious", 0), ("HE_denkt", "HE", "Suspicious", 0),
    ("GR_ruhig", "GR", "Calm", 0), ("GR_genervt", "GR", "Suspicious", 0), ("GR_redet", "GR", "Concerned Fear|Serious", 1),
    ("GR_angst", "GR", "Fear", 0), ("GR_erleichtert", "GR", "Awe", 0), ("GR_froh", "GR", "Smile", 0),
    ("GR_ernst", "GR", "Serious", 0),
]

if __name__ == "__main__":
    os.makedirs(ZIEL, exist_ok=True)
    nur = sys.argv[1:]
    n = 0
    for name, p, mimik, mund in LISTE:
        if nur and name not in nur:
            continue
        pose, kopf, bart, brille, farben = P[p]
        for suffix, gespiegelt in (("", 1), ("_r", 0)):
            figur(pose, kopf, mimik, bart, brille, farben, hoehe=1200, spiegeln=bool(gespiegelt)).save(f"{ZIEL}/{name}{suffix}.png"); n += 1
            if mund:
                for k, m in MUND.items():
                    figur(pose, kopf, f"{mimik.split('|')[0]}|{m}", bart, brille, farben, hoehe=1200,
                          spiegeln=bool(gespiegelt)).save(f"{ZIEL}/{name}{suffix}_{k}.png"); n += 1
    if not nur:
        # Lexi (feste Moderatorin, Stimme Carla), blickt nach links zur Tafel
        for name, (pose, mimik) in {"LX_erklaert": ("standing/robot_dance-1", "Smile"), "LX_warnt": ("standing/robot_dance-1", "Serious")}.items():
            a = LX.AUSSEHEN
            for k, g in {"": mimik, **{"_" + k: f"{mimik}|{m}" for k, m in MUND.items()}}.items():
                figur(pose, a["kopf"], g, a["bart"], a["brille"], a["farben"], hoehe=1200, spiegeln=True).save(f"{ZIEL}/{name}{k}.png"); n += 1
    print(n, "Figurenbilder ->", ZIEL)
