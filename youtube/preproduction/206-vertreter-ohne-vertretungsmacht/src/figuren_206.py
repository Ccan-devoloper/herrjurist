"""Figuren für Folge 206 (Vertreter ohne Vertretungsmacht) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Personen fiktiv.
Enno (EN, um 28, Eigentümer des Motorrads, verweigert die Genehmigung; Stimme niklas): standing/pointing_finger-1 (schwarzer
  Pullover, schwarze Hose und Stiefel der Pose, erhobener Zeigefinger – er lehnt ab), Kopf Short 5, Haut #D9A47E, kein Bart.
Kuno (KU, um 60, Bekannter, verkauft ohne Vertretungsmacht; Stimme helmut): standing/robot_dance-2 (schwarzes Oberteil der
  Pose, Hose Braun #6B5440, weiße Schuhe, anbietende offene Hand), Kopf No Hair 2, Brille Glasses, Haut #EDC3A0, kein Bart.
  Kein Bösewicht: verlegen, nicht „fies“.
Silja (SI, um 30, Käuferin; Stimme ela_froh): standing/resting-1 (Pullover Rosa #F6A5C0, schwarze Hose der Pose), Kopf
  Long Curly, Haut #F2CDB0.
Posen der letzten drei Folgen (203: crossed_arms-1, pointing_finger-2; 204: shirt-3, crossed_arms-2, easing-2; 205: shirt-3,
resting-2, easing-1) und aus 202 (robot_dance-3, blazer-3, shirt-4) nicht verwendet; robot_dance-1 bleibt Lexi; blazer-1,
blazer-2, shirt-1/2 (Prothesen) verworfen; keine Polka Dots, keine Bärte. Präfixe EN_/KU_/SI_ (nie ER_). Alle Posen blicken
im Original nach rechts; Grundansicht gespiegelt (blickt nach links), Suffix _r nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Smile, Awe, Fear, Serious, Suspicious, Solemn bzw.
„Augen|geschlossener Mund“ (Concerned|Serious, Smile Big|Smile). Sprechende Ansichten EN_redet (Serious), KU_redet (Smile),
KU_klagt (Concerned|Serious), SI_redet (Smile Big|Smile), SI_fordert (Serious) und Lexi zusätzlich mit a/o/e: Augen der
Grundmimik + Mund Explaining / Concerned Fear / Hectic."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_206")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "EN": ("standing/pointing_finger-1", "Short 5", None, None, {"Skin": "#D9A47E"}),
    "KU": ("standing/robot_dance-2", "No Hair 2", None, "Glasses", {"Skin": "#EDC3A0", "Pants": "#6B5440"}),
    "SI": ("standing/resting-1", "Long Curly", None, None, {"Skin": "#F2CDB0", "Top": "#F6A5C0"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("EN_ruhig", "EN", "Calm", 0), ("EN_froh", "EN", "Smile", 0), ("EN_ernst", "EN", "Serious", 0),
    ("EN_denkt", "EN", "Suspicious", 0), ("EN_sorge", "EN", "Concerned|Serious", 0), ("EN_staunt", "EN", "Awe", 0),
    ("EN_redet", "EN", "Serious", 1),
    ("KU_ruhig", "KU", "Calm", 0), ("KU_froh", "KU", "Smile", 0), ("KU_sorge", "KU", "Concerned|Serious", 0),
    ("KU_schreck", "KU", "Fear", 0), ("KU_denkt", "KU", "Suspicious", 0), ("KU_still", "KU", "Solemn", 0),
    ("KU_redet", "KU", "Smile", 1), ("KU_klagt", "KU", "Concerned|Serious", 1),
    ("SI_ruhig", "SI", "Calm", 0), ("SI_froh", "SI", "Smile", 0), ("SI_freut", "SI", "Smile Big|Smile", 0),
    ("SI_staunt", "SI", "Awe", 0), ("SI_ernst", "SI", "Serious", 0), ("SI_denkt", "SI", "Suspicious", 0),
    ("SI_sorge", "SI", "Concerned|Serious", 0), ("SI_redet", "SI", "Smile Big|Smile", 1), ("SI_fordert", "SI", "Serious", 1),
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
