"""Figuren für Folge 197 (Zweistufentheorie: Foyer der Stadthalle, Tafeln) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv.
Frau Lammers (LA, um 60, Vorsitzende des Chors Liederkranz; Stimme hilde): standing/easing-1 (offene Jacke Lila #B8A9F5,
  Shirt Weiß, schwarze Hose), Kopf Gray Bun (grauer Dutt, Haar #C8C8C8), Haut #F1C9A5, Brille Glasses 2.
Herr Scheffler (SC, um 45, Geschäftsführer der Stadthallen-GmbH; Stimme christian): standing/blazer-1 (Blazer Grün #8FD694,
  Hose Dunkelgrau #4A4A4A, dunkle Socken der Originalpose), Kopf Short 3, Haut #D9A07A, keine Brille, kein Bart.
Posen der letzten Folgen (193: shirt-3, shirt-4; 194: blazer-3, robot_dance-3; 195: blazer-3, crossed_arms-1, pointing_finger-2;
196: blazer-4, crossed_arms-2, robot_dance-2; 192: shirt-3, blazer-2) nicht verwendet; keine Polka Dots, keine Bärte, keine
Karikatur. Präfixe LA_/SC_ (nie ER_).
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Smile, Serious, Suspicious, Calm, Solemn, Driven bzw.
„Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten LA_redet, LA_froh_redet, SC_redet, SC_freundlich_redet
(und Lexi) zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_197")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "LA": ("standing/easing-1", "Gray Bun", None, "Glasses 2", {"Skin": "#F1C9A5", "Jacket": "#B8A9F5", "Top": "#FFFFFF", "Hair": "#C8C8C8"}),
    "SC": ("standing/blazer-1", "Short 3", None, None, {"Skin": "#D9A07A", "Jacket": "#8FD694", "Pants": "#4A4A4A"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("LA_ruhig", "LA", "Smile", 0), ("LA_hofft", "LA", "Calm", 0), ("LA_sorge", "LA", "Concerned|Serious", 0),
    ("LA_entschlossen", "LA", "Driven", 0), ("LA_denkt", "LA", "Suspicious", 0), ("LA_liest", "LA", "Serious", 0),
    ("LA_redet", "LA", "Calm", 1), ("LA_froh_redet", "LA", "Smile", 1),
    ("SC_ruhig", "SC", "Calm", 0), ("SC_verlegen", "SC", "Solemn", 0), ("SC_denkt", "SC", "Suspicious", 0),
    ("SC_froh", "SC", "Smile", 0), ("SC_ernst", "SC", "Serious", 0),
    ("SC_redet", "SC", "Solemn", 1), ("SC_freundlich_redet", "SC", "Smile", 1),
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
