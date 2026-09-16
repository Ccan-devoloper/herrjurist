#!/usr/bin/env node
/**
 * Wertet den Webhook-Mitschnitt aus: Was schickt Instagram bei einer
 * Story-Antwort wirklich?
 *
 * Kostet nichts - liest nur state/webhook-roh.jsonl und zählt aus. Die eine
 * Frage, um die es geht: Steht im EINGEHENDEN Ereignis eine Story-ID? Die
 * nachträgliche Abfrage über /conversations lieferte am 16.09. ein leeres
 * `reply_to.story`; ob das auch fürs Live-Ereignis gilt, sagt nur dieser
 * Mitschnitt.
 *
 * Aufruf: node bin/webhook-zeigen.mjs [pfad]
 */
import fs from "node:fs";
import path from "node:path";

const pfad = process.argv[2] || path.join(process.env.IG_STATE_DIR || "state", "webhook-roh.jsonl");
if (!fs.existsSync(pfad)) {
  console.log(`Kein Mitschnitt unter ${pfad}. Noch kein Ereignis angekommen – oder der Worker läuft nicht.`);
  process.exit(0);
}

const zeilen = fs.readFileSync(pfad, "utf8").split("\n").filter(Boolean);
console.log(`${zeilen.length} Ereignis(se) mitgeschnitten.\n`);

const zaehler = { gesamt: 0, mitStoryId: 0, mitStoryUrl: 0, storyLeer: 0, ohneReplyTo: 0, echo: 0 };
const beispiele = [];

for (const z of zeilen) {
  let eintrag;
  try { eintrag = JSON.parse(z); } catch { continue; }
  for (const e of eintrag.ereignis?.entry || []) {
    for (const ev of e.messaging || []) {
      const m = ev.message;
      if (!m) continue;
      if (m.is_echo) { zaehler.echo++; continue; }
      zaehler.gesamt++;
      const story = m.reply_to?.story ?? m.story ?? null;
      if (!m.reply_to && !m.story) zaehler.ohneReplyTo++;
      else if (story?.id) zaehler.mitStoryId++;
      else if (story?.url || story?.link) zaehler.mitStoryUrl++;
      else zaehler.storyLeer++;
      if (beispiele.length < 5) {
        beispiele.push({
          empfangen: eintrag.empfangen,
          text: String(m.text || "").slice(0, 70),
          /* Absichtlich nur die Struktur, nicht der ganze Rohtext: Es geht um
             die Frage, WELCHE Felder ankommen. */
          felder: Object.keys(m).join(", "),
          reply_to: m.reply_to ? JSON.stringify(m.reply_to).slice(0, 220) : "—",
          story: m.story ? JSON.stringify(m.story).slice(0, 220) : "—",
        });
      }
    }
  }
}

console.log("Eingehende Nachrichten (ohne Echos):", zaehler.gesamt);
console.log(`  mit Story-ID          : ${zaehler.mitStoryId}   ← das ist die Frage`);
console.log(`  nur Story-URL/Link    : ${zaehler.mitStoryUrl}`);
console.log(`  Story-Objekt leer     : ${zaehler.storyLeer}`);
console.log(`  ohne Story-Bezug      : ${zaehler.ohneReplyTo}`);
console.log(`  eigene Echos          : ${zaehler.echo}\n`);

for (const b of beispiele) {
  console.log(`— ${b.empfangen} · „${b.text}"`);
  console.log(`    Felder   : ${b.felder}`);
  console.log(`    reply_to : ${b.reply_to}`);
  console.log(`    story    : ${b.story}\n`);
}

if (zaehler.mitStoryId) {
  console.log("Befund: Das Live-Ereignis TRÄGT die Story-ID. Damit ist die Zuordnung");
  console.log("über den Webhook möglich - ohne Raten, ohne Zeitfenster.");
} else if (zaehler.gesamt) {
  console.log("Befund: Bisher kam keine Story-ID im Live-Ereignis an. Wichtig: Nur");
  console.log("aussagekräftig, wenn darunter eine ECHTE Story-Antwort war.");
}
