"""Figuren für Folge 038 (Körperverletzung § 223, Wohngemeinschaft) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Katrin (Ende 20, Mitbewohnerin): sitting/closed_legs-1 (sitzt auf dem Sofa bzw. auf der Behandlungsliege), Jacke Blau.
    Kopf „Long“ (lange Haare) vor dem Abschneiden, „Medium 1“ (kurz) danach – die einzige gewollte Änderung der Frisur,
    weil sie der Sachverhalt ist (KAL_ = lang, KA_ = kurz).
Sigrid (Mitte 50, Mitbewohnerin): standing/walking-1 (schleicht), Kopf „Gray Medium“, Oberteil Lila.
Doktor Lindner (um 60, Hautarzt): standing/doctor-nurse-02 (Arztkittel), Kopf „Gray Short“, Brille „Glasses 3“.
Je Person eine Pose (Outfit konstant). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und
blickt nach links, Suffix _r nach rechts. Keine Bärte.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF): Calm, Smile, Serious, Suspicious, Driven, Contempt, Fear,
Tired, Eyes Closed, Very Angry bzw. „Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten zusätzlich mit
a/o/e (Augen der Grundmimik + Mund Explaining/Concerned Fear/Hectic, Schnitt bei 60 % der Gesichtshöhe)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_038")
os.makedirs(ZIEL, exist_ok=True)
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

KA_F = {"Skin": "#F0C8A8", "Jacket": "#8DB3F2"}
SI_F = {"Skin": "#E0B48E", "Top": "#B8A9F5", "Hair": "#BDBDC6"}   # graues Haar (Mitte 50)
LI_F = {"Skin": "#D9A27A", "Hair": "#D9D9DE"}   # graues Haar (um 60)

# Ansicht: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "KAL": ("sitting/closed_legs-1", "Long", None, None, KA_F),
    "KA": ("sitting/closed_legs-1", "Medium 1", None, None, KA_F),
    "SI": ("standing/walking-1", "Gray Medium", None, None, SI_F),
    "LI": ("standing/doctor-nurse-02", "Gray Short", None, "Glasses 3", LI_F),
}

# (Name, Ansicht, Grundmimik, mit Mundzuständen)
LISTE = [
    ("KAL_schlaeft", "KAL", "Eyes Closed", 0), ("KAL_ruhig", "KAL", "Calm", 0), ("KAL_erschrickt", "KAL", "Fear", 0),
    ("KAL_krank", "KAL", "Concerned|Serious", 0), ("KAL_denkt", "KAL", "Serious", 0),
    ("KA_erschrickt", "KA", "Fear", 0), ("KA_redet", "KA", "Concerned|Serious", 1), ("KA_wuetend", "KA", "Very Angry", 0),
    ("KA_ruhig", "KA", "Calm", 0), ("KA_denkt", "KA", "Serious", 0), ("KA_muede", "KA", "Tired", 0),
    ("KA_einv", "KA", "Smile", 1), ("KA_skeptisch", "KA", "Suspicious", 0),
    ("SI_ruhig", "SI", "Calm", 0), ("SI_schleicht", "SI", "Suspicious", 0), ("SI_entschlossen", "SI", "Driven", 0),
    ("SI_redet", "SI", "Contempt", 1), ("SI_ertappt", "SI", "Fear", 0), ("SI_aua", "SI", "Concerned|Serious", 0),
    ("SI_denkt", "SI", "Serious", 0),
    ("LI_ruhig", "LI", "Calm", 0), ("LI_redet", "LI", "Smile", 1), ("LI_froh", "LI", "Smile", 0), ("LI_denkt", "LI", "Serious", 0),
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
