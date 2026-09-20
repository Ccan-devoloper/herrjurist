import { test } from "node:test";
import assert from "node:assert/strict";
import { wochenThemenPrompt } from "../src/autor.mjs";
import { pruefeWochenrueckblick } from "../src/pruefung.mjs";

test("Wochenrückblick gruppiert Unterfächer nach den drei Rechtsgebieten", () => {
  const prompt = wochenThemenPrompt([
    { titel: "Anfechtung und Vertrauensschaden", fach: "bgbat" },
    { titel: "Belehrung nach § 136 StPO", fach: "stpo" },
    { titel: "Eilantrag nach § 80 Abs. 5 VwGO", fach: "vwgo" },
    { titel: "Zeitmanagement in der Klausur", fach: "methodik" },
  ]);

  const zivil = prompt.indexOf("### Zivilrecht");
  const straf = prompt.indexOf("### Strafrecht");
  const oeff = prompt.indexOf("### Öffentliches Recht");
  const methode = prompt.indexOf("### Klausur- und Lernmethodik");

  assert.ok(zivil >= 0 && straf > zivil && oeff > straf && methode > oeff);
  assert.match(prompt.slice(zivil, straf), /\[BGB AT\] Anfechtung und Vertrauensschaden/);
  assert.doesNotMatch(prompt.slice(oeff, methode), /BGB AT/);
  assert.match(prompt.slice(straf, oeff), /\[StPO\] Belehrung nach § 136 StPO/);
  assert.match(prompt.slice(oeff, methode), /\[VwGO\] Eilantrag nach § 80 Abs\. 5 VwGO/);
});

test("Wochenrückblick verlangt je Rechtsgebiet eine eigene Folie", () => {
  const gut = {
    format: "wochenrueckblick",
    folien: [
      { titel: "Die Woche im Überblick", text: "" },
      { titel: "Zivilrecht der Woche", punkte: ["BGB AT"] },
      { titel: "Strafrecht der Woche", punkte: ["StPO"] },
      { titel: "Öffentliches Recht der Woche", punkte: ["VwGO"] },
      { titel: "Klausurtechnik fürs Wochenende", text: "Wiederholen" },
      { art: "cta", titel: null },
    ],
  };
  assert.deepEqual(pruefeWochenrueckblick(gut), []);

  const gemischt = JSON.parse(JSON.stringify(gut));
  gemischt.folien[1].titel = "Zivil- und Strafrecht der Woche";
  assert.ok(pruefeWochenrueckblick(gemischt).length > 0);

  const bgbFalsch = JSON.parse(JSON.stringify(gut));
  bgbFalsch.folien[3].punkte = ["BGB AT: § 122 BGB"];
  assert.match(pruefeWochenrueckblick(bgbFalsch).join("\n"), /BGB AT gehört zum Zivilrecht/);
});
