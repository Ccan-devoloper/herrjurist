/* ==========================================================================
   Ein Fehlertyp für „der bezahlte Schritt darf jetzt nicht stattfinden“.

   Beim Verdrahten der Admission ist eine zweite Fehlerklasse entstanden. Vorher
   gab es BudgetFehler; dazu kamen AdmissionAbgelehnt, TopfGesperrt und
   JournalNichtDurable. Semantisch sagen sie alle dasselbe - aber der
   bestehende Code prüfte an vielen Stellen weiter nur:

       if (e instanceof BudgetFehler) …

   Eine Admission-Ablehnung fiel damit durch dieses Raster und wurde wie ein
   technischer Fehler des Modells behandelt. Das ist an einer Stelle richtig
   gefährlich: In faktenSicher() führt der allgemeine Fehlerpfad bei
   IG_FAKTENCHECK_STRIKT=false dazu, dass ein Beitrag OHNE bestandene Prüfung
   weitergereicht wird. Ein Budgetstopp darf niemals eine fachliche Freigabe
   erzeugen - lieber erscheint heute nichts.

   Deshalb eine gemeinsame Oberklasse und EINE Abfrage. Keine verteilten
   String- oder name-Vergleiche: Die wachsen mit jedem neuen Fehlertyp still
   auseinander, und genau das war das Problem.
   ========================================================================== */

/**
 * Oberklasse aller Fehler, die bedeuten: Dieser bezahlte Schritt findet jetzt
 * nicht statt. Nicht: Er ist fachlich gescheitert.
 */
export class BudgetStopp extends Error {
  constructor(nachricht) {
    super(nachricht);
    this.name = "BudgetStopp";
    /** Damit ein Aufrufer die Absicht abfragen kann, ohne die Klasse zu kennen. */
    this.budgetStopp = true;
  }
}

/**
 * Die eine Abfrage. Sie erkennt auch Fehler, die über eine Modulgrenze kamen
 * (zwei Instanzen desselben Moduls, ein serialisierter Fehler) - deshalb neben
 * instanceof auch die Marke und die Namensliste.
 */
export function istBudgetStopp(e) {
  if (!e) return false;
  if (e instanceof BudgetStopp) return true;
  if (e.budgetStopp === true) return true;
  return NAMEN.has(e.name);
}

const NAMEN = new Set([
  "BudgetStopp",
  "BudgetFehler",
  "PostenFehler",
  "AdmissionAbgelehnt",
  "TopfGesperrt",
  "JournalNichtDurable",
  "PflichtUeberreserviert",
  "ResearchGrenze",
]);

/** Für Protokollzeilen: kurz und ohne Stapelspur. */
export function budgetStoppGrund(e) {
  return String(e?.message || e || "Budgetstopp").split("\n")[0];
}
