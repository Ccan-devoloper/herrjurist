#!/usr/bin/env node
/**
 * Redaktionell finalisierte Vorproduktionstage aus dem Repository
 * (vorproduktion/<datum>.json) in den Asset-Zweig übernehmen.
 *
 * Kostenfrei: keine Autor-, Faktencheck- oder Bild-Aufrufe. Gerendert wird
 * anschließend mit bin/vorproduktion-ohne-coverbilder-rendern.mjs.
 */
import fs from "node:fs";
import path from "node:path";
import { Hosting } from "../src/hosting.mjs";
import { quizPruefen } from "./vorproduktion-quiz-regel.mjs";

for (const k of ["OPENAI_API_KEY", "ANTHROPIC_API_KEY", "ELEVENLABS_API_KEY", "PEXELS_API_KEY"]) {
  if (String(process.env[k] || "").trim()) throw new Error(`${k} muss leer sein`);
}
const tage = process.argv.slice(2).sort();
if (!tage.length || tage.some((d) => !/^\d{4}-\d{2}-\d{2}$/.test(d))) throw new Error("Datumsargumente fehlen/ungueltig");

const quelle = (d) => new URL(`../vorproduktion/${d}.json`, import.meta.url);

function pruefen(tag, datum) {
  if (tag?.datum !== datum) throw new Error(`${datum}: Datum in der Datei passt nicht`);
  const b = tag.plan?.beitraege || [], s = tag.plan?.stories || [];
  if (b.length !== 3) throw new Error(`${datum}: erwartet 3 Feed-Beiträge`);
  if (s.length !== 9 || s.filter((x) => x.beitragSlot).length !== 3) throw new Error(`${datum}: erwartet 9 Stories, davon 3 Teaser`);
  for (const x of [...b, ...s.filter((y) => !y.beitragSlot)]) {
    const inhalt = tag.inhalte?.[x.slot];
    if (!inhalt) throw new Error(`${datum}: Inhalt ${x.slot} fehlt`);
    if (inhalt.manuellGeprueft !== true) throw new Error(`${datum}: ${x.slot} ist nicht redaktionell geprüft`);
  }
  quizPruefen(tag, datum);
  for (const x of b) {
    const inhalt = tag.inhalte[x.slot];
    if (inhalt.format !== x.format) throw new Error(`${datum}: ${x.slot} Format weicht vom Plan ab`);
    const zeilen = inhalt.folien?.[0]?.titelZeilen || inhalt.titelZeilen || [];
    if (zeilen.length < 2 || zeilen.length > 4) throw new Error(`${datum}: ${x.slot} braucht 2–4 Titelzeilen`);
    for (const z of zeilen) {
      if (/(?:§|Art\.|Abs\.|Satz|S\.|Nr\.|Alt\.|lit\.)$/.test(z.trim())) throw new Error(`${datum}: ${x.slot} Titelzeile endet mit Normteil: ${z}`);
    }
  }
}

const host = new Hosting({ pushen: true }).vorbereiten();
const vp = path.join(host.dir, "vorproduktion");
fs.mkdirSync(vp, { recursive: true });
for (const d of tage) {
  const tag = JSON.parse(fs.readFileSync(quelle(d), "utf8"));
  pruefen(tag, d);
  fs.writeFileSync(path.join(vp, `${d}.json`), JSON.stringify(tag, null, 2) + "\n");
  console.log(`${d}: redaktionelle Fassung übernommen`);
}

const ip = path.join(vp, "index.json");
const idx = fs.existsSync(ip) ? JSON.parse(fs.readFileSync(ip, "utf8")) : { version: 1, tage: [] };
const im = new Map((idx.tage || []).map((x) => [x.datum, x]));
for (const d of tage) {
  im.set(d, { datum: d, status: "vorproduziert", freigabeBetreiber: false, liveVerknuepft: false, vorproduktionStatus: "review", feed: 3, storiesEigenstaendig: 6, teaserAbgeleitet: 3, reviewPfad: `vorproduktion/${d}/fertig`, coverbilder: false, providerKostenUsd: 0 });
}
idx.tage = [...im.values()].sort((a, b) => a.datum.localeCompare(b.datum));
idx.stand = idx.tage.at(-1).datum;
fs.writeFileSync(ip, JSON.stringify(idx, null, 2) + "\n");
host.commit(`Übernehme redaktionelle Vorproduktion ${tage.join(" + ")}`);
await host.push();
console.log("0,00 USD Providerkosten.");
