import test from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { execFileSync } from "node:child_process";
import { CHARAKTERE, charaktereFuer, charakterPrompt } from "../src/charakterbild.mjs";
import { titelZeilen, folieHtml, buntCss, BUEHNE_CHARAKTER, MASSE } from "../src/vorlagen.mjs";
import { kontext } from "../src/render.mjs";
import { CONFIG } from "../src/config.mjs";
import { lernPalette } from "../src/stile.mjs";

const ids = (ziel) => charaktereFuer(ziel).map((x) => x.id);

test("cover-quality-v2: alle kanonischen Charakterreferenzen sind dekodierbare JPEGs", () => {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), "hj-ref-test-"));
  try {
    for (const ch of Object.values(CHARAKTERE)) {
      const b64 = fs.readFileSync(new URL(`../assets/charaktere/${ch.datei}`, import.meta.url), "utf8").trim();
      assert.match(b64, /^[A-Za-z0-9+/]+={0,2}$/, `${ch.name}: Referenz enthaelt Nicht-Base64-Zeichen oder Platzhalter`);
      const roh = path.join(dir, `${ch.id}.jpg`);
      const probe = path.join(dir, `${ch.id}-probe.png`);
      const bytes = Buffer.from(b64, "base64");
      assert.equal(bytes[0], 0xff, `${ch.name}: JPEG-SOI fehlt`);
      assert.equal(bytes[1], 0xd8, `${ch.name}: JPEG-SOI fehlt`);
      assert.equal(bytes.at(-2), 0xff, `${ch.name}: JPEG-EOI fehlt`);
      assert.equal(bytes.at(-1), 0xd9, `${ch.name}: JPEG-EOI fehlt`);
      fs.writeFileSync(roh, bytes);
      assert.doesNotThrow(() => execFileSync("ffmpeg", [
        "-y", "-loglevel", "error", "-i", roh, "-frames:v", "1", probe,
      ]), `${ch.name}: Masterreferenz ist nicht dekodierbar`);
      assert.ok(fs.existsSync(probe) && fs.statSync(probe).size > 0, `${ch.name}: ffmpeg erzeugt kein Prüfbild`);
    }
  } finally {
    fs.rmSync(dir, { recursive: true, force: true });
  }
});

test("cover-quality-v2: Legacy-Fallback bleibt fuer alte Inhalte deterministisch", () => {
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
test("cover-quality-v2: strukturierte Cover-Regie darf Cast und Szene frei bestimmen", () => {
  const ziel = {
    titel: "Vollstreckungsklausel und Klauselrechtsbehelfe",
    fach: "zpo",
    coverRegie: {
      charaktere: ["rex", "zylla"],
      kernidee: "Eine formale Freigabe entscheidet, ob es weitergeht.",
      handlung: "{A} tries to pass a sealed case capsule through a checkpoint while {B} discovers the missing clearance tag.",
      alternative: "{A} holds a locked legal crate while {B} finds the one matching clearance key.",
      hinweisZiel: "the missing clearance tag",
      hinweisZone: "left-mid",
    },
  };
  assert.deepEqual(ids(ziel), ["rex", "zylla"]);
  const prompt = charakterPrompt(ziel);
  assert.match(prompt, /sealed case capsule/);
  assert.match(prompt, /left-middle edge/);
  assert.match(prompt, /missing clearance tag/);
  assert.match(prompt, /Do NOT draw handwriting, arrows/i);
  assert.doesNotMatch(prompt, /leftmost roughly 16 percent/i);
  assert.doesNotMatch(prompt, /three separate blank legal objects/);
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

test("cover-quality-v2: juristische Fundstellen brechen nur an sinnvollen Grenzen", () => {
  assert.deepEqual(
    titelZeilen("Was verlangt § 344 Abs. 2 Satz 2 StPO?"),
    ["Was verlangt", "§ 344 Abs. 2", "Satz 2 StPO?"],
  );
  assert.deepEqual(
    titelZeilen("Was verlangt § 344 Abs. 2 Satz 2 StPO?", ["Was verlangt §", "344 Abs. 2 Satz", "2 StPO?"]),
    ["Was verlangt", "§ 344 Abs. 2", "Satz 2 StPO?"],
  );
  assert.deepEqual(
    titelZeilen("§ 80 Abs. 5 VwGO? Erst Vollziehung prüfen"),
    ["§ 80 Abs. 5 VwGO?", "Erst Vollziehung", "prüfen"],
  );
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
  assert.doesNotMatch(html, /<div class="cover-hinweis">/);
});

test("cover-quality-v2: Produktionsparameter und 4:5-Format entsprechen dem Referenzlook", () => {
  assert.deepEqual(MASSE.beitrag, { breite: 1080, hoehe: 1350 });
  assert.equal(CONFIG.bilder.charaktere.guete, "high");
  assert.equal(CONFIG.bilder.charaktere.retryGuete, "xhigh");
  assert.equal(CONFIG.bilder.charaktere.reelGuete, "medium");
  assert.equal(CONFIG.bilder.charaktere.reelRetryGuete, "high");
  assert.equal(CONFIG.bilder.charaktere.qaAktiv, true);
});

test("cover-quality-v2: Golden-Reference-Layout bleibt als Markenvertrag abgesichert", () => {
  const archiv = fs.readFileSync(new URL("../assets/referenzen/cover-v2/reference-images.zip", import.meta.url));
  assert.ok(archiv.length > 10_000, "Referenzarchiv ist unerwartet leer/klein");
  assert.equal(archiv[0], 0x50, "ZIP-Signatur P fehlt");
  assert.equal(archiv[1], 0x4b, "ZIP-Signatur K fehlt");

  assert.deepEqual(BUEHNE_CHARAKTER, { flaeche: 1040 * 820 * 0.98, maxB: 1060, maxH: 820 });

  const ctx = kontext({ fach: "zpo", klausur: 1, fachLabel: "ZPO" });
  const cssText = buntCss(ctx);
  assert.match(cssText, /\.art-titel\{padding-left:52px;padding-right:52px\}/);
  assert.match(cssText, /\.art-titel>\.kopf\{left:-52px;top:-72px;right:-52px\}/);
  assert.match(cssText, /font-size:104px/);
  assert.match(cssText, /\.frei\.charakter\{right:-6px;bottom:0;width:940px;height:800px\}/);
  assert.match(cssText, /\.cover-hinweis\{[^}]*z-index:6/);
  assert.match(cssText, /\.cover-hinweis-pfeil\{/);
  assert.match(cssText, /\.art-titel:has\(\.frei\) \.fuss\{[^}]*bottom:24px/);

  const html = folieHtml({
    art: "titel",
    titel: "Zulässigkeit kommt vor Begründetheit",
    titelZeilen: ["Zulässigkeit", "kommt vor", "Begründetheit"],
    coverBadge: "Klausurrelevant",
    coverText: "Reihenfolge merken",
    coverHinweisZone: "right-mid",
    coverHinweisZiel: "document stack",
    icon: "dokument",
  }, ctx, 1, 6);
  assert.match(html, />1\/6</);
  assert.match(html, /class="cover-hinweis" data-zone="right-mid" data-ziel="document stack"/);
  assert.match(html, /class="cover-hinweis-text"/);
  assert.match(html, /class="cover-hinweis-pfeil"/);
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
