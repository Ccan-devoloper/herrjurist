import test from "node:test";
import assert from "node:assert/strict";

import { persistierteStoryBeanstandungen, storyFreigabe } from "../src/pruefung.mjs";
import { budgetStarten, AdmissionAbgelehnt } from "../src/budget.mjs";

test("Regression: gespeicherte fachliche Beanstandungen werden im Folgelauf erneut repariert", () => {
  const geschrieben = new Map([
    ["s4", { slot: "s4", art: "frage", beanstandetFachlich: ["fachlicher Fehler"] }],
    ["s5", { slot: "s5", art: "antwort", beanstandetFachlich: [] }],
    ["s6", { slot: "s6", art: "merksatz", beanstandetFachlich: ["neu in diesem Lauf"] }],
  ]);
  const schonVorhanden = new Set(["s4", "s5"]);

  const erneut = persistierteStoryBeanstandungen(geschrieben, schonVorhanden);
  assert.deepEqual(erneut.map((s) => s.slot), ["s4"],
    "nur bereits gespeicherte und weiterhin beanstandete Stories gehen erneut in die Reparaturschleife");

  const gate = storyFreigabe(geschrieben.get("s4"));
  assert.equal(gate.frei, false, "vor der Reparatur darf die Story nicht veröffentlicht werden");
  assert.equal(gate.warten, true, "sie bleibt reparierbar statt endgültig auszufallen");
});

test("Regression: Schwesterbudget steht nur Pflichtarbeit zur Verfügung und erhöht nicht den Gesamtdeckel", () => {
  const deckel = { core: 0.30, engagement: 0.20, research: 0.10 };
  const budget = budgetStarten({
    deckel,
    bisher: { core: 0.28, engagement: 0, research: 0 },
    fremdFrei: { core: 0.10, engagement: 0, research: 0 },
  });

  /* Lokal sind nur 0,02 $ frei. Pflichtarbeit darf zusätzlich die 0,10 $
     nachweislich freien Schwester-Rest nutzen. */
  const pflicht = budget.zulassen("autor", 0.08, { pflichtName: "b2" });
  assert.equal(pflicht.reservedUsd, 0.08);
  pflicht.freigeben();

  /* Optionale Arbeit darf das Schwesterbudget ausdrücklich NICHT verwenden. */
  assert.throws(
    () => budget.zulassen("autor", 0.03, { optional: true }),
    AdmissionAbgelehnt,
    "optionale Arbeit bleibt am lokalen Deckel"
  );

  /* 0,02 lokal + 0,10 Schwester = 0,12. Auch Pflichtarbeit darf nicht mehr
     als diesen gemeinsamen nachweislich freien Betrag versprechen. */
  assert.throws(
    () => budget.zulassen("autor", 0.121, { pflichtName: "b2" }),
    AdmissionAbgelehnt,
    "der kombinierte verfügbare Betrag bleibt eine harte Obergrenze"
  );
});
