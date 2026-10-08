"""Figuren für Folge 252 (Anklageschrift § 200 StPO: Referendar schreibt die Anklage zum Schöffengericht) aus der
LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv.
Referendar Hiller (um 27, Station Staatsanwaltschaft; Stimme niklas): standing/pointing_finger-2 (schwarzer Pullover,
Hose Jeansblau #3D5A80), Kopf Short 4_2 (blond), Haut #F0C8A8, kein Bart.
Oberstaatsanwalt Endres (um 60, Ausbilder; Stimme helmut): standing/blazer-3 (Sakko Schiefergrau #4A5568 über schwarzem
Shirt, Hose #3D3D48), Kopf Gray Short, Glasses (1), Haut #EBC29E, kein Bart.
Herr Unger (41, Angeschuldigter, spricht nicht): standing/walking-2 (schwarzes Shirt, Hose Graublau #6B7A8F), Kopf Short 5
(Haar #6B4A32), Haut #E8B898, kein Bart – Alltagskleidung, ruhige Mimik, kein Klischee.
Frau Probst (um 65, Zeugin und Geschädigte, spricht nicht): standing/robot_dance-2 (schwarzes Oberteil, Hose Lila #B8A9F5),
Kopf Gray Bun, Haut #F2D0B4.
Sachlich, keine Karikatur, keine bösen Mimiken; keine Bärte, keine Polka Dots, keine Prothesen-Posen. Posen nicht aus den
letzten drei Folgen 249–251 (blazer-2, easing-1/-2, shirt-3/-4, resting-1/-2, crossed_arms-2, walking-1); Lexi bleibt
robot_dance-1. Präfix HI_/EN_/UN_/PR_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt
und blickt nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (HI_redet, EN_redet, Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_252")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "HI": ("standing/pointing_finger-2", "Short 4_2", None, None, {"Skin": "#F0C8A8", "Pants": "#3D5A80"}),
    "EN": ("standing/blazer-3", "Gray Short", None, "Glasses", {"Skin": "#EBC29E", "Jacket": "#4A5568", "Pants": "#3D3D48"}),
    "UN": ("standing/walking-2", "Short 5", None, None, {"Skin": "#E8B898", "Pants": "#6B7A8F", "Hair": "#6B4A32"}),
    "PR": ("standing/robot_dance-2", "Gray Bun", None, None, {"Skin": "#F2D0B4", "Pants": "#B8A9F5"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("HI_ruhig", "HI", "Calm", 0), ("HI_redet", "HI", "Concerned|Serious", 1), ("HI_denkt", "HI", "Suspicious", 0),
    ("HI_froh", "HI", "Smile", 0), ("HI_fest", "HI", "Driven", 0), ("HI_sorge", "HI", "Concerned|Serious", 0),
    ("HI_staunt", "HI", "Awe", 0),
    ("EN_ruhig", "EN", "Calm", 0), ("EN_redet", "EN", "Serious", 1), ("EN_ernst", "EN", "Serious", 0),
    ("EN_froh", "EN", "Smile", 0), ("EN_denkt", "EN", "Suspicious", 0), ("EN_still", "EN", "Solemn", 0),
    ("UN_ruhig", "UN", "Calm", 0), ("UN_still", "UN", "Solemn", 0), ("UN_ernst", "UN", "Serious", 0),
    ("PR_ruhig", "PR", "Calm", 0), ("PR_sorge", "PR", "Concerned|Serious", 0), ("PR_muede", "PR", "Tired", 0),
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
