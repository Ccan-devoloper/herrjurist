"""Figuren für Folge 158 (§ 823 II BGB, Schutzgesetzverletzung; Nachbar ohne Fahrerlaubnis) aus der LexVerse-Figma-Bibliothek
(Open Peeps, CC0). Alle Figuren fiktiv.
Hiltrud (HI, um 45, Geschädigte, ihr Auto parkt am Straßenrand; Stimme laura_ruhig): standing/shirt-4 (schwarze Bluse mit
  Knöpfen, Hose Rot #F07A6A, weiße Schuhe), Kopf Bangs (Haar Kastanienbraun #8A5A34), Haut #F2C9A6, keine Brille.
  (robot_dance-3 verworfen: zu ähnlich wie Lexi, robot_dance-1.)
Burkhard (BU, um 60, Nachbar ohne Fahrerlaubnis, Halter seines Autos; Stimme william): standing/easing-1 (offenes Hemd Beige
  #D6B48A über weißem Shirt, schwarze Hose, weiße Schuhe), Kopf Gray Medium (Haar Grau #C9C9C9), Brille Glasses 2,
  Haut #E3B08C, kein Bart.
Posen und Kleidung der letzten drei Folgen (155: blazer-4, walking-3, sitting/hands_back-1; 156: easing-2, shirt-3, walking-2,
robot_dance-2, pointing_finger-2; 157 beim Start ohne Figuren) nicht verwendet; robot_dance-1 bleibt Lexi; keine Polka Dots,
keine Prothesen-Posen, keine Bärte, keine Karikatur. Präfixe HI_/BU_ (nie ER_). Alle Posen blicken im Original nach rechts;
die Grundansicht ist gespiegelt und blickt nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Suspicious, Fear, Tired, Smile, Solemn bzw.
„Augen|geschlossener Mund“ (Concerned|Serious, Rage|Serious). Sprechende Ansichten HI_redet, BU_redet (und Lexi) zusätzlich
mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_158")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "HI": ("standing/shirt-4", "Bangs", None, None, {"Skin": "#F2C9A6", "Pants": "#F07A6A", "Hair": "#8A5A34"}),
    "BU": ("standing/easing-1", "Gray Medium", None, "Glasses 2", {"Skin": "#E3B08C", "Jacket": "#D6B48A", "Top": "#FFFFFF",
                                                                  "Hair": "#C9C9C9"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("HI_ruhig", "HI", "Calm", 0), ("HI_schreck", "HI", "Fear", 0), ("HI_redet", "HI", "Rage|Serious", 1),
    ("HI_ernst", "HI", "Serious", 0), ("HI_skeptisch", "HI", "Suspicious", 0), ("HI_sorge", "HI", "Concerned|Serious", 0),
    ("HI_froh", "HI", "Smile", 0), ("HI_still", "HI", "Solemn", 0),
    ("BU_ruhig", "BU", "Calm", 0), ("BU_schreck", "BU", "Fear", 0), ("BU_redet", "BU", "Concerned|Serious", 1),
    ("BU_ernst", "BU", "Serious", 0), ("BU_denkt", "BU", "Suspicious", 0), ("BU_sorge", "BU", "Concerned|Serious", 0),
    ("BU_muede", "BU", "Tired", 0), ("BU_still", "BU", "Solemn", 0),
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
