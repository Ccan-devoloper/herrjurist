"""Figuren für Folge 098 (Gesetzgebungskompetenz) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle fiktiv.
Die Landesministerin (um 45, ohne Namen, Funktionsrolle): standing/blazer-3 (lila Blazer, dunkle Hose), Kopf Long.
Frau Dahlke (um 30, Mieterin): standing/shirt-4 (schwarze Bluse, blaue Hose), Kopf Long Curly.
Herr Henke (um 65, Vermieter): standing/resting-2 (schwarzer Pullover, graublaue Hose, Hand an der Hüfte), Kopf Gray Short (graues Haar),
Brille Glasses 2; sachlich, keine „fiese“ Darstellung.
Posen bewusst anders als in 095–097 (easing-1/-2, shirt-3, resting-1, blazer-4, crossed_arms-1, pointing_finger-2,
walking-1). Keine Bärte, keine Prothesen-Posen, keine Muster. Alle Posen blicken im Original nach rechts; die Grundansicht
ist gespiegelt und blickt nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Smile, Serious, Suspicious, Driven bzw.
„Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten (…_redet…, Lexi) zusätzlich mit a/o/e: Augen der
Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 % der Gesichtshöhe."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_098")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "LM": ("standing/blazer-3", "Long", None, None, {"Skin": "#D9A47E", "Jacket": "#B8A9F5", "Pants": "#3A3A48"}),
    "DA": ("standing/shirt-4", "Long Curly", None, None, {"Skin": "#E8B894", "Pants": "#8DB3F2"}),
    "HE": ("standing/resting-2", "Gray Short", None, "Glasses 2", {"Skin": "#EBC2A0", "Pants": "#7A8BA8", "Hair": "#C4C4CC"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("LM_ruhig", "LM", "Calm", 0), ("LM_redet", "LM", "Smile", 1), ("LM_entschlossen", "LM", "Driven", 0),
    ("DA_ruhig", "DA", "Calm", 0), ("DA_froh", "DA", "Smile", 0), ("DA_liest", "DA", "Serious", 0),
    ("DA_redet", "DA", "Driven", 1), ("DA_sorge", "DA", "Concerned|Serious", 0), ("DA_denkt", "DA", "Suspicious", 0),
    ("DA_redetfroh", "DA", "Smile", 1),
    ("HE_ruhig", "HE", "Calm", 0), ("HE_redet", "HE", "Serious", 1), ("HE_denkt", "HE", "Suspicious", 0),
    ("HE_froh", "HE", "Smile", 0),
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
