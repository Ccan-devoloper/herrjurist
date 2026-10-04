"""Vertonung Folge 165 über ../../stimme-elevenlabs/synth_el.py (dort nichts geändert).
Ergänzt nur für diese Folge Aussprachehilfen für lateinische Begriffe (deutsche Juristenaussprache), wie es
synth_el.AUSSPRACHE vorsieht: Skript, Tafeln und Untertitel behalten die normale Schreibung; cues.json enthält die
gesprochene Form („pöna“, „zerta“, „präwia“) – beim()-Anker darauf setzen, Untertitel in meta_165.py zurückführen.
Aufruf im src-Ordner: python3 vertonen_165.py"""
import fcntl, os, sys
sys.path.insert(0, ".")
sys.path.insert(0, "../../stimme-elevenlabs")
import synth_el

LATEIN = [(r"\bpoena\b", "pöna"), (r"\bcerta\b", "zerta"), (r"\bpraevia\b", "präwia")]
synth_el.AUSSPRACHE = list(synth_el.AUSSPRACHE) + LATEIN

if __name__ == "__main__":
    sperre = open(os.path.join(os.path.dirname(os.path.abspath(synth_el.__file__)), ".vertonung.lock"), "w")
    fcntl.flock(sperre, fcntl.LOCK_EX)          # wie synth_el.py: nie zwei Vertonungen gleichzeitig
    synth_el.main("skript_165", "carla")
