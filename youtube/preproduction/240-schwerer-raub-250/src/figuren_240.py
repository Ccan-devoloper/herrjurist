"""Figuren für Folge 240 (Schwerer Raub § 250 StGB, Spielzeugpistole und Labello-Fall) aus der LexVerse-Figma-Bibliothek
(Open Peeps, CC0). Personen fiktiv, ohne Klischees.
Wiltrud (WI, um 45, Bäckereiverkäuferin; spricht nicht): standing/easing-1 (offene Jacke Lila #B8A9F5, Oberteil Weiß #FFFFFF, schwarze Hose der Pose),
  Kopf Medium Straight (schwarzes Haar der Vorlage), Haut #F0C8A0, keine Brille, kein Bart.
Alois (AL, um 25, Täter; Stimme niklas): standing/walking-1 (Oberteil Blau #8DB3F2, schwarze Hose der Pose), Kopf Short 3,
  Haut #E3B58E, kein Bart, keine Maske, keine Kapuze – unauffälliger junger Mann, keine „fiese“ Täterfigur.
Ottfried (OT, um 60, Bäckermeister; Stimme helmut): standing/shirt-3 (Hemd Grün #8FD694, schwarze Hose der Pose),
  Kopf Gray Short, Brille Glasses 2, Haut #E7B995, kein Bart.
Posen der letzten Folgen (235: walking-3, blazer-4; 236: crossed_arms-2, blazer-3; 237: easing-2, blazer-3) nicht verwendet;
robot_dance-1 bleibt Lexi; keine Prothesen-Posen (blazer-1/-2, shirt-1/-2), keine Polka Dots, keine Bärte. Präfixe WI_/AL_/OT_
(nie ER_). Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (blickt nach links), Suffix _r nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Smile, Fear, Serious, Suspicious, Solemn, Awe, Tired bzw.
„Augen|geschlossener Mund“ (Concerned|Serious, Smile Big|Smile). Sprechende Ansichten AL_redet (Serious), OT_redet
(Awe) und Lexi zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_240")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "WI": ("standing/easing-1", "Medium Straight", None, None, {"Skin": "#F0C8A0", "Jacket": "#B8A9F5", "Top": "#FFFFFF"}),
    "AL": ("standing/walking-1", "Short 3", None, None, {"Skin": "#E3B58E", "Top": "#8DB3F2"}),
    "OT": ("standing/shirt-3", "Gray Short", None, "Glasses 2", {"Skin": "#E7B995", "Top": "#8FD694"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("WI_ruhig", "WI", "Calm", 0), ("WI_froh", "WI", "Smile", 0), ("WI_schreck", "WI", "Fear", 0),
    ("WI_sorge", "WI", "Concerned|Serious", 0), ("WI_ernst", "WI", "Serious", 0), ("WI_denkt", "WI", "Suspicious", 0),
    ("WI_staunt", "WI", "Awe", 0), ("WI_muede", "WI", "Tired", 0),
    ("AL_ruhig", "AL", "Calm", 0), ("AL_ernst", "AL", "Serious", 0), ("AL_denkt", "AL", "Suspicious", 0),
    ("AL_still", "AL", "Solemn", 0), ("AL_schreck", "AL", "Fear", 0), ("AL_sorge", "AL", "Concerned|Serious", 0),
    ("AL_redet", "AL", "Serious", 1),
    ("OT_ruhig", "OT", "Calm", 0), ("OT_froh", "OT", "Smile", 0), ("OT_staunt", "OT", "Awe", 0),
    ("OT_denkt", "OT", "Suspicious", 0), ("OT_sorge", "OT", "Concerned|Serious", 0), ("OT_ernst", "OT", "Serious", 0),
    ("OT_redet", "OT", "Awe", 1),
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
