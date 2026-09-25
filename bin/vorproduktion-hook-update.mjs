#!/usr/bin/env node
/**
 * Cover-Hooks bereits vorproduzierter Tage auf starke Hook-Typen umstellen
 * (vorproduktion/hook-update.json). Setzt Titel, Titelzeilen, Kurztitel und
 * Hook-Typ, bei Reels zusätzlich Hook-Szene und ersten Sprechertext, und baut
 * betroffene Reels mit Piper offline neu. Cover und Story-Teaser rendert
 * anschließend bin/vorproduktion-coverbilder-anwenden.mjs mit dem vorhandenen
 * Freisteller. Providerfrei.
 */
import fs from "node:fs";
import path from "node:path";

for (const k of ["OPENAI_API_KEY", "ANTHROPIC_API_KEY", "ELEVENLABS_API_KEY", "PEXELS_API_KEY"]) {
  if (String(process.env[k] || "").trim()) throw new Error(`${k} muss leer sein`);
}
if (String(process.env.IG_STIMME || "").toLowerCase() !== "piper") throw new Error("Hook-Update verlangt IG_STIMME=piper.");

const { Hosting } = await import("../src/hosting.mjs");
const { reelBauen } = await import("../src/reel.mjs");
const { browserBeenden } = await import("../src/render.mjs");

const update = JSON.parse(fs.readFileSync(new URL("../vorproduktion/hook-update.json", import.meta.url), "utf8"));
const host = new Hosting({ pushen: true }).vorbereiten();
const tage = new Map();
const lesen = (d) => {
  if (!tage.has(d)) {
    const p = path.join(host.dir, "vorproduktion", `${d}.json`);
    if (!fs.existsSync(p)) throw new Error(`Vorproduktion fehlt: ${d}`);
    tage.set(d, JSON.parse(fs.readFileSync(p, "utf8")));
  }
  return tage.get(d);
};

const reels = [];
for (const [key, u] of Object.entries(update.beitraege)) {
  const [datum, slot] = key.split("/");
  const tag = lesen(datum);
  const b = tag.inhalte?.[slot];
  if (!b) throw new Error(`${key}: Beitrag fehlt`);
  if (Array.isArray(b.folien)) {
    const t = b.folien.find((f) => f.art === "titel") || b.folien[0];
    t.titel = u.titel;
    t.titelZeilen = u.titelZeilen;
  } else if (Array.isArray(b.szenen)) {
    b.titelZeilen = u.titelZeilen;
    b.szenen[0].titel = u.titel;
    if (u.sprecher) b.szenen[0].sprecher = u.sprecher;
    reels.push({ datum, slot });
  } else throw new Error(`${key}: unbekanntes Format`);
  b.kurztitel = u.kurztitel;
  b.hookTyp = "fehler";
  b.hookMuster = u.hookMuster;
  if (typeof b.caption === "string" && !b.caption.startsWith(u.titel)) b.caption = `${u.titel}\n\n${b.caption}`;
  b.hookUpdate = { stand: new Date().toISOString(), quelle: "vorproduktion/hook-update.json" };
  const p = (tag.plan?.beitraege || []).find((x) => x.slot === slot);
  if (p) p.themaTitel = u.kurztitel;
  console.log(`${key}: ${u.titel}`);
}

try {
  for (const { datum, slot } of reels) {
    const tag = lesen(datum);
    const beitrag = structuredClone(tag.inhalte[slot]);
    const ziel = path.join(host.dir, tag.renderVorschau?.pfad || `vorproduktion/${datum}/fertig`, slot);
    fs.rmSync(ziel, { recursive: true, force: true });
    const reel = await reelBauen(beitrag, ziel, { datum, layout: "erklaer", clip: null, framesBehalten: false });
    console.log(`${datum} ${slot}: Reel neu gebaut (${Math.round(reel.dauer)} s, ${reel.anbieter})`);
  }
} finally {
  await browserBeenden().catch(() => {});
}

for (const [d, tag] of tage) fs.writeFileSync(path.join(host.dir, "vorproduktion", `${d}.json`), JSON.stringify(tag, null, 2) + "\n");
host.commit(`Starke Cover-Hooks für ${Object.keys(update.beitraege).length} vorproduzierte Beiträge ab ${[...tage.keys()].sort()[0]}`);
await host.push();
console.log("0,00 USD Providerkosten.");
