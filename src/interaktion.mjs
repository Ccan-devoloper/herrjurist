/* ==========================================================================
   Echte Interaktion: Kommentare unter den eigenen Beiträgen beantworten.

   Läuft bei jedem Lauf (stündlich). Beantwortet werden neue Kommentare der
   letzten Tage unter den letzten Beiträgen – kurz, fachlich, freundlich.
   Nicht beantwortet werden: eigene Kommentare, bereits beantwortete, Spam,
   reine Emojis, Werbung, Bitten um individuelle Steuerberatung.
   Alles über die offizielle API (Antworten auf Kommentare); kein Auto-Follow,
   kein Auto-Like – das erlaubt Instagram nicht.
   ========================================================================== */

import Anthropic from "@anthropic-ai/sdk";
import { CONFIG } from "./config.mjs";
import { budgetPruefen, erfassen } from "./kosten.mjs";
import { korpus } from "./pruefung.mjs";

let clientCache = null;
const client = () => (clientCache ||= new Anthropic({ maxRetries: 3, timeout: 5 * 60 * 1000 }));

const ANTWORT_SCHEMA = {
  type: "object",
  additionalProperties: false,
  properties: {
    antworten: {
      type: "array",
      items: {
        type: "object",
        additionalProperties: false,
        properties: {
          id: { type: "string" },
          antworten: { type: "boolean" },
          grund: { type: ["string", "null"] },
          text: { type: ["string", "null"] },
        },
        required: ["id", "antworten", "grund", "text"],
      },
    },
  },
  required: ["antworten"],
};

const SYSTEM = `Du betreust die Kommentare eines Instagram-Kanals für Menschen, die sich auf das deutsche Steuerberaterexamen vorbereiten. Du antwortest wie eine erfahrene, freundliche Kollegin aus dem Lernkreis: kurz, konkret, auf Augenhöhe, Du-Ansprache.

Regeln:
- Maximal 280 Zeichen je Antwort, meistens 1–2 Sätze. Kein Emoji-Spam (höchstens eines).
- Fachfragen: knapp und korrekt beantworten, mit Norm (§, Abs., Gesetz). Wenn die Frage in einem Kommentar nicht sicher beantwortbar ist, sag das ehrlich und nenne, worauf es ankommt.
- Lob oder Zustimmung: kurz bedanken und eine Rückfrage stellen, die zum Weiterreden einlädt (z. B. welches Thema als Nächstes).
- Kritik oder Fehlerhinweis: dankbar aufnehmen, sachlich prüfen; wenn der Einwand berechtigt ist, das anerkennen.
- Bitten um individuelle Steuerberatung zu einem persönlichen Fall: freundlich ablehnen und auf die allgemeine Regel verweisen – keine Beratung im Einzelfall.
- Nicht antworten (antworten=false) bei: Spam, Werbung, Links, reinen Emojis oder „Erster!“, Beleidigungen, Bots, Kommentaren in anderen Sprachen ohne Bezug, und wenn der Kanal bereits geantwortet hat.
- Keine Erwähnung von Websites, Produkten oder Kursen. Kein Verweis auf eine „Quelle“ oder ein Skript.
- Niemals Namen aus der Sperrliste verwenden.`;

/* Kommentare sammeln, die eine Antwort brauchen. */
export function offeneKommentare(medien, eigenerName, ledger, opt = {}) {
  const maxAlter = (opt.maxAlterTage ?? CONFIG.interaktion.maxAlterTage) * 86400000;
  const beantwortet = new Set(ledger.interaktionen?.map((i) => i.kommentarId) || []);
  const offen = [];
  const uebersprungen = [];
  const skip = (k, grund) => uebersprungen.push({ id: k.id, username: k.username, text: (k.text || "").slice(0, 60), grund });
  for (const m of medien) {
    for (const k of m.comments?.data || []) {
      if (!k.text || k.hidden) { skip(k, "leer oder verborgen"); continue; }
      if (k.username && eigenerName && k.username.toLowerCase() === eigenerName.toLowerCase()) { skip(k, "eigener Kommentar"); continue; }
      if (beantwortet.has(k.id)) { skip(k, "bereits behandelt"); continue; }
      if (Date.now() - new Date(k.timestamp).getTime() > maxAlter) { skip(k, "älter als Frist"); continue; }
      const eigeneAntwort = (k.replies?.data || []).some((r) => r.username && eigenerName && r.username.toLowerCase() === eigenerName.toLowerCase());
      if (eigeneAntwort) { skip(k, "schon beantwortet"); continue; }
      const text = k.text.trim();
      if (text.length < 2 || /^[\p{Extended_Pictographic}\s!.?]+$/u.test(text)) { skip(k, "nur Emoji"); continue; }
      offen.push({ id: k.id, text, username: k.username, timestamp: k.timestamp, beitrag: (m.caption || "").split("\n")[0].slice(0, 160), permalink: m.permalink, medienId: m.id });
    }
  }
  offen.sort((a, b) => new Date(a.timestamp) - new Date(b.timestamp));
  offen.uebersprungen = uebersprungen;
  return offen;
}

/* Antworten in einem Aufruf formulieren. */
export async function antwortenFormulieren(kommentare) {
  if (!kommentare.length) return [];
  const user = `Beantworte die folgenden Kommentare. Zu jedem Kommentar steht die erste Zeile des Beitrags, unter dem er steht.

${kommentare.map((k) => `- id ${k.id} · Beitrag: „${k.beitrag}“ · @${k.username}: „${k.text}“`).join("\n")}

Sperrliste: ${korpus().namen.join(", ")}

Gib für jede id an, ob geantwortet werden soll (antworten), den Grund bei Nein (grund) und den Antworttext (text, null bei Nein).`;
  budgetPruefen("Kommentare beantworten");
  const response = await client().messages.create({
    model: CONFIG.ki.modellNeben,
    max_tokens: 8000,
    system: [{ type: "text", text: SYSTEM, cache_control: { type: "ephemeral" } }],
    messages: [{ role: "user", content: user }],
    thinking: { type: "adaptive" },
    output_config: { effort: "medium", format: { type: "json_schema", schema: ANTWORT_SCHEMA } },
  });
  erfassen(CONFIG.ki.modellNeben, response.usage, "kommentare");
  if (response.stop_reason === "refusal") return [];
  const text = response.content.filter((b) => b.type === "text").map((b) => b.text).join("");
  const daten = JSON.parse(text.slice(text.indexOf("{"), text.lastIndexOf("}") + 1));
  return daten.antworten.map((a) => ({ id: a.id, text: a.antworten && a.text && a.text.trim().length > 0 ? a.text.trim().slice(0, 300) : null, grund: a.grund || null }));
}

/**
 * Kompletter Interaktionslauf.
 * @returns {{geprueft:number, beantwortet:number}}
 */
export async function kommentareBeantworten(ig, ledger, { log = console.log } = {}) {
  const eigener = await ig.eigenerName();
  const medien = await ig.neuesteMedien(CONFIG.interaktion.beitraegeZurueck);
  const alle = offeneKommentare(medien, eigener, ledger);
  const gesamtKommentare = medien.reduce((n, m) => n + (m.comments?.data?.length || 0), 0);
  for (const u of alle.uebersprungen || []) if (u.grund !== "bereits behandelt") log(`  · Kommentar von @${u.username || "?"} „${u.text}“ → übersprungen (${u.grund})`);
  const offen = alle.slice(0, CONFIG.interaktion.maxAntwortenJeLauf);
  if (!offen.length) return { geprueft: medien.length, kommentare: gesamtKommentare, beantwortet: 0 };
  log(`Interaktion: ${offen.length} neue Kommentare unter ${medien.length} Beiträgen (${gesamtKommentare} gesamt)`);
  const antworten = await antwortenFormulieren(offen);
  const nachId = new Map(antworten.map((a) => [a.id, a.text]));
  const gruende = new Map(antworten.map((a) => [a.id, a.grund]));
  let n = 0;
  ledger.interaktionen = ledger.interaktionen || [];
  for (const k of offen) {
    const text = nachId.get(k.id);
    const eintrag = { kommentarId: k.id, medienId: k.medienId, datum: new Date().toISOString().slice(0, 10), von: k.username };
    if (!text) { ledger.interaktionen.push({ ...eintrag, uebersprungen: true }); log(`  · @${k.username} „${k.text.slice(0, 60)}“ → keine Antwort (${gruende.get(k.id) || "vom Modell übersprungen"})`); continue; }
    try {
      const antwortId = await ig.kommentarBeantworten(k.id, text);
      ledger.interaktionen.push({ ...eintrag, antwortId, text });
      n++;
      log(`  ↳ @${k.username}: „${k.text.slice(0, 60)}“ → „${text.slice(0, 80)}“`);
    } catch (e) {
      console.error(`  ✗ Antwort auf ${k.id}: ${e.message}`);
    }
  }
  /* Ledger schlank halten. */
  const grenze = new Date(Date.now() - 60 * 86400000).toISOString().slice(0, 10);
  ledger.interaktionen = ledger.interaktionen.filter((i) => i.datum >= grenze);
  return { geprueft: medien.length, beantwortet: n };
}
