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
const motif = path.join(sourceDir, "single-strafrecht-fahrlaessige-toetung.png");
if (!fs.existsSync(motif)) throw new Error(`Motiv fehlt: ${motif}`);

const out = path.join(root, "out", "gutglaeubiger-zweiterwerb-dryrun");
fs.rmSync(out, { recursive: true, force: true });
fs.mkdirSync(out, { recursive: true });

const norm = (v) => String(v || "").toLowerCase()
  .normalize("NFD").replace(/[\u0300-\u036f]/g, "")
  .replace(/ß/g, "ss");

const topic = THEMEN.find((t) => norm(t.titel || t.title).includes("gutglaubiger zweiterwerb"))
  || THEMEN.find((t) => norm(JSON.stringify(t)).includes("gutglaubig") && norm(JSON.stringify(t)).includes("zweiterwerb"))
  || THEMEN.find((t) => norm(t.titel || t.title).includes("zweiterwerb"));

if (!topic) {
  const candidates = THEMEN.filter((t) => {
    const hay = norm(JSON.stringify(t));
    return hay.includes("gutglaub") || hay.includes("zweiterwerb") || hay.includes("hypothek") || hay.includes("vormerkung");
  }).slice(0, 50).map((t) => ({
    id: t.id || t.themaId || null,
    titel: t.titel || t.title || null,
    normen: t.normen || null,
    fach: t.fach || null,
    fachLabel: t.fachLabel || null
  }));
  console.log("DIAG_MATCHING_TOPICS=" + JSON.stringify(candidates));
  throw new Error("Thema 'gutgläubiger Zweiterwerb' nicht im entschlüsselten Themenpool gefunden.");
}

const title = String(topic.titel || topic.title || "Gutgläubiger Zweiterwerb");
const titleHay = norm(title);
const normen = Array.isArray(topic.normen) ? topic.normen : [];
const normenText = normen.length ? normen.join(", ") : "die einschlägigen Gutglaubensvorschriften des BGB";

let folienKern;
if (titleHay.includes("hypothek")) {
  folienKern = {
    grundidee: "Beim Zweiterwerb wird eine bereits bestehende Hypothek von einem bisherigen Berechtigten auf einen Erwerber übertragen. In der Klausur trennst du Übertragungstatbestand und guten Glauben an die Rechtslage.",
    schritte: [
      { titel: "Übertragung", text: "Ausgangspunkt ist die Übertragung der gesicherten Forderung; die Hypothek folgt grundsätzlich der Forderung. Form und Übergabevoraussetzungen sind gesondert zu prüfen." },
      { titel: "Berechtigung", text: "Dann fragst du, ob der Veräußerer tatsächlich Inhaber der übergehenden Rechtsposition war." },
      { titel: "Gutglaubensschutz", text: "Fehlt die Berechtigung, kommt ein gutgläubiger Erwerb nur in Betracht, soweit das Gesetz den öffentlichen Glauben des Grundbuchs bzw. die einschlägigen Gutglaubensregeln eröffnet." }
    ],
    falle: [
      "Nicht Ersterwerb und Zweiterwerb vermischen: Beim Zweiterwerb existiert die Rechtsposition bereits und wird weiterübertragen.",
      "Der gute Glaube ersetzt nicht jede fehlende Voraussetzung. Ein nicht übertragbares oder überhaupt nicht bestehendes Recht kann nur insoweit fingiert werden, wie das Gesetz das ausdrücklich zulässt.",
      "Grundbuchlage, Kenntnis und ein möglicher Widerspruch sind sauber getrennt zu prüfen."
    ],
    merke: "Beim gutgläubigen Zweiterwerb erst den normalen Übertragungstatbestand prüfen – und erst danach fragen, welche fehlende Berechtigung der gesetzliche Gutglaubensschutz überwinden kann."
  };
} else if (titleHay.includes("vormerkung")) {
  folienKern = {
    grundidee: "Beim gutgläubigen Zweiterwerb einer Vormerkung wird eine bereits bestehende Sicherungsposition zusammen mit dem gesicherten Anspruch weitergegeben. Entscheidend ist, ob der Erwerber auf den fortbestehenden Rechtsschein vertrauen darf.",
    schritte: [
      { titel: "Gesicherten Anspruch übertragen", text: "Zuerst muss der durch die Vormerkung gesicherte Anspruch wirksam auf den Erwerber übergehen." },
      { titel: "Vormerkung folgt", text: "Die Vormerkung ist akzessorisch zum gesicherten Anspruch und geht mit ihm auf den Erwerber über." },
      { titel: "Guten Glauben prüfen", text: "Ist die Vormerkung beim Veräußerer fehlerhaft, wird geprüft, ob der Erwerber aufgrund der maßgeblichen Rechtsschein- und Gutglaubensregeln geschützt ist." }
    ],
    falle: [
      "Nicht pauschal §§ 892 ff. BGB anwenden, ohne die besondere Akzessorietät der Vormerkung zu berücksichtigen.",
      "Der gesicherte Anspruch und die Vormerkung müssen getrennt gedacht werden.",
      "Eintragung, Berechtigung und guter Glaube gehören in unterschiedliche Prüfungsschritte."
    ],
    merke: "Beim Zweiterwerb der Vormerkung folgt die Sicherung dem Anspruch – der Gutglaubensschutz wird erst relevant, wenn die Rechtsposition des Veräußerers fehlerhaft ist."
  };
} else if (titleHay.includes("grundschuld")) {
  folienKern = {
    grundidee: "Beim gutgläubigen Zweiterwerb einer Grundschuld wird eine bereits bestehende Grundschuld rechtsgeschäftlich weiterübertragen. Der Erwerber kann unter den gesetzlichen Voraussetzungen auf die Grundbuchlage vertrauen.",
    schritte: [
      { titel: "Übertragungstatbestand", text: "Zunächst ist die Abtretung der Grundschuld mit den erforderlichen Form- und Registervoraussetzungen zu prüfen." },
      { titel: "Berechtigung", text: "Danach ist zu klären, ob der Veräußerer tatsächlich Grundschuldgläubiger war." },
      { titel: "Gutgläubiger Erwerb", text: "Fehlt die Berechtigung, können die Gutglaubensregeln des Grundstücksrechts den Erwerb schützen, sofern kein Ausschlussgrund wie positive Kenntnis oder Widerspruch vorliegt." }
    ],
    falle: [
      "Die Grundschuld ist nicht akzessorisch wie die Hypothek; deshalb nicht automatisch mit einer Forderung verknüpfen.",
      "Buch- und Briefgrundschuld haben unterschiedliche Übertragungsvoraussetzungen.",
      "Der gute Glaube bezieht sich auf die grundbuchfähige Rechtslage, nicht auf jede schuldrechtliche Nebenabrede."
    ],
    merke: "Beim Zweiterwerb der Grundschuld zuerst die Übertragung vollständig prüfen; der öffentliche Glaube des Grundbuchs heilt nur die vom Gesetz erfassten Berechtigungsmängel."
  };
} else {
  folienKern = {
    grundidee: "Gutgläubiger Zweiterwerb bedeutet: Eine bereits bestehende dingliche Rechtsposition wird weiterübertragen, obwohl beim Veräußerer ein Berechtigungsproblem besteht. Die Klausur fragt, ob der Erwerber auf einen gesetzlich geschützten Rechtsschein vertrauen darf.",
    schritte: [
      { titel: "Recht identifizieren", text: "Zuerst bestimmst du genau, welche dingliche Rechtsposition weiterübertragen wird und welche normalen Übertragungsvoraussetzungen gelten." },
      { titel: "Berechtigung prüfen", text: "Dann klärst du, ob der Veräußerer Inhaber der Rechtsposition und verfügungsbefugt war." },
      { titel: "Gutglaubensschutz", text: "Erst wenn die Berechtigung fehlt, prüfst du die einschlägigen gesetzlichen Rechtsschein- und Gutglaubensvorschriften samt Ausschlussgründen." }
    ],
    falle: [
      "Zweiterwerb setzt eine bereits bestehende Rechtsposition voraus; deshalb nicht mit einem erstmaligen Erwerb vermischen.",
      "Guter Glaube ersetzt nur die vom Gesetz erfasste fehlende Berechtigung, nicht beliebige Tatbestandsvoraussetzungen.",
      "Kenntnis, grobe Fahrlässigkeit und Registerwidersprüche sind nur dort relevant, wo die jeweilige Gutglaubensnorm sie vorsieht."
    ],
    merke: "Schema: normaler Zweiterwerb → fehlende Berechtigung feststellen → passende Gutglaubensnorm → Ausschluss des guten Glaubens → Ergebnis."
  };
}

const motifBytes = fs.readFileSync(motif);
const motifData = `data:image/png;base64,${motifBytes.toString("base64")}`;
const fach = topic.fach || "sachen";
const fachLabel = topic.fachLabel || "Sachenrecht";
const themaId = topic.id || topic.themaId || "dryrun-gutglaeubiger-zweiterwerb";

const inhalt = {
  format: "lernkarte",
  fach,
  klausur: 1,
  fachLabel,
  themaId,
  folien: [
    {
      art: "titel",
      titel: "Gutgläubiger Zweiterwerb: Wie prüfen?",
      titelZeilen: ["Gutgläubiger", "Zweiterwerb:", "Wie prüfen?"],
      icon: "schluessel",
      prioritaet: "hoch",
      prioritaetText: "Sachenrechtsklassiker",
      coverBadge: "Sachenrechtsklassiker",
      coverText: "Rechtsschein zuerst sauber zuordnen",
      bild: motifData,
      bildQuelle: null,
      bildFrei: true,
      bildTyp: "charakter",
      bildBreite: 1024,
      bildHoehe: 960,
      coverHinweisPlan: {
        noteX: 0.70, noteY: 0.42,
        targetX: 0.68, targetY: 0.56,
        rotationDeg: -5, bend: 0
      }
    },
    {
      art: "text",
      titel: title,
      text: folienKern.grundidee
    },
    {
      art: "schritte",
      titel: "Prüfung in 3 Schritten",
      schritte: folienKern.schritte
    },
    {
      art: "text",
      titel: "Normenanker",
      punkte: [
        `Themenpool-Normen: ${normenText}.`,
        "Die konkrete Gutglaubensnorm bestimmt, welcher Rechtsschein geschützt wird und welche subjektiven Voraussetzungen gelten.",
        "Deshalb niemals nur „gutgläubig“ hinschreiben: Rechtsscheinträger, fehlende Berechtigung und Ausschlussgründe müssen benannt werden."
      ]
    },
    {
      art: "text",
      titel: "Typische Fehler",
      punkte: folienKern.falle
    },
    {
      art: "merke",
      titel: "Klausur-Merksatz",
      text: folienKern.merke
    },
    {
      art: "cta",
      titel: "Für Sachenrecht speichern",
      text: "Erst normaler Übertragungstatbestand, dann Berechtigung, dann die passende Gutglaubensnorm. Genau diese Reihenfolge verhindert die häufigsten Aufbaufehler."
    }
  ],
  caption: `${title}: Beim gutgläubigen Zweiterwerb zuerst den normalen Übertragungstatbestand prüfen, dann das Berechtigungsproblem isolieren und erst anschließend den gesetzlichen Gutglaubensschutz anwenden.`,
  hashtags: ["#jura","#jurastudium","#staatsexamen","#sachenrecht","#bgb","#gutglaeubigererwerb","#examenswissen"],
  kurztitel: "Gutgläubiger Zweiterwerb",
  coverText: "Rechtsschein zuerst sauber zuordnen",
  coverBadge: "Sachenrechtsklassiker",
  quellen: normen.length ? normen : [],
  hookTyp: "frage",
  slug: "dryrun-gutglaeubiger-zweiterwerb",
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
  productionBaseCommit: process.env.DRYRUN_BASE_COMMIT || null,
  dryRunCommit: process.env.GITHUB_SHA || null,
  topicSource: "encrypted-themenpool",
  topic,
  motif: "single-strafrecht-fahrlaessige-toetung.png",
  motifSourceArtifactId: 10708830448,
  motifSourceRunId: 35755786908,
  motifSha256: crypto.createHash("sha256").update(motifBytes).digest("hex"),
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
  `Theme from encrypted pool: ${title}`,
  `Theme fach: ${fachLabel}`,
  "Motif: exact existing single-strafrecht-fahrlaessige-toetung.png from prior zero-cost artifact",
  "Renderer: current production main contract",
  "Provider/API cost: $0.00",
  "No publishing performed."
].join("\n"));

await browserBeenden();
console.log(JSON.stringify({
  topic: { id: themaId, title, normen, fach, fachLabel },
  motif: "single-strafrecht-fahrlaessige-toetung.png",
  providerCostUsd: 0,
  externalProviderCalls: false,
  publishingPerformed: false,
  outputs: files.length,
  cover: path.relative(out, cover)
}, null, 2));
