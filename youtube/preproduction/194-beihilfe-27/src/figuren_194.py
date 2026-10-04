"""Figuren für Folge 194 (Beihilfe § 27 StGB: Autoleihe zum Wohnungseinbruch) aus der LexVerse-Figma-Bibliothek
(Open Peeps, CC0). Alle Figuren fiktiv, gewöhnlich gekleidet (keine Mütze, keine Maske, kein Werkzeug).
Falko (FA, um 35, Haupttäter; Stimme stephan): standing/robot_dance-3 (Oberteil Grün #8FD694, Hose Dunkelblau #3F5F8F,
  weiße Schuhe der Pose; offene Hand = Bitte um das Auto), Kopf Short 3, Haut #EBC0A0, keine Brille, kein Bart.
Hedda (HE, um 35, Freundin, leiht das Auto; Stimme lucy): standing/blazer-3 (Blazer Rot #F07A6A, schwarzes Shirt der Pose,
  Hose Grau #5A5A5A), Kopf Long Bangs, Haut #E2B08C.
Posen der letzten drei Folgen (191: easing-2, walking-1; 192: shirt-3, blazer-2; 193: shirt-3, shirt-4) und von 189/190
(blazer-4, crossed_arms-2, resting-1/-2, walking-2) nicht verwendet; Lexi-Posen (robot_dance-1, crossed_arms-1) nicht für
Fallfiguren; keine Polka Dots, keine Bärte, keine Prothesen-Posen, keine Karikatur. Präfixe FA_/HE_ (nie ER_).
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Driven, Suspicious, Solemn, Smile bzw.
„Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten FA_redet, HE_redet (und Lexi) zusätzlich mit a/o/e:
Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_194")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "FA": ("standing/robot_dance-3", "Short 3", None, None, {"Skin": "#EBC0A0", "Top": "#8FD694", "Pants": "#3F5F8F"}),
    "HE": ("standing/blazer-3", "Long Bangs", None, None, {"Skin": "#E2B08C", "Jacket": "#F07A6A", "Pants": "#5A5A5A"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("FA_ruhig", "FA", "Calm", 0), ("FA_ernst", "FA", "Serious", 0), ("FA_entschlossen", "FA", "Driven", 0),
    ("FA_denkt", "FA", "Suspicious", 0), ("FA_still", "FA", "Solemn", 0),
    ("FA_redet", "FA", "Serious", 1),
    ("HE_ruhig", "HE", "Calm", 0), ("HE_sorge", "HE", "Concerned|Serious", 0), ("HE_denkt", "HE", "Suspicious", 0),
    ("HE_ernst", "HE", "Solemn", 0), ("HE_liest", "HE", "Serious", 0),
    ("HE_redet", "HE", "Concerned|Serious", 1),
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
