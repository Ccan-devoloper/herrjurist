"""Figuren für Folge 015 (Strafrecht AT Überblick, Gartenfest-Fall) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Otto (Gärtner, um 65, Geschädigter): standing/crossed_arms-1 (lila Oberteil, schwarze Hose), Kopf No Hair 2, Brille Glasses 3.
Konrad (Nachbar, um 45, Täter): standing/robot_dance-2 (schwarzes Oberteil, blaue Hose), Kopf Short 1.
Ina (Nachbarin, um 25, Gehilfin): standing/resting-2 (schwarzes Oberteil, rote Hose), Kopf Medium 2.
Rudolf (Gast, um 50, Versuch): standing/walking-2 (schwarzes Oberteil, gelbe Hose), Kopf Short 3 (ohne Bart, damit keine Schurkenkarikatur entsteht).
Bernd (Grillmeister, um 35, Fahrlässigkeit): standing/easing-2 (orange Jacke, graue Hose), Kopf Flat Top.
Gerda (Hundehalterin, um 70, Unterlassen): sitting/closed_legs-1 (grüne Jacke) auf der Gartenbank, Kopf Gray Bun, Glasses 2.
Keine Prothesen-Posen. Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links,
Suffix _r nach rechts. Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Smile, Serious, Driven, Fear,
Very Angry, Suspicious, Contempt bzw. „Augen|geschlossener Mund“ (Concerned|Serious, Cheeky|Smile).
Sprechende Ansichten (KO_redet, OT_redet, GE_redet, Lexi) zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining /
Concerned Fear / Hectic, Schnitt bei 60 % der Gesichtshöhe."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_015")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "OT": ("standing/crossed_arms-1", "No Hair 2", None, "Glasses 3", {"Skin": "#EBC4A0", "Top": "#B8A9F5"}),
    "KO": ("standing/robot_dance-2", "Short 1", None, None, {"Skin": "#E8B98F", "Pants": "#8DB3F2"}),
    "IN": ("standing/resting-2", "Medium 2", None, None, {"Skin": "#B07552", "Pants": "#F07A6A"}),
    "RU": ("standing/walking-2", "Short 3", None, None, {"Skin": "#F0C8A8", "Pants": "#F9D56E"}),
    "BE": ("standing/easing-2", "Flat Top", None, None, {"Skin": "#8D5A3B", "Jacket": "#F9A66C", "Pants": "#5A5A6A"}),
    "GE": ("sitting/closed_legs-1", "Gray Bun", None, "Glasses 2", {"Skin": "#E8B894", "Jacket": "#8FD694"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("OT_ruhig", "OT", "Calm", 0), ("OT_streng", "OT", "Suspicious", 0), ("OT_redet", "OT", "Concerned|Serious", 1),
    ("OT_schreck", "OT", "Fear", 0), ("OT_wuetend", "OT", "Very Angry", 0), ("OT_denkt", "OT", "Serious", 0),
    ("KO_ruhig", "KO", "Calm", 0), ("KO_redet", "KO", "Driven", 1), ("KO_wuetend", "KO", "Very Angry", 0),
    ("KO_zufrieden", "KO", "Smile", 0), ("KO_denkt", "KO", "Serious", 0), ("KO_ertappt", "KO", "Concerned|Serious", 0),
    ("IN_ruhig", "IN", "Calm", 0), ("IN_cool", "IN", "Cheeky|Smile", 0), ("IN_denkt", "IN", "Serious", 0),
    ("IN_ertappt", "IN", "Concerned|Serious", 0),
    ("RU_ruhig", "RU", "Calm", 0), ("RU_gierig", "RU", "Cheeky|Smile", 0), ("RU_zieht", "RU", "Driven", 0),
    ("RU_schreck", "RU", "Fear", 0), ("RU_ertappt", "RU", "Concerned|Serious", 0), ("RU_denkt", "RU", "Serious", 0),
    ("BE_ruhig", "BE", "Calm", 0), ("BE_froh", "BE", "Smile", 0), ("BE_schreck", "BE", "Fear", 0),
    ("BE_ertappt", "BE", "Concerned|Serious", 0), ("BE_denkt", "BE", "Serious", 0),
    ("GE_ruhig", "GE", "Calm", 0), ("GE_schaut", "GE", "Suspicious", 0), ("GE_redet", "GE", "Contempt", 1),
    ("GE_boese", "GE", "Contempt", 0), ("GE_denkt", "GE", "Serious", 0), ("GE_ertappt", "GE", "Concerned|Serious", 0),
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
