#!/usr/bin/env python3
"""Human 02/06 style gate: prepare visual comparison and validate recorded reviews.

This deliberately does not infer aesthetic similarity from pixels or embeddings.
The 80/100 score is entered by a reviewer using MASTERSTANDARD-09.md § 2.
"""

import argparse
import csv
import html
import json
import sys
from datetime import date
from pathlib import Path


WEIGHTS = {"figure": 30, "contour": 20, "shape": 20, "color": 15, "calm": 15}
COLUMNS = ["asset", *WEIGHTS, "veto", "reviewer", "date", "golden_reference", "notes"]
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp"}


def images(assets):
    return sorted(
        (p.relative_to(assets).as_posix() for p in assets.rglob("*")
         if p.is_file() and p.suffix.lower() in IMAGE_SUFFIXES),
        key=lambda s: s.casefold(),
    )


def make_csv(path, names):
    if path.exists():
        raise ValueError(f"Scores file already exists: {path}. Keep prior human decisions.")
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows({"asset": name} for name in names)


def make_gallery(path, assets, names, ref02, ref06, golden):
    def shown_image(p, label):
        src = html.escape(p.resolve().as_uri(), quote=True)
        return f'<a href="{src}" target="_blank"><img src="{src}" alt="{html.escape(label)}"></a>'

    rows = []
    for name in names:
        current = assets / name
        refs = [shown_image(ref02, "Master 02"), shown_image(ref06, "Master 06")]
        if golden:
            refs.append(shown_image(golden, "Golden Reference (falls diese Figur gezeigt wird)"))
        rows.append(
            f'<section><h2>{html.escape(name)}</h2><div class="grid">'
            + "".join(f'<figure>{image}<figcaption>{caption}</figcaption></figure>'
                      for image, caption in zip(
                          [*refs, shown_image(current, name)],
                          ["02", "06", *(["Golden Reference"] if golden else []), "Neues Bild"],
                      ))
            + '</div><p>Jedes Bild anklicken und bei 100 % prüfen. Wertung in der CSV eintragen.</p></section>'
        )
    document = """<!doctype html><html lang="de"><meta charset="utf-8">
<title>Herrjurist · Stil-Gate 80/100</title>
<style>body{font:16px system-ui,sans-serif;background:#11204a;color:#fafdff;margin:2rem}
h1,h2{color:#ffad76}section{border:1px solid #ff8447;border-radius:14px;padding:1rem;margin:1.5rem 0}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:1rem}
figure{margin:0}img{display:block;width:100%;height:auto}figcaption{margin-top:.4rem}
a{color:#ffe3ce}</style>
<h1>02/06-Stil-Gate</h1><p>Die Bilder werden hier verkleinert; Klick öffnet die native Datei zur 100-%-Ansicht.
Die Wertung ist ein menschliches Urteil. Andere Schauplätze und Requisiten sind erlaubt.</p>""" + "".join(rows) + "</html>"
    path.write_text(document, encoding="utf-8")


def validate(scores_path, names):
    with scores_path.open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames or any(col not in reader.fieldnames for col in COLUMNS):
            raise ValueError(f"CSV must contain: {', '.join(COLUMNS)}")
        rows = list(reader)
    seen = [row["asset"] for row in rows]
    if len(seen) != len(set(seen)):
        raise ValueError("Duplicate asset names in score CSV")
    if set(seen) != set(names):
        missing = sorted(set(names) - set(seen))
        extra = sorted(set(seen) - set(names))
        raise ValueError(f"CSV/assets mismatch. Missing: {missing}; extra: {extra}")

    findings = []
    for row in rows:
        reasons = []
        values = {}
        for category in WEIGHTS:
            raw = row[category].strip()
            if raw not in {"0", "1", "2", "3", "4", "5"}:
                reasons.append(f"{category}: human score 0–5 missing")
            else:
                values[category] = int(raw)
        if not row["reviewer"].strip() or not row["date"].strip():
            reasons.append("reviewer/date missing")
        try:
            if row["date"].strip():
                date.fromisoformat(row["date"].strip())
        except ValueError:
            reasons.append("date must be YYYY-MM-DD")
        veto = row["veto"].strip().lower()
        if veto not in {"yes", "no"}:
            reasons.append("veto must be yes or no")
        elif veto == "yes":
            reasons.append("hard veto declared")
        score = sum(WEIGHTS[k] * values[k] / 5 for k in values)
        if len(values) == len(WEIGHTS):
            if score < 80:
                reasons.append(f"total {score:g}/100 < 80")
            for category in ("figure", "contour"):
                if values[category] < 4:
                    reasons.append(f"{category} < 4/5")
            for category in ("shape", "color", "calm"):
                if values[category] < 3:
                    reasons.append(f"{category} < 3/5")
        findings.append({"asset": row["asset"], "human_score": score if len(values) == len(WEIGHTS) else None,
                         "passed": not reasons, "reasons": reasons, "reviewer": row["reviewer"],
                         "review_date": row["date"], "golden_reference": row["golden_reference"]})
    return {"basis": "human review, not an automated similarity metric",
            "passed": all(item["passed"] for item in findings), "asset_count": len(names),
            "results": findings}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--assets", required=True, type=Path, help="Anchor or final image folder")
    parser.add_argument("--ref02", required=True, type=Path, help="Approved full-size frame from 02")
    parser.add_argument("--ref06", required=True, type=Path, help="Approved full-size frame from 06")
    parser.add_argument("--golden", type=Path, help="Additional large character Golden Reference")
    parser.add_argument("--out", required=True, type=Path, help="Output folder for gallery and CSV")
    parser.add_argument("--validate", action="store_true", help="Check completed CSV; write report JSON")
    args = parser.parse_args()
    for p in [args.ref02, args.ref06, *([args.golden] if args.golden else [])]:
        if not p.is_file():
            parser.error(f"Reference missing: {p}")
    if not args.assets.is_dir():
        parser.error(f"Image directory missing: {args.assets}")
    names = images(args.assets)
    if not names:
        parser.error(f"No image assets found in {args.assets}")
    args.out.mkdir(parents=True, exist_ok=True)
    scores_path = args.out / "scores.csv"
    gallery_path = args.out / "compare.html"
    if not scores_path.exists():
        make_csv(scores_path, names)
    make_gallery(gallery_path, args.assets, names, args.ref02, args.ref06, args.golden)
    print(f"Review {len(names)} images: {gallery_path}\nHuman scores: {scores_path}")
    if args.validate:
        try:
            result = validate(scores_path, names)
        except ValueError as e:
            parser.error(str(e))
        report = args.out / "style-gate-report.json"
        report.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"{'PASS' if result['passed'] else 'FAIL'}: {report}")
        return 0 if result["passed"] else 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
