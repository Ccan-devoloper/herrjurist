#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { beitragRendern, browserBeenden } from "../src/render.mjs";
import { titelZeilen } from "../src/vorlagen.mjs";

const hier = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(hier, "..");
const quelle = path.resolve(root, process.env.HJ_RERENDER_SOURCE || ".rerender-source");
const out = path.join(root, "out", "cover-quality-v2-rerender");
fs.rmSync(out, { recursive: true, force: true });
fs.mkdirSync(out, { recursive: true });

function finde(name) {
  const stack = [quelle];
  while (stack.length) {
    const dir = stack.pop();
    for (const eintrag of fs.readdirSync(dir, { withFileTypes: true })) {
      const p = path.join(dir, eintrag.name);
      if (eintrag.isDirectory()) stack.push(p);
      else if (eintrag.name === name) return p;
    }
  }
  return null;
}

const manifestPfad = finde("manifest.json");
const motivPfad = finde("single-strafrecht.png");
if (!manifestPfad || !motivPfad) throw new Error("Gespeichertes Single-Cover-Artifact unvollständig.");
const manifest = JSON.parse(fs.readFileSync(manifestPfad, "utf8"));
const thema = manifest.topic;
const cover = manifest.cover;
const hintTarget = String(process.env.HJ_HINT_TARGET || "the incomplete revision brief held by Rex").trim();
const hintZone = String(process.env.HJ_HINT_ZONE || "auto").trim();

const bild = `data:image/png;base64,${fs.readFileSync(motivPfad).toString("base64")}`;
const folie = {
  art: "titel",
  titel: thema.title,
  titelZeilen: titelZeilen(thema.title),
  icon: "paragraf",
  coverText: cover.coverText,
  coverBadge: cover.coverBadge,
  bild,
  bildFrei: true,
  bildBreite: cover.motifDimensions?.width || 1024,
  bildHoehe: cover.motifDimensions?.height || 960,
  bildTyp: "charakter",
  bildCharaktere: cover.renderedCharacters || [],
  coverHinweisPlan: cover.annotationPlan || {
    noteX: 0.52, noteY: 0.14,
    targetX: 0.62, targetY: 0.47,
    rotationDeg: -4, bend: 0.35,
  },
};
const beitrag = {
  format: "pruefungsfrage",
  fach: thema.fach,
  klausur: 2,
  fachLabel: thema.fachLabel,
  slug: "single-strafrecht-rerender",
  coverRegie: {
    ...(cover.director || {}),
    hinweisZiel: hintTarget,
    hinweisZone: hintZone,
  },
  folien: [folie],
};

try {
  const [datei] = await beitragRendern(beitrag, out, { variante: 0 });
  const ziel = path.join(out, "cover-rerendered.jpg");
  if (datei !== ziel) fs.renameSync(datei, ziel);
  const report = {
    generatedAt: new Date().toISOString(),
    sourceRunId: 35658855942,
    sourceCommit: manifest.commit,
    currentCommit: process.env.GITHUB_SHA || null,
    topic: thema,
    titleLines: titelZeilen(thema.title),
    coverText: cover.coverText,
    coverBadge: cover.coverBadge,
    hintTarget,
    hintZone,
    providerCostUsd: 0,
    note: "Pure renderer rerun using the already-paid QA-approved PNG motif. No provider/API calls.",
  };
  fs.writeFileSync(path.join(out, "manifest.json"), JSON.stringify(report, null, 2));
  console.log(JSON.stringify(report, null, 2));
} finally {
  await browserBeenden().catch(() => {});
}
