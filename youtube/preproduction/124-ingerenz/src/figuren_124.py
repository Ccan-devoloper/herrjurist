"""Figuren für Folge 124 (Ingerenz, Dorfstraße: Unfall und Weiterfahrt) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv.
Eckhard (um 50, Autofahrer, fährt zu schnell, erfasst den Fußgänger, hält kurz an und fährt weiter; Stimme christian):
standing/walking-2 (schwarzes Oberteil, Hose Blau #8DB3F2, weiße Schuhe), Kopf Short 1 (Haar grau meliert #7D7D7D), kein
Bart, keine Brille. Sachlich, keine Dämonisierung: keine bösen Mimiken (kein Contempt, kein Angry), nur Calm/Fear/
Suspicious/Serious/Solemn/Concerned|Serious.
Fußgänger (um 70, Funktionsrolle, spricht nicht): standing/shirt-4 (schwarzes Hemd, Hose Lila #B8A9F5), Kopf No Hair 3
(Glatze mit grauem Haarkranz), Haut #F2D0B1. Stehend (Calm) beim Überqueren; nach dem Unfall liegt er ruhig: dieselbe
Figur mit Eyes Closed um 90° gedreht (keine Verletzungsdetails, kein Blut; nur gedreht, nicht umgezeichnet).
Radfahrerin (um 30, Funktionsrolle; Stimme lucy): sitting/bike (Jacke Grün, schwarze Hose, rosa Fahrrad), Kopf
Medium Straight, Haut #C98F6B; Mimiken Calm, Fear (findet ihn), Concerned|Serious (redet).
Keine Prothesen-Posen, keine Bärte, keine Polka Dots. Posen und Kleidung nicht aus 121–123 (polka_dots, shirt-3, walking-3,
walking-1, resting-2, easing-1, blazer-3) und nicht aus 115 (shirt-3, crossed_legs, resting-2, blazer-3).
Präfix EC_/FU_/RA_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach
links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (EC_redet, RA_redet, Lexi) zusätzlich mit
a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
from PIL import Image
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_124")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "EC": ("standing/walking-2", "Short 1", None, None, {"Skin": "#E8B894", "Pants": "#8DB3F2", "Hair": "#7D7D7D"}),
    "FU": ("standing/shirt-4", "No Hair 3", None, None, {"Skin": "#F2D0B1", "Pants": "#B8A9F5"}),
    "RA": ("sitting/bike", "Medium Straight", None, None, {"Skin": "#C98F6B", "Hair": "#3A2A20"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("EC_ruhig", "EC", "Calm", 0), ("EC_schreck", "EC", "Fear", 0), ("EC_denkt", "EC", "Suspicious", 0),
    ("EC_redet", "EC", "Serious", 1), ("EC_still", "EC", "Solemn", 0), ("EC_sorge", "EC", "Concerned|Serious", 0),
    ("FU_ruhig", "FU", "Calm", 0),
    ("RA_ruhig", "RA", "Calm", 0), ("RA_schreck", "RA", "Fear", 0), ("RA_redet", "RA", "Concerned|Serious", 1),
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
    # Fußgänger liegt ruhig am Straßenrand: dieselbe Figur mit geschlossenen Augen, um 90° gedreht (Kopf rechts bzw. links)
    pose, kopf, bart, brille, farben = P["FU"]
    stehend = figur(pose, kopf, "Eyes Closed", bart, brille, farben, hoehe=1200)
    for suffix, winkel in (("", -90), ("_l", 90)):
        im = stehend.rotate(winkel, expand=True, resample=Image.BICUBIC)
        im.crop(im.getbbox()).save(f"{ZIEL}/FU_liegt{suffix}.png"); n += 1
    # Lexi (feste Moderatorin, Stimme Carla), blickt nach links zur Tafel
    for name, (pose, mimik) in {"LX_erklaert": ("standing/robot_dance-1", "Smile"), "LX_warnt": ("standing/robot_dance-1", "Serious")}.items():
        a = LX.AUSSEHEN
        for k, g in {"": mimik, **{"_" + k: f"{mimik}|{m}" for k, m in MUND.items()}}.items():
            figur(pose, a["kopf"], g, a["bart"], a["brille"], a["farben"], hoehe=1200, spiegeln=True).save(f"{ZIEL}/{name}{k}.png"); n += 1
    print(n, "Figurenbilder ->", ZIEL)
