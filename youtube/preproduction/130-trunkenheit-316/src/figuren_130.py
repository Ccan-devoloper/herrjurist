"""Figuren für Folge 130 (Trunkenheit im Verkehr, Verkehrskontrolle am Ortsausgang) aus der LexVerse-Figma-Bibliothek
(Open Peeps, CC0). Alle Figuren fiktiv.
Heinrich (um 45, Autofahrer, 0,8 ‰, fährt schnurgerade; Stimme marc): standing/robot_dance-2 (schwarzes Oberteil, Hose Blau
#8DB3F2, weiße Schuhe; offene Handgeste), Kopf Short 4 (Haar dunkelbraun #5A3A22), Haut #E8B894, kein Bart, keine Brille.
Siegfried (um 60, Autofahrer, 1,2 ‰, unauffällig, hält sich für fit; Stimme william): standing/blazer-3 (Jackett Gelb
#F9D56E, schwarzes Shirt, Hose Grau #5B5F66), Kopf No Hair 2 (Haarkranz grau #B9B4AE), Brille Glasses 2, Haut #F0CDB4.
Polizistin (um 35, Funktionsrolle ohne Namen; Stimme sabrina): standing/blazer-4 (Jackett Dunkelblau #2F3D63, Oberteil
Hellblau #8DB3F2, schwarze Hose – uniformähnlich), Kopf Medium Bangs (#3A2A20), Haut #D9A47E.
Sachlich, keine Karikatur, keine bösen Mimiken bei den Fahrern; keine Prothesen-Posen (shirt-1/-2 bewusst nicht), keine
Bärte, keine Polka Dots. Posen nicht aus 127–129 (blazer-2, crossed_arms-2, easing-1, resting-2, pointing_finger-2, shirt-4)
und nicht aus 124 (walking-2, shirt-4, sitting/bike); Lexi bleibt robot_dance-1.
Präfix HE_/SI_/PO_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach
links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (HE_redet, SI_redet, PO_redet, Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
from PIL import Image
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_130")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "HE": ("standing/robot_dance-2", "Short 4", None, None, {"Skin": "#E8B894", "Pants": "#8DB3F2", "Hair": "#5A3A22"}),
    "SI": ("standing/blazer-3", "No Hair 2", None, "Glasses 2", {"Skin": "#F0CDB4", "Jacket": "#F9D56E", "Pants": "#5B5F66",
                                                              "Hair": "#B9B4AE"}),
    "PO": ("standing/blazer-4", "Medium Bangs", None, None, {"Skin": "#D9A47E", "Jacket": "#2F3D63", "Top": "#8DB3F2",
                                                           "Hair": "#3A2A20"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("HE_ruhig", "HE", "Calm", 0), ("HE_redet", "HE", "Concerned|Serious", 1), ("HE_denkt", "HE", "Suspicious", 0),
    ("HE_sorge", "HE", "Concerned|Serious", 0), ("HE_still", "HE", "Solemn", 0), ("HE_staunt", "HE", "Awe", 0),
    ("SI_ruhig", "SI", "Calm", 0), ("SI_redet", "SI", "Smile", 1), ("SI_froh", "SI", "Smile", 0),
    ("SI_still", "SI", "Solemn", 0), ("SI_sorge", "SI", "Concerned|Serious", 0), ("SI_muede", "SI", "Tired", 0),
    ("PO_ruhig", "PO", "Calm", 0), ("PO_redet", "PO", "Serious", 1), ("PO_ernst", "PO", "Serious", 0),
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
