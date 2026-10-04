"""Figuren für Folge 179 (Besitzkonstitut & Co.; Auto des Nachbarn) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv, Erwachsene in Alltagskleidung, keine Marken.
Käthe (KA, um 30, Käuferin; Stimme sabrina): standing/blazer-4 (Blazer Blau #8DB3F2, Oberteil Weiß, schwarze Hose),
  Kopf Medium Bangs 2 (Haar Kastanienbraun #8B5A2B), Haut #F3CDB0, keine Brille.
Herr Wöhler (WO, um 45, Nachbar und Verkäufer; Stimme marc): standing/shirt-3 (Hemd Grün #8FD694, schwarze Hose), Kopf Short 5, Brille Glasses, Haut #D9A07A, kein Bart.
Werkstattmeisterin (WM, um 50, Fall 3; spricht nicht; Schild „Werkstatt“): standing/crossed_arms-2 (schwarzes Oberteil,
  Arbeitshose Orange #F9A66C), Kopf Bun, Haut #C99470.
Posen der letzten drei Folgen (176: blazer-1, pointing_finger-2; 177: blazer-3, robot_dance-2; 178: noch ohne Figuren;
robot_dance-3 verworfen, weil zu ähnlich wie Lexi)
nicht verwendet; robot_dance-1 bleibt Lexi; keine Polka Dots, keine Prothesen-Posen (blazer-1/-2, shirt-1/-2), keine
Bärte, keine Karikatur. Präfixe KA_/WO_/WM_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist
gespiegelt und blickt nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten KA_redet, WO_redet (und Lexi) zusätzlich mit
a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_179")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "KA": ("standing/blazer-4", "Medium Bangs 2", None, None, {"Skin": "#F3CDB0", "Jacket": "#8DB3F2", "Top": "#FFFFFF",
                                                               "Hair": "#8B5A2B"}),
    "WO": ("standing/shirt-3", "Short 5", None, "Glasses", {"Skin": "#D9A07A", "Top": "#8FD694"}),
    "WM": ("standing/crossed_arms-2", "Bun", None, None, {"Skin": "#C99470", "Pants": "#F9A66C"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("KA_ruhig", "KA", "Calm", 0), ("KA_redet", "KA", "Smile", 1), ("KA_froh", "KA", "Smile", 0),
    ("KA_denkt", "KA", "Suspicious", 0), ("KA_sorge", "KA", "Concerned|Serious", 0), ("KA_ernst", "KA", "Serious", 0),
    ("WO_ruhig", "WO", "Calm", 0), ("WO_redet", "WO", "Smile", 1), ("WO_froh", "WO", "Smile", 0),
    ("WO_denkt", "WO", "Suspicious", 0), ("WO_sorge", "WO", "Concerned|Serious", 0), ("WO_ernst", "WO", "Serious", 0),
    ("WM_ruhig", "WM", "Calm", 0), ("WM_ernst", "WM", "Serious", 0), ("WM_froh", "WM", "Smile", 0),
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
