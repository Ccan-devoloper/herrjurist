#!/usr/bin/env node
/* ==========================================================================
   Neue Wissensbände aus dem Staging in den Tresor übernehmen.

   node bin/wissen-einpflegen.mjs pruefen      – zählt, was im Staging liegt
   node bin/wissen-einpflegen.mjs uebernehmen  – Staging → daten/wissen (Workflow)
   node bin/wissen-einpflegen.mjs bericht      – druckt den Einpflege-Bericht (nur lokal)

   Warum ein zweiter Schlüssel: Wer die Bände vorbereitet (z. B. eine
   Claude-Session), hat IG_WISSEN_KEY nicht – der Schlüssel liegt nur in den
   GitHub-Secrets. Damit trotzdem nie Klartext ins Repository gelangt, werden
   die neuen Bände mit einem frei gewählten TRANSFERSCHLÜSSEL verschlüsselt
   nach daten/wissen-neu/ gelegt. Der Workflow "Wissen einpflegen" kennt
   beide Secrets, schlüsselt um, richtet die Themen-Zeiger und räumt das
   Staging weg. Danach kann das Secret WISSEN_TRANSFER_KEY gelöscht werden.

   Die Themen-Zeiger (`wissen: "4/2"`) zeigen auf Band/Kapitelnummer. Nach
   einem Bände-Update wird jeder Zeiger geprüft: Trägt das Kapitel noch
   seinen Titel, bleibt er; ist das Kapitel unter neuer Nummer auffindbar,
   wird er umgeschrieben; sonst wird er gestrichen, und das Thema fällt auf
   die Wortsuche zurück – ein stiller Zeiger auf das falsche Kapitel wäre
   die schlechteste aller Varianten.

   Dieses Skript läuft in einem öffentlichen Actions-Log. Es gibt deshalb
   nur Zahlen und Schlüssel-Fingerabdrücke aus, nie Titel oder Text. Der
   volle Bericht (welche Zeiger wohin) liegt verschlüsselt in
   daten/wissen-einpflegen-bericht.json.enc und lässt sich lokal mit
   `bericht` lesen.
   ========================================================================== */

import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { CONFIG } from "../src/config.mjs";
import { WISSEN_ORDNER, wissenVerschluesseln, wissenEntschluesseln, wissenIndex, wissenLeeren } from "../src/wissen.mjs";

const STAGING = path.resolve("daten/wissen-neu");
const THEMEN_ENC = path.resolve("daten/themen.json.enc");
const BERICHT_ENC = path.resolve("daten/wissen-einpflegen-bericht.json.enc");

const [, , befehl] = process.argv;
const geheim = CONFIG.wissen?.schluessel;
const transfer = process.env.WISSEN_TRANSFER_KEY || "";
const abdruck = (s) => (s ? crypto.createHash("sha256").update(String(s)).digest("hex").slice(0, 12) : "–");
const norm = (s) => String(s || "").toLowerCase().replace(/\s+/g, " ").trim();

function stagingLesen() {
  if (!fs.existsSync(STAGING)) { console.error(`Staging fehlt: ${STAGING}`); process.exit(1); }
  const dateien = fs.readdirSync(STAGING).filter((d) => d.endsWith(".txt.enc")).sort();
  if (!dateien.length) { console.error("Keine *.txt.enc im Staging."); process.exit(1); }
  if (!transfer) { console.error("WISSEN_TRANSFER_KEY fehlt."); process.exit(1); }
  const baende = [];
  for (const datei of dateien) {
    let text;
    try {
      text = wissenEntschluesseln(fs.readFileSync(path.join(STAGING, datei)), transfer);
    } catch {
      console.error(`${datei}: Transferschlüssel passt nicht (Fingerabdruck ${abdruck(transfer)}).`);
      process.exit(1);
    }
    baende.push({ datei, text, nr: Number(/band-(\d+)/.exec(datei)?.[1] || 0) });
  }
  return baende;
}

function pruefen() {
  const baende = stagingLesen();
  wissenLeeren();
  const index = wissenIndex({ geheim: transfer, ordner: STAGING, neu: true });
  wissenLeeren();
  const zeichen = baende.reduce((a, b) => a + b.text.length, 0);
  console.log(`${baende.length} Bände, ${index.length} Kapitel, ${(zeichen / 1024 / 1024).toFixed(2)} MB Klartext im Staging.`);
  console.log(`Transferschlüssel-Fingerabdruck: ${abdruck(transfer)}`);
}

function uebernehmen() {
  if (!geheim) { console.error("IG_WISSEN_KEY fehlt."); process.exit(1); }
  const baende = stagingLesen();

  /* Alten Stand einlesen, solange er noch da ist: Er liefert die Titel, an
     denen sich verschobene Kapitel wiederfinden lassen. Ohne Schlüssel oder
     ohne alte Bände ist die Liste leer und jeder Zeiger wird streng geprüft. */
  wissenLeeren();
  const altIndex = fs.existsSync(WISSEN_ORDNER) ? wissenIndex({ geheim, neu: true }) : [];
  const altKapitel = new Map(altIndex.map((k) => [k.id, k.titel]));
  const altBaende = new Set(altIndex.map((k) => k.band));

  /* Kein Band darf still verschwinden, und schrumpfen darf der Bestand auch
     nicht: Beides wäre ein halb geladenes Staging, kein Update. */
  const neuBaende = new Set(baende.map((b) => b.nr));
  const fehlend = [...altBaende].filter((b) => !neuBaende.has(b));
  if (fehlend.length) { console.error(`Staging deckt Bände nicht ab: ${fehlend.join(", ")}`); process.exit(1); }

  fs.mkdirSync(WISSEN_ORDNER, { recursive: true });
  const neuNamen = new Set(baende.map((b) => b.datei));
  for (const b of baende) fs.writeFileSync(path.join(WISSEN_ORDNER, b.datei), wissenVerschluesseln(b.text, geheim));
  for (const alt of fs.readdirSync(WISSEN_ORDNER).filter((d) => d.endsWith(".txt.enc"))) {
    if (!neuNamen.has(alt)) fs.unlinkSync(path.join(WISSEN_ORDNER, alt));
  }

  /* Zurücklesen, was gerade geschrieben wurde – erst der eigene Schlüssel
     beweist, dass der Tresor wieder aufgeht. */
  wissenLeeren();
  const index = wissenIndex({ geheim, neu: true });
  if (index.length < altIndex.length) { console.error(`Neuer Index kleiner als alter (${index.length} < ${altIndex.length}).`); process.exit(1); }
  const kapitel = new Map(index.map((k) => [k.id, k]));
  /* Wiederfinden über den Titel: erst im selben Band, dann im ganzen Werk –
     "Versäumnisurteil" gibt es im Assessorband und im Seitenaudit, gewandert
     ist aber das Kapitel im eigenen Band. null heißt mehrdeutig. */
  const nachTitel = new Map(), nachBandTitel = new Map();
  for (const k of index) {
    const t = norm(k.titel), bt = `${k.band}|${t}`;
    nachTitel.set(t, nachTitel.has(t) ? null : k.id);
    nachBandTitel.set(bt, nachBandTitel.has(bt) ? null : k.id);
  }

  /* Themen-Zeiger richten. */
  const zeiger = { behalten: 0, umgeschrieben: [], gestrichen: [] };
  let themenAnzahl = 0;
  if (fs.existsSync(THEMEN_ENC)) {
    const themen = JSON.parse(wissenEntschluesseln(fs.readFileSync(THEMEN_ENC), geheim));
    themenAnzahl = themen.length;
    let geaendert = false;
    for (const thema of themen) {
      if (!thema.wissen) continue;
      const altTitel = altKapitel.get(thema.wissen);
      const neues = kapitel.get(thema.wissen);
      if (neues && (!altTitel || norm(neues.titel) === norm(altTitel))) { zeiger.behalten += 1; continue; }
      const band = Number(String(thema.wissen).split("/")[0]);
      const ersatz = altTitel ? (nachBandTitel.get(`${band}|${norm(altTitel)}`) || nachTitel.get(norm(altTitel))) : null;
      if (ersatz) {
        zeiger.umgeschrieben.push({ thema: thema.titel, von: thema.wissen, nach: ersatz });
        thema.wissen = ersatz; geaendert = true; continue;
      }
      if (neues) { zeiger.behalten += 1; continue; } /* Nummer da, alter Titel unbekannt: gelten lassen */
      zeiger.gestrichen.push({ thema: thema.titel, zeiger: thema.wissen });
      delete thema.wissen; geaendert = true;
    }
    for (const thema of themen) {
      if (thema.wissen && !kapitel.has(thema.wissen)) { console.error(`Zeiger zeigt ins Leere: ${thema.wissen}`); process.exit(1); }
    }
    if (geaendert) fs.writeFileSync(THEMEN_ENC, wissenVerschluesseln(JSON.stringify(themen), geheim));
  }

  const bericht = {
    datum: new Date().toISOString(),
    baende: baende.map((b) => ({ datei: b.datei, zeichen: b.text.length, kapitel: index.filter((k) => k.band === b.nr).length })),
    kapitelGesamt: index.length,
    zeichenGesamt: baende.reduce((a, b) => a + b.text.length, 0),
    zeiger,
  };
  fs.writeFileSync(BERICHT_ENC, wissenVerschluesseln(JSON.stringify(bericht, null, 2), geheim));

  fs.rmSync(STAGING, { recursive: true, force: true });

  console.log(`${baende.length} Bände mit ${index.length} Kapiteln übernommen (vorher ${altBaende.size} Bände, ${altIndex.length} Kapitel).`);
  console.log(`Themen: ${themenAnzahl} · Zeiger behalten ${zeiger.behalten}, umgeschrieben ${zeiger.umgeschrieben.length}, gestrichen ${zeiger.gestrichen.length}.`);
  console.log(`Schlüssel-Fingerabdruck ${abdruck(geheim)} · Details verschlüsselt in ${path.basename(BERICHT_ENC)} (lokal: node bin/wissen-einpflegen.mjs bericht).`);
  console.log("Staging entfernt. Das Secret WISSEN_TRANSFER_KEY wird nicht mehr gebraucht und kann gelöscht werden.");
}

function berichtZeigen() {
  if (!geheim) { console.error("IG_WISSEN_KEY fehlt."); process.exit(1); }
  if (!fs.existsSync(BERICHT_ENC)) { console.error(`${BERICHT_ENC} fehlt.`); process.exit(1); }
  console.log(wissenEntschluesseln(fs.readFileSync(BERICHT_ENC), geheim));
}

if (befehl === "pruefen") pruefen();
else if (befehl === "uebernehmen") uebernehmen();
else if (befehl === "bericht") berichtZeigen();
else {
  console.log("Aufruf: node bin/wissen-einpflegen.mjs pruefen|uebernehmen|bericht");
  process.exit(1);
}
