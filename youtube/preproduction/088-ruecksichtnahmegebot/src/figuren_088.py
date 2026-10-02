"""Figuren für Folge 088 (Rücksichtnahmegebot, Wohnblock neben dem Einfamilienhaus) aus der LexVerse-Figma-Bibliothek
(Open Peeps, CC0). Alle fiktiv.
Frau Kolbe (um 70, wohnt seit 40 Jahren in ihrem Einfamilienhaus, Klägerin): standing/easing-2 (lila Jacke, graue Hose),
Kopf Gray Medium (graues Haar), Brille Glasses 2.
Herr Reimers (um 45, Bauherr des Wohnblocks): standing/resting-1 (roter Pullover, schwarze Hose), Kopf Short 3.
Keine Bärte, keine Prothesen-Posen, keine Muster. Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt
und blickt nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Smile, Serious, Suspicious, Tired bzw. „Augen|geschlossener Mund“
(Concerned|Serious, Rage|Serious, Smile Big|Smile). Sprechende Ansichten (…_redet, …_protest, Lexi) zusätzlich mit a/o/e:
Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 % der Gesichtshöhe."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_088")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "KO": ("standing/easing-2", "Gray Medium", None, "Glasses 2",
           {"Skin": "#F2C9A8", "Hair": "#C8C8C8", "Jacket": "#B8A9F5", "Pants": "#6A6A76"}),
    "RE": ("standing/resting-1", "Short 3", None, None,
           {"Skin": "#E8B48E", "Hair": "#4A3428", "Top": "#F07A6A"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("KO_ruhig", "KO", "Smile", 0), ("KO_redet", "KO", "Smile", 1), ("KO_froh", "KO", "Smile Big|Smile", 0),
    ("KO_denkt", "KO", "Suspicious", 0), ("KO_sorge", "KO", "Concerned|Serious", 0),
    ("KO_protest", "KO", "Rage|Serious", 1), ("KO_muede", "KO", "Tired", 0),
    ("RE_ruhig", "RE", "Smile", 0), ("RE_redet", "RE", "Smile", 1), ("RE_denkt", "RE", "Suspicious", 0),
    ("RE_ernst", "RE", "Serious", 0),
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
