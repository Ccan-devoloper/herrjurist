import test from "node:test";
import assert from "node:assert/strict";
import { storyInsights, storyInsightsAktualisieren, medienInsights, kontoInsights } from "../src/insights.mjs";

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


test("Karussells speichern views genauso wie Reels", async () => {
  const angefragt = [];
  const ig = {
    async anfrage(_methode, pfad, params) {
      angefragt.push({ pfad, metric: params.metric });
      const werte = { reach: 700, views: 980, saved: 44, shares: 8, likes: 35, comments: 2, total_interactions: 89, follows: 3, profile_visits: 12, reposts: 1 };
      return { data: String(params.metric).split(",").map((name) => ({ name, values: [{ value: werte[name] ?? 0 }] })) };
    },
  };
  const m = await medienInsights(ig, { id: "17900000000000001", media_type: "CAROUSEL_ALBUM", media_product_type: "FEED" });
  assert.equal(m.views, 980);
  assert.equal(m.reach, 700);
  assert.equal(m.saved, 44);
  assert.equal(m.follows, 3);
  assert.ok(angefragt.some((x) => String(x.metric).split(",").includes("views")), "views muss für Karussells abgefragt werden");
});

test("Konto-Insights archivieren Ansichten und Interaktionen für 7/14/30 Tage", async () => {
  const ig = {
    kontoId: "17890000000000000",
    async anfrage(_methode, pfad, params) {
      if (pfad === this.kontoId && params.fields === "followers_count,media_count") return { followers_count: 6500, media_count: 180 };
      if (pfad === this.kontoId && /biography/.test(params.fields || "")) return { biography: "bio", website: "", profile_picture_url: "x", name: "Herr Jurist" };
      if (String(pfad).endsWith("/insights") && params.metric === "online_followers") return { data: [{ name: "online_followers", values: [{ value: { "18": 120 } }] }] };
      if (String(pfad).endsWith("/insights")) {
        const tage = Math.round((params.until - params.since) / 86400);
        const basis = tage * 100;
        return { data: String(params.metric).split(",").map((name) => ({ name, total_value: { value: name === "views" ? basis : name === "reach" ? Math.round(basis * .7) : 5 } })) };
      }
      throw new Error("unerwarteter Aufruf");
    },
  };
  const k = await kontoInsights(ig);
  assert.equal(k.follower, 6500);
  assert.equal(k.ansichten7, 700);
  assert.equal(k.reichweite7, 490);
  assert.equal(k.zeitraeume["14"].views, 1400);
  assert.equal(k.zeitraeume["30"].views, 3000);
  assert.deepEqual(k.onlineStunden, { "18": 120 });
});
