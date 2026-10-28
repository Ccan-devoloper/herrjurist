"""Figuren für Folge 216 (Beweiswürdigung in der Revision; Kanzlei, Paketlager und Gerichtssaal im Rückblick) aus der
LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv.
Herr Kerber (KE, um 40, Angeklagter und Mandant, Lagerarbeiter; Stimme marc): standing/shirt-3 (Hemd Khaki #C9A66B,
  schwarze Hose, weiße Schuhe), Kopf Short 1, Haut #E2B08A, kein Bart, keine Brille.
Frau Bremer (BR, um 35, Kollegin und Belastungszeugin; Stimme sabrina): standing/crossed_arms-1 (Pullover Lila #B8A9F5,
  schwarze Hose), Kopf Medium Straight (Haar #6B4A35), Haut #F0C8A8, keine Brille; ruhige, ernste Mimik, keine Karikatur.
Rechtsanwalt Wegmann (WG, um 60, Verteidiger; Stimme william): standing/blazer-3 (Sakko Stahlblau #4F6D8F, Hose #3A3A44),
  Kopf Gray Short, Brille Glasses 3, Haut #EBC3A3.
Die Richterin (RI, um 50, Strafrichterin am Amtsgericht, nur im Rückblick; Stimme laura_ruhig): standing/blazer-4 (Jacke
  Schwarzgrau #2B2B35 wie eine Robe, weißes Oberteil), Kopf Bun (Haar #3A2A20), Haut #D9A884, keine Brille.
Posen der letzten drei Folgen (213: robot_dance-3, easing-1, walking-2, shirt-1; 214: easing-2, walking-1, walking-3;
215: robot_dance-2, resting-1, crossed_arms-2) nicht verwendet; keine Polka Dots, keine Prothesen-Posen (blazer-1/-2,
shirt-1/-2), keine Bärte, keine Karikatur, keine Täter-Klischees. Präfixe KE_/BR_/WG_/RI_ (nie ER_).
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Suspicious, Smile, Solemn bzw.
„Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten KE_redet, KE_redet2, BR_redet, WG_redet, RI_redet
(und Lexi) zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_216")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "KE": ("standing/shirt-3", "Short 1", None, None, {"Skin": "#E2B08A", "Top": "#C9A66B"}),
    "BR": ("standing/crossed_arms-1", "Medium Straight", None, None, {"Skin": "#F0C8A8", "Top": "#B8A9F5", "Hair": "#6B4A35"}),
    "WG": ("standing/blazer-3", "Gray Short", None, "Glasses 3", {"Skin": "#EBC3A3", "Jacket": "#4F6D8F", "Pants": "#3A3A44"}),
    "RI": ("standing/blazer-4", "Bun", None, None, {"Skin": "#D9A884", "Jacket": "#2B2B35", "Top": "#FFFFFF", "Hair": "#3A2A20"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("KE_ruhig", "KE", "Calm", 0), ("KE_ernst", "KE", "Serious", 0), ("KE_sorge", "KE", "Concerned|Serious", 0),
    ("KE_skeptisch", "KE", "Suspicious", 0), ("KE_froh", "KE", "Smile", 0),
    ("KE_redet", "KE", "Concerned|Serious", 1), ("KE_redet2", "KE", "Smile", 1),
    ("BR_ruhig", "BR", "Calm", 0), ("BR_ernst", "BR", "Serious", 0), ("BR_still", "BR", "Solemn", 0),
    ("BR_redet", "BR", "Serious", 1),
    ("WG_ruhig", "WG", "Calm", 0), ("WG_ernst", "WG", "Serious", 0), ("WG_skeptisch", "WG", "Suspicious", 0),
    ("WG_froh", "WG", "Smile", 0), ("WG_redet", "WG", "Suspicious", 1),
    ("RI_ruhig", "RI", "Calm", 0), ("RI_ernst", "RI", "Serious", 0), ("RI_redet", "RI", "Serious", 1),
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
