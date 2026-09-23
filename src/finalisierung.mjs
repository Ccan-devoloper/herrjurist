import { MANUELLER_COVER_FALLNAMEN_HINWEIS } from "./charaktere.mjs";

/* ==========================================================================
   Manuelle Tagesfinalisierung.

   Inhalte, die morgens im Chat fachlich geprüft und finalisiert wurden,
   tragen `manuellGeprueft: true`. Das ist ein harter Kostenschutz:
   - keine erneute LLM-Faktenprüfung,
   - keine automatische Reparatur/Neufassung,
   - keine nachträgliche Bildregie per LLM.

   Lokale, kostenlose Struktur-/Quizprüfungen dürfen weiterhin blockieren,
   wenn die gespeicherte Datei technisch widersprüchlich ist.

   Für manuell finalisierte Herr-Jurist-Feedposts gilt zusätzlich ein harter
   visueller Publish-Gate: Die Veröffentlichung darf nur das bereits
   freigegebene, dauerhaft auf instagram-assets gespeicherte End-Cover
   verwenden. Fehlt dieser persistierte Asset-Vertrag, bleibt der Slot zu.
   Für nicht manuell finalisierte autonome Beiträge bleibt die normale
   Bildbeschaffung einschließlich Availability-Fallback unverändert.
   ========================================================================== */

/* WICHTIG FUER MANUELLE PRUEFUNG/ERSTELLUNG IM CHAT ODER DURCH EINE KI:
   "manuellGeprueft" bedeutet fachlich final, nicht "Formregeln ueberspringen".
   Insbesondere bei Story art=zahl muss `zahl` eine ECHTE, zum konkreten
   Themenbeitrag passende Ziffernangabe sein (max. 8 Zeichen), z. B. "0 %",
   "14 Tage", "3 Jahre" oder "100 %". Woerter wie "automatisch", "sofort" oder
   "immer" gehoeren in Titel/Text, niemals in `zahl`. Eine Paragraphennummer
   allein ist ebenfalls keine sinnvolle "Zahl des Tages".

   Diese Regel steht hier bewusst direkt am manuellen Finalisierungs-Gate, damit
   sie bei spaeterer Chat-/KI-Finalisierung zusammen mit der Kostenschutzlogik
   sichtbar ist. Die lokale Pruefung erzwingt sie zusaetzlich vor dem Posten. */
export const MANUELLE_FINALISIERUNG_REGELN = Object.freeze({
  zahl: "Bei art=zahl: konkrete, thematisch tragende Ziffernangabe; max. 8 Zeichen; mindestens eine Ziffer; keine Wortwerte und keine bloße Paragraphennummer.",
  charakterNamen: MANUELLER_COVER_FALLNAMEN_HINWEIS,
});

export function manuellFinalisiert(inhalt) {
  return inhalt?.manuellGeprueft === true;
}

/* Harte Freigabe für manuell finalisierte Karussell-/Feedposts.
   Das End-Cover ist selbst Teil der Freigabe, nicht nur ein Preview-Artefakt.
   Der SHA bindet die redaktionelle Sichtprüfung an exakt die später
   veröffentlichte Datei. Nicht manuell finalisierte Beiträge fallen bewusst
   nicht unter diesen Gate; deren autonome Produktionslogik bleibt erhalten. */
export function manuellesCarouselAssetGate(inhalt) {
  if (!manuellFinalisiert(inhalt)) return { frei: true, manuell: false, grund: null };
  if (inhalt?.visuellGeprueft !== true) {
    return { frei: false, manuell: true, grund: "manuell finalisiert, aber visuellGeprueft fehlt" };
  }
  if (!String(inhalt?.coverFinalUrl || "").trim()) {
    return { frei: false, manuell: true, grund: "manuell finalisiert, aber coverFinalUrl fehlt" };
  }
  if (!/^[a-f0-9]{64}$/i.test(String(inhalt?.coverFinalSha256 || ""))) {
    return { frei: false, manuell: true, grund: "manuell finalisiert, aber coverFinalSha256 fehlt oder ist ungueltig" };
  }
  if (!String(inhalt?.finalisiertVon || "").trim() || !String(inhalt?.finalisiertAm || "").trim()) {
    return { frei: false, manuell: true, grund: "manuell finalisiert, aber Finalisierungsmetadaten fehlen" };
  }
  return { frei: true, manuell: true, grund: null };
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
