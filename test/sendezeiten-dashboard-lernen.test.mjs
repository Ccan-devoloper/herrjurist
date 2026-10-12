import test from "node:test";
import assert from "node:assert/strict";
import { CONFIG } from "../src/config.mjs";
import { sendezeitenAnwenden } from "../src/sendezeiten.mjs";
import { zeitenWaehlen, kandidatenStunden } from "../src/zeiten.mjs";
import { planAusVorproduktion } from "../src/vorproduktion-live.mjs";
import { planFuerWecker, naechsterTermin } from "../src/vorproduktion-zeitplan.mjs";
import { zeitpunktVon } from "../src/zeit.mjs";

function tagMitZeiten(datum, zeiten) {
  return {
    datum,
    plan: {
      beitraege: zeiten.map((zeit, i) => ({ slot: `b${i + 1}`, zeit, status: "geplant" })),
      stories: zeiten.map((zeit, i) => ({ slot: `s${i + 1}`, zeit, art: "teaser", beitragSlot: `b${i + 1}`, status: "geplant" })),
    },
  };
}

function livePlan(tag, gespeichert = null) {
  return planAusVorproduktion({ tag, rel: `vorproduktion/${tag.datum}.json`, fertigRel: `vorproduktion/${tag.datum}/fertig` }, gespeichert);
}

for (const datum of ["2026-10-14", "2026-10-25", "2027-01-02"]) {
  test(`Dashboard-Zeiten bleiben am ${datum} im Live-Plan und Wecker massgeblich`, () => {
    const zeiten = ["07:45", "11:15", "18:40"];
    const tag = tagMitZeiten(datum, zeiten);
    const vorher = structuredClone(tag);
    for (const plan of [livePlan(tag), planFuerWecker(tag)]) {
      assert.deepEqual(plan.beitraege.map((e) => e.zeit), zeiten);
      assert.deepEqual(plan.stories.map((e) => e.zeit), zeiten);
    }
    assert.deepEqual(tag, vorher);
    const jetzt = zeitpunktVon(datum, "06:00");
    assert.equal(naechsterTermin(planFuerWecker(tag), datum, jetzt), zeitpunktVon(datum, "07:45"));
  });
}

test("Spaetere Dashboard-Aenderungen gewinnen gegen alte noch offene Planzeiten", () => {
  const tag = tagMitZeiten("2026-10-14", ["07:45", "11:15", "18:40"]);
  const gespeichert = livePlan(tag);
  tag.plan.beitraege[0].zeit = "09:10";
  tag.plan.stories[0].zeit = "09:12";
  const vorher = structuredClone(gespeichert);
  for (const plan of [livePlan(tag, gespeichert), planFuerWecker(tag, gespeichert)]) {
    assert.equal(plan.beitraege[0].zeit, "09:10");
    assert.equal(plan.stories[0].zeit, "09:12");
  }
  assert.deepEqual(gespeichert, vorher);
});

test("Zeitlernen reagiert auf Messungen; die Tagesausnahme fixiert spaetere Ergebnisse nicht", () => {
  assert.equal(CONFIG.plan.zeitLernen, true, "Zeitlernen bleibt standardmaessig aktiv");
  const gelernt = (besteStunde) => zeitenWaehlen({
    formate: ["reel"], datum: "2026-10-14", ledger: { veroeffentlicht: [] }, zufall: () => 0,
    statistik: {
      belastbar: true, gesamt: 1600, tagStunden: {},
      stunden: Object.fromEntries(kandidatenStunden().map((h) => [`reel|${h}`, { n: 100, mittel: h === besteStunde ? 20 : 1 }])),
    },
  })[0];
  const zeiten = [gelernt(9), gelernt(20)];
  assert.notEqual(zeiten[0], zeiten[1], "Andere Messungen muessen eine andere Zeitwahl ergeben");
  for (const zeit of zeiten) {
    const plan = { datum: "2026-10-14", beitraege: [{ slot: "b3", zeit, format: "reel", status: "geplant" }], stories: [] };
    assert.equal(sendezeitenAnwenden(plan), plan);
    const tag = { datum: plan.datum, plan };
    assert.equal(livePlan(tag).beitraege[0].zeit, zeit);
    assert.equal(planFuerWecker(tag).beitraege[0].zeit, zeit);
  }
});
