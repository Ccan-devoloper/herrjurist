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
import crypto from "node:crypto";

import { Hosting } from "../src/hosting.mjs";
import { titelbild } from "../src/bilder.mjs";
import { beitragRendern, storyRendern, coverRendern, browserBeenden } from "../src/render.mjs";
import { reelBauen, coverDaten } from "../src/reel.mjs";
import { stickerFarbe } from "../src/stile.mjs";
import { budgetStarten, ZWECK_TOPF } from "../src/budget.mjs";
import { journalStarten } from "../src/journal.mjs";
import { einzelkostenSynchronisieren } from "../src/kostenledger.mjs";
import { telemetrieStarten } from "../src/telemetrie.mjs";
import { kontextSetzen, kontextLoeschen } from "../src/anbieter.mjs";
import { rohbildLaden, rohbildSpeichern } from "../src/vorproduktionsbild.mjs";
import {
  budgetSetzen,
  abschluss as kostenAbschluss,
  vortagsSchaetzung,
} from "../src/kosten.mjs";

const args = process.argv.slice(2);
const daten = args.filter((x) => /^\d{4}-\d{2}-\d{2}$/.test(x));
const tage = daten.length ? daten : ["2026-09-24", "2026-09-25"];
const flagWert = (name) => {
  const treffer = args.find((x) => x.startsWith(`--${name}=`));
  return treffer ? treffer.slice(name.length + 3) : "";
};
const feedSlots = (flagWert("slots") || "b1,b2,b3").split(",").map((x) => x.trim()).filter(Boolean);
const storySlots = (flagWert("stories") || "").split(",").map((x) => x.trim()).filter(Boolean);
const nurCover = args.includes("--cover-only");
const patchModus = args.includes("--patch");
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


/* Alle harten Layout-Gates laufen VOR der ersten Provider-Reservierung.
   Damit kann eine zu breite Hook-Zeile nie wieder erst nach einem bezahlten
   Charakterbild auffallen. Der Preflight rendert nur lokal mit Icon/Typografie. */
async function layoutPreflight() {
  const basis = path.join(temp, "preflight");
  for (const datum of tage) {
    const quelle = path.join(hosting.dir, "vorproduktion", `${datum}.json`);
    if (!fs.existsSync(quelle)) throw new Error(`Vorproduktion fehlt: ${quelle}`);
    const tag = JSON.parse(fs.readFileSync(quelle, "utf8"));

    for (const slot of feedSlots) {
      const inhalt = structuredClone(tag.inhalte?.[slot]);
      if (!inhalt) throw new Error(`${datum} ${slot}: Inhalt fehlt im Layout-Preflight`);
      if (Array.isArray(inhalt.folien)) {
        const ziel = path.join(basis, datum, slot);
        fs.mkdirSync(ziel, { recursive: true });
        await beitragRendern(inhalt, ziel, { variante: 0 });
      } else if (Array.isArray(inhalt.szenen)) {
        const cover = path.join(basis, datum, `${slot}-cover.jpg`);
        fs.mkdirSync(path.dirname(cover), { recursive: true });
        await coverRendern(coverDaten(inhalt, { gesamt: 60 }), cover, { variante: 0 });
      } else {
        throw new Error(`${datum} ${slot}: unbekanntes Format im Layout-Preflight`);
      }
    }
  }
}

await layoutPreflight();
console.log(`Layout-Preflight: ${tage.join(", ")} ✓ – 0 Provideraufrufe`);

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

const bildModell = process.env.IG_CHARAKTER_MODELL || "gpt-image-2.5-sunburst-2026-09-08";
const bildGuete = process.env.IG_CHARAKTER_GUETE || "high";
const schlafen = (ms) => new Promise((r) => setTimeout(r, ms));

async function remoteShaPruefen(url, erwartet, versuche = 8) {
  if (!url) throw new Error("Persistiertes Rohbild hat keine Remote-Referenz.");
  let letzter = "";
  for (let i = 0; i < versuche; i++) {
    try {
      const res = await fetch(url, { cache: "no-store" });
      if (res.ok) {
        const puffer = Buffer.from(await res.arrayBuffer());
        const ist = crypto.createHash("sha256").update(puffer).digest("hex");
        if (ist === erwartet) return true;
        letzter = `SHA ${ist.slice(0, 12)} statt ${erwartet.slice(0, 12)}`;
      } else letzter = `HTTP ${res.status}`;
    } catch (e) {
      letzter = String(e?.message || e);
    }
    await schlafen(1500 * (i + 1));
  }
  throw new Error(`Persistiertes Rohbild ist remote nicht SHA-identisch: ${letzter}`);
}

async function charakterTreffer(datum, slot, inhalt) {
  const vorhanden = rohbildLaden({
    basisDir: hosting.dir, datum, slot, inhalt, modell: bildModell, guete: bildGuete,
  });
  if (vorhanden) {
    await remoteShaPruefen(vorhanden.rohbild.rawUrl, vorhanden.rohbild.sha256);
    console.log(`  → Rohbild wiederverwendet: ${datum} ${slot} · ${vorhanden.rohbild.sha256.slice(0, 12)} · 0 $ neuer Provideraufwand`);
    return vorhanden;
  }

  const treffer = await titelbild(inhalt, null, {
    randFarbe: stickerFarbe(inhalt.klausur, process.env.IG_STIL || "bunt"),
    zweck: "bild",
    slot: `vorproduktion:${datum}:${slot}`,
    charaktere: true,
  });
  if (!treffer) throw new Error(`${datum} ${slot}: kein Charakter-Cover erzeugt`);

  const gespeichert = rohbildSpeichern({
    basisDir: hosting.dir,
    basisUrl: hosting.basisUrl,
    datum, slot, inhalt, treffer,
    modell: bildModell,
    guete: bildGuete,
  });
  hosting.commit(`Persistiere Rohbild ${datum} ${slot} ${gespeichert.meta.sha256.slice(0, 12)}`);
  await hosting.push();
  await remoteShaPruefen(gespeichert.meta.rawUrl, gespeichert.meta.sha256);
  console.log(`  → Rohbild dauerhaft: ${gespeichert.meta.gitPfad} · SHA-256 ${gespeichert.meta.sha256}`);

  return {
    ...treffer,
    wiederverwendet: false,
    urspruenglicheKostenUsd: Number(treffer.kostenUsd || 0),
    rohbild: gespeichert.meta,
  };
}

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

    for (const slot of feedSlots) {
      const inhalt = structuredClone(tag.inhalte?.[slot]);
      if (!inhalt) throw new Error(`${datum} ${slot}: Inhalt fehlt`);

      /* Bei Reels liegt die kreative Cover-Regie in der Hook-Szene. Fuer die
         bestehende Charakterpipeline wird sie fuer das Cover nach oben gespiegelt. */
      if (!inhalt.folien && !inhalt.coverRegie && inhalt.szenen?.[0]?.coverRegie) {
        inhalt.coverRegie = structuredClone(inhalt.szenen[0].coverRegie);
      }

      const treffer = await charakterTreffer(datum, slot, inhalt);

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
          urspruenglicheBildKostenUsd: treffer.urspruenglicheKostenUsd ?? treffer.kostenUsd ?? null,
          rohbildWiederverwendet: Boolean(treffer.wiederverwendet),
          rohbildSha256: treffer.rohbild?.sha256 || null,
          rohbildPfad: treffer.rohbild?.gitPfad || null,
          rohbildUrl: treffer.rohbild?.rawUrl || null,
          dateien: pfade.map((p) => path.basename(p)),
        });
      } else if (Array.isArray(inhalt.szenen)) {
        motivUebernehmen(inhalt, treffer);
        if (nurCover) {
          const cover = path.join(slotTemp, `${inhalt.slug || "reel"}-cover.jpg`);
          await coverRendern(coverDaten(inhalt, { gesamt: 60 }), cover, { variante: 0 });
          mTag.feed.push({
            slot,
            format: "reel-cover",
            hook: inhalt.szenen?.[0]?.titel || null,
            charaktere: treffer.charaktere || [],
            bildKostenUsd: treffer.kostenUsd ?? null,
            urspruenglicheBildKostenUsd: treffer.urspruenglicheKostenUsd ?? treffer.kostenUsd ?? null,
            rohbildWiederverwendet: Boolean(treffer.wiederverwendet),
            rohbildSha256: treffer.rohbild?.sha256 || null,
            rohbildPfad: treffer.rohbild?.gitPfad || null,
            rohbildUrl: treffer.rohbild?.rawUrl || null,
            dateien: [path.basename(cover)],
            reel: null,
          });
        } else {
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
            urspruenglicheBildKostenUsd: treffer.urspruenglicheKostenUsd ?? treffer.kostenUsd ?? null,
            rohbildWiederverwendet: Boolean(treffer.wiederverwendet),
            rohbildSha256: treffer.rohbild?.sha256 || null,
            rohbildPfad: treffer.rohbild?.gitPfad || null,
            rohbildUrl: treffer.rohbild?.rawUrl || null,
            dateien: [path.basename(r.cover), path.basename(r.video)],
            reel: {
              dauer: r.dauer,
              stimme: r.anbieter,
              layout: r.layout,
            },
          });
        }
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
      .filter(([s, x]) => /^s\d+$/.test(s) && x?.art && (!storySlots.length || storySlots.includes(s)))) {
      const ziel = path.join(storyDir, `${slot}-${story.art}.jpg`);
      await storyRendern(structuredClone(story), ziel, { variante: 0 });
      mTag.stories.push({ slot, art: story.art, datei: path.basename(ziel) });
    }

    const aktuelleBildKosten = Number(mTag.feed.reduce((summe, x) => summe + Number(x.bildKostenUsd || 0), 0).toFixed(6));
    if (patchModus) {
      tag.renderVorschau = {
        ...(tag.renderVorschau || {}),
        letzteReparatur: {
          erzeugtAm: new Date().toISOString(),
          feedSlots,
          storySlots,
          nurCover,
          bildKostenUsd: aktuelleBildKosten,
          textProviderKostenUsd: 0,
          faktencheckProviderKostenUsd: 0,
          bildQaProviderKostenUsd: 0,
        },
        freigabeBetreiber: false,
      };
    } else {
      tag.renderVorschau = {
        status: "fertig",
        erzeugtAm: new Date().toISOString(),
        pfad: `vorproduktion/${datum}/fertig`,
        textProviderKostenUsd: 0,
        faktencheckProviderKostenUsd: 0,
        bildQaProviderKostenUsd: 0,
        bildKostenUsd: aktuelleBildKosten,
        freigabeBetreiber: false,
      };
    }
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

/* Kostenaggregate werden aus der dauerhaften Einzelkostenhistorie neu
   abgeleitet. So gehen auch Bildkosten eines vorher abgebrochenen Preview-
   Laufs nicht verloren und werden zugleich niemals doppelt addiert. */
await journal.abschluss();
{
  const k = hosting.jsonLesen("kosten.json", { wochen: {}, tage: {} });
  k.tage ||= {};
  k.wochen ||= {};

  const liste = (k.einzelkosten?.[kostenDatum] || [])
    .filter((e) => e?.kostenBekannt && Number.isFinite(Number(e.kostenUsd)));
  const zwecke = {};
  const messungen = { ...(k.tage[kostenDatum]?.messungen || {}) };
  let usd = 0;
  let aufrufe = 0;

  for (const e of liste) {
    const betrag = Number(e.kostenUsd || 0);
    usd += betrag;
    if (betrag > 0) aufrufe += 1;
    if (e.zweck) {
      zwecke[e.zweck] = Number(((zwecke[e.zweck] || 0) + betrag).toFixed(6));
      if (betrag > 0) messungen[e.zweck] = Number(Math.max(Number(messungen[e.zweck] || 0), betrag).toFixed(6));
    }
  }

  const antworten = Number(((zwecke.kommentare || 0) + (zwecke.nachrichten || 0)).toFixed(6));
  k.tage[kostenDatum] = {
    ...(k.tage[kostenDatum] || {}),
    usd: Number(usd.toFixed(6)),
    antworten,
    aufrufe,
    zwecke,
    messungen,
    stand: new Date().toISOString(),
  };

  const key = kw(kostenDatum);
  const wochenTage = Object.entries(k.tage).filter(([datum]) => {
    try { return kw(datum) === key; } catch { return false; }
  });
  const wochenUsd = wochenTage.reduce((s, [, tag]) => s + Number(tag?.usd || 0), 0);
  const wochenAufrufe = wochenTage.reduce((s, [, tag]) => s + Number(tag?.aufrufe || 0), 0);
  const altWoche = k.wochen[key] || {};
  const cacheSumme = Number(altWoche.cacheSumme || 0);
  k.wochen[key] = {
    ...altWoche,
    usd: Number(wochenUsd.toFixed(6)),
    aufrufe: wochenAufrufe,
    cacheSumme,
    cacheAnteil: wochenAufrufe ? cacheSumme / wochenAufrufe : 0,
  };
  hosting.jsonSchreiben("kosten.json", k);
}

/* Fertige Cover/Videos kommen weiterhin erst nach komplett erfolgreichem
   Rendering in den Review-Ordner. Die kostenpflichtigen Rohbilder wurden
   dagegen bereits einzeln direkt nach ihrer Erzeugung committed, gepusht
   und per SHA-256 remote verifiziert. */
for (const datum of tage) {
  const ziel = path.join(hosting.dir, "vorproduktion", datum, "fertig");
  const quelle = path.join(temp, datum);
  if (patchModus) {
    fs.mkdirSync(ziel, { recursive: true });
    for (const slot of feedSlots) {
      const q = path.join(quelle, slot);
      if (fs.existsSync(q)) fs.cpSync(q, path.join(ziel, slot), { recursive: true });
    }
    const qStories = path.join(quelle, "stories");
    if (fs.existsSync(qStories)) {
      fs.mkdirSync(path.join(ziel, "stories"), { recursive: true });
      for (const datei of fs.readdirSync(qStories)) {
        fs.copyFileSync(path.join(qStories, datei), path.join(ziel, "stories", datei));
      }
    }
  } else {
    fs.rmSync(ziel, { recursive: true, force: true });
    fs.mkdirSync(path.dirname(ziel), { recursive: true });
    fs.cpSync(quelle, ziel, { recursive: true });
  }
  fs.writeFileSync(
    path.join(hosting.dir, "vorproduktion", `${datum}.json`),
    JSON.stringify(tagesUpdates.get(datum), null, 2) + "\n",
  );
}
fs.writeFileSync(
  path.join(hosting.dir, "vorproduktion", patchModus ? "render-reparatur-manifest.json" : "render-manifest.json"),
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
  patchModus,
  feedSlots,
  storySlots,
  nurCover,
  ziel: tage.map((d) => `vorproduktion/${d}/fertig`),
}, null, 2));
