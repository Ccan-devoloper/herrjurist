/* ==========================================================================
   Die Mechanik des Reservebestands: auffüllen, aufräumen, entnehmen.

   Die REGEL steht in reserve.mjs und hat bewusst keine Abhängigkeiten. Hier
   steht, wann sie angewendet wird - mit hereingereichten Abhängigkeiten,
   damit sich das Verhalten prüfen lässt, ohne Git, Netz und Instagram zu
   brauchen.

   Drei Dinge, die diese Datei anders macht als der Tageslauf:

   1. DIE ENTNAHME KOSTET NICHTS. Sie rendert nicht, sie färbt nicht um, sie
      ruft keinen Anbieter. Sie nimmt die gespeicherten Bild-URLs und schickt
      sie an Instagram. Wer hier etwas nachbessert, hat den Vorrat als Antwort
      auf den Blockadetag bereits verloren.

   2. DIE FARBE KOMMT AUS DEM EINTRAG. Der Renderer nimmt `fach` und
      `klausur` aus dem Beitrag (render.mjs), nicht aus dem Kalendertag - die
      Bilder tragen die Farbe ihres eigenen Klausurtags schon, seit sie
      gerendert wurden. Die Entnahme veröffentlicht sie unverändert. Ein
      Tag-2-Inhalt bleibt Tag-2-farbig.

   3. DIE BILDER LIEGEN AUSSERHALB DER ROTATION. hosting.aufraeumen() löscht
      Bildordner, deren Name ein Datum ist und das älter als 21 Tage ist -
      dieselbe Frist wie die Haltbarkeit des Vorrats. Ein am 01.09. erzeugter
      Eintrag gilt bis zum 22.09. und hätte am 22.09. keine Bilder mehr.
      Deshalb liegen sie unter `bilder/reserve/<id>/`: Der Name ist kein
      Datum, die Rotation fasst ihn nicht an, und der Vorrat räumt selbst auf.
      Zwei Systeme, die dieselbe Frist unabhängig voneinander verwalten, gehen
      irgendwann auseinander.
   ========================================================================== */

import fs from "node:fs";
import path from "node:path";
import { bestandPruefen, bedarf, entnehmen, eintragBauen, ZIEL_BESTAND } from "./reserve.mjs";

/** Ablageort der Vorratsbilder - bewusst kein Datum, siehe oben. */
export const RESERVE_ORDNER = "reserve";
export const BESTAND_DATEI = "reserve.json";

export const reservePfad = (id) => path.posix.join(RESERVE_ORDNER, String(id));

export function bestandLaden(hosting) {
  const roh = hosting.jsonLesen(BESTAND_DATEI, null);
  return Array.isArray(roh?.eintraege) ? roh.eintraege : [];
}

export function bestandInhalt(bestand, kanal = null) {
  return { kanal, ziel: ZIEL_BESTAND, eintraege: bestand, stand: new Date().toISOString() };
}

/** Löscht die Bilder eines Eintrags. Der Vorrat besitzt sie, also räumt er sie weg. */
export function bilderLoeschen(hosting, id) {
  try {
    const ordner = path.join(hosting.dir, "bilder", RESERVE_ORDNER, String(id));
    if (fs.existsSync(ordner)) { fs.rmSync(ordner, { recursive: true, force: true }); return true; }
  } catch { /* ein misslungenes Aufräumen darf keinen Lauf kosten */ }
  return false;
}

/**
 * Wirft aus dem Bestand, was nicht mehr gilt - und die zugehörigen Bilder mit.
 * Kein Nachcheck, keine Verlängerung: Ersatz entsteht später an einem
 * günstigen Tag.
 */
export function reserveAufraeumen({ hosting, bestand, heute, log = () => {} }) {
  const { gueltig, verfallen } = bestandPruefen(bestand, heute);
  for (const e of verfallen) {
    bilderLoeschen(hosting, e.id);
    log(`  Vorrat: ${e.id} verworfen (${e.grund})`);
  }
  return { bestand: gueltig, entfernt: verfallen };
}

/**
 * Nimmt einen Vorratsbeitrag und veröffentlicht ihn - ohne einen einzigen
 * bezahlten Aufruf.
 *
 * Gibt `{eintrag: null}` zurück, wenn nichts Passendes da ist. Das ist kein
 * Fehler, sondern der Normalfall eines leeren Vorrats; der Slot bleibt dann
 * blockiert wie bisher.
 */
export async function reserveEntnehmen({ hosting, bestand, heute, ledger, ig, slot, echteMedienId, vermerken, log = () => {} }) {
  const wahl = entnehmen(bestand, { heute, ledger });
  for (const e of wahl.verfallen) bilderLoeschen(hosting, e.id);
  if (!wahl.eintrag) {
    log(`  Vorrat: kein Ersatz für ${slot} (${wahl.grund})`);
    return { eintrag: null, medienId: null, bestand: wahl.rest, grund: wahl.grund };
  }

  const e = wahl.eintrag;
  log(`  Vorrat: ${slot} wird durch ${e.id} ersetzt (${e.fach || "?"}, Klausurtag ${e.klausur ?? "?"}) - unverändert, ohne Neurendern`);

  /* Genau hier: die gespeicherten URLs, so wie sie sind. Kein Rendern, kein
     Umfärben, keine Farbe aus dem Tagesplan. */
  const medienId = await ig.beitragPosten({ bildUrls: e.bildUrls, caption: e.caption });
  if (!echteMedienId(medienId)) {
    log(`  ○ Vorrat: ${e.id} ohne Medien-ID - der Eintrag bleibt im Bestand.`);
    return { eintrag: e, medienId: null, bestand, grund: "keine Medien-ID" };
  }

  vermerken(ledger, {
    datum: heute, art: "beitrag", slot, format: e.format || "karussell",
    thema: e.themaId, fach: e.fach, klausur: e.klausur,
    titel: e.beitrag?.folien?.[0]?.titel || null,
    hashtags: e.hashtags || [], medienId,
    ausReserve: e.id,
    veroeffentlicht: new Date().toISOString(),
  });

  bilderLoeschen(hosting, e.id);
  return { eintrag: e, medienId, bestand: wahl.rest, grund: null };
}

/**
 * Füllt den Bestand schrittweise auf - aber nur aus echtem Restbudget.
 *
 * Die Reihenfolge ist die Regel:
 *   1. Steht bezahlte Pflichtarbeit aus, passiert hier gar nichts.
 *   2. Ist der Bestand voll, passiert nichts.
 *   3. Reicht das freie Budget den Worst Case eines Beitrags nicht, passiert
 *      nichts. Es gibt keinen Mindestverbrauch.
 *
 * `erzeugen()` macht die teure Arbeit (schreiben, prüfen, rendern, Bilder
 * ablegen) und wird hereingereicht - diese Datei soll ohne Anbieter testbar
 * bleiben.
 */
export async function reserveAuffuellen({
  bestand, heute, kanal, budget, erzeugen, speichern,
  kostenJeBeitragUsd, ziel = ZIEL_BESTAND, maxJeLauf = 1, log = () => {},
}) {
  const offen = bedarf(bestand, heute, ziel);
  if (!offen) return { bestand, erzeugt: 0, grund: "Bestand voll" };

  const sperre = budget?.optionalGesperrt?.();
  if (sperre) return { bestand, erzeugt: 0, grund: `Pflichtarbeit steht aus: ${sperre}` };

  let neu = [...bestand];
  let erzeugt = 0;
  for (let i = 0; i < Math.min(offen, maxJeLauf); i++) {
    const frei = budget?.frei?.("core") ?? 0;
    if (frei < kostenJeBeitragUsd) {
      return { bestand: neu, erzeugt, grund: `Restbudget ${frei.toFixed(4)} $ trägt keinen Vorratsbeitrag (${kostenJeBeitragUsd.toFixed(4)} $)` };
    }
    const id = `${heute}-r${Date.now().toString(36)}`;
    const roh = await erzeugen({ id, pfad: reservePfad(id), heute });
    if (!roh) { log("  Vorrat: kein taugliches Thema frei - heute kein Nachschub."); break; }

    const gebaut = eintragBauen({ ...roh, id, kanal, erstelltAm: heute });
    if (!gebaut.ok) {
      /* Nicht blind wiederholen: Wer hier scheitert, scheitert am naechsten
         Thema vermutlich genauso - und jeder Versuch kostet Geld. */
      log(`  Vorrat: ${id} nicht aufgenommen (${gebaut.gruende.join("; ")})`);
      break;
    }
    neu = [...neu, gebaut.eintrag];
    erzeugt += 1;
    await speichern(neu);
    log(`  Vorrat: ${gebaut.eintrag.id} aufgenommen · ${gebaut.eintrag.fach || "?"} · Klausurtag ${gebaut.eintrag.klausur ?? "?"} · gültig bis ${gebaut.eintrag.verfaelltAm} (${neu.length}/${ziel})`);
  }
  return { bestand: neu, erzeugt, grund: null };
}
