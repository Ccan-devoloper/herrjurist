"""Figuren für Folge 218 (Nichtanzeige geplanter Straftaten, Chat am Donnerstagabend) aus der LexVerse-Figma-Bibliothek
(Open Peeps, CC0). Alle Figuren fiktiv, keine realen Personen.
Sören (SO, um 30, Stimme niklas): stehend standing/pointing_finger-2, sitzend sitting/one_leg_up-1 (je schwarzes Oberteil,
Hose Blau #8DB3F2 – gleiches Outfit), Kopf Short 4, Haut #D9A07A.
Mirko (MI, um 30, spricht nicht, nur Chat-Text): standing/shirt-4 (schwarzes Hemd, Hose Orange #F9A66C), Kopf Short 3,
Haut #F2C6A0. Sachlich, keine Gangster-Klischees: Alltagskleidung, ruhige Mimiken (Calm, Serious, Solemn, Smile).
Keine Prothesen-Posen (blazer-1/-2, shirt-1/-2), keine Bärte, keine Polka Dots. Posen nicht aus den letzten Folgen
213–216 (robot_dance-3, easing-1, walking-2, shirt-1, easing-2, walking-1, walking-3, robot_dance-2, resting-1,
crossed_arms-2, shirt-3, crossed_arms-1, blazer-3, blazer-4) und nicht robot_dance-1 (Lexi). Präfix SO_/MI_ (nie ER_).
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links, Suffix _r blickt nach
rechts. Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (SO_sitzt_redet, SO_redet, Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_218")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "SO": ("standing/pointing_finger-2", "Short 4", None, None, {"Skin": "#D9A07A", "Pants": "#8DB3F2"}),
    "SS": ("sitting/one_leg_up-1", "Short 4", None, None, {"Skin": "#D9A07A", "Pants": "#8DB3F2"}),
    "MI": ("standing/shirt-4", "Short 3", None, None, {"Skin": "#F2C6A0", "Pants": "#F9A66C"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("SO_sitzt", "SS", "Calm", 0), ("SO_liest", "SS", "Concerned|Serious", 0), ("SO_sitzt_denkt", "SS", "Suspicious", 0),
    ("SO_sitzt_redet", "SS", "Serious", 1), ("SO_sitzt_still", "SS", "Solemn", 0),
    ("SO_ruhig", "SO", "Calm", 0), ("SO_ernst", "SO", "Serious", 0), ("SO_redet", "SO", "Serious", 1),
    ("SO_still", "SO", "Solemn", 0), ("SO_denkt", "SO", "Suspicious", 0), ("SO_froh", "SO", "Smile", 0),
    ("MI_ruhig", "MI", "Calm", 0), ("MI_ernst", "MI", "Serious", 0), ("MI_still", "MI", "Solemn", 0),
    ("MI_froh", "MI", "Smile", 0),
]

if __name__ == "__main__":
    os.makedirs(ZIEL, exist_ok=True)
    n = 0
    for name, p, mimik, mund in LISTE:
        pose, kopf, bart, brille, farben = P[p]
        for suffix, gespiegelt in (("", 1), ("_r", 0)):
            mach = lambda g: figur(pose, kopf, g, bart, brille, farben, hoehe=1200, spiegeln=bool(gespiegelt))
            mach(mimik).save(f"{ZIEL}/{name}{suffix}.png"); n += 1
            if mund:
                for k, m in MUND.items():
                    mach(f"{mimik.split('|')[0]}|{m}").save(f"{ZIEL}/{name}{suffix}_{k}.png"); n += 1
    # Lexi (feste Moderatorin, Stimme Carla), blickt nach links zur Tafel
    for name, (pose, mimik) in {"LX_erklaert": ("standing/robot_dance-1", "Smile"), "LX_warnt": ("standing/robot_dance-1", "Serious")}.items():
        a = LX.AUSSEHEN
        for k, g in {"": mimik, **{"_" + k: f"{mimik}|{m}" for k, m in MUND.items()}}.items():
            figur(pose, a["kopf"], g, a["bart"], a["brille"], a["farben"], hoehe=1200, spiegeln=True).save(f"{ZIEL}/{name}{k}.png"); n += 1
    print(n, "Figurenbilder ->", ZIEL)
