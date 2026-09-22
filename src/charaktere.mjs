/* ==========================================================================
   Wiederkehrende Cover-Charaktere: stabile Namen fuer Text und Bild.

   Der Bildrenderer kennt zusaetzlich Referenzdateien und Beschreibungen.
   Hier stehen nur die redaktionell stabilen Namen, damit Autor und manuelle
   Finalisierung denselben Cast verwenden koennen, ohne Bildcode zu laden.
   ========================================================================== */

export const CHARAKTER_NAMEN = Object.freeze({
  rex: "Rex Rohrbruch",
  zylla: "Zylla Glitch",
  form7: "FORM-7",
  brakk: "Brakk Quarzfaust",
  flux: "Prof. Wurmfried Flux",
  mara: "Mara Sternpfad",
});

export const CHARAKTER_NAMEN_LEGENDE = Object.entries(CHARAKTER_NAMEN)
  .map(([id, name]) => `${id} = ${name}`)
  .join(", ");

export const COVER_FALLNAMEN_REGEL =
  `Wenn ein Beitrag einen frei erfundenen Fall, ein Beispiel oder sonst konkret benannte fiktive Personen enthaelt, sollen die zentralen Personen moeglichst die Namen der in coverRegie.charaktere gewaehlten Cover-Figuren tragen. Verwende die Namen exakt nach dieser Zuordnung: ${CHARAKTER_NAMEN_LEGENDE}. Wenn fuer den Fall mehr Personen noetig sind als das Cover Figuren zeigt, duerfen nur fuer die zusaetzlichen Rollen neue Namen erfunden werden. Reale Personen, amtliche Fallbezeichnungen und notwendige Anonymisierungen werden niemals in Cast-Namen umbenannt.`;

export const MANUELLER_COVER_FALLNAMEN_HINWEIS =
  `Hinweis, nicht blockierend: Bei manueller oder KI-gestuetzter Finalisierung fiktive Fallpersonen moeglichst nach dem jeweiligen Cover benennen. Wenn folien[0].bildCharaktere vorhanden ist, diese Namen bevorzugen; sonst coverRegie.charaktere nach folgender Zuordnung verwenden: ${CHARAKTER_NAMEN_LEGENDE}. Reale Personen oder amtliche/anonymisierte Fallparteien nicht umbenennen.`;
