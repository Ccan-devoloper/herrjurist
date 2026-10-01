"""Figuren für Folge 027 (Besitz und Eigentum) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv.
Anke (um 28, Eigentümerin des Rades): Reihe „-1“ (farbiges Oberteil Grün, schwarze Hose): standing/resting-1 (ruhig, redet),
crossed_arms-1 (trotzig/ärgerlich), walking-1 (geht, nimmt das Rad); Kopf Medium Straight.
Jürgen (um 25, Mitbewohner, Entleiher, Aushilfe im Fahrradladen): standing/robot_dance-3 (offene Hand), Kopf Short 4,
Oberteil Blau, Hose Gelb (eine Pose, Outfit konstant).
Frau Kunze (um 60, Inhaberin des Fahrradladens): standing/blazer-3 (Blazer Orange, Hose Blau), Kopf Gray Short, Glasses 2.
Ein Unbekannter (Dieb, ohne Text): standing/walking-2 (Hose Grau), Mütze hat-beanie.
Keine Bärte, keine Prothesen-Posen. Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt
nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Smile, Suspicious, Fear, Contempt bzw.
„Augen|geschlossener Mund“ (Smile Big|Smile). Sprechende Ansichten (AN_redet, AN_trotzig, JU_redet, JU_ruft, KU_redet, Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_027")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

AN_F = {"Skin": "#E8B98F", "Top": "#8FD694", "Hair": "#7A4B2E"}
# Person/Pose: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "AN": ("standing/resting-1", "Medium Straight", None, None, AN_F),
    "AN_A": ("standing/crossed_arms-1", "Medium Straight", None, None, AN_F),
    "AN_W": ("standing/walking-1", "Medium Straight", None, None, AN_F),
    "JU": ("standing/robot_dance-3", "Short 4", None, None, {"Skin": "#C99470", "Top": "#8DB3F2", "Pants": "#F9D56E"}),
    "KU": ("standing/blazer-3", "Gray Short", None, "Glasses 2", {"Skin": "#F0C8A8", "Jacket": "#F9A66C", "Pants": "#8DB3F2"}),
    "DI": ("standing/walking-2", "hat-beanie", None, None, {"Skin": "#D9A07A", "Pants": "#9C9CA6"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("AN_ruhig", "AN", "Calm", 0), ("AN_redet", "AN", "Smile", 1), ("AN_froh", "AN", "Smile", 0),
    ("AN_trotzig", "AN_A", "Contempt", 1), ("AN_aerger", "AN_A", "Contempt", 0), ("AN_denkt", "AN_A", "Suspicious", 0),
    ("AN_zufrieden", "AN_A", "Smile", 0), ("AN_geht", "AN_W", "Serious", 0),
    ("JU_ruhig", "JU", "Calm", 0), ("JU_redet", "JU", "Smile", 1), ("JU_ruft", "JU", "Serious", 1),
    ("JU_froh", "JU", "Smile Big|Smile", 0), ("JU_schreck", "JU", "Fear", 0), ("JU_ernst", "JU", "Serious", 0),
    ("JU_denkt", "JU", "Suspicious", 0), ("JU_aerger", "JU", "Contempt", 0),
    ("KU_ruhig", "KU", "Calm", 0), ("KU_redet", "KU", "Smile", 1), ("KU_froh", "KU", "Smile", 0),
    ("DI_geht", "DI", "Suspicious", 0), ("DI_ertappt", "DI", "Fear", 0),
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
