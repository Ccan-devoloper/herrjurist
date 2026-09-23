import test from "node:test";
import assert from "node:assert/strict";
import { einzelkostenSynchronisieren, kostenGrund } from "../src/kostenledger.mjs";
import { journalStarten } from "../src/journal.mjs";

test("Einzelkosten erklaeren Betrag, Zweck, Provider und Slot dauerhaft", () => {
  const basis = { wochen: {}, tage: {} };
  const journal = {
    datum: "2026-09-24",
    kanal: "herrjurist",
    eintraege: [{
      reservationId: "2026-09-24-0001-faktencheck",
      date: "2026-09-24",
      channel: "herrjurist",
      bucket: "core",
      purpose: "faktencheck",
      slot: "b1",
      attempt: 1,
      provider: "anthropic",
      model: "claude-sonnet-5",
      promptVersion: "3",
      reservedUsd: 0.04,
      actualUsd: 0.018765,
      state: "settled",
      outcome: "ok",
      usage: { inputTokens: 1900, outputTokens: 420, cacheReadTokens: 0 },
      createdAt: "2026-09-24T06:00:00.000Z",
      updatedAt: "2026-09-24T06:00:04.000Z",
    }],
  };

  const k = einzelkostenSynchronisieren(basis, journal);
  const e = k.einzelkosten["2026-09-24"][0];
  assert.equal(e.kostenUsd, 0.018765);
  assert.equal(e.zweck, "faktencheck");
  assert.equal(e.warum, "Juristischer Faktencheck eines Feedbeitrags (Slot b1)");
  assert.equal(e.provider, "anthropic");
  assert.equal(e.modell, "claude-sonnet-5");
  assert.equal(e.usage.outputTokens, 420);
  assert.equal(k.einzelkostenSummen["2026-09-24"].bekannteKostenUsd, 0.018765);
});

test("Einzelkosten-Sync ist idempotent und aktualisiert unresolved zu settled", () => {
  const sent = {
    datum: "2026-09-24", kanal: "herrjurist",
    eintraege: [{
      reservationId: "r1", date: "2026-09-24", bucket: "core", purpose: "bild",
      reservedUsd: 0.12, actualUsd: null, state: "sent",
      createdAt: "2026-09-24T07:00:00.000Z", updatedAt: "2026-09-24T07:00:01.000Z",
    }],
  };
  const a = einzelkostenSynchronisieren({}, sent);
  assert.equal(a.einzelkosten["2026-09-24"].length, 1);
  assert.equal(a.einzelkostenSummen["2026-09-24"].ungeklaerteMaxBelastungUsd, 0.12);

  const settled = structuredClone(sent);
  settled.eintraege[0].state = "settled";
  settled.eintraege[0].actualUsd = 0.031;
  settled.eintraege[0].provider = "openai";
  settled.eintraege[0].model = "gpt-image-1-mini";

  const b = einzelkostenSynchronisieren(a, settled);
  assert.equal(b.einzelkosten["2026-09-24"].length, 1);
  assert.equal(b.einzelkosten["2026-09-24"][0].kostenUsd, 0.031);
  assert.equal(b.einzelkostenSummen["2026-09-24"].ungeklaertePosten, 0);
  assert.equal(b.einzelkostenSummen["2026-09-24"].bekannteKostenUsd, 0.031);
});

test("Journal schreibt Abrechnung mit Erklaer-Metadaten erneut durable", async () => {
  let bestand = null;
  const geschrieben = [];
  const journal = journalStarten({
    datum: "2026-09-24",
    kanal: "herrjurist",
    lesen: () => bestand,
    schreiben: async (inhalt) => {
      bestand = structuredClone(inhalt);
      geschrieben.push(structuredClone(inhalt));
      return true;
    },
  });

  const id = await journal.reservieren({
    bucket: "core", purpose: "reel-faktencheck", slot: "b3", attempt: 2,
    reservedUsd: 0.09, provider: "openai", model: "gpt-5", promptVersion: "7",
  });
  await journal.senden(id);
  const ok = await journal.abrechnen(id, 0.027, {
    provider: "openai", model: "gpt-5", promptVersion: "7", outcome: "ok",
    usage: { inputTokens: 2100, outputTokens: 600 },
  });

  assert.equal(ok, true);
  assert.equal(geschrieben.length, 3);
  const e = bestand.eintraege[0];
  assert.equal(e.state, "settled");
  assert.equal(e.actualUsd, 0.027);
  assert.equal(e.provider, "openai");
  assert.equal(e.model, "gpt-5");
  assert.equal(e.usage.outputTokens, 600);
});

test("Kostenbegruendung bleibt fuer unbekannte Zwecke explizit", () => {
  assert.match(kostenGrund("sonderlauf", "x1"), /sonderlauf/);
  assert.match(kostenGrund("sonderlauf", "x1"), /Slot x1/);
});
