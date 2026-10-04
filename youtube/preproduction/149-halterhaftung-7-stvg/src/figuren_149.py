"""Figuren für Folge 149 (Halterhaftung § 7 StVG; Parkplatzrempler) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv.
Heidrun (HD, um 45, setzt rückwärts aus, Geschädigte; Stimme sabrina): standing/blazer-4 (Blazer Lila #B8A9F5 über weißem
  Shirt, Hose Dunkelblau #2E3550, weiße Schuhe), Kopf Medium 2 (Haar Dunkelblond #8A5E34), Haut #EFC2A0, keine Brille.
Volkmar (VO, um 50, setzt gegenüber zurück, Halter und Fahrer; Stimme marc): standing/crossed_arms-2 (schwarzes Oberteil,
  verschränkte Arme – „Ich?“, Hose Grün #8FD694, schwarze Schuhe), Kopf Short 3 (Haar Graubraun #6A5A4E), Haut #D8A27C,
  keine Brille, kein Bart.
Posen der letzten drei Folgen (145: resting-1, easing-1, crossed_arms-1, blazer-3; 146: resting-1, crossed_arms-1; 147:
pointing_finger-2, easing-2) nicht verwendet; keine Polka Dots, keine Prothesen-Posen (blazer-1/-2, shirt-1/-2), keine Bärte,
keine Karikatur. Präfixe HD_/VO_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und
blickt nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Suspicious, Fear, Tired, Smile, Solemn bzw.
„Augen|geschlossener Mund“ (Concerned|Serious, Rage|Serious). Sprechende Ansichten HD_redet, VO_redet (und Lexi) zusätzlich
mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_149")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "HD": ("standing/blazer-4", "Medium 2", None, None, {"Skin": "#EFC2A0", "Jacket": "#B8A9F5", "Top": "#FFFFFF",
                                                       "Pants": "#2E3550", "Hair": "#8A5E34"}),
    "VO": ("standing/crossed_arms-2", "Short 3", None, None, {"Skin": "#D8A27C", "Pants": "#8FD694", "Hair": "#6A5A4E"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("HD_ruhig", "HD", "Calm", 0), ("HD_schreck", "HD", "Fear", 0), ("HD_redet", "HD", "Rage|Serious", 1),
    ("HD_ernst", "HD", "Serious", 0), ("HD_skeptisch", "HD", "Suspicious", 0), ("HD_sorge", "HD", "Concerned|Serious", 0),
    ("HD_froh", "HD", "Smile", 0), ("HD_still", "HD", "Solemn", 0),
    ("VO_ruhig", "VO", "Calm", 0), ("VO_schreck", "VO", "Fear", 0), ("VO_redet", "VO", "Suspicious", 1),
    ("VO_ernst", "VO", "Serious", 0), ("VO_denkt", "VO", "Suspicious", 0), ("VO_sorge", "VO", "Concerned|Serious", 0),
    ("VO_muede", "VO", "Tired", 0), ("VO_still", "VO", "Solemn", 0),
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
