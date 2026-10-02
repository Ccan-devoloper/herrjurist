"""Figuren für Folge 081 (Zulässigkeit und Begründetheit) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle fiktiv.
Tabea (Anfang 20, Studentin, Halterin des Autos): standing/polka_dots (gepunktetes Oberteil, Hose Lila), Kopf Medium Straight.
Lennart (Anfang 20, Mitbewohner, Jurastudent): standing/pointing_finger-1 (erhobener Zeigefinger, Pullover Grün), Kopf Short 2.
Keine Bärte, keine Prothesen-Posen. Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt
nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Smile, Serious, Suspicious, Calm, Driven, Tired bzw.
„Augen|geschlossener Mund“ (Concerned|Serious, Rage|Serious). Sprechende Ansichten (…_redet, …_fragt, …_einsicht, Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 % der Gesichtshöhe."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_081")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "TA": ("standing/polka_dots", "Medium Straight", None, None, {"Skin": "#F1C6A5", "Pants": "#B8A9F5"}),
    "LE": ("standing/pointing_finger-1", "Short 2", None, None, {"Skin": "#E0A979", "Top": "#8FD694"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("TA_ruhig", "TA", "Smile", 0), ("TA_liest", "TA", "Serious", 0), ("TA_aerger", "TA", "Rage|Serious", 0),
    ("TA_redet", "TA", "Rage|Serious", 1), ("TA_fragt", "TA", "Concerned|Serious", 1), ("TA_denkt", "TA", "Suspicious", 0),
    ("TA_sorge", "TA", "Concerned|Serious", 0),
    ("LE_ruhig", "LE", "Calm", 0), ("LE_redet", "LE", "Driven", 1), ("LE_denkt", "LE", "Suspicious", 0),
    ("LE_einsicht", "LE", "Smile", 1),
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
