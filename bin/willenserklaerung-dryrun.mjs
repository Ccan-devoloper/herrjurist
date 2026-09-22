#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { fileURLToPath } from "node:url";
import { THEMEN } from "../daten/themen.loader.mjs";
import { beitragRendern, browserBeenden } from "../src/render.mjs";

const hier = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(hier, "..");
const sourceDir = path.resolve(root, process.env.HJ_SINGLE_SOURCE || ".single-source");
const motif = path.join(sourceDir, "motifs", "single-strafrecht.png");
if (!fs.existsSync(motif)) throw new Error(`Motiv fehlt: ${motif}`);

const out = path.join(root, "out", "willenserklaerung-dryrun");
fs.rmSync(out, { recursive: true, force: true });
fs.mkdirSync(out, { recursive: true });

const norm = (v) => String(v || "").toLowerCase()
  .normalize("NFD").replace(/[\u0300-\u036f]/g, "")
  .replace(/ß/g, "ss");

const topic = THEMEN.find((t) => norm(t.titel || t.title).includes("willenserklarung"))
  || THEMEN.find((t) => norm(JSON.stringify(t)).includes("willenserklar"));
if (!topic) {
  const candidates = THEMEN.filter((t) => {
    const hay = norm(JSON.stringify(t));
    return hay.includes("willen") || hay.includes("erklar") || hay.includes("bgb at");
  }).slice(0,30).map((t) => ({
    id: t.id || t.themaId || null,
    titel: t.titel || t.title || null,
    normen: t.normen || null,
    fach: t.fach || null,
    fachLabel: t.fachLabel || null
  }));
  console.log("DIAG_MATCHING_TOPICS=" + JSON.stringify(candidates));
  throw new Error("Thema 'Willenserklärung' nicht im entschlüsselten Themenpool gefunden.");
}

const motifBytes = fs.readFileSync(motif);
const motifData = `data:image/png;base64,${motifBytes.toString("base64")}`;
const fach = topic.fach || "bgbat";
const fachLabel = topic.fachLabel || "BGB AT";
const themaId = topic.id || topic.themaId || "dryrun-willenserklaerung";

const inhalt = {
  format: "lernkarte",
  fach,
  klausur: 1,
  fachLabel,
  themaId,
  folien: [
    {
      art: "titel",
      titel: "Willenserklärung: Was zählt wirklich?",
      titelZeilen: ["Willenserklärung:", "Was zählt", "wirklich?"],
      icon: "stift",
      prioritaet: "hoch",
      prioritaetText: "Examensbasis",
      coverBadge: "Examensbasis",
      coverText: "Äußerer + innerer Tatbestand",
      bild: motifData,
      bildQuelle: null,
      bildFrei: true,
      bildTyp: "charakter",
      bildBreite: 1024,
      bildHoehe: 960,
      coverHinweisPlan: {
        noteX: 0.70, noteY: 0.43,
        targetX: 0.72, targetY: 0.55,
        rotationDeg: -5, bend: 0
      }
    },
    {
      art: "text",
      titel: "Die Grundidee",
      text: "Eine Willenserklärung ist die Äußerung eines privaten Willens, die auf die Herbeiführung einer Rechtsfolge gerichtet ist. In der Klausur trennst du objektiven und subjektiven Tatbestand."
    },
    {
      art: "schritte",
      titel: "Objektiver Tatbestand",
      schritte: [
        {
          titel: "Erklärungsverhalten",
          text: "Es muss ein nach außen hervortretendes Verhalten vorliegen – ausdrücklich oder konkludent."
        },
        {
          titel: "Rechtsbindungswille",
          text: "Aus Sicht eines objektiven Empfängers muss das Verhalten als rechtlich verbindliche Erklärung erscheinen."
        },
        {
          titel: "Auslegung",
          text: "Entscheidend ist nicht nur der Wortlaut. §§ 133, 157 BGB und der objektive Empfängerhorizont bestimmen den Erklärungswert."
        }
      ]
    },
    {
      art: "text",
      titel: "Subjektiver Tatbestand",
      punkte: [
        "Handlungswille: Der Erklärende handelt überhaupt bewusst.",
        "Erklärungsbewusstsein: Er erkennt oder hätte erkennen können, dass sein Verhalten als rechtserhebliche Erklärung verstanden wird.",
        "Geschäftswille: Der Wille zu genau dieser Rechtsfolge ist für das Vorliegen einer Willenserklärung nicht zwingend erforderlich; sein Fehlen kann aber für die Anfechtung wichtig werden."
      ]
    },
    {
      art: "text",
      titel: "Zugang nicht vergessen",
      punkte: [
        "Bei empfangsbedürftigen Willenserklärungen wird die Erklärung grundsätzlich erst mit Zugang wirksam.",
        "Zugang liegt vor, wenn sie in den Machtbereich des Empfängers gelangt und unter normalen Umständen mit Kenntnisnahme zu rechnen ist.",
        "Für Abwesende ist § 130 Abs. 1 S. 1 BGB der klassische Ausgangspunkt."
      ]
    },
    {
      art: "merke",
      titel: "Klausur-Merksatz",
      text: "Erst auslegen, dann anfechten: Zuerst wird ermittelt, welchen objektiven Erklärungswert das Verhalten hat. Erst danach prüfst du, ob Wille und Erklärung auseinanderfallen."
    },
    {
      art: "cta",
      titel: "Für BGB AT speichern",
      text: "Schema merken: objektiver Tatbestand → subjektiver Tatbestand → bei Empfangsbedürftigkeit Zugang → erst danach mögliche Willensmängel."
    }
  ],
  caption: "Willenserklärung im BGB AT: objektiver und subjektiver Tatbestand sauber trennen, den Erklärungswert auslegen und bei empfangsbedürftigen Erklärungen den Zugang nach § 130 Abs. 1 S. 1 BGB prüfen.",
  hashtags: ["#jura","#jurastudium","#staatsexamen","#bgbat","#zivilrecht","#willenserklärung","#examenswissen"],
  kurztitel: "Willenserklärung",
  coverText: "Äußerer + innerer Tatbestand",
  coverBadge: "Examensbasis",
  quellen: Array.isArray(topic.normen) && topic.normen.length ? topic.normen : ["§§ 133, 157 BGB", "§ 130 Abs. 1 S. 1 BGB"],
  hookTyp: "frage",
  slug: "dryrun-willenserklaerung",
  befundeTypisiert: true,
  manuellGeprueft: true,
  finalisiertVon: "chat-dryrun"
};

const files = await beitragRendern(inhalt, path.join(out, "rendered"), { variante: 0 });
const cover = files.find((f) => /-01\.jpg$/i.test(f)) || files[0];
fs.copyFileSync(motif, path.join(out, "single-strafrecht.png"));
fs.copyFileSync(cover, path.join(out, "cover.jpg"));

const manifest = {
  generatedAt: new Date().toISOString(),
  productionBaseCommit: "94abb7742b2383cb85fbbedc634c0329b441be5f",
  dryRunCommit: process.env.GITHUB_SHA || null,
  topicSource: "encrypted-themenpool",
  topic,
  motif: "single-strafrecht.png",
  motifSourceArtifactId: 10665974713,
  motifSourceRunId: 35658855942,
  motifSha256: crypto.createHash("sha256").update(motifBytes).digest("hex"),
  motifDimensions: { width: 1024, height: 960 },
  targetContract: "current production main / Cover Quality v2 / no-arrow",
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
  `Theme from encrypted pool: ${topic.titel || topic.title}`,
  `Theme fach: ${fachLabel}`,
  "Motif: exact existing single-strafrecht.png from saved paid artifact",
  "Renderer: current production main contract",
  "Provider/API cost: $0.00",
  "No publishing performed."
].join("\n"));

await browserBeenden();
console.log(JSON.stringify({
  topic: { id: themaId, title: topic.titel || topic.title, normen: topic.normen, fach, fachLabel },
  motif: "single-strafrecht.png",
  providerCostUsd: 0,
  externalProviderCalls: false,
  outputs: files.length,
  cover: path.relative(out, cover)
}, null, 2));
