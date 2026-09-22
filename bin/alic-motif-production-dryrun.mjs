#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { fileURLToPath } from "node:url";
import { Hosting } from "../src/hosting.mjs";
import { beitragRendern, browserBeenden } from "../src/render.mjs";

const hier = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(hier, "..");
const sourceDir = path.resolve(root, process.env.HJ_ALIC_SOURCE || ".alic-source");
const motif = path.join(sourceDir, "motifs", "single-strafrecht-alic.png");
const out = path.join(root, "out", "alic-motif-production-dryrun");
fs.rmSync(out, { recursive: true, force: true });
fs.mkdirSync(out, { recursive: true });

if (!fs.existsSync(motif)) throw new Error(`Motiv fehlt: ${motif}`);

const hosting = new Hosting({ pushen: false }).vorbereiten();
const datum = "2026-09-22";
const slot = "b2";
const sourcePath = path.join(hosting.stateDir, "inhalte", `${datum}-${slot}.json`);
if (!fs.existsSync(sourcePath)) throw new Error(`Gespeicherter Feed-Beitrag fehlt: ${sourcePath}`);

const inhalt = JSON.parse(fs.readFileSync(sourcePath, "utf8"));
const title = inhalt.folien?.find((f) => f.art === "titel");
if (!title) throw new Error("Titelfolie fehlt.");

const motifBytes = fs.readFileSync(motif);
title.bild = `data:image/png;base64,${motifBytes.toString("base64")}`;
title.bildQuelle = null;
title.bildFrei = true;
title.bildTyp = "charakter";
title.bildBreite = 1024;
title.bildHoehe = 918;
title.bildCharaktere = ["Rex Rohrbruch", "FORM-7"];
title.coverHinweisPlan = {
  noteX: 0.68,
  noteY: 0.43,
  targetX: 0.64,
  targetY: 0.44,
  rotationDeg: -6,
  bend: 0.25
};

const renderDir = path.join(out, "rendered");
const files = await beitragRendern(inhalt, renderDir, { variante: 0 });
const cover = files.find((f) => /-01\.jpg$/i.test(f)) || files[0];

fs.copyFileSync(motif, path.join(out, "single-strafrecht-alic.png"));
fs.copyFileSync(cover, path.join(out, "cover.jpg"));

const manifest = {
  generatedAt: new Date().toISOString(),
  productionCommitUnderTest: process.env.GITHUB_SHA || null,
  sourceContent: `instagram-assets:state/inhalte/${datum}-${slot}.json`,
  sourceTopic: inhalt.folien?.[0]?.titel || null,
  motif: "single-strafrecht-alic.png",
  motifSourceArtifactId: 10674227857,
  motifSourceRunId: 35681116751,
  motifSha256: crypto.createHash("sha256").update(motifBytes).digest("hex"),
  motifDimensions: { width: 1024, height: 918 },
  annotationPlan: title.coverHinweisPlan,
  targetContract: "Cover Quality v2 / fb2fc680 / handwritten note without arrow",
  providerCostUsd: 0,
  externalProviderCalls: false,
  notes: [
    "Uses the exact already-generated, alpha-channel ALIC motif from the original single-cover artifact.",
    "Uses current production renderer code from main; only the test harness lives on this dry-run branch.",
    "No OpenAI, Anthropic, image-generation, Pexels, ElevenLabs or publishing call is made.",
    "Legacy fields from the saved b2 content are deliberately left intact so duplicate-note regressions are exercised."
  ],
  outputs: files.map((f) => path.relative(out, f)),
  cover: path.relative(out, cover)
};
fs.writeFileSync(path.join(out, "manifest.json"), JSON.stringify(manifest, null, 2));
fs.writeFileSync(path.join(out, "README.txt"), [
  "Herr Jurist – production renderer dry run with exact ALIC motif",
  "Source feed content: 2026-09-22-b2 (Allein gerast: § 315d StGB?)",
  "Motif: single-strafrecht-alic.png from original ALIC artifact",
  "Renderer target: current main Cover Quality v2 no-arrow",
  "Provider/API cost: $0.00",
  "No publishing performed."
].join("\n"));

await browserBeenden();
console.log(JSON.stringify(manifest, null, 2));
