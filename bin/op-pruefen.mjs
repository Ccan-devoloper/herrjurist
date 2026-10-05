#!/usr/bin/env node
/* Prüft die sichtbaren Texte der Open-Peeps-Vorproduktion (op/) gegen die
   verbindlichen Quellenregeln (QUELLENREGELN.md) – mit derselben Prüfung wie
   jeder Live-Beitrag (pruefeBeitrag), ohne die Formalgrenzen des alten Renderers.

     node bin/op-pruefen.mjs texte.json [weitere.json …]

   texte.json: { "<datei>": ["Text", …], … } – je Ausgabedatei die sichtbaren Texte.
   Folien „Im Gesetz markieren“ (Gesetzeszitat, Regel 1 nimmt Gesetzeszitate aus)
   werden über "gesetz": true im Dateinamen-Eintrag oder den Suffix -gesetz übersprungen.
   Exitcode 1 bei einem Befund. */
import fs from "node:fs";
/* Ohne IG_WISSEN_KEY lässt sich der verschlüsselte Themenpool (Korpus) nicht öffnen. Lokal darf dann mit
   OP_OHNE_KORPUS=1 ohne Übernahmeprüfung gerendert werden; der Workflow prüft immer mit Korpus. */
let pruefeBeitrag;
try {
  ({ pruefeBeitrag } = await import("../src/pruefung.mjs"));
} catch (e) {
  if (process.env.OP_OHNE_KORPUS !== "1") throw e;
  console.log(`! Quellenprüfung ohne Korpus übersprungen (${e.message.split("\n")[0]})`);
  process.exit(0);
}

const FORMAL = /^(Folienzahl|Folie \d+: (Titel|Text) zu lang|Folie 1 braucht|Caption zu lang|Zu viele Hashtags|Story „)/;
const AUFBAU = /Aufbau|Sachverhalt|Merksatz|CTA|Folie/;

function gruppen(daten) {
  const g = new Map();
  for (const [datei, texte] of Object.entries(daten)) {
    if (/gesetz/i.test(datei) || texte?.gesetz) continue;
    const m = datei.match(/(\d{4}-\d{2}-\d{2})-(b\d|s\d|reel)/);
    const key = m ? `${m[1]} ${m[2].startsWith("s") ? "stories" : m[2]}` : datei;
    if (!g.has(key)) g.set(key, []);
    g.get(key).push(...(Array.isArray(texte) ? texte : texte.texte || []));
  }
  return g;
}

let befunde = 0;
for (const pfad of process.argv.slice(2)) {
  const daten = JSON.parse(fs.readFileSync(pfad, "utf8"));
  for (const [key, texte] of gruppen(daten)) {
    const folien = texte.filter((t) => String(t).trim()).map((t, i) => ({ art: i ? "text" : "titel", titel: i ? "" : t, text: i ? t : "" }));
    const r = pruefeBeitrag({ folien }, {});
    const echt = r.fehler.filter((f) => !FORMAL.test(f) && !(AUFBAU.test(f) && /Folie|Aufbau/.test(f.slice(0, 40)) && !/Übernahme|Fallnamen|Merkhilfe|Quelle|Bezug|Verfasser|Gliederung|Überschrift/.test(f)));
    if (echt.length) { befunde += echt.length; console.log(`✗ ${key}`); echt.forEach((f) => console.log("   - " + f)); }
    else console.log(`✓ ${key} (${texte.length} Texte)`);
  }
}
process.exit(befunde ? 1 : 0);
