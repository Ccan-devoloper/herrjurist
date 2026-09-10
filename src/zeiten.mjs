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
  return { gesamt: eintraege.length, mitWirkung, belastbar, mittelPunkte: mittel, stunden: fassen(stunden), tagStunden: fassen(tagStunden) };
}

/* Vorwissen: Sind die Follower zu dieser Stunde online, ist sie einen kleinen
   Bonus wert, solange noch nichts gemessen wurde. */
function vorwissen(strategie, stunde) {
  const zeiten = strategie?.besteStunden;
  if (!Array.isArray(zeiten) || !zeiten.length) return 1;
  return zeiten.some((z) => Math.floor(minutenVon(z) / 60) === stunde) ? 1.15 : 1;
}

/**
 * Bewertet eine Stunde für eine Beitragsart: gemessenes Mittel plus
 * Erkundungsaufschlag. Der Aufschlag ist groß, solange die Stunde selten
 * getestet wurde, und schrumpft mit der Gesamtzahl der Messungen.
 */
export function stundenWert(stunde, { klasse, wochentag, statistik, strategie, erkundung = CONFIG.plan.zeitErkundung }) {
  /* Ohne belastbare Zahlen zählt nur das Vorwissen; alle Stunden starten
     gleichauf und werden der Reihe nach ausprobiert. */
  if (!statistik.belastbar) return { wert: vorwissen(strategie, stunde), mittel: vorwissen(strategie, stunde), n: 0, bonus: 0 };
  const global = statistik.stunden[`${klasse}|${stunde}`];
  const jeTag = statistik.tagStunden[`${klasse}|${wochentag}|${stunde}`];
  /* Der Wochentag zählt erst mit, wenn es dafür mehrere Messungen gibt. */
  const n = (global?.n || 0) + (jeTag?.n || 0);
  let mittel;
  if (!global && !jeTag) mittel = vorwissen(strategie, stunde);
  else if (jeTag && jeTag.n >= 2) mittel = 0.5 * (global?.mittel ?? jeTag.mittel) + 0.5 * jeTag.mittel;
  else mittel = global?.mittel ?? jeTag.mittel;
  const gesamt = Math.max(1, statistik.gesamt);
  const bonus = erkundung * Math.sqrt(Math.log(gesamt + 1) / (n + 1));
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
  const gewaehlt = [];
  for (let i = 0; i < formate.length; i++) {
    const klasse = klasseVon(formate[i]);
    /* Jeder Beitrag bekommt ein eigenes Zeitfenster, damit der Tag nicht
       zusammenrückt: Beitrag i darf frühestens abstand·i Stunden nach dem
       ersten möglichen Slot liegen und muss vor den folgenden Beiträgen bleiben. */
    const frueheste = gewaehlt.length ? gewaehlt.at(-1) + abstand : alle[0];
    const spaeteste = alle.at(-1) - abstand * (formate.length - 1 - i);
    const moeglich = alle.filter((h) => h >= frueheste && h <= spaeteste);
    if (!moeglich.length) { gewaehlt.push(Math.min(alle.at(-1), (gewaehlt.at(-1) ?? alle[0]) + abstand)); continue; }
    const bewertet = moeglich.map((h) => ({ h, ...stundenWert(h, { klasse, wochentag, statistik: stat, strategie }) }));
    const beste = Math.max(...bewertet.map((b) => b.wert));
    /* Gleichauf liegende Stunden werden je Tag zufällig, aber reproduzierbar
       aufgelöst – so wandert die Zeit beim Ausprobieren über die Woche. */
    const spitze = bewertet.filter((b) => b.wert >= beste - 1e-9);
    gewaehlt.push(spitze[Math.floor(zufall() * spitze.length)].h);
  }
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
