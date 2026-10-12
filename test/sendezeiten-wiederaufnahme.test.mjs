import test from "node:test";
import assert from "node:assert/strict";
import { sendezeitenAnwenden } from "../src/sendezeiten.mjs";
import { planFuerWecker } from "../src/vorproduktion-zeitplan.mjs";
import { planAusVorproduktion } from "../src/vorproduktion-live.mjs";

test("Bestaetigte fruehe Publikation behaelt ihre Planzeit nach erneutem Laden", () => {
  const raw = {
    datum: "2026-10-13",
    beitraege: [
      { slot: "b1", zeit: "08:00", status: "geplant" },
      { slot: "b2", zeit: "12:30", status: "geplant" },
      { slot: "b3", zeit: "17:30", status: "geplant" },
    ],
    stories: [{ slot: "s1", zeit: "08:00", art: "teaser", beitragSlot: "b1", status: "geplant" }],
  };
  const tag = { datum: raw.datum, plan: raw };
  const gespeichert = sendezeitenAnwenden(raw);
  Object.assign(gespeichert.beitraege[0], { status: "veroeffentlicht", medienId: "123456" });
  Object.assign(gespeichert.stories[0], { status: "veroeffentlicht", medienId: "654321" });
  const vp = { tag, rel: "vorproduktion/2026-10-13.json", fertigRel: "vorproduktion/2026-10-13/fertig" };
  const live = planAusVorproduktion(vp, gespeichert);
  const wecker = planFuerWecker(tag, gespeichert);
  for (const plan of [live, wecker]) {
    assert.equal(plan.beitraege[0].zeit, "06:30");
    assert.equal(plan.stories[0].zeit, "06:30");
    assert.equal(plan.beitraege[0].status, "veroeffentlicht");
  }
  assert.equal(live.beitraege[0].medienId, "123456");
  assert.equal(live.stories[0].medienId, "654321");
  assert.equal(raw.beitraege[0].zeit, "08:00");
});
