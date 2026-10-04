"""Figuren für Folge 187 (Bagger trifft Stromkabel; reiner Vermögensschaden) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv.
Fiete (FI, um 30, Inhaber eines kleinen Tiefbauunternehmens, fährt selbst den Bagger; Stimme niklas): standing/easing-1
  (offenes Arbeitshemd Orange #F9A66C über weißem Shirt, schwarze Hose, weiße Schuhe), Kopf Short 3 (Haar Dunkelbraun
  #5A3A22), Haut #F0C4A0, keine Brille, kein Bart.
Gotthard (GO, um 60, Chef der Fahrradfabrik; Stimme helmut): standing/pointing_finger-1 (dunkler Pullover, dunkle Hose,
  schwarze Schuhe – die Pose hat keine einfärbbare Kleidung), Kopf Gray Short (Haar Grau #C9C9C9), Brille Glasses 3,
  Haut #D9A27A, kein Bart.
Posen der letzten drei Folgen (184: sitting/mid-2, blazer-1; 185: resting-2, closed_legs-2, walking-1, walking-2,
crossed_arms-2, shirt-4, robot_dance-2, mid-1; 186: easing-2, doctor-nurse-01, resting-1, blazer-3) nicht verwendet, auch nicht
deren Farbpaare (blazer-2, crossed_arms-1); robot_dance-1 bleibt Lexi; keine Polka Dots, keine Prothesen-Posen (shirt-1/-2,
blazer-2 verworfen), keine Bärte, keine Karikatur. Präfixe FI_/GO_ (nie ER_). Alle Posen blicken im Original nach rechts;
die Grundansicht ist gespiegelt und blickt nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Suspicious, Fear, Tired, Smile, Solemn, Very Angry
bzw. „Augen|geschlossener Mund“ (Concerned|Serious, Rage|Serious). Sprechende Ansichten FI_redet, GO_redet (und Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_187")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "FI": ("standing/easing-1", "Short 3", None, None, {"Skin": "#F0C4A0", "Jacket": "#F9A66C", "Top": "#FFFFFF",
                                                        "Hair": "#5A3A22"}),
    "GO": ("standing/pointing_finger-1", "Gray Short", None, "Glasses 3", {"Skin": "#D9A27A", "Hair": "#C9C9C9"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("FI_ruhig", "FI", "Calm", 0), ("FI_schreck", "FI", "Fear", 0), ("FI_redet", "FI", "Concerned|Serious", 1),
    ("FI_ernst", "FI", "Serious", 0), ("FI_denkt", "FI", "Suspicious", 0), ("FI_sorge", "FI", "Concerned|Serious", 0),
    ("FI_froh", "FI", "Smile", 0), ("FI_muede", "FI", "Tired", 0), ("FI_still", "FI", "Solemn", 0),
    ("GO_ruhig", "GO", "Calm", 0), ("GO_schreck", "GO", "Fear", 0), ("GO_redet", "GO", "Rage|Serious", 1),
    ("GO_wut", "GO", "Very Angry", 0), ("GO_ernst", "GO", "Serious", 0), ("GO_skeptisch", "GO", "Suspicious", 0),
    ("GO_sorge", "GO", "Concerned|Serious", 0), ("GO_muede", "GO", "Tired", 0), ("GO_still", "GO", "Solemn", 0),
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
