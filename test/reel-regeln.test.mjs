import test from "node:test";
import assert from "node:assert/strict";
import { normenOhneGesetz } from "../src/pruefung.mjs";

test("Auch gesprochene Normen brauchen ihr Gesetz", () => {
  /* Das Campus-Reel vom 17.09.: zwei Paragrafen, nirgends das Gesetz. */
  assert.deepEqual(
    normenOhneGesetz("Erwerb von Todes wegen nach Paragraf 3 oder Schenkung unter Lebenden nach Paragraf 7 Absatz 1 Nummer 1."),
    ["Paragraf 3", "Paragraf 7"],
  );
  /* Herr Jurist am selben Tag: richtig. */
  assert.deepEqual(normenOhneGesetz("Paragraf 1365 Absatz 1 BGB verlangt die Zustimmung des Ehegatten."), []);
  /* Wird das Gesetz später im selben Text genannt, reicht das der Hörerin. */
  assert.deepEqual(normenOhneGesetz("Paragraf 823 und Paragraf 831 BGB stehen nebeneinander."), []);
});
