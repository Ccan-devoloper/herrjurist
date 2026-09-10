#!/usr/bin/env node
/* ==========================================================================
   Stimmen suchen und anhören.

   node bin/stimmen.mjs            listet die Kandidaten (kostet nichts)
   node bin/stimmen.mjs --proben   spricht je Kandidat einen Probesatz und legt
                                   die MP3s im Asset-Zweig unter stimmen/ ab
   node bin/stimmen.mjs --setzen 2 schreibt Kandidat Nr. 2 als feste Stimme fest

   Der Probesatz steht in CONFIG.reel.stimmeProbeText (≈ 200 Zeichen je
   Stimme; drei Kandidaten kosten also ≈ 600 der 10.000 Freizeichen).
   ========================================================================== */

import fs from "node:fs";
import path from "node:path";
import { CONFIG } from "../src/config.mjs";
import { Hosting } from "../src/hosting.mjs";
import { kandidatenSuchen, stimmeUebernehmen, tarif } from "../src/stimmen.mjs";
import { sprechen, stimmeStandVerbinden, kontingentAbfragen } from "../src/stimme.mjs";

const args = process.argv.slice(2);
const will = (name) => args.includes(`--${name}`);
const argWert = (name) => { const i = args.indexOf(`--${name}`); return i >= 0 ? args[i + 1] : null; };

if (!CONFIG.reel.elevenlabsKey) { console.error("ELEVENLABS_API_KEY fehlt."); process.exit(1); }

const hosting = new Hosting({ pushen: true }).vorbereiten();
stimmeStandVerbinden({ lesen: () => hosting.jsonLesen("stimme.json", null), schreiben: (s) => hosting.jsonSchreiben("stimme.json", s) });

const abo = await tarif();
let liste = hosting.jsonLesen("stimmen.json", null);
if (!liste?.kandidaten?.length || will("neu")) {
  const roh = await kandidatenSuchen({ anzahl: CONFIG.reel.stimmeAnzahl, abo });
  const kandidaten = [];
  for (const k of roh) kandidaten.push(await stimmeUebernehmen(k, { bezahlt: abo !== "free" }));
  liste = { gesucht: new Date().toISOString(), kandidaten, fest: liste?.fest || null };
  hosting.jsonSchreiben("stimmen.json", liste);
}

const rest = await kontingentAbfragen({ frisch: true });
console.log(`Abo: ${abo || "?"} · Guthaben: ${rest ?? "?"} Zeichen · Modell ${CONFIG.reel.modell}`);
if (abo === "free") console.log("Hinweis: Im kostenlosen Tarif dürfen über die API nur die Stimmen des Kontos sprechen, keine Bibliotheksstimmen.");
console.log("");
console.log("Kandidaten:");
liste.kandidaten.forEach((k, i) => {
  console.log(`  ${i + 1}. ${k.name.padEnd(22)} ${String(k.geschlecht || "?").padEnd(7)} ${String(k.alter || "?").padEnd(12)} ${String(k.beschreibung || "–").padEnd(14)} Einsatz ${k.einsatz || "–"} · Eignung ${k.punkte} · ${k.id}`);
});
if (liste.fest) console.log(`\nFest eingestellt: „${liste.fest.name}“`);

const setzen = argWert("setzen");
if (setzen) {
  const k = liste.kandidaten[Number(setzen) - 1];
  if (!k) { console.error(`Kandidat ${setzen} gibt es nicht.`); process.exit(1); }
  hosting.jsonSchreiben("stimmen.json", { ...liste, fest: { id: k.id, name: k.name }, entschieden: new Date().toISOString() });
  hosting.commit(`Stimme festgelegt: ${k.name}`); await hosting.push();
  console.log(`\n→ „${k.name}“ spricht ab jetzt alle Reels.`);
  process.exit(0);
}

if (will("proben")) {
  console.log("\nProben:");
  for (const [i, k] of liste.kandidaten.entries()) {
    /* Das Modell steht im Dateinamen, sonst überschreibt ein Vergleichslauf
       (v3 gegen flash) die vorherigen Proben. */
    const kennung = /flash|turbo/i.test(CONFIG.reel.modell) ? `-${CONFIG.reel.modell.replace(/[^\w]+/g, "")}` : "";
    const datei = path.join(hosting.stateDir, "stimmen", `${String(i + 1).padStart(2, "0")}-${k.name.replace(/[^\w]+/g, "-").toLowerCase()}${kennung}.mp3`);
    try {
      const r = await sprechen(CONFIG.reel.stimmeProbeText, datei, { anbieter: "elevenlabs", stimmeId: k.id, betonung: "hook" });
      /* Fällt die Stimme durch (Tarif, Kontingent), gibt es keine Datei – das
         darf nicht als gelungene Probe im Log stehen. */
      if (r.anbieter === "elevenlabs" && fs.existsSync(datei)) console.log(`  ${k.name}: ${r.dauer.toFixed(1)} s → ${path.relative(hosting.stateDir, datei)}`);
      else console.log(`  ${k.name}: keine Probe (${r.anbieter})`);
    } catch (e) { console.error(`  ${k.name}: ${e.message}`); }
  }
  hosting.commit("Stimmproben"); await hosting.push();
  const zweig = "instagram-assets";
  console.log(`\nAnhören: https://github.com/${process.env.GITHUB_REPOSITORY || "Ccan-devoloper/steuerberater"}/tree/${zweig}/state/stimmen`);
}
