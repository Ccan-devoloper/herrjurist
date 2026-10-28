"""Figuren für Folge 201 (Lernplan Examen: WG-Küche mit Wandkalender) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv.
Fenna (FE, Mitte 20, Jurastudentin ein Jahr vor dem Examen; Stimme lucy): standing/pointing_finger-2 (schwarzes Oberteil,
  Hose Türkis #7FD6D0, schwarze Schuhe, Zeigefinger erhoben – sie plant am Kalender), Kopf Medium Straight (Haar #7A4E2D),
  Haut #F0C8A8, keine Brille.
Nils (NI, um 28, Referendar, hat das Examen im letzten Jahr geschrieben; Stimme christian): standing/blazer-4 (Sakko Blau
  #8DB3F2 über weißem Shirt, Hose #3B3B4F, Hand an der Hüfte), Kopf Short 3 (Haar #3A2A20), Haut #D9A47E, kein Bart.
Posen der letzten drei Folgen (198: easing-1, resting-1; 199: easing-2, pointing_finger-1; 200: shirt-3, resting-2,
walking-1, walking-2) nicht verwendet; robot_dance-1 bleibt Lexi; keine Polka Dots, keine Prothesen-Posen (blazer-1/-2,
shirt-1/-2), keine Bärte, keine Karikatur. Präfixe FE_/NI_ (nie ER_).
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Smile, Suspicious, Serious, Driven bzw.
„Augen|geschlossener Mund“ (Smile Big|Smile, Concerned|Serious). Sprechende Ansichten FE_redet, FE_fragt, FE_redetfroh,
NI_redet, NI_redet2 (und Lexi) zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic,
Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_201")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "FE": ("standing/pointing_finger-2", "Medium Straight", None, None, {"Skin": "#F0C8A8", "Pants": "#7FD6D0", "Hair": "#7A4E2D"}),
    "NI": ("standing/blazer-4", "Short 3", None, None, {"Skin": "#D9A47E", "Jacket": "#8DB3F2", "Top": "#FFFFFF",
                                                      "Pants": "#3B3B4F", "Hair": "#3A2A20"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("FE_ruhig", "FE", "Calm", 0), ("FE_ratlos", "FE", "Concerned|Serious", 0), ("FE_denkt", "FE", "Suspicious", 0),
    ("FE_froh", "FE", "Smile", 0), ("FE_stolz", "FE", "Smile Big|Smile", 0), ("FE_entschlossen", "FE", "Driven", 0),
    ("FE_redet", "FE", "Concerned|Serious", 1), ("FE_fragt", "FE", "Serious", 1), ("FE_redetfroh", "FE", "Smile", 1),
    ("NI_ruhig", "NI", "Calm", 0), ("NI_froh", "NI", "Smile", 0), ("NI_ernst", "NI", "Serious", 0),
    ("NI_redet", "NI", "Smile", 1), ("NI_redet2", "NI", "Calm", 1),
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
