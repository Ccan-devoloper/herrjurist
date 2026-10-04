"""Figuren für Folge 193 (Weiterfresserschaden) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv.
Hinnerk (HI, um 30, Käufer des fabrikneuen Kleinwagens; Stimme niklas): standing/shirt-3 (hellblaues Hemd #8DB3F2,
  schwarze Hose, weiße Schuhe), Kopf Short 5 (Haar Dunkelbraun #4A3222), Haut #F1C9A5, keine Brille, kein Bart.
Ottokar (OT, um 60, Kfz-Meister der Werkstatt; Stimme helmut): standing/shirt-4 (dunkles Hemd, blaue Arbeitshose #3F6FB5,
  weiße Schuhe), Kopf No Hair 3 (Glatze, Haarkranz Grau #C9C9C9), Brille Glasses 2, Haut #E2B08C, kein Bart.
Posen der letzten drei Folgen (188: pointing_finger-2, crossed_arms-1; 189: blazer-4, crossed_arms-2; 190: resting-1,
resting-2, walking-2) und der Folge 187 (easing-1, pointing_finger-1) nicht verwendet, auch nicht deren Kopf-/Farbpaare
(Gray Short, No Hair 1, Orange-Hemd, Rosa, Koralle, Navy); robot_dance-1 bleibt Lexi; keine Polka Dots, keine Prothesen-
Posen (shirt-1/-2, blazer-1/-2), keine Bärte, keine Karikatur. Präfixe HI_/OT_ (nie ER_). Alle Posen blicken im Original
nach rechts; die Grundansicht ist gespiegelt und blickt nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Suspicious, Fear, Tired, Smile, Solemn, Very Angry
bzw. „Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten HI_redet, OT_redet (und Lexi) zusätzlich mit a/o/e:
Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_193")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "HI": ("standing/shirt-3", "Short 5", None, None, {"Skin": "#F1C9A5", "Top": "#8DB3F2", "Hair": "#4A3222"}),
    "OT": ("standing/shirt-4", "No Hair 3", None, "Glasses 2", {"Skin": "#E2B08C", "Pants": "#3F6FB5", "Hair": "#C9C9C9"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("HI_ruhig", "HI", "Calm", 0), ("HI_froh", "HI", "Smile", 0), ("HI_schreck", "HI", "Fear", 0),
    ("HI_redet", "HI", "Concerned|Serious", 1), ("HI_wut", "HI", "Very Angry", 0), ("HI_ernst", "HI", "Serious", 0),
    ("HI_denkt", "HI", "Suspicious", 0), ("HI_sorge", "HI", "Concerned|Serious", 0), ("HI_muede", "HI", "Tired", 0),
    ("HI_still", "HI", "Solemn", 0),
    ("OT_ruhig", "OT", "Calm", 0), ("OT_redet", "OT", "Serious", 1), ("OT_ernst", "OT", "Serious", 0),
    ("OT_denkt", "OT", "Suspicious", 0), ("OT_sorge", "OT", "Concerned|Serious", 0), ("OT_froh", "OT", "Smile", 0),
    ("OT_muede", "OT", "Tired", 0), ("OT_still", "OT", "Solemn", 0),
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
