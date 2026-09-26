import { KostenKontrollFehler } from "./kostenfehler.mjs";

/* Der Tageslauf sperrt kostenpflichtige Provider immer vor seiner ersten
   Arbeit. Die Sperre ist fuer diesen Prozess irreversibel: weder Budget,
   Break Glass noch ein neuer Laufkontext koennen sie aufheben.
   IG_PROVIDERKOSTEN_GESPERRT=true schuetzt zusaetzlich Hilfsmodi des
   Instagram-Workflows. GitHub/Instagram-Transport bleibt unberuehrt. */
let gesperrt = false;

export function providerKostenSperren() {
  gesperrt = true;
}

export function providerKostenSindGesperrt() {
  return gesperrt || process.env.IG_PROVIDERKOSTEN_GESPERRT === "true";
}

export class ProviderKostenGesperrt extends KostenKontrollFehler {
  constructor(zweck) {
    super(`Providerkosten sind gesperrt: ${zweck}. Kein Anbieteraufruf, kein kostenpflichtiger Fallback; vorhandene freigegebene Medien bleiben nutzbar.`);
    this.name = "ProviderKostenGesperrt";
    this.zweck = zweck;
  }
}

export function providerKostenPruefen(zweck) {
  if (providerKostenSindGesperrt()) throw new ProviderKostenGesperrt(zweck);
}
