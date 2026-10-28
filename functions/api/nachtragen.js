// Cloudflare Pages Function: POST /api/nachtragen
// Schickt bis zu 20 „offen:“-Anmeldungen erneut an Brevo. Wird stündlich vom Workflow
// .github/workflows/anmeldungen-nachtragen.yml aufgerufen. Gibt nur Zähler zurück, keine Adressen.
import { nachtragen } from "../_lib/brevo.js";

export async function onRequestPost({ env }) {
  const ergebnis = await nachtragen(env);
  return new Response(JSON.stringify(ergebnis), { headers: { "content-type": "application/json" } });
}
