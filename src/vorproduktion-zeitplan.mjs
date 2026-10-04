/* ==========================================================================
   Nächster Veröffentlichungstermin der Vorproduktion – für die Weckkette.

   Bewusst ohne Abhängigkeiten außer zeit.mjs: Die Weckkette im Workflow lädt
   dieses Modul ohne npm ci. Der Plan entsteht wie im Lauf aus der
   Dashboard-Datei vorproduktion/<datum>.json; Status und Fehler kommen aus
   dem gespeicherten Tagesplan state/plaene/<datum>.json.
   ========================================================================== */

import { zeitpunktVon } from "./zeit.mjs";

/* Diese Zeitspanne vor dem Termin startet die Weckkette den Lauf: Job-Start,
   Abhängigkeiten, Token-/Insight-Arbeit und die Container-Verarbeitung bei
   Instagram müssen davor fertig sein. */
export const WECK_VORLAUF_MINUTEN = 8;

/* Nach einem Fehler weckt die Kette für diesen Eintrag nicht sofort erneut;
   den nächsten Versuch übernimmt der stündliche Lauf. */
const FEHLER_RUHE_MS = 30 * 60 * 1000;

export function planFuerWecker(tag, gespeichert = null) {
  const alt = new Map([...(gespeichert?.beitraege || []), ...(gespeichert?.stories || [])].map((e) => [e.slot, e]));
  const eintrag = (e) => {
    const a = alt.get(e.slot);
    return { ...e, status: a?.status && a.status !== "geplant" ? a.status : "geplant", fehler: a?.fehler || null };
  };
  return {
    beitraege: (tag?.plan?.beitraege || []).map(eintrag),
    stories: (tag?.plan?.stories || []).map(eintrag),
  };
}

/**
 * Nächster offener Termin des Tages als Zeitpunkt (ms), oder null.
 * Berücksichtigt nur geplante Einträge ohne frischen Fehler, deren Uhrzeit
 * nach `seit` liegt – dem Start des Laufs, zu dem die Weckkette gehört. Was
 * davor fällig war, hat dieser Lauf schon gesehen; ein Termin, der erst
 * während des Laufs fällig wurde, führt zum sofortigen Wecken.
 */
export function naechsterTermin(plan, datum, jetzt = Date.now(), seit = jetzt) {
  const frischerFehler = (e) => {
    const t = Date.parse(String(e?.fehler || "").split(" ")[0]);
    return Number.isFinite(t) && jetzt - t < FEHLER_RUHE_MS;
  };
  let bester = null;
  for (const e of [...(plan?.beitraege || []), ...(plan?.stories || [])]) {
    if (e.status !== "geplant" || !/^\d{1,2}:\d{2}$/.test(e.zeit || "")) continue;
    if (frischerFehler(e)) continue;
    if (e.art === "teaser" && frischerFehler((plan.beitraege || []).find((b) => b.slot === e.beitragSlot))) continue;
    const t = zeitpunktVon(datum, e.zeit);
    if (t <= seit) continue;
    if (bester === null || t < bester) bester = t;
  }
  return bester;
}
