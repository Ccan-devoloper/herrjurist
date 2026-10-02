"""Figuren für Folge 087 (Raub § 249 Schema) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Margit (um 55, kommt vom Wochenmarkt, Opfer, respektvoll dargestellt): standing/polka_dots (weiß gepunktete Bluse der Pose,
        Hose Blau #8DB3F2, schwarze Schuhe), Kopf Gray Medium (Haar Grau #B9B4AE), Haut #F0C8A8.
Hagen (um 30, Täter, gewöhnlich gekleidet, keine Karikatur): standing/robot_dance-2 (schwarzes Langarmshirt der Pose,
        Hose Grün #8FD694, weiße Turnschuhe), Kopf Short 5 (schwarzes Haar), Haut #EDC1A0 (ähnlich hell wie Margit,
        keine Herkunfts- oder Hautfarbenzuschreibung). Kein Bart, keine Waffe, keine Prothesen-Pose.
Posen in 084–086 nicht verwendet (resting-2, blazer-3, robot_dance-3, walking-1, crossed_arms-1).
Alle Posen blicken im Original nach rechts; die Grundansicht blickt nach links (Figur rechts neben der Tafel), Suffix _r nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Smile, Fear, Awe, Suspicious, Driven, Solemn,
Very Angry, „Concerned|Serious“. Sprechende Ansichten zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining /
Concerned Fear / Hectic."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_087")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}
P = {
    "MG": ("standing/polka_dots", "Gray Medium", None, None, {"Skin": "#F0C8A8", "Pants": "#8DB3F2", "Hair": "#B9B4AE"}),
    "HG": ("standing/robot_dance-2", "Short 5", None, None, {"Skin": "#EDC1A0", "Pants": "#8FD694"}),
}
LISTE = [
    ("MG_ruhig", "MG", "Calm", 0), ("MG_froh", "MG", "Smile", 0), ("MG_erschrickt", "MG", "Fear", 0),
    ("MG_sorge", "MG", "Concerned|Serious", 0), ("MG_redet", "MG", "Concerned|Serious", 1), ("MG_ernst", "MG", "Serious", 0),
    ("MG_staunt", "MG", "Awe", 0),
    ("HG_ruhig", "HG", "Calm", 0), ("HG_listig", "HG", "Suspicious", 0), ("HG_redet", "HG", "Suspicious", 1),
    ("HG_entschlossen", "HG", "Driven", 0), ("HG_wut", "HG", "Very Angry", 0), ("HG_ernst", "HG", "Serious", 0),
    ("HG_ertappt", "HG", "Fear", 0), ("HG_still", "HG", "Solemn", 0),
]

if __name__ == "__main__":
    os.makedirs(ZIEL, exist_ok=True)
    n = 0
    for name, p, mimik, mund in LISTE:
        pose, kopf, bart, brille, farben = P[p]
        for suffix, gespiegelt in (("", True), ("_r", False)):
            figur(pose, kopf, mimik, bart, brille, farben, hoehe=1200, spiegeln=gespiegelt).save(f"{ZIEL}/{name}{suffix}.png"); n += 1
            if mund:
                for k, m in MUND.items():
                    figur(pose, kopf, f"{mimik.split('|')[0]}|{m}", bart, brille, farben, hoehe=1200,
                          spiegeln=gespiegelt).save(f"{ZIEL}/{name}{suffix}_{k}.png"); n += 1
    for name, (pose, mimik) in {"LX_erklaert": ("standing/robot_dance-1", "Smile"), "LX_warnt": ("standing/robot_dance-1", "Serious")}.items():
        a = LX.AUSSEHEN
        for k, g in {"": mimik, **{"_" + k: f"{mimik}|{m}" for k, m in MUND.items()}}.items():
            figur(pose, a["kopf"], g, a["bart"], a["brille"], a["farben"], hoehe=1200, spiegeln=True).save(f"{ZIEL}/{name}{k}.png"); n += 1
    print(n, "Figurenbilder ->", ZIEL)
