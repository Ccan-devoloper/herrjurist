/* ==========================================================================
   Wie viel Eingabe ein Aufruf HÖCHSTENS hat.

   Bisher stand hier eine Schätzung: die Länge des serialisierten Prompts
   geteilt durch 3,5. Das war bequem und falsch. Falsch nicht, weil die Zahl
   meistens danebenlag - meistens lag sie ordentlich -, sondern weil auf ihr
   eine Zusage stand, die sie nicht tragen kann:

     - 3,5 Zeichen je Token gilt für deutschen Fließtext. Für dichten JSON,
       für Tabellen, für Paragraphenzeichen, für Emoji, für kyrillische oder
       japanische Zeichen gilt es nicht; dort sind es schnell 1,5 oder 1.
     - `tools` fehlten in der Rechnung komplett. Ein Werkzeugschema ist
       Eingabe und kostet Eingabepreis.
     - Das Structured-Output-Schema fehlte ebenso.
     - Und der Aufschlag von 15 % war gesetzt, nicht bewiesen.

   Eine Admission, die auf einer Schätzung steht, hält nur so lange, wie die
   Schätzung stimmt. Genau das war der Fehler vom 18.09., eine Ebene tiefer.

   Deshalb hier eine BEWEISBARE obere Schranke statt einer Schätzung.

   Der Satz, auf dem sie steht:

     Anthropic und OpenAI tokenisieren beide mit byte-level BPE. Jedes Token
     des Vokabulars dekodiert zu mindestens EINEM Byte. Also dekodieren n
     Token zu mindestens n Bytes; also kodiert eine Folge von b Bytes zu
     HÖCHSTENS b Token.

   Wir zählen die UTF-8-Bytes der vollständigen serialisierten Anfrage. Das
   ist großzügig - die JSON-Syntax (Anführungszeichen, Klammern,
   Feldnamen) zählt mit, und die ist im Ergebnis kein Text, sondern Struktur.
   Großzügig in die sichere Richtung ist genau das, was eine Vorabzusage
   braucht.

   Was der Satz NICHT abdeckt, und was deshalb als Pauschale dazukommt:
   Sondertoken, die die API selbst um jede Nachricht legt (Rollenmarken,
   Trenner). Sie dekodieren zu null Inhaltsbytes. Dafür steht OVERHEAD_JE_-
   NACHRICHT - reichlich bemessen, es geht um einstellige Zahlen je Nachricht.

   Grenzen dieser Schranke, ausdrücklich:

     - Für serverseitige Werkzeuge (Websuche) gilt sie nicht: Deren Ergebnisse
       kommen NACH dem Absenden in den Verlauf und stehen in keiner Anfrage,
       die wir vorher wiegen könnten. Der Research-Topf sagt deshalb die Zahl
       der Anfragen und Suchen zu, nicht den Cent - so steht es dort, und so
       bleibt es.
     - Sie ist lose: typisch das Drei- bis Vierfache der echten Tokenzahl. Das
       kostet Spielraum im Topf. Ein Deckel, der hält, ist das wert.
   ========================================================================== */

/** Sondertoken je Nachricht (Rollenmarke, Trenner). Reichlich bemessen. */
export const OVERHEAD_JE_NACHRICHT = 8;
/** Feste Pauschale je Anfrage (Systemrahmen, Abschlussmarken). */
export const OVERHEAD_FEST = 64;

const byteLaenge = (s) => (typeof Buffer !== "undefined"
  ? Buffer.byteLength(s, "utf8")
  : new TextEncoder().encode(s).length);

/**
 * Die obere Schranke der Eingabetoken EINER Anfrage.
 *
 * Bewusst über die GESAMTE Anfrage, nicht über ausgewählte Felder: Wer
 * einzelne Felder aufzählt, vergisst beim nächsten Feature eines - `tools`
 * und das Schema waren genau so verlorengegangen.
 *
 * @param {object} params  der vollständige Anfragekörper
 * @returns {number} Tokenobergrenze (ganzzahlig)
 */
export function eingabeObergrenzeTokens(params) {
  if (!params || typeof params !== "object") return OVERHEAD_FEST;
  let roh;
  try { roh = JSON.stringify(params); } catch { roh = String(params); }
  const bytes = byteLaenge(roh ?? "");
  const nachrichten = Array.isArray(params.messages) ? params.messages.length
    : Array.isArray(params.input) ? params.input.length : 1;
  return bytes + OVERHEAD_JE_NACHRICHT * nachrichten + OVERHEAD_FEST;
}

/**
 * Nimmt die beweisbare Schranke und, falls vorhanden, das Ergebnis des
 * Zählendpunkts - und nimmt den GRÖSSEREN Wert.
 *
 * Warum nicht den kleineren, wo der Zähler doch genauer ist: Anthropic
 * bezeichnet `count_tokens` selbst als Schätzung. Eine Schätzung darf eine
 * bewiesene Schranke ergänzen, nicht sie unterbieten - sonst steht die Zusage
 * wieder auf dem Wort eines Dritten. Liegt der Zähler über der Schranke, ist
 * entweder unsere Annahme falsch oder die Anfrage ungewöhnlich; in beiden
 * Fällen ist die größere Zahl die richtige.
 */
export function eingabeGrenze(params, gezaehlt = null) {
  const schranke = eingabeObergrenzeTokens(params);
  const z = Number(gezaehlt);
  return Number.isFinite(z) && z > schranke ? Math.ceil(z) : schranke;
}
