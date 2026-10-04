"""Figuren für Folge 144 (Verfügungsbewusstsein, versteckte Ware an der Kasse) aus der LexVerse-Figma-Bibliothek
(Open Peeps, CC0). Alle Figuren fiktiv.
Fabian (um 30, Kunde; Stimme niklas): standing/walking-2 (schwarzes T-Shirt, Hose Blau #8DB3F2, weiße Schuhe; gehend),
Kopf Short 4 (Haar schwarz, Original-Tusche; Kopf hat keine einfärbbare Haarfläche), Haut #E8B48F, kein Bart, keine Brille.
Carina (um 30, Kassiererin; Stimme ela_froh): standing/shirt-3 (Hemdbluse Orange #F9A66C, schwarze Hose), Kopf Long
(Haar schwarz, Original-Tusche), Haut #F4D0B5, keine Brille.
Sachlich, keine Karikatur, keine „listige“ oder böse Mimik bei Fabian (Verstecken nur mit Suspicious = prüfender Blick),
keine Prothesen-Posen (shirt-1/-2, blazer-2 bewusst nicht), keine Bärte, keine Polka Dots. Posen und Kleidung nicht aus
141–143 (blazer-4, crossed_arms-2, easing-1, robot_dance-2, blazer-3, easing-2, resting-2, shirt-4); Lexi bleibt robot_dance-1.
Präfix FA_/CA_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach
links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (FA_redet, CA_redet, Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_144")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "FA": ("standing/walking-2", "Short 4", None, None, {"Skin": "#E8B48F", "Pants": "#8DB3F2"}),
    "CA": ("standing/shirt-3", "Long", None, None, {"Skin": "#F4D0B5", "Top": "#F9A66C"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("FA_ruhig", "FA", "Calm", 0), ("FA_redet", "FA", "Smile", 1), ("FA_prueft", "FA", "Suspicious", 0),
    ("FA_ernst", "FA", "Serious", 0), ("FA_sorge", "FA", "Concerned|Serious", 0), ("FA_still", "FA", "Solemn", 0),
    ("FA_froh", "FA", "Smile", 0), ("FA_muede", "FA", "Tired", 0),
    ("CA_ruhig", "CA", "Calm", 0), ("CA_redet", "CA", "Smile", 1), ("CA_froh", "CA", "Smile", 0),
    ("CA_ernst", "CA", "Serious", 0), ("CA_denkt", "CA", "Suspicious", 0), ("CA_staunt", "CA", "Awe", 0),
    ("CA_sorge", "CA", "Concerned|Serious", 0),
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
