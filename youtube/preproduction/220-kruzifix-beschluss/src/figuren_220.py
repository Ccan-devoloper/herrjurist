"""Figuren für Folge 220 (Kruzifix-Beschluss) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv; die
realen Beschwerdeführer des Ausgangsverfahrens werden weder dargestellt noch benannt.
Herr Rohde (RO, um 38, Vater; Stimme niklas): standing/robot_dance-2 (schwarzes Oberteil der Pose, Hose Sand #D9B38C),
  Kopf Short 3 (Haar #6B4A2E), Haut #EBC3A0 – höflich, besorgt, nie aggressiv.
Frau Rohde (FR, um 36, Mutter; spricht nicht): standing/walking-3 (schwarze Kleidung der Pose, nicht einfärbbar), Kopf Long
  (Haar #3A2A20), Haut #D9A884.
Herr Kampe (KA, um 60, Schulleiter; Stimme helmut): standing/blazer-4 (Sakko Blau #8DB3F2, Hemd Weiß, schwarze Hose),
  Kopf Gray Short (Haar #A8A8A8), Brille Glasses 4, Haut #F0CDB2 – sachlich, freundlich, nicht abweisend.
Sohn der Rohdes (SO, 7 Jahre; spricht nicht, ohne Namen): standing/resting-1 (Pullover Grün #8FD694,
  schwarze Hose), Kopf Short 2 (Haar #8A5A2B), Haut #EBC3A0; im Bild über `hoehe` auf etwa 58 % der Erwachsenenhöhe.
Mitschüler K1, K2 (7 Jahre; sprechen nicht): standing/pointing_finger-1 (Pullover Lila #B8A9F5; Kopf Bun 2 ohne Band,
  Haar #1F1A17), standing/crossed_arms-2 (schwarzes Oberteil, Hose Blau #8DB3F2; Kopf Bangs, Haar #C98E4E).
Posen nicht aus 217–219 (blazer-3, shirt-4, crossed_arms-1, resting-2, walking-1, easing-1, shirt-3, pointing_finger-2,
sitting/one_leg_up-1, easing-2, robot_dance-3, walking-2). robot_dance-1 bleibt Lexi; keine Polka Dots, keine
Prothesen-Posen (blazer-1/-2, shirt-1/-2), keine Bärte. Präfixe RO_/FR_/KA_/SO_/K1_/K2_ (nie ER_).
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links, Suffix _r nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (RO_redet, KA_redet, KA_redet2, Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_220")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "RO": ("standing/robot_dance-2", "Short 3", None, None, {"Skin": "#EBC3A0", "Pants": "#D9B38C", "Hair": "#6B4A2E"}),
    "FR": ("standing/walking-3", "Long", None, None, {"Skin": "#D9A884", "Hair": "#3A2A20"}),
    "KA": ("standing/blazer-4", "Gray Short", None, "Glasses 4", {"Skin": "#F0CDB2", "Jacket": "#8DB3F2", "Top": "#FFFFFF",
                                                                  "Hair": "#A8A8A8"}),
    "SO": ("standing/resting-1", "Short 2", None, None, {"Skin": "#EBC3A0", "Top": "#8FD694", "Hair": "#8A5A2B"}),
    "K1": ("standing/pointing_finger-1", "Bun 2", None, None, {"Skin": "#B07552", "Top": "#B8A9F5", "Hair": "#1F1A17",
                                                               "bandana": "#1F1A17"}),
    "K2": ("standing/crossed_arms-2", "Bangs", None, None, {"Skin": "#F2D3B8", "Pants": "#8DB3F2", "Hair": "#C98E4E"}),
}

LISTE = [
    ("RO_ruhig", "RO", "Smile", 0), ("RO_sorge", "RO", "Concerned|Serious", 0), ("RO_redet", "RO", "Serious", 1),
    ("RO_froh", "RO", "Calm", 0), ("RO_denkt", "RO", "Tired", 0),
    ("FR_ruhig", "FR", "Smile", 0), ("FR_sorge", "FR", "Concerned|Serious", 0), ("FR_froh", "FR", "Calm", 0),
    ("KA_ruhig", "KA", "Smile", 0), ("KA_redet", "KA", "Calm", 1), ("KA_ernst", "KA", "Serious", 0),
    ("KA_denkt", "KA", "Tired", 0), ("KA_redet2", "KA", "Smile", 1),
    ("SO_ruhig", "SO", "Calm", 0), ("SO_froh", "SO", "Cute", 0), ("SO_sorge", "SO", "Concerned|Serious", 0),
    ("K1_froh", "K1", "Smile", 0), ("K1_ruhig", "K1", "Calm", 0),
    ("K2_froh", "K2", "Cute", 0), ("K2_ruhig", "K2", "Calm", 0),
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
    for name, (pose, mimik) in {"LX_erklaert": ("standing/robot_dance-1", "Smile"), "LX_warnt": ("standing/robot_dance-1", "Serious")}.items():
        a = LX.AUSSEHEN
        for k, g in {"": mimik, **{"_" + k: f"{mimik}|{m}" for k, m in MUND.items()}}.items():
            figur(pose, a["kopf"], g, a["bart"], a["brille"], a["farben"], hoehe=1200, spiegeln=True).save(f"{ZIEL}/{name}{k}.png"); n += 1
    print(n, "Figurenbilder ->", ZIEL)
