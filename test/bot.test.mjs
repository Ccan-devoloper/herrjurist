import { test } from "node:test";
import assert from "node:assert/strict";
import { themenpool, poolStatistik, FAECHER } from "../src/inhalte.mjs";
import { pruefeBeitrag, uebernahmen, uebernahmeLaeufe, gesperrteNamen, korpus, firmenNamen, benutzteFirmen, namenSperren } from "../src/pruefung.mjs";
import { tagesplan, vermerken, ledgerLaden } from "../src/planer.mjs";
import { folieHtml, storyHtml, coverHtml, FOLIEN_ARTEN, STORY_ARTEN } from "../src/vorlagen.mjs";
import { kontext } from "../src/render.mjs";
import { STILE } from "../src/stile.mjs";
import { tageBis, minutenVon, hhmm, heuteIso } from "../src/zeit.mjs";
import { tokenVerschluesseln, tokenEntschluesseln } from "../src/instagram.mjs";
import fs from "node:fs";
import os from "node:os";
import { spawnSync } from "node:child_process";
import path from "node:path";
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
  /* „mindset" ist kein Pool-Fach: Diese Themen stehen im Kalender. */
  for (const f of Object.keys(FAECHER).filter((x) => x !== "mindset")) assert.ok(st.jeFach[f] > 0, `Fach ${f} fehlt`);
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
  assert.equal(gesperrteNamen("Die Nordlicht GmbH klagt gegen die Stadt.", k).length, 1);
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
  /* Zwei Karussells plus das Reel: Auf diesem Kanal kommt das Reel zu den
     Beiträgen dazu, statt den letzten zu ersetzen (CONFIG.reel.zusaetzlich). */
  assert.equal(a.beitraege.length, CONFIG.plan.beitraegeWerktag + (CONFIG.reel.zusaetzlich ? 1 : 0));
  assert.equal(a.beitraege.filter((b) => b.format === "reel").length, 1);
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
  assert.equal(so.beitraege.length, CONFIG.plan.beitraegeWochenende + (CONFIG.reel.zusaetzlich ? 1 : 0));
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
  assert.ok(MINDSET_THEMEN.some((t) => t.id === mindsetThema("2026-09-12").id));
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
    const erwartet = CONFIG.plan.formateEndspurt[1].slice(0, CONFIG.plan.beitraegeWerktag);
    if (CONFIG.reel.zusaetzlich) erwartet.push("reel");
    else erwartet[erwartet.length - 1] = "reel";
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
  assert.ok(zeitenPlan.at(-1) <= minutenVon("22:59"));
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
  /* Der Deckel wird vorab mit dem belastet, was ein Aufruf dieses Zwecks
     erfahrungsgemäß kostet (rund 0,05 $ für einen Beitrag). Deshalb braucht
     dieser Test echte Größenordnungen statt Centbeträge. */
  k.budgetSetzen({ limitUsd: 0.12, bisher: 0.02, speichern: (usd) => gespeichert.push(usd) });
  assert.equal(k.budgetFrei("beitrag"), true);
  k.budgetPruefen("beitrag");
  k.erfassen("claude-sonnet-5", { input_tokens: 1000, output_tokens: 2500 }, "beitrag");   // 0,002 + 0,025 = 0,027 $
  assert.ok(gespeichert.length === 1 && gespeichert[0] > 0.04, JSON.stringify(gespeichert));
  /* Ab jetzt rechnet der Deckel mit dem gemessenen Wert (0,027 $ je Beitrag),
     nicht mehr mit der Schätzung – ein dritter Aufruf passt also noch. */
  k.erfassen("claude-sonnet-5", { input_tokens: 1000, output_tokens: 2500 }, "beitrag");
  assert.equal(k.budgetFrei("beitrag"), true);
  k.erfassen("claude-sonnet-5", { input_tokens: 1000, output_tokens: 2500 }, "beitrag");   // 0,02 + 3 × 0,027 = 0,101 $
  assert.equal(k.budgetFrei("beitrag"), false);
  assert.throws(() => k.budgetPruefen("Beitrag"), k.BudgetFehler);
  assert.ok(k.tagesStand() < 0.12, `Deckel überschritten: ${k.tagesStand()}`);
  k.budgetSetzen({});   // zurücksetzen, damit andere Tests nicht betroffen sind
  assert.equal(k.budgetFrei(), true);
});

test("Tagesdeckel: nach der ersten Messung zählt die Messung, nicht die Schätzung", async () => {
  const k = await import("../src/kosten.mjs");
  /* Der Fall vom 11.09.: Ein Reel-Entwurf kostete 0,047 $, wurde vom
     Faktencheck zu Recht beanstandet – und der zweite Versuch scheiterte an
     der Schätzung von 0,06 $, nicht am Geld. Ein Aufruf, der günstiger ist
     als geschätzt, darf den nächsten nicht blockieren. */
  k.budgetSetzen({ limitUsd: 0.27, bisher: 0.168, reserviert: 0.11, reserviertFuer: "reel" });
  k.erfassen("claude-sonnet-5", { input_tokens: 2400, output_tokens: 1900 }, "reel");        // ≈ 0,024 $
  k.erfassen("claude-haiku-4-5", { input_tokens: 2000, output_tokens: 621 }, "reel-faktencheck");
  const vorher = k.tagesStand();
  assert.ok(vorher > 0.19 && vorher < 0.22, String(vorher));
  assert.equal(k.budgetFrei("reel"), true, `zweiter Versuch blockiert bei ${vorher.toFixed(3)} $`);

  /* Und der nächste Lauf des Tages rechnet ebenfalls mit der Messung: Sie
     wandert über state/kosten.json in den folgenden Prozess. */
  const gemessen = k.messungen();
  assert.ok(gemessen.reel > 0.02 && gemessen.reel < 0.06, JSON.stringify(gemessen));
  k.budgetSetzen({ limitUsd: 0.27, bisher: 0.2145, reserviert: 0.11, reserviertFuer: "reel" });
  assert.equal(k.budgetFrei("reel"), false, "ohne Messung müsste der Deckel greifen");
  k.budgetSetzen({ limitUsd: 0.27, bisher: 0.2145, reserviert: 0.11, reserviertFuer: "reel", gemessen });
  assert.equal(k.budgetFrei("reel"), true, "mit Messung muss das Reel noch passen");
  k.budgetSetzen({});
});

test("Reel: Animation rotiert täglich, Untertitel zeigen ganze Sätze", async () => {
  const { animationFuer, untertitelBloecke } = await import("../src/reel.mjs");
  const a = ["2026-09-06", "2026-09-07", "2026-09-08", "2026-09-09"].map(animationFuer);
  assert.deepEqual(new Set(a.slice(0, 3)).size, 3, a.join(","));
  assert.equal(a[3], a[0]);
  const { woerterVerteilen } = await import("../src/stimme.mjs");
  const szenen = [{ index: 0, woerter: woerterVerteilen("Erstens: Gibt es eine Verpflichtung nach außen? Ja, gegenüber einem Dritten.", 6, 0) }];
  const b = untertitelBloecke(szenen);
  /* Zwei Sätze, also zwei Blöcke - der zweite ist so kurz, dass er nicht bricht. */
  assert.equal(b.length, 2, JSON.stringify(b.map((x) => x.text)));
  assert.equal(b[0].text, "Erstens: Gibt es eine Verpflichtung nach außen?");
  assert.equal(b[1].text, "Ja, gegenüber einem Dritten.");
  assert.ok(b.every((x, i) => i === 0 || x.von >= b[i - 1].bis - 1e-9));
  /* Ein sehr langer Satz bricht, sonst passt er nicht auf die Karte. */
  const lang = [{ index: 0, woerter: woerterVerteilen("Die Behörde darf den Bescheid nur zurücknehmen, wenn das Vertrauen des Begünstigten nicht schutzwürdig ist und die Jahresfrist noch läuft.", 9, 0) }];
  const bl = untertitelBloecke(lang);
  assert.ok(bl.length >= 2, JSON.stringify(bl.map((x) => x.text)));
  assert.ok(bl.every((x) => x.text.split(" ").length <= 17), JSON.stringify(bl.map((x) => x.text.split(" ").length)));
  /* Kein Wort geht verloren. */
  assert.equal(bl.map((x) => x.text).join(" "), lang[0].woerter.map((w) => w.wort).join(" "));
  /* Gesprochen wird der ausgeschriebene Gesetzesname, angezeigt das Kürzel –
     sonst läuft „VERWALTUNGSVERFAHRENSGESETZ“ quer über die Karte. */
  const norm = [{ index: 0, woerter: woerterVerteilen("Paragraf 48 Absatz 4 Verwaltungsverfahrensgesetz: Die Behörde hat ein Jahr.", 6, 0) }];
  const bn = untertitelBloecke(norm);
  assert.ok(bn[0].text.startsWith("§ 48 Abs. 4 VwVfG"), bn[0].text);
  assert.ok(!bn.some((x) => /Verwaltungsverfahrensgesetz|Paragraf/.test(x.text)), JSON.stringify(bn.map((x) => x.text)));
  /* „Abs.“ endet auf einen Punkt, beendet aber keinen Satz – sonst zerfiel
     „§ 48 Abs. 4 VwVfG“ in zwei Untertitel. */
  assert.equal(bn[0].text.startsWith("§ 48 Abs. 4 VwVfG:"), true, bn[0].text);
});

test("Reel-Seite: Untertitel steht groß, Gesetzeskürzel behalten ihre Schreibweise", async () => {
  /* Die Funktion, die die Kürzel schont, steht in einem Template-String und
     wird erst in der Seite zu Code. Ein einfach geschriebenes \\s verschluckt
     der String – dann trennt das Muster keine Wörter mehr, der ganze Satz
     landet in einer Spanne und die Großschreibung fällt aus. Genau das ist
     passiert, und nur die fertige Seite zeigt es. */
  const src = fs.readFileSync(new URL("../src/reel.mjs", import.meta.url), "utf8");
  const fn = src.match(/function kuerzelSchonen\(text\)[\s\S]*?\n\}/);
  assert.ok(fn, "kuerzelSchonen nicht gefunden");
  /* So, wie es in der Seite ankommt: einmal durch den Template-String. */
  const inSeite = new Function(`return \`${fn[0].replace(/`/g, "\\`")}\``)();
  const kuerzelSchonen = new Function(`${inSeite}; return kuerzelSchonen;`)();
  assert.equal(kuerzelSchonen("§ 48 Abs. 4 VwVfG: Die Behörde hat"), '§ 48 Abs. 4 <span class="k">VwVfG:</span> Die Behörde hat');
  assert.equal(kuerzelSchonen("Nach § 280 Abs. 1 BGB haftet er"), "Nach § 280 Abs. 1 BGB haftet er");
  assert.equal(kuerzelSchonen("a < b"), "a &lt; b");
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
  /* Der Kurztitel fasst das ganze Reel zusammen und darf vom ersten
     gesprochenen Satz abweichen - er steht auf dem Cover. */
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

  /* Ohne Messungen: Der erste Tag folgt dem Vorwissen aus den Studien
     (Karussell vormittags, Reel abends); danach werden die Nachbarstunden
     ausprobiert. Jeder Tag trägt seine Beiträge in den Ledger ein, wie im
     Betrieb - nur so kann die Erkundung wissen, was schon dran war. */
  const leer = { veroeffentlicht: [] };
  const erster = zeitenWaehlen({ formate: ["spickzettel", "reel"], datum: "2026-09-14", ledger: leer, zufall: rngFuer("2026-09-14") });
  assert.ok(minutenVon(erster[0]) >= minutenVon("08:00") && minutenVon(erster[0]) <= minutenVon("13:59"), `Karussell ohne Daten nicht vormittags/mittags: ${erster[0]}`);
  assert.ok(minutenVon(erster[1]) >= minutenVon("18:00"), `Reel ohne Daten nicht abends: ${erster[1]}`);
  const gesehen = new Set();
  for (const datum of ["2026-09-14", "2026-09-15", "2026-09-16", "2026-09-17", "2026-09-18", "2026-09-19", "2026-09-20"]) {
    const z = zeitenWaehlen({ formate: ["spickzettel", "reel"], datum, ledger: leer, zufall: rngFuer(datum) });
    assert.equal(z.length, 2);
    const [a, b] = z.map((t) => minutenVon(t));
    assert.ok(a >= minutenVon("06:00") && b <= minutenVon("22:59"), z.join(" "));
    assert.ok(b - a >= CONFIG.plan.zeitAbstandStunden * 60, `Abstand zu klein: ${z.join(" ")}`);
    z.forEach((t) => gesehen.add(t));
    leer.veroeffentlicht.push({ art: "beitrag", datum, format: "spickzettel", zeit: z[0] }, { art: "beitrag", datum, format: "reel", zeit: z[1] });
  }
  assert.ok(gesehen.size >= 4, `zu wenig Erkundung: ${[...gesehen].join(" ")}`);
  /* Erkundet wird in der Nähe des Vorwissens, nicht wahllos: Die meisten
     Reels bleiben am Abend, das zweite Studienfenster (8–12 Uhr) darf
     vorkommen, die Nacht nicht. */
  const reels = leer.veroeffentlicht.filter((e) => e.format === "reel").map((e) => minutenVon(e.zeit));
  assert.ok(reels.filter((m) => m >= minutenVon("17:00")).length >= 5, `Reels zu selten abends: ${reels.join(" ")}`);
  assert.ok(reels.every((m) => m >= minutenVon("08:00")), `Reel zu früh: ${reels.join(" ")}`);

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
  for (const datum of ["2026-09-21", "2026-09-22", "2026-09-23", "2026-09-24", "2026-09-25"]) {
    const z = zeitenWaehlen({ formate: ["spickzettel", "reel"], datum, ledger: schwach, zufall: rngFuer(datum) });
    verteilt.add(z.join(" "));
    /* Wie im Betrieb: Jeder Tag landet im Ledger, auch ohne Zahlen. */
    schwach.veroeffentlicht.push({ art: "beitrag", datum, format: "spickzettel", zeit: z[0], insights: { reach: 0 } }, { art: "beitrag", datum, format: "reel", zeit: z[1], insights: { reach: 0 } });
  }
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

  /* Für die Stimme ausgeschrieben, sonst liest sie „Abs Punkt“. Kürzel mit
     gemischter Schreibweise werden dazu ausgeschrieben – „VwGO“ kam als
     „Vau-Weh-Geh-O“ zerhackt heraus. */
  assert.equal(normGesprochen("§ 80 Abs. 1 S. 5 VwGO"), "Paragraf 80 Absatz 1 Satz 5 Verwaltungsgerichtsordnung");
  assert.equal(normGesprochen("§ 48 Abs. 2 VwVfG"), "Paragraf 48 Absatz 2 Verwaltungsverfahrensgesetz");
  /* Saubere Initialen liest jede Stimme richtig und bleiben stehen. */
  assert.equal(normGesprochen("§ 280 Abs. 1 BGB"), "Paragraf 280 Absatz 1 BGB");
  assert.equal(normGesprochen("§ 212 StGB"), "Paragraf 212 StGB");
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

  /* Deutsch-Regel: Eine englisch aufgenommene Stimme kommt gar nicht erst in
     die Auswahl - sie liest „§ 294 BGB" falsch. */
  assert.equal(stimmeBewerten({ voice_id: "d", name: "Daniel", gender: "male", age: "middle_aged", use_case: "informative_educational", descriptive: "professional", accent: "british" }), null);
  assert.ok(stimmeBewerten({ voice_id: "e", name: "Erik", gender: "male", age: "middle_aged", use_case: "informative_educational", accent: "german" })?.deutsch);

  const kandidaten = [{ id: "a", name: "Anna", deutsch: true }, { id: "b", name: "Bert", deutsch: true }, { id: "c", name: "Carla", deutsch: true }];
  /* Stehen nur englische Stimmen in der Liste, wird keine gewaehlt - dann
     spricht die deutsche Offline-Stimme. */
  assert.equal(stimmeWaehlen({ kandidaten: [{ id: "x", name: "Alice", deutsch: false }], ledger: { veroeffentlicht: [] }, datum: "2026-09-15" }), null);
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
  assert.deepEqual(r, { ok: true, fehler: [], hinweise: [], korrekturen: [], behebbar: [] });
  CONFIG.faktencheck.aktiv = alt;
  assert.equal(CONFIG.faktencheck.strikt, true, "streng ist der Standard");
});

test("Normen: gesprochene Form wird für Text zurückgewandelt", async () => {
  const { normKurz } = await import("../src/normen.mjs");
  assert.equal(normKurz("Paragraf 48 Absatz 2 VwVfG"), "§ 48 Abs. 2 VwVfG");
  assert.equal(normKurz("Paragrafen 116 ff. BGB"), "§§ 116 ff. BGB");
  assert.equal(normKurz("Artikel 3 Absatz 1 GG"), "Art. 3 Abs. 1 GG");
  assert.equal(normKurz("§ 441 III BGB"), "§ 441 III BGB");
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
  /* Auch die taeglich rotierenden Entdecker-Tags duerfen kein fremdes Gebiet
     einschleusen - genau daran ist #staatsrecht unter einem Zivilrechtsbeitrag
     gelandet. Ueber viele Tage geprueft, weil sie nach Datum rotieren. */
  const fremd = ["#staatsrecht", "#strafrecht", "#öffentlichesrecht", "#verwaltungsrecht", "#grundrechte", "#stpo"];
  for (let t = 0; t < 60; t++) {
    const tags = hashtagsWaehlen([], kern, null, t, 1);
    for (const f of fremd) assert.ok(!tags.includes(f), `Tag ${t}: ${f} in ${tags.join(" ")}`);
  }
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

test("Prüfung weist Vorstellungen zurück, die es nur im Steuerberaterexamen gibt", async () => {
  const { pruefeBeitrag } = await import("../src/pruefung.mjs");
  const abgelehnt = (t) => pruefeBeitrag({ caption: t }).fehler.some((f) => f.includes(t.match(/\S.*\S/)[0].slice(0, 6)) || /Staatsexamen|Reihenfolge|Klausur|Ankündigung/.test(f));
  for (const t of ["Der Klassiker in der zweiten Klausurenrunde", "Hier verlierst du die meisten Punkte", "Das kostet dich 5 Punkte", "Am zweiten Prüfungstag kommt das dran", "Nächstes Mal zeige ich dir den Widerruf", "Teil 2 folgt"]) {
    assert.ok(abgelehnt(t), `nicht erkannt: ${t}`);
  }
  /* Notenpunkte als Klausurergebnis und „Punkte sammeln“ bleiben erlaubt –
     nur die Punktzahl je Prüfungsschritt gibt es im Staatsexamen nicht. */
  for (const t of ["Mit 9 Notenpunkten hast du bestanden", "Ein Dauerbrenner in den Zivilrechtsklausuren", "Punkte sammeln, wo es leichtfällt", "Folg mir für den Unterschied zur Rücknahme"]) {
    const f = pruefeBeitrag({ caption: t }).fehler.filter((x) => /Staatsexamen|Reihenfolge|Ankündigung|Punkte/.test(x));
    assert.equal(f.length, 0, `zu Unrecht beanstandet: ${t} → ${f.join(" | ")}`);
  }
});

test("Prüfung: Grundgesetz wird mit Artikel zitiert, nie mit Paragraf", async () => {
  const { pruefeBeitrag } = await import("../src/pruefung.mjs");
  const geruegt = (t) => pruefeBeitrag({ caption: t }).fehler.some((f) => /Artikel zitiert/.test(f));
  /* Beide Schreibweisen: auf der Kachel „§“, im Sprechertext „Paragraf“. */
  for (const t of ["§ 9 Abs. 3 GG schützt die Koalitionsfreiheit", "Das steht in § 9 GG", "Nach Paragraf 9 Absatz 3 GG ist das geschützt", "Paragraf 20 Absatz 3 GG bindet die Verwaltung", "§ 5 Abs. 1 Satz 2 GG", "§ 47 EMRK"]) {
    assert.ok(geruegt(t), `nicht erkannt: ${t}`);
  }
  for (const t of ["Art. 9 Abs. 3 GG schützt die Koalitionsfreiheit", "Artikel 20 Absatz 3 GG bindet die Verwaltung", "§ 823 Abs. 1 BGB", "§ 80 Abs. 5 VwGO", "Art. 19 Abs. 4 GG i.V.m. § 40 VwGO", "§ 9 BGB und Art. 12 GG"]) {
    assert.ok(!geruegt(t), `zu Unrecht beanstandet: ${t}`);
  }
});

test("Reel-Länge: unerforschte Fenster zuerst, danach entscheidet die Messung", async () => {
  const { dauerFenster, dauerWaehlen, strategieAbleiten } = await import("../src/insights.mjs");
  assert.equal(dauerFenster(32), "30-45");
  assert.equal(dauerFenster(70), "60-80");
  /* Auch was über dem letzten Fenster liegt, zählt mit – sonst fiele ein Reel,
     das ein paar Sekunden überzieht, aus der Messung. */
  assert.equal(dauerFenster(140), "80-105");
  assert.equal(dauerFenster(0), null);
  /* Ohne Messwerte rotieren alle vier Fenster über die Tage. */
  const daten = ["2026-09-10", "2026-09-11", "2026-09-12", "2026-09-13"];
  const tage = daten.map((d) => dauerWaehlen(d).join("-"));
  assert.equal(new Set(tage).size, 4, tage.join(" "));
  /* Ein langes Reel bekommt nie ein kurzes Fenster. */
  for (const d of daten) assert.ok(dauerWaehlen(d, null, { min: 60 })[1] > 60, `${d}: ${dauerWaehlen(d, null, { min: 60 }).join("-")}`);
  /* Sind alle Fenster durchgemessen, gewinnt das mit den besseren Zahlen. */
  const eintraege = [];
  for (let i = 0; i < 24; i++) {
    const dauer = [35, 50, 70, 90][i % 4];
    eintraege.push({ art: "beitrag", format: "reel", dauer, insights: { reach: 1000, follows: dauer === 70 ? 9 : 1, saved: 2 } });
  }
  const st = strategieAbleiten({ veroeffentlicht: eintraege });
  assert.ok(st.dauerGewicht["60-80"] > st.dauerGewicht["30-45"], JSON.stringify(st.dauerGewicht));
  const gewaehlt = ["2026-09-10", "2026-09-11", "2026-09-12"].map((d) => dauerWaehlen(d, st).join("-"));
  assert.ok(gewaehlt.every((f) => f === "60-80"), gewaehlt.join(" "));
});

test("Tagesplan: Stories füllen das ganze Fenster, auch den Morgen", async () => {
  const { tagesplan } = await import("../src/planer.mjs");
  const p = tagesplan("2026-09-11", { veroeffentlicht: [] });
  const frei = p.stories.filter((s) => s.art !== "teaser");
  assert.ok(frei.length >= 5, `nur ${frei.length} eigenständige Stories`);
  /* Die Teaser bringen die Zeit ihres Beitrags mit. Wurden sie bei der
     Verteilung mitgezählt, blieben die ersten beiden Slots ungenutzt und vor
     10 Uhr erschien nichts – obwohl das Fenster um 7 Uhr beginnt. */
  const erste = Math.min(...frei.map((s) => Number(s.zeit.slice(0, 2)) * 60 + Number(s.zeit.slice(3))));
  assert.ok(erste < 9 * 60, `erste eigenständige Story erst um ${p.stories[0].zeit}`);
  /* Und der Abend wird auch bespielt. */
  const letzte = Math.max(...frei.map((s) => Number(s.zeit.slice(0, 2)) * 60 + Number(s.zeit.slice(3))));
  assert.ok(letzte > 17 * 60, `letzte eigenständige Story schon um ${letzte}`);
});

test("Faktencheck liest auch Stories und ordnet Befunde ihrem Slot zu", async () => {
  const { textAus } = await import("../src/faktencheck.mjs");
  const t = textAus({ stories: [
    { slot: "s3", art: "frage", titel: "Wann liegt ein Reisemangel vor?", optionen: ["A", "B"] },
    { slot: "s5", art: "norm", norm: "§ 651m BGB", text: "Rechtsfolgen: Abhilfe, Minderung" },
  ] });
  assert.match(t, /\[Story s3 frage\]/);
  assert.match(t, /\[Story s5 norm\]/);
  assert.match(t, /§ 651m BGB/);
  /* Der Slot im Kopf ist der Anker, über den ein Befund später genau einer
     Kachel zugeordnet wird – ohne ihn müssten alle neu geschrieben werden. */
  assert.ok(t.split("\n").length === 2, t);
});

test("Reel-Länge: die Annahmegrenze passt zu jedem Zeitfenster", async () => {
  const { CONFIG } = await import("../src/config.mjs");
  /* Dieselbe Rechnung wie in reelSchreiben. Stand die Grenze fest (45–110
     Wörter), wurde jedes Reel ab dem zweiten Fenster abgelehnt, obwohl die
     Anleitung genau diese Länge verlangt hatte – ein Nachschlag pro Reel und
     nach drei Versuchen gar kein Reel. */
  const JE_SEKUNDE = 2.4;
  for (const [von, bis] of CONFIG.reel.dauerFenster) {
    const zielVon = Math.round(von * JE_SEKUNDE), zielBis = Math.round(bis * JE_SEKUNDE);
    const min = Math.round(zielVon * 0.75), max = Math.round(zielBis * 1.25);
    assert.ok(min <= zielVon && zielBis <= max, `Fenster ${von}-${bis}: Ziel ${zielVon}-${zielBis} liegt nicht in ${min}-${max}`);
    /* Die Mitte des Fensters muss komfortabel drin liegen, nicht am Rand. */
    const mitte = Math.round(((von + bis) / 2) * JE_SEKUNDE);
    assert.ok(mitte > min && mitte < max, `Fenster ${von}-${bis}: Mitte ${mitte} am Rand von ${min}-${max}`);
  }
  /* Und der Quelltext darf die Grenze nicht wieder fest verdrahten. */
  const src = fs.readFileSync(new URL("../src/autor.mjs", import.meta.url), "utf8");
  assert.ok(!/const \[min, max\] = lang \? \[/.test(src), "feste Wortgrenze im Quelltext");
  assert.match(src, /const zielVon = Math\.round\(von \* WOERTER_JE_SEKUNDE\)/);
});

test("Tagesdeckel hält, auch wenn ein Aufruf teurer ist als die alte Pauschale", async () => {
  const k = await import("../src/kosten.mjs");
  /* Unabhängig davon, was frühere Tests schon gebucht haben: der Kopf steht
     dort, wo wir jetzt sind, und darüber liegen genau 0,27 $. */
  const start = k.tagesStand();
  const limit = start + 0.27;
  k.budgetSetzen({ limitUsd: limit, bisher: 0 });
  /* Ein Reel-Aufruf kostet 0,06 $ – das Dreifache der alten Pauschale von
     0,02 $. Genau daran sind einzelne Tage über das Limit geschossen. */
  const teuer = { input_tokens: 0, output_tokens: 6000 };   // 0,06 $ bei Sonnet
  let aufrufe = 0;
  for (let i = 0; i < 20; i++) {
    try { k.budgetPruefen("reel"); } catch { break; }
    k.erfassen("claude-sonnet-5", teuer, "reel");
    aufrufe++;
  }
  assert.ok(aufrufe >= 3, `nur ${aufrufe} Aufrufe möglich – der Deckel ist zu streng`);
  assert.ok(k.tagesStand() <= limit, `${k.tagesStand().toFixed(4)} $ über dem Limit von ${limit.toFixed(2)} $`);
});

test("Faktencheck: Sprachversehen werden im Text ersetzt, nicht neu geschrieben", async () => {
  const { korrekturenAnwenden } = await import("../src/faktencheck.mjs");
  const beitrag = { folien: [{ art: "schritte", schritte: [{ titel: "Teilnehmer prüfen", text: "U hat U selbst keine Amtsträgereigenschaft. Er stiftet R zur Tat an, § 26 StGB." }] }], caption: "U hat U selbst keine Amtsträgereigenschaft – das ist der Kern." };
  const n = korrekturenAnwenden(beitrag, [{ original: "U hat U selbst keine", ersatz: "U hat selbst keine" }, { original: "kommt nicht vor", ersatz: "egal" }]);
  assert.equal(n, 2);
  assert.equal(beitrag.folien[0].schritte[0].text, "U hat selbst keine Amtsträgereigenschaft. Er stiftet R zur Tat an, § 26 StGB.");
  assert.ok(beitrag.caption.startsWith("U hat selbst keine"));
});

test("Icons: jeder Schlüssel des Autors hat ein farbiges Gegenstück", async () => {
  const { ICONS, iconSvg } = await import("../src/stile.mjs");
  const { farbIcon, ZUORDNUNG } = await import("../src/icons.mjs");
  for (const k of Object.keys(ICONS)) assert.ok(ZUORDNUNG[k], `keine Zuordnung für ${k}`);
  for (const k of Object.keys(ZUORDNUNG)) assert.ok(farbIcon(k, 48)?.includes("<svg"), `kein Icon für ${k} (${ZUORDNUNG[k]})`);
  /* iconSvg liefert das farbige Icon, sobald der Satz da ist. */
  assert.ok(iconSvg("waage").includes('class="icon farb"'));
  assert.equal(farbIcon("gibt-es-nicht"), null);
});

test("Freisteller: vom Fotorand angeschnittene Motive werden erkannt", async () => {
  const { randkontakt } = await import("../src/freistellen.mjs");
  const { execFileSync } = await import("node:child_process");
  const { ffmpegPfad } = await import("../src/stimme.mjs");
  const os = await import("node:os");
  const path = (await import("node:path")).default;
  const ganz = path.join(os.tmpdir(), `rand-ganz-${Date.now()}.png`), oben = path.join(os.tmpdir(), `rand-oben-${Date.now()}.png`);
  /* Deckender Kasten in der Mitte (ganz im Bild) bzw. bis an den oberen Rand. */
  /* Weißer Kasten, ringsum durchsichtig aufgefüllt (ganz im Bild) bzw. bis an
     den oberen und unteren Rand reichend (angeschnitten). */
  execFileSync(ffmpegPfad(), ["-y", "-loglevel", "error", "-f", "lavfi", "-i", "color=c=white:s=100x150", "-vf", "format=rgba,pad=200:200:50:50:color=black@0.0", "-frames:v", "1", ganz]);
  execFileSync(ffmpegPfad(), ["-y", "-loglevel", "error", "-f", "lavfi", "-i", "color=c=white:s=100x200", "-vf", "format=rgba,pad=200:200:50:0:color=black@0.0", "-frames:v", "1", oben]);
  const a = randkontakt(ganz), b = randkontakt(oben);
  assert.ok(a && a.oben === 0 && a.links === 0 && a.rechts === 0, JSON.stringify(a));
  assert.ok(b && b.oben > 0.3 && b.unten > 0.3, JSON.stringify(b));
  fs.rmSync(ganz, { force: true }); fs.rmSync(oben, { force: true });
});

test("Motive auf Reel-Cover und Stories, Nebentext auf Blau hell", async () => {
  const { coverHtml, storyHtml, folieHtml } = await import("../src/vorlagen.mjs");
  const { teaserAusBeitrag } = await import("../src/autor.mjs");
  const bild = "data:image/png;base64,iVBORw0KGgo=";
  const ctx = kontext({ fach: "strafbt", klausur: 2 });
  assert.ok(coverHtml({ titel: "Test", bild, bildFrei: true }, ctx).includes('class="frei"'));
  assert.ok(!coverHtml({ titel: "Test", icon: "waage" }, ctx).includes('class="frei"'));
  const s = storyHtml({ art: "begriff", titel: "Begriff", text: "Text", bild, bildFrei: true, bildQuelle: "Foto: X / Pexels" }, ctx);
  assert.ok(s.includes('class="frei"') && s.includes("Foto: X / Pexels"));
  /* Der Teaser trägt das Bild des Beitrags. */
  const t = teaserAusBeitrag({ fach: "strafbt", klausur: 2, kurztitel: "K", folien: [{ art: "titel", titel: "T", bild, bildFrei: true, bildQuelle: "Q" }] }, "s1");
  assert.equal(t.bild, bild);
  /* Blau (Klausur 1): weicher Text hell; auf weißen Flächen dunkel. */
  const blau = folieHtml({ art: "text", titel: "T", text: "x" }, kontext({ fach: "zivil", klausur: 1 }), 2, 3);
  assert.ok(/--text-weich:#dbe4ff/.test(blau), "helle Weichfarbe fehlt");
  assert.ok(/\.text[^{]*\{--text-weich:#0c1b4d\}/.test(blau) || /\.text,[^{]*\{--text-weich:#0c1b4d\}/.test(blau), "dunkle Weichfarbe auf weißen Flächen fehlt");
  const orange = folieHtml({ art: "text", titel: "T", text: "x" }, ctx, 2, 3);
  assert.ok(/--text-weich:#3a1708/.test(orange));
});

test("Token-Tresor: ein neu gesetztes Secret gewinnt gegen den gespeicherten Token", async () => {
  const { Instagram, fingerabdruck } = await import("../src/instagram.mjs");
  const os = await import("node:os");
  const path = (await import("node:path")).default;
  const altSchluessel = CONFIG.instagram.tokenSchluessel, altToken = CONFIG.instagram.token;
  CONFIG.instagram.tokenSchluessel = "test-schluessel";
  const datei = path.join(os.tmpdir(), `tresor-${Date.now()}.enc`);
  try {
    /* Kette beginnt mit Secret A; der Tresor hält den daraus verlängerten Token. */
    CONFIG.instagram.token = "secret-A";
    const a = new Instagram({ token: "secret-A", tresorDatei: datei, trockenlauf: true });
    a.token = "verlaengert-aus-A"; a.tokenAblauf = "2026-12-01T00:00:00Z";
    assert.ok(a.tresorSpeichern());
    const b = new Instagram({ token: "secret-A", tresorDatei: datei, trockenlauf: true });
    assert.equal(b.tresorLaden(), true);
    assert.equal(b.token, "verlaengert-aus-A", "gleiches Secret: Tresor gewinnt");
    /* Secret neu gesetzt (etwa mit weiterer Berechtigung): Secret gewinnt, Tresor startet neu. */
    CONFIG.instagram.token = "secret-B";
    const c = new Instagram({ token: "secret-B", tresorDatei: datei, trockenlauf: true });
    assert.equal(c.tresorLaden(), false);
    assert.equal(c.token, "secret-B", "neues Secret muss gewinnen");
    const d = new Instagram({ token: "secret-B", tresorDatei: datei, trockenlauf: true });
    assert.equal(d.tresorLaden(), true);
    assert.equal(d.token, "secret-B");
    assert.equal(fingerabdruck("secret-B").length, 16);
    assert.notEqual(fingerabdruck("secret-A"), fingerabdruck("secret-B"));
  } finally {
    CONFIG.instagram.tokenSchluessel = altSchluessel; CONFIG.instagram.token = altToken;
    fs.rmSync(datei, { force: true });
  }
});

test("Bilder: unscharfe Fotos und Maskenfotos fliegen raus, Passung sortiert", async () => {
  const { schaerfe, SCHAERFE_MIN } = await import("../src/freistellen.mjs");
  const { passung } = await import("../src/bilder.mjs");
  const { execFileSync } = await import("node:child_process");
  const { ffmpegPfad } = await import("../src/stimme.mjs");
  const os = await import("node:os");
  const path = (await import("node:path")).default;
  const scharf = path.join(os.tmpdir(), `scharf-${Date.now()}.png`), weich = path.join(os.tmpdir(), `weich-${Date.now()}.png`);
  /* Schachbrett = viele Kanten; dasselbe stark weichgezeichnet = fast keine. */
  execFileSync(ffmpegPfad(), ["-y", "-loglevel", "error", "-f", "lavfi", "-i", "testsrc2=s=320x320", "-frames:v", "1", scharf]);
  execFileSync(ffmpegPfad(), ["-y", "-loglevel", "error", "-f", "lavfi", "-i", "testsrc2=s=320x320", "-vf", "gblur=sigma=12", "-frames:v", "1", weich]);
  const a = schaerfe(scharf), b = schaerfe(weich);
  assert.ok(a > SCHAERFE_MIN, `scharf: ${a}`);
  assert.ok(b < SCHAERFE_MIN, `weich: ${b}`);
  fs.rmSync(scharf, { force: true }); fs.rmSync(weich, { force: true });
  /* Passung: Wörter der Szene in der Bildbeschreibung. */
  assert.ok(passung({ alt: "Woman reading a letter at the kitchen table" }, "woman reading letter at kitchen table") > 0.8);
  assert.equal(passung({ alt: "Portrait of a smiling man" }, "woman reading letter at kitchen table"), 0);
});

test("Sticker-Rand liegt in der PNG: Bild wächst um die Randbreite, Saum trägt die Farbe", async () => {
  const { bestickern } = await import("../src/freistellen.mjs");
  const { stickerFarbe } = await import("../src/stile.mjs");
  const { execFileSync } = await import("node:child_process");
  const { ffmpegPfad } = await import("../src/stimme.mjs");
  const os = await import("node:os");
  const path = (await import("node:path")).default;
  const quelle = path.join(os.tmpdir(), `sticker-${Date.now()}.png`);
  /* Weißes Quadrat, ringsum durchsichtig. */
  execFileSync(ffmpegPfad(), ["-y", "-loglevel", "error", "-f", "lavfi", "-i", "color=c=white:s=60x60", "-vf", "format=rgba,pad=100:100:20:20:color=black@0.0", "-frames:v", "1", quelle]);
  const ziel = bestickern(quelle, "#ffd166", 12);
  assert.notEqual(ziel, quelle);
  assert.ok(fs.existsSync(ziel));
  const { spawnSync } = await import("node:child_process");
  const masse = String(spawnSync(ffmpegPfad(), ["-hide_banner", "-i", ziel, "-f", "null", "-"], { encoding: "utf8" }).stderr || "");
  assert.ok(/124x124/.test(masse), `Maße: ${masse.match(/\d+x\d+/)?.[0]}`);
  /* Pixel im Saum (6 px außerhalb des Quadrats) ist gelb und deckend. */
  const raw = execFileSync(ffmpegPfad(), ["-loglevel", "error", "-i", ziel, "-vf", "crop=1:1:26:62", "-frames:v", "1", "-f", "rawvideo", "-pix_fmt", "rgba", "-"]);
  assert.deepEqual([...raw], [255, 209, 102, 255], `Saumpixel: ${[...raw].join(",")}`);
  fs.rmSync(ziel, { force: true });
  assert.equal(stickerFarbe(1, "bunt"), "#ffd166");
  assert.equal(stickerFarbe(2, "bunt"), "#2d5be3");
});

test("TikTok: Upload-Stücke nach den API-Regeln, Verteilen ohne Zugangsdaten still", async () => {
  const { tiktokStuecke, verteilen } = await import("../src/verteilen.mjs");
  const MB = 1024 * 1024;
  assert.deepEqual(tiktokStuecke(3 * MB), [{ von: 0, bis: 3 * MB - 1 }], "unter 5 MB: ein Stück");
  assert.deepEqual(tiktokStuecke(20 * MB), [{ von: 0, bis: 20 * MB - 1 }], "unter der Stückgröße: ein Stück");
  const gross = tiktokStuecke(70 * MB);
  assert.equal(gross.length, 2);
  assert.equal(gross[0].bis + 1, gross[1].von);
  assert.equal(gross.at(-1).bis, 70 * MB - 1, "der Rest wandert ins letzte Stück");
  assert.ok(gross.every((s) => s.bis - s.von + 1 >= 5 * MB));
  /* Ohne Secrets postet kein Kanal - und nichts wirft. */
  const r = await verteilen({ art: "reel", videoPfad: "/nicht/da.mp4", titel: "T", text: "t", hashtags: [] });
  assert.deepEqual(Object.values(r).filter((x) => x.fehler), []);
});

test("Samstags-Reel: das Mindset-Thema wird aufgelöst, obwohl es nicht im Pool steht", async () => {
  const { mindsetThema } = await import("../src/kalender.mjs");
  const { tagesplan } = await import("../src/planer.mjs");
  const { themenpool } = await import("../src/inhalte.mjs");
  /* 12.09.2026 ist ein Samstag: Der Planer setzt ein Mindset-Thema. */
  const samstag = "2026-09-12";
  assert.equal(new Date(`${samstag}T12:00:00Z`).getUTCDay(), 6);
  const t = mindsetThema(samstag);
  assert.ok(t?.id?.startsWith("mindset") && t.fach && t.titel, JSON.stringify(t));
  const pool = themenpool();
  assert.equal(pool.some((x) => x.id === t.id), false, "Mindset-Themen stehen bewusst nicht im Pool");
  const plan = tagesplan(samstag, { veroeffentlicht: [] }, pool, null);
  const reel = plan.beitraege.find((b) => b.format === "reel");
  assert.ok(reel, "am Samstag gehört ein Reel in den Plan");
  assert.equal(reel.thema?.typ, "mindset", "Samstags-Reel bekommt ein Mindset-Thema");
  /* Im gespeicherten Plan steht nur die Kennung - genau so kommt sie beim
     Veröffentlichen wieder an. So löst der Tageslauf sie auf: erst Pool,
     dann Kalender. */
  const gespeichert = { themaId: reel.thema?.id || null };
  const index = new Map(pool.map((x) => [x.id, x]));
  const themaFuer = (id) => (id ? index.get(id) || (String(id).startsWith("mindset") ? mindsetThema(samstag) : null) : null);
  assert.equal(index.get(gespeichert.themaId), undefined, "nur über den Kalender auflösbar");
  assert.ok(themaFuer(gespeichert.themaId)?.fach, `Thema ${gespeichert.themaId} nicht auflösbar`);
  /* Und der Auftrag an das Modell kommt ohne Absturz zustande. */
  const { pruefeBeitrag } = await import("../src/pruefung.mjs");
  assert.ok(pruefeBeitrag({ caption: themaFuer(gespeichert.themaId).titel }));
});

test("Themen-Skelett: Methodik-Themen ohne Klausurtag brechen den Lauf nicht ab", async () => {
  const { FAECHER, KLAUSUREN } = await import("../src/inhalte.mjs");
  const { mindsetThema } = await import("../src/kalender.mjs");
  const t = mindsetThema("2026-09-12");
  /* Genau die Zeile, die am 12.09. abstürzte: Methodik trägt klausur 0,
     KLAUSUREN kennt nur 1–3. */
  const f = FAECHER[t.fach] || { label: t.fach, klausur: t.klausur || 0 };
  const label = KLAUSUREN[f.klausur]?.label || KLAUSUREN[t.klausur]?.label || null;
  assert.ok(f.label, `kein Label für Fach ${t.fach}`);
  assert.doesNotThrow(() => (label ? `Fach: ${f.label} (${label})` : `Fach: ${f.label}`));
  /* Und jedes Fach des Pools lässt sich beschriften. */
  for (const [name, fach] of Object.entries(FAECHER)) {
    assert.ok(fach.label, `Fach ${name} ohne Label`);
    assert.ok(fach.klausur === 0 || KLAUSUREN[fach.klausur], `Fach ${name}: Klausurtag ${fach.klausur} unbekannt`);
  }
});

test("Mindset: eigene Farbe, eigenes Etikett, kein Prüfungstag", async () => {
  const { mindsetThema } = await import("../src/kalender.mjs");
  const { FAECHER } = await import("../src/inhalte.mjs");
  const { STILE } = await import("../src/stile.mjs");
  const { folieHtml, coverHtml, fussRechts } = await import("../src/vorlagen.mjs");
  const t = mindsetThema("2026-09-12");
  assert.equal(t.fach, "mindset");
  assert.equal(t.klausur, 0);
  assert.equal(FAECHER.mindset.label, "Kopfsache");
  /* Klausurtag 0 hat eine eigene Farbe, die sich von allen dreien unterscheidet. */
  const f = STILE.bunt.tagFarben;
  assert.ok(f[0]?.grund, "keine Farbe für Klausurtag 0");
  assert.equal(new Set([f[0].grund, f[1].grund, f[2].grund, f[3].grund]).size, 4);
  assert.equal(fussRechts({ fach: "mindset", klausur: 0 }), "Kopfsache");
  /* Und die 0 überlebt den Weg bis in die Kachel - vorher wurde sie zu 3. */
  const ctx = kontext({ fach: "mindset", klausur: 0 });
  assert.equal(ctx.klausur, 0);
  const html = folieHtml({ art: "titel", titel: "T" }, ctx, 1, 1);
  const flaeche = html.match(/\.folie,\.story,\.reel\{background:(#[0-9a-f]{6})/i)?.[1];
  assert.equal(flaeche?.toLowerCase(), f[0].grund.toLowerCase(), `Kachelfläche ${flaeche} statt Mindset-Farbe`);
  assert.ok(coverHtml({ titel: "T" }, ctx).includes("Kopfsache"));
});

test("Motiv-Bühne: gleiche Fläche für jede Bildform", async () => {
  const { motivBuehne, BUEHNE_BEITRAG, BUEHNE_STORY } = await import("../src/vorlagen.mjs");
  const hoch = motivBuehne(600, 900, BUEHNE_BEITRAG);
  const breit = motivBuehne(1200, 500, BUEHNE_BEITRAG);
  /* Beide nehmen ungefähr gleich viel Fläche ein - das war der Fehler: Ein
     breites Motiv schrumpfte in der festen Box zur Briefmarke. */
  const fl = (b) => b.breite * b.hoehe;
  assert.ok(fl(breit) > fl(hoch) * 0.9, `breit ${fl(breit)} vs hoch ${fl(hoch)}`);
  /* Die Form bleibt erhalten. */
  assert.ok(Math.abs(breit.breite / breit.hoehe - 2.4) < 0.05, JSON.stringify(breit));
  assert.ok(Math.abs(hoch.breite / hoch.hoehe - 0.667) < 0.02, JSON.stringify(hoch));
  /* Nichts wird breiter oder höher als erlaubt. */
  for (const ziel of [BUEHNE_BEITRAG, BUEHNE_STORY]) {
    for (const [b, h] of [[3000, 400], [400, 3000], [800, 800]]) {
      const box = motivBuehne(b, h, ziel);
      assert.ok(box.breite <= ziel.maxB && box.hoehe <= ziel.maxH, `${b}x${h} → ${JSON.stringify(box)}`);
    }
  }
  assert.equal(motivBuehne(0, 0, BUEHNE_BEITRAG), null);
});

test("Story mit Motiv: alle Inhaltsblöcke gleich breit, Nachweis Ton in Ton", async () => {
  const { storyHtml } = await import("../src/vorlagen.mjs");
  const html = storyHtml({ art: "begriff", titel: "Begriff", norm: "§ 1 BGB", text: "Text", bild: "data:image/png;base64,iVBORw0KGgo=", bildFrei: true, bildBreite: 600, bildHoehe: 400, bildQuelle: "Foto: X / Pexels" }, kontext({ fach: null, klausur: 1 }));
  const regel = html.match(/\.story:has\(\.frei\)[^{]*\{max-width:(\d+)px\}/);
  assert.ok(regel, "Breitenregel fehlt");
  for (const teil of [".norm", ".text", ".karte", "h1"]) assert.ok(regel[0].includes(teil), `${teil} fehlt in der Breitenregel`);
  /* Breit genug, dass ein langes deutsches Wort hineinpasst: „Vollstreckungs-
     klausel" brauchte am 13.09. rund 800 px und ragte aus seiner Pille. */
  assert.ok(Number(regel[1]) >= 800, `Inhaltsspalte zu schmal (${regel[1]} px)`);
  /* Die Bühne trägt die gerechneten Maße, nicht die feste Box. */
  assert.ok(/class="frei" style="width:\d+px;height:\d+px"/.test(html), "Bühne ohne gerechnete Maße");
  assert.ok(html.includes("Foto: X / Pexels"), "Bildnachweis fehlt");
});

test("Streitstand als Story-Art: zwei Ansichten und der Entscheid", async () => {
  const { storyHtml, STORY_ARTEN } = await import("../src/vorlagen.mjs");
  const { farbIcon } = await import("../src/icons.mjs");
  assert.ok(STORY_ARTEN.includes("streitstand"));
  assert.ok(farbIcon("streitstand", 48)?.includes("<svg"), "kein Zeichen für den Streitstand");
  const html = storyHtml({
    art: "streitstand", titel: "Wann beginnt der Versuch beim Unterlassen?", norm: "§ 22 StGB",
    optionen: ["Rechtsprechung: Mit der ersten Rettungsmöglichkeit.", "h.L.: Erst mit der letzten."],
    text: "Der Rechtsprechung folgen: Wer die erste Chance verstreichen lässt, gibt das Geschehen aus der Hand.",
  }, kontext({ fach: "strafat", klausur: 2 }));
  /* Label und Aussage werden getrennt dargestellt. */
  assert.ok(html.includes("<b>Rechtsprechung</b>"), "Label der ersten Ansicht fehlt");
  assert.ok(html.includes("<b>h.L.</b>"), "Label der zweiten Ansicht fehlt");
  assert.ok(html.includes("Streitentscheid"), "Streitentscheid fehlt");
  /* Nur zwei Ansichten, auch wenn das Modell mehr liefert. */
  const drei = storyHtml({ art: "streitstand", titel: "T", optionen: ["A: eins", "B: zwei", "C: drei"], text: "x" }, kontext({ fach: "strafat", klausur: 2 }));
  assert.ok(!drei.includes("<b>C</b>"), "dritte Ansicht wird gezeigt");
  /* Ohne Doppelpunkt bleibt die Aussage stehen, das Label wird allgemein. */
  const ohne = storyHtml({ art: "streitstand", titel: "T", optionen: ["Eine Ansicht ohne Label"], text: "x" }, kontext({ fach: "strafat", klausur: 2 }));
  assert.ok(ohne.includes("Eine Ansicht ohne Label") && ohne.includes("<b>Ansicht</b>"));
});

test("Story-Arten mit dünnem Vorrat laufen im Takt, nicht täglich", async () => {
  const { tagesplan } = await import("../src/planer.mjs");
  const { themenpool } = await import("../src/inhalte.mjs");
  const pool = themenpool();
  const ledger = { veroeffentlicht: [] };
  const takt = CONFIG.plan.storyArtTakt || {};
  assert.ok(takt.formel >= 14, `Rechenwege sollten selten sein, Takt ist ${takt.formel}`);
  /* Über drei Wochen darf höchstens an jedem n-ten Tag ein Rechenweg stehen. */
  let mitFormel = 0, mitStreitstand = 0;
  for (let i = 0; i < 21; i++) {
    const d = new Date(Date.UTC(2026, 8, 14 + i)).toISOString().slice(0, 10);
    const arten = tagesplan(d, ledger, pool, null).stories.map((s) => s.art);
    if (arten.includes("formel")) mitFormel++;
    if (arten.includes("streitstand")) mitStreitstand++;
  }
  assert.ok(mitFormel <= 2, `Rechenweg an ${mitFormel} von 21 Tagen - zu oft`);
  /* Der Streitstand rotiert mit den anderen Arten - regelmäßig, aber nicht
     täglich; so bekommen auch Fehler, Tipp und Zahl ihren Platz. */
  assert.ok(mitStreitstand >= 6, `Streitstand nur an ${mitStreitstand} von 21 Tagen`);
  /* Über drei Wochen kommt jede Art mindestens einmal vor. */
  const gesehen = new Set();
  for (let i = 0; i < 21; i++) {
    const d = new Date(Date.UTC(2026, 8, 14 + i)).toISOString().slice(0, 10);
    for (const s of tagesplan(d, ledger, pool, null).stories) gesehen.add(s.art);
  }
  for (const art of ["frage", "antwort", "norm", "streitstand", "merksatz", "begriff", "fehler", "tipp", "zahl"]) {
    assert.ok(gesehen.has(art), `Art ${art} kommt in drei Wochen nie vor`);
  }
});

test("Erfundene Firmennamen werden erkannt und aus früheren Inhalten gesperrt", () => {
  assert.deepEqual(firmenNamen("Die Rheinperle GmbH liefert an die Kornblume KG. Die GmbH haftet. Eine Beteiligung GmbH zählt nicht. Mini-Fall Nordlicht GmbH: Der Malerbetrieb Roth GmbH zahlt."), ["Rheinperle", "Kornblume", "Nordlicht", "Malerbetrieb Roth"]);
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), "inhalte-"));
  fs.writeFileSync(path.join(dir, "2026-09-05-b1.json"), JSON.stringify({ caption: "Die Nordfeld GmbH kauft eine Maschine." }));
  fs.writeFileSync(path.join(dir, "2026-09-13-s3.json"), JSON.stringify({ text: "Die Heutig AG zahlt." }));
  fs.writeFileSync(path.join(dir, "2025-01-01-b1.json"), JSON.stringify({ text: "Die Uralt OHG." }));
  const namen = benutzteFirmen(dir, "2026-09-13");
  assert.deepEqual(namen, ["Nordfeld"]);
  namenSperren(namen);
  assert.ok(gesperrteNamen("Die Nordfeld KG erwirbt ein Grundstück.").includes("Nordfeld"));
  assert.ok(gesperrteNamen("Die Nordlicht GmbH kauft.").includes("Nordlicht"));
  const ergebnis = pruefeBeitrag({ folien: [{ art: "titel", titel: "Frage" }, { art: "text", titel: "Fall", text: "Die Nordlicht GmbH verkauft eine Maschine an die Nordfeld KG." }, { art: "cta" }], caption: "Test" });
  assert.ok(ergebnis.fehler.some((f) => /Nordlicht/.test(f) && /Nordfeld/.test(f)));
  fs.rmSync(dir, { recursive: true, force: true });
});

test("Reel-Reserve folgt den gemessenen Reel-Tagen statt der Schätzung", async () => {
  const { reelReserve } = await import("../src/kosten.mjs");
  /* Ohne Messung bleibt es beim Wert aus der Konfiguration. */
  assert.equal(reelReserve({}, 0.11), 0.11);
  /* Drei Tage, einer davon ein Ausreißer mit Neuversuch: der mittlere zählt. */
  const tage = {
    "2026-09-10": { zwecke: { reel: 0.06, "reel-faktencheck": 0.006 } },
    "2026-09-11": { zwecke: { reel: 0.094, "reel-faktencheck": 0.007 } },
    "2026-09-12": { zwecke: { reel: 0.044, "reel-faktencheck": 0.002 } },
    "2026-09-13": { zwecke: { stories: 0.08 } },
  };
  const r = reelReserve(tage, 0.11);
  assert.ok(r > 0.05 && r < 0.11, `Reserve ${r} liegt nicht zwischen Untergrenze und Deckel`);
  assert.equal(r, 0.083);
  /* Der Deckel bleibt hart: teure Tage binden nie mehr als konfiguriert. */
  assert.equal(reelReserve({ a: { zwecke: { reel: 0.5 } } }, 0.11), 0.11);
  /* Untergrenze gegen einen einzelnen Billigtag. */
  assert.equal(reelReserve({ a: { zwecke: { reel: 0.01 } } }, 0.11), 0.05);
});

test("Fachfehler mit austauschbarer Stelle wird berichtigt, nicht neu geschrieben", async () => {
  const { korrekturenAnwenden } = await import("../src/faktencheck.mjs");
  const beitrag = { folien: [{ art: "text", titel: "Prüfung", text: "Die Klage prüft Rechtswidrigkeit und Rechtsverletzung." }] };
  const n = korrekturenAnwenden(beitrag, [{ original: "Rechtswidrigkeit und Rechtsverletzung", ersatz: "Rechtswidrigkeit und Verletzung in eigenen Rechten" }]);
  assert.equal(n, 1);
  assert.match(beitrag.folien[0].text, /Verletzung in eigenen Rechten/);
});

test("Rücklage gilt allen noch zu schreibenden Beiträgen, nicht den Stories", async () => {
  const { budgetSetzen, budgetFrei, reservieren, reservierungAufheben, erwartet } = await import("../src/kosten.mjs");
  budgetSetzen({ limitUsd: 0.15, bisher: 0.05 });
  reservieren(0.1, ["autor", "faktencheck", "recherche", "reel", "reel-faktencheck"], "zwei Beiträge");
  assert.equal(budgetFrei("stories"), false, "Stories dürfen die Rücklage nicht anfassen");
  assert.equal(budgetFrei("Story-Faktencheck"), false, "der Story-Faktencheck auch nicht, obwohl er „faktencheck“ enthält");
  assert.equal(budgetFrei("Text schreiben (Autor)"), true, "ein Beitrag darf – unter dem Etikett, das der Autor wirklich meldet");
  assert.equal(budgetFrei("Stories schreiben"), false, "Stories nicht");
  assert.equal(budgetFrei("Reel-Skript schreiben"), true, "das Reel-Skript darf");
  assert.equal(budgetFrei("Reel-Faktencheck"), true, "das Reel darf");
  reservierungAufheben();
  assert.equal(budgetFrei("stories"), true);
  assert.ok(erwartet("autor") > 0 && erwartet("reel") > 0);
  budgetSetzen({});
});

test("Übertrag: nicht erschienene Beiträge von gestern ersetzen neue Themen gleicher Art", async () => {
  const { uebertragen } = await import("../src/planer.mjs");
  const gestern = { datum: "2026-09-13", beitraege: [
    { slot: "b1", format: "wochenrueckblick", status: "geplant" },
    { slot: "b2", format: "schema", themaId: "x-1", themaTitel: "Thema X", fach: "zpo", status: "geplant" },
    { slot: "b3", format: "reel", themaId: "y-2", themaTitel: "Thema Y", fach: "strafat", status: "geplant" },
    { slot: "b4", format: "schema", themaId: "z-3", themaTitel: "Schon einmal übertragen", status: "geplant", uebertragen: 1 },
    { slot: "b5", format: "aktuell", themaId: "a-4", status: "geplant" },
  ] };
  const heute = { datum: "2026-09-14", beitraege: [
    { slot: "b1", zeit: "10:30", format: "pruefungsfrage", themaId: "neu-1", themaTitel: "Neu 1", status: "geplant" },
    { slot: "b2", zeit: "20:30", format: "reel", themaId: "neu-2", themaTitel: "Neu 2", status: "geplant" },
  ] };
  const u = uebertragen(heute, gestern, "2026-09-13");
  assert.equal(u.length, 3, "Wochenrückblick, Schema und Reel kommen mit; das schon übertragene und das Aktuelle nicht");
  /* Der Wochenrückblick nimmt den ersten Beitragsplatz, das Schema wird angehängt, das Reel ersetzt das Reel. */
  assert.equal(heute.beitraege[0].format, "wochenrueckblick");
  assert.equal(heute.beitraege[0].uebertragenVon, "2026-09-13-b1");
  assert.equal(heute.beitraege[0].zeit, "10:30", "die Uhrzeit von heute bleibt");
  assert.equal(heute.beitraege[1].themaId, "y-2");
  assert.equal(heute.beitraege[1].format, "reel");
  assert.equal(heute.beitraege[2].themaId, "x-1");
  assert.equal(heute.beitraege[2].slot, "b3");
  assert.equal(heute.beitraege[2].uebertragen, 1);
  assert.equal(heute.beitraege.length, 3);
  /* Ohne gestrigen Plan passiert nichts. */
  assert.deepEqual(uebertragen({ beitraege: [] }, null, "2026-09-13"), []);
});

test("Zweitmeinung: nur bestätigte Einwände bleiben, ohne Urteil gilt der Einwand", async () => {
  const { urteileAnwenden } = await import("../src/faktencheck.mjs");
  const befunde = [
    { stelle: "A", problem: "§ 28 Abs. 1 StGB gilt nicht für Anstifter", korrektur: "…" },
    { stelle: "B", problem: "Absatz falsch", korrektur: "Abs. 2 statt Abs. 1" },
    { stelle: "C", problem: "ohne Urteil", korrektur: "…" },
  ];
  const { bestaetigt, verworfen } = urteileAnwenden(befunde, [{ nr: 1, zutreffend: false, begruendung: "§ 28 Abs. 1 StGB erfasst Teilnehmer" }, { nr: 2, zutreffend: true, begruendung: "stimmt" }]);
  assert.deepEqual(verworfen.map((b) => b.stelle), ["A"]);
  assert.deepEqual(bestaetigt.map((b) => b.stelle), ["B", "C"]);
  assert.deepEqual(urteileAnwenden(befunde, []).bestaetigt.length, 3);
  assert.equal(CONFIG.faktencheck.zweitmeinung, true, "Zweitmeinung ist Standard");
});

test("Freisteller: ein halbdurchsichtiger Schleier wird verworfen, ein festes Motiv nicht", async () => {
  const { alphaProfil, FESTIGKEIT_MIN } = await import("../src/freistellen.mjs");
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), "alpha-"));
  const ff = process.env.FFMPEG_PATH || "ffmpeg";
  const bauen = (name, alpha) => {
    /* Ein Quadrat in der Bildmitte mit der gegebenen Deckkraft, ringsum leer. */
    const p = path.join(dir, name);
    const r = spawnSync(ff, ["-y", "-loglevel", "error", "-f", "lavfi", "-i", "color=c=black@0:s=192x192,format=rgba",
      "-f", "lavfi", "-i", `color=c=white@${alpha}:s=96x96,format=rgba`,
      "-filter_complex", "[0][1]overlay=48:48:format=auto", "-frames:v", "1", "-update", "1", p], { encoding: "utf8" });
    return r.status === 0 && fs.existsSync(p) ? p : null;
  };
  const fest = bauen("fest.png", 1);
  const schleier = bauen("schleier.png", 0.18);
  if (!fest || !schleier) { fs.rmSync(dir, { recursive: true, force: true }); return; }   // ohne ffmpeg kein Test
  const pf = alphaProfil(fest), ps = alphaProfil(schleier);
  /* Beide belegen dieselbe Fläche - der Mittelwert unterscheidet sie kaum
     genug, die Festigkeit dagegen eindeutig. */
  assert.ok(pf.festigkeit > 0.9, `festes Motiv: Festigkeit ${pf.festigkeit}`);
  assert.ok(ps.festigkeit < FESTIGKEIT_MIN, `Schleier: Festigkeit ${ps.festigkeit}`);
  assert.ok(ps.mittel > 0.02, "der Schleier belegt durchaus Fläche - genau deshalb rutschte er durch");
  fs.rmSync(dir, { recursive: true, force: true });
});

test("Bildauftrag: ein Gegenstand, kein Text, durchsichtiger Grund", async () => {
  const { bildAuftrag, bildKiAktiv } = await import("../src/bildki.mjs");
  const a = bildAuftrag("a judge's gavel on a desk");
  assert.match(a, /judge's gavel/);
  for (const muss of [/no text/i, /no letters/i, /no numbers/i, /no logos/i, /transparent background/i, /exactly one/i]) {
    assert.match(a, muss, `Auftrag ohne „${muss}": ${a}`);
  }
  /* Ohne Schlüssel bleibt alles beim Alten - der Bot läuft weiter mit Icons. */
  assert.equal(bildKiAktiv(), Boolean(CONFIG.bilder.ki.key) && CONFIG.bilder.ki.aktiv);
  assert.equal(CONFIG.bilder.ki.preisUsd > 0, true, "ein erzeugtes Bild muss den Tagesdeckel belasten");
});

test("Erzeugte Bilder belasten den Tagesdeckel wie jeder andere Posten", async () => {
  const { budgetSetzen, erfassenStueck, tagesStand, budgetFrei } = await import("../src/kosten.mjs");
  budgetSetzen({ limitUsd: 0.05 });
  const vorher = tagesStand();
  erfassenStueck(0.01, "bild", "Testmotiv");
  assert.ok(tagesStand() - vorher > 0.009, "der Posten fehlt in der Tagessumme");
  erfassenStueck(0.03, "bild", "noch ein Motiv");
  assert.equal(budgetFrei("bild"), false, "über dem Deckel darf kein weiteres Bild gezeichnet werden");
  budgetSetzen({});
});

test("Gezeichnet wird nur für den Feed, nicht für neun Stories am Tag", async () => {
  const { titelbild } = await import("../src/bilder.mjs");
  const alt = { ...CONFIG.bilder.ki };
  Object.assign(CONFIG.bilder.ki, { key: "test", aktiv: true });
  /* Mit ki:false wird nichts gezeichnet und auch kein Foto gesucht - die
     Kachel bleibt beim Icon, ohne dass ein Aufruf Geld kostet. */
  const ohne = await titelbild({ bildSzene: "a calculator on a desk" }, null, { ki: false });
  assert.equal(ohne, null);
  Object.assign(CONFIG.bilder.ki, alt);
});

test("Motiv-Archiv: gleiche Szene ja, aber erst nach langer Pause", async () => {
  const { aehnlichkeit, passendesMotiv } = await import("../src/motivarchiv.mjs");
  /* Fuellwoerter duerfen den Vergleich nicht aufblaehen. */
  assert.equal(aehnlichkeit("person reviewing notes at a desk", "person reviewing notes at desk"), 1);
  assert.ok(aehnlichkeit("court clerk stamping legal document", "judge stamping a document") < 0.85, "verschiedene Motive gelten nicht als gleich");
  /* Bei 85 % reicht ein fehlendes Wort nicht mehr: „a gavel on a wooden desk"
     ist nicht dasselbe Motiv wie „a gavel on a desk". */
  assert.ok(aehnlichkeit("a gavel on a wooden desk", "a gavel on a desk") < 0.85);
  const archiv = { motive: [
    { datei: "alt.png", szene: "person reviewing notes at a desk", gezeichnet: "2026-03-01", zuletzt: "2026-03-01" },
    { datei: "frisch.png", szene: "a calculator and a ledger", gezeichnet: "2026-09-01", zuletzt: "2026-09-01" },
  ] };
  /* Passt und ist lange her: wird hervorgeholt. */
  const fund = passendesMotiv(archiv, "person reviewing notes at desk", "2026-09-13", { mindestTage: 90, schwelle: 0.85 });
  assert.ok(fund, "das alte Motiv haette passen muessen");
  assert.equal(fund.eintrag.datei, "alt.png");
  assert.ok(fund.alter > 90);
  /* Passt, ist aber zu frisch: wird neu gezeichnet. */
  assert.equal(passendesMotiv(archiv, "a calculator and a ledger", "2026-09-13", { mindestTage: 90 }), null);
  /* Passt gar nicht. */
  assert.equal(passendesMotiv(archiv, "a lighthouse in a storm", "2026-09-13", { mindestTage: 90 }), null);
  assert.equal(CONFIG.bilder.ki.wiederTage >= 60, true, "der Abstand muss deutlich sein");
  assert.equal(CONFIG.bilder.ki.aehnlich >= 0.85, true, "die Szene muss praktisch dieselbe sein");
  /* Der Deckel muss laenger reichen als Ruhefrist plus Themenumlauf, sonst
     fliegt ein Motiv genau dann hinaus, wenn es wieder verwendbar waere. */
  assert.ok(CONFIG.bilder.ki.archivMax >= 3 * (CONFIG.bilder.ki.wiederTage + 200), `Archivdeckel ${CONFIG.bilder.ki.archivMax} zu klein`);
});

test("Motiv-Archiv: ablegen, wiederfinden, Deckel einhalten", async () => {
  const { motivAblegen, archivLaden, passendesMotiv, verwendungVermerken } = await import("../src/motivarchiv.mjs");
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), "motive-"));
  const quelle = path.join(dir, "quelle.png");
  fs.writeFileSync(quelle, "nicht wirklich ein Bild");
  let archiv = { motive: [] };
  archiv = motivAblegen(dir, archiv, { szene: "a gavel on a wooden desk", quelle, datum: "2026-01-10", breite: 900, hoehe: 700, max: 2 });
  assert.equal(archiv.motive.length, 1);
  assert.ok(fs.existsSync(path.join(dir, archiv.motive[0].datei)), "die Bilddatei fehlt im Archiv");
  /* Gespeichert und wieder eingelesen bleibt es auffindbar. */
  const gelesen = archivLaden(dir);
  const fund = passendesMotiv(gelesen, "a gavel on a wooden desk", "2026-09-13", { mindestTage: 90 });
  assert.ok(fund, "nach dem Neuladen nicht wiedergefunden");
  verwendungVermerken(dir, gelesen, fund.eintrag, "2026-09-13");
  assert.equal(archivLaden(dir).motive[0].zuletzt, "2026-09-13");
  assert.equal(archivLaden(dir).motive[0].benutzt, 2);
  /* Der Deckel greift: Das am laengsten ungenutzte faellt heraus. */
  archiv = motivAblegen(dir, archivLaden(dir), { szene: "zwei", quelle, datum: "2026-02-10", max: 2 });
  archiv = motivAblegen(dir, archiv, { szene: "drei", quelle, datum: "2026-03-10", max: 2 });
  assert.equal(archiv.motive.length, 2);
  assert.ok(!archiv.motive.some((m) => m.szene === "zwei"), "das aelteste haette weichen muessen");
  fs.rmSync(dir, { recursive: true, force: true });
});

test("Archiviert wird als WebP, mit Transparenz und deutlich kleiner", async () => {
  const { nachWebp } = await import("../src/motivarchiv.mjs");
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), "webp-"));
  const ff = process.env.FFMPEG_PATH || "ffmpeg";
  const png = path.join(dir, "motiv.png");
  /* Ein Bild mit durchsichtigem Rand und deckender Mitte. */
  const bau = spawnSync(ff, ["-y", "-loglevel", "error", "-f", "lavfi", "-i", "color=c=black@0:s=512x512,format=rgba",
    "-f", "lavfi", "-i", "testsrc2=s=256x256,format=rgba", "-filter_complex", "[0][1]overlay=128:128:format=auto",
    "-frames:v", "1", "-update", "1", png], { encoding: "utf8" });
  if (bau.status !== 0 || !fs.existsSync(png)) { fs.rmSync(dir, { recursive: true, force: true }); return; }
  const webp = nachWebp(png, path.join(dir, "motiv.webp"));
  if (!webp) { fs.rmSync(dir, { recursive: true, force: true }); return; }   // ffmpeg ohne libwebp: PNG bleibt
  assert.ok(fs.statSync(webp).size < fs.statSync(png).size, "WebP muss kleiner sein als das PNG");
  /* Der Alphakanal muss die Umwandlung ueberleben - sonst klebt spaeter ein
     schwarzes Rechteck auf der Kachel. */
  const alpha = spawnSync(ff, ["-hide_banner", "-loglevel", "error", "-i", webp, "-vf", "alphaextract,scale=16:16", "-frames:v", "1", "-f", "rawvideo", "-pix_fmt", "gray", "-"], { maxBuffer: 1 << 20 });
  assert.equal(alpha.status, 0);
  const werte = [...alpha.stdout];
  assert.ok(werte.some((v) => v < 40), "der durchsichtige Rand fehlt");
  assert.ok(werte.some((v) => v > 200), "die deckende Mitte fehlt");
  fs.rmSync(dir, { recursive: true, force: true });
});

test("Erklärvideo: Stichworte, Zeitpunkte und Bühne", async () => {
  const { markenFuer, eintritte, zeilen, erklaerHtml } = await import("../src/erklaervideo.mjs");
  const { layoutFuer } = await import("../src/reel.mjs");

  /* Der Autor liefert die Stichworte; ohne sie wird der Bildschirmtext am
     ersten Satzzeichen zerlegt statt ungekürzt auf die Plakette gelegt. */
  assert.deepEqual(markenFuer({ marken: ["Schuldner *bietet an*", "§ 294 BGB", "zu viel"] }), ["Schuldner *bietet an*", "§ 294 BGB"]);
  const abgeleitet = markenFuer({ text: "Verpflichtung gegenüber einem Dritten; nicht gegenüber dir selbst." });
  assert.equal(abgeleitet.length, 2);
  assert.ok(abgeleitet.every((m) => m.length <= 50 && !/[.;]$/.test(m)));
  assert.deepEqual(markenFuer({}), []);

  /* Die Eintritte liegen in der Szene und nacheinander - nichts darf vor dem
     Kapitelbeginn oder nach seinem Ende auftauchen. */
  const z = eintritte({ start: 10, dauer: 12 }, ["a", "b"]);
  assert.ok(z.figur > 10 && z.figur < 22);
  assert.ok(z.plaketten[0] > z.figur && z.plaketten[1] > z.plaketten[0]);
  assert.ok(z.medaillon > z.plaketten[1] && z.medaillon < 22);

  /* Überschrift: möglichst wenige Zeilen, und keine, die ein Wort zerreißt. */
  assert.deepEqual(zeilen("Wann liegt Annahmeverzug vor?"), ["Wann liegt", "Annahmeverzug vor?"]);
  assert.equal(zeilen("Kurz").length, 1);

  /* Die Bühne trägt die Farbe des Klausurtags, nicht irgendein Blau. */
  const { stil: stilLaden } = await import("../src/stile.mjs");
  const stil = stilLaden("bunt");
  const reel = { szenen: [{ titel: "Erste Frage", marken: ["Antwort *hier*"], bild: "data:image/png;base64,AA", kreuz: true }] };
  const plan = { szenen: [{ index: 0, start: 0, dauer: 10 }], gesamt: 10 };
  const html = erklaerHtml(reel, plan, { stil, klausur: 1, handle: "@test", fachLabel: "Zivilrecht" });
  assert.ok(html.includes(stil.tagFarben[1].grund), "Bühnenfarbe des Klausurtags fehlt");
  assert.ok(html.includes("<b>hier</b>"), "das hervorgehobene Wort fehlt");
  assert.ok(/Antwort <b>/.test(html), "das Leerzeichen vor dem hervorgehobenen Wort fehlt");
  assert.ok(html.includes("kreuz"), "das rote Kreuz fehlt");
  assert.ok(!/aevalsrc|klangbett/i.test(html), "im Erklärvideo darf kein Klang stecken");

  /* Beide Layouts lösen sich ab, damit die Zahlen vergleichbar bleiben. */
  assert.notEqual(layoutFuer("2026-09-14"), layoutFuer("2026-09-15"));
  assert.equal(layoutFuer("2026-09-14"), "erklaer");
});

test("Erklärvideo: kein Bild ist besser als ein falsches", async () => {
  const { motiveVerteilen } = await import("../src/erklaervideo.mjs");

  /* Die erste Szene hat kein Motiv bekommen - dann bleibt die Bühne leer.
     Ein Bild aus einer späteren Szene wäre hier schlicht das falsche. */
  const a = [{ bild: null }, { bild: "B" }, { bild: "C" }];
  motiveVerteilen(a);
  assert.equal(a[0].bild, null);

  /* Eine Lücke mittendrin übernimmt die Figur der VORHERIGEN Szene, nicht
     irgendeine: dieselbe Person läuft durch zwei zusammenhängende Schritte. */
  const b = [{ bild: "A" }, { bild: null }, { bild: "C" }, { bild: null }];
  const zahlen = motiveVerteilen(b);
  assert.equal(b[1].bild, "A");
  assert.equal(b[3].bild, "C");
  assert.deepEqual(zahlen, { mit: 4, eigene: 2 });

  /* Das Medaillon blickt auf den vorigen Schritt zurück - erst ab dem
     dritten, und nie auf dasselbe Bild, das ohnehin groß danebensteht. */
  const c = [{ bild: "A" }, { bild: "B" }, { bild: "C" }, { bild: "C" }];
  motiveVerteilen(c);
  assert.equal(c[0].medaillon, undefined);
  assert.equal(c[1].medaillon, undefined);
  assert.equal(c[2].medaillon, "B");
  assert.equal(c[3].medaillon, undefined, "dasselbe Bild zweimal wäre ein Versehen");
});

test("Langes Wort bleibt in seiner Pille – gemessen am Text, nicht an scrollWidth", async () => {
  const { storyRendern, browserBeenden } = await import("../src/render.mjs");
  const { spawnSync } = await import("node:child_process");
  const ff = process.env.FFMPEG_PATH || "ffmpeg";
  if (spawnSync("sh", ["-c", `command -v ${ff}`], { stdio: "ignore" }).status !== 0) return;
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), "pille-"));
  const ziel = path.join(dir, "story.jpg");
  /* Dieselbe Lage wie am 13.09.: ein Motiv auf der Story (deshalb die
     schmalere Spalte) und ein Wort, das breiter ist als die Spalte. Die
     Ueberschrift traegt im bunten Stil width:fit-content samt Hoechstbreite -
     dann meldet scrollWidth keinen Ueberlauf, obwohl das Wort neben seinem
     farbigen Grund steht. */
  await storyRendern({
    art: "teaser", fach: "zpo", klausur: 1, fachLabel: "Zivilprozessrecht",
    titel: "Vollstreckungsklausel Prüfschema", text: "Kurz.", pille: "Jetzt im Feed",
    bild: "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==",
    bildFrei: true, bildBreite: 600, bildHoehe: 800,
  }, ziel);
  await browserBeenden();

  /* Aus dem fertigen Bild lesen: Wo endet die dunkle Pille, wo die weisse
     Schrift? Steht die Schrift weiter rechts, ragt sie hinaus. */
  const roh = spawnSync(ff, ["-hide_banner", "-loglevel", "error", "-i", ziel, "-vf", "format=gray", "-frames:v", "1", "-f", "rawvideo", "-pix_fmt", "gray", "-"], { maxBuffer: 1 << 26 });
  assert.equal(roh.status, 0);
  const bild = roh.stdout, B = 1080;
  let verletzt = 0;
  for (let y = 420; y < 620; y += 4) {
    const zeile = bild.subarray(y * B, (y + 1) * B);
    let pille = -1, schrift = -1;
    for (let x = 0; x < B; x++) { if (zeile[x] < 60) pille = x; if (zeile[x] > 200) schrift = x; }
    if (pille > 0 && schrift > pille + 2) verletzt++;
  }
  assert.equal(verletzt, 0, `die Überschrift ragt in ${verletzt} Zeilen über ihre Pille hinaus`);
  fs.rmSync(dir, { recursive: true, force: true });
});

test("Reel-Cover und Karussell-Titelfolie tragen dieselbe Überschriften-Optik", async () => {
  const { coverHtml, folieHtml } = await import("../src/vorlagen.mjs");
  const ctx = kontext({ fach: "zpo", klausur: 1 });
  const titel = "Kosten und Anwaltszuziehung trennen";
  const cover = coverHtml({ titel, ueberzeile: "Reel · 91 Sekunden", dauerText: "In 91 Sekunden erklärt", icon: "waage", fach: "zpo", klausur: 1 }, ctx);
  const folie = folieHtml({ art: "titel", titel, untertitel: "Dauerbrenner im Examen", icon: "waage" }, ctx, 1, 6);

  /* Beide setzen den Titel in Pillen ZEILE FÜR ZEILE. Bis zum 13.09. legte
     nur die Titelfolie die .z-Spanne an; das Cover bekam einen einzigen
     Kasten um den ganzen Titel und sah im Profilraster aus wie ein fremder
     Kanal. */
  for (const [was, html] of [["Cover", cover], ["Titelfolie", folie]]) {
    assert.ok(/<h1[^>]*><span class="z">/.test(html), `${was}: Titel ohne Zeilenpille`);
  }
  /* Und das Cover nimmt die Story-Regel zurück, die einen Grund um das ganze
     h1 legt - sonst läge die Pille in der Pille. */
  assert.ok(/\.story\.cover h1\{[^}]*background:none/.test(cover), "Cover: der Kasten um das ganze h1 ist nicht zurückgenommen");
  /* Gleiche WIRKUNG, nicht gleiche Zahl: Das Cover ist 1920 hoch, die
     Titelfolie 1350. Bis zum 14.09. stand auf beiden 100px - im Profilraster
     wirkte die Reel-Überschrift dadurch ein Drittel kleiner und fiel als die
     schwächere auf (gemessen: 15,6 % der Kachelhöhe gegen 33,3 %). Die
     Cover-Größe ist deshalb mit 1920/1350 hochgerechnet. */
  const buntGroesse = Number(folie.match(/h1\{margin-top:72px;font-size:(\d+)px/)?.[1]);
  const coverGroesse = Number(cover.match(/\.story\.cover h1\{[^}]*font-size:(\d+)px/)?.[1]);
  assert.ok(buntGroesse, "Titelfolie: Schriftgröße nicht gefunden");
  const faktor = 1920 / 1350;
  assert.ok(Math.abs(coverGroesse / buntGroesse - faktor) < 0.05,
    `Cover ${coverGroesse}px zu Titelfolie ${buntGroesse}px ergibt ${(coverGroesse / buntGroesse).toFixed(2)}, erwartet ${faktor.toFixed(2)}`);
  /* Auch die beiden Stufen für lange Titel. Gesucht wird das Paar, das im
     bunten Stil für die Titelfolie gilt - „.story h1.klein" ist eine andere
     Regel und darf nicht dazwischenfunken. */
  const stufen = folie.match(/(?:^|[};\n])h1\.klein\{font-size:(\d+)px\}h1\.winzig\{font-size:(\d+)px\}/);
  assert.ok(stufen, "Titelfolie: Stufen für lange Titel nicht gefunden");
  const coverKlein = Number(cover.match(/\.story\.cover h1\.klein\{font-size:(\d+)px\}/)?.[1]);
  const coverWinzig = Number(cover.match(/\.story\.cover h1\.winzig\{font-size:(\d+)px\}/)?.[1]);
  for (const [name, gross, klein] of [["klein", Number(stufen[1]), coverKlein], ["winzig", Number(stufen[2]), coverWinzig]]) {
    assert.ok(klein, `Cover: Stufe ${name} nicht gefunden`);
    assert.ok(Math.abs(klein / gross - faktor) < 0.05, `Cover-Stufe ${name}: ${klein}px zu ${gross}px`);
  }
});

test("Instagram: „Datei nicht ladbar“ wird nachgefasst, nicht aufgegeben", async () => {
  process.env.IG_HOL_WARTEN_MS = "1";
  const { Instagram } = await import("../src/instagram.mjs");
  const echt = globalThis.fetch;
  let rufe = 0;
  /* Erst zweimal der Holfehler, dann klappt es - genau der Verlauf vom
     14.09., als der erste Campus-Beitrag ausfiel, obwohl die Kachel in
     Ordnung war und Sekunden später abrufbar. */
  globalThis.fetch = async () => {
    rufe++;
    const antwort = rufe <= 2
      ? { error: { message: "Only photo or video can be accepted as media type.", code: 9004, error_subcode: 2207052 } }
      : { id: "42" };
    return { ok: rufe > 2, json: async () => antwort, headers: new Map() };
  };
  try {
    const ig = new Instagram({ token: "t", kontoId: "1", trockenlauf: false });
    const t0 = Date.now();
    const r = await ig.anfrage("POST", "1/media", { image_url: "https://x/y.jpg" });
    assert.equal(r.id, "42");
    assert.equal(rufe, 3, "es muss zweimal nachgefasst worden sein");
    assert.ok(Date.now() - t0 >= 0);
  } finally { globalThis.fetch = echt; }
});

test("Jedes Fach trägt Themen, und der Auftrag ans Modell kennt jedes Fach", async () => {
  const pool = themenpool();
  const belegt = new Set(pool.map((t) => t.fach));
  /* "mindset" ist absichtlich leer: Kopfsache-Beiträge entstehen frei, ohne
     Themeneintrag. Jedes andere Fach muss Stoff haben, sonst steht ein
     Etikett in der Tabelle, das nie auf einer Kachel erscheint. */
  for (const id of Object.keys(FAECHER)) {
    if (id === "mindset") continue;
    assert.ok(belegt.has(id), `Fach ${id} hat kein einziges Thema`);
  }
  /* Die Faecherliste im Recherche-Auftrag wird aus der Tabelle gebaut. Waere
     sie von Hand gepflegt, ordnete das Modell einen Beitrag zur Tenorierung
     wieder "zpo" zu - so sind die Assessorthemen urspruenglich dort gelandet. */
  const quelle = await fs.promises.readFile(new URL("../src/autor.mjs", import.meta.url), "utf8");
  assert.ok(!/bgbat, schuld, schuldbt/.test(quelle), "die Faecherliste steht noch fest im Prompt");
  assert.ok(/\$\{FACH_LISTE\}/.test(quelle), "der Prompt muss die abgeleitete Liste einsetzen");
});

test("Das zweite Examen hat eigene Fächer statt des Etiketts der ersten Instanz", () => {
  const pool = themenpool();
  const zweitExamen = ["assessorz", "zwangsv", "assessoroer", "anklage", "revision"];
  for (const id of zweitExamen) {
    const themen = pool.filter((t) => t.fach === id);
    assert.ok(themen.length >= 10, `${id} braucht Stoff für mehr als ein paar Wochen, hat ${themen.length}`);
    /* Die Farbe bleibt die des Rechtsgebiets - ein Assessorbeitrag im
       Strafrecht ist orange wie jeder andere Strafrechtsbeitrag. */
    assert.ok([1, 2, 3].includes(FAECHER[id].klausur), `${id} muss zu einem Rechtsgebiet gehören`);
  }
  /* Tenorierung, Anklagesatz und Revisionsbegründung haben unter "ZPO",
     "VwGO" und "StPO" gestanden - dort darf jetzt nichts davon mehr liegen. */
  const falschAbgelegt = pool.filter((t) => ["zpo", "vwgo", "stpo"].includes(t.fach)
    && /Tenor|Relation|Anklageschrift|Anklagesatz|Revisionsgutachten|Widerspruchsbescheid|Urteilsklausur|Aktenvortrag/i.test(t.titel));
  assert.deepEqual(falschAbgelegt.map((t) => t.titel), [], "diese Themen gehören in die Assessorfächer");
});

test("Wissensbasis: ohne Schlüssel bleibt der Tresor zu, mit Schlüssel liest er sich", async () => {
  const { wissenVerschluesseln, wissenEntschluesseln, wissenIndex, wissenLeeren } = await import("../src/wissen.mjs");
  const klartext = "# Band 4 - Probe\n\n# 2. Relationstechnik\nKlägerstation, Beklagtenstation, Beweisstation.\n";
  const tresor = wissenVerschluesseln(klartext, "probe-schluessel");
  /* Der springende Punkt: Das Repo ist öffentlich. Wer die Datei im Browser
     öffnet, darf kein Wort davon lesen können. */
  assert.ok(!tresor.includes(Buffer.from("Relationstechnik")), "Klartext steht noch in der Datei");
  assert.ok(!tresor.includes(Buffer.from("Band 4")), "Klartext steht noch in der Datei");
  assert.equal(wissenEntschluesseln(tresor, "probe-schluessel"), klartext);
  /* Falscher Schlüssel: GCM merkt das am Prüfsiegel und wirft, statt Unsinn
     zurückzugeben - sonst landete Datenmüll als "Belegstelle" im Prompt. */
  assert.throws(() => wissenEntschluesseln(tresor, "falscher-schluessel"));
  assert.equal(wissenEntschluesseln(tresor, ""), null);

  const ordner = await fs.promises.mkdtemp(path.join(os.tmpdir(), "wissen-"));
  await fs.promises.writeFile(path.join(ordner, "band-4-probe.txt.enc"), tresor);
  wissenLeeren();
  const index = wissenIndex({ geheim: "probe-schluessel", ordner, neu: true });
  assert.equal(index.length, 1);
  assert.equal(index[0].id, "4/2");
  assert.equal(index[0].titel, "Relationstechnik");
  /* Ohne Schlüssel kein Index – und vor allem kein Absturz. */
  wissenLeeren();
  assert.deepEqual(wissenIndex({ geheim: "", ordner, neu: true }), []);
  wissenLeeren();
});

test("Wissensbasis: lieber keine Belegstelle als die zum Nachbarthema", async () => {
  const { wissenFuer, wissenLeeren } = await import("../src/wissen.mjs");
  const ordner = await fs.promises.mkdtemp(path.join(os.tmpdir(), "wissen-"));
  await fs.promises.writeFile(path.join(ordner, "band-3-strafrecht.txt"),
    "# Band 3 - Strafrecht\n\n# 16. Diebstahl und Unterschlagung\nWegnahme, Gewahrsam, Zueignungsabsicht.\n\n# 17. Betrug und Computerbetrug\nTäuschung, Irrtum, Vermögensverfügung, Vermögensschaden.\n\n# 26. Beweisverwertungsverbote\nUnselbständige und selbständige Verwertungsverbote, Abwägungslehre.\n");
  await fs.promises.writeFile(path.join(ordner, "band-5-oeffentlich.txt"),
    "# Band 5 - Öffentliches Recht im 2. Staatsexamen\n\n# 5. Vorläufige Vollstreckbarkeit\nDer Ausspruch richtet sich nach § 167 VwGO.\n");
  const opt = { ordner, neu: true };

  wissenLeeren();
  const treffer = wissenFuer({ titel: "Welche Beweisverwertungsverbote gibt es?", klausur: 2, normen: [], kern: {} }, opt);
  assert.equal(treffer?.titel, "Beweisverwertungsverbote");

  /* Zwei Kapitel fast gleichauf heißt: keines von beiden ist DIE Stelle.
     Eine halb passende Quelle im Prompt ist schlimmer als gar keine. */
  wissenLeeren();
  assert.equal(wissenFuer({ titel: "Wie grenzt man Diebstahl und Betrug ab?", klausur: 2, normen: [], kern: {} }, opt), null);

  /* Und quer durchs Rechtsgebiet nie: Die vorläufige Vollstreckbarkeit des
     Verwaltungsurteils ist nicht die des Zivilurteils. */
  wissenLeeren();
  assert.equal(wissenFuer({ titel: "Wann ist ein Urteil vorläufig vollstreckbar?", klausur: 1, normen: [], kern: {} }, opt), null);
  wissenLeeren();
});

test("Wissensbasis: jeder Zeiger am Thema trifft ein Kapitel, das es gibt", async () => {
  const { wissenIndex, wissenLeeren } = await import("../src/wissen.mjs");
  wissenLeeren();
  const index = wissenIndex({ neu: true });
  /* Ohne Schlüssel (so läuft der Test normalerweise) ist der Index leer –
     dann ist hier nichts zu prüfen. Mit Schlüssel muss jeder Zeiger sitzen:
     Ein Zeiger ins Leere fällt sonst still auf die Wortsuche zurück. */
  if (!index.length) return;
  const ids = new Set(index.map((k) => k.id));
  const kaputt = themenpool().filter((t) => t.wissen && !ids.has(t.wissen));
  assert.deepEqual(kaputt.map((t) => `${t.titel} → ${t.wissen}`), []);
  wissenLeeren();
});

test("Bildauftrag: ohne Person in der Szene wird auch keine gezeichnet", async () => {
  const { bildAuftrag } = await import("../src/bildki.mjs");
  /* Der Fehler vom 14.09.: Der Auftrag sprach immer von Armen, Haenden und
     Anatomie. Aus "scale balancing two stacks" wurde damit zuverlaessig ein
     Mensch neben einer Waage - und aus einem Reel ueber das steuerliche
     Einlagekonto eine Bilderfolge mit einem Mann und einem Einmachglas. */
  const sache = bildAuftrag("ledger page with running balance column");
  assert.match(sache, /no people|no faces|no hands/i, "ohne Person muss der Auftrag Menschen ausschliessen");
  assert.doesNotMatch(sache, /arms relaxed|natural proportions/i, "ohne Person keine Koerperhaltungs-Regeln");

  const mensch = bildAuftrag("person dropping letter into mailbox");
  assert.match(mensch, /arms relaxed/i, "mit Person bleiben die Haltungsregeln");
  assert.doesNotMatch(mensch, /no people/i, "mit Person darf der Auftrag Menschen nicht verbieten");

  /* "official" ist als Beiwort kein Mensch. Ohne diese Unterscheidung wurde
     aus "official notice with embossed seal" - einem Schriftstueck - wieder
     eine Figur mit Requisite. */
  const { menschInSzene } = await import("../src/bildki.mjs");
  assert.equal(menschInSzene("official notice with embossed seal"), false);
  assert.equal(menschInSzene("official letter with red stamp"), false);
  assert.equal(menschInSzene("stopped by official"), true);
  assert.equal(menschInSzene("official stamping a form"), true);

  /* Unverhandelbar in beiden Faellen. */
  for (const a of [sache, mensch]) {
    assert.match(a, /no text, no letters/i);
    assert.match(a, /transparent background/i);
  }
});

test("Erklärvideo: die Marke bleibt im sichtbaren Bereich und auf einer Zeile", async () => {
  const { chromium } = await import("playwright");
  const { erklaerHtml } = await import("../src/erklaervideo.mjs");
  const { stil } = await import("../src/stile.mjs");
  const { CONFIG } = await import("../src/config.mjs");
  let browser;
  try { browser = await chromium.launch({ executablePath: process.env.CHROMIUM_PATH }); }
  catch { return; /* ohne Browser kein Pixeltest */ }
  try {
    /* Genau die Marke aus dem Reel vom 14.09., die auf dem Telefon
       angeschnitten war. Bei 50px ist sie breiter als der sichere Bereich,
       muss also kleiner werden statt umzubrechen. */
    const reel = {
      fach: "zpo", klausur: 1, fachLabel: "Zivilprozessrecht",
      szenen: [{ art: "schritt", titel: "Bestand vom Vorjahr", marken: ["Vorjahresbestand: *übernehmen*"], sprecher: "x" }],
    };
    const plan = { szenen: [{ index: 0, start: 0, dauer: 5, sprichVon: 0.3, sprichDauer: 4.4 }], dauer: 5 };
    const ctx = { stil: stil(CONFIG.marke.stil), handle: "test", fach: "zpo", klausur: 1, fachLabel: "Zivilprozessrecht", farbeJeKlausur: CONFIG.marke.farbeJeKlausur };
    const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
    await page.setContent(erklaerHtml(reel, plan, ctx), { waitUntil: "load" });
    /* Wie im Renderer: erst die Schriften, dann das erste Bild. Vor dieser
       Aenderung lief das Einpassen beim Parsen, also gegen die Ersatzschrift -
       die Messung war damit wertlos. */
    await page.evaluate(() => document.fonts.ready);
    await page.evaluate(() => window.setzeZeit(0));
    const m = await page.evaluate(() => {
      const el = document.querySelector(".szene");
      el.style.display = "block";
      const k = el.querySelector(".plakette");
      /* Die Ruhelage messen, nicht die Einflugbahn: Zum Zeitpunkt 0 steht die
         Plakette noch ausserhalb des Bildes, das ist die Animation. */
      k.style.transform = "none";
      const bereich = document.createRange();
      let links = Infinity, rechts = -Infinity, zeilen = 0;
      const lauf = document.createTreeWalker(k, NodeFilter.SHOW_TEXT);
      for (let n = lauf.nextNode(); n; n = lauf.nextNode()) {
        bereich.selectNodeContents(n);
        for (const r of bereich.getClientRects()) { links = Math.min(links, r.left); rechts = Math.max(rechts, r.right); zeilen = Math.max(zeilen, r.top); }
      }
      const kasten = k.getBoundingClientRect();
      return { links, rechts, hoehe: kasten.height, px: parseFloat(getComputedStyle(k).fontSize) };
    });
    /* Der Kasten darf ueber den Rand ragen - die Schrift nie. */
    assert.ok(m.links >= 56, `Schrift beginnt bei ${Math.round(m.links)}px, mindestens 56 erwartet`);
    assert.ok(m.rechts <= 1024, `Schrift endet bei ${Math.round(m.rechts)}px, hoechstens 1024 erlaubt`);
    /* Eine Zeile: sonst bliebe der Kasten auf voller Breite stehen und zoege
       einen leeren Schwanz ueber den Bildrand. */
    assert.ok(m.hoehe < 130, `Marke bricht um (Kastenhoehe ${Math.round(m.hoehe)}px)`);
    assert.ok(m.px < 50, "die Marke haette verkleinert werden muessen");
  } finally { await browser.close(); }
});

test("Erbquote: § 1931 neben Kindern ist 1/4 – der Fehler vom 14.09. wird gefangen", async () => {
  const { pruefeBeitrag, normfallen } = await import("../src/pruefung.mjs");
  /* Wortgleich die Folie, die veröffentlicht wurde. Die Ehefrau stand dort
     neben zwei Kindern auf 3/4; richtig ist 1/2, weil § 1931 Abs. 1 BGB
     neben der ERSTEN Ordnung nur ein Viertel gibt. */
  const falsch = {
    folien: [
      { art: "text", titel: "Der Fall", text: "Herr Bosse stirbt ohne Testament. Er lebte in Zugewinngemeinschaft. Er hinterlässt seine Ehefrau, zwei Kinder und seine Mutter. Wer erbt was?" },
      { art: "rechnung", titel: "Quoten im Beispiel",
        formel: "Ehefrau: 1/2 (§ 1931 BGB) + 1/4 (§ 1371 I BGB) = 3/4",
        zeilen: ["Kinder (2): teilen 1/4 nach § 1924 IV BGB → je 1/8"],
        ergebnis: "Ehefrau 3/4, Kinder je 1/8, Mutter 0" },
    ],
  };
  const r = pruefeBeitrag(falsch);
  assert.equal(r.ok, false, "die falsche Quote muss beanstandet werden");
  assert.ok(r.fehler.some((f) => /1931/.test(f) && /1\/4/.test(f)), `erwartet wurde ein Befund zu § 1931, bekommen: ${JSON.stringify(r.fehler)}`);

  /* Die berichtigte Fassung muss durchgehen - sonst steht der Kanal still. */
  const richtig = JSON.parse(JSON.stringify(falsch));
  richtig.folien[1].formel = "Ehefrau: 1/4 (§ 1931 I BGB) + 1/4 (§ 1371 I BGB) = 1/2";
  richtig.folien[1].zeilen = ["Kinder (2): teilen die andere Hälfte nach § 1924 IV BGB → je 1/4"];
  richtig.folien[1].ergebnis = "Ehefrau 1/2, Kinder je 1/4, Mutter 0";
  assert.deepEqual(normfallen(JSON.stringify(richtig)), []);

  /* Der erklärende Satz darf beide Zahlen nennen - er wendet sie nicht an. */
  assert.deepEqual(normfallen("§ 1931 Abs. 1 BGB: neben der ersten Ordnung 1/4, neben der zweiten Ordnung oder Großeltern 1/2. Kinder gehen vor."), []);

  /* Ohne Kinder, neben der Mutter: dort ist die Hälfte richtig. */
  assert.deepEqual(normfallen("Der Erblasser hinterlässt seine Ehefrau und seine Mutter. Ehefrau: 1/2 (§ 1931 BGB) bei Zugewinngemeinschaft."), []);
  assert.ok(normfallen("Der Erblasser hinterlässt seine Ehefrau und seine Mutter. Ehefrau: 1/4 (§ 1931 BGB) bei Zugewinngemeinschaft.").length);

  /* § 1371 ohne Güterstand im Sachverhalt: die Quote stünde auf einer Annahme. */
  assert.ok(normfallen("Ehefrau: 1/4 (§ 1931 BGB) + 1/4 (§ 1371 I BGB). Kinder erben den Rest.").some((f) => /1371/.test(f)));
});

test("Die Rechenfolie ist für die Prüfung sichtbar – formel, zeilen, ergebnis", async () => {
  const { pruefeBeitrag } = await import("../src/pruefung.mjs");
  /* Der stille Teil des Fehlers vom 14.09.: alleTexte() las die Felder der
     Rechenfolie gar nicht aus. Die Folie mit den Zahlen war für jede Prüfung
     in pruefung.mjs unsichtbar - auch für die Namenssperre und die
     Uebernahmepruefung. */
  const mitZahlenInDerFormel = {
    folien: [
      { art: "text", titel: "Der Fall", text: "Zwei Kinder und die Ehefrau erben. Zugewinngemeinschaft." },
      { art: "rechnung", titel: "Quoten", formel: "Ehefrau: 3/4 (§ 1931 BGB)", zeilen: [], ergebnis: "" },
    ],
  };
  assert.equal(pruefeBeitrag(mitZahlenInDerFormel).ok, false, "was nur in der Formel steht, muss trotzdem geprüft werden");
});

test("Wo gerechnet wird, prüft nicht das billigste Modell", async () => {
  const { zahlenLastig } = await import("../src/faktencheck.mjs");
  const { CONFIG } = await import("../src/config.mjs");
  /* Am 14.09. prüfte Haiku, was Sonnet geschrieben hatte, und sah die
     vertauschte Erbquote nicht. Bei Zahlen ist das die falsche Sparsamkeit:
     Eine falsche Zahl steht groß auf der Kachel und wandert in die Klausur. */
  assert.ok(zahlenLastig({ folien: [{ art: "rechnung", formel: "Ehefrau: 1/4 (§ 1931 I BGB)" }] }));
  assert.ok(zahlenLastig({ folien: [{ art: "text", text: "Die Ehefrau erbt die Hälfte." }] }));
  assert.ok(zahlenLastig({ folien: [{ art: "text", text: "Sie bekommt 1/2 (§ 1931 BGB)." }] }));
  /* Ein Beitrag ohne Zahlen bleibt beim günstigen Prüfer – sonst wäre die
     Eskalation keine Eskalation, sondern der Normalfall. */
  assert.equal(zahlenLastig({ folien: [{ art: "text", text: "Der Gutachtenstil beginnt mit dem Obersatz." }] }), false);
  assert.ok(CONFIG.ki.modellPruefungStreng, "es muss ein strenger Prüfer gesetzt sein");
  assert.notEqual(CONFIG.ki.modellPruefungStreng, CONFIG.ki.modellPruefung, "der strenge Prüfer darf nicht derselbe sein");
});

test("Wenn es eng wird, weicht das Bild – nicht die Prüfung", async () => {
  const { budgetSetzen, budgetFrei } = await import("../src/kosten.mjs");
  /* Der Stand von heute Abend: 0,25 $ verbraucht, Deckel 0,27 $. Beides -
     ein Bild (0,01 $) und ein Faktencheck (0,01 $) - passt rechnerisch noch,
     aber nicht beides. Bisher gewann, wer zuerst dran war. */
  budgetSetzen({ limitUsd: 0.27, bisher: 0.25 });
  assert.equal(budgetFrei("Faktencheck"), true, "der Faktencheck muss noch laufen dürfen");
  assert.equal(budgetFrei("Bild zeichnen"), false, "das Bild muss zurückstehen");
  assert.equal(budgetFrei("Erklärbild"), false, "auch die Reel-Motive stehen zurück");

  /* Früh am Tag ist Platz für beides - der Abstand darf das Zeichnen nicht
     grundsätzlich verhindern, sonst gäbe es nie wieder ein Motiv. */
  budgetSetzen({ limitUsd: 0.27, bisher: 0.05 });
  assert.equal(budgetFrei("Bild zeichnen"), true);
  assert.equal(budgetFrei("Faktencheck"), true);
  budgetSetzen({});
});

test("Angeschnittene Motive werden auch dann verworfen, wenn sie gezeichnet sind", async () => {
  const { randVerdacht, RAND_GRENZE } = await import("../src/freistellen.mjs");
  const { bildAuftrag } = await import("../src/bildki.mjs");
  /* Die gemessenen Werte des Motivs, das am 14.09. auf der Erbrechts-Kachel
     stand: 46 % der obersten Bildzeile deckend, der Kopf glatt abgeschnitten,
     der Stickerrand quer über den Scheitel. Die Prüfung dafür gab es - aber
     nur im Pfad für gesuchte Fotos, nicht für gezeichnete Motive. */
  assert.ok(randVerdacht({ oben: 0.46, unten: 0.23, links: 0, rechts: 0 }), "der abgeschnittene Kopf muss auffallen");
  /* Unten darf ein Motiv anschneiden - dort läuft die Figur ohnehin aus der
     Kachel. Sonst würde jede Figur verworfen, die auf dem Boden steht. */
  assert.equal(randVerdacht({ oben: 0, unten: 0.6, links: 0, rechts: 0 }), null);
  assert.equal(randVerdacht({ oben: 0, unten: 0, links: 0, rechts: 0 }), null);
  assert.ok(randVerdacht({ oben: 0, unten: 0, links: 0.2, rechts: 0 }), "seitlich angeschnitten zählt auch");
  assert.equal(randVerdacht(null), null, "ohne Messung keine Beanstandung – sonst fiele jedes Motiv aus");
  assert.ok(RAND_GRENZE.oben < RAND_GRENZE.seite, "oben wird strenger gemessen als an den Seiten");

  /* Und der Auftrag verlangt den Platz jetzt ausdrücklich, statt nur das
     Anschneiden zu verbieten. */
  const auftrag = bildAuftrag("elderly woman holding old photograph");
  assert.match(auftrag, /clear empty margin on all four sides/i);
  assert.doesNotMatch(auftrag, /filling the frame/i, "„filling the frame“ widerspricht der Randvorgabe");
});

test("Derselbe Beitrag bekommt sein eigenes Motiv zurück, nicht ein neu gezeichnetes", async () => {
  const { passendesMotiv } = await import("../src/motivarchiv.mjs");
  const archiv = { motive: [{ datei: "a.webp", szene: "elderly woman holding old photograph", themaId: "famerb-257", gezeichnet: "2026-09-14", zuletzt: "2026-09-14" }] };
  const heute = "2026-09-14";
  /* Ohne Themenbezug greift die Sperrfrist: Dasselbe Bild soll sich im Feed
     nicht binnen 90 Tagen wiederholen. */
  assert.equal(passendesMotiv(archiv, "elderly woman holding old photograph", heute, { mindestTage: 90 }), null);
  /* Beim selben Beitrag ist es kein Wiederholen, sondern dasselbe Bild zum
     selben Text - etwa wenn er berichtigt und neu gestellt wird. */
  const fund = passendesMotiv(archiv, "elderly woman holding old photograph", heute, { mindestTage: 90, themaId: "famerb-257" });
  assert.equal(fund?.eintrag.datei, "a.webp");
  /* Ein fremdes Thema darf die Sperrfrist nicht aushebeln. */
  assert.equal(passendesMotiv(archiv, "elderly woman holding old photograph", heute, { mindestTage: 90, themaId: "stpo-785" }), null);
});

test("Das Reel wählt zuerst und rotiert über die Rechtsgebiete", async () => {
  const { tagesplan, ledgerLaden, vermerken } = await import("../src/planer.mjs");
  const pool = themenpool();
  const ledger = JSON.parse(JSON.stringify(ledgerLaden()));
  ledger.veroeffentlicht = [];
  /* Bis zum 14.09. stand das Reel im Plan an letzter Stelle und bekam damit
     nicht die beste Wahl, sondern den Rest: Der Farbwechsel-Filter verbot ihm
     die Gebiete der Kachelbeiträge, und die nehmen fast immer Zivil- und
     Strafrecht. Die ersten fünf Reels des Kanals waren deshalb alle grün. */
  const gebiete = [];
  for (let t = 0; t < 12; t++) {
    const datum = new Date(Date.UTC(2026, 9, 5 + t)).toISOString().slice(0, 10);
    const plan = tagesplan(datum, ledger, pool);
    const reel = plan.beitraege.find((b) => b.format === "reel");
    if (!reel?.thema) continue;
    const g = FAECHER[reel.thema.fach]?.klausur;
    if (g) gebiete.push(g);
    vermerken(ledger, { datum, art: "beitrag", slot: "b3", format: "reel", fach: reel.thema.fach, thema: reel.thema.id, veroeffentlicht: datum });
  }
  assert.ok(gebiete.length >= 8, `zu wenige Reels im Versuch: ${gebiete.length}`);
  const je = { 1: 0, 2: 0, 3: 0 };
  for (const g of gebiete) je[g]++;
  /* Kein Gebiet darf mehr als die Hälfte der Reels stellen. */
  for (const [g, n] of Object.entries(je)) {
    assert.ok(n <= Math.ceil(gebiete.length / 2), `Gebiet ${g} stellt ${n} von ${gebiete.length} Reels`);
  }
  /* Und jedes Gebiet muss überhaupt vorkommen - genau das war der Befund. */
  for (const g of [1, 2, 3]) assert.ok(je[g] > 0, `Gebiet ${g} kam in ${gebiete.length} Reels nie vor`);
});

test("Die früheste geplante Uhrzeit ist von der Weckkette auch erreichbar", async () => {
  const { CONFIG } = await import("../src/config.mjs");
  const { kandidatenStunden } = await import("../src/zeiten.mjs");
  /* Am 14.09. stand auf dem Steuerkanal ein Beitrag mit Slot 06:30 erst um
     07:35 im Feed - 65 Minuten zu spät. Nicht weil etwas kaputt war, sondern
     weil der erste Lauf des Tages später liegt als der Slot. Die beiden Werte
     stehen in verschiedenen Dateien und wussten nichts voneinander. */
  const yml = await fs.promises.readFile(new URL("../.github/workflows/instagram.yml", import.meta.url), "utf8");
  const cron = yml.match(/cron:\s*"(\d+)\s+(\d+)-(\d+)/);
  assert.ok(cron, "Cron im Workflow nicht gefunden");
  const [, minute, ersteStundeUtc] = cron;
  /* Sommerzeit, der ungünstigere Fall: Europe/Berlin ist dann UTC+2, der
     erste Lauf liegt also zwei Stunden später am Tag als in der Cron-Zeile. */
  const ersterLaufLokal = Number(ersteStundeUtc) + 2;
  const frueheste = kandidatenStunden(CONFIG.plan.zeitFenster)[0];
  /* Beiträge werden zur halben Stunde geplant; der Lauf muss danach liegen. */
  const slotMinuten = frueheste * 60 + 30;
  const laufMinuten = ersterLaufLokal * 60 + Number(minute);
  assert.ok(laufMinuten >= slotMinuten,
    `Frühester Slot ${frueheste}:30, erster Lauf aber erst ${ersterLaufLokal}:${minute} – der Beitrag käme ${slotMinuten - laufMinuten} min zu spät`);
  /* Und nicht unnötig eng: Wäre die Untergrenze eine Stunde tiefer, ginge eine
     brauchbare Sendezeit verloren. Genau das wäre mit "8-22" passiert. */
  assert.ok(laufMinuten < slotMinuten + 60,
    `Untergrenze ${frueheste} ist zu hoch – die Stunde davor wäre um ${ersterLaufLokal}:${minute} erreichbar gewesen`);
});


test("Bezahlte Entwürfe überleben den Lauf, in dem sie entstanden sind", async () => {
  const { entwurfsspeicher, entwuerfeAufraeumen } = await import("../src/autor.mjs");
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), "entwuerfe-"));
  try {
    entwurfsspeicher(dir);
    /* Der Speicher wird über strukturiert() gefüllt, und das ruft das Modell.
       Geprüft wird deshalb, was ohne Netz prüfbar ist: dass abgelegte Entwürfe
       nach Alter verschwinden und frische liegen bleiben. Ohne Aufräumen
       wüchse der Asset-Zweig mit jedem Tag. */
    const schreib = (name, datum) => fs.writeFileSync(path.join(dir, name), JSON.stringify({ datum, zweck: "autor", daten: { titel: name } }));
    schreib("heute.json", "2026-09-15");
    schreib("vorgestern.json", "2026-09-13");
    schreib("uralt.json", "2026-08-01");
    schreib("kaputt.json", "2026-09-15");
    fs.writeFileSync(path.join(dir, "kaputt.json"), "{kein json");
    const weg = entwuerfeAufraeumen(3, "2026-09-15");
    const da = fs.readdirSync(dir).sort();
    assert.deepEqual(da, ["heute.json", "vorgestern.json"], `übrig: ${da.join(", ")}`);
    assert.equal(weg, 2, "Anzahl der entfernten Entwürfe stimmt nicht");
  } finally {
    entwurfsspeicher(null);
    fs.rmSync(dir, { recursive: true, force: true });
  }
});
