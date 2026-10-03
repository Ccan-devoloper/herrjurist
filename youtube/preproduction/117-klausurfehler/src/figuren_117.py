"""Figuren für Folge 117 (Klausurfehler, Rückgabe einer Übungsklausur) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv.
Ronja (Anfang 20, Jurastudentin): standing/shirt-4 (schwarze Bluse, Hose Rot #F07A6A, weiße Schuhe; nicht Grün wie Hartung in 114), Kopf Medium
Bangs 2 (blond), keine Brille. Stimme ela_froh. (robot_dance-3 verworfen: Geste fast wie Lexis robot_dance-1.)
Frau Brinkmann (um 55, Korrektorin): standing/pointing_finger-2 (zeigt mit dem Finger auf die Randbemerkung; schwarzes
Oberteil, Hose Blau #8DB3F2; nicht Lila wie die Wirtin in 115), Kopf Gray Medium (Haar #9A9A9A), Brille Glasses 2. Die Pose stand zuletzt in 112, nicht in
den letzten drei Folgen.
Spricht nicht (ihre Randbemerkungen liest die Erzählerin vor) und hat deshalb keine Mundzustände.
Keine Prothesen-Posen (blazer-1/-2, shirt-1/-2), keine Bärte, keine Polka Dots, keine Karikatur. Posen, Farben und Muster
nicht aus den Folgen 114–116 (crossed_arms-1, walking-2, blazer-4, shirt-3, crossed_legs, resting-2, blazer-3, easing-1,
robot_dance-2); shirt-4 zuletzt in 110.
Präfix RO_/BR_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links
(Figur rechts neben der Tafel), Suffix _r blickt nach rechts. Grundmimik immer mit geschlossenem Mund: Calm, Serious,
Smile, Suspicious, Fear, Tired bzw. „Augen|geschlossener Mund“ (Concerned|Serious, Smile Big|Smile). Sprechende Ansichten
(RO_redet, Lexi) zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_117")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person/Pose: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "RO": ("standing/shirt-4", "Medium Bangs 2", None, None, {"Skin": "#E8B98F", "Pants": "#F07A6A"}),
    "BR": ("standing/pointing_finger-2", "Gray Medium", None, "Glasses 2", {"Skin": "#F0CDB0", "Hair": "#9A9A9A", "Pants": "#8DB3F2"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("RO_ruhig", "RO", "Calm", 0), ("RO_froh", "RO", "Smile Big|Smile", 0), ("RO_redet", "RO", "Smile", 1),
    ("RO_sorge", "RO", "Concerned|Serious", 0), ("RO_denkt", "RO", "Suspicious", 0), ("RO_ertappt", "RO", "Fear", 0),
    ("RO_ernst", "RO", "Serious", 0),
    ("BR_ruhig", "BR", "Calm", 0), ("BR_ernst", "BR", "Serious", 0), ("BR_froh", "BR", "Smile", 0),
    ("BR_denkt", "BR", "Suspicious", 0),
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
