"""Figuren für Folge 237 (Probeklausuren auswerten: Sprechstunde im Büro des Mentors) aus der LexVerse-Figma-Bibliothek
(Open Peeps, CC0). Alle Figuren fiktiv.
Friedrich (FR, Mitte 20, Jurastudent in NRW, sieben Monate vor den Examensklausuren; Stimme niklas): standing/easing-2
  (offenes Hemd Grün #8FD694 über schwarzem Shirt, Jeans #4A5A7A, weiße Turnschuhe, Hände locker), Kopf Short 4 (schwarzes
  Haar), Haut #EAC09A, keine Brille, kein Bart.
Herr Seebach (SB, um 60, Mentor an der Uni; Stimme helmut): standing/blazer-3 (Sakko Braun #9C6B4E über schwarzem Shirt,
  Hose #4A4A55, Hand an der Hüfte), Kopf No Hair 3 (Glatze mit grauem Haarkranz #BDBDC4), Brille „Glasses 3“, Haut #E8B896, kein Bart.
Posen der letzten Folgen nicht verwendet (230: pointing_finger-2, shirt-3, shirt-4; 231: walking-2, robot_dance-3;
232: resting-1, easing-1, crossed_arms-1; 233: easing-1, blazer-4, pointing_finger-1, sitting/bike, resting-2;
235: walking-3, blazer-4); 234 und 236 entstehen parallel. robot_dance-1 bleibt Lexi; keine Polka Dots, keine
Prothesen-Posen (blazer-1/-2, shirt-1/-2), keine Bärte, keine Karikatur. Präfixe FR_/SB_ (nie ER_).
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Smile, Suspicious, Serious, Driven, Awe, Tired bzw.
„Augen|geschlossener Mund“ (Smile Big|Smile, Concerned|Serious). Sprechende Ansichten FR_redet, FR_redet2, FR_redetfroh,
SB_redet, SB_redet2, SB_redetfroh (und Lexi) zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear /
Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_237")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "FR": ("standing/easing-2", "Short 4", None, None, {"Skin": "#EAC09A", "Jacket": "#8FD694", "Pants": "#4A5A7A"}),
    "SB": ("standing/blazer-3", "No Hair 3", None, "Glasses 3", {"Skin": "#E8B896", "Jacket": "#9C6B4E", "Pants": "#4A4A55",
                                                                  "Hair": "#BDBDC4"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("FR_ruhig", "FR", "Calm", 0), ("FR_ratlos", "FR", "Concerned|Serious", 0), ("FR_denkt", "FR", "Suspicious", 0),
    ("FR_muede", "FR", "Tired", 0), ("FR_froh", "FR", "Smile", 0), ("FR_stolz", "FR", "Smile Big|Smile", 0),
    ("FR_entschlossen", "FR", "Driven", 0), ("FR_staunt", "FR", "Awe", 0),
    ("FR_redet", "FR", "Concerned|Serious", 1), ("FR_redet2", "FR", "Awe", 1), ("FR_redetfroh", "FR", "Smile", 1),
    ("SB_ruhig", "SB", "Calm", 0), ("SB_froh", "SB", "Smile", 0), ("SB_ernst", "SB", "Serious", 0),
    ("SB_denkt", "SB", "Suspicious", 0),
    ("SB_redet", "SB", "Calm", 1), ("SB_redet2", "SB", "Serious", 1), ("SB_redetfroh", "SB", "Smile", 1),
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
