"""Figuren für Folge 168 (Revisionsfrist StPO; Landgericht und Kanzlei) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv.
Herr Tiedemann (TI, um 60, Angeklagter; Stimme william): standing/crossed_arms-1 (Pullover Sand #C9B38C, schwarze Hose, weiße
  Schuhe), Kopf Gray Short, Brille Glasses 3, Haut #EDC3A0, kein Bart.
Rechtsanwältin Sternberg (SB, um 40, Verteidigerin; Stimme laura_ruhig): standing/blazer-4 (Sakko Anthrazit #2B2B35 wie eine
  Robe, weißes Shirt, schwarze Hose), Kopf Medium Straight (schwarzes Haar), Haut #E2B190, keine Brille.
Vorsitzende Richterin (RI, um 55, Funktionsrolle ohne Namen, spricht nicht): standing/pointing_finger-1 (ganz in Schwarz wie
  eine Robe, erhobener Zeigefinger bei der Urteilsverkündung), Kopf Medium 3, Brille Glasses 2, Haut #F0CDB4.
Posen der letzten drei Folgen (165: walking-1, crossed_arms-2; 166: resting-2, pointing_finger-2, blazer-3, walking-1; 167:
resting-1, blazer-1) nicht verwendet; keine Polka Dots, keine Prothesen-Posen (blazer-1/-2, shirt-1/-2), keine Bärte, keine
Karikatur, keine Täter-Klischees (Angeklagter in Alltagskleidung, neutrale Mimik). Präfixe TI_/SB_/RI_ (nie ER_).
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Suspicious, Fear, Tired, Smile, Solemn bzw.
„Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten TI_redet, TI_redet2, SB_redet, SB_redet2 (und Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_168")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "TI": ("standing/crossed_arms-1", "Gray Short", None, "Glasses 3", {"Skin": "#EDC3A0", "Top": "#C9B38C"}),
    "SB": ("standing/blazer-4", "Medium Straight", None, None, {"Skin": "#E2B190", "Jacket": "#2B2B35", "Top": "#FFFFFF"}),
    "RI": ("standing/pointing_finger-1", "Medium 3", None, "Glasses 2", {"Skin": "#F0CDB4"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("TI_ruhig", "TI", "Calm", 0), ("TI_ernst", "TI", "Serious", 0), ("TI_sorge", "TI", "Concerned|Serious", 0),
    ("TI_schreck", "TI", "Fear", 0), ("TI_skeptisch", "TI", "Suspicious", 0), ("TI_muede", "TI", "Tired", 0),
    ("TI_froh", "TI", "Smile", 0), ("TI_redet", "TI", "Serious", 1), ("TI_redet2", "TI", "Concerned|Serious", 1),
    ("SB_ruhig", "SB", "Calm", 0), ("SB_ernst", "SB", "Serious", 0), ("SB_froh", "SB", "Smile", 0),
    ("SB_skeptisch", "SB", "Suspicious", 0), ("SB_schreck", "SB", "Fear", 0), ("SB_still", "SB", "Solemn", 0),
    ("SB_redet", "SB", "Serious", 1), ("SB_redet2", "SB", "Calm", 1),
    ("RI_ernst", "RI", "Serious", 0), ("RI_ruhig", "RI", "Calm", 0),
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
