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
import crypto from "node:crypto";
import { CONFIG } from "./config.mjs";

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
   Dieselbe Bauart wie beim Token-Tresor (AES-256-GCM), aber mit EIGENEM
   Schlüssel: Der Asset-Zweig ist öffentlich, und eine Instagram-Sitzung im
   Klartext wäre dort ein Konto zum Mitnehmen. Der eigene Schlüssel ist nötig,
   weil die Sitzung am eigenen Rechner entsteht - dort muss er bekannt sein. */
function tresorSchluessel() {
  const s = CONFIG.interaktiv.schluessel;
  if (!s) throw new Error("IG_PRIVAT_KEY fehlt");
  return crypto.createHash("sha256").update(s).digest();
}

export function tresorSchreiben(daten) {
  const iv = crypto.randomBytes(12);
  const c = crypto.createCipheriv("aes-256-gcm", tresorSchluessel(), iv);
  const enc = Buffer.concat([c.update(JSON.stringify(daten), "utf8"), c.final()]);
  return Buffer.concat([iv, c.getAuthTag(), enc]).toString("base64");
}

export function tresorOeffnen(text) {
  const buf = Buffer.from(text, "base64");
  const iv = buf.subarray(0, 12), tag = buf.subarray(12, 28), enc = buf.subarray(28);
  const d = crypto.createDecipheriv("aes-256-gcm", tresorSchluessel(), iv);
  d.setAuthTag(tag);
  return JSON.parse(Buffer.concat([d.update(enc), d.final()]).toString("utf8"));
}

const sitzungsPfad = (stateDir) => path.join(stateDir, SITZUNGSDATEI);

/* Die Sitzung wird zum Kontonamen gespeichert. Ohne diesen Schlüssel würde
   beim Wechsel vom Testkonto auf den echten Kanal die fremde Sitzung mit den
   neuen Zugangsdaten probiert - und genau das sieht für Instagram nach einer
   Übernahme aus. Passt der Name nicht, gilt die Sitzung als nicht vorhanden. */
function tresorLesen(text, nutzer) {
  try {
    const tresor = tresorOeffnen(text);
    if (!tresor || typeof tresor !== "object") return null;
    if (String(tresor.nutzer || "").toLowerCase() !== String(nutzer || "").toLowerCase()) return null;
    return tresor.sitzung || null;
  } catch { return null; }
}

/* Erst der Asset-Zweig, dann die Saat aus dem Secret. Die Saat entsteht einmal
   am eigenen Rechner (bin/interaktiv-anmelden.mjs) - denn eine Erstanmeldung
   vom GitHub-Runner weist Instagram ab ("Please wait a few minutes", am 17.09.
   belegt): Rechenzentrums-IPs sind dort das auffälligste Muster. */
export function sitzungLaden(stateDir, nutzer = CONFIG.interaktiv.nutzer, saat = CONFIG.interaktiv.sitzungSaat) {
  const p = sitzungsPfad(stateDir);
  if (fs.existsSync(p)) {
    const ausDatei = tresorLesen(fs.readFileSync(p, "utf8"), nutzer);
    if (ausDatei) return ausDatei;
  }
  return saat ? tresorLesen(String(saat).trim(), nutzer) : null;
}

export function sitzungSichern(stateDir, sitzung, nutzer = CONFIG.interaktiv.nutzer) {
  if (!sitzung) return false;
  try {
    fs.writeFileSync(sitzungsPfad(stateDir), tresorSchreiben({ nutzer: String(nutzer || ""), sitzung }));
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
export async function interaktivPosten({ bildPfad, umfrage, link = null, stateDir, ledger = {}, log = console.log, python, skript = BRUECKE, nutzer = CONFIG.interaktiv.nutzer, passwort = CONFIG.interaktiv.passwort }) {
  if (sperreAktiv(ledger)) {
    throw new InteraktivFehler(`Gesperrt bis ${ledger.interaktivSperreBis} (${ledger.interaktivSperreGrund || "ohne Grund"})`, "gesperrt");
  }
  if (!fs.existsSync(skript)) throw new InteraktivFehler(`Brücke fehlt: ${skript}`, "aufbau");

  const sitzung = sitzungLaden(stateDir, nutzer);
  const antwort = await bruecke({
    bild: path.resolve(bildPfad),
    nutzer,
    passwort,
    sitzung,
    /* In der CI ist eine Neuanmeldung verboten. Fehlt oder trägt die Sitzung
       nicht, bricht die Brücke ab, statt von einer Rechenzentrums-IP eine
       Anmeldung zu versuchen - das würde nur eine Sperre einbringen. */
    neuanmeldungErlaubt: CONFIG.interaktiv.neuanmeldung,
    umfrage,
    link,
  }, { python, skript });

  /* Die Sitzung kommt auch aus einem gescheiterten Versuch zurück und ist dann
     oft die frischere - erst sichern, dann urteilen. */
  if (antwort.sitzung) sitzungSichern(stateDir, antwort.sitzung, nutzer);

  if (!antwort.ok) {
    if (["challenge", "bremse"].includes(antwort.art)) {
      sperreSetzen(ledger, antwort.fehler);
      log(`  ! Interaktive Stories bis ${ledger.interaktivSperreBis} ausgesetzt: ${antwort.fehler}`);
    }
    throw new InteraktivFehler(antwort.fehler || "unbekannter Fehler", antwort.art || "sonstig");
  }
  return String(antwort.medienId);
}

/* Nur anmelden, nichts veröffentlichen: der Weg für den eigenen Rechner.
   Gibt den verschlüsselten Tresor zurück, der als Secret hinterlegt wird. */
export async function anmeldenNur({ nutzer = CONFIG.interaktiv.nutzer, passwort = CONFIG.interaktiv.passwort, python, skript = BRUECKE } = {}) {
  /* Viel Zeit: Hier wird unter Umständen ein Bestätigungscode aus der Mail
     abgetippt. Das Zeitlimit des Tageslaufs (drei Minuten) wäre zu knapp -
     bis die Mail da ist, vergehen schon mal ein paar Minuten. */
  const antwort = await bruecke(
    { aktion: "anmelden", nutzer, passwort, sitzung: null, neuanmeldungErlaubt: true },
    { python, skript, zeitlimit: 15 * 60e3 },
  );
  if (!antwort.ok) throw new InteraktivFehler(antwort.fehler || "Anmeldung fehlgeschlagen", antwort.art || "login");
  return { sitzung: antwort.sitzung, tresor: tresorSchreiben({ nutzer: String(nutzer || ""), sitzung: antwort.sitzung }) };
}
