"""Figuren für Folge 203 (Einverständliche Fremdgefährdung: Beifahrer beim Straßenrennen) aus der LexVerse-Figma-Bibliothek
(Open Peeps, CC0). Alle Figuren fiktiv, gewöhnlich gekleidet (keine Rennkleidung, keine Markenlogos, keine Klischees).
Hilmar (HI, Anfang 50, Fahrer; Stimme helmut): standing/crossed_arms-1 (Pullover Orange #F9A66C, schwarze Hose der Pose),
  Kopf No Hair 3 (Haarkranz Grau #B5B5B5), Haut #EDC3A0, keine Brille, kein Bart. Keine „fiese“ Mimik.
Eike (EI, um 25, Beifahrer, feuert an; Stimme niklas): standing/pointing_finger-2 (schwarzes Oberteil der Pose, Hose Blau
  #8DB3F2), Kopf Short 2, Haut #B9805A.
Posen der letzten drei Folgen (198: easing-1, resting-1; 199: easing-2, pointing_finger-1; 200: shirt-3, resting-2,
walking-1/-2) nicht verwendet; Lexi-Pose (robot_dance-1) nicht für Fallfiguren; keine Polka Dots, keine Bärte, keine
Prothesen-Posen, keine Karikatur. Präfixe HI_/EI_ (nie ER_).
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Suspicious, Solemn, Smile, Driven bzw.
„Augen|geschlossener Mund“ (Smile Big|Smile, Concerned|Serious). Sprechende Ansichten HI_redet, EI_redet (und Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_203")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "HI": ("standing/crossed_arms-1", "No Hair 3", None, None, {"Skin": "#EDC3A0", "Top": "#F9A66C", "Hair": "#B5B5B5"}),
    "EI": ("standing/pointing_finger-2", "Short 2", None, None, {"Skin": "#B9805A", "Pants": "#8DB3F2"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("HI_ruhig", "HI", "Calm", 0), ("HI_ernst", "HI", "Serious", 0), ("HI_entschl", "HI", "Driven", 0),
    ("HI_still", "HI", "Solemn", 0), ("HI_denkt", "HI", "Suspicious", 0), ("HI_sorge", "HI", "Concerned|Serious", 0),
    ("HI_redet", "HI", "Driven", 1),
    ("EI_ruhig", "EI", "Calm", 0), ("EI_froh", "EI", "Smile", 0), ("EI_begeistert", "EI", "Smile Big|Smile", 0),
    ("EI_denkt", "EI", "Suspicious", 0), ("EI_ernst", "EI", "Serious", 0),
    ("EI_redet", "EI", "Smile Big|Smile", 1),
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
