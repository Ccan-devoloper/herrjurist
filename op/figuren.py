"""Besetzung je Beitrag: Figuren aus der Open-Peeps-Bibliothek (CC0), ein Outfit je Figur.

Eine Figur wird im Tagesplan einmal beschrieben (Kopf, Hautton, Kleidung, Brustbild, Standpose) und auf den
Folien nur noch über Kürzel angesprochen:  "A:froh" = Brustbild mit Mimik froh, "A/eilt" = stehend, Pose eilt.
Die Blickrichtung ergibt sich aus der Position (links → schaut nach rechts zur Bildmitte).
"""
import hashlib, json, os
import opkern
from lexpeeps import figur as _figur

ORDNER = os.path.join(opkern.RES, "peeps", "op_ec")
os.makedirs(ORDNER, exist_ok=True)

MIMIK = {"froh": "Smile Big|Smile", "sorge": "Concerned|Serious", "fragt": "Suspicious|Explaining",
         "redet": "Smile|Explaining", "ernst": "Serious", "denkt": "Suspicious", "skeptisch": "Suspicious",
         "ruhig": "Smile", "erklaert": "Smile|Explaining", "eilt": "Hectic|Serious", "staunt": "Awe|Awe",
         "lacht": "Smile LOL|Smile Big", "muede": "Tired|Serious"}
POSEN = {"eilt": "standing/walking-1", "sorge": "standing/resting-1", "skeptisch": "standing/crossed_arms-1",
         "erklaert": "standing/robot_dance-1", "blazer": "standing/blazer-4", "ruhig": "standing/shirt-3",
         "laessig": "standing/easing-1"}
POSE_MIMIK = {"eilt": "eilt", "sorge": "sorge", "skeptisch": "skeptisch", "erklaert": "erklaert", "blazer": "froh",
              "ruhig": "ruhig", "laessig": "ruhig"}


def _farben(f):
    m = {"Skin": f.get("haut"), "Top": f.get("oberteil"), "Hair": f.get("haar"), "Hat": f.get("hut"),
         "Jacket": f.get("jacke") or f.get("oberteil"), "Blazer": f.get("jacke") or f.get("oberteil")}
    return {k: v for k, v in m.items() if v}


def _id(f):
    return hashlib.sha1(json.dumps(f, sort_keys=True).encode()).hexdigest()[:10]


class Besetzung:
    def __init__(self, figuren):
        self.figuren = figuren or {}

    def name(self, ref, cx=540):
        """Kürzel → Bilddatei-Name (ohne .png) im Figurenordner; erzeugt die Ansicht bei Bedarf."""
        if "/" in ref:
            rolle, key = ref.split("/", 1); art = "stand"
        else:
            rolle, key = ref.split(":", 1); art = "bueste"
        f = self.figuren[rolle]
        if art == "stand":
            pose, mimik = POSEN[key], MIMIK[POSE_MIMIK.get(key, "ruhig")]
        else:
            pose, mimik = "body/" + f.get("bueste", "Tee 1"), MIMIK[key]
        basis = f"{_id(f)}_{art}_{key}"
        rechts = cx < 540                      # links stehend → schaut nach rechts (Original)
        datei = basis + ("_r" if rechts else "")
        pfad = os.path.join(ORDNER, datei + ".png")
        if not os.path.exists(pfad):
            img = _figur(pose, f["kopf"], mimik, f.get("bart"), f.get("brille"), farben=_farben(f), hoehe=1200, spiegeln=not rechts)
            img.save(pfad)
        return datei
