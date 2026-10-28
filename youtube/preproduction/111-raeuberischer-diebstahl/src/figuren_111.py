"""Figuren für Folge 111 (Räuberischer Diebstahl § 252) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Gottfried (um 60, Täter, gewöhnlich gekleidet, keine Karikatur): standing/easing-1 (offene Überjacke Lila #B8A9F5 über
        weißem T-Shirt, schwarze Hose und Turnschuhe der Pose), Kopf Gray Short (Haar Grau #B9B4AE), Haut #EDC1A0.
        Kein Bart, keine Waffe, keine Prothesen-Pose, keine Herkunfts- oder Hautfarbenzuschreibung.
Edda (um 35, Mitarbeiterin des Elektromarkts): standing/pointing_finger-2 (schwarzes Langarmoberteil der Pose, Hose Rot
        #F07A6A), Kopf Bun (dunkles Haar), Haut #C68E62.
Posen und Muster nicht aus 107–109 (shirt-3, resting-2, blazer-3, robot_dance-3, pointing_finger-1, crossed_arms-1,
easing-2, walking-3) und nicht aus 087 (polka_dots, robot_dance-2).
Alle Posen blicken im Original nach rechts; die Grundansicht blickt nach links (Figur rechts neben der Tafel), Suffix _r nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Smile, Fear, Awe, Suspicious, Driven, Solemn,
„Concerned|Serious“. Sprechende Ansichten zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_111")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}
P = {
    "GO": ("standing/easing-1", "Gray Short", None, None, {"Skin": "#EDC1A0", "Jacket": "#B8A9F5", "Top": "#FFFFFF", "Hair": "#B9B4AE"}),
    "ED": ("standing/pointing_finger-2", "Bun", None, None, {"Skin": "#C68E62", "Pants": "#F07A6A"}),
}
LISTE = [
    ("GO_ruhig", "GO", "Calm", 0), ("GO_listig", "GO", "Suspicious", 0), ("GO_redet", "GO", "Driven", 1),
    ("GO_entschlossen", "GO", "Driven", 0), ("GO_ernst", "GO", "Serious", 0), ("GO_ertappt", "GO", "Fear", 0),
    ("GO_still", "GO", "Solemn", 0),
    ("ED_ruhig", "ED", "Calm", 0), ("ED_ernst", "ED", "Serious", 0), ("ED_redet", "ED", "Serious", 1),
    ("ED_erschrickt", "ED", "Fear", 0), ("ED_sorge", "ED", "Concerned|Serious", 0), ("ED_staunt", "ED", "Awe", 0),
    ("ED_froh", "ED", "Smile", 0),
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
