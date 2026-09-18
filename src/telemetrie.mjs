/* ==========================================================================
   Was jeder bezahlte Aufruf hinterlässt.

   Bis heute stand im Protokoll eine Zeile pro Aufruf und im Asset-Zweig eine
   Tagessumme. Damit liess sich hinterher sagen, DASS ein Tag teuer war, aber
   nicht warum: Welcher Versuch, welches Modell, welcher Aufwand, wie viele
   Token, abgeschnitten oder nicht. Am 18.09. kostete ein Faktencheck 0,072 $
   statt der veranschlagten 0,01 $, und niemand konnte nachsehen, welcher der
   Aufrufe das war.

   Zwei Ebenen, mit Absicht getrennt:

     Rohdaten     Eine Zeile NDJSON je Aufruf, mit allem, was spaeter eine
                  Frage beantworten koennte. Sie landen NICHT im Asset-Zweig -
                  ein Git-Zweig ist kein Zeitreihenspeicher, und taeglich
                  zwanzig Zeilen wachsen dort ueber Monate zu einer Historie,
                  die niemand mehr liest, aber jeder Klon mitschleppt. Sie
                  gehen als Actions-Artefakt mit begrenzter Aufbewahrung.

     Aggregate    Klein, langlebig, im Asset-Zweig: je Profil ein rollendes
                  Fenster. Daraus lassen sich Perzentile rechnen, ohne die
                  Rohdaten aufzuheben.

   Erfasst werden AUCH die gescheiterten und die ungeklaerten Aufrufe. Gerade
   die Fehlerpfade sind die teuren; wer nur die gelungenen aufschreibt, misst
   am Ende die falsche Verteilung.
   ========================================================================== */

import fs from "node:fs";
import path from "node:path";
import { fensterAktualisieren, leeresFenster } from "./profile.mjs";

/** Die Felder einer Rohzeile. Reihenfolge ist Dokumentation. */
export const ROHFELDER = [
  "timestamp", "date", "channel", "purpose", "bucket", "slot",
  "provider", "model", "effort", "thinkingMode", "attempt",
  "profileId", "calibrationFamily",
  "maxTokens", "inputTokens", "outputTokens", "thinkingTokens",
  "cacheReadTokens", "cacheWriteTokens", "serverToolUsage",
  "stopReason", "sent", "spendUnknown",
  "reservedUsd", "actualUsd", "releasedUsd", "usd",
  "breakGlass", "outcome", "approved", "errorType",
];

/**
 * Öffnet die Telemetrie eines Laufs.
 *
 * @param {object} o
 * @param {string} o.datum   ISO-Tag
 * @param {string} o.kanal   "herrjurist" | "examenscampus"
 * @param {string} o.dir     lokales Ausgabeverzeichnis (out/<datum>)
 * @param {boolean} o.breakGlass
 */
export function telemetrieStarten({ datum, kanal, dir, breakGlass = false }) {
  const datei = path.join(dir, "telemetrie.ndjson");
  const zeilen = [];
  let offen = null;

  const schreiben = (eintrag) => {
    zeilen.push(eintrag);
    try {
      if (!offen) { fs.mkdirSync(dir, { recursive: true }); offen = true; }
      fs.appendFileSync(datei, `${JSON.stringify(eintrag)}\n`);
    } catch (e) {
      /* Telemetrie darf einen Lauf nie zum Scheitern bringen. */
      console.warn(`  ! Telemetrie nicht geschrieben: ${e.message}`);
    }
  };

  /**
   * Ein bezahlter Aufruf ist zu Ende - gelungen, gescheitert oder ungeklaert.
   * Fehlende Angaben bleiben null; erfunden wird nichts.
   */
  const aufruf = (roh = {}) => {
    const eintrag = {};
    for (const feld of ROHFELDER) eintrag[feld] = roh[feld] ?? null;
    eintrag.timestamp = roh.timestamp || new Date().toISOString();
    eintrag.date = roh.date || datum;
    eintrag.channel = roh.channel || kanal;
    eintrag.breakGlass = roh.breakGlass ?? breakGlass;
    eintrag.sent = roh.sent ?? false;
    eintrag.spendUnknown = roh.spendUnknown ?? false;
    eintrag.usd = roh.usd ?? roh.actualUsd ?? null;
    schreiben(eintrag);
    return eintrag;
  };

  /** Aus den Rohzeilen die rollenden Fenster je Profil fortschreiben. */
  const fensterFortschreiben = (bestand = {}) => {
    const neu = { ...bestand };
    for (const z of zeilen) {
      if (!z.profileId) continue;
      const vorher = neu[z.profileId] || leeresFenster(z.profileId, z.calibrationFamily);
      neu[z.profileId] = fensterAktualisieren(vorher, {
        ausgabeTokens: z.outputTokens,
        stopReason: z.stopReason,
        fehlerArt: z.errorType ? (/schema|json|parse/i.test(z.errorType) ? "schema" : /anbieter|provider|http|timeout|connection/i.test(z.errorType) ? "anbieter" : "sonstige") : null,
        ceiling: z.maxTokens,
        zeit: z.timestamp,
      });
    }
    return neu;
  };

  return {
    datei, aufruf, fensterFortschreiben,
    zeilen: () => [...zeilen],
    anzahl: () => zeilen.length,
    /* Kleine Tagesübersicht für den Bericht - nicht die Rohdaten. */
    uebersicht: () => {
      const jeTopf = {};
      for (const z of zeilen) {
        const t = z.bucket || "unbekannt";
        jeTopf[t] = jeTopf[t] || { aufrufe: 0, usd: 0, ungeklaert: 0, abschnitte: 0, breakGlass: 0 };
        jeTopf[t].aufrufe += 1;
        jeTopf[t].usd = Math.round((jeTopf[t].usd + (z.actualUsd || 0)) * 1e6) / 1e6;
        if (z.spendUnknown) jeTopf[t].ungeklaert += 1;
        if (z.stopReason === "max_tokens") jeTopf[t].abschnitte += 1;
        if (z.breakGlass) jeTopf[t].breakGlass += 1;
      }
      return { datum, kanal, jeTopf };
    },
  };
}
