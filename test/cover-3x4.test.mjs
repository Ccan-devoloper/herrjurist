import test from "node:test";
import assert from "node:assert/strict";

import { MASSE, BUEHNE_BEITRAG, BUEHNE_CHARAKTER, folieHtml } from "../src/vorlagen.mjs";
import { kontext } from "../src/render.mjs";

test("Feed-Karussells rendern nativ im 3:4-Format", () => {
  assert.equal(MASSE.beitrag.breite, 1080);
  assert.equal(MASSE.beitrag.hoehe, 1440);
  assert.equal(MASSE.beitrag.breite / MASSE.beitrag.hoehe, 3 / 4);
});

test("Charakter-Cover nutzt die zusaetzliche 3:4-Hoehe fuer eine grosse Szene", () => {
  assert.ok(BUEHNE_CHARAKTER.flaeche > BUEHNE_BEITRAG.flaeche * 2);
  assert.ok(BUEHNE_CHARAKTER.maxB >= 1000);
  assert.ok(BUEHNE_CHARAKTER.maxH >= 800);

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
  assert.match(html, /cover-hinweis/);
  assert.match(html, /Ohne Zugang keine Frist/);
});
