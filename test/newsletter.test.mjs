import test from "node:test";
import assert from "node:assert/strict";
import {
  tokenBauen, tokenLesen, emailGueltig, listeLesen, listeSchreiben,
  eintragen, austragen, aktiveAdressen, doiMail, willkommenMail,
} from "../src/newsletter.mjs";
import * as worker from "../newsletter/worker.mjs";

const GEHEIM = "test-geheimnis-nur-fuer-den-lauf";

test("Token: hin und zurück", () => {
  const t = tokenBauen({ email: "Max@Beispiel.DE", zweck: "doi" }, GEHEIM);
  assert.equal(tokenLesen(t, GEHEIM, { zweck: "doi" }), "max@beispiel.de");
});

test("Token: fremdes Geheimnis trägt nicht", () => {
  const t = tokenBauen({ email: "max@beispiel.de", zweck: "doi" }, GEHEIM);
  assert.equal(tokenLesen(t, "anderes-geheimnis", { zweck: "doi" }), null);
});

test("Token: veränderte Nutzlast fällt auf", () => {
  const t = tokenBauen({ email: "max@beispiel.de", zweck: "doi" }, GEHEIM);
  const [nutzlast, sig] = t.split(".");
  const fremd = Buffer.from(JSON.stringify({ e: "angreifer@boese.de", z: "doi", exp: Date.now() + 1e6 }))
    .toString("base64").replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
  assert.equal(tokenLesen(`${fremd}.${sig}`, GEHEIM, { zweck: "doi" }), null);
  assert.equal(tokenLesen(`${nutzlast}.${sig}`, GEHEIM, { zweck: "doi" }), "max@beispiel.de");
});

test("Token: Zweck ist nicht austauschbar", () => {
  /* Sonst wäre der Bestätigungslink aus der Mail zugleich ein Dauerzugang
     zur Datei - und ein Abmeldelink ließe sich als Anmeldung einlösen. */
  const t = tokenBauen({ email: "max@beispiel.de", zweck: "doi" }, GEHEIM);
  assert.equal(tokenLesen(t, GEHEIM, { zweck: "datei" }), null);
  assert.equal(tokenLesen(t, GEHEIM, { zweck: "abmelden" }), null);
});

test("Token: abgelaufen gilt nicht", () => {
  const t = tokenBauen({ email: "max@beispiel.de", zweck: "doi", gueltigMs: 1000 }, GEHEIM);
  assert.equal(tokenLesen(t, GEHEIM, { zweck: "doi", jetzt: Date.now() + 2000 }), null);
});

test("Token: Worker und Actions-Lauf verstehen einander", async () => {
  /* Die Signatur entsteht im Cloudflare-Worker (WebCrypto) und wird im
     Actions-Lauf geprüft (node:crypto). Gehen die Ableitungen auseinander,
     kommt keine einzige Bestätigung an - und zwar lautlos. */
  const vomWorker = await worker.tokenBauen("max@beispiel.de", "doi", 3600e3, GEHEIM);
  assert.equal(tokenLesen(vomWorker, GEHEIM, { zweck: "doi" }), "max@beispiel.de");

  const vomLauf = tokenBauen({ email: "max@beispiel.de", zweck: "datei" }, GEHEIM);
  assert.equal(await worker.tokenLesen(vomLauf, "datei", GEHEIM), "max@beispiel.de");
});

test("Adressprüfung: Kopfzeilen-Einschleusung und Unsinn fallen durch", () => {
  for (const gut of ["max@beispiel.de", "a.b+c@sub.example.co.uk"]) assert.ok(emailGueltig(gut), gut);
  for (const schlecht of [
    "", "max", "max@", "@beispiel.de", "max@beispiel",
    "max@beispiel.de\nBcc: opfer@example.com",      // Einschleusung in den Mailkopf
    "max@beispiel.de, zweite@example.com",
    "<max@beispiel.de>", `a${"b".repeat(300)}@x.de`,
  ]) assert.ok(!emailGueltig(schlecht), JSON.stringify(schlecht));
});

test("Adressprüfung: Worker und Lauf urteilen gleich", () => {
  for (const s of ["max@beispiel.de", "max@beispiel", "max@beispiel.de\nBcc: x@y.de", "<a@b.de>"]) {
    assert.equal(worker.emailGueltig(s), emailGueltig(s), s);
  }
});

test("Liste: verschlüsselt hin und zurück", () => {
  const { liste } = eintragen({ version: 1, eintraege: [] }, "max@beispiel.de");
  const text = listeSchreiben(liste, GEHEIM);
  assert.ok(!text.includes("beispiel"), "die Adresse darf im Dateiinhalt nicht lesbar sein");
  assert.deepEqual(listeLesen(text, GEHEIM).eintraege.map((e) => e.adresse), ["max@beispiel.de"]);
});

test("Liste: fremder Schlüssel entschlüsselt nicht", () => {
  const text = listeSchreiben({ version: 1, eintraege: [{ adresse: "max@beispiel.de" }] }, GEHEIM);
  assert.throws(() => listeLesen(text, "anderes-geheimnis"));
});

test("Liste: leerer Inhalt ergibt eine leere Liste", () => {
  assert.deepEqual(listeLesen("", GEHEIM), { version: 1, eintraege: [] });
});

test("Eintragen: zweimal derselbe Klick ändert nichts", () => {
  let liste = { version: 1, eintraege: [] };
  ({ liste } = eintragen(liste, "max@beispiel.de"));
  const zweiter = eintragen(liste, "MAX@beispiel.de");
  assert.equal(zweiter.neu, false);
  assert.equal(zweiter.liste.eintraege.length, 1);
});

test("Abmelden: Eintrag bleibt, wird aber nicht mehr angeschrieben", () => {
  let liste = { version: 1, eintraege: [] };
  ({ liste } = eintragen(liste, "max@beispiel.de"));
  ({ liste } = austragen(liste, "max@beispiel.de"));
  assert.equal(liste.eintraege.length, 1);
  assert.deepEqual(aktiveAdressen(liste), []);
});

test("Abmelden und neu bestätigen führt zurück auf die Liste", () => {
  let liste = { version: 1, eintraege: [] };
  ({ liste } = eintragen(liste, "max@beispiel.de"));
  ({ liste } = austragen(liste, "max@beispiel.de"));
  const wieder = eintragen(liste, "max@beispiel.de");
  assert.equal(wieder.neu, true);
  assert.deepEqual(aktiveAdressen(wieder.liste), ["max@beispiel.de"]);
});

test("Mailtexte tragen die Pflichtlinks", () => {
  const doi = doiMail({ bestaetigenUrl: "https://example.test/ja?t=abc" });
  assert.match(doi.text, /https:\/\/example\.test\/ja\?t=abc/);
  assert.match(doi.text, /nicht angefordert/i);

  const will = willkommenMail({ uebersichtUrl: "https://example.test/uebersicht?t=x", abmeldenUrl: "https://example.test/abmelden?t=y" });
  assert.match(will.text, /https:\/\/example\.test\/uebersicht\?t=x/);
  assert.match(will.text, /https:\/\/example\.test\/abmelden\?t=y/);
});
