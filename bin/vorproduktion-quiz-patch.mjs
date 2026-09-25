#!/usr/bin/env node
/**
 * Frage-/Antwort-Stories der Vorproduktion auf das Quiz-System bringen:
 * Optionen und richtige Antwort aus vorproduktion/quiz-optionen.json in
 * frage und antwort eintragen und nur diese beiden Stories neu rendern.
 *
 * Kostenfrei: keine Autor-, Faktencheck- oder Bild-Aufrufe.
 */
import fs from "node:fs";
import path from "node:path";

for (const k of ["OPENAI_API_KEY", "ANTHROPIC_API_KEY", "ELEVENLABS_API_KEY", "PEXELS_API_KEY"]) {
  if (String(process.env[k] || "").trim()) throw new Error(`${k} muss leer sein`);
}

const { Hosting } = await import("../src/hosting.mjs");
const { storyRendern, browserBeenden } = await import("../src/render.mjs");
const { quizPruefen } = await import("./vorproduktion-quiz-regel.mjs");

const patch = JSON.parse(fs.readFileSync(new URL("../vorproduktion/quiz-optionen.json", import.meta.url), "utf8"));
const host = new Hosting({ pushen: true }).vorbereiten();
const erledigt = [];

try {
  for (const [datum, quiz] of Object.entries(patch.tage)) {
    const tagPfad = path.join(host.dir, "vorproduktion", `${datum}.json`);
    if (!fs.existsSync(tagPfad)) throw new Error(`Vorproduktion fehlt: ${datum}`);
    const tag = JSON.parse(fs.readFileSync(tagPfad, "utf8"));
    const slots = (tag.plan?.stories || []).filter((s) => s.art === "frage" || s.art === "antwort");
    if (slots.length !== 2) throw new Error(`${datum}: erwartet genau ein Frage-/Antwort-Paar`);
    for (const s of slots) {
      const story = tag.inhalte?.[s.slot];
      if (!story) throw new Error(`${datum} ${s.slot}: Story fehlt`);
      story.optionen = [...quiz.optionen];
      story.richtig = quiz.richtig;
    }
    quizPruefen(tag, datum);
    const dir = path.join(host.dir, tag.renderVorschau?.pfad || `vorproduktion/${datum}/fertig`, "stories");
    fs.mkdirSync(dir, { recursive: true });
    for (const s of slots) {
      const story = structuredClone(tag.inhalte[s.slot]);
      story.bild = null;
      story.bildQuelle = null;
      await storyRendern(story, path.join(dir, `${s.slot}-${story.art}.jpg`), { variante: 0 });
    }
    tag.renderVorschau = { ...(tag.renderVorschau || {}), quizPatch: { stand: new Date().toISOString(), slots: slots.map((s) => s.slot), providerKostenUsd: 0 } };
    fs.writeFileSync(tagPfad, JSON.stringify(tag, null, 2) + "\n");
    erledigt.push(datum);
    console.log(`${datum}: Quiz ${slots.map((s) => s.slot).join("+")} neu gerendert`);
  }
  host.commit(`Frage-/Antwort-Stories ${erledigt[0]} bis ${erledigt.at(-1)} auf Quiz-System bringen`);
  await host.push();
} finally {
  await browserBeenden().catch(() => {});
}
console.log("0,00 USD Providerkosten.");
