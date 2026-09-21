#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";
import { execFileSync } from "node:child_process";
import { fileURLToPath } from "node:url";
import { titelbild } from "../src/bilder.mjs";
import { beitragRendern, browserBeenden } from "../src/render.mjs";
import { budgetStarten } from "../src/budget.mjs";
import { kontextSetzen, kontextLoeschen } from "../src/anbieter.mjs";
import { budgetSetzen, abschluss as kostenAbschluss } from "../src/kosten.mjs";

const hier = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(hier, "..");
const out = path.join(root, "out", "charakter-test");
fs.rmSync(out, { recursive: true, force: true });
fs.mkdirSync(out, { recursive: true });

const faelle = [
  { path: "state/inhalte/2026-09-20-b2.json", art: "cover" },
  { path: "state/inhalte/2026-09-20-b3.json", art: "reel", szene: 1 },
  { path: "state/inhalte/2026-09-19-b1.json", art: "cover" },
  { path: "state/inhalte/2026-09-19-b2.json", art: "cover" },
  { path: "state/inhalte/2026-09-19-b3.json", art: "reel", szene: 1 },
  { path: "state/inhalte/2026-09-18-b1.json", art: "cover" },
  { path: "state/inhalte/2026-09-18-b2.json", art: "cover" },
  { path: "state/inhalte/2026-09-18-b3.json", art: "reel", szene: 1 },
  { path: "state/inhalte/2026-09-17-b1.json", art: "cover" },
  { path: "state/inhalte/2026-09-17-b2.json", art: "cover" },
];

function ausAssets(pfad) {
  return JSON.parse(execFileSync("git", ["show", `origin/instagram-assets:${pfad}`], { cwd: root, encoding: "utf8" }));
}

function titleSlide(ziel, original) {
  return {
    art: "titel",
    titel: ziel.titel || original.folien?.[0]?.titel || original.szenen?.[0]?.titel || original.kurztitel || "Examenswissen",
    icon: ziel.icon || original.folien?.[0]?.icon || original.szenen?.[0]?.icon || "paragraf",
    pille: original.format === "reel" ? "Reel-Szene" : "Swipen →",
    hinweis: original.format === "reel" ? "Charakter-Test" : "Kurz erklärt",
    prioritaet: original.folien?.[0]?.prioritaet || null,
    prioritaetText: original.folien?.[0]?.prioritaetText || null,
  };
}

const budget = budgetStarten({
  deckel: { core: 100, engagement: 100, research: 100 },
  bisher: { core: 0, engagement: 0, research: 0 },
  protokoll: () => {},
});
budgetSetzen({ limitUsd: 100, antwortLimitUsd: 100 });
kontextSetzen({ budget, telemetrie: null, journal: null, kanal: "herrjurist-charakter-test", datum: "dry-run" });

const manifest = [];
let nr = 0;
try {
  for (const fall of faelle) {
    nr++;
    const original = ausAssets(fall.path);
    const ziel = fall.art === "reel"
      ? { ...original, ...(original.szenen?.[fall.szene ?? 1] || original.szenen?.[0] || {}), format: "reel-szene", slug: `test-${nr}` }
      : { ...original, slug: `test-${nr}` };

    const treffer = await titelbild(ziel, null, { randFarbe: null, zweck: fall.art === "reel" ? "erklaerbild" : "bild", slot: `test-${nr}` });
    if (!treffer) {
      manifest.push({ nr, quelle: fall.path, art: fall.art, ok: false, fehler: "kein Charakterbild erzeugt" });
      continue;
    }

    const folie = titleSlide(ziel, original);
    folie.bild = treffer.bild;
    folie.bildFrei = treffer.frei !== false;
    folie.bildBreite = treffer.breite || null;
    folie.bildHoehe = treffer.hoehe || null;
    folie.bildTyp = treffer.typ || "charakter";
    folie.bildCharaktere = treffer.charaktere || null;

    const beitrag = {
      format: fall.art === "reel" ? "reel-szene" : original.format,
      fach: original.fach,
      klausur: original.klausur,
      fachLabel: original.fachLabel,
      slug: `test-${String(nr).padStart(2, "0")}`,
      folien: [folie],
    };
    const [jpeg] = await beitragRendern(beitrag, out, { variante: 0 });
    const zielName = path.join(out, `${String(nr).padStart(2, "0")}-${fall.art}-${path.basename(fall.path, ".json")}.jpg`);
    fs.renameSync(jpeg, zielName);
    manifest.push({
      nr, quelle: fall.path, art: fall.art, ok: true,
      titel: folie.titel,
      charaktere: treffer.charaktere || [],
      kostenUsd: treffer.kostenUsd ?? null,
      datei: path.basename(zielName),
      prompt: treffer.prompt || null,
    });
  }
} finally {
  await browserBeenden().catch(() => {});
  kontextLoeschen();
}

const kosten = kostenAbschluss();
fs.writeFileSync(path.join(out, "manifest.json"), JSON.stringify({ erzeugt: new Date().toISOString(), manifest, kosten }, null, 2));
console.log(JSON.stringify({ ok: manifest.filter((x) => x.ok).length, gesamt: manifest.length, kostenUsd: kosten.usd, out }, null, 2));
if (manifest.some((x) => !x.ok)) process.exitCode = 2;
