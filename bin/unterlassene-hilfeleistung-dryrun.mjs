#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { fileURLToPath } from "node:url";
import { THEMEN } from "../daten/themen.loader.mjs";
import { beitragRendern, browserBeenden } from "../src/render.mjs";

const hier = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(hier, "..");
const sourceDir = path.resolve(root, process.env.HJ_FAHR_SOURCE || ".fahr-source");
const candidates = [
  path.join(sourceDir, "single-strafrecht-fahrlaessige-toetung.png"),
  path.join(sourceDir, "debug", "attempt-2-xhigh", "raw.png"),
  path.join(sourceDir, "debug", "attempt-1-high", "raw.png"),
];
const motif = candidates.find(fs.existsSync);
if (!motif) throw new Error("Kein vorhandenes Fahrlaessige-Toetung-Motiv gefunden.");

const out = path.join(root, "out", "unterlassene-hilfeleistung-dryrun");
fs.rmSync(out, { recursive: true, force: true });
fs.mkdirSync(out, { recursive: true });

const norm = (v) => String(v || "").toLowerCase()
  .normalize("NFD").replace(/[\u0300-\u036f]/g, "");
const poolTopic = THEMEN.find((t) => norm(t.titel || t.title).includes("unterlassene hilfeleistung"))
  || THEMEN.find((t) => JSON.stringify(t).includes("323c"));
const topic = poolTopic || {
  id: "dryrun-strafbt-323c",
  titel: "Unterlassene Hilfeleistung",
  fach: "strafbt",
  fachLabel: "Strafrecht BT",
  normen: ["§ 323c Abs. 1 StGB"],
  prioritaet: "hoch"
};
const topicSource = poolTopic ? "encrypted-themenpool" : "manual-fallback-requested-theme-not-present-in-pool";
if (!poolTopic) {
  console.log("THEMENPOOL_NOTE=Unterlassene Hilfeleistung / § 323c is not present in the encrypted Themenpool; using a clearly marked dry-run-only manual fallback so the visual regression can complete.");
}

const motifBytes = fs.readFileSync(motif);
const motifData = `data:image/png;base64,${motifBytes.toString("base64")}`;

const fach = topic.fach || "strafbt";
const fachLabel = topic.fachLabel || "Strafrecht BT";
const themaId = topic.id || topic.themaId || "strafbt-323c";

const inhalt = {
  format: "minifall",
  fach,
  klausur: 2,
  fachLabel,
  themaId,
  folien: [
    {
      art: "titel",
      titel: "Unterlassene Hilfeleistung: § 323c StGB?",
      titelZeilen: ["Unterlassene", "Hilfeleistung:", "§ 323c StGB?"],
      icon: "warnung",
      prioritaet: "hoch",
      prioritaetText: "Klausurrelevant",
      coverBadge: "Klausurrelevant",
      coverText: "Garantenstellung nicht nötig",
      bild: motifData,
      bildQuelle: null,
      bildFrei: true,
      bildTyp: "charakter",
      bildBreite: 1024,
      bildHoehe: 1024,
      coverHinweisPlan: {
        noteX: 0.18, noteY: 0.18,
        targetX: 0.83, targetY: 0.46,
        rotationDeg: -5, bend: 0.35
      }
    },
    {
      art: "text",
      titel: "Sachverhalt",
      text: "A sieht nach einem Fahrradsturz den verletzten B reglos am Straßenrand liegen. A könnte gefahrlos den Notruf wählen und Hilfe organisieren. Trotzdem fährt er aus Bequemlichkeit weiter."
    },
    {
      art: "schritte",
      titel: "§ 323c Abs. 1 StGB",
      schritte: [
        {
          titel: "Unglücksfall, gemeine Gefahr oder Not",
          text: "Ein plötzliches Ereignis muss erhebliche Gefahren für Personen oder bedeutende Rechtsgüter auslösen."
        },
        {
          titel: "Hilfe ist erforderlich",
          text: "Erforderlich ist die Hilfe, die aus ex-ante-Sicht geeignet und nötig ist. Häufig genügt schon ein sofortiger Notruf."
        },
        {
          titel: "Hilfe ist zumutbar",
          text: "Die Hilfe muss ohne erhebliche eigene Gefahr und ohne Verletzung anderer wichtiger Pflichten möglich sein."
        }
      ]
    },
    {
      art: "text",
      titel: "Keine Garantenstellung nötig",
      punkte: [
        "§ 323c StGB ist ein eigenständiges echtes Unterlassungsdelikt: Täter kann grundsätzlich jedermann sein.",
        "Anders als bei § 13 StGB braucht A deshalb keine besondere Garantenpflicht gegenüber B.",
        "Wie weit A helfen muss, hängt von der konkreten Lage ab; jedenfalls darf er eine ohne Risiko mögliche Mindesthilfe nicht einfach unterlassen."
      ]
    },
    {
      art: "text",
      titel: "Ergebnis im Fall",
      punkte: [
        "Der Fahrradsturz mit dem verletzten B ist ein Unglücksfall.",
        "Ein Notruf wäre für A erforderlich, möglich und ohne erhebliche Eigengefährdung zumutbar gewesen.",
        "Fährt A vorsätzlich weiter, obwohl er die Hilfesituation erkennt, ist § 323c Abs. 1 StGB erfüllt."
      ]
    },
    {
      art: "merke",
      titel: "Merksatz",
      text: "Bei § 323c StGB zuerst Hilfesituation, Erforderlichkeit und Zumutbarkeit prüfen. Eine Garantenstellung wie bei § 13 StGB braucht es nicht."
    },
    {
      art: "cta",
      titel: "Für Strafrecht BT speichern",
      text: "Im Klausurfall § 323c StGB nicht mit dem unechten Unterlassen nach § 13 StGB vermischen."
    }
  ],
  caption: "Unterlassene Hilfeleistung nach § 323c Abs. 1 StGB setzt eine Hilfesituation, erforderliche und zumutbare Hilfe sowie Vorsatz voraus. Eine Garantenstellung ist nicht erforderlich.",
  hashtags: ["#jura","#jurastudium","#staatsexamen","#strafrecht","#strafrechtbt","#323cstgb","#unterlassenehilfeleistung","#examenswissen"],
  kurztitel: "§ 323c StGB: Hilfeleistung",
  coverText: "Garantenstellung nicht nötig",
  coverBadge: "Klausurrelevant",
  quellen: ["§ 323c Abs. 1 StGB"],
  hookTyp: "frage",
  slug: "dryrun-unterlassene-hilfeleistung",
  befundeTypisiert: true,
  manuellGeprueft: true,
  finalisiertVon: "chat-dryrun"
};

const files = await beitragRendern(inhalt, path.join(out, "rendered"), { variante: 0 });
const cover = files.find((f) => /-01\.jpg$/i.test(f)) || files[0];
fs.copyFileSync(motif, path.join(out, "single-strafrecht-fahrlaessige-toetung.png"));
fs.copyFileSync(cover, path.join(out, "cover.jpg"));

const manifest = {
  generatedAt: new Date().toISOString(),
  productionBaseCommit: "94abb7742b2383cb85fbbedc634c0329b441be5f",
  dryRunCommit: process.env.GITHUB_SHA || null,
  topic: topic,
  topicSource,
  motif: "single-strafrecht-fahrlaessige-toetung.png",
  motifOriginalPath: path.relative(root, motif),
  motifSourceArtifactId: 10676033128,
  motifSourceRunId: 35684151355,
  motifSha256: crypto.createHash("sha256").update(motifBytes).digest("hex"),
  targetContract: "Cover Quality v2 / no-arrow / one handwritten note",
  providerCostUsd: 0,
  externalProviderCalls: false,
  publishingPerformed: false,
  textDirection: "Manual by ChatGPT; no provider/API call in workflow.",
  outputs: files.map((f) => path.relative(out, f)),
  cover: path.relative(out, cover)
};
fs.writeFileSync(path.join(out, "manifest.json"), JSON.stringify(manifest, null, 2));
fs.writeFileSync(path.join(out, "README.txt"), [
  "Herr Jurist – zero-cost production renderer dry run",
  "Theme: Unterlassene Hilfeleistung",
  `Theme source: ${topicSource}`,
  "Motif: existing Fahrlaessige-Toetung transparent PNG",
  "Renderer: current production main contract",
  "Provider/API cost: $0.00",
  "No publishing performed."
].join("\n"));

await browserBeenden();
console.log(JSON.stringify({
  topic: { id: themaId, title: topic.titel || topic.title, normen: topic.normen, source: topicSource },
  motif: path.relative(root, motif),
  providerCostUsd: 0,
  externalProviderCalls: false,
  outputs: files.length,
  cover: path.relative(out, cover)
}, null, 2));
