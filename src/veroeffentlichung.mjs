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
 * Woran laesst sich BEWEISEN, dass dieser Zustand aus einem Trockenlauf
 * stammt? Nur mit einem solchen Beweis darf ein Slot zurueckgesetzt werden.
 *
 * Der Unterschied ist nicht akademisch. Zwei Zustaende sehen im Plan gleich
 * aus - „veroeffentlicht“ ohne brauchbare Medien-ID -, haben aber
 * entgegengesetzte sichere Behandlungen:
 *
 *   Trockenlauf          Der Beitrag ist NIE erschienen. Zuruecksetzen ist
 *                        richtig; nichts zu tun hiesse, den Slot zu verlieren.
 *   Abbruch nach dem     Der Beitrag IST erschienen, nur die Quittung ging
 *   Senden               verloren (Runner weg, Prozess getoetet, Push
 *                        gescheitert). Zuruecksetzen hiesse, ihn ein zweites
 *                        Mal zu posten.
 *
 * Ohne Beweis gilt der zweite Fall. Ein Doppelpost ist oeffentlich und nicht
 * zurueckzunehmen; ein blockierter Slot ist ein Eintrag im Bericht.
 *
 * @returns {string|null} der Nachweis, oder null wenn es keinen gibt
 */
export function trockenlaufNachweis(eintrag, plan = null) {
  if (!eintrag) return null;
  /* Die Kennung, die der Instagram-Client im Trockenlauf zurueckgibt. Sie
     entsteht nirgends sonst. */
  if (typeof eintrag.medienId === "string" && eintrag.medienId.trim() === PROBE_KENNUNG) {
    return `Medien-ID „${PROBE_KENNUNG}“ - die Kennung des Trockenlaufs`;
  }
  /* Marke aus der ersten Fassung dieser Reparatur (18.09.). Sie wurde nur
     dort gesetzt, wo nichts gesendet wurde. */
  if (eintrag.probelauf) return "Probelauf-Marke aus einer frueheren Fassung";
  /* Ein Plan, der als Ganzes aus einem Trockenlauf stammt und nichts
     bestaetigt Veroeffentlichtes enthaelt. */
  if (planNurAusTrockenlauf(plan)) return "der gesamte Plan stammt aus einem Trockenlauf";
  return null;
}

/**
 * Altbestand in Ordnung bringen, Eintrag fuer Eintrag.
 *
 * Plaene von vor dieser Reparatur koennen Slots enthalten, die als
 * veroeffentlicht gelten, ohne es zu sein. Frueher wurde deshalb der ganze
 * Tagesplan verworfen und neu erzeugt. Das ist zu grob: Stehen daneben echte
 * Veroeffentlichungen, gehen deren Zustaende verloren.
 *
 * Jetzt entscheidet der Nachweis:
 *
 *   mit Nachweis    -> zuruecksetzen, der Slot wird wieder faellig
 *   ohne Nachweis   -> BLOCKIEREN. Der Status bleibt „veroeffentlicht“, damit
 *                      der Slot nicht erneut faellig wird; ein Marker sagt,
 *                      dass die Veroeffentlichung unbestaetigt ist, und
 *                      veroeffentlichtBestaetigt() bleibt false, damit sich
 *                      auch nichts darauf stuetzt. Fail closed in beide
 *                      Richtungen: kein Doppelpost, kein stiller Beleg.
 *
 * @returns {{bereinigt: Array, unklar: Array}}
 */
export function planBereinigen(plan, opt = {}) {
  const jetzt = opt.jetzt || new Date().toISOString();
  const bereinigt = [];
  const unklar = [];
  for (const e of [...(plan?.beitraege || []), ...(plan?.stories || [])]) {
    if (!e) continue;
    if (e.status !== "veroeffentlicht" || echteMedienId(e.medienId)) {
      /* Kein Widerspruch: Nur das Feld aus der ersten Fassung raeumen wir weg,
         es gehoert nicht in den Plan. */
      if (e.probelauf) delete e.probelauf;
      continue;
    }
    const nachweis = trockenlaufNachweis(e, plan);
    if (nachweis) {
      bereinigt.push({ slot: e.slot, grund: nachweis });
      delete e.medienId;
      delete e.veroeffentlicht;
      delete e.kanaele;
      delete e.probelauf;
      delete e.veroeffentlichungUnklar;
      e.status = "geplant";
      continue;
    }
    /* Kein Nachweis: Der Slot bleibt gesperrt, bis ein Mensch oder eine
       spaetere Reconciliation ihn aufloest. */
    const grund = `als veroeffentlicht markiert, Medien-ID „${e.medienId ?? "fehlt"}“ ist keine - und kein Nachweis, dass es ein Trockenlauf war`;
    if (!e.veroeffentlichungUnklar) e.veroeffentlichungUnklar = { seit: jetzt, medienId: e.medienId ?? null, grund };
    unklar.push({ slot: e.slot, grund });
  }
  return { bereinigt, unklar };
}

/**
 * Ist dieser Eintrag als unbestaetigt gesperrt? Solche Slots erscheinen im
 * Bericht und warten auf eine Aufloesung - sie werden weder erneut
 * veroeffentlicht noch als Beleg verwendet.
 */
export function veroeffentlichungUnklar(eintrag) {
  return !!eintrag?.veroeffentlichungUnklar;
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
