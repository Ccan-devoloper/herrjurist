"""Figuren für Folge 161 (Abhandenkommen § 935 BGB; verliehene und gestohlene Kamera) aus der LexVerse-Figma-Bibliothek
(Open Peeps, CC0). Alle Figuren fiktiv, Erwachsene in Alltagskleidung, keine Marken.
Hella (HE, um 35, Eigentümerin der Kamera; Stimme sabrina): standing/blazer-3 (Blazer Lila #B8A9F5, Hose Blau #8DB3F2,
  weiße Schuhe), Kopf Medium Straight (Haar Dunkelbraun #5A3A22), Haut #F1C9A5, keine Brille.
Knut (KN, um 35, Freund und Entleiher; im Gedankenfall Angestellter im Fotoladen; Stimme marc): standing/resting-1 (Pullover
  Orange #F9A66C, schwarze Hose), Kopf Short 2, Haut #E8B48C, kein Bart.
Berta (BT, um 60, gutgläubige Käuferin; spricht nicht): standing/crossed_arms-1 (Oberteil Gelb #F9D56E, schwarze Hose), Kopf
  Gray Short (Haar Grau #C9C9C9), Brille Glasses 3, Haut #F3D3B8.
Dieb (DI, um 40, Fall B; spricht nicht; bewusst unauffällig, kein Täterklischee: keine Kapuze, keine Maske, ruhige Mimik):
  standing/crossed_arms-2 (schwarzes Oberteil, Hose Graublau #9FB4C7), Kopf Short 3, Haut #EDC09A, kein Bart.
Posen der letzten drei Folgen (156: easing-2, shirt-3, walking-2, robot_dance-2, pointing_finger-2; 157: resting-2,
walking-1; 158: shirt-4, easing-1) nicht verwendet; robot_dance-1 bleibt Lexi; keine Polka Dots, keine Prothesen-Posen
(blazer-1/-2, shirt-1/-2), keine Bärte, keine Karikatur. Präfixe HE_/KN_/BT_/DI_ (nie ER_). Alle Posen blicken im Original
nach rechts; die Grundansicht ist gespiegelt und blickt nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten HE_redet, KN_redet (und Lexi) zusätzlich mit
a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_161")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "HE": ("standing/blazer-3", "Medium Straight", None, None, {"Skin": "#F1C9A5", "Jacket": "#B8A9F5", "Pants": "#8DB3F2",
                                                                "Hair": "#5A3A22"}),
    "KN": ("standing/resting-1", "Short 2", None, None, {"Skin": "#E8B48C", "Top": "#F9A66C"}),
    "BT": ("standing/crossed_arms-1", "Gray Short", None, "Glasses 3", {"Skin": "#F3D3B8", "Top": "#F9D56E", "Hair": "#C9C9C9"}),
    "DI": ("standing/crossed_arms-2", "Short 3", None, None, {"Skin": "#EDC09A", "Pants": "#9FB4C7"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("HE_ruhig", "HE", "Calm", 0), ("HE_redet", "HE", "Smile", 1), ("HE_froh", "HE", "Smile", 0),
    ("HE_ernst", "HE", "Serious", 0), ("HE_skeptisch", "HE", "Suspicious", 0), ("HE_sorge", "HE", "Concerned|Serious", 0),
    ("HE_schreck", "HE", "Fear", 0), ("HE_still", "HE", "Solemn", 0),
    ("KN_ruhig", "KN", "Calm", 0), ("KN_redet", "KN", "Smile", 1), ("KN_froh", "KN", "Smile", 0),
    ("KN_denkt", "KN", "Suspicious", 0), ("KN_sorge", "KN", "Concerned|Serious", 0), ("KN_ernst", "KN", "Serious", 0),
    ("KN_still", "KN", "Solemn", 0),
    ("BT_ruhig", "BT", "Calm", 0), ("BT_froh", "BT", "Smile", 0), ("BT_denkt", "BT", "Suspicious", 0),
    ("BT_sorge", "BT", "Concerned|Serious", 0), ("BT_ernst", "BT", "Serious", 0),
    ("DI_ruhig", "DI", "Calm", 0), ("DI_ernst", "DI", "Serious", 0),
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
