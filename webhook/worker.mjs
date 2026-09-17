/**
 * Mitschnitt-Worker für Instagram-Webhooks ("Shadow Logger").
 *
 * Er beantwortet NICHTS. Seine einzige Aufgabe: Jedes eingehende
 * Nachrichten-Ereignis von Meta unverändert festhalten, damit endlich
 * feststeht, was Instagram beim EINGANG einer Story-Antwort tatsächlich
 * mitschickt.
 *
 * Der Anlass: Am 16.09. lieferte die nachträgliche Abfrage über
 * /conversations bei einer Story-Antwort ein leeres `reply_to.story` -
 * weder ID noch URL. Daraus wurde vorschnell geschlossen, Instagram gebe
 * den Bezug überhaupt nicht heraus. Das ist ein Schluss von EINEM
 * Abfrageweg auf die ganze Plattform, und er ist nicht belegt: Meta
 * dokumentiert die Story-Referenz im eingehenden Ereignis. Ob sie bei
 * DIESEM Konto und DIESEM Zugang ankommt, beantwortet nur ein Mitschnitt.
 *
 * Bewusst ohne Datenbank: Der Worker reicht das Rohereignis an GitHub
 * weiter, wo es im Asset-Zweig als JSONL landet. Damit liegt der Beweis
 * dort, wo der Bot ohnehin seinen Zustand führt - lesbar, versioniert und
 * ohne einen weiteren Dienst, der Geld kosten oder ausfallen kann.
 *
 * Kosten: Cloudflare Workers Free deckt 100.000 Anfragen am Tag ab. Für
 * einen einzelnen Instagram-Kanal ist das um Größenordnungen zu viel.
 *
 * Nötige Secrets (in Cloudflare, NIE im Code oder im Chat):
 *   VERIFY_TOKEN   - frei gewählt, muss bei Meta identisch eingetragen sein
 *   APP_SECRET     - App-Geheimcode aus dem Meta-Dashboard
 *   GITHUB_TOKEN   - Fine-grained PAT, nur "Contents: Read and write"
 *   GITHUB_REPO    - Rueckfallziel, z. B. Ccan-devoloper/herrjurist
 *   ROUTEN         - optional, "<kontoId>=<owner/repo>,<kontoId>=<owner/repo>"
 *                    Beide Kanaele haengen an DERSELBEN Meta-App, also kommen
 *                    ihre Ereignisse ueber dieselbe Adresse herein. Ohne
 *                    Verteilung landeten Campus-Nachrichten im Jura-Repo.
 *                    Die Konto-ID steht in entry[].id.
 */

/* Signaturprüfung auf den ROHEN Bytes. Wer den Body erst parst und dann
   neu serialisiert, bekommt eine andere Byte-Folge und damit eine andere
   Signatur - ein Fehler, der lange unbemerkt bleibt, weil er nur die
   Prüfung entwertet, nicht den Ablauf stört. */
async function signaturStimmt(roh, kopf, geheim) {
  if (!kopf?.startsWith("sha256=")) return false;
  const schluessel = await crypto.subtle.importKey(
    "raw", new TextEncoder().encode(geheim),
    { name: "HMAC", hash: "SHA-256" }, false, ["sign"],
  );
  const sig = await crypto.subtle.sign("HMAC", schluessel, roh);
  const erwartet = [...new Uint8Array(sig)].map((b) => b.toString(16).padStart(2, "0")).join("");
  const gegeben = kopf.slice(7);
  /* Vergleich in konstanter Zeit: Ein früher Abbruch verrät über die
     Laufzeit, wie viele Zeichen stimmten. */
  if (erwartet.length !== gegeben.length) return false;
  let unterschied = 0;
  for (let i = 0; i < erwartet.length; i++) unterschied |= erwartet.charCodeAt(i) ^ gegeben.charCodeAt(i);
  return unterschied === 0;
}

/* Das Rohereignis nach GitHub reichen. Base64, damit kein Zeichen unterwegs
   verlorengeht, und als EIN Feld - client_payload verträgt nur wenige. */
/* Welche Repositories dieses Ereignis betrifft. Unbekannte Konten fallen auf
   GITHUB_REPO zurueck, damit ein neues Konto nicht stillschweigend ins Leere
   sendet - lieber im falschen Protokoll als gar nicht. */
function zieleFuer(env, roh) {
  const ziele = new Set();
  const karte = new Map(
    String(env.ROUTEN || "").split(",").map((t) => t.trim()).filter(Boolean)
      .map((t) => t.split("=")).filter((a) => a.length === 2)
      .map(([k, v]) => [k.trim(), v.trim()]),
  );
  try {
    const daten = JSON.parse(new TextDecoder().decode(roh));
    for (const e of daten?.entry || []) ziele.add(karte.get(String(e?.id)) || env.GITHUB_REPO);
  } catch { /* Unlesbares geht ans Rueckfallziel - der Mitschnitt soll es sehen. */ }
  if (!ziele.size) ziele.add(env.GITHUB_REPO);
  return [...ziele].filter(Boolean);
}

async function anGithub(env, roh, repo) {
  const antwort = await fetch(`https://api.github.com/repos/${repo}/dispatches`, {
    method: "POST",
    headers: {
      authorization: `Bearer ${env.GITHUB_TOKEN}`,
      accept: "application/vnd.github+json",
      "content-type": "application/json",
      "user-agent": "instagram-webhook-mitschnitt",
    },
    body: JSON.stringify({
      event_type: "instagram-webhook",
      client_payload: { roh: btoa(String.fromCharCode(...new Uint8Array(roh))), empfangen: new Date().toISOString() },
    }),
  });
  if (!antwort.ok) console.log(`GitHub lehnte ab (${repo}): ${antwort.status}`);
}

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);

    /* Metas Einrichtungsprüfung: Sie ruft die Adresse einmal per GET auf und
       erwartet die Challenge zurück. Ohne das lässt sich der Webhook gar
       nicht erst abonnieren. */
    if (request.method === "GET") {
      const p = url.searchParams;
      if (p.get("hub.mode") === "subscribe" && p.get("hub.verify_token") === env.VERIFY_TOKEN) {
        return new Response(p.get("hub.challenge") ?? "", { status: 200 });
      }
      return new Response("forbidden", { status: 403 });
    }

    if (request.method !== "POST") return new Response("method not allowed", { status: 405 });

    const roh = await request.arrayBuffer();
    if (!await signaturStimmt(roh, request.headers.get("x-hub-signature-256"), env.APP_SECRET)) {
      return new Response("bad signature", { status: 401 });
    }

    /* Meta erwartet schnell ein 200 und stellt sonst erneut zu. Das
       Weiterreichen läuft deshalb NACH der Antwort weiter - waitUntil hält
       den Worker dafür am Leben, ohne Meta warten zu lassen. */
    for (const repo of zieleFuer(env, roh)) ctx.waitUntil(anGithub(env, roh, repo));
    return new Response("EVENT_RECEIVED", { status: 200 });
  },
};
