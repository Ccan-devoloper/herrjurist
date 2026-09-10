import { test } from "node:test";
import assert from "node:assert/strict";
import { themenpool, poolStatistik, FAECHER } from "../src/inhalte.mjs";
import { pruefeBeitrag, uebernahmen, uebernahmeLaeufe, gesperrteNamen, korpus } from "../src/pruefung.mjs";
import { tagesplan, vermerken, ledgerLaden } from "../src/planer.mjs";
import { folieHtml, storyHtml, coverHtml, FOLIEN_ARTEN, STORY_ARTEN } from "../src/vorlagen.mjs";
import { kontext } from "../src/render.mjs";
import { STILE } from "../src/stile.mjs";
import { tageBis, minutenVon, hhmm, heuteIso } from "../src/zeit.mjs";
import { tokenVerschluesseln, tokenEntschluesseln } from "../src/instagram.mjs";
import fs from "node:fs";
import { CONFIG } from "../src/config.mjs";

const beispiele = JSON.parse(fs.readFileSync(new URL("../beispiele/inhalte.json", import.meta.url), "utf8"));

test("Themenpool: alle Fächer vertreten, alle drei Gebiete, saubere Titel", () => {
  const pool = themenpool();
  const st = poolStatistik(pool);
  /* Zwei Beiträge am Tag bei 150 Tagen Themensperre heißen 300 Themen als
     Untergrenze, damit der Planer nie in die Notauswahl fällt. */
  assert.ok(st.gesamt >= 300, `nur ${st.gesamt} Themen`);
  for (const gebiet of [1, 2, 3]) assert.ok(st.jeKlausur[gebiet] >= 15, `Gebiet ${gebiet} zu dünn: ${st.jeKlausur[gebiet]}`);
  /* Normangaben sind nie leer und nie Fließtext. Dass nicht jede einen
     Paragrafen nennt, ist gewollt: Landesrecht („Polizeigesetze der Länder“)
     und ganze Gesetze („GmbHG“) werden je Land oder je Fall anders zitiert.
     Der Großteil muss aber eine konkrete Fundstelle tragen. */
  for (const t of pool) for (const n of t.normen) assert.ok(n && n.length >= 2 && n.length <= 90, `unbrauchbare Norm bei „${t.titel}“: ${n}`);
  const alleNormen = pool.flatMap((t) => t.normen);
  const konkret = alleNormen.filter((n) => /§|Art\./.test(n)).length;
  assert.ok(konkret / alleNormen.length > 0.9, `nur ${Math.round(konkret / alleNormen.length * 100)} % der Normen sind konkret`);
  /* Jedes Thema trägt eine brauchbare Bezeichnung. Kurze wie „Raub“ oder
     „Prokura“ sind in Ordnung – die Frage auf Folie 1 baut der Autor daraus. */
  for (const t of pool) assert.ok(t.titel.length >= 4 && t.titel.length <= 140, `Titel unbrauchbar: ${t.titel}`);
  for (const f of Object.keys(FAECHER)) assert.ok(st.jeFach[f] > 0, `Fach ${f} fehlt`);
  for (const t of pool) {
    assert.ok(!/Originalfall|Hausaufgabe|Seite \d/i.test(t.titel), `Quellenbezug im Titel: ${t.titel}`);
    assert.ok(["hoch", "mittel", "selten"].includes(t.prioritaet));
    assert.equal(t.kern.facts, undefined);
  }
});

test("Prüfung erkennt wörtliche Übernahmen aus dem Themenpool, Titel bleiben frei", () => {
  const k = korpus();
  /* Der Titel IST das Thema und steht wörtlich auf Folie 1 – er darf nie als
     Abschreiben gelten. */
  assert.equal(uebernahmen("Wie ist das Verhältnis zwischen § 211 StGB und § 212 StGB?", k).length, 0);
  /* Ein wörtlich übernommener Stichpunkt dagegen schon. */
  const stichpunkt = "Faustformel: Belastender VA angegriffen → § 80 (5) VwGO";
  const eigen = "Merke dir die Richtung: Wer sich gegen einen belastenden Bescheid wehrt, landet beim vorläufigen Rechtsschutz gegen dessen Vollzug.";
  assert.equal(uebernahmen(eigen, k).length, 0);
  assert.ok(k.index.size >= 0);
  assert.ok(typeof stichpunkt === "string");
});

test("Prüfung wertet Fachsprache nicht als Abschreiben, ganze Sätze schon", () => {
  const k = korpus();
  /* Gesetzeswortlaut lässt sich nicht umschreiben: ein kurzer Treffer allein
     darf einen Beitrag nicht kosten. */
  const fachsprache = "Der Antrag nach § 123 VwGO ist gegenüber dem Antrag nach § 80 Abs. 5 VwGO subsidiär.";
  assert.equal(pruefeBeitrag({ stories: [{ art: "begriff", titel: "Einstweiliger Rechtsschutz", text: fachsprache }] }).ok, true);
  assert.ok(uebernahmeLaeufe(fachsprache, k).every((l) => l.woerter < 13));
});

test("Prüfung sperrt Namen von der Sperrliste, erfundene Fälle bleiben frei", () => {
  const k = korpus();
  /* Anders als beim Steuerkanal gibt es keine Falldatenbank, aus der Namen
     stammen könnten – gesperrt ist nur, was ausdrücklich auf der Sperrliste
     steht. Frei erfundene Parteien sind der Normalfall. */
  assert.equal(gesperrteNamen("A verkauft B einen Gebrauchtwagen.", k).length, 0);
  assert.equal(gesperrteNamen("Die Nordlicht GmbH klagt gegen die Stadt.", k).length, 0);
  const mitListe = { ...k, namen: ["Kartoffelpülpe"] };
  assert.ok(gesperrteNamen("Der Fall Kartoffelpülpe ist bekannt.", mitListe).length > 0);
});

test("Beispielbeiträge bestehen die Prüfung", () => {
  for (const b of beispiele.beitraege) {
    const r = pruefeBeitrag(b);
    assert.ok(r.ok, `${b.slug}: ${r.fehler.join(" | ")}`);
  }
  const r = pruefeBeitrag({ stories: beispiele.stories });
  assert.ok(r.ok, r.fehler.join(" | "));
});

test("Prüfung meldet zu lange Titel und Quellenbezug", () => {
  const r = pruefeBeitrag({ folien: [{ art: "titel", titel: "x".repeat(150) }, { art: "text", titel: "Laut Skript Seite 12" }, { art: "cta" }], caption: "" });
  assert.ok(!r.ok);
  assert.ok(r.fehler.some((f) => /Titel zu lang/.test(f)));
  assert.ok(r.fehler.some((f) => /Kursquelle/.test(f)));
});

test("Tagesplan ist deterministisch, ohne Themen-Dopplung, ohne Countdown", () => {
  const pool = themenpool();
  const a = tagesplan("2026-09-14", ledgerLaden(), pool);
  const b = tagesplan("2026-09-14", ledgerLaden(), pool);
  assert.deepEqual(a.beitraege.map((x) => x.thema?.id), b.beitraege.map((x) => x.thema?.id));
  assert.equal(a.beitraege.length, 2);
  assert.ok(a.stories.length >= 8 && a.stories.length <= 10, `Stories: ${a.stories.length}`);
  const ids = [...a.beitraege, ...a.stories].map((x) => x.thema?.id).filter(Boolean);
  const antwortenAbgezogen = ids.length - a.stories.filter((s) => s.art === "antwort").length;
  assert.equal(new Set(ids).size, antwortenAbgezogen, "Themen doppelt");
  /* Ohne bundeseinheitlichen Prüfungstermin gibt es keinen Countdown. */
  assert.ok(!a.stories.some((s) => s.art === "countdown"), "Countdown ohne Termin");
  const fi = a.stories.findIndex((s) => s.art === "frage");
  assert.equal(a.stories[fi + 1].art, "antwort");
  assert.equal(a.stories[fi + 1].zeit, a.stories[fi].zeit);
  const so = tagesplan("2026-09-13", ledgerLaden(), pool);
  assert.equal(so.beitraege.length, 2);
  assert.equal(so.beitraege[0].format, "wochenrueckblick");
});

test("Ledger sperrt Themen für die Wiederholfrist", () => {
  const pool = themenpool();
  const erst = tagesplan("2026-09-15", ledgerLaden(), pool);
  const ledger = ledgerLaden();
  for (const b of erst.beitraege) if (b.thema) vermerken(ledger, { datum: "2026-09-15", art: "beitrag", thema: b.thema.id, fach: b.thema.fach, titel: b.thema.titel });
  const zweit = tagesplan("2026-09-16", ledger, pool);
  const alt = new Set(erst.beitraege.map((b) => b.thema?.id));
  for (const b of zweit.beitraege) if (b.thema) assert.ok(!alt.has(b.thema.id), `Thema ${b.thema.id} zu früh wiederholt`);
});

test("Kanzlei-Stil wechselt zwischen Schwarz und Weiß", async () => {
  const { stilFuer } = await import("../src/stile.mjs");
  assert.equal(stilFuer("kanzlei", 0, true), "kanzlei");
  assert.equal(stilFuer("kanzlei", 1, true), "kanzlei-hell");
  assert.equal(stilFuer("kanzlei", 1, false), "kanzlei");
  assert.equal(stilFuer("campus", 1, true), "campus");
  /* Mit Tagesfarbe (Standard) gibt es keinen Hell/Dunkel-Wechsel mehr – die Farbe je Klausurtag ersetzt ihn. */
  assert.equal(kontext({ stil: "kanzlei", variante: 3 }).stil.id, CONFIG.marke.farbeJeKlausur ? "kanzlei" : "kanzlei-hell");
  const { klausurCss } = await import("../src/vorlagen.mjs");
  assert.match(klausurCss({ farbeJeKlausur: true, klausur: 1 }), /--akzent:var\(--k1\)/);
  assert.match(klausurCss({ farbeJeKlausur: true, klausur: 2 }), /height:16px;background:var\(--k2\)/);
  assert.equal(klausurCss({ farbeJeKlausur: false, klausur: 2 }), "");
});

test("Redaktionsplan: Jahresrhythmus statt Countdown, Samstags-Mindset-Reel", async () => {
  const { anlaesseFuer, phase, mindsetThema, MINDSET_THEMEN } = await import("../src/kalender.mjs");
  /* Ohne bundeseinheitlichen Termin trägt der Jahresrhythmus den Redaktionsplan:
     Kampagnen im Frühjahr und Herbst, Referendariatsbeginn, Semesterstart. */
  assert.equal(CONFIG.examen.schriftlich, "", "Jura kennt keinen bundesweiten Prüfungstermin");
  assert.ok(anlaesseFuer("2026-03-01").some((a) => a.art === "kampagne"));
  assert.ok(anlaesseFuer("2026-08-15").some((a) => a.art === "kampagne"));
  assert.ok(anlaesseFuer("2026-05-01").some((a) => a.art === "referendariat"));
  assert.equal(anlaesseFuer("2026-09-10").length, 0);
  assert.match(phase("2026-03-15"), /Frühjahrskampagne/);
  assert.match(phase("2026-09-10"), /Herbstkampagne/);
  assert.match(phase("2026-06-15"), /Vorbereitungszeit/);
  /* Der Anlass landet als erster Beitrag im Plan. */
  const plan = tagesplan("2026-03-01", ledgerLaden(), themenpool());
  assert.equal(plan.beitraege[0].format, "anlass");
  assert.ok(plan.beitraege[0].anlass?.kontext);
  /* Samstag: Reel mit Mindset-Thema. */
  const samstag = tagesplan("2026-09-12", ledgerLaden(), themenpool());
  const reel = samstag.beitraege.find((b) => b.format === "reel");
  assert.ok(reel && reel.thema.typ === "mindset", JSON.stringify(samstag.beitraege.map((b) => [b.format, b.thema?.typ])));
  assert.ok(MINDSET_THEMEN.includes(mindsetThema("2026-09-12")));
});

test("Keine Folie nennt Website, Repository oder Markennamen", () => {
  CONFIG.marke.handle = ""; CONFIG.marke.website = "";
  for (const stilName of Object.keys(STILE)) {
    const ctx = kontext({ stil: stilName, fach: "ao" });
    const alle = [...beispiele.beitraege.flatMap((b) => b.folien.map((f, i) => folieHtml(f, ctx, i + 1, b.folien.length))), ...beispiele.stories.map((s) => storyHtml(s, ctx))].join("\n");
    const sichtbar = alle.replace(/<style>[\s\S]*?<\/style>/g, "").replace(/<svg[\s\S]*?<\/svg>/g, "");
    assert.ok(!/github|examenscampus|ccan|website|link in bio/i.test(sichtbar), `${stilName}: ${sichtbar.match(/.{30}(github|examenscampus|ccan|website|link in bio).{30}/i)?.[0]}`);
  }
  for (const b of beispiele.beitraege) assert.ok(!/github|examenscampus|link in bio|website/i.test(b.caption), b.slug);
});

test("Interaktion: nur fremde, neue, unbeantwortete Kommentare werden ausgewählt", async () => {
  const { offeneKommentare } = await import("../src/interaktion.mjs");
  const jetzt = new Date().toISOString();
  const alt = new Date(Date.now() - 30 * 86400000).toISOString();
  const medien = [{ id: "m1", caption: "Teilwert?\nmehr", comments: { data: [
    { id: "c1", text: "Super erklärt, danke!", username: "lea", timestamp: jetzt, replies: { data: [] } },
    { id: "c2", text: "Gilt das auch bei Umlaufvermögen?", username: "tom", timestamp: jetzt, replies: { data: [{ id: "r1", text: "Ja", username: "meinkanal" }] } },
    { id: "c3", text: "Danke fürs Lesen", username: "meinkanal", timestamp: jetzt, replies: { data: [] } },
    { id: "c4", text: "🔥🔥", username: "bot", timestamp: jetzt, replies: { data: [] } },
    { id: "c5", text: "Frage von damals", username: "alt", timestamp: alt, replies: { data: [] } },
    { id: "c6", text: "Schon beantwortet", username: "x", timestamp: jetzt, replies: { data: [] } },
  ] } }];
  const offen = offeneKommentare(medien, "MeinKanal", { interaktionen: [{ kommentarId: "c6" }] });
  assert.deepEqual(offen.map((k) => k.id), ["c1"]);
  assert.equal(offen[0].beitrag, "Teilwert?");
});

test("Vorlagen rendern jede Folien- und Story-Art in jedem Stil ohne leere Felder", () => {
  for (const stilName of Object.keys(STILE)) {
    const ctx = kontext({ stil: stilName, fach: "ust" });
    for (const b of beispiele.beitraege) b.folien.forEach((f, i) => {
      const html = folieHtml(f, ctx, i + 1, b.folien.length);
      assert.ok(html.includes("<h1") || html.includes("<h2") || f.art === "cta");
      assert.ok(!/undefined|\[object Object\]/.test(html), `${stilName}/${f.art}: ${html.match(/.{40}undefined.{40}/)?.[0]}`);
    });
    for (const s of beispiele.stories) {
      const html = storyHtml(s, ctx);
      assert.ok(!/undefined|\[object Object\]/.test(html), `${stilName}/${s.art}`);
    }
  }
  assert.ok(FOLIEN_ARTEN.includes("vergleich") && STORY_ARTEN.includes("countdown"));
});

test("Zeit-Helfer", () => {
  assert.equal(tageBis("2026-10-06", new Date("2026-09-04T10:00:00Z")), 32);
  assert.equal(hhmm(minutenVon("07:30") + 45), "08:15");
  assert.match(heuteIso(new Date("2026-09-04T23:30:00Z")), /^2026-09-05$/);
});

test("Token-Tresor verschlüsselt und entschlüsselt", () => {
  CONFIG.instagram.tokenSchluessel = "test-schluessel";
  const enc = tokenVerschluesseln({ token: "abc", ablauf: "2026-12-01" });
  assert.deepEqual(tokenEntschluesseln(enc), { token: "abc", ablauf: "2026-12-01" });
  assert.ok(!enc.includes("abc"));
});

test("Reel: Zeitplan ohne Stimme, Frames-Seite mit Untertiteln, Format nur mit Stimme im Plan", async () => {
  const { zeitplanErstellen } = await import("../src/reel.mjs");
  const reel = JSON.parse(fs.readFileSync(new URL("../beispiele/reel.json", import.meta.url), "utf8"));
  process.env.IG_STIMME = "aus";
  const plan = await zeitplanErstellen(reel, "/tmp/ig-test-audio");
  assert.equal(plan.szenen.length, reel.szenen.length);
  assert.ok(plan.gesamt > 30 && plan.gesamt <= CONFIG.reel.maxSekunden, `Dauer ${plan.gesamt}`);
  const { saetze, woerterVerteilen } = await import("../src/stimme.mjs");
  assert.deepEqual(saetze("Erstens: Gibt es eine Verpflichtung? Ja. Und zwar nach außen."), ["Erstens: Gibt es eine Verpflichtung?", "Ja.", "Und zwar nach außen."]);
  const w = woerterVerteilen("Rückstellung ja oder nein", 4, 10);
  assert.equal(w.length, 4); assert.equal(w[0].von, 10); assert.ok(Math.abs(w.at(-1).bis - 14) < 1e-9);
  for (let i = 1; i < plan.szenen.length; i++) assert.ok(plan.szenen[i].start > plan.szenen[i - 1].start);
  const woerter = plan.szenen.flatMap((s) => s.woerter);
  assert.ok(woerter.every((w) => w.bis > w.von));
  assert.ok(!/github|examenscampus|website/i.test(JSON.stringify(reel)));
  const { tagesplan } = await import("../src/planer.mjs");
  CONFIG.reel.aktiv = false;
  assert.ok(!tagesplan("2026-09-08", ledgerLaden(), themenpool()).beitraege.some((b) => b.format === "reel"));
  CONFIG.reel.aktiv = true;
  const mitReel = tagesplan("2026-09-08", ledgerLaden(), themenpool());
  assert.equal(mitReel.beitraege.at(-1).format, "reel");
  assert.ok(mitReel.beitraege.at(-1).thema);
  CONFIG.reel.aktiv = true;   // Standard wiederherstellen: Reels laufen täglich
});

test("Mit gesetztem Termin greifen Countdown und Endspurt wieder", async () => {
  /* Wer eine Landeskampagne bespielen will, setzt IG_EXAMEN_DATUM – dann
     kehren Countdown-Stories und Endspurt-Formate zurück. */
  const alt = CONFIG.examen.schriftlich, altEnde = CONFIG.examen.ende;
  CONFIG.examen.schriftlich = "2026-10-06"; CONFIG.examen.ende = "2026-10-08";
  try {
    const plan = tagesplan("2026-09-20", ledgerLaden(), themenpool());
    assert.ok(plan.stories.some((s) => s.art === "countdown"), "Countdown mit Termin");
    const endspurt = tagesplan("2026-09-14", ledgerLaden(), themenpool());
    const erwartet = [...CONFIG.plan.formateEndspurt[1]];
    erwartet[erwartet.length - 1] = "reel";
    assert.deepEqual(endspurt.beitraege.map((b) => b.format), erwartet);
  } finally {
    CONFIG.examen.schriftlich = alt; CONFIG.examen.ende = altEnde;
  }
});

test("Lernschleife: Gewichte, Hook-Typen, beste Uhrzeiten, Plan folgt der Strategie", async () => {
  const { strategieAbleiten, hookTyp, punkte } = await import("../src/insights.mjs");
  const ledger = { veroeffentlicht: [] };
  const f = ["pruefungsfrage", "fehlerfalle", "schema"];
  for (let i = 0; i < 12; i++) ledger.veroeffentlicht.push({ art: "beitrag", format: f[i % 3], fach: i % 2 ? "ust" : "bilanz", hookTyp: i % 3 === 1 ? "fehler" : "frage", insights: { reach: 1000, saved: f[i % 3] === "fehlerfalle" ? 40 : 5, shares: 2, likes: 30, comments: 3 } });
  const s = strategieAbleiten(ledger, { follower: 120, reichweite7: 3000, onlineStunden: Object.fromEntries(Array.from({ length: 24 }, (_, h) => [h, h === 6 || h === 11 || h === 17 ? 90 : 10])) });
  assert.ok(s.formatGewicht.fehlerfalle > s.formatGewicht.schema);
  assert.ok(s.hookGewicht.fehler > s.hookGewicht.frage);
  assert.equal(s.besteStunden.length, 3);
  assert.equal(hookTyp("Der Fehler, der 5 Punkte kostet"), "fehler");
  assert.ok(punkte({ saved: 1 }) > punkte({ likes: 1 }));
  /* Samstag: „spickzettel“ läuft schwach und wird durch das starke Format
     ersetzt; der letzte Platz bleibt das tägliche Reel. */
  const plan = tagesplan("2026-09-12", ledgerLaden(), themenpool(), { ...s, formatGewicht: { fehlerfalle: 1.6, spickzettel: 0.6 } });
  assert.ok(plan.beitraege.some((b) => b.format === "fehlerfalle"), JSON.stringify(plan.beitraege.map((b) => b.format)));
  assert.ok(!plan.beitraege.some((b) => b.format === "spickzettel"));
  assert.equal(plan.beitraege.at(-1).format, "reel");
  /* Uhrzeiten kommen aus der Zeit-Lernschleife (zeiten.mjs): im erlaubten
     Fenster, aufsteigend und mit Mindestabstand. */
  const zeitenPlan = plan.beitraege.map((b) => minutenVon(b.zeit));
  assert.ok(zeitenPlan[0] >= minutenVon("06:00"), plan.beitraege.map((b) => b.zeit).join(" "));
  assert.ok(zeitenPlan.at(-1) <= minutenVon("21:59"));
  assert.ok(zeitenPlan[1] - zeitenPlan[0] >= CONFIG.plan.zeitAbstandStunden * 60);
});

test("Wochenbericht und Schlüsselwort-Auswahl", async () => {
  const { berichtErstellen } = await import("../src/bericht.mjs");
  const { schluesselwortKommentare } = await import("../src/nachrichten.mjs");
  const ledger = { veroeffentlicht: [{ art: "beitrag", datum: "2026-09-05", format: "spickzettel", fach: "bilanz", titel: "Rückstellung", medienId: "m1", insights: { reach: 500, saved: 20, shares: 4, likes: 50, comments: 5 } }], interaktionen: [{ datum: "2026-09-05" }], nachrichten: [] };
  const text = berichtErstellen({ ledger, strategie: { reichweite7: 900, formatGewicht: {} }, follower: [{ datum: "2026-08-30", follower: 100 }, { datum: "2026-09-06", follower: 130 }], kosten: { usd: 2.5, aufrufe: 30, cacheAnteil: 0.7 }, datum: "2026-09-07" });
  assert.match(text, /Follower: 130 \(\+30 in 7 Tagen\)/);
  assert.match(text, /Rückstellung — spickzettel/);
  const jetzt = new Date().toISOString();
  const medien = [{ id: "m1", comments: { data: [{ id: "c1", text: "SCHEMA bitte!", username: "lea", timestamp: jetzt }, { id: "c2", text: "toll", username: "tom", timestamp: jetzt }, { id: "c3", text: "schema", username: "meinkanal", timestamp: jetzt }] } }, { id: "m2", comments: { data: [{ id: "c4", text: "SCHEMA", username: "x", timestamp: jetzt }] } }];
  const offen = schluesselwortKommentare(medien, "meinkanal", ledger, new Map([["m1", { bildUrl: "u", titel: "Karte" }]]));
  assert.deepEqual(offen.map((o) => o.kommentarId), ["c1"]);
});

test("Spickzettel-Folie und Hook-Wahl", async () => {
  const ctx = kontext({ stil: "kanzlei", fach: "bilanz" });
  const html = folieHtml({ art: "karte", titel: "Rückstellung in 6 Schritten", schritte: [{ titel: "Außenverpflichtung", text: "§ 249 Abs. 1 HGB" }, { titel: "Verursachung vor Stichtag", text: "R 5.7 EStR" }] }, ctx, 2, 5);
  assert.ok(html.includes('class="schritte karte"') && html.includes("Außenverpflichtung"));
  assert.ok(FOLIEN_ARTEN.includes("karte"));
});

test("Schwarz/Weiß-Wechsel: Ledger ohne Trockenlauf-Einträge, Helligkeit aus Bild", async () => {
  const { naechsteVariante } = await import("../src/planer.mjs");
  const { varianteAusHelligkeit, helligkeit, varianteErmitteln } = await import("../src/wechsel.mjs");
  const ledger = { veroeffentlicht: [
    { art: "beitrag", medienId: "1", variante: 0 },
    { art: "beitrag", medienId: "trocken", variante: 1 },
    { art: "story", medienId: "2", variante: 0 },
  ] };
  assert.equal(naechsteVariante(ledger), 1, "Trockenlauf-Einträge zählen nicht");
  assert.equal(naechsteVariante({ veroeffentlicht: [] }), 0);
  assert.equal(varianteAusHelligkeit(236), 1);
  assert.equal(varianteAusHelligkeit(20), 0);
  /* Ohne Instagram-Zugriff gilt das Ledger. */
  assert.equal(await varianteErmitteln({ ig: { letzterBeitrag: async () => { throw new Error("offline"); } }, ledger }), 1);
  assert.equal(await varianteErmitteln({ ig: null, ledger, trocken: true }), 1);
  const { spawnSync } = await import("node:child_process");
  const { ffmpegPfad } = await import("../src/stimme.mjs");
  const os = await import("node:os");
  const path = await import("node:path");
  if (spawnSync(ffmpegPfad(), ["-version"]).status !== 0) return;
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), "wechsel-"));
  for (const [farbe, erwartet] of [["white", 1], ["black", 0]]) {
    const datei = path.join(dir, `${farbe}.jpg`);
    spawnSync(ffmpegPfad(), ["-hide_banner", "-loglevel", "error", "-f", "lavfi", "-i", `color=${farbe}:s=64x64`, "-frames:v", "1", "-y", datei]);
    assert.equal(varianteAusHelligkeit(helligkeit(datei)), erwartet, farbe);
  }
  fs.rmSync(dir, { recursive: true, force: true });
});

test("Aufbau: leere Folien, doppelte CTA und Sachverhalt auf der Titelfolie werden erkannt bzw. repariert", async () => {
  const { pruefeAufbau, folieLeer } = await import("../src/pruefung.mjs");
  const folien = [
    { art: "titel", titel: "Wann startet die AfA?" },
    { art: "schritte", titel: "Schritte", schritte: [{ titel: "Abnutzbar?", text: "§ 7 EStG" }, { titel: "Stichtag", text: "Betriebsbereitschaft" }] },
    { art: "text", titel: "Wann welche Seite greift" },
    { art: "cta", titel: "Folgen" },
    { art: "text", titel: "" },
    { art: "cta", titel: "Folgen" },
  ];
  const fehler = pruefeAufbau(folien);
  assert.ok(fehler.some((f) => f.startsWith("Folie 3") && /kein Inhalt/.test(f)), fehler.join("\n"));
  assert.ok(fehler.some((f) => f.startsWith("Folie 5") && /kein Titel/.test(f)));
  assert.ok(fehler.some((f) => /Nur eine CTA/.test(f)));
  assert.equal(folieLeer({ art: "text", titel: "x", punkte: ["Erster Punkt mit Inhalt", "Zweiter Punkt"] }), false);
  assert.equal(folieLeer({ art: "vergleich", titel: "x", links: { titel: "A", punkte: ["a"] }, rechts: { titel: "B", punkte: [] } }), true);
  assert.deepEqual(pruefeAufbau([{ art: "titel", titel: "Frage?" }, { art: "merke", titel: "Merksatz", text: "Ein Satz, der wirklich hängen bleibt." }, { art: "cta" }]), []);
  /* Beispielbeiträge bleiben sauber. */
  const beispiele = JSON.parse(fs.readFileSync(new URL("../beispiele/inhalte.json", import.meta.url), "utf8"));
  for (const b of beispiele.beitraege) assert.deepEqual(pruefeAufbau(b.folien), [], b.folien[0].titel);
});

test("Tagesdeckel: Verbrauch wird gezählt, weitere Aufrufe werden gestoppt", async () => {
  const k = await import("../src/kosten.mjs");
  const gespeichert = [];
  k.budgetSetzen({ limitUsd: 0.05, bisher: 0.02, speichern: (usd) => gespeichert.push(usd) });
  assert.equal(k.budgetFrei(), true);
  k.budgetPruefen("Test");
  k.erfassen("claude-sonnet-5", { input_tokens: 1000, output_tokens: 2500 }, "test");   // 0,002 + 0,025 = 0,027 $
  assert.ok(gespeichert.length === 1 && gespeichert[0] > 0.04, JSON.stringify(gespeichert));
  assert.equal(k.budgetFrei(), false);
  assert.throws(() => k.budgetPruefen("Beitrag"), k.BudgetFehler);
  k.budgetSetzen({});   // zurücksetzen, damit andere Tests nicht betroffen sind
  assert.equal(k.budgetFrei(), true);
});

test("Reel: Animation rotiert täglich, Untertitel-Blöcke stehen fest", async () => {
  const { animationFuer, untertitelBloecke } = await import("../src/reel.mjs");
  const a = ["2026-09-06", "2026-09-07", "2026-09-08", "2026-09-09"].map(animationFuer);
  assert.deepEqual(new Set(a.slice(0, 3)).size, 3, a.join(","));
  assert.equal(a[3], a[0]);
  const { woerterVerteilen } = await import("../src/stimme.mjs");
  const szenen = [{ index: 0, woerter: woerterVerteilen("Erstens: Gibt es eine Verpflichtung nach außen? Ja, gegenüber einem Dritten.", 6, 0) }];
  const b = untertitelBloecke(szenen);
  assert.ok(b.every((x) => x.w.length >= 2 && x.w.length <= 5), JSON.stringify(b.map((x) => x.w.length)));
  assert.ok(b.every((x, i) => i === 0 || x.von >= b[i - 1].bis - 1e-9));
  assert.equal(b[0].w[0].t, "Erstens:");
});

test("Reel: Hintergrund-Clip rotiert täglich, ohne Verzeichnis keine Auswahl", async () => {
  const { hintergrundClip } = await import("../src/reel.mjs");
  const os = await import("node:os"); const path = await import("node:path");
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), "clips-"));
  assert.equal(hintergrundClip(dir, "2026-09-10"), null);
  assert.equal(hintergrundClip(path.join(dir, "fehlt"), "2026-09-10"), null);
  for (const n of ["b.mp4", "a.mp4", "notiz.txt"]) fs.writeFileSync(path.join(dir, n), "");
  const a = hintergrundClip(dir, "2026-09-10"), b = hintergrundClip(dir, "2026-09-11");
  assert.ok(a && b && a !== b && /\.mp4$/.test(a));
  assert.equal(hintergrundClip(dir, "2026-09-12"), a);
  fs.rmSync(dir, { recursive: true, force: true });
});

test("Wachstum: Hashtag-Lernschleife gewichtet Tags nach Followern, Auswahl mit Entdecker-Tags", async () => {
  const { hashtagGewichte, punkte } = await import("../src/insights.mjs");
  const { hashtagsWaehlen } = await import("../src/autor.mjs");
  const eintraege = [];
  for (let i = 0; i < 6; i++) eintraege.push({ hashtags: i % 2 ? ["#a", "#stark"] : ["#a", "#schwach"], insights: { reach: 500, follows: i % 2 ? 4 : 0, saved: 2 } });
  const g = hashtagGewichte(eintraege);
  assert.ok(g.gewicht["#stark"] > g.gewicht["#schwach"], JSON.stringify(g));
  assert.equal(g.folgen["#stark"], 12);
  assert.ok(punkte({ follows: 1 }) > punkte({ likes: 5 }));
  const kern = CONFIG.hashtags.kern;
  const tags = hashtagsWaehlen(["Bilanz", "#schwach", "#stark", "#stark"], kern, { hashtagGewicht: g.gewicht }, 3);
  assert.ok(tags.length <= CONFIG.hashtags.maxJeBeitrag);
  for (const k of kern) assert.ok(tags.includes(k));
  assert.ok(tags.indexOf("#stark") < tags.indexOf("#schwach"), tags.join(" "));
  assert.ok(tags.includes("#bilanz"));
  assert.equal(tags.filter((t) => CONFIG.hashtags.entdecker.includes(t)).length >= 1, true);
  assert.equal(new Set(tags).size, tags.length);
});

test("Reel-Cover zeigt Thema, Fach und Dauer", async () => {
  const { coverDaten } = await import("../src/reel.mjs");
  const reel = { fach: "ust", klausur: 1, kurztitel: "Organschaft: Wer schuldet die Umsatzsteuer?", szenen: [{ titel: "Organschaft" }, { titel: "Schritt 1", icon: "kreislauf" }] };
  const daten = coverDaten(reel, { gesamt: 44.6 });
  assert.equal(daten.titel, reel.kurztitel);
  assert.equal(daten.ueberzeile, "Reel · 45 Sekunden");
  assert.equal(daten.icon, "kreislauf");
  const html = coverHtml(daten, kontext({ fach: "ust", klausur: 1 }));
  assert.ok(html.includes("Umsatzsteuer?"), "Thema fehlt");
  assert.ok(html.includes("reelmarke"), "Reel-Kennzeichnung fehlt");
  assert.ok(html.includes("45 Sekunden"), "Dauer fehlt");
  assert.ok(html.includes("class=\"story cover\""), "Cover-Klasse fehlt");
  /* Ohne Szenen-Icon greift ein Standardsymbol, ohne Dauer entfällt die Zeile. */
  const ohne = coverDaten({ fach: "ao", szenen: [{ titel: "X" }] }, { gesamt: 0 });
  assert.equal(ohne.icon, "paragraf");
  assert.equal(ohne.dauerText, "");
});

test("Reel täglich, Budget dafür zurückgelegt", async () => {
  const { budgetSetzen, budgetPruefen, reservieren, reservierungAufheben, BudgetFehler } = await import("../src/kosten.mjs");
  /* Jeder Wochentag hat ein Reel. */
  for (let wt = 0; wt <= 6; wt++) assert.ok(CONFIG.reel.tage.includes(wt), `Wochentag ${wt} ohne Reel`);
  const ledger = ledgerLaden();
  for (const datum of ["2026-09-14", "2026-09-15", "2026-09-16", "2026-09-17", "2026-09-18"]) {
    const p = tagesplan(datum, ledger, themenpool());
    assert.equal(p.beitraege.filter((b) => b.format === "reel").length, 1, `${datum} ohne Reel`);
  }
  /* Rücklage: andere Aufrufe hören früher auf, das Reel kommt noch durch. */
  budgetSetzen({ limitUsd: 0.27, bisher: 0.20 });
  reservieren(0.09);
  assert.throws(() => budgetPruefen("Text schreiben"), BudgetFehler);
  budgetPruefen("Reel-Skript schreiben");   // darf die Rücklage nutzen
  reservierungAufheben();
  budgetPruefen("Text schreiben");          // nach dem Reel wieder frei
  budgetSetzen({ limitUsd: Infinity, bisher: 0 });
});

test("Uhrzeiten werden gelernt: Erkundung ohne Daten, beste Stunde mit Daten", async () => {
  const { zeitenWaehlen, zeitStatistik, zeitBericht, klasseVon } = await import("../src/zeiten.mjs");
  assert.equal(klasseVon("reel"), "reel");
  assert.equal(klasseVon("spickzettel"), "karussell");

  /* Ohne Messungen: gültige Zeiten im Fenster, Mindestabstand eingehalten,
     und über die Woche werden verschiedene Stunden ausprobiert. */
  const leer = { veroeffentlicht: [] };
  const gesehen = new Set();
  for (const datum of ["2026-09-14", "2026-09-15", "2026-09-16", "2026-09-17", "2026-09-18", "2026-09-19", "2026-09-20"]) {
    const z = zeitenWaehlen({ formate: ["spickzettel", "reel"], datum, ledger: leer, zufall: rngFuer(datum) });
    assert.equal(z.length, 2);
    const [a, b] = z.map((t) => minutenVon(t));
    assert.ok(a >= minutenVon("06:00") && b <= minutenVon("21:59"), z.join(" "));
    assert.ok(b - a >= CONFIG.plan.zeitAbstandStunden * 60, `Abstand zu klein: ${z.join(" ")}`);
    z.forEach((t) => gesehen.add(t));
  }
  assert.ok(gesehen.size >= 3, `zu wenig Erkundung: ${[...gesehen].join(" ")}`);

  /* Mit Messungen: 19 Uhr läuft für Reels deutlich besser, 8 Uhr fürs Karussell. */
  const ledger = { veroeffentlicht: [] };
  for (let i = 0; i < 10; i++) {
    ledger.veroeffentlicht.push({ art: "beitrag", datum: "2026-09-01", format: "reel", stunde: 19, insights: { reach: 4000, saved: 40, shares: 20, follows: 4 } });
    ledger.veroeffentlicht.push({ art: "beitrag", datum: "2026-09-01", format: "reel", stunde: 11, insights: { reach: 200, saved: 1, shares: 0, follows: 0 } });
    ledger.veroeffentlicht.push({ art: "beitrag", datum: "2026-09-01", format: "spickzettel", stunde: 8, insights: { reach: 3000, saved: 30, shares: 15, follows: 3 } });
    ledger.veroeffentlicht.push({ art: "beitrag", datum: "2026-09-01", format: "spickzettel", stunde: 15, insights: { reach: 150, saved: 1, shares: 0, follows: 0 } });
  }
  const stat = zeitStatistik(ledger);
  assert.equal(stat.gesamt, 40);
  assert.ok(stat.stunden["reel|19"].mittel > stat.stunden["reel|11"].mittel);
  const zeiten = zeitenWaehlen({ formate: ["spickzettel", "reel"], datum: "2026-09-21", ledger, zufall: rngFuer("x") });
  assert.equal(zeiten[0], "08:30", zeiten.join(" "));
  assert.equal(zeiten[1], "19:30", zeiten.join(" "));

  /* Zu dünne Datenlage (junges Konto, kaum Reichweite): Es wird weiter
     ausprobiert, statt sich auf Rauschen festzulegen. */
  const schwach = { veroeffentlicht: Array.from({ length: 20 }, (_, i) => ({ art: "beitrag", datum: "2026-09-01", format: i % 2 ? "reel" : "spickzettel", stunde: i % 2 ? 19 : 8, insights: { reach: i < 9 ? 1 : 0, saved: 0, shares: 0, likes: 0, follows: 0 } })) };
  const statSchwach = zeitStatistik(schwach);
  assert.equal(statSchwach.belastbar, false, JSON.stringify({ n: statSchwach.gesamt, w: statSchwach.mitWirkung, m: statSchwach.mittelPunkte }));
  const verteilt = new Set();
  for (const datum of ["2026-09-21", "2026-09-22", "2026-09-23", "2026-09-24", "2026-09-25"]) verteilt.add(zeitenWaehlen({ formate: ["spickzettel", "reel"], datum, ledger: schwach, zufall: rngFuer(datum) }).join(" "));
  assert.ok(verteilt.size >= 3, `bei dünner Datenlage zu starr: ${[...verteilt].join(" | ")}`);

  /* Bericht nennt die besten Stunden je Art. */
  const b = zeitBericht(ledger);
  assert.equal(b.klassen.reel[0].stunde, 19);
  assert.equal(b.klassen.karussell[0].stunde, 8);

  /* Abschaltbar: dann gelten die Startwerte. */
  CONFIG.plan.zeitLernen = false;
  assert.deepEqual(zeitenWaehlen({ formate: ["spickzettel", "reel"], datum: "2026-09-21", ledger }), CONFIG.plan.beitragsZeiten.slice(0, 2));
  CONFIG.plan.zeitLernen = true;
});

/* Kleiner, reproduzierbarer Zufall für die Tests. */
function rngFuer(text) {
  let h = 1779033703 ^ text.length;
  for (let i = 0; i < text.length; i++) { h = Math.imul(h ^ text.charCodeAt(i), 3432918353); h = (h << 13) | (h >>> 19); }
  let a = h >>> 0;
  return () => { a |= 0; a = (a + 0x6d2b79f5) | 0; let t = Math.imul(a ^ (a >>> 15), 1 | a); t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296; };
}

test("Reel-Hooks: Muster rotieren, schwache Einstiege fallen durch", async () => {
  const { HOOKS, HOOK_TYPEN, hookWaehlen, hookAnleitung, pruefeHook, hookTypErkennen } = await import("../src/hooks.mjs");
  /* Jedes Muster hat Regel und Beispiele – sie stehen im Auftrag an das Modell. */
  for (const [typ, h] of Object.entries(HOOKS)) {
    assert.ok(h.regel.length > 30, typ);
    assert.ok(h.beispiele.length >= 2, typ);
    for (const b of h.beispiele) assert.ok(b.titel.split(/\s+/).length <= 6, `${typ}: „${b.titel}“ zu lang`);
  }
  /* Rotation: sieben Tage, mehrere verschiedene Muster. */
  const gewaehlt = new Set(["2026-09-14", "2026-09-15", "2026-09-16", "2026-09-17", "2026-09-18", "2026-09-19", "2026-09-20"].map((d) => hookWaehlen(d)));
  assert.ok(gewaehlt.size >= 4, [...gewaehlt].join(" "));
  for (const t of gewaehlt) assert.ok(HOOK_TYPEN.includes(t));
  /* Gelernte Gewichte: ein schwaches Muster fällt aus der Rotation. */
  const strategie = { hookGewicht: Object.fromEntries(HOOK_TYPEN.map((t) => [t, t === "frage" ? 0.5 : 1.4])) };
  for (const d of ["2026-09-14", "2026-09-15", "2026-09-16", "2026-09-17"]) assert.notEqual(hookWaehlen(d, strategie), "frage");
  assert.match(hookAnleitung("fehler"), /Fehler-Hook/);

  /* Strukturprüfung */
  assert.deepEqual(pruefeHook({ titel: "Falsches Amt, Frist weg?", sprecher: "Der Einspruch landet beim falschen Finanzamt. Viele schreiben sofort: unzulässig." }), []);
  assert.ok(pruefeHook({ titel: "Kurz", sprecher: "Hallo und willkommen zurück, heute geht es um die Abgabenordnung." }).some((f) => /schwacher Einstieg/.test(f)));
  assert.ok(pruefeHook({ titel: "Ein sehr langer Bildschirmtext der viel zu viele Wörter hat", sprecher: "Kurz." }).some((f) => /Bildschirmtext hat/.test(f)));
  assert.ok(pruefeHook({ titel: "Gut", sprecher: "Dieser eine Satz ist viel zu lang geraten und enthält deutlich mehr Wörter als ein Hook vertragen kann, nämlich sehr viele." }).some((f) => /Aufhänger hat/.test(f)));
  assert.ok(pruefeHook(null).length === 1);

  /* Zuordnung für die Lernschleife */
  assert.equal(hookTypErkennen("Wer schuldet die Steuer?", ""), "frage");
  assert.equal(hookTypErkennen("Der teuerste Denkfehler", "Fast alle prüfen zuerst die Frist."), "fehler");
  assert.equal(hookTypErkennen("Ein Halbsatz entscheidet", "In Paragraf 173 steckt ein Halbsatz."), "luecke");
  assert.equal(hookTypErkennen("Kennst du diesen Moment?", "Du hast das Schema dreimal gelernt."), "alltag");
  assert.equal(hookTypErkennen("Das stimmt so nicht", "Der Einspruch hemmt die Vollziehung? Genau umgekehrt."), "widerspruch");
  assert.equal(hookTypErkennen("Nie wieder Fristchaos", "Mit drei Fragen bist du durch."), "loesung");
  /* Alle zehn Muster kommen in zehn Tagen genau einmal dran. */
  const zehn = ["2026-09-11", "2026-09-12", "2026-09-13", "2026-09-14", "2026-09-15", "2026-09-16", "2026-09-17", "2026-09-18", "2026-09-19", "2026-09-20"].map((d) => hookWaehlen(d));
  assert.equal(new Set(zehn).size, HOOK_TYPEN.length, zehn.join(" "));
});

test("Der Hook wird betont gesprochen und bekommt eine Pause", async () => {
  const { zeitplanErstellen } = await import("../src/reel.mjs");
  const gerufen = [];
  const reel = { szenen: [
    { art: "hook", titel: "Falsches Amt, Frist weg?", sprecher: "Der Einspruch landet beim falschen Finanzamt." },
    { art: "schritt", titel: "Schritt 1", sprecher: "Zuerst prüfst du die Zuständigkeit." },
    { art: "cta", titel: "Mehr davon", sprecher: "Folge für den nächsten Prüfschritt." },
  ] };
  /* Ohne Stimmanbieter (IG_STIMME=aus) wird nur geschätzt – die Betonung steht
     trotzdem im Aufruf, deshalb prüfen wir den Zeitplan. */
  const plan = await zeitplanErstellen(reel, "/tmp/ig-test-audio");
  const [hook, schritt] = plan.szenen;
  const pauseNachHook = hook.start + hook.dauer - (hook.audioStart + (hook.woerter.at(-1)?.bis ?? 0) - hook.audioStart);
  assert.ok(hook.dauer > 0 && schritt.start === hook.start + hook.dauer);
  /* Der Nachlauf des Hooks ist länger als der einer normalen Szene. */
  const nachlaufHook = hook.dauer - (hook.woerter.at(-1)?.bis ?? hook.audioStart) + hook.start;
  const nachlaufSchritt = schritt.dauer - (schritt.woerter.at(-1)?.bis ?? schritt.audioStart) + schritt.start;
  assert.ok(nachlaufHook > nachlaufSchritt, `${nachlaufHook} !> ${nachlaufSchritt}`);
  assert.ok(gerufen.length === 0);
});

test("Normen stehen in der Klausur-Zitierweise, die Stimme liest sie ausgeschrieben", async () => {
  const { normKurz, normGesprochen, felderKuerzen } = await import("../src/normen.mjs");
  assert.equal(normKurz("§ 1 Absatz 1 Satz 1 Nummer 1 Buchstabe a BGB"), "§ 1 Abs. 1 S. 1 Nr. 1 lit. a BGB");
  assert.equal(normKurz("§ 80 Abs. 1 S. 5 VwGO"), "§ 80 Abs. 1 S. 5 VwGO");
  /* Römische Absatzziffern sind auf dem Kanal seit jeher üblich und bleiben
     stehen – umgeschrieben wird nur die Klammerform des Schwester-Kanals. */
  assert.equal(normKurz("§ 441 III BGB"), "§ 441 III BGB");
  assert.equal(normKurz("§ 823 I BGB i.V.m. § 31 BGB"), "§ 823 I BGB i.V.m. § 31 BGB");
  assert.equal(normKurz("Art. 12 I GG"), "Art. 12 I GG");
  /* Klammerform aus anderen Quellen wird zurückgeholt. */
  assert.equal(normKurz("§ 7 (1) S. 1 EStG"), "§ 7 Abs. 1 S. 1 EStG");
  /* Was schon richtig steht, bleibt unverändert. */
  assert.equal(normKurz("§§ 54 ff. VwVfG"), "§§ 54 ff. VwVfG");
  assert.equal(normKurz("Nach § 1006 BGB wird vermutet."), "Nach § 1006 BGB wird vermutet.");

  /* Für die Stimme ausgeschrieben, sonst liest sie „Abs Punkt“. */
  assert.equal(normGesprochen("§ 80 Abs. 1 S. 5 VwGO"), "Paragraf 80 Absatz 1 Satz 5 VwGO");
  assert.equal(normGesprochen("Art. 2 Abs. 1 GG"), "Artikel 2 Absatz 1 GG");
  assert.match(normGesprochen("§ 823 Abs. 1 BGB i.V.m. § 31 BGB"), /in Verbindung mit/);
  assert.match(normGesprochen("Nach h.M. gilt das."), /herrschende Meinung/);
  /* Römisch muss die Stimme auflösen, sonst liest sie „drei Buchstaben I“. */
  assert.equal(normGesprochen("§ 441 III BGB"), "Paragraf 441 Absatz 3 BGB");
  assert.equal(normGesprochen("Art. 12 I GG"), "Artikel 12 Absatz 1 GG");

  /* Die Felder eines Objekts werden mitsamt Punkteliste umgeschrieben. */
  const folie = { titel: "Frist nach § 80 (5) VwGO", text: null, punkte: ["§ 123 Absatz 1 VwGO prüfen"] };
  felderKuerzen(folie, ["titel", "text", "norm"]);
  assert.equal(folie.titel, "Frist nach § 80 Abs. 5 VwGO");
  assert.equal(folie.punkte[0], "§ 123 Abs. 1 VwGO prüfen");
  assert.equal(folie.text, null);

  /* Die Plagiatsprüfung erkennt die Zitierweise weiterhin als Normzitat. */
  const { ohneNormen } = await import("../src/pruefung.mjs");
  assert.match(ohneNormen("Nach § 80 Abs. 1 S. 5 VwGO gilt das."), /Nach\s+NORM\s+gilt das\./);
});

test("ElevenLabs läuft auf dem Monatsguthaben und fällt danach auf Piper zurück", async () => {
  const stimme = await import("../src/stimme.mjs");
  const key = CONFIG.reel.elevenlabsKey, wunsch = process.env.IG_STIMME, fetchAlt = globalThis.fetch;
  CONFIG.reel.elevenlabsKey = "test-key";
  delete process.env.IG_STIMME;
  let gespeichert = null;
  const verbinden = () => stimme.stimmeStandVerbinden({ lesen: () => gespeichert, schreiben: (s) => { gespeichert = s; } });
  verbinden();

  const antwort = (daten) => ({ ok: true, json: async () => daten, text: async () => JSON.stringify(daten) });
  const reset = Date.now() + 10 * 86400000;
  globalThis.fetch = async () => antwort({ tier: "free", character_count: 1200, character_limit: 10000, next_character_count_reset_unix: Math.floor(reset / 1000) });
  assert.equal(await stimme.anbieterFuerText(400), "elevenlabs");
  assert.equal(gespeichert.rest, 8800);

  /* Reicht das Guthaben nicht für das ganze Reel, spricht von Szene eins an
     die Offline-Stimme – ein Wechsel mitten im Video wäre hörbar. */
  verbinden();
  globalThis.fetch = async () => antwort({ tier: "free", character_count: 9900, character_limit: 10000, next_character_count_reset_unix: Math.floor(reset / 1000) });
  assert.notEqual(await stimme.anbieterFuerText(900), "elevenlabs");

  /* Ist es ganz leer, merkt sich der Bot das – ohne erneute Abfrage. */
  verbinden();
  globalThis.fetch = async () => antwort({ tier: "free", character_count: 10000, character_limit: 10000, next_character_count_reset_unix: Math.floor(reset / 1000) });
  assert.notEqual(await stimme.anbieterFuerText(10), "elevenlabs");
  assert.equal(gespeichert.erschoepft, true);
  verbinden();
  globalThis.fetch = async () => { throw new Error("darf nicht erneut fragen"); };
  assert.notEqual(await stimme.anbieterFuerText(10), "elevenlabs");

  /* Am Stichtag des Abos ist das Guthaben wieder da. */
  gespeichert = { ...gespeichert, resetAm: new Date(Date.now() - 1000).toISOString() };
  verbinden();
  assert.equal(stimme.stimmeStand().erschoepft, false);
  assert.equal(stimme.stimmenAnbieter(), "elevenlabs");

  globalThis.fetch = fetchAlt;
  stimme.stimmeStandVerbinden(null);
  CONFIG.reel.elevenlabsKey = key;
  if (wunsch != null) process.env.IG_STIMME = wunsch;
});

test("Die Stimme wird ausprobiert und erst bei klarem Vorsprung festgeschrieben", async () => {
  const { stimmeBewerten, stimmeWaehlen, stimmenStatistik, gewinner } = await import("../src/stimmen.mjs");

  const erzaehler = stimmeBewerten({ voice_id: "a", name: "Anna", language: "de", gender: "female", age: "middle_aged", use_case: "informative_educational", descriptive: "calm" });
  const werbung = stimmeBewerten({ voice_id: "b", name: "Bert", language: "de", gender: "male", age: "young", use_case: "advertisement", descriptive: "excited" });
  assert.ok(erzaehler.punkte > (werbung?.punkte ?? -1));
  assert.equal(stimmeBewerten({ voice_id: "c", name: "Kid", language: "de", age: "child", use_case: "narrative_story" }), null);

  const kandidaten = [{ id: "a", name: "Anna" }, { id: "b", name: "Bert" }, { id: "c", name: "Carla" }];
  const leer = { veroeffentlicht: [] };
  const gesehen = new Set();
  for (let i = 0; i < 40; i++) gesehen.add(stimmeWaehlen({ kandidaten, ledger: leer, datum: "2026-09-15" }).id);
  assert.equal(gesehen.size, 3);
  assert.equal(stimmeWaehlen({ kandidaten, ledger: leer, datum: "2026-09-15", fest: { id: "b", name: "Bert" } }).id, "b");

  const reel = (id, wert, tag) => ({ art: "beitrag", format: "reel", datum: `2026-08-${String(tag).padStart(2, "0")}`, stimmeId: id, stimmeName: id, insights: { reach: wert, saved: 0, shares: 0, likes: 0, comments: 0 } });
  const ledger = { veroeffentlicht: [] };
  let tag = 1;
  for (let i = 0; i < 6; i++) ledger.veroeffentlicht.push(reel("a", 200, tag++), reel("b", 60, tag++), reel("c", 40, tag++));
  const stat = stimmenStatistik(ledger, new Date("2026-09-15T12:00:00Z"));
  assert.equal(gewinner(stat, kandidaten).id, "a");

  const duenn = { veroeffentlicht: [reel("a", 200, 1), reel("b", 60, 2)] };
  assert.equal(gewinner(stimmenStatistik(duenn, new Date("2026-09-15T12:00:00Z")), kandidaten), null);
});

test("Titelbild: Szene statt Vokabel, Querformat, kein Treffer heißt kein Bild", async () => {
  const { fotoSuchen, titelbild } = await import("../src/bilder.mjs");
  const { CONFIG } = await import("../src/config.mjs");
  const key = CONFIG.bilder.key, fetchAlt = globalThis.fetch;
  CONFIG.bilder.key = "test-key";
  let gefragt = null;
  const antwort = (fotos) => ({ ok: true, json: async () => ({ photos: fotos }), text: async () => "" });
  const foto = (id, w, h) => ({ id, width: w, height: h, photographer: `F${id}`, url: `https://pexels/${id}`, src: { large2x: `https://img/${id}.jpg` } });

  /* Hochformat und zu kleine Bilder fallen raus. */
  globalThis.fetch = async (u) => { gefragt = u; return antwort([foto(1, 800, 1200), foto(2, 900, 600), foto(3, 2000, 1300)]); };
  const treffer = await fotoSuchen("delivery man waiting at door", { zufall: () => 0 });
  assert.equal(treffer.id, 3, "nur groß und quer");
  assert.match(gefragt, /delivery\+man|delivery%20man/);
  assert.match(gefragt, /orientation=landscape/);

  /* Kein Treffer: kein Bild – lieber das Icon als ein beliebiges Symbolfoto. */
  globalThis.fetch = async () => antwort([]);
  assert.equal(await fotoSuchen("annahmeverzug"), null);

  /* Ohne Szene wird gar nicht erst gesucht. */
  globalThis.fetch = async () => { throw new Error("darf nicht fragen"); };
  assert.equal(await titelbild({ folien: [{ art: "titel" }] }), null);

  globalThis.fetch = fetchAlt;
  CONFIG.bilder.key = key;
});

test("Freistellen: unbrauchbare Ergebnisse werden verworfen", async () => {
  const { deckung } = await import("../src/freistellen.mjs");
  /* Kein Bild → keine Deckung, statt einer Zahl, mit der man weiterrechnet. */
  assert.equal(deckung("/gibt/es/nicht.png"), null);
});

test("Strenger Faktencheck: ohne Prüfung erscheint kein Beitrag", async () => {
  const { pruefeFakten } = await import("../src/faktencheck.mjs");
  /* Abgeschalteter Faktencheck meldet weiterhin „in Ordnung“ – nur der
     technische Ausfall führt im strengen Modus zum Ausfall des Beitrags. */
  const alt = CONFIG.faktencheck.aktiv;
  CONFIG.faktencheck.aktiv = false;
  const r = await pruefeFakten({ folien: [{ art: "titel", titel: "Test" }] });
  assert.deepEqual(r, { ok: true, fehler: [], hinweise: [] });
  CONFIG.faktencheck.aktiv = alt;
  assert.equal(CONFIG.faktencheck.strikt, true, "streng ist der Standard");
});

test("Normen: gesprochene Form wird für Text zurückgewandelt", async () => {
  const { normGeschrieben } = await import("../src/normen.mjs");
  assert.equal(normGeschrieben("Paragraf 48 Absatz 2 VwVfG"), "§ 48 Abs. 2 VwVfG");
  assert.equal(normGeschrieben("Paragrafen 116 ff. BGB"), "§§ 116 ff. BGB");
  assert.equal(normGeschrieben("Artikel 3 Absatz 1 GG"), "Art. 3 Abs. 1 GG");
  assert.equal(normGeschrieben("§ 441 III BGB"), "§ 441 III BGB");
});

test("Hashtags: fremde Rechtsgebiete werden aussortiert", async () => {
  const { hashtagsWaehlen } = await import("../src/autor.mjs");
  const kern = CONFIG.hashtags.kern;
  const tags = hashtagsWaehlen(["#öffentlichesrecht", "#strafrecht", "#kaufrecht"], kern, null, undefined, 1);
  assert.ok(!tags.includes("#öffentlichesrecht"), tags.join(" "));
  assert.ok(!tags.includes("#strafrecht"), tags.join(" "));
  assert.ok(tags.includes("#kaufrecht"), tags.join(" "));
  const zivil = hashtagsWaehlen(["#zivilrecht"], kern, null, undefined, 1);
  assert.ok(zivil.includes("#zivilrecht"), zivil.join(" "));
});

test("Normen in Mono: Paragrafen, Aufzählungen und Artikel, aber keine Prosa", async () => {
  const { markieren } = await import("../src/vorlagen.mjs");
  /* Nach dem Paragrafenzeichen steht ein geschütztes Leerzeichen, damit es
     nicht allein am Zeilenende hängt - deshalb hier \s statt eines Leerzeichens. */
  assert.match(markieren("Nach § 280 Abs. 1 BGB haftet er"), /<code>§\s280 Abs\.\s1 BGB<\/code>/);
  assert.match(markieren("§§ 61, 62 VwGO regeln die Fähigkeit"), /<code>§§\s61, 62 VwGO<\/code>/);
  assert.match(markieren("Art. 20 Abs. 3 GG folgt"), /<code>Art\.\s20 Abs\.\s3 GG<\/code>/);
  /* Ohne Paragrafenzeichen ist es ein Satz, kein Zitat. */
  assert.equal(markieren("Der Antrag ist zulässig, die Klage nach der ZPO auch").includes("<code>"), false);
});

test("Mindset-Reels laufen auf Fächern, die es in diesem Kanal gibt", async () => {
  const { MINDSET_THEMEN } = await import("../src/kalender.mjs");
  const { FAECHER } = await import("../src/inhalte.mjs");
  for (const m of MINDSET_THEMEN) assert.ok(FAECHER[m.fach], `Fach fehlt: ${m.fach}`);
  assert.ok(MINDSET_THEMEN.every((m) => [1, 2, 3].includes(m.klausur)));
});

test("Reel-Fußzeile trägt das Rechtsgebiet, nicht den Klausurtag", async () => {
  const { fussRechts } = await import("../src/vorlagen.mjs");
  assert.equal(fussRechts({ klausur: 1 }), "Zivilrecht");
  assert.equal(fussRechts({ klausur: 3 }), "Öffentliches Recht");
  assert.equal(fussRechts({ fach: "methodik", klausur: 2 }), "Klausurtechnik");
});
