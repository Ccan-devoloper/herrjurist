"""Figuren für Folge 212 (§ 326 BGB, ausgefallenes Privatkonzert) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv, keine realen Künstler oder Veranstalter.
Theodor (TH, um 30, Pianist, Schuldner des Konzerts; Stimme niklas): standing/blazer-4 (Konzertkleidung: Sakko Anthrazit
#3A3A48, Oberteil Weiß; die Hand in der Hüfte wirkt selbstbewusst), Kopf Short 4 (kurzes dunkles Haar), keine Brille, kein Bart.
Friedhelm (FR, 70, Gastgeber, Gläubiger des Konzerts; Stimme helmut): standing/resting-2 (schwarzer Pullover der Pose, Hose
Blau #8DB3F2), Kopf Gray Short (graues Haar), Brille Glasses 3, kein Bart (kein Bart über dem Mund).
Keine Karikatur, keine Polka Dots. Posen nicht aus den Folgen 209–211 (easing-2, shirt-3, pointing_finger-2, blazer-1,
blazer-2, crossed_arms-1, crossed_arms-2, resting-1, blazer-3, shirt-4, pointing_finger-1, robot_dance-2) und nicht 208
(robot_dance-3, walking-2, blazer-4 dort als Nebenfigur Kaltenbach mit Rosa-Blazer; hier anderes Outfit, Mann, Anthrazit).
Präfix TH_/FR_ (nie ER_, weil bausteine.peep_voll ER_* in den Ordner op_we umleitet). Alle Posen blicken im Original nach
rechts; die Grundansicht ist gespiegelt und blickt nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Smile, Suspicious, Awe, Tired bzw.
„Augen|geschlossener Mund“ (Smile Big|Smile, Concerned|Serious). Sprechende Ansichten (TH_redet, TH_krank_redet, FR_redet,
FR_sorge_redet, FR_ernst_redet, Lexi) zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear /
Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_212")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

TH_F = {"Skin": "#E9B892", "Jacket": "#3A3A48", "Top": "#FFFFFF", "Hair": "#3B2A20"}
FR_F = {"Skin": "#F2D2BA", "Pants": "#8DB3F2", "Hair": "#A8A8A8"}
# Person/Pose: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "TH": ("standing/blazer-4", "Short 4", None, None, TH_F),
    "FR": ("standing/resting-2", "Gray Short", None, "Glasses 3", FR_F),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("TH_ruhig", "TH", "Calm", 0), ("TH_redet", "TH", "Smile", 1), ("TH_froh", "TH", "Smile Big|Smile", 0),
    ("TH_krank", "TH", "Tired", 0), ("TH_krank_redet", "TH", "Tired", 1), ("TH_sorge", "TH", "Concerned|Serious", 0),
    ("TH_denkt", "TH", "Suspicious", 0), ("TH_ernst", "TH", "Serious", 0), ("TH_staunt", "TH", "Awe", 0),
    ("FR_ruhig", "FR", "Calm", 0), ("FR_redet", "FR", "Smile", 1), ("FR_froh", "FR", "Smile Big|Smile", 0),
    ("FR_sorge", "FR", "Concerned|Serious", 0), ("FR_sorge_redet", "FR", "Concerned|Serious", 1),
    ("FR_ernst", "FR", "Serious", 0), ("FR_ernst_redet", "FR", "Serious", 1), ("FR_denkt", "FR", "Suspicious", 0),
    ("FR_staunt", "FR", "Awe", 0),
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
