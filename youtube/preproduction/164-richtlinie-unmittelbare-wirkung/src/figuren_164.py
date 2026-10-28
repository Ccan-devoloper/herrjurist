"""Figuren für Folge 164 (Richtlinie unmittelbare Wirkung; Feuerwehrmann und Personalamt der Stadt) aus der LexVerse-Figma-
Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv, Erwachsene; Feuerwehr neutral (keine Wappen, keine Beschriftung).
Herr Ruppert (RU, um 35, Feuerwehrmann der Berufsfeuerwehr; Stimme niklas): standing/shirt-3 (Diensthemd Dunkelblau
  #4F6FA8, schwarze Hose aus der Pose, weiße Schuhe), Kopf Short 4 (dunkles Kurzhaar), Haut #E9B996, keine Brille, kein Bart.
Herr Goldbach (GO, um 60, leitet das Personalamt der Stadt; Stimme helmut): standing/blazer-4 (Sakko Grau #A9A9A9, Hemd
  Weiß, schwarze Hose aus der Pose), Kopf No Hair 1 (Glatze), Brille Glasses, Haut #D8A580, kein Bart.
Posen der letzten drei Folgen (159: robot_dance-3, crossed_arms-1; 160: crossed_arms-1, resting-1; 161: blazer-3,
resting-1, crossed_arms-1, crossed_arms-2) nicht verwendet; robot_dance-1 bleibt Lexi; keine Polka Dots, keine
Prothesen-Posen, keine Bärte; Oberteilfarben der Vorfolgen (Koralle, Grün, Lila, Orange, Gelb) vermieden. Präfixe RU_/GO_
(nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links, Suffix _r
blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten RU_redet, GO_redet, GO_einsicht (und
Lexi) zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_164")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "RU": ("standing/shirt-3", "Short 4", None, None, {"Skin": "#E9B996", "Top": "#4F6FA8"}),
    "GO": ("standing/blazer-4", "No Hair 1", None, "Glasses", {"Skin": "#D8A580", "Jacket": "#A9A9A9", "Top": "#FFFFFF"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("RU_ruhig", "RU", "Calm", 0), ("RU_redet", "RU", "Serious", 1), ("RU_ernst", "RU", "Serious", 0),
    ("RU_froh", "RU", "Smile", 0), ("RU_denkt", "RU", "Suspicious", 0), ("RU_sorge", "RU", "Concerned|Serious", 0),
    ("RU_staunt", "RU", "Awe", 0), ("RU_entschlossen", "RU", "Driven", 0),
    ("GO_ruhig", "GO", "Calm", 0), ("GO_redet", "GO", "Serious", 1), ("GO_einsicht", "GO", "Calm", 1),
    ("GO_ernst", "GO", "Serious", 0), ("GO_froh", "GO", "Smile", 0), ("GO_denkt", "GO", "Suspicious", 0),
    ("GO_staunt", "GO", "Awe", 0), ("GO_still", "GO", "Solemn", 0),
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
