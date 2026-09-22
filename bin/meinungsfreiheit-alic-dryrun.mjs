#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { fileURLToPath } from "node:url";
import { THEMEN } from "../daten/themen.loader.mjs";
import { beitragRendern, browserBeenden } from "../src/render.mjs";

const hier = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(hier, "..");
const sourceDir = path.resolve(root, process.env.HJ_ALIC_SOURCE || ".alic-source");
const motif = path.join(sourceDir, "motifs", "single-strafrecht-alic.png");
if (!fs.existsSync(motif)) throw new Error(`ALIC-Motiv fehlt: ${motif}`);

const out = path.join(root, "out", "meinungsfreiheit-alic-dryrun");
fs.rmSync(out, { recursive: true, force: true });
fs.mkdirSync(out, { recursive: true });

const norm = (v) => String(v || "").toLowerCase()
  .normalize("NFD").replace(/[\u0300-\u036f]/g, "")
  .replace(/ß/g, "ss");

const topic = THEMEN.find((t) => norm(t.titel || t.title).includes("meinungsfreiheit"))
  || THEMEN.find((t) => norm(JSON.stringify(t)).includes("meinungsfreiheit"));

if (!topic) {
  const candidates = THEMEN.filter((t) => {
    const hay = norm(JSON.stringify(t));
    return hay.includes("meinung") || hay.includes("art. 5") || hay.includes("art 5") || hay.includes("grundrecht");
  }).slice(0, 40).map((t) => ({
    id: t.id || t.themaId || null,
    titel: t.titel || t.title || null,
    normen: t.normen || null,
    fach: t.fach || null,
    fachLabel: t.fachLabel || null
  }));
  console.log("DIAG_MATCHING_TOPICS=" + JSON.stringify(candidates));
  throw new Error("Thema 'Meinungsfreiheit' nicht im entschlüsselten Themenpool gefunden.");
}

const motifBytes = fs.readFileSync(motif);
const motifData = `data:image/png;base64,${motifBytes.toString("base64")}`;
const fach = topic.fach || "grundr";
const fachLabel = topic.fachLabel || "Grundrechte";
const themaId = topic.id || topic.themaId || "dryrun-meinungsfreiheit";

const inhalt = {
  format: "lernkarte",
  fach,
  klausur: 3,
  fachLabel,
  themaId,
  folien: [
    {
      art: "titel",
      titel: "Meinungsfreiheit: Wie prüfst du Art. 5 GG?",
      titelZeilen: ["Meinungsfreiheit:", "Wie prüfst du", "Art. 5 GG?"],
      icon: "megafon",
      prioritaet: "hoch",
      prioritaetText: "Grundrechtsklassiker",
      coverBadge: "Grundrechtsklassiker",
      coverText: "Schutzbereich weit",
      bild: motifData,
      bildQuelle: null,
      bildFrei: true,
      bildTyp: "charakter",
      bildBreite: 1024,
      bildHoehe: 918,
      coverHinweisPlan: {
        noteX: 0.70, noteY: 0.42,
        targetX: 0.68, targetY: 0.56,
        rotationDeg: -5, bend: 0
      }
    },
    {
      art: "text",
      titel: "Schutzbereich",
      punkte: [
        "Art. 5 Abs. 1 S. 1 GG schützt das Äußern und Verbreiten von Meinungen in Wort, Schrift und Bild.",
        "Meinungen sind durch Stellungnahme, Dafürhalten oder Wertung geprägt. Auf ihren Inhalt oder ihre Qualität kommt es für die Eröffnung des Schutzbereichs grundsätzlich nicht an.",
        "Auch scharfe, polemische oder überspitzte Formulierungen können vom Schutzbereich erfasst sein."
      ]
    },
    {
      art: "vergleich",
      titel: "Meinung oder Tatsache?",
      links: {
        titel: "Werturteil",
        punkte: [
          "subjektive Bewertung",
          "nicht wahr oder falsch beweisbar",
          "Kernbereich des Art. 5 Abs. 1 GG"
        ]
      },
      rechts: {
        titel: "Tatsachenbehauptung",
        punkte: [
          "dem Beweis zugänglich",
          "kann geschützt sein, wenn sie der Meinungsbildung dient",
          "bewusst oder erwiesen unwahre Tatsachen genießen keinen entsprechenden Schutz"
        ]
      }
    },
    {
      art: "text",
      titel: "Eingriff",
      punkte: [
        "Ein Eingriff liegt vor, wenn staatliches Handeln die Äußerung oder Verbreitung einer geschützten Meinung erschwert, sanktioniert oder verhindert.",
        "Typische Klausurfälle sind straf- oder zivilrechtliche Folgen einer Äußerung sowie behördliche Verbote oder Auflagen.",
        "Bei gerichtlichen Entscheidungen ist zu prüfen, ob Bedeutung und Tragweite der Meinungsfreiheit bei Auslegung und Anwendung des einfachen Rechts beachtet wurden."
      ]
    },
    {
      art: "schritte",
      titel: "Schranken: Art. 5 Abs. 2 GG",
      schritte: [
        {
          titel: "Allgemeine Gesetze",
          text: "Die Vorschrift darf sich nicht gegen eine bestimmte Meinung als solche richten, sondern muss ein von der konkreten Meinung unabhängiges Rechtsgut schützen."
        },
        {
          titel: "Jugendschutz",
          text: "Gesetzliche Bestimmungen zum Schutz der Jugend bilden eine ausdrücklich genannte Schranke."
        },
        {
          titel: "Persönliche Ehre",
          text: "Auch der Schutz der persönlichen Ehre ist ausdrücklich als Schranke genannt."
        }
      ]
    },
    {
      art: "merke",
      titel: "Wechselwirkungslehre",
      text: "Die Schranken begrenzen die Meinungsfreiheit – zugleich müssen die einschränkenden Gesetze im Lichte der besonderen Bedeutung von Art. 5 Abs. 1 GG ausgelegt und angewendet werden."
    },
    {
      art: "cta",
      titel: "Für Grundrechte speichern",
      text: "Schema merken: Schutzbereich → Eingriff → Schranke nach Art. 5 Abs. 2 GG → verfassungsgemäße Anwendung, insbesondere Wechselwirkungslehre und Verhältnismäßigkeit."
    }
  ],
  caption: "Meinungsfreiheit in der Grundrechtsklausur: Schutzbereich, Eingriff und die Schranken des Art. 5 Abs. 2 GG sauber trennen. Bei der Rechtfertigung die Wechselwirkungslehre nicht vergessen.",
  hashtags: ["#jura","#jurastudium","#staatsexamen","#grundrechte","#oeffentlichesrecht","#meinungsfreiheit","#art5gg"],
  kurztitel: "Meinungsfreiheit",
  coverText: "Schutzbereich weit",
  coverBadge: "Grundrechtsklassiker",
  quellen: [
    ...(Array.isArray(topic.normen) ? topic.normen : []),
    "Art. 5 Abs. 1 S. 1 GG",
    "Art. 5 Abs. 2 GG",
    "BVerfGE 7, 198 (Lüth)"
  ],
  hookTyp: "frage",
  slug: "dryrun-meinungsfreiheit-alic",
  befundeTypisiert: true,
  manuellGeprueft: true,
  finalisiertVon: "chat-dryrun"
};

const files = await beitragRendern(inhalt, path.join(out, "rendered"), { variante: 0 });
const cover = files.find((f) => /-01\.jpg$/i.test(f)) || files[0];
fs.copyFileSync(motif, path.join(out, "single-strafrecht-alic.png"));
fs.copyFileSync(cover, path.join(out, "cover.jpg"));

const manifest = {
  generatedAt: new Date().toISOString(),
  productionBaseCommit: process.env.DRYRUN_BASE_COMMIT || null,
  dryRunCommit: process.env.GITHUB_SHA || null,
  topicSource: "encrypted-themenpool",
  topic,
  motif: "single-strafrecht-alic.png",
  motifSourceArtifactId: 10674227857,
  motifSourceRunId: 35681116751,
  motifSha256: crypto.createHash("sha256").update(motifBytes).digest("hex"),
  motifDimensions: { width: 1024, height: 918 },
  targetContract: "current production main / Cover Quality v2 / no-arrow / no cover counter",
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
  "Motif: exact existing single-strafrecht-alic.png from saved artifact",
  "Renderer: current production main contract",
  "Provider/API cost: $0.00",
  "No publishing performed."
].join("\n"));

await browserBeenden();
console.log(JSON.stringify({
  topic: { id: themaId, title: topic.titel || topic.title, normen: topic.normen, fach, fachLabel },
  motif: "single-strafrecht-alic.png",
  providerCostUsd: 0,
  externalProviderCalls: false,
  publishingPerformed: false,
  outputs: files.length,
  cover: path.relative(out, cover)
}, null, 2));
