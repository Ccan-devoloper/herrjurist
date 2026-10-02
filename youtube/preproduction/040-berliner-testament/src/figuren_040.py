"""Figuren für Folge 040 (Berliner Testament) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
- Günter (GU, um 75, Ehemann, verstirbt im Fall): standing/shirt-4 (schwarzes Hemd, Hose Blau), Kopf No Hair 3 (graue
  Seiten), Brille Glasses. Stimme helmut (Mann, älter). Erscheint nur in Szenen, die zu seinen Lebzeiten spielen.
- Ingrid (IN, um 72, Ehefrau, Überlebende): standing/easing-1 (Jacke Grün, Oberteil Weiß), Kopf Gray Medium (Haar grau),
  Brille Glasses 4. Stimme hilde (Frau, älter).
- Petra (PE, um 45, Tochter): standing/shirt-3 (Hemd Rosa), Kopf Medium Bangs 2 (Haar braun). Stimme lisa (Frau, älter).
- Uwe (UW, um 42, Sohn, ohne Text): standing/resting-2 (Hose Grau), Kopf Short 2.
Je Person eine Pose (Outfit konstant), keine Prothesen-Posen, keine Bärte. Grundansicht gespiegelt (blickt nach links),
Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Smile, Serious, Suspicious, Tired, Driven, Solemn bzw.
„Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten (GU_redet, IN_redet, IN_entschl, PE_redet, Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_040")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "GU": ("standing/shirt-4", "No Hair 3", None, "Glasses", {"Skin": "#EBC1A0", "Pants": "#8DB3F2"}),
    "IN": ("standing/easing-1", "Gray Medium", None, "Glasses 4",
           {"Skin": "#F0C8A8", "Hair": "#DCD7D7", "Jacket": "#8FD694", "Top": "#FFFFFF"}),
    "PE": ("standing/shirt-3", "Medium Bangs 2", None, None, {"Skin": "#E2B08C", "Hair": "#7A4B2E", "Top": "#F6A5C0"}),
    "UW": ("standing/resting-2", "Short 2", None, None, {"Skin": "#E2B08C", "Pants": "#9C9CA6"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("GU_ruhig", "GU", "Calm", 0), ("GU_froh", "GU", "Smile", 0), ("GU_redet", "GU", "Smile", 1),
    ("GU_ernst", "GU", "Serious", 0),
    ("IN_ruhig", "IN", "Calm", 0), ("IN_froh", "IN", "Smile", 0), ("IN_redet", "IN", "Smile", 1),
    ("IN_entschl", "IN", "Driven", 1), ("IN_sorge", "IN", "Concerned|Serious", 0), ("IN_ernst", "IN", "Serious", 0),
    ("IN_denkt", "IN", "Suspicious", 0), ("IN_traurig", "IN", "Solemn", 0), ("IN_muede", "IN", "Tired", 0),
    ("PE_ruhig", "PE", "Calm", 0), ("PE_redet", "PE", "Driven", 1), ("PE_sorge", "PE", "Concerned|Serious", 0),
    ("PE_froh", "PE", "Smile", 0), ("PE_ernst", "PE", "Serious", 0),
    ("UW_ruhig", "UW", "Calm", 0), ("UW_froh", "UW", "Smile", 0), ("UW_denkt", "UW", "Suspicious", 0),
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
