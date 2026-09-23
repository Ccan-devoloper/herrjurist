import test from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";

import { storyHtml, buntCss } from "../src/vorlagen.mjs";
import { kontext, coverRendern, browserBeenden } from "../src/render.mjs";

test.after(async () => { await browserBeenden().catch(() => {}); });

test("Fehler-Story nutzt den Titel als falsche Aussage statt eine leere Karte zu rendern", () => {
  const ctx = kontext({ fach: "schuldbt", klausur: 1, fachLabel: "Schuldrecht BT" });
  const titel = "„Unverhältnismäßig = keine Nacherfüllung“ ist zu pauschal";
  const html = storyHtml({
    art: "fehler",
    fach: "schuldbt",
    titel,
    text: "§ 439 Abs. 4 BGB differenziert zwischen den Arten der Nacherfüllung.",
  }, ctx);
  assert.match(html, /Falsch/);
  assert.match(html, /Unverhältnismäßig = keine Nacherfüllung/);
  assert.match(html, /Richtig/);
  assert.doesNotMatch(html, /<div class="u"><\/div>/);
  assert.equal((html.match(/Unverhältnismäßig = keine Nacherfüllung/g) || []).length, 1);
});

test("Fehler-Story bricht bei fehlender richtiger Aufloesung hart ab", () => {
  const ctx = kontext({ fach: "schuldbt", klausur: 1, fachLabel: "Schuldrecht BT" });
  assert.throws(() => storyHtml({
    art: "fehler",
    titel: "Falsche Aussage",
  }, ctx), /richtige Aufloesung/);
});

test("Norm-Story haelt einzelne Gesetzeszitate beim Umbruch zusammen", () => {
  const ctx = kontext({ fach: "bgbat", klausur: 1, fachLabel: "BGB Allgemeiner Teil" });
  const html = storyHtml({
    art: "norm",
    norm: "§ 134 BGB · § 108 BGB · § 177 BGB",
    titel: "Nichtig oder schwebend unwirksam?",
    text: "Unterschied sauber prüfen.",
  }, ctx);
  assert.match(html, /norm-liste/);
  assert.equal((html.match(/class="norm-einheit"/g) || []).length, 3);
  assert.match(html, /§\s*108 BGB/u);
});

test("Charakter-Reel-Cover blendet die redundante Fusszeile aus", () => {
  const css = buntCss(kontext({ fach: "strafbt", klausur: 2, fachLabel: "Strafrecht BT" }));
  assert.match(css, /\.story\.cover:has\(\.frei\.charakter\) \.fuss\{display:none\}/);
});

test("Reel-Cover mit den beiden beanstandeten Hooks bleibt innerhalb des 1080er Canvas", async () => {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), "hj-reel-cover-"));
  try {
    const faelle = [
      {
        fach: "strafbt", klausur: 2, fachLabel: "Strafrecht BT",
        titel: "Urkunde ohne Papier? Wann § 267 StGB trotzdem greift",
        titelZeilen: ["Urkunde ohne Papier?", "Wann § 267 StGB", "trotzdem greift"],
        coverBadge: "Examensklassiker",
      },
      {
        fach: "staat", klausur: 3, fachLabel: "Staatsrecht",
        titel: "Verfassungsbeschwerde: Grundrecht verletzt? Das reicht nicht",
        titelZeilen: ["Verfassungs-", "beschwerde:", "Grundrecht verletzt?", "Das reicht nicht"],
        coverBadge: "Fehlerfalle",
      },
    ];
    for (let i = 0; i < faelle.length; i++) {
      const ziel = path.join(dir, `cover-${i}.jpg`);
      await coverRendern(faelle[i], ziel);
      assert.ok(fs.existsSync(ziel));
      assert.ok(fs.statSync(ziel).size > 10_000);
    }
  } finally {
    fs.rmSync(dir, { recursive: true, force: true });
  }
});
