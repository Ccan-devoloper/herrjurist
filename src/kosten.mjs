/* Verbrauch der Claude API mitschreiben (für den Wochenbericht). */
const PREISE = {
  "claude-opus-5": { ein: 5, aus: 25, cacheLesen: 0.5, cacheSchreiben: 6.25 },
  "claude-sonnet-5": { ein: 2, aus: 10, cacheLesen: 0.2, cacheSchreiben: 2.5 },
  "claude-opus-4-8": { ein: 5, aus: 25, cacheLesen: 0.5, cacheSchreiben: 6.25 },
  "claude-haiku-4-5": { ein: 1, aus: 5, cacheLesen: 0.1, cacheSchreiben: 1.25 },
  "claude-haiku-4-5-20251001": { ein: 1, aus: 5, cacheLesen: 0.1, cacheSchreiben: 1.25 },
};

const posten = [];

/* --- Tagesdeckel -------------------------------------------------------
   Vor jedem Claude-Aufruf wird geprüft, ob der Tagesverbrauch (bisherige
   Läufe des Tages + dieser Lauf) unter der Grenze liegt. Ist sie erreicht,
   wirft budgetPruefen() einen BudgetFehler – der Rest wartet bis morgen. */
let limitUsd = Infinity, vorbelastung = 0, speichern = null;
/* Für das Reel des Tages zurückgelegter Betrag. Alle anderen Aufrufe hören
   entsprechend früher auf, damit das Reel am Abend noch geschrieben werden
   kann – es soll täglich erscheinen. */
let reserviert = 0, reserviertFuer = "";

export class BudgetFehler extends Error {}

export function budgetSetzen(opt = {}) {
  limitUsd = opt.limitUsd ?? Infinity;
  vorbelastung = opt.bisher ?? 0;
  speichern = opt.speichern ?? null;
  reserviert = opt.reserviert ?? 0;
  reserviertFuer = (opt.reserviertFuer ?? "reel").toLowerCase();
}

/* Hebt die Rücklage auf, sobald das Reel steht (oder feststeht, dass heute
   keines mehr kommt). Danach darf der Rest des Tages sie ausschöpfen. */
export function reservieren(betrag, fuer = "reel") { reserviert = Math.max(0, Number(betrag) || 0); reserviertFuer = String(fuer).toLowerCase(); }
export function reservierungAufheben() { reserviert = 0; }
export const reservierung = () => reserviert;

export const tagesStand = () => vorbelastung + summe();
export const tagesLimit = () => limitUsd;
/* Kleine Reserve: ein Aufruf kostet 0,02–0,05 $, so bleibt der Deckel praktisch eingehalten. */
const RESERVE = 0.02;
const darfReserve = (zweck) => Boolean(reserviertFuer) && String(zweck).toLowerCase().includes(reserviertFuer);
export const budgetFrei = (zweck = "") => tagesStand() + RESERVE + (darfReserve(zweck) ? 0 : reserviert) < limitUsd;

export function budgetPruefen(zweck = "Claude-Aufruf") {
  if (budgetFrei(zweck)) return;
  const rest = reserviert && !darfReserve(zweck) ? ` (davon ${reserviert.toFixed(2)} $ für das Reel zurückgelegt)` : "";
  throw new BudgetFehler(`Tagesbudget erreicht (${tagesStand().toFixed(3)} $ von ${limitUsd.toFixed(2)} $)${rest} – ${zweck} wartet bis morgen.`);
}

export function erfassen(modell, usage, zweck = "") {
  if (!usage) return 0;
  const p = PREISE[modell] || PREISE["claude-opus-5"];
  const usd = ((usage.input_tokens || 0) * p.ein + (usage.output_tokens || 0) * p.aus + (usage.cache_read_input_tokens || 0) * p.cacheLesen + (usage.cache_creation_input_tokens || 0) * p.cacheSchreiben) / 1e6;
  posten.push({ modell, zweck, usd, ein: usage.input_tokens || 0, aus: usage.output_tokens || 0, cache: usage.cache_read_input_tokens || 0 });
  const k = (n) => (n >= 1000 ? `${(n / 1000).toFixed(1)}k` : String(n));
  console.log(`  $ ${usd.toFixed(4)} ${zweck || modell} · ${k(usage.input_tokens || 0)} ein / ${k(usage.output_tokens || 0)} aus / ${k(usage.cache_read_input_tokens || 0)} Cache`);
  if (speichern) { try { speichern(tagesStand(), posten.length, jeZweck()); } catch (e) { console.warn(`  ! Kosten nicht gespeichert: ${e.message}`); } }
  return usd;
}

/** Kosten dieses Laufs je Zweck (z. B. recherche, beitrag, faktencheck). */
export function jeZweck() {
  const m = {};
  for (const p of posten) m[p.zweck || p.modell] = (m[p.zweck || p.modell] || 0) + p.usd;
  return m;
}

export function summe() {
  return posten.reduce((a, b) => a + b.usd, 0);
}

export function abschluss() {
  return { usd: summe(), aufrufe: posten.length, cacheAnteil: posten.length ? posten.reduce((a, b) => a + b.cache, 0) / Math.max(1, posten.reduce((a, b) => a + b.ein + b.cache, 0)) : 0, posten: [...posten] };
}
