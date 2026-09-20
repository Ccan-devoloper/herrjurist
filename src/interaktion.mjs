/* ==========================================================================
   Echte Interaktion: Kommentare unter den eigenen Beiträgen beantworten.

   Läuft bei jedem Lauf (stündlich). Beantwortet werden neue Kommentare der
   letzten Tage unter den letzten Beiträgen – kurz, fachlich, freundlich.
   Nicht beantwortet werden: eigene Kommentare, bereits beantwortete, Spam,
   reine Emojis, Werbung, Bitten um Rechtsberatung im Einzelfall.
   Alles über die offizielle API (Antworten auf Kommentare); kein Auto-Follow,
   kein Auto-Like – das erlaubt Instagram nicht.
   ========================================================================== */

import { CONFIG } from "./config.mjs";
import { claudeAufruf } from "./anbieter.mjs";
import { uebersprungeneMelden } from "./postfach.mjs";
import { korpus } from "./pruefung.mjs";


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

const SYSTEM = `Du betreust die Kommentare eines Instagram-Kanals für Menschen, die sich auf das erste oder zweite juristische Staatsexamen vorbereiten. Du antwortest wie eine erfahrene, freundliche Kollegin aus der Lerngruppe: kurz, konkret, auf Augenhöhe, Du-Ansprache.

Regeln:
- Maximal 280 Zeichen je Antwort, meistens 1–2 Sätze. Kein Emoji-Spam (höchstens eines).
- Klinge wie ein Mensch, der kurz zurückschreibt - nicht wie ein Automat: keine Aufzählungszeichen, keine Überschriften, keine Paragrafenketten, keine Sätze über dich selbst („dann baue ich dir …", „schreib mir einfach …"), kein „Gerne!" und kein „Super Frage!".
- Rate nie, worum es geht. Passt der Kommentar nicht erkennbar zum Beitrag oder zum mitgelieferten Thread, frag in einem kurzen Satz nach, statt ein Thema zu erfinden.
- Thread-Kontext ist Teil des Gesprächs: Kurze Folgeantworten wie „ja“, „genau“, „gerne beides“, „das zweite“ oder „mach beides“ beziehen sich regelmäßig auf die unmittelbar vorherige Frage/Alternative. Wenn der Thread diese Referenz auflöst, darfst du NICHT erneut fragen, worauf sich die Folgeantwort bezieht.
- Fachfragen: knapp und korrekt beantworten, mit Norm (§, Abs., Gesetz). Wenn die Frage in einem Kommentar nicht sicher beantwortbar ist, sag das ehrlich und nenne, worauf es ankommt.
- Lob oder Zustimmung: kurz bedanken und eine Rückfrage stellen, die zum Weiterreden einlädt (z. B. welches Thema als Nächstes).
- Kritik oder Fehlerhinweis: dankbar aufnehmen, sachlich prüfen; wenn der Einwand berechtigt ist, das anerkennen.
- Bitten um Rechtsberatung zu einem persönlichen Fall: freundlich ablehnen und auf die allgemeine Regel verweisen. Rechtsberatung im Einzelfall ist Anwältinnen und Anwälten vorbehalten (§ 3 RDG) – dieser Kanal erklärt Examensstoff, er berät nicht.
- Nicht antworten (antworten=false) bei: Spam, Werbung, Links, reinen Emojis oder „Erster!“, Beleidigungen, Bots, Kommentaren in anderen Sprachen ohne Bezug, und wenn der Kanal bereits geantwortet hat.
- Keine Erwähnung von Websites, Produkten oder Kursen. Kein Verweis auf eine „Quelle“ oder ein Skript.
- Normzitate absatz- und satzgenau: „§ 80 Abs. 3 S. 2 VwVfG“, nicht „§ 80 Abs. 1, 2 VwVfG“. Bist du dir bei Absatz oder Satz nicht sicher, nenne nur den Paragrafen – ein ungenaues Zitat ist schlimmer als ein kurzes.
- Bezeichnungen (Verbote, Institute, Prüfungspunkte) nur, wenn sie genau passen: Schutzausrüstung fällt unter das Schutzwaffenverbot (§ 17a Abs. 1 VersG), nicht unter das Vermummungsverbot (Abs. 2). Prüfe jede Klammer und jedes Etikett einzeln.
- Lieber eine Aussage weniger als eine ungenaue: Ist ein Teil der Antwort unsicher, lass ihn weg.
- Niemals Namen aus der Sperrliste verwenden.`;

/* Kommentare sammeln, die eine Antwort brauchen. */
const gleicherName = (a, b) => Boolean(a && b && String(a).toLowerCase() === String(b).toLowerCase());
const zeitwert = (x) => {
  const n = new Date(x || 0).getTime();
  return Number.isFinite(n) ? n : 0;
};
const verlaufsZeile = (k, eigenerName) => ({
  rolle: gleicherName(k.username, eigenerName) ? "Kanal" : `@${k.username || "Nutzer"}`,
  text: String(k.text || "").trim().slice(0, 500),
});

function kommentarKandidaten(medium) {
  const roots = medium.comments?.data || [];
  const alle = new Map();
  const threadVorher = new Map();

  for (const root of roots) {
    if (root?.id) alle.set(root.id, root);
    const replies = [...(root.replies?.data || [])].sort((a, b) => zeitwert(a.timestamp) - zeitwert(b.timestamp));
    const vorher = [root];
    for (const r of replies) {
      if (!r?.id) continue;
      if (!threadVorher.has(r.id)) threadVorher.set(r.id, vorher.filter(Boolean));
      if (!alle.has(r.id)) alle.set(r.id, r);
      vorher.push(r);
    }
  }
  return { roots, alle: [...alle.values()], threadVorher };
}

function fallbackKontext(k, medium, eigenerName, ledger, alleKommentare) {
  const aktuell = zeitwert(k.timestamp);
  const fenster = 48 * 60 * 60 * 1000;
  const nachId = new Map(alleKommentare.filter((c) => c?.id).map((c) => [c.id, c]));
  const kandidaten = (ledger.interaktionen || [])
    .filter((i) => i && !i.uebersprungen && i.text && i.medienId === medium.id && gleicherName(i.von, k.username))
    .map((i) => {
      const ursprung = nachId.get(i.kommentarId);
      const frage = String(i.kommentarText || ursprung?.text || "").trim();
      const zeit = zeitwert(i.zeitpunkt || ursprung?.timestamp || i.datum);
      return { i, frage, zeit };
    })
    .filter((x) => x.frage && (!aktuell || !x.zeit || (x.zeit < aktuell && aktuell - x.zeit <= fenster)))
    .sort((a, b) => b.zeit - a.zeit);

  const vor = kandidaten[0];
  if (!vor) return [];
  return [
    { rolle: `@${k.username || "Nutzer"}`, text: vor.frage.slice(0, 500) },
    { rolle: "Kanal", text: String(vor.i.text).trim().slice(0, 500) },
  ];
}

export function offeneKommentare(medien, eigenerName, ledger, opt = {}) {
  const maxAlter = (opt.maxAlterTage ?? CONFIG.interaktion.maxAlterTage) * 86400000;
  const beantwortet = new Set(ledger.interaktionen?.map((i) => i.kommentarId) || []);
  const offen = [];
  const uebersprungen = [];
  const skip = (k, grund) => uebersprungen.push({ id: k.id, username: k.username, text: (k.text || "").slice(0, 60), grund });

  for (const m of medien) {
    const { alle, threadVorher } = kommentarKandidaten(m);
    for (const k of alle) {
      if (!k.text || k.hidden) { skip(k, "leer oder verborgen"); continue; }
      if (gleicherName(k.username, eigenerName)) { skip(k, "eigener Kommentar"); continue; }
      if (beantwortet.has(k.id)) { skip(k, "bereits behandelt"); continue; }
      if (Date.now() - zeitwert(k.timestamp) > maxAlter) { skip(k, "älter als Frist"); continue; }
      const eigeneAntwort = (k.replies?.data || []).some((r) => gleicherName(r.username, eigenerName));
      if (eigeneAntwort) { skip(k, "schon beantwortet"); continue; }
      const text = k.text.trim();
      if (text.length < 2 || /^[\p{Extended_Pictographic}\s!.?]+$/u.test(text)) { skip(k, "nur Emoji"); continue; }

      const direkt = (threadVorher.get(k.id) || []).map((v) => verlaufsZeile(v, eigenerName)).filter((v) => v.text);
      const kontext = direkt.length ? direkt.slice(-6) : fallbackKontext(k, m, eigenerName, ledger, alle);
      offen.push({
        id: k.id, text, username: k.username, timestamp: k.timestamp,
        beitrag: (m.caption || "").split("\n")[0].slice(0, 160),
        permalink: m.permalink, medienId: m.id, kontext,
      });
    }
  }
  offen.sort((a, b) => new Date(a.timestamp) - new Date(b.timestamp));
  offen.uebersprungen = uebersprungen;
  return offen;
}

/* Antworten in einem Aufruf formulieren. */
export function kommentarPrompt(kommentare) {
  const block = (k) => {
    const thread = k.kontext?.length
      ? `\n  Thread davor:\n${k.kontext.map((v) => `    ${v.rolle}: „${v.text}“`).join("\n")}`
      : "";
    return `- id ${k.id} · Beitrag: „${k.beitrag}“${thread}\n  Aktueller Kommentar · @${k.username}: „${k.text}“`;
  };
  return `Beantworte die folgenden Kommentare. Zu jedem Kommentar steht die erste Zeile des Beitrags und, falls vorhanden, der Gesprächsverlauf davor. Der Thread ist verbindlicher Kontext für kurze Folgeantworten.

${kommentare.map(block).join("\n\n")}

Sperrliste: ${korpus().namen.join(", ")}

Gib für jede id an, ob geantwortet werden soll (antworten), den Grund bei Nein (grund) und den Antworttext (text, null bei Nein).`;
}

export async function antwortenFormulieren(kommentare) {
  if (!kommentare.length) return [];
  const user = kommentarPrompt(kommentare);
  const response = await claudeAufruf({
    zweck: "kommentare", modell: CONFIG.antworten.modell,
    params: {
      model: CONFIG.antworten.modell,
      max_tokens: 8000,
      system: [{ type: "text", text: SYSTEM, cache_control: { type: "ephemeral" } }],
      messages: [{ role: "user", content: user }],
      thinking: { type: "adaptive" },
      output_config: { effort: CONFIG.antworten.aufwand, format: { type: "json_schema", schema: ANTWORT_SCHEMA } },
    },
  });
  if (response.stop_reason === "refusal") return [];
  const text = response.content.filter((b) => b.type === "text").map((b) => b.text).join("");
  let daten;
  try { daten = JSON.parse(text.slice(text.indexOf("{"), text.lastIndexOf("}") + 1)); }
  catch (e) { console.warn(`  ! Antworten nicht lesbar (${e.message.slice(0, 80)}) – diesmal keine Antworten.`); return []; }
  if (!Array.isArray(daten?.antworten)) return [];
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
  uebersprungeneMelden(alle.uebersprungen || [], log, "username");
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
    const eintrag = { kommentarId: k.id, medienId: k.medienId, datum: new Date().toISOString().slice(0, 10), zeitpunkt: k.timestamp || new Date().toISOString(), von: k.username, kommentarText: k.text };
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
