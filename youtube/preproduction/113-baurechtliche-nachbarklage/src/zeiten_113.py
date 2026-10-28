"""Hilfsausgabe Folge 113: Hauptfilmzeit (s) eines Wortes nach einer Marke, für Einzelbild-Prüfungen.
Aufruf: python3 zeiten_113.py marke:wort[:nr] …"""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine as B
for a in sys.argv[1:]:
    t = a.split(":")
    c = B.beim(t[0], t[1], int(t[2]) if len(t) > 2 else 1) if len(t) > 1 else t[0]
    print(round(B._t(c), 2), end=",")
