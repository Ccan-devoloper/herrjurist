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
  /* Beginn eines Laufs: Die Posten der bisherigen Läufe des Tages stecken in
     `bisher`, nicht in dieser Liste. Ohne das Leeren zählte ein zweiter Aufruf
     von budgetSetzen im selben Prozess die alten Posten doppelt. */
  posten.length = 0;
  for (const k of Object.keys(GEMESSEN)) delete GEMESSEN[k];
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

/* --- Was ein Aufruf kostet, bevor er läuft ------------------------------
   Geprüft wird vor dem Aufruf, gezählt danach. Eine pauschale Reserve von
   0,02 $ reichte deshalb nicht: Ein Reel-Aufruf kostet das Dreifache, und
   einzelne Tage lagen bis zu 16 % über dem Limit.

   Der Deckel wird jetzt vorab mit dem belastet, was ein Aufruf dieses Zwecks
   erfahrungsgemäß kostet. Die Werte stammen aus den Läufen der letzten Woche;
   wird ein Aufruf teurer als gedacht, rechnet der Rest des Laufs mit dem
   höheren Wert weiter. */
const ERWARTET = {
  "story-faktencheck": 0.01,
  "reel-faktencheck": 0.01,
  faktencheck: 0.01,
  recherche: 0.05,
  stories: 0.05,
  beitrag: 0.05,
  autor: 0.05,
  reel: 0.06,
};
const STANDARD = 0.05;
/* Längste Übereinstimmung gewinnt: „reel-faktencheck“ enthält „reel“. */
const schluessel = (zweck) => Object.keys(ERWARTET).sort((a, b) => b.length - a.length).find((n) => String(zweck).toLowerCase().includes(n)) || null;

/* Was ein Zweck in diesem Lauf tatsächlich gekostet hat (teuerster Aufruf).
   Die Tabelle oben ist nur der Startwert für den ersten Aufruf; sobald
   gemessen wurde, zählt die Messung – in beide Richtungen.

   Warum das wichtig ist: Am 11.09. wurde ein Reel-Entwurf vom Faktencheck zu
   Recht beanstandet („Paragraf 9“ statt „Art. 9 Abs. 3 GG“). Der zweite
   Versuch scheiterte dann nicht am Geld, sondern an der Schätzung – der
   Entwurf hatte 0,047 $ gekostet, vorab belastet wurden aber 0,06 $, und
   damit lag der Deckel rechnerisch 0,005 $ zu tief. Das Reel fiel aus,
   obwohl es bezahlbar gewesen wäre. */
const GEMESSEN = {};
const erwartetFuer = (zweck) => { const k = schluessel(zweck); if (!k) return STANDARD; return GEMESSEN[k] ?? ERWARTET[k]; };

const darfReserve = (zweck) => Boolean(reserviertFuer) && String(zweck).toLowerCase().includes(reserviertFuer);
export const budgetFrei = (zweck = "") => tagesStand() + erwartetFuer(zweck) + (darfReserve(zweck) ? 0 : reserviert) < limitUsd;

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
  /* Der Rest des Laufs rechnet ab jetzt mit dem gemessenen Wert (dem teuersten
     Aufruf dieses Zwecks), nicht mehr mit der Schätzung. */
  const zweckSchluessel = schluessel(zweck);
  if (zweckSchluessel) GEMESSEN[zweckSchluessel] = Math.max(GEMESSEN[zweckSchluessel] ?? 0, usd);
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
