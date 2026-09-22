#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { beitragRendern, browserBeenden } from "../src/render.mjs";
import { titelZeilen } from "../src/vorlagen.mjs";
import { themenpool, FAECHER } from "../src/inhalte.mjs";

const hier = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(hier, "..");
const quelle = path.resolve(root, process.env.HJ_RERENDER_SOURCE || ".rerender-source");
const out = path.join(root, "out", "cover-quality-v2-rerender");
fs.rmSync(out, { recursive: true, force: true });
fs.mkdirSync(out, { recursive: true });

function alleDateien(dir) {
  const aus = [];
  const stack = [dir];
  while (stack.length) {
    const aktuell = stack.pop();
    for (const eintrag of fs.readdirSync(aktuell, { withFileTypes: true })) {
      const p = path.join(aktuell, eintrag.name);
      if (eintrag.isDirectory()) stack.push(p);
      else aus.push(p);
    }
  }
  return aus;
}

function finde(name) {
  return alleDateien(quelle).find((p) => path.basename(p) === name) || null;
}

function findeSuffix(suffix) {
  const norm = suffix.split("/").join(path.sep);
  return alleDateien(quelle).find((p) => p.endsWith(norm)) || null;
}

function bildDaten(pfad) {
  return `data:image/png;base64,${fs.readFileSync(pfad).toString("base64")}`;
}

async function fahrlaessigeToetungAusDebug() {
  const quellen = [
    {
      id: "attempt-1-high",
      quality: "high",
      pfad: findeSuffix("debug/attempt-1-high/raw.png"),
      annotationPlan: {
        noteX: 0.18, noteY: 0.18,
        targetX: 0.83, targetY: 0.46,
        rotationDeg: -5, bend: 0.35,
      },
    },
    {
      id: "attempt-2-xhigh",
      quality: "xhigh",
      pfad: findeSuffix("debug/attempt-2-xhigh/raw.png"),
      annotationPlan: {
        noteX: 0.18, noteY: 0.18,
        targetX: 0.88, targetY: 0.48,
        rotationDeg: -5, bend: 0.35,
      },
    },
  ].filter((x) => x.pfad);

  if (!quellen.length) return false;

  const gesucht = /fahrl[aä]ssig(?:e|er|en|em|es)?\s+t[oö]tung/i;
  const thema = themenpool()
    .filter((t) => Number(t.klausur) === 2)
    .find((t) => gesucht.test(String(t.titel || "")));
  if (!thema) throw new Error("Im entschlüsselten Themenpool wurde kein Titel zur fahrlässigen Tötung gefunden.");

  const fachLabel = FAECHER[thema.fach]?.label || "Strafrecht";
  const coverText = "Vorhersehbar & vermeidbar?";
  const coverBadge = "Klausurrelevant";
  const ergebnisse = [];

  for (const quelleBild of quellen) {
    const folie = {
      art: "titel",
      titel: thema.titel,
      titelZeilen: titelZeilen(thema.titel),
      icon: "paragraf",
      coverText,
      coverBadge,
      bild: bildDaten(quelleBild.pfad),
      bildFrei: true,
      bildBreite: 1024,
      bildHoehe: 1024,
      bildTyp: "charakter",
      bildCharaktere: ["Rex Rohrbruch", "Zylla Glitch"],
      coverHinweisPlan: quelleBild.annotationPlan,
    };
    const beitrag = {
      format: "pruefungsfrage",
      fach: thema.fach,
      klausur: 2,
      fachLabel,
      slug: `single-strafrecht-rerender-${quelleBild.id}`,
      folien: [folie],
    };

    const [datei] = await beitragRendern(beitrag, out, { variante: 0 });
    const ziel = path.join(out, `cover-${quelleBild.id}.jpg`);
    if (datei !== ziel) fs.renameSync(datei, ziel);
    ergebnisse.push({
      source: path.relative(root, quelleBild.pfad),
      sourceAttempt: quelleBild.id,
      sourceQuality: quelleBild.quality,
      output: path.relative(root, ziel),
      annotationPlan: quelleBild.annotationPlan,
    });
  }

  const report = {
    generatedAt: new Date().toISOString(),
    sourceRunId: 35684151355,
    sourceArtifactId: 10676033128,
    currentCommit: process.env.GITHUB_SHA || null,
    topic: {
      id: thema.id,
      title: thema.titel,
      fach: thema.fach,
      fachLabel,
      normen: thema.normen || [],
    },
    coverText,
    coverBadge,
    providerCostUsd: 0,
    sourceImagesAlreadyPaid: true,
    visualQaRepeated: false,
    note: "Pure local renderer rerun from the two already-paid Run 47 PNGs. No provider/API calls were made.",
    results: ergebnisse,
  };
  fs.writeFileSync(path.join(out, "manifest.json"), JSON.stringify(report, null, 2));
  console.log(JSON.stringify(report, null, 2));
  return true;
}

async function legacyRerender() {
  const manifestPfad = finde("manifest.json");
  const motivPfad = finde("single-strafrecht.png");
  if (!manifestPfad || !motivPfad) throw new Error("Gespeichertes Single-Cover-Artifact unvollständig.");
  const manifest = JSON.parse(fs.readFileSync(manifestPfad, "utf8"));
  const thema = manifest.topic;
  const cover = manifest.cover;
  const hintTarget = String(process.env.HJ_HINT_TARGET || "the incomplete revision brief held by Rex").trim();
  const hintZone = String(process.env.HJ_HINT_ZONE || "auto").trim();

  const folie = {
    art: "titel",
    titel: thema.title,
    titelZeilen: titelZeilen(thema.title),
    icon: "paragraf",
    coverText: cover.coverText,
    coverBadge: cover.coverBadge,
    bild: bildDaten(motivPfad),
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
}

try {
  const debugGerendert = await fahrlaessigeToetungAusDebug();
  if (!debugGerendert) await legacyRerender();
} finally {
  await browserBeenden().catch(() => {});
}
