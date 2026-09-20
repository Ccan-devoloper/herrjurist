/* ==========================================================================
   Manuelle Tagesfinalisierung.

   Inhalte, die morgens im Chat fachlich geprüft und finalisiert wurden,
   tragen `manuellGeprueft: true`. Das ist ein harter Kostenschutz:
   - keine erneute LLM-Faktenprüfung,
   - keine automatische Reparatur/Neufassung,
   - keine nachträgliche Bildregie per LLM.

   Lokale, kostenlose Struktur-/Quizprüfungen dürfen weiterhin blockieren,
   wenn die gespeicherte Datei technisch widersprüchlich ist. Rendering,
   Pexels/Bild-KI, TTS und die zeitgesteuerte Veröffentlichung bleiben davon
   unberührt.
   ========================================================================== */

export function manuellFinalisiert(inhalt) {
  return inhalt?.manuellGeprueft === true;
}

export function finalisierungsInfo(inhalt) {
  return manuellFinalisiert(inhalt)
    ? { manuell: true, quelle: inhalt.finalisiertVon || "chat", zeit: inhalt.finalisiertAm || null }
    : { manuell: false, quelle: null, zeit: null };
}

export function tagesinhaltManuellFinalisiert(plan, textLesen = () => null) {
  if (!plan) return false;
  const pflicht = [
    ...(plan.beitraege || []),
    ...(plan.stories || []).filter((s) => s.art !== "teaser"),
  ];
  return pflicht.length > 0 && pflicht.every((e) => manuellFinalisiert(textLesen(e.slot)));
}
