import test from "node:test";
import assert from "node:assert/strict";

import { manuellFinalisiert, tagesinhaltManuellFinalisiert } from "../src/finalisierung.mjs";
import { persistierteStoryBeanstandungen, storyFreigabe } from "../src/pruefung.mjs";
import { storiesPruefen, bildregieSicher } from "../src/autor.mjs";

test("manuellGeprueft ist der harte Finalisierungsmarker", () => {
  assert.equal(manuellFinalisiert({ manuellGeprueft: true }), true);
  assert.equal(manuellFinalisiert({ manuellGeprueft: false }), false);
  assert.equal(manuellFinalisiert(null), false);
});

test("manuell finalisierte Stories werden nicht automatisch neu geschrieben", () => {
  const story = {
    slot: "s7",
    art: "tipp",
    titel: "Prüfe zuerst den Tatbestand",
    text: "Arbeite die Voraussetzungen in fester Reihenfolge ab.",
    icon: "paragraf",
    manuellGeprueft: true,
    beanstandetFachlich: ["alter, inzwischen erledigter Befund"],
  };
  const strittig = persistierteStoryBeanstandungen(new Map([["s7", story]]), new Set(["s7"]));
  assert.deepEqual(strittig, []);
});

test("manuelle Freigabe überspringt einen alten API-Faktencheckstatus, aber nicht den lokalen Formcheck", () => {
  const story = {
    slot: "s7",
    art: "tipp",
    titel: "Prüfe zuerst den Tatbestand",
    text: "Arbeite die Voraussetzungen in fester Reihenfolge ab.",
    icon: "paragraf",
    manuellGeprueft: true,
    faktencheckOffen: true,
  };
  const freigabe = storyFreigabe(story);
  assert.equal(freigabe.frei, true);
  assert.equal(freigabe.manuell, true);
});

test("Story-Faktencheck ruft für ausschließlich manuell finalisierte Inhalte kein Modell auf", async () => {
  const story = {
    slot: "s7",
    art: "tipp",
    titel: "Prüfe zuerst den Tatbestand",
    text: "Arbeite die Voraussetzungen in fester Reihenfolge ab.",
    manuellGeprueft: true,
    faktencheckOffen: true,
  };
  const result = await storiesPruefen([story]);
  assert.equal(result[0], story);
  assert.equal(story.faktencheckOffen, true);
});

test("manuell finalisiertes Reel bekommt keine nachträgliche LLM-Bildregie", async () => {
  const reel = { manuellGeprueft: true, bildregie: false, szenen: [] };
  const geaendert = await bildregieSicher(reel);
  assert.equal(geaendert, false);
  assert.equal(reel.bildregie, true);
});

test("manuell finalisiertes Reel ergänzt fehlende Bildaufträge ohne LLM", async () => {
  const reel = {
    manuellGeprueft: true,
    bildregie: true,
    kurztitel: "Prüfschema",
    szenen: [{ titel: "Wichtiger Grund?", text: "Fortsetzung bis zum Vertragsende ist unzumutbar.", bildSzene: null }],
  };
  const geaendert = await bildregieSicher(reel);
  assert.equal(geaendert, true);
  assert.equal(reel.bildregie, true);
  assert.match(reel.szenen[0].bildSzene, /Wichtiger Grund/);
  assert.match(reel.szenen[0].bildSzene, /unzumutbar/);
});


test("vollständig im Chat finalisierte Tage erzeugen keinen bezahlten Vorrat", () => {
  const plan = {
    beitraege: [{ slot: "b1" }, { slot: "b2" }],
    stories: [{ slot: "s1", art: "teaser" }, { slot: "s2", art: "tipp" }],
  };
  const texte = {
    b1: { manuellGeprueft: true },
    b2: { manuellGeprueft: true },
    s2: { manuellGeprueft: true },
  };
  assert.equal(tagesinhaltManuellFinalisiert(plan, (slot) => texte[slot] || null), true);
  assert.equal(tagesinhaltManuellFinalisiert(plan, (slot) => slot === "b2" ? null : texte[slot] || null), false);
});
