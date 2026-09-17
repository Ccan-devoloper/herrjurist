#!/usr/bin/env node
/* ==========================================================================
   Einzelprobe für den interaktiven Story-Weg.

   Wozu es das braucht: „Erst mit einem Testkonto" lässt sich im laufenden
   Tagesbetrieb nicht machen. Trüge man das Testkonto als IG_PRIVAT_USER ein,
   ginge die Prüfungsfrage-Story an das Testkonto - und beim echten Kanal
   fehlte sie an dem Tag, weil der Weg ja gelungen ist. Diese Probe läuft
   deshalb ganz außerhalb des Tageslaufs: Sie fasst weder Tagesplan noch
   Ledger an und veröffentlicht nichts über die Graph API.

   Aufruf (Zugangsdaten stehen in der Umgebung, nie in der Kommandozeile):
     node bin/interaktiv-probe.mjs --state <Verzeichnis> [--datei <story.json>]

   Ohne --datei nimmt die Probe ein festes Beispiel. Das ist Absicht: Die
   Frage, die hier beantwortet wird, ist „trägt der Weg?", nicht „wie liest
   sich der Text von heute?".
   ========================================================================== */

import fs from "node:fs";
import path from "node:path";
import { CONFIG } from "../src/config.mjs";
import { storyRendernInteraktiv, browserBeenden } from "../src/render.mjs";
import { interaktivPosten, umfrageBauen, sitzungLaden } from "../src/interaktiv.mjs";

const arg = (name, standard = "") => {
  const i = process.argv.indexOf(`--${name}`);
  return i >= 0 && process.argv[i + 1] ? process.argv[i + 1] : standard;
};

const BEISPIEL = {
  slot: "probe",
  art: "frage",
  fach: "schuld",
  klausur: 1,
  ueberzeile: "Prüfungsfrage Schuldrecht AT",
  titel: "Wann tritt Konkretisierung bei der Schickschuld ein?",
  optionen: [
    "Mit Übergabe an die Transportperson, § 243 Abs. 2 BGB",
    "Erst mit Ankunft der Ware beim Gläubiger",
    "Mit Abschluss des Kaufvertrags",
  ],
  fachLabel: "Schuldrecht AT",
};

const stateDir = arg("state", "");
if (!stateDir) { console.error("✗ --state <Verzeichnis> fehlt – dort liegt der Sitzungstresor."); process.exit(2); }
fs.mkdirSync(stateDir, { recursive: true });

const { nutzer, passwort } = CONFIG.interaktiv;
if (!nutzer || !passwort) { console.error("✗ IG_PRIVAT_USER und IG_PRIVAT_PASS fehlen."); process.exit(2); }

const story = arg("datei") ? JSON.parse(fs.readFileSync(arg("datei"), "utf8")) : BEISPIEL;
if (!(story.optionen || []).length) { console.error("✗ Die Story hat keine Optionen – ohne die gibt es nichts abzufragen."); process.exit(2); }

console.log(`Probe für @${nutzer}`);
console.log(`  Sitzung vorhanden: ${sitzungLaden(stateDir, nutzer) ? "ja (keine Neuanmeldung nötig)" : "nein (es wird einmal angemeldet)"}`);

const ziel = path.join("out", "probe", "interaktiv-probe.jpg");
const { pfad, platz } = await storyRendernInteraktiv(story, ziel);
await browserBeenden();
if (!platz) { console.error("✗ Kein Platz für die Umfrage gemessen – die Vorlage hat den Streifen nicht gerendert."); process.exit(1); }

const umfrage = umfrageBauen(story, platz);
console.log(`  Bild: ${pfad}`);
console.log(`  Sticker: „${umfrage.frage}" ${umfrage.optionen.join("/")} bei x=${umfrage.x.toFixed(3)} y=${umfrage.y.toFixed(3)}`);

try {
  const id = await interaktivPosten({ bildPfad: pfad, umfrage, stateDir, ledger: {}, log: console.log });
  console.log(`\n✓ Story mit nativer Umfrage veröffentlicht: ${id}`);
  console.log("  Jetzt im Konto nachsehen: Ist der Sticker antippbar und liegt er frei?");
} catch (e) {
  console.error(`\n✗ Nicht veröffentlicht (${e.art || "fehler"}): ${e.message}`);
  if (e.art === "challenge") console.error("  Instagram verlangt eine Bestätigung. In der App anmelden, bestätigen, dann erneut – NICHT sofort wiederholen.");
  if (e.art === "sitzung") console.error("  Es liegt keine gültige Sitzung vor und Neuanmeldung ist aus. Einmal am eigenen Rechner\n  anmelden (node bin/interaktiv-anmelden.mjs) und den Wert als Secret IG_PRIVAT_SITZUNG eintragen.");
  if (["challenge", "bremse"].includes(e.art)) {
    console.error("  Hinweis: Im Tageslauf würde der Weg jetzt 24 Stunden ruhen. Diese Probe führt kein\n  Ledger, hier ist also nichts gespeichert – trotzdem nicht sofort wiederholen.");
  }
  if (e.art === "aufbau") console.error("  Läuft instagrapi in dieser Umgebung? IG_PYTHON zeigt auf: " + CONFIG.interaktiv.python);
  process.exit(1);
}
