import test from "node:test";
import assert from "node:assert/strict";

import { zeitpunktVon } from "../src/zeit.mjs";
import { feedWartezeitMs } from "../src/vorproduktion-live.mjs";
import { planFuerWecker, naechsterTermin } from "../src/vorproduktion-zeitplan.mjs";

const DATUM = "2026-10-04";
const uhr = (h, m) => h * 3600 + m * 60;

/* Stand vom 04.10.2026: s4/s5 (07:21) werden in jedem Lauf übersprungen,
   b2 stand im Dashboard auf 09:30, b3 auf 16:30, s8 auf 16:53. */
function tagesplan() {
  return {
    beitraege: [
      { slot: "b1", zeit: "07:00", status: "veroeffentlicht" },
      { slot: "b2", zeit: "09:30", status: "geplant" },
      { slot: "b3", zeit: "16:30", format: "reel", status: "geplant" },
    ],
    stories: [
      { slot: "s4", zeit: "07:21", art: "frage", status: "geplant" },
      { slot: "s5", zeit: "07:21", art: "antwort", status: "geplant" },
      { slot: "s2", zeit: "09:30", art: "teaser", beitragSlot: "b2", status: "geplant" },
      { slot: "s3", zeit: "16:30", art: "teaser", beitragSlot: "b3", status: "geplant" },
      { slot: "s8", zeit: "16:53", art: "tipp", status: "geplant" },
    ],
  };
}

test("zeitpunktVon rechnet Berliner Uhrzeit in Sommer- und Winterzeit um", () => {
  assert.equal(new Date(zeitpunktVon("2026-10-04", "16:30")).toISOString(), "2026-10-04T14:30:00.000Z");
  assert.equal(new Date(zeitpunktVon("2026-12-01", "16:30")).toISOString(), "2026-12-01T15:30:00.000Z");
});

test("Übersprungene frühe Story schaltet das exakte Warten nicht mehr ab", () => {
  /* Lauf um 16:24 (Weckkette 8 Minuten vorher geweckt, Vorarbeit fertig):
     bis 16:27 warten, dann Upload/Container, media_publish um 16:30. */
  assert.equal(feedWartezeitMs(tagesplan(), uhr(16, 24), 100, 180), 3 * 60 * 1000);
  /* Ohne Vorbereitungsspanne bis zur Planminute selbst. */
  assert.equal(feedWartezeitMs(tagesplan(), uhr(16, 24)), 6 * 60 * 1000);
});

test("Mit einem vergangenen offenen Slot wird höchstens 15 Minuten gewartet", () => {
  /* Der Stundenlauf um 09:00 wartet nicht 30 Minuten auf b2 – den Start kurz
     vorher übernimmt die Weckkette, der vergangene Slot kommt sofort dran. */
  assert.equal(feedWartezeitMs(tagesplan(), uhr(9, 0), 100, 180), 0);
  assert.equal(feedWartezeitMs(tagesplan(), uhr(9, 20), 100, 180), 7 * 60 * 1000);
});

test("Gespeicherte Status zählen für die Weckkette, Uhrzeiten kommen aus dem Dashboard", () => {
  const dashboard = { plan: tagesplan() };
  const gespeichert = {
    beitraege: [{ slot: "b1", status: "veroeffentlicht" }, { slot: "b2", zeit: "14:30", status: "veroeffentlicht" }],
    stories: [{ slot: "s4", status: "uebersprungen" }, { slot: "s5", status: "uebersprungen" }, { slot: "s2", status: "veroeffentlicht" }],
  };
  const plan = planFuerWecker(dashboard, gespeichert);
  assert.equal(plan.stories.find((e) => e.slot === "s4").status, "uebersprungen");
  assert.equal(plan.beitraege.find((e) => e.slot === "b3").zeit, "16:30");

  const um1600 = Date.parse("2026-10-04T14:00:00Z");
  assert.equal(new Date(naechsterTermin(plan, DATUM, um1600)).toISOString(), "2026-10-04T14:30:00.000Z");

  /* Nach b3/s3: s8 um 16:53 ist der nächste Termin. */
  plan.beitraege.find((e) => e.slot === "b3").status = "veroeffentlicht";
  plan.stories.find((e) => e.slot === "s3").status = "veroeffentlicht";
  const um1632 = Date.parse("2026-10-04T14:32:00Z");
  assert.equal(new Date(naechsterTermin(plan, DATUM, um1632)).toISOString(), "2026-10-04T14:53:00.000Z");
});

test("Während des Laufs fällig gewordener Termin weckt sofort, frisch gescheiterter nicht", () => {
  const plan = planFuerWecker({ plan: tagesplan() }, null);
  const laufstart = Date.parse("2026-10-04T14:20:00Z");
  const jetzt = Date.parse("2026-10-04T14:31:00Z");
  assert.equal(new Date(naechsterTermin(plan, DATUM, jetzt, laufstart)).toISOString(), "2026-10-04T14:30:00.000Z");
  assert.equal(new Date(naechsterTermin(plan, DATUM, jetzt)).toISOString(), "2026-10-04T14:53:00.000Z");

  plan.beitraege.find((e) => e.slot === "b3").fehler = "2026-10-04T14:30:40.000Z Container ERROR";
  assert.equal(new Date(naechsterTermin(plan, DATUM, jetzt, laufstart)).toISOString(), "2026-10-04T14:53:00.000Z");
});
