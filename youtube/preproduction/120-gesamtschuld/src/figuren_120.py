"""Figuren für Folge 120 (Gesamtschuld §§ 421, 426 BGB, Stromrechnung der Wohngemeinschaft) aus der LexVerse-Figma-Bibliothek
(Open Peeps, CC0). Alle Figuren fiktiv.
Insa (um 25, Mitbewohnerin, zahlt die 900 €; Stimme ela_froh): standing/pointing_finger-1 (schwarzes Langarmoberteil, schwarze
Hose und Stiefel der Pose – die Pose hat keine umfärbbare Oberteilfläche; zeigt mit dem Finger), Kopf Medium 2, Haut #F0C8A8.
Lars (um 26, Mitbewohner, soll ausgleichen; Stimme niklas): standing/crossed_arms-1 (Pullover Blau #8DB3F2, schwarze Hose,
verschränkte Arme), Kopf Short 3, Haar #6B4A32, Haut #E3B48E, kein Bart.
Rieke (um 24, ausgezogene Mitbewohnerin, zahlungsunfähig; spricht nicht): standing/walking-2 (schwarzes T-Shirt der Pose, Hose
Lila #B8A9F5, Schrittpose beim Auszug), Kopf Medium Straight, Haut #F2D3B8.
Sachbearbeiter des Stromversorgers (um 60, Funktionsrolle ohne Namen; Stimme helmut): standing/blazer-4 (Blazer Grün #8FD694,
weißes Oberteil, schwarze Hose), Kopf Gray Short, Brille Glasses 3, Haut #D9A47E; sachlich, keine „fiese“ Gläubigerfigur.
Keine Bärte, keine Prothesen-Posen, keine Karikatur, keine Herkunfts- oder Hautfarbenzuschreibung; die zahlungsunfähige Rieke
ist keine Täterin und wird neutral gezeigt. Posen nicht aus 117–119 (shirt-4, pointing_finger-2, robot_dance-3, resting-1,
crossed_arms-2, easing-2, blazer-3) und nicht aus der WG-Folge 107 (shirt-3, resting-2, blazer-3); keine Polka Dots.
Präfix IN_/LA_/RI_/SB_ (nie ER_). Grundansicht gespiegelt (blickt nach links), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md); sprechende Ansichten IN_redet, LA_redet, SB_redet und Lexi
zusätzlich mit a/o/e (Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_120")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "IN": ("standing/pointing_finger-1", "Medium 2", None, None, {"Skin": "#F0C8A8"}),
    "LA": ("standing/crossed_arms-1", "Short 3", None, None, {"Skin": "#E3B48E", "Top": "#8DB3F2", "Hair": "#6B4A32"}),
    "RI": ("standing/walking-2", "Medium Straight", None, None, {"Skin": "#F2D3B8", "Pants": "#B8A9F5"}),
    "SB": ("standing/blazer-4", "Gray Short", None, "Glasses 3", {"Skin": "#D9A47E", "Jacket": "#8FD694", "Top": "#FFFFFF"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("IN_ruhig", "IN", "Calm", 0), ("IN_redet", "IN", "Serious", 1), ("IN_froh", "IN", "Smile", 0),
    ("IN_sorge", "IN", "Concerned|Serious", 0), ("IN_denkt", "IN", "Suspicious", 0), ("IN_staunt", "IN", "Awe", 0),
    ("LA_ruhig", "LA", "Calm", 0), ("LA_redet", "LA", "Serious", 1), ("LA_froh", "LA", "Smile", 0),
    ("LA_denkt", "LA", "Suspicious", 0), ("LA_sorge", "LA", "Concerned|Serious", 0),
    ("RI_ruhig", "RI", "Calm", 0), ("RI_sorge", "RI", "Concerned|Serious", 0), ("RI_traurig", "RI", "Tired", 0),
    ("SB_ruhig", "SB", "Calm", 0), ("SB_redet", "SB", "Serious", 1), ("SB_froh", "SB", "Smile", 0),
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
