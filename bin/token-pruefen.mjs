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
  /* Meta antwortet auf diesen Aufruf gern mit "(#2) Service temporarily
     unavailable". Das Feld is_transient sagt selbst, dass es vorübergeht -
     also warten und erneut fragen, statt daraus einen Befund zu machen. */
  for (let versuch = 1; versuch <= 4 && !scopes; versuch++) {
    try {
      const url = new URL("https://graph.facebook.com/v23.0/debug_token");
      url.searchParams.set("input_token", ig.token);
      url.searchParams.set("access_token", `${appId}|${appGeheim}`);
      const json = await (await fetch(url)).json();
      scopes = json?.data?.scopes || null;
      if (scopes) { gut(`debug_token nennt ${scopes.length} Berechtigung(en) am Token.`); break; }
      if (json?.error?.is_transient && versuch < 4) {
        console.log(`  · debug_token: ${json.error.message} – erneut in ${3 * versuch} s (${versuch}/3)`);
        await new Promise((r) => setTimeout(r, 3000 * versuch));
        continue;
      }
      warnung(`debug_token mit App-Token liefert keine Liste: ${knapp(json, 300)}`);
      break;
    } catch (e) { warnung(`debug_token nicht erreichbar (${e.message}).`); break; }
  }
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
  /* ALLE Beiträge, nicht die neuesten N.

     Erst waren es zehn, dann 25 - und beide Male hätte ein Kommentar auf
     einem älteren Beitrag unbemerkt bleiben können. Genau das ist am
     15.09. passiert: Die Testkommentare standen auf älteren Beiträgen, und
     ich habe daraus voreilig geschlossen, die API halte sie zurück.

     Die Medienliste selbst ist billig - 50 Einträge je Aufruf. Teuer wäre
     erst, jeden Beitrag einzeln nach Kommentaren zu fragen; das bleibt
     deshalb unten auf die beschränkt, die überhaupt einen Zähler melden,
     und ist zusätzlich gedeckelt. Das Stundenlimit der App liegt bei rund
     200 Aufrufen, und das Veröffentlichen hat Vorrang. */
  medien = await ig.alleSeiten(`${ig.kontoId || "me"}/media`, { fields: "id,comments_count,permalink,timestamp", limit: 50 }, { maxSeiten: 12 });
  gut(`Medien lesen: ${medien.length} Beiträge (instagram_business_basic)`);
} catch (e) { fehler(`Medien lesen: ${e.message}`); }

/* JEDEN Beitrag fragen, nicht nur die mit comments_count > 0.

   Am 15.09. hat mich genau diese Abkürzung blind gemacht: Die Prüfung sah
   nur Beiträge, deren Zähler etwas meldete, und übersah damit zwei frisch
   geschriebene Kommentare. Der Zähler aus /media steht seit Stunden
   unverändert auf 1 und 2 - über hinzugefügte und wieder gelöschte
   Kommentare hinweg. Er ist also zwischengespeichert und taugt nicht als
   Vorfilter. Die Kante selbst ist die Quelle, nicht der Zähler. */
const MAX_ABFRAGEN = 60;
const zuPruefen = medien.filter((m) => (m.comments_count || 0) > 0).slice(0, MAX_ABFRAGEN);
const uebersprungen = medien.filter((m) => (m.comments_count || 0) > 0).length - zuPruefen.length;
gut(`${medien.length} Beiträge insgesamt, davon ${zuPruefen.length + uebersprungen} mit Zählerstand${uebersprungen ? ` (die ersten ${MAX_ABFRAGEN} werden gefragt)` : ""}.`);
let gefunden = 0, gezaehlt = 0, stumm = 0;
for (const m of zuPruefen) {
  try {
    const k = await ig.anfrage("GET", `${m.id}/comments`, { fields: "id,text,username,timestamp", limit: 50 });
    const n = (k.data || []).length;
    const zaehler = m.comments_count || 0;
    gefunden += n;
    gezaehlt += zaehler;
    if (n) {
      gut(`Kommentare zu ${m.id}: ${n} geliefert (Zähler sagt ${zaehler}).`);
      gut(`    ${m.permalink || "(ohne Link)"}`);
      for (const c of k.data.slice(0, 3)) gut(`    @${c.username || "?"}: ${String(c.text || "").slice(0, 60)}`);
    } else if (zaehler) {
      stumm++;
      const cursor = k.paging?.cursors?.after ? ", mit Cursor" : "";
      warnung(`Kommentare zu ${m.id}: Zähler ${zaehler}, geliefert 0${cursor}.`);
    }
  } catch (e) { fehler(`Kommentare zu ${m.id}: ${e.message}`); }
}
if (gefunden) gut(`Kommentare gesamt: ${gefunden} geliefert über ${medien.length} Beiträge (Zählerstand zusammen ${gezaehlt}).`);
else if (gezaehlt) fehler(`Kein einziger Kommentar geliefert, obwohl die Zähler zusammen ${gezaehlt} melden (${stumm} stumme Beiträge von ${medien.length} geprüften).`);
else warnung(`Kein Beitrag meldet Kommentare (${medien.length} geprüft) – schreib einen Testkommentar und starte erneut.`);

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
