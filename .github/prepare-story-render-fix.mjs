import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import { createHash } from "node:crypto";
import { storyRenderInhaltSha256, storyBildSha256 } from "../src/story-render-freigabe.mjs";

function patch(file, edits) {
  let text = fs.readFileSync(file, "utf8");
  for (const [from, to] of edits) {
    assert.equal(text.split(from).length - 1, 1, `${file}: expected one exact target ${from}`);
    text = text.replace(from, to);
  }
  fs.writeFileSync(file, text);
}
const kostenImport = 'import { providerKostenPruefen } from "./provider-kostensperre.mjs";\n';
patch("src/pruefung.mjs", [
  ['import { THEMEN } from "../daten/themen.mjs";', 'import { THEMEN } from "../daten/themen.mjs";\nimport { visuelleStoryLaengeFreigegeben } from "./story-render-freigabe.mjs";'],
  ['export function storyFreigabe(story) {', 'export function storyFreigabe(story, opt = {}) {'],
  ['    const lokal = pruefeBeitrag({ stories: [story] });', '    const lokal = pruefeBeitrag({ stories: [story] }, opt);'],
  ['  if (manuellFinalisiert(story)) {\n    const lokal', '  if (manuellFinalisiert(story) && (story.faktencheckOffen || (story.beanstandetFachlich || []).length || ((story.beanstandet || []).length && !story.befundeTypisiert))) {\n    return { frei: false, warten: true, grund: "Offene fachliche/ungeklaerte Befunde bleiben trotz Sichtfreigabe gesperrt" };\n  }\n  if (manuellFinalisiert(story)) {\n    const lokal'],
  ['if (l > GRENZEN.storyTextZeichen) fehler.push(', 'if (l > GRENZEN.storyTextZeichen && !visuelleStoryLaengeFreigegeben(s, opt.vorproduktion)) fehler.push('],
]);
patch("src/lauf.mjs", [
  ['import { CONFIG } from "./config.mjs";', 'import { CONFIG } from "./config.mjs";\nimport { providerKostenSperren } from "./provider-kostensperre.mjs";'],
  ['async function main() {\n', 'async function main() {\n  providerKostenSperren();\n  log("Providerkosten dauerhaft fuer diesen Lauf gesperrt: keine kostenpflichtigen KI-, Bild- oder Voice-Aufrufe.");\n'],
  ['const freigabe = storyFreigabe(story);', 'const freigabe = storyFreigabe(story, { vorproduktion });'],
  ['    if (ungeprueft.length) {', '    if (ungeprueft.length && !vorproduktionAktiv) {'],
  ['    if (vorhanden) return vorhanden;\n    /* Die Obergrenze', '    if (vorhanden) return vorhanden;\n    if (vorproduktionAktiv) throw new Error(`Vorproduktion ${datum} ${eintrag.slot}: Inhalt fehlt; kein KI-Fallback.`);\n    /* Die Obergrenze'],
]);
patch("src/anbieter.mjs", [
  ['import Anthropic from "@anthropic-ai/sdk";', 'import Anthropic from "@anthropic-ai/sdk";\n' + kostenImport.trimEnd()],
  ['async function durchDieTuer({ zweck, provider, modell, params, attempt, slot, optional, pflichtName, effort, denkmodus, promptVersion, senden, preis, admissionInputTokens = null }) {', 'async function durchDieTuer({ zweck, provider, modell, params, attempt, slot, optional, pflichtName, effort, denkmodus, promptVersion, senden, preis, admissionInputTokens = null }) {\n  providerKostenPruefen(zweck);'],
  ['export async function openaiBildEditSenden({ form, key, zeitlimitMs = 120000, fetchFn = fetch }) {', 'export async function openaiBildEditSenden({ form, key, zeitlimitMs = 120000, fetchFn = fetch }) {\n  providerKostenPruefen("Bildbearbeitung");'],
  ['export async function bildAufruf({ zweck = "bild", auftrag = null, senden = null, preisUsd = null, slot = null, optional = true, modell = "gpt-image-1-mini", zeitlimitMs = 120000, url = "https://api.openai.com/v1/images/generations", fetchFn = fetch, kostenAusAntwort = null }) {', 'export async function bildAufruf({ zweck = "bild", auftrag = null, senden = null, preisUsd = null, slot = null, optional = true, modell = "gpt-image-1-mini", zeitlimitMs = 120000, url = "https://api.openai.com/v1/images/generations", fetchFn = fetch, kostenAusAntwort = null }) {\n  providerKostenPruefen(zweck);'],
]);
patch("src/stimme.mjs", [
  ['import { CONFIG } from "./config.mjs";', 'import { CONFIG } from "./config.mjs";\nimport { providerKostenPruefen, providerKostenSindGesperrt } from "./provider-kostensperre.mjs";'],
  ['export async function kontingentAbfragen({ frisch = false } = {}) {', 'export async function kontingentAbfragen({ frisch = false } = {}) {\n  if (providerKostenSindGesperrt()) return null;'],
  ['export function stimmenAnbieter() {', 'export function stimmenAnbieter() {\n  if (providerKostenSindGesperrt()) return offlineAnbieter();'],
  ['export async function anbieterFuerText(zeichen = 0) {', 'export async function anbieterFuerText(zeichen = 0) {\n  if (providerKostenSindGesperrt()) return offlineAnbieter();'],
  ['async function elevenlabs(text, zielDatei, art = "normal", stimmeId = null) {', 'async function elevenlabs(text, zielDatei, art = "normal", stimmeId = null) {\n  providerKostenPruefen("ElevenLabs-Spracherzeugung");'],
]);
patch("src/stimmen.mjs", [
  ['import { CONFIG } from "./config.mjs";', 'import { CONFIG } from "./config.mjs";\n' + kostenImport.trimEnd()],
  ['async function api(pfad, opt = {}) {', 'async function api(pfad, opt = {}) {\n  providerKostenPruefen("ElevenLabs-Stimmenbibliothek");'],
]);
patch(".github/workflows/instagram.yml", [
  ['permissions:\n  contents: write', 'env:\n  # Kostenverbot gilt auch fuer manuelle Hilfsmodi; keine Repository-Variable.\n  IG_PROVIDERKOSTEN_GESPERRT: "true"\n\npermissions:\n  contents: write'],
  ['          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}\n', ''],
  ['          ELEVENLABS_API_KEY: ${{ secrets.ELEVENLABS_API_KEY }}\n', ''],
  ['          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}\n', ''],
]);

// Ausschliesslich GET bei GitHub, keine Provider-Secrets, keine Assets schreiben.
const datum = "2026-09-27";
const snapshot = "29c06652c2489a3d7ede50e175b072301578d3c1";
const raw = `https://raw.githubusercontent.com/Ccan-devoloper/herrjurist/${snapshot}/`;
const live = "https://raw.githubusercontent.com/Ccan-devoloper/herrjurist/instagram-assets/";
const gitSha = (b) => createHash("sha1").update(`blob ${b.length}\0`).update(b).digest("hex");
async function bytes(url) {
  const r = await fetch(url, { signal: AbortSignal.timeout(30000) });
  assert.ok(r.ok, `GET ${url}: ${r.status}`);
  return Buffer.from(await r.arrayBuffer());
}
const rawDay = await bytes(raw + `vorproduktion/${datum}.json`);
assert.equal(gitSha(rawDay), "fe22c51309630b8537897d7e57218abe38c58430", "approved text snapshot changed");
assert.equal(gitSha(await bytes(live + `vorproduktion/${datum}.json?v=${Date.now()}`)), gitSha(rawDay), "live text changed: review again instead of auto-approving");
const tag = JSON.parse(rawDay);
const assetDir = path.resolve(".tmp/story-gate-assets");
const localDay = path.join(assetDir, `vorproduktion/${datum}.json`);
fs.mkdirSync(path.dirname(localDay), { recursive: true });
fs.writeFileSync(localDay, rawDay);
const media = [];
for (const p of tag.plan.beitraege) {
  const root = `vorproduktion/${datum}/fertig/${p.slot}/${datum}-${p.slot}`;
  if (p.format === "reel") media.push(root + ".mp4", root + "-cover.jpg");
  else tag.inhalte[p.slot].folien.forEach((_, i) => media.push(root + "-" + String(i + 1).padStart(2, "0") + ".jpg"));
}
for (const p of tag.plan.stories) media.push(`vorproduktion/${datum}/fertig/stories/${p.slot}-${p.art}.jpg`);
assert.equal(media.length, 25);
for (let i = 0; i < media.length; i += 5) {
  await Promise.all(media.slice(i, i + 5).map(async (rel) => {
    const b = await bytes(raw + rel);
    assert.ok(b.length > 1000, rel + " unexpectedly empty");
    if (rel.endsWith(".jpg")) assert.ok(b[0] === 0xff && b[1] === 0xd8, rel + " is not JPEG");
    else assert.equal(b.toString("ascii", 4, 8), "ftyp", rel + " is not MP4");
    fs.mkdirSync(path.dirname(path.join(assetDir, rel)), { recursive: true });
    fs.writeFileSync(path.join(assetDir, rel), b);
  }));
}
const expectedBlobs = { s7: "14f61961f2120553c212b85a2380fec8f9bdfa2b", s8: "326db352b519ce0fed113a31d23dc6c9f6487a0f" };
const freigaben = [];
for (const slot of ["s7", "s8"]) {
  const story = tag.inhalte[slot];
  const pfad = `vorproduktion/${datum}/fertig/stories/${slot}-${story.art}.jpg`;
  const bild = fs.readFileSync(path.join(assetDir, pfad));
  assert.equal(gitSha(bild), expectedBlobs[slot]);
  assert.equal(gitSha(await bytes(live + pfad + `?v=${Date.now()}`)), expectedBlobs[slot], "live image changed: new visual review required");
  freigaben.push({ datum, slot, art: story.art, pfad, visuellGeprueft: true, freigegebenVon: "Betreiber: Screenshot-Sichtpruefung und Anpassungsauftrag im Chat", freigegebenAm: new Date().toISOString(), grund: "Text passt im bestaetigten fertigen Story-Bild; nur pauschale 260-Zeichen-Grenze ersetzen", inhaltSha256: storyRenderInhaltSha256(story), bildSha256: storyBildSha256(bild), bildGitBlob: expectedBlobs[slot], quellCommit: snapshot });
}
fs.writeFileSync("config/story-render-freigaben.json", JSON.stringify({ version: 1, repository: "Ccan-devoloper/herrjurist", freigaben }, null, 2) + "\n");
console.log("READ_ONLY_MEDIA_OK", JSON.stringify({ datum, files: media.length, lengths: Object.fromEntries(["s7", "s8"].map((s) => [s, tag.inhalte[s].text.length])), unchanged: true }));
