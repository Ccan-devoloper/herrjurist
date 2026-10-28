"""Figuren für Folge 217 (Kopftuch-Urteil) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv; die
realen Beschwerdeführerinnen werden weder dargestellt noch benannt.
Frau Sander (SA, um 30, Mathematiklehrerin; Stimme lucy): standing/blazer-3 (Blazer Lila #B8A9F5, Hose Dunkelblau #3D3D58),
  Kopf Hijab (Open-Peeps-Kopfteil „Hijab“, unverändert: schwarzes Tuch, Unterband Lila #B8A9F5), Haut #C98E66 –
  freundlich, kompetent, kein Klischee; immer dieselbe Kleidung.
Herr Steffens (ST, um 55, Schulleiter; Stimme stephan): standing/shirt-4 (schwarzes Hemd der Pose, Hose Hellblau #8DB3F2),
  Kopf Short 1 (Haar Grau #8A8A8A), Brille Glasses 3, Haut #E3B08C – sachlich, neutral.
Herr Röder (RD, um 45, Vater eines Schülers; Stimme christian): standing/crossed_arms-1 (Pullover Türkis #7FD6D0, schwarze
  Hose), Kopf Short 4 (Haar #5A3A22), Haut #F0C8A8 – besorgt, nicht feindselig.
Drei Kinder der Klasse 8b (K1–K3, um 13; sprechen nicht): standing/resting-2 (Kopf Buns), standing/walking-1 (Kopf Short 2,
  Röders Sohn), standing/easing-1 (Kopf Medium 2); im Bild über `hoehe` auf etwa 68 % der Erwachsenenhöhe skaliert.
Rechtsreferendarin (RF, um 27, spricht nicht): standing/shirt-3 (Bluse Grün #8FD694, schwarze Hose), Kopf Hijab (Unterband
  Grün), Haut #E0AC84.
Vorsitzende Richterin (RI, um 60, Ausbilderin; Stimme hilde): standing/pointing_finger-2 (schwarzes Oberteil der Pose wie
  eine Robe, Hose #3A3A44), Kopf Gray Medium (Haar #B4B4B4), Brille Glasses, Haut #F0CDB2; hinter dem Richtertisch.
Posen nicht aus 212–215 (blazer-4, resting-2, robot_dance-3, easing-1, walking-2, shirt-1, easing-2, walking-1/-3,
robot_dance-2, resting-1, crossed_arms-2) für die Hauptfiguren; die Kinder sind Nebenfiguren. robot_dance-1 bleibt Lexi; keine
Polka Dots, keine Prothesen-Posen (blazer-1/-2, shirt-1/-2), keine Bärte. Präfixe SA_/ST_/RD_/K1_/K2_/K3_/RF_/RI_ (nie ER_).
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links, Suffix _r nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (SA_redet, ST_redet, ST_redet2, RD_redet,
RI_redet, Lexi) zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_217")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "SA": ("standing/blazer-3", "Hijab", None, None, {"Skin": "#C98E66", "Jacket": "#B8A9F5", "Pants": "#3D3D58",
                                                     "hijab": "#B8A9F5"}),
    "ST": ("standing/shirt-4", "Short 1", None, "Glasses 3", {"Skin": "#E3B08C", "Pants": "#8DB3F2", "Hair": "#8A8A8A"}),
    "RD": ("standing/crossed_arms-1", "Short 4", None, None, {"Skin": "#F0C8A8", "Top": "#7FD6D0", "Hair": "#5A3A22"}),
    "K1": ("standing/resting-2", "Buns", None, None, {"Skin": "#E8B894", "Pants": "#F07A6A", "Hair": "#3A2A20"}),
    "K2": ("standing/walking-1", "Short 2", None, None, {"Skin": "#F2D3B8", "Top": "#F9D56E", "Hair": "#8A5A2B"}),
    "K3": ("standing/easing-1", "Medium 2", None, None, {"Skin": "#B07552", "Jacket": "#8DB3F2", "Top": "#FFFFFF",
                                                       "Hair": "#1F1A17"}),
    "RF": ("standing/shirt-3", "Hijab", None, None, {"Skin": "#E0AC84", "Top": "#8FD694", "hijab": "#8FD694"}),
    "RI": ("standing/pointing_finger-2", "Gray Medium", None, "Glasses", {"Skin": "#F0CDB2", "Pants": "#3A3A44",
                                                                         "Hair": "#B4B4B4"}),
}

LISTE = [
    ("SA_ruhig", "SA", "Smile", 0), ("SA_froh", "SA", "Calm", 0), ("SA_strahlt", "SA", "Smile Big|Smile", 0),
    ("SA_entschl", "SA", "Driven", 0), ("SA_betroffen", "SA", "Solemn", 0), ("SA_redet", "SA", "Driven", 1),
    ("ST_ruhig", "ST", "Smile", 0), ("ST_ernst", "ST", "Serious", 0), ("ST_redet", "ST", "Serious", 1),
    ("ST_froh", "ST", "Calm", 0), ("ST_redet2", "ST", "Smile", 1), ("ST_bedauert", "ST", "Tired", 0),
    ("RD_sorge", "RD", "Concerned|Serious", 0), ("RD_redet", "RD", "Serious", 1), ("RD_ruhig", "RD", "Smile", 0),
    ("RD_denkt", "RD", "Tired", 0),
    ("K1_froh", "K1", "Smile", 0), ("K1_ruhig", "K1", "Calm", 0),
    ("K2_froh", "K2", "Cute", 0), ("K2_ruhig", "K2", "Calm", 0),
    ("K3_froh", "K3", "Smile", 0), ("K3_ruhig", "K3", "Calm", 0),
    ("RF_ruhig", "RF", "Smile", 0), ("RF_froh", "RF", "Calm", 0), ("RF_sorge", "RF", "Concerned|Serious", 0),
    ("RF_denkt", "RF", "Solemn", 0),
    ("RI_ruhig", "RI", "Smile", 0), ("RI_redet", "RI", "Smile", 1), ("RI_ernst", "RI", "Serious", 0),
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
