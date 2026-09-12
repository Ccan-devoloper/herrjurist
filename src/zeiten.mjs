/* ==========================================================================
   Lernende Uhrzeiten: Wann erscheint ein Beitrag, damit er die meiste
   Reichweite bekommt?

   Statt fester Zeiten probiert der Bot die Stunden des Tages aus und merkt
   sich, was sie gebracht haben (Punkte aus insights.mjs: Follower, Saves,
   Shares, Reichweite …). Die Wahl folgt dem Prinzip „optimistisch bei
   Unsicherheit“ (UCB1): Eine Stunde ist attraktiv, wenn sie entweder gut lief
   oder noch kaum getestet wurde. Mit jedem gemessenen Beitrag wird der
   Erkundungsanteil kleiner, bis die Zeiten stehen.

   Gelernt wird getrennt nach Beitragsart (Reel oder Karussell) und, sobald
   genug Daten da sind, zusätzlich je Wochentag – Sonntagabend verhält sich
   anders als Dienstagmorgen.
   ========================================================================== */

import { punkte } from "./insights.mjs";
import { hhmm, minutenVon, lokaleMinuten } from "./zeit.mjs";
import { CONFIG } from "./config.mjs";

/** Beiträge fallen in zwei Klassen: Video oder Bild. */
export function klasseVon(format) {
  return format === "reel" ? "reel" : "karussell";
}

/* Stunde einer Veröffentlichung: bevorzugt die tatsächlich vermerkte Stunde,
   sonst die geplante Uhrzeit, sonst der Zeitstempel der Veröffentlichung – so
   zählen auch Beiträge mit, die vor der Zeit-Lernschleife entstanden sind. */
function stundeVon(eintrag) {
  if (Number.isInteger(eintrag.stunde)) return eintrag.stunde;
  if (typeof eintrag.zeit === "string" && /^\d{1,2}:\d{2}$/.test(eintrag.zeit)) return Math.floor(minutenVon(eintrag.zeit) / 60);
  if (eintrag.veroeffentlicht) {
    const d = new Date(eintrag.veroeffentlicht);
    if (!Number.isNaN(d.getTime())) return Math.floor(lokaleMinuten(d) / 60);
  }
  return null;
}

/**
 * Wertet den Ledger aus: je Klasse (und Klasse × Wochentag) je Stunde die
 * Anzahl der Beiträge und ihr mittleres Ergebnis, normiert auf den Schnitt
 * aller gemessenen Beiträge (1 = Durchschnitt).
 */
export function zeitStatistik(ledger, heute = new Date()) {
  /* Frisch veröffentlichte Beiträge haben noch kaum Zahlen. Sie mitzuzählen
     würde die Stunde bestrafen, zu der zuletzt gepostet wurde, statt sie zu
     bewerten – deshalb zählen nur Beiträge ab einem Mindestalter. */
  const reife = new Date(heute.getTime() - CONFIG.plan.zeitReifeTage * 86400000).toISOString().slice(0, 10);
  const eintraege = (ledger?.veroeffentlicht || []).filter((e) => e.art === "beitrag" && e.insights && punkte(e.insights) != null && stundeVon(e) != null && (e.datum || "9999") <= reife);
  const mittel = eintraege.length ? eintraege.reduce((a, e) => a + punkte(e.insights), 0) / eintraege.length : 0;
  const stunden = {}, tagStunden = {};
  for (const e of eintraege) {
    const k = klasseVon(e.format), h = stundeVon(e);
    const wert = mittel > 0 ? punkte(e.insights) / mittel : 1;
    const wt = new Date(`${e.datum}T12:00:00Z`).getUTCDay();
    (stunden[`${k}|${h}`] ||= []).push(wert);
    (tagStunden[`${k}|${wt}|${h}`] ||= []).push(wert);
  }
  const fassen = (roh) => Object.fromEntries(Object.entries(roh).map(([k, v]) => [k, { n: v.length, mittel: v.reduce((a, b) => a + b, 0) / v.length }]));
  /* Solange fast alle Beiträge bei null stehen (junges Konto, kaum Reichweite),
     ist der Unterschied zwischen zwei Stunden Rauschen. Dann wird nicht
     ausgenutzt, sondern weiter über den Tag verteilt ausprobiert. */
  const mitWirkung = eintraege.filter((e) => punkte(e.insights) > 0).length;
  /* Es braucht genug Beiträge mit Wirkung UND eine Wirkung, die über
     Einzelklicks hinausgeht – sonst entscheiden ein paar Aufrufe die Uhrzeit. */
  const belastbar = mitWirkung >= CONFIG.plan.zeitMindestMessungen && mittel >= CONFIG.plan.zeitMindestWirkung;
  /* Versuche je Stunde - alle Beiträge, auch die ohne Zahlen. Damit weiß die
     Erkundung, welche Stunden schon dran waren, bevor Messungen belastbar sind. */
  const versuche = {};
  let versucheGesamt = 0;
  for (const e of ledger?.veroeffentlicht || []) {
    if (e.art !== "beitrag") continue;
    const h = stundeVon(e);
    if (h == null) continue;
    versuche[`${klasseVon(e.format)}|${h}`] = (versuche[`${klasseVon(e.format)}|${h}`] || 0) + 1;
    versucheGesamt++;
  }
  return { gesamt: eintraege.length, mitWirkung, belastbar, mittelPunkte: mittel, stunden: fassen(stunden), tagStunden: fassen(tagStunden), versuche, versucheGesamt };
}

/* Vorwissen aus Studien (Stand September 2026), bevor eigene Zahlen da sind.

   Quellen, die sich weitgehend decken: Sprout Social (2 Mrd. Interaktionen,
   deutsche Auswertung), Buffer (9,6 Mio. Beiträge), Hootsuite, Later (6 Mio.),
   SocialPilot (7 Mio. Beiträge, 250.000 Reels), PostFast (23.552 Beiträge),
   dazu deutsche Ratgeber zur Zielgruppe Studierende (Social Media Akademie,
   pixx.io, ds-onlinemarketing).

   Karussells und Bildbeiträge: Vormittag 8–11 Uhr und Mittag 12–14 Uhr am
   stärksten, zweiter Gipfel abends 18–21 Uhr; Dienstag bis Donnerstag vorn,
   Wochenende schwächer.
   Reels: Abend 19–22 Uhr klar vorn, Sonntag mit den meisten Reel-Aufrufen;
   ein zweites, kleineres Fenster 8–12 Uhr. Für Studierende verschiebt sich
   der Abend nach hinten (20–23 Uhr) und das Wochenende zählt mit.

   Die Werte sind bewusst schwach (0,85–1,15): Sie ordnen die ersten Tage,
   sollen die eigenen Messungen aber nicht übertönen. Mit jedem gemessenen
   Beitrag verlieren sie an Gewicht (siehe stundenWert). */
export const VORWISSEN = {
  karussell: {
    stunden: { 6: 0.88, 7: 0.95, 8: 1.08, 9: 1.15, 10: 1.12, 11: 1.08, 12: 1.12, 13: 1.08, 14: 0.97, 15: 0.93, 16: 0.95, 17: 1.0, 18: 1.08, 19: 1.12, 20: 1.08, 21: 1.0, 22: 0.9 },
    /* Sonntag … Samstag */
    tage: [0.97, 1.0, 1.03, 1.05, 1.03, 0.97, 0.95],
  },
  reel: {
    stunden: { 6: 0.85, 7: 0.9, 8: 1.0, 9: 1.0, 10: 0.97, 11: 0.95, 12: 1.0, 13: 0.95, 14: 0.9, 15: 0.9, 16: 0.95, 17: 1.0, 18: 1.06, 19: 1.12, 20: 1.15, 21: 1.12, 22: 1.08 },
    tage: [1.05, 1.0, 1.0, 1.03, 1.03, 0.97, 1.0],
  },
};

/* Vorwissen einer Stunde: Studienwert × Wochentag, und sind die eigenen
   Follower zu dieser Stunde online (Insights), noch ein kleiner Aufschlag. */
export function vorwissen(strategie, stunde, klasse = "karussell", wochentag = null) {
  const v = VORWISSEN[klasse] || VORWISSEN.karussell;
  let wert = v.stunden[stunde] ?? 0.9;
  if (Number.isInteger(wochentag)) wert *= v.tage[wochentag] ?? 1;
  const zeiten = strategie?.besteStunden;
  if (Array.isArray(zeiten) && zeiten.some((z) => Math.floor(minutenVon(z) / 60) === stunde)) wert *= 1.15;
  return wert;
}

/* So viele Beobachtungen ist das Vorwissen wert: Nach drei gemessenen
   Beiträgen zu einer Stunde zählt die Messung halb, nach zehn fast allein. */
const VORWISSEN_GEWICHT = 3;

/**
 * Bewertet eine Stunde für eine Beitragsart: gemessenes Mittel plus
 * Erkundungsaufschlag. Der Aufschlag ist groß, solange die Stunde selten
 * getestet wurde, und schrumpft mit der Gesamtzahl der Messungen.
 */
export function stundenWert(stunde, { klasse, wochentag, statistik, strategie, erkundung = CONFIG.plan.zeitErkundung }) {
  const prior = vorwissen(strategie, stunde, klasse, wochentag);
  /* Ohne belastbare Zahlen entscheidet das Vorwissen - und ein Aufschlag für
     Stunden, die noch selten ausprobiert wurden. So beginnt der Kanal bei den
     Studienwerten und wandert von dort aus zu den Nachbarstunden, statt jeden
     Tag dieselbe Uhrzeit zu wiederholen oder wahllos zu streuen. */
  if (!statistik.belastbar) {
    const n = statistik.versuche?.[`${klasse}|${stunde}`] || 0;
    const gesamt = statistik.versucheGesamt || 0;
    const bonus = erkundung * Math.sqrt(Math.log(gesamt + 1) / (n + 1));
    return { wert: prior + bonus, mittel: prior, n, bonus };
  }
  const global = statistik.stunden[`${klasse}|${stunde}`];
  const jeTag = statistik.tagStunden[`${klasse}|${wochentag}|${stunde}`];
  /* Der Wochentag zählt erst mit, wenn es dafür mehrere Messungen gibt. */
  const n = (global?.n || 0) + (jeTag?.n || 0);
  let gemessen;
  if (!global && !jeTag) gemessen = null;
  else if (jeTag && jeTag.n >= 2) gemessen = 0.5 * (global?.mittel ?? jeTag.mittel) + 0.5 * jeTag.mittel;
  else gemessen = global?.mittel ?? jeTag.mittel;
  /* Messung und Vorwissen verschmelzen: Das Vorwissen zählt wie drei
     Beobachtungen, danach übernimmt die Messung. */
  const mittel = gemessen == null ? prior : (n * gemessen + VORWISSEN_GEWICHT * prior) / (n + VORWISSEN_GEWICHT);
  const gesamt = Math.max(1, statistik.gesamt);
  /* Auch der Erkundungsaufschlag rechnet das Vorwissen als Beobachtungen
     mit: Eine Stunde, die laut Studien gut ist, gilt nicht zusätzlich als
     "unerforscht" - sonst schlüge sie eine zehnfach gemessene Nachbarstunde. */
  const bonus = erkundung * Math.sqrt(Math.log(gesamt + 1) / (n + VORWISSEN_GEWICHT + 1));
  return { wert: mittel + bonus, mittel, n, bonus };
}

/** Erlaubte Stunden aus der Konfiguration, z. B. "6-21" → [6 … 21]. */
export function kandidatenStunden(fenster = CONFIG.plan.zeitFenster) {
  const [von, bis] = String(fenster).split("-").map(Number);
  const out = [];
  for (let h = von; h <= bis; h++) out.push(h);
  return out;
}

/**
 * Wählt die Uhrzeiten eines Tages – eine je Beitrag, in der Reihenfolge der
 * Formate. Reels und Karussells lernen getrennt. Zwischen zwei Beiträgen
 * bleibt ein Mindestabstand, damit sie sich nicht gegenseitig die Reichweite
 * nehmen; die Reihenfolge über den Tag bleibt erhalten.
 * @param {{formate:string[], datum:string, ledger:object, strategie?:object, zufall?:()=>number}} opt
 * @returns {string[]} Uhrzeiten "HH:MM"
 */
export function zeitenWaehlen({ formate, datum, ledger, strategie = null, zufall = Math.random, statistik = null }) {
  const standard = CONFIG.plan.beitragsZeiten;
  if (!CONFIG.plan.zeitLernen || !formate.length) return formate.map((_, i) => standard[i] || standard.at(-1));
  const stat = statistik || zeitStatistik(ledger);
  const wochentag = new Date(`${datum}T12:00:00Z`).getUTCDay();
  const abstand = CONFIG.plan.zeitAbstandStunden;
  const alle = kandidatenStunden();
  /* Alle Beiträge des Tages zusammen wählen, nicht einen nach dem anderen.
     Der Reihe nach gewählt nahm sich der zweite Beitrag die beste Stunde am
     frühen Abend und schob den dritten (das Reel) mit vier Stunden Abstand
     an das Ende des Fensters - 22:30 statt 20:30. Gesucht wird jetzt die
     Kombination mit der höchsten Summe, Reihenfolge und Mindestabstand
     bleiben. Bei drei Beiträgen und 17 Stunden sind das 680 Kombinationen. */
  const werte = formate.map((f) => { const klasse = klasseVon(f); const m = {}; for (const h of alle) m[h] = stundenWert(h, { klasse, wochentag, statistik: stat, strategie }).wert; return m; });
  let besteSumme = -Infinity, spitze = [];
  const suche = (i, ab, bisher, summe) => {
    if (i === formate.length) {
      if (summe > besteSumme + 1e-9) { besteSumme = summe; spitze = [bisher]; }
      else if (summe >= besteSumme - 1e-9) spitze.push(bisher);
      return;
    }
    const spaeteste = alle.at(-1) - abstand * (formate.length - 1 - i);
    for (const h of alle) { if (h < ab || h > spaeteste) continue; suche(i + 1, h + abstand, [...bisher, h], summe + werte[i][h]); }
  };
  suche(0, alle[0], [], 0);
  /* Passt der Abstand nicht in das Fenster: der Reihe nach so dicht wie möglich. */
  if (!spitze.length) { const g = []; for (let i = 0; i < formate.length; i++) g.push(Math.min(alle.at(-1), (g.at(-1) ?? alle[0] - abstand) + abstand)); return g.map((h) => hhmm(h * 60 + 30)); }
  /* Gleichauf liegende Kombinationen werden je Tag zufällig, aber
     reproduzierbar aufgelöst - so wandert die Zeit beim Ausprobieren. */
  const gewaehlt = spitze[Math.floor(zufall() * spitze.length)];
  return gewaehlt.map((h) => hhmm(h * 60 + 30));
}

/**
 * Für den Wochenbericht: die drei besten gemessenen Stunden je Klasse mit
 * Anzahl der Messungen. Zeigt, wie sicher die Wahl schon ist.
 */
export function zeitBericht(ledger) {
  const stat = zeitStatistik(ledger);
  const out = {};
  for (const klasse of ["karussell", "reel"]) {
    const zeilen = Object.entries(stat.stunden)
      .filter(([k]) => k.startsWith(`${klasse}|`))
      .map(([k, v]) => ({ stunde: Number(k.split("|")[1]), ...v }))
      .sort((a, b) => b.mittel - a.mittel)
      .slice(0, 3);
    if (zeilen.length) out[klasse] = zeilen;
  }
  return { gesamt: stat.gesamt, belastbar: stat.belastbar, mitWirkung: stat.mitWirkung, klassen: out };
}
