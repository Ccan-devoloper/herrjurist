#!/usr/bin/env node
/**
 * Archiv für vergangene Tage im Asset-Zweig.
 *
 *   node bin/archiv-tage.mjs liste            → `tage=<d1> <d2> …` (für $GITHUB_OUTPUT)
 *   node bin/archiv-tage.mjs loeschen d1 d2 … → Bild-/Videoordner löschen, Archiv-Eintrag, Commit, Push
 *
 * Ein Tag ist archivierbar, wenn er vor dem heutigen Tag (Europe/Berlin) liegt
 * und laut state/plaene/<datum>.json JEDER geplante Beitrag und jede Story
 * veröffentlicht ist. Gelöscht werden nur die schweren Ordner
 * bilder/<datum>/ und vorproduktion/<datum>/ – Tagesplan, Inhalte (JSON),
 * Ledger und Insights bleiben, damit Lernschleife und Berichte weiterlaufen.
 * Gelöscht wird ausschließlich, was der Workflow vorher nachweislich auf
 * Google Drive gesichert hat.
 */
import fs from "node:fs";
import path from "node:path";
import { Hosting } from "../src/hosting.mjs";

const MAX_JE_LAUF = Number(process.env.IG_ARCHIV_MAX_JE_LAUF || 10);
const heute = process.env.IG_HEUTE || new Intl.DateTimeFormat("sv-SE", { timeZone: "Europe/Berlin" }).format(new Date());
const [modus, ...args] = process.argv.slice(2);
const host = new Hosting({ pushen: modus === "loeschen" }).vorbereiten();
const ordner = (d) => [path.join(host.dir, "bilder", d), path.join(host.dir, "vorproduktion", d)].filter((p) => fs.existsSync(p));

function veroeffentlicht(d) {
  const p = path.join(host.stateDir, "plaene", `${d}.json`);
  if (!fs.existsSync(p)) return false;
  const plan = JSON.parse(fs.readFileSync(p, "utf8"));
  const slots = [...(plan.beitraege || []), ...(plan.stories || [])];
  return slots.length > 0 && slots.every((s) => s.status === "veroeffentlicht");
}

if (modus === "liste") {
  const kandidaten = new Set();
  for (const basis of ["bilder", "vorproduktion"]) {
    const dir = path.join(host.dir, basis);
    if (!fs.existsSync(dir)) continue;
    for (const e of fs.readdirSync(dir, { withFileTypes: true })) if (e.isDirectory() && /^\d{4}-\d{2}-\d{2}$/.test(e.name)) kandidaten.add(e.name);
  }
  const tage = [...kandidaten].sort().filter((d) => d < heute);
  const fertig = tage.filter(veroeffentlicht).slice(0, MAX_JE_LAUF);
  for (const d of tage.filter((x) => !fertig.includes(x))) console.error(`${d}: nicht vollständig veröffentlicht oder Limit – bleibt liegen`);
  console.error(`Heute ${heute}: archivierbar ${fertig.join(", ") || "–"}`);
  console.log(`tage=${fertig.join(" ")}`);
} else if (modus === "loeschen") {
  const archivPfad = path.join(host.stateDir, "archiv.json");
  const archiv = fs.existsSync(archivPfad) ? JSON.parse(fs.readFileSync(archivPfad, "utf8")) : { tage: [] };
  const ziel = process.env.IG_ARCHIV_ZIEL || "gdrive:HerrJurist-Archiv";
  for (const d of args.filter((x) => /^\d{4}-\d{2}-\d{2}$/.test(x))) {
    if (!veroeffentlicht(d) || d >= heute) throw new Error(`${d}: nicht archivierbar – Abbruch ohne Löschen`);
    let dateien = 0, bytes = 0;
    const zaehlen = (p) => { for (const e of fs.readdirSync(p, { withFileTypes: true })) { const q = path.join(p, e.name); if (e.isDirectory()) zaehlen(q); else { dateien++; bytes += fs.statSync(q).size; } } };
    for (const p of ordner(d)) { zaehlen(p); fs.rmSync(p, { recursive: true, force: true }); }
    archiv.tage = archiv.tage.filter((x) => x.datum !== d);
    archiv.tage.push({ datum: d, drive: `${ziel}/${d}`, dateien, megabyte: Math.round(bytes / 1e5) / 10, archiviertAm: new Date().toISOString() });
    console.log(`${d}: ${dateien} Dateien (${Math.round(bytes / 1e6)} MB) gelöscht – Sicherung ${ziel}/${d}`);
  }
  archiv.tage.sort((a, b) => a.datum.localeCompare(b.datum));
  fs.writeFileSync(archivPfad, JSON.stringify(archiv, null, 2) + "\n");
  host.commit(`Archiviere ${args.join(" + ")} nach Google Drive und entferne die Mediendateien`);
  await host.push();
} else {
  throw new Error("Modus: liste | loeschen <datum…>");
}
