"""Figuren für Folge 058 (Eigenverantwortliche Selbstgefährdung) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Achim (Freund, um 35): standing/easing-1, Kopf Short 1, Oberteil Blau, Jacke Grün, Haut #E8B894.
Udo (erfahrener Konsument, Mitte 50): standing/shirt-4, Kopf Gray Short, Brille Glasses, Hose Lila, Haut #F0C8A8.
Keine Bärte, keine Prothesen, keine Karikaturen, kein Klischee (Udo ordentlich gekleidet, kein „Junkie“-Bild).
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links, Suffix _r nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF): Calm, Serious, Smile, Suspicious, Fear, Tired, Solemn bzw.
„Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten zusätzlich mit a/o/e (Augen der Grundmimik +
Mund Explaining/Concerned Fear/Hectic, Schnitt bei 60 % der Gesichtshöhe)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_058")
os.makedirs(ZIEL, exist_ok=True)
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

AC_F = {"Skin": "#E8B894", "Top": "#8DB3F2", "Jacket": "#8FD694"}
UD_F = {"Skin": "#F0C8A8", "Pants": "#B8A9F5"}

# Ansicht: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "AC": ("standing/easing-1", "Short 1", None, None, AC_F),
    "UD": ("standing/shirt-4", "Gray Short", None, "Glasses", UD_F),
}

# (Name, Ansicht, Grundmimik, mit Mundzuständen)
LISTE = [
    ("AC_ruhig", "AC", "Calm", 0), ("AC_redet", "AC", "Concerned|Serious", 1), ("AC_sorge", "AC", "Concerned|Serious", 0),
    ("AC_denkt", "AC", "Serious", 0), ("AC_weiss", "AC", "Suspicious", 0), ("AC_angst", "AC", "Fear", 0),
    ("AC_ernst", "AC", "Solemn", 0), ("AC_froh", "AC", "Smile", 0),
    ("UD_ruhig", "UD", "Calm", 0), ("UD_redet", "UD", "Smile", 1), ("UD_froh", "UD", "Smile", 0),
    ("UD_denkt", "UD", "Serious", 0), ("UD_muede", "UD", "Tired", 0), ("UD_fragt", "UD", "Concerned|Serious", 0),
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
