#!/usr/bin/env node
/* ==========================================================================
   TikTok einmalig anmelden: liefert den Refresh-Token für das Secret
   TT_REFRESH_TOKEN. Läuft auf deinem Rechner, nicht im Bot.

   Ablauf (zwei Aufrufe):
     1. node bin/tiktok-anmelden.mjs
          → zeigt die Anmelde-Adresse. Im Browser öffnen, mit dem Konto des
            Kanals anmelden, Zugriff bestätigen. TikTok leitet auf deine
            Rückleit-Adresse weiter; in der Adresszeile steht ?code=…
     2. node bin/tiktok-anmelden.mjs <code>
          → tauscht den Code gegen die Token und zeigt den Refresh-Token.

   Braucht als Umgebungsvariablen: TT_CLIENT_KEY, TT_CLIENT_SECRET und
   TT_REDIRECT_URI (genau die Rückleit-Adresse, die in der TikTok-App
   eingetragen ist). Nichts davon wird gespeichert oder gesendet außer an
   TikTok selbst.
   ========================================================================== */

const key = process.env.TT_CLIENT_KEY, secret = process.env.TT_CLIENT_SECRET, redirect = process.env.TT_REDIRECT_URI;
if (!key || !secret || !redirect) {
  console.error("Bitte TT_CLIENT_KEY, TT_CLIENT_SECRET und TT_REDIRECT_URI setzen, z. B.:\n  TT_CLIENT_KEY=… TT_CLIENT_SECRET=… TT_REDIRECT_URI=https://deine-seite.de/tiktok node bin/tiktok-anmelden.mjs");
  process.exit(1);
}
const code = process.argv[2];
if (!code) {
  const u = new URL("https://www.tiktok.com/v2/auth/authorize/");
  u.search = new URLSearchParams({ client_key: key, scope: "user.info.basic,video.publish,video.upload", response_type: "code", redirect_uri: redirect, state: String(Date.now()) }).toString();
  console.log(`\n1. Diese Adresse im Browser öffnen und mit dem Kanal-Konto anmelden:\n\n${u}\n\n2. Nach der Bestätigung steht in der Adresszeile ein Parameter code=… – den Wert kopieren (bis zum nächsten &) und aufrufen:\n\n   node bin/tiktok-anmelden.mjs <code>\n`);
  process.exit(0);
}
const res = await fetch("https://open.tiktokapis.com/v2/oauth/token/", { method: "POST", headers: { "Content-Type": "application/x-www-form-urlencoded" }, body: new URLSearchParams({ client_key: key, client_secret: secret, code: decodeURIComponent(code), grant_type: "authorization_code", redirect_uri: redirect }) });
const j = await res.json();
if (!j.refresh_token) { console.error("Kein Refresh-Token erhalten:", JSON.stringify(j).slice(0, 400)); process.exit(1); }
console.log(`\nAngemeldet als open_id ${j.open_id}. Gewährte Rechte: ${j.scope}\nRefresh-Token gültig ${Math.round((j.refresh_expires_in || 0) / 86400)} Tage.\n\nIn GitHub → Settings → Secrets → Actions eintragen:\n  TT_REFRESH_TOKEN = ${j.refresh_token}\n\nDen Token nirgendwo sonst ablegen. Der Bot erneuert ihn selbst und legt den jeweils neuesten verschlüsselt im Asset-Zweig ab.\n`);
