#!/usr/bin/env node
/**
 * Stellt Prüfer an denselben Text und misst, was sie finden und was sie kosten.
 *
 * Anlass: Am 18.09. sollte der Faktencheck zu OpenAI wechseln, weil das
 * „gründlicher und günstiger" sei. Beides ist prüfbar, und genau das Nicht-
 * Prüfen einer solchen Annahme hat am Tag zuvor den Kanal gekostet. Hier
 * laufen die Modelle gegen einen Text mit einem BEKANNTEN Fehler, der am
 * 16.09. durch die Prüfung gerutscht ist: Bei § 1365 BGB muss der
 * VERTRAGSPARTNER wissen, dass es um das ganze Vermögen geht - nicht der
 * andere Ehegatte.
 *
 * Aufruf (ein Anbieter je Prozess, weil die Konfiguration beim Laden gilt):
 *   IG_FAKTENCHECK_ANBIETER=openai IG_FAKTENCHECK_OPENAI_MODELL=gpt-5-mini \
 *     node bin/pruefer-probe.mjs
 *   IG_FAKTENCHECK_ANBIETER=claude node bin/pruefer-probe.mjs
 */
process.env.IG_FAKTENCHECK_ZWEITMEINUNG ||= "false";

const { pruefeFakten } = await import("../src/faktencheck.mjs");
const { summe, jeZweck } = await import("../src/kosten.mjs");

/* Zwei Texte: einer mit bekanntem Fehler, einer ohne. Ein Prüfer, der alles
   beanstandet, ist so unbrauchbar wie einer, der nichts findet - die zweite
   Probe misst die Fehlalarme. */
const MIT_FEHLER = {
  folien: [
    { art: "titel", titel: "Verfügung über das ganze Vermögen", untertitel: "§ 1365 BGB in der Klausur" },
    { art: "text", titel: "Der Grundsatz", text: "Verfügt ein Ehegatte im gesetzlichen Güterstand über sein ganzes Vermögen, braucht er die Einwilligung des anderen Ehegatten. Ohne sie ist der Vertrag schwebend unwirksam." },
    { art: "text", titel: "Die subjektive Seite", text: "Die Rechtsprechung verlangt zusätzlich, dass der andere Ehegatte weiß oder wissen musste, dass es sich um das ganze Vermögen handelt." },
  ],
  caption: "Die Einzeltheorie fragt, ob der Gegenstand nahezu das ganze Vermögen ausmacht.",
  kurztitel: "Das ganze Vermögen?",
};
const OHNE_FEHLER = {
  folien: [
    { art: "titel", titel: "Der Rücktritt vom Versuch", untertitel: "§ 24 Abs. 1 StGB" },
    { art: "text", titel: "Unbeendeter Versuch", text: "Beim unbeendeten Versuch genügt es, dass der Täter die weitere Ausführung der Tat aufgibt (§ 24 Abs. 1 Satz 1 Alt. 1 StGB)." },
    { art: "text", titel: "Beendeter Versuch", text: "Beim beendeten Versuch muss der Täter die Vollendung verhindern (§ 24 Abs. 1 Satz 1 Alt. 2 StGB). Maßgeblich ist der Rücktrittshorizont nach Abschluss der letzten Ausführungshandlung." },
  ],
  caption: "Freiwillig ist der Rücktritt, wenn der Täter Herr seiner Entschlüsse bleibt.",
  kurztitel: "Rücktritt: aufgeben oder verhindern?",
};

const anbieter = process.env.IG_FAKTENCHECK_ANBIETER || "claude";
const modell = anbieter === "openai" ? (process.env.IG_FAKTENCHECK_OPENAI_MODELL || "gpt-5-mini") : (process.env.IG_KI_MODELL_PRUEFUNG_STRENG || "claude-sonnet-5");
console.log(`\n=== Prüfer: ${anbieter} · ${modell} ===`);

const zeigen = (name, e, ms) => {
  console.log(`\n--- ${name} (${(ms / 1000).toFixed(1)} s) ---`);
  console.log(`  ok: ${e.ok}`);
  for (const f of e.fehler) console.log(`  FEHLER  ${f}`);
  for (const h of e.hinweise) console.log(`  hinweis ${h}`);
  for (const k of e.korrekturen || []) console.log(`  sprache „${k.original}" → „${k.ersatz}"`);
};

let t = Date.now();
const a = await pruefeFakten(MIT_FEHLER, "faktencheck");
zeigen("Text MIT bekanntem Fehler (§ 1365 BGB: Kenntnis des Vertragspartners)", a, Date.now() - t);
/* Der Fund zählt nur, wenn er die richtige Person benennt. */
const alles = [...a.fehler, ...a.hinweise].join(" ");
const erkannt = /vertragspartner|vertragsgegner|geschäftspartner|erwerber|gegenüber/i.test(alles);
console.log(`\n  >>> Bekannter Fehler erkannt: ${erkannt ? "JA" : "NEIN"}`);

t = Date.now();
const b = await pruefeFakten(OHNE_FEHLER, "faktencheck");
zeigen("Text OHNE bekannten Fehler (§ 24 StGB)", b, Date.now() - t);
console.log(`\n  >>> Fehlalarme: ${b.fehler.length}`);

console.log(`\n=== Kosten ${anbieter} · ${modell}: ${summe().toFixed(4)} $ für 2 Prüfungen ===`);
console.log(`    ${JSON.stringify(jeZweck())}\n`);
