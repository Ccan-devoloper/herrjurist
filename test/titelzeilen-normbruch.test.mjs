import test from "node:test";
import assert from "node:assert/strict";
import { titelZeilen } from "../src/vorlagen.mjs";

test("Titelzeilen: Wörter auf -satz oder -s. sind kein hängender Normbruch", () => {
  const z = ["Kein Schadensersatz", "ohne Vertretenmüssen"];
  assert.deepEqual(titelZeilen(z.join(" "), z), z);
  const y = ["Schlafend arglos.", "Bewusstlos nicht"];
  assert.deepEqual(titelZeilen(y.join(" "), y), y);
});

test("Titelzeilen: echte hängende Fundstelle wird weiter verworfen", () => {
  const z = ["Was verlangt § 344 Abs.", "2 Satz 2 StPO?"];
  assert.notDeepEqual(titelZeilen(z.join(" "), z), z);
  const y = ["Art.", "20 GG"];
  assert.notDeepEqual(titelZeilen(y.join(" "), y), y);
});
