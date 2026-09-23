import test from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";

import { storyHtml, folieHtml, buntCss } from "../src/vorlagen.mjs";
import { kontext, coverRendern, browserStarten, browserBeenden, storyTitelEinpassen } from "../src/render.mjs";

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

test("Kurzer Norm-Story-Titel nutzt die Breite und bleibt bei hoechstens zwei Zeilen", async () => {
  const ctx = kontext({ fach: "bgbat", klausur: 1, fachLabel: "BGB Allgemeiner Teil" });
  const html = storyHtml({
    art: "norm",
    norm: "§ 134 BGB · § 108 BGB · § 177 BGB",
    titel: "Nichtig oder schwebend unwirksam?",
    text: "Unterschied sauber prüfen.",
  }, ctx);
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), "hj-story-title-"));
  const datei = path.join(dir, "s6.html");
  fs.writeFileSync(datei, html);
  try {
    const browser = await browserStarten();
    const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
    try {
      await page.goto(`file://${datei}`, { waitUntil: "load" });
      await page.evaluate(() => document.fonts.ready);
      await page.evaluate(storyTitelEinpassen);
      const messung = await page.locator(".story h1").evaluate((el) => {
        const cs = getComputedStyle(el);
        const lineHeight = parseFloat(cs.lineHeight);
        const innen = el.clientHeight - parseFloat(cs.paddingTop) - parseFloat(cs.paddingBottom);
        return {
          zeilen: Math.round(innen / lineHeight),
          breite: el.getBoundingClientRect().width,
          maxBreite: el.parentElement.getBoundingClientRect().width
            - parseFloat(getComputedStyle(el.parentElement).paddingLeft)
            - parseFloat(getComputedStyle(el.parentElement).paddingRight),
        };
      });
      assert.ok(messung.zeilen <= 2, `Titel belegt ${messung.zeilen} Zeilen`);
      assert.ok(messung.breite > 700, `Titelkarte ist unnoetig schmal: ${messung.breite}px`);
    } finally {
      await page.close();
    }
  } finally {
    fs.rmSync(dir, { recursive: true, force: true });
  }
});

test("Streitstand-Story behaelt den Fachkopf", () => {
  const ctx = kontext({ fach: "strafbt", klausur: 2, fachLabel: "Strafrecht BT" });
  const html = storyHtml({
    art: "streitstand",
    titel: "§ 211 zu § 212 StGB: eigener Tatbestand oder Qualifikation?",
    optionen: ["Rechtsprechung: eigener Tatbestand", "Literatur: Qualifikation"],
    text: "Der Streit kann sich bei § 28 StGB auswirken.",
  }, ctx);
  assert.match(html, /class="kopf"/);
  assert.match(html, /Strafrecht BT/);
});

test("Zahl-Story zeigt den Zahlenbezug als exakt nummerierte Punkte", () => {
  const ctx = kontext({ fach: "staat", klausur: 3, fachLabel: "Staatsrecht" });
  const html = storyHtml({
    art: "zahl",
    zahl: "4",
    titel: "Vier Rechtsstaats-Anker",
    punkte: ["Gesetzesbindung", "Effektiver Rechtsschutz", "Verhältnismäßigkeit", "Rechtssicherheit"],
  }, ctx);
  assert.equal((html.match(/class="zp"/g) || []).length, 4);
  assert.match(html, />1<\/b>/);
  assert.match(html, />4<\/b>/);
  assert.throws(() => storyHtml({
    art: "zahl",
    zahl: "3",
    titel: "Drei Voraussetzungen",
    punkte: ["eins", "zwei"],
  }, ctx), /genau 3 sichtbar getrennte punkte/);
});

test("Bildloses Karussell-Cover nutzt Cover-v2 ohne Ersatzmotiv", () => {
  const ctx = kontext({ fach: "methodik", klausur: 0, fachLabel: "Klausurtechnik" });
  const html = folieHtml({
    art: "titel",
    titel: "Anspruchsgrundlage zuerst",
    titelZeilen: ["Anspruchsgrundlage", "zuerst"],
    coverBadge: "Klausurtechnik",
    coverText: "Wer will was von wem woraus?",
    coverBildAuslassen: true,
  }, ctx, 1, 7);
  assert.match(html, /art-titel cover-ohne-bild/);
  assert.match(html, /cover-hinweis/);
  assert.doesNotMatch(html, /class="karte2"/);
  assert.doesNotMatch(html, /class="illu"/);
});

test("CTA kann inhaltsspezifische Icons statt zyklischer Deko vorgeben", () => {
  const ctx = kontext({ fach: "zpo", klausur: 1, fachLabel: "Zivilprozessrecht" });
  const spezifisch = folieHtml({
    art: "cta",
    titel: "TKZ als Startblock",
    punkte: ["Titel benennen", "Klausel prüfen", "Zustellung prüfen", "Vollstreckung starten"],
    icons: ["dokument", "lupe", "umschlag", "hammer"],
  }, ctx, 7, 7);
  const fallback = folieHtml({
    art: "cta",
    titel: "TKZ als Startblock",
    punkte: ["Titel benennen", "Klausel prüfen", "Zustellung prüfen", "Vollstreckung starten"],
  }, ctx, 7, 7);
  assert.notEqual(spezifisch, fallback);
});

test("Langes einzelnes Wort bleibt innerhalb der Story-Titelpille", async () => {
  const ctx = kontext({ fach: "vwgo", klausur: 3, fachLabel: "Verwaltungsprozessrecht" });
  const html = storyHtml({
    art: "teaser",
    titel: "Fortsetzungsfeststellungsklage",
    text: "Der vollständige Beitrag ist jetzt im Feed.",
    pille: "Jetzt im Feed",
  }, ctx);
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), "hj-teaser-title-"));
  const datei = path.join(dir, "teaser.html");
  fs.writeFileSync(datei, html);
  try {
    const browser = await browserStarten();
    const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
    try {
      await page.goto(`file://${datei}`, { waitUntil: "load" });
      await page.evaluate(() => document.fonts.ready);
      await page.evaluate(storyTitelEinpassen);
      const ok = await page.locator(".story h1").evaluate((el) => {
        const root = el.closest(".story").getBoundingClientRect();
        const rs = getComputedStyle(el.closest(".story"));
        const rechts = root.right - parseFloat(rs.paddingRight || 0);
        const b = el.getBoundingClientRect();
        return el.scrollWidth <= el.clientWidth + 1 && b.right <= rechts + 1;
      });
      assert.equal(ok, true);
    } finally {
      await page.close();
    }
  } finally {
    fs.rmSync(dir, { recursive: true, force: true });
  }
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
