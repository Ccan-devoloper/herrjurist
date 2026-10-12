import test from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { spawnSync } from "node:child_process";
import { SENDEZEITEN, sendezeitenAnwenden } from "../src/sendezeiten.mjs";
import { planFuerWecker, naechsterTermin } from "../src/vorproduktion-zeitplan.mjs";
import { planAusVorproduktion, feedWartezeitMs } from "../src/vorproduktion-live.mjs";
import { zeitpunktVon } from "../src/zeit.mjs";

const root = fileURLToPath(new URL("../", import.meta.url));
const planAlt = () => ({
  datum: "2026-10-13",
  beitraege: [
    { slot: "b1", zeit: "08:00", status: "geplant" },
    { slot: "b2", zeit: "12:30", status: "geplant" },
    { slot: "b3", zeit: "17:30", status: "geplant", format: "reel" },
  ],
  stories: [
    { slot: "s1", zeit: "08:00", art: "teaser", beitragSlot: "b1", status: "geplant" },
    { slot: "s2", zeit: "12:30", art: "teaser", beitragSlot: "b2", status: "geplant" },
    { slot: "s3", zeit: "17:30", art: "teaser", beitragSlot: "b3", status: "geplant" },
    { slot: "s4", zeit: "07:06", art: "frage", status: "geplant" },
  ],
});

test("Neue Betreiberzeiten ab 13.10.; alte Plaene und Eingabe bleiben unveraendert", () => {
  const alt = planAlt();
  const copy = structuredClone(alt);
  const neu = sendezeitenAnwenden(alt);
  assert.deepEqual(neu.beitraege.map((e) => e.zeit), Object.values(SENDEZEITEN));
  assert.deepEqual(neu.stories.map((e) => e.zeit), ["06:30", "10:30", "17:30", "07:06"]);
  assert.deepEqual(alt, copy);
  assert.equal(sendezeitenAnwenden(alt, "2026-10-12"), alt);
  assert.equal(sendezeitenAnwenden(alt, undefined).beitraege[0].zeit, "06:30");
  assert.equal(sendezeitenAnwenden(alt, "2027-01-02").beitraege[0].zeit, "06:30");
  assert.equal(sendezeitenAnwenden(alt, "ungueltig"), alt);
});

test("Veroeffentlichte Slots, IDs, Sperren und fremde Slots bleiben erhalten", () => {
  const plan = planAlt();
  Object.assign(plan.beitraege[0], { status: "veroeffentlicht", medienId: "123456" });
  Object.assign(plan.beitraege[1], { fehler: "Testfehler", freigabeBetreiber: false });
  plan.beitraege.push({ slot: "b4", zeit: "21:00", status: "geplant" });
  const neu = sendezeitenAnwenden(plan);
  assert.equal(neu.beitraege[0], plan.beitraege[0]);
  assert.equal(neu.beitraege[0].medienId, "123456");
  assert.equal(neu.stories[0].zeit, "08:00");
  assert.equal(neu.beitraege[1].fehler, "Testfehler");
  assert.equal(neu.beitraege[1].freigabeBetreiber, false);
  assert.equal(neu.beitraege[3].zeit, "21:00");
});

test("Live-Plan und Weckkette verwenden identische Uhrzeiten", () => {
  const alt = planAlt();
  const tag = { datum: alt.datum, plan: alt };
  const vp = { tag, rel: "vorproduktion/2026-10-13.json", fertigRel: "vorproduktion/2026-10-13/fertig" };
  const live = planAusVorproduktion(vp);
  const wecker = planFuerWecker(tag);
  assert.deepEqual(live.beitraege, wecker.beitraege.map(({ fehler: _fehler, ...e }) => e));
  assert.deepEqual(live.stories, wecker.stories.map(({ fehler: _fehler, ...e }) => e));
  assert.equal(feedWartezeitMs(live, 6 * 3600 + 24 * 60, 100, 180), 180000);
  const vorher = zeitpunktVon(alt.datum, "06:00");
  assert.equal(naechsterTermin(wecker, alt.datum, vorher), zeitpunktVon(alt.datum, "06:30"));
});

test("Zeitumstellung veraendert UTC, aber nicht 06:30 Berliner Ortszeit", () => {
  assert.equal(new Date(zeitpunktVon("2026-10-13", "06:30")).toISOString(), "2026-10-13T04:30:00.000Z");
  assert.equal(new Date(zeitpunktVon("2026-10-25", "06:30")).toISOString(), "2026-10-25T05:30:00.000Z");
  assert.equal(new Date(zeitpunktVon("2026-12-01", "17:30")).toISOString(), "2026-12-01T16:30:00.000Z");
});

function shell(mode, command) {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), "weckruf-test-"));
  try {
    const calls = path.join(dir, "calls");
    fs.writeFileSync(path.join(dir, "gh"), `#!/usr/bin/env bash
n=$(cat "$GH_CALLS" 2>/dev/null || echo 0)
n=$((n + 1))
echo "$n" > "$GH_CALLS"
case "$GH_MODE" in
  transient) if [ "$n" -lt 2 ]; then echo '{"message":"Server Error"}'; exit 1; fi; echo '2026-10-12T12:35:27Z';;
  failure) echo '{"message":"Server Error"}'; exit 1;;
  badjson) echo '{"message":"Server Error"}';;
  baddate) echo '2026-99-99T12:00:00Z';;
  null) echo null;;
  newer) echo 1;;
  none) echo 0;;
  dispatch) if [ "$n" -lt 2 ]; then exit 1; fi;;
esac
`, { mode: 0o755 });
    const r = spawnSync("bash", ["-c", `set -euo pipefail; source bin/weckruf.sh; sleep() { :; }; ${command}`], {
      cwd: root, encoding: "utf8", timeout: 5000,
      env: { ...process.env, PATH: `${dir}:${process.env.PATH}`, GH_CALLS: calls, GH_MODE: mode,
        GH_REPO: "test/repo", GH_TOKEN: "test-placeholder", GITHUB_RUN_ID: "123" },
    });
    assert.equal(r.error, undefined);
    assert.equal(r.status, 0, r.stderr);
    return { stdout: r.stdout.trim(), stderr: r.stderr, calls: Number(fs.readFileSync(calls, "utf8")) };
  } finally { fs.rmSync(dir, { recursive: true, force: true }); }
}

test("502 wird wiederholt; Fehler-JSON gelangt nicht in date", () => {
  const r = shell("transient", 'laufstart_epoch 42; echo weiter');
  assert.equal(r.stdout, `${Date.parse("2026-10-12T12:35:27Z") / 1000}\nweiter`);
  assert.equal(r.calls, 2);
});

for (const mode of ["failure", "badjson", "baddate", "null"]) {
  test(`Ungueltiger Laufstart (${mode}) faellt auch mit set -e sicher zurueck`, () => {
    const r = shell(mode, 'laufstart_epoch 42; echo weiter');
    assert.equal(r.stdout, "42\nweiter");
    assert.equal(r.calls, mode === "failure" ? 3 : 1);
    assert.ok(!r.stdout.includes("Server Error"));
  });
}

test("Unbekannter Kettenstatus wird nicht fuer eine juengere Kette gehalten", () => {
  assert.equal(shell("failure", 'if juengere_kette_aktiv; then echo beenden; else echo weiter; fi').stdout, "weiter");
  assert.equal(shell("badjson", 'if juengere_kette_aktiv; then echo beenden; else echo weiter; fi').stdout, "weiter");
  assert.equal(shell("none", 'if juengere_kette_aktiv; then echo beenden; else echo weiter; fi').stdout, "weiter");
  assert.equal(shell("newer", 'if juengere_kette_aktiv; then echo beenden; else echo weiter; fi').stdout, "beenden");
});

test("Auch ein voruebergehend gescheiterter Dispatch wird wiederholt", () => {
  assert.equal(shell("dispatch", "wecken").calls, 2);
});
