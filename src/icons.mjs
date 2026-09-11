/* ==========================================================================
   Farbige Icons (Iconify, Satz „Fluent Emoji Flat“, Rückfall „Fluent Color“).

   Die Strichgrafiken in stile.mjs bleiben als letzter Rückfall; hier liegt
   zu jedem Schlüssel, den der Autor kennt, ein farbiges Gegenstück. Die
   Icons kommen aus den npm-Paketen, nicht über die Iconify-API: kein
   Schlüssel, kein Netz zur Laufzeit, dasselbe Bild bei jedem Rendern.

   Warum Emoji Flat: Der Satz ist mit 3.000 Zeichen konkret genug für ein
   Thema - Polizei, Richterin, Handschlag, Schlüssel, Schriftrolle - statt
   nur Waage und Paragraf. Ein Zeichen, das mit dem Thema nichts zu tun
   hat, ist Dekoration; eines, das es trifft, erzählt mit.
   ========================================================================== */

import { createRequire } from "node:module";
import { getIconData, iconToSVG, iconToHTML, replaceIDs } from "@iconify/utils";

const require = createRequire(import.meta.url);
const saetze = {};
function satz(name) {
  if (name in saetze) return saetze[name];
  try { saetze[name] = require(`@iconify-json/${name}/icons.json`); } catch { saetze[name] = null; }
  return saetze[name];
}

/* Schlüssel des Autors → Zeichen. Allgemeine Zeichen zuerst (die 25 alten
   Schlüssel), dann die Story-Arten, dann das themennahe Vokabular. */
export const ZUORDNUNG = {
  waage: "balance-scale", rechner: "abacus", kalender: "spiral-calendar", gebaeude: "office-building",
  diagramm: "bar-chart", dokument: "page-facing-up", warnung: "warning", uhr: "alarm-clock",
  muenzen: "coin", haus: "house", lkw: "delivery-truck", vertrag: "memo",
  lupe: "magnifying-glass-tilted-left", kreislauf: "counterclockwise-arrows-button", blitz: "high-voltage", buch: "open-book",
  fabrik: "factory", person: "bust-in-silhouette", personen: "busts-in-silhouette", globus: "globe-with-meridians",
  paragraf: "books", haken: "check-mark-button", kreuz: "cross-mark", zielscheibe: "bullseye", trophaee: "trophy",
  /* Story-Arten und Folienbausteine */
  merke: "light-bulb", fehler: "cross-mark", frage: "thinking-face", norm: "open-book", formel: "abacus",
  begriff: "books", tipp: "light-bulb", zahl: "bar-chart", countdown: "hourglass-done", lesezeichen: "bookmark",
  teilen: "envelope-with-arrow", folgen: "raised-hand",
  /* Themennah: Personen und Orte */
  polizei: "police-officer", richter: "judge", gericht: "classical-building", polizeiauto: "police-car",
  detektiv: "detective", arzt: "health-worker", buero: "office-worker", landwirt: "farmer", mechaniker: "mechanic",
  bauarbeiter: "construction-worker", senior: "older-person", baby: "baby", familie: "people-hugging",
  achselzucken: "person-shrugging", krankenhaus: "hospital", schule: "school", hotel: "hotel", laden: "convenience-store",
  bank: "bank", baustelle: "construction", haeuser: "houses", ruine: "derelict-house", tuer: "door",
  /* Themennah: Dinge und Geld */
  handschlag: "handshake", schluessel: "key", schloss: "locked", verbot: "no-entry", stopp: "stop-sign", schild: "shield",
  geldbeutel: "money-bag", banknote: "euro-banknote", kreditkarte: "credit-card", quittung: "receipt", hauptbuch: "ledger",
  "geld-weg": "money-with-wings", "kurve-hoch": "chart-increasing", "kurve-runter": "chart-decreasing",
  einkaufswagen: "shopping-cart", paket: "package", handtasche: "handbag", edelstein: "gem-stone", ordner: "file-folder",
  aktenschrank: "card-file-box", aktentasche: "briefcase", klemmbrett: "clipboard", schriftrolle: "scroll", umschlag: "envelope",
  fueller: "fountain-pen", zeitung: "newspaper", kamera: "camera", handy: "mobile-phone", laptop: "laptop", fernseher: "television",
  mikrofon: "microphone", megafon: "megaphone", telefon: "telephone", drucker: "printer", glocke: "bell", etikett: "label",
  link: "link", bueroklammer: "paperclip", schere: "scissors", hammer: "hammer", werkzeug: "wrench", messer: "kitchen-knife",
  dolch: "dagger", feuer: "fire", weinglas: "wine-glass", bier: "beer-mug", tablette: "pill", sarg: "coffin",
  hochzeit: "wedding", ring: "ring", wahlurne: "ballot-box-with-ballot", abschluss: "graduation-cap", medaille: "sports-medal",
  stoppuhr: "stopwatch", hund: "dog", baum: "deciduous-tree", setzling: "seedling", schneeflocke: "snowflake",
  /* Themennah: Verkehr */
  auto: "automobile", taxi: "taxi", motorrad: "motorcycle", fahrrad: "bicycle", bus: "bus", zug: "train",
  sattelzug: "articulated-lorry", traktor: "tractor", schiff: "ship", flugzeug: "airplane", krankenwagen: "ambulance",
  tanken: "fuel-pump", anker: "anchor", rakete: "rocket",
};

/** Ob ein farbiger Satz verfügbar ist. */
export const farbIconsVorhanden = () => Boolean(satz("fluent-emoji-flat") || satz("fluent-color"));

/** Farbiges Icon als SVG-String, oder null, wenn kein Satz da ist oder der Name unbekannt ist. */
export function farbIcon(schluessel, groesse = 96) {
  const roh = ZUORDNUNG[schluessel] || (String(schluessel).includes("-") ? schluessel : null);
  if (!roh) return null;
  /* „satz:name“ erlaubt, sonst Emoji Flat zuerst, dann Fluent Color. */
  const [setName, name] = roh.includes(":") ? roh.split(":") : [null, roh];
  for (const kandidat of setName ? [setName] : ["fluent-emoji-flat", "fluent-color"]) {
    const s = satz(kandidat);
    const daten = s && getIconData(s, name);
    if (!daten) continue;
    const { attributes, body } = iconToSVG(daten, { height: groesse });
    return iconToHTML(replaceIDs(body), { ...attributes, class: "icon farb" });
  }
  return null;
}
