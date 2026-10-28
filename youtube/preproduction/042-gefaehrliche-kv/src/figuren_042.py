"""Figuren für Folge 042 (Gefährliche Körperverletzung § 224, Dorffest) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Reinhard (Mitte 50): standing/pointing_finger-2 (schwarze Stiefel der Originalpose = „schwerer Arbeitsstiefel“), Kopf
    „No Hair 3“ (Glatze mit grauem Haarkranz), schwarzes Oberteil der Pose, Hose Grün.
Tobias (Mitte 20): standing/walking-2 (tanzt, geht) und – nach dem Stoß am Boden – sitting/hands_back-1; beide Posen
    mit schwarzem T-Shirt der Pose und blauer Hose, damit das Outfit gleich bleibt (TO_ = steht, TOS_ = sitzt am Boden).
Anja (Ende 20, Reinhards Tochter): standing/easing-2, Kopf „Medium Bangs 2“, Jacke Lila, Hose dunkel.
Je Person ein Outfit. Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links,
Suffix _r nach rechts. Keine Bärte, keine Prothesen-Posen.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF): Calm, Smile, Serious, Suspicious, Driven, Contempt, Fear, Awe,
Eyes Closed, Very Angry bzw. „Augen|geschlossener Mund“ (Concerned|Serious, Rage|Serious). Sprechende Ansichten zusätzlich
mit a/o/e (Augen der Grundmimik + Mund Explaining/Concerned Fear/Hectic, Schnitt bei 60 % der Gesichtshöhe)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_042")
os.makedirs(ZIEL, exist_ok=True)
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

RE_F = {"Skin": "#E8B894", "Pants": "#8FD694", "Hair": "#BDBDC6"}    # graues Haar (Mitte 50)
TO_F = {"Skin": "#D9A27A", "Pants": "#8DB3F2"}
AN_F = {"Skin": "#F0C8A8", "Jacket": "#B8A9F5", "Pants": "#4A4A5E"}

# Ansicht: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "RE": ("standing/pointing_finger-2", "No Hair 3", None, None, RE_F),
    "TO": ("standing/walking-2", "Short 1", None, None, TO_F),
    "TOS": ("sitting/hands_back-1", "Short 1", None, None, TO_F),
    "AN": ("standing/easing-2", "Medium Bangs 2", None, None, AN_F),
}

# (Name, Ansicht, Grundmimik, mit Mundzuständen)
LISTE = [
    ("RE_ruhig", "RE", "Calm", 0), ("RE_wuetend", "RE", "Very Angry", 0), ("RE_redet", "RE", "Rage|Serious", 1),
    ("RE_laechelt", "RE", "Smile", 1), ("RE_entschlossen", "RE", "Driven", 0), ("RE_denkt", "RE", "Serious", 0),
    ("RE_veraechtlich", "RE", "Contempt", 0), ("RE_ertappt", "RE", "Fear", 0), ("RE_listig", "RE", "Suspicious", 0),
    ("TO_ruhig", "TO", "Calm", 0), ("TO_froh", "TO", "Smile", 0), ("TO_erschrickt", "TO", "Fear", 0),
    ("TO_aua", "TO", "Concerned|Serious", 0), ("TO_denkt", "TO", "Serious", 0), ("TO_skeptisch", "TO", "Suspicious", 0),
    ("TO_staunt", "TO", "Awe", 0),
    ("TOS_erschrickt", "TOS", "Fear", 0), ("TOS_redet", "TOS", "Concerned|Serious", 1), ("TOS_schlaeft", "TOS", "Eyes Closed", 0),
    ("TOS_ruhig", "TOS", "Calm", 0), ("TOS_staunt", "TOS", "Awe", 0),
    ("AN_ruhig", "AN", "Calm", 0), ("AN_redet", "AN", "Driven", 1), ("AN_streng", "AN", "Driven", 0), ("AN_denkt", "AN", "Serious", 0),
]

if __name__ == "__main__":
    n = 0
    for name, v, mimik, mund in LISTE:
        pose, kopf, bart, brille, farben = P[v]
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
