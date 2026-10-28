"""Figuren für Folge 264 (Begleitverfügung StA: Haft, Pflichtverteidiger, Mitteilungen) aus der LexVerse-Figma-Bibliothek
(Open Peeps, CC0). Alle Figuren fiktiv.
Referendarin Ortlieb (um 27, Station Staatsanwaltschaft; Stimme lucy): standing/resting-1 (Oberteil Grün #8FD694, schwarze
Hose), Kopf Long Bangs, Haut #F2C9A8.
Oberstaatsanwältin Pfaff (um 60, Ausbilderin; Stimme hilde): standing/blazer-4 (Blazer Marineblau #3D5A80 über weißem
Oberteil, schwarze Hose), Kopf Gray Medium (Haar Grau #C9C9C9), Glasses 2, Haut #EDC3A0.
Herr Wittig (38, Beschuldigter in Untersuchungshaft, spricht nicht): standing/robot_dance-2 (schwarzes Oberteil, Hose
Jeansblau #5B7DB1), Kopf Short 1, Haut #E9B996 – Alltagskleidung, ruhige Mimik, kein Klischee, keine Zelle.
Herr Dengler (um 50, Anzeigeerstatter, Verletzter; Stimme stephan): standing/crossed_arms-2 (schwarzes Oberteil, Hose
Graublau #6B7A8F), Kopf Short 2, Glasses 3, Haut #DDA885.
Keine Bärte, keine Polka Dots, keine Prothesen-Posen (blazer-1/-2, shirt-1/-2). Posen nicht aus den letzten drei Folgen
261–263 (resting-2, shirt-3, shirt-4, easing-1, easing-2, blazer-3, pointing_finger-2, walking-1/-2/-3); Lexi bleibt
robot_dance-1. Präfix OR_/PF_/WI_/DE_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist
gespiegelt und blickt nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (OR_redet, PF_redet, PF_redet2, DE_redet,
Lexi) zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_264")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "OR": ("standing/resting-1", "Long Bangs", None, None, {"Skin": "#F2C9A8", "Top": "#8FD694"}),
    "PF": ("standing/blazer-4", "Gray Medium", None, "Glasses 2", {"Skin": "#EDC3A0", "Hair": "#C9C9C9", "Jacket": "#3D5A80",
                                                                   "Top": "#FFFFFF"}),
    "WI": ("standing/robot_dance-2", "Short 1", None, None, {"Skin": "#E9B996", "Pants": "#5B7DB1"}),
    "DE": ("standing/crossed_arms-2", "Short 2", None, "Glasses 3", {"Skin": "#DDA885", "Pants": "#6B7A8F"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("OR_ruhig", "OR", "Calm", 0), ("OR_redet", "OR", "Concerned|Serious", 1), ("OR_denkt", "OR", "Suspicious", 0),
    ("OR_froh", "OR", "Smile", 0), ("OR_fest", "OR", "Driven", 0), ("OR_sorge", "OR", "Concerned|Serious", 0),
    ("OR_staunt", "OR", "Awe", 0),
    ("PF_ruhig", "PF", "Calm", 0), ("PF_redet", "PF", "Serious", 1), ("PF_redet2", "PF", "Smile", 1),
    ("PF_ernst", "PF", "Serious", 0), ("PF_froh", "PF", "Smile", 0), ("PF_denkt", "PF", "Suspicious", 0),
    ("PF_still", "PF", "Solemn", 0),
    ("WI_ruhig", "WI", "Calm", 0), ("WI_still", "WI", "Solemn", 0), ("WI_ernst", "WI", "Serious", 0),
    ("DE_ruhig", "DE", "Calm", 0), ("DE_redet", "DE", "Suspicious", 1), ("DE_muede", "DE", "Tired", 0),
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
