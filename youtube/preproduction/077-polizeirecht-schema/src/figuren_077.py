"""Figuren für Folge 077 (Polizeirecht Schema, Platzverweis im Park) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle fiktiv. Vorgabe 02.10.2026: alle Menschen im Bild sind Open-Peeps-Figuren (auch die Freunde von Herrn Schröder).
Herr Schröder (um 30, feiert Geburtstag): standing/robot_dance-2 (schwarzes Shirt, grüne Hose), Kopf Short 2.
Frau Götz (um 30, Polizei): standing/shirt-4 (schwarzes Hemd, dunkelblaue Hose wie eine Uniform), Kopf Bun 2.
Frau Krämer (um 70, Anwohnerin): standing/crossed_arms-2 (schwarzes Oberteil, lila Hose), Kopf Gray Medium (grau), Brille.
Freundin (um 30) sitzend: sitting/closed_legs-1 (rosa Jacke), Kopf Long Curly; Freund (um 30) sitzend: sitting/hands_back-1
(schwarzes Shirt, hellblaue Hose), Kopf Short 5. Beide sprechen nicht (immer geschlossener Mund).
Keine Bärte, keine Prothesen-Posen. Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach
links, Suffix _r blickt nach rechts. Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Smile, Serious, Suspicious,
Calm, Tired bzw. „Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten (…_redet…, Lexi) zusätzlich mit a/o/e:
Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 % der Gesichtshöhe."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_077")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "SR": ("standing/robot_dance-2", "Short 2", None, None, {"Skin": "#E8B894", "Pants": "#8FD694", "Hair": "#5A3E2B"}),
    "GO": ("standing/shirt-4", "Bun 2", None, None, {"Skin": "#F0C8A8", "Pants": "#3D4A7A", "Hair": "#3B2A20"}),
    "KR": ("standing/crossed_arms-2", "Gray Medium", None, "Glasses 2", {"Skin": "#F2CDB0", "Pants": "#B8A9F5", "Hair": "#BDBDC6"}),
    "FA": ("sitting/closed_legs-1", "Long Curly", None, None, {"Skin": "#C68C66"}),
    "FB": ("sitting/hands_back-1", "Short 5", None, None, {"Skin": "#D9A07A", "Pants": "#8DB3F2"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("SR_froh", "SR", "Smile", 0), ("SR_redet", "SR", "Smile", 1), ("SR_fragt", "SR", "Suspicious", 1),
    ("SR_sorge", "SR", "Concerned|Serious", 0), ("SR_denkt", "SR", "Suspicious", 0), ("SR_muede", "SR", "Tired", 0),
    ("GO_ruhig", "GO", "Calm", 0), ("GO_redet", "GO", "Calm", 1), ("GO_ernst", "GO", "Serious", 0),
    ("GO_ernst_redet", "GO", "Serious", 1), ("GO_denkt", "GO", "Suspicious", 0),
    ("KR_muede", "KR", "Tired", 0), ("KR_sorge", "KR", "Concerned|Serious", 0), ("KR_redet", "KR", "Concerned|Serious", 1),
    ("FA_froh", "FA", "Smile", 0), ("FA_sorge", "FA", "Concerned|Serious", 0),
    ("FB_froh", "FB", "Smile", 0), ("FB_sorge", "FB", "Concerned|Serious", 0),
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
