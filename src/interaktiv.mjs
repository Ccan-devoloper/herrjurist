/* ==========================================================================
   Interaktive Stories über die private Instagram-Schnittstelle (instagrapi).

   Die offizielle Publishing-API kennt keinen nativen Umfrage-Sticker. Eine ins
   Bild gemalte Umfrage sieht aus wie eine, ist aber nicht antippbar, erzeugt
   keine Stimmen und liefert keine Ergebnisse. Für echte Interaktion führt kein
   Weg an der privaten Schnittstelle vorbei.

   Die ist nicht freigegeben, und das hat Folgen. Dieses Modul ist deshalb so
   gebaut, dass es NIE der einzige Weg ist:

     * Jeder Fehler wird geworfen, nicht geschluckt - der Aufrufer schickt die
       Story dann über die Graph API raus wie bisher. Eine Story fällt nie aus,
       nur weil der Zusatzweg klemmt.
     * Nach einer Challenge oder einer Bremse von Instagram wird für Stunden
       gar nicht erst wieder versucht. Eine Wiederholungsschleife gegen eine
       Anmeldesperre ist genau das, was ein Konto endgültig kostet.
     * Die Sitzung wird wiederverwendet und verschlüsselt abgelegt. Eine
       bestehende Sitzung sieht für Instagram nach dem immer gleichen Gerät
       aus; eine Neuanmeldung von wechselnder Runner-IP nach einer Übernahme.

   Die Zugangsdaten gehen über stdin, nie über die Kommandozeile: Argumente
   liest jeder andere Prozess auf demselben Rechner in der Prozessliste mit.
   ========================================================================== */

import { execFile } from "node:child_process";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { CONFIG } from "./config.mjs";
import { tokenVerschluesseln, tokenEntschluesseln } from "./instagram.mjs";

const HIER = path.dirname(fileURLToPath(import.meta.url));
export const BRUECKE = path.resolve(HIER, "..", "bin", "story_privat.py");
export const SITZUNGSDATEI = "instagrapi.enc";

export class InteraktivFehler extends Error {
  constructor(nachricht, art = "sonstig") { super(nachricht); this.art = art; }
}

/* Soll diese Story eine Umfrage bekommen? Getrennt und ohne Seiteneffekte,
   damit sich die Entscheidung prüfen lässt, ohne Instagram anzufassen. */
export function interaktivGeplant(story, config = CONFIG.interaktiv) {
  if (!config.aktiv) return false;
  if (!config.nutzer || !config.passwort) return false;
  if (!config.arten.includes(story?.art)) return false;
  return (story?.optionen || []).length >= 2;
}

/* Der gemessene Platz im Bild (Pixel) wird zur Sticker-Angabe (Anteil der
   Fläche, Mittelpunkt). Gerechnet wird mit dem echten Kasten aus dem Layout,
   nicht mit geschätzten Koordinaten - sonst liegt der Sticker bei einem
   längeren Titel plötzlich auf dem Text. */
export function umfrageBauen(story, platz, { breite = 1080, hoehe = 1920, frage = CONFIG.interaktiv.stickerFrage } = {}) {
  if (!platz || !(platz.width > 0) || !(platz.height > 0)) throw new InteraktivFehler("Kein Platz für die Umfrage gemessen", "aufbau");
  const optionen = (story.optionen || []).slice(0, 4).map((_, k) => "ABCD"[k]);
  if (optionen.length < 2) throw new InteraktivFehler("Umfrage braucht mindestens zwei Optionen", "aufbau");
  return {
    frage,
    optionen,
    x: (platz.x + platz.width / 2) / breite,
    y: (platz.y + platz.height / 2) / hoehe,
    width: platz.width / breite,
    height: platz.height / hoehe,
  };
}

/* --- Sperre nach einer Challenge ----------------------------------------- */
export const sperreAktiv = (ledger, jetzt = Date.now()) =>
  Boolean(ledger?.interaktivSperreBis && new Date(ledger.interaktivSperreBis).getTime() > jetzt);

export function sperreSetzen(ledger, grund, { stunden = CONFIG.interaktiv.sperreStunden, jetzt = Date.now() } = {}) {
  ledger.interaktivSperreBis = new Date(jetzt + stunden * 3600e3).toISOString();
  ledger.interaktivSperreGrund = String(grund).slice(0, 200);
  return ledger;
}

/* --- Sitzungstresor ------------------------------------------------------
   Dieselbe Verschlüsselung wie beim Token: Der Asset-Zweig ist öffentlich,
   und eine Instagram-Sitzung im Klartext wäre dort ein Konto zum Mitnehmen. */
const sitzungsPfad = (stateDir) => path.join(stateDir, SITZUNGSDATEI);

export function sitzungLaden(stateDir) {
  const p = sitzungsPfad(stateDir);
  if (!fs.existsSync(p)) return null;
  try { return tokenEntschluesseln(fs.readFileSync(p, "utf8")); } catch { return null; }
}

export function sitzungSichern(stateDir, sitzung) {
  if (!sitzung) return false;
  try {
    fs.writeFileSync(sitzungsPfad(stateDir), tokenVerschluesseln(sitzung));
    return true;
  } catch (e) {
    console.warn(`  ! Sitzung nicht gespeichert (${e.message}) – beim nächsten Lauf wird neu angemeldet.`);
    return false;
  }
}

/* --- Aufruf der Brücke ---------------------------------------------------- */
function bruecke(auftrag, opt = {}) {
  const zeitlimit = opt.zeitlimit ?? CONFIG.interaktiv.zeitlimitSekunden * 1000;
  const python = opt.python || CONFIG.interaktiv.python;
  const skript = opt.skript || BRUECKE;
  return new Promise((fertig, scheitern) => {
    const kind = execFile(python, [skript], { timeout: zeitlimit, maxBuffer: 4 << 20 }, (fehler, stdout, stderr) => {
      /* Auch im Fehlerfall steht die Auskunft auf stdout - das Skript beendet
         sich mit Code 1, sagt aber trotzdem, WAS schiefging. Erst wenn sich
         daraus nichts lesen lässt, zählt der Prozessfehler. */
      const zeile = String(stdout || "").trim().split("\n").filter(Boolean).pop();
      if (zeile) {
        try { return fertig(JSON.parse(zeile)); } catch { /* unten weiter */ }
      }
      const grund = fehler?.killed ? `Zeitlimit von ${Math.round(zeitlimit / 1000)} s überschritten`
        : `${fehler?.message || "keine Antwort"}${stderr ? ` – ${String(stderr).trim().split("\n").pop()}` : ""}`;
      scheitern(new InteraktivFehler(grund, fehler?.killed ? "zeitlimit" : "bruecke"));
    });
    kind.stdin.end(JSON.stringify(auftrag));
  });
}

/**
 * Veröffentlicht eine Story mit nativer Umfrage. Wirft bei jedem Fehlschlag –
 * der Aufrufer muss dann über die Graph API veröffentlichen.
 *
 * @returns {Promise<string>} Medien-ID der Story
 */
export async function interaktivPosten({ bildPfad, umfrage, link = null, stateDir, ledger = {}, log = console.log, python, skript = BRUECKE }) {
  if (sperreAktiv(ledger)) {
    throw new InteraktivFehler(`Gesperrt bis ${ledger.interaktivSperreBis} (${ledger.interaktivSperreGrund || "ohne Grund"})`, "gesperrt");
  }
  if (!fs.existsSync(skript)) throw new InteraktivFehler(`Brücke fehlt: ${skript}`, "aufbau");

  const sitzung = sitzungLaden(stateDir);
  const antwort = await bruecke({
    bild: path.resolve(bildPfad),
    nutzer: CONFIG.interaktiv.nutzer,
    passwort: CONFIG.interaktiv.passwort,
    sitzung,
    umfrage,
    link,
  }, { python, skript });

  /* Die Sitzung kommt auch aus einem gescheiterten Versuch zurück und ist dann
     oft die frischere - erst sichern, dann urteilen. */
  if (antwort.sitzung) sitzungSichern(stateDir, antwort.sitzung);

  if (!antwort.ok) {
    if (["challenge", "bremse"].includes(antwort.art)) {
      sperreSetzen(ledger, antwort.fehler);
      log(`  ! Interaktive Stories bis ${ledger.interaktivSperreBis} ausgesetzt: ${antwort.fehler}`);
    }
    throw new InteraktivFehler(antwort.fehler || "unbekannter Fehler", antwort.art || "sonstig");
  }
  return String(antwort.medienId);
}
