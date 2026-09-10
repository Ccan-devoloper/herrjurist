/* ==========================================================================
   Schreibweise der Normen.

   Auf dem Bildschirm gilt die Zitierweise, die in der juristischen Klausur
   üblich ist: § 80 Abs. 1 S. 5 VwGO, § 1 Abs. 1 S. 1 Nr. 1 BGB. Absatz,
   Satz, Nummer und Buchstabe werden abgekürzt, aber ausgeschrieben – keine
   Klammern.

   Römische Ziffern („§ 441 III BGB“) bleiben stehen, wo sie stehen: Der Kanal
   zitiert sie seit jeher so, und beides ist in der Klausur üblich. Nur die
   Klammerform wird aufgelöst, die gehört zum Schwester-Kanal.

   Gesprochen geht beides nicht: „Abs.“ liest keine Stimme als „Absatz“, und
   „III“ liest sie als Buchstaben. Deshalb gibt es zwei Fassungen – normKurz()
   für alles Sichtbare, normGesprochen() für den Sprechertext.
   ========================================================================== */

/* Römische Ziffern, wie sie hinter einem Paragrafen vorkommen (Absätze gehen
   in der Praxis kaum über 20 hinaus). */
const ROEMISCH = { I: 1, II: 2, III: 3, IV: 4, V: 5, VI: 6, VII: 7, VIII: 8, IX: 9, X: 10, XI: 11, XII: 12, XIII: 13, XIV: 14, XV: 15, XVI: 16, XVII: 17, XVIII: 18, XIX: 19, XX: 20 };

/* Reihenfolge zählt: Erst die langen Formen, dann die kurzen, damit nichts
   doppelt umgeschrieben wird. */
const KURZ = [
  /* Klammerform aus anderen Quellen zurückholen: „§ 7 (1)“ → „§ 7 Abs. 1“. */
  [/(§{1,2}\s*\d+[a-z]?)\s*\((\d+[a-z]?)\)/g, (_, p, n) => `${p} Abs. ${n}`],
  /* Ausgeschriebene Formen abkürzen. Bewusst ohne i-Flag bei Absatz und
     Nummer: Der Zusatz hinter der Zahl ist immer klein („1a“); mit i-Flag
     verschluckte die Regel das große S aus „Abs. 1 S. 1“. */
  [/\b(?:Absatz|absatz)\s*(\d+)\s*([a-z])?(?![A-Za-zÄÖÜäöüß.])/g, (_, n, b) => `Abs. ${n}${b || ""}`],
  [/\bSatz\s*(\d+)\b/gi, "S. $1"],
  [/\b(?:Nummer|nummer)\s*(\d+)\s*([a-z])?(?![A-Za-zÄÖÜäöüß.])/g, (_, n, b) => `Nr. ${n}${b || ""}`],
  [/\bHalbsatz\s*(\d+)\b/gi, "Hs. $1"],
  /* Doppelbuchstabe vor Buchstabe prüfen, sonst greift der Buchstabe zuerst. */
  [/\b(?:Doppelbuchstabe|DBuchst\.|Doppelbuchst\.)\s*([a-z]{2})\)?/gi, "$1"],
  [/\b(?:Buchstabe|Buchst\.)\s*([a-z])\)?/gi, "lit. $1"],
];

/** Kurzform für alles, was gelesen wird: Kacheln, Stories, Reel-Bildschirmtext. */
export function normKurz(text) {
  if (typeof text !== "string" || !text) return text;
  let out = text;
  for (const [muster, ersatz] of KURZ) out = out.replace(muster, ersatz);
  return out.replace(/§\s*(\d)/g, "§ $1").replace(/\s{2,}/g, " ").trim();
}

const GESPROCHEN = [
  /* „§ 441 III“ würde die Stimme als „drei Buchstaben I“ lesen – zuerst
     auflösen, solange das § noch als Anker dasteht. */
  [/((?:§{1,2}|Art\.)\s*\d+[a-z]?)\s+([IVX]+)(?=[\s,.;)]|$)/g, (_, p, r) => (ROEMISCH[r] ? `${p} Absatz ${ROEMISCH[r]}` : `${p} ${r}`)],
  [/§§/g, "Paragrafen"],
  [/§/g, "Paragraf"],
  [/\bArt\./g, "Artikel"],
  [/\bAbs\.\s*(\d+)/gi, "Absatz $1"],
  [/\bS\.\s*(\d+)/g, "Satz $1"],
  [/\bNr\.\s*(\d+)/g, "Nummer $1"],
  [/\bHs\.\s*(\d+)/g, "Halbsatz $1"],
  [/\blit\.\s*([a-z])\b/gi, "Buchstabe $1"],
  [/\bi\.\s?V\.\s?m\./gi, "in Verbindung mit"],
  [/\bff\./g, "fortfolgende"],
  [/\bh\.\s?M\./g, "herrschende Meinung"],
  [/\ba\.\s?A\./g, "andere Ansicht"],
];

/**
 * Fassung für die Stimme: Abkürzungen ausgeschrieben, damit die Sprachausgabe
 * „Paragraf 80 Absatz 1 Satz 5“ sagt statt „Paragraf 80 Abs Punkt 1“.
 * Die Gesetzeskürzel (BGB, StGB, VwGO …) bleiben stehen; sie werden korrekt
 * gelesen.
 */
export function normGesprochen(text) {
  if (typeof text !== "string" || !text) return text;
  let out = text;
  for (const [muster, ersatz] of GESPROCHEN) out = out.replace(muster, ersatz);
  return out.replace(/\s{2,}/g, " ").replace(/\s+([,.;:])/g, "$1").trim();
}

/** Die Regel, wie sie im Auftrag an das Modell steht. */
export const NORM_REGEL = 'Normen in der Klausur-Zitierweise: § 80 Abs. 1 S. 5 VwGO, § 1 Abs. 1 S. 1 Nr. 1 lit. a BGB. Absatz, Satz, Nummer und Buchstabe abgekürzt, nie in Klammern. Römische Absatzziffern („§ 441 III BGB“) sind ebenfalls in Ordnung, wenn die Norm üblicherweise so zitiert wird – nur nicht innerhalb eines Beitrags mischen.';
export const NORM_REGEL_STIMME = 'Im Sprechertext dagegen ausgeschrieben, damit die Stimme es richtig liest: „Paragraf 80 Absatz 1 Satz 5 VwGO“ – dort keine Abkürzungen.';

/** Wendet die Kurzform auf alle sichtbaren Felder eines Objekts an. */
export function felderKuerzen(objekt, felder) {
  for (const f of felder) if (typeof objekt?.[f] === "string") objekt[f] = normKurz(objekt[f]);
  if (Array.isArray(objekt?.punkte)) objekt.punkte = objekt.punkte.map(normKurz);
  if (Array.isArray(objekt?.optionen)) objekt.optionen = objekt.optionen.map(normKurz);
  return objekt;
}
