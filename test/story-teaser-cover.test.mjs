import test from "node:test";
import assert from "node:assert/strict";

import { teaserAusBeitrag } from "../src/autor.mjs";
import { storyHtml } from "../src/vorlagen.mjs";
import { kontext } from "../src/render.mjs";

test("Story-Teaser zeigt das fertige Cover des verknuepften Beitrags", () => {
  const motiv = "data:image/png;base64,iVBORw0KGgo=";
  const cover = "https://example.invalid/fertig/b1/cover.jpg";
  const beitrag = {
    fach: "schuld",
    klausur: 1,
    fachLabel: "Schuldrecht",
    kurztitel: "Kurz",
    folien: [{ art: "titel", titel: "Der volle Titel", icon: "vertrag", bild: motiv, bildFrei: true }],
  };
  const teaser = teaserAusBeitrag(beitrag, "s1", cover);
  assert.equal(teaser.coverBild, cover);
  assert.equal(teaser.bild, motiv, "Motiv bleibt nur als Rueckfall erhalten");

  const html = storyHtml(teaser, kontext({ fach: "schuld", klausur: 1 }));
  assert.match(html, /class="teaser-cover"/);
  assert.ok(html.includes(cover));
});

test("persistiertes Final-Cover wird ohne expliziten Parameter uebernommen", () => {
  const cover = "https://raw.githubusercontent.com/example/repo/main/cover.jpg";
  const teaser = teaserAusBeitrag({
    fach: "zpo", klausur: 1, coverFinalUrl: cover,
    folien: [{ art: "titel", titel: "Titel", icon: "paragraf" }],
  }, "s2");
  assert.equal(teaser.coverBild, cover);
});
