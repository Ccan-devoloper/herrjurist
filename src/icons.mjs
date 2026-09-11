/* ==========================================================================
   Farbige Icons (Iconify, Satz „Fluent Color“).

   Die Strichgrafiken in stile.mjs bleiben als Rückfall; hier liegt zu jedem
   Schlüssel, den der Autor kennt, ein farbiges Gegenstück. Die Icons kommen
   aus dem npm-Paket @iconify-json/fluent-color, nicht über die Iconify-API:
   kein Schlüssel, kein Netz zur Laufzeit, dasselbe Bild bei jedem Rendern.
   ========================================================================== */

import { createRequire } from "node:module";
import { getIconData, iconToSVG, iconToHTML, replaceIDs } from "@iconify/utils";

const require = createRequire(import.meta.url);
let satz;
function laden() {
  if (satz !== undefined) return satz;
  try { satz = require("@iconify-json/fluent-color/icons.json"); } catch { satz = null; }
  return satz;
}

/* Schlüssel des Autors → Icon im Satz. Wo Fluent Color kein direktes
   Gegenstück hat (Waage, Lkw, Fabrik), steht das sinnverwandte Zeichen. */
export const ZUORDNUNG = {
  waage: "building-government-24", rechner: "receipt-24", kalender: "calendar-24", gebaeude: "building-24",
  diagramm: "chart-multiple-24", dokument: "document-text-24", warnung: "warning-24", uhr: "clock-24",
  muenzen: "coin-multiple-24", haus: "home-24", lkw: "building-store-24", vertrag: "clipboard-text-edit-24",
  lupe: "search-visual-24", kreislauf: "arrow-sync-24", blitz: "alert-urgent-24", buch: "book-open-24",
  fabrik: "building-multiple-24", person: "person-24", personen: "people-team-24", globus: "globe-24",
  paragraf: "library-24", haken: "checkmark-circle-24", kreuz: "dismiss-circle-24", zielscheibe: "flag-24",
  trophaee: "trophy-24",
  /* Story-Arten und Folienbausteine */
  merke: "lightbulb-24", fehler: "error-circle-24", frage: "notebook-question-mark-24", norm: "book-open-24",
  formel: "receipt-24", begriff: "book-star-24", tipp: "lightbulb-filament-24", zahl: "chart-multiple-24",
  countdown: "clock-alarm-24", lesezeichen: "bookmark-24", teilen: "people-chat-24", folgen: "person-add-24",
};

/** Ob der farbige Satz verfügbar ist. */
export const farbIconsVorhanden = () => Boolean(laden());

/** Farbiges Icon als SVG-String, oder null, wenn der Satz fehlt oder der Name unbekannt ist. */
export function farbIcon(schluessel, groesse = 96) {
  const s = laden();
  if (!s) return null;
  const name = ZUORDNUNG[schluessel] || (String(schluessel).includes("-") ? schluessel : null);
  if (!name) return null;
  const daten = getIconData(s, name);
  if (!daten) return null;
  const { attributes, body } = iconToSVG(daten, { height: groesse });
  return iconToHTML(replaceIDs(body), { ...attributes, class: "icon farb" });
}
