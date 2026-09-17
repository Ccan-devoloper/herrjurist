/**
 * Newsletter-Test: Landingpage, Double-Opt-In und Übersicht.
 *
 * Bewusst ein EIGENER Worker, nicht eine weitere Route im Webhook-Worker.
 * Der Webhook trägt inzwischen den Story-Bezug für die Antworten des Bots;
 * ein Versuchsaufbau darf ihn nicht mit in den Ausfall ziehen können. Zwei
 * Worker kosten dasselbe wie einer (Free: 100.000 Anfragen am Tag) und haben
 * getrennte Fehlerräume.
 *
 * Kein Speicher im Worker: Der Bestätigungslink trägt die Adresse signiert in
 * sich (HMAC-SHA256). Deshalb schreibt die Anmeldung nirgends etwas – erst
 * der bestätigte Klick löst einen repository_dispatch aus, und nur dort wird
 * die Adresse in die verschlüsselte Liste im Asset-Zweig aufgenommen.
 *
 * Der Inhalt der Übersicht kommt aus daten/themen.mjs – demselben Pool, aus
 * dem der Bot seine Beiträge zieht. Damit gibt es keine zweite Wahrheit, die
 * veraltet: Wächst der Pool, wächst die Übersicht mit.
 *
 * Nötige Secrets (in Cloudflare, NIE im Code oder im Chat):
 *   NEWSLETTER_SECRET - langes Zufallsgeheimnis, identisch als GitHub-Secret
 *   GITHUB_TOKEN      - Fine-grained PAT, nur "Contents: Read and write"
 * Variablen:
 *   GITHUB_REPO       - z. B. Ccan-devoloper/herrjurist
 *   MARKE             - Anzeigename, z. B. "Herr Jurist"
 *   ANBIETER, ANSCHRIFT, KONTAKT - Impressumsangaben (Pflicht, § 5 DDG)
 */

import { THEMEN } from "../daten/themen.mjs";
import { FAECHER, GEBIETE } from "../daten/gebiete.mjs";

/* --- Kleinkram ------------------------------------------------------------ */
const enc = new TextEncoder();
const b64url = (bytes) => btoa(String.fromCharCode(...new Uint8Array(bytes))).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
const vonB64url = (s) => Uint8Array.from(atob(String(s).replace(/-/g, "+").replace(/_/g, "/")), (c) => c.charCodeAt(0));
const escape = (s) => String(s).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));

/* Ein Geheimnis, mehrere Verwendungen – jede mit eigener Ableitung. Muss mit
   src/newsletter.mjs Zeichen für Zeichen übereinstimmen, sonst passen die
   Signaturen von Worker und Actions-Lauf nicht zusammen. */
async function hmacSchluessel(geheim, zweck) {
  const roh = await crypto.subtle.digest("SHA-256", enc.encode(`herrjurist-newsletter-v1|${zweck}|${geheim}`));
  return crypto.subtle.importKey("raw", roh, { name: "HMAC", hash: "SHA-256" }, false, ["sign"]);
}

async function signieren(text, geheim, zweck) {
  return b64url(await crypto.subtle.sign("HMAC", await hmacSchluessel(geheim, zweck), enc.encode(text)));
}

/* Vergleich in konstanter Zeit – ein früher Abbruch verrät über die Laufzeit,
   wie viele Zeichen stimmten. */
function gleich(a, b) {
  if (a.length !== b.length) return false;
  let u = 0;
  for (let i = 0; i < a.length; i++) u |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return u === 0;
}

export async function tokenBauen(email, zweck, gueltigMs, geheim) {
  const nutzlast = b64url(enc.encode(JSON.stringify({ e: String(email).toLowerCase(), z: zweck, exp: Date.now() + gueltigMs })));
  return `${nutzlast}.${await signieren(nutzlast, geheim, "token")}`;
}

export async function tokenLesen(token, zweck, geheim) {
  const [nutzlast, sig] = String(token || "").split(".");
  if (!nutzlast || !sig) return null;
  if (!gleich(await signieren(nutzlast, geheim, "token"), sig)) return null;
  let d;
  try { d = JSON.parse(new TextDecoder().decode(vonB64url(nutzlast))); } catch { return null; }
  if (d?.z !== zweck || !Number.isFinite(d?.exp) || d.exp < Date.now()) return null;
  return String(d.e || "").toLowerCase() || null;
}

/* Adressprüfung – identisch zu src/newsletter.mjs gehalten. */
export function emailGueltig(email) {
  const s = String(email || "").trim();
  if (s.length < 6 || s.length > 254) return false;
  if (/[\s<>,;"\\\r\n]/.test(s)) return false;
  return /^[^@]+@[^@.]+(\.[^@.]+)+$/.test(s);
}

/* --- Missbrauchsbremse ----------------------------------------------------
   Das Formular schickt am Ende eine E-Mail an eine fremde Adresse. Ohne
   Bremse ließe sich damit jemand zumüllen. Drei billige, zustandslose Hürden:
   ein signiertes Formularticket (wer POSTet, muss die Seite geholt haben),
   eine Mindestverweildauer und ein Honigtopf-Feld, das nur Skripte ausfüllen.
   Das hält Gelegenheitsunsinn ab; gegen einen entschlossenen Angreifer hilft
   nur die Ratenbegrenzung von Cloudflare (siehe README). */
const ipKennung = (request) => {
  const ip = request.headers.get("cf-connecting-ip") || "";
  return ip.includes(":") ? ip.split(":").slice(0, 4).join(":") : ip.split(".").slice(0, 3).join(".");
};

async function formularTicket(request, geheim) {
  const ts = String(Date.now());
  return `${ts}.${await signieren(`${ts}|${ipKennung(request)}`, geheim, "formular")}`;
}

async function ticketGilt(ticket, request, geheim) {
  const [ts, sig] = String(ticket || "").split(".");
  if (!ts || !sig) return false;
  if (!gleich(await signieren(`${ts}|${ipKennung(request)}`, geheim, "formular"), sig)) return false;
  const alter = Date.now() - Number(ts);
  return alter >= 2000 && alter <= 30 * 60e3;          // 2 s bis 30 min
}

/* --- GitHub ---------------------------------------------------------------
   Der Worker verschickt keine Mail (Workers können kein SMTP). Er stößt den
   Actions-Lauf an, der die schon vorhandenen SMTP-Zugänge des Wochenberichts
   nutzt. So kommt kein weiterer Dienst und keine weitere Rechnung dazu.
   Im Nutzdatenteil steht nur das signierte Token – die Adresse steckt darin
   und ist damit gegen Veränderung geschützt. */
async function anGithub(env, typ, token) {
  const antwort = await fetch(`https://api.github.com/repos/${env.GITHUB_REPO}/dispatches`, {
    method: "POST",
    headers: {
      authorization: `Bearer ${env.GITHUB_TOKEN}`,
      accept: "application/vnd.github+json",
      "content-type": "application/json",
      "user-agent": "herrjurist-newsletter",
    },
    body: JSON.stringify({ event_type: typ, client_payload: { token, empfangen: new Date().toISOString() } }),
  });
  if (!antwort.ok) console.log(`GitHub lehnte ab (${typ}): ${antwort.status}`);
}

/* --- Seitengerüst --------------------------------------------------------- */
const FARBEN = { 1: "#2d5be3", 2: "#ff7a45", 3: "#23d98b", 0: "#6b4bd6" };

function seite({ titel, inhalt, env, breit = false }) {
  const marke = env.MARKE || "Herr Jurist";
  return new Response(`<!doctype html>
<html lang="de"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>${escape(titel)} · ${escape(marke)}</title>
<meta name="robots" content="noindex">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&family=Inter:wght@400;600&display=swap" rel="stylesheet">
<style>
:root{--grund:#0b0b0d;--flaeche:#161619;--text:#fff;--weich:#b9b9c2;--linie:#2a2a30;--g1:${FARBEN[1]};--g2:${FARBEN[2]};--g3:${FARBEN[3]};--g0:${FARBEN[0]};--zr:var(--g1);--sr:var(--g2);--oer:var(--g3)}
*{box-sizing:border-box}
body{margin:0;background:var(--grund);color:var(--text);font:16px/1.6 Inter,system-ui,sans-serif;-webkit-text-size-adjust:100%}
.h{max-width:${breit ? "1100px" : "640px"};margin:0 auto;padding:40px 20px 72px}
h1{font:700 clamp(30px,6vw,46px)/1.08 "Space Grotesk",sans-serif;letter-spacing:-.02em;margin:0 0 16px}
h2{font:700 22px/1.2 "Space Grotesk",sans-serif;margin:36px 0 10px}
p{margin:0 0 16px}
.weich{color:var(--weich)}
.band{display:flex;gap:6px;margin-bottom:28px}
.band i{height:6px;flex:1;border-radius:99px;display:block}
.karte{background:var(--flaeche);border:1px solid var(--linie);border-radius:18px;padding:22px}
label{display:block;font-weight:600;margin:0 0 8px}
input[type=email]{width:100%;padding:15px 16px;border-radius:12px;border:1px solid var(--linie);background:#0b0b0d;color:#fff;font-size:17px}
input[type=email]:focus{outline:2px solid var(--oer);outline-offset:1px}
button{margin-top:12px;width:100%;padding:16px;border:0;border-radius:12px;background:var(--oer);color:#07301f;font:700 17px "Space Grotesk",sans-serif;cursor:pointer}
button:hover{filter:brightness(1.08)}
.knopf{display:inline-block;padding:16px 26px;border-radius:12px;background:var(--oer);color:#07301f;font:700 17px "Space Grotesk",sans-serif;text-decoration:none}
.topf{position:absolute;left:-9999px}
.mini{font-size:13px;color:var(--weich);line-height:1.5}
a{color:#7fe8bb}
ul{margin:0 0 16px;padding-left:20px}
li{margin:0 0 6px}
.probe{border-left:3px solid var(--zr);padding:2px 0 2px 12px;margin:0 0 12px}
.probe b{display:block;font-weight:600}
.probe span{color:var(--weich);font-size:14px}
footer{margin-top:48px;border-top:1px solid var(--linie);padding-top:18px}
</style></head><body><div class="h">
<div class="band"><i style="background:var(--zr)"></i><i style="background:var(--sr)"></i><i style="background:var(--oer)"></i></div>
${inhalt}
<footer class="mini"><a href="/impressum">Impressum</a> · <a href="/datenschutz">Datenschutz</a> · ${escape(marke)}</footer>
</div></body></html>`, { headers: { "content-type": "text/html; charset=utf-8", "cache-control": "no-store" } });
}

/* --- Landingpage ---------------------------------------------------------- */
function themenGezaehlt() {
  const hoch = THEMEN.filter((t) => t.prioritaet === "hoch");
  return { anzahl: hoch.length, normen: new Set(hoch.flatMap((t) => t.normen || [])).size };
}

async function startseite(request, env, { fehler = "" } = {}) {
  const { anzahl, normen } = themenGezaehlt();
  const ticket = await formularTicket(request, env.NEWSLETTER_SECRET);
  /* Eine Probe je Rechtsgebiet: Die drei Farben sind der Kern der Marke -
     drei blaue Zivilrechtsfragen untereinander sagen darueber nichts. */
  const proben = [1, 2, 3].map((g) => THEMEN.find((t) => t.prioritaet === "hoch" && t.normen?.length >= 2 && FAECHER[t.fach]?.gebiet === g)).filter(Boolean);
  return seite({
    titel: "Examens-Übersicht", env,
    inhalt: `
<h1>${anzahl} Examensfragen.<br>Die Normen dazu.<br>Eine Seite.</h1>
<p class="weich">Die Fragen, die im Ersten und Zweiten Staatsexamen immer wieder drankommen – nach Rechtsgebiet sortiert, jede mit den tragenden Normen. ${normen} Vorschriften insgesamt. Zum Durchgehen vor der Klausur, nicht zum Lesen im Sessel.</p>
${proben.map((t) => `<div class="probe" style="border-color:var(--g${FAECHER[t.fach]?.gebiet ?? 0})"><b>${escape(t.titel)}</b><span>${escape((t.normen || []).join(" · "))}</span></div>`).join("")}
<p class="weich">…und ${anzahl - proben.length} weitere.</p>
<div class="karte">
  <form method="post" action="/anmelden">
    <label for="email">E-Mail eintragen, Übersicht sofort ansehen</label>
    <input id="email" name="email" type="email" required autocomplete="email" placeholder="du@beispiel.de" inputmode="email">
    <input class="topf" type="text" name="webseite" tabindex="-1" autocomplete="off" aria-hidden="true">
    <input type="hidden" name="ticket" value="${escape(ticket)}">
    <button type="submit">Übersicht anfordern</button>
  </form>
  ${fehler ? `<p class="mini" style="color:#ff9c9c;margin-top:12px">${escape(fehler)}</p>` : ""}
  <p class="mini" style="margin:14px 0 0">Du bekommst eine Mail mit einem Bestätigungslink. Ein Klick – und die Übersicht steht sofort da. Danach schicke ich dir neue Ausgaben; abmelden geht jederzeit mit einem Klick. Ohne die Bestätigung wird nichts gespeichert. <a href="/datenschutz">Datenschutz</a></p>
</div>`,
  });
}

/* --- Die Übersicht selbst -------------------------------------------------
   Als Webseite statt als PDF: druckbar („Drucken → Als PDF sichern“), auf dem
   Handy lesbar, ohne Build-Schritt und ohne Binärdatei im Repository. Für den
   Versuch ist das der kürzeste Weg zu einem echten Gegenwert; ein gesetztes
   PDF lohnt erst, wenn sich zeigt, dass überhaupt jemand einträgt. */
function uebersichtSeite(env) {
  const hoch = THEMEN.filter((t) => t.prioritaet === "hoch");
  const nachGebiet = new Map();
  for (const t of hoch) {
    const fach = FAECHER[t.fach];
    if (!fach) continue;
    const g = fach.gebiet ?? 0;
    if (!nachGebiet.has(g)) nachGebiet.set(g, new Map());
    const faecher = nachGebiet.get(g);
    if (!faecher.has(t.fach)) faecher.set(t.fach, []);
    faecher.get(t.fach).push(t);
  }
  const reihenfolge = [1, 2, 3, 0];
  const teile = [];
  for (const g of reihenfolge) {
    const faecher = nachGebiet.get(g);
    if (!faecher) continue;
    const name = GEBIETE[g]?.label || "Klausurtechnik und Kopfsache";
    teile.push(`<h2 style="color:var(--g${g})">${escape(name)}</h2>`);
    for (const [kuerzel, liste] of faecher) {
      teile.push(`<h3>${escape(FAECHER[kuerzel].label)}</h3><ol class="fr">`);
      for (const t of liste) {
        const normen = (t.normen || []).join(" · ");
        teile.push(`<li>${escape(t.titel)}${normen ? `<span>${escape(normen)}</span>` : ""}</li>`);
      }
      teile.push("</ol>");
    }
  }
  return seite({
    titel: "Die Übersicht", env, breit: true,
    inhalt: `
<h1>Examensfragen mit Normen</h1>
<p class="weich">${hoch.length} Fragen, nach Rechtsgebiet und Fach sortiert. Zum Speichern: im Browser <b>Drucken → Als PDF sichern</b>.</p>
<p><a class="knopf" href="#" onclick="window.print();return false">Als PDF speichern</a></p>
<style>
h3{font:600 15px/1.2 Inter,sans-serif;color:var(--weich);text-transform:uppercase;letter-spacing:.06em;margin:22px 0 8px}
ol.fr{columns:2;column-gap:36px;padding-left:20px;margin:0}
ol.fr li{break-inside:avoid;margin:0 0 10px}
ol.fr li span{display:block;font-size:13px;color:var(--weich)}
@media(max-width:700px){ol.fr{columns:1}}
@media print{
  /* Auf Weiss trägt keine der Bildschirmfarben: Hellgrau auf Weiss ist
     unlesbar, und das helle Blau/Gruen verliert auf Papier den Kontrast. */
  :root{--weich:#4a4a52;--g1:#2f63e0;--g2:#c2400f;--g3:#15764a;--g0:#4b2fa8}
  body{background:#fff;color:#111}
  .band,.knopf,footer,p:has(.knopf){display:none}
  h1{font-size:26pt;margin-bottom:6pt}
  h2{page-break-after:avoid;margin:16pt 0 4pt}
  h3{page-break-after:avoid}
  ol.fr{columns:2;font-size:9.5pt;line-height:1.35}
  ol.fr li span{font-size:8.5pt}
  .h{max-width:none;padding:0}
  @page{margin:12mm 10mm}
}
</style>
${teile.join("")}`,
  });
}

/* --- Rechtstexte ----------------------------------------------------------
   Pflichtangaben stehen als Variablen im Worker, nicht im Code: Eine private
   Anschrift gehört nicht in ein öffentliches Repository. Fehlen sie, sagt die
   Seite das offen – lieber ein sichtbarer Hinweis als ein stiller Verstoß. */
function angabe(env, feld, hinweis) {
  return env[feld] ? escape(env[feld]) : `<mark style="background:#ffb020;color:#000">${escape(hinweis)}</mark>`;
}

const impressum = (env) => seite({
  titel: "Impressum", env,
  inhalt: `<h1>Impressum</h1><p>Angaben nach § 5 DDG:</p>
<p>${angabe(env, "ANBIETER", "ANBIETER fehlt – im Worker als Variable eintragen")}<br>
${angabe(env, "ANSCHRIFT", "ANSCHRIFT fehlt – im Worker als Variable eintragen")}<br>
${angabe(env, "KONTAKT", "KONTAKT fehlt – im Worker als Variable eintragen")}</p>`,
});

const datenschutz = (env) => seite({
  titel: "Datenschutz", env,
  inhalt: `<h1>Datenschutz</h1>
<h2>Was gespeichert wird</h2>
<p>Trägst du deine E-Mail-Adresse ein, wird sie zunächst <b>nirgends gespeichert</b>. Sie steht nur signiert im Bestätigungslink, den du per Mail bekommst. Erst wenn du diesen Link anklickst, wird die Adresse in eine verschlüsselte Liste aufgenommen (Double-Opt-In).</p>
<h2>Wozu</h2>
<p>Um dir die angeforderte Übersicht und danach neue Ausgaben des Newsletters zu schicken. Rechtsgrundlage ist deine Einwilligung, Art. 6 Abs. 1 lit. a DSGVO. Du kannst sie jederzeit über den Abmeldelink in jeder Mail widerrufen.</p>
<h2>Wer sie verarbeitet</h2>
<p>Die Seite läuft bei Cloudflare, Inc., der Versand über den im Impressum genannten Anbieter und dessen Mailanbieter. Die Liste liegt verschlüsselt in einem GitHub-Repository (GitHub, Inc.). Es gibt kein Tracking, keine Analyse, keine Werbe-Cookies; die Seite setzt überhaupt keine Cookies.</p>
<h2>Wie lange</h2>
<p>Bis zum Widerruf. Nach einer Abmeldung bleibt die Adresse gespeichert, damit sie nicht versehentlich erneut angeschrieben wird; auf Wunsch wird sie vollständig gelöscht.</p>
<h2>Deine Rechte</h2>
<p>Auskunft, Berichtigung, Löschung, Einschränkung, Widerspruch und Datenübertragbarkeit (Art. 15–21 DSGVO) sowie Beschwerde bei einer Aufsichtsbehörde. Kontakt: siehe <a href="/impressum">Impressum</a>.</p>`,
});

/* --- Formular entgegennehmen ---------------------------------------------- */
async function anmelden(request, env, ctx) {
  const form = await request.formData();
  const email = String(form.get("email") || "").trim();
  if (form.get("webseite")) return seite({ titel: "Danke", env, inhalt: "<h1>Danke</h1><p>Schau in dein Postfach.</p>" });
  if (!emailGueltig(email)) return startseite(request, env, { fehler: "Diese Adresse sieht nicht vollständig aus. Bitte noch einmal." });
  if (!await ticketGilt(form.get("ticket"), request, env.NEWSLETTER_SECRET)) {
    return startseite(request, env, { fehler: "Das Formular war zu lange offen. Bitte noch einmal absenden." });
  }
  const token = await tokenBauen(email, "doi", 48 * 3600e3, env.NEWSLETTER_SECRET);
  ctx.waitUntil(anGithub(env, "newsletter-anmeldung", token));
  return seite({
    titel: "Fast geschafft", env,
    inhalt: `<h1>Fast geschafft</h1>
<p>Wir haben eine Mail an <b>${escape(email)}</b> geschickt. Ein Klick auf den Link darin – und die Übersicht steht sofort da.</p>
<p class="weich">Die Mail braucht meist unter einer Minute. Nichts angekommen? Dann schau bitte im Spam-Ordner nach und markiere die Mail als „Kein Spam“, sonst gehen die nächsten denselben Weg.</p>`,
  });
}

async function bestaetigen(request, env, ctx) {
  const email = await tokenLesen(new URL(request.url).searchParams.get("t"), "doi", env.NEWSLETTER_SECRET);
  if (!email) {
    return seite({
      titel: "Link abgelaufen", env,
      inhalt: `<h1>Dieser Link gilt nicht mehr</h1><p>Bestätigungslinks laufen nach 48 Stunden ab. Trag deine Adresse einfach noch einmal ein, dann kommt ein frischer.</p><p><a class="knopf" href="/">Noch einmal eintragen</a></p>`,
    });
  }
  const token = await tokenBauen(email, "doi", 48 * 3600e3, env.NEWSLETTER_SECRET);
  ctx.waitUntil(anGithub(env, "newsletter-bestaetigt", token));
  const datei = await tokenBauen(email, "datei", 365 * 24 * 3600e3, env.NEWSLETTER_SECRET);
  return seite({
    titel: "Bestätigt", env,
    inhalt: `<h1>Bestätigt. Hier ist deine Übersicht.</h1>
<p><a class="knopf" href="/uebersicht?t=${escape(datei)}">Übersicht öffnen</a></p>
<p class="weich">Du bekommst denselben Link gleich noch einmal per Mail, damit du ihn später wiederfindest. Auf der Seite speicherst du sie über <b>Drucken → Als PDF sichern</b>.</p>`,
  });
}

async function abmelden(request, env, ctx) {
  const email = await tokenLesen(new URL(request.url).searchParams.get("t"), "abmelden", env.NEWSLETTER_SECRET);
  if (!email) return seite({ titel: "Abmelden", env, inhalt: `<h1>Dieser Abmeldelink gilt nicht</h1><p>Schreib eine kurze Mail an die Adresse im <a href="/impressum">Impressum</a>, dann wird die Adresse von Hand ausgetragen.</p>` });
  ctx.waitUntil(anGithub(env, "newsletter-abmeldung", await tokenBauen(email, "abmelden", 3600e3, env.NEWSLETTER_SECRET)));
  return seite({ titel: "Abgemeldet", env, inhalt: `<h1>Abgemeldet</h1><p>${escape(email)} bekommt keine weiteren Mails. Kein Nachhaken, kein „schade, dass du gehst“.</p>` });
}

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const pfad = url.pathname.replace(/\/+$/, "") || "/";

    if (!env.NEWSLETTER_SECRET) return new Response("NEWSLETTER_SECRET fehlt", { status: 500 });

    if (request.method === "POST" && pfad === "/anmelden") return anmelden(request, env, ctx);
    if (request.method !== "GET") return new Response("method not allowed", { status: 405 });

    switch (pfad) {
      case "/": return startseite(request, env);
      case "/ja": return bestaetigen(request, env, ctx);
      case "/abmelden": return abmelden(request, env, ctx);
      case "/impressum": return impressum(env);
      case "/datenschutz": return datenschutz(env);
      case "/uebersicht": {
        const email = await tokenLesen(url.searchParams.get("t"), "datei", env.NEWSLETTER_SECRET);
        if (!email) return seite({ titel: "Nicht freigegeben", env, inhalt: `<h1>Dieser Link gilt nicht</h1><p>Die Übersicht gibt es über die Anmeldung.</p><p><a class="knopf" href="/">Zur Anmeldung</a></p>` });
        return uebersichtSeite(env);
      }
      default: return seite({ titel: "Nichts gefunden", env, inhalt: `<h1>Hier ist nichts</h1><p><a class="knopf" href="/">Zur Startseite</a></p>` });
    }
  },
};
