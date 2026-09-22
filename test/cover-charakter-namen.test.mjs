import test from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";

import { CHARAKTER_NAMEN, COVER_FALLNAMEN_REGEL, MANUELLER_COVER_FALLNAMEN_HINWEIS } from "../src/charaktere.mjs";
import { CHARAKTERE } from "../src/charakterbild.mjs";
import { FORMATE } from "../src/autor.mjs";
import { MANUELLE_FINALISIERUNG_REGELN } from "../src/finalisierung.mjs";

test("Cover-Cast hat eine gemeinsame stabile Namensquelle", () => {
  for (const [id, name] of Object.entries(CHARAKTER_NAMEN)) {
    assert.equal(CHARAKTERE[id]?.name, name, id);
  }
});

test("automatische Beitragsredaktion koppelt fiktive Fallnamen an coverRegie", () => {
  assert.match(COVER_FALLNAMEN_REGEL, /coverRegie\.charaktere/);
  assert.match(COVER_FALLNAMEN_REGEL, /Rex Rohrbruch/);
  assert.match(COVER_FALLNAMEN_REGEL, /Zylla Glitch/);
  assert.match(FORMATE.minifall.anleitung, /coverRegie/);

  const autorQuelle = fs.readFileSync(new URL("../src/autor.mjs", import.meta.url), "utf8");
  assert.match(autorQuelle, /\$\{COVER_FALLNAMEN_REGEL\}/);
  assert.match(autorQuelle, /wiederkehrenden Cover-Charaktere sind die ausdrückliche Ausnahme/);
});

test("manuelle KI-Finalisierung bekommt nur einen nicht blockierenden Hinweis", () => {
  assert.equal(MANUELLE_FINALISIERUNG_REGELN.charakterNamen, MANUELLER_COVER_FALLNAMEN_HINWEIS);
  assert.match(MANUELLER_COVER_FALLNAMEN_HINWEIS, /nicht blockierend/i);
  assert.match(MANUELLER_COVER_FALLNAMEN_HINWEIS, /bildCharaktere/);
  assert.match(MANUELLER_COVER_FALLNAMEN_HINWEIS, /coverRegie\.charaktere/);
});
