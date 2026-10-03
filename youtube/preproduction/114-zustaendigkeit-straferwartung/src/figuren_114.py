"""Figuren für Folge 114 (Straferwartung und Zuständigkeit, Terrassen-Anzahlungen) aus der LexVerse-Figma-Bibliothek
(Open Peeps, CC0). Alle Figuren fiktiv.
Herr Grote (um 70, Kunde, Geschädigter): standing/crossed_arms-1 (Pullover Lila #B8A9F5, schwarze Hose; verschränkte Arme
passen zum Warten), Kopf No Hair 3 (Glatze mit grauem Haarkranz), Brille Glasses 4, kein Bart.
Herr Hartung (34, angeblicher Terrassenbauer, Beschuldigter): standing/walking-2 (schwarzes T-Shirt, Arbeitshose Grün
#8FD694, Turnschuhe), Kopf Short 4, kein Bart (nichts über dem Mund). Kein Herkunfts- oder Hautfarben-Klischee bei der
Täterrolle, Alltagskleidung, keine „fiese“ Figur.
Staatsanwältin Eggert (um 40): standing/blazer-4 (blauer Blazer #8DB3F2, weißes Oberteil, schwarze Hose), Kopf Medium
Straight, keine Brille.
Keine Prothesen-Posen (blazer-1/-2, shirt-1/-2), keine Bärte, keine Polka Dots, keine Karikatur. Posen, Farben und Muster
nicht aus den Folgen 110–112 (shirt-4, easing-1, blazer-1, pointing_finger-2, walking-1).
Präfix GR_/HA_/EG_ (nie ER_, weil bausteine.peep_voll ER_* in den Ordner op_we umleitet). Alle Posen blicken im Original
nach rechts; die Grundansicht ist gespiegelt und blickt nach links (Figur rechts neben der Tafel), Suffix _r blickt nach
rechts. Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Smile, Suspicious, Tired, Driven, Solemn,
Fear bzw. „Augen|geschlossener Mund“ (Concerned|Serious, Cheeky|Smile, Smile Big|Smile). Sprechende Ansichten (GR_redet,
HA_redet, EG_redet, Lexi) zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic,
Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_114")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person/Pose: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "GR": ("standing/crossed_arms-1", "No Hair 3", None, "Glasses 4", {"Skin": "#F0CDB0", "Top": "#B8A9F5", "Hair": "#C4C4C4"}),
    "HA": ("standing/walking-2", "Short 4", None, None, {"Skin": "#E3B48E", "Pants": "#8FD694"}),
    "EG": ("standing/blazer-4", "Medium Straight", None, None, {"Skin": "#D9A47E", "Jacket": "#8DB3F2", "Top": "#FFFFFF"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("GR_ruhig", "GR", "Calm", 0), ("GR_froh", "GR", "Smile Big|Smile", 0), ("GR_redet", "GR", "Concerned|Serious", 1),
    ("GR_sorge", "GR", "Concerned|Serious", 0), ("GR_muede", "GR", "Tired", 0), ("GR_denkt", "GR", "Suspicious", 0),
    ("HA_ruhig", "HA", "Calm", 0), ("HA_redet", "HA", "Smile", 1), ("HA_cool", "HA", "Cheeky|Smile", 0),
    ("HA_denkt", "HA", "Suspicious", 0), ("HA_schreck", "HA", "Fear", 0), ("HA_ernst", "HA", "Serious", 0),
    ("EG_ruhig", "EG", "Calm", 0), ("EG_redet", "EG", "Serious", 1), ("EG_denkt", "EG", "Suspicious", 0),
    ("EG_froh", "EG", "Smile", 0), ("EG_ernst", "EG", "Solemn", 0),
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
