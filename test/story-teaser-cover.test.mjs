import test from "node:test";
import assert from "node:assert/strict";

import { teaserAusBeitrag } from "../src/autor.mjs";
import { storyHtml } from "../src/vorlagen.mjs";
import { kontext } from "../src/render.mjs";

test("Story-Teaser zeigt nur den Freisteller, nie das fertige Beitragscover", () => {
  const motiv = "data:image/png;base64,iVBORw0KGgo=";
  const cover = "https://example.invalid/fertig/b1/cover.jpg";
  const beitrag = {
    fach: "schuld",
    klausur: 1,
    fachLabel: "Schuldrecht",
    kurztitel: "Kurz",
    coverFinalUrl: cover,
    teaserCoverUrl: cover,
    folien: [{ art: "titel", titel: "Der volle Titel", icon: "vertrag", bild: motiv, bildFrei: true }],
  };
  const teaser = teaserAusBeitrag(beitrag, "s1");
  assert.equal(teaser.bild, motiv);
  assert.equal("coverBild" in teaser, false);

  const html = storyHtml(teaser, kontext({ fach: "schuld", klausur: 1 }));
  assert.match(html, /class="frei"/);
  assert.ok(html.includes(motiv));
  assert.ok(!html.includes(cover));
  assert.ok(!html.includes("teaser-cover"));
});

test("Reel-Teaser übernimmt den Freisteller vom Reel-Objekt", () => {
  const motiv = "data:image/png;base64,reelmotiv";
  const teaser = teaserAusBeitrag({
    fach: "strafbt", klausur: 2, bild: motiv, bildFrei: true,
    szenen: [{ titel: "Reel-Titel", icon: "paragraf" }],
  }, "s3");
  assert.equal(teaser.bild, motiv);
});
