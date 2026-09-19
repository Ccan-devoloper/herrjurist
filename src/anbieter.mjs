/* ==========================================================================
   Die einzige Tür zu einem bezahlten Anbieter.

   Vorher lagen die Aufrufe verstreut: `client().messages.create(...)` in
   autor.mjs, in faktencheck.mjs, in interaktion.mjs, dazu zwei fetch() an
   OpenAI. Jede dieser Stellen musste selbst daran denken, vorher das Budget
   zu fragen - und an sechs von ihnen hat es das nicht getan. Ein
   Schema-Fallback, eine Fortsetzung, eine Zweitmeinung: alles bezahlte
   Aufrufe, von denen der Deckel nichts wusste.

   Deshalb gibt es jetzt genau eine Stelle, an der ein Anbieter angesprochen
   wird. Wer bezahlen will, kommt hier durch - oder gar nicht. Ein Test
   prueft, dass ausserhalb dieser Datei kein Anbieter-Einstiegspunkt mehr
   vorkommt; das ist der eigentliche Beweis, nicht die Aufzaehlung der sechs
   bekannten Stellen.

   Was hier bei JEDEM Aufruf passiert:

     1. Admission Reserve rechnen: Ausgabe aus dem konfigurierten Hard
        Ceiling, Eingabe aus admissionBound() - dem groesseren aus
        konservativem clientInputBound ueber den GESENDETEN Request und dem
        Zaehlwert des Anbieters. Beides ist konservativ; was der Anbieter
        zusaetzlich injiziert und berechnet, erfasst es nicht - es steht in
        keinem Koerper, den wir vorher wiegen koennen (Belege in
        eingabe.mjs). Ein bewiesener Provider-Worst-Case ist das nicht;
        dafuer liegt der Provider-Guard unter dem Policy cap, und dahinter
        prueft die Invariante.
     2. Admission aus dem Topf des Zwecks. Passt die Reserve nicht,
        startet der Aufruf nicht (fail closed).
     3. `gesendet()` unmittelbar vor dem Absenden. Ab hier gibt es kein Geld
        zurueck.
     4. Tatsaechliche Kosten buchen, Rest freigeben.
     5. Eine Telemetriezeile - auch wenn es schiefging.

   Wichtig und ausdruecklich: Das Ceiling begrenzt die AUSGABE eines
   Aufrufs. Dass die Summe aller Pflichtaufrufe eines Tages unter dem
   Tagesdeckel bleibt, folgt daraus NICHT - siehe
   tagesplanAdmissionBedarf().
   ========================================================================== */

import Anthropic from "@anthropic-ai/sdk";
import { CONFIG } from "./config.mjs";
import { admissionReserveUsd, preisAus, erfassen, erfassenStueck } from "./kosten.mjs";
import { InvarianteVerletzt } from "./budget.mjs";
import { KostenKontrollFehler } from "./kostenfehler.mjs";
import { admissionBound, clientInputBound, zaehlKoerper } from "./eingabe.mjs";
import { exaktesProfil, kalibrierFamilie, bausteinHash } from "./profile.mjs";

/* --- Laufkontext ---------------------------------------------------------
   Ein Lauf ist ein Prozess; der Kontext ist Modulzustand wie das Budget
   selbst. Ohne ihn laeuft kein bezahlter Aufruf - auch nicht in einem
   Hilfsskript. */
let kontext = null;

export function kontextSetzen(neu) { kontext = neu; return kontext; }
export function kontextLesen() { return kontext; }
export function kontextLoeschen() { kontext = null; }

export class OhneKontext extends KostenKontrollFehler {
  constructor(zweck) {
    super(`Bezahlter Aufruf „${zweck}“ ohne Laufkontext: Es gibt kein Budget, aus dem er zugelassen werden könnte. `
      + `Wer einen Anbieter ruft, muss vorher kontextSetzen({ budget, telemetrie, kanal, datum }) aufrufen.`);
    this.name = "OhneKontext";
  }
}

/* maxRetries: 0 ist Absicht. Das SDK wiederholt sonst bei 429 und 5xx von
   sich aus - das sind weitere Anbieteraufrufe, von denen keine Zulassung
   etwas wuesste. Wiederholungen sind Sache des Aufrufers, mit eigener
   Admission. Der Preis dafuer ist weniger Nachsicht bei kurzen Stoerungen;
   ein stiller Mehrverbrauch waere teurer. */
const anthropic = () => new Anthropic({ maxRetries: 0, timeout: 10 * 60 * 1000 });
let klient = null;
const client = () => (klient ||= anthropic());
export function klientSetzen(k) { klient = k; }   /* nur für Tests */

/* Der Zählendpunkt von Anthropic. Kostenlos, eigenes Ratenlimit - und der
   einzige Weg, die Eingabetoken zu erfassen, die Anthropic bei Structured
   Outputs selbst hinzufügt und berechnet (Belege in eingabe.mjs). Übergeben
   wird der VOLLSTÄNDIGE unterstützte Anfragekörper, nicht eine gepflegte
   Teilmenge: Die kleine Teilmenge war der Fehler, durch den tools und Schema
   aus der alten Rechnung fielen.

   Scheitert er, läuft der Aufruf mit der clientseitigen Schranke weiter. Das
   ist kein Freibrief - die Schranke deckt den injizierten Prompt nicht ab -,
   sondern der Grund, warum darüber der Provider-Guard liegt.

   Abschaltbar mit IG_TOKEN_ZAEHLEN=false, falls das Ratenlimit drückt. */
const zaehlenAktiv = () => String(process.env.IG_TOKEN_ZAEHLEN || "") !== "false";

async function eingabeZaehlen(params) {
  if (!zaehlenAktiv()) return null;
  const koerper = zaehlKoerper(params);
  if (!koerper) return null;
  const c = client();
  if (typeof c?.messages?.countTokens !== "function") return null;
  try {
    const r = await c.messages.countTokens(koerper);
    const n = Number(r?.input_tokens);
    return Number.isFinite(n) ? n : null;
  } catch { return null; }
}

function profilVon({ zweck, provider, modell, params, promptVersion, effort, denkmodus }) {
  const schemaHash = bausteinHash(params?.output_config?.format?.schema || params?.text?.format || null);
  const systemHash = bausteinHash(params?.system || params?.instructions || null);
  const werkzeugHash = bausteinHash(params?.tools || null);
  const maxTokens = params?.max_tokens ?? params?.max_output_tokens ?? null;
  const profil = exaktesProfil({ zweck, provider, modell, effort, denkmodus, systemHash, schemaHash, werkzeugHash, promptVersion, maxTokens });
  return { profil, familie: kalibrierFamilie({ zweck, modell, effort, schemaVersion: schemaHash.slice(0, 6) }), maxTokens };
}

/**
 * Der gemeinsame Ablauf aller Anbieter. `senden` bekommt den Griff und macht
 * genau einen Anbieteraufruf.
 */
async function durchDieTuer({ zweck, provider, modell, params, attempt, slot, optional, pflichtName, effort, denkmodus, promptVersion, senden, preis }) {
  if (!kontext?.budget) throw new OhneKontext(zweck);
  const { budget, telemetrie, journal } = kontext;
  const { profil, familie, maxTokens } = profilVon({ zweck, provider, modell, params, promptVersion, effort, denkmodus });
  /* Die Ausgabeseite ist gedeckelt (das Ceiling erzwingt der Anbieter). Die
     Eingabeseite ist ein konservativer clientInputBound über den gesendeten
     Request, angehoben durch den Zählwert des Anbieters, wo es ihn gibt -
     nicht mehr chars/3.5, aber ohne die Token, die der Anbieter selbst
     hinzufügt und berechnet (eingabe.mjs sagt, warum). Zusammen ergeben sie
     die Admission Reserve, nicht eine bewiesene Kostenobergrenze. */
  const clientBound = clientInputBound(params);
  const gezaehlt = provider === "anthropic" ? await eingabeZaehlen(params) : null;
  const eingabeTokens = admissionBound(params, gezaehlt);
  const admissionReserve = admissionReserveUsd({ modell, maxTokens: maxTokens || 0, eingabeTokens });

  const roh = {
    purpose: zweck, bucket: null, slot, provider, model: modell, effort, thinkingMode: denkmodus,
    attempt, profileId: profil.id, calibrationFamily: familie, maxTokens,
    clientInputBoundTokens: clientBound, providerCountTokens: gezaehlt,
    admissionBoundTokens: eingabeTokens,
  };

  let griff;
  try {
    griff = budget.zulassen(zweck, admissionReserve, { optional, pflichtName });
  } catch (e) {
    telemetrie?.aufruf({ ...roh, sent: false, reservedUsd: admissionReserve, actualUsd: 0, releasedUsd: 0, outcome: "abgelehnt", errorType: e.name, approved: false });
    throw e;
  }
  roh.bucket = griff.topf;
  roh.reservedUsd = griff.reservedUsd;
  roh.breakGlass = griff.breakGlass;

  /* Schritt 1 der Durability: Die Reservierung muss den Lauf ueberdauern,
     BEVOR der Anbieter sie zu sehen bekommt. Wird sie nicht durable, findet
     der Aufruf nicht statt - fail closed. */
  let reservierung = null;
  if (journal) {
    try {
      reservierung = await journal.reservieren({ bucket: griff.topf, purpose: zweck, attempt, reservedUsd: griff.reservedUsd, slot });
    } catch (e) {
      griff.freigeben();
      telemetrie?.aufruf({ ...roh, sent: false, actualUsd: 0, releasedUsd: griff.reservedUsd, outcome: "abgelehnt", errorType: e.name, approved: false });
      throw e;
    }
  }
  roh.reservationId = reservierung;

  try {
    /* Schritt 2: der Sendevermerk, unmittelbar vor dem Absenden. Erst er
       macht spaeter unterscheidbar, ob ein Absturz vor oder nach dem Senden
       kam. Scheitert er, ist nichts gesendet - der Fehler faellt in den
       catch, und dort gibt istGesendet() korrekt false zurueck. */
    if (journal && reservierung) await journal.senden(reservierung);
    griff.gesendet();
    const antwort = await senden();
    const usd = preis(antwort);
    griff.kosten(usd);
    const usage = antwort?.usage || {};
    griff.buchen(usd);
    journal?.abrechnen(reservierung, usd);
    telemetrie?.aufruf({
      ...roh, sent: true, actualUsd: usd, usd,
      releasedUsd: Math.max(0, Math.round((griff.reservedUsd - usd) * 1e6) / 1e6),
      inputTokens: usage.input_tokens ?? usage.input_tokens_details?.total ?? null,
      outputTokens: usage.output_tokens ?? null,
      cacheReadTokens: usage.cache_read_input_tokens ?? null,
      cacheWriteTokens: usage.cache_creation_input_tokens ?? null,
      serverToolUsage: usage.server_tool_use ?? null,
      stopReason: antwort?.stop_reason ?? antwort?.status ?? null,
      outcome: "ok", approved: true,
    });
    return antwort;
  } catch (e) {
    /* Eine Invariantenverletzung ist das Gegenteil eines ungeklaerten Falls:
       Die Usage lag vor, die Kosten sind gebucht, der Topf ist gesperrt. Sie
       als „Kosten unbekannt“ zu protokollieren wuerde die eine Zeile
       unbrauchbar machen, die hinterher erklaert, was schiefging. */
    if (e instanceof InvarianteVerletzt) {
      journal?.abrechnen(reservierung, e.tatsaechlich);
      telemetrie?.aufruf({
        ...roh, sent: true, spendUnknown: false,
        actualUsd: e.tatsaechlich, usd: e.tatsaechlich, releasedUsd: 0,
        outcome: "invariant_violation", errorType: e.name, approved: false,
      });
      throw e;
    }
    /* Ein explizites HTTP 400 ist kein ungeklärter Providerverbrauch:
       Der Anbieter hat die Anfrage als ungültig zurückgewiesen, bevor ein
       Modelllauf/Usage entstehen konnte. Am 19.09. hat der Faktencheck danach
       korrekt mit seinem schemafreien Fallback weitergemacht, das Journal
       hielt die 400er-Reservierung aber trotzdem als „ungeklärt verbraucht“
       fest und blockierte so echte Pflichtarbeit. 400 wird deshalb mit 0 $
       abgerechnet; Netzabbrüche/5xx bleiben weiterhin konservativ ungeklärt. */
    if (Number(e?.status) === 400) {
      griff.kosten(0);
      griff.buchen(0);
      journal?.abrechnen(reservierung, 0);
      telemetrie?.aufruf({
        ...roh, sent: true, spendUnknown: false, actualUsd: 0, usd: 0,
        releasedUsd: griff.reservedUsd, outcome: "provider_rejected_400",
        errorType: e?.name || "HTTP400", approved: false,
      });
      throw e;
    }
    const gesendet = griff.istGesendet();
    if (!gesendet) { griff.freigeben(); journal?.verfallen(reservierung, e?.name || "vor dem Senden abgebrochen"); }
    else { griff.ungeklaert(e?.name || "Fehler nach dem Senden"); journal?.ungeklaert(reservierung, e?.name || "Fehler nach dem Senden"); }
    telemetrie?.aufruf({
      ...roh, sent: gesendet, spendUnknown: gesendet, actualUsd: gesendet ? null : 0,
      releasedUsd: gesendet ? 0 : griff.reservedUsd,
      outcome: gesendet ? "ungeklaert" : "nicht-gesendet", errorType: e?.name || String(e?.message || e).slice(0, 80), approved: false,
    });
    throw e;
  }
}

/** Ein Claude-Aufruf. Jeder Versuch, jeder Fallback ruft das hier selbst auf. */
export async function claudeAufruf({ zweck, params, modell = null, attempt = 1, slot = null, optional = false, pflichtName = null, promptVersion = "1" }) {
  const m = modell || params.model;
  const antwort = await durchDieTuer({
    zweck, provider: "anthropic", modell: m, params, attempt, slot, optional, pflichtName,
    effort: params?.output_config?.effort ?? null,
    denkmodus: params?.thinking?.type ?? null,
    promptVersion,
    senden: () => client().messages.create(params),
    preis: (a) => preisAus(m, a?.usage),
  });
  /* Die alte Kostenerfassung bleibt, solange Bericht und Schätzungen darauf
     stehen - sie zählt dieselbe Zahl ein zweites Mal für die Tagesdatei. */
  erfassen(m, antwort?.usage, zweck);
  return antwort;
}

/** Ein OpenAI-Aufruf (Prüfer). */
export async function openaiAufruf({ zweck, params, modell, attempt = 1, slot = null, url = "https://api.openai.com/v1/responses", fetchFn = fetch, promptVersion = "1" }) {
  const antwort = await durchDieTuer({
    zweck, provider: "openai", modell, params, attempt, slot, optional: false, pflichtName: null,
    effort: params?.reasoning?.effort ?? null, denkmodus: null, promptVersion,
    senden: async () => {
      const r = await fetchFn(url, {
        method: "POST",
        headers: { "content-type": "application/json", authorization: `Bearer ${process.env.OPENAI_API_KEY}` },
        body: JSON.stringify(params),
      });
      if (!r.ok) throw new Error(`OpenAI ${r.status}: ${(await r.text()).slice(0, 200)}`);
      const d = await r.json();
      /* Usage vereinheitlichen, damit Preis und Telemetrie dieselbe Sprache
         sprechen - und dabei der Unterschied zwischen den Anbietern:

           Anthropic  input_tokens zaehlt NUR die ungecachten Token;
                      cache_read und cache_creation stehen daneben.
           OpenAI     input_tokens ist die GESAMTZAHL, cached_tokens ist eine
                      TEILMENGE davon.

         Wer das gleichsetzt, bezahlt den gecachten Anteil zweimal - einmal
         zum vollen, einmal zum Cachepreis. Das erzeugt keinen Overspend (die
         Zahl ist zu hoch, nicht zu niedrig), blockiert aber unnoetig Budget
         und verfaelscht Telemetrie und Kalibrierung. */
      const gesamtEin = d.usage?.input_tokens || 0;
      const gecacht = Math.min(gesamtEin, d.usage?.input_tokens_details?.cached_tokens || 0);
      d.usage = {
        input_tokens: Math.max(0, gesamtEin - gecacht),
        output_tokens: d.usage?.output_tokens || 0,
        cache_read_input_tokens: gecacht,
        cache_creation_input_tokens: 0,
      };
      return d;
    },
    preis: (a) => preisAus(modell, a?.usage),
  });
  erfassen(modell, antwort?.usage, zweck);
  return antwort;
}

/**
 * Ein erzeugtes Bild. Der Preis steht pro Stück fest, das Ceiling ist hier
 * keine Token-, sondern eine Stückgrenze.
 */
export async function bildAufruf({ zweck = "bild", auftrag = null, senden = null, preisUsd = null, slot = null, optional = true, modell = "gpt-image-1-mini", zeitlimitMs = 120000, url = "https://api.openai.com/v1/images/generations", fetchFn = fetch }) {
  if (!kontext?.budget) throw new OhneKontext(zweck);
  const { budget, telemetrie, journal } = kontext;
  const stueck = preisUsd ?? CONFIG.bilder?.ki?.preisUsd ?? 0.01;
  const roh = { purpose: zweck, provider: "openai", model: modell, attempt: 1, slot, maxTokens: null, profileId: `${zweck}:stueck`, calibrationFamily: `${zweck} / ${modell} / - / stueck` };

  let griff;
  try {
    griff = budget.zulassen(zweck, stueck, { optional });
  } catch (e) {
    telemetrie?.aufruf({ ...roh, bucket: null, sent: false, reservedUsd: stueck, actualUsd: 0, releasedUsd: 0, outcome: "abgelehnt", errorType: e.name, approved: false });
    throw e;
  }
  roh.bucket = griff.topf; roh.reservedUsd = griff.reservedUsd; roh.breakGlass = griff.breakGlass;
  let reservierung = null;
  if (journal) {
    try {
      reservierung = await journal.reservieren({ bucket: griff.topf, purpose: zweck, attempt: 1, reservedUsd: griff.reservedUsd, slot });
    } catch (e) {
      griff.freigeben();
      telemetrie?.aufruf({ ...roh, sent: false, actualUsd: 0, releasedUsd: griff.reservedUsd, outcome: "abgelehnt", errorType: e.name, approved: false });
      throw e;
    }
  }
  roh.reservationId = reservierung;
  /* Ohne eigene Sendefunktion macht die Tuer den Aufruf selbst - der
     Endpunkt gehoert hierher, damit es ausserhalb keinen zweiten gibt. */
  const senderStandard = async () => {
    const steuerung = new AbortController();
    const wecker = setTimeout(() => steuerung.abort(), zeitlimitMs);
    try {
      const r = await fetchFn(url, {
        method: "POST",
        headers: { Authorization: `Bearer ${auftrag?.key || ""}`, "Content-Type": "application/json" },
        body: JSON.stringify(auftrag?.koerper || {}),
        signal: steuerung.signal,
      });
      if (!r.ok) throw new Error(`HTTP ${r.status}: ${(await r.text().catch(() => "")).slice(0, 200)}`);
      return await r.json();
    } finally { clearTimeout(wecker); }
  };

  try {
    if (journal && reservierung) await journal.senden(reservierung);
    griff.gesendet();
    const ergebnis = await (senden || senderStandard)();
    griff.kosten(stueck);
    griff.buchen(stueck);
    journal?.abrechnen(reservierung, stueck);
    erfassenStueck(stueck, zweck);
    telemetrie?.aufruf({ ...roh, sent: true, actualUsd: stueck, usd: stueck, releasedUsd: 0, outcome: "ok", approved: true });
    return ergebnis;
  } catch (e) {
    if (e instanceof InvarianteVerletzt) {
      journal?.abrechnen(reservierung, e.tatsaechlich);
      telemetrie?.aufruf({ ...roh, sent: true, spendUnknown: false, actualUsd: e.tatsaechlich, usd: e.tatsaechlich, releasedUsd: 0, outcome: "invariant_violation", errorType: e.name, approved: false });
      throw e;
    }
    const gesendet = griff.istGesendet();
    if (!gesendet) { griff.freigeben(); journal?.verfallen(reservierung, e?.name || "vor dem Senden abgebrochen"); }
    else { griff.ungeklaert(e?.name || "Fehler nach dem Senden"); journal?.ungeklaert(reservierung, e?.name || "Fehler nach dem Senden"); }
    telemetrie?.aufruf({ ...roh, sent: gesendet, spendUnknown: gesendet, actualUsd: gesendet ? null : 0, releasedUsd: gesendet ? 0 : stueck, outcome: gesendet ? "ungeklaert" : "nicht-gesendet", errorType: e?.name || "Fehler", approved: false });
    throw e;
  }
}

/**
 * Was das Pflichtprodukt eines Tages an ADMISSION verlangen würde - und ob
 * der Tagesdeckel das überhaupt trägt.
 *
 * Ausdrücklich KEIN Provider-Worst-Case, und der Name sagt das jetzt auch.
 * Zwei Gründe:
 *
 *   - Die Eingabezahlen sind PLANUNGSWERTE. Zum Zeitpunkt der Planung gibt
 *     es die Anfragen noch nicht, also auch keine Schranke über ihre Bytes.
 *   - Und selbst mit echten Anfragen wäre die Summe kein bewiesener
 *     Höchstpreis, sondern die Summe konservativer Admissionwerte.
 *
 * Die Zahl ist trotzdem unbequem und gehört ins Protokoll: Mit den heutigen
 * Ceilings liegt sie weit über dem Core-Deckel. Das heißt nicht, dass der
 * Tag teuer wird - gemessen kostet er einen Bruchteil. Es heißt, dass
 * niemand vorher sagen kann, dass jeder Pflichtaufruf zugelassen wird, wenn
 * jeder seine Reserve in voller Höhe anmeldet.
 *
 * Die Verfügbarkeitszusage kann die Admission allein ohnehin nicht geben -
 * dafür braucht es den Reservebestand.
 */
export function tagesplanAdmissionBedarf({ posten = [], deckelCore = 0.32 }) {
  const einzeln = posten.map((p) => ({ ...p, admissionReserve: admissionReserveUsd({ modell: p.modell, maxTokens: p.maxTokens, eingabeTokens: p.eingabeTokens || 0 }) }));
  const summe = Math.round(einzeln.reduce((a, p) => a + p.admissionReserve, 0) * 1e6) / 1e6;
  return {
    posten: einzeln,
    summe,
    deckelCore,
    /* Der Name hiess bis RC4 dailyPlanNotWorstCaseFundable. Er behauptete
       einen Provider-Worst-Case, der es nie war: Die Eingabezahlen sind
       Planungswerte, und die Summe ist eine Summe von Admissionwerten. Ein
       Signal, dessen Name mehr verspricht als die Zahl, ist ein schlechtes
       Signal - auch wenn der alte Name aus der ursprünglichen Anforderung
       stammt. */
    dailyPlanNotAdmissibleAtCap: summe > deckelCore,
    /* Bewusst als Signal benannt, nicht als Fehler: Es ist ein
       Kalibrierungs- und Verfügbarkeitshinweis, kein Grund, still den
       Deckel anzuheben. */
    basis: "planungswerte",
    hinweis: summe > deckelCore
      ? `Admissionbedarf des Pflichtprodukts ${summe.toFixed(4)} $ (aus Planungswerten) über dem Core-Deckel ${deckelCore.toFixed(2)} $ - `
        + `jeder einzelne Aufruf wird weiter gegen die Betriebsgrenze geprüft, eine Verfügbarkeitszusage gibt es damit nicht.`
      : "",
  };
}
