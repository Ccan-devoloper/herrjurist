"""Figuren für Folge 207 (Gesamtsaldierung: der Vermögensschaden beim Betrug) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv, gewöhnlich gekleidet (keine Markenlogos, keine Klischees, keine Karikatur).
Gundula (GU, um 60, Käuferin; Stimme hilde): standing/blazer-3 (Blazer Lila #B8A9F5, Hose Dunkelgrau #5A5A6A), Kopf Gray Medium
  (Haar Grau #B5B5B5), Brille Glasses 3, Haut #F0C8A8.
Alwin (AL, um 45, Verkäufer beim Garagenverkauf; Stimme stephan): standing/walking-1 (T-Shirt Grün #8FD694, schwarze Hose der
  Pose), Kopf Short 3, Haut #EDC3A0, kein Bart. Keine „fiese“ Mimik, keine Prothesen-Pose für die Täterrolle, keine
  Herkunfts- oder Hautfarbenzuschreibung.
Ulla (UL, um 30, Gutachterin; Stimme lucy): standing/shirt-4 (dunkles Hemd der Pose, Hose Türkis #7FD6D0), Kopf Long, Haut #B9805A.
Posen der letzten drei Folgen (204: shirt-3, crossed_arms-2, easing-2; 205: shirt-3, resting-2, easing-1; 206: pointing_finger-1,
robot_dance-2, resting-1) nicht verwendet; Lexi-Pose (robot_dance-1) nicht für Fallfiguren; keine Polka Dots, keine Bärte.
Präfixe GU_/AL_/UL_ (nie ER_). Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (blickt nach links),
Suffix _r blickt nach rechts. Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Suspicious, Smile
bzw. „Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten GU_redet, AL_redet, UL_redet (und Lexi) zusätzlich
mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_207")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "GU": ("standing/blazer-3", "Gray Medium", None, "Glasses 3", {"Skin": "#F0C8A8", "Jacket": "#B8A9F5", "Pants": "#5A5A6A", "Hair": "#B5B5B5"}),
    "AL": ("standing/walking-1", "Short 3", None, None, {"Skin": "#EDC3A0", "Top": "#8FD694"}),
    "UL": ("standing/shirt-4", "Long", None, None, {"Skin": "#B9805A", "Pants": "#7FD6D0"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("GU_ruhig", "GU", "Calm", 0), ("GU_froh", "GU", "Smile", 0), ("GU_denkt", "GU", "Suspicious", 0),
    ("GU_ernst", "GU", "Serious", 0), ("GU_sorge", "GU", "Concerned|Serious", 0), ("GU_redet", "GU", "Calm", 1),
    ("AL_ruhig", "AL", "Calm", 0), ("AL_froh", "AL", "Smile", 0), ("AL_denkt", "AL", "Suspicious", 0),
    ("AL_ernst", "AL", "Serious", 0), ("AL_sorge", "AL", "Concerned|Serious", 0), ("AL_redet", "AL", "Smile", 1),
    ("UL_ruhig", "UL", "Calm", 0), ("UL_denkt", "UL", "Suspicious", 0), ("UL_ernst", "UL", "Serious", 0),
    ("UL_redet", "UL", "Calm", 1),
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
