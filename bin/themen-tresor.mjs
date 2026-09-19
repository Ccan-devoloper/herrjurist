#!/usr/bin/env node
/* Themenpool-Tresor: AES-256-GCM mit IG_WISSEN_KEY.
   packen [quelle]  -> daten/themen.json.enc
   pruefen          -> entschlüsselt nur zur Validierung, gibt keinen Inhalt aus
   auspacken [ziel] -> nur für lokale Pflege; Ziel liegt standardmäßig außerhalb von Git
*/

import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { pathToFileURL } from "node:url";
import { CONFIG } from "../src/config.mjs";
import { wissenVerschluesseln, wissenEntschluesseln } from "../src/wissen.mjs";

const [, , befehl, arg] = process.argv;
const geheim = CONFIG.wissen?.schluessel;
const encPfad = path.resolve("daten/themen.json.enc");
const abdruck = (s) => s ? crypto.createHash("sha256").update(String(s)).digest("hex").slice(0, 12) : "–";

if (!geheim) {
  console.error("IG_WISSEN_KEY fehlt.");
  process.exit(1);
}

async function packen(quelle = "daten/themen.mjs") {
  const q = path.resolve(quelle);
  if (!fs.existsSync(q)) throw new Error(`Quelle fehlt: ${q}`);
  const mod = await import(`${pathToFileURL(q).href}?t=${Date.now()}`);
  if (!Array.isArray(mod.THEMEN) || mod.THEMEN.length < 1) throw new Error("Quelle exportiert keinen gültigen THEMEN-Pool.");
  const text = JSON.stringify(mod.THEMEN);
  const verschluesselt = wissenVerschluesseln(text, geheim);
  fs.writeFileSync(encPfad, verschluesselt);
  console.log(`${mod.THEMEN.length} Themen verschlüsselt · ${verschluesselt.length} Byte · Schlüssel ${abdruck(geheim)}`);
}

function pruefen() {
  if (!fs.existsSync(encPfad)) throw new Error("daten/themen.json.enc fehlt.");
  const text = wissenEntschluesseln(fs.readFileSync(encPfad), geheim);
  const daten = JSON.parse(text);
  if (!Array.isArray(daten) || daten.length < 300) throw new Error(`Themenpool unplausibel: ${Array.isArray(daten) ? daten.length : "kein Array"}`);
  console.log(`${daten.length} Themen lesbar · Schlüssel ${abdruck(geheim)}`);
}

function auspacken(ziel = "../themenpool-klartext.json") {
  if (!fs.existsSync(encPfad)) throw new Error("daten/themen.json.enc fehlt.");
  const text = wissenEntschluesseln(fs.readFileSync(encPfad), geheim);
  JSON.parse(text);
  const z = path.resolve(ziel);
  fs.writeFileSync(z, text + "\n", { mode: 0o600 });
  console.log(`Themenpool nach ${z} geschrieben. Nicht ins Repository committen.`);
}

if (befehl === "packen") await packen(arg);
else if (befehl === "pruefen") pruefen();
else if (befehl === "auspacken") auspacken(arg);
else {
  console.log("Aufruf: node bin/themen-tresor.mjs packen|pruefen|auspacken [pfad]");
  process.exit(1);
}
