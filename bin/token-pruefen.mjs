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

/* Erster Weg: das App-Token aus App-ID und App-Geheimnis. Nur so nennt
   debug_token die Berechtigungen wirklich beim Namen. Der Aufruf geht an
   graph.facebook.com - über graph.instagram.com antwortet er mit
   "Application does not have permission for this action". */
const { appId, appGeheim } = CONFIG.instagram;
if (appId && appGeheim) {
  try {
    const url = new URL("https://graph.facebook.com/v23.0/debug_token");
    url.searchParams.set("input_token", ig.token);
    url.searchParams.set("access_token", `${appId}|${appGeheim}`);
    const json = await (await fetch(url)).json();
    scopes = json?.data?.scopes || null;
    if (scopes) gut(`debug_token nennt ${scopes.length} Berechtigung(en) am Token.`);
    else warnung(`debug_token mit App-Token liefert keine Liste: ${knapp(json, 300)}`);
  } catch (e) { warnung(`debug_token nicht erreichbar (${e.message}).`); }
} else {
  warnung("IG_APP_ID und IG_APP_SECRET sind nicht gesetzt – ohne sie lassen sich die Berechtigungen am Token nicht ablesen, nur erraten. Beide stehen im Meta-Dashboard unter App-Einstellungen → Allgemein und gehören als Secrets ins Repo.");
}

/* Zweiter Weg, falls das App-Token fehlt: derselbe Aufruf mit dem Token als
   eigenem Prüfer. Über graph.instagram.com schlägt er meist fehl - der
   Versuch kostet aber nichts. */
if (!scopes) {
  try {
    const url = new URL(`${ig.basis}/debug_token`);
    url.searchParams.set("input_token", ig.token);
    url.searchParams.set("access_token", ig.token);
    const json = await (await fetch(url)).json();
    scopes = json?.data?.scopes || null;
    if (!scopes) warnung(`Auch ohne App-Token nennt debug_token nichts (${knapp(json, 200)}) – der Kantentest unten entscheidet.`);
  } catch (e) { warnung(`debug_token nicht erreichbar (${e.message}) – der Kantentest unten entscheidet.`); }
}

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
      if (n) { gut(`Kommentare zu ${m.id}: ${n} von ${m.comments_count} geliefert.`); continue; }
      /* Leer mit Cursorn heißt: gefunden und beim Ausliefern aussortiert.
         Eine Kante, die nichts kennt, liefert keine Cursor. */
      const cursor = k.paging?.cursors?.after ? " (mit Cursor – die Kante kennt Einträge und liefert sie nicht)" : "";
      fehler(`Kommentare zu ${m.id}: comments_count=${m.comments_count}, geliefert 0${cursor}. Rohantwort ${knapp(k)}`);
      const knoten = await ig.anfrage("GET", `${m.id}`, { fields: "comments_count,comments{id,text,username,timestamp}" });
      const ueber = knoten.comments?.data || [];
      if (ueber.length) warnung(`Über den Medienknoten kommen ${ueber.length} Kommentare an – die Kante /comments ist der Fehler, nicht der Token.`);
      else warnung(`Auch der Medienknoten liefert nichts: ${knapp(knoten, 300)}`);
    } catch (e) { fehler(`Kommentare zu ${m.id}: ${e.message}`); }
  }
}

try {
  /* Über alle Seiten: Die erste Seite kann leer sein und trotzdem eine
     weitere ankündigen – genau das war am 15.09. der Fall. */
  const alle = await ig.alleSeiten(`${ig.kontoId || "me"}/conversations`, { platform: "instagram", fields: "id,updated_time", limit: 10 });
  if (alle.length) gut(`Unterhaltungen: ${alle.length} über alle Seiten (instagram_business_manage_messages)`);
  else warnung("Unterhaltungen: 0, auch über alle Seiten. Entweder hat wirklich niemand geschrieben, oder instagram_business_manage_messages fehlt.");
} catch (e) { fehler(`Unterhaltungen: ${e.message}`); }

try {
  const i = await ig.anfrage("GET", `${ig.kontoId || "me"}/insights`, { metric: "reach", period: "day" });
  gut(`Statistiken: ${(i.data || []).length} Kennzahl(en) (instagram_business_manage_insights)`);
} catch (e) { warnung(`Statistiken: ${e.message}`); }

/* 4. Was jetzt zu tun ist ------------------------------------------------- */
console.log("");
if (blocker) {
  console.log(`${blocker} Punkt(e) offen.

Ob es am Token liegt, sagen die Zeilen oben – nicht diese Anleitung:

  · Meldet eine Kante einen Fehler oder nennt debug_token die Berechtigung
    nicht, fehlt sie am Token. Dann hilft ein neuer Token (unten).
  · Kommt 200 mit leerer Liste UND einem Cursor zurück, während andere
    Kanten derselben Berechtigungsstufe liefern, liegt es nicht am Token.
    Dann ist die Abfrage dran, nicht das Meta-Dashboard.

Falls ein neuer Token nötig ist: Ein Token trägt die Berechtigungen, die beim
Erzeugen angehakt waren – ein nachträglich gesetzter Schalter wirkt erst auf
einen NEU erzeugten Token.

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
