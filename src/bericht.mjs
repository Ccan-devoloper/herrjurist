/* ==========================================================================
   Wochenbericht: Follower, Reichweite, beste Beiträge, Kommentare, Kosten,
   Fehler – als E-Mail (SMTP) und immer auch als Datei im Asset-Zweig.
   ========================================================================== */

import nodemailer from "nodemailer";
import { CONFIG } from "./config.mjs";
import { punkte } from "./insights.mjs";
import { zeitBericht } from "./zeiten.mjs";
import { stimmenBericht } from "./stimmen.mjs";
import { datumLesbar } from "./zeit.mjs";

export function berichtErstellen({ ledger, strategie, follower, kosten, datum, fehler = [], hinweise = [], stimme = null, stimmen = null }) {
  const woche = new Date(new Date(`${datum}T12:00:00Z`).getTime() - 7 * 86400000).toISOString().slice(0, 10);
  const beitraege = (ledger.veroeffentlicht || []).filter((e) => e.art === "beitrag" && e.datum >= woche);
  const stories = (ledger.veroeffentlicht || []).filter((e) => e.art === "story" && e.datum >= woche);
  const antworten = (ledger.interaktionen || []).filter((i) => i.datum >= woche && !i.uebersprungen);
  const karten = (ledger.nachrichten || []).filter((n) => n.datum >= woche);
  const bewertet = (ledger.veroeffentlicht || []).filter((e) => e.art === "beitrag" && e.insights).sort((a, b) => punkte(b.insights) - punkte(a.insights));
  const top = bewertet.slice(0, 3);
  const f = follower || [];
  const jetzt = f.at(-1)?.follower, vorWoche = f.filter((x) => x.datum <= woche).at(-1)?.follower;
  const zeilen = [];
  zeilen.push(`Wochenbericht Instagram-Bot · ${datumLesbar(woche)} bis ${datumLesbar(datum)}`, "");
  zeilen.push(`Follower: ${jetzt ?? "unbekannt"}${jetzt != null && vorWoche != null ? ` (${jetzt - vorWoche >= 0 ? "+" : ""}${jetzt - vorWoche} in 7 Tagen)` : ""}`);
  if (strategie?.reichweite7 != null) zeilen.push(`Reichweite letzte 7 Tage: ${strategie.reichweite7}`);
  zeilen.push(`Veröffentlicht: ${beitraege.length} Beiträge (davon ${beitraege.filter((b) => b.format === "reel").length} Reels), ${stories.length} Stories`);
  zeilen.push(`Kommentare beantwortet: ${antworten.length} · Karten per Nachricht: ${karten.length}`);
  zeilen.push(`Kosten Claude API diese Woche: ≈ ${(kosten?.usd ?? 0).toFixed(2)} $ (${kosten?.aufrufe ?? 0} Aufrufe, Cache-Anteil ${Math.round((kosten?.cacheAnteil ?? 0) * 100)} %)`);
  const tage = Object.entries(kosten?.tage || {}).sort().slice(-7);
  if (tage.length) zeilen.push(`Je Tag (Deckel ${(kosten?.limit ?? 0).toFixed(2)} $): ${tage.map(([t, v]) => `${t.slice(8)}.${t.slice(5, 7)}. ${(v.usd ?? 0).toFixed(2)} $`).join(" · ")}`);
  /* Stimme: Wie viel vom ElevenLabs-Monatsguthaben ist noch da? */
  if (stimme && (stimme.grenze || stimme.erschoepft)) {
    zeilen.push(stimme.erschoepft
      ? `Stimme: ElevenLabs-Guthaben aufgebraucht${stimme.resetAm ? ` (neu ab ${datumLesbar(String(stimme.resetAm).slice(0, 10))})` : ""} – die Reels spricht bis dahin Piper`
      : `Stimme: ElevenLabs${stimme.abo ? ` (${stimme.abo})` : ""} · ${stimme.rest ?? "?"} von ${stimme.grenze} Zeichen frei`);
  }
  /* Stimmenrennen: welche Sprecherin trägt die Reels? */
  const rennen = stimmenBericht(ledger, stimmen?.kandidaten || []);
  if (rennen) {
    zeilen.push(`Stimmen (Faktor zum Reel-Schnitt, gemessene Reels): ${rennen.zeilen.map((z) => `${z.name} ${z.mittel.toFixed(2)}× (${z.n})`).join(" · ")}`);
    if (rennen.sieger) zeilen.push(`  → entschieden: „${rennen.sieger}“ spricht ab jetzt alle Reels`);
  }
  const folgen = Object.entries(strategie?.hashtagFolgen || {}).filter(([, n]) => n > 0).sort((a, b) => b[1] - a[1]).slice(0, 6);
  if (folgen.length) zeilen.push(`Hashtags mit neuen Followern: ${folgen.map(([h, n]) => `${h} (${n})`).join(" · ")}`);
  if (strategie?.folgenGesamt != null) zeilen.push(`Neue Follower aus Beiträgen (gemessen): ${strategie.folgenGesamt}`);
  /* Gelernte Uhrzeiten: Was hat sich bewährt, und wie sicher ist das schon? */
  const zeitenGelernt = zeitBericht(ledger);
  if (zeitenGelernt.gesamt) {
    const namen = { karussell: "Karussell", reel: "Reel" };
    for (const [klasse, zeilenZeit] of Object.entries(zeitenGelernt.klassen)) {
      zeilen.push(`Beste Uhrzeiten ${namen[klasse] || klasse} (Faktor zum Schnitt, Messungen): ${zeilenZeit.map((z) => `${String(z.stunde).padStart(2, "0")}:30 ${z.mittel.toFixed(2)}× (${z.n})`).join(" · ")}`);
    }
    zeilen.push(`Uhrzeiten: ${zeitenGelernt.gesamt} Beiträge ausgewertet, davon ${zeitenGelernt.mitWirkung} mit messbarer Wirkung${zeitenGelernt.belastbar ? " – die Zeiten folgen jetzt den Zahlen" : " – noch zu dünn, der Bot probiert weiter Stunden aus"}`);
  }
  zeilen.push("");
  if (top.length) {
    zeilen.push("Beste Beiträge (Speichern ×3, Teilen ×4, Kommentare ×2, Likes, Reichweite):");
    for (const t of top) zeilen.push(`  · ${t.titel} — ${t.format}/${t.fach} · Reichweite ${t.insights.reach ?? "?"}, gespeichert ${t.insights.saved ?? "?"}, geteilt ${t.insights.shares ?? "?"}`);
    zeilen.push("");
  }
  if (strategie && Object.keys(strategie.formatGewicht || {}).length) {
    const fmt = Object.entries(strategie.formatGewicht).sort((a, b) => b[1] - a[1]).map(([k, v]) => `${k} ${v.toFixed(2)}`).join(", ");
    zeilen.push(`Gelernte Gewichte – Formate: ${fmt}`);
    const fach = Object.entries(strategie.fachGewicht || {}).sort((a, b) => b[1] - a[1]).map(([k, v]) => `${k} ${v.toFixed(2)}`).join(", ");
    if (fach) zeilen.push(`Fächer: ${fach}`);
    if (strategie.besteStunden) zeilen.push(`Beste Uhrzeiten laut Online-Zeiten der Follower: ${strategie.besteStunden.join(", ")}`);
    zeilen.push("");
  } else zeilen.push("Lernschleife: noch zu wenige bewertete Beiträge (ab 6 beginnt die Anpassung).", "");
  if (hinweise.length) { zeilen.push("Hinweise:"); for (const h of hinweise) zeilen.push(`  · ${h}`); zeilen.push(""); }
  if (fehler.length) { zeilen.push("Fehler der Woche:"); for (const e of fehler.slice(-10)) zeilen.push(`  · ${e}`); zeilen.push(""); }
  zeilen.push("Der Bot läuft weiter ohne dein Zutun. Pausieren: Variable IG_PAUSE=true.");
  return zeilen.join("\n");
}

export async function berichtSenden(text, betreff) {
  const { an, smtp } = CONFIG.bericht;
  if (!an || !smtp.host || !smtp.user) return { gesendet: false, grund: "SMTP nicht konfiguriert" };
  const transport = nodemailer.createTransport({ host: smtp.host, port: smtp.port, secure: smtp.port === 465, auth: { user: smtp.user, pass: smtp.pass } });
  await transport.sendMail({ from: smtp.von || smtp.user, to: an, subject: betreff, text });
  return { gesendet: true };
}
