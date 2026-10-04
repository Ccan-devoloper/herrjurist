"""Figuren für Folge 191 (Erfolgsqualifikation, Freiheitsberaubung mit Todesfolge; Wohnung im 2. Stock) aus der
LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv, Erwachsene, kein Milieu-Klischee.
Bertram (BE, um 60, schließt seinen Mitbewohner ein; Stimme william): standing/easing-2 (offenes Hemd/Jacke Orange #F9A66C
  über schwarzem T-Shirt, Hose Grau #6B6B6B, weiße Schuhe), Kopf Gray Short (Haar Grau #A9A9A9), Brille Glasses 3,
  Haut #E9C3A0, kein Bart. Sachlich, keine Dämonisierung: keine bösen Mimiken (kein Contempt, Angry, Rage).
Hubertus (HU, um 45, Mitbewohner; Stimme marc): standing/walking-1 (T-Shirt Lila #B8A9F5, schwarze Hose, weiße Schuhe;
  nicht robot_dance-*, damit er nicht wie Lexi wirkt),
  Kopf Short 2 (Haar #2B2B2B), Haut #D9A27A, keine Brille, kein Bart.
Posen der letzten drei Folgen (188: pointing_finger-2, crossed_arms-1; 189: blazer-4, crossed_arms-2; 190: resting-1,
resting-2, walking-2) nicht verwendet; robot_dance-1 bleibt Lexi; keine Polka Dots, keine Prothesen-Posen, keine Bärte.
Präfixe BE_/HU_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach
links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Suspicious, Fear, Solemn bzw. „Augen|geschlossener
Mund“ (Concerned|Serious). Sprechende Ansichten BE_redet, HU_redet (und Lexi) zusätzlich mit a/o/e: Augen der Grundmimik +
Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_191")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "BE": ("standing/easing-2", "Gray Short", None, "Glasses 3", {"Skin": "#E9C3A0", "Jacket": "#F9A66C", "Pants": "#6B6B6B",
                                                                  "Hair": "#A9A9A9"}),
    "HU": ("standing/walking-1", "Short 2", None, None, {"Skin": "#D9A27A", "Top": "#B8A9F5", "Hair": "#2B2B2B"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("BE_ruhig", "BE", "Calm", 0), ("BE_redet", "BE", "Serious", 1), ("BE_ernst", "BE", "Serious", 0),
    ("BE_denkt", "BE", "Suspicious", 0), ("BE_schreck", "BE", "Fear", 0), ("BE_still", "BE", "Solemn", 0),
    ("BE_sorge", "BE", "Concerned|Serious", 0),
    ("HU_ruhig", "HU", "Calm", 0), ("HU_redet", "HU", "Concerned|Serious", 1), ("HU_sorge", "HU", "Concerned|Serious", 0),
    ("HU_ernst", "HU", "Serious", 0), ("HU_denkt", "HU", "Suspicious", 0), ("HU_angst", "HU", "Fear", 0),
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
