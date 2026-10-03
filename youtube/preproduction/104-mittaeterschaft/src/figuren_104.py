"""Figuren für Folge 104 (Mittäterschaft § 25 II) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Vier Beteiligte, klar unterscheidbar (Kleidung, Frisur, Statur der Pose, Namensschild):
Ansgar (AN, um 50, Planer): standing/blazer-4 (Blazer Blau #8DB3F2, Hemd der Pose, schwarze Hose), Kopf Gray Short, Haut #E8B896.
Kilian (KI, um 25, droht nur mit Worten und Körpersprache): standing/crossed_arms-2 (verschränkte Arme, schwarzer Pullover der
        Pose, Hose Rot #F07A6A), Kopf Short 4, Haut #F0C8A8.
Fenja (FE, um 25, greift in die Kasse): standing/walking-1 (T-Shirt Lila #B8A9F5, schwarze Hose), Kopf Long, Haut #EDC1A0.
Thea (TH, um 20, steht Schmiere): standing/resting-1 (Langarmshirt Grün #8FD694, schwarze Hose), Kopf Medium Bangs 3, Haut #D9A07A.
Emil (EM, um 60, Kioskinhaber): standing/shirt-4 (schwarzes Hemd der Pose, Hose Blau #8DB3F2), Kopf No Hair 3, Haut #F2CDB0.
Keine Bärte, keine Waffen, keine Prothesen-Posen (blazer-1/2, shirt-1/2 bewusst nicht verwendet), keine „fiese“ Mimik.
Posen der letzten drei Folgen (101–103: crossed_arms-1, pointing_finger-1/2, robot_dance-2, polka_dots, shirt-3, easing-1/2)
nicht verwendet. Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (blickt nach links), Suffix _r nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md); Sprechende Ansichten (AN_redet, KI_redet, FE_redet) zusätzlich
a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_104")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}
P = {
    "AN": ("standing/blazer-4", "Gray Short", None, None, {"Skin": "#E8B896", "Jacket": "#8DB3F2"}),
    "KI": ("standing/crossed_arms-2", "Short 4", None, None, {"Skin": "#F0C8A8", "Pants": "#F07A6A"}),
    "FE": ("standing/walking-1", "Long", None, None, {"Skin": "#EDC1A0", "Top": "#B8A9F5"}),
    "TH": ("standing/resting-1", "Medium Bangs 3", None, None, {"Skin": "#D9A07A", "Top": "#8FD694"}),
    "EM": ("standing/shirt-4", "No Hair 3", None, None, {"Skin": "#F2CDB0", "Pants": "#8DB3F2"}),
}
LISTE = [
    ("AN_ruhig", "AN", "Calm", 0), ("AN_froh", "AN", "Smile", 0), ("AN_ernst", "AN", "Serious", 0),
    ("AN_redet", "AN", "Serious", 1), ("AN_entschlossen", "AN", "Driven", 0), ("AN_still", "AN", "Solemn", 0),
    ("KI_ruhig", "KI", "Calm", 0), ("KI_ernst", "KI", "Serious", 0), ("KI_redet", "KI", "Serious", 1),
    ("KI_entschlossen", "KI", "Driven", 0), ("KI_still", "KI", "Solemn", 0),
    ("FE_ruhig", "FE", "Calm", 0), ("FE_entschlossen", "FE", "Driven", 0), ("FE_redet", "FE", "Driven", 1),
    ("FE_ernst", "FE", "Serious", 0), ("FE_still", "FE", "Solemn", 0),
    ("TH_ruhig", "TH", "Calm", 0), ("TH_wachsam", "TH", "Suspicious", 0), ("TH_ernst", "TH", "Serious", 0),
    ("TH_sorge", "TH", "Concerned|Serious", 0), ("TH_still", "TH", "Solemn", 0),
    ("EM_ruhig", "EM", "Calm", 0), ("EM_froh", "EM", "Smile", 0), ("EM_erschrickt", "EM", "Fear", 0),
    ("EM_sorge", "EM", "Concerned|Serious", 0),
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
