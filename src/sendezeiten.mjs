/* Betreiber-Vorgabe ab 13.10.2026: Berliner Ortszeit, auch nach der Zeitumstellung.
   Gemeinsame Quelle fuer Live-Uebernahme und Weckkette. Keine Aenderung an
   Inhalten, Freigaben, Medien-IDs oder bereits abgeschlossenen Slots. */
export const SENDEZEITEN_AB = "2026-10-13";
export const SENDEZEITEN = Object.freeze({ b1: "06:30", b2: "10:30", b3: "17:30" });

export function sendezeitenAnwenden(plan, datum = plan?.datum) {
  if (!/^\d{4}-\d{2}-\d{2}$/.test(datum || "") || datum < SENDEZEITEN_AB) return plan;
  const abgeschlossen = (e) => ["veroeffentlicht", "uebersprungen"].includes(e.status);
  const beitraege = (plan?.beitraege || []).map((e) =>
    !abgeschlossen(e) && Object.hasOwn(SENDEZEITEN, e.slot) ? { ...e, zeit: SENDEZEITEN[e.slot] } : e);
  const zeiten = new Map(beitraege.map((e) => [e.slot, e.zeit]));
  const stories = (plan?.stories || []).map((e) =>
    !abgeschlossen(e) && e.art === "teaser" && Object.hasOwn(SENDEZEITEN, e.beitragSlot) && zeiten.has(e.beitragSlot)
      ? { ...e, zeit: zeiten.get(e.beitragSlot) } : e);
  return { ...plan, beitraege, stories };
}
