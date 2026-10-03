"""Figuren für Folge 106 (Verbraucherbegriff, §§ 13, 14 BGB) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv.
Ricarda (um 55, Rechtsanwältin mit eigener Kanzlei, kauft den Laptop): standing/blazer-4 (lila Blazer, weißes Oberteil,
schwarze Hose, weiße Schuhe), Kopf Gray Medium (graues Haar), Brille Glasses 3.
Herr Kortmann (um 40, betreibt einen Elektronikhandel im Internet, Unternehmer): standing/crossed_arms-2 (schwarzer
Pullover, verschränkte Arme, braune Hose), Kopf Short 4. Keine Prothesen-Pose, keine Bärte, keine Karikatur.
Posen, Kleidung und Muster nicht aus den Folgen 103–105 (easing-1, pointing_finger-2, resting-1, walking-2, blazer-2;
104: nur Skript ohne Figuren), keine Polka Dots.
Präfix RI_/KO_ (nie ER_, weil bausteine.peep_voll ER_* in den Ordner op_we umleitet). Alle Posen blicken im Original nach
rechts; die Grundansicht ist gespiegelt und blickt nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Suspicious, Awe bzw. „Augen|geschlossener Mund“
(Smile Big|Smile, Concerned|Serious). Sprechende Ansichten (RI_redet, KO_redet, Lexi) zusätzlich mit a/o/e: Augen der
Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_106")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

RI_F = {"Skin": "#EBC2A0", "Jacket": "#B8A9F5", "Top": "#FFFFFF", "Hair": "#BDBDC6"}
KO_F = {"Skin": "#E3AE88", "Pants": "#9A7B5B"}
# Person/Pose: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "RI": ("standing/blazer-4", "Gray Medium", None, "Glasses 3", RI_F),
    "KO": ("standing/crossed_arms-2", "Short 4", None, None, KO_F),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("RI_ruhig", "RI", "Calm", 0), ("RI_redet", "RI", "Serious", 1), ("RI_froh", "RI", "Smile Big|Smile", 0),
    ("RI_sorge", "RI", "Concerned|Serious", 0), ("RI_denkt", "RI", "Suspicious", 0), ("RI_staunt", "RI", "Awe", 0),
    ("KO_ruhig", "KO", "Calm", 0), ("KO_redet", "KO", "Serious", 1), ("KO_froh", "KO", "Smile Big|Smile", 0),
    ("KO_sorge", "KO", "Concerned|Serious", 0), ("KO_denkt", "KO", "Suspicious", 0),
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
