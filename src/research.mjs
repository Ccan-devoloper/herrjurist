/* ==========================================================================
   Research: begrenzte Zahl von Anfragen, begrenzte Zahl von Suchen - und
   eine ehrliche Aussage darüber, was das garantiert.

   Der Fehler, den dieses Modul ausräumt, steckte in einer einzigen Zeile:

       tools: [{ ..., max_uses: Math.min(CONFIG.ki.rechercheSuchen, 2) }]

   `max_uses` gilt pro ANFRAGE. Bei `pause_turn` schickt der Bot die Anfrage
   erneut - und das Modell bekommt wieder zwei Suchen. Nach vier Runden waren
   es acht, nicht zwei. In der Nacht zum 16.09. kostete ein einziger
   Recherche-Auftrag 0,252 $ und lieferte null Quellen: Ohne Cache-Marke wurde
   bei jeder Fortsetzung der ganze Verlauf samt Suchergebnissen neu bezahlt.

   Was dieses Modul hart zusichert:
     - keine Anfrage ohne eigene Admission,
     - höchstens ZWEI Websuchen über den GESAMTEN Auftrag hinweg,
     - eine begrenzte Zahl von Fortsetzungen,
     - kein Borrowing aus einem anderen Topf.

   Was es NICHT zusichert - und was deshalb auch nirgends behauptet wird:
   den Dollarbetrag einer bereits gestarteten Anfrage. Serverseitige Suchen
   erzeugen Eingabe-Token, deren Menge vorher niemand kennt. „Research kostet
   garantiert höchstens 0,12 $“ wäre eine Zusage, die dieses Modul nicht
   einlösen kann. Es sichert die Zahl der Anfragen und Suchen zu, und es hört
   auf, wenn der Topf leer ist.
   ========================================================================== */

/** Über den ganzen Auftrag, nicht je Anfrage. */
import { BudgetStopp } from "./kostenfehler.mjs";

export const SUCHEN_JE_AUFTRAG = 2;

export class ResearchGrenze extends BudgetStopp {
  constructor(nachricht) { super(nachricht); this.name = "ResearchGrenze"; }
}

/**
 * Begleitet EINEN Recherche-Auftrag - also alles, was zu einer Frage gehört,
 * inklusive aller `pause_turn`-Fortsetzungen.
 *
 * @param {object} o
 * @param {number} o.maxSuchen      global, Standard 2
 * @param {number} o.maxAnfragen    Fortsetzungen eingeschlossen
 */
export function rechercheAuftrag({ maxSuchen = SUCHEN_JE_AUFTRAG, maxAnfragen = 3 } = {}) {
  let suchenVerbraucht = 0;
  let anfragen = 0;
  const verlauf = [];

  /** Wie viele Suchen darf die NÄCHSTE Anfrage höchstens bekommen? */
  const restSuchen = () => Math.max(0, maxSuchen - suchenVerbraucht);

  /**
   * Darf noch eine Anfrage gestellt werden? Prüft Anzahl und Suchkontingent
   * gemeinsam - eine weitere Runde ohne verbleibende Suche ist keine
   * Recherche mehr, sondern nur noch bezahltes Nachdenken.
   */
  const darfAnfragen = ({ brauchtSuche = true } = {}) => {
    if (anfragen >= maxAnfragen) return { ok: false, grund: `${maxAnfragen} Anfragen sind das Limit dieses Auftrags` };
    if (brauchtSuche && restSuchen() <= 0) return { ok: false, grund: `alle ${maxSuchen} Suchen des Auftrags sind verbraucht` };
    return { ok: true, grund: "" };
  };

  /** Meldet eine gestellte Anfrage an und liefert ihr Suchkontingent. */
  const anfrageBeginnen = ({ brauchtSuche = true } = {}) => {
    const erlaubt = darfAnfragen({ brauchtSuche });
    if (!erlaubt.ok) throw new ResearchGrenze(erlaubt.grund);
    anfragen += 1;
    return { nummer: anfragen, maxUses: restSuchen() };
  };

  /**
   * Nach jeder Antwort: Was hat der Server wirklich gesucht? Der Zähler folgt
   * der gemeldeten Nutzung, nicht der Erlaubnis - `max_uses` ist eine
   * Obergrenze, keine Buchung.
   */
  const antwortVerbuchen = (usage = {}) => {
    const suchen = Number(usage?.server_tool_use?.web_search_requests || 0);
    suchenVerbraucht += Math.max(0, suchen);
    verlauf.push({ anfrage: anfragen, suchen, gesamt: suchenVerbraucht });
    return { suchenVerbraucht, restSuchen: restSuchen() };
  };

  return {
    anfrageBeginnen, antwortVerbuchen, darfAnfragen, restSuchen,
    stand: () => ({ suchenVerbraucht, anfragen, maxSuchen, maxAnfragen, restSuchen: restSuchen(), verlauf: [...verlauf] }),
  };
}

/**
 * Die Zeile für das Protokoll am Mess-Tag. Null verbrauchtes Budget ist kein
 * Fehler - es heißt, dass keine Recherche nötig war oder keine zugelassen
 * wurde.
 */
export function researchZeile(verbrauchtUsd, deckelUsd) {
  return `Research used: $${Number(verbrauchtUsd || 0).toFixed(3)} / $${Number(deckelUsd || 0).toFixed(3)}`;
}
