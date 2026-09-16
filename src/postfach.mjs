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

Woher du weißt, worum es geht – und was du tust, wenn du es nicht weißt:
- Steht ein „Bezug“ dabei, ist die Sache klar: Beantworte die Frage zu GENAU diesem Inhalt und frag nicht zurück, worum es geht.
- Nennt die Nachricht das Thema selbst („Wie ist das bei der Anfechtung?“), antworte darauf.
- Steht als Bezug, dass es eine Story-Antwort ist, die Story aber nicht zugeordnet werden konnte: Dann ist der VERLAUF NICHT der Bezug. Wer gerade auf eine Story antwortet, meint diese Story – nicht das Thema von gestern. Sieh in „Aktuell laufende Stories“ nach: Passt genau eine davon erkennbar zur Frage, beantworte sie dazu. Passen mehrere oder keine, frag in EINEM kurzen Satz nach und biete zwei bis drei der LAUFENDEN Stories zur Auswahl an („Meinst du die zur Norm des Tages, die Prüfungsfrage zum Verwaltungsrecht oder die zum Streitstand Beweislast?“). Nenne dabei NIEMALS einen Beitrag aus „Zuletzt erschienen“ – auf einen Beitrag kann man nicht per Story antworten. Das ist keine Schwäche, sondern das Einzige, was hier richtig ist.
- Am 16.09. kam auf eine Antwort zur Beweislast-Story die Frage „Wo müsste ich das genau einbauen und prüfen?“ – und zurück ging eine Antwort zum Unterhaltsrecht, weil das im Verlauf davor stand. Der Verlauf hilft beim Ton und beim Wiederholungsschutz, er bestimmt aber nicht das Thema.
- RATE NIEMALS. Du erfindest kein Thema und schreibst nie „Ich tippe auf …“, „Vermutlich meinst du …“, „Falls du etwas anderes meinst …“. Eine selbstbewusst falsche Antwort ist der schlimmste Ausgang – schlimmer als eine Rückfrage, schlimmer als gar keine Antwort. Am 16.09. wurde auf eine Frage zur Beweislast im Zivilprozess eine Prüfung der Anfechtung geschickt; so etwas darf nicht noch einmal passieren.
- „Zuletzt erschienen“ ist HINTERGRUND, keine Zuordnungshilfe. Daraus darfst du nur schließen, wenn die Frage unmissverständlich zu genau einem Eintrag passt und zu keinem anderen. Sind mehrere Einträge zur selben Uhrzeit erschienen, sagt die Liste gar nichts – dann frag.

So klingst du:
- Wie ein Mensch, der zwischendurch am Handy antwortet. Zwei bis vier Sätze, höchstens 500 Zeichen, höchstens ein Emoji.
- Keine Paragrafenketten in einer DM. Ein, zwei Normen reichen; der Rest ist Prosa.
- Keine Sätze über dich selbst und deine Arbeitsweise: kein „dann baue ich dir den Aufbau dazu“, kein „schreib mir einfach das Stichwort“, kein Anbieten von Leistungen, keine Ankündigung, was du als Nächstes tun würdest.
- Keine Aufzählungszeichen, keine Überschriften, keine Nummerierung. Fließtext.
- Nicht überfreundlich und nicht anbiedernd. Kein „Gerne!“, kein „Super Frage!“, kein Ausrufezeichen-Stakkato.

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
export function offeneNachrichten(konversationen, eigeneId, ledger, jetzt = Date.now(), laufend = []) {
  const beantwortet = new Set(ledger.postfach?.map((n) => n.nachrichtId) || []);
  const offen = [];
  const uebersprungen = [];
  const skip = (n, von, grund) => uebersprungen.push({ id: n.id, von, text: (n.message || "").slice(0, 60), grund });

  /* Was der Kanal zuletzt veröffentlicht hat, nach Medien-ID. Damit wird aus
     einer Story-Antwort ein Thema statt einer anonymen ID. */
  const nachId = new Map();
  for (const e of ledger.veroeffentlicht || []) if (e.medienId) nachId.set(String(e.medienId), e);
  /* Bruecke ueber den Veroeffentlichungszeitpunkt: Sollte Instagram fuer die
     Story-Antwort eine andere ID nennen als die, die wir beim Posten
     zurueckbekommen haben, verbindet die Uhrzeit die beiden Welten. Unsere
     Stories erscheinen sekundengenau protokolliert; zwei Minuten Abstand
     reichen zur Zuordnung und sind eng genug, um nicht die Nachbarstory zu
     erwischen. */
  const heute = new Date(jetzt).toISOString().slice(0, 10);
  const wannText = (e) => {
    const t = e.veroeffentlicht ? new Date(e.veroeffentlicht) : null;
    if (!t || Number.isNaN(t.getTime())) return String(e.datum || "");
    const uhr = t.toLocaleTimeString("de-DE", { hour: "2-digit", minute: "2-digit", timeZone: CONFIG.marke.zeitzone || "Europe/Berlin" });
    return `${e.datum === heute ? "heute" : e.datum} ${uhr}`;
  };
  const laufendeMitTitel = [];
  for (const st of laufend || []) {
    const t = st.timestamp ? new Date(st.timestamp).getTime() : NaN;
    const treffer = (ledger.veroeffentlicht || [])
      .filter((e) => e.art === "story" && e.veroeffentlicht && e.titel)
      .map((e) => ({ e, abstand: Math.abs(new Date(e.veroeffentlicht).getTime() - t) }))
      .filter((x) => x.abstand < 120000)
      .sort((a, b) => a.abstand - b.abstand)[0]?.e;
    if (treffer && st.id) nachId.set(String(st.id), treffer);
    if (treffer) laufendeMitTitel.push({ titel: String(treffer.titel).slice(0, 110), wann: wannText(treffer) });
  }
  /* Und wenn Instagram gar nichts liefert - am 16.09. kam „Laufende Stories: 0"
     zurueck, der Zugang ueber Instagram Login kennt den Endpunkt offenbar
     nicht -, nehmen wir unser eigenes Protokoll. Was in den letzten 24 Stunden
     als Story erschienen ist, laeuft noch; das wissen wir besser als jede
     Abfrage, denn wir haben es selbst veroeffentlicht. */
  if (!laufendeMitTitel.length) {
    const vor24h = jetzt - 24 * 3600000;
    for (const e of ledger.veroeffentlicht || []) {
      if (e.art !== "story" || !e.titel || !e.veroeffentlicht) continue;
      if (new Date(e.veroeffentlicht).getTime() < vor24h) continue;
      laufendeMitTitel.push({ titel: String(e.titel).slice(0, 110), wann: wannText(e) });
    }
  }
  const grenzeBezug = new Date(jetzt - 3 * 86400000).toISOString().slice(0, 10);
  /* Mit Uhrzeit, nicht nur mit Titel: Wurden neun Stories innerhalb von zwei
     Minuten veroeffentlicht, taugt die Liste NICHT zum Zuordnen - und das
     muss das Modell sehen koennen, statt zu raten. */
  const zuletzt = (ledger.veroeffentlicht || [])
    .filter((e) => String(e.datum || "") >= grenzeBezug && e.titel)
    .slice(-12)
    .map((e) => ({ art: e.art === "story" ? "Story" : "Beitrag", titel: String(e.titel).slice(0, 110), wann: wannText(e) }));

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
    /* Instagram legt den Bezug einer Story-Antwort nicht immer an dieselbe
       Stelle - am 16.09. fehlte `reply_to` an einer Story-Antwort ganz, und
       der Bot riet daraufhin ein Thema zusammen („Ich tippe auf die
       Anfechtung"). Deshalb wird an jeder Stelle nachgesehen, die die ID
       tragen kann, und festgehalten, WOHER sie kam - sonst tappt man beim
       naechsten Mal wieder im Dunkeln. */
    const idKandidaten = [letzte.reply_to?.story?.id, letzte.story?.id, letzte.reply_to?.message?.id]
      .filter(Boolean).map(String);
    const istStoryAntwort = Boolean(letzte.reply_to?.story || letzte.story);
    const eintrag = idKandidaten.map((id) => nachId.get(id)).find(Boolean) || null;
    const bezug = eintrag
      ? `${eintrag.art === "story" ? "Story" : "Beitrag"} „${String(eintrag.titel || "").slice(0, 140)}“`
      : istStoryAntwort ? "Die Nachricht ist eine Antwort auf eine unserer Stories – WELCHE, hat Instagram nicht mitgeliefert" : null;
    const bezugQuelle = eintrag ? "aufgelöst" : istStoryAntwort ? "Story-Antwort ohne Zuordnung" : "kein Bezug";
    /* Welche IDs Instagram ueberhaupt geschickt hat, gehoert ins Log: Ohne das
       bleibt offen, ob gar keine ID kam oder eine aus einem anderen
       Namensraum - und damit auch, was zu tun ist. */
    const bezugRoh = istStoryAntwort && !eintrag
      ? `ids=[${idKandidaten.join(",") || "keine"}] url=${letzte.reply_to?.story?.url ? "ja" : "nein"}`
      : "";

    offen.push({ id: letzte.id, text, von, empfaengerId: letzte.from?.id, konversationId: k.id, zeit: letzte.created_time, verlauf, bezug, bezugQuelle, bezugRoh });
  }

  offen.sort((a, b) => new Date(a.zeit) - new Date(b.zeit));
  offen.uebersprungen = uebersprungen;
  offen.zuletzt = zuletzt;
  offen.laufend = laufendeMitTitel;
  return offen;
}

/* Antworten in einem Aufruf formulieren - wie bei den Kommentaren. Ein Aufruf
   für alle offenen Nachrichten, nicht einer je Nachricht. */
export async function antwortenFormulieren(nachrichten, zuletzt = [], laufend = []) {
  if (!nachrichten.length) return [];
  const hintergrund = zuletzt.length
    ? `\nZuletzt erschienen (nur als Hintergrund – daraus darfst du NICHT raten):\n${zuletzt.map((e) => `- ${e.wann} · ${e.art}: „${e.titel}“`).join("\n")}\n`
    : "";
  const live = laufend.length
    ? `\nAktuell laufende Stories – NUR diese kommen für eine Story-Antwort in Frage, Beiträge nicht:\n${laufend.map((e) => `- ${e.wann} · „${e.titel}“`).join("\n")}\n`
    : "";
  const user = `Beantworte die folgenden Direktnachrichten. „Bezug“ nennt die Story oder den Beitrag, auf den sich die Nachricht bezieht; „Verlauf“, was in derselben Unterhaltung davor stand.
${live}${hintergrund}
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
  /* Welche Stories gerade laufen, ist die zweite Quelle fuer die Zuordnung -
     und, wenn sie doch misslingt, die Grundlage fuer eine gezielte Rueckfrage
     statt einer allgemeinen. */
  const laufend = await ig.laufendeStories();
  const alle = offeneNachrichten(konversationen, ig.kontoId, ledger, Date.now(), laufend);
  for (const u of alle.uebersprungen || []) {
    if (u.grund !== "bereits behandelt") log(`  · Nachricht von @${u.von} „${u.text}“ → übersprungen (${u.grund})`);
  }
  const offen = alle.slice(0, CONFIG.postfach.maxJeLauf);
  if (!offen.length) return { unterhaltungen: konversationen.length, offen: 0, beantwortet: 0 };

  log(`Postfach: ${offen.length} offene Nachrichten in ${konversationen.length} Unterhaltungen`);
  /* Woher der Bezug kam, gehoert ins Log. Am 16.09. stand dort nur die
     Antwort - dass ihr der Bezug fehlte, war nicht zu sehen, und die Ursache
     musste im Nachhinein rekonstruiert werden. */
  for (const n of offen) log(`  · Bezug @${n.von}: ${n.bezugQuelle}${n.bezugRoh ? ` (${n.bezugRoh})` : ""}${n.bezug ? ` – ${n.bezug.slice(0, 90)}` : ""}`);
  log(`  · Laufende Stories: ${alle.laufend?.length || 0}`);
  const antworten = await antwortenFormulieren(offen, alle.zuletzt || [], alle.laufend || []);
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
