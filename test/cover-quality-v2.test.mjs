import test from "node:test";
import assert from "node:assert/strict";
import { charaktereFuer, charakterPrompt } from "../src/charakterbild.mjs";
import { titelZeilen, folieHtml, MASSE } from "../src/vorlagen.mjs";
import { kontext } from "../src/render.mjs";
import { CONFIG } from "../src/config.mjs";
import { lernPalette } from "../src/stile.mjs";

const ids = (ziel) => charaktereFuer(ziel).map((x) => x.id);

test("cover-quality-v2: semantische Charakterauswahl fuer die Kernfaelle", () => {
  assert.deepEqual(ids({ titel: "Wann beginnt der Versuch? § 22 StGB" }), ["rex", "mara"]);
  assert.deepEqual(ids({ titel: "§ 142 StGB richtig aufbauen" }), ["rex", "mara"]);
  assert.deepEqual(ids({ titel: "§ 985 BGB: Eigentümer gegen Besitzer", fach: "sachen" }), ["brakk", "form7"]);
  assert.deepEqual(ids({ titel: "Wie prüfst du die betriebsbedingte Kündigung?", fach: "arbeit" }), ["zylla", "flux"]);
  assert.deepEqual(ids({ titel: "Vollstreckungsklausel und Klauselrechtsbehelfe", fach: "zpo" }), ["form7", "flux"]);
  assert.deepEqual(ids({ titel: "Aufschiebende Wirkung nach § 80 VwGO", fach: "vwgo" }), ["mara", "form7"]);
});

test("cover-quality-v2: alte automatische coverCharaktere ueberschreiben Semantik nicht", () => {
  assert.deepEqual(ids({
    titel: "Wann beginnt der Versuch?",
    coverCharaktere: ["form7", "flux"],
  }), ["rex", "mara"]);
});

test("cover-quality-v2: explizit manuelle/chat Charakterwahl darf ueberschreiben", () => {
  assert.deepEqual(ids({
    titel: "Wann beginnt der Versuch?",
    coverCharaktere: ["zylla", "brakk"],
    coverCharaktereQuelle: "chat",
  }), ["zylla", "brakk"]);
  assert.deepEqual(ids({
    titel: "§ 142 StGB richtig aufbauen",
    coverCharaktereManuell: ["flux"],
  }), ["flux"]);
});

test("cover-quality-v2: Prompt erfindet keine Fremdrollen", () => {
  const faelle = [
    { titel: "Wann beginnt der Versuch?" },
    { titel: "§ 142 StGB richtig aufbauen" },
    { titel: "Wie prüfst du die betriebsbedingte Kündigung?" },
    { titel: "Vollstreckungsklausel und Klauselrechtsbehelfe" },
    { titel: "Aufschiebende Wirkung nach § 80 VwGO" },
  ];
  for (const ziel of faelle) {
    const prompt = charakterPrompt(ziel);
    assert.doesNotMatch(prompt, /another character|official|clerk|detective/i);
    assert.match(prompt, /No other human, humanoid, robot, creature/i);
  }
});

test("cover-quality-v2: Titelpillen bleiben bei hoechstens vier semantischen Zeilen", () => {
  assert.equal(titelZeilen("A B C D E F G H I J", ["A", "B", "C", "D", "E", "F"]).length, 4);
  const auto = titelZeilen("Eigenschaftsirrtum ist kein Motivirrtum – merk dir die Ausnahme");
  assert.ok(auto.length >= 2 && auto.length <= 4);
});

test("cover-quality-v2: generische Coverhinweise werden nicht gerendert", () => {
  const html = folieHtml({
    art: "titel",
    titel: "Kündigung: Zugang prüfen",
    titelZeilen: ["Kündigung:", "Zugang prüfen"],
    icon: "umschlag",
    hinweis: "Schau rein!",
  }, kontext({ fach: "arbeit", klausur: 1, fachLabel: "Arbeitsrecht" }), 1, 4);
  assert.doesNotMatch(html, /Schau rein!/);
  assert.doesNotMatch(html, /cover-hinweis/);
});

test("cover-quality-v2: Produktionsparameter und 3:4-Format bleiben kompatibel", () => {
  assert.deepEqual(MASSE.beitrag, { breite: 1080, hoehe: 1440 });
  assert.equal(CONFIG.bilder.charaktere.guete, "high");
  assert.equal(CONFIG.bilder.charaktere.retryGuete, "xhigh");
  assert.equal(CONFIG.bilder.charaktere.reelGuete, "medium");
  assert.equal(CONFIG.bilder.charaktere.reelRetryGuete, "high");
  assert.equal(CONFIG.bilder.charaktere.qaAktiv, true);
});

test("cover-quality-v2: vereinbarte Lernfamilienfarben sind permanent verdrahtet", () => {
  const erwartet = {
    bgbat: ["#8AF0A6", "#0A2B1C"],
    schuld: ["#6DBEFD", "#092653"],
    sachen: ["#E8D0A0", "#372B11"],
    arbeit: ["#15DDDB", "#052234"],
    zpo: ["#388FEA", "#081941"],
    strafat: ["#D97371", "#461214"],
    strafbt: ["#FB902F", "#351A0A"],
    vwgo: ["#E41D78", "#330122"],
    methodik: ["#36E6B2", "#11183A"],
    wochenrueckblick: ["#F1EBDD", "#171717"],
  };
  for (const [fach, [grund, dunkel]] of Object.entries(erwartet)) {
    const p = lernPalette(fach);
    assert.equal(p?.grund, grund, fach);
    assert.equal(p?.dunkel, dunkel, fach);
  }
});
