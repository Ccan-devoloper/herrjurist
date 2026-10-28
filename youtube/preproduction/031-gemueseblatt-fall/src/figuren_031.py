"""Figuren für Folge 031 (Gemüseblatt-Fall, BGHZ 66, 51) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Echter Fall, Beteiligte nur als namenlose Funktionsfiguren (keine Porträts, keine Karikaturen, keine Namen):
- Mutter (MU, um 40, Kundin): standing/shirt-3 (Hemd Lila, schwarze Hose), Kopf Medium Bangs 2.
- Tochter (TO, 14, begleitet die Mutter, spricht nicht): standing/walking-3 (schwarzes Oberteil, schwarze Hose);
  nach dem Sturz am Boden sitting/mid-1 mit schwarz gefärbter Hose (gleiches Outfit), Kopf Long, kleiner skaliert.
- Betreiber des Ladens (BE, um 50, Beklagter): standing/pointing_finger-2 (schwarzes Oberteil, Hose Blau; eine Pose,
  crossed_arms-2 wegen anderer Statur verworfen), Kopf Short 3, Brille Glasses 2, kein Bart.
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links, Suffix _r nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Smile, Suspicious, Fear, Contempt, Tired bzw.
„Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten (MU_redet, BE_redet, Lexi) zusätzlich mit a/o/e:
Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_031")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

MU_F = {"Skin": "#E8BE9A", "Top": "#B8A9F5", "Hair": "#6B4226"}
TO_F = {"Skin": "#E8BE9A", "Pants": "#222222", "Hair": "#C98A3A"}
BE_F = {"Skin": "#D9A47A", "Pants": "#8DB3F2"}
# Person/Pose: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "MU": ("standing/shirt-3", "Medium Bangs 2", None, None, MU_F),
    "TO": ("standing/walking-3", "Long", None, None, TO_F),
    "TS": ("sitting/mid-1", "Long", None, None, TO_F),            # Tochter nach dem Sturz am Boden
    "BE": ("standing/pointing_finger-2", "Short 3", None, "Glasses 2", BE_F),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("MU_ruhig", "MU", "Calm", 0), ("MU_froh", "MU", "Smile", 0), ("MU_redet", "MU", "Concerned|Serious", 1),
    ("MU_sorge", "MU", "Concerned|Serious", 0), ("MU_schreck", "MU", "Fear", 0), ("MU_ernst", "MU", "Serious", 0),
    ("TO_ruhig", "TO", "Calm", 0), ("TO_froh", "TO", "Smile", 0), ("TO_ernst", "TO", "Serious", 0),
    ("TO_denkt", "TO", "Suspicious", 0), ("TO_zufrieden", "TO", "Smile Big|Smile", 0),
    ("TS_schreck", "TS", "Fear", 0), ("TS_schmerz", "TS", "Concerned|Serious", 0), ("TS_muede", "TS", "Tired", 0),
    ("BE_redet", "BE", "Contempt", 1), ("BE_ruhig", "BE", "Calm", 0), ("BE_ernst", "BE", "Serious", 0),
    ("BE_abwehr", "BE", "Contempt", 0), ("BE_denkt", "BE", "Suspicious", 0), ("BE_ertappt", "BE", "Concerned|Serious", 0),
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
