import test from "node:test";
import assert from "node:assert/strict";

import {
  REGEL_DECKEL,
  kostenmessungLesen,
  effektiveKonfiguration,
  richtlinieGate,
  RichtlinieVerletzt,
} from "../src/richtlinie.mjs";

test("temporäre Kostenmessung hebt nur Core an und läuft automatisch aus", () => {
  const aktiv = kostenmessungLesen({
    bis: "2026-09-22T02:00:00.000Z",
    coreUsd: "1.14847",
    jetzt: Date.parse("2026-09-21T02:00:00.000Z"),
  });
  assert.equal(aktiv.aktiv, true);
  assert.equal(aktiv.gueltig, true);
  assert.equal(aktiv.coreUsd, 1.14847);

  const k = effektiveKonfiguration({
    ausloeser: "schedule",
    datum: "2026-09-21",
    kostenMessung: aktiv,
  });
  assert.equal(k.deckel.core, 1.14847);
  assert.equal(k.deckel.engagement, REGEL_DECKEL.engagement);
  assert.equal(k.deckel.research, REGEL_DECKEL.research);
  assert.equal(k.betriebsDeckel.core, 1.12847);
  assert.ok(richtlinieGate({ konfiguration: k }).ok);

  const abgelaufen = kostenmessungLesen({
    bis: "2026-09-22T02:00:00.000Z",
    coreUsd: "1.14847",
    jetzt: Date.parse("2026-09-22T02:00:00.000Z"),
  });
  assert.equal(abgelaufen.aktiv, false);
  assert.equal(abgelaufen.abgelaufen, true);
  const normal = effektiveKonfiguration({
    ausloeser: "schedule",
    datum: "2026-09-22",
    kostenMessung: abgelaufen,
  });
  assert.equal(normal.deckel.core, REGEL_DECKEL.core);
  assert.ok(richtlinieGate({ konfiguration: normal }).ok);
});

test("ungültige temporäre Kostenmessung stoppt vor bezahlten Aufrufen", () => {
  const unvollstaendig = kostenmessungLesen({
    bis: "2026-09-22T02:00:00.000Z",
    coreUsd: "",
    jetzt: Date.parse("2026-09-21T02:00:00.000Z"),
  });
  assert.equal(unvollstaendig.gueltig, false);
  const k = effektiveKonfiguration({
    ausloeser: "schedule",
    datum: "2026-09-21",
    kostenMessung: unvollstaendig,
  });
  assert.equal(k.deckel.core, REGEL_DECKEL.core);
  assert.throws(() => richtlinieGate({ konfiguration: k }), RichtlinieVerletzt);
});

test("manuelles Break Glass behält Vorrang vor aktiver Messung", () => {
  const aktiv = kostenmessungLesen({
    bis: "2026-09-22T02:00:00.000Z",
    coreUsd: "1.14847",
    jetzt: Date.parse("2026-09-21T02:00:00.000Z"),
  });
  const k = effektiveKonfiguration({
    ausloeser: "workflow_dispatch",
    datum: "2026-09-21",
    kostenMessung: aktiv,
    breakGlass: { aktiv: true, betragUsd: 1.5, grund: "bewusster manueller Sonderlauf" },
  });
  assert.equal(k.breakGlass.aktiv, true);
  assert.equal(k.deckel.core, 1.5);
  assert.ok(richtlinieGate({ konfiguration: k }).ok);
});
