"""Figuren für Folge 280 (Entschuldigender Notstand: Hafenbüro der Wasserschutzpolizei, Tafeln) aus der
LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv. Niemand erscheint im Wasser.
Herr Tamm (TA, Mitte 40, Fahrgast und Überlebender; Stimme marc): standing/resting-1 (Pullover Orange #F9A66C, schwarze Hose
  der Pose), Kopf Short 3 (Haar Dunkelbraun #5A3E2B), Haut #E8B994, kein Bart, keine Brille.
Kommissarin Petzold (PE, um 35, Wasserschutzpolizei; Stimme sabrina): standing/shirt-3 (hellblaues Hemd #8DB3F2 wie ein
  Uniformhemd, ohne Abzeichen/Logo, schwarze Hose der Pose), Kopf Medium Straight (Haar schwarz; die Kopfvorlage hat keine einfärbbare Haarfläche), Haut #EBC2A0.
Kapitän (KA, um 60, nur Abwandlung 1, namenlos, spricht nicht): standing/resting-2 (schwarzes Oberteil der Pose, Hose
  Marineblau #3E4A6B), Kopf Gray Short (helles Haar der Vorlage), Haut #D9A57E, kein Bart (keine Bärte über dem Mund).
Posen der letzten drei Folgen (277: blazer-2, easing-1; 278: walking-1, blazer-3; 279: robot_dance-3, sitting/mid-2,
blazer-4) nicht verwendet; Farben Orange/Hellblau/Marine statt Blau/Grün/Lila (277), Grün/Lila (278), Lila/Türkis (279).
Keine Polka Dots, keine Prothesen-Posen (blazer-1/-2, shirt-1/-2), keine Karikatur. Präfixe TA_/PE_/KA_ (nie ER_).
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Fear, Tired, Solemn, Driven, Eyes Closed,
Suspicious, Smile bzw. „Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten TA_redet, TA_redet2, PE_redet
(und Lexi) zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_280")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "TA": ("standing/resting-1", "Short 3", None, None, {"Skin": "#E8B994", "Top": "#F9A66C", "Hair": "#5A3E2B"}),
    "PE": ("standing/shirt-3", "Medium Straight", None, None, {"Skin": "#EBC2A0", "Top": "#8DB3F2", "Hair": "#B08850"}),
    "KA": ("standing/resting-2", "Gray Short", None, None, {"Skin": "#D9A57E", "Pants": "#3E4A6B", "Hair": "#B4B4B4"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("TA_ruhig", "TA", "Calm", 0), ("TA_ernst", "TA", "Serious", 0), ("TA_sorge", "TA", "Concerned|Serious", 0),
    ("TA_angst", "TA", "Fear", 0), ("TA_muede", "TA", "Tired", 0), ("TA_still", "TA", "Solemn", 0),
    ("TA_zu", "TA", "Eyes Closed", 0), ("TA_skeptisch", "TA", "Suspicious", 0), ("TA_erleichtert", "TA", "Smile", 0),
    ("TA_redet", "TA", "Concerned|Serious", 1), ("TA_redet2", "TA", "Tired", 1),
    ("PE_ruhig", "PE", "Calm", 0), ("PE_ernst", "PE", "Serious", 0), ("PE_skeptisch", "PE", "Suspicious", 0),
    ("PE_freundlich", "PE", "Smile", 0), ("PE_redet", "PE", "Serious", 1),
    ("KA_ernst", "KA", "Serious", 0), ("KA_still", "KA", "Solemn", 0), ("KA_skeptisch", "KA", "Suspicious", 0),
    ("KA_muede", "KA", "Tired", 0),
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
