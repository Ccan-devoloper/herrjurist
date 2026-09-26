import assert from "node:assert/strict";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { test } from "node:test";
import { pruefeStoryRenderFreigabe, storyRenderInhaltSha256, storyBildSha256 } from "../src/story-render-freigabe.mjs";
import { storyFreigabe, quizPaarFreigabe, pruefeBeitrag } from "../src/pruefung.mjs";
import { vorproduktionLaden, planAusVorproduktion, inhalteUebernehmen, feedAssets } from "../src/vorproduktion-live.mjs";
import { providerKostenSperren, providerKostenPruefen, providerKostenSindGesperrt, ProviderKostenGesperrt } from "../src/provider-kostensperre.mjs";
import { istKostenKontrollFehler } from "../src/kostenfehler.mjs";
import { claudeAufruf, openaiAufruf, bildAufruf, openaiBildEditSenden, klientSetzen, kontextSetzen, kontextLoeschen } from "../src/anbieter.mjs";
import { sprechen, anbieterFuerText, stimmenAnbieter, kontingentAbfragen } from "../src/stimme.mjs";
import { tarif } from "../src/stimmen.mjs";

function fixture(t) {
  const assetDir = fs.mkdtempSync(path.join(os.tmpdir(), "story-approval-"));
  t.after(() => fs.rmSync(assetDir, { recursive: true, force: true }));
  const datum = "2026-09-27";
  const story = { slot: "s7", art: "fehler", titel: "Ein gepruefter Titel", text: "Ein langer, gepruefter Text. ".repeat(12), manuellGeprueft: true, befundeTypisiert: true };
  const pfad = `vorproduktion/${datum}/fertig/stories/s7-fehler.jpg`;
  const datei = path.join(assetDir, pfad);
  const bytes = Buffer.from([0xff, 0xd8, 11, 12, 13, 0xff, 0xd9]);
  fs.mkdirSync(path.dirname(datei), { recursive: true });
  fs.writeFileSync(datei, bytes);
  const vp = { assetDir, fertigRel: `vorproduktion/${datum}/fertig`, tag: { datum, plan: { stories: [{ slot: story.slot, art: story.art }] }, inhalte: { s7: structuredClone(story) } } };
  const freigaben = [{ datum, slot: story.slot, art: story.art, pfad, visuellGeprueft: true, freigegebenVon: "offline-test", freigegebenAm: "2026-09-26T12:00:00Z", inhaltSha256: storyRenderInhaltSha256(story), bildSha256: storyBildSha256(bytes) }];
  return { story, vp, freigaben, datei };
}

test("visual approval matches exact story, date, slot and JPEG", (t) => {
  const { story, vp, freigaben } = fixture(t);
  assert.ok(story.text.length > 260);
  assert.equal(pruefeStoryRenderFreigabe(story, vp, freigaben), true);
  const live = { ...story, freigabeBetreiber: true, liveVerknuepft: true, vorproduktionStatus: "live-vorrang", vorproduktionQuelle: "vorproduktion/2026-09-27.json" };
  assert.equal(pruefeStoryRenderFreigabe(live, vp, freigaben), true);
  assert.equal(storyRenderInhaltSha256(live), storyRenderInhaltSha256(story));
});

test("text, title, source and image changes invalidate visual approval", (t) => {
  const { story, vp, freigaben, datei } = fixture(t);
  for (const patch of [{ text: story.text + "!" }, { titel: "Anderer Titel" }, { optionen: ["neu"] }, { manuellGeprueft: false }, { slot: "s8" }, { art: "tipp" }]) {
    assert.equal(pruefeStoryRenderFreigabe({ ...story, ...patch }, vp, freigaben), false);
  }
  const changed = structuredClone(vp);
  changed.tag.inhalte.s7.text += "!";
  assert.equal(pruefeStoryRenderFreigabe(story, changed, freigaben), false);
  fs.appendFileSync(datei, "changed");
  assert.equal(pruefeStoryRenderFreigabe(story, vp, freigaben), false);
});

test("missing evidence, other dates, pending facts and legacy findings fail closed", (t) => {
  const { story, vp, freigaben, datei } = fixture(t);
  for (const patch of [{ visuellGeprueft: false }, { inhaltSha256: "" }, { bildSha256: "" }, { datum: "2026-09-28" }, { freigegebenAm: "invalid" }, { pfad: "../outside.jpg" }]) {
    assert.equal(pruefeStoryRenderFreigabe(story, vp, [{ ...freigaben[0], ...patch }]), false);
  }
  for (const patch of [{ faktencheckOffen: true }, { beanstandetFachlich: ["offen"] }, { beanstandet: ["unklar"], befundeTypisiert: false }]) {
    const s = { ...story, ...patch };
    const evidence = [{ ...freigaben[0], inhaltSha256: storyRenderInhaltSha256(s) }];
    assert.equal(pruefeStoryRenderFreigabe(s, { ...vp, tag: { ...vp.tag, inhalte: { s7: s } } }, evidence), false);
    assert.equal(storyFreigabe(s, { vorproduktion: vp }).frei, false);
  }
  fs.unlinkSync(datei);
  assert.equal(pruefeStoryRenderFreigabe(story, vp, freigaben), false);
});

test("a plain visual flag cannot bypass the ordinary length or content checks", (t) => {
  const { story, vp } = fixture(t);
  assert.equal(storyFreigabe({ ...story, visuellGeprueft: true }, { vorproduktion: vp }).frei, false);
  assert.equal(pruefeBeitrag({ stories: [story] }).ok, false);
  assert.equal(storyFreigabe({ ...story, art: "zahl", text: "Kurz.", zahl: "immer" }).frei, false);
});

test("production wiring preserves the image upload and has no paid fallback", () => {
  const lauf = fs.readFileSync(new URL("../src/lauf.mjs", import.meta.url), "utf8");
  assert.match(lauf, /storyFreigabe\(story, \{ vorproduktion \}\)/);
  assert.match(lauf, /async function main\(\) \{\s+providerKostenSperren\(\)/);
  assert.match(lauf, /if \(ungeprueft.length && !vorproduktionAktiv\)/);
  assert.match(lauf, /if \(vorproduktionAktiv\) throw new Error\(`Vorproduktion.*kein KI-Fallback/);
  const workflow = fs.readFileSync(new URL("../.github/workflows/instagram.yml", import.meta.url), "utf8");
  assert.match(workflow, /IG_PROVIDERKOSTEN_GESPERRT: "true"/);
  assert.doesNotMatch(workflow, /secrets\.(ANTHROPIC_API_KEY|OPENAI_API_KEY|ELEVENLABS_API_KEY)/);
  assert.match(workflow, /cron: "0 5-20 \* \* \*"/);
});

test("actual 27 September assets: all nine stories and quiz pass offline", { skip: !process.env.IG_PREFLIGHT_ASSET_DIR }, () => {
  const vp = vorproduktionLaden({ dir: process.env.IG_PREFLIGHT_ASSET_DIR, basisUrl: "https://example.invalid" }, "2026-09-27");
  const plan = planAusVorproduktion(vp);
  const inhalte = new Map();
  inhalteUebernehmen({ jsonSchreiben: (p, v) => inhalte.set(p, v) }, vp, plan);
  const lesen = (slot) => inhalte.get(`inhalte/2026-09-27-${slot}.json`);
  assert.equal(plan.beitraege.length, 3);
  assert.equal(plan.stories.length, 9);
  for (const p of plan.beitraege) {
    const a = feedAssets(vp, p);
    assert.ok(p.format === "reel" ? a.videoPfad && a.coverPfad : a.bildPfade.length === 7);
  }
  const before = JSON.stringify(vp.tag);
  const antwort = plan.stories.find((p) => p.art === "antwort");
  assert.equal(quizPaarFreigabe(antwort, plan.stories, lesen).status, "warten", "answer must wait for question publication");
  for (const p of plan.stories) {
    const s = lesen(p.slot);
    const result = storyFreigabe(s, { vorproduktion: vp });
    assert.equal(result.frei, true, p.slot + ": " + result.grund);
    if (["frage", "antwort"].includes(p.art)) {
      const paar = quizPaarFreigabe(p, plan.stories, lesen);
      assert.equal(paar.status, "frei", p.slot + ": " + paar.grund);
      // Simulate successful question publication locally; never call Instagram.
      if (p.art === "frage") p.status = "veroeffentlicht";
    }
    if (["s7", "s8"].includes(p.slot)) assert.equal(storyFreigabe(s).frei, false, "without verified asset context the length gate remains active");
  }
  assert.equal(JSON.stringify(vp.tag), before, "no text, image metadata, schedule or publication status mutations");
});

test("cost lock prevents text, review, image, voice and fallback requests before network or booking", async (t) => {
  const original = globalThis.fetch;
  const temp = fs.mkdtempSync(path.join(os.tmpdir(), "provider-lock-"));
  t.after(() => { globalThis.fetch = original; klientSetzen(null); kontextLoeschen(); fs.rmSync(temp, { recursive: true, force: true }); });
  let sends = 0, counts = 0, bookings = 0;
  const send = async () => { sends++; throw new Error("NETWORK MUST NOT BE REACHED"); };
  globalThis.fetch = send;
  klientSetzen({ messages: { create: send, countTokens: async () => { counts++; return { input_tokens: 1 }; } } });
  kontextSetzen({ budget: { zulassen: () => { bookings++; throw new Error("booking reached"); } }, journal: { reservieren: send }, providerKostenGesperrt: false });
  providerKostenSperren();
  process.env.IG_PROVIDERKOSTEN_GESPERRT = "false";
  process.env.IG_BREAK_GLASS = "true";
  assert.equal(providerKostenSindGesperrt(), true, "environment and break glass cannot unlock the running bot");
  assert.throws(() => providerKostenPruefen("test"), ProviderKostenGesperrt);
  for (const request of [
    () => claudeAufruf({ zweck: "beitrag", params: { model: "test", max_tokens: 1, messages: [] } }),
    () => openaiAufruf({ zweck: "faktencheck", params: {}, modell: "test", fetchFn: send }),
    () => bildAufruf({ senden: send, preisUsd: 0 }),
    () => bildAufruf({ fetchFn: send, preisUsd: 0 }),
    () => openaiBildEditSenden({ form: new globalThis.FormData(), fetchFn: send }),
  ]) {
    await assert.rejects(request, (e) => e instanceof ProviderKostenGesperrt && istKostenKontrollFehler(e));
  }
  assert.notEqual(await anbieterFuerText(100), "elevenlabs");
  assert.notEqual(stimmenAnbieter(), "elevenlabs");
  assert.equal(await kontingentAbfragen(), null);
  await tarif();
  await sprechen("Offline-Test", path.join(temp, "test.mp3"), { anbieter: "elevenlabs" });
  assert.equal(sends, 0);
  assert.equal(counts, 0);
  assert.equal(bookings, 0);
});
