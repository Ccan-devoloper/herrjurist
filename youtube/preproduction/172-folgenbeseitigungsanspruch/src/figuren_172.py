"""Figuren für Folge 172 (Folgenbeseitigungsanspruch, gepflasterter Vorgarten) aus der LexVerse-Figma-Bibliothek
(Open Peeps, CC0). Alle Figuren fiktiv.
Ottilie (um 60, Eigentümerin des Vorgartens): standing/shirt-3 (Hemdbluse Rot #F07A6A, Hose schwarz), Kopf Gray Bun
(graues Haar mit Dutt), ohne Brille, Haut #F0C8A8.
Herr Wernicke (um 45, Mitarbeiter des Bauamts der Gemeinde): standing/easing-2 (offene Jacke Türkis #7FD6D0, Hose Dunkelgrau
#4A4A58), Kopf Short 3, ohne Brille, ohne Bart, Haut #E3B08C. Sachlich, kein Bösewicht.
Bauarbeiter (ohne Namen, spricht nicht): standing/robot_dance-2 (Arbeitshose Orange #E8A03A), Mütze hat-beanie, Haut #EDC3A0;
ruhige Darstellung, keine Gewalt.
Keine Bärte, keine Karikatur, keine Polka Dots, keine Prothesen-Posen.
Posen und Farben nicht aus den Folgen 169–171 (doctor-nurse-02, shirt-4, robot_dance-3, blazer-1/-2/-3, easing-1,
pointing_finger-2) und nicht aus 168 (crossed_arms-1, blazer-4, pointing_finger-1).
Präfix OT_/WE_/BA_ (nie ER_, weil bausteine.peep_voll ER_* in den Ordner op_we umleitet). Alle Posen blicken im Original
nach rechts; die Grundansicht ist gespiegelt und blickt nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Smile, Suspicious, Awe bzw. „Augen|geschlossener
Mund“ (Smile Big|Smile, Concerned|Serious). Sprechende Ansichten (OT_redet, OT_bestimmt, WE_redet, Lexi) zusätzlich mit a/o/e:
Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_172")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

OT_F = {"Skin": "#F0C8A8", "Top": "#F07A6A"}
WE_F = {"Skin": "#E3B08C", "Jacket": "#7FD6D0", "Pants": "#4A4A58"}
BA_F = {"Skin": "#EDC3A0", "Pants": "#E8A03A"}
# Person/Pose: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "OT": ("standing/shirt-3", "Gray Bun", None, None, OT_F),
    "WE": ("standing/easing-2", "Short 3", None, None, WE_F),
    "BA": ("standing/robot_dance-2", "hat-beanie", None, None, BA_F),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("OT_ruhig", "OT", "Calm", 0), ("OT_redet", "OT", "Concerned|Serious", 1), ("OT_bestimmt", "OT", "Serious", 1),
    ("OT_sorge", "OT", "Concerned|Serious", 0), ("OT_staunt", "OT", "Awe", 0), ("OT_denkt", "OT", "Suspicious", 0),
    ("OT_froh", "OT", "Smile Big|Smile", 0), ("OT_ernst", "OT", "Serious", 0),
    ("WE_ruhig", "WE", "Calm", 0), ("WE_redet", "WE", "Smile", 1), ("WE_verlegen", "WE", "Concerned|Serious", 0),
    ("WE_denkt", "WE", "Suspicious", 0), ("WE_ernst", "WE", "Serious", 0), ("WE_froh", "WE", "Smile Big|Smile", 0),
    ("BA_ruhig", "BA", "Calm", 0), ("BA_froh", "BA", "Smile", 0), ("BA_sorge", "BA", "Concerned|Serious", 0),
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
