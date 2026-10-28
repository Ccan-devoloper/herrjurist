"""Figuren für Folge 115 (Garantenstellung, Winternacht: Kneipe und Parkbank) aus der LexVerse-Figma-Bibliothek
(Open Peeps, CC0). Alle Figuren fiktiv.
Karsten (um 40, sagt zu, Wolfgang heimzubringen, und lässt ihn auf der Bank zurück; Stimme stephan): standing/shirt-3
(langärmliges Hemd Grün #8FD694, schwarze Hose, weiße Schuhe), Kopf hat-beanie (Wintermütze), kein Bart, keine Brille.
Sachlich, keine Dämonisierung: keine bösen Mimiken (kein Contempt, kein Angry), nur Calm/Smile/Serious/Solemn/
Concerned|Serious/Suspicious.
Wolfgang (um 40, volltrunken, spricht nicht): sitting/crossed_legs (Pullover Blau #8DB3F2, schwarze Hose) in Kneipe und auf
der Bank (gleiches Outfit), Kopf Short 3, Mimiken Tired (müde), Eyes Closed (dösend), Calm/Smile (erholt). Keine Bilder von
Leiden.
Wirtin (um 60, Funktionsrolle; Stimme hilde): standing/resting-2 (schwarzes Oberteil, Hose Lila #B8A9F5), Kopf Gray Bun.
Passantin (um 30, Funktionsrolle; Stimme lucy): standing/blazer-3 (Blazer Rot #F07A6A, schwarzes Oberteil, Hose Weiß),
Kopf Long Bangs.
Keine Prothesen-Posen, keine Bärte, keine Polka Dots. Posen nicht aus 112–114 (pointing_finger-2, walking-1, resting-1,
shirt-1, crossed_arms-1, walking-2, blazer-4).
Präfix KA_/WO_/WI_/PA_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach
links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (KA_redet, KA_ernst2, WI_redet, PA_redet,
Lexi) zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_115")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "KA": ("standing/shirt-3", "hat-beanie", None, None, {"Skin": "#E8B894", "Top": "#8FD694"}),
    "WO": ("sitting/crossed_legs", "Short 3", None, None, {"Skin": "#F0C8A8", "Top": "#8DB3F2", "Hair": "#6B4A32"}),
    "WI": ("standing/resting-2", "Gray Bun", None, None, {"Skin": "#F2D0B1", "Pants": "#B8A9F5"}),
    "PA": ("standing/blazer-3", "Long Bangs", None, None, {"Skin": "#C68E62", "Jacket": "#F07A6A", "Pants": "#FFFFFF"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("KA_ruhig", "KA", "Calm", 0), ("KA_redet", "KA", "Smile", 1), ("KA_ernst", "KA", "Serious", 1),
    ("KA_still", "KA", "Solemn", 0), ("KA_sorge", "KA", "Concerned|Serious", 0), ("KA_denkt", "KA", "Suspicious", 0),
    ("WO_muede", "WO", "Tired", 0), ("WO_doest", "WO", "Eyes Closed", 0), ("WO_ruhig", "WO", "Calm", 0),
    ("WO_froh", "WO", "Smile", 0),
    ("WI_ruhig", "WI", "Calm", 0), ("WI_redet", "WI", "Concerned|Serious", 1), ("WI_froh", "WI", "Smile", 0),
    ("WI_denkt", "WI", "Suspicious", 0),
    ("PA_ruhig", "PA", "Calm", 0), ("PA_schreck", "PA", "Fear", 0), ("PA_redet", "PA", "Concerned|Serious", 1),
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
