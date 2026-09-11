/* ==========================================================================
   Faktencheck: ein zweiter, unabhängiger Aufruf prüft jeden Beitrag und
   jedes Reel-Skript auf fachliche Fehler – Normzitate, Prüfungsaufbau,
   Streitstände, Definitionen, Fristen, Zuständigkeiten, Rechtsstand 2026.
   Nur klare Fehler führen zur Nachbesserung; Stilfragen nicht, und auch
   nicht, dass eine vertretbare Ansicht vertreten wird.
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
          schwere: { type: "string", enum: ["fehler", "unsicher", "hinweis", "sprache"] },
          stelle: { type: "string" },
          problem: { type: "string" },
          korrektur: { type: "string" },
          /* Nur bei „sprache“: die fehlerhafte Wortfolge genau so, wie sie im
             Text steht, und die berichtigte Fassung. Damit lässt sich der
             Fehler ohne Neufassung im Text ersetzen. */
          original: { type: "string" },
          ersatz: { type: "string" },
        },
        required: ["schwere", "stelle", "problem", "korrektur", "original", "ersatz"],
      },
    },
  },
  required: ["befunde"],
};

const SYSTEM = `Du bist Prüfer:in für juristische Fachtexte (erstes und zweites juristisches Staatsexamen, deutsches Recht, Rechtsstand 2026). Du bekommst Texte eines Instagram-Kanals und prüfst ausschließlich die fachliche Richtigkeit:
- Normzitate: richtiges Gesetz, Paragraf, Absatz, Satz, Nummer, Buchstabe. Ein falscher Absatz ist ein Fehler, auch wenn die Aussage stimmt.
- Ob die genannte Norm die Aussage überhaupt trägt: Wird § 823 Abs. 1 BGB für etwas zitiert, das aus § 823 Abs. 2 BGB folgt, ist das ein Fehler.
- Prüfungsaufbau und Reihenfolge: Tatbestand vor Rechtswidrigkeit vor Schuld; Zulässigkeit vor Begründetheit; Anspruch entstanden, nicht erloschen, durchsetzbar.
- Streitstände: Wird eine Ansicht der Rechtsprechung oder der Literatur zugeschrieben, muss die Zuordnung stimmen. Wird ein Streit als entschieden dargestellt, der offen ist (oder umgekehrt), ist das ein Fehler. Fehlt bei einem Streit der Streitentscheid, ist das ein Hinweis.
- Definitionen: Die gängige Definition muss vollständig sein – fehlt ein Merkmal, kostet das in der Klausur Punkte.
- Fristen, Zahlen, Schwellenwerte und Zuständigkeiten (Instanzenzug, Gerichtsbarkeit, sachliche und örtliche Zuständigkeit).
- Rechtsstand: aufgehobene oder geänderte Normen sind Fehler (z. B. die GbR nach dem MoPeG, das Schuldrecht nach der Warenkaufrichtlinie).
- Landesrecht: Polizei-, Kommunal- und Bauordnungsrecht unterscheiden sich je Bundesland. Wird ein Landesparagraf als bundesweit gültig ausgegeben, ist das ein Fehler; fehlt der Hinweis auf die Landesabhängigkeit, ist es ein Hinweis.
- Innere Logik: Der Text muss aus sich heraus verständlich sein. Wird auf einen Fall, eine Person oder eine Zahl Bezug genommen, die nirgends eingeführt wird, ist das ein „fehler“ – mit dem Hinweis, welche Angaben fehlen.

Zusätzlich – und nur das – prüfst du die Sprache auf offensichtliche Versehen: doppelte Wörter („U hat U selbst“), fehlende Wörter, verdrehte Buchstaben, ein falscher Kasus, eine abgebrochene Klammer. Melde solche Versehen als „sprache“ und gib in „original“ die fehlerhafte Wortfolge exakt so an, wie sie im Text steht (mindestens drei Wörter, damit die Stelle eindeutig ist), in „ersatz“ die berichtigte Fassung mit denselben Wörtern drumherum. Stilfragen, Umformulierungen und Kürzungen sind keine Sprachversehen – nur, was ein Korrektor mit dem Rotstift anstreichen würde. Bei allen anderen Befunden bleiben „original“ und „ersatz“ leer.

Melde als „fehler“ nur, was eindeutig falsch ist und in der Klausur Punkte kosten würde. Als „unsicher“ alles, was du nicht sicher beurteilen kannst – gerade bei Streitständen und Landesrecht lieber „unsicher“ als eine falsche Korrektur. Als „hinweis“ Unschärfen, die vertretbar sind. Keine Stil- oder Formatkritik, und keine Kritik daran, dass eine vertretbare Ansicht vertreten wird. Wenn alles korrekt ist, gib eine leere Liste zurück.`;

export function textAus(beitrag) {
  const teile = [];
  for (const f of beitrag.folien || []) teile.push(`[Folie ${f.art}] ${[f.titel, f.untertitel, f.text, ...(f.punkte || []), ...(f.schritte || []).map((s) => (typeof s === "string" ? s : `${s.titel}: ${s.text || ""}`)), f.formel, ...(f.zeilen || []), f.ergebnis, f.links?.titel, ...(f.links?.punkte || []), f.rechts?.titel, ...(f.rechts?.punkte || [])].filter(Boolean).join(" · ")}`);
  for (const s of beitrag.szenen || []) teile.push(`[Szene ${s.art}] ${[s.titel, s.text, s.norm, s.sprecher].filter(Boolean).join(" · ")}`);
  /* Stories tragen den Slot im Kopf, damit ein Befund einer einzelnen Kachel
     zugeordnet werden kann - neun Stories in einem Aufruf zu pruefen ist
     bezahlbar, neun einzelne Aufrufe waeren es nicht. */
  for (const s of beitrag.stories || []) teile.push(`[Story ${s.slot} ${s.art}] ${[s.ueberzeile, s.titel, s.norm, s.formel, s.zahl, s.text, ...(s.optionen || []), s.richtigText, s.falsch].filter(Boolean).join(" · ")}`);
  if (beitrag.caption) teile.push(`[Caption] ${beitrag.caption}`);
  return teile.join("\n");
}

/**
 * Wendet Sprachkorrekturen direkt auf die Texte an: jede Zeichenkette im
 * Objekt, in der „original“ wörtlich vorkommt, bekommt „ersatz“. Kein neuer
 * Aufruf, keine Neufassung – ein doppeltes Wort kostet so nichts.
 * @returns {number} Zahl der ersetzten Stellen
 */
export function korrekturenAnwenden(obj, korrekturen = []) {
  let n = 0;
  const gehe = (o) => {
    if (Array.isArray(o)) { o.forEach((v, i) => { if (typeof v === "string") { const w = ersetze(v); if (w !== v) { o[i] = w; } } else gehe(v); }); return; }
    if (o && typeof o === "object") for (const k of Object.keys(o)) { const v = o[k]; if (typeof v === "string") { const w = ersetze(v); if (w !== v) o[k] = w; } else gehe(v); }
  };
  const ersetze = (text) => {
    let t = text;
    for (const k of korrekturen) { if (k.original && t.includes(k.original)) { t = t.split(k.original).join(k.ersatz); n++; } }
    return t;
  };
  gehe(obj);
  return n;
}

/**
 * @returns {{ok:boolean, fehler:string[], hinweise:string[], korrekturen:{original:string, ersatz:string}[]}}
 */
export async function pruefeFakten(beitrag, zweck = "faktencheck", { hinweis = "" } = {}) {
  if (!CONFIG.faktencheck.aktiv) return { ok: true, fehler: [], hinweise: [], korrekturen: [] };
  budgetPruefen({ "reel-faktencheck": "Reel-Faktencheck", "story-faktencheck": "Story-Faktencheck" }[zweck] || "Faktencheck");
  const modell = CONFIG.ki.modellPruefung || CONFIG.ki.modellNeben;
  const haiku = /haiku/i.test(modell);
  const user = `Prüfe diesen Text:\n\n${textAus(beitrag)}${hinweis ? `\n\n${hinweis}` : ""}`;
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
  if (response.stop_reason === "refusal") return { ok: true, fehler: [], hinweise: [], korrekturen: [] };
  const text = response.content.filter((b) => b.type === "text").map((b) => b.text).join("");
  let daten;
  try { daten = JSON.parse(text.slice(text.indexOf("{"), text.lastIndexOf("}") + 1)); } catch { return { ok: true, fehler: [], hinweise: [], korrekturen: [] }; }
  /* Weiche Beanstandungen („irreführend“, „präzisieren“, „missverständlich“) sind
     keine Fehler, die eine teure Neufassung rechtfertigen – sie werden zu Hinweisen. */
  const WEICH = /irreführend|präzisier|missverständlich|ungenau|unscharf|unschärfe|ausdrucksweise|formulierung|konzeptionell|didaktisch|sollte (?:ergänzt|erwähnt|klargestellt)|könnte|empfehl|verkürzt|vereinfacht|mathematisch (?:richtig|korrekt)|ist (?:zwar |dann )?(?:sachlich )?korrekt/i;
  const ist = (b) => b.schwere === "fehler" && !WEICH.test(`${b.problem} ${b.korrektur}`);
  /* Sprachversehen mit brauchbarer Fundstelle werden ersetzt, nicht neu
     geschrieben. Ohne verwertbares Original (zu kurz, oder Original gleich
     Ersatz) bleibt es ein Hinweis. */
  const sprache = (b) => b.schwere === "sprache";
  const korrekturen = daten.befunde.filter((b) => sprache(b) && b.original && b.ersatz && b.original !== b.ersatz && b.original.trim().split(/\s+/).length >= 2).map((b) => ({ original: b.original, ersatz: b.ersatz }));
  const fehler = daten.befunde.filter(ist).map((b) => `${b.stelle}: ${b.problem} → ${b.korrektur}`);
  const hinweise = daten.befunde.filter((b) => !ist(b) && !sprache(b)).map((b) => `${b.stelle}: ${b.problem}`);
  if (korrekturen.length) console.log(`  Sprachkorrekturen: ${korrekturen.map((k) => `„${k.original}“ → „${k.ersatz}“`).join(" · ")}`);
  return { ok: fehler.length === 0, fehler, hinweise, korrekturen };
}
