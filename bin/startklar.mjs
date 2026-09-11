#!/usr/bin/env node
/* ==========================================================================
   Startklar? – prüft vor dem Livegang alles, was der Bot zum Veröffentlichen
   braucht, ohne einen einzigen Beitrag zu erzeugen.

   node bin/startklar.mjs

   Der wichtigste Punkt ist der Instagram-Token: Im Trockenlauf wird die API
   nie angefasst, ein abgelaufener oder falsch hinterlegter Token fällt also
   erst beim ersten echten Lauf auf – und dann steht der Kanal.

   Rückgabewert 1, wenn etwas fehlt, das das Veröffentlichen verhindert.
   ========================================================================== */

import fs from "node:fs";
import path from "node:path";
import { Instagram } from "../src/instagram.mjs";
import { Hosting } from "../src/hosting.mjs";
import { CONFIG } from "../src/config.mjs";
import { kontingentAbfragen, stimmeStand } from "../src/stimme.mjs";

const zeilen = [];
let blocker = 0;
const gut = (t) => zeilen.push(`  ✓ ${t}`);
const warnung = (t) => zeilen.push(`  · ${t}`);
const fehler = (t) => { zeilen.push(`  ✗ ${t}`); blocker++; };

console.log(`Startklar-Prüfung · ${CONFIG.marke.name || "(ohne Markennamen)"} · ${new Date().toISOString().slice(0, 16).replace("T", " ")} UTC\n`);

/* 1. Instagram ----------------------------------------------------------- */
console.log("Instagram");
const hosting = new Hosting({ pushen: false }).vorbereiten();
const tresor = path.join(hosting.stateDir, "token.enc");
const ig = new Instagram({ trockenlauf: false, tresorDatei: tresor });
const ausTresor = ig.tresorLaden();
if (!ig.token) fehler("Kein Zugangstoken: weder im Tresor noch als Secret IG_ACCESS_TOKEN.");
else {
  gut(`Token vorhanden (${ausTresor ? "aus dem Tresor" : "aus dem Secret"}${ig.tokenAblauf ? `, gültig bis ${ig.tokenAblauf.slice(0, 10)}` : ""})`);
  if (!CONFIG.instagram.kontoId) warnung("IG_ACCOUNT_ID ist leer – das Tageskontingent lässt sich nicht abfragen.");
  try {
    const { konto, limit } = await ig.pruefen();
    const name = konto.username || konto.name || "(ohne Namen)";
    gut(`Verbindung steht: @${name}`);
    gut(`Tageskontingent der API: ${limit.genutzt} von ${limit.maximum} genutzt${limit.hinweis ? ` (${limit.hinweis})` : ""}`);
    if (CONFIG.marke.handle && CONFIG.marke.handle.replace(/^@/, "") !== String(name)) {
      warnung(`IG_HANDLE ist „${CONFIG.marke.handle}“, das Konto heißt @${name} – die Fußzeile zeigt das Falsche.`);
    }
  } catch (e) {
    fehler(`Instagram antwortet nicht: ${e.message.split("\n")[0].slice(0, 180)}`);
  }
}
if (!process.env.IG_TOKEN_KEY) warnung("IG_TOKEN_KEY fehlt – ein verlängerter Token kann nicht gespeichert werden und läuft irgendwann ab.");
else gut("IG_TOKEN_KEY gesetzt, verlängerte Token werden verschlüsselt abgelegt");

/* 2. Texte und Prüfung --------------------------------------------------- */
console.log(zeilen.splice(0).join("\n") + "\n\nTexte");
/* Der Schlüssel steht nicht in CONFIG – das SDK liest ihn selbst aus der
   Umgebung. Deshalb hier direkt nachsehen. */
if (!process.env.ANTHROPIC_API_KEY) fehler("ANTHROPIC_API_KEY fehlt – ohne ihn entsteht kein einziger Beitrag.");
else gut(`Claude-Schlüssel gesetzt (${CONFIG.ki.modell}, Faktencheck ${CONFIG.faktencheck.aktiv ? CONFIG.faktencheck.modellPruefung || CONFIG.faktencheck.modell || "an" : "aus"})`);
if (CONFIG.faktencheck.aktiv && CONFIG.faktencheck.strikt) gut("Faktencheck streng: Fällt er aus, erscheint der Beitrag nicht");
else if (CONFIG.faktencheck.aktiv) warnung("Faktencheck nicht streng – fällt er aus, erscheint der Beitrag trotzdem.");
else fehler("Faktencheck ist abgeschaltet.");
gut(`Tagesbudget: ${CONFIG.ki.tagesBudgetUsd.toFixed(2)} $`);

/* 3. Stimme und Bilder --------------------------------------------------- */
console.log(zeilen.splice(0).join("\n") + "\n\nReels und Bilder");
if (!CONFIG.reel.aktiv) warnung("Reels sind abgeschaltet.");
else if (!CONFIG.reel.elevenlabsKey) warnung("Kein ElevenLabs-Schlüssel – gesprochen wird mit der Offline-Stimme.");
else {
  const stand = stimmeStand();
  const rest = await kontingentAbfragen();
  if (rest == null) warnung("ElevenLabs antwortet nicht auf die Kontingentabfrage – im Zweifel wird gesprochen und bei Bedarf auf Piper gewechselt.");
  else if (rest < 400) warnung(`ElevenLabs: nur noch ${rest} Kredite – die nächsten Reels laufen über die Offline-Stimme.`);
  else gut(`ElevenLabs: ${rest} Kredite frei (reicht für rund ${Math.floor(rest / 300)} Reels)`);
  if (stand.erschoepft) warnung("ElevenLabs gilt als erschöpft; der Bot spricht offline weiter.");
}
const clipDir = path.join(hosting.stateDir, "hintergrund");
const clips = fs.existsSync(clipDir) ? fs.readdirSync(clipDir).filter((f) => /\.(mp4|mov|webm)$/i.test(f)) : [];
if (clips.length) gut(`${clips.length} Hintergrund-Clips im Asset-Zweig`);
else warnung("Keine Hintergrund-Clips – die Reels laufen mit der selbst berechneten Animation.");
if (CONFIG.bilder.aktiv && CONFIG.bilder.key) gut("Pexels-Schlüssel gesetzt, Titelbilder werden geholt und freigestellt");
else warnung("Kein Pexels-Schlüssel – die Titelfolien bleiben beim Icon.");

/* 4. Marke --------------------------------------------------------------- */
console.log(zeilen.splice(0).join("\n") + "\n\nMarke");
if (CONFIG.marke.name) gut(`Markenname: ${CONFIG.marke.name}`);
else warnung("IG_MARKE ist leer – im Auftrag ans Modell steht dann „eines Instagram-Kanals“ statt des Namens.");
if (CONFIG.marke.handle) gut(`Handle in der Fußzeile: ${CONFIG.marke.handle}`);
else warnung("IG_HANDLE ist leer – die Fußzeile der Kacheln bleibt links leer.");

/* 5. Fazit --------------------------------------------------------------- */
console.log(zeilen.splice(0).join("\n"));
/* Zwei verschiedene Fragen: Was tut DIESER Lauf, und was tut der Zeitplan?
   Ein von Hand ausgeloester Lauf ist immer trocken; ob der naechste
   stuendliche Lauf veroeffentlicht, haengt allein an IG_PAUSE. */
const trocken = CONFIG.instagram.trockenlauf;
const pause = String(process.env.IG_PAUSE || "").toLowerCase() === "true";
console.log(`\nDieser Lauf: ${trocken ? "TROCKEN – es wird nichts veröffentlicht." : "würde LIVE veröffentlichen."}`);
console.log(`Zeitplan:    ${pause ? "steht auf Pause (IG_PAUSE=true) – die stündlichen Läufe veröffentlichen nichts." : "LIVE – der nächste stündliche Lauf veröffentlicht, was fällig ist."}`);
/* Auch das Fazit auf stdout: Auf stderr mischt GitHub die Reihenfolge, und
   dann steht „1 Punkt verhindert das Veröffentlichen“ mitten im Bericht. */
if (blocker) { console.log(`\n${blocker} Punkt${blocker === 1 ? "" : "e"} verhindert das Veröffentlichen.`); process.exitCode = 1; }
else console.log("\nAlles bereit.");
