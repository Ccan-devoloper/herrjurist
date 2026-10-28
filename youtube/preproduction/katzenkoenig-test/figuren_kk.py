"""Figuren für den Katzenkönig-Fall aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Je sprechender Ansicht vier Mundzustände: zu (Grundmimik), a (weit offen), o (rund), e (breit/Zähne).
Augen/Nase bleiben aus der Grundmimik, nur die Mundpartie wechselt (lexpeeps: 'Augen|Mund')."""
import os, sys
BIB = "/home/user/herrjurist/youtube/openpeeps-erweiterung/figma-bibliothek"
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_kk")
os.makedirs(ZIEL, exist_ok=True)
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Kopf, Bart, Brille, Farben)
P = {
    "BA": ("Long", None, None, {"Skin": "#F1C6A5", "Jacket": "#B784D1", "Pants": "#3D3D58"}),      # Barbara
    "PE": ("Short 3", "Full", None, {"Skin": "#D9A07A", "Top": "#7FB2F0"}),                     # Peter
    "RI": ("Short 2", None, None, {"Skin": "#E9BE98", "Top": "#9BD88A"}),                        # Richard
    "NO": ("Long Curly", None, None, {"Skin": "#8D5A3B", "Jacket": "#FFCF77", "Top": "#F28C6B"}),  # Nora
}
POSE = {"BA": "standing/blazer-3", "PE": "standing/shirt-3", "RI": "standing/crossed_arms-1", "NO": "standing/easing-1"}

# (Name, Person, Pose|None, Grundmimik, spiegeln, mit Mundzuständen)
LISTE = [
    ("BA_ruhig", "BA", None, "Calm", 0, 0), ("BA_listig", "BA", None, "Suspicious", 0, 1),
    ("BA_drohend", "BA", None, "Serious", 0, 1), ("BA_zufrieden", "BA", None, "Contempt", 0, 0),
    ("PE_ruhig", "PE", None, "Calm", 0, 0), ("PE_ernst", "PE", None, "Serious", 0, 1), ("PE_zufrieden", "PE", None, "Smile", 0, 0),
    ("RI_ruhig", "RI", None, "Calm", 1, 0), ("RI_staunt", "RI", None, "Awe", 1, 0), ("RI_zweifel", "RI", None, "Concerned", 1, 1),
    ("RI_glaubt", "RI", None, "Driven", 1, 0), ("RI_denkt", "RI", None, "Serious", 1, 0), ("RI_schuld", "RI", None, "Tired", 1, 0),
    ("RI_geht", "RI", "standing/walking-1", "Driven", 0, 0), ("RI_steht", "RI", "standing/robot_dance-1", "Driven", 0, 0),
    ("RI_ruhig_r", "RI", None, "Calm", 0, 0), ("RI_denkt_r", "RI", None, "Serious", 0, 0),
    ("NO_ruhig", "NO", None, "Smile", 0, 0), ("NO_arglos", "NO", None, "Calm", 0, 0), ("NO_liegt_", "NO", None, "Eyes Closed", 0, 0),
    ("NO_ruhig_l", "NO", None, "Smile", 1, 0),
]

for name, p, pose, mimik, sp, mund in LISTE:
    kopf, bart, brille, farben = P[p]
    pose = pose or POSE[p]
    figur(pose, kopf, mimik, bart, brille, farben, hoehe=1200, spiegeln=bool(sp)).save(f"{ZIEL}/{name}.png")
    if mund:
        for k, m in MUND.items():
            figur(pose, kopf, f"{mimik}|{m}", bart, brille, farben, hoehe=1200, spiegeln=bool(sp)).save(f"{ZIEL}/{name}_{k}.png")
# Nora liegt (nach dem Stich nach vorn gefallen, Kopf rechts)
from PIL import Image
Image.open(f"{ZIEL}/NO_liegt_.png").rotate(-90, expand=True).save(f"{ZIEL}/NO_liegt.png"); os.remove(f"{ZIEL}/NO_liegt_.png")
# Lexi (feste Moderatorin, Stimme Carla): erklärt mit Mundzuständen, freut sich beim Merksatz
for name, (pose, mimik) in {"LX_erklaert": ("standing/robot_dance-1", "Smile"), "LX_warnt": ("standing/robot_dance-1", "Serious"),
                            "LX_freut": ("standing/crossed_arms-1", "Cute")}.items():
    a = LX.AUSSEHEN
    for k, g in {"": mimik, **{"_" + k: f"{mimik}|{m}" for k, m in MUND.items()}}.items():
        figur(pose, a["kopf"], g, a["bart"], a["brille"], a["farben"], hoehe=1200, spiegeln=True).save(f"{ZIEL}/{name}{k}.png")
print(len(os.listdir(ZIEL)), "Figurenbilder ->", ZIEL)
