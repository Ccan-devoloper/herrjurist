"""Figuren für Folge 274 (Gebietserhaltungsanspruch: Flüchtlingsunterkunft im Gewerbegebiet) aus der
LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv.
Frau Hollenberg (HO, um 45, Schreinermeisterin, Eigentümerin der Schreinerei; Stimme laura_ruhig): standing/easing-2
  (offenes Hemd Orange #F9A66C über schwarzem Shirt, Hose Graublau #5A6B7A – Werkstattkleidung), Kopf Medium Bangs 3,
  Haut #E8B894, keine Brille.
Herr Kerkhoff (KE, um 60, leitet die Bauaufsicht; Stimme william): standing/resting-2 (schwarzer Pullover, Hose Khaki
  #C9A66B), Kopf No Hair 2, Brille Glasses 4, Haut #D9A47E, kein Bart.
Geflüchtete erscheinen nicht als Figuren (Vorgabe Koordinator: keine Gesichter in Gruppen, die Unterkunft nur als Gebäude).
Posen der letzten Folgen (270: resting-1, robot_dance-2, blazer-4; 271: resting-1, easing-1; 272: robot_dance-3,
crossed_arms-1, blazer-3; 273: crossed_arms-2, shirt-4) nicht verwendet; robot_dance-1 bleibt Lexi; keine Polka Dots, keine
Prothesen-Posen, keine Bärte, keine Karikatur. Präfixe HO_/KE_ (nie ER_).
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Suspicious, Smile bzw. „Augen|geschlossener Mund“
(Concerned|Serious, Smile Big|Smile). Sprechende Ansichten HO_redet, HO_redet2, KE_redet (und Lexi) zusätzlich mit a/o/e:
Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_274")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "HO": ("standing/easing-2", "Medium Bangs 3", None, None, {"Skin": "#E8B894", "Jacket": "#F9A66C", "Pants": "#5A6B7A"}),
    "KE": ("standing/resting-2", "No Hair 2", None, "Glasses 4", {"Skin": "#D9A47E", "Pants": "#C9A66B"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("HO_ruhig", "HO", "Calm", 0), ("HO_sorge", "HO", "Concerned|Serious", 0), ("HO_denkt", "HO", "Suspicious", 0),
    ("HO_ernst", "HO", "Serious", 0), ("HO_froh", "HO", "Smile", 0), ("HO_erleichtert", "HO", "Smile Big|Smile", 0),
    ("HO_redet", "HO", "Concerned|Serious", 1), ("HO_redet2", "HO", "Smile", 1),
    ("KE_ruhig", "KE", "Calm", 0), ("KE_ernst", "KE", "Serious", 0), ("KE_froh", "KE", "Smile", 0),
    ("KE_denkt", "KE", "Suspicious", 0), ("KE_redet", "KE", "Calm", 1),
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
