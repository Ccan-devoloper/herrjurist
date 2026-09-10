/* ==========================================================================
   Faktencheck: ein zweiter, unabhängiger Aufruf prüft jeden Beitrag und
   jedes Reel-Skript auf fachliche Fehler (Normen, Fristen, Prozentsätze,
   Zuständigkeiten, Rechtsstand 2026). Nur klare Fehler führen zur
   Nachbesserung; Stilfragen nicht.
   ========================================================================== */

import Anthropic from "@anthropic-ai/sdk";
import { CONFIG } from "./config.mjs";
import { erfassen, budgetPruefen } from "./kosten.mjs";

let clientCache = null;
const client = () => (clientCache ||= new Anthropic({ maxRetries: 3, timeout: 5 * 60 * 1000 }));

const SCHEMA = {
  type: "object",
  additionalProperties: false,
  properties: {
    befunde: {
      type: "array",
      items: {
        type: "object",
        additionalProperties: false,
        properties: {
          schwere: { type: "string", enum: ["fehler", "unsicher", "hinweis"] },
          stelle: { type: "string" },
          problem: { type: "string" },
          korrektur: { type: "string" },
        },
        required: ["schwere", "stelle", "problem", "korrektur"],
      },
    },
  },
  required: ["befunde"],
};

const SYSTEM = `Du bist Prüfer:in für Fachtexte zum deutschen Steuerrecht (Steuerberaterexamen, Rechtsstand 2026). Du bekommst Texte eines Instagram-Kanals und prüfst ausschließlich die fachliche Richtigkeit:
- Normzitate (richtiges Gesetz, Paragraf, Absatz, Satz, Nummer), Richtlinien und Verwaltungsanweisungen
- Zahlen: Fristen, Prozentsätze, Freibeträge, Grenzen, Zinssätze
- Rechtsfolgen, Prüfungsreihenfolgen, Zuständigkeiten
- Rechtsstand: veraltete Regelungen (z. B. Abzinsung von Verbindlichkeiten, alte Freibeträge) sind Fehler
- Innere Logik: Der Text muss aus sich heraus verständlich sein. Wird auf einen Fall, einen Namen oder eine Zahl Bezug genommen, die nirgends im Text eingeführt wird (z. B. „Mini-Fall Nordlicht GmbH“ ohne Sachverhalt, eine Rechnung mit Zahlen, die vorher nicht genannt sind), ist das ein „fehler“ – mit dem Hinweis, welche Angaben ergänzt werden müssen.

Melde als „fehler“ nur, was eindeutig falsch ist und in der Prüfung Punkte kosten würde. Als „unsicher“ alles, was du nicht sicher beurteilen kannst. Als „hinweis“ Unschärfen, die vertretbar sind. Keine Stil- oder Formatkritik. Wenn alles korrekt ist, gib eine leere Liste zurück.`;

function textAus(beitrag) {
  const teile = [];
  for (const f of beitrag.folien || []) teile.push(`[Folie ${f.art}] ${[f.titel, f.untertitel, f.text, ...(f.punkte || []), ...(f.schritte || []).map((s) => (typeof s === "string" ? s : `${s.titel}: ${s.text || ""}`)), f.formel, ...(f.zeilen || []), f.ergebnis, f.links?.titel, ...(f.links?.punkte || []), f.rechts?.titel, ...(f.rechts?.punkte || [])].filter(Boolean).join(" · ")}`);
  for (const s of beitrag.szenen || []) teile.push(`[Szene ${s.art}] ${[s.titel, s.text, s.norm, s.sprecher].filter(Boolean).join(" · ")}`);
  if (beitrag.caption) teile.push(`[Caption] ${beitrag.caption}`);
  return teile.join("\n");
}

/**
 * @returns {{ok:boolean, fehler:string[], hinweise:string[]}}
 */
export async function pruefeFakten(beitrag, zweck = "faktencheck") {
  if (!CONFIG.faktencheck.aktiv) return { ok: true, fehler: [], hinweise: [] };
  budgetPruefen(zweck === "reel-faktencheck" ? "Reel-Faktencheck" : "Faktencheck");
  const modell = CONFIG.ki.modellPruefung || CONFIG.ki.modellNeben;
  const haiku = /haiku/i.test(modell);
  const user = `Prüfe diesen Text:\n\n${textAus(beitrag)}`;
  const basis = {
    model: modell,
    max_tokens: 6000,
    system: [{ type: "text", text: SYSTEM, cache_control: { type: "ephemeral" } }],
    messages: [{ role: "user", content: user }],
    /* Haiku kennt kein adaptives Denken – dort ohne. */
    ...(haiku ? {} : { thinking: { type: "adaptive" } }),
    output_config: { ...(haiku ? {} : { effort: "medium" }), format: { type: "json_schema", schema: SCHEMA } },
  };
  let response;
  try {
    response = await client().messages.create(basis);
  } catch (e) {
    if (!(e instanceof Anthropic.BadRequestError)) throw e;
    /* Rückfall: ohne Denken und ohne Schema-Format, JSON per Anweisung. */
    const { thinking, output_config, ...rest } = basis;
    response = await client().messages.create({ ...rest, messages: [{ role: "user", content: `${user}\n\nAntworte ausschließlich mit einem JSON-Objekt nach diesem Schema:\n${JSON.stringify(SCHEMA)}` }] });
  }
  erfassen(modell, response.usage, zweck);
  if (response.stop_reason === "refusal") return { ok: true, fehler: [], hinweise: [] };
  const text = response.content.filter((b) => b.type === "text").map((b) => b.text).join("");
  let daten;
  try { daten = JSON.parse(text.slice(text.indexOf("{"), text.lastIndexOf("}") + 1)); } catch { return { ok: true, fehler: [], hinweise: [] }; }
  /* Weiche Beanstandungen („irreführend“, „präzisieren“, „missverständlich“) sind
     keine Fehler, die eine teure Neufassung rechtfertigen – sie werden zu Hinweisen. */
  const WEICH = /irreführend|präzisier|missverständlich|ungenau|unscharf|unschärfe|ausdrucksweise|formulierung|konzeptionell|didaktisch|sollte (?:ergänzt|erwähnt|klargestellt)|könnte|empfehl|verkürzt|vereinfacht|mathematisch (?:richtig|korrekt)|ist (?:zwar |dann )?(?:sachlich )?korrekt/i;
  const ist = (b) => b.schwere === "fehler" && !WEICH.test(`${b.problem} ${b.korrektur}`);
  const fehler = daten.befunde.filter(ist).map((b) => `${b.stelle}: ${b.problem} → ${b.korrektur}`);
  const hinweise = daten.befunde.filter((b) => !ist(b)).map((b) => `${b.stelle}: ${b.problem}`);
  return { ok: fehler.length === 0, fehler, hinweise };
}
