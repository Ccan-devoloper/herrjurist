"""Figuren für Folge 211 (Fall Gäfgen) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv; die realen
Beteiligten (Beschuldigter, Polizisten, Richter) werden NICHT dargestellt und nicht benannt. Das Kind erscheint nie.
Herr Wallmann (WA, Ende 20, Beschuldigter; spricht nicht): standing/resting-1 (Pullover Petrol #5FA8A0, schwarze Hose der Pose),
  Kopf Short 3 (Haar #4A3426), Haut #F2D3B8, kein Bart – gewöhnlicher junger Mann, keine „fiese“ Täterfigur, keine Fesseln.
Herr Rombach (RO, um 60, stellvertretender Polizeipräsident; Stimme william): standing/blazer-3 (Anzug Anthrazit #4A4A55,
  Hose #2B2B35), Kopf No Hair 1, Brille Glasses 3, Haut #E8B48F.
Kommissar Leitner (LE, um 45; Stimme marc): standing/shirt-4 (schwarzes Hemd der Pose, Hose Graublau #5A6A80), Kopf Short 5
  (Haar #6B4A35), Haut #E3B08C. Keine Waffe, kein Werkzeug, keine Uniformabzeichen.
Verteidigerin (VE, um 45; Stimme sabrina): standing/pointing_finger-1 (erhobener Zeigefinger; Oberteil Schwarz #2B2B2B wie eine
  Robe), Kopf Medium Bangs 2 (Haar #3A2A20), Brille Glasses 2, Haut #F1C9A5.
Vorsitzende Richterin (RI, um 55; Stimme laura_ruhig): standing/robot_dance-2 (schwarzes Oberteil der Pose wie eine Robe, Hose
  #3A3A44), Kopf Gray Medium (Haar #A8A8A8), Brille Glasses, Haut #E9BC9A; steht hinter dem Richtertisch.
Posen nicht aus 208–210 (blazer-1/-2/-4, robot_dance-3, walking-2, easing-2, pointing_finger-2, shirt-3, crossed_arms-1/-2);
keine Polka Dots, keine Bärte, keine Prothesen-Posen, keine Sitz-/Kniepose für den Beschuldigten.
Präfix WA_/RO_/LE_/VE_/RI_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt
nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (RO_redet, LE_redet, VE_redet, RI_redet,
Lexi) zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_211")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "WA": ("standing/resting-1", "Short 3", None, None, {"Skin": "#F2D3B8", "Top": "#5FA8A0", "Hair": "#4A3426"}),
    "RO": ("standing/blazer-3", "No Hair 1", None, "Glasses 3", {"Skin": "#E8B48F", "Jacket": "#4A4A55", "Pants": "#2B2B35"}),
    "LE": ("standing/shirt-4", "Short 5", None, None, {"Skin": "#E3B08C", "Pants": "#5A6A80", "Hair": "#6B4A35"}),
    "VE": ("standing/pointing_finger-1", "Medium Bangs 2", None, "Glasses 2", {"Skin": "#F1C9A5", "Top": "#2B2B2B",
                                                                                "Hair": "#3A2A20"}),
    "RI": ("standing/robot_dance-2", "Gray Medium", None, "Glasses", {"Skin": "#E9BC9A", "Pants": "#3A3A44", "Hair": "#A8A8A8"}),
}

LISTE = [
    ("WA_ruhig", "WA", "Calm", 0), ("WA_ernst", "WA", "Serious", 0), ("WA_sorge", "WA", "Concerned|Serious", 0),
    ("WA_angst", "WA", "Fear", 0), ("WA_muede", "WA", "Tired", 0), ("WA_reue", "WA", "Solemn", 0),
    ("WA_denkt", "WA", "Suspicious", 0),
    ("RO_ernst", "RO", "Serious", 0), ("RO_redet", "RO", "Serious", 1), ("RO_drang", "RO", "Driven", 0),
    ("RO_muede", "RO", "Tired", 0), ("RO_feierlich", "RO", "Solemn", 0), ("RO_sorge", "RO", "Concerned|Serious", 0),
    ("LE_ernst", "LE", "Serious", 0), ("LE_redet", "LE", "Serious", 1), ("LE_sorge", "LE", "Concerned|Serious", 0),
    ("LE_muede", "LE", "Tired", 0), ("LE_feierlich", "LE", "Solemn", 0),
    ("VE_ruhig", "VE", "Calm", 0), ("VE_redet", "VE", "Serious", 1), ("VE_denkt", "VE", "Suspicious", 0),
    ("VE_froh", "VE", "Smile", 0), ("VE_ernst", "VE", "Serious", 0),
    ("RI_ruhig", "RI", "Calm", 0), ("RI_redet", "RI", "Calm", 1), ("RI_ernst", "RI", "Serious", 0),
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
