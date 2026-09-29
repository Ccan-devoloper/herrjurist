#!/usr/bin/env python3
"""Index and extract exact heading sections from the uploaded UNCERTIFIED corpus.

Examples:
  python gesamtwissen_index.py build --source /path/Jura_Gesamtwissen_...html
  python gesamtwissen_index.py plan --source /path/Jura_Gesamtwissen_...html \
      --workbook /path/HerrJurist_156_YouTube_Themenplan.xlsx --out output
  python gesamtwissen_index.py extract --source /path/source.html --anchor anfechtungsgruende
  python gesamtwissen_index.py query --source /path/source.html --out output --query frist

The HTML is explicitly UNCERTIFIED and is NOT an authority for current law.
Every legal proposition requires separate validation against current official
statutes and primary court decisions before script approval. An exact anchor
match proves only source routing, never legal correctness or completeness.

Requires lxml. Input files are explicit and remain outside the repository;
the tool writes local JSONL indexes and a 156-episode JSON source map.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import zipfile
from collections import Counter
from pathlib import Path
from xml.etree import ElementTree as ET

from lxml import html


SOURCE: Path
INDEX: Path
ARTICLE_INDEX: Path
META: Path


def configure(source: Path, out: Path):
    global SOURCE, INDEX, ARTICLE_INDEX, META
    SOURCE = source.resolve()
    INDEX = out / "heading-index.jsonl"
    ARTICLE_INDEX = out / "article-index.jsonl"
    META = out / "source-meta.json"
    if not SOURCE.is_file():
        raise FileNotFoundError(f"HTML source not found: {SOURCE}")


def find_local_input(pattern: str):
    """Convenience only; explicit --source/--workbook is best for reproducibility."""
    for directory in (Path.cwd() / "upload", Path.cwd()):
        matches = sorted(directory.glob(pattern))
        if len(matches) == 1:
            return matches[0]
    return None

TOPICS_15_20 = {
    15: ("Akte statt Lehrbuch: So funktioniert die Relation", "Band 4 · 2. Relationstechnik", "relationstechnik"),
    16: ("Falscher Preis im Onlineshop: Muss der Händler liefern?", "Band 1 · 4.1 Anfechtungsgruende", "anfechtungsgruende"),
    17: ("Öffentlich-rechtliche Akte: Was ist wirklich entscheidend?", "Band 5 · 1.3 Aktenauswertung", "aktenauswertung"),
    18: ("Körperverletzung: Zählt schon eine Ohrfeige?", "Band 3 · 35.1 Koerperverletzung, § 223 StGB", "koerperverletzung-223-stgb"),
    19: ("AGB-Falle: Welche Klauseln gelten überhaupt?", "Band 1 · 7.3 Allgemeine Geschaeftsbedingungen", "allgemeine-geschaeftsbedingungen"),
    20: ("Verfassungsbeschwerde: Kann jeder nach Karlsruhe?", "Band 2 · 19.4 Verfassungsbeschwerde", "verfassungsbeschwerde"),
}

TOPIC_SUPPORT = {
    15: ["relation-voll", "2ex-akte-methode", "jo-learn-4121-excursus-c748563e90"],
    16: ["anfechtungserklaerung-frist-und-rechtsfolgen", "anfechtung-119-ff.-142-bgb", "der-preisfehler-im-technikshop---festplatte-muster"],
    17: ["2ex-akte-methode", "relation-voll"],
    18: ["sr-koerperverletzung", "vollaudit-838", "vollaudit-3409"],
    19: ["agb-kontrolle-305-ff.-bgb", "agb-einbeziehung-und-überraschende-klauseln", "vollaudit-178"],
    20: ["verfassungsbeschwerde---komplettschema", "verfassungsbeschwerde-und-aktuelle-art.-94-systematik", "vollaudit-3465"],
}


def norm(s: str) -> str:
    return " ".join(s.split())


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def load():
    return html.parse(str(SOURCE)).getroot()


def heading_text(h):
    return norm(" ".join(h.itertext()))


def section_nodes(h):
    level = int(h.tag[1])
    for sibling in h.itersiblings():
        if sibling.tag in ("h1", "h2", "h3", "h4", "h5", "h6") and int(sibling.tag[1]) <= level:
            break
        # The audit annex is a giant ledger, not doctrinal content of the preceding heading.
        if sibling.get("id") == "update30-audit-annex":
            break
        if sibling.tag in ("script", "style", "nav"):
            continue
        yield sibling


def section_lines(h):
    lines = []
    for n in section_nodes(h):
        if n.tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            lines.append("#" * int(n.tag[1]) + " " + heading_text(n))
        elif n.tag == "p":
            lines.append(norm(" ".join(n.itertext())))
        elif n.tag in ("ul", "ol"):
            for i, li in enumerate(n.xpath("./li"), 1):
                mark = f"{i}." if n.tag == "ol" else "-"
                lines.append(f"{mark} {norm(' '.join(li.itertext()))}")
        elif n.tag == "table":
            for row in n.xpath(".//tr"):
                lines.append(" | ".join(norm(" ".join(c.itertext())) for c in row.xpath("./th|./td")))
        elif n.tag in ("article", "section", "div"):
            # Preserve the visible nested block while avoiding script/style text.
            for bad in n.xpath(".//script|.//style"):
                bad.drop_tree()
            lines.append(norm(" ".join(n.itertext())))
    return [line for line in lines if line]


def doc_meta(root):
    audit = root.xpath('//*[@id="update30-audit-annex"]')
    rows = audit[0].xpath('.//table[@id="currentLedger"]//tbody/tr') if audit else []
    formal = Counter(norm(" ".join(row.xpath("./td")[4].itertext())) for row in rows)
    current = Counter(norm(" ".join(row.xpath("./td")[13].itertext())) for row in rows)
    return {
        "source_path": str(SOURCE),
        "source_sha256": sha256(SOURCE),
        "source_bytes": SOURCE.stat().st_size,
        "document_title": heading_text(root.xpath("//title")[0]),
        "current_working_view": "UPDATE30, 2026-09-24, UNCERTIFIED",
        "historical_corpus_date": "2026-09-13",
        "audit_row_count": len(rows),
        "audit_formal_flags": dict(formal),
        "update30_row_status": dict(current),
        "warning": "Historical PREAUDIT corpus and row-level formal source audit; every legal statement requires independent current-law verification using official norms and primary decisions.",
    }


def build():
    root = load()
    INDEX.parent.mkdir(parents=True, exist_ok=True)
    meta = doc_meta(root)
    META.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    count = 0
    with INDEX.open("w", encoding="utf-8") as f:
        for h in root.xpath("//body//h1|//body//h2|//body//h3|//body//h4"):
            if not h.get("id") or h.xpath('ancestor::nav|ancestor::*[@id="update30-audit-annex"]'):
                continue
            title = heading_text(h)
            preview = []
            for n in section_nodes(h):
                if n.tag in ("p", "h3", "h4"):
                    preview.append(norm(" ".join(n.itertext())))
                if len(" ".join(preview)) >= 500:
                    break
            obj = {
                "anchor": h.get("id"),
                "heading": title,
                "level": int(h.tag[1]),
                "parent_id": h.getparent().get("id"),
                "parent_class": h.getparent().get("class"),
                "excerpt": " ".join(preview)[:500],
                "source_sha256": meta["source_sha256"],
                "provenance": "historical corpus or appended working addendum; UNCERTIFIED, not current-law authority",
            }
            f.write(json.dumps(obj, ensure_ascii=False) + "\n")
            count += 1
    articles = 0
    with ARTICLE_INDEX.open("w", encoding="utf-8") as f:
        for n in root.xpath('//body//article[@id][@data-source-url]'):
            title_node = n.xpath('./h1|./h2|./h3|./h4')
            label = heading_text(title_node[0]) if title_node else ""
            source_url = n.get("data-source-url")
            excerpt = norm(" ".join(n.itertext()))[:1600]
            record = {
                "anchor": n.get("id"),
                "title": label,
                "data_source_url": source_url,
                "page_id": n.get("data-page-id"),
                "page_type": n.get("data-page-type"),
                "audit_status": n.get("data-full-content-status"),
                "audit_date": n.get("data-audit-date") or n.get("data-full-content-audit"),
                "excerpt": excerpt,
                "source_sha256": meta["source_sha256"],
                "provenance": "source-route mapping or historical audit paragraph, NOT current-law validation",
            }
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
            articles += 1
    print(f"indexed {count} headings -> {INDEX}")
    print(f"indexed {articles} source-linked articles -> {ARTICLE_INDEX}")
    print(f"audit {meta['audit_row_count']} rows: {meta['audit_formal_flags']}")


def extract(anchor: str, target: Path | None = None, topic: tuple | None = None):
    root = load()
    nodes = root.xpath('//*[@id=$id]', id=anchor)
    if len(nodes) != 1:
        raise RuntimeError(f"anchor {anchor!r}: expected 1 DOM node, found {len(nodes)}")
    h = nodes[0]
    meta = doc_meta(root)
    if h.tag in ("h1", "h2", "h3", "h4"):
        title = heading_text(h)
        lines = section_lines(h)
        source_info = "HTML-Überschrift"
    elif h.tag == "article" and h.get("data-source-url"):
        title_node = h.xpath('./h1|./h2|./h3|./h4')
        title = heading_text(title_node[0]) if title_node else anchor
        lines = [norm(" ".join(x.itertext())) for x in h if x.tag not in ("script", "style")]
        source_info = f"Artikel-Repräsentation `{h.get('data-source-url')}` · page-id `{h.get('data-page-id')}` · Status `{h.get('data-full-content-status')}`"
    else:
        raise RuntimeError(f"anchor {anchor!r} is not an indexed heading or source-linked article")
    label = topic[0] if topic else title
    source_band = topic[1] if topic else "by exact HTML anchor"
    header = [
        f"# {label}",
        "",
        f"Originalabschnitt: `{source_band}` · HTML-Anker `#{anchor}` · Überschrift „{title}“ · {source_info}.",
        f"Quelle: `{SOURCE.name}` · SHA-256 `{meta['source_sha256']}` · UPDATE30 24.09.2026 · **UNCERTIFIED**. Historischer Korpusstand: 13.09.2026. Kein amtlicher Rechtsnachweis.",
        "",
        "## Unbearbeiteter Korpusauszug",
        "",
    ]
    body = "\n\n".join(header + lines) + "\n"
    if target is None:
        print(body)
    else:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(body, encoding="utf-8")
        print(f"wrote {target}, {len(lines)} blocks, {len(body)} chars")
    return len(lines)


def read_jahresplan(workbook: Path):
    """Read the two-column-style XLSX XML without adding a workbook dependency."""
    main_ns = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
    rel_ns = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
    package_ns = "{http://schemas.openxmlformats.org/package/2006/relationships}"
    with zipfile.ZipFile(workbook) as z:
        strings = []
        if "xl/sharedStrings.xml" in z.namelist():
            root = ET.fromstring(z.read("xl/sharedStrings.xml"))
            strings = ["".join(si.itertext()) for si in root.findall(f"{main_ns}si")]
        wb = ET.fromstring(z.read("xl/workbook.xml"))
        sheets = wb.find(f"{main_ns}sheets")
        sheet = next(s for s in sheets if s.attrib.get("name") == "Jahresplan")
        relationship = sheet.attrib[f"{rel_ns}id"]
        rels = ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))
        target = next(r.attrib["Target"] for r in rels.findall(f"{package_ns}Relationship") if r.attrib["Id"] == relationship)
        member = target.lstrip("/") if target.startswith("/") else "xl/" + target
        root = ET.fromstring(z.read(member))
        result = []
        for row in root.findall(f".//{main_ns}sheetData/{main_ns}row"):
            cells = {}
            for c in row.findall(f"{main_ns}c"):
                key = re.match(r"[A-Z]+", c.attrib["r"]).group()
                value = c.find(f"{main_ns}v")
                if c.attrib.get("t") == "inlineStr":
                    inline = c.find(f"{main_ns}is")
                    cells[key] = "".join(inline.itertext()) if inline is not None else ""
                elif value is None:
                    cells[key] = None
                elif c.attrib.get("t") == "s":
                    cells[key] = strings[int(value.text)]
                elif c.attrib.get("t") in ("str", "e"):
                    cells[key] = value.text
                else:
                    cells[key] = float(value.text) if "." in value.text else int(value.text)
            if isinstance(cells.get("A"), int):
                result.append({
                    "topic_id": cells["A"],
                    "week": cells.get("B"),
                    "field": cells.get("D"),
                    "exam": cells.get("E"),
                    "title": cells.get("F"),
                    "hook": cells.get("G"),
                    "five_minute_goal": cells.get("H"),
                    "workbook_source": cells.get("J"),
                    "workbook_html_anchor": cells.get("K"),
                    "exam_focus": cells.get("L"),
                })
    ids = [r["topic_id"] for r in result]
    if ids != list(range(1, 157)):
        raise ValueError(f"Expected workbook IDs 1..156 in order, got {len(ids)} rows and IDs {ids[:5]}…{ids[-5:]}")
    return result


def make_plan(workbook: Path, out: Path):
    current_hash = sha256(SOURCE)
    if not INDEX.exists() or not META.exists() or json.loads(META.read_text(encoding="utf-8")).get("source_sha256") != current_hash:
        build()
    headings = {x["anchor"]: x for x in map(json.loads, INDEX.read_text(encoding="utf-8").splitlines())}
    articles = {x["anchor"]: x for x in map(json.loads, ARTICLE_INDEX.read_text(encoding="utf-8").splitlines())}
    rows = read_jahresplan(workbook)
    repeat_count = Counter((r["workbook_html_anchor"] or "").lstrip("#") for r in rows)
    mapping = []
    for r in rows:
        anchor = (r["workbook_html_anchor"] or "").lstrip("#")
        node = headings.get(anchor) or articles.get(anchor)
        broad = repeat_count[anchor] > 1
        mapping.append({
            **r,
            "match_status": "exact_html_id" if node else "unmatched",
            "mapping_confidence": "exact_broad_heading_review_subtopic" if node and broad else ("exact_unique_heading" if node else "unmatched"),
            "html_anchor": anchor,
            "html_heading": node.get("heading", node.get("title")) if node else None,
            "excerpt": node.get("excerpt") if node else None,
            "source_provenance": {
                "html_file": SOURCE.name,
                "html_sha256": current_hash,
                "location": f"#{anchor}",
                "source_kind": "heading" if anchor in headings else ("source_linked_article" if anchor in articles else "missing"),
                "legal_validation": "NOT VALIDATED: check current official norms and primary decisions separately",
            },
        })
    out.mkdir(parents=True, exist_ok=True)
    payload = {
        "workbook_file": workbook.name,
        "workbook_sha256": sha256(workbook),
        "html_file": SOURCE.name,
        "html_sha256": current_hash,
        "warning": "The workbook and HTML are UNCERTIFIED editorial leads, not current-law authorities. Mapping confidence concerns exact HTML IDs only.",
        "total": len(mapping),
        "unmatched_ids": [r["topic_id"] for r in mapping if r["match_status"] == "unmatched"],
        "reused_anchors": {k: v for k, v in repeat_count.items() if v > 1},
        "topics": mapping,
    }
    target = out / "topics-001-156-source-map.json"
    target.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Mapped {len(mapping)} workbook IDs, {len(payload['unmatched_ids'])} unmatched, {len(payload['reused_anchors'])} reused anchors -> {target}")
    return payload


def main():
    p = argparse.ArgumentParser()
    p.add_argument("action", choices=("build", "extract", "topics", "query", "plan"))
    p.add_argument("--source", type=Path, default=find_local_input("Jura_Gesamtwissen_*UPDATE30*FULL4958*UNCERTIFIED*.html"), help="exact local UNCERTIFIED HTML input")
    p.add_argument("--workbook", type=Path, default=find_local_input("HerrJurist_156_YouTube_Themenplan*.xlsx"), help="exact local 156-topic workbook input")
    p.add_argument("--anchor")
    p.add_argument("--out", default="corpus-extracts")
    p.add_argument("--query")
    args = p.parse_args()
    if args.source is None:
        p.error("provide --source /path/to/UNCERTIFIED.html")
    out = Path(args.out).resolve()
    configure(args.source, out)
    if args.action == "build":
        build()
    elif args.action == "extract":
        if not args.anchor:
            p.error("extract requires --anchor")
        extract(args.anchor)
    elif args.action == "topics":
        manifest = []
        for ident, topic in TOPICS_15_20.items():
            extract(topic[2], out / f"{ident:03d}-{topic[2]}.md", topic)
            supp = []
            for j, anchor in enumerate(TOPIC_SUPPORT[ident], 1):
                target = out / f"{ident:03d}-supp-{j:02d}-{anchor}.md"
                extract(anchor, target, (topic[0], f"Ergänzender Originalanker #{anchor}"))
                supp.append({"anchor": anchor, "file": target.name})
            manifest.append({
                "topic_id": ident,
                "title": topic[0],
                "workbook_source": topic[1],
                "primary_html_anchor": topic[2],
                "primary_file": f"{ident:03d}-{topic[2]}.md",
                "support": supp,
                "legal_status": "UNCERTIFIED corpus evidence only; official current-law audit pending",
            })
        (out / "topics-015-020-map.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    elif args.action == "plan":
        if args.workbook is None:
            p.error("plan requires --workbook /path/to/HerrJurist_156...xlsx")
        make_plan(args.workbook.resolve(), out)
    else:
        if not args.query:
            p.error("query requires --query")
        q = args.query.casefold()
        if not INDEX.exists():
            build()
        hits = (json.loads(line) for line in INDEX.read_text(encoding="utf-8").splitlines())
        hits = [x for x in hits if q in (x["heading"] + " " + x["excerpt"]).casefold()]
        for x in hits[:30]:
            print(f"#{x['anchor']} [{x['level']}] {x['heading']} :: {x['excerpt'][:150]}")
        if ARTICLE_INDEX.exists():
            articles = (json.loads(line) for line in ARTICLE_INDEX.read_text(encoding="utf-8").splitlines())
            articles = [x for x in articles if q in (x["title"] + " " + x["data_source_url"]).casefold()]
            for x in articles[:15]:
                print(f"#{x['anchor']} [article {x['page_id']}] {x['title']} :: {x['data_source_url']}")


if __name__ == "__main__":
    main()
