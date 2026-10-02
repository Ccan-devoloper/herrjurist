"""Figuren für Folge 084 (Nötigung § 240 Schema) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Gernot (um 60, Vermieter, sachlich, keine Karikatur): standing/blazer-3 (Sakko Blau #8DB3F2, dunkelgraue Hose), Kopf Gray Short,
        Haut #E3B48C. Keine Prothesen-Pose, kein Bart.
Gesine (um 35, Mieterin): standing/resting-2 und standing/walking-2 (gleiches Outfit: schwarzes Oberteil, grüne Hose #8FD694),
        Kopf Long Bangs (schwarzes Haar), weiße Schuhe, Haut #F0C8A8.
Posen in 081–083 nicht verwendet (polka_dots, pointing_finger-1, shirt-3, doctor-nurse-02, shirt-4, easing-1, resting-1, blazer-4).
Alle Posen blicken im Original nach rechts; die Grundansicht blickt nach links (Figur rechts neben der Tafel), Suffix _r nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Smile, Solemn, Tired, Suspicious, „Concerned|Serious“.
Sprechende Ansichten zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_084")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}
GS_F = {"Skin": "#F0C8A8", "Pants": "#8FD694", "Shoes": "#FFFFFF"}
P = {
    "GE": ("standing/blazer-3", "Gray Short", None, None, {"Skin": "#E3B48C", "Jacket": "#8DB3F2", "Pants": "#3C3C46", "Hair": "#A9A9A9"}),
    "GS": ("standing/resting-2", "Long Bangs", None, None, GS_F),
    "GW": ("standing/walking-2", "Long Bangs", None, None, GS_F),
}
LISTE = [
    ("GE_ruhig", "GE", "Calm", 0), ("GE_ernst", "GE", "Serious", 0), ("GE_redet", "GE", "Serious", 1),
    ("GE_still", "GE", "Solemn", 0), ("GE_skeptisch", "GE", "Suspicious", 0),
    ("GS_ruhig", "GS", "Calm", 0), ("GS_sorge", "GS", "Concerned|Serious", 0), ("GS_redet", "GS", "Concerned|Serious", 1),
    ("GS_ernst", "GS", "Serious", 0), ("GS_muede", "GS", "Tired", 0), ("GS_froh", "GS", "Smile", 0),
    ("GW_ernst", "GW", "Serious", 0), ("GW_muede", "GW", "Tired", 0),
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
