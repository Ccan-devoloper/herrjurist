/* ==========================================================================
   Gemeinschaftsbudget fuer die beiden Instagram-Kanaele.

   Jeder Kanal behält seinen eigenen Tagesdeckel. Pflichtarbeit darf aber den
   nachweislich freien Rest desselben Topfs des Schwesterkanals mitbenutzen,
   wenn dessen Pflichtprodukt fuer den Tag bereits vollständig vorbereitet ist.

   Warum nur dann: Beide Workflows laufen unabhaengig und haben keinen
   gemeinsamen atomaren Speicher. Würden beide gleichzeitig auf vermeintlich
   freien Rest zugreifen, könnten sie denselben Dollar zweimal versprechen.
   Sobald der Schwesterkanal keine bezahlte Pflichtarbeit mehr braucht, gibt es
   diese Race Condition für Pflichtaufrufe nicht mehr.

   Fremdbudget gilt ausschliesslich fuer Pflichtaufrufe. Optionale Bilder,
   Auffuellen, Kommentare usw. bleiben am lokalen Deckel.
   ========================================================================== */

import { manuellFinalisiert } from "./finalisierung.mjs";

const TOEPFE = ["core", "engagement", "research"];
const SCHWESTER = {
  examenscampus: "Ccan-devoloper/herrjurist",
  herrjurist: "Ccan-devoloper/steuerberater",
};

const runden = (n) => Math.round((Number(n) || 0) * 1e6) / 1e6;

async function rawJson(repo, pfad) {
  const url = `https://raw.githubusercontent.com/${repo}/instagram-assets/${pfad}?stand=${Date.now()}`;
  const r = await fetch(url, { headers: { accept: "application/json" }, cache: "no-store" });
  if (!r.ok) return null;
  try { return await r.json(); } catch { return null; }
}

export function journalVerbrauch(journal, datum) {
  const out = Object.fromEntries(TOEPFE.map((t) => [t, 0]));
  if (!journal || journal.datum !== datum) return out;
  for (const t of TOEPFE) out[t] = runden(journal.legacyBaseline?.[t] || 0);
  for (const e of journal.eintraege || []) {
    if (!TOEPFE.includes(e.bucket)) continue;
    if (e.state === "settled") out[e.bucket] = runden(out[e.bucket] + Number(e.actualUsd || 0));
    else if (e.state === "reserved" || e.state === "sent" || e.state === "unresolved") {
      out[e.bucket] = runden(out[e.bucket] + Number(e.reservedUsd || 0));
    }
  }
  return out;
}

const inhaltSauber = (x) => !!x && (
  manuellFinalisiert(x)
  || (!x.faktencheckOffen
    && !(x.beanstandet || []).length
    && !(x.beanstandetFachlich || []).length)
);

/* Der Schwesterkanal darf Restbudget erst verleihen, wenn kein Pflichttext
   mehr erzeugt oder fachlich repariert werden muss. Veröffentlichen/rendern
   selbst kostet hier kein Modellbudget. */
export async function pflichtVorbereitet(repo, datum) {
  const plan = await rawJson(repo, `state/plaene/${datum}.json`);
  if (!plan || plan.trocken) return { ok: false, grund: "kein belastbarer Tagesplan" };

  for (const b of plan.beitraege || []) {
    if (b.status === "veroeffentlicht") continue;
    const text = await rawJson(repo, `state/inhalte/${datum}-${b.slot}.json`);
    if (!inhaltSauber(text)) return { ok: false, grund: `Beitrag ${b.slot} braucht noch Pflichtarbeit` };
  }
  for (const s of plan.stories || []) {
    if (s.status === "veroeffentlicht" || s.art === "teaser") continue;
    const text = await rawJson(repo, `state/inhalte/${datum}-${s.slot}.json`);
    if (!inhaltSauber(text)) return { ok: false, grund: `Story ${s.slot} braucht noch Pflichtarbeit` };
  }
  return { ok: true, grund: "Pflichtprodukt vorbereitet" };
}

export async function gemeinschaftsBudget({ kanal, datum, deckel }) {
  const repo = SCHWESTER[kanal];
  const nullen = Object.fromEntries(TOEPFE.map((t) => [t, 0]));
  if (!repo) return { repo: null, fremdFrei: nullen, grund: "kein Schwesterkanal" };

  try {
    const bereit = await pflichtVorbereitet(repo, datum);
    if (!bereit.ok) return { repo, fremdFrei: nullen, grund: bereit.grund };

    const journal = await rawJson(repo, "state/budget-journal.json");
    if (!journal || journal.datum !== datum) return { repo, fremdFrei: nullen, grund: "kein heutiges Schwester-Journal" };
    const verbraucht = journalVerbrauch(journal, datum);
    const fremdFrei = Object.fromEntries(TOEPFE.map((t) => [
      t, runden(Math.max(0, Number(deckel[t] || 0) - Number(verbraucht[t] || 0))),
    ]));
    return { repo, fremdFrei, verbraucht, grund: bereit.grund };
  } catch (e) {
    return { repo, fremdFrei: nullen, grund: `Schwesterstand nicht lesbar: ${e.message}` };
  }
}
