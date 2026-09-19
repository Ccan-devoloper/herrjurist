import test from "node:test";
import assert from "node:assert/strict";
import { storyInsights, storyInsightsAktualisieren } from "../src/insights.mjs";

function insightAntwort(metric) {
  const werte = {
    reach: 120,
    views: 180,
    shares: 7,
    total_interactions: 12,
    replies: 2,
    follows: 1,
    profile_visits: 5,
    profile_activity: 6,
    link_clicks: 3,
  };
  return {
    data: String(metric).split(",").map((name) => ({
      name,
      values: [{ value: werte[name] ?? 0 }],
    })),
  };
}

test("Story-Insights speichern Kern-, Wachstums- und Navigationsmetriken", async () => {
  const ig = {
    host: "instagram",
    async anfrage(_methode, _pfad, params) {
      if (params.metric === "navigation") {
        return {
          data: [{
            name: "navigation",
            total_value: {
              breakdowns: [{
                results: [
                  { dimension_values: ["story_taps_forward"], value: 14 },
                  { dimension_values: ["story_taps_back"], value: 4 },
                  { dimension_values: ["story_exits"], value: 3 },
                ],
              }],
            },
          }],
        };
      }
      return insightAntwort(params.metric);
    },
  };

  const r = await storyInsights(ig, "123456789");
  assert.equal(r.reach, 120);
  assert.equal(r.views, 180);
  assert.equal(r.shares, 7);
  assert.equal(r.replies, 2);
  assert.equal(r.follows, 1);
  assert.equal(r.profile_visits, 5);
  assert.equal(r.navigation, 21);
  assert.equal(r.navigation_taps_forward, 14);
  assert.equal(r.navigation_taps_back, 4);
  assert.equal(r.navigation_exits, 3);
});

test("Story-Insights werden nur im verfuegbaren Zeitfenster und gedrosselt aktualisiert", async () => {
  const aufgerufeneIds = [];
  const ig = {
    host: "instagram",
    async anfrage(_methode, pfad, params) {
      aufgerufeneIds.push(String(pfad).split("/")[0]);
      if (params.metric === "navigation") return { data: [{ name: "navigation", values: [{ value: 8 }] }] };
      return insightAntwort(params.metric);
    },
  };
  const jetzt = new Date("2026-09-19T12:00:00.000Z");
  const ledger = {
    veroeffentlicht: [
      { art: "story", medienId: "11111", datum: "2026-09-19", veroeffentlicht: "2026-09-19T10:00:00.000Z" },
      { art: "story", medienId: "22222", datum: "2026-09-19", veroeffentlicht: "2026-09-19T11:30:00.000Z" },
      { art: "story", medienId: "33333", datum: "2026-09-18", veroeffentlicht: "2026-09-18T10:00:00.000Z" },
      { art: "story", medienId: "44444", datum: "2026-09-19", veroeffentlicht: "2026-09-19T03:00:00.000Z", insightsStand: "2026-09-19T10:00:00.000Z" },
      { art: "story", medienId: "55555", datum: "2026-09-18", veroeffentlicht: "2026-09-18T14:30:00.000Z", insightsStand: "2026-09-19T09:00:00.000Z" },
      { art: "beitrag", medienId: "66666", datum: "2026-09-19", veroeffentlicht: "2026-09-19T10:00:00.000Z" },
    ],
  };

  const r = await storyInsightsAktualisieren(ig, ledger, { jetzt, log: () => {} });
  assert.deepEqual(r, { gemessen: 2, versucht: 2 });
  assert.deepEqual([...new Set(aufgerufeneIds)].sort(), ["11111", "55555"]);
  assert.equal(ledger.veroeffentlicht[0].insights.reach, 120);
  assert.equal(ledger.veroeffentlicht[0].insightsStand, jetzt.toISOString());
  assert.equal(ledger.veroeffentlicht[0].insightsAlterStunden, 2);
  assert.equal(ledger.veroeffentlicht[4].insightsAlterStunden, 21.5);
  assert.equal(ledger.veroeffentlicht[1].insights, undefined);
  assert.equal(ledger.veroeffentlicht[2].insights, undefined);
  assert.equal(ledger.veroeffentlicht[3].insights, undefined);
  assert.equal(ledger.veroeffentlicht[5].insights, undefined);
});
