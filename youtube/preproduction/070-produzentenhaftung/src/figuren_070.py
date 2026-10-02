"""Figuren für Folge 070 (Produzentenhaftung, explodierende Mehrwegflasche) aus der LexVerse-Figma-Bibliothek
(Open Peeps, CC0).
Bettina (Kundin, um 35): standing/robot_dance-3 (ausgestreckte Hand: hält die Flasche bzw. zeigt), blaues Oberteil,
dunkelblaue Hose, Kopf Long, kein Bart; nach dem Unfall mit Augenklappe („Eyepatch“, abstrakt, keine Wunde).
Herr Kroll (Inhaber des Mineralbrunnens, Hersteller, um 55): standing/shirt-3 (Hemd grün, schwarze Hose),
Kopf Gray Short, Brille Glasses 3, kein Bart. Keine Prothesen-Posen (shirt-1/-2, blazer-1/-2 nicht verwendet).
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links (Figur rechts neben der
Tafel), Suffix _r blickt nach rechts. Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF); offene Mimiken nur als
„Augen|Serious/Smile“. Je sprechender Ansicht vier Mundzustände: zu (Grundmimik), a, o, e (lexpeeps 'Augen|Mund',
Schnitt bei 60 % der Gesichtshöhe)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_070")
os.makedirs(ZIEL, exist_ok=True)
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

BE_F = {"Skin": "#E8BE9A", "Top": "#8DB3F2", "Pants": "#4A5A85"}
KR_F = {"Skin": "#E2B08C", "Top": "#8FD694"}
# Ansicht: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "BE_g": ("standing/robot_dance-3", "Long", None, None, BE_F),
    "BE_a": ("standing/robot_dance-3", "Long", None, "Eyepatch", BE_F),
    "KR_s": ("standing/shirt-3", "Gray Short", None, "Glasses 3", KR_F),
}

# (Name, Ansicht, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts).
LISTE = [
    ("BE_ruhig", "BE_g", "Calm", 0), ("BE_froh", "BE_g", "Smile", 0), ("BE_schreck", "BE_g", "Fear", 0),
    ("BE_redet", "BE_a", "Concerned|Serious", 1), ("BE_sorge", "BE_a", "Concerned|Serious", 0),
    ("BE_denkt", "BE_a", "Suspicious", 0), ("BE_ernst", "BE_a", "Serious", 0), ("BE_ok", "BE_a", "Smile", 0),
    ("BE_ruhig2", "BE_a", "Calm", 0),
    ("KR_ruhig", "KR_s", "Calm", 0), ("KR_redet", "KR_s", "Serious", 1), ("KR_denkt", "KR_s", "Suspicious", 0),
    ("KR_sorge", "KR_s", "Concerned|Serious", 0), ("KR_ertappt", "KR_s", "Fear", 0), ("KR_froh", "KR_s", "Smile", 0),
    ("KR_ernst", "KR_s", "Solemn", 0),
]

if __name__ == "__main__":
    n = 0
    for name, v, mimik, mund in LISTE:
        pose, kopf, bart, brille, farben = P[v]
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
