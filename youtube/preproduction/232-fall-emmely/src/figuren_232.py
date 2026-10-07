"""Figuren für Folge 232 (Der Fall Emmely, § 626 BGB; Supermarkt) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv; die reale Klägerin wird nicht dargestellt.
Doris (DO, um 55, Kassiererin seit fast 31 Jahren; spricht nicht): standing/resting-1 (Langarm-Oberteil Petrol #5FA8A0,
  schwarze Hose der Pose), Kopf Gray Medium (Haar in der Bibliotheksfarbe Kupferrot), Brille Glasses 4, Haut #F0C8A8 – freundlich, kein Klischee.
Merle (ME, um 25, Kassiererin, Kollegin; Stimme ela_froh): standing/easing-1 (offene Jacke Rot #F07A6A, weißes Oberteil, schwarze
  Hose der Pose), Kopf Long Bangs (schwarzes Haar), Haut #C68E6A.
Herr Bartels (BT, um 60, Filialleiter; Stimme helmut): standing/crossed_arms-1 (Oberteil Hellblau #8DB3F2, schwarze Hose der
  Pose), Kopf Gray Short (Haar nur als Kontur, Fläche hautfarben; der Hair-Wert greift nicht sichtbar), Brille Glasses, Haut #E8B48F, kein Bart.
Posen der letzten drei Folgen (229: robot_dance-3, blazer-3, easing-2, walking-1; 230: pointing_finger-2, shirt-3, shirt-4;
231: walking-2, robot_dance-3) nicht verwendet; keine Polka Dots, keine Prothesen-Posen (blazer-1/-2, shirt-1/-2), keine Bärte,
keine Karikatur. Präfixe DO_/ME_/BT_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und
blickt nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Smile, Fear, Tired, Solemn, Suspicious, Awe bzw.
„Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten ME_redet, BT_redet (und Lexi) zusätzlich mit a/o/e:
Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_232")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "DO": ("standing/resting-1", "Gray Medium", None, "Glasses 4", {"Skin": "#F0C8A8", "Top": "#5FA8A0"}),
    "ME": ("standing/easing-1", "Long Bangs", None, None, {"Skin": "#C68E6A", "Jacket": "#F07A6A", "Top": "#FFFFFF"}),
    "BT": ("standing/crossed_arms-1", "Gray Short", None, "Glasses", {"Skin": "#E8B48F", "Top": "#8DB3F2", "Hair": "#A9A9B0"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("DO_froh", "DO", "Smile", 0), ("DO_ruhig", "DO", "Calm", 0), ("DO_ernst", "DO", "Serious", 0),
    ("DO_sorge", "DO", "Concerned|Serious", 0), ("DO_schreck", "DO", "Fear", 0), ("DO_muede", "DO", "Tired", 0),
    ("DO_still", "DO", "Solemn", 0), ("DO_staunt", "DO", "Awe", 0),
    ("ME_froh", "ME", "Smile", 0), ("ME_redet", "ME", "Smile", 1), ("ME_ruhig", "ME", "Calm", 0),
    ("ME_sorge", "ME", "Concerned|Serious", 0), ("ME_staunt", "ME", "Awe", 0), ("ME_ernst", "ME", "Serious", 0),
    ("BT_ruhig", "BT", "Calm", 0), ("BT_redet", "BT", "Serious", 1), ("BT_ernst", "BT", "Serious", 0),
    ("BT_skeptisch", "BT", "Suspicious", 0), ("BT_still", "BT", "Solemn", 0), ("BT_froh", "BT", "Smile", 0),
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
