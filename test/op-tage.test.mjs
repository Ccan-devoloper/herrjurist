import { test } from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { spawnSync } from "node:child_process";

/* Quellenprüfung aller Open-Peeps-Tagesbeschreibungen (op/tage/<datum>.json) mit dem echten,
   verschlüsselten Themenpool – dieselbe Prüfung, die op/tag.py vor dem Ablegen ausführt
   (bin/op-pruefen.mjs), hier aber ohne Rendern: Geprüft werden alle sichtbaren und gesprochenen
   Texte sowie die Captions. Läuft in „Validate“ mit IG_WISSEN_KEY; ohne Schlüssel übersprungen. */

const TAGE = new URL("../op/tage/", import.meta.url);
const TECHNISCH = new Set(["slot", "zeit", "format", "fach", "klausur", "themaId", "themaTitel", "figuren", "figur", "x", "typ",
  "badgeFarbe", "farbe", "motiv", "icon", "iconFarbe", "layout", "reelTyp", "stil", "wort", "woerter", "cta_wort", "blase_wort",
  "seg", "id", "hashtags", "quellen", "klausurLabel", "beitragSlot", "art", "richtig", "ls", "zs", "size", "h", "abstand", "sfx",
  "nr", "pose", "mimik", "datum", "name", "fachLabel", "hoehe", "anim", "groesse", "normImTitel"]);

function texte(wert, aus = []) {
  if (typeof wert === "string") {
    const t = wert.trim();
    if (t && !/^[a-z-]+:[a-z0-9-]+$/.test(t) && !/^[A-Z]{3,}$/.test(t) && !/^[A-Z][:/][a-z]+$/.test(t)) aus.push(t);
  } else if (Array.isArray(wert)) {
    for (const x of wert) texte(x, aus);
  } else if (wert && typeof wert === "object") {
    for (const [k, v] of Object.entries(wert)) if (!TECHNISCH.has(k)) texte(v, aus);
  }
  return aus;
}

const tage = fs.existsSync(TAGE) ? fs.readdirSync(TAGE).filter((f) => /^\d{4}-\d{2}-\d{2}\.json$/.test(f)).sort() : [];

test("op/tage: keine Übernahmen aus dem Themenpool, keine gesperrten Namen", { skip: !process.env.IG_WISSEN_KEY && "IG_WISSEN_KEY fehlt" }, () => {
  const daten = {};
  for (const f of tage) {
    const tag = JSON.parse(fs.readFileSync(new URL(f, TAGE), "utf8"));
    for (const b of tag.beitraege || []) daten[`${tag.datum}-${b.slot}-alle.jpg`] = texte(b);
    daten[`${tag.datum}-s1-stories.jpg`] = texte(tag.stories || []);
  }
  const datei = path.join(fs.mkdtempSync(path.join(os.tmpdir(), "op-tage-")), "texte.json");
  fs.writeFileSync(datei, JSON.stringify(daten));
  const r = spawnSync(process.execPath, [new URL("../bin/op-pruefen.mjs", import.meta.url).pathname, datei], { encoding: "utf8" });
  const befunde = r.stdout.split("\n").filter((z) => z.startsWith("✗") || z.startsWith("   - "));
  assert.equal(r.status, 0, `Quellenprüfung op/tage:\n${befunde.join("\n")}\n${r.stderr}`);
});

test("op/tage: Quizpaare tragen dieselben drei Optionen", () => {
  for (const f of tage) {
    const tag = JSON.parse(fs.readFileSync(new URL(f, TAGE), "utf8"));
    const quiz = (tag.stories || []).filter((s) => s.art === "frage" || s.art === "antwort");
    const frage = quiz.find((s) => s.art === "frage"), antwort = quiz.find((s) => s.art === "antwort");
    if (!frage && !antwort) continue;
    assert.ok(frage && antwort, `${f}: Quiz braucht Frage und Antwort`);
    assert.equal(frage.optionen?.length, 3, `${f}: Frage braucht drei Optionen`);
    assert.deepEqual(antwort.optionen, frage.optionen, `${f}: Antwort und Frage mit unterschiedlichen Optionen`);
    assert.ok(Number.isInteger(antwort.richtig) && antwort.richtig >= 0 && antwort.richtig < 3, `${f}: Antwort ohne gültige Markierung`);
    assert.equal(antwort.themaId, frage.themaId, `${f}: Quizpaar mit unterschiedlicher themaId`);
  }
});
