import test from "node:test";
import assert from "node:assert/strict";

import { MASSE, BUEHNE_BEITRAG, BUEHNE_CHARAKTER, folieHtml } from "../src/vorlagen.mjs";
import { kontext } from "../src/render.mjs";

test("Feed-Karussells rendern nativ im 4:5-Format", () => {
  assert.equal(MASSE.beitrag.breite, 1080);
  assert.equal(MASSE.beitrag.hoehe, 1350);
  assert.equal(MASSE.beitrag.breite / MASSE.beitrag.hoehe, 4 / 5);
});

test("Charakter-Cover nutzt die 4:5-Flaeche fuer eine grosse Szene", () => {
  assert.ok(BUEHNE_CHARAKTER.flaeche > BUEHNE_BEITRAG.flaeche * 2);
  assert.ok(BUEHNE_CHARAKTER.maxB >= 1000);
  assert.ok(BUEHNE_CHARAKTER.maxH >= 740);

  const html = folieHtml({
    art: "titel",
    titel: "Kündigung: Zugang vor Fristbeginn prüfen",
    icon: "umschlag",
    coverText: "Ohne Zugang keine Frist",
    bild: "data:image/png;base64,AA==",
    bildFrei: true,
    bildTyp: "charakter",
    bildBreite: 1000,
    bildHoehe: 780,
  }, kontext({ fach: "zivil", klausur: 1 }), 1, 6);

  assert.match(html, /frei charakter/);
  assert.doesNotMatch(html, /<div class="cover-hinweis"/);
  assert.doesNotMatch(html, /Ohne Zugang keine Frist/);
  assert.match(html, /1\/6/);
});
