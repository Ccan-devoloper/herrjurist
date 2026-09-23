import test from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";

import {
  rohbildLaden,
  rohbildSpeichern,
  vorproduktionsBildInputHash,
} from "../src/vorproduktionsbild.mjs";

const png = Buffer.concat([
  Buffer.from("89504e470d0a1a0a", "hex"),
  Buffer.from("herr-jurist-testbild", "utf8"),
]);

function inhalt(titel = "Drittwirkung: Warum vor § 80a das eigene Recht zählt") {
  return {
    slug: "2026-09-24-b1",
    themaId: "verwalt-388",
    fach: "verwalt",
    format: "spickzettel",
    coverText: "Erst eigenes Recht",
    coverRegie: { charaktere: ["form7", "mara"], kernidee: "Drittwirkung" },
    folien: [{ art: "titel", titel }],
    caption: "Caption A",
  };
}

test("Rohbild wird mit SHA und Referenz persistiert und kostenlos wiederverwendet", () => {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), "hj-rohbild-"));
  try {
    const gespeichert = rohbildSpeichern({
      basisDir: dir,
      basisUrl: "https://raw.githubusercontent.com/x/y/instagram-assets",
      datum: "2026-09-24",
      slot: "b1",
      inhalt: inhalt(),
      treffer: {
        bild: `data:image/png;base64,${png.toString("base64")}`,
        breite: 900, hoehe: 900,
        charaktere: ["FORM-7", "Mara Sternpfad"],
        kostenUsd: 0.0734,
      },
      modell: "gpt-image-test",
      guete: "high",
    });

    assert.match(gespeichert.meta.sha256, /^[a-f0-9]{64}$/);
    assert.match(gespeichert.meta.gitPfad, /b1-[a-f0-9]{16}\.png$/);
    assert.ok(fs.existsSync(gespeichert.bildPfad));

    const wieder = rohbildLaden({
      basisDir: dir,
      datum: "2026-09-24",
      slot: "b1",
      inhalt: inhalt(),
      modell: "gpt-image-test",
      guete: "high",
    });
    assert.equal(wieder.wiederverwendet, true);
    assert.equal(wieder.kostenUsd, 0);
    assert.equal(wieder.urspruenglicheKostenUsd, 0.0734);
    assert.equal(wieder.rohbild.sha256, gespeichert.meta.sha256);
  } finally {
    fs.rmSync(dir, { recursive: true, force: true });
  }
});

test("Caption-Aenderung behaelt Rohbild, visuelle Hook-Aenderung nicht", () => {
  const a = inhalt();
  const b = structuredClone(a);
  b.caption = "Caption B";
  assert.equal(
    vorproduktionsBildInputHash(a, { modell: "m", guete: "high" }),
    vorproduktionsBildInputHash(b, { modell: "m", guete: "high" }),
  );
  assert.notEqual(
    vorproduktionsBildInputHash(a, { modell: "m", guete: "high" }),
    vorproduktionsBildInputHash(inhalt("Neue visuelle Hook"), { modell: "m", guete: "high" }),
  );
});

test("Beschaedigtes Rohbild bricht fail-closed ab statt neu zu erzeugen", () => {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), "hj-rohbild-"));
  try {
    const gespeichert = rohbildSpeichern({
      basisDir: dir,
      basisUrl: "https://raw.githubusercontent.com/x/y/instagram-assets",
      datum: "2026-09-25",
      slot: "b2",
      inhalt: inhalt("Lebensgefährlich = Tötungsvorsatz?"),
      treffer: { bild: `data:image/png;base64,${png.toString("base64")}`, kostenUsd: 0.07 },
      modell: "gpt-image-test",
      guete: "high",
    });
    fs.appendFileSync(gespeichert.bildPfad, "kaputt");

    assert.throws(() => rohbildLaden({
      basisDir: dir,
      datum: "2026-09-25",
      slot: "b2",
      inhalt: inhalt("Lebensgefährlich = Tötungsvorsatz?"),
      modell: "gpt-image-test",
      guete: "high",
    }), /falschen SHA-256/);
  } finally {
    fs.rmSync(dir, { recursive: true, force: true });
  }
});
