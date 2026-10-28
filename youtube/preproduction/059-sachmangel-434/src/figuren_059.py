"""Figuren für Folge 059 (Sachmangel § 434 BGB) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Kerstin (Käuferin, Verbraucherin, um 40): nur standing/polka_dots (gepunktete Bluse, Hose Lila),
Kopf Medium Straight, kein Bart. Herr Kranich (Inhaber des Computerladens, um 45): nur standing/crossed_arms-2 (verschränkte
Arme; schwarzes Oberteil, Hose Blau), Kopf Short 3, Brille Glasses 2, kein Bart.
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links (Figur rechts neben der
Tafel), Suffix _r blickt nach rechts. Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF); offene Mimiken nur als
„Augen|Smile/Serious“. Je sprechender Ansicht vier Mundzustände: zu (Grundmimik), a, o, e (lexpeeps 'Augen|Mund',
Schnitt bei 60 % der Gesichtshöhe). Keine Bärte, keine Prothesen-Posen."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_059")
os.makedirs(ZIEL, exist_ok=True)
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

KE_F = {"Skin": "#F2C9A5", "Pants": "#B8A9F5"}
KR_F = {"Skin": "#E0A47E", "Pants": "#8DB3F2"}
# Person: (Pose, Kopf, Bart, Brille, Farben, Grundansicht gespiegelt?)
P = {
    "KE": ("standing/polka_dots", "Medium Straight", None, None, KE_F, 1),
    "KR": ("standing/crossed_arms-2", "Short 3", None, "Glasses 2", KR_F, 1),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts).
LISTE = [
    ("KE_ruhig", "KE", "Calm", 0), ("KE_froh", "KE", "Smile Big|Smile", 0), ("KE_redet", "KE", "Smile", 1),
    ("KE_aerger", "KE", "Very Angry", 1), ("KE_denkt", "KE", "Serious", 0), ("KE_ueberlegt", "KE", "Suspicious", 0),
    ("KE_sorge", "KE", "Concerned|Serious", 0),
    ("KR_ruhig", "KR", "Calm", 0), ("KR_froh", "KR", "Smile", 0), ("KR_redet", "KR", "Smile", 1),
    ("KR_denkt", "KR", "Suspicious", 0), ("KR_ernst", "KR", "Serious", 0), ("KR_sorge", "KR", "Concerned|Serious", 0),
]

if __name__ == "__main__":
    n = 0
    for name, p, mimik, mund in LISTE:
        pose, kopf, bart, brille, farben, sp = P[p]
        for suffix, gespiegelt in (("", sp), ("_r", 1 - sp)):
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
