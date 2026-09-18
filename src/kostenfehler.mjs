/* ==========================================================================
   Fehler der Kostenkontrolle - und warum sie nie eine fachliche Freigabe
   erzeugen dürfen.

   Es gibt zwei Sorten Fehler auf einem bezahlten Pfad, und sie brauchen
   entgegengesetzte Antworten:

     FACHLICH/TECHNISCH   Der Prüfer antwortet nicht, das Schema ist kaputt,
                          der Anbieter hat eine Störung. Dafür gibt es
                          definierte Degrade-Pfade - etwa bei
                          IG_FAKTENCHECK_STRIKT=false den Beitrag ohne
                          Faktencheck durchzulassen.

     KOSTENKONTROLLE      Der Schritt DARF nicht stattfinden, oder er hat
                          stattgefunden und die Kostenzusage gebrochen. Hier
                          ist jeder Degrade-Pfad falsch: „Kein Geld für die
                          Prüfung" darf niemals „gilt als geprüft" bedeuten.

   Die erste Fassung kannte nur BudgetStopp und traf damit die Fälle VOR dem
   Senden. Sie traf NICHT:

     InvarianteVerletzt   Gesendet, und teurer als zugesagt. Ausgerechnet der
                          Fall, in dem der Topf gesperrt wird - und er wäre
                          bei strikt=false in den fachlichen Fallback
                          gelaufen und hätte { ok: true } erzeugt.
     UnbekannterZweck     Ein neuer bezahlter Zweck ohne Topf. Ein
                          Policy-Fehler, kein Prüferausfall.
     OhneKontext          Ein bezahlter Pfad ohne Laufkontext, also ohne
                          jedes Budget.

   Deshalb zwei Ebenen statt einer:

     KostenKontrollFehler          alles, was die Kostenkontrolle betrifft
       ├─ BudgetStopp              vor dem Senden gestoppt
       ├─ InvarianteVerletzt       gesendet, Zusage gebrochen
       ├─ UnbekannterZweck         Policy-/Mappingfehler
       └─ OhneKontext              bezahlter Pfad ohne Budget

   Jeder fachliche Freigabe- oder Degrade-Pfad prüft
   istKostenKontrollFehler() ZUERST. Wer nur istBudgetStopp() fragt, fragt
   nach dem Zeitpunkt, nicht nach der Zuständigkeit.
   ========================================================================== */

/**
 * Die Oberklasse: Dieser Fehler gehört der Kostenkontrolle, nicht der
 * Fachlichkeit. Ein Degrade-Pfad darf ihn niemals behandeln.
 */
export class KostenKontrollFehler extends Error {
  constructor(nachricht) {
    super(nachricht);
    this.name = "KostenKontrollFehler";
    /** Marke für den Fall, dass der Fehler eine Modulgrenze überquert hat. */
    this.kostenKontrolle = true;
  }
}

/**
 * Der Teil davon, der bedeutet: Dieser bezahlte Schritt findet jetzt nicht
 * statt. Nicht: Er ist fachlich gescheitert.
 */
export class BudgetStopp extends KostenKontrollFehler {
  constructor(nachricht) {
    super(nachricht);
    this.name = "BudgetStopp";
    this.budgetStopp = true;
  }
}

const STOPP_NAMEN = new Set([
  "BudgetStopp",
  "BudgetFehler",
  "PostenFehler",
  "AdmissionAbgelehnt",
  "TopfGesperrt",
  "JournalNichtDurable",
  "PflichtUeberreserviert",
  "ResearchGrenze",
]);

/* Kostenkontrolle, aber KEIN Budgetstopp: Hier wurde gesendet oder gar nicht
   erst richtig konfiguriert. */
const WEITERE_KOSTEN_NAMEN = new Set([
  "KostenKontrollFehler",
  "InvarianteVerletzt",
  "UnbekannterZweck",
  "OhneKontext",
]);

/**
 * Die Abfrage, die vor jedem fachlichen Degrade steht.
 *
 * Bewusst eng: Echte technische Fehler (Error, TypeError, SyntaxError)
 * gehören NICHT hierher - sonst würde ein Modellausfall künftig wie ein
 * Kostenproblem behandelt, und das wäre derselbe Fehler in die andere
 * Richtung.
 */
export function istKostenKontrollFehler(e) {
  if (!e) return false;
  if (e instanceof KostenKontrollFehler) return true;
  if (e.kostenKontrolle === true || e.budgetStopp === true) return true;
  return STOPP_NAMEN.has(e.name) || WEITERE_KOSTEN_NAMEN.has(e.name);
}

/** Der engere Fall: vor dem Senden gestoppt, es ist kein Geld geflossen. */
export function istBudgetStopp(e) {
  if (!e) return false;
  if (e instanceof BudgetStopp) return true;
  if (e.budgetStopp === true) return true;
  return STOPP_NAMEN.has(e.name);
}

/** Für Protokollzeilen: kurz und ohne Stapelspur. */
export function budgetStoppGrund(e) {
  return String(e?.message || e || "Kostenkontrolle").split("\n")[0];
}
