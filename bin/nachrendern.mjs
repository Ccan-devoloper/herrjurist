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

   Mit IG_ABLEGEN=1 landen die Ergebnisse unter vorschau/<datum>/ im
   Asset-Zweig. So laesst sich das Ergebnis vom Runner aus ansehen, ohne den
   Feed anzufassen.
   ========================================================================== */

import fs from "node:fs";
import path from "node:path";
import { Hosting } from "../src/hosting.mjs";
import { beitragRendern, storyRendern, browserBeenden } from "../src/render.mjs";
import { titelbild } from "../src/bilder.mjs";
import { reelBauen } from "../src/reel.mjs";
import { heuteIso } from "../src/zeit.mjs";
import { CONFIG } from "../src/config.mjs";

const datum = process.argv[2] || heuteIso();
const ziel = process.argv[3] || path.resolve("out", `nach-${datum}`);

const ablegen = process.env.IG_ABLEGEN === "1";
const hosting = new Hosting({ pushen: ablegen }).vorbereiten();
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
      /* Das Reel kostet auch hier keinen Claude-Aufruf – der Text steht ja
         schon. Die Stimme wird allerdings neu gesprochen; das geht auf das
         Kontingent von ElevenLabs (oder auf Piper, wenn es erschöpft ist). */
      const r = await reelBauen(inhalt, path.join(ziel, slot), { datum, hintergrundDir: path.join(hosting.stateDir, "hintergrund") });
      n += 2;
      console.log(`  ${slot}: Reel ${r.dauer.toFixed(1)} s${r.echt ? "" : " (Ersatzstimme)"} → ${path.basename(r.video)}`);
    }
  } catch (e) {
    console.error(`  ${slot}: ${e.message}`);
  }
}
await browserBeenden();
console.log(`${n} Bilder → ${ziel}`);

if (ablegen) {
  /* Flach in den Zweig legen: die Unterordner je Beitrag wuerden die Pfade nur
     verlaengern, die Dateinamen sind schon eindeutig. */
  const dateien = [];
  const sammeln = (d) => { for (const e of fs.readdirSync(d, { withFileTypes: true })) e.isDirectory() ? sammeln(path.join(d, e.name)) : /\.(jpg|png|mp4)$/.test(e.name) && dateien.push(path.join(d, e.name)); };
  sammeln(ziel);
  const kennung = Date.now().toString(36);
  for (const d of dateien) {
    const { name, ext } = path.parse(d);
    const teil = path.relative(ziel, path.dirname(d)).split(path.sep).filter(Boolean).join("-");
    hosting.ablegen(d, path.join("vorschau", datum, `${teil ? teil + "-" : ""}${name}-${kennung}${ext}`));
  }
  hosting.commit(`Vorschau ${datum} (${dateien.length} Bilder)`);
  await hosting.push();
  console.log(`${dateien.length} Bilder im Asset-Zweig unter vorschau/${datum}/`);
}
