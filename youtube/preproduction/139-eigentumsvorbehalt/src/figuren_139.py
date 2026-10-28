"""Figuren für Folge 139 (Eigentumsvorbehalt, Sofa auf Raten) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv.
Sonja (SO, um 30, Käuferin, Vorbehaltskäuferin): standing/robot_dance-3 (rotes Oberteil #F07A6A, schwarze Hose, weiße
  Turnschuhe; die geöffnete Hand passt zu „Endlich ein eigenes Sofa!“), Kopf Long Bangs (schwarzes Haar), Haut #F2C9A5.
Herr Schuster (SC, um 60, Verkäufer im Möbelhaus): standing/pointing_finger-2 (schwarzes Oberteil, Hose Graublau #5B6B8C,
  schwarze Stiefel; der erhobene Zeigefinger zeigt auf die Vorbehaltsklausel), Kopf Gray Short, Brille Glasses, Haut
  #EDC3A3, kein Bart.
Posen der letzten drei Folgen (135: blazer-4, crossed_arms-2; 136: blazer-3, robot_dance-2, pointing_finger-1; 137:
easing-2, shirt-3, resting-2) nicht verwendet; keine Polka Dots, keine Prothesen-Posen (blazer-1/-2, shirt-1/-2), keine
Bärte, keine Karikatur. Präfix SO_/SC_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist
gespiegelt und blickt nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Smile, Suspicious, Awe bzw. „Augen|geschlossener
Mund“ (Smile Big|Smile, Concerned|Serious). Sprechende Ansichten (SO_redet, SO_empoert, SC_redet, SC_streng, Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_139")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "SO": ("standing/robot_dance-3", "Long Bangs", None, None, {"Skin": "#F2C9A5", "Top": "#F07A6A", "Pants": "#151515"}),
    "SC": ("standing/pointing_finger-2", "Gray Short", None, "Glasses", {"Skin": "#EDC3A3", "Pants": "#5B6B8C"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("SO_ruhig", "SO", "Calm", 0), ("SO_redet", "SO", "Smile Big|Smile", 1), ("SO_empoert", "SO", "Concerned|Serious", 1),
    ("SO_froh", "SO", "Smile Big|Smile", 0), ("SO_sorge", "SO", "Concerned|Serious", 0), ("SO_denkt", "SO", "Suspicious", 0),
    ("SO_staunt", "SO", "Awe", 0), ("SO_laechelt", "SO", "Smile", 0),
    ("SC_ruhig", "SC", "Calm", 0), ("SC_redet", "SC", "Smile", 1), ("SC_streng", "SC", "Serious", 1),
    ("SC_ernst", "SC", "Serious", 0), ("SC_denkt", "SC", "Suspicious", 0), ("SC_froh", "SC", "Smile", 0),
    ("SC_sorge", "SC", "Concerned|Serious", 0),
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
