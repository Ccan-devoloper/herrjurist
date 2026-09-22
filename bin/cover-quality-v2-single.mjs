#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";
import { execFileSync } from "node:child_process";
import { fileURLToPath } from "node:url";
import { themenpool, FAECHER } from "../src/inhalte.mjs";
import { CHARAKTERE, charaktereFuer } from "../src/charakterbild.mjs";
import { aiCoverZeichnen } from "../src/cover-ai-first.mjs";
import { beitragRendern, browserBeenden } from "../src/render.mjs";
import { titelZeilen } from "../src/vorlagen.mjs";
import { budgetStarten } from "../src/budget.mjs";
import { kontextSetzen, kontextLoeschen, openaiAufruf } from "../src/anbieter.mjs";
import { budgetSetzen } from "../src/kosten.mjs";
import { CONFIG } from "../src/config.mjs";

const hier = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(hier, "..");
const out = path.join(root, "out", "cover-quality-v2-single");
const coversDir = path.join(out, "covers");
const motifsDir = path.join(out, "motifs");
fs.rmSync(out, { recursive: true, force: true });
fs.mkdirSync(coversDir, { recursive: true });
fs.mkdirSync(motifsDir, { recursive: true });

const events = [];
const telemetrie = { aufruf(e) { events.push({ zeit: new Date().toISOString(), ...e }); } };
const budget = budgetStarten({
  deckel: { core: 0.35, engagement: 0, research: 0 },
  bisher: { core: 0, engagement: 0, research: 0 },
  protokoll: () => {},
});
budgetSetzen({ limitUsd: 0.35, antwortLimitUsd: 0.35 });
kontextSetzen({ budget, telemetrie, journal: null, kanal: "herrjurist-cover-quality-v2-single-sterbehilfe", datum: "acceptance-single" });

const round = (n) => Number(Number(n || 0).toFixed(6));
const sum = (liste, feld = "actualUsd") => round(liste.reduce((a, x) => a + (Number.isFinite(Number(x?.[feld])) ? Number(x[feld]) : 0), 0));
const responsesText = (antwort) => typeof antwort?.output_text === "string"
  ? antwort.output_text
  : (antwort?.output || []).flatMap((o) => o?.content || []).filter((x) => x?.type === "output_text" || x?.type === "text").map((x) => x?.text || "").join("\n");

function dateiDaten(pfad) {
  return `data:image/png;base64,${fs.readFileSync(pfad).toString("base64")}`;
}

function dimensionen(pfad) {
  const raw = execFileSync("ffprobe", [
    "-v", "error", "-select_streams", "v:0",
    "-show_entries", "stream=width,height", "-of", "json", pfad,
  ], { encoding: "utf8" });
  const s = JSON.parse(raw)?.streams?.[0] || {};
  return { width: Number(s.width || 0), height: Number(s.height || 0) };
}

function motivAufraeumen(motiv) {
  for (const p of new Set([motiv?.pfad, motiv?.ohneRand].filter(Boolean))) fs.rmSync(p, { force: true });
}

function themaWaehlen() {
  const sterbehilfe = /sterbehilfe|t[oö]tung\s+auf\s+verlangen|suizid|behandlungsabbruch|patientenverf[uü]gung|§\s*216\s*stgb|216\s*stgb/i;
  const prioritaet = { hoch: 0, mittel: 1, niedrig: 2 };
  const kandidaten = themenpool()
    .filter((t) => Number(t.klausur) === 2)
    .filter((t) => sterbehilfe.test([
      t.titel,
      ...(t.normen || []),
      ...(t.kern?.lernziele || []),
      ...(t.kern?.pruefschritte || []),
      t.kern?.merksatz,
      ...(t.kern?.fehler || []),
    ].filter(Boolean).join(" | ")))
    .sort((a, b) =>
      (prioritaet[a.prioritaet] ?? 9) - (prioritaet[b.prioritaet] ?? 9)
      || Number(Boolean(b.kern?.merksatz)) - Number(Boolean(a.kern?.merksatz))
      || String(a.id).localeCompare(String(b.id))
    );
  if (!kandidaten.length) {
    throw new Error("Im entschlüsselten Strafrecht-Themenpool wurde kein Sterbehilfe-/§216-/Suizid-/Behandlungsabbruch-Thema gefunden. Kein Fallback-Thema wird erzeugt.");
  }
  return kandidaten[0];
}

const REGIE_SCHEMA = {
  type: "object",
  additionalProperties: false,
  properties: {
    charaktere: { type: "array", minItems: 1, maxItems: 2, items: { type: "string", enum: Object.keys(CHARAKTERE) } },
    kernidee: { type: "string" },
    handlung: { type: "string" },
    alternative: { type: "string" },
    hinweisRegie: { type: "string" },
    coverText: { type: "string" },
    coverBadge: { type: "string", enum: ["Fehlerfalle", "Examensklassiker", "Klausurrelevant", "Schemawissen", "Praxisrelevant"] },
  },
  required: ["charaktere", "kernidee", "handlung", "alternative", "hinweisRegie", "coverText", "coverBadge"],
};

async function regieErzeugen(thema, fachLabel) {
  const rollen = Object.values(CHARAKTERE).map((c) => `${c.id}: ${c.name} – ${c.kurz}`).join("\n");
  const user = [
    `Juristisches Thema: ${thema.titel}`,
    `Fach: ${fachLabel}`,
    thema.normen?.length ? `Normen: ${thema.normen.join(", ")}` : "",
    thema.kern?.lernziele?.length ? `Lernziele: ${thema.kern.lernziele.slice(0, 5).join(" | ")}` : "",
    thema.kern?.pruefschritte?.length ? `Prüfschritte: ${thema.kern.pruefschritte.slice(0, 6).join(" | ")}` : "",
    thema.kern?.merksatz ? `Merksatz: ${thema.kern.merksatz}` : "",
    "",
    "Verfügbare wiederkehrende Figuren:",
    rollen,
    "",
    "Gib eine originelle Cover-Regie. Wähle 1–2 Figuren passend zur Dramaturgie.",
    "Die Handlung muss in ENGLISCH 25–70 Wörter lang sein, genau eine klare Interaktion mit höchstens 1–2 starken Requisiten zeigen und den juristischen Gedanken ohne lesbaren Text verständlich machen.",
    "Keine Pixelkoordinaten, keine starre Links-rechts-Anordnung, keine unnötigen Objektzählungen, keine Zusatzfiguren, keine Richterhämmer/Gesetzbücher als generische Symbolik.",
    "coverText: DEUTSCH, 2–6 Wörter, höchstens 36 Zeichen, zusätzlicher Aha-Effekt statt Titelwiederholung.",
    "hinweisRegie: ENGLISCH, 18–55 Wörter. Entscheide kreativ, wo der handschriftliche coverText in der konkreten Szene natürlich sitzt, wie der lockere Pfeil läuft und auf welches konkrete Szenenelement er zeigt. Keine Pixelkoordinaten und keine feste Links-/Rechtszone.",
  ].filter(Boolean).join("\n");
  const params = {
    model: "gpt-5.4-mini",
    reasoning: { effort: "low" },
    max_output_tokens: 900,
    input: [{ role: "user", content: [{ type: "input_text", text: user }] }],
    text: { format: { type: "json_schema", name: "herrjurist_single_cover_regie", strict: true, schema: REGIE_SCHEMA } },
  };
  const antwort = await openaiAufruf({
    zweck: "bildregie",
    modell: "gpt-5.4-mini",
    params,
    optional: false,
    admissionInputTokens: 2200,
    slot: "single-cover-regie-sterbehilfe",
    promptVersion: "single-cover-regie-v1",
  });
  const roh = responsesText(antwort);
  const daten = JSON.parse(roh.slice(roh.indexOf("{"), roh.lastIndexOf("}") + 1));
  daten.coverText = String(daten.coverText || "").replace(/\s+/g, " ").trim().slice(0, 36);
  return daten;
}

let report;
try {
  const thema = themaWaehlen();
  const fachLabel = FAECHER[thema.fach]?.label || "Strafrecht";
  const regie = await regieErzeugen(thema, fachLabel);
  const slot = "single-strafrecht-sterbehilfe";
  const folie = {
    art: "titel",
    titel: thema.titel,
    titelZeilen: titelZeilen(thema.titel),
    icon: "paragraf",
    coverText: regie.coverText,
    coverBadge: regie.coverBadge,
  };
  const ziel = {
    format: "pruefungsfrage",
    fach: thema.fach,
    klausur: 2,
    fachLabel,
    themaId: thema.id,
    slug: slot,
    titel: thema.titel,
    kurztitel: thema.titel,
    coverText: regie.coverText,
    coverBadge: regie.coverBadge,
    coverRegie: {
      charaktere: regie.charaktere,
      kernidee: regie.kernidee,
      handlung: regie.handlung,
      alternative: regie.alternative,
      hinweisRegie: regie.hinweisRegie,
    },
    folien: [folie],
  };

  const selectedCharacterIds = charaktereFuer(ziel).map((x) => x.id);
  const motiv = await aiCoverZeichnen(ziel, { slot });
  if (!motiv) throw new Error("Kein AI-first Komplettcover hat die visuelle QA bestanden.");

  try {
    const motivDatei = path.join(motifsDir, `${slot}-ai-first.png`);
    fs.copyFileSync(motiv.pfad, motivDatei);
    folie.bild = dateiDaten(motivDatei);
    folie.bildFrei = false;
    folie.bildBreite = motiv.breite || 1080;
    folie.bildHoehe = motiv.hoehe || 1350;
    folie.bildTyp = "ai-cover";
    folie.bildCharaktere = motiv.charaktere;
    folie.coverQa = motiv.qa || null;
    const beitrag = {
      format: "pruefungsfrage",
      fach: thema.fach,
      klausur: 2,
      fachLabel,
      slug: slot,
      folien: [folie],
    };
    const [render] = await beitragRendern(beitrag, coversDir, { variante: 0 });
    const datei = path.join(coversDir, "cover.jpg");
    if (render !== datei) fs.renameSync(render, datei);
    const dim = dimensionen(datei);
    if (dim.width !== 1080 || dim.height !== 1350) throw new Error(`Falsches Coverformat ${dim.width}x${dim.height}`);

    const unbekannt = events.some((e) => e.spendUnknown);
    if (unbekannt) throw new Error("Providerverbrauch enthält unbekannte Kosten.");

    report = {
      generatedAt: new Date().toISOString(),
      branch: process.env.GITHUB_REF_NAME || "feature/cover-quality-v2",
      commit: process.env.GITHUB_SHA || null,
      topic: {
        id: thema.id,
        title: thema.titel,
        fach: thema.fach,
        fachLabel,
        normen: thema.normen || [],
        prioritaet: thema.prioritaet || null,
      },
      cover: {
        titleLines: titelZeilen(thema.titel),
        coverText: regie.coverText,
        coverBadge: regie.coverBadge,
        director: {
          characterIds: regie.charaktere,
          coreIdea: regie.kernidee,
          action: regie.handlung,
          alternative: regie.alternative,
          annotationDirection: regie.hinweisRegie,
        },
        selectedCharacterIds,
        renderedCharacterIds: motiv.charakterIds,
        renderedCharacters: motiv.charaktere,
        quality: motiv.quality,
        attempt: motiv.attempt,
        qaFirstPass: motiv.qaFirstPass,
        qaAttempts: motiv.qaAttempts,
        finalQa: motiv.qa || null,
        aiFirst: true,
        imagePath: path.relative(root, datei),
        motifPath: path.relative(root, motivDatei),
        motifDimensions: { width: Number(motiv.breite || 0), height: Number(motiv.hoehe || 0) },
        dimensions: dim,
      },
      costUsd: {
        director: sum(events.filter((e) => e.purpose === "bildregie")),
        image: sum(events.filter((e) => e.purpose === "bild" || e.purpose === "erklaerbild")),
        visionQa: sum(events.filter((e) => e.purpose === "bild-qa")),
        total: sum(events),
      },
      model: CONFIG.bilder.charaktere.modell,
      qaModel: CONFIG.bilder.charaktere.qaModell,
      calls: events,
    };
    fs.writeFileSync(path.join(out, "manifest.json"), JSON.stringify(report, null, 2));
    fs.writeFileSync(path.join(out, "README.txt"), [
      "Herrjurist AI-first – single Strafrecht Sterbehilfe acceptance",
      `Topic: ${thema.titel}`,
      `Artifact cover: ${path.relative(root, datei)}`,
      `Measured provider cost: $${report.costUsd.total.toFixed(6)}`,
      "Exactly one AI-first full cover was generated. No reel and no publishing.",
    ].join("\n") + "\n");
    console.log(JSON.stringify({ topic: thema.titel, costUsd: report.costUsd, quality: motiv.quality, attempt: motiv.attempt }, null, 2));
  } finally {
    motivAufraeumen(motiv);
  }
} catch (e) {
  fs.writeFileSync(path.join(out, "error.txt"), String(e?.stack || e));
  throw e;
} finally {
  await browserBeenden().catch(() => {});
  kontextLoeschen();
}
