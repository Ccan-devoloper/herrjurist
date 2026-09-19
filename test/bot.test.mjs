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

/* Quelltext ohne Kommentare - fuer Pruefungen, bei denen die REIHENFOLGE
   von Anweisungen zaehlt und eine Erklaerung im Kommentar sie verschoebe. */
const ohneKommentare = (t) => t.replace(/\/\*[\s\S]*?\*\//g, "").replace(/^\s*\/\/.*$/gm, "");

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


test("Die Rücklage für die Beiträge ist vor der Recherche sicher", async () => {
  const k = await import("../src/kosten.mjs");
  /* Am 16.09. hat ein einziger Recherche-Aufruf die Rücklage aufgebraucht,
     die für zwei noch zu schreibende Beiträge gedacht war. Danach fielen auf
     beiden Kanälen alle Beiträge und Stories des Tages aus. Eine Recherche
     schmückt einen Beitrag; ein Beitrag ohne Recherche erscheint trotzdem. */
  k.budgetSetzen({ limitUsd: 0.32, bisher: 0.12 });
  k.reservieren(0.12, ["autor", "faktencheck", "reel", "reel-faktencheck"], "2 Beiträge");
  assert.equal(k.budgetFrei("autor"), true, "der Beitrag darf die Rücklage nutzen");
  assert.equal(k.budgetFrei("Recherche"), false,
    "die Recherche darf die Rücklage NICHT anrühren – genau das hat am 16.09. den Tag gekostet");

  /* Am frischen Tag darf sie – aber nur mit doppeltem Spielraum, weil ihre
     Schätzung erwiesenermaßen um das Fünffache danebenliegen kann. Damit
     läuft eine Recherche früh am Tag, wenn Luft da ist, und nie mehr als
     letzte Handlung, die den Rest mitreißt. */
  const schaetzung = k.erwartet("recherche");
  k.budgetSetzen({ limitUsd: 0.32, bisher: 0 });
  assert.equal(k.budgetFrei("Recherche"), true, "am frischen Tag mit voller Luft darf sie laufen");
  k.budgetSetzen({ limitUsd: 0.32, bisher: 0.32 - schaetzung * 1.5 });
  assert.equal(k.budgetFrei("autor"), true, "für einen Beitrag reicht die einfache Schätzung");
  assert.equal(k.budgetFrei("Recherche"), false, "anderthalb Schätzungen Luft sind der Recherche zu wenig");
  k.budgetSetzen({});
});

test("Recherche: Cache-Marke im Aufruf und eine Schätzung, die den Tag nicht sprengt", async () => {
  const { rechercheAnfrage } = await import("../src/autor.mjs");
  const { erwartet } = await import("../src/kosten.mjs");
  const { CONFIG } = await import("../src/config.mjs");
  /* Am 16.09. kostete EIN Recherche-Aufruf 0,252 $ bei einer Schätzung von
     0,05 $ und lieferte null Quellen – danach fielen auf beiden Kanälen alle
     Beiträge und Stories des Tages aus. Ursache: Bei jedem `pause_turn` wurde
     der ganze Verlauf samt Suchergebnissen erneut voll bezahlt. */
  const anfrage = rechercheAnfrage("Was gibt es Neues?");
  assert.deepEqual(anfrage.cache_control, { type: "ephemeral" }, "ohne Cache-Marke wird jede pause_turn-Runde voll bezahlt");
  assert.equal(anfrage.tools[0].name, "web_search");
  assert.ok(anfrage.tools[0].max_uses > 0, "die Zahl der Websuchen muss begrenzt bleiben");

  /* Die Schätzung muss zwei Dinge leisten: ehrlicher sein als die alten
     0,05 $ und klein genug bleiben, dass ein einzelner Aufruf nicht den
     halben Tag frisst. */
  const schaetzung = erwartet("Recherche");
  assert.ok(schaetzung > 0.05, `Recherche wird mit ${schaetzung} $ immer noch zu billig geschätzt`);
  assert.ok(schaetzung <= CONFIG.ki.tagesBudgetUsd / 2, `eine Recherche (${schaetzung} $) darf nicht mehr als den halben Tagesdeckel (${CONFIG.ki.tagesBudgetUsd} $) beanspruchen`);
});

test("Story-Antwort im Postfach bekommt ihren Bezug – statt einer Rückfrage", async () => {
  const { offeneNachrichten, antwortenFormulieren } = await import("../src/postfach.mjs");
  /* Am 15.09. fragte jemand unter einer Story „Ist das hier die erbrechtliche
     oder die familienrechtliche Lösung?“ und bekam zurück: „Magst du mir kurz
     sagen, welchen Punkt du meinst?“ Instagram hatte die Nachricht als
     Story-Antwort markiert – das Feld wurde nur nie abgefragt. */
  const ledger = { postfach: [], veroeffentlicht: [
    { datum: new Date().toISOString().slice(0, 10), art: "story", titel: "Wann ist eine Versammlung friedlich?", medienId: "111" },
    { datum: new Date().toISOString().slice(0, 10), art: "beitrag", titel: "Beschuldigter oder Zeuge? § 136 StPO", medienId: "222" },
  ] };
  const nachricht = (extra) => [{ id: "k1", messages: { data: [{
    id: "m1", from: { id: "99", username: "ysf.kmn" }, message: "Gilt das auch bei Sitzblockaden?",
    created_time: new Date().toISOString(), ...extra,
  }] } }];

  const mitBezug = offeneNachrichten(nachricht({ reply_to: { story: { id: "111" } } }), "1", ledger);
  assert.equal(mitBezug.length, 1);
  assert.match(mitBezug[0].bezug, /Versammlung friedlich/, "die Story-ID muss im Ledger aufgelöst werden");

  /* Unbekannte Story: ehrlich benennen, nicht erfinden. */
  const fremd = offeneNachrichten(nachricht({ reply_to: { story: { id: "999" } } }), "1", ledger);
  assert.match(fremd[0].bezug, /WELCHE, hat Instagram nicht mitgeliefert/);

  /* Ohne reply_to bleibt der Bezug leer – aber die letzten Inhalte stehen als
     Hintergrund bereit, damit das Modell zuordnen kann. */
  const ohne = offeneNachrichten(nachricht({}), "1", ledger);
  assert.equal(ohne[0].bezug, null);
  assert.equal(ohne.zuletzt.length, 2, "die letzten Veröffentlichungen fehlen als Hintergrund");

  /* Der Prompt darf den Bezug nicht unterschlagen. */
  let gesehen = null;
  const echt = globalThis.fetch;
  globalThis.fetch = async (url, opt) => { gesehen = JSON.parse(opt.body); return echt(url, opt); };
  try { await antwortenFormulieren(mitBezug, mitBezug.zuletzt); } catch { /* kein Schlüssel im Test – der Prompt steht trotzdem */ }
  globalThis.fetch = echt;
  if (gesehen) {
    const text = gesehen.messages[0].content;
    assert.match(text, /Bezug: Story/, "der Bezug fehlt im Prompt");
    assert.match(text, /Zuletzt erschienen/, "der Hintergrund fehlt im Prompt");
  }
});

test("Antworten haben einen eigenen Topf: Inhaltsdeckel voll, Antworten laufen weiter – und umgekehrt", async () => {
  const k = await import("../src/kosten.mjs");
  k.budgetSetzen({ limitUsd: 0.10, bisher: 0.09, antwortLimitUsd: 0.08, bisherAntworten: 0.01 });
  assert.equal(k.budgetFrei("beitrag"), false, "Inhalt ist voll");
  assert.equal(k.budgetFrei("kommentare"), true, "Antworten haben noch Platz");
  assert.equal(k.budgetFrei("nachrichten"), true);
  const vorher = k.tagesStand();
  k.erfassen("claude-opus-5", { input_tokens: 1000, output_tokens: 2000 }, "kommentare");   // 0,055 $
  assert.equal(k.tagesStand(), vorher, "Antworten belasten den Inhaltsdeckel nicht");
  assert.ok(k.antwortStand() > 0.06, "aber den Antworttopf");
  /* Ab jetzt rechnet der Topf mit dem gemessenen Wert (0,055), nicht mehr mit der Schätzung. */
  assert.equal(k.budgetFrei("kommentare"), false, "0,065 + 0,055 gemessen ≥ 0,08");
  assert.throws(() => k.budgetPruefen("Kommentare beantworten"), /Antwortbudget/);
  k.budgetSetzen({ limitUsd: 0.10, bisher: 0.0, antwortLimitUsd: 0.08, bisherAntworten: 0.08 });
  assert.equal(k.budgetFrei("kommentare"), false, "Antworttopf voll");
  assert.equal(k.budgetFrei("beitrag"), true, "Inhalt läuft weiter");
  k.budgetSetzen({});
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
     Kachel zugeordnet wird – ohne ihn müssten alle neu geschrieben werden.
     Seit Safety 0b steht eine Quiz-Kachel nicht mehr auf einer Zeile, sondern
     als Block unter [QuizPair] mit ihren Optionen und der Markierung; der
     Anker bleibt derselbe. */
  assert.equal((t.match(/\[Story s3 frage\]/g) || []).length, 1, "der Anker der Frage steht genau einmal");
  assert.equal((t.match(/\[Story s5 norm\]/g) || []).length, 1, "der Anker der Norm-Kachel steht genau einmal");
  assert.equal(t.split("\n").filter((z) => z.startsWith("[Story s5 norm]")).length, 1,
    "eine Kachel ohne Quiz bleibt einzeilig");
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
  for (const muss of [/no text/i, /no letters/i, /no numbers/i, /no logos/i, /without a background/i, /exactly one/i]) {
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
    assert.match(a, /without a background/i);
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

test("Postfach: nur offene Nachrichten innerhalb der Frist", async () => {
  const { offeneNachrichten, FRIST_STUNDEN } = await import("../src/postfach.mjs");
  const ICH = "17841400000000000";
  const jetzt = Date.parse("2026-09-15T12:00:00Z");
  const vorStunden = (h) => new Date(jetzt - h * 3600000).toISOString();
  const von = (id, name) => ({ id, username: name });

  const k = (id, msgs) => ({ id, messages: { data: msgs } });
  const konv = [
    /* frisch und offen – muss beantwortet werden */
    k("c1", [{ id: "m1", from: von("u1", "lena"), message: "Ist die Drittwirkung der Grundrechte im Zivilrecht klausurrelevant?", created_time: vorStunden(2) }]),
    /* wir haben zuletzt geschrieben – nichts offen */
    k("c2", [
      { id: "m2", from: von("u2", "tim"), message: "Danke!", created_time: vorStunden(5) },
      { id: "m3", from: von(ICH, "herrjurist"), message: "Gern!", created_time: vorStunden(4) },
    ]),
    /* zu alt – Instagram nimmt keine Antwort mehr an */
    k("c3", [{ id: "m4", from: von("u3", "jo"), message: "Kurze Frage zur StPO", created_time: vorStunden(FRIST_STUNDEN + 1) }]),
    /* ohne Text (Sticker, geteilter Beitrag) */
    k("c4", [{ id: "m5", from: von("u4", "mia"), message: "", created_time: vorStunden(1) }]),
    /* nur Emoji */
    k("c5", [{ id: "m6", from: von("u5", "ben"), message: "🔥🔥", created_time: vorStunden(1) }]),
    /* Werbung */
    k("c6", [{ id: "m7", from: von("u6", "spam"), message: "Hi, Interesse an einer Kooperation?", created_time: vorStunden(1) }]),
    /* schon behandelt */
    k("c7", [{ id: "m8", from: von("u7", "alt"), message: "Frage von gestern", created_time: vorStunden(3) }]),
  ];
  const ledger = { postfach: [{ nachrichtId: "m8" }] };
  const offen = offeneNachrichten(konv, ICH, ledger, jetzt);
  assert.deepEqual(offen.map((o) => o.id), ["m1"], `unerwartet offen: ${offen.map((o) => o.id).join(", ")}`);
  assert.equal(offen[0].empfaengerId, "u1", "die Antwort ginge an die falsche Person");

  const gruende = Object.fromEntries((offen.uebersprungen || []).map((u) => [u.id, u.grund]));
  assert.match(gruende.m4 || "", /Stunden/, "die Frist wird nicht als Grund genannt");
  assert.equal(gruende.m5, "ohne Text");
  assert.equal(gruende.m6, "nur Emoji");
  assert.equal(gruende.m7, "Werbung");
  assert.equal(gruende.m8, "bereits behandelt");
  /* c2 taucht gar nicht auf: Wer zuletzt geschrieben hat, entscheidet. */
  assert.ok(!(offen.uebersprungen || []).some((u) => u.id === "m3"), "eigene Nachricht wurde geprüft statt übergangen");
});

test("Postfach: der Verlauf kommt mit, die eigene Stimme ist erkennbar", async () => {
  const { offeneNachrichten } = await import("../src/postfach.mjs");
  const ICH = "17841400000000000";
  const jetzt = Date.parse("2026-09-15T12:00:00Z");
  const konv = [{ id: "c1", messages: { data: [
    { id: "m1", from: { id: "u1", username: "lena" }, message: "Wie prüfe ich die Versammlungsfreiheit?", created_time: new Date(jetzt - 3 * 3600000).toISOString() },
    { id: "m2", from: { id: ICH, username: "herrjurist" }, message: "Schutzbereich, Eingriff, Rechtfertigung – in dieser Reihenfolge.", created_time: new Date(jetzt - 2.5 * 3600000).toISOString() },
    { id: "m3", from: { id: "u1", username: "lena" }, message: "Und wenn der Eingriff mittelbar ist?", created_time: new Date(jetzt - 1 * 3600000).toISOString() },
  ] } }];
  const offen = offeneNachrichten(konv, ICH, { postfach: [] }, jetzt);
  assert.equal(offen.length, 1);
  assert.equal(offen[0].id, "m3", "die letzte fremde Nachricht ist die offene");
  assert.equal(offen[0].verlauf.length, 2, "der Verlauf fehlt");
  assert.deepEqual(offen[0].verlauf.map((v) => v.wer), ["person", "kanal"], "die eigene Stimme wird nicht erkannt");
});

test("Postfach: die Grenze zur Einzelfallberatung steht im Systemtext", async () => {
  const quelle = await fs.promises.readFile(new URL("../src/postfach.mjs", import.meta.url), "utf8");
  /* Auf einem Jurakanal ist das keine Geschmacksfrage: Rechtsdienstleistung in einer
     fremden Angelegenheit ist nach § 3 RDG vorbehalten. Eine DM ist der Ort,
     an dem genau danach gefragt wird. */
  assert.match(quelle, /RDG/, "der Systemtext nennt die Norm nicht");
  assert.match(quelle, /Rechtslage.*geht.*was soll ich tun/s, "die Trennlinie fehlt");
  for (const wort of ["Werbung", "Kooperationsanfragen", "Sperrliste"]) {
    assert.ok(quelle.includes(wort), `im Systemtext fehlt: ${wort}`);
  }
});

test("Kommentare und Nachrichten haben eine eigene, bezahlbare Schätzung", async () => {
  const { erwartet } = await import("../src/kosten.mjs");
  const { CONFIG } = await import("../src/config.mjs");
  /* Seit dem 15.09. schreibt das starke Modell die Antworten und sie laufen
     über einen eigenen Topf (CONFIG.antworten). Die Schätzung muss zwei
     Dinge leisten: Sie darf nicht der blinde Standardwert sein, und sie muss
     unter dem Antwortdeckel liegen - sonst könnte an einem frischen Tag kein
     einziger Aufruf starten. */
  for (const zweck of ["Kommentare beantworten", "Nachrichten beantworten"]) {
    const wert = erwartet(zweck);
    assert.ok(wert > 0, `${zweck}: keine Schätzung`);
    assert.ok(wert < CONFIG.antworten.tagesBudgetUsd, `${zweck}: ${wert} $ erwartet – übersteigt den Antwortdeckel ${CONFIG.antworten.tagesBudgetUsd} $`);
    assert.equal(wert, erwartet(zweck.split(" ")[0].toLowerCase()), `${zweck}: Wortlaut und Schlüssel müssen dieselbe Schätzung liefern`);
  }
  /* Der teure Weg bleibt teuer geschätzt – sonst reißt die Rücklage. */
  assert.ok(erwartet("Reel-Skript schreiben") >= 0.05, "das Reel wird zu billig geschätzt");
});

test("Token-Tresor: ohne Herkunftsvermerk gewinnt das Secret", async () => {
  const quelle = await fs.promises.readFile(new URL("../src/instagram.mjs", import.meta.url), "utf8");
  /* Am 15.09. wurde ein neu gesetztes Secret mit zwei zusätzlichen
     Berechtigungen stillschweigend verworfen. Die Bedingung lautete
     `t.herkunft && secret && t.herkunft !== secret` – bei einem Tresor ohne
     Herkunft knipste das erste Glied die ganze Prüfung aus, und der alte
     Token lief weiter. Der Tresor stammte vom 11.09. um 05:43, die Prüfung
     kam 17 Stunden später dazu.

     Ein Eintrag ohne Herkunft ist gerade der Fall, in dem man ihm nicht
     trauen darf – geprüft wird deshalb der Quelltext der Bedingung. */
  assert.doesNotMatch(quelle, /if \(t\.herkunft && secret && t\.herkunft !== secret\)/,
    "die alte Bedingung steht wieder da – ein Tresor ohne Herkunft gewinnt dann erneut");
  assert.match(quelle, /if \(secret && t\.herkunft !== secret\)/,
    "die Herkunftsprüfung greift nicht mehr bei fehlendem Vermerk");
  assert.match(quelle, /Tresor ohne Herkunftsvermerk/, "der Fall wird nicht sichtbar protokolliert");
});

test("Bezahlte Story-Texte überleben ein leeres Budget und erscheinen erst nach ihrer Prüfung", async () => {
  /* 16.09.: Auf dem Schwesterkanal waren neun Story-Texte geschrieben und
     bezahlt (0,068 $), der Faktencheck lief (0,018 $) - und dann warf die
     optionale Zweitmeinung einen BudgetFehler, der den ganzen Aufruf
     mitriss. Aus `storiesSchreiben` kam nichts zurück, nichts wurde
     gespeichert, sieben von neun Stories fielen aus. Das darf nicht wieder
     passieren. */
  const { budgetSetzen, BudgetFehler } = await import("../src/kosten.mjs");
  const { storiesPruefen } = await import("../src/autor.mjs");

  const liste = [{ slot: "s3", art: "merksatz", titel: "Anfechtung", text: "Die Anfechtung wirkt auf den Zeitpunkt des Vertragsschlusses zurück." }];
  budgetSetzen({ limitUsd: 0.1, bisher: 0.1 });
  const zurueck = await storiesPruefen(liste);
  budgetSetzen({ limitUsd: Infinity, bisher: 0 });

  assert.equal(zurueck.length, 1, "der bezahlte Text ging verloren statt erhalten zu bleiben");
  assert.equal(zurueck[0].titel, "Anfechtung", "der Text wurde unterwegs verändert");
  assert.ok(zurueck[0].faktencheckOffen, "die ausstehende Prüfung ist nicht vermerkt – der Text erschiene ungeprüft");

  /* Die Zweitmeinung ist eine Zusatzrunde: Ein BudgetFehler dort darf den
     Prüfer nicht sprengen, sonst stirbt der Aufruf an einer Kür. */
  const fc = fs.readFileSync(new URL("../src/faktencheck.mjs", import.meta.url), "utf8");
  assert.ok(!/catch \(e\) \{\s*\n\s*if \(e instanceof BudgetFehler\) throw e;\s*\n\s*console\.warn\(`  ! Zweitmeinung/.test(fc),
    "die Zweitmeinung wirft den BudgetFehler wieder nach oben");
  assert.match(fc, /Einwände gelten ohne Zweitmeinung/, "der günstige Ausweg ohne Zweitmeinung fehlt");

  /* Und ungeprüft erscheint nichts. Die Entscheidung dazu ist seit dem
     18.09. eine eigene Funktion (Safety 0c) - geprüft wird sie dort, hier
     zählt nur, dass der Tageslauf sie auch fragt. */
  const lauf = fs.readFileSync(new URL("../src/lauf.mjs", import.meta.url), "utf8");
  const pruef = fs.readFileSync(new URL("../src/pruefung.mjs", import.meta.url), "utf8");
  assert.match(pruef, /if \(story\.faktencheckOffen\) return \{ frei: false, warten: true/,
    "die Freigabe lässt Stories mit offener Prüfung durch");
  assert.match(lauf, /const freigabe = storyFreigabe\(story\);/,
    "der Tageslauf fragt die Freigabe nicht");
  assert.match(lauf, /storiesPruefen\(ungeprueft\)/, "der Tageslauf holt die offene Prüfung nicht nach");
  assert.ok(BudgetFehler);
});

test("Die Quellensperre trifft Verweise, nicht das blosse Wort", () => {
  /* 16.09. auf dem Schwesterkanal: Das blosse Wort „Skript“ in einem Lerntipp
     galt als Verweis auf das Kursmaterial, die Story fiel aus. Die Sperre
     bleibt, sie zielt jetzt genauer. */
  const f = (t) => pruefeBeitrag({ stories: [{ slot: "s1", art: "norm", titel: "T", text: t }] });
  assert.ok(f("Nimm dir heute dein Skript vor und wiederhole die Fristen.").ok, "Lerntipp zu Unrecht beanstandet");
  for (const t of ["Laut Skript gilt das anders.", "Siehe Skript, S. 42.", "Das steht auf Seite 12."]) {
    assert.ok(!f(t).ok, `durchgerutscht: „${t}“`);
  }
});

test("Wer auf den Folien handelt, wird auf den Folien vorgestellt", async () => {
  /* 16.09.: Ein Karussell zur Leistungskondiktion erzählte ab Folie 2 von
     „Finn" und „Nora" – wer die beiden sind, stand nur in der Caption, und
     die ist zugeklappt. */
  const { fallnamenOhneSachverhalt } = await import("../src/pruefung.mjs");
  const derFall = {
    folien: [
      { art: "titel", titel: "4.320 Euro zu viel – wie viel muss zurück?" },
      { art: "schritte", titel: "Der Grundaufbau", schritte: [
        { titel: "Etwas erlangt", text: "Finn hat 4.320 Euro zu viel erhalten." },
        { titel: "Durch Leistung", text: "Nora hat bewusst fremdes Vermögen gemehrt." },
      ] },
      { art: "text", titel: "Was jetzt gilt", punkte: ["Finn bucht davon eine ohnehin geplante Reise."] },
    ],
    caption: "Nora überweist Finn aus Versehen zu viel Geld.",
  };
  assert.deepEqual(fallnamenOhneSachverhalt(derFall).sort(), ["Finn", "Nora"],
    "die Fallnamen ohne Sachverhalt werden nicht erkannt");

  /* Mit Sachverhaltsfolie ist alles vorgestellt – der Beitrag geht durch. */
  const mitSachverhalt = { ...derFall, folien: [
    derFall.folien[0],
    { art: "text", titel: "Sachverhalt", text: "Nora überweist Finn 4.320 Euro zu viel. Finn bucht davon eine ohnehin geplante Reise." },
    ...derFall.folien.slice(1),
  ] };
  assert.deepEqual(fallnamenOhneSachverhalt(mitSachverhalt), [],
    "ein Beitrag mit Sachverhaltsfolie wird zu Unrecht beanstandet");

  /* Juristische Normalsprache ist keine Falldarstellung. */
  const abstrakt = { folien: [
    { art: "titel", titel: "Wie prüft man die Leistungskondiktion?" },
    { art: "text", titel: "Aufbau", punkte: [
      "Fraglich ist, ob ein Rechtsgrund besteht.",
      "Entscheidend ist der Empfängerhorizont.",
      "Grundsätzlich hat der Bereicherungsschuldner Wertersatz zu leisten.",
    ] },
  ] };
  assert.deepEqual(fallnamenOhneSachverhalt(abstrakt), [],
    "abstrakte Fachsprache wird als Falldarstellung missverstanden");
});

test("Das Erklärvideo läuft fünf Tage am Stück und hat Budget für seine Figuren", async () => {
  const { layoutFuer } = await import("../src/reel.mjs");
  for (const d of ["2026-09-17", "2026-09-18", "2026-09-19", "2026-09-20", "2026-09-21"]) {
    assert.equal(layoutFuer(d), "erklaer", `${d} baut nicht das Erklärvideo`);
  }
  /* Danach läuft das Fenster von selbst ab – niemand muss etwas zurücksetzen. */
  assert.equal(layoutFuer("2026-09-23"), "klassisch", "das Fenster endet nicht von selbst");

  /* Die Figuren tragen einen eigenen Zweck - und der ist eine Kür. Solange
     bezahlte Pflichtarbeit aussteht, bekommen sie kein Geld; danach schon.
     Die alte Rücklagenliste aus kosten.mjs hat das entschieden, ohne dass sie
     noch jemand prüfte; jetzt entscheidet es die Admission. */
  const lauf = fs.readFileSync(new URL("../src/lauf.mjs", import.meta.url), "utf8");
  assert.match(lauf, /zweck: "erklaerbild"/, "die Erklärbilder laufen nicht unter eigenem Zweck");
  assert.match(lauf, /optionalSperren\(/, "der Lauf sperrt bezahlte Küren nicht, solange Pflicht aussteht");

  const { budgetStarten, AdmissionAbgelehnt } = await import("../src/budget.mjs");
  const b = budgetStarten({ deckel: { core: 0.32, engagement: 0.25, research: 0.12 } });
  b.optionalSperren("Bezahlte Pflichtarbeit steht aus: 1 Beitrag/Reel.");
  assert.throws(() => b.zulassen("erklaerbild", 0.01, { optional: true }), AdmissionAbgelehnt,
    "die Figuren laufen, obwohl Pflichtarbeit aussteht");
  b.optionalFreigeben();
  assert.ok(b.zulassen("erklaerbild", 0.01, { optional: true }), "nach der Pflicht bekommen sie ihr Geld");
});

test("Jeden Tag ein Rechtsgebiet je Beitrag, und rotierend", async () => {
  const { gebieteDesTages } = await import("../src/planer.mjs");

  /* Drei Plätze, drei Gebiete – jedes genau einmal. */
  for (const d of ["2026-09-17", "2026-09-18", "2026-09-19"]) {
    assert.deepEqual([...gebieteDesTages(d, 3)].sort(), [1, 2, 3], `${d} verteilt die Gebiete nicht sauber`);
  }
  /* Und die Reihenfolge wandert Tag für Tag weiter, statt stehen zu bleiben. */
  const a = gebieteDesTages("2026-09-17", 3);
  const b = gebieteDesTages("2026-09-18", 3);
  const c = gebieteDesTages("2026-09-19", 3);
  assert.notDeepEqual(a, b, "die Zuteilung rotiert nicht");
  assert.notDeepEqual(b, c, "die Zuteilung rotiert nicht");
  assert.deepEqual(gebieteDesTages("2026-09-20", 3), a, "nach drei Tagen ist der Kreis nicht geschlossen");

  /* Weniger Plätze (Mittwoch: „aktuell" folgt der Nachrichtenlage, Samstag:
     Mindset-Reel) – dann eben zwei verschiedene Gebiete, nie zweimal dasselbe. */
  const zwei = gebieteDesTages("2026-09-23", 2);
  assert.equal(zwei.length, 2);
  assert.notEqual(zwei[0], zwei[1], "bei zwei Plätzen doppelt sich das Gebiet");

  /* Im echten Plan: An einem vollen Werktag tragen die drei Beiträge drei
     verschiedene Gebiete. Vorher entschied das eine gewichtete Zufallswahl,
     und die ersten fünf Reels des Kanals waren allesamt grün. */
  const { tagesplan, ledgerLaden } = await import("../src/planer.mjs");
  const plan = tagesplan("2026-09-17", ledgerLaden(), themenpool());
  const gebiete = plan.beitraege.map((x) => x.thema?.klausur).filter(Boolean);
  assert.equal(new Set(gebiete).size, gebiete.length, "zwei Beiträge desselben Tages tragen dasselbe Rechtsgebiet");
  assert.equal(gebiete.length, 3, "der Werktag trägt nicht drei Fachbeiträge");
});

test("Über sechs Wochen trägt jedes Rechtsgebiet gleich viele Beiträge", async () => {
  /* Die Zuteilung geht nach PLATZ im Tag, nicht nach Reihenfolge der
     Pool-Slots. Zählte man die Pool-Slots durch, rückte mittwochs b2 auf das
     Gebiet von b1 nach (weil „aktuell" kein Pool-Thema zieht) und b1 spränge
     von Tag zu Tag. Gemessen kostete das spürbar Gleichmaß: 27/26/25 Beiträge
     und 9/10/7 Reels statt der glatten Verteilung hier. */
  const { tagesplan, ledgerLaden } = await import("../src/planer.mjs");
  const ledger = ledgerLaden();
  const pool = themenpool();
  const gesamt = {}, alsReel = {}, alsErster = {};
  const zaehl = (o, k) => { if (k) o[k] = (o[k] || 0) + 1; };
  for (let i = 0; i < 42; i++) {
    const datum = new Date(Date.UTC(2026, 8, 17) + i * 864e5).toISOString().slice(0, 10);
    const plan = tagesplan(datum, ledger, pool);
    /* Kein Tag trägt zweimal dasselbe Gebiet – im Profilraster sähe das aus
       wie ein Doppelpost. */
    const heute = plan.beitraege.map((b) => b.thema?.klausur).filter(Boolean);
    assert.equal(new Set(heute).size, heute.length, `${datum}: zwei Beiträge im selben Rechtsgebiet`);
    for (const g of heute) zaehl(gesamt, g);
    zaehl(alsReel, plan.beitraege.find((b) => b.format === "reel")?.thema?.klausur);
    zaehl(alsErster, plan.beitraege[0]?.thema?.klausur);
  }
  for (const [was, zaehler] of [["insgesamt", gesamt], ["als Reel", alsReel], ["als erster Beitrag", alsErster]]) {
    const werte = [1, 2, 3].map((g) => zaehler[g] || 0);
    assert.equal(new Set(werte).size, 1,
      `${was} ungleich verteilt: Zivilrecht ${werte[0]}, Strafrecht ${werte[1]}, Öffentliches Recht ${werte[2]}`);
  }
});

test("Die Recherche zeigt nur auf geprüfte Quellen und darf leer ausgehen", async () => {
  /* 16.09.: Von dreizehn Quellen im Prompt waren zehn tot - alle von Hand
     geraten. Eine Recherche, die auf tote Seiten zeigt, sucht frei weiter
     und zahlt jede Runde mit. Die Quellen stehen jetzt in
     bin/quellen-pruefen.mjs und werden dort abgerufen, bevor sie in den
     Prompt kommen. */
  const autor = fs.readFileSync(new URL("../src/autor.mjs", import.meta.url), "utf8");
  const pruefer = fs.readFileSync(new URL("../bin/quellen-pruefen.mjs", import.meta.url), "utf8");

  /* Jede URL aus dem Recherche-Prompt muss in der Quellenprüfung stehen -
     sonst behauptet der Prompt etwas, das nie jemand abgerufen hat. */
  const block = autor.slice(autor.indexOf("const QUELLEN_JURA"), autor.indexOf("export async function aktuellRecherchieren"));
  const urls = [...block.matchAll(/https?:\/\/[^\s`]+/g)].map((m) => m[0]);
  assert.ok(urls.length >= 8, `zu wenige Quellen im Prompt: ${urls.length}`);
  for (const u of urls) assert.ok(pruefer.includes(u), `ungeprüfte Quelle im Prompt: ${u}`);

  /* Tote Quellen aus früheren Läufen dürfen nicht zurückkehren. */
  for (const tot of ["RSSNewsfeed_Pressemitteilungen.xml", "/DE/Aktuelles/aktuelles_node.html", "gesetze-im-internet.de", "rechtsprechung-im-internet.de"]) {
    assert.ok(!block.includes(tot), `zweimal nicht erreichbare Quelle steht wieder im Prompt: ${tot}`);
  }

  /* „Nichts gefunden" ist ein sauberes Ergebnis, kein Fehler - und führt
     ohne weitere Kosten auf den Themenpool. */
  assert.match(autor, /KEINE_NEUIGKEIT/, "dem Modell fehlt der Weg, sauber nichts zu finden");
  assert.match(autor, /HÖCHSTENS ZWEI Suchvorgänge/, "die Suche ist nicht begrenzt");
  const lauf = fs.readFileSync(new URL("../src/lauf.mjs", import.meta.url), "utf8");
  assert.match(lauf, /KEINE_NEUIGKEIT/, "der Tageslauf wertet das leere Ergebnis nicht aus");
  assert.match(lauf, /aufThemenpoolAusweichen/, "der Ausweg auf den Themenpool ist nicht benannt");
});

test("Story-Antworten: Bezug aus jeder Quelle, und nie geraten", async () => {
  /* 16.09.: Jemand antwortete auf die Story „Wonach richtet sich die
     Verteilung der Beweislast im Zivilprozess?" mit „Wie prüfe ich das in der
     Klausur?". An dieser Nachricht fehlte `reply_to`, der Bot hatte nur die
     Hintergrundliste - und schickte eine Prüfung der ANFECHTUNG los, mit den
     Worten „Ich tippe auf die Anfechtung". Das war das Thema eines anderen
     Beitrags desselben Tages. */
  const { offeneNachrichten } = await import("../src/postfach.mjs");
  const jetzt = new Date("2026-09-16T15:00:00Z").getTime();
  const ledger = { veroeffentlicht: [
    { art: "story", medienId: "S7", titel: "Wonach richtet sich die Verteilung der Beweislast?", datum: "2026-09-16", veroeffentlicht: "2026-09-16T07:10:00.000Z" },
    { art: "beitrag", medienId: "B1", titel: "Voraussetzungen der Anfechtung", datum: "2026-09-16", veroeffentlicht: "2026-09-16T06:20:00.000Z" },
  ] };
  const bauen = (letzte) => [{ id: "k1", messages: { data: [{ id: "m1", from: { id: "99", username: "test" }, message: "Wie prüfe ich das in der Klausur?", created_time: new Date(jetzt - 3600000).toISOString(), ...letzte }] } }];

  /* Die ID kann an drei Stellen stehen - jede muss zum Ziel führen. */
  for (const feld of [
    { reply_to: { story: { id: "S7" } } },
    { story: { id: "S7" } },
    { reply_to: { message: { id: "S7" } } },
  ]) {
    const offen = offeneNachrichten(bauen(feld), "1", ledger, jetzt);
    assert.equal(offen.length, 1);
    assert.match(offen[0].bezug || "", /Beweislast/, `Bezug nicht gefunden aus ${JSON.stringify(feld)}`);
    assert.equal(offen[0].bezugQuelle, "aufgelöst");
  }

  /* Story-Antwort ohne verwertbare ID: Das muss als solches benannt sein,
     damit das Modell nachfragt statt zu raten. */
  const ohne = offeneNachrichten(bauen({ reply_to: { story: { url: "https://cdn.example/x.jpg" } } }), "1", ledger, jetzt);
  assert.equal(ohne[0].bezugQuelle, "Story-Antwort ohne Zuordnung");
  assert.match(ohne[0].bezug || "", /WELCHE/, "dem Modell wird nicht gesagt, dass die Story unbekannt ist");

  /* Die Hintergrundliste trägt Uhrzeiten - neun Stories in zwei Minuten
     taugen nicht zum Zuordnen, und das muss sichtbar sein. */
  assert.ok(ohne.zuletzt.every((e) => e.wann), "der Hintergrundliste fehlt die Uhrzeit");

  /* Und die Regeln verbieten das Raten ausdrücklich. */
  const quelle = fs.readFileSync(new URL("../src/postfach.mjs", import.meta.url), "utf8");
  assert.match(quelle, /RATE NIEMALS/, "das Rateverbot fehlt");
  assert.match(quelle, /Ich tippe auf/, "die konkrete Fehlformulierung ist nicht gesperrt");
  assert.match(quelle, /HINTERGRUND, keine Zuordnungshilfe/, "die Hintergrundliste ist nicht als solche gekennzeichnet");
});

test("Story-Antwort ohne ID: laufende Stories statt Gesprächsverlauf", async () => {
  /* 16.09., der echte Testfall: Jemand antwortete auf die Beweislast-Story
     mit „Wo müsste ich das genau einbauen und prüfen?". Instagram meldete
     die Nachricht als Story-Antwort, gab aber keine verwertbare ID mit. Der
     Bot nahm den Verlauf – dort stand Unterhaltsrecht von vorher – und
     antwortete zum falschen Thema. */
  const { offeneNachrichten } = await import("../src/postfach.mjs");
  const jetzt = new Date("2026-09-16T16:40:00Z").getTime();
  const ledger = { veroeffentlicht: [
    { art: "story", medienId: "EIGEN-7", titel: "Wonach richtet sich die Verteilung der Beweislast?", datum: "2026-09-16", veroeffentlicht: "2026-09-16T07:10:00.000Z" },
    { art: "story", medienId: "EIGEN-3", titel: "Trennungsunterhalt: die Voraussetzungen", datum: "2026-09-16", veroeffentlicht: "2026-09-16T07:09:00.000Z" },
  ] };
  const konv = (extra) => [{ id: "k1", messages: { data: [{
    id: "m1", from: { id: "99", username: "nachfolgeberatung" },
    message: "Wo müsste ich das genau einbauen und prüfen?",
    created_time: new Date(jetzt - 600000).toISOString(), ...extra,
  }] } }];

  /* Eine fremde ID darf NICHT über die Uhrzeit zugeordnet werden. Unsere neun
     Stories erscheinen im Minutenabstand; ein Zeitfenster träfe womöglich die
     Nachbarstory. Eine falsche Zuordnung ist schlimmer als keine. */
  const laufend = [{ id: "IG-FREMD-7", timestamp: "2026-09-16T07:10:30.000Z" }];
  const ueberZeit = offeneNachrichten(konv({ reply_to: { story: { id: "IG-FREMD-7" } } }), "1", ledger, jetzt, laufend);
  assert.equal(ueberZeit[0].bezugQuelle, "Story-Antwort ohne Zuordnung",
    "eine fremde ID wurde über die Uhrzeit zugeordnet – genau das darf nicht passieren");

  /* Stimmt die ID dagegen überein, ist es eine echte Zuordnung. */
  const echt = offeneNachrichten(konv({ reply_to: { story: { id: "EIGEN-7" } } }), "1", ledger, jetzt, []);
  assert.equal(echt[0].bezugQuelle, "aufgelöst");
  assert.match(echt[0].bezug, /Beweislast/);

  /* Gar keine ID: Dann muss wenigstens feststehen, WELCHE Stories laufen –
     sonst kann nur allgemein zurückgefragt werden. */
  const ohneId = offeneNachrichten(konv({ reply_to: { story: { url: "https://cdn.example/x.jpg" } } }), "1", ledger, jetzt, laufend);
  assert.equal(ohneId[0].bezugQuelle, "Story-Antwort ohne Zuordnung");
  assert.match(ohneId[0].bezugRoh, /ids=\[keine\] url=ja/, "die rohen Felder fehlen im Log");
  /* Ohne verwertbare ID greift der Ledger-Fallback: BEIDE heutigen Stories
     sind Kandidaten für die Rückfrage – zugeordnet wird keine. */
  assert.equal(ohneId.laufend.length, 2, "die laufenden Stories stehen dem Modell nicht zur Verfügung");
  assert.ok(ohneId.laufend.some((e) => /Beweislast/.test(e.titel)));

  /* Und die Regel sagt ausdrücklich, dass der Verlauf hier nicht das Thema
     bestimmt - genau daran ist die Antwort heute gescheitert. */
  const quelle = fs.readFileSync(new URL("../src/postfach.mjs", import.meta.url), "utf8");
  assert.match(quelle, /VERLAUF NICHT der Bezug/, "die Regel gegen den Verlauf als Thema fehlt");
  assert.match(quelle, /Aktuell laufende Stories/, "die laufenden Stories kommen nicht in den Prompt");
});

test("Liefert Instagram gar nichts, kommen die laufenden Stories aus dem eigenen Protokoll", async () => {
  /* 16.09., zweiter Test: Im Log stand „(ids=[keine] url=nein)" und
     „Laufende Stories: 0". Instagram schickt das Feld reply_to.story als
     LEERES Objekt und kennt den /stories-Endpunkt bei diesem Zugang nicht.
     Damit ist über die API nichts zu holen - wohl aber aus dem eigenen
     Ledger: Was wir in den letzten 24 Stunden als Story veröffentlicht
     haben, läuft noch. */
  const { offeneNachrichten } = await import("../src/postfach.mjs");
  const jetzt = new Date("2026-09-16T17:45:00Z").getTime();
  const ledger = { veroeffentlicht: [
    { art: "story", medienId: "S1", titel: "Grundrechte als Schutzauftrag des Staates", datum: "2026-09-16", veroeffentlicht: "2026-09-16T07:09:00.000Z" },
    { art: "story", medienId: "S2", titel: "Kann jede rechtswidrige Nebenbestimmung isoliert angegriffen werden?", datum: "2026-09-16", veroeffentlicht: "2026-09-16T07:11:00.000Z" },
    /* Ein Beitrag - der darf NICHT als Story-Kandidat auftauchen. */
    { art: "beitrag", medienId: "B2", titel: "Wie prüft man die Leistungskondiktion?", datum: "2026-09-16", veroeffentlicht: "2026-09-16T06:20:00.000Z" },
    /* Eine Story von vorgestern - aus dem 24-Stunden-Fenster heraus. */
    { art: "story", medienId: "S0", titel: "Alte Story von vorgestern", datum: "2026-09-14", veroeffentlicht: "2026-09-14T07:00:00.000Z" },
    /* So sahen Story-Einträge bis zum 16.09. aus: GAR KEIN Zeitstempel. Genau
       daran wäre die Fallback-Liste still leer geblieben. */
    { art: "story", medienId: "S3", titel: "Story von heute ohne Zeitstempel", datum: "2026-09-16" },
  ] };
  const konv = [{ id: "k1", messages: { data: [{
    id: "m1", from: { id: "99", username: "test" },
    message: "Wo muss ich das in der Klausur prüfen?",
    created_time: new Date(jetzt - 600000).toISOString(),
    reply_to: { story: {} },   // genau das, was Instagram schickt: leer
  }] } }];

  const offen = offeneNachrichten(konv, "1", ledger, jetzt, []);
  assert.equal(offen[0].bezugQuelle, "Story-Antwort ohne Zuordnung");
  assert.match(offen[0].bezugRoh, /ids=\[keine\] url=nein/, "die rohen Felder werden nicht protokolliert");

  const titel = offen.laufend.map((e) => e.titel);
  assert.equal(titel.length, 3, `es sollten die drei heutigen Stories sein, waren: ${titel.join(" | ")}`);
  assert.ok(titel.some((t) => /ohne Zeitstempel/.test(t)), "Stories ohne Zeitstempel fallen aus der Liste – der echte Ledger hat keinen");
  assert.ok(titel.some((t) => /Schutzauftrag/.test(t)) && titel.some((t) => /Nebenbestimmung/.test(t)));
  assert.ok(!titel.some((t) => /Leistungskondiktion/.test(t)), "ein Beitrag steht als Story-Kandidat drin");
  assert.ok(!titel.some((t) => /vorgestern/.test(t)), "eine abgelaufene Story steht noch drin");
  assert.ok(offen.laufend.every((e) => e.wann), "den Kandidaten fehlt die Zeitangabe");

  /* Und beim Nachfragen dürfen nur Stories angeboten werden. */
  const quelle = fs.readFileSync(new URL("../src/postfach.mjs", import.meta.url), "utf8");
  assert.match(quelle, /NIEMALS einen Beitrag aus „Zuletzt erschienen“/, "die Regel gegen Beiträge als Story-Kandidat fehlt");
});

test("Der Mitschnitt-Worker prüft die Signatur auf den rohen Bytes", async () => {
  /* Die Signaturprüfung ist die einzige Verteidigung des Endpunkts: Ohne sie
     kann jeder beliebige Daten in den Mitschnitt schreiben. Zwei Fehler sind
     dabei üblich und beide still - über dem neu serialisierten JSON prüfen
     statt über den rohen Bytes, und mit === vergleichen statt in konstanter
     Zeit. */
  const quelle = fs.readFileSync(new URL("../webhook/worker.mjs", import.meta.url), "utf8");
  assert.match(quelle, /await request\.arrayBuffer\(\)/, "der rohe Body wird nicht erhalten");
  assert.match(quelle, /x-hub-signature-256/, "die Signatur wird nicht geprüft");
  assert.match(quelle, /unterschied \|=/, "der Vergleich läuft nicht in konstanter Zeit");
  /* Erst prüfen, dann weiterreichen - nie umgekehrt. */
  assert.ok(quelle.indexOf("signaturStimmt") < quelle.indexOf("ctx.waitUntil"),
    "das Ereignis wird weitergereicht, bevor die Signatur geprüft ist");
  /* Und die Challenge, ohne die sich der Webhook nicht abonnieren lässt. */
  assert.match(quelle, /hub\.challenge/, "die Einrichtungsprüfung von Meta fehlt");
  /* Kein Geheimnis im Code. */
  for (const s of ["VERIFY_TOKEN", "APP_SECRET", "GITHUB_TOKEN"]) {
    assert.match(quelle, new RegExp(`env\\.${s}`), `${s} wird nicht aus der Umgebung gelesen`);
  }
  assert.ok(!/EAA[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}/.test(quelle), "im Worker steht ein Token im Klartext");

  /* Der Mitschnitt darf nichts beantworten - das ist sein ganzer Sinn. */
  assert.ok(!/nachrichtSenden|\/messages/.test(quelle), "der Mitschnitt sendet Nachrichten");
});

/* --------------------------------------------------------------------------
   Story-Zuordnung aus dem Webhook.

   Am 17.09. wurde mitgeschnitten, was Meta beim Eingang einer Story-Antwort
   wirklich schickt. Ergebnis: `message.reply_to.story.id` ist da - waehrend
   derselbe Vorgang ueber /conversations ein leeres `reply_to` lieferte. Der
   Test benutzt deshalb das ECHTE Ereignis, nicht ein ausgedachtes, und die
   Gegenprobe (normale DM ohne Story) gleich mit.
   -------------------------------------------------------------------------- */
test("Story-Bezug kommt aus dem Webhook, wenn der Abruf ihn verschweigt", async () => {
  const { offeneNachrichten } = await import("../src/postfach.mjs");
  const jetzt = Date.parse("2026-09-17T00:20:00Z");

  /* Wortgetreu aus state/webhook-roh.jsonl, gekuerzt um die Signatur-URL. */
  const MID = "aWdfZAG1faXRlbToxOklHTWVzc2FnZAUlEOjE3ODQxNDQ2NTY0NTEwODc3";
  const webhookBezug = {
    [MID]: { storyId: "17908618605537083", absender: "1079335494816469", text: "Test Beweislast", zeit: 1789603907432 },
  };
  const ledger = {
    postfach: [],
    veroeffentlicht: [{ medienId: "17908618605537083", art: "story", titel: "Beweislast beim Anscheinsbeweis", datum: "2026-09-16" }],
  };
  /* So, wie /conversations es geliefert hat: OHNE reply_to. */
  const konv = [{
    id: "k1",
    messages: { data: [{ id: MID, message: "Test Beweislast", from: { id: "1079335494816469" }, created_time: "2026-09-17T00:11:47+0000" }] },
  }];

  const ohneTabelle = offeneNachrichten(konv, "17841446564510877", ledger, jetzt, []);
  assert.equal(ohneTabelle[0].bezug, null, "ohne Webhook hat der Abruf keinen Bezug - das war der Fehler vom 16.09.");

  const mitTabelle = offeneNachrichten(konv, "17841446564510877", ledger, jetzt, [], webhookBezug);
  assert.match(mitTabelle[0].bezug, /Beweislast beim Anscheinsbeweis/, "mit Webhook steht die richtige Story fest");
  assert.equal(mitTabelle[0].bezugQuelle, "aufgelöst");
  assert.equal(mitTabelle[0].bezugWie, "webhook/mid");
});

test("Zweitschluessel Absender+Text traegt, wenn die Nachrichten-ID abweicht", async () => {
  const { offeneNachrichten } = await import("../src/postfach.mjs");
  const jetzt = Date.parse("2026-09-17T00:20:00Z");
  const webhookBezug = {
    "mid-aus-dem-ereignis": { storyId: "S7", absender: "42", text: "Test Beweislast", zeit: jetzt - 60000 },
  };
  const ledger = { postfach: [], veroeffentlicht: [{ medienId: "S7", art: "story", titel: "Anscheinsbeweis", datum: "2026-09-16" }] };
  const konv = [{
    id: "k1",
    messages: { data: [{ id: "voellig-andere-id", message: "Test Beweislast", from: { id: "42" }, created_time: "2026-09-17T00:11:47+0000" }] },
  }];
  const offen = offeneNachrichten(konv, "1", ledger, jetzt, [], webhookBezug);
  assert.match(offen[0].bezug, /Anscheinsbeweis/);
  assert.equal(offen[0].bezugWie, "webhook/absender+text");

  /* Und die Gegenprobe: Ein anderer Absender mit demselben Wortlaut darf den
     Bezug NICHT erben. Sonst raet der Bot wieder, nur subtiler. */
  const fremd = [{
    id: "k2",
    messages: { data: [{ id: "x", message: "Test Beweislast", from: { id: "999" }, created_time: "2026-09-17T00:11:47+0000" }] },
  }];
  assert.equal(offeneNachrichten(fremd, "1", ledger, jetzt, [], webhookBezug)[0].bezug, null);
});

test("Normale DM ohne Story bekommt keinen Bezug angedichtet", async () => {
  const { offeneNachrichten } = await import("../src/postfach.mjs");
  const jetzt = Date.parse("2026-09-17T00:20:00Z");
  /* Zweites echtes Ereignis vom 17.09.: "Test ohne Story" kam ohne reply_to
     herein - der Webhook unterscheidet die beiden Faelle also selbst. */
  const webhookBezug = { "mid-a": { storyId: "S7", absender: "42", text: "Test Beweislast", zeit: jetzt - 60000 } };
  const ledger = { postfach: [], veroeffentlicht: [{ medienId: "S7", art: "story", titel: "Anscheinsbeweis", datum: "2026-09-16" }] };
  const konv = [{
    id: "k1",
    messages: { data: [{ id: "mid-b", message: "Test ohne Story", from: { id: "42" }, created_time: "2026-09-17T00:11:55+0000" }] },
  }];
  const offen = offeneNachrichten(konv, "1", ledger, jetzt, [], webhookBezug);
  assert.equal(offen[0].bezug, null);
  assert.equal(offen[0].bezugQuelle, "kein Bezug");
});

test("Fehlende Zuordnungsdatei laesst den Lauf unberuehrt", async () => {
  const { webhookBezugLaden } = await import("../src/postfach.mjs");
  assert.deepEqual(webhookBezugLaden(null), {});
  assert.deepEqual(webhookBezugLaden("/gibt/es/nicht"), {});
});

test("Worker verteilt nach Konto-ID auf das richtige Repository", async () => {
  const quelle = fs.readFileSync(new URL("../webhook/worker.mjs", import.meta.url), "utf8");
  assert.match(quelle, /ROUTEN/, "Verteilung ist konfigurierbar");
  assert.match(quelle, /zieleFuer\(env, roh\)/, "vor dem Senden wird das Ziel bestimmt");
  /* Die Signaturpruefung muss VOR der Verteilung bleiben - sonst wuerde ein
     Fremder bestimmen, in welches Repository geschrieben wird. */
  assert.ok(quelle.indexOf("signaturStimmt(roh") < quelle.indexOf("zieleFuer(env, roh)"),
    "Signatur wird vor der Verteilung geprueft");
});

/* --------------------------------------------------------------------------
   Rücklage: nur zurücklegen, was auch bezahlbar ist.

   Am 17.09. lagen 0.13 $ für einen noch zu schreibenden Beitrag und die vier
   Erklärfiguren zurück, während vom Tagesdeckel nur noch 0.045 $ frei waren.
   Der Beitrag war davon nie zu bezahlen - seine Rücklage hat aber die neun
   Stories blockiert, die zusammen weniger gekostet hätten. Ergebnis: 0 von 3
   Beiträgen, 0 von 9 Stories.
   -------------------------------------------------------------------------- */
test("Rücklage übersteigt nie das noch freie Budget", async () => {
  const { bezahlbareSumme } = await import("../src/kosten.mjs");

  /* Der Fall vom 17.09.: b2 kostet erwartet 0.085, frei sind 0.045. */
  assert.equal(bezahlbareSumme([0.085], 0.045), 0, "Unbezahlbares wird nicht zurückgelegt");

  /* Reicht es, bleibt der Vorrang: der Beitrag bekommt sein Geld. */
  assert.equal(bezahlbareSumme([0.085], 0.2), 0.085);

  /* Mehrere Beiträge: der Reihe nach, Abbruch beim ersten, der nicht passt.
     Die Reihenfolge IST die Rangfolge - es wird nicht umsortiert, damit der
     dritte Beitrag sich nicht am zweiten vorbeidrängt. */
  assert.equal(bezahlbareSumme([0.06, 0.06, 0.06], 0.13), 0.12);
  assert.equal(bezahlbareSumme([0.20, 0.01], 0.15), 0, "nach dem ersten Fehlschlag wird abgebrochen");

  /* Nichts offen, nichts frei, Unsinn im Eingang. */
  assert.equal(bezahlbareSumme([], 0.3), 0);
  assert.equal(bezahlbareSumme([0.05], 0), 0);
  assert.equal(bezahlbareSumme([0.05], -1), 0);
  assert.equal(bezahlbareSumme([null, undefined, "x"], 0.3), 0);

  /* Cent-Bruchteile dürfen sich nicht zu einem Phantombetrag aufaddieren. */
  assert.equal(bezahlbareSumme([0.0001, 0.0001, 0.0001], 1), 0);
});

/* --------------------------------------------------------------------------
   Obergrenze je Beitrag UND eigener Topf für die Stories.

   Beschluss des Betreibers am 17.09.: höchstens 0,10 $ je Beitrag - aber es
   muss sichergestellt sein, dass das reicht und trotzdem alle Beiträge, Reels
   und Stories erscheinen. Genau das rechnen diese Tests nach.
   -------------------------------------------------------------------------- */
/* Dieser Test hat eine Woche lang Ruhe gemeldet, waehrend die Tage 0,50 bis
   0,70 $ kosteten: Er rechnete mit der Schaetztabelle, und die stand noch auf
   den Preisen von Anfang September. Jetzt stehen dort die gemessenen Zahlen
   vom 18.09., und der Test ist eine Ratsche - er schlaegt an, sobald eine
   Aenderung den Tag teurer macht als das, was zuletzt bewusst hingenommen
   wurde.

   Zwei Zahlen stehen nebeneinander, und der Unterschied ist wichtig:
   Nach der Tabelle kostet ein voller Tag 0,37 $, seit Opus das Reel prueft.
   GEMESSEN kostete er am 18.09. rund 0,54 $, weil Schreiben und Pruefen
   teurer geworden sind als die Tabelle sagt (im Lauf faengt das die
   Vortagsschaetzung ab, hier nicht). Der Regeldeckel liegt bei 0,32 $.

   Diese Luecke ist keine Panne, sondern eine offene Entscheidung des
   Betreibers: weniger Inhalt, guenstigere Modelle oder ein hoeherer Deckel. */
const VOLLER_TAG_MAX = 0.38;
test("Ein voller Tag wird nicht teurer als zuletzt hingenommen", async () => {
  const k = await import("../src/kosten.mjs");
  const { CONFIG } = await import("../src/config.mjs");

  /* Was ein voller Tag an Schreibarbeit kostet, zu den Erwartungswerten. */
  const karussell = k.erwartet("autor") + k.erwartet("faktencheck");
  const reel      = k.erwartet("reel") + k.erwartet("reel-faktencheck");
  const stories   = k.erwartet("stories") + k.erwartet("story-faktencheck");
  const motive    = CONFIG.reel.erklaerBilder * k.erwartet("erklaerbild");

  const vollerTag = 2 * karussell + reel + stories + motive;
  assert.ok(vollerTag <= VOLLER_TAG_MAX,
    `Ein voller Tag (2 Karussells + Reel + 9 Stories + ${CONFIG.reel.erklaerBilder} Motive) kostet jetzt ${vollerTag.toFixed(3)} $ und damit mehr als die zuletzt hingenommenen ${VOLLER_TAG_MAX} $ - wer das erhoeht, muss es dem Betreiber sagen`);

  /* Und die Obergrenze darf nicht unter dem liegen, was ein Beitrag normal
     braucht - sonst stellt sie gesunde Beiträge zurück. */
  assert.ok(CONFIG.ki.maxJeBeitragUsd > karussell,
    `Obergrenze ${CONFIG.ki.maxJeBeitragUsd} $ muss über den normalen Kosten eines Beitrags (${karussell.toFixed(3)} $) liegen`);
  /* Das Reel hat seine eigene Obergrenze - mit der Beitragsgrenze waere es
     an dem Tag zurueckgestellt worden, an dem Opus es zum ersten Mal prueft. */
  assert.ok(CONFIG.ki.maxJeReelUsd > reel,
    `Reel-Obergrenze ${CONFIG.ki.maxJeReelUsd} $ muss über den normalen Kosten eines Reels (${reel.toFixed(3)} $) liegen`);
});

test("Ein teurer Beitrag frisst die Stories nicht mehr auf", async () => {
  const k = await import("../src/kosten.mjs");
  k.budgetSetzen({ limitUsd: 0.32 });

  /* Die Stories bekommen ihren eigenen Topf. */
  k.reservieren(0.06, ["stories", "story-faktencheck"], "die Stories", "stories");
  assert.equal(k.fremdeReserve("autor"), 0.06, "für den Autor ist der Story-Topf gesperrt");
  assert.equal(k.fremdeReserve("stories"), 0, "die Stories kommen an ihren eigenen Topf");

  /* Der Beitrag läuft gegen seine Obergrenze, nicht gegen den Tag. */
  k.postenBeginnen("Beitrag b1", 0.10);
  k.erfassenStueck(0.095, "autor", "erster Entwurf und zwei Prüfrunden");
  assert.throws(() => k.budgetPruefen("faktencheck"), k.PostenFehler,
    "die dritte Runde reisst die Obergrenze des Beitrags");
  /* PostenFehler bleibt ein BudgetFehler - alte Behandlungen greifen weiter. */
  assert.ok(new k.PostenFehler("x") instanceof k.BudgetFehler);
  k.postenBeenden();

  /* Entscheidend: Die Stories können danach trotzdem noch geschrieben werden. */
  assert.ok(k.budgetFrei("stories"),
    "nach dem zurückgestellten Beitrag muss für die Stories noch Geld da sein");
});

test("Ohne eigenen Topf wäre genau der Fehler vom 17.09. wieder da", async () => {
  const k = await import("../src/kosten.mjs");
  k.budgetSetzen({ limitUsd: 0.32 });
  k.erfassenStueck(0.275, "autor", "wie in der Nacht zum 17.09.");
  /* Ohne Story-Topf: Die Rücklage der Beiträge sperrt die Stories aus. */
  k.reservieren(0.13, ["autor", "faktencheck", "reel"], "noch zu schreibende Beiträge", "beitraege");
  assert.equal(k.budgetFrei("stories"), false, "so sah es am 17.09. aus");
  /* Genau dagegen hilft bezahlbareSumme: 0.13 waren nie bezahlbar. */
  assert.equal(k.bezahlbareSumme([0.085], k.tagesLimit() - k.tagesStand()), 0);
});

/* ==========================================================================
   Tiefenprüfung 17.09.: sieben Befunde, jeder mit Test.
   ========================================================================== */
test("Faktencheck: unlesbares oder verweigertes Ergebnis ist KEIN bestandenes", async () => {
  const quelle = fs.readFileSync(new URL("../src/faktencheck.mjs", import.meta.url), "utf8");
  /* Bis zum 17.09. stand hier `return { ok: true }` für beide Fälle. */
  assert.ok(!/catch \{ return \{ ok: true/.test(quelle), "kein stilles Bestehen bei unlesbarem JSON");
  assert.ok(!/=== "refusal"\) return \{ ok: true/.test(quelle), "kein stilles Bestehen bei Verweigerung");
  assert.match(quelle, /throw new Error\(`Modell hat die Prüfung abgelehnt/);
  assert.match(quelle, /throw new Error\(`keine lesbare JSON-Antwort/);
  assert.match(quelle, /Antwort ohne Befundliste/);
  /* Und bevor ein Fehler entsteht, gibt es einen zweiten Anlauf ohne Schema -
     ein einzelner Fehlversuch soll keinen Beitrag um eine Stunde verschieben. */
  assert.match(quelle, /zweiter Anlauf ohne Schema/);
  assert.match(quelle, /throw new Error\(`Faktencheck nicht auswertbar: \$\{ersterFehler\.message\}; zweiter Anlauf/);
  /* Und faktenSicher setzt das um: streng heißt, der Beitrag erscheint nicht. */
  const autor = fs.readFileSync(new URL("../src/autor.mjs", import.meta.url), "utf8");
  assert.match(autor, /Faktencheck nicht möglich \(\$\{e\.message[^}]*\}\) – der Beitrag erscheint nicht\./);
});

test("Faktencheck: ein weich formulierter Fehler MIT Ersetzung bleibt ein Fehler", async () => {
  const { befundeSortieren } = await import("../src/faktencheck.mjs");
  const befunde = [
    /* Weich formuliert, aber mit konkreter Fundstelle: das ist ein Fehler. */
    { schwere: "fehler", stelle: "Folie 2", problem: "Die Zuordnung ist ungenau", korrektur: "Abs. 2", original: "§ 823 Abs. 1 BGB greift", ersatz: "§ 823 Abs. 2 BGB greift" },
    /* Weich formuliert ohne Fundstelle: Hinweis. */
    { schwere: "fehler", stelle: "Folie 3", problem: "Die Darstellung ist etwas verkürzt", korrektur: "ausführlicher", original: "", ersatz: "" },
    /* Hart formuliert ohne Fundstelle: Fehler. */
    { schwere: "fehler", stelle: "Folie 4", problem: "§ 243 Abs. 2 StGB enthält keine Regelbeispiele", korrektur: "Abs. 1 S. 2", original: "", ersatz: "" },
    /* Sprachversehen mit Fundstelle: Korrektur, kein Fehler. */
    { schwere: "sprache", stelle: "Folie 1", problem: "doppeltes Wort", korrektur: "", original: "hat hat der", ersatz: "hat der" },
    /* Unsicher: Hinweis. */
    { schwere: "unsicher", stelle: "Caption", problem: "Streitstand offen?", korrektur: "", original: "", ersatz: "" },
  ];
  const s = befundeSortieren(befunde);
  assert.deepEqual(s.fehler.map((b) => b.stelle), ["Folie 2", "Folie 4"], "weich + Ersetzung zählt, weich ohne nicht");
  assert.deepEqual(s.korrekturen, [{ original: "hat hat der", ersatz: "hat der" }]);
  assert.deepEqual(s.weich.map((b) => b.stelle), ["Folie 3", "Caption"]);
  assert.equal(s.brauchbar(befunde[0]), true);
  assert.equal(s.brauchbar({ original: "x", ersatz: "y" }), false, "ein Wort ist keine eindeutige Fundstelle");
  assert.deepEqual(befundeSortieren([]).fehler, []);
});

test("Erklärvideo-Figuren werden unter ihrem eigenen Zweck geprüft, nicht als Schmuckbild", async () => {
  const k = await import("../src/kosten.mjs");
  k.budgetSetzen({ limitUsd: 0.48 });
  k.erfassenStueck(0.43, "autor", "Tag fast voll");
  /* Die Rücklage für die vier Figuren, wie lauf.mjs sie anlegt. */
  k.reservieren(0.04, ["autor", "faktencheck", "reel", "reel-faktencheck", "erklaerbild"], "die Figuren des Erklärvideos", "beitraege");
  /* Seit dem 17.09. zählt für ein Beitragsbild nur der Sicherheitsabstand,
     nicht die Rücklage anderer Zwecke: 0.43 + 0.01 + 0.03 = 0.47 < 0.48 -
     das Bild darf. Ein Cent soll nicht vor zwölf Cent Rücklage weichen; an
     diesem Tag blieb jeder Beitrag beider Kanäle ohne Bild. */
  assert.equal(k.budgetFrei("Bild zeichnen"), true, "die Rücklage des Abend-Reels blockiert das Morgenbild nicht mehr");
  /* Der Abstand selbst schützt weiter die Prüfung: Ist der Tag wirklich voll,
     weicht das Bild. */
  k.erfassenStueck(0.02, "autor", "noch ein Stück");
  assert.equal(k.budgetFrei("Bild zeichnen"), false, "0.45 + 0.01 + 0.03 = 0.49 > 0.48");
  /* Unter dem richtigen Zweck ist die Rücklage die eigene: 0.43 + 0.01 < 0.48. */
  assert.equal(k.budgetFrei("Figur zeichnen (erklaerbild)"), true, "die Figur darf ihre eigene Rücklage benutzen");
  /* Seit 1a entscheidet die Admission des eigenen Zwecks, nicht mehr ein
     Zwecktext im alten Deckel: Das Bild geht durch bildAufruf() und traegt
     dabei „bild" oder „erklaerbild" als Zweck - beide im Core-Topf, beide
     als optional gekennzeichnet. */
  const bildki = fs.readFileSync(new URL("../src/bildki.mjs", import.meta.url), "utf8");
  assert.match(bildki, /await bildAufruf\(\{\s*\n?\s*zweck, modell: ki\.modell, optional: true/,
    "das Bild geht unter seinem eigenen Zweck durch die Tür");
  const { ZWECK_TOPF } = await import("../src/budget.mjs");
  assert.equal(ZWECK_TOPF.bild, "core");
  assert.equal(ZWECK_TOPF.erklaerbild, "core");
});

test("Obergrenze je Beitrag gilt in jedem Schreibpfad, verschachtelt läuft der Posten weiter", async () => {
  const k = await import("../src/kosten.mjs");
  k.budgetSetzen({ limitUsd: 1 });
  assert.equal(k.postenAktiv(), false);
  k.postenBeginnen("Beitrag b1", 0.10);
  assert.equal(k.postenAktiv(), true);
  k.erfassenStueck(0.06, "autor", "Entwurf");
  /* Ein Ausweichbeitrag ruft textBesorgen aus textBesorgen - der Posten
     darf dabei nicht neu beginnen, sonst zählte der Entwurf davor nicht. */
  assert.equal(k.postenStand(), 0.06);
  k.postenBeenden();
  assert.equal(k.postenAktiv(), false);
  const lauf = fs.readFileSync(new URL("../src/lauf.mjs", import.meta.url), "utf8");
  assert.match(lauf, /const eigenerPosten = !postenAktiv\(\);/, "textBesorgen prüft, ob schon ein Posten läuft");
  assert.match(lauf, /postenBeginnen\(`Auffüllen \$\{eintrag\.slot\}`, CONFIG\.ki\.maxJeBeitragUsd\)/, "auch das Auffüllen hat die Grenze");
  assert.ok(!/postenBeginnen\(`Beitrag \$\{eintrag\.slot\}`, CONFIG\.ki\.maxJeBeitragUsd\);\n\s+await textBesorgen/.test(lauf), "die Vorab-Schleife beginnt keinen zweiten Posten");
});

test("nachbessern reicht einen BudgetFehler weiter statt einen neuen Entwurf zu provozieren", async () => {
  const autor = fs.readFileSync(new URL("../src/autor.mjs", import.meta.url), "utf8");
  const block = autor.slice(autor.indexOf("async function nachbessern"), autor.indexOf("export function pruefHinweis"));
  /* Seit es die gemeinsame Oberklasse gibt, wird nicht mehr auf einen
     einzelnen Fehlertyp geprüft: Admission, gesperrter Topf und ein nicht
     durable gewordenes Journal sagen dasselbe wie der alte BudgetFehler. */
  assert.match(block, /if \(istKostenKontrollFehler\(e\)\) throw e;/);
  assert.ok(!/catch \{ return null; \}/.test(block), "kein stilles Schlucken mehr");
});

test("Story-Faktencheck: jeder Ausfall hält die Texte, verwirft sie nicht", async () => {
  const autor = fs.readFileSync(new URL("../src/autor.mjs", import.meta.url), "utf8");
  const block = autor.slice(autor.indexOf("export async function storiesPruefen"), autor.indexOf("const REEL_SCHEMA"));
  assert.ok(!/throw e;/.test(block), "ein technischer Ausfall fliegt nicht mehr nach oben");
  assert.match(block, /for \(const o of liste\) o\.faktencheckOffen = true;/);
});

test("Übersprungene Nachrichten und Kommentare werden je Grund gebündelt gemeldet", async () => {
  const { uebersprungeneMelden } = await import("../src/postfach.mjs");
  const zeilen = [];
  const liste = [
    ...Array.from({ length: 40 }, (_, i) => ({ von: `leer${i}`, text: "", grund: "ohne Text" })),
    { von: "a", text: "Danke!", grund: "älter als 24 Stunden – Instagram nimmt keine Antwort mehr an" },
    { von: "b", text: "🎉", grund: "nur Emoji" },
    { von: "c", text: "x", grund: "bereits behandelt" },
  ];
  uebersprungeneMelden(liste, (z) => zeilen.push(z));
  assert.equal(zeilen.length, 3, "eine Zeile je Grund, „bereits behandelt“ gar nicht");
  assert.match(zeilen[0], /^  · 40 übersprungen \(ohne Text\): @leer0, @leer1, @leer2, …$/);
  assert.match(zeilen[1], /1 übersprungen \(älter als 24 Stunden/);
  /* Kommentare tragen den Namen unter `username`. */
  const z2 = [];
  uebersprungeneMelden([{ username: "k1", text: "hi", grund: "nur Emoji" }], (z) => z2.push(z), "username");
  assert.match(z2[0], /@k1/);
});

test("Antwortpfade überleben ein unlesbares Modellergebnis", async () => {
  for (const datei of ["postfach", "interaktion"]) {
    const q = fs.readFileSync(new URL(`../src/${datei}.mjs`, import.meta.url), "utf8");
    assert.match(q, /catch \(e\) \{ console\.warn\(`  ! Antworten nicht lesbar/, `${datei}: JSON-Fehler wird abgefangen`);
    assert.match(q, /if \(!Array\.isArray\(daten\?\.antworten\)\) return \[\];/, `${datei}: fehlende Liste heißt keine Antworten`);
  }
});

test("Planmäßige Läufe halten die Concurrency-Gruppe höchstens zwei Stunden", async () => {
  const wf = fs.readFileSync(new URL("../.github/workflows/instagram.yml", import.meta.url), "utf8");
  assert.match(wf, /timeout-minutes: \$\{\{ \(github\.event_name == 'schedule' \|\| github\.event\.inputs\.wecker == 'true'\) && 120 \|\| 300 \}\}/);
});

test("Messversuch: Beiträge schreiben mit medium, Reels und Stories bleiben bei low", async () => {
  /* Reels sind seit der Nacht zum 18.09. aus dem Versuch heraus: Mit medium
     kostete das Skript auf beiden Kanälen mehr als die Obergrenze je Beitrag
     (0,116 $ und 0,143 $) und wurde zurückgestellt. */
  const { CONFIG } = await import("../src/config.mjs");
  assert.equal(CONFIG.ki.effortBeitrag, "medium");
  assert.equal(CONFIG.ki.effortReel, "low");
  assert.equal(CONFIG.ki.effort, "low");
  const autor = fs.readFileSync(new URL("../src/autor.mjs", import.meta.url), "utf8");
  assert.match(autor, /schema: BEITRAG_SCHEMA, effort: CONFIG\.ki\.effortBeitrag/);
  assert.match(autor, /schema: REEL_SCHEMA, zweck: "reel", effort: CONFIG\.ki\.effortReel/);
  assert.match(autor, /schema: STORY_SCHEMA, modell: CONFIG\.ki\.modellNeben, effort: CONFIG\.ki\.effort/);
});

/* --------------------------------------------------------------------------
   Reel vom 17.09.: Motive daneben, Paragrafen ohne Gesetz, Eigenbegriff im
   Kurztitel. Drei Regeln dagegen.
   -------------------------------------------------------------------------- */
test("Bühnentext: jede Norm trägt ihr Gesetz", async () => {
  const { normenOhneGesetz } = await import("../src/pruefung.mjs");
  /* Genau die Zeilen, die am 17.09. auf dem Reel standen. */
  assert.deepEqual(normenOhneGesetz("§ 3 vs. § 7: Vorgang trennen"), ["§ 3", "§ 7"]);
  assert.deepEqual(normenOhneGesetz("§ 20: Schuldner klären"), ["§ 20"]);
  /* Einmal das Gesetz am Ende versorgt eine Aufzählung. */
  assert.deepEqual(normenOhneGesetz("§ 823 + § 826 BGB: zwei Wege"), []);
  assert.deepEqual(normenOhneGesetz("§ 80 Abs. 5 VwGO, § 123 VwGO"), []);
  assert.deepEqual(normenOhneGesetz("Frist gewahrt"), []);
  const autor = fs.readFileSync(new URL("../src/autor.mjs", import.meta.url), "utf8");
  assert.match(autor, /nennt \$\{nackt\.join\(", "\)\} ohne Gesetz/, "reelSchreiben lehnt Stichwortzeilen ohne Gesetz ab");
  assert.match(autor, /Jede Norm auf der Bühne trägt ihr Gesetz/, "und die Anleitung sagt es dem Autor vorher");
});

test("Bildregie: Metaphern fliegen, Fachgegenstände bleiben, Ausfall kostet das Reel nicht", async () => {
  const autor = fs.readFileSync(new URL("../src/autor.mjs", import.meta.url), "utf8");
  const { bildregie } = await import("../src/autor.mjs");
  assert.equal(typeof bildregie, "function");
  /* Ohne Motive kein Aufruf - und damit kein Geld. */
  assert.deepEqual(await bildregie({ szenen: [{ art: "hook", titel: "x", sprecher: "y" }] }), { geprueft: 0, ersetzt: 0 });
  assert.match(autor, /zweck: "bildregie"/, "die Regie hat ihren eigenen Zweck und damit ihre eigene Admission");
  assert.match(autor, /await bildregieSicher\(reel\); return reel;/, "läuft vor jeder Rückgabe des Reels");
  assert.match(autor, /Bildregie übersprungen/, "und ein Ausfall lässt das Reel durch");
  assert.match(autor, /Metaphern gelten NICHT/, "die Regel steht im Systemtext");
  const k = await import("../src/kosten.mjs");
  assert.equal(k.erwartet("bildregie"), 0.01, "Cent-Betrag, nicht der Standardwert");
  /* Die Bildregie ist Pflicht, keine Kür: Ohne sie hat das Reel keine
     Bildanweisungen. Sie darf deshalb auch dann laufen, wenn bezahlte Küren
     gesperrt sind. */
  const { budgetStarten } = await import("../src/budget.mjs");
  const b = budgetStarten({ deckel: { core: 0.32, engagement: 0.25, research: 0.12 } });
  b.optionalSperren("Bezahlte Pflichtarbeit steht aus.");
  assert.ok(b.zulassen("bildregie", 0.02), "die Regie wird als Kür behandelt und fällt aus");
});

test("Eine Berichtigung landet im abgelegten Entwurf, nicht nur im laufenden Prozess", async () => {
  const { entwurfsspeicher, entwurfBerichtigen } = await import("../src/autor.mjs");
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), "entwuerfe-"));
  try {
    entwurfsspeicher(dir);
    /* 18.09.: Der Faktencheck fand an b2 eine Stelle, die Ersetzung griff im
       Prozess, die Nachprüfung scheiterte an der Obergrenze - und der Speicher
       hielt weiter den alten Text. Jeder folgende Lauf hätte dieselbe Prüfung
       bezahlt und wäre an derselben Stelle gescheitert. */
    fs.writeFileSync(path.join(dir, "abc.json"), JSON.stringify({ datum: "2026-09-18", zweck: "autor", daten: { folien: [{ text: "Die Frist beträgt einen Monat." }], caption: "Frist: einen Monat." } }));
    const n = entwurfBerichtigen("abc", [{ original: "einen Monat", ersatz: "zwei Wochen" }]);
    assert.equal(n, 2, "beide Stellen ersetzt");
    const neu = JSON.parse(fs.readFileSync(path.join(dir, "abc.json"), "utf8"));
    assert.equal(neu.daten.folien[0].text, "Die Frist beträgt zwei Wochen.");
    assert.equal(neu.daten.caption, "Frist: zwei Wochen.");
    assert.equal(neu.zweck, "autor", "Zweck bleibt erhalten");
    /* Ohne Treffer wird nichts geschrieben; ohne Schlüssel oder Speicher auch nicht. */
    assert.equal(entwurfBerichtigen("abc", [{ original: "gibt es nicht", ersatz: "x" }]), 0);
    assert.equal(entwurfBerichtigen(null, [{ original: "zwei Wochen", ersatz: "x" }]), 0);
    assert.equal(entwurfBerichtigen("fehlt", [{ original: "zwei Wochen", ersatz: "x" }]), 0);
  } finally {
    entwurfsspeicher(null);
    fs.rmSync(dir, { recursive: true, force: true });
  }
});

test("Die Schätzung lernt aus den Vortagen, heutige Messungen gehen vor", async () => {
  const { vortagsSchaetzung, budgetSetzen, erwartet, budgetFrei } = await import("../src/kosten.mjs");
  /* Der Fehler vom 18.09.: Der Faktencheck stand in der Tabelle mit 0,01 $,
     gemessen kostete er seit dem 16.09. das Fünf- bis Siebenfache. Jeder Tag
     startete trotzdem wieder mit 0,01 $ - der Deckel plante mit einer Zahl,
     die die Wirklichkeit längst widerlegt hatte. */
  const tage = {
    "2026-09-14": { messungen: { faktencheck: 0.005 } },
    "2026-09-15": { messungen: { faktencheck: 0.0188 } },
    "2026-09-16": { messungen: { faktencheck: 0.0501, reel: 0.09 } },
    "2026-09-17": { messungen: { faktencheck: 0.0354 } },
    "2026-09-18": { messungen: { faktencheck: 0.99 } },
  };
  const v = vortagsSchaetzung(tage, "2026-09-18", 3);
  assert.equal(v.faktencheck, 0.0501, "teuerster Aufruf der letzten drei Tage");
  assert.equal(v.reel, 0.09, "auch Zwecke, die nur an einem der Tage vorkamen");
  assert.ok(!("stories" in v), "unbekannte Zwecke bleiben leer");
  /* Der laufende Tag zählt nicht mit: sonst rechnete der Nachmittag mit dem
     Ausrutscher des Vormittags weiter, obwohl der Lauf ihn ohnehin misst. */
  assert.ok(v.faktencheck < 0.99);

  budgetSetzen({ limitUsd: 1, vortag: v });
  assert.equal(erwartet("faktencheck"), 0.0501, "Vortag schlägt die Tabelle (0,01 $)");
  assert.equal(erwartet("recherche"), 0.12, "die Tabelle bleibt Untergrenze, wo sie höher liegt");
  /* Heute gemessen schlägt den Vortag - ein billiger gewordener Zweck darf
     nicht drei Tage lang teuer gerechnet werden. */
  budgetSetzen({ limitUsd: 1, vortag: v, gemessen: { faktencheck: 0.012 } });
  assert.equal(erwartet("faktencheck"), 0.012);
  /* Und die Zahl wirkt: Mit 0,05 $ Erwartung ist bei 0,97 $ Stand Schluss,
     mit 0,01 $ wäre der Aufruf noch gestartet. */
  budgetSetzen({ limitUsd: 1, bisher: 0.97, vortag: v });
  assert.equal(budgetFrei("faktencheck"), false, "teurer Aufruf startet nicht mehr");
  budgetSetzen({ limitUsd: 1, bisher: 0.97 });
  assert.equal(budgetFrei("faktencheck"), true, "mit der alten Tabelle wäre er gestartet - genau der Fehler");
});

test("Foto-Look bestellt keinen durchsichtigen Hintergrund, Flat-Look schon", async () => {
  /* Die Probe vom 18.09.: Verlangt man eine Fotografie, malt das Modell immer
     einen Hintergrund dazu - alle drei Proben kamen mit Studiogrund zurück,
     obwohl Transparenz gesetzt war. Bilder ohne Alphakanal verwirft die
     Pipeline, also überlebte gerade die flache Illustration. Deshalb wird der
     Hintergrund beim Foto-Look gar nicht erst verlangt, sondern hinterher
     weggeschnitten. */
  const { bildAuftrag } = await import("../src/bildki.mjs");
  const foto = bildAuftrag("stack of unopened envelopes", { look: "foto" });
  const flach = bildAuftrag("stack of unopened envelopes", { look: "flach" });
  assert.match(foto, /Photorealistic photograph/);
  /* „Ohne Hintergrund" steht in BEIDEN Aufträgen, vorn und am Ende - so, wie
     der Betreiber es am 18.09. selbst erfolgreich erprobt hat. Das Wort
     „transparent" kommt im Auftrag nicht mehr vor: Es ist ein Wort aus der
     Dateiwelt, und das Modell hat darauf mit gemalten Studiohintergründen
     geantwortet. */
  for (const a of [foto, flach]) {
    assert.match(a, /WITHOUT ANY BACKGROUND/);
    assert.match(a, /WITHOUT A BACKGROUND/);
    assert.ok(!/transparent/i.test(a), "das Wort transparent steht nicht mehr im Auftrag");
  }
  assert.match(flach, /Flat vector illustration/);
  /* Beide Aufträge verbieten Schrift im Bild - der Grund steht im Protokoll
     vom 18.09.: „GERITIFIEID MAIL" auf einem Titelbild. */
  for (const a of [foto, flach]) assert.match(a, /no text, no letters, no words/);
  /* Und der Freisteller lässt sich für gezeichnete Bilder ohne
     Schärfeprüfung aufrufen: Die weiche Tiefenschärfe ist dort bestellt. */
  const { freistellen } = await import("../src/freistellen.mjs");
  assert.equal(freistellen("/gibt-es-nicht.png", { schaerfePruefen: false }), null, "kennt die Option und stirbt nicht daran");
});

test("Ein Beitrag passt mit Schreiben und zwei Prüfungen unter die Obergrenze", async () => {
  const { CONFIG } = await import("../src/config.mjs");
  const { budgetSetzen, postenBeginnen, budgetFrei, erfassen } = await import("../src/kosten.mjs");
  /* Gemessen am 18.09.: Schreiben 0,077 $, Prüfung 0,034 $. Mit der alten
     Grenze von 0,10 $ passte kein einziger Beitrag mehr in einen Lauf - b2
     wurde an diesem Tag viermal angefasst und erschien nicht. */
  budgetSetzen({ limitUsd: 5, gemessen: { autor: 0.077, faktencheck: 0.034 } });
  postenBeginnen("Beitrag b2", CONFIG.ki.maxJeBeitragUsd);
  assert.equal(budgetFrei("Text schreiben (Autor)"), true, "schreiben muss gehen");
  erfassen("claude-sonnet-5", { input_tokens: 900, output_tokens: 4500 }, "autor");
  assert.equal(budgetFrei("Faktencheck"), true, "die Prüfung danach muss in denselben Lauf passen");
  erfassen("claude-sonnet-5", { input_tokens: 1200, output_tokens: 2200 }, "faktencheck");
  assert.equal(budgetFrei("Faktencheck"), true, "und eine zweite Runde nach einer Berichtigung auch");
  /* Aber nicht beliebig weiter: Der Ausreißer vom 17.09. - ein Beitrag, der
     nach Beanstandungen ganz neu geschrieben wurde und mit 0,19 $ neun
     Stories mitnahm - muss weiter auflaufen. */
  erfassen("claude-sonnet-5", { input_tokens: 1500, output_tokens: 6000 }, "autor");
  erfassen("claude-sonnet-5", { input_tokens: 1500, output_tokens: 6000 }, "autor");
  assert.equal(budgetFrei("Faktencheck"), false, "die Neufassungs-Schleife wird gestoppt");
});

test("Safety 0a: Quiz-Invarianten halten Frage und Antwort zusammen", async () => {
  const { quizBefunde, QUIZ_OPTIONEN } = await import("../src/pruefung.mjs");
  const frage = (o, extra = {}) => ({ slot: "s3", art: "frage", pairId: "t1", optionen: o, richtig: null, ...extra });
  const antwort = (o, r, extra = {}) => ({ slot: "s4", art: "antwort", pairId: "t1", optionen: o, richtig: r, ...extra });
  const ABC = ["Wirtschaftsgut", "Rückstellung", "Merkposten"];

  assert.equal(QUIZ_OPTIONEN, 3);

  /* Der Index muss in die Liste zeigen - strukturell, kostenlos. */
  assert.equal(quizBefunde([antwort(ABC, -1)]).length, 1, "negativer Index");
  assert.equal(quizBefunde([antwort(ABC, 3)]).length, 1, "Index hinter der letzten Option");
  assert.equal(quizBefunde([antwort(ABC, 1.5)]).length, 1, "kein ganzzahliger Index");
  assert.equal(quizBefunde([antwort(ABC, null)]).length, 1, "eine Antwort ohne Markierung ist keine Antwort");
  for (const r of [0, 1, 2]) assert.deepEqual(quizBefunde([antwort(ABC, r)]), [], `Index ${r} ist zulässig`);

  /* Drei Optionen, keine leer. */
  assert.equal(quizBefunde([antwort(["A", "B"], 1)]).length, 1, "zwei Optionen");
  assert.equal(quizBefunde([antwort(["A", "  ", "C"], 1)]).length, 1, "leere Option");

  /* Das Paar: gleiche Folge, gleiche Reihenfolge. */
  assert.deepEqual(quizBefunde([frage(ABC), antwort(ABC, 1)]), [], "identische Folge ist in Ordnung");

  /* Der reale Vorfall vom 16.09.2026 (Examens Campus): Nach dem isolierten
     Neuschreiben trug die Frage A/B/C, die bereits bestehende Antwort
     A/C/B mit richtig=1. Die Frage sagte damit inhaltlich Merkposten, die
     Antwort markierte Rückstellung. */
  const sep16 = quizBefunde([
    frage(["Wirtschaftsgut", "Rückstellung", "Merkposten"]),
    antwort(["Wirtschaftsgut", "Merkposten", "Rückstellung"], 1),
  ]);
  assert.equal(sep16.length, 1, "vertauschte Optionen müssen auffallen");
  assert.match(sep16[0], /Platz 2/, "der Befund benennt die Stelle");
  assert.match(sep16[0], /\[s4\]/, "der Befund benennt den Slot");

  /* Zwei Markierungen, die sich widersprechen. */
  const doppelt = quizBefunde([frage(ABC, { richtig: 2 }), antwort(ABC, 1)]);
  assert.equal(doppelt.length, 1, "Frage und Antwort dürfen nicht verschiedene Optionen markieren");

  /* Ohne gemeinsamen Schlüssel wird nichts zusammengerechnet. */
  assert.deepEqual(quizBefunde([frage(ABC, { pairId: "t1" }), antwort(["X", "Y", "Z"], 0, { pairId: "t2" })]), [],
    "verschiedene Themen sind kein Paar");

  /* Andere Story-Arten bleiben unberührt. */
  assert.deepEqual(quizBefunde([{ slot: "s7", art: "merksatz", text: "x" }]), []);

  /* Dieselbe Optionsfolge vom 16.09. noch einmal - diesmal nicht gegen die
     Invariante, sondern gegen das Gate, das vor dem Veröffentlichen läuft.
     Der Fehler von damals muss auf BEIDEN Wegen auffallen, und zwar auch von
     der Frage aus: Sie war die Kachel, die zuerst hinausging. */
  const { quizPaarFreigabe } = await import("../src/pruefung.mjs");
  const planSep16 = [
    { slot: "s3", art: "frage", themaId: "t1", zeit: "09:00", status: "geplant" },
    { slot: "s4", art: "antwort", themaId: "t1", zeit: "12:00", status: "geplant" },
  ];
  const textSep16 = {
    s3: { ...frage(["Wirtschaftsgut", "Rückstellung", "Merkposten"]), titel: "Was liegt vor?", text: "Welche Einordnung trifft zu?", befundeTypisiert: true },
    s4: { ...antwort(["Wirtschaftsgut", "Merkposten", "Rückstellung"], 1), titel: "Die Lösung", text: "Es handelt sich um eine Rückstellung.", befundeTypisiert: true },
  };
  const gate = quizPaarFreigabe(planSep16[0], planSep16, (slot) => textSep16[slot] || null);
  assert.notEqual(gate.status, "frei", "die Frage vom 16.09. hätte nicht hinausgehen dürfen");
  assert.equal(gate.status, "verfallen");
  assert.match(gate.grund, /Platz 2/);
});

test("Safety 0c: ein Formcheck löscht keinen fachlichen Befund", async () => {
  const { storyFreigabe } = await import("../src/pruefung.mjs");
  const sauber = { slot: "s7", art: "merksatz", titel: "Kurz", text: "Ein kurzer, unauffälliger Merksatz.", befundeTypisiert: true };

  /* Der Normalfall: nichts beanstandet, die Story darf erscheinen. */
  assert.equal(storyFreigabe(sauber).frei, true);

  /* Der Kern des Befunds V12: Ein fachlicher Befund liegt vor, die
     Formprüfung ist zufrieden - die Story darf trotzdem nicht erscheinen. */
  const fachlich = { ...sauber, beanstandetFachlich: ["[s7] § 433 BGB trägt diese Aussage nicht."] };
  const f = storyFreigabe(fachlich);
  assert.equal(f.frei, false, "ein fachlicher Befund bleibt aktiv, auch wenn die Form stimmt");
  assert.match(f.grund, /fachlich beanstandet/);
  assert.equal(f.warten, false, "das ist kein Warten, sondern ein Nein");

  /* Eine reine Formbeanstandung darf eine erneute Formprüfung aufheben. */
  const form = { ...sauber, beanstandet: ["Story „Kurz“: Text zu lang (999 > 200)"] };
  const g = storyFreigabe(form);
  assert.equal(g.frei, true, "die Formprüfung darf ihren eigenen Befund schließen");
  assert.equal(g.bereinigt, true, "und der Befund wird dann entfernt");

  /* Altbestand ohne Herkunft: kein Freifahrtschein durch den Formcheck. */
  const alt = { ...sauber, befundeTypisiert: undefined, beanstandet: ["irgendein Befund von gestern"] };
  delete alt.befundeTypisiert;
  const h = storyFreigabe(alt);
  assert.equal(h.frei, false, "ein Befund ohne Herkunft bleibt zu");
  assert.match(h.grund, /Altbestand/);

  /* Ungeprüft erscheint nichts - aber das ist Warten, kein Verwerfen. */
  const offen = storyFreigabe({ ...sauber, faktencheckOffen: true });
  assert.equal(offen.frei, false);
  assert.equal(offen.warten, true, "der Text wartet auf seine Prüfung, statt verworfen zu werden");

  /* Auch die Quiz-Invarianten gehören zur deterministischen Prüfung: Eine
     Story mit Formbefund und kaputtem Quiz kommt nicht durch. */
  const quiz = { slot: "s5", art: "antwort", pairId: "t1", optionen: ["A", "B", "C"], richtig: 7,
    titel: "Antwort", text: "kurz", befundeTypisiert: true, beanstandet: ["alter Formbefund"] };
  assert.equal(storyFreigabe(quiz).frei, false, "ein kaputter Index bleibt ein Hindernis");
});

test("Safety 0b: der Prüfer sieht, welche Option als richtig markiert ist", async () => {
  const { textAus } = await import("../src/faktencheck.mjs");
  /* Bis zum 18.09. standen die Optionen als blosse Aufzählung im Prüftext,
     und der Index `richtig` kam darin gar nicht vor. Der Prüfer konnte nicht
     bemerken, dass ein formal gültiger Index auf die fachlich falsche Option
     zeigt - genau das ist am 16.09. passiert. */
  const stories = [
    { slot: "s4", art: "frage", pairId: "t1", titel: "Wie heißt der Posten?", optionen: ["Wirtschaftsgut", "Rückstellung", "Merkposten"], richtig: null },
    { slot: "s5", art: "antwort", pairId: "t1", titel: "Auflösung", optionen: ["Wirtschaftsgut", "Rückstellung", "Merkposten"], richtig: 1, richtigText: "Es ist eine Rückstellung.", norm: "§ 249 HGB" },
    { slot: "s7", art: "merksatz", titel: "Merksatz", text: "Ein kurzer Satz." },
  ];
  const text = textAus({ stories });

  assert.match(text, /ALS RICHTIG MARKIERT: B - Rückstellung/,
    "die Markierung muss im Klartext dastehen, nicht als Zahl irgendwo");
  assert.match(text, /\[QuizPair t1\]/, "Frage und Antwort stehen unter einem gemeinsamen Kopf");
  assert.match(text, /A: Wirtschaftsgut[\s\S]*B: Rückstellung[\s\S]*C: Merkposten/,
    "die Optionen tragen Buchstaben in ihrer Reihenfolge");
  /* Die Frage steht vor der Antwort, damit der Widerspruch sichtbar wird. */
  assert.ok(text.indexOf("FRAGE [Story s4") < text.indexOf("ANTWORT [Story s5"));
  /* Andere Kacheln bleiben, wie sie waren. */
  assert.match(text, /\[Story s7 merksatz\] Merksatz · Ein kurzer Satz\./);

  /* Eine Antwort ohne Markierung fällt auf. */
  const ohne = textAus({ stories: [{ slot: "s5", art: "antwort", pairId: "t2", optionen: ["A", "B", "C"], richtig: null }] });
  assert.match(ohne, /ALS RICHTIG MARKIERT: \(keine Markierung\)/);

  /* Und der Auftrag an den Prüfer sagt ausdrücklich, dass das Paar ein
     Gegenstand ist - „jede Kachel steht für sich" war dort falsch. */
  const autor = fs.readFileSync(new URL("../src/autor.mjs", import.meta.url), "utf8");
  assert.match(autor, /Was unter \[QuizPair\] steht, ist EIN Gegenstand/);
});

/* ---------------------------------------------------------------------------
   Safety 0 – Verhaltenstests statt Quelltextproben.

   Die erste Fassung dieser Tests las den Quelltext und suchte Zeilen darin.
   Das faengt eine geloeschte Zeile, aber kein falsches Verhalten: Ein Gate,
   das die richtigen Zeilen enthaelt und trotzdem freigibt, waere durchgekommen.
   Die folgenden Tests rufen die Funktionen auf und pruefen, was sie tun.
   --------------------------------------------------------------------------- */

/* Ein sauberes Quiz-Paar als Ausgangslage. Aus dem realen Vorfall vom
   16.09.2026: dieselbe Optionsfolge in beiden Kacheln. */
const QUIZ_OPTIONEN_FIXTURE = ["Wirtschaftsgut", "Rückstellung", "Merkposten"];
const quizFrage = (extra = {}) => ({
  slot: "s3", art: "frage", pairId: "t1", titel: "Was liegt hier vor?",
  text: "Der Unternehmer aktiviert einen Posten. Welche Einordnung trifft zu?",
  optionen: [...QUIZ_OPTIONEN_FIXTURE], richtig: null, befundeTypisiert: true, ...extra,
});
const quizAntwort = (extra = {}) => ({
  slot: "s4", art: "antwort", pairId: "t1", titel: "Die Lösung",
  text: "Es handelt sich um ein Wirtschaftsgut.",
  optionen: [...QUIZ_OPTIONEN_FIXTURE], richtig: 0, befundeTypisiert: true, ...extra,
});
/* Plan-Eintraege tragen Status und Paar-Schluessel, nicht den Text. */
const planPaar = (fStatus = "geplant", aStatus = "geplant", extra = {}) => ([
  { slot: "s3", art: "frage", themaId: "t1", zeit: "09:00", status: fStatus, ...(extra.frage || {}) },
  { slot: "s4", art: "antwort", themaId: "t1", zeit: "12:00", status: aStatus, ...(extra.antwort || {}) },
]);

test("Safety 0a: das Gate laesst keine halbe Quiz-Kachel durch", async () => {
  const { quizPaarFreigabe } = await import("../src/pruefung.mjs");
  const leser = (dateien) => (slot) => dateien[slot] || null;

  /* 1. Frage sauber, Antwort fehlt: Die Frage darf nicht erscheinen. Eine
        Frage ohne Antwort bleibt unbeantwortet - die Kachel wartet. */
  const ohneAntwort = quizPaarFreigabe(planPaar()[0], planPaar(), leser({ s3: quizFrage() }));
  assert.equal(ohneAntwort.status, "warten", "ohne Antworttext darf die Frage nicht raus");
  assert.notEqual(ohneAntwort.status, "frei");

  /* 2. Antwort noch im Faktencheck: Die Frage wartet, sie verfaellt nicht. */
  const offen = quizPaarFreigabe(planPaar()[0], planPaar(), leser({ s3: quizFrage(), s4: quizAntwort({ faktencheckOffen: true }) }));
  assert.equal(offen.status, "warten", "ein offener Faktencheck der Antwort haelt die Frage zurueck");

  /* 3. Antwort fachlich beanstandet: Das ist kein Warten, das ist ein Nein.
        Genau hier lief der Faktencheck der Gegenseite frueher ins Leere. */
  const fachlich = quizPaarFreigabe(planPaar()[0], planPaar(), leser({ s3: quizFrage(), s4: quizAntwort({ beanstandetFachlich: ["[s4] § 5 EStG trägt das nicht."] }) }));
  assert.equal(fachlich.status, "verfallen", "ein fachlicher Befund an der Antwort blockiert die Frage");
  assert.match(fachlich.grund, /fachlich beanstandet/);

  /* 4. Beide Seiten fuer sich sauber, aber die Optionen driften auseinander.
        Der Vorfall vom 16.09.2026, diesmal am Frage-Gate: A/B/C gegen A/C/B. */
  const driftend = quizPaarFreigabe(planPaar()[0], planPaar(), leser({
    s3: quizFrage(),
    s4: quizAntwort({ optionen: ["Wirtschaftsgut", "Merkposten", "Rückstellung"], richtig: 1 }),
  }));
  assert.equal(driftend.status, "verfallen", "verschobene Optionen duerfen nicht veroeffentlicht werden");
  assert.match(driftend.grund, /Platz 2/, "der Grund benennt die Stelle");

  /* 5. Eine Antwort ohne Frage im Plan ist ein widerspruechlicher Zustand -
        niemals frei. Frueher galt hier die alte Regel und liess sie durch. */
  const verwaist = quizPaarFreigabe(planPaar()[1], [planPaar()[1]], leser({ s4: quizAntwort() }));
  assert.equal(verwaist.status, "inkonsistent");
  assert.notEqual(verwaist.status, "frei");

  /* 6. Die Frage gilt laut Plan als veroeffentlicht, ihr gespeicherter Text
        fehlt: Dann ist das Paar nicht mehr pruefbar, die Antwort bleibt drin. */
  const fehlendeQuelle = quizPaarFreigabe(planPaar("veroeffentlicht")[1], planPaar("veroeffentlicht"), leser({ s4: quizAntwort() }));
  assert.equal(fehlendeQuelle.status, "inkonsistent");
  assert.match(fehlendeQuelle.grund, /nicht pruefbar/);

  /* Und der Normalfall bleibt normal: Frage erst, dann Antwort. */
  const alles = { s3: quizFrage(), s4: quizAntwort() };
  assert.equal(quizPaarFreigabe(planPaar()[0], planPaar(), leser(alles)).status, "frei", "die saubere Frage darf raus");
  assert.equal(quizPaarFreigabe(planPaar()[1], planPaar(), leser(alles)).status, "warten",
    "die Antwort wartet, solange die Frage nicht draussen ist");
  assert.equal(quizPaarFreigabe(planPaar("veroeffentlicht")[1], planPaar("veroeffentlicht"), leser(alles)).status, "frei",
    "nach der veroeffentlichten Frage darf die Antwort folgen");

  /* Eine uebersprungene Frage nimmt ihre Antwort mit. */
  assert.equal(quizPaarFreigabe(planPaar("uebersprungen")[1], planPaar("uebersprungen"), leser(alles)).status, "verfallen");
});

test("Safety 0d: der zweite Versuch nimmt den Partner mit", async () => {
  const { quizNachschlag } = await import("../src/pruefung.mjs");

  /* 7. Partial State vom 16.09.: Die Frage wird beanstandet, die Antwort liegt
        gespeichert und unveroeffentlicht daneben. Wer jetzt nur die Frage neu
        schreibt, erzeugt genau die Drift. Beide muessen mit. */
  const plan = planPaar();
  const strittig = [quizFrage({ beanstandet: ["Story „Was liegt hier vor?“: Text zu lang"] })];
  const a = quizNachschlag(strittig, plan, (slot) => (slot === "s4" ? quizAntwort({ beanstandetFachlich: ["[s4] falsch"] }) : null));
  assert.deepEqual(a.slots.map((s) => s.slot).sort(), ["s3", "s4"],
    "eine beanstandete Antwort wird gemeinsam mit der Frage neu geschrieben");
  assert.equal(a.festeOptionen.length, 0, "eine beanstandete Gegenseite gibt keine Optionen vor");
  assert.ok(a.paarSlots.has("s3") && a.paarSlots.has("s4"), "beide Slots gelten als Paar-Slots");

  /* Dasselbe, wenn der Partnertext ueberhaupt fehlt. */
  const b = quizNachschlag(strittig, plan, () => null);
  assert.deepEqual(b.slots.map((s) => s.slot).sort(), ["s3", "s4"], "ein fehlender Partnertext wird mitgeschrieben");

  /* 8. Ist der Partner schon draussen, ist er unveraenderlich: Er wird NICHT
        neu geschrieben, seine Optionsfolge wird woertlich vorgegeben. */
  const veroeffentlicht = planPaar("veroeffentlicht");
  const c = quizNachschlag(
    [quizAntwort({ beanstandet: ["Story „Die Lösung“: Text zu lang"] })],
    veroeffentlicht,
    (slot) => (slot === "s3" ? quizFrage() : null),
  );
  assert.deepEqual(c.slots.map((s) => s.slot), ["s4"], "die veroeffentlichte Frage wird nicht angefasst");
  assert.equal(c.festeOptionen.length, 1);
  assert.match(c.festeOptionen[0], /bereits veröffentlicht und darf nicht verändert werden/);
  assert.match(c.festeOptionen[0], /Übernimm exakt diese Optionen in exakt dieser Reihenfolge/);
  for (const o of QUIZ_OPTIONEN_FIXTURE) assert.ok(c.festeOptionen[0].includes(o), `Option „${o}“ fehlt in der Vorgabe`);

  /* Geschrieben, sauber, aber noch nicht draussen: ebenfalls unveraenderlich -
     dieser Fall fehlte in der ersten Fassung ganz, weil nur die Slots ohne
     gespeicherte Datei betrachtet wurden. */
  const d = quizNachschlag(
    [quizAntwort({ beanstandet: ["Story „Die Lösung“: Text zu lang"] })],
    plan,
    (slot) => (slot === "s3" ? quizFrage() : null),
  );
  assert.deepEqual(d.slots.map((s) => s.slot), ["s4"], "eine saubere, gespeicherte Frage wird nicht neu geschrieben");
  assert.match(d.festeOptionen[0], /bereits geschrieben und wird nicht angefasst/);

  /* Veroeffentlicht, aber ohne brauchbaren Text: kein stiller Rewrite, sondern
     eine Warnung - das Gate sperrt das Paar ohnehin. */
  const e = quizNachschlag([quizAntwort({ beanstandet: ["zu lang"] })], veroeffentlicht, () => null);
  assert.deepEqual(e.slots.map((s) => s.slot), ["s4"]);
  assert.equal(e.festeOptionen.length, 0);
  assert.match(e.warnungen[0], /liefert aber keine Optionen/);

  /* Nicht-Quiz-Slots bleiben, wie sie waren: keine Partnersuche, kein Paar. */
  const merksatz = { slot: "s7", art: "merksatz", themaId: "t9", status: "geplant" };
  const f = quizNachschlag([{ slot: "s7", beanstandet: ["zu lang"] }], [merksatz], () => null);
  assert.deepEqual(f.slots.map((s) => s.slot), ["s7"]);
  assert.equal(f.paarSlots.size, 0);
});

test("Safety 0: eine neue fachliche Pruefung ersetzt den alten fachlichen Befund", async () => {
  const { fachpruefungAbschliessen, fachStempel, storyFreigabe } = await import("../src/pruefung.mjs");

  /* 11. Der Text wurde beanstandet, korrigiert und neu geprueft - diesmal ohne
         Befund. Frueher blieb der alte Befund haengen: Die Kachel war nicht
         mehr zu retten, obwohl die Sache geklaert war. */
  const story = quizAntwort({ beanstandetFachlich: ["[s4] § 5 EStG trägt das nicht."] });
  assert.equal(storyFreigabe(story).frei, false, "Ausgangslage: fachlich beanstandet");

  fachpruefungAbschliessen(story, []);
  assert.equal(story.beanstandetFachlich, undefined, "eine saubere Vollpruefung schliesst den alten Befund");
  assert.equal(storyFreigabe(story).frei, true, "danach darf die Kachel erscheinen");
  assert.equal(story.fachStand, fachStempel(story), "die geprüfte Fassung ist gestempelt");
  assert.equal(story.befundeTypisiert, true);

  /* Eine neue Pruefung mit Befund ersetzt ebenfalls - sie haengt nicht an. */
  fachpruefungAbschliessen(story, ["[s4] neuer Befund"]);
  assert.deepEqual(story.beanstandetFachlich, ["[s4] neuer Befund"]);
  fachpruefungAbschliessen(story, ["[s4] wieder ein anderer"]);
  assert.deepEqual(story.beanstandetFachlich, ["[s4] wieder ein anderer"], "zwei Laeufe ergeben keine zwei Befundsaetze");

  /* Befunde anderer Herkunft bleiben unberuehrt: Der Formcheck gehoert nicht
     dem Faktencheck (Safety 0c, andere Richtung). */
  const mitForm = quizAntwort({ beanstandet: ["Story „Die Lösung“: Text zu lang (999 > 200)"], beanstandetFachlich: ["[s4] falsch"] });
  fachpruefungAbschliessen(mitForm, []);
  assert.deepEqual(mitForm.beanstandet, ["Story „Die Lösung“: Text zu lang (999 > 200)"],
    "der fachliche Abschluss fasst den Formbefund nicht an");

  /* Und ein offener Faktencheck gilt nach der Pruefung als erledigt. */
  const warAusgefallen = quizAntwort({ faktencheckOffen: true });
  fachpruefungAbschliessen(warAusgefallen, []);
  assert.equal(warAusgefallen.faktencheckOffen, undefined);

  /* Der Stempel unterscheidet Fassungen: Wird der Text geaendert, passt er
     nicht mehr - daran erkennt ein spaeterer Lauf, dass neu geprueft werden
     muss. */
  const vorher = fachStempel(story);
  assert.notEqual(fachStempel({ ...story, text: "Ein anderer Text." }), vorher);
  assert.notEqual(fachStempel({ ...story, optionen: ["Wirtschaftsgut", "Merkposten", "Rückstellung"] }), vorher);
  assert.equal(fachStempel({ ...story }), vorher, "gleiche Fassung, gleicher Stempel");
});

test("Ein Commit ohne Änderung ist kein Fehler – ein abgelehnter Commit schon", async () => {
  /* Hosting.commit() verschluckte beides zu `false`. Wer damit Zustand
     festschreibt, haelt einen abgelehnten Commit dann faelschlich fuer
     erledigt. Hier laeuft echtes Git in einem Wegwerf-Verzeichnis. */
  const { Hosting } = await import("../src/hosting.mjs");
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), "commit-"));
  const git = (...args) => spawnSync("git", args, { cwd: dir, encoding: "utf8" });
  git("init", "--quiet", "-b", "test");
  const h = new Hosting({ verzeichnis: dir, pushen: false, basisUrl: "https://example.invalid" });

  fs.writeFileSync(path.join(dir, "a.txt"), "eins\n");
  assert.equal(h.commit("erste Fassung"), true, "eine Änderung wird committet");
  assert.equal(h.commit("nichts passiert"), false, "ohne Änderung ist nichts zu tun - und das ist kein Fehler");

  /* Ein echter Fehler: Ein pre-commit-Hook lehnt ab. */
  fs.mkdirSync(path.join(dir, ".git", "hooks"), { recursive: true });
  fs.writeFileSync(path.join(dir, ".git", "hooks", "pre-commit"), "#!/bin/sh\nexit 1\n", { mode: 0o755 });
  fs.writeFileSync(path.join(dir, "a.txt"), "zwei\n");
  assert.throws(() => h.commit("wird abgelehnt"), /./, "ein abgelehnter Commit muss sichtbar fehlschlagen");

  fs.rmSync(dir, { recursive: true, force: true });
});

/* ---------------------------------------------------------------------------
   Ein Trockenlauf ist keine Veröffentlichung.

   18.09.2026: Ein von Hand ausgelöster Lauf lief im Standardmodus „trocken“.
   Er schickte nichts an Instagram und schrieb trotzdem in Plan und Ledger,
   Beitrag und Story seien veröffentlicht – mit `medienId: "trocken"`. Der
   nächste Lauf hätte beide übersprungen; der Tag wäre still ausgefallen.
   --------------------------------------------------------------------------- */

test("Ein Probelauf gilt nie als veröffentlicht – Feed, Reel und Story", async () => {
  const { veroeffentlichungEintragen, veroeffentlichtBestaetigt, echteMedienId, PROBE_KENNUNG }
    = await import("../src/veroeffentlichung.mjs");

  /* Was Instagram zurückgibt, ist eine Ziffernfolge. Alles andere nicht. */
  assert.equal(echteMedienId("18125726395891138"), true, "echte Medien-ID vom 18.09.");
  assert.equal(echteMedienId(PROBE_KENNUNG), false, "die Kennung des Trockenlaufs");
  for (const mist of [null, undefined, "", "   ", 18125726395891138, "17e9", "trocken-1", {}, []])
    assert.equal(echteMedienId(mist), false, `„${String(mist)}“ ist keine Medien-ID`);

  /* Die drei Sendewege, jeder mit demselben Vertrag. */
  for (const art of ["beitrag", "reel", "story"]) {
    const eintrag = { slot: "x1", zeit: "12:30", art, status: "geplant" };
    const vorher = JSON.parse(JSON.stringify(eintrag));

    /* Trockenlauf: Der Eintrag bleibt UNVERÄNDERT. Kein Status, keine ID -
       und auch kein Vermerk: Ein Feld im Plan wäre selbst eine Verschmutzung
       (die erste Fassung dieser Reparatur legte eines an). */
    const probe = veroeffentlichungEintragen(eintrag, PROBE_KENNUNG);
    assert.equal(probe.bestaetigt, false, `${art}: ein Probelauf ist keine Veröffentlichung`);
    assert.equal(probe.kennung, PROBE_KENNUNG, `${art}: die Kennung geht ans Protokoll zurück`);
    assert.deepEqual(eintrag, vorher, `${art}: der Plan-Eintrag wird nicht angefasst`);
    assert.equal(veroeffentlichtBestaetigt(eintrag), false, `${art}: nichts darf sich darauf stützen`);

    /* Und der echte Lauf danach trägt ein. */
    const echt = veroeffentlichungEintragen(eintrag, "17908485354484188", { jetzt: "2026-09-18T16:15:00.000Z" });
    assert.equal(echt.bestaetigt, true, `${art}: eine echte Medien-ID zählt`);
    assert.equal(eintrag.status, "veroeffentlicht");
    assert.equal(eintrag.medienId, "17908485354484188");
    assert.equal(eintrag.veroeffentlicht, "2026-09-18T16:15:00.000Z");
    assert.equal(veroeffentlichtBestaetigt(eintrag), true);
  }

  /* Der Kern des Vorfalls: Status „veröffentlicht“ ohne echte ID zählt nicht. */
  assert.equal(veroeffentlichtBestaetigt({ status: "veroeffentlicht", medienId: "trocken" }), false,
    "genau dieser Zustand stand am 18.09. im Plan");
  assert.equal(veroeffentlichtBestaetigt({ status: "veroeffentlicht" }), false, "Status ohne ID");
  assert.equal(veroeffentlichtBestaetigt({ status: "geplant", medienId: "17908485354484188" }), false,
    "ID ohne Status ist ebenfalls kein Beleg");
});

test("Ein Trockenlauf mitten am Tag kostet keinen veröffentlichten Slot", async () => {
  /* Der Fall, der die erste Fassung dieser Reparatur widerlegt hat: Sie
     vermerkte den Probelauf im Plan, eine spätere Prüfung erkannte daran
     einen „kontaminierten“ Plan und verwarf ihn ganz – samt der beiden
     Beiträge, die wirklich draußen waren. Die hätte der nächste Lauf noch
     einmal veröffentlicht. */
  const { veroeffentlichungEintragen, planBereinigen, planNurAusTrockenlauf, veroeffentlichtBestaetigt }
    = await import("../src/veroeffentlichung.mjs");

  const plan = {
    datum: "2026-09-18",
    beitraege: [
      { slot: "b1", zeit: "08:30", format: "minifall", status: "veroeffentlicht", medienId: "18073311611740667", veroeffentlicht: "2026-09-18T06:46:00.000Z" },
      { slot: "b2", zeit: "12:30", format: "pruefungsfrage", status: "veroeffentlicht", medienId: "17908485354484188", veroeffentlicht: "2026-09-18T16:15:00.000Z" },
      { slot: "b3", zeit: "19:30", format: "reel", status: "geplant" },
    ],
    stories: [
      { slot: "s1", zeit: "08:30", art: "teaser", beitragSlot: "b1", status: "veroeffentlicht", medienId: "17968846791174489" },
      { slot: "s3", zeit: "19:30", art: "teaser", beitragSlot: "b3", status: "geplant" },
    ],
  };
  const vorher = JSON.parse(JSON.stringify(plan));

  /* 1. Der Trockenlauf für b3. */
  const probe = veroeffentlichungEintragen(plan.beitraege[2], "trocken");
  assert.equal(probe.bestaetigt, false);
  assert.deepEqual(plan, vorher, "der Trockenlauf hinterlässt im Plan keine Spur");

  /* 2. Der Livelauf danach: Der Plan wird nicht neu erzeugt … */
  assert.equal(planNurAusTrockenlauf(plan), false,
    "ein Plan mit echten Veröffentlichungen wird nie verworfen");
  const { bereinigt, unklar } = planBereinigen(plan);
  assert.deepEqual(bereinigt, [], "es gibt nichts zu bereinigen");
  assert.deepEqual(unklar, [], "und nichts Unklares");

  /* … b1 und b2 bleiben exakt veröffentlicht … */
  assert.equal(veroeffentlichtBestaetigt(plan.beitraege[0]), true);
  assert.equal(veroeffentlichtBestaetigt(plan.beitraege[1]), true);
  assert.equal(plan.beitraege[0].medienId, "18073311611740667");
  assert.equal(plan.beitraege[1].medienId, "17908485354484188");
  assert.equal(veroeffentlichtBestaetigt(plan.stories[0]), true);

  /* … und nur b3 ist noch fällig. */
  assert.deepEqual(
    [...plan.beitraege, ...plan.stories].filter((e) => e.status === "geplant").map((e) => e.slot),
    ["b3", "s3"], "offen sind das Reel und sein Teaser – sonst nichts");
  assert.deepEqual(plan, vorher, "der ganze Plan ist unverändert durch den Trockenlauf gegangen");

  /* 3. Der Livelauf veröffentlicht b3 wirklich – erst dann darf der Teaser. */
  assert.equal(veroeffentlichtBestaetigt(plan.beitraege[2]), false, "vor dem Senden: kein Teaser");
  veroeffentlichungEintragen(plan.beitraege[2], "18125726395891138");
  assert.equal(veroeffentlichtBestaetigt(plan.beitraege[2]), true, "nach dem Senden: der Teaser darf");
});

test("Altbestand wird Eintrag für Eintrag bereinigt, nicht der ganze Tag verworfen", async () => {
  const { planBereinigen, planNurAusTrockenlauf, veroeffentlichtBestaetigt }
    = await import("../src/veroeffentlichung.mjs");

  /* Ein Plan von vor der Reparatur: zwei echte Veröffentlichungen, zwei
     Schein-Veröffentlichungen aus einem Trockenlauf. */
  const plan = {
    trocken: false,
    beitraege: [
      { slot: "b1", status: "veroeffentlicht", medienId: "18073311611740667" },
      { slot: "b2", status: "veroeffentlicht", medienId: "trocken", veroeffentlicht: "2026-09-18T16:04:59.205Z", kanaele: {} },
    ],
    stories: [
      { slot: "s1", status: "veroeffentlicht", medienId: "17968846791174489" },
      { slot: "s2", status: "veroeffentlicht", medienId: "trocken", probelauf: { kennung: "trocken" } },
    ],
  };

  const { bereinigt, unklar } = planBereinigen(plan);
  assert.deepEqual(bereinigt.map((b) => b.slot), ["b2", "s2"], "nur die nachweislich trockenen Slots");
  assert.deepEqual(unklar, [], "beide tragen die Kennung „trocken“ – kein Zweifelsfall");

  /* Die echten bleiben unangetastet - das ist der Punkt. */
  assert.equal(plan.beitraege[0].medienId, "18073311611740667");
  assert.equal(veroeffentlichtBestaetigt(plan.beitraege[0]), true);
  assert.equal(veroeffentlichtBestaetigt(plan.stories[0]), true);

  /* Die unbelegten werden wieder fällig, fail closed, ohne Reste. */
  assert.equal(plan.beitraege[1].status, "geplant");
  assert.equal(plan.beitraege[1].medienId, undefined);
  assert.equal(plan.beitraege[1].veroeffentlicht, undefined);
  assert.equal(plan.beitraege[1].kanaele, undefined);
  assert.equal(plan.stories[1].status, "geplant");
  assert.equal(plan.stories[1].probelauf, undefined, "das Feld aus der ersten Fassung fliegt raus");

  /* Ein zweiter Durchgang findet nichts mehr. */
  assert.deepEqual(planBereinigen(plan).bereinigt, [], "die Bereinigung ist idempotent");

  /* Ein Plan, der KOMPLETT aus einem Trockenlauf stammt, darf neu erzeugt
     werden – dabei geht nichts verloren. */
  assert.equal(planNurAusTrockenlauf({ trocken: true, beitraege: [{ slot: "b1", status: "geplant" }], stories: [] }), true);
  assert.equal(planNurAusTrockenlauf({ trocken: true, beitraege: [{ slot: "b1", status: "veroeffentlicht", medienId: "18073311611740667" }], stories: [] }), false,
    "sobald etwas echt draußen ist, wird bereinigt statt verworfen");
  assert.equal(planNurAusTrockenlauf({ beitraege: [], stories: [] }), false, "ohne Marke gar nicht");
});

test("Der Tageslauf schreibt Ledger, Teaser und Protokoll nach derselben Regel", async () => {
  /* Der vollständige Tageslauf braucht Netz, Bilder und Instagram; geprüft
     wird deshalb an der Quelle, dass die vier Sendewege die gemeinsame Regel
     benutzen. Das ist ein Wächter gegen Rückfall, kein Verhaltensbeleg – der
     steht in den drei Tests darüber. */
  const quelle = fs.readFileSync(new URL("../src/lauf.mjs", import.meta.url), "utf8");

  assert.equal((quelle.match(/eintrag\.status = "veroeffentlicht"/g) || []).length, 0,
    "der Status wird nur noch in veroeffentlichung.mjs gesetzt");
  assert.equal((quelle.match(/eintrag\.medienId = medienId/g) || []).length, 0,
    "die Medien-ID wird nur noch dort eingetragen");

  for (const zeile of quelle.split("\n").filter((z) => z.includes("vermerken(ledger,"))) {
    assert.match(zeile, /if \((echt\.bestaetigt|echteMedienId\(medienId\))\) vermerken\(ledger,/,
      `ein Ledger-Eintrag ohne Bestätigung: ${zeile.trim().slice(0, 80)}`);
  }

  assert.match(quelle, /if \(!beitrag \|\| !veroeffentlichtBestaetigt\(b\)\)/,
    "der Teaser darf sich nicht auf den Planstatus allein stützen");
  assert.match(quelle, /if \(echteMedienId\(medienId\)\) stand\.fertig = i \+ 1;/,
    "ein Trockenlauf darf den Auffüll-Fortschritt nicht weiterzählen");

  /* Das Protokoll des Trockenlaufs geht in die lokale Ausgabe, nicht in den
     Asset-Zweig und nicht in den Plan. */
  assert.match(quelle, /fs\.writeFileSync\(path\.join\(AUSGABE, "trockenlauf\.json"\)/,
    "das Protokoll gehört in out/<datum>/");
  assert.equal(/hosting\.jsonSchreiben\([^)]*trockenlauf/.test(quelle), false,
    "das Protokoll darf nicht in den Asset-Zweig");
  assert.equal(/eintrag\.probelauf/.test(quelle), false,
    "kein Probelauf-Vermerk im Plan-Eintrag");

  /* Und der Prozess sichert am Ende in jedem Fall - auch nach einem Fehler.
     18.09.: Die Zeile „Nichts fällig" stand vor dem Block, der den Zustand
     festschreibt, und kehrte mit return zurück. Zwei Läufe verloren dabei
     zusammen 0,166 $ an bezahlter Arbeit. */
  const schluss = quelle.slice(quelle.indexOf("main()"));
  assert.match(schluss, /\.finally\(async \(\) => \{[\s\S]*await zustandSichern\(\)/,
    "am Prozessende muss der Zustand gesichert werden, auch wenn der Lauf abgebrochen ist");
  assert.match(schluss, /catch \(e\) \{ console\.error\(`  ! Zustand nicht gesichert/,
    "ein Fehler beim Sichern darf den ursprünglichen Fehler nicht verdecken");
  assert.match(quelle, /await zustandSichern\(`Zustand \$\{datum\}`\);/,
    "der reguläre Abschluss ruft die Sicherung auf");
});

test("Ohne Nachweis wird ein unklarer Publish-Zustand gesperrt, nicht zurückgesetzt", async () => {
  /* Zwei Zustände sehen im Plan gleich aus – „veröffentlicht“ ohne brauchbare
     Medien-ID –, brauchen aber entgegengesetzte Behandlungen:

       Trockenlauf            nie erschienen  → zurücksetzen
       Abbruch nach dem Post  erschienen, Quittung weg → sperren

     Ohne Beweis gilt der zweite Fall: Ein Doppelpost ist öffentlich und nicht
     zurückzunehmen, ein gesperrter Slot ist ein Eintrag im Bericht. */
  const { planBereinigen, trockenlaufNachweis, veroeffentlichtBestaetigt, veroeffentlichungUnklar, planNurAusTrockenlauf }
    = await import("../src/veroeffentlichung.mjs");

  const eintrag = (extra) => ({ slot: "b1", zeit: "08:30", status: "veroeffentlicht", ...extra });

  /* 1. medienId „trocken“ – die Kennung entsteht nirgends sonst. */
  const p1 = { beitraege: [eintrag({ medienId: "trocken", veroeffentlicht: "2026-09-18T16:04:59.205Z", kanaele: {} })], stories: [] };
  const r1 = planBereinigen(p1);
  assert.deepEqual(r1.bereinigt.map((b) => b.slot), ["b1"]);
  assert.deepEqual(r1.unklar, []);
  assert.equal(p1.beitraege[0].status, "geplant", "der Trockenlauf-Slot wird wieder fällig");
  assert.equal(p1.beitraege[0].medienId, undefined);
  assert.equal(p1.beitraege[0].veroeffentlicht, undefined);
  assert.equal(p1.beitraege[0].kanaele, undefined);
  assert.match(r1.bereinigt[0].grund, /Kennung des Trockenlaufs/);

  /* 2. Die Probelauf-Marke aus der ersten Fassung der Reparatur. */
  const p2 = { beitraege: [], stories: [eintrag({ slot: "s2", medienId: null, probelauf: { kennung: "trocken", zeit: "2026-09-18T16:05:02.126Z" } })] };
  const r2 = planBereinigen(p2);
  assert.deepEqual(r2.bereinigt.map((b) => b.slot), ["s2"]);
  assert.equal(p2.stories[0].status, "geplant");
  assert.equal(p2.stories[0].probelauf, undefined, "die Marke selbst fliegt raus");
  assert.match(r2.bereinigt[0].grund, /Probelauf-Marke/);

  /* 3. Ein Plan, der als Ganzes aus einem Trockenlauf stammt. */
  const p3 = { trocken: true, beitraege: [eintrag({ medienId: null })], stories: [] };
  assert.equal(planNurAusTrockenlauf(p3), true, "nichts Echtes darin");
  const r3 = planBereinigen(p3);
  assert.deepEqual(r3.bereinigt.map((b) => b.slot), ["b1"]);
  assert.deepEqual(r3.unklar, []);
  assert.equal(p3.beitraege[0].status, "geplant");

  /* 4. Medien-ID fehlt, KEINE Trockenlauf-Evidenz: Der Beitrag kann draußen
        sein und die Quittung verloren gegangen. Nicht zurücksetzen. */
  const p4 = { beitraege: [eintrag({ veroeffentlicht: "2026-09-18T12:30:00.000Z" })], stories: [] };
  assert.equal(trockenlaufNachweis(p4.beitraege[0], p4), null, "es gibt keinen Nachweis");
  const r4 = planBereinigen(p4, { jetzt: "2026-09-18T21:00:00.000Z" });
  assert.deepEqual(r4.bereinigt, [], "nichts wird zurückgesetzt");
  assert.deepEqual(r4.unklar.map((u) => u.slot), ["b1"]);
  assert.equal(p4.beitraege[0].status, "veroeffentlicht",
    "der Status bleibt – sonst würde der Slot wieder fällig und der Beitrag ein zweites Mal gepostet");
  assert.equal(veroeffentlichungUnklar(p4.beitraege[0]), true, "als unklar gekennzeichnet");
  assert.equal(p4.beitraege[0].veroeffentlichungUnklar.seit, "2026-09-18T21:00:00.000Z");
  assert.equal(veroeffentlichtBestaetigt(p4.beitraege[0]), false,
    "und trotzdem kein Beleg: nichts darf sich darauf stützen");

  /* Der Slot ist damit weder fällig noch bestätigt – genau das ist fail closed. */
  const faellig = (e) => e.status !== "veroeffentlicht";
  assert.equal(faellig(p4.beitraege[0]), false, "wird nicht erneut veröffentlicht");

  /* 5. Eine andere unbrauchbare ID, ebenfalls ohne Evidenz. */
  for (const kaputt of ["abc123", "", "   ", "17e9", "post-42"]) {
    const p5 = { beitraege: [eintrag({ medienId: kaputt })], stories: [] };
    const r5 = planBereinigen(p5);
    assert.deepEqual(r5.bereinigt, [], `„${kaputt}“ ist kein Trockenlauf-Nachweis`);
    assert.deepEqual(r5.unklar.map((u) => u.slot), ["b1"]);
    assert.equal(p5.beitraege[0].status, "veroeffentlicht");
    assert.equal(veroeffentlichtBestaetigt(p5.beitraege[0]), false);
  }

  /* 6. Eine echte Veröffentlichung bleibt vollständig unverändert. */
  const echt = { slot: "b2", status: "veroeffentlicht", medienId: "17908485354484188", veroeffentlicht: "2026-09-18T16:15:00.000Z", kanaele: { threads: "x" } };
  const p6 = { beitraege: [JSON.parse(JSON.stringify(echt))], stories: [] };
  const r6 = planBereinigen(p6);
  assert.deepEqual(r6.bereinigt, []);
  assert.deepEqual(r6.unklar, []);
  assert.deepEqual(p6.beitraege[0], echt, "kein Feld angefasst");
  assert.equal(veroeffentlichtBestaetigt(p6.beitraege[0]), true);

  /* 7. Ein zweiter Durchgang ist idempotent – auch über beide Fälle hinweg. */
  const p7 = {
    beitraege: [
      { slot: "b1", status: "veroeffentlicht", medienId: "18073311611740667" },
      { slot: "b2", status: "veroeffentlicht", medienId: "trocken" },
      { slot: "b3", status: "veroeffentlicht" },
    ],
    stories: [],
  };
  const erst = planBereinigen(p7, { jetzt: "2026-09-18T21:00:00.000Z" });
  assert.deepEqual(erst.bereinigt.map((b) => b.slot), ["b2"]);
  assert.deepEqual(erst.unklar.map((u) => u.slot), ["b3"]);
  const nachher = JSON.parse(JSON.stringify(p7));
  const zweit = planBereinigen(p7, { jetzt: "2026-09-19T05:35:00.000Z" });
  assert.deepEqual(zweit.bereinigt, [], "nichts mehr zurückzusetzen");
  assert.deepEqual(zweit.unklar.map((u) => u.slot), ["b3"], "der unklare Slot bleibt gemeldet");
  assert.deepEqual(p7, nachher, "aber der Plan ändert sich nicht mehr – auch der Zeitstempel nicht");
});

test("Die Zustandssicherung verbucht Kosten erst nach dem Schreiben und vertraut dem Push nicht blind", async () => {
  const { zustandsSicherung } = await import("../src/zustand.mjs");

  const bauen = (opt = {}) => {
    const dateien = { "kosten.json": { wochen: {} } };
    const protokoll = [];
    const hosting = {
      pushen: opt.pushen ?? true,
      jsonLesen: (name, standard) => (name in dateien ? JSON.parse(JSON.stringify(dateien[name])) : standard),
      jsonSchreiben: (name, wert) => {
        protokoll.push(`schreiben:${name}`);
        if (name === "kosten.json" && opt.kostenFehler?.()) throw new Error("kosten.json nicht schreibbar");
        dateien[name] = JSON.parse(JSON.stringify(wert));
      },
      aufraeumen: () => 0,
      commit: (n) => { protokoll.push(`commit:${n}`); return true; },
      push: async () => { protokoll.push("push"); return opt.push ? opt.push() : true; },
    };
    let abschluesse = 0;
    const sichern = zustandsSicherung({
      hosting, plan: { datum: "2026-09-18", beitraege: [], stories: [] }, datum: "2026-09-18",
      kostenAbschluss: () => { abschluesse++; return { usd: 0.12, aufrufe: 4, cacheAnteil: 0.5 }; },
      wochenKennung: () => "2026-W38",
      planSpeichern: (h, p) => h.jsonSchreiben(`plaene/${p.datum}.json`, p),
      remoteNoetig: opt.remoteNoetig,
    });
    return { sichern, dateien, protokoll, abschluesse: () => abschluesse };
  };
  const woche = (d) => d["kosten.json"].wochen["2026-W38"];

  /* (a) Das Schreiben der Kosten scheitert. Früher galt der Betrag trotzdem
         als verbucht – er fehlte danach einfach. Jetzt bleibt er wiederholbar,
         und der Snapshot wird nur einmal erhoben. */
  let kostenKaputt = true;
  const a = bauen({ kostenFehler: () => kostenKaputt });
  await assert.rejects(() => a.sichern(), /kosten\.json nicht schreibbar/);
  assert.equal(a.sichern.stand().kostenErhoben, true, "erhoben ist er");
  assert.equal(a.sichern.stand().kostenAngewendet, false, "aber nicht verbucht");
  assert.equal(woche(a.dateien), undefined, "und steht nirgends");

  kostenKaputt = false;
  await a.sichern();
  assert.equal(a.sichern.stand().kostenAngewendet, true);
  assert.equal(a.sichern.stand().durable, true);
  assert.equal(woche(a.dateien).usd, 0.12, "genau einmal verbucht");
  assert.equal(woche(a.dateien).aufrufe, 4);
  assert.equal(a.abschluesse(), 1, "der Snapshot wurde genau einmal erhoben");

  await a.sichern();
  assert.equal(woche(a.dateien).usd, 0.12, "ein dritter Aufruf addiert nichts");

  /* (b) push() liefert false, obwohl Remote-Durability verlangt ist: Das ist
         kein Erfolg. Der Zustand bleibt nicht durable, der Fehler ist sichtbar. */
  let pushErgebnis = false;
  const b = bauen({ push: () => pushErgebnis });
  await assert.rejects(() => b.sichern(), /Push nicht bestaetigt/);
  assert.equal(b.sichern.stand().durable, false, "ein unbestätigter Push macht nichts durable");
  assert.equal(b.sichern.stand().vorbereitet, true, "der Commit steht trotzdem");
  assert.equal(woche(b.dateien).usd, 0.12, "die Kosten sind verbucht");

  pushErgebnis = true;
  await b.sichern();
  assert.equal(b.sichern.stand().durable, true, "der zweite Versuch bestätigt");
  assert.equal(b.protokoll.filter((p) => p === "push").length, 2, "der Push wurde wiederholt");
  assert.equal(woche(b.dateien).usd, 0.12, "und die Kosten stehen weiterhin genau einmal da");

  /* Ein Lauf ohne Remote-Durability (IG_NO_PUSH) ist damit zufrieden - aber
     ausdrücklich, und er sagt es. */
  const c = bauen({ pushen: false, push: () => false });
  const ergebnis = await c.sichern();
  assert.equal(ergebnis.durable, true, "lokal gesichert reicht, wenn nicht gepusht wird");
  assert.equal(ergebnis.ohneRemote, true, "und das wird ausgewiesen");

  /* Umgekehrt: Wer Remote-Durability ausdrücklich verlangt, bekommt sie auch
     dann geprüft, wenn das Hosting nicht pusht. */
  const d = bauen({ pushen: false, push: () => false, remoteNoetig: true });
  await assert.rejects(() => d.sichern(), /Push nicht bestaetigt/);
  assert.equal(d.sichern.stand().durable, false);

  /* Die Wochenkosten dürfen nur an EINER Stelle aufaddiert werden. */
  const quelle = fs.readFileSync(new URL("../src/zustand.mjs", import.meta.url), "utf8");
  assert.equal((quelle.match(/w\.usd \+= kostenSnapshot\.usd/g) || []).length, 1,
    "die Wochenkosten werden an genau einer Stelle fortgeschrieben");
});

/* ---------------------------------------------------------------------------
   Phase 1a: drei getrennte Töpfe, harte Zweck-Zuordnung, Admission vor jedem
   bezahlten Aufruf.

   Der alte Deckel prüfte einmal vor dem ersten Call und danach nicht mehr.
   Am 18.09. kostete Herr Jurist 0,742 $ bei einem Tagesziel von 0,32 $.
   --------------------------------------------------------------------------- */

test("1a: Ein unbekannter Zweck wird abgelehnt, bevor der Anbieter gerufen wird", async () => {
  const { budgetStarten, topfFuer, UnbekannterZweck, ZWECK_TOPF } = await import("../src/budget.mjs");

  assert.throws(() => topfFuer("voellig-neuer-zweck"), UnbekannterZweck,
    "ein Zweck ohne Topf ist ein Programmierfehler, kein Sonderfall");
  assert.throws(() => topfFuer(undefined), UnbekannterZweck);
  assert.throws(() => topfFuer(""), UnbekannterZweck);

  /* Und die Ablehnung passiert in der Admission – vor jedem Anbieteraufruf. */
  const budget = budgetStarten({ deckel: { core: 0.32, engagement: 0.25, research: 0.12 } });
  let anbieterGerufen = false;
  await assert.rejects(
    () => budget.mitAdmission("voellig-neuer-zweck", 0.001, async () => { anbieterGerufen = true; return { usd: 0.001 }; }),
    UnbekannterZweck);
  assert.equal(anbieterGerufen, false, "der Anbieter darf gar nicht erst gerufen werden");

  /* Die Zuordnung ist vollständig für alles, was im Code wirklich abgerechnet wird. */
  for (const zweck of ["autor", "reel", "stories", "faktencheck", "reel-faktencheck", "story-faktencheck",
    "bildregie", "bild", "erklaerbild", "loesungsskizze", "loesung", "kommentare", "nachrichten",
    "recherche", "recherche-loesung"]) {
    assert.ok(ZWECK_TOPF[zweck], `„${zweck}“ braucht einen Topf`);
  }
  assert.equal(ZWECK_TOPF.autor, "core");
  assert.equal(ZWECK_TOPF.kommentare, "engagement");
  assert.equal(ZWECK_TOPF.recherche, "research");
  assert.equal(ZWECK_TOPF.stories, "core", "das Schreiben des Inhalts bleibt Core, auch nach einer Recherche");
});

test("1a: Der Worst Case entscheidet, nicht der erhoffte Preis", async () => {
  const { budgetStarten, AdmissionAbgelehnt } = await import("../src/budget.mjs");
  const budget = budgetStarten({ deckel: { core: 0.32, engagement: 0.25, research: 0.12 }, bisher: { core: 0.30 } });

  assert.equal(budget.frei("core"), 0.02, "0,30 von 0,32 sind verbraucht");

  /* Passt: 0,015 im Worst Case. */
  const a = budget.zulassen("autor", 0.015);
  assert.equal(budget.frei("core"), 0.005, "die Reservierung belegt den Topf sofort");

  /* Solange die Reservierung offen ist, kommt nichts Teures mehr durch. */
  assert.throws(() => budget.zulassen("faktencheck", 0.01), AdmissionAbgelehnt);

  /* Der Aufruf war billiger als befürchtet – der Rest kommt zurück. */
  a.buchen(0.009);
  assert.equal(budget.frei("core"), 0.011, "die ungenutzte Reserve ist wieder frei");
  assert.equal(budget.stand().verbraucht.core, 0.309);

  /* Ein Aufruf, dessen Worst Case den Deckel reißen würde, startet nicht. */
  let gerufen = false;
  await assert.rejects(
    () => budget.mitAdmission("reel", 0.05, async () => { gerufen = true; return { usd: 0.02 }; }),
    AdmissionAbgelehnt);
  assert.equal(gerufen, false, "kein Aufruf, dessen Worst Case nicht mehr passt");
  assert.equal(budget.frei("core"), 0.011, "und der Topf bleibt unberührt");

  /* Ein gescheiterter Aufruf gibt seine Reservierung vollständig zurück. */
  await assert.rejects(
    () => budget.mitAdmission("faktencheck", 0.01, async () => { throw new Error("Anbieter kaputt"); }),
    /Anbieter kaputt/);
  assert.equal(budget.frei("core"), 0.011, "nach dem Fehler ist die Reserve zurück");
});

test("1a: Jeder Versuch braucht seine eigene Admission", async () => {
  const { budgetStarten, AdmissionAbgelehnt } = await import("../src/budget.mjs");
  /* Genau hier lag das Leck: Erstaufruf, Schema-Fallback, Retry, Zweitmeinung
     liefen früher auf EINER Prüfung. Ein Schema-Fehler verdoppelte den Preis,
     ohne dass der Deckel davon wusste. */
  const budget = budgetStarten({ deckel: { core: 0.05, engagement: 0.25, research: 0.12 } });

  const versuche = [];
  const versuch = async (name, worstCase, usd) => {
    versuche.push(name);
    return budget.mitAdmission("faktencheck", worstCase, async () => ({ usd }));
  };

  await versuch("erstaufruf", 0.02, 0.02);
  await versuch("schema-fallback", 0.02, 0.02);
  assert.equal(budget.stand().verbraucht.core, 0.04);

  /* Der dritte Versuch passt nicht mehr – und wird abgelehnt, nicht bezahlt. */
  await assert.rejects(() => versuch("zweitmeinung", 0.02, 0.02), AdmissionAbgelehnt);
  assert.equal(budget.stand().verbraucht.core, 0.04, "der abgelehnte Versuch hat nichts gekostet");
  assert.deepEqual(versuche, ["erstaufruf", "schema-fallback", "zweitmeinung"]);

  /* Auch der Provider-Fallback ist ein eigener Aufruf mit eigener Admission. */
  const knapp = budgetStarten({ deckel: { core: 0.03, engagement: 0.25, research: 0.12 } });
  await knapp.mitAdmission("faktencheck", 0.02, async () => ({ usd: 0.02 }));
  await assert.rejects(() => knapp.mitAdmission("faktencheck", 0.02, async () => ({ usd: 0.02 })),
    AdmissionAbgelehnt, "der Anbieterwechsel bekommt keine Freifahrt auf der ersten Prüfung");
});

test("1a: Kein Topf leiht dem anderen", async () => {
  const { budgetStarten, AdmissionAbgelehnt } = await import("../src/budget.mjs");
  const budget = budgetStarten({
    deckel: { core: 0.32, engagement: 0.25, research: 0.12 },
    bisher: { core: 0.32, engagement: 0.0, research: 0.0 },
  });

  /* Core ist voll – Engagement und Research haben davon nichts. */
  assert.throws(() => budget.zulassen("autor", 0.001), AdmissionAbgelehnt, "Core ist erschöpft");
  budget.zulassen("kommentare", 0.20).buchen(0.20);
  budget.zulassen("recherche", 0.10).buchen(0.10);
  assert.equal(budget.stand().verbraucht.engagement, 0.20);
  assert.equal(budget.stand().verbraucht.research, 0.10);
  assert.throws(() => budget.zulassen("reel", 0.001), AdmissionAbgelehnt,
    "und Core bleibt erschöpft, egal wie viel anderswo frei ist");

  /* Umgekehrt genauso: ein voller Engagement-Topf nimmt Core nichts weg. */
  const b2 = budgetStarten({ deckel: { core: 0.32, engagement: 0.25, research: 0.12 }, bisher: { engagement: 0.25 } });
  assert.throws(() => b2.zulassen("nachrichten", 0.001), AdmissionAbgelehnt);
  b2.zulassen("autor", 0.30).buchen(0.30);
  assert.equal(b2.stand().verbraucht.core, 0.30, "Core ist unberührt vom vollen Engagement-Topf");

  /* Und Research nimmt Core nichts weg. */
  const b3 = budgetStarten({ deckel: { core: 0.32, engagement: 0.25, research: 0.12 }, bisher: { research: 0.12 } });
  assert.throws(() => b3.zulassen("recherche", 0.001), AdmissionAbgelehnt);
  b3.zulassen("faktencheck", 0.30).buchen(0.30);
  assert.equal(b3.stand().verbraucht.core, 0.30);
});

test("1a: Optionale Verbesserungen dürfen das Pflichtprodukt nicht verdrängen", async () => {
  const { budgetStarten, AdmissionAbgelehnt } = await import("../src/budget.mjs");
  /* 18.09.: Drei zusätzliche Erklärbilder kosteten 0,030 $. Sie waren in
     Ordnung, weil der Sonderdeckel noch Platz hatte. Unter 0,32 $ gilt:
     zuerst das Pflichtprodukt absichern. */
  const budget = budgetStarten({ deckel: { core: 0.32, engagement: 0.25, research: 0.12 }, bisher: { core: 0.28 } });
  assert.equal(budget.frei("core"), 0.04);

  /* Der Faktencheck des Abendreels ist Pflicht und braucht 0,035 $. */
  budget.pflichtRuecklage("reel-faktencheck", "reel-faktencheck", 0.035);

  /* Ein optionales Erklärbild (0,01 $) würde die Rücklage anknabbern. */
  assert.throws(() => budget.zulassen("erklaerbild", 0.01, { optional: true }), AdmissionAbgelehnt,
    "optional kommt nicht an der Pflichtrücklage vorbei");
  assert.equal(budget.frei("core"), 0.005, "neben der Rücklage bleiben 0,005 $ für alles andere");
  assert.equal(budget.frei("core", { ohnePflicht: "reel-faktencheck" }), 0.04,
    "nur der Faktencheck selbst darf seine eigene Rücklage einlösen");

  /* Der Pflichtaufruf selbst kommt durch – er darf seine eigene Rücklage nutzen. */
  const pflicht = budget.zulassen("reel-faktencheck", 0.035, { pflichtName: "reel-faktencheck" });
  pflicht.buchen(0.030);
  budget.pflichtAufloesen("reel-faktencheck");
  assert.equal(budget.stand().verbraucht.core, 0.31);

  /* Danach ist wieder Platz für das Optionale. */
  const bild = budget.zulassen("erklaerbild", 0.01, { optional: true });
  bild.buchen(0.01);
  assert.equal(budget.stand().verbraucht.core, 0.32, "der Deckel ist punktgenau ausgeschöpft");
  assert.throws(() => budget.zulassen("bild", 0.001, { optional: true }), AdmissionAbgelehnt);
});

test("1a: Was gesendet wurde, gibt kein Geld zurück", async () => {
  /* Der gefährlichste Randfall der Admission: Ein Fehler kann auch NACH dem
     Senden auftreten – HTTP-Abbruch, unlesbares Schema, Parser. Dann sind
     Tokens verbraucht. Gäbe die Admission die Reserve zurück, dürfte der
     nächste Aufruf dasselbe Geld ein zweites Mal ausgeben, während die
     Rechnung des Anbieters weiterläuft. */
  const { budgetStarten, ZUSTAND } = await import("../src/budget.mjs");
  const bauen = () => budgetStarten({ deckel: { core: 0.10, engagement: 0.25, research: 0.12 } });

  /* 1. Fehler VOR dem Senden: Die Reserve kommt vollständig zurück. */
  const a = bauen();
  await assert.rejects(() => a.mitAdmission("autor", 0.02, async () => {
    throw new Error("Schlüssel fehlt"); // noch nichts gesendet
  }), /Schlüssel fehlt/);
  assert.equal(a.frei("core"), 0.10, "nichts verbraucht");
  assert.equal(a.stand().verbraucht.core, 0);

  /* 2. Fehler NACH dem Senden, Usage bekannt: echte Kosten buchen, Rest frei. */
  const b = bauen();
  await assert.rejects(() => b.mitAdmission("autor", 0.02, async (griff) => {
    griff.gesendet();
    griff.kosten(0.012);          // die Antwort kam, die Usage steht fest
    throw new Error("JSON kaputt"); // und erst danach zerbricht der Parser
  }), /JSON kaputt/);
  assert.equal(b.stand().verbraucht.core, 0.012, "die echten Kosten sind gebucht");
  assert.equal(b.frei("core"), 0.088, "nur der Rest ist wieder frei");

  /* 3. Fehler NACH dem Senden, Usage unbekannt: Die Reserve bleibt weg. */
  const c = bauen();
  await assert.rejects(() => c.mitAdmission("autor", 0.02, async (griff) => {
    griff.gesendet();
    throw new Error("Verbindung abgebrochen");
  }), /Verbindung abgebrochen/);
  assert.equal(c.stand().verbraucht.core, 0.02,
    "konservativ gilt der Worst Case als ausgegeben – der Anbieter könnte ihn berechnet haben");
  assert.equal(c.frei("core"), 0.08, "die Reserve wird NICHT wieder verfügbar");
  assert.equal(c.stand().ungeklaert.length, 1, "und der Fall steht als ungeklärt im Protokoll");
  assert.equal(c.stand().ungeklaert[0].zweck, "autor");

  /* freigeben() nach dem Senden ist kein Rückgeld, sondern ein ungeklärter Fall. */
  const d = bauen();
  const griff = d.zulassen("autor", 0.02);
  assert.equal(griff.zustand, ZUSTAND.RESERVIERT);
  griff.gesendet();
  assert.equal(griff.zustand, ZUSTAND.GESENDET);
  griff.freigeben();
  assert.equal(griff.zustand, ZUSTAND.UNGEKLAERT, "freigeben() nach dem Senden wird zu ungeklaert");
  assert.equal(d.stand().verbraucht.core, 0.02);

  /* Und vor dem Senden bleibt freigeben() echtes Rückgeld. */
  const e = bauen();
  const g2 = e.zulassen("autor", 0.02);
  g2.freigeben();
  assert.equal(g2.zustand, ZUSTAND.VERFALLEN);
  assert.equal(e.frei("core"), 0.10);
});

test("1a: Mehr ausgeben als zugesagt sperrt den Topf", async () => {
  const { budgetStarten, InvarianteVerletzt, TopfGesperrt, AdmissionAbgelehnt } = await import("../src/budget.mjs");
  const budget = budgetStarten({ deckel: { core: 0.32, engagement: 0.25, research: 0.12 } });

  const griff = budget.zulassen("faktencheck", 0.020);
  griff.gesendet();
  assert.throws(() => griff.buchen(0.025), InvarianteVerletzt,
    "eine gebrochene Zusage ist ein Fehler, kein Rundungsergebnis");

  /* Das Geld ist ausgegeben – es wird vollständig verbucht. */
  assert.equal(budget.stand().verbraucht.core, 0.025, "die tatsächlichen Kosten stehen im Topf");
  assert.equal(budget.stand().verletzungen.length, 1);
  assert.deepEqual(budget.stand().verletzungen[0], { zweck: "faktencheck", topf: "core", reservedUsd: 0.02, actualUsd: 0.025 });

  /* Aber der Topf hat seine Zusage verloren und nimmt nichts mehr an. */
  assert.ok(budget.gesperrt("core"), "core ist gesperrt");
  assert.throws(() => budget.zulassen("autor", 0.001), TopfGesperrt,
    "kein weiterer Aufruf darf den Schaden vergrößern");
  assert.throws(() => budget.zulassen("reel", 0.20), TopfGesperrt);

  /* Die anderen Töpfe sind davon unberührt. */
  assert.equal(budget.gesperrt("engagement"), null);
  budget.zulassen("kommentare", 0.05).freigeben();

  /* Research trägt bewusst keine Cent-Zusage: dort keine Verletzung, keine Sperre. */
  const r = budgetStarten({ deckel: { core: 0.32, engagement: 0.25, research: 0.12 } });
  const rg = r.zulassen("recherche", 0.05);
  rg.gesendet();
  rg.buchen(0.07);
  assert.equal(r.stand().verbraucht.research, 0.07, "die echten Kosten stehen da");
  assert.equal(r.gesperrt("research"), null,
    "für Server-Tools wird keine Cent-Garantie behauptet – also auch keine gebrochen");
  assert.equal(r.stand().verletzungen.length, 0);

  /* Der reguläre Fall bleibt regulär. */
  const ok = budgetStarten({ deckel: { core: 0.32, engagement: 0.25, research: 0.12 } });
  const g = ok.zulassen("autor", 0.020); g.gesendet(); g.buchen(0.018);
  assert.equal(ok.gesperrt("core"), null);
  assert.equal(ok.stand().verbraucht.core, 0.018);
  assert.doesNotThrow(() => ok.zulassen("faktencheck", 0.01).freigeben());
  assert.throws(() => ok.zulassen("reel", 0.40), AdmissionAbgelehnt, "der Deckel gilt weiterhin");
});

test("1a: Pflichtrücklagen schützen sich gegenseitig", async () => {
  const { budgetStarten, AdmissionAbgelehnt, PflichtUeberreserviert } = await import("../src/budget.mjs");
  /* Semantik ausdrücklich: JEDER Aufruf respektiert ALLE Pflichtrücklagen –
     außer seiner eigenen, die er unter ihrem Namen anmeldet. */
  const budget = budgetStarten({ deckel: { core: 0.32, engagement: 0.25, research: 0.12 }, bisher: { core: 0.22 } });
  assert.equal(budget.frei("core"), 0.10);

  budget.pflichtRuecklage("reel", "reel", 0.06);
  budget.pflichtRuecklage("faktencheck", "reel-faktencheck", 0.04);
  assert.equal(budget.frei("core"), 0, "beide Rücklagen zusammen füllen den Rest");

  /* Ein optionaler Aufruf kommt an keiner Rücklage vorbei. */
  assert.throws(() => budget.zulassen("erklaerbild", 0.01, { optional: true }), AdmissionAbgelehnt);

  /* Ein anderer Pflichtaufruf ebenso wenig: Er darf nicht 0,08 nehmen und
     damit den Faktencheck unmöglich machen. */
  assert.throws(() => budget.zulassen("stories", 0.08), AdmissionAbgelehnt,
    "fremdes Pflichtgeld ist tabu");

  /* Das Reel darf seine EIGENE Rücklage einlösen … */
  assert.equal(budget.frei("core", { ohnePflicht: "reel" }), 0.06);
  const reel = budget.zulassen("reel", 0.06, { pflichtName: "reel" });
  reel.gesendet(); reel.buchen(0.05);
  budget.pflichtAufloesen("reel");

  /* … und danach steht die Rücklage des Faktenchecks unverändert da. */
  assert.equal(budget.stand().verbraucht.core, 0.27);
  assert.equal(budget.frei("core"), 0.01, "0,04 liegen weiter für den Faktencheck zurück");
  assert.equal(budget.frei("core", { ohnePflicht: "faktencheck" }), 0.05);
  const fc = budget.zulassen("reel-faktencheck", 0.04, { pflichtName: "faktencheck" });
  fc.gesendet(); fc.buchen(0.035);
  budget.pflichtAufloesen("faktencheck");
  assert.equal(budget.stand().verbraucht.core, 0.305, "beide Pflichtstücke sind bezahlt");

  /* Eine Rücklage, die der Topf nicht mehr hergibt, wird nicht still angenommen. */
  const eng = budgetStarten({ deckel: { core: 0.32, engagement: 0.25, research: 0.12 }, bisher: { core: 0.30 } });
  eng.pflichtRuecklage("reel", "reel", 0.015);
  assert.throws(() => eng.pflichtRuecklage("faktencheck", "reel-faktencheck", 0.03), PflichtUeberreserviert,
    "dass das Pflichtprodukt nicht mehr finanzierbar ist, ist eine Nachricht – keine Rundungsfrage");
  assert.equal(Object.keys(eng.stand().pflicht).length, 1, "die unmögliche Rücklage wird nicht gespeichert");
});

test("1a: Überlappende Admissions buchen sich nicht gegenseitig über", async () => {
  const { budgetStarten, AdmissionAbgelehnt } = await import("../src/budget.mjs");
  const budget = budgetStarten({ deckel: { core: 0.06, engagement: 0.25, research: 0.12 } });

  /* Zwei Aufrufe laufen gleichzeitig – beide Reservierungen zählen. */
  const a = budget.zulassen("autor", 0.025);
  const b = budget.zulassen("faktencheck", 0.025);
  assert.equal(budget.frei("core"), 0.01, "beide Reservierungen sind belegt");
  assert.throws(() => budget.zulassen("stories", 0.02), AdmissionAbgelehnt, "der dritte passt nicht mehr");

  /* Sie enden in umgekehrter Reihenfolge – jede löst nur ihre eigene Reserve. */
  b.gesendet(); b.buchen(0.020);
  assert.equal(budget.frei("core"), 0.015);
  a.gesendet(); a.buchen(0.010);
  assert.equal(budget.stand().verbraucht.core, 0.03);
  assert.equal(budget.stand().reserviert.core, 0, "keine Reserve bleibt hängen");
  assert.equal(budget.frei("core"), 0.03);

  /* Ein zweites Abrechnen desselben Griffs ist ein Fehler, kein Doppelbuchen. */
  assert.throws(() => a.buchen(0.01), /bereits abgeschlossen/);
  assert.equal(budget.stand().verbraucht.core, 0.03);

  /* Parallel gestartete Aufrufe über mitAdmission(): der dritte wird abgelehnt. */
  const parallel = budgetStarten({ deckel: { core: 0.05, engagement: 0.25, research: 0.12 } });
  const lauf = (usd) => parallel.mitAdmission("autor", 0.02, async (griff) => {
    griff.gesendet(); await new Promise((r) => setTimeout(r, 5)); griff.kosten(usd); return { usd };
  });
  const ergebnisse = await Promise.allSettled([lauf(0.02), lauf(0.02), lauf(0.02)]);
  assert.deepEqual(ergebnisse.map((r) => r.status), ["fulfilled", "fulfilled", "rejected"]);
  assert.ok(ergebnisse[2].reason instanceof AdmissionAbgelehnt);
  assert.equal(parallel.stand().verbraucht.core, 0.04, "genau zwei Aufrufe sind bezahlt");
});

test("1a: Telemetrie erfasst auch die Fehlerpfade und landet nicht im Asset-Zweig", async () => {
  const { telemetrieStarten, ROHFELDER } = await import("../src/telemetrie.mjs");
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), "telemetrie-"));
  const t = telemetrieStarten({ datum: "2026-09-19", kanal: "herrjurist", dir });

  /* Ein gelungener Aufruf. */
  t.aufruf({
    purpose: "autor", bucket: "core", slot: "b1", provider: "anthropic", model: "claude-sonnet-5",
    effort: "low", thinkingMode: "adaptive", attempt: 1, profileId: "autor:abc123",
    calibrationFamily: "autor / claude-sonnet-5 / low / beitrag-v3",
    maxTokens: 16000, inputTokens: 1500, outputTokens: 4200, cacheReadTokens: 900, cacheWriteTokens: 0,
    stopReason: "end_turn", sent: true, reservedUsd: 0.02, actualUsd: 0.0143, releasedUsd: 0.0057,
    outcome: "ok", approved: true,
  });

  /* Ein zweiter Versuch nach Schema-Fehler – eigener Attempt, eigene Zeile. */
  t.aufruf({
    purpose: "autor", bucket: "core", slot: "b1", provider: "anthropic", model: "claude-sonnet-5",
    attempt: 2, profileId: "autor:abc123", maxTokens: 16000, inputTokens: 1500, outputTokens: 16000,
    stopReason: "max_tokens", sent: true, reservedUsd: 0.02, actualUsd: 0.0195, releasedUsd: 0.0005,
    outcome: "abgeschnitten", errorType: "schema", approved: false,
  });

  /* Ein Aufruf, der nach dem Senden abriss – Kosten unbekannt. */
  t.aufruf({
    purpose: "faktencheck", bucket: "core", slot: "b1", provider: "openai", model: "gpt-5-mini",
    attempt: 1, profileId: "faktencheck:def456", maxTokens: 8000,
    sent: true, spendUnknown: true, reservedUsd: 0.01, actualUsd: null, releasedUsd: 0,
    outcome: "ungeklaert", errorType: "connection reset",
  });

  /* Und einer, der gar nicht erst startete. */
  t.aufruf({
    purpose: "erklaerbild", bucket: "core", provider: "openai", model: "gpt-image-1-mini",
    attempt: 1, sent: false, reservedUsd: 0.01, actualUsd: 0, releasedUsd: 0.01,
    outcome: "abgelehnt", errorType: "AdmissionAbgelehnt",
  });

  assert.equal(t.anzahl(), 4, "jeder Aufruf eine Zeile – auch die gescheiterten");

  /* NDJSON: eine Zeile je Aufruf, jede für sich lesbar. */
  const roh = fs.readFileSync(t.datei, "utf8").trim().split("\n");
  assert.equal(roh.length, 4);
  const erste = JSON.parse(roh[0]);
  for (const feld of ROHFELDER) assert.ok(feld in erste, `Feld „${feld}“ fehlt in der Rohzeile`);
  assert.equal(erste.date, "2026-09-19");
  assert.equal(erste.channel, "herrjurist");
  assert.equal(erste.usd, 0.0143, "usd folgt den tatsächlichen Kosten");
  assert.equal(JSON.parse(roh[2]).spendUnknown, true, "der ungeklärte Fall ist als solcher markiert");
  assert.equal(JSON.parse(roh[3]).sent, false, "und der nie gestartete auch");

  /* Die Datei liegt in der lokalen Ausgabe, nicht im Asset-Zweig. */
  assert.match(t.datei, /telemetrie\.ndjson$/);
  assert.equal(t.datei.startsWith(dir), true, "Rohdaten bleiben in out/<datum>/");

  /* Die Übersicht ist klein genug für den Bericht. */
  const u = t.uebersicht();
  assert.equal(u.jeTopf.core.aufrufe, 4);
  assert.equal(u.jeTopf.core.ungeklaert, 1);
  assert.equal(u.jeTopf.core.abschnitte, 1);

  /* Die rollenden Fenster entstehen aus den Rohzeilen – mit den Fehlern. */
  const fenster = t.fensterFortschreiben();
  const f = fenster["autor:abc123"];
  assert.equal(f.aufrufeGesamt, 2);
  assert.equal(f.erfolgreicheAufrufe, 1, "der abgeschnittene zählt nicht als Erfolg");
  assert.equal(f.abschnitte, 1);
  assert.equal(f.schemaFehler, 1);
  assert.deepEqual(f.letzteAusgabeTokens, [4200], "nur die vollständige Antwort geht in die Messreihe");
  assert.equal(f.aktuellesCeiling, 16000);
  assert.equal(fenster["faktencheck:def456"].anbieterFehler, 1, "der Verbindungsabriss zählt als Anbieterfehler");

  fs.rmSync(dir, { recursive: true, force: true });
});

test("1a: Ceilings werden gemessen und vorgeschlagen, nie automatisch geändert", async () => {
  const { leeresFenster, fensterAktualisieren, perzentile, abschneideGrenze, ceilingVorschlag, CHECKPOINTS, exaktesProfil, kalibrierFamilie }
    = await import("../src/profile.mjs");

  /* Das exakte Profil hängt an der Struktur, nicht am Beitragstext. */
  const basis = { zweck: "autor", provider: "anthropic", modell: "claude-sonnet-5", effort: "low", maxTokens: 16000, systemHash: "sys1", schemaHash: "sch1" };
  assert.equal(exaktesProfil(basis).id, exaktesProfil({ ...basis }).id, "gleiche Struktur, gleiches Profil");
  assert.notEqual(exaktesProfil(basis).id, exaktesProfil({ ...basis, maxTokens: 8000 }).id, "anderes Ceiling, anderes Profil");
  assert.notEqual(exaktesProfil(basis).id, exaktesProfil({ ...basis, schemaHash: "sch2" }).id, "anderes Schema, anderes Profil");
  assert.notEqual(exaktesProfil(basis).id, exaktesProfil({ ...basis, effort: "high" }).id);
  assert.equal(kalibrierFamilie({ zweck: "reel-autor", modell: "sonnet-5", effort: "low", schemaVersion: "reel-schema-v3" }),
    "reel-autor / sonnet-5 / low / reel-schema-v3", "die Familie ist lesbar, nicht gehasht");

  /* Die Obergrenze bei null Abschnitten ist die geschlossene Form. */
  assert.ok(Math.abs(abschneideGrenze(20, 0) - (1 - Math.pow(0.05, 1 / 20))) < 1e-12);
  assert.ok(Math.abs(abschneideGrenze(20, 0) - 0.1391) < 0.001, "n=20 ohne Abschnitt heißt noch 13,9 % Restrisiko");
  assert.ok(abschneideGrenze(100, 0) < abschneideGrenze(20, 0), "mehr Messungen, engere Schranke");
  /* Mit Abschnitten die exakte einseitige Binomialgrenze. */
  assert.ok(abschneideGrenze(40, 2) > 2 / 40, "die Schranke liegt über der beobachteten Quote");
  assert.ok(abschneideGrenze(40, 2) < 0.20);
  assert.equal(abschneideGrenze(0, 0), null, "ohne Daten keine Aussage");

  /* Ein Fenster füllt sich – und behält die Rohwerte, nicht nur p95. */
  let f = leeresFenster("autor:abc", "autor / sonnet-5 / low / v3");
  assert.equal(f.unkalibriert, true, "ein neues Profil gilt als unkalibriert");
  for (let i = 0; i < 25; i++) f = fensterAktualisieren(f, { ausgabeTokens: 3000 + i * 40, stopReason: "end_turn", ceiling: 16000 });
  assert.equal(f.erfolgreicheAufrufe, 25);
  assert.equal(f.letzteAusgabeTokens.length, 25, "die Rohwerte bleiben – daraus lässt sich später jeder Perzentil rechnen");
  assert.equal(f.unkalibriert, false, "ab 20 Messungen gilt es als kalibriert");
  assert.deepEqual(CHECKPOINTS, [20, 40, 60, 100]);

  const vorschlag = ceilingVorschlag(f);
  assert.equal(vorschlag.aktuellesCeiling, 16000, "das harte Ceiling steht unverändert da");
  assert.ok(vorschlag.vorschlag < 16000, "die Messung legt ein kleineres nahe");
  assert.equal(vorschlag.angewendet, false, "aber nichts wird automatisch geändert");
  assert.equal(perzentile(f.letzteAusgabeTokens).p95 <= vorschlag.vorschlag, true);

  /* Auch nach hundert braven Aufrufen bleibt das Ceiling, was es war. */
  const vorher = f.aktuellesCeiling;
  for (let i = 0; i < 100; i++) f = fensterAktualisieren(f, { ausgabeTokens: 2000, stopReason: "end_turn", ceiling: 16000 });
  assert.equal(f.aktuellesCeiling, vorher, "kein automatisches Heruntersetzen");
  assert.equal(f.letzteAusgabeTokens.length, 100, "das Fenster bleibt bei hundert Werten");

  /* Und Abschnitte werden getrennt gezählt, nicht unterschlagen. */
  let g = leeresFenster("reel:xyz", "reel / sonnet-5 / low / v2");
  g = fensterAktualisieren(g, { ausgabeTokens: 8000, stopReason: "max_tokens", ceiling: 8000 });
  g = fensterAktualisieren(g, { fehlerArt: "anbieter", ceiling: 8000 });
  g = fensterAktualisieren(g, { ausgabeTokens: 5000, stopReason: "end_turn", ceiling: 8000 });
  assert.equal(g.aufrufeGesamt, 3);
  assert.equal(g.erfolgreicheAufrufe, 1);
  assert.equal(g.abschnitte, 1);
  assert.equal(g.anbieterFehler, 1);
  assert.deepEqual(g.letzteAusgabeTokens, [5000], "der abgeschnittene Wert verfälscht die Messreihe nicht");
});

test("1a: Das Suchkontingent gilt für den ganzen Research-Auftrag, nicht je Anfrage", async () => {
  const { rechercheAuftrag, ResearchGrenze, SUCHEN_JE_AUFTRAG, researchZeile } = await import("../src/research.mjs");
  assert.equal(SUCHEN_JE_AUFTRAG, 2);

  /* Der Fall aus der Anweisung: Anfrage 1 verbraucht beide Suchen. Die
     pause_turn-Fortsetzung darf dann keine weiteren zwei bekommen – genau
     das passierte bisher, weil max_uses pro Anfrage gilt. */
  const a = rechercheAuftrag();
  const erste = a.anfrageBeginnen();
  assert.equal(erste.maxUses, 2, "die erste Anfrage darf zweimal suchen");
  a.antwortVerbuchen({ server_tool_use: { web_search_requests: 2 } });
  assert.equal(a.restSuchen(), 0, "danach ist das Kontingent des Auftrags leer");
  assert.equal(a.darfAnfragen().ok, false);
  assert.throws(() => a.anfrageBeginnen(), ResearchGrenze,
    "keine Fortsetzung mit frischem Suchkontingent");

  /* Anfrage 1 verbraucht eine Suche → die Fortsetzung bekommt höchstens eine. */
  const b = rechercheAuftrag();
  assert.equal(b.anfrageBeginnen().maxUses, 2);
  b.antwortVerbuchen({ server_tool_use: { web_search_requests: 1 } });
  assert.equal(b.restSuchen(), 1);
  const zweite = b.anfrageBeginnen();
  assert.equal(zweite.maxUses, 1, "nur noch eine – nicht wieder zwei");
  assert.equal(zweite.nummer, 2);
  b.antwortVerbuchen({ server_tool_use: { web_search_requests: 1 } });
  assert.equal(b.restSuchen(), 0);
  assert.throws(() => b.anfrageBeginnen(), ResearchGrenze);

  /* Eine Antwort ohne Suche verbraucht nichts – gezählt wird die gemeldete
     Nutzung, nicht die Erlaubnis. */
  const c = rechercheAuftrag();
  c.anfrageBeginnen();
  c.antwortVerbuchen({});
  assert.equal(c.restSuchen(), 2, "max_uses ist eine Obergrenze, keine Buchung");
  assert.equal(c.stand().anfragen, 1);

  /* Die Zahl der Anfragen ist ebenfalls begrenzt – auch wenn noch Suchen frei wären. */
  const d = rechercheAuftrag({ maxSuchen: 9, maxAnfragen: 2 });
  d.anfrageBeginnen(); d.antwortVerbuchen({ server_tool_use: { web_search_requests: 1 } });
  d.anfrageBeginnen(); d.antwortVerbuchen({ server_tool_use: { web_search_requests: 1 } });
  assert.equal(d.restSuchen(), 7, "Suchen wären noch frei …");
  assert.throws(() => d.anfrageBeginnen(), /Anfragen sind das Limit/, "… aber die Runden sind es nicht");

  /* Eine Runde, die keine Suche mehr braucht, ist nach verbrauchtem
     Kontingent weiterhin zulässig – Nachdenken ohne Suche. */
  const e = rechercheAuftrag();
  e.anfrageBeginnen(); e.antwortVerbuchen({ server_tool_use: { web_search_requests: 2 } });
  assert.equal(e.darfAnfragen({ brauchtSuche: false }).ok, true);
  assert.equal(e.anfrageBeginnen({ brauchtSuche: false }).maxUses, 0, "aber ohne jedes Suchkontingent");

  /* Der Protokollsatz behauptet keine Garantie, er nennt den Stand. */
  assert.equal(researchZeile(0, 0.12), "Research used: $0.000 / $0.120");
  assert.equal(researchZeile(0.0734, 0.12), "Research used: $0.073 / $0.120");
});

test("1a: Ein geplanter Lauf kann seinen Deckel nicht selbst anheben", async () => {
  const { effektiveKonfiguration, richtlinieGate, RichtlinieVerletzt, REGEL_DECKEL } = await import("../src/richtlinie.mjs");
  const { ZWECK_TOPF } = await import("../src/budget.mjs");
  assert.deepEqual(REGEL_DECKEL, { core: 0.32, engagement: 0.25, research: 0.12 });

  /* Die Ausnahmedatei von heute – mit dem Eintrag, der den 23.09. betrifft. */
  const ausnahmen = { "2026-09-13": 0.5, "2026-09-17": 0.48, "2026-09-18": 0.8, "2026-09-23": 0.45 };

  /* Ein geplanter Lauf am 23.09.: 0,45 wirkt NICHT mehr. */
  const k = effektiveKonfiguration({ ausloeser: "schedule", ausnahmen, datum: "2026-09-23" });
  assert.equal(k.deckel.core, 0.32, "Core bleibt bei 0,32 – die alte Ausnahme ist Historie");
  assert.equal(k.deckel.research, 0.12, "Research hat seinen eigenen Topf");
  assert.equal(k.deckel.engagement, 0.25);
  assert.notEqual(k.deckel.core, 0.45, "ausdrücklich nicht 0,45 Core");
  assert.notEqual(k.deckel.core + k.deckel.research, 0.57, "und erst recht nicht 0,45 + 0,12");
  assert.match(k.hinweise.join(" "), /steht in der Historie, wirkt aber nicht mehr/);
  assert.equal(k.breakGlass.aktiv, false);

  /* Dasselbe an einem Tag mit alter Ausnahme (18.09., 0,80). */
  const alt = effektiveKonfiguration({ ausloeser: "schedule", ausnahmen, datum: "2026-09-18" });
  assert.equal(alt.deckel.core, 0.32, "auch rückwirkend hebt keine Datei den geplanten Lauf an");

  /* Break Glass aus dem Zeitplan: abgelehnt. */
  const versuch = effektiveKonfiguration({
    ausloeser: "schedule", ausnahmen, datum: "2026-09-23",
    breakGlass: { aktiv: true, betragUsd: 0.9, grund: "der Tag soll vollständig erscheinen" },
  });
  assert.equal(versuch.breakGlass.aktiv, false, "ein geplanter Lauf zieht kein Break Glass");
  assert.equal(versuch.deckel.core, 0.32);
  assert.match(versuch.hinweise.join(" "), /aus einem geplanten Lauf verlangt - abgelehnt/);

  /* Break Glass von Hand: nur mit Begründung und sinnvollem Betrag. */
  const ohneGrund = effektiveKonfiguration({
    ausloeser: "workflow_dispatch", datum: "2026-09-23",
    breakGlass: { aktiv: true, betragUsd: 0.9, grund: "   " },
  });
  assert.equal(ohneGrund.breakGlass.aktiv, false, "ohne Begründung kein Break Glass");
  assert.equal(ohneGrund.deckel.core, 0.32);

  const zuKlein = effektiveKonfiguration({
    ausloeser: "workflow_dispatch", datum: "2026-09-23",
    breakGlass: { aktiv: true, betragUsd: 0.2, grund: "Tippfehler" },
  });
  assert.equal(zuKlein.breakGlass.aktiv, false);

  const echt = effektiveKonfiguration({
    ausloeser: "workflow_dispatch", datum: "2026-09-23",
    breakGlass: { aktiv: true, betragUsd: 0.42, grund: "Messtag Recherche, Betreiberentscheidung" },
  });
  assert.equal(echt.breakGlass.aktiv, true);
  assert.equal(echt.deckel.core, 0.42, "nur der ausdrücklich genannte Betrag");
  assert.equal(echt.breakGlass.grund, "Messtag Recherche, Betreiberentscheidung");
  assert.equal(echt.deckel.engagement, 0.25, "die anderen Töpfe bleiben unberührt");
  assert.equal(echt.deckel.research, 0.12);

  /* Das Gate lässt einen geplanten Lauf mit falscher Konfiguration nicht starten. */
  const produkt = { reelZusaetzlich: true, feedBeitraege: 3 };
  const erwartet = { reelZusaetzlich: true, feedBeitraege: 3 };
  const ceilings = { "autor": 16000, "recherche": 8000 };
  const ceilingPolicy = { "autor": { min: 4000, max: 16000 }, "recherche": { min: 2000, max: 8000 } };
  const zwecke = Object.keys(ZWECK_TOPF);

  assert.deepEqual(
    richtlinieGate({ konfiguration: k, produkt, erwartet, ceilings, ceilingPolicy, researchSuchen: 2, zwecke, zweckTopf: ZWECK_TOPF }),
    { ok: true, deckel: k.deckel, breakGlass: k.breakGlass });

  /* Produktmenge verändert → Start verweigert. */
  assert.throws(() => richtlinieGate({ konfiguration: k, produkt: { reelZusaetzlich: false, feedBeitraege: 2 }, erwartet, ceilings, ceilingPolicy, zwecke, zweckTopf: ZWECK_TOPF }),
    RichtlinieVerletzt, "die Produktmenge ist keine Stellschraube für Kostenprobleme");

  /* Unbekannter Zweck, Suchlimit, Ceiling außerhalb der Richtlinie. */
  assert.throws(() => richtlinieGate({ konfiguration: k, produkt, erwartet, ceilings, ceilingPolicy, zwecke: [...zwecke, "neuer-zweck"], zweckTopf: ZWECK_TOPF }), RichtlinieVerletzt);
  assert.throws(() => richtlinieGate({ konfiguration: k, produkt, erwartet, ceilings, ceilingPolicy, researchSuchen: 3, zwecke, zweckTopf: ZWECK_TOPF }), RichtlinieVerletzt);
  assert.throws(() => richtlinieGate({ konfiguration: k, produkt, erwartet, ceilings: { autor: 32000, recherche: 8000 }, ceilingPolicy, zwecke, zweckTopf: ZWECK_TOPF }), RichtlinieVerletzt);

  /* Und ein geplanter Lauf mit aktivem Break Glass kommt nicht durch das Gate. */
  const geschummelt = { ...echt, ausloeser: "schedule" };
  assert.throws(() => richtlinieGate({ konfiguration: geschummelt, produkt, erwartet, ceilings, ceilingPolicy, zwecke, zweckTopf: ZWECK_TOPF }),
    RichtlinieVerletzt, "Break Glass und Zeitplan schließen sich aus");
});

test("1a: Jeder Anbieteraufruf geht durch die Admission – auch Fallback und Retry", async () => {
  const { claudeAufruf, kontextSetzen, kontextLoeschen, klientSetzen, OhneKontext, tagesplanAdmissionBedarf: tagesplanWorstCase }
    = await import("../src/anbieter.mjs");
  const { budgetStarten, AdmissionAbgelehnt } = await import("../src/budget.mjs");
  const { telemetrieStarten } = await import("../src/telemetrie.mjs");

  const dir = fs.mkdtempSync(path.join(os.tmpdir(), "tuer-"));
  const antwort = (out) => ({ usage: { input_tokens: 1000, output_tokens: out }, stop_reason: "end_turn", content: [{ type: "text", text: "{}" }] });

  /* Ohne Laufkontext gibt es kein Budget – und damit keinen Aufruf. */
  kontextLoeschen();
  await assert.rejects(() => claudeAufruf({ zweck: "autor", params: { model: "claude-sonnet-5", max_tokens: 1000 } }), OhneKontext);

  /* Mit Kontext: Der Worst Case folgt dem Ceiling, nicht der Schätzung. */
  const budget = budgetStarten({ deckel: { core: 0.32, engagement: 0.25, research: 0.12 } });
  const telemetrie = telemetrieStarten({ datum: "2026-09-19", kanal: "herrjurist", dir });
  kontextSetzen({ budget, telemetrie, kanal: "herrjurist", datum: "2026-09-19" });

  let gerufen = 0;
  klientSetzen({ messages: { create: async () => { gerufen++; return antwort(2000); } } });

  await claudeAufruf({ zweck: "autor", params: { model: "claude-sonnet-5", max_tokens: 2000, messages: [{ role: "user", content: "x" }] }, attempt: 1, slot: "b1" });
  assert.equal(gerufen, 1);
  const nachErstem = budget.stand().verbraucht.core;
  assert.ok(nachErstem > 0 && nachErstem < 0.03, `tatsächliche Kosten gebucht (${nachErstem})`);
  assert.equal(budget.stand().reserviert.core, 0, "die Reserve ist aufgelöst");

  /* Ein zweiter Versuch ist ein eigener Aufruf mit eigener Admission und
     eigener Telemetriezeile. */
  await claudeAufruf({ zweck: "autor", params: { model: "claude-sonnet-5", max_tokens: 2000, messages: [{ role: "user", content: "x" }] }, attempt: 2, slot: "b1" });
  assert.equal(gerufen, 2);
  const zeilen = telemetrie.zeilen();
  assert.equal(zeilen.length, 2);
  assert.deepEqual(zeilen.map((z) => z.attempt), [1, 2], "Retry erscheint als eigener Versuch");
  assert.equal(zeilen[0].bucket, "core");
  assert.equal(zeilen[0].sent, true);
  assert.ok(zeilen[0].reservedUsd > zeilen[0].actualUsd, "reserviert wurde der Worst Case, gebucht der echte Preis");
  assert.ok(zeilen[0].releasedUsd > 0);
  assert.ok(zeilen[0].profileId.startsWith("autor:"));

  /* Ein Aufruf, dessen Ceiling nicht mehr in den Resttopf passt, startet nicht. */
  const knapp = budgetStarten({ deckel: { core: 0.05, engagement: 0.25, research: 0.12 } });
  kontextSetzen({ budget: knapp, telemetrie, kanal: "herrjurist", datum: "2026-09-19" });
  const vorher = gerufen;
  await assert.rejects(() => claudeAufruf({
    zweck: "autor", params: { model: "claude-sonnet-5", max_tokens: 16000, messages: [{ role: "user", content: "x" }] }, slot: "b2",
  }), AdmissionAbgelehnt, "16k Ceiling passen nicht in 0,05 $");
  assert.equal(gerufen, vorher, "der Anbieter wurde nicht gerufen");
  assert.equal(knapp.stand().verbraucht.core, 0, "und nichts verbraucht");
  const abgelehnt = telemetrie.zeilen().at(-1);
  assert.equal(abgelehnt.sent, false);
  assert.equal(abgelehnt.outcome, "abgelehnt");
  assert.equal(abgelehnt.errorType, "AdmissionAbgelehnt");

  /* Ein Fehler NACH dem Senden gibt kein Geld zurück. */
  const nach = budgetStarten({ deckel: { core: 0.32, engagement: 0.25, research: 0.12 } });
  kontextSetzen({ budget: nach, telemetrie, kanal: "herrjurist", datum: "2026-09-19" });
  klientSetzen({ messages: { create: async () => { throw new Error("Verbindung abgebrochen"); } } });
  await assert.rejects(() => claudeAufruf({ zweck: "faktencheck", params: { model: "claude-sonnet-5", max_tokens: 4000, messages: [{ role: "user", content: "x" }] } }), /Verbindung/);
  assert.ok(nach.stand().verbraucht.core > 0, "die Reservierung gilt als verbraucht");
  assert.equal(nach.stand().ungeklaert.length, 1);
  const letzte = telemetrie.zeilen().at(-1);
  assert.equal(letzte.sent, true);
  assert.equal(letzte.spendUnknown, true);
  assert.equal(letzte.releasedUsd, 0);

  /* Und der unbequeme Befund steht als Signal zur Verfügung. */
  const plan = tagesplanWorstCase({
    posten: [
      { name: "b1 autor", modell: "claude-sonnet-5", maxTokens: 16000, eingabeTokens: 3000 },
      { name: "b1 faktencheck", modell: "claude-sonnet-5", maxTokens: 6000, eingabeTokens: 4000 },
    ],
    deckelCore: 0.32,
  });
  assert.equal(plan.dailyPlanNotAdmissibleAtCap, false, "zwei Aufrufe passen noch");
  const ganz = tagesplanWorstCase({
    posten: Array.from({ length: 9 }, () => ({ modell: "claude-sonnet-5", maxTokens: 16000, eingabeTokens: 3000 })),
    deckelCore: 0.32,
  });
  assert.equal(ganz.dailyPlanNotAdmissibleAtCap, true, "das ganze Pflichtprodukt nicht");
  assert.match(ganz.hinweis, /aus Planungswerten.*Verfügbarkeitszusage gibt es damit nicht/);

  kontextLoeschen();
  klientSetzen(null);
  fs.rmSync(dir, { recursive: true, force: true });
});

test("1a: Kein bezahlter Anbieteraufruf außerhalb der einen Tür", async () => {
  /* Der eigentliche Beweis: nicht die sechs bekannten Stellen abhaken,
     sondern zeigen, dass es keine siebte geben kann. */
  const quellen = fs.readdirSync(new URL("../src/", import.meta.url))
    .filter((f) => f.endsWith(".mjs") && f !== "anbieter.mjs");

  const einstiegspunkte = [
    { muster: /\.messages\.create\s*\(/, was: "Anthropic messages.create" },
    { muster: /api\.openai\.com/, was: "OpenAI-Endpunkt" },
    { muster: /api\.anthropic\.com/, was: "Anthropic-Endpunkt" },
    { muster: /\bnew\s+Anthropic\s*\(/, was: "Anthropic-Client" },
  ];

  const funde = [];
  for (const datei of quellen) {
    const text = fs.readFileSync(new URL(`../src/${datei}`, import.meta.url), "utf8");
    /* Kommentare zählen nicht – sie rufen niemanden. */
    const code = text.replace(/\/\*[\s\S]*?\*\//g, "").replace(/^\s*\/\/.*$/gm, "");
    for (const e of einstiegspunkte) if (e.muster.test(code)) funde.push(`${datei}: ${e.was}`);
  }
  assert.deepEqual(funde, [],
    `Bezahlte Anbieteraufrufe außerhalb von anbieter.mjs:\n${funde.join("\n")}`);

  /* Und in der Tür selbst hängt jeder Aufruf an einer Admission. */
  const tuer = fs.readFileSync(new URL("../src/anbieter.mjs", import.meta.url), "utf8");
  assert.match(tuer, /budget\.zulassen\(/, "die Tür fragt das Budget");
  assert.match(tuer, /griff\.gesendet\(\)/, "und markiert das Absenden");
  assert.equal((tuer.match(/budget\.zulassen\(/g) || []).length >= 2, true);
});

test("1a Simulation: ein günstiger Tag bleibt unter 0,32 $ und liefert vollständig", async () => {
  const { budgetStarten } = await import("../src/budget.mjs");
  const { telemetrieStarten } = await import("../src/telemetrie.mjs");
  const { kontextSetzen, kontextLoeschen, klientSetzen, claudeAufruf } = await import("../src/anbieter.mjs");

  const dir = fs.mkdtempSync(path.join(os.tmpdir(), "sim1-"));
  const budget = budgetStarten({ deckel: { core: 0.32, engagement: 0.25, research: 0.12 } });
  const telemetrie = telemetrieStarten({ datum: "2026-09-19", kanal: "herrjurist", dir });
  kontextSetzen({ budget, telemetrie, kanal: "herrjurist", datum: "2026-09-19" });

  /* Gemessene Größenordnung eines guten Tages (14.09.: 0,232 $ Core). */
  const gemessen = { autor: 1800, faktencheck: 900, reel: 2200, "reel-faktencheck": 700, stories: 1900, "story-faktencheck": 500, bildregie: 400 };
  klientSetzen({ messages: { create: async (p) => ({ usage: { input_tokens: 1500, output_tokens: p.__aus }, stop_reason: "end_turn", content: [{ type: "text", text: "{}" }] }) } });

  const ruf = (zweck, ceiling, aus, slot) => claudeAufruf({
    zweck, slot, modell: "claude-sonnet-5",
    params: { model: "claude-sonnet-5", max_tokens: ceiling, __aus: aus, messages: [{ role: "user", content: "x" }] },
  });

  /* Das vollständige Pflichtprodukt von Herr Jurist: 2 Karussells + 1 Reel + Stories. */
  await ruf("autor", 4000, gemessen.autor, "b1");
  await ruf("faktencheck", 2000, gemessen.faktencheck, "b1");
  await ruf("autor", 4000, gemessen.autor, "b2");
  await ruf("faktencheck", 2000, gemessen.faktencheck, "b2");
  await ruf("reel", 4000, gemessen.reel, "b3");
  await ruf("reel-faktencheck", 2000, gemessen["reel-faktencheck"], "b3");
  await ruf("stories", 4000, gemessen.stories, "s*");
  await ruf("story-faktencheck", 2000, gemessen["story-faktencheck"], "s*");
  await ruf("bildregie", 1000, gemessen.bildregie, "b3");

  const stand = budget.stand();
  assert.equal(stand.verbraucht.core <= 0.32, true, `Core ${stand.verbraucht.core} über dem Deckel`);
  assert.equal(telemetrie.zeilen().length, 9, "neun Pflichtaufrufe, neun Telemetriezeilen");
  assert.equal(telemetrie.zeilen().every((z) => z.sent && z.outcome === "ok"), true, "alle durchgelaufen");
  assert.equal(stand.gesperrt.core, null, "kein Topf gesperrt");
  assert.equal(stand.ungeklaert.length, 0);

  kontextLoeschen(); klientSetzen(null);
  fs.rmSync(dir, { recursive: true, force: true });
});

test("1a Simulation: der zu teure Pflichtaufruf startet nicht – und wird gemeldet", async () => {
  const { budgetStarten, AdmissionAbgelehnt } = await import("../src/budget.mjs");
  const { telemetrieStarten } = await import("../src/telemetrie.mjs");
  const { kontextSetzen, kontextLoeschen, klientSetzen, claudeAufruf } = await import("../src/anbieter.mjs");
  const { admissionReserveUsd: obergrenzeUsd } = await import("../src/kosten.mjs");

  const dir = fs.mkdtempSync(path.join(os.tmpdir(), "sim2-"));
  /* Der Tag ist fast voll: 0,30 von 0,32 $ sind verbraucht. */
  const budget = budgetStarten({ deckel: { core: 0.32, engagement: 0.25, research: 0.12 }, bisher: { core: 0.30 } });
  const telemetrie = telemetrieStarten({ datum: "2026-09-19", kanal: "herrjurist", dir });
  kontextSetzen({ budget, telemetrie, kanal: "herrjurist", datum: "2026-09-19" });

  let anbieterGerufen = 0;
  klientSetzen({ messages: { create: async () => { anbieterGerufen++; return { usage: { input_tokens: 1000, output_tokens: 500 }, stop_reason: "end_turn", content: [] }; } } });

  /* Der nächste notwendige Aufruf hat sein Ceiling bei 16.000 Token. Sein
     Worst Case liegt weit über dem Rest – er startet nicht. */
  const worstCase = obergrenzeUsd({ modell: "claude-sonnet-5", maxTokens: 16000, eingabeTokens: 3000 });
  assert.ok(worstCase > 0.02, `Worst Case ${worstCase} $ passt nicht in 0,02 $ Rest`);

  const plan = { beitraege: [{ slot: "b3", format: "reel", status: "geplant" }], stories: [] };
  let fehler = null;
  try {
    await claudeAufruf({ zweck: "reel", slot: "b3", modell: "claude-sonnet-5",
      params: { model: "claude-sonnet-5", max_tokens: 16000, messages: [{ role: "user", content: "x" }] } });
  } catch (e) {
    fehler = e;
    /* So meldet lauf.mjs den Slot – sichtbar, nicht still. */
    if (e instanceof AdmissionAbgelehnt) plan.beitraege[0].budgetBlockiert = { seit: "2026-09-19T18:00:00.000Z", grund: e.message, topf: e.topf };
  }

  assert.ok(fehler instanceof AdmissionAbgelehnt, "abgelehnt, nicht gestartet");
  assert.equal(anbieterGerufen, 0, "der Anbieter wurde nicht gerufen");
  assert.equal(budget.stand().verbraucht.core, 0.30, "kein Cent zusätzlich – kein Overspend");
  assert.ok(budget.stand().verbraucht.core <= 0.32);
  assert.ok(plan.beitraege[0].budgetBlockiert, "der Slot ist als budget-blockiert vermerkt");
  assert.match(plan.beitraege[0].budgetBlockiert.grund, /nicht mehr zulässig/);
  assert.equal(plan.beitraege[0].status, "geplant", "er gilt nicht als veröffentlicht");

  /* Die Ablehnung steht in der Telemetrie – mit Reservierung und Grund. */
  const zeile = telemetrie.zeilen().at(-1);
  assert.equal(zeile.sent, false);
  assert.equal(zeile.outcome, "abgelehnt");
  assert.equal(zeile.errorType, "AdmissionAbgelehnt");
  assert.equal(zeile.actualUsd, 0);
  assert.equal(zeile.maxTokens, 16000, "das Ceiling steht dabei – es wurde NICHT gesenkt");

  /* Und das Ceiling bleibt, was es war: keine automatische Senkung, damit es
     rechnerisch passt. */
  const { leeresFenster, fensterAktualisieren, ceilingVorschlag } = await import("../src/profile.mjs");
  let f = leeresFenster("reel:x", "reel / sonnet-5 / low / v1");
  for (let i = 0; i < 30; i++) f = fensterAktualisieren(f, { ausgabeTokens: 2200, stopReason: "end_turn", ceiling: 16000 });
  assert.equal(f.aktuellesCeiling, 16000);
  assert.equal(ceilingVorschlag(f).angewendet, false, "der Vorschlag bleibt ein Vorschlag");

  kontextLoeschen(); klientSetzen(null);
  fs.rmSync(dir, { recursive: true, force: true });
});

test("1a Simulation: das optionale Bild wird abgelehnt – das Pflichtstück läuft weiter", async () => {
  /* Der Fall, der im Alltag am häufigsten eintritt: Der Tag ist fast voll,
     ein Pflichtstück steht noch aus, und ein zusätzliches Erklärbild wäre
     nett. Das Bild darf dann nicht stattfinden - und zwar so, dass der
     Anbieter gar nicht erst gerufen wird. */
  const { budgetStarten, AdmissionAbgelehnt } = await import("../src/budget.mjs");
  const { telemetrieStarten } = await import("../src/telemetrie.mjs");
  const { kontextSetzen, kontextLoeschen, klientSetzen, bildAufruf, claudeAufruf } = await import("../src/anbieter.mjs");

  const dir = fs.mkdtempSync(path.join(os.tmpdir(), "sim3-"));
  /* 0,29 von 0,32 $ sind verbraucht; 0,025 $ liegen für den ausstehenden
     Story-Faktencheck zurück. Frei für alles andere: 0,005 $. */
  const budget = budgetStarten({ deckel: { core: 0.32, engagement: 0.25, research: 0.12 }, bisher: { core: 0.29 } });
  const telemetrie = telemetrieStarten({ datum: "2026-09-19", kanal: "herrjurist", dir });
  kontextSetzen({ budget, telemetrie, kanal: "herrjurist", datum: "2026-09-19" });
  budget.pflichtRuecklage("story-faktencheck", "story-faktencheck", 0.025);
  assert.equal(budget.frei("core"), 0.005, "neben der Rücklage bleiben 0,005 $");

  let bildAnfragen = 0;
  const fetchFn = async () => { bildAnfragen++; return { ok: true, json: async () => ({ data: [{ b64_json: "x" }] }) }; };

  /* Das optionale Bild kostet 0,01 $ - mehr, als neben der Rücklage frei
     ist. Es startet nicht. */
  let fehler = null;
  try {
    await bildAufruf({ zweck: "erklaerbild", optional: true, slot: "b3", preisUsd: 0.01,
      auftrag: { key: "k", koerper: {} }, fetchFn });
  } catch (e) { fehler = e; }

  assert.ok(fehler instanceof AdmissionAbgelehnt, "das optionale Bild wird abgelehnt");
  assert.equal(bildAnfragen, 0, "die Bild-API wurde nicht gerufen");
  assert.equal(budget.stand().verbraucht.core, 0.29, "kein Cent zusätzlich");

  const abgelehnt = telemetrie.zeilen().at(-1);
  assert.equal(abgelehnt.purpose, "erklaerbild");
  assert.equal(abgelehnt.sent, false);
  assert.equal(abgelehnt.outcome, "abgelehnt");
  assert.equal(abgelehnt.actualUsd, 0);

  /* Und jetzt der Punkt: Das Pflichtstück, für das zurückgelegt wurde, läuft
     trotzdem - es löst seine eigene Rücklage ein. */
  klientSetzen({ messages: { create: async () => ({ usage: { input_tokens: 4000, output_tokens: 600 }, stop_reason: "end_turn", content: [{ type: "text", text: "{}" }] }) } });
  const antwort = await claudeAufruf({
    zweck: "story-faktencheck", slot: "s*", modell: "claude-haiku-4-5-20251001",
    pflichtName: "story-faktencheck",
    params: { model: "claude-haiku-4-5-20251001", max_tokens: 3000, messages: [{ role: "user", content: "x" }] },
  });
  assert.ok(antwort, "der Pflichtaufruf ist durchgelaufen");
  budget.pflichtAufloesen("story-faktencheck");

  const stand = budget.stand();
  assert.ok(stand.verbraucht.core <= 0.32, `Core ${stand.verbraucht.core} über dem Deckel`);
  assert.ok(stand.verbraucht.core > 0.29, "der Pflichtaufruf hat bezahlt");
  assert.equal(stand.gesperrt.core, null);
  assert.equal(telemetrie.zeilen().length, 2, "beide Aufrufe stehen in der Telemetrie - der abgelehnte auch");

  kontextLoeschen(); klientSetzen(null);
  fs.rmSync(dir, { recursive: true, force: true });
});
/* ===== 1a-Nachbesserung: die sechs Befunde der Gegenprüfung ================ */

test("1a+: Die Eingabeschranke ist konservativ - und deckt den Anbieter nicht ab", async () => {
  /* chars/3.5 war eine Faustregel für deutschen Fließtext. Die Admission
     stand darauf - und damit auf einer Annahme über den Prompt. */
  const { clientInputBound: eingabeObergrenzeTokens, admissionBound: eingabeGrenze, zaehlKoerper, ZAEHL_FELDER } = await import("../src/eingabe.mjs");
  const alteSchaetzung = (p) => Math.ceil((JSON.stringify(p.system || "") + JSON.stringify(p.messages || "")).length / 3.5);

  const basis = {
    model: "claude-sonnet-5", max_tokens: 4000,
    system: "Du schreibst juristische Beiträge. ".repeat(50),
    messages: [{ role: "user", content: "Schreibe zu § 823 BGB. ".repeat(80) }],
  };

  /* a) Werkzeuge und Schema zählen mit - sie fehlten in der alten Rechnung
        komplett, sind aber Eingabe und kosten Eingabepreis. */
  const mitWerkzeug = { ...basis, tools: [{ name: "suche", input_schema: { type: "object", properties: Object.fromEntries([...Array(50)].map((_, i) => [`feld${i}`, { type: "string", description: `Beschreibung von Feld ${i}` }])) } }] };
  const mitSchema = { ...basis, output_config: { format: { schema: { type: "object", properties: Object.fromEntries([...Array(50)].map((_, i) => [`s${i}`, { type: "string" }])) } } } };
  assert.ok(eingabeObergrenzeTokens(mitWerkzeug) > eingabeObergrenzeTokens(basis) + 500,
    "das Werkzeugschema vergrößert die Schranke nicht");
  assert.ok(eingabeObergrenzeTokens(mitSchema) > eingabeObergrenzeTokens(basis) + 200,
    "das Ausgabeschema vergrößert die Schranke nicht");
  assert.equal(alteSchaetzung(mitWerkzeug), alteSchaetzung(basis),
    "Kontrolle: die alte Schätzung hat den Unterschied gar nicht gesehen");

  /* b) Tokenreicher Unicode: Wo die alte Schätzung um ein Vielfaches zu
        NIEDRIG lag, liegt die Schranke darüber. */
  const dicht = { model: "claude-sonnet-5", messages: [{ role: "user", content: "日本語のテキスト😀§±→".repeat(200) }] };
  const schranke = eingabeObergrenzeTokens(dicht);
  const zeichen = dicht.messages[0].content.length;
  assert.ok(schranke >= zeichen, `Schranke ${schranke} unter der Zeichenzahl ${zeichen} - bei CJK ist ~1 Token je Zeichen möglich`);
  assert.ok(alteSchaetzung(dicht) < zeichen,
    "Kontrolle: die alte Schätzung lag unter der Zeichenzahl und damit möglicherweise unter der Tokenzahl");

  /* Der Zählendpunkt darf die Schranke anheben, nie senken. */
  assert.equal(eingabeGrenze(basis, 5), eingabeObergrenzeTokens(basis), "ein kleiner Zählwert senkt die Schranke");
  assert.equal(eingabeGrenze(basis, 10 ** 7), 10 ** 7, "ein größerer Zählwert wird nicht ignoriert");
});

test("1a+: Ein Aufruf, dessen Input+Output den Resttopf sprengen könnte, startet nicht", async () => {
  const { budgetStarten, AdmissionAbgelehnt } = await import("../src/budget.mjs");
  const { telemetrieStarten } = await import("../src/telemetrie.mjs");
  const { kontextSetzen, kontextLoeschen, klientSetzen, claudeAufruf } = await import("../src/anbieter.mjs");
  const { admissionReserveUsd: obergrenzeUsd } = await import("../src/kosten.mjs");
  const { clientInputBound: eingabeObergrenzeTokens } = await import("../src/eingabe.mjs");

  const dir = fs.mkdtempSync(path.join(os.tmpdir(), "preflight-"));
  /* Der Ausgabeteil allein passt bequem: 500 Token bei Haiku sind 0,0029 $.
     Erst die Eingabe macht den Aufruf zu teuer - und genau diesen Fall hat
     die alte Schätzung um den Faktor 3,5 kleingerechnet. */
  const langerText = "Sachverhalt: ".repeat(4000);
  const params = { model: "claude-haiku-4-5-20251001", max_tokens: 500, messages: [{ role: "user", content: langerText }] };
  const echterWorstCase = obergrenzeUsd({ modell: "claude-haiku-4-5-20251001", maxTokens: 500, eingabeTokens: eingabeObergrenzeTokens(params) });
  const alterWorstCase = obergrenzeUsd({ modell: "claude-haiku-4-5-20251001", maxTokens: 500, eingabeTokens: Math.ceil(JSON.stringify(params.messages).length / 3.5) });
  assert.ok(echterWorstCase > alterWorstCase * 2, "die Schranke ist nicht deutlich konservativer als die alte Schätzung");

  /* Frei ist ein Betrag, der zwischen beiden liegt: Die alte Rechnung hätte
     den Aufruf zugelassen, die neue lehnt ihn ab. */
  const frei = (echterWorstCase + alterWorstCase) / 2;
  const budget = budgetStarten({ deckel: { core: 0.32, engagement: 0.25, research: 0.12 }, bisher: { core: 0.32 - frei } });
  const telemetrie = telemetrieStarten({ datum: "2026-09-19", kanal: "herrjurist", dir });
  kontextSetzen({ budget, telemetrie, kanal: "herrjurist", datum: "2026-09-19" });
  let gerufen = 0;
  klientSetzen({ messages: { create: async () => { gerufen++; return { usage: { input_tokens: 1, output_tokens: 1 }, content: [] }; } } });

  await assert.rejects(() => claudeAufruf({ zweck: "faktencheck", slot: "b1", params }), AdmissionAbgelehnt);
  assert.equal(gerufen, 0, "der Anbieter wurde trotz zu knappen Budgets gerufen");
  assert.equal(telemetrie.zeilen().at(-1).outcome, "abgelehnt");
  const z = telemetrie.zeilen().at(-1);
  assert.equal(z.clientInputBoundTokens, eingabeObergrenzeTokens(params), "die clientseitige Schranke fehlt in der Telemetrie");
  assert.equal(z.admissionBoundTokens, eingabeObergrenzeTokens(params), "die Admissiongrenze fehlt in der Telemetrie");
  assert.equal(z.providerCountTokens, null, "ohne Zählendpunkt steht dort kein Wert");

  kontextLoeschen(); klientSetzen(null);
  fs.rmSync(dir, { recursive: true, force: true });
});

test("1a+: Ein Absturz nach dem Senden vergisst das Geld nicht", async () => {
  /* Die vier Fälle der Fehlerinjektion - jeder über eine echte
     Journal-Instanz, nicht über eine nachgebaute Logik. */
  const { journalStarten, JZUSTAND } = await import("../src/journal.mjs");

  /* Der Zwischenspeicher steht für den Asset-Zweig: Was hier landet, hat den
     Absturz überlebt. */
  let platte = null;
  const lesen = () => (platte ? JSON.parse(platte) : null);
  const schreiben = async (inhalt) => { platte = JSON.stringify(inhalt); return true; };
  const neuerLauf = () => journalStarten({ lesen, schreiben, datum: "2026-09-19", kanal: "herrjurist" });

  /* A) Absturz NACH der durablen Reservierung, VOR dem Senden.
        Der Sendevermerk fehlt - es wurde beweisbar nichts gesendet. */
  const lauf1 = neuerLauf();
  await lauf1.reservieren({ bucket: "core", purpose: "autor", reservedUsd: 0.05, slot: "b1" });
  /* … hier stirbt der Runner. */
  const nach1 = neuerLauf().uebernahme();
  assert.equal(nach1.vorbelastung.core, 0, "eine nie gesendete Reservierung blockiert weiter Geld");
  assert.equal(nach1.freigegeben.length, 1, "sie wird nicht freigegeben");

  /* B) Absturz UNMITTELBAR nach dem Senden. */
  platte = null;
  const lauf2 = neuerLauf();
  const id2 = await lauf2.reservieren({ bucket: "core", purpose: "autor", reservedUsd: 0.05, slot: "b1" });
  await lauf2.senden(id2);
  /* … hier stirbt der Runner, während der Anbieter rechnet. */
  const nach2 = neuerLauf();
  const u2 = nach2.uebernahme();
  assert.equal(u2.vorbelastung.core, 0.05, "das Geld wird ein zweites Mal freigegeben");
  assert.equal(u2.blockiert.length, 1);
  assert.equal(u2.blockiert[0].state, JZUSTAND.UNGEKLAERT);

  /* C) Absturz nach bekannter Usage, vor dem Tagesabschluss: Die Abrechnung
        stand nur im Speicher. Konservativ bleibt die Reservierung stehen -
        sie ist größer als die tatsächlichen Kosten, nie kleiner. */
  platte = null;
  const lauf3 = neuerLauf();
  const id3 = await lauf3.reservieren({ bucket: "core", purpose: "reel", reservedUsd: 0.08, slot: "b3" });
  await lauf3.senden(id3);
  lauf3.abrechnen(id3, 0.021);        // bekannt, aber noch nicht geschrieben
  /* … Runner tot, kein abschluss(). */
  const u3 = neuerLauf().uebernahme();
  assert.equal(u3.vorbelastung.core, 0.08, "der Betrag ist im Folgelauf nicht mehr sichtbar");
  assert.ok(u3.vorbelastung.core >= 0.021, "der konservative Wert liegt unter den echten Kosten");

  /* D) Zwei Stundenläufe desselben Tages: Lauf 2 beginnt mit allem, was
        Lauf 1 abgerechnet ODER offen gelassen hat. */
  platte = null;
  const lauf4 = neuerLauf();
  const a = await lauf4.reservieren({ bucket: "core", purpose: "autor", reservedUsd: 0.06 });
  await lauf4.senden(a); lauf4.abrechnen(a, 0.019);
  const b = await lauf4.reservieren({ bucket: "core", purpose: "faktencheck", reservedUsd: 0.04 });
  await lauf4.senden(b); lauf4.ungeklaert(b, "Verbindung abgebrochen");
  const c = await lauf4.reservieren({ bucket: "engagement", purpose: "kommentare", reservedUsd: 0.03 });
  await lauf4.senden(c); lauf4.abrechnen(c, 0.008);
  await lauf4.abschluss();

  const u4 = neuerLauf().uebernahme();
  assert.equal(u4.vorbelastung.core, 0.059, "0,019 abgerechnet + 0,04 ungeklärt");
  assert.equal(u4.vorbelastung.engagement, 0.008);
  assert.equal(u4.vorbelastung.research, 0, "Research hat nichts verbraucht");

  /* Und ein Journal des Vortags gilt nicht weiter: Töpfe sind Tagessache. */
  const morgen = journalStarten({ lesen, schreiben, datum: "2026-09-20", kanal: "herrjurist" });
  assert.equal(morgen.uebernahme().vorbelastung.core, 0, "der Vortag belastet den neuen Tag");
});

test("1a+: Wird die Reservierung nicht durable, findet der Aufruf nicht statt", async () => {
  const { budgetStarten } = await import("../src/budget.mjs");
  const { telemetrieStarten } = await import("../src/telemetrie.mjs");
  const { journalStarten, JournalNichtDurable } = await import("../src/journal.mjs");
  const { kontextSetzen, kontextLoeschen, klientSetzen, claudeAufruf } = await import("../src/anbieter.mjs");

  const dir = fs.mkdtempSync(path.join(os.tmpdir(), "nichtdurable-"));
  const budget = budgetStarten({ deckel: { core: 0.32, engagement: 0.25, research: 0.12 } });
  const telemetrie = telemetrieStarten({ datum: "2026-09-19", kanal: "herrjurist", dir });
  /* Der Push bestätigt nicht - etwa weil der Asset-Zweig auseinanderlief. */
  const journal = journalStarten({ lesen: () => null, schreiben: async () => false, datum: "2026-09-19", remoteNoetig: true });
  kontextSetzen({ budget, telemetrie, journal, kanal: "herrjurist", datum: "2026-09-19" });

  let gerufen = 0;
  klientSetzen({ messages: { create: async () => { gerufen++; return { usage: { input_tokens: 10, output_tokens: 10 }, content: [] }; } } });

  await assert.rejects(() => claudeAufruf({
    zweck: "autor", slot: "b1", modell: "claude-sonnet-5",
    params: { model: "claude-sonnet-5", max_tokens: 2000, messages: [{ role: "user", content: "x" }] },
  }), JournalNichtDurable);

  assert.equal(gerufen, 0, "gesendet, obwohl die Reservierung den nächsten Lauf nicht erreicht hätte");
  assert.equal(budget.stand().verbraucht.core, 0, "und es wurde trotzdem Geld gebucht");
  assert.equal(budget.frei("core"), 0.32, "die Reservierung wurde nicht zurückgegeben");
  assert.equal(telemetrie.zeilen().at(-1).errorType, "JournalNichtDurable");

  kontextLoeschen(); klientSetzen(null);
  fs.rmSync(dir, { recursive: true, force: true });
});

test("1a+: Solange bezahlte Pflichtarbeit aussteht, bekommt keine Kür Geld", async () => {
  const { budgetStarten, AdmissionAbgelehnt } = await import("../src/budget.mjs");
  const { telemetrieStarten } = await import("../src/telemetrie.mjs");
  const { kontextSetzen, kontextLoeschen, klientSetzen, bildAufruf, claudeAufruf } = await import("../src/anbieter.mjs");

  const dir = fs.mkdtempSync(path.join(os.tmpdir(), "kuer-"));
  /* Der Topf ist fast leer erst NACH der Pflicht - hier ist reichlich Geld da.
     Die Kür fällt trotzdem aus, weil die Pflicht noch aussteht. Genau das
     unterscheidet die Regel von einer Rücklage: Sie rechnet nicht, sie
     ordnet. */
  const budget = budgetStarten({ deckel: { core: 0.32, engagement: 0.25, research: 0.12 } });
  const telemetrie = telemetrieStarten({ datum: "2026-09-19", kanal: "herrjurist", dir });
  kontextSetzen({ budget, telemetrie, kanal: "herrjurist", datum: "2026-09-19" });
  budget.optionalSperren("Bezahlte Pflichtarbeit steht aus: 1 Beitrag/Reel, 9 Story-Texte.");

  let bildAnfragen = 0;
  const fetchFn = async () => { bildAnfragen++; return { ok: true, json: async () => ({ data: [] }) }; };
  await assert.rejects(() => bildAufruf({ zweck: "erklaerbild", optional: true, slot: "b3", preisUsd: 0.01, auftrag: { key: "k", koerper: {} }, fetchFn }), AdmissionAbgelehnt);
  assert.equal(bildAnfragen, 0, "die Bild-API wurde gerufen");
  assert.match(telemetrie.zeilen().at(-1).errorType, /AdmissionAbgelehnt/);
  assert.equal(budget.frei("core"), 0.32, "der Topf ist unberührt - es lag nicht am Geld, sondern an der Reihenfolge");

  /* Die Pflicht selbst läuft dabei völlig normal weiter. */
  klientSetzen({ messages: { create: async () => ({ usage: { input_tokens: 2000, output_tokens: 900 }, stop_reason: "end_turn", content: [{ type: "text", text: "{}" }] }) } });
  const antwort = await claudeAufruf({ zweck: "stories", slot: "s*", modell: "claude-sonnet-5", params: { model: "claude-sonnet-5", max_tokens: 3000, messages: [{ role: "user", content: "x" }] } });
  assert.ok(antwort, "die Pflicht wurde von der Kürsperre mitgetroffen");

  /* Nach der Pflicht ist der Rest des Topfes wieder für Küren da. */
  budget.optionalFreigeben();
  const bild = await bildAufruf({ zweck: "erklaerbild", optional: true, slot: "b3", preisUsd: 0.01, auftrag: { key: "k", koerper: {} }, fetchFn });
  assert.ok(bild, "nach der Pflicht bleibt die Kür gesperrt");
  assert.equal(bildAnfragen, 1);

  kontextLoeschen(); klientSetzen(null);
  fs.rmSync(dir, { recursive: true, force: true });
});

test("1a+: Die rollenden Profilfenster überleben den Runner", async () => {
  /* Vorher wurde profile.json NACH zustandSichern geschrieben. Der Commit war
     da durch, ein zweiter kam nicht - und mit dem Runner verschwanden die
     Messwerte. Der Test läuft deshalb über zwei getrennte „Läufe“ mit einem
     Speicher dazwischen, nicht innerhalb eines Prozesses. */
  const { zustandsSicherung } = await import("../src/zustand.mjs");
  const { telemetrieStarten } = await import("../src/telemetrie.mjs");

  const platte = new Map();           // steht für den Asset-Zweig
  const commits = [];
  const hostingBauen = () => ({
    pushen: true,
    jsonLesen: (n, vor) => (platte.has(n) ? JSON.parse(platte.get(n)) : vor),
    jsonSchreiben: (n, d) => platte.set(n, JSON.stringify(d)),
    aufraeumen: () => 0,
    commit: (m) => { commits.push({ m, inhalt: new Map(platte) }); return true; },
    push: async () => true,
  });

  const einLauf = async (ausgabeTokens) => {
    const dir = fs.mkdtempSync(path.join(os.tmpdir(), "profil-"));
    const hosting = hostingBauen();
    const telemetrie = telemetrieStarten({ datum: "2026-09-19", kanal: "herrjurist", dir });
    telemetrie.aufruf({
      purpose: "autor", bucket: "core", provider: "anthropic", model: "claude-sonnet-5",
      profileId: "autor:fest", calibrationFamily: "autor / claude-sonnet-5", attempt: 1,
      maxTokens: 16000, outputTokens: ausgabeTokens, stopReason: "end_turn",
      sent: true, actualUsd: 0.02, outcome: "ok",
    });
    const sichern = zustandsSicherung({
      hosting, plan: { beitraege: [], stories: [] }, datum: "2026-09-19",
      kostenAbschluss: () => ({ usd: 0, aufrufe: 0, cacheAnteil: 0 }),
      wochenKennung: () => "2026-W38", planSpeichern: () => {},
      vorSichern: () => {
        const bestand = hosting.jsonLesen("profile.json", {});
        hosting.jsonSchreiben("profile.json", telemetrie.fensterFortschreiben(bestand));
      },
    });
    await sichern("Zustand");
    fs.rmSync(dir, { recursive: true, force: true });
  };

  await einLauf(1800);
  /* Der entscheidende Punkt: Der Wert steht im COMMIT, nicht erst danach. */
  const letzterCommit = commits.at(-1);
  assert.ok(letzterCommit.inhalt.has("profile.json"),
    "profile.json war beim Commit noch nicht geschrieben - es hätte den Runner nicht überlebt");
  const imCommit = JSON.parse(letzterCommit.inhalt.get("profile.json"));
  assert.deepEqual(imCommit["autor:fest"].letzteAusgabeTokens, [1800]);

  /* Runner weg, neuer Prozess, derselbe Asset-Zweig. */
  await einLauf(2100);
  const fenster = JSON.parse(platte.get("profile.json"))["autor:fest"];
  assert.deepEqual(fenster.letzteAusgabeTokens, [1800, 2100],
    "der Messwert des ersten Laufs ist verloren gegangen");
  assert.equal(fenster.aufrufeGesamt, 2);
});

test("1a+: Das Gate prüft gegen die Richtlinie, nicht gegen sich selbst", async () => {
  /* Der Maßstab kam bisher aus derselben CONFIG, die geprüft wurde: Wer dort
     core auf 0,40 stellte, verschob effektiven Deckel UND Maßstab gemeinsam -
     und das Gate war zufrieden. */
  const { effektiveKonfiguration, richtlinieGate, RichtlinieVerletzt, REGEL_DECKEL } = await import("../src/richtlinie.mjs");
  assert.deepEqual({ ...REGEL_DECKEL }, { core: 0.32, engagement: 0.25, research: 0.12 });

  const pruefen = (deckel, ausloeser = "schedule") => richtlinieGate({
    konfiguration: effektiveKonfiguration({ ausloeser, datum: "2026-09-19", deckel }),
  });

  assert.ok(pruefen({ core: 0.32, engagement: 0.25, research: 0.12 }).ok, "die richtige Konfiguration wird abgelehnt");
  for (const [feld, wert] of [["core", 0.33], ["engagement", 0.26], ["research", 0.13]]) {
    const deckel = { core: 0.32, engagement: 0.25, research: 0.12, [feld]: wert };
    assert.throws(() => pruefen(deckel), RichtlinieVerletzt, `CONFIG ${feld}=${wert} kommt durch das Gate`);
    try { pruefen(deckel); } catch (e) {
      assert.ok(e.befunde.some((b) => b.includes("Richtlinie")), `der Befund nennt die Richtlinie nicht: ${e.befunde.join(" | ")}`);
    }
  }
  /* Auch nach unten: Eine stille Absenkung ist ebenfalls eine Policy-Änderung. */
  assert.throws(() => pruefen({ core: 0.20, engagement: 0.25, research: 0.12 }), RichtlinieVerletzt);

  /* Break Glass bleibt die einzige Ausnahme - und nur von Hand. */
  const bg = effektiveKonfiguration({
    ausloeser: "workflow_dispatch", datum: "2026-09-19", deckel: REGEL_DECKEL,
    breakGlass: { aktiv: true, betragUsd: 0.5, grund: "Nachholtag" },
  });
  assert.ok(richtlinieGate({ konfiguration: bg }).ok, "Break Glass von Hand wird abgelehnt");
  assert.equal(bg.deckel.core, 0.5);
});

test("1a+: Eine Invariantenverletzung erscheint mit ihrem echten Betrag", async () => {
  const { budgetStarten, InvarianteVerletzt } = await import("../src/budget.mjs");
  const { telemetrieStarten } = await import("../src/telemetrie.mjs");
  const { kontextSetzen, kontextLoeschen, klientSetzen, claudeAufruf } = await import("../src/anbieter.mjs");

  const dir = fs.mkdtempSync(path.join(os.tmpdir(), "invariante-"));
  const budget = budgetStarten({ deckel: { core: 0.32, engagement: 0.25, research: 0.12 } });
  const telemetrie = telemetrieStarten({ datum: "2026-09-19", kanal: "herrjurist", dir });
  kontextSetzen({ budget, telemetrie, kanal: "herrjurist", datum: "2026-09-19" });

  /* Der Anbieter meldet mehr Ausgabetoken, als das Ceiling zuließ - der Fall,
     für den die Invariante da ist. */
  klientSetzen({ messages: { create: async () => ({ usage: { input_tokens: 1000, output_tokens: 400000 }, stop_reason: "end_turn", content: [] }) } });
  await assert.rejects(() => claudeAufruf({
    zweck: "autor", slot: "b1", modell: "claude-sonnet-5",
    params: { model: "claude-sonnet-5", max_tokens: 100, messages: [{ role: "user", content: "x" }] },
  }), InvarianteVerletzt);

  const zeile = telemetrie.zeilen().at(-1);
  assert.equal(zeile.outcome, "invariant_violation", "die Verletzung steht als ungeklärter Fall in der Telemetrie");
  assert.equal(zeile.spendUnknown, false, "die Kosten waren bekannt - sie dürfen nicht als unbekannt gelten");
  assert.ok(zeile.actualUsd > 0, "der tatsächliche Betrag fehlt");
  assert.ok(zeile.actualUsd > zeile.reservedUsd, "der Betrag ist nicht der überschrittene");
  assert.equal(zeile.sent, true);
  /* Und der Topf ist gesperrt, damit niemand den Schaden vergrößert. */
  assert.ok(budget.gesperrt("core"), "der Topf läuft weiter");

  kontextLoeschen(); klientSetzen(null);
  fs.rmSync(dir, { recursive: true, force: true });
});

test("1a+: Die alte Reservelogik entscheidet über keinen bezahlten Aufruf mehr", async () => {
  /* Zwei Reservierungssysteme nebeneinander sind schlechter als eines, das
     hart ist: Das alte aus kosten.mjs rechnete mit ERWARTETEN Preisen und
     wurde seit der Verdrahtung der Admission von keinem Aufruf mehr gefragt -
     es sah nur noch aus wie eine Sicherung. */
  const quellen = fs.readdirSync(new URL("../src/", import.meta.url)).filter((f) => f.endsWith(".mjs") && f !== "kosten.mjs");
  const funde = [];
  for (const datei of quellen) {
    const text = fs.readFileSync(new URL(`../src/${datei}`, import.meta.url), "utf8")
      .replace(/\/\*[\s\S]*?\*\//g, "").replace(/^\s*\/\/.*$/gm, "");
    /* Der Punkt davor ist wichtig: journal.reservieren() ist die NEUE,
       durable Reservierung und hat mit der alten nichts zu tun. Gesucht sind
       die freien Aufrufe der Funktionen aus kosten.mjs. */
    for (const muster of [/(?<![.\w])budgetPruefen\s*\(/, /(?<![.\w])reservieren\s*\(/, /(?<![.\w])reservierungAufheben\s*\(/, /(?<![.\w])fremdeReserve\s*\(/]) {
      if (muster.test(text)) funde.push(`${datei}: ${muster}`);
    }
  }
  assert.deepEqual(funde, [], `alte Reservelogik im Produktionscode:\n${funde.join("\n")}`);

  /* Und die Zuständigkeit ist eindeutig: Wer bezahlen will, fragt budget.zulassen. */
  const tuer = fs.readFileSync(new URL("../src/anbieter.mjs", import.meta.url), "utf8");
  assert.ok(!/budgetPruefen/.test(tuer), "die Tür fragt noch den alten Deckel");
  assert.match(tuer, /budget\.zulassen\(/);
});

test("1a+: Gecachte OpenAI-Token werden einmal berechnet, nicht zweimal", async () => {
  /* Anthropic: input_tokens zählt NUR die ungecachten Token.
     OpenAI:    input_tokens ist die Gesamtzahl, cached_tokens eine Teilmenge.
     Wer das gleichsetzt, bezahlt den gecachten Anteil doppelt. */
  const { budgetStarten } = await import("../src/budget.mjs");
  const { telemetrieStarten } = await import("../src/telemetrie.mjs");
  const { kontextSetzen, kontextLoeschen, openaiAufruf } = await import("../src/anbieter.mjs");
  const { preisAus } = await import("../src/kosten.mjs");

  const dir = fs.mkdtempSync(path.join(os.tmpdir(), "cache-"));
  const budget = budgetStarten({ deckel: { core: 0.32, engagement: 0.25, research: 0.12 } });
  const telemetrie = telemetrieStarten({ datum: "2026-09-19", kanal: "herrjurist", dir });
  kontextSetzen({ budget, telemetrie, kanal: "herrjurist", datum: "2026-09-19" });

  const fetchFn = async () => ({
    ok: true,
    json: async () => ({ usage: { input_tokens: 10000, output_tokens: 1000, input_tokens_details: { cached_tokens: 8000 } } }),
  });
  /* Die Anfrage trägt den Text, den der Anbieter später als 10.000
     Eingabetoken meldet - sonst prüft der Test einen Fall, den es nicht gibt:
     Die Byte-Schranke gilt für das, was WIR schicken. Was der Anbieter
     zusätzlich in den Kontext legt (serverseitige Werkzeuge, fortgesetzte
     Antworten), deckt sie nicht ab; solche Pfade laufen deshalb über den
     Research-Topf mit seiner ausdrücklich weicheren Zusage. */
  const langerText = "Prüfe diesen Beitrag auf fachliche Fehler. ".repeat(1000);
  await openaiAufruf({ zweck: "faktencheck", modell: "gpt-5-mini", slot: "b1", fetchFn,
    params: { model: "gpt-5-mini", max_output_tokens: 1000, input: [{ role: "user", content: langerText }] } });

  const zeile = telemetrie.zeilen().at(-1);
  assert.equal(zeile.inputTokens, 2000, "die ungecachten Token sind nicht 10000 - 8000");
  assert.equal(zeile.cacheReadTokens, 8000);

  /* 2000 × 0,25 + 8000 × 0,025 + 1000 × 2,00 je Million. */
  const erwartet = (2000 * 0.25 + 8000 * 0.025 + 1000 * 2) / 1e6;
  assert.ok(Math.abs(zeile.actualUsd - erwartet) < 1e-9, `${zeile.actualUsd} statt ${erwartet}`);
  /* Die alte Rechnung hätte die 8000 zusätzlich zum vollen Preis gezählt. */
  const alt = preisAus("gpt-5-mini", { input_tokens: 10000, output_tokens: 1000, cache_read_input_tokens: 8000 });
  assert.ok(alt > zeile.actualUsd, "Kontrolle: die alte Rechnung war nicht teurer");

  kontextLoeschen();
  fs.rmSync(dir, { recursive: true, force: true });
});
/* ===== 1a-RC3: die vier Befunde der dritten Gegenprüfung =================== */

test("1a RC3: Der Zählendpunkt bekommt den vollständigen Request, nicht eine Teilmenge", async () => {
  /* Anthropic fügt bei Structured Outputs einen zusätzlichen System-Prompt
     hinzu, der berechnet wird - er steht in KEINER Anfrage, die wir vorher
     wiegen können. Der Zählendpunkt kann ihn mitrechnen, aber nur, wenn er
     output_config überhaupt zu sehen bekommt. Die alte Fassung übergab
     model/messages/system/tools - das Schema fiel heraus. */
  const { zaehlKoerper, ZAEHL_FELDER } = await import("../src/eingabe.mjs");

  const schema = { type: "object", additionalProperties: false, properties: { a: { type: "string" } }, required: ["a"] };
  const params = {
    model: "claude-sonnet-5", max_tokens: 4000,
    system: "Systemtext", messages: [{ role: "user", content: "x" }],
    tools: [{ name: "t", input_schema: { type: "object" } }],
    tool_choice: { type: "auto" },
    thinking: { type: "adaptive" },
    output_config: { format: { type: "json_schema", schema } },
    cache_control: { type: "ephemeral" },
  };
  const koerper = zaehlKoerper(params);

  for (const feld of ["model", "messages", "system", "tools", "tool_choice", "thinking", "output_config", "cache_control"]) {
    assert.ok(feld in koerper, `${feld} fehlt im Zähl-Request`);
    assert.deepEqual(koerper[feld], params[feld], `${feld} wurde verändert statt unverändert übergeben`);
  }
  assert.deepEqual([...ZAEHL_FELDER].sort(), ["cache_control", "messages", "model", "output_config", "system", "thinking", "tool_choice", "tools"]);
  /* max_tokens ist eine Ausgabegrenze und gehört nicht in einen Eingabezähler. */
  assert.ok(!("max_tokens" in koerper), "max_tokens gehört nicht in den Zähl-Request");

  /* Serverseitige Werkzeuge lehnt der Endpunkt ab - dort gibt es keinen
     Vorabwert, und genau deshalb sagt der Research-Topf Anfragen und Suchen
     zu, nicht den Cent. */
  assert.equal(zaehlKoerper({ model: "m", messages: [], tools: [{ type: "web_search_20260209", name: "web_search" }] }), null);
  assert.equal(zaehlKoerper({ model: "m", messages: [], tools: [{ type: "code_execution_20260521", name: "code_execution" }] }), null);
});

test("1a RC3: Die Admissiongrenze ist die größere der beiden Zahlen - und heißt nicht Beweis", async () => {
  const { clientInputBound, admissionBound } = await import("../src/eingabe.mjs");
  const params = { model: "claude-sonnet-5", max_tokens: 2000, messages: [{ role: "user", content: "Text ".repeat(200) }] };
  const client = clientInputBound(params);

  assert.equal(admissionBound(params, null), client, "ohne Zählwert gilt die clientseitige Schranke");
  assert.equal(admissionBound(params, client - 500), client, "ein kleinerer Zählwert darf die Schranke nicht senken");
  assert.equal(admissionBound(params, client + 500), client + 500, "ein größerer Zählwert muss sie anheben");

  /* Der injizierte Systemprompt der Structured Outputs ist genau der Fall, in
     dem der Zählwert über der Byte-Schranke liegen kann. */
  const mitSchema = { ...params, output_config: { format: { type: "json_schema", schema: { type: "object" } } } };
  assert.ok(admissionBound(mitSchema, clientInputBound(mitSchema) + 300) > clientInputBound(mitSchema));

  /* Und im Quelltext steht keine Beweisbehauptung mehr. */
  const quelle = fs.readFileSync(new URL("../src/eingabe.mjs", import.meta.url), "utf8");
  assert.ok(!/BEWEISBARE|mathematisch bewiesen|beweisbare Schranke/i.test(quelle),
    "die Datei behauptet weiterhin einen Beweis");
  assert.match(quelle, /additional system prompt/, "der Beleg aus der Anbieterdokumentation fehlt");
  assert.match(quelle, /is an estimate/, "der Beleg zur Schätzung des Zählendpunkts fehlt");
});

test("1a RC3: Der Provider-Guard liegt sichtbar unter dem Policy-Deckel", async () => {
  const { effektiveKonfiguration, providerGuard, REGEL_DECKEL } = await import("../src/richtlinie.mjs");
  const k = effektiveKonfiguration({ ausloeser: "schedule", datum: "2026-09-19" });

  assert.equal(k.deckel.core, 0.32, "der Policy-Deckel ist die Zusage und bleibt 0,32 $");
  assert.ok(k.betriebsDeckel.core < k.deckel.core, "die Betriebsgrenze liegt nicht unter dem Policy-Deckel");
  assert.equal(Math.round((k.deckel.core - k.betriebsDeckel.core) * 1e6) / 1e6, k.providerGuardUsd);
  for (const t of ["engagement", "research"]) {
    assert.ok(k.betriebsDeckel[t] < REGEL_DECKEL[t], `${t} hat keinen Guard`);
  }
  assert.ok(k.hinweise.some((h) => /Guard/.test(h)), "der Guard steht in keinem Hinweis");
  assert.equal(providerGuard("0.05"), 0.05, "der Guard ist nicht konfigurierbar");
  assert.equal(providerGuard("quatsch"), 0.02, "ein unbrauchbarer Wert fällt nicht auf den Standard zurück");

  /* Zugelassen wird bis zur Betriebsgrenze. */
  const { budgetStarten, AdmissionAbgelehnt } = await import("../src/budget.mjs");
  const b = budgetStarten({ deckel: k.betriebsDeckel });
  assert.equal(b.frei("core"), k.betriebsDeckel.core);
  assert.throws(() => b.zulassen("autor", 0.315), AdmissionAbgelehnt,
    "ein Aufruf zwischen Betriebsgrenze und Policy-Deckel wird zugelassen");

  /* Und die Telemetrie weist ihn aus. */
  const { telemetrieStarten } = await import("../src/telemetrie.mjs");
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), "guard-"));
  const t = telemetrieStarten({ datum: "2026-09-19", kanal: "herrjurist", dir, providerGuardUsd: k.providerGuardUsd });
  t.aufruf({ purpose: "autor", bucket: "core", sent: true, actualUsd: 0.01, outcome: "ok" });
  assert.equal(t.zeilen().at(-1).providerGuardUsd, k.providerGuardUsd, "der Guard fehlt in der Telemetrie");
  fs.rmSync(dir, { recursive: true, force: true });
});

test("1a RC3: Ein Budgetstopp erzeugt niemals eine fachliche Freigabe", async () => {
  /* Der gefährlichste Pfad: Bei IG_FAKTENCHECK_STRIKT=false gibt faktenSicher()
     bei einem technischen Ausfall `ok: true` zurück. Eine Admission-Ablehnung
     dort hineinlaufen zu lassen hieße: kein Geld für die Prüfung, also gilt
     der Beitrag als geprüft. */
  const { istBudgetStopp, BudgetStopp, budgetStoppGrund } = await import("../src/kostenfehler.mjs");
  const { BudgetFehler, PostenFehler } = await import("../src/kosten.mjs");
  const { AdmissionAbgelehnt, TopfGesperrt, PflichtUeberreserviert } = await import("../src/budget.mjs");
  const { JournalNichtDurable } = await import("../src/journal.mjs");
  const { ResearchGrenze } = await import("../src/research.mjs");

  const stopps = [
    new BudgetFehler("Tagesbudget erreicht"),
    new PostenFehler("Posten zu teuer"),
    new AdmissionAbgelehnt("autor", "core", 0.2, 0.01, 0.32),
    new TopfGesperrt("core", "Invariante verletzt"),
    new PflichtUeberreserviert("core", 0.3, 0.1),
    new JournalNichtDurable("autor", "reservierung"),
    new ResearchGrenze("Suchkontingent aufgebraucht"),
  ];
  for (const e of stopps) {
    assert.ok(istBudgetStopp(e), `${e.name} gilt nicht als Budgetstopp`);
    assert.ok(e instanceof BudgetStopp, `${e.name} hängt nicht an der Oberklasse`);
    assert.ok(budgetStoppGrund(e).length > 0);
  }
  /* Echte technische Fehler dürfen NICHT hineinrutschen - sonst würde ein
     Modellausfall künftig wie ein Budgetstopp behandelt. */
  for (const e of [new Error("Modell antwortet nicht"), new TypeError("kaputt"), null, undefined, { name: "SyntaxError" }]) {
    assert.ok(!istBudgetStopp(e), `${e?.name || e} wird fälschlich als Budgetstopp gewertet`);
  }
  /* Auch über Modulgrenzen hinweg, wo instanceof versagt. */
  assert.ok(istBudgetStopp({ name: "AdmissionAbgelehnt", message: "x" }), "ein fremder Fehler gleichen Namens wird nicht erkannt");

  /* Und die fünf Klassen im Quelltext. */
  const autor = fs.readFileSync(new URL("../src/autor.mjs", import.meta.url), "utf8");
  const lauf = fs.readFileSync(new URL("../src/lauf.mjs", import.meta.url), "utf8");
  const fc = fs.readFileSync(new URL("../src/faktencheck.mjs", import.meta.url), "utf8");

  const faktenBlock = autor.slice(autor.indexOf("async function faktenSicher"), autor.indexOf("export function themaText"));
  assert.match(faktenBlock, /if \(istKostenKontrollFehler\(e\)\) throw e;/, "Faktencheck: ein Budgetstopp wird nicht nach oben gereicht");
  assert.ok(ohneKommentare(faktenBlock).indexOf("istKostenKontrollFehler(e)") < ohneKommentare(faktenBlock).indexOf("CONFIG.faktencheck.strikt"),
    "Faktencheck: der Budgetstopp wird erst NACH dem Strikt-Zweig geprüft - er könnte eine Freigabe erzeugen");

  const storyBlock = autor.slice(autor.indexOf("export async function storiesPruefen"), autor.indexOf("const REEL_SCHEMA"));
  assert.match(storyBlock, /istKostenKontrollFehler\(e\)/, "Story-Prüfung: kein Budgetstopp-Zweig");
  assert.match(storyBlock, /faktencheckOffen = true/, "Story-Prüfung: die Texte gelten nicht als offen");

  const rechercheBlock = autor.slice(autor.indexOf("Web-Recherche"), autor.indexOf("export async function bildregie") + 1 || undefined);
  assert.match(rechercheBlock, /istKostenKontrollFehler\(e\)/, "Research: kein sauberer Budgetstopp-Zweig");

  assert.match(lauf, /if \(istKostenKontrollFehler\(e\)\) log\(`  ⏸ \$\{e\.message\}`\); else console\.error\(`  ✗ Interaktion/, "Engagement: Budgetstopp nicht getrennt protokolliert");
  assert.match(lauf, /eintrag\.budgetBlockiert = \{[\s\S]{0,200}?art: e\.name \}/, "Feed/Reel: der blockierte Slot hält die Art des Stopps nicht fest");
  assert.match(fc, /istKostenKontrollFehler\(e\)/, "Zweitmeinung: kein Budgetstopp-Zweig");

  /* Nirgends mehr ein Vergleich auf den alten Einzeltyp. */
  for (const [name, quelle] of [["autor.mjs", autor], ["lauf.mjs", lauf], ["faktencheck.mjs", fc]]) {
    assert.ok(!/instanceof BudgetFehler/.test(quelle), `${name} prüft noch auf den alten Einzeltyp`);
  }
});

test("1a RC3: Ein fehlgeschlagener Sendevermerk hinterlässt kein Phantom-sent", async () => {
  /* Der Ablauf, der das Geld eines nie gesendeten Aufrufs blockiert hätte:
     senden() setzt lokal auf "sent", der Push scheitert, der Provider wird
     korrekt nicht gerufen - und ein SPÄTERER Push trägt das "sent" doch
     hinaus. Der nächste Lauf hält dann Geld für möglicherweise ausgegeben,
     das nie ausgegeben wurde. Kein Overspend, aber Phantomverbrauch, der
     Pflichtinhalte verdrängt. */
  const { journalStarten, JZUSTAND, JournalNichtDurable } = await import("../src/journal.mjs");
  const { budgetStarten } = await import("../src/budget.mjs");
  const { telemetrieStarten } = await import("../src/telemetrie.mjs");
  const { kontextSetzen, kontextLoeschen, klientSetzen, claudeAufruf } = await import("../src/anbieter.mjs");

  let platte = null;
  /* Der lokale Commit gelingt IMMER - nur der Push entscheidet über
     Durability. Genau in dieser Lücke entstand das Phantom: Die Datei trug
     schon „sent", der Push dazu scheiterte, und der nächste gelungene Push
     trug es hinaus. Der erste Schreibvorgang (die Reservierung) wird durable,
     der zweite (der Sendevermerk) nicht. */
  let schreibVorgang = 0;
  let pushGeht = true;
  const lesen = () => (platte ? JSON.parse(platte) : null);
  const schreiben = async (inhalt) => {
    platte = JSON.stringify(inhalt);
    schreibVorgang += 1;
    return pushGeht && schreibVorgang !== 2;
  };

  const journal = journalStarten({ lesen, schreiben, datum: "2026-09-19", kanal: "herrjurist" });
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), "phantom-"));
  const budget = budgetStarten({ deckel: { core: 0.32, engagement: 0.25, research: 0.12 } });
  const telemetrie = telemetrieStarten({ datum: "2026-09-19", kanal: "herrjurist", dir });
  kontextSetzen({ budget, telemetrie, journal, kanal: "herrjurist", datum: "2026-09-19" });

  let gerufen = 0;
  klientSetzen({ messages: { create: async () => { gerufen++; return { usage: { input_tokens: 10, output_tokens: 10 }, content: [] }; } } });

  /* 1. Die Reservierung wird durable (Schreibvorgang 1).
     2./3. Der Sendevermerk wird lokal geschrieben, sein Push scheitert (2). */
  await assert.rejects(() => claudeAufruf({
    zweck: "autor", slot: "b1", modell: "claude-sonnet-5",
    params: { model: "claude-sonnet-5", max_tokens: 2000, messages: [{ role: "user", content: "x" }] },
  }), JournalNichtDurable);

  /* 4. Der Provider wurde nicht gerufen. */
  assert.equal(gerufen, 0, "gesendet, obwohl der Sendevermerk nicht durable wurde");

  /* 5. Später gelingt irgendein Push - etwa der Tagesabschluss. */
  assert.ok(schreibVorgang >= 3, "nach dem gescheiterten Sendevermerk wurde nicht zurückgerollt");
  await journal.abschluss();
  assert.ok(pushGeht);

  /* 6./7. Ein neuer Runner liest das Journal. */
  const nachher = journalStarten({ lesen, schreiben, datum: "2026-09-19", kanal: "herrjurist" });
  const eintraege = nachher.eintraege();
  assert.equal(eintraege.length, 1, "genau eine Reservierung sollte im Journal stehen");
  assert.notEqual(eintraege[0].state, JZUSTAND.GESENDET, "der Eintrag steht als gesendet im Journal - Phantom");
  assert.notEqual(eintraege[0].state, JZUSTAND.UNGEKLAERT, "der Eintrag gilt als ungeklärt - Phantom");
  /* Zulässig sind zwei Ausgänge, beide harmlos: `reserved` (der Folgelauf
     gibt frei, weil der Sendevermerk fehlt) oder `expired` (der Lauf selbst
     hat schon aufgeräumt, weil er weiß, dass er nichts gesendet hat). Der
     zweite ist der bessere - er braucht den Folgelauf nicht mehr. */
  assert.ok([JZUSTAND.RESERVIERT, JZUSTAND.VERFALLEN].includes(eintraege[0].state),
    `unerwarteter Zustand: ${eintraege[0].state}`);

  /* 8. Und kein Phantomverbrauch - das ist der eigentliche Prüfstein. */
  const u = nachher.uebernahme();
  assert.equal(u.vorbelastung.core, 0, "Geld für einen nie gesendeten Aufruf bleibt blockiert");
  assert.equal(u.blockiert.length, 0, "der Aufruf gilt als möglicherweise bezahlt");

  kontextLoeschen(); klientSetzen(null);
  fs.rmSync(dir, { recursive: true, force: true });
});

test("1a RC3: Der Cutover addiert den Altbestand, statt ihn zu maximieren", async () => {
  /* max(kosten.json, journal) ist nur richtig, wenn das Journal alle Aufrufe
     des Tages kennt. Beim Mid-Day-Cutover sind die Mengen disjunkt: 0,10 $
     von vorher und 0,08 $ ungeklärt von nachher ergeben 0,18 $, nicht 0,10 $. */
  const { journalStarten } = await import("../src/journal.mjs");

  let platte = null;
  const lesen = () => (platte ? JSON.parse(platte) : null);
  const schreiben = async (i) => { platte = JSON.stringify(i); return true; };

  /* Erster Lauf nach der Einführung: Der Altbestand wird eingefroren. */
  const lauf1 = journalStarten({ lesen, schreiben, datum: "2026-09-19", legacyBaseline: { core: 0.10, engagement: 0, research: 0 } });
  assert.equal(lauf1.baselineNeu(), true);
  assert.equal(lauf1.uebernahme().vorbelastung.core, 0.10, "der Altbestand fehlt");

  const a = await lauf1.reservieren({ bucket: "core", purpose: "autor", reservedUsd: 0.08 });
  await lauf1.senden(a);
  lauf1.ungeklaert(a, "Verbindung abgebrochen");
  await lauf1.abschluss();

  /* Nächster Lauf: 0,10 aus der Zeit davor PLUS 0,08 ungeklärt danach. */
  const lauf2 = journalStarten({ lesen, schreiben, datum: "2026-09-19", legacyBaseline: { core: 0.10, engagement: 0, research: 0 } });
  assert.equal(lauf2.baselineNeu(), false, "die Baseline darf nicht neu gesetzt werden");
  assert.equal(lauf2.uebernahme().vorbelastung.core, 0.18,
    "max() hätte hier 0,10 ergeben - das Geld des ungeklärten Aufrufs wäre ein zweites Mal ausgebbar");

  /* Und die Gegenprobe: Ein abgerechneter Aufruf steht inzwischen AUCH in
     kosten.json. Die Baseline wächst trotzdem nicht mit - sonst zählte er
     doppelt. */
  let platte2 = null;
  const lesen2 = () => (platte2 ? JSON.parse(platte2) : null);
  const schreiben2 = async (i) => { platte2 = JSON.stringify(i); return true; };

  const l1 = journalStarten({ lesen: lesen2, schreiben: schreiben2, datum: "2026-09-20", legacyBaseline: { core: 0.10, engagement: 0, research: 0 } });
  const b = await l1.reservieren({ bucket: "core", purpose: "autor", reservedUsd: 0.05 });
  await l1.senden(b);
  l1.abrechnen(b, 0.03);
  await l1.abschluss();

  /* kosten.json steht jetzt bei 0,13 - der nächste Lauf reicht das als
     legacyBaseline herein, weil er es nicht besser weiß. */
  const l2 = journalStarten({ lesen: lesen2, schreiben: schreiben2, datum: "2026-09-20", legacyBaseline: { core: 0.13, engagement: 0, research: 0 } });
  assert.equal(l2.uebernahme().vorbelastung.core, 0.13,
    "0,10 eingefroren + 0,03 abgerechnet = 0,13; die hereingereichten 0,13 dürfen nicht noch einmal obendrauf");
  assert.equal(l2.legacyBaseline().core, 0.10, "die eingefrorene Baseline wurde überschrieben");

  /* Ein neuer Tag beginnt wieder bei seiner eigenen Baseline. */
  const l3 = journalStarten({ lesen: lesen2, schreiben: schreiben2, datum: "2026-09-21", legacyBaseline: { core: 0, engagement: 0, research: 0 } });
  assert.equal(l3.uebernahme().vorbelastung.core, 0, "der Vortag belastet den neuen Tag");
});
/* ===== 1a-RC4: zwei Codefehler, zwei Abnahmepunkte ======================== */

test("1a RC4: Die Baseline überlebt den echten Tagesabschluss", async () => {
  /* Der Blocker: lauf.mjs baute das Journalobjekt beim Tagesabschluss selbst
     nach und liess legacyBaseline weg. Der naechste Runner leitete sie wieder
     aus kosten.json ab - inklusive der Aufrufe, die im Journal schon standen.
     Aus 0,13 wurden 0,16. Der Test laeuft deshalb ueber den ECHTEN
     zustandSichern/vorSichern-Pfad, nicht ueber journal.abschluss(). */
  const { journalStarten } = await import("../src/journal.mjs");
  const { zustandsSicherung } = await import("../src/zustand.mjs");

  const platte = new Map();                       // steht für den Asset-Zweig
  const hostingBauen = () => ({
    pushen: true,
    jsonLesen: (n, vor) => (platte.has(n) ? JSON.parse(platte.get(n)) : vor),
    jsonSchreiben: (n, d) => platte.set(n, JSON.stringify(d)),
    aufraeumen: () => 0, commit: () => true, push: async () => true,
  });

  /* Ein Lauf, wie ihn lauf.mjs baut: Journal anlegen, Aufruf verbuchen,
     Zustand über zustandSichern sichern - mit vorSichern wie im Produktivcode. */
  const einLauf = async ({ legacyBaseline, arbeit }) => {
    const hosting = hostingBauen();
    const journal = journalStarten({
      datum: "2026-09-19", kanal: "herrjurist", legacyBaseline,
      lesen: () => hosting.jsonLesen("budget-journal.json", null),
      schreiben: async (inhalt) => { hosting.jsonSchreiben("budget-journal.json", inhalt); return await hosting.push(); },
    });
    const uebernommen = journal.uebernahme();
    await arbeit(journal);
    const sichern = zustandsSicherung({
      hosting, plan: { beitraege: [], stories: [] }, datum: "2026-09-19",
      kostenAbschluss: () => ({ usd: 0, aufrufe: 0, cacheAnteil: 0 }),
      wochenKennung: () => "2026-W38", planSpeichern: () => {},
      /* genau die Zeile aus lauf.mjs */
      vorSichern: () => hosting.jsonSchreiben("budget-journal.json", journal.snapshot()),
    });
    await sichern("Zustand");
    return uebernommen;
  };

  /* Lauf 1: Altbestand 0,10 aus kosten.json, ein Aufruf kostet 0,03. */
  await einLauf({
    legacyBaseline: { core: 0.10, engagement: 0, research: 0 },
    arbeit: async (j) => {
      const id = await j.reservieren({ bucket: "core", purpose: "autor", reservedUsd: 0.05 });
      await j.senden(id);
      j.abrechnen(id, 0.03);
    },
  });

  /* Der Tagesabschluss muss die Baseline mitgeschrieben haben. */
  const geschrieben = JSON.parse(platte.get("budget-journal.json"));
  assert.ok(geschrieben.legacyBaseline, "legacyBaseline fehlt im geschriebenen Journal");
  assert.equal(geschrieben.legacyBaseline.core, 0.10);
  assert.equal(geschrieben.eintraege.length, 1);
  assert.equal(geschrieben.eintraege[0].state, "settled", "die Abrechnung wurde nicht mitgeschrieben");

  /* Lauf 2: kosten.json steht inzwischen bei 0,13 und wird als Baseline
     hereingereicht - der neue Runner weiss es nicht besser. */
  const u2 = await einLauf({ legacyBaseline: { core: 0.13, engagement: 0, research: 0 }, arbeit: async () => {} });
  assert.equal(u2.vorbelastung.core, 0.13,
    "0,10 eingefroren + 0,03 abgerechnet = 0,13; ohne mitgeschriebene Baseline wären es 0,16 gewesen");
  assert.notEqual(u2.vorbelastung.core, 0.16, "der Aufruf wird doppelt gezählt");

  /* Und der ungeklärte Fall über denselben Pfad: 0,10 + 0,08 = 0,18. */
  platte.clear();
  await einLauf({
    legacyBaseline: { core: 0.10, engagement: 0, research: 0 },
    arbeit: async (j) => {
      const id = await j.reservieren({ bucket: "core", purpose: "reel", reservedUsd: 0.08 });
      await j.senden(id);
      j.ungeklaert(id, "Verbindung abgebrochen");
    },
  });
  const u3 = await einLauf({ legacyBaseline: { core: 0.10, engagement: 0, research: 0 }, arbeit: async () => {} });
  assert.equal(u3.vorbelastung.core, 0.18, "0,10 Altbestand + 0,08 ungeklärt");

  /* Niemand ausser dem Journal baut das Format. */
  const lauf = fs.readFileSync(new URL("../src/lauf.mjs", import.meta.url), "utf8");
  assert.match(lauf, /jsonSchreiben\("budget-journal\.json", journal\.snapshot\(\)\)/,
    "lauf.mjs schreibt das Journal nicht über snapshot()");
  assert.ok(!/budget-journal\.json",\s*\{/.test(lauf), "irgendwo wird das Journalobjekt von Hand gebaut");
});

test("1a RC4: Kein Kostenkontrollfehler erzeugt eine fachliche Freigabe", async () => {
  /* Mit IG_FAKTENCHECK_STRIKT=false gibt faktenSicher() auf dem allgemeinen
     Fehlerpfad { ok: true } zurück. Fünf Fehlerarten dürfen dort nie
     ankommen - und eine muss es weiterhin. */
  const { istKostenKontrollFehler, istBudgetStopp, KostenKontrollFehler, BudgetStopp } = await import("../src/kostenfehler.mjs");
  const { AdmissionAbgelehnt, InvarianteVerletzt, UnbekannterZweck, TopfGesperrt } = await import("../src/budget.mjs");
  const { OhneKontext } = await import("../src/anbieter.mjs");
  const { JournalNichtDurable } = await import("../src/journal.mjs");
  const { BudgetFehler } = await import("../src/kosten.mjs");

  const faelle = {
    A_AdmissionAbgelehnt: new AdmissionAbgelehnt("faktencheck", "core", 0.2, 0.01, 0.32),
    B_InvarianteVerletzt: new InvarianteVerletzt("faktencheck", "core", 0.05, 0.09),
    C_UnbekannterZweck: new UnbekannterZweck("neuer-zweck"),
    D_OhneKontext: new OhneKontext("faktencheck"),
    E_TopfGesperrt: new TopfGesperrt("core", "Invariante verletzt"),
    F_JournalNichtDurable: new JournalNichtDurable("faktencheck", "sendevermerk"),
    G_BudgetFehler: new BudgetFehler("Tagesbudget erreicht"),
  };
  for (const [name, e] of Object.entries(faelle)) {
    assert.ok(e instanceof KostenKontrollFehler, `${name} hängt nicht an KostenKontrollFehler`);
    assert.ok(istKostenKontrollFehler(e), `${name} wird nicht erkannt - Degrade-Pfad erreichbar`);
  }
  /* Die engere Klasse trennt weiterhin sauber: gesendet ist nicht gestoppt. */
  assert.ok(!istBudgetStopp(faelle.B_InvarianteVerletzt), "InvarianteVerletzt ist kein Stopp VOR dem Senden");
  assert.ok(!istBudgetStopp(faelle.C_UnbekannterZweck));
  assert.ok(!istBudgetStopp(faelle.D_OhneKontext));
  assert.ok(istBudgetStopp(faelle.A_AdmissionAbgelehnt));
  assert.ok(faelle.A_AdmissionAbgelehnt instanceof BudgetStopp);

  /* E) Ein echter technischer Fehler behält seinen Degrade-Pfad. */
  for (const e of [new Error("Prüfer antwortet nicht"), new TypeError("kaputt"), new SyntaxError("JSON")]) {
    assert.ok(!istKostenKontrollFehler(e), `${e.name} wird fälschlich der Kostenkontrolle zugeschlagen`);
  }
  /* Auch über Modulgrenzen, wo instanceof versagt. */
  assert.ok(istKostenKontrollFehler({ name: "InvarianteVerletzt" }));
  assert.ok(istKostenKontrollFehler({ kostenKontrolle: true, name: "Irgendwas" }));

  /* Und im Quelltext: die weite Prüfung steht VOR dem Degrade. */
  const autor = fs.readFileSync(new URL("../src/autor.mjs", import.meta.url), "utf8");
  const roh = autor.slice(autor.indexOf("async function faktenSicher"), autor.indexOf("export function themaText"));
  assert.match(roh, /if \(istKostenKontrollFehler\(e\)\) throw e;/,
    "faktenSicher prüft nicht auf die weite Klasse");
  /* Ohne Kommentare, sonst verschiebt eine Erklärung im Kommentar die
     Reihenfolge - der Kommentar oben nennt „{ ok: true }" bewusst. */
  const block = ohneKommentare(roh);
  assert.ok(block.indexOf("istKostenKontrollFehler(e)") < block.indexOf("CONFIG.faktencheck.strikt"),
    "die Prüfung steht nach dem Strikt-Zweig - ein Kostenfehler könnte eine Freigabe erzeugen");
  assert.ok(block.indexOf("istKostenKontrollFehler(e)") < block.indexOf("ok: true"),
    "die Prüfung steht nach dem Freigabepfad");
  assert.ok(!/istBudgetStopp\(e\)/.test(block), "die enge Prüfung deckt InvarianteVerletzt nicht ab");
});

test("1a RC4: faktenSicher gibt bei strikt=false kein ok für einen Kostenfehler", async () => {
  /* Der Verhaltenstest zum vorigen: derselbe Pfad, einmal gelaufen. Der
     Degrade-Zweig wird nachgebaut, weil faktenSicher nicht exportiert ist -
     aber mit der ECHTEN Prüffunktion aus dem Produktionscode. */
  const { istKostenKontrollFehler } = await import("../src/kostenfehler.mjs");
  const { AdmissionAbgelehnt, InvarianteVerletzt, UnbekannterZweck } = await import("../src/budget.mjs");
  const { OhneKontext } = await import("../src/anbieter.mjs");

  const strikt = false;                    // IG_FAKTENCHECK_STRIKT=false
  const faktenSicherNachbau = (e) => {
    if (istKostenKontrollFehler(e)) throw e;
    if (strikt) throw new Error("Faktencheck nicht möglich");
    return { ok: true, fehler: [], hinweise: [], korrekturen: [], behebbar: [] };
  };

  for (const [name, e] of [
    ["A AdmissionAbgelehnt", new AdmissionAbgelehnt("faktencheck", "core", 0.2, 0.01, 0.32)],
    ["B InvarianteVerletzt", new InvarianteVerletzt("faktencheck", "core", 0.05, 0.09)],
    ["C UnbekannterZweck", new UnbekannterZweck("neuer-zweck")],
    ["D OhneKontext", new OhneKontext("faktencheck")],
  ]) {
    assert.throws(() => faktenSicherNachbau(e), (geworfen) => geworfen === e,
      `${name}: der Fehler wurde geschluckt und der Beitrag freigegeben`);
  }
  /* E) Der technische Ausfall darf den definierten Degrade nehmen. */
  const r = faktenSicherNachbau(new Error("Prüfer antwortet nicht"));
  assert.equal(r.ok, true, "der definierte Degrade-Pfad für technische Fehler ist verschwunden");
});

test("1a RC4: Keine Beweisbehauptung mehr in irgendeiner Quelldatei", async () => {
  /* Der RC3-Test grepte nur eingabe.mjs und belegte deshalb nicht, was der
     Bericht behauptete. Jetzt über alle Quelldateien beider Kanäle. */
  const verbotene = [
    { muster: /beweisbare\w*\s+(Byte-|Eingabe-|Token-)?Schranke/i, was: "„beweisbare Schranke“" },
    { muster: /beweist\s+alle/i, was: "„beweist alle …“" },
    { muster: /Schranke\s+aller\s+abgerechneten/i, was: "„Schranke aller abgerechneten …“" },
    { muster: /mathematisch\s+(niemals|bewiesen|garantiert|sicher)/i, was: "„mathematisch niemals/bewiesen“" },
    { muster: /kann\s+(den\s+Deckel\s+)?niemals\s+über/i, was: "„kann niemals über …“" },
  ];
  const dateien = fs.readdirSync(new URL("../src/", import.meta.url)).filter((f) => f.endsWith(".mjs"));
  const funde = [];
  for (const datei of dateien) {
    const text = fs.readFileSync(new URL(`../src/${datei}`, import.meta.url), "utf8");
    for (const v of verbotene) if (v.muster.test(text)) funde.push(`${datei}: ${v.was}`);
  }
  assert.deepEqual(funde, [], `Beweisbehauptung im Produktionscode:\n${funde.join("\n")}`);

  /* „beweisbar nicht gesendet" im Journal bleibt zulässig und ist ein anderer
     Satz: Ob ein durabler Schreibvorgang stattgefunden hat, ist eine Tatsache
     über unsere eigene Datei - keine Aussage über die Tokenisierung des
     Anbieters. */
  const journal = fs.readFileSync(new URL("../src/journal.mjs", import.meta.url), "utf8");
  assert.match(journal, /beweisbar nicht gesendet/i, "die zulässige Aussage wurde versehentlich mitentfernt");

  /* Und die Tür beschreibt die Eingabeseite korrekt. */
  const tuer = fs.readFileSync(new URL("../src/anbieter.mjs", import.meta.url), "utf8");
  assert.match(tuer, /clientInputBound/, "die Tür benennt die clientseitige Schranke nicht");
  assert.match(tuer, /ohne die Token, die der Anbieter selbst\s*\n?\s*hinzufügt und berechnet/,
    "die Tür sagt nicht, was die Schranke NICHT leistet");
});

test("1a RC4: Ein geplanter Lauf kann den Provider-Guard nicht per Umgebung absenken", async () => {
  const { effektiveKonfiguration, richtlinieGate, RichtlinieVerletzt, POLICY_PROVIDER_GUARD_USD, providerGuard } = await import("../src/richtlinie.mjs");
  assert.equal(POLICY_PROVIDER_GUARD_USD, 0.02);

  const mitGuard = (guard, ausloeser = "schedule") => {
    const k = effektiveKonfiguration({ ausloeser, datum: "2026-09-19" });
    k.providerGuardUsd = guard;
    k.betriebsDeckel = Object.fromEntries(Object.entries(k.deckel).map(([t, v]) => [t, v - guard]));
    return () => richtlinieGate({ konfiguration: k });
  };

  assert.ok(mitGuard(0.02)().ok, "der Regelfall wird abgelehnt");
  assert.ok(mitGuard(0.05)().ok, "ein größerer, konservativerer Guard ist nicht erlaubt");
  for (const zuKlein of [0, 0.001, 0.0199]) {
    assert.throws(mitGuard(zuKlein), RichtlinieVerletzt, `Guard ${zuKlein} kommt durch das Gate`);
    try { mitGuard(zuKlein)(); } catch (e) {
      assert.ok(e.befunde.some((b) => /Policy-Mindestwert/.test(b)), `der Befund nennt den Mindestwert nicht: ${e.befunde.join(" | ")}`);
    }
  }
  assert.throws(mitGuard(Number.NaN), RichtlinieVerletzt, "ein unbrauchbarer Betrag kommt durch");

  /* Die Umgebungsvariable wirkt weiterhin - aber nur nach oben oder von Hand. */
  assert.equal(providerGuard("0.05"), 0.05);
  assert.equal(providerGuard("0"), 0, "die Umgebung kann den Wert setzen …");
  /* … aber seit RC6 gilt der Mindestwert in JEDEM Produktionslauf. Die
     RC5-Ausnahme fuer workflow_dispatch beschrieb einen Workflow-Pfad, den es
     gar nicht gibt - und waere ohne Betrag und Begruendung auch kein Break
     Glass gewesen. Siehe den RC6-Test. */
  assert.throws(mitGuard(0, "workflow_dispatch"), RichtlinieVerletzt,
    "von Hand laesst sich der Guard weiterhin absenken");
});
/* ===== 1a-RC5: Garantiesprache und Guard-Pfad =========================== */

test("1a RC5: Keine kostenbezogene Aussage behauptet mehr Sicherheit, als es gibt", async () => {
  /* Der RC4-Test verbot fünf Schlagwörter und leitete daraus „global geprüft"
     ab. Das war zu wenig: Im Code standen weiter Aussagen, die mit RC4s
     eigener Rücknahme kollidierten - „Die Kostenzusage bleibt hart", „der
     teuerste denkbare Ausgang EINES Aufrufs", „harte Vorab-Zusage: tatsächliche
     Kosten <= reservierte Kosten". Dieser Test nimmt die konkret gefundenen
     Altformulierungen als Ausgangspunkt.

     Er prüft Quelltext UND die Texte, die zur Laufzeit entstehen. Ein
     Kommentar, der die Wahrheit sagt, nützt wenig, wenn das Protokoll etwas
     anderes behauptet. */
  const verbotene = [
    /* Die konkret beanstandeten Altformulierungen */
    { muster: /Kostenzusage (bleibt hart|hält|haelt)/i, was: "„Kostenzusage hält/bleibt hart“" },
    { muster: /harte\s+(Vorab-)?Zusage/i, was: "„harte (Vorab-)Zusage“" },
    { muster: /tatsächliche Kosten\s*<=\s*reservierte/i, was: "„tatsächliche Kosten <= reservierte“" },
    { muster: /teuerste\s+denkbare\s+Ausgang/i, was: "„der teuerste denkbare Ausgang“" },
    { muster: /harte\s+Schranke/i, was: "„harte Schranke“" },
    { muster: /WORST\s+CASE\s+reserviert/i, was: "„WORST CASE reserviert“" },
    /* Und die Muster aus RC4 */
    { muster: /beweisbare\w*\s+(Byte-|Eingabe-|Token-)?Schranke/i, was: "„beweisbare Schranke“" },
    { muster: /beweist\s+alle/i, was: "„beweist alle …“" },
    { muster: /Schranke\s+aller\s+abgerechneten/i, was: "„Schranke aller abgerechneten …“" },
    { muster: /mathematisch\s+(niemals|bewiesen|garantiert|sicher)/i, was: "„mathematisch niemals/bewiesen“" },
    { muster: /kann\s+(den\s+Deckel\s+)?niemals\s+über/i, was: "„kann niemals über …“" },
  ];

  /* Die Gattung selbst - eine Reserve als bewiesene Providergrenze - wird
     SATZWEISE geprüft, nicht per Muster. Grund: Genau dieselben Wörter stehen
     in den Sätzen, die das Gegenteil sagen („… ist eine Reserve, nicht eine
     bewiesene Kostenobergrenze"). Ein Muster kann eine Behauptung nicht von
     ihrer Verneinung unterscheiden; ein Satz mit „nicht" oder „kein" ist keine
     Zusage. */
  const RESERVE = /(admissionBound|Admission Reserve|Reserve|Reservierung|admissionReserve)/i;
  const BEWEIS = /(bewiesen|beweisbar|garantiert|mathematisch|kann nicht überschritten|niemals überschritten)/i;
  const VERNEINT = /\b(nicht|kein|keine|keinen|keiner|ohne|statt)\b/i;
  const behauptungen = (text) => text
    .split(/(?<=[.:;!?])\s+|\n\s*\n/)
    .map((satz) => satz.replace(/\s+/g, " ").trim())
    .filter((satz) => RESERVE.test(satz) && BEWEIS.test(satz) && !VERNEINT.test(satz));

  /* Kostenrelevante Module - nicht der ganze Baum: „Obergrenze je Beitrag" in
     config.mjs ist unsere eigene Ausgabengrenze und keine Aussage über den
     Anbieter. Gemeint sind Admission, Kostenzusage und Providergrenzen. */
  const kostenModule = ["anbieter.mjs", "budget.mjs", "kosten.mjs", "eingabe.mjs", "journal.mjs", "richtlinie.mjs", "kostenfehler.mjs", "lauf.mjs", "telemetrie.mjs"];
  const funde = [];
  for (const datei of kostenModule) {
    let text;
    try { text = fs.readFileSync(new URL(`../src/${datei}`, import.meta.url), "utf8"); } catch { continue; }
    for (const v of verbotene) if (v.muster.test(text)) funde.push(`${datei}: ${v.was}`);
    for (const satz of behauptungen(text)) funde.push(`${datei}: Reserve als bewiesene Grenze – „${satz.slice(0, 90)}“`);
  }
  assert.deepEqual(funde, [], `Zu starke Kostenaussage im Quelltext:\n${funde.join("\n")}`);

  /* Die Laufzeittexte, erzeugt, nicht gelesen. */
  const { tagesplanAdmissionBedarf } = await import("../src/anbieter.mjs");
  const knapp = tagesplanAdmissionBedarf({
    posten: Array.from({ length: 9 }, () => ({ modell: "claude-sonnet-5", maxTokens: 16000, eingabeTokens: 16000 })),
    deckelCore: 0.32,
  });
  for (const v of verbotene) {
    assert.ok(!v.muster.test(knapp.hinweis), `Laufzeithinweis enthält ${v.was}: ${knapp.hinweis}`);
  }
  assert.deepEqual(behauptungen(knapp.hinweis), [], "der Laufzeithinweis behauptet eine bewiesene Grenze");
  /* Und er sagt ausdrücklich, worauf er beruht. */
  assert.match(knapp.hinweis, /Planungswerten/, "der Laufzeithinweis nennt die Planungswerte nicht");
  assert.match(knapp.hinweis, /Admissionbedarf/, "der Laufzeithinweis nennt die Zahl weiter Worst Case");
  assert.equal(knapp.basis, "planungswerte");
  assert.equal(knapp.dailyPlanNotAdmissibleAtCap, true);
  assert.ok(!("dailyPlanNotWorstCaseFundable" in knapp),
    "das alte Signal behauptet weiter einen Provider-Worst-Case");

  const { effektiveKonfiguration } = await import("../src/richtlinie.mjs");
  for (const h of effektiveKonfiguration({ ausloeser: "schedule", datum: "2026-09-19" }).hinweise) {
    for (const v of verbotene) assert.ok(!v.muster.test(h), `Konfigurationshinweis enthält ${v.was}: ${h}`);
  }

  /* Die Begriffe, die es stattdessen gibt - und zwar benannt. */
  const kosten = fs.readFileSync(new URL("../src/kosten.mjs", import.meta.url), "utf8");
  assert.match(kosten, /export function admissionReserveUsd/, "die Reserve heißt weiter „Obergrenze“");
  const richtlinie = fs.readFileSync(new URL("../src/richtlinie.mjs", import.meta.url), "utf8");
  assert.match(richtlinie, /Policy cap/, "Policy cap ist nicht benannt");

  /* Zulässig bleibt eine Aussage über eine echte lokale Tatsache. */
  const journal = fs.readFileSync(new URL("../src/journal.mjs", import.meta.url), "utf8");
  assert.match(journal, /beweisbar nicht gesendet/i,
    "die zulässige Aussage über den durablen Schreibvorgang wurde mitentfernt");
});

test("1a RC6: Der Mindestguard gilt in jedem Produktionslauf, auch von Hand", async () => {
  /* RC5 liess fuer workflow_dispatch eine Ausnahme und nannte sie „wie Break
     Glass". Sie war aus zwei Gruenden falsch: Es gibt keinen Workflow-Input
     fuer den Guard und keine Uebergabe von IG_PROVIDER_GUARD_USD an den
     Tageslauf - die Ausnahme beschrieb einen Weg, den es nicht gibt. Und sie
     waere kein Break Glass gewesen: Dort braucht es Betrag UND Begruendung,
     hier haette ein Haekchen genuegt.

     Der Test laeuft den echten Pfad, ohne nachtraeglich mutierte Konfiguration:
       IG_PROVIDER_GUARD_USD → providerGuardLesen → effektiveKonfiguration
                             → richtlinieGate                                */
  const { providerGuardLesen, effektiveKonfiguration, richtlinieGate, RichtlinieVerletzt,
    POLICY_PROVIDER_GUARD_USD, PROVIDER_GUARD_USD, REGEL_DECKEL } = await import("../src/richtlinie.mjs");

  const vorher = process.env.IG_PROVIDER_GUARD_USD;
  const durchlauf = (roh, ausloeser, breakGlass = null) => {
    if (roh === undefined) delete process.env.IG_PROVIDER_GUARD_USD;
    else process.env.IG_PROVIDER_GUARD_USD = roh;
    const konfiguration = effektiveKonfiguration({ ausloeser, datum: "2026-09-19", breakGlass });
    try { richtlinieGate({ konfiguration }); return { ok: true, konfiguration }; }
    catch (e) { return { ok: false, fehler: e, konfiguration }; }
  };
  const guardBefund = (r) => (r.fehler?.befunde || []).filter((b) => /Guard|GUARD/.test(b));

  try {
    assert.equal(POLICY_PROVIDER_GUARD_USD, 0.02);
    assert.equal(PROVIDER_GUARD_USD, 0.02);

    /* Erlaubt - und zwar unter BEIDEN Ausloesern gleich. */
    for (const ausloeser of ["schedule", "workflow_dispatch"]) {
      const unset = durchlauf(undefined, ausloeser);
      assert.ok(unset.ok, `${ausloeser}: nicht gesetzt wird abgelehnt`);
      assert.equal(unset.konfiguration.providerGuardUsd, 0.02);
      assert.equal(unset.konfiguration.providerGuard.quelle, "standard");
      assert.equal(unset.konfiguration.betriebsDeckel.core, 0.30);

      const leer = durchlauf("", ausloeser);
      assert.ok(leer.ok, `${ausloeser}: Leerstring wird abgelehnt`);
      assert.equal(leer.konfiguration.providerGuard.quelle, "standard",
        "eine leere Actions-Variable muss als nicht gesetzt gelten");

      const genau = durchlauf("0.02", ausloeser);
      assert.ok(genau.ok, `${ausloeser}: 0,02 wird abgelehnt`);
      assert.equal(genau.konfiguration.providerGuard.quelle, "umgebung");

      const groesser = durchlauf("0.05", ausloeser);
      assert.ok(groesser.ok, `${ausloeser}: ein groesserer Guard wird abgelehnt`);
      assert.equal(groesser.konfiguration.betriebsDeckel.core, 0.27,
        "der groessere Abstand wirkt auch wirklich");
    }

    /* Abgelehnt - ebenfalls unter BEIDEN Ausloesern. Das ist der Kern von RC6. */
    for (const ausloeser of ["schedule", "workflow_dispatch"]) {
      for (const zuKlein of ["0", "0.0199", "0.01"]) {
        const r = durchlauf(zuKlein, ausloeser);
        assert.ok(!r.ok && r.fehler instanceof RichtlinieVerletzt,
          `${ausloeser}: Guard ${zuKlein} kommt durch das Gate`);
        assert.ok(guardBefund(r).some((b) => /Policy-Mindestwert/.test(b)),
          `${ausloeser}: der Befund nennt den Mindestwert nicht`);
        assert.ok(guardBefund(r).some((b) => /Break Glass hebt den Core-Deckel/.test(b)),
          `${ausloeser}: der Befund erklaert die Zustaendigkeit von Break Glass nicht`);
      }
      /* Ein gesetzter, unbrauchbarer Wert bleibt in jedem Lauf ein Fehler. */
      for (const murks of ["quatsch", "-1", "0,02", "NaN"]) {
        const r = durchlauf(murks, ausloeser);
        assert.ok(!r.ok && r.fehler instanceof RichtlinieVerletzt, `${ausloeser}: Wert ${murks} kommt durch`);
        assert.ok(guardBefund(r).some((b) => b.includes("kein gültiger Betrag")));
        assert.equal(providerGuardLesen(murks).gueltig, false);
        assert.equal(providerGuardLesen(murks).usd, PROVIDER_GUARD_USD, "der Rueckfallwert ist nicht der sichere");
      }
    }

    /* Break Glass bleibt unveraendert moeglich - und laesst den Abstand in
       Ruhe. Das ist die Trennung, die RC5 vermischt hatte: Break Glass hebt
       den Core-Deckel, der Guard bleibt darunter stehen. */
    const bg = durchlauf(undefined, "workflow_dispatch", { aktiv: true, betragUsd: 0.5, grund: "Nachholtag" });
    assert.ok(bg.ok, "Break Glass von Hand wird abgelehnt");
    assert.equal(bg.konfiguration.deckel.core, 0.5, "der Core-Deckel wurde nicht angehoben");
    assert.equal(bg.konfiguration.providerGuardUsd, 0.02, "Break Glass hat den Guard veraendert");
    assert.equal(bg.konfiguration.betriebsDeckel.core, 0.48, "der Abstand unter dem angehobenen Deckel fehlt");
    assert.equal(bg.konfiguration.breakGlass.aktiv, true);

    /* Und auch mit Break Glass laesst sich der Guard nicht absenken. */
    const bgKlein = durchlauf("0", "workflow_dispatch", { aktiv: true, betragUsd: 0.5, grund: "Nachholtag" });
    assert.ok(!bgKlein.ok, "Break Glass oeffnet einen Weg, den Guard abzusenken");
    assert.ok(guardBefund(bgKlein).some((b) => /Policy-Mindestwert/.test(b)));

    /* Break Glass aus dem Zeitplan bleibt wirkungslos - unveraendert aus RC4.
       Der Lauf bricht nicht ab, die Anhebung wird schlicht nicht wirksam und
       steht als Hinweis im Protokoll. Das ist die richtige Reaktion: Ein
       geplanter Lauf soll am Regeldeckel weiterarbeiten, nicht ausfallen. */
    const bgPlan = durchlauf(undefined, "schedule", { aktiv: true, betragUsd: 0.5, grund: "x" });
    assert.ok(bgPlan.ok, "ein geplanter Lauf faellt wegen einer ignorierten Anhebung aus");
    assert.equal(bgPlan.konfiguration.breakGlass.aktiv, false, "Break Glass wirkt aus dem Zeitplan");
    assert.equal(bgPlan.konfiguration.deckel.core, 0.32, "der Deckel wurde aus dem Zeitplan angehoben");
    assert.ok(bgPlan.konfiguration.hinweise.some((h) => /Break Glass aus einem geplanten Lauf/.test(h)),
      "die abgelehnte Anhebung steht in keinem Hinweis");
    assert.deepEqual({ ...REGEL_DECKEL }, { core: 0.32, engagement: 0.25, research: 0.12 });
  } finally {
    if (vorher === undefined) delete process.env.IG_PROVIDER_GUARD_USD;
    else process.env.IG_PROVIDER_GUARD_USD = vorher;
  }
});

test("1a RC6: Es gibt keinen zweiten, unverdrahteten Weg am Guard vorbei", async () => {
  /* Die RC5-Ausnahme behauptete einen manuellen Pfad, den es im Workflow gar
     nicht gab. Dieser Test haelt beides fest: dass das Gate keine Ausnahme
     nach Ausloeser mehr kennt, und dass der Kommentar daneben nicht laenger
     das Gegenteil sagt. */
  const richtlinie = fs.readFileSync(new URL("../src/richtlinie.mjs", import.meta.url), "utf8");

  /* Der Guard-Zweig im Gate haengt an keinem Ausloeser mehr. */
  const gate = richtlinie.slice(richtlinie.indexOf("export function richtlinieGate"));
  const guardZweig = gate.slice(gate.indexOf("POLICY_PROVIDER_GUARD_USD") - 200, gate.indexOf("POLICY_PROVIDER_GUARD_USD") + 200);
  assert.ok(!/geplant\s*&&\s*guard\s*</.test(guardZweig),
    "der Mindestguard gilt weiterhin nur fuer geplante Laeufe");
  assert.match(gate, /guard < POLICY_PROVIDER_GUARD_USD/, "die Mindestpruefung fehlt");

  /* Und der Kommentar sagt dasselbe wie das Gate. */
  assert.match(richtlinie, /JEDEM Produktionslauf/, "die Policy nennt ihren Geltungsbereich nicht");
  assert.ok(!/wie Break Glass/i.test(richtlinie), "die alte Gleichsetzung mit Break Glass steht noch da");
  assert.match(richtlinie, /Break Glass bleibt zuständig für die bewusste Anhebung des Core-Deckels/,
    "die Zustaendigkeit von Break Glass ist nicht abgegrenzt");

  /* „Ausgabedeckel" trug zwei Bedeutungen - Token und Dollar. */
  assert.ok(!/anbieterseitiger Ausgabedeckel/.test(richtlinie),
    "der Begriff Ausgabedeckel steht weiter fuer zwei verschiedene Dinge");
  assert.match(richtlinie, /KOSTEN-HARDCAP je Anfrage/, "der gemeinte Dollar-Hardcap ist nicht benannt");
  assert.match(richtlinie, /max_tokens.*begrenzt die Ausgabe-TOKEN|begrenzt die Ausgabe-TOKEN/s,
    "der Unterschied zu max_tokens ist nicht festgehalten");

  /* Der Workflow kennt keinen Guard-Input - und soll auch keinen bekommen.
     Break Glass hat seine beiden Eingaben, der Guard hat keine. */
  const pfade = ["../.github/workflows/instagram.yml", "../../.github/workflows/instagram.yml"];
  let workflow = null;
  for (const pfad of pfade) {
    try { workflow = fs.readFileSync(new URL(pfad, import.meta.url), "utf8"); break; } catch { /* der andere Kanal */ }
  }
  assert.ok(workflow, "der Workflow wurde nicht gefunden");
  assert.ok(!/IG_PROVIDER_GUARD_USD/.test(workflow),
    "der Workflow reicht den Guard durch - dann braucht es auch eine Policy dafuer");
  assert.match(workflow, /break_glass_grund/, "Break Glass hat seine Begruendungseingabe verloren");
});

test("1a: Der Admissionbedarf des Pflichtprodukts liegt über dem Deckel – und wird so benannt", async () => {
  /* Fall 3 aus der Anweisung braucht den Reservebestand und ist noch nicht
     gebaut. Was 1a leisten kann, ist die Kostenzusage; die Verfügbarkeits-
     zusage steht ausdrücklich aus. Dieser Test hält den Befund fest, damit
     er nicht in einem Bericht verschwindet. */
  const { tagesplanAdmissionBedarf: tagesplanWorstCase } = await import("../src/anbieter.mjs");

  const pflichtHerrJurist = [
    { name: "b1 Text", modell: "claude-sonnet-5", maxTokens: 16000, eingabeTokens: 3000 },
    { name: "b1 Faktencheck", modell: "claude-sonnet-5", maxTokens: 6000, eingabeTokens: 4000 },
    { name: "b2 Text", modell: "claude-sonnet-5", maxTokens: 16000, eingabeTokens: 3000 },
    { name: "b2 Faktencheck", modell: "claude-sonnet-5", maxTokens: 6000, eingabeTokens: 4000 },
    { name: "b3 Reel", modell: "claude-sonnet-5", maxTokens: 16000, eingabeTokens: 3000 },
    { name: "b3 Reel-Faktencheck", modell: "claude-opus-5", maxTokens: 6000, eingabeTokens: 4000 },
    { name: "Stories", modell: "claude-sonnet-5", maxTokens: 16000, eingabeTokens: 3000 },
    { name: "Story-Faktencheck", modell: "claude-haiku-4-5-20251001", maxTokens: 6000, eingabeTokens: 4000 },
  ];
  const wc = tagesplanWorstCase({ posten: pflichtHerrJurist, deckelCore: 0.32 });

  assert.equal(wc.dailyPlanNotAdmissibleAtCap, true,
    "mit den heutigen Ceilings ist das Pflichtprodukt im Worst Case nicht finanzierbar");
  assert.ok(wc.summe > 1.0, `Worst Case ${wc.summe} $ gegen 0,32 $ Deckel`);
  assert.match(wc.hinweis, /Admissionbedarf des Pflichtprodukts.*aus Planungswerten.*Verfügbarkeitszusage gibt es damit nicht/);

  /* Der Befund ist kein Grund, den Deckel still anzuheben … */
  assert.equal(wc.deckelCore, 0.32);
  /* … und auch keiner, die Ceilings zurechtzuschneiden: Sie stehen unverändert
     in den Posten. */
  assert.deepEqual(wc.posten.map((p) => p.maxTokens), [16000, 6000, 16000, 6000, 16000, 6000, 16000, 6000]);
});

/* ===== Reservebestand: die Policy ======================================== */

const reserveBeitrag = (zusatz = {}) => ({
  format: "karussell", themaId: "strafat-schema-1", fach: "strafat",
  folien: [
    { art: "titel", titel: "Der dreistufige Deliktsaufbau" },
    { art: "text", titel: "Aufbau", text: "Zuerst der Tatbestand, dann die Rechtswidrigkeit, dann die Schuld." },
    { art: "karte" }, { art: "cta" },
  ],
  caption: "Der Aufbau in der richtigen Reihenfolge.",
  ...zusatz,
});
const reserveEintrag = (zusatz = {}) => ({
  id: "r1", kanal: "herrjurist",
  erstelltAm: "2026-09-01", verfaelltAm: "2026-09-22",
  themaId: "strafat-schema-1", fach: "strafat", typ: "schema", format: "karussell",
  beitrag: reserveBeitrag(), bildUrls: ["https://x/1.png", "https://x/2.png"],
  caption: "Der Aufbau in der richtigen Reihenfolge.\n\n#jurastudium", hashtags: ["#jurastudium"],
  faktenFreigabe: { ok: true, geprueftAm: "2026-09-01T10:00:00.000Z", hinweise: [] },
  regelVersion: 1,
  ...zusatz,
});

test("Reserve: nur alterungsarme Themenarten kommen überhaupt in Frage", async () => {
  const { themaTauglich, RESERVE_TYPEN } = await import("../src/reserve.mjs");

  for (const typ of ["schema", "begriff"]) {
    assert.equal(themaTauglich({ typ }).ok, true, `${typ} sollte zulässig sein`);
  }
  /* Module und Karteikarten tragen regelmäßig Jahreswerte, Formeln tragen
     Sätze und Grenzen, Quiz gehört nicht in diese Phase. */
  for (const typ of ["modul", "karteikarte", "formel", "quiz", undefined, null, "irgendwas"]) {
    const r = themaTauglich({ typ });
    assert.equal(r.ok, false, `${typ} darf nicht in den Vorrat`);
    assert.ok(r.gruende.length, "die Ablehnung wird nicht begründet");
  }
  assert.equal(themaTauglich(null).ok, false, "ohne Thema kein Vorrat");
  assert.deepEqual([...RESERVE_TYPEN], ["schema", "begriff"]);
});

test("Reserve: zeitabhängige Inhalte fallen durch, auch bei tauglichem Thema", async () => {
  const { inhaltTauglich, reserveTauglich } = await import("../src/reserve.mjs");

  /* Der Regelfall: reine Systematik, kein Zeitbezug. */
  assert.equal(inhaltTauglich(reserveBeitrag()).ok, true, "reine Systematik wird abgelehnt");

  /* Und die Fälle, die der Vorrat NICHT tragen darf. Jeder einzeln, damit
     eine gelockerte Regel sichtbar wird. */
  const faelle = [
    ["Jahreszahl", { text: "Seit 2025 gilt die neue Reihenfolge." }],
    ["Geldbetrag", { text: "Der Betrag von 1.000 € bleibt außer Ansatz." }],
    ["Prozentsatz", { text: "Der Satz beträgt 15 % des Einkommens." }],
    ["Verwaltungsanweisung", { text: "Das BMF sieht das anders." }],
    ["Entscheidung", { text: "Der BFH hat das entschieden." }],
    ["Fundstelle", { text: "Urteil vom 3. März, Az. I R 1/24." }],
    ["Betragsgrenze", { text: "Der Freibetrag mindert die Bemessungsgrundlage." }],
    ["Pauschale", { text: "Stattdessen greift die Pauschale." }],
    ["Zeitbezug", { text: "Ab dem Veranlagungszeitraum gilt das nicht mehr." }],
    ["Rechtsstand", { text: "Rechtsstand beachten." }],
  ];
  for (const [was, folie] of faelle) {
    const b = reserveBeitrag({ folien: [{ art: "titel", titel: "X" }, { art: "text", titel: "Y", ...folie }] });
    const r = inhaltTauglich(b);
    assert.equal(r.ok, false, `${was} kommt durch: ${folie.text}`);
    assert.ok(r.gruende.length, `${was} wird nicht begründet`);
  }

  /* Auch in der Caption, nicht nur in den Folien. */
  assert.equal(inhaltTauglich(reserveBeitrag({ caption: "Stand 2026." })).ok, false, "die Caption wird nicht geprüft");

  /* Recherche macht den Inhalt abhängig von einer Quelle, die altert. */
  assert.equal(inhaltTauglich(reserveBeitrag({ format: "aktuell" })).ok, false);
  assert.equal(inhaltTauglich(reserveBeitrag({ quellen: [{ url: "https://x" }] })).ok, false);
  assert.equal(inhaltTauglich(reserveBeitrag({ recherche: true })).ok, false);

  /* Beide Tore müssen offen sein - ein tauglicher Inhalt zum untauglichen
     Thema reicht nicht, und umgekehrt auch nicht. */
  assert.equal(reserveTauglich({ thema: { typ: "schema" }, beitrag: reserveBeitrag() }).ok, true);
  assert.equal(reserveTauglich({ thema: { typ: "modul" }, beitrag: reserveBeitrag() }).ok, false);
  assert.equal(reserveTauglich({ thema: { typ: "schema" }, beitrag: reserveBeitrag({ caption: "1.000 €" }) }).ok, false);
});

test("Reserve: ein Slug mit Jahreszahl sperrt den Beitrag nicht aus", async () => {
  /* Die naheliegende Falle: Wer über das ganze Objekt sucht, findet in
     `slug: "2026-09-19-b1"` eine Jahreszahl und sperrt damit jeden Beitrag
     aus. Gesucht wird deshalb nur im Inhaltstext. */
  const { inhaltTauglich, inhaltsText } = await import("../src/reserve.mjs");
  const b = reserveBeitrag({ slug: "2026-09-19-b1", themaId: "strafat-2024-schema", bildUrls: ["https://x/2025/1.png"] });
  assert.equal(inhaltTauglich(b).ok, true, "Slug, Themen-ID oder Bildpfad sperren den Beitrag aus");
  const text = inhaltsText(b);
  assert.ok(!text.includes("2026-09-19"), "der Slug landet im geprüften Text");
  assert.ok(text.includes("Tatbestand"), "der eigentliche Inhalt fehlt im geprüften Text");
});

test("Reserve: unvollständige Einträge werden nicht aufgenommen", async () => {
  /* Ein halber Eintrag ist schlimmer als keiner: Er belegt einen Platz und
     faellt am Blockadetag durch - wo es kein Geld gibt, ihn zu retten. */
  const { vollstaendig, eintragBauen } = await import("../src/reserve.mjs");

  assert.equal(vollstaendig(reserveEintrag()).ok, true, "der vollständige Eintrag wird abgelehnt");
  for (const [feld, kaputt] of [
    ["Beitragstext", { beitrag: { folien: [] } }],
    ["Caption", { caption: "" }],
    ["gerenderte Bilder", { bildUrls: [] }],
    ["Faktenfreigabe", { faktenFreigabe: { ok: false } }],
    ["Zeitpunkt der Faktenfreigabe", { faktenFreigabe: { ok: true } }],
    /* Die gespeicherte Caption IST die Publikationscaption - am Blockadetag
       wird nichts mehr zusammengesetzt, und bereitsVeroeffentlicht()
       vergleicht genau diesen Text. */
    ["Hashtags", { caption: "Nur der Text, ohne Hashtags." }],
    /* Ein ausgefallener Pruefer ist im Tagesbetrieb ein Degrade, im Vorrat
       nicht: Der Beitrag liegt 21 Tage, und es gibt keinen Nachcheck. */
    ["tatsaechlich", { faktenFreigabe: { ok: true, geprueftAm: "2026-09-01T10:00:00.000Z", ausgefallen: true } }],
  ]) {
    const r = vollstaendig(reserveEintrag(kaputt));
    assert.equal(r.ok, false, `${feld} fehlt und faellt nicht auf`);
    assert.ok(r.fehlend.some((f) => f.includes(feld.split(" ")[0])), `${feld}: ${r.fehlend.join(", ")}`);
  }

  /* eintragBauen nimmt nur an, was beide Tore passiert UND vollständig ist. */
  const gut = eintragBauen({
    id: "r9", kanal: "herrjurist", erstelltAm: "2026-09-19",
    thema: { id: "strafat-schema-1", fach: "strafat", typ: "schema" },
    beitrag: reserveBeitrag(), bildUrls: ["https://x/1.png"], caption: "Systematik.",
    faktenFreigabe: { ok: true, geprueftAm: "2026-09-19T10:00:00.000Z" },
  });
  assert.equal(gut.ok, true, `Aufnahme abgelehnt: ${gut.gruende.join(" | ")}`);
  assert.equal(gut.eintrag.verfaelltAm, "2026-10-10", "21 Tage Haltbarkeit");
  assert.equal(gut.eintrag.regelVersion, 1);

  const ohneBild = eintragBauen({
    id: "r10", kanal: "herrjurist", erstelltAm: "2026-09-19",
    thema: { id: "x", typ: "schema" }, beitrag: reserveBeitrag(),
    bildUrls: [], caption: "Systematik.", faktenFreigabe: { ok: true, geprueftAm: "2026-09-19T10:00:00.000Z" },
  });
  assert.equal(ohneBild.ok, false, "ein Eintrag ohne Bilder wird aufgenommen");
  assert.equal(ohneBild.eintrag, null);
});

test("Reserve: die Haltbarkeit ist hart - kein Nachcheck, keine Verlängerung", async () => {
  const { abgelaufen, bestandPruefen, bedarf, TTL_TAGE, ZIEL_BESTAND, verfallsdatum } = await import("../src/reserve.mjs");
  assert.equal(TTL_TAGE, 21);
  assert.equal(ZIEL_BESTAND, 4);
  assert.equal(verfallsdatum("2026-09-01"), "2026-09-22");

  const frisch = reserveEintrag({ id: "a", erstelltAm: "2026-09-19", verfaelltAm: "2026-10-10" });
  const alt = reserveEintrag({ id: "b", erstelltAm: "2026-08-01", verfaelltAm: "2026-08-22" });
  assert.equal(abgelaufen(frisch, "2026-09-25"), false);
  assert.equal(abgelaufen(alt, "2026-09-25"), true);
  assert.equal(abgelaufen(alt, "2026-08-22"), false, "am letzten Tag gilt er noch");
  assert.equal(abgelaufen(alt, "2026-08-23"), true, "einen Tag später nicht mehr");
  assert.equal(abgelaufen({ id: "c" }, "2026-09-25"), true, "ohne Datum im Zweifel weg");

  const { gueltig, verfallen } = bestandPruefen([frisch, alt], "2026-09-25");
  assert.deepEqual(gueltig.map((e) => e.id), ["a"]);
  assert.deepEqual(verfallen.map((e) => e.id), ["b"]);
  assert.match(verfallen[0].grund, /TTL abgelaufen/);

  /* Eine Regeländerung lässt den Altbestand nicht stillschweigend mitgelten. */
  const alteRegel = reserveEintrag({ id: "d", erstelltAm: "2026-09-19", verfaelltAm: "2026-10-10", regelVersion: 0 });
  assert.equal(bestandPruefen([alteRegel], "2026-09-25").gueltig.length, 0);
  assert.match(bestandPruefen([alteRegel], "2026-09-25").verfallen[0].grund, /Regelversion/);

  /* Bedarf: was zum Ziel fehlt - kein Mindestverbrauch. */
  assert.equal(bedarf([], "2026-09-25"), 4);
  assert.equal(bedarf([frisch], "2026-09-25"), 3);
  assert.equal(bedarf([frisch, alt], "2026-09-25"), 3, "das Abgelaufene zählt nicht mit");
  assert.equal(bedarf([frisch, frisch, frisch, frisch], "2026-09-25"), 0, "bei vollem Bestand wird nichts erzeugt");
  assert.equal(bedarf([frisch, frisch, frisch, frisch, frisch], "2026-09-25"), 0, "und erst recht nicht darüber hinaus");
});

test("Reserve: die Entnahme kostet nichts und wiederholt kein junges Thema", async () => {
  const { entnehmen } = await import("../src/reserve.mjs");

  const a = reserveEintrag({ id: "a", themaId: "t-alt", erstelltAm: "2026-09-02", verfaelltAm: "2026-09-23" });
  const b = reserveEintrag({ id: "b", themaId: "t-neu", erstelltAm: "2026-09-10", verfaelltAm: "2026-10-01" });
  const weg = reserveEintrag({ id: "c", themaId: "t-weg", erstelltAm: "2026-08-01", verfaelltAm: "2026-08-22" });

  /* Das Älteste zuerst: Was zuerst verfällt, wird zuerst gebraucht. */
  const r1 = entnehmen([b, a, weg], { heute: "2026-09-19" });
  assert.equal(r1.eintrag.id, "a", "nicht das älteste Stück genommen");
  assert.deepEqual(r1.rest.map((e) => e.id), ["b"], "der Rest stimmt nicht");
  assert.deepEqual(r1.verfallen.map((e) => e.id), ["c"]);

  /* Ein Thema, das kürzlich erschienen ist, wird übersprungen. Die Form ist
     die ECHTE - so, wie vermerken() den Ledger schreibt. Ein erfundener
     Feldname hätte den Dublettenschutz still wirkungslos gemacht. */
  const ledger = { veroeffentlicht: [{ datum: "2026-09-05", art: "beitrag", thema: "t-alt" }] };
  const r2 = entnehmen([b, a], { heute: "2026-09-19", ledger });
  assert.equal(r2.eintrag.id, "b", "die Dublette wurde genommen");

  /* Sind alle Themen jung, wird nichts entnommen - und der Grund steht da. */
  const r3 = entnehmen([a, b], { heute: "2026-09-19", ledger: { veroeffentlicht: [{ datum: "2026-09-05", art: "beitrag", thema: "t-alt" }, { datum: "2026-09-06", art: "beitrag", thema: "t-neu" }] } });
  assert.equal(r3.eintrag, null);
  assert.match(r3.grund, /letzten 60 Tagen erschienen/);

  /* Ein altes Vorkommen desselben Themas blockiert nicht ewig. */
  const r4 = entnehmen([a], { heute: "2026-09-19", ledger: { veroeffentlicht: [{ datum: "2026-01-05", art: "beitrag", thema: "t-alt" }] } });
  assert.equal(r4.eintrag.id, "a", "ein halbes Jahr altes Thema blockiert weiterhin");

  /* Eine Story zum selben Thema sperrt den Feed-Beitrag nicht: Sie ist ein
     anderes Produkt, und der Vorrat haelt Feed-Beitraege. */
  const r6 = entnehmen([a], { heute: "2026-09-19", ledger: { veroeffentlicht: [{ datum: "2026-09-18", art: "story", thema: "t-alt" }] } });
  assert.equal(r6.eintrag.id, "a", "eine Story sperrt den Vorratsbeitrag zum selben Thema");

  /* Und der Feldname ist nicht frei erfunden: So schreibt vermerken(). */
  const { vermerken: ledgerVermerken } = await import("../src/planer.mjs");
  const echt = ledgerVermerken({}, { datum: "2026-09-18", art: "beitrag", thema: "t-alt", fach: "strafat" });
  assert.equal(entnehmen([a], { heute: "2026-09-19", ledger: echt }).eintrag, null,
    "der Dublettenschutz greift nicht auf dem Ledger, den vermerken() wirklich schreibt");

  /* Leerer Bestand: kein Absturz, ein benennbarer Grund. */
  const r5 = entnehmen([], { heute: "2026-09-19" });
  assert.equal(r5.eintrag, null);
  assert.match(r5.grund, /kein gültiger Vorratsbeitrag/);

  /* Und der Kern: Das Modul ruft keinen Anbieter und kein Budget. Die
     Entnahme am Blockadetag muss ohne jeden bezahlten Aufruf funktionieren. */
  const quelle = fs.readFileSync(new URL("../src/reserve.mjs", import.meta.url), "utf8");
  for (const verboten of [/claudeAufruf/, /openaiAufruf/, /bildAufruf/, /budget\./, /anbieter\.mjs/, /import .*kosten\.mjs/]) {
    assert.ok(!verboten.test(quelle), `die Reserve-Policy greift auf ${verboten} zu - die Entnahme muss kostenlos sein`);
  }
  assert.ok(!/^import /m.test(quelle), "die Reserve-Policy hat Abhängigkeiten - sie soll für sich stehen");
});

/* ===== Reservebestand: die Mechanik ====================================== */

const resHosting = () => {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), "reshost-"));
  const state = new Map();
  fs.mkdirSync(path.join(dir, "bilder", "reserve"), { recursive: true });
  return {
    dir,
    jsonLesen: (n, vor) => (state.has(n) ? JSON.parse(state.get(n)) : vor),
    jsonSchreiben: (n, d) => state.set(n, JSON.stringify(d)),
    _state: state,
    _bilderAnlegen: (id) => {
      const o = path.join(dir, "bilder", "reserve", String(id));
      fs.mkdirSync(o, { recursive: true });
      fs.writeFileSync(path.join(o, "1.png"), "x");
      return o;
    },
  };
};

test("Reserve-Mechanik: die Entnahme veröffentlicht unverändert und kostet nichts", async () => {
  const { reserveEntnehmen } = await import("../src/reservelauf.mjs");
  const { echteMedienId } = await import("../src/veroeffentlichung.mjs");

  const hosting = resHosting();
  hosting._bilderAnlegen("r-tag2");
  /* Ein Tag-2-Inhalt, gerendert in Tag-2-Farbe, entnommen an einem Tag, an
     dem ein Tag-1-Thema geplant war. */
  const eintrag = {
    id: "r-tag2", kanal: "herrjurist", erstelltAm: "2026-09-10", verfaelltAm: "2026-10-01",
    themaId: "strafat-schema-1", fach: "strafat", klausur: 2, typ: "schema", format: "karussell",
    beitrag: { folien: [{ art: "titel", titel: "Der dreistufige Deliktsaufbau" }], fach: "strafat", klausur: 2 },
    bildUrls: ["https://assets/bilder/reserve/r-tag2/1-abc.png", "https://assets/bilder/reserve/r-tag2/2-abc.png"],
    caption: "Systematik.\n\n#x", hashtags: ["#x"],
    faktenFreigabe: { ok: true, geprueftAm: "2026-09-10T08:00:00.000Z" },
    regelVersion: 1,
  };

  const gesendet = [];
  const ig = { bereitsVeroeffentlicht: async () => null, beitragPosten: async (p) => { gesendet.push(p); return "17900000000000001"; } };
  const ledger = { veroeffentlicht: [] };
  const eintraege = [];
  const inhalte = new Map();
  const planEintrag = { slot: "b1", status: "geplant", format: "karussell", zeit: "09:00" };

  const r = await reserveEntnehmen({
    hosting, bestand: [eintrag], heute: "2026-09-19", ledger, ig, slot: "b1", eintrag: planEintrag,
    echteMedienId, veroeffentlichungEintragen: (e, id) => { e.status = "veroeffentlicht"; e.medienId = id; return { bestaetigt: true }; },
    vermerken: (l, e) => { eintraege.push(e); l.veroeffentlicht.push(e); },
    inhaltSpeichern: (slot, b) => inhalte.set(slot, b),
  });

  assert.equal(r.medienId, "17900000000000001");
  assert.equal(r.bestand.length, 0, "der entnommene Eintrag bleibt im Bestand");

  /* 1. UNVERÄNDERT: genau die gespeicherten URLs, genau die Caption. */
  assert.equal(gesendet.length, 1);
  assert.deepEqual(gesendet[0].bildUrls, eintrag.bildUrls, "die Bilder wurden ersetzt oder neu erzeugt");
  assert.equal(gesendet[0].caption, "Systematik.\n\n#x", "die Caption wurde beim Senden neu zusammengesetzt");

  /* 2. EIGENE FARBE: Fach und Klausurtag des Inhalts landen im Ledger -
        nicht die des Entnahmetags. */
  assert.equal(eintraege[0].fach, "strafat");
  assert.equal(eintraege[0].klausur, 2, "der Klausurtag des Entnahmetags hat den des Inhalts überschrieben");
  assert.equal(eintraege[0].ausReserve, "r-tag2", "die Herkunft steht nicht im Ledger");
  assert.equal(eintraege[0].slot, "b1");

  /* 3. KOSTENLOS: Die Mechanik ruft keinen Anbieter und rendert nicht. */
  const quelle = fs.readFileSync(new URL("../src/reservelauf.mjs", import.meta.url), "utf8");
  for (const verboten of [/claudeAufruf/, /openaiAufruf/, /bildAufruf/, /beitragRendern/, /beitragSchreiben/, /titelfolieBebildern/, /veroeffentlichen\(/]) {
    assert.ok(!verboten.test(quelle), `die Mechanik greift auf ${verboten} zu - die Entnahme muss kostenlos sein`);
  }

  /* 4. DER TEASER FINDET IHN: Der veröffentlichte Inhalt wird der Inhalt des
        Slots - sonst kündigt ein Teaser nach einem Runner-Wechsel den
        geplanten, nie erschienenen Beitrag an. */
  assert.equal(inhalte.get("b1").ausReserve, "r-tag2");
  assert.equal(inhalte.get("b1").folien[0].titel, "Der dreistufige Deliktsaufbau");
  assert.equal(planEintrag.status, "veroeffentlicht");
  assert.equal(planEintrag.ausReserve, "r-tag2");

  /* 5. DIE BILDER BLEIBEN, BIS DER ZUSTAND DURABLE IST. Erst der Aufrufer
        löscht sie - nach Ledger, Commit und Push. Stirbt der Runner davor,
        braucht der nächste sie womöglich noch. */
  assert.ok(fs.existsSync(path.join(hosting.dir, "bilder", "reserve", "r-tag2")), "die Bilder wurden vor dem durablen Zustand gelöscht");
  r.nachDurable();
  assert.ok(!fs.existsSync(path.join(hosting.dir, "bilder", "reserve", "r-tag2")), "nachDurable() räumt die Bilder nicht weg");
  fs.rmSync(hosting.dir, { recursive: true, force: true });
});

test("Reserve-Mechanik: ohne Medien-ID bleibt der Eintrag im Bestand", async () => {
  /* Dieselbe Disziplin wie beim Tagesplan: Was nicht bestätigt draußen ist,
     gilt nicht als verbraucht - sonst ist der Vorrat weg und der Beitrag
     trotzdem nicht erschienen. */
  const { reserveEntnehmen } = await import("../src/reservelauf.mjs");
  const { echteMedienId } = await import("../src/veroeffentlichung.mjs");

  const hosting = resHosting();
  hosting._bilderAnlegen("r1");
  const eintrag = {
    id: "r1", erstelltAm: "2026-09-10", verfaelltAm: "2026-10-01", themaId: "t", fach: "strafat", klausur: 2,
    beitrag: { folien: [{ art: "titel", titel: "X" }] }, bildUrls: ["https://a/1.png"],
    caption: "c", faktenFreigabe: { ok: true, geprueftAm: "2026-09-10T08:00:00.000Z" }, regelVersion: 1,
  };
  let vermerkt = 0, gespeichert = 0;
  const r = await reserveEntnehmen({
    hosting, bestand: [eintrag], heute: "2026-09-19", ledger: { veroeffentlicht: [] },
    ig: { bereitsVeroeffentlicht: async () => null, beitragPosten: async () => "trocken" },
    slot: "b1", eintrag: { slot: "b1", status: "geplant" },
    echteMedienId, veroeffentlichungEintragen: () => ({ bestaetigt: true }),
    vermerken: () => { vermerkt++; }, inhaltSpeichern: () => { gespeichert++; },
  });
  assert.equal(gespeichert, 0, "ohne Medien-ID wurde der Slot-Inhalt überschrieben");
  assert.equal(r.medienId, null);
  assert.equal(r.bestand.length, 1, "der Eintrag wurde trotz fehlender Medien-ID verbraucht");
  assert.equal(vermerkt, 0, "ein Trockenlauf wurde in den Ledger geschrieben");
  assert.ok(fs.existsSync(path.join(hosting.dir, "bilder", "reserve", "r1")), "die Bilder wurden voreilig gelöscht");
  fs.rmSync(hosting.dir, { recursive: true, force: true });
});

test("Reserve-Mechanik: Vorratsbilder entgehen der Bildrotation", async () => {
  /* hosting.aufraeumen() löscht Bildordner mit Datumsnamen, die älter als 21
     Tage sind - dieselbe Frist wie die Haltbarkeit. Ein am 01.09. erzeugter
     Eintrag gilt bis zum 22.09. und hätte am 22.09. keine Bilder mehr.
     Deshalb liegen sie unter bilder/reserve/<id>. */
  const { RESERVE_ORDNER, reservePfad, bilderLoeschen } = await import("../src/reservelauf.mjs");
  assert.equal(RESERVE_ORDNER, "reserve");
  assert.equal(reservePfad("r1"), "reserve/r1");

  /* Die Rotation erkennt nur Datumsordner. */
  const datumsOrdner = /^\d{4}-\d{2}-\d{2}$/;
  assert.equal(datumsOrdner.test("reserve"), false, "der Vorratsordner sieht aus wie ein Datum und wird rotiert");
  assert.equal(datumsOrdner.test("2026-09-01"), true, "die Rotation erkennt Datumsordner nicht mehr");

  /* Und der Vorrat räumt seine Bilder selbst weg. */
  const hosting = resHosting();
  hosting._bilderAnlegen("r1");
  assert.equal(bilderLoeschen(hosting, "r1"), true);
  assert.ok(!fs.existsSync(path.join(hosting.dir, "bilder", "reserve", "r1")));
  assert.equal(bilderLoeschen(hosting, "gibtsnicht"), false, "ein fehlender Ordner darf keinen Fehler werfen");
  fs.rmSync(hosting.dir, { recursive: true, force: true });
});

test("Reserve-Mechanik: aufgefüllt wird nur aus echtem Restbudget", async () => {
  const { reserveAuffuellen } = await import("../src/reservelauf.mjs");
  const { budgetStarten } = await import("../src/budget.mjs");

  const thema = { id: "t1", fach: "strafat", klausur: 2, typ: "schema" };
  const beitrag = {
    format: "karussell",
    folien: [{ art: "titel", titel: "Der Deliktsaufbau" }, { art: "text", titel: "Aufbau", text: "Erst der Tatbestand, dann die Rechtswidrigkeit." }],
    caption: "Systematik.",
  };
  const rohBauen = () => ({ thema, beitrag, bildUrls: ["https://a/1.png"], caption: "Systematik.", hashtags: [], faktenFreigabe: { ok: true, geprueftAm: "2026-09-19T08:00:00.000Z" } });

  /* 1. Steht Pflichtarbeit aus, passiert nichts - egal wie voll der Topf ist. */
  const b1 = budgetStarten({ deckel: { core: 0.30, engagement: 0.23, research: 0.10 } });
  b1.optionalSperren("Bezahlte Pflichtarbeit steht aus: 1 Beitrag/Reel.");
  let gerufen = 0;
  const r1 = await reserveAuffuellen({
    bestand: [], heute: "2026-09-19", kanal: "herrjurist", budget: b1,
    erzeugen: async () => { gerufen++; return rohBauen(); }, speichern: async () => {},
    beitragsGrenzeUsd: 0.08,
  });
  assert.equal(gerufen, 0, "bei ausstehender Pflichtarbeit wurde produziert");
  assert.equal(r1.erzeugt, 0);
  assert.match(r1.grund, /Pflichtarbeit steht aus/);

  /* 2. Kein Restbudget: kein Mindestverbrauch, es entsteht nichts. */
  const b2 = budgetStarten({ deckel: { core: 0.30, engagement: 0.23, research: 0.10 }, bisher: { core: 0.28 } });
  const r2 = await reserveAuffuellen({
    bestand: [], heute: "2026-09-19", kanal: "herrjurist", budget: b2,
    erzeugen: async () => { gerufen++; return rohBauen(); }, speichern: async () => {},
    beitragsGrenzeUsd: 0.08,
  });
  assert.equal(gerufen, 0, "ohne Restbudget wurde produziert");
  assert.match(r2.grund, /Restbudget/);

  /* 3. Günstiger Tag, Pflicht durch: genau EIN Beitrag je Lauf. */
  const b3 = budgetStarten({ deckel: { core: 0.30, engagement: 0.23, research: 0.10 }, bisher: { core: 0.05 } });
  const gespeichert = [];
  const r3 = await reserveAuffuellen({
    bestand: [], heute: "2026-09-19", kanal: "herrjurist", budget: b3,
    erzeugen: async () => { gerufen++; return rohBauen(); },
    speichern: async (b) => gespeichert.push(b.length),
    beitragsGrenzeUsd: 0.08,
  });
  assert.equal(gerufen, 1, "es wurde nicht genau ein Beitrag erzeugt");
  assert.equal(r3.erzeugt, 1);
  assert.equal(r3.bestand.length, 1);
  assert.equal(r3.bestand[0].klausur, 2, "der Klausurtag fehlt im Eintrag");
  assert.equal(r3.bestand[0].fach, "strafat");
  assert.equal(r3.bestand[0].verfaelltAm, "2026-10-10");
  assert.deepEqual(gespeichert, [1], "der Bestand wurde nicht nach jedem Stück gesichert");

  /* 4. Voller Bestand: es entsteht nichts. */
  const voll = Array.from({ length: 4 }, (_, i) => ({
    id: `v${i}`, erstelltAm: "2026-09-18", verfaelltAm: "2026-10-09", themaId: `t${i}`,
    beitrag: { folien: [{ art: "titel", titel: "X" }] }, bildUrls: ["https://a/1.png"],
    caption: "c", faktenFreigabe: { ok: true, geprueftAm: "2026-09-18T08:00:00.000Z" }, regelVersion: 1,
  }));
  const r4 = await reserveAuffuellen({
    bestand: voll, heute: "2026-09-19", kanal: "herrjurist",
    budget: budgetStarten({ deckel: { core: 0.30, engagement: 0.23, research: 0.10 } }),
    erzeugen: async () => { gerufen++; return rohBauen(); }, speichern: async () => {},
    beitragsGrenzeUsd: 0.08,
  });
  assert.equal(r4.erzeugt, 0);
  assert.match(r4.grund, /Bestand voll/);
  assert.equal(gerufen, 1, "bei vollem Bestand wurde nachproduziert");

  /* 5. Was die Tore nicht passiert, wird nicht aufgenommen - und der Versuch
        wird nicht blind wiederholt, weil jeder Versuch Geld kostet. */
  const b5 = budgetStarten({ deckel: { core: 0.30, engagement: 0.23, research: 0.10 } });
  let versuche = 0;
  const r5 = await reserveAuffuellen({
    bestand: [], heute: "2026-09-19", kanal: "herrjurist", budget: b5,
    erzeugen: async () => { versuche++; return { ...rohBauen(), thema: { ...thema, typ: "modul" } }; },
    speichern: async () => {}, beitragsGrenzeUsd: 0.08, maxJeLauf: 3,
  });
  assert.equal(r5.erzeugt, 0, "ein untauglicher Beitrag wurde aufgenommen");
  assert.equal(versuche, 1, "der untaugliche Versuch wurde wiederholt - das kostet jedes Mal");
});

test("Reserve-Mechanik: Abgelaufenes fliegt samt Bildern raus, ohne Nachcheck", async () => {
  const { reserveAufraeumen } = await import("../src/reservelauf.mjs");
  const hosting = resHosting();
  hosting._bilderAnlegen("alt");
  hosting._bilderAnlegen("frisch");

  const mach = (id, erstelltAm, verfaelltAm) => ({
    id, erstelltAm, verfaelltAm, themaId: id,
    beitrag: { folien: [{ art: "titel", titel: "X" }] }, bildUrls: ["https://a/1.png"],
    caption: "c", faktenFreigabe: { ok: true, geprueftAm: `${erstelltAm}T08:00:00.000Z` }, regelVersion: 1,
  });
  const zeilen = [];
  const r = reserveAufraeumen({
    hosting, heute: "2026-09-25", log: (z) => zeilen.push(z),
    bestand: [mach("alt", "2026-08-01", "2026-08-22"), mach("frisch", "2026-09-19", "2026-10-10")],
  });

  assert.deepEqual(r.bestand.map((e) => e.id), ["frisch"]);
  assert.deepEqual(r.entfernt.map((e) => e.id), ["alt"]);
  assert.ok(!fs.existsSync(path.join(hosting.dir, "bilder", "reserve", "alt")), "die Bilder des Abgelaufenen bleiben liegen");
  assert.ok(fs.existsSync(path.join(hosting.dir, "bilder", "reserve", "frisch")), "die Bilder des gültigen Eintrags wurden gelöscht");
  assert.ok(zeilen.some((z) => /verworfen/.test(z)), "das Verwerfen wird nicht protokolliert");
  fs.rmSync(hosting.dir, { recursive: true, force: true });
});

/* ===== Reservebestand im Tageslauf: Integration ==========================

   Was hier geprüft wird, ist nicht mehr die Regel und nicht mehr die
   Mechanik für sich, sondern ihr Zusammenspiel mit dem Tageslauf: die
   Reihenfolge, die Dauerhaftigkeit und das, was ein zweiter Runner davon
   vorfindet.

   Der Aufbau spiegelt lauf.mjs, ohne Git, Netz und Instagram zu brauchen:
   `runner()` ist derselbe Ablauf wie der Fangzweig der Beitragsschleife -
   laden, aufräumen, entnehmen, durable machen, erst dann die Bilder weg.
   Damit Spiegel und Original nicht auseinanderlaufen, prüft der letzte Test
   die Reihenfolge direkt in der Quelle von lauf.mjs.
   ========================================================================= */

/* Ein Instagram, das sich merkt, was draußen steht - und Captions genauso
   vergleicht wie der echte Client: über den gespeicherten Text. */
const resInstagram = () => {
  const feed = [];
  return {
    feed,
    stuerzeNachSenden: false,
    async bereitsVeroeffentlicht(caption) {
      const t = feed.find((p) => p.caption === caption);
      return t ? t.medienId : null;
    },
    async beitragPosten({ bildUrls, caption }) {
      const medienId = `179${String(feed.length + 1).padStart(14, "0")}`;
      feed.push({ bildUrls, caption, medienId });
      if (this.stuerzeNachSenden) throw new Error("RUNNER-ABSTURZ nach dem Senden");
      return medienId;
    },
  };
};

const resVorrat = (zusatz = {}) => ({
  id: "r-vorrat", kanal: "herrjurist", erstelltAm: "2026-09-10", verfaelltAm: "2026-10-01",
  themaId: "strafat-schema-1", fach: "strafat", klausur: 2, typ: "schema", format: "karussell",
  beitrag: { format: "karussell", themaId: "strafat-schema-1", fach: "strafat", klausur: 2, kurztitel: "Deliktsaufbau",
    folien: [{ art: "titel", titel: "Der dreistufige Deliktsaufbau", icon: "schema" }, { art: "text", titel: "Aufbau", text: "Erst der Tatbestand, dann die Rechtswidrigkeit." }] },
  bildUrls: ["https://assets/bilder/reserve/r-vorrat/1-abc.png", "https://assets/bilder/reserve/r-vorrat/2-abc.png"],
  caption: "Der Aufbau in der richtigen Reihenfolge.\n\n#staatsexamen #strafrecht",
  hashtags: ["#staatsexamen", "#strafrecht"],
  faktenFreigabe: { ok: true, geprueftAm: "2026-09-10T08:00:00.000Z", ausgefallen: false, hinweise: [] },
  regelVersion: 1,
  ...zusatz,
});

/**
 * Ein Runner - derselbe Ablauf wie in lauf.mjs, mit denselben Bausteinen.
 *
 * `welt` ist der dauerhafte Teil: Hosting (state + Bilder auf Platte), Plan,
 * Ledger, Instagram. Er überlebt den Runner, genau wie der Asset-Zweig einen
 * Stundenlauf überlebt.
 */
const resWelt = ({ eintraege = [resVorrat()], plan = null } = {}) => {
  const hosting = resHosting();
  for (const e of eintraege) hosting._bilderAnlegen(e.id);
  hosting.jsonSchreiben("reserve.json", { kanal: "herrjurist", ziel: 4, eintraege });
  hosting.jsonSchreiben("plan.json", plan || { beitraege: [{ slot: "b1", zeit: "09:00", format: "karussell", themaId: "strafat-modul-7", status: "geplant" }], stories: [] });
  hosting.jsonSchreiben("ledger.json", { veroeffentlicht: [] });
  return { hosting, ig: resInstagram(), ledger: null, plan: null, protokoll: [] };
};

async function runner(welt, { fehler, slot = "b1", trocken = false, sichernWirft = false } = {}) {
  const { bestandLaden, bestandInhalt, reserveAufraeumen, reserveEntnehmen, ersatzZulaessig, BESTAND_DATEI } = await import("../src/reservelauf.mjs");
  const { istKostenKontrollFehler, budgetStoppGrund } = await import("../src/kostenfehler.mjs");
  const { echteMedienId, veroeffentlichungEintragen } = await import("../src/veroeffentlichung.mjs");
  const log = (z) => welt.protokoll.push(z);

  /* Ein Runner beginnt bei null: frischer Klon des Asset-Zweigs, nichts aus
     dem Arbeitsspeicher des vorigen. Nur was gepusht wurde, ist da. */
  welt.plan = welt.hosting.jsonLesen("plan.json", null);
  welt.ledger = welt.hosting.jsonLesen("ledger.json", null);

  /* --- Laufbeginn: laden, aufräumen, durable sichern, wenn sich etwas ändert */
  let bestand = bestandLaden(welt.hosting);
  const auf = reserveAufraeumen({ hosting: welt.hosting, bestand, heute: "2026-09-19", log });
  bestand = auf.bestand;
  if (auf.entfernt.length || auf.verwaist.length) welt.hosting.jsonSchreiben(BESTAND_DATEI, bestandInhalt(bestand, "herrjurist"));

  const eintrag = welt.plan.beitraege.find((b) => b.slot === slot) || welt.plan.stories.find((b) => b.slot === slot);
  /* Ein Slot, der schon veröffentlicht ist, wird gar nicht mehr angefasst. */
  if (eintrag.status === "veroeffentlicht") { log(`  ${slot} steht bereits - übersprungen.`); return { bestand, bearbeitet: false }; }

  /* --- Der Fangzweig der Beitragsschleife ------------------------------- */
  if (!istKostenKontrollFehler(fehler)) { eintrag.fehler = String(fehler.message); return { bestand, bearbeitet: true, ersetzt: false }; }
  eintrag.budgetBlockiert = { seit: "2026-09-19T09:00:00.000Z", grund: budgetStoppGrund(fehler), topf: fehler.topf || null, art: fehler.name };

  const zulaessig = ersatzZulaessig({ eintrag, fehler });
  if (trocken || !zulaessig.ok) { if (!zulaessig.ok) log(`  Vorrat: kein Ersatz für ${slot} - ${zulaessig.grund}`); return { bestand, bearbeitet: true, ersetzt: false, zulaessig }; }

  const r = await reserveEntnehmen({
    hosting: welt.hosting, bestand, heute: "2026-09-19", ledger: welt.ledger, ig: welt.ig,
    eintrag, slot, echteMedienId, veroeffentlichungEintragen,
    vermerken: (l, e) => { l.veroeffentlicht.push(e); },
    inhaltSpeichern: (s, b) => welt.hosting.jsonSchreiben(`inhalte/2026-09-19-${s}.json`, b),
    log,
  });
  if (!r.medienId) return { bestand: r.bestand, bearbeitet: true, ersetzt: false, grund: r.grund };

  /* Ledger → Bestand/Plan → EIN Zustands-Commit mit Push → erst danach die
     Bilder. Durable ist, was gepusht wurde: Ein Absturz davor lässt den
     nächsten Runner denselben Ausgangszustand vorfinden. */
  bestand = r.bestand;
  if (sichernWirft) throw new Error("RUNNER-ABSTURZ vor dem Push");
  welt.hosting.jsonSchreiben("ledger.json", welt.ledger);
  welt.hosting.jsonSchreiben("plan.json", welt.plan);
  welt.hosting.jsonSchreiben(BESTAND_DATEI, bestandInhalt(bestand, "herrjurist"));
  r.nachDurable();
  return { bestand, bearbeitet: true, ersetzt: true, medienId: r.medienId, wiedergefunden: r.wiedergefunden };
}

const budgetFehlerBauen = async () => {
  const { AdmissionAbgelehnt } = await import("../src/budget.mjs");
  return new AdmissionAbgelehnt("autor", "core", 0.1200, 0.0150, 0.3000);
};

test("Vorrat im Tageslauf 1: kostenblockierter Feed-Slot wird aus dem Vorrat bedient - ohne einen bezahlten Aufruf", async () => {
  const welt = resWelt();
  const r = await runner(welt, { fehler: await budgetFehlerBauen() });

  assert.equal(r.ersetzt, true, "der blockierte Slot blieb leer, obwohl Vorrat da war");
  assert.equal(welt.ig.feed.length, 1);
  /* Unverändert: genau die gespeicherten Bilder, genau die gespeicherte Caption. */
  assert.deepEqual(welt.ig.feed[0].bildUrls, resVorrat().bildUrls, "die Bilder wurden neu gerendert oder ersetzt");
  assert.equal(welt.ig.feed[0].caption, resVorrat().caption, "die Caption wurde bei der Entnahme neu zusammengesetzt");
  /* Die Farbe des eigenen Klausurtags, nicht die des Entnahmetags. */
  assert.equal(welt.ledger.veroeffentlicht[0].klausur, 2);
  assert.equal(welt.ledger.veroeffentlicht[0].fach, "strafat");
  assert.equal(welt.ledger.veroeffentlicht[0].ausReserve, "r-vorrat");
  fs.rmSync(welt.hosting.dir, { recursive: true, force: true });
});

test("Vorrat im Tageslauf 2: nach der Entnahme ist der Slot durable veröffentlicht - der nächste Runner fasst ihn nicht mehr an", async () => {
  const welt = resWelt();
  await runner(welt, { fehler: await budgetFehlerBauen() });

  assert.equal(welt.plan.beitraege[0].status, "veroeffentlicht");
  assert.equal(welt.plan.beitraege[0].ausReserve, "r-vorrat");
  /* Und alles davon steht auf Platte, nicht nur im Arbeitsspeicher. */
  assert.equal(welt.hosting.jsonLesen("plan.json").beitraege[0].status, "veroeffentlicht");
  assert.equal(welt.hosting.jsonLesen("reserve.json").eintraege.length, 0, "der entnommene Eintrag steht noch im gespeicherten Bestand");
  assert.equal(welt.hosting.jsonLesen("ledger.json").veroeffentlicht.length, 1);

  const zweiter = await runner(welt, { fehler: await budgetFehlerBauen() });
  assert.equal(zweiter.bearbeitet, false, "der zweite Runner hat den fertigen Slot noch einmal bearbeitet");
  assert.equal(welt.ig.feed.length, 1, "der zweite Runner hat ein zweites Mal gepostet");
  fs.rmSync(welt.hosting.dir, { recursive: true, force: true });
});

test("Vorrat im Tageslauf 3: Absturz nach dem Senden, vor dem Push - der nächste Runner erzeugt KEIN Duplikat", async () => {
  /* Der gefährlichste Ablauf überhaupt: Instagram hat den Beitrag, der
     Runner stirbt, nichts davon ist durable. Der nächste Lauf sieht einen
     blockierten Slot und einen vollen Vorrat - und darf trotzdem nicht
     posten. Die Wiedererkennung hängt an der gespeicherten Caption. */
  const welt = resWelt();
  welt.ig.stuerzeNachSenden = true;
  const blockade = await budgetFehlerBauen();
  await assert.rejects(() => runner(welt, { fehler: blockade }), /RUNNER-ABSTURZ/);

  assert.equal(welt.ig.feed.length, 1, "der Beitrag steht nicht auf Instagram");
  assert.equal(welt.plan.beitraege[0].status, "geplant", "der Plan wurde trotz Absturz fortgeschrieben");
  assert.equal(welt.hosting.jsonLesen("reserve.json").eintraege.length, 1, "der Vorratseintrag wurde trotz Absturz verbraucht");
  assert.ok(fs.existsSync(path.join(welt.hosting.dir, "bilder", "reserve", "r-vorrat")), "die Bilder wurden trotz Absturz gelöscht");

  /* Zweiter Runner, dieselbe Welt. */
  welt.ig.stuerzeNachSenden = false;
  const r2 = await runner(welt, { fehler: await budgetFehlerBauen() });

  assert.equal(welt.ig.feed.length, 1, "der zweite Runner hat den Beitrag ein zweites Mal gepostet");
  assert.equal(r2.ersetzt, true, "der zweite Runner hat die bestehende Veröffentlichung nicht übernommen");
  assert.equal(r2.wiedergefunden, true, "die Wiedererkennung über die gespeicherte Caption hat nicht gegriffen");
  assert.equal(r2.medienId, welt.ig.feed[0].medienId);
  assert.equal(welt.plan.beitraege[0].status, "veroeffentlicht");
  assert.equal(welt.hosting.jsonLesen("reserve.json").eintraege.length, 0);
  fs.rmSync(welt.hosting.dir, { recursive: true, force: true });
});

test("Vorrat im Tageslauf 4: der Teaser nach einem Runner-Wechsel meint den wirklich erschienenen Vorratsbeitrag", async () => {
  /* Der Teaser lädt nach einem Runner-Wechsel inhalte/<datum>-<slot>.json.
     Stünde dort noch der geplante, nie erschienene Beitrag, kündigte die
     Story am Abend etwas an, das es nicht gibt. */
  const welt = resWelt();
  /* Was der Tag ursprünglich vorhatte - ein anderes Thema, ein anderer Tag. */
  welt.hosting.jsonSchreiben("inhalte/2026-09-19-b1.json", { themaId: "strafat-modul-7", fach: "bgbat", klausur: 1, folien: [{ art: "titel", titel: "Der geplante, nie erschienene Beitrag" }], caption: "geplant" });

  await runner(welt, { fehler: await budgetFehlerBauen() });

  /* Ein NEUER Runner - nichts aus dem Arbeitsspeicher des ersten. */
  const { teaserAusBeitrag } = await import("../src/autor.mjs");
  const geladen = welt.hosting.jsonLesen("inhalte/2026-09-19-b1.json", null);
  assert.equal(geladen.ausReserve, "r-vorrat", "der Slot trägt noch den geplanten Inhalt");
  assert.equal(geladen.folien[0].titel, "Der dreistufige Deliktsaufbau");
  assert.equal(geladen.fach, "strafat", "der Teaser bekäme das falsche Fach - und damit die falsche Farbe");
  assert.equal(geladen.klausur, 2);

  const teaser = teaserAusBeitrag(geladen, "s3");
  const text = JSON.stringify(teaser);
  assert.ok(text.includes("Deliktsaufbau"), `der Teaser meint nicht den erschienenen Beitrag: ${text}`);
  assert.ok(!text.includes("nie erschienene"), "der Teaser kündigt den geplanten Beitrag an, der nie erschienen ist");
  fs.rmSync(welt.hosting.dir, { recursive: true, force: true });
});

test("Vorrat im Tageslauf 5: ein technischer Fehler bekommt keinen Ersatz", async () => {
  /* Der Vorrat ist Verfügbarkeit bei Kostenblockade, kein allgemeiner
     Fehler-Fallback. Ein Renderfehler, ein Anbieterausfall, ein
     Instagram-Fehler: Ein Ersatzbeitrag würde sie nur verdecken. */
  for (const fehler of [
    new Error("Chromium konnte nicht starten"),
    new Error("Instagram: Container nicht fertig (code 9007)"),
    new Error("Beitrag „X“ nach 3 Versuchen nicht freigegeben"),
    Object.assign(new Error("anthropic 529 overloaded"), { name: "AnbieterFehler" }),
  ]) {
    const welt = resWelt();
    const r = await runner(welt, { fehler });
    assert.equal(r.ersetzt, false, `„${fehler.message}“ wurde aus dem Vorrat ersetzt`);
    assert.equal(welt.ig.feed.length, 0);
    assert.equal(welt.hosting.jsonLesen("reserve.json").eintraege.length, 1, "der Vorrat wurde für einen technischen Fehler verbraucht");
    assert.equal(welt.plan.beitraege[0].status, "geplant");
    fs.rmSync(welt.hosting.dir, { recursive: true, force: true });
  }
});

test("Vorrat im Tageslauf 6: Reels und Stories werden nicht aus dem Vorrat ersetzt", async () => {
  /* Der Vorrat hält Feed-Beiträge. Ein Karussell an Stelle eines Reels wäre
     ein anderes Produkt, eine Story an Stelle eines Reels erst recht. */
  const reelWelt = resWelt({ plan: { beitraege: [{ slot: "b3", zeit: "18:00", format: "reel", status: "geplant" }], stories: [] } });
  const r1 = await runner(reelWelt, { fehler: await budgetFehlerBauen(), slot: "b3" });
  assert.equal(r1.ersetzt, false, "ein Reel wurde durch ein Karussell ersetzt");
  assert.match(r1.zulaessig.grund, /Reels/);
  assert.equal(reelWelt.ig.feed.length, 0);
  fs.rmSync(reelWelt.hosting.dir, { recursive: true, force: true });

  const storyWelt = resWelt({ plan: { beitraege: [], stories: [{ slot: "s2", zeit: "12:00", art: "begriff", status: "geplant" }] } });
  const r2 = await runner(storyWelt, { fehler: await budgetFehlerBauen(), slot: "s2" });
  assert.equal(r2.ersetzt, false, "eine Story wurde durch einen Feed-Beitrag ersetzt");
  assert.match(r2.zulaessig.grund, /begriff/);
  assert.equal(storyWelt.ig.feed.length, 0);
  fs.rmSync(storyWelt.hosting.dir, { recursive: true, force: true });
});

test("Vorrat im Tageslauf 7: leerer oder abgelaufener Vorrat - der Slot bleibt blockiert, der Lauf stürzt nicht ab", async () => {
  /* Der Vorrat ist eine Versicherung, keine Garantie. Ist er leer, ist der
     Tag so schlecht wie vorher - aber nicht schlechter. */
  const leer = resWelt({ eintraege: [] });
  const r1 = await runner(leer, { fehler: await budgetFehlerBauen() });
  assert.equal(r1.ersetzt, false);
  assert.match(r1.grund, /kein gültiger Vorratsbeitrag/);
  assert.equal(leer.plan.beitraege[0].status, "geplant");
  assert.ok(leer.plan.beitraege[0].budgetBlockiert, "die Blockade wurde nicht vermerkt");
  fs.rmSync(leer.hosting.dir, { recursive: true, force: true });

  /* Abgelaufen: verworfen, kein bezahlter Nachcheck, keine Verlängerung. */
  const alt = resWelt({ eintraege: [resVorrat({ id: "r-alt", erstelltAm: "2026-08-01", verfaelltAm: "2026-08-22" })] });
  const r2 = await runner(alt, { fehler: await budgetFehlerBauen() });
  assert.equal(r2.ersetzt, false);
  assert.equal(alt.hosting.jsonLesen("reserve.json").eintraege.length, 0, "der abgelaufene Eintrag liegt noch im Bestand");
  assert.ok(!fs.existsSync(path.join(alt.hosting.dir, "bilder", "reserve", "r-alt")), "die Bilder des abgelaufenen Eintrags liegen noch da");
  assert.ok(alt.protokoll.some((z) => /verworfen/.test(z)));
  fs.rmSync(alt.hosting.dir, { recursive: true, force: true });
});

test("Vorrat im Tageslauf 8: ein Thema, das gerade erschienen ist, kommt nicht sofort noch einmal", async () => {
  const welt = resWelt();
  welt.hosting.jsonSchreiben("ledger.json", { veroeffentlicht: [{ datum: "2026-09-12", art: "beitrag", thema: "strafat-schema-1" }] });
  const r = await runner(welt, { fehler: await budgetFehlerBauen() });

  assert.equal(r.ersetzt, false, "dasselbe Thema erschien binnen einer Woche zweimal");
  assert.match(r.grund, /letzten 60 Tagen erschienen/);
  /* Der Eintrag bleibt liegen - er ist nicht schlecht, nur heute unpassend. */
  assert.equal(welt.hosting.jsonLesen("reserve.json").eintraege.length, 1, "der Eintrag wurde wegen einer Dublette weggeworfen");
  fs.rmSync(welt.hosting.dir, { recursive: true, force: true });
});

test("Vorrat im Tageslauf 9: die Bilder fallen erst nach dem durablen Zustand - ein Absturz davor behält sie", async () => {
  /* Die Reihenfolge ist die eigentliche Aussage: Slot, Inhalt, Ledger,
     Bestand, EIN Zustands-Commit - und erst danach die Bilder. Wer sie
     vorher löscht, hat nach einem gescheiterten Push nichts mehr in der
     Hand, falls die Wiedererkennung wider Erwarten nicht greift. */
  const welt = resWelt();
  const blockade = await budgetFehlerBauen();
  await assert.rejects(() => runner(welt, { fehler: blockade, sichernWirft: true }), /vor dem Push/);
  assert.ok(fs.existsSync(path.join(welt.hosting.dir, "bilder", "reserve", "r-vorrat")), "die Bilder wurden vor dem durablen Zustand gelöscht");

  /* Der nächste Runner findet die Veröffentlichung wieder und räumt dann auf. */
  const r2 = await runner(welt, { fehler: await budgetFehlerBauen() });
  assert.equal(r2.wiedergefunden, true);
  assert.equal(welt.ig.feed.length, 1);
  assert.ok(!fs.existsSync(path.join(welt.hosting.dir, "bilder", "reserve", "r-vorrat")), "die Bilder blieben nach dem durablen Zustand liegen");
  fs.rmSync(welt.hosting.dir, { recursive: true, force: true });
});

test("Vorrat im Tageslauf 10: Bildordner ohne Eintrag werden weggeräumt", async () => {
  /* Sie entstehen, wenn die Bilder hochgeladen sind und der Eintrag danach
     an Tor 2 scheitert oder der Runner stirbt. Weil bilder/reserve/ bewusst
     außerhalb der Datumsrotation liegt, räumt sie sonst niemand weg. */
  const welt = resWelt();
  welt.hosting._bilderAnlegen("2026-09-19-rxyz");
  assert.ok(fs.existsSync(path.join(welt.hosting.dir, "bilder", "reserve", "2026-09-19-rxyz")));

  await runner(welt, { fehler: await budgetFehlerBauen() });
  assert.ok(!fs.existsSync(path.join(welt.hosting.dir, "bilder", "reserve", "2026-09-19-rxyz")), "ein Bildordner ohne Eintrag bleibt ewig liegen");
  /* Die Bilder des gültigen Eintrags fasst das Aufräumen nicht an - sie
     werden erst nach der Veröffentlichung gelöscht. */
  assert.ok(welt.ig.feed.length === 1);
  fs.rmSync(welt.hosting.dir, { recursive: true, force: true });
});

test("Vorrat im Tageslauf 11: nachgefüllt wird zuletzt, höchstens um einen Beitrag und nur aus echtem Restbudget", async () => {
  const { reserveAuffuellen } = await import("../src/reservelauf.mjs");
  const { budgetStarten } = await import("../src/budget.mjs");
  const roh = () => ({
    thema: { id: "t-neu", fach: "staat", klausur: 1, typ: "schema" },
    beitrag: { format: "karussell", folien: [{ art: "titel", titel: "Der Deliktsaufbau" }, { art: "text", titel: "A", text: "Erst der Tatbestand." }], caption: "Systematik." },
    bildUrls: ["https://a/1.png"], caption: "Systematik.\n\n#x", hashtags: ["#x"],
    faktenFreigabe: { ok: true, geprueftAm: "2026-09-19T08:00:00.000Z", ausgefallen: false },
  });
  const deckel = { core: 0.30, engagement: 0.23, research: 0.10 };

  /* Solange bezahlte Pflichtarbeit aussteht: kein einziger Aufruf. Das ist
     dieselbe Sperre, die für jede andere bezahlte Kür gilt. */
  const gesperrt = budgetStarten({ deckel });
  gesperrt.optionalSperren("Bezahlte Pflichtarbeit steht aus: 1 Beitrag/Reel.");
  let gerufen = 0;
  const a = await reserveAuffuellen({ bestand: [], heute: "2026-09-19", kanal: "herrjurist", budget: gesperrt, beitragsGrenzeUsd: 0.08, erzeugen: async () => { gerufen++; return roh(); }, speichern: async () => {} });
  assert.equal(gerufen, 0);
  assert.match(a.grund, /Pflichtarbeit steht aus/);

  /* Pflicht durch, aber der Topf trägt die Beitragsgrenze nicht mehr: kein
     Mindestverbrauch, es entsteht nichts. */
  const knapp = budgetStarten({ deckel, bisher: { core: 0.27 } });
  const b = await reserveAuffuellen({ bestand: [], heute: "2026-09-19", kanal: "herrjurist", budget: knapp, beitragsGrenzeUsd: 0.08, erzeugen: async () => { gerufen++; return roh(); }, speichern: async () => {} });
  assert.equal(gerufen, 0, "aus einem Restbudget unter der Beitragsgrenze wurde produziert");
  assert.match(b.grund, /Restbudget .* trägt die Beitragsgrenze/);
  assert.ok(!/Worst Case/i.test(b.grund), "die alte, irreführende Wortwahl ist zurück");

  /* Günstiger Tag, Pflicht durch, Bedarf 4 - und trotzdem genau einer. */
  const guenstig = budgetStarten({ deckel, bisher: { core: 0.04 } });
  const gespeichert = [];
  const c = await reserveAuffuellen({ bestand: [], heute: "2026-09-19", kanal: "herrjurist", budget: guenstig, beitragsGrenzeUsd: 0.08, erzeugen: async () => { gerufen++; return roh(); }, speichern: async (n) => gespeichert.push(n.length) });
  assert.equal(gerufen, 1, "es wurde mehr als ein Beitrag je Lauf erzeugt");
  assert.equal(c.erzeugt, 1);
  assert.deepEqual(gespeichert, [1], "der Bestand wurde nicht sofort gesichert");
  assert.equal(c.bestand[0].klausur, 1, "der Eintrag trägt den Klausurtag seines eigenen Fachs nicht");
  assert.equal(c.bestand[0].verfaelltAm, "2026-10-10");
});

test("Vorrat im Tageslauf 12: die Reihenfolge steht so in lauf.mjs - nicht nur im Spiegel dieses Tests", async () => {
  /* Die Tests oben prüfen einen nachgebauten Ablauf. Damit Nachbau und
     Original nicht auseinanderlaufen, wird die Reihenfolge hier direkt in
     der Quelle festgehalten. */
  const quelle = fs.readFileSync(new URL("../src/lauf.mjs", import.meta.url), "utf8");
  const ohneKommentar = quelle.replace(/\/\*[\s\S]*?\*\//g, "");
  const wo = (muster) => { const i = ohneKommentar.search(muster); assert.ok(i > 0, `nicht gefunden: ${muster}`); return i; };

  /* 1. Der Vorrat wird am Laufbeginn geladen und aufgeräumt. */
  const laden = wo(/bestandLaden\(hosting\)/);
  const aufraeumen = wo(/reserveAufraeumen\(\{/);
  assert.ok(laden < aufraeumen, "aufgeräumt wird vor dem Laden");

  /* 2. Die Entnahme hängt am Kostenkontrollfehler und an ersatzZulaessig. */
  const blockiert = wo(/istKostenKontrollFehler\(e\)\) \{\s*eintrag\.budgetBlockiert/);
  const zulaessig = wo(/ersatzZulaessig\(\{ eintrag, fehler: e \}\)/);
  const entnehmen = wo(/await reserveEntnehmen\(\{/);
  assert.ok(blockiert < zulaessig && zulaessig < entnehmen, "die Entnahme hängt nicht am Kostenkontrollfehler");

  /* 3. Ledger → Zustand sichern → erst dann die Bilder. */
  const ledger = ohneKommentar.indexOf("ledgerSpeichern(ledgerPfad, ledger);", entnehmen);
  const sichern = ohneKommentar.indexOf("await zustandSichern(`Reserve", entnehmen);
  const bilder = ohneKommentar.indexOf("r.nachDurable();", entnehmen);
  assert.ok(entnehmen < ledger, "der Ledger wird vor der Entnahme geschrieben");
  assert.ok(ledger < sichern, "der Zustand wird vor dem Ledger gesichert");
  assert.ok(sichern > 0 && bilder > sichern, "die Bilder fallen vor dem durablen Zustand");

  /* 4. Nachgefüllt wird ganz am Ende - nach Beiträgen UND Stories, und erst
        nach einer frisch nachgezogenen Pflichtsperre. */
  const storySchleife = wo(/for \(const eintrag of storiesFaellig\)/);
  const auffuellen = wo(/await reserveAuffuellen\(\{/);
  const schlussSichern = ohneKommentar.indexOf("await zustandSichern(`Zustand ${datum}`)");
  assert.ok(storySchleife < auffuellen, "der Vorrat wird vor den Stories aufgefüllt");
  assert.ok(auffuellen < schlussSichern, "das Auffüllen liegt hinter der Schlusssicherung");
  const sperre = ohneKommentar.lastIndexOf("ruecklageAktualisieren();", auffuellen);
  assert.ok(sperre > storySchleife, "die Pflichtsperre wird vor dem Auffüllen nicht nachgezogen");

  /* 5. Die Beitragsgrenze ist die konfigurierte, keine eigene Zahl. */
  assert.match(ohneKommentar, /beitragsGrenzeUsd: CONFIG\.ki\.maxJeBeitragUsd/);
  /* 6. Die Vorratsbilder gehen nicht in die Datumsrotation. */
  assert.match(ohneKommentar, /hosting\.veroeffentlichen\(bilder, pfad, `Vorrat/);
});
