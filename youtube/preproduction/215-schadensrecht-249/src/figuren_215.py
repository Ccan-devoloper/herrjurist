"""Figuren für Folge 215 (Differenzhypothese und Naturalrestitution) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Personen fiktiv.
Hedi (HD, um 25, Radfahrerin, Geschädigte; Stimme lucy): standing/robot_dance-2 (schwarzes Oberteil der Pose, Hose Grün
  #8FD694), Kopf Long, Haut #E9C2A0, kein Bart.
Ludolf (LU, um 50, Autofahrer, Schädiger; Stimme stephan): standing/resting-1 (Pullover Orange #F4A259, nicht Gelb wie Lexi, schwarze Hose der Pose),
  Kopf Short 2, Brille Glasses 2, Haut #D9A884, kein Bart. Kein Bösewicht: entschuldigt sich, will es „in Ordnung bringen“.
Trude (TR, um 65, Inhaberin der Fahrradwerkstatt; Stimme hilde): standing/crossed_arms-2 (schwarzes Oberteil der Pose, Hose
  Blau #8DB3F2), Kopf Gray Bun, Brille Glasses 3, Haut #F0CDB2.
Posen der letzten drei Folgen (212: blazer-4, resting-2; 213: robot_dance-3, easing-1, walking-2, shirt-1; 214: easing-2,
walking-1, walking-3) nicht verwendet; robot_dance-1 bleibt Lexi; Prothesen-Posen (blazer-1, blazer-2, shirt-1/2) verworfen;
keine Polka Dots, keine Bärte. Präfixe HD_/LU_/TR_ (nie ER_). Alle Posen blicken im Original nach rechts;
Grundansicht gespiegelt (blickt nach links), Suffix _r nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Smile, Serious, Suspicious, Fear, Solemn, Tired bzw.
„Augen|geschlossener Mund“ (Concerned|Serious, Smile Big|Smile). Sprechende Ansichten HD_redet (Serious), LU_klagt
(Concerned|Serious), LU_redet (Smile), TR_redet (Calm) und Lexi zusätzlich mit a/o/e:
Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_215")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "HD": ("standing/robot_dance-2", "Long", None, None, {"Skin": "#E9C2A0", "Pants": "#8FD694"}),
    "LU": ("standing/resting-1", "Short 2", None, "Glasses 2", {"Skin": "#D9A884", "Top": "#F4A259"}),
    "TR": ("standing/crossed_arms-2", "Gray Bun", None, "Glasses 3", {"Skin": "#F0CDB2", "Pants": "#8DB3F2"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("HD_ruhig", "HD", "Calm", 0), ("HD_froh", "HD", "Smile", 0), ("HD_ernst", "HD", "Serious", 0),
    ("HD_denkt", "HD", "Suspicious", 0), ("HD_sorge", "HD", "Concerned|Serious", 0), ("HD_schreck", "HD", "Fear", 0),
    ("HD_freut", "HD", "Smile Big|Smile", 0),
    ("HD_redet", "HD", "Serious", 1),
    ("LU_ruhig", "LU", "Calm", 0), ("LU_froh", "LU", "Smile", 0), ("LU_sorge", "LU", "Concerned|Serious", 0),
    ("LU_schreck", "LU", "Fear", 0), ("LU_denkt", "LU", "Suspicious", 0), ("LU_still", "LU", "Solemn", 0),
    ("LU_klagt", "LU", "Concerned|Serious", 1), ("LU_redet", "LU", "Smile", 1),
    ("TR_ruhig", "TR", "Calm", 0), ("TR_froh", "TR", "Smile", 0), ("TR_denkt", "TR", "Suspicious", 0),
    ("TR_redet", "TR", "Calm", 1),
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
