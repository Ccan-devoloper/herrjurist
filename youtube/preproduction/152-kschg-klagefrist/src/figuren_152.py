"""Figuren für Folge 152 (Kündigungsschutzgesetz und Klagefrist; Gärtnerei) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv.
Kornelia (KO, um 40, Gärtnerin seit acht Jahren, Arbeitnehmerin; Stimme laura_ruhig): standing/walking-1 (T-Shirt Grün
  #8FD694, schwarze Hose, weiße Schuhe), Kopf Medium Bangs (schwarzes Haar, Kopf ohne Haarfarbfläche), Haut #E8B48F, keine Brille.
Herr Steinmetz (ST, um 60, Inhaber der Gärtnerei, Arbeitgeber; Stimme william): standing/shirt-4 (schwarzes Hemd – die Pose hat keine
  Oberteilfläche –, Hose Dunkelblau #2E3550, weiße Schuhe), Kopf Gray Short, Brille Glasses 2, Haut #F0C8A8, kein Bart.
Posen der letzten drei Folgen (148: robot_dance-3, walking-3; 149: blazer-4, crossed_arms-2; 150: shirt-3, blazer-3) nicht
verwendet; keine Polka Dots, keine Prothesen-Posen (blazer-1/-2, shirt-1/-2), keine Bärte, keine Karikatur. Präfixe KO_/ST_
(nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links, Suffix _r blickt
nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Suspicious, Fear, Tired, Smile, Solemn bzw.
„Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten KO_redet, ST_redet (und Lexi) zusätzlich mit a/o/e:
Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_152")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "KO": ("standing/walking-1", "Medium Bangs", None, None, {"Skin": "#E8B48F", "Top": "#8FD694"}),
    "ST": ("standing/shirt-4", "Gray Short", None, "Glasses 2", {"Skin": "#F0C8A8", "Pants": "#2E3550"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("KO_ruhig", "KO", "Calm", 0), ("KO_froh", "KO", "Smile", 0), ("KO_schreck", "KO", "Fear", 0),
    ("KO_redet", "KO", "Concerned|Serious", 1), ("KO_ernst", "KO", "Serious", 0), ("KO_sorge", "KO", "Concerned|Serious", 0),
    ("KO_skeptisch", "KO", "Suspicious", 0), ("KO_muede", "KO", "Tired", 0), ("KO_still", "KO", "Solemn", 0),
    ("ST_ruhig", "ST", "Calm", 0), ("ST_redet", "ST", "Serious", 1), ("ST_ernst", "ST", "Serious", 0),
    ("ST_skeptisch", "ST", "Suspicious", 0), ("ST_still", "ST", "Solemn", 0), ("ST_froh", "ST", "Smile", 0),
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
