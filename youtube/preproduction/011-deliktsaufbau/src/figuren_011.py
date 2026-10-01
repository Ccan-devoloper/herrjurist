"""Figuren für Folge 011 (Deliktsaufbau, Uferweg) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Nele (Joggerin, Mitte 50): walking-1 (läuft), resting-1 (steht) – alle Reihe -1
(farbiges Laufshirt Orange, schwarze Hose), Kopf Gray Medium. Holger (Radfahrer, um 40): sitting/bike (fährt) und
standing/blazer-4 (steht) mit derselben blauen Jacke und weißem Oberteil; nach dem Sturz sitting/hands_back-2 (am Boden,
Oberteil im Jackenblau, keine Jacke in dieser Pose – Abweichung im Szenenplan vermerkt). Herr Albrecht (Angler, um 70):
shirt-3, Kopf Gray Short, Schnurrbart Moustache 6 (verdeckt den Mund nicht), Brille Glasses 4.
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links, Suffix _r nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF): nur Calm, Smile, Serious, Driven, Fear, Very Angry, Tired,
Suspicious, Solemn bzw. „Augen|geschlossener Mund“. Sprechende Ansichten zusätzlich mit a/o/e (Augen der Grundmimik + Mund
Explaining/Concerned Fear/Hectic, Schnitt bei 60 % der Gesichtshöhe)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_011")
os.makedirs(ZIEL, exist_ok=True)
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

NE_F = {"Skin": "#E8B894", "Top": "#F9A66C", "Hair": "#C3C6CF"}
HO_F = {"Skin": "#C68A62", "Jacket": "#8DB3F2", "Top": "#FFFFFF", "Bicycle Frame": "#8DB3F2"}
HO_BODEN = {"Skin": "#C68A62", "Top": "#8DB3F2"}
AL_F = {"Skin": "#F0C8A8", "Top": "#8FD694", "Hair": "#D9D9DE"}

# Ansicht: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "NE_l": ("standing/walking-1", "Gray Medium", None, None, NE_F),
    "NE_s": ("standing/resting-1", "Gray Medium", None, None, NE_F),
    "HO_r": ("sitting/bike", "Short 2", None, None, HO_F),
    "HO_s": ("standing/blazer-4", "Short 2", None, None, HO_F),
    "HO_b": ("sitting/hands_back-2", "Short 2", None, None, HO_BODEN),
    "AL_s": ("standing/shirt-3", "Gray Short", "Moustache 6", "Glasses 4", AL_F),
}

# (Name, Ansicht, Grundmimik, mit Mundzuständen)
LISTE = [
    ("NE_laeuft", "NE_l", "Calm", 0), ("NE_schreck", "NE_l", "Fear", 0), ("NE_wut", "NE_l", "Very Angry", 0),
    ("NE_redet", "NE_s", "Very Angry", 1), ("NE_ruhig", "NE_s", "Calm", 0), ("NE_denkt", "NE_s", "Serious", 0),
    ("NE_ertappt", "NE_s", "Concerned|Serious", 0), ("NE_angst", "NE_s", "Fear", 0), ("NE_froh", "NE_s", "Smile", 0),
   
    ("HO_faehrt", "HO_r", "Driven", 0), ("HO_rad_redet", "HO_r", "Driven", 1), ("HO_rad_wut", "HO_r", "Very Angry", 0),
    ("HO_steht", "HO_s", "Calm", 0), ("HO_trinkt", "HO_s", "Smile", 0), ("HO_schreck", "HO_s", "Fear", 0),
    ("HO_boden", "HO_b", "Concerned|Serious", 0), ("HO_boden_muede", "HO_b", "Tired", 0),
    ("AL_ruhig", "AL_s", "Calm", 0), ("AL_schaut", "AL_s", "Suspicious", 0), ("AL_redet", "AL_s", "Serious", 1),
]

if __name__ == "__main__":
    n = 0
    for name, v, mimik, mund in LISTE:
        pose, kopf, bart, brille, farben = P[v]
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
