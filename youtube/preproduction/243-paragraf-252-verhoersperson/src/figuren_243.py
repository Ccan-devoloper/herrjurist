"""Figuren für Folge 243 (§ 252 StPO: Die Ehefrau schweigt – Verhörsperson als Zeuge?) aus der LexVerse-Figma-Bibliothek
(Open Peeps, CC0).
Frau Hasselbach (FH, um 45, Ehefrau, Zeugin, Buchhaltung im Malerbetrieb, Stimme sabrina): standing/blazer-3 (Blazer
  Petrol #2E8B84, schwarzes Oberteil der Pose, Hose Grau #6B6F80), Kopf Long.
Herr Hasselbach (HH, um 45, Ehemann, Malermeister, Beschuldigter/Angeklagter, spricht nicht): standing/walking-2 (schwarzes
  Oberteil der Pose, Hose Khaki #C9A46A), Kopf Short 1, ohne Bart.
Polizeibeamter (PB, um 40, Vernehmungsbeamter, Stimme marc): standing/blazer-2 (Jacke Dunkelblau #2F4B7C wie eine
  Dienstjacke ohne Abzeichen, Oberteil Hellblau #8DB3F2, schwarze Hose; die Pose zeigt eine Unterschenkelprothese – beim
  Polizeibeamten, nicht bei einer Täterrolle), Kopf Short 2.
Vorsitzender (VR, um 60, Stimme william): standing/pointing_finger-1 (schwarz wie eine Robe, erhobener Zeigefinger bei der
  Belehrung), Kopf No Hair 2, Brille Glasses 2.
Verteidigerin (VT, um 40, Stimme laura_ruhig): standing/walking-3 (schwarz wie eine Robe), Kopf Medium Bangs 3.
Ermittlungsrichterin (EJ, um 55, Gegenbeispiel richterliche Vernehmung, spricht nicht): standing/robot_dance-2 (Oberteil
  Schwarz #2B2B2B wie eine Robe, Hose #3A3A44), Kopf Medium 3, Brille Glasses 4.
Freundin (FR, um 45, hypothetischer Gegenfall, spricht nicht): standing/shirt-1 (Hemd Terrakotta #E58E5A, schwarze Hose der Pose,
  Unterschenkelprothese der Pose), Kopf Bangs.
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links, _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Suspicious, Smile, Solemn, Tired bzw.
„Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten zusätzlich mit a/o/e: Augen der Grundmimik + Mund
Explaining / Concerned Fear / Hectic (Schnitt bei 60 % der Gesichtshöhe). Figurenpräfix nie ER_."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_243")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "FH": ("standing/blazer-3", "Long", None, None, {"Skin": "#E8BB98", "Jacket": "#2E8B84", "Pants": "#6B6F80"}),
    "HH": ("standing/walking-2", "Short 1", None, None, {"Skin": "#F2D0B5", "Pants": "#C9A46A"}),
    "PB": ("standing/blazer-2", "Short 2", None, None, {"Skin": "#C68E6A", "Jacket": "#2F4B7C", "Top": "#8DB3F2"}),
    "VR": ("standing/pointing_finger-1", "No Hair 2", None, "Glasses 2", {"Skin": "#EBC29E"}),
    "VT": ("standing/walking-3", "Medium Bangs 3", None, None, {"Skin": "#B07552"}),
    "EJ": ("standing/robot_dance-2", "Medium 3", None, "Glasses 4", {"Skin": "#D9A47E", "Top": "#2B2B2B", "Pants": "#3A3A44"}),
    "FR": ("standing/shirt-1", "Bangs", None, None, {"Skin": "#F0C8A8", "Top": "#E58E5A"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("FH_ruhig", "FH", "Calm", 0), ("FH_redet", "FH", "Serious", 1), ("FH_sorge", "FH", "Concerned|Serious", 0),
    ("FH_denkt", "FH", "Suspicious", 0), ("FH_froh", "FH", "Smile", 0), ("FH_ernst", "FH", "Serious", 0),
    ("FH_fest", "FH", "Solemn", 0),
    ("HH_ruhig", "HH", "Calm", 0), ("HH_froh", "HH", "Smile", 0), ("HH_sorge", "HH", "Concerned|Serious", 0),
    ("HH_denkt", "HH", "Suspicious", 0), ("HH_muede", "HH", "Tired", 0),
    ("PB_ruhig", "PB", "Calm", 0), ("PB_redet", "PB", "Calm", 1), ("PB_ernst", "PB", "Serious", 0),
    ("PB_denkt", "PB", "Suspicious", 0), ("PB_froh", "PB", "Smile", 0),
    ("VR_ruhig", "VR", "Calm", 0), ("VR_redet", "VR", "Serious", 1), ("VR_ernst", "VR", "Serious", 0),
    ("VR_denkt", "VR", "Suspicious", 0),
    ("VT_ruhig", "VT", "Calm", 0), ("VT_redet", "VT", "Serious", 1), ("VT_ernst", "VT", "Serious", 0),
    ("VT_denkt", "VT", "Suspicious", 0), ("VT_froh", "VT", "Smile", 0),
    ("EJ_ruhig", "EJ", "Calm", 0), ("EJ_ernst", "EJ", "Serious", 0), ("EJ_denkt", "EJ", "Suspicious", 0),
    ("FR_ruhig", "FR", "Calm", 0), ("FR_denkt", "FR", "Suspicious", 0), ("FR_froh", "FR", "Smile", 0),
]

if __name__ == "__main__":
    os.makedirs(ZIEL, exist_ok=True)
    n = 0
    for name, p, mimik, mund in LISTE:
        pose, kopf, bart, brille, farben = P[p]
        for suffix, gespiegelt in (("", True), ("_r", False)):
            figur(pose, kopf, mimik, bart, brille, farben, hoehe=1200, spiegeln=gespiegelt).save(f"{ZIEL}/{name}{suffix}.png"); n += 1
            if mund:
                for k, m in MUND.items():
                    figur(pose, kopf, f"{mimik.split('|')[0]}|{m}", bart, brille, farben, hoehe=1200,
                          spiegeln=gespiegelt).save(f"{ZIEL}/{name}{suffix}_{k}.png"); n += 1
    # Lexi (feste Moderatorin, Stimme Carla), blickt nach links zur Tafel
    for name, (pose, mimik) in {"LX_erklaert": ("standing/robot_dance-1", "Smile"), "LX_warnt": ("standing/robot_dance-1", "Serious")}.items():
        a = LX.AUSSEHEN
        for k, g in {"": mimik, **{"_" + k: f"{mimik}|{m}" for k, m in MUND.items()}}.items():
            figur(pose, a["kopf"], g, a["bart"], a["brille"], a["farben"], hoehe=1200, spiegeln=True).save(f"{ZIEL}/{name}{k}.png"); n += 1
    print(n, "Figurenbilder ->", ZIEL)
