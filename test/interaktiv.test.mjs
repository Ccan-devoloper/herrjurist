import test from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";

/* Der Schlüssel muss stehen, bevor config.mjs geladen wird - die Konfiguration
   liest die Umgebung beim Import. Deshalb erst setzen, dann dynamisch laden. */
process.env.IG_PRIVAT_KEY = process.env.IG_PRIVAT_KEY || "test-schluessel-nur-fuer-den-lauf";
const { CONFIG } = await import("../src/config.mjs");
const {
  interaktivGeplant, umfrageBauen, medienStickerGeplant, medienStickerBauen, sperreAktiv, sperreSetzen,
  sitzungLaden, sitzungSichern, interaktivPosten, InteraktivFehler,
} = await import("../src/interaktiv.mjs");

const AN = { aktiv: true, nutzer: "kontoname", passwort: "geheim", arten: ["frage"], stickerFrage: "Was stimmt?", teaserMedienSticker: true, sperreStunden: 24 };
const FRAGE = { art: "frage", optionen: ["A lang", "B lang", "C lang"] };
const tmpdir = () => fs.mkdtempSync(path.join(os.tmpdir(), "ia-"));

test("Umfrage nur, wenn alles zusammenkommt", () => {
  assert.equal(interaktivGeplant(FRAGE, AN), true);
  assert.equal(interaktivGeplant(FRAGE, { ...AN, aktiv: false }), false, "Schalter aus");
  assert.equal(interaktivGeplant(FRAGE, { ...AN, passwort: "" }), false, "ohne Zugangsdaten");
  assert.equal(interaktivGeplant({ ...FRAGE, art: "merksatz" }, AN), false, "andere Story-Art");
  assert.equal(interaktivGeplant({ ...FRAGE, optionen: ["nur eine"] }, AN), false, "zu wenige Optionen");
  assert.equal(interaktivGeplant({ art: "frage" }, AN), false, "ohne Optionen");
});

test("Der Sticker sitzt dort, wo das Layout Platz gelassen hat", () => {
  /* Gerechnet wird mit dem gemessenen Kasten, nicht mit geschätzten
     Koordinaten - sonst läge der Sticker bei längerem Titel auf dem Text. */
  const u = umfrageBauen(FRAGE, { x: 84, y: 1412, width: 912, height: 300 }, { frage: "Was stimmt?" });
  assert.deepEqual(u.optionen, ["A", "B", "C"], "im Bild stehen die langen Antworten, der Sticker fragt nur ab");
  assert.equal(u.x, 0.5);
  assert.ok(Math.abs(u.y - (1412 + 150) / 1920) < 1e-9);
  assert.ok(u.x > 0 && u.x < 1 && u.y > 0 && u.y < 1);
  assert.ok(u.width <= 1 && u.height <= 1);
});

test("Ohne gemessenen Platz wird keine Umfrage geraten", () => {
  assert.throws(() => umfrageBauen(FRAGE, null), InteraktivFehler);
  assert.throws(() => umfrageBauen(FRAGE, { x: 0, y: 0, width: 0, height: 0 }), InteraktivFehler);
});

test("Höchstens vier Optionen – mehr nimmt der Sticker nicht", () => {
  const viele = { art: "frage", optionen: ["a", "b", "c", "d", "e", "f"] };
  assert.deepEqual(umfrageBauen(viele, { x: 0, y: 0, width: 100, height: 100 }).optionen, ["A", "B", "C", "D"]);
});

test("Feed-Teaser bekommt nur mit echter Medien-ID einen antippbaren Sticker", () => {
  const teaser = { art: "teaser" };
  assert.equal(medienStickerGeplant(teaser, "17900000000000000", AN), true);
  assert.equal(medienStickerGeplant(teaser, "trocken", AN), false);
  assert.equal(medienStickerGeplant({ art: "frage" }, "17900000000000000", AN), false);
  assert.equal(medienStickerGeplant(teaser, "17900000000000000", { ...AN, teaserMedienSticker: false }), false);
  assert.deepEqual(
    medienStickerBauen("17900000000000000"),
    { media_pk: "17900000000000000", x: 0.5, y: 0.79, width: 0.48, height: 0.22 },
  );
  assert.throws(() => medienStickerBauen("trocken"), InteraktivFehler);
});

test("Sperre: gesetzt, wirksam, und danach wieder frei", () => {
  const ledger = {};
  assert.equal(sperreAktiv(ledger), false);
  sperreSetzen(ledger, "Challenge verlangt", { stunden: 24, jetzt: Date.parse("2026-09-17T12:00:00Z") });
  assert.equal(ledger.interaktivSperreBis, "2026-09-18T12:00:00.000Z");
  assert.equal(sperreAktiv(ledger, Date.parse("2026-09-18T11:59:00Z")), true);
  assert.equal(sperreAktiv(ledger, Date.parse("2026-09-18T12:01:00Z")), false);
});

test("Sitzung liegt verschlüsselt, nicht im Klartext", () => {
  const dir = tmpdir();
  assert.equal(sitzungLaden(dir, "", ""), null, "ohne Datei und ohne Saat keine Sitzung");
  const sitzung = { uuids: { phone_id: "abc-123" }, authorization_data: { ds_user_id: "42", sessionid: "geheime-sitzung" } };
  assert.equal(sitzungSichern(dir, sitzung), true);
  const roh = fs.readFileSync(path.join(dir, "instagrapi.enc"), "utf8");
  assert.ok(!roh.includes("geheime-sitzung"), "der Asset-Zweig ist öffentlich – die Sitzung darf dort nicht lesbar sein");
  assert.deepEqual(sitzungLaden(dir), sitzung);
});

test("Die Sitzung des Testkontos wird nicht für den echten Kanal benutzt", () => {
  /* Der Grund, warum die Sitzung zum Kontonamen gespeichert wird: Eine fremde
     Sitzung mit neuen Zugangsdaten zu probieren, sieht für Instagram nach
     einer Übernahme aus - genau das, was eine Challenge auslöst. */
  const dir = tmpdir();
  sitzungSichern(dir, { authorization_data: { sessionid: "vom-testkonto" } }, "testkonto");
  assert.equal(sitzungLaden(dir, "herrjurist", ""), null, "fremde Sitzung darf nicht gelten");
  assert.deepEqual(sitzungLaden(dir, "TESTKONTO", ""), { authorization_data: { sessionid: "vom-testkonto" } }, "Groß- und Kleinschreibung ist egal");
});

test("Ohne Datei zieht die Saat aus dem Secret", async () => {
  /* Der Weg, der am 17.09. nötig wurde: Die CI darf sich nicht anmelden
     (Rechenzentrums-IP), also kommt die Sitzung einmalig vom eigenen Rechner
     und liegt als Secret. Ohne diesen Rückfall stünde die CI ohne Sitzung da. */
  const { tresorSchreiben } = await import("../src/interaktiv.mjs");
  const dir = tmpdir();
  const saat = tresorSchreiben({ nutzer: "testkonto", sitzung: { authorization_data: { sessionid: "aus-dem-secret" } } });
  assert.deepEqual(sitzungLaden(dir, "testkonto", saat), { authorization_data: { sessionid: "aus-dem-secret" } });
  assert.equal(sitzungLaden(dir, "jemand-anderes", saat), null, "auch die Saat gilt nur für ihr Konto");

  /* Die Datei im Asset-Zweig hat Vorrang – sie ist die frischere. */
  sitzungSichern(dir, { authorization_data: { sessionid: "aus-dem-zweig" } }, "testkonto");
  assert.deepEqual(sitzungLaden(dir, "testkonto", saat), { authorization_data: { sessionid: "aus-dem-zweig" } });
});

test("Beschädigte Sitzungsdatei wirft nicht, sie gilt als keine", () => {
  const dir = tmpdir();
  fs.writeFileSync(path.join(dir, "instagrapi.enc"), "kein gültiger Tresor");
  assert.equal(sitzungLaden(dir, "", ""), null);
});

/* --- Der Weg, der das Konto schützt --------------------------------------
   Eine Challenge darf NICHT zu einem zweiten Versuch führen. Diese beiden
   Tests fahren die Brücke gegen ein nachgebautes Skript, damit der Pfad
   geprüft ist, ohne Instagram anzufassen. */
function fakeBruecke(antwort, { code = 0 } = {}) {
  const datei = path.join(tmpdir(), "fake.mjs");
  fs.writeFileSync(datei, `
let roh = "";
process.stdin.on("data", (d) => { roh += d; });
process.stdin.on("end", () => {
  const auftrag = JSON.parse(roh);
  if (!auftrag.bild || !auftrag.nutzer) { process.stdout.write('{"ok":false,"art":"aufruf","fehler":"unvollständig"}\\n'); process.exit(1); }
  process.stdout.write(${JSON.stringify(JSON.stringify(antwort))} + "\\n");
  process.exit(${code});
});
`);
  return datei;
}

test("Challenge sperrt den Weg, statt es noch einmal zu versuchen", async () => {
  const dir = tmpdir();
  const ledger = {};
  const skript = fakeBruecke({ ok: false, art: "challenge", fehler: "Bestätigung verlangt" }, { code: 1 });
  const zeilen = [];
  CONFIG.interaktiv.nutzer = "kontoname";
  CONFIG.interaktiv.passwort = "geheim";

  await assert.rejects(
    () => interaktivPosten({ bildPfad: skript, umfrage: { frage: "x", optionen: ["A", "B"], x: .5, y: .8, width: .8, height: .1 }, stateDir: dir, ledger, log: (z) => zeilen.push(z), python: process.execPath, skript }),
    (e) => e instanceof InteraktivFehler && e.art === "challenge",
  );
  assert.equal(sperreAktiv(ledger), true, "nach einer Challenge ist der Weg gesperrt");
  assert.match(ledger.interaktivSperreGrund, /Bestätigung/);

  /* Und der zweite Versuch geht gar nicht erst los. */
  await assert.rejects(
    () => interaktivPosten({ bildPfad: skript, umfrage: {}, stateDir: dir, ledger, python: process.execPath, skript }),
    (e) => e.art === "gesperrt",
  );
});

test("Ein gelungener Lauf liefert die Medien-ID und sichert die Sitzung", async () => {
  const dir = tmpdir();
  const skript = fakeBruecke({ ok: true, medienId: "17900000000000000", sitzung: { authorization_data: { sessionid: "frisch" } } });
  CONFIG.interaktiv.nutzer = "kontoname";
  CONFIG.interaktiv.passwort = "geheim";
  const id = await interaktivPosten({ bildPfad: skript, umfrage: { frage: "x", optionen: ["A", "B"], x: .5, y: .8, width: .8, height: .1 }, stateDir: dir, ledger: {}, python: process.execPath, skript });
  assert.equal(id, "17900000000000000");
  assert.deepEqual(sitzungLaden(dir), { authorization_data: { sessionid: "frisch" } });
});

test("Ein stummer Absturz der Brücke ist ein Fehler, kein stiller Erfolg", async () => {
  const dir = tmpdir();
  const leer = path.join(tmpdir(), "stumm.mjs");
  fs.writeFileSync(leer, "process.exit(3);\n");
  await assert.rejects(
    () => interaktivPosten({ bildPfad: leer, umfrage: {}, stateDir: dir, ledger: {}, python: process.execPath, skript: leer }),
    (e) => e instanceof InteraktivFehler && e.art === "bruecke",
  );
});
