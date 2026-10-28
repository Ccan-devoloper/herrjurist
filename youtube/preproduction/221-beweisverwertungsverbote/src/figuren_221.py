"""Figuren für Folge 221 (Beweisverwertungsverbote, System) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Fall 1 – Herr Kleinert (um 30, Beschuldigter, spricht nicht): sitting/mid-1, durchgehend sitzend (schwarzes Oberteil der
  Pose, Hose Salbei #A3B18A), Kopf Short 2, ohne Bart.
Fall 1 – Kommissar (um 55, Stimme christian): standing/pointing_finger-1 (erhobener Zeigefinger; Kleidung der Pose schwarz,
  Zivil), Kopf Gray Short, Brille Glasses 4.
Fall 2 – Herr Haferkamp (um 45, Beschuldigter, Stimme stephan): standing/resting-1 (Oberteil Terrakotta #D98C5F, Hose der
  Pose schwarz), Kopf Short 3, ohne Bart, ohne Prothese.
Fall 2 – Polizistin (um 30, Stimme lucy): standing/crossed_arms-2 (schwarzes Oberteil der Pose, Hose Dunkelblau #2F4A6D
  wie eine Uniform, ohne Abzeichen), Kopf Bangs 2.
Fall 2 – Verteidigerin (um 45, spricht nicht): standing/blazer-2 (Jacke Schwarz #2B2B2B wie eine Robe; die Pose zeigt eine
  Unterschenkelprothese – bei der Verteidigerin, nicht bei einer Täterrolle), Kopf Long, Brille Glasses 2.
Fall 3 – Frau Ruhnke (um 70, Beschuldigte, Stimme hilde): standing/polka_dots (Bluse mit Punkten), Kopf Gray Bun, Brille
  Glasses 3.
Fall 3 – Polizist (um 35, spricht nicht): standing/robot_dance-2 (schwarzes Oberteil, Hose Dunkelblau
  #2F4A6D wie die Polizistin, ohne Abzeichen), Kopf Short 1.
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links, _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Suspicious, Solemn, Smile, Tired, Fear bzw.
„Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten zusätzlich mit a/o/e: Augen der Grundmimik + Mund
Explaining / Concerned Fear / Hectic (Schnitt bei 60 % der Gesichtshöhe). Figurenpräfix nie ER_."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_221")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "KL": ("sitting/mid-1", "Short 2", None, None, {"Skin": "#EBC29E", "Pants": "#A3B18A"}),
    "KO": ("standing/pointing_finger-1", "Gray Short", None, "Glasses 4", {"Skin": "#C98E6A"}),
    "HA": ("standing/resting-1", "Short 3", None, None, {"Skin": "#F2D3B8", "Top": "#D98C5F"}),
    "PO": ("standing/crossed_arms-2", "Bangs 2", None, None, {"Skin": "#B07552", "Pants": "#2F4A6D"}),
    "VE": ("standing/blazer-2", "Long", None, "Glasses 2", {"Skin": "#8D5A3C", "Jacket": "#2B2B2B"}),
    "RU": ("standing/polka_dots", "Gray Bun", None, "Glasses 3", {"Skin": "#F2D3B8"}),
    "PZ": ("standing/robot_dance-2", "Short 1", None, None, {"Skin": "#E3B08C", "Pants": "#2F4A6D"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("KL_ruhig", "KL", "Calm", 0), ("KL_sorge", "KL", "Concerned|Serious", 0), ("KL_angst", "KL", "Fear", 0),
    ("KL_denkt", "KL", "Suspicious", 0), ("KL_muede", "KL", "Tired", 0), ("KL_froh", "KL", "Smile", 0),
    ("KO_ruhig", "KO", "Calm", 0), ("KO_redet", "KO", "Serious", 1), ("KO_ernst", "KO", "Serious", 0),
    ("KO_denkt", "KO", "Suspicious", 0), ("KO_betr", "KO", "Solemn", 0),
    ("HA_ruhig", "HA", "Calm", 0), ("HA_redet", "HA", "Serious", 1), ("HA_sorge", "HA", "Concerned|Serious", 0),
    ("HA_denkt", "HA", "Suspicious", 0), ("HA_muede", "HA", "Tired", 0), ("HA_froh", "HA", "Smile", 0),
    ("PO_ruhig", "PO", "Calm", 0), ("PO_redet", "PO", "Serious", 1), ("PO_ernst", "PO", "Serious", 0),
    ("PO_denkt", "PO", "Suspicious", 0), ("PO_froh", "PO", "Smile", 0),
    ("VE_ruhig", "VE", "Calm", 0), ("VE_ernst", "VE", "Serious", 0), ("VE_denkt", "VE", "Suspicious", 0),
    ("VE_froh", "VE", "Smile", 0),
    ("RU_ruhig", "RU", "Calm", 0), ("RU_redet", "RU", "Suspicious", 1), ("RU_sorge", "RU", "Concerned|Serious", 0),
    ("RU_denkt", "RU", "Suspicious", 0), ("RU_froh", "RU", "Smile", 0), ("RU_ernst", "RU", "Serious", 0),
    ("PZ_ruhig", "PZ", "Calm", 0), ("PZ_ernst", "PZ", "Serious", 0), ("PZ_denkt", "PZ", "Suspicious", 0),
    ("PZ_betr", "PZ", "Solemn", 0),
]

if __name__ == "__main__":
    os.makedirs(ZIEL, exist_ok=True)
    n = 0
    for name, p, mimik, mund in LISTE:
        pose, kopf, bart, brille, farben = P[p]
        for suffix, gespiegelt in (("", True), ("_r", False)):
            figur(pose, kopf, mimik, bart, brille, farben, hoehe=1200, spiegeln=gespiegelt).save(f"{ZIEL}/{name}{suffix}.png"); n += 1
            if mund:
                for k, m in MUND.items():
                    figur(pose, kopf, f"{mimik.split('|')[0]}|{m}", bart, brille, farben, hoehe=1200,
                          spiegeln=gespiegelt).save(f"{ZIEL}/{name}{suffix}_{k}.png"); n += 1
    # Lexi (feste Moderatorin, Stimme Carla), blickt nach links zur Tafel
    for name, (pose, mimik) in {"LX_erklaert": ("standing/robot_dance-1", "Smile"), "LX_warnt": ("standing/robot_dance-1", "Serious")}.items():
        a = LX.AUSSEHEN
        for k, g in {"": mimik, **{"_" + k: f"{mimik}|{m}" for k, m in MUND.items()}}.items():
            figur(pose, a["kopf"], g, a["bart"], a["brille"], a["farben"], hoehe=1200, spiegeln=True).save(f"{ZIEL}/{name}{k}.png"); n += 1
    print(n, "Figurenbilder ->", ZIEL)
