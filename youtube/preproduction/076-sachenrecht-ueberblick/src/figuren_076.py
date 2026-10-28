"""Figuren für Folge 076 (Sachenrecht Überblick: Handy, Auto, Haus) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv.
Nina (um 30, Käuferin in allen drei Stationen): Reihe „-1“ (farbiges Oberteil Lila, schwarze Hose): standing/resting-1
(ruhig, redet, froh, Schreck), crossed_arms-1 (denkt, Sorge, zufrieden), walking-1 (geht); Kopf Long Curly.
Arne (um 25, verkauft das Handy seiner Schwester): standing/easing-1 (offenes Hemd), Kopf Short 3.
Herr Kuhnert (um 60, verkauft den Gebrauchtwagen seines Schwagers): standing/robot_dance-3 (offene Hand, reicht den
Schlüssel), Oberteil Grau, Hose Blau, Kopf No Hair 1, Glasses 3.
Frau Lohse (um 35, im Grundbuch eingetragene Verkäuferin des Hauses): standing/blazer-4, Blazer Gelb, Kopf Long Bangs.
Keine Bärte, keine Prothesen-Posen (shirt-1/-2, blazer-1/-2 nicht verwendet). Alle Posen blicken im Original nach
rechts; die Grundansicht ist gespiegelt und blickt nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Smile, Suspicious, Fear bzw.
„Augen|geschlossener Mund“ (Smile Big|Smile, Concerned|Serious). Sprechende Ansichten (NI_redet, AR_redet, KU_redet,
LO_redet, Lexi) zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_076")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

NI_F = {"Skin": "#E8B98F", "Top": "#B8A9F5"}
# Person/Pose: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "NI": ("standing/resting-1", "Long Curly", None, None, NI_F),
    "NI_A": ("standing/crossed_arms-1", "Long Curly", None, None, NI_F),
    "NI_W": ("standing/walking-1", "Long Curly", None, None, NI_F),
    "AR": ("standing/easing-1", "Short 3", None, None, {"Skin": "#B07552"}),
    "KU": ("standing/robot_dance-3", "No Hair 1", None, "Glasses 3", {"Skin": "#F0C8A8", "Top": "#9C9CA6", "Pants": "#8DB3F2"}),
    "LO": ("standing/blazer-4", "Long Bangs", None, None, {"Skin": "#D9A07A", "Jacket": "#F9D56E"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("NI_ruhig", "NI", "Calm", 0), ("NI_redet", "NI", "Serious", 1), ("NI_froh", "NI", "Smile", 0),
    ("NI_schreck", "NI", "Fear", 0), ("NI_denkt", "NI_A", "Suspicious", 0), ("NI_sorge", "NI_A", "Concerned|Serious", 0),
    ("NI_zufrieden", "NI_A", "Smile Big|Smile", 0), ("NI_geht", "NI_W", "Smile", 0),
    ("AR_ruhig", "AR", "Calm", 0), ("AR_redet", "AR", "Smile", 1), ("AR_froh", "AR", "Smile Big|Smile", 0),
    ("AR_denkt", "AR", "Suspicious", 0),
    ("KU_ruhig", "KU", "Calm", 0), ("KU_redet", "KU", "Smile", 1), ("KU_denkt", "KU", "Suspicious", 0),
    ("KU_ernst", "KU", "Serious", 0),
    ("LO_ruhig", "LO", "Calm", 0), ("LO_redet", "LO", "Smile", 1), ("LO_froh", "LO", "Smile", 0),
    ("LO_sorge", "LO", "Concerned|Serious", 0),
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
