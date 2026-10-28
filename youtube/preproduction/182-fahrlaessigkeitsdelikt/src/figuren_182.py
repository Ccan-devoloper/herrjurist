"""Figuren für Folge 182 (Fahrlässigkeitsdelikt, Mietshaus mit morscher Balkonbrüstung) aus der LexVerse-Figma-Bibliothek
(Open Peeps, CC0). Alle Figuren fiktiv.
Herr Berger (BE, um 60, Eigentümer und Vermieter des Hauses; Stimme william): standing/blazer-3 (Sakko Orange #F9A66C,
Hose Dunkelgrau #3A3A44), Kopf Gray Short (Haar grau #A3A3A3), Brille Glasses 4, Haut #E9BE9A, kein Bart. Sachlich, keine
böse Mimik: Calm, Smile (sagt Reparatur zu), Suspicious (denkt), Serious, Solemn, Concerned|Serious.
Frau Specht (SP, um 40, Mieterin; Stimme laura_ruhig): standing/pointing_finger-2 (schwarzes Oberteil aus der Pose, Hose
Türkis #7FD6D0), Kopf Long Curly (schwarzes Haar), Haut #B97A56; zeigt auf die Brüstung. Mimiken Calm, Concerned|Serious
(redet, sorgt sich), Serious, Fear (Schreck).
Gast (GA, um 35, Funktionsrolle ohne Namen, spricht nicht): standing/resting-1 (Oberteil Blau #8DB3F2, schwarze Hose), Kopf Short 4
(schwarzes Haar), Haut #8D5A3B; Mimiken Calm, Smile (geschlossener Mund).
Keine Prothesen-Posen (blazer-1/-2, shirt-1/-2), keine Bärte, keine Polka Dots. Posen und Kleidung nicht aus den letzten
drei Folgen 179–181 (blazer-4, shirt-3, crossed_arms-2, easing-1, crossed_arms-1, resting-2, shirt-4, easing-2) und
nicht robot_dance-1/-3 (Lexi bzw. zu ähnlich).
Präfix BE_/SP_/GA_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach
links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (BE_redet, SP_redet, Lexi) zusätzlich mit
a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_182")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "BE": ("standing/blazer-3", "Gray Short", None, "Glasses 4", {"Skin": "#E9BE9A", "Jacket": "#F9A66C", "Pants": "#3A3A44",
                                                                "Hair": "#A3A3A3"}),
    "SP": ("standing/pointing_finger-2", "Long Curly", None, None, {"Skin": "#B97A56", "Pants": "#7FD6D0"}),
    "GA": ("standing/resting-1", "Short 4", None, None, {"Skin": "#8D5A3B", "Top": "#8DB3F2"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("BE_ruhig", "BE", "Calm", 0), ("BE_redet", "BE", "Smile", 1), ("BE_froh", "BE", "Smile", 0),
    ("BE_denkt", "BE", "Suspicious", 0), ("BE_ernst", "BE", "Serious", 0), ("BE_still", "BE", "Solemn", 0),
    ("BE_sorge", "BE", "Concerned|Serious", 0),
    ("SP_ruhig", "SP", "Calm", 0), ("SP_redet", "SP", "Concerned|Serious", 1), ("SP_sorge", "SP", "Concerned|Serious", 0),
    ("SP_ernst", "SP", "Serious", 0), ("SP_schreck", "SP", "Fear", 0), ("SP_froh", "SP", "Smile", 0),
    ("GA_ruhig", "GA", "Calm", 0), ("GA_froh", "GA", "Smile", 0),
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
