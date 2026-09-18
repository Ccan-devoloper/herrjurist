/* ==========================================================================
   Was zaehlt als veroeffentlicht?

   Am 18.09. lief ein von Hand ausgeloester Lauf im Standardmodus „trocken“.
   Er hat nichts an Instagram geschickt - und trotzdem Plan und Ledger so
   beschrieben, als waere es geschehen: `status: "veroeffentlicht"`,
   `medienId: "trocken"`. Der naechste Lauf haette Beitrag und Story
   uebersprungen, und der Tag waere still ausgefallen. Aufgefallen ist es nur,
   weil jemand nachgesehen hat.

   Die Lehre ist nicht „im Trockenlauf weniger schreiben“, sondern: Ein Posten
   gilt erst als veroeffentlicht, wenn Instagram eine Medien-ID zurueckgegeben
   hat. Alles andere ist ein Probelauf und wird auch so vermerkt - sichtbar,
   aber ohne Wirkung auf den Produktionszustand.

   Die Unterscheidung steht hier und nicht verstreut an den vier Sendestellen,
   damit sie an allen vieren dieselbe ist.
   ========================================================================== */

/* Kennung, die der Instagram-Client im Trockenlauf statt einer Medien-ID
   zurueckgibt. Sie darf nie in Plan oder Ledger landen. */
export const PROBE_KENNUNG = "trocken";

/**
 * Eine echte Medien-ID von Instagram: eine reine Ziffernfolge. Die Graph API
 * liefert 17-stellige Zahlen; kurze Zahlen gibt es dort nicht, aber die
 * Grenze ist bewusst grosszuegig - geprueft wird die Form, nicht die Laenge.
 *
 * Bewusst streng: Alles, was keine Ziffernfolge ist - „trocken“, null, ein
 * leerer String, ein Fehlerobjekt -, gilt als nicht veroeffentlicht.
 */
export function echteMedienId(id) {
  return typeof id === "string" && /^[0-9]{5,}$/.test(id.trim());
}

/**
 * Darf sich etwas anderes darauf stuetzen, dass dieser Eintrag draussen ist?
 * Der Teaser einer Story haengt daran: Er kuendigt einen Beitrag an, den es
 * ohne bestaetigte Medien-ID nicht gibt.
 *
 * Der Planstatus allein reicht nicht. Genau das war die Luecke: Der Status
 * stand auf „veroeffentlicht“, die ID war „trocken“.
 */
export function veroeffentlichtBestaetigt(eintrag) {
  return !!eintrag && eintrag.status === "veroeffentlicht" && echteMedienId(eintrag.medienId);
}

/**
 * Traegt das Ergebnis eines Sendeversuchs in den Plan-Eintrag ein.
 *
 * Bestaetigt (echte Medien-ID): Status, ID und Zeitpunkt werden gesetzt, ein
 * frueherer Probelauf-Vermerk verschwindet - der Eintrag ist jetzt echt.
 *
 * Nicht bestaetigt (Trockenlauf, leere Antwort): Der Eintrag bleibt
 * `geplant`. Vermerkt wird nur, dass ein Probelauf ihn erzeugt hat, unter
 * einem eigenen Feld, das keine Produktionslogik liest.
 *
 * @returns {{bestaetigt: boolean, medienId: string|null, grund: string}}
 */
export function veroeffentlichungEintragen(eintrag, medienId, opt = {}) {
  if (!eintrag) return { bestaetigt: false, medienId: null, grund: "kein Plan-Eintrag" };
  const jetzt = opt.jetzt || new Date().toISOString();
  if (!echteMedienId(medienId)) {
    const kennung = typeof medienId === "string" && medienId ? medienId : PROBE_KENNUNG;
    eintrag.probelauf = { zeit: jetzt, kennung };
    return { bestaetigt: false, medienId: null, grund: `ohne Medien-ID von Instagram (${kennung})` };
  }
  delete eintrag.probelauf;
  eintrag.status = "veroeffentlicht";
  eintrag.medienId = medienId;
  eintrag.veroeffentlicht = jetzt;
  return { bestaetigt: true, medienId, grund: "" };
}

/**
 * Traegt ein alter Plan Spuren eines Trockenlaufs? Solche Plaene wurden live
 * schon bisher verworfen; geprueft wurde aber nur auf die Zeichenfolge
 * „trocken“. Jede andere Ersatzkennung waere durchgerutscht.
 */
export function ausTrockenlauf(plan) {
  if (!plan) return false;
  if (plan.trocken) return true;
  return [...(plan.beitraege || []), ...(plan.stories || [])]
    .some((e) => e && (e.probelauf || (e.status === "veroeffentlicht" && !echteMedienId(e.medienId))));
}
