/* ==========================================================================
   Wie viel Eingabe ein Aufruf kostet - und was daran zugesagt werden kann.

   Die erste Fassung stand auf einer Schätzung: Promptlänge geteilt durch 3,5.
   Die zweite ersetzte sie durch eine Byte-Schranke und nannte sie einen
   Beweis. Der Beweis trägt nicht, und das ist wichtiger als die Schranke.

   WAS DIE BYTE-SCHRANKE KANN
   Beide Anbieter tokenisieren mit byte-level BPE; ein Token dekodiert zu
   mindestens einem Byte, also kodieren b Bytes zu höchstens b Token. Das ist
   eine belastbare Überlegung - ABER sie stützt sich auf eine Eigenschaft des
   Tokenizers, die kein Anbieter öffentlich zusichert, und sie begrenzt nur,
   was WIR senden.

   WAS SIE NICHT KANN - und das ist dokumentiert, nicht vermutet
   Anthropic schreibt zu Structured Outputs:

     „When using structured outputs, Claude automatically receives an
      additional system prompt explaining the expected output format. This
      means: Your input token count is slightly higher. The injected prompt
      costs you tokens like any other system prompt."
     (platform.claude.com/docs/en/build-with-claude/structured-outputs,
      Abschnitt „Prompt modification and token costs")

   Fast alle Core-Aufrufe hier benutzen Structured Outputs. Es gibt also
   berechnete Eingabetoken, die in unserem Anfragekörper nicht vorkommen.
   Damit erfasst die Byte-Schranke nicht, was der Anbieter zusaetzlich
   hinzufuegt und berechnet. Ein Satz, der daraus eine Obergrenze ALLER abgerechneten
   Eingabetoken macht, wäre damit falsch - und steht deshalb nirgends mehr.

   WAS DER ZÄHLENDPUNKT KANN
   `POST /v1/messages/count_tokens` nimmt denselben Anfragekörper an - laut
   API-Referenz messages, model, system, tools, tool_choice, thinking,
   output_config und cache_control. Er ist kostenlos und hat ein eigenes
   Ratenlimit. Mit output_config kann er den injizierten Systemprompt
   mitrechnen; wir übergeben deshalb ALLE unterstützten Felder, nicht eine
   gepflegte Teilmenge - die kleine Teilmenge war genau der Fehler, durch den
   tools und Schema aus der alten Rechnung fielen.

   Aber auch er ist keine Garantie. Anthropic sagt dazu selbst:

     „The token count is an estimate. In some cases, the actual number of
      input tokens used when creating a message might differ by a small
      amount."
     (platform.claude.com/docs/en/build-with-claude/token-counting)

   Eine dokumentierte MAXIMALE Abweichung gibt es nicht. „Small amount" ist
   keine Zahl, auf die man einen Deckel stellt.

   Für serverseitige Werkzeuge (Websuche) lehnt der Endpunkt die Anfrage
   ohnehin mit invalid_request_error ab - dort gibt es keinen Vorabwert, und
   deshalb sagt der Research-Topf die Zahl der Anfragen und Suchen zu, nicht
   den Cent.

   WAS DARAUS FOLGT
   Größen, die auseinandergehalten werden müssen - und zwar in ZWEI Einheiten.
   Sie zu vermischen ist der bequemste Weg, sich selbst zu täuschen:

     TOKEN
       clientInputBoundTokens   konservative Schranke über das, was wir senden
       providerCountTokens      vollständiger Zählwert, wo verfügbar
       admissionBoundTokens     max(beide) - die Eingabezahl, mit der gerechnet wird
       actualInputTokens        was der Anbieter hinterher meldet

     DOLLAR
       admissionReserveUsd      aus admissionBoundTokens und dem Ceiling
                                gerechnet - der reservierte Betrag
       actualUsd                was der Aufruf laut Usage gekostet hat

     Die KOSTENINVARIANTE ist eine Aussage über Dollar:

       invariantViolation   actualUsd > admissionReserveUsd

     Auf der Tokenebene gilt die entsprechende Aussage getrennt:

       actualInputTokens > admissionBoundTokens

     Beides kann unabhängig voneinander eintreten - die Tokenschranke kann
     halten, während der Dollarbetrag reißt (etwa bei einer Preisänderung),
     und umgekehrt.

   Und darüber, in richtlinie.mjs, die Trennung zwischen dem Policy-Deckel
   (0,32 $) und der operativen Admissiongrenze darunter. Der Abstand ist ein
   Guard gegen genau die Unschärfe, die oben dokumentiert ist - eine
   konservative Betriebsgrenze, kein Beweis. Ohne zugesicherte Maximal-
   abweichung oder einen anbieterseitigen Ausgabedeckel gibt es keinen.
   ========================================================================== */

/** Sondertoken je Nachricht (Rollenmarke, Trenner). Reichlich bemessen. */
export const OVERHEAD_JE_NACHRICHT = 8;
/** Feste Pauschale je Anfrage (Systemrahmen, Abschlussmarken). */
export const OVERHEAD_FEST = 64;

/**
 * Felder, die der Zählendpunkt laut API-Referenz annimmt. Die Liste steht
 * hier, damit ein neues Feld an EINER Stelle nachgetragen wird, statt an der
 * Aufrufstelle vergessen zu werden.
 */
export const ZAEHL_FELDER = Object.freeze([
  "model", "messages", "system", "tools", "tool_choice", "thinking",
  "output_config", "cache_control",
]);

const byteLaenge = (s) => (typeof Buffer !== "undefined"
  ? Buffer.byteLength(s, "utf8")
  : new TextEncoder().encode(s).length);

/**
 * Die konservative Schranke über den von UNS gesendeten Anfragekörper.
 *
 * Bewusst über die GESAMTE Anfrage, nicht über ausgewählte Felder: Wer Felder
 * aufzählt, vergisst beim nächsten Feature eines - `tools` und das Schema
 * waren genau so verlorengegangen.
 *
 * Sie begrenzt NICHT, was der Anbieter zusätzlich injiziert (siehe oben).
 *
 * @param {object} params  der vollständige Anfragekörper
 * @returns {number} Tokenschranke (ganzzahlig)
 */
export function clientInputBound(params) {
  if (!params || typeof params !== "object") return OVERHEAD_FEST;
  let roh;
  try { roh = JSON.stringify(params); } catch { roh = String(params); }
  const bytes = byteLaenge(roh ?? "");
  const nachrichten = Array.isArray(params.messages) ? params.messages.length
    : Array.isArray(params.input) ? params.input.length : 1;
  return bytes + OVERHEAD_JE_NACHRICHT * nachrichten + OVERHEAD_FEST;
}

/**
 * Baut den Körper für den Zählendpunkt: alle unterstützten Felder aus der
 * echten Anfrage, unverändert übernommen.
 *
 * `null`, wenn der Aufruf dort nicht zählbar ist - serverseitige Werkzeuge
 * (Websuche, Code-Ausführung) lehnt der Endpunkt ab.
 */
export function zaehlKoerper(params) {
  if (!params || typeof params !== "object") return null;
  const serverWerkzeug = (params.tools || []).some((t) => typeof t?.type === "string"
    && /^(web_search|web_fetch|code_execution|tool_search)/.test(t.type));
  if (serverWerkzeug) return null;
  const koerper = {};
  for (const feld of ZAEHL_FELDER) if (params[feld] !== undefined) koerper[feld] = params[feld];
  return koerper.model && koerper.messages ? koerper : null;
}

/**
 * Die OPERATIVE Eingabezahl fuer die Admission.
 *
 * Wenn der kostenlose Provider-Zaehler einen Wert liefert, ist er die
 * bessere Betriebsgrundlage: Er sieht den vollstaendigen Request inklusive
 * des fuer Structured Outputs injizierten Prompts. Die Bytezahl des JSON-
 * Koerpers ist dagegen nur eine absichtlich extrem grobe clientseitige
 * Schranke und lag am 19.09. bei langen Schemas so weit ueber der realen
 * Tokenzahl, dass ein 0,32-$-Tag trotz realer Kosten um wenige Cent schon vor
 * dem Senden blockiert wurde.
 *
 * Der Zaehler bleibt eine Schaetzung, also bekommt er 10 % plus 256 Token
 * Puffer. Das ist KEINE mathematische Garantie; genau fuer die verbleibende
 * Unschaerfe existieren Provider-Guard und die Dollar-Invariante. Faellt der
 * Zaehler aus oder ist fuer Server-Tools nicht verfuegbar, bleibt die
 * clientseitige Byte-Schranke der konservative Fallback.
 */
export const PROVIDER_COUNT_FAKTOR = 1.10;
export const PROVIDER_COUNT_PUFFER = 256;
export function admissionBound(params, providerCountEstimate = null) {
  /* Number(null) === 0. Ohne diese ausdrueckliche Abfrage wurde ein FEHLENDER
     Zaehlerwert deshalb am 19.09. zu 256 Token Admission statt zum
     clientseitigen Fallback. Das unterreservierte insbesondere OpenAI-Pfade. */
  if (providerCountEstimate !== null && providerCountEstimate !== undefined && providerCountEstimate !== "") {
    const z = Number(providerCountEstimate);
    if (Number.isFinite(z) && z >= 0) return Math.ceil(z * PROVIDER_COUNT_FAKTOR + PROVIDER_COUNT_PUFFER);
  }
  return clientInputBound(params);
}
