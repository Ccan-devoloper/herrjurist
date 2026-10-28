"""Figuren für Folge 026 (Kausalität, Dorfkiosk und Scheune) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Egon (Kioskbesitzer, Mitte 60): standing/blazer-1, Kopf No Hair 2, Brille Glasses 2, Jacke Grün (Pose mit Unterschenkelprothese;
Egon ist kein Täter, die Beine stehen hinter der Theke bzw. sind im Bild unauffällig). Bodo (Käufer, Brandstifter, um 40):
standing/easing-2, Kopf Short 3, Jacke Rot, Hose dunkel. Maren (Landwirtin, um 30): standing/polka_dots, Kopf Medium Bangs 2,
Oberteil Blau, Hose Gelb. Silke (Abwandlungen 2 und 3, ohne Sprechrolle): standing/crossed_arms-2, Kopf Long Curly, Hose Lila.
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links, Suffix _r nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF): Calm, Smile, Serious, Suspicious, Driven, Fear, Tired bzw.
„Augen|geschlossener Mund“ (Concerned|Serious, Cheeky|Smile). Sprechende Ansichten zusätzlich mit a/o/e (Augen der Grundmimik +
Mund Explaining/Concerned Fear/Hectic, Schnitt bei 60 % der Gesichtshöhe)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_026")
os.makedirs(ZIEL, exist_ok=True)
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

EG_F = {"Skin": "#F0C8A8", "Jacket": "#8FD694", "Pants": "#5A5A6E"}
BO_F = {"Skin": "#D9A27A", "Jacket": "#F07A6A", "Pants": "#3B3B4F"}
MA_F = {"Skin": "#E8B894", "Top": "#8DB3F2", "Pants": "#F9D56E"}
SI_F = {"Skin": "#C68A62", "Pants": "#B8A9F5"}

# Ansicht: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "EG": ("standing/blazer-1", "No Hair 2", None, "Glasses 2", EG_F),
    "BO": ("standing/easing-2", "Short 3", None, None, BO_F),
    "MA": ("standing/polka_dots", "Medium Bangs 2", None, None, MA_F),
    "SI": ("standing/crossed_arms-2", "Long Curly", None, None, SI_F),
}

# (Name, Ansicht, Grundmimik, mit Mundzuständen)
LISTE = [
    ("EG_ruhig", "EG", "Calm", 0), ("EG_redet", "EG", "Smile", 1), ("EG_froh", "EG", "Smile", 0),
    ("EG_denkt", "EG", "Serious", 0), ("EG_sorge", "EG", "Concerned|Serious", 0),
    ("BO_ruhig", "BO", "Calm", 0), ("BO_redet", "BO", "Calm", 1), ("BO_frech", "BO", "Cheeky|Smile", 1),
    ("BO_schleicht", "BO", "Suspicious", 0), ("BO_zuendet", "BO", "Driven", 0), ("BO_schreck", "BO", "Fear", 0),
    ("BO_denkt", "BO", "Serious", 0), ("BO_ertappt", "BO", "Concerned|Serious", 0),
    ("MA_ruhig", "MA", "Calm", 0), ("MA_redet", "MA", "Fear", 1), ("MA_traurig", "MA", "Tired", 0),
    ("MA_denkt", "MA", "Serious", 0),
    ("SI_ruhig", "SI", "Calm", 0), ("SI_schleicht", "SI", "Suspicious", 0), ("SI_ertappt", "SI", "Concerned|Serious", 0),
]

if __name__ == "__main__":
    n = 0
    for name, v, mimik, mund in LISTE:
        pose, kopf, bart, brille, farben = P[v]
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
