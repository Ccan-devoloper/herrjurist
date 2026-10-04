"""Figuren für Folge 159 (Auslegungsmethoden) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv.
Thekla (Anfang 20, Jurastudentin mit E-Scooter): standing/robot_dance-3 (Oberteil Koralle #F07A6A, Hose Dunkelblau
#3B3B4F, die ausgestreckte Hand hält die Lenkstange des E-Scooters), Kopf Medium Bangs (Haar #7A4A2A), keine Brille,
Haut #F2D3B8. Stimme ela_froh.
Professor Lindhorst (um 60, Dozent im Methodenseminar): standing/crossed_arms-1 (Pullover Grün #8FD694, schwarze Hose,
Arme verschränkt), Kopf Gray Short, Brille Glasses 3, kein Bart, Haut #E8B98F. Stimme helmut.
Posen, Kleidung und Muster nicht aus den Folgen 156–158 (easing-1, easing-2, shirt-3, shirt-4, walking-1, walking-2,
resting-2, robot_dance-2, pointing_finger-2); robot_dance-1 bleibt Lexi vorbehalten; keine Prothesen-Posen (blazer-1/-2,
shirt-1/-2), keine Bärte, keine Polka Dots, keine Karikatur. Präfix TH_/LI_ (nie ER_).
Blickrichtung: wird am Kontaktbild besetzung_159.png geprüft (BLICK_LINKS = Originalrichtung je Person). Grundansicht blickt
immer nach links (zur Tafel), Suffix _r nach rechts. Grundmimik immer mit geschlossenem Mund: Calm, Serious, Smile,
Suspicious bzw. „Augen|geschlossener Mund“ (Concerned|Serious, Smile Big|Smile). Sprechende Ansichten (TH_redet,
LI_redet, LI_redetfroh, Lexi) zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_159")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben, blickt im Original nach links?)
P = {
    "TH": ("standing/robot_dance-3", "Medium Bangs", None, None, {"Skin": "#F2D3B8", "Hair": "#7A4A2A", "Top": "#F07A6A",
                                                                 "Pants": "#3B3B4F"}, False),
    "LI": ("standing/crossed_arms-1", "Gray Short", None, "Glasses 3", {"Skin": "#E8B98F", "Top": "#8FD694",
                                                                       "Pants": "#2B2B2B"}, False),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("TH_ruhig", "TH", "Calm", 0), ("TH_froh", "TH", "Smile Big|Smile", 0), ("TH_redet", "TH", "Smile", 1),
    ("TH_denkt", "TH", "Suspicious", 0), ("TH_staunt", "TH", "Concerned|Serious", 0), ("TH_laechelt", "TH", "Smile", 0),
    ("LI_ruhig", "LI", "Calm", 0), ("LI_redet", "LI", "Serious", 1), ("LI_redetfroh", "LI", "Smile", 1),
    ("LI_froh", "LI", "Smile Big|Smile", 0), ("LI_denkt", "LI", "Suspicious", 0), ("LI_ernst", "LI", "Serious", 0),
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
