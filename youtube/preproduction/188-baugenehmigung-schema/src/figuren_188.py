"""Figuren für Folge 188 (Baugenehmigung Schema: Wiese vor dem Dorf, Bauaufsichtsbehörde) aus der LexVerse-Figma-Bibliothek
(Open Peeps, CC0). Alle Figuren fiktiv.
Herr Hasenkamp (HA, um 55, Bauherr, Oldtimer-Besitzer; Stimme christian): standing/pointing_finger-2 (schwarzer Pullover,
  Hose Beige #C9A66B), Kopf Short 3 (schwarzes Haar), Haut #E8B48E, keine Brille, kein Bart.
Frau Ortmann (OR, um 35, Sachbearbeiterin der Bauaufsichtsbehörde; Stimme lucy): standing/crossed_arms-1 (Oberteil Rosé
  #F2A7C3, schwarze Hose), Kopf Medium Bangs, Haut #F3CDB0, keine Brille.
Posen der letzten drei Folgen (184: sitting/mid-2, blazer-1; 185: resting-2, sitting/closed_legs-2, walking-1, walking-2,
crossed_arms-2, shirt-4; 186: easing-2, doctor-nurse-01, resting-1, blazer-3) nicht verwendet; Farben Schwarz/Beige und Rosé
(Orange, Türkis, Anthrazit aus 186, Grün/Lila/Blau aus 185 vermieden); keine Polka Dots, keine Prothesen-Posen, keine Bärte,
keine Karikatur. Präfixe HA_/OR_ (nie ER_).
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Suspicious, Tired, Smile, Solemn bzw.
„Augen|geschlossener Mund“ (Concerned|Serious, Smile Big|Smile). Sprechende Ansichten HA_redet, HA_redet2, OR_redet (und Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_188")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "HA": ("standing/pointing_finger-2", "Short 3", None, None, {"Skin": "#E8B48E", "Pants": "#C9A66B"}),
    "OR": ("standing/crossed_arms-1", "Medium Bangs", None, None, {"Skin": "#F3CDB0", "Top": "#F2A7C3"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("HA_ruhig", "HA", "Calm", 0), ("HA_froh", "HA", "Smile", 0), ("HA_stolz", "HA", "Smile Big|Smile", 0),
    ("HA_sorge", "HA", "Concerned|Serious", 0), ("HA_ernst", "HA", "Serious", 0), ("HA_muede", "HA", "Tired", 0),
    ("HA_skeptisch", "HA", "Suspicious", 0),
    ("HA_redet", "HA", "Smile Big|Smile", 1), ("HA_redet2", "HA", "Tired", 1),
    ("OR_ruhig", "OR", "Calm", 0), ("OR_ernst", "OR", "Serious", 0), ("OR_froh", "OR", "Smile", 0),
    ("OR_skeptisch", "OR", "Suspicious", 0), ("OR_denkt", "OR", "Solemn", 0),
    ("OR_redet", "OR", "Serious", 1),
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
