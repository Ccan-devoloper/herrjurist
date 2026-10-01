"""Figuren für Folge 002 (BGB AT Überblick, E-Bike-Fall) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Karl (72): resting-1, Emma (17): easing-2 und sitting/bike (Probefahrt; dunkle Hose,
weil die Radpose keine einfärbbare Hose hat), Jens (Mitte 40): resting-2 bzw. robot_dance-2 (gleiche Reihe -2: schwarzes Oberteil,
blaue Hose). Grundansicht blickt nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Je sprechender Ansicht drei Mundzustände a/o/e zusätzlich zur Grundmimik (lexpeeps 'Augen|Mund', Schnitt bei 60 % Gesichtshöhe)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_002")
os.makedirs(ZIEL, exist_ok=True)
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben, Grundansicht gespiegelt?)
P = {
    "KA": ("standing/resting-1", "Gray Short", "Moustache 9", "Glasses 2", {"Skin": "#EBC4A0", "Top": "#8FD694"}, SPK := 1),
    "EM": ("standing/easing-2", "Long", None, None, {"Skin": "#B07552", "Pants": "#2E2E3A", "Jacket": "#F9A66C"}, SPE := 1),
    "ER": ("sitting/bike", "Long", None, None, {"Skin": "#B07552", "Jacket": "#F9A66C", "Top": "#2E2E3A",
                                                "Bicycle Frame": "#8DB3F2"}, 1),     # Emma auf dem E-Bike (Probefahrt)
    "JE": ("standing/resting-2", "Pomp", "Full", None, {"Skin": "#D9A07A", "Pants": "#8DB3F2"}, SPJ := 1),
    "JG": ("standing/robot_dance-2", "Pomp", "Full", None, {"Skin": "#D9A07A", "Pants": "#8DB3F2"}, 1),   # Jens mit Geste
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts).
# Grundmimik "Augen|Mund": Mimiken mit offenem oder unklarem Mund (Concerned, Smile Big, Fear, Awe, Cheeky) bekommen einen
# geschlossenen Mund, damit der Mund in Pausen und bei anderen Sprechern zu ist (Befund Koordinator/Folge 004, 01.10.2026).
LISTE = [
    ("KA_ruhig", "KA", "Calm", 0), ("KA_redet", "KA", "Smile", 1), ("KA_streng", "KA", "Driven", 1),
    ("KA_denkt", "KA", "Concerned|Serious", 0), ("KA_froh", "KA", "Smile Big|Smile", 0), ("KA_muede", "KA", "Tired", 0),
    ("EM_ruhig", "EM", "Calm", 0), ("EM_froh", "EM", "Smile", 0), ("EM_redet", "EM", "Smile Big|Smile", 1),
    ("EM_denkt", "EM", "Serious", 0), ("EM_staunt", "EM", "Awe|Serious", 0), ("EM_rad", "ER", "Smile", 1),
    ("JE_ruhig", "JE", "Calm", 0), ("JE_schreck", "JE", "Fear|Serious", 0), ("JE_denkt", "JE", "Concerned|Serious", 0),
    ("JE_froh", "JE", "Cheeky|Smile", 0),
    ("JG_redet", "JG", "Smile", 1), ("JG_ernst", "JG", "Serious", 1),
]

if __name__ == "__main__":
    n = 0
    for name, p, mimik, mund in LISTE:
        pose, kopf, bart, brille, farben, sp = P[p]
        for suffix, gespiegelt in (("", sp), ("_r", 1 - sp)):
            figur(pose, kopf, mimik, bart, brille, farben, hoehe=1200, spiegeln=bool(gespiegelt)).save(f"{ZIEL}/{name}{suffix}.png"); n += 1
            if mund:
                for k, m in MUND.items():
                    figur(pose, kopf, f"{mimik.split('|')[0]}|{m}", bart, brille, farben, hoehe=1200,
                          spiegeln=bool(gespiegelt)).save(f"{ZIEL}/{name}{suffix}_{k}.png"); n += 1
    # Lexi (feste Moderatorin, Stimme Carla), blickt nach links zur Tafel
    for name, (pose, mimik) in {"LX_erklaert": ("standing/robot_dance-1", "Smile"), "LX_warnt": ("standing/robot_dance-1", "Serious"),
                                "LX_freut": ("standing/crossed_arms-1", "Cute")}.items():
        a = LX.AUSSEHEN
        for k, g in {"": mimik, **{"_" + k: f"{mimik}|{m}" for k, m in MUND.items()}}.items():
            figur(pose, a["kopf"], g, a["bart"], a["brille"], a["farben"], hoehe=1200, spiegeln=True).save(f"{ZIEL}/{name}{k}.png"); n += 1
    print(n, "Figurenbilder ->", ZIEL)
