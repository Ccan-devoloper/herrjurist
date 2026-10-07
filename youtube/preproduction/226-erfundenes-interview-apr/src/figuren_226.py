"""Figuren für Folge 226 (Erfundenes Interview) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv;
die reale Person des echten Falls wird NICHT dargestellt und nicht karikiert. Das Magazin „Funkelblatt“ ist erfunden.
Juliane Hellberg (JU, um 35, Schauspielerin; Stimme julia): standing/resting-1 (Oberteil Rosa #F2A7B8, schwarze Hose der Pose),
Kopf Long Curly (Haar der Bibliothek, schwarz – nicht einfärbbar), Haut #F0C8A8.
Chefredakteur Kettler (KE, um 35; Stimme niklas): standing/blazer-4 (Sakko Blau #8DB3F2, weißes Shirt), Kopf Short 2 (Haar
#4A3426), Brille Glasses 2, Haut #E3B08C, kein Bart – sachlich, keine Karikatur.
Dr. Ruhnau (RU, um 60, Anwalt; Stimme helmut): standing/crossed_arms-2 (schwarzes Oberteil der Pose, Hose Graublau #6B7A8F),
Kopf Gray Short (graues Haar der Bibliothek), Brille Glasses 4, Haut #EBC29E, kein Bart (Bärte nie über dem Mund). pointing_finger-1
verworfen (Oberteil lässt sich nicht einfärben, Figur wirkt ganz schwarz).
Leserin (LE, um 25; Stimme ela_froh): standing/walking-3 (Kleidung der Pose), Kopf Bun 2 (Haar #2B2B2B), Haut #B07552.
Posen nicht aus 223–225 (shirt-2/3/4, blazer-1/3, easing-2, resting-2, walking-1/2, robot_dance-3, pointing_finger-2,
crossed_arms-1); keine Polka Dots, keine Prothesen-Posen (blazer-2 deshalb verworfen), keine Bärte.
Präfix JU_/KE_/RU_/LE_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach
links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (JU_redet, KE_redet, RU_redet, LE_redet,
Lexi) zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_226")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "JU": ("standing/resting-1", "Long Curly", None, None, {"Skin": "#F0C8A8", "Top": "#F2A7B8", "Hair": "#C8873A"}),
    "KE": ("standing/blazer-4", "Short 2", None, "Glasses 2", {"Skin": "#E3B08C", "Jacket": "#8DB3F2", "Top": "#FFFFFF",
                                                              "Hair": "#4A3426"}),
    "RU": ("standing/crossed_arms-2", "Gray Short", None, "Glasses 4", {"Skin": "#EBC29E", "Pants": "#6B7A8F"}),
    "LE": ("standing/walking-3", "Bun 2", None, None, {"Skin": "#B07552", "Hair": "#2B2B2B"}),
}

LISTE = [
    ("JU_ruhig", "JU", "Calm", 0), ("JU_redet", "JU", "Serious", 1), ("JU_ernst", "JU", "Serious", 0),
    ("JU_sorge", "JU", "Concerned|Serious", 0), ("JU_denkt", "JU", "Suspicious", 0), ("JU_froh", "JU", "Smile", 0),
    ("JU_muede", "JU", "Tired", 0),
    ("KE_ruhig", "KE", "Calm", 0), ("KE_redet", "KE", "Smile", 1), ("KE_froh", "KE", "Smile", 0),
    ("KE_denkt", "KE", "Suspicious", 0), ("KE_ernst", "KE", "Serious", 0),
    ("RU_ruhig", "RU", "Calm", 0), ("RU_redet", "RU", "Serious", 1), ("RU_ernst", "RU", "Serious", 0),
    ("RU_froh", "RU", "Smile", 0), ("RU_denkt", "RU", "Suspicious", 0),
    ("LE_ruhig", "LE", "Calm", 0), ("LE_redet", "LE", "Cute", 1), ("LE_froh", "LE", "Cute", 0),
    ("LE_staunt", "LE", "Awe", 0),
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
