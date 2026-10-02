"""Figuren für Folge 086 (AGB-Kontrolle, §§ 305 ff. BGB) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv.
Mira (um 28, Verbraucherin, bucht online ein Kurs-Abo): standing/walking-1 (rosa T-Shirt, schwarze Hose, weiße Turnschuhe),
Kopf Medium Straight, keine Brille.
Rolf (um 50, betreibt das Fitnessstudio, Unternehmer): standing/crossed_arms-1 (blaues Langarmshirt, schwarze Hose,
verschränkte Arme), Kopf Short 2. Keine Prothesen-Pose, keine Bärte, keine Karikatur.
Posen, Farben und Köpfe nicht aus den Folgen 083–085 (easing-1, resting-1/-2, blazer-3/-4, robot_dance-3, sitting/bike).
Präfix MI_/RO_ (nie ER_, weil bausteine.peep_voll ER_* in den Ordner op_we umleitet). Alle Posen blicken im Original nach
rechts; die Grundansicht ist gespiegelt und blickt nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Suspicious, Awe bzw. „Augen|geschlossener Mund“
(Smile Big|Smile, Concerned|Serious). Sprechende Ansichten (MI_redet, RO_redet, Lexi) zusätzlich mit a/o/e: Augen der
Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_086")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

MI_F = {"Skin": "#C99272", "Top": "#F6A5C0"}
RO_F = {"Skin": "#F2C7A8", "Top": "#8DB3F2"}
# Person/Pose: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "MI": ("standing/walking-1", "Medium Straight", None, None, MI_F),
    "RO": ("standing/crossed_arms-1", "Short 2", None, None, RO_F),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("MI_ruhig", "MI", "Calm", 0), ("MI_redet", "MI", "Serious", 1), ("MI_froh", "MI", "Smile Big|Smile", 0),
    ("MI_sorge", "MI", "Concerned|Serious", 0), ("MI_denkt", "MI", "Suspicious", 0), ("MI_staunt", "MI", "Awe", 0),
    ("RO_ruhig", "RO", "Calm", 0), ("RO_redet", "RO", "Serious", 1), ("RO_froh", "RO", "Smile Big|Smile", 0),
    ("RO_sorge", "RO", "Concerned|Serious", 0), ("RO_denkt", "RO", "Suspicious", 0),
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
