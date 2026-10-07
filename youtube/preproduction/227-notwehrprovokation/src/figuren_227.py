"""Figuren für Folge 227 (Notwehrprovokation) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv.
Ferdinand (FE, Anfang 30, provoziert; Stimme stephan): standing/blazer-4 (Sakko Petrol #3E6E8E über cremefarbenem Shirt #F2E6CF, schwarze Hose der Pose),
  Kopf Short 3 (Haar #5A3A22), Haut #EBC29E, kein Bart, keine Brille – gewöhnlicher Festbesucher, keine „fiese“ Täterfigur.
Herr Pelzer (PE, um 50, kräftig; spricht nicht): standing/pointing_finger-1 (schwarze Kleidung der Pose),
  Kopf Gray Short, Haut #E3B08C.
Josefine (JO, Mitte 20, Kollegin; Stimme lucy): standing/easing-1 (offenes Hemd Grün #8FD694 über weißem Shirt), Kopf Long
  (Haar #7A4A2A), Haut #F1CBA6.
Frau Höfer (HO, um 65, Weinstand; Stimme hilde): standing/resting-1 (Oberteil Lila #B8A9F5), Kopf Gray Bun, Brille Glasses 2,
  Haut #E8B894.
Posen nicht aus 223–225 und 226 (dort noch keine Figuren) (shirt-2/-3/-4, blazer-1/-3, easing-2, resting-2, walking-1/-2, robot_dance-3, pointing_finger-2,
crossed_arms-1) und nicht aus 214 (easing-2, walking-1/-3); keine Prothesen-Posen (blazer-2, shirt-1), keine Polka Dots, keine
Bärte. Keine Waffe, kein Messer in der Hand.
Präfix FE_/PE_/JO_/HO_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach
links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (FE_plant, FE_redet, JO_redet, HO_ruft, Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_227")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "FE": ("standing/blazer-4", "Short 3", None, None, {"Skin": "#EBC29E", "Jacket": "#3E6E8E", "Top": "#F2E6CF",
                                                       "Hair": "#5A3A22"}),
    "PE": ("standing/pointing_finger-1", "Gray Short", None, None, {"Skin": "#E3B08C"}),
    "JO": ("standing/easing-1", "Long", None, None, {"Skin": "#F1CBA6", "Jacket": "#8FD694", "Top": "#FFFFFF",
                                                     "Hair": "#7A4A2A"}),
    "HO": ("standing/resting-1", "Gray Bun", None, "Glasses 2", {"Skin": "#E8B894", "Top": "#B8A9F5"}),
}

LISTE = [
    ("FE_ruhig", "FE", "Calm", 0), ("FE_schlau", "FE", "Suspicious", 0), ("FE_froh", "FE", "Smile", 0),
    ("FE_ernst", "FE", "Serious", 0), ("FE_sorge", "FE", "Concerned|Serious", 0), ("FE_angst", "FE", "Fear", 0),
    ("FE_muede", "FE", "Tired", 0), ("FE_denkt", "FE", "Driven", 0),
    ("FE_plant", "FE", "Suspicious", 1), ("FE_redet", "FE", "Serious", 1),
    ("PE_ruhig", "PE", "Calm", 0), ("PE_wuetend", "PE", "Very Angry", 0), ("PE_ernst", "PE", "Serious", 0),
    ("PE_schmerz", "PE", "Concerned|Serious", 0), ("PE_muede", "PE", "Tired", 0), ("PE_denkt", "PE", "Suspicious", 0),
    ("JO_ruhig", "JO", "Calm", 0), ("JO_sorge", "JO", "Concerned|Serious", 0), ("JO_angst", "JO", "Fear", 0),
    ("JO_ernst", "JO", "Serious", 0), ("JO_denkt", "JO", "Suspicious", 0), ("JO_froh", "JO", "Smile", 0),
    ("JO_redet", "JO", "Concerned|Serious", 1),
    ("HO_ruhig", "HO", "Calm", 0), ("HO_froh", "HO", "Smile", 0), ("HO_sorge", "HO", "Concerned|Serious", 0),
    ("HO_angst", "HO", "Fear", 0), ("HO_ernst", "HO", "Serious", 0), ("HO_ruft", "HO", "Fear", 1),
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
