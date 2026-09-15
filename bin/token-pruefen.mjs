#!/usr/bin/env node
/* ==========================================================================
   Token-Prüfung – fragt den Instagram-Token, was er darf.

   node bin/token-pruefen.mjs

   Anlass: Am 15.09. meldete die API für zwei Beiträge comments_count 1 und 2,
   lieferte aber auf {media}/comments zweimal 200 mit leerer Liste – einmal mit
   und einmal ohne replies{}. An der Feldverschachtelung lag es also nicht.
   Gleichzeitig gab /conversations null Unterhaltungen zurück. Beide Kanten
   brauchen eine Berechtigung, die über instagram_business_basic hinausgeht;
   Lesen der Medien und Veröffentlichen liefen weiter. Das Muster passt dazu,
   dass der Token vor dem Einschalten der Berechtigungen erzeugt wurde: Ein
   Token trägt die Berechtigungen, die beim Erzeugen angehakt waren, nicht die,
   die heute in den App-Einstellungen stehen.

   Dieses Skript kostet nichts – es ruft Claude nie auf und schreibt nirgends
   hin. Es gibt ausschließlich Zählwerte und Fehlermeldungen aus, niemals den
   Token selbst.

   Rückgabewert 1, wenn eine Berechtigung fehlt oder eine Kante stumm bleibt.
   ========================================================================== */

import path from "node:path";
import crypto from "node:crypto";
import { Instagram } from "../src/instagram.mjs";
import { Hosting } from "../src/hosting.mjs";
import { CONFIG } from "../src/config.mjs";

/* Der Token darf nie ins Protokoll. Was hier erscheint, ist ein Kürzel, das
   nur zum Vergleichen taugt: gleiche Prüfsumme = gleicher Token. */
const kuerzel = (t) => (t ? `${crypto.createHash("sha256").update(t).digest("hex").slice(0, 8)} (${t.length} Zeichen)` : "—");
const knapp = (o, n = 600) => { const s = JSON.stringify(o); return s.length > n ? `${s.slice(0, n)}…` : s; };

/* Berechtigungen, ohne die der Bot nicht vollständig arbeitet – jeweils mit
   dem, was ohne sie ausfällt. */
const NOETIG = {
  instagram_business_basic: "Beiträge lesen",
  instagram_business_content_publish: "veröffentlichen",
  instagram_business_manage_comments: "Kommentare lesen und beantworten",
  instagram_business_manage_messages: "Direktnachrichten lesen und beantworten",
  instagram_business_manage_insights: "Statistiken für die Lernschleife",
};

let blocker = 0;
const gut = (t) => console.log(`  ✓ ${t}`);
const warnung = (t) => console.log(`  · ${t}`);
const fehler = (t) => { console.log(`  ✗ ${t}`); blocker++; };

console.log(`Token-Prüfung · ${CONFIG.marke.name || "(ohne Markennamen)"} · ${new Date().toISOString().slice(0, 16).replace("T", " ")} UTC\n`);

const hosting = new Hosting({ pushen: false }).vorbereiten();
const ig = new Instagram({ trockenlauf: false, tresorDatei: path.join(hosting.stateDir, "token.enc") });
const ausTresor = ig.tresorLaden();

console.log("Herkunft");
if (!ig.token) { fehler("Kein Token vorhanden – weder im Tresor noch im Secret IG_ACCESS_TOKEN."); process.exit(1); }
gut(`Der Lauf arbeitet mit dem Token ${ausTresor ? "aus dem Tresor" : "aus dem Secret"}: ${kuerzel(ig.token)}`);
if (ausTresor) warnung(`Im Secret steht ${kuerzel(CONFIG.instagram.token)} – der Tresor stammt davon ab und wurde nur verlängert.`);
if (ig.tokenAblauf) gut(`Gültig bis ${ig.tokenAblauf.slice(0, 10)}`);

/* 1. Wem gehört der Token? ----------------------------------------------- */
console.log("\nKonto");
try {
  const me = await ig.anfrage("GET", "me", { fields: "id,user_id,username,account_type" });
  gut(`@${me.username || "?"} · id ${me.id} · Kontotyp ${me.account_type || "(nicht gemeldet)"}`);
  if (CONFIG.instagram.kontoId && String(CONFIG.instagram.kontoId) !== String(me.id) && String(CONFIG.instagram.kontoId) !== String(me.user_id)) {
    warnung(`IG_ACCOUNT_ID ist ${CONFIG.instagram.kontoId}, der Token gehört aber zu ${me.id}.`);
  }
} catch (e) { fehler(`Konto nicht abfragbar: ${e.message}`); }

/* 2. Welche Berechtigungen trägt der Token? ------------------------------
   debug_token beantwortet genau die Frage, um die es geht. Über
   graph.instagram.com ist der Aufruf nicht garantiert – schlägt er fehl,
   entscheiden unten die Kanten selbst. */
console.log("\nBerechtigungen");
let scopes = null;
try {
  const url = new URL(`${ig.basis}/debug_token`);
  url.searchParams.set("input_token", ig.token);
  url.searchParams.set("access_token", ig.token);
  const json = await (await fetch(url)).json();
  scopes = json?.data?.scopes || null;
  if (!scopes) warnung(`debug_token nennt keine Berechtigungen (${knapp(json, 300)}) – der Kantentest unten entscheidet.`);
} catch (e) { warnung(`debug_token nicht erreichbar (${e.message}) – der Kantentest unten entscheidet.`); }

if (scopes) {
  for (const [name, zweck] of Object.entries(NOETIG)) {
    if (scopes.includes(name)) gut(`${name} – ${zweck}`);
    else fehler(`${name} FEHLT – ${zweck} fällt aus.`);
  }
  const extra = scopes.filter((s) => !NOETIG[s]);
  if (extra.length) warnung(`Zusätzlich: ${extra.join(", ")}`);
}

/* 3. Der Kantentest: was kommt wirklich zurück? --------------------------
   Aussagekräftiger als jede Einstellungsseite. Eine Kante, die 200 mit leerer
   Liste zurückgibt, obwohl der Zähler etwas anderes sagt, ist der Beweis. */
console.log("\nKanten");
let medien = [];
try {
  const r = await ig.anfrage("GET", `${ig.kontoId || "me"}/media`, { fields: "id,comments_count,permalink", limit: 10 });
  medien = r.data || [];
  gut(`Medien lesen: ${medien.length} Beiträge (instagram_business_basic)`);
} catch (e) { fehler(`Medien lesen: ${e.message}`); }

const mitKommentaren = medien.filter((m) => (m.comments_count || 0) > 0);
if (!mitKommentaren.length) {
  warnung("Kein Beitrag meldet Kommentare – die Kommentarkante lässt sich gerade nicht prüfen. Schreib einen Testkommentar und starte erneut.");
} else {
  for (const m of mitKommentaren.slice(0, 3)) {
    try {
      const k = await ig.anfrage("GET", `${m.id}/comments`, { fields: "id,text,username,timestamp", limit: 50 });
      const n = (k.data || []).length;
      if (n) gut(`Kommentare zu ${m.id}: ${n} von ${m.comments_count} geliefert.`);
      else fehler(`Kommentare zu ${m.id}: comments_count=${m.comments_count}, geliefert 0. Rohantwort ${knapp(k)} – der Token trägt instagram_business_manage_comments nicht.`);
    } catch (e) { fehler(`Kommentare zu ${m.id}: ${e.message}`); }
  }
}

try {
  const c = await ig.anfrage("GET", `${ig.kontoId || "me"}/conversations`, { fields: "id,updated_time", limit: 10 });
  const n = (c.data || []).length;
  if (n) gut(`Unterhaltungen: ${n} (instagram_business_manage_messages)`);
  else warnung(`Unterhaltungen: 0. Rohantwort ${knapp(c)} – entweder wirklich leer oder instagram_business_manage_messages fehlt.`);
} catch (e) { fehler(`Unterhaltungen: ${e.message}`); }

try {
  const i = await ig.anfrage("GET", `${ig.kontoId || "me"}/insights`, { metric: "reach", period: "day" });
  gut(`Statistiken: ${(i.data || []).length} Kennzahl(en) (instagram_business_manage_insights)`);
} catch (e) { warnung(`Statistiken: ${e.message}`); }

/* 4. Was jetzt zu tun ist ------------------------------------------------- */
console.log("");
if (blocker) {
  console.log(`${blocker} Punkt(e) offen.

Ein Token trägt die Berechtigungen, die beim Erzeugen angehakt waren – nicht
die, die heute in den App-Einstellungen stehen. Ein nachträglich gesetzter
Schalter wirkt also erst auf einen NEU erzeugten Token.

  1. Meta-Dashboard → App → Instagram → API-Einrichtung mit Instagram-Login
  2. Bei „Zugriffstoken generieren“ alle fünf Berechtigungen anhaken
  3. Den erzeugten Token als Secret IG_ACCESS_TOKEN hinterlegen –
     nur dort, nicht im Chat
  4. Diese Prüfung erneut starten (Aktion „Instagram-Bot“, Modus „token“)

Der Tresor merkt am Fingerabdruck, dass das Secret neu ist, und führt sich von
dem neuen Token aus weiter. Es ist nichts zu löschen.`);
  process.exit(1);
}
console.log("Alles in Ordnung: Der Token trägt jede Berechtigung, die der Bot braucht.");
