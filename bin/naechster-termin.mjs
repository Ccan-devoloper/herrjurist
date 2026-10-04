/* ==========================================================================
   Nächster Veröffentlichungstermin der Vorproduktion – für die Weckkette.

   Liest vorproduktion/<heute>.json (Dashboard) und state/plaene/<heute>.json
   (Sendestatus des Bots) direkt aus dem Asset-Zweig über die GitHub-API und
   gibt den nächsten offenen Termin als Unix-Zeit in Sekunden aus. Keine
   Ausgabe = heute nichts mehr offen.

   Nur Node-Bordmittel: läuft ohne npm ci.
   Umgebung: GH_TOKEN, GH_REPO (owner/repo), optional IG_ASSET_BRANCH und
   NAECHSTER_SEIT (Unix-Sekunden: Start des Laufs, zu dem die Kette gehört).
   ========================================================================== */

import { heuteIso } from "../src/zeit.mjs";
import { planFuerWecker, naechsterTermin } from "../src/vorproduktion-zeitplan.mjs";

const repo = process.env.GH_REPO;
const zweig = process.env.IG_ASSET_BRANCH || "instagram-assets";

async function datei(pfad) {
  const url = `https://api.github.com/repos/${repo}/contents/${pfad}?ref=${encodeURIComponent(zweig)}`;
  const r = await fetch(url, {
    headers: {
      Accept: "application/vnd.github.raw+json",
      Authorization: `Bearer ${process.env.GH_TOKEN}`,
      "X-GitHub-Api-Version": "2022-11-28",
    },
  });
  if (r.status === 404) return null;
  if (!r.ok) throw new Error(`${pfad}: HTTP ${r.status}`);
  return JSON.parse(await r.text());
}

async function main() {
  const datum = heuteIso();
  const tag = await datei(`vorproduktion/${datum}.json`);
  if (!tag) return;
  const plan = planFuerWecker(tag, await datei(`state/plaene/${datum}.json`));
  const jetzt = Date.now();
  const seit = Number(process.env.NAECHSTER_SEIT) > 0 ? Math.min(jetzt, Number(process.env.NAECHSTER_SEIT) * 1000) : jetzt;
  const t = naechsterTermin(plan, datum, jetzt, seit);
  if (t !== null) console.log(Math.floor(t / 1000));
}

main().catch((e) => {
  /* Die Weckkette fällt dann auf den stündlichen Takt zurück. */
  console.error(`naechster-termin: ${e.message}`);
});
