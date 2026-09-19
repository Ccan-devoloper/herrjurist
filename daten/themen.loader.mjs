/* ==========================================================================
   Verschlüsselter Themenpool.

   Der Klartext liegt nicht mehr im aktuellen Repository-Zustand. Der Pool
   wird mit demselben IG_WISSEN_KEY geöffnet wie die verschlüsselte
   Wissensbasis unter daten/wissen/. Verschlüsselung: AES-256-GCM.
   ========================================================================== */

import fs from "node:fs";
import { CONFIG } from "../src/config.mjs";
import { wissenEntschluesseln } from "../src/wissen.mjs";

const DATEI = new URL("./themen.json.enc", import.meta.url);

function laden() {
  const geheim = CONFIG.wissen?.schluessel;
  if (!geheim) throw new Error("IG_WISSEN_KEY fehlt – der Themenpool ist verschlüsselt.");
  if (!fs.existsSync(DATEI)) throw new Error("daten/themen.json.enc fehlt.");
  const text = wissenEntschluesseln(fs.readFileSync(DATEI), geheim);
  const daten = JSON.parse(text);
  if (!Array.isArray(daten) || daten.length < 1) throw new Error("Verschlüsselter Themenpool ist leer oder ungültig.");
  return daten;
}

export const THEMEN = laden();
