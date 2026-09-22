#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { themenpool, FAECHER } from "../src/inhalte.mjs";
import { titelbild } from "../src/bilder.mjs";
import { beitragRendern, browserBeenden } from "../src/render.mjs";
import { budgetStarten } from "../src/budget.mjs";
import { kontextSetzen, kontextLoeschen } from "../src/anbieter.mjs";
import { budgetSetzen, abschluss as kostenAbschluss } from "../src/kosten.mjs";

const hier = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(hier, "..");
const out = path.join(root, "out", "charakter-meinungsfreiheit");
fs.rmSync(out, { recursive: true, force: true });
fs.mkdirSync(out, { recursive: true });

const pool = themenpool();
const kandidaten = pool.filter((t) => String(t.titel || "").toLowerCase().includes("meinungsfreiheit"));
if (!kandidaten.length) throw new Error("Kein Thema mit „Meinungsfreiheit“ im Themenpool gefunden.");
const thema = kandidaten[0];
const fach = FAECHER[thema.fach];

const budget = budgetStarten({
  deckel: { core: 100, engagement: 100, research: 100 },
  bisher: { core: 0, engagement: 0, research: 0 },
  protokoll: () => {},
});
budgetSetzen({ limitUsd: 100, antwortLimitUsd: 100 });
kontextSetzen({ budget, telemetrie: null, journal: null, kanal: "herrjurist-charakter-meinungsfreiheit", datum: "dry-run" });

let manifest;
try {
  const ziel = {
    format: "pruefungsfrage",
    slug: "meinungsfreiheit-charakter-test",
    themaId: thema.id,
    titel: thema.titel,
    kurztitel: "Meinungsfreiheit",
    fach: thema.fach,
    fachLabel: fach?.kurz || fach?.label || thema.fach,
    klausur: thema.klausur,
    norm: (thema.normen || []).join(", "),
    bildSzene: "one character speaks openly while another character marks a clear legal boundary, showing protected expression versus a lawful limit",
    folien: [{
      art: "titel",
      titel: "Meinungsfreiheit",
      icon: "sprechblase",
      pille: fach?.kurz || "Grundrechte",
      hinweis: (thema.normen || [])[0] || "Art. 5 GG",
      prioritaet: thema.prioritaet || null,
      bildSzene: "one character speaks openly while another character marks a clear legal boundary, showing protected expression versus a lawful limit",
    }],
  };

  const treffer = await titelbild(ziel, null, {
    randFarbe: null,
    zweck: "bild",
    slot: "meinungsfreiheit-charakter-test",
  });
  if (!treffer) throw new Error("Kein Charakterbild erzeugt.");

  ziel.folien[0].bild = treffer.bild;
  ziel.folien[0].bildFrei = treffer.frei !== false;
  ziel.folien[0].bildBreite = treffer.breite || null;
  ziel.folien[0].bildHoehe = treffer.hoehe || null;
  ziel.folien[0].bildTyp = treffer.typ || "charakter";
  ziel.folien[0].bildCharaktere = treffer.charaktere || null;

  const [jpeg] = await beitragRendern(ziel, out, { variante: 0 });
  const cover = path.join(out, "meinungsfreiheit-cover.jpg");
  fs.renameSync(jpeg, cover);

  manifest = {
    thema: { id: thema.id, titel: thema.titel, fach: thema.fach, klausur: thema.klausur, normen: thema.normen },
    cover: path.basename(cover),
    charaktere: treffer.charaktere || [],
    kostenUsd: treffer.kostenUsd ?? null,
    prompt: treffer.prompt || null,
  };
} finally {
  await browserBeenden().catch(() => {});
  kontextLoeschen();
}

const kosten = kostenAbschluss();
fs.writeFileSync(path.join(out, "manifest.json"), JSON.stringify({ erzeugt: new Date().toISOString(), manifest, kosten }, null, 2));
console.log(JSON.stringify({ ok: true, thema: manifest.thema, charaktere: manifest.charaktere, kostenUsd: manifest.kostenUsd, out }, null, 2));
