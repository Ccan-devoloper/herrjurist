/* ==========================================================================
   Was zaehlt als veroeffentlicht?

   Am 18.09. lief ein von Hand ausgeloester Lauf im Standardmodus „trocken“.
   Er hat nichts an Instagram geschickt - und trotzdem Plan und Ledger so
   beschrieben, als waere es geschehen: `status: "veroeffentlicht"`,
   `medienId: "trocken"`. Der naechste Lauf haette Beitrag und Story
   uebersprungen, und der Tag waere still ausgefallen.

   Die Regel: Ein Posten gilt erst als veroeffentlicht, wenn Instagram eine
   Medien-ID zurueckgegeben hat. Alles andere ist ein Probelauf - und ein
   Probelauf hinterlaesst im Produktionszustand GAR NICHTS. Auch keinen
   Vermerk: Die erste Fassung dieser Reparatur legte ein Feld `probelauf` an,
   und eine spaetere Pruefung erkannte daran einen kontaminierten Plan und
   verwarf ihn ganz. Ein Trockenlauf mitten am Tag haette damit die bereits
   veroeffentlichten Slots aus dem Plan geloescht - schlimmer als der Fehler,
   den er verhindern sollte. Was ein Trockenlauf getan haette, gehoert in sein
   eigenes Protokoll, nicht in den Tagesplan.
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
 * Bestaetigt (echte Medien-ID): Status, ID und Zeitpunkt werden gesetzt.
 *
 * Nicht bestaetigt: Der Eintrag wird NICHT angefasst. Er bleibt so, wie er
 * war - in aller Regel `geplant`. Der Aufrufer bekommt die Beschreibung
 * zurueck und schreibt sie in das Protokoll des Trockenlaufs.
 *
 * @returns {{bestaetigt: boolean, medienId: string|null, kennung: string, grund: string}}
 */
export function veroeffentlichungEintragen(eintrag, medienId, opt = {}) {
  if (!eintrag) return { bestaetigt: false, medienId: null, kennung: "", grund: "kein Plan-Eintrag" };
  if (!echteMedienId(medienId)) {
    const kennung = typeof medienId === "string" && medienId ? medienId : PROBE_KENNUNG;
    return { bestaetigt: false, medienId: null, kennung, grund: `ohne Medien-ID von Instagram (${kennung})` };
  }
  eintrag.status = "veroeffentlicht";
  eintrag.medienId = medienId;
  eintrag.veroeffentlicht = opt.jetzt || new Date().toISOString();
  return { bestaetigt: true, medienId, kennung: "", grund: "" };
}

/**
 * Altbestand in Ordnung bringen, Eintrag fuer Eintrag.
 *
 * Plaene von vor dieser Reparatur koennen Slots enthalten, die als
 * veroeffentlicht gelten, ohne es zu sein. Frueher wurde deshalb der ganze
 * Tagesplan verworfen und neu erzeugt. Das ist zu grob: Stehen daneben echte
 * Veroeffentlichungen, gehen deren Zustaende verloren, und der Bot schickt
 * sie ein zweites Mal hinaus.
 *
 * Stattdessen wird genau das zurueckgesetzt, was nicht belegt ist. Ein Slot
 * ohne echte Medien-ID gilt als nicht erschienen (fail closed) und wird
 * wieder faellig; alle uebrigen bleiben unangetastet.
 *
 * @returns {Array<{slot: string, grund: string}>} was bereinigt wurde
 */
export function planBereinigen(plan) {
  const bereinigt = [];
  for (const e of [...(plan?.beitraege || []), ...(plan?.stories || [])]) {
    if (!e) continue;
    /* Feld aus der ersten Fassung dieser Reparatur - es gehoert nicht in den
       Plan und wird kommentarlos entfernt. */
    if (e.probelauf) delete e.probelauf;
    if (e.status === "veroeffentlicht" && !echteMedienId(e.medienId)) {
      bereinigt.push({ slot: e.slot, grund: `galt als veroeffentlicht, Medien-ID „${e.medienId ?? "fehlt"}“ ist keine` });
      delete e.medienId;
      delete e.veroeffentlicht;
      delete e.kanaele;
      e.status = "geplant";
    }
  }
  return bereinigt;
}

/**
 * Ein Plan, der KOMPLETT aus einem Trockenlauf stammt und noch nichts
 * Echtes enthaelt, darf neu erzeugt werden - dabei geht nichts verloren.
 * Sobald auch nur ein Slot bestaetigt veroeffentlicht ist, wird er
 * stattdessen bereinigt.
 */
export function planNurAusTrockenlauf(plan) {
  if (!plan?.trocken) return false;
  return ![...(plan.beitraege || []), ...(plan.stories || [])].some(veroeffentlichtBestaetigt);
}
