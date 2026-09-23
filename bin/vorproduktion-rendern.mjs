#!/usr/bin/env node
/**
 * Rendert die Chat-Vorproduktion als echte Herr-Jurist-Vorschau.
 *
 * Wichtig:
 * - Texte werden ausschliesslich aus vorproduktion/<datum>.json gelesen.
 * - Es gibt KEINEN Autor-, Faktencheck- oder Bild-QA-Provideraufruf.
 * - Kostenpflichtig ist ausschliesslich die bestehende OpenAI-Charakter-
 *   Bildgenerierung via titelbild()/charakterMotivZeichnen().
 * - Reels sprechen mit Piper offline.
 * - Kosten laufen durch dieselbe durable Provider-Tuer und dasselbe Journal.
 */
import fs from "node:fs";
import os from "node:os";
import path from "node:path";

import { Hosting } from "../src/hosting.mjs";
import { titelbild } from "../src/bilder.mjs";
import { beitragRendern, storyRendern, browserBeenden } from "../src/render.mjs";
import { reelBauen } from "../src/reel.mjs";
import { stickerFarbe } from "../src/stile.mjs";
import { budgetStarten, ZWECK_TOPF } from "../src/budget.mjs";
import { journalStarten } from "../src/journal.mjs";
import { einzelkostenSynchronisieren } from "../src/kostenledger.mjs";
import { telemetrieStarten } from "../src/telemetrie.mjs";
import { kontextSetzen, kontextLoeschen } from "../src/anbieter.mjs";
import {
  budgetSetzen,
  abschluss as kostenAbschluss,
  vortagsSchaetzung,
} from "../src/kosten.mjs";

const daten = process.argv.slice(2).filter((x) => /^\d{4}-\d{2}-\d{2}$/.test(x));
const tage = daten.length ? daten : ["2026-09-24", "2026-09-25"];
const kostenDatum = new Date().toISOString().slice(0, 10);
const kanal = "herrjurist-vorproduktion";
const budgetDeckel = Number(process.env.IG_VORPRODUKTION_BILD_BUDGET_USD || 2.0);

if (String(process.env.IG_CHARAKTER_QA || "").toLowerCase() !== "false") {
  throw new Error("Vorproduktions-Render darf keine bezahlte Bild-QA starten: IG_CHARAKTER_QA=false ist Pflicht.");
}
if (String(process.env.IG_STIMME || "").toLowerCase() !== "piper") {
  throw new Error("Vorproduktions-Render muss mit der kostenlosen Piper-Stimme laufen: IG_STIMME=piper ist Pflicht.");
}
if (!process.env.OPENAI_API_KEY) throw new Error("OPENAI_API_KEY fehlt.");

const hosting = new Hosting({ pushen: true }).vorbereiten();
const temp = fs.mkdtempSync(path.join(os.tmpdir(), "herrjurist-vorproduktion-"));
const telemetrie = telemetrieStarten({
  datum: kostenDatum,
  kanal,
  dir: path.join(temp, "telemetrie"),
  breakGlass: true,
});

const kostenStart = hosting.jsonLesen("kosten.json", { wochen: {}, tage: {} });
const heute = kostenStart.tage?.[kostenDatum] || {};
const antwortenBisher = heute.antworten
  ?? Number(((heute.zwecke?.kommentare || 0) + (heute.zwecke?.nachrichten || 0)).toFixed(4));
const inhaltBisher = heute.antworten != null
  ? Number(heute.usd || 0)
  : Math.max(0, Number(heute.usd || 0) - antwortenBisher);

budgetSetzen({
  limitUsd: budgetDeckel,
  antwortLimitUsd: 0,
  bisher: inhaltBisher,
  bisherAntworten: antwortenBisher,
  gemessen: heute.messungen || {},
  vortag: vortagsSchaetzung(kostenStart.tage || {}, kostenDatum),
  speichern: (usd, aufrufe, zwecke, gemessen, antworten) => {
    const k = hosting.jsonLesen("kosten.json", { wochen: {}, tage: {} });
    k.tage ||= {};
    const alt = kostenStart.tage?.[kostenDatum] || {};
    const gesamtZwecke = { ...(alt.zwecke || {}) };
    for (const [z, betrag] of Object.entries(zwecke || {})) {
      gesamtZwecke[z] = Number(((alt.zwecke?.[z] || 0) + Number(betrag || 0)).toFixed(4));
    }
    const hoechste = { ...(alt.messungen || {}) };
    for (const [z, betrag] of Object.entries(gemessen || {})) {
      hoechste[z] = Number(Math.max(hoechste[z] || 0, Number(betrag || 0)).toFixed(4));
    }
    k.tage[kostenDatum] = {
      usd: Number(Number(usd || 0).toFixed(4)),
      antworten: Number(Number(antworten || 0).toFixed(4)),
      aufrufe: Number(alt.aufrufe || 0) + Number(aufrufe || 0),
      zwecke: gesamtZwecke,
      messungen: hoechste,
      stand: new Date().toISOString(),
    };
    hosting.jsonSchreiben("kosten.json", k);
  },
});

const bisherJeTopf = { core: 0, engagement: 0, research: 0 };
for (const [zweck, betrag] of Object.entries(heute.zwecke || {})) {
  const topf = ZWECK_TOPF[zweck];
  if (topf) bisherJeTopf[topf] += Number(betrag) || 0;
}

const journal = journalStarten({
  datum: kostenDatum,
  kanal,
  lesen: () => hosting.jsonLesen("budget-journal.json", null),
  schreiben: async (inhalt) => {
    hosting.jsonSchreiben("budget-journal.json", inhalt);
    const kosten = hosting.jsonLesen("kosten.json", { wochen: {}, tage: {} });
    hosting.jsonSchreiben("kosten.json", einzelkostenSynchronisieren(kosten, inhalt));
    hosting.commit(`Budget-Journal + Einzelkosten Vorproduktion ${kostenDatum}`);
    return await hosting.push();
  },
  remoteNoetig: true,
  legacyBaseline: bisherJeTopf,
});

const uebernahme = journal.uebernahme();
for (const topf of Object.keys(bisherJeTopf)) {
  bisherJeTopf[topf] = Number(uebernahme.vorbelastung?.[topf] || 0);
}
if (uebernahme.freigegeben.length || uebernahme.blockiert.length) await journal.abschluss();

const budget = budgetStarten({
  deckel: { core: budgetDeckel, engagement: 0, research: 0 },
  bisher: bisherJeTopf,
  breakGlass: true,
  protokoll: () => {},
});
kontextSetzen({ budget, telemetrie, journal, kanal, datum: kostenDatum });

function motivUebernehmen(ziel, treffer) {
  ziel.bild = treffer.bild;
  ziel.bildQuelle = treffer.quelle;
  ziel.bildFrei = treffer.frei !== false;
  ziel.bildBreite = treffer.breite || null;
  ziel.bildHoehe = treffer.hoehe || null;
  ziel.bildTyp = treffer.typ || "charakter";
  ziel.bildCharaktere = treffer.charaktere || [];
  ziel.coverHinweisPlan = treffer.coverHinweisPlan || null;
  ziel.bildPrompt = treffer.prompt || null;
  ziel.bildKostenUsd = treffer.kostenUsd ?? null;
}

function kw(iso) {
  const d = new Date(`${iso}T12:00:00Z`);
  d.setUTCDate(d.getUTCDate() + 4 - (d.getUTCDay() || 7));
  const j = new Date(Date.UTC(d.getUTCFullYear(), 0, 1));
  const w = Math.ceil((((d - j) / 86400000) + 1) / 7);
  return `${d.getUTCFullYear()}-W${String(w).padStart(2, "0")}`;
}

const manifest = {
  version: 1,
  erzeugtAm: new Date().toISOString(),
  kostenDatum,
  textProviderKostenUsd: 0,
  faktencheckProviderKostenUsd: 0,
  bildQaProviderKostenUsd: 0,
  bildgenerierung: "OpenAI Images Edits API ueber bestehende Herr-Jurist-Pipeline",
  bildmodell: process.env.IG_CHARAKTER_MODELL || "gpt-image-2.5-sunburst-2026-09-08",
  tage: [],
};

const tagesUpdates = new Map();

try {
  for (const datum of tage) {
    const quelle = path.join(hosting.dir, "vorproduktion", `${datum}.json`);
    if (!fs.existsSync(quelle)) throw new Error(`Vorproduktion fehlt: ${quelle}`);
    const tag = JSON.parse(fs.readFileSync(quelle, "utf8"));
    const tagTemp = path.join(temp, datum);
    fs.mkdirSync(tagTemp, { recursive: true });
    const mTag = { datum, feed: [], stories: [] };

    for (const slot of ["b1", "b2", "b3"]) {
      const inhalt = structuredClone(tag.inhalte?.[slot]);
      if (!inhalt) throw new Error(`${datum} ${slot}: Inhalt fehlt`);

      /* Bei Reels liegt die kreative Cover-Regie in der Hook-Szene. Fuer die
         bestehende Charakterpipeline wird sie fuer das Cover nach oben gespiegelt. */
      if (!inhalt.folien && !inhalt.coverRegie && inhalt.szenen?.[0]?.coverRegie) {
        inhalt.coverRegie = structuredClone(inhalt.szenen[0].coverRegie);
      }

      const treffer = await titelbild(inhalt, null, {
        randFarbe: stickerFarbe(inhalt.klausur, process.env.IG_STIL || "bunt"),
        zweck: "bild",
        slot: `vorproduktion:${datum}:${slot}`,
        charaktere: true,
      });
      if (!treffer) throw new Error(`${datum} ${slot}: kein Charakter-Cover erzeugt`);

      const slotTemp = path.join(tagTemp, slot);
      fs.mkdirSync(slotTemp, { recursive: true });

      if (Array.isArray(inhalt.folien)) {
        const titel = inhalt.folien.find((x) => x.art === "titel") || inhalt.folien[0];
        motivUebernehmen(titel, treffer);
        const pfade = await beitragRendern(inhalt, slotTemp, { variante: 0 });
        mTag.feed.push({
          slot,
          format: inhalt.format,
          hook: titel?.titel || null,
          charaktere: treffer.charaktere || [],
          bildKostenUsd: treffer.kostenUsd ?? null,
          dateien: pfade.map((p) => path.basename(p)),
        });
      } else if (Array.isArray(inhalt.szenen)) {
        motivUebernehmen(inhalt, treffer);
        const r = await reelBauen(inhalt, slotTemp, {
          datum,
          layout: "erklaer",
          framesBehalten: false,
        });
        mTag.feed.push({
          slot,
          format: "reel",
          hook: inhalt.szenen?.[0]?.titel || null,
          charaktere: treffer.charaktere || [],
          bildKostenUsd: treffer.kostenUsd ?? null,
          dateien: [path.basename(r.cover), path.basename(r.video)],
          reel: {
            dauer: r.dauer,
            stimme: r.anbieter,
            layout: r.layout,
          },
        });
      } else {
        throw new Error(`${datum} ${slot}: unbekanntes Inhaltsformat`);
      }
    }

    /* Eigenstaendige Story-Vorschauen kosten nichts und helfen bei der
       Gesamtpruefung des Tages. Teaser s1-s3 werden spaeter aus den Feedposts
       abgeleitet und sind deshalb hier nicht doppelt gespeichert. */
    const storyDir = path.join(tagTemp, "stories");
    fs.mkdirSync(storyDir, { recursive: true });
    for (const [slot, story] of Object.entries(tag.inhalte || {})
      .filter(([s, x]) => /^s\d+$/.test(s) && x?.art)) {
      const ziel = path.join(storyDir, `${slot}-${story.art}.jpg`);
      await storyRendern(structuredClone(story), ziel, { variante: 0 });
      mTag.stories.push({ slot, art: story.art, datei: path.basename(ziel) });
    }

    tag.renderVorschau = {
      status: "fertig",
      erzeugtAm: new Date().toISOString(),
      pfad: `vorproduktion/${datum}/fertig`,
      textProviderKostenUsd: 0,
      faktencheckProviderKostenUsd: 0,
      bildQaProviderKostenUsd: 0,
      bildKostenUsd: Number(mTag.feed.reduce((s, x) => s + Number(x.bildKostenUsd || 0), 0).toFixed(6)),
      freigabeBetreiber: false,
    };
    tagesUpdates.set(datum, tag);
    manifest.tage.push(mTag);
  }
} finally {
  await browserBeenden().catch(() => {});
  kontextLoeschen();
}

const laufKosten = kostenAbschluss();
manifest.bildKostenUsd = Number(laufKosten.usd.toFixed(6));
manifest.providerAufrufe = laufKosten.aufrufe;
manifest.erzeugtAm = new Date().toISOString();

/* Wochenaggregat um genau die in diesem Lauf tatsaechlich verbuchten
   Bildkosten erweitern. Die Einzelposten stehen bereits durable im Journal. */
{
  const k = hosting.jsonLesen("kosten.json", { wochen: {}, tage: {} });
  k.wochen ||= {};
  const key = kw(kostenDatum);
  const alt = k.wochen[key] || { usd: 0, aufrufe: 0, cacheSumme: 0, cacheAnteil: 0 };
  const aufrufe = Number(alt.aufrufe || 0) + Number(laufKosten.aufrufe || 0);
  const cacheSumme = Number(alt.cacheSumme || 0);
  k.wochen[key] = {
    ...alt,
    usd: Number(alt.usd || 0) + Number(laufKosten.usd || 0),
    aufrufe,
    cacheSumme,
    cacheAnteil: aufrufe ? cacheSumme / aufrufe : 0,
  };
  hosting.jsonSchreiben("kosten.json", k);
}

/* Erst NACH allen Provideraufrufen kommen die grossen Previewdateien in den
   Asset-Clone. So committen die durablen Journal-Schreibvorgaenge niemals
   halbfertige Bilder oder Videos. */
for (const datum of tage) {
  const ziel = path.join(hosting.dir, "vorproduktion", datum, "fertig");
  fs.rmSync(ziel, { recursive: true, force: true });
  fs.mkdirSync(path.dirname(ziel), { recursive: true });
  fs.cpSync(path.join(temp, datum), ziel, { recursive: true });
  fs.writeFileSync(
    path.join(hosting.dir, "vorproduktion", `${datum}.json`),
    JSON.stringify(tagesUpdates.get(datum), null, 2) + "\n",
  );
}
fs.writeFileSync(
  path.join(hosting.dir, "vorproduktion", "render-manifest.json"),
  JSON.stringify(manifest, null, 2) + "\n",
);

hosting.commit(`Rendere Vorproduktion ${tage.join(" + ")}`);
await hosting.push();
await journal.abschluss();

console.log(JSON.stringify({
  ok: true,
  tage,
  bildKostenUsd: manifest.bildKostenUsd,
  providerAufrufe: manifest.providerAufrufe,
  textProviderKostenUsd: 0,
  faktencheckProviderKostenUsd: 0,
  bildQaProviderKostenUsd: 0,
  ziel: tage.map((d) => `vorproduktion/${d}/fertig`),
}, null, 2));
