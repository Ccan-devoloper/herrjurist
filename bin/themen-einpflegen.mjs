#!/usr/bin/env node
/* ==========================================================================
   Neue Themen aus dem Staging in den verschlüsselten Themenpool übernehmen.

   node bin/themen-einpflegen.mjs pruefen      – zählt, was im Staging liegt
   node bin/themen-einpflegen.mjs uebernehmen  – Staging → themen.json.enc (Workflow)
   node bin/themen-einpflegen.mjs bericht      – druckt den Einpflege-Bericht (nur lokal)

   Gleiche Bauart wie bin/wissen-einpflegen.mjs: Wer die Themen vorbereitet,
   hat IG_WISSEN_KEY nicht und legt sie mit einem Transferschlüssel als
   daten/themen-neu.json.enc ab. Der Workflow "Themen einpflegen" kennt beide
   Secrets, prüft jeden Kandidaten und hängt ihn an den Pool an.

   Angehängt, nie einsortiert: Die Themen-IDs entstehen aus der Position im
   Pool (inhalte.mjs), und der Ledger merkt sich Themen über diese IDs.
   Ein Einschub in der Mitte würde alle Sperren dahinter verschieben.

   Dubletten: Der Bestand ist gegen ein ganzes Handbuch abgeglichen worden -
   fast alles Klassische ist schon da. Ein Kandidat mit gleichem Titel fliegt
   raus; ein sehr ähnlicher Titel im selben Fach ebenso. Die Grauzone wird
   aufgenommen, aber im Bericht zum Nachsehen markiert - ein grobes Maß, das
   still entscheidet, wäre gefährlicher als eines, das seine Zweifel nennt.

   Öffentliches Actions-Log: nur Zahlen und Fingerabdrücke, nie Titel.
   ========================================================================== */

import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { CONFIG } from "../src/config.mjs";
import { wissenVerschluesseln, wissenEntschluesseln, wissenIndex, wissenLeeren } from "../src/wissen.mjs";
import { FAECHER } from "../daten/gebiete.mjs";

const STAGING = path.resolve("daten/themen-neu.json.enc");
const POOL = path.resolve("daten/themen.json.enc");
const BERICHT = path.resolve("daten/themen-einpflegen-bericht.json.enc");
const TYPEN = new Set(["modul", "karteikarte", "quiz", "schema", "formel", "begriff"]);

const [, , befehl] = process.argv;
const geheim = CONFIG.wissen?.schluessel;
const transfer = process.env.WISSEN_TRANSFER_KEY || "";
const abdruck = (s) => (s ? crypto.createHash("sha256").update(String(s)).digest("hex").slice(0, 12) : "–");

/* Wortmengen-Ähnlichkeit für den Dublettenabgleich. Bewusst grob - sie
   entscheidet allein nur über nahezu identische Titel; alles darunter wird
   aufgenommen und im Bericht ausgewiesen. */
const STOPP = new Set(["und", "oder", "der", "die", "das", "wie", "was", "wann", "wer", "wem", "wen", "man", "ist", "sind", "wird", "für", "fuer", "nach", "aus", "als", "ein", "eine", "einen", "einem", "gilt", "gibt", "sich", "nicht", "kein", "keine", "ohne", "über", "ueber", "gegen", "zwischen", "beim", "trotz", "noch", "schon", "dann", "auch", "prüft", "prueft", "seine", "ihre", "dem", "den", "des", "bei", "mit", "von", "vom", "zum", "zur", "auf"]);
const woerter = (s) => new Set(String(s).toLowerCase().replace(/[§„“”"?,:;().–—/-]/g, " ").split(/\s+/)
  .filter((w) => w.length >= 4 && !STOPP.has(w)).map((w) => w.replace(/(en|er|es|em|e|s|n)$/, "")));
function aehnlichkeit(a, b) {
  const wa = woerter(a), wb = woerter(b);
  let beide = 0;
  for (const w of wa) if (wb.has(w)) beide++;
  return beide / (wa.size + wb.size - beide || 1);
}
const glatt = (s) => String(s || "").toLowerCase().replace(/\s+/g, " ").trim();

function stagingLesen() {
  if (!fs.existsSync(STAGING)) { console.error(`Staging fehlt: ${STAGING}`); process.exit(1); }
  if (!transfer) { console.error("WISSEN_TRANSFER_KEY fehlt."); process.exit(1); }
  let daten;
  try {
    daten = JSON.parse(wissenEntschluesseln(fs.readFileSync(STAGING), transfer));
  } catch {
    console.error(`Staging nicht lesbar (Transferschlüssel-Fingerabdruck ${abdruck(transfer)}).`);
    process.exit(1);
  }
  if (!Array.isArray(daten) || !daten.length) { console.error("Staging ist leer oder kein Array."); process.exit(1); }
  return daten;
}

function kandidatPruefen(t, ids) {
  const f = [];
  if (!FAECHER[t.fach]) f.push("unbekanntes Fach");
  if (!(typeof t.titel === "string" && t.titel.length >= 4 && t.titel.length <= 140)) f.push("Titel");
  if (/Originalfall|Hausaufgabe|Seite \d/i.test(t.titel || "")) f.push("Quellenbezug im Titel");
  if (!Array.isArray(t.normen)) f.push("Normen fehlen");
  else for (const n of t.normen) if (!(typeof n === "string" && n.length >= 2 && n.length <= 90)) f.push("Norm unbrauchbar");
  if (!["hoch", "mittel", "selten"].includes(t.prioritaet)) f.push("Priorität");
  if (t.typ && !TYPEN.has(t.typ)) f.push("Typ");
  if (t.kern?.facts !== undefined) f.push("kern.facts");
  if (t.wissen && !ids.has(t.wissen)) f.push(`Zeiger ${t.wissen} trifft kein Kapitel`);
  return f;
}

function pruefen() {
  const daten = stagingLesen();
  console.log(`${daten.length} Themen-Kandidaten im Staging · Transferschlüssel-Fingerabdruck ${abdruck(transfer)}`);
}

function uebernehmen() {
  if (!geheim) { console.error("IG_WISSEN_KEY fehlt."); process.exit(1); }
  const kandidaten = stagingLesen();
  if (!fs.existsSync(POOL)) { console.error("daten/themen.json.enc fehlt."); process.exit(1); }
  const pool = JSON.parse(wissenEntschluesseln(fs.readFileSync(POOL), geheim));
  if (!Array.isArray(pool) || pool.length < 300) { console.error(`Bestandspool unplausibel: ${pool?.length}`); process.exit(1); }

  wissenLeeren();
  const ids = new Set(wissenIndex({ geheim, neu: true }).map((k) => k.id));

  let fehler = 0;
  for (const t of kandidaten) {
    const f = kandidatPruefen(t, ids);
    if (f.length) { fehler++; console.error(`Kandidat ungültig (${f.join(", ")})`); }
  }
  if (fehler) { console.error(`${fehler} von ${kandidaten.length} Kandidaten ungültig – nichts übernommen.`); process.exit(1); }

  const vorher = pool.length;
  const titelDa = new Set(pool.map((t) => glatt(t.titel)));
  const aufgenommen = [], uebersprungen = [];
  for (const t of kandidaten) {
    let naechster = null, mass = 0;
    for (const alt of pool) {
      const j = aehnlichkeit(t.titel, alt.titel);
      if (j > mass) { mass = j; naechster = alt.titel; }
    }
    const eintrag = { fach: t.fach, titel: t.titel, wissen: t.wissen || null, naechster, mass: Number(mass.toFixed(2)) };
    if (titelDa.has(glatt(t.titel)) || mass >= 0.7) { uebersprungen.push(eintrag); continue; }
    if (mass >= 0.45) eintrag.pruefen = true;
    aufgenommen.push(eintrag);
    pool.push(t);
    titelDa.add(glatt(t.titel));
  }

  if (pool.length !== vorher + aufgenommen.length || aufgenommen.length + uebersprungen.length !== kandidaten.length) { console.error("Zählprobe fehlgeschlagen."); process.exit(1); }
  fs.writeFileSync(POOL, wissenVerschluesseln(JSON.stringify(pool), geheim));

  const bericht = { datum: new Date().toISOString(), vorher, nachher: pool.length, aufgenommen, uebersprungen };
  fs.writeFileSync(BERICHT, wissenVerschluesseln(JSON.stringify(bericht, null, 2), geheim));
  fs.unlinkSync(STAGING);

  const nachsehen = aufgenommen.filter((a) => a.pruefen).length;
  console.log(`Themenpool ${vorher} → ${pool.length}: ${aufgenommen.length} aufgenommen, ${uebersprungen.length} als Dublette übersprungen${nachsehen ? `, ${nachsehen} zum Nachsehen markiert` : ""}.`);
  console.log(`Schlüssel-Fingerabdruck ${abdruck(geheim)} · Details verschlüsselt in ${path.basename(BERICHT)} (lokal: node bin/themen-einpflegen.mjs bericht).`);
  console.log("Staging entfernt. Das Secret WISSEN_TRANSFER_KEY wird nicht mehr gebraucht und kann gelöscht werden.");
}

function berichtZeigen() {
  if (!geheim) { console.error("IG_WISSEN_KEY fehlt."); process.exit(1); }
  if (!fs.existsSync(BERICHT)) { console.error(`${BERICHT} fehlt.`); process.exit(1); }
  console.log(wissenEntschluesseln(fs.readFileSync(BERICHT), geheim));
}

if (befehl === "pruefen") pruefen();
else if (befehl === "uebernehmen") uebernehmen();
else if (befehl === "bericht") berichtZeigen();
else {
  console.log("Aufruf: node bin/themen-einpflegen.mjs pruefen|uebernehmen|bericht");
  process.exit(1);
}
