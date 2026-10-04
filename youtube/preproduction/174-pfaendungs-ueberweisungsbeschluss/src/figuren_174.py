"""Figuren für Folge 174 (Pfändungs- und Überweisungsbeschluss) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle fiktiv.
Herr Dorfmann (DO, um 45, Tischler, Gläubiger; Stimme christian): standing/crossed_arms-1 (Oberteil Holzbraun #C9A27A, schwarze
Hose), Kopf Short 1, Haut #D9A07A, ohne Bart, ohne Brille.
Frau Kästner (KA, um 30, Angestellte im Autowerk, Schuldnerin; Stimme lucy): standing/resting-2 (schwarzes Oberteil, Hose
Rosa #F4A6C0), Kopf Long Bangs, Haut #F2D3B8. robot_dance-3 verworfen: gleiche Haltung wie Lexi (ausgestreckte Hand).
Die Personalleiterin (PL, um 60, ohne Namen, Drittschuldnerin Arbeitgeber; Stimme hilde): standing/shirt-4 (schwarze Bluse, Hose
Petrol #5FA8A0), Kopf Gray Medium, Brille Glasses 4, Haut #E8B98F.
Der Bankberater (BB, um 40, ohne Namen, spricht nicht): standing/crossed_arms-2 (schwarzes Oberteil, Hose Grau #6B6B78), Kopf
Short 2, Brille Glasses, Haut #C99470.
Posen nicht aus 171–173 (easing-1, blazer-3, pointing_finger-2, blazer-1, sitting/bike, shirt-3, easing-2, robot_dance-2,
resting-1, blazer-4); keine Prothesen-Posen, keine Polka Dots, keine Bärte. Präfix DO_/KA_/PL_/BB_ (nie ER_).
Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (blickt nach links), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Suspicious, Smile, Fear, Driven bzw.
Concerned|Serious. Sprechende Ansichten (DO_redet, KA_klagt, KA_redet, PL_redet, Lexi) zusätzlich mit a/o/e: Augen der
Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 % der Gesichtshöhe."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_174")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "DO": ("standing/crossed_arms-1", "Short 1", None, None, {"Skin": "#D9A07A", "Top": "#C9A27A"}),
    "KA": ("standing/resting-2", "Long Bangs", None, None, {"Skin": "#F2D3B8", "Pants": "#F4A6C0"}),
    "PL": ("standing/shirt-4", "Gray Medium", None, "Glasses 4", {"Skin": "#E8B98F", "Pants": "#5FA8A0"}),
    "BB": ("standing/crossed_arms-2", "Short 2", None, "Glasses", {"Skin": "#C99470", "Pants": "#6B6B78"}),
}

LISTE = [
    ("DO_ruhig", "DO", "Calm", 0), ("DO_redet", "DO", "Serious", 1), ("DO_denkt", "DO", "Suspicious", 0),
    ("DO_froh", "DO", "Smile", 0), ("DO_bestimmt", "DO", "Driven", 0), ("DO_sorge", "DO", "Concerned|Serious", 0),
    ("KA_ruhig", "KA", "Calm", 0), ("KA_klagt", "KA", "Concerned|Serious", 1), ("KA_redet", "KA", "Calm", 1),
    ("KA_sorge", "KA", "Concerned|Serious", 0), ("KA_schreck", "KA", "Fear", 0), ("KA_denkt", "KA", "Suspicious", 0),
    ("KA_froh", "KA", "Smile", 0),
    ("PL_ruhig", "PL", "Calm", 0), ("PL_redet", "PL", "Serious", 1), ("PL_denkt", "PL", "Suspicious", 0),
    ("PL_froh", "PL", "Smile", 0),
    ("BB_ruhig", "BB", "Calm", 0), ("BB_froh", "BB", "Smile", 0),
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
