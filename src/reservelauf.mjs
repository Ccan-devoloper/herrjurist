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
import { istKostenKontrollFehler } from "./kostenfehler.mjs";

/**
 * Wann der Vorrat ueberhaupt eingreift - und wann nicht.
 *
 * Er ist Verfuegbarkeit bei KOSTENBLOCKADE, kein allgemeiner Fehler-Fallback.
 * Ein technischer Anbieterfehler, ein fachlich nicht freigegebener Inhalt, ein
 * Instagram-Fehler: Das sind andere Probleme, und ein Ersatzbeitrag wuerde sie
 * nur verdecken. Reels und Stories bleiben ebenfalls aussen vor - der Vorrat
 * haelt Feed-Beitraege.
 */
export function ersatzZulaessig({ eintrag, fehler }) {
  if (!istKostenKontrollFehler(fehler)) return { ok: false, grund: `kein Kostenkontrollfehler (${fehler?.name || "unbekannt"})` };
  if (eintrag?.format === "reel") return { ok: false, grund: "Reels werden nicht aus dem Vorrat ersetzt" };
  if (eintrag?.art && eintrag.art !== "beitrag") return { ok: false, grund: `${eintrag.art} wird nicht aus dem Vorrat ersetzt` };
  return { ok: true, grund: null };
}

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
  const verwaist = bilderVerwaist(hosting, gueltig);
  if (verwaist.length) log(`  Vorrat: ${verwaist.length} Bildordner ohne Eintrag entfernt (${verwaist.join(", ")})`);
  return { bestand: gueltig, entfernt: verfallen, verwaist };
}

/**
 * Bildordner ohne Eintrag im Bestand.
 *
 * Sie entstehen genau einmal: Die Bilder werden hochgeladen und gepusht,
 * BEVOR der Eintrag steht - und dazwischen kann der Beitrag an Tor 2
 * scheitern oder der Runner sterben. Weil `bilder/reserve/` bewusst
 * ausserhalb der Datumsrotation liegt, raeumt sie sonst niemand weg. Ein
 * Vorrat, der seinen eigenen Muell nicht aufraeumt, laesst den Zweig
 * wachsen, bis das Klonen im Stundenlauf teuer wird.
 */
export function bilderVerwaist(hosting, bestand) {
  const weg = [];
  try {
    const wurzel = path.join(hosting.dir, "bilder", RESERVE_ORDNER);
    if (!fs.existsSync(wurzel)) return weg;
    const bekannt = new Set(bestand.map((e) => String(e.id)));
    for (const d of fs.readdirSync(wurzel)) {
      if (bekannt.has(d)) continue;
      fs.rmSync(path.join(wurzel, d), { recursive: true, force: true });
      weg.push(d);
    }
  } catch { /* ein misslungenes Aufraeumen darf keinen Lauf kosten */ }
  return weg;
}

/**
 * Nimmt einen Vorratsbeitrag und veröffentlicht ihn - ohne einen einzigen
 * bezahlten Aufruf.
 *
 * Gibt `{eintrag: null}` zurück, wenn nichts Passendes da ist. Das ist kein
 * Fehler, sondern der Normalfall eines leeren Vorrats; der Slot bleibt dann
 * blockiert wie bisher.
 */
export async function reserveEntnehmen({
  hosting, bestand, heute, ledger, ig, eintrag, slot,
  echteMedienId, veroeffentlichungEintragen, vermerken, inhaltSpeichern,
  log = () => {},
}) {
  const kennung = slot || eintrag?.slot || "?";
  const wahl = entnehmen(bestand, { heute, ledger });
  for (const e of wahl.verfallen) bilderLoeschen(hosting, e.id);
  if (!wahl.eintrag) {
    log(`  Vorrat: kein Ersatz für ${kennung} (${wahl.grund})`);
    return { eintrag: null, medienId: null, bestand: wahl.rest, grund: wahl.grund, nachDurable: () => {} };
  }

  const e = wahl.eintrag;
  log(`  Vorrat: ${kennung} wird durch ${e.id} ersetzt (${e.fach || "?"}, Klausurtag ${e.klausur ?? "?"}) - unverändert, ohne Neurendern`);

  /* IDEMPOTENZ, wie im normalen Feed. Der gefaehrliche Ablauf ohne sie:
     Instagram nimmt den Beitrag an, die Medien-ID kommt zurueck, der Runner
     stirbt vor reserve.json, Ledger und Push - und der naechste Lauf sieht
     denselben Vorratseintrag und postet ihn ein zweites Mal. Oeffentlich und
     nicht zurueckzunehmen.

     Verglichen wird die GESPEICHERTE Publikationscaption, unveraendert. */
  const schonDa = await ig.bereitsVeroeffentlicht(e.caption);
  if (schonDa) log(`  Vorrat: ${e.id} steht bereits auf Instagram (${schonDa}) - wird nur noch vermerkt.`);

  /* Genau hier: die gespeicherten URLs, so wie sie sind. Kein Rendern, kein
     Umfaerben, keine Farbe aus dem Tagesplan. */
  const medienId = schonDa || await ig.beitragPosten({ bildUrls: e.bildUrls, caption: e.caption });
  if (!echteMedienId(medienId)) {
    log(`  ○ Vorrat: ${e.id} ohne Medien-ID - der Eintrag bleibt im Bestand.`);
    return { eintrag: e, medienId: null, bestand, grund: "keine Medien-ID", nachDurable: () => {} };
  }

  /* Ab hier ohne fachliche Arbeit dazwischen: Slot, Inhalt, Ledger, Bestand -
     und dann EIN Zustands-Commit des Aufrufers. */
  const echt = veroeffentlichungEintragen(eintrag, medienId);
  if (!echt?.bestaetigt) {
    log(`  ○ Vorrat: ${e.id} ${echt?.grund || "nicht bestätigt"} - der Eintrag bleibt im Bestand.`);
    return { eintrag: e, medienId: null, bestand, grund: echt?.grund || "nicht bestätigt", nachDurable: () => {} };
  }
  eintrag.ausReserve = e.id;

  /* Der veroeffentlichte Inhalt wird der Inhalt dieses Slots. Damit findet
     jeder Folgepfad ihn ohne neue Aufloesung - insbesondere der Teaser, der
     nach einem Runner-Wechsel inhalte/<datum>-<slot>.json laedt und sonst den
     geplanten, nie erschienenen Beitrag ankuendigen wuerde. */
  inhaltSpeichern(eintrag.slot, { ...e.beitrag, ausReserve: e.id, caption: e.caption, hashtags: e.hashtags || [] });

  vermerken(ledger, {
    datum: heute, art: "beitrag", slot: eintrag.slot, zeit: eintrag.zeit, format: e.format || "karussell",
    thema: e.themaId, fach: e.fach, klausur: e.klausur,
    titel: e.beitrag?.folien?.[0]?.titel || null,
    hashtags: e.hashtags || [], medienId,
    ausReserve: e.id, wiedergefunden: !!schonDa,
    veroeffentlicht: new Date().toISOString(),
  });

  /* Die Bilder erst NACH dem durablen Zustand loeschen. Scheitert der Push,
     steigt der naechste Lauf ueber bereitsVeroeffentlicht() wieder ein - und
     falls der Beitrag dort wider Erwarten nicht gefunden wird, braucht er die
     Bilder noch. */
  return { eintrag: e, medienId, bestand: wahl.rest, wiedergefunden: !!schonDa, grund: null, nachDurable: () => bilderLoeschen(hosting, e.id) };
}

/**
 * Füllt den Bestand schrittweise auf - aber nur aus echtem Restbudget.
 *
 * Die Reihenfolge ist die Regel:
 *   1. Steht bezahlte Pflichtarbeit aus, passiert hier gar nichts.
 *   2. Ist der Bestand voll, passiert nichts.
 *   3. Traegt das freie Restbudget die konfigurierte Beitragsgrenze nicht,
 *      passiert nichts. Es gibt keinen Mindestverbrauch.
 *
 * `erzeugen()` macht die teure Arbeit (schreiben, prüfen, rendern, Bilder
 * ablegen) und wird hereingereicht - diese Datei soll ohne Anbieter testbar
 * bleiben.
 */
export async function reserveAuffuellen({
  bestand, heute, kanal, budget, erzeugen, speichern,
  beitragsGrenzeUsd, ziel = ZIEL_BESTAND, maxJeLauf = 1, log = () => {},
}) {
  const offen = bedarf(bestand, heute, ziel);
  if (!offen) return { bestand, erzeugt: 0, grund: "Bestand voll" };

  const sperre = budget?.optionalGesperrt?.();
  if (sperre) return { bestand, erzeugt: 0, grund: `Pflichtarbeit steht aus: ${sperre}` };

  let neu = [...bestand];
  let erzeugt = 0;
  for (let i = 0; i < Math.min(offen, maxJeLauf); i++) {
    const frei = budget?.frei?.("core") ?? 0;
    if (frei < beitragsGrenzeUsd) {
      return { bestand: neu, erzeugt, grund: `Restbudget ${frei.toFixed(4)} $ trägt die Beitragsgrenze ${beitragsGrenzeUsd.toFixed(4)} $ nicht` };
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
