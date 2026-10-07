"""Figuren für Folge 239 (Sicherungsübereignung, §§ 929 S. 1, 930 BGB) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Personen fiktiv.
Sieglinde (SG, um 55, Malermeisterin mit eigenem Malerbetrieb, Kreditnehmerin/Sicherungsgeberin; Stimme hilde):
  standing/resting-2 (schwarzes Oberteil der Pose, weiße Malerhose #FFFFFF, schwarze Schuhe), Kopf Gray Medium (in der
  Bibliothek rotbraun), Haut #F0C8A8, kein Bart, keine Brille.
Herr Lohberg (LO, um 45, Bankberater der Bank, Sicherungsnehmerseite; Stimme christian): standing/shirt-4 (schwarzes Hemd
  der Pose, Hose Marine #2F3E66), Kopf Short 4, Brille Glasses 4, Haut #E0B08A, kein Bart. Kein Bösewicht: sachlich, freundlich.
Gerichtsvollzieherin (GV, um 40, spricht nicht; nur Szene Einzelvollstreckung): standing/easing-1 (Jacke Lila #B8A9F5,
  Oberteil Weiß), Kopf Bun 2, Haut #C68E6A.
Posen der letzten Folgen (234: crossed_arms-2, shirt-3, blazer-3, easing-2, resting-1; 235: walking-3, blazer-4;
236: crossed_arms-2, blazer-3; 237: easing-2, blazer-3) nicht verwendet; robot_dance-1 bleibt Lexi; Prothesen-Posen
(blazer-1, blazer-2, shirt-1/2) verworfen; keine Polka Dots, keine Bärte. Präfixe SG_/LO_/GV_ (nie ER_). Alle Posen blicken
im Original nach rechts; Grundansicht gespiegelt (blickt nach links), Suffix _r nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Smile, Awe, Fear, Serious, Suspicious, Solemn, Tired bzw.
„Augen|geschlossener Mund“ (Concerned|Serious, Smile Big|Smile). Sprechende Ansichten SG_redet (Concerned|Serious),
LO_redet (Smile), LO_erklaert (Calm) und Lexi zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining /
Concerned Fear / Hectic."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_239")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "SG": ("standing/resting-2", "Gray Medium", None, None, {"Skin": "#F0C8A8", "Pants": "#FFFFFF"}),
    "LO": ("standing/shirt-4", "Short 4", None, "Glasses 4", {"Skin": "#E0B08A", "Pants": "#2F3E66"}),
    "GV": ("standing/easing-1", "Bun 2", None, None, {"Skin": "#C68E6A", "Jacket": "#B8A9F5", "Top": "#FFFFFF"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("SG_ruhig", "SG", "Calm", 0), ("SG_froh", "SG", "Smile", 0), ("SG_freut", "SG", "Smile Big|Smile", 0),
    ("SG_sorge", "SG", "Concerned|Serious", 0), ("SG_schreck", "SG", "Fear", 0), ("SG_ernst", "SG", "Serious", 0),
    ("SG_denkt", "SG", "Suspicious", 0), ("SG_staunt", "SG", "Awe", 0), ("SG_muede", "SG", "Tired", 0),
    ("SG_redet", "SG", "Concerned|Serious", 1),
    ("LO_ruhig", "LO", "Calm", 0), ("LO_froh", "LO", "Smile", 0), ("LO_denkt", "LO", "Suspicious", 0),
    ("LO_ernst", "LO", "Serious", 0), ("LO_sorge", "LO", "Concerned|Serious", 0), ("LO_still", "LO", "Solemn", 0),
    ("LO_staunt", "LO", "Awe", 0),
    ("LO_redet", "LO", "Smile", 1), ("LO_erklaert", "LO", "Calm", 1),
    ("GV_ernst", "GV", "Serious", 0), ("GV_ruhig", "GV", "Calm", 0),
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
