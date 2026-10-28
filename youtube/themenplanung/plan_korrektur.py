#!/usr/bin/env python3
"""Korrigiert einzelne Felder einer Folge in themenplan-780.csv, ohne die übrigen Zeilen anzufassen
(CRLF, BOM und Quoting bleiben erhalten), und spiegelt die Beschreibung in seo_*.json.

    python3 plan_korrektur.py NR "Feldname=neuer Wert" ["Feldname=neuer Wert" …]

Feldnamen wie in der Kopfzeile, z. B. "Normen", "Leitentscheidung", "Beschreibung (Anfang)".
Nur nach Rechtsprüfung einer Folge verwenden; die Änderung im RECHTSSTAND.md der Folge begründen."""
import csv, glob, io, json, os, sys

HIER = os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(HIER, "themenplan-780.csv")


def zeile_schreiben(felder):
    buf = io.StringIO()
    csv.writer(buf, delimiter=";", lineterminator="\r\n").writerow(felder)
    return buf.getvalue()


def main():
    nr, aenderungen = sys.argv[1], [a.split("=", 1) for a in sys.argv[2:]]
    roh = open(CSV, "rb").read().decode("utf-8")
    bom = roh.startswith("﻿")
    zeilen = (roh[1:] if bom else roh).split("\r\n")
    kopf = next(csv.reader([zeilen[0]], delimiter=";"))
    for i, z in enumerate(zeilen[1:], 1):
        if not z:
            continue
        felder = next(csv.reader([z], delimiter=";"))
        if felder[0] != nr:
            continue
        assert zeile_schreiben(felder).rstrip("\r\n") == z, "Quoting dieser Zeile ließe sich nicht verlustfrei erhalten"
        alt_beschr = felder[kopf.index("Beschreibung (Anfang)")]
        for feld, wert in aenderungen:
            assert ";" not in wert or True
            felder[kopf.index(feld)] = wert
            print(f"Folge {nr}: {feld}: {wert}")
        zeilen[i] = zeile_schreiben(felder).rstrip("\r\n")
        neu_beschr = felder[kopf.index("Beschreibung (Anfang)")]
        break
    else:
        sys.exit(f"Folge {nr} nicht gefunden")
    open(CSV, "wb").write((("﻿" if bom else "") + "\r\n".join(zeilen)).encode("utf-8"))
    rows = list(csv.reader(open(CSV, encoding="utf-8-sig"), delimiter=";"))
    assert all(len(r) == len(kopf) for r in rows if r), "Spaltenzahl stimmt nicht mehr"
    if neu_beschr != alt_beschr:
        for f in glob.glob(os.path.join(HIER, "seo_*.json")):
            s = open(f, encoding="utf-8").read()
            alt_js = json.dumps(alt_beschr, ensure_ascii=False)
            if alt_js in s:
                open(f, "w", encoding="utf-8").write(s.replace(alt_js, json.dumps(neu_beschr, ensure_ascii=False)))
                print("Beschreibung auch in", os.path.basename(f))


if __name__ == "__main__":
    main()
