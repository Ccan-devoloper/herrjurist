"""Figuren für Folge 269 (Öffentliche Ordnung: Zwergenweitwurf und Laserdrome) aus der LexVerse-Figma-Bibliothek (Open Peeps,
CC0). Alle Figuren fiktiv, keine Karikatur, keine Klischees, keine Waffen.
Frau Leuschner (um 45, Leiterin des Ordnungsamts; Stimme julia): standing/blazer-1 (Blazer Dunkelgrün #3B6B57, Hose
Anthrazit #2E3440; Beinprothese der Pose – positive Rolle), Kopf Long, Haut #E0A882.
Frau Bredemeier (um 40, Betreiberin der Diskothek; Stimme ela_froh): standing/pointing_finger-1 (schwarzes Oberteil und
schwarze Hose der Pose, zeigt auf das Plakat), Kopf Long Curly, Haut #F2C9A8.
Herr Mehring (um 35, kleinwüchsiger Artist; Stimme niklas): standing/resting-2 (schwarzer Pullover der Pose, Jeans
Dunkelblau #2F3E6B), Kopf Short 2, Kinnbart „Chin“ (liegt unter dem Mund), Haut #B9805C. Ein selbstbewusster Erwachsener,
respektvoll dargestellt; die Körpergröße entsteht nur über die Darstellungshöhe (74 % der Erwachsenenhöhe) in den
Folien, nicht über eine veränderte Zeichnung. Kein Wurf im Bild.
Posen nicht aus den letzten Folgen 262–267 (easing-1/-2, blazer-2/-3/-4, pointing_finger-2, shirt-3/-4, resting-1,
robot_dance-2/-3, crossed_arms-1/-2, walking-1/-2/-3); keine Polka Dots. Präfix LE_/BR_/ME_ (nie ER_). Alle Posen blicken
im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (LE_redet, BR_redet, ME_redet, Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_269")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "LE": ("standing/blazer-1", "Long", None, None, {"Skin": "#E0A882", "Jacket": "#3B6B57", "Pants": "#2E3440"}),
    "BR": ("standing/pointing_finger-1", "Long Curly", None, None, {"Skin": "#F2C9A8"}),
    "ME": ("standing/resting-2", "Short 2", "Chin", None, {"Skin": "#B9805C", "Pants": "#2F3E6B"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("LE_ruhig", "LE", "Calm", 0), ("LE_redet", "LE", "Serious", 1), ("LE_ernst", "LE", "Serious", 0),
    ("LE_denkt", "LE", "Suspicious", 0), ("LE_still", "LE", "Solemn", 0), ("LE_froh", "LE", "Smile", 0),
    ("BR_froh", "BR", "Smile", 0), ("BR_redet", "BR", "Smile", 1), ("BR_sorge", "BR", "Concerned|Serious", 0),
    ("BR_skeptisch", "BR", "Suspicious", 0), ("BR_muede", "BR", "Tired", 0), ("BR_ruhig", "BR", "Calm", 0),
    ("ME_ruhig", "ME", "Calm", 0), ("ME_redet", "ME", "Driven", 1), ("ME_fest", "ME", "Driven", 0),
    ("ME_ernst", "ME", "Serious", 0), ("ME_still", "ME", "Solemn", 0), ("ME_froh", "ME", "Smile", 0),
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
    for name, (pose, mimik) in {"LX_erklaert": ("standing/robot_dance-1", "Smile"), "LX_warnt": ("standing/robot_dance-1", "Serious")}.items():
        a = LX.AUSSEHEN
        for k, g in {"": mimik, **{"_" + k: f"{mimik}|{m}" for k, m in MUND.items()}}.items():
            figur(pose, a["kopf"], g, a["bart"], a["brille"], a["farben"], hoehe=1200, spiegeln=True).save(f"{ZIEL}/{name}{k}.png"); n += 1
    print(n, "Figurenbilder ->", ZIEL)
