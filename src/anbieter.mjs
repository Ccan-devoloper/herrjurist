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

     1. Worst Case aus dem konfigurierten Hard Ceiling rechnen - nicht aus
        einer Schaetzung. Schaetzungen waren das Problem.
     2. Admission aus dem Topf des Zwecks. Passt der Worst Case nicht,
        startet der Aufruf nicht (fail closed).
     3. `gesendet()` unmittelbar vor dem Absenden. Ab hier gibt es kein Geld
        zurueck.
     4. Tatsaechliche Kosten buchen, Rest freigeben.
     5. Eine Telemetriezeile - auch wenn es schiefging.

   Wichtig und ausdruecklich: Der Hard Ceiling begrenzt die Kosten EINES
   Aufrufs. Dass die Summe aller Pflichtaufrufe eines Tages unter dem
   Tagesdeckel bleibt, folgt daraus NICHT - siehe tagesplanWorstCase().
   ========================================================================== */

import Anthropic from "@anthropic-ai/sdk";
import { CONFIG } from "./config.mjs";
import { obergrenzeUsd, preisAus, erfassen, erfassenStueck } from "./kosten.mjs";
import { exaktesProfil, kalibrierFamilie, bausteinHash } from "./profile.mjs";

/* --- Laufkontext ---------------------------------------------------------
   Ein Lauf ist ein Prozess; der Kontext ist Modulzustand wie das Budget
   selbst. Ohne ihn laeuft kein bezahlter Aufruf - auch nicht in einem
   Hilfsskript. */
let kontext = null;

export function kontextSetzen(neu) { kontext = neu; return kontext; }
export function kontextLesen() { return kontext; }
export function kontextLoeschen() { kontext = null; }

export class OhneKontext extends Error {
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

/** Grobe Schätzung der Eingabelänge - für den Worst Case reicht die Größenordnung. */
const eingabeSchaetzen = (params) => {
  const text = JSON.stringify(params?.system || "") + JSON.stringify(params?.messages || "");
  return Math.ceil(text.length / 3.5);
};

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
  const { budget, telemetrie } = kontext;
  const { profil, familie, maxTokens } = profilVon({ zweck, provider, modell, params, promptVersion, effort, denkmodus });
  const eingabeTokens = eingabeSchaetzen(params);
  const worstCase = obergrenzeUsd({ modell, maxTokens: maxTokens || 0, eingabeTokens });

  const roh = {
    purpose: zweck, bucket: null, slot, provider, model: modell, effort, thinkingMode: denkmodus,
    attempt, profileId: profil.id, calibrationFamily: familie, maxTokens,
  };

  let griff;
  try {
    griff = budget.zulassen(zweck, worstCase, { optional, pflichtName });
  } catch (e) {
    telemetrie?.aufruf({ ...roh, sent: false, reservedUsd: worstCase, actualUsd: 0, releasedUsd: 0, outcome: "abgelehnt", errorType: e.name, approved: false });
    throw e;
  }
  roh.bucket = griff.topf;
  roh.reservedUsd = griff.reservedUsd;
  roh.breakGlass = griff.breakGlass;

  try {
    griff.gesendet();
    const antwort = await senden();
    const usd = preis(antwort);
    griff.kosten(usd);
    const usage = antwort?.usage || {};
    griff.buchen(usd);
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
    const gesendet = griff.istGesendet();
    if (!gesendet) griff.freigeben();
    else griff.ungeklaert(e?.name || "Fehler nach dem Senden");
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
      /* Usage vereinheitlichen, damit Preis und Telemetrie dieselbe Sprache sprechen. */
      d.usage = {
        input_tokens: d.usage?.input_tokens || 0,
        output_tokens: d.usage?.output_tokens || 0,
        cache_read_input_tokens: d.usage?.input_tokens_details?.cached_tokens || 0,
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
  const { budget, telemetrie } = kontext;
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
    griff.gesendet();
    const ergebnis = await (senden || senderStandard)();
    griff.kosten(stueck);
    griff.buchen(stueck);
    erfassenStueck(stueck, zweck);
    telemetrie?.aufruf({ ...roh, sent: true, actualUsd: stueck, usd: stueck, releasedUsd: 0, outcome: "ok", approved: true });
    return ergebnis;
  } catch (e) {
    const gesendet = griff.istGesendet();
    if (!gesendet) griff.freigeben(); else griff.ungeklaert(e?.name || "Fehler nach dem Senden");
    telemetrie?.aufruf({ ...roh, sent: gesendet, spendUnknown: gesendet, actualUsd: gesendet ? null : 0, releasedUsd: gesendet ? 0 : stueck, outcome: gesendet ? "ungeklaert" : "nicht-gesendet", errorType: e?.name || "Fehler", approved: false });
    throw e;
  }
}

/**
 * Was das Pflichtprodukt eines Tages im Worst Case kostet - und ob der
 * Tagesdeckel das überhaupt tragen kann.
 *
 * Diese Zahl ist unbequem und gehört trotzdem ins Protokoll: Mit den heutigen
 * Hard Ceilings (Autor 16k, Prüfer 6k) liegt sie über dem Core-Deckel. Das
 * heißt NICHT, dass der Tag teuer wird - gemessen kostet er einen Bruchteil.
 * Es heißt, dass niemand VORHER garantieren kann, dass jeder Pflichtaufruf
 * stattfindet, wenn jeder von ihnen sein Ceiling ausschöpft.
 *
 * Die Kostenzusage bleibt hart. Die Verfügbarkeitszusage kann die Admission
 * allein nicht geben - dafür braucht es den freigegebenen Reservebestand.
 */
export function tagesplanWorstCase({ posten = [], deckelCore = 0.32 }) {
  const einzeln = posten.map((p) => ({ ...p, worstCase: obergrenzeUsd({ modell: p.modell, maxTokens: p.maxTokens, eingabeTokens: p.eingabeTokens || 0 }) }));
  const summe = Math.round(einzeln.reduce((a, p) => a + p.worstCase, 0) * 1e6) / 1e6;
  return {
    posten: einzeln,
    summe,
    deckelCore,
    dailyPlanNotWorstCaseFundable: summe > deckelCore,
    /* Bewusst als Signal benannt, nicht als Fehler: Es ist ein
       Kalibrierungs- und Verfügbarkeitshinweis, kein Grund, still den
       Deckel anzuheben. */
    hinweis: summe > deckelCore
      ? `Worst Case des Pflichtprodukts ${summe.toFixed(4)} $ über dem Core-Deckel ${deckelCore.toFixed(2)} $ - `
        + `die Kostenzusage hält, eine Verfügbarkeitszusage gibt es damit nicht.`
      : "",
  };
}
