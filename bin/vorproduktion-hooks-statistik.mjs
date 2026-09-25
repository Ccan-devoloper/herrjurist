#!/usr/bin/env node
/* Hook-Übersicht über mehrere Tage: Hook-Typen, Anteil etikettierter Cover-Titel
   („Fehler/falsch/=…?“) und doppelte Titelanfänge. Ziel: Etikett ≤ 20 %. */
import fs from "node:fs";
import { ETIKETT, coverTitel } from "./vorproduktion-tag-pruefen.mjs";
const titel = [], typ = {};
for (const p of process.argv.slice(2)) {
  const t = JSON.parse(fs.readFileSync(p, "utf8"));
  for (const b of t.plan.beitraege) { const c = t.inhalte[b.slot]; if (!c) continue; typ[c.hookTyp] = (typ[c.hookTyp] || 0) + 1; titel.push({ k: `${t.datum}/${b.slot}`, t: c.folien?.[0]?.titel || c.szenen?.[0]?.titel || "" , e: ETIKETT.test(coverTitel(c)) }); }
}
const e = titel.filter((x) => x.e);
console.log("Hook-Typen:", typ);
console.log(`Etikett: ${e.length}/${titel.length} (${Math.round((100 * e.length) / Math.max(1, titel.length))} %)`);
for (const x of e) console.log("  E", x.k, x.t);
const anf = {}; for (const x of titel) { const a = x.t.split(/\s+/).slice(0, 2).join(" ").toLowerCase(); (anf[a] ||= []).push(x.k); }
for (const [a, l] of Object.entries(anf)) if (l.length > 1) console.log(`  Doppelter Anfang „${a}“: ${l.join(", ")}`);
