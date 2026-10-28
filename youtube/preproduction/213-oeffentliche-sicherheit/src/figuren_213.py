"""Figuren für Folge 213 (Öffentliche Sicherheit: Graffiti auf der eigenen Garage) aus der LexVerse-Figma-Bibliothek
(Open Peeps, CC0). Alle Figuren fiktiv.
Frau Schulze (SC, um 35, Garagenbesitzerin bzw. im Gegenfall Mieterin; Stimme sabrina): standing/robot_dance-3 (Oberteil
  Koralle #F07A6A, Hose Anthrazit #3A3A48, ausgestreckter Arm = sprüht), Kopf Bangs (Haar #5A3A28), Haut #E8B894.
Herr Neumann (NE, um 40, Polizei; Stimme marc): standing/easing-1 (Jacke Dunkelblau #3D4A7A, Hemd Hellblau #8DB3F2,
  Hose #2B2F45 wie eine Uniform), Kopf Shaved 2 (Haar #3A2A20), Haut #D9A07A.
Herr Gebauer (GB, um 70, Nachbar; Stimme william): standing/walking-2 (schwarzes Oberteil, Hose Beige #C9A66B), Kopf
  No Hair 2, Brille Glasses 4, Haut #F2CDB0.
Frau Dietz (DI, um 60, Vermieterin im Gegenfall; Stimme laura_ruhig): standing/shirt-1 (Hemd Lila #B8A9F5, schwarze Hose;
  die Pose zeigt eine Beinprothese – kein Täterbezug), Kopf Gray Medium (Haar #B4B4B4), Brille Glasses 2, Haut #F0D0B0.
Posen der letzten Folgen (209–212: blazer-1…4, crossed_arms-1/-2, resting-1/-2, shirt-3, shirt-4, pointing_finger-1/-2,
robot_dance-2, easing-2, walking-1/-2 in 209 nicht als Hauptfigur) – geprüft: robot_dance-3, easing-1, shirt-1 neu; walking-2
nur für den Nachbarn. Keine Polka Dots, keine Bärte, keine Karikatur. Präfixe SC_/NE_/GB_/DI_ (nie ER_).
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Smile, Serious, Driven, Suspicious, Tired, Very Angry bzw.
„Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten SC_redet, NE_redet, GB_redet, DI_redet (und Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_213")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "SC": ("standing/robot_dance-3", "Bangs", None, None, {"Skin": "#E8B894", "Top": "#F07A6A", "Pants": "#3A3A48",
                                                         "Hair": "#5A3A28"}),
    "NE": ("standing/easing-1", "Shaved 2", None, None, {"Skin": "#D9A07A", "Jacket": "#3D4A7A", "Top": "#8DB3F2",
                                                       "Pants": "#2B2F45", "Hair": "#3A2A20"}),
    "GB": ("standing/walking-2", "No Hair 2", None, "Glasses 4", {"Skin": "#F2CDB0", "Pants": "#C9A66B"}),
    "DI": ("standing/shirt-1", "Gray Medium", None, "Glasses 2", {"Skin": "#F0D0B0", "Top": "#B8A9F5", "Hair": "#B4B4B4",
                                                                "Prosthesis": "#B8B8B8"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("SC_ruhig", "SC", "Calm", 0), ("SC_froh", "SC", "Smile", 0), ("SC_denkt", "SC", "Serious", 0),
    ("SC_sorge", "SC", "Concerned|Serious", 0), ("SC_skeptisch", "SC", "Suspicious", 0), ("SC_redet", "SC", "Driven", 1),
    ("NE_ruhig", "NE", "Calm", 0), ("NE_ernst", "NE", "Serious", 0), ("NE_denkt", "NE", "Suspicious", 0),
    ("NE_froh", "NE", "Smile", 0), ("NE_redet", "NE", "Serious", 1),
    ("GB_sorge", "GB", "Concerned|Serious", 0), ("GB_skeptisch", "GB", "Suspicious", 0), ("GB_muede", "GB", "Tired", 0),
    ("GB_ruhig", "GB", "Calm", 0), ("GB_redet", "GB", "Concerned|Serious", 1),
    ("DI_ruhig", "DI", "Calm", 0), ("DI_aerger", "DI", "Very Angry", 0), ("DI_denkt", "DI", "Serious", 0),
    ("DI_redet", "DI", "Very Angry", 1),
]

if __name__ == "__main__":
    os.makedirs(ZIEL, exist_ok=True)
    nur = sys.argv[1:]          # optional: nur bestimmte Personen (Vorschau)
    n = 0
    for name, p, mimik, mund in LISTE:
        if nur and p not in nur:
            continue
        pose, kopf, bart, brille, farben = P[p]
        for suffix, gespiegelt in (("", 1), ("_r", 0)):
            figur(pose, kopf, mimik, bart, brille, farben, hoehe=1200, spiegeln=bool(gespiegelt)).save(f"{ZIEL}/{name}{suffix}.png"); n += 1
            if mund:
                for k, m in MUND.items():
                    figur(pose, kopf, f"{mimik.split('|')[0]}|{m}", bart, brille, farben, hoehe=1200,
                          spiegeln=bool(gespiegelt)).save(f"{ZIEL}/{name}{suffix}_{k}.png"); n += 1
    if not nur:
        # Lexi (feste Moderatorin, Stimme Carla), blickt nach links zur Tafel
        for name, (pose, mimik) in {"LX_erklaert": ("standing/robot_dance-1", "Smile"), "LX_warnt": ("standing/robot_dance-1", "Serious")}.items():
            a = LX.AUSSEHEN
            for k, g in {"": mimik, **{"_" + k: f"{mimik}|{m}" for k, m in MUND.items()}}.items():
                figur(pose, a["kopf"], g, a["bart"], a["brille"], a["farben"], hoehe=1200, spiegeln=True).save(f"{ZIEL}/{name}{k}.png"); n += 1
    print(n, "Figurenbilder ->", ZIEL)
