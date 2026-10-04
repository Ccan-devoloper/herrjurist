"""Figuren für Folge 198 (Heimtücke § 211 StGB: Versöhnungsessen) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv, gewöhnlich gekleidet (keine Waffe, kein Werkzeug, keine Klischees).
Heribert (HB, um 60, Täter; Stimme helmut): standing/easing-1 (Jacke Lila #B8A9F5, Oberteil Weiß, schwarze Hose der Pose),
  Kopf Gray Short (Haar Grau #BDBDBD), Haut #E8B894, keine Brille, kein Bart. Keine „fiese“ Mimik (Calm, Serious, Smile, Suspicious, Solemn).
Siegmund (SG, um 40, Geschäftspartner und Opfer; Stimme niklas): standing/resting-1 (Pullover Türkis #7FD6D0, schwarze
  Hose der Pose), Kopf Short 5, Haut #D9A27A.
Posen der letzten drei Folgen (194: robot_dance-3, blazer-3; 195: pointing_finger-2, crossed_arms-1, blazer-3;
196: robot_dance-2, blazer-4, crossed_arms-2) nicht verwendet; Lexi-Posen (robot_dance-1) nicht für Fallfiguren; keine
Polka Dots, keine Bärte, keine Prothesen-Posen, keine Karikatur. Präfixe HB_/SG_ (nie ER_).
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Suspicious, Solemn, Smile, Driven bzw.
„Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten HB_redet, SG_redet (und Lexi) zusätzlich mit a/o/e:
Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_198")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "HB": ("standing/easing-1", "Gray Short", None, None, {"Skin": "#E8B894", "Jacket": "#B8A9F5", "Top": "#FFFFFF", "Hair": "#BDBDBD"}),
    "SG": ("standing/resting-1", "Short 5", None, None, {"Skin": "#D9A27A", "Top": "#7FD6D0"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("HB_ruhig", "HB", "Calm", 0), ("HB_ernst", "HB", "Serious", 0), ("HB_denkt", "HB", "Suspicious", 0),
    ("HB_still", "HB", "Solemn", 0), ("HB_laechelt", "HB", "Smile", 0), ("HB_streit", "HB", "Concerned|Serious", 0),
    ("HB_redet", "HB", "Smile", 1),
    ("SG_ruhig", "SG", "Calm", 0), ("SG_froh", "SG", "Smile", 0), ("SG_streit", "SG", "Concerned|Serious", 0),
    ("SG_denkt", "SG", "Suspicious", 0), ("SG_ernst", "SG", "Serious", 0),
    ("SG_redet", "SG", "Smile", 1),
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
