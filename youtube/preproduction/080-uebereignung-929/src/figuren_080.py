"""Figuren für Folge 080 (§ 929 S. 1 BGB: Übereignung des Fahrrads) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv.
Annika (um 25, verkauft ihr Fahrrad): Reihe „-2“ (schwarzes Oberteil, farbige Hose, hier Blau): standing/robot_dance-2
(offene Hand: ruhig, redet, froh, reicht das Rad), standing/crossed_arms-2 (denkt, Sorge); Kopf Medium Straight.
Herr Brunner (um 45, kauft das Rad): standing/shirt-4 (schwarzes Hemd, Hose Grau), Kopf Short 2, Glasses 2;
sitting/bike (fährt morgen mit dem gekauften Rad davon; Jacke schwarz wie das Hemd, Rahmen Rot wie das Rad-Symbol).
Keine Bärte, keine Prothesen-Posen. Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt
nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Smile, Suspicious bzw. „Augen|geschlossener
Mund“ (Smile Big|Smile, Concerned|Serious). Sprechende Ansichten (AN_redet, BR_redet, Lexi) zusätzlich mit a/o/e:
Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_080")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

AN_F = {"Skin": "#F0C8A8", "Pants": "#8DB3F2", "Shoes": "#FFFFFF"}
BR_F = {"Skin": "#B98055", "Pants": "#9C9CA6"}
# Person/Pose: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "AN": ("standing/robot_dance-2", "Medium Straight", None, None, AN_F),
    "AN_A": ("standing/crossed_arms-2", "Medium Straight", None, None, AN_F),
    "BR": ("standing/shirt-4", "Short 2", None, "Glasses 2", BR_F),
    "BR_B": ("sitting/bike", "Short 2", None, "Glasses 2",
             {"Skin": "#B98055", "Jacket": "#151515", "Top": "#151515", "Bicycle Frame": "#F07A6A"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("AN_ruhig", "AN", "Calm", 0), ("AN_redet", "AN", "Smile", 1), ("AN_froh", "AN", "Smile Big|Smile", 0),
    ("AN_denkt", "AN_A", "Suspicious", 0), ("AN_sorge", "AN_A", "Concerned|Serious", 0),
    ("BR_ruhig", "BR", "Calm", 0), ("BR_redet", "BR", "Smile", 1), ("BR_froh", "BR", "Smile Big|Smile", 0),
    ("BR_denkt", "BR", "Suspicious", 0), ("BR_ernst", "BR", "Serious", 0),
    ("BR_rad", "BR_B", "Smile Big|Smile", 0),
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
