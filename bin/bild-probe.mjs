#!/usr/bin/env node
/**
 * Zeichnet dasselbe Motiv in mehreren Einstellungen und legt die Ergebnisse
 * nebeneinander ab, damit man sie ansehen kann, statt über sie zu reden.
 *
 * Anlass: Seit dem 18.09. sollen die Titelbilder „echt" wirken
 * (IG_BILD_LOOK=foto). Der Auftrag an das Zeichenmodell sagt das auch
 * ausdrücklich („Photorealistic photograph … not an illustration, not a 3D
 * render"), herausgekommen sind an diesem Morgen trotzdem eine flache
 * Illustration (Herr Jurist) und ein 3D-Rendering (Examens Campus). Verdacht:
 * Güte „low" und der durchsichtige Hintergrund verhindern zusammen jede
 * Fotoanmutung - das Modell baut dann einen Aufkleber.
 *
 * Geprüft werden deshalb drei Wege am selben Motiv:
 *   A  low  + durchsichtig                 (der heutige Stand)
 *   B  low  + Hintergrund, danach freigestellt (rembg, kostet nichts extra)
 *   C  mittel + durchsichtig               (teurer, dafür mehr Güte)
 *
 * Aufruf: node bin/bild-probe.mjs "stack of unopened envelopes" [ziel]
 */
import fs from "node:fs";
import path from "node:path";

const szene = process.argv[2] || "wooden desk calendar with circled date";
const ziel = process.argv[3] || "proben";
const { CONFIG } = await import("../src/config.mjs");
const { bildAuftrag } = await import("../src/bildki.mjs");
const { bildAufruf } = await import("../src/anbieter.mjs");
const { freistellen, alphaProfil, masse } = await import("../src/freistellen.mjs");

const ki = CONFIG.bilder.ki;
if (!ki.key) { console.error("Kein OPENAI_API_KEY - nichts zu messen."); process.exit(1); }
fs.mkdirSync(ziel, { recursive: true });

const wege = [
  { name: "A-low-durchsichtig", guete: "low", transparent: true },
  { name: "B-low-freigestellt", guete: "low", transparent: false },
  { name: "C-mittel-durchsichtig", guete: "medium", transparent: true },
];

for (const weg of wege) {
  const auftrag = bildAuftrag(szene, { look: "foto" });
  const koerper = {
    model: ki.modell, prompt: auftrag, n: 1, size: ki.groesse,
    quality: weg.guete, output_format: "png",
    ...(weg.transparent ? { background: "transparent" } : {}),
  };
  const t = Date.now();
  /* Keine Sondertür für Proben mehr: Auch dieser manuelle Bildvergleich muss
     durch anbieter.mjs. Ohne zuvor gesetzten durablen Kostenkontext bricht
     bildAufruf fail-closed ab, bevor OpenAI angesprochen wird. So kann ein
     Hilfs-/Previewlauf nie wieder still außerhalb des Kostenledgers bezahlen. */
  let daten;
  try {
    daten = await bildAufruf({
      zweck: "bild",
      modell: ki.modell,
      optional: true,
      preisUsd: ki.preisUsd,
      slot: `probe:${weg.name}`,
      auftrag: { key: ki.key, koerper },
    });
  } catch (e) {
    console.error(`  ${weg.name}: ${e.name}: ${e.message}`);
    throw e;
  }
  const b64 = daten?.data?.[0]?.b64_json;
  if (!b64) { console.log(`  ${weg.name}: keine Bilddaten`); continue; }
  const roh = path.join(ziel, `${weg.name}-roh.png`);
  fs.writeFileSync(roh, Buffer.from(b64, "base64"));
  let fertig = roh;
  if (!weg.transparent) {
    const frei = freistellen(roh, {});
    if (frei?.pfad) { fertig = path.join(ziel, `${weg.name}.png`); fs.copyFileSync(frei.pfad, fertig); }
    else console.log(`  ${weg.name}: Freistellen misslungen - nur das Rohbild liegt vor.`);
  }
  const prof = alphaProfil(fertig);
  const m = masse(fertig) || {};
  console.log(`  ${weg.name}: ${((Date.now() - t) / 1000).toFixed(1)} s · ${m.breite || "?"}x${m.hoehe || "?"} · ${prof ? `${(prof.festigkeit * 100).toFixed(0)} % deckend` : "kein Alphakanal"} · ${(fs.statSync(fertig).size / 1024).toFixed(0)} kB`);
}
fs.writeFileSync(path.join(ziel, "auftrag.txt"), `${szene}\n\n${bildAuftrag(szene, { look: "foto" })}\n`);
console.log(`\nFertig. Bilder in ${ziel}/`);
