"""Figuren für Folge 133 (Bürgschaft Schema §§ 765 ff. BGB) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv.
Marlies (um 45, Bürgin, Schwester von Hilke): standing/resting-1 (lila Pullover, schwarze Hose), Kopf Medium 1.
Hilke (um 40, Kreditnehmerin, Hauptschuldnerin): standing/easing-1 (rote Jacke über gelbem Shirt, schwarze Hose),
Kopf Long Curly.
Herr Seibold (um 58, Mitarbeiter der Bank, Gläubigerseite): standing/blazer-2 (dunkelblauer Blazer, weißes Shirt,
Beinprothese), Kopf Short 2 (graues Haar), Brille Glasses 2.
Keine Bärte, keine Karikatur, keine Klischees; die Bank bleibt sachlich. Posen nicht aus den Folgen 130–132
(robot_dance-2/-3, blazer-3/-4, crossed_arms-1, shirt-1/-2/-3, easing-2, walking-3) und nicht wie 099 (shirt-4,
walking-3, blazer-1); keine Polka Dots. Präfix MA_/HI_/SE_ (nie ER_). Grundansicht gespiegelt (blickt nach links),
Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md); sprechende Ansichten (…_redet, …_redetfroh) und Lexi
zusätzlich mit a/o/e (Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_133")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

MA_F = {"Skin": "#F2C9A5", "Top": "#B8A9F5"}
HI_F = {"Skin": "#EDBF9A", "Jacket": "#F07A6A", "Top": "#F9D56E"}
SE_F = {"Skin": "#E3B48E", "Jacket": "#3D4A7A", "Top": "#FFFFFF", "Hair": "#9A9AA5"}
# Person/Pose: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "MA": ("standing/resting-1", "Medium 1", None, None, MA_F),
    "HI": ("standing/easing-1", "Long Curly", None, None, HI_F),
    "SE": ("standing/blazer-2", "Short 2", None, "Glasses 2", SE_F),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("MA_ruhig", "MA", "Calm", 0), ("MA_redet", "MA", "Serious", 1), ("MA_redetfroh", "MA", "Smile", 1),
    ("MA_froh", "MA", "Smile Big|Smile", 0), ("MA_sorge", "MA", "Concerned|Serious", 0), ("MA_denkt", "MA", "Suspicious", 0),
    ("MA_schreck", "MA", "Fear", 0),
    ("HI_ruhig", "HI", "Calm", 0), ("HI_redet", "HI", "Calm", 1), ("HI_froh", "HI", "Smile Big|Smile", 0),
    ("HI_sorge", "HI", "Concerned|Serious", 0), ("HI_muede", "HI", "Tired", 0),
    ("SE_ruhig", "SE", "Calm", 0), ("SE_redet", "SE", "Serious", 1), ("SE_froh", "SE", "Smile", 0),
    ("SE_denkt", "SE", "Suspicious", 0),
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
