import test from "node:test";
import assert from "node:assert/strict";
import { nachrichtHash, postfachAnonymisieren, offeneNachrichten } from "../src/postfach.mjs";

test("Postfach-Ledger entfernt personenbezogene Felder", () => {
  const alt = [{ nachrichtId: "msg-123", konversationId: "conv-9", datum: "2026-09-17", von: "beispielnutzer", antwortId: "reply-7", text: "Antwort im Klartext" }];
  const [neu] = postfachAnonymisieren(alt);
  assert.deepEqual(Object.keys(neu).sort(), ["datum", "nachrichtHash", "status"]);
  assert.equal(neu.nachrichtHash, nachrichtHash("msg-123"));
  assert.equal(neu.status, "beantwortet");
  const json = JSON.stringify(neu);
  for (const geheim of ["beispielnutzer", "Antwort im Klartext", "conv-9", "reply-7", "msg-123"]) assert.equal(json.includes(geheim), false);
});

test("Hash erhält den Wiederholungsschutz", () => {
  const jetzt = Date.parse("2026-09-20T12:00:00Z");
  const ledger = { postfach: [{ nachrichtHash: nachrichtHash("msg-123"), datum: "2026-09-20", status: "beantwortet" }], veroeffentlicht: [] };
  const konversationen = [{ id: "conv", messages: { data: [{ id: "msg-123", from: { id: "person-1", username: "privat" }, message: "Noch eine Frage", created_time: "2026-09-20T11:30:00Z" }] } }];
  const offen = offeneNachrichten(konversationen, "eigen", ledger, jetzt, [], {});
  assert.equal(offen.length, 0);
  assert.equal(offen.uebersprungen?.[0]?.grund, "bereits behandelt");
});
