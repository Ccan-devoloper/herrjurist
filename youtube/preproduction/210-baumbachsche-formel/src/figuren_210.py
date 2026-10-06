"""Figuren für Folge 210 (Baumbachsche Kostenformel: Darlehensklage gegen zwei Gesamtschuldner) aus der
LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv.
Frau Eschenbach (ES, um 65, Darlehensgeberin, Klägerin; Stimme hilde): standing/blazer-1 (blaue Jacke #8DB3F2, dunkle Hose
  #3A3A48; die Pose zeigt eine Beinprothese – kein Täterbezug), Kopf Gray Bun (Haar #B8B8B8), Haut #F2C9A8.
Herr Lohmann (LO, um 40, Ladeninhaber, Beklagter zu 1; Stimme stephan, spricht im Video nicht): standing/crossed_arms-2
  (schwarzes Oberteil, Hose Taubenblau #5B6B8C, verschränkte Arme), Kopf Short 2 (Haar #4A3426), Haut #E0A981.
Frau Kreutzer (KR, um 30, Ladeninhaberin, Beklagte zu 2; Stimme lucy): standing/crossed_arms-1 (Oberteil Grün #8FD694,
  schwarze Hose), Kopf Medium Bangs (Haar #2E2018), Haut #C98F6A.
Richter am Landgericht (RI, um 55, ohne Namen; Stimme christian): standing/blazer-2 (dunkler Blazer #3A3A48 wie eine Robe,
  weißes Oberteil; Beine hinter dem Richtertisch), Kopf Short 1 (Haar Grau #9A9A9A), Brille Glasses 2, Haut #F0D0B0.
Posen der letzten Folgen (205–209: shirt-3, shirt-4, resting-1, resting-2, easing-1, easing-2, pointing_finger-1/-2,
robot_dance-2/-3, blazer-3, blazer-4, walking-1, walking-2) nicht verwendet; keine Polka Dots, keine Bärte, keine Karikatur.
Präfixe ES_/LO_/KR_/RI_ (nie ER_).
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Smile, Serious, Driven, Suspicious, Tired, Very Angry bzw.
„Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten ES_redet, ES_fragt, KR_redet, RI_redet (und Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_210")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "ES": ("standing/blazer-1", "Gray Bun", None, None, {"Skin": "#F2C9A8", "Jacket": "#8DB3F2", "Pants": "#3A3A48",
                                                       "Hair": "#B8B8B8"}),
    "LO": ("standing/crossed_arms-2", "Short 2", None, None, {"Skin": "#E0A981", "Pants": "#5B6B8C", "Hair": "#4A3426"}),
    "KR": ("standing/crossed_arms-1", "Medium Bangs", None, None, {"Skin": "#C98F6A", "Top": "#8FD694", "Hair": "#2E2018"}),
    "RI": ("standing/blazer-2", "Short 1", None, "Glasses 2", {"Skin": "#F0D0B0", "Jacket": "#3A3A48", "Top": "#FFFFFF", "Prosthesis": "#B8B8B8",
                                                             "Hair": "#9A9A9A"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("ES_ruhig", "ES", "Calm", 0), ("ES_froh", "ES", "Smile", 0), ("ES_denkt", "ES", "Serious", 0),
    ("ES_sorge", "ES", "Concerned|Serious", 0), ("ES_aerger", "ES", "Very Angry", 0),
    ("ES_redet", "ES", "Driven", 1), ("ES_fragt", "ES", "Concerned|Serious", 1),
    ("LO_ruhig", "LO", "Calm", 0), ("LO_froh", "LO", "Smile", 0), ("LO_denkt", "LO", "Serious", 0),
    ("LO_sorge", "LO", "Concerned|Serious", 0), ("LO_skeptisch", "LO", "Suspicious", 0), ("LO_muede", "LO", "Tired", 0),
    ("KR_ruhig", "KR", "Calm", 0), ("KR_froh", "KR", "Smile", 0), ("KR_denkt", "KR", "Serious", 0),
    ("KR_sorge", "KR", "Concerned|Serious", 0), ("KR_skeptisch", "KR", "Suspicious", 0),
    ("KR_redet", "KR", "Serious", 1),
    ("RI_ruhig", "RI", "Calm", 0), ("RI_denkt", "RI", "Suspicious", 0), ("RI_redet", "RI", "Serious", 1),
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
