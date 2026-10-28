"""Figuren für Folge 214 (Notwehr bei Bagatellen) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv.
Herr Gehrke (GE, 68, Obstbauer; Stimme helmut): standing/easing-2 (offenes Arbeitshemd Olivgrün #7E9C5E über schwarzem
  Oberteil der Pose, Hose Braun #6B5A48), Kopf hat-hip (Hut), Haut #E8B894, kein Bart, keine Brille. Grundmimik „Old“.
Jannes (JA, 16; Stimme niklas): standing/walking-1 (T-Shirt Blau #8DB3F2, schwarze Hose der Pose), Kopf Medium 1
  (Haar #8A5A2B), Haut #F1CBA6 – sympathischer Jugendlicher, kein Klischee.
Paulina (PA, 16; Stimme ela_froh): standing/walking-3 (schwarzes T-Shirt und Hose der Pose), Kopf Buns (Haar #5A3A22),
  Haut #E3B48C.
Jugendliche etwas kleiner als Erwachsene (über hoehe im Folienskript, ca. 92–95 %).
Posen nicht aus 211–213 (resting-1/-2, blazer-3/-4, shirt-1, shirt-4, pointing_finger-1, robot_dance-2/-3, easing-1,
walking-2); keine Polka Dots, keine Bärte, keine Prothesen-Posen. Keine Waffe, kein Werkzeug in der Hand.
Präfix GE_/JA_/PA_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach
links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (GE_redet, GE_ruft, JA_ruft, PA_redet, Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_214")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "GE": ("standing/easing-2", "hat-hip", None, None, {"Skin": "#E8B894", "Jacket": "#7E9C5E", "Pants": "#6B5A48"}),
    "JA": ("standing/walking-1", "Medium 1", None, None, {"Skin": "#F1CBA6", "Top": "#8DB3F2", "Hair": "#8A5A2B"}),
    "PA": ("standing/walking-3", "Buns", None, None, {"Skin": "#E3B48C", "Hair": "#5A3A22"}),
}

LISTE = [
    ("GE_alt", "GE", "Old", 0), ("GE_ruhig", "GE", "Calm", 0), ("GE_wuetend", "GE", "Very Angry", 0),
    ("GE_ernst", "GE", "Serious", 0), ("GE_sorge", "GE", "Concerned|Serious", 0), ("GE_denkt", "GE", "Suspicious", 0),
    ("GE_muede", "GE", "Tired", 0), ("GE_feierlich", "GE", "Solemn", 0),
    ("GE_ruft", "GE", "Very Angry", 1), ("GE_redet", "GE", "Serious", 1),
    ("JA_froh", "JA", "Smile", 0), ("JA_ruhig", "JA", "Calm", 0), ("JA_angst", "JA", "Fear", 0),
    ("JA_sorge", "JA", "Concerned|Serious", 0), ("JA_ernst", "JA", "Serious", 0), ("JA_muede", "JA", "Tired", 0),
    ("JA_denkt", "JA", "Suspicious", 0), ("JA_ruft", "JA", "Fear", 1),
    ("PA_froh", "PA", "Smile", 0), ("PA_ruhig", "PA", "Calm", 0), ("PA_angst", "PA", "Fear", 0),
    ("PA_sorge", "PA", "Concerned|Serious", 0), ("PA_ernst", "PA", "Serious", 0), ("PA_denkt", "PA", "Suspicious", 0),
    ("PA_redet", "PA", "Smile", 1),
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
