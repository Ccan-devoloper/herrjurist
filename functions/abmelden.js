// Cloudflare Pages Function: GET /abmelden?e=<E-Mail base64url>&t=<Signatur>
// Abmeldelink des Wochenbriefs. Der Wochenbrief geht als Transaktionsmail raus (kein Brevo-Logo im kostenlosen
// Tarif), deshalb gibt es keinen Brevo-Abmeldelink – dieser hier nimmt den Kontakt aus der Liste BREVO_LISTE.
// Die Signatur (HMAC-SHA256 über die Adresse, Schlüssel WOCHENBRIEF_SCHLUESSEL) erzeugt bin/wochenbrief-versand.mjs;
// ohne sie könnte jeder fremde Adressen abmelden.
// Einstellungen in Cloudflare Pages: WOCHENBRIEF_SCHLUESSEL (Secret, derselbe Wert wie in GitHub), BREVO_API_KEY, BREVO_LISTE.

const b64url = buf => btoa(String.fromCharCode(...new Uint8Array(buf))).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
const ausB64url = s => atob(s.replace(/-/g, '+').replace(/_/g, '/'));

async function signatur(schluessel, email) {
  const roh = Uint8Array.from(atob(schluessel), c => c.charCodeAt(0));
  const key = await crypto.subtle.importKey('raw', roh, { name: 'HMAC', hash: 'SHA-256' }, false, ['sign']);
  return b64url(await crypto.subtle.sign('HMAC', key, new TextEncoder().encode(`abmelden:${email}`))).slice(0, 22);
}

const seite = (titel, text) => new Response(`<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>${titel}</title>
<style>body{margin:0;min-height:100vh;display:grid;place-items:center;background:#FFF8EC;font:600 17px/1.5 system-ui,sans-serif;color:#16161d;padding:16px}div{max-width:440px;background:#fff;border:3px solid #16161d;border-radius:18px;box-shadow:6px 6px 0 #16161d;padding:24px}h1{font-size:24px;margin:0 0 8px}a{color:#7c5cff}</style></head>
<body><div><h1>${titel}</h1><p>${text}</p><p><a href="/">Zur Startseite</a></p></div></body></html>`, { headers: { 'content-type': 'text/html; charset=utf-8' } });

export async function onRequestGet({ request, env }) {
  const url = new URL(request.url);
  let email = '';
  try { email = ausB64url(url.searchParams.get('e') || '').trim().toLowerCase(); } catch {}
  const t = url.searchParams.get('t') || '';
  if (!email || !env.WOCHENBRIEF_SCHLUESSEL || t !== await signatur(env.WOCHENBRIEF_SCHLUESSEL, email)) {
    return seite('Link ungültig', 'Dieser Abmeldelink ist unvollständig. Antworte einfach auf den Wochenbrief, dann tragen wir dich von Hand aus.');
  }
  const res = await fetch(`https://api.brevo.com/v3/contacts/${encodeURIComponent(email)}?identifierType=email_id`, {
    method: 'PUT',
    headers: { 'api-key': env.BREVO_API_KEY, 'content-type': 'application/json', accept: 'application/json' },
    body: JSON.stringify({ unlinkListIds: [Number(env.BREVO_LISTE)] }),
  });
  if (!res.ok && res.status !== 404) {
    console.log('Abmelden fehlgeschlagen', res.status, await res.text());
    return seite('Hat nicht geklappt', 'Gerade gab es ein technisches Problem. Versuch es bitte später noch einmal oder antworte auf den Wochenbrief.');
  }
  return seite('Abgemeldet', 'Du bekommst den Wochenbrief ab jetzt nicht mehr. Schade, dass du gehst – du kannst dich jederzeit wieder eintragen.');
}
