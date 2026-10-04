"""Figuren für Folge 166 (Trierer Weinversteigerung) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren
fiktiv; die realen Beteiligten des BGH-Falls (Sparkasse, Firmen) werden nicht dargestellt.
Ekkehard (um 40, Zuschauer bei der Versteigerung; Stimme christian): standing/resting-2 (Hand unten) und
standing/pointing_finger-2 (erhobene Hand beim Winken) – beide mit dem festen schwarzen Oberteil der Posen, Hose Blau
#8DB3F2, Kopf Short 1, Haut #E3B08A, ohne Bart/Brille (gleiches Outfit in beiden Posen).
Frau Haller (um 60, Auktionatorin; Stimme hilde): standing/blazer-3 (Blazer Türkis #7FD6D0, Hose #4A4A58), Kopf Gray Bun,
Brille Glasses 2, Haut #F0C8A8.
Reinhild (um 40, Ekkehards Freundin an der Tür; spricht nicht): standing/walking-1 (Oberteil Orange #F9A66C), Kopf Long
Curly (Haar #6B4226), Haut #C98E66.
Posen nicht aus 163–165/162 (easing-1/-2, walking-3, robot_dance-2, shirt-3, blazer-4, closed_legs-1); keine Polka
Dots, keine Bärte, keine Prothesen-Posen.
Präfix EK_/HA_/RE_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt
nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (EK_redet, HA_redet, Lexi) zusätzlich
mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_166")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

EKF = {"Skin": "#E3B08A", "Pants": "#8DB3F2"}
P = {
    "EK": ("standing/resting-2", "Short 1", None, None, EKF),
    "EW": ("standing/pointing_finger-2", "Short 1", None, None, EKF),      # Ekkehard mit erhobener Hand
    "HA": ("standing/blazer-3", "Gray Bun", None, "Glasses 2", {"Skin": "#F0C8A8", "Jacket": "#7FD6D0", "Pants": "#4A4A58"}),
    "RE": ("standing/walking-1", "Long Curly", None, None, {"Skin": "#C98E66", "Top": "#F9A66C", "Hair": "#6B4226"}),
}

LISTE = [
    ("EK_ruhig", "EK", "Smile", 0), ("EK_redet", "EK", "Concerned|Serious", 1), ("EK_denkt", "EK", "Suspicious", 0),
    ("EK_froh", "EK", "Cute", 0), ("EK_sorge", "EK", "Concerned|Serious", 0),
    ("EK_winkt", "EW", "Cute", 0), ("EK_staunt", "EW", "Awe", 0),
    ("HA_ruhig", "HA", "Smile", 0), ("HA_redet", "HA", "Smile", 1), ("HA_denkt", "HA", "Suspicious", 0),
    ("HA_froh", "HA", "Cute", 0), ("HA_ernst", "HA", "Serious", 0),
    ("RE_ruhig", "RE", "Smile", 0), ("RE_froh", "RE", "Cute", 0), ("RE_staunt", "RE", "Awe", 0),
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
    for name, (pose, mimik) in {"LX_erklaert": ("standing/robot_dance-1", "Smile"), "LX_warnt": ("standing/robot_dance-1", "Serious")}.items():
        a = LX.AUSSEHEN
        for k, g in {"": mimik, **{"_" + k: f"{mimik}|{m}" for k, m in MUND.items()}}.items():
            figur(pose, a["kopf"], g, a["bart"], a["brille"], a["farben"], hoehe=1200, spiegeln=True).save(f"{ZIEL}/{name}{k}.png"); n += 1
    print(n, "Figurenbilder ->", ZIEL)
