#!/usr/bin/env node
/* ==========================================================================
   Einen bereits geschriebenen Tag neu rendern.

   node bin/nachrendern.mjs [datum]

   Liest die fertigen Texte aus state/inhalte/<datum>-*.json und baut die
   Kacheln neu – ohne einen einzigen Claude-Aufruf. Nach jeder Änderung an
   Vorlage, Layout oder Bildlogik lässt sich damit sehen, was dabei
   herauskommt, ohne den Tagesetat anzufassen.

   Bilder werden dabei frisch geholt (Pexels ist kostenlos) und neu
   freigestellt, damit auch daran gearbeitet werden kann.
   ========================================================================== */

import fs from "node:fs";
import path from "node:path";
import { Hosting } from "../src/hosting.mjs";
import { beitragRendern, storyRendern, browserBeenden } from "../src/render.mjs";
import { titelbild } from "../src/bilder.mjs";
import { heuteIso } from "../src/zeit.mjs";
import { CONFIG } from "../src/config.mjs";

const datum = process.argv[2] || heuteIso();
const ziel = process.argv[3] || path.resolve("out", `nach-${datum}`);

const hosting = new Hosting({ pushen: false }).vorbereiten();
const dir = path.join(hosting.stateDir, "inhalte");
if (!fs.existsSync(dir)) { console.error(`Keine Inhalte in ${dir}`); process.exit(1); }

const dateien = fs.readdirSync(dir).filter((f) => f.startsWith(`${datum}-`) && f.endsWith(".json")).sort();
if (!dateien.length) { console.error(`Nichts gespeichert für ${datum}`); process.exit(1); }

console.log(`${dateien.length} Dateien für ${datum} · Stil ${CONFIG.marke.stil}`);
let n = 0;
for (const datei of dateien) {
  const inhalt = JSON.parse(fs.readFileSync(path.join(dir, datei), "utf8"));
  const slot = datei.replace(`${datum}-`, "").replace(".json", "");
  try {
    if (inhalt.folien) {
      const titelfolie = inhalt.folien.find((f) => f.art === "titel");
      if (titelfolie) {
        const treffer = await titelbild(inhalt);
        if (treffer) { titelfolie.bild = treffer.bild; titelfolie.bildQuelle = treffer.quelle; titelfolie.bildFrei = treffer.frei !== false; }
      }
      const pfade = await beitragRendern(inhalt, path.join(ziel, slot), { variante: 0 });
      n += pfade.length;
      console.log(`  ${slot}: ${pfade.length} Folien`);
    } else if (inhalt.art) {
      await storyRendern(inhalt, path.join(ziel, `${slot}-${inhalt.art}.jpg`), { variante: 0 });
      n++;
      console.log(`  ${slot}: Story ${inhalt.art}`);
    } else if (inhalt.szenen) {
      console.log(`  ${slot}: Reel übersprungen (Video, nicht nur Rendern)`);
    }
  } catch (e) {
    console.error(`  ${slot}: ${e.message}`);
  }
}
await browserBeenden();
console.log(`${n} Bilder → ${ziel}`);
