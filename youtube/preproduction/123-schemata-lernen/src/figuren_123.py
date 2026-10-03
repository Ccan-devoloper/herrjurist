"""Figuren für Folge 123 (Prüfungsschemata lernen) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv.
Gunnar (Anfang 20, Jurastudent mit Karteikarten-Turm): standing/easing-1 (offenes Hemd Grün #8FD694 über weißem Shirt,
schwarze Hose, Turnschuhe), Kopf Short 4 (Haar braun #6B4A32), keine Brille, Haut #E8B98F. Stimme niklas.
Marlene (Mitte 20, Tutorin): standing/blazer-3 (Blazer Rot #F07A6A über schwarzem Top, Hose Dunkelblau #3B3B4F, Hand an der
Hüfte), Kopf Medium 3 (Haar dunkel #3A2A20), keine Brille, Haut #F2D3B8. Stimme ela_froh.
Posen, Farben und Muster nicht aus den Folgen 120–122 (pointing_finger-1, crossed_arms-1, walking-2, blazer-4, polka_dots,
shirt-3, walking-3, walking-1, resting-2); keine Prothesen-Posen (blazer-1/-2, shirt-1/-2), keine Bärte, keine Polka Dots,
keine Karikatur. Präfix GU_/MA_ (nie ER_).
Blickrichtung: beide Posen blicken mit diesen Köpfen im Original nach rechts (Kopfprobe am Kontaktbild: Ohr links, Gesicht rechts). Grundansicht blickt
immer nach links (zur Tafel), Suffix _r nach rechts. Grundmimik immer mit geschlossenem Mund: Calm, Serious, Smile,
Suspicious, Fear, Tired bzw. „Augen|geschlossener Mund“ (Concerned|Serious, Smile Big|Smile). Sprechende Ansichten
(GU_redet, MA_redet, Lexi) zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_123")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben, blickt im Original nach links?)
P = {
    "GU": ("standing/easing-1", "Short 4", None, None, {"Skin": "#E8B98F", "Hair": "#6B4A32", "Jacket": "#8FD694",
                                                       "Top": "#FFFFFF", "Pants": "#2B2B2B"}, False),
    "MA": ("standing/blazer-3", "Medium 3", None, None, {"Skin": "#F2D3B8", "Hair": "#3A2A20", "Jacket": "#F07A6A",
                                                        "Pants": "#3B3B4F"}, False),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("GU_ruhig", "GU", "Calm", 0), ("GU_froh", "GU", "Smile Big|Smile", 0), ("GU_redet", "GU", "Serious", 1),
    ("GU_redetfroh", "GU", "Smile", 1), ("GU_sorge", "GU", "Concerned|Serious", 0), ("GU_denkt", "GU", "Suspicious", 0),
    ("GU_muede", "GU", "Tired", 0),
    ("MA_ruhig", "MA", "Calm", 0), ("MA_redet", "MA", "Smile", 1), ("MA_froh", "MA", "Smile Big|Smile", 0),
    ("MA_ernst", "MA", "Serious", 0), ("MA_denkt", "MA", "Suspicious", 0),
]

if __name__ == "__main__":
    os.makedirs(ZIEL, exist_ok=True)
    n = 0
    for name, p, mimik, mund in LISTE:
        pose, kopf, bart, brille, farben, links = P[p]
        for suffix, nach_links in (("", True), ("_r", False)):
            sp = links != nach_links          # spiegeln, wenn die Originalrichtung nicht passt
            figur(pose, kopf, mimik, bart, brille, farben, hoehe=1200, spiegeln=sp).save(f"{ZIEL}/{name}{suffix}.png"); n += 1
            if mund:
                for k, m in MUND.items():
                    figur(pose, kopf, f"{mimik.split('|')[0]}|{m}", bart, brille, farben, hoehe=1200,
                          spiegeln=sp).save(f"{ZIEL}/{name}{suffix}_{k}.png"); n += 1
    # Lexi (feste Moderatorin, Stimme Carla), blickt nach links zur Tafel
    for name, (pose, mimik) in {"LX_erklaert": ("standing/robot_dance-1", "Smile"), "LX_warnt": ("standing/robot_dance-1", "Serious")}.items():
        a = LX.AUSSEHEN
        for k, g in {"": mimik, **{"_" + k: f"{mimik}|{m}" for k, m in MUND.items()}}.items():
            figur(pose, a["kopf"], g, a["bart"], a["brille"], a["farben"], hoehe=1200, spiegeln=True).save(f"{ZIEL}/{name}{k}.png"); n += 1
    print(n, "Figurenbilder ->", ZIEL)
