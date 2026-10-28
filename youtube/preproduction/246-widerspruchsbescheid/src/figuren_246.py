"""Figuren für Folge 246 (Widerspruchsbescheid schreiben) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv, Behörden fiktiv.
Herr Holzapfel (HO, um 68, Hundehalter und Widerspruchsführer; Stimme william): standing/resting-2 (schwarzer Pullover der
  Pose, Hose Braun #6B5A48), Kopf No Hair 3 (Glatze mit grauem Haarkranz), Brille Glasses 2, Haut #EDBE9C, kein Bart.
Herr Sperling (SP, um 45, Sachbearbeiter der Gemeinde; Stimme marc): standing/crossed_arms-2 (schwarzes Oberteil der Pose,
  Hose Dunkelblau #3A4A6B), Kopf Short 5, Haut #A8714E – sachlich.
Frau Körner (KO, um 28, Referendarin im Landratsamt; Stimme laura_ruhig): standing/blazer-4 (Blazer Lila #B8A9F5, Oberteil
  Weiß, Hose #3D3D48), Kopf Medium Bangs 2, Haut #F0C8A8.
Posen und Kleidung nicht aus 243–245 (blazer-3, walking-2, blazer-2, pointing_finger-1, walking-3, robot_dance-2, shirt-1,
robot_dance-3, crossed_arms-1, resting-1, polka_dots, shirt-4, shirt-3); keine Prothesen-Posen (shirt-1/-2, blazer-1/-2),
keine Polka Dots, keine Bärte. Präfixe HO_/SP_/KO_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht
ist gespiegelt und blickt nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (HO_redet, SP_spricht, KO_fragt, Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_246")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "HO": ("standing/resting-2", "No Hair 3", None, "Glasses 2", {"Skin": "#EDBE9C", "Pants": "#6B5A48"}),
    "SP": ("standing/crossed_arms-2", "Short 5", None, None, {"Skin": "#A8714E", "Pants": "#3A4A6B"}),
    "KO": ("standing/blazer-4", "Medium Bangs 2", None, None, {"Skin": "#F0C8A8", "Jacket": "#B8A9F5", "Top": "#FFFFFF",
                                                             "Pants": "#3D3D48"}),
}

LISTE = [
    ("HO_ruhig", "HO", "Calm", 0), ("HO_froh", "HO", "Smile", 0), ("HO_ernst", "HO", "Serious", 0),
    ("HO_sorge", "HO", "Concerned|Serious", 0), ("HO_denkt", "HO", "Suspicious", 0), ("HO_muede", "HO", "Tired", 0),
    ("HO_entschl", "HO", "Driven", 0),
    ("HO_redet", "HO", "Smile", 1),
    ("SP_ruhig", "SP", "Calm", 0), ("SP_ernst", "SP", "Serious", 0), ("SP_denkt", "SP", "Suspicious", 0),
    ("SP_spricht", "SP", "Serious", 1),
    ("KO_ruhig", "KO", "Calm", 0), ("KO_froh", "KO", "Smile", 0), ("KO_ernst", "KO", "Serious", 0),
    ("KO_denkt", "KO", "Suspicious", 0), ("KO_entschl", "KO", "Driven", 0),
    ("KO_fragt", "KO", "Suspicious", 1),
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
