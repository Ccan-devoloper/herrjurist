/* ==========================================================================
   Das Postfach: Direktnachrichten lesen und beantworten.

   Läuft bei jedem Lauf (stündlich), wie die Kommentare. Beantwortet werden
   Nachrichten, die von außen kamen, auf die der Kanal noch nicht geantwortet
   hat und die innerhalb der Frist liegen.

   Die Frist ist keine Höflichkeit, sondern Instagrams Regel: Nach der letzten
   Nachricht einer Person darf ein Konto 24 Stunden lang antworten. Danach
   lehnt die API ab. Ein stündlicher Lauf hält das mühelos ein - geprüft wird
   es trotzdem, damit ein verspäteter Versuch gar nicht erst Geld kostet.

   Nicht beantwortet werden: eigene Nachrichten, bereits beantwortete,
   Nachrichten ohne Text (Bilder, Sticker, geteilte Beiträge), reine Emojis
   und alles, was nach Werbung aussieht. Über die Grenze zur Einzelfall-
   beratung wacht der Systemtext - sie ist auf einem Jurakanal keine
   Geschmacksfrage, sondern § 3 RDG.
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

const SYSTEM = `Du beantwortest die Direktnachrichten eines Instagram-Kanals für Menschen, die sich auf das deutsche juristische Staatsexamen vorbereiten. Du schreibst wie eine erfahrene, freundliche Kollegin aus dem Lernkreis: kurz, konkret, auf Augenhöhe, Du-Ansprache.

Eine Direktnachricht ist persönlicher als ein Kommentar – und genau deshalb ist die Grenze hier wichtiger:
- Fachfragen zum Examensstoff beantwortest du gern: knapp, korrekt, mit Norm (§, Abs., Gesetz). Das ist allgemeine Information zum Prüfungsstoff.
- Fragen zu einer KONKRETEN eigenen Rechtssache beantwortest du nicht. „Mein Vermieter hat gekündigt, was kann ich tun?“, „Lohnt sich Widerspruch gegen meinen Bescheid?“, „Habe ich Anspruch auf …?“ – das ist Rechtsdienstleistung in einer fremden Angelegenheit und nach § 3 RDG den Anwält:innen vorbehalten. Sag freundlich, dass du dazu nichts sagen darfst, nenne wenn möglich die allgemeine Regel dahinter, und verweise auf anwaltliche Beratung. Kein „aber grundsätzlich wäre in deinem Fall …“.
- Die Grenze verläuft zwischen „wie ist die Rechtslage“ (geht) und „was soll ich tun“ (geht nicht).

- WENN ein Bezug angegeben ist (Story oder Beitrag, auf den sich die Nachricht bezieht), beantworte die Frage zu genau diesem Inhalt. Frag dann NICHT zurück, worum es geht - das weißt du. Beispiel: Bezug „Wann ist eine Versammlung friedlich?“ und die Frage „Gilt das auch bei Sitzblockaden?“ ist eine Frage zu genau dieser Story.
- Steht kein Bezug dabei, sondern nur „Zuletzt erschienen“, dann ordne die Frage einem dieser Inhalte zu, wenn sie erkennbar dazu passt. Nur wenn mehrere gleich gut passen oder keiner, frag kurz zurück.
- Zurückfragen ist der letzte Ausweg, nicht der erste Reflex.

Weitere Regeln:
- Höchstens 500 Zeichen je Antwort, meistens zwei bis vier Sätze. Höchstens ein Emoji.
- Lob oder Dank: kurz bedanken, eine Frage zurückstellen, die zum Weiterreden einlädt.
- Kritik oder Fehlerhinweis: dankbar aufnehmen und sachlich prüfen; ist der Einwand berechtigt, erkenne das an.
- Keine Zusagen im Namen des Kanals: keine Termine, keine Unterlagen, keine Preise, keine Kooperationen. Steht so etwas im Raum, sag, dass sich jemand meldet.
- Nicht antworten (antworten=false) bei: Werbung, Kooperationsanfragen, Links, Spam, reinen Emojis, Beleidigungen, Bots, Nachrichten ohne erkennbares Anliegen, Nachrichten in anderen Sprachen ohne Bezug.
- Keine Erwähnung von Websites, Produkten, Kursen oder Preisen. Kein Verweis auf eine „Quelle“, ein Skript oder eine Folie.
- Normzitate absatz- und satzgenau: „§ 80 Abs. 3 S. 2 VwVfG“, nicht „§ 80 Abs. 1, 2 VwVfG“. Bist du dir bei Absatz oder Satz nicht sicher, nenne nur den Paragrafen – ein ungenaues Zitat ist schlimmer als ein kurzes.
- Bezeichnungen (Verbote, Institute, Prüfungspunkte) nur, wenn sie genau passen: Schutzausrüstung fällt unter das Schutzwaffenverbot (§ 17a Abs. 1 VersG), nicht unter das Vermummungsverbot (Abs. 2). Prüfe jede Klammer und jedes Etikett einzeln.
- Lieber eine Aussage weniger als eine ungenaue: Ist ein Teil der Antwort unsicher, lass ihn weg.
- Niemals Namen aus der Sperrliste verwenden.
- Du bist ein Kanal, keine Privatperson: keine privaten Verabredungen, keine Telefonnummern, keine Mailadressen.`;

/* Instagrams Antwortfenster. Danach lehnt die API ab - siehe Kopf. */
export const FRIST_STUNDEN = 24;

const NUR_EMOJI = /^[\p{Extended_Pictographic}\s!.?]+$/u;
const WERBUNG = /\b(kooperation|zusammenarbeit|werbung|rabatt|gutschein|promo|follow4follow|f4f|gewinnspiel|invest|krypto|bitcoin|trading|abnehmen|onlyfans)\b/i;

/**
 * Sammelt die Nachrichten, die eine Antwort brauchen.
 *
 * @param {object[]} konversationen Rohdaten aus ig.konversationen()
 * @param {string} eigeneId Konto-ID des Kanals – alles von ihr ist unsere eigene Stimme
 * @param {object} ledger
 * @returns {object[]} mit .uebersprungen als Beiwerk
 */
export function offeneNachrichten(konversationen, eigeneId, ledger, jetzt = Date.now()) {
  const beantwortet = new Set(ledger.postfach?.map((n) => n.nachrichtId) || []);
  const offen = [];
  const uebersprungen = [];
  const skip = (n, von, grund) => uebersprungen.push({ id: n.id, von, text: (n.message || "").slice(0, 60), grund });

  /* Was der Kanal zuletzt veröffentlicht hat, nach Medien-ID. Damit wird aus
     einer Story-Antwort ein Thema statt einer anonymen ID. */
  const nachId = new Map();
  for (const e of ledger.veroeffentlicht || []) if (e.medienId) nachId.set(String(e.medienId), e);
  const grenzeBezug = new Date(jetzt - 3 * 86400000).toISOString().slice(0, 10);
  const zuletzt = (ledger.veroeffentlicht || [])
    .filter((e) => String(e.datum || "") >= grenzeBezug && e.titel)
    .slice(-12)
    .map((e) => ({ art: e.art === "story" ? "Story" : "Beitrag", titel: String(e.titel).slice(0, 110) }));

  for (const k of konversationen || []) {
    const nachrichten = [...(k.messages?.data || [])].sort((a, b) => new Date(a.created_time) - new Date(b.created_time));
    if (!nachrichten.length) continue;
    const letzte = nachrichten.at(-1);
    /* Haben wir zuletzt geschrieben, ist nichts offen - unabhängig davon, was
       davor stand. Das erspart es, jede einzelne Nachricht zu vergleichen. */
    if (letzte.from?.id && String(letzte.from.id) === String(eigeneId)) continue;
    const von = letzte.from?.username || letzte.from?.id || "?";

    if (beantwortet.has(letzte.id)) { skip(letzte, von, "bereits behandelt"); continue; }
    const text = String(letzte.message || "").trim();
    /* Bilder, Sticker und geteilte Beiträge kommen ohne Text an. Darauf lässt
       sich nichts Sinnvolles antworten. */
    if (!text) { skip(letzte, von, "ohne Text"); continue; }
    if (text.length < 2 || NUR_EMOJI.test(text)) { skip(letzte, von, "nur Emoji"); continue; }
    if (WERBUNG.test(text)) { skip(letzte, von, "Werbung"); continue; }
    const alter = jetzt - new Date(letzte.created_time).getTime();
    if (!(alter >= 0)) { skip(letzte, von, "ohne brauchbaren Zeitstempel"); continue; }
    if (alter > FRIST_STUNDEN * 3600000) { skip(letzte, von, `älter als ${FRIST_STUNDEN} Stunden – Instagram nimmt keine Antwort mehr an`); continue; }

    /* Der Verlauf davor gibt der Antwort Halt: Wer schon einmal gefragt hat,
       bekommt sonst dieselbe Auskunft ein zweites Mal. */
    const verlauf = nachrichten.slice(-6, -1).map((m) => ({
      wer: String(m.from?.id) === String(eigeneId) ? "kanal" : "person",
      text: String(m.message || "").trim().slice(0, 300),
    })).filter((m) => m.text);

    /* Bezug: Story-Antwort oder Antwort auf eine frühere Nachricht. Die ID
       schlagen wir im Ledger nach - dort steht der Titel dessen, was wir
       selbst veröffentlicht haben. */
    const storyId = letzte.reply_to?.story?.id;
    const eintrag = storyId ? nachId.get(String(storyId)) : null;
    const bezug = eintrag
      ? `${eintrag.art === "story" ? "Story" : "Beitrag"} „${String(eintrag.titel || "").slice(0, 140)}“`
      : (storyId || letzte.reply_to?.story?.url) ? "Antwort auf eine unserer Stories (Inhalt nicht auffindbar)" : null;

    offen.push({ id: letzte.id, text, von, empfaengerId: letzte.from?.id, konversationId: k.id, zeit: letzte.created_time, verlauf, bezug });
  }

  offen.sort((a, b) => new Date(a.zeit) - new Date(b.zeit));
  offen.uebersprungen = uebersprungen;
  offen.zuletzt = zuletzt;
  return offen;
}

/* Antworten in einem Aufruf formulieren - wie bei den Kommentaren. Ein Aufruf
   für alle offenen Nachrichten, nicht einer je Nachricht. */
export async function antwortenFormulieren(nachrichten, zuletzt = []) {
  if (!nachrichten.length) return [];
  const hintergrund = zuletzt.length
    ? `\nZuletzt erschienen (falls kein Bezug dabeisteht, passt die Frage oft zu einem davon):\n${zuletzt.map((e) => `- ${e.art}: „${e.titel}“`).join("\n")}\n`
    : "";
  const user = `Beantworte die folgenden Direktnachrichten. „Bezug“ nennt die Story oder den Beitrag, auf den sich die Nachricht bezieht; „Verlauf“, was in derselben Unterhaltung davor stand.
${hintergrund}
${nachrichten.map((n) => {
    const b = n.bezug ? `\n  Bezug: ${n.bezug}` : "";
    const v = n.verlauf?.length ? `\n  Verlauf: ${n.verlauf.map((m) => `${m.wer === "kanal" ? "wir" : "sie/er"}: „${m.text}“`).join(" | ")}` : "";
    return `- id ${n.id} · von @${n.von}: „${n.text}“${b}${v}`;
  }).join("\n")}

Sperrliste: ${korpus().namen.join(", ")}

Gib für jede id an, ob geantwortet werden soll (antworten), den Grund bei Nein (grund) und den Antworttext (text, null bei Nein).`;
  budgetPruefen("Nachrichten beantworten");
  const response = await client().messages.create({
    model: CONFIG.antworten.modell,
    max_tokens: 8000,
    system: [{ type: "text", text: SYSTEM, cache_control: { type: "ephemeral" } }],
    messages: [{ role: "user", content: user }],
    thinking: { type: "adaptive" },
    output_config: { effort: CONFIG.antworten.aufwand, format: { type: "json_schema", schema: ANTWORT_SCHEMA } },
  });
  erfassen(CONFIG.antworten.modell, response.usage, "nachrichten");
  if (response.stop_reason === "refusal") return [];
  const text = response.content.filter((b) => b.type === "text").map((b) => b.text).join("");
  const daten = JSON.parse(text.slice(text.indexOf("{"), text.lastIndexOf("}") + 1));
  return daten.antworten.map((a) => ({
    id: a.id,
    text: a.antworten && a.text && a.text.trim().length > 0 ? a.text.trim().slice(0, CONFIG.postfach.maxZeichen) : null,
    grund: a.grund || null,
  }));
}

/**
 * Kompletter Postfachlauf.
 * @returns {{unterhaltungen:number, offen:number, beantwortet:number}}
 */
export async function nachrichtenBeantworten(ig, ledger, { log = console.log } = {}) {
  const konversationen = await ig.konversationen(CONFIG.postfach.unterhaltungen);
  const alle = offeneNachrichten(konversationen, ig.kontoId, ledger);
  for (const u of alle.uebersprungen || []) {
    if (u.grund !== "bereits behandelt") log(`  · Nachricht von @${u.von} „${u.text}“ → übersprungen (${u.grund})`);
  }
  const offen = alle.slice(0, CONFIG.postfach.maxJeLauf);
  if (!offen.length) return { unterhaltungen: konversationen.length, offen: 0, beantwortet: 0 };

  log(`Postfach: ${offen.length} offene Nachrichten in ${konversationen.length} Unterhaltungen`);
  const antworten = await antwortenFormulieren(offen, alle.zuletzt || []);
  const nachId = new Map(antworten.map((a) => [a.id, a.text]));
  const gruende = new Map(antworten.map((a) => [a.id, a.grund]));
  let n = 0;
  ledger.postfach = ledger.postfach || [];
  for (const nachricht of offen) {
    const text = nachId.get(nachricht.id);
    const eintrag = { nachrichtId: nachricht.id, konversationId: nachricht.konversationId, datum: new Date().toISOString().slice(0, 10), von: nachricht.von };
    if (!text) {
      ledger.postfach.push({ ...eintrag, uebersprungen: true });
      log(`  · @${nachricht.von} „${nachricht.text.slice(0, 60)}“ → keine Antwort (${gruende.get(nachricht.id) || "vom Modell übersprungen"})`);
      continue;
    }
    try {
      const antwortId = await ig.nachrichtSenden(nachricht.empfaengerId, text);
      ledger.postfach.push({ ...eintrag, antwortId, text });
      n++;
      log(`  ↳ @${nachricht.von}: „${nachricht.text.slice(0, 60)}“ → „${text.slice(0, 80)}“`);
    } catch (e) {
      console.error(`  ✗ Antwort an @${nachricht.von}: ${e.message}`);
    }
  }
  /* Ledger schlank halten - wie bei den Kommentaren. */
  const grenze = new Date(Date.now() - 60 * 86400000).toISOString().slice(0, 10);
  ledger.postfach = ledger.postfach.filter((x) => x.datum >= grenze);
  return { unterhaltungen: konversationen.length, offen: offen.length, beantwortet: n };
}
